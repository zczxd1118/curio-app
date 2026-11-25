# Curio · 大厂 AI 动态 · 2026-11-25

> 今日 2 条头条 + 4 条备选

_今天真正的大新闻只有一条：Nvidia 董事会在一周内把黄仁勋赶下台又请回来，Trump 被指直接介入，国会与 SEC 同时开火——这不是人事八卦，而是 AI 算力供应链治理结构的一次压力测试。另一条值得盯的是 Anthropic 跌破 83 美元 IPO 发行价、护盘仓位已平，AI 一级市场估值开始被二级市场重新定价。_

---

## 🌟 今日精选

### 3. Gemini 4 Neon 发布并登顶 Models Engineering Index，被指对标 Opus 5.5

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _yigitdemirag_

Google 在 11 月 18 日发布 Gemini 4 Neon，三天后登上第三方 Models Engineering Index 榜首，独立博客 micjm.com 直接把它称为「Opus 5.5 的竞争者」。这是 Google 在两个月内发布的第四个 Gemini 4 变体（Carbon、Hydrogen、Neon，加上 Genie 4），命名体系已经让外部难以追踪。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 4 Neon 于 11 月 18 日发布，HN 1071 分 | Models Engineering Index 是个人维护的第三方榜单，权重与方法论未公开，不能等同于行业共识 |
| 11 月 19 日登上 Models Engineering Index 第一，作者为第三方 git-aarvin | 「对标 Opus 5.5」目前只有一篇独立博客的判断，缺少同任务对比数据 |
| Gemini 4 Carbon 此前于 10 月 28 日发布，11 月 10 日正式可用，曾登顶 Artificial Analysis Intelligence Index v5 | 四个变体的定位差异（Carbon/Hydrogen/Neon）官方文档尚未给出清晰矩阵 |
| Gemini 4 Hydrogen 于 11 月 12 日发布，同步上线 Google Antigravity 平台 | Neon 在 Agent 长任务上的实际稳定性没有公开 benchmark |
| Genie 4 世界模拟模型于 10 月 27 日发布，11 月 18 日开放使用 | 定价与速率限制未在发布博客中明确 |

**📖 主编点评**

你的 content-curator 如果要接多模型路由，现在必须处理「同一家族四个变体」的选择问题。建议别追榜单，直接用你自己的真实任务（比如一次完整的选题+摘要流水线）跑 A/B，把 token 成本和一次通过率记下来——这比任何第三方 index 都可靠。

📺 [打开原文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

---

### 4. 新 benchmark 显示最强 AI Agent 在日常任务上仍不可靠，且会引入新问题

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Rebecca Bellan_

TechCrunch 报道了一个针对个人助理场景的新 benchmark，结论是即便最先进的模型也难以可靠、安全地完成日常任务，并且在失败时会引入新的风险。这条和你的项目直接相关——你做的是每天自动跑一遍的 Agent 流水线，可靠性比能力上限更重要。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 新 benchmark 聚焦个人 AI 助理的日常任务完成率与安全性 | benchmark 的具体任务集、评分口径与开源情况报道未披露，无法复现 |
| 结论是顶级模型在可靠性上仍有明显缺口，失败时会引入新问题 | 「引入新问题」的具体类型（越权操作、错误下单还是隐私泄露）未细分 |
| 报道时间为 11 月 24 日，作者 Rebecca Bellan | 样本规模与模型版本未公开，结论的统计强度存疑 |
| 同期 Walmart 把黑五促销接入 Meta 的 AI agent Muse，说明消费级 Agent 已进入真实交易场景 | 对长周期、多步骤任务的覆盖程度未知 |

**📖 主编点评**

这条应该直接改变你的工程决策：给 content-curator 加一层「失败可见」——每次运行输出结构化日志（选了哪些候选、为什么跳过、哪一步降级），而不是只给最终 JSON。Agent 不可靠是常态，可观测性才是你的护城河。

📺 [打开原文](https://techcrunch.com/2026/11/24/even-the-best-ai-agents-struggle-with-everyday-life/)

---

## 📋 备选阅读

- [Amazon's Decart acquisition is a bet on using software to narrow the silicon gap with Nvidia](https://techcrunch.com/2026/11/24/amazons-decart-acquisition-is-a-bet-on-using-software-to-narrow-the-silicon-gap-with-nvidia/) —— 75 亿美元收购 Decart 提升 Trainium 效率，是「软件补硬件」路线的重要下注，但交易细节仍少。
  _Anna Heim_
- [Microsoft declares 'Code Red' after huge Outlook outage](https://www.theverge.com/news/1042025/microsoft-code-red-outlook-outage) —— 近 24 小时的 Exchange Online 中断触发内部 Code Red，基础设施可靠性话题，与 AI 弱相关。
  _Tom Warren_
- [Huawei found guilty of stealing trade secrets](https://www.theverge.com/tech/1041820/huawei-guilty-trade-secrets-trial) —— 纽约联邦法院陪审团裁定华为窃取商业秘密，中美科技博弈的法律节点，影响待观察。
  _Emma Roth_
- [Tidal to ban and remove millions of AI-generated tracks as AI slop inundates music streaming](https://techcrunch.com/2026/11/24/tidal-to-ban-and-remove-millions-of-ai-generated-tracks-as-ai-slop-inundates-music-streaming/) —— 平台首次大规模清理纯 AI 生成内容，对内容平台治理有参考价值，但与你项目距离较远。
  _Ivan Mehta_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
