# Curio 趋势雷达 · 2026-11-25

> 你的私人主编 · 今日跨域精选 5 条头条 + 18 条备选

_今天真正的大信号只有一个：Nvidia 用两周时间演完了「逼宫—辞职—复职」全套，黄仁勋回归首场全员会承认在心理咨询、否认白宫干预，同时 SEC 在查会计问题、国会开骂、Anthropic 股价跌破 83 美元 IPO 价。AI 资本叙事第一次出现「治理风险」这个新变量，而不是算力或模型能力。另一条线是 Gemini 4 系列（Carbon/Hydrogen/Neon）在两周内连发三代，模型迭代节奏已经快到评测榜都跟不上。_

---

## 🌟 AI 算力 / 半导体

### 1. Nvidia 董事会正式复职黄仁勋：从辞职到回归只隔 11 天，SEC 会计调查与国会质疑同步压顶

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _alanwong_

11 月 12 日黄仁勋因第二段办公室恋情报道辞职，11 月 23 日董事会宣布复职，官方新闻稿措辞是「恢复总裁、CEO 与董事职务」。这 11 天里 Nvidia 市值经历剧烈震荡，做空基金 Short Nvidia 在 91% 回撤后被停牌，Polymarket 上两个可疑账户靠「黄回归」赚了 34 万美元。复职不是终点，而是把治理问题正式摆上台面。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 11 月 12 日黄仁勋辞职，Reuters 与 BBC 均报道辞职与第二段员工恋情报道有关 | 复职是否意味着董事会独立性彻底失效，Reuters 称批评者已质疑「董事会反转损害独立性」 |
| 11 月 23 日 Nvidia 官方新闻稿宣布董事会复职黄仁勋为总裁、CEO 及董事 | SEC 会计调查与新加坡销售不披露是否指向同一问题，目前只有「潜在会计问题」这一模糊表述 |
| 复职前一周 Nvidia 员工发起请愿要求黄回归，Wired 报道该请愿获得 820 分 HN 讨论 | 白宫是否真的介入，黄仁勋在全员会上否认，但 NYT 称 Trump 曾「指示推动复职」 |
| SEC 正在调查 Nvidia 潜在会计问题，Reuters 11 月 20 日报道 | 黄仁勋称在做心理咨询、感谢白宫，这些表态能否平息机构投资者仍未知 |
| Nvidia 停止披露新加坡销售额，同期营收达 1040 亿美元，FT 报道 | Megaspeed 被美国商务部列入出口禁令，与 Nvidia 新加坡销售疑云是否关联尚无定论 |
| 国会两党公开批评复职决定，CNBC 引述议员称这是「品格的失败」 |  |

**📖 主编点评**

你不需要关心八卦，但要关心一件事：AI 算力链的最大单一供应商现在带着治理折价交易。如果你在做任何依赖 GPU 成本假设的项目规划或投资判断，把「Nvidia 供应链稳定性」从默认常量改成需要显式评估的变量。另外这条新闻的传播路径（HN 首发 → 官方稿 → 国会表态 → 做空基金爆仓）本身就是一次很好的信息流观察样本。

📺 [打开原文](https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director)

---

## 🌟 大厂 AI 动态

### 2. Gemini 4 Neon 发布并登顶 Models Engineering Index，Google 两周内连发 Carbon / Hydrogen / Neon 三代

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _yigitdemirag_

10 月 28 日 Gemini 4 Carbon、11 月 12 日 Gemini 4 Hydrogen（含 Antigravity 里的 Orchestrator）、11 月 18 日 Gemini 4 Neon，三周三代。Neon 上线当天就在第三方 Models Engineering Index 登顶，有博主直接称它「看起来像 Opus 5.5 的竞争对手」。这个发布节奏本身比单代模型能力更值得注意。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 4 Carbon 于 10 月 28 日发布，10 月 29 日登上 Artificial Analysis Intelligence Index v5 第一 | 三代模型之间的实际能力差异有多大，目前只有第三方榜单和博主评测，缺少官方对比数据 |
| Gemini 4 Hydrogen 于 11 月 12 日发布，同步在 Google Antigravity 上线 Orchestrator | Neon 是否真是 Opus 5.5 同级，micjm.com 的判断属于个人评测而非系统基准 |
| Gemini 4 Neon 于 11 月 18 日发布，HN 1071 分 | Gemini 4 Carbon「为什么这么慢」的讨论（kernel.dev 一文 288 分）暗示发布节奏与内部工程压力存在张力 |
| Neon 在 Models Engineering Index 登顶，该榜单由第三方维护 | Orchestrator 在 Antigravity 里的具体编排能力边界尚不清楚 |
| Gemini Decisions API 于 11 月 11 日单独发布，是面向 Agent 决策的独立接口 | DeepMind 员工正在组建工会（gdmunion.co.uk），是否影响后续发布节奏未知 |
| Genie 4 世界模拟模型于 10 月 27 日发布、11 月 18 日开放使用 |  |

**📖 主编点评**

对你的 content-curator 项目来说，这是直接的工程信号：模型迭代周期已经压缩到 2-3 周，任何硬编码模型名的架构都会很快过时。如果你在 Agent 里写死了具体模型，现在就该把模型选择抽象成配置层。另外 Gemini Decisions API 值得单独看一眼——它是少数专门为 Agent 决策路径设计的官方接口，比通用 chat completion 更贴近你要做的事。

📺 [打开原文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

---

## 🌟 股票

### 3. Anthropic 跌破 83 美元 IPO 发行价，承销行稳定股价的仓位已平掉

**[股票]** · ⭐⭐⭐⭐ · _thm_

Anthropic 以 83 美元定价、1.5 万亿美元估值上市，首日冲高后迅速回落，11 月 24 日正式跌破发行价。更关键的是 Reuters 报道承销行已经关闭了用于稳定股价的仓位——这意味着护盘力量撤了。TechCrunch 直接把这称为「对 AI 创业公司的令人担忧的信号」。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Anthropic IPO 定价 83 美元/股，估值 1.5 万亿美元，AP 报道 | 跌破发行价是短期市场情绪还是估值逻辑重估，目前只有一周数据 |
| 11 月 24 日股价跌破 83 美元发行价，Reuters 报道「首日涨势瓦解」 | 9000 亿美元支出承诺与 17 亿美元季度人力成本的组合能否持续，取决于收入曲线，而收入数据尚未充分披露 |
| 承销行已关闭用于稳定股价的仓位，Reuters 11 月 20 日报道 | IPO 文件警告可能「即将」接近递归自我改进（RSI），这一表述的法律与监管含义不明 |
| IPO 文件披露季度人力成本 17 亿美元，人均月成本约 10.7 万美元 | Michael Burry 称 Anthropic 在「赌上存在」，属于观点而非事实 |
| IPO 文件披露 9000 亿美元 AI 支出承诺，FT 报道 | AI 创业公司估值整体承压的传导速度未知 |
| Blackstone 称 Anthropic 可能拿不到投资级评级，FT 报道 |  |

**📖 主编点评**

这条对你的实际含义不是「别买」，而是：AI 一级市场估值锚正在松动，这会反向影响你未来求职和做 Side Project 时的资源预期。如果你在考虑毕业后进 AI 创业公司，现在多看一眼它们的融资结构和 runway，比看产品 demo 更有用。另外 IPO 文件里那句「接近 RSI」的警告，是少见的把技术风险写进法律文件的案例，值得找原文读一遍。

📺 [打开原文](https://www.reuters.com/business/anthropic-breaks-below-83-ipo-price-debut-rally-unravels-2026-11-24/)

---

## 🌟 AI

### 4. Claude 桌面端把 Code / Design / Cowork 三合一，Claude Code 从命令行进化成完整桌面客户端

**[AI]** · ⭐⭐⭐⭐ · _技术爬爬虾_

11 月 8 日发布的这条视频拆解了 Claude Desktop 的一波大更新：Claude Code 的编程能力、Claude Design 的设计能力、Claude Cowork 的办公能力被收进同一个客户端，配 Opus 5.5。这是 Anthropic 第一次把「Agent 工作台」做成一个统一入口，而不是散在 CLI、网页、IDE 插件里。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Claude Desktop 已整合 Claude Code、Claude Design、Claude Cowork 三项能力到同一客户端 | 三合一客户端是否真的减少上下文切换成本，还是只是 UI 层聚合，需要实际使用验证 |
| Claude Code 从纯命令行工具变为桌面客户端形态 | Opus 5.5 在桌面端的实际表现与 API 端是否一致，尚无系统对比 |
| 该版本搭配 Opus 5.5 模型 | Cowork 的办公能力边界（能操作哪些外部系统）不清晰 |
| 视频发布于 11 月 8 日，属于近期更新而非旧内容 | 第三方 API 接入的稳定性取决于 Anthropic 是否封堵，历史上有先例 |
| 社区已有第三方 API 接入、中文汉化、免登录等改法流传（多条 B 站教程佐证） | 桌面端是否会成为 Anthropic 的主推形态，还是并行选项，官方未明确 |

**📖 主编点评**

你在做 content-curator，这直接关系到你的开发形态选择：如果 Claude Desktop 真能把 Code + Cowork 打通，你的 Agent 可能不需要自己写 UI，而是作为一个 Skill 或 MCP 挂进桌面端。建议你花一个晚上实际装一遍，重点测两件事——它能不能稳定调用你自己的 MCP server，以及 Cowork 能不能读到本地文件系统。这两点决定了你的项目是「独立应用」还是「桌面端插件」。

📺 [打开原文](http://www.bilibili.com/video/av117580048108571)

---

## 🌟 金融

### 5. 巴西税务局把税收计算器以 MIT 协议开源到 GitHub，税改透明度第一次落到代码层

**[金融]** · ⭐⭐⭐⭐ · _dvaplima_

巴西联邦税务局在 GitHub 上发布了该国第一个开源政府代码：一个完整的税收计算器，MIT 协议。背景是巴西正在推进的税制改革，官方说法是「扩大税改透明度」。HN 上 789 分，讨论集中在「政府把税法写成可执行代码」这件事本身的意义。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 巴西联邦税务局（Receita Federal）在 GitHub 发布首个开源代码库 | 开源计算器是否与正式征税口径完全一致，官方未承诺代码即法律 |
| 该代码库是税收计算器，采用 MIT 协议 | MIT 协议意味着任何人可商用修改，但税法解释权仍在政府，二者如何协调不明 |
| 发布背景是巴西税制改革，官方表述为提升透明度 | 其他国家的税务机构是否会跟进，目前无迹象 |
| HN 讨论 789 分，属于当日高热度技术话题 | 代码维护的持续性取决于政府预算与人员，开源项目的长期治理未知 |
| 这是巴西政府第一个公开发布的开源代码 | 对个人开发者是否有实际可用场景，取决于巴西税法的适用范围 |

**📖 主编点评**

这条对你是个方法论样本，不是实用工具：把「规则」写成可执行、可审计、可 fork 的代码，是政府透明度的一种新形态。你做 content-curator 时其实在做同一件事——把「什么值得看」这条模糊规则写成可运行的筛选逻辑。区别在于你的规则可以私有，而公共规则一旦开源就获得了可验证性。值得想想你的 Agent 里哪些判断逻辑未来可以抽出来开源，作为简历上的「可审计作品」。

📺 [打开原文](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/novembro/receita-federal-publica-primeiro-codigo-fonte-aberto-no-github-e-amplia-transparencia-da-reforma-tributaria)

---

## 📋 备选池

### AI 算力 / 半导体

- [Google DeepMind 用 AlphaProof Code 形式化证明了 Signal 加密协议](https://www.tomshardware.com/tech-industry/artificial-intelligence/google-deepmind-ai-engineers-conjure-mathematical-proof-of-signals-encryption-protocol-alphaproof-code-framework-powered-human-bot-cooperation-for-speedy-work) —— AI 参与形式化验证真实生产级加密协议，是「AI 做数学」从玩具走向工程的关键一步，但细节还停留在新闻稿层面。
  _Bruno Ferreira_
- [两块 DGX Station 跑 GLM-5.3，vLLM 下达到 607.8 tok/s](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/) —— 有具体吞吐数字和多机部署细节，是少见的推理工程实操文，但场景偏企业级，离个人项目远。
  _wondersky_
- [TSMC 遭黑客攻击，已向 SEC 提交声明](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000800/a20261112statementregardin.htm) —— 原始 SEC 文件，信息密度高但无解读，适合自己读原文；影响面可能很大但细节未明。
  _gmays_
- [Winbond 认证 NOR Flash 切入边缘 AI 存储](https://www.eetimes.com/winbond-widens-edge-ai-reach-certifies-nor-flash/) —— 边缘 AI 的存储瓶颈是个被低估的工程问题，但这条是厂商通稿性质，缺独立数据。
  _Gary Hilson_

### 大厂 AI 动态

- [即便最好的 AI Agent 也搞不定日常生活](https://techcrunch.com/2026/11/24/even-the-best-ai-agents-struggle-with-everyday-life/) —— 新基准显示顶级 Agent 在日常任务上仍不可靠且会引入新问题，和你做 Agent 项目直接相关，但报道偏结论缺方法细节。
  _Rebecca Bellan_
- [Amazon 收购 Decart，7.5 亿美元赌软件缩小与 Nvidia 的芯片差距](https://techcrunch.com/2026/11/24/amazons-decart-acquisition-is-a-bet-on-using-software-to-narrow-the-gap-with-nvidia-in-the-ai-chip-race/) —— 用软件效率补硬件差距的思路值得关注，但 7.5 亿美元数字来自「reported」，未经证实。
  _Anna Heim_
- [Walmart 联手 Meta，把黑五折扣搬进 AI Agent Muse](https://techcrunch.com/2026/11/24/walmart-teams-up-with-meta-to-bring-black-friday-deals-to-ai-agent-muse/) —— AI Agent 第一次成为零售大促的正式入口，商业信号强于技术信号，但对你个人项目参考价值有限。
  _Lauren Forristal_
- [Microsoft 因 Outlook 大规模宕机内部宣布「Code Red」](https://www.theverge.com/news/1042025/microsoft-code-red-outlook-outage) —— 近 24 小时邮件中断触发内部红色警报，是基础设施可靠性话题，但和你的关注方向关联弱。
  _Tom Warren_
- [Huawei 被判窃取美国商业机密](https://www.theverge.com/tech/1041820/huawei-guilty-trade-secrets-trial) —— 纽约联邦法院陪审团裁定有罪，地缘科技话题，但判决细节和后续影响尚未展开。
  _Emma Roth_

### 股票

- [Nasdaq 回吐 2026 年全部涨幅，Nvidia 与 Anthropic 双双下挫](https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-24-2026) —— 大盘层面的确认信号，说明 AI 板块回调不是个股事件，但属于行情播报而非深度分析。
  _petethomas_
- [Anthropic IPO 文件里的人力成本：季度 17 亿美元，人均月 10.7 万美元](https://www.techspot.com/news/114428-anthropic-ipo-filing-reveals-17-billion-quarterly-personnel.html) —— 一个具体到人均的数字，比估值讨论更有信息量，适合作为理解 AI 公司成本结构的锚点。
  _entryleveljobsc_
- [Net Interest：供需——在 AI 经济里寻找均衡](https://www.netinterest.co/p/supply-and-demand) —— Marc Rubinstein 的金融视角长文，质量稳定，但发布在 11 月 23 日、偏综述，留作周末深读。
  _Marc Rubinstein_

### 金融

- [Visa、Mastercard、JPMorgan 客户数据被黑客泄露](https://www.wsj.com/finance/banking/visa-mastercard-and-jpmorgan-customer-data-leaked-by-hackers-3b5a0f87) —— 三大支付机构同时中招，影响面大，但 WSJ 付费墙且细节有限，先记着等后续披露。
  _mikhael_
- [美联储担心 AI Agent 可能引发银行挤兑](https://gizmodo.com/the-fed-is-worried-ai-agents-could-trigger-a-bank-run-2000840566) —— 把 Agent 的速度优势和金融系统脆弱性连起来，是个新颖角度，但 Gizmodo 报道偏转述，缺一手材料。
  _pera_
- [Oracle 申请发行 200 亿美元新股与债券为 AI 建设融资](https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html) —— AI 基建融资从股权转向债权的又一例证，但发布于 11 月 2 日，时效性偏旧。
  _smartmic_

### AI

- [狂烧上万元，我用 AI 做了 500 多个网站](http://www.bilibili.com/video/av117666283002439) —— 11 月 23 日发布，有真实成本数字和开源模板库，是 vibe coding 规模化产出的少见样本，但标题党味重、内容偏产品推广。
  _程序员鱼皮_
- [Vibe Coding 完不会获客？我用 AI 做了一个营销数据库](http://www.bilibili.com/video/av117587245599812) —— 从「做出产品」推进到「找到用户」，是 Side Project 工作流里被忽略的一环，演示了 Antigravity + MCP 的实际接法。
  _熠辉IndieDev_
- [全网最详细的 AI 入门课：一期搞懂 58 个 AI 术语](http://www.bilibili.com/video/av117587144940374) —— 11 月 9 日发布，术语覆盖到 Skill 这一层，适合当索引而非学习材料，对你来说密度偏低。
  _亚里今天也要AI_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
