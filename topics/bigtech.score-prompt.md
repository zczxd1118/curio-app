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
    "title": "Apple’s strategy for smart glasses is the same as smart watches",
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
    "id": "rss:https://www.theverge.com/entertainment/940449/feeble-little-horse-bitknot-music-album-review",
    "platform": "rss",
    "title": "Feeble Little Horse leans into digital weirdness on bitknot",
    "url": "https://www.theverge.com/entertainment/940449/feeble-little-horse-bitknot-music-album-review",
    "source": "Terrence O’Brien",
    "published_at": "2026-05-31T16:00:00+00:00",
    "summary": "From the opening moments of bitknot, it's obvious that Feeble Little Horse has found an entirely new gear. Where on Girl with Fish the blown-out textures were more '90s indie rock and shoegaze, on their latest LP, there's a more modern edge to the distortion and the riffs cut cleaner. Similarly, whe",
    "feed": "The Verge"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/940486/united-flight-236-bluetooth-speaker-name-bomb",
    "platform": "rss",
    "title": "United flight forced to turn around because of a Bluetooth speaker name",
    "url": "https://www.theverge.com/transportation/940486/united-flight-236-bluetooth-speaker-name-bomb",
    "source": "Terrence O’Brien",
    "published_at": "2026-05-31T15:50:02+00:00",
    "summary": "United flight 236 from Newark to Palma de Mallorca on Saturday night was forced to turn around just an hour after takeoff due to security concerns around a Bluetooth signal. Multiple Redditors claimed to be on the flight and reported that the crew repeatedly requested passengers to turn off their Bl",
    "feed": "The Verge"
  },
  {
    "id": "rss:https://www.theverge.com/tech/940221/asus-rog-strix-scar-18-elmb-gaming-laptop-motion-blur-handson-impressions",
    "platform": "rss",
    "title": "This extravagant gaming laptop could ruin other screens for you",
    "url": "https://www.theverge.com/tech/940221/asus-rog-strix-scar-18-elmb-gaming-laptop-motion-blur-handson-impressions",
    "source": "Antonio G. Di Benedetto",
    "published_at": "2026-05-31T15:00:00+00:00",
    "summary": "My eyes have seen the PC gaming promised land, and it's a beautifully bright world without a shred of blurriness. It's warm, it looks lovely, and it's impeccably sharp. Also, it's expensive as hell. I've dipped my toe in this world by testing a pre-production version of the upcoming Asus ROG Strix S",
    "feed": "The Verge"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/940126/007-first-light-ps5-pc-steam-deal-sale",
    "platform": "rss",
    "title": "007 First Light is already discounted for the PS5 and Steam",
    "url": "https://www.theverge.com/gadgets/940126/007-first-light-ps5-pc-steam-deal-sale",
    "source": "Cameron Faulkner",
    "published_at": "2026-05-31T14:00:00+00:00",
    "summary": "IO Interactive’s 007 First Light is here, and it’s just as stunning a James Bond mov — err, video game — as we hoped it would be. Pardon the confusion, the title’s engaging tutorial really feels like you’re watching a great Bond movie at times. Whether you’re a longtime Hitman fan who’s been eagerly",
    "feed": "The Verge"
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
    "id": "rss:https://techcrunch.com/2026/05/29/artificial-intelligence-definition-glossary-hallucinations-guide-to-common-ai-terms/",
    "platform": "rss",
    "title": "So you’ve heard these AI terms and nodded along; let’s fix that",
    "url": "https://techcrunch.com/2026/05/29/artificial-intelligence-definition-glossary-hallucinations-guide-to-common-ai-terms/",
    "source": "Natasha Lomas, Romain Dillet, Kyle Wiggers, Lucas Ropek",
    "published_at": "2026-05-29T18:49:19+00:00",
    "summary": "The rise of AI has brought an avalanche of new terms and slang. Here is a glossary with definitions of some of the most important words and phrases you might encounter.",
    "feed": "TechCrunch"
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
    "id": "rss:https://stratechery.com/2026/an-interview-with-ben-thompson-at-the-moffettnathanson-media-internet-communications-conference/",
    "platform": "rss",
    "title": "An Interview with Ben Thompson at the MoffettNathanson Media, Internet & Communications Conference",
    "url": "https://stratechery.com/2026/an-interview-with-ben-thompson-at-the-moffettnathanson-media-internet-communications-conference/",
    "source": "Ben Thompson",
    "published_at": "2026-05-14T10:00:00+00:00",
    "summary": "An interview with me about the implications of the compute shortage on Aggregation Theory, consumer AI, and more.",
    "feed": "Stratechery by Ben Thompson"
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
    "id": "rss:https://arstechnica.com/ai/2026/05/llms-believe-false-statements-even-after-explicit-warnings-that-theyre-false/",
    "platform": "rss",
    "title": "LLMs believe false statements even after explicit warnings that they're false",
    "url": "https://arstechnica.com/ai/2026/05/llms-believe-false-statements-even-after-explicit-warnings-that-theyre-false/",
    "source": "Kyle Orland",
    "published_at": "2026-05-28T21:29:43+00:00",
    "summary": "Fine-tuning tests show \"bias... toward confidently representing the claims as true.\"",
    "feed": "Ars Technica"
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
    "id": "rss:https://www.producthunt.com/products/openstatus-2",
    "platform": "rss",
    "title": "Openstatus MCP Health Checker",
    "url": "https://www.producthunt.com/products/openstatus-2",
    "source": "fmerian",
    "published_at": "2026-05-28T14:14:25+00:00",
    "summary": "Test MCP servers like a real AI client, not just a ping Discussion | Link",
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
    "id": "rss:https://www.producthunt.com/products/coffee-piano-harmony-lab",
    "platform": "rss",
    "title": "Coffee Piano",
    "url": "https://www.producthunt.com/products/coffee-piano-harmony-lab",
    "source": "Jaime",
    "published_at": "2026-05-28T21:45:11+00:00",
    "summary": "Browser music and piano studio with visual harmony tools Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/firecoach",
    "platform": "rss",
    "title": "Firecoach AI",
    "url": "https://www.producthunt.com/products/firecoach",
    "source": "KP",
    "published_at": "2026-05-25T08:13:13+00:00",
    "summary": "AI roleplays that turn reps into top performers Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/artisan-3",
    "platform": "rss",
    "title": "Ava 2.0",
    "url": "https://www.producthunt.com/products/artisan-3",
    "source": "Rohan Chaubey",
    "published_at": "2026-05-27T22:10:18+00:00",
    "summary": "Your AI BDR that runs outbound sales autonomously Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/linear",
    "platform": "rss",
    "title": "Linear Diffs",
    "url": "https://www.producthunt.com/products/linear",
    "source": "fmerian",
    "published_at": "2026-05-28T18:09:28+00:00",
    "summary": "A new way to review PRs, directly inside Linear Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/integuru",
    "platform": "rss",
    "title": "Integuru",
    "url": "https://www.producthunt.com/products/integuru",
    "source": "Garry Tan",
    "published_at": "2026-05-28T13:41:04+00:00",
    "summary": "Generate fast, reliable APIs for any platform. No browsers Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/clipline-2",
    "platform": "rss",
    "title": "Clipline",
    "url": "https://www.producthunt.com/products/clipline-2",
    "source": "серж",
    "published_at": "2026-05-28T14:56:30+00:00",
    "summary": "AI Video Cutter for viral Shorts, Reels, TikTok in Telegram Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/promptlayer-2",
    "platform": "rss",
    "title": "PromptLayer",
    "url": "https://www.producthunt.com/products/promptlayer-2",
    "source": "Sam Benson",
    "published_at": "2026-05-29T06:41:50+00:00",
    "summary": "Trace AI requests, workflows, and costs in one timeline Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/gps-2",
    "platform": "rss",
    "title": "GPS",
    "url": "https://www.producthunt.com/products/gps-2",
    "source": "Hardik Singh",
    "published_at": "2026-05-28T15:05:48+00:00",
    "summary": "Memory layer for LLMs that stores repo rules + past lessons Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/screen-ruler",
    "platform": "rss",
    "title": "Screen Ruler",
    "url": "https://www.producthunt.com/products/screen-ruler",
    "source": "Myster Violets",
    "published_at": "2026-05-23T08:30:35+00:00",
    "summary": "The go-to ruler for designers and developers Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/basedash",
    "platform": "rss",
    "title": "Basedash: Embedded Analytics",
    "url": "https://www.producthunt.com/products/basedash",
    "source": "Max Musing",
    "published_at": "2026-05-28T18:57:07+00:00",
    "summary": "Give customers AI analytics inside your product. Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/rabbittravel",
    "platform": "rss",
    "title": "RabbitTravel",
    "url": "https://www.producthunt.com/products/rabbittravel",
    "source": "Tuan Anh",
    "published_at": "2026-05-28T10:34:41+00:00",
    "summary": "Smart travel planning made effortless Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/drafted-4",
    "platform": "rss",
    "title": "Drafted",
    "url": "https://www.producthunt.com/products/drafted-4",
    "source": "Garry Tan",
    "published_at": "2026-05-29T05:25:33+00:00",
    "summary": "Design a home instantly with AI Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/modev",
    "platform": "rss",
    "title": "MoDev",
    "url": "https://www.producthunt.com/products/modev",
    "source": "Juan Rivera Jr",
    "published_at": "2026-05-13T19:05:26+00:00",
    "summary": "The AI dev environment built for your phone. Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/hyper-11",
    "platform": "rss",
    "title": "Hyper: Self-driving Company Brain",
    "url": "https://www.producthunt.com/products/hyper-11",
    "source": "Garry Tan",
    "published_at": "2026-05-27T20:25:45+00:00",
    "summary": "Turn your AI agents from interns to veterans Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/extract-by-firecrawl",
    "platform": "rss",
    "title": "/monitor by Firecrawl",
    "url": "https://www.producthunt.com/products/extract-by-firecrawl",
    "source": "Eric Ciarla",
    "published_at": "2026-05-28T22:56:59+00:00",
    "summary": "Notify your AI agent when the web changes Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/tracknotch",
    "platform": "rss",
    "title": "TrackNotch",
    "url": "https://www.producthunt.com/products/tracknotch",
    "source": "Manoj Achari",
    "published_at": "2026-05-28T14:59:17+00:00",
    "summary": "LLM usage tracking that lives in your Mac's notch Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/sinalytica",
    "platform": "rss",
    "title": "Sinalytica",
    "url": "https://www.producthunt.com/products/sinalytica",
    "source": "Sina Rajaeeian",
    "published_at": "2026-05-23T20:37:22+00:00",
    "summary": "Travel back to 1998 and use Lovable on Windows 98 Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/mcp-bridge-by-appfactor",
    "platform": "rss",
    "title": "MCP Bridge by Appfactor",
    "url": "https://www.producthunt.com/products/mcp-bridge-by-appfactor",
    "source": "fmerian",
    "published_at": "2026-04-01T19:46:27+00:00",
    "summary": "Connect any API to any AI agent Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
  },
  {
    "id": "rss:https://www.producthunt.com/products/notchy",
    "platform": "rss",
    "title": "Notchy",
    "url": "https://www.producthunt.com/products/notchy",
    "source": "Vishva Variya",
    "published_at": "2026-05-28T10:38:55+00:00",
    "summary": "Mac dynamic island with music, timers, clipboard, file drops Discussion | Link",
    "feed": "Product Hunt — The best new products, every day"
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
    "id": "rss:https://36kr.com/p/3825786926633607?f=rss",
    "platform": "rss",
    "title": "“世纪合并”落空，雅诗兰黛松了一口气",
    "url": "https://36kr.com/p/3825786926633607?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T01:50:58+00:00",
    "summary": "化妆品公司全球市值第四和第九的合并交易落空。 5月21日，美国高端美妆巨头雅诗兰黛与西班牙香水美容集团Puig联合宣布，双方已正式终止就潜在合并事宜展开的谈判，协议未能达成。雅诗兰黛盘后股价随即跳涨逾10%，至86.9美元；Puig股价则在马德里市场重挫逾14%。 交易告吹的导火索，外界说法不一。路透社援引两名知情人士称，Puig旗下英国彩妆品牌Charlotte Tilbury的同名创始人在谈判过程中提出了一系列涉及自身持股回购条款的诉求，在财务上大幅抬高了交易推进的复杂程度。据悉，Charlotte Tilbury目前仍持有品牌约21.5%的股份，Puig预计将在2026至2031年间通过",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/p/3833859545343618?f=rss",
    "platform": "rss",
    "title": "8点1氪丨停服三年后，天涯社区正式恢复访问；广东辟谣高考将用AI改卷；MiniMax拟科创板上市",
    "url": "https://36kr.com/p/3833859545343618?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T00:05:59+00:00",
    "summary": "今日热点导览 OpenAI称使用AI攻克“80岁”数学难题 亚马逊：关停词元跟踪榜单 马斯克辟谣SpaceX估值下调 三花智控高管“为孩子教育”减持套现超4.3亿 哈根达斯中国被曝将被柠季收购 TOP 3大新闻 天涯社区正式恢复访问 6月1日起，天涯社区正式恢复访问。据“天涯社区”官方微博发布的《关于天涯社区恢复访问进展的情况说明》，自2023年4月1日起，天涯社区因电信IDC欠费而暂停访问。为了确保涉及上亿用户的天涯数据完整存续以及天涯社区的恢复访问，三年来，天涯社区重启团队持续不懈地展开自救。今年2月份，在新天涯联合工作组的支持下，确立了推进2026年6月1日前恢复天涯社区访问的方案。此外",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/p/3831348302358408?f=rss",
    "platform": "rss",
    "title": "当美妆品牌走进运动场：欧莱雅把校园公益做成了一场“运动实验”｜最前线",
    "url": "https://36kr.com/p/3831348302358408?f=rss",
    "source": "36氪",
    "published_at": "2026-05-30T05:33:05+00:00",
    "summary": "5月29日，欧莱雅中国在复旦大学启动2026年度“有意思青年”高校公益计划，并首次以校园运动会形式开启新一年的项目活动。活动现场，乒乓球运动员马龙、篮球运动员杨力维、足球运动员赵丽娜等体育界人士与高校学生展开互动，欧莱雅同时宣布向中国青少年发展基金会捐赠总价值约468万元的产品，并启动新一年度校园义卖活动。 从表面来看，这是一场校园公益活动；但放在全球美妆行业的发展背景下，它更像是美妆品牌持续拥抱运动文化和健康生活方式的一次缩影。 过去很长一段时间，美妆与运动被视为两个相对独立的消费领域。前者围绕审美表达展开，后者则强调竞技和功能价值。然而近年来，随着健康消费崛起、女性运动参与率提升以及生活方",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/p/3831135917107075?f=rss",
    "platform": "rss",
    "title": "36氪首发 | 服务富士康，半年营收超两千万的机器人解决方案商完成天使轮融资",
    "url": "https://36kr.com/p/3831135917107075?f=rss",
    "source": "36氪",
    "published_at": "2026-05-30T01:53:46+00:00",
    "summary": "作者&nbsp;|&nbsp;乔钰杰 编辑&nbsp;|&nbsp;袁斯来 硬氪获悉，乘物机器人（深圳）有限公司（以下简称“乘物机器人”）近日完成天使轮融资，由中国台湾工业自动化与智能机器人解决方案领域龙头企业和椿科技战略投资，华君资本担任独家财务顾问。 乘物机器人成立于2025年，总部位于深圳，专注工业具身智能技术研发与产品解决方案，具备从软硬件研发、数据采集、模型训练、场景部署与维护的一体化技术能力。 创始人黄金龙技术出身，拥有十余年机器人全栈研发与产业化经验，主导过多类工业机器人产品研发与落地；联合创始人单玉虎博士，曾先后在腾讯、小鹏、美团等企业负责机器人核心技术研发，深耕多模态大模型、",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/p/3831073348855433?f=rss",
    "platform": "rss",
    "title": "9点1氪｜泡泡玛特大涨，段永平日赚10亿；诺基亚发布首款微聊手机，售价199元；滴滴回应“乘客车内排泄”",
    "url": "https://36kr.com/p/3831073348855433?f=rss",
    "source": "36氪",
    "published_at": "2026-05-30T00:52:20+00:00",
    "summary": "今日热点导览 黄仁勋披露“赶飞机”细节，特朗普要出发时来电话 国内航线燃油附加费6月5日起首次下调 铁路将实施新规：违规乘车拒不补票将被限制购票 iPhone 17系列中国销量破3000万台，Pro Max版占近一半 SpaceX据悉将IPO估值目标下调至至少1.8万亿美元 TOP3大新闻 泡泡玛特上涨，段永平单日盈利近10亿港币 泡泡玛特迎来强势上涨，5月29日盘中最大涨幅超12%，截至29日记者发稿报收176港元，涨幅达8.98%。此番行情走高，与知名投资人段永平大举布局相关。据港交所5月27日披露的信息显示，知名投资人段永平举牌泡泡玛特，当时的持仓市值超117亿港元。伴随29日股价上扬，",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/p/3831071878358659?f=rss",
    "platform": "rss",
    "title": "最前线｜中科创星第十二期“好望角科学沙龙”聚焦“太空智驾”，卫星将从被动响应走向自主决策",
    "url": "https://36kr.com/p/3831071878358659?f=rss",
    "source": "36氪",
    "published_at": "2026-05-30T00:48:34+00:00",
    "summary": "“太空智驾时代将到来，卫星和星座会如同L4级自动驾驶汽车一样，在太空具备自主环境感知、任务规划和机动决策能力。” 5月28日，在上海举行的“好望角科学沙龙”上，中国科学院西安光学精密机械研究所（简称“西安光机所”）副所长邵晓鹏在演讲中提出了这一判断。 西安光机所副所长邵晓鹏在沙龙上演讲 “好望角科学沙龙”是由中科创星发起，中科创星、东壁科技数据、上海市研发公共服务平台管理中心、曲率引擎共同主办的科创融合与跨界交流平台。本期沙龙以“星际智控——太空智驾与遥感技术的产业共振”为主题，汇聚了航天领域专家，以及来自科创企业、投资机构与地方政府的近百位代表，共同探讨卫星和星座从被动响应向自主决策升级的技",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/p/3830580716365449?f=rss",
    "platform": "rss",
    "title": "千里科技再添筹码，或将整合吉利辅助驾驶团队｜36氪独家",
    "url": "https://36kr.com/p/3830580716365449?f=rss",
    "source": "36氪",
    "published_at": "2026-05-29T16:28:31+00:00",
    "summary": "为助力千里科技成为“第二个华为”，吉利决定为它增添新的技术筹码。 36氪从多位产业人士处了解到，吉利中央研究院数百人的辅助驾驶团队，将在近期被整合入千里科技。目前，吉利研究院辅助驾驶团队，已有人收到了转移合同的通知。 有接近吉利的知情人士告诉36氪：“这轮整合后，吉利研究院辅助驾驶团队，被平移至千里智驾与极氪的合资公司千里浩瀚，千里浩瀚今后主要负责为吉利的车型提供定制化开发和量产交付。千里智驾可以将更多精力转移至主线研发，提供平台级能力。吉利暂定了这样一个整合方案。”针对以上信息，36氪向吉利求证，截止发稿，��有回应。 据公开信息显示，千里智驾是千里科技负责辅助驾驶研发的子公司，千里科技通过",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/p/3830545234552452?f=rss",
    "platform": "rss",
    "title": "连续15年披露ESG报告，自然堂开始把“可持续”做成一门生意｜最前线",
    "url": "https://36kr.com/p/3830545234552452?f=rss",
    "source": "36氪",
    "published_at": "2026-05-29T16:02:16+00:00",
    "summary": "在中国美妆行业增长放缓、价格竞争加剧的背景下，越来越多品牌开始重新审视“可持续发展”这件事的商业意义。 5月26日，自然堂集团发布《2025年度可持续发展报告》，这是其连续第15年披露ESG相关内容。相比早期以公益、环保为主的企业社会责任叙事，今年的报告更强调“可量化”与“产业化”：包括首次按照科学碳目标倡议（SBTi）标准制定减碳路径、扩大范围三碳排放披露边界，以及将生物多样性、绿色原料、智能制造与供应链效率直接绑定。 对于当前的中国美妆行业而言，这种变化并不只是“做ESG”，更像是在寻找下一阶段竞争力。 过去几年，ESG更多是国际消费品公司的标准动作。包括L'Oréal、Estée Lau",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834096288917382?f=rss",
    "platform": "rss",
    "title": "蔚来：2026年5月共交付37705辆汽车，同比增长62.3%",
    "url": "https://36kr.com/newsflashes/3834096288917382?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T04:04:26+00:00",
    "summary": "36氪获悉，蔚来公告，2026年5月共交付37705辆汽车，同比增长62.3%。今年前五个月，蔚来公司共交付新车150,526台，同比增长68.7%。截至目前，蔚来公司已累计交付新车1,148,118台。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834093903242880?f=rss",
    "platform": "rss",
    "title": "易方达财富构建全市场基金筛选体系，买方投顾策略去年平均回报超11%",
    "url": "https://36kr.com/newsflashes/3834093903242880?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T04:02:00+00:00",
    "summary": "易方达财富已建立起一套覆盖全市场的基金筛选与投研体系。该体系以资产、基金、策略“三位一体”为核心，通过定量与定性相结合的分析方法，对近100家基金公司及其产品进行“分类、比较、跟踪”的动态维护，从全市场客观优选基金配置，践行买方立场。据第三方机构晨星的评价结果，易方达投顾策略组合在2025年均实现正收益。成立满6个月的实盘策略组合超过160个，平均回报为11.29%，平均夏普比率达到2.57，其中九成策略组合跑赢业绩基准，平均超额收益为1.32%。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834093699327624?f=rss",
    "platform": "rss",
    "title": "恒指午间休盘涨0.87%，恒生科技指数涨1.8%",
    "url": "https://36kr.com/newsflashes/3834093699327624?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T04:01:48+00:00",
    "summary": "36氪获悉，恒指午间休盘涨0.87%，恒生科技指数涨1.8%；煤炭、耐用消费品、传媒板块领涨，中煤能源涨超7%，铜师傅、阅文集团涨超6%；半导体、医药生物、建材板块走弱，天数智芯跌超11%，来凯医药跌超8%，中国建材跌超4%；南向资金净买入61.86亿港元。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834084353828743?f=rss",
    "platform": "rss",
    "title": "英伟达推出NVIDIA DSX平台",
    "url": "https://36kr.com/newsflashes/3834084353828743?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T03:52:17+00:00",
    "summary": "英伟达当地时间5月31日宣布推出NVIDIA DSX平台，为基础设施构建者提供创建AI工厂的完整行动指南。英伟达CEO黄仁勋表示：“借助DSX平台，你可以在不花一分钱的情况下对整个工厂进行模拟，在安装一个机架之前验证性能，并以生产级AI所需的可靠性运营。”（界面）",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834080621848451?f=rss",
    "platform": "rss",
    "title": "英伟达CEO黄仁勋：从产业的角度来看，Token就是资产、已经成为获利的营收单位",
    "url": "https://36kr.com/newsflashes/3834080621848451?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T03:48:29+00:00",
    "summary": "英伟达CEO黄仁勋6月1日在Gtc Taipei 2026大会上表示，从产业的角度来看，Token就是资产，Token已经成为获利的营收单位。因为它可以制造利润。AI公司会想要建造更多Token，生成更多Token，生产更多的AI工厂，这也是为什么台湾的运算需求已经火箭式飙升。（财联社）",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834069899192192?f=rss",
    "platform": "rss",
    "title": "宁德时代等入股赛力斯旗下赛豆科技公司",
    "url": "https://36kr.com/newsflashes/3834069899192192?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T03:45:30+00:00",
    "summary": "36氪获悉，天眼查App显示，近日，重庆蓝电科技有限公司发生工商变更，企业名称变更为重庆赛豆科技有限公司，新增宁德时代旗下宁波梅山保税港区问鼎投资有限公司、星宇股份等为股东，同时，注册资本由3.2亿人民币增至9.71亿人民币，增幅约203%。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834074636805769?f=rss",
    "platform": "rss",
    "title": "新易盛：预计二季度至四季度公司产能将处于持续扩产阶段",
    "url": "https://36kr.com/newsflashes/3834074636805769?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T03:42:24+00:00",
    "summary": "36氪获悉，新易盛在互动平台表示，预计今年二季度至四季度公司产能将处于持续扩产阶段，以满足日益增长的订单交付需求。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834068222371717?f=rss",
    "platform": "rss",
    "title": "海利得：尼龙气囊丝产品已有小批量供货",
    "url": "https://36kr.com/newsflashes/3834068222371717?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T03:35:53+00:00",
    "summary": "36氪获悉，海利得在互动平台表示，公司尼龙气囊丝产品已有小批量供货。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834064699532936?f=rss",
    "platform": "rss",
    "title": "A股三大指数午间休盘集体下跌，白酒股领跌",
    "url": "https://36kr.com/newsflashes/3834064699532936?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T03:32:18+00:00",
    "summary": "36氪获悉，A股三大指数午间休盘集体下跌，沪指跌0.12%，深成指跌0.6%，创业板指跌0.9%；能源、软件、文化传媒板块走强；赛微电子涨超8%，当虹科技涨超7%，天龙集团涨超5%；半导体、通信设备、白酒板块领跌，燕东微跌超9%，太辰光跌超6%，五粮液跌超2%。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834056145069701?f=rss",
    "platform": "rss",
    "title": "“博登智能”宣布完成数亿元A+轮及A++轮融资",
    "url": "https://36kr.com/newsflashes/3834056145069701?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T03:23:35+00:00",
    "summary": "近日，“博登智能”正式宣布完成数亿元A+轮及A++轮融资，鼎晖百孚、清新资本、鲁信创投、深产投等多家知名机构联合参投。作为面向Physical AI时代的真实世界AI基础设施公司，博登智能深度布局具身智能、大模型与自动驾驶三大核心方向，构建起“真实世界场景网络、全自动化数据引擎、现实世界验证体系”三层能力生态。本轮融资将进一步推动博登智能核心技术平台升级、全球真实世界训练网络建设及顶尖人才集聚，加速“Train at Scale, Validate in Reality”战略落地。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834054883665541?f=rss",
    "platform": "rss",
    "title": "宗馥莉名下娃哈哈广盛投资公司更名宏盛",
    "url": "https://36kr.com/newsflashes/3834054883665541?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T03:22:18+00:00",
    "summary": "36氪获悉，天眼查App显示，近日，杭州娃哈哈广盛投资有限公司发生工商变更，企业名称变更为杭州宏胜广盛投资有限公司。该公司成立于2001年6月，宗馥莉为法定代表人、执行董事、经理并全资持股该公司，注册资本8000万人民币，经营范围为实业投资。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834037865146249?f=rss",
    "platform": "rss",
    "title": "英特尔拟年底前推出新AI芯片，将使用更便宜内存与风冷技术",
    "url": "https://36kr.com/newsflashes/3834037865146249?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T03:05:00+00:00",
    "summary": "据报道，英特尔计划在今年年底前推出一款人工智能芯片，该芯片使用的内存和冷却技术比英伟达和AMD的同类产品更便宜。领导英特尔数据中心部门的Kevork Kechichian表示，该公司正“从基础入手”。其新款“Crescent Island”图形处理器旨在加速“推理”任务（即用户提出请求的阶段），而非模型训练——这是英伟达处理器占据主导地位的领域。（财联社）",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834024691066756?f=rss",
    "platform": "rss",
    "title": "创业板指跌逾1%",
    "url": "https://36kr.com/newsflashes/3834024691066756?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T02:51:36+00:00",
    "summary": "36氪获悉，创业板指跌逾1%，上证指数涨0.04%，深证成指跌0.58%。沪深京三市下跌个股超1400只。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834014212728456?f=rss",
    "platform": "rss",
    "title": "沪深两市成交额突破1.5万亿元",
    "url": "https://36kr.com/newsflashes/3834014212728456?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T02:40:56+00:00",
    "summary": "36氪获悉，沪深两市成交额突破1.5万亿元。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834001383384708?f=rss",
    "platform": "rss",
    "title": "“微光医疗”完成数亿元融资",
    "url": "https://36kr.com/newsflashes/3834001383384708?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T02:27:53+00:00",
    "summary": "36氪获悉，近日，“微光医疗”完成新一轮数亿元融资。本轮融资由中美绿色长三角和倚锋资本共同领投，中银资本、汇誉投资共同跟投。此次融资将重点用于公司核心产品的全球商业化布局，以及创新管线的研发、注册与临床推进，进一步夯实微光医疗在智能介入领域的战略布局。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3834000457049990?f=rss",
    "platform": "rss",
    "title": "恒生指数涨幅扩大至1%",
    "url": "https://36kr.com/newsflashes/3834000457049990?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T02:26:56+00:00",
    "summary": "36氪获悉，港股恒生指数涨幅扩大至1%，恒生科技指数现涨2.50%。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3833994033243779?f=rss",
    "platform": "rss",
    "title": "创业板指涨逾1%，上涨个股近4200只",
    "url": "https://36kr.com/newsflashes/3833994033243779?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T02:20:24+00:00",
    "summary": "36氪获悉，指数走强，创业板指拉升涨逾1.02%，沪指涨近0.6%，深成指涨近0.9%。AIPC、文化传媒、养殖业、煤炭、光伏等方向涨幅居前，沪深京三市上涨个股近4200只。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3833992947836550?f=rss",
    "platform": "rss",
    "title": "上海：实施优质企业培优、中小企业育强、小微企业成长的梯度激励政策，推动跨境电商、直播电商创新发展",
    "url": "https://36kr.com/newsflashes/3833992947836550?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T02:19:18+00:00",
    "summary": "36氪获悉，上海市人民政府办公厅印发《上海市服务业发展“十五五”规划》，其中提到，提高软件研发应用水平，实施优质企业培优、中小企业育强、小微企业成长的梯度激励政策。提高操作系统、数据库、工具软件等基础软件性能，强化计算机辅助设计、辅助分析、产品生命周期管理等工业软件供给能力，推进云化部署，鼓励布局研发智能助手、智能办公、智能娱乐等智能原生软件。壮大在线新经济规模，做强生活性互联网、社交电商、文化社区视频平台等优势业态。提升大宗商品交易、工业品电商、工业数字化转型服务平台能级。推动跨境电商、直播电商创新发展。",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3833984953296514?f=rss",
    "platform": "rss",
    "title": "科技记者古尔曼：苹果更轻薄的Vision Air头显预计2028年末或2029年发布",
    "url": "https://36kr.com/newsflashes/3833984953296514?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T02:11:10+00:00",
    "summary": "科技记者古尔曼称，苹果在研发一款更纤薄、轻便的头显，作为售价3499美元的初代Vision Pro的迭代产品。这款新品最早要到2028年末或2029年才会发布。（财联社）",
    "feed": "36氪"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3833984563226240?f=rss",
    "platform": "rss",
    "title": "上海：到2030年，服务业增加值达到6万亿元左右",
    "url": "https://36kr.com/newsflashes/3833984563226240?f=rss",
    "source": "36氪",
    "published_at": "2026-06-01T02:10:46+00:00",
    "summary": "36氪获悉，上海市人民政府办公厅印发《上海市服务业发展“十五五”规划》。其中提出，到2030年，服务业优结构、育动能、提质效取得明显成效，数智化、标准化、融合化、国际化水平持续提升，服务业增加值达到6万亿元左右，基本形成以高能级城市核心服务功能为引领，以高端化生产性服务业为主体，以高品质生活性服务业为支撑的优质高效服务业新体系，把上海服务业打造成能级更高的经济增长“韧性基座”，辐射更强的全球服务资源配置“活力枢纽”。",
    "feed": "36氪"
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
    "id": "rss:https://sspai.com/post/110425",
    "platform": "rss",
    "title": "派早报：Sony 发布 Bravia 2026 款电视产品等",
    "url": "https://sspai.com/post/110425",
    "source": "少数派编辑部",
    "published_at": "2026-05-29T00:51:34+00:00",
    "summary": "Anthropic 发布旗舰模型 Claude Opus 4.8，Intel 发布锐炫 G 系列处理器等。查看全文",
    "feed": "少数派"
  },
  {
    "id": "rss:https://sspai.com/prime/story/hair-dye-tutorial",
    "platform": "rss",
    "title": "从原理到实践：年轻人的第一篇染发及洗护指南",
    "url": "https://sspai.com/prime/story/hair-dye-tutorial",
    "source": "宛潼",
    "published_at": "2026-05-28T09:42:02+00:00",
    "summary": "我不用染发来对抗岁月，但我用它来对抗焦虑。[......]查看全文本文为会员文章，出自《单篇文章》，订阅后可阅读全文。",
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
    "id": "hn:47984675",
    "platform": "hackernews",
    "title": "Show HN: Filling PDF forms with AI using client-side tool calling",
    "url": "https://copilot.simplepdf.com/?share=a7d00ad073c75a75d493228e6ff7b11eb3f2d945b6175913e87898ec96ca8076&form=w9&lang=en",
    "source": "nip",
    "published_at": "2026-05-02T08:54:27+00:00",
    "summary": "",
    "points": 60,
    "comments": 29
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
    "comments": 547
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
