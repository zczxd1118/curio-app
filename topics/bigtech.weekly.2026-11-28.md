# Curio · 大厂 AI 动态 · 2026-11-28

> 今日 1 条头条 + 4 条备选

_今天最重要的信号只有一个：Nvidia 的治理危机已经盖过技术叙事——黄仁勋被董事会请回 CEO，SEC 会计调查、国会质询、Polymarket 内幕交易、东南亚出货暂停同时压上来，芯片股跟着崩。第二个信号是 Anthropic IPO 破发到 83 美元以下，AI 泡沫的定价开始被市场用脚投票。这两件事合起来说明：AI 的资本周期正在从'叙事驱动'转向'审计驱动'。_

---

## 🌟 今日精选

### 3. Gemini 4 Neon 发布并登顶 Models Engineering Index，Google 一个月内连发四代模型

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _yigitdemirag_

Google 在 11 月连续发布 Gemini 4 Carbon、4 Hydrogen、4 Neon 三代模型，外加 Genie 4、AlphaProof Code、Gemini Decisions API。Neon 在 Models Engineering Index 上登顶，被社区视为 Opus 5.5 的直接对手。这种发布节奏本身比单个模型更值得注意：Google 在用版本号密度抢占开发者心智。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 4 Neon 官方博客发布，HN 首页 1071 分 | Models Engineering Index 是个人维护的第三方榜单，权威性不及 Artificial Analysis 或 LMSYS |
| Neon 在 Models Engineering Index 上排名第一（第三方站点 git-aarvin.github.io/mei） | 'Neon 是 Opus 5.5 竞品'的判断来自个人博客 micjm.com，尚无独立基准复现 |
| 同月内 Carbon、Hydrogen、Neon 三代模型先后上线，另有 Genie 4 与 AlphaProof Code | 一个月四代模型是否意味着内部版本管理混乱，还是刻意的发布策略，外界无法判断 |
| Gemini Decisions API 面向开发者开放，定位为决策类工具调用 | Decisions API 的实际能力边界（是否只是结构化输出封装）官方文档未充分说明 |
| DeepMind 员工正在组建工会（gdmunion.co.uk） | 工会化对 DeepMind 产品节奏的影响目前为零，但值得长期跟踪 |

**📖 主编点评**

你该做的是别追版本号，追 API 差异。Neon 和 Decisions API 如果真把'决策/工具调用'做成一等公民，对你的 Agent 项目是直接利好——意味着你少写一层 orchestration。花 20 分钟读 Decisions API 文档，比看十个'Neon 实测'视频有用。

📺 [打开原文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

---

## 📋 备选阅读

- [AMD-specific fork of llama.cpp](https://devnull.land/amd-specific-llama-cpp) —— AMD 专用 llama.cpp 分支，HN 444 分。如果你考虑本地跑模型，这是绕开 CUDA 生态的一条现实路径。
  _julianlam / HN_
- [Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU](https://github.com/synchopate/llama-modchip) —— 64GB 内存无 GPU 跑 284B 模型的开源项目。工程猎奇价值高，实际可用性存疑，但思路值得看。
  _joshcsimmons / HN_
- [Stacktrace — Real-time steering and guardrails for AI agents](https://www.producthunt.com/products/stacktrace) —— 给 Agent 做实时干预和护栏的产品。和你的 content-curator 直接相关，可以看它怎么定义'steering'的接口。
  _Nico Lumma / Product Hunt_
- [OpenCrawl — Multiplayer for your coding agents](https://www.producthunt.com/products/opencrawl) —— 多个 coding agent 协作的'多人模式'。概念新，产品成熟度未知，但方向正好卡在你的子 Agent 兴趣点上。
  _Nico Lumma / Product Hunt_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
