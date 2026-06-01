# Curio 趋势雷达 · 2026-06-01

> 你的私人主编 · 今日跨域精选 4 条头条 + 12 条备选

_今天 Computex 2026 开幕，英伟达正式发布 RTX Spark 超级芯片，联手微软将 Windows 变成 Agentic AI OS，这是 PC 产业的分水岭。同时，宇树科技 73 天闪电过会，A 股具身智能第一股即将诞生。AI 编程工具赛道持续内卷，Claude Code vs Codex 实测对比出炉。_

---

## 🌟 AI 算力 / 半导体

### 1. 英伟达发布 RTX Spark 超级芯片：20核Arm CPU + Blackwell GPU，128GB统一内存，Windows 变身 Agentic AI OS

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

Computex 2026 首日，黄仁勋正式揭晓 RTX Spark 平台。这不是又一款 GPU，而是一颗完整的 SoC——20 核 Arm CPU 搭配 6144 CUDA 核心的 Blackwell GPU，最高 128GB 统一内存，目标是把本地 AI 推理和 Agent 能力塞进笔记本和桌面。微软同步推出 Surface Laptop Ultra 首发搭载，Windows 终于有了真正能跑大模型的本地硬件。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| RTX Spark 采用 20 核 Arm CPU + Blackwell GPU，CUDA 核心数 6144，匹配桌面 RTX 5070 级别 | RTX Spark 能否真正挑战苹果 Mac 系列在本地 AI 推理上的地位，取决于软件生态和开发者支持 |
| 最高 128GB 统一内存，支持本地运行大模型推理 | 128GB 统一内存对个人开发者跑 70B 模型够用，但多卡扩展性未知 |
| 微软 Surface Laptop Ultra 首发搭载，配备 15 英寸 mini-LED PixelSense Ultra 显示屏 | Intel 和 AMD 如何应对 Arm 架构入侵 PC 市场，x86 生态护城河是否会被突破 |
| 英伟达公布三代路线图：当前 Rubin（LPDDR6），后续 Rosa、Feynman | 定价尚未公布，若过高可能仅限高端市场，难以普及 |
| 与微软联合宣布 Windows 将深度集成 Agentic AI 能力 | Agentic AI OS 的具体形态和用户体验还需实测验证 |

**📖 主编点评**

如果你在做 AI Agent 或个人 Side Project，RTX Spark 意味着你可以在笔记本上本地跑大模型推理，不再依赖云端 API。这对你的 content-curator 项目是利好——本地部署 RAG 和 Agent 的硬件门槛大幅降低。建议关注 Surface Laptop Ultra 的评测，特别是统一内存带宽和实际推理速度。

📺 [打开原文](https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory)

---

## 🌟 股票

### 2. 宇树科技 73 天闪电过会，A 股具身智能第一股估值至少 420 亿元

**[股票]** · ⭐⭐⭐⭐⭐ · _华尔街见闻_

从 IPO 受理到过会仅 73 天，宇树科技刷新了 A 股纪录。按发行比例不低于 10% 测算，整体估值至少 420 亿元，业内预期实际市值将远高于此。这是具身智能赛道在资本市场的里程碑事件——人形机器人从概念走向 IPO，意味着产业成熟度获得监管和资本双重认可。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 宇树科技从 IPO 受理到过会仅用 73 天，创 A 股纪录 | 420 亿估值是否合理，取决于人形机器人商业化落地速度 |
| 按发行比例不低于 10% 测算，整体估值至少 420 亿元 | 宇树科技在消费级市场的占比和盈利能力尚未公开 |
| 宇树科技是 A 股具身智能第一股 | 具身智能赛道当前估值偏高，需警惕二级市场炒作风险 |
| 公司主营业务包括四足机器人、人形机器人及核心零部件 | 过会后到正式上市还有流程，时间窗口不确定 |

**📖 主编点评**

具身智能从实验室走向 IPO，说明资本市场开始为机器人赛道买单。如果你关注 AI 硬件落地，宇树的过会是一个重要信号——人形机器人不再是 PPT 项目。但作为个人开发者，短期内更值得关注的是宇树开源的控制算法和 SDK，这些可能成为你 Side Project 的组件。

📺 [打开原文](https://wallstreetcn.com/articles/3773573)

---

## 🌟 AI

### 3. 100 小时实测 Claude Code vs Codex：结果令人意外

**[AI]** · ⭐⭐⭐⭐ · _设计之道_

一位开发者花了 100 小时，用相同的提示词和项目构建任务，对比测试 Claude Code 和 Codex。结果并非一边倒——Claude Code 在复杂多文件重构上更强，Codex 在快速原型和简单任务上速度更快。这不是又一篇工具评测，而是给所有 Vibe Coding 用户的实战参考：选工具要看场景。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 测试时长 100 小时，使用相同提示词和项目构建任务 | 测试样本量有限，结论可能不适用于所有项目类型 |
| Claude Code 在复杂多文件重构和跨文件修改上表现更好 | 工具版本更新快，当前结论可能在未来 1-2 个月内失效 |
| Codex 在快速原型和简单任务上速度更快 | 个人偏好和熟悉度对效率影响很大，客观对比难完全排除主观因素 |
| 两者在代码质量和错误率上互有胜负 | 未涉及 MCP 集成和自定义 Skills 的对比 |

**📖 主编点评**

如果你在做 content-curator 这类多文件、多模块的 Agent 项目，Claude Code 的复杂任务处理能力可能更适合。但 Codex 的快速迭代能力也不容忽视——建议两个工具都装，根据任务类型切换。另外，关注视频中提到的具体 commands 和 prompts，这些细节比结论更有价值。

📺 [打开原文](http://www.bilibili.com/video/av116656495925868)

---

## 🌟 大厂 AI 动态

### 4. GitHub Copilot 改按 Token 计费，开发者炸锅

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _TechCrunch_

GitHub Copilot 宣布从固定订阅制转向 Token 计费模式，引发开发者强烈不满。新计费方式下，频繁使用 AI 补全的开发者成本可能翻倍。这标志着 AI 编程工具的商业模式从“无限畅吃”转向“按量付费”，对重度用户影响巨大。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| GitHub Copilot 从固定订阅制转向 Token 计费模式 | Token 计费的具体单价和免费额度尚未公布，实际影响待评估 |
| 频繁使用 AI 补全的开发者成本可能翻倍 | 此举可能推动开发者转向 Cursor、Windsurf 等竞品 |
| 开发者社区反应强烈，称新计费方式为 'a joke' | 微软可能后续调整策略，类似之前 VS Code 'Co-Authored by Copilot' 争议后的妥协 |
| 微软官方尚未回应开发者反馈 | 对偶尔使用 Copilot 的开发者影响有限，重度用户需重新评估成本 |

**📖 主编点评**

如果你重度依赖 Copilot（比如每天写几百行 AI 辅助代码），新计费模式可能让你的月支出从 10 美元涨到 30-50 美元。建议提前评估使用量，对比 Cursor 和 Windsurf 的定价。对于你的 content-curator 项目，如果主要用 Claude Code 或 Codex，Copilot 的变动影响不大，但值得关注行业定价趋势。

📺 [打开原文](https://techcrunch.com/2026/05/30/what-a-joke-github-copilots-new-token-based-billing-spurs-consternation-among-devs)

---

## 📋 备选池

### AI 算力 / 半导体

- [Intel Xeon 6+ Clearwater Forest：288 核，18A 工艺数据中心 CPU](https://www.tomshardware.com/pc-components/cpus/intel-xeon-6-clearwater-forest-puts-18a-in-the-data-center-with-up-to-288-cores-576-mb-of-l3-cache-new-xeon-6990e-is-30-percent-faster-per-thread-than-192-core-amd-epyc-9965-says-intel) —— Intel 在 Computex 上展示 288 核 Clearwater Forest，18A 工艺，单线程比 AMD 192 核 Epyc 快 30%，但量产时间未定。
  _Tom's Hardware_
- [SoftBank 投资 870 亿美元建设法国 AI 数据中心](https://www.tomshardware.com/tech-industry/softbank-to-spend-up-to-75-billion-on-french-ai-data-centers) —— SoftBank 利用法国核电优势，计划建设 5GW 数据中心，但自身负债超 1300 亿美元，资金链存疑。
  _Tom's Hardware_
- [韩国 5 月芯片出口 372 亿美元创历史新高](https://wallstreetcn.com/articles/3773558) —— AI 芯片需求驱动韩国出口同比飙升 53.2%，三星和 SK Hynix 坐享红利，但周期性风险需警惕。
  _华尔街见闻_
- [AMD 确认 AM5 支持至 2029 年，重推 5800X3D 和 7700X3D](https://www.tomshardware.com/pc-components/cpus/amd-confirms-am5-support-through-2029-zen-4-and-5-platform-will-likely-see-two-more-generations-at-least) —— AMD 延长 AM5 寿命至 2029 年，并重新推出 5800X3D 和 7700X3D 应对涨价，对 DIY 玩家是利好。
  _Tom's Hardware_

### 大厂 AI 动态

- [微软 Surface Laptop Ultra 首发搭载 RTX Spark](https://www.theverge.com/tech/940584/microsoft-surface-laptop-ultra-nvidia-rtx-spark-pictures) —— 微软再次押注 Arm+Nvidia，Surface Laptop Ultra 配备 RTX Spark，128GB 内存，但定价未公布。
  _The Verge_
- [Meta 正在开发 AI 挂坠](https://techcrunch.com/2026/05/30/meta-is-reportedly-developing-an-ai-pendant/) —— Meta 继续押注 AI 硬件，AI 挂坠可能是 Ray-Ban 眼镜后的新形态，但具体功能未披露。
  _TechCrunch_
- [Google Gemini Spark 24/7 AI 助手实测：有用但为何独立成产品？](https://techcrunch.com/2026/05/30/i-put-googles-24-7-ai-assistant-gemini-spark-to-work-and-its-actually-pretty-useful/) —— Gemini Spark 可自动处理收件箱摘要和本地活动规划，但作为独立产品定位模糊。
  _TechCrunch_

### 股票

- [MiniMax 发布 M3 旗舰模型：12 小时复现 ICLR 获奖论文](https://wallstreetcn.com/articles/3773560) —— MiniMax 在科创板 IPO 辅导后推出 M3，首次实现编程+1M 上下文+原生多模态，Agent 能力显著提升。
  _华尔街见闻_
- [美团 Q1 营收 910 亿超预期，但竞争加剧导致核心业务转亏](https://wallstreetcn.com/articles/3773571) —— 美团营收增长 5.6% 超预期，但营销开支激增 51%，核心本地商业由盈转亏，AI 投入加码。
  _华尔街见闻_

### 金融

- [美国通胀升至 3.8%，伊朗战争推高能源成本](https://www.bbc.com/news/articles/c202pgxx89lo) —— 伊朗战争导致能源价格飙升，美国通胀反弹至 3.8%，美联储降息预期进一步推迟。
  _BBC_
- [微软内部数据：使用 AI 比雇佣人类更贵](https://finance.yahoo.com/sectors/technology/articles/microsoft-data-suggests-using-ai-225900743.html) —— 微软研究发现，当前 AI 替代人类在某些任务上成本更高，AI 降本增效的叙事需谨慎看待。
  _Yahoo Finance_

### AI

- [B 站热门：锐评 32 个 AI 编程工具从夯到拉](http://www.bilibili.com/video/av116578532200786) —— 鱼皮一口气实测 32 个 AI 编程工具，从 Cursor 到 CodeBuddy，帮你快速找到适合自己的工具。
  _程序员鱼皮_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
