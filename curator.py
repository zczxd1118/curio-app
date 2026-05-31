#!/usr/bin/env python3
"""
Curio (content-curator) — 搜寻型 AI 信息策展 Agent (M0 v0.3)

人机协作环路（搜寻型）：
  1. python curator.py explore "vibe coding"
     → 生成喂给 WorkBuddy 的 prompt（拆领域 + 关键词 + 底底源）

  2. 把 AI 输出的 JSON 存到 topics/<slug>.explore.json
     python curator.py search topics/<slug>.explore.json
     → 调 B 站搜索抓真实内容池 → topics/<slug>.candidates.json

  3. python curator.py score topics/<slug>.candidates.json
     → 生成喂给 WorkBuddy 的打分 prompt（含画像 + 候选池）

  4. 把 AI 输出的打分 JSON 存到 topics/<slug>.scored.json
     python curator.py digest topics/<slug>.scored.json
     → 渲染最终的 markdown digest
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import time
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent
PROMPTS = ROOT / "prompts"
TOPICS = ROOT / "topics"
PROFILE_PATH = ROOT / "profile.yaml"


# ----------------------------- 通用工具 ----------------------------- #
def slugify(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"[^\w\u4e00-\u9fff\-]", "", s)
    return s or "topic"


def load_profile() -> dict[str, Any]:
    if not PROFILE_PATH.exists():
        print(f"❌ 找不到 profile.yaml：{PROFILE_PATH}", file=sys.stderr)
        sys.exit(1)
    return yaml.safe_load(PROFILE_PATH.read_text(encoding="utf-8"))


def load_json_loose(path: Path) -> dict[str, Any]:
    """容错读 JSON（支持带 ```json``` 代码块的粘贴）"""
    text = path.read_text(encoding="utf-8").strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


def fill_prompt(template: str, **kwargs: Any) -> str:
    out = template
    for k, v in kwargs.items():
        if isinstance(v, (list, dict)):
            v = json.dumps(v, ensure_ascii=False, indent=2, default=str)
        out = out.replace(f"{{{k}}}", str(v))
    return out


# ----------------------------- explore ----------------------------- #
def cmd_explore(args: argparse.Namespace) -> int:
    """生成"拆领域 + 关键词 + 底底源"prompt"""
    template = (PROMPTS / "explore_domain.md").read_text(encoding="utf-8")
    profile = load_profile()
    today = dt.date.today().isoformat()

    prompt = fill_prompt(
        template,
        TOPIC=args.topic,
        DATE=today,
        IDENTITY=profile.get("identity", "").strip(),
        SIGNAL_PREFERENCES=profile.get("signal_preferences", []),
        DISLIKES=profile.get("dislikes", []),
    )

    print("=" * 78)
    print(f"🎯 领域：{args.topic}    📅 {today}")
    print("=" * 78)
    print()
    print("👇 复制下面整段，贴到 WorkBuddy 让 AI 拆领域：")
    print()
    print("-" * 78)
    print(prompt)
    print("-" * 78)
    print()
    slug = slugify(args.topic)
    print(f"✏️  AI 返回 JSON 后：")
    print(f"   1. 把 JSON（仅 ```json``` 内的）保存到 topics/{slug}.explore.json")
    print(f"   2. 跑：python curator.py search topics/{slug}.explore.json")
    return 0


# ----------------------------- search（v0.4 多源） ----------------------------- #
SOURCES_PATH = ROOT / "sources.yaml"


def _load_sources_for_domain(domain_id: str) -> dict[str, list[dict]]:
    """从 sources.yaml 读出指定 domain 下所有 topic 的信源列表"""
    if not SOURCES_PATH.exists():
        return {}
    cfg = yaml.safe_load(SOURCES_PATH.read_text(encoding="utf-8"))
    domain_cfg = cfg.get("domains", {}).get(domain_id, {})
    topics_cfg = domain_cfg.get("topics", {})
    # 返回 {topic_id: [source_dict, ...]}
    return {tid: tcfg.get("sources", []) for tid, tcfg in topics_cfg.items()}


def _run_source(src: dict) -> list[dict]:
    """根据 kind 调对应抓取器"""
    kind = src.get("kind")
    name = src.get("name", "?")

    sys.path.insert(0, str(ROOT))

    try:
        if kind == "rss":
            from agent.fetch_rss import fetch_one_feed
            return fetch_one_feed(
                src["url"],
                feed_name=name,
                lang=src.get("lang", ""),
                max_items=src.get("max", 30),
            )
        elif kind == "hn_search":
            from agent.fetch_hackernews import search_hn
            return search_hn(
                src["query"],
                days=src.get("days", 7),
                min_points=src.get("min_points", 0),
            )
        elif kind == "bilibili_search":
            from agent.search_bilibili import search_keywords as bili_search
            return bili_search(
                src.get("keywords", []),
                pages_per_kw=1,
                sleep=1.0,
            )
        elif kind == "wallstreetcn_api":
            from agent.fetch_wallstreetcn import fetch_wallstreetcn
            return fetch_wallstreetcn(
                limit=src.get("limit", 20),
                source_name=name,
            )
        else:
            print(f"   ⚠️ 未知 kind: {kind}", file=sys.stderr)
            return []
    except Exception as e:
        if src.get("optional"):
            print(f"   ⚠️ optional 源失败已忽略: {name} ({e})", file=sys.stderr)
            return []
        raise


def cmd_search(args: argparse.Namespace) -> int:
    """v0.4：读 sources.yaml，多源并行抓取候选池

    （并行用串行实现以保持代码简单；候选池规模不大无需并发）
    """
    explore_path = Path(args.explore_file)
    if not explore_path.exists():
        print(f"❌ 找不到 {explore_path}", file=sys.stderr)
        return 1

    explore = load_json_loose(explore_path)
    domain_name = explore.get("domain", "未命名领域")
    domain_id = explore.get("domain_id") or slugify(domain_name)

    # 兼容老的 explore.json：如果用户写的是 "vibe coding"，去 sources.yaml 里
    # 不一定能找到对应 domain_id。给一个 fallback：用全局 + ai 域试试
    sources_by_topic = _load_sources_for_domain(domain_id)

    # 如果该 domain 在 sources.yaml 里找不到，fallback 用 ai 域
    # （因为 v0.3 的 explore.json domain="vibe coding" 实际属于 ai 域下的 topic）
    if not sources_by_topic:
        # 智能 fallback：vibe coding / claude code 等都是 ai 域下的 topic
        if any(kw in domain_name.lower() for kw in ["vibe", "ai", "claude", "cursor", "agent"]):
            print(f"💡 domain '{domain_name}' 没有专属 sources.yaml 配置，回退到 ai 域", file=sys.stderr)
            sources_by_topic = _load_sources_for_domain("ai")
        if not sources_by_topic:
            print(f"❌ sources.yaml 里没找到 '{domain_id}' 的信源配置", file=sys.stderr)
            return 1

    # 收集所有 topic 下的所有信源（先选 vibe-coding 这个具体 topic 如果对的上）
    target_topic_id = None
    for tid in sources_by_topic.keys():
        if tid.lower() in domain_name.lower().replace(" ", "-"):
            target_topic_id = tid
            break
    if not target_topic_id:
        # 否则用所有 topic 的信源
        target_topic_id = list(sources_by_topic.keys())[0] if sources_by_topic else None

    if target_topic_id:
        print(f"🎯 命中 topic: {target_topic_id}", file=sys.stderr)
        sources = sources_by_topic[target_topic_id]
    else:
        # 把所有 topic 的信源 flatten
        sources = [s for srcs in sources_by_topic.values() for s in srcs]

    print(f"📡 共 {len(sources)} 个信源待抓取\n", file=sys.stderr)

    all_items: dict[str, dict] = {}
    source_stats: dict[str, int] = {}

    for src in sources:
        items = _run_source(src)
        source_stats[src.get("name", "?")] = len(items)
        for it in items:
            all_items.setdefault(it["id"], it)
        time.sleep(0.5)

    items = list(all_items.values())

    output = {
        "domain": domain_name,
        "domain_id": domain_id,
        "topic_id": target_topic_id,
        "fetched_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "platforms": sorted({it.get("platform", "?") for it in items}),
        "source_stats": source_stats,
        "subtopics": explore.get("subtopics", []),
        "total": len(items),
        "items": items,
    }

    slug = slugify(domain_name)
    out_path = TOPICS / f"{slug}.candidates.json"
    TOPICS.mkdir(exist_ok=True)
    out_path.write_text(
        json.dumps(output, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"\n✅ 候选池：{out_path}（{len(items)} 条 · 来自 {len(output['platforms'])} 个平台）")
    print(f"   平台分布: {', '.join(output['platforms'])}")
    print(f"   信源贡献：")
    for name, n in source_stats.items():
        print(f"     · {name}: {n} 条")
    print(f"\n💡 下一步：python curator.py score {out_path}")
    return 0


# ----------------------------- score ----------------------------- #
def cmd_score(args: argparse.Namespace) -> int:
    """读候选池 + 画像，生成喂给 WorkBuddy 的打分 prompt"""
    candidates_path = Path(args.candidates_file)
    if not candidates_path.exists():
        print(f"❌ 找不到 {candidates_path}", file=sys.stderr)
        return 1

    candidates = load_json_loose(candidates_path)
    profile = load_profile()
    today = dt.date.today().isoformat()
    domain = candidates.get("domain", "未命名领域")

    # 精简候选条目（避免 prompt 过长，每条只留打分必要字段）
    # v0.4：支持多平台，每条带 platform 字段；HN 用 points、RSS 没 duration
    items_for_prompt = []
    for it in candidates.get("items", []):
        platform = it.get("platform", "?")
        item = {
            "id": it["id"],
            "platform": platform,
            "title": it.get("title", ""),
            "url": it.get("url", ""),
            "source": it.get("source", {}).get("name", ""),
            "published_at": it.get("published_at", ""),
            "summary": (it.get("summary", "") or "")[:300],
        }
        # 平台特定字段
        if platform == "bilibili":
            item["duration_sec"] = it.get("duration_sec", 0)
            item["views"] = it.get("views", 0)
        elif platform == "hackernews":
            item["points"] = it.get("views", 0)   # 我们用 views 字段存 points
            item["comments"] = it.get("comments", 0)
        elif platform == "rss":
            item["feed"] = it.get("source", {}).get("feed_title", "")

        if it.get("matched_keywords"):
            item["matched_keywords"] = it["matched_keywords"]
        items_for_prompt.append(item)

    template = (PROMPTS / "score_content.md").read_text(encoding="utf-8")
    prompt = fill_prompt(
        template,
        DOMAIN=domain,
        DATE=today,
        SUBTOPICS=[st.get("name") for st in candidates.get("subtopics", [])],
        IDENTITY=profile.get("identity", "").strip(),
        INTERESTS=profile.get("interests", []),
        DISLIKES=profile.get("dislikes", []),
        SIGNAL_PREFERENCES=profile.get("signal_preferences", []),
        READING_PACE=profile.get("reading_pace", "").strip(),
        FEEDBACK_TIMELINE=profile.get("feedback_timeline", []),
        ALREADY_PUSHED_TITLES=[],
    )

    # 在 prompt 末尾追加候选池
    prompt += "\n\n---\n\n## 候选内容池\n\n```json\n"
    prompt += json.dumps(items_for_prompt, ensure_ascii=False, indent=2)
    prompt += "\n```\n"

    # 输出到文件（太长了不直接打印）
    slug = slugify(domain)
    prompt_path = TOPICS / f"{slug}.score-prompt.md"
    TOPICS.mkdir(exist_ok=True)
    prompt_path.write_text(prompt, encoding="utf-8")

    print("=" * 78)
    print(f"🎯 领域：{domain}    候选 {len(items_for_prompt)} 条    📅 {today}")
    print("=" * 78)
    print(f"📄 打分 prompt 已写入：{prompt_path}")
    print(f"   （太长了不打印到终端）")
    print()
    print("👇 操作步骤：")
    print(f"   1. 打开 {prompt_path}，把全文贴到 WorkBuddy")
    print(f"   2. AI 返回打分 JSON 后保存到 topics/{slug}.scored.json")
    print(f"   3. 跑：python curator.py digest topics/{slug}.scored.json")
    return 0


# ----------------------------- digest ----------------------------- #
def cmd_digest(args: argparse.Namespace) -> int:
    """读打分 JSON，渲染 markdown digest"""
    scored_path = Path(args.scored_file)
    if not scored_path.exists():
        print(f"❌ 找不到 {scored_path}", file=sys.stderr)
        return 1

    scored = load_json_loose(scored_path)
    today = dt.date.today().isoformat()
    domain = scored.get("domain", "未命名领域")

    def render_card(c: dict[str, Any], idx: int) -> str:
        score = c.get("score", {})
        stars_n = score.get("novelty", 0)
        stars_d = score.get("depth", 0)
        stars_r = score.get("relevance", 0)
        diverse = " 🌱" if c.get("is_diverse") else ""
        return (
            f"### {idx}. {c.get('title', '?')}{diverse}\n"
            f"- **来源**：{c.get('source', '?')}　|　**链接**：[打开]({c.get('url', '#')})\n"
            f"- **评分**：新颖 {stars_n} · 深度 {stars_d} · 相关 {stars_r}\n"
            f"- **为什么推**：{c.get('why_recommend', '')}\n"
        )

    must = scored.get("must_read", []) or []
    ref = scored.get("reference", []) or []
    skip = scored.get("skip", []) or []
    intro = scored.get("intro", "")
    stats = scored.get("stats", {})

    lines = [
        f"# {domain} · Curio Digest",
        "",
        f"> **生成于**：{today}",
        f"> **候选池**：{stats.get('candidates_total', '?')} 条 → "
        f"必读 {len(must)} · 参考 {len(ref)} · 跳过 {len(skip)}",
        "",
        "---",
        "",
        "## 🤖 主编开场白",
        "",
        intro or "_（AI 没写开场白）_",
        "",
        "---",
        "",
        f"## ✨ 必读（{len(must)}）",
        "",
    ]
    for i, c in enumerate(must, 1):
        lines.append(render_card(c, i))

    lines += ["", "---", "", f"## 📖 参考（{len(ref)}）", ""]
    for i, c in enumerate(ref, 1):
        lines.append(render_card(c, i))

    lines += [
        "",
        "---",
        "",
        f"## ⏭ 跳过（{len(skip)}）",
        "",
    ]
    SKIP_PREVIEW_LIMIT = 5
    if skip:
        preview = skip[:SKIP_PREVIEW_LIMIT]
        rest = len(skip) - len(preview)
        lines.append(
            f"_展示前 {len(preview)} 条跳过理由（共 {len(skip)} 条），"
            f"其余 {rest} 条按相同标准筛除（流量号 SEO / 老内容 / 跨主题 / 标题党 / 破解类）_"
            if rest > 0 else
            f"_共 {len(skip)} 条跳过理由_"
        )
        lines.append("")
        for c in preview:
            lines.append(
                f"- **{c.get('title', '?')}**　_{c.get('skip_reason', '')}_"
            )
        if rest > 0:
            lines += [
                "",
                f"<details><summary>展开剩余 {rest} 条</summary>",
                "",
            ]
            for c in skip[SKIP_PREVIEW_LIMIT:]:
                lines.append(
                    f"- **{c.get('title', '?')}**　_{c.get('skip_reason', '')}_"
                )
            lines += ["", "</details>", ""]
    lines.append("")

    lines += [
        "---",
        "",
        "## 📝 你的反馈（M0 手动写一段，下次跑前 Agent 会读）",
        "",
        "本期整体：____________________________________________",
        "",
        "想多看：______________________________________________",
        "",
        "想少看：______________________________________________",
        "",
    ]

    md = "\n".join(lines)

    slug = slugify(domain)
    out_path = TOPICS / f"{slug}.digest.{today}.md"
    TOPICS.mkdir(exist_ok=True)
    out_path.write_text(md, encoding="utf-8")
    print(f"✅ Digest 已生成：{out_path}")
    print(f"📊 必读 {len(must)} · 参考 {len(ref)} · 跳过 {len(skip)}")
    return 0


# ----------------------------- write（v0.5 报纸化） ----------------------------- #
def _fetch_body_for(item: dict) -> tuple[str, str]:
    """对一条必读：根据 platform 拿原文，返回 (body, source_kind)
    source_kind: article / subtitle / fallback
    """
    sys.path.insert(0, str(ROOT))
    platform = item.get("platform", "")
    url = item.get("url", "")

    # B 站：尝试拿字幕
    if platform == "bilibili" and url:
        # url 格式 https://www.bilibili.com/video/BVxxx
        bv = None
        m = re.search(r"(BV[a-zA-Z0-9]+)", url)
        if m:
            bv = m.group(1)
        if bv:
            sub_path = TOPICS / "subtitles" / f"{bv}.txt"
            if sub_path.exists():
                return sub_path.read_text(encoding="utf-8"), "subtitle (cached)"
            try:
                from agent.fetch_subtitle import fetch_subtitle
                r = fetch_subtitle(bv, use_whisper=False)
                if r.get("ok"):
                    return r["content"], r.get("source", "subtitle")
            except Exception as e:
                print(f"   ⚠️ 字幕抓取失败 ({bv}): {e}", file=sys.stderr)

    # RSS / HN：用 trafilatura 抓全文
    if platform in ("rss", "hackernews") and url:
        try:
            from agent.fetch_article import fetch_article
            r = fetch_article(url)
            if r.get("ok"):
                return r["body"], "article" + (" (cache)" if r.get("from_cache") else "")
        except Exception as e:
            print(f"   ⚠️ 全文抓取失败 ({url[:50]}): {e}", file=sys.stderr)

    # fallback：用 summary
    return item.get("summary", "") or "", "fallback (no body)"


def cmd_write(args: argparse.Namespace) -> int:
    """读 scored.json 必读区，抓每条原文/字幕，生成报纸写作 prompt"""
    scored_path = Path(args.scored_file)
    if not scored_path.exists():
        print(f"❌ 找不到 {scored_path}", file=sys.stderr)
        return 1

    scored = load_json_loose(scored_path)
    profile = load_profile()
    domain = scored.get("domain", "未命名领域")
    today = dt.date.today().isoformat()

    must = (scored.get("must_read", []) or [])[: args.top_must]
    if not must:
        print("❌ 必读区是空的", file=sys.stderr)
        return 1

    print(f"📰 准备为 {len(must)} 条必读写报纸式报道...\n", file=sys.stderr)

    # Step 1：批量抓原文
    enriched = []
    for i, m_item in enumerate(must, 1):
        title = (m_item.get("title", "") or "")[:50]
        platform = m_item.get("platform", "?")
        print(f"📄 [{i}/{len(must)}] [{platform}] {title}", file=sys.stderr)
        body, kind = _fetch_body_for(m_item)
        print(f"   → {kind}, {len(body)} chars\n", file=sys.stderr)
        enriched.append({**m_item, "_body": body, "_body_kind": kind})

    # Step 2：为每条生成 write_article prompt
    article_template = (PROMPTS / "write_article.md").read_text(encoding="utf-8")
    article_prompts = []
    for i, m_item in enumerate(enriched, 1):
        prompt = fill_prompt(
            article_template,
            IDENTITY=profile.get("identity", "").strip(),
            SIGNAL_PREFERENCES=profile.get("signal_preferences", []),
            DISLIKES=profile.get("dislikes", []),
            TITLE=m_item.get("title", ""),
            SOURCE=m_item.get("source", ""),
            PLATFORM=m_item.get("platform", ""),
            PUBLISHED_AT=m_item.get("published_at", "") or "",
            URL=m_item.get("url", ""),
            DOMAIN=domain,
            ARTICLE_BODY=m_item.get("_body", "")[:8000],   # 防止 prompt 过长
        )
        article_prompts.append({
            "index": i,
            "id": m_item.get("id"),
            "title": m_item.get("title"),
            "platform": m_item.get("platform"),
            "body_kind": m_item.get("_body_kind"),
            "prompt": prompt,
        })

    # Step 3：editorial prompt
    editorial_template = (PROMPTS / "write_editorial.md").read_text(encoding="utf-8")
    must_read_headlines = "\n".join(
        f"#{i+1} 「{m.get('title','')[:60]}」({m.get('platform')})\n     ↳ 论点：{m.get('why_recommend','')[:80]}"
        for i, m in enumerate(enriched)
    )
    last_feedback = ""
    fb = profile.get("feedback_timeline", []) or []
    if fb:
        last = fb[0] if isinstance(fb, list) else fb
        if isinstance(last, dict):
            last_feedback = f"[{last.get('date','')}] {last.get('text','')}"

    editorial_prompt = fill_prompt(
        editorial_template,
        IDENTITY=profile.get("identity", "").strip(),
        SIGNAL_PREFERENCES=profile.get("signal_preferences", []),
        DOMAIN=domain,
        PERIOD=today,
        LAST_FEEDBACK=last_feedback or "（无）",
        MUST_READ_HEADLINES=must_read_headlines,
        CANDIDATES_TOTAL=scored.get("stats", {}).get("candidates_total", "?"),
        MUST_READ_COUNT=len(enriched),
    )

    # Step 4：把所有 prompt 写到一个 .write-prompts.md 文件
    slug = slugify(domain)
    out_path = TOPICS / f"{slug}.write-prompts.md"
    parts = [
        f"# Curio 报纸写作 prompt 集（{domain} · {today}）",
        "",
        f"> 把下面每个 prompt 块**逐个**贴回 WorkBuddy 让 Agent 写。",
        f"> 写完的报道按顺序保存为 `topics/{slug}.articles.md`，社论保存为 `topics/{slug}.editorial.md`。",
        f"> 然后跑：`python curator.py assemble topics/{slug}.scored.json topics/{slug}.articles.md topics/{slug}.editorial.md`",
        "",
        "---",
        "",
        f"## 📰 头版社论 prompt",
        "",
        editorial_prompt,
        "",
        "---",
        "",
        f"## 📑 头版报道 prompts（共 {len(article_prompts)} 篇）",
        "",
    ]
    for ap in article_prompts:
        parts += [
            f"### 报道 #{ap['index']} · {ap['title'][:60]}",
            f"- platform: `{ap['platform']}`",
            f"- body 来源: `{ap['body_kind']}`",
            "",
            "<details><summary>展开 prompt</summary>",
            "",
            ap["prompt"],
            "",
            "</details>",
            "",
            "---",
            "",
        ]

    out_path.write_text("\n".join(parts), encoding="utf-8")

    print(f"✅ 写作 prompt 已生成：{out_path}")
    print(f"   📑 {len(article_prompts)} 篇报道 prompt + 1 篇社论 prompt")
    print()
    print(f"💡 下一步：")
    print(f"   1. 打开 {out_path.name}")
    print(f"   2. 把 social prompt 贴给我，我写社论 → 保存到 topics/{slug}.editorial.md")
    print(f"   3. 依次把每篇报道 prompt 贴给我 → 全部保存到 topics/{slug}.articles.md（用 ## 报道 N 分隔）")
    print(f"   4. 跑：python curator.py assemble topics/{slug}.scored.json topics/{slug}.articles.md topics/{slug}.editorial.md")
    return 0


def cmd_assemble(args: argparse.Namespace) -> int:
    """把 WorkBuddy 写的 articles + editorial 拼成最终报纸 markdown"""
    scored_path = Path(args.scored_file)
    articles_path = Path(args.articles_file)
    editorial_path = Path(args.editorial_file)

    for p in (scored_path, articles_path, editorial_path):
        if not p.exists():
            print(f"❌ 找不到 {p}", file=sys.stderr)
            return 1

    scored = load_json_loose(scored_path)
    domain = scored.get("domain", "未命名领域")
    today = dt.date.today().isoformat()

    editorial_md = editorial_path.read_text(encoding="utf-8").strip()
    articles_md = articles_path.read_text(encoding="utf-8").strip()

    must = scored.get("must_read", []) or []
    ref = scored.get("reference", []) or []
    skip = scored.get("skip", []) or []
    stats = scored.get("stats", {})

    # 把 articles_md 按 "## 报道 N" 分段（如果用户按这个格式贴的）
    article_blocks = re.split(r"^##\s*报道\s*#?\d+", articles_md, flags=re.MULTILINE)
    article_blocks = [b.strip() for b in article_blocks if b.strip()]

    # 渲染最终报纸
    lines = [
        f"# Curio · {domain} 周刊",
        "",
        f"**{today} · 由 Curio 主编从 {stats.get('candidates_total', '?')} 条候选选出**",
        "",
        "---",
        "",
        "## 🛰️ 今日信号纵览（精选 Top {})".format(len(must)),
        "",
        "| # | 平台 | 事件一句话 | 信号 |",
        "|---|---|---|---|",
    ]

    def _platform_emoji(p):
        return {"rss": "📰 RSS", "hackernews": "🔶 HN", "bilibili": "🎬 B站"}.get(p, p)

    for i, m_item in enumerate(must, 1):
        title = (m_item.get("title", "") or "").replace("|", "｜")
        # 一句话事件：用 why_recommend 的前句
        oneliner = (m_item.get("why_recommend", "") or title).split("。")[0]
        oneliner = oneliner.replace("|", "｜")[:80]
        if len(oneliner) >= 79:
            oneliner += "…"
        score = m_item.get("score", {})
        avg = (score.get("novelty", 0) + score.get("depth", 0) + score.get("relevance", 0)) // 3
        stars = "★" * min(5, max(1, avg // 2)) + "☆" * (5 - min(5, max(1, avg // 2)))
        lines.append(f"| {i} | {_platform_emoji(m_item.get('platform','?'))} | {oneliner} | {stars} |")

    lines += [
        "",
        "---",
        "",
        "## 📰 主编社论",
        "",
        editorial_md,
        "",
        "---",
        "",
        f"## 🗞️ 头版报道（{len(must)} 篇）",
        "",
    ]
    for i, m_item in enumerate(must, 1):
        # 头版小标题
        lines += [
            f"### {i}. {m_item.get('title', '?')}",
            "",
            f"_来源：{m_item.get('source', '?')} · {m_item.get('platform', '?')} · {(m_item.get('published_at') or '')[:10]}_",
            "",
        ]
        # 报道正文（从 article_blocks 取第 i 块）
        if i - 1 < len(article_blocks):
            lines.append(article_blocks[i - 1])
        else:
            lines.append("_（这篇报道未提交，请补写）_")
        lines += [
            "",
            f"📺 [打开原文]({m_item.get('url', '#')})",
            "",
            "---",
            "",
        ]

    # 参考区（仍用列表式，简洁）
    if ref:
        lines += [f"## 📖 参考（{len(ref)} 条）", ""]
        for i, r_item in enumerate(ref, 1):
            diverse = " 🌱" if r_item.get("is_diverse") else ""
            lines += [
                f"**{i}. {r_item.get('title','?')}{diverse}**　_{r_item.get('source','?')} · {r_item.get('platform','?')}_",
                f"- {r_item.get('why_recommend','')}",
                f"- [打开]({r_item.get('url','#')})",
                "",
            ]
        lines += ["---", ""]

    # 跳过区（折叠版）
    if skip:
        SKIP_PREVIEW = 5
        rest = max(0, len(skip) - SKIP_PREVIEW)
        lines += [
            f"## ⏭ 跳过（{stats.get('skip_count_actual', len(skip))} 条）",
            "",
            f"_展示前 {min(SKIP_PREVIEW, len(skip))} 条跳过理由_",
            "",
        ]
        for s_item in skip[:SKIP_PREVIEW]:
            lines.append(f"- **{s_item.get('title','?')}**　_{s_item.get('skip_reason','')}_")
        if rest > 0:
            lines += ["", f"<details><summary>展开剩余 {rest} 条</summary>", ""]
            for s_item in skip[SKIP_PREVIEW:]:
                lines.append(f"- **{s_item.get('title','?')}**　_{s_item.get('skip_reason','')}_")
            lines += ["", "</details>"]
        lines += ["", "---", ""]

    # 反馈区（v2：每条独立反馈 + 长期偏好）
    lines += [
        "## 📝 本期反馈",
        "",
        "_填写后下次跑会读这段调整。每条选 [有用 / 一般 / 偏了] 之一，可加备注。_",
        "",
    ]
    for i, m_item in enumerate(must, 1):
        title_short = (m_item.get('title', '') or '?')[:50]
        lines += [
            f"**{i}. {title_short}**　[ ] 有用　[ ] 一般　[ ] 偏了",
            f"   _备注：_",
            "",
        ]

    lines += [
        "**最近更关注**：__________________（如 AI Agent / 美股期权 / 半导体先进制程…）",
        "",
        "**最近不太关注**：__________________（如 纯产品更新 / 概念股炒作…）",
        "",
        "**报道笔法（这是新尝试，重点反馈）**：__________________",
        "",
        "---",
        "",
        f"_Curio v0.5 · {today}_",
    ]

    slug = slugify(domain)
    out_path = TOPICS / f"{slug}.weekly.{today}.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"✅ 最终报纸：{out_path}")
    print(f"   📊 头版 {len(must)} 篇 · 参考 {len(ref)} · 跳过 {len(skip)}")
    return 0


# ----------------------------- 多领域管理（v0.6） ----------------------------- #
SOURCES_YAML = ROOT / "sources.yaml"


def _load_sources_cfg() -> dict:
    if not SOURCES_YAML.exists():
        return {"domains": {}}
    return yaml.safe_load(SOURCES_YAML.read_text(encoding="utf-8")) or {"domains": {}}


def _save_sources_cfg(cfg: dict) -> None:
    SOURCES_YAML.write_text(
        yaml.dump(cfg, allow_unicode=True, sort_keys=False, indent=2),
        encoding="utf-8",
    )


def cmd_add_domain(args: argparse.Namespace) -> int:
    """添加新领域到 sources.yaml；信源稍后由 explore 命令补全"""
    cfg = _load_sources_cfg()
    domains = cfg.setdefault("domains", {})
    if args.domain_id in domains:
        print(f"⚠️  领域 '{args.domain_id}' 已存在", file=sys.stderr)
        return 1
    domains[args.domain_id] = {
        "name": args.name,
        "icon": args.icon,
        "frequency": args.frequency,
        "topics": {},
        "_added_at": dt.datetime.now().isoformat(),
    }
    _save_sources_cfg(cfg)
    print(f"✅ 已添加领域：{args.icon} {args.name}（id={args.domain_id}）")
    print(f"   下一步：python curator.py explore \"{args.name}\" 让 AI 拆子话题 + 推荐信源")
    return 0


def cmd_list_domains(args: argparse.Namespace) -> int:
    cfg = _load_sources_cfg()
    domains = cfg.get("domains") or {}
    if not domains:
        print("（暂无领域）")
        return 0
    print(f"📚 共 {len(domains)} 个领域：\n")
    for did, dcfg in domains.items():
        topics = dcfg.get("topics") or {}
        n_sources = sum(len(t.get("sources", []) or []) for t in topics.values())
        print(f"  {dcfg.get('icon', '📰')} {dcfg.get('name', did)} ({did})")
        print(f"     · 频率: {dcfg.get('frequency', 'weekly')}")
        print(f"     · {len(topics)} 个 topic / {n_sources} 个信源")
        for tid, t in topics.items():
            print(f"        - {tid}: {len(t.get('sources', []) or [])} 源")
    return 0


def cmd_site(args: argparse.Namespace) -> int:
    """触发静态站点构建"""
    sys.path.insert(0, str(ROOT))
    from agent.render_site import build_site
    return build_site()


# ----------------------------- 入口 ----------------------------- #
def main() -> int:
    parser = argparse.ArgumentParser(
        prog="curator",
        description="Curio —— 搜寻型 AI 信息策展 Agent (M0 v0.3)",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_e = sub.add_parser("explore", help="拆领域 + 关键词 + 底底源")
    p_e.add_argument("topic", help='领域名，如 "vibe coding"')
    p_e.set_defaults(func=cmd_explore)

    p_s = sub.add_parser("search", help="按 explore.json 关键词调 B 站搜索")
    p_s.add_argument("explore_file", help="explore JSON 路径")
    p_s.add_argument("--pages", type=int, default=1)
    p_s.add_argument("--sleep", type=float, default=1.2)
    p_s.set_defaults(func=cmd_search)

    p_sc = sub.add_parser("score", help="生成打分 prompt（贴给 WorkBuddy）")
    p_sc.add_argument("candidates_file", help="candidates JSON 路径")
    p_sc.set_defaults(func=cmd_score)

    p_d = sub.add_parser("digest", help="把打分 JSON 渲染为 markdown digest")
    p_d.add_argument("scored_file", help="scored JSON 路径")
    p_d.set_defaults(func=cmd_digest)

    p_w = sub.add_parser("write", help="抓必读全文 → 生成报纸 prompt（贴给 WorkBuddy 写）")
    p_w.add_argument("scored_file", help="scored JSON 路径")
    p_w.add_argument("--top-must", type=int, default=6, help="只对前 N 条必读抓全文")
    p_w.set_defaults(func=cmd_write)

    p_a = sub.add_parser("assemble", help="把 WorkBuddy 写的 articles + editorial 拼成最终报纸")
    p_a.add_argument("scored_file", help="scored JSON 路径")
    p_a.add_argument("articles_file", help="articles markdown 文件（含每篇报道）")
    p_a.add_argument("editorial_file", help="社论 markdown 文件")
    p_a.set_defaults(func=cmd_assemble)

    p_ad = sub.add_parser("add-domain", help="添加新领域（用户自定义）")
    p_ad.add_argument("domain_id", help='领域 slug，如 "biotech"')
    p_ad.add_argument("--name", required=True, help='中文显示名，如 "生物科技"')
    p_ad.add_argument("--icon", default="📰", help="emoji 图标")
    p_ad.add_argument("--frequency", default="weekly", choices=["daily", "weekly"])
    p_ad.set_defaults(func=cmd_add_domain)

    p_ld = sub.add_parser("list-domains", help="列出所有已配置领域")
    p_ld.set_defaults(func=cmd_list_domains)

    p_site = sub.add_parser("site", help="构建静态站点（site/）")
    p_site.set_defaults(func=cmd_site)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
