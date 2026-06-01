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
    "id": "rss:https://huggingface.co/blog/nvidia/nemotron-labs-diffusion",
    "platform": "rss",
    "title": "Towards Speed-of-Light Text Generation with Nemotron-Labs Diffusion Language Models",
    "url": "https://huggingface.co/blog/nvidia/nemotron-labs-diffusion",
    "source": "Hugging Face - Blog",
    "published_at": "2026-05-23T00:02:03+00:00",
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
    "points": 441,
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
    "points": 192,
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
    "points": 72,
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
    "points": 21,
    "comments": 2
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
    "points": 382,
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
    "comments": 7
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
    "points": 43,
    "comments": 72
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
    "points": 394,
    "comments": 399
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
    "points": 1088,
    "comments": 1241
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
    "points": 416,
    "comments": 469
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
    "comments": 426
  },
  {
    "id": "hn:48214017",
    "platform": "hackernews",
    "title": "Anthropic is expanding to Colossus2. Will use GB200",
    "url": "https://twitter.com/nottombrown/status/2057194829986300375",
    "source": "aurareturn",
    "published_at": "2026-05-20T20:55:52+00:00",
    "summary": "",
    "points": 306,
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
    "points": 1758,
    "comments": 1363
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
    "id": "bvid:BV1Yi5M6DERk",
    "platform": "bilibili",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】",
    "duration_sec": 27045,
    "views": 159684,
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
    "views": 1499,
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
    "views": 850712,
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
    "views": 11700,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "platform": "bilibili",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "穷在街头无人问lhj",
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：https://pan.baidu.com/s/12IDm7vXhr-o8kL65S6tEyA?pwd=1029",
    "duration_sec": 700,
    "views": 3279,
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
    "views": 83507,
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
    "views": 746229,
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
    "views": 13431,
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
    "views": 3450,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1XDVh61Ej2",
    "platform": "bilibili",
    "title": "（B站狂推！比刷剧爽！）2026公认最好的《Claude Code》教程，附课件代码—Claude Code探索-测试-重构-调试代码库",
    "url": "http://www.bilibili.com/video/av116656831466162",
    "source": "吴老师讲人工智能",
    "published_at": "2026-05-31T03:45:00+00:00",
    "summary": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码-----ClaudeCode【配套课程笔记+代码文件】+进阶学习路线-可以在我的gong.粽.号.【辅论AI】发送【333】无偿自取就行哦~",
    "duration_sec": 6174,
    "views": 1901,
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
    "views": 2214,
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
    "views": 62147,
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
    "views": 2811,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1VzVV6cEjN",
    "platform": "bilibili",
    "title": "（比刷剧爽！）2026公认最好的《Claude Code》教程，附课件代码—Claude Code探索-测试-重构-调试代码库",
    "url": "http://www.bilibili.com/video/av116663894671930",
    "source": "有情的码农",
    "published_at": "2026-05-30T14:11:55+00:00",
    "summary": "本课程我们将学习到：\n1.使用 Claude 代码来探索、开发、测试、重构和调试代码库。\n2.使用 MCP 服务器（例如 Playwright 和 Figma MCP 服务器）扩展 Claude Code 的功能。\n3.将 Claude Code 最佳实践应用于三个项目：探索和开发 RAG 聊天机器人的代码库，重构电子商务数据的 Jupyter 笔记本并将其转换为仪表板，以及从 Figma 模型构建 Web 应用程序。",
    "duration_sec": 6173,
    "views": 1204,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV116Vt6dEG4",
    "platform": "bilibili",
    "title": "GPT 5.5 还是赢了？Claude Opus 4.8 实测",
    "url": "http://www.bilibili.com/video/av116656495986521",
    "source": "kate人不错",
    "published_at": "2026-05-29T06:44:14+00:00",
    "summary": "欢迎关注我的知识星球：https://t.zsxq.com/FF0He\n\n我会分享最新AI资讯、源代码、回答你的提问。\n\n这期视频我会先介绍 Opus 4.8 的主要变化，包括榜单表现、早期测试者反馈、Agent 能力、价格变化、Claude Code 动态工作流，以及它在工具调用和不确定性表达上的改进。\n\n然后我会用 8 个复杂前端交互任务，把 Claude Opus 4.8 和 GPT 5.5 放在一起对比。测试重点不是单纯看页面好不好看，而是看核心功能、算法模拟、交互状态、事件绑定、可运行性和交付完",
    "duration_sec": 734,
    "views": 17681,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1GLdABKEaR",
    "platform": "bilibili",
    "title": "【自用】Claude Code 驱动 Comsol 复现论文仿真",
    "url": "http://www.bilibili.com/video/av116534089482864",
    "source": "Ricardo_Tsang",
    "published_at": "2026-05-07T16:10:32+00:00",
    "summary": "",
    "duration_sec": 6198,
    "views": 16396,
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
    "views": 3545,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1CNV86tEQM",
    "platform": "bilibili",
    "title": "[parallel] Claude Code 动态工作流详解",
    "url": "http://www.bilibili.com/video/av116655640283767",
    "source": "isomoes",
    "published_at": "2026-05-29T03:05:47+00:00",
    "summary": "1.5x https://claude.com/blog/introducing-dynamic-workflows-in-claude-code\n\n本期视频介绍 Claude Code 随 Opus 4.8 同步推出的动态工作流（dynamic workflow），也就是把思考等级调到最高档 ultra code 后才会启用的功能。视频首先对比了上一期讲过的 Claude agents（Claude views）：两者都做并行任务，但 Claude agents 基于 git worktree，靠文件系",
    "duration_sec": 680,
    "views": 630,
    "matched_keywords": [
      "Claude Code 实战"
    ]
  },
  {
    "id": "bvid:BV1TcLg67Egj",
    "platform": "bilibili",
    "title": "Claude Code + Hermes架构打造自己的ai员工",
    "url": "http://www.bilibili.com/video/av116583431210323",
    "source": "dadafastrun",
    "published_at": "2026-05-16T09:01:42+00:00",
    "summary": "claude code + hermes架构打造自己的ai员工",
    "duration_sec": 1311,
    "views": 2830,
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
    "views": 10840,
    "matched_keywords": [
      "Claude Code 实战"
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
    "views": 3064,
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
    "views": 304899,
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
    "views": 4999,
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
    "views": 1484,
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
    "views": 33117,
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
    "views": 6177,
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
    "views": 2671,
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
    "views": 13431,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "platform": "bilibili",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": "",
    "duration_sec": 1083,
    "views": 220461,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1ZPdZBcEof",
    "platform": "bilibili",
    "title": "【零基础AI游戏编程】手搓塞尔达传说.Godot·AI安装(win版)",
    "url": "http://www.bilibili.com/video/av116430775259436",
    "source": "西高君",
    "published_at": "2026-04-19T13:00:00+00:00",
    "summary": "Godot官网：https://godotengine.org/zh-cn/\nTRAE国内版官网：https://www.trae.cn/ide/download  （注意：选择trae ide版本，不是solo版）\nTRAE国际版官网：https://www.trae.ai/download   （注意：选择trae ide版本，不是solo版）\nvscode插件商城：https://marketplace.visualstudio.com/items?itemName=geequlim.godot-t",
    "duration_sec": 553,
    "views": 6829,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV19uhGzXErR",
    "platform": "bilibili",
    "title": "使用Cursor AI和SuperDesign打造真正美观的应用和网站！",
    "url": "http://www.bilibili.com/video/av114963590941894",
    "source": "攒钱换房车的福叔",
    "published_at": "2025-08-03T07:18:55+00:00",
    "summary": "本品由Wshiper 语音识别，由Gemma3-27b（deepseek 被大家吐槽说垃圾翻译）进行翻译，由xtts 进行语音配音。\n高性价比 4090（100M公网） 租赁：https://passport.compshare.cn/register?referral_code=JmXHLuBEM7TBJQK7s1tjx3 实名认证后，你有10，我也有10，\n关注公众号：福满楼的私货，获取更多AI工具一键包。\n4090 48G 大显存 https://www.ucloud.cn/site/active/",
    "duration_sec": 903,
    "views": 217,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1yXVp6GE13",
    "platform": "bilibili",
    "title": "Cursor彻底杀疯了！直接干翻全场，这才是最强AI编程神器！",
    "url": "http://www.bilibili.com/video/av116653207586628",
    "source": "AI-seeker",
    "published_at": "2026-05-28T16:52:06+00:00",
    "summary": "原视频链接https://www.youtube.com/watch?v=GBISeUYMzoU \n本视频为AI翻译，翻译：小胡api（xiaohumini.site），配音：鸡哥\n①xiaohuminiAPI中转：xiaohumini.site，0.8r/1$，拥有500+大模型API；\n②在线生图、视频生成工具https://creator.vertexgen.net，支持接入中转api；\n③批发API中转站：aifast.site（备用域名chat.aifast.site），0.4r/1$，sora",
    "duration_sec": 1822,
    "views": 425,
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
    "views": 6320,
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
    "views": 57480,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "platform": "bilibili",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改",
    "duration_sec": 9184,
    "views": 564979,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1ka4QziEBr",
    "platform": "bilibili",
    "title": "Codesys IDE 通过Cursor AI自动生成项目，定义程序组织单元，生成变量，编写程序，编译和保存程序。",
    "url": "http://www.bilibili.com/video/av115369649898669",
    "source": "Yellance_HCH",
    "published_at": "2025-10-14T00:23:56+00:00",
    "summary": "Codesys IDE 通过Cursor AI自动生成项目，定义程序组织单元，生成变量，编写程序，编译和保存程序。",
    "duration_sec": 276,
    "views": 496,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV192Vb66Erj",
    "platform": "bilibili",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116656110049859",
    "source": "槐柚子柚",
    "published_at": "2026-05-29T08:30:00+00:00",
    "summary": "",
    "duration_sec": 1080,
    "views": 291,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1b5AeeGEFc",
    "platform": "bilibili",
    "title": "Cursor太贵？分享三个免费AI编程方案+海量编程技巧【如何看待AI编程】",
    "url": "http://www.bilibili.com/video/av114025056699722",
    "source": "技术爬爬虾",
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。",
    "duration_sec": 752,
    "views": 153394,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "platform": "bilibili",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "published_at": "2025-03-22T04:02:08+00:00",
    "summary": "很多人都想学编程,但被高门槛劝退。本期给大家介绍一款零门槛的AI编程工具-豆包电脑版。通过3个实战案例,带你体验如何用AI轻松实现编程。\n\n豆包电脑版特点:\n- 中文界面,所见即所得\n- 支持html代码预览\n- 支持Python运行\n- 可生成完整项目代码\n- 历史版本管理\n- 代码一键导出\n\n时间戳\n00:00 为什么要学AI编程\n03:19 案例1:图片压缩网站实战\n04:15 案例2:数据可视化图表生成\n07:02 案例3:长文本翻译网站开发\n10:22 总结与工具获取方式",
    "duration_sec": 642,
    "views": 382798,
    "matched_keywords": [
      "Cursor AI 编程"
    ]
  },
  {
    "id": "bvid:BV1thXHY2EXh",
    "platform": "bilibili",
    "title": "Cursor+three.js，简单提示词也能生成交互式3D",
    "url": "http://www.bilibili.com/video/av114205059521179",
    "source": "Next蔡蔡",
    "published_at": "2025-03-22T08:11:40+00:00",
    "summary": "上周发布了 Cursor+Blender MCP 快速实现3D建模的教程，但由于目前MCP还不是特别稳定，加上配置有点麻烦不一定能一次成功，所以不少小伙伴被劝退了。\n.\n后面我发现借助three.js，就能让大家通过简单的提示词，轻松实现一些还不错的交互式3D场景，非常适合放在一些教学或者科普场景。大家快去试试吧 ~ \n.\n欢迎加入我的知识星球，有问必答：https://t.zsxq.com/fD4Fb",
    "duration_sec": 132,
    "views": 33325,
    "matched_keywords": [
      "Cursor AI 编程"
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
    "views": 80167,
    "matched_keywords": [
      "vibe coding"
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
    "views": 3875,
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
    "views": 149198,
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
    "views": 139925,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1GyGX6TEDi",
    "platform": "bilibili",
    "title": "1个人，如何通过Vibe Coding快速实现变现？",
    "url": "http://www.bilibili.com/video/av116650858847182",
    "source": "老麦的工具库",
    "published_at": "2026-05-29T12:00:00+00:00",
    "summary": "",
    "duration_sec": 310,
    "views": 305726,
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
    "views": 2808,
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
    "views": 741,
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
    "views": 9187,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1t1Gt6bEzH",
    "platform": "bilibili",
    "title": "看到 API Key 泄漏视频后，我连夜扫了自己的 GitHub，结果真出事了",
    "url": "http://www.bilibili.com/video/av116617270790182",
    "source": "goldenzihang",
    "published_at": "2026-05-22T08:27:55+00:00",
    "summary": "看了 B 站账号 网络小白_Uncle城 关于 GitHub API Key 泄漏的视频后，我有点后背发凉。作为一个靠 AI 速成写项目、GitHub 还在熟悉中的人，我立刻给自己的项目做了一次扫描，结果真的发现旧公开仓库存在脱敏命中风险。\n这个视频介绍我整理的开源前检查工具 / Codex Skill：api-key-leak-checker-leop。\nGitHub：\nhttps://github.com/leo-cheung-itlger/api-key-leak-checker-leop\n它会在上",
    "duration_sec": 186,
    "views": 1441,
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
    "views": 229038,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1E6Vh6WEDa",
    "platform": "bilibili",
    "title": "把Claude code丨Codex接入Rstudio的工具ClaudeR体验分享，在分析步骤可控的情况下vibe coding",
    "url": "http://www.bilibili.com/video/av116656680540306",
    "source": "外科小小硕",
    "published_at": "2026-05-29T07:30:54+00:00",
    "summary": "效果还行，在步骤可控的情况下vibe coding，适合做数据分析等工作。但体验还可进一步优化。",
    "duration_sec": 779,
    "views": 1502,
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
    "views": 25630,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1huVS64Epj",
    "platform": "bilibili",
    "title": "Vibe Coding劝退指南：别踩我30亿的坑",
    "url": "http://www.bilibili.com/video/av116668827179903",
    "source": "流明AI笔记",
    "published_at": "2026-05-31T10:59:56+00:00",
    "summary": "",
    "duration_sec": 286,
    "views": 45,
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
    "views": 50608,
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
    "views": 94177,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1u1V36EE3G",
    "platform": "bilibili",
    "title": "如何让 AI 写出高质量代码？Spec 定义+Vibe Coding+Design MD UI 规范全攻略",
    "url": "http://www.bilibili.com/video/av116662653162533",
    "source": "前端进阶学习站",
    "published_at": "2026-05-30T08:48:35+00:00",
    "summary": "",
    "duration_sec": 388,
    "views": 151,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV13tVU6xEM7",
    "platform": "bilibili",
    "title": "【实战经验】达芬奇自动剪辑插件！Vibe Coding全流程分享",
    "url": "http://www.bilibili.com/video/av116669347339006",
    "source": "觅影长风",
    "published_at": "2026-05-31T13:13:53+00:00",
    "summary": "本期分享我用 Vibe Coding 制作达芬奇自动化剪辑插件的全过程✨\n从插件开发思路、完整的Vibe Coding流程、用到的Skill，\n再到如何自定义制作专属Skill，\n以及我的开发灵感来源，一次性讲清楚～",
    "duration_sec": 369,
    "views": 116,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1BGGyzKEDs",
    "platform": "bilibili",
    "title": "🔥 体验NeoVim下的Vibe Coding",
    "url": "http://www.bilibili.com/video/av114419421942829",
    "source": "比特光锥_BightCone",
    "published_at": "2025-04-30T00:45:00+00:00",
    "summary": "https://www.youtube.com/watch?v=CbQGeaa8XrQ\n感谢观看~~如果觉得视频内容不错，欢迎点赞、投币、三连和关注~~\n视频主要内容如下：\n💻 NeoVim 是 Vim 的增强版，提供更快的代码编辑体验！\n🔧 安装 NeoVim 可以通过 pip 或 Homebrew，注意选择正确的安装方式。\n🎨 NeoVim 与 Vim 的细微差异，例如光标显示不同。\n🚀 使用 LazyVim 设置可以优化 NeoVim 的配置，提升效率。\n💡 Boot.dev 用 RPG 的方式学习",
    "duration_sec": 2891,
    "views": 38086,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV19x6vBXEqC",
    "platform": "bilibili",
    "title": "1小时精通 Qoder Skills：实战+避坑指南",
    "url": "http://www.bilibili.com/video/av115982991365489",
    "source": "Qoder",
    "published_at": "2026-01-30T10:05:00+00:00",
    "summary": "",
    "duration_sec": 3488,
    "views": 27775,
    "matched_keywords": [
      "vibe coding"
    ]
  },
  {
    "id": "bvid:BV1wh5q6mEEx",
    "platform": "bilibili",
    "title": "成功了！小白手搓app全栈上云过程实录（超详细+避坑）像猹一样在ai之间穿梭",
    "url": "http://www.bilibili.com/video/av116578330872798",
    "source": "月小小吖",
    "published_at": "2026-05-15T12:00:29+00:00",
    "summary": "起因是市面上没好用的缅语背单词 App，遂手搓之。\n作为一个一行代码都不会写的历史文化方向的文科生，我用了 10 天，经历了无数莫名其妙的问题，终于把这玩意儿送上了云端。这期就是全过程实录！\n我会复盘我是怎么在 Gemini 和 Cursor 之间像猹一样来回穿梭，不管嘛，反正做成功了。\n如果你也想试试，除了看我历经三程，其中这几个关键点建议收藏：\n 1. 必备三大文档：校准需求，让ai不跑偏，核心技术来自up主@PM刘搞定  老师，视频里多次提及且感谢，大家一定要去看他的视频。\n 2. 语音大法：逻辑乱",
    "duration_sec": 1065,
    "views": 11191,
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
    "views": 556730,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1jAVh6UEmZ",
    "platform": "bilibili",
    "title": "【搭建智能体】2026B站最新保姆级Agent智能体搭建教程，从入门到实战全搞定！手把手教你打造个人专属智能体，彻底搞懂AI智能体开发，学会直接薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116657351563831",
    "source": "Agent搭建智能体",
    "published_at": "2026-05-29T13:36:47+00:00",
    "summary": "【视频配套籽料、零基础学习路线、实战项目案例、电子书+问题解答 在 ”置顶平论” 自取哦】\n本套教程从零开始讲解Agent智能体搭建，包含AI开发环境搭建，模型预训练等一些基础概念、RAG、Agent、Langchain、LangGraph和私有化部署\n无论是新手小白，还是有经验的友友，皆可学习\n视频对你有用的话，还请 一键三连【长按点赞】支持一下UP哦！你的支持是我更新的动力~",
    "duration_sec": 53868,
    "views": 2709,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1fuV56zEXh",
    "platform": "bilibili",
    "title": "【2026最新】这绝对是B站最优质的Agent开发全套教程！全程干货，允许白嫖！从0开始手把手落地企业级AI实战！开发Agent智能体！学完直接就业！",
    "url": "http://www.bilibili.com/video/av116663559133035",
    "source": "开发Agent",
    "published_at": "2026-05-30T12:43:25+00:00",
    "summary": "【视频配套籽料、零基础学习路线、实战项目案例、电子书+问题解答 在 ”置顶平论” 自取哦】\n本套教程从零开始讲解agent开发，手把手教学，包含AI大模型入门、AI开发环境搭建及提示词工程、Transformer架构和预训练等一些基础概念、RAG、Agent、Langchain、LangGraph大模型微调和私有化部署\n无论是新手小白，还是有经验的友友，皆可学习\n视频对你有用的话，还请 一键三连【长按点赞】支持一下UP哦！你的支持是我更新的动力~",
    "duration_sec": 58870,
    "views": 4086,
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
    "views": 3326,
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
    "views": 485,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1uZVJ6GEjB",
    "platform": "bilibili",
    "title": "目前B站讲的最好的AI Agent智能体开发全套教程，手把手教你快速搭建自己的智能体！全程干货无废话！学完即就业，让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116668072201170",
    "source": "阿里架构师诸葛",
    "published_at": "2026-05-31T07:53:46+00:00",
    "summary": "目前B站讲的最好的AI Agent智能体开发全套教程，手把手教你快速搭建自己的智能体！全程干货无废话！学完即就业，让你少走99%的弯路！",
    "duration_sec": 63382,
    "views": 6011,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1AZV36gEt4",
    "platform": "bilibili",
    "title": "【26年最新版】B站超详细《 AI Agent》 开发实战教程，手把手带你搭建企业级智能体，从零基础入门到项目落地，让你少走99%的弯路",
    "url": "http://www.bilibili.com/video/av116662787380623",
    "source": "AI学习小课堂",
    "published_at": "2026-05-30T09:28:12+00:00",
    "summary": "【26年最新版】B站超详细 《AI Agent》 开发实战教程，手把手带你搭建企业级智能体，从零基础入门到项目落地，让你少走99%的弯路",
    "duration_sec": 24368,
    "views": 379,
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
    "views": 10444,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1ZHAozLE7b",
    "platform": "bilibili",
    "title": "【SynthPilot】全网首发！2026年最新基于AI的FPGA开发教程，Agent自主编程/调试全链路闭环，500+工具接入Vivado",
    "url": "http://www.bilibili.com/video/av116164755790661",
    "source": "晓川科研站",
    "published_at": "2026-03-03T10:26:33+00:00",
    "summary": "全网首个AI Agent FPGA开发教程。SynthPilot通过MCP协议打通Vivado全链路，AI自主写码、综合、读报告、改Bug、迭代——真正的Agent模式闭环开发。从零开始，带你见证FPGA开发方式的代际变革。\n获取工具:synthpilot.dev\n晓川交流群:1007696121",
    "duration_sec": 2387,
    "views": 12725,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1MEojBeEMZ",
    "platform": "bilibili",
    "title": "这次真不难！Agent智能体 + Seedance 2.0助你快速做出AI视频",
    "url": "http://www.bilibili.com/video/av116459799843179",
    "source": "机智波玩ai",
    "published_at": "2026-04-24T13:05:06+00:00",
    "summary": "通过 Agent智能体和Seedance 2.0的结合，快速了解AI视频制作的基本流程。\n同款画布工作流地址：https://rhtv.runninghub.cn/camp/view/2047231703323254785?inviteCode=rh-v1222\n新人福利：注册送1000积分+3元体验金。",
    "duration_sec": 694,
    "views": 372,
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
    "views": 4553,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1ccVG6MERR",
    "platform": "bilibili",
    "title": "【全100集】全B站最详细“即梦+豆包+剪映”教程，2小时快速掌握AI动漫制作技巧，手把手教你从0到1制作AI短片！小白适用！学完即接单，带你玩转AI视频赛道！",
    "url": "http://www.bilibili.com/video/av116662820936496",
    "source": "Ai短剧制作官方教程",
    "published_at": "2026-05-30T09:35:22+00:00",
    "summary": "持续更新中，资料和工具在评论区哦",
    "duration_sec": 5861,
    "views": 9168,
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
    "views": 921,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "platform": "bilibili",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！",
    "duration_sec": 1951,
    "views": 1057973,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1kYVJ6bEyA",
    "platform": "bilibili",
    "title": "【AI教程】B站最全最细的Agent开发教程，从入门到实战！手把手教你快速打造自己的专属智能体，全程干货无废话，让你少走99%弯路！",
    "url": "http://www.bilibili.com/video/av116668340704862",
    "source": "Agent搭建教程",
    "published_at": "2026-05-31T09:03:48+00:00",
    "summary": "【AI教程】B站最全最细的Agent开发教程，从入门到实战！手把手教你快速打造自己的专属智能体，全程干货无废话，让你少走99%弯路！",
    "duration_sec": 73939,
    "views": 370,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "platform": "bilibili",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。",
    "duration_sec": 7636,
    "views": 9066,
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
    "views": 2391,
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
    "views": 11201,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1V8Gv6XE1T",
    "platform": "bilibili",
    "title": "【OpenClaw保姆级教程】最新版小龙虾OpenClaw完整安装教学，一个视频搞懂OpenClaw本地部署/接入微信/飞书/钉钉（附完整操作文档）",
    "url": "http://www.bilibili.com/video/av116621699979136",
    "source": "Agent喂饭级教程",
    "published_at": "2026-05-23T03:20:10+00:00",
    "summary": "全新版本，大家记得三连获取安装资料哦",
    "duration_sec": 6398,
    "views": 37984,
    "matched_keywords": [
      "AI Agent 教程"
    ]
  },
  {
    "id": "bvid:BV1CmGy6wEha",
    "platform": "bilibili",
    "title": "【Java+大模型】B站唯一讲的最好的Java AI Agent大模型教程，Spring AI Alibaba Agent Framwork+Skill全搞懂！",
    "url": "http://www.bilibili.com/video/av116645607512248",
    "source": "图灵官方诸葛",
    "published_at": "2026-05-27T08:43:15+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\nJava+AI大模型200万字面试宝典，学习路线图和简历模板自取：https://www.bilibili.com/opus/808122827166187527",
    "duration_sec": 20874,
    "views": 5149,
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
    "views": 172854,
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
    "views": 3052,
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
    "views": 50090,
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
    "views": 4770,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1EyoCBhEHZ",
    "platform": "bilibili",
    "title": "OpenClaw 接入MCP服务",
    "url": "http://www.bilibili.com/video/av116476610609849",
    "source": "龙虾讲AI",
    "published_at": "2026-04-27T12:17:08+00:00",
    "summary": "本节课程配套学习籽聊，点击下方连结，快速令曲👇\nhttps://www.bilibili.com/opus/1100126091579752452\n包含AI智能体搭建/AI大模型应用开发/AI商业变现/AI图文漫剧生成全套籽聊，\nAI智能体搭建入门到精通(最新版)，完全零基础学习，全面精通智能体搭建技术，\nAI大模型企业级应用实战(最新版)，全网最通俗易懂，彻底掌握大模型开发技术，\nAI热门工具从入门到精通(最新版)，全面提高生产效率，快速掌握AI热门工具，\n全程干货，无废话，通俗易懂，小白学了都直呼太简",
    "duration_sec": 120,
    "views": 268,
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
    "views": 4061,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV13K1YBtE6e",
    "platform": "bilibili",
    "title": "【GMM】MCP 使用说明",
    "url": "http://www.bilibili.com/video/av115485010168640",
    "source": "3DM小莫",
    "published_at": "2025-11-03T09:19:08+00:00",
    "summary": "MCP 支持 是 Gloss Mod Manager（GMM ）在 1.62.0 新增的一个功能， 你需要至少更新到 1.62 才能使用此功能；\n\n你可以使用任何支持 MCP 的客户端 和 AI 使用它, 但建议你的 AI 最大 Token 至少有 32K, 否则部分功能可能会受影响。\n\n相关代码已经开源，欢迎参与维护:  https://github.com/GlossMod/Gloss-Mod-Manager\n\nBGM: Modern Technology",
    "duration_sec": 600,
    "views": 35476,
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
    "views": 12169,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1UY42zhEtU",
    "platform": "bilibili",
    "title": "如何使用codex连接mcp",
    "url": "http://www.bilibili.com/video/av115366747578338",
    "source": "DashLi进化论",
    "published_at": "2025-10-13T12:05:10+00:00",
    "summary": "https://youtu.be/zfYEZ3_Nnkc?si=N0ARm9zeICrC1zJ4\n一键三连，关注我，一起vibe coding",
    "duration_sec": 406,
    "views": 4599,
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
    "views": 139943,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1hnjGzLE14",
    "platform": "bilibili",
    "title": "【小智教程】手挽手教你如何接入别人的MCP服务",
    "url": "http://www.bilibili.com/video/av114568722450105",
    "source": "空白泡泡糖果",
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html",
    "duration_sec": 510,
    "views": 16878,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "platform": "bilibili",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！",
    "duration_sec": 7408,
    "views": 364507,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1rq4y117uA",
    "platform": "bilibili",
    "title": "保姆级教程！教你开设MC服务器，自己当服主权限不求人！【我的世界】",
    "url": "http://www.bilibili.com/video/av592774390",
    "source": "苏打baka",
    "published_at": "2022-01-01T15:08:21+00:00",
    "summary": "教程类视频制作不易 点个收藏随时回来学习\n投币加经验！轻松到LV6！\n喜欢的话别忘了关注苏打！\n你的支持是我更新的最大动力！\n↓↓↓↓↓视频中使用到的连接↓↓↓↓↓\nspigot核心下载：https://getbukkit.org/download/spigot\nWIKI解释：https://minecraft.fandom.com/zh/wiki/Server.properties?so=search\n文本文档中的字符：\n@echo off\njava -Xmx1g -Xms1g -jar 这里是名字.j",
    "duration_sec": 344,
    "views": 2330022,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1hMXWBSELe",
    "platform": "bilibili",
    "title": "成功让小米龙虾miclaw连接上了Google服务，mcp玩法有待开发",
    "url": "http://www.bilibili.com/video/av116293856462980",
    "source": "霜月琉依",
    "published_at": "2026-03-26T05:39:24+00:00",
    "summary": "成功让小米龙虾miclaw连接上了Google服务，mcp玩法有待开发",
    "duration_sec": 101,
    "views": 1714,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "platform": "bilibili",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-",
    "duration_sec": 100,
    "views": 10200,
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
    "views": 29467,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1GX9dYWEPw",
    "platform": "bilibili",
    "title": "我居然能在MC里玩到这么好玩的摸金服务器！",
    "url": "http://www.bilibili.com/video/av114108926068217",
    "source": "物骨",
    "published_at": "2025-03-06T21:00:00+00:00",
    "summary": "视频内容均来自《LRL服务器》\n服务器游玩方式看评论区置顶\n无需正版，不卖数值，爆率嘎嘎高，不会跑路",
    "duration_sec": 132,
    "views": 312299,
    "matched_keywords": [
      "MCP 服务器"
    ]
  },
  {
    "id": "bvid:BV1eNLn6sESA",
    "platform": "bilibili",
    "title": "28.「AI安全」Claude+Trae大模型 MCP联动 Burpsuite渗透测试",
    "url": "http://www.bilibili.com/video/av116589638846348",
    "source": "一个想当文人的黑客",
    "published_at": "2026-05-17T11:24:44+00:00",
    "summary": "内容覆盖企业SRC、众测、护网HVV行动、红蓝攻防等多场景漏洞挖掘技术，包含信息收集、XSS、SQL注入、CSRF、文件包含、文件上传、Nday框架漏洞等各类漏洞实战挖掘，渗透测试工具配置，CNVD/CVE/EDUSRC 等平台漏洞提交与证书获取，同时涵盖职业规划与护网攻防实战技巧，助力从 0 到 1 成长为赏金猎人！\n详情请看：http://8cc7.com/s9yu",
    "duration_sec": 1586,
    "views": 2915,
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
    "views": 5235,
    "matched_keywords": [
      "MCP 服务器"
    ]
  }
]
```
