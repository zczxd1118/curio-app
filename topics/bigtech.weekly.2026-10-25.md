# Curio · 大厂 AI 动态 · 2026-10-25

> 今日 1 条头条 + 3 条备选

_今天最重要的两个信号：一是 AI 资本叙事开始松动——Anthropic 估值被传缩水 5000 亿美元、Firmus 30 亿美元 IPO 48 小时崩盘、数据中心股集体下挫，钱开始重新定价算力；二是工程侧出现真东西，Opus 5.5 agent 自主发现两个室温磁性半导体候选材料，这是 agent 从写代码走向做科研的第一个可验证样本。_

---

## 🌟 今日精选

### 3. OpenAI 宣布前沿模型不再用实时互联网训练，理由是"重大风险"

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Tim Fernholz_

OpenAI 表示将切断前沿模型与实时互联网的训练连接，官方给出的理由是 significant risks。时间点很微妙——几周前自家工程师还公开说这个方案行不通。这条对做 RAG 和 agent 的人影响直接：训练数据与推理时检索的边界被官方重新划了一次。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| OpenAI 官方表态，前沿模型训练不再接入实时互联网 | '实时互联网'的具体边界未定义，是否包含定期快照语料不明 |
| 官方理由是 significant risks | 是否只针对前沿模型、小模型是否同样处理，未说明 |
| 时间点在自家工程师公开质疑该方案数周之后 | 与数据授权、版权诉讼的关联程度未公开 |
| TechCrunch 10 月 23 日报道 | 对推理时联网检索（如 Search 产品）是否受影响，官方未回应 |

**📖 主编点评**

这条直接关系到你的 RAG 实践：训练侧关掉实时数据，意味着推理侧的检索质量权重更高。你项目里如果要做内容聚合，抓取与索引的时效性设计会比模型选型更关键，值得单独写一段设计说明放进 README。

📺 [打开原文](https://techcrunch.com/2026/10/23/openai-says-it-will-no-longer-train-its-ai-models-on-the-live-internet-citing-significant-risks/)

---

## 📋 备选阅读

- [Block 新语音模型听起来像真人，可在 MacBook M4 Max 本地跑](https://techcrunch.com/2026/10/24/blocks-new-voice-model-sounds-eerily-human/) —— 本地推理 + 拟真度是双卖点，对关注端侧部署的人是新事实，但缺少技术细节披露。
  _Ivan Mehta_
- [Agent 云创业公司 Daytona 估值达 10 亿美元，FirstMark 领投](https://techcrunch.com/2026/10/23/agent-cloud-startup-daytona-hits-1b-valuation-backed-by-firstmark-and-a-whos-who-of-angels/) —— '给每个 agent 一台自己的电脑'这个定位值得关注，Stripe、Datadog 创始人跟投，是 agent 基础设施层的信号。
  _Julie Bort_
- [宾州通过 AI 欺骗性广告法，要求 AI 生成广告加标注](https://www.theverge.com/ai-artificial-intelligence/1018187/pennsylvania-ai-deceptive-advertising-act) —— 州级立法落地，对做内容生成产品的人是合规前置信号，但短期不影响个人项目。
  _Terrence O’Brien_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
