# Curio 趋势雷达 · 2026-11-12

> 你的私人主编 · 今日跨域精选 5 条头条 + 22 条备选

_今天最重要的信号只有一个：Nvidia 董事会据报准备罢免黄仁勋，股价自丑闻爆发以来已跌 20%，国会要求闭门简报、FBI 介入。这不只是公司治理事件，而是整个 AI 算力叙事的定价锚在松动——同期 Nasdaq 已跌入回调区间、AI 相关股票被系统性抛售。另一条线是 Anthropic 在 IPO 前夕自曝"关键 AI 安全警报已被触发"，目标估值 1.4 万亿美元。两条线合起来看：AI 资本周期的风险溢价正在被重新定价。_

---

## 🌟 AI 算力 / 半导体

### 1. Nvidia 董事会据报准备罢免黄仁勋：第二段婚外情曝光，股价自丑闻以来跌 20%，33 年唯一 CEO 面临下台

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

WSJ 与多家媒体同步报道，Nvidia 董事会正就黄仁勋的去留召开紧急会议，最早周三晚间可能做出决定。触发点是第二段婚外情——对象是向他直接汇报的 Nvidia 高管，此前他已承认与一名被指为中国情报人员的女性有染。股价自丑闻爆发以来累计下跌约 20%，公司 33 年来没有继任计划。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| WSJ 报道 Nvidia 董事会准备罢免 CEO 黄仁勋，最早周三晚间决定 | 董事会是否真的投票罢免，还是以"调查+留任"收场，目前只有媒体转述，无公司正式公告 |
| 第二段婚外情对象为向其直接汇报的 Nvidia 高管，并涉掩盖尝试 | 婚外情本身不构成罢免的法律依据，真正的杠杆是国家安全审查与治理失效 |
| 股价自丑闻爆发以来累计下跌约 20% | 继任者人选完全空白，短期可能由 CFO 或 COO 临时接管，市场对"无 succession plan"的恐慌可能大于事件本身 |
| 黄仁勋任 Nvidia CEO 已 33 年，公司无公开继任计划 | 若黄仁勋留任，国会与 FBI 的调查会持续压制估值；若离职，AI 算力采购的连续性会被重新评估 |
| 美国众议院三个委员会要求其就"防范外国对手间谍的安全协议"做闭门简报，否则发传票 |  |
| FBI 已介入调查，TechCrunch 与 Ars Technica 均确认董事会紧急磋商 |  |

**📖 主编点评**

你不需要交易 Nvidia，但需要理解一件事：过去两年所有 AI 产品的成本曲线都建立在"算力持续降价+供应稳定"的假设上。这个假设的锚现在在晃。做 content-curator 这类个人项目时，把模型调用做成可切换（Claude / Gemini / DeepSeek 都能跑）不是过度设计，是今天这种局面的基本对冲。

📺 [打开原文](https://www.tomshardware.com/pc-components/gpus/nvidias-board-reportedly-preparing-to-oust-ceo-jensen-huang-as-second-extra-marital-affair-emerges-stock-has-plunged-20-percent-since-scandals-began-huang-has-been-first-and-only-ceo-for-33-years)

---

### 5. Linux 内核内存管理审阅者因 AI 生成的低质补丁洪流辞职："浪费的时间已经太多，而这只是开始"

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

一位 Linux 内核内存管理子系统的审阅者宣布退出该职责，直接原因是 AI 生成的"slop patch"大量涌入，审阅成本远超人力承受。他的原话是"浪费在 AI slop 上的时间已经太多，而我们才处在提交量的起点"。这是开源治理层面第一次有人因 AI 生成内容而退出关键岗位。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Linux 内核内存管理子系统一位审阅者因 AI 生成补丁洪流辞职 | AI 生成补丁占提交总量的比例没有量化数据 |
| 当事人称"浪费在 AI slop 上的时间已经太多" | 内核社区是否会引入 AI 生成内容标识或提交门槛，尚未有提案 |
| 补丁提交量上升与审阅人力不足同时发生 | 类似压力是否已扩散到其他子系统（网络、文件系统）未知 |
| 该决定由 Tom's Hardware 报道，引述内核邮件列表 | 这是否会加速"AI 审 AI"的自动化 review 工具落地，方向不明 |

**📖 主编点评**

这条对你做 content-curator 是直接的方法论警告：Agent 生成内容的瓶颈从来不在生成，在审阅与筛选。你的项目里"候选池 → 选稿"这一步就是人工审阅位，别把它全自动化掉。反过来，这也是一个产品机会——做"AI 生成内容的去重与质量前置过滤"，比再做一打生成工具更有价值。

📺 [打开原文](https://www.tomshardware.com/software/linux/linux-kernel-reviewer-steps-down-from-memory-management-duties-due-to-influx-of-ai-slop-patches-the-amount-of-time-wasted-on-ai-slop-is-already-too-much-and-were-only-at-the-start-of-this-volume-of-submissions-and-low-manpower-forces-the-step-back)

---

## 🌟 大厂 AI 动态

### 2. OpenAI 单季营收首次突破 100 亿美元，环比 Q2 的 67 亿增长近 50%

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _TechCrunch_

据 TechCrunch 报道，OpenAI 季度营收首次跨过 100 亿美元，相比第二季度 67 亿美元增长近 50%。这个数字出现在 AI 股票被系统性抛售、Anthropic IPO 估值遭质疑的同一周，构成一个有意思的对照：终端付费需求仍在加速，但资本市场对 AI 公司的定价在收缩。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| OpenAI 单季营收首次突破 100 亿美元 | 100 亿是营收不是利润，OpenAI 的推理成本与算力支出是否同步扩大，报道未披露 |
| 上一季度（Q2）营收为 67 亿美元，环比增长近 50% | 增长中有多少来自 API/企业合同、多少来自 ChatGPT 订阅，结构不明 |
| 该数据由 TechCrunch 引述知情人士报道，非官方财报 | 若算力成本随 Nvidia 供应波动上升，这个增速的可持续性存疑 |
| 同期 Nasdaq 跌入回调区间，AI 相关股票遭抛售 | 与 Anthropic 1.4 万亿 IPO 估值对照，市场可能在重新分配"谁配得上高倍数" |

**📖 主编点评**

对你做 Agent 项目有直接含义：API 价格短期不会因为资本寒冬而上涨，反而可能继续打。现在是把重活（批量摘要、embedding、评测跑批）往 API 上搬的好窗口，别急着自建推理。同时留意 OpenAI 的收入结构披露——如果企业 API 占比在涨，说明 Agent 类产品的付费意愿是真的。

📺 [打开原文](https://techcrunch.com/2026/11/11/openais-quarterly-revenue-reportedly-crosses-10b-for-the-first-time/)

---

### 4. 美联航明确拒绝个人 AI Agent 代订机票，理由是隐私与监管

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _The Verge_

United 公开表示不会允许个人 AI 助手在其系统上代订机票，援引隐私与监管顾虑。公司称目前实际尝试用 Agent 订票的用户还不多，但选择提前划线。这是主流服务商第一次明确对"Agent 代操作"说不，对做 Agent 产品的人是重要的边界信号。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| United 明确表示不允许个人 AI Agent 代订机票 | "监管顾虑"具体指哪条法规未说明，可能是身份验证与授权链条问题 |
| 官方理由是隐私与监管顾虑 | 实际执行层面如何识别 Agent 流量（UA、行为指纹、支付信息）未披露 |
| 公司称目前尝试用 Agent 订票的用户数量还不多 | 其他航司与平台是否会跟进形成行业惯例，目前未知 |
| 这是主流航空公司首次公开对 Agent 代操作表态 | 对 Agent 生态的长期影响取决于是否有标准化授权协议出现 |

**📖 主编点评**

你在做 content-curator 时迟早会遇到同类问题：Agent 去抓取/操作第三方服务，对方是否授权。这条新闻的价值在于它给了你一个判断框架——先问"对方有没有明确的拒绝声明"，再设计自动化路径。把 Agent 的对外操作做成"可插拔的 connector + 显式授权记录"，比事后补救便宜得多。

📺 [打开原文](https://www.theverge.com/ai-artificial-intelligence/1031623/united-unauthorized-ai-agents)

---

## 🌟 股票

### 3. Anthropic 在 IPO 前几天自曝"关键 AI 安全警报已被触发"，同时目标 1.4 万亿美元估值

**[股票]** · ⭐⭐⭐⭐ · _Yahoo Finance_

Anthropic 在 IPO 前夕披露其内部一项"关键 AI 安全警报"已被触发，具体内容未公开。同一周 Bloomberg 报道其 IPO 目标估值 1.4 万亿美元，而 Michael Burry 公开称 Anthropic 是在"拿存在性做赌注"。S-1 文件里还警告公司可能"即将"接近递归自我改进（RSI）。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Anthropic 在 IPO 前披露一项"关键 AI 安全警报"被触发 | "安全警报"的具体触发条件与严重程度未披露，可能是治理披露义务，也可能是真实能力跃迁信号 |
| Bloomberg 报道其 IPO 目标估值 1.4 万亿美元 | 在 IPO 前主动披露风险，更像合规动作而非产品事故，但市场会如何解读不确定 |
| S-1 文件警告公司可能"imminently"接近递归自我改进（RSI） | RSI 相关措辞出现在 S-1 里，法律上是风险提示，技术上是否成立无法外部验证 |
| Michael Burry 公开质疑其估值逻辑 | 1.4 万亿估值在 AI 抛售周能否撑住，取决于承销商定价而非基本面 |
| 大型投资者对 1.5 万亿估值表示怀疑（WSJ） |  |

**📖 主编点评**

这是本周最值得你读原文的一条——不是因为估值，而是因为一家前沿实验室在招股书里写"可能接近递归自我改进"。如果你在做 Agent 项目，去读 S-1 里关于能力评估与安全阈值的章节，比读任何"Agent 教程"都更能校准你对模型能力边界的判断。

📺 [打开原文](https://finance.yahoo.com/markets/article/anthropic-says-a-key-ai-safety-alarm-has-been-triggered-days-before-its-ipo-171519615.html)

---

## 📋 备选池

### AI 算力 / 半导体

- [AMD Venice-X 最高 5.3 GHz，3D V-Cache 四年后重回数据中心](https://www.tomshardware.com/pc-components/cpus/amds-venice-x-maxes-out-family-at-5-3-ghz-returning-3d-v-cache-to-data-center-after-four-years-chips-target-hpc-workloads-with-pcie-6-0-and-1-6-tb-s-memory-bandwidth) —— 2027 下半年才上市，但 PCIe 6.0 + 1.6TB/s 带宽的参数说明 AMD 在数据中心正面压 Nvidia 的意图，值得存档。
  _Tom's Hardware_
- [AMD 用 MEXT 技术在仅一半 DRAM 下保住 95% 服务器性能](https://www.tomshardware.com/pc-components/cpus/amd-shares-how-it-can-retain-95-percent-of-server-performance-with-just-half-the-dram-sidestepping-memory-shortages-with-mext-tech-powers-over-100-servers-already-running-with-plans-to-expand-to-2-000-servers-in-2027) —— 内存短缺背景下的工程解法，已有 100+ 台服务器在跑、2027 扩到 2000 台，是少见的"已落地"数字。
  _Tom's Hardware_
- [有人用电压毛刺把 2500 美元矿卡刷成 2 万美元 A100 80GB](https://www.tomshardware.com/pc-components/gpus/techie-turns-usd2-500-cmp-170hx-8gb-mining-card-into-a-full-fat-a100-80gb-with-voltage-glitching-carefully-blowing-onboard-fuses-to-unlock-entire-vram-and-shader-modules) —— 硬件极客向，但说明 A100 的 VRAM/着色器模块是熔丝锁的——对理解 GPU 分级定价有启发，不是教程。
  _Tom's Hardware_
- [SpaceX 据报自研 Kessel 机架系统，72 颗 Nvidia Rubin GPU 上太空](https://www.tomshardware.com/tech-industry/artificial-intelligence/spacex-develops-its-own-kessel-rack-scale-system-featuring-72-nvidia-rubin-gpus-for-data-centers-in-space-report-claims-replaces-conventional-nvlink-cable-assemblies-with-a-massive-84-layer-printed-circuit-board) —— 84 层 PCB 中板替代 NVLink 线缆，太空数据中心从概念走向具体设计，但目前只是"report claims"。
  _Tom's Hardware_
- [SoftBank 取消 AI 数据中心燃气轮机订单，损失 37 亿美元](https://www.tomshardware.com/tech-industry/data-centers/softbank-loses-usd3-7-billion-on-canceled-ai-data-center-gas-turbine-orders-days-after-denying-elon-musks-claim-it-was-defaulting-company-kills-reserved-13-gigawatts-of-power-more-than-six-hoover-dams-worth-of-capacity) —— 取消 13GW 电力预留（相当于六个胡佛大坝），是 AI 数据中心建设退潮最硬的数字证据。
  _Tom's Hardware_

### 大厂 AI 动态

- [Google DeepMind 发布 AlphaGenome 2，从细胞层面解析疾病](https://www.theverge.com/ai-artificial-intelligence/1031524/google-deepmind-alphagenome-2-genetic-ai-model) —— DeepMind 在科学 AI 上的持续投入，与你偏好相关度低但属于"AI 真正落地"的少数方向。
  _The Verge_
- [Google 实验性产品 Tabletop：用 AI 生成定制协作应用](https://www.theverge.com/tech/1031526/google-tabletop-ai-experiment-waitlist-availability) —— 生成式 UI 的又一次尝试，目前是 waitlist 实验，值得关注但还没有工程细节可学。
  _The Verge_
- [Databricks 给 CEO 造了个 AI Agent，专门说"不加滤镜的真话"](https://techcrunch.com/2026/11/11/databricks-new-ai-agent-tells-ceo-ali-ghodsi-the-unvarnished-truth/) —— 1.2 万人公司的内部 Agent 实践，方向有意思（向上反馈），但报道偏故事、缺实现细节。
  _TechCrunch_
- [Meta 基础设施负责人 Santosh Janardhan 离职](https://techcrunch.com/2026/11/11/meta-is-losing-its-longtime-head-of-infrastructure/) —— 2009 年入职的老将离开，在 AI 算力军备竞赛节点上的人事变动，值得记一笔。
  _TechCrunch_
- [英国 Fractile 完成 7.2 亿美元融资，押注专用 AI 芯片](https://techcrunch.com/2026/11/11/with-720m-round-britains-fractile-gets-a-leg-up-in-the-race-for-ai-chips/) —— Nvidia 动荡周里，欧洲 AI 芯片挑战者拿到大额融资，是算力供应链多元化的一个注脚。
  _TechCrunch_
- [Ben Thompson：Intel 与 AMD 财报分化，Intel 可能需要找回"新（旧）路"](https://stratechery.com/2026/intel-earnings-amd-earnings-intel-and-amds-divergence/) —— Stratechery 的框架性分析，适合周末慢读，但今天不是最紧急的一条。
  _Stratechery_

### 股票

- [Nvidia 危机让公司治理专家"拿起爆米花"：没人见过这种局面](https://techcrunch.com/2026/11/10/nvidias-crisis-has-corporate-governance-experts-reaching-for-the-popcorn/) —— 黄仁勋事件的头条已选，这条是治理视角的补充，解释了为什么"无继任计划"比丑闻本身更致命。
  _TechCrunch_
- [Nasdaq 跌入回调区间，单日跌 4%](https://www.cnbc.com/2026/11/04/stock-market-today-live-updates.html) —— AI 抛售的宏观背景，数字硬但已是上周事件，作为头条的注脚而非独立条目。
  _CNBC_
- [Oracle 申请发行 200 亿美元新股与债券为 AI 建设融资](https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html) —— AI 资本开支从"经营现金流"转向"举债"的标志性动作，值得放进你的宏观观察清单。
  _CNBC_

### 金融

- [Tesla 将停产 Cybertruck](https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817) —— 1163 分的高热度，但与你关注方向距离较远，作为"制造业产品失败"案例存档即可。
  _NBC News_
- [美国联邦预算赤字一年跳增 12%，接近 2 万亿美元](https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html) —— AI 资本周期背后的利率环境变量，赤字扩张会压制长端利率下行空间，间接影响科技估值。
  _Yahoo Finance_
- [美国国土安全部下令联邦民事机构全面移除 DeepSeek](https://www.reuters.com/technology/us-banning-chinese-ai-deepseek-government-agency-it-systems-2026-10-19/) —— 10 月 19 日的旧闻，但作为"模型地缘政治化"的基线事实，做多模型路由时值得记住这条边界。
  _Reuters_

### AI

- [Claude Code 桌面端全攻略：编程、设计、办公能力收进同一客户端](http://www.bilibili.com/video/av117580048108571) —— 11 月 8 日发布，讲 Claude Desktop 把 Code/Design/Cowork 合并 + Opus 5.5，是本周最贴近你工作流的一条，但形式是视频教程、密度不如文字。
  _技术爬爬虾_
- [DeepSeek 开源的 Super Agent 是什么，真有用么](http://www.bilibili.com/video/av117564076202051) —— 11 月 5 日发布，讲 DeepSeek Harness 团队的 Super-agent 与常规定位差异，新颖度够但缺代码细节。
  _程序员鱼皮_
- [蚂蚁灵光 2.0 Personal AI 助理实操：9 件琐事交给它](http://www.bilibili.com/video/av117591808940027) —— 11 月 10 日最新，Personal AI 是本周产品热点，但本质是产品演示而非工程拆解。
  _GenJi是真想教会你_
- [Skills 开发教程：WorkBuddy + Codex + DeepSeek Harness 实战](http://www.bilibili.com/video/av117511429295044) —— Agent Skills 是你偏好方向，但尚硅谷的课程偏"喂饭式"，工程细节密度低，适合当索引而非正文。
  _尚硅谷_
- [40 分钟速通 Codex 深度教程](http://www.bilibili.com/video/av117558925596398) —— 11 月 5 日发布，安装+核心功能+实战案例，是 Codex 目前较完整的中文材料，但仍是教程类。
  _GenJi是真想教会你_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
