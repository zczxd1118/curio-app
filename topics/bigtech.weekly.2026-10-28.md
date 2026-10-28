# Curio · 大厂 AI 动态 · 2026-10-28

> 今日 2 条头条 + 5 条备选

_今天最重的信号是 Anthropic 递交 IPO：半年 163 亿美元收入、传闻 2 万亿美元估值，同时招股书里写满了自我风险警告——AI 资本周期正式进入公开市场定价阶段。另一条是 Nvidia 掏钱给六家供应链厂商扩产、TSMC 传 CoWoS 涨价 20%，算力瓶颈从芯片转向封装与基板。_

---

## 🌟 今日精选

### 1. Anthropic 递交 IPO：半年 163 亿美元收入，但 Ben Thompson 说利润会被竞争吃光

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _Ben Thompson_

Anthropic 的 S-1 终于公开，2026 上半年收入 16.3 亿美元级别（$16.3B），并寻求数万亿美元估值。Ben Thompson 的判断比数字更值得看：核心业务确实赚钱，但算力成本与模型竞争会把利润压回去，公开市场投资者还要面对持续稀释。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Anthropic 已递交 IPO 文件，披露 2026 上半年收入 163 亿美元 | 2 万亿美元估值是否成立，取决于推理成本能否持续下降 |
| 招股书 93 页风险因素中明确写入模型可能被滥用、失控等极端风险 | 收入增速已出现放缓迹象，部分投资者下调了估值预期 |
| Amazon 通过债转股成为最大受益方之一，VC 账面收益以十亿美元计 | 招股书的风险披露更像合规动作，还是真实的产品路线约束 |
| Stratechery 判断核心业务当前盈利，但竞争可能吃掉全部利润 | 上市后 Anthropic 是否会因股东压力放松安全承诺 |
| 公司治理结构复杂，IPO 后谁真正掌权仍存疑 |  |

**📖 主编点评**

你不需要读完整 S-1，但该读 Stratechery 这篇——它把「收入好看 ≠ 生意好」讲透了。对你做 content-curator 的启示：模型能力不再是护城河，成本结构和分发渠道才是，选型时别只盯 benchmark。

📺 [打开原文](https://stratechery.com/2026/anthropic-s-1-the-cost-of-compute-who-is-paying/)

---

### 3. Google 发布 Genie 4 世界模型：场景一致性翻倍到 2 分钟，加入音频与实时操控

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _acossta_

Genie 4 把一致场景时长从 Genie 3 的 1 分钟拉到 2 分钟，物理表现更真实，角色动作更像人，并首次加入音频与实时 steering。HN 上 886 分，是本周讨论度最高的模型发布。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Genie 4 场景一致性上限为 2 分钟，是 Genie 3 的两倍 | 2 分钟一致性对训练具身智能体是否够用，尚无第三方评测 |
| 新增音频生成与实时 steering 能力 | 实时 steering 的延迟数据未公开 |
| 物理模拟与角色行为拟人度均有提升 | 与 Gemini 4 Argon 的能力边界如何划分仍不清楚 |
| DeepMind 官方博客与模型页同步上线 | 商业化路径（API 还是内部训练工具）未说明 |
| HN 讨论 886 分，为当日最高 |  |

**📖 主编点评**

世界模型的价值不在生成视频，而在给 Agent 提供一个可交互的模拟环境。你做 Agent 项目时可以留意：未来「在 Genie 里跑一遍再上真机」可能成为标准流程，就像现在先跑单测再上线。

📺 [打开原文](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)

---

## 📋 备选阅读

- [研究者开始不满 OpenAI 对突破成果的封锁](https://www.theverge.com/ai-artificial-intelligence/1019921/openai-breakthrough-math-computer-science-physics) —— OpenAI 宣称数学/CS/物理突破但不公开细节，学界反弹。和 ETH 被证伪那条一起看更有意思。
  _Robert Hart_
- [前沿实验室称模型证伪了「指数时间假设」，这意味着什么？](https://techcrunch.com/2026/10/27/frontier-ai-labs-say-their-models-refuted-the-exponential-time-hypothesis-what-does-that-mean/) —— TechCrunch 采访 MIT 计算机科学家解读。属于「看不懂但该知道」类，深度够，可周末读。
  _Tim Fernholz_
- [Firefox Smart Window 加入 AI 表单填写与网页监控](https://www.theverge.com/ai-artificial-intelligence/1019551/firefox-smart-window-ai-fill-forms) —— 浏览器内建 Agent 能力的又一步。对做浏览器侧 Agent 的人有参考价值，但增量不大。
  _Emma Roth_
- [Meta AI 总监 Rohit Patel 离职创业，要做 Ndoc 挑战 Office 与 Workspace](https://techcrunch.com/2026/10/27/meta-ai-director-rohit-patel-leaves-to-take-on-microsoft-office-and-google-workspace/) —— 做 AI 评测与 RL 八年后出走做文档工具。AI 原生办公赛道又添一个重量级玩家。
  _Rebecca Bellan_
- [Delaware 拟允许 AI Agent 独立运营整家公司，无需人类掌舵](https://arstechnica.com/tech-policy/2026/10/no-human-at-the-helm-delaware-plan-would-let-ai-agents-run-entire-businesses/) —— 法律层面的 Agent 主体性实验，同时涉及责任豁免争议。做 Agent 产品的人该知道边界在哪。
  _Jon Brodkin_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
