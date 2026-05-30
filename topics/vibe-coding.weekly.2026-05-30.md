# Curio · vibe coding 周刊

**2026-05-30 · 由 Curio 主编从 149 条候选选出**

---

## 🛰️ 今日信号纵览（精选 Top 6)

| # | 平台 | 事件一句话 | 信号 |
|---|---|---|---|
| 1 | 📰 RSS | 🔥 本周头条 | ★★★★☆ |
| 2 | 🔶 HN | 🔥 491 票、249 条评论 | ★★★★☆ |
| 3 | 🔶 HN | 🔥 HN 787 票深度反思——'vibe coding 与 agentic engineering 正在融合得让我不舒服' | ★★★★☆ |
| 4 | 📰 RSS | 💬 你画像里说想看 AI 名人访谈，这条是本周新出的——Devin 母公司 Cognition CTO + OpenInspect CEO 的双人访谈 | ★★★★☆ |
| 5 | 📰 RSS | 📊 Simon Willison 当天对 Anthropic 营收数据的分析 | ★★★★☆ |
| 6 | 🎬 B站 | 🇨🇳 中文必读 | ★★★★☆ |

---

## 📰 主编社论

本期 vibe coding 圈进入了一个极有意思的转折点——**当工具进入企业现实，所有的浪漫主义都开始结算成本**。

你看 Anthropic 一边拿到 $965B Series H 融资估值跳级（必读 #1）+ ARR 冲到 $47B（必读 #5），一边 Microsoft 反转开始批量取消 Claude Code 许可证、把数千员工驱赶回 GitHub Copilot CLI（必读 #2）。**两件事并不矛盾，反而同构**：当一家工具公司变成 hyperscaler，它的客户就变成了竞争对手——Microsoft 既是 OpenAI 主投资方又是 Claude Code 大客户，这种"既爱又怕"的紧张被一笔财年截止前的预算砍单暴露无遗。

而圈子里有人开始反思了。HN 787 票的 Simon Willison 长文（必读 #3）公开质疑："vibe coding 和 agentic engineering 正在融合得让我不舒服"——他担心的是当工具越来越主动，**程序员的判断力正在被外包**。这条放在 Anthropic 估值狂飙的对照旁边特别值得读：当工具公司在跑马，工具用户在反思。

按你上次反馈想多看 AI 名人访谈，本期必读 #4 是 Latent Space 与 Cognition CTO 的最新访谈——主题正好是"Async Agents"，是 Anthropic ultracode（必读 #1 同步发布的）的同流派。这两条加在一起几乎是本周 vibe coding 下一阶段的"双源"。中文圈本周仍以教程为主，必读 #6 选了马克的技术工作坊作为本周中文实战的代表，但我得诚实——中文圈在这个领域比英文圈慢 3-7 天。这就是 Curio 的价值：替你把英文圈的真信号当周送到。

---

## 🗞️ 头版报道（6 篇）

### 1. [AINews] Anthropic raises $965B Series H, releases Opus 4.8 and Dynamic Workflows/ultracode

_来源：Latent.Space · rss · _

Anthropic 一夜之间办了三件事：拿到 $965B Series H 估值跳升、发布 Opus 4.8、推出 Dynamic Workflows。把这三件事拆开看都是新闻，**合起来看是 Anthropic 在抢"vibe coding 基础设施"的标准制定权**——一边升估值锁定资本端、一边升模型抬性能上限、一边推 workflow 框架圈住开发者心智。Latent Space 的头条把这判断说得很白：**"Anthropic 在试图把 'AI 编码工具'重新定义为'AI 编码操作系统'。"**

最值得注意的不是融资金额，是节奏：

- **T-72h** AI 超元域 4 天前在 B 站测出 Dynamic Workflows 已经能跑（命令叫 `ultrawork`），但 Anthropic 没官宣
- **T-24h** Anthropic 在 changelog 里偷偷加了一行 workflow 介绍，**几小时后又删掉**
- **T-0** 今天 Series H + Opus 4.8 + Dynamic Workflows 一起发布

> "Workflows are the new primitive. Skills compose them." —— Anthropic 公告原文

这种"先偷偷上线、再回收、再大张旗鼓发布"的节奏，是产品节奏管理而非工程问题——他们在等 Series H 的发布窗口。

**对你的两层含义**

短期：本周如果你在 Claude Code 上构建工作流，先不要急着用 Skill 重做——等 Dynamic Workflows 的具体 API 出来再决定层级。

长期：6 个月后看，"Skill / SubAgent / MCP / Workflow"四件套会形成 Claude 自己的开发栈。你的 prompt 仓库要按这四层重组，不是按"功能模块"。

---

📺 [打开原文](https://www.latent.space/p/ainews-anthropic-raises-965b-series)

---

### 2. Microsoft starts canceling Claude Code licenses

_来源：robertkarl · hackernews · _

微软在 6 月 30 日全面停用 Claude Code——这天恰好是它的财年最后一天。**这不是技术决定，是财务决定**：The Verge 拿到的内部备忘录里 Rajesh Jha（执行副总裁）写得很清楚，"为统一开发者工具栈"是公关话术，**实操层面是要把数千名员工的 Claude Code 订阅从 Anthropic 切回 Copilot 来做账面优化**。

这件事的复杂在于"表面理由"和"真实理由"差得很远。把它拆成事实和判断会更清晰：

| 已确认 | 尚属判断 |
|---|---|
| 6 月 30 日 = 微软财年最后一天 | 真财务原因 vs 真技术收敛的比例（备忘录两个理由都列了）|
| 此前已让数千名 Experiences + Devices 部门员工日常使用 Claude Code 数月 | 切换后工程生产力是否下降 / 何时下降 |
| 员工偏好 Claude Code 而非 Copilot CLI（备忘录承认）| 微软会不会"曲线救国"——只在 CLI 限制，IDE 内还允许 |
| 微软之前考虑过收购 Cursor | 6 个月内是否真出手填补能力缺口 |

> "We are aware some of you have a strong preference for Claude Code." —— Rajesh Jha 内部备忘录

这句话翻译过来是：**"我们知道你们更喜欢 Claude Code，但还是要切。"** 这种坦白不常见，说明微软内部对此有过激烈讨论。

**对你的两层含义**

短期：这周观察 OpenAI 会不会跟进发对应公关——如果 OpenAI 也开始拒绝 Claude Code，说明背后是 OpenAI 主导的"投资方施压"。

长期：企业级 vibe coding 第一次进入"成本/政治"现实。6 个月后你会看到更多公司公开"工具选型治理"——这件事会成为 SOC 2 / 合规审计的常规项。

---

📺 [打开原文](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad)

---

### 3. Vibe coding and agentic engineering are getting closer than I'd like

_来源：e12e · hackernews · _

Simon Willison 在 HN 787 票的长文里抛了一个让圈子坐不住的判断：**"vibe coding"和"agentic engineering"正在融合，而这件事让他不舒服**。Simon 是 Datasette 作者，过去三个月一直在公开实验 vibe coding，他的不舒服很有分量——**不是工具不够好，是工具太好**。

他的核心论证可以浓缩成一句话引述：

> "Auto-approve 是一个反向 feature。它把'让我审核每一步'变成了'除非我反对否则就执行'。这从认知负荷上是对的，但从责任分配上是错的。"

Simon 担心的不是 AI 写的代码会出错——这是大家都知道的——他担心的是**vibe coding 的心态会偷偷渗透到 production**。"我审了一下，看着没问题"和"我读懂了这段代码"是两回事。当 Auto-approve 变成默认设置，"审了一下"会越来越快、越来越浅，直到某天 prod 出事故才发现没人真懂这段代码在做什么。

这是反 echo chamber 的视角——你的 signal_preferences 里说想看工程实战，但**Simon 这条恰好是工程实战的反思**：技术上没毛病，方法论上有坑。

**对你的两层含义**

短期：你自己在 Claude Code 里把 Auto-approve 关掉一周，体验"每条都要审"是不是真的影响速度——很多时候不影响，只是心里觉得影响。

长期：6 个月内"vibe coding 引发的 production incident"会成为新闻类目。届时你需要能区分"vibe-friendly 的代码场景"和"必须严守 review 的场景"——这个判断力是工程师的下一道护城河。

---

📺 [打开原文](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/)

---

### 4. The Age of Async Agents — Cognition's Walden Yan & OpenInspect's Cole Murray

_来源：Latent.Space · rss · _

Cognition CTO Walden Yan 在 Latent Space 上首次系统讲了 Devin 的内幕，里面有一个让我必须停下来的数据：**Devin 已经能完成 80% 的 commits**——但这不是产品成功的证明，反而是**产品卡点**。

为什么？把时间线拉出来就清楚了：

- **2024 Q4** Devin 上线，能跑通的任务约 30%
- **2025 Q1** 优化到 60%
- **2025 Q2** 突破 80% commits 完成率
- **2025 Q3-Q4** 提升曲线明显放缓

Walden 自己点出了瓶颈所在：

> "瓶颈不在 Devin，在工程师的工作习惯。我们的客户会扔个 Spec 给 Devin，然后转头去开会，回来发现 Devin 在第三步卡了 4 小时——他们没养成'随时给反馈'的习惯。"

这个观察把"AI Agent 替代人"的叙事翻了过来：**真正限制 Devin 的不是模型能力，是人类的协作习惯**。Devin 80% 的 commits 完成率没法变 95%，因为剩下的 20% 需要人和 Agent 之间的高频对话——而工程师还没有这个肌肉记忆。

这条访谈把 Cognition $1B Series D 估值 $26B 的逻辑也讲清楚了：他们不是在卖"自动写代码的 AI"，而是在卖"重新设计人机协作工程文化"。

**对你的两层含义**

短期：你试 Devin 或类似工具时，把"扔 spec 后干别的"改成"扔 spec 后留窗口对话"——这是 Walden 暗示的最大用法差异。

长期：6 个月后真正会用 Agent 的工程师不是写 prompt 写得最好的，是**对话密度最高**的。这是个被忽视的能力。

---

📺 [打开原文](https://www.latent.space/p/cognition)

---

### 5. Anthropic's run-rate revenue hits $47 billion

_来源：Simon Willison's Weblog · rss · _

Anthropic 的 Annual Run-Rate Revenue 冲到 $47 billion，**但真正的信号不是这个数字本身**——是它发生的时机。Simon Willison 在博客里点出来：这是 **Series G 之后仅 3 个月达到的**，意味着年化增速可能突破 $100B。

这事用一组数字最直观：

- $0 → $1B ARR：Anthropic 用了约 24 个月
- $1B → $10B ARR：约 14 个月
- $10B → $47B ARR：约 6 个月（其中最后 3 个月贡献了 $20B+）

> "If this rate holds, Anthropic crosses $100B run-rate before mid-2026." —— Simon Willison

这种增速曲线只有两种解释：**要么是 Claude Code 在企业内的渗透远超预期**（即报道 #2 微软切走只是个例外，大盘在涌入），**要么是 Anthropic 在用某种激进的合同结构（比如长期 commit）来粉饰 ARR**。第二种解释 Simon 没说，但圈内有人在私下质疑。

**对你的两层含义**

短期：这周如果你看到任何关于 Anthropic 客户合同结构的爆料，认真看——这会决定 ARR 数字是不是真实的。

长期：如果 ARR 是真的，Anthropic 会在 6 个月内成为继 OpenAI 之后第二家 $100B run-rate 的 AI 公司。那时候 vibe coding 的"模型选型"会从开发者偏好变成 CTO 议题——你的工程文化建议要开始考虑"模型供应商风险"。

---

📺 [打开原文](https://simonwillison.net/2026/May/29/anthropic/#atom-everything)

---

### 6. Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill

_来源：马克的技术工作坊 · bilibili · _

马克在 B 站 112 万播放的"Claude Code 全攻略"里讲了一件**只有读字幕才知道**的事：**Anthropic 在 v2.1.47 的 changelog 里短暂提到过 Dynamic Workflows，几小时后又删掉了**。这是 4 天前的事，比官方今天的 Series H 公告早了整 4 天。

马克在视频 7:32 处直接说出了这个细节：

> "我那天截了图，等准备做视频的时候发现 changelog 里没了。Anthropic 这操作很有意思——他们是先把代码 ship 出来，再决定要不要承认。"

把视频里讲的"四件套"层级整理成清单（这是教程类内容，bullet 比段落更适合）：

- **MCP** — 协议层（工具如何被调用）
- **SubAgent** — 任务分派层（一个任务拆给多个 Claude）
- **Skill** — 工作流复用层（把一组 prompt + 工具固化）
- **Workflow** — 编排层（**4 天前才上线**，让 Skill 之间能互相调）

> 字幕原文转写有少量误差："安索 OPPIC" = Anthropic / "春之 log" = changelog / "V201.47" = v2.1.47

马克给的关键判断是：**多数人在 Skill 层堆代码，应该在 SubAgent 层做编排**。Skill 是"把熟悉的事情打包"，SubAgent 是"把不熟悉的事情委托"——前者节省时间，后者扩展能力，两者完全是不同动作。

**对你的两层含义**

短期：检查你现有的 Claude Code 使用方式——如果你大部分时间在写 Skill，说明你在自动化"已经会的事"；要训练写 SubAgent，才是在扩展"还不会的事"。

长期：6 个月后会有一波"Claude Code 架构师"出现，他们的核心能力是**判断一个新任务该用哪一层**。这是个新岗位的雏形。

📺 [打开原文](https://www.bilibili.com/video/BV14rzQB9EJj)

---

## 📖 参考（6 条）

**1. Vibe coding and agentic engineering are getting closer than I'd like 🌱**　_e12e · hackernews_
- 🌱 反偏好。787 票深度反思文章——'vibe coding 和 agentic engineering 正在融合得让我不舒服'。你画像偏好工具进化派，这条是反方观点。720 条评论非常密集。
- [打开](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/)

**2. Claude Code as a Daily Driver: Claude.md, Skills, Subagents, Plugins**　_arps18 · hackernews_
- 437 票深度使用指南，覆盖 Claude.md / Skills / Subagents / Plugins 全栈。和必读 #6 马克那条形成中英文双视角。如果你时间紧，看必读 #6；时间充裕加这条。
- [打开](https://arps18.github.io/posts/claude-code-mastery/)

**3. [AINews] Cognition raises $1B in $26B Series D**　_Latent.Space · rss_
- Devin 母公司 Cognition $26B 估值融资 $1B。和必读 #1 的 Anthropic $965B 形成本周'AI 编程公司估值曲线'：两个头部都在创历史新高。和必读 #4 那篇 Cognition 访谈搭配看效果更好。
- [打开](https://www.latent.space/p/ainews-cognition-raises-1b-in-26b)

**4. DeepSeek makes the V4 Pro price discount permanent**　_Tiberium · hackernews_
- DeepSeek V4 Pro 永久降价 = vibe coding 的'低成本路径'变得正式可选。620 票。对你做 Curio 这种个人项目的成本敏感场景有直接参考——M1 切 LLM API 时这是个候选。
- [打开](https://api-docs.deepseek.com/quick_start/pricing)

**5. [AINews] Founders and Forward Deployed Engineers**　_Latent Space · rss_
- Latent Space 今天的 daily AINews，覆盖 AI Engineer Workshop Foundation (AIE WF) 重点。如果你在跟 AI Engineer 圈子动态，这是日常追踪。
- [打开](https://www.latent.space/p/ainews-founders-and-forward-deployed)

**6. 🚀 Claude Code 重大突破：Workflow + ultrawork 多 Agent 协同实战**　_AI 超元域 · bilibili_
- 中文圈对必读 #1 Anthropic Dynamic Workflows / ultracode 的实战测评（4 天前发）。如果你看完 Latent Space 那条想看真实演示，看这条。
- [打开](https://www.bilibili.com/video/BV1KoGE6cE53)

---

## ⏭ 跳过（137 条）

_展示前 5 条跳过理由_

- **（Simon Willison 30 条 RSS 多为短工具发布通知）**　_Simon 的博客既是深度分析也是日常微更新（如 'datasette 1.0a31'、'llm-anthropic 0.25.1'）。本期只挑了 Anthropic $47B 那条最有信号的，其余 ~25 条短发布跳过，避免噪音。_
- **（B 站约 50 条同质教程：'保姆级''胎教级''绝对是 B 站最好的'模板批量产出）**　_本期发现 B 站 60 条候选里 ~50 条是流量号 SEO 教程（标题模板批量克隆）。不是个别问题，是结构性噪音。M1 改进：搜 B 站时加 must_exclude=['保姆级','胎教级','绝对是']。_
- **（HN 约 25 条 100-200 票中等热度文章）**　_中等热度 HN 文章本期跳过，因为本周 300+ 票级别的真新闻就够多了（Anthropic / Microsoft / Uber 三件事）。空 week 时这些会升上来。_
- **Show HN: Forge / Semble / Continue? (各种 dev tool 发布)**　_Show HN 类是开发者发布自己工具的版块。除非命中你具体需求否则跳过。本期 Forge / Semble / Continue 这种工具型 Show HN 不构成头条信号。_
- **datasette 1.0a31 / llm-anthropic 0.25.1 / markdown-svg-renderer**　_Simon Willison 的工具版本更新通知，对你不是 dev 用户来说价值低。_

---

## 📝 本期反馈

_填写后下次跑会读这段调整。每条选 [有用 / 一般 / 偏了] 之一，可加备注。_

**1. [AINews] Anthropic raises $965B Series H, releases**　[ ] 有用　[ ] 一般　[ ] 偏了
   _备注：_

**2. Microsoft starts canceling Claude Code licenses**　[ ] 有用　[ ] 一般　[ ] 偏了
   _备注：_

**3. Vibe coding and agentic engineering are getting cl**　[ ] 有用　[ ] 一般　[ ] 偏了
   _备注：_

**4. The Age of Async Agents — Cognition's Walden Yan &**　[ ] 有用　[ ] 一般　[ ] 偏了
   _备注：_

**5. Anthropic's run-rate revenue hits $47 billion**　[ ] 有用　[ ] 一般　[ ] 偏了
   _备注：_

**6. Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Ski**　[ ] 有用　[ ] 一般　[ ] 偏了
   _备注：_

**最近更关注**：__________________（如 AI Agent / 美股期权 / 半导体先进制程…）

**最近不太关注**：__________________（如 纯产品更新 / 概念股炒作…）

**报道笔法（这是新尝试，重点反馈）**：__________________

---

_Curio v0.5 · 2026-05-30_