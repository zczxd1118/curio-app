# Curio 趋势雷达 · 2026-08-05

> 你的私人主编 · 今日跨域精选 5 条头条 + 14 条备选

_AI 算力与股市冰火两重天：一边是 DeepSeek 重启融资、SpaceX 首份季报显示 AI 烧钱凶猛，另一边是德州暂停数据中心并网、存储价格暴涨引发连锁反应。对做 Agent 的你，DeepSeek V4 Flash 接入 Claude Code 的实测和开源模型安全报告更值得关注。_

---

## 🌟 AI

### 1. DeepSeek V4 Flash 实测：Claude Code 接入后连续开发 7 个项目，逼近 Opus 4.8？

**[AI]** · ⭐⭐⭐⭐⭐ · _AI超元域_

DeepSeek 发布 V4 Flash 0731，284B 总参数、13B 激活、100 万上下文，官方基准接近 Claude Opus 4.8。UP 主在 Claude Code 里接入后连做 7 个项目，发现代码生成任务耗时数十分钟，疑似新模型上线算力拥堵。这是国产模型首次在 Agent 场景下如此接近前沿闭源。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DeepSeek V4 Flash 0731 发布，284B 总参数、13B 激活参数、100 万 Token 上下文 | 官方基准接近 Opus 4.8，但真实 Agent 场景是否稳定尚需更多测试 |
| 官方基准表现接近 Claude Opus 4.8，且为最便宜的国产模型之一 | 耗时数十分钟是算力拥堵还是模型本身推理慢，需要后续复测确认 |
| UP 主在 Claude Code 中接入后连续开发 7 个项目，基础指令、24 点运算、密码锁逻辑推理全部答对 | 与 Kimi K3 的对比是否公平，取决于测试用例和配置是否一致 |
| 代码生成任务统一耗时数十分钟，判断为新模型上线调用高峰算力拥堵 | 国产模型在 Agent 工具链的兼容性（如 Claude Code）是否已成熟，仍需观察 |
| 对比 Kimi K3 后优缺点明显，自制桌面操作系统成品完整性不及 Codex 平台 | 价格优势能否持续，取决于 DeepSeek 后续的定价策略和算力成本 |

**📖 主编点评**

你正在做 content-curator 这个 Agent 项目，DeepSeek V4 Flash 可能是降低 API 成本的关键。建议在 Claude Code 里配好 cc-switch，实测一下你的工作流，重点看长任务耗时和代码质量。如果算力拥堵缓解，这可能是目前性价比最高的国产模型。

📺 [打开原文](http://www.bilibili.com/video/av117014605731815)

---

## 🌟 AI 算力 / 半导体

### 2. 德州暂停 1800 个数据中心并网：474GW 电力请求是峰值纪录 5 倍，AI 基建撞上电网墙

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Jowi Morales_

德州州长 Abbott 指示 PUCT 和 ERCOT 暂停所有数据中心并网申请，直到完成审计。474GW 的电力请求是峰值纪录的 5 倍，这个数字比美国全国发电能力还高。AI 算力扩张第一次在物理世界撞上硬约束。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 德州州长 Greg Abbott 指示 PUCT 和 ERCOT 暂停所有数据中心并网申请 | 审计结果和恢复并网的时间表尚不明确 |
| 474GW 电力请求是峰值纪录的 5 倍，涉及 1800 个数据中心 | 其他州可能跟进类似限制，影响全国数据中心布局 |
| 暂停将持续到完成对数据中心开发商提交信息的审计 | 电力短缺是否会推高 AI 算力成本，进而影响模型价格 |
| 此前德州被宣传为 AI 中心，宽松监管和充足电力是卖点 | 对现有数据中心项目的影响程度需要评估 |
|  | 是否会导致算力向海外转移，值得关注 |

**📖 主编点评**

这对你意味着 AI 算力成本可能上升，尤其是如果你依赖美国数据中心。短期看，模型 API 价格可能上涨；长期看，算力地理分布会变化。做 Agent 项目时，建议多关注国产算力和边缘部署方案，降低成本风险。

📺 [打开原文](https://www.tomshardware.com/tech-industry/data-centers/texas-slams-on-the-breaks-for-1-800-data-centers-power-grid-requirements-are-five-times-higher-than-peak-record-demand-474-gigawatts-of-power-requests-are-now-subject-to-new-moratorium)

---

## 🌟 大厂 AI 动态

### 3. Anthropic 签下 100 亿美元云协议：AI 算力军备竞赛白热化，Volta 成新贵

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Lucas Ropek_

Anthropic 与 AI 云初创 Volta 达成 100 亿美元合作，这是其近期一系列云合作的最新动作。此前 Anthropic 已与 Google、AWS 等有合作，如今转向初创云厂商，显示算力需求远超传统云供给。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Anthropic 与 AI 云初创 Volta 签署 100 亿美元协议 | 协议的具体内容和期限未披露 |
| 这是 Anthropic 近期一系列云合作的最新一笔 | Volta 的算力来源和可持续性存疑 |
| Volta 是一家专注于 AI 算力的云初创公司 | Anthropic 是否在分散云供应商风险 |
| Anthropic 此前已与 Google、AWS 等有合作 | 对传统云厂商（AWS、Google）的影响有待观察 |
|  | 100 亿美元的投资回报周期和盈利能力未知 |

**📖 主编点评**

Anthropic 在算力上砸重金，说明 Claude 系列模型的需求远超预期。对你来说，Claude Code 等工具可能会更稳定，但 API 价格短期难降。做 Agent 项目时，可以关注 Anthropic 的模型更新，同时考虑多模型备份。

📺 [打开原文](https://techcrunch.com/2026/08/04/anthropic-signs-10-billion-deal-with-ai-cloud-startup-volta/)

---

## 🌟 股票

### 4. DeepSeek 重启融资：投前估值 5000 亿元，计划募资 500 亿，8 月下旬签约

**[股票]** · ⭐⭐⭐⭐ · _华尔街见闻 API_

据报道，DeepSeek 重启第二轮融资，投前估值 5000 亿元，计划募资 500 亿元，8 月下旬完成签约。若成功，两轮融资总额将超 1000 亿元。此前暂停融资是因为创始人梁文锋对网上言论不满。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DeepSeek 重启第二轮融资，投前估值 5000 亿元 | 融资是否顺利完成存在不确定性 |
| 计划募资 500 亿元，8 月下旬完成签约 | 5000 亿估值是否合理，取决于后续商业化进展 |
| 若成功，两轮融资总额将超 1000 亿元 | 梁文锋的态度是否会影响融资进程 |
| 此前暂停融资，原因与创始人梁文锋对网上言论不满有关 | 资金用途（算力、研发、人才）未明确 |
|  | 对国产 AI 竞争格局的影响需观察 |

**📖 主编点评**

DeepSeek 融资成功意味着国产模型将有更多资源投入研发，V4 Flash 这类高性价比模型会更多。对你的 Agent 项目是利好，可以期待更便宜的 API 和更好的模型。但也要注意，估值高企可能带来泡沫风险。

📺 [打开原文](https://wallstreetcn.com/articles/3778712)

---

## 🌟 金融

### 5. Troy Hunt 再谈钓鱼：FedEx 案例揭示邮件安全漏洞，为何我们总被钓

**[金融]** · ⭐⭐⭐ · _stymaar_

安全专家 Troy Hunt 发文，以 FedEx 为例剖析钓鱼邮件为何屡屡得手。他展示了攻击者如何利用合法服务和邮件协议漏洞，绕过传统安全措施。这篇文章虽是 2024 年的，但在 AI 生成钓鱼邮件泛滥的当下，重新引发关注。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Troy Hunt 以 FedEx 为例分析钓鱼攻击手法 | AI 生成钓鱼邮件的威胁是否被夸大 |
| 攻击者利用合法服务和邮件协议漏洞 | 传统邮件安全措施（SPF、DKIM、DMARC）是否足够 |
| 文章在 Hacker News 上获得 266 分，重新引发讨论 | 企业是否在安全培训上投入不足 |
| 文章标注为 2024 年发布，但内容仍具现实意义 | 个人用户如何有效防范此类攻击 |
|  | 平台（如 Gmail）的过滤机制能否跟上攻击演变 |

**📖 主编点评**

你在做 Agent 项目，可能会处理用户数据或与外部服务交互，需要警惕钓鱼攻击。建议在项目中实现邮件验证和链接安全检查，同时关注 Troy Hunt 的 Have I Been Pwned 等工具，增强安全性。

📺 [打开原文](https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/)

---

## 📋 备选池

### AI

- [Claude Code 封号原因曝光：Anthropic 植入隐形代码标记中国用户？](http://www.bilibili.com/video/av116844031774993) —— 逆向发现 Anthropic 在客户端藏了用户标记系统，涉及封号机制，对国内用户影响大，但需验证真实性。
  _程序员鱼皮_
- [OpenAI 和苹果互撕：苹果起诉 OpenAI 窃取商业机密，OpenAI 否认](https://www.tomshardware.com/tech-industry/big-tech/apple-is-getting-this-wrong-says-openai-startup-blasts-iphone-maker-over-lawsuit-alleging-it-stole-confidential-information-through-ex-apple-employees) —— 苹果称更多前员工可能将机密带给 OpenAI，OpenAI 回应“没有也不想要”，法律战升级。
  _Jowi Morales_

### AI 算力 / 半导体

- [AMD 数据中心收入翻倍，游戏业务暴跌 31%](https://www.tomshardware.com/tech-industry/amd-doubles-data-center-revenue-year-over-year-but-gaming-revenue-plunged-by-31-percent-ceo-lisa-su-says-prices-have-weighed-on-consumer-demand-but-is-optimistic-about-client-market) —— Q2 营收创纪录，数据中心业务同比翻倍至 67 亿美元，但游戏业务拖后腿，Lisa Su 对客户端市场乐观。
  _Jake Roach_
- [美国考虑禁止中国光模块进入数据中心，中国称将反制](https://www.tomshardware.com/tech-industry/data-centers/us-mulling-ban-on-key-chinese-networking-tech-in-data-center-component-crackdown-white-house-wants-to-impose-restrictions-in-2026-china-says-it-will-respond-if-necessary) —— FCC 起草禁令，限制中国光收发器，可能影响数据中心供应链，2026 年实施。
  _Jowi Morales_
- [Kioxia 和 SanDisk 展示 332 层 3D NAND，密度创纪录](https://www.tomshardware.com/pc-components/ssds/kioxia-and-sandisk-demonstrate-the-worlds-highest-density-3d-nand-flash-332-active-layers-and-up-to-4-800-mt-s-interface) —— BiCS10 3D QLC NAND，面积密度超 37 Gbit/mm²，存储技术持续突破。
  _Anton Shilov_

### 大厂 AI 动态

- [SpaceX 首份季报：AI 收入超太空业务，星链日赚 1800 万，AI 日烧 1.7 亿](https://techcrunch.com/2026/08/04/spacex-doubles-revenues-on-anthropic-and-google-compute-deals-starlink-growth/) —— 营收同比增 92% 至 78 亿美元，AI 资本开支 158 亿，马斯克在星链盈利和 AI 烧钱间走钢丝。
  _Sean O'Kane_
- [Gemini 3.6 Flash 等新模型发布，温度等参数被弃用](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/) —— Google 发布 Gemini 3.6 Flash 等，API 弃用 temperature/top_p/top_k，开发者需调整。
  _logickkk1_
- [Gemini Robotics 2 带来全身智能，机器人领域新突破](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/) —— DeepMind 发布 Gemini Robotics 2，提升机器人全身控制能力，未来应用可期。
  _ai2027_

### 股票

- [高盛：超大型科技股垄断瓦解，15 年市场集中度拐点已现](https://wallstreetcn.com/articles/3778721) —— 高盛警告美股集中度拐点，资本开支侵蚀现金流，建议多元化配置，关注日本、欧洲、新兴市场。
  _华尔街见闻 API_
- [马斯克谈存储涨价：供给增 20%，需求增 200%，价格当然涨](https://wallstreetcn.com/articles/3778717) —— 存储价格暴涨逻辑清晰，高盛交易员称除非三星 2027 亏损，否则股价下行有限。
  _华尔街见闻 API_
- [韩国警方立案调查三星、SK海力士 CEO，涉嫌背信罪](https://wallstreetcn.com/articles/3778723) —— 少数股东投诉 CEO 将营业利润与奖金挂钩未经股东大会批准，警方已立案。
  _华尔街见闻 API_

### 金融

- [高盛上调中国大模型收入预期至 130 亿美元，Agent 驱动 Token 消费](https://wallstreetcn.com/articles/3778709) —— 中国模型连续 14 周包揽 OpenRouter 前五，成本优势 4-8 倍，收入兑现加速。
  _华尔街见闻 API_
- [德州暂停数据中心并网，AI 电力危机加剧](https://techcrunch.com/2026/08/04/texas-halts-new-data-centers-as-governor-calls-for-audits/) —— 474GW 电力请求是峰值 5 倍，州长要求审计，数据中心扩张遇阻。
  _Tim De Chant_
- [Stripe 和 Advent 联合收购 PayPal，报价超 530 亿美元](https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/) —— 支付领域重大并购，Stripe 联手 Advent 提出收购 PayPal，交易金额巨大。
  _rvz_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
