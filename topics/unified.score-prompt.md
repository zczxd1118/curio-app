# Curio · 趋势雷达 · 跨域 Top 选稿

> 一次跑完整份简报：从所有领域的合并候选池里，选出 4-5 条跨域 Top 头条 + 备选池。
> 借鉴 Starfan 趋势雷达形态，每条头条含"二维表 + 主编点评"。

---

## 角色

你是 Curio 的**总编辑**——读者把"看全网"的工作交给你，你的责任是：

1. 从今天的所有候选（覆盖 AI / 金融 / 半导体 / 大厂讯息 4 个域）里**精选 4-5 条头条**
2. 每条头条按 **Starfan 二维表式**写：标题 + 引子段 + 已确认/尚属判断 + 主编点评
3. 列一份"备选池"（10-15 条标题级简单解释）

**不要分域。** 头条按重要性混编。每条标注 `[领域]` 即可。

---

## 输入（变量替换）

- 今日日期：`2026-05-31`
- 用户画像：
  ```yaml
  电子信息工程大四 + 搜狗实习生 + AI 产品 / Agent 重度玩家。
正在做 content-curator 这个个人 Agent 项目，目标是简历亮点 + 长期个人工具。
  ```
- 用户偏好：
  - 喜欢：`["vibe coding（Claude Code / Cursor / Windsurf 实战）", "AI Agent 工具构建（MCP / Skills / 子 Agent）", "AI 工程实践（RAG / 部署 / 推理优化）", "个人 Side Project 工作流", "大模型评测与发布动态"]`
  - 不喜欢：`["纯流量号、标题党", "抽象方法论、玄学论调", "概念股炒作、热点蹭文", "1 分钟短视频科普（密度太低）", "套娃合集（\"10 个最强工具\"这类）"]`
  - 信号偏好：`["要工程实践细节（具体到 commands、prompts、配置）", "要看到代码 / 示例 / 真实截图", "要\"为什么\"的解释（不只是 what，要 why）", "要新颖度（最近一周的进展优先于综述）", "长内容优先（10 分钟以上的深度内容）", "AI 领域名人访谈（行业 KOL/创业者的深度对话，比教程更稀缺）"]`
  - 阅读节奏：`工作日 30 分钟，周末 2 小时。
日报 3-5 条必读，周报 5-8 条必读，每条配 2-3 句"为什么推"。
能跳就跳，宁缺毋滥。`
- 历史反馈摘要（最近 4 周）：`[{"date": "2026-05-30", "issue": "ai/2026-05-30", "text": "想多看：AI 名人访谈 / 想少看：标题党 / 笔法：时间线很好", "applied": []}, {"date": "2026-05-30", "issue": "ai/2026-05-30", "text": "想多看：AI 名人访谈 / 想少看：标题党教程 / 笔法：时间线很好", "applied": []}, {"date": "2026-05-29", "text": "想多看 AI 领域名人访谈（不只是教程）；digest 跳过区展示太长，可以折叠/只展示前几条", "applied": ["加入 signal_preferences：\"AI 领域名人访谈\"", "explore prompt 在关键词扩展时纳入\"AI 访谈 / 对话 / 创业者\"等访谈类词", "digest 渲染：skip 区只展示前 5 条，其余只统计数字"]}]`
- 已推过的标题（避免重复）：`[]`
- **本期用户特别请求**（可能为空）：`想看一些跟ai技术相关的`
- 候选内容池（已合并所有域，每条带 `domain` 字段）：见末尾

---

## 输出格式（严格 JSON）

```json
{
  "date": "2026-05-31",
  "intro": "今日大意（80-150 字，1 段，告诉读者今天最重要的 1-2 个信号是什么，给个判断）",
  "headlines": [
    {
      "rank": 1,
      "domain": "AI",
      "id": "原候选 id",
      "url": "原候选 url",
      "source": "原 source 名",
      "stars": 5,
      "title": "事件 + 含义型标题（一句话点题，30-50 字，可保留英文产品名）",
      "lead": "150-200 字的事件引子。陈述事实+给一句判断。不要复述标题。",
      "confirmed": [
        "已确认的事实点 1（30-50 字）",
        "已确认的事实点 2",
        "已确认的事实点 3",
        "已确认的事实点 4-6（共 4-6 条）"
      ],
      "judgment": [
        "尚属判断/未明朗的点 1",
        "尚属判断的点 2",
        "尚属判断的点 3-5（共 3-5 条，与 confirmed 一一对照）"
      ],
      "implication": "这对你的含义（80-150 字主编点评，第二人称，给行动或判断建议，不要重复 lead）"
    }
  ],
  "shortlist": [
    {
      "domain": "金融",
      "title": "标题",
      "url": "url",
      "source": "source",
      "one_liner": "30-60 字一句话点评（说为什么放进备选池而不是头条）"
    }
  ]
}
```

---

## 评分规则（必读）

### 头条选择（4-5 条）
- **跨域均衡**：4 个域里至少覆盖 3 个域。如果某域今天没有"够 4 星"的，可以不选。
- **新颖度优先**：选今天/本周首发的、有数字的、有未来动作的。避免"已知信息再拼装"。
- **跨平台同事件去重**：同一个事件（如某公司 IPO）在 HN + RSS 都出现，**选英文原版/最深度的源**。
- **反偏好**：保留 0-1 条用户可能不爱看但应该看的（标 `is_diverse: true`，可选）。
- **历史反馈优先**：如果用户最近一次反馈说"想多看 X"，至少 1 条头条契合。

### 备选池（10-15 条）
- 不上头条但仍值得知晓的。
- 每条 30-60 字一句话。
- 按 domain 自然分组，先 AI、金融，再 半导体、大厂。

### 信号等级（stars 5/4/3）
- ⭐⭐⭐⭐⭐：本周必看（产业级别 / 影响 6+ 月）
- ⭐⭐⭐⭐：值得关注（影响 1-3 月 / 行业新事实）
- ⭐⭐⭐：可看可跳（增量信息）

---

## 笔法约束

- **去机翻味道**：不写"在...的背景下"、"值得我们注意的是"、"#问题"、"互联网巨头"
- **保留英文专名**：Anthropic、Claude、TSMC、OpenAI、Stratechery 等不翻
- **第二人称**：implication 段直接对读者说"你应该..."而不是"读者应当..."
- **直接说事**：每段 3 句话以内，不要堆形容词
- **数字优先**：估值、融资额、票数、增长率必须保留

---

## 用户特别请求（如有）

用户留言：

> **想看一些跟ai技术相关的**

请让 ≥1 条头条贴合。

---

## 候选池（已合并所有域）

```json
[
  {
    "id": "hn:48311647",
    "domain": "半导体",
    "title": "Claude Opus 4.8",
    "url": "https://www.anthropic.com/news/claude-opus-4-8",
    "source": "craigmart",
    "platform": "hackernews",
    "points": 1734,
    "published_at": "2026-05-28T16:49:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:48206768",
    "domain": "半导体",
    "title": "Meta blocks human rights accounts from reaching audiences in Saudi Arabia, UAE",
    "url": "https://www.alqst.org/ar/posts/1190",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 1079,
    "published_at": "2026-05-20T12:43:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:47920074",
    "domain": "半导体",
    "title": "Men who stare at walls",
    "url": "https://www.alexselimov.com/posts/men_who_stare_at_walls/",
    "source": "aselimov3",
    "platform": "hackernews",
    "points": 724,
    "published_at": "2026-04-27T11:08:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:48192383",
    "domain": "半导体",
    "title": "Show HN: Forge – Guardrails take an 8B model from 53% to 99% on agentic tasks",
    "url": "https://github.com/antoinezambelli/forge",
    "source": "zambelli",
    "platform": "hackernews",
    "points": 687,
    "published_at": "2026-05-19T12:23:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:48143880",
    "domain": "半导体",
    "title": "Mullvad exit IPs are surprisingly identifying",
    "url": "https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/",
    "source": "RGBCube",
    "platform": "hackernews",
    "points": 613,
    "published_at": "2026-05-15T02:35:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48164287",
    "domain": "半导体",
    "title": "Zerostack – A Unix-inspired coding agent written in pure Rust",
    "url": "https://crates.io/crates/zerostack/1.0.0",
    "source": "gidellav",
    "platform": "hackernews",
    "points": 575,
    "published_at": "2026-05-16T22:23:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:48184402",
    "domain": "半导体",
    "title": "Was my $48K GPU server worth it?",
    "url": "https://rosmine.ai/2026/05/13/was-my-48k-gpu-worth-it/",
    "source": "apwheele",
    "platform": "hackernews",
    "points": 568,
    "published_at": "2026-05-18T19:33:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:48191602",
    "domain": "半导体",
    "title": "Show HN: Gaussian Splat of a Strawberry",
    "url": "https://superspl.at/scene/84df8849",
    "source": "danybittel",
    "platform": "hackernews",
    "points": 529,
    "published_at": "2026-05-19T10:38:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:48259808",
    "domain": "半导体",
    "title": "Migrating from Go to Rust",
    "url": "https://corrode.dev/learn/migration-guides/go-to-rust/",
    "source": "jabits",
    "platform": "hackernews",
    "points": 477,
    "published_at": "2026-05-24T18:31:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48169874",
    "domain": "半导体",
    "title": "Show HN: Semble – Code search for agents that uses 98% fewer tokens than grep",
    "url": "https://github.com/MinishLab/semble",
    "source": "Bibabomas",
    "platform": "hackernews",
    "points": 445,
    "published_at": "2026-05-17T15:37:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:47776035",
    "domain": "半导体",
    "title": "Anna's Archive loses $322M Spotify piracy case without a fight",
    "url": "https://torrentfreak.com/annas-archive-loses-322-million-spotify-piracy-case-without-a-fight/",
    "source": "askl",
    "platform": "hackernews",
    "points": 444,
    "published_at": "2026-04-15T08:05:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:47827259",
    "domain": "半导体",
    "title": "Stop trying to engineer your way out of listening to people",
    "url": "https://ashley.rolfmore.com/stop-trying-to-engineer-your-way-out-of-listening-to-people/",
    "source": "walterbell",
    "platform": "hackernews",
    "points": 438,
    "published_at": "2026-04-19T20:09:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:48238025",
    "domain": "半导体",
    "title": "U.S. researchers face new restrictions on publishing with foreign collaborators",
    "url": "https://www.science.org/content/article/u-s-researchers-face-new-restrictions-publishing-foreign-collaborators",
    "source": "ceejayoz",
    "platform": "hackernews",
    "points": 419,
    "published_at": "2026-05-22T16:23:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48299220",
    "domain": "半导体",
    "title": "What Apple and Google are doing to push notifications",
    "url": "https://www.jacquescorbytuech.com/writing/what-apple-and-google-are-doing-your-push-notifications",
    "source": "iamacyborg",
    "platform": "hackernews",
    "points": 416,
    "published_at": "2026-05-27T19:24:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:47901064",
    "domain": "半导体",
    "title": "ASML became the chokepoint for cutting-edge chips",
    "url": "https://worksinprogress.co/issue/the-worlds-most-complex-machine/",
    "source": "mellosouls",
    "platform": "hackernews",
    "points": 416,
    "published_at": "2026-04-25T12:47:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:48206340",
    "domain": "半导体",
    "title": "Saying goodbye to asm.js",
    "url": "https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html",
    "source": "eqrion",
    "platform": "hackernews",
    "points": 410,
    "published_at": "2026-05-20T12:01:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:48307231",
    "domain": "半导体",
    "title": "AMD pulls a bait-and-switch on Linux users with Vivado licensing changes",
    "url": "https://itsfoss.com/news/amd-vivado-bait-and-switch-on-linux-users/",
    "source": "teleforce",
    "platform": "hackernews",
    "points": 336,
    "published_at": "2026-05-28T10:56:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48293080",
    "domain": "半导体",
    "title": "Incident with Pull Requests, Issues, Git Operations and API Requests",
    "url": "https://www.githubstatus.com/incidents/xy1tt3hs572m",
    "source": "maxnoe",
    "platform": "hackernews",
    "points": 335,
    "published_at": "2026-05-27T12:15:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:48165797",
    "domain": "半导体",
    "title": "I found ultra-pure quantum crystals in an abandoned mine in the Atacama desert",
    "url": "https://medium.com/@breid.at/ultra-pure-quantum-crystals-from-an-abandoned-mine-in-a-mysterious-desert-93cc87d12314",
    "source": "vi_sextus_vi",
    "platform": "hackernews",
    "points": 287,
    "published_at": "2026-05-17T03:25:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:48231247",
    "domain": "半导体",
    "title": "Gnutella: A Protocol Outliving the World That Created It",
    "url": "https://rickcarlino.com/notes/p2p/gnutella-explanation.html",
    "source": "rickcarlino",
    "platform": "hackernews",
    "points": 272,
    "published_at": "2026-05-22T02:24:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48221896",
    "domain": "半导体",
    "title": "Show HN: I Dedicated 4 Years to Mastering Offline Password Cracking",
    "url": "https://news.ycombinator.com/item?id=48221896",
    "source": "bojta-lepenye",
    "platform": "hackernews",
    "points": 268,
    "published_at": "2026-05-21T12:56:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48270111",
    "domain": "半导体",
    "title": "The bootstrapper's EU stack for under €10 per month",
    "url": "https://eualternative.eu/guides/bootstrapper-free-tier-eu-stack/",
    "source": "sparkling",
    "platform": "hackernews",
    "points": 225,
    "published_at": "2026-05-25T18:37:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:47595971",
    "domain": "半导体",
    "title": "My son pleasured himself on Gemini Live. Entire family's Google accounts banned",
    "url": "https://old.reddit.com/r/LegalAdviceUK/comments/1s92fql/my_son_pleasured_himself_in_front_of_gemini_live/",
    "source": "samlinnfer",
    "platform": "hackernews",
    "points": 208,
    "published_at": "2026-04-01T02:14:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48321076",
    "domain": "半导体",
    "title": "Real-time LLM Inference on Standard GPUs: 3k tokens/s per request",
    "url": "https://blog.kog.ai/real-time-llm-inference-on-standard-gpus-3-000-tokens-s-per-request/",
    "source": "NicoConstant",
    "platform": "hackernews",
    "points": 204,
    "published_at": "2026-05-29T09:47:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:47896163",
    "domain": "半导体",
    "title": "Show HN: I've built a nice home server OS",
    "url": "https://lightwhale.asklandd.dk/",
    "source": "Zta77",
    "platform": "hackernews",
    "points": 194,
    "published_at": "2026-04-24T21:42:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:48226038",
    "domain": "半导体",
    "title": "Chewing gum restores dad's taste and smell years after Covid",
    "url": "https://discover.swns.com/2026/05/chewing-gum-restores-dads-taste-and-smell-years-after-covid/",
    "source": "speckx",
    "platform": "hackernews",
    "points": 193,
    "published_at": "2026-05-21T17:14:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:48210590",
    "domain": "半导体",
    "title": "Ask HN: Shouldn't Google need to give a public statement about Railway incident?",
    "url": "https://news.ycombinator.com/item?id=48210590",
    "source": "srameshc",
    "platform": "hackernews",
    "points": 180,
    "published_at": "2026-05-20T16:50:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48266422",
    "domain": "半导体",
    "title": "Microsoft pulls plug on plans for 244-acre data center in Caledonia (2025)",
    "url": "https://www.tmj4.com/news/racine-county/microsoft-pulls-plug-on-plans-for-244-acre-data-center-in-caledonia-after-community-pushback",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 179,
    "published_at": "2026-05-25T13:09:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:48247005",
    "domain": "半导体",
    "title": "Matrix Multiplications on GPUs Run Faster When Given “Predictable” Data (2024)",
    "url": "https://www.thonking.ai/p/strangely-matrix-multiplications",
    "source": "tosh",
    "platform": "hackernews",
    "points": 172,
    "published_at": "2026-05-23T12:11:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:48265056",
    "domain": "半导体",
    "title": "IBM Spins Off the First Pure-Play Quantum Chip Foundry",
    "url": "https://futurumgroup.com/insights/2-billion-chips-act-investment-in-quantum-bets-on-ibms-300mm-superconducting-silicon/",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 158,
    "published_at": "2026-05-25T09:43:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:48250980",
    "domain": "半导体",
    "title": "Air France and Airbus found guilty of manslaughter over 2009 plane crash",
    "url": "https://www.bbc.com/news/articles/czd2qmdvmq6o",
    "source": "baal80spam",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-05-23T20:09:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48189539",
    "domain": "半导体",
    "title": "Fender escalates legal campaign against S-style guitars",
    "url": "https://www.guitarworld.com/gear/electric-guitars/fender-cease-and-desist-lsl-instruments",
    "source": "rectang",
    "platform": "hackernews",
    "points": 131,
    "published_at": "2026-05-19T05:28:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48012477",
    "domain": "半导体",
    "title": "Offenders sentenced up to 10 years for spying on TSMC",
    "url": "https://www.taipeitimes.com/News/front/archives/2026/04/28/2003856358",
    "source": "ironyman",
    "platform": "hackernews",
    "points": 127,
    "published_at": "2026-05-04T18:04:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48256108",
    "domain": "半导体",
    "title": "What it takes to transpose a matrix",
    "url": "https://gudok.xyz/transpose/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 105,
    "published_at": "2026-05-24T10:30:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48225040",
    "domain": "半导体",
    "title": "Launch HN: Runtime (YC P26) – Sandboxed coding agents for everyone on a team",
    "url": "https://www.runtm.com/",
    "source": "gustrigos",
    "platform": "hackernews",
    "points": 102,
    "published_at": "2026-05-21T16:07:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48234574",
    "domain": "半导体",
    "title": "How do you build a semiconductor company on something that's free?",
    "url": "https://www.siliconimist.com/p/the-open-source-silicon-business",
    "source": "johncole",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-05-22T11:49:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:48209105",
    "domain": "半导体",
    "title": "Stable Audio 3",
    "url": "https://arxiv.org/abs/2605.17991",
    "source": "guardienaveugle",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-05-20T15:10:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48007145",
    "domain": "半导体",
    "title": "ASML's Best Selling Product Isn't What You Think It Is",
    "url": "https://www.siliconimist.com/p/asmls-best-selling-product",
    "source": "johncole",
    "platform": "hackernews",
    "points": 98,
    "published_at": "2026-05-04T11:08:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:48272393",
    "domain": "半导体",
    "title": "Show HN: OpenBrief – Local-first video downloader/summarizer",
    "url": "https://github.com/tantara/openbrief",
    "source": "tantara",
    "platform": "hackernews",
    "points": 92,
    "published_at": "2026-05-25T21:50:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:48183038",
    "domain": "半导体",
    "title": "Cutting inference cold starts by 40x with LP, FUSE, C/R, and CUDA-checkpoint",
    "url": "https://modal.com/blog/truly-serverless-gpus",
    "source": "charles_irl",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-05-18T17:56:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:48041316",
    "domain": "半导体",
    "title": "Show HN: PHP-fts – Full-text search engine in pure PHP, no extensions",
    "url": "https://github.com/olivier-ls/php-fts",
    "source": "asmodios",
    "platform": "hackernews",
    "points": 89,
    "published_at": "2026-05-06T20:28:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:48265745",
    "domain": "半导体",
    "title": "GPT Guesses Between 1 and 100",
    "url": "https://github.com/exmergo/research-chatgpt-guesses-between-1-and-100",
    "source": "adunk",
    "platform": "hackernews",
    "points": 87,
    "published_at": "2026-05-25T11:46:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:48220446",
    "domain": "半导体",
    "title": "IBM invented semiconductor manufacturing automation",
    "url": "https://spectrum.ieee.org/semiconductor-fabrication",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-05-21T10:39:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:47807609",
    "domain": "半导体",
    "title": "Writing string.h functions using string instructions in asm x86-64 (2025)",
    "url": "https://pmasschelier.github.io/x86_64_strings/",
    "source": "thaisstein",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-04-17T16:22:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48037923",
    "domain": "半导体",
    "title": "Canadian fiddler sues Google after AI Overview claimed he was a sex offender",
    "url": "https://www.theguardian.com/music/2026/may/05/canadian-ashley-macisaac-fiddler-musician-singer-songwriter-sues-google-ai-sex-offender-ntwnfb",
    "source": "LordAtlas",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-05-06T16:12:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:48291230",
    "domain": "半导体",
    "title": "Nvidia Vera CPU Benchmarks: Olympus Cores Delivering Great Performance",
    "url": "https://www.phoronix.com/review/nvidia-vera-benchmarks",
    "source": "naves",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-05-27T08:15:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48261543",
    "domain": "半导体",
    "title": "San Francisco immigration court shuts down after purge of judges",
    "url": "https://apnews.com/article/san-francisco-immigration-court-closed-asylum-8a0946a7cd4bcc9bd925d075cabef44a",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 40,
    "published_at": "2026-05-24T22:12:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48327222",
    "domain": "半导体",
    "title": "AI will be used to estimate age of asylum seekers from next year",
    "url": "https://www.bbc.co.uk/news/articles/ce3pe36qe7ro",
    "source": "vylorn",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-05-29T18:23:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:48198551",
    "domain": "金融",
    "title": "Tesla's lithium refinery discharges 231,000 gallons of polluted wastewater a day",
    "url": "https://www.autonocion.com/us/tesla-lithium-refinery-texas/",
    "source": "atombender",
    "platform": "hackernews",
    "points": 498,
    "published_at": "2026-05-19T19:52:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48165980",
    "domain": "金融",
    "title": "Tesla Solar Roof is on life support as it pivot to panels",
    "url": "https://electrek.co/2026/05/14/tesla-solar-roof-promise-vs-reality-pivot-panels/",
    "source": "celsoazevedo",
    "platform": "hackernews",
    "points": 328,
    "published_at": "2026-05-17T04:09:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48108313",
    "domain": "金融",
    "title": "US inflation jumps to 3.8% as energy costs surge from Iran war",
    "url": "https://www.bbc.com/news/articles/c202pgxx89lo",
    "source": "tartoran",
    "platform": "hackernews",
    "points": 260,
    "published_at": "2026-05-12T13:51:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48236770",
    "domain": "金融",
    "title": "Launch HN: Superset (YC P26) – IDE for the agents era",
    "url": "https://github.com/superset-sh/superset",
    "source": "avipeltz",
    "platform": "hackernews",
    "points": 107,
    "published_at": "2026-05-22T14:53:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48225596",
    "domain": "金融",
    "title": "Show HN: Agent.email – sign up via curl, claim with a human OTP",
    "url": "https://news.ycombinator.com/item?id=48225596",
    "source": "adisingh13",
    "platform": "hackernews",
    "points": 98,
    "published_at": "2026-05-21T16:42:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:48309986",
    "domain": "金融",
    "title": "Show HN: Ktx – Open-source executable context layer for data agents",
    "url": "https://github.com/Kaelio/ktx",
    "source": "lucamrtl",
    "platform": "hackernews",
    "points": 83,
    "published_at": "2026-05-28T15:05:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:48160991",
    "domain": "金融",
    "title": "Tesla reveals two Robotaxi crashes involving teleoperators",
    "url": "https://techcrunch.com/2026/05/15/tesla-reveals-two-robotaxi-crashes-involving-teleoperators/",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-05-16T15:21:45+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://stratechery.com/2026/luceing-their-mind/",
    "domain": "金融",
    "title": "2026.22: Luceing Their Mind",
    "url": "https://stratechery.com/2026/luceing-their-mind/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of May 25, 2026, including why everyone hates Luce, how to monetize AI answers, and social mobility in China."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-eric-seufert-about-models-and-ads-and-ais-upside-for-humanity/",
    "domain": "金融",
    "title": "An Interview with Eric Seufert About Models and Ads, and AI’s Upside for Humanity",
    "url": "https://stratechery.com/2026/an-interview-with-eric-seufert-about-models-and-ads-and-ais-upside-for-humanity/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T10:00:00+00:00",
    "summary": "An Interview with Eric Seufert about building models for generative AI, why Meta's foundational models are so important, and why understanding advertising leads to optimism about humanity's future."
  },
  {
    "id": "rss:https://stratechery.com/2026/the-spacex-ipo-and-data-centers-in-space/",
    "domain": "金融",
    "title": "The SpaceX IPO and Data Centers in Space",
    "url": "https://stratechery.com/2026/the-spacex-ipo-and-data-centers-in-space/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-27T10:00:00+00:00",
    "summary": "There isn't a financial model that justifies the SpaceX IPO, but data centers in space are plausible, and that might be enough."
  },
  {
    "id": "rss:https://stratechery.com/2026/nvidia-earnings-the-ai-stack-nvidias-new-reporting/",
    "domain": "金融",
    "title": "Nvidia Earnings, The AI Stack, Nvidia’s New Reporting",
    "url": "https://stratechery.com/2026/nvidia-earnings-the-ai-stack-nvidias-new-reporting/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-26T10:00:00+00:00",
    "summary": "Nvidia is changing its reporting to delineate between hyperscaler sales — where Nvidia is fighting commoditization — and everyone else, where Nvidia runs the whole stack."
  },
  {
    "id": "rss:https://stratechery.com/2026/the-data-center-veto/",
    "domain": "金融",
    "title": "2026.21: The Data Center Veto",
    "url": "https://stratechery.com/2026/the-data-center-veto/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-22T17:12:32+00:00",
    "summary": "The best Stratechery content from the week of May 18, 2026, including data center discontent, agent economics, and slime mold."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-parallel-founder-parag-agarwal-about-valuing-content-on-the-agentic-web/",
    "domain": "金融",
    "title": "An Interview with Parallel Founder Parag Agarwal About Valuing Content on the Agentic Web",
    "url": "https://stratechery.com/2026/an-interview-with-parallel-founder-parag-agarwal-about-valuing-content-on-the-agentic-web/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-21T10:00:00+00:00",
    "summary": "An interview with Parallel founder Parag Agarwal about valuing content and incentivizing its creation in a world of agents (plus questions about Twitter)."
  },
  {
    "id": "rss:https://stratechery.com/2026/google-i-o-world-models-i-o-spaghetti/",
    "domain": "金融",
    "title": "Google I/O, World Models, I/O Spaghetti",
    "url": "https://stratechery.com/2026/google-i-o-world-models-i-o-spaghetti/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-20T10:00:00+00:00",
    "summary": "Google I/O put AI everywhere, for better and for worse. Meanwhile, is DeepMind aligned with Google's business objectives?"
  },
  {
    "id": "rss:https://stratechery.com/2026/data-center-discontent-understanding-the-opposition-fixing-the-problem/",
    "domain": "金融",
    "title": "Data Center Discontent, Understanding the Opposition, Fixing the Problem",
    "url": "https://stratechery.com/2026/data-center-discontent-understanding-the-opposition-fixing-the-problem/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-18T10:00:00+00:00",
    "summary": "There are understandable reasons for people to oppose data centers; the only solution that will work is simply paying them off."
  },
  {
    "id": "rss:https://stratechery.com/2026/shifting-alliances-in-a-changing-world/",
    "domain": "金融",
    "title": "2026.20: Shifting Alliances in a Changing World",
    "url": "https://stratechery.com/2026/shifting-alliances-in-a-changing-world/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-15T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of May 11, 2026, including a new kind of computing, Elon Musk, and 360 degrees of US-China relations."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-ben-thompson-at-the-moffettnathanson-media-internet-communications-conference/",
    "domain": "金融",
    "title": "An Interview with Ben Thompson at the MoffettNathanson Media, Internet & Communications Conference",
    "url": "https://stratechery.com/2026/an-interview-with-ben-thompson-at-the-moffettnathanson-media-internet-communications-conference/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-14T10:00:00+00:00",
    "summary": "An interview with me about the implications of the compute shortage on Aggregation Theory, consumer AI, and more."
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-founders-and-forward-deployed",
    "domain": "AI",
    "title": "[AINews] Founders and Forward Deployed Engineers",
    "url": "https://www.latent.space/p/ainews-founders-and-forward-deployed",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T01:57:15+00:00",
    "summary": "a quiet day lets us highlight the new AIE WF focuses"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-anthropic-raises-965b-series",
    "domain": "AI",
    "title": "[AINews] Anthropic raises $965B Series H, releases Opus 4.8 and Dynamic Workflows/ultracode",
    "url": "https://www.latent.space/p/ainews-anthropic-raises-965b-series",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T02:07:24+00:00",
    "summary": "Total Anthropic victory!"
  },
  {
    "id": "rss:https://www.latent.space/p/cognition",
    "domain": "AI",
    "title": "The Age of Async Agents — Cognition's Walden Yan & OpenInspect's Cole Murray",
    "url": "https://www.latent.space/p/cognition",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T18:41:24+00:00",
    "summary": "80% Devin Commits, Spec-to-PR Workflows, Full VMs, Agent Memory, and PMs Shipping Code"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-cognition-raises-1b-in-26b",
    "domain": "AI",
    "title": "[AINews] Cognition raises $1B in $26B Series D",
    "url": "https://www.latent.space/p/ainews-cognition-raises-1b-in-26b",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T07:26:09+00:00",
    "summary": "coding is an uncapped TAM market"
  },
  {
    "id": "rss:https://www.latent.space/p/esmfold2",
    "domain": "AI",
    "title": "🔬ESM: The Bitter Lesson is Coming for Proteins - Alex Rives, BioHub",
    "url": "https://www.latent.space/p/esmfold2",
    "source": "RJ Honicky",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-27T17:46:16+00:00",
    "summary": "Biohub&#8217;s Protein World Model: ESMC-6B, ESMFold2, 6.8B proteins, 1.1B structures, antibody design, SAEs, & the potential for programmable biology"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-new-ai-infra-decacorns-fireworks",
    "domain": "AI",
    "title": "[AINews] New AI Infra decacorns: Fireworks, Baseten (with OpenRouter on the way)",
    "url": "https://www.latent.space/p/ainews-new-ai-infra-decacorns-fireworks",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-27T03:33:53+00:00",
    "summary": "it's funding news, but it's good news."
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-all-model-labs-are-now-agent",
    "domain": "AI",
    "title": "[AINews] All Model Labs are now Agent Labs",
    "url": "https://www.latent.space/p/ainews-all-model-labs-are-now-agent",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-23T04:21:17+00:00",
    "summary": "a quiet day lets us tie together a few quotes as all model labs become agent labs"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-new-ai-infra-unicorns-exa",
    "domain": "AI",
    "title": "[AINews] New AI Infra unicorns: Exa, Modal, TurboPuffer",
    "url": "https://www.latent.space/p/ainews-new-ai-infra-unicorns-exa",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-22T05:50:58+00:00",
    "summary": "a quiet day lets us feature fundraises!"
  },
  {
    "id": "rss:https://www.latent.space/p/daytona",
    "domain": "AI",
    "title": "Giving Agents Computers — Ivan Burazin, Daytona",
    "url": "https://www.latent.space/p/daytona",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-21T20:37:40+00:00",
    "summary": "We chat with Daytona's CEO about their insane 74% MoM Growth, 850K Daily Runs, Bare Metal Sandboxes, RL Evals, and the New Agent Cloud"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-openai-gpt-next-disproves",
    "domain": "AI",
    "title": "[AINews] OpenAI GPT-next disproves 80 year old Erdős planar unit distance problem for under $1000",
    "url": "https://www.latent.space/p/ainews-openai-gpt-next-disproves",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-21T07:28:36+00:00",
    "summary": "a quiet day but a nice result in AI x mathematics"
  },
  {
    "id": "rss:https://www.latent.space/p/railway",
    "domain": "AI",
    "title": "Railway: The Agent-Native Cloud — Jake Cooper",
    "url": "https://www.latent.space/p/railway",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-20T22:42:06+00:00",
    "summary": "3M Users, 100K Signups/Week, Own-Metal Data Centers, $200K+ Coding Agent Spend, and the Death of PRs"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-google-io-2026-gemini-35-flash",
    "domain": "AI",
    "title": "[AINews] Google I/O 2026: Gemini 3.5 Flash, Omni (NanoBanana for Video), Spark (background agents), and Antigravity 2.0",
    "url": "https://www.latent.space/p/ainews-google-io-2026-gemini-35-flash",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-20T03:34:17+00:00",
    "summary": "Google has been busy!"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-how-to-land-a-job-at-a-frontier",
    "domain": "AI",
    "title": "[AINews] How to land a job at a frontier lab (on Pretraining)",
    "url": "https://www.latent.space/p/ainews-how-to-land-a-job-at-a-frontier",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-19T07:31:40+00:00",
    "summary": "a quiet day before google i/o lets us amplify a notable blogpost"
  },
  {
    "id": "rss:https://www.latent.space/p/the-fourth-law",
    "domain": "AI",
    "title": "The Autonomous Drone Tech Stack & Economics of Drones — Yaroslav Azhnyuk, The Fourth Law & Guest Host Noah Smith, Noahpinion",
    "url": "https://www.latent.space/p/the-fourth-law",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-18T13:45:32+00:00",
    "summary": "Ukrainian drone founder Yaroslav Azhnyuk went from pet cameras to AI-guided weapons. He and guest host Noah Smith make the case that the West is asleep at the wheel."
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-cerebras-60b-ipo-slowly-then",
    "domain": "AI",
    "title": "[AINews] Cerebras' $60B IPO: Slowly, then All at Once",
    "url": "https://www.latent.space/p/ainews-cerebras-60b-ipo-slowly-then",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-16T04:36:50+00:00",
    "summary": "Congrats Big Chip!"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-everything-is-conductor",
    "domain": "AI",
    "title": "[AINews] Everything is Conductor",
    "url": "https://www.latent.space/p/ainews-everything-is-conductor",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-15T00:30:21+00:00",
    "summary": "an ultra quiet day lets us highlight a smaller trend."
  },
  {
    "id": "rss:https://www.latent.space/p/abridge",
    "domain": "AI",
    "title": "AI-Native Healthcare: 100M Doctor Visits, 10–20 Hours Saved, Prior Auth in Minutes — Janie Lee & Chai Asawa, Abridge",
    "url": "https://www.latent.space/p/abridge",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-14T22:05:31+00:00",
    "summary": "How Abridge is quietly turning the patient and clinician conversation into the operating system of healthcare"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-codex-rises-claude-meters",
    "domain": "AI",
    "title": "[AINews] Codex Rises, Claude Meters Programmatic Usage",
    "url": "https://www.latent.space/p/ainews-codex-rises-claude-meters",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-14T03:53:26+00:00",
    "summary": "a quiet day lets us report on a long trend of the major coding agents"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-the-end-of-finetuning",
    "domain": "AI",
    "title": "[AINews] The End of Finetuning",
    "url": "https://www.latent.space/p/ainews-the-end-of-finetuning",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-13T02:47:22+00:00",
    "summary": "a quiet day lets us reflect on whither finetuning"
  },
  {
    "id": "rss:https://www.latent.space/p/ainews-thinking-machines-native-interaction",
    "domain": "AI",
    "title": "[AINews] Thinking Machines' Native Interaction Models - TML-Interaction-Small 276B-A12B - advances SOTA Realtime Voice and kills standard VAD",
    "url": "https://www.latent.space/p/ainews-thinking-machines-native-interaction",
    "source": "Latent.Space",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-12T04:33:46+00:00",
    "summary": "well done, Team Thinky."
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/31/anthropic-run-rate/#atom-everything",
    "domain": "AI",
    "title": "Quoting Karen Kwok for Reuters Breakingviews",
    "url": "https://simonwillison.net/2026/May/31/anthropic-run-rate/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-31T01:48:12+00:00",
    "summary": "Anthropic defines “run-rate revenue” in two parts. Use the last 28 days of sales ⁠from customers charged on a consumption basis and multiply it by 13. Then, multiply the monthly subscription take by 1"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/30/how-we-contain-claude/#atom-everything",
    "domain": "AI",
    "title": "How we contain Claude across products",
    "url": "https://simonwillison.net/2026/May/30/how-we-contain-claude/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T21:36:24+00:00",
    "summary": "How we contain Claude across products A complaint I often have about sandboxing products is that they are rarely thoroughly documented, and in the absence of detailed documentation it's hard to know h"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/30/pyodide-asgi-browser/#atom-everything",
    "domain": "AI",
    "title": "Running Python ASGI apps in the browser via Pyodide + a service worker",
    "url": "https://simonwillison.net/2026/May/30/pyodide-asgi-browser/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T21:02:16+00:00",
    "summary": "Research: Running Python ASGI apps in the browser via Pyodide + a service worker Datasette Lite is my version of Datasette that runs entirely in the browser using Pyodide in WebAssembly. When I first "
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/30/retiring-from-tech-to-live-offline/#atom-everything",
    "domain": "AI",
    "title": "I Am Retiring from Tech to Live Offline",
    "url": "https://simonwillison.net/2026/May/30/retiring-from-tech-to-live-offline/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T19:39:08+00:00",
    "summary": "I Am Retiring from Tech to Live Offline I've seen a lot of posts on forums from people threatening to quit their careers over AI. This is not one of those: Chad Whitacre is taking concrete steps, star"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/30/daniel-jalkut/#atom-everything",
    "domain": "AI",
    "title": "Quoting Daniel Jalkut",
    "url": "https://simonwillison.net/2026/May/30/daniel-jalkut/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T17:29:55+00:00",
    "summary": "My take on AI is, essentially, everybody who’s against it is too against it and everybody who’s for it is too for it. &mdash; Daniel Jalkut, via John Gruber Tags: ai, john-gruber"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/29/datasette/#atom-everything",
    "domain": "AI",
    "title": "datasette 1.0a31",
    "url": "https://simonwillison.net/2026/May/29/datasette/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T03:32:02+00:00",
    "summary": "Release: datasette 1.0a31 Another significant alpha release, with two new headline features. Datasette now offers users with the necessary permissions the ability to both execute write queries against"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/29/anthropic/#atom-everything",
    "domain": "AI",
    "title": "Anthropic's run-rate revenue hits $47 billion",
    "url": "https://simonwillison.net/2026/May/29/anthropic/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T01:23:08+00:00",
    "summary": "The most interesting thing about Anthropic's $65B Series H announcement is this line (emphasis mine): Since our Series G in February, adoption has continued to grow across global enterprise customers,"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/28/claude-opus-4-8/#atom-everything",
    "domain": "AI",
    "title": "Claude Opus 4.8: \"a modest but tangible improvement\"",
    "url": "https://simonwillison.net/2026/May/28/claude-opus-4-8/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T23:59:50+00:00",
    "summary": "Anthropic shipped Claude Opus 4.8 today. My favourite thing about it is this note in the release announcement: Users will find Opus 4.8 to be a modest but tangible improvement on its predecessor. Ther"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/28/llm-anthropic/#atom-everything",
    "domain": "AI",
    "title": "llm-anthropic 0.25.1",
    "url": "https://simonwillison.net/2026/May/28/llm-anthropic/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T23:54:56+00:00",
    "summary": "Release: llm-anthropic 0.25.1 New model: Claude Opus 4.8 (claude-opus-4.8). New -o fast 1 option for fast mode, for organizations with that feature enabled on their account. Default max_tokens for eac"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/28/markdown-svg-renderer/#atom-everything",
    "domain": "AI",
    "title": "markdown-svg-renderer",
    "url": "https://simonwillison.net/2026/May/28/markdown-svg-renderer/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T19:45:14+00:00",
    "summary": "Tool: markdown-svg-renderer A slightly customized Markdown rendering tool with special treatment for fenced code SVG blocks - it both renders the image and provides a tab for switching to the code vie"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/27/sqlite-agents/#atom-everything",
    "domain": "AI",
    "title": "sqlite AGENTS.md",
    "url": "https://simonwillison.net/2026/May/27/sqlite-agents/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-27T23:44:37+00:00",
    "summary": "sqlite AGENTS.md SQLite gained an AGENTS.md file five days ago - but it's not intended for their own development, it's presumably aimed at people who are pointing agents at the SQLite codebase. It inc"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/27/product-market-fit/#atom-everything",
    "domain": "AI",
    "title": "I think Anthropic and OpenAI have found product-market fit",
    "url": "https://simonwillison.net/2026/May/27/product-market-fit/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-27T16:38:35+00:00",
    "summary": "Anthropic are strongly rumored to be about to have their first profitable quarter. Stories are circulating of companies surprised at how expensive their LLM bills are becoming from usage by their staf"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/27/kyle-ferrana/#atom-everything",
    "domain": "AI",
    "title": "Quoting Kyle Ferrana",
    "url": "https://simonwillison.net/2026/May/27/kyle-ferrana/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-27T06:41:43+00:00",
    "summary": "PICARD: Data, shields up DATA: Brilliant! Shields can reduce damage we sustain. Not immunity. Not hubris. Just prudence. It's not precaution—it's strategy. [camera shakes] WORF: HULL BREACHES ON NINE "
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/26/the-pressure/#atom-everything",
    "domain": "AI",
    "title": "The pressure",
    "url": "https://simonwillison.net/2026/May/26/the-pressure/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-26T23:48:45+00:00",
    "summary": "The pressure Daniel Stenberg on the unprecedented level of pressure the curl team are facing right now thanks to the deluge of (credible) AI-assisted security issues being reported. The rate of incomi"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything",
    "domain": "AI",
    "title": "Microsoft Copilot Cowork Exfiltrates Files",
    "url": "https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-26T15:36:48+00:00",
    "summary": "Microsoft Copilot Cowork Exfiltrates Files The biggest challenge in designing agentic systems continues to be preventing them from enabling attackers to exfiltrate data. In this case Microsoft Copilot"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/26/paul-graham/#atom-everything",
    "domain": "AI",
    "title": "Quoting Paul Graham",
    "url": "https://simonwillison.net/2026/May/26/paul-graham/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-26T15:02:30+00:00",
    "summary": "A lot of the emails I get from founders are now written in a hard-hitting journalistic style. I know they're written by AI, because no founder ever wrote this way before. And once you realize somethin"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/26/corey-quinn/#atom-everything",
    "domain": "AI",
    "title": "Quoting Corey Quinn",
    "url": "https://simonwillison.net/2026/May/26/corey-quinn/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-26T02:28:54+00:00",
    "summary": "I cannot believe I'm saying this, but getting the literal Pope to canonize your product's specific technical limitations as a spiritual treatise is the single greatest act of vendor lobbying I have ev"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/25/encyclical-on-ai/#atom-everything",
    "domain": "AI",
    "title": "Notes on Pope Leo XIV's encyclical on AI",
    "url": "https://simonwillison.net/2026/May/25/encyclical-on-ai/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-25T23:58:17+00:00",
    "summary": "Dropped this morning by the Vatican: Magnifica Humanitas of His Holiness Pope Leo XIV on Safeguarding the Human Person in the Time of Artificial Intelligence. This is a very interesting document. It's"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/25/sighting-365297287/#atom-everything",
    "domain": "AI",
    "title": "California Brown Pelican, Snowy Egret, California Sea Lion, Harbor Seal",
    "url": "https://simonwillison.net/2026/May/25/sighting-365297287/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-25T23:08:00+00:00",
    "summary": "California Brown Pelican, Snowy Egret, California Sea Lion, Harbor Seal, in San Mateo County, CA, USWe took our new folding kayak out in the harbor and saw sea lions and harbor seals chilling on the d"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/24/datasette/#atom-everything",
    "domain": "AI",
    "title": "datasette 1.0a30",
    "url": "https://simonwillison.net/2026/May/24/datasette/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-24T23:52:37+00:00",
    "summary": "Release: datasette 1.0a30 The big new feature in this alpha is a new customizable \"Jump to...\" menu, described in detail in The extensible \"Jump to\" menu in Datasette 1.0a30 on the Datasette blog. You"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/24/datasette-agent/#atom-everything",
    "domain": "AI",
    "title": "datasette-agent 0.1a4",
    "url": "https://simonwillison.net/2026/May/24/datasette-agent/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-24T23:19:34+00:00",
    "summary": "Release: datasette-agent 0.1a4 Taking advantage of the new makeJumpSections() JavaScript plugin hook added in Datasette 1.0a30, datasette-agent now presents this \"Start a new agent chat\" interface as "
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/24/datasette-fixtures/#atom-everything",
    "domain": "AI",
    "title": "datasette-fixtures 0.1a0",
    "url": "https://simonwillison.net/2026/May/24/datasette-fixtures/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-24T21:38:32+00:00",
    "summary": "Release: datasette-fixtures 0.1a0 One of the smaller features in Datasette 1.0a30 is this: New documented datasette.fixtures.populate_fixture_database(conn) helper for creating the fixture database ta"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/24/armin-ronacher/#atom-everything",
    "domain": "AI",
    "title": "Quoting Armin Ronacher",
    "url": "https://simonwillison.net/2026/May/24/armin-ronacher/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-24T18:46:53+00:00",
    "summary": "The most frustrating failure mode right now is that people submit issues that are not in their own voice. They contain an observed problem somewhere, but it has been thrown into a clanker and the clan"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/24/usborne-mad-house/#atom-everything",
    "domain": "AI",
    "title": "Mad House — Usborne Creepy Computer Games",
    "url": "https://simonwillison.net/2026/May/24/usborne-mad-house/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-24T17:14:11+00:00",
    "summary": "Tool: Mad House — Usborne Creepy Computer Games Via Hacker News I learned that UK publisher Usborne published free PDFs of their 1980s Computer Books, some of which I remember working through on my Co"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/23/on-the-dl/#atom-everything",
    "domain": "AI",
    "title": "On the",
    "url": "https://simonwillison.net/2026/May/23/on-the-dl/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-23T20:24:48+00:00",
    "summary": "On the &lt;dl&gt; I learned a few new-to-me things about the &lt;dl&gt; element from this article by Ben Meyer: A &lt;dt&gt; can be followed by multiple &lt;dd&gt; You can optionally group the &lt;dt&"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/22/memory-shortage/#atom-everything",
    "domain": "AI",
    "title": "The memory shortage is causing a repricing of consumer electronics",
    "url": "https://simonwillison.net/2026/May/22/memory-shortage/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-22T22:01:31+00:00",
    "summary": "The memory shortage is causing a repricing of consumer electronics David Oks provides the clearest explanation I've seen yet of why consumer products that use memory are likely to get significantly mo"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/22/ftc-active-listening/#atom-everything",
    "domain": "AI",
    "title": "FTC to Require Cox Media Group, Two Other Firms to Pay Nearly $1 Million to Settle Charges They Deceived Customers About “Active Listening” AI-Powered Marketing Service",
    "url": "https://simonwillison.net/2026/May/22/ftc-active-listening/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-22T04:48:32+00:00",
    "summary": "FTC to Require Cox Media Group, Two Other Firms to Pay Nearly $1 Million to Settle Charges They Deceived Customers About “Active Listening” AI-Powered Marketing Service Back in 2024 Cox Media Group we"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/21/datasette-agent/#atom-everything",
    "domain": "AI",
    "title": "Datasette Agent",
    "url": "https://simonwillison.net/2026/May/21/datasette-agent/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-21T19:52:19+00:00",
    "summary": "We just announced the first release of Datasette Agent, a new extensible AI assistant for Datasette. I've been working on my LLM Python library for just over three years now, and Datasette Agent repre"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/21/datasette-agent-sprites/#atom-everything",
    "domain": "AI",
    "title": "datasette-agent-sprites 0.1a0",
    "url": "https://simonwillison.net/2026/May/21/datasette-agent-sprites/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-21T18:21:07+00:00",
    "summary": "Release: datasette-agent-sprites 0.1a0 A Datasette Agent plugin for running commands in a Fly Sprites sandbox. Tags: sandboxing, datasette, fly, datasette-agent"
  },
  {
    "id": "rss:https://simonwillison.net/2026/May/21/datasette-agent-charts/#atom-everything",
    "domain": "AI",
    "title": "datasette-agent-charts 0.1a2",
    "url": "https://simonwillison.net/2026/May/21/datasette-agent-charts/#atom-everything",
    "source": "Simon Willison's Weblog",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-21T15:15:58+00:00",
    "summary": "Release: datasette-agent-charts 0.1a2 \"View SQL query\" buttons below rendered charts. Tags: datasette, datasette-agent"
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/ai-native-engineering-leadership",
    "domain": "AI",
    "title": "AI-Native Engineering Leadership",
    "url": "https://newsletter.eng-leadership.com/p/ai-native-engineering-leadership",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T07:42:51+00:00",
    "summary": "Important trends and how to become a great engineering leader in 2026 and beyond."
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/updated-speaker-lineup-engineering",
    "domain": "AI",
    "title": "Engineering Leadership LIVE Event in San Francisco",
    "url": "https://newsletter.eng-leadership.com/p/updated-speaker-lineup-engineering",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-25T18:35:56+00:00",
    "summary": "Updated speaker lineup for the Engineering Leadership Live event in San Francisco, that I am hosting together with my friends from Augment Code."
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/how-to-use-critical-chain-methodology",
    "domain": "AI",
    "title": "How to Finish Engineering Projects Early Without Added Stress",
    "url": "https://newsletter.eng-leadership.com/p/how-to-use-critical-chain-methodology",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-24T16:46:14+00:00",
    "summary": "A real-world case study on using the critical chain methodology to finish projects early without added stress."
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/full-speaker-lineup-engineering-leadership",
    "domain": "AI",
    "title": "Full Speaker Lineup: Engineering Leadership LIVE Event in San Francisco",
    "url": "https://newsletter.eng-leadership.com/p/full-speaker-lineup-engineering-leadership",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-21T20:30:59+00:00",
    "summary": "Full speaker lineup for the Engineering Leadership Live event in San Francisco, that I am hosting together with my friends from Augment Code."
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/how-to-build-narrative-around-your",
    "domain": "AI",
    "title": "How to Build a Narrative Around Your Work",
    "url": "https://newsletter.eng-leadership.com/p/how-to-build-narrative-around-your",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-21T06:42:34+00:00",
    "summary": "The highest-impact people are not only great operators but also strong storytellers. This is how to build a story around your work!"
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/how-to-avoid-ai-code-slop",
    "domain": "AI",
    "title": "How to Avoid AI Code Slop",
    "url": "https://newsletter.eng-leadership.com/p/how-to-avoid-ai-code-slop",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-17T16:50:06+00:00",
    "summary": "AI can generate code faster than ever, but it can also scale technical debt faster than ever! Learn the practical strategies to optimize the AI-generated output."
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/how-to-manage-your-time-as-a-first",
    "domain": "AI",
    "title": "How to Manage Your Time as a First-Time Lead",
    "url": "https://newsletter.eng-leadership.com/p/how-to-manage-your-time-as-a-first",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-14T09:30:57+00:00",
    "summary": "Practical strategies to protect your time, avoid burnout, and lead your team effectively."
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/how-to-use-ai-to-onboard-into-a-codebase",
    "domain": "AI",
    "title": "How to Use AI to Onboard Into a Codebase Faster",
    "url": "https://newsletter.eng-leadership.com/p/how-to-use-ai-to-onboard-into-a-codebase",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-10T14:51:16+00:00",
    "summary": "4 onboarding steps to speed up your understanding of a codebase and get you up and running in a few hours!"
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/companies-should-allow-ai-usage-in",
    "domain": "AI",
    "title": "Removing AI in Tech Interviews is Wrong",
    "url": "https://newsletter.eng-leadership.com/p/companies-should-allow-ai-usage-in",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-07T10:06:16+00:00",
    "summary": "AI-assisted engineering is already the standard, and technical interviews should reflect how modern software is actually built."
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/engineering-leadership-live-event",
    "domain": "AI",
    "title": "Engineering Leadership LIVE Event in San Francisco",
    "url": "https://newsletter.eng-leadership.com/p/engineering-leadership-live-event",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-04T15:58:47+00:00",
    "summary": "Together with my friends from Augment Code, we are hosting a live event in San Francisco on May 26th!"
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/how-to-thrive-as-an-em-in-the-ai",
    "domain": "AI",
    "title": "How to Thrive as an EM in the AI Era",
    "url": "https://newsletter.eng-leadership.com/p/how-to-thrive-as-an-em-in-the-ai",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-03T17:24:14+00:00",
    "summary": "Case study from The Multiplier Mindset: How to Move from Senior Engineer to Tech Leader in the AI Era"
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/should-you-become-a-forward-deployed",
    "domain": "AI",
    "title": "Should You Become a Forward Deployed Engineer?",
    "url": "https://newsletter.eng-leadership.com/p/should-you-become-a-forward-deployed",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-30T10:35:06+00:00",
    "summary": "What do FDEs at Salesforce, OpenAI, and Palantir really do, and should you become one?"
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/salesforce-is-going-all-in-on-ai",
    "domain": "AI",
    "title": "3 Key AI Trends and How Salesforce Engineers use AI",
    "url": "https://newsletter.eng-leadership.com/p/salesforce-is-going-all-in-on-ai",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-27T10:12:14+00:00",
    "summary": "Recap from the Salesforce TDX 2026: AI Agents, 3 key AI trends and how engineers use AI."
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/the-differences-between-us-and-eu",
    "domain": "AI",
    "title": "The Differences Between US and EU Tech Companies",
    "url": "https://newsletter.eng-leadership.com/p/the-differences-between-us-and-eu",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-23T07:49:48+00:00",
    "summary": "One optimizes for speed and innovation, and the other optimizes for stability and sustainability. Which is the way to go?"
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/how-an-ai-native-startup-from-sf",
    "domain": "AI",
    "title": "How an AI-Native Startup From SF Works and Builds Its Product",
    "url": "https://newsletter.eng-leadership.com/p/how-an-ai-native-startup-from-sf",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-20T01:21:54+00:00",
    "summary": "An insider's look into the workflows, tools, and culture powering a modern AI-first engineering team."
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/become-a-great-generalist-or-extreme",
    "domain": "AI",
    "title": "Become a Great Generalist or Extreme Specialist",
    "url": "https://newsletter.eng-leadership.com/p/become-a-great-generalist-or-extreme",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-16T09:09:40+00:00",
    "summary": "Should you become a great generalist or an extreme specialist? One thing is clear: staying in the middle will result in fewer opportunities."
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/code-review-is-the-new-bottleneck",
    "domain": "AI",
    "title": "Code Review is the New Bottleneck For Engineering Teams",
    "url": "https://newsletter.eng-leadership.com/p/code-review-is-the-new-bottleneck",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-13T04:09:59+00:00",
    "summary": "Building is now limited to how fast we are able to review the newly generated code. This is what to do in order to make it less of a bottleneck."
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/meta-created-an-internal-leaderboard",
    "domain": "AI",
    "title": "Meta Created an Internal Leaderboard on AI Token Usage",
    "url": "https://newsletter.eng-leadership.com/p/meta-created-an-internal-leaderboard",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-09T04:22:14+00:00",
    "summary": "This seems to be a part of the broader trend in Silicon Valley called \"tokenmaxxing\". Here's what's happening."
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/how-to-use-openclaw-as-an-engineering",
    "domain": "AI",
    "title": "How to Use OpenClaw as an Engineering Leader",
    "url": "https://newsletter.eng-leadership.com/p/how-to-use-openclaw-as-an-engineering",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-05T22:36:25+00:00",
    "summary": "I recently tried OpenClaw and did 3 test projects. This is how you can get started with it and how it can help you!"
  },
  {
    "id": "rss:https://newsletter.eng-leadership.com/p/would-i-still-go-the-engineering",
    "domain": "AI",
    "title": "Would I Still Go The Engineering Manager Route in 2026?",
    "url": "https://newsletter.eng-leadership.com/p/would-i-still-go-the-engineering",
    "source": "Gregor Ojstersek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-02T03:52:08+00:00",
    "summary": "Engineering management has changed. Here are my thoughts if I were a senior software engineer again, thinking of my next step."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-doordash-built-a-testing-system",
    "domain": "AI",
    "title": "How DoorDash Built a Testing System to Evaluate LLMs",
    "url": "https://blog.bytebytego.com/p/how-doordash-built-a-testing-system",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-30T15:30:52+00:00",
    "summary": "In this article, we will learn how they built this flywheel and the key takeaways."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/must-know-failure-modes-in-distributed",
    "domain": "AI",
    "title": "Must-Know Failure Modes in Distributed Systems",
    "url": "https://blog.bytebytego.com/p/must-know-failure-modes-in-distributed",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-28T16:31:00+00:00",
    "summary": "In this article, we will look at the most significant failure mode patterns in distributed systems and the standard approaches to deal with each of them."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-airtable-built-the-search-layer",
    "domain": "AI",
    "title": "How Airtable Built the Search Layer Behind Their AI Features",
    "url": "https://blog.bytebytego.com/p/how-airtable-built-the-search-layer",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-27T15:30:43+00:00",
    "summary": "In this article, we will look at how Airtable&#8217;s data infrastructure team built its architecture, the challenges they faced, the tradeoffs they accepted, and why the choices they made only make s"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-vercel-cut-build-wait-times-from",
    "domain": "AI",
    "title": "How Vercel Cut Build Wait Times From 90 Seconds To 5",
    "url": "https://blog.bytebytego.com/p/how-vercel-cut-build-wait-times-from",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-26T15:31:10+00:00",
    "summary": "In this article, we examine the constraints Vercel faced, the choices they made in response, and the optimizations that produced the speedup."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-cockroachdb-built-vector-indexing",
    "domain": "AI",
    "title": "How CockroachDB Built Vector Indexing at Scale",
    "url": "https://blog.bytebytego.com/p/how-cockroachdb-built-vector-indexing",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-25T15:30:38+00:00",
    "summary": "In this article, we will look at how the CockroachDB engineering team built this index and the challenges they faced."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/ep216-rags-vs-agents",
    "domain": "AI",
    "title": "EP216: RAGs vs Agents",
    "url": "https://blog.bytebytego.com/p/ep216-rags-vs-agents",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-23T15:31:18+00:00",
    "summary": "Ask an LLM about your company's data and it will guess. The two patterns that fix this are RAG and agents, and they solve different problems."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/build-with-claude-code-new-cohort",
    "domain": "AI",
    "title": "Build with Claude Code: New Cohort Launch",
    "url": "https://blog.bytebytego.com/p/build-with-claude-code-new-cohort",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-22T15:31:20+00:00",
    "summary": "The first cohort starts in about a week: May 28-29, 2026."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/a-guide-to-async-patterns-in-api",
    "domain": "AI",
    "title": "A Guide to Async Patterns in API Design",
    "url": "https://blog.bytebytego.com/p/a-guide-to-async-patterns-in-api",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-21T15:30:24+00:00",
    "summary": "In this article, we will look at each of these patterns in detail, along with their advantages."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-netflix-is-using-multimodal-ai",
    "domain": "AI",
    "title": "How Netflix is Using Multimodal AI to Power Video Search",
    "url": "https://blog.bytebytego.com/p/how-netflix-is-using-multimodal-ai",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-20T15:31:07+00:00",
    "summary": "In this article, we will understand how Netflix built this system and the challenges it faced."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-snapchat-serves-a-billion-predictions",
    "domain": "AI",
    "title": "How Snapchat Serves a Billion Predictions Per Second",
    "url": "https://blog.bytebytego.com/p/how-snapchat-serves-a-billion-predictions",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-19T15:31:28+00:00",
    "summary": "For Snap, machine learning is closer to the product itself than a feature on top of it."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-grab-is-using-ai-agents-to-boost",
    "domain": "AI",
    "title": "How Grab is Using AI Agents to Boost Team Productivity",
    "url": "https://blog.bytebytego.com/p/how-grab-is-using-ai-agents-to-boost",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-18T15:31:16+00:00",
    "summary": "Grab&#8217;s data engineering team had a problem that looks familiar to anyone who&#8217;s maintained shared infrastructure."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/ep215-the-anatomy-of-an-ai-agent",
    "domain": "AI",
    "title": "EP215: The Anatomy of an AI Agent",
    "url": "https://blog.bytebytego.com/p/ep215-the-anatomy-of-an-ai-agent",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-16T15:31:01+00:00",
    "summary": "An AI agent can be thought of as a simple While-loop."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/last-call-for-enrollment-become-an-a88",
    "domain": "AI",
    "title": "LAST CALL FOR ENROLLMENT: Become an AI Engineer - Cohort 6",
    "url": "https://blog.bytebytego.com/p/last-call-for-enrollment-become-an-a88",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-15T15:02:20+00:00",
    "summary": "Our 6th cohort of Becoming an AI Engineer starts tomorrow, Saturday, May 16. This is a live, cohort-based course created in collaboration with best-selling author Ali Aminian and published by ByteByte"
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/a-guide-to-event-driven-architectural",
    "domain": "AI",
    "title": "A Guide To Event-Driven Architectural Patterns",
    "url": "https://blog.bytebytego.com/p/a-guide-to-event-driven-architectural",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-14T15:32:28+00:00",
    "summary": "Distributed systems are built out of services that need to communicate, and the simplest way to do that is for one service to call another directly and wait for a response."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/high-performance-rate-limiting-at",
    "domain": "AI",
    "title": "High Performance Rate Limiting at Databricks",
    "url": "https://blog.bytebytego.com/p/high-performance-rate-limiting-at",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-13T15:30:35+00:00",
    "summary": "In this article, we look at how Databricks implemented rate limiting at scale, how they shrank the critical path, and the accuracy tradeoff that shrinking usually requires."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-figma-upgraded-data-pipeline",
    "domain": "AI",
    "title": "How Figma Upgraded Data Pipeline from Multi-Day Latency to Real-Time",
    "url": "https://blog.bytebytego.com/p/how-figma-upgraded-data-pipeline",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-12T15:31:03+00:00",
    "summary": "In this article, we will learn what happened as Figma grew and how its engineering team handled the growth in terms of the data pipeline issues."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/how-pinterest-built-a-production",
    "domain": "AI",
    "title": "How Pinterest Built a Production MCP Ecosystem",
    "url": "https://blog.bytebytego.com/p/how-pinterest-built-a-production",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-11T15:31:17+00:00",
    "summary": "In this article, we look at how Pinterest designed that ecosystem and what they had to get right beyond the protocol itself."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/ep214-claude-code-vs-openclaw-5-design",
    "domain": "AI",
    "title": "EP214: Claude Code vs. OpenClaw: 5 Design Dimensions",
    "url": "https://blog.bytebytego.com/p/ep214-claude-code-vs-openclaw-5-design",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-09T15:31:10+00:00",
    "summary": "Both are highly capable, but they have key architectural differences."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/enrollment-ends-soon-become-an-ai",
    "domain": "AI",
    "title": "Become an AI Engineer | Enrollment Ends Soon",
    "url": "https://blog.bytebytego.com/p/enrollment-ends-soon-become-an-ai",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-08T15:31:40+00:00",
    "summary": "Our 6th cohort of Becoming an AI Engineer starts in about a week."
  },
  {
    "id": "rss:https://blog.bytebytego.com/p/container-design-patterns-for-distributed",
    "domain": "AI",
    "title": "Container Design Patterns for Distributed Systems",
    "url": "https://blog.bytebytego.com/p/container-design-patterns-for-distributed",
    "source": "ByteByteGo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-07T15:31:08+00:00",
    "summary": "In this article, we&#8217;ll walk through the patterns that have crystallized over the past decade, organized by the scope of their coordination."
  },
  {
    "id": "hn:48238896",
    "domain": "AI",
    "title": "Microsoft starts canceling Claude Code licenses",
    "url": "https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad",
    "source": "robertkarl",
    "platform": "hackernews",
    "points": 492,
    "published_at": "2026-05-22T17:32:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:48289950",
    "domain": "AI",
    "title": "Claude Code as a Daily Driver: Claude.md, Skills, Subagents, Plugins, and MCPs",
    "url": "https://arps18.github.io/posts/claude-code-mastery/",
    "source": "arps18",
    "platform": "hackernews",
    "points": 439,
    "published_at": "2026-05-27T05:13:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48318174",
    "domain": "AI",
    "title": "Claude Code – Everything you can configure that the docs don't tell you",
    "url": "https://buildingbetter.tech/p/i-read-the-claude-code-source-code",
    "source": "ankitg12",
    "platform": "hackernews",
    "points": 326,
    "published_at": "2026-05-29T02:13:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48311705",
    "domain": "AI",
    "title": "Dynamic Workflows in Claude Code",
    "url": "https://claude.com/blog/introducing-dynamic-workflows-in-claude-code",
    "source": "mil22",
    "platform": "hackernews",
    "points": 189,
    "published_at": "2026-05-28T16:52:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48267432",
    "domain": "AI",
    "title": "Why Ctrl+V won't paste images in Claude Code on WSL, with a fix",
    "url": "https://rajveerbachkaniwala.com/blog/2026/05/24/on-the-difficulty-of-pasting-a-picture/",
    "source": "rajveerb",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-05-25T14:41:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:48322956",
    "domain": "AI",
    "title": "Show HN: AISlop, a CLI for catching AI generated code smells",
    "url": "https://github.com/scanaislop/aislop",
    "source": "Heavykenny",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-05-29T13:37:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:48221805",
    "domain": "AI",
    "title": "Show HN: I Made a Claude Skill for Spec-Driven Development (SDD)",
    "url": "https://github.com/FredAntB/Spec-Driven-Development",
    "source": "NTRIXLM",
    "platform": "hackernews",
    "points": 40,
    "published_at": "2026-05-21T12:49:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:48205415",
    "domain": "AI",
    "title": "Learnings from 100K lines of Rust with AI (2025)",
    "url": "https://zfhuang99.github.io/rust/claude%20code/codex/contracts/spec-driven%20development/2025/12/01/rust-with-ai.html",
    "source": "pramodbiligiri",
    "platform": "hackernews",
    "points": 192,
    "published_at": "2026-05-20T10:04:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:48174465",
    "domain": "AI",
    "title": "Reverse engineering Android malware from popular Chinese projectors",
    "url": "https://zanestjohn.com/blog/reing-with-claude-code",
    "source": "3abiton",
    "platform": "hackernews",
    "points": 89,
    "published_at": "2026-05-18T00:36:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48182516",
    "domain": "AI",
    "title": "Cursor Introduces Composer 2.5",
    "url": "https://cursor.com/blog/composer-2-5",
    "source": "asar",
    "platform": "hackernews",
    "points": 290,
    "published_at": "2026-05-18T17:20:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:48308376",
    "domain": "AI",
    "title": "Show HN: Continue? Y/N: A 60-second game about AI agent permission fatigue",
    "url": "https://llmgame.scalex.dev",
    "source": "Wirbelwind",
    "platform": "hackernews",
    "points": 380,
    "published_at": "2026-05-28T13:02:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:48326659",
    "domain": "AI",
    "title": "Robinhood now lets your AI agents trade stocks",
    "url": "https://techcrunch.com/2026/05/27/robinhood-now-lets-your-ai-agents-trade-stocks/",
    "source": "wapasta",
    "platform": "hackernews",
    "points": 109,
    "published_at": "2026-05-29T17:46:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:48208685",
    "domain": "AI",
    "title": "Testing distributed systems with AI agents",
    "url": "https://github.com/shenli/distributed-system-testing",
    "source": "shenli3514",
    "platform": "hackernews",
    "points": 96,
    "published_at": "2026-05-20T14:40:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48324910",
    "domain": "AI",
    "title": "CAPTCHAs can still detect AI agents",
    "url": "https://research.roundtable.ai/captchas-detect-ai/",
    "source": "timshell",
    "platform": "hackernews",
    "points": 83,
    "published_at": "2026-05-29T15:57:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48319968",
    "domain": "AI",
    "title": "Undisclosed addition in jqwik instructed AI coding agents to delete app output",
    "url": "https://arstechnica.com/security/2026/05/fed-up-with-vibe-coders-dev-sneaks-data-nuking-prompt-injection-into-their-code/",
    "source": "joozio",
    "platform": "hackernews",
    "points": 61,
    "published_at": "2026-05-29T07:05:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:48183301",
    "domain": "AI",
    "title": "We let AIs run radio stations",
    "url": "https://andonlabs.com/blog/andon-fm",
    "source": "lukaspetersson",
    "platform": "hackernews",
    "points": 374,
    "published_at": "2026-05-18T18:12:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48230104",
    "domain": "AI",
    "title": "Tell HN: I'm tired of AI-generated answers",
    "url": "https://news.ycombinator.com/item?id=48230104",
    "source": "theorchid",
    "platform": "hackernews",
    "points": 120,
    "published_at": "2026-05-21T23:37:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:48181342",
    "domain": "AI",
    "title": "Show HN: InsForge – Open-source Heroku for coding agents",
    "url": "https://github.com/InsForge/InsForge",
    "source": "mrcoldbrew",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-05-18T15:40:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48244434",
    "domain": "AI",
    "title": "Microsoft reports AI is more expensive than paying human employees",
    "url": "https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/",
    "source": "nreece",
    "platform": "hackernews",
    "points": 229,
    "published_at": "2026-05-23T03:44:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:48205626",
    "domain": "AI",
    "title": "Qwen3.7-Max: The Agent Frontier",
    "url": "https://qwen.ai/blog?id=qwen3.7",
    "source": "kevinsimper",
    "platform": "hackernews",
    "points": 721,
    "published_at": "2026-05-20T10:35:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48209323",
    "domain": "AI",
    "title": "Formal Verification Gates for AI Coding Loops",
    "url": "https://reubenbrooks.dev/blog/structural-backpressure-beats-smarter-agents/",
    "source": "pyrex41",
    "platform": "hackernews",
    "points": 144,
    "published_at": "2026-05-20T15:25:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48284939",
    "domain": "AI",
    "title": "DeepSWE: A contamination-free benchmark for long-horizon coding agents",
    "url": "https://deepswe.datacurve.ai/blog",
    "source": "ammar_x",
    "platform": "hackernews",
    "points": 65,
    "published_at": "2026-05-26T19:40:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:48037128",
    "domain": "AI",
    "title": "Vibe coding and agentic engineering are getting closer than I'd like",
    "url": "https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/",
    "source": "e12e",
    "platform": "hackernews",
    "points": 787,
    "published_at": "2026-05-06T15:06:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48335640",
    "domain": "AI",
    "title": "Vibe Coding Is Not Engineering",
    "url": "https://phroneses.com/articles/build/notes/vibe-coding-is-not-engineering.html",
    "source": "jhevans",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-05-30T12:53:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:48148601",
    "domain": "AI",
    "title": "Show HN: Vibe Coding a $20k /Year Enterprise Logistics Platform",
    "url": "https://trmnl.com/blog/vibe-coding-shiphero",
    "source": "ryanckulp",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-05-15T13:51:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48219901",
    "domain": "AI",
    "title": "Managers Have Been Vibe Coding All Along",
    "url": "https://yusufaytas.com/managers-have-been-vibe-coding-all-along",
    "source": "wyajmd",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-05-21T09:19:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:48056267",
    "domain": "AI",
    "title": "Show HN: Blamo A vibecoded app for vibecoding vibe games",
    "url": "https://www.blamo.ai/",
    "source": "semateos",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-05-07T23:06:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:47998601",
    "domain": "AI",
    "title": "Uncle Bob: It's Over",
    "url": "https://old.reddit.com/r/vibecoding/comments/1srfqm0/uncle_bob_its_over/",
    "source": "lopespm",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-05-03T16:29:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:48012681",
    "domain": "AI",
    "title": "Usage-based pricing killing your vibe, here's how to roll your own local AI",
    "url": "https://www.theregister.com/2026/05/02/local_ai_coding_agents/",
    "source": "Bender",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-05-04T18:19:04+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 156526,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 13340,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1jsV861EVM",
    "domain": "AI",
    "title": "【2026胎教级】Claude Code全栈教程，从入门到精通，搞定所有开发场景，小白10分钟搞定，全程干货无废话，存下吧，很难找全的！",
    "url": "http://www.bilibili.com/video/av116657502687649",
    "source": "程序员黑梦",
    "platform": "bilibili",
    "points": 10377,
    "published_at": "2026-05-29T11:08:50+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1NYVG6jEKE",
    "domain": "AI",
    "title": "Claude Code保姆级在国内从安装到代码实战教程，10分钟入门精通",
    "url": "http://www.bilibili.com/video/av116662133132089",
    "source": "字节软件测试",
    "platform": "bilibili",
    "points": 8868,
    "published_at": "2026-05-30T06:39:27+00:00",
    "summary": "Claude Code保姆级在国内从安装到代码实战教程，10分钟入门精通"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 4239,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1JUGb6jEny",
    "domain": "AI",
    "title": "90% 的人都没用对 Claude Code，Claude Code 的高阶玩法都在这",
    "url": "http://www.bilibili.com/video/av116618998912532",
    "source": "程序员Shark",
    "platform": "bilibili",
    "points": 2178,
    "published_at": "2026-05-22T15:46:55+00:00",
    "summary": "为了做了精心的翻译和校对，原文：https://www.youtube.com/watch?v=uogzSxOw4LU，再次感谢作者。\n概要：这部分内容真正想讲的，不是 Claude Code 又多了几个新功能，而是怎么把它用成一套顺手的开发工具。很多人一开始只是拿它来聊天，但真想把效率拉起来，重点其实在\n setup、命令、扩展能力和工作流设计。前面先讲了几个特别常用的 command：mode"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 844427,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "穷在街头无人问lhj",
    "platform": "bilibili",
    "points": 3203,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1fyVY6tE6y",
    "domain": "AI",
    "title": "Ultracode：Claude Code这次真的把“工程团队”塞进了一个命令里",
    "url": "http://www.bilibili.com/video/av116659683595894",
    "source": "MIP耀",
    "platform": "bilibili",
    "points": 844,
    "published_at": "2026-05-29T20:15:59+00:00",
    "summary": "5 月 28 日,Claude Code 上线了一个新功能——Ultracode。\n它让 Claude 自己决定要不要拆任务、起几十上百个子代理并发执行、\n然后自己验证结果——你只敲一个命令。\n \nAnthropic 给的标杆案例:Bun 运行时从 Zig 移植到 Rust,\n75 万行代码、11 天、99.8% 测试通过。\n \n但这条视频不只是讲&quot;哇好牛&quot;——而是想拆解一件事"
  },
  {
    "id": "bvid:BV1mdGR6iEoH",
    "domain": "AI",
    "title": "Code with Claude 2026 | London 2026",
    "url": "http://www.bilibili.com/video/av116634450657952",
    "source": "DesyncInfoSec",
    "platform": "bilibili",
    "points": 764,
    "published_at": "2026-05-25T09:22:07+00:00",
    "summary": "https://claude.com/code-with-claude/london\nCode with Claude 2026 是 Anthropic 面向开发者举办的年度 AI 编程大会，聚焦 Claude Code、Agentic Coding、MCP 生态以及 AI 原生软件开发实践。大会包含主题演讲、实战 Workshop、最新能力演示，以及与 Anthropic 工程团队的技术交流，重"
  },
  {
    "id": "bvid:BV1CNV86tEQM",
    "domain": "AI",
    "title": "[parallel] Claude Code 动态工作流详解",
    "url": "http://www.bilibili.com/video/av116655640283767",
    "source": "isomoes",
    "platform": "bilibili",
    "points": 621,
    "published_at": "2026-05-29T03:05:47+00:00",
    "summary": "1.5x https://claude.com/blog/introducing-dynamic-workflows-in-claude-code\n\n本期视频介绍 Claude Code 随 Opus 4.8 同步推出的动态工作流（dynamic workflow），也就是把思考等级调到最高档 ultra code 后才会启用的功能。视频首先对比了上一期讲过的 Claude agents（Clau"
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 61918,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1cqVh6xEuD",
    "domain": "AI",
    "title": "Claude Code ultracode效果",
    "url": "http://www.bilibili.com/video/av116656781137372",
    "source": "gps949",
    "platform": "bilibili",
    "points": 405,
    "published_at": "2026-05-29T07:57:43+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1m29ZByEWm",
    "domain": "AI",
    "title": "5月最新Claude Code使用安装教程，手把手教你在国内怎么免费使用安装Claude Code！",
    "url": "http://www.bilibili.com/video/av116508520875071",
    "source": "Claudecode使用教程",
    "platform": "bilibili",
    "points": 66224,
    "published_at": "2026-05-03T03:38:16+00:00",
    "summary": "一个冷知识:点赞是免费的!\n但是可以让辛苦做视频的UP主开心快乐一整天!!!\n视频配套的整 合 包 &amp;工 作 流，关注+评论掉落~"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 741658,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "点赞+评论+关注，AI 会发你详细文档（不关注会导致无法发送私信给你，因为批量发太多给陌生人，会平台限流）"
  },
  {
    "id": "bvid:BV1W9cZzxEYs",
    "domain": "AI",
    "title": "AI 当助手！Claude 深度协助 UE5 游戏开发全流程",
    "url": "http://www.bilibili.com/video/av116209752277031",
    "source": "叁昧火游戏",
    "platform": "bilibili",
    "points": 14482,
    "published_at": "2026-03-11T12:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1XDVh61Ej2",
    "domain": "AI",
    "title": "（B站狂推！比刷剧爽！）2026公认最好的《Claude Code》教程，附课件代码—Claude Code探索-测试-重构-调试代码库",
    "url": "http://www.bilibili.com/video/av116656831466162",
    "source": "吴老师讲人工智能",
    "platform": "bilibili",
    "points": 978,
    "published_at": "2026-05-31T03:45:00+00:00",
    "summary": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码-----ClaudeCode【配套课程笔记+代码文件】+进阶学习路线-可以在我的gong.粽.号.【辅论AI】发送【333】无偿自取就行哦~"
  },
  {
    "id": "bvid:BV1j2Lw6CEyQ",
    "domain": "AI",
    "title": "Hermes Agent + Claude Code 互联：把 AI 升级成 7x24 全知员工",
    "url": "http://www.bilibili.com/video/av116594822876107",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 964,
    "published_at": "2026-05-18T09:26:55+00:00",
    "summary": "Jack Roberts 演示如何把 Hermes Agent（Nous Research）与 Claude Code Operating System 互联，打造跨平台共享记忆的 AI 智能系统。完整覆盖：Hermes 安装（Telegram bot 配置 + 用户授权）、Pantheon 自定义 AI 人格（Labyrinth/Mercury/Philosopher）、GitHub 仓库镜像备"
  },
  {
    "id": "bvid:BV1259NBdE47",
    "domain": "AI",
    "title": "Claude Code 最强搭档！手把手教你 CC Switch 安装，实现多模型自由",
    "url": "http://www.bilibili.com/video/av116338332800226",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 17633,
    "published_at": "2026-04-03T04:00:00+00:00",
    "summary": "CC Switch 安装（Win/Mac通用）\nWindows/Mac：终端执行 npm install -g cc-switch（需先安装Node.js）\n验证安装：命令行输入 cc-switch --version\n⚙️ 配合 Claude Code 切换模型\n启动 Claude Code 后，输入 /model 查看当前模型\n运行 cc-switch 进入交互菜单，选择目标模型（方向键+回车"
  },
  {
    "id": "bvid:BV1sJVL6QEzR",
    "domain": "AI",
    "title": "Claude Code 动态工作流实战指南",
    "url": "http://www.bilibili.com/video/av116664867755402",
    "source": "凌云_API",
    "platform": "bilibili",
    "points": 278,
    "published_at": "2026-05-30T18:18:16+00:00",
    "summary": "原视频链接：https://www.youtube.com/watch?v=jZgcWCzxh1I\n本视频为Ai技术搬运翻译，使用AI智能移除原视频广告营销内容，旨在降低信息差，帮助大家了解海外最新Ai动态\n翻译：凌云API模型gemini-3-flash-preview\nAI实用工具看下面：\n1、凌云AI平台：yunai.chat，国内可直接调用全球500+AI大模型API，支持Gemini、G"
  },
  {
    "id": "bvid:BV1Z5Gy69Ee7",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116645691394576",
    "source": "茶子兀",
    "platform": "bilibili",
    "points": 2528,
    "published_at": "2026-05-27T08:54:10+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1JfT4zVEa5",
    "domain": "AI",
    "title": "Cursor1.0新特性BugBot自动化代码Code Review使用教程+实测",
    "url": "http://www.bilibili.com/video/av114630882037891",
    "source": "码里奥Ziho",
    "platform": "bilibili",
    "points": 15077,
    "published_at": "2025-06-05T13:05:30+00:00",
    "summary": "Cursor推出了新的1.0版本，本视频对新特性Bugbot做了一个教程+实测\nBugBot可以在Github进行PR (Pull Request) 的时候，通过AI大模型帮助我们进行CR (Code Review)\n本视频用一个例子演示了如何使用Bugbot功能，并且最后给出了实测的结果\n\n感谢支持！！！欢迎三连\n个人公众号 【码里奥】"
  },
  {
    "id": "bvid:BV1zbduYgEBH",
    "domain": "AI",
    "title": "Cursor新手教程⑤：Cursor降智真相+解决办法",
    "url": "http://www.bilibili.com/video/av114311359891940",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 10744,
    "published_at": "2025-04-10T02:53:27+00:00",
    "summary": "你是不是经常碰到这种情况：\n你试图修复一个小错误\n人工智能给出一个看似合理的更改建议\n这个修复导致其他地方出错\n你要求人工智能修复新出现的问题\n这又产生了另外两个问题\n如此反复\n本视频带你拆解Cursor降智的真相以及解决办法"
  },
  {
    "id": "bvid:BV1wuLHzDEGA",
    "domain": "AI",
    "title": "【Godot&amp;Cursor】0.亲测一个月后，我选择Godot+Cursor组合做独立游戏",
    "url": "http://www.bilibili.com/video/av114398869853632",
    "source": "破妄-胖",
    "platform": "bilibili",
    "points": 13425,
    "published_at": "2025-04-25T13:43:22+00:00",
    "summary": "飞书文档：https://sh67ozct1z.feishu.cn/docx/Hn5jd0cE6op1Sux9RrFcl8Npnbd"
  },
  {
    "id": "bvid:BV1FXLJ6YELZ",
    "domain": "AI",
    "title": "Cursor无限薅最强大模型claude4.7，gpt5.5使用方法",
    "url": "http://www.bilibili.com/video/av116590041369141",
    "source": "长青来了奥",
    "platform": "bilibili",
    "points": 3640,
    "published_at": "2026-05-17T13:01:58+00:00",
    "summary": "一键三连吧！在主页\n自动回复私信要1000粉丝呜呜呜呜求帮忙"
  },
  {
    "id": "bvid:BV182XnY2EKQ",
    "domain": "AI",
    "title": "cursor怎么降级到0.45 回退版本 快乐又回来了",
    "url": "http://www.bilibili.com/video/av114203666946145",
    "source": "项目禅",
    "platform": "bilibili",
    "points": 1893,
    "published_at": "2025-03-22T02:16:33+00:00",
    "summary": "快乐又回来了 不降智 而且发了信息几秒就回复 还是这个用起来方便啊 最新版的是真用不习惯??"
  },
  {
    "id": "bvid:BV1ZFc2epE4s",
    "domain": "AI",
    "title": "Cursor+VS2022编译器 准备cursor的c++开发环境",
    "url": "http://www.bilibili.com/video/av113820676655607",
    "source": "新手村养牛人",
    "platform": "bilibili",
    "points": 14037,
    "published_at": "2025-01-13T11:00:14+00:00",
    "summary": "cmake_minimum_required(VERSION 3.23)\nproject(CursorVs2022)\nset(CMAKE_CXX_STANDARD 17)\n\nset(CMAKE_INCLUDE_CURRENT_DIR ON)\nSET(CMAKE_BUILD_TYPE Debug)\nset(CMAKE_AUTOMOC ON)\nset(CMAKE_AUTOUIC ON)\nset(CMA"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6320,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV16GV86XEPa",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116655757723840",
    "source": "刘十二-是我啊",
    "platform": "bilibili",
    "points": 2628,
    "published_at": "2026-05-29T03:42:21+00:00",
    "summary": "喜欢请三连哦   喜欢请三连哦   喜欢请三连哦   喜欢请三连哦   喜欢请三连哦   喜欢请三连哦   喜欢请三连哦"
  },
  {
    "id": "bvid:BV1X15y6nE8Z",
    "domain": "AI",
    "title": "cursor无限免费使用最新方法cursor无限续杯cursor使用教程免费",
    "url": "http://www.bilibili.com/video/av116567140540269",
    "source": "开团秒跟cursor",
    "platform": "bilibili",
    "points": 5084,
    "published_at": "2026-05-13T11:59:02+00:00",
    "summary": "最新2026年5月13号 免费Cursor无限续杯保姆级使用教程集成MCP，实现opus4.6/4.7无限使用额度自由，相关工具请到 1030496866 文件夹中自行获取,完全免费，完全免费，离线插件版本,安装即可用，无任何数据收集行为"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29176,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV19P38zHEJ8",
    "domain": "AI",
    "title": "Cursor1.0 手机版最新演示！上厕所、高铁、地铁、随时编程！",
    "url": "http://www.bilibili.com/video/av114784393563896",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 1908,
    "published_at": "2025-07-02T15:45:52+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1TWMszpEbk",
    "domain": "AI",
    "title": "【Obsidian+Cursor】10分钟打造外置大脑，学习效率暴增30倍！",
    "url": "http://www.bilibili.com/video/av114684971713670",
    "source": "AI辅导员小宇",
    "platform": "bilibili",
    "points": 16699,
    "published_at": "2025-06-15T02:25:13+00:00",
    "summary": "再也不用担心记不住、找不到！这套Obsidian+Cursor组合拳让你秒变学霸🔥 看了100个视频全是白看？学了50个知识点转眼就忘？本期教你零基础打造AI知识库，自动提取、分类、连接所有学习内容！不仅能记住一切，还能主动挖掘知识关联，比市面上几千块的课程还实用！学会这招能帮你节省200小时重复学习时间，不信你试试！👇点赞收藏，解锁最强&quot;外置大脑&quot;秘籍！#AI学习 #Curs"
  },
  {
    "id": "bvid:BV1b5WMzEEmK",
    "domain": "AI",
    "title": "测评某鱼买的Cursor无限续杯工具",
    "url": "http://www.bilibili.com/video/av115228083751177",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 38743,
    "published_at": "2025-09-19T00:17:50+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Bq5NzYETK",
    "domain": "AI",
    "title": "使用学生认证！白嫖Cursor一年会员！！！",
    "url": "http://www.bilibili.com/video/av114471028657003",
    "source": "硅基马达",
    "platform": "bilibili",
    "points": 14258,
    "published_at": "2025-05-08T07:30:20+00:00",
    "summary": "cursor学生认证地址：https://www.cursor.com/cn/students\n不知道能白嫖多久且行且珍惜"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 564778,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV18fhHz3Ezk",
    "domain": "AI",
    "title": "8月份最新cursor一键重置机器码",
    "url": "http://www.bilibili.com/video/av114952853593114",
    "source": "玩转Code",
    "platform": "bilibili",
    "points": 9484,
    "published_at": "2025-08-01T09:43:22+00:00",
    "summary": "软件安装包\nhttps://pan.quark.cn/s/9ffba35bd00a"
  },
  {
    "id": "bvid:BV1gwk3Y8Ers",
    "domain": "AI",
    "title": "CURSOR 遇到机器上使用过多的免费账号",
    "url": "http://www.bilibili.com/video/av113663037931907",
    "source": "想回家的前端开发",
    "platform": "bilibili",
    "points": 8062,
    "published_at": "2024-12-16T14:51:24+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Tvg3zsEDA",
    "domain": "AI",
    "title": "cursor 四种配置方式，测底解除模型地区不可用！",
    "url": "http://www.bilibili.com/video/av114872792647810",
    "source": "三少科技",
    "platform": "bilibili",
    "points": 11519,
    "published_at": "2025-07-18T06:24:35+00:00",
    "summary": "devbox注册地址：https://cloud.sealos.run/?uid=AoSqusVZZL\n我的知识星球，https://t.zsxq.com/jVAk9\n徕卡云服务器：https://www.lcayun.com/aff/GEYCYCZE"
  },
  {
    "id": "bvid:BV1FRNwekE7W",
    "domain": "AI",
    "title": "Cursor高效回溯技巧",
    "url": "http://www.bilibili.com/video/av113945465590642",
    "source": "BarrySong4Real",
    "platform": "bilibili",
    "points": 2180,
    "published_at": "2025-02-04T11:54:15+00:00",
    "summary": "AI生成的代码常会出现逻辑混乱或上下文脱节的情况。这种情况下，建立高效的回溯机制成为开发者的必备技能。"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 78867,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1caVh6fE6Z",
    "domain": "AI",
    "title": "【2026最新版】绝对是B站讲的最细的Claude Code教程，从国内环境安装出发，项目开发及个人使用总结带你玩转 Vibe Coding！",
    "url": "http://www.bilibili.com/video/av116656764358481",
    "source": "AI大模型_",
    "platform": "bilibili",
    "points": 3285,
    "published_at": "2026-05-29T07:53:39+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n本视频配套课件笔记代码/学习大纲/大模型学习路线戳这里获取→https://www.bilibili.com/opus/1195847460814061571?spm_id_from=333.1387.0.0\n另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 149047,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1VNVb6zEdw",
    "domain": "AI",
    "title": "【全网最细】目前B站讲得最全最细的Vibe Coding全套系统教程！零代码也能直接上手！七天就能从小白到大神，学完即就业！少走99%的弯路！存下吧，很难找全的",
    "url": "http://www.bilibili.com/video/av116656227489865",
    "source": "Agent智能体-",
    "platform": "bilibili",
    "points": 723,
    "published_at": "2026-05-29T05:43:23+00:00",
    "summary": "【全网最细】目前B站讲得最全最细的Vibe Coding全套系统教程！零代码也能直接上手！七天就能从小白到大神，学完即就业！少走99%的弯路！存下吧，真的很难找全！"
  },
  {
    "id": "bvid:BV1oNVH6xEWS",
    "domain": "AI",
    "title": "Claude Code 国内直连保姆级教程｜10分钟从入门到精通，原理+安装+实战全覆盖，解锁Vibe Coding编程新范式",
    "url": "http://www.bilibili.com/video/av116667602503393",
    "source": "码士集团-小晨晨晨",
    "platform": "bilibili",
    "points": 4936,
    "published_at": "2026-05-31T06:14:34+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1QbVE6GE9a",
    "domain": "AI",
    "title": "新手也能用Vibe Coding给Hermes搭建可视化办公室~ 动手coding自己做工具~",
    "url": "http://www.bilibili.com/video/av116667099122260",
    "source": "在下李君陌",
    "platform": "bilibili",
    "points": 1925,
    "published_at": "2026-05-31T04:02:32+00:00",
    "summary": "视频中的大模型分别来自\n1.Kimi K2.6&amp; GLM5.1 — 优云智算\nhttps://passport.compshare.cn/register?referral_code=DzKOV5Iik6lG9svK0phShR&amp;ytag=GPU_YY_YX_bl_ljm0531\n2.DeepSeek-V4\nhttps://platform.deepseek.com/"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 139610,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "domain": "AI",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 129875,
    "published_at": "2026-01-11T15:43:58+00:00",
    "summary": "🚀开发者必看！Superpowers把专业工程团队方法论固化成Skills，让Claude Code告别越写越乱的困境：规格驱动+代码质量双重保障！AI编程新范式！头脑风暴+计划+执行一条龙自动化\n\n\n🚀🚀🚀 视频简介：\n🎬 本期视频详细演示了开源AI编程工作流系统Superpowers的完整使用方法，并通过开发一款iOS时间线笔记原生应用来实测其效果。\n🔧 核心内容：\nSuperpowers工作"
  },
  {
    "id": "bvid:BV1e7VA6vEJU",
    "domain": "AI",
    "title": "【2026最新】绝对是B站No.1的Claude Code教程：国内安装+实战开发案例+个人使用心得总结，手把手带你拥抱Vibe Coding！",
    "url": "http://www.bilibili.com/video/av116640356304890",
    "source": "码士集团-马小安",
    "platform": "bilibili",
    "points": 25047,
    "published_at": "2026-05-26T10:22:46+00:00",
    "summary": "绝对是B站No.1的Claude Code教程：国内安装+实战开发案例+个人使用心得总结，手把手带你拥抱Vibe Coding！\n配套课件笔记/PPT已备好，另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景题移步评论置顶即可~"
  },
  {
    "id": "bvid:BV14pVJ6KEoG",
    "domain": "AI",
    "title": "Vibe Coding全栈开发实战体系课（B站高分课程）",
    "url": "http://www.bilibili.com/video/av116666579032769",
    "source": "西瓜讲大模型",
    "platform": "bilibili",
    "points": 435,
    "published_at": "2026-05-31T01:29:24+00:00",
    "summary": "项目驱动是最快的学习方式！"
  },
  {
    "id": "bvid:BV19x6vBXEqC",
    "domain": "AI",
    "title": "1小时精通 Qoder Skills：实战+避坑指南",
    "url": "http://www.bilibili.com/video/av115982991365489",
    "source": "Qoder",
    "platform": "bilibili",
    "points": 27708,
    "published_at": "2026-01-30T10:05:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 228542,
    "published_at": "2026-04-04T15:19:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1DjVM66EF5",
    "domain": "AI",
    "title": "Vibe Coding从入门到精通实战课(手把手教学)",
    "url": "http://www.bilibili.com/video/av116660908332561",
    "source": "西瓜讲大模型",
    "platform": "bilibili",
    "points": 834,
    "published_at": "2026-05-30T01:25:43+00:00",
    "summary": "项目驱动是最快的学习方式！"
  },
  {
    "id": "bvid:BV1v8mtBpEwK",
    "domain": "AI",
    "title": "Kiro 上手必看：从Vibe 到 Spec 全攻略！",
    "url": "http://www.bilibili.com/video/av115695564102585",
    "source": "AI编程瓜哥",
    "platform": "bilibili",
    "points": 20438,
    "published_at": "2025-12-10T13:49:11+00:00",
    "summary": "一眼懂，Vibe coding 和Spec Coding，双模式实战。"
  },
  {
    "id": "bvid:BV1huVS64Epj",
    "domain": "AI",
    "title": "Vibe Coding劝退指南：别踩我30亿的坑",
    "url": "http://www.bilibili.com/video/av116668827179903",
    "source": "流明AI笔记",
    "platform": "bilibili",
    "points": 35,
    "published_at": "2026-05-31T10:59:56+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1aHqHBME3a",
    "domain": "AI",
    "title": "如何高效使用 Qoder",
    "url": "http://www.bilibili.com/video/av115738832541682",
    "source": "Qoder",
    "platform": "bilibili",
    "points": 14906,
    "published_at": "2025-12-18T05:11:43+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 50416,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV1K2Va6uEuZ",
    "domain": "AI",
    "title": "我的第一个Vibe Coding软件终于上线了，但过程很曲折～",
    "url": "http://www.bilibili.com/video/av116658106666921",
    "source": "游戏开发极客",
    "platform": "bilibili",
    "points": 845,
    "published_at": "2026-05-31T02:00:00+00:00",
    "summary": "OPC创业，最简单的是做产品，后面的工作比你想象的难的多。"
  },
  {
    "id": "bvid:BV1vhVn6SEuk",
    "domain": "AI",
    "title": "【2026最新】绝对是B站No.1的Claude Code教程：国内安装+实战开发案例+个人使用心得总结，手把手带你拥抱Vibe Coding！",
    "url": "http://www.bilibili.com/video/av116667904561472",
    "source": "杨淑娟Python",
    "platform": "bilibili",
    "points": 550,
    "published_at": "2026-05-31T07:14:54+00:00",
    "summary": "绝对是B站No.1的Claude Code教程：国内安装+实战开发案例+个人使用心得总结，手把手带你拥抱Vibe Coding！\n配套课件笔记/PPT已备好，另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景题移步评论置顶即可~\n\ncodex+hermes+claude code 从0到1全讲明白"
  },
  {
    "id": "bvid:BV1sWVQ6REVz",
    "domain": "AI",
    "title": "声历voice calendar by vibe coding demo演示",
    "url": "http://www.bilibili.com/video/av116669766698987",
    "source": "翠花上酸菜鱼米线",
    "platform": "bilibili",
    "points": 0,
    "published_at": "2026-05-31T15:04:03+00:00",
    "summary": ""
  }
]
```
