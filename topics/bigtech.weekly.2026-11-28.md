# Curio · 大厂 AI 动态 · 2026-11-28

> 今日 1 条头条 + 3 条备选

_今天最重要的信号有两个：一是 Nvidia 的治理危机彻底变成产业事件——Jensen Huang 被董事会请回 CEO，同时 SEC 会计调查、东南亚出货暂停、国会与标普质疑董事会独立性全部叠在一起，这不是八卦，是算力供应链的定价重估。二是 Anthropic IPO 从 1.5T 定价一路跌破 83 美元发行价，AI 资产的信用定价开始被市场重新审视。其余候选池以教程和黑五促销为主，深度内容稀缺。_

---

## 🌟 今日精选

### 3. Gemini 4 Neon 发布并登顶 Models Engineering Index，Google 一个月内连发四代模型

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _yigitdemirag_

Google 在 11 月连续放出 Gemini 4 Carbon、4 Hydrogen、4 Neon 三代模型，Neon 上线后直接冲到 Models Engineering Index 第一，被社区拿来和 Opus 5.5 对标。同期还有 Gemini Decisions API 和 Genie 4 落地，发布节奏明显加快。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 4 Neon 已在 Google 官方博客发布，HN 讨论超 1000 分 | Models Engineering Index 是第三方榜单，权威性不及 Artificial Analysis，排名第一的说服力有限 |
| Neon 在 Models Engineering Index 上排名第一 | Neon 在真实 Agent 长任务上的稳定性，目前缺少工程侧复现 |
| 11 月内 Google 还发布了 Gemini 4 Carbon、Gemini 4 Hydrogen 与 Gemini Omni 1.2 Flash | 一个月四代模型的命名体系是否会让企业客户选择困难，Google 未解释 |
| Gemini Decisions API 与 Genie 4 同期上线 | 与 Opus 5.5 的实际差距需要等独立评测 |
| 社区评测文章将 Neon 定位为 Opus 5.5 的竞争者 |  |

**📖 主编点评**

你重度用 Agent，值得花半小时把 Neon 接进你现有的工具链跑一遍真实任务，而不是看榜单。重点测两件事：长上下文下的工具调用成功率、以及 Decisions API 能不能替代你自己写的路由逻辑。如果 Decisions API 好用，content-curator 的选稿分支可以省掉一层自研。

📺 [打开原文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

---

## 📋 备选阅读

- [AMD 专用版 llama.cpp 分支](https://devnull.land/amd-specific-llama-cpp) —— 对没有 N 卡但想本地跑模型的人有实际价值，属于工具类增量信息。
  _julianlam_
- [llama-modchip：64GB 内存无 GPU 跑 284B DeepSeek](https://github.com/synchopate/llama-modchip) —— 极客向的本地推理实验，思路有意思但可用性存疑，放备选观察。
  _joshcsimmons_
- [DeepMind 员工正在组建工会](https://www.gdmunion.co.uk) —— AI 实验室劳资关系的新动向，长期值得跟踪，今天信息量还不足以做头条。
  _nervai_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
