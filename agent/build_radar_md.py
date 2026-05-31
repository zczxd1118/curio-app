"""Curio · Trend Radar 统一渲染器

读 unified.scored.json → 输出两类 md：
1. build_radar_md(scored)            —— 完整版（按域分组的全景，写到 topics/radar.{date}.md）
2. split_by_domain(scored, slug_map) —— 拆分版（每域一份 md，复用现有 site/邮件链路）

设计要点：
- Claude 一次跑（unified.scored.json 是单一来源）
- 展示按域分组（用户明确要求"不能全混在一起"）
- 拆分后写到 topics/{slug}.weekly.{date}.md，render_site / 邮件 broadcast 自动消费

格式（借鉴 Starfan 趋势雷达）：
  ### N. 标题
  **[域]** · ⭐⭐⭐⭐ · 来源
  > 引子段
  | ✅ 已确认 | ⚖️ 尚属判断 |
  📖 主编点评：xxx
  📺 [打开原文](url)
"""
from __future__ import annotations

import json
from typing import Any


STARS_MAP = {5: "⭐⭐⭐⭐⭐", 4: "⭐⭐⭐⭐", 3: "⭐⭐⭐"}


def _render_headline_block(h: dict[str, Any], show_rank: bool = True) -> list[str]:
    """渲染单条头条（被两个调用方共用）"""
    lines: list[str] = []
    rank = h.get("rank", "?")
    domain = h.get("domain", "")
    stars = STARS_MAP.get(h.get("stars", 4), "⭐⭐⭐⭐")
    title = (h.get("title") or "").strip()
    lead = (h.get("lead") or "").strip()
    confirmed = h.get("confirmed", []) or []
    judgment = h.get("judgment", []) or []
    implication = (h.get("implication") or "").strip()
    url = h.get("url", "")
    source = h.get("source", "")

    if show_rank:
        lines.append(f"### {rank}. {title}")
    else:
        lines.append(f"### {title}")
    lines.append("")
    meta_parts = []
    if domain:
        meta_parts.append(f"**[{domain}]**")
    meta_parts.append(stars)
    if source:
        meta_parts.append(f"_{source}_")
    lines.append(" · ".join(meta_parts))
    lines.append("")

    if lead:
        lines.append(lead)
        lines.append("")

    if confirmed or judgment:
        lines.append("| ✅ 已确认 | ⚖️ 尚属判断 |")
        lines.append("|---|---|")
        max_rows = max(len(confirmed), len(judgment))
        for i in range(max_rows):
            left = confirmed[i] if i < len(confirmed) else ""
            right = judgment[i] if i < len(judgment) else ""
            left_safe = str(left).replace("|", "\\|").replace("\n", " ")
            right_safe = str(right).replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {left_safe} | {right_safe} |")
        lines.append("")

    if implication:
        lines.append("**📖 主编点评**")
        lines.append("")
        lines.append(implication)
        lines.append("")

    if url:
        lines.append(f"📺 [打开原文]({url})")
        lines.append("")

    return lines


def build_radar_md(scored: dict[str, Any]) -> str:
    """完整全景版（按域分组渲染，不混排）"""
    date = scored.get("date", "")
    intro = (scored.get("intro") or "").strip()
    headlines = scored.get("headlines") or []
    shortlist = scored.get("shortlist") or []

    lines: list[str] = []

    lines.append(f"# Curio 趋势雷达 · {date}")
    lines.append("")
    lines.append(f"> 你的私人主编 · 今日跨域精选 {len(headlines)} 条头条 + {len(shortlist)} 条备选")
    lines.append("")
    if intro:
        lines.append(f"_{intro}_")
        lines.append("")
    lines.append("---")
    lines.append("")

    # 按 domain 分组头条（用户要求"不能全混在一起"）
    headlines_by_domain: dict[str, list] = {}
    for h in headlines:
        d = h.get("domain", "其他")
        headlines_by_domain.setdefault(d, []).append(h)

    for d, items in headlines_by_domain.items():
        lines.append(f"## 🌟 {d}")
        lines.append("")
        for h in items:
            lines.extend(_render_headline_block(h, show_rank=True))
            lines.append("---")
            lines.append("")

    # 备选池：也按域分组
    if shortlist:
        lines.append("## 📋 备选池")
        lines.append("")
        by_domain: dict[str, list] = {}
        for s in shortlist:
            d = s.get("domain", "其他")
            by_domain.setdefault(d, []).append(s)

        for d, items in by_domain.items():
            lines.append(f"### {d}")
            lines.append("")
            for it in items:
                title = (it.get("title") or "").strip()
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

    lines.append("---")
    lines.append("")
    lines.append("## 💬 反馈")
    lines.append("")
    lines.append("觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。")
    lines.append("")

    return "\n".join(lines)


def split_by_domain(
    scored: dict[str, Any],
    domain_to_slug: dict[str, str],
) -> dict[str, str]:
    """把 unified.scored.json 拆成每个域一份 md。

    Args:
        scored: unified.scored.json 内容
        domain_to_slug: 中文域名 → 英文 slug 映射，例如 {"AI / 科技": "ai", "金融": "finance"}

    Returns:
        dict {slug: markdown_content}，可直接写到 topics/{slug}.weekly.{date}.md
    """
    date = scored.get("date", "")
    intro = (scored.get("intro") or "").strip()
    headlines = scored.get("headlines") or []
    shortlist = scored.get("shortlist") or []

    # 按域分组
    headlines_by_domain: dict[str, list] = {}
    for h in headlines:
        d = h.get("domain", "其他")
        headlines_by_domain.setdefault(d, []).append(h)

    shortlist_by_domain: dict[str, list] = {}
    for s in shortlist:
        d = s.get("domain", "其他")
        shortlist_by_domain.setdefault(d, []).append(s)

    # 收集所有出现过的域
    all_domains = set(headlines_by_domain.keys()) | set(shortlist_by_domain.keys())

    out: dict[str, str] = {}
    for domain in all_domains:
        # 找对应 slug：先精确匹配，再 fuzzy（中文 -> 英文）
        slug = domain_to_slug.get(domain)
        if not slug:
            # fuzzy 匹配：去除域名里 " / 科技" 这种装饰
            for k, v in domain_to_slug.items():
                if domain in k or k in domain:
                    slug = v
                    break
        if not slug:
            # 兜底：用 domain 作 slug（可能是英文）
            slug = domain.lower().replace(" ", "-").replace("/", "-")

        domain_headlines = headlines_by_domain.get(domain, [])
        domain_shortlist = shortlist_by_domain.get(domain, [])

        if not domain_headlines and not domain_shortlist:
            continue

        lines: list[str] = []
        lines.append(f"# Curio · {domain} · {date}")
        lines.append("")
        lines.append(f"> 今日 {len(domain_headlines)} 条头条 + {len(domain_shortlist)} 条备选")
        lines.append("")
        if intro:
            lines.append(f"_{intro}_")
            lines.append("")
        lines.append("---")
        lines.append("")

        # 该域的头条
        if domain_headlines:
            lines.append("## 🌟 今日精选")
            lines.append("")
            for h in domain_headlines:
                lines.extend(_render_headline_block(h, show_rank=True))
                lines.append("---")
                lines.append("")

        # 该域的备选
        if domain_shortlist:
            lines.append("## 📋 备选阅读")
            lines.append("")
            for it in domain_shortlist:
                title = (it.get("title") or "").strip()
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

        # 反馈
        lines.append("---")
        lines.append("")
        lines.append(f"## 💬 觉得 {domain} 这期怎么样？")
        lines.append("")
        lines.append(f"[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。")
        lines.append("")

        out[slug] = "\n".join(lines)

    return out


def build_email_html(scored: dict[str, Any], domain_filter: list[str] | None = None) -> str:
    """生成邮件 HTML（用户订阅了哪些域，就发哪些域的内容；按域分组）

    Args:
        scored: unified.scored.json
        domain_filter: 用户订阅的 domain_id 列表（如 ["ai", "finance"]）；None 表示全部

    Returns:
        HTML 字符串（仅正文，不含 <html><body> 外壳——交给 worker 包装）
    """
    date = scored.get("date", "")
    intro = (scored.get("intro") or "").strip()
    headlines = scored.get("headlines") or []
    shortlist = scored.get("shortlist") or []

    # 按域分组
    headlines_by_domain: dict[str, list] = {}
    for h in headlines:
        # h 里 domain 是中文名，但匹配用 domain_id（如果有）
        d = h.get("domain", "其他")
        headlines_by_domain.setdefault(d, []).append(h)

    shortlist_by_domain: dict[str, list] = {}
    for s in shortlist:
        d = s.get("domain", "其他")
        shortlist_by_domain.setdefault(d, []).append(s)

    parts: list[str] = []

    if intro:
        parts.append(
            f'<p style="background:#fafaf8;border-left:3px solid #d4af37;padding:12px 16px;'
            f'margin:16px 0;font-style:italic;color:#444">{intro}</p>'
        )

    # 收集所有出现过的域 + 按用户订阅过滤
    all_domains = list(headlines_by_domain.keys()) + [
        d for d in shortlist_by_domain if d not in headlines_by_domain
    ]

    if domain_filter:
        # domain_filter 是 slug，需要用 fuzzy 匹配（unified 里 domain 是中文）
        filtered = []
        for d in all_domains:
            d_lower = d.lower()
            for slug in domain_filter:
                slug_lower = slug.lower()
                if (slug_lower in d_lower or d_lower in slug_lower
                    or _fuzzy_match_domain(d, slug)):
                    filtered.append(d)
                    break
        all_domains = filtered

    if not all_domains:
        return '<p style="color:#888">本期暂无你订阅领域的内容。</p>'

    for domain in all_domains:
        parts.append(
            f'<h2 style="border-bottom:2px solid #d4af37;padding-bottom:6px;'
            f'margin-top:32px;font-size:20px">🌟 {domain}</h2>'
        )

        # 该域头条
        for h in headlines_by_domain.get(domain, []):
            parts.append(_render_headline_html(h))

        # 该域备选
        sl = shortlist_by_domain.get(domain, [])
        if sl:
            parts.append('<div style="margin-top:20px"><strong style="color:#666">📋 备选阅读</strong><ul style="padding-left:20px;color:#444">')
            for it in sl:
                title = (it.get("title") or "").strip()
                url = it.get("url", "")
                one_liner = (it.get("one_liner") or "").strip()
                if url:
                    parts.append(
                        f'<li><a href="{url}" style="color:#1a1a1c">{title}</a>'
                        + (f' —— <span style="color:#666">{one_liner}</span>' if one_liner else "")
                        + "</li>"
                    )
                else:
                    parts.append(
                        f'<li>{title}'
                        + (f' —— <span style="color:#666">{one_liner}</span>' if one_liner else "")
                        + "</li>"
                    )
            parts.append("</ul></div>")

    return "\n".join(parts)


def _render_headline_html(h: dict[str, Any]) -> str:
    """单条头条 → HTML 卡片"""
    title = (h.get("title") or "").strip()
    stars = STARS_MAP.get(h.get("stars", 4), "⭐⭐⭐⭐")
    source = h.get("source", "")
    lead = (h.get("lead") or "").strip()
    confirmed = h.get("confirmed", []) or []
    judgment = h.get("judgment", []) or []
    implication = (h.get("implication") or "").strip()
    url = h.get("url", "")

    out = []
    out.append('<div style="border:1px solid #e5e5e0;border-radius:8px;padding:18px 22px;margin:16px 0;background:#fff">')
    out.append(f'<h3 style="margin:0 0 6px;font-size:17px;line-height:1.4">{title}</h3>')
    out.append(f'<div style="color:#888;font-size:12px;margin-bottom:12px">{stars} · {source}</div>')

    if lead:
        out.append(f'<p style="margin:10px 0;color:#333">{lead}</p>')

    if confirmed or judgment:
        out.append('<table cellpadding="0" cellspacing="0" style="width:100%;margin:14px 0;border-collapse:collapse;font-size:13px">')
        out.append('<tr style="background:#fafaf8"><td style="padding:8px 12px;border:1px solid #eee;color:#0a7a3d;width:50%">✅ 已确认</td><td style="padding:8px 12px;border:1px solid #eee;color:#a06000">⚖️ 尚属判断</td></tr>')
        max_rows = max(len(confirmed), len(judgment))
        for i in range(max_rows):
            left = str(confirmed[i]) if i < len(confirmed) else ""
            right = str(judgment[i]) if i < len(judgment) else ""
            out.append(f'<tr><td style="padding:8px 12px;border:1px solid #eee;vertical-align:top">{left}</td><td style="padding:8px 12px;border:1px solid #eee;vertical-align:top">{right}</td></tr>')
        out.append("</table>")

    if implication:
        out.append(f'<p style="margin:14px 0 8px;padding:10px 14px;background:#fff8e1;border-left:3px solid #d4af37;color:#444"><strong>📖 主编点评</strong><br>{implication}</p>')

    if url:
        out.append(f'<p style="margin:10px 0 0"><a href="{url}" style="color:#1a1a1c;text-decoration:none;font-size:13px">📺 打开原文 →</a></p>')

    out.append("</div>")
    return "\n".join(out)


def _fuzzy_match_domain(domain_zh: str, slug_en: str) -> bool:
    """中文域名 vs 英文 slug 的 fuzzy 匹配"""
    mapping = {
        "ai": ["ai", "科技", "人工智能"],
        "finance": ["金融", "财经"],
        "semiconductor": ["半导体", "芯片"],
        "bigtech": ["大厂", "科技公司"],
        "vibe-coding": ["vibe", "coding", "编程"],
    }
    keys = mapping.get(slug_en.lower(), [])
    return any(k in domain_zh.lower() for k in keys)


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
