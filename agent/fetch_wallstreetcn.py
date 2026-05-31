#!/usr/bin/env python3
"""华尔街见闻 API 抓取器

WSCN 自家 RSS 是空骨架，但 JSON API 直接返回结构化文章。
使用 GET https://api.wallstreetcn.com/apiv1/content/articles?cursor=&limit=20

返回字段（按 curio candidate schema 标准化）：
  id, title, url, summary, source, platform, lang, published_at, score
"""

from __future__ import annotations

import json
import sys
import time
import urllib.request
from datetime import datetime, timezone
from typing import Any


WSCN_API = "https://api.wallstreetcn.com/apiv1/content/articles?cursor=&limit={limit}"
UA = "curio-bot/1.0"


# 内容过滤：跳过涉及政治领导人/敏感政治话题的条目
_POLITICAL_BLOCKLIST = (
    "习近平", "总书记", "中央政治局", "政治局",
    "求是", "人民日报", "新华社", "央视",
    "李强", "王沪宁", "赵乐际", "蔡奇", "丁薛祥", "李希", "韩正",
    "中共中央", "国务院", "全国人大", "政协",
)


def _is_political(title: str, summary: str = "") -> bool:
    blob = (title or "") + " " + (summary or "")
    return any(kw in blob for kw in _POLITICAL_BLOCKLIST)


def fetch_wallstreetcn(limit: int = 20, source_name: str = "华尔街见闻") -> list[dict[str, Any]]:
    """抓最新 limit 条华尔街见闻文章，输出标准化 candidate 列表"""
    url = WSCN_API.format(limit=limit)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"  ⚠️ wallstreetcn fetch failed: {e}", file=sys.stderr)
        return []

    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        print(f"  ⚠️ wallstreetcn invalid JSON", file=sys.stderr)
        return []

    items = (data.get("data") or {}).get("items") or []
    out: list[dict[str, Any]] = []
    skipped_political = 0
    for it in items:
        title = (it.get("title") or "").strip()
        summary = (it.get("content_short") or it.get("brief") or "").strip()
        # 过滤政治敏感内容（领导人 / 党政机关相关），与产品无关
        if _is_political(title, summary):
            skipped_political += 1
            continue
        # WSCN API 返回字段：title, content_short, uri, display_time(unix), score
        aid = it.get("id") or it.get("uri", "").split("/")[-1]
        if not aid:
            continue
        published_ts = it.get("display_time") or 0
        try:
            published_at = datetime.fromtimestamp(published_ts, tz=timezone.utc).isoformat() if published_ts else ""
        except Exception:
            published_at = ""
        out.append({
            "id": f"wscn:{aid}",
            "title": title,
            "url": it.get("uri") or "",
            "summary": summary[:500],
            "source": source_name,
            "platform": "rss",  # 复用 rss 的下游逻辑
            "lang": "zh",
            "published_at": published_at,
            "points": it.get("score", 0),
        })
    if skipped_political:
        print(f"  ℹ️ 过滤掉 {skipped_political} 条政治敏感内容", file=sys.stderr)
    return out


def main():
    import argparse
    ap = argparse.ArgumentParser(description="抓华尔街见闻最新文章")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--source", default="华尔街见闻")
    ap.add_argument("--out", help="可选：输出 JSON 文件路径")
    args = ap.parse_args()

    items = fetch_wallstreetcn(limit=args.limit, source_name=args.source)
    print(f"✅ 抓到 {len(items)} 条", file=sys.stderr)
    if not items:
        return 1

    payload = {
        "source": args.source,
        "kind": "wallstreetcn_api",
        "fetched_at": datetime.now(tz=timezone.utc).isoformat(),
        "items": items,
    }
    txt = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(txt)
        print(f"✅ 写出 {args.out}")
    else:
        print(txt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
