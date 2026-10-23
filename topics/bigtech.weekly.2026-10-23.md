# Curio · 大厂 AI 动态 · 2026-10-23

> 今日 2 条头条 + 3 条备选

_今天最硬的信号有两个：一是 OpenAI 传出以 1.25 万亿美元估值再融 300 亿美元、抢在 IPO 前落袋，AI 资本周期进入「自我加杠杆」阶段；二是 Google TPU 首次外销并跑进 Meta 数据中心，Nvidia 的算力垄断第一次出现真实裂缝。半导体侧，TSMC 开始要求设备商去中国稀土磁体，供应链脱钩从口号变成采购条款。_

---

## 🌟 今日精选

### 1. OpenAI 传以 1.25 万亿美元估值再融 300 亿美元，抢在 IPO 前锁定弹药

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _TechCrunch_

TechCrunch 报道 OpenAI 正在推进新一轮 300 亿美元融资，投前估值约 1.25 万亿美元。若成，它将成为史上估值最高的未上市公司，且时间点卡在 IPO 之前。这不是一次普通融资，而是把未来两年的算力与人才成本一次性前置——对下游所有依赖 OpenAI 定价的团队，意味着 API 价格战还会继续。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 融资规模约 300 亿美元，估值约 1.25 万亿美元，报道来自 TechCrunch | 1.25 万亿是投前还是投后估值，报道未完全锁定，实际稀释比例待确认 |
| 若落地将刷新未上市公司估值纪录，超过此前所有私募轮次 | 本轮是否含战略投资者（云厂商/主权基金）以及是否附带算力采购绑定，尚无细节 |
| 融资时点被明确描述为「IPO 之前」，即上市前的最后一轮私募 | IPO 时间表仍属传闻，2027 年上市只是市场推测 |
| 同期 Anthropic 的 S-1 文件已公开，两家头部实验室同时进入资本公开化阶段 | 300 亿中有多少用于算力 capex、多少用于人才与并购，没有拆分 |

**📖 主编点评**

你不需要关心估值本身，但要关心它对你手上项目的传导：融资落地后 OpenAI 大概率继续压 API 单价换份额，你的 content-curator 如果依赖模型调用，现在就该把模型层做成可替换的抽象（一个 provider 接口 + 配置切换），别把 prompt 和 SDK 细节焊死在某一家上。

📺 [打开原文](https://techcrunch.com/2026/10/22/openai-working-on-new-30b-raise-at-1-25t-valuation-ahead-of-ipo/)

---

### 4. 1Password 让 AI Agent 代你登录，但全程看不到你的密码

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _TechCrunch_

1Password 上线新能力：Agent 可以代替用户登录账户，而凭证始终不暴露给模型。这是 Agent 落地绕不开的一环——过去所有「让 Agent 帮你操作网页」的方案，卡点都在凭据托管。现在密码管理器主动站出来做这层信任中介，等于给 Agent 生态补上了缺失的一块基础设施。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 1Password 发布让 AI Agent 代为登录的功能 | 具体鉴权协议（是否基于 OAuth 委托 / 短期令牌）未公开技术细节 |
| Agent 在登录过程中不接触明文密码，凭证由 1Password 侧托管 | 支持哪些 Agent 框架、是否开放 API 给第三方，尚不明确 |
| 该能力面向用户的个人账户登录场景 | 安全边界依赖 1Password 自身的信任模型，一旦被攻破影响面很大 |
| 此前 Agent 自动化普遍需要把凭证交给模型或本地脚本 | 定价与是否仅限企业版未知 |

**📖 主编点评**

这条直接对应你在做的 content-curator：如果后续要让它自动抓取需要登录的站点，别自己存 cookie 或明文 token。先去看 1Password 这套委托模型的设计思路（短期凭证 + 权限范围收窄），哪怕不用它的产品，这个模式也值得抄进你的 Agent 架构里。

📺 [打开原文](https://techcrunch.com/2026/10/22/1password-launches-a-way-for-ai-agents-to-log-in-on-your-behalf-without-seeing-your-password/)

---

## 📋 备选阅读

- [Left alone with nothing to do, AI agents started playing](https://techcrunch.com/2026/10/22/left-alone-with-nothing-to-do-ai-agents-started-playing/) —— MIT 把 13 个 AI 扔到虚拟荒岛，它们自己发明游戏、悼念丢失的戒指，是本周最有意思的 Agent 行为观察，但偏趣味。
  _TechCrunch_
- [Canva's first AI image model plans designs before generating them](https://www.theverge.com/ai-artificial-intelligence/1017151/canva-craft-in-house-ai-model) —— Canva Craft 用两阶段架构先规划再生成，思路和纯扩散模型不同，但属于产品发布，工程细节披露有限。
  _The Verge_
- [Uber puts all 30,000 employees on ChatGPT Work](https://techcrunch.com/2026/10/22/uber-puts-all-30000-employees-on-chatgpt-work/) —— 3 万人全员上 ChatGPT Work，是企业级 Agent 落地的规模样本，但报道只有结论没有部署细节，参考价值打折。
  _TechCrunch_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
