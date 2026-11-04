# Curio 趋势雷达 · 2026-11-04

> 你的私人主编 · 今日跨域精选 5 条头条 + 15 条备选

_今天最值得看的两条信号：一是 Gemini 4 Carbon 在 Artificial Analysis 智能指数上登顶、同时 Anthropic 的 IPO 文件把"算力经济学"和"可能接近递归自我改进"写进风险披露，前沿模型竞赛已经进入"能力+资本"双线叙事；二是芯片股集体大跌、Intel 单日崩盘叠加 Oracle 发 200 亿美元债融资 AI 基建，市场开始给 AI 资本开支重新定价。工程侧则有一条极硬的料：有人把 32 位 RISC-V CPU 编译进 Qwen 3.5 4B 的权重里并跑起 DOOM。_

---

## 🌟 大厂 AI 动态

### 1. Gemini 4 Carbon 登顶 Artificial Analysis 智能指数 v5，Google 称其幻觉率最低

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _theHocineSaad_

Google 上周发布的 Gemini 4 Carbon 在 Artificial Analysis Intelligence Index v5 上拿到第一，官方同时宣称它是前沿模型中最不容易产生幻觉的一个。HN 上 Gemini 4 Carbon 的发布帖拿到 1018 分，说明开发者社区确实在认真测。这不是一次常规迭代，而是 Google 在"能力榜"和"可靠性"两个维度同时抢话语权。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 4 Carbon 在 Artificial Analysis Intelligence Index v5 上排名第一 | "幻觉率最低"目前只有 Google 自报的 benchmark 支撑，缺少第三方复现 |
| Google 官方博客称其为"最不可能产生幻觉"的前沿模型 | 微弱领先 Opus 5.5 意味着榜单差距可能在噪声范围内，下一次更新就会翻转 |
| HN 发布帖 1018 分，Artificial Analysis 分析帖 338 分 | Carbon 与 Argon 的定位差异（通用 vs 机器人）尚未有官方清晰说明 |
| Tom's Hardware 报道其"以微弱优势超过 Claude Opus 5.5" | 实际 coding / agent 任务上的表现是否同步提升，还没有社区大规模实测 |
| 此前 Gemini 4 Argon 已发布并扩展到机器人方向 |  |

**📖 主编点评**

你如果正在给 content-curator 选模型，别只看榜单名次——先拿你自己的 20 条真实抓取任务跑一遍 Carbon 和 Opus 5.5 的对比，重点看结构化输出稳定性和长上下文里的幻觉。榜单第一不等于你的 pipeline 里第一。

📺 [打开原文](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)

---

### 5. Anthropic 的算力经济学在恶化：本该改善的毛利率反而变差

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Russell Brandom_

TechCrunch 指出，在 Anthropic 的算力毛利本该随规模改善的节点上，它反而在变差。结合同一天曝出的 IPO 文件把"可能接近递归自我改进（RSI）"写进风险披露，以及有研究机构称这是"对投资者轻信度的空前考验"，Anthropic 正处在能力叙事与商业现实的最紧张交叉点。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| TechCrunch 报道 Anthropic 的算力毛利在恶化而非改善 | 毛利恶化的具体数字未在报道中给出，需要看 S-1 原文 |
| Anthropic IPO 文件已公开，含收入增长与算力成本披露 | 把 RSI 写进风险披露是法律自保还是真实技术判断，无法从外部验证 |
| IPO 文件警告公司可能"即将"接近递归自我改进 | "最荒谬 IPO"是卖方观点，不代表定价结果 |
| 有研究机构公开称该 IPO 是"2026 年最荒谬的 IPO" | 算力成本恶化与模型能力提升之间的取舍策略尚不清晰 |
| IPO 采用双层股权结构，创始人保留控制权 |  |

**📖 主编点评**

这条值得你花 20 分钟读 S-1 原文里的成本结构段落——它是目前最诚实的"前沿模型公司到底怎么烧钱"的公开材料。对你写 content-curator 的商业化设想（哪怕只是简历里的一段）来说，比任何二手分析都有说服力。

---

## 🌟 股票

### 2. 芯片股 3.5 万亿美元蒸发：Intel 崩盘加剧，Oracle 发 200 亿美元债为 AI 基建融资

**[股票]** · ⭐⭐⭐⭐⭐ · _entryleveljobsc_

一场覆盖 3.5 万亿美元市值的芯片股抛售正在扩散，Intel 的下跌还在加速。同一时间 Oracle 向 SEC 提交文件，计划发行 200 亿美元新股与债券来给 AI 数据中心建设输血；美国对冲基金据报已清空 2025 年以来买入的全部 AI 股票。资本市场的信号很明确：AI 基建的融资成本开始被重新定价。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 芯片板块累计蒸发约 3.5 万亿美元市值，Intel 跌幅居前 | 这轮下跌是估值修正还是 AI 资本开支周期见顶，目前没有共识 |
| Oracle 提交文件拟发行 200 亿美元股票与债券，用于 AI buildout | Oracle 举债扩产若遇融资成本上行，可能形成"越建越贵"的负循环 |
| BBC 报道美股科技板块因 AI 成本担忧出现急跌 | 对冲基金清仓的说法来自单一媒体统计，样本口径不明 |
| 有报道称美国对冲基金已卖出 2025 年以来建仓的全部 AI 股票 | 芯片股与 AI 应用股的走势是否脱钩，还需再看两周 |
| Texas 州长选举结果被指加剧数据中心政策风险，AI 股随之下滑 |  |

**📖 主编点评**

别被"AI 泡沫破裂"的标题带节奏，真正值得跟踪的是融资结构：Oracle 这类靠发债建数据中心的公司，其债券利差比股价更能提前反映风险。如果你关注 AI 基建相关标的，盯债务成本而不是股价日线。

📺 [打开原文](https://finance.yahoo.com/markets/article/the-intel-stock-collapse-is-getting-worse--and-the-37-trillion-chip-rout-is-spreading-212154947.html)

---

## 🌟 AI 算力 / 半导体

### 3. 工程师把 32 位 RISC-V CPU 编译进 Qwen 3.5 4B 的权重里，然后在上面跑 DOOM

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Mark Tyson_

一个叫 Qwenputer 的实验把 32 位 RISC-V CPU 直接编译并插入 Qwen 3.5 4B 的模型权重，让这个 CPU 能执行处理器算术运算、跑代码，当然还有 DOOM。这不是产品，但它把"权重即程序"这件事推到了一个很具体的边界：模型参数里可以装下一台可运行的计算机。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Qwenputer 基于开源 Qwen 3.5 4B 构建 | "编译进权重"的具体实现方式（是嵌入权重张量还是利用量化空间）尚未有论文级说明 |
| 32 位 RISC-V CPU 被编译后直接插入模型权重 | 这种做法的推理开销与实际可用性存疑，更像概念验证 |
| 该内置 CPU 可执行算术运算与代码，并能运行 DOOM | 是否会影响模型原有语言能力，没有公开评测 |
| 项目由一名 AI 工程师完成，属实验性质 | 对模型安全与可解释性研究可能是个新切口，但还没人系统分析 |

**📖 主编点评**

这条对你做 Agent 项目有直接启发：模型的"能力边界"正在从 prompt 层下沉到权重层。你不需要复现它，但值得读一遍实现思路——它提示了一种把确定性逻辑（比如你的 JSON schema 校验）硬编码进推理路径的可能性，比纯 prompt 约束更可靠。

---

## 🌟 金融

### 4. DHS 下令美国联邦民事机构全面移除 DeepSeek，含基于它构建的第三方工具

**[金融]** · ⭐⭐⭐⭐ · _cmrdporcupine_

路透报道，美国国土安全部发布命令，禁止联邦民事机构使用 DeepSeek，并要求连基于 DeepSeek 构建的第三方工具一并清除。HN 上这条拿到 584 分，是本周政策类最高。这条的影响不在 DeepSeek 本身，而在于"基于某模型构建"这件事第一次被写进了合规红线。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DHS 命令覆盖所有美国联邦民事机构 | "基于 DeepSeek 构建"的判定标准（微调？蒸馏？API 调用？）官方未明确 |
| 禁令不仅针对 DeepSeek 本体，也针对基于它构建的工具 | 对开源模型二次开发的合规边界可能被显著收紧，但尚无判例 |
| 路透为首发信源，HN 讨论 584 分 | 是否扩展到其他中国开源模型，目前没有信号 |
| 此前已有针对中国 AI 的政府采购限制趋势 | 对非美国市场的实际约束力有限，更多是采购层面的示范效应 |

**📖 主编点评**

你在做 content-curator 时如果用到任何开源模型做摘要或分类，留意模型来源的合规叙事正在变化。个人项目不受影响，但如果这个项目将来要写进简历、面向企业场景，提前把"模型可替换"做成配置项，比事后改架构便宜得多。

📺 [打开原文](https://www.reuters.com/technology/us-banning-chinese-ai-deepseek-government-agency-it-systems-2026-10-19/)

---

## 📋 备选池

### AI

- [DeepSeek Harness 实测：同一模型在 Claude Code 与 DSH 里差距比想象大](http://www.bilibili.com/video/av117100337236191) —— 少见的 harness 层对比实测，用同一 DeepSeek Pro 模型跑相同任务，讲清了工具链对最终效果的影响——但视频形态密度不如文字，放备选。
  _程序员晓刘_
- [最新 Skills 开发教程：Agent Skill 实战（WorkBuddy + Codex + DeepSeek Harness）](http://www.bilibili.com/video/av117511429295044) —— 10 月底发布，正好卡在 Skills 生态起量的窗口，尚硅谷的课工程细节通常够，但 60 分钟视频需要挑着看。
  _尚硅谷_
- [从零实现 Claude Code（第一话）——Agent Loop](http://www.bilibili.com/video/av116273857961234) —— "一个工具 + 一个循环 = 一个智能体"，讲 harness 层原理的少见内容，契合你要"为什么"的偏好，但系列才第一话。
  _日新月异max_
- [Claude Code Agent Teams 上手指南 + 项目实测](http://www.bilibili.com/video/av116037064331269) —— Agent Teams 的架构与实战讲得比较完整，但发布已 9 个月，新颖度打折。
  _程序员阿江-Relakkes_

### AI 算力 / 半导体

- [Marvell 以 1150 亿美元收购光子公司 Lumentum，押注 AI 互联](https://www.eetimes.com/marvell-snaps-photonics-chipmaker-lumentum-to-bolster-ai-connectivity/) —— 1150 亿美元是本周最大并购数字，co-packaged optics 是 AI 集群互联的关键路径，值得知道但离你的工程实践较远。
  _Majeed Ahmad_
- [Nvidia 要求数据中心运营商对华客户业务不超过 49%](https://www.tomshardware.com/tech-industry/data-centers/nvidia-tells-data-center-operators-to-limit-business-from-chinese-customers-with-new-global-restrictions-report-claims-allegedly-restricted-to-49-percent-of-the-total-ensuring-51-percent-are-non-chinese-outfits) —— 出口管制从卖芯片延伸到卖算力服务，49/51 的比例规则是个新机制，但目前仍是报道口径。
  _Oliver Haslam_
- [Intel 14A 进入 PDK 0.9，2027 年冲刺 1.0](https://www.tomshardware.com/tech-industry/semiconductors/intel-14a-moves-closer-to-production-as-pdk-0-9-becomes-available-process-design-kit-gives-developers-important-production-milestone-ahead-of-1-0-in-2027) —— Intel 代工的关键里程碑，但 PDK 版本号对非芯片从业者信息密度偏低。
  _Anton Shilov_
- [中国部署全球首个 800V 直流供电 AI 数据中心](https://www.tomshardware.com/tech-industry/data-centers/china-deploys-worlds-first-800-volt-dc-power-system-for-massive-ai-data-center-seeks-to-quench-power-needs-with-higher-conversion-and-efficiency-inside-a-smaller-footprint) —— 供电架构是 AI 数据中心被低估的瓶颈，800V DC 是个有工程含量的具体进展。
  _Mark Tyson_

### 大厂 AI 动态

- [AMD Q3 2026 创历史最高单季营收 134 亿美元](https://www.theverge.com/tech/1026148/amd-earnings-q3-2026-data-center-pc) —— 数据中心业务驱动的纪录季度，与芯片股大跌形成有趣对照，但属于财报常规解读。
  _Stevie Bonifield_
- [Anthropic 在做 FlashProve：证明 AI 响应的模型身份](https://techcrunch.com/2026/11/03/anthropic-is-working-on-a-system-to-prove-ai-models-identity/) —— 让任何人验证一条响应确实来自它声称的模型，对 Agent 生态的信任层有意义，但还在早期。
  _Russell Brandom_
- [CrowdStrike 近 5 亿美元收购两家 AI 安全公司](https://techcrunch.com/2026/11/03/crowdstrike-to-shell-out-nearly-500m-for-2-ai-security-startups-as-the-market-for-securing-agents-takes-off/) —— "保护 Agent"正在成为一个独立市场，Fiddler AI 做 agent 可观测性，这个方向值得你留意。
  _Ram Iyer_

### 股票

- [Anthropic IPO 文件警告可能"即将"接近递归自我改进](https://epyhia.com/anthropic-s-ipo-filing-warns-it-may-be-imminently-close-to-recursive) —— 把 RSI 写进 IPO 风险披露是件怪事，值得单独读，但信源是小站转载，需回查 S-1 原文。
  _arbuge_
- [Alphabet 市值单日蒸发 5000 亿美元，史上最大](https://finance.yahoo.com/markets/article/alphabet-heads-for-a-500-billion-drop-in-market-value-the-biggest-in-its-history-134824763.html) —— 与 Gemini 4 Carbon 登顶形成反差：能力领先不等于估值安全，但这条本身是市场情绪而非新事实。
  _rawgabbit_

### 金融

- [美国联邦预算赤字一年跳增 12%，逼近 2 万亿美元](https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html) —— 宏观背景板，与 AI 基建举债扩张叠加看才有意义，单条信息增量有限。
  _ck2_
- [3000 亿美元"债务墙"逼近 PE 控股公司](https://www.wsj.com/finance/investing/a-300-billion-debt-wall-is-looming-over-private-equity-backed-companies-d6359497) —— AI 基建之外的另一条信用风险线，若与数据中心债务叠加会是明年的主线之一。
  _JumpCrisscross_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
