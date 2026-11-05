# Curio 趋势雷达 · 2026-11-05

> 你的私人主编 · 今日跨域精选 5 条头条 + 16 条备选

_今天最重要的信号只有一个：AI 基建的政治与资金地基同时松动。美国中期选举里 45 项数据中心相关公投几乎全线被否，德州翻蓝直接砸了 AI 股；另一边内存涨价把 Apple 制造成本推高 330 亿美元、Team Group CEO 说"钱也买不到货"。算力扩张从"技术问题"变成"选址+电价+选票问题"，这会重塑未来 6-12 个月的产业链节奏。_

---

## 🌟 AI 算力 / 半导体

### 1. 美国中期选举 45 项数据中心公投几乎全被否，AI 基建第一次在选票上输掉

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Jowi Morales_

多个县把数据中心议题直接放上中期选举选票，结果压倒性反对。这不是某个社区的邻避情绪，而是 AI 基建第一次遭遇成规模的政治否决。叠加德州翻蓝导致 AI 股下挫，算力的瓶颈正从芯片转向"能不能建、建在哪、谁买单"。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 45 项数据中心相关措施进入中期选举公投，绝大多数被选民否决 | 被否的项目是否会迁往监管更松的州或海外，尚无数据 |
| 反对跨党派分布，非单一政治阵营议题 | 联邦层面是否会出手预emption（联邦优先权）压制地方否决，未明朗 |
| 同日 AI 相关股票因德州州长选举结果下跌 | 电价与水资源成本是否成为下一轮选址的决定性变量，仍属推测 |
| TechCrunch 与 Ars Technica 均独立报道同一趋势 | AI 资本开支指引是否会在 Q4 财报季被下调，待观察 |
| Stratechery 判断：若美国反对建设是长期性的，影响远超单个项目 |  |

**📖 主编点评**

你如果关注 AI 产业链，别只盯 GPU 出货量——把"电力+选址+地方政治"加进你的观察清单。对做 Agent 产品的你，短期反而是好消息：算力供给紧张会推高推理成本，逼你把 prompt 和上下文做省，这正好是 content-curator 这类项目的护城河。

📺 [打开原文](https://www.tomshardware.com/tech-industry/data-centers/ai-data-centers-comprehensively-defeated-at-us-midterm-elections-45-measures-put-on-the-ballot-as-americans-overwhelmingly-vote-against-developments)

---

### 3. 内存危机升级：Team Group CEO 称明年"钱也买不到货"，价格没有任何下行趋势

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Jowi Morales_

Team Group CEO 陈庆文在财报电话会上说得很直白："什么都没了，价格怎么跌？"AI 数据中心把三星、SK hynix、美光的产能吸向高毛利服务器产品，消费级 DRAM 被挤压。Apple 制造成本因此多出 330 亿美元。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Team Group CEO 在财报电话会警告内存短缺明年加剧，价格无下行趋势 | 涨价周期会持续到 2027 年哪个季度，各家口径不一 |
| Apple 因内存涨价制造成本增加约 330 亿美元 | 消费电子终端价格是否会在假日季明显上调，待观察 |
| 三星、SK hynix、美光优先供应服务器与 HBM，挤压消费级供给 | 国产存储厂商能否填补缺口，缺乏产能数据 |
| Micron 公布激进 DRAM/NAND 路线图，含 3D NAND 与 High-NA EUV | HBM 之外的通用 DRAM 是否会出现二次分配，属推测 |
| Macronix 退出 Nintendo ROM 芯片业务，转产 AI 数据中心用 NOR/NAND |  |

**📖 主编点评**

如果你近期要买笔记本/显卡/SSD，别等降价——这轮是结构性短缺不是周期波动。做 AI 工程时也要把"显存/内存成本"当成设计约束：本地跑模型、RAG 索引规模、上下文长度，都该按"内存贵"来优化。

📺 [打开原文](https://www.tomshardware.com/pc-components/dram/team-group-ceo-warns-memory-crisis-could-reach-point-where-even-money-cant-buy-goods-will-get-worse-next-year-with-no-downward-trend-in-price-whatsoever)

---

## 🌟 大厂 AI 动态

### 2. Meta 收购 AI 编程创业公司 Conductor，卖点是"让工程师调度一队 Agent 并行干活"

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _Lucas Ropek_

Conductor 的核心产品是让软件工程师部署多个 Agent 同时推进项目的不同部分。Meta 直接买下，说明大厂认可的不是"更强的单 Agent"，而是"Agent 编排层"。这对正在做多 Agent 工作流的你，是一条方向确认信号。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Meta 已完成对 AI 编程创业公司 Conductor 的收购 | 收购金额与团队整合方式未披露 |
| Conductor 产品定位是让工程师部署 Agent 团队并行处理项目不同部分 | Conductor 技术是否会并入 Meta 内部工具链还是独立产品，不明 |
| 收购由 TechCrunch 于 2026-11-04 报道 | "Agent 团队并行"在真实大型代码库上的可靠性，缺乏公开评测 |
| 同周 Meta 在 AI 编程方向持续加码 | 这是否会引发其他大厂跟进收购同类编排层公司，属推测 |

**📖 主编点评**

你正在做 content-curator 的多 Agent 编排，这条值得当作"方向被大厂验证"的证据写进简历叙事。具体可借鉴的是它的任务拆分粒度——把"并行"做在任务边界清晰的地方（抓取/筛选/写作），而不是让多个 Agent 抢同一份上下文。

📺 [打开原文](https://techcrunch.com/2026/11/04/meta-acquires-ai-coding-startup-conductor/)

---

### 4. Uber 说最忙的一周里只有 4 个人用 AI Agent 叫车——Agent 落地的冷水

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Sarah Perez_

Uber 披露：上季度最繁忙的一周，全平台只有 4 个人通过 AI Agent 完成叫车。这个数字和满屏的"Agent 元年"叙事形成刺眼对比。它不否定 Agent 技术，但说明"让 Agent 替用户操作真实服务"的链路还远没打通。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Uber 称上季度最繁忙一周仅 4 人用 AI Agent 叫车 | 这 4 人是否代表"功能刚上线、入口太深"而非需求不存在，无法区分 |
| 数据由 Uber 官方在 TechCrunch 报道中给出 | Agent 调用第三方服务的授权与支付标准何时成熟，未明朗 |
| Agent 叫车涉及支付、身份、第三方 API 授权等链路 | 是 Uber 侧限制还是 Agent 侧能力不足，报道未拆解 |
| 同期 Meta 收购 Agent 编排公司，说明供给侧仍在投入 | 其他平台（外卖/订票）的 Agent 使用率是否同样低，缺数据 |

**📖 主编点评**

做 Agent 产品时，这条是最好的"反 hype"校准器：技术 demo 能跑通 ≠ 用户会用。content-curator 这类项目要警惕同样陷阱——先验证"你自己每天真的会用"，再谈扩展。把"真实使用频次"当第一指标，而不是"功能数量"。

📺 [打开原文](https://techcrunch.com/2026/11/04/almost-no-one-uses-ai-agents-to-book-their-uber-company-says/)

---

## 🌟 股票

### 5. Intel 股价跌势加剧，3.5 万亿美元芯片抛售潮扩散

**[股票]** · ⭐⭐⭐⭐ · _entryleveljobsc_

Intel 的股价崩塌在恶化，并带动一场规模 3.5 万亿美元的芯片板块抛售。与此同时 AMD 预计 Q4 史上首次营收超过 Intel，数据中心业务翻倍。芯片板块正在经历"AI 赢家"与"AI 输家"的剧烈分化。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Intel 股价持续下跌，芯片板块抛售规模达 3.5 万亿美元 | Intel 代工业务能否靠 14A 翻盘，2027 年前无法验证 |
| AMD 预计 Q4 营收 170 亿美元，史上首次超过 Intel | 抛售是情绪面还是基本面重估，市场分歧大 |
| AMD 数据中心业务同比翻倍，游戏业务下滑 40% | AMD 数据中心增长能否持续到 2027，取决于客户 capex |
| AMD Q4 指引高于 Intel 的同期预测 | 芯片板块分化是否会传导到 A 股半导体情绪，属推测 |
| Intel 14A 工艺 PDK 0.9 已可用，目标 2027 年 PDK 1.0 |  |

**📖 主编点评**

这条对你更多是"行业地图"价值：记住 AMD 数据中心翻倍、Intel 靠 14A 赌 2027 这个格局。如果你以后面芯片/硬件相关岗位，这个分化叙事比任何教程都更能帮你在面试里讲清楚"产业在往哪走"。

📺 [打开原文](https://finance.yahoo.com/markets/article/the-intel-stock-collapse-is-getting-worse--and-the-37-trillion-chip-rout-is-spreading-212154947.html)

---

## 📋 备选池

### AI

- [DeepSeek Harness 实测对比 Claude Code：同一模型下工具链差距比想象大](http://www.bilibili.com/video/av117100337236191) —— 用同一个 DeepSeek Pro 模型分别在两套 harness 里跑相同任务，比的是工具链而非模型——正好切中你关心的 Agent 工程细节，但发布时间偏早。
  _程序员晓刘_
- [Everything Claude Code：116K star 的 Claude Code 配置项目实战](http://www.bilibili.com/video/av116319122885806) —— 斜杠命令、子 Agent、Hooks 全覆盖，是 vibe coding 工作流的现成模板；但属教程类，深度不如一手文档。
  _极客魔导师_
- [Claude Code Hooks 回调 + Agent Teams 全自动开发零轮询省 Token](http://www.bilibili.com/video/av116046157647899) —— Stop Hook 自动回调替代轮询、把 Token 消耗压到可忽略，工程细节密度高；但主题偏窄，适合当工具文而非头条。
  _AI超元域_
- [DeepSeek Harness 50 分钟超详细教程（DSH + SuperAgent）](http://www.bilibili.com/video/av117540671982699) —— 11-01 发布的新工具教程，时效性好；但"全网最全"式标题和 60 天制作叙事偏流量号笔法，降级备选。
  _Git源宝_

### AI 算力 / 半导体

- [Nvidia 讨论按 GPU 收每年 2000 美元软件费，用于跑 Agent 基础设施](https://www.tomshardware.com/pc-components/gpus/nvidia-discusses-usd2-000-per-gpu-annual-software-fee-for-running-agents-on-ai-infrastructure-firm-already-charges-more-than-twice-that-amount-for-its-ai-enterprise-software-platform) —— 如果 Agent 推理要按 GPU 年费计，推理成本模型会变；但目前只是"讨论中"，HN 仅 41 分，证据强度不够上头条。
  _gscott_
- [Nvidia 只能满足中国 700 亿美元 GPU 订单的 1%](https://www.tomshardware.com/pc-components/gpus/nvidia-can-only-fulfill-1-percent-of-chinas-massive-usd70-billion-gpu-order-for-ai-chips-report-claims-supply-constraints-choke-export-friendly-rtx-pro-5500-deliveries-despite-huge-demand) —— 700 亿美元订单只交付 1%，供给约束是硬事实；但数据来自"report claims"，且与出口管制叙事重叠，放备选。
  _Ben Stockton_
- [Nvidia 要求数据中心运营商把中国客户业务压到 49% 以下](https://www.tomshardware.com/tech-industry/data-centers/nvidia-tells-data-center-operators-to-limit-business-from-chinese-customers-with-new-global-restrictions-report-claims-allegedly-restricted-to-49-percent-of-the-total-ensuring-51-percent-are-non-chinese-outfits) —— 新全球限制要求非中国客户占 51% 以上，是出口管制的执行层细节；但同样基于"report claims"，待官方确认。
  _Oliver Haslam_
- [Google 发布 Gemini 4 Carbon，微弱超过 Claude Opus 5.5，号称最不易幻觉](https://www.tomshardware.com/tech-industry/artificial-intelligence/google-reveals-new-gemini-4-carbon-ai-model-narrowly-beating-claude-opus-5-5-frontier-ai-model-is-also-the-least-likely-to-hallucinate-benchmarks-claim) —— 模型发布本身是大事，但这条是二手转述且"微弱超过"缺乏评测细节；HN 上 Artificial Analysis 原始榜单更值得看。
  _Jon Martindale_

### 大厂 AI 动态

- [Gemini 4 Carbon 登顶 Artificial Analysis Intelligence Index v5](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1) —— 一手评测榜单来源，比媒体转述可信；但属"已知发布"的评测补充，信息增量有限，放备选供你查细节。
  _theHocineSaad_
- [Tell HN：Gemini 即使对付费个人账号也用聊天记录训练](https://news.ycombinator.com/item?id=50363461) —— 670 分的 HN 讨论，隐私议题对重度用户有实际影响；但属社区爆料非官方确认，证据等级不够头条。
  _jameslk_
- [Canva 裁员超 1200 人，占员工 22%，称面临"最难的一年"](https://techcrunch.com/2026/11/04/canva-lays-off-over-1200-people-amid-slowing-growth/) —— AI 设计工具反噬自身增长，22% 裁员是硬数字；但与你关注方向关联弱，放备选做行业温度计。
  _Ivan Mehta_
- [Apple 据报削减内部 AI 使用预算](https://techcrunch.com/2026/11/04/apple-is-reportedly-cutting-budgets-for-its-internal-ai-usage/) —— 工程团队 AI 支出被"显著下调"，与内存成本暴涨形成呼应；但消息源是"reportedly"，细节缺失。
  _Lucas Ropek_

### 股票

- [Oracle 申请发行 200 亿美元新股与债券，为 AI 基建融资](https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html) —— 200 亿美元融资是 AI 基建"借钱扩张"的典型样本；但属融资动作，产业含义不如头条几条深。
  _smartmic_
- [研究机构称 Anthropic IPO 是"对投资者轻信度的史无前例测试"](https://www.cnbc.com/2026/10/07/anthropic-will-be-most-ridiculous-ipo-of-year-analyst-says.html) —— New Constructs 的尖锐质疑，配合 S-1 里的 RSI 风险披露很有信息量；但发布于 10-07，新颖度不足。
  _m463_

### 金融

- [美国联邦预算赤字一年跳增 12%，逼近 2 万亿美元](https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917691.html) —— 赤字 1.99 万亿是宏观底色，与 AI 基建融资潮互为因果；但属常规宏观数据，非本周新增信号。
  _ck2_
- [3000 亿美元"债务墙"逼近 PE 支持的私有公司](https://www.wsj.com/finance/investing/a-300-billion-debt-wall-is-looming-over-private-equity-backed-companies-d6359497) —— AI 基建大量靠债务融资，这堵墙是潜在系统性风险点；但 WSJ 付费墙且发布于 10-27，时效偏旧。
  _JumpCrisscross_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
