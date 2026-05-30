#!/usr/bin/env python3
"""
从 GitHub Issues 拉取反馈 → 蒸馏到 profile.yaml.feedback_timeline → 关闭 Issue

用法：
  python -m agent.ingest_feedback
  python -m agent.ingest_feedback --dry-run    # 只打印不修改

约定：
  - 反馈 Issue 必须带 label 'curio-feedback'
  - body 内有 ```yaml ... ``` 块，结构由 render_site.js 拼出
  - 处理完后给 Issue 加 'curio-ingested' label 并 close
"""

from __future__ import annotations
import argparse
import json
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional, Union

ROOT = Path(__file__).resolve().parent.parent
PAT_FILE = ROOT / ".gh_pat"
PROFILE = ROOT / "profile.yaml"
GH_OWNER = "zczxd1118"
GH_REPO = "curio-app"
LABEL_OPEN = "curio-feedback"
LABEL_DONE = "curio-ingested"


def _pat() -> str:
    if not PAT_FILE.exists():
        return ""
    return PAT_FILE.read_text().strip()


def _api(path: str, method: str = "GET", body: Optional[dict] = None) -> Union[dict, list]:
    pat = _pat()
    if not pat:
        raise RuntimeError(".gh_pat 不存在或为空")
    url = f"https://api.github.com/repos/{GH_OWNER}/{GH_REPO}{path}"
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"token {pat}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "curio-bot")
    if data:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"  HTTP {e.code}: {e.read().decode()[:200]}", file=sys.stderr)
        raise


def fetch_open_feedback() -> list[dict]:
    """拉所有 open + 带 curio-feedback label 的 Issue"""
    issues = _api(f"/issues?labels={LABEL_OPEN}&state=open&per_page=50")
    return [i for i in issues if "pull_request" not in i]


def parse_yaml_block(body: str) -> dict | None:
    """从 Issue body 里提取 ```yaml ... ``` 块"""
    m = re.search(r"```yaml\s*\n(.*?)\n```", body, re.S)
    if not m:
        return None
    raw = m.group(1)
    try:
        import yaml
        return yaml.safe_load(raw)
    except Exception as e:
        print(f"  parse yaml failed: {e}", file=sys.stderr)
        return None


def distill_to_text(parsed: dict) -> str:
    """把结构化反馈压成一行人类可读 + 可被 Claude 利用的文字"""
    parts = []
    items = parsed.get("items", []) or []
    if items:
        good = [i for i in items if (i.get("rating") == "useful")]
        bad = [i for i in items if (i.get("rating") == "off")]
        meh = [i for i in items if (i.get("rating") == "meh")]
        if good:
            parts.append("👍 " + " / ".join((i.get("title") or "")[:40] for i in good))
        if bad:
            parts.append("👎 " + " / ".join((i.get("title") or "")[:40] for i in bad))
        if meh:
            parts.append("😐 " + " / ".join((i.get("title") or "")[:40] for i in meh))
        notes = [i.get("note") for i in items if i.get("note")]
        if notes:
            parts.append("备注: " + " | ".join(notes))
    lt = parsed.get("long_term") or {}
    if lt.get("more"):
        parts.append("想多看: " + lt["more"])
    if lt.get("less"):
        parts.append("不想看: " + lt["less"])
    if lt.get("format"):
        parts.append("笔法: " + lt["format"])
    return " · ".join(parts) if parts else "(空反馈)"


def update_profile(entries: list[dict], dry_run: bool = False):
    """把蒸馏后的反馈追加到 profile.yaml.feedback_timeline 头部"""
    import yaml
    profile = yaml.safe_load(PROFILE.read_text(encoding="utf-8")) or {}
    timeline = profile.get("feedback_timeline", []) or []
    new_entries = [
        {"date": e["submitted_at"][:10], "issue_id": e["issue_id"], "text": e["text"], "github_issue": e["gh_number"]}
        for e in entries
    ]
    timeline = new_entries + timeline
    profile["feedback_timeline"] = timeline[:50]   # 最多保留 50 条
    if dry_run:
        print("[dry-run] 将写入 profile.yaml.feedback_timeline 头部:")
        for e in new_entries:
            print(f"  - [{e['date']}] {e['text']}")
        return
    PROFILE.write_text(
        yaml.safe_dump(profile, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    print(f"  ✅ profile.yaml 更新（追加 {len(new_entries)} 条到 timeline）")


def close_issue(number: int, dry_run: bool = False):
    """给 Issue 加 ingested label + close"""
    if dry_run:
        print(f"  [dry-run] 将关闭 Issue #{number} 并加 label {LABEL_DONE}")
        return
    # 加 label
    try:
        _api(f"/issues/{number}/labels", "POST", body={"labels": [LABEL_DONE]})
    except Exception:
        pass
    # 评论 + close
    try:
        _api(f"/issues/{number}/comments", "POST",
             body={"body": "✅ Curio 已读取这条反馈并合并到 profile.yaml。"})
    except Exception:
        pass
    _api(f"/issues/{number}", "PATCH", body={"state": "closed"})
    print(f"  ✅ Issue #{number} 已关闭")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print(f"[ingest_feedback] 拉取 GitHub {GH_OWNER}/{GH_REPO} 的 {LABEL_OPEN} Issues...")
    if not _pat():
        print("⚠️ 没有 .gh_pat，跳过反馈拉取（这是正常的，如果你还没设置）")
        return 0

    try:
        issues = fetch_open_feedback()
    except Exception as e:
        print(f"⚠️ 拉取失败: {e}")
        return 0

    if not issues:
        print("  没有待处理的反馈 Issue")
        return 0

    print(f"  找到 {len(issues)} 条待处理")

    entries = []
    for it in issues:
        num = it["number"]
        title = it["title"]
        body = it.get("body") or ""
        print(f"  Issue #{num}: {title[:60]}")
        parsed = parse_yaml_block(body)
        if not parsed:
            print(f"    无法解析 body，跳过（不关闭）")
            continue
        text = distill_to_text(parsed)
        entries.append({
            "issue_id": parsed.get("issue_id", "?"),
            "submitted_at": parsed.get("submitted_at") or time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "text": text,
            "gh_number": num,
        })
        print(f"    → {text[:120]}")

    if entries:
        update_profile(entries, args.dry_run)
        for e in entries:
            close_issue(e["gh_number"], args.dry_run)

    print(f"[ingest_feedback] 完成：处理 {len(entries)} 条反馈")
    return 0


if __name__ == "__main__":
    sys.exit(main())
