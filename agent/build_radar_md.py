"""Curio · Trend Radar 统一渲染器

读 unified.scored.json → 出一份 markdown（Top 4-5 头条 + 备选池）。
对应每天 12:00 daily / 每周一 12:00 weekly 的输出。

格式（借鉴 Starfan 趋势雷达）：
  # Curio 趋势雷达 · {date}
  > intro 一段

  ## 今日精选
  ### 1. [域] 标题
  > 引子段
  | 已确认 | 尚属判断 |
  | --- | --- |
  | ... | ... |
  📖 主编点评：xxx
  📺 [打开原文](url)

  ## 备选池
  ### AI
  - 标题（一句话点评）
"""
from __future__ import annotations

import json
from typing import Any


STARS_MAP = {5: "⭐⭐⭐⭐⭐", 4: "⭐⭐⭐⭐", 3: "⭐⭐⭐"}


def build_radar_md(scored: dict[str, Any]) -> str:
    """读 unified.scored.json dict → 输出 markdown"""
    date = scored.get("date", "")
    intro = (scored.get("intro") or "").strip()
    headlines = scored.get("headlines") or []
    shortlist = scored.get("shortlist") or []

    lines: list[str] = []

    # 头部
    lines.append(f"# Curio 趋势雷达 · {date}")
    lines.append("")
    lines.append(f"> 你的私人主编 · 今日跨域精选 {len(headlines)} 条头条 + {len(shortlist)} 条备选")
    lines.append("")
    if intro:
        lines.append(f"_{intro}_")
        lines.append("")
    lines.append("---")
    lines.append("")

    # 头条区
    lines.append("## 🌟 今日精选")
    lines.append("")
    for h in headlines:
        rank = h.get("rank", "?")
        domain = h.get("domain", "")
        stars = STARS_MAP.get(h.get("stars", 4), "⭐⭐⭐⭐")
        title = h.get("title", "").strip()
        lead = (h.get("lead") or "").strip()
        confirmed = h.get("confirmed", []) or []
        judgment = h.get("judgment", []) or []
        implication = (h.get("implication") or "").strip()
        url = h.get("url", "")
        source = h.get("source", "")

        lines.append(f"### {rank}. {title}")
        lines.append("")
        lines.append(f"**[{domain}]** · {stars} · _{source}_")
        lines.append("")
        if lead:
            lines.append(lead)
            lines.append("")

        # 二维表（已确认 vs 尚属判断）
        if confirmed or judgment:
            lines.append("| ✅ 已确认 | ⚖️ 尚属判断 |")
            lines.append("|---|---|")
            max_rows = max(len(confirmed), len(judgment))
            for i in range(max_rows):
                left = confirmed[i] if i < len(confirmed) else ""
                right = judgment[i] if i < len(judgment) else ""
                # markdown 表格里的 | 要转义
                left_safe = str(left).replace("|", "\\|").replace("\n", " ")
                right_safe = str(right).replace("|", "\\|").replace("\n", " ")
                lines.append(f"| {left_safe} | {right_safe} |")
            lines.append("")

        if implication:
            lines.append(f"**📖 主编点评**")
            lines.append("")
            lines.append(implication)
            lines.append("")

        if url:
            lines.append(f"📺 [打开原文]({url})")
            lines.append("")

        lines.append("---")
        lines.append("")

    # 备选池
    if shortlist:
        lines.append("## 📋 备选池")
        lines.append("")
        # 按 domain 自然分组
        by_domain: dict[str, list] = {}
        for s in shortlist:
            d = s.get("domain", "其他")
            by_domain.setdefault(d, []).append(s)

        for d, items in by_domain.items():
            lines.append(f"### {d}")
            lines.append("")
            for it in items:
                title = it.get("title", "").strip()
                url = it.get("url", "")
                source = it.get("source", "")
                one_liner = (it.get("one_liner") or "").strip()
                title_link = f"[{title}]({url})" if url else title
                if one_liner:
                    lines.append(f"- {title_link} —— {one_liner}")
                else:
                    lines.append(f"- {title_link}")
                if source:
                    lines.append(f"  _{source}_")
            lines.append("")

    # 反馈区
    lines.append("---")
    lines.append("")
    lines.append("## 💬 反馈")
    lines.append("")
    lines.append("觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。")
    lines.append("")

    return "\n".join(lines)


# CLI 入口（手测用）
if __name__ == "__main__":
    import sys
    from pathlib import Path
    if len(sys.argv) < 2:
        print("usage: python -m agent.build_radar_md <unified.scored.json>")
        sys.exit(1)
    p = Path(sys.argv[1])
    scored = json.loads(p.read_text(encoding="utf-8"))
    md = build_radar_md(scored)
    print(md)
