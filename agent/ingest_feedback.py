#!/usr/bin/env python3
"""
反馈蒸馏到 profile.yaml —— 双源
  1. 远端：从 GitHub Issues 拉（需 .gh_pat）
  2. 本地：扫 feedback/*.json （--local，不需 PAT，回路兜底）

两种源都会：
  - 蒸馏成一行 text，追加到 profile.yaml.feedback_timeline 头部
  - 把 long_term.more/less/format 真的合并进 signal_preferences / dislikes / signal_preferences
  - 在 timeline 条目上写明 applied: [...]
  - auto_updated_from_feedback: true

用法：
  python -m agent.ingest_feedback              # GitHub 模式
  python -m agent.ingest_feedback --local      # 本地 feedback/*.json
  python -m agent.ingest_feedback --local --dry-run
"""

from __future__ import annotations
import argparse
import json
import re
import shutil
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path
from typing import Optional, Union

ROOT = Path(__file__).resolve().parent.parent
PAT_FILE = ROOT / ".gh_pat"
PROFILE = ROOT / "profile.yaml"
FEEDBACK_DIR = ROOT / "feedback"
INGESTED_DIR = FEEDBACK_DIR / "ingested"
GH_OWNER = "zczxd1118"
GH_REPO = "curio-app"
LABEL_OPEN = "curio-feedback"
LABEL_DONE = "curio-ingested"

# —— 蒸馏后真的会写进 Profile 的字段映射 ——
PROFILE_FIELD_MAP = {
    "more":   "signal_preferences",   # 想多看 → 加到 signal_preferences
    "less":   "dislikes",              # 不想看 → 加到 dislikes
    "format": "signal_preferences",   # 笔法偏好 → 也归到 signal_preferences（带"笔法："前缀）
}


# ============================================================
# 通用：蒸馏 + Profile 合并
# ============================================================

def distill_to_text(parsed: dict) -> str:
    """结构化反馈 → 一行人类可读文字（写进 timeline.text）"""
    parts = []
    items = parsed.get("items") or []
    if items:
        good = [i for i in items if i.get("rating") == "useful"]
        bad  = [i for i in items if i.get("rating") == "off"]
        meh  = [i for i in items if i.get("rating") == "meh"]
        if good: parts.append("👍 " + " / ".join((i.get("title") or "")[:40] for i in good))
        if bad:  parts.append("👎 " + " / ".join((i.get("title") or "")[:40] for i in bad))
        if meh:  parts.append("😐 " + " / ".join((i.get("title") or "")[:40] for i in meh))
        notes = [i.get("note") for i in items if i.get("note")]
        if notes:
            parts.append("备注: " + " | ".join(notes))
    lt = parsed.get("long_term") or {}
    if lt.get("more"):   parts.append("想多看: " + lt["more"])
    if lt.get("less"):   parts.append("不想看: " + lt["less"])
    if lt.get("format"): parts.append("笔法: " + lt["format"])
    return " · ".join(parts) if parts else "(空反馈)"


def apply_long_term_to_profile(profile: dict, long_term: dict) -> list[str]:
    """
    把 long_term.{more,less,format} 真的合并进 profile 的 list 字段。
    返回 applied 描述列表（人话），用于写到 timeline 条目上。
    """
    applied: list[str] = []
    if not long_term:
        return applied

    def ensure_list(key: str) -> list:
        v = profile.get(key)
        if not isinstance(v, list):
            v = []
            profile[key] = v
        return v

    def add_if_new(target_key: str, value: str, label: str = "") -> bool:
        items = ensure_list(target_key)
        v = (value or "").strip()
        if not v:
            return False
        # 加前缀（笔法用）
        entry = f"{label}：{v}" if label else v
        # 去重：完全相同 / 包含关系都算重复
        for it in items:
            if isinstance(it, str) and (it == entry or v in it):
                return False
        items.append(entry)
        return True

    if long_term.get("more"):
        if add_if_new("signal_preferences", long_term["more"]):
            applied.append(f'signal_preferences += "{long_term["more"]}"')
    if long_term.get("less"):
        if add_if_new("dislikes", long_term["less"]):
            applied.append(f'dislikes += "{long_term["less"]}"')
    if long_term.get("format"):
        if add_if_new("signal_preferences", long_term["format"], label="笔法"):
            applied.append(f'signal_preferences += "笔法：{long_term["format"]}"')
    return applied


def dedupe_timeline(timeline: list[dict]) -> list[dict]:
    """同一天 + 同一 issue + 同一 text 的条目只保留第一条"""
    seen: set[tuple] = set()
    out: list[dict] = []
    for e in timeline:
        key = (
            str(e.get("date") or "")[:10],
            e.get("issue") or e.get("issue_id") or "",
            (e.get("text") or "").strip(),
        )
        if key in seen:
            continue
        seen.add(key)
        out.append(e)
    return out


def write_profile(profile: dict, dry_run: bool):
    import yaml
    profile["auto_updated_from_feedback"] = True
    if dry_run:
        print("[dry-run] 不写盘。预览将写入的关键字段：")
        for k in ("signal_preferences", "dislikes", "auto_updated_from_feedback"):
            print(f"  {k}: {profile.get(k)}")
        print("  feedback_timeline[:3]:")
        for e in (profile.get("feedback_timeline") or [])[:3]:
            print(f"    - {e}")
        return
    PROFILE.write_text(
        yaml.safe_dump(profile, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    print(f"  ✅ profile.yaml 已更新")


# ============================================================
# 远端：GitHub Issues
# ============================================================

def _pat() -> str:
    """读 GitHub token：env 优先（CI），文件 fallback（本地）"""
    import os as _os
    pat = _os.environ.get("GH_TOKEN") or _os.environ.get("GITHUB_TOKEN")
    if pat:
        return pat
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
    issues = _api(f"/issues?labels={LABEL_OPEN}&state=open&per_page=50")
    return [i for i in issues if "pull_request" not in i]


def parse_yaml_block(body: str) -> dict | None:
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


def close_issue(number: int, dry_run: bool):
    if dry_run:
        print(f"  [dry-run] 将关闭 Issue #{number} 并加 label {LABEL_DONE}")
        return
    try:
        _api(f"/issues/{number}/labels", "POST", body={"labels": [LABEL_DONE]})
    except Exception:
        pass
    try:
        _api(f"/issues/{number}/comments", "POST",
             body={"body": "✅ Curio 已读取这条反馈并合并到 profile.yaml。"})
    except Exception:
        pass
    _api(f"/issues/{number}", "PATCH", body={"state": "closed"})
    print(f"  ✅ Issue #{number} 已关闭")


# ============================================================
# 处理一条 parsed 反馈 —— 共用入口
# ============================================================

def process_one(parsed: dict, profile: dict, source_tag: str) -> dict:
    """
    返回一个新 timeline 条目（含 applied）。
    同时副作用：在 profile 上合并 long_term 偏好。
    """
    text = distill_to_text(parsed)
    long_term = parsed.get("long_term") or {}
    applied = apply_long_term_to_profile(profile, long_term)
    return {
        "date": (parsed.get("submitted_at") or "")[:10] or datetime.now().strftime("%Y-%m-%d"),
        "issue": parsed.get("issue_id", "?"),
        "source": source_tag,           # github / local
        "text": text,
        "applied": applied,
    }


# ============================================================
# 主流程：远端
# ============================================================

def run_github(dry_run: bool) -> int:
    import yaml
    print(f"[ingest_feedback] GitHub 模式 → {GH_OWNER}/{GH_REPO} label={LABEL_OPEN}")
    if not _pat():
        print("⚠️ 没有 .gh_pat，跳过 GitHub 拉取（如果你只想跑本地，请加 --local）")
        return 0
    try:
        issues = fetch_open_feedback()
    except Exception as e:
        print(f"⚠️ 拉取失败: {e}")
        return 0
    if not issues:
        print("  没有待处理的 GitHub 反馈 Issue")
        return 0
    print(f"  找到 {len(issues)} 条待处理")

    profile = yaml.safe_load(PROFILE.read_text(encoding="utf-8")) or {}
    new_entries: list[dict] = []
    closed_numbers: list[int] = []
    for it in issues:
        num = it["number"]
        body = it.get("body") or ""
        print(f"  Issue #{num}: {it['title'][:60]}")
        parsed = parse_yaml_block(body)
        if not parsed:
            print(f"    无法解析 body，跳过（不关闭）")
            continue
        entry = process_one(parsed, profile, source_tag=f"github#{num}")
        new_entries.append(entry)
        closed_numbers.append(num)
        print(f"    → text: {entry['text'][:120]}")
        if entry["applied"]:
            print(f"    → applied: {entry['applied']}")

    if new_entries:
        timeline = profile.get("feedback_timeline") or []
        timeline = new_entries + timeline
        timeline = dedupe_timeline(timeline)[:50]
        profile["feedback_timeline"] = timeline
        write_profile(profile, dry_run)
        for n in closed_numbers:
            close_issue(n, dry_run)
    print(f"[ingest_feedback] GitHub 完成：处理 {len(new_entries)} 条")
    return 0


# ============================================================
# 主流程：本地 feedback/*.json
# ============================================================

def run_local(dry_run: bool) -> int:
    import yaml
    print(f"[ingest_feedback] 本地模式 → {FEEDBACK_DIR}")
    if not FEEDBACK_DIR.exists():
        print("  feedback/ 不存在，跳过")
        return 0
    files = sorted([p for p in FEEDBACK_DIR.glob("*.json") if p.is_file()])
    if not files:
        print("  没有待处理的本地 feedback json")
        return 0
    print(f"  找到 {len(files)} 个 json")

    profile = yaml.safe_load(PROFILE.read_text(encoding="utf-8")) or {}

    # 先把已有的 timeline 去重一遍（你 profile 里有 3 条 5/30 重复条目）
    before = profile.get("feedback_timeline") or []
    after = dedupe_timeline(before)
    if len(after) != len(before):
        print(f"  📐 现有 timeline 去重: {len(before)} → {len(after)}")
        profile["feedback_timeline"] = after

    new_entries: list[dict] = []
    moved: list[Path] = []
    for fp in files:
        try:
            parsed = json.loads(fp.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  ⚠️ {fp.name} 解析失败: {e}")
            continue
        print(f"  📄 {fp.name}: issue={parsed.get('issue_id')}")
        entry = process_one(parsed, profile, source_tag=f"local:{fp.name}")
        new_entries.append(entry)
        moved.append(fp)
        print(f"    → text: {entry['text'][:120]}")
        if entry["applied"]:
            print(f"    → applied: {entry['applied']}")
        else:
            print(f"    → applied: (无新偏好，可能已合并过)")

    if new_entries:
        timeline = profile.get("feedback_timeline") or []
        timeline = new_entries + timeline
        timeline = dedupe_timeline(timeline)[:50]
        profile["feedback_timeline"] = timeline
        write_profile(profile, dry_run)

    # 归档
    if not dry_run and moved:
        today = datetime.now().strftime("%Y-%m-%d")
        archive = INGESTED_DIR / today
        archive.mkdir(parents=True, exist_ok=True)
        for fp in moved:
            target = archive / fp.name
            shutil.move(str(fp), str(target))
            print(f"  📦 归档 {fp.name} → feedback/ingested/{today}/")
    elif dry_run and moved:
        print(f"  [dry-run] 将归档 {len(moved)} 个 json 到 feedback/ingested/")

    print(f"[ingest_feedback] 本地完成：处理 {len(new_entries)} 条")
    return 0


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--local", action="store_true", help="扫 feedback/*.json 而不是 GitHub Issues")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.local:
        return run_local(args.dry_run)
    return run_github(args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
