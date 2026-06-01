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

- 用户领域：`AI` / 子话题：`[
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
    "id": "rss:https://simonwillison.net/2026/Jun/1/may-newsletter/#atom-everything",
    "platform": "rss",
    "title": "May 2026 newsletter",
    "url": "https://simonwillison.net/2026/Jun/1/may-newsletter/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-06-01T04:45:00+00:00",
    "summary": "I just sent out the May edition of my sponsors-only monthly newsletter. If you are a sponsor (or if you start a sponsorship now) you can access it here. This month: Al got expensive, and Anthropic had a really good month The model releases were a little disappointing Conferences and podcasts I launc",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/31/datasette/#atom-everything",
    "platform": "rss",
    "title": "datasette 1.0a32",
    "url": "https://simonwillison.net/2026/May/31/datasette/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-31T23:23:38+00:00",
    "summary": "Release: datasette 1.0a32 A minor bugfix release. Fixes a bug with INSERT ... RETURNING queries via the new /db/-/execute-write endpoint and a bunch of base_url issues which showed up when I was experimenting with Service Workers yesterday. Tags: datasette, annotated-release-notes",
    "feed": "Simon Willison's Weblog"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/31/the-solution-might-be-cancelling-my-ai-subscription/#atom-everything",
    "platform": "rss",
    "title": "The solution might be cancelling my AI subscription",
    "url": "https://simonwillison.net/2026/May/31/the-solution-might-be-cancelling-my-ai-subscription/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-31T16:31:32+00:00",
    "summary": "The solution might be cancelling my AI subscription I find this post by David Wilson very relatable. David lists 16+ projects he's spun up with AI tooling, and concludes: I didn't mean to build most of these things. Usually the Claude session started with something like \"write a quick script for X\",",
    "feed": "Simon Willison's Weblog"
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
    "id": "rss:https://simonwillison.net/2026/May/22/monty-investigation/#atom-everything",
    "platform": "rss",
    "title": "pydantic-monty investigation",
    "url": "https://simonwillison.net/2026/May/22/monty-investigation/#atom-everything",
    "source": "Simon Willison's Weblog",
    "published_at": "2026-05-22T22:41:00+00:00",
    "summary": "Research: pydantic-monty investigation It's been a few months since I last poked at Monty, the sandboxed subset of Python implemented in Rust. I had Claude Code look at the most recent release. Importantly the max_duration_secs, max_memory, max_allocations, and max_recursion_depth settings all appea",
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
    "id": "rss:https://openai.com/index/boston-childrens-hospital",
    "platform": "rss",
    "title": "Boston Children’s uses AI to unlock new diagnoses",
    "url": "https://openai.com/index/boston-childrens-hospital",
    "source": "OpenAI News",
    "published_at": "2026-05-29T12:00:00+00:00",
    "summary": "Boston Children’s Hospital uses OpenAI technology to improve patient care, reduce operational burden, and help diagnose more than 40 rare disease cases.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/braintrust",
    "platform": "rss",
    "title": "How Braintrust turns customer requests into code with Codex",
    "url": "https://openai.com/index/braintrust",
    "source": "OpenAI News",
    "published_at": "2026-05-29T12:00:00+00:00",
    "summary": "How Braintrust engineers use Codex with GPT-5.5 to run experiments and code faster.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense",
    "platform": "rss",
    "title": "Strengthening societal resilience with Rosalind Biodefense",
    "url": "https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense",
    "source": "OpenAI News",
    "published_at": "2026-05-29T03:00:00+00:00",
    "summary": "OpenAI launches Rosalind Biodefense, expanding trusted access to GPT-Rosalind for vetted developers and U.S. government partners advancing biodefense, public health, and pandemic preparedness through frontier AI.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/trustworthy-third-party-evaluations-foundations",
    "platform": "rss",
    "title": "A shared playbook for trustworthy third party evaluations",
    "url": "https://openai.com/index/trustworthy-third-party-evaluations-foundations",
    "source": "OpenAI News",
    "published_at": "2026-05-29T00:00:00+00:00",
    "summary": "OpenAI shares guidance on third-party AI evaluations, covering how to assess model capabilities, safeguards, and validity for frontier systems.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/endava",
    "platform": "rss",
    "title": "How Endava builds an agentic organization with Codex",
    "url": "https://openai.com/index/endava",
    "source": "OpenAI News",
    "published_at": "2026-05-28T12:00:00+00:00",
    "summary": "Learn how Endava uses Codex to build an agentic organization, accelerating software delivery and reducing requirements analysis from weeks to hours.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/openai-frontier-governance-framework",
    "platform": "rss",
    "title": "OpenAI’s Frontier Governance Framework",
    "url": "https://openai.com/index/openai-frontier-governance-framework",
    "source": "OpenAI News",
    "published_at": "2026-05-28T00:00:00+00:00",
    "summary": "Explore OpenAI’s Frontier Governance Framework and how our AI safety, security, and risk practices align with emerging EU and California regulations.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/mufg",
    "platform": "rss",
    "title": "MUFG aims to become AI-native with OpenAI",
    "url": "https://openai.com/index/mufg",
    "source": "OpenAI News",
    "published_at": "2026-05-28T00:00:00+00:00",
    "summary": "MUFG uses ChatGPT Enterprise to build an AI-native organization, improve workflows, and deliver new AI-powered financial services at scale.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/cisco",
    "platform": "rss",
    "title": "Cisco and OpenAI redefine enterprise engineering with Codex",
    "url": "https://openai.com/index/cisco",
    "source": "OpenAI News",
    "published_at": "2026-05-27T11:00:00+00:00",
    "summary": "Cisco and OpenAI are redefining enterprise engineering with Codex, helping Cisco scale AI-native development, accelerate AI Defense work, and automate defect remediation.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/building-self-improving-tax-agents-with-codex",
    "platform": "rss",
    "title": "Building self-improving tax agents with Codex",
    "url": "https://openai.com/index/building-self-improving-tax-agents-with-codex",
    "source": "OpenAI News",
    "published_at": "2026-05-27T07:00:00+00:00",
    "summary": "See how OpenAI, Thrive, and Crete built a self-improving tax agent with Codex, automating filings, improving accuracy, and accelerating workflows.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/warp",
    "platform": "rss",
    "title": "Warp’s big bet on building open source with GPT-5.5",
    "url": "https://openai.com/index/warp",
    "source": "OpenAI News",
    "published_at": "2026-05-27T00:00:00+00:00",
    "summary": "Warp uses GPT-5.5 and OpenAI models to coordinate coding agents across local, cloud, and open-source development workflows.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/election-safeguards-2026",
    "platform": "rss",
    "title": "Election information and safeguards in 2026",
    "url": "https://openai.com/index/election-safeguards-2026",
    "source": "OpenAI News",
    "published_at": "2026-05-27T00:00:00+00:00",
    "summary": "Ahead of global elections, we’re helping people access information, supporting cyber defenders, and increasing AI transparency",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/grupo-folha-grupo-uol-partnership",
    "platform": "rss",
    "title": "OpenAI, Grupo Folha and Grupo UOL announce strategic content partnership",
    "url": "https://openai.com/index/grupo-folha-grupo-uol-partnership",
    "source": "OpenAI News",
    "published_at": "2026-05-25T00:00:00+00:00",
    "summary": "OpenAI partners with Grupo Folha and Grupo UOL to bring trusted Brazilian journalism to ChatGPT, expanding access to news with attribution and transparency.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/virgin-atlantic",
    "platform": "rss",
    "title": "How Virgin Atlantic ships faster with Codex",
    "url": "https://openai.com/index/virgin-atlantic",
    "source": "OpenAI News",
    "published_at": "2026-05-22T00:00:00+00:00",
    "summary": "How Virgin Atlantic used Codex to ship its revamped mobile app on a fixed holiday travel deadline, reaching near-total unit test coverage and zero P1 defects.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/gartner-2026-agentic-coding-leader",
    "platform": "rss",
    "title": "OpenAI named a Leader in enterprise coding agents by Gartner",
    "url": "https://openai.com/index/gartner-2026-agentic-coding-leader",
    "source": "OpenAI News",
    "published_at": "2026-05-22T00:00:00+00:00",
    "summary": "OpenAI is named a leader in the 2026 Gartner Magic Quadrant for Enterprise AI Coding Agents, with Codex recognized for innovation and enterprise-scale deployment.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/adventhealth",
    "platform": "rss",
    "title": "AdventHealth advances whole-person care with OpenAI",
    "url": "https://openai.com/index/adventhealth",
    "source": "OpenAI News",
    "published_at": "2026-05-21T12:00:00+00:00",
    "summary": "AdventHealth is using ChatGPT for Healthcare to streamline workflows, reduce administrative burden, and return more time to patient care.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/model-disproves-discrete-geometry-conjecture",
    "platform": "rss",
    "title": "An OpenAI model has disproved a central conjecture in discrete geometry",
    "url": "https://openai.com/index/model-disproves-discrete-geometry-conjecture",
    "source": "OpenAI News",
    "published_at": "2026-05-20T00:00:00+00:00",
    "summary": "An OpenAI model solved the 80-year-old unit distance problem, disproving a major conjecture in discrete geometry and marking a milestone in AI-driven mathematics.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/ramp",
    "platform": "rss",
    "title": "How Ramp engineers accelerate code review with Codex",
    "url": "https://openai.com/index/ramp",
    "source": "OpenAI News",
    "published_at": "2026-05-20T00:00:00+00:00",
    "summary": "How Ramp engineers use Codex with GPT-5.5 to review code and ship improvements, allowing them to get substantive feedback in minutes instead of hours.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/the-next-phase-of-education-for-countries",
    "platform": "rss",
    "title": "The next phase of OpenAI’s Education for Countries",
    "url": "https://openai.com/index/the-next-phase-of-education-for-countries",
    "source": "OpenAI News",
    "published_at": "2026-05-20T00:00:00+00:00",
    "summary": "OpenAI advances Education for Countries, expanding AI adoption in schools with new partnerships, teacher training, and tools to improve global learning outcomes.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/introducing-openai-for-singapore",
    "platform": "rss",
    "title": "Introducing OpenAI for Singapore",
    "url": "https://openai.com/index/introducing-openai-for-singapore",
    "source": "OpenAI News",
    "published_at": "2026-05-19T20:30:00+00:00",
    "summary": "OpenAI for Singapore launches a multi-year AI partnership to expand deployment, build local talent, and support businesses and public services with AI.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/advancing-content-provenance",
    "platform": "rss",
    "title": "Advancing content provenance for a safer, more transparent AI ecosystem",
    "url": "https://openai.com/index/advancing-content-provenance",
    "source": "OpenAI News",
    "published_at": "2026-05-19T10:45:00+00:00",
    "summary": "OpenAI advances AI content provenance with Content Credentials, SynthID, and a verification tool to help people identify and trust AI-generated media.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/dell-codex-enterprise-partnership",
    "platform": "rss",
    "title": "OpenAI and Dell partner to bring Codex to hybrid and on-premise enterprise environments",
    "url": "https://openai.com/index/dell-codex-enterprise-partnership",
    "source": "OpenAI News",
    "published_at": "2026-05-18T10:00:00+00:00",
    "summary": "OpenAI and Dell partner to bring Codex to hybrid and on-premise environments, helping enterprises deploy AI coding agents securely across data and workflows.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/malta-chatgpt-plus-partnership",
    "platform": "rss",
    "title": "OpenAI and Malta partner to bring ChatGPT Plus to all citizens",
    "url": "https://openai.com/index/malta-chatgpt-plus-partnership",
    "source": "OpenAI News",
    "published_at": "2026-05-16T00:00:00+00:00",
    "summary": "OpenAI and Malta partner to expand AI access, offering ChatGPT Plus and training to help citizens build practical AI skills and use AI responsibly.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/databricks",
    "platform": "rss",
    "title": "Databricks brings GPT-5.5 to enterprise agent workflows",
    "url": "https://openai.com/index/databricks",
    "source": "OpenAI News",
    "published_at": "2026-05-15T00:00:00+00:00",
    "summary": "Databricks uses GPT-5.5 for enterprise agent workflows after the model set a new state of the art on the OfficeQA Pro benchmark.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/academy/codex-for-work/how-sales-teams-use-codex",
    "platform": "rss",
    "title": "How sales teams use Codex",
    "url": "https://openai.com/academy/codex-for-work/how-sales-teams-use-codex",
    "source": "OpenAI News",
    "published_at": "2026-05-15T00:00:00+00:00",
    "summary": "See how sales teams can use Codex to create pipeline briefs, meeting prep packets, forecast reviews, account plans, and stalled-deal diagnoses from real work inputs.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/academy/codex-for-work/how-data-science-teams-use-codex",
    "platform": "rss",
    "title": "How data science teams use Codex",
    "url": "https://openai.com/academy/codex-for-work/how-data-science-teams-use-codex",
    "source": "OpenAI News",
    "published_at": "2026-05-15T00:00:00+00:00",
    "summary": "See how data science teams can use Codex to build root-cause briefs, impact readouts, KPI memos, scoped analyses, and dashboard specs from real work inputs.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/personal-finance-chatgpt",
    "platform": "rss",
    "title": "A new personal finance experience in ChatGPT",
    "url": "https://openai.com/index/personal-finance-chatgpt",
    "source": "OpenAI News",
    "published_at": "2026-05-15T00:00:00+00:00",
    "summary": "Preview a new personal finance experience in ChatGPT for Pro users in the U.S. Securely connect your financial accounts and get AI-powered insights and guidance grounded in your financial context, goals, and priorities.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/academy/codex-for-work/how-business-operations-teams-use-codex",
    "platform": "rss",
    "title": "How business operations teams use Codex",
    "url": "https://openai.com/academy/codex-for-work/how-business-operations-teams-use-codex",
    "source": "OpenAI News",
    "published_at": "2026-05-15T00:00:00+00:00",
    "summary": "See how business operations teams can use Codex to create initiative briefs, strategy updates, leadership decision packets, progress updates, and more from real work inputs.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/sea-david-chen",
    "platform": "rss",
    "title": "Sea's View on the Future of Agentic Software Development with Codex",
    "url": "https://openai.com/index/sea-david-chen",
    "source": "OpenAI News",
    "published_at": "2026-05-14T20:30:00+00:00",
    "summary": "Sea Limited's CPO explains why the company is deploying Codex across engineering teams to accelerate AI-native software development in Asia.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/work-with-codex-from-anywhere",
    "platform": "rss",
    "title": "Work with Codex from anywhere",
    "url": "https://openai.com/index/work-with-codex-from-anywhere",
    "source": "OpenAI News",
    "published_at": "2026-05-14T13:00:00+00:00",
    "summary": "Use Codex anywhere with the ChatGPT mobile app. Monitor, steer, and approve coding tasks in real time across devices and remote environments.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://openai.com/index/chatgpt-recognize-context-in-sensitive-conversations",
    "platform": "rss",
    "title": "Helping ChatGPT better recognize context in sensitive conversations",
    "url": "https://openai.com/index/chatgpt-recognize-context-in-sensitive-conversations",
    "source": "OpenAI News",
    "published_at": "2026-05-14T00:00:00+00:00",
    "summary": "Learn how new ChatGPT safety updates improve context awareness in sensitive conversations, helping detect risk over time and respond more safely.",
    "feed": "OpenAI News"
  },
  {
    "id": "rss:https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai",
    "platform": "rss",
    "title": "Welcome NVIDIA Cosmos 3: The First Open Omni-model for Physical AI Reasoning and Action",
    "url": "https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai",
    "source": "Hugging Face - Blog",
    "published_at": "2026-06-01T04:44:55+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/torch-profiler",
    "platform": "rss",
    "title": "Profiling in PyTorch (Part 1): A Beginner's Guide to torch.profiler",
    "url": "https://huggingface.co/blog/torch-profiler",
    "source": "Hugging Face - Blog",
    "published_at": "2026-05-29T00:00:00+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/ibm-research/itbench-aa",
    "platform": "rss",
    "title": "ITBench-AA: Frontier Models Score Below 50% on the First Benchmark for Agentic Enterprise IT Tasks — by Artificial Analysis and IBM",
    "url": "https://huggingface.co/blog/ibm-research/itbench-aa",
    "source": "Hugging Face - Blog",
    "published_at": "2026-05-27T17:20:29+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/local-reachy-mini-conversation",
    "platform": "rss",
    "title": "Reachy Mini goes fully local",
    "url": "https://huggingface.co/blog/local-reachy-mini-conversation",
    "source": "Hugging Face - Blog",
    "published_at": "2026-05-27T00:00:00+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/delta-weight-sync",
    "platform": "rss",
    "title": "Shipping a Trillion Parameters With a Hub Bucket: Delta Weight Sync in TRL",
    "url": "https://huggingface.co/blog/delta-weight-sync",
    "source": "Hugging Face - Blog",
    "published_at": "2026-05-27T00:00:00+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/agent-glossary",
    "platform": "rss",
    "title": "Harness, Scaffold, and the AI Agent Terms Worth Getting Right",
    "url": "https://huggingface.co/blog/agent-glossary",
    "source": "Hugging Face - Blog",
    "published_at": "2026-05-25T00:00:00+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/Dharma-AI/specialization-beats-scale",
    "platform": "rss",
    "title": "Specialization Beats Scale: A Strategic Variable Most AI Procurement Decisions Overlook",
    "url": "https://huggingface.co/blog/Dharma-AI/specialization-beats-scale",
    "source": "Hugging Face - Blog",
    "published_at": "2026-05-22T15:25:59+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/allenai/olmoearth-v1-1",
    "platform": "rss",
    "title": "OlmoEarth v1.1: A more efficient family of Earth observation models",
    "url": "https://huggingface.co/blog/allenai/olmoearth-v1-1",
    "source": "Hugging Face - Blog",
    "published_at": "2026-05-19T18:38:09+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/ettin-reranker",
    "platform": "rss",
    "title": "Introducing the Ettin Reranker Family",
    "url": "https://huggingface.co/blog/ettin-reranker",
    "source": "Hugging Face - Blog",
    "published_at": "2026-05-19T00:00:00+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/PaddlePaddle/paddleocr-transformers",
    "platform": "rss",
    "title": "PaddleOCR 3.5: Running OCR and Document Parsing Tasks with a Transformers Backend",
    "url": "https://huggingface.co/blog/PaddlePaddle/paddleocr-transformers",
    "source": "Hugging Face - Blog",
    "published_at": "2026-05-18T15:12:46+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/ibm-granite/granite-embedding-multilingual-r2",
    "platform": "rss",
    "title": "Granite Embedding Multilingual R2: Open Apache 2.0 Multilingual Embeddings with 32K Context — Best Sub-100M Retrieval Quality",
    "url": "https://huggingface.co/blog/ibm-granite/granite-embedding-multilingual-r2",
    "source": "Hugging Face - Blog",
    "published_at": "2026-05-14T18:55:01+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/continuous_async",
    "platform": "rss",
    "title": "Unlocking asynchronicity in continuous batching",
    "url": "https://huggingface.co/blog/continuous_async",
    "source": "Hugging Face - Blog",
    "published_at": "2026-05-14T00:00:00+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/amazon/foundation-model-building-blocks",
    "platform": "rss",
    "title": "Building Blocks for Foundation Model Training and Inference on AWS",
    "url": "https://huggingface.co/blog/amazon/foundation-model-building-blocks",
    "source": "Hugging Face - Blog",
    "published_at": "2026-05-11T23:18:26+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/ServiceNow-AI/correctness-before-corrections",
    "platform": "rss",
    "title": "vLLM V0 to V1: Correctness Before Corrections in RL",
    "url": "https://huggingface.co/blog/ServiceNow-AI/correctness-before-corrections",
    "source": "Hugging Face - Blog",
    "published_at": "2026-05-06T19:06:55+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/open-asr-leaderboard-private-data",
    "platform": "rss",
    "title": "Adding Benchmaxxer Repellant to the Open ASR Leaderboard",
    "url": "https://huggingface.co/blog/open-asr-leaderboard-private-data",
    "source": "Hugging Face - Blog",
    "published_at": "2026-05-06T00:00:00+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/ibm-granite/granite-4-1",
    "platform": "rss",
    "title": "Granite 4.1 LLMs: How They’re Built",
    "url": "https://huggingface.co/blog/ibm-granite/granite-4-1",
    "source": "Hugging Face - Blog",
    "published_at": "2026-04-29T15:01:48+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/inference-providers-deepinfra",
    "platform": "rss",
    "title": "DeepInfra on Hugging Face Inference Providers 🔥",
    "url": "https://huggingface.co/blog/inference-providers-deepinfra",
    "source": "Hugging Face - Blog",
    "published_at": "2026-04-29T00:00:00+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence",
    "platform": "rss",
    "title": "Introducing NVIDIA Nemotron 3 Nano Omni: Long-Context Multimodal Intelligence for Documents, Audio and Video Agents",
    "url": "https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence",
    "source": "Hugging Face - Blog",
    "published_at": "2026-04-28T15:58:57+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/openai-privacy-filter-web-apps",
    "platform": "rss",
    "title": "How to build scalable web apps with OpenAI's Privacy Filter",
    "url": "https://huggingface.co/blog/openai-privacy-filter-web-apps",
    "source": "Hugging Face - Blog",
    "published_at": "2026-04-27T00:00:00+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/deepseekv4",
    "platform": "rss",
    "title": "DeepSeek-V4: a million-token context that agents can actually use",
    "url": "https://huggingface.co/blog/deepseekv4",
    "source": "Hugging Face - Blog",
    "published_at": "2026-04-24T00:00:00+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/transformersjs-chrome-extension",
    "platform": "rss",
    "title": "How to Use Transformers.js in a Chrome Extension",
    "url": "https://huggingface.co/blog/transformersjs-chrome-extension",
    "source": "Hugging Face - Blog",
    "published_at": "2026-04-23T00:00:00+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/tiiuae/qimma-arabic-leaderboard",
    "platform": "rss",
    "title": "QIMMA قِمّة ⛰: A Quality-First Arabic LLM Leaderboard",
    "url": "https://huggingface.co/blog/tiiuae/qimma-arabic-leaderboard",
    "source": "Hugging Face - Blog",
    "published_at": "2026-04-21T10:09:58+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/cybersecurity-openness",
    "platform": "rss",
    "title": "AI and the Future of Cybersecurity: Why Openness Matters",
    "url": "https://huggingface.co/blog/cybersecurity-openness",
    "source": "Hugging Face - Blog",
    "published_at": "2026-04-21T00:00:00+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/ecom-rlve",
    "platform": "rss",
    "title": "Ecom-RLVE: Adaptive Verifiable Environments for E-Commerce Conversational Agents",
    "url": "https://huggingface.co/blog/ecom-rlve",
    "source": "Hugging Face - Blog",
    "published_at": "2026-04-16T00:00:00+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/transformers-to-mlx",
    "platform": "rss",
    "title": "The PR you would have opened yourself",
    "url": "https://huggingface.co/blog/transformers-to-mlx",
    "source": "Hugging Face - Blog",
    "published_at": "2026-04-16T00:00:00+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/train-multimodal-sentence-transformers",
    "platform": "rss",
    "title": "Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers",
    "url": "https://huggingface.co/blog/train-multimodal-sentence-transformers",
    "source": "Hugging Face - Blog",
    "published_at": "2026-04-16T00:00:00+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/ibm-research/vakra-benchmark-analysis",
    "platform": "rss",
    "title": "Inside VAKRA: Reasoning, Tool Use, and Failure Modes of Agents",
    "url": "https://huggingface.co/blog/ibm-research/vakra-benchmark-analysis",
    "source": "Hugging Face - Blog",
    "published_at": "2026-04-15T12:07:25+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/Hcompany/holotab",
    "platform": "rss",
    "title": "Meet HoloTab by HCompany. Your AI browser companion.",
    "url": "https://huggingface.co/blog/Hcompany/holotab",
    "source": "Hugging Face - Blog",
    "published_at": "2026-04-15T09:25:20+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/waypoint-1-5",
    "platform": "rss",
    "title": "Waypoint-1.5: Higher-Fidelity Interactive Worlds for Everyday GPUs",
    "url": "https://huggingface.co/blog/waypoint-1-5",
    "source": "Hugging Face - Blog",
    "published_at": "2026-04-09T00:00:00+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://huggingface.co/blog/multimodal-sentence-transformers",
    "platform": "rss",
    "title": "Multimodal Embedding & Reranker Models with Sentence Transformers",
    "url": "https://huggingface.co/blog/multimodal-sentence-transformers",
    "source": "Hugging Face - Blog",
    "published_at": "2026-04-09T00:00:00+00:00",
    "summary": "",
    "feed": "Hugging Face - Blog"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures",
    "platform": "rss",
    "title": "Recent Developments in LLM Architectures: KV Sharing, mHC, and Compressed Attention",
    "url": "https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2026-05-16T11:33:51+00:00",
    "summary": "From Gemma 4 to DeepSeek V4, How New Open-Weight LLMs Are Reducing Long-Context Costs",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/workflow-for-understanding-llms",
    "platform": "rss",
    "title": "My Workflow for Understanding LLM Architectures",
    "url": "https://magazine.sebastianraschka.com/p/workflow-for-understanding-llms",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2026-04-18T11:24:36+00:00",
    "summary": "A learning-oriented workflow for understanding new open-weight model releases",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/components-of-a-coding-agent",
    "platform": "rss",
    "title": "Components of A Coding Agent",
    "url": "https://magazine.sebastianraschka.com/p/components-of-a-coding-agent",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2026-04-04T11:45:37+00:00",
    "summary": "How coding agents use tools, memory, and repo context to make LLMs work better in practice",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/visual-attention-variants",
    "platform": "rss",
    "title": "A Visual Guide to Attention Variants in Modern LLMs",
    "url": "https://magazine.sebastianraschka.com/p/visual-attention-variants",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2026-03-22T11:55:40+00:00",
    "summary": "From MHA and GQA to MLA, sparse attention, and hybrid architectures",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/a-dream-of-spring-for-open-weight",
    "platform": "rss",
    "title": "A Dream of Spring for Open-Weight LLMs: 10 Architectures from Jan-Feb 2026",
    "url": "https://magazine.sebastianraschka.com/p/a-dream-of-spring-for-open-weight",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2026-02-25T13:26:56+00:00",
    "summary": "A Round Up And Comparison of 10 Open-Weight LLM Releases in Spring 2026",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling",
    "platform": "rss",
    "title": "Categories of Inference-Time Scaling for Improved LLM Reasoning",
    "url": "https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2026-01-24T11:23:18+00:00",
    "summary": "And an Overview of Recent Inference-Scaling Papers",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/state-of-llms-2025",
    "platform": "rss",
    "title": "The State Of LLMs 2025: Progress, Problems, and Predictions",
    "url": "https://magazine.sebastianraschka.com/p/state-of-llms-2025",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2025-12-30T12:22:26+00:00",
    "summary": "A 2025 review of large language models, from DeepSeek R1 and RLVR to inference-time scaling, benchmarks, architectures, and predictions for 2026.",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2",
    "platform": "rss",
    "title": "LLM Research Papers: The 2025 List (July to December)",
    "url": "https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2025-12-30T12:15:39+00:00",
    "summary": "In June, I shared a bonus article with my curated and bookmarked research paper lists to the paid subscribers who make this Substack possible.",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/technical-deepseek",
    "platform": "rss",
    "title": "From DeepSeek V3 to V3.2: Architecture, Sparse Attention, and RL Updates",
    "url": "https://magazine.sebastianraschka.com/p/technical-deepseek",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2025-12-03T12:03:33+00:00",
    "summary": "Understanding How DeepSeek's Flagship Open-Weight Models Evolved",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/beyond-standard-llms",
    "platform": "rss",
    "title": "Beyond Standard LLMs",
    "url": "https://magazine.sebastianraschka.com/p/beyond-standard-llms",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2025-11-04T13:06:07+00:00",
    "summary": "Linear Attention Hybrids, Text Diffusion, Code World Models, and Small Recursive Transformers",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches",
    "platform": "rss",
    "title": "Understanding the 4 Main Approaches to LLM Evaluation (From Scratch)",
    "url": "https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2025-10-05T11:12:32+00:00",
    "summary": "Multiple-Choice Benchmarks, Verifiers, Leaderboards, and LLM Judges with Code Examples",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/qwen3-from-scratch",
    "platform": "rss",
    "title": "Understanding and Implementing Qwen3 From Scratch",
    "url": "https://magazine.sebastianraschka.com/p/qwen3-from-scratch",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2025-09-06T11:10:21+00:00",
    "summary": "A Detailed Look at One of the Leading Open-Source LLMs",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/from-gpt-2-to-gpt-oss-analyzing-the",
    "platform": "rss",
    "title": "From GPT-2 to gpt-oss: Analyzing the Architectural Advances",
    "url": "https://magazine.sebastianraschka.com/p/from-gpt-2-to-gpt-oss-analyzing-the",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2025-08-09T11:23:07+00:00",
    "summary": "And How They Stack Up Against Qwen3",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison",
    "platform": "rss",
    "title": "The Big LLM Architecture Comparison",
    "url": "https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2025-07-19T11:11:10+00:00",
    "summary": "From DeepSeek-V3 to Kimi K2: A Look At Modern LLM Architecture Design",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/llm-research-papers-2025-list-one",
    "platform": "rss",
    "title": "LLM Research Papers: The 2025 List (January to June)",
    "url": "https://magazine.sebastianraschka.com/p/llm-research-papers-2025-list-one",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2025-07-01T11:11:45+00:00",
    "summary": "A topic-organized collection of 200+ LLM research papers from 2025",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms",
    "platform": "rss",
    "title": "Understanding and Coding the KV Cache in LLMs from Scratch",
    "url": "https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2025-06-17T10:55:34+00:00",
    "summary": "KV caches are one of the most critical techniques for efficient inference in LLMs in production.",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/coding-llms-from-the-ground-up",
    "platform": "rss",
    "title": "Coding LLMs from the Ground Up: A Complete Course",
    "url": "https://magazine.sebastianraschka.com/p/coding-llms-from-the-ground-up",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2025-05-10T11:03:17+00:00",
    "summary": "Why build LLMs from scratch? It's probably the best and most efficient way to learn how LLMs really work. Plus, many readers have told me they had a lot of fun doing it.",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training",
    "platform": "rss",
    "title": "The State of Reinforcement Learning for LLM Reasoning",
    "url": "https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2025-04-19T11:02:44+00:00",
    "summary": "Understanding GRPO and New Insights from Reasoning Model Papers",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/first-look-at-reasoning-from-scratch",
    "platform": "rss",
    "title": "First Look at Reasoning From Scratch: Chapter 1",
    "url": "https://magazine.sebastianraschka.com/p/first-look-at-reasoning-from-scratch",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2025-03-29T11:11:41+00:00",
    "summary": "Welcome to the next stage of large language models (LLMs): reasoning. LLMs have transformed how we process and generate text, but their success has been largely driven by statistical pattern recognition. However, new advances in reasoning methodologies now enable LLMs to tackle more complex tasks, s",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling",
    "platform": "rss",
    "title": "The State of LLM Reasoning Model Inference",
    "url": "https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling",
    "source": "Sebastian Raschka, PhD",
    "published_at": "2025-03-08T12:11:42+00:00",
    "summary": "Inference-Time Compute Scaling Methods to Improve Reasoning Models",
    "feed": "Ahead of AI"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2025-05-01-thinking/",
    "platform": "rss",
    "title": "Why We Think",
    "url": "https://lilianweng.github.io/posts/2025-05-01-thinking/",
    "source": "Lil'Log",
    "published_at": "2025-05-01T00:00:00+00:00",
    "summary": "Special thanks to John Schulman for a lot of super valuable feedback and direct edits on this post. Test time compute (Graves et al. 2016, Ling, et al. 2017, Cobbe et al. 2021) and Chain-of-thought (CoT) (Wei et al. 2022, Nye et al. 2021), have led to significant improvements in model performance, w",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2024-11-28-reward-hacking/",
    "platform": "rss",
    "title": "Reward Hacking in Reinforcement Learning",
    "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/",
    "source": "Lil'Log",
    "published_at": "2024-11-28T00:00:00+00:00",
    "summary": "Reward hacking occurs when a reinforcement learning (RL) agent exploits flaws or ambiguities in the reward function to achieve high rewards, without genuinely learning or completing the intended task. Reward hacking exists because RL environments are often imperfect, and it is fundamentally challeng",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2024-07-07-hallucination/",
    "platform": "rss",
    "title": "Extrinsic Hallucinations in LLMs",
    "url": "https://lilianweng.github.io/posts/2024-07-07-hallucination/",
    "source": "Lil'Log",
    "published_at": "2024-07-07T00:00:00+00:00",
    "summary": "Hallucination in large language models usually refers to the model generating unfaithful, fabricated, inconsistent, or nonsensical content. As a term, hallucination has been somewhat generalized to cases when the model makes mistakes. Here, I would like to narrow down the problem of hallucination to",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2024-04-12-diffusion-video/",
    "platform": "rss",
    "title": "Diffusion Models for Video Generation",
    "url": "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/",
    "source": "Lil'Log",
    "published_at": "2024-04-12T00:00:00+00:00",
    "summary": "Diffusion models have demonstrated strong results on image synthesis in past years. Now the research community has started working on a harder task&mdash;using it for video generation. The task itself is a superset of the image case, since an image is a video of 1 frame, and it is much more challeng",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2024-02-05-human-data-quality/",
    "platform": "rss",
    "title": "Thinking about High-Quality Human Data",
    "url": "https://lilianweng.github.io/posts/2024-02-05-human-data-quality/",
    "source": "Lil'Log",
    "published_at": "2024-02-05T00:00:00+00:00",
    "summary": "[Special thank you to Ian Kivlichan for many useful pointers (E.g. the 100+ year old Nature paper &ldquo;Vox populi&rdquo;) and nice feedback. 🙏 ] High-quality data is the fuel for modern data deep learning model training. Most of the task-specific labeled data comes from human annotation, such as c",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
    "platform": "rss",
    "title": "Adversarial Attacks on LLMs",
    "url": "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
    "source": "Lil'Log",
    "published_at": "2023-10-25T00:00:00+00:00",
    "summary": "The use of large language models in the real world has strongly accelerated by the launch of ChatGPT. We (including my team at OpenAI, shoutout to them) have invested a lot of effort to build default safe behavior into the model during the alignment process (e.g. via RLHF). However, adversarial atta",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2023-06-23-agent/",
    "platform": "rss",
    "title": "LLM Powered Autonomous Agents",
    "url": "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "source": "Lil'Log",
    "published_at": "2023-06-23T00:00:00+00:00",
    "summary": "Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it c",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "platform": "rss",
    "title": "Prompt Engineering",
    "url": "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "source": "Lil'Log",
    "published_at": "2023-03-15T00:00:00+00:00",
    "summary": "Prompt Engineering, also known as In-Context Prompting, refers to methods for how to communicate with LLM to steer its behavior for desired outcomes without updating the model weights. It is an empirical science and the effect of prompt engineering methods can vary a lot among models, thus requiring",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/",
    "platform": "rss",
    "title": "The Transformer Family Version 2.0",
    "url": "https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/",
    "source": "Lil'Log",
    "published_at": "2023-01-27T00:00:00+00:00",
    "summary": "Many new Transformer architecture improvements have been proposed since my last post on &ldquo;The Transformer Family&rdquo; about three years ago. Here I did a big refactoring and enrichment of that 2020 post &mdash; restructure the hierarchy of sections and improve many sections with more recent p",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2023-01-10-inference-optimization/",
    "platform": "rss",
    "title": "Large Transformer Model Inference Optimization",
    "url": "https://lilianweng.github.io/posts/2023-01-10-inference-optimization/",
    "source": "Lil'Log",
    "published_at": "2023-01-10T17:00:00+00:00",
    "summary": "[Updated on 2023-01-24: add a small section on Distillation.] Large transformer models are mainstream nowadays, creating SoTA results for a variety of tasks. They are powerful but very expensive to train and use. The extremely high inference cost, in both time and memory, is a big bottleneck for ado",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2022-09-08-ntk/",
    "platform": "rss",
    "title": "Some Math behind Neural Tangent Kernel",
    "url": "https://lilianweng.github.io/posts/2022-09-08-ntk/",
    "source": "Lil'Log",
    "published_at": "2022-09-08T17:00:00+00:00",
    "summary": "Neural networks are well known to be over-parameterized and can often easily fit data with near-zero training loss with decent generalization performance on test dataset. Although all these parameters are initialized at random, the optimization process can consistently lead to similarly good outcome",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2022-06-09-vlm/",
    "platform": "rss",
    "title": "Generalized Visual Language Models",
    "url": "https://lilianweng.github.io/posts/2022-06-09-vlm/",
    "source": "Lil'Log",
    "published_at": "2022-06-09T22:10:30+00:00",
    "summary": "Processing images to generate text, such as image captioning and visual question-answering, has been studied for years. Traditionally such systems rely on an object detection network as a vision encoder to capture visual features and then produce text via a text decoder. Given a large amount of exis",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2022-04-15-data-gen/",
    "platform": "rss",
    "title": "Learning with not Enough Data Part 3: Data Generation",
    "url": "https://lilianweng.github.io/posts/2022-04-15-data-gen/",
    "source": "Lil'Log",
    "published_at": "2022-04-15T22:10:30+00:00",
    "summary": "Here comes the Part 3 on learning with not enough data (Previous: Part 1 and Part 2). Let’s consider two approaches for generating synthetic data for training. Augmented data. Given a set of existing training samples, we can apply a variety of augmentation, distortion and transformation to derive ne",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2022-02-20-active-learning/",
    "platform": "rss",
    "title": "Learning with not Enough Data Part 2: Active Learning",
    "url": "https://lilianweng.github.io/posts/2022-02-20-active-learning/",
    "source": "Lil'Log",
    "published_at": "2022-02-20T00:00:00+00:00",
    "summary": "This is part 2 of what to do when facing a limited amount of labeled data for supervised learning tasks. This time we will get some amount of human labeling work involved, but within a budget limit, and therefore we need to be smart when selecting which samples to label.",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2021-12-05-semi-supervised/",
    "platform": "rss",
    "title": "Learning with not Enough Data Part 1: Semi-Supervised Learning",
    "url": "https://lilianweng.github.io/posts/2021-12-05-semi-supervised/",
    "source": "Lil'Log",
    "published_at": "2021-12-05T00:00:00+00:00",
    "summary": "When facing a limited amount of labeled data for supervised learning tasks, four approaches are commonly discussed.",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2021-09-25-train-large/",
    "platform": "rss",
    "title": "How to Train Really Large Models on Many GPUs?",
    "url": "https://lilianweng.github.io/posts/2021-09-25-train-large/",
    "source": "Lil'Log",
    "published_at": "2021-09-24T00:00:00+00:00",
    "summary": "[Updated on 2022-03-13: add expert choice routing.] [Updated on 2022-06-10]: Greg and I wrote a shorted and upgraded version of this post, published on OpenAI Blog: &ldquo;Techniques for Training Large Neural Networks&rdquo;",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2021-07-11-diffusion-models/",
    "platform": "rss",
    "title": "What are Diffusion Models?",
    "url": "https://lilianweng.github.io/posts/2021-07-11-diffusion-models/",
    "source": "Lil'Log",
    "published_at": "2021-07-11T00:00:00+00:00",
    "summary": "[Updated on 2021-09-19: Highly recommend this blog post on score-based generative modeling by Yang Song (author of several key papers in the references)]. [Updated on 2022-08-27: Added classifier-free guidance, GLIDE, unCLIP and Imagen. [Updated on 2022-08-31: Added latent diffusion model. [Updated ",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2021-05-31-contrastive/",
    "platform": "rss",
    "title": "Contrastive Representation Learning",
    "url": "https://lilianweng.github.io/posts/2021-05-31-contrastive/",
    "source": "Lil'Log",
    "published_at": "2021-05-31T00:00:00+00:00",
    "summary": "The goal of contrastive representation learning is to learn such an embedding space in which similar sample pairs stay close to each other while dissimilar ones are far apart. Contrastive learning can be applied to both supervised and unsupervised settings. When working with unsupervised data, contr",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2021-03-21-lm-toxicity/",
    "platform": "rss",
    "title": "Reducing Toxicity in Language Models",
    "url": "https://lilianweng.github.io/posts/2021-03-21-lm-toxicity/",
    "source": "Lil'Log",
    "published_at": "2021-03-21T00:00:00+00:00",
    "summary": "Large pretrained language models are trained over a sizable collection of online data. They unavoidably acquire certain toxic behavior and biases from the Internet. Pretrained language models are very powerful and have shown great success in many NLP tasks. However, to safely deploy them for practic",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2021-01-02-controllable-text-generation/",
    "platform": "rss",
    "title": "Controllable Neural Text Generation",
    "url": "https://lilianweng.github.io/posts/2021-01-02-controllable-text-generation/",
    "source": "Lil'Log",
    "published_at": "2021-01-02T00:00:00+00:00",
    "summary": "[Updated on 2021-02-01: Updated to version 2.0 with several work added and many typos fixed.] [Updated on 2021-05-26: Add P-tuning and Prompt Tuning in the &ldquo;prompt design&rdquo; section.] [Updated on 2021-09-19: Add &ldquo;unlikelihood training&rdquo;.]",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2020-10-29-odqa/",
    "platform": "rss",
    "title": "How to Build an Open-Domain Question Answering System?",
    "url": "https://lilianweng.github.io/posts/2020-10-29-odqa/",
    "source": "Lil'Log",
    "published_at": "2020-10-29T00:00:00+00:00",
    "summary": "[Updated on 2020-11-12: add an example on closed-book factual QA using OpenAI API (beta). A model that can answer any question with regard to factual knowledge can lead to many useful and practical applications, such as working as a chatbot or an AI assistant🤖. In this post, we will review several c",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2020-08-06-nas/",
    "platform": "rss",
    "title": "Neural Architecture Search",
    "url": "https://lilianweng.github.io/posts/2020-08-06-nas/",
    "source": "Lil'Log",
    "published_at": "2020-08-06T00:00:00+00:00",
    "summary": "Although most popular and successful model architectures are designed by human experts, it doesn&rsquo;t mean we have explored the entire network architecture space and settled down with the best option. We would have a better chance to find the optimal solution if we adopt a systematic and automati",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2020-06-07-exploration-drl/",
    "platform": "rss",
    "title": "Exploration Strategies in Deep Reinforcement Learning",
    "url": "https://lilianweng.github.io/posts/2020-06-07-exploration-drl/",
    "source": "Lil'Log",
    "published_at": "2020-06-07T00:00:00+00:00",
    "summary": "[Updated on 2020-06-17: Add &ldquo;exploration via disagreement&rdquo; in the &ldquo;Forward Dynamics&rdquo; section. Exploitation versus exploration is a critical topic in Reinforcement Learning. We&rsquo;d like the RL agent to find the best solution as fast as possible. However, in the meantime, c",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2020-04-07-the-transformer-family/",
    "platform": "rss",
    "title": "The Transformer Family",
    "url": "https://lilianweng.github.io/posts/2020-04-07-the-transformer-family/",
    "source": "Lil'Log",
    "published_at": "2020-04-07T00:00:00+00:00",
    "summary": "[Updated on 2023-01-27: After almost three years, I did a big refactoring update of this post to incorporate a bunch of new Transformer models since 2020. The enhanced version of this post is here: The Transformer Family Version 2.0. Please refer to that post on this topic.]",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2020-01-29-curriculum-rl/",
    "platform": "rss",
    "title": "Curriculum for Reinforcement Learning",
    "url": "https://lilianweng.github.io/posts/2020-01-29-curriculum-rl/",
    "source": "Lil'Log",
    "published_at": "2020-01-29T00:00:00+00:00",
    "summary": "[Updated on 2020-02-03: mentioning PCG in the &ldquo;Task-Specific Curriculum&rdquo; section. [Updated on 2020-02-04: Add a new &ldquo;curriculum through distillation&rdquo; section.",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2019-11-10-self-supervised/",
    "platform": "rss",
    "title": "Self-Supervised Representation Learning",
    "url": "https://lilianweng.github.io/posts/2019-11-10-self-supervised/",
    "source": "Lil'Log",
    "published_at": "2019-11-10T00:00:00+00:00",
    "summary": "[Updated on 2020-01-09: add a new section on Contrastive Predictive Coding]. [Updated on 2020-04-13: add a &ldquo;Momentum Contrast&rdquo; section on MoCo, SimCLR and CURL.] [Updated on 2020-07-08: add a &ldquo;Bisimulation&rdquo; section on DeepMDP and DBC.] [Updated on 2020-09-12: add MoCo V2 and ",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2019-09-05-evolution-strategies/",
    "platform": "rss",
    "title": "Evolution Strategies",
    "url": "https://lilianweng.github.io/posts/2019-09-05-evolution-strategies/",
    "source": "Lil'Log",
    "published_at": "2019-09-05T00:00:00+00:00",
    "summary": "Stochastic gradient descent is a universal choice for optimizing deep learning models. However, it is not the only option. With black-box optimization algorithms, you can evaluate a target function $f(x): \\mathbb{R}^n \\to \\mathbb{R}$, even when you don&rsquo;t know the precise analytic form of $f(x)",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2019-06-23-meta-rl/",
    "platform": "rss",
    "title": "Meta Reinforcement Learning",
    "url": "https://lilianweng.github.io/posts/2019-06-23-meta-rl/",
    "source": "Lil'Log",
    "published_at": "2019-06-23T00:00:00+00:00",
    "summary": "In my earlier post on meta-learning, the problem is mainly defined in the context of few-shot classification. Here I would like to explore more into cases when we try to &ldquo;meta-learn&rdquo; Reinforcement Learning (RL) tasks by developing an agent that can solve unseen tasks fast and efficiently",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2019-05-05-domain-randomization/",
    "platform": "rss",
    "title": "Domain Randomization for Sim2Real Transfer",
    "url": "https://lilianweng.github.io/posts/2019-05-05-domain-randomization/",
    "source": "Lil'Log",
    "published_at": "2019-05-05T00:00:00+00:00",
    "summary": "In Robotics, one of the hardest problems is how to make your model transfer to the real world. Due to the sample inefficiency of deep RL algorithms and the cost of data collection on real robots, we often need to train models in a simulator which theoretically provides an infinite amount of data. Ho",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://lilianweng.github.io/posts/2019-03-14-overfit/",
    "platform": "rss",
    "title": "Are Deep Neural Networks Dramatically Overfitted?",
    "url": "https://lilianweng.github.io/posts/2019-03-14-overfit/",
    "source": "Lil'Log",
    "published_at": "2019-03-14T00:00:00+00:00",
    "summary": "[Updated on 2019-05-27: add the section on Lottery Ticket Hypothesis.] If you are like me, entering into the field of deep learning with experience in traditional machine learning, you may often ponder over this question: Since a typical deep neural network has so many parameters and training error ",
    "feed": "Lil'Log"
  },
  {
    "id": "rss:https://karpathy.bearblog.dev/sequoia-ascent-2026/",
    "platform": "rss",
    "title": "Sequoia Ascent 2026 summary",
    "url": "https://karpathy.bearblog.dev/sequoia-ascent-2026/",
    "source": "karpathy (hidden)",
    "published_at": "2026-04-30T16:00:00+00:00",
    "summary": "Summary of my talk at Sequoia Ascent",
    "feed": "karpathy"
  },
  {
    "id": "rss:https://karpathy.bearblog.dev/year-in-review-2025/",
    "platform": "rss",
    "title": "2025 LLM Year in Review",
    "url": "https://karpathy.bearblog.dev/year-in-review-2025/",
    "source": "karpathy (hidden)",
    "published_at": "2025-12-19T18:00:00+00:00",
    "summary": "2025 Year in Review of LLM paradigm changes",
    "feed": "karpathy"
  },
  {
    "id": "rss:https://karpathy.bearblog.dev/chemical-hygiene/",
    "platform": "rss",
    "title": "Chemical hygiene",
    "url": "https://karpathy.bearblog.dev/chemical-hygiene/",
    "source": "karpathy (hidden)",
    "published_at": "2025-12-18T18:00:00+00:00",
    "summary": "An evolving guide of protecting your health from a pricemaxxing industry.",
    "feed": "karpathy"
  },
  {
    "id": "rss:https://karpathy.bearblog.dev/auto-grade-hn/",
    "platform": "rss",
    "title": "Auto-grading decade-old Hacker News discussions with hindsight",
    "url": "https://karpathy.bearblog.dev/auto-grade-hn/",
    "source": "karpathy (hidden)",
    "published_at": "2025-12-10T15:00:00+00:00",
    "summary": "A vibe coding thought exercise on what it might look like for LLMs to scour human historical data at scale and in retrospect.",
    "feed": "karpathy"
  },
  {
    "id": "rss:https://karpathy.bearblog.dev/the-space-of-minds/",
    "platform": "rss",
    "title": "The space of minds",
    "url": "https://karpathy.bearblog.dev/the-space-of-minds/",
    "source": "karpathy (hidden)",
    "published_at": "2025-11-29T18:00:00+00:00",
    "summary": "On the space of minds and the optimizations that give rise to them.",
    "feed": "karpathy"
  },
  {
    "id": "rss:https://karpathy.bearblog.dev/verifiability/",
    "platform": "rss",
    "title": "Verifiability",
    "url": "https://karpathy.bearblog.dev/verifiability/",
    "source": "karpathy (hidden)",
    "published_at": "2025-11-17T17:00:00+00:00",
    "summary": "The impact of verifiability on the jagged frontier of LLMs",
    "feed": "karpathy"
  },
  {
    "id": "rss:https://karpathy.bearblog.dev/animals-vs-ghosts/",
    "platform": "rss",
    "title": "Animals vs Ghosts",
    "url": "https://karpathy.bearblog.dev/animals-vs-ghosts/",
    "source": "karpathy (hidden)",
    "published_at": "2025-10-01T17:00:00+00:00",
    "summary": "Today's frontier LLM research is not about building animals. It is about summoning ghosts. And a bit more on Sutton's Dwarkesh pod.",
    "feed": "karpathy"
  },
  {
    "id": "rss:https://karpathy.bearblog.dev/vibe-coding-menugen/",
    "platform": "rss",
    "title": "Vibe coding MenuGen",
    "url": "https://karpathy.bearblog.dev/vibe-coding-menugen/",
    "source": "karpathy (hidden)",
    "published_at": "2025-04-27T12:00:00+00:00",
    "summary": "Work log of vibe coding menugen app",
    "feed": "karpathy"
  },
  {
    "id": "rss:https://karpathy.bearblog.dev/power-to-the-people/",
    "platform": "rss",
    "title": "Power to the people: How LLMs flip the script on technology diffusion",
    "url": "https://karpathy.bearblog.dev/power-to-the-people/",
    "source": "karpathy (hidden)",
    "published_at": "2025-04-07T18:00:00+00:00",
    "summary": "Yes",
    "feed": "karpathy"
  },
  {
    "id": "rss:https://karpathy.bearblog.dev/finding-the-best-sleep-tracker/",
    "platform": "rss",
    "title": "Finding the Best Sleep Tracker",
    "url": "https://karpathy.bearblog.dev/finding-the-best-sleep-tracker/",
    "source": "karpathy (hidden)",
    "published_at": "2025-03-24T23:00:00+00:00",
    "summary": "Finding the best sleep tracker with data",
    "feed": "karpathy"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-doordash-built-a-testing-system",
    "platform": "rss",
    "title": "How DoorDash Built a Testing System to Evaluate LLMs",
    "url": "https://blog.bytebytego.com/p/how-doordash-built-a-testing-system",
    "source": "ByteByteGo",
    "published_at": "2026-05-30T15:30:52+00:00",
    "summary": "In this article, we will learn how they built this flywheel and the key takeaways.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/must-know-failure-modes-in-distributed",
    "platform": "rss",
    "title": "Must-Know Failure Modes in Distributed Systems",
    "url": "https://blog.bytebytego.com/p/must-know-failure-modes-in-distributed",
    "source": "ByteByteGo",
    "published_at": "2026-05-28T16:31:00+00:00",
    "summary": "In this article, we will look at the most significant failure mode patterns in distributed systems and the standard approaches to deal with each of them.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-airtable-built-the-search-layer",
    "platform": "rss",
    "title": "How Airtable Built the Search Layer Behind Their AI Features",
    "url": "https://blog.bytebytego.com/p/how-airtable-built-the-search-layer",
    "source": "ByteByteGo",
    "published_at": "2026-05-27T15:30:43+00:00",
    "summary": "In this article, we will look at how Airtable&#8217;s data infrastructure team built its architecture, the challenges they faced, the tradeoffs they accepted, and why the choices they made only make sense once their data is properly understood.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-vercel-cut-build-wait-times-from",
    "platform": "rss",
    "title": "How Vercel Cut Build Wait Times From 90 Seconds To 5",
    "url": "https://blog.bytebytego.com/p/how-vercel-cut-build-wait-times-from",
    "source": "ByteByteGo",
    "published_at": "2026-05-26T15:31:10+00:00",
    "summary": "In this article, we examine the constraints Vercel faced, the choices they made in response, and the optimizations that produced the speedup.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-cockroachdb-built-vector-indexing",
    "platform": "rss",
    "title": "How CockroachDB Built Vector Indexing at Scale",
    "url": "https://blog.bytebytego.com/p/how-cockroachdb-built-vector-indexing",
    "source": "ByteByteGo",
    "published_at": "2026-05-25T15:30:38+00:00",
    "summary": "In this article, we will look at how the CockroachDB engineering team built this index and the challenges they faced.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/ep216-rags-vs-agents",
    "platform": "rss",
    "title": "EP216: RAGs vs Agents",
    "url": "https://blog.bytebytego.com/p/ep216-rags-vs-agents",
    "source": "ByteByteGo",
    "published_at": "2026-05-23T15:31:18+00:00",
    "summary": "Ask an LLM about your company's data and it will guess. The two patterns that fix this are RAG and agents, and they solve different problems.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/build-with-claude-code-new-cohort",
    "platform": "rss",
    "title": "Build with Claude Code: New Cohort Launch",
    "url": "https://blog.bytebytego.com/p/build-with-claude-code-new-cohort",
    "source": "ByteByteGo",
    "published_at": "2026-05-22T15:31:20+00:00",
    "summary": "The first cohort starts in about a week: May 28-29, 2026.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/a-guide-to-async-patterns-in-api",
    "platform": "rss",
    "title": "A Guide to Async Patterns in API Design",
    "url": "https://blog.bytebytego.com/p/a-guide-to-async-patterns-in-api",
    "source": "ByteByteGo",
    "published_at": "2026-05-21T15:30:24+00:00",
    "summary": "In this article, we will look at each of these patterns in detail, along with their advantages.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-netflix-is-using-multimodal-ai",
    "platform": "rss",
    "title": "How Netflix is Using Multimodal AI to Power Video Search",
    "url": "https://blog.bytebytego.com/p/how-netflix-is-using-multimodal-ai",
    "source": "ByteByteGo",
    "published_at": "2026-05-20T15:31:07+00:00",
    "summary": "In this article, we will understand how Netflix built this system and the challenges it faced.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-snapchat-serves-a-billion-predictions",
    "platform": "rss",
    "title": "How Snapchat Serves a Billion Predictions Per Second",
    "url": "https://blog.bytebytego.com/p/how-snapchat-serves-a-billion-predictions",
    "source": "ByteByteGo",
    "published_at": "2026-05-19T15:31:28+00:00",
    "summary": "For Snap, machine learning is closer to the product itself than a feature on top of it.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-grab-is-using-ai-agents-to-boost",
    "platform": "rss",
    "title": "How Grab is Using AI Agents to Boost Team Productivity",
    "url": "https://blog.bytebytego.com/p/how-grab-is-using-ai-agents-to-boost",
    "source": "ByteByteGo",
    "published_at": "2026-05-18T15:31:16+00:00",
    "summary": "Grab&#8217;s data engineering team had a problem that looks familiar to anyone who&#8217;s maintained shared infrastructure.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/ep215-the-anatomy-of-an-ai-agent",
    "platform": "rss",
    "title": "EP215: The Anatomy of an AI Agent",
    "url": "https://blog.bytebytego.com/p/ep215-the-anatomy-of-an-ai-agent",
    "source": "ByteByteGo",
    "published_at": "2026-05-16T15:31:01+00:00",
    "summary": "An AI agent can be thought of as a simple While-loop.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/last-call-for-enrollment-become-an-a88",
    "platform": "rss",
    "title": "LAST CALL FOR ENROLLMENT: Become an AI Engineer - Cohort 6",
    "url": "https://blog.bytebytego.com/p/last-call-for-enrollment-become-an-a88",
    "source": "ByteByteGo",
    "published_at": "2026-05-15T15:02:20+00:00",
    "summary": "Our 6th cohort of Becoming an AI Engineer starts tomorrow, Saturday, May 16. This is a live, cohort-based course created in collaboration with best-selling author Ali Aminian and published by ByteByteGo.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/a-guide-to-event-driven-architectural",
    "platform": "rss",
    "title": "A Guide To Event-Driven Architectural Patterns",
    "url": "https://blog.bytebytego.com/p/a-guide-to-event-driven-architectural",
    "source": "ByteByteGo",
    "published_at": "2026-05-14T15:32:28+00:00",
    "summary": "Distributed systems are built out of services that need to communicate, and the simplest way to do that is for one service to call another directly and wait for a response.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/high-performance-rate-limiting-at",
    "platform": "rss",
    "title": "High Performance Rate Limiting at Databricks",
    "url": "https://blog.bytebytego.com/p/high-performance-rate-limiting-at",
    "source": "ByteByteGo",
    "published_at": "2026-05-13T15:30:35+00:00",
    "summary": "In this article, we look at how Databricks implemented rate limiting at scale, how they shrank the critical path, and the accuracy tradeoff that shrinking usually requires.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-figma-upgraded-data-pipeline",
    "platform": "rss",
    "title": "How Figma Upgraded Data Pipeline from Multi-Day Latency to Real-Time",
    "url": "https://blog.bytebytego.com/p/how-figma-upgraded-data-pipeline",
    "source": "ByteByteGo",
    "published_at": "2026-05-12T15:31:03+00:00",
    "summary": "In this article, we will learn what happened as Figma grew and how its engineering team handled the growth in terms of the data pipeline issues.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-pinterest-built-a-production",
    "platform": "rss",
    "title": "How Pinterest Built a Production MCP Ecosystem",
    "url": "https://blog.bytebytego.com/p/how-pinterest-built-a-production",
    "source": "ByteByteGo",
    "published_at": "2026-05-11T15:31:17+00:00",
    "summary": "In this article, we look at how Pinterest designed that ecosystem and what they had to get right beyond the protocol itself.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/ep214-claude-code-vs-openclaw-5-design",
    "platform": "rss",
    "title": "EP214: Claude Code vs. OpenClaw: 5 Design Dimensions",
    "url": "https://blog.bytebytego.com/p/ep214-claude-code-vs-openclaw-5-design",
    "source": "ByteByteGo",
    "published_at": "2026-05-09T15:31:10+00:00",
    "summary": "Both are highly capable, but they have key architectural differences.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/enrollment-ends-soon-become-an-ai",
    "platform": "rss",
    "title": "Become an AI Engineer | Enrollment Ends Soon",
    "url": "https://blog.bytebytego.com/p/enrollment-ends-soon-become-an-ai",
    "source": "ByteByteGo",
    "published_at": "2026-05-08T15:31:40+00:00",
    "summary": "Our 6th cohort of Becoming an AI Engineer starts in about a week.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/container-design-patterns-for-distributed",
    "platform": "rss",
    "title": "Container Design Patterns for Distributed Systems",
    "url": "https://blog.bytebytego.com/p/container-design-patterns-for-distributed",
    "source": "ByteByteGo",
    "published_at": "2026-05-07T15:31:08+00:00",
    "summary": "In this article, we&#8217;ll walk through the patterns that have crystallized over the past decade, organized by the scope of their coordination.",
    "feed": "ByteByteGo Newsletter"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30400",
    "platform": "rss",
    "title": "Protocol for evaluating ChatGPT in biomedical association generation and verification using a RAG-enabled, cross-model majority voting workflow",
    "url": "https://arxiv.org/abs/2605.30400",
    "source": "Ahmed Abdeen Hamed, Luis M. Rocha",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30400v1 Announce Type: new Abstract: We present a protocol to evaluate ChatGPT's ability to generate disease-centric biomedical associations. It outlines how we generate the associations, validate the biological entities using biomedical ontologies, and verify associations using literatur",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30407",
    "platform": "rss",
    "title": "Exploring Autonomous Agentic Data Engineering for Model Specialization",
    "url": "https://arxiv.org/abs/2605.30407",
    "source": "Yujie Luo, Xiangyuan Ru, Jingsheng Zheng, Jingjing Wang, Yuqi Zhu, Jintian Zhang, Runnan Fang, Kewei Xu, Ye Liu, Zheng Wei, Jiang Bian, Zang Li, Shumin Deng",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30407v1 Announce Type: new Abstract: Large Language Models (LLMs) have demonstrated strong performance on general tasks, while often struggling to adapt to specialized domains without high-quality domain-specific data. Existing LLM-based data curation methods primarily rely on human-desig",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30415",
    "platform": "rss",
    "title": "Domain Adaptation and Reasoning Frameworks in Language Models: A Controlled Experiment with Historical Cosmology",
    "url": "https://arxiv.org/abs/2605.30415",
    "source": "Francesco De Bernardis",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30415v1 Announce Type: new Abstract: We investigate how domain adaptation reshapes explanatory behavior in language models using historical cosmology as a controlled setting. In Phase 1, we train a small language model from scratch on a pre-Copernican corpus from which explicit heliocentr",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30443",
    "platform": "rss",
    "title": "Cross-Lingual Steering for Figurative Language Generation",
    "url": "https://arxiv.org/abs/2605.30443",
    "source": "Linfeng Liu, Tiffany Zhan, Louie Hong Yao, Saptarshi Ghosh, Tianyu Jiang",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30443v1 Announce Type: new Abstract: Multilingual large language models can generate figurative language, but whether the internal signals driving this behavior are language-specific or reusable across languages is unclear. Using activation steering as a probe, we estimate a direction for",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30459",
    "platform": "rss",
    "title": "Can LLM Teams Play What? Where? When?",
    "url": "https://arxiv.org/abs/2605.30459",
    "source": "Anastasia Kotelnikova, Viktor Byzov, Maria Dolzhenkova, Evgeny Kotelnikov",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30459v1 Announce Type: new Abstract: Large language models (LLMs) remain limited on tasks requiring indirect reasoning, cultural knowledge, and coordinated hypothesis testing. We investigate whether team-based interaction improves LLM performance in What? Where? When? (ChGK), a quiz game ",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30465",
    "platform": "rss",
    "title": "Knowledge Graph-Enhanced Zero-Shot Topic Classification: A Multi-Strategy Comparative Study",
    "url": "https://arxiv.org/abs/2605.30465",
    "source": "Shahana Akter, Yatharth Vohra, Ankita Shukla, Souvika Sarkar",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30465v1 Announce Type: new Abstract: Multi-label topic classification without labeled training data is a challenging task, specially when documents contain complex relational information. We present a zero-shot multi-label topic classification framework and systematically investigate how ",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30472",
    "platform": "rss",
    "title": "Your Multimodal Speech Model Says I Have a Face for Radio",
    "url": "https://arxiv.org/abs/2605.30472",
    "source": "Maya K. Nachesa, Vlad Niculae, Vagrant Gautam",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30472v1 Announce Type: new Abstract: As large neural models have become better at language tasks, researchers are increasingly building multi- and omnimodal models that handle more modalities of data. One example is the expansion of speech recognition models to audio-visual data for noise",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30481",
    "platform": "rss",
    "title": "When English Rewrites Local Knowledge: Global Narrative Dominance in Large Language Models",
    "url": "https://arxiv.org/abs/2605.30481",
    "source": "Md Arid Hasan, Ruwad Naswan, Farhan Samir, Sharifa Sultana, Syed Ishtiaque Ahmed",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30481v1 Announce Type: new Abstract: Large language models (LLMs) are widely used as cross-lingual knowledge interfaces. However, culturally grounded questions often reflect globally dominant narratives rather than local contexts. We study this failure mode as \\textit{global narrative dom",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30487",
    "platform": "rss",
    "title": "Configurable Reward Model for Balanced Safety Alignment",
    "url": "https://arxiv.org/abs/2605.30487",
    "source": "Zhengping Jiang, Mehran Khodabandeh, Akash Bharadwaj, Manik Bhandari, Mayur Srungarapu, Anqi Liu, Benjamin Van Durme, Li Chen",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30487v1 Announce Type: new Abstract: Aligning large language models (LLMs) to heterogeneous and rapidly evolving safety requirements remains a critical challenge. Existing instruction-tuned LLMs and standalone safety classifiers often fail to generalize to new safety configurations, motiv",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30497",
    "platform": "rss",
    "title": "CanLegalRAGBench: Evaluating Retrieval-Augmented Generation on Canadian Case Law",
    "url": "https://arxiv.org/abs/2605.30497",
    "source": "Ethan Zhao, Maksym Taranukhin, Wei Cui, Moira Aikenhead, Vered Shwartz",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30497v1 Announce Type: new Abstract: RAG-based legal assistants have been growing in popularity, but LLM hallucinations remain a key issue and potentially undermines justice. While benchmarks have been developed to evaluate progress, many rely on synthetic queries rather than realistic le",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30501",
    "platform": "rss",
    "title": "Linear Ensembles Wash Away Watermarks: On the Fragility of Distributional Perturbations in LLMs",
    "url": "https://arxiv.org/abs/2605.30501",
    "source": "Zhihao Wu, Gracia Gong, Qinglin Zhu, Yudong Chen, Runcong Zhao",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30501v1 Announce Type: new Abstract: Watermarking embeds statistical signatures in AI-generated text for detection and attribution. We reveal a fundamental vulnerability: when users access multiple models (today's reality), watermarks trivially fail. Watermarks perturb output distribution",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30504",
    "platform": "rss",
    "title": "Auditing LLM Benchmarks with Item Response Theory",
    "url": "https://arxiv.org/abs/2605.30504",
    "source": "Sander Land, Daniel M. Bikel",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30504v1 Announce Type: new Abstract: LLM benchmark labels are frozen at release and silently propagated into downstream benchmarks, errors and all. We introduce an Item Response Theory-based indicator that surfaces likely mislabels at 95% precision in the top 200 examples across seven pre",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30521",
    "platform": "rss",
    "title": "Evaluating using Mock Tool Calls to Quarantine Untrusted Prompt Inputs",
    "url": "https://arxiv.org/abs/2605.30521",
    "source": "David Gros, Adam Gleave",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30521v1 Announce Type: new Abstract: Large language models must frequently process untrusted inputs, such as judging an answer from another model or running tasks like spam and harm classifiers while under adversarial pressure. These inputs are often string-formatted directly into a promp",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30529",
    "platform": "rss",
    "title": "Generalistic or Specific Embeddings, Which is Better? An Empirical Study on Search for Clinical Coding in Non-English Languages",
    "url": "https://arxiv.org/abs/2605.30529",
    "source": "David Rey-Blanco, Roberto Cruz",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30529v1 Announce Type: new Abstract: Sentence-embedding models for semantic search are overwhelmingly developed and evaluated on English corpora. When applied to clinical retrieval in other languages -- particularly retrieval of ICD-10-CM / CIE-10 codes -- recall degrades in ways often ma",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30545",
    "platform": "rss",
    "title": "Refining Word-Based Grammatical Error Annotation for L2 Korean",
    "url": "https://arxiv.org/abs/2605.30545",
    "source": "Jungyeul Park, Kyungtae Lim, Wonjun Oh, Benjamin Nguyen, Zihao Huang, Mengyang Qiu, Jayoung Song",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30545v1 Announce Type: new Abstract: Korean grammatical error correction (K-GEC) presents a structural mismatch between word-based evaluation and the morpheme-level locus of many learner errors. Postpositions and verbal endings are bound to lexical hosts, but they encode grammatical relat",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30568",
    "platform": "rss",
    "title": "Generating and Refining Dynamic Evaluation Rubrics for LLM-as-a-Judge",
    "url": "https://arxiv.org/abs/2605.30568",
    "source": "Zijie Wang, Eduardo Blanco",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30568v1 Announce Type: new Abstract: LLM-as-a-Judge is a scalable alternative to human evaluation, yet existing rubric-based methods rely on human-annotated data such as reference answers or expert-crafted rubrics. We propose to automatically generate fine-grained evaluation rubrics witho",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30574",
    "platform": "rss",
    "title": "Probing the Prompt KV Cache: Where It Becomes Dispensable",
    "url": "https://arxiv.org/abs/2605.30574",
    "source": "Vinayshekhar Bannihatti Kumar, Manoj Ghuhan Arivazhagan, Disha Makhija, Rashmi Gangadharaiah",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30574v1 Announce Type: new Abstract: Prior KV cache compression schemes empirically demonstrate that the prompt cache is partially redundant during decoding, dropping or summarising entries with little accuracy loss. We ask when and what kind of redundancy: at which layers, after how many",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30580",
    "platform": "rss",
    "title": "Speculative Decoding Across Languages",
    "url": "https://arxiv.org/abs/2605.30580",
    "source": "Nirajan Paudel, Michael Ginn, Luc De Nardi, Alexis Palmer",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30580v1 Announce Type: new Abstract: Speculative decoding has become a crucial component of large language model (LLM) inference, enabling faster generation by drafting multiple tokens and verifying them in parallel. However, small draft models tend to suffer from disproportionately poor ",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30582",
    "platform": "rss",
    "title": "AI for Monitoring and Classifying Data Used in Research Literature",
    "url": "https://arxiv.org/abs/2605.30582",
    "source": "Rafael Macalaba, Aivin V. Solatorio",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30582v1 Announce Type: new Abstract: While platforms like Google Scholar and Semantic Scholar track citations for academic papers, no comparable infrastructure exists for monitoring dataset usage in research literature, leaving the landscape of data use largely opaque. Addressing this gap",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30589",
    "platform": "rss",
    "title": "ImmigrationQA: A Source-Grounded Dataset and Small-Model Adaptation for U.S. Immigration Law",
    "url": "https://arxiv.org/abs/2605.30589",
    "source": "Nazarii Shportun",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30589v1 Announce Type: new Abstract: U.S. immigration law spans thousands of pages of official policy, federal regulations, and procedural guidance that change frequently and carry high stakes for petitioners who lack legal representation. We describe the construction of ImmigrationQA, a ",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30608",
    "platform": "rss",
    "title": "Semantic Motion Anchors: Bridging Motion and Meaning in Co-Speech Gestures",
    "url": "https://arxiv.org/abs/2605.30608",
    "source": "Varsha Suresh, Mohammad Mahdi Abootorabi, Mohamed Salman, M. Hamza Mughal, Christian Theobalt, Ashwin Ram, J\\\"urgen Steimle, Vera Demberg",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30608v1 Announce Type: new Abstract: Learning a shared representation between spoken text and gesture is central to co-speech gesture retrieval, synthesis, and understanding, but remains challenging for semantically meaningful gestures whose communicative intent is not captured by motion ",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30628",
    "platform": "rss",
    "title": "The Architecture of Errors: From Universal Impossibility to Patch-Local LLM Reliability",
    "url": "https://arxiv.org/abs/2605.30628",
    "source": "Mikhail L. Arbuzov, Lee Mosbacker, Sisong Bei, Ziwei Dong, Dmitri Kalaev, Alexey Shvets",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30628v1 Announce Type: new Abstract: Universal LLM reliability is not a finite-library problem: across all possible tasks, tools, schemas, knowledge sources, and evaluator expectations, new intervention-distinguishable failure modes can appear without bound, so no finite intervention dict",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30641",
    "platform": "rss",
    "title": "COFT: Counterfactual-Conformal Decoding for Fair Chain-of-Thought Reasoning in Large Language Models",
    "url": "https://arxiv.org/abs/2605.30641",
    "source": "Arya Fayyazi, Mehdi Kamal, Massoud Pedram",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30641v1 Announce Type: new Abstract: Large language models (LLMs) can reveal and amplify societal biases during chain-of-thought (CoT) generation. We present COFT (Chain of Fair Thought), a training-free decoding method that applies token-level fairness control at decode time, with distri",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30646",
    "platform": "rss",
    "title": "Same Patient, Different Words, Different Diagnosis? Evaluating Semantic Stability in Clinical LLMs",
    "url": "https://arxiv.org/abs/2605.30646",
    "source": "Mahdi Alkaeed, Adnan Qayyum, Nabeel Abo Kashreef, Muhammad Bilal, Junaid Qadir",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30646v1 Announce Type: new Abstract: Large Language Models (LLMs) are increasingly used in clinical applications. However, their behavior remains highly sensitive to subtle linguistic variations, such as rephrasing or syntactic variation. This sensitivity poses risks in safety-critical he",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30653",
    "platform": "rss",
    "title": "Counterfactual Graph for Multi-Agent LLM Calibration",
    "url": "https://arxiv.org/abs/2605.30653",
    "source": "Jiatan Huang, Mingchen Li, Ziming Li, Sunjae Kwon, Hong Yu, Chuxu Zhang",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30653v1 Announce Type: new Abstract: Multi-agent LLM systems often treat agreement as evidence: when many agents in a panel give the same answer, that answer is assumed to be more reliable. We show that this assumption can fail after agents communicate. Communication can induce correlated",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30654",
    "platform": "rss",
    "title": "EUDAIMONIA: Evaluating Undesirable Dynamics in AI",
    "url": "https://arxiv.org/abs/2605.30654",
    "source": "Jun Rui Huang, Wang Bill Zhu, Ziyi Liu, Nathanael Fast, Ravi Iyer, Robin Jia",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30654v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly used as conversational partners for companionship, emotional disclosure, and interpersonal advice, but the social dynamics of these interactions can create harms that are not captured by capability-oriented",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30668",
    "platform": "rss",
    "title": "CobSeg: Coherence Boundary Modeling for Dialogue Topic Segmentation",
    "url": "https://arxiv.org/abs/2605.30668",
    "source": "Sijin Sun, Liangbin Zhao, Jiaxiang Cai, Ming Deng, Mingyu Luo, Xiuju Fu",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30668v1 Announce Type: new Abstract: Dialogue topic segmentation is critical in many human-AI collaborative applications which requires identifying heterogeneous boundary cues, including lexical transitions near utterance edges and semantic discontinuities across utterances. Existing utte",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30673",
    "platform": "rss",
    "title": "TeachObs: A Human-Validated Benchmark for Multimodal Teaching Observation and Model Evaluation",
    "url": "https://arxiv.org/abs/2605.30673",
    "source": "Yeil Jeong, Youngjin Yoo, Seobin Sohn, Hyejin Han, Jinseo Lee, Scott Howard, Unggi Lee",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30673v1 Announce Type: new Abstract: Classroom videos contain observable teaching practices, but their pedagogical and visual signals are rarely organized in forms suitable for model evaluation. We present \\textit{TeachObs}, a human-validated benchmark for multimodal teaching observation ",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30675",
    "platform": "rss",
    "title": "Human-Alignment, Calibration, and Activation Patterns in Large Language Model Uncertainty",
    "url": "https://arxiv.org/abs/2605.30675",
    "source": "Kyle Moore, Jesse Roberts, Daryl Watson, William Ward, Grayson Heyboer",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30675v1 Announce Type: new Abstract: Uncertainty Quantification is a large and growing subfield of large language model behavioral analysis. Primarily to recognize and combat hallucination, the field has largely focused on measuring and improving calibration, the accuracy of uncertainty j",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30690",
    "platform": "rss",
    "title": "ElasticMem: Latent Memory as a Learnable Resource for LLM Agents",
    "url": "https://arxiv.org/abs/2605.30690",
    "source": "Tao Feng, Chongrui Ye, Tianyang Luo, Jingjun Xu, Xueqiang Xu, Haozhen Zhang, Ge Liu, Jiaxuan You",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30690v1 Announce Type: new Abstract: Long-term memory is essential for LLM agents to reason coherently across extended interactions, personalize responses, and reuse past experience. However, existing memory-augmented methods typically treat memory as a fixed resource: text-space approach",
    "feed": "cs.CL updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30358",
    "platform": "rss",
    "title": "QASM-Eval: A Dataset to Train and Evaluate LLMs on OpenQASM-3 Beyond Quantum Circuits",
    "url": "https://arxiv.org/abs/2605.30358",
    "source": "Zhenxiao Fu, Lei Jiang, Fan Chen",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30358v1 Announce Type: new Abstract: Quantum computing remains in the Noisy Intermediate-Scale Quantum (NISQ) era, where the performance is highly constrained to noise. Addressing the limitation often requires hardware-facing capabilities beyond gate-sequence circuit specification, includ",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30374",
    "platform": "rss",
    "title": "Gait2Hip-60: A Unified Deep Learning Benchmark for Predicting Hip Muscle Forces and Joint Moments from Multi-Cadence Gait Kinematics",
    "url": "https://arxiv.org/abs/2605.30374",
    "source": "Jiaqi Zhang, Ji Hou, Qing Sun, Xianzhi Gao, Bo Huo",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30374v1 Announce Type: new Abstract: Estimating hip muscle forces and joint moments during gait typically relies on musculoskeletal simulation, which is informative but time-consuming and difficult to apply in clinical settings. This study developed a deep learning framework to predict th",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30376",
    "platform": "rss",
    "title": "Unicorn: Scaling High-Dimensional Time Series Forecasting via Universal Correlation Modeling",
    "url": "https://arxiv.org/abs/2605.30376",
    "source": "Haochen Yuan, Yichen Song, Yunbo Wang, Xiaokang Yang",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30376v1 Announce Type: new Abstract: Modern time series architectures face a fundamental trade-off: channel-independent models scale well with increasing data volume but ignore critical inter-channel dependencies, while channel-dependent models are expressive but remain ``dimension-bounde",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30381",
    "platform": "rss",
    "title": "When LLMs Learn to Be Consistently Wrong: A Multi-Model Study of Linear Representations of Synthetic Deception",
    "url": "https://arxiv.org/abs/2605.30381",
    "source": "Vahideh Zolfaghari",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30381v1 Announce Type: new Abstract: Deceptive alignment, in which models maintain accurate internal representations while deliberately producing false outputs, remains a central challenge in AI safety. While strategic deception is the primary long-term concern, synthetic dishonesty - ind",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30385",
    "platform": "rss",
    "title": "LLMs Without Deep Neural Networks: New Architecture, Benefits and Case Study",
    "url": "https://arxiv.org/abs/2605.30385",
    "source": "Vincent Granville",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30385v1 Announce Type: new Abstract: The purpose of this article is to provide validation to my deep neural network alternative in the context of LLMs. Very recently, there has been a significant interest by Chinese researchers in a model called RBF network, as a substitute to standard DN",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30387",
    "platform": "rss",
    "title": "Functional MRI Time Series Generation via Wavelet-Based Image Transform and Spectral Flow Matching for Brain Disorder Identification",
    "url": "https://arxiv.org/abs/2605.30387",
    "source": "Hwa Hui Tew, Junn Yong Loo, Fang Yu Leong, Julia K. Lau, Ding Fan, Hernando Ombao, Rapha\\\"el C. -W. Phan, Chee Pin Tan, Chee-Ming Ting",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30387v1 Announce Type: new Abstract: Functional Magnetic Resonance Imaging (fMRI) provides non-invasive access to dynamic brain activity by measuring blood oxygen level-dependent (BOLD) signals over time. However, the resource-intensive nature of fMRI acquisition limits the availability o",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30388",
    "platform": "rss",
    "title": "A Novel Evaluation Metric for Unsupervised Learning in AIS-Based Maritime Anomaly Detection: MADQI",
    "url": "https://arxiv.org/abs/2605.30388",
    "source": "Ismet Gocer, Zakirul Bhuiyan, Raza Hasan, Shakeel Ahmad",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30388v1 Announce Type: new Abstract: This paper introduces a new systematic framework for detecting anomalies in maritime Automatic Identification System (AIS) datasets. These anomalies include abnormal vessel behaviours related to speed, position jumps, time gaps, and turn angles. Althou",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30393",
    "platform": "rss",
    "title": "NumLeak: Public Numeric Benchmarks as Latent Labels in Foundation Models",
    "url": "https://arxiv.org/abs/2605.30393",
    "source": "Anany Kotawala",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30393v1 Announce Type: new Abstract: Public numeric benchmarks appear in pretraining, so an evaluation that conditions on a date may be measuring memorized recall rather than out-of-sample skill. We introduce NumLeak, a measurement framework that combines API-boundary probes on production",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30434",
    "platform": "rss",
    "title": "LongDS-Bench: On the Failure of Long-Horizon Agentic Data Analysis",
    "url": "https://arxiv.org/abs/2605.30434",
    "source": "Kewei Xu, Xiaoben Lu, Shuofei Qiao, Zihan Ding, Haoming Xu, Lei Liang, Ningyu Zhang",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30434v1 Announce Type: new Abstract: Real-world data analysis is inherently iterative, yet existing benchmarks mostly evaluate isolated or short interactive tasks, leaving agents' ability to track evolving analytical context over long horizons untested. We introduce LongDS, a benchmark fo",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30447",
    "platform": "rss",
    "title": "Calibrated Preference Learning: The Case of Label Ranking",
    "url": "https://arxiv.org/abs/2605.30447",
    "source": "Santo M. A. R. Thies, Viktor Bengs, Timo Kaufmann, Sebastian J. Vollmer, Eyke H\\\"ullermeier",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30447v1 Announce Type: new Abstract: Calibration, the alignment of predicted probabilities with true outcome frequencies, is essential for reliable decision-making. While extensively studied for classification and regression, calibration has not been formally addressed for probabilistic l",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30448",
    "platform": "rss",
    "title": "Bounded Behavioral Indistinguishability for Black-Box LLM Distillation",
    "url": "https://arxiv.org/abs/2605.30448",
    "source": "Munawar Hasan",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30448v1 Announce Type: new Abstract: Black-box LLM distillation is usually evaluated as an output-matching problem: a student is considered successful when its responses are semantically similar to, or task-consistent with, those of a teacher. However, output similarity does not imply tha",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30451",
    "platform": "rss",
    "title": "VeriGate: Verifier-Gated Step-Level Supervision for GRPO",
    "url": "https://arxiv.org/abs/2605.30451",
    "source": "Aakriti Agrawal, Minghui Liu, Furong Huang",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30451v1 Announce Type: new Abstract: Group Relative Policy Optimization (GRPO) is an effective recipe for training reasoning models with verifier-based outcome rewards, but its supervision is sparse: when all sampled trajectories for a prompt receive the same verifier reward, the group-re",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30452",
    "platform": "rss",
    "title": "A Unified Framework for Gradient Aggregation in Multi-Objective Optimization",
    "url": "https://arxiv.org/abs/2605.30452",
    "source": "Zeou Hu, Kelvin Ho, Yaoliang Yu",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30452v1 Announce Type: new Abstract: Many machine learning problems involve multiple inherent trade-offs that are best addressed by gradient-based multi-objective optimization (MOO) algorithms. Existing methods are often proposed with various motivations, analyzed case by case, and differ",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30456",
    "platform": "rss",
    "title": "DisjunctiveNet: Neural Symbolic Learning via Differentiable Convexified Optimization Layers",
    "url": "https://arxiv.org/abs/2605.30456",
    "source": "Shraman Pal, Can Li",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30456v1 Announce Type: new Abstract: Many learning tasks in science and engineering are characterized by sparse datasets, which limits the effectiveness of purely data-driven approaches. At the same time, these problems are often accompanied by rich domain knowledge derived from physical ",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30461",
    "platform": "rss",
    "title": "Scalable Constrained Multi-Agent Reinforcement Learning via State Augmentation and Consensus for Separable Dynamics",
    "url": "https://arxiv.org/abs/2605.30461",
    "source": "Santiago Amaya-Corredor, Miguel Calvo-Fullana, Anders Jonsson",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30461v1 Announce Type: new Abstract: We present a distributed approach for constrained Multi-Agent Reinforcement Learning (MARL) that combines state-augmented policy learning with distributed consensus over dual variables. Our method targets systems where agents have separable dynamics bu",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30462",
    "platform": "rss",
    "title": "idSCD: Identifying Training Datasets through Semantic Correlation Descriptors",
    "url": "https://arxiv.org/abs/2605.30462",
    "source": "Andrada Gobeaja, Ionut Hodoroaga, Elena Burceanu, Marius Leordeanu",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30462v1 Announce Type: new Abstract: Can a dataset be recognized from the spurious correlations it induces during training? We argue that datasets leave dataset-specific traces in a model's learned semantic correlation structure: incidental regularities that are predictive within a datase",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30470",
    "platform": "rss",
    "title": "Can Subgraph Explanations Be Weaponized to Steal Graph Neural Networks?",
    "url": "https://arxiv.org/abs/2605.30470",
    "source": "Ojas Nimase, Jiate Li, Yue Zhao, Yushun Dong",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30470v1 Announce Type: new Abstract: Graph Machine Learning as a Service (GMLaaS) platforms increasingly implement explainability interfaces to meet regulatory transparency requirements. However, this transparency creates exploitable vulnerabilities for model extraction attacks. We presen",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30479",
    "platform": "rss",
    "title": "Universal Multiclass Transductive Online Learning",
    "url": "https://arxiv.org/abs/2605.30479",
    "source": "Steve Hanneke, Hongao Wang",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30479v1 Announce Type: new Abstract: We consider the problem of universal transductive online classification with a possibly unbounded label space. This setting considers online learning, with the sequence of instances (without labels) known to the learner in advance. We say a concept cla",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30482",
    "platform": "rss",
    "title": "Discovering a Zeta Map Algorithm on Dyck Paths via Mechanistic Interpretability",
    "url": "https://arxiv.org/abs/2605.30482",
    "source": "Xiaoyu Huang, Blake Jackson, Kyu-Hwan Lee",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30482v1 Announce Type: new Abstract: Machine learning is increasingly used in mathematical discovery, but in mathematics the desired output is often not a prediction itself, but an explicit construction that can be checked independently. We study this setting through the zeta map on Dyck ",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30486",
    "platform": "rss",
    "title": "Graph-Conditioned Mixture of Graph Neural Network Experts for Traffic Forecasting",
    "url": "https://arxiv.org/abs/2605.30486",
    "source": "Amirhossein Ghaffari, Saeid Sheikhi, Ekaterina Gilman",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30486v1 Announce Type: new Abstract: Spatio-temporal forecasting on sensor graphs is commonly tackled with a single backbone architecture applied uniformly across all nodes, although graph regions can exhibit different dynamics. Road segments differ in functional class, structure, and tra",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30514",
    "platform": "rss",
    "title": "MAAT: Multi-phase Adapter-Aware Targeted Unlearning",
    "url": "https://arxiv.org/abs/2605.30514",
    "source": "Suryash Yagnik, Shubham Gaur, Saksham Thakur, Vinija Jain, Aman Chadha, Amitava Das",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30514v1 Announce Type: new Abstract: Machine unlearning evaluation is structurally skewed: Why-type questions, which probe causal and relational knowledge, comprise less than 0.06% of CounterFact, 0.6% of ZSRE, and less than 1.3% of TOFU, MUSE, and WMDP-Cyber. This near-zero representatio",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30523",
    "platform": "rss",
    "title": "Revisiting Padded Transformer Expressivity: Which Architectural Choices Matter and Which Don't",
    "url": "https://arxiv.org/abs/2605.30523",
    "source": "Anej Svete, William Merrill, Ryan Cotterell, Ashish Sabharwal",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30523v1 Announce Type: new Abstract: Recent work describes what transformers can and cannot compute through connections to boolean circuits, but existing results lack exact characterizations and are sensitive to modeling choices. Padded transformers -- to whose input filler symbols such a",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30524",
    "platform": "rss",
    "title": "Representation Collapse in Sequential Post-Training of Large Language Models",
    "url": "https://arxiv.org/abs/2605.30524",
    "source": "Yichen Liu, Mingyu Chen, Hao Wang, Xiaoran Xu, Chenxi Lin, Rui Zhang, Yutong Zhou, Yuxin Yang, Jiarui Wu, Wei Sun",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30524v1 Announce Type: new Abstract: Large language models are now adapted through chains of post-training stages rather than through a single instruction-tuning pass. This paper studies whether such sequential post-training gradually compresses internal representations into low-rank, ani",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30526",
    "platform": "rss",
    "title": "Measuring, Localizing, and Ablating Alignment Signatures in LLMs",
    "url": "https://arxiv.org/abs/2605.30526",
    "source": "Aniket Anand, Janvijay Singh, Zhewei Sun, Dilek Hakkani-T\\\"ur, Nick Feamster",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30526v1 Announce Type: new Abstract: Aligned language models often exhibit a recognizable AI-like style, yet its connection to post-training and internal representations remains poorly understood. In this work, we study whether post-training introduces or amplifies AI-like stylistic regul",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30537",
    "platform": "rss",
    "title": "The Long-Term Effects of Data Selection in LLM Fine-Tuning",
    "url": "https://arxiv.org/abs/2605.30537",
    "source": "Yuxin Yang, Aoxiong Zeng, Xiangquan Yang",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30537v1 Announce Type: new Abstract: Data selection is increasingly used to reduce the cost of large language model (LLM) fine-tuning, with recent methods prioritizing samples by current utility, diversity, quality, or influence. This paper studies a different question: when fine-tuning o",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30538",
    "platform": "rss",
    "title": "DisasterLex: An Expert Concept-to-Schema Knowledge Graph for Geospatial Reasoning in Disaster Analytics",
    "url": "https://arxiv.org/abs/2605.30538",
    "source": "Yiming Xiao, Ankit Basu, Kai Yin, Sahil Vartak, Christian Swords, Ali Mostafavi",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30538v1 Announce Type: new Abstract: Disasters are inevitable and increasingly costly, and effective response depends on querying structured tabular data: precise, information-dense records of hazard, exposure, vulnerability, and lifeline infrastructure that underpin disaster management. ",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30541",
    "platform": "rss",
    "title": "SubsurfaceGen: Procedural Generation of Field-Scale Earth Models and Seismic Data",
    "url": "https://arxiv.org/abs/2605.30541",
    "source": "Joseph Stitt, Pratik Rathore, Madeleine Udell, Ching-Yao Lai",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30541v1 Announce Type: new Abstract: Full waveform inversion (FWI) is the gold standard for subsurface imaging, with applications from carbon sequestration to energy and mineral exploration to earthquake hazard assessment. Machine learning approaches to FWI need field-scale, geologically ",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30550",
    "platform": "rss",
    "title": "Early Prediction of Future Behavioral Strategy from Process Traces",
    "url": "https://arxiv.org/abs/2605.30550",
    "source": "Robert Kasumba, Dennis Barbour, Chien-Ju Ho",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30550v1 Announce Type: new Abstract: Adaptive systems often need to make task-specific decisions about people from limited evidence: a tutor may need to anticipate how a learner will approach a new problem, a game may need to adapt when a player enters a new level, and a human-AI system m",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30553",
    "platform": "rss",
    "title": "Destruction is a General Strategy to Learn Generation; Diffusion's Strength is to Take it Seriously; Exploration is the Future",
    "url": "https://arxiv.org/abs/2605.30553",
    "source": "Pierre-Andr\\'e No\\\"el",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30553v1 Announce Type: new Abstract: I present diffusion models as part of a family of machine learning techniques that withhold information from a model's input and train it to guess the withheld information. I argue that diffusion's destroying approach to withholding is more flexible th",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30556",
    "platform": "rss",
    "title": "Supervised Training Rapidly Degrades Early Visual Cortex Alignment Across Biologically Plausible Learning Rules",
    "url": "https://arxiv.org/abs/2605.30556",
    "source": "Nils Leutenegger",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30556v1 Announce Type: new Abstract: Random, untrained neural networks consistently match or exceed trained networks in representational similarity to early visual cortex. This puzzling finding challenges the assumption that learning improves brain alignment. We investigate it by tracking",
    "feed": "cs.LG updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30512",
    "platform": "rss",
    "title": "PhyDrawGen: Physically Grounded Diagram Generation from Natural Language",
    "url": "https://arxiv.org/abs/2605.30512",
    "source": "Nafiul Haque, Syed Nazmus Sakib, Shifat E Arman",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30512v1 Announce Type: new Abstract: Generating physics diagrams from text requires strict adherence to physical laws. While current generative models produce visually plausible outputs, they systematically hallucinate force vectors, ignore conservation laws, and violate geometric constra",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30542",
    "platform": "rss",
    "title": "Physically Viable World Models: A Case for Query-Conditioned Embodied AI",
    "url": "https://arxiv.org/abs/2605.30542",
    "source": "Adam J. Thorpe, Stepan Tretiakov, Cheng-Hsi Hsiao, Su Ann Low, Xingjian Li, Hassan Iqbal, Neel P. Bhatt, Ufuk Topcu, Krishna Kumar",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30542v1 Announce Type: new Abstract: World models for embodied AI must be physically viable: constructed to answer intervention queries by representing the physical structure governing action outcomes, rather than merely predicting future observations. Existing observation-predictive worl",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30563",
    "platform": "rss",
    "title": "Transforming and Encoding FTS for SAT Solving: What Helps, What Hurts (Extended Version)",
    "url": "https://arxiv.org/abs/2605.30563",
    "source": "Jo\\~ao Filipe, \\'Alvaro Torralba, Gregor Behnke",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30563v1 Announce Type: new Abstract: Factored tasks are a classical planning representation that extends SAS+ with limited forms of disjunctive preconditions, conditional effects, and angelic nondeterminism. This allows for a more compact representation of tasks than traditional formalism",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30570",
    "platform": "rss",
    "title": "Procedural Generation of First Person Shooter Maps using Map-Elites",
    "url": "https://arxiv.org/abs/2605.30570",
    "source": "Simone de Donato, Pier Luca Lanzi, Daniele Loiacono",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30570v1 Announce Type: new Abstract: We investigate the application of MAP-Elites (a well-known quality diversity algorithm) to design levels for First-Person Shooter (FPS) games. We consider two well-known map representations (All-Black and Grid-Graph) and introduce two novel representat",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30576",
    "platform": "rss",
    "title": "Uncertainty-Aware and Temporally Regulated Expert Advice in Reinforcement Learning for Autonomous Driving",
    "url": "https://arxiv.org/abs/2605.30576",
    "source": "Ahmed Abouelazm, Felix Klingebiel, Philip Sch\\\"orner, J. Marius Z\\\"ollner",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30576v1 Announce Type: new Abstract: Exploration in reinforcement learning for autonomous driving is inherently unsafe: agents must experience novel behaviors to learn, yet exploration can lead to collisions or off-road driving. We propose an uncertainty-aware framework that leverages exp",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30621",
    "platform": "rss",
    "title": "Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents",
    "url": "https://arxiv.org/abs/2605.30621",
    "source": "Minhua Lin, Juncheng Wu, Zijun Wang, Zhan Shi, Yisi Sang, Bing He, Zewen Liu, Tianxin Wei, Zongyu Wu, Zhiwei Zhang, Dakuo Wang, Xiang Zhang, Benoit Dumoulin, Cihang Xie, Yuyin Zhou, Suhang Wang, Hanqing Lu",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30621v1 Announce Type: new Abstract: LLM agents are increasingly deployed as systems built around editable external harnesses, including prompts, skills, memories and tools, that shape task execution without changing model parameters. Harness self-evolution adapts such agents by updating ",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30637",
    "platform": "rss",
    "title": "EHRBench: An Automated and Reliable EHR-based Benchmark for Clinical Decision Making with LLMs",
    "url": "https://arxiv.org/abs/2605.30637",
    "source": "Yuzhang Xie, Keqi Han, Yunpeng Xiao, Hejie Cui, Guanchen Wu, Ziyang Zhang, Kai Shu, Jiaying Lu, Xiao Hu, Carl Yang",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30637v1 Announce Type: new Abstract: Clinical decision-making (CDM) is central to real-world clinical workflows, where clinicians infer diagnoses, select treatments, or anticipate future health outcomes under incomplete evidence. LLMs are increasingly used to support these decisions due t",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30664",
    "platform": "rss",
    "title": "Structure-Induced Information for Rerooting Levin Tree Search",
    "url": "https://arxiv.org/abs/2605.30664",
    "source": "Jake Tuero, Michael Buro, Laurent Orseau, Levi H. S. Lelis",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30664v1 Announce Type: new Abstract: Subgoal-based policy tree search, which uses a policy to guide search, is effective for complex single-agent deterministic problems but often relies on explicit subgoal generation that can incur substantial overhead and hinders scalability. In this pap",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30680",
    "platform": "rss",
    "title": "Healthcare Mechanisms from Policy-as-Code Search under Strategic Provider Response",
    "url": "https://arxiv.org/abs/2605.30680",
    "source": "Zihan Wang, Xiang Xu, Hongyuan Zha, Wenhao Li",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30680v1 Announce Type: new Abstract: Healthcare mechanisms are inseparable from the strategic provider response they induce: existing healthcare AI benchmarks hold this response fixed and so cannot evaluate mechanisms by the equilibrium they produce. We recast hospital mechanism design as",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30738",
    "platform": "rss",
    "title": "MAVEN: Improving Generalization in Agentic Tool Calling",
    "url": "https://arxiv.org/abs/2605.30738",
    "source": "Omkar Ghugarkar, Vishvesh Bhat, Muhammad Ahmed Mohsin, Asad Aali",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30738v1 Announce Type: new Abstract: Generalization across agentic tool-calling environments remains a central challenge for reliable agentic reasoning systems. Although large language models achieve strong results on individual benchmarks, their ability to compose reasoning strategies, p",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30747",
    "platform": "rss",
    "title": "Generating Graph-like Rules for Knowledge Graph Reasoning via Diffusion Models",
    "url": "https://arxiv.org/abs/2605.30747",
    "source": "Haoxiang Cheng, Yunfei Wang, Chao Chen, Kewei Cheng, Zhipeng Lin, Haoxuan Li, Changjun Fan, Shixuan Liu",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30747v1 Announce Type: new Abstract: Logical rules constitute a cornerstone of knowledge graph (KG) reasoning, valued for their interpretability and ability to model relational patterns. However, existing rule mining methods predominantly focus on simple chain-like rules and therefore neg",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30785",
    "platform": "rss",
    "title": "Learning Agent-Compatible Context Management for Long-Horizon Tasks",
    "url": "https://arxiv.org/abs/2605.30785",
    "source": "Lu Yi, Runlin Lei, Liuyi Yao, Yuexiang Xie, Yuyang Li, Wenhao Zhang, Zhewei Wei, Yaliang Li, Jian-Yun Nie",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30785v1 Announce Type: new Abstract: LLM agents increasingly face long-horizon tasks such as web search and deep research in real-world applications, where accumulated context can cause long-context degradation and reasoning failures. Prior work mitigates this through context management w",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30803",
    "platform": "rss",
    "title": "PReMISE: Policy Rubrics as Measurement Specifications for LLM Judges",
    "url": "https://arxiv.org/abs/2605.30803",
    "source": "Swastik Roy, Rajkumar Pujari, Tharindu Kumarage, Charith Peris, Rahul Gupta, Anna Rumshisky, Pradeep Natarajan, Venkatesh Saligrama",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30803v1 Announce Type: new Abstract: LLM judges are increasingly used to evaluate open-ended responses, but their scores depend strongly on the rubrics that condition them. A vague rubric asking for a response to be ``helpful and factual'' can reward polished answers that invent facts or ",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30824",
    "platform": "rss",
    "title": "Planner-Centric Reinforcement Learning for Deep Research with Structure-Aware Reward",
    "url": "https://arxiv.org/abs/2605.30824",
    "source": "Mustafa Anis Hussain, Xinle Wu, Yao Lu",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30824v1 Announce Type: new Abstract: Deep research tasks require LLMs to plan what to investigate, retrieve evidence, and synthesize long-form answers across multiple branches of inquiry. Existing training paradigms either rely on short-form verifiable QA as a proxy or optimize monolithic",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30832",
    "platform": "rss",
    "title": "SLAT: Segment-Level Adaptive Trimming for Efficient CoT Reasoning",
    "url": "https://arxiv.org/abs/2605.30832",
    "source": "Jian Yao, Xiongcai Luo, Ran Cheng, Kay Chen Tan",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30832v1 Announce Type: new Abstract: Recent advances in Large Reasoning Models have significantly improved chain-of-thought (CoT) capabilities via reinforcement learning (RL). However, generated reasoning chains frequently suffer from structural redundancy (i.e., \\emph{overthinking}), inc",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30838",
    "platform": "rss",
    "title": "COMPASS: Cognitive MCTS-Guided Process Alignment for Safe Search Agents",
    "url": "https://arxiv.org/abs/2605.30838",
    "source": "Wenkai Shen, Pengyang Zhou, Jiahe Xu, Jiaming Qian, Haozhe He, Zhihao Huang, Chaochao Chen, Xiaolin Zheng",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30838v1 Announce Type: new Abstract: LLM-powered search agents enable multi-step reasoning and tool use. However, these capabilities introduce retrieval-induced safety degradation, as harmful intents may decompose into seemingly innocuous sub-queries that lead to unsafe outcomes. Existing",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30861",
    "platform": "rss",
    "title": "Distilling LLM Feedback for Lean Theorem Proving",
    "url": "https://arxiv.org/abs/2605.30861",
    "source": "Gaetan Narozniak, G\\'erard Biau, R\\'emi Munos, Ahmad Rammal, Pierre Marion",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30861v1 Announce Type: new Abstract: Post-training for reasoning models typically combines supervised fine-tuning with reinforcement learning from verifiable rewards, most commonly with GRPO. However, this algorithm suffers from sparse rewards, limited exploration, and mode collapse. Buil",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30898",
    "platform": "rss",
    "title": "UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling",
    "url": "https://arxiv.org/abs/2605.30898",
    "source": "Kaiyu Huang, Xingyu Wang, Mingze Kong, Zhubo Shi, Yuqian Hou, Hong Xu, Zhongxiang Dai, Minchen Yu, Qingjiang Shi",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30898v1 Announce Type: new Abstract: In real-world deployments of large language models (LLMs), balancing inference quality and computational cost has become a central challenge. Existing approaches tackle this trade-off along two largely independent dimensions: model routing, which switc",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30900",
    "platform": "rss",
    "title": "BilliardPhys-Bench: Benchmarking Physical Reasoning and Visual Dynamics of Multimodal LLMs",
    "url": "https://arxiv.org/abs/2605.30900",
    "source": "Ben Wang, Xiaogang Li, Ruochen Gao, Peiyao Xiao, Chengliang Xu, Zeyu Wang, Zichao Chen, Bing Zhao, Hu Wei",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.30900v1 Announce Type: new Abstract: Current multimodal models handle static image recognition well, but intuitive physical reasoning remains a weakness. Predicting how objects will move and interact from a single image is still difficult for these systems. We present BilliardPhys-Bench, ",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.31021",
    "platform": "rss",
    "title": "A Persona-Based Evaluation Framework for Pluralistic Alignment in Generative AI",
    "url": "https://arxiv.org/abs/2605.31021",
    "source": "Atahan Karagoz",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.31021v1 Announce Type: new Abstract: Current alignment paradigms for generative artificial intelligence rely predominantly on monolithic benchmarking frameworks that reduce the plurality of human judgment to aggregated statistical baselines, thereby obscuring cultural, demographic, and co",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.31023",
    "platform": "rss",
    "title": "HADT: A Heterogeneous Multi-Agent Differential Transformer for Autonomous Earth Observation Satellite Cluster",
    "url": "https://arxiv.org/abs/2605.31023",
    "source": "Mohamad A. Hady, Muhammad Anwar Masum, Siyi Hu, Mahardhika Pratama, Jimmy Cao, Ryszard Kowalczyk",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.31023v1 Announce Type: new Abstract: This work addresses the problem of autonomous resource management in heterogeneous satellite cluster conducting Earth Observation (EO) missions including optical and Synthetic Aperture Radar (SAR) satellites. In autonomous operation mode, satellites ar",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.31031",
    "platform": "rss",
    "title": "GraphARC: A Comprehensive Benchmark for Graph-Based Abstract Reasoning",
    "url": "https://arxiv.org/abs/2605.31031",
    "source": "Saku Peltonen, August B{\\o}gh R{\\o}nberg, Andreas Plesner, Roger Wattenhofer",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.31031v1 Announce Type: new Abstract: Relational reasoning lies at the heart of intelligence, but existing benchmarks are typically confined to formats such as grids or text. We introduce GraphARC, a benchmark for abstract reasoning on graph-structured data. GraphARC generalizes the few-sh",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.31100",
    "platform": "rss",
    "title": "Vector Linking via Cross-Model Local Isometric Consistency",
    "url": "https://arxiv.org/abs/2605.31100",
    "source": "Ziying Chen, Yang Cao, He Sun, Beining Yang, Tianjian Yang",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.31100v1 Announce Type: new Abstract: We study Vector Linking: given two embedding clouds produced by different black-box encoders over partially overlapping datasets, recover cross-model object correspondences using only vectors. Empirically and theoretically, we show that independently t",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.31167",
    "platform": "rss",
    "title": "LLM-FACETS: A Privacy-Preserving Framework for Evaluating LLM Transparency and Accountability",
    "url": "https://arxiv.org/abs/2605.31167",
    "source": "Tom Lucas, Alessio Buscemi, Alfredo Capozucca, German Castignani, Barbara Delacroix",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.31167v1 Announce Type: new Abstract: Assessing whether Large Language Models outputs are factually grounded, epistemically calibrated, and methodologically reproducible is a prerequisite for responsible AI deployment. Yet auditing LLMs remains inaccessible to non-technical practitioners: ",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.31254",
    "platform": "rss",
    "title": "Formalizing and falsifying causal pathways of rare events",
    "url": "https://arxiv.org/abs/2605.31254",
    "source": "Anahita Haghighat, Dominik Janzing",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.31254v1 Announce Type: new Abstract: Building on recent formalizations of root cause analysis for rare events (``outliers'') in structural equation models, we propose a formal definition of a causal pathway and discuss its testable implications. We identify conditions under which these im",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.31264",
    "platform": "rss",
    "title": "COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation",
    "url": "https://arxiv.org/abs/2605.31264",
    "source": "Tianyi Zhou, Dongrui Liu, Leitao Yuan, Jing Shao, Xia Hu",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.31264v1 Announce Type: new Abstract: LLM agents are increasingly expected not only to complete isolated tasks, but also to carry bounded representations of human expertise, judgment, and interaction style. Building such person-grounded agents remains difficult because actionable knowledge",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.31278",
    "platform": "rss",
    "title": "Industrializing Prediction-Powered Inference: The GLIDE Library for Reliable GenAI and Agentic Systems Evaluation",
    "url": "https://arxiv.org/abs/2605.31278",
    "source": "Gr\\'egoire Martinon, Ibrahim Merad, Mohammed Raki",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.31278v1 Announce Type: new Abstract: Reliable evaluation of agentic systems requires unbiased estimates with valid uncertainty, but standard practice navigates between costly human annotation and biased LLM-as-judge proxies. Prediction-powered inference (PPI) combines both into debiased e",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.31308",
    "platform": "rss",
    "title": "TraceGraph: Shared Decision Landscapes for Diagnosing and Improving Agent Trajectories",
    "url": "https://arxiv.org/abs/2605.31308",
    "source": "Junjie Nian, Kang Chen, Ge Zhang, Yixin Cao, Yugang Jiang",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.31308v1 Announce Type: new Abstract: Agent benchmarks increasingly record rich interaction trajectories, yet evaluation often reduces each rollout to a pass rate or reward score. We introduce TraceGraph, a graph-based framework that turns released multi-model agent trajectories into share",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.31354",
    "platform": "rss",
    "title": "Diagnosing Failure Modes of Shared-State Collaboration in Resource-Constrained Visual Agents",
    "url": "https://arxiv.org/abs/2605.31354",
    "source": "Yunpeng Zhou",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.31354v1 Announce Type: new Abstract: Modular visual reasoning systems increasingly rely on shared working memory for multi-step collaboration, yet the failure dynamics of intermediate state evolution in low-capacity regimes remain underexplored. We study failure modes of collaborative rea",
    "feed": "cs.AI updates on arXiv.org"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.31365",
    "platform": "rss",
    "title": "Learning to Adapt: Self-Improving Web Agent via Cognitive-Aware Exploration",
    "url": "https://arxiv.org/abs/2605.31365",
    "source": "Weile Chen, Bingchen Miao, Qifan Yu, Wendong Bu, Guoming Wang, Wenqiao Zhang, Shengyu Zhang, Juncheng Li, Siliang Tang",
    "published_at": "2026-06-01T04:00:00+00:00",
    "summary": "arXiv:2605.31365v1 Announce Type: new Abstract: Recent advances in Multimodal Large Language Models (MLLMs) have led to promising progress in web agents. However, existing web agents often rely on handcrafted execution pipelines or expensive expert trajectories, limiting their adaptability to comple",
    "feed": "cs.AI updates on arXiv.org"
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
    "comments": 466
  },
  {
    "id": "hn:48289950",
    "platform": "hackernews",
    "title": "Claude Code as a Daily Driver: Claude.md, Skills, Subagents, Plugins, and MCPs",
    "url": "https://arps18.github.io/posts/claude-code-mastery/",
    "source": "arps18",
    "published_at": "2026-05-27T05:13:39+00:00",
    "summary": "",
    "points": 442,
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
    "points": 326,
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
    "points": 193,
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
    "id": "hn:48275571",
    "platform": "hackernews",
    "title": "Show HN: skills-for-humanity – 171 structured reasoning skills for Claude Code",
    "url": "https://github.com/human-avatar/skills-for-humanity",
    "source": "finnworks",
    "published_at": "2026-05-26T05:58:43+00:00",
    "summary": "",
    "points": 28,
    "comments": 7
  },
  {
    "id": "hn:48231575",
    "platform": "hackernews",
    "title": "Show HN: Spec-Driven Development Workflow for Claude Code",
    "url": "https://news.ycombinator.com/item?id=48231575",
    "source": "sermakarevich",
    "published_at": "2026-05-22T03:17:38+00:00",
    "summary": "",
    "points": 20,
    "comments": 12
  },
  {
    "id": "hn:48318978",
    "platform": "hackernews",
    "title": "Python utility package for building Claude Code hooks",
    "url": "https://github.com/RasmusGodske/claude-hook-utils",
    "source": "ankitg12",
    "published_at": "2026-05-29T04:18:34+00:00",
    "summary": "",
    "points": 18,
    "comments": 2
  },
  {
    "id": "hn:48187727",
    "platform": "hackernews",
    "title": "AgentCRM – Headless CRM for Claude Code",
    "url": "https://github.com/cluster-software/agent-crm",
    "source": "samuelstros",
    "published_at": "2026-05-19T00:23:16+00:00",
    "summary": "",
    "points": 17,
    "comments": 0
  },
  {
    "id": "hn:48281066",
    "platform": "hackernews",
    "title": "Show HN: MCPs aren't enough, give Codex/Claude accurate memory of everything",
    "url": "https://timeglass.ai",
    "source": "midas",
    "published_at": "2026-05-26T15:23:38+00:00",
    "summary": "",
    "points": 16,
    "comments": 2
  },
  {
    "id": "hn:48322956",
    "platform": "hackernews",
    "title": "Show HN: AISlop, a CLI for catching AI generated code smells",
    "url": "https://github.com/scanaislop/aislop",
    "source": "Heavykenny",
    "published_at": "2026-05-29T13:37:38+00:00",
    "summary": "",
    "points": 73,
    "comments": 64
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
    "id": "hn:48188727",
    "platform": "hackernews",
    "title": "Sieve – scans Cursor/Claude chat history for leaked API keys",
    "url": "https://apps.apple.com/us/app/sieve-secret-scanner/id6767409365?mt=12",
    "source": "helpful_human",
    "published_at": "2026-05-19T03:06:45+00:00",
    "summary": "",
    "points": 18,
    "comments": 3
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
    "id": "hn:48287025",
    "platform": "hackernews",
    "title": "Uber blows through its AI budget in 1 quarter",
    "url": "https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/",
    "source": "ChuckMcM",
    "published_at": "2026-05-26T22:44:31+00:00",
    "summary": "",
    "points": 28,
    "comments": 34
  },
  {
    "id": "hn:48345028",
    "platform": "hackernews",
    "title": "With Claude: Less Coding, More Testing",
    "url": "https://henrikwarne.com/2026/05/31/with-claude-less-coding-more-testing/",
    "source": "ingve",
    "published_at": "2026-05-31T11:56:54+00:00",
    "summary": "",
    "points": 25,
    "comments": 3
  },
  {
    "id": "hn:48324078",
    "platform": "hackernews",
    "title": "Claude Opus 4.8 distilled Alibaba Qwen models",
    "url": "https://twitter.com/maxforai/status/2060053228566495410",
    "source": "simjnd",
    "published_at": "2026-05-29T15:10:18+00:00",
    "summary": "",
    "points": 20,
    "comments": 7
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
    "id": "hn:48196479",
    "platform": "hackernews",
    "title": "Cursor Cloud Agents Down",
    "url": "https://forum.cursor.com/t/cloud-agents-broken-ii/161036",
    "source": "mopatches",
    "published_at": "2026-05-19T17:37:19+00:00",
    "summary": "",
    "points": 21,
    "comments": 3
  },
  {
    "id": "hn:48182126",
    "platform": "hackernews",
    "title": "Composer 2.5",
    "url": "https://cursor.com/blog/composer-2-5",
    "source": "meetpateltech",
    "published_at": "2026-05-18T16:46:56+00:00",
    "summary": "",
    "points": 18,
    "comments": 3
  },
  {
    "id": "hn:48308376",
    "platform": "hackernews",
    "title": "Show HN: Continue? Y/N: A 60-second game about AI agent permission fatigue",
    "url": "https://llmgame.scalex.dev",
    "source": "Wirbelwind",
    "published_at": "2026-05-28T13:02:00+00:00",
    "summary": "",
    "points": 384,
    "comments": 159
  },
  {
    "id": "hn:48326659",
    "platform": "hackernews",
    "title": "Robinhood now lets your AI agents trade stocks",
    "url": "https://techcrunch.com/2026/05/27/robinhood-now-lets-your-ai-agents-trade-stocks/",
    "source": "wapasta",
    "published_at": "2026-05-29T17:46:27+00:00",
    "summary": "",
    "points": 110,
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
    "comments": 68
  },
  {
    "id": "hn:48319968",
    "platform": "hackernews",
    "title": "Undisclosed addition in jqwik instructed AI coding agents to delete app output",
    "url": "https://arstechnica.com/security/2026/05/fed-up-with-vibe-coders-dev-sneaks-data-nuking-prompt-injection-into-their-code/",
    "source": "joozio",
    "published_at": "2026-05-29T07:05:31+00:00",
    "summary": "",
    "points": 63,
    "comments": 1
  },
  {
    "id": "hn:48294315",
    "platform": "hackernews",
    "title": "Why AI Agents Cannot Change Software Systems",
    "url": "https://phroneses.com/articles/build/notes/agents-cannot-maintain-systems.html",
    "source": "jhevans",
    "published_at": "2026-05-27T13:46:38+00:00",
    "summary": "",
    "points": 46,
    "comments": 39
  },
  {
    "id": "hn:48315016",
    "platform": "hackernews",
    "title": "Show HN: Open Envelope – an open schema for defining AI agent teams",
    "url": "https://openenvelope.org/docs/schema/",
    "source": "ashconway",
    "published_at": "2026-05-28T20:30:20+00:00",
    "summary": "",
    "points": 46,
    "comments": 9
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
    "points": 99,
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
    "points": 103,
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
    "points": 65,
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
    "points": 44,
    "comments": 71
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
    "id": "hn:47993235",
    "platform": "hackernews",
    "title": "Kimi K2.6 just beat Claude, GPT-5.5, and Gemini in a coding challenge",
    "url": "https://thinkpol.ca/2026/04/30/an-open-weights-chinese-model-just-beat-claude-gpt-5-5-and-gemini-in-a-programming-challenge/",
    "source": "bazlightyear",
    "published_at": "2026-05-03T04:05:28+00:00",
    "summary": "",
    "points": 380,
    "comments": 219
  },
  {
    "id": "hn:48057209",
    "platform": "hackernews",
    "title": "GPT-5.5 Price Increase: What It Costs",
    "url": "https://openrouter.ai/announcements/gpt55-cost-analysis",
    "source": "gmays",
    "published_at": "2026-05-08T01:02:28+00:00",
    "summary": "",
    "points": 214,
    "comments": 73
  },
  {
    "id": "hn:48025274",
    "platform": "hackernews",
    "title": "GPT‑5.5 Instant",
    "url": "https://openai.com/index/gpt-5-5-instant/",
    "source": "meetpateltech",
    "published_at": "2026-05-05T17:02:23+00:00",
    "summary": "",
    "points": 87,
    "comments": 20
  },
  {
    "id": "hn:48234090",
    "platform": "hackernews",
    "title": "Antigravity 2.0 Tops the OpenSCAD Architectural 3D LLM Benchmark",
    "url": "https://modelrift.com/blog/openscad-llm-benchmark/",
    "source": "jetter",
    "published_at": "2026-05-22T10:38:26+00:00",
    "summary": "",
    "points": 421,
    "comments": 161
  },
  {
    "id": "hn:48180438",
    "platform": "hackernews",
    "title": "The Rage of the Billionaires Is Coming",
    "url": "https://www.thebignewsletter.com/p/monopoly-round-up-the-rage-of-the",
    "source": "aworks",
    "published_at": "2026-05-18T14:31:01+00:00",
    "summary": "",
    "points": 38,
    "comments": 24
  },
  {
    "id": "hn:48199756",
    "platform": "hackernews",
    "title": "Raven Software's Jedi Academy sources, from 2013, had all the crunch rage intact",
    "url": "https://old.reddit.com/r/programming/comments/1thewau/raven_software_released_the_jedi_academy_source/",
    "source": "perching_aix",
    "published_at": "2026-05-19T21:15:03+00:00",
    "summary": "",
    "points": 10,
    "comments": 1
  },
  {
    "id": "hn:48330436",
    "platform": "hackernews",
    "title": "MCP is dead?",
    "url": "https://www.quandri.io/engineering-blog/mcp-is-dead",
    "source": "nadis",
    "published_at": "2026-05-29T22:56:49+00:00",
    "summary": "",
    "points": 398,
    "comments": 402
  },
  {
    "id": "hn:48194352",
    "platform": "hackernews",
    "title": "I’ve joined Anthropic",
    "url": "https://twitter.com/karpathy/status/2056753169888334312",
    "source": "dmarcos",
    "published_at": "2026-05-19T15:07:45+00:00",
    "summary": "",
    "points": 1430,
    "comments": 617
  },
  {
    "id": "hn:48296794",
    "platform": "hackernews",
    "title": "I think Anthropic and OpenAI have found product-market fit",
    "url": "https://simonwillison.net/2026/May/27/product-market-fit/",
    "source": "simonw",
    "published_at": "2026-05-27T16:39:13+00:00",
    "summary": "",
    "points": 1089,
    "comments": 1242
  },
  {
    "id": "hn:48182281",
    "platform": "hackernews",
    "title": "Anthropic acquires Stainless",
    "url": "https://www.anthropic.com/news/anthropic-acquires-stainless",
    "source": "tomeraberbach",
    "published_at": "2026-05-18T17:01:21+00:00",
    "summary": "",
    "points": 531,
    "comments": 382
  },
  {
    "id": "hn:48336233",
    "platform": "hackernews",
    "title": "Anthropic surpasses OpenAI to become most valuable AI startup",
    "url": "https://qazinform.com/news/anthropic-surpasses-openai-to-become-worlds-most-valuable-ai-startup",
    "source": "Bolat14",
    "published_at": "2026-05-30T13:56:34+00:00",
    "summary": "",
    "points": 419,
    "comments": 471
  },
  {
    "id": "hn:48313048",
    "platform": "hackernews",
    "title": "Anthropic raises $65B in Series H funding at $965B post-money valuation",
    "url": "https://www.anthropic.com/news/series-h",
    "source": "meetpateltech",
    "published_at": "2026-05-28T18:09:44+00:00",
    "summary": "",
    "points": 362,
    "comments": 428
  },
  {
    "id": "hn:48214017",
    "platform": "hackernews",
    "title": "Anthropic is expanding to Colossus2. Will use GB200",
    "url": "https://twitter.com/nottombrown/status/2057194829986300375",
    "source": "aurareturn",
    "published_at": "2026-05-20T20:55:52+00:00",
    "summary": "",
    "points": 307,
    "comments": 351
  },
  {
    "id": "hn:48193111",
    "platform": "hackernews",
    "title": "Anthropic Is Preparing for IPO and We Should Be Worried",
    "url": "https://www.vincentschmalbach.com/anthropic-ipo-developers-should-be-worried-v2/",
    "source": "vincent_s",
    "published_at": "2026-05-19T13:30:58+00:00",
    "summary": "",
    "points": 89,
    "comments": 96
  },
  {
    "id": "hn:48270497",
    "platform": "hackernews",
    "title": "Anthropic Cofounder Chris Olah's Remarks on Pope Leo XIV's \"Magnifica Humanitas\"",
    "url": "https://www.anthropic.com/news/chris-olah-pope-leo-encyclical",
    "source": "Philpax",
    "published_at": "2026-05-25T19:12:29+00:00",
    "summary": "",
    "points": 87,
    "comments": 99
  },
  {
    "id": "hn:48311647",
    "platform": "hackernews",
    "title": "Claude Opus 4.8",
    "url": "https://www.anthropic.com/news/claude-opus-4-8",
    "source": "craigmart",
    "published_at": "2026-05-28T16:49:14+00:00",
    "summary": "",
    "points": 1762,
    "comments": 1366
  },
  {
    "id": "hn:48240419",
    "platform": "hackernews",
    "title": "Project Glasswing: An Initial Update",
    "url": "https://www.anthropic.com/research/glasswing-initial-update",
    "source": "louiereederson",
    "published_at": "2026-05-22T19:31:45+00:00",
    "summary": "",
    "points": 561,
    "comments": 325
  },
  {
    "id": "bvid:BV1quVd6DEw3",
    "platform": "bilibili",
    "title": "B站讲的最好的 Claude Code保姆级入门到实战教程，从安装到使用原理到Claude案例实战（国内直连），零基础也能秒上手，让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116673742901660",
    "source": "java面试题",
    "published_at": "2026-06-01T08:10:17+00:00",
    "summary": "一个冷知识：点赞是免费的！但是可以让辛苦做视频的UP主开心快乐一整天！！！\n\n视频配套笔记；https://www.bilibili.com/read/cv43135702/?",
    "duration_sec": 33293,
    "views": 1175,
    "matched_keywords": [
      "Claude Code 实战"
    ]
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
    "views": 164054,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1HqV969EcU",
    "platform": "bilibili",
    "title": "10分钟快速入门Claude Code保姆级安装到代码实战教程",
    "url": "http://www.bilibili.com/video/av116672333616934",
    "source": "字节测试工程师",
    "published_at": "2026-06-01T01:53:10+00:00",
    "summary": "勉费领取视频全套资料/文档/学习笔记点击→https://www.bilibili.com/read/cv38114879/?jump_opus=1",
    "duration_sec": 4965,
    "views": 3751,
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
    "views": 13533,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1x6Vt6dEef",
    "platform": "bilibili",
    "title": "100 小时测试 Claude Code vs Codex（真实结果）",
    "url": "http://www.bilibili.com/video/av116656495925868",
    "source": "设计之道",
    "published_at": "2026-05-29T06:44:49+00:00",
    "summary": "【海外 AI 订阅】\n国内直连，支付宝付款，不用代理，\n一站订阅 ChatGPT / Codex / Claude Code / X\n订阅链接：https://bewild.ai?code=SJZD\n订阅时请填优惠邀请码：SJZD，具体优惠金额以官网为准。\n\n【视频介绍】\n我花了 100 个小时测试 Claude Code 和 Codex，结果真的让我非常意外。\n相同的提示词、相同的项目构建、两个工具并排测试，而其中一个工具的表现远超我的预期。\n如果你现在正在这类 AI 编程 Agent 之间做选择，那么",
    "duration_sec": 1597,
    "views": 4157,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1fyVY6tE6y",
    "platform": "bilibili",
    "title": "Ultracode：Claude Code这次真的把“工程团队”塞进了一个命令里",
    "url": "http://www.bilibili.com/video/av116659683595894",
    "source": "MIP耀",
    "published_at": "2026-05-29T20:15:59+00:00",
    "summary": "5 月 28 日,Claude Code 上线了一个新功能——Ultracode。\n它让 Claude 自己决定要不要拆任务、起几十上百个子代理并发执行、\n然后自己验证结果——你只敲一个命令。\n \nAnthropic 给的标杆案例:Bun 运行时从 Zig 移植到 Rust,\n75 万行代码、11 天、99.8% 测试通过。\n \n但这条视频不只是讲&quot;哇好牛&quot;——而是想拆解一件事:\n为什么 Ultracode 不是 Claude Code 的下一个功能,\n而是过去一年所有更新的合体形态。",
    "duration_sec": 389,
    "views": 885,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1vPVJ6EEYM",
    "platform": "bilibili",
    "title": "【2026最新版】Claude Code教程，从入门到精通，搞定所有开发场景，小白轻松搞定，全程干货无废话，存下吧，很难找全的！",
    "url": "http://www.bilibili.com/video/av116666780353563",
    "source": "居然说AI",
    "published_at": "2026-05-31T02:24:09+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！",
    "duration_sec": 15977,
    "views": 4114,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1sJVL6QEzR",
    "platform": "bilibili",
    "title": "Claude Code 动态工作流实战指南",
    "url": "http://www.bilibili.com/video/av116664867755402",
    "source": "凌云_API",
    "published_at": "2026-05-30T18:18:16+00:00",
    "summary": "原视频链接：https://www.youtube.com/watch?v=jZgcWCzxh1I\n本视频为Ai技术搬运翻译，使用AI智能移除原视频广告营销内容，旨在降低信息差，帮助大家了解海外最新Ai动态\n翻译：凌云API模型gemini-3-flash-preview\nAI实用工具看下面：\n1、凌云AI平台：yunai.chat，国内可直接调用全球500+AI大模型API，支持Gemini、GPT、Claude等最新模型\n2、低价稳定大流量云服务器推荐：https://www.rainyun.com/",
    "duration_sec": 1702,
    "views": 298,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1JUGb6jEny",
    "platform": "bilibili",
    "title": "90% 的人都没用对 Claude Code，Claude Code 的高阶玩法都在这",
    "url": "http://www.bilibili.com/video/av116618998912532",
    "source": "程序员Shark",
    "published_at": "2026-05-22T15:46:55+00:00",
    "summary": "为了做了精心的翻译和校对，原文：https://www.youtube.com/watch?v=uogzSxOw4LU，再次感谢作者。\n概要：这部分内容真正想讲的，不是 Claude Code 又多了几个新功能，而是怎么把它用成一套顺手的开发工具。很多人一开始只是拿它来聊天，但真想把效率拉起来，重点其实在\n setup、命令、扩展能力和工作流设计。前面先讲了几个特别常用的 command：model 用来按任务切换不同 model，别什么事都一直开最贵的；insights\n 可以帮你回看自己平时是怎么用",
    "duration_sec": 2299,
    "views": 2238,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1L9VZ6bE2r",
    "platform": "bilibili",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！！",
    "url": "http://www.bilibili.com/video/av116673893893645",
    "source": "马小洋qwer",
    "published_at": "2026-06-01T08:30:19+00:00",
    "summary": "视频制作不易，如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托~这对我真的很重要！",
    "duration_sec": 53187,
    "views": 499,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1zNVd6WEGQ",
    "platform": "bilibili",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你企业级电商项目 Harness AI 工程化编程实战！",
    "url": "http://www.bilibili.com/video/av116673793233265",
    "source": "图灵官方视频号",
    "published_at": "2026-06-01T08:24:34+00:00",
    "summary": "喜欢UP主发的视频记得一键3连支持一波噢，你的支持，是我最大的动力！\n视频配套笔记、简历模板、面经都在这了：https://www.bilibili.com/read/cv41607246/?jump_opus=1\n还可领取2026年Java面试题总结与最新2025版Java 技术栈学习路线脑图。",
    "duration_sec": 8660,
    "views": 85,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1j2Lw6CEyQ",
    "platform": "bilibili",
    "title": "Hermes Agent + Claude Code 互联：把 AI 升级成 7x24 全知员工",
    "url": "http://www.bilibili.com/video/av116594822876107",
    "source": "星小脉",
    "published_at": "2026-05-18T09:26:55+00:00",
    "summary": "Jack Roberts 演示如何把 Hermes Agent（Nous Research）与 Claude Code Operating System 互联，打造跨平台共享记忆的 AI 智能系统。完整覆盖：Hermes 安装（Telegram bot 配置 + 用户授权）、Pantheon 自定义 AI 人格（Labyrinth/Mercury/Philosopher）、GitHub 仓库镜像备份、Obsidian Vault 知识库连接、Claude OS Bridge 数据互通、Apollo lea",
    "duration_sec": 3368,
    "views": 1044,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV16FVd6oE5F",
    "platform": "bilibili",
    "title": "5分钟安装ClaudeCode并接入DeepSeek，手把手教你在Claude Code中熟练使用SKILLS技能！",
    "url": "http://www.bilibili.com/video/av116673642234395",
    "source": "字节测试员",
    "published_at": "2026-06-01T07:33:29+00:00",
    "summary": "勉费领取视频全套资料/文档/学习笔记点击：https://www.bilibili.com/opus/1043733334236069896",
    "duration_sec": 15248,
    "views": 1278,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1Nm5L64E2Q",
    "platform": "bilibili",
    "title": "Warp 终端实测体验，一键 cc 快速启动 Claude Code✨",
    "url": "http://www.bilibili.com/video/av116549188851891",
    "source": "大强同学_",
    "published_at": "2026-05-10T07:55:33+00:00",
    "summary": "",
    "duration_sec": 354,
    "views": 2830,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1s8V96bEFS",
    "platform": "bilibili",
    "title": "（比刷剧爽！）2026公认最好的《Claude Code》教程，附课件代码—Claude Code探索-测试-重构-调试代码库",
    "url": "http://www.bilibili.com/video/av116672753047771",
    "source": "AI学习日记",
    "published_at": "2026-06-01T03:43:19+00:00",
    "summary": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码-----ClaudeCode【配套课程笔记+代码文件】+进阶学习路线-可以在我的gong.粽.号.【辅论AI】发送【333】无偿自取就行哦~",
    "duration_sec": 6174,
    "views": 173,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1mdGR6iEoH",
    "platform": "bilibili",
    "title": "Code with Claude 2026 | London 2026",
    "url": "http://www.bilibili.com/video/av116634450657952",
    "source": "DesyncInfoSec",
    "published_at": "2026-05-25T09:22:07+00:00",
    "summary": "https://claude.com/code-with-claude/london\nCode with Claude 2026 是 Anthropic 面向开发者举办的年度 AI 编程大会，聚焦 Claude Code、Agentic Coding、MCP 生态以及 AI 原生软件开发实践。大会包含主题演讲、实战 Workshop、最新能力演示，以及与 Anthropic 工程团队的技术交流，重点探讨 AI Agent 如何改变软件开发、自动化协作与未来工程模式。2026 伦敦站汇聚了大量开发者、创业团",
    "duration_sec": 41860,
    "views": 814,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV19NRSBeEQi",
    "platform": "bilibili",
    "title": "把 Claude Code 放进 Unity",
    "url": "http://www.bilibili.com/video/av116540850571812",
    "source": "郎曦nink",
    "published_at": "2026-05-08T20:31:41+00:00",
    "summary": "MCP插件仓库地址：https://github.com/CoplayDev/unity-mcp\n我制作的插件的仓库地址：https://github.com/ninkjin/Claude-Code-Terminal-for-Unity\n在unity中add git url 的这个插件地址：https://github.com/ninkjin/Claude-Code-Terminal-for-Unity.git#upm",
    "duration_sec": 303,
    "views": 1777,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1nEVn6ZEcB",
    "platform": "bilibili",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116667770279060",
    "source": "AI探索喵",
    "published_at": "2026-05-31T06:39:47+00:00",
    "summary": "",
    "duration_sec": 23519,
    "views": 873,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1hB5K6rESX",
    "platform": "bilibili",
    "title": "用 Claude Code 改 WordPress 站点：WP-CLI + MCP + Novamira 实战",
    "url": "http://www.bilibili.com/video/av116559288737600",
    "source": "星小脉",
    "published_at": "2026-05-12T02:52:34+00:00",
    "summary": "ByteGrad 的 35 分钟实战课：用 Claude Code 接管 WordPress 网站运维。三种接入方式——直接改文件、WP-CLI 终端命令、MCP server（Novamira 是当下最火的 MCP）。一句话装 WP Rocket、改首页标题、做完整性能审计；甚至让 Claude Code 调用浏览器做 Lighthouse 审计 + 自动调参 + 前后对比，主动避开 &quot;移除未使用 CSS&quot; 这种会搞砸 Elementor 布局的边缘坑。CLAUDE.md / AGENTS.md / 1",
    "duration_sec": 3743,
    "views": 246,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1HYV964Erb",
    "platform": "bilibili",
    "title": "Claude Code 工作流详解：别把词元和额度烧光",
    "url": "http://www.bilibili.com/video/av116672652379307",
    "source": "AI_Express",
    "published_at": "2026-06-01T03:17:49+00:00",
    "summary": "这期围绕 Claude Code 的 dynamic workflow 做一次实测拆解：作者让工作流分析 41 个 skills，系统并行启动 41 个 Haiku 评分智能体，再交给 Opus 综合智能体汇总，最后生成一个按质量排序的 HTML 报告，并给出可改进的反馈。视频重点不是炫功能，而是讲清它和 skills、子智能体、Agent Team、/goal 的边界：谁负责持有计划，智能体之间能不能沟通，结果如何合并，以及为什么并行看起来很快却可能消耗数百万输入词元。适合正在用 Claude Code",
    "duration_sec": 1986,
    "views": 229,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1HeV96dEu7",
    "platform": "bilibili",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116672702711316",
    "source": "IT界的泥石流1",
    "published_at": "2026-06-01T03:28:45+00:00",
    "summary": "",
    "duration_sec": 9462,
    "views": 806,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV16GV86XEPa",
    "platform": "bilibili",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116655757723840",
    "source": "刘十二-是我啊",
    "published_at": "2026-05-29T03:42:21+00:00",
    "summary": "喜欢请三连哦   喜欢请三连哦   喜欢请三连哦   喜欢请三连哦   喜欢请三连哦   喜欢请三连哦   喜欢请三连哦",
    "duration_sec": 8715,
    "views": 3491,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV13cVf69EQC",
    "platform": "bilibili",
    "title": "【Cursor教程】史上最强 AI 编程工具免费啦！Cursor保姆级使用教程！教你用AI每次都写出完美的Python代码，从此再无报错！从入门到实战全套指南！",
    "url": "http://www.bilibili.com/video/av116674011335233",
    "source": "Python蒲公英",
    "published_at": "2026-06-01T08:58:00+00:00",
    "summary": "",
    "duration_sec": 538,
    "views": 58,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1ZSVG6eE3V",
    "platform": "bilibili",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116662284130312",
    "source": "非六于期",
    "published_at": "2026-05-30T07:13:36+00:00",
    "summary": "",
    "duration_sec": 1068,
    "views": 2075,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1wuLHzDEGA",
    "platform": "bilibili",
    "title": "【Godot&amp;Cursor】0.亲测一个月后，我选择Godot+Cursor组合做独立游戏",
    "url": "http://www.bilibili.com/video/av114398869853632",
    "source": "破妄-胖",
    "published_at": "2025-04-25T13:43:22+00:00",
    "summary": "飞书文档：https://sh67ozct1z.feishu.cn/docx/Hn5jd0cE6op1Sux9RrFcl8Npnbd",
    "duration_sec": 184,
    "views": 13436,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1f5DvB4Eoa",
    "platform": "bilibili",
    "title": "AI 直接操控 Cocos Creator！78 个自动化工具一键搞定场景搭建 让 AI 接管你的 Cocos Creator 编辑器 | Link CC MC",
    "url": "http://www.bilibili.com/video/av116362978528338",
    "source": "一个凡人鸭",
    "published_at": "2026-04-07T10:40:52+00:00",
    "summary": "让 AI 直接操控 Cocos Creator 编辑器！\nLink CC MCP 是一款 AI 驱动的 Cocos Creator 编辑器自动化插件，通过 MCP 协议连接 Cursor 等 AI 编辑器，提供 78 个编辑器操作工具。\n你可以用自然语言让 AI：\n✦ 创建节点、搭建 UI 层级\n✦ 添加/修改组件、绑定脚本\n✦ 管理场景、资源、预制体\n✦ 截图查看场景效果\n✦ 批量操作、动画生成\n✦ 一句话完成原本需要手动操作几十步的工作\n支持 Cocos Creator 3.8.6+，兼容 Curso",
    "duration_sec": 930,
    "views": 5017,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "platform": "bilibili",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards",
    "duration_sec": 863,
    "views": 6323,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1oUVc6vEEY",
    "platform": "bilibili",
    "title": "【2026最新】B站最全最细的 AI 编程工具Cursor保姆级教程！Cursor保姆级安装使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116639383159883",
    "source": "AI大模型教学",
    "published_at": "2026-05-26T06:24:36+00:00",
    "summary": "",
    "duration_sec": 22258,
    "views": 6352,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1XAVf6pExZ",
    "platform": "bilibili",
    "title": "【保姆级教程】史上最强AI编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116673994691797",
    "source": "人工补智能体的皮皮",
    "published_at": "2026-06-01T09:26:29+00:00",
    "summary": "",
    "duration_sec": 11087,
    "views": 57,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "platform": "bilibili",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor/Claude Code/Codex/Copilot/Windsurf/Kiro/Zed/Antigravit",
    "duration_sec": 1451,
    "views": 308073,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV12NVR6vEyL",
    "platform": "bilibili",
    "title": "AI编程 Cursor 1小时开发一个微信小程序个人健康管理系统(带AI智能客服功能) Spring AI2，SpringBoot4后端 Vue3后台管理前端",
    "url": "http://www.bilibili.com/video/av116672098862714",
    "source": "java1234官方",
    "published_at": "2026-06-01T00:51:43+00:00",
    "summary": "手把手教大家 用 AI编程 Cursor 1小时开发一个微信小程序个人健康管理系统(带AI智能客服功能) Spring AI2.0 SpringBoot4后端 Vue3后台管理前端 ，包括Plan需求设计，Agent实现项目，BUG，缺陷修复技巧等。",
    "duration_sec": 2293,
    "views": 575,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1qyAqzZEGg",
    "platform": "bilibili",
    "title": "【Cursor教程】Cursor 保姆级使用教程！教你用AI每次都写出完美的Python代码，再无报错！从入门到实战全套指南，零基础小白也能学会！",
    "url": "http://www.bilibili.com/video/av116151468165209",
    "source": "不要花生碎",
    "published_at": "2026-03-01T02:07:52+00:00",
    "summary": "",
    "duration_sec": 911,
    "views": 435,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV12NK1zMESx",
    "platform": "bilibili",
    "title": "如何用Cursor开发大项目，全流程讲解，干货十足",
    "url": "http://www.bilibili.com/video/av114758657246726",
    "source": "AI随风随风",
    "published_at": "2025-06-28T02:37:22+00:00",
    "summary": "视频主题&amp;项目背景\n主题： 分享个人如何使用cursor 从0到1开发一个比较大的项目，使用的技术栈是vue+小程序+java\n项目\n一个B2B的订货商城及供应链全流程管理，包含的端有：\n小程序商城端\n供应商端\n仓储物流端\n司机配送端\n销售端\n后台管理系统\n以上小程序端都是使用webview的方式\n核心功能：\n商城的基本功能: 正逆向订单、商品、购物车、优惠券、积分、钱包、充值、工单等\n供应链的基本功能：采购、仓储出入库，司机配送（仓库功能比较简单，只是一个中转仓功能）\n供应商基本功能：上品、财务核算、送",
    "duration_sec": 2358,
    "views": 57499,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1XdFzz7Ei8",
    "platform": "bilibili",
    "title": "不写代码就能轻松开发应用？Cursor+Gemini 超强指挥官工作法！",
    "url": "http://www.bilibili.com/video/av116021511853604",
    "source": "PM刘搞定",
    "published_at": "2026-02-06T03:17:18+00:00",
    "summary": "如何像传统互联网大厂一样指挥AI干活？本期视频通过一个“个人工作台”的实战项目，拆解了一套利用 LLM (Gemini) 辅助 Cursor 开发的高效工作流。\n\n核心内容：\n角色转换：你不是程序员，你是产品经理（PM）。\n文档驱动：如何用 AI 生成标准的产品文档 (PRD)、UI 文档和技术方案。\n避坑指南：如何防止 Cursor “手搓核弹”或开发中途“失忆”。\n\n实操流程：\nStep 1：愿望清单与草图绘制\nStep 2-4：利用大模型生成三件套文档 (PRD/UI/Tech)\nStep 5-6：",
    "duration_sec": 1079,
    "views": 55722,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1QzuRz2Epz",
    "platform": "bilibili",
    "title": "【中文】Cursor AI Unity 教程：新手指南，简单易懂 ｜ Nikhil Malankar",
    "url": "http://www.bilibili.com/video/av114879017000489",
    "source": "CursorInsider",
    "published_at": "2025-07-19T13:00:00+00:00",
    "summary": "在本视频中，我将带你逐步完成 Cursor AI 在 Unity 中的完整设置和配置，帮助你利用 AI 驱动的代码辅助功能，加速你的游戏开发流程。无论你是正在构建一个新项目，还是将 AI 集成到现有的 Unity 游戏中，本教程都涵盖了你所需的一切。\n\n🔧 你将学到：\n✔️ 如何在 Unity 中安装和配置 Cursor AI\n✔️ 设置 Cursor AI 扩展以实现无缝开发\n✔️ 使用 AI 建议在 Unity 中编写高效的 C# 脚本\n✔️ 利用 AI 工具增强 Unity 编辑器的生产力\n✔️ 关",
    "duration_sec": 931,
    "views": 17165,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1spGC68ECh",
    "platform": "bilibili",
    "title": "Claude Code vs Cursor vs Codex：AI 编程工具到底该怎么选？",
    "url": "http://www.bilibili.com/video/av116644181447025",
    "source": "小牛AI_XNAI",
    "published_at": "2026-05-27T02:33:20+00:00",
    "summary": "市面上的 AI 编程工具琳琅满目，Claude Code、Cursor 和 Codex 到底有什么本质区别？这期视频不聊枯燥的参数对比，而是带你深入拆解这些工具背后的设计理念与核心差异。无论你是已经有心仪工具的开发者，还是正在寻找提效方案的程序员，通过这期深度剖析，你将更清晰地了解哪种方案最适合你的工作流。拒绝盲目跟风，带你从底层逻辑看清 AI 编程工具的真实面貌。",
    "duration_sec": 1791,
    "views": 2758,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1QH5n6UEVe",
    "platform": "bilibili",
    "title": "保姆级Claude code+Cursor+DeepSeek-V4-pro 实现AI自动编程",
    "url": "http://www.bilibili.com/video/av116550547803032",
    "source": "cmasj",
    "published_at": "2026-05-10T13:55:05+00:00",
    "summary": "Claude code+Cursor+DeepSeek-V4-pro 实现AI自动编程，整体流程环境搭建",
    "duration_sec": 374,
    "views": 1931,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "platform": "bilibili",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型",
    "duration_sec": 484,
    "views": 33194,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1jRD7BTEgk",
    "platform": "bilibili",
    "title": "Figma + Cursor AI 高效开发指南：零基础快速构建商业级移动应用 | Cursor AI / Firebase / 身份验证 / 营养大师APP",
    "url": "http://www.bilibili.com/video/av116369337160878",
    "source": "赛博门外憨",
    "published_at": "2026-04-09T00:00:00+00:00",
    "summary": "本课程旨在通过 AI 赋能的开发工作流，彻底改变传统的移动应用构建方式。你将学习如何利用 Figma AI 进行高效 UI 设计，并结合 Cursor AI 将设计稿快速转化为功能完备的 Flutter 应用程序。这不仅是一门技术课程，更是一场关于“AI 先行”开发思维的实战演练，无论你是零基础入门者、产品创始人还是设计师，都能通过本课程掌握从创意构思到产品落地的全链路开发能力。\n\n【你将学到的内容清单】\n\n1. AI 驱动的 UI 设计流程：学习如何利用 Figma AI 快速生成现代化的移动应用界面，",
    "duration_sec": 8864,
    "views": 2924,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "platform": "bilibili",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库环境的安装\n2.创建数据库和数据表\n3.利用本地数据库实现注册与登录\n\n***你也可以直接购买包含9课时的完整",
    "duration_sec": 549,
    "views": 6945,
    "matched_keywords": [
      "Cursor AI 编程"
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
    "views": 4814,
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
    "views": 81789,
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
    "views": 149384,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1iKVd6XESo",
    "platform": "bilibili",
    "title": "零基础速冲！Vibe Coding全流程保姆级教程，手把手带你使用Stitch+AI Studio+Antigravity从0到上线搭建项目，小白也能轻松上手！",
    "url": "http://www.bilibili.com/video/av116673843563264",
    "source": "AI大模型入门阿坤",
    "published_at": "2026-06-01T08:13:13+00:00",
    "summary": "零基础速冲！Vibe Coding全流程保姆级教程，手把手带你使用Stitch+AI Studio+Antigravity从0到上线搭建项目，小白也能轻松上手！",
    "duration_sec": 1185,
    "views": 43,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1oNVH6xEWS",
    "platform": "bilibili",
    "title": "Claude Code 国内直连保姆级教程｜10分钟从入门到精通，原理+安装+实战全覆盖，解锁Vibe Coding编程新范式",
    "url": "http://www.bilibili.com/video/av116667602503393",
    "source": "码士集团-小晨晨晨",
    "published_at": "2026-05-31T06:14:34+00:00",
    "summary": "",
    "duration_sec": 18347,
    "views": 9397,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1cCVZ6NEym",
    "platform": "bilibili",
    "title": "这绝对是B站讲的最全最细的VibeCoding系统教程，手把手带你从环境安装到实战，包含所有干货！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116673944492771",
    "source": "峰识在大模型",
    "published_at": "2026-06-01T08:53:14+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n本视频配套课件笔记代码/学习大纲/大模型学习路线戳这里获取→https://www.bilibili.com/opus/1195847460814061571?spm_id_from=333.1387.0.0\n另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景题移步评论置顶即可~",
    "duration_sec": 53487,
    "views": 195,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1vhVn6SEuk",
    "platform": "bilibili",
    "title": "【2026最新】绝对是B站No.1的Claude Code教程：国内安装+实战开发案例+个人使用心得总结，手把手带你拥抱Vibe Coding！",
    "url": "http://www.bilibili.com/video/av116667904561472",
    "source": "杨淑娟Python",
    "published_at": "2026-05-31T07:14:54+00:00",
    "summary": "绝对是B站No.1的Claude Code教程：国内安装+实战开发案例+个人使用心得总结，手把手带你拥抱Vibe Coding！\n配套课件笔记/PPT已备好，另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景题移步评论置顶即可~\n\ncodex+hermes+claude code 从0到1全讲明白",
    "duration_sec": 33757,
    "views": 920,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "platform": "bilibili",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "published_at": "2026-01-11T15:43:58+00:00",
    "summary": "🚀开发者必看！Superpowers把专业工程团队方法论固化成Skills，让Claude Code告别越写越乱的困境：规格驱动+代码质量双重保障！AI编程新范式！头脑风暴+计划+执行一条龙自动化\n\n\n🚀🚀🚀 视频简介：\n🎬 本期视频详细演示了开源AI编程工作流系统Superpowers的完整使用方法，并通过开发一款iOS时间线笔记原生应用来实测其效果。\n🔧 核心内容：\nSuperpowers工作流介绍：告别Vibe Coding，拥抱工程化开发方法论\n支持Claude Code、OpenAI Codex",
    "duration_sec": 758,
    "views": 130212,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1cwVG6qEEW",
    "platform": "bilibili",
    "title": "【硬核教程】如何让一个J人红温？只需要给他做这份“发疯版NBTI”...",
    "url": "http://www.bilibili.com/video/av116662737048980",
    "source": "GenJi是真想教会你",
    "published_at": "2026-05-30T10:00:00+00:00",
    "summary": "NBTI测试链接：https://www.starkawaii.top/\n\n还在因为MBTI不是J人被面试官拒绝？别再掉进这个当代职场大坑了！\n本期视频，我用 Claude Code手搓了一个专属打工人的“NBTI”发疯测试！同时找来三位不同岗位的小伙伴，记录他们一周的工作实况，来验证测验的准确性。\n还有满满干货，三个步骤沉浸式拆解Vibe Coding全流程，视频同款测试链接+网页搭建详细教程已放在评论区，快来测测你是什么职场人格吧，记得三连哦！",
    "duration_sec": 549,
    "views": 641772,
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
    "views": 50817,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV14pVJ6KEoG",
    "platform": "bilibili",
    "title": "Vibe Coding全栈开发实战体系课（B站高分课程）",
    "url": "http://www.bilibili.com/video/av116666579032769",
    "source": "西瓜讲大模型",
    "published_at": "2026-05-31T01:29:24+00:00",
    "summary": "项目驱动是最快的学习方式！",
    "duration_sec": 761,
    "views": 610,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1NBV56DEBA",
    "platform": "bilibili",
    "title": "Codex依赖症重症患者采访",
    "url": "http://www.bilibili.com/video/av116665119479370",
    "source": "AIwood爱屋研究室",
    "published_at": "2026-05-31T01:30:00+00:00",
    "summary": "剧情纯属虚构，如有雷同，算你NB！",
    "duration_sec": 106,
    "views": 54847,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1VXA2z5Exv",
    "platform": "bilibili",
    "title": "vibe coding作品",
    "url": "http://www.bilibili.com/video/av116141183735099",
    "source": "whisperr_",
    "published_at": "2026-02-27T06:33:08+00:00",
    "summary": "",
    "duration_sec": 142,
    "views": 61,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV13KVf6nE7u",
    "platform": "bilibili",
    "title": "Vibe coding重度成瘾患者为啥不找妹子？",
    "url": "http://www.bilibili.com/video/av116674028115860",
    "source": "AIwood爱屋研究室",
    "published_at": "2026-06-01T09:32:00+00:00",
    "summary": "剧情纯属虚构，如有雷同，算你NB！",
    "duration_sec": 132,
    "views": 1466,
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
    "views": 229475,
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
    "views": 26193,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1yBVU6mEhs",
    "platform": "bilibili",
    "title": "152-WLB社群网站上线，欢迎访问wlbclub.com，Vibe Coding / Pencil + Codex",
    "url": "http://www.bilibili.com/video/av116669431155531",
    "source": "勇敢的心bbk",
    "published_at": "2026-05-31T13:32:14+00:00",
    "summary": "",
    "duration_sec": 512,
    "views": 706,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1zAVd6REtz",
    "platform": "bilibili",
    "title": "左打Spark、右踢Mavis，开源版Mac桌面Agent居然吊打腾讯、Google！拥有最强TensorLogic的记忆推理",
    "url": "http://www.bilibili.com/video/av116673810013007",
    "source": "LLM张老师",
    "published_at": "2026-06-01T08:06:27+00:00",
    "summary": "客户端下载：https://kocoro.ai\n开源地址：https://github.com/Kocoro-lab/Kocoro",
    "duration_sec": 1435,
    "views": 1313,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1bwVR6qE9o",
    "platform": "bilibili",
    "title": "读书：Vibe Coding",
    "url": "http://www.bilibili.com/video/av116672065246804",
    "source": "周小蜷",
    "published_at": "2026-06-01T00:45:40+00:00",
    "summary": "分享一本好书：《Vibe Coding： AI编程时代的认知重构》。\n作者：张昕东。",
    "duration_sec": 661,
    "views": 22,
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
    "views": 140208,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "platform": "bilibili",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "duration_sec": 64993,
    "views": 561055,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "platform": "bilibili",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！",
    "duration_sec": 55323,
    "views": 6833,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1hEVd6yEcn",
    "platform": "bilibili",
    "title": "【2026最新】全B站最详细AI Agent开发教程，手把手教你搭建企业级Agent智能体！从入门到实战，学完即就业，带你玩转AI Agent！",
    "url": "http://www.bilibili.com/video/av116673440909829",
    "source": "Agent开发",
    "published_at": "2026-06-01T06:35:48+00:00",
    "summary": "【2026最新】全B站最详细AI Agent开发教程，手把手教你搭建企业级Agent智能体！从入门到实战，学完即就业，带你玩转AI Agent！",
    "duration_sec": 94965,
    "views": 2251,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1eUVJ6EEB9",
    "platform": "bilibili",
    "title": "2026搞懂Java+AI大模型全套教程 | Spring AI+RAG+AI Agent+DeepSeek+航空AI智能客服项目实战，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116668374254145",
    "source": "程序员诸葛",
    "published_at": "2026-05-31T09:12:07+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套笔记和100万字面试宝典+场景题，简历模板，Java P 5~P8技术栈学习路线自取：https://t.bilibili.com/783606020197842963",
    "duration_sec": 16883,
    "views": 5268,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV13sVU6tEtJ",
    "platform": "bilibili",
    "title": "2026吃透AI Agent智能体全套系统教程，手把手教你从0到1打造企业级AI Agent智能体，学完即可就业！拿走不谢，学不会我退出IT圈！！！",
    "url": "http://www.bilibili.com/video/av116669313780558",
    "source": "AI大模型系统课程",
    "published_at": "2026-05-31T13:16:16+00:00",
    "summary": "【视频配套籽料，大模型最新学习路线，系统学习，问题解答等这里自取哦：https://www.bilibili.com/read/cv41307778/?jump_opus=1】\n视频制作不易，如果视频对你有用的话请一键三连【长按点赞】支持一下up哦，拜托，这对我真的很重要",
    "duration_sec": 71721,
    "views": 7688,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1x8Vd6TETt",
    "platform": "bilibili",
    "title": "【喂饭教程】全B站最详细AI Agent零基础系统入门教程，2小时快速掌握AI Agent实战开发技巧，手把手教你从0到1做AI项目！小白适用！学完即就业，带你",
    "url": "http://www.bilibili.com/video/av116673524794438",
    "source": "大模型开发入门",
    "published_at": "2026-06-01T06:58:26+00:00",
    "summary": "【喂饭教程】全B站最详细AI Agent零基础系统入门教程，2小时快速掌握AI Agent实战开发技巧，手把手教你从0到1做AI项目！小白适用！学完即就业，带你玩转AI开发赛道！",
    "duration_sec": 58868,
    "views": 495,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1EaVS6rEtY",
    "platform": "bilibili",
    "title": "【2026最新】全B站最全最细的AI Agent开发保姆级教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话，允许白嫖！学完直接就业！",
    "url": "http://www.bilibili.com/video/av116668575515757",
    "source": "大模型全栈开发",
    "published_at": "2026-05-31T10:00:27+00:00",
    "summary": "【2026最新】全B站最全最细的AI Agent开发保姆级教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话，允许白嫖！学完直接就业！",
    "duration_sec": 46384,
    "views": 1459,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1sM6xB5EEE",
    "platform": "bilibili",
    "title": "基于LabVIEW的AI Agent智能体实现教程",
    "url": "http://www.bilibili.com/video/av115993393238477",
    "source": "三易电子工作室",
    "published_at": "2026-02-01T04:12:23+00:00",
    "summary": "基于LabVIEW的AI Agent智能体实现教程，made by 三易电子工作室。",
    "duration_sec": 2577,
    "views": 3334,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1YWCgBfEdz",
    "platform": "bilibili",
    "title": "00_AI Agent for LabVIEW 全面教学：安装、配置、VI解析、代码生成，一次讲透！",
    "url": "http://www.bilibili.com/video/av115547740113313",
    "source": "仪酷智能",
    "published_at": "2025-11-14T11:13:10+00:00",
    "summary": "本视频将从零开始，带你完整掌握 AI Agent for LabVIEW 工具包的使用方法。\n无论你是 LabVIEW 开发者、做自动化/视觉/测试测控的工程师，还是对大模型 + LabVIEW 的结合感兴趣，本期内容都非常值得收藏！\n🔧 本期内容概览\n1）如何下载与安装工具包\n官方下载方式（官网入口）\nVIPM 安装步骤与 64bit 版本注意事项\n\n2）API 接入配置\n支持多家大模型：阿里云、DeepSeek、豆包、智谱、OpenAI 等\n如何填写 API Key\n如何测试连通性\nLabVIEW 内",
    "duration_sec": 1714,
    "views": 4219,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1HxDrB5Em2",
    "platform": "bilibili",
    "title": "【B站天花板】全网最细最全的Agent应用开发教程|手把手教你搭建企业级智能体，全程干货无废话，小白直接上手不踩坑,帮你少走 99% 弯路！ LLM|大模型",
    "url": "http://www.bilibili.com/video/av116367441334742",
    "source": "AI-Agent开发",
    "published_at": "2026-04-08T05:40:05+00:00",
    "summary": "【B站天花板】全网最细最全的Agent应用开发教程|手把手教你搭建企业级智能体，全程干货无废话，小白直接上手不踩坑,帮你少走 99% 弯路！ LLM|大模型",
    "duration_sec": 72517,
    "views": 16383,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1FSVZ6AENh",
    "platform": "bilibili",
    "title": "【AI教程】目前B站最全最细的AI Agent智能体零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116673877251747",
    "source": "大模型学习教程",
    "published_at": "2026-06-01T08:32:16+00:00",
    "summary": "【AI教程】目前B站最全最细的AI Agent智能体零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "duration_sec": 145628,
    "views": 200,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV13xVU6oEF3",
    "platform": "bilibili",
    "title": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！七天手把手带你从入门到精通！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116669297001988",
    "source": "大模型Agent开发",
    "published_at": "2026-05-31T13:07:42+00:00",
    "summary": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！七天手把手带你从入门到精通！少走99%的弯路！存下吧！很难找全的！",
    "duration_sec": 133045,
    "views": 2125,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "platform": "bilibili",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如何构建高效的AI代理\nP07 什么是AI代理规划设计模式\nP08 如何使用多AI代理系统\nP09 AI代理如何",
    "duration_sec": 7760,
    "views": 12594,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1peV96dExP",
    "platform": "bilibili",
    "title": "【最新】Hermes Agent保姆级教程，小白亦可玩转最强AI Agent，下载安装部署手把手教学，效率提升10倍，十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116672702715741",
    "source": "今天开始学Ai",
    "published_at": "2026-06-01T03:29:09+00:00",
    "summary": "Hermes Agent保姆级教程，小白亦可玩转最强AI Agent，工作效率提升10倍。喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up",
    "duration_sec": 10359,
    "views": 897,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV13gVb6KEEC",
    "platform": "bilibili",
    "title": "【全748集】目前B站最全最细的AI大模型零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116656244261441",
    "source": "Agent智能体搭建-",
    "published_at": "2026-05-29T05:45:53+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！！",
    "duration_sec": 94134,
    "views": 13736,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1RtGU6hEDd",
    "platform": "bilibili",
    "title": "DeepSeek-Reasonix 【保姆级教程】：专为 DeepSeek 打造的 AI 编程 Agent客户端，长会话成本到底能省多少？",
    "url": "http://www.bilibili.com/video/av116647486556383",
    "source": "程序员晓刘",
    "published_at": "2026-05-27T16:33:52+00:00",
    "summary": "本期体验 DeepSeek-Reasonix 这个开源项目，主要看客户端界面、模型模式、会话导入、MCP 配置、记忆与缓存等功能。内容基于个人使用记录，不做夸张结论，适合对 DeepSeek 生态和 AI 编程工具感兴趣的朋友参考。",
    "duration_sec": 370,
    "views": 6058,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV156VS6KEYu",
    "platform": "bilibili",
    "title": "【全136集】吊打付费！快速掌握AI Agent开发技巧，手把手教你从0到1搭建企业级智能体！AI Agent开发零基础入门保姆级教程 教你玩转AI智能体赛道！",
    "url": "http://www.bilibili.com/video/av116668491630778",
    "source": "全栈AI开发",
    "published_at": "2026-05-31T09:39:35+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦",
    "duration_sec": 90600,
    "views": 613,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1qMVd6HEBz",
    "platform": "bilibili",
    "title": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116673826789179",
    "source": "AI产品开发",
    "published_at": "2026-06-01T08:17:04+00:00",
    "summary": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！",
    "duration_sec": 76400,
    "views": 83,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1UvG96wETz",
    "platform": "bilibili",
    "title": "全网首套 Nuxt.js AI Agent 实战指南",
    "url": "http://www.bilibili.com/video/av116650305198611",
    "source": "vibecoding教程",
    "published_at": "2026-05-28T04:32:15+00:00",
    "summary": "课件免费领取踢小助理;web5189\n全网首套 Nuxt.js AI Agent 实战指南",
    "duration_sec": 6054,
    "views": 475,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1p5X6BSEFR",
    "platform": "bilibili",
    "title": "【AI教程】目前B站最详细的AI Agent智能体搭建全套教程，手把手带你从0到1搭建企业级智能体！全程干货无废话！让你少走99%弯路！AI大模型|LLM",
    "url": "http://www.bilibili.com/video/av116322142784662",
    "source": "Agent智能体搭建-",
    "published_at": "2026-03-31T05:39:12+00:00",
    "summary": "【AI教程】目前B站最详细的AI Agent智能体搭建全套教程，手把手带你从0到1搭建企业级智能体！全程干货无废话！让你少走99%弯路！AI大模型|LLM",
    "duration_sec": 51322,
    "views": 10584,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "platform": "bilibili",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP",
    "duration_sec": 474,
    "views": 172906,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV16xdBBLEtR",
    "platform": "bilibili",
    "title": "手把手教你搭建Claude MCP服务：从本地到远程，大厂已落地",
    "url": "http://www.bilibili.com/video/av116417437503756",
    "source": "下班学AI",
    "published_at": "2026-04-17T01:25:49+00:00",
    "summary": "🔥 MCP（模型上下文协议）到底是什么？为什么阿里、腾讯都在抢着布局？\n\n本期视频带你从零上手MCP——从常见的开源服务（Playwright自动化、Figma设计转代码、GitHub操作），到手写一个自己的MCP服务器（时间查询、数字相加、商品价格查询），并成功接入Claude CLI实现本地调用。\n\n随后，我会演示如何将MCP服务从本地部署到云端，让它真正变成可远程调用的AI能力。\n\n最后，拆解两大厂商的MCP落地案例：\n\n阿里云百炼：60+预置MCP服务\n腾讯云TI：嵌入微信生态，聚焦社交与支付\n🚀",
    "duration_sec": 591,
    "views": 3078,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1mnG16zExm",
    "platform": "bilibili",
    "title": "构建第一个MCP服务器",
    "url": "http://www.bilibili.com/video/av116645305588571",
    "source": "knight008848",
    "published_at": "2026-05-27T07:17:37+00:00",
    "summary": "https://www.youtube.com/playlist?list=PLlrxD0HtieHjYfVUpGl_-ai7D6FRBjV-d\n欢迎您踏上模型上下文协议的学习之旅！如果您曾好奇 AI 应用程序如何与各种工具和服务进行通信，您即将发现一个优雅的解决方案，它正在改变开发者构建智能系统的方式。",
    "duration_sec": 204,
    "views": 5,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "platform": "bilibili",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP",
    "duration_sec": 511,
    "views": 50130,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1rE1SBpEha",
    "platform": "bilibili",
    "title": "【MCP】使用FastMCP快速实现MCP服务端和客户端功能",
    "url": "http://www.bilibili.com/video/av115512960883264",
    "source": "胖虎遛二狗",
    "published_at": "2025-11-08T07:50:20+00:00",
    "summary": "相关文档：https://gofastmcp.com/getting-started/welcome\n大模型系列教程： https://github.com/echonoshy/cgft-llm",
    "duration_sec": 1562,
    "views": 5241,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1Uc7Sz2EqJ",
    "platform": "bilibili",
    "title": "自动化挖漏洞哪家强？LLM+Burpsuite 组合出道，黑客看了直呼 “蚌埠住了”！",
    "url": "http://www.bilibili.com/video/av114612527701492",
    "source": "水獭安全",
    "published_at": "2025-06-02T07:17:41+00:00",
    "summary": "通过 MCP 服务构建&quot;AI渗透测试工程师&quot;，实现Burp Suite的智能调度与自动化漏洞狩猎。",
    "duration_sec": 1052,
    "views": 4775,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "platform": "bilibili",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www.bilibili.com/video/BV1r17azXEAj\n\nMCP简单来说就是AI大模型的标准化工具箱，",
    "duration_sec": 971,
    "views": 140024,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1yT8qzMEbd",
    "platform": "bilibili",
    "title": "基于SpringAI开发Java版mcp服务",
    "url": "http://www.bilibili.com/video/av114942720148945",
    "source": "程序员Cafe",
    "published_at": "2025-07-30T15:05:27+00:00",
    "summary": "如何用Java开发一个mcp服务？如何把已有的spingboot微服务改造成mcp服务呢？如何在mcp客户端调用mcp服务？\n今天来一个保姆级教学",
    "duration_sec": 779,
    "views": 11055,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1Kuahz8Efz",
    "platform": "bilibili",
    "title": "Dify教程-MCP服务",
    "url": "http://www.bilibili.com/video/av115151881641819",
    "source": "花里胡哨的汤无际",
    "published_at": "2025-09-05T13:23:34+00:00",
    "summary": "",
    "duration_sec": 1271,
    "views": 3654,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1ARV36GEQ4",
    "platform": "bilibili",
    "title": "配置一台医疗影像系统服务器！主要配置 至强双路32核心CPU,128G内存，两个1.92T SSD组RAID1，4U机架式服务器！",
    "url": "http://www.bilibili.com/video/av116662619604849",
    "source": "易加服务器工作站",
    "published_at": "2026-06-01T03:00:00+00:00",
    "summary": "",
    "duration_sec": 77,
    "views": 209,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1BwVd6xEBM",
    "platform": "bilibili",
    "title": "5 分钟 动手 写一个 MCP Server",
    "url": "http://www.bilibili.com/video/av116673625460733",
    "source": "白羊武士弗拉明戈",
    "published_at": "2026-06-01T07:23:15+00:00",
    "summary": "MCP 是什么，怎么创建 MCP server？5分钟上手自己写一个 MCP server！",
    "duration_sec": 281,
    "views": 11,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1vc7YzkEws",
    "platform": "bilibili",
    "title": "小智AI MCP外置视觉系统重磅升级2.0所有设备0成本0改造接入摄像头视觉系统硬件平权，代码开源！人形机器人？语音小盒子？通通给我接入AI小智MCP服务！",
    "url": "http://www.bilibili.com/video/av114620815642839",
    "source": "闪猫侠机器人",
    "published_at": "2025-06-04T01:09:18+00:00",
    "summary": "闪猫MCP服务平台：http://mcp.shanmaotech.cn\n官网www.shanmaotech.cn\nQQ技术交流群：795042597",
    "duration_sec": 255,
    "views": 13081,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1W7ijBkEwJ",
    "platform": "bilibili",
    "title": "cheatengine-mcp自动化逆向，CE调试器的MCP",
    "url": "http://www.bilibili.com/video/av115835855242400",
    "source": "花老板AI",
    "published_at": "2026-01-04T08:24:14+00:00",
    "summary": "Cheat Engine MCP Bridge是一个开源中间件项目，通过Model Context Protocol（MCP）协议为AI助手提供逆向工程能力。该项目将Cheat Engine的内存读写、汇编分析等核心功能封装为标准化的MCP工具，让AI模型能够直接调用这些专业逆向工具进行自动化分析。\n\n核心功能包括：内存地址扫描与读写、汇编代码反编译、断点调试管理、内存数据修改等。开发者可以通过简单的JSON配置集成到支持MCP的AI平台（如DeepSeek、通义千问等），实现自然语言驱动的逆向分析工作流",
    "duration_sec": 161,
    "views": 4068,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1aMAczmEmf",
    "platform": "bilibili",
    "title": "[MoonPack]在布吉岛里注入模组-mcp",
    "url": "http://www.bilibili.com/video/av116264966163402",
    "source": "DanciestZebra70",
    "published_at": "2026-03-21T03:13:25+00:00",
    "summary": "交流群\n①1051043310\n②365233792",
    "duration_sec": 85,
    "views": 2851,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV165dAYxEdD",
    "platform": "bilibili",
    "title": "只需几行代码用Java写一个MCP服务！从0到1开发MCP服务！",
    "url": "http://www.bilibili.com/video/av114306863598282",
    "source": "图灵诸葛官方号",
    "published_at": "2025-04-09T07:43:00+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持~\r\n本视频配套资料戳这里获取→https://www.bilibili.com/read/cv38661345/\r\n【还可额外领取100w字Java面试宝典】",
    "duration_sec": 328,
    "views": 12171,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1L1VJ6nEe8",
    "platform": "bilibili",
    "title": "5分钟讲清楚 MCP 是什么",
    "url": "http://www.bilibili.com/video/av116668474852072",
    "source": "白羊武士弗拉明戈",
    "published_at": "2026-05-31T09:31:30+00:00",
    "summary": "",
    "duration_sec": 330,
    "views": 222,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "platform": "bilibili",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp",
    "duration_sec": 1854,
    "views": 29472,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1u4G9zmEte",
    "platform": "bilibili",
    "title": "什么是MCP？VS Code中使用MCP Server",
    "url": "http://www.bilibili.com/video/av114426032168712",
    "source": "AI落地派",
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based on NodeJS\nhttps://www.npmjs.com/package/@benborla29/mcp-",
    "duration_sec": 347,
    "views": 5927,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1DHQGB7EMk",
    "platform": "bilibili",
    "title": "一个用于AI内存操作的MCP工具 Memory Disassembler MCP",
    "url": "http://www.bilibili.com/video/av116403361352590",
    "source": "远程力量英雄_",
    "published_at": "2026-04-14T13:51:39+00:00",
    "summary": "这是一个面向 MCP（Model Context Protocol）的 Memory Disassembler 工具：让 AI 在受控的工具调用下完成进程附加、读写内存、模块/内存区域枚举、反汇编、结构体分析、AOB 特征码扫描、指针链解析、快照对比、字符串搜索等逆向与调试工作流。\n 项目重点做了“工程化可用”：耗时任务统一队列化（job 管理避免客户端超时）、提供静态分析优先的安全策略、以及调试/断点相关的恢复工具（卡死时可一键清理并释放调试状态）。适合做安全研究、二进制分析学习、以及搭建 AI 辅助的",
    "duration_sec": 940,
    "views": 2217,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "platform": "bilibili",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/",
    "duration_sec": 452,
    "views": 8896,
    "matched_keywords": [
      "MCP 服务器"
    ]
  }
]
```
