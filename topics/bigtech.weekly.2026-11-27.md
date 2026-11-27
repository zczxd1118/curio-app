# Curio · 大厂 AI 动态 · 2026-11-27

> 今日 1 条头条 + 4 条备选

_今天最重要的信号有两个。一是 Nvidia 的治理危机已经从八卦升级为信用事件：S&P 考虑下调评级、SEC 查会计问题、东南亚出货暂停，黄仁勋被董事会请回 CEO 反而加深了外界对董事会独立性的怀疑。二是 Anthropic 上市后股价跌破 83 美元发行价，AI 资产的定价逻辑正在被重新校准。这两件事叠加，意味着「算力无限增长」的叙事第一次出现了裂缝。_

---

## 🌟 今日精选

### 3. Gemini 4 Neon 发布并登顶 Models Engineering Index，Google 一个月内连发三个 4 系模型

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Google Blog / HN_

Google 在 11 月 18 日发布 Gemini 4 Neon，随即在 Models Engineering Index 上排名第一，被社区评价为 Opus 5.5 的直接竞品。值得注意的是节奏：Carbon（10 月底）、Hydrogen（11 月 12 日）、Neon（11 月 18 日），三周内三个 4 系模型。这种发布密度说明 Google 已经把模型迭代压缩到以周为单位，而不是以季度。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 4 Neon 于 11 月 18 日发布，官方博客同步上线 | Neon 的「第一」来自第三方 index，实际 coding / agent 任务表现需独立复现 |
| Neon 在 Models Engineering Index 上排名第一 | 三周三个版本的命名体系（Carbon/Hydrogen/Neon）是否对应不同规模或不同用途，官方未清晰说明 |
| Gemini 4 Carbon 于 10 月 28 日发布，曾在 Artificial Analysis Intelligence Index v5 上排名第一 | 发布密度高是否意味着单版本稳定性下降，目前缺少长周期故障率数据 |
| Gemini 4 Hydrogen 于 11 月 12 日发布，同时上线 Antigravity 平台的 Orchestrator 功能 | Antigravity Orchestrator 与 Neon 的组合能否真正支撑多 Agent 工作流，只有 demo 级证据 |
| Google 同期发布 Gemini Decisions API 与 Gemini Omni 1.2 Flash | Google 内部员工工会化与学校 AI 争议是否会影响产品路线，尚不明朗 |
| DeepMind 发布 AlphaProof Code 与 Genie 4 |  |

**📖 主编点评**

你在做 Agent 项目，Neon + Antigravity Orchestrator 这个组合值得花半天实测，尤其是多 Agent 编排部分——这是你 content-curator 里「子 Agent」设计的直接参照。但别急着迁移，先跑你自己的评测集。另外提醒：模型发布密度这么高，你的 digest 里「大模型评测与发布动态」这一类应该开始做去重和归并，否则每周都会被同类新闻淹没。

📺 [打开原文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

---

## 📋 备选阅读

- [OpenAI 合并 Chat 与 Work，重度用户会更早触达用量上限](https://techcrunch.com/2026/11/25/openai-says-heavy-chatgpt-users-may-hit-limits-sooner-as-it-merges-chat-and-work/) —— 统一用量计量意味着重度用户成本上升。对做 Agent 项目的人是个提醒：依赖单一 API 的额度策略要重新算。
  _TechCrunch_
- [FCC 批准 SpaceX 在太空部署 AI 数据中心的计划](https://techcrunch.com/2026/11/25/fcc-approves-spacex-plan-to-put-ai-data-centers-in-space/) —— FCC 驳回了科研威胁等反对意见，理由是超出其监管权限。方向性事件，但离落地很远，先记一笔。
  _TechCrunch_
- [Dario Amodei 回应「向 AI 交出人类控制权」的指控，称其「荒谬」](https://techcrunch.com/2026/11/25/anthropics-dario-amodei-calls-accusations-of-surrendering-human-control-to-ai-absurd/) —— 符合你「AI 名人访谈/表态」的偏好，但这是回应式表态而非深度对话，密度一般，放备选。
  _TechCrunch_
- [1Password 承认内部系统被入侵，但称用户密码安全](https://techcrunch.com/2026/11/25/1password-said-hackers-broke-into-its-internal-systems-but-customer-passwords-are-safe/) —— 攻击者拿到员工企业账号和部分客户信息。如果你用 1Password 管项目密钥，值得看一眼官方说明。
  _TechCrunch_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
