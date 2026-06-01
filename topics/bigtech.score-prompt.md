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

- 用户领域：`大厂 AI 动态` / 子话题：`[
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
  "domain": "大厂 AI 动态",
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
    "id": "rss:https://www.theverge.com/gadgets/940794/first-nvidia-rtx-spark-laptops-roundup-computex-2026",
    "platform": "rss",
    "title": "These are the first Nvidia RTX Spark laptops",
    "url": "https://www.theverge.com/gadgets/940794/first-nvidia-rtx-spark-laptops-roundup-computex-2026",
    "source": "Jess Weatherbed",
    "published_at": "2026-06-01T11:29:52+00:00",
    "summary": "Nvidia has officially entered the world of consumer laptop chips with the RTX Spark, and several device makers already have hardware lined up for it. Microsoft, Asus, HP, MSI, Lenovo, and Dell are expected to launch RTX Spark laptops sometime this fall, and some of those partner companies have share",
    "feed": "The Verge"
  },
  {
    "id": "rss:https://www.theverge.com/games/940722/asus-xbox-ally-x20-special-edition-oled-screen",
    "platform": "rss",
    "title": "Asus just announced the OLED Xbox Ally X of my dreams",
    "url": "https://www.theverge.com/games/940722/asus-xbox-ally-x20-special-edition-oled-screen",
    "source": "Sean Hollister",
    "published_at": "2026-06-01T10:00:00+00:00",
    "summary": "If you asked me what I'd change about the Xbox Ally X handheld - aside from fixing Windows, I mean - I'd tell you two key things. First, give me a bigger, better screen. Even a little bit bigger, so games feel less claustrophobic and with less ugly bezel. Second, get rid of the \"Library\" [&#8230;]",
    "feed": "The Verge"
  },
  {
    "id": "rss:https://www.theverge.com/tech/940584/microsoft-surface-laptop-ultra-nvidia-rtx-spark-pictures",
    "platform": "rss",
    "title": "This is the Microsoft Surface Laptop Ultra with Nvidia RTX Spark",
    "url": "https://www.theverge.com/tech/940584/microsoft-surface-laptop-ultra-nvidia-rtx-spark-pictures",
    "source": "Sean Hollister",
    "published_at": "2026-06-01T04:36:41+00:00",
    "summary": "Once upon a time, Microsoft had to write off $900 million betting an Arm-based Nvidia chip could power its first flagship Windows portable, the original Microsoft Surface. But today, it's trying again. Microsoft and Nvidia have just announced the Surface Laptop Ultra, a computer with a new Arm-based",
    "feed": "The Verge"
  },
  {
    "id": "rss:https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-date",
    "platform": "rss",
    "title": "Nvidia announces RTX Spark as ‘the most efficient PC chip ever built’",
    "url": "https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-date",
    "source": "Sean Hollister",
    "published_at": "2026-06-01T04:28:53+00:00",
    "summary": "This fall, Nvidia will officially become a consumer PC chipmaker like Intel, AMD, Apple, and Qualcomm, putting a complete computing chip - not just graphics - into the very heart of laptops and mini-PCs. After many months of leaks, it's finally announcing the RTX Spark, the first in a family of chip",
    "feed": "The Verge"
  },
  {
    "id": "rss:https://www.theverge.com/tech/940524/amd-computex-am5-promise-2029-rx9070gre-7700x3d-5800x3d",
    "platform": "rss",
    "title": "AMD’s new pitch: our old tech is so good you should just keep using it",
    "url": "https://www.theverge.com/tech/940524/amd-computex-am5-promise-2029-rx9070gre-7700x3d-5800x3d",
    "source": "Sean Hollister",
    "published_at": "2026-06-01T00:00:00+00:00",
    "summary": "Computex 2026 is underway in Taiwan, and we're expecting all manner of flashy computers with jaw-dropping prices (or no prices at all) as the entire industry navigates RAMageddon. But for desktop PC gamers, AMD has a different pitch. It's relaunching three old components alongside a big new promise:",
    "feed": "The Verge"
  },
  {
    "id": "rss:https://www.theverge.com/games/938956/alienware-computex-tandem-qd-oled-penta-rgb-stripe-gaming-monitors-specs",
    "platform": "rss",
    "title": "The QD-OLED gaming monitor that started it all got a big upgrade",
    "url": "https://www.theverge.com/games/938956/alienware-computex-tandem-qd-oled-penta-rgb-stripe-gaming-monitors-specs",
    "source": "Cameron Faulkner",
    "published_at": "2026-05-31T23:00:00+00:00",
    "summary": "Alienware is taking to this year's Computex 2026 in Taipei to announce some cool gaming monitors, most notably two exciting OLED options that are coming at different points this year. First off, the company is debuting the successor to its very first QD-OLED gaming monitor from 2022 with a refreshed",
    "feed": "The Verge"
  },
  {
    "id": "rss:https://www.theverge.com/tech/940498/dell-xps-13-student-laptop-intel-wildcat-panther-lake-computex-price",
    "platform": "rss",
    "title": "Dell is bringing back the XPS 13 as a MacBook Neo competitor — with a temporary discount to $599",
    "url": "https://www.theverge.com/tech/940498/dell-xps-13-student-laptop-intel-wildcat-panther-lake-computex-price",
    "source": "Antonio G. Di Benedetto",
    "published_at": "2026-05-31T23:00:00+00:00",
    "summary": "Dell is making good on its tease from CES and finally announcing a new XPS 13. The XPS 13 returns as a budget-friendly option, launching in July at a promotional student price of $599 - though that introductory deal only runs until September for back-to-school shopping; it'll start at $699 for every",
    "feed": "The Verge"
  },
  {
    "id": "rss:https://www.theverge.com/tech/940572/apples-strategy-smart-glasses-smart-watches",
    "platform": "rss",
    "title": "Apple’s strategy for smart glasses is the same as for smart watches",
    "url": "https://www.theverge.com/tech/940572/apples-strategy-smart-glasses-smart-watches",
    "source": "Terrence O’Brien",
    "published_at": "2026-05-31T21:33:11+00:00",
    "summary": "Apple isn't just looking to take on Meta in the smart glasses market; it's looking to upend eyewear as a whole, according to Bloomberg's Mark Gurman. When the Apple Watch launched, it wasn't simply competing against the Pebbles and the Motorolas of the world. The company also had Swatch, Fossil, and",
    "feed": "The Verge"
  },
  {
    "id": "rss:https://www.theverge.com/tech/940540/how-to-watch-nvidias-computex-keynote",
    "platform": "rss",
    "title": "How to watch Nvidia&#8217;s Computex keynote",
    "url": "https://www.theverge.com/tech/940540/how-to-watch-nvidias-computex-keynote",
    "source": "Terrence O’Brien",
    "published_at": "2026-05-31T20:20:35+00:00",
    "summary": "NVIDIA's CEO Jensen Huang is set to take the stage for his GTC Taipei keynote at 8PM PT / 11PM ET. You can watch all the announcements here and embedded below. Rumors have been flying about what to expect from today's presentation, but the big one is the possibility of a partnership with Microsoft a",
    "feed": "The Verge"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/940523/minecraft-movie-squared-sequel-kirsten-dunst-alex",
    "platform": "rss",
    "title": "Here’s your first look at ‘A Minecraft Movie Squared’ with Kirsten Dunst as Alex",
    "url": "https://www.theverge.com/entertainment/940523/minecraft-movie-squared-sequel-kirsten-dunst-alex",
    "source": "Terrence O’Brien",
    "published_at": "2026-05-31T19:28:11+00:00",
    "summary": "The A Minecraft Movie sequel officially has a title: A Minecraft Movie Squared. What's more, we now know that Kirsten Dunst will star as Alex, the game's female character option, and that Matt Berry is set to play an even bigger role in this film. He voiced Nitwit in the first movie, but in this [&#",
    "feed": "The Verge"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/01/unastella-a-south-korean-rocket-startup-that-launched-from-home-raises-24m/",
    "platform": "rss",
    "title": "Unastella, a South Korean rocket startup that launched from home, raises $24M",
    "url": "https://techcrunch.com/2026/06/01/unastella-a-south-korean-rocket-startup-that-launched-from-home-raises-24m/",
    "source": "Kate Park",
    "published_at": "2026-06-01T10:00:00+00:00",
    "summary": "The Seoul-based rocket startup is developing its own launch vehicles and engines.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/erin-brockovich-takes-aim-at-data-center-secrecy/",
    "platform": "rss",
    "title": "Erin Brockovich takes aim at data center secrecy",
    "url": "https://techcrunch.com/2026/05/31/erin-brockovich-takes-aim-at-data-center-secrecy/",
    "source": "Anthony Ha",
    "published_at": "2026-05-31T21:05:14+00:00",
    "summary": "Environmental activist Erin Brockovich has a new mission.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/this-weekends-two-biggest-movies-were-both-directed-by-youtubers/",
    "platform": "rss",
    "title": "This weekend’s two biggest movies were both directed by YouTubers",
    "url": "https://techcrunch.com/2026/05/31/this-weekends-two-biggest-movies-were-both-directed-by-youtubers/",
    "source": "Anthony Ha",
    "published_at": "2026-05-31T18:34:58+00:00",
    "summary": "The YouTube-to-prestige-horror pipeline is looking very strong.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/this-is-fine-artist-kc-green-reaches-agreement-with-ai-startup-artisan/",
    "platform": "rss",
    "title": "‘This is fine’ artist KC Green reaches agreement with AI startup Artisan",
    "url": "https://techcrunch.com/2026/05/31/this-is-fine-artist-kc-green-reaches-agreement-with-ai-startup-artisan/",
    "source": "Anthony Ha",
    "published_at": "2026-05-31T18:28:17+00:00",
    "summary": "The startup has apparently taken down the ads using KC Green's \"This is fine\" meme.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/techcrunch-mobility-it-doesnt-matter-that-people-hate-the-ferrari-luce/",
    "platform": "rss",
    "title": "TechCrunch Mobility: It doesn’t matter that people hate the Ferrari Luce",
    "url": "https://techcrunch.com/2026/05/31/techcrunch-mobility-it-doesnt-matter-that-people-hate-the-ferrari-luce/",
    "source": "Kirsten Korosec",
    "published_at": "2026-05-31T16:05:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, how AI is playing a part.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/making-sense-of-the-debate-over-ai-psychosis/",
    "platform": "rss",
    "title": "Making sense of the debate over AI psychosis",
    "url": "https://techcrunch.com/2026/05/31/making-sense-of-the-debate-over-ai-psychosis/",
    "source": "Anthony Ha",
    "published_at": "2026-05-31T15:30:00+00:00",
    "summary": "On the latest episode of Equity, we debate whether tech CEOs are \"uniquely prone to AI psychosis.\"",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/black-founders-raise-highest-amount-of-quarterly-funding-since-2022-but-theres-a-catch/",
    "platform": "rss",
    "title": "Black founders raise highest amount of quarterly funding since 2022, but there’s a catch",
    "url": "https://techcrunch.com/2026/05/31/black-founders-raise-highest-amount-of-quarterly-funding-since-2022-but-theres-a-catch/",
    "source": "Dominic-Madori Davis",
    "published_at": "2026-05-31T15:00:00+00:00",
    "summary": "Speaking to TechCrunch, Crunchbase’s head of research Gené Teare, said the factors holding back Black founders include “access to networks, relationships, and early introductions.\"",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/31/i-went-to-the-so-called-steroid-olympics-to-understand-why-silicon-valley-is-obsessed-with-peptides/",
    "platform": "rss",
    "title": "What happens in Vega$: steroids, swimmers, and a billion-dollar hustle",
    "url": "https://techcrunch.com/2026/05/31/i-went-to-the-so-called-steroid-olympics-to-understand-why-silicon-valley-is-obsessed-with-peptides/",
    "source": "Lucas Ropek",
    "published_at": "2026-05-31T13:00:00+00:00",
    "summary": "The Enhanced Games — a singular sporting competition where a majority of the athletes were on performance enhancing drugs — may herald a new business model that the tech industry is ready to embrace.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/softbank-says-it-will-invest-up-to-e75-billion-to-build-french-data-centers/",
    "platform": "rss",
    "title": "SoftBank says it will invest up to €75 billion to build French data centers",
    "url": "https://techcrunch.com/2026/05/30/softbank-says-it-will-invest-up-to-e75-billion-to-build-french-data-centers/",
    "source": "Anthony Ha",
    "published_at": "2026-05-30T21:45:00+00:00",
    "summary": "The goal, the firm said, is to develop and operate up to 5 gigawatts of additional data center capacity.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/snap-alums-unveil-ghost-angels-fund/",
    "platform": "rss",
    "title": "Snap alums unveil Ghost Angels fund",
    "url": "https://techcrunch.com/2026/05/30/snap-alums-unveil-ghost-angels-fund/",
    "source": "Dominic-Madori Davis",
    "published_at": "2026-05-30T17:00:00+00:00",
    "summary": "A group of 20 Snap alumni has come together to launch a fund called Ghost Angels to back the next generation of social media.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/what-a-joke-github-copilots-new-token-based-billing-spurs-consternation-among-devs/",
    "platform": "rss",
    "title": "‘What a joke’: Github Copilot’s new token-based billing spurs consternation among devs",
    "url": "https://techcrunch.com/2026/05/30/what-a-joke-github-copilots-new-token-based-billing-spurs-consternation-among-devs/",
    "source": "Lucas Ropek",
    "published_at": "2026-05-30T16:30:00+00:00",
    "summary": "The golden age of Microsoft's Github Copilot appears to be at an end.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/meta-is-reportedly-developing-an-ai-pendant/",
    "platform": "rss",
    "title": "Meta is reportedly developing an AI pendant",
    "url": "https://techcrunch.com/2026/05/30/meta-is-reportedly-developing-an-ai-pendant/",
    "source": "Anthony Ha",
    "published_at": "2026-05-30T15:59:58+00:00",
    "summary": "Meta seems to be making big bets on AI-powered hardware.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/i-put-googles-24-7-ai-assistant-gemini-spark-to-work-and-its-actually-pretty-useful/",
    "platform": "rss",
    "title": "I put Google’s 24/7 AI assistant Gemini Spark to work, and it’s actually pretty useful",
    "url": "https://techcrunch.com/2026/05/30/i-put-googles-24-7-ai-assistant-gemini-spark-to-work-and-its-actually-pretty-useful/",
    "source": "Sarah Perez",
    "published_at": "2026-05-30T15:30:00+00:00",
    "summary": "Gemini Spark helps automate everyday tasks, from inbox summaries to local event planning, but it’s unclear why Google made it a separate product.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/the-groupthink-boom-what-three-top-vcs-really-think-about-the-ai-frenzy/",
    "platform": "rss",
    "title": "The groupthink boom: what three top VCs really think about the AI frenzy",
    "url": "https://techcrunch.com/2026/05/30/the-groupthink-boom-what-three-top-vcs-really-think-about-the-ai-frenzy/",
    "source": "Connie Loizos",
    "published_at": "2026-05-30T14:49:27+00:00",
    "summary": "\"If you're 22 years old in San Francisco and building something in AI, there may be a seed term sheet in your inbox — but if you're 19, oh my God, this means you're really good; you might already have a Series A [offer],\" said one, half-kiddingly.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/as-the-browser-wars-heat-up-here-are-the-hottest-alternatives-to-chrome-and-safari-in-2026/",
    "platform": "rss",
    "title": "As the browser wars heat up, here are the hottest alternatives to Chrome and Safari in 2026",
    "url": "https://techcrunch.com/2026/05/30/as-the-browser-wars-heat-up-here-are-the-hottest-alternatives-to-chrome-and-safari-in-2026/",
    "source": "Lauren Forristal",
    "published_at": "2026-05-30T13:00:00+00:00",
    "summary": "We’ve compiled an overview of some of the top alternative browsers available today aiming to challenge Chrome and Safari.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/this-300-pizza-oven-can-easily-help-elevate-your-summer-pizza-nights/",
    "platform": "rss",
    "title": "This $300 pizza oven can easily help elevate your summer pizza nights",
    "url": "https://techcrunch.com/2026/05/30/this-300-pizza-oven-can-easily-help-elevate-your-summer-pizza-nights/",
    "source": "Aisha Malik",
    "published_at": "2026-05-30T13:00:00+00:00",
    "summary": "The Ninja Artisan Outdoor Pizza Oven is aimed at people who want delicious pizza nights without having to deal with things like propane or wood pellets, unlike many other pizza ovens.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/30/tiktoks-road-to-becoming-a-super-app/",
    "platform": "rss",
    "title": "TikTok’s road to becoming a super app",
    "url": "https://techcrunch.com/2026/05/30/tiktoks-road-to-becoming-a-super-app/",
    "source": "Aisha Malik",
    "published_at": "2026-05-30T13:00:00+00:00",
    "summary": "TikTok may be working to become the app that people use for most of their digital activities.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/29/founders-seize-on-indian-court-ruling-to-revive-criticism-of-googles-ad-business/",
    "platform": "rss",
    "title": "Founders seize on Indian court ruling to revive criticism of Google’s ad business",
    "url": "https://techcrunch.com/2026/05/29/founders-seize-on-indian-court-ruling-to-revive-criticism-of-googles-ad-business/",
    "source": "Jagmeet Singh",
    "published_at": "2026-05-30T02:00:00+00:00",
    "summary": "The ruling drew support from founders, while lawyers said it could force platforms to revisit how they handle trademarked keywords.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/29/spacex-awarded-6-45b-in-space-force-contracts-ahead-of-ipo/",
    "platform": "rss",
    "title": "SpaceX awarded $6.45B in Space Force contracts ahead of IPO",
    "url": "https://techcrunch.com/2026/05/29/spacex-awarded-6-45b-in-space-force-contracts-ahead-of-ipo/",
    "source": "Sean O'Kane",
    "published_at": "2026-05-29T22:21:38+00:00",
    "summary": "SpaceX already generated one-fifth of its 2025 revenue from government contracts, the company revealed in its IPO filing.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://techcrunch.com/2026/05/29/coders-are-refusing-to-work-without-ai-and-that-could-come-back-to-bite-them/",
    "platform": "rss",
    "title": "Coders are refusing to work without AI — and that could come back to bite them",
    "url": "https://techcrunch.com/2026/05/29/coders-are-refusing-to-work-without-ai-and-that-could-come-back-to-bite-them/",
    "source": "Julie Bort",
    "published_at": "2026-05-29T22:14:22+00:00",
    "summary": "While AI is helping coders produce code faster, it may not be producing better code, researchers warn. And that could cause problems down the road for them.",
    "feed": "TechCrunch"
  },
  {
    "id": "rss:https://stratechery.com/2026/youtubers-win-the-box-office-goodbye-gatekeepers-the-youtube-bar/",
    "platform": "rss",
    "title": "YouTubers Win the Box Office, Goodbye Gatekeepers, The YouTube Bar",
    "url": "https://stratechery.com/2026/youtubers-win-the-box-office-goodbye-gatekeepers-the-youtube-bar/",
    "source": "Ben Thompson",
    "published_at": "2026-06-01T10:00:00+00:00",
    "summary": "YouTubers are ruling the box office, and it shouldn't be a surprise: succeeding on YouTube is a much higher bar than the gates that currently govern Hollywood.",
    "feed": "Stratechery by Ben Thompson"
  },
  {
    "id": "rss:https://stratechery.com/2026/luceing-their-mind/",
    "platform": "rss",
    "title": "2026.22: Luceing Their Mind",
    "url": "https://stratechery.com/2026/luceing-their-mind/",
    "source": "Ben Thompson",
    "published_at": "2026-05-29T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of May 25, 2026, including why everyone hates Luce, how to monetize AI answers, and social mobility in China.",
    "feed": "Stratechery by Ben Thompson"
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-eric-seufert-about-models-and-ads-and-ais-upside-for-humanity/",
    "platform": "rss",
    "title": "An Interview with Eric Seufert About Models and Ads, and AI’s Upside for Humanity",
    "url": "https://stratechery.com/2026/an-interview-with-eric-seufert-about-models-and-ads-and-ais-upside-for-humanity/",
    "source": "Ben Thompson",
    "published_at": "2026-05-28T10:00:00+00:00",
    "summary": "An Interview with Eric Seufert about building models for generative AI, why Meta's foundational models are so important, and why understanding advertising leads to optimism about humanity's future.",
    "feed": "Stratechery by Ben Thompson"
  },
  {
    "id": "rss:https://stratechery.com/2026/the-spacex-ipo-and-data-centers-in-space/",
    "platform": "rss",
    "title": "The SpaceX IPO and Data Centers in Space",
    "url": "https://stratechery.com/2026/the-spacex-ipo-and-data-centers-in-space/",
    "source": "Ben Thompson",
    "published_at": "2026-05-27T10:00:00+00:00",
    "summary": "There isn't a financial model that justifies the SpaceX IPO, but data centers in space are plausible, and that might be enough.",
    "feed": "Stratechery by Ben Thompson"
  },
  {
    "id": "rss:https://stratechery.com/2026/nvidia-earnings-the-ai-stack-nvidias-new-reporting/",
    "platform": "rss",
    "title": "Nvidia Earnings, The AI Stack, Nvidia’s New Reporting",
    "url": "https://stratechery.com/2026/nvidia-earnings-the-ai-stack-nvidias-new-reporting/",
    "source": "Ben Thompson",
    "published_at": "2026-05-26T10:00:00+00:00",
    "summary": "Nvidia is changing its reporting to delineate between hyperscaler sales — where Nvidia is fighting commoditization — and everyone else, where Nvidia runs the whole stack.",
    "feed": "Stratechery by Ben Thompson"
  },
  {
    "id": "rss:https://stratechery.com/2026/the-data-center-veto/",
    "platform": "rss",
    "title": "2026.21: The Data Center Veto",
    "url": "https://stratechery.com/2026/the-data-center-veto/",
    "source": "Ben Thompson",
    "published_at": "2026-05-22T17:12:32+00:00",
    "summary": "The best Stratechery content from the week of May 18, 2026, including data center discontent, agent economics, and slime mold.",
    "feed": "Stratechery by Ben Thompson"
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-parallel-founder-parag-agarwal-about-valuing-content-on-the-agentic-web/",
    "platform": "rss",
    "title": "An Interview with Parallel Founder Parag Agarwal About Valuing Content on the Agentic Web",
    "url": "https://stratechery.com/2026/an-interview-with-parallel-founder-parag-agarwal-about-valuing-content-on-the-agentic-web/",
    "source": "Ben Thompson",
    "published_at": "2026-05-21T10:00:00+00:00",
    "summary": "An interview with Parallel founder Parag Agarwal about valuing content and incentivizing its creation in a world of agents (plus questions about Twitter).",
    "feed": "Stratechery by Ben Thompson"
  },
  {
    "id": "rss:https://stratechery.com/2026/google-i-o-world-models-i-o-spaghetti/",
    "platform": "rss",
    "title": "Google I/O, World Models, I/O Spaghetti",
    "url": "https://stratechery.com/2026/google-i-o-world-models-i-o-spaghetti/",
    "source": "Ben Thompson",
    "published_at": "2026-05-20T10:00:00+00:00",
    "summary": "Google I/O put AI everywhere, for better and for worse. Meanwhile, is DeepMind aligned with Google's business objectives?",
    "feed": "Stratechery by Ben Thompson"
  },
  {
    "id": "rss:https://stratechery.com/2026/data-center-discontent-understanding-the-opposition-fixing-the-problem/",
    "platform": "rss",
    "title": "Data Center Discontent, Understanding the Opposition, Fixing the Problem",
    "url": "https://stratechery.com/2026/data-center-discontent-understanding-the-opposition-fixing-the-problem/",
    "source": "Ben Thompson",
    "published_at": "2026-05-18T10:00:00+00:00",
    "summary": "There are understandable reasons for people to oppose data centers; the only solution that will work is simply paying them off.",
    "feed": "Stratechery by Ben Thompson"
  },
  {
    "id": "rss:https://stratechery.com/2026/shifting-alliances-in-a-changing-world/",
    "platform": "rss",
    "title": "2026.20: Shifting Alliances in a Changing World",
    "url": "https://stratechery.com/2026/shifting-alliances-in-a-changing-world/",
    "source": "Ben Thompson",
    "published_at": "2026-05-15T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of May 11, 2026, including a new kind of computing, Elon Musk, and 360 degrees of US-China relations.",
    "feed": "Stratechery by Ben Thompson"
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/openais-math-breakthrough-played-to-ais-strengths/",
    "platform": "rss",
    "title": "An OpenAI model solved a famous math problem that stumped humans for 80 years",
    "url": "https://arstechnica.com/ai/2026/06/openais-math-breakthrough-played-to-ais-strengths/",
    "source": "Kai Williams",
    "published_at": "2026-06-01T11:00:00+00:00",
    "summary": "I tried to explain OpenAI’s solution more clearly than OpenAI did.",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/05/on-its-40th-anniversary-we-reassess-1986s-spacecamp/",
    "platform": "rss",
    "title": "On its 40th anniversary, we reassess 1986's SpaceCamp",
    "url": "https://arstechnica.com/culture/2026/05/on-its-40th-anniversary-we-reassess-1986s-spacecamp/",
    "source": "Eric Berger & Lee Hutchinson",
    "published_at": "2026-05-31T11:15:12+00:00",
    "summary": "Is it a hidden gem, a cult classic, or hopelessly dumb? We vote \"all of the above.\"",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/05/they-call-it-stupid-hot-for-a-reason-heat-muddles-animal-brains/",
    "platform": "rss",
    "title": "They call it stupid hot for a reason: Heat muddles animal brains",
    "url": "https://arstechnica.com/science/2026/05/they-call-it-stupid-hot-for-a-reason-heat-muddles-animal-brains/",
    "source": "Marta Zaraska",
    "published_at": "2026-05-31T10:00:07+00:00",
    "summary": "As temperatures rise, some creatures pick fights while others struggle to learn.",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/05/grifters-cynics-and-true-believers-the-family-tree-of-vaccine-opponents/",
    "platform": "rss",
    "title": "Grifters, cynics, and true believers: The family tree of vaccine opponents",
    "url": "https://arstechnica.com/science/2026/05/grifters-cynics-and-true-believers-the-family-tree-of-vaccine-opponents/",
    "source": "Diana Gitig",
    "published_at": "2026-05-30T11:00:05+00:00",
    "summary": "A new book looks into the long history of people who have opposed vaccines.",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/05/environmentalists-turn-out-in-force-to-oppose-trump-coal-ash-rollbacks/",
    "platform": "rss",
    "title": "Environmentalists turn out in force to oppose Trump coal ash rollbacks",
    "url": "https://arstechnica.com/tech-policy/2026/05/environmentalists-turn-out-in-force-to-oppose-trump-coal-ash-rollbacks/",
    "source": "Arcelia Martin",
    "published_at": "2026-05-30T10:00:38+00:00",
    "summary": "Trump admin wants to rely on states for coal ash monitoring, enforcement, allow them to bypass national standards.",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/05/the-office-of-management-and-budget-tries-again-to-cripple-us-science/",
    "platform": "rss",
    "title": "Proposed new US funding rules: We can cancel any grant at any time",
    "url": "https://arstechnica.com/science/2026/05/the-office-of-management-and-budget-tries-again-to-cripple-us-science/",
    "source": "John Timmer",
    "published_at": "2026-05-29T22:58:29+00:00",
    "summary": "Peer review now optional, political staff would screen grants for forbidden topics.",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/05/kenyan-court-blocks-trump-admin-from-dumping-ebola-exposed-americans-there/",
    "platform": "rss",
    "title": "Kenyan court blocks Trump admin from dumping Ebola-exposed Americans there",
    "url": "https://arstechnica.com/health/2026/05/kenyan-court-blocks-trump-admin-from-dumping-ebola-exposed-americans-there/",
    "source": "Beth Mole",
    "published_at": "2026-05-29T21:17:09+00:00",
    "summary": "The US has previously built specialized facilities just for this purpose.",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/05/botnet-of-more-than-17-million-devices-dismantled/",
    "platform": "rss",
    "title": "Botnet of more than 17 million devices dismantled",
    "url": "https://arstechnica.com/security/2026/05/botnet-of-more-than-17-million-devices-dismantled/",
    "source": "Dan Goodin",
    "published_at": "2026-05-29T18:46:33+00:00",
    "summary": "The botnet was reportedly tied to a Russia-based residential proxy network.",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/05/analysis-of-texas-measles-outbreak-shows-just-how-dangerous-virus-is/",
    "platform": "rss",
    "title": "Analysis of Texas measles outbreak shows just how dangerous virus is",
    "url": "https://arstechnica.com/health/2026/05/analysis-of-texas-measles-outbreak-shows-just-how-dangerous-virus-is/",
    "source": "Beth Mole",
    "published_at": "2026-05-29T18:35:38+00:00",
    "summary": "About 1 in 5 cases were hospitalized and most of those developed complications.",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/05/house-of-the-dragon-s3-trailer-revels-in-dragons-fire-and-blood/",
    "platform": "rss",
    "title": "House of the Dragon S3 trailer revels in dragons, fire, and blood",
    "url": "https://arstechnica.com/culture/2026/05/house-of-the-dragon-s3-trailer-revels-in-dragons-fire-and-blood/",
    "source": "Jennifer Ouellette",
    "published_at": "2026-05-29T18:21:44+00:00",
    "summary": "\"The crown is a weight that crushes. You'll do things that spell death for all involved.\"",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/05/trump-fcc-warns-all-broadcasters-to-follow-orders-or-be-punished-like-abc/",
    "platform": "rss",
    "title": "Trump FCC warns all broadcasters to follow orders or be punished like ABC",
    "url": "https://arstechnica.com/tech-policy/2026/05/trump-fcc-warns-all-broadcasters-to-follow-orders-or-be-punished-like-abc/",
    "source": "Jon Brodkin",
    "published_at": "2026-05-29T18:09:43+00:00",
    "summary": "ABC says early renewal for all stations is unprecedented, has no legitimate purpose.",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/05/doj-sues-states-that-rejected-ice-requests-for-undercover-license-plates/",
    "platform": "rss",
    "title": "DOJ sues states that rejected ICE requests for undercover license plates",
    "url": "https://arstechnica.com/tech-policy/2026/05/doj-sues-states-that-rejected-ice-requests-for-undercover-license-plates/",
    "source": "Ashley Belanger",
    "published_at": "2026-05-29T17:41:56+00:00",
    "summary": "DOJ keeps accusing ICE monitoring sites of doxing, but evidence remains scarce.",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/05/robot-training-startup-will-send-humans-wearing-cameras-to-clean-your-home/",
    "platform": "rss",
    "title": "Startup offers free home cleaning—if it can record it all for robot training",
    "url": "https://arstechnica.com/ai/2026/05/robot-training-startup-will-send-humans-wearing-cameras-to-clean-your-home/",
    "source": "Jeremy Hsu",
    "published_at": "2026-05-29T16:16:14+00:00",
    "summary": "The latest twist in paying humans to wear head cameras for robot training data.",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/05/f1-in-2026-to-finish-first-first-you-have-to-finish/",
    "platform": "rss",
    "title": "After years of stability, F1 reliability can no longer be taken for granted",
    "url": "https://arstechnica.com/cars/2026/05/f1-in-2026-to-finish-first-first-you-have-to-finish/",
    "source": "Jonathan M. Gitlin",
    "published_at": "2026-05-29T16:03:28+00:00",
    "summary": "Until recently, a driver had maybe a six in ten chance of finishing a race.",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/05/severed-sea-cucumber-appendages-dont-seem-to-die/",
    "platform": "rss",
    "title": "Severed sea cucumber appendages don't seem to die",
    "url": "https://arstechnica.com/science/2026/05/severed-sea-cucumber-appendages-dont-seem-to-die/",
    "source": "Jacek Krywko",
    "published_at": "2026-05-29T15:10:29+00:00",
    "summary": "They seem to reorganize their tissues and then just keep living.",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/05/rocket-report-blue-origin-suffers-setback-spacexs-falcon-9-wins-new-business/",
    "platform": "rss",
    "title": "Rocket Report: A dark day for Blue Origin; Pentagon eyes new launch site",
    "url": "https://arstechnica.com/space/2026/05/rocket-report-blue-origin-suffers-setback-spacexs-falcon-9-wins-new-business/",
    "source": "Stephen Clark",
    "published_at": "2026-05-29T13:03:46+00:00",
    "summary": "A new crew launched to China's Tiangong space station, and one of the astronauts will stay for a year.",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/05/heres-why-the-failure-of-blue-origins-new-glenn-rocket-is-so-catastrophic/",
    "platform": "rss",
    "title": "Here's why the failure of Blue Origin's New Glenn rocket is so catastrophic",
    "url": "https://arstechnica.com/space/2026/05/heres-why-the-failure-of-blue-origins-new-glenn-rocket-is-so-catastrophic/",
    "source": "Eric Berger",
    "published_at": "2026-05-29T12:43:35+00:00",
    "summary": "\"I hope that it makes it far enough away from the pad that it does not cause pad damage.\"",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/05/these-researchers-would-be-in-africa-fighting-ebola-but-trump-cut-their-funding/",
    "platform": "rss",
    "title": "These researchers would be in Africa fighting ebola—but Trump cut their funding",
    "url": "https://arstechnica.com/health/2026/05/these-researchers-would-be-in-africa-fighting-ebola-but-trump-cut-their-funding/",
    "source": "Emily Mullin",
    "published_at": "2026-05-29T10:30:40+00:00",
    "summary": "US Infectious diseases centers launched during COVID have lost their funding under Trump.",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/05/blue-origins-new-glenn-rocket-just-exploded-during-a-static-fire-test/",
    "platform": "rss",
    "title": "The most spectacular rocket explosion since N1 just happened in Florida",
    "url": "https://arstechnica.com/space/2026/05/blue-origins-new-glenn-rocket-just-exploded-during-a-static-fire-test/",
    "source": "Eric Berger",
    "published_at": "2026-05-29T02:21:08+00:00",
    "summary": "New Glenn was due to play a starring role in NASA's Artemis Program.",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/05/2027-audi-rs5-first-drive-a-performance-phev-with-split-personalities/",
    "platform": "rss",
    "title": "2027 Audi RS5 first drive: A performance PHEV with split personalities",
    "url": "https://arstechnica.com/cars/2026/05/2027-audi-rs5-first-drive-a-performance-phev-with-split-personalities/",
    "source": "Jonathan M. Gitlin",
    "published_at": "2026-05-28T22:01:02+00:00",
    "summary": "Audi has developed an entirely new electric torque-vectoring rear differential.",
    "feed": "Ars Technica"
  },
  {
    "id": "rss:https://www.producthunt.com/products/sentinel-10",
    "platform": "rss",
    "title": "Sentinel",
    "url": "https://www.producthunt.com/products/sentinel-10",
    "source": "Ary Indarapu",
    "published_at": "2026-05-29T15:04:29+00:00",
    "summary": "Control your robots from anywhere in the world Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/typeahead",
    "platform": "rss",
    "title": "Typeahead",
    "url": "https://www.producthunt.com/products/typeahead",
    "source": "Hiten Shah",
    "published_at": "2026-05-30T23:47:44+00:00",
    "summary": "AI autocomplete for every app on your Mac Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/mina-meeting-assistant",
    "platform": "rss",
    "title": "Mina",
    "url": "https://www.producthunt.com/products/mina-meeting-assistant",
    "source": "Rohan Chaubey",
    "published_at": "2026-05-26T18:29:06+00:00",
    "summary": "Your AI Teammate now responds and executes during your calls Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/joanium-2",
    "platform": "rss",
    "title": "Joanium",
    "url": "https://www.producthunt.com/products/joanium-2",
    "source": "Joel Jolly",
    "published_at": "2026-05-21T10:19:14+00:00",
    "summary": "Local AI workspace to build and work with your computer Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/trippple-club",
    "platform": "rss",
    "title": "Trippple Club",
    "url": "https://www.producthunt.com/products/trippple-club",
    "source": "Nicolas Grenié",
    "published_at": "2026-05-26T19:17:42+00:00",
    "summary": "Advertise together on Meta Ads and pay 3x less Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/presentify",
    "platform": "rss",
    "title": "Presentify",
    "url": "https://www.producthunt.com/products/presentify",
    "source": "Ram Patra",
    "published_at": "2026-05-18T08:28:43+00:00",
    "summary": "Take your presentation skills to the next level Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/socialecho",
    "platform": "rss",
    "title": "SocialEcho 2.0",
    "url": "https://www.producthunt.com/products/socialecho",
    "source": "Chris Messina",
    "published_at": "2026-05-27T16:57:27+00:00",
    "summary": "AI social media copilot for teams and agents Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/dune-4",
    "platform": "rss",
    "title": "Dune Keypad",
    "url": "https://www.producthunt.com/products/dune-4",
    "source": "Rohan Chaubey",
    "published_at": "2026-05-21T13:04:56+00:00",
    "summary": "Context-aware Mac keypad, w/ Claude + community extensions Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/databox",
    "platform": "rss",
    "title": "Databox MCP",
    "url": "https://www.producthunt.com/products/databox",
    "source": "Rohan Chaubey",
    "published_at": "2026-05-19T11:05:48+00:00",
    "summary": "Chat with your business data inside Claude, ChatGPT and more Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/tokenwise",
    "platform": "rss",
    "title": "Tokenwise",
    "url": "https://www.producthunt.com/products/tokenwise",
    "source": "Théophile Louvart",
    "published_at": "2026-05-31T14:36:39+00:00",
    "summary": "A smart LLM proxy that shows where you're overpaying Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/folk-3",
    "platform": "rss",
    "title": "folk",
    "url": "https://www.producthunt.com/products/folk-3",
    "source": "Garry Tan",
    "published_at": "2026-05-25T21:24:24+00:00",
    "summary": "the AI in your texts that gets stuff done Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/tabstack",
    "platform": "rss",
    "title": "Tabstack Web Research",
    "url": "https://www.producthunt.com/products/tabstack",
    "source": "fmerian",
    "published_at": "2026-05-29T23:25:35+00:00",
    "summary": "Run a research agent with cited answers in a single API call Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/mistral-7b",
    "platform": "rss",
    "title": "Mistral Vibe",
    "url": "https://www.producthunt.com/products/mistral-7b",
    "source": "Zac Zuo",
    "published_at": "2026-06-01T03:25:48+00:00",
    "summary": "I agent for long-running, multi-step work and coding Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/open-caffeine",
    "platform": "rss",
    "title": "Open Caffeine",
    "url": "https://www.producthunt.com/products/open-caffeine",
    "source": "Hoon Choi",
    "published_at": "2026-06-01T03:48:12+00:00",
    "summary": "Keep your Mac awake Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/co-desk",
    "platform": "rss",
    "title": "Emily by Co-Desk",
    "url": "https://www.producthunt.com/products/co-desk",
    "source": "Rafael Romano",
    "published_at": "2026-05-29T10:21:55+00:00",
    "summary": "Voice AI copilot for coworking & coliving operators Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/skylive",
    "platform": "rss",
    "title": "Skylive",
    "url": "https://www.producthunt.com/products/skylive",
    "source": "Samuel Angel Gallo Ocampo",
    "published_at": "2026-05-31T23:30:09+00:00",
    "summary": "Never miss a celestial event, anywhere on Earth Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/r0y-ai-financial-studio",
    "platform": "rss",
    "title": "R0Y OMNI 1.0",
    "url": "https://www.producthunt.com/products/r0y-ai-financial-studio",
    "source": "Bryan Liu",
    "published_at": "2026-05-31T19:03:57+00:00",
    "summary": "Generate more accurate investment dashboards and reports Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/paint-by-json-an-api-client-for-figma",
    "platform": "rss",
    "title": "Paint By JSON | Figma API Client",
    "url": "https://www.producthunt.com/products/paint-by-json-an-api-client-for-figma",
    "source": "Rob McLoughlin",
    "published_at": "2026-05-31T21:45:07+00:00",
    "summary": "Real API data in your mockups made as easy as lorem ipsum. Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/stella-4",
    "platform": "rss",
    "title": "Stella",
    "url": "https://www.producthunt.com/products/stella-4",
    "source": "Senan Gaffori",
    "published_at": "2026-05-31T21:46:27+00:00",
    "summary": "Local natural language search across all your files Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/networkspy",
    "platform": "rss",
    "title": "NetworkSpy",
    "url": "https://www.producthunt.com/products/networkspy",
    "source": "Muhammad Muizzsuddin",
    "published_at": "2026-05-30T01:55:12+00:00",
    "summary": "HTTP(s) proxy debugger with custom viewer Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/tabtasker",
    "platform": "rss",
    "title": "TabTasker",
    "url": "https://www.producthunt.com/products/tabtasker",
    "source": "Çağlar SU",
    "published_at": "2026-05-29T23:00:20+00:00",
    "summary": "Zero servers. Total privacy. Your new favorite toolbox. Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/second-brain-cloudflare",
    "platform": "rss",
    "title": "Second Brain for AI",
    "url": "https://www.producthunt.com/products/second-brain-cloudflare",
    "source": "fmerian",
    "published_at": "2026-05-20T06:21:04+00:00",
    "summary": "Persistent memory for Claude, ChatGPT & Cursor. Free. Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/marqly",
    "platform": "rss",
    "title": "Marqly 5.0",
    "url": "https://www.producthunt.com/products/marqly",
    "source": "Kim",
    "published_at": "2026-05-30T09:30:11+00:00",
    "summary": "Your AI-powered bookmark manager Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/clipto-ai",
    "platform": "rss",
    "title": "Clipto",
    "url": "https://www.producthunt.com/products/clipto-ai",
    "source": "Chris Messina",
    "published_at": "2026-04-27T10:29:24+00:00",
    "summary": "Fully local, natural language search over terabytes of media Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/web-clipper-for-notebooklm",
    "platform": "rss",
    "title": "Web Clipper for NotebookLM",
    "url": "https://www.producthunt.com/products/web-clipper-for-notebooklm",
    "source": "Stéphane Turquay",
    "published_at": "2026-05-09T19:31:45+00:00",
    "summary": "Your ultimate NotebookLM's Chrome Extension Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/oura",
    "platform": "rss",
    "title": "Oura Ring 5",
    "url": "https://www.producthunt.com/products/oura",
    "source": "Zac Zuo",
    "published_at": "2026-05-30T18:05:21+00:00",
    "summary": "The world’s smallest smart ring, now even better Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/exstats",
    "platform": "rss",
    "title": "Exstats",
    "url": "https://www.producthunt.com/products/exstats",
    "source": "fmerian",
    "published_at": "2026-05-18T08:45:37+00:00",
    "summary": "Track your browser extensions and competitors in one place Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/wandesk-ai",
    "platform": "rss",
    "title": "Wandesk",
    "url": "https://www.producthunt.com/products/wandesk-ai",
    "source": "Ben Lang",
    "published_at": "2025-12-06T03:15:50+00:00",
    "summary": "Build Your Own AI Desktop Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/step-3-5-flash",
    "platform": "rss",
    "title": "Step 3.7 Flash",
    "url": "https://www.producthunt.com/products/step-3-5-flash",
    "source": "Zac Zuo",
    "published_at": "2026-05-29T12:47:02+00:00",
    "summary": "Flash-speed agents model that can see and act Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/wingbits-ai",
    "platform": "rss",
    "title": "Wingbits AI",
    "url": "https://www.producthunt.com/products/wingbits-ai",
    "source": "Ben Lang",
    "published_at": "2026-05-11T19:20:03+00:00",
    "summary": "AI agents for real-time aircraft monitoring and alerts Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://36kr.com/p/3834544830721671?f=rss",
    "platform": "rss",
    "title": "豆包6月下旬正式付费，并加速打通抖音电商丨独家",
    "url": "https://36kr.com/p/3834544830721671?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T11:44:01+00:00",
    "summary": "5月初旬，豆包将推出付费订阅服务的消息，引发市场广泛讨论。其在苹果App Store中更新的付费订阅方案显示，豆包将推出四档收费标准：基础版、标准版、加强版、专业版。对应的月收费价格为：免费、68元、200元、500元；年收费价格为：免费、688元、2048元、5088元。 随后官方回应：“豆包始终提供免费服务。在免费服务的基础上，我们也在探索推出更多增值内容，以满足不同用户的差异化需求。” 据36氪独家了解，以上只是豆包商业化的预热动作。在接下来的季度中，豆包将持续推进商业化的落地。知情人士透露，豆包预计将在6月下旬正式上线付费内容，并于同期举行的Force大会上更新相关功能。之所以选择这一",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/p/3826034537223043?f=rss",
    "platform": "rss",
    "title": "量坤科技获数亿元天使轮融资，AI4S急需量子级精度数据 | 36氪独家",
    "url": "https://36kr.com/p/3826034537223043?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T11:06:39+00:00",
    "summary": "「暗涌Waves」独家获悉，量子计算公司「量坤科技」近日完成数亿元人民币天使轮、天使+轮融资。本轮系列融资由英诺天使基金领投，国汽投资、北工投资、BV百度风投、水木清华校友基金、明势创投等多家机构参与投资。光源资本担任独家财务顾问。 这笔融资背后，是一个逐渐清晰的判断：AI for Science需要量子计算。 AI可以学习规律，但模型能力上限，受制于它所见过世界的“分辨率”。在化学、材料与医药等研发场景中，如果底层数据的精度不够，模型预测结果也会显著受限。 量子计算，天然适合模拟分子结构、化学键等体系。作为一种高精度求解器，它有可能输出更接近物理世界规律的计算结果；计算产出的量子级高精度数据",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/p/3834354415347337?f=rss",
    "platform": "rss",
    "title": "氪星晚报｜中国国新等在杭州成立创业投资基金，出资额10.01亿；天津人工智能传感器产业园正式开园，首批10家企业集中签约；浙江：拟实施“星火计划”培育未来产业行动，加速量子技术产品规模化应用",
    "url": "https://36kr.com/p/3834354415347337?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T10:56:21+00:00",
    "summary": "大公司： 中通快递在广州成立新物流公司，注册资本5亿 36氪获悉，天眼查App显示，近日，广州中竞物流有限公司成立，法定代表人为范嘉玮，注册资本5亿人民币，经营范围包括国内货物运输代理、机械设备租赁、计算机系统服务等。股东信息显示，该公司由中通快递股份有限公司全资持股。 OpenAI官宣进军机器人赛道，短期内专注研发协助型机器人 OpenAI CEO山姆·奥特曼在社交平台发布OpenAI Robotics招聘信息，称公司正在寻找杰出的全栈硬件、运营、系统及机器学习工程师，共同编程并制造对社会真正有用的机器人。奥特曼表示，人工智能应当能够在现实世界中帮助人类。短期内，OpenAI专注于研发能够协",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/p/3834276149356420?f=rss",
    "platform": "rss",
    "title": "今年盛夏，WAVES之夜会浪的一群年轻人",
    "url": "https://36kr.com/p/3834276149356420?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T10:26:33+00:00",
    "summary": "一、每一年，我们都在找一个地方，让年轻人在一起 WAVES之夜是WAVES独有的标签。 不是又一个分论坛，不是又一个颁奖礼，不是又一场穿西装坐两小时的行业对话。它是WAVES的\"晚上\"——白天属于议程和逻辑，夜晚属于人和直觉。 2023年，我们把年轻人和创业者拉到了北京金海湖的碧波岛上。那个夜晚，有人在草坪上喝啤酒，有人在帐篷里聊融资条款，有人在露天电影前什么都没想，发了一小时呆。暗涌WAVES后来写了一段话，成了WAVES之夜最好的一句注脚： \"几年、十几年甚至更长的时间之后，我们今天在场的人中如果有一些人，会一不小心想起今天，大概大多数记忆都是模糊，但你也会觉得这是一个美好的夏天夜晚。有落",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/p/3834427736024965?f=rss",
    "platform": "rss",
    "title": "硬氪首发 | 获近2亿元融资，这家公司用无损Micro-LED加速AI眼镜全彩化进程",
    "url": "https://36kr.com/p/3834427736024965?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T09:42:20+00:00",
    "summary": "作者&nbsp;|&nbsp;林晴晴 编辑&nbsp;|&nbsp;袁斯来 硬氪获悉，Micro-LED显示技术公司「秋水半导体」已于近期连续完成Pre-A及A轮融资，合计近2亿元人民币。本轮融资由朝晖资本领投，通商基金、盛宇投资、宁波人才发展基金、嘉溢创投、涌现科技、数字光芯及兴棠资本跟投，兴棠资本担任长期财务顾问。本轮融资资金将主要用于在宁波高新区建设8英寸混合键合量产线及后续研发投入。 「秋水半导体」成立于2022年11月，是一家专注于Micro-LED微显示芯片与模组的半导体公司，产品覆盖数字车灯、AR眼镜、微投影等应用领域。公司总部原在苏州，近期已整体搬迁至宁波。 Micro-LED",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/p/3834297577383553?f=rss",
    "platform": "rss",
    "title": "我们有全世界最多的运动鞋，却没有一支值得爱20年的球队",
    "url": "https://36kr.com/p/3834297577383553?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T09:29:10+00:00",
    "summary": "编者按： 当中国体育用品业总产出突破2万亿元，占据体育产业总产出的54.3%，这无疑是一份值得骄傲的成绩单。过去几十年，中国建立起全球最完整、最高效的体育用品供应链，也孕育出一批具有国际竞争力的品牌。 但在规模增长之外，另一个问题同样值得关注：当体育产业的大部分价值仍来自商品制造与销售，我们距离一个成熟的体育文化生态还有多远？赛事、IP、社区、俱乐部、体育传媒，以及由此产生的情感认同与共同体文化，是否正在成为中国体育下一阶段发展的关键命题？ 本文并非讨论体育用品行业本身，而是试图透过“54.3%”这一数字，重新审视中国体育产业的结构与未来。 文/邹国俊（前散打冠军，有“亚洲第一快腿”之称。“英",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/p/3832924137138057?f=rss",
    "platform": "rss",
    "title": "「AromeManpo馥郁满铺」完成近亿元B轮融资，今年��下门店将突破10家",
    "url": "https://36kr.com/p/3832924137138057?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T08:06:01+00:00",
    "summary": "作者 | &nbsp;钟艺璇 36氪获悉，芳香馥愈&nbsp;情绪护肤品牌「AromeManpo馥郁满铺」已于近期完成近亿元B轮融资，投资方为颖通控股，穆棉资本作为独家财务顾问。交易完成后，颖通控股将获得杭州白昼与梦生物科技有限公司（馥郁满铺母公司）增资完成后15%的股权。 馥郁满铺诞生于2013年，品牌灵感最初来源于创始人姜腾数十年的芳疗基因，承传欧洲芳疗系统，融汇东西方植物智慧与前沿发酵科技，以香为引，秉持“芳香馥愈，情绪护肤”的品牌定位，带用户奔赴回归本真的感官之旅。品牌目前已推出「晚香玉光感发酵系列」「黑鸢尾赋活琉金系列」两条功效芳疗面护线，创《植物图鉴》与「东方非遗」x中国节IP两大",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/p/3834310434875011?f=rss",
    "platform": "rss",
    "title": "连续完成五源、峰瑞两轮数千万元融资，清华00后团队要解决Token账单焦虑｜智能涌现首发",
    "url": "https://36kr.com/p/3834310434875011?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T07:49:38+00:00",
    "summary": "文｜王欣逸 编辑｜邓咏仪 万格智元团队有这样一些标签：00后、博士团队、埋头搞技术。 CEO王冠博恰好占全了，他现博士就读于清华大学计算机系，是一位00后连续创业者。 其团队相当年轻，规模约20人，其中近90%的成员为00后，大多数为清华、北大等院校的硕博生，也有来自亚马逊、OpenAI、字节跳动等公司的成员。 《智能涌现》独家获悉，近日，万格智元连续完成两轮五源资本、峰瑞资本参投的数千万元天使轮及天使+轮融资，源合资本担任独家财务顾问。本轮融资将用于产品研发和市场推广。 在过去，算力上云几乎是必选项。随着Claude Code、Codex、OpenClaw等Agent能力的爆发，Token需",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/p/3824416083825027?f=rss",
    "platform": "rss",
    "title": "获国家队采购、联名比音勒芬，「PLAYTOP」想用东方美学演绎户外功能服饰｜早期项目",
    "url": "https://36kr.com/p/3824416083825027?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T03:19:10+00:00",
    "summary": "当户外运动品牌纷纷在“防晒”“速干”“保暖”等参数上展开竞赛时，一家成立仅三年的新锐品牌，开始在功能的基础上，将“东方美学”元素融入一件功能衣中。 成立于2022年的「PLAYTOP」，是一家将东方美学与天然功能材料融合的户外品牌，瞄准25-40岁追求颜值与舒适体验的高智菁英人群。2025年雪季，PLAYTOP做到了小红书滑雪速干衣用户主动搜索排名第一。 目前，PLAYTOP已获得12项独家专利及多国环保创意新材料奖，产品被国家队和军事科学院采购，也是首个连续登上中国国际时装周的户外针织品牌。 PLAYTOP的诞生，源于一个“奢品+供应链”的组合。创始人梁辰是服装设计出身，曾任职香奈儿和巴宝莉",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/p/3833985105782402?f=rss",
    "platform": "rss",
    "title": "硬氪观察 | 苹果代工厂开造人形机器人，一场豪赌未来的产能大迁移",
    "url": "https://36kr.com/p/3833985105782402?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T02:12:48+00:00",
    "summary": "作者&nbsp;|&nbsp;邱晓芬 编辑&nbsp;|&nbsp;袁斯来 在龙旗位于南昌的智能制造工厂中，两台智元精灵G2人形机器人已融入平板产线，承担起多媒体集成测试（MMIT）工站的上下料作业。 其工作节拍已接近熟练产线员工——依托腰部的三个运动自由度与全向移动底盘，机器人精准从传送带抓取生产完成的平板，送入检测机箱；待测试完毕，又能迅速取出合格产品、利落放回传送带分流。 据现场实测数据，单台机器人每小时可稳定处理约310台平板设备，峰值达316台，8小时连续作业整体成功率超99.5% 这并非一次单纯的展示。 2026年，中国的具身智能机器人热潮中，一大波市值百亿、千亿手机供应链巨头躬身",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834546448723585?f=rss",
    "platform": "rss",
    "title": "银河电子：控股股东未减持公司股份并提前终止减持计划",
    "url": "https://36kr.com/newsflashes/3834546448723585?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T11:42:21+00:00",
    "summary": "36氪获悉，银河电子公告，公司控股股东银河电子集团投资有限公司原拟减持公司股份不超过909.96万股（占本公司总股本0.81%）。公司于近日收到银河电子集团投资有限公司出具的《关于股份减持计划提前终止的告知函》，截至本公告披露日，银河电子集团投资有限公司未减持公司股份，并决定提前终止上述减持计划。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834538829688707?f=rss",
    "platform": "rss",
    "title": "深振业A：拟1.5亿元出售5项深圳地区自有物业",
    "url": "https://36kr.com/newsflashes/3834538829688707?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T11:34:36+00:00",
    "summary": "36氪获悉，深振业A公告，为盘活存量资产，提高资产周转与资金使用效率，公司董事会同意采用公开挂牌方式在深圳联合产权交易所公开挂牌转让5项深圳地区自有物业，包括：宝丽大厦裙楼二层、宝丽大厦裙楼三层、星海名城三期幼儿园整栋、星海名城组团一商铺肉菜市场一层、星海名城组团一商铺肉菜市场二层。本次拟出售物业挂牌底价总计1.5亿元。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834536817880704?f=rss",
    "platform": "rss",
    "title": "《北京市卫星物联网产业发展规划（框架）》发布",
    "url": "https://36kr.com/newsflashes/3834536817880704?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T11:32:33+00:00",
    "summary": "6月1日，北京市卫星物联网行业发展大会在海淀举办。会上，北京市经济和信息化局航空航天产业处处长周斌发布《北京市卫星物联网产业发展规划（框架）》。按照规划，北京力争2030年建成全国首个卫星互联网示范城市、产业集聚区与全球知名创新高地。规划同时部署五大重点工作，从基础设施建设、核心技术攻关、应用场景培育、产业生态构建，到区域协同与国际化发展全面发力，推动产业提质增效。（证券时报）",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834533163036291?f=rss",
    "platform": "rss",
    "title": "消息称SpaceX保留最多5%的IPO A类股份，供特定人士认购",
    "url": "https://36kr.com/newsflashes/3834533163036291?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T11:28:50+00:00",
    "summary": "消息称，SpaceX保留最多5%的IPO A类股份，供特定人士认购。（财联社）",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834530577067650?f=rss",
    "platform": "rss",
    "title": "赛力斯：5月份销量36480辆，同比下降17.38%",
    "url": "https://36kr.com/newsflashes/3834530577067650?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T11:26:12+00:00",
    "summary": "36氪获悉，赛力斯发布5月份产销快报，5月份销量36480辆，同比下降17.38%；本年累计销量160386辆，同比增长8.18%。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834523900046979?f=rss",
    "platform": "rss",
    "title": "健康元：重组人促卵泡激素注射液获得药品注册证书",
    "url": "https://36kr.com/newsflashes/3834523900046979?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T11:19:25+00:00",
    "summary": "36氪获悉，健康元公告，近日，控股子公司丽珠医药集团股份有限公司的子公司珠海市丽珠单抗生物技术有限公司收到国家药品监督管理局核准签发的《药品注册证书》。药品通用名称为重组人促卵泡激素注射液，商品名称为丽优宝。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834521574829698?f=rss",
    "platform": "rss",
    "title": "高通美股盘前跌幅扩大至10%",
    "url": "https://36kr.com/newsflashes/3834521574829698?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T11:17:03+00:00",
    "summary": "36氪获悉，高通美股盘前跌幅扩大至10%。消息面上，英伟达此前宣布推出PC端“超级芯片”，与苹果、高通、英特尔及AMD展开正面角逐。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834512402624384?f=rss",
    "platform": "rss",
    "title": "黄仁勋宣布：联手宇树打造1.8米参考人形机器人",
    "url": "https://36kr.com/newsflashes/3834512402624384?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T11:07:43+00:00",
    "summary": "6月1日，英伟达首席执行官黄仁勋宣布，英伟达已与宇树科技合作，推出新一代人形机器人参考设计H2+，也被称为Isaac GR00T系统，以加速全球人形机器人行业创新。黄仁勋在演讲中表示，这套系统已经完成整体集成。机器人本体拥有31个自由度，每只机械手拥有25个自由度，整机身高约1.8米、重量约68公斤。（红星新闻）",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834511006346888?f=rss",
    "platform": "rss",
    "title": "名创优品：叶国富增持约5382.8万港元公司股份",
    "url": "https://36kr.com/newsflashes/3834511006346888?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T11:06:18+00:00",
    "summary": "36氪获悉，名创优品在港交所公告，公司此前披露控股股东、执行董事、董事会主席兼首席执行官叶国富计划自2026年4月23日起12个月内增持公司股份，总金额不少于5000万港元。本次叶国富于2026年5月29日及6月1日以平均价格约每股25.63港元于公开市场购买合共210万股普通股，总金额约5382.8万港元。增持后，叶国富直接及间接持有7.92亿股，占公司已发行股份约63.9%。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834505546540935?f=rss",
    "platform": "rss",
    "title": "五粮液：首次回购公司股份119万股，成交总金额约1亿元",
    "url": "https://36kr.com/newsflashes/3834505546540935?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T11:00:45+00:00",
    "summary": "36氪获悉，五粮液公告，公司于2026年5月29日首次通过回购专用证券账户以集中竞价交易方式回购公司股份1191013股，占公司总股本的0.03%，最高成交价为85.25元/股，最低成交价为82.28元/股，成交总金额为1亿元（不含交易费用）。截至2026年5月31日，公司累计回购股份1191013股，支付总金额1亿元。本次回购符合相关法律法规及公司回购方案要求。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834499945358980?f=rss",
    "platform": "rss",
    "title": "创新医疗：拟5000万元—1亿元回购股份",
    "url": "https://36kr.com/newsflashes/3834499945358980?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T10:55:03+00:00",
    "summary": "36氪获悉，创新医疗公告，公司拟以5000万元—1亿元回购股份，用于维护公司价值及股东权益所必需。回购价格不超过20元/股。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834491535107973?f=rss",
    "platform": "rss",
    "title": "豆包6月下旬正式付费，并加速打通抖音电商",
    "url": "https://36kr.com/newsflashes/3834491535107973?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T10:46:29+00:00",
    "summary": "5月初旬，豆包将推出付费订阅服务的消息，引发市场广泛讨论。据36氪独家了解，以上只是豆包商业化的预热动作。在接下来的季度中，豆包将持续推进商业化的落地。知情人士透露，豆包预计将在6月下旬正式上线付费内容，并于同期举行的Force大会上更新相关功能。之所以选择这一时间节点，是因为PC端与移动端仍需约一个月时间，完成基础功能与收费体系的适配改造。据36氪了解，若进展顺利，豆包将于三季度进一步结合电商功能更新完善付费场景，并通过补贴为抖音商城进行引流，四季度进入运行期。这些动作，皆是为了面向2027年及更长期的商业化回报做准备。因此，2026年豆包将不会把付费用户的渗透率作为考察指标。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834475052787586?f=rss",
    "platform": "rss",
    "title": "比亚迪5月汽车销量38.3万辆",
    "url": "https://36kr.com/newsflashes/3834475052787586?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T10:29:43+00:00",
    "summary": "36氪获悉，比亚迪5月汽车销量383453辆，今年累计销量1405039辆，累计同比下降20.32%。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834469689140871?f=rss",
    "platform": "rss",
    "title": "机构今日买入东山精密等27股，卖出华能国际1.99亿元",
    "url": "https://36kr.com/newsflashes/3834469689140871?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T10:24:16+00:00",
    "summary": "盘后数据显示，6月1日龙虎榜中，共57只个股出现了机构的身影，有27只股票呈现机构净买入，30只股票呈现机构净卖出。当天机构净买入前三的股票分别是风华高科、东山精密、新集能源，净买入金额分别是12.41亿元、10.34亿元、5.36亿元。当天机构净卖出前三的股票分别是华能国际、宇晶股份、信音电子，净流出金额分别是1.99亿元、1.09亿元、7632万元。（第一财经）",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834465837115008?f=rss",
    "platform": "rss",
    "title": "鼎龙科技：拟投资1000万元认购守正基金部分股权",
    "url": "https://36kr.com/newsflashes/3834465837115008?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T10:20:21+00:00",
    "summary": "36氪获悉，鼎龙科技公告，公司于5月29日与硬核坚果资本签订了《嘉兴坚持守正股权投资合伙企业（有限合伙）合伙协议》，参与硬核坚果资本设立、管理的嘉兴坚持守正股权投资合伙企业（有限合伙）（简称“守正基金”）。公司作为有限合伙人以自有资金认购出资份额1000万元。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834460452497028?f=rss",
    "platform": "rss",
    "title": "康方生物获南向资金净买入27.07亿港元",
    "url": "https://36kr.com/newsflashes/3834460452497028?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T10:14:52+00:00",
    "summary": "南向资金净买入46.57亿港元，康方生物、腾讯控股、泡泡玛特净买入额位列前三，分别获净买入27.07亿港元、10.24亿港元、8.01亿港元。净卖出方面，联想集团、小米集团-W、建滔积层板分别遭净卖出5.48亿港元、3.53亿港元、2.08亿港元。（第一财经）",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834457275590531?f=rss",
    "platform": "rss",
    "title": "牧原股份：选举曹治年为董事长",
    "url": "https://36kr.com/newsflashes/3834457275590531?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T10:11:38+00:00",
    "summary": "36氪获悉，牧原股份公告，公司董事会于近日收到秦英林、曹治年递交的辞任报告。根据公司制度，秦英林已到规定退休年龄，现依据制度申请辞去公司董事、董事长、战略委员会及可持续发展委员会委员、总裁职务；曹治年申请辞去公司副董事长、常务副总裁、财务负责人职务。公司于6月1日召开了第五届董事会第十六次会议，选举曹治年为公司第五届董事会董事长，担任第五届董事会战略委员会及可持续发展委员会主任委员，任期自本次董事会审议通过之日起至第五届董事会任期届满之日止。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834445075195528?f=rss",
    "platform": "rss",
    "title": "多家全国性银行今年不再报送数据，房地产贷款集中度管理进一步“放松”",
    "url": "https://36kr.com/newsflashes/3834445075195528?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T09:59:14+00:00",
    "summary": "记者近日从多家全国性银行了解到，2021年起执行的“商业银行房地产贷款‘五档两线’集中度管理制度”已进一步“放松”，有关部门去年底已不再要求专门上报相关数据。一家全国性商业银行对公业务负责人向记者证实，今年该行没有报送数据，因去年底有关部门曾口头传达相关数据不再报送。一家全国性商业银行负责贷款统计和管理的人士亦对记者表示，有关部门已经不再向银行提及房地产贷款占比的情况，“没再听说有相关要求”。（财联社）",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834441488557705?f=rss",
    "platform": "rss",
    "title": "我国正式发布非化石能源电力消费核算指南",
    "url": "https://36kr.com/newsflashes/3834441488557705?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T09:55:35+00:00",
    "summary": "国家发展改革委、国家能源局等5部门近日联合印发出台了《非化石能源电力消费核算指南（试行）》，标志着我国在非化石能源电力消费的核算上有了统一的“标尺”，为更好推动碳排放双控制度实施奠定了制度基础。据介绍，我国95%的非化石能源都是以电力形式被消费的，精准核算这部分电量，是衡量非化石能源消费占比、开展碳排放双控考核等的核心基础。此前，各地核算多以省级为主，地市和企业层面缺乏统一方法，电能量交易、绿证交易、碳排放核算等规则缺乏充分衔接。此次出台的《指南》，对非化石能源电力消费的认定方式和核算方法做出了具体规定。（央视新闻）",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834440142088070?f=rss",
    "platform": "rss",
    "title": "“秋水半导体”连续完成Pre-A及A轮融资",
    "url": "https://36kr.com/newsflashes/3834440142088070?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T09:54:13+00:00",
    "summary": "36氪获悉，Micro-LED显示技术公司“秋水半导体”已于近期连续完成Pre-A及A轮融资，合计近2亿元人民币。本轮融资由朝晖资本领投，通商基金、盛宇投资、宁波人才发展基金、嘉溢创投、涌现科技、数字光芯及兴棠资本跟投，兴棠资本担任长期财务顾问。本轮融资资金将主要用于在宁波高新区建设8英寸混合键合量产线及后续研发投入。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://sspai.com/post/110547",
    "platform": "rss",
    "title": "派评 | 近期值得关注的 App",
    "url": "https://sspai.com/post/110547",
    "source": "少数派编辑部",
    "published_at": "2026-06-01T09:57:27+00:00",
    "summary": ">下载少数派2.0客户端、关注少数派公众号，解锁全新阅读体验📰>实用、好用的正版软件，少数派为你呈现🚀查看全文",
    "feed": "少数派"
  },
  {
    "id": "rss:https://sspai.com/post/110412",
    "platform": "rss",
    "title": "成本 600 元不到，我 3D 打印了一把能弹的电吉他",
    "url": "https://sspai.com/post/110412",
    "source": "MapleShadow",
    "published_at": "2026-06-01T07:00:00+00:00",
    "summary": "有时候，完成比完美更重要。查看全文",
    "feed": "少数派"
  },
  {
    "id": "rss:https://sspai.com/post/110094",
    "platform": "rss",
    "title": "把一句经文放进每天：「一日一偈」的轻阅读尝试",
    "url": "https://sspai.com/post/110094",
    "source": "Cloud001",
    "published_at": "2026-06-01T03:01:26+00:00",
    "summary": "Matrix首页推荐Matrix是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选Matrix最优质的文章，展示来自用户的最真实的体验和观点。文章代表作者个人观点 ...查看全文",
    "feed": "少数派"
  },
  {
    "id": "rss:https://sspai.com/post/110519",
    "platform": "rss",
    "title": "派早报：Anthropic 估值超过 OpenAI",
    "url": "https://sspai.com/post/110519",
    "source": "少数派编辑部",
    "published_at": "2026-05-31T23:26:34+00:00",
    "summary": "Anthropic 估值超过 OpenAI海盗湾被查封二十周年，至今仍维持运营高通推出骁龙 C 系列，用于对标 MacBook Neo 的笔记本 PCLast.fm 重归独立运营vivo 发布 vivo S60 系列北京互联网法院称有未成年人游戏充值单案超 60 万元比尔·盖茨公众形象面临空前危机看看就行的简讯少数派的近期动态你可能错过的好文章查看全文",
    "feed": "少数派"
  },
  {
    "id": "rss:https://sspai.com/post/110488",
    "platform": "rss",
    "title": "本月玩什么｜混音青春、007 初露锋芒、归零巡礼、地平线 6",
    "url": "https://sspai.com/post/110488",
    "source": "板斧",
    "published_at": "2026-05-31T06:36:11+00:00",
    "summary": "给你的快乐查漏补缺。查看全文",
    "feed": "少数派"
  },
  {
    "id": "rss:https://sspai.com/post/110172",
    "platform": "rss",
    "title": "AI 如何影响你的审美？",
    "url": "https://sspai.com/post/110172",
    "source": "AstrianZ",
    "published_at": "2026-05-30T09:04:38+00:00",
    "summary": "去感受、去思考、去创作吧，这是只有身为人类的你能做到的事情。查看全文",
    "feed": "少数派"
  },
  {
    "id": "rss:https://sspai.com/post/110446",
    "platform": "rss",
    "title": "本周看什么 | 最近值得一看的 8 部作品",
    "url": "https://sspai.com/post/110446",
    "source": "少数派编辑部",
    "published_at": "2026-05-29T10:12:15+00:00",
    "summary": "📅本周新预告《玩具总动员5》终极预告5月26日，皮克斯动画电影《玩具总动员5》发布了终极预告，将于6月19日内地上映。安德鲁·斯坦顿、麦肯纳·哈里斯执导，胡迪、巴斯光年、翠丝等老朋友们回归，无所不能的 ...查看全文",
    "feed": "少数派"
  },
  {
    "id": "rss:https://sspai.com/prime/story/how-to-renovate-a-rental-bedroom",
    "platform": "rss",
    "title": "住久了没意思（三）：打造能好好放松的卧室",
    "url": "https://sspai.com/prime/story/how-to-renovate-a-rental-bedroom",
    "source": "程天冲",
    "published_at": "2026-05-29T09:20:56+00:00",
    "summary": "前文回顾：租房常见问题与我的改造原则从有光的地方开始动手对大部分人来说，卧室可能是在家里待得最长时间的区域。除了每天睡觉，周末可能也会花很多时间赖在卧室；如果家里比较小，卧室还可能承担休闲和娱乐的功能 ...查看全文本文为会员文章，出自《单篇文章》，订阅后可阅读全文。",
    "feed": "少数派"
  },
  {
    "id": "rss:https://sspai.com/post/110106",
    "platform": "rss",
    "title": "Await：五分钟，把点子变成 iPhone 小组件",
    "url": "https://sspai.com/post/110106",
    "source": "maundytime",
    "published_at": "2026-05-29T07:00:28+00:00",
    "summary": "我希望 Await 最后留下的，是一种更轻的创作入口：不必很大，但足够好看和好玩，也足够贴近自己每天使用手机的方式。查看全文",
    "feed": "少数派"
  },
  {
    "id": "rss:https://sspai.com/post/110120",
    "platform": "rss",
    "title": "什么才是「好」的 Android 音频输出？从一台旧日 Xperia 说起",
    "url": "https://sspai.com/post/110120",
    "source": "纳兰音韵",
    "published_at": "2026-05-29T02:57:32+00:00",
    "summary": "Android 早已具备高质量音频输出的能力，但一段声音从在抵达耳机之前，往往还要经过系统层层处理。下面我们一起探究 Android 高保真输出背后的秘密。查看全文",
    "feed": "少数派"
  },
  {
    "id": "hn:48196570",
    "platform": "hackernews",
    "title": "Gemini 3.5 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/",
    "source": "spectraldrift",
    "published_at": "2026-05-19T17:43:45+00:00",
    "summary": "",
    "points": 962,
    "comments": 658
  },
  {
    "id": "hn:48111896",
    "platform": "hackernews",
    "title": "Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model",
    "url": "https://github.com/cactus-compute/needle",
    "source": "HenryNdubuaku",
    "published_at": "2026-05-12T18:03:11+00:00",
    "summary": "",
    "points": 776,
    "comments": 211
  },
  {
    "id": "hn:48196867",
    "platform": "hackernews",
    "title": "Gemini CLI will stop working from June 18, 2026",
    "url": "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/",
    "source": "primaprashant",
    "published_at": "2026-05-19T18:03:10+00:00",
    "summary": "",
    "points": 406,
    "comments": 210
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
    "id": "hn:48050278",
    "platform": "hackernews",
    "title": "AlphaEvolve: Gemini-powered coding agent scaling impact across fields",
    "url": "https://deepmind.google/blog/alphaevolve-impact/",
    "source": "berlianta",
    "published_at": "2026-05-07T15:02:20+00:00",
    "summary": "",
    "points": 327,
    "comments": 149
  },
  {
    "id": "hn:48196609",
    "platform": "hackernews",
    "title": "Gemini Omni",
    "url": "https://deepmind.google/models/gemini-omni/",
    "source": "meetpateltech",
    "published_at": "2026-05-19T17:46:19+00:00",
    "summary": "",
    "points": 323,
    "comments": 146
  },
  {
    "id": "hn:48196656",
    "platform": "hackernews",
    "title": "Gemini 3.5 Flash: frontier intelligence with action",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/",
    "source": "meetpateltech",
    "published_at": "2026-05-19T17:49:50+00:00",
    "summary": "",
    "points": 180,
    "comments": 1
  },
  {
    "id": "hn:48080702",
    "platform": "hackernews",
    "title": "Gemini API File Search is now multimodal",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/expanded-gemini-api-file-search-multimodal-rag/",
    "source": "gmays",
    "published_at": "2026-05-10T03:22:02+00:00",
    "summary": "",
    "points": 156,
    "comments": 46
  },
  {
    "id": "hn:48297467",
    "platform": "hackernews",
    "title": "Gemini, Gophers, and Fingers. Oh My Alternative Internets Beyond HTTPS",
    "url": "https://brennan.day/gemini-gophers-and-fingers-oh-my-alternative-internets-beyond-https/",
    "source": "ChrisArchitect",
    "published_at": "2026-05-27T17:24:25+00:00",
    "summary": "",
    "points": 146,
    "comments": 85
  },
  {
    "id": "hn:48221976",
    "platform": "hackernews",
    "title": "Gemini randomly dumped its system prompt",
    "url": "https://gist.github.com/mkaramuk/44a44d83178e632ec0dd1f02186d822c",
    "source": "mkaramuk",
    "published_at": "2026-05-21T13:04:21+00:00",
    "summary": "",
    "points": 94,
    "comments": 44
  },
  {
    "id": "hn:48084710",
    "platform": "hackernews",
    "title": "Chrome's AI features may be hogging 4GB of your computer storage",
    "url": "https://www.theverge.com/tech/924933/google-chrome-4gb-gemini-nano-ai-features",
    "source": "birdculture",
    "published_at": "2026-05-10T15:22:46+00:00",
    "summary": "",
    "points": 117,
    "comments": 59
  },
  {
    "id": "hn:47989883",
    "platform": "hackernews",
    "title": "VS Code inserting 'Co-Authored-by Copilot' into commits regardless of usage",
    "url": "https://github.com/microsoft/vscode/pull/310226",
    "source": "indrora",
    "published_at": "2026-05-02T19:57:26+00:00",
    "summary": "",
    "points": 1513,
    "comments": 850
  },
  {
    "id": "hn:48272354",
    "platform": "hackernews",
    "title": "Microsoft Copilot Cowork Exfiltrates Files",
    "url": "https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files",
    "source": "Kneenex",
    "published_at": "2026-05-25T21:45:57+00:00",
    "summary": "",
    "points": 264,
    "comments": 49
  },
  {
    "id": "hn:48029753",
    "platform": "hackernews",
    "title": "Xbox CEO ends Copilot AI development and overhauls leadership",
    "url": "https://www.dexerto.com/gaming/xbox-ceo-ends-copilot-ai-development-overhauls-leadership-3361353/",
    "source": "gmays",
    "published_at": "2026-05-05T22:43:47+00:00",
    "summary": "",
    "points": 113,
    "comments": 42
  },
  {
    "id": "hn:48031707",
    "platform": "hackernews",
    "title": "Update on \"Co-authored-by: Copilot\" in commit messages",
    "url": "https://github.com/microsoft/vscode/issues/314311",
    "source": "extesy",
    "published_at": "2026-05-06T03:15:05+00:00",
    "summary": "",
    "points": 102,
    "comments": 66
  },
  {
    "id": "hn:48176987",
    "platform": "hackernews",
    "title": "Microsoft admits Windows 11's dedicated Copilot key breaks certain workflows",
    "url": "https://www.windowscentral.com/microsoft/windows-11/microsoft-admits-windows-11s-dedicated-copilot-key-breaks-certain-workflows-confirms-plans-to-let-users-restore-right-ctrl-or-context-menu-key-later-this-year",
    "source": "01-_-",
    "published_at": "2026-05-18T08:53:29+00:00",
    "summary": "",
    "points": 20,
    "comments": 10
  },
  {
    "id": "hn:48248839",
    "platform": "hackernews",
    "title": "Surface laptop ships with 8GB RAM for $1299 despite pushing 16GB for Copilot PCs",
    "url": "https://www.windowslatest.com/2026/05/21/microsoft-pushed-16gb-ram-as-must-have-for-windows-11-for-years-now-sells-an-8gb-surface-laptop-for-1299/",
    "source": "MoltenMonster",
    "published_at": "2026-05-23T16:10:39+00:00",
    "summary": "",
    "points": 14,
    "comments": 4
  },
  {
    "id": "hn:48192224",
    "platform": "hackernews",
    "title": "Apple unveils new accessibility features",
    "url": "https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/",
    "source": "interpol_p",
    "published_at": "2026-05-19T12:04:18+00:00",
    "summary": "",
    "points": 726,
    "comments": 382
  },
  {
    "id": "hn:48032167",
    "platform": "hackernews",
    "title": "Apple agrees to pay iPhone owners $250M for not delivering AI Siri",
    "url": "https://www.theverge.com/tech/924706/apple-iphone-siri-intelligence-class-action-lawsuit-settlement",
    "source": "Garbage",
    "published_at": "2026-05-06T04:28:17+00:00",
    "summary": "",
    "points": 20,
    "comments": 6
  },
  {
    "id": "hn:48233563",
    "platform": "hackernews",
    "title": "Steve Wozniak cheered after telling students they have AI – actual intelligence",
    "url": "https://www.businessinsider.com/steve-wozniak-apple-ai-graduation-speech-2026-5",
    "source": "signa11",
    "published_at": "2026-05-22T09:04:54+00:00",
    "summary": "",
    "points": 650,
    "comments": 548
  },
  {
    "id": "hn:48018965",
    "platform": "hackernews",
    "title": "A complete Llama2 inference engine that fits in 1356 bytes of x86 assembly",
    "url": "https://github.com/rdmsr/sectorllm",
    "source": "monax",
    "published_at": "2026-05-05T06:53:34+00:00",
    "summary": "",
    "points": 27,
    "comments": 0
  },
  {
    "id": "hn:48329957",
    "platform": "hackernews",
    "title": "Llama.cpp now has an official website: llama.app",
    "url": "https://twitter.com/ggerganov/status/2060394400237109567",
    "source": "julien_c",
    "published_at": "2026-05-29T22:08:47+00:00",
    "summary": "",
    "points": 17,
    "comments": 4
  },
  {
    "id": "hn:48029334",
    "platform": "hackernews",
    "title": "Zuckerberg 'personally authorized' Meta's copyright infringement, publishers say",
    "url": "https://apnews.com/article/meta-mark-zuckerberg-ai-publishers-lawsuit-llama-5609846d4d840014974a847b01079c32",
    "source": "jethronethro",
    "published_at": "2026-05-05T22:07:18+00:00",
    "summary": "",
    "points": 156,
    "comments": 6
  },
  {
    "id": "hn:48307849",
    "platform": "hackernews",
    "title": "Show HN: LiteParse v2, now in Rust 100x faster",
    "url": "https://github.com/run-llama/liteparse/",
    "source": "pierre",
    "published_at": "2026-05-28T12:15:42+00:00",
    "summary": "",
    "points": 14,
    "comments": 0
  },
  {
    "id": "hn:48153507",
    "platform": "hackernews",
    "title": "Lua as a practical \"soft-bedrock\" language",
    "url": "https://portal.mozz.us/gemini/zaibatsu.circumlunar.space/users/solderpunk/gemlog/lua-as-a-practical-soft-bedrock-language.gmi",
    "source": "birdculture",
    "published_at": "2026-05-15T20:39:48+00:00",
    "summary": "",
    "points": 25,
    "comments": 0
  },
  {
    "id": "hn:48330539",
    "platform": "hackernews",
    "title": "AWS reportedly to tuck Grok into Bedrock, despite zero enterprise demand",
    "url": "https://www.theregister.com/ai-ml/2026/05/29/aws-reportedly-to-tuck-elon-musks-grok-into-bedrock-despite-zero-enterprise-demand/5248832",
    "source": "Jimmc414",
    "published_at": "2026-05-29T23:08:29+00:00",
    "summary": "",
    "points": 17,
    "comments": 9
  },
  {
    "id": "hn:48020872",
    "platform": "hackernews",
    "title": "Google DeepMind workers in UK vote to unionize amid deal with US Military",
    "url": "https://www.theguardian.com/us-news/2026/may/04/google-deepmind-uk-workers-union",
    "source": "moxifly7",
    "published_at": "2026-05-05T11:15:01+00:00",
    "summary": "",
    "points": 20,
    "comments": 1
  },
  {
    "id": "hn:48141146",
    "platform": "hackernews",
    "title": "Google DeepMind Workers Vote to Unionize over Military AI Deals",
    "url": "https://www.wired.com/story/google-deepmind-workers-vote-to-unionize-over-military-ai-deals/",
    "source": "cdrnsf",
    "published_at": "2026-05-14T20:57:35+00:00",
    "summary": "",
    "points": 15,
    "comments": 1
  },
  {
    "id": "hn:48111581",
    "platform": "hackernews",
    "title": "Reimagining the mouse pointer for the AI era",
    "url": "https://deepmind.google/blog/ai-pointer/",
    "source": "devhouse",
    "published_at": "2026-05-12T17:40:13+00:00",
    "summary": "",
    "points": 252,
    "comments": 213
  },
  {
    "id": "hn:48248173",
    "platform": "hackernews",
    "title": "AlphaProof Nexus solves 9 Erdős problems and proves 44 sequence conjectures",
    "url": "https://cryptobriefing.com/deepmind-alphaproof-nexus-erdos-problems/",
    "source": "hackernj",
    "published_at": "2026-05-23T14:46:56+00:00",
    "summary": "",
    "points": 24,
    "comments": 2
  }
]
```
