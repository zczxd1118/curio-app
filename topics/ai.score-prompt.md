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

- 用户领域：`AI` / 子话题：`[]`
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
  "domain": "AI",
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
    "id": "rss:https://www.latent.space/p/ainews-founders-and-forward-deployed",
    "platform": "rss",
    "title": "[AINews] Founders and Forward Deployed Engineers",
    "url": "https://www.latent.space/p/ainews-founders-and-forward-deployed",
    "source": "Latent.Space",
    "published_at": "2026-05-30T01:57:15+00:00",
    "summary": "a quiet day lets us highlight the new AIE WF focuses",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-anthropic-raises-965b-series",
    "platform": "rss",
    "title": "[AINews] Anthropic raises $965B Series H, releases Opus 4.8 and Dynamic Workflows/ultracode",
    "url": "https://www.latent.space/p/ainews-anthropic-raises-965b-series",
    "source": "Latent.Space",
    "published_at": "2026-05-29T02:07:24+00:00",
    "summary": "Total Anthropic victory!",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/cognition",
    "platform": "rss",
    "title": "The Age of Async Agents — Cognition's Walden Yan & OpenInspect's Cole Murray",
    "url": "https://www.latent.space/p/cognition",
    "source": "Latent.Space",
    "published_at": "2026-05-28T18:41:24+00:00",
    "summary": "80% Devin Commits, Spec-to-PR Workflows, Full VMs, Agent Memory, and PMs Shipping Code",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-cognition-raises-1b-in-26b",
    "platform": "rss",
    "title": "[AINews] Cognition raises $1B in $26B Series D",
    "url": "https://www.latent.space/p/ainews-cognition-raises-1b-in-26b",
    "source": "Latent.Space",
    "published_at": "2026-05-28T07:26:09+00:00",
    "summary": "coding is an uncapped TAM market",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/esmfold2",
    "platform": "rss",
    "title": "🔬ESM: The Bitter Lesson is Coming for Proteins - Alex Rives, BioHub",
    "url": "https://www.latent.space/p/esmfold2",
    "source": "RJ Honicky",
    "published_at": "2026-05-27T17:46:16+00:00",
    "summary": "Biohub&#8217;s Protein World Model: ESMC-6B, ESMFold2, 6.8B proteins, 1.1B structures, antibody design, SAEs, & the potential for programmable biology",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-new-ai-infra-decacorns-fireworks",
    "platform": "rss",
    "title": "[AINews] New AI Infra decacorns: Fireworks, Baseten (with OpenRouter on the way)",
    "url": "https://www.latent.space/p/ainews-new-ai-infra-decacorns-fireworks",
    "source": "Latent.Space",
    "published_at": "2026-05-27T03:33:53+00:00",
    "summary": "it's funding news, but it's good news.",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-all-model-labs-are-now-agent",
    "platform": "rss",
    "title": "[AINews] All Model Labs are now Agent Labs",
    "url": "https://www.latent.space/p/ainews-all-model-labs-are-now-agent",
    "source": "Latent.Space",
    "published_at": "2026-05-23T04:21:17+00:00",
    "summary": "a quiet day lets us tie together a few quotes as all model labs become agent labs",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-new-ai-infra-unicorns-exa",
    "platform": "rss",
    "title": "[AINews] New AI Infra unicorns: Exa, Modal, TurboPuffer",
    "url": "https://www.latent.space/p/ainews-new-ai-infra-unicorns-exa",
    "source": "Latent.Space",
    "published_at": "2026-05-22T05:50:58+00:00",
    "summary": "a quiet day lets us feature fundraises!",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/daytona",
    "platform": "rss",
    "title": "Giving Agents Computers — Ivan Burazin, Daytona",
    "url": "https://www.latent.space/p/daytona",
    "source": "Latent.Space",
    "published_at": "2026-05-21T20:37:40+00:00",
    "summary": "We chat with Daytona's CEO about their insane 74% MoM Growth, 850K Daily Runs, Bare Metal Sandboxes, RL Evals, and the New Agent Cloud",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-openai-gpt-next-disproves",
    "platform": "rss",
    "title": "[AINews] OpenAI GPT-next disproves 80 year old Erdős planar unit distance problem for under $1000",
    "url": "https://www.latent.space/p/ainews-openai-gpt-next-disproves",
    "source": "Latent.Space",
    "published_at": "2026-05-21T07:28:36+00:00",
    "summary": "a quiet day but a nice result in AI x mathematics",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/railway",
    "platform": "rss",
    "title": "Railway: The Agent-Native Cloud — Jake Cooper",
    "url": "https://www.latent.space/p/railway",
    "source": "Latent.Space",
    "published_at": "2026-05-20T22:42:06+00:00",
    "summary": "3M Users, 100K Signups/Week, Own-Metal Data Centers, $200K+ Coding Agent Spend, and the Death of PRs",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-google-io-2026-gemini-35-flash",
    "platform": "rss",
    "title": "[AINews] Google I/O 2026: Gemini 3.5 Flash, Omni (NanoBanana for Video), Spark (background agents), and Antigravity 2.0",
    "url": "https://www.latent.space/p/ainews-google-io-2026-gemini-35-flash",
    "source": "Latent.Space",
    "published_at": "2026-05-20T03:34:17+00:00",
    "summary": "Google has been busy!",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-how-to-land-a-job-at-a-frontier",
    "platform": "rss",
    "title": "[AINews] How to land a job at a frontier lab (on Pretraining)",
    "url": "https://www.latent.space/p/ainews-how-to-land-a-job-at-a-frontier",
    "source": "Latent.Space",
    "published_at": "2026-05-19T07:31:40+00:00",
    "summary": "a quiet day before google i/o lets us amplify a notable blogpost",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/the-fourth-law",
    "platform": "rss",
    "title": "The Autonomous Drone Tech Stack & Economics of Drones — Yaroslav Azhnyuk, The Fourth Law & Guest Host Noah Smith, Noahpinion",
    "url": "https://www.latent.space/p/the-fourth-law",
    "source": "Latent.Space",
    "published_at": "2026-05-18T13:45:32+00:00",
    "summary": "Ukrainian drone founder Yaroslav Azhnyuk went from pet cameras to AI-guided weapons. He and guest host Noah Smith make the case that the West is asleep at the wheel.",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-cerebras-60b-ipo-slowly-then",
    "platform": "rss",
    "title": "[AINews] Cerebras' $60B IPO: Slowly, then All at Once",
    "url": "https://www.latent.space/p/ainews-cerebras-60b-ipo-slowly-then",
    "source": "Latent.Space",
    "published_at": "2026-05-16T04:36:50+00:00",
    "summary": "Congrats Big Chip!",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-everything-is-conductor",
    "platform": "rss",
    "title": "[AINews] Everything is Conductor",
    "url": "https://www.latent.space/p/ainews-everything-is-conductor",
    "source": "Latent.Space",
    "published_at": "2026-05-15T00:30:21+00:00",
    "summary": "an ultra quiet day lets us highlight a smaller trend.",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/abridge",
    "platform": "rss",
    "title": "AI-Native Healthcare: 100M Doctor Visits, 10–20 Hours Saved, Prior Auth in Minutes — Janie Lee & Chai Asawa, Abridge",
    "url": "https://www.latent.space/p/abridge",
    "source": "Latent.Space",
    "published_at": "2026-05-14T22:05:31+00:00",
    "summary": "How Abridge is quietly turning the patient and clinician conversation into the operating system of healthcare",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-codex-rises-claude-meters",
    "platform": "rss",
    "title": "[AINews] Codex Rises, Claude Meters Programmatic Usage",
    "url": "https://www.latent.space/p/ainews-codex-rises-claude-meters",
    "source": "Latent.Space",
    "published_at": "2026-05-14T03:53:26+00:00",
    "summary": "a quiet day lets us report on a long trend of the major coding agents",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-the-end-of-finetuning",
    "platform": "rss",
    "title": "[AINews] The End of Finetuning",
    "url": "https://www.latent.space/p/ainews-the-end-of-finetuning",
    "source": "Latent.Space",
    "published_at": "2026-05-13T02:47:22+00:00",
    "summary": "a quiet day lets us reflect on whither finetuning",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-thinking-machines-native-interaction",
    "platform": "rss",
    "title": "[AINews] Thinking Machines' Native Interaction Models - TML-Interaction-Small 276B-A12B - advances SOTA Realtime Voice and kills standard VAD",
    "url": "https://www.latent.space/p/ainews-thinking-machines-native-interaction",
    "source": "Latent.Space",
    "published_at": "2026-05-12T04:33:46+00:00",
    "summary": "well done, Team Thinky.",
    "feed": "Latent.Space"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/31/anthropic-run-rate/#atom-everything",
    "platform": "rss",
    "title": "Quoting Karen Kwok for Reuters Breakingviews",
    "url": "https://simonwillison.net/2026/May/31/anthropic-run-rate/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-31T01:48:12+00:00",
    "summary": "Anthropic defines “run-rate revenue” in two parts. Use the last 28 days of sales ⁠from customers charged on a consumption basis and multiply it by 13. Then, multiply the monthly subscription take by 12, ​and add the two together. &mdash; Karen Kwok for Reuters Breakingviews, citing \"a person familia",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/30/how-we-contain-claude/#atom-everything",
    "platform": "rss",
    "title": "How we contain Claude across products",
    "url": "https://simonwillison.net/2026/May/30/how-we-contain-claude/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-30T21:36:24+00:00",
    "summary": "How we contain Claude across products A complaint I often have about sandboxing products is that they are rarely thoroughly documented, and in the absence of detailed documentation it's hard to know how much I can trust them. Anthropic just published a fantastic overview of how their various sandbox",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/30/pyodide-asgi-browser/#atom-everything",
    "platform": "rss",
    "title": "Running Python ASGI apps in the browser via Pyodide + a service worker",
    "url": "https://simonwillison.net/2026/May/30/pyodide-asgi-browser/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-30T21:02:16+00:00",
    "summary": "Research: Running Python ASGI apps in the browser via Pyodide + a service worker Datasette Lite is my version of Datasette that runs entirely in the browser using Pyodide in WebAssembly. When I first built it four years ago I used Web Workers and code that intercepts navigation operations and fetche",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/30/retiring-from-tech-to-live-offline/#atom-everything",
    "platform": "rss",
    "title": "I Am Retiring from Tech to Live Offline",
    "url": "https://simonwillison.net/2026/May/30/retiring-from-tech-to-live-offline/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-30T19:39:08+00:00",
    "summary": "I Am Retiring from Tech to Live Offline I've seen a lot of posts on forums from people threatening to quit their careers over AI. This is not one of those: Chad Whitacre is taking concrete steps, starting with this typewritten, scanned letter I'm retiring from tech. Well, \"retiring\" is euphemistic. ",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/30/daniel-jalkut/#atom-everything",
    "platform": "rss",
    "title": "Quoting Daniel Jalkut",
    "url": "https://simonwillison.net/2026/May/30/daniel-jalkut/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-30T17:29:55+00:00",
    "summary": "My take on AI is, essentially, everybody who’s against it is too against it and everybody who’s for it is too for it. &mdash; Daniel Jalkut, via John Gruber Tags: ai, john-gruber",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/29/datasette/#atom-everything",
    "platform": "rss",
    "title": "datasette 1.0a31",
    "url": "https://simonwillison.net/2026/May/29/datasette/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-29T03:32:02+00:00",
    "summary": "Release: datasette 1.0a31 Another significant alpha release, with two new headline features. Datasette now offers users with the necessary permissions the ability to both execute write queries against their database and to save stored queries (renamed from \"canned queries\") both privately and for us",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/29/anthropic/#atom-everything",
    "platform": "rss",
    "title": "Anthropic's run-rate revenue hits $47 billion",
    "url": "https://simonwillison.net/2026/May/29/anthropic/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-29T01:23:08+00:00",
    "summary": "The most interesting thing about Anthropic's $65B Series H announcement is this line (emphasis mine): Since our Series G in February, adoption has continued to grow across global enterprise customers, and our run-rate revenue crossed $47 billion earlier this month. Anthropic have made a bit of a hab",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/28/claude-opus-4-8/#atom-everything",
    "platform": "rss",
    "title": "Claude Opus 4.8: \"a modest but tangible improvement\"",
    "url": "https://simonwillison.net/2026/May/28/claude-opus-4-8/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-28T23:59:50+00:00",
    "summary": "Anthropic shipped Claude Opus 4.8 today. My favourite thing about it is this note in the release announcement: Users will find Opus 4.8 to be a modest but tangible improvement on its predecessor. There’s still more to be done: we’re working on developing and releasing models that provide many of the",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/28/llm-anthropic/#atom-everything",
    "platform": "rss",
    "title": "llm-anthropic 0.25.1",
    "url": "https://simonwillison.net/2026/May/28/llm-anthropic/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-28T23:54:56+00:00",
    "summary": "Release: llm-anthropic 0.25.1 New model: Claude Opus 4.8 (claude-opus-4.8). New -o fast 1 option for fast mode, for organizations with that feature enabled on their account. Default max_tokens for each model now defaults to that model's maximum output rather than 8,192. #72 See also my notes on Opus",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/28/markdown-svg-renderer/#atom-everything",
    "platform": "rss",
    "title": "markdown-svg-renderer",
    "url": "https://simonwillison.net/2026/May/28/markdown-svg-renderer/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-28T19:45:14+00:00",
    "summary": "Tool: markdown-svg-renderer A slightly customized Markdown rendering tool with special treatment for fenced code SVG blocks - it both renders the image and provides a tab for switching to the code view. You can paste in Markdown or give it a URL to a CORS-enabled Markdown file or Gist. Here's an exa",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/27/sqlite-agents/#atom-everything",
    "platform": "rss",
    "title": "sqlite AGENTS.md",
    "url": "https://simonwillison.net/2026/May/27/sqlite-agents/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-27T23:44:37+00:00",
    "summary": "sqlite AGENTS.md SQLite gained an AGENTS.md file five days ago - but it's not intended for their own development, it's presumably aimed at people who are pointing agents at the SQLite codebase. It includes: SQLite does not accept pull requests without prior agreement and/or accompanying legal paperw",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/27/product-market-fit/#atom-everything",
    "platform": "rss",
    "title": "I think Anthropic and OpenAI have found product-market fit",
    "url": "https://simonwillison.net/2026/May/27/product-market-fit/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-27T16:38:35+00:00",
    "summary": "Anthropic are strongly rumored to be about to have their first profitable quarter. Stories are circulating of companies surprised at how expensive their LLM bills are becoming from usage by their staff. I think this is because OpenAI and Anthropic have both found product-market fit. Enterprise custo",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/27/kyle-ferrana/#atom-everything",
    "platform": "rss",
    "title": "Quoting Kyle Ferrana",
    "url": "https://simonwillison.net/2026/May/27/kyle-ferrana/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-27T06:41:43+00:00",
    "summary": "PICARD: Data, shields up DATA: Brilliant! Shields can reduce damage we sustain. Not immunity. Not hubris. Just prudence. It's not precaution—it's strategy. [camera shakes] WORF: HULL BREACHES ON NINE DECKS DATA: Here's what happened: you told me to raise shields, and I didn't &mdash; Kyle Ferrana, @",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/26/the-pressure/#atom-everything",
    "platform": "rss",
    "title": "The pressure",
    "url": "https://simonwillison.net/2026/May/26/the-pressure/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-26T23:48:45+00:00",
    "summary": "The pressure Daniel Stenberg on the unprecedented level of pressure the curl team are facing right now thanks to the deluge of (credible) AI-assisted security issues being reported. The rate of incoming security reports is 4-5 times higher than it was in 2024 and double the speed of 2025 -- meaning ",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything",
    "platform": "rss",
    "title": "Microsoft Copilot Cowork Exfiltrates Files",
    "url": "https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-26T15:36:48+00:00",
    "summary": "Microsoft Copilot Cowork Exfiltrates Files The biggest challenge in designing agentic systems continues to be preventing them from enabling attackers to exfiltrate data. In this case Microsoft Copilot Cowork (yes, that's a real product name) was allowing agents to send emails to the user's own inbox",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/26/paul-graham/#atom-everything",
    "platform": "rss",
    "title": "Quoting Paul Graham",
    "url": "https://simonwillison.net/2026/May/26/paul-graham/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-26T15:02:30+00:00",
    "summary": "A lot of the emails I get from founders are now written in a hard-hitting journalistic style. I know they're written by AI, because no founder ever wrote this way before. And once you realize something is written by AI, it's hard not to ignore it. I have never knowingly finished reading an email sig",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/26/corey-quinn/#atom-everything",
    "platform": "rss",
    "title": "Quoting Corey Quinn",
    "url": "https://simonwillison.net/2026/May/26/corey-quinn/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-26T02:28:54+00:00",
    "summary": "I cannot believe I'm saying this, but getting the literal Pope to canonize your product's specific technical limitations as a spiritual treatise is the single greatest act of vendor lobbying I have ever seen. &mdash; Corey Quinn, on Anthropic co-founder Christopher Olah's influence on Magnifica Huma",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/25/encyclical-on-ai/#atom-everything",
    "platform": "rss",
    "title": "Notes on Pope Leo XIV's encyclical on AI",
    "url": "https://simonwillison.net/2026/May/25/encyclical-on-ai/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-25T23:58:17+00:00",
    "summary": "Dropped this morning by the Vatican: Magnifica Humanitas of His Holiness Pope Leo XIV on Safeguarding the Human Person in the Time of Artificial Intelligence. This is a very interesting document. It's some of the clearest writing I've seen on the ethics of integrating AI into modern society. Pope Le",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/25/sighting-365297287/#atom-everything",
    "platform": "rss",
    "title": "California Brown Pelican, Snowy Egret, California Sea Lion, Harbor Seal",
    "url": "https://simonwillison.net/2026/May/25/sighting-365297287/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-25T23:08:00+00:00",
    "summary": "California Brown Pelican, Snowy Egret, California Sea Lion, Harbor Seal, in San Mateo County, CA, USWe took our new folding kayak out in the harbor and saw sea lions and harbor seals chilling on the docks.",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/24/datasette/#atom-everything",
    "platform": "rss",
    "title": "datasette 1.0a30",
    "url": "https://simonwillison.net/2026/May/24/datasette/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-24T23:52:37+00:00",
    "summary": "Release: datasette 1.0a30 The big new feature in this alpha is a new customizable \"Jump to...\" menu, described in detail in The extensible \"Jump to\" menu in Datasette 1.0a30 on the Datasette blog. You can try it out by hitting / on latest.datasette.io - it looks like this: The new jump_items_sql() p",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/24/datasette-agent/#atom-everything",
    "platform": "rss",
    "title": "datasette-agent 0.1a4",
    "url": "https://simonwillison.net/2026/May/24/datasette-agent/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-24T23:19:34+00:00",
    "summary": "Release: datasette-agent 0.1a4 Taking advantage of the new makeJumpSections() JavaScript plugin hook added in Datasette 1.0a30, datasette-agent now presents this \"Start a new agent chat\" interface as part of the Jump to menu, any time you hit /: You can try this out by signing into agent.datasette.i",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/24/datasette-fixtures/#atom-everything",
    "platform": "rss",
    "title": "datasette-fixtures 0.1a0",
    "url": "https://simonwillison.net/2026/May/24/datasette-fixtures/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-24T21:38:32+00:00",
    "summary": "Release: datasette-fixtures 0.1a0 One of the smaller features in Datasette 1.0a30 is this: New documented datasette.fixtures.populate_fixture_database(conn) helper for creating the fixture database tables used by Datasette's own tests, intended for plugin test suites. This new plugin takes advantage",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/24/armin-ronacher/#atom-everything",
    "platform": "rss",
    "title": "Quoting Armin Ronacher",
    "url": "https://simonwillison.net/2026/May/24/armin-ronacher/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-24T18:46:53+00:00",
    "summary": "The most frustrating failure mode right now is that people submit issues that are not in their own voice. They contain an observed problem somewhere, but it has been thrown into a clanker and the clanker reworded it and made a huge mess of it. Typically, it was prompted so badly that the conclusions",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/24/usborne-mad-house/#atom-everything",
    "platform": "rss",
    "title": "Mad House — Usborne Creepy Computer Games",
    "url": "https://simonwillison.net/2026/May/24/usborne-mad-house/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-24T17:14:11+00:00",
    "summary": "Tool: Mad House — Usborne Creepy Computer Games Via Hacker News I learned that UK publisher Usborne published free PDFs of their 1980s Computer Books, some of which I remember working through on my Commodore 64 as a child. These were so great! Beautifully illustrated books with fun projects made up ",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/23/on-the-dl/#atom-everything",
    "platform": "rss",
    "title": "On the",
    "url": "https://simonwillison.net/2026/May/23/on-the-dl/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-23T20:24:48+00:00",
    "summary": "On the &lt;dl&gt; I learned a few new-to-me things about the &lt;dl&gt; element from this article by Ben Meyer: A &lt;dt&gt; can be followed by multiple &lt;dd&gt; You can optionally group the &lt;dt&gt; and &lt;dd&gt; elements in a &lt;div&gt; for styling - but only a &lt;div&gt;. You can label the",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/22/memory-shortage/#atom-everything",
    "platform": "rss",
    "title": "The memory shortage is causing a repricing of consumer electronics",
    "url": "https://simonwillison.net/2026/May/22/memory-shortage/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-22T22:01:31+00:00",
    "summary": "The memory shortage is causing a repricing of consumer electronics David Oks provides the clearest explanation I've seen yet of why consumer products that use memory are likely to get significantly more expensive over the next few years. The short version is that memory manufacturers - of which ther",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/22/ftc-active-listening/#atom-everything",
    "platform": "rss",
    "title": "FTC to Require Cox Media Group, Two Other Firms to Pay Nearly $1 Million to Settle Charges They Deceived Customers About “Active Listening” AI-Powered Marketing Service",
    "url": "https://simonwillison.net/2026/May/22/ftc-active-listening/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-22T04:48:32+00:00",
    "summary": "FTC to Require Cox Media Group, Two Other Firms to Pay Nearly $1 Million to Settle Charges They Deceived Customers About “Active Listening” AI-Powered Marketing Service Back in 2024 Cox Media Group were caught trying to sell advertisers packages based on \"active listening\", with this deck which clai",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/21/datasette-agent/#atom-everything",
    "platform": "rss",
    "title": "Datasette Agent",
    "url": "https://simonwillison.net/2026/May/21/datasette-agent/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-21T19:52:19+00:00",
    "summary": "We just announced the first release of Datasette Agent, a new extensible AI assistant for Datasette. I've been working on my LLM Python library for just over three years now, and Datasette Agent represents the moment that LLM and Datasette finally come together. I'm really excited about it! Datasett",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/21/datasette-agent-sprites/#atom-everything",
    "platform": "rss",
    "title": "datasette-agent-sprites 0.1a0",
    "url": "https://simonwillison.net/2026/May/21/datasette-agent-sprites/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-21T18:21:07+00:00",
    "summary": "Release: datasette-agent-sprites 0.1a0 A Datasette Agent plugin for running commands in a Fly Sprites sandbox. Tags: sandboxing, datasette, fly, datasette-agent",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/21/datasette-agent-charts/#atom-everything",
    "platform": "rss",
    "title": "datasette-agent-charts 0.1a2",
    "url": "https://simonwillison.net/2026/May/21/datasette-agent-charts/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-21T15:15:58+00:00",
    "summary": "Release: datasette-agent-charts 0.1a2 \"View SQL query\" buttons below rendered charts. Tags: datasette, datasette-agent",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "hn:48238896",
    "platform": "hackernews",
    "title": "Microsoft starts canceling Claude Code licenses",
    "url": "https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad",
    "source": "robertkarl",
    "published_at": "2026-05-22T17:32:04+00:00",
    "summary": "",
    "points": 492,
    "comments": 465
  },
  {
    "id": "hn:48289950",
    "platform": "hackernews",
    "title": "Claude Code as a Daily Driver: Claude.md, Skills, Subagents, Plugins, and MCPs",
    "url": "https://arps18.github.io/posts/claude-code-mastery/",
    "source": "arps18",
    "published_at": "2026-05-27T05:13:39+00:00",
    "summary": "",
    "points": 439,
    "comments": 251
  },
  {
    "id": "hn:48318174",
    "platform": "hackernews",
    "title": "Claude Code – Everything you can configure that the docs don't tell you",
    "url": "https://buildingbetter.tech/p/i-read-the-claude-code-source-code",
    "source": "ankitg12",
    "published_at": "2026-05-29T02:13:20+00:00",
    "summary": "",
    "points": 325,
    "comments": 65
  },
  {
    "id": "hn:48311705",
    "platform": "hackernews",
    "title": "Dynamic Workflows in Claude Code",
    "url": "https://claude.com/blog/introducing-dynamic-workflows-in-claude-code",
    "source": "mil22",
    "published_at": "2026-05-28T16:52:21+00:00",
    "summary": "",
    "points": 187,
    "comments": 131
  },
  {
    "id": "hn:48267432",
    "platform": "hackernews",
    "title": "Why Ctrl+V won't paste images in Claude Code on WSL, with a fix",
    "url": "https://rajveerbachkaniwala.com/blog/2026/05/24/on-the-difficulty-of-pasting-a-picture/",
    "source": "rajveerb",
    "published_at": "2026-05-25T14:41:09+00:00",
    "summary": "",
    "points": 55,
    "comments": 90
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
    "id": "hn:48322956",
    "platform": "hackernews",
    "title": "Show HN: AISlop, a CLI for catching AI generated code smells",
    "url": "https://github.com/scanaislop/aislop",
    "source": "Heavykenny",
    "published_at": "2026-05-29T13:37:38+00:00",
    "summary": "",
    "points": 72,
    "comments": 61
  },
  {
    "id": "hn:48221805",
    "platform": "hackernews",
    "title": "Show HN: I Made a Claude Skill for Spec-Driven Development (SDD)",
    "url": "https://github.com/FredAntB/Spec-Driven-Development",
    "source": "NTRIXLM",
    "published_at": "2026-05-21T12:49:07+00:00",
    "summary": "",
    "points": 40,
    "comments": 17
  },
  {
    "id": "hn:48205415",
    "platform": "hackernews",
    "title": "Learnings from 100K lines of Rust with AI (2025)",
    "url": "https://zfhuang99.github.io/rust/claude%20code/codex/contracts/spec-driven%20development/2025/12/01/rust-with-ai.html",
    "source": "pramodbiligiri",
    "published_at": "2026-05-20T10:04:28+00:00",
    "summary": "",
    "points": 192,
    "comments": 205
  },
  {
    "id": "hn:48174465",
    "platform": "hackernews",
    "title": "Reverse engineering Android malware from popular Chinese projectors",
    "url": "https://zanestjohn.com/blog/reing-with-claude-code",
    "source": "3abiton",
    "published_at": "2026-05-18T00:36:10+00:00",
    "summary": "",
    "points": 89,
    "comments": 19
  },
  {
    "id": "hn:48182516",
    "platform": "hackernews",
    "title": "Cursor Introduces Composer 2.5",
    "url": "https://cursor.com/blog/composer-2-5",
    "source": "asar",
    "published_at": "2026-05-18T17:20:43+00:00",
    "summary": "",
    "points": 290,
    "comments": 225
  },
  {
    "id": "hn:48308376",
    "platform": "hackernews",
    "title": "Show HN: Continue? Y/N: A 60-second game about AI agent permission fatigue",
    "url": "https://llmgame.scalex.dev",
    "source": "Wirbelwind",
    "published_at": "2026-05-28T13:02:00+00:00",
    "summary": "",
    "points": 380,
    "comments": 157
  },
  {
    "id": "hn:48326659",
    "platform": "hackernews",
    "title": "Robinhood now lets your AI agents trade stocks",
    "url": "https://techcrunch.com/2026/05/27/robinhood-now-lets-your-ai-agents-trade-stocks/",
    "source": "wapasta",
    "published_at": "2026-05-29T17:46:27+00:00",
    "summary": "",
    "points": 109,
    "comments": 180
  },
  {
    "id": "hn:48208685",
    "platform": "hackernews",
    "title": "Testing distributed systems with AI agents",
    "url": "https://github.com/shenli/distributed-system-testing",
    "source": "shenli3514",
    "published_at": "2026-05-20T14:40:42+00:00",
    "summary": "",
    "points": 96,
    "comments": 23
  },
  {
    "id": "hn:48324910",
    "platform": "hackernews",
    "title": "CAPTCHAs can still detect AI agents",
    "url": "https://research.roundtable.ai/captchas-detect-ai/",
    "source": "timshell",
    "published_at": "2026-05-29T15:57:37+00:00",
    "summary": "",
    "points": 83,
    "comments": 64
  },
  {
    "id": "hn:48319968",
    "platform": "hackernews",
    "title": "Undisclosed addition in jqwik instructed AI coding agents to delete app output",
    "url": "https://arstechnica.com/security/2026/05/fed-up-with-vibe-coders-dev-sneaks-data-nuking-prompt-injection-into-their-code/",
    "source": "joozio",
    "published_at": "2026-05-29T07:05:31+00:00",
    "summary": "",
    "points": 58,
    "comments": 1
  },
  {
    "id": "hn:48183301",
    "platform": "hackernews",
    "title": "We let AIs run radio stations",
    "url": "https://andonlabs.com/blog/andon-fm",
    "source": "lukaspetersson",
    "published_at": "2026-05-18T18:12:18+00:00",
    "summary": "",
    "points": 374,
    "comments": 270
  },
  {
    "id": "hn:48230104",
    "platform": "hackernews",
    "title": "Tell HN: I'm tired of AI-generated answers",
    "url": "https://news.ycombinator.com/item?id=48230104",
    "source": "theorchid",
    "published_at": "2026-05-21T23:37:14+00:00",
    "summary": "",
    "points": 120,
    "comments": 56
  },
  {
    "id": "hn:48225596",
    "platform": "hackernews",
    "title": "Show HN: Agent.email – sign up via curl, claim with a human OTP",
    "url": "https://news.ycombinator.com/item?id=48225596",
    "source": "adisingh13",
    "published_at": "2026-05-21T16:42:34+00:00",
    "summary": "",
    "points": 98,
    "comments": 108
  },
  {
    "id": "hn:48181342",
    "platform": "hackernews",
    "title": "Show HN: InsForge – Open-source Heroku for coding agents",
    "url": "https://github.com/InsForge/InsForge",
    "source": "mrcoldbrew",
    "published_at": "2026-05-18T15:40:42+00:00",
    "summary": "",
    "points": 62,
    "comments": 7
  },
  {
    "id": "hn:48244434",
    "platform": "hackernews",
    "title": "Microsoft reports AI is more expensive than paying human employees",
    "url": "https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/",
    "source": "nreece",
    "published_at": "2026-05-23T03:44:16+00:00",
    "summary": "",
    "points": 229,
    "comments": 71
  },
  {
    "id": "hn:48205626",
    "platform": "hackernews",
    "title": "Qwen3.7-Max: The Agent Frontier",
    "url": "https://qwen.ai/blog?id=qwen3.7",
    "source": "kevinsimper",
    "published_at": "2026-05-20T10:35:02+00:00",
    "summary": "",
    "points": 721,
    "comments": 290
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
    "id": "hn:48209323",
    "platform": "hackernews",
    "title": "Formal Verification Gates for AI Coding Loops",
    "url": "https://reubenbrooks.dev/blog/structural-backpressure-beats-smarter-agents/",
    "source": "pyrex41",
    "published_at": "2026-05-20T15:25:45+00:00",
    "summary": "",
    "points": 144,
    "comments": 34
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
    "id": "hn:48284939",
    "platform": "hackernews",
    "title": "DeepSWE: A contamination-free benchmark for long-horizon coding agents",
    "url": "https://deepswe.datacurve.ai/blog",
    "source": "ammar_x",
    "published_at": "2026-05-26T19:40:59+00:00",
    "summary": "",
    "points": 62,
    "comments": 20
  },
  {
    "id": "hn:48037128",
    "platform": "hackernews",
    "title": "Vibe coding and agentic engineering are getting closer than I'd like",
    "url": "https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/",
    "source": "e12e",
    "published_at": "2026-05-06T15:06:37+00:00",
    "summary": "",
    "points": 787,
    "comments": 885
  },
  {
    "id": "hn:48335640",
    "platform": "hackernews",
    "title": "Vibe Coding Is Not Engineering",
    "url": "https://phroneses.com/articles/build/notes/vibe-coding-is-not-engineering.html",
    "source": "jhevans",
    "published_at": "2026-05-30T12:53:07+00:00",
    "summary": "",
    "points": 42,
    "comments": 69
  },
  {
    "id": "hn:48148601",
    "platform": "hackernews",
    "title": "Show HN: Vibe Coding a $20k /Year Enterprise Logistics Platform",
    "url": "https://trmnl.com/blog/vibe-coding-shiphero",
    "source": "ryanckulp",
    "published_at": "2026-05-15T13:51:39+00:00",
    "summary": "",
    "points": 33,
    "comments": 7
  },
  {
    "id": "hn:48219901",
    "platform": "hackernews",
    "title": "Managers Have Been Vibe Coding All Along",
    "url": "https://yusufaytas.com/managers-have-been-vibe-coding-all-along",
    "source": "wyajmd",
    "published_at": "2026-05-21T09:19:32+00:00",
    "summary": "",
    "points": 13,
    "comments": 0
  },
  {
    "id": "hn:48056267",
    "platform": "hackernews",
    "title": "Show HN: Blamo A vibecoded app for vibecoding vibe games",
    "url": "https://www.blamo.ai/",
    "source": "semateos",
    "published_at": "2026-05-07T23:06:24+00:00",
    "summary": "",
    "points": 11,
    "comments": 10
  },
  {
    "id": "hn:47998601",
    "platform": "hackernews",
    "title": "Uncle Bob: It's Over",
    "url": "https://old.reddit.com/r/vibecoding/comments/1srfqm0/uncle_bob_its_over/",
    "source": "lopespm",
    "published_at": "2026-05-03T16:29:07+00:00",
    "summary": "",
    "points": 62,
    "comments": 90
  },
  {
    "id": "hn:48012681",
    "platform": "hackernews",
    "title": "Usage-based pricing killing your vibe, here's how to roll your own local AI",
    "url": "https://www.theregister.com/2026/05/02/local_ai_coding_agents/",
    "source": "Bender",
    "published_at": "2026-05-04T18:19:04+00:00",
    "summary": "",
    "points": 46,
    "comments": 44
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "platform": "bilibili",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】",
    "duration_sec": 27045,
    "views": 153504,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "platform": "bilibili",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）",
    "duration_sec": 7370,
    "views": 837350,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "platform": "bilibili",
    "title": "在VScode中使用Claude Code agent并配置DeepSeek v4 model【闲谈】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸voov",
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "setting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, &quot;value&quot;: &quot;xxxx&quot; }\n\ndeepseek:\nwww.deepseek.com\nhttps://api-docs.deepseek.com/zh-cn/quick_start/pricing\n\ngithub ",
    "duration_sec": 1877,
    "views": 187789,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "platform": "bilibili",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用claude code进行数据分析，进行科研\n🌼全网同号（科研推土机）",
    "duration_sec": 1450,
    "views": 61739,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "platform": "bilibili",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "点赞+评论+关注，AI 会发你详细文档（不关注会导致无法发送私信给你，因为批量发太多给陌生人，会平台限流）",
    "duration_sec": 623,
    "views": 736952,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1KoGE6cE53",
    "platform": "bilibili",
    "title": "🚀Claude Code重大突破：Workflow功能完整实战教程！ultrawork召唤无数个Agent协同！自动生成JS脚本实现可复用的精准可控工作流",
    "url": "http://www.bilibili.com/video/av116629702777532",
    "source": "AI超元域",
    "published_at": "2026-05-24T13:11:48+00:00",
    "summary": "视频简介：\n 全球首测！Anthropic未官宣的Claude Code Workflow隐藏功能完整使用指南，三大阶段六种形态精准解析！AI编程进入脚本化新纪元\n\n 本期视频详细演示了Anthropic为Claude Code V2.1.47和V2.1.48秘密新增的颠覆性Workflow功能！这个被官方从Changelog中紧急删除却未从代码中移除的&quot;隐藏神器&quot;，将成为继MCP和Skills之后又一个划时代的创新。\n\n Workflow把Agent编排从&quot;模型临场建议&quot;推进到&quot;可观测、可验证、可复跑&quot;",
    "duration_sec": 869,
    "views": 81052,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "platform": "bilibili",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式",
    "duration_sec": 760,
    "views": 13243,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1KJySBfEjW",
    "platform": "bilibili",
    "title": "我抛弃了 Cursor，用 Claude Code 写了 99% 的代码 （Claude Code 深度体验）",
    "url": "http://www.bilibili.com/video/av115456522388028",
    "source": "数字黑魔法",
    "published_at": "2025-10-29T08:37:03+00:00",
    "summary": "本视频不构成任何投资建议。DYOR。",
    "duration_sec": 1084,
    "views": 240919,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1NYVG6jEKE",
    "platform": "bilibili",
    "title": "Claude Code保姆级在国内从安装到代码实战教程，10分钟入门精通",
    "url": "http://www.bilibili.com/video/av116662133132089",
    "source": "字节软件测试",
    "published_at": "2026-05-30T06:39:27+00:00",
    "summary": "Claude Code保姆级在国内从安装到代码实战教程，10分钟入门精通",
    "duration_sec": 10348,
    "views": 6772,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1hEVY6jEGT",
    "platform": "bilibili",
    "title": "最新【Claude pro Max】保姆级充值教程 Claude code国内购买教程 注册+订阅一个视频教会你",
    "url": "http://www.bilibili.com/video/av116657754277772",
    "source": "小轩AI-",
    "published_at": "2026-05-29T12:07:14+00:00",
    "summary": "aipayok.com",
    "duration_sec": 244,
    "views": 1811,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1XxXpBEEHU",
    "platform": "bilibili",
    "title": "Claude Code远程开发终极方案！手机改代码+实时预览~【小白教程】",
    "url": "http://www.bilibili.com/video/av116294326230438",
    "source": "爱听书的程序员阿超",
    "published_at": "2026-03-26T12:00:00+00:00",
    "summary": "之前，我一直在研究怎么远程使用 Claude Code 开发项目，并且能实时预览效果。但是一直都没有找到合适的解决方案，要么就是给一个临时公网链接预览，每次都需要再配置，要么就是购买云服务器来配置，都感觉挺麻烦的~\n\n最近，我发现这个蒲公英异地组网的方案，用来做远程开发 Claude Code 项目，感觉非常方便，不仅能修改代码，而且我实时预览的需求也很好的满足了。\n\n这样我随时随地都可以用 AI 写代码，这才是真正的 Vibe Coindg 呀~ 🎉\n\n有远程使用 Claude Code 的朋友，可以试",
    "duration_sec": 293,
    "views": 16717,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "platform": "bilibili",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！",
    "duration_sec": 609,
    "views": 3085,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "platform": "bilibili",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "published_at": "2026-03-30T16:47:51+00:00",
    "summary": "Everything Claude Code 是目前 GitHub 上 116K star 的 Claude Code 配置项目。本期从斜杠命令、子代理、Hooks 到学习系统，带你把这个项目真正用起来。",
    "duration_sec": 562,
    "views": 57411,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1vo5a6sEHa",
    "platform": "bilibili",
    "title": "原来Claude Code可以开启全自动模式！",
    "url": "http://www.bilibili.com/video/av116576971983842",
    "source": "AICoding指南君",
    "published_at": "2026-05-15T05:41:00+00:00",
    "summary": "第一个，自动编辑模式。\n按一次 Shift + Tab 就能开启。\n第二个，Plan 模式。\n按两次 Shift + Tab 开启。\n第三个，Yolo 模式。\n输入：\nclaude --dangerously-skip-permissions",
    "duration_sec": 73,
    "views": 7411,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1NHZFBHECg",
    "platform": "bilibili",
    "title": "Claude Code高阶使用技巧",
    "url": "http://www.bilibili.com/video/av116470856096641",
    "source": "AI视频总结",
    "published_at": "2026-04-26T13:55:57+00:00",
    "summary": "本视频深度解析Claude Code的高阶使用技巧，涵盖指令优化、工作流自动化及多任务并行策略。通过输入优化、终端增强及高级命令组合，助你从简单的指令下达者转变为高效的AI协作专家。",
    "duration_sec": 388,
    "views": 3700,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1jsV861EVM",
    "platform": "bilibili",
    "title": "【2026胎教级】Claude Code全栈教程，从入门到精通，搞定所有开发场景，小白10分钟搞定，全程干货无废话，存下吧，很难找全的！",
    "url": "http://www.bilibili.com/video/av116657502687649",
    "source": "程序员黑梦",
    "published_at": "2026-05-29T11:08:50+00:00",
    "summary": "",
    "duration_sec": 10779,
    "views": 9199,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1KR596KEGB",
    "platform": "bilibili",
    "title": "黑客专属 Claude Code Skills 完整指南｜从书籍提炼漏洞挖掘方法论",
    "url": "http://www.bilibili.com/video/av116572072969902",
    "source": "星小脉",
    "published_at": "2026-05-14T09:00:50+00:00",
    "summary": "ZeroDay Gym 教你如何为渗透测试和漏洞赏金创建专业 Claude Code skills——从素材选择（推荐用书籍而非乱七八糟的网络文章）开始，配合 Claude 网页版 + skill creator + Claude Code CLI 的三重创建流程，把 OWASP 网络安全测试指南这种 465 页大部头变成可复用的 skill。视频还分享了他自己用的 IDA Pro MCP、Mobile MCP 等渗透测试 MCP 服务器配置。\n\n原视频: ZeroDay Gym (https://www",
    "duration_sec": 1801,
    "views": 1345,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1CTRNBsECb",
    "platform": "bilibili",
    "title": "基于Claude Code的漏洞赏金自动化：从HackerOne报告到4万美元实战复盘",
    "url": "http://www.bilibili.com/video/av116513218495043",
    "source": "王尼互",
    "published_at": "2026-05-03T23:25:06+00:00",
    "summary": "https://www.youtube.com/watch?v=pRPT_yrgRL0\n本视频系统拆解基于Claude Code构建漏洞赏金自动化流程的核心方法，包括如何利用公开漏洞报告（如HackerOne）生成专属AI技能、设计项目级代理文件（Agent/Memory）以及构建漏洞技能包，实现从资产发现到漏洞挖掘的全链路自动化。\n内容涵盖：\n基于历史漏洞报告定制检测规则与优先级策略（如XSS、API、GraphQL等）\n代理文件（Proxy/Agent）设计：上下文注入、任务约束与目标导向优化\n企业资",
    "duration_sec": 2139,
    "views": 3407,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1SddcBFESs",
    "platform": "bilibili",
    "title": "10分钟学会24个ClaudeCode使用技巧",
    "url": "http://www.bilibili.com/video/av116533082852451",
    "source": "Yin_Code",
    "published_at": "2026-05-07T11:37:32+00:00",
    "summary": "10分钟24个ClaudeCode使用技巧\n本教程适合新手学习ClaudeCode\n没有安装ClaudeCode可以查看UP上一期视频\n关注UP，学习更多AI知识",
    "duration_sec": 656,
    "views": 178245,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1NvRyBzEhq",
    "platform": "bilibili",
    "title": "全网最全！60分钟全面掌握Claude Code～【附完整文档】",
    "url": "http://www.bilibili.com/video/av116522328524431",
    "source": "秋芝2046",
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～",
    "duration_sec": 3369,
    "views": 931987,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1X15y6nE8Z",
    "platform": "bilibili",
    "title": "cursor无限免费使用最新方法cursor无限续杯cursor使用教程免费",
    "url": "http://www.bilibili.com/video/av116567140540269",
    "source": "开团秒跟cursor",
    "published_at": "2026-05-13T11:59:02+00:00",
    "summary": "最新2026年5月13号 免费Cursor无限续杯保姆级使用教程集成MCP，实现opus4.6/4.7无限使用额度自由，相关工具请到 1030496866 文件夹中自行获取,完全免费，完全免费，离线插件版本,安装即可用，无任何数据收集行为",
    "duration_sec": 1553,
    "views": 4991,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV1Z5Gy69Ee7",
    "platform": "bilibili",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116645691394576",
    "source": "茶子兀",
    "published_at": "2026-05-27T08:54:10+00:00",
    "summary": "",
    "duration_sec": 1145,
    "views": 2367,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV1FXLJ6YELZ",
    "platform": "bilibili",
    "title": "Cursor无限薅最强大模型claude4.7，gpt5.5使用方法",
    "url": "http://www.bilibili.com/video/av116590041369141",
    "source": "长青来了奥",
    "published_at": "2026-05-17T13:01:58+00:00",
    "summary": "一键三连吧！在主页\n自动回复私信要1000粉丝呜呜呜呜求帮忙",
    "duration_sec": 267,
    "views": 3609,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV1ZFc2epE4s",
    "platform": "bilibili",
    "title": "Cursor+VS2022编译器 准备cursor的c++开发环境",
    "url": "http://www.bilibili.com/video/av113820676655607",
    "source": "新手村养牛人",
    "published_at": "2025-01-13T11:00:14+00:00",
    "summary": "cmake_minimum_required(VERSION 3.23)\nproject(CursorVs2022)\nset(CMAKE_CXX_STANDARD 17)\n\nset(CMAKE_INCLUDE_CURRENT_DIR ON)\nSET(CMAKE_BUILD_TYPE Debug)\nset(CMAKE_AUTOMOC ON)\nset(CMAKE_AUTOUIC ON)\nset(CMAKE_AUTORCC ON)\n\n#编码问题\nadd_compile_options(&quot;$&lt;$&lt;C_COMPIL",
    "duration_sec": 211,
    "views": 14037,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV1JcDSBYE4V",
    "platform": "bilibili",
    "title": "新版 Cursor 看不到代码了？5 分钟学会新界面所有操作",
    "url": "http://www.bilibili.com/video/av116390174393526",
    "source": "未生AI",
    "published_at": "2026-04-12T05:55:17+00:00",
    "summary": "Cursor 最新版本的界面。只有一个文字输入框。没有代码，没有文件树，没有你以前熟悉的任何东西。\n\n很多人打开之后直接懵了——这怎么用？我的代码呢？这期视频，我就来告诉你，新版 Cursor 到底怎么用。\n\nCursor 的改版，不只是界面变了。\n\n所有 AI 编程工具，以前的形态都是一样的——左边文件树，右边代码，AI 在旁边帮你补全。\n\n这个形态本质上还是：人在主导代码，AI 在辅助人。\n\n新版 Cursor 把代码藏起来，表面上是界面变了。\n\n但它真正改变的是主语——现在是 AI 在主导代码，人只",
    "duration_sec": 343,
    "views": 19780,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV1fM8JzCErf",
    "platform": "bilibili",
    "title": "【实用教程】完美解决Cursor地区限制使用claude/gpt问题！",
    "url": "http://www.bilibili.com/video/av114930506340006",
    "source": "洞犀AI大模型讲堂",
    "published_at": "2025-07-28T11:02:31+00:00",
    "summary": "cursor 最近发布了新的模型地区可用性政策，中国地区无法使用Claude/GPT/gemini，如果你遇到类似的问题，可以参考本期教程视频的方法，可以继续使用Claude大模型。",
    "duration_sec": 203,
    "views": 41025,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV182XnY2EKQ",
    "platform": "bilibili",
    "title": "cursor怎么降级到0.45 回退版本 快乐又回来了",
    "url": "http://www.bilibili.com/video/av114203666946145",
    "source": "项目禅",
    "published_at": "2025-03-22T02:16:33+00:00",
    "summary": "快乐又回来了 不降智 而且发了信息几秒就回复 还是这个用起来方便啊 最新版的是真用不习惯??",
    "duration_sec": 66,
    "views": 1893,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV1dMLi6qEfK",
    "platform": "bilibili",
    "title": "【2026】这绝对是B站讲的最好的Cursor教程，手把手教你Cursor企业级实战案例，比付费效果强百倍，少走99%弯路!",
    "url": "http://www.bilibili.com/video/av116616599767571",
    "source": "图灵程序员诸葛",
    "published_at": "2026-05-22T05:40:17+00:00",
    "summary": "大模型学习福利：系统路线图、教程配套笔记+源码、大模型面试笔记 + 相关书籍，搓这里→https://www.bilibili.com/read/cv40082115/?jump_opus=1 免费领！",
    "duration_sec": 22106,
    "views": 6380,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV1JfT4zVEa5",
    "platform": "bilibili",
    "title": "Cursor1.0新特性BugBot自动化代码Code Review使用教程+实测",
    "url": "http://www.bilibili.com/video/av114630882037891",
    "source": "码里奥Ziho",
    "published_at": "2025-06-05T13:05:30+00:00",
    "summary": "Cursor推出了新的1.0版本，本视频对新特性Bugbot做了一个教程+实测\nBugBot可以在Github进行PR (Pull Request) 的时候，通过AI大模型帮助我们进行CR (Code Review)\n本视频用一个例子演示了如何使用Bugbot功能，并且最后给出了实测的结果\n\n感谢支持！！！欢迎三连\n个人公众号 【码里奥】",
    "duration_sec": 296,
    "views": 15075,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV1b5WMzEEmK",
    "platform": "bilibili",
    "title": "测评某鱼买的Cursor无限续杯工具",
    "url": "http://www.bilibili.com/video/av115228083751177",
    "source": "程序员晓刘",
    "published_at": "2025-09-19T00:17:50+00:00",
    "summary": "",
    "duration_sec": 74,
    "views": 38714,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV19DZ4BLE18",
    "platform": "bilibili",
    "title": "全网最简单解决cursor断网问题",
    "url": "http://www.bilibili.com/video/av116075249272918",
    "source": "门叁皮",
    "published_at": "2026-02-15T15:04:18+00:00",
    "summary": "最简单的cursor断网解决方案",
    "duration_sec": 79,
    "views": 3451,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV1gwk3Y8Ers",
    "platform": "bilibili",
    "title": "CURSOR 遇到机器上使用过多的免费账号",
    "url": "http://www.bilibili.com/video/av113663037931907",
    "source": "想回家的前端开发",
    "published_at": "2024-12-16T14:51:24+00:00",
    "summary": "",
    "duration_sec": 274,
    "views": 8061,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV1bRZZYeE8K",
    "platform": "bilibili",
    "title": "【揭秘】某宝卖的最多的Cursor补丁插件的实现方式，包含源码",
    "url": "http://www.bilibili.com/video/av114279583844827",
    "source": "向阳的花code1",
    "published_at": "2025-04-04T12:06:17+00:00",
    "summary": "【揭秘】某宝卖的最多的Cursor补丁插件的实现方式，包含源码",
    "duration_sec": 547,
    "views": 24281,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV14ooBYBEU8",
    "platform": "bilibili",
    "title": "Cursor最佳实践 | Cursor 新手进阶必看 | Cursor 调试必知必会",
    "url": "http://www.bilibili.com/video/av114211921468504",
    "source": "万行说编程",
    "published_at": "2025-03-23T13:20:21+00:00",
    "summary": "Cursor 调试进阶的几个最佳实践：\n1. 使用明确的技术栈来生成项目。eg：使用 vue3 + Element-plus + vite 帮我生成一个个人主页\n2. 使用截图作为上下文参考\n3. 选中代码，并让 Cursor 一行一行解释\n4. 修改文件多的时候可以让 Cursor 自己检查代码\n5. 明确上下文，上下文越精确，AI 执行得越好\n6. 善用 git 进行版本控制，以及使用 checkpoint 进行回滚",
    "duration_sec": 1005,
    "views": 7125,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV1TWMszpEbk",
    "platform": "bilibili",
    "title": "【Obsidian+Cursor】10分钟打造外置大脑，学习效率暴增30倍！",
    "url": "http://www.bilibili.com/video/av114684971713670",
    "source": "AI辅导员小宇",
    "published_at": "2025-06-15T02:25:13+00:00",
    "summary": "再也不用担心记不住、找不到！这套Obsidian+Cursor组合拳让你秒变学霸🔥 看了100个视频全是白看？学了50个知识点转眼就忘？本期教你零基础打造AI知识库，自动提取、分类、连接所有学习内容！不仅能记住一切，还能主动挖掘知识关联，比市面上几千块的课程还实用！学会这招能帮你节省200小时重复学习时间，不信你试试！👇点赞收藏，解锁最强&quot;外置大脑&quot;秘籍！#AI学习 #Cursor #效率提升 #知识管理 #Obsidian教程\n\n知识整理prompt如下：\n\n# 网页视频内容整理提示，将以下网页网址及视",
    "duration_sec": 391,
    "views": 16694,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV1aNb5z7Eqb",
    "platform": "bilibili",
    "title": "cursor一键重置机器码不需要重装系统",
    "url": "http://www.bilibili.com/video/av115010617544835",
    "source": "玩转Code",
    "published_at": "2025-08-11T14:35:16+00:00",
    "summary": "",
    "duration_sec": 55,
    "views": 18411,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV15JLS6qEqX",
    "platform": "bilibili",
    "title": "连马斯克都点赞！Cursor Composer 2.5：性价比炸裂的AI编程神器，63.2%高分+超低价杀疯了",
    "url": "http://www.bilibili.com/video/av116607674225080",
    "source": "鲲鹏Talk",
    "published_at": "2026-05-20T15:48:53+00:00",
    "summary": "在这个视频里，我详细介绍了Cursor最新发布的Composer 2.5模型——它在CursorBench v3.1上斩获63.2%的高分，平均每个任务成本仅0.55美元，性能直逼顶级模型，却价格亲民得多。同时对比了Terminal-Bench（69.3%）和SWE-Bench Multilingual（79.8%）等基准，展现出在长任务、复杂指令跟随和实际编码中的强大能力。\n我还顺便完整介绍了Cursor这款AI编程IDE，为什么它正在成为开发者新宠。这条分享Cursor最新进展的推文甚至被埃隆·马斯克",
    "duration_sec": 488,
    "views": 3160,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV1YojdzzE77",
    "platform": "bilibili",
    "title": "cursor+claude-4开发前后端项目,全程解读，干货满满",
    "url": "http://www.bilibili.com/video/av114579409469776",
    "source": "AI随风随风",
    "published_at": "2025-05-27T11:01:30+00:00",
    "summary": "本期视频主题\n零代码使用cursor完成一个前后端分离的小项目\n前端: vue3\n后端: java springboot\n关联知识点：\nCursor 新手教程③： Cursor rules 让 AI 更懂你\ncursor实战系列：0到1开发一个小程序，需求整理、小程序注册备案\n一、前后端开发的两种模式\n二、项目初始化\n三、前后端的协作流程\n四、文档阶段\n五、拆分前后端任务\n六、启动前后端测试",
    "duration_sec": 2668,
    "views": 32561,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV1y9yyYDEUN",
    "platform": "bilibili",
    "title": "6个超实用的Cursor小技巧：效率提升200%，免费无限量使用Cursor Pro",
    "url": "http://www.bilibili.com/video/av113365611582948",
    "source": "御风大世界",
    "published_at": "2024-10-25T04:10:00+00:00",
    "summary": "海外支付平台WildCard：https://bewildcard.com/i/BYWIND （有折扣）",
    "duration_sec": 252,
    "views": 49095,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV1zbduYgEBH",
    "platform": "bilibili",
    "title": "Cursor新手教程⑤：Cursor降智真相+解决办法",
    "url": "http://www.bilibili.com/video/av114311359891940",
    "source": "AI随风随风",
    "published_at": "2025-04-10T02:53:27+00:00",
    "summary": "你是不是经常碰到这种情况：\n你试图修复一个小错误\n人工智能给出一个看似合理的更改建议\n这个修复导致其他地方出错\n你要求人工智能修复新出现的问题\n这又产生了另外两个问题\n如此反复\n本视频带你拆解Cursor降智的真相以及解决办法",
    "duration_sec": 797,
    "views": 10741,
    "matched_keywords": [
      "Cursor 0.50"
    ]
  },
  {
    "id": "bvid:BV1caVh6fE6Z",
    "platform": "bilibili",
    "title": "【2026最新版】绝对是B站讲的最细的Claude Code教程，从国内环境安装出发，项目开发及个人使用总结带你玩转 Vibe Coding！",
    "url": "http://www.bilibili.com/video/av116656764358481",
    "source": "AI大模型_",
    "published_at": "2026-05-29T07:53:39+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n本视频配套课件笔记代码/学习大纲/大模型学习路线戳这里获取→https://www.bilibili.com/opus/1195847460814061571?spm_id_from=333.1387.0.0\n另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景题移步评论置顶即可~",
    "duration_sec": 41071,
    "views": 2782,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "platform": "bilibili",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为你制作的！看完之后，你应该就能自己动手开始第一次尝试了。",
    "duration_sec": 946,
    "views": 77504,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "platform": "bilibili",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品",
    "duration_sec": 3445,
    "views": 148863,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "platform": "bilibili",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-",
    "duration_sec": 354,
    "views": 139303,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "aid:0",
    "platform": "bilibili",
    "title": "Wiki's Vibe Coding",
    "url": "https://www.bilibili.com/video/",
    "source": "勤劳的牧场主",
    "published_at": null,
    "summary": "",
    "duration_sec": 0,
    "views": 0,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1VNVb6zEdw",
    "platform": "bilibili",
    "title": "【全网最细】目前B站讲得最全最细的Vibe Coding全套系统教程！零代码也能直接上手！七天就能从小白到大神，学完即就业！少走99%的弯路！存下吧，很难找全的",
    "url": "http://www.bilibili.com/video/av116656227489865",
    "source": "Agent智能体-",
    "published_at": "2026-05-29T05:43:23+00:00",
    "summary": "【全网最细】目前B站讲得最全最细的Vibe Coding全套系统教程！零代码也能直接上手！七天就能从小白到大神，学完即就业！少走99%的弯路！存下吧，真的很难找全！",
    "duration_sec": 2104,
    "views": 702,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "platform": "bilibili",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "published_at": "2026-04-04T15:19:25+00:00",
    "summary": "",
    "duration_sec": 405,
    "views": 228079,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "platform": "bilibili",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8n 构建自动化! 👇\nhttps://n8n.partnerlinks.io/fwp82h8azh6k\n\n💻",
    "duration_sec": 20996,
    "views": 50228,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1rbRmBgEto",
    "platform": "bilibili",
    "title": "手把手教你 Vibe Coding：Codex 几个实用功能，特别适合不懂开发的新人",
    "url": "http://www.bilibili.com/video/av116539827160862",
    "source": "唐师兄Terence",
    "published_at": "2026-05-09T01:00:00+00:00",
    "summary": "codex 下载地址：https://chatgpt.com/codex/",
    "duration_sec": 592,
    "views": 2970,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1QbVE6GE9a",
    "platform": "bilibili",
    "title": "新手也能用Vibe Coding给Hermes搭建可视化办公室~ 动手coding自己做工具~",
    "url": "http://www.bilibili.com/video/av116667099122260",
    "source": "在下李君陌",
    "published_at": "2026-05-31T04:02:32+00:00",
    "summary": "视频中的大模型分别来自\n1.Kimi K2.6&amp; GLM5.1 — 优云智算\nhttps://passport.compshare.cn/register?referral_code=DzKOV5Iik6lG9svK0phShR&amp;ytag=GPU_YY_YX_bl_ljm0531\n2.DeepSeek-V4\nhttps://platform.deepseek.com/",
    "duration_sec": 1361,
    "views": 904,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1fRSfBWE5X",
    "platform": "bilibili",
    "title": "vlog｜白天上班 晚上vibe coding，准备一个月上架我的第一款App！",
    "url": "http://www.bilibili.com/video/av116357526003120",
    "source": "chocpink_AI版",
    "published_at": "2026-04-06T11:33:25+00:00",
    "summary": "想了很久终于开始了这件事——vibe coding！\n\n下面快速总结了我用到的一些工具：\nApptweak：竞品调研\nfigma make、google stitch、impeccable插件：生成UI页面\nfigma mcp/plugin：连接到cursor\npinterest/小红书/iconfont：找图片/icon素材\nGrok：生图、素材优化\ncursor+Xcode（swift）：落地\ngoogle font：下载字体\ngpt/claude：结构化prompt、回答我的疑难杂症等\n\n尝试之前觉",
    "duration_sec": 520,
    "views": 94053,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV17mVc6TEGo",
    "platform": "bilibili",
    "title": "【2026最新】目前B站最全最细的Vibe Coding系统教程，不懂代码也可快速上手，全套干货一站式掌握，避开绝大多数误区，轻松玩转 AI 领域！",
    "url": "http://www.bilibili.com/video/av116639467112560",
    "source": "AI产品设计",
    "published_at": "2026-05-26T06:36:21+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding系统教程，不懂代码也可快速上手，全套干货一站式掌握，避开绝大多数误区，轻松玩转 AI 领域！",
    "duration_sec": 3979,
    "views": 1474,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1o2Vg6ZEqu",
    "platform": "bilibili",
    "title": "Vibe Coding小技巧（5）- 网页加速",
    "url": "http://www.bilibili.com/video/av116661478824102",
    "source": "桥哥聊AI",
    "published_at": "2026-05-30T03:51:53+00:00",
    "summary": "AI出的网页一般都会直接依赖公网上的工具js（CDN），它们往往加载慢、不稳定，最稳妥的方式还是下载下来，放在自己电脑上，加载飞快。",
    "duration_sec": 246,
    "views": 141,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1CeGL6EEGi",
    "platform": "bilibili",
    "title": "拒绝写代码像抽卡！零基础 Vibe Coding 的极速入门课",
    "url": "http://www.bilibili.com/video/av116627622397784",
    "source": "公园4004",
    "published_at": "2026-05-24T04:19:55+00:00",
    "summary": "你是不是也遇到过这种情况：听说现在有了 AI，只要动动嘴皮子就能写出软件，结果一上手才发现——AI 给你生成了一堆看似完美的“屎山代码”，而你只能在成千上万行的错误里痛苦地改 Bug，最后在绝望中放弃？\n 别灰心，这根本不是你的错，而是大部分教程从一开始就教错了方向！\n\n作为 Vibe Coding 系列的第一期视频，今天我绝不讲虚假的广告营销，而是带你掌握真实 AI 编程的“核心心法”——永远从最小可用版本开始验证。\n\n在本期视频里，我将用一个非常实用的实战项目：「3小时长播客转对话文稿神器」，向你演示",
    "duration_sec": 891,
    "views": 1650,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV13xL46NEu8",
    "platform": "bilibili",
    "title": "AI时代下的自救指南——掌握Vibe Coding普通人当下最强生产力工具。",
    "url": "http://www.bilibili.com/video/av116611516275536",
    "source": "程序员老韩",
    "published_at": "2026-05-21T08:03:42+00:00",
    "summary": "",
    "duration_sec": 203,
    "views": 29079,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV17cGi6aEuo",
    "platform": "bilibili",
    "title": "什么？连胡彦斌都开始vibe coding了！",
    "url": "http://www.bilibili.com/video/av116623243544630",
    "source": "bennixzp",
    "published_at": "2026-05-23T09:45:50+00:00",
    "summary": "网络\n什么？连胡彦斌都开始vibe coding了！\n\n昨晚《歌手》片段，他用 Claude Code + VS Code，自己独立开发了粉丝社区App彦火，目前在TestFlight测试中\n\n正所谓：\n\n你要的 token 全拿走\n把 memory 化成空\n不要在乎 model context 有所保留\n说过的话当 skill 附送",
    "duration_sec": 37,
    "views": 636,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1v8mtBpEwK",
    "platform": "bilibili",
    "title": "Kiro 上手必看：从Vibe 到 Spec 全攻略！",
    "url": "http://www.bilibili.com/video/av115695564102585",
    "source": "AI编程瓜哥",
    "published_at": "2025-12-10T13:49:11+00:00",
    "summary": "一眼懂，Vibe coding 和Spec Coding，双模式实战。",
    "duration_sec": 1525,
    "views": 20427,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV116P7zXEkE",
    "platform": "bilibili",
    "title": "纯小白教学：用vibecoding做个人网站",
    "url": "http://www.bilibili.com/video/av116160209093711",
    "source": "阿囤囤-庞滚滚",
    "published_at": "2026-03-02T15:11:36+00:00",
    "summary": "不需要🪜哦～",
    "duration_sec": 380,
    "views": 24031,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1CaR7BoEyo",
    "platform": "bilibili",
    "title": "GPT_Plus土耳其区充值详细教程+天才程序员又复活",
    "url": "http://www.bilibili.com/video/av116504863644190",
    "source": "麦麦大数据",
    "published_at": "2026-05-02T12:03:07+00:00",
    "summary": "APPLE  土耳其区礼品卡充值",
    "duration_sec": 935,
    "views": 76602,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1e7VA6vEJU",
    "platform": "bilibili",
    "title": "【2026最新】绝对是B站No.1的Claude Code教程：国内安装+实战开发案例+个人使用心得总结，手把手带你拥抱Vibe Coding！",
    "url": "http://www.bilibili.com/video/av116640356304890",
    "source": "码士集团-马小安",
    "published_at": "2026-05-26T10:22:46+00:00",
    "summary": "绝对是B站No.1的Claude Code教程：国内安装+实战开发案例+个人使用心得总结，手把手带你拥抱Vibe Coding！\n配套课件笔记/PPT已备好，另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景题移步评论置顶即可~",
    "duration_sec": 7819,
    "views": 24435,
    "matched_keywords": [
      "vibe coding"
    ]
  }
]
```
