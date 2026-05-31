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

- 用户领域：`半导体` / 子话题：`[]`
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
  "scored_at": "2026-05-31",
  "domain": "半导体",
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
    "id": "hn:48311647",
    "platform": "hackernews",
    "title": "Claude Opus 4.8",
    "url": "https://www.anthropic.com/news/claude-opus-4-8",
    "source": "craigmart",
    "published_at": "2026-05-28T16:49:14+00:00",
    "summary": "",
    "points": 1734,
    "comments": 1350
  },
  {
    "id": "hn:48206768",
    "platform": "hackernews",
    "title": "Meta blocks human rights accounts from reaching audiences in Saudi Arabia, UAE",
    "url": "https://www.alqst.org/ar/posts/1190",
    "source": "giuliomagnifico",
    "published_at": "2026-05-20T12:43:41+00:00",
    "summary": "",
    "points": 1079,
    "comments": 469
  },
  {
    "id": "hn:47920074",
    "platform": "hackernews",
    "title": "Men who stare at walls",
    "url": "https://www.alexselimov.com/posts/men_who_stare_at_walls/",
    "source": "aselimov3",
    "published_at": "2026-04-27T11:08:26+00:00",
    "summary": "",
    "points": 724,
    "comments": 337
  },
  {
    "id": "hn:48192383",
    "platform": "hackernews",
    "title": "Show HN: Forge – Guardrails take an 8B model from 53% to 99% on agentic tasks",
    "url": "https://github.com/antoinezambelli/forge",
    "source": "zambelli",
    "published_at": "2026-05-19T12:23:07+00:00",
    "summary": "",
    "points": 687,
    "comments": 252
  },
  {
    "id": "hn:48143880",
    "platform": "hackernews",
    "title": "Mullvad exit IPs are surprisingly identifying",
    "url": "https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/",
    "source": "RGBCube",
    "published_at": "2026-05-15T02:35:35+00:00",
    "summary": "",
    "points": 613,
    "comments": 389
  },
  {
    "id": "hn:48164287",
    "platform": "hackernews",
    "title": "Zerostack – A Unix-inspired coding agent written in pure Rust",
    "url": "https://crates.io/crates/zerostack/1.0.0",
    "source": "gidellav",
    "published_at": "2026-05-16T22:23:50+00:00",
    "summary": "",
    "points": 575,
    "comments": 308
  },
  {
    "id": "hn:48184402",
    "platform": "hackernews",
    "title": "Was my $48K GPU server worth it?",
    "url": "https://rosmine.ai/2026/05/13/was-my-48k-gpu-worth-it/",
    "source": "apwheele",
    "published_at": "2026-05-18T19:33:03+00:00",
    "summary": "",
    "points": 568,
    "comments": 449
  },
  {
    "id": "hn:48191602",
    "platform": "hackernews",
    "title": "Show HN: Gaussian Splat of a Strawberry",
    "url": "https://superspl.at/scene/84df8849",
    "source": "danybittel",
    "published_at": "2026-05-19T10:38:47+00:00",
    "summary": "",
    "points": 529,
    "comments": 200
  },
  {
    "id": "hn:48259808",
    "platform": "hackernews",
    "title": "Migrating from Go to Rust",
    "url": "https://corrode.dev/learn/migration-guides/go-to-rust/",
    "source": "jabits",
    "published_at": "2026-05-24T18:31:42+00:00",
    "summary": "",
    "points": 477,
    "comments": 507
  },
  {
    "id": "hn:48169874",
    "platform": "hackernews",
    "title": "Show HN: Semble – Code search for agents that uses 98% fewer tokens than grep",
    "url": "https://github.com/MinishLab/semble",
    "source": "Bibabomas",
    "published_at": "2026-05-17T15:37:07+00:00",
    "summary": "",
    "points": 445,
    "comments": 151
  },
  {
    "id": "hn:47776035",
    "platform": "hackernews",
    "title": "Anna's Archive loses $322M Spotify piracy case without a fight",
    "url": "https://torrentfreak.com/annas-archive-loses-322-million-spotify-piracy-case-without-a-fight/",
    "source": "askl",
    "published_at": "2026-04-15T08:05:18+00:00",
    "summary": "",
    "points": 444,
    "comments": 451
  },
  {
    "id": "hn:47827259",
    "platform": "hackernews",
    "title": "Stop trying to engineer your way out of listening to people",
    "url": "https://ashley.rolfmore.com/stop-trying-to-engineer-your-way-out-of-listening-to-people/",
    "source": "walterbell",
    "published_at": "2026-04-19T20:09:09+00:00",
    "summary": "",
    "points": 438,
    "comments": 280
  },
  {
    "id": "hn:48238025",
    "platform": "hackernews",
    "title": "U.S. researchers face new restrictions on publishing with foreign collaborators",
    "url": "https://www.science.org/content/article/u-s-researchers-face-new-restrictions-publishing-foreign-collaborators",
    "source": "ceejayoz",
    "published_at": "2026-05-22T16:23:08+00:00",
    "summary": "",
    "points": 419,
    "comments": 279
  },
  {
    "id": "hn:48299220",
    "platform": "hackernews",
    "title": "What Apple and Google are doing to push notifications",
    "url": "https://www.jacquescorbytuech.com/writing/what-apple-and-google-are-doing-your-push-notifications",
    "source": "iamacyborg",
    "published_at": "2026-05-27T19:24:10+00:00",
    "summary": "",
    "points": 416,
    "comments": 408
  },
  {
    "id": "hn:47901064",
    "platform": "hackernews",
    "title": "ASML became the chokepoint for cutting-edge chips",
    "url": "https://worksinprogress.co/issue/the-worlds-most-complex-machine/",
    "source": "mellosouls",
    "published_at": "2026-04-25T12:47:32+00:00",
    "summary": "",
    "points": 416,
    "comments": 248
  },
  {
    "id": "hn:48206340",
    "platform": "hackernews",
    "title": "Saying goodbye to asm.js",
    "url": "https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html",
    "source": "eqrion",
    "published_at": "2026-05-20T12:01:56+00:00",
    "summary": "",
    "points": 410,
    "comments": 158
  },
  {
    "id": "hn:48307231",
    "platform": "hackernews",
    "title": "AMD pulls a bait-and-switch on Linux users with Vivado licensing changes",
    "url": "https://itsfoss.com/news/amd-vivado-bait-and-switch-on-linux-users/",
    "source": "teleforce",
    "published_at": "2026-05-28T10:56:55+00:00",
    "summary": "",
    "points": 336,
    "comments": 166
  },
  {
    "id": "hn:48293080",
    "platform": "hackernews",
    "title": "Incident with Pull Requests, Issues, Git Operations and API Requests",
    "url": "https://www.githubstatus.com/incidents/xy1tt3hs572m",
    "source": "maxnoe",
    "published_at": "2026-05-27T12:15:14+00:00",
    "summary": "",
    "points": 335,
    "comments": 209
  },
  {
    "id": "hn:48165797",
    "platform": "hackernews",
    "title": "I found ultra-pure quantum crystals in an abandoned mine in the Atacama desert",
    "url": "https://medium.com/@breid.at/ultra-pure-quantum-crystals-from-an-abandoned-mine-in-a-mysterious-desert-93cc87d12314",
    "source": "vi_sextus_vi",
    "published_at": "2026-05-17T03:25:23+00:00",
    "summary": "",
    "points": 287,
    "comments": 119
  },
  {
    "id": "hn:48231247",
    "platform": "hackernews",
    "title": "Gnutella: A Protocol Outliving the World That Created It",
    "url": "https://rickcarlino.com/notes/p2p/gnutella-explanation.html",
    "source": "rickcarlino",
    "published_at": "2026-05-22T02:24:48+00:00",
    "summary": "",
    "points": 272,
    "comments": 93
  },
  {
    "id": "hn:48221896",
    "platform": "hackernews",
    "title": "Show HN: I Dedicated 4 Years to Mastering Offline Password Cracking",
    "url": "https://news.ycombinator.com/item?id=48221896",
    "source": "bojta-lepenye",
    "published_at": "2026-05-21T12:56:37+00:00",
    "summary": "",
    "points": 268,
    "comments": 60
  },
  {
    "id": "hn:48270111",
    "platform": "hackernews",
    "title": "The bootstrapper's EU stack for under €10 per month",
    "url": "https://eualternative.eu/guides/bootstrapper-free-tier-eu-stack/",
    "source": "sparkling",
    "published_at": "2026-05-25T18:37:05+00:00",
    "summary": "",
    "points": 225,
    "comments": 84
  },
  {
    "id": "hn:47595971",
    "platform": "hackernews",
    "title": "My son pleasured himself on Gemini Live. Entire family's Google accounts banned",
    "url": "https://old.reddit.com/r/LegalAdviceUK/comments/1s92fql/my_son_pleasured_himself_in_front_of_gemini_live/",
    "source": "samlinnfer",
    "published_at": "2026-04-01T02:14:42+00:00",
    "summary": "",
    "points": 208,
    "comments": 165
  },
  {
    "id": "hn:48321076",
    "platform": "hackernews",
    "title": "Real-time LLM Inference on Standard GPUs: 3k tokens/s per request",
    "url": "https://blog.kog.ai/real-time-llm-inference-on-standard-gpus-3-000-tokens-s-per-request/",
    "source": "NicoConstant",
    "published_at": "2026-05-29T09:47:23+00:00",
    "summary": "",
    "points": 204,
    "comments": 91
  },
  {
    "id": "hn:47896163",
    "platform": "hackernews",
    "title": "Show HN: I've built a nice home server OS",
    "url": "https://lightwhale.asklandd.dk/",
    "source": "Zta77",
    "published_at": "2026-04-24T21:42:26+00:00",
    "summary": "",
    "points": 194,
    "comments": 91
  },
  {
    "id": "hn:48226038",
    "platform": "hackernews",
    "title": "Chewing gum restores dad's taste and smell years after Covid",
    "url": "https://discover.swns.com/2026/05/chewing-gum-restores-dads-taste-and-smell-years-after-covid/",
    "source": "speckx",
    "published_at": "2026-05-21T17:14:56+00:00",
    "summary": "",
    "points": 193,
    "comments": 106
  },
  {
    "id": "hn:48210590",
    "platform": "hackernews",
    "title": "Ask HN: Shouldn't Google need to give a public statement about Railway incident?",
    "url": "https://news.ycombinator.com/item?id=48210590",
    "source": "srameshc",
    "published_at": "2026-05-20T16:50:54+00:00",
    "summary": "",
    "points": 180,
    "comments": 106
  },
  {
    "id": "hn:48266422",
    "platform": "hackernews",
    "title": "Microsoft pulls plug on plans for 244-acre data center in Caledonia (2025)",
    "url": "https://www.tmj4.com/news/racine-county/microsoft-pulls-plug-on-plans-for-244-acre-data-center-in-caledonia-after-community-pushback",
    "source": "cdrnsf",
    "published_at": "2026-05-25T13:09:53+00:00",
    "summary": "",
    "points": 179,
    "comments": 188
  },
  {
    "id": "hn:48247005",
    "platform": "hackernews",
    "title": "Matrix Multiplications on GPUs Run Faster When Given “Predictable” Data (2024)",
    "url": "https://www.thonking.ai/p/strangely-matrix-multiplications",
    "source": "tosh",
    "published_at": "2026-05-23T12:11:47+00:00",
    "summary": "",
    "points": 172,
    "comments": 57
  },
  {
    "id": "hn:48265056",
    "platform": "hackernews",
    "title": "IBM Spins Off the First Pure-Play Quantum Chip Foundry",
    "url": "https://futurumgroup.com/insights/2-billion-chips-act-investment-in-quantum-bets-on-ibms-300mm-superconducting-silicon/",
    "source": "rbanffy",
    "published_at": "2026-05-25T09:43:03+00:00",
    "summary": "",
    "points": 158,
    "comments": 73
  },
  {
    "id": "hn:48250980",
    "platform": "hackernews",
    "title": "Air France and Airbus found guilty of manslaughter over 2009 plane crash",
    "url": "https://www.bbc.com/news/articles/czd2qmdvmq6o",
    "source": "baal80spam",
    "published_at": "2026-05-23T20:09:13+00:00",
    "summary": "",
    "points": 135,
    "comments": 132
  },
  {
    "id": "hn:48189539",
    "platform": "hackernews",
    "title": "Fender escalates legal campaign against S-style guitars",
    "url": "https://www.guitarworld.com/gear/electric-guitars/fender-cease-and-desist-lsl-instruments",
    "source": "rectang",
    "published_at": "2026-05-19T05:28:30+00:00",
    "summary": "",
    "points": 131,
    "comments": 132
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
    "id": "hn:48256108",
    "platform": "hackernews",
    "title": "What it takes to transpose a matrix",
    "url": "https://gudok.xyz/transpose/",
    "source": "tosh",
    "published_at": "2026-05-24T10:30:39+00:00",
    "summary": "",
    "points": 105,
    "comments": 19
  },
  {
    "id": "hn:48225040",
    "platform": "hackernews",
    "title": "Launch HN: Runtime (YC P26) – Sandboxed coding agents for everyone on a team",
    "url": "https://www.runtm.com/",
    "source": "gustrigos",
    "published_at": "2026-05-21T16:07:13+00:00",
    "summary": "",
    "points": 102,
    "comments": 30
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
    "id": "hn:48209105",
    "platform": "hackernews",
    "title": "Stable Audio 3",
    "url": "https://arxiv.org/abs/2605.17991",
    "source": "guardienaveugle",
    "published_at": "2026-05-20T15:10:05+00:00",
    "summary": "",
    "points": 99,
    "comments": 18
  },
  {
    "id": "hn:48007145",
    "platform": "hackernews",
    "title": "ASML's Best Selling Product Isn't What You Think It Is",
    "url": "https://www.siliconimist.com/p/asmls-best-selling-product",
    "source": "johncole",
    "published_at": "2026-05-04T11:08:22+00:00",
    "summary": "",
    "points": 98,
    "comments": 43
  },
  {
    "id": "hn:48272393",
    "platform": "hackernews",
    "title": "Show HN: OpenBrief – Local-first video downloader/summarizer",
    "url": "https://github.com/tantara/openbrief",
    "source": "tantara",
    "published_at": "2026-05-25T21:50:03+00:00",
    "summary": "",
    "points": 92,
    "comments": 17
  },
  {
    "id": "hn:48183038",
    "platform": "hackernews",
    "title": "Cutting inference cold starts by 40x with LP, FUSE, C/R, and CUDA-checkpoint",
    "url": "https://modal.com/blog/truly-serverless-gpus",
    "source": "charles_irl",
    "published_at": "2026-05-18T17:56:26+00:00",
    "summary": "",
    "points": 91,
    "comments": 18
  },
  {
    "id": "hn:48041316",
    "platform": "hackernews",
    "title": "Show HN: PHP-fts – Full-text search engine in pure PHP, no extensions",
    "url": "https://github.com/olivier-ls/php-fts",
    "source": "asmodios",
    "published_at": "2026-05-06T20:28:17+00:00",
    "summary": "",
    "points": 89,
    "comments": 27
  },
  {
    "id": "hn:48265745",
    "platform": "hackernews",
    "title": "GPT Guesses Between 1 and 100",
    "url": "https://github.com/exmergo/research-chatgpt-guesses-between-1-and-100",
    "source": "adunk",
    "published_at": "2026-05-25T11:46:09+00:00",
    "summary": "",
    "points": 87,
    "comments": 73
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
    "id": "hn:47807609",
    "platform": "hackernews",
    "title": "Writing string.h functions using string instructions in asm x86-64 (2025)",
    "url": "https://pmasschelier.github.io/x86_64_strings/",
    "source": "thaisstein",
    "published_at": "2026-04-17T16:22:36+00:00",
    "summary": "",
    "points": 71,
    "comments": 7
  },
  {
    "id": "hn:48037923",
    "platform": "hackernews",
    "title": "Canadian fiddler sues Google after AI Overview claimed he was a sex offender",
    "url": "https://www.theguardian.com/music/2026/may/05/canadian-ashley-macisaac-fiddler-musician-singer-songwriter-sues-google-ai-sex-offender-ntwnfb",
    "source": "LordAtlas",
    "published_at": "2026-05-06T16:12:50+00:00",
    "summary": "",
    "points": 55,
    "comments": 27
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
    "id": "hn:48261543",
    "platform": "hackernews",
    "title": "San Francisco immigration court shuts down after purge of judges",
    "url": "https://apnews.com/article/san-francisco-immigration-court-closed-asylum-8a0946a7cd4bcc9bd925d075cabef44a",
    "source": "petethomas",
    "published_at": "2026-05-24T22:12:48+00:00",
    "summary": "",
    "points": 40,
    "comments": 9
  },
  {
    "id": "hn:48327222",
    "platform": "hackernews",
    "title": "AI will be used to estimate age of asylum seekers from next year",
    "url": "https://www.bbc.co.uk/news/articles/ce3pe36qe7ro",
    "source": "vylorn",
    "published_at": "2026-05-29T18:23:03+00:00",
    "summary": "",
    "points": 36,
    "comments": 40
  }
]
```
