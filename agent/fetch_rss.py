#!/usr/bin/env python3
"""
通用 RSS / Atom 抓取器

用法：
  python fetch_rss.py "https://api.substack.com/feed/podcast/1084089.rss"
  python fetch_rss.py "https://anthropic.com/news/rss.xml" --max 20

输出：标准化候选 JSON，与 search_bilibili 的格式对齐
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from typing import Any

import feedparser
import requests

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
)


def _strip_html(text: str) -> str:
    """去 HTML 标签"""
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _parse_dt(entry: Any) -> str | None:
    """从 feedparser entry 拿发布时间，统一为 ISO 8601"""
    for key in ("published_parsed", "updated_parsed"):
        t = getattr(entry, key, None) or entry.get(key) if isinstance(entry, dict) else None
        if t:
            try:
                return datetime(*t[:6], tzinfo=timezone.utc).isoformat()
            except (TypeError, ValueError):
                continue
    return None


def fetch_one_feed(
    url: str,
    feed_name: str | None = None,
    lang: str = "",
    max_items: int = 30,
    timeout: int = 15,
) -> list[dict[str, Any]]:
    """抓单个 RSS feed，返回标准化条目"""
    print(f"📡 RSS · {feed_name or url[:50]}", file=sys.stderr)

    try:
        resp = requests.get(url, headers={"User-Agent": UA}, timeout=timeout)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"   ⚠️ 抓取失败: {e}", file=sys.stderr)
        return []

    feed = feedparser.parse(resp.content)
    if feed.bozo and not feed.entries:
        print(f"   ⚠️ 解析失败：{feed.bozo_exception}", file=sys.stderr)
        return []

    feed_title = feed.feed.get("title", feed_name or "Unknown Feed")
    items: list[dict[str, Any]] = []

    for e in feed.entries[:max_items]:
        title = _strip_html(e.get("title", ""))
        link = e.get("link", "")
        if not title or not link:
            continue

        # 摘要：summary > description > content
        summary = ""
        if "summary" in e:
            summary = _strip_html(e.summary)
        elif "description" in e:
            summary = _strip_html(e.description)
        elif "content" in e:
            content_list = e.content if isinstance(e.content, list) else [e.content]
            if content_list:
                summary = _strip_html(content_list[0].get("value", ""))

        # 限制 summary 长度（防止整篇文章塞进来）
        if len(summary) > 500:
            summary = summary[:500] + "..."

        author = ""
        if "author" in e:
            author = _strip_html(e.author)
        elif "authors" in e and e.authors:
            author = _strip_html(e.authors[0].get("name", ""))

        items.append(
            {
                "id": f"rss:{link}",
                "title": title,
                "url": link,
                "platform": "rss",
                "source": {
                    "type": "rss",
                    "id": url,
                    "name": author or feed_title,
                    "feed_title": feed_title,
                },
                "duration_sec": None,
                "views": None,
                "published_at": _parse_dt(e),
                "summary": summary,
                "lang": lang,
            }
        )

    print(f"   ✓ 拿到 {len(items)} 条", file=sys.stderr)
    return items


def fetch_many(
    feeds: list[dict[str, Any]],
    max_per_feed: int = 30,
    sleep: float = 0.5,
) -> list[dict[str, Any]]:
    """批量抓多个 feed"""
    all_items: dict[str, dict[str, Any]] = {}

    for fc in feeds:
        url = fc.get("url")
        if not url:
            continue
        try:
            items = fetch_one_feed(
                url,
                feed_name=fc.get("name"),
                lang=fc.get("lang", ""),
                max_items=max_per_feed,
            )
        except Exception as e:
            if fc.get("optional"):
                print(f"   ⚠️ optional 源失败已忽略: {fc.get('name')} ({e})", file=sys.stderr)
                continue
            raise

        for it in items:
            all_items.setdefault(it["id"], it)
        time.sleep(sleep)

    return list(all_items.values())


def main() -> int:
    parser = argparse.ArgumentParser(description="RSS / Atom 抓取器")
    parser.add_argument("url", help="RSS feed URL")
    parser.add_argument("--name", help="feed 显示名（可选）")
    parser.add_argument("--lang", default="", help="语言标记（zh / en）")
    parser.add_argument("--max", type=int, default=30, help="最大条数")
    parser.add_argument("--out", help="输出文件路径")
    args = parser.parse_args()

    items = fetch_one_feed(
        args.url,
        feed_name=args.name,
        lang=args.lang,
        max_items=args.max,
    )

    output = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "kind": "rss",
        "feed_url": args.url,
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
