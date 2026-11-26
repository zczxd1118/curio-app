# Curio 趋势雷达 · 2026-11-26

> 你的私人主编 · 今日跨域精选 5 条头条 + 15 条备选

_今天最重要的两条线：一是 Nvidia 的治理危机从丑闻升级成信用事件——S&P 考虑下调评级、董事会独立性遭质疑、Huang 复职被国会炮轰，同时出口禁令下的 B300 服务器仍在中国公开叫价 340 万美元；二是 Anthropic IPO 上市即破发，跌破 83 美元发行价，AI 泡沫叙事第一次有了可量化的价格。对你来说，模型榜单的噪音（Gemini 4 各种代号）远不如这两条真实。_

---

## 🌟 AI 算力 / 半导体

### 1. 禁运的 Blackwell B300 服务器在中国公开叫价 340 万美元，溢价 5-6 倍

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

Tom's Hardware 今天实测发现，被美国出口管制的 Nvidia Blackwell B300 整机在中国市场可以公开买到，报价最高 340 万美元，是美国本土价的 5-6 倍。这不是暗网传闻，是能直接询价的现货。管制执行的不均匀，正在把算力变成一种有明确黑市汇率的商品。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| B300 整机在中国可公开询价，最高报价 340 万美元 | 这些现货的真实来源尚不清楚，可能是转口贸易、拆机件或库存灰色渠道 |
| 溢价幅度为美国本土价的 5-6 倍 | 溢价能否长期维持取决于下一轮管制收紧的力度，目前无公开数据 |
| 同期 Megaspeed（前 Nvidia 合作方）被美国商务部列入出口禁令名单 | 买方结构未知，无法判断是训练集群刚需还是囤货投机 |
| Nvidia 已停止单独披露新加坡地区销售额，总营收达 1040 亿美元 | 如果管制进一步收紧，黑市价格可能继续走高而非回落 |

**📖 主编点评**

这条对你有两层用处。一是做 content-curator 时，算力供给的灰色地带是比模型榜单更硬的选题——它直接决定你调 API 的成本曲线。二是如果你以后要做推理部署相关的 side project，记住国内拿卡的真实成本是官方价的 5 倍以上，任何'本地跑大模型'的方案都要把这个数字算进去。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/export-banned-nvidia-blackwell-b300-servers-are-openly-for-sale-in-china-for-up-to-usd3-4-million-a-5x-to-6x-markup-over-u-s-prices)

---

## 🌟 股票

### 2. Anthropic 跌破 83 美元发行价，1.5 万亿美元估值的上市叙事开始瓦解

**[股票]** · ⭐⭐⭐⭐⭐ · _Reuters_

Reuters 报道，Anthropic 在创纪录上市后迅速反转，股价跌破 83 美元的 IPO 发行价。此前定价对应 1.5 万亿美元估值，承销银行甚至已平掉用于稳定股价的仓位。同一天 Nasdaq 恢复抛售，Nvidia 与 Anthropic 双双下挫。这是 AI 泡沫论第一次拿到一个可交易的价格证据。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Anthropic IPO 定价 83 美元/股，对应约 1.5 万亿美元估值 | 跌破发行价是否代表长期估值重估，还是上市初期的正常波动，需要看未来两周成交量 |
| 上市后股价跌破发行价 | 1.5 万亿估值对应的收入模型尚未被公开验证 |
| 承销银行已关闭用于稳定股价的仓位 | Dario Amodei 回应'交出人类控制权'的指控称其荒谬，但安全叙事与商业估值的张力仍在 |
| IPO 文件披露季度人力成本 17 亿美元，人均月成本约 10.7 万美元 | AI 板块整体回调是否会传导到一级市场融资，目前只有信号没有结论 |
| 信用评级机构给出高收益级（垃圾级）评级预期 |  |

**📖 主编点评**

你不需要关心股价，但要关心它背后的信号：头部 AI 公司的估值开始被公开质疑，意味着 2027 年的融资环境会比 2026 年紧。如果你打算把 content-curator 做成简历亮点，现在正是把'能落地的工程能力'讲清楚的时候——泡沫期讲愿景，退潮期讲交付。

📺 [打开原文](https://www.reuters.com/business/anthropic-breaks-below-83-ipo-price-debut-rally-unravels-2026-11-24/)

---

## 🌟 大厂 AI 动态

### 3. OpenAI 合并 Chat 与 Work，重度用户会更早撞上用量上限

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _TechCrunch_

OpenAI 宣布把 ChatGPT 的 Chat 和 Work 两个体验合并，并引入统一的用量计量表。官方明确说，重度用户会比以前更早触达限额。这是把'聊天'和'干活'当成同一种消耗品来计费，对每天拿它跑 Agent 的人是直接的成本信号。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Chat 与 Work 体验将合并为单一产品 | 具体的限额数值和重置周期尚未公布 |
| 引入跨 ChatGPT 的统一用量计量 | 是否会影响 API 计费体系目前未知，可能只针对订阅端 |
| OpenAI 明确表示重度用户会更早触达上限 | 合并后 Work 侧的 Agent 能力是否保留完整，需要实测 |
|  | 对第三方 Agent 工具（依赖 ChatGPT 订阅额度）的连带影响不明 |

**📖 主编点评**

如果你在 content-curator 里用 ChatGPT 订阅额度跑批处理，现在就该做两件事：一是把用量监控加进工作流，二是准备一个 API 直连的降级路径。统一计量意味着'聊天'和'跑 Agent'抢同一份配额，你的自动化任务可能被日常对话挤掉。

📺 [打开原文](https://techcrunch.com/2026/11/25/openai-says-heavy-chatgpt-users-may-hit-limits-sooner-as-it-merges-chat-and-work/)

---

## 🌟 AI

### 4. T3 Code：开源 AI IDE，一条指令拉起多个 Agent 线程并行改代码

**[AI]** · ⭐⭐⭐⭐ · _AI超元域_

T3 Code 是一个新出的开源 AI IDE，核心卖点是统一调度 Claude Code、Codex、Pi、Antigravity 等多个订阅，一条指令拉起多个 AI 线程并行改同一项目，还能从手机下发任务。视频是完整的安装到多 Agent 工作流实战，重点讲了代码改动如何隔离。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| T3 Code 开源，可统一调度 Claude Code、Codex、Pi、Antigravity 等 | 多 Agent 并行改同一仓库的冲突解决机制，视频未给出完整技术细节 |
| 支持一条指令拉起多个 AI 线程并行处理同一项目 | '比 Orca 更好用'是 UP 主主观判断，缺横向基准 |
| 支持手机端下发任务 | 开源项目的维护活跃度和长期可持续性未知 |
| 视频覆盖从安装配置到多 Agent 工作流的完整流程 | 实际吞吐提升是否抵消多线程的合并成本，需要自己跑一遍 |

**📖 主编点评**

这正好踩在你的偏好上：多 Agent 编排 + 真实工作流。建议你花一个周末实测 T3 Code 的改动隔离机制——如果它真能干净地并行跑多个 Agent，content-curator 的采集/摘要/渲染三段可以拆成并行线程，这是能写进简历的具体优化。别只看视频，自己跑一遍才知道坑在哪。

📺 [打开原文](http://www.bilibili.com/video/av117671802705979)

---

## 🌟 金融

### 5. 美联储开始担心 AI Agent 会引发挤兑

**[金融]** · ⭐⭐⭐ · _Gizmodo_

Gizmodo 报道，美联储内部已在讨论 AI Agent 集中执行提款或转账指令可能引发的系统性风险——当成千上万个 Agent 在同一信号下同时行动，挤兑的速度会远超人类反应时间。这是监管层第一次把 Agent 当成金融稳定变量来对待。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 美联储已就 AI Agent 可能触发银行挤兑展开讨论 | 目前处于讨论阶段，没有任何监管草案或时间表 |
| 关注点是 Agent 在高频、同质化指令下的集体行为 | Agent 行为的同质化程度缺乏实证数据 |
|  | 是否会被纳入现有算法交易监管框架尚不明确 |
|  | 对个人开发者使用金融类 Agent 的合规边界没有说明 |

**📖 主编点评**

这条标 is_diverse，因为它不在你的舒适区，但值得看。你做 Agent 项目时迟早会碰'多个 Agent 同时调用外部 API'的场景，美联储的担忧本质是同一个工程问题：并发 Agent 的幂等性和限流。把这个思路提前设计进 content-curator 的采集层，比事后补锅便宜得多。

📺 [打开原文](https://gizmodo.com/the-fed-is-worried-ai-agents-could-trigger-a-bank-run-2000840566)

---

## 📋 备选池

### AI 算力 / 半导体

- [Nvidia 董事会恢复黄仁勋 CEO 职务，国会称'品格失败'](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html) —— 治理危机的核心事件，但已被头条的 B300 黑市和 S&P 评级覆盖，单看这条信息密度不够。
  _CNBC_
- [S&P 考虑因治理与'关键人风险'下调 Nvidia 信用评级](https://techcrunch.com/2026/11/25/sp-considers-nvidia-credit-downgrade-over-governance-and-key-man-risks/) —— 丑闻升级成信用事件的标志，AA- 是第四高评级，值得知道但缺后续数据。
  _TechCrunch_
- [TSMC 提交 226 亿美元德州建厂申请，2031 年前不产 2nm 级芯片](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-files-for-usd22-6-billion-texas-fab-campus-with-local-tax-breaks-just-one-county-over-from-musks-terafab-proposed-brazos-county-plant-wont-make-2nm-class-chips-until-2031) —— 时间线是关键：2031 年才量产 2nm，说明美国本土先进制程的落地比宣传慢得多。
  _Tom's Hardware_
- [AMD 用 AI 把冷内存页挪到闪存，缓解 DRAM 短缺](https://www.eetimes.com/amd-tackles-dram-shortages-with-ai-and-flash-storage/) —— MEXT 方案有工程细节，但对你当前项目关联度低，留作技术储备。
  _EE Times_

### 大厂 AI 动态

- [FCC 批准 SpaceX 在太空部署 AI 数据中心的计划](https://techcrunch.com/2026/11/25/fcc-approves-spacex-plan-to-put-ai-data-centers-in-space/) —— 监管放行是事实，但离落地很远，属于'知道就好'的新闻。
  _TechCrunch_
- [42 州总检察长试图阻止 Character.AI 出售用户聊天记录](https://www.theverge.com/policy/1042620/character-ai-sale-state-ags-block-selling-users-chats) —— 破产清算中 2100 万美国账户数据被摆上货架，AI 产品数据合规的警示案例。
  _The Verge_
- [Dario Amodei 称'向 AI 交出人类控制权'的指控荒谬](https://techcrunch.com/2026/11/25/anthropics-dario-amodei-calls-accusations-of-surrendering-human-control-to-ai-absurd/) —— 符合你想多看名人访谈的偏好，但这是回应式表态而非深度对话，密度不够上头条。
  _TechCrunch_
- [Amazon 与 Meta 据称在谈解除对 AI Agent Muse 的封锁](https://techcrunch.com/2026/11/25/amazon-and-meta-reportedly-in-talks-to-lift-blockade-on-ai-agent-muse/) —— Agent 生态的封锁与解封值得跟踪，但目前只有'据称'，缺硬事实。
  _TechCrunch_

### 股票

- [Nasdaq 抹平 2026 年全部涨幅](https://www.cnbc.com/2026/11/19/stock-market-today-live-updates.html) —— Anthropic 破发的宏观背景，单条信息量低，但和头条 2 一起看有意义。
  _CNBC_
- [两名 Polymarket 账户在黄仁勋复职事件上赚超 34 万美元](https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-23-2026/card/two-groups-of-polymarket-accounts-made-over-340-000-on-huang-comeback-Lan2T0TwbJPNsyhmQHGq) —— 预测市场的'可疑集群'，内幕交易味道浓，但属于八卦级信息。
  _WSJ_

### 金融

- [Visa、Mastercard、JPMorgan 客户数据被黑客泄露](https://www.wsj.com/finance/banking/visa-mastercard-and-jpmorgan-customer-data-leaked-by-hackers-3b5a0f87) —— 支付巨头数据泄露，安全事件但缺技术细节，适合快速扫一眼。
  _WSJ_
- [Oracle 申请发行 200 亿美元股票与债券为 AI 建设融资](https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html) —— AI 基建融资的典型案例，但发布于三周前，新颖度不足。
  _CNBC_
- [arXiv：任务复杂度如何降低初级岗位被 AI 替代的风险](https://arxiv.org/abs/2611.34099) —— 直接关联你'大四找工作'的处境，结论是复杂任务更难被替代，值得读全文。
  _arXiv_

### AI

- [Claude Code 从 0 到 1 全攻略：权限、MCP、Skills、Hooks、子智能体](http://www.bilibili.com/video/av117642291582518) —— 覆盖你关心的全部工程点，但属于教程合集，密度不如 T3 Code 的实战视频。
  _大模型分享员_
- [50 分钟速通 Codex，含 DeepSeek 接入、无需 ChatGPT 订阅](http://www.bilibili.com/video/av117671517489403) —— 国内直连方案有实用价值，尤其配合头条 3 的用量限额问题，但内容是教程性质。
  _林粒粒呀_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
