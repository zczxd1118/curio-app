# Curio · 大厂 AI 动态 · 2026-11-03

> 今日 2 条头条 + 4 条备选

_今天最值得看的两条线：一是 AI 资本结构开始承压——Marvell 1150 亿美元吞下 Lumentum、Oracle 发 200 亿股债、Intel 领跌 3.5 万亿芯片股回调，钱在往光互联和算力上压重注，同时市场开始怀疑回报；二是 Anthropic 一边限制 Claude Code 复刻游戏 IP，一边自曝接近 RSI，模型厂商的自我约束和自加速同时发生。_

---

## 🌟 今日精选

### 2. Anthropic 自曝「非常接近 RSI」：AI 开始能改进自己，公司同时给 Claude Code 加限制

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _Julie Bort_

同一天两条 Anthropic 新闻放在一起看才有意思：一边警告自己接近递归自我改进（RSI），一边确认给 Claude Code 加了禁止复刻游戏 IP 的系统提示。能力在加速，约束也在加码，这不是矛盾，是同一件事的两面。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Anthropic 公开表示已「非常接近」RSI 能力 | 「非常接近」是营销措辞还是内部评估，无量化指标 |
| RSI 指 AI 改进自身训练、引发能力加速的临界点 | RSI 定义本身在学界仍有争议，缺乏可测量标准 |
| 同日 Anthropic 确认 Claude Code 新增系统提示，禁止复刻现有游戏 | 限制游戏克隆是法律风险驱动还是能力担忧，官方未说明 |
| 用户报告 Opus 5.5 也在拦截逆向工程类任务 | 拦截逆向工程是否误伤正常开发，需看用户实测反馈 |
| 公司称正在「迭代以找到合适的平衡」 |  |

**📖 主编点评**

这条对你的 Agent 项目有直接含义：模型厂商正在系统提示层做价值对齐，你的 content-curator 如果调用 Claude，要预期某些任务会被静默拒绝。建议在 pipeline 里加一层「拒绝检测 + 备用模型切换」，这是工程上迟早要踩的坑。

📺 [打开原文](https://techcrunch.com/2026/11/02/anthropic-warns-that-its-very-close-to-rsi-capability-aka-self-building-ai/)

---

### 5. YC 的 Garry Tan 一年在 token 上花 20 万美元，自称得了「赛博精神病」

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Julie Bort_

Garry Tan 在播客里承认自己因为和 AI Agent 协作太兴奋，经常不怎么睡觉，一年 token 开销最高 20 万美元。这个数字比任何 benchmark 都更能说明重度 Agent 用户的真实成本结构。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Garry Tan 称年度 token 支出最高达 20 万美元 | 20 万美元是个人支出还是含 YC 团队，口径不明 |
| 他自嘲患有「cyber psychosis」，睡眠很少 | 这种使用强度是否可复制到普通开发者，存疑 |
| 说法出自 Walter Isaacson 播客新一期 | 高 token 消耗能否转化为实际产出，无公开数据 |
| Tan 是 Y Combinator 现任掌门 | 「Agent 重度用户」是否成为新的人群分层，尚属观察 |
| 他把高支出归因于对 Agent 协作的兴奋 |  |

**📖 主编点评**

这条给你一个成本锚点：重度 Agent 用户的年支出在六位数美元量级。你做 content-curator 时应该反过来想——哪些环节值得烧 token（选题判断、长文摘要），哪些必须走便宜模型或规则（去重、抓取）。成本结构设计比模型选型更影响项目能不能长期跑。

📺 [打开原文](https://techcrunch.com/2026/11/02/y-combinators-garry-tan-uses-ai-agents-so-much-he-spends-up-to-200k-a-year-on-tokens/)

---

## 📋 备选阅读

- [Google 财报像极了当年的 Facebook，Stratechery 谈「Agent 这一手」](https://stratechery.com/2026/google-earnings-facebook-deja-vu-the-agent-play/) —— Ben Thompson 的框架值得读，把 Google 的激进和 Agent 战略串起来了。
  _Ben Thompson_
- [Gemini 4 Carbon 登顶 Artificial Analysis 智能指数 v5](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1) —— 模型排名变动，对选型有参考，但缺工程细节所以没上头条。
  _theHocineSaad_
- [纽约时报等多家媒体起诉 Brave 浏览器抓取内容](https://techcrunch.com/2026/11/02/new-york-times-and-other-outlets-sue-web-browser-brave-over-alleged-content-scraping/) —— 抓取的法律边界在收紧，做 content-curator 这类聚合工具要留意合规。
  _Rebecca Bellan_
- [42AI 出隐身模式，6250 万美元融资，做能「预测人类行为」的世界模型](https://techcrunch.com/2026/11/02/42ai-comes-out-of-stealth-with-62-5m-and-a-world-model-that-can-predict-human-behavior/) —— 世界模型赛道新玩家，宣称能预测行为，但缺技术细节，先观察。
  _Ram Iyer_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
