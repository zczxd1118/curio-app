# Curio 趋势雷达 · 2026-10-21

> 你的私人主编 · 今日跨域精选 5 条头条 + 18 条备选

_今天最值得盯的是两条反向信号：一边是 SpaceX 靠 AI 业务把季度营收推到 146 亿美元、净利 44 亿，另一边是 Anthropic 估值被传缩水 5000 亿、云算力拿不到、IPO 前夜承压。AI 泡沫的分歧已经从口水战变成财报和估值数字，同时 Google 和 Amazon 都在推工具把 PyTorch 应用搬离 Nvidia GPU，算力层的护城河开始被撬。_

---

## 🌟 大厂 AI 动态

### 1. SpaceX 季度营收 146 亿美元、净利 44 亿，AI 业务成了增长引擎

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _TechCrunch_

SpaceX 在 Q3 财报里报出 146 亿美元营收，同比增长 161%，净利 44 亿美元，公司明确把增长归因于 Super Intelligence 业务。同一场电话会上 Musk 还确认 Tesla 与 SpaceX 已各自成立特别委员会评估合并。一家火箭公司靠 AI 赚钱，这件事本身就说明算力与模型的现金流正在从纯 AI 公司外溢。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Q3 营收 146 亿美元，同比 +161% | Super Intelligence 业务的具体构成与客户尚未披露 |
| 季度净利 44 亿美元，公司称 AI 是主要驱动 | AI 收入是否可持续，还是单季大单拉动，无法判断 |
| Tesla 与 SpaceX 董事会已成立特别委员会评估合并 | 合并若成行，监管审查周期可能长达一年以上 |
| Musk 称合并"有很多合理性"，本人不在委员会内 | SpaceX 的 AI 算力从哪来、与 xAI 的关系如何，仍是空白 |
| SpaceX 同时宣布下月首次尝试同时回收 Starship 与助推器 |  |

**📖 主编点评**

别只把它当航天新闻看。一个非 AI 原生公司用 AI 把营收翻倍，是"AI 变现"最硬的样本，值得你拆它的业务结构。如果你在准备简历或面试，这类"传统公司靠 AI 重估"的案例比任何模型跑分都更能说明行业阶段。

📺 [打开原文](https://techcrunch.com/2026/10/20/spacexs-ai-business-is-beating-expectations/)

---

### 4. Figma 联创直言 MCP 不是完美协议，计划同时支持多种标准

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _TechCrunch_

Figma 联合创始人 Dylan Field 在采访中称 MCP 并非完美协议，公司打算支持尽可能多的标准，同时不把全部数据暴露出去。这是头部产品公司第一次公开给 MCP 泼冷水。对重度玩 MCP 的你来说，这比又一篇"MCP 教程"有价值得多——它指向协议层的真实摩擦。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Figma 联创 Dylan Field 公开表示 MCP 不是完美协议 | MCP 的具体缺陷（鉴权、粒度、状态管理？）Field 未展开 |
| Figma 计划支持多种标准而非只押 MCP | Figma 会否自研协议或转向 A2A 等方案，不明 |
| 公司强调不会通过协议暴露全部数据 | 其他 SaaS 厂商是否跟进"多标准"策略，待观察 |
| 同期 Figma 未公布具体支持哪些替代标准 | MCP 生态的碎片化风险是否被低估 |

**📖 主编点评**

你在做 Agent 项目时如果深度绑定 MCP，这条是提醒：协议层还没定型。建议把工具接入层做成可替换的抽象，别让 MCP 的 schema 渗进业务代码。这也是一个很好的技术判断素材——"为什么我不把 MCP 写死"。

📺 [打开原文](https://techcrunch.com/2026/10/20/figma-co-founder-dylan-field-thinks-mcp-is-not-a-perfect-protocol/)

---

## 🌟 金融

### 2. Anthropic 估值被传缩水 5000 亿美元，IPO 前夜云算力还拿不到

**[金融]** · ⭐⭐⭐⭐⭐ · _Hacker News / The Telegraph_

Telegraph 报道 Anthropic 估值较此前高点回落约 5000 亿美元，同期 TechCrunch 称它在 IPO 前难以从云厂商拿到足够算力——因为这些云厂商越来越把它当竞争对手。9 月底 Reuters 披露的招股书已显示"宏大 AI 愿景 + 成本飙升"的组合。估值、算力、上市三件事叠在一起，是本周 AI 资本市场最值得盯的裂缝。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Telegraph 报道 Anthropic 估值缩水约 5000 亿美元 | 5000 亿缩水是二级市场传闻还是真实融资定价，尚无官方确认 |
| TechCrunch 称其云算力采购受阻，云厂商视其为竞争者 | 算力受限会否直接推迟模型迭代节奏，未知 |
| Reuters 早前披露招股书显示成本大幅上升 | IPO 是否按期在 11 月落地仍存变数 |
| 公司计划 11 月推进 IPO | 云厂商"既供货又竞争"的结构性矛盾会持续多久 |
| Eric Schmidt 据报持股约为 Dario Amodei 的一半 |  |

**📖 主编点评**

这是你判断"AI 泡沫是否开始泄气"的关键观测点。建议你把 Anthropic 招股书原文找出来读成本结构那一节——比任何二手评论都清楚。同时留意：如果头部模型公司都拿不到算力，你做的 Agent 项目未来调用成本只会更贵，架构上要预留多模型切换。

📺 [打开原文](https://www.telegraph.co.uk/business/2026/10/16/anthropic-valuation-ipo-ai-stock-listing/)

---

## 🌟 AI 算力 / 半导体

### 3. Modal 实测 Nvidia Vera CPU 在 Agent 负载上吞吐是 Intel/AMD 的两倍

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

AI 推理平台 Modal 把 Nvidia 的 Vera CPU 部署进现有 x86 集群，内部测试显示在 AI Agent 类负载上吞吐达到 Intel 和 AMD 芯片的两倍。同一周 Arm 也放出自家 AGI CPU 对比 AMD EPYC 9755 的"每机架近 2 倍"数据。CPU 侧针对 Agent 负载的军备竞赛正式开打。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Modal 已在生产环境部署 Nvidia Vera CPU | 两倍吞吐的测试条件与基线未完整公开，需谨慎看待 |
| 内部测试称 Agent 负载吞吐为 Intel/AMD 的 2 倍 | Agent 负载的基准是否代表真实生产流量，存疑 |
| Arm 同期发布 AGI CPU，称每机架性能近 2 倍于 EPYC 9755 | Vera CPU 的定价与供货时间未披露 |
| Arm 的评测方法由 Fujitsu、Meta、OpenAI 共同参与制定 | CPU 侧竞争能否真正削弱 Nvidia 在训练端的地位，为时尚早 |
| Google 与 Amazon 均在推工具帮 PyTorch 用户迁离 Nvidia GPU |  |

**📖 主编点评**

如果你关心推理成本，这条比模型发布更实用。Agent 类负载（多轮工具调用、长上下文）和传统推理的硬件偏好不同，未来选型不能只看 GPU。做 content-curator 这类项目时，把"CPU 侧 Agent 负载"作为一个观察维度记下来，面试时是加分细节。

📺 [打开原文](https://www.tomshardware.com/pc-components/cpus/nvidia-vera-cpu-deployed-at-ai-startup-modal-alongside-existing-x86-fleet-internal-testing-showed-2x-throughput-compared-to-amd-and-intel)

---

### 5. DeepMind 四个 Gemini 4 Agent 用 27 小时通关 Minecraft，自己写了 2783 个程序

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

DeepMind 研究者称四个 Gemini 4 Argon Agent 在无人工干预下 27 小时通关 Minecraft，期间自行编写 2783 个程序，死亡 605 次（简单难度），烧掉约 520 美元 token。数字很诚实——包括失败次数和成本。这是多 Agent 协作在长程任务上少见的完整公开数据。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 四个 Gemini 4 Argon Agent 协作通关 Minecraft | "通关"的判定标准与是否用了模组未说明 |
| 耗时 27 小时，全程无人工干预 | 2783 个程序的质量与复用率未知 |
| Agent 自行编写 2783 个程序 | 简单难度下的成绩能否外推到复杂任务，存疑 |
| 死亡 605 次，难度为简单 | 多 Agent 协作的具体分工机制未公开 |
| token 成本约 520 美元 |  |

**📖 主编点评**

这条的价值在"失败数据"：605 次死亡和 520 美元成本，比任何"Agent 通关游戏"的标题都更能说明长程 Agent 的真实状态。你做 content-curator 时，可以借鉴它的思路——记录 Agent 的失败次数和 token 成本，作为项目的一个量化指标写进 README。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/google-deepmind-claims-four-gemini-4-agents-beat-minecraft-in-27-hours-by-writing-2-783-programs-of-their-own-the-ai-team-died-605-times-on-easy-difficulty-and-ran-up-an-estimated-usd520-in-tokens)

---

## 📋 备选池

### AI

- [Claude Code 四个阶段](http://www.bilibili.com/video/av117449504595834) —— 10 月 19 日新发，讲 Claude Code 使用进阶路径，时长偏短、信息密度待验证，先放备选。
  _程序员牛牛学长_
- [DeepSeek V4.1 Flash 接入指南｜六大 Agent 工具一次配好](http://www.bilibili.com/video/av117459403150912) —— 实测把 V4.1 Flash 接进 Codex、Claude Code 等七个工具，含配置与避坑，工程细节够但偏工具合集。
  _跟着小陈玩AI_
- [太炸裂了！Claude Code 3.0 彻底杀疯了！](http://www.bilibili.com/video/av117450007911196) —— 搬运翻译海外视频，标题党味重，但 Claude Code 3.0 本身值得留意，等原版信息再深挖。
  _烟神殿殿主_
- [【实操】claude 稳定不封的方法](http://www.bilibili.com/video/av117457104672336) —— 国内用 Claude 的封号规避实操，实用但偏灰色地带，按需自取。
  _程序员大龙虾_
- [AI 产品经理作品集：Vibe Coding 实操 ChatBI 落地写进简历](http://www.bilibili.com/video/av117445360618053) —— 讲企业级 Vibe Coding 落地流程（SDD、Harness、skill 设计），和你做简历项目的诉求直接相关。
  _AI产品经理PMGao_
- [开源安卓 AI Agent：RikkaHub Agent Pure 让手机自己操作 App](http://www.bilibili.com/video/av117394643097499) —— AGPL 开源，靠无障碍控件树做屏幕自动化而非死坐标脚本，架构思路值得看源码。
  _补药满减哇_

### 金融

- [Data center stocks slide as Korea IPO plunges 30%](https://www.cnbc.com/2026/10/20/data-center-stocks-slide-as-korea-ipo-plunges-30percent-pressuring-tech-sentiment.html) —— 韩国数据中心 IPO 首日跌 30%，拖累全球数据中心股，是 AI 基建估值松动的又一信号。
  _CNBC / Hacker News_
- [Anthropic's cloud partnerships are getting messy](https://techcrunch.com/2026/10/20/anthropics-cloud-partnerships-are-getting-messy/) —— 与头条 2 同源但聚焦云合作细节，算力采购与 IPO 时间线的补充材料。
  _TechCrunch_
- [US federal budget deficit jumps 12% in one year to nearly $2 Trillion](https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html) —— 美国联邦赤字一年增 12% 至近 2 万亿美元，是 AI 资本开支狂欢的宏观背景板。
  _Yahoo Finance / Hacker News_
- [10-year Treasury yield climbs above 5.3%, highest in 24 years](https://www.wsj.com/finance/investing/surging-yields-bring-the-bond-market-back-to-the-turn-of-the-century-2b74773f) —— 十年期美债收益率破 5.3%，融资成本上升直接压制数据中心与 AI 基建的杠杆故事。
  _WSJ / Hacker News_

### AI 算力 / 半导体

- [China's tech giants drop $35B on Nvidia RTX Pro 5500 orders](https://www.tomshardware.com/pc-components/gpus/chinas-tech-giants-drop-usd35-billion-on-export-compliant-nvidia-rtx-pro-5500-workstation-gpu-orders-to-power-ai-ambitions-according-to-reports-bytedance-alibaba-and-tencent-order-3-million-cards-despite-warnings-that-only-10-percent-of-orders-are-fulfillable) —— 字节、阿里、腾讯下单 35 亿美元合规版 GPU，但据报仅 10% 订单可交付，供需缺口惊人。
  _Tom's Hardware_
- [US restarts three shut-down nuclear reactors to feed AI data centers](https://www.tomshardware.com/tech-industry/big-tech/us-takes-unprecedented-step-of-recommissioning-nuclear-plants-due-to-ai-power-demand-2-25-gw-currently-on-tap-from-refurbished-reactors) —— 美国重启三座核反应堆供电 AI 数据中心，现有 2.25GW 容量，电力正成为算力瓶颈。
  _Tom's Hardware_
- [Chris Lattner: AI Code Generation Doesn't Solve Software Engineering](https://www.eetimes.com/chris-lattner-ai-code-generation-doesnt-solve-software-engineering/) —— LLVM 之父谈 AI 生成代码反而让软件生态更难维护，观点稀缺，适合你这种重度 vibe coding 玩家反刍。
  _EE Times_
- [Qualcomm Wins Key Claims Against Arm, but Damages Total Just $2](https://www.eetimes.com/qualcomm-wins-key-claims-against-arm-but-damages-total-just-2/) —— 高通在四年 IP 诉讼中赢下关键主张，但赔偿仅 2 美元，象征意义大于财务意义。
  _EE Times_

### 大厂 AI 动态

- [US orders federal agencies to remove China's DeepSeek AI from their systems](https://techcrunch.com/2026/10/20/us-orders-federal-agencies-to-remove-chinas-deepseek-ai-from-their-systems/) —— 美政府要求联邦机构移除 DeepSeek 及基于其技术的第三方服务，国产模型出海再添阻力。
  _TechCrunch_
- [Muse Spark Open, Meta + Apple, Thin and Thick](https://stratechery.com/2026/muse-spark-open-meta-apple-thin-and-thick/) —— Ben Thompson 分析 Meta 新开源模型与 Apple 合作本地运行，是本周最值得读的深度评论。
  _Stratechery_
- [Anthropic pitches AI safety bill that may block a model if 50+ people could be killed](https://techcrunch.com/2026/10/20/anthropic-pitches-ai-safety-bill-that-may-block-a-model-if-50-people-could-be-killed/) —— Anthropic 推安全法案，表面设门槛实则要求法官批准才能阻止模型发布，立法博弈值得关注。
  _TechCrunch_
- [Meta's Muse hits 10M US downloads in 40 days](https://techcrunch.com/2026/10/20/metas-muse-hits-10m-u-s-downloads-in-40-days-a-milestone-reached-by-only-11-other-apps/) —— Meta 的 Muse 40 天美国下载破千万，留存率高于 AI 竞品，消费级 AI 格局在变。
  _TechCrunch_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
