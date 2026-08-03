# Curio 趋势雷达 · 2026-08-03

> 你的私人主编 · 今日跨域精选 5 条头条 + 16 条备选

_今日核心信号：AI 算力链遭遇全球性去杠杆，韩国 KOSPI 暴跌、存储股重挫，但阿里发布千问 3.8-Max 开源模型，性能对标 Anthropic Fable 5，为市场注入强心剂。同时，SpaceX 首份季报在即，股价已跌去近半，成为观察 AI 泡沫成色的关键。_

---

## 🌟 AI

### 1. 阿里发布千问 3.8-Max：2.4 万亿参数开源，性能对标 Anthropic Fable 5

**[AI]** · ⭐⭐⭐⭐⭐ · _华尔街见闻_

阿里巴巴今日发布千问 3.8-Max，参数规模达 2.4 万亿，是千问家族最强模型，也是首个开源 Max 级权重的版本（下周发布）。API 定价输入 2.0 美元/百万 tokens、输出 6.0 美元/百万 tokens。基准测试显示其编程与通用智能体能力与 Anthropic Fable 5 相当，部分指标超越，并在芯片设计、量化研究、电商模拟等长程任务中展现出显著的自主执行能力。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 千问 3.8-Max 参数规模 2.4 万亿，为千问家族迄今最强模型 | 基准测试的具体方法论和测试集尚未公开，需独立验证 |
| API 定价：输入 2.0 美元/百万 tokens，输出 6.0 美元/百万 tokens | 与 Anthropic Fable 5 的对比是否涵盖所有关键场景，尚不明确 |
| 基准测试显示编程与通用智能体能力与 Anthropic Fable 5 相当，部分指标超越 | 开源版本的实际推理成本和部署难度有待评估 |
| 在芯片设计、量化研究、电商模拟等长程任务中展现显著自主执行能力 | 长程任务能力是否能在真实生产环境中稳定复现，仍需观察 |
| 下周将发布开源 Max 级权重版本 |  |

**📖 主编点评**

千问 3.8-Max 的开源策略直接冲击闭源模型市场，你应该关注其权重发布后的社区评测和微调案例。对于你的 Agent 项目，可以尝试用其 API 或本地部署测试长程任务处理能力，尤其在工具调用和自主规划方面。同时，留意阿里云生态的配套工具链，可能成为你构建 content-curator 的替代方案。

📺 [打开原文](https://wallstreetcn.com/articles/3778546)

---

### 5. DeepSeek V4 Flash 实测：Claude Code 接入后连续开发 7 个项目，逼近 Opus 4.8

**[AI]** · ⭐⭐⭐⭐ · _AI超元域_

DeepSeek 发布 V4 Flash 0731 版本，284B 总参数、13B 激活参数、100 万 Token 上下文，官方基准表现接近 Claude Opus 4.8。UP 主实测将其接入 Claude Code，连续开发 7 个项目，评估其性能、速度与真实短板，并与 Kimi K3 对比。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DeepSeek V4 Flash 0731 版本发布 | 官方基准与真实场景表现可能存在差距 |
| 284B 总参数、13B 激活参数、100 万 Token 上下文 | 13B 激活参数的实际推理效率，需进一步验证 |
| 官方基准表现接近 Claude Opus 4.8 | 100 万 Token 上下文的实用性，取决于具体任务 |
| UP 主实测接入 Claude Code 连续开发 7 个项目 | 与 Claude Opus 4.8 的差距在哪些方面，尚不明确 |
| 与 Kimi K3 进行了对比 |  |

**📖 主编点评**

DeepSeek V4 Flash 的低成本和高性能，可能成为你构建 Agent 的性价比之选。建议你观看视频，了解其在 Claude Code 中的实际表现，特别是长上下文和复杂任务处理能力。如果表现稳定，可以尝试将其作为 content-curator 的底层模型，降低 API 成本。

📺 [打开原文](http://www.bilibili.com/video/av117014605731815)

---

## 🌟 金融

### 2. 韩国 KOSPI 再暴跌超 5%，监管拟强制降杠杆，存储股领跌

**[金融]** · ⭐⭐⭐⭐⭐ · _华尔街见闻_

韩股今日再遭重挫，KOSDAQ 触发熔断，三星电子、SK海力士单日跌超 7%。监管层加速推进“紧急行动权限”立法，拟在市场剧烈波动时直接将单股杠杆 ETF 倍数从 2 倍强制下调至 1.5 倍乃至 1.1 倍。但机构普遍判断杠杆风险尚未完全出清，8 月中旬政策落地前韩股高波动格局难以打破。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| KOSPI 今日暴跌超 5%，KOSDAQ 触发熔断机制 | 监管干预能否有效遏制抛售，尚待观察 |
| 三星电子、SK海力士单日跌超 7% | 杠杆出清是否接近尾声，机构观点存在分歧 |
| 韩国监管拟将单股杠杆 ETF 倍数从 2 倍强制下调至 1.5 倍乃至 1.1 倍 | 存储芯片价格走势是否已见顶，影响后续市场情绪 |
| 机构普遍判断杠杆风险尚未完全出清 | 韩国市场波动是否会传导至全球 AI 算力链，需持续跟踪 |
| 8 月中旬政策落地前韩股高波动格局难以打破 |  |

**📖 主编点评**

韩国市场的暴跌是全球 AI 去杠杆的缩影，直接影响存储芯片价格和供应链预期。对于你关注的 AI 工程实践，存储成本可能短期波动，但长期看，HBM 等高端存储需求仍强劲。建议你关注 SK 海力士和三星的后续财报，以及长鑫存储等国产替代的进展，这会影响你构建 Agent 时的硬件成本。

📺 [打开原文](https://wallstreetcn.com/articles/3778557)

---

## 🌟 半导体

### 3. Lumentum CEO 警告：磷化铟短缺将比存储更严重，硅光子材料告急

**[半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

Lumentum CEO Michael Hurlston 在 RAISE 峰会上表示，磷化铟（InP）正面临比存储更严重的短缺。目前 fab 和材料供应已落后客户需求 30%，而共封装光学（CPO）需求激增，将进一步加剧供需失衡。这一瓶颈将影响硅光子、光互连等 AI 基础设施的关键组件。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Lumentum CEO 在 RAISE 峰会上发出磷化铟短缺警告 | 短缺持续时间尚不明确，可能影响未来 1-2 年供应链 |
| fab 和材料供应已落后客户需求 30% | 替代材料或新产能能否及时补充，存在不确定性 |
| 共封装光学（CPO）需求激增，加剧供需失衡 | 对 AI 基础设施成本的影响程度，有待量化 |
| 磷化铟是硅光子、光互连的关键材料 | 是否会导致光模块价格上涨，需观察市场反应 |

**📖 主编点评**

磷化铟短缺将推高光模块和 CPO 成本，直接影响 AI 数据中心的建设成本。对于你关注的 AI 工程实践，这意味着未来部署大规模模型时，网络互连成本可能上升。建议你关注光通信领域的国产替代机会，以及 CPO 技术的成熟度，这可能影响你未来构建分布式 Agent 系统的架构选择。

📺 [打开原文](https://www.tomshardware.com/tech-industry/semiconductors/lumentum-ceo-says-the-indium-phosphide-shortage-will-become-worse-than-memory)

---

## 🌟 大厂讯息

### 4. SpaceX 首份季报明日发布：股价已跌 46%，12 亿股解禁压顶

**[大厂讯息]** · ⭐⭐⭐⭐ · _华尔街见闻_

SpaceX 将于 8 月 4 日发布上市后首份季报。尽管股价自高点已下挫 46%，且面临超 12 亿股解禁抛压，但市场聚焦于 AI 数据中心租赁带来的营收弹性、Starlink 订阅用户增长以及 Starship 第 14 次飞测进展。华尔街预估二季度营收约 69 亿美元，该财报被视为能否扭转股价颓势的关键。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| SpaceX 将于 8 月 4 日发布上市后首份季报 | 财报能否超预期，存在不确定性 |
| 股价自高点已下挫 46% | 解禁抛压对股价的实际影响，尚待观察 |
| 面临超 12 亿股解禁抛压 | AI 数据中心租赁业务的营收贡献，需要财报数据验证 |
| 华尔街预估二季度营收约 69 亿美元 | Starship 飞测进展是否顺利，影响长期估值 |
| 市场关注 AI 数据中心租赁、Starlink 用户增长和 Starship 进展 |  |

**📖 主编点评**

SpaceX 的财报是观察 AI 基建投资回报的窗口。如果 AI 数据中心租赁收入强劲，说明算力需求依然旺盛，你的 Agent 项目可以继续依赖云服务；如果不及预期，可能引发 AI 泡沫担忧，影响整个行业的融资环境。建议你关注财报后的市场反应，并调整你的技术选型策略。

📺 [打开原文](https://wallstreetcn.com/articles/3778555)

---

## 📋 备选池

### AI

- [【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！](http://www.bilibili.com/video/av115897075242856) —— 吴恩达的 Agent 教程，系统覆盖设计模式、工具集成与评估，适合作为 Agent 构建的系统性参考。
  _吴恩达Agent_
- [从零开始，学会让桌面Agent帮你干活！【小白教程】](http://www.bilibili.com/video/av116861865887789) —— 国产桌面 Agent 实操教程，覆盖 8 大用法，适合快速上手桌面自动化。
  _秋芝2046_
- [零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor](http://www.bilibili.com/video/av116711944620974) —— 尚硅谷的 Vibe Coding 实战教程，从零开始用自然语言指挥 AI 开发项目，适合入门。
  _尚硅谷_
- [从夯到拉，锐评 32 个 AI 编程工具！](http://www.bilibili.com/video/av116578532200786) —— 鱼皮实测 32 个 AI 编程工具，帮你快速找到最适合自己的，避免踩坑。
  _程序员鱼皮_
- [Claude Code Agent Teams上手指南+项目实测](http://www.bilibili.com/video/av116037064331269) —— 深入讲解 Claude Code Agent Teams 的架构与实战，解决复杂任务并行处理问题。
  _程序员阿江-Relakkes_
- [MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。](http://www.bilibili.com/video/av114155298228756) —— MCP 概念与实战全覆盖，适合理解 Agent 工具调用的底层原理。
  _技术爬爬虾_
- [【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！](http://www.bilibili.com/video/av116951003242391) —— 吴恩达的 Vibe Coding 教程，强调标准化流水线，适合建立规范开发流程。
  _吴恩达AIAgent_
- [用Codex、cursor 还是Claude ？程序员不作选择题，我都要用，还一起用 | Orca ADE 介绍](http://www.bilibili.com/video/av116996217838997) —— Orca ADE 整合多 Agent 协作，开源免费，适合探索多工具协同工作流。
  _技术胖_
- [10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型](http://www.bilibili.com/video/av116579891153749) —— 快速在 Ubuntu 上配置 Claude Code 并接入 DeepSeek V4，低成本体验。
  _不倒翁lhj_

### 半导体

- [CEA-Leti Pushes Stacking Roadmap as AI Runs Into Memory and Power Limits](https://www.eetimes.com/cea-leti-pushes-stacking-roadmap-as-ai-runs-into-memory-and-power-limits/) —— CEA-Leti 押注 3D 堆叠与 chiplet，应对 AI 内存墙与功耗瓶颈，值得关注。
  _EE Times_
- [Hygon Reveals 512-Thread CPU and AI GPU to Rival Intel Xeon and Nvidia](https://www.ubergizmo.com/2026/06/hygon-512-thread-cpu/) —— 海光发布 512 线程 CPU 和 AI GPU，国产算力新选择，关注其性能与生态。
  _Ubergizmo_
- [Big tech spends more than $1 trillion on AI infrastructure — additional $745 billion expected in 2026](https://www.tomshardware.com/tech-industry/big-tech/big-tech-spends-more-than-usd1-trillion-on-ai-infrastructure-additional-usd745-billion-expected-to-be-added-to-the-figure-in-2026-alone) —— 四大科技巨头 AI 资本开支超 1 万亿美元，2026 年再投 7450 亿，算力需求持续。
  _Tom's Hardware_

### 大厂讯息

- [Gemini Robotics 2 brings whole body intelligence to robots](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/) —— Gemini Robotics 2 发布，机器人全身智能，关注具身智能进展。
  _Google DeepMind_
- [Document-borne AI worms can self-propagate through Copilot for Word](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/) —— AI 蠕虫可通过 Word 文档在 Copilot 中自我传播，安全风险需警惕。
  _Hacker News_

### 金融

- [高盛旗帜鲜明：这是人类历史上最大规模的资本需求周期，美联储只是看客](https://wallstreetcn.com/articles/3778540) —— 高盛认为资本稀缺时代来临，AI 基建与再工业化推升资本成本，影响投资范式。
  _华尔街见闻_
- [去杠杆冲击之下，算力核心逻辑变了吗？](https://wallstreetcn.com/articles/3778530) —— 中信建投分析韩国去杠杆影响，算力逻辑从涨价转向订单兑现，关注产能释放。
  _华尔街见闻_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
