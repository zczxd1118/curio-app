# Prompt: 内容打分 + 推荐理由

> Curio Agent 第 3 个动作：从候选池里挑出值得读的，每条说"为什么"
> v0.4：支持多平台候选（bilibili / hackernews / rss / ...）

---

## 角色

你是一位资深的「**信息领域主编**」。
用户的搜索引擎已经从**多个平台**给你拉来一堆候选内容（30-200 条），跨 B 站、HackerNews、英文博客 RSS 等。你要替用户**严格筛选**，并解释每个判断。

**核心心智**：你不是在评内容好坏，你是在替**这个具体的用户**判断"值不值得占用他/她 30 分钟的时间"。

---

## 输入

- 用户领域：`AI 算力 / 半导体` / 子话题：`[
  "default"
]`
- 用户画像：
  ```yaml
  identity: 电子信息工程大四 + 搜狗实习生 + AI 产品 / Agent 重度玩家。
正在做 content-curator 这个个人 Agent 项目，目标是简历亮点 + 长期个人工具。
  interests: [
  "vibe coding（Claude Code / Cursor / Windsurf 实战）",
  "AI Agent 工具构建（MCP / Skills / 子 Agent）",
  "AI 工程实践（RAG / 部署 / 推理优化）",
  "个人 Side Project 工作流",
  "大模型评测与发布动态"
]
  dislikes: [
  "纯流量号、标题党",
  "抽象方法论、玄学论调",
  "概念股炒作、热点蹭文",
  "1 分钟短视频科普（密度太低）",
  "套娃合集（\"10 个最强工具\"这类）"
]
  signal_preferences: [
  "要工程实践细节（具体到 commands、prompts、配置）",
  "要看到代码 / 示例 / 真实截图",
  "要\"为什么\"的解释（不只是 what，要 why）",
  "要新颖度（最近一周的进展优先于综述）",
  "长内容优先（10 分钟以上的深度内容）",
  "AI 领域名人访谈（行业 KOL/创业者的深度对话，比教程更稀缺）"
]
  reading_pace: 工作日 30 分钟，周末 2 小时。
日报 3-5 条必读，周报 5-8 条必读，每条配 2-3 句"为什么推"。
能跳就跳，宁缺毋滥。
  ```
- 历史反馈摘要（最近 4 周）：`[
  {
    "date": "2026-05-30",
    "issue": "ai/2026-05-30",
    "text": "想多看：AI 名人访谈 / 想少看：标题党 / 笔法：时间线很好",
    "applied": []
  },
  {
    "date": "2026-05-30",
    "issue": "ai/2026-05-30",
    "text": "想多看：AI 名人访谈 / 想少看：标题党 / 笔法：时间线很好",
    "applied": []
  },
  {
    "date": "2026-05-30",
    "issue": "ai/2026-05-30",
    "text": "想多看：AI 名人访谈 / 想少看：标题党教程 / 笔法：时间线很好",
    "applied": []
  },
  {
    "date": "2026-05-29",
    "text": "想多看 AI 领域名人访谈（不只是教程）；digest 跳过区展示太长，可以折叠/只展示前几条",
    "applied": [
      "加入 signal_preferences：\"AI 领域名人访谈\"",
      "explore prompt 在关键词扩展时纳入\"AI 访谈 / 对话 / 创业者\"等访谈类词",
      "digest 渲染：skip 区只展示前 5 条，其余只统计数字"
    ]
  }
]`
- 已推过的内容标题（避免重复）：`[]`
- 候选内容池（多平台合并，附 `platform` 字段）：见末尾

---

## 多平台的解读规则

每条候选都有 `platform` 字段，请按平台特性解读：

| 平台 | 信号特征 | 用法 |
|---|---|---|
| **hackernews** | 全球高热度英文新闻/讨论。`points` ≥ 100 通常是"圈子热议"，≥ 300 是"重大事件" | 优先级 P0，**英文圈最快的"今天发生了什么"信号** |
| **rss**（Substack / 个人博客）| 深度分析、行业内幕。无热度数据但**作者可信度极高**（如 Latent Space / Simon Willison）| 优先级 P0，是报纸的"深度版" |
| **bilibili** | 中文视频教程为主，标题党严重。视频 `duration_sec` < 600 通常是水文 | 优先级 P2，主要补充中文视角 |

**推送优先级原则**：

1. **HN 高热度新闻 (points ≥ 200)** → 几乎必入必读区，因为代表英文圈"今天最重要的事"
2. **可信博主 RSS 长文** → 入必读或参考，是报纸的"深度版"
3. **B 站重要 KOL 教程** → 仅在用户关心实操时入必读
4. **B 站标题党** → 直接跳过

---

## 任务

对每条候选打分，决定：

| 评级 | 含义 | 数量约束 |
|---|---|---|
| **必读** | 这条用户今天/本周必看 | 周报 5-8 条 / 日报 ≤3 条 |
| **参考** | 有时间可以看 | ≤8 条 |
| **跳过** | 跳过没损失，但记录"为什么跳"，给透明度 | 其余全部 |

**多平台覆盖目标**：必读区里**至少有 1 条 HN + 1 条 RSS + 1 条 B 站**（不强求平均，但避免单一平台垄断）

### 打分维度（每条都要）

| 维度 | 含义 | 1-10 |
|---|---|---|
| **新颖度** | 是不是最近、是不是没被别处反复讲。**HN points 越高越说明是 fresh news** | 越新颖越高 |
| **深度** | 工程细节 / 代码 / 真实经验 vs 泛泛而谈 | RSS 长文通常深度高，B 站短视频通常浅 |
| **相关度** | 跟用户画像/反馈历史的契合度 | echo chamber 风险——下面会处理 |

**最终评级公式**：
- **必读**：三项都 ≥ 7，或单项 ≥ 9（爆点新闻 / 重大融资 / 模型发布）
- **参考**：两项 ≥ 6
- **跳过**：其余

### 反 echo chamber 机制

为了避免 Profile 越准 → 推送越窄：
- 每期保留 **1-2 条"反偏好但有信号"** 的内容（评级=参考）
- 这类内容用 `is_diverse: true` 标记
- 在 `why_recommend` 里说："虽然你说不爱看 X，但这条值得看，因为..."

### 重复识别

- 候选池里多条讲同一事件（比如 5 条都是 Anthropic 融资 $965B）→ 选最权威的留下，其余进 skip
- 跨平台同一事件（HN + RSS + B 站都报道）→ **优先选英文源**（更早 + 更深），中文版进 skip
- 标题与 already_pushed 高度相似 → 跳过

---

## 输出（严格 JSON）

```json
{
  "scored_at": "2026-06-01",
  "domain": "AI 算力 / 半导体",
  "intro": "本期 149 条候选里挑了 6 条必读。最大新闻是 Anthropic 融资 $965B + Opus 4.8 发布——HN 上 491 票、Latent Space 当天发了深度分析。我把这条放在头版。考虑到你想多看实战案例，必读 #4 选了 Microsoft 取消 Claude Code license 这条业务侧新闻...",
  "must_read": [
    {
      "id": "hn:xxxxxx",
      "platform": "hackernews",
      "title": "Anthropic raises $965B Series H, releases Opus 4.8",
      "title_zh": "Anthropic 完成 H 轮 965 亿融资，发布 Opus 4.8",
      "keywords": ["Anthropic", "Series H", "Claude Opus 4.8", "Agent"],
      "summary_zh": "Anthropic 当地时间宣布完成 H 轮 965 亿美元融资，估值升至 1.2 万亿。同日发布 Claude Opus 4.8，agent 任务基准较 4.6 提升 11 个百分点，多模态推理与代码编辑首次拿到 GPT-5 同档分数。融资方除既有的 Google / Spark Capital 外，新增主权基金 Mubadala 与 GIC。Anthropic CEO Dario 表示新一轮主要用于扩大 H100 集群与对应的安全研究团队。",
      "url": "...",
      "source": "Latent Space",
      "score": { "novelty": 10, "depth": 8, "relevance": 10 },
      "why_recommend": "HN 491 票，本周英文圈头号事件。Anthropic 估值跳升 + Opus 4.8 同步发布意味着 vibe coding 的底层模型又升级了。",
      "is_diverse": false
    }
  ],
  "_note_for_llm": "重要：必读和参考的每一条都要给出三个字段（中文文章 title_zh 直接用原标题，summary_zh 仍要写）：\n- title_zh：人话中文标题，不是机翻；保留产品/公司名英文（如 Anthropic、TSMC、Forge）。\n- keywords：3-5 个核心词，混合英文产品名和中文话题词。\n- summary_zh：80-180 字的中文事实摘要，只陈述事件主体（什么人/公司/事件、关键数字、时间、地点），**不带主观判断**。主观点评放在 editor_note（独立流程）里，不要写到 summary_zh。",
  "reference": [...],
  "skip": [
    {
      "id": "...",
      "title": "...",
      "skip_reason": "B 站标题党教程，已有 HN 上的 Anthropic 官方深度版本"
    }
  ],
  "stats": {
    "candidates_total": 149,
    "must_read_count": 6,
    "reference_count": 6,
    "skip_count_shown": 10,
    "skip_count_actual": 137,
    "diverse_count": 1,
    "platform_distribution": {
      "must_read_by_platform": {"hackernews": 3, "rss": 2, "bilibili": 1}
    }
  }
}
```

---

## 重要原则

1. **宁缺毋滥**：用户 reading_pace 里说"周报 5-8 条必读"，就严守这个数。没好内容时，必读可以是 1 条甚至 0 条
2. **"为什么推"要具体**：禁用"内容很好"、"值得关注"、"高质量分享"。必须说出**这条独特在哪、跟用户哪个偏好对应**
3. **平台优先级**：HN 高热度 > RSS 深度博客 > B 站精选 KOL > B 站普通教程 > B 站标题党
4. **跨平台去重**：同一事件多平台报道时，**优先英文源**（更早+更深），中文版进 skip 但理由写"已被英文源 [HN xxx] 覆盖"
5. **诚实**：候选池里一条都没好的 → intro 写"本周搜了 N 条没找到值得推的，可能这周圈子太静了"
6. **结合反馈历史**：feedback_timeline 里说过"想多看 X" → 本期就要在 intro 里点出来"按你上次反馈，本期重点放在 X"


---

## 候选内容池

```json
[
  {
    "id": "rss:https://www.eetimes.com/beyond-the-factory-floor-xr-training-for-the-next-industrial-era/",
    "platform": "rss",
    "title": "Beyond the Factory Floor: XR Training for the Next Industrial Era",
    "url": "https://www.eetimes.com/beyond-the-factory-floor-xr-training-for-the-next-industrial-era/",
    "source": "Rebecca Pool",
    "published_at": "2026-06-01T07:30:00+00:00",
    "summary": "EU-funded project MASTER is using extended reality to transform how industrial robotics is taught and deployed. The post Beyond the Factory Floor: XR Training for the Next Industrial Era appeared first on EE Times.",
    "feed": "EE Times"
  },
  {
    "id": "rss:https://www.eetimes.com/the-stratosphere-race-haps-move-from-experiment-to-commercial-reality/",
    "platform": "rss",
    "title": "The Stratosphere Race: HAPS Move from Experiment to Commercial Reality",
    "url": "https://www.eetimes.com/the-stratosphere-race-haps-move-from-experiment-to-commercial-reality/",
    "source": "Rebecca Pool",
    "published_at": "2026-05-29T22:00:00+00:00",
    "summary": "Autonomous high-altitude platform stations are getting ready to bridge ground networks and LEO satellites. The post The Stratosphere Race: HAPS Move from Experiment to Commercial Reality appeared first on EE Times.",
    "feed": "EE Times"
  },
  {
    "id": "rss:https://www.eetimes.com/gartner-says-supply-chain-confront-geopolitical-and-ai-challenges/",
    "platform": "rss",
    "title": "Gartner Says Supply Chain Confront Geopolitical and AI Challenges",
    "url": "https://www.eetimes.com/gartner-says-supply-chain-confront-geopolitical-and-ai-challenges/",
    "source": "Pablo Valerio",
    "published_at": "2026-05-29T14:16:57+00:00",
    "summary": "Gartner Supply Chain Symposium highlights strategies to navigate chaos, orchestrate agility, and accelerate Innovation. The post Gartner Says Supply Chain Confront Geopolitical and AI Challenges appeared first on EE Times.",
    "feed": "EE Times"
  },
  {
    "id": "rss:https://www.eetimes.com/qilimanjaro-pushes-analog-quantum-as-ai-compute-demands-surge/",
    "platform": "rss",
    "title": "Qilimanjaro Pushes Analog Quantum as AI Compute Demands Surge",
    "url": "https://www.eetimes.com/qilimanjaro-pushes-analog-quantum-as-ai-compute-demands-surge/",
    "source": "Pat Brans",
    "published_at": "2026-05-29T08:30:00+00:00",
    "summary": "Qilimanjaro says analog quantum systems could reduce error correction and accelerate AI, optimization, and simulation. On May 28, its analog system joined the digital quantum computer at the Barcelona Supercomputing Center. The post Qilimanjaro Pushes Analog Quantum as AI Compute Demands Surge appea",
    "feed": "EE Times"
  },
  {
    "id": "rss:https://www.eetimes.com/majestic-labs-raises-100m-for-memory-pooling-ai-server/",
    "platform": "rss",
    "title": "Majestic Labs Raises $100M for Memory Pooling AI Server",
    "url": "https://www.eetimes.com/majestic-labs-raises-100m-for-memory-pooling-ai-server/",
    "source": "Sally Ward-Foxton",
    "published_at": "2026-05-28T22:00:00+00:00",
    "summary": "Server architecture will offer up to 100 TB of DRAM per accelerator. The post Majestic Labs Raises $100M for Memory Pooling AI Server appeared first on EE Times.",
    "feed": "EE Times"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-in-design-verification-from-experimentation-to-measurable-capability/",
    "platform": "rss",
    "title": "AI in Design Verification: From Experimentation to Measurable Capability",
    "url": "https://www.eetimes.com/ai-in-design-verification-from-experimentation-to-measurable-capability/",
    "source": "Mike Bartley",
    "published_at": "2026-05-28T14:28:52+00:00",
    "summary": "AI in design verification no longer asks if AI helps tasks, but does it measurably improve real verification flows? The post AI in Design Verification: From Experimentation to Measurable Capability appeared first on EE Times.",
    "feed": "EE Times"
  },
  {
    "id": "rss:https://www.eetimes.com/chiplets-ecosystems-and-europes-post-fab-semiconductor-strategy/",
    "platform": "rss",
    "title": "Chiplets, Ecosystems, and Europe’s Post-Fab Semiconductor Strategy",
    "url": "https://www.eetimes.com/chiplets-ecosystems-and-europes-post-fab-semiconductor-strategy/",
    "source": "Pat Brans",
    "published_at": "2026-05-28T08:38:29+00:00",
    "summary": "“Can Europe realistically compete on leading-edge fabs alone?” Maria Marced said. “No.” The post Chiplets, Ecosystems, and Europe’s Post-Fab Semiconductor Strategy appeared first on EE Times.",
    "feed": "EE Times"
  },
  {
    "id": "rss:https://www.eetimes.com/vicinity-unveils-trave-ai-native-sdr-platform-at-5g-acia-frankfurt/",
    "platform": "rss",
    "title": "Vicinity Unveils “TRAVE” — AI-Native SDR Platform at 5G-ACIA Frankfurt",
    "url": "https://www.eetimes.com/vicinity-unveils-trave-ai-native-sdr-platform-at-5g-acia-frankfurt/",
    "source": "Vicinity Technologies Limited",
    "published_at": "2026-05-28T01:00:00+00:00",
    "summary": "Vicinity Technologies Limited has officially unveiled TRAVE, its next-generation AI-native 5G/6G Software Defined Radio (SDR) platform, during the 5G-ACIA 5G User Conference in Frankfurt. The post Vicinity Unveils “TRAVE” — AI-Native SDR Platform at 5G-ACIA Frankfurt appeared first on EE Times.",
    "feed": "EE Times"
  },
  {
    "id": "rss:https://www.eetimes.com/canada-university-of-saskatchewan-acquires-quantum-computer/",
    "platform": "rss",
    "title": "Canada’s University of Saskatchewan Acquires Quantum Computer",
    "url": "https://www.eetimes.com/canada-university-of-saskatchewan-acquires-quantum-computer/",
    "source": "Gary Hilson",
    "published_at": "2026-05-27T19:00:00+00:00",
    "summary": "University of Saskatchewan will leverage quantum computing for health, defense, energy, and agriculture research. The post Canada’s University of Saskatchewan Acquires Quantum Computer appeared first on EE Times.",
    "feed": "EE Times"
  },
  {
    "id": "rss:https://www.eetimes.com/intelligent-configurable-i-o-edge-autonomy-thermal-efficiency-and-higher-uptime-in-industrial-control-systems/",
    "platform": "rss",
    "title": "Intelligent, Configurable I/O: Edge Autonomy, Thermal Efficiency, and Higher Uptime in Industrial Control Systems",
    "url": "https://www.eetimes.com/intelligent-configurable-i-o-edge-autonomy-thermal-efficiency-and-higher-uptime-in-industrial-control-systems/",
    "source": "Analog Devices",
    "published_at": "2026-05-27T14:00:00+00:00",
    "summary": "This paper explores how configurable and intelligent I/O technologies are transforming industrial control systems by enabling greater flexibility, improved thermal performance, and higher system uptime. Traditional fixed-function I/O architectures, while effective in stable environments, create inef",
    "feed": "EE Times"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/vpn/save-78-percent-on-nords-latest-complete-vpn-package-27-months-of-online-protection-for-usd107",
    "platform": "rss",
    "title": "Save 78% on Nord's latest Complete VPN package — 27 months of online protection for $107",
    "url": "https://www.tomshardware.com/software/vpn/save-78-percent-on-nords-latest-complete-vpn-package-27-months-of-online-protection-for-usd107",
    "source": "Stewart Bendle",
    "published_at": "2026-06-01T11:36:31+00:00",
    "summary": "Pick up 27 months of NordVPN coverage for just $107. Fast VPN connections, anti-virus protection, and a password manager for only $3.99 per month.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/us-closes-loophole-that-allowed-chinese-owned-subsidiaries-located-outside-china-to-buy-ai-chips-report-claims-that-hundreds-of-thousands-of-advanced-ai-chips-have-been-acquired-through-bis-blind-spot",
    "platform": "rss",
    "title": "US closes loophole that allowed Chinese-owned subsidiaries located outside China to buy AI chips — report claims that hundreds of thousands of advanced AI chips have been acquired through BIS blind spot",
    "url": "https://www.tomshardware.com/tech-industry/us-closes-loophole-that-allowed-chinese-owned-subsidiaries-located-outside-china-to-buy-ai-chips-report-claims-that-hundreds-of-thousands-of-advanced-ai-chips-have-been-acquired-through-bis-blind-spot",
    "source": "Jowi Morales",
    "published_at": "2026-06-01T11:32:24+00:00",
    "summary": "The BIS just issued a clarification that Chinese-owned subsidiaries are included in U.S. export controls, even if they're based outside of China. However, one source said that some companies have been using this loophole to acquire AI chips that estimated to be in the hundreds of thousands.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/negative-time-experiment-clears-peer-review-as-photons-appear-to-leave-an-atom-cloud-before-entering",
    "platform": "rss",
    "title": "Negative time experiment clears peer review as photons appear to leave an atom cloud before entering — groundbreaking quantum 'negative time' proven after 1 million test runs",
    "url": "https://www.tomshardware.com/tech-industry/negative-time-experiment-clears-peer-review-as-photons-appear-to-leave-an-atom-cloud-before-entering",
    "source": "Luke James",
    "published_at": "2026-06-01T11:30:00+00:00",
    "summary": "A University of Toronto experiment showing that photons can spend a negative amount of time inside a cloud of atoms has been published in Physical Review Letters.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/portable-monitors/acers-pm131qt-portable-monitor-is-a-12-3-inch-touchscreen-with-magnetic-mounting-a-built-in-kickstand-and-5-point-touch-1920-x-720-ips-screen-has-pogo-pins-for-a-keyboard-and-is-designed-for-secondary-and-in-vehicle-use",
    "platform": "rss",
    "title": "Acer’s PM131QT portable monitor is a 12.3-inch touchscreen with magnetic mounting, a built-in kickstand, and 5-point touch – 1920 x 720 IPS screen has pogo pins for a keyboard, and is designed for secondary and “in-vehicle” use",
    "url": "https://www.tomshardware.com/monitors/portable-monitors/acers-pm131qt-portable-monitor-is-a-12-3-inch-touchscreen-with-magnetic-mounting-a-built-in-kickstand-and-5-point-touch-1920-x-720-ips-screen-has-pogo-pins-for-a-keyboard-and-is-designed-for-secondary-and-in-vehicle-use",
    "source": "Matt Safford",
    "published_at": "2026-06-01T11:00:00+00:00",
    "summary": "Are you looking for a compact monitor for multiple uses around the home and on the go? Acer’s new PM131QT might be just what you’re looking for.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/resourceful-runner-can-race-my-own-ghost-using-homemade-meta-ray-ban-display-app-also-adds-bonus-coins-mini-leaderboard-and-more",
    "platform": "rss",
    "title": "Resourceful runner 'can race my own ghost' using homemade Meta Ray-Ban Display app — also adds bonus coins, mini leaderboard, and more",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/resourceful-runner-can-race-my-own-ghost-using-homemade-meta-ray-ban-display-app-also-adds-bonus-coins-mini-leaderboard-and-more",
    "source": "Mark Tyson",
    "published_at": "2026-06-01T10:48:30+00:00",
    "summary": "Video demonstrates brand-new gamified running app for the Meta Ray-Ban Display glasses.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/news/live/computex-2026-",
    "platform": "rss",
    "title": "Computex 2026 Live: Every update and announcement from day one in Taipei",
    "url": "https://www.tomshardware.com/news/live/computex-2026-",
    "source": "Stephen Warwick",
    "published_at": "2026-06-01T10:39:37+00:00",
    "summary": "Every update live from Taipei as Computex continues in Taiwan.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-warns-it-has-a-healthy-dose-of-paranoia-over-nvidia-entrance-into-pc-market-company-says-rtx-spark-is-great-for-the-market-while-touting-the-virtues-of-x86",
    "platform": "rss",
    "title": "Intel warns it has 'a healthy dose of paranoia' over Nvidia entrance into PC market — company says RTX Spark is 'great for the market' while touting the virtues of x86",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-warns-it-has-a-healthy-dose-of-paranoia-over-nvidia-entrance-into-pc-market-company-says-rtx-spark-is-great-for-the-market-while-touting-the-virtues-of-x86",
    "source": "Jake Roach",
    "published_at": "2026-06-01T10:30:00+00:00",
    "summary": "Intel reacts to Nvidia’s RTX Spark announcement, and says that it’s treating the green giant’s entrance into consumer SoCs with “a healthy dose of skepticism.\"",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/amd-promises-13-percent-uplift-with-new-expo-ultra-low-latency-overclocking-on-ddr5-dimms-automatic-memory-overclocking-delivers-4-percent-improvement-over-standard-expo-says-amd",
    "platform": "rss",
    "title": "AMD promises 13% uplift with new EXPO ‘Ultra Low Latency’ overclocking on DDR5 DIMMs — automatic memory overclocking delivers 4% improvement over standard EXPO, says AMD",
    "url": "https://www.tomshardware.com/pc-components/ram/amd-promises-13-percent-uplift-with-new-expo-ultra-low-latency-overclocking-on-ddr5-dimms-automatic-memory-overclocking-delivers-4-percent-improvement-over-standard-expo-says-amd",
    "source": "Jake Roach",
    "published_at": "2026-06-01T10:30:00+00:00",
    "summary": "AMD’s upcoming EXPO ‘Ultra Low Latency’ automatic memory overclocking promises a 13% improvement over standard DDR5 speeds, as well as a 4% jump compared to standard EXPO.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/we-went-hands-on-with-qualcomms-new-usd300-and-up-arm-laptop-platform-mystery-eight-core-cpu-in-active-cooled-snapdragon-c-laptop-surfaces-in-acer-aspire-go-15",
    "platform": "rss",
    "title": "We went hands-on with Qualcomm's new '$300 and up' ARM laptop platform with mystery eight-core CPU — active-cooled Snapdragon C laptop surfaces in Acer Aspire Go 15",
    "url": "https://www.tomshardware.com/laptops/we-went-hands-on-with-qualcomms-new-usd300-and-up-arm-laptop-platform-mystery-eight-core-cpu-in-active-cooled-snapdragon-c-laptop-surfaces-in-acer-aspire-go-15",
    "source": "Paul Alcorn",
    "published_at": "2026-06-01T10:00:00+00:00",
    "summary": "We've learned a few new details of the Snapdragon C platform at Computex 2026 by opening up a few Windows utilities on a demo unit.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/dlss-4-5-ray-reconstruction-update-arrives-in-august-for-better-ray-tracing-visuals-broader-training-data-set-and-second-gen-transformer-architecture-combine-for-improved-image-quality",
    "platform": "rss",
    "title": "DLSS 4.5 Ray Reconstruction update arrives in August for better ray tracing visuals — broader training data set and second-gen transformer architecture combine for improved image quality",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/dlss-4-5-ray-reconstruction-update-arrives-in-august-for-better-ray-tracing-visuals-broader-training-data-set-and-second-gen-transformer-architecture-combine-for-improved-image-quality",
    "source": "Jeffrey Kampman",
    "published_at": "2026-06-01T09:30:00+00:00",
    "summary": "At Computex 2026, Nvidia announced DLSS 4.5 Ray Reconstruction, an updated version of its neural RT denoiser with a second-gen transformer architecture and a broader training data set for better output image quality.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/microsoft-surface-laptop-ultra-weilds-nvidias-rtx-spark-superchip-with-128gb-of-ram-20-arm-cpu-cores-and-a-blackwell-gpu-15-inch-mini-led-pixelsense-ultra-display-rounds-out-the-powerful-package",
    "platform": "rss",
    "title": "Microsoft Surface Laptop Ultra weilds Nvidia's RTX Spark superchip with 128GB of RAM, 20 Arm CPU cores, and a Blackwell GPU — 15-inch mini-LED PixelSense Ultra display rounds out the powerful package",
    "url": "https://www.tomshardware.com/laptops/microsoft-surface-laptop-ultra-weilds-nvidias-rtx-spark-superchip-with-128gb-of-ram-20-arm-cpu-cores-and-a-blackwell-gpu-15-inch-mini-led-pixelsense-ultra-display-rounds-out-the-powerful-package",
    "source": "Kunal Khullar",
    "published_at": "2026-06-01T09:00:00+00:00",
    "summary": "Powered by Nvidia's RTX Spark Superchip, the Surface Laptop Ultra features 20 Arm CPU cores, 6,144 CUDA cores, and up to 128GB of unified memory",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nvidia-unveils-dgx-sparrk-roadmap-for-laptops-and-desktop-pcs-at-computex-2026-three-generations-outlined-rubin-followed-by-rosa-feynman",
    "platform": "rss",
    "title": "Nvidia lays out RTX Spark roadmap for laptops and desktop PCs at Computex 2026 — three generations outlined, Rubin with LPDDR6 memory, followed by Rosa Feynman",
    "url": "https://www.tomshardware.com/pc-components/cpus/nvidia-unveils-dgx-sparrk-roadmap-for-laptops-and-desktop-pcs-at-computex-2026-three-generations-outlined-rubin-followed-by-rosa-feynman",
    "source": "Jeffrey Kampman",
    "published_at": "2026-06-01T05:55:07+00:00",
    "summary": "Along with its first-generation RTX Spark platform for desktop and laptop PCs, Nvidia CEO Jensen Huang revealed the company's commitment to future generations of those platforms on its future roadmaps.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory",
    "platform": "rss",
    "title": "Nvidia unveils RTX Spark Superchip for laptops and desktop PCs at Computex 2026 – new platform promises to turn Windows into an agentic AI OS with Arm CPU, Blackwell GPU, and 128GB unified memory",
    "url": "https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory",
    "source": "Jeffrey Kampman",
    "published_at": "2026-06-01T04:52:13+00:00",
    "summary": "At Computex 2026, Nvidia CEO Jensen Huang unveiled the RTX Spark Superchip, a new Arm laptop and desktop platform that powers agentic AI on Windows with a 20-core Arm CPU, powerful 6144-CUDA-core Blackwell GPU, and up to 128 GB of local memory.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-xeon-7-diamond-rapids-cpus-officially-launching-in-2027-on-intel-18a-p-next-gen-p-core-xeon-features-pcie-6-0-50-percent-higher-core-counts-and-twice-the-memory-bandwidth",
    "platform": "rss",
    "title": "Intel Xeon 7 ‘Diamond Rapids’ CPUs officially launching in 2027 on Intel 18A-P — next-gen P-core Xeon features PCIe 6.0, 50% higher core counts, and twice the memory bandwidth",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-xeon-7-diamond-rapids-cpus-officially-launching-in-2027-on-intel-18a-p-next-gen-p-core-xeon-features-pcie-6-0-50-percent-higher-core-counts-and-twice-the-memory-bandwidth",
    "source": "Jake Roach",
    "published_at": "2026-06-01T03:00:00+00:00",
    "summary": "Intel has officially confirmed its next-gen Xeon 7 Diamond Rapids CPUs are coming in 2027, featuring 50% higher core counts and twice the memory bandwidth of Xeon 6 in a bid to compete against AMD’s upcoming EPYC Venice CPUs.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/intel-details-long-awaited-crescent-island-ai-gpu-at-computex-boasts-up-to-480-gb-of-lpddr5x-to-combat-memory-shortages-company-shares-more-details-of-its-xe3p-inference-accelerator-at-computex",
    "platform": "rss",
    "title": "Intel details long-awaited Crescent Island AI GPU at Computex, boasts up to 480 GB of LPDDR5X to combat memory shortages — company shares more details of its Xe3P inference accelerator at Computex",
    "url": "https://www.tomshardware.com/pc-components/gpus/intel-details-long-awaited-crescent-island-ai-gpu-at-computex-boasts-up-to-480-gb-of-lpddr5x-to-combat-memory-shortages-company-shares-more-details-of-its-xe3p-inference-accelerator-at-computex",
    "source": "Jeffrey Kampman",
    "published_at": "2026-06-01T03:00:00+00:00",
    "summary": "Intel revealed more details of its next-gen Data Center GPU, code-named Crescent Island, at Computex 2026. This inference-optimized chip will feature up to 480GB of LPDDR5X memory for efficient handling of massive AI contexts.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-xeon-6-clearwater-forest-puts-18a-in-the-data-center-with-up-to-288-cores-576-mb-of-l3-cache-new-xeon-6990e-is-30-percent-faster-per-thread-than-192-core-amd-epyc-9965-says-intel",
    "platform": "rss",
    "title": "Intel Xeon 6+ ‘Clearwater Forest’ puts 18A in the data center with up to 288 cores, 576 MB of L3 cache — new Xeon 6990E+ is 30% faster per thread than 192-core AMD Epyc 9965, says Intel",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-xeon-6-clearwater-forest-puts-18a-in-the-data-center-with-up-to-288-cores-576-mb-of-l3-cache-new-xeon-6990e-is-30-percent-faster-per-thread-than-192-core-amd-epyc-9965-says-intel",
    "source": "Jake Roach",
    "published_at": "2026-06-01T03:00:00+00:00",
    "summary": "Intel is putting its 18A node into the data center with new Xeon 6+ Clearwater Forest CPUs, which pack up to 288 E-cores for dense compute.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amds-formerly-china-exclusive-radeon-rx-9070-gre-goes-global-for-usd549-on-june-2-rdna-4-gpu-will-bridge-the-gap-between-rx-9060-xt-and-rx-9070",
    "platform": "rss",
    "title": "AMD’s formerly China-exclusive Radeon RX 9070 GRE goes global for $549 on June 2 — RDNA 4 GPU will bridge the gap between RX 9060 XT and RX 9070",
    "url": "https://www.tomshardware.com/pc-components/gpus/amds-formerly-china-exclusive-radeon-rx-9070-gre-goes-global-for-usd549-on-june-2-rdna-4-gpu-will-bridge-the-gap-between-rx-9060-xt-and-rx-9070",
    "source": "Zhiye Liu",
    "published_at": "2026-06-01T02:00:21+00:00",
    "summary": "AMD has officially launched the Radeon RX 9070 GRE for $549, an RDNA 4 graphics card that was previously exclusive to the Chinese market.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/nvidia-keynote-computex-2026-gtc-taipei-where-to-watch",
    "platform": "rss",
    "title": "Watch Nvidia's Computex 2026 keynote here — Jensen Huang takes the stage for Computex and GTC Taipei at 8pm PT / 11pm ET on May 31",
    "url": "https://www.tomshardware.com/tech-industry/nvidia-keynote-computex-2026-gtc-taipei-where-to-watch",
    "source": "Jake Roach",
    "published_at": "2026-06-01T00:21:39+00:00",
    "summary": "Nvidia CEO Jensen Huang is set to take the stage at Computex 2026 and GTC Taipei. Here's how to watch the keynote address, where we could hear more about the rumored N1X.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-confirms-am5-support-through-2029-zen-4-and-5-platform-will-likely-see-two-more-generations-at-least",
    "platform": "rss",
    "title": "AMD confirms AM5 support through 2029 — Zen 4 and 5 platform will likely see two more generations, at least",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-confirms-am5-support-through-2029-zen-4-and-5-platform-will-likely-see-two-more-generations-at-least",
    "source": "Jake Roach",
    "published_at": "2026-06-01T00:00:00+00:00",
    "summary": "AMD confirmed it will support its current AM5 socket through 2029, extending the timeline by two years and likely lining up at least two more generations on the socket.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-brings-back-ryzen-7-5800x3d-launches-ryzen-7-7700x3d-to-combat-rising-component-prices-eight-core-x3d-cpus-arrive-under-usd350-for-am4-or-am5-ddr4-or-ddr5",
    "platform": "rss",
    "title": "AMD brings back Ryzen 7 5800X3D, launches Ryzen 7 7700X3D to combat rising component prices — eight-core X3D CPUs arrive under $350 for AM4 or AM5, DDR4 or DDR5",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-brings-back-ryzen-7-5800x3d-launches-ryzen-7-7700x3d-to-combat-rising-component-prices-eight-core-x3d-cpus-arrive-under-usd350-for-am4-or-am5-ddr4-or-ddr5",
    "source": "Jake Roach",
    "published_at": "2026-06-01T00:00:00+00:00",
    "summary": "AMD is rereleasing the Ryzen 7 5800X3D and introducing the Ryzen 7 7700X3D, both eight-core chips with 3DV-Cache targeting midrange gamers who’ve been under the thumb of rising component prices.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/alienware-debuts-39-34-inch-oled-gaming-monitors-rgb-stripe-tandem-and-penta-tandem-tech-should-boost-color-performance-and-text-clarity",
    "platform": "rss",
    "title": "Alienware debuts 39, 34-inch OLED gaming monitors — RGB Stripe Tandem and Penta Tandem tech should boost color performance and text clarity",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/alienware-debuts-39-34-inch-oled-gaming-monitors-rgb-stripe-tandem-and-penta-tandem-tech-should-boost-color-performance-and-text-clarity",
    "source": "Brandon Hill",
    "published_at": "2026-05-31T23:00:00+00:00",
    "summary": "Alienware hits the ground running at Computex with four new gaming monitors covering OLED and VA panel types.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/dell-xps-13-targets-macbook-neo-with-intels-wildcat-lake-usd699-starting-price-usd599-for-students",
    "platform": "rss",
    "title": "Dell XPS 13 targets MacBook Neo with Intel's Wildcat Lake — $699 starting price, $599 for students",
    "url": "https://www.tomshardware.com/laptops/dell-xps-13-targets-macbook-neo-with-intels-wildcat-lake-usd699-starting-price-usd599-for-students",
    "source": "Andrew E. Freedman",
    "published_at": "2026-05-31T23:00:00+00:00",
    "summary": "Dell's XPS 13 is going after Apple's MacBook Neo with a $699 starting price, some higher specs, and Intel's new Wildcat Lake processors.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nvidias-long-awaited-n1-n1x-soc-specs-leak-ahead-of-computex-launch-n1-to-feature-up-to-20-arm-based-cores-standard-n1-equipped-with-12-and-10-core-configs",
    "platform": "rss",
    "title": "Nvidia's long-awaited N1/N1X SoC specs leak ahead of Computex launch — N1 to feature up to 20 Arm-based cores, standard N1 equipped with 12- and 10-core configs",
    "url": "https://www.tomshardware.com/pc-components/cpus/nvidias-long-awaited-n1-n1x-soc-specs-leak-ahead-of-computex-launch-n1-to-feature-up-to-20-arm-based-cores-standard-n1-equipped-with-12-and-10-core-configs",
    "source": "Hassam Nasir",
    "published_at": "2026-05-31T15:47:07+00:00",
    "summary": "The N1X reportedly comes in two SKUs: a top-end 20-core option with 6,144 CUDA cores matching the desktop RTX 5070, and a cut-down 18-core option with 5,120 CUDA cores. The standard N1 also has two configs, one with a 12-core CPU and 2,560 CUDA cores and a 10-core model with 2,048 CUDA cores.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/core-i7-14700f-gaming-pc-with-rtx-5060-32gb-of-ram-and-1tb-of-storage-gets-usd470-discount-neweggs-abs-cyclone-aqua-prebuilt-is-usd1-329-with-code",
    "platform": "rss",
    "title": "Core i7-14700F gaming PC with RTX 5060, 32GB of RAM, and 1TB of storage gets $470 discount — Newegg's ABS Cyclone Aqua prebuilt is $1,329 with code",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/core-i7-14700f-gaming-pc-with-rtx-5060-32gb-of-ram-and-1tb-of-storage-gets-usd470-discount-neweggs-abs-cyclone-aqua-prebuilt-is-usd1-329-with-code",
    "source": "Kunal Khullar",
    "published_at": "2026-05-31T15:01:35+00:00",
    "summary": "Newegg's ABS Cyclone Aqua prebuilt combines Intel's 20-core Core i7-14700F with Nvidia's RTX 5060, and 32GB of DDR5 memory for less than the cost of building a comparable system",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/softbank-to-spend-up-to-75-billion-on-french-ai-data-centers",
    "platform": "rss",
    "title": "SoftBank to spend up to $87 billion on French AI data centers — country offers ample nuclear grid that US sites lack",
    "url": "https://www.tomshardware.com/tech-industry/softbank-to-spend-up-to-75-billion-on-french-ai-data-centers",
    "source": "Luke James",
    "published_at": "2026-05-31T14:48:09+00:00",
    "summary": "SoftBank carries over $130 billion in debt and took a $40 billion bridge loan in March to fund its latest OpenAI investment.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/new-one-meter-cubed-3d-printer-pumps-out-large-scale-prints-at-3kg-an-hour-modix-mama-1000-also-needs-a-big-wallet-with-prices-starting-at-usd35-000",
    "platform": "rss",
    "title": "New one-meter-cubed 3D printer pumps out large-scale prints at 3kg an hour — Modix MAMA-1000 also needs a big wallet with prices starting at $35,000",
    "url": "https://www.tomshardware.com/3d-printing/new-one-meter-cubed-3d-printer-pumps-out-large-scale-prints-at-3kg-an-hour-modix-mama-1000-also-needs-a-big-wallet-with-prices-starting-at-usd35-000",
    "source": "Denise Bertacchi",
    "published_at": "2026-05-31T13:59:24+00:00",
    "summary": "The MAMA-1000 pellet 3D printer from Modix prints with a whopping 3kg an hour throughput.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/lenovo-yoga-slim-7x-review",
    "platform": "rss",
    "title": "Lenovo Yoga Slim 7x review: Snapdragon X2 Elite makes its case",
    "url": "https://www.tomshardware.com/laptops/lenovo-yoga-slim-7x-review",
    "source": "Charles Jefferies",
    "published_at": "2026-05-31T13:56:36+00:00",
    "summary": "The Yoga Slim 7x brings Snapdragon performance, long battery life, and an OLED display provided you’re fine with ARM apps and USB-C everything.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/microsoft-veteran-recalls-the-last-time-nvidia-and-arm-was-the-future-of-windows-shares-a-video-of-the-first-time-windows-ran-on-nvidia-tegra-arm-from-2010",
    "platform": "rss",
    "title": "Microsoft veteran recalls the last time Nvidia and Arm was the future of Windows — shares a video of ‘the first time Windows ran on Nvidia Tegra Arm’ from 2010",
    "url": "https://www.tomshardware.com/pc-components/microsoft-veteran-recalls-the-last-time-nvidia-and-arm-was-the-future-of-windows-shares-a-video-of-the-first-time-windows-ran-on-nvidia-tegra-arm-from-2010",
    "source": "Mark Tyson",
    "published_at": "2026-05-31T13:05:00+00:00",
    "summary": "Microsoft veteran Steven Sinofsky is here to remind folks that excitement about a new PC era fueled by Nvidia and Arm culminated in the Surface RT 16 years ago.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptomining/new-ai-compute-cryptocurrency-pearl-sparks-a-gpu-mining-rush-but-profitability-is-sliding",
    "platform": "rss",
    "title": "New AI-compute cryptocurrency Pearl sparks a GPU mining rush but profitability is already sliding — RTX 5090 daily revenue has halved to $17.19 since April",
    "url": "https://www.tomshardware.com/tech-industry/cryptomining/new-ai-compute-cryptocurrency-pearl-sparks-a-gpu-mining-rush-but-profitability-is-sliding",
    "source": "Luke James",
    "published_at": "2026-05-31T12:40:00+00:00",
    "summary": "A new cryptocurrency called Pearl has set off a short-lived GPU mining rush.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/robot-kits/the-ultimate-mosquito-killer-uses-lasers-and-ai-custom-model-trained-to-detect-and-lock-lasers-on-these-pests",
    "platform": "rss",
    "title": "The 'ultimate mosquito killer' uses lasers and AI — custom model trained to detect and lock lasers on these pests",
    "url": "https://www.tomshardware.com/maker-stem/robot-kits/the-ultimate-mosquito-killer-uses-lasers-and-ai-custom-model-trained-to-detect-and-lock-lasers-on-these-pests",
    "source": "Mark Tyson",
    "published_at": "2026-05-31T12:20:00+00:00",
    "summary": "A computer vision and robotics expert has created and trained what he boasts is “the ultimate mosquito killer” using machine learning and a laser.",
    "feed": "Latest from Tom's Hardware"
  },
  {
    "id": "hn:48012477",
    "platform": "hackernews",
    "title": "Offenders sentenced up to 10 years for spying on TSMC",
    "url": "https://www.taipeitimes.com/News/front/archives/2026/04/28/2003856358",
    "source": "ironyman",
    "published_at": "2026-05-04T18:04:33+00:00",
    "summary": "",
    "points": 127,
    "comments": 24
  },
  {
    "id": "hn:48274048",
    "platform": "hackernews",
    "title": "Taiwan Overtakes India as Fifth-Largest Stock Market",
    "url": "https://www.bloomberg.com/news/articles/2026-05-26/tsmc-s-relentless-rise-powers-taiwan-s-market-value-above-india",
    "source": "leopoldj",
    "published_at": "2026-05-26T01:49:54+00:00",
    "summary": "",
    "points": 10,
    "comments": 0
  },
  {
    "id": "hn:48352939",
    "platform": "hackernews",
    "title": "Nvidia RTX Spark",
    "url": "https://www.nvidia.com/en-us/products/rtx-spark/",
    "source": "shenli3514",
    "published_at": "2026-06-01T05:24:40+00:00",
    "summary": "",
    "points": 82,
    "comments": 67
  },
  {
    "id": "hn:48291230",
    "platform": "hackernews",
    "title": "Nvidia Vera CPU Benchmarks: Olympus Cores Delivering Great Performance",
    "url": "https://www.phoronix.com/review/nvidia-vera-benchmarks",
    "source": "naves",
    "published_at": "2026-05-27T08:15:35+00:00",
    "summary": "",
    "points": 54,
    "comments": 23
  },
  {
    "id": "hn:48245087",
    "platform": "hackernews",
    "title": "Nvidia Removes Gaming Revenue Category from Financial Reports",
    "url": "https://www.guru3d.com/story/nvidia-removes-gaming-revenue-category-from-financial-reports/",
    "source": "theanonymousone",
    "published_at": "2026-05-23T05:50:28+00:00",
    "summary": "",
    "points": 41,
    "comments": 10
  },
  {
    "id": "hn:48323697",
    "platform": "hackernews",
    "title": "The Nvidia Tax",
    "url": "https://www.cringely.com/2026/05/29/the-nvidia-tax/",
    "source": "HotGarbage",
    "published_at": "2026-05-29T14:41:43+00:00",
    "summary": "",
    "points": 23,
    "comments": 5
  },
  {
    "id": "hn:48284628",
    "platform": "hackernews",
    "title": "Trump's 25% cut on Nvidia chips to China backfired as Beijing blocks H200 sales",
    "url": "https://finance.yahoo.com/markets/stocks/articles/trumps-25-cut-nvidia-chips-194500691.html",
    "source": "frasermarlow",
    "published_at": "2026-05-26T19:21:02+00:00",
    "summary": "",
    "points": 21,
    "comments": 0
  },
  {
    "id": "hn:48352693",
    "platform": "hackernews",
    "title": "A powerful new chapter for Windows PCs, accelerated by Nvidia RTX Spark",
    "url": "https://blogs.windows.com/windowsexperience/2026/05/31/introducing-a-powerful-new-chapter-for-windows-pcs-accelerated-by-nvidia-rtx-spark/",
    "source": "WalterSobchak",
    "published_at": "2026-06-01T04:45:20+00:00",
    "summary": "",
    "points": 20,
    "comments": 19
  },
  {
    "id": "hn:48352951",
    "platform": "hackernews",
    "title": "Nvidia Announces RTX Spark",
    "url": "https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-date",
    "source": "rayhaanj",
    "published_at": "2026-06-01T05:26:06+00:00",
    "summary": "",
    "points": 15,
    "comments": 0
  },
  {
    "id": "hn:48343372",
    "platform": "hackernews",
    "title": "Dell Confirms XPS Laptop with Nvidia N1X at Computex",
    "url": "https://videocardz.com/newz/dell-confirms-xps-laptop-with-nvidia-n1x-at-computex",
    "source": "theanonymousone",
    "published_at": "2026-05-31T05:58:07+00:00",
    "summary": "",
    "points": 11,
    "comments": 0
  },
  {
    "id": "hn:48352705",
    "platform": "hackernews",
    "title": "Nvidia and Microsoft Reinvent Windows PCs for the Age of Personal AI",
    "url": "https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark",
    "source": "goshx",
    "published_at": "2026-06-01T04:47:29+00:00",
    "summary": "",
    "points": 10,
    "comments": 1
  },
  {
    "id": "hn:48195039",
    "platform": "hackernews",
    "title": "How Corrupt Is Trump? Here Are the Numbers",
    "url": "https://www.thebulwark.com/p/how-corrupt-is-trump-here-are-the-numbers-trades-chips-nvidia-pardons-settlement-fund",
    "source": "rawgabbit",
    "published_at": "2026-05-19T15:55:21+00:00",
    "summary": "",
    "points": 26,
    "comments": 2
  },
  {
    "id": "hn:48234574",
    "platform": "hackernews",
    "title": "How do you build a semiconductor company on something that's free?",
    "url": "https://www.siliconimist.com/p/the-open-source-silicon-business",
    "source": "johncole",
    "published_at": "2026-05-22T11:49:04+00:00",
    "summary": "",
    "points": 99,
    "comments": 36
  },
  {
    "id": "hn:48220446",
    "platform": "hackernews",
    "title": "IBM invented semiconductor manufacturing automation",
    "url": "https://spectrum.ieee.org/semiconductor-fabrication",
    "source": "rbanffy",
    "published_at": "2026-05-21T10:39:48+00:00",
    "summary": "",
    "points": 81,
    "comments": 6
  },
  {
    "id": "hn:48151102",
    "platform": "hackernews",
    "title": "Infineon Unveils Auto Industry's First RISC-V MCU: Linux Era for Semiconductors",
    "url": "https://en.infomaxai.com/news/articleView.html?idxno=116421",
    "source": "fork-bomber",
    "published_at": "2026-05-15T17:05:52+00:00",
    "summary": "",
    "points": 22,
    "comments": 1
  },
  {
    "id": "hn:48063979",
    "platform": "hackernews",
    "title": "When semiconductor materials misbehave",
    "url": "https://semiengineering.com/when-semiconductor-materials-misbehave/",
    "source": "PaulHoule",
    "published_at": "2026-05-08T14:43:50+00:00",
    "summary": "",
    "points": 21,
    "comments": 4
  }
]
```
