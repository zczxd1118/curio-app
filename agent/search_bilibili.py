#!/usr/bin/env python3
"""
B 站搜索抓取（Curio M0 唯一信源）

用 B 站公开搜索接口拉候选内容池。
不需要登录、不需要 Cookie（基础搜索）。

注意：B 站接口偶发反爬，有 wbi 签名要求。
M0 用最简版：直接走 search/all/v2，按关键词列表拉取。

输出：标准化候选 JSON（title / url / up_name / up_mid / duration_sec / views / published_at / desc）
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote

import requests

ROOT = Path(__file__).resolve().parent.parent
SEARCH_URL = "https://api.bilibili.com/x/web-interface/wbi/search/all/v2"
SEARCH_FALLBACK = "https://api.bilibili.com/x/web-interface/search/all/v2"

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0.0.0 Safari/537.36"
)

HEADERS = {
    "User-Agent": UA,
    "Referer": "https://www.bilibili.com/",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
}


def _strip_em(text: str | None) -> str:
    """B 站搜索结果里 title 带 <em class="keyword"> 高亮，要清理"""
    if not text:
        return ""
    return re.sub(r"<[^>]+>", "", text).strip()


def _parse_duration(s: str | int | None) -> int:
    """B 站 duration 可能是 'mm:ss' 或秒数，统一转秒"""
    if s is None:
        return 0
    if isinstance(s, int):
        return s
    if isinstance(s, str) and ":" in s:
        parts = s.split(":")
        try:
            if len(parts) == 2:
                return int(parts[0]) * 60 + int(parts[1])
            if len(parts) == 3:
                return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
        except ValueError:
            return 0
    try:
        return int(s)
    except (ValueError, TypeError):
        return 0


def search_one_keyword(
    keyword: str,
    page: int = 1,
    session: requests.Session | None = None,
) -> list[dict[str, Any]]:
    """搜单个关键词，返回视频列表（已清洗）"""
    sess = session or requests.Session()

    # 先建立 SESSDATA-less 的 buvid3，避免接口直接拒绝
    try:
        sess.get("https://www.bilibili.com/", headers=HEADERS, timeout=10)
    except requests.RequestException:
        pass

    params = {
        "keyword": keyword,
        "page": page,
        "order": "totalrank",   # 综合排序；可换 "pubdate"（最新）/"click"（最多播放）
        "duration": 0,           # 0=全部；2=10-30 分；3=>30 分
    }

    items: list[dict[str, Any]] = []

    for url in (SEARCH_FALLBACK, SEARCH_URL):   # 先用免签的，wbi 作 fallback
        try:
            resp = sess.get(url, headers=HEADERS, params=params, timeout=15)
        except requests.RequestException as e:
            print(f"  ⚠️ 请求失败 ({url[:40]}...): {e}", file=sys.stderr)
            continue

        if resp.status_code != 200:
            print(f"  ⚠️ HTTP {resp.status_code} from {url[:40]}", file=sys.stderr)
            continue

        try:
            data = resp.json()
        except json.JSONDecodeError:
            print(f"  ⚠️ 非 JSON 响应（可能被反爬）", file=sys.stderr)
            continue

        if data.get("code") != 0:
            msg = data.get("message", "unknown")
            print(f"  ⚠️ B站返回 code={data.get('code')} msg={msg}", file=sys.stderr)
            continue

        # search/all/v2 的 result 是分组数组
        groups = data.get("data", {}).get("result", []) or []
        videos_group = next(
            (g for g in groups if g.get("result_type") == "video"),
            None,
        )
        if not videos_group:
            # 该 URL 拿到了 200 但没 video 组，换下一个 URL
            continue

        raw_list = videos_group.get("data", []) or []
        for v in raw_list:
            items.append({
                "id": f"bvid:{v.get('bvid', '')}" if v.get("bvid") else f"aid:{v.get('aid', '')}",
                "title": _strip_em(v.get("title")),
                "url": (v.get("arcurl") or f"https://www.bilibili.com/video/{v.get('bvid', '')}").strip(),
                "platform": "bilibili",
                "source": {
                    "type": "bilibili",
                    "id": str(v.get("mid", "")),
                    "name": _strip_em(v.get("author") or v.get("upic_name")),
                },
                "duration_sec": _parse_duration(v.get("duration")),
                "views": int(v.get("play") or 0),
                "danmaku": int(v.get("video_review") or 0),
                "favorites": int(v.get("favorites") or 0),
                "published_at": (
                    datetime.fromtimestamp(v.get("pubdate") or 0, tz=timezone.utc)
                    .isoformat()
                ) if v.get("pubdate") else None,
                "summary": _strip_em(v.get("description")),
                "matched_keyword": keyword,
            })
        return items   # 拿到结果就返回，不试第二个 URL

    return items


def search_keywords(
    keywords: list[str],
    pages_per_kw: int = 1,
    sleep: float = 1.2,
) -> list[dict[str, Any]]:
    """串行搜多个关键词，去重合并"""
    sess = requests.Session()
    all_items: dict[str, dict[str, Any]] = {}   # key=id, value=item

    for kw in keywords:
        print(f"🔍 搜索：{kw}", file=sys.stderr)
        for p in range(1, pages_per_kw + 1):
            items = search_one_keyword(kw, page=p, session=sess)
            print(f"   page {p} -> {len(items)} 条", file=sys.stderr)
            for it in items:
                if it["id"] in all_items:
                    # 合并 matched_keyword（同一视频被多关键词命中）
                    existing = all_items[it["id"]].setdefault("matched_keywords", [])
                    if it["matched_keyword"] not in existing:
                        existing.append(it["matched_keyword"])
                else:
                    it["matched_keywords"] = [it.pop("matched_keyword")]
                    all_items[it["id"]] = it
            time.sleep(sleep)
        time.sleep(sleep)

    return list(all_items.values())


def main() -> int:
    parser = argparse.ArgumentParser(
        description="B 站搜索抓取（Curio M0 唯一信源）",
    )
    parser.add_argument(
        "keywords",
        nargs="+",
        help="一个或多个搜索关键词，空格分隔",
    )
    parser.add_argument("--pages", type=int, default=1, help="每个关键词翻几页（默认 1）")
    parser.add_argument("--sleep", type=float, default=1.2, help="请求间隔秒（默认 1.2）")
    parser.add_argument("--out", type=str, help="输出文件路径（默认 stdout）")
    args = parser.parse_args()

    items = search_keywords(args.keywords, pages_per_kw=args.pages, sleep=args.sleep)

    # 简单排序：matched_keywords 数量 desc, views desc
    items.sort(
        key=lambda x: (len(x.get("matched_keywords", [])), x.get("views", 0)),
        reverse=True,
    )

    output = {
        "fetched_at": datetime.now(tz=timezone.utc).isoformat(),
        "platform": "bilibili",
        "keywords": args.keywords,
        "total": len(items),
        "items": items,
    }

    text = json.dumps(output, ensure_ascii=False, indent=2)

    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"✅ 已写入 {args.out}（{len(items)} 条）", file=sys.stderr)
    else:
        print(text)

    return 0


if __name__ == "__main__":
    sys.exit(main())
