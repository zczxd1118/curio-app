# Curio · 大厂 AI 动态 · 2026-11-28

> 今日 1 条头条 + 3 条备选

_今天最重要的信号有两个：一是 Nvidia 董事会把黄仁勋请回 CEO 位子，但 SEC 会计调查、国会质疑、S&P 警告董事会独立性、东南亚出货暂停同时压上来，这件事已经从人事八卦变成治理与出口管制的双重风险；二是 Anthropic IPO 定价 $83、估值 $1.5T 后迅速跌破发行价，AI 资产的定价逻辑正在被重新校准。对做 Agent 的你来说，工具层今天没有大新闻，但 Claude Code 桌面端整合、Gemini 4 系列迭代仍在推进。_

---

## 🌟 今日精选

### 3. Google 发布 Gemini 4 Neon，在 Models Engineering Index 上登顶，被指对标 Opus 5.5

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _yigitdemirag_

Gemini 4 系列今年迭代极快：Carbon、Hydrogen、Neon 接连发布，Neon 上线后直接冲到 Models Engineering Index 第一，社区评价它'看起来像 Opus 5.5 的竞争对手'。同期 Google 还放出了 Gemini Decisions API 和 Genie 4，模型层和工具层一起推。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 4 Neon 已通过 Google 官方博客发布 | Neon 的实际编码与 Agent 任务表现是否真能对标 Opus 5.5，需要独立评测而非榜单 |
| Neon 在 Models Engineering Index 上排名第一，该榜单由第三方维护 | Models Engineering Index 的权威性和评测方法未公开细节，排名需谨慎看待 |
| Gemini 4 Carbon 此前在 Artificial Analysis Intelligence Index v5 上曾登顶 | Gemini 4 系列迭代过快，模型命名（Carbon/Hydrogen/Neon）对开发者选择造成困惑 |
| Google 同期发布 Gemini Decisions API，面向开发者工具场景 | Decisions API 的具体能力和定价尚未清晰 |
| Genie 4 已开放使用，DeepMind 发布相关博客 | Google 内部员工工会化、抗议向学校施压等事件是否影响产品节奏 |
| Gemini 4 Hydrogen 与 Orchestrator 已在 Google Antigravity 平台上线 |  |

**📖 主编点评**

如果你在 content-curator 里做模型路由，现在值得把 Gemini 4 Neon 加进候选池实测一轮，尤其是长上下文和工具调用场景。但别只看榜单——用你自己的真实任务（比如抓取+摘要+结构化输出）跑一遍，比任何 index 都准。

📺 [打开原文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

---

## 📋 备选阅读

- [AMD-specific fork of llama.cpp](https://devnull.land/amd-specific-llama-cpp) —— llama.cpp 的 AMD 专用分支，对没有 N 卡但想本地跑模型的开发者是实用增量，444 分说明需求真实。
  _julianlam / HN_
- [Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU](https://github.com/synchopate/llama-modchip) —— 在 64GB 内存、无 GPU 的机器上跑 284B DeepSeek，工程取巧思路值得一看，但实用性待验证。
  _joshcsimmons / HN_
- [Stacktrace: Real-time steering and guardrails for AI agents](https://www.producthunt.com/products/stacktrace) —— 给 AI Agent 做实时转向和护栏的工具，正好踩在 Agent 可控性这个痛点上，值得关注其实现方式。
  _Nico Lumma / Product Hunt_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
