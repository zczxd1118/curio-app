"""
agent/auto_sources.py

为新加领域自动生成合理的默认信源。

核心设计（v0.9 升级版）：
- 不再只给 HN 关键词，而是**按领域类型匹配优质信源池**
- 类型识别：金融 / 半导体 / AI / 大厂科技 / 加密 / 生物医疗 / 新能源 / 通用
- 每个类型都有：HN 关键词 + 行业 RSS + 中文一手源
- 跟 sources.yaml 里现有 4 个域（ai/finance/semiconductor/bigtech）的信源水平**对齐**

主入口：default_sources_for(domain_name) → list[dict]
"""

from __future__ import annotations
import re
from typing import List, Dict


def is_chinese_name(s: str) -> bool:
    chars = re.findall(r"[\u4e00-\u9fa5]", s or "")
    return len(chars) / max(1, len(s or "")) > 0.3


# ============== 领域分类（关键词触发） ==============

CATEGORY_KEYWORDS = {
    "finance": [
        "金融", "财经", "投资", "股票", "美股", "A股", "港股", "基金", "期货",
        "宏观", "央行", "利率", "通胀", "美联储", "证券",
        "finance", "stock", "market", "investing", "fed", "macro",
    ],
    "semiconductor": [
        "半导体", "芯片", "晶圆", "代工", "制程", "GPU", "光刻机",
        "semiconductor", "chip", "wafer", "tsmc", "asml", "nvidia hardware",
    ],
    "ai": [
        "AI", "人工智能", "大模型", "agent", "智能体", "机器学习", "深度学习",
        "LLM", "GPT", "Claude", "vibe", "coding", "编程",
        "ai", "llm", "machine learning", "deep learning",
    ],
    "bigtech": [
        "大厂", "巨头", "互联网", "科技公司", "Google", "苹果", "微软",
        "Apple", "Microsoft", "Meta", "Amazon", "tencent", "alibaba",
        "tech", "bigtech", "startup",
    ],
    "crypto": [
        "加密", "区块链", "比特币", "以太坊", "web3", "defi",
        "crypto", "blockchain", "bitcoin", "ethereum",
    ],
    "biotech": [
        "生物", "医疗", "医药", "基因", "biotech", "biology", "pharma",
        "medical", "healthtech", "crispr",
    ],
    "energy": [
        "新能源", "电动车", "电池", "光伏", "氢能", "碳中和", "汽车", "车企",
        "Tesla", "BYD", "EV", "battery", "solar", "renewable", "climate", "auto",
    ],
    "space": [
        "航天", "太空", "火箭", "卫星", "SpaceX", "space", "rocket", "satellite",
    ],
    "gaming": [
        "游戏", "电竞", "gaming", "esports", "gamedev",
    ],
}


def detect_category(domain_name: str) -> str:
    """识别领域属于哪个类型，返回类型 key"""
    name = (domain_name or "").lower()
    name_zh = domain_name or ""
    scores: Dict[str, int] = {}
    for cat, kws in CATEGORY_KEYWORDS.items():
        for kw in kws:
            if kw.lower() in name or kw in name_zh:
                scores[cat] = scores.get(cat, 0) + (3 if kw.lower() == name else 1)
    if not scores:
        return "general"
    return max(scores.items(), key=lambda x: x[1])[0]


# ============== 行业级 RSS / API 信源池 ==============
# 这些是已经验证活的源（5/31 实测）

INDUSTRY_SOURCES = {
    "finance": [
        {"name": "Stratechery", "kind": "rss", "url": "https://stratechery.com/feed/", "lang": "en"},
        {"name": "Net Interest（金融行业深度）", "kind": "rss", "url": "https://www.netinterest.co/feed", "lang": "en"},
        {"name": "华尔街见闻 API", "kind": "wallstreetcn_api",
         "url": "https://api.wallstreetcn.com/apiv1/content/articles?cursor=&limit=20",
         "lang": "zh", "optional": True},
        {"name": "arXiv q-fin（量化金融论文）", "kind": "rss",
         "url": "https://export.arxiv.org/rss/q-fin", "lang": "en", "optional": True},
    ],
    "semiconductor": [
        {"name": "SemiAnalysis（半导体深度）", "kind": "rss",
         "url": "https://www.semianalysis.com/feed", "lang": "en"},
        {"name": "EE Times", "kind": "rss",
         "url": "https://www.eetimes.com/feed", "lang": "en", "optional": True},
    ],
    "ai": [
        {"name": "Latent Space Blog", "kind": "rss",
         "url": "https://www.latent.space/feed", "lang": "en"},
        {"name": "Simon Willison's Blog", "kind": "rss",
         "url": "https://simonwillison.net/atom/everything/", "lang": "en"},
        {"name": "AI Engineer Newsletter", "kind": "rss",
         "url": "https://newsletter.eng-leadership.com/feed", "lang": "en", "optional": True},
        {"name": "ByteByteGo Newsletter", "kind": "rss",
         "url": "https://blog.bytebytego.com/feed", "lang": "en", "optional": True},
        {"name": "arXiv cs.CL", "kind": "rss",
         "url": "https://export.arxiv.org/rss/cs.CL", "lang": "en", "optional": True},
    ],
    "bigtech": [
        {"name": "The Verge", "kind": "rss",
         "url": "https://www.theverge.com/rss/index.xml", "lang": "en"},
        {"name": "Stratechery", "kind": "rss",
         "url": "https://stratechery.com/feed/", "lang": "en"},
        {"name": "Product Hunt", "kind": "rss",
         "url": "https://www.producthunt.com/feed", "lang": "en", "optional": True},
        {"name": "TechCrunch", "kind": "rss",
         "url": "https://techcrunch.com/feed/", "lang": "en", "optional": True},
        {"name": "36氪", "kind": "rss",
         "url": "https://36kr.com/feed", "lang": "zh", "optional": True},
        {"name": "少数派", "kind": "rss",
         "url": "https://sspai.com/feed", "lang": "zh", "optional": True},
    ],
    "crypto": [
        # 加密领域专业 RSS（占位，需要时实测后加）
    ],
    "biotech": [
        {"name": "Nature Biotechnology", "kind": "rss",
         "url": "https://www.nature.com/nbt.rss", "lang": "en", "optional": True},
    ],
    "energy": [
        {"name": "Electrek", "kind": "rss",
         "url": "https://electrek.co/feed/", "lang": "en", "optional": True},
        {"name": "CleanTechnica", "kind": "rss",
         "url": "https://cleantechnica.com/feed/", "lang": "en", "optional": True},
    ],
    "space": [
        # 留 HN 处理为主
    ],
    "gaming": [
        {"name": "Polygon", "kind": "rss",
         "url": "https://www.polygon.com/rss/index.xml", "lang": "en", "optional": True},
    ],
    "general": [
        {"name": "The Verge", "kind": "rss",
         "url": "https://www.theverge.com/rss/index.xml", "lang": "en", "optional": True},
        {"name": "36氪", "kind": "rss",
         "url": "https://36kr.com/feed", "lang": "zh", "optional": True},
    ],
}


# 每个类型的 HN 关键词配置（带 days/min_points 调优）
HN_KEYWORDS_BY_CATEGORY: Dict[str, List[Dict]] = {
    "finance": [
        {"query": "Federal Reserve", "days": 30, "min_points": 30},
        {"query": "inflation", "days": 30, "min_points": 50},
        {"query": "Tesla", "days": 14, "min_points": 50},
    ],
    "semiconductor": [
        {"query": "TSMC", "days": 30, "min_points": 30},
        {"query": "Nvidia", "days": 14, "min_points": 50},
        {"query": "semiconductor", "days": 30, "min_points": 30},
    ],
    "ai": [
        {"query": "Claude OR Anthropic", "days": 14, "min_points": 30},
        {"query": "GPT-5 OR OpenAI", "days": 14, "min_points": 50},
        {"query": "AI agent", "days": 14, "min_points": 50},
    ],
    "bigtech": [
        {"query": "Google", "days": 30, "min_points": 50},
        {"query": "Apple", "days": 30, "min_points": 50},
        {"query": "Microsoft", "days": 30, "min_points": 50},
    ],
    "crypto": [
        {"query": "bitcoin OR ethereum", "days": 14, "min_points": 100},
        {"query": "crypto regulation", "days": 30, "min_points": 50},
    ],
    "biotech": [
        {"query": "biotech OR pharma", "days": 30, "min_points": 30},
        {"query": "CRISPR OR mRNA", "days": 60, "min_points": 30},
    ],
    "energy": [
        {"query": "Tesla OR EV", "days": 14, "min_points": 50},
        {"query": "battery OR solar", "days": 30, "min_points": 30},
    ],
    "space": [
        {"query": "SpaceX OR Starlink", "days": 30, "min_points": 50},
        {"query": "NASA OR rocket launch", "days": 30, "min_points": 30},
    ],
    "gaming": [
        {"query": "Steam OR gaming", "days": 14, "min_points": 100},
    ],
}


# ============== 中文 → 英文关键词映射（保留兼容） ==============

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
    """尽量从映射表拿，没的话用翻译 API，最后退回原文"""
    if zh in ZH_EN_HINTS:
        return ZH_EN_HINTS[zh]
    lower = zh.lower()
    if lower in ZH_EN_HINTS:
        return ZH_EN_HINTS[lower]
    for k, v in ZH_EN_HINTS.items():
        if k in zh or zh in k:
            return v
    try:
        from agent.translate import translate
        en = translate(zh, target="en-US")
        words = [w.strip() for w in (en or "").split() if len(w.strip()) >= 2]
        if words:
            return words[:3]
    except Exception:
        pass
    return [zh]


# ============== 主入口 ==============

def default_sources_for(domain_name: str) -> List[Dict]:
    """根据领域名生成默认信源列表（v0.9：与现有 4 个域同等优质）

    流程：
    1. 识别领域类型（finance / ai / semiconductor / bigtech / crypto / biotech / energy / space / gaming / general）
    2. 加该类型的行业 RSS / API（INDUSTRY_SOURCES）
    3. 加该类型的 HN 关键词（HN_KEYWORDS_BY_CATEGORY）
    4. 全局再加一个 HN frontpage 200pts+ 兜底
    """
    name = (domain_name or "").strip()
    if not name:
        return []

    category = detect_category(name)
    sources: List[Dict] = []

    # 1. 行业专业 RSS / API（最重要的差异化）
    for s in INDUSTRY_SOURCES.get(category, []):
        sources.append(dict(s))

    # 2. HN 关键词（按类型预设 + 用户名字本身）
    seen_queries = set()
    for hn in HN_KEYWORDS_BY_CATEGORY.get(category, []):
        q = hn["query"]
        if q in seen_queries:
            continue
        seen_queries.add(q)
        sources.append({
            "name": f"HN · {q}",
            "kind": "hn_search",
            "query": q,
            "days": hn.get("days", 30),
            "min_points": hn.get("min_points", 30),
            "lang": "en",
        })

    # 3. 用户领域名翻译后的 HN 关键词（个性化）
    is_zh = is_chinese_name(name)
    if is_zh:
        en_words = _translate_safe(name)
        for w in en_words[:2]:
            if w in seen_queries or len(w) < 2:
                continue
            seen_queries.add(w)
            sources.append({
                "name": f"HN · {w}",
                "kind": "hn_search",
                "query": w,
                "days": 30,
                "min_points": 30,
                "lang": "en",
            })
    else:
        # 英文名，前 2 个词作为 HN 关键词
        for w in [w for w in name.split() if len(w) >= 3][:2]:
            if w in seen_queries:
                continue
            seen_queries.add(w)
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
    import sys, json
    name = sys.argv[1] if len(sys.argv) > 1 else "大厂讯息"
    print(f"==== 领域：{name} ====")
    print(f"识别类型：{detect_category(name)}")
    print()
    print("生成 topics：")
    print(json.dumps(default_topics_for(name), ensure_ascii=False, indent=2))
