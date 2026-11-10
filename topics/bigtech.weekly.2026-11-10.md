# Curio · 大厂 AI 动态 · 2026-11-10

> 今日 3 条头条 + 3 条备选

_今天最重要的信号有两个：一是 Nvidia 的 Jensen Huang 与疑似中国间谍的关系被本人承认，董事会启动独立调查、国会传唤、集体诉讼同时压上，Nvidia 股价单日跌超 4%，这不只是八卦，而是直接卡住 Nvidia 对华游说与出口管制的关键变量；二是 AI 资本面同步转向，Nasdaq 一周内跌入回调区间、2.5 万亿美元市值蒸发，Anthropic 却在这时推进 IPO。技术侧则有一条被低估的：Claude Code 的 settings 文件正在 GitHub 上批量泄露密钥。_

---

## 🌟 今日精选

### 1. Jensen Huang 承认与疑似中国间谍的婚外关系，Nvidia 董事会启动独立调查，Ben Thompson 判断「他能活下来，但影响力回不去了」

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _Ben Thompson_

Nvidia 董事会已成立独立委员会调查 CEO Jensen Huang 与 Megaspeed 董事 Alice Huang 的关系，Huang 本人向全员发信承认婚外情并道歉。国会中国问题特别委员会已传唤他作证，至少一家律所提起证券欺诈集体诉讼，Nvidia 股价单日跌超 4%。Ben Thompson 在 Stratechery 给出的判断很直接：他希望 Huang 挺过去，但 Huang 在华盛顿的话语权将永久性削弱。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Huang 向全体员工发信承认婚外关系并致歉，董事会成立独立委员会调查 | 调查结论是否触及出口管制合规，目前无任何官方定性 |
| 国会众议院中国问题特别委员会已传唤 Huang 出席作证 | Megaspeed 是否被认定为中国情报资产，美方尚未公开确认 |
| 至少一家律所提起证券欺诈集体诉讼，多家律所跟进调查 | Huang 是否会因此失去 CEO 职位——Stratechery 判断不会，但这是判断不是事实 |
| Nvidia 股价在调查消息后单日下跌超过 4% | 对华 GPU 出口政策会否因此收紧，取决于国会而非公司 |
| 做空机构 Culper Research 早在六个月前就质疑过这层关系 | 集体诉讼能否成立，要看 Nvidia 早期披露是否构成误导 |
| Huang 已临时退出 ElevenLabs Summit 与一场 Anthropic 活动 |  |

**📖 主编点评**

这条对你的实际含义不在八卦，而在算力供给的不确定性：Nvidia 对华政策一旦被国会接管，国内可获得的算力路径（云租赁、黑市 B300、二手 V100）价格与合规风险都会变。如果你在做需要调用海外模型的 Agent 项目，现在就该把「模型供应商可替换」当成架构约束写进设计，而不是等政策落地再改。

📺 [打开原文](https://stratechery.com/2026/jensen-huangs-affair-the-culper-report-huangs-righteousness/)

---

### 3. Claude Code 的 settings 文件正在 GitHub 上批量泄露 API key 和密码，起因是「Do not ask again」这个授权选项

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Kyle Orland_

Ars Technica 报道，大量开发者把 Claude Code 的本地 settings 文件连同密钥一起提交到了公开仓库，泄露内容包括 API key、数据库密码等。根因是 Claude Code 在请求权限时提供的「Do not ask again」选项——用户为了少点几次确认，把敏感路径的访问权限永久放开了，而这些配置随后被 git 带上了 GitHub。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| GitHub 上已发现数千条来自 Claude Code settings 文件的密钥泄露 | 受影响仓库的准确总数尚无权威统计 |
| 泄露内容包含 API key、密码等凭证 | Anthropic 是否会修改默认权限模型，官方未表态 |
| 直接诱因是「Do not ask again」权限选项被广泛使用 | 有多少泄露密钥已被实际利用，目前未知 |
| Ars Technica 已核实多起案例 |  |

**📖 主编点评**

你正在用 Claude Code 做 content-curator，这条是直接冲你来的。现在就去检查两件事：项目里有没有 .claude/settings*.json 被 git 跟踪，以及 .gitignore 有没有覆盖它。另外把「Do not ask again」改成对写操作永远确认——省下的点击次数，不值得用一次密钥泄露换。

📺 [打开原文](https://arstechnica.com/ai/2026/11/claude-code-settings-files-expose-thousands-of-secrets-on-github/)

---

### 5. Meta 发布 Muse Ember：专为 Agent 执行设计的轻量模型，输入价格 0.1 美元/百万 token

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Russell Brandom_

Meta 发布 Muse Ember，定位明确——不是通用对话模型，而是给 Agent 执行用的轻量模型。输入定价 0.1 美元/百万 token，TechCrunch 称其显著低于 Haiku 和 Luna 等前沿竞品。同一天 Anthropic 发布 Claude Fable 5.2 与 Mythos 5.2，主打编码、推理与视觉能力提升。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Muse Ember 输入定价 0.1 美元/百万 token | Ember 在真实 Agent 任务上的工具调用准确率，尚无第三方评测 |
| 官方定位为 Agent 执行场景的轻量模型 | 0.1 美元定价是否可持续，取决于 Meta 的补贴意愿 |
| 价格显著低于 Haiku、Luna 等竞品 | 与 Claude 新模型的对比结论，需要等独立 benchmark |
| 同日 Anthropic 发布 Claude Fable 5.2 与 Mythos 5.2 |  |

**📖 主编点评**

Agent 项目的成本结构正在被重写：当执行层模型降到 0.1 美元/百万 token，你的 content-curator 里那些「跑很多次、每次任务简单」的环节（分类、抽取、格式化）就该换模型了。建议做一次分层：规划用强模型，执行用 Ember 这类便宜模型，先量一下你现在的 token 花在哪一层。

📺 [打开原文](https://techcrunch.com/2026/11/09/meta-releases-muse-ember-a-new-lightweight-model-for-agent-execution/)

---

## 📋 备选阅读

- [Anthropic 推进 IPO，本周将确定估值区间](https://techcrunch.com/2026/11/09/anthropic-reportedly-plans-to-move-forward-with-ipo-plans/) —— WSJ 称本周定价，但 Michael Burry 和多家机构公开质疑 1.5 万亿美元估值能否成立——和上面的市场抛售是同一条线。
  _TechCrunch_
- [Anthropic 发布 Claude Fable 5.2 与 Mythos 5.2](https://www.theverge.com/ai-artificial-intelligence/1030005/anthropic-claude-fable-mythos-5-2) —— 官方称在编码、推理、视觉上有提升，但发布稿没给具体 benchmark 数字，等第三方评测再决定要不要迁移。
  _The Verge_
- [Google Gemini 把个人 Drive 文件和邮件路由给人工标注员](https://github.com/thisisme6598/gemini_files/) —— HN 736 分的另一条 Gemini 训练数据争议，和「订阅用户聊天记录也被训练」是同一问题的两面。
  _Hacker News_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
