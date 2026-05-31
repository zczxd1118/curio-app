#!/usr/bin/env python3
"""
Hacker News 抓取（Algolia HN Search API）

用法：
  python fetch_hackernews.py "Claude Code" --days 14
  python fetch_hackernews.py "AI agent" --days 7 --min-points 50

API 文档：https://hn.algolia.com/api
- 免登录、免 key、CORS 友好
- 支持关键词搜索、时间过滤、热度过滤
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timedelta, timezone
from typing import Any

import requests

ENDPOINT = "https://hn.algolia.com/api/v1/search"
UA = "Curio/0.1 (https://github.com/zoezczhou)"


def _is_relevant(title: str, url: str, query: str) -> bool:
    """关键词必须在标题或 URL 域名里出现，否则丢掉（HN 全文搜索副作用）"""
    q = query.lower().strip()
    if not q:
        return True
    # 拆多关键词（如 "TSMC chip"），任一命中就过
    tokens = [t for t in q.replace("-", " ").split() if len(t) >= 2]
    hay = (title + " " + url).lower()
    return any(t in hay for t in tokens) if tokens else True


def search_hn(
    query: str,
    days: int = 7,
    min_points: int = 0,
    hits_per_page: int = 30,
    tags: str = "story",
    strict_match: bool = True,
    adaptive: bool = True,
) -> list[dict[str, Any]]:
    """
    搜 HN
    - tags=story 只要文章（不要评论）
    - numericFilters 限定时间和热度

    ⚙️ adaptive=True（默认）：动态阈值
    - 不直接用 min_points 过滤 API 请求（避免漏冷门话题的早期爆款）
    - 拉回来后看 points 分布，按"实际中位数 vs 配置阈值取较低"做软筛
    - 例如：配置 min_points=50，但近期实际中位数才 20 分（冷门话题），
      则用 max(实际_top30%, 10) 作阈值，多召回 10-15 条
    """
    now = datetime.now(timezone.utc)
    since_ts = int((now - timedelta(days=days)).timestamp())

    # adaptive 模式：API 调用时只用一个"地板阈值"（min_points * 0.3 或 5），
    # 真正过滤在拿到数据后做
    if adaptive:
        api_min = max(5, int(min_points * 0.3))
        # 多拉一些（adaptive 需要更大池子做分位数）
        hits_per_page = max(hits_per_page, 50)
    else:
        api_min = min_points

    numeric_filters = [f"created_at_i>{since_ts}"]
    if api_min > 0:
        numeric_filters.append(f"points>={api_min}")

    params = {
        "query": query,
        "tags": tags,
        "hitsPerPage": hits_per_page,
        "numericFilters": ",".join(numeric_filters),
    }

    if adaptive:
        print(f"📡 HN · '{query}' · 近 {days} 天 · adaptive (api_min={api_min}, target={min_points})", file=sys.stderr)
    else:
        print(f"📡 HN · '{query}' · 近 {days} 天 · points>={min_points}", file=sys.stderr)

    try:
        r = requests.get(ENDPOINT, params=params, headers={"User-Agent": UA}, timeout=15)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"   ⚠️ 请求失败: {e}", file=sys.stderr)
        return []

    hits = r.json().get("hits", [])

    items: list[dict[str, Any]] = []
    skipped_irrelevant = 0
    for h in hits:
        title = h.get("title") or ""
        url = h.get("url") or f"https://news.ycombinator.com/item?id={h.get('objectID')}"
        if not title:
            continue
        # 关键修复：HN Algolia 是全文搜索，命中会包含正文里偶然提到关键词的不相关文章
        # 只保留标题或 url 里真正出现关键词的条目
        if strict_match and not _is_relevant(title, url, query):
            skipped_irrelevant += 1
            continue

        created = h.get("created_at_i", 0)
        published = (
            datetime.fromtimestamp(created, tz=timezone.utc).isoformat()
            if created else None
        )

        items.append(
            {
                "id": f"hn:{h.get('objectID')}",
                "title": title,
                "url": url,
                "platform": "hackernews",
                "source": {
                    "type": "hackernews",
                    "id": str(h.get("objectID", "")),
                    "name": h.get("author", ""),
                    "hn_url": f"https://news.ycombinator.com/item?id={h.get('objectID')}",
                },
                "duration_sec": None,
                "views": h.get("points", 0),  # 借用 views 字段表示热度
                "comments": h.get("num_comments", 0),
                "published_at": published,
                "summary": "",  # HN 没有摘要
                "matched_keyword": query,
                "lang": "en",
            }
        )

    # adaptive 模式：根据实际分布做软筛，避免阈值死板
    # 策略：保留 (满足配置阈值的) ∪ (相对热度 top 50% 且 ≥10 票的)
    #       前者抓"标杆"，后者抓"冷门话题里的相对爆款"
    if adaptive and items and min_points > 0:
        all_points = sorted([it["views"] for it in items], reverse=True)
        # 该 keyword 近期 top 50% 中位数
        if all_points:
            median_p = all_points[len(all_points) // 2]
        else:
            median_p = 0
        # 软阈值：max(地板=10, 中位数 * 0.7)，但不超过配置 min_points
        soft_threshold = max(10, int(median_p * 0.7))
        soft_threshold = min(soft_threshold, min_points)

        before = len(items)
        items = [it for it in items if it["views"] >= soft_threshold or it["views"] >= min_points]
        # 如果筛后剩太少（<3），回退到只用地板阈值（避免极端冷门话题被全过滤）
        if len(items) < 3 and before >= 5:
            items = sorted(
                [it for it in items + [{"views": p} for p in all_points]
                 if isinstance(it, dict) and it.get("title")],
                key=lambda x: x["views"], reverse=True
            )[:max(5, before // 3)]
        adapt_msg = f"（自适应阈值={soft_threshold}，配置阈值={min_points}，中位数={median_p}）"
    else:
        adapt_msg = ""

    skip_msg = f"（过滤掉 {skipped_irrelevant} 条不相关）" if skipped_irrelevant else ""
    print(f"   ✓ 拿到 {len(items)} 条 {skip_msg}{adapt_msg}", file=sys.stderr)
    return items


def search_many(
    queries: list[str],
    days: int = 7,
    min_points: int = 0,
    sleep: float = 0.4,
) -> list[dict[str, Any]]:
    """批量搜多个关键词，去重"""
    all_items: dict[str, dict[str, Any]] = {}

    for q in queries:
        items = search_hn(q, days=days, min_points=min_points)
        for it in items:
            if it["id"] in all_items:
                # 合并 matched_keywords
                existing = all_items[it["id"]].setdefault("matched_keywords", [])
                if it["matched_keyword"] not in existing:
                    existing.append(it["matched_keyword"])
            else:
                it["matched_keywords"] = [it.pop("matched_keyword")]
                all_items[it["id"]] = it
        time.sleep(sleep)

    return list(all_items.values())


def main() -> int:
    parser = argparse.ArgumentParser(description="Hacker News 搜索（Algolia API）")
    parser.add_argument("query", help="搜索关键词")
    parser.add_argument("--days", type=int, default=7, help="近 N 天")
    parser.add_argument("--min-points", type=int, default=0, help="最低热度（points）")
    parser.add_argument("--out", help="输出文件路径")
    args = parser.parse_args()

    items = search_hn(args.query, days=args.days, min_points=args.min_points)
    items.sort(key=lambda x: x.get("views", 0), reverse=True)

    output = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "kind": "hn_search",
        "query": args.query,
        "days": args.days,
        "min_points": args.min_points,
        "total": len(items),
        "items": items,
    }

    text = json.dumps(output, ensure_ascii=False, indent=2)
    if args.out:
        from pathlib import Path
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"✅ 已写入 {args.out}（{len(items)} 条）", file=sys.stderr)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
