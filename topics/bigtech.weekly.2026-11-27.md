# Curio · 大厂 AI 动态 · 2026-11-27

> 今日 1 条头条 + 3 条备选

_今天最重要的信号有两个：一是 Nvidia 的治理危机从八卦升级成信用事件——S&P 考虑下调评级、董事会独立性被质疑、对东南亚出货暂停，Jensen Huang 回归 CEO 反而成了风险源；二是 Anthropic 上市后股价跌破 83 美元发行价，1.5T 估值叙事开始松动。AI 资本周期的第一次真实回调，可能就从这两条开始。_

---

## 🌟 今日精选

### 3. Gemini 4 Neon 发布并登顶 Models Engineering Index，Google 一个月内连发三代 Gemini 4

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _yigitdemirag_

Google 在 10 月底到 11 月中连续发布 Gemini 4 Carbon、Hydrogen、Neon 三个版本，Neon 上线即登顶 Models Engineering Index，社区评价其为 Opus 5.5 的正面竞争者。这种发布节奏本身就是一个信号：模型迭代周期已经压缩到以周计。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 4 Neon 官方博客发布，HN 1071 分 | Models Engineering Index 是社区榜单，权重和评测方法未公开，排名参考价值有限 |
| Neon 在 Models Engineering Index 上排名第一（第三方榜单 git-aarvin.github.io/mei） | Neon 相对 Opus 5.5 的实际工程差距，需要真实任务跑分而非榜单 |
| Gemini 4 Carbon 此前在 Artificial Analysis Intelligence Index v5 登顶 | 一个月三代命名（Carbon/Hydrogen/Neon）是否对应不同规模还是不同能力侧重，官方未说清 |
| Gemini 4 Hydrogen 与 Orchestrator 同步在 Antigravity 平台上线 | Orchestrator 是否意味着 Google 在做多 Agent 编排层，目前只有产品页信息 |
| Gemini Decisions API 已作为开发者工具单独发布 | Gemini 训练用户聊天记录的争议（HN 738 分帖）可能影响企业采用 |

**📖 主编点评**

你做 Agent 项目时，模型选型窗口正在变短——上个月的最优解这个月可能被替代。建议把 content-curator 的模型调用层做成可切换抽象，别硬编码单一 provider。另外 Neon 登顶的榜单值得你自己跑几个真实任务验证，社区榜单和你的实际 workload 往往不是一回事。

📺 [打开原文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

---

## 📋 备选阅读

- [OpenAI 合并 Chat 与 Work，重度用户将更早触及用量上限](https://techcrunch.com/2026/11/25/openai-says-heavy-chatgpt-users-may-hit-limits-sooner-as-it-merges-chat-and-work/) —— 统一用量计量对重度用户是实质变化，但细节未公布，等具体限额出来再深读。
  _Jagmeet Singh_
- [FCC 批准 SpaceX 在太空部署 AI 数据中心的计划](https://techcrunch.com/2026/11/25/fcc-approves-spacex-plan-to-put-ai-data-centers-in-space/) —— 监管放行是事实，但工程可行性存疑，属于长期叙事而非近期变量。
  _Kirsten Korosec_
- [Dario Amodei 回应「向 AI 交出人类控制权」指控：荒谬](https://techcrunch.com/2026/11/25/anthropics-dario-amodei-calls-accusations-of-surrendering-human-control-to-ai-absurd/) —— 符合你想多看 AI 名人访谈/表态的偏好，但只有单方回应，缺对话深度。
  _Rebecca Bellan_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
