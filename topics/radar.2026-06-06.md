# Curio 趋势雷达 · 2026-06-06

> 你的私人主编 · 今日跨域精选 5 条头条 + 15 条备选

_今天全球AI牛市遭遇黑色星期五，费城半导体指数暴跌超10%，美光因内存需求降温担忧单日重挫13%。与此同时，SpaceX IPO进入倒计时，与Anthropic和谷歌签下合计700亿美元算力大单，但Morningstar估值仅为IPO目标一半。Anthropic IPO也箭在弦上，年化营收已达470亿美元。Claude Code的Ultracode功能悄然上线，可操控100个Agent并行开发，是本周最值得关注的工程实践。_

---

## 🌟 AI

### 1. Claude Code Ultracode上线：操控100个Agent并行开发，Vibe Coding进入脚本化新纪元

**[AI]** · ⭐⭐⭐⭐⭐ · _技术胖_

Anthropic为Claude Code V2.1.47/48秘密新增了Workflow功能，被官方从Changelog中删除但未从代码中移除。该功能允许用户通过JS脚本定义多Agent协同工作流，单个任务可拆解给100个子Agent并行执行。这是自MCP以来Claude Code最重要的架构升级，直接解决了大型项目单Agent跑不完的痛点。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Claude Code V2.1.47/48新增Workflow功能，支持JS脚本定义多Agent工作流 | 官方删除Changelog的原因不明，可能是功能尚未稳定或策略调整 |
| 单个Workflow可调度最多100个Agent并行执行子任务 | 100个Agent并行实际效果取决于任务拆分粒度，存在边际收益递减 |
| 功能被官方从Changelog中删除但代码中保留，可通过特定方式启用 | 脚本化工作流对非开发者用户门槛较高，可能限制普及速度 |
| Ultracode（超码）为同一功能的中文社区命名 | 与Anthropic即将IPO的节奏是否相关，有待观察 |

**📖 主编点评**

你应该立即尝试这个功能。如果你在用Claude Code做Side Project，Workflow能让你把"写一个记账App"拆成"设计数据库→写API→写前端→部署"四个子任务并行执行，效率翻倍。关注技术胖视频中的具体配置方法，尤其是JS脚本的编写模板——这是未来AI编程的标配能力。

📺 [打开原文](http://www.bilibili.com/video/av116697163896598)

---

## 🌟 AI 算力 / 半导体

### 2. 全球AI大牛市遭黑色星期五：费城半导体指数暴跌10%，单日市值蒸发超1万亿美元

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _华尔街见闻 API_

周五强劲非农数据引爆加息忧虑，叠加博通财报指引失望、谷歌增发、Meta融资传闻及SpaceX IPO预期，多重利空共振。费城半导体指数单日暴跌逾10%，美光因SemiAnalysis报告称英伟达削减内存容量而重挫13%。这是持续两个月的AI大牛市首次遭遇系统性回调。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 费城半导体指数周五暴跌逾10%，单日市值蒸发超1万亿美元 | SemiAnalysis报告称英伟达削减内存容量，但该机构此前多次看空美光被基本面打脸 |
| 美光股价重挫13%，创2025年4月以来最大单日跌幅 | 回调是健康调整还是趋势反转，取决于下周CPI数据和AI公司资本开支指引 |
| 博通财报指引不及预期，刺破"AI受益股坚不可摧"神话 | 高盛认为这是获利了结，标普500回调2%时买入历史上都有回报 |
| 强劲非农数据使利率互换市场完全定价年内加息 |  |

**📖 主编点评**

如果你持有AI相关仓位，不要恐慌性抛售。这次回调的导火索是宏观数据而非AI基本面恶化。关注下周美光是否澄清HBM4订单情况，以及博通电话会是否给出更清晰的AI收入指引。对于你的个人项目，内存芯片价格波动可能影响你搭建本地AI服务器的成本。

📺 [打开原文](https://wallstreetcn.com/articles/3774007)

---

### 5. 台积电CEO："很久才能满足客户需求"，但承诺不涨价

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Jowi Morales_

台积电CEO魏哲家在股东大会上表示，AI需求远超产能，"需要很长时间才能满足客户需求"。但他同时承诺保持价格稳定，不会涨价。这一表态为AI芯片供应链吃紧定调，但暂时缓解了市场对成本上涨的担忧。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 台积电CEO表示产能无法满足AI客户需求，需很长时间才能匹配 | 不涨价可能挤压台积电自身利润率，长期不可持续 |
| 承诺保持价格稳定，不会实施涨价 | 产能瓶颈可能促使客户转向三星或Intel代工 |
| AI hyperscaler需求持续超出预期 | 对英伟达等无晶圆厂公司是利好，成本端压力减轻 |
| 3nm/5nm产能利用率接近满载 |  |

**📖 主编点评**

台积电不涨价对AI芯片公司是利好，但产能瓶颈意味着你如果想买RTX 5090或专业卡，可能还要等很久。对于你的Side Project，如果依赖云端GPU推理，短期内价格不会因芯片成本下降而降低。建议关注台积电是否会在下半年调整定价策略。

📺 [打开原文](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-ceo-c-c-wei-says-it-will-be-a-long-time-before-we-can-meet-customer-demand-tells-shareholders-that-he-will-keep-prices-stable-refrain-from-implementing-price-hikes)

---

## 🌟 大厂 AI 动态

### 3. Anthropic年化营收达470亿美元，Daniela Amodei在IPO前回应AI回报质疑

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _Marina Temkin_

Anthropic CFO Daniela Amodei在IPO路演前接受专访，透露公司年化营收已从2025年底的90亿美元飙升至470亿美元。她表示对AI投资回报率充满信心，并驳斥了市场对AI泡沫的担忧。Anthropic已秘密提交IPO文件，预计将成为2026年最受瞩目的科技IPO之一。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Anthropic年化营收从2025年底的约90亿美元增长至2026年5月的470亿美元 | 470亿美元年化营收的可持续性存疑，部分可能来自一次性大单 |
| 公司已秘密提交IPO文件，预计近期正式启动路演 | IPO定价将是对AI行业估值的重要锚定，可能影响整个AI板块 |
| Daniela Amodei在专访中表示AI投资回报率被低估 | Anthropic与SpaceX的算力协议存在利益冲突（马斯克同时控制xAI） |
| Anthropic与SpaceX签署每月12.5亿美元的算力租赁协议 |  |

**📖 主编点评**

Anthropic IPO是你作为AI产品玩家需要密切跟踪的事件。如果定价合理，可以考虑参与打新——但注意其营收高度依赖Claude API调用，一旦开源模型追上，护城河可能变窄。对你的content-curator项目来说，关注Anthropic IPO后是否会降低API价格，这将直接影响你的项目运营成本。

📺 [打开原文](https://techcrunch.com/2026/06/04/ahead-of-its-ipo-anthropics-daniela-amodei-shrugs-off-doubts-about-ais-returns/)

---

## 🌟 股票

### 4. SpaceX签下700亿美元算力大单：与Anthropic和谷歌达成租赁协议，ARR达260亿美元

**[股票]** · ⭐⭐⭐⭐ · _华尔街见闻 API_

SpaceX相继与Anthropic（每月12.5亿美元）和谷歌（每月9.2亿美元）签署算力租赁协议，合计ARR约260亿美元。这为其计划融资750亿美元的IPO提供强劲收入支撑。但Morningstar估值仅780亿美元，仅为IPO目标价的一半，引发估值争议。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| SpaceX与Anthropic签署每月12.5亿美元的算力租赁协议 | 算力租赁ARR能否持续取决于AI需求是否降温 |
| SpaceX与谷歌签署每月9.2亿美元的算力租赁协议 | SpaceX同时运营xAI，与Anthropic存在潜在利益冲突 |
| 合计年化经常性收入（ARR）约260亿美元 | Fidelity已将IPO最低投资额从50万美元降至2000美元，散户参与度可能影响定价 |
| Morningstar估值SpaceX为780亿美元，仅为IPO目标的一半 |  |

**📖 主编点评**

SpaceX IPO是2026年最大的散户投资事件。但Morningstar的估值警示你：不要被马斯克的故事迷惑。如果你打算参与，建议只投入你能承受归零的资金。对于你的项目，关注SpaceX算力租赁业务是否会影响Starlink的消费级服务价格。

📺 [打开原文](https://wallstreetcn.com/articles/3774016)

---

## 📋 备选池

### AI

- [Anthropic：Claude现在编写超过80%的合并代码，警告递归自我改进风险](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-claude-now-writes-more-than-80-percent-of-its-merged-code) —— Anthropic内部报告显示Claude已主导自身代码编写，同时呼吁建立前沿AI暂停机制——既是技术里程碑也是IPO前的风险提示。
  _Tom's Hardware_
- [NSA被曝使用Anthropic Mythos进行网络攻击，6名Anthropic工程师嵌入该机构](https://www.tomshardware.com/tech-industry/artificial-intelligence/nsa-using-clause-mythos-for-offensive-cyber-operations-report-claims-says-half-a-dozen-anthropic-engineers-embedded-inside-the-agency) —— AI军事化应用加速，Anthropic与NSA的合作可能影响其IPO合规审查。
  _Tom's Hardware_
- [Reid Hoffman离开微软董事会，全职投入AI药物发现初创Manus](https://techcrunch.com/2026/06/05/reid-hoffman-is-leaving-microsofts-board-to-go-founder-mode-with-startup-manus/) —— LinkedIn联合创始人从微软董事会抽身，All in AI+生物——信号：AI制药赛道正在吸引顶级人才。
  _TechCrunch_
- [Google将每月向SpaceX支付9.2亿美元算力费](https://techcrunch.com/2026/06/05/google-will-pay-spacex-920m-per-month-for-compute/) —— Google成为SpaceX算力租赁第二大客户，显示云巨头对GPU的渴求已突破传统供应商边界。
  _TechCrunch_

### AI 算力 / 半导体

- [Nvidia RTX Spark正式发布：面向个人电脑的AI芯片](https://www.nvidia.com/en-us/products/rtx-spark/) —— Nvidia将AI推理能力带入PC端，RTX Spark系列可能改变本地AI部署格局——你的下一台笔记本可能自带专用AI核。
  _Nvidia_
- [微软推出NVIDIA版Surface Laptop Ultra，对标MacBook Pro](https://www.windowslatest.com/2026/06/01/microsoft-builds-its-ultimate-macbook-pro-rival-with-the-nvidia-powered-surface-laptop-ultra/) —— 微软首次在Surface中搭载NVIDIA GPU，AI PC战事升级——对开发者意味着本地运行大模型成为可能。
  _Windows Latest_
- [行业联盟敦促特朗普政府解决AI数据中心导致的内存芯片短缺](https://www.tomshardware.com/tech-industry/artificial-intelligence/industry-coalition-urges-trump-administration-to-take-urgent-action-as-ai-data-centers-extreme-memory-consumption-threatens-other-industries-ai-driven-memory-chip-shortage-could-raise-prices-in-automotive-medical-telecommunications-sectors) —— 9家美国贸易协会警告AI数据中心正在吞噬DRAM产能，汽车、医疗等行业面临芯片涨价——这是你买不到便宜内存的深层原因。
  _Tom's Hardware_

### 股票

- [SpaceX IPO获超额认购，预计6月12日开盘交易](https://wallstreetcn.com/articles/3774001) —— 史上最大IPO进入倒计时，但散户入场门槛已降至2000美元——注意估值泡沫风险。
  _华尔街见闻_
- [S&P拒绝为SpaceX等超级IPO修改指数快速纳入规则](https://www.bloomberg.com/news/articles/2026-06-04/s-p-dow-jones-keeps-megacap-ipo-rules-as-is-after-consultation) —— SpaceX无法立即纳入标普500，被动基金不会被迫接盘——短期抛压可能来自散户获利了结。
  _Bloomberg_
- [美国5月科技行业裁员38,242人，AI是最主要原因](https://www.tomshardware.com/tech-industry/artificial-intelligence/tech-sector-cut-us-jobs-by-38242-in-may) —— AI替代效应开始显性化，信息业岗位自2022年峰值已净流失超30万个——你的职业规划需要考虑AI原生技能。
  _Tom's Hardware_
- [特朗普表态支持美国政府持有顶级AI公司股权，考虑向公众分配收益](https://wallstreetcn.com/articles/3774004) —— "AI全民红利"从韩国传到美国，但前白宫AI主管Sacks警告这可能导致"国有化"风险。
  _华尔街见闻_

### 大厂 AI 动态

- [Supabase估值8个月翻倍至100亿美元，受益于AI编程工具生态](https://techcrunch.com/2026/06/05/supabase-doubles-valuation-to-10b-in-8-months/) —— 开源BaaS平台因Claude Code/Codex等AI编程工具的普及而爆发——你的Side Project后端可以优先考虑Supabase。
  _TechCrunch_
- [Airbnb CEO Brian Chesky计划成立新AI实验室](https://techcrunch.com/2026/06/04/airbnbs-brian-chesky-plans-to-launch-a-new-ai-lab/) —— 非传统AI公司也开始自建AI研发能力，说明AI人才争夺战从大厂蔓延至各行业。
  _TechCrunch_
- [Google Gemini CLI将于6月18日停止服务，迁移至Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) —— 如果你在用Gemini CLI做自动化脚本，只剩两周迁移时间——注意检查Antigravity CLI的兼容性。
  _Google Developers Blog_

### 金融

- [美国5月非农超预期，利率互换市场完全定价年内加息](https://wallstreetcn.com/articles/3774008) —— 高盛放弃降息预测，花旗成为唯一仍坚持年内降息三次的投行——宏观环境对高估值科技股不利。
  _华尔街见闻_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
