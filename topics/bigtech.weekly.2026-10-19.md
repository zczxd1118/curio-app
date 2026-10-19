# Curio · 大厂 AI 动态 · 2026-10-19

> 今日 2 条头条 + 3 条备选

_今天最值得看的是两条互相咬合的线：一是 AI 资本叙事开始松动——Anthropic 估值被砍 5000 亿美元、Firmus 的 300 亿 IPO 48 小时崩盘、CoreWeave 创始人套现 33 亿，钱在往回收；二是模型侧仍在推进——Gemini 4 Argon 系列铺到机器人、星际争霸，Replit 把默认模型从 Anthropic 换成 OpenAI。工程侧则有一个很具体的信号：Claude Code 每轮对话先 gzip 压缩再送模型。_

---

## 🌟 今日精选

### 2. Gemini 4 Argon 连发：模型页、机器人版、星际争霸基准同日铺开

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _737max_

Google 在 DeepMind 模型页上线 Gemini 4 Argon，HN 两次登榜合计超 3100 分。随后几天内，Argon for Robotics 的开发者博客、用 Argon 打星际争霸的第三方基准站、以及 Artificial Analysis 的智能/性能/价格分析陆续出现。这是一次少见的「模型+具身+游戏智能体」同步发布。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 4 Argon 官方模型页已上线，HN 两条提交分别 1705 与 1466 分 | Argon 在真实 Agent 任务上的稳定性尚无独立复现 |
| Gemini 4 Argon for Robotics 发布在 Google 开发者博客 | 机器人版本是研究预览还是可商用 API，官方措辞含糊 |
| 第三方基准 starskirmish.com 上线 Argon 打星际争霸的评测 | 星际争霸成绩与通用推理能力的相关性存疑 |
| Artificial Analysis 已给出 Argon (High) 的智能、性能与价格分析 | 价格档位相对 3.x 的实际涨幅需看账单而非博客 |
| Gemini 3.8 的 TTS 版本在 9 月底已先行发布 |  |

**📖 主编点评**

你正在做 Agent 项目，Argon 的机器人版和游戏智能体基准值得各花 20 分钟看：前者说明 Google 在把模型往具身上压，后者是少见的「长程规划」公开测试场。但别急着切默认模型——先看 Artificial Analysis 的价格页，再拿你自己的 content-curator 跑一轮真实任务对比。

📺 [打开原文](https://deepmind.google/models/gemini/)

---

### 3. Replit 把默认模型从 Anthropic 换成 OpenAI，Claude 降为可选项

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Kirsten Korosec, Lucas Ropek, Rebecca Bellan_

Replit CEO Masad 在周末澄清，OpenAI 将取代 Anthropic 成为平台默认模型供应商，Claude 仍对客户开放但不再是默认。这是 vibe coding 赛道里第一个公开的「默认模型换供应商」案例，发生在 Anthropic 估值承压的同一周。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Replit CEO Masad 公开确认 OpenAI 成为默认模型供应商 | 切换是成本驱动、能力驱动还是商务条款驱动，CEO 未说明 |
| Claude 仍保留在平台上，客户可手动选择 | 存量项目的默认模型是否迁移、迁移窗口多长，未披露 |
| 消息由 TechCrunch 在 10 月 17 日报道 | 是否伴随定价调整，目前无信息 |
| Replit 是 vibe coding / 在线 IDE 赛道的主要玩家之一 | 其他 vibe coding 平台是否会跟进，值得观察 |

**📖 主编点评**

这条对你直接相关：如果你在 Replit 上有项目，默认模型变了意味着同样的 prompt 输出会变，回归测试要重跑。更重要的判断是——「默认模型」正在变成平台的商务筹码而非技术选择，你自建 Agent 时应该把模型层做成可替换的适配器，别把 prompt 写死在某家模型的行为上。

📺 [打开原文](https://techcrunch.com/2026/10/17/replit-is-no-longer-working-with-anthropic-ceo-says/)

---

## 📋 备选阅读

- [Anthropic 承诺将 5% 股份投入「公共利益基金」](https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares-to-a-public-benefit-fund/) —— 在估值缩水的同一周宣布捐股，时机耐人寻味，治理结构值得关注。
  _Anthony Ha_
- [Anthropic 给外部 AI 监督机构「准员工级」访问权限](https://arstechnica.com/ai/2026/10/anthropic-gives-outside-ai-watchdog-employee-like-access/) —— 外部监督方可未经批准发布结论，是 AI 治理里少见的实质让步。
  _Cristina Criddle, Financial Times_
- [Disney 同意接收 Character.AI 大部分员工](https://techcrunch.com/2026/10/18/disney-agrees-to-hire-the-majority-of-character-ais-workforce/) —— 以 stalking horse 竞标形式进行，Character.AI 的结局基本确定，AI 陪伴赛道洗牌。
  _Anthony Ha_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
