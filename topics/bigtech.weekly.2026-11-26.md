# Curio · 大厂 AI 动态 · 2026-11-26

> 今日 1 条头条 + 4 条备选

_今天真正的信号是 Nvidia 治理危机进入第二阶段：Jensen Huang 被董事会火速复职，但 S&P 已在考虑下调其信用评级，国会、SEC 与 Polymarket 异常交易同时压上来，AI 算力叙事第一次被公司治理而非需求打断。另一条主线是 Anthropic IPO 破发——$83 发行价上市后迅速跌破，$1.5T 估值被市场当场打折，AI 泡沫的定价开始由二级市场说了算。_

---

## 🌟 今日精选

### 3. Gemini 4 Neon 发布并登顶 Models Engineering Index，被社区视为 Opus 5.5 的直接对手

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _yigitdemirag_

Google 在 11 月连发 Gemini 4 Carbon、Hydrogen、Neon 三个版本，Neon 是当前最强的一版，HN 1071 分、MEI 榜首。社区讨论的焦点不是跑分，而是它在 Antigravity 里配合 Orchestrator 做多 Agent 调度的实际表现。同时 Gemini 4 Carbon 的「为什么这么慢」也成了独立热帖。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 4 Neon 已在 Google 官方博客发布，HN 首页 1071 分 | Neon 相对 Opus 5.5 的真实差距目前只有博客对比，缺第三方复现 |
| Neon 在 Models Engineering Index 上排名第一，作者自建榜单，HN 376 分 | MEI 是个人自建榜单，权威性弱于 Artificial Analysis，排名第一的说服力要打折 |
| Gemini 4 Hydrogen 已集成进 Google Antigravity，配套 Orchestrator 多 Agent 调度 | Antigravity + Orchestrator 的多 Agent 调度是否稳定，社区反馈还太少 |
| Gemini 4 Carbon 在 Artificial Analysis Intelligence Index v5 上曾登顶 | Gemini 数据路由给人工标注的争议是否会影响企业客户采购，尚无客户侧回应 |
| Google 员工公开请愿，反对公司惩罚不愿采用 AI 的学校 | Carbon 发布节奏拖慢的原因，Google 未正面解释 |
| Gemini 被曝将个人 Drive 文件与邮件路由给人工标注员，HN 740 分 |  |

**📖 主编点评**

你在做 Agent 项目，Neon + Antigravity Orchestrator 这套组合值得这周就上手试一次——重点不是比分数，而是看它的多 Agent 调度接口和你的子 Agent 架构能不能对上。另外，Gemini 把用户数据路由给人工标注这件事，如果你打算把 content-curator 的用户数据接到任何大厂 API，先读一遍对方的数据使用条款再决定。

📺 [打开原文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

---

## 📋 备选阅读

- [OpenAI 合并 Chat 与 Work，重度用户会更早撞上用量上限](https://techcrunch.com/2026/11/25/openai-says-heavy-chatgpt-users-may-hit-limits-sooner-as-it-merges-chat-and-work/) —— 统一用量表意味着你的 Agent 项目如果依赖 ChatGPT 额度，成本模型要重算。
  _Jagmeet Singh_
- [FCC 批准 SpaceX 把 AI 数据中心送上太空的计划](https://techcrunch.com/2026/11/25/fcc-approves-spacex-plan-to-put-ai-data-centers-in-space/) —— 监管放行是事实，但科学界对干扰天文观测的担忧被 FCC 以「超出管辖」驳回，值得记一笔。
  _Kirsten Korosec_
- [Dario Amodei 回应「向 AI 交出人类控制权」的指控，称其荒谬](https://techcrunch.com/2026/11/25/anthropics-dario-amodei-calls-accusations-of-surrendering-human-control-to-ai-absurd/) —— 符合你想多看名人访谈/表态的偏好，但这条只有立场没有新事实，所以放备选。
  _Rebecca Bellan_
- [纽约州禁止 AI 聊天玩具五年，Common Sense Media 研究指出安全失效](https://techcrunch.com/2026/11/25/want-to-buy-your-kid-an-ai-toy-this-christmas-not-in-new-york/) —— AI 硬件的监管先例，对做消费级 Agent 产品的人是早期信号。
  _Rebecca Bellan_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
