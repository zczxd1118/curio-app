"""
agent/auto_sources.py

为新加领域自动生成合理的默认信源。从 server.py 抽出来，不依赖 Flask。

主入口：default_sources_for(domain_name) → list[dict]
"""

from __future__ import annotations
import re
from typing import List, Dict


def is_chinese_name(s: str) -> bool:
    chars = re.findall(r"[\u4e00-\u9fa5]", s or "")
    return len(chars) / max(1, len(s or "")) > 0.3


# 一些常见的中文领域 → 英文关键词映射，避免依赖外部翻译 API
ZH_EN_HINTS: Dict[str, List[str]] = {
    "金融": ["finance", "fed", "rates"],
    "半导体": ["semiconductor", "chip", "tsmc"],
    "人工智能": ["AI", "LLM", "agent"],
    "ai": ["AI", "LLM", "agent"],
    "AI": ["AI", "LLM", "agent"],
    "大厂讯息": ["Google", "Microsoft", "Apple", "Tencent", "Alibaba"],
    "大厂": ["Google", "Microsoft", "Apple", "Tencent", "Alibaba"],
    "互联网": ["startup", "tech", "Google"],
    "电动车": ["Tesla", "BYD", "EV"],
    "新能源": ["battery", "renewable", "solar"],
    "生物科技": ["biotech", "CRISPR", "synthetic biology"],
    "量子计算": ["quantum", "qubit", "IBM Quantum"],
    "区块链": ["blockchain", "crypto", "bitcoin"],
    "加密货币": ["bitcoin", "ethereum", "crypto"],
    "游戏": ["game", "gamedev", "unreal"],
    "音乐": ["music", "spotify", "audio"],
    "汽车": ["auto", "car", "Tesla"],
    "教育": ["edtech", "education", "learning"],
    "医疗": ["healthtech", "medicine", "biotech"],
    "气候": ["climate", "carbon", "renewable"],
    "宇宙": ["space", "SpaceX", "NASA"],
    "航天": ["space", "SpaceX", "rocket"],
    "vibe-coding": ["AI coding", "Claude Code", "Cursor"],
    "vibe coding": ["AI coding", "Claude Code", "Cursor"],
}


def _translate_safe(zh: str) -> List[str]:
    """尽量从映射表拿，没的话用 MyMemory（如果可用），最后退回原文"""
    # 1. 直接查映射
    if zh in ZH_EN_HINTS:
        return ZH_EN_HINTS[zh]
    lower = zh.lower()
    if lower in ZH_EN_HINTS:
        return ZH_EN_HINTS[lower]
    # 2. 子串匹配
    for k, v in ZH_EN_HINTS.items():
        if k in zh or zh in k:
            return v
    # 3. 翻译 API（可能被墙，要兜底）
    try:
        from agent.translate import translate
        en = translate(zh, target="en-US")
        words = [w.strip() for w in (en or "").split() if len(w.strip()) >= 2]
        if words:
            return words[:3]
    except Exception:
        pass
    # 4. 退回原文
    return [zh]


def default_sources_for(domain_name: str) -> List[Dict]:
    """根据领域名生成默认信源列表。

    返回结构对应 sources.yaml 里 topics.{topic}.sources[]：
        [{name, kind: hn_search/rss, query/url, days, min_points, lang, optional}]
    """
    name = (domain_name or "").strip()
    if not name:
        return []

    is_zh = is_chinese_name(name)
    sources: List[Dict] = []

    if is_zh:
        # 中文领域：翻译成英文关键词搜 HN，再加几条 RSSHub 中文源
        en_words = _translate_safe(name)
        for w in en_words[:3]:
            if not w:
                continue
            sources.append({
                "name": f"HN · {w}",
                "kind": "hn_search",
                "query": w,
                "days": 30,
                "min_points": 30,
                "lang": "en",
            })

        # 大厂讯息类：加 The Verge / TechCrunch RSS
        if any(brand in name for brand in ["大厂", "互联网", "科技", "公司"]):
            sources.append({
                "name": "The Verge",
                "kind": "rss",
                "url": "https://www.theverge.com/rss/index.xml",
                "lang": "en",
                "optional": True,
            })
            sources.append({
                "name": "TechCrunch",
                "kind": "rss",
                "url": "https://techcrunch.com/feed/",
                "lang": "en",
                "optional": True,
            })

        # AI / 编程类：加 Latent Space
        if any(k in name for k in ["AI", "ai", "人工智能", "vibe", "编程", "代码"]):
            sources.append({
                "name": "Latent Space",
                "kind": "rss",
                "url": "https://www.latent.space/feed",
                "lang": "en",
                "optional": True,
            })

        # 通用中文 RSS（RSSHub）
        sources.append({
            "name": "量子位（公众号 via RSSHub）",
            "kind": "rss",
            "url": "https://rsshub.app/wechat/ranking/all/qbitai",
            "lang": "zh",
            "optional": True,
        })
        sources.append({
            "name": "机器之心（RSSHub）",
            "kind": "rss",
            "url": "https://rsshub.app/jiqizhixin/zixun",
            "lang": "zh",
            "optional": True,
        })
    else:
        # 英文领域：拆几个独立关键词搜 HN
        words = [w.strip() for w in name.split() if len(w.strip()) >= 2]
        for w in words[:3] or [name]:
            sources.append({
                "name": f"HN · {w}",
                "kind": "hn_search",
                "query": w,
                "days": 30,
                "min_points": 30,
                "lang": "en",
            })

    return sources


def default_topics_for(domain_name: str) -> Dict:
    """生成包装好的 topics dict，可直接塞到 sources.yaml.domains.{slug}.topics"""
    sources = default_sources_for(domain_name)
    if not sources:
        return {}
    return {
        "default": {
            "name": domain_name,
            "sources": sources,
        }
    }


if __name__ == "__main__":
    # 调试入口
    import sys
    name = sys.argv[1] if len(sys.argv) > 1 else "大厂讯息"
    import json
    print(json.dumps(default_topics_for(name), ensure_ascii=False, indent=2))
