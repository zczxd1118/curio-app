# Curio · 大厂 AI 动态 · 2026-10-25

> 今日 1 条头条 + 3 条备选

_今天最值得看的两条信号：一是 OpenAI 宣布前沿模型不再吃「活的互联网」数据，训练数据供应链开始主动收缩；二是 AI 资本侧明显降温——Anthropic 估值被传缩水 5000 亿美元、数据中心类 IPO 接连折戟、10 年期美债收益率破 5.3%。算力与半导体侧则是另一条线：中国用 DUV 多重曝光硬撑 5nm 级，代价是良率与成本。_

---

## 🌟 今日精选

### 1. OpenAI 停止用「活的互联网」训练前沿模型，理由是「重大风险」

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _TechCrunch_

OpenAI 公开表示将不再让前沿模型直接抓取实时互联网数据训练，理由是存在「significant risks」。时间点很微妙——几周前自家工程师还公开说这条路走不通。这不是技术细节调整，而是训练数据供应链的一次主动收缩：实时网页既是最大的语料池，也是最大的投毒面和合规雷区。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| OpenAI 官方表态：前沿模型不再以实时互联网数据为训练来源 | 「不再训练」的具体边界未明：是彻底断网，还是仅限前沿模型、是否含 RL 环境 |
| 给出的理由是「significant risks」，未逐条列明具体风险类型 | 是否与近期网页投毒、版权诉讼或监管压力直接相关，官方未确认 |
| 该决定发生在一位 OpenAI 工程师公开质疑该方案可行性数周之后 | 对模型时效性的实际影响要等下一代模型评测才能验证 |
| 此前业界普遍做法是持续抓取实时网页以保持模型时效性 | 其他厂商（Anthropic、Google）是否跟进，目前无信号 |

**📖 主编点评**

你做 content-curator 这类依赖实时抓取的 Agent，这条是反向提醒：上游模型厂商开始不信任开放网页，你自己的数据管道就更该做来源白名单和内容校验。别把「能抓到」当成「能信」。

📺 [打开原文](https://techcrunch.com/2026/10/23/openai-says-it-will-no-longer-train-its-ai-models-on-the-live-internet-citing-significant-risks/)

---

## 📋 备选阅读

- [Gemini 4 Argon 发布，配套机器人版本与 StarCraft 实测](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) —— 1700+ 分的大发布，但已过去三周多，且摘要信息薄，放备选等评测沉淀。
  _Hacker News_
- [Block 新语音模型可在 MacBook M4 Max 本地运行](https://techcrunch.com/2026/10/24/blocks-new-voice-model-sounds-eerily-human/) —— 本地跑、听感接近真人，端侧语音这条线值得跟，但缺具体参数。
  _TechCrunch_
- [Daytona 估值达 10 亿美元：给每个 Agent 一台云上电脑](https://techcrunch.com/2026/10/23/agent-cloud-startup-daytona-hits-1b-valuation-backed-by-firstmark-and-a-whos-who-of-angels/) —— Agent 沙箱基础设施的融资信号，Stripe、Datadog 创始人跟投，方向值得记。
  _TechCrunch_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
