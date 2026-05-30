#!/usr/bin/env python3
"""
HN / RSS 文章全文抓取（用 trafilatura 提取正文）

用法：
  python fetch_article.py "https://www.latent.space/p/cognition"
  python fetch_article.py @candidates.json --top 10   # 批量

带本地缓存（按 URL hash 存到 .article_cache/），避免重抓。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

import requests
import trafilatura

ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / ".article_cache"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

MAX_BODY_CHARS = 12000   # 给 LLM 的正文上限（避免 context 爆）


def cache_key(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]


def cache_get(url: str) -> str | None:
    p = CACHE_DIR / f"{cache_key(url)}.txt"
    if p.exists():
        return p.read_text(encoding="utf-8")
    return None


def cache_set(url: str, body: str) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    p = CACHE_DIR / f"{cache_key(url)}.txt"
    p.write_text(body, encoding="utf-8")


def fetch_article(url: str, use_cache: bool = True, timeout: int = 20) -> dict[str, Any]:
    """抓单篇文章，提取正文"""
    # HN 链接特殊处理：news.ycombinator.com 链接是评论页，不是文章本身
    if "news.ycombinator.com/item?" in url:
        # 这种情况下用 HN 评论页本身（trafilatura 也能从里面抽出讨论文本）
        pass

    if use_cache:
        cached = cache_get(url)
        if cached:
            return {"url": url, "ok": True, "body": cached, "from_cache": True}

    try:
        downloaded = trafilatura.fetch_url(url)
    except Exception as e:
        return {"url": url, "ok": False, "error": f"fetch error: {e}"}

    if not downloaded:
        return {"url": url, "ok": False, "error": "fetch_url returned empty"}

    text = trafilatura.extract(
        downloaded,
        include_comments=False,
        include_tables=False,
        favor_precision=True,
        no_fallback=False,
        output_format="markdown",
    )

    if not text:
        # fallback：raw html → 简单去 tag
        text = trafilatura.extract(downloaded, output_format="txt") or ""

    text = (text or "").strip()
    if not text:
        return {"url": url, "ok": False, "error": "extract returned empty"}

    if len(text) > MAX_BODY_CHARS:
        text = text[:MAX_BODY_CHARS] + f"\n\n[...truncated, original was {len(text)} chars]"

    cache_set(url, text)

    return {
        "url": url,
        "ok": True,
        "body": text,
        "char_count": len(text),
        "from_cache": False,
    }


def fetch_batch(items: list[dict], top: int | None = None) -> list[dict]:
    """批量抓一组候选条目"""
    if top:
        items = items[:top]
    out = []
    for i, it in enumerate(items, 1):
        url = it.get("url", "")
        title = it.get("title", "")[:50]
        if not url:
            continue
        print(f"📰 [{i}/{len(items)}] {title}", file=sys.stderr)
        r = fetch_article(url)
        cached = " (cache)" if r.get("from_cache") else ""
        if r["ok"]:
            print(f"   ✓ {r.get('char_count', len(r['body']))} chars{cached}", file=sys.stderr)
        else:
            print(f"   ✗ {r['error']}", file=sys.stderr)
        out.append({**it, "article": r})
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="抓 HN/RSS 文章全文（trafilatura）")
    parser.add_argument("url_or_file", help="URL 或 @file（含 items 数组的 JSON）")
    parser.add_argument("--top", type=int, help="批量时只取前 N 条")
    parser.add_argument("--out", help="输出文件路径")
    parser.add_argument("--no-cache", action="store_true")
    args = parser.parse_args()

    if args.url_or_file.startswith("@"):
        # 批量
        path = Path(args.url_or_file[1:])
        data = json.loads(path.read_text(encoding="utf-8"))
        items = data.get("items", []) if isinstance(data, dict) else data
        results = fetch_batch(items, top=args.top)
        text = json.dumps({"total": len(results), "items": results}, ensure_ascii=False, indent=2)
    else:
        r = fetch_article(args.url_or_file, use_cache=not args.no_cache)
        if r["ok"]:
            print(f"✅ {r.get('char_count', len(r['body']))} chars{' (cache)' if r.get('from_cache') else ''}", file=sys.stderr)
            print(f"\n--- 前 500 字预览 ---", file=sys.stderr)
            print(r["body"][:500], file=sys.stderr)
            print(f"---", file=sys.stderr)
        text = json.dumps(r, ensure_ascii=False, indent=2)

    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"\n✅ 已写入 {args.out}", file=sys.stderr)
    else:
        if not args.url_or_file.startswith("@"):
            # 单条不输出 JSON 到 stdout（已经预览过了）
            return 0
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
