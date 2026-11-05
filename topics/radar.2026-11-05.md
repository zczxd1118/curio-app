# Curio 趋势雷达 · 2026-11-05

> 你的私人主编 · 今日跨域精选 5 条头条 + 16 条备选

_今天最重要的信号有两个：一是美国中期选举把 AI 数据中心投成了政治议题，45 项地方公投几乎全线否决，Stratechery 和 TechCrunch 都在追问"如果反对建设是长期民意，算力扩张还怎么走"；二是内存/存储涨价已经从 DRAM 蔓延到 Nintendo 卡带供应链，Team Group CEO 直接说"钱也买不到货"。对做 Agent 的你来说，另一条值得盯的是 Meta 收购 Conductor——多 Agent 并行写代码正在被大厂收编。_

---

## 🌟 大厂 AI 动态

### 1. AI 数据中心在中期选举上全线落败：45 项公投被否决，算力扩张撞上永久性民意墙

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _Ben Thompson_

美国中期选举里，数据中心议题被直接放上选票，45 项地方公投中绝大多数被选民否决，跨党派一致。Ben Thompson 的核心追问不是"这次输了"，而是"如果美国人对建设的反对是结构性的、不会随经济周期消退，AI 基建的融资和选址逻辑要不要重写"。这比任何单季财报都更影响未来 6-12 个月的算力供给曲线。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 中期选举中约 45 项与数据中心相关的地方公投进入选票，多数被否决 | 公投结果是否真能阻断已获批项目的开工，目前只有个案证据 |
| 反对票跨党派分布，Ars Technica 称科技业"仍在否认"选民的反 AI 情绪 | 联邦层面是否会出台对冲性立法（加速审批/预emption），尚无信号 |
| Texas 州长选举结果直接触发 AI 相关股票下挫，市场把政治风险计入定价 | 算力缺口是否会转向海外（中东、东南亚）落地，尚无量化数据 |
| TechCrunch 判断中期选举之后还会有更大规模的数据中心冲突 | 电价与地方财政压力在其中的权重，各方解读分歧较大 |
| Stratechery 将问题上升到"美国反对建设是否已成永久状态" |  |

**📖 主编点评**

别只把这条当政治新闻读。你如果要做依赖大模型 API 的 Agent 产品，算力供给的政治风险会传导成价格和配额波动——建议在架构上保留多 provider 切换能力，别把关键链路锁死在单一云的单一大模型上。同时这条是很好的"为什么"素材，比任何教程都更能解释行业为什么开始谈推理成本和本地化部署。

📺 [打开原文](https://stratechery.com/2026/ai-on-the-ballot/)

---

### 3. Meta 收购 AI 编程创业公司 Conductor：核心能力是让工程师同时调度一队 Agent 并行开发

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Lucas Ropek_

Conductor 的产品定位很具体——让软件工程师部署多个 Agent 同时处理项目的不同部分。Meta 把它买下来，说明"多 Agent 并行协作"从个人玩具变成了大厂认可的工程范式。这对你正在做的 content-curator 有直接参考价值：单 Agent 串行执行是当前主流，但并行子 Agent 分工正在成为下一层抽象。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Meta 已完成对 AI 编程创业公司 Conductor 的收购 | Meta 会把 Conductor 整合进内部编码工具还是做成对外产品，未公布 |
| Conductor 的核心产品是让工程师部署 Agent 团队并行处理项目不同部分 | 多 Agent 并行的实际工程收益（相对串行）缺少公开 benchmark |
| 收购由 TechCrunch 于 2026-11-04 报道 | 收购金额未披露，无法判断估值逻辑 |
| 同期 Canva 裁员 1200 人（22%），AI 对软件公司人力结构的挤压在同步发生 | Conductor 团队是否保留独立产品线，尚不明确 |

**📖 主编点评**

这条值得你花 10 分钟想清楚一件事：你的 content-curator 现在是单 Agent 串行，如果拆成"抓取 Agent / 筛选 Agent / 写作 Agent"并行跑，瓶颈会从模型能力转移到编排和状态同步上。Conductor 被收购说明这个方向有产业背书，可以放心在你的项目里试子 Agent 分工，但重点要放在"如何让并行结果收敛"而不是"如何并行"。

📺 [打开原文](https://techcrunch.com/2026/11/04/meta-acquires-ai-coding-startup-conductor/)

---

## 🌟 AI 算力 / 半导体

### 2. 内存危机升级：Team Group CEO 称"钱也买不到货"，明年价格无下行趋势，Apple 制造成本多出 330 亿美元

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Jowi Morales_

存储涨价不再是"贵一点"的问题。Team Group CEO 陈庆文在财报电话会上说，价格明年没有任何下行趋势，极端情况是"有钱也拿不到货"。同一天，Apple 因内存成本上升制造成本增加 330 亿美元，Nintendo 的 ROM 芯片供应商 Macronix 直接退出该业务转做 AI 数据中心闪存。AI 数据中心对 HBM 和服务器内存的挤占，正在把消费电子和游戏卡带的供应链一起拖下水。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Team Group CEO 明确表态：明年内存价格无任何下行趋势 | 涨价周期会持续多久，取决于 AI 数据中心资本开支何时见顶，目前无人给出可信拐点 |
| Apple 制造成本因内存涨价增加 330 亿美元，压力延续到 2027 | 消费级 GPU/整机价格是否会被同步推高，RTX 5090 街价已破 9000 美元但样本有限 |
| Macronix 退出 Nintendo ROM 芯片业务，转产 AI 数据中心用 NOR/NAND | 国产存储厂商能否填补中低端缺口，尚无产能数据 |
| Samsung、SK hynix、Micron 优先把产能分配给高毛利服务器产品与 HBM | 游戏实体卡带是否真的涨价，取决于库存消化速度 |
| Micron 公布 DRAM/NAND 新路线图，含 3D NAND 与 High-NA EUV |  |

**📖 主编点评**

如果你近期要买机器跑本地模型或做推理实验，别等降价——这轮周期的方向是单边的。更实际的建议：把本地推理需求往云端或按需租用迁移，或者优先考虑二手/租赁。做 Agent 项目时也要意识到，token 单价的长期趋势不再是无脑下降，成本模型里该留出涨价缓冲。

📺 [打开原文](https://www.tomshardware.com/pc-components/dram/team-group-ceo-warns-memory-crisis-could-reach-point-where-even-money-cant-buy-goods-will-get-worse-next-year-with-no-downward-trend-in-price-whatsoever)

---

## 🌟 股票

### 4. Intel 股价崩塌加剧，3.5 万亿美元芯片抛售潮扩散；Oracle 发 200 亿美元新股债为 AI 基建融资

**[股票]** · ⭐⭐⭐⭐ · _entryleveljobsc_

芯片板块的抛售从 Intel 扩散到整个半导体，规模达 3.5 万亿美元。与此同时 Oracle 申请发行 200 亿美元新股和债券来给 AI 基建输血——一边是二级市场在撤，一边是一级市场在加杠杆。这种背离通常不会持续太久，要么是市场错杀，要么是基建投资过度，接下来一两个季度的财报会给出答案。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Intel 股价持续下跌，芯片板块整体抛售规模达 3.5 万亿美元 | 这轮抛售是估值修正还是趋势反转，取决于 AI 收入兑现速度，尚无定论 |
| Oracle 提交文件，拟发行 200 亿美元新股与债券为 AI 基建融资 | Oracle 的 200 亿美元融资能否顺利定价，反映机构对 AI 债的真实态度 |
| US Hedge Funds 已清空 2025 年以来买入的全部 AI 股票 | Intel 的 14A 工艺（PDK 0.9 已发布）能否挽回基本面，需等 2027 量产 |
| AMD Q4 指引 170 亿美元，预计史上首次单季营收超过 Intel | 对冲基金清仓是否代表聪明钱离场，还是只是季度调仓 |
| AMD 数据中心业务翻倍，游戏业务下滑 40% |  |

**📖 主编点评**

你不需要交易，但需要读懂这个信号：AI 基建的融资成本在上升，这会传导到大模型 API 的定价策略。如果云厂商融资变贵，推理价格的下行速度会放缓——这和你做 Agent 产品的成本模型直接相关。另外 AMD 首次单季营收超 Intel 是个历史节点，值得记一笔，做技术选型时 x86 生态的重心正在偏移。

📺 [打开原文](https://finance.yahoo.com/markets/article/the-intel-stock-collapse-is-getting-worse--and-the-37-trillion-chip-rout-is-spreading-212154947.html)

---

## 🌟 金融

### 5. Tangled 发布联邦化代码托管方案：像 email 一样去中心化的 code forge

**[金融]** · ⭐⭐⭐⭐ · _zlliang_

Tangled 提出"联邦化代码托管"——每个实例独立运行，但能像 email 一样互相发现和协作。这是对 GitHub 单点垄断的一次认真技术回应，也踩在"平台风险"情绪最浓的时间点上（同期 Google 因 AI 政策威胁关掉学校的 Search）。对做开源 side project 的人，这是一个值得关注的替代路径。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Tangled 发布联邦化 code forge 方案，架构上类似 email 的联邦模型 | 联邦化代码托管的实际协作体验能否接近 GitHub，缺少大规模验证 |
| 项目在 Hacker News 获得 333 分，进入当日热榜前列 | 跨实例的 issue/PR 流转协议是否标准化，尚未看到规范文档 |
| 同期 Google 因学校限制 AI 而威胁关闭 Search，平台权力争议升温 | 商业化与可持续维护模式不明 |
| GitHub 目前仍是代码托管的事实垄断者 | 迁移成本对已有大型仓库是否可接受，无数据 |

**📖 主编点评**

短期内你不会把 content-curator 从 GitHub 搬走，但这条值得收藏：它代表"平台可替换性"这个工程价值观正在被认真对待。更实际的用法是——如果你以后要做需要长期存活的个人工具，架构上把"代码托管"和"CI/协作"解耦，别让整个工作流绑死在一家平台上。

📺 [打开原文](https://tangled.org/blog/forge/)

---

## 📋 备选池

### AI

- [DeepSeek Harness 超详细教程：50 分钟吃透 DSH，让 SuperAgent 干活](http://www.bilibili.com/video/av117540671982699) —— 11-01 新发，60 天制作，是目前少见的 DSH 系统教程；放备选是因为教程类密度不如头条，但对你做 Agent 编排有实操价值。
  _Git源宝_
- [DeepSeek Harness 实测 vs Claude Code：同一模型下工具链差距比想象大](http://www.bilibili.com/video/av117100337236191) —— 用同一个 DeepSeek Pro 模型在两个 harness 里跑同样任务做对比，正好回答"模型重要还是工具链重要"，比纯教程更有信息量。
  _程序员晓刘_
- [认真用 Claude Code 的人，迟早会遇见 Everything Claude Code（116K star 配置项目）](http://www.bilibili.com/video/av116319122885806) —— 拆解 116K star 的 Claude Code 配置项目：斜杠命令、子代理、Hooks、学习系统，工程细节密度高，契合你的偏好。
  _极客魔导师_
- [14k Star Claude Code 开源桌面端，能自动操作电脑了](http://www.bilibili.com/video/av117251936293145) —— 基于泄露源码做的开源桌面端 cc-haha，重构了 Computer Use，支持自选模型不需 Claude 账号，技术猎奇价值高。
  _程序员阿江-Relakkes_
- [Claude Code 接入微信：一行命令实现手机远程开发（cc-connect）](http://www.bilibili.com/video/av116350093694897) —— cc-connect 把 Claude Code 接进即时通讯工具做远程调用，是个不错的 side project 灵感，但工程深度一般。
  _下班学AI_

### AI 算力 / 半导体

- [Nvidia 讨论按 GPU 每年 2000 美元收软件费，用于在 AI 基建上跑 Agent](https://www.tomshardware.com/pc-components/gpus/nvidia-discusses-usd2-000-per-gpu-annual-software-fee-for-running-agents-on-ai-infrastructure-firm-already-charges-more-than-twice-that-amount-for-its-ai-enterprise-software-platform) —— 如果 Agent 运行要按 GPU 年费计费，会直接改变 Agent 产品的成本结构，值得提前知道定价风向。
  _gscott_
- [Nvidia 只能满足中国 700 亿美元 GPU 订单的 1%](https://www.tomshardware.com/pc-components/gpus/nvidia-can-only-fulfill-1-percent-of-chinas-massive-usd70-billion-gpu-order-for-ai-chips-report-claims-supply-constraints-choke-export-friendly-rtx-pro-5500-deliveries-despite-huge-demand) —— 供给约束 + 出口管制的双重挤压，1% 的履约率是个极端数字，反映全球算力分配的紧张程度。
  _Ben Stockton_
- [Nvidia RTX Spark 加密固件让 Linux 上推理速度降到 35%](https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop) —— HN 600 分热帖，加密固件拖慢 Linux 推理，对想用消费级卡跑本地模型的人是直接的坏消息。
  _novaRom_
- [Google 发布 Gemini 4 Carbon，微弱超过 Claude Opus 5.5，号称最不易幻觉](https://www.tomshardware.com/tech-industry/artificial-intelligence/google-reveals-new-gemini-4-carbon-ai-model-narrowly-beating-claude-opus-5-5-frontier-ai-model-is-also-the-least-likely-to-hallucinate-benchmarks-claim) —— 模型发布动态，Carbon 在 Artificial Analysis 榜单登顶，但"微弱超过"意味着前沿模型差距已进入噪声区间。
  _Jon Martindale_

### 大厂 AI 动态

- [Gemini 对订阅用户的聊天记录也用于训练（个人账号）](https://news.ycombinator.com/item?id=50363461) —— HN 670 分，付费也不豁免训练，对把敏感内容丢给 Gemini 做 Agent 的人是隐私层面的实质提醒。
  _jameslk_
- [Uber：几乎没人用 AI Agent 叫车，最忙一周只有 4 个人](https://techcrunch.com/2026/11/04/almost-no-one-uses-ai-agents-to-book-their-uber-company-says/) —— 一个冷静的数据点：Agent 落地真实场景的使用率极低，值得你对"Agent 已成熟"的叙事保持怀疑。
  _Sarah Perez_
- [Apple 据报削减内部 AI 使用预算](https://techcrunch.com/2026/11/04/apple-is-reportedly-cutting-budgets-for-its-internal-ai-usage/) —— 工程团队 AI 支出被大幅削减，和"全员 AI 化"的行业叙事形成反差，值得留意大厂内部的实际 ROI 计算。
  _Lucas Ropek_

### 股票

- [Anthropic IPO 文件警告可能"即将"接近递归自我改进（RSI）](https://epyhia.com/anthropic-s-ipo-filing-warns-it-may-be-imminently-close-to-recursive) —— S-1 里写 RSI 风险是极罕见的披露，无论你信不信，这是理解 Anthropic 叙事的关键文本。
  _arbuge_
- [研究机构称 Anthropic IPO 是"对投资者轻信度的空前考验"](https://www.cnbc.com/2026/10/07/anthropic-will-be-most-ridiculous-ipo-of-year-analyst-says.html) —— 与上一条形成对照：一边是 RSI 叙事，一边是"最荒谬 IPO"的质疑，读两条能看清这场 IPO 的争议结构。
  _m463_

### 金融

- [美国联邦赤字一年跳增 12%，接近 2 万亿美元](https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html) —— 赤字与 AI 基建融资在同一时间窗口放大，是理解"钱从哪来"的宏观背景，但离你的日常较远。
  _ck2_
- [3000 亿美元"债务墙"逼近 PE 控股公司](https://www.wsj.com/finance/investing/a-300-billion-debt-wall-is-looming-over-private-equity-backed-companies-d6359497) —— 私募信贷的到期压力，和 AI 基建加杠杆是同一枚硬币的两面，作为宏观风险背景放备选。
  _JumpCrisscross_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
