# Curio 趋势雷达 · 2026-11-10

> 你的私人主编 · 今日跨域精选 5 条头条 + 15 条备选

_今天最重要的信号有两个：一是 Nvidia 的 Jensen Huang 与疑似中国间谍的关系被本人承认，董事会启动独立调查、国会传唤、集体诉讼同时压上，Nvidia 股价单日跌超 4%，这不只是八卦，而是直接卡住 Nvidia 对华游说与出口管制的关键变量；二是 AI 资本面同步转向，Nasdaq 一周内跌入回调区间、2.5 万亿美元市值蒸发，Anthropic 却在这时推进 IPO。技术侧则有一条被低估的：Claude Code 的 settings 文件正在 GitHub 上批量泄露密钥。_

---

## 🌟 大厂 AI 动态

### 1. Jensen Huang 承认与疑似中国间谍的婚外关系，Nvidia 董事会启动独立调查，Ben Thompson 判断「他能活下来，但影响力回不去了」

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _Ben Thompson_

Nvidia 董事会已成立独立委员会调查 CEO Jensen Huang 与 Megaspeed 董事 Alice Huang 的关系，Huang 本人向全员发信承认婚外情并道歉。国会中国问题特别委员会已传唤他作证，至少一家律所提起证券欺诈集体诉讼，Nvidia 股价单日跌超 4%。Ben Thompson 在 Stratechery 给出的判断很直接：他希望 Huang 挺过去，但 Huang 在华盛顿的话语权将永久性削弱。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Huang 向全体员工发信承认婚外关系并致歉，董事会成立独立委员会调查 | 调查结论是否触及出口管制合规，目前无任何官方定性 |
| 国会众议院中国问题特别委员会已传唤 Huang 出席作证 | Megaspeed 是否被认定为中国情报资产，美方尚未公开确认 |
| 至少一家律所提起证券欺诈集体诉讼，多家律所跟进调查 | Huang 是否会因此失去 CEO 职位——Stratechery 判断不会，但这是判断不是事实 |
| Nvidia 股价在调查消息后单日下跌超过 4% | 对华 GPU 出口政策会否因此收紧，取决于国会而非公司 |
| 做空机构 Culper Research 早在六个月前就质疑过这层关系 | 集体诉讼能否成立，要看 Nvidia 早期披露是否构成误导 |
| Huang 已临时退出 ElevenLabs Summit 与一场 Anthropic 活动 |  |

**📖 主编点评**

这条对你的实际含义不在八卦，而在算力供给的不确定性：Nvidia 对华政策一旦被国会接管，国内可获得的算力路径（云租赁、黑市 B300、二手 V100）价格与合规风险都会变。如果你在做需要调用海外模型的 Agent 项目，现在就该把「模型供应商可替换」当成架构约束写进设计，而不是等政策落地再改。

📺 [打开原文](https://stratechery.com/2026/jensen-huangs-affair-the-culper-report-huangs-righteousness/)

---

### 3. Claude Code 的 settings 文件正在 GitHub 上批量泄露 API key 和密码，起因是「Do not ask again」这个授权选项

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Kyle Orland_

Ars Technica 报道，大量开发者把 Claude Code 的本地 settings 文件连同密钥一起提交到了公开仓库，泄露内容包括 API key、数据库密码等。根因是 Claude Code 在请求权限时提供的「Do not ask again」选项——用户为了少点几次确认，把敏感路径的访问权限永久放开了，而这些配置随后被 git 带上了 GitHub。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| GitHub 上已发现数千条来自 Claude Code settings 文件的密钥泄露 | 受影响仓库的准确总数尚无权威统计 |
| 泄露内容包含 API key、密码等凭证 | Anthropic 是否会修改默认权限模型，官方未表态 |
| 直接诱因是「Do not ask again」权限选项被广泛使用 | 有多少泄露密钥已被实际利用，目前未知 |
| Ars Technica 已核实多起案例 |  |

**📖 主编点评**

你正在用 Claude Code 做 content-curator，这条是直接冲你来的。现在就去检查两件事：项目里有没有 .claude/settings*.json 被 git 跟踪，以及 .gitignore 有没有覆盖它。另外把「Do not ask again」改成对写操作永远确认——省下的点击次数，不值得用一次密钥泄露换。

📺 [打开原文](https://arstechnica.com/ai/2026/11/claude-code-settings-files-expose-thousands-of-secrets-on-github/)

---

### 5. Meta 发布 Muse Ember：专为 Agent 执行设计的轻量模型，输入价格 0.1 美元/百万 token

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Russell Brandom_

Meta 发布 Muse Ember，定位明确——不是通用对话模型，而是给 Agent 执行用的轻量模型。输入定价 0.1 美元/百万 token，TechCrunch 称其显著低于 Haiku 和 Luna 等前沿竞品。同一天 Anthropic 发布 Claude Fable 5.2 与 Mythos 5.2，主打编码、推理与视觉能力提升。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Muse Ember 输入定价 0.1 美元/百万 token | Ember 在真实 Agent 任务上的工具调用准确率，尚无第三方评测 |
| 官方定位为 Agent 执行场景的轻量模型 | 0.1 美元定价是否可持续，取决于 Meta 的补贴意愿 |
| 价格显著低于 Haiku、Luna 等竞品 | 与 Claude 新模型的对比结论，需要等独立 benchmark |
| 同日 Anthropic 发布 Claude Fable 5.2 与 Mythos 5.2 |  |

**📖 主编点评**

Agent 项目的成本结构正在被重写：当执行层模型降到 0.1 美元/百万 token，你的 content-curator 里那些「跑很多次、每次任务简单」的环节（分类、抽取、格式化）就该换模型了。建议做一次分层：规划用强模型，执行用 Ember 这类便宜模型，先量一下你现在的 token 花在哪一层。

📺 [打开原文](https://techcrunch.com/2026/11/09/meta-releases-muse-ember-a-new-lightweight-model-for-agent-execution/)

---

## 🌟 AI 算力 / 半导体

### 2. Anthropic 花 34 亿美元买下 1.7GW 燃气发电机组，靠接手 Caterpillar 既有订单跳过六年排队

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Newton Gitonga_

Anthropic 与 OnePWR Solutions 达成 34 亿美元交易，拿下 1.7GW 燃气发电容量，方式是直接接手 OnePWR 手上已有的 Caterpillar 订单——因为燃气轮机交付排期已长达六年，新下单等于放弃 2032 年前的算力扩张。同期 Envision 在中国交付了 800MW 的 Galaxy 数据中心园区首期 120MW，用时不到一年，成本约为美国同类项目的五分之一。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 交易金额 34 亿美元，锁定 1.7GW 燃气发电容量 | Anthropic 这笔交易是否划算，取决于天然气价格与碳成本的中期走势，目前无法定论 |
| 通过接手 OnePWR 现有 Caterpillar 订单实现，而非新下单 | 「电力而非 GPU 成为 AI 扩张瓶颈」这个判断正在成型，但还没有成为行业共识 |
| 美国燃气轮机交付排期已达约六年 | 中国以五分之一成本建数据中心，是否可复制到海外，样本只有一个 |
| Envision 在中国交付 800MW 园区首期 120MW，用时不足一年 | 接手他人订单的合规与交付风险，合同细节未公开 |
| Envision 项目成本约为美国同类项目的五分之一 |  |
| Fervo 地热订单簿已达 120 亿美元 |  |

**📖 主编点评**

这条值得你记进长期判断库：AI 基础设施的瓶颈已经从芯片转移到电力和交付周期。做 Agent 产品时，推理成本的中期曲线不该假设「继续线性下降」——供给端被电力卡住时，价格下降会变慢。如果你在算 side project 的长期 API 成本，把这条当风险项。

📺 [打开原文](https://www.tomshardware.com/tech-industry/data-centers/anthropic-skips-six-year-waitlist-with-massive-usd3-4-billion-gas-turbine-generator-deal-firm-takes-over-onepwrs-orders-secures-1-7gw-of-capacity-to-power-ai-data-centers)

---

## 🌟 股票

### 4. 美股两周蒸发 2.5 万亿美元，Nasdaq 跌入回调区间，AI 交易正在被系统性减仓

**[股票]** · ⭐⭐⭐⭐ · _madihaa_

中期选举后市场对 AI 资本开支的定价迅速反转：Nasdaq 单日跌 5% 进入回调区间，两周内美股市值蒸发约 2.5 万亿美元，对冲基金据报已清空 2025 年以来建仓的 AI 股票。Intel 领跌，芯片板块整体承压，被称为 1896 年以来最差的中期选举后交易日。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Nasdaq 单日下跌 5%，进入技术性回调区间 | 这是估值修正还是 AI 泡沫破裂的起点，现在无法判断 |
| 两周内美股市值蒸发约 2.5 万亿美元 | 数据中心相关政策风险是否真会落地，取决于具体立法 |
| 对冲基金据报已卖出 2025 年以来买入的全部 AI 股票 | AI 资本开支的基本面是否已变化，财报数据尚未体现 |
| 芯片股整体重挫，Intel 跌幅居前 |  |
| 民主党中期选举表现超预期被视为数据中心扩张的政策风险 |  |

**📖 主编点评**

别把这条当财经八卦跳过——它决定你未来半年看到的 AI 工具定价。融资环境收紧时，第一批涨价或砍免费额度的就是中小 AI 工具。如果你在选长期依赖的 Agent 工具链，优先选有明确收入模型或大厂背书的，别把工作流押在靠融资烧免费额度的产品上。

📺 [打开原文](https://finlaws.substack.com/p/25t-has-been-wiped-from-us-stocks)

---

## 📋 备选池

### 大厂 AI 动态

- [Anthropic 推进 IPO，本周将确定估值区间](https://techcrunch.com/2026/11/09/anthropic-reportedly-plans-to-move-forward-with-ipo-plans/) —— WSJ 称本周定价，但 Michael Burry 和多家机构公开质疑 1.5 万亿美元估值能否成立——和上面的市场抛售是同一条线。
  _TechCrunch_
- [Anthropic 发布 Claude Fable 5.2 与 Mythos 5.2](https://www.theverge.com/ai-artificial-intelligence/1030005/anthropic-claude-fable-mythos-5-2) —— 官方称在编码、推理、视觉上有提升，但发布稿没给具体 benchmark 数字，等第三方评测再决定要不要迁移。
  _The Verge_
- [Google Gemini 把个人 Drive 文件和邮件路由给人工标注员](https://github.com/thisisme6598/gemini_files/) —— HN 736 分的另一条 Gemini 训练数据争议，和「订阅用户聊天记录也被训练」是同一问题的两面。
  _Hacker News_

### AI 算力 / 半导体

- [DeepX 第二代芯片流片，LPDDR5x-PIM 架构预计 6.7 倍性能提升](https://www.eetimes.com/deepx-tapes-out-second-gen-chip-projects-6-7x-performance-gain-with-lpddr5x-pim/) —— 5W 以内跑端侧大模型，面向机器人市场——存算一体的路线第一次有了可量产的流片样本。
  _EE Times_
- [Nvidia 限制云合作伙伴对华业务占比至 49%](https://www.tomshardware.com/tech-industry/policy/nvidia-cracks-down-on-overseas-cloud-ai-gpu-rentals-for-china-partners-face-51-percent-non-chinese-quota-as-black-market-b300-rack-prices-surge-to-usd2-8-million) —— 黑市 B300 整机柜价格已涨到 280 万美元，这条和头条 1 是同一件事的产业侧后果。
  _Tom's Hardware_
- [律师用 8 张二手 V100 搭私有 AI 服务器，跑 DeepSeek V4.1 Flash 达 215 tokens/s](https://www.tomshardware.com/tech-industry/artificial-intelligence/lawyer-builds-private-ai-server-with-eight-used-nvidia-v100-gpus-up-to-215-tokens-per-second-to-keep-legal-files-offline-costing-about-usd2-400-per-four-gpu-board) —— 2018 年的卡、四卡板约 2400 美元，跑出 215 tokens/s——自建推理的真实成本样本，比任何评测都有参考价值。
  _Tom's Hardware_
- [内存短缺逼手机厂商从旧设备上拆内存重新植球再用](https://www.tomshardware.com/pc-components/dram/memory-shortage-spurs-smartphone-makers-to-melt-used-memory-off-old-devices-then-re-solder-it-onto-new-products-recycled-memory-to-keep-budget-phones-affordable-reballing-adoption-to-double-by-2027) —— DRAM 涨价已经逼出拆机回收内存的产业行为，2027 年采用率预计翻倍——供应链紧张的硬信号。
  _Tom's Hardware_

### 股票

- [Oracle 申请发行 200 亿美元新股与债券，为 AI 基建融资](https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html) —— AI 数据中心建设正在从股权融资转向债务融资，这是资本面对回报周期变长的直接反应。
  _CNBC_
- [Nvidia 与 Micron 两家贡献了美国盈利增长的 34%](https://www.wsj.com/finance/stocks/the-earnings-boom-is-heavily-reliant-on-just-a-handful-of-stocks-21decb53) —— 盈利集中度这么高，解释了为什么 Nvidia 一条负面消息能带动整个 Nasdaq 下跌。
  _WSJ_

### 金融

- [美国联邦预算赤字一年跳增 12%，接近 2 万亿美元](https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html) —— 利率高位叠加赤字扩张，是 AI 基建债务融资成本上升的宏观背景，和 Oracle 发债那条连起来看。
  _Hacker News_
- [3000 亿美元「债务墙」压向 PE 支持的公司](https://www.wsj.com/finance/investing/a-300-billion-debt-wall-is-looming-over-private-equity-backed-companies-d6359497) —— 再融资高峰撞上高利率，AI 泡沫若破，最先倒的是这批杠杆收购的公司。
  _WSJ_
- [Tesla 将逐步停产 Cybertruck](https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817) —— HN 1160 分，销量长期不及预期后的止损；同期 Tesla 与 SpaceX 两日合计蒸发 4200 亿美元市值。
  _NBC News_

### AI

- [Claude 桌面端全攻略：Code、Design、Cowork 三块能力收进同一个客户端](http://www.bilibili.com/video/av117580048108571) —— 11 月 8 日发布，讲的是 Claude Code 从命令行进化成桌面客户端完整形态——对重度用户是本周最实用的更新解读。
  _技术爬爬虾_
- [DeepSeek Harness 实测对比 Claude Code：同一模型下工具链差距有多大](http://www.bilibili.com/video/av117100337236191) —— 用同一个 DeepSeek Pro 模型在两个 harness 里跑相同任务，结论是插件化、缓存命中、流程记录对最终效果影响很大——工程细节够。
  _程序员晓刘_
- [用 Claude Skill 做高质量 PPT 的完整流程](http://www.bilibili.com/video/av116474832361424) —— 基于 Anthropic 的 Claude Design，从装 Skill 到跑出成品全流程，适合直接抄进自己的工作流。
  _阿西_出海_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
