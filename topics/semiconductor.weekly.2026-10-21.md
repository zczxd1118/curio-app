# Curio · AI 算力 / 半导体 · 2026-10-21

> 今日 2 条头条 + 4 条备选

_今天最值得看的两个信号：一是 AI 资本叙事开始松动——Anthropic 估值据报缩水 5000 亿美元、云算力合作变紧张、数据中心 IPO 接连崩盘，11 月 IPO 前的窗口很窄；二是工程侧的真进展，DeepMind 用四个 Gemini 4 Agent 27 小时通关 Minecraft、自己写了 2783 个程序，Agent 从演示走向可验证的长程任务。前者提醒你别把行业热度当个人判断，后者才是你该动手复现的东西。_

---

## 🌟 今日精选

### 2. DeepMind 称四个 Gemini 4 Agent 用 27 小时通关 Minecraft，自己写了 2783 个程序、死了 605 次、烧掉约 520 美元 token

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

Google DeepMind 研究者称，四个 Gemini 4 Argon Agent 在无人工干预下 27 小时通关 Minecraft，过程中自行编写了 2783 个程序来扩展能力。代价同样具体：简单难度下死了 605 次，token 成本约 520 美元。这是少见的把「长程自主任务」的成功率、失败次数、成本三件事同时摊开的公开案例。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 四个 Gemini 4 Argon Agent 协作，27 小时无人工干预通关 Minecraft | 「通关」的判定标准（是否含终局 Boss、是否用种子）未在摘要中说明，复现前不宜直接对比 |
| Agent 自行编写 2783 个程序作为工具扩展 | 2783 个程序里有多少被复用、多少是一次性脚本，决定了这套方法能否迁移到真实工程 |
| 简单难度下累计死亡 605 次 | 520 美元成本对研究可接受，对产品化仍偏高，取决于任务价值密度 |
| 估算 token 消耗约 520 美元 | 多 Agent 分工的具体协议（谁写代码、谁执行、谁验证）尚不明确 |
| 同期另有 Gemini 4 Argon 在 StarCraft 上的第三方 benchmark 出现 |  |

**📖 主编点评**

这条对你的 content-curator 项目是直接可抄的范式：让子 Agent 写一次性脚本去扩展能力，而不是把所有逻辑塞进一个 prompt。建议你复现最小版本——两个 Agent、一个写工具一个跑工具、记录失败次数与 token 成本，这套「成功率 + 成本」的记录方式本身就是简历上很硬的一段。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/google-deepmind-claims-four-gemini-4-agents-beat-minecraft-in-27-hours-by-writing-2-783-programs-of-their-own-the-ai-team-died-605-times-on-easy-difficulty-and-ran-up-an-estimated-usd520-in-tokens)

---

### 3. Chris Lattner：AI 代码生成解决不了软件工程，反而让维护生态更难

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _EE Times_

LLVM 与 Swift 之父 Chris Lattner 在 EE Times 访谈里给 AI 编程泼了盆冷水：生成低层代码不是瓶颈，真正的难题是构建和维护软件生态，而代码生成正在让这件事变难。在你天天用 Claude Code 的当下，这是少数来自编译器一线、而非产品营销视角的判断。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Chris Lattner 是 LLVM、Clang、Swift 的创造者，现从事 AI 芯片与编译器相关工作 | Lattner 的具体论据链条需读全文，摘要只给了结论 |
| 其核心论点：代码生成 ≠ 软件工程，生态维护才是真瓶颈 | 「让维护更难」是否可量化（如 PR 体积、review 时长）尚无数据 |
| 访谈发表于 EE Times，属工程侧深度对话而非产品发布 | 该观点与 vibe coding 主流叙事相左，短期不会被产品方引用 |
| 同期社区已有大量关于 AI 生成代码增加 review 负担的讨论 |  |

**📖 主编点评**

你正在用 vibe coding 做真实项目，这条正好是反向校准：写出来的代码你自己能不能在两周后读懂、改得动。建议你在 content-curator 里加一条硬规矩——每个 AI 生成的模块必须配一段你自己写的注释说明「为什么这样设计」，这既是工程习惯，也是面试时能讲的东西。

📺 [打开原文](https://www.eetimes.com/chris-lattner-ai-code-generation-doesnt-solve-software-engineering/)

---

## 📋 备选阅读

- [中国三大厂下单 350 亿美元英伟达 RTX Pro 5500，传仅 10% 订单可交付](https://www.tomshardware.com/pc-components/gpus/chinas-tech-giants-drop-usd35-billion-on-export-compliant-nvidia-rtx-pro-5500-workstation-gpu-orders-to-power-ai-ambitions-according-to-reports-bytedance-alibaba-and-tencent-order-3-million-cards-despite-warnings-that-only-10-percent-of-orders-are-fulfillable) —— 字节、阿里、腾讯合计下单约 300 万张合规版 GPU，需求远超产能，交付率成关键变量。
  _Tom's Hardware_
- [美国重启三座核反应堆为 AI 数据中心供电，现有 2.25 GW 装机](https://www.tomshardware.com/tech-industry/big-tech/us-takes-unprecedented-step-of-recommissioning-nuclear-plants-due-to-ai-power-demand-2-25-gw-currently-on-tap-from-refurbished-reactors) —— AI 算力的瓶颈从芯片转向电力，政府出资重启退役机组，是基建层最硬的一条信号。
  _Tom's Hardware_
- [Modal 采用 Nvidia Vera CPU，内部测试吞吐为 Intel/AMD 的两倍](https://www.tomshardware.com/pc-components/cpus/nvidia-vera-cpu-deployed-at-ai-startup-modal-alongside-existing-x86-fleet-internal-testing-showed-2x-throughput-compared-to-amd-and-intel) —— 首个公开的 Vera CPU 生产部署案例，专打 Agent 类负载，值得关注 Arm 在推理侧的位置。
  _Tom's Hardware_
- [高通在与 Arm 的诉讼中赢下关键主张，但赔偿总额仅 2 美元](https://www.eetimes.com/qualcomm-wins-key-claims-against-arm-but-damages-total-just-2/) —— 四年 IP 纠纷的最新一章，法律上高通保住自研处理器，财务上几乎无影响，象征意义大于实质。
  _EE Times_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
