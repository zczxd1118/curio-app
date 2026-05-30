#!/usr/bin/env python3
"""
B 站字幕探针：批量检查多条视频是否有官方字幕

输入：BV 列表
输出：每条视频的字幕情况（有/无、语言、URL）
"""
from __future__ import annotations

import json
import sys
import time
import requests

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
HEADERS = {
    "User-Agent": UA,
    "Referer": "https://www.bilibili.com/",
    "Accept": "application/json",
}


def get_video_meta(bvid: str, sess: requests.Session) -> dict | None:
    """通过 BV 拿到 aid 和 cid"""
    r = sess.get(
        "https://api.bilibili.com/x/web-interface/view",
        headers=HEADERS,
        params={"bvid": bvid},
        timeout=10,
    )
    if r.status_code != 200:
        return None
    d = r.json()
    if d.get("code") != 0:
        return None
    return d.get("data")


def get_subtitle_info(aid: int, cid: int, bvid: str, sess: requests.Session) -> dict:
    """调 player/v2 拿字幕列表"""
    r = sess.get(
        "https://api.bilibili.com/x/player/v2",
        headers=HEADERS,
        params={"aid": aid, "cid": cid, "bvid": bvid},
        timeout=10,
    )
    if r.status_code != 200:
        return {"error": f"HTTP {r.status_code}"}
    d = r.json()
    if d.get("code") != 0:
        return {"error": d.get("message")}
    return d.get("data", {}).get("subtitle", {})


def fetch_subtitle_content(url: str, sess: requests.Session) -> dict | None:
    """字幕 URL 是 //i0.hdslb.com/... 形式，拼 https: 前缀"""
    if not url:
        return None
    if url.startswith("//"):
        url = "https:" + url
    try:
        r = sess.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            return r.json()
    except Exception as e:
        return {"error": str(e)}
    return None


def probe_one(bvid: str, sess: requests.Session) -> dict:
    """探针单条视频"""
    meta = get_video_meta(bvid, sess)
    if not meta:
        return {"bvid": bvid, "error": "meta fetch failed"}

    aid = meta.get("aid")
    cid = meta.get("cid")
    title = meta.get("title", "")[:40]
    duration = meta.get("duration", 0)
    owner = meta.get("owner", {}).get("name", "")

    sub = get_subtitle_info(aid, cid, bvid, sess)
    subtitles = sub.get("subtitles", []) or []

    result = {
        "bvid": bvid,
        "title": title,
        "owner": owner,
        "duration_sec": duration,
        "aid": aid,
        "cid": cid,
        "subtitle_count": len(subtitles),
        "subtitles": [
            {
                "lan": s.get("lan"),
                "lan_doc": s.get("lan_doc"),
                "type": s.get("type"),  # 0=用户上传 1=AI 生成
                "ai_type": s.get("ai_type"),
                "subtitle_url": s.get("subtitle_url", ""),
            }
            for s in subtitles
        ],
    }
    return result


def main() -> None:
    # 必读区 6 条 BV
    bvids = [
        "BV14rzQB9EJj",  # 马克 · Claude Code 全攻略
        "BV1KoGE6cE53",  # AI 超元域 · ultrawork
        "BV1CTRNBsECb",  # 王尼互 · 漏洞赏金
        "BV1KJySBfEjW",  # 数字黑魔法 · 抛弃 Cursor
        "BV1f8j8zZEac",  # 张小珺 · 姚顺宇访谈
        "BV1cqcCe1ECG",  # WhynotTV · 翁家翌
    ]

    sess = requests.Session()
    # 建立基础 cookies
    try:
        sess.get("https://www.bilibili.com/", headers={"User-Agent": UA}, timeout=10)
    except Exception:
        pass

    print(f"探测 {len(bvids)} 条视频...\n", file=sys.stderr)
    results = []
    for bv in bvids:
        r = probe_one(bv, sess)
        results.append(r)
        sub_n = r.get("subtitle_count", 0)
        symbol = "✅" if sub_n > 0 else "❌"
        print(f"{symbol} {bv}  字幕={sub_n}  {r.get('owner','?')}  {r.get('duration_sec','?')}s  {r.get('title','')[:30]}", file=sys.stderr)
        if sub_n > 0:
            for s in r["subtitles"]:
                print(f"     · {s['lan']} ({s['lan_doc']}) type={s['type']} {s['subtitle_url'][:60]}", file=sys.stderr)
        time.sleep(1.0)

    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
