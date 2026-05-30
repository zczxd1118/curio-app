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


def search_hn(
    query: str,
    days: int = 7,
    min_points: int = 0,
    hits_per_page: int = 30,
    tags: str = "story",
) -> list[dict[str, Any]]:
    """
    搜 HN
    - tags=story 只要文章（不要评论）
    - numericFilters 限定时间和热度
    """
    now = datetime.now(timezone.utc)
    since_ts = int((now - timedelta(days=days)).timestamp())

    numeric_filters = [f"created_at_i>{since_ts}"]
    if min_points > 0:
        numeric_filters.append(f"points>={min_points}")

    params = {
        "query": query,
        "tags": tags,
        "hitsPerPage": hits_per_page,
        "numericFilters": ",".join(numeric_filters),
    }

    print(f"📡 HN · '{query}' · 近 {days} 天 · points>={min_points}", file=sys.stderr)

    try:
        r = requests.get(ENDPOINT, params=params, headers={"User-Agent": UA}, timeout=15)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"   ⚠️ 请求失败: {e}", file=sys.stderr)
        return []

    hits = r.json().get("hits", [])

    items: list[dict[str, Any]] = []
    for h in hits:
        title = h.get("title") or ""
        url = h.get("url") or f"https://news.ycombinator.com/item?id={h.get('objectID')}"
        if not title:
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

    print(f"   ✓ 拿到 {len(items)} 条", file=sys.stderr)
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
