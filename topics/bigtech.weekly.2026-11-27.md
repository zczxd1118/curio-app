# Curio · 大厂 AI 动态 · 2026-11-27

> 今日 1 条头条 + 4 条备选

_今天最重的信号来自 Nvidia：Jensen Huang 被董事会重新任命为 CEO，同时公司暂停向东南亚出货、SEC 调查会计问题、S&P 考虑下调信用评级——一家公司的治理风险正在变成整个 AI 算力供应链的风险。另一条线是 Anthropic 上市后跌破 83 美元发行价，AI 资本叙事第一次出现公开市场的反向定价。对做 Agent 的你来说，工具链层面真正的新东西是 T3 Code 这类多 Agent 并行工作台。_

---

## 🌟 今日精选

### 3. Gemini 4 Neon 发布，在 Models Engineering Index 上登顶，被指对标 Opus 5.5

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _yigitdemirag_

Google 在 11 月 18 日发布 Gemini 4 Neon，随后在第三方 Models Engineering Index 上排到第一，社区讨论普遍把它和 Opus 5.5 放在同一档比较。这是 Google 在一个月内连续放出 Carbon、Hydrogen、Neon 三个 Gemini 4 变体后的最新一版。发布节奏本身比单次跑分更值得注意。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 4 Neon 于 11 月 18 日在 Google 官方博客发布，HN 讨论 1071 分 | Models Engineering Index 是社区维护的第三方榜单，权重设计未公开，排名第一不等于综合最强 |
| 该模型在 Models Engineering Index 上排名第一，索引页面公开可查 | 「对标 Opus 5.5」目前只是博客作者的判断，没有官方基准对比 |
| Google 在 10 月底至 11 月中旬已连续发布 Gemini 4 Carbon、4 Hydrogen、Omni 1.2 Flash 等多个变体 | Neon 与 Carbon、Hydrogen 的定位差异官方说明含糊，命名体系像营销分层而非能力分层 |
| Gemini 4 Carbon 曾在 Artificial Analysis Intelligence Index v5 上排第一 | 实际编码与 Agent 任务表现缺少独立复现，社区评测样本还很少 |
| Google 同期发布 Genie 4 与 AlphaProof Code | 定价与上下文窗口细节在发布博客中不完整 |

**📖 主编点评**

别急着换模型。你现在跑 Agent 的核心成本是调试 prompt 和工具链，不是模型分数。真正值得做的是：拿你自己 content-curator 的 3-5 个真实任务，在 Neon 和当前模型上各跑一遍，看工具调用成功率而不是看榜单。如果 Google 的发布节奏继续这个密度，模型选型会变成季度动作，把评测脚本固化下来比追新更有价值。

📺 [打开原文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

---

## 📋 备选阅读

- [OpenAI 合并 Chat 与 Work，重度用户会更早触达用量上限](https://techcrunch.com/2026/11/25/openai-says-heavy-chatgpt-users-may-hit-limits-sooner-as-it-merges-chat-and-work/) —— 统一用量计费表。对重度用户是实质性收紧，做 Agent 项目时要重新算 token 预算。
  _TechCrunch_
- [FCC 批准 SpaceX 在太空部署 AI 数据中心的计划](https://techcrunch.com/2026/11/25/fcc-approves-spacex-plan-to-put-ai-data-centers-in-space/) —— FCC 驳回了科研威胁等反对意见，理由是超出其监管权限。听起来科幻，但批文是真的，算力基建的边界在往外推。
  _TechCrunch_
- [Dario Amodei 回应「向 AI 交出人类控制权」指控：荒谬](https://techcrunch.com/2026/11/25/anthropics-dario-amodei-calls-accusations-of-surrendering-human-control-to-ai-absurd/) —— 竞争对手指控他在自动化研发上走得太远。属于你偏好的名人表态类内容，但只有立场没有技术细节，所以放备选。
  _TechCrunch_
- [AMD 专用版 llama.cpp 分支](https://devnull.land/amd-specific-llama-cpp) —— 针对 AMD 硬件的推理优化分支，HN 377 分。如果你以后想在非 Nvidia 硬件上跑本地模型，这是条实用线索。
  _HN_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
