#!/usr/bin/env python3
"""
B 站字幕抓取（三级 fallback）

路径优先级：
  A. player/v2 拿官方字幕（用户上传，最准但极少）
  A+. player/v2 带 SESSDATA 拿 AI 自动字幕（核心路径，覆盖率 ~80%）
  C. yt-dlp 下载音轨 + Whisper 转写（兜底，慢但 100% 覆盖）

用法：
  python fetch_subtitle.py BV1YR5E6EE9o          # 自动尝试 A → A+ → C
  python fetch_subtitle.py BV1YR5E6EE9o --no-whisper  # 不走 Whisper

SESSDATA 配置：
  把 cookie 放到 content-curator/.bili_secret（一行，仅 SESSDATA 值）
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

import requests

ROOT = Path(__file__).resolve().parent.parent
SECRET_PATH = ROOT / ".bili_secret"
SUBTITLE_DIR = ROOT / "topics" / "subtitles"

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"


def load_sessdata() -> str | None:
    """从 .bili_secret 读 SESSDATA（只读第一行）"""
    if not SECRET_PATH.exists():
        return None
    text = SECRET_PATH.read_text(encoding="utf-8").strip()
    # 兼容 "SESSDATA=xxx" 和裸 "xxx"
    if text.startswith("SESSDATA="):
        text = text.split("=", 1)[1]
    return text or None


def make_session(use_login: bool = True) -> tuple[requests.Session, bool]:
    """建立 session。返回 (session, is_logged_in)"""
    sess = requests.Session()
    sess.headers.update(
        {
            "User-Agent": UA,
            "Referer": "https://www.bilibili.com/",
            "Accept": "application/json, text/plain, */*",
        }
    )

    is_logged_in = False
    if use_login:
        sessdata = load_sessdata()
        if sessdata:
            sess.cookies.set("SESSDATA", sessdata, domain=".bilibili.com")
            is_logged_in = True
            print("🔐 使用 SESSDATA 登录态", file=sys.stderr)

    # 建立基础 cookies（buvid3 等）
    try:
        sess.get("https://www.bilibili.com/", timeout=10)
    except requests.RequestException:
        pass

    return sess, is_logged_in


def get_video_meta(bvid: str, sess: requests.Session) -> dict | None:
    """通过 BV 拿到 aid 和 cid"""
    r = sess.get(
        "https://api.bilibili.com/x/web-interface/view",
        params={"bvid": bvid},
        timeout=10,
    )
    if r.status_code != 200:
        return None
    d = r.json()
    if d.get("code") != 0:
        print(f"⚠️ meta 接口 code={d.get('code')} msg={d.get('message')}", file=sys.stderr)
        return None
    return d.get("data")


# ----------------------------- Path A / A+ ----------------------------- #
def try_official_subtitle(
    aid: int, cid: int, bvid: str, sess: requests.Session
) -> list[dict] | None:
    """调 player/v2 拿字幕列表（A 路径，登录时可拿 AI 字幕）"""
    r = sess.get(
        "https://api.bilibili.com/x/player/v2",
        params={"aid": aid, "cid": cid, "bvid": bvid},
        timeout=10,
    )
    if r.status_code != 200:
        return None
    d = r.json()
    if d.get("code") != 0:
        return None
    subs = d.get("data", {}).get("subtitle", {}).get("subtitles", []) or []
    return subs or None


def fetch_subtitle_json(url: str, sess: requests.Session) -> dict | None:
    """字幕 URL 是 //i0.hdslb.com/... 形式"""
    if url.startswith("//"):
        url = "https:" + url
    try:
        r = sess.get(url, timeout=15)
        if r.status_code == 200:
            return r.json()
    except requests.RequestException as e:
        print(f"⚠️ 字幕 URL 抓取失败: {e}", file=sys.stderr)
    return None


def subtitle_json_to_text(sub_json: dict) -> str:
    """字幕 JSON {body: [{from, to, content}, ...]} 转纯文本"""
    body = sub_json.get("body", []) or []
    lines = []
    for seg in body:
        content = seg.get("content", "").strip()
        if content:
            lines.append(content)
    return "\n".join(lines)


def subtitle_json_to_srt(sub_json: dict) -> str:
    """转 SRT 时间戳格式（Whisper 友好）"""
    body = sub_json.get("body", []) or []
    lines = []
    for i, seg in enumerate(body, 1):
        t_from = seg.get("from", 0)
        t_to = seg.get("to", 0)
        content = seg.get("content", "").strip()
        if not content:
            continue
        lines.append(str(i))
        lines.append(f"{_fmt_srt_ts(t_from)} --> {_fmt_srt_ts(t_to)}")
        lines.append(content)
        lines.append("")
    return "\n".join(lines)


def _fmt_srt_ts(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


# ----------------------------- Path C: Whisper ----------------------------- #
def has_whisper() -> bool:
    return shutil.which("whisper") is not None or shutil.which("whisper-cpp") is not None


def has_ytdlp() -> bool:
    return shutil.which("yt-dlp") is not None


def whisper_transcribe(bvid: str, work_dir: Path) -> str | None:
    """yt-dlp 下载音轨 + Whisper 转写"""
    if not has_ytdlp():
        print("❌ 未安装 yt-dlp（pip install yt-dlp）", file=sys.stderr)
        return None
    if not has_whisper():
        print("❌ 未安装 whisper（pip install openai-whisper 或 brew install whisper-cpp）", file=sys.stderr)
        return None

    work_dir.mkdir(parents=True, exist_ok=True)
    audio_path = work_dir / f"{bvid}.m4a"
    print(f"📥 yt-dlp 下载音轨 → {audio_path}", file=sys.stderr)
    rc = subprocess.run(
        [
            "yt-dlp",
            "-f", "bestaudio[ext=m4a]/bestaudio",
            "-o", str(audio_path),
            f"https://www.bilibili.com/video/{bvid}",
        ],
        capture_output=True, text=True,
    )
    if rc.returncode != 0:
        print(f"❌ yt-dlp 失败: {rc.stderr[:200]}", file=sys.stderr)
        return None

    print(f"🎙 Whisper 转写中（这步慢，30 分钟视频约 3-5 分钟）...", file=sys.stderr)
    transcript_path = work_dir / f"{bvid}.txt"
    rc = subprocess.run(
        [
            "whisper",
            str(audio_path),
            "--language", "Chinese",
            "--model", "small",
            "--output_dir", str(work_dir),
            "--output_format", "txt",
        ],
        capture_output=True, text=True,
    )
    if rc.returncode != 0:
        print(f"❌ whisper 失败: {rc.stderr[:200]}", file=sys.stderr)
        return None

    if transcript_path.exists():
        return transcript_path.read_text(encoding="utf-8")
    return None


# ----------------------------- 主流程 ----------------------------- #
def fetch_subtitle(
    bvid: str,
    use_whisper: bool = True,
) -> dict[str, Any]:
    """主入口：返回 {bvid, source, content, ...}"""
    sess, is_logged_in = make_session(use_login=True)

    meta = get_video_meta(bvid, sess)
    if not meta:
        return {"bvid": bvid, "ok": False, "error": "meta fetch failed"}

    aid = meta["aid"]
    cid = meta["cid"]
    title = meta.get("title", "")
    duration = meta.get("duration", 0)
    owner = meta.get("owner", {}).get("name", "")

    print(f"📺 {bvid} · {title[:40]} · {owner} · {duration}s", file=sys.stderr)

    # 路径 A / A+
    subs = try_official_subtitle(aid, cid, bvid, sess)
    if subs:
        print(f"✅ 找到 {len(subs)} 条字幕", file=sys.stderr)
        # 优先选中文 / AI 字幕
        chosen = (
            next((s for s in subs if s.get("lan", "").startswith("zh")), None)
            or subs[0]
        )
        sub_url = chosen.get("subtitle_url", "")
        sub_json = fetch_subtitle_json(sub_url, sess)
        if sub_json:
            text = subtitle_json_to_text(sub_json)
            return {
                "bvid": bvid,
                "ok": True,
                "source": "official" if chosen.get("type") == 0 else "ai_subtitle",
                "lan": chosen.get("lan"),
                "title": title,
                "owner": owner,
                "duration_sec": duration,
                "content": text,
                "raw_json": sub_json,
            }

    # 路径 A 失败 → 提示
    if not is_logged_in:
        print("⚠️ 没有官方字幕。建议提供 SESSDATA cookie 拿 AI 字幕。", file=sys.stderr)
        print("   把 SESSDATA 写到 content-curator/.bili_secret", file=sys.stderr)
    else:
        print("⚠️ 即使带登录也没拿到字幕，可能视频未生成 AI 字幕", file=sys.stderr)

    # 路径 C: Whisper
    if use_whisper:
        print("🔄 尝试 Whisper 兜底...", file=sys.stderr)
        text = whisper_transcribe(bvid, ROOT / "tmp" / "whisper")
        if text:
            return {
                "bvid": bvid,
                "ok": True,
                "source": "whisper",
                "lan": "zh",
                "title": title,
                "owner": owner,
                "duration_sec": duration,
                "content": text,
            }

    return {
        "bvid": bvid,
        "ok": False,
        "title": title,
        "owner": owner,
        "duration_sec": duration,
        "error": "no subtitle available (try SESSDATA or whisper)",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="B 站字幕抓取")
    parser.add_argument("bvid", help="BV 号")
    parser.add_argument("--no-whisper", action="store_true", help="跳过 Whisper 兜底")
    parser.add_argument("--out", help="输出文件路径（默认 topics/subtitles/<bvid>.txt）")
    args = parser.parse_args()

    result = fetch_subtitle(args.bvid, use_whisper=not args.no_whisper)

    if not result.get("ok"):
        print(f"\n❌ 失败：{result.get('error')}", file=sys.stderr)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1

    out_path = Path(args.out) if args.out else SUBTITLE_DIR / f"{args.bvid}.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    text = result["content"]
    out_path.write_text(text, encoding="utf-8")

    # 同时存元数据
    meta_path = out_path.with_suffix(".meta.json")
    meta = {k: v for k, v in result.items() if k not in ("content", "raw_json")}
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n✅ 字幕已保存（{result['source']}）")
    print(f"   📄 文本：{out_path}（{len(text)} 字）")
    print(f"   📋 元数据：{meta_path}")
    print(f"   📺 {result.get('title', '')[:50]}")
    print(f"   👤 {result.get('owner', '')} · {result.get('duration_sec', 0)}s")
    print(f"\n前 200 字预览：")
    print(text[:200])
    return 0


if __name__ == "__main__":
    sys.exit(main())
