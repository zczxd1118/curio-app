"""
agent/translate.py — 中英对照翻译（用 MyMemory，免费、不需 key、不被墙）
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

CACHE_DIR = Path(__file__).resolve().parent.parent / ".translate_cache"
CACHE_DIR.mkdir(exist_ok=True)


def _cache_key(text: str, target: str) -> Path:
    import hashlib
    h = hashlib.sha1((target + "::" + text).encode("utf-8")).hexdigest()[:16]
    return CACHE_DIR / f"{h}.txt"


def is_chinese(text: str) -> bool:
    """文本主体是不是中文（汉字占比 > 30%）"""
    if not text:
        return False
    chinese_chars = re.findall(r"[\u4e00-\u9fa5]", text)
    return len(chinese_chars) / max(1, len(text)) > 0.3


def translate(text: str, target: str = "zh-CN", source: str = "auto") -> str:
    """翻译。失败返回原文。"""
    if not text or not text.strip():
        return text
    text = text.strip()
    # 中文不翻
    if target.startswith("zh") and is_chinese(text):
        return text

    # cache
    cache = _cache_key(text, target)
    if cache.exists():
        return cache.read_text(encoding="utf-8")

    # MyMemory 单次最长 500 字节，超过分段
    if len(text.encode("utf-8")) <= 480:
        result = _translate_chunk(text, target, source)
    else:
        result = _translate_long(text, target, source)

    cache.write_text(result, encoding="utf-8")
    return result


def _translate_chunk(text: str, target: str, source: str) -> str:
    try:
        from deep_translator import MyMemoryTranslator
        src = "en-US" if source == "auto" else source
        tgt = "zh-CN" if target.startswith("zh") else target
        r = MyMemoryTranslator(source=src, target=tgt).translate(text)
        return r or text
    except Exception as e:
        print(f"[translate] 失败 ({e})，返回原文", file=sys.stderr)
        return text


def _translate_long(text: str, target: str, source: str) -> str:
    """按句号 / 换行切，分段翻译再拼接"""
    # 切段
    parts = re.split(r"(?<=[\.\?\!。？！\n])", text)
    out = []
    buf = ""
    for p in parts:
        if len((buf + p).encode("utf-8")) > 460:
            if buf:
                out.append(_translate_chunk(buf.strip(), target, source))
                buf = p
            else:
                # 单段太长，硬切
                out.append(_translate_chunk(p[:200], target, source))
                buf = p[200:]
        else:
            buf += p
    if buf:
        out.append(_translate_chunk(buf.strip(), target, source))
    return " ".join(out).strip()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python translate.py <text>")
        sys.exit(1)
    print(translate(sys.argv[1]))
