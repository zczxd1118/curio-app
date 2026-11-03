# Curio 趋势雷达 · 2026-11-03

> 你的私人主编 · 今日跨域精选 5 条头条 + 17 条备选

_今天最值得看的两条线：一是 AI 资本结构开始承压——Marvell 1150 亿美元吞下 Lumentum、Oracle 发 200 亿股债、Intel 领跌 3.5 万亿芯片股回调，钱在往光互联和算力上压重注，同时市场开始怀疑回报；二是 Anthropic 一边限制 Claude Code 复刻游戏 IP，一边自曝接近 RSI，模型厂商的自我约束和自加速同时发生。_

---

## 🌟 AI 算力 / 半导体

### 1. Marvell 以 1150 亿美元收购光子公司 Lumentum，赌 AI 互联而非算力本身

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Majeed Ahmad_

这是科技史上最大并购之一。Marvell 要把网络处理器和激光器放在同一张图纸上协同设计，目标直指光模块——AI 集群里最先卡住的那一环。两家背后站着同一个战略投资人 Nvidia，说明这笔钱不是财务投资，是给算力扩张补血管。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 交易对价 1150 亿美元，为科技史最大并购之一 | 协同设计能否真正缩短光模块交付周期，尚无产品时间表 |
| Lumentum 主营光收发器用激光器，Marvell 做网络处理器 | 1150 亿美元溢价是否合理，要等监管与股东投票 |
| 双方将协同设计网络处理器与激光器，做 AI 互联品类龙头 | Nvidia 在两边持股是否触发反垄断审查，未明朗 |
| Marvell 与 Lumentum 拥有同一战略投资人 Nvidia | 光互联会不会成为下一个产能瓶颈，取决于 CPO 落地节奏 |
| 消息于 2026-11-03 由 EE Times 首发报道 |  |

**📖 主编点评**

你如果只盯 GPU 会漏掉这条。AI 集群的瓶颈正从算力转向互联，光模块、CPO、交换芯片是未来 12 个月最值得跟踪的硬件方向。做 content-curator 时可以加一条「光互联」关键词，比追 GPU 新闻更有信息差。

📺 [打开原文](https://www.eetimes.com/marvell-snaps-photonics-chipmaker-lumentum-to-bolster-ai-connectivity/)

---

### 4. 有人把 32 位 RISC-V CPU 编译进 Qwen 3.5 4B 的权重里，还跑起了 DOOM

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Mark Tyson_

Qwenputer 这个实验把一颗 32 位 RISC-V CPU 直接编译并塞进 Qwen 3.5 4B 的权重，模型能执行处理器算术运算，最后跑通了 DOOM。这不是产品，但它把「权重即程序」这件事推到了一个荒诞又清晰的极端。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 项目名 Qwenputer，基于 Qwen 3.5 4B 开源模型 | 这是否代表一种新的模型能力范式，还是精巧的工程 trick |
| 32 位 RISC-V CPU 被编译并插入模型权重 | 权重内嵌 CPU 对推理效率是否有任何实际收益，未知 |
| 模型可执行处理器算术运算与代码 | 方法能否迁移到更大模型或其他架构，未验证 |
| 已成功运行 DOOM | 对模型可解释性研究是否有价值，尚属猜测 |
| 由独立 AI 工程师完成，非官方项目 |  |

**📖 主编点评**

这条值得你花 10 分钟看原理，因为它挑战了「模型只会预测 token」的默认假设。做 Agent 时你会越来越常遇到「模型内部模拟执行」的现象，理解这类实验能帮你想清楚 tool use 和内部推理的边界。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-engineer-successfully-compiles-a-32-bit-risc-v-cpu-in-qwen-3-5-4b-llm-inserted-directly-into-its-weights-built-in-cpu-can-run-processor-arithmetic-operations-code-and-of-course-doom)

---

## 🌟 大厂 AI 动态

### 2. Anthropic 自曝「非常接近 RSI」：AI 开始能改进自己，公司同时给 Claude Code 加限制

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _Julie Bort_

同一天两条 Anthropic 新闻放在一起看才有意思：一边警告自己接近递归自我改进（RSI），一边确认给 Claude Code 加了禁止复刻游戏 IP 的系统提示。能力在加速，约束也在加码，这不是矛盾，是同一件事的两面。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Anthropic 公开表示已「非常接近」RSI 能力 | 「非常接近」是营销措辞还是内部评估，无量化指标 |
| RSI 指 AI 改进自身训练、引发能力加速的临界点 | RSI 定义本身在学界仍有争议，缺乏可测量标准 |
| 同日 Anthropic 确认 Claude Code 新增系统提示，禁止复刻现有游戏 | 限制游戏克隆是法律风险驱动还是能力担忧，官方未说明 |
| 用户报告 Opus 5.5 也在拦截逆向工程类任务 | 拦截逆向工程是否误伤正常开发，需看用户实测反馈 |
| 公司称正在「迭代以找到合适的平衡」 |  |

**📖 主编点评**

这条对你的 Agent 项目有直接含义：模型厂商正在系统提示层做价值对齐，你的 content-curator 如果调用 Claude，要预期某些任务会被静默拒绝。建议在 pipeline 里加一层「拒绝检测 + 备用模型切换」，这是工程上迟早要踩的坑。

📺 [打开原文](https://techcrunch.com/2026/11/02/anthropic-warns-that-its-very-close-to-rsi-capability-aka-self-building-ai/)

---

### 5. YC 的 Garry Tan 一年在 token 上花 20 万美元，自称得了「赛博精神病」

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Julie Bort_

Garry Tan 在播客里承认自己因为和 AI Agent 协作太兴奋，经常不怎么睡觉，一年 token 开销最高 20 万美元。这个数字比任何 benchmark 都更能说明重度 Agent 用户的真实成本结构。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Garry Tan 称年度 token 支出最高达 20 万美元 | 20 万美元是个人支出还是含 YC 团队，口径不明 |
| 他自嘲患有「cyber psychosis」，睡眠很少 | 这种使用强度是否可复制到普通开发者，存疑 |
| 说法出自 Walter Isaacson 播客新一期 | 高 token 消耗能否转化为实际产出，无公开数据 |
| Tan 是 Y Combinator 现任掌门 | 「Agent 重度用户」是否成为新的人群分层，尚属观察 |
| 他把高支出归因于对 Agent 协作的兴奋 |  |

**📖 主编点评**

这条给你一个成本锚点：重度 Agent 用户的年支出在六位数美元量级。你做 content-curator 时应该反过来想——哪些环节值得烧 token（选题判断、长文摘要），哪些必须走便宜模型或规则（去重、抓取）。成本结构设计比模型选型更影响项目能不能长期跑。

📺 [打开原文](https://techcrunch.com/2026/11/02/y-combinators-garry-tan-uses-ai-agents-so-much-he-spends-up-to-200k-a-year-on-tokens/)

---

## 🌟 股票

### 3. Intel 领跌，3.5 万亿美元芯片股回调扩散，AI 成本担忧开始反噬估值

**[股票]** · ⭐⭐⭐⭐ · _entryleveljobsc_

BBC 前一天刚报「AI 成本担忧引发科技股急跌」，今天 Intel 的跌势把回调推到 3.5 万亿规模。同一周 Oracle 申请发 200 亿新股和债券为 AI 建设融资——市场开始问一个简单问题：这些钱什么时候回来。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Intel 股价在公布疲弱 Q4 指引后持续下跌 | 这轮回调是估值修正还是泡沫破裂起点，尚无定论 |
| 芯片板块整体回调规模达 3.5 万亿美元 | Oracle 举债扩张能否被云收入覆盖，要看下两个季度 |
| Oracle 于 11-02 申请发行 200 亿美元新股与债券，用于 AI 基建 | Intel 的问题是自身制程还是行业周期，市场解读不一 |
| BBC 报道美国科技股因 AI 成本担忧出现急跌 | AI 资本开支的回报周期是否被系统性高估，仍属判断 |
| Alphabet 一度面临史上最大 5000 亿美元市值缩水 |  |

**📖 主编点评**

别把这条当财经八卦跳过。它决定你未来半年能不能拿到便宜的推理算力——芯片股回调往往先于云厂商降价。如果你在跑本地模型或租 GPU，现在是观察窗口，不是抄底窗口。

📺 [打开原文](https://finance.yahoo.com/markets/article/the-intel-stock-collapse-is-getting-worse--and-the-37-trillion-chip-rout-is-spreading-212154947.html)

---

## 📋 备选池

### AI 算力 / 半导体

- [OpenAI 考虑把数据中心改名为「AI 计算园区」，应对日益强烈的社区反弹](https://www.tomshardware.com/tech-industry/data-centers/openai-considers-rebranding-data-centers-to-ai-compute-campuses-as-data-center-backlash-intensifies-company-reportedly-sees-2028-presidential-election-becoming-an-ai-issue) —— 改名是公关动作，但透露 OpenAI 已把 AI 基建政治化，预判 2028 大选议题。
  _Newton Gitonga_
- [超 90% 公众评论反对数据中心，水是头号担忧](https://www.tomshardware.com/tech-industry/data-centers/america-hates-data-centers-new-database-reveals-more-than-90-percent-of-10-000-public-comments-are-negative-only-21-percent-mention-ai-73-percent-of-meetings-had-no-data-center-supporters-water-is-the-number-one-concern) —— 1 万条公众评论的量化数据，是理解 AI 基建社会成本最硬的一份材料。
  _Oliver Haslam_
- [开源 USB 工具解锁 Nvidia 半速 AI 限制器，FP16 性能提升最高 65%](https://www.tomshardware.com/pc-components/gpus/open-source-usb-tool-unlocks-nvidias-half-speed-gpu-ai-limiter-on-windows-lifts-gpus-fp16-math-performance-up-to-65-percent-uefi-unlocker-covers-rtx-20-30-and-40-series-desktops-and-laptops) —— 覆盖 RTX 20/30/40 系，对跑本地模型的你有实操价值，但有保修风险。
  _Shane Downing_
- [Nvidia Brev 平台安全事件，可能泄露客户 VM 的 SSH 密钥](https://www.tomshardware.com/tech-industry/cyber-security/nvidia-brev-security-breach-may-have-exposed-ssh-keys-used-to-access-customer-vms-investigation-finds-unauthorized-activity-spanning-16-days-but-no-evidence-of-misuse) —— 16 天未授权活动，如果你用 Brev 跑开发环境，现在该轮换密钥。
  _Newton Gitonga_
- [新型 AI 驱动 Windows 恶意软件把窃取数据喂给 Claude 按价值排序资产](https://www.tomshardware.com/tech-industry/cyber-security/new-ai-driven-windows-malware-feeds-stolen-data-to-claude-to-rank-victims-assets-by-value-then-deletes-itself-payload-builds-custom-target-assessment-can-switch-models-if-one-refuses-or-skip-the-ai-step-entirely) —— Cisco Talos 披露的 VOLTA 样本，是 LLM 被武器化的具体案例，值得安全向读者看。
  _Shane Downing_

### 大厂 AI 动态

- [Google 财报像极了当年的 Facebook，Stratechery 谈「Agent 这一手」](https://stratechery.com/2026/google-earnings-facebook-deja-vu-the-agent-play/) —— Ben Thompson 的框架值得读，把 Google 的激进和 Agent 战略串起来了。
  _Ben Thompson_
- [Gemini 4 Carbon 登顶 Artificial Analysis 智能指数 v5](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1) —— 模型排名变动，对选型有参考，但缺工程细节所以没上头条。
  _theHocineSaad_
- [纽约时报等多家媒体起诉 Brave 浏览器抓取内容](https://techcrunch.com/2026/11/02/new-york-times-and-other-outlets-sue-web-browser-brave-over-alleged-content-scraping/) —— 抓取的法律边界在收紧，做 content-curator 这类聚合工具要留意合规。
  _Rebecca Bellan_
- [42AI 出隐身模式，6250 万美元融资，做能「预测人类行为」的世界模型](https://techcrunch.com/2026/11/02/42ai-comes-out-of-stealth-with-62-5m-and-a-world-model-that-can-predict-human-behavior/) —— 世界模型赛道新玩家，宣称能预测行为，但缺技术细节，先观察。
  _Ram Iyer_

### 股票

- [Oracle 申请发行 200 亿美元新股与债券，为 AI 建设融资](https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html) —— 和头条的芯片回调是同一条叙事：AI 资本开支开始靠举债支撑。
  _smartmic_
- [研究机构称 Anthropic 的 IPO 是「对投资者轻信度的空前考验」](https://www.cnbc.com/2026/10/07/anthropic-will-be-most-ridiculous-ipo-of-year-analyst-says.html) —— 看空声音的代表，和 Anthropic 高增长叙事形成对照，值得两边都读。
  _m463_
- [3000 亿美元「债务墙」逼近 PE 支持的私人公司](https://www.wsj.com/finance/investing/a-300-billion-debt-wall-is-looming-over-private-equity-backed-companies-d6359497) —— AI 之外的系统性风险，和 AI 举债扩张叠加时会更危险。
  _JumpCrisscross_

### 金融

- [美国联邦预算赤字一年跳增 12%，逼近 2 万亿美元](https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html) —— 宏观底色，解释了为什么利率和 AI 融资成本同时承压。
  _ck2_
- [美国就业回暖，可能让美联储继续加息](https://www.bloomberg.com/news/articles/2026-10-31/us-jobs-pickup-may-keep-fed-on-track-to-hike-rates-again) —— 加息预期直接压制高估值 AI 股，和头条回调互为因果。
  _frank_clover_
- [DeepSeek 被美国土安全部下令禁止在联邦民用机构使用](https://www.reuters.com/technology/us-banning-chinese-ai-deepseek-government-agency-it-systems-2026-10-19/) —— 监管层面的实质动作，影响国内模型出海与合规讨论。
  _cmrdporcupine_

### AI

- [DeepSeek Harness 超详细教程：50 分钟吃透 DSH，让 SuperAgent 干活](http://www.bilibili.com/video/av117540671982699) —— 本周新发且是 DSH 首个系统教程，但属教程类，按你的偏好放备选。
  _Git源宝_
- [认真用 Claude Code 的人，迟早会遇见 Everything Claude Code](http://www.bilibili.com/video/av116319122885806) —— 116K star 的 Claude Code 配置项目实战讲解，斜杠命令、子代理、Hooks 都有，契合你的偏好但非本周新事。
  _极客魔导师_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
