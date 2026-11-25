# Curio · 大厂 AI 动态 · 2026-11-25

> 今日 1 条头条 + 5 条备选

_今天真正的大信号只有一个：Nvidia 用两周时间演完了「逼宫—辞职—复职」全套，黄仁勋回归首场全员会承认在心理咨询、否认白宫干预，同时 SEC 在查会计问题、国会开骂、Anthropic 股价跌破 83 美元 IPO 价。AI 资本叙事第一次出现「治理风险」这个新变量，而不是算力或模型能力。另一条线是 Gemini 4 系列（Carbon/Hydrogen/Neon）在两周内连发三代，模型迭代节奏已经快到评测榜都跟不上。_

---

## 🌟 今日精选

### 2. Gemini 4 Neon 发布并登顶 Models Engineering Index，Google 两周内连发 Carbon / Hydrogen / Neon 三代

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _yigitdemirag_

10 月 28 日 Gemini 4 Carbon、11 月 12 日 Gemini 4 Hydrogen（含 Antigravity 里的 Orchestrator）、11 月 18 日 Gemini 4 Neon，三周三代。Neon 上线当天就在第三方 Models Engineering Index 登顶，有博主直接称它「看起来像 Opus 5.5 的竞争对手」。这个发布节奏本身比单代模型能力更值得注意。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 4 Carbon 于 10 月 28 日发布，10 月 29 日登上 Artificial Analysis Intelligence Index v5 第一 | 三代模型之间的实际能力差异有多大，目前只有第三方榜单和博主评测，缺少官方对比数据 |
| Gemini 4 Hydrogen 于 11 月 12 日发布，同步在 Google Antigravity 上线 Orchestrator | Neon 是否真是 Opus 5.5 同级，micjm.com 的判断属于个人评测而非系统基准 |
| Gemini 4 Neon 于 11 月 18 日发布，HN 1071 分 | Gemini 4 Carbon「为什么这么慢」的讨论（kernel.dev 一文 288 分）暗示发布节奏与内部工程压力存在张力 |
| Neon 在 Models Engineering Index 登顶，该榜单由第三方维护 | Orchestrator 在 Antigravity 里的具体编排能力边界尚不清楚 |
| Gemini Decisions API 于 11 月 11 日单独发布，是面向 Agent 决策的独立接口 | DeepMind 员工正在组建工会（gdmunion.co.uk），是否影响后续发布节奏未知 |
| Genie 4 世界模拟模型于 10 月 27 日发布、11 月 18 日开放使用 |  |

**📖 主编点评**

对你的 content-curator 项目来说，这是直接的工程信号：模型迭代周期已经压缩到 2-3 周，任何硬编码模型名的架构都会很快过时。如果你在 Agent 里写死了具体模型，现在就该把模型选择抽象成配置层。另外 Gemini Decisions API 值得单独看一眼——它是少数专门为 Agent 决策路径设计的官方接口，比通用 chat completion 更贴近你要做的事。

📺 [打开原文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

---

## 📋 备选阅读

- [即便最好的 AI Agent 也搞不定日常生活](https://techcrunch.com/2026/11/24/even-the-best-ai-agents-struggle-with-everyday-life/) —— 新基准显示顶级 Agent 在日常任务上仍不可靠且会引入新问题，和你做 Agent 项目直接相关，但报道偏结论缺方法细节。
  _Rebecca Bellan_
- [Amazon 收购 Decart，7.5 亿美元赌软件缩小与 Nvidia 的芯片差距](https://techcrunch.com/2026/11/24/amazons-decart-acquisition-is-a-bet-on-using-software-to-narrow-the-gap-with-nvidia-in-the-ai-chip-race/) —— 用软件效率补硬件差距的思路值得关注，但 7.5 亿美元数字来自「reported」，未经证实。
  _Anna Heim_
- [Walmart 联手 Meta，把黑五折扣搬进 AI Agent Muse](https://techcrunch.com/2026/11/24/walmart-teams-up-with-meta-to-bring-black-friday-deals-to-ai-agent-muse/) —— AI Agent 第一次成为零售大促的正式入口，商业信号强于技术信号，但对你个人项目参考价值有限。
  _Lauren Forristal_
- [Microsoft 因 Outlook 大规模宕机内部宣布「Code Red」](https://www.theverge.com/news/1042025/microsoft-code-red-outlook-outage) —— 近 24 小时邮件中断触发内部红色警报，是基础设施可靠性话题，但和你的关注方向关联弱。
  _Tom Warren_
- [Huawei 被判窃取美国商业机密](https://www.theverge.com/tech/1041820/huawei-guilty-trade-secrets-trial) —— 纽约联邦法院陪审团裁定有罪，地缘科技话题，但判决细节和后续影响尚未展开。
  _Emma Roth_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
