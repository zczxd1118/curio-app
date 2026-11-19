# Curio · 金融 · 2026-11-19

> 今日 1 条头条 + 2 条备选

_今天最重要的信号有两个：一是 Nvidia 在黄仁勋辞职后首次交出季报，营收 1158 亿美元、利润依旧强劲，但董事会明确不打算让黄回归，公司进入「后黄仁勋时代」的过渡期；二是 Anthropic 以每股 83 美元、1.5 万亿美元估值完成 IPO 定价，AI 一级市场的泡沫争论被推到台前。对做 Agent 的你来说，今天还有一条值得细读的工程实践：用三块二手 V100 跑出 100 tok/s 的家庭实验室方案，成本只要 1042 美元。_

---

## 🌟 今日精选

### 5. 美联储开始担心 AI Agent 会触发银行挤兑，Citi 等大行已对 Agent 操作免责

**[金融]** · ⭐⭐⭐⭐ · _Gizmodo_

美联储内部讨论文件开始关注一个新型系统性风险：如果大量用户把理财决策交给 AI Agent，而 Agent 在恐慌信号下同步撤资，可能形成比人工更快、更同步的银行挤兑。与此同时，Citi 等大行已在条款中写明「使用 AI Agent 操作的客户自行承担被黑损失」。Agent 进入金融场景，责任边界正在被重新划线。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 美联储内部讨论文件将「AI Agent 同步撤资」列为潜在金融稳定风险 | 美联储是否会把 Agent 挤兑纳入正式监管框架，目前只是讨论阶段 |
| Citi 是最新一家在条款中声明「客户使用 AI Agent 操作风险自负」的大型银行 | 「同步撤资」的触发阈值和传播速度没有实证数据，属于情景推演 |
| 多家银行已对个人理财类 AI Agent 的接入采取限制或免责立场 | 银行免责条款在司法上是否站得住，尚无判例 |
| 讨论背景是 Agent 在支付、转账、投资指令上的自动化程度快速上升 | Agent 开发者（包括个人项目）在什么情况下会被认定为「金融业务主体」，监管未明确 |

**📖 主编点评**

这条对你做 content-curator 是提醒而非威胁：只要你的 Agent 不碰支付和交易指令，就不在监管射程内。但如果你以后想给 Agent 加「自动订阅付费内容」这类功能，先看清楚 Stripe 和银行的 Agent 条款——现在多数平台把「Agent 发起的交易」默认归为持卡人本人操作，出了事你自己扛。

📺 [打开原文](https://gizmodo.com/the-fed-is-worried-ai-agents-could-trigger-a-bank-run-2000840566)

---

## 📋 备选阅读

- [Oracle 申请发行 200 亿美元股票和债券，为 AI 基建融资](https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html) —— 11 月 2 日的融资动作，说明 AI 基建的钱正从经营现金流转向资本市场，是「AI 资本结构」主题的注脚。
  _CNBC_
- [arXiv：Vibe-Trading——面向 Agent 原生交易的框架](https://arxiv.org/abs/2611.24845) —— 11 月 19 日新论文，把「Vibe Coding」范式搬到交易 Agent 上，和你做 Agent 项目的思路同源，但偏学术、无代码。
  _arXiv_

---

## 💬 觉得 金融 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
