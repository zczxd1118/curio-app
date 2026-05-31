#!/usr/bin/env python3
"""
build_issue_md — 统一的 daily/weekly md 生成器

把 scored.json + editor_notes.json + candidates.json 拼成一份完整的 issue markdown：

  # Curio · {域} {日报|周刊}
  **{date} · 由 Curio 主编从 N 条候选选出**

  ## 📰 主编社论
  {intro}

  ## 🗞️ 头版报道（K 条）
  ### 1. {中文标题}
  **来源**：{source} · {platform}
  _原标题：{title_en}_
  🏷️ `kw1` · `kw2` · `kw3`
  **📖 中文摘要**
  {summary_zh}
  <details><summary>展开英文原文</summary>...</details>
  **📖 主编点评**
  {note}
  📺 [打开原文]({url})

  ## 📑 参考阅读
  ## ⏭ 跳过

daily 和 weekly 走同一个函数，区别只在：
- cadence="daily":  must_read 取前 3-5，标题用"日报"，时间窗口"今日"
- cadence="weekly": must_read 取前 5-8，标题用"周刊"，时间窗口"本周"

输出文件名统一是 {slug}.weekly.{date}.md（保持 render_site 兼容）。
"""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
TOPICS = ROOT / "topics"


# 每个 cadence 的选条上限和标题
CADENCE_CFG = {
    "daily": {"label": "日报", "headline_max": 5, "ref_max": 5, "window_text": "今日"},
    "weekly": {"label": "周刊", "headline_max": 8, "ref_max": 8, "window_text": "本周"},
}


def _is_english_title(title: str) -> bool:
    if not title:
        return False
    ascii_alpha = sum(1 for c in title if c.isascii() and c.isalpha())
    return ascii_alpha / max(len(title), 1) > 0.4


def _platform_label(platform: str, source_name: str = "") -> str:
    table = {
        "rss": "RSS",
        "hackernews": "HN",
        "bilibili": "B站",
    }
    p = table.get(platform, platform or "?")
    src = (source_name or "").strip()
    if not src:
        return p
    # 如果 source_name 已含平台缩写或全称，避免重复
    src_upper = src.upper()
    if (p and p.upper() in src_upper) or (platform and platform.upper() in src_upper):
        return src
    return f"{src} · {p}"


def _source_str(item: dict) -> str:
    s = item.get("source")
    if isinstance(s, dict):
        return s.get("name") or ""
    return s or ""


def _load_candidates_body_map(slug: str) -> dict[str, str]:
    """读 candidates.json，返回 {id: summary_or_body[:600]} 用于 details 折叠英文原文"""
    out: dict[str, str] = {}
    cand_path = TOPICS / f"{slug}.candidates.json"
    if not cand_path.exists():
        return out
    try:
        data = json.loads(cand_path.read_text(encoding="utf-8"))
    except Exception:
        return out
    for it in data.get("items", []) or data.get("candidates", []) or []:
        iid = it.get("id")
        if not iid:
            continue
        # 优先 summary，其次 body 前段
        body = it.get("summary") or it.get("body") or it.get("description") or ""
        if body:
            out[iid] = body[:1200]
    return out


def _load_editor_notes(slug: str) -> dict[str, str]:
    out: dict[str, str] = {}
    p = TOPICS / f"{slug}.editor_notes.json"
    if not p.exists():
        return out
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return out
    for it in data.get("notes", []) or data.get("items", []) or []:
        iid = it.get("id")
        note = (it.get("note") or "").strip()
        if iid and note:
            out[iid] = note
    return out


def _kw_chips(keywords: list[str], limit: int = 5) -> str:
    if not keywords:
        return ""
    chips = " · ".join(f"`{k}`" for k in keywords[:limit])
    return f"🏷️ {chips}"


def _render_headline_card(idx: int, item: dict, note: str, body_en: str) -> list[str]:
    title = (item.get("title") or "").strip()
    title_zh = (item.get("title_zh") or "").strip()
    keywords = item.get("keywords") or []
    summary_zh = (item.get("summary_zh") or "").strip()
    url = item.get("url") or "#"
    platform = item.get("platform") or ""
    source_name = _source_str(item)

    display_title = title_zh or title or "(无标题)"
    is_en = _is_english_title(title)

    lines = [
        f"### {idx}. {display_title}",
        "",
        f"**来源**：{_platform_label(platform, source_name)}",
        "",
    ]
    # 英文原标题（仅当中文标题与英文不同才显示）
    if is_en and title and title != display_title:
        lines += [f"_原标题：{title}_", ""]

    # 关键词 chips
    chips = _kw_chips(keywords)
    if chips:
        lines += [chips, ""]

    # 中文摘要
    if summary_zh:
        lines += ["**📖 中文摘要**", "", summary_zh, ""]

    # 英文原文 details（仅英文条目且有正文时折叠）
    if is_en and body_en:
        body_clipped = body_en.strip()
        if len(body_clipped) > 800:
            body_clipped = body_clipped[:800].rstrip() + "..."
        lines += [
            "<details><summary>展开英文原文</summary>",
            "",
            body_clipped,
            "",
            "</details>",
            "",
        ]

    # 主编点评
    if note:
        lines += ["**📖 主编点评**", "", note, ""]

    # 原文链接
    lines += [f"📺 [打开原文]({url})", "", "---", ""]
    return lines


def _render_reference_card(idx: int, item: dict) -> list[str]:
    title = (item.get("title") or "").strip()
    title_zh = (item.get("title_zh") or "").strip()
    keywords = item.get("keywords") or []
    why = (item.get("why_recommend") or "").strip()
    url = item.get("url") or ""
    platform = item.get("platform") or ""
    source_name = _source_str(item)

    display_title = title_zh or title or "(无标题)"
    is_en = _is_english_title(title)

    head = f"**{idx}. {display_title}**　_{_platform_label(platform, source_name)}_"
    out = [head]
    if is_en and title and title != display_title:
        out.append(f"_原标题：{title}_")
    chips = _kw_chips(keywords, limit=4)
    if chips:
        out.append(chips)
    if why:
        out.append(f"- {why}")
    if url:
        out.append(f"- [打开]({url})")
    out.append("")
    return out


def _render_skip_block(skip: list[dict], stats_total: int = 0) -> list[str]:
    if not skip:
        return []
    SKIP_PREVIEW = 5
    rest = max(0, len(skip) - SKIP_PREVIEW)
    lines = [
        f"## ⏭ 跳过（{stats_total or len(skip)} 条）",
        "",
        f"_展示前 {min(SKIP_PREVIEW, len(skip))} 条跳过理由_",
        "",
    ]
    for s in skip[:SKIP_PREVIEW]:
        title = (s.get("title") or "?")[:80]
        reason = (s.get("skip_reason") or "").strip()
        lines.append(f"- **{title}**　_{reason}_")
    if rest > 0:
        lines += ["", f"<details><summary>展开剩余 {rest} 条</summary>", ""]
        for s in skip[SKIP_PREVIEW:]:
            title = (s.get("title") or "?")[:80]
            reason = (s.get("skip_reason") or "").strip()
            lines.append(f"- **{title}**　_{reason}_")
        lines += ["", "</details>"]
    lines += ["", "---", ""]
    return lines


def build_issue_md(
    scored: dict,
    cadence: str = "weekly",
    *,
    slug: str | None = None,
    today: str | None = None,
) -> str:
    """生成统一格式的 issue markdown 文本"""
    cfg = CADENCE_CFG.get(cadence, CADENCE_CFG["weekly"])
    today = today or dt.date.today().isoformat()
    domain = scored.get("domain", "未命名领域")
    slug = slug or scored.get("domain_id") or _slugify_zh(domain)

    must = (scored.get("must_read") or [])[: cfg["headline_max"]]
    ref = (scored.get("reference") or [])[: cfg["ref_max"]]
    skip = scored.get("skip") or []
    intro = (scored.get("intro") or "").strip()
    stats = scored.get("stats") or {}
    candidates_total = stats.get("candidates_total") or "?"
    skip_total = stats.get("skip_count_actual") or len(skip)

    # 加载补充数据
    candidates_body = _load_candidates_body_map(slug)
    editor_notes = _load_editor_notes(slug)

    label = cfg["label"]
    window = cfg["window_text"]

    lines: list[str] = [
        f"# Curio · {domain} {label}",
        "",
        f"**{today} · 由 Curio 主编从 {candidates_total} 条候选选出（{window}窗口）**",
        "",
        "---",
        "",
        "## 📰 主编社论",
        "",
        intro or "_（本期无社论）_",
        "",
        "---",
        "",
        f"## 🗞️ 头版报道（{len(must)} 条）",
        "",
    ]

    for i, m in enumerate(must, 1):
        iid = m.get("id") or ""
        body_en = candidates_body.get(iid, "")
        note = editor_notes.get(iid, "")
        lines += _render_headline_card(i, m, note=note, body_en=body_en)

    if ref:
        lines += [f"## 📑 参考阅读（{len(ref)} 条）", ""]
        for i, r in enumerate(ref, 1):
            lines += _render_reference_card(i, r)
        lines += ["---", ""]

    lines += _render_skip_block(skip, stats_total=skip_total)

    # 反馈区由 render_site 注入交互组件，这里给个占位段（render_site 会砍掉）
    lines += [
        "## 📝 本期反馈",
        "",
        "_（网页底部交互式反馈）_",
        "",
        "---",
        "",
        f"_Curio · {today} · {label}_",
    ]
    return "\n".join(lines)


def _slugify_zh(s: str) -> str:
    return re.sub(r"[^\w\u4e00-\u9fa5]+", "-", (s or "").lower()).strip("-")


# -------------------- CLI --------------------

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True, help="领域 slug，如 finance / ai")
    ap.add_argument("--cadence", choices=["daily", "weekly"], default="weekly")
    ap.add_argument("--date", default=None, help="覆盖日期（默认今天）")
    ap.add_argument("--out", default=None, help="输出文件，默认 topics/{slug}.weekly.{date}.md")
    args = ap.parse_args()

    scored_path = TOPICS / f"{args.slug}.scored.json"
    if not scored_path.exists():
        print(f"❌ 找不到 {scored_path}", file=sys.stderr)
        return 1
    scored = json.loads(scored_path.read_text(encoding="utf-8"))

    today = args.date or dt.date.today().isoformat()
    md = build_issue_md(scored, cadence=args.cadence, slug=args.slug, today=today)

    out_path = Path(args.out) if args.out else TOPICS / f"{args.slug}.weekly.{today}.md"
    out_path.write_text(md, encoding="utf-8")
    print(f"✅ 写出 {out_path}")
    print(f"   头版 {len((scored.get('must_read') or [])[:CADENCE_CFG[args.cadence]['headline_max']])} · "
          f"参考 {len((scored.get('reference') or [])[:CADENCE_CFG[args.cadence]['ref_max']])} · "
          f"跳过 {len(scored.get('skip') or [])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
