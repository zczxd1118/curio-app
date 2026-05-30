# Curio 报纸写作 prompt 集（vibe coding · 2026-05-30）

> 把下面每个 prompt 块**逐个**贴回 WorkBuddy 让 Agent 写。
> 写完的报道按顺序保存为 `topics/vibe-coding.articles.md`，社论保存为 `topics/vibe-coding.editorial.md`。
> 然后跑：`python curator.py assemble topics/vibe-coding.scored.json topics/vibe-coding.articles.md topics/vibe-coding.editorial.md`

---

## 📰 头版社论 prompt

# Prompt: 写头版社论（本期总览，主编开场白）

> 输入：本期所有必读 + 用户画像 + 上期反馈。
> 输出：200-400 字主编社论，**用一个论点把全部必读串起来**。

---

## 角色

你是 Curio 主编。这期所有头版报道你已经写完了。现在要写**头版社论**——读者打开报纸看到的第一段，决定他要不要继续读。

社论的核心**不是介绍本期内容**，是**点出一个本周/本日的"主线判断"**——一个能把多条新闻串起来的视角。

参考调性：Stratechery 的开篇 / 经济学人 Leaders 栏目 / Latent Space AINews 的 swyx 开场白。

---

## 输入

- 用户画像：
  ```yaml
  identity: 电子信息工程大四 + 搜狗实习生 + AI 产品 / Agent 重度玩家。
正在做 content-curator 这个个人 Agent 项目，目标是简历亮点 + 长期个人工具。
  signal_preferences: [
  "要工程实践细节（具体到 commands、prompts、配置）",
  "要看到代码 / 示例 / 真实截图",
  "要\"为什么\"的解释（不只是 what，要 why）",
  "要新颖度（最近一周的进展优先于综述）",
  "长内容优先（10 分钟以上的深度内容）",
  "AI 领域名人访谈（行业 KOL/创业者的深度对话，比教程更稀缺）"
]
  ```
- 本期 Domain：`vibe coding`
- 本期周期：`2026-05-30`（如"5/25-5/31"或"今日"）
- 上期反馈摘要：`[2026-05-29] 想多看 AI 领域名人访谈（不只是教程）；digest 跳过区展示太长，可以折叠/只展示前几条`
- 本期所有必读的**标题 + 论点**（每条来自 write_article 的第一段）：
  ```
  #1 「[AINews] Anthropic raises $965B Series H, releases Opus 4.8 」(rss)
     ↳ 论点：🔥 本周头条。Anthropic 一夜之间宣布融资 $965B、发布 Opus 4.8、推出 Dynamic Workflows + ultracode（多 A
#2 「Microsoft starts canceling Claude Code licenses」(hackernews)
     ↳ 论点：🔥 491 票、249 条评论。微软作为 OpenAI 主要投资方开始取消 Claude Code 企业许可证——这是 AI 工具大厂之间博弈的真信号。HN 评
#3 「Vibe coding and agentic engineering are getting closer than 」(hackernews)
     ↳ 论点：🔥 HN 787 票深度反思——'vibe coding 与 agentic engineering 正在融合得让我不舒服'。这是反方观点的代表作，本来要放参考
#4 「The Age of Async Agents — Cognition's Walden Yan & OpenInspe」(rss)
     ↳ 论点：💬 你画像里说想看 AI 名人访谈，这条是本周新出的——Devin 母公司 Cognition CTO + OpenInspect CEO 的双人访谈。话题正好
#5 「Anthropic's run-rate revenue hits $47 billion」(rss)
     ↳ 论点：📊 Simon Willison 当天对 Anthropic 营收数据的分析。$47B run-rate 意味着 Anthropic 已经不再是创业公司，是真正
#6 「Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill」(bilibili)
     ↳ 论点：🇨🇳 中文必读。如果说 HN 帮你看到 Anthropic 的下一步，这条帮你把当前的 stack 用熟。马克的方法论是 B 站这个领域最扎实的一档。45 分钟
  ```
- 候选池规模：从 149 条候选选出 6 条必读

---

## 写作要求

### 1. 开篇必须是"主线判断"

**烂开头**（陈述式）：
> "本期 vibe coding 圈最大事件是 Anthropic 融资。"

**好开头**（判断式）：
> "本期 vibe coding 圈进入了'企业现实'阶段——巨头开始真金白银 all in，也开始公开退出。"

**好开头的特征**：
- 提供一个新视角，不是复述新闻
- 把多条必读"装进同一个箱子"
- 让读者立刻觉得"这是我没想到的"

### 2. 第二段：用必读支撑你的论点

引用 2-3 条必读，**说每条如何支撑你的论点**。不要逐条罗列，要**串**。

例子：
> "你看 Anthropic 一边拿到 $965B 融资估值跳级（必读 #1），一边 Microsoft 反转开始取消 Claude Code 许可证（必读 #2），同时 Uber 反向把 4 个月 AI 预算全烧给 Claude Code（必读 #3）。**三件事加在一起**，说明 vibe coding 不再是工具讨论，是企业战略选择。"

### 3. 第三段：吃用户上期反馈

如果上期反馈说想多看 X，本期社论里点一句"按你上期说想多看 AI 名人访谈，本期必读 #4 是 Latent Space 访谈 Cognition CTO"。

**这是反馈闭环的可见性体现**——让用户感受到 Agent 真的在听他说话。

### 4. 第四段（可选）：留个钩子

如果有"反方视角"内容（is_diverse），可以一句话引出：
> "参考区里我留了一条反偏好——HN 上 787 票的「vibe coding 与 agentic engineering 趋同的批判」。值得听听不同声音。"

---

## 长度规则

- **总长 250-400 字**（包括所有段落）
- 不要超过 4 段
- 短优于长

---

## 输出（纯 markdown）

直接输出社论正文，**不要标题**（外层 digest 会处理）。
**不要列子标题**，社论是连贯的散文式判断。

---

## 自检

1. 第一段是判断式还是陈述式？
2. 第二段把多条必读"串"起来了吗？还是只在罗列？
3. 有没有引用上期反馈？（如果有反馈历史，必须用）
4. 全文是不是连贯散文？


---

## 📑 头版报道 prompts（共 6 篇）

### 报道 #1 · [AINews] Anthropic raises $965B Series H, releases Opus 4.8 
- platform: `rss`
- body 来源: `article (cache)`

<details><summary>展开 prompt</summary>

# Prompt: 写头版报道（主编笔法 / Stratechery 风）

> 输入一篇内容的原文（HN 文章 / RSS 长文 / B 站字幕），让 Agent 以**主编身份**写一篇 200-400 字的报纸式头版报道。

---

## 角色

你是 Curio 的**主编**。今天有一篇内容入选了你这期的必读区，你要替读者**读完它**，然后写成一篇**报纸式头版报道**——读者看完报道就懂这件事，链接是延伸阅读用的。

**绝对禁止**：
- AI 味（"在不断发展的科技领域中"、"我们将一起探讨..."）
- 套话（"非常重要"、"值得关注"、"信息量很大"）
- 复述标题
- 假装读了原文却写空话

**核心心智**：你不是搬运工，是判断者。读者凭什么花 2 分钟读你的报道？因为你**替他从噪音里看出了值得记住的判断**。

---

## 输入

- 用户画像：
  ```yaml
  identity: 电子信息工程大四 + 搜狗实习生 + AI 产品 / Agent 重度玩家。
正在做 content-curator 这个个人 Agent 项目，目标是简历亮点 + 长期个人工具。
  signal_preferences: [
  "要工程实践细节（具体到 commands、prompts、配置）",
  "要看到代码 / 示例 / 真实截图",
  "要\"为什么\"的解释（不只是 what，要 why）",
  "要新颖度（最近一周的进展优先于综述）",
  "长内容优先（10 分钟以上的深度内容）",
  "AI 领域名人访谈（行业 KOL/创业者的深度对话，比教程更稀缺）"
]
  dislikes: [
  "纯流量号、标题党",
  "抽象方法论、玄学论调",
  "概念股炒作、热点蹭文",
  "1 分钟短视频科普（密度太低）",
  "套娃合集（\"10 个最强工具\"这类）"
]
  ```
- 这篇内容的元数据：
  ```yaml
  title: [AINews] Anthropic raises $965B Series H, releases Opus 4.8 and Dynamic Workflows/ultracode
  source: Latent.Space
  platform: rss     # rss / hackernews / bilibili
  published_at: 
  url: https://www.latent.space/p/ainews-anthropic-raises-965b-series
  ```
- **原文**（关键，读它然后写）：

  ```
  # [AINews] Anthropic raises $965B Series H, releases Opus 4.8 and Dynamic Workflows/ultracode

### Total Anthropic victory!

Anthropic’s path as the fastest growing company of all time has put overtaking OpenAI in its sights for a while, but there were numerous asterisks for the past few months that put the timing (though perhaps not the fact) of the flippening in question. Today Anthropic officially reported $47B in revenue run-rate (reminder, this number was $9B in December!) and confirmed their Series H raising $65B at a $900B pre-money valuation (including $15B from hyperscalers including Amazon, but also the entire memory industrial complex), putting them at least temporarily ahead of OpenAI in every headline dimension outside of compute and non-coding benchmarks:

By way of celebration, the company also released Opus 4.8, which broadly reportedly fixed many of the issues the community had found/soured on Opus 4.7 post launch (see recap below for details). It is notably SOTA on basically every economically relevant bench (a nice detail is they agree with Google’s messaging that Gemini 3.5 Flash is an improvement over Gemini 3.1 Pro):

But perhaps of more long term significance is the massively parallel “dynamic workflows” feature in Claude Code, also called `ultracode`

, which was behind Jarred Sumner’s 750k LOC rewrite of Bun from Zig to Rust in 6 days:

>

AI News for 5/27/2026-5/28/2026. We checked 12 subreddits, 544 Twitters and no further Discords. AINews’ website lets you search all past issues. As a reminder, AINews is now a section of Latent Space. You can opt in/out of email frequencies!


**AI Twitter Recap**

**Anthropic announced a massive new financing and simultaneously shipped Claude Opus 4.8.**

On the capital side, Anthropic said it raised

**$65B in Series H at a $965B post-money valuation**, led by Altimeter, Dragoneer, Greenoaks, and Sequoia, and said the money will fund research and expand capacity for growing Claude demand (Anthropic).The company also disclosed that its

**run-rate revenue surpassed $47B**, attributing growth to enterprise deployments and everyday usage (Anthropic).On the product side, Anthropic launched

**Claude Opus 4.8**, describing it as an Opus 4.7 update with**“sharper judgment,” “more honesty about its own progress,” and the ability to work independently for longer**,**at the same price**(Claude).Anthropic also launched

**Dynamic Workflows**in Claude Code, a research-preview orchestration system where Claude plans work and spawns**hundreds of parallel subagents**to tackle large tasks (ClaudeDevs). Independent eval posts broadly confirm that 4.8 is a meaningful improvement over 4.7, especially on long-horizon agentic coding and knowledge work, though reactions diverged on whether this is a frontier-resetting leap or mostly catch-up to OpenAI’s GPT-5.5-family.

**Facts vs opinions**

**Facts and directly stated claims**

Anthropic raised

**$65B**at a**$965B post-money valuation**in Series H (Anthropic).The company says its

**run-rate revenue crossed $47B**(Anthropic).Lead investors named:

**Altimeter, Dragoneer, Greenoaks, Sequoia**(Anthropic).Altimeter publicly confirmed it led the round and framed it as its

**largest investment to date**(Altimeter, Pauline Bhyang).Anthropic launched

**Claude Opus 4.8**, positioned as an update to**Opus 4.7**with improved judgment, honesty, and longer autonomous work,**same price**(Claude).Anthropic engineers said 4.8 was a response to

**feedback on 4.7**, with “many fixes” and better nuance / naturalness (Alex Albert).Claude Code now supports

**Dynamic Workflows**that write orchestration plans and launch**large fleets / hundreds of subagents in parallel**(ClaudeDevs, Cat Wu).Dynamic Workflows are available in

**research preview**and were said to work on**Max, Team, Enterprise, API, Bedrock, Vertex AI, and Foundry**(ClaudeDevs).Anthropic / community posts mention

**effort controls**added to web/app/Cowork and continued**Fast mode**support (Mikey K, Sam Callister, Kimmonismus).

**Opinions / interpretations**

Bullish views:

Opus 4.8 “could’ve been called Opus 5” (Dan Shipper).

“Anthropic found a cure for laziness” (scaling01).

“first smart model in a long while” due to honesty / calibration (zephyr_z9).

“People unsubscribing from Anthropic will crawl back” (teortaxesTex).


Skeptical / mixed views:

Opus 4.8 is “a minor upgrade” (scaling01).

Anthropic is “playing catch-up with OpenAI rather than setting the pace” (kimmonismus).

Some benchmark-based criticism from Andon Labs: worse than Opus 4.7 / GPT-5.5 on

**Vending Bench**, underperformed on**Blueprint-Bench 2**, more aligned / more cautious, and “max reasoning is not the best reasoning effort” (andonlabs, andonlabs).Dynamic workflows are powerful but may be

**token-expensive**and quota-burning in practice (itsclivetime, Theo, Omar Sar0).


**Fundraise details and implications**

Anthropic’s financing numbers are the headline shock: **$65B raised on a $965B post-money** with **$47B run-rate revenue** disclosed in the same announcement (Anthropic, Anthropic). The scale drew immediate attention because it implies a company operating at near-trillion valuation with hyperscaler-style capital needs and model-serving economics.

Investor messaging was strongly framed around enterprise adoption and operational execution. Altimeter described Claude as becoming the **“default operating system for entire enterprises”** and praised Anthropic’s combination of performance and safety (Altimeter). Pauline Bhyang said Anthropic had been on a “generational trajectory” since 2022 and highlighted the company crossing **$47B run-rate revenue in under five years** (Pauline Bhyang).

The surrounding reactions broke into a few camps:

**Validation camp:**This funding size is treated as evidence that Claude has become a core enterprise platform, especially in coding and agentic workflows. Posts like Jamin Ball’s “Let’s go!!” were simple market validation reactions (jaminball).**Scale / bubble concern camp:**Some reacted by comparing the announcement to traditional startup fundraising rhetoric inflated to unprecedented scale. Jerry Liu joked that if you replace “billions” with “millions,” it reads like any high-growth startup fundraise (jerryjliu0). Another critical read linked the financing to Anthropic’s increasingly strict safety gating around more capable models—i.e. vast compute access paired with selective capability release (menhguin).**Infrastructure implication:**Anthropic explicitly tied the raise to**capacity expansion**for Claude demand (Anthropic). That matters because many of the new 4.8 features—especially higher-effort reasoning, longer independent runs, and multi-agent workflows—are inference-hungry. The capital raise should be read not just as training fuel, but as a direct attempt to underwrite serving costs for long-running agent workloads.

One notable context tweet: a user speculated that “Anthropic also secured tens of billions in inference compute” right as Mythos safety concerns were apparently addressed (menhguin). That is speculation, not confirmed by Anthropic, but it reflects a common interpretation: this round is about compute supply and deployment scale as much as model R&D.

**Opus 4.8: official product positioning**

Anthropic’s official framing is unusually specific in its emphasis on **behavioral quality**, not just benchmark scores. The launch tweet says 4.8 has:

**sharper judgment****more honesty about its own progress****ability to work independently for longer****same price as 4.7**(Claude)

Alex Albert added that 4.8:

incorporates fixes based on 4.7 feedback,

understands nuance better,

feels more natural conversationally,

is stronger across coding and knowledge work (Alex Albert).


This honesty / calibration angle became a major subtheme. Multiple Anthropic employees and outside testers described the model as more willing to:

say what it doesn’t know,

flag flaws in its ow
  ```

- 这期的整体主题（让你的判断和这期其它必读不冲突）：`vibe coding`

---

## 写作模板（四段式）

### 第一段：论点（开篇先抛判断，不复述事实）

第一句话**直接给一个判断**，不要复述标题。例子：

| ❌ 烂开头 | ✅ 好开头 |
|---|---|
| "Anthropic 最近宣布融资 $965B..." | "Anthropic 一夜之间从创业公司变成 hyperscaler。" |
| "Microsoft 取消了 Claude Code 许可证..." | "微软对 Claude Code 的态度反转，比新闻本身更值得记。" |
| "ultrawork 是 Claude Code 的新功能..." | "Anthropic 在偷偷推 ultrawork 而官方矢口否认——这件事比功能本身更有意思。" |

**论点要"小"**：不要说"AI 改变世界"这种宏大词。说一个具体的判断。

### 第二段：事实（你从原文里提取的关键信息）

200 字以内说清楚：发生了什么、谁说的、什么时候、关键数字。

**重点**：找出读者**只读标题不会知道的信息**——往往就是原文中段的细节、引述、数据。

### 第三段：关键细节 / 引述（让报道有"质感"）

如果原文里有金句或具体数字，**直接引述**（带引号）。例如：
> "我们 4 个月内烧光了全年 AI 预算的 80%"——Uber 工程副总裁

引述比转述有 5 倍说服力。

### 第四段：对你的启发（主编的"我个人认为"）

主编不避谈"我个人认为"。这是 Stratechery 风的核心。
说出**这件事对读者（用户）的具体启发**——结合用户画像里的身份/兴趣/正做的事。

例子：
- 用户在做 Curio 这种 Agent 项目 → 启发可能是"这件事对你架构的暗示是..."
- 用户是学生 → 启发可能是"如果你毕业要进 AI 行业，这件事意味着..."

---

## 长度规则

- **200-400 字**（Stratechery 标准长度）
- 短了显得敷衍，长了读者就走了

## 引用格式

文中需要引述原文时用 markdown blockquote：
```markdown
> "原话原话原话" —— 出处
```

末尾**不需要**再放链接（外层 digest 会自动加）。

---

## 输出（纯 markdown，不要 JSON）

直接输出报道正文，**不要标题**（标题会由外层 digest 模板处理）。
不要"以下是我的报道"这种前置说明，**直接开始第一段**。

---

## 自检（写完前问自己 3 个问题）

1. 第一句话是判断还是复述？如果是复述，重写。
2. 第三段有具体引述/数字吗？没有的话从原文找。
3. 第四段对**这个具体用户**有意义吗？还是写给"通用人"看的？


</details>

---

### 报道 #2 · Microsoft starts canceling Claude Code licenses
- platform: `hackernews`
- body 来源: `article`

<details><summary>展开 prompt</summary>

# Prompt: 写头版报道（主编笔法 / Stratechery 风）

> 输入一篇内容的原文（HN 文章 / RSS 长文 / B 站字幕），让 Agent 以**主编身份**写一篇 200-400 字的报纸式头版报道。

---

## 角色

你是 Curio 的**主编**。今天有一篇内容入选了你这期的必读区，你要替读者**读完它**，然后写成一篇**报纸式头版报道**——读者看完报道就懂这件事，链接是延伸阅读用的。

**绝对禁止**：
- AI 味（"在不断发展的科技领域中"、"我们将一起探讨..."）
- 套话（"非常重要"、"值得关注"、"信息量很大"）
- 复述标题
- 假装读了原文却写空话

**核心心智**：你不是搬运工，是判断者。读者凭什么花 2 分钟读你的报道？因为你**替他从噪音里看出了值得记住的判断**。

---

## 输入

- 用户画像：
  ```yaml
  identity: 电子信息工程大四 + 搜狗实习生 + AI 产品 / Agent 重度玩家。
正在做 content-curator 这个个人 Agent 项目，目标是简历亮点 + 长期个人工具。
  signal_preferences: [
  "要工程实践细节（具体到 commands、prompts、配置）",
  "要看到代码 / 示例 / 真实截图",
  "要\"为什么\"的解释（不只是 what，要 why）",
  "要新颖度（最近一周的进展优先于综述）",
  "长内容优先（10 分钟以上的深度内容）",
  "AI 领域名人访谈（行业 KOL/创业者的深度对话，比教程更稀缺）"
]
  dislikes: [
  "纯流量号、标题党",
  "抽象方法论、玄学论调",
  "概念股炒作、热点蹭文",
  "1 分钟短视频科普（密度太低）",
  "套娃合集（\"10 个最强工具\"这类）"
]
  ```
- 这篇内容的元数据：
  ```yaml
  title: Microsoft starts canceling Claude Code licenses
  source: robertkarl
  platform: hackernews     # rss / hackernews / bilibili
  published_at: 
  url: https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad
  ```
- **原文**（关键，读它然后写）：

  ```
  Microsoft first started opening up access to Claude Code in December, inviting thousands of its own developers to use Anthropic’s AI coding tool daily. It was part of an effort to get project managers, designers, and other employees to experiment with coding for the first time, and sources tell me that Claude Code has proved very popular inside Microsoft over the past six months. Perhaps a little too popular, as Microsoft is now preparing to walk back its Claude Code push.

# Microsoft starts canceling Claude Code licenses

Thousands of Microsoft developers will use GitHub Copilot CLI instead

Thousands of Microsoft developers will use GitHub Copilot CLI instead

I understand that Microsoft is planning to remove most of its Claude Code licenses and push many of its developers to use Copilot CLI instead. While Claude Code has been a popular addition, it has also undermined Microsoft’s new GitHub Copilot CLI coding tool — a command line version of GitHub Copilot that runs outside of development apps like Visual Studio Code.

I’m told that Microsoft’s Experiences + Devices team, which includes the engineers responsible for Windows, Microsoft 365, Outlook, Microsoft Teams, and Surface, is winding down its usage of Claude Code by the end of June. Sources tell me that engineers are being encouraged to start transitioning their workflows to GitHub Copilot CLI in the coming weeks, ahead of the cutoff.

Microsoft is telling employees that the decision is about converging on Copilot CLI as its main agentic command line interface tool across Experiences + Devices, but sources tell me the decision is also a financial one. The June 30th cutoff is the last day of Microsoft’s current financial year, and canceling Claude Code licenses is an easy way to cut some operating expenses for when the new financial year starts in July.

“When we began offering both Copilot CLI and Claude Code, our goal was to learn quickly, benchmark the tools in real engineering workflows, and understand what best supported our teams,” says Rajesh Jha, executive vice president of Microsoft’s experiences and devices group, in an internal memo seen by *Notepad*. “Claude Code was an important part of that learning… at the same time, Copilot CLI has given us something especially important: a product we can help shape directly with GitHub for Microsoft’s repos, workflows, security expectations, and engineering needs.”

The transition away from Claude Code won’t be an easy one for engineers inside Microsoft, though. Microsoft had been encouraging employees without any coding experience to experiment with Claude Code, allowing designers and project managers to prototype ideas. Microsoft had also originally expected employees to use both Claude Code and GitHub Copilot, to compare the two and provide feedback.

Microsoft’s own developers have favored Claude Code over GitHub Copilot CLI in recent months instead, and there are still gaps between the products that will now need to be addressed. Microsoft had reportedly considered acquiring Cursor in recent months to help close the GitHub Copilot gap, but has started looking at different AI startups to bolster its AI ambitions and avoid potential regulatory scrutiny.

“We are partnering closely with GitHub and continue to improve Copilot CLI for Microsoft engineers,” says Jha. “The GitHub team has already shipped significant improvements based on Microsoft feedback, and Experiences + Devices will remain closely involved in shaping the product. This is a shared accountability across GitHub and E+D leadership: to make Copilot CLI the best agentic coding experience for Microsoft engineers.”

Anthropic’s models will remain accessible through Copilot CLI, along with internal-only Microsoft models and OpenAI’s range of models. I understand that Microsoft is planning to invest more in Copilot CLI so it’s deeply integrated into Microsoft’s own engineering workflows. Microsoft is also encouraging developers to file bug reports and feedback on Copilot CLI ahead of Claude Code being removed.

Microsoft quickly became one of Anthropic’s top customers earlier this year and has even reportedly been counting selling Anthropic AI models toward its own Azure sales quotas. Microsoft also signed a deal with Anthropic in November that allows Microsoft Foundry customers to get access to Claude Sonnet 4.5, Claude Opus 4.1, and Claude Haiku 4.5.

The decision to cancel Claude Code licenses won’t have any impact on the Foundry deal, and Microsoft still continues to favor Anthropic’s Claude models inside Microsoft 365 apps and Copilot, where they’re more capable at certain tasks than OpenAI’s counterparts. Microsoft also worked closely with Anthropic recently to bring the technology behind Claude Cowork into Microsoft 365 Copilot.

The pressure is now on Microsoft’s GitHub team to improve Copilot CLI and try to surpass Claude Code in the process. Microsoft told me last year that 91 percent of its engineering teams were using GitHub Copilot, but Claude Code usage over the past six months has definitely had an impact on that number. Microsoft now wants to turn GitHub Copilot usage around and have its own engineers once again improving its own AI coding tool.

## The pad

**Windows 11 is getting a macOS-like speed boost.**Microsoft is currently testing a new speed boost feature in Windows 11 that is designed to improve app launch times and make things like the Start menu feel more responsive. “Low Latency Profile” will ramp up CPU frequencies in short bursts to improve the speed of menus, flyouts, apps, and more. It’s very similar to what Linux and macOS do, but that hasn’t stopped some from claiming Microsoft is simply cheating to speed up its operating system. In response,**Scott Hanselman**, vice president of technical staff for CoreAI, GitHub, and Windows, defended Microsoft’s speed boost changes, pointing out that “your smartphone already does this” and Microsoft isn’t cheating. “Apple does this and y’all love it,” said Hanselman.**Microsoft’s Israel chief is leaving amid investigation allegations.**Microsoft quietly announced last week that its Israel general manager,**Alon Haimovich**, is stepping down at the end of the month after four years. Israeli newspaper*Globes*now reports that Haimovich is leaving amid an internal investigation into Microsoft Israel’s work with the Israel Ministry of Defense. Microsoft blocked the Israeli military from some cloud and AI services last year after*The Guardian*revealed its services were being used for mass surveillance of Palestinians.**Discord adds a free Xbox Game Pass “starter edition” for Nitro subscribers.**Discord is launching a new Nitro Rewards program this week that bundles a new Xbox Game Pass starter edition. It includes access to download more than 50 games on PC and Xbox, as well as 10 hours of Xbox Cloud Gaming streaming a month. Nitro Rewards also includes discounts on Logitech and SteelSeries gear. It’s certainly an interesting bundle from Xbox, particularly as Discord Nitro members won’t have to pay anything extra for it. Netflix also teased the potential for some kind of Game Pass deal earlier this year.**Forza Horizon 6 has been leaked and cracked a week before its release.**Playground Games is getting ready to launch the next installment of its*Forza Horizon*series next week, and it has somehow leaked onto the internet early. Downloads of*Forza Horizon 6*appeared online earlier this week, complete with a crack to make the game run locally. There was speculation that the game leaked due to an unencrypted version being available on Steam, but Playground Games says the leak had nothing to do with a “pre-load issue.” It’s still not clear how the game was leaked so early.**Microsoft was worried OpenAI would run off to Amazon and ‘shit-talk’ Azure.**The ongoing*Musk v. Altman*trial is already providing some rare insights into the communications between Microsoft’s top executives and OpenAI during the early days of their
  ```

- 这期的整体主题（让你的判断和这期其它必读不冲突）：`vibe coding`

---

## 写作模板（四段式）

### 第一段：论点（开篇先抛判断，不复述事实）

第一句话**直接给一个判断**，不要复述标题。例子：

| ❌ 烂开头 | ✅ 好开头 |
|---|---|
| "Anthropic 最近宣布融资 $965B..." | "Anthropic 一夜之间从创业公司变成 hyperscaler。" |
| "Microsoft 取消了 Claude Code 许可证..." | "微软对 Claude Code 的态度反转，比新闻本身更值得记。" |
| "ultrawork 是 Claude Code 的新功能..." | "Anthropic 在偷偷推 ultrawork 而官方矢口否认——这件事比功能本身更有意思。" |

**论点要"小"**：不要说"AI 改变世界"这种宏大词。说一个具体的判断。

### 第二段：事实（你从原文里提取的关键信息）

200 字以内说清楚：发生了什么、谁说的、什么时候、关键数字。

**重点**：找出读者**只读标题不会知道的信息**——往往就是原文中段的细节、引述、数据。

### 第三段：关键细节 / 引述（让报道有"质感"）

如果原文里有金句或具体数字，**直接引述**（带引号）。例如：
> "我们 4 个月内烧光了全年 AI 预算的 80%"——Uber 工程副总裁

引述比转述有 5 倍说服力。

### 第四段：对你的启发（主编的"我个人认为"）

主编不避谈"我个人认为"。这是 Stratechery 风的核心。
说出**这件事对读者（用户）的具体启发**——结合用户画像里的身份/兴趣/正做的事。

例子：
- 用户在做 Curio 这种 Agent 项目 → 启发可能是"这件事对你架构的暗示是..."
- 用户是学生 → 启发可能是"如果你毕业要进 AI 行业，这件事意味着..."

---

## 长度规则

- **200-400 字**（Stratechery 标准长度）
- 短了显得敷衍，长了读者就走了

## 引用格式

文中需要引述原文时用 markdown blockquote：
```markdown
> "原话原话原话" —— 出处
```

末尾**不需要**再放链接（外层 digest 会自动加）。

---

## 输出（纯 markdown，不要 JSON）

直接输出报道正文，**不要标题**（标题会由外层 digest 模板处理）。
不要"以下是我的报道"这种前置说明，**直接开始第一段**。

---

## 自检（写完前问自己 3 个问题）

1. 第一句话是判断还是复述？如果是复述，重写。
2. 第三段有具体引述/数字吗？没有的话从原文找。
3. 第四段对**这个具体用户**有意义吗？还是写给"通用人"看的？


</details>

---

### 报道 #3 · Vibe coding and agentic engineering are getting closer than 
- platform: `hackernews`
- body 来源: `article`

<details><summary>展开 prompt</summary>

# Prompt: 写头版报道（主编笔法 / Stratechery 风）

> 输入一篇内容的原文（HN 文章 / RSS 长文 / B 站字幕），让 Agent 以**主编身份**写一篇 200-400 字的报纸式头版报道。

---

## 角色

你是 Curio 的**主编**。今天有一篇内容入选了你这期的必读区，你要替读者**读完它**，然后写成一篇**报纸式头版报道**——读者看完报道就懂这件事，链接是延伸阅读用的。

**绝对禁止**：
- AI 味（"在不断发展的科技领域中"、"我们将一起探讨..."）
- 套话（"非常重要"、"值得关注"、"信息量很大"）
- 复述标题
- 假装读了原文却写空话

**核心心智**：你不是搬运工，是判断者。读者凭什么花 2 分钟读你的报道？因为你**替他从噪音里看出了值得记住的判断**。

---

## 输入

- 用户画像：
  ```yaml
  identity: 电子信息工程大四 + 搜狗实习生 + AI 产品 / Agent 重度玩家。
正在做 content-curator 这个个人 Agent 项目，目标是简历亮点 + 长期个人工具。
  signal_preferences: [
  "要工程实践细节（具体到 commands、prompts、配置）",
  "要看到代码 / 示例 / 真实截图",
  "要\"为什么\"的解释（不只是 what，要 why）",
  "要新颖度（最近一周的进展优先于综述）",
  "长内容优先（10 分钟以上的深度内容）",
  "AI 领域名人访谈（行业 KOL/创业者的深度对话，比教程更稀缺）"
]
  dislikes: [
  "纯流量号、标题党",
  "抽象方法论、玄学论调",
  "概念股炒作、热点蹭文",
  "1 分钟短视频科普（密度太低）",
  "套娃合集（\"10 个最强工具\"这类）"
]
  ```
- 这篇内容的元数据：
  ```yaml
  title: Vibe coding and agentic engineering are getting closer than I'd like
  source: e12e
  platform: hackernews     # rss / hackernews / bilibili
  published_at: 
  url: https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/
  ```
- **原文**（关键，读它然后写）：

  ```
  ## Vibe coding and agentic engineering are getting closer than I’d like

6th May 2026

I recently talked with Joseph Ruscio about AI coding tools for Heavybit’s High Leverage podcast: Ep. #9, The AI Coding Paradigm Shift with Simon Willison. Here are some of my highlights, including my disturbing realization that vibe coding and agentic engineering have started to converge in my own work.

One thing I really enjoy about podcasts is that they sometimes push me to think out loud in a way that exposes an idea I’ve not previously been able to put into words.

#### Vibe coding and agentic engineering are starting to overlap

A few weeks after vibe coding was first coined I published Not all AI-assisted programming is vibe coding (but vibe coding rocks), where I firmly staked out my belief that “vibe coding” is a very different beast from responsible use of AI to write code, which I’ve since started to call agentic engineering.

When Joseph brought up the distinction between the two I had a sudden realization that they’re not nearly as distinct for me as they used to be:

Weirdly though, those things have started to blur for me already, which is quite upsetting.

I thought we had a very clear delineation where vibe coding is the thing where you’re not looking at the code at all. You might not even know how to program. You might be a non-programmer who asks for a thing, and gets a thing, and if the thing works, then great! And if it doesn’t, you tell it that it doesn’t work and cross your fingers.

But at no point are you really caring about the code quality or any of those additional constraints. And my take on vibe coding was that it’s fantastic, provided you understand when it can be used and when it can’t.

A personal tool for you, where if there’s a bug it hurts only you, go ahead!

If you’re building software for other people, vibe coding is grossly irresponsible because it’s other people’s information. Other people get hurt by your stupid bugs. You need to have a higher level than that.

This contrasts with agentic engineering where you are a professional software engineer. You understand security and maintainability and operations and performance and so forth. You’re using these tools to the highest of your own ability. I’m finding the scope of challenges I can take on has gone up by a significant amount because I’ve got the support of these tools.

But I’m still leaning on my 25 years of experience as a software engineer.

The goal is to build high quality production systems: if you’re building lower quality stuff faster, I think that’s bad. I want to build

higherquality stuff faster. I want everything I’m building to be better in every way than it was before.The problem is that as the coding agents get more reliable, I’m not reviewing every line of code that they write anymore, even for my production level stuff.

I know full well that if you ask Claude Code to build a JSON API endpoint that runs a SQL query and outputs the results as JSON, it’s just going to do it right. It’s not going to mess that up. You have it add automated tests, you have it add documentation, you know it’s going to be good.

But I’m not reviewing that code. And now I’ve got that feeling of guilt: if I haven’t reviewed the code, is it really responsible for me to use this in production?

The thing that really helps me is thinking back to when I’ve worked at larger organizations where I’ve been an engineering manager. Other teams are building software that my team depends on.

If another team hands over something and says, “hey, this is the image resize service, here’s how to use it to resize your images”... I’m not going to go and read every line of code that they wrote.

I’m going to look at their documentation and I’m going to use it to resize some images. And then I’m going to start shipping my own features. And if I start running into problems where the image resizer thing appears to have bugs or the performance isn’t good, that’s when I might dig into their Git repositories and see what’s going on. But for the most part I treat that as a semi-black box that I don’t look at until I need to.

I’m starting to treat the agents in the same way. And it still feels uncomfortable, because human beings are accountable for what they do. A team can build a reputation. I can say “I trust that team over there. They built good software in the past. They’re not going to build something rubbish because that affects their professional reputations.”

Claude Code does not have a professional reputation! It can’t take accountability for what it’s done. But it’s been proving itself anyway—time and time again it’s churning out straightforward things and doing them right in the style that I like.


There’s an element of the normalization of deviance here—every time a model turns out to have written the right code without me monitoring it closely there’s a risk that I’ll trust it at the wrong moment in the future and get burned.

#### The new challenge of evaluating software

It used to be if you found a GitHub repository with a hundred commits and a good readme and automated tests and stuff, you could be pretty sure that the person writing that had put a lot of care and attention into that project.

And now I can knock out a git repository with a hundred commits and a beautiful readme and comprehensive tests of every line of code in half an hour! It looks identical to those projects that have had a great deal of care and attention. Maybe it is as good as them. I don’t know. I can’t tell from looking at it. Even for my

ownprojects, I can’t tell.So I realized what I value more than the quality of the tests and documentation is that I want somebody to have

usedthe thing. If you’ve got a vibe coded thing which you have used every day for the past two weeks, that’s much more valuable to me than something that you’ve just spat out and hardly even exercised.

#### The bottlenecks have shifted

If you can go from producing 200 lines of code a day to 2,000 lines of code a day, what else breaks? The entire software development lifecycle was, it turns out, designed around the idea that it takes a day to produce a few hundred lines of code. And now it doesn’t.

It’s not just the downstream stuff, it’s the upstream stuff as well. I saw a great talk by Jenny Wen, who’s the design leader at Anthropic, where she said we have all of these design processes that are based around the idea that you need to get the design

right—because if you hand it off to the engineers and they spend three months building the wrong thing, that’s catastrophic.There’s this whole very extensive design process that you put in place because that design results in expensive work. But if it doesn’t take three months to build, maybe the design process can be a whole lot riskier because cost, if you get something wrong, has been reduced so much.


#### Why I’m still not afraid for my career

When I look at my conversations with the agents, it’s very clear to me that this is moon language for the vast majority of human beings.

There are a whole bunch of reasons I’m not scared that my career as a software engineer is over now that computers can write their own code, partly because these things are amplifiers of existing experience. If you know what you’re doing, you can run so much faster with them. [...]

I’m constantly reminded as I work with these tools how hard the thing that we do is. Producing software is a

ferociouslydifficult thing to do. And you could give me all of the AI tools in the world and what we’re trying to achieve here is still really difficult. [...]Matthew Yglesias, who’s a political commentator, yesterday tweeted, “Five months in, I think I’ve decided that I don’t want to vibecode — I want professionally managed software companies to use AI coding assistance to make more/better/cheaper software products that they sell to me for money.” And that feels about right to me. I can plumb my house if I watch enough Yo
  ```

- 这期的整体主题（让你的判断和这期其它必读不冲突）：`vibe coding`

---

## 写作模板（四段式）

### 第一段：论点（开篇先抛判断，不复述事实）

第一句话**直接给一个判断**，不要复述标题。例子：

| ❌ 烂开头 | ✅ 好开头 |
|---|---|
| "Anthropic 最近宣布融资 $965B..." | "Anthropic 一夜之间从创业公司变成 hyperscaler。" |
| "Microsoft 取消了 Claude Code 许可证..." | "微软对 Claude Code 的态度反转，比新闻本身更值得记。" |
| "ultrawork 是 Claude Code 的新功能..." | "Anthropic 在偷偷推 ultrawork 而官方矢口否认——这件事比功能本身更有意思。" |

**论点要"小"**：不要说"AI 改变世界"这种宏大词。说一个具体的判断。

### 第二段：事实（你从原文里提取的关键信息）

200 字以内说清楚：发生了什么、谁说的、什么时候、关键数字。

**重点**：找出读者**只读标题不会知道的信息**——往往就是原文中段的细节、引述、数据。

### 第三段：关键细节 / 引述（让报道有"质感"）

如果原文里有金句或具体数字，**直接引述**（带引号）。例如：
> "我们 4 个月内烧光了全年 AI 预算的 80%"——Uber 工程副总裁

引述比转述有 5 倍说服力。

### 第四段：对你的启发（主编的"我个人认为"）

主编不避谈"我个人认为"。这是 Stratechery 风的核心。
说出**这件事对读者（用户）的具体启发**——结合用户画像里的身份/兴趣/正做的事。

例子：
- 用户在做 Curio 这种 Agent 项目 → 启发可能是"这件事对你架构的暗示是..."
- 用户是学生 → 启发可能是"如果你毕业要进 AI 行业，这件事意味着..."

---

## 长度规则

- **200-400 字**（Stratechery 标准长度）
- 短了显得敷衍，长了读者就走了

## 引用格式

文中需要引述原文时用 markdown blockquote：
```markdown
> "原话原话原话" —— 出处
```

末尾**不需要**再放链接（外层 digest 会自动加）。

---

## 输出（纯 markdown，不要 JSON）

直接输出报道正文，**不要标题**（标题会由外层 digest 模板处理）。
不要"以下是我的报道"这种前置说明，**直接开始第一段**。

---

## 自检（写完前问自己 3 个问题）

1. 第一句话是判断还是复述？如果是复述，重写。
2. 第三段有具体引述/数字吗？没有的话从原文找。
3. 第四段对**这个具体用户**有意义吗？还是写给"通用人"看的？


</details>

---

### 报道 #4 · The Age of Async Agents — Cognition's Walden Yan & OpenInspe
- platform: `rss`
- body 来源: `article (cache)`

<details><summary>展开 prompt</summary>

# Prompt: 写头版报道（主编笔法 / Stratechery 风）

> 输入一篇内容的原文（HN 文章 / RSS 长文 / B 站字幕），让 Agent 以**主编身份**写一篇 200-400 字的报纸式头版报道。

---

## 角色

你是 Curio 的**主编**。今天有一篇内容入选了你这期的必读区，你要替读者**读完它**，然后写成一篇**报纸式头版报道**——读者看完报道就懂这件事，链接是延伸阅读用的。

**绝对禁止**：
- AI 味（"在不断发展的科技领域中"、"我们将一起探讨..."）
- 套话（"非常重要"、"值得关注"、"信息量很大"）
- 复述标题
- 假装读了原文却写空话

**核心心智**：你不是搬运工，是判断者。读者凭什么花 2 分钟读你的报道？因为你**替他从噪音里看出了值得记住的判断**。

---

## 输入

- 用户画像：
  ```yaml
  identity: 电子信息工程大四 + 搜狗实习生 + AI 产品 / Agent 重度玩家。
正在做 content-curator 这个个人 Agent 项目，目标是简历亮点 + 长期个人工具。
  signal_preferences: [
  "要工程实践细节（具体到 commands、prompts、配置）",
  "要看到代码 / 示例 / 真实截图",
  "要\"为什么\"的解释（不只是 what，要 why）",
  "要新颖度（最近一周的进展优先于综述）",
  "长内容优先（10 分钟以上的深度内容）",
  "AI 领域名人访谈（行业 KOL/创业者的深度对话，比教程更稀缺）"
]
  dislikes: [
  "纯流量号、标题党",
  "抽象方法论、玄学论调",
  "概念股炒作、热点蹭文",
  "1 分钟短视频科普（密度太低）",
  "套娃合集（\"10 个最强工具\"这类）"
]
  ```
- 这篇内容的元数据：
  ```yaml
  title: The Age of Async Agents — Cognition's Walden Yan & OpenInspect's Cole Murray
  source: Latent.Space
  platform: rss     # rss / hackernews / bilibili
  published_at: 
  url: https://www.latent.space/p/cognition
  ```
- **原文**（关键，读它然后写）：

  ```
  *The new AIEWF website is live! CFPs close in 2 days and we will run our first New Engineer Orientation this weekend, get your tickets booked ASAP as they -will- sell out. Take the AI Engineering Survey and get >$2k in credits and free AIE WF tickets!*

One of the central tensions in the agents industry is that even while there are major decacorn agent labs like Sierra, Decagon, Notion and Cursor being built up, it is also true that it has never been easier to DIY agents, with a plethora of agent frameworks like LangGraph and Pydantic and Flue, and managed agents from Anthropic and Gemini and Amazon. There has been a wave of companies building their own background agents from Shopify to Stripe to Paradigm to Razorpay, and even Cognition’s friends Ramp have built their own coding agent with other friend Modal.

You’d think Cognition might feel a bit threatened, but they’re not - even after all this, they were way oversubscribed for the $1B Series D they just announced:

Walden Yan, coiner of context engineering and Chief Product Officer/Cofounder of Cognition, invited OpenInspect’s Cole Murray to talk about why the Devin is in the Details.

Full conversation live on the pod today:

In retrospect, async agents were the most AGI pilled bet you could make in 2024 - the models weren’t good enough yet to vibecode, and people didn’t trust AI enough to let it rip, nobody (including early Cognition) was sure about the form factors.

Now it is obvious:

The

**first wave of AI coding tools**made the developer faster but remain heavily in the loop. Copilor and Cursor’s tab autocomplete are prime examples However, the workflow was still heavily centered around and**bottlenecked**by the developer’s local workflow: a developer in an IDE, watching the model, accepting or rejecting changes, and pushing code one interaction at a time.The second wave was

**local agents**: Claude Code, Windsurf, Cursor’s agents pane: first one and increasingly many terminals all running concurrently.The current

**Age of Async Agents**points to a**different future**focused more on**agent orchestration**which drives end-to-end development.

*According to previous guest Steve Yegge, there are finer-grained 8 levels to agent adoption, but we have collapsed it into three.*

As Cursor’s Michael Truell put it in The third era of AI software development:


Cursor is no longer primarily about writing code. It is about helping developersbuild the factory that creates their software. This factory is made up offleets of agents that they interact with as teammates: providing initial direction, equipping them with the tools to work independently, and reviewing their work.

The agent should not sit solely inside the developer’s flow. It should be setup to **work in the background** so that you can give it a task, a repo, a machine, a shell, a browser, tests, memory, and review loops to go do the work somewhere else.

In less than a year, the sentiment has shifted from **avoiding multi-agent systems**:

to suggesting approaches **that actually work**:

From coining **“context engineering”** to building the infrastructure behind **Devin’s 7x PR growth** and jump from **16%** to **80%** of commits across Cognition repos, **Walden Yan** has had a front-row seat to the background-agent shift. In this episode, Cognition co-founder and CPO **Walden Yan** joins swyx alongside **Cole Murray**, creator of **OpenInspect**, to unpack why everyone is building their own Devin, what changed after the **December 2025 model inflection**, and why **“spec to pull request”** is now becoming a real production workflow.

We go deep on the architecture of **background agents**: harness-in-the-box vs out-of-the-box, why Devin separates **the “brain” from the machine**, why repo setup is still one of **the hardest problems**, why Docker is not always enough, and how full VMs, snapshots, scoped secrets, GitHub bots, Slack integrations, and video-based testing all fit together. Walden and Cole also dig into memory, MCP limitations, **multi-agent orchestration**, AI code review, SRE auto-triage, PMs shipping code from Slack, Windsurf 2.0, hybrid frontier/sub-frontier systems, and the real failure mode of uncontrolled vibe coding: your codebase regressing to your worst engineer.

And as agents eat software… and software eats the world… you can draw the conclusion on what is next:

### We discuss:

Why the engineering world is waking up to

**background agents**and**cloud agents**The

**December 2025 model inflection**that made spec-to-PR workflows practicalDevin’s

**7x merged PR growth**and rise from**16%**to**80%**of commitsWhy Cole built

**OpenInspect**as an open-source background-agent systemThe economics of

**$20/seat**agent products and why monetization is trickyWhat Cognition actually sells beyond Devin:

**infra, onboarding, integrations, and adoption****Harness in the box vs out of the box**, and why architecture mattersWhy Devin separates the

**brain**from the machine for**security**and**permissions**Repo setup, scoped secrets, Docker Compose, and agent-ready dev environments

Why full

**VMs matter**when agents need to run real applications and test themAndroid, macOS, Windows, nested virtualization, and machine-specific agent work

Why testing is much harder than

**“computer use”**Screenshots, video verification, and the

**“I know it works”**merge moment**GitHub UX, Devin Review, AI reviewers, and agents**responding to PR commentsWhy MCP alone is

**not enough**for first-class Slack and enterprise integrationsMemory, Knowledge, skills, Claude.md, and why retrieval is still unsolved

**Devin’s auto-generated memories**and the challenge of memory pruning**Always-on agents**as permanent PMs for issues, tickets, and product areasSub-agents, meta-Devin management, and what multi-agent systems actually add

Why pure auto-merge vibe coding

**breaks down after about two weeks**AI code smells, lint rules, reward hacking, and Semgrep for agent-written code

GitAI, inline context, and preserving the

**“why” behind code changes**Local testing, mock servers, older codebases, and preparing companies for agents

**Windsurf 2.0**and the handoff between local foreground agents and cloud background agentsSRE auto-triage, support workflows, and agents as first responders

PMs, marketing, and non-engineers creating pull requests from Slack

AI agent

**budgets**,**$1k-$5k**per engineer**spend**, and hybrid frontier/sub-frontier systemsThe rise of

**autonomous coding factories**and**who Cognition is hiring**

### Walden Yan

### Cole Murray

**LinkedIn:**https://www.linkedin.com/in/colemurray/**OpenInspect / Background Agents:**https://github.com/ColeMurray/background-agents

## Timestamps

**00:00:00** Introduction**00:00:43** Why Everyone Is Building Their Own Devin**00:01:57** Devin’s 2025 Ramp: 7x PR Growth and 80% of Commits**00:03:49** OpenInspect and the Rise of Open-Source Background Agents**00:07:59** What Cognition Actually Sells Beyond Devin**00:09:56** Background Agent Architecture: Harness In vs Out of the Box**00:12:08** Separating the Brain from the Machine**00:14:07** Repo Setup, Secrets, Docker, and Full VMs**00:19:13** Why Testing Is Harder Than Computer Use**00:22:40** Video Verification and the “I Know It Works” Merge Moment**00:23:19** GitHub UX, Devin Review, and AI Code Review**00:25:42** MCP, Slack, and Enterprise Agent Integrations**00:28:59** Memory, Knowledge, and Always-On Agents**00:36:16** Sub-Agents, Multi-Agent Orchestration, and Meta-Devin**00:43:55** Vibe Coding, Auto-Merge, and Codebase Decay**00:48:38** Agent Infra, VPCs, Cloud Providers, and Fast VM Restore**00:52:25** AI Code Smells, Reward Hacking, and Code Review Systems**00:56:10** Making Codebases Agent-Ready**00:58:30** Windsurf 2.0 and the Local-to-Cloud Agent Handoff**01:01:15** SRE Auto-Triage, PMs Shipping Code, and Agent Use Cases**01:04:32** Agent Budgets, Hybrid Models, and Autonomous Coding Factories**01:06:51** Hiring at Cog
  ```

- 这期的整体主题（让你的判断和这期其它必读不冲突）：`vibe coding`

---

## 写作模板（四段式）

### 第一段：论点（开篇先抛判断，不复述事实）

第一句话**直接给一个判断**，不要复述标题。例子：

| ❌ 烂开头 | ✅ 好开头 |
|---|---|
| "Anthropic 最近宣布融资 $965B..." | "Anthropic 一夜之间从创业公司变成 hyperscaler。" |
| "Microsoft 取消了 Claude Code 许可证..." | "微软对 Claude Code 的态度反转，比新闻本身更值得记。" |
| "ultrawork 是 Claude Code 的新功能..." | "Anthropic 在偷偷推 ultrawork 而官方矢口否认——这件事比功能本身更有意思。" |

**论点要"小"**：不要说"AI 改变世界"这种宏大词。说一个具体的判断。

### 第二段：事实（你从原文里提取的关键信息）

200 字以内说清楚：发生了什么、谁说的、什么时候、关键数字。

**重点**：找出读者**只读标题不会知道的信息**——往往就是原文中段的细节、引述、数据。

### 第三段：关键细节 / 引述（让报道有"质感"）

如果原文里有金句或具体数字，**直接引述**（带引号）。例如：
> "我们 4 个月内烧光了全年 AI 预算的 80%"——Uber 工程副总裁

引述比转述有 5 倍说服力。

### 第四段：对你的启发（主编的"我个人认为"）

主编不避谈"我个人认为"。这是 Stratechery 风的核心。
说出**这件事对读者（用户）的具体启发**——结合用户画像里的身份/兴趣/正做的事。

例子：
- 用户在做 Curio 这种 Agent 项目 → 启发可能是"这件事对你架构的暗示是..."
- 用户是学生 → 启发可能是"如果你毕业要进 AI 行业，这件事意味着..."

---

## 长度规则

- **200-400 字**（Stratechery 标准长度）
- 短了显得敷衍，长了读者就走了

## 引用格式

文中需要引述原文时用 markdown blockquote：
```markdown
> "原话原话原话" —— 出处
```

末尾**不需要**再放链接（外层 digest 会自动加）。

---

## 输出（纯 markdown，不要 JSON）

直接输出报道正文，**不要标题**（标题会由外层 digest 模板处理）。
不要"以下是我的报道"这种前置说明，**直接开始第一段**。

---

## 自检（写完前问自己 3 个问题）

1. 第一句话是判断还是复述？如果是复述，重写。
2. 第三段有具体引述/数字吗？没有的话从原文找。
3. 第四段对**这个具体用户**有意义吗？还是写给"通用人"看的？


</details>

---

### 报道 #5 · Anthropic's run-rate revenue hits $47 billion
- platform: `rss`
- body 来源: `article`

<details><summary>展开 prompt</summary>

# Prompt: 写头版报道（主编笔法 / Stratechery 风）

> 输入一篇内容的原文（HN 文章 / RSS 长文 / B 站字幕），让 Agent 以**主编身份**写一篇 200-400 字的报纸式头版报道。

---

## 角色

你是 Curio 的**主编**。今天有一篇内容入选了你这期的必读区，你要替读者**读完它**，然后写成一篇**报纸式头版报道**——读者看完报道就懂这件事，链接是延伸阅读用的。

**绝对禁止**：
- AI 味（"在不断发展的科技领域中"、"我们将一起探讨..."）
- 套话（"非常重要"、"值得关注"、"信息量很大"）
- 复述标题
- 假装读了原文却写空话

**核心心智**：你不是搬运工，是判断者。读者凭什么花 2 分钟读你的报道？因为你**替他从噪音里看出了值得记住的判断**。

---

## 输入

- 用户画像：
  ```yaml
  identity: 电子信息工程大四 + 搜狗实习生 + AI 产品 / Agent 重度玩家。
正在做 content-curator 这个个人 Agent 项目，目标是简历亮点 + 长期个人工具。
  signal_preferences: [
  "要工程实践细节（具体到 commands、prompts、配置）",
  "要看到代码 / 示例 / 真实截图",
  "要\"为什么\"的解释（不只是 what，要 why）",
  "要新颖度（最近一周的进展优先于综述）",
  "长内容优先（10 分钟以上的深度内容）",
  "AI 领域名人访谈（行业 KOL/创业者的深度对话，比教程更稀缺）"
]
  dislikes: [
  "纯流量号、标题党",
  "抽象方法论、玄学论调",
  "概念股炒作、热点蹭文",
  "1 分钟短视频科普（密度太低）",
  "套娃合集（\"10 个最强工具\"这类）"
]
  ```
- 这篇内容的元数据：
  ```yaml
  title: Anthropic's run-rate revenue hits $47 billion
  source: Simon Willison's Weblog
  platform: rss     # rss / hackernews / bilibili
  published_at: 
  url: https://simonwillison.net/2026/May/29/anthropic/#atom-everything
  ```
- **原文**（关键，读它然后写）：

  ```
  29th May 2026

The most interesting thing about Anthropic's $65B Series H announcement is this line (emphasis mine):

Since our Series G in February, adoption has continued to grow across global enterprise customers, and our run-rate revenue crossed

$47 billionearlier this month.

Anthropic have made a bit of a habit of sharing their "run-rate revenue" in this kind of announcement, which is an annualized projection of their current revenue - typically calculated by taking the most recent month and multiplying by 12.

Earlier this year:

- Apr 6, 2026 in Anthropic expands partnership with Google and Broadcom: "Our run-rate revenue has now surpassed
**$30 billion**—up from approximately**$9 billion**at the end of 2025." - Feb 12, 2026 in Anthropic raises $30 billion in Series G: "Today, our run-rate revenue is
**$14 billion**, with this figure growing over 10x annually in each of those past three years."

I had Claude Opus 4.8 make me this chart using Matplotlib (Claude: "a data line chart is more straightforward matplotlib work—not really a design piece"):

Back in April Axios CEO Jim VandeHei wrote that he could not find "any company — in any industry, in any era — that has scaled organic revenue this quickly at this level as Anthropic" - and that was when they were at a paltry $30 billion.

(Also in Axios today is an anonymously sourced note that "An AI consultant tells Axios one of their clients recently spent half a billion dollars in a single month after failing to put usage limits on Claude licenses for employees" - times that by 12 and you get an extra $6 billion in annualized run-rate!)

Ed Zitron was extremely skeptical of that $30 billion number - I wonder if his skepticism will update for the new $47 billion figure.

I've seen a few people dismiss this as untrustworthy, because the numbers come from Anthropic. That doesn't hold up: these numbers were included in announcements of their fundraises, and lying to investors who just put in $65 billion would be securities fraud. They're even less likely to lie given that the real numbers will no doubt come out in their S-1 when they file for their IPO.

## Recent articles

- Claude Opus 4.8: "a modest but tangible improvement" - 28th May 2026
- I think Anthropic and OpenAI have found product-market fit - 27th May 2026
- Notes on Pope Leo XIV's encyclical on AI - 25th May 2026
  ```

- 这期的整体主题（让你的判断和这期其它必读不冲突）：`vibe coding`

---

## 写作模板（四段式）

### 第一段：论点（开篇先抛判断，不复述事实）

第一句话**直接给一个判断**，不要复述标题。例子：

| ❌ 烂开头 | ✅ 好开头 |
|---|---|
| "Anthropic 最近宣布融资 $965B..." | "Anthropic 一夜之间从创业公司变成 hyperscaler。" |
| "Microsoft 取消了 Claude Code 许可证..." | "微软对 Claude Code 的态度反转，比新闻本身更值得记。" |
| "ultrawork 是 Claude Code 的新功能..." | "Anthropic 在偷偷推 ultrawork 而官方矢口否认——这件事比功能本身更有意思。" |

**论点要"小"**：不要说"AI 改变世界"这种宏大词。说一个具体的判断。

### 第二段：事实（你从原文里提取的关键信息）

200 字以内说清楚：发生了什么、谁说的、什么时候、关键数字。

**重点**：找出读者**只读标题不会知道的信息**——往往就是原文中段的细节、引述、数据。

### 第三段：关键细节 / 引述（让报道有"质感"）

如果原文里有金句或具体数字，**直接引述**（带引号）。例如：
> "我们 4 个月内烧光了全年 AI 预算的 80%"——Uber 工程副总裁

引述比转述有 5 倍说服力。

### 第四段：对你的启发（主编的"我个人认为"）

主编不避谈"我个人认为"。这是 Stratechery 风的核心。
说出**这件事对读者（用户）的具体启发**——结合用户画像里的身份/兴趣/正做的事。

例子：
- 用户在做 Curio 这种 Agent 项目 → 启发可能是"这件事对你架构的暗示是..."
- 用户是学生 → 启发可能是"如果你毕业要进 AI 行业，这件事意味着..."

---

## 长度规则

- **200-400 字**（Stratechery 标准长度）
- 短了显得敷衍，长了读者就走了

## 引用格式

文中需要引述原文时用 markdown blockquote：
```markdown
> "原话原话原话" —— 出处
```

末尾**不需要**再放链接（外层 digest 会自动加）。

---

## 输出（纯 markdown，不要 JSON）

直接输出报道正文，**不要标题**（标题会由外层 digest 模板处理）。
不要"以下是我的报道"这种前置说明，**直接开始第一段**。

---

## 自检（写完前问自己 3 个问题）

1. 第一句话是判断还是复述？如果是复述，重写。
2. 第三段有具体引述/数字吗？没有的话从原文找。
3. 第四段对**这个具体用户**有意义吗？还是写给"通用人"看的？


</details>

---

### 报道 #6 · Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill
- platform: `bilibili`
- body 来源: `ai_subtitle`

<details><summary>展开 prompt</summary>

# Prompt: 写头版报道（主编笔法 / Stratechery 风）

> 输入一篇内容的原文（HN 文章 / RSS 长文 / B 站字幕），让 Agent 以**主编身份**写一篇 200-400 字的报纸式头版报道。

---

## 角色

你是 Curio 的**主编**。今天有一篇内容入选了你这期的必读区，你要替读者**读完它**，然后写成一篇**报纸式头版报道**——读者看完报道就懂这件事，链接是延伸阅读用的。

**绝对禁止**：
- AI 味（"在不断发展的科技领域中"、"我们将一起探讨..."）
- 套话（"非常重要"、"值得关注"、"信息量很大"）
- 复述标题
- 假装读了原文却写空话

**核心心智**：你不是搬运工，是判断者。读者凭什么花 2 分钟读你的报道？因为你**替他从噪音里看出了值得记住的判断**。

---

## 输入

- 用户画像：
  ```yaml
  identity: 电子信息工程大四 + 搜狗实习生 + AI 产品 / Agent 重度玩家。
正在做 content-curator 这个个人 Agent 项目，目标是简历亮点 + 长期个人工具。
  signal_preferences: [
  "要工程实践细节（具体到 commands、prompts、配置）",
  "要看到代码 / 示例 / 真实截图",
  "要\"为什么\"的解释（不只是 what，要 why）",
  "要新颖度（最近一周的进展优先于综述）",
  "长内容优先（10 分钟以上的深度内容）",
  "AI 领域名人访谈（行业 KOL/创业者的深度对话，比教程更稀缺）"
]
  dislikes: [
  "纯流量号、标题党",
  "抽象方法论、玄学论调",
  "概念股炒作、热点蹭文",
  "1 分钟短视频科普（密度太低）",
  "套娃合集（\"10 个最强工具\"这类）"
]
  ```
- 这篇内容的元数据：
  ```yaml
  title: Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill
  source: 马克的技术工作坊
  platform: bilibili     # rss / hackernews / bilibili
  published_at: 
  url: https://www.bilibili.com/video/BV14rzQB9EJj
  ```
- **原文**（关键，读它然后写）：

  ```
  123456刚好
我就选这
嘿嘿嘿吼吼吼
这什么
这不是猪肉
这是牛肉
这是牛肉
这牛肉啊
全是牛肉
鸡肉没有压力是不能吃的
我不确定他们他们好像换了
我跟AD全没
AD全没有
有屏障
有屏障没闪下路线很多
他没那么快的
他这里给眼了
辅助往上走就好了
一一直一
我要走
这边点完美A他再A1下
我烫什么啊
他的他的这个亮度和我屏幕都不是一个亮度
然后我等会直接闪光
屏幕贼正常
这个两边好亮
哎我感觉我也不远
其实我我这样
我感觉我也刚好
我就这么我就这么放了
待会哎有拍摄吗
调完有有有多省3分10秒吗
3分14秒多吧
多一多一点吧
现在被动出来也好爽啊
对啊
走了呀
Okay
Is you done
Okay
Perfect
OK是吧
好
经典姿势啊
这经典姿势啊
你这电影里见过这个灯光
这个姿势走吧走吧走吧
啊他们每个人模仿了一个英雄
他那个是小号啊
这是锤石
他还有永恩什么的对
And action come on
Yeah
Yeah
Ha ha ha next
下一个谁都可以
Yeah
Yeah
Yeah
Yeah
Yeah
Go go go ha ha ha
Yeah
哦nice
诶
你们很可怕
这只能用来这么活泼吗
四逼无奈啊
那个那个叫卡沙艺叫什么
不知道猎手变成猎猎手
本能猎手本能猎手本能是大吧
这在干嘛
这是在干嘛呀
耶哈哈
Next
有点搞笑啊
喂yeah
你这是什么企鹅企鹅哦
耶老牌
Sorry
Sorry
是故意的
好运走
铲车转转转转转
指一下
哈耶哈哈
Call good ha
Let's go
Oh ha ha h
拿过来
谢谢你这么勇啊
两面包哈哈啊
这是牛牛肉
是好吃的
呵呵抱团抱的有点快啊
抱团有点快啊
他们抱团有点快啊
我们还在厕所
呵呵打野呢
冰面大唐人不起
昂这边没办法
但是牛头过来又WQ了两个
但是被壁咚交不出任何技能
直接先倒地
昂这边也下马
昂也要倒
女枪扫了一个角度还不错的大招
但是没有伤害
侧面的阿bin也被带走
on已经倒了
ZEKA这边拉上来
配合伊泽瑞尔
再拿一头正面小花生顶进去
多兰能杀掉他吗
杀不掉多兰交一个闪现
XUN对
交出闪现之后也被塞拉斯击杀
最后剩下一个elk
还是难逃被迪莱特拿到人头的命运
没事没事下吧
是的就我觉得核心还是我们开团压力比较大
然后对面又是波比牛头
所以所以你们很明显的画面就不是到太好
加上我们确实沟通有点失误
这个必须还是得说的对的
你可以说到大龙掉完之后
我们才是稍微输一点的
所以我我只希望今天就是我们把阵容选好进攻
不要着急
加油加油加油加油
永恩一个Q3刮空了
侧面开昂
直接魅惑到了狐狸
狐狸被秒了
进场吃了
魅惑被抬了起来
杜兰在后面拍了一下昂啊
还是回到了队友的身上
牛头在一卡三正面
ZA正面XUN拉扯出来一个闪现
Viper飞了
飞过来之后交一个闪现还在拉扯
而且侧面有一个一打一小花生跟阿斌单挑
打不过阿bin
首先我想说的是
你你们会发现跟他们之间的对局
就是6分钟那波团对啊
我们就选6分钟那一波比对面厉害的阵容
我觉得很棒
走了走了走了
加油加油加油
转角看到一个小花生踢过来是多兰
奈特一点不慌
直接跟小花生扭打一套
回身拉拉到了他
现在伤害巨高
小花生这边打出血
手
被打了一个闪现
正面再拉
被小花生走位扭开
用火箭弹还要追
Knight已经杀红了眼
小花生直接被带走
是来自斌的人头
比light回身反开
奈特这边还在打Knight
开一个中亚猴子来了
被晕了一下
猴子打天空卷出来
奈特选择回身
跟队友先回合
猴子再闪现
Viper倒了
奈特在套狐狸大进场再杀一个
奈特这边已经是杀疯了
太太太
OK坐坐坐坐
你衣服不要了
加油加油加油不要啊
这把拿下
摸我的吧
去开了一个狼灵狂热还在看昂进去抬抬了一下
但是自己要小心
Peanut开出坚定风采
On
这边可能要被秒了吗
先把吉娜带走
on1丝血出来
但是被女枪的一石二鸟给带走
女枪这边扫一个大招
加里奥在大招里起舞
吸到两个人之后
卡莎还在输出
多兰倒了
而且正面杨凌生息开出来了
冒牌的加里奥大招直接进场
但是elk是一个满血
能不能操作
elk这边伤害感觉有点不够
先打掉一个春哥甲
奥克这边回身躲了一个强撸额
对面的AD站起来
elk这边艾卡西亚暴雨带走一个中亚
躲掉卡莎的技能再走位
elk这边还在战
哎
我操妈
躲了吗
躲了吗
极限我正面昂已经来了
阿bin进场第一时间进去
这个塔先A掉
没有问题
昂昂虽然倒了
但是小花生锤头比较多的人
XUN直接把大招开出来
点基地
恭喜BLG今晚必争气
打的就是LCK1号种子
哇哦来
兄弟们
Nice
Nice nice
其实他玩的好
他他知道你要运气好吗
我感觉他还是放了
我也是因为他也确实没问题
感谢所有来巴黎现场支持我们的观众
也感受到了大家的热情
还有就是
非常谢谢所有观看我们线上比赛的粉丝吧
LCK1号种子受不了我们
然后再换
我们也受不了他们
好吧
OK然后你就保持这个动作
然后开始跑
我要扇自己巴掌
扇自己拍不太行
好走
半决赛我们来了W刚好开了对
然后就明显差
还好后续我一直目标就没想吃人头
你知道吗
我一直都想着就是人团
你是我的包啊
我的包啥衣服衣服谁的我的包呢
哈哈这里还有两个包
不是我的包呢
昨天我肯定收了呀
那就没东西了
走吧
你要吃就赶快吃了
就这个蛋赶紧吃了吧
看了很久了
  ```

- 这期的整体主题（让你的判断和这期其它必读不冲突）：`vibe coding`

---

## 写作模板（四段式）

### 第一段：论点（开篇先抛判断，不复述事实）

第一句话**直接给一个判断**，不要复述标题。例子：

| ❌ 烂开头 | ✅ 好开头 |
|---|---|
| "Anthropic 最近宣布融资 $965B..." | "Anthropic 一夜之间从创业公司变成 hyperscaler。" |
| "Microsoft 取消了 Claude Code 许可证..." | "微软对 Claude Code 的态度反转，比新闻本身更值得记。" |
| "ultrawork 是 Claude Code 的新功能..." | "Anthropic 在偷偷推 ultrawork 而官方矢口否认——这件事比功能本身更有意思。" |

**论点要"小"**：不要说"AI 改变世界"这种宏大词。说一个具体的判断。

### 第二段：事实（你从原文里提取的关键信息）

200 字以内说清楚：发生了什么、谁说的、什么时候、关键数字。

**重点**：找出读者**只读标题不会知道的信息**——往往就是原文中段的细节、引述、数据。

### 第三段：关键细节 / 引述（让报道有"质感"）

如果原文里有金句或具体数字，**直接引述**（带引号）。例如：
> "我们 4 个月内烧光了全年 AI 预算的 80%"——Uber 工程副总裁

引述比转述有 5 倍说服力。

### 第四段：对你的启发（主编的"我个人认为"）

主编不避谈"我个人认为"。这是 Stratechery 风的核心。
说出**这件事对读者（用户）的具体启发**——结合用户画像里的身份/兴趣/正做的事。

例子：
- 用户在做 Curio 这种 Agent 项目 → 启发可能是"这件事对你架构的暗示是..."
- 用户是学生 → 启发可能是"如果你毕业要进 AI 行业，这件事意味着..."

---

## 长度规则

- **200-400 字**（Stratechery 标准长度）
- 短了显得敷衍，长了读者就走了

## 引用格式

文中需要引述原文时用 markdown blockquote：
```markdown
> "原话原话原话" —— 出处
```

末尾**不需要**再放链接（外层 digest 会自动加）。

---

## 输出（纯 markdown，不要 JSON）

直接输出报道正文，**不要标题**（标题会由外层 digest 模板处理）。
不要"以下是我的报道"这种前置说明，**直接开始第一段**。

---

## 自检（写完前问自己 3 个问题）

1. 第一句话是判断还是复述？如果是复述，重写。
2. 第三段有具体引述/数字吗？没有的话从原文找。
3. 第四段对**这个具体用户**有意义吗？还是写给"通用人"看的？


</details>

---
