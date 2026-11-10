# Curio · 大厂 AI 动态 · 2026-11-10

> 今日 2 条头条 + 6 条备选

_今天只有一个真正的信号：Nvidia 的 Jensen Huang 丑闻从八卦升级成公司治理与监管事件——董事会立案、国会传唤、集体诉讼、股价跌超 4%，同时 Anthropic 一边发新模型一边推进 IPO。AI 资本叙事正在被两件事同时拉扯：算力军备竞赛（Anthropic 花 34 亿美元买燃气轮机）和信任危机。_

---

## 🌟 今日精选

### 1. Jensen Huang 承认与疑似中国间谍有私情，Nvidia 董事会立案、国会传唤、集体诉讼三线齐发

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _Ben Thompson_

Huang 在致员工信中承认与 Megaspeed 高管 Alice Huang 的关系，Nvidia 董事会随即成立独立委员会调查，美国众议院中共问题特别委员会已传唤他作证，律所集体诉讼紧随其后，股价单日跌超 4%。Ben Thompson 的判断是：他大概能保住职位，但影响力再也回不到从前。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Huang 已向全体员工发信承认私情并道歉，董事会声明仍表示信任其领导 | 董事会"仍信任管理层"的表态能否撑过国会听证，目前无法判断 |
| 众议院 Select Committee on the CCP 已正式传唤 Huang 出席作证 | 集体诉讼的核心争点可能是公司此前声明是否构成误导性披露，尚未定论 |
| 至少一家律所已就证券欺诈提起集体诉讼，多家律所在跟进调查 | 此事对 Nvidia 游说放宽对华芯片出口的实际影响有多大，仍是推测 |
| Nvidia 股价在董事会宣布调查后单日下跌超过 4% | Huang 是否会主动卸任或转任董事长，目前没有任何实质信号 |
| Culper Research 早在六个月前就发布做空报告质疑 Huang 与该高管的关系 |  |
| Huang 已临时退出 ElevenLabs Summit 与一场 Anthropic 活动 |  |

**📖 主编点评**

别把这条当八卦看。Nvidia 是当前 AI 基建的定价锚，CEO 治理风险会直接传导到算力采购节奏和出口政策。你如果关注 AI 产业链，接下来两周盯三件事：国会听证日期、董事会调查结论、以及 Q4 财报电话会上管理层被追问的密度。

📺 [打开原文](https://stratechery.com/2026/jensen-huangs-affair-the-culper-report-huangs-righteousness/)

---

### 2. Anthropic 花 34 亿美元买下 1.7GW 燃气轮机，插队六年等待名单抢电

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _Tim De Chant_

Anthropic 接手了 OnePWR Solutions 从 Caterpillar 的既有订单，一次性锁定 1.7GW 燃气发电容量，代价 34 亿美元。设备交付周期已经长到让 AI 公司不得不"买别人的排队位置"，这是算力竞赛从买 GPU 转向买电力的明确信号。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 交易金额 34 亿美元，锁定 1.7GW 燃气发电容量 | 这笔交易是否会在天然气价格波动时变成"买家懊悔"，取决于合同条款，目前未知 |
| 方式是接手 OnePWR Solutions 已有的 Caterpillar 涡轮机订单，绕过六年等待名单 | 1.7GW 对应的实际可用算力规模没有披露，无法换算成 GPU 数量 |
| Anthropic 同期被报道将在本周确定 IPO 估值区间 | Anthropic 在 IPO 前夜大额资本开支，是展示增长还是暴露成本结构，两种解读都成立 |
| Anthropic 昨日发布 Claude Fable 5.2 与 Mythos 5.2 两个新模型 | 自建发电是否会成为头部 AI 公司的标配，还要看监管与并网审批速度 |
| Fervo 地热公司同期披露 120 亿美元订单储备，同样指向数据中心供电缺口 |  |

**📖 主编点评**

这条对你做 Agent 项目的直接含义是：推理成本的中长期曲线取决于电力而不是芯片。如果你在给 content-curator 做成本模型，别只算 token 单价，把"供给紧张导致的限流与排队"当成一个真实变量写进设计里。

📺 [打开原文](https://techcrunch.com/2026/11/09/anthropic-joins-ais-natural-gas-frenzy-buys-3-4b-worth-of-turbines/)

---

## 📋 备选阅读

- [Anthropic 发布 Claude Fable 5.2 与 Mythos 5.2，主打"艰巨"技术任务](https://www.theverge.com/ai-artificial-intelligence/1030005/anthropic-claude-fable-mythos-5-2) —— 官方称在编码、推理、视觉上有提升，但没给可复现 benchmark，先记一笔等实测。
  _The Verge_
- [Meta 发布 Muse Ember，每百万输入 token 仅 10 美分](https://techcrunch.com/2026/11/09/meta-releases-muse-ember-a-new-lightweight-model-for-agent-execution/) —— 专为 Agent 执行设计的轻量模型，价格显著低于 Haiku 和 Luna，做 Agent 的值得关注定价。
  _TechCrunch_
- [Claude Code 配置文件在 GitHub 上泄露数千条密钥](https://arstechnica.com/ai/2026/11/claude-code-settings-files-expose-thousands-of-secrets-on-github/) —— "Do not ask again" 的权限提示导致密码和 API key 被提交，你本地跑 Claude Code 前该看一眼 .gitignore。
  _Ars Technica_
- [Google Gemini 把个人 Drive 文件和邮件路由给人工标注员](https://github.com/thisisme6598/gemini_files/) —— HN 620 分，配合此前"订阅用户聊天记录也被训练"的讨论，企业数据合规风险在累积。
  _Hacker News_
- [Anthropic 据报推进 IPO，本周确定估值区间](https://techcrunch.com/2026/11/09/anthropic-reportedly-plans-to-move-forward-with-ipo-plans/) —— WSJ 消息，配合 34 亿美元买电动作看，是"增长叙事 + 成本压力"的组合拳。
  _TechCrunch_
- [Apple 推出 50 美元 Intelligence Usage Packs 扩展部分 AI 功能额度](https://www.theverge.com/tech/1030084/apple-intelligence-usage-packs-ai-features-creator-studio-logic-pro) —— AI 功能开始按量收费，Logic Pro 已上线"Buy More Usage"，端侧 AI 的商业模式在试水。
  _The Verge_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
