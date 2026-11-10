# Curio 趋势雷达 · 2026-11-10

> 你的私人主编 · 今日跨域精选 5 条头条 + 15 条备选

_今天只有一个真正的信号：Nvidia 的 Jensen Huang 丑闻从八卦升级成公司治理与监管事件——董事会立案、国会传唤、集体诉讼、股价跌超 4%，同时 Anthropic 一边发新模型一边推进 IPO。AI 资本叙事正在被两件事同时拉扯：算力军备竞赛（Anthropic 花 34 亿美元买燃气轮机）和信任危机。_

---

## 🌟 大厂 AI 动态

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

## 🌟 AI

### 3. Claude Desktop 把 Code、Design、Cowork 收进同一个客户端，命令行 Agent 正在变成桌面应用

**[AI]** · ⭐⭐⭐⭐ · _技术爬爬虾_

Claude 桌面端这轮更新把 Claude Code 的编程能力、Claude Design 的设计能力、Claude Cowork 的办公能力合并进一个客户端，配 Opus 5.5。Claude Code 从黑框终端进化成有 GUI 的完整形态，这个方向值得你亲手跑一遍。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Claude Desktop 已整合 Claude Code、Claude Design、Claude Cowork 三块能力 | 桌面端相比 CLI 在长任务、后台任务上的实际体验差异，需要自己实测 |
| Claude Code 在桌面端不再是纯命令行工具，具备图形界面交互 | GUI 化是否会削弱脚本化、可编程的优势，目前没有定论 |
| 当前搭配的模型是 Opus 5.5 | Opus 5.5 在编码任务上的具体提升幅度，官方未给可复现的 benchmark |
| 视频发布于 2026-11-08，属于本周新内容 | 这套整合对第三方 IDE 插件生态的挤压程度，尚不明朗 |

**📖 主编点评**

你正在做 content-curator，这类"Agent 从 CLI 走向 GUI"的演进直接决定你的产品形态选择。建议花 30 分钟装一次，重点看两件事：桌面端怎么展示工具调用过程、以及它怎么处理需要人工确认的权限请求——这两点是你自己 Agent 的交互设计参考。

📺 [打开原文](http://www.bilibili.com/video/av117580048108571)

---

## 🌟 AI 算力 / 半导体

### 4. DeepX 第二代 AI 加速器流片，LPDDR5x-PIM 架构宣称 6.7 倍性能提升、5W 内跑大模型

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Sally Ward-Foxton_

韩国 DeepX 宣布第二代 AI 加速器完成流片，采用 LPDDR5x 存内计算（PIM）架构，官方给出的数字是 6.7 倍性能提升，目标是在 5W 功耗内本地运行大语言模型，主攻机器人与边缘设备。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 第二代芯片已完成 tape-out，进入流片后阶段 | 6.7 倍是与自家上一代还是与竞品对比，官方口径需要核实 |
| 架构采用 LPDDR5x-PIM（存内计算），宣称性能提升 6.7 倍 | "5W 内跑大模型"的具体模型规模与 token/s 未披露 |
| 目标场景是机器人等边缘市场，可在 5W 以内运行大模型 | PIM 架构的软件栈成熟度是落地关键，目前没有生态信息 |
| 同期 Tom's Hardware 报道其 DX-M1 处理器用"黄油散热器"演示比竞品低 40 度 | 边缘端跑 LLM 的实际需求规模，仍待市场验证 |

**📖 主编点评**

你是电子信息工程背景，这条是少见的"架构层面"而非"产品层面"的进展。存内计算解决的是内存墙问题，值得你花 10 分钟读原文搞清楚 PIM 到底把计算单元放在哪一层——这个概念在面试里比背参数值钱。

📺 [打开原文](https://www.eetimes.com/deepx-tapes-out-second-gen-chip-projects-6-7x-performance-gain-with-lpddr5x-pim/)

---

## 🌟 股票

### 5. 中期选举后 AI 交易集体退潮，纳斯达克两日蒸发 2.5 万亿美元

**[股票]** · ⭐⭐⭐⭐ · _madihaa_

民主党中期选举表现超预期，市场担忧数据中心扩张政策环境变化，叠加 AI 成本质疑，纳斯达克跌入回调区间，两日市值蒸发 2.5 万亿美元，芯片股跌幅居前，被称作 1896 年以来最差的中期选举后交易日。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 纳斯达克两日内市值蒸发约 2.5 万亿美元，跌幅进入回调区间 | 这轮回调是估值修正还是趋势反转，取决于下季度云厂商资本开支指引 |
| 芯片股是重灾区，Intel 股价持续下跌，芯片板块整体蒸发 3.5 万亿美元 | 选举结果与 AI 股价的因果链是否成立，多数分析仍属事后归因 |
| 对冲基金据报已清空 2025 年以来建仓的 AI 股票 | Anthropic IPO 定价会成为情绪修复还是二次探底的触发点，无法预判 |
| 得州州长选举结果被视为数据中心扩张的风险变量 | AI 基建融资从股权转向债务的可持续性，尚无压力测试 |
| Oracle 提交文件拟增发 200 亿美元股票与债券为 AI 基建融资 |  |

**📖 主编点评**

这条放进来是因为它和你的头条 1、2 是同一件事的三面：治理风险、资本开支、市场情绪。你不需要做交易判断，但要意识到——如果 AI 融资环境收紧，你依赖的 API 价格、免费额度、模型迭代速度都会受影响。做个人项目时，把"供应商可能涨价或限流"当成默认假设。

📺 [打开原文](https://finlaws.substack.com/p/25t-has-been-wiped-from-us-stocks)

---

## 📋 备选池

### 大厂 AI 动态

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

### AI 算力 / 半导体

- [Nvidia RTX Spark 加密固件让 Linux 上推理速度掉到 35%](https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop) —— HN 617 分，本地跑模型的硬件自由度在收缩，对自建推理的人是实打实的坏消息。
  _Hacker News_
- [Nvidia 收紧海外云 GPU 对华租赁，合作伙伴面临 51% 非中国配额](https://www.tomshardware.com/tech-industry/policy/nvidia-cracks-down-on-overseas-cloud-ai-gpu-rentals-for-china-partners-face-51-percent-non-chinese-quota-as-black-market-b300-rack-prices-surge-to-usd2-8-million) —— 黑市 B300 整机架价格涨到 280 万美元，出口管制的实际执行细节比政策本身更值得看。
  _Tom's Hardware_
- [内存短缺逼手机厂商把旧设备内存熔下来重新焊到新机上](https://www.tomshardware.com/pc-components/dram/memory-shortage-spurs-smartphone-makers-to-melt-used-memory-off-old-devices-then-re-solder-it-onto-new-products-recycled-memory-to-keep-budget-phones-affordable-reballing-adoption-to-double-by-2027) —— DRAM 涨价传导到消费电子的最直观证据，reballing 采用率预计 2027 年翻倍。
  _Tom's Hardware_
- [律师用 8 张二手 V100 搭私有 AI 服务器，跑 DeepSeek V4.1 Flash 达 215 tokens/s](https://www.tomshardware.com/tech-industry/artificial-intelligence/lawyer-builds-private-ai-server-with-eight-used-nvidia-v100-gpus-up-to-215-tokens-per-second-to-keep-legal-files-offline-costing-about-usd2-400-per-four-gpu-board) —— 四卡板约 2400 美元，2018 年的卡跑 2026 年的模型，本地部署的性价比参考样本。
  _Tom's Hardware_
- [中国建成 800MW AI 数据中心园区对标 Stargate，首期 120MW 一年内交付、成本仅五分之一](https://www.tomshardware.com/tech-industry/data-centers/china-builds-massive-800-megawatt-ai-data-center-campus-to-rival-us-stargate-project-galaxy-campus-delivers-first-120-megawatts-in-a-year-at-one-fifth-the-cost) —— 远景的 Galaxy 园区结合风电、储能和非常规散热，建设速度与成本是这条的重点。
  _Tom's Hardware_

### 股票

- [Michael Burry：Anthropic 是在拿"乐观情绪"赌上自己的存亡](https://www.businessinsider.com/michael-burry-anthropic-ipo-outlook-ant-big-short-2026-11) —— 配合 WSJ 报道的大型投资者对 1.5 万亿美元估值存疑，IPO 定价会是一场公开博弈。
  _Business Insider_
- [Oracle 提交文件拟增发 200 亿美元股票与债券为 AI 基建融资](https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html) —— AI 基建融资从股权转向债务的典型样本，利率环境一变这类结构最先承压。
  _CNBC_

### 金融

- [Tesla 将停产 Cybertruck](https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817) —— HN 1160 分，销量长期不佳后的收场；同期 Tesla 与 SpaceX 两日合计蒸发 4200 亿美元市值。
  _NBC News_
- [美国联邦预算赤字一年内增长 12%，接近 2 万亿美元](https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html) —— 在 AI 资本开支狂飙的同一时期，财政端也在扩张，利率路径会更难预测。
  _Yahoo Finance_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
