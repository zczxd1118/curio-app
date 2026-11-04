# Curio · 大厂 AI 动态 · 2026-11-04

> 今日 2 条头条 + 3 条备选

_今天最值得看的两条信号：一是 Gemini 4 Carbon 在 Artificial Analysis 智能指数上登顶、同时 Anthropic 的 IPO 文件把"算力经济学"和"可能接近递归自我改进"写进风险披露，前沿模型竞赛已经进入"能力+资本"双线叙事；二是芯片股集体大跌、Intel 单日崩盘叠加 Oracle 发 200 亿美元债融资 AI 基建，市场开始给 AI 资本开支重新定价。工程侧则有一条极硬的料：有人把 32 位 RISC-V CPU 编译进 Qwen 3.5 4B 的权重里并跑起 DOOM。_

---

## 🌟 今日精选

### 1. Gemini 4 Carbon 登顶 Artificial Analysis 智能指数 v5，Google 称其幻觉率最低

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _theHocineSaad_

Google 上周发布的 Gemini 4 Carbon 在 Artificial Analysis Intelligence Index v5 上拿到第一，官方同时宣称它是前沿模型中最不容易产生幻觉的一个。HN 上 Gemini 4 Carbon 的发布帖拿到 1018 分，说明开发者社区确实在认真测。这不是一次常规迭代，而是 Google 在"能力榜"和"可靠性"两个维度同时抢话语权。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 4 Carbon 在 Artificial Analysis Intelligence Index v5 上排名第一 | "幻觉率最低"目前只有 Google 自报的 benchmark 支撑，缺少第三方复现 |
| Google 官方博客称其为"最不可能产生幻觉"的前沿模型 | 微弱领先 Opus 5.5 意味着榜单差距可能在噪声范围内，下一次更新就会翻转 |
| HN 发布帖 1018 分，Artificial Analysis 分析帖 338 分 | Carbon 与 Argon 的定位差异（通用 vs 机器人）尚未有官方清晰说明 |
| Tom's Hardware 报道其"以微弱优势超过 Claude Opus 5.5" | 实际 coding / agent 任务上的表现是否同步提升，还没有社区大规模实测 |
| 此前 Gemini 4 Argon 已发布并扩展到机器人方向 |  |

**📖 主编点评**

你如果正在给 content-curator 选模型，别只看榜单名次——先拿你自己的 20 条真实抓取任务跑一遍 Carbon 和 Opus 5.5 的对比，重点看结构化输出稳定性和长上下文里的幻觉。榜单第一不等于你的 pipeline 里第一。

📺 [打开原文](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)

---

### 5. Anthropic 的算力经济学在恶化：本该改善的毛利率反而变差

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Russell Brandom_

TechCrunch 指出，在 Anthropic 的算力毛利本该随规模改善的节点上，它反而在变差。结合同一天曝出的 IPO 文件把"可能接近递归自我改进（RSI）"写进风险披露，以及有研究机构称这是"对投资者轻信度的空前考验"，Anthropic 正处在能力叙事与商业现实的最紧张交叉点。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| TechCrunch 报道 Anthropic 的算力毛利在恶化而非改善 | 毛利恶化的具体数字未在报道中给出，需要看 S-1 原文 |
| Anthropic IPO 文件已公开，含收入增长与算力成本披露 | 把 RSI 写进风险披露是法律自保还是真实技术判断，无法从外部验证 |
| IPO 文件警告公司可能"即将"接近递归自我改进 | "最荒谬 IPO"是卖方观点，不代表定价结果 |
| 有研究机构公开称该 IPO 是"2026 年最荒谬的 IPO" | 算力成本恶化与模型能力提升之间的取舍策略尚不清晰 |
| IPO 采用双层股权结构，创始人保留控制权 |  |

**📖 主编点评**

这条值得你花 20 分钟读 S-1 原文里的成本结构段落——它是目前最诚实的"前沿模型公司到底怎么烧钱"的公开材料。对你写 content-curator 的商业化设想（哪怕只是简历里的一段）来说，比任何二手分析都有说服力。

---

## 📋 备选阅读

- [AMD Q3 2026 创历史最高单季营收 134 亿美元](https://www.theverge.com/tech/1026148/amd-earnings-q3-2026-data-center-pc) —— 数据中心业务驱动的纪录季度，与芯片股大跌形成有趣对照，但属于财报常规解读。
  _Stevie Bonifield_
- [Anthropic 在做 FlashProve：证明 AI 响应的模型身份](https://techcrunch.com/2026/11/03/anthropic-is-working-on-a-system-to-prove-ai-models-identity/) —— 让任何人验证一条响应确实来自它声称的模型，对 Agent 生态的信任层有意义，但还在早期。
  _Russell Brandom_
- [CrowdStrike 近 5 亿美元收购两家 AI 安全公司](https://techcrunch.com/2026/11/03/crowdstrike-to-shell-out-nearly-500m-for-2-ai-security-startups-as-the-market-for-securing-agents-takes-off/) —— "保护 Agent"正在成为一个独立市场，Fiddler AI 做 agent 可观测性，这个方向值得你留意。
  _Ram Iyer_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
