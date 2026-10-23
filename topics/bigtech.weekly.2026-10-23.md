# Curio · 大厂 AI 动态 · 2026-10-23

> 今日 2 条头条 + 4 条备选

_今天最值得盯的两条线：一是资本端开始给 AI 叙事重新定价——Anthropic 估值从高点回落 500B、Firmus 的 300 亿美元 IPO 两天内崩掉、亚洲芯片股与数据中心股同步下挫，而 OpenAI 反手在 IPO 前谈 1.25 万亿美元估值的新一轮 300 亿美元融资；二是算力供给端出现结构性位移——Google TPU 首次外销并跑进 Meta 机房。工程侧则有一个你会直接用到的东西：1Password 让 Agent 代登录而不暴露密码。_

---

## 🌟 今日精选

### 1. OpenAI 在 IPO 前谈新一轮 300 亿美元融资，估值 1.25 万亿美元，将成史上最贵私营公司

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _TechCrunch_

同一周里，Anthropic 的估值被市场砍掉 5000 亿美元、Firmus 的 300 亿美元 IPO 两天崩盘，OpenAI 却在推进 300 亿美元新融资、喊出 1.25 万亿美元估值并筹备 IPO。这不是矛盾，是分层：头部模型公司拿到了"最后赢家"的定价权，二线算力和二线模型开始被折价。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| TechCrunch 报道 OpenAI 正推进约 300 亿美元新融资，投前估值约 1.25 万亿美元 | 1.25 万亿美元是投前还是投后、是否有对赌或结构性条款，目前未披露 |
| 若成交，将刷新史上最高估值私营公司纪录 | 这轮融资是否包含算力/云资源的实物出资（类似此前与云厂商的循环交易），尚不清楚 |
| 融资时点在 IPO 之前，属于上市前最后一轮私募 | "IPO 前最后一轮"的说法来自媒体，OpenAI 官方未确认时间表 |
| 同期 Anthropic 估值从高点回落约 5000 亿美元（Telegraph 报道） | 高估值能否在公开市场被接住，取决于 2027 年的收入曲线，现在无法验证 |
| 数据中心公司 Firmus 的 300 亿美元 IPO 在 48 小时内告吹（Bloomberg） |  |

**📖 主编点评**

别把这条当财经八卦看。它真正告诉你的是：模型层的资本正在向 2-3 家收敛，其余玩家会越来越难拿到便宜算力。如果你在做 Agent 项目，选型时优先押注能长期活下去的模型供应商，别把架构绑在一个融资前景不明的 API 上——抽象一层 provider 接口，成本很低，回报很高。

📺 [打开原文](https://techcrunch.com/2026/10/22/openai-working-on-new-30b-raise-at-1-25t-valuation-ahead-of-ipo/)

---

### 3. 1Password 上线 Agent 代登录：Agent 能登你的账号，但看不到你的密码

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _TechCrunch_

Agent 落地最脏的一环一直是凭证：要么把密码明文塞进 prompt，要么手工贴 cookie。1Password 这次把凭证从 Agent 的上下文里彻底拿走了——Agent 发起登录请求，密码库完成认证，Agent 只拿到会话。这是 Agent 基础设施开始成型的信号。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 1Password 发布新功能，允许 AI Agent 代表用户登录账户 | 具体协议是 OAuth 代理、还是自研的凭证注入通道，官方细节有限 |
| Agent 全程不接触用户的明文密码或私钥 | 第三方 Agent 框架（Claude Code、Cursor 等）的接入方式与 SDK 尚未明确 |
| 凭证由 1Password 侧保管并完成认证流程 | 被登录站点的兼容性范围未知，长尾站点大概率不支持 |
| 面向个人账户场景推出 | 一旦 Agent 被 prompt injection 劫持，授权边界能收多紧，是核心风险点 |

**📖 主编点评**

你在做 content-curator，迟早要让它自动登录某些站点抓数据或发内容。这条给了你一个正确的架构方向：凭证永远不进 LLM 上下文，Agent 只持有"能力"不持有"秘密"。哪怕不用 1Password，也照这个模式设计——把登录封装成一个独立工具，Agent 调用它，返回值里只有会话句柄。

📺 [打开原文](https://techcrunch.com/2026/10/22/1password-launches-a-way-for-ai-agents-to-log-in-on-your-behalf-without-seeing-your-password/)

---

## 📋 备选阅读

- [Uber puts all 30,000 employees on ChatGPT Work](https://techcrunch.com/2026/10/22/uber-puts-all-30000-employees-on-chatgpt-work/) —— 从小组试点扩到全公司 3 万人，是 Agent 类产品最大规模的企业级铺开案例之一。缺具体使用数据，故未上头条。
  _TechCrunch_
- [Left alone with nothing to do, AI agents started playing](https://techcrunch.com/2026/10/22/left-alone-with-nothing-to-do-ai-agents-started-playing/) —— MIT 把 13 个 Agent 扔到虚拟岛上，它们自己发明游戏、悼念丢失的戒指。多 Agent 涌现行为的有趣观察，深度有限。
  _TechCrunch_
- [Arc browser sunsets December 22 as The Browser Company doubles down on Dia](https://techcrunch.com/2026/10/22/arc-browser-sunsets-december-22-as-the-browser-company-doubles-down-on-dia/) —— Arc 12 月 22 日停止维护，公司全面转向 Dia。一个被极客热爱但没做成大众产品的典型样本。
  _TechCrunch_
- [An Interview with Craig Moffett About SpaceX and Bubbles](https://stratechery.com/2026/an-interview-with-craig-moffett-about-spacex-and-bubbles/) —— Ben Thompson 对话 Craig Moffett，把 dot-com 泡沫的经验套到今天的 AI 资本结构上。契合你的访谈偏好，但与头条 1/5 主题重叠。
  _Stratechery_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
