# Curio · 大厂 AI 动态 · 2026-11-11

> 今日 2 条头条 + 5 条备选

_今天真正的大信号只有一个：Nvidia 的治理危机已经从八卦升级为国家级风险——Jensen Huang 承认与疑似中方情报人员的关系，国会传唤、集体诉讼、FBI 介入同时发生，而 Stratechery 指出真正的风险在治理而非国安。第二个信号是 Anthropic IPO 定价 1.4T 估值，7 位创始人各套现 2.5 亿美元，同时纽约 AI 安全法生效——AI 头部公司第一次同时被资本市场和监管双向夹击。_

---

## 🌟 今日精选

### 1. Jensen Huang 危机升级：国会传唤、集体诉讼、FBI 介入，Ben Thompson 判断真正风险在治理而非国安

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _Ben Thompson_

Huang 承认与 Megaspeed 董事总经理的关系后，事件在 48 小时内连跳三级：国会 CCP 特别委员会传唤、律所发起证券欺诈集体诉讼、特朗普称 FBI 已介入。Stratechery 的 Ben Thompson 给出与主流叙事不同的判断——对 Huang 最致命的不是国安审查，而是董事会治理结构，他的影响力「永远不会和以前一样」。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Huang 已公开承认与 Megaspeed 董事总经理 Alice Huang 存在恋爱关系，对方被指为中方情报资产 | Huang 是否会辞去 CEO 或仅失去董事长职位，目前无任何官方信号 |
| 国会 CCP 特别委员会已传唤 Huang 出席作证 | Nvidia 董事会调查的结论与时间表未知，可能拖到 2027 年 |
| 至少一家律所已就证券欺诈发起集体诉讼，多家律所在跟进调查 | 对华 GPU 出口政策是否会因此收紧，白宫尚未表态 |
| 特朗普公开表示 FBI 正在调查此事 | Nvidia 股价的下跌是情绪性还是结构性重估，需看下季度财报 |
| 报道称 Alice Huang 三年间协助约 24 万颗 H100/H200 流入中国，涉资 75 亿美元 | Megaspeed 调查被叫停是否与 Huang 干预有关，纽约时报的报道尚未被官方证实 |

**📖 主编点评**

这条你该读 Stratechery 原文而不是新闻标题——Ben Thompson 的框架是「治理风险 > 国安风险」，这决定了 Nvidia 未来 6 个月的估值逻辑。如果你在关注 AI 算力链的任何标的或供应链判断，把「Huang 是否留任」当成一个需要持续跟踪的变量，而不是一次性新闻。

📺 [打开原文](https://stratechery.com/2026/the-jensen-huang-story-gets-worse-washington-vs-new-york-silicon-valley/)

---

### 3. Anthropic 发布 Claude Meetings：会议中实时起草计划、画时间线、调取工作 App 数据

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Aisha Malik_

Claude Meetings 的定位不是「会议纪要工具」，而是会议进行中就介入——参与者说话时 Claude 同步起草讨论中的计划、在白板上画时间线、在会议聊天里回答问题，并能调用已连接的工作 App 取数据。这是把 Agent 从「会后总结」推进到「会中协作」的一步，产品形态上更接近一个参会者而不是记录员。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Anthropic 正式发布 Claude Meetings 功能 | 实时介入的延迟和准确率没有公开数据，实际体验待验证 |
| 支持会议中实时起草计划、白板时间线、会议聊天问答 | 与 Zoom/Teams/Meet 的集成深度未知 |
| 可访问已连接的工作类 App 获取信息 | 是否会记录并存储会议内容，隐私边界未说明 |
| 由 TechCrunch 于 11 月 10 日报道 | 定价是否包含在现有订阅内，报道未提及 |
|  | 对企业 IT 采购的影响需观察 1-2 个季度 |

**📖 主编点评**

你做 Agent 项目时值得拆解这个产品的一个设计决策：Claude 在会议中「主动产出」而不是「被动等待提问」。这和你 content-curator 里「主动筛选 vs 被动检索」是同一类问题——主动性的边界在哪，什么时候该插话。可以去看官方 demo 里它什么时候选择不说话。

📺 [打开原文](https://techcrunch.com/2026/11/10/anthropic-launches-claude-meetings-to-turn-workplace-discussions-into-plans-and-tasks/)

---

## 📋 备选阅读

- [AlphaProof Code](https://deepmind.google/blog/introducing-alphaproof-code/) —— DeepMind 把 AlphaProof 扩展到代码领域，HN 639 分。数学证明到代码的形式化迁移是硬核方向，但今天缺细节，等官方技术博客。
  _ilreb_
- [Google 发布两款新专用 TPU，覆盖机密训练与大内存场景](https://techcrunch.com/2026/11/10/google-broadens-its-ai-hardware-portfolio-with-two-new-specialized-chips/) —— TPU 产品线细分到「机密模型训练」和「更大内存」，说明 Google 在抢企业合规训练场景。硬件参数未披露，暂列备选。
  _Ram Iyer_
- [Google Gemini 把用户 Drive 文件和邮件路由给人工标注员](https://github.com/thisisme6598/gemini_files/) —— HN 720 分，GitHub 仓库形式爆料。如果属实是重大隐私问题，但目前是单方证据，需要等 Google 回应再判断。
  _gf74918_
- [纽约 AI 安全法生效，OpenAI 与 Anthropic 面临注册与事故报告义务](https://techcrunch.com/2026/11/10/openai-anthropic-face-new-oversight-as-new-yorks-ai-safety-law-takes-effect/) —— 首个州级 AI 安全强制披露制度落地，违规罚款。对做 AI 产品的人是合规风向标，但今天只是生效日，细则影响待观察。
  _Rebecca Bellan_
- [Meta 的 AI Agent Muse 登陆 Apple Watch 与 Wear OS](https://techcrunch.com/2026/11/10/metas-ai-agent-muse-lands-on-apple-watch-and-wear-os/) —— 语音/文字/听写三种交互上手表。Agent 往可穿戴走的信号，但产品细节少，属于增量信息。
  _Aisha Malik_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
