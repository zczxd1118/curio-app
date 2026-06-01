# Curio · AI · 2026-06-01

> 今日 2 条头条 + 0 条备选

_今天Computex 2026开幕，NVIDIA正式发布RTX Spark超级芯片，标志着AI PC进入新纪元。同时，OpenAI数学突破解决80年难题，AI能力边界再拓宽。但企业AI支出开始理性化，Token经济学遭遇挑战。_

---

## 🌟 今日精选

### 2. OpenAI模型解决困扰人类80年的数学难题，AI推理能力再突破

**[AI]** · ⭐⭐⭐⭐⭐ · _Ars Technica_

OpenAI的一个未公开模型解决了'Keller猜想'的变体——一个组合几何问题，自1940年代以来无人能解。Ars Technica的深度分析指出，这次突破的关键不是算力堆砌，而是模型学会了'构造反例'的推理策略。这不是AGI，但这是AI在数学研究中从'助手'变成'合作者'的标志。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 解决的是Keller猜想的一个变体，属于组合几何领域 | 该突破是否可泛化到其他数学领域尚不明确 |
| 模型采用'构造性反例'策略，而非暴力搜索 | 模型是否使用了特殊训练数据（如形式化数学语料）未披露 |
| 解决方案已通过同行评审，发表于数学期刊 | 与DeepMind的AlphaGeometry相比，方法论差异待分析 |
| OpenAI未公开该模型的具体参数规模 | 对实际工程应用（如代码推理）的迁移价值未知 |
|  | OpenAI可能将其能力整合到未来版本的GPT中 |

**📖 主编点评**

这对你的AI Agent项目有间接启示：推理能力正在从'模式匹配'转向'策略构造'。如果你在Claude Code或Cursor中遇到复杂调试问题，可以尝试让模型'构造反例'而非直接修复——这种思维链策略可能更有效。关注OpenAI后续是否将此类推理能力集成到API中。

📺 [打开原文](https://arstechnica.com/ai/2026/06/openais-math-breakthrough-played-to-ais-strengths/)

---

### 5. Claude Code隐藏Workflow功能曝光：脚本化多Agent协同，AI编程进入'工作流即代码'时代

**[AI]** · ⭐⭐⭐⭐ · _AI超元域_

B站UP主'AI超元域'发现并实测了Anthropic未官宣的Claude Code Workflow功能。该功能允许用户用JS脚本定义多Agent协作流程，实现'一个指令召唤多个子Agent并行工作'。虽然官方从Changelog中删除了相关描述，但代码中仍保留该功能。这可能是AI编程工具从'单兵作战'到'团队协作'的关键进化。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Claude Code V2.1.47和V2.1.48版本中存在Workflow功能 | 该功能是否会被官方正式支持尚不确定 |
| 支持用JavaScript脚本定义多Agent协作流程 | 脚本化工作流的调试和错误处理机制不完善 |
| 可实现子Agent并行执行、结果聚合、条件分支 | 多Agent并行时的Token消耗和成本控制未知 |
| 官方从Changelog中删除了该功能描述但未移除代码 | 与Cursor的YOLO模式、Windsurf的Flow模式的对比待验证 |

**📖 主编点评**

如果你在用Claude Code做content-curator项目，这个Workflow功能可以让你定义'采集→摘要→分类→存储'的自动化流水线。建议立即尝试V2.1.47版本，用JS脚本构建你的第一个多Agent工作流。即使官方后续移除，这种'工作流即代码'的思路也会成为AI编程的标配。

📺 [打开原文](http://www.bilibili.com/video/av116629702777532)

---

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
