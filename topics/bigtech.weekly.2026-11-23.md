# Curio · 大厂 AI 动态 · 2026-11-23

> 今日 1 条头条 + 4 条备选

_今天最重要的两个信号：一是 Nvidia 的治理危机已经从八卦升级成财务与监管事件——SEC 查会计问题、新加坡 104B 收入口径消失、董事会在讨论请回黄仁勋，这不是一个人事新闻，是 AI 算力供应链的定价风险。二是 Google 一周内连发 Gemini 4 Carbon / Hydrogen / Neon 三代模型，Neon 已登顶多个工程指数，模型迭代节奏快到评测体系本身开始失效。_

---

## 🌟 今日精选

### 2. Gemini 4 Neon 发布并登顶 Models Engineering Index，Google 一个月内连发三代 4 系模型

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _yigitdemirag_

Google 在 10 月底到 11 月中连续放出 Gemini 4 Carbon、Hydrogen、Neon 三个版本，Neon 上线后迅速在 Models Engineering Index 拿到第一，社区评测认为它是 Opus 5.5 的直接对手。同时 Antigravity 平台已接入 Hydrogen 与 Orchestrator。节奏之快，已经让"等下一代再评测"的策略失效。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 4 Neon 已在 Google 官方博客发布，HN 讨论 1066 分 | Models Engineering Index 是社区自建指标，权威性不及 Artificial Analysis，排名需交叉验证 |
| Neon 在 Models Engineering Index 上排名第一，HN 帖 376 分 | 三代模型命名（Carbon/Hydrogen/Neon）对应的能力分层官方未清晰说明 |
| Gemini 4 Carbon 曾在 Artificial Analysis Intelligence Index v5 上排名第一 | Neon 相对 Opus 5.5 的实际差距目前只有博客级对比，缺独立复现 |
| Gemini 4 Hydrogen 与 Orchestrator 已集成进 Google Antigravity 平台 | Antigravity 的 Orchestrator 是否等同于多 Agent 编排，官方文档尚未展开 |
| Google 同期发布 Gemini Decisions API 与 Gemini Omni 1.2 Flash |  |

**📖 主编点评**

你的 Agent 项目现在有一个真实的选择题：模型层要不要做抽象。一个月三代模型、每代都可能换最优解，硬编码单一 provider 的代价变高了。建议在 content-curator 里把模型调用收敛到一个薄适配层，prompt 与工具定义独立于模型，这样换 Neon 或 Opus 5.5 只改配置不改逻辑。

📺 [打开原文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

---

## 📋 备选阅读

- [Walmart 明天开放 Agent Gateway，允许 Meta Muse 代用户在网站上下单黑五折扣](https://www.theverge.com/ai-artificial-intelligence/1039874/walmart-agent-gateway-meta-muse-black-friday) —— Agent 电商代购的第一个大规模真实场景，11 月 24 日上线，值得盯后续的授权与风控设计。
  _Jess Weatherbed_
- [Stratechery：Amazon 财报、芯片问题与关于 Agent 的讨论](https://stratechery.com/2026/amazon-earnings-the-chip-question-about-agents/) —— Ben Thompson 今天的分析，核心是 Amazon 愿意牺牲毛利服务前沿客户，长文深度，周末 2 小时档。
  _Ben Thompson_
- [Signal 限制移动端截图，称面对 AI 监控的"生存级威胁"](https://techcrunch.com/2026/11/21/signal-restricts-mobile-screenshots-as-it-confronts-existential-threat-of-ai-surveillance/) —— 隐私工具对 AI 监控的第一次产品级反制，方向值得关注，但具体实现细节披露很少。
  _Anthony Ha_
- [OpenAI 首席科学家谈如何给 AI 发展设限：先得就"怎么测速度"达成一致](https://techcrunch.com/2026/11/22/openais-chief-scientist-has-thoughts-on-how-to-limit-ai-development/) —— 契合你想多看访谈类内容的偏好，但这是二手转述，深度有限，可跳。
  _Anthony Ha_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
