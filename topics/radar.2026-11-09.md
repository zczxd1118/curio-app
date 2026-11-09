# Curio 趋势雷达 · 2026-11-09

> 你的私人主编 · 今日跨域精选 5 条头条 + 16 条备选

_今天最重要的信号有两个：一是 Nvidia 董事会正式调查黄仁勋与疑似中国间谍的关系，Yale 的 Sonnenfeld 给出「50-50 留任概率」——这不只是花边，是 AI 算力供应链最大单一节点的治理风险；二是 AI 交易在中期选举后遭遇 2.5 万亿美元级别的抛售，Nasdaq 进入回调区间，算力叙事第一次被政治与融资成本同时定价。工程侧则有一条被低估的：284B 参数 DeepSeek 在 64GB 内存、无 GPU 上跑起来了。_

---

## 🌟 大厂 AI 动态

### 1. 黄仁勋承认婚外情，Nvidia 董事会启动独立调查：Ben Thompson 判断「他能活下来，但影响力再也回不去了」

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _Ben Thompson_

周日 Nvidia 连发两份声明：黄仁勋致员工信承认与 Megaspeed 高管 Alice Huang 的关系，董事会成立独立委员会调查，同时表态「仍对 Jensen 和领导团队有信心」。美方情报口径称对方是中国国安部招募的「蜜罐」人员。Ben Thompson 的判断是：黄仁勋大概率留任，但他在华盛顿与供应链之间的斡旋资本被永久削弱。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 黄仁勋在致全员信中承认婚外情，Nvidia 官方新闻室发布了该信全文 | 董事会「有信心」的表态与「独立调查」并存，实际是给继任方案留时间窗，还是真心背书，目前无法判断 |
| 董事会成立独立委员会调查，同时公开表态支持黄仁勋及现有管理层 | Megaspeed 的走私指控与本案是否同一证据链，公开信息尚不完整 |
| 涉事方 Alice Huang 为 Megaspeed 高管，该公司此前被指向中国走私约 20 亿美元 AI 芯片 | 国会听证会的时间与议题范围未定，是否升级为出口管制立法尚不明朗 |
| 美国情报备忘录称中国国安部招募该女性针对黄仁勋，属「蜜罐」行动 | 黄仁勋若留任，其对华游说能力受损程度难以量化，供应链政策走向仍是变量 |
| 黄仁勋已被正式传唤至国会就中国间谍问题作证 | Nvidia 股价与 AI 板块的联动反应尚未充分定价治理风险 |
| Yale 管理学者 Jeffrey Sonnenfeld 估算其留任概率「大约 50-50」 |  |

**📖 主编点评**

这条你该读 Stratechery 原文而不是新闻标题——Thompson 拆的是「CEO 个人影响力作为公司资产」这件事怎么被折价。对你的实际含义：如果你在做任何依赖 Nvidia 生态的技术选型或简历叙事，把「单一供应商治理风险」写进你的判断框架里，比复述新闻有价值得多。

📺 [打开原文](https://stratechery.com/2026/jensen-huangs-affair-the-culper-report-huangs-righteousness/)

---

## 🌟 股票

### 2. 中期选举后 AI 交易崩解：2.5 万亿美元市值蒸发，Nasdaq 跌入回调区间，芯片股创 1896 年以来最差中期选举次日

**[股票]** · ⭐⭐⭐⭐⭐ · _madihaa_

民主党中期选举大胜后，市场把「数据中心扩张受阻」重新定价：Nasdaq 单日跌 4-5% 进入回调，芯片板块遭遇 3.5 万亿美元级别的抛售，Intel 领跌。对冲基金据报已清空 2025 年以来建仓的全部 AI 股票。这是 AI 叙事第一次被政治变量而非业绩变量主导定价。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Nasdaq 跌约 4-5% 进入技术性回调区间，单日市值蒸发规模约 2.5 万亿美元 | 抛售是政治事件的短期情绪反应，还是 AI 资本开支周期的真实拐点，需要看 Q4 财报验证 |
| 芯片股创 1896 年以来最差的中期选举次日表现，Intel 跌幅居前 | 数据中心电力与选址的政治阻力是否形成长期约束，目前只有州级信号 |
| Oracle 申报发行 200 亿美元新股与债券为 AI 基建融资 | Oracle 200 亿美元融资的认购情况尚未披露，是观察机构胃口的直接指标 |
| 德州州长选举结果被市场解读为数据中心扩张风险上升 | Anthropic IPO 估值（传 1.5 万亿）能否成立，将检验这轮抛售的深度 |
| 美对冲基金据报已卖出 2025 年以来买入的全部 AI 股票 | 「AI 泡沫」论调与真实算力需求之间的缺口，尚无数据能证伪任一方 |

**📖 主编点评**

别把这条当财经八卦看。你正在做的 content-curator 如果未来要接任何模型 API，成本曲线和供应商稳定性会直接受这轮定价影响——现在就该想清楚「模型可替换」的架构，而不是绑死一家。另外，这轮抛售是绝佳的观察窗口：谁在跌的时候还在扩产，谁才是真需求。

📺 [打开原文](https://finlaws.substack.com/p/25t-has-been-wiped-from-us-stocks)

---

## 🌟 AI 算力 / 半导体

### 3. llama-modchip：284B 参数 DeepSeek 在 64GB 内存、无 GPU 的机器上跑起来，HN 429 分

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _joshcsimmons_

一个 GitHub 项目把 284B 参数的 DeepSeek 模型塞进了 64GB 内存的纯 CPU 环境，不依赖 GPU。同期还有 homelab 玩家用二代 Optane 持久内存跑 2.8 万亿参数的 Kimi K3，1-bit 量化下 0.85 tokens/s。这两条放在一起说明：内存带宽与量化技术正在把「大模型必须上 GPU」这条假设撕开一个口子。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| llama-modchip 项目在 HN 获 429 分，实现 284B DeepSeek 模型在 64GB RAM 无 GPU 环境运行 | 0.85 tokens/s 的实际可用性极低，这类方案目前是技术验证而非生产可用 |
| Reddit homelab 用户用 Optane PMem 200 跑 Kimi K3（2.8T 参数），1-bit 量化下 0.85 tokens/s | llama-modchip 的具体量化方案与内存布局未在摘要中说明，需读源码判断可复现性 |
| 该用户警告 Optane 发热会烧毁邻近 DRAM，需用鼓风机散热 | Optane 已停产，这条路线依赖二手硬件，不具备规模化意义 |
| 同期 CPU-Z 数据显示 64GB 内存 PC 占比同比下滑 18%，因 AI DRAM 涨价 | 内存涨价是否会反过来压制本地推理社区的增长，尚待观察 |
| TSMC 否认应 Nvidia 要求探索 3D DRAM，称该技术距量产仍有数年 | 「无 GPU 跑大模型」与「边缘设备跑小模型」是两条不同路线，别混为一谈 |

**📖 主编点评**

这条对你的价值不在「能不能用」，而在「为什么能」——去读 llama-modchip 的 README，看它怎么做权重分片和量化调度，这套思路直接能迁移到你的 Agent 项目的本地推理降本上。如果你哪天要给 content-curator 加一个本地小模型做初筛，这就是现成的工程参考。

📺 [打开原文](https://github.com/synchopate/llama-modchip)

---

## 🌟 AI

### 4. Claude Desktop 把 Claude Code、Design、Cowork 三合一：命令行 Agent 正在变成桌面客户端完全体

**[AI]** · ⭐⭐⭐⭐ · _技术爬爬虾_

11 月 8 日发布的这条实测指出，Claude 桌面端已把 Claude Code 的编程能力、Claude Design 的设计能力、Claude Cowork 的办公能力收进同一个客户端，配合 Opus 5.5。这是 Agent 产品形态的一次明确转向：从「终端里的工具」变成「操作系统级的常驻入口」。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Claude Desktop 近期更新将 Claude Code 从纯命令行形态整合进桌面客户端 | 桌面客户端是否真能替代终端工作流，取决于它对本地文件系统与 shell 的权限模型，视频未深入 |
| 同一客户端内整合了 Claude Design 与 Claude Cowork 两条产品线 | 三合一是否意味着 Anthropic 在做「Agent OS」的入口卡位，官方未表态 |
| 视频实测基于 Opus 5.5 模型 | Opus 5.5 在长任务上的稳定性缺乏第三方基准 |
| 同期 HN 讨论指出 Gemini 对订阅用户也在用聊天历史训练（734 分），隐私边界在收紧 | 隐私训练争议可能影响企业侧采用节奏 |
| Apple 据报正加速让 Siri 具备 agentic 能力，对标 OpenAI Dots 与 Meta Muse | 与 Cursor/Windsurf 的竞争边界会怎么划，目前看不清 |

**📖 主编点评**

你天天用 Claude Code，这条值得花 20 分钟看——重点不是功能罗列，而是观察 Anthropic 怎么设计「Agent 的权限与上下文边界」。这套交互范式很可能成为你 content-curator 前端形态的参考：是继续做 CLI，还是做一个常驻的桌面面板。看完再决定你的项目往哪走。

📺 [打开原文](http://www.bilibili.com/video/av117580048108571)

---

## 🌟 金融

### 5. Tesla 停产 Cybertruck：一款产品从发布到退场的完整失败样本，HN 1155 分

**[金融]** · ⭐⭐⭐⭐ · _PLenz_

Tesla 确认将逐步关停 Cybertruck 产线，原因是销量长期不及预期。同期数据显示 Tesla 与 SpaceX 两日合计蒸发逾 4200 亿美元市值，CleanTechnica 的文章把矛头指向 JB Straubel 离职后「再没成功发布过新产品」。这是本周 HN 讨论度最高的一条，也是产品决策的反面教材。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Tesla 官方确认将逐步关停 Cybertruck 生产 | 停产是彻底放弃还是转产线做别的车型，官方表述含糊 |
| 停产原因为上市多年销量持续低迷 | 市值蒸发与 Cybertruck 停产的因果强度难以分离，中期选举后的板块抛售是更大变量 |
| Tesla 与 SpaceX 两日内合计市值蒸发超 4200 亿美元 | SpaceX 的估值波动与 Tesla 是否同源，缺乏拆分数据 |
| CleanTechnica 统计称自 JB Straubel 卸任 CTO 后 Tesla 无成功新品发布 | 「Straubel 之后无成功产品」是相关性叙事，不能直接当因果 |
| Tesla Semi 此前在 I-880 发生无碰撞起火事故 | Cybertruck 的品牌残值对 Tesla 后续车型的影响未知 |

**📖 主编点评**

这条对你有用的地方是「产品决策复盘」的素材：一个被创始人审美强推、无视市场反馈的产品线，最后怎么收场。你做 content-curator 时同样会面临「我自己觉得酷」和「用户真的要用」的拉扯——把这条存下来，下次你想加一个花哨功能时翻出来看。

📺 [打开原文](https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817)

---

## 📋 备选池

### 大厂 AI 动态

- [Gemini 4 Carbon 登顶 Artificial Analysis 智能指数 v5](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1) —— 第三方基准上的第一名易主，值得记一笔，但缺少工程细节，放备选。
  _theHocineSaad_
- [Apple 据报正加速让 Siri 具备 agentic 能力](https://www.theverge.com/ai-artificial-intelligence/1029552/apple-siri-ai-agentic) —— Gurman 爆料 Ternus 施压 Federighi 加速 Siri 路线图，对标 OpenAI Dots——大厂 Agent 入口战的又一枚棋子。
  _Terrence O’Brien_
- [Gemini 对订阅用户也在用聊天历史训练](https://news.ycombinator.com/item?id=50363461) —— HN 734 分，隐私边界问题；对你选型时的数据合规判断有直接参考价值。
  _jameslk_
- [Agent Clan：用手势指挥你的 Claude Code 和 Codex Agent](https://www.producthunt.com/products/agent-clan) —— Product Hunt 新品，多 Agent 编排的交互实验，思路比完成度更值得看。
  _鄭策（TSETSE）_

### AI 算力 / 半导体

- [DeepX 流片二代芯片，LPDDR5x-PIM 架构宣称 6.7 倍性能提升](https://www.eetimes.com/deepx-tapes-out-second-gen-chip-projects-6-7x-performance-gain-with-lpddr5x-pim/) —— 5W 以内跑大模型，存内计算路线在边缘侧的又一次下注，数字漂亮但需等实测。
  _Sally Ward-Foxton_
- [Diamond Foundry 造出全球首片 200mm 单晶金刚石晶圆](https://www.tomshardware.com/pc-components/cooling/diamond-foundry-creates-worlds-first-200mm-single-crystal-diamond-wafer-massive-gem-aims-to-solve-ai-chip-cooling-crisis-envisioned-as-a-cooling-material-for-semiconductors) —— 冲着 AI 芯片散热危机去的材料突破，200mm 尺寸是关键，但离量产还远。
  _Jowi Morales_
- [Nvidia RTX Spark 加密固件把 Linux 上推理速度压到 35%](https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop) —— HN 617 分，本地推理玩家必看：买卡之前先确认固件策略，这是实打实的踩坑预警。
  _novaRom_
- [开源 GPU 任务管理器 gputaskman 精确显示谁在吃你的 VRAM](https://www.tomshardware.com/pc-components/gpus/open-source-gpu-task-manager-reveals-exactly-whats-eating-your-vram-microsoft-vps-new-gpu-taskman-tool-reveals-every-process-using-your-gpu-how-much-memory-each-uses-and-breaks-down-ai-and-llm-workloads) —— 微软 VP Scott Hanselman 发布的小工具，能拆分 AI/LLM 负载，本地调试刚需。
  _Mark Tyson_
- [Synaptics 向开源 DisplayLink 驱动作者发律师函，还「激将」其公开威胁](https://www.tomshardware.com/peripherals/docking-stations-hubs/synaptics-sends-cease-and-desist-order-to-creator-of-open-source-displaylink-driver-dares-him-to-publicize-its-threats-dev-reverse-engineers-displaylink-using-claude-ai-and-rust-synaptics-threatens-to-bill-creator-for-legal-documentation) —— 开发者用 Claude AI + Rust 逆向 DisplayLink 被发函，AI 辅助逆向的法律边界案例。
  _Jowi Morales_

### 股票

- [Anthropic IPO 估值 1.5 万亿美元遭大型投资者质疑](https://www.wsj.com/finance/major-investors-are-skeptical-anthropic-ipo-can-achieve-1-5-trillion-valuation-ca965d8b) —— Michael Burry 说 Anthropic 在「赌上存在」，配合本周抛售看，这是 AI 估值叙事的压力测试点。
  _sandinmyjoints_
- [Oracle 申报发行 200 亿美元新股与债券为 AI 基建融资](https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html) —— AI 资本开支从「利润支撑」转向「举债支撑」的标志性动作，认购情况值得跟踪。
  _smartmic_

### 金融

- [Tesla 与 SpaceX 两日合计蒸发逾 4200 亿美元市值](https://techlaws.pages.dev/tesla-and-spacex-lose-over-420b-in-combined-market-cap-in-the-two-days/) —— 与 Cybertruck 停产同源，但把 SpaceX 拉进来后是另一个量级的信号。
  _Pepitobombito_
- [美国联邦赤字一年跳增 12%，逼近 2 万亿美元](https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html) —— 利率与 AI 基建融资成本的宏观底色，解释了为什么这轮抛售来得这么急。
  _ck2_
- [3000 亿美元「债务墙」逼近 PE 控股公司](https://www.wsj.com/finance/investing/a-300-billion-debt-wall-is-looming-over-private-equity-backed-companies-d6359497) —— AI 基建之外的另一条杠杆风险线，和数据中心融资是同一批资金在承压。
  _JumpCrisscross_

### AI

- [DeepSeek Harness 实测对比 Claude Code：同一模型，工具链差距比想象大](http://www.bilibili.com/video/av117100337236191) —— 用同一个 DeepSeek Pro 0813 模型在两个 harness 里跑同样任务，结论是插件化与缓存命中决定成败——工程视角对味。
  _程序员晓刘_
- [mcp2cli：一个 CLI 干掉所有 MCP 工具，省 99% token](http://www.bilibili.com/video/av116204349953548) —— 核心实现只有一个 Python 文件，用「懒发现」把 MCP 的 token 浪费从数十万降到几千，你的 Agent 项目直接能借鉴。
  _探索未至之境_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
