# Curio · AI 算力 / 半导体 · 2026-10-20

> 今日 2 条头条 + 4 条备选

_今天最值得盯的信号有两个：一是 AI 资本叙事开始松动——CoreWeave 债券跌入困境区间、Anthropic 估值被传缩水 5000 亿美元、Firmus 的 300 亿 IPO 48 小时崩盘，算力泡沫的融资端先出裂缝；二是大厂在 Agent 安全上集体转向防守，微软直接把 AI Agent 定性为「内部威胁」。对做 Agent 的你，前者决定明年算力成本，后者决定你产品的信任边界。_

---

## 🌟 今日精选

### 3. Claude Code 顺手抓出一个潜伏在 Mac 上的挖矿木马：xmrig 占用 1175% CPU、温度飙到 112 度

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

一个开发者用 Claude Code 帮忙写温度监控 App，结果 Claude Code 反过来警告他：系统里有个隐藏的 xmrig 挖矿进程在跑，占用约 1175% CPU（约 12 核），把机器温度推到 112 度。这是个罕见的「Agent 作为系统诊断工具」的真实案例，也顺带暴露了 Claude Code 的 system prompt 里对异常进程的敏感度。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 涉事进程为 xmrig，典型门罗币挖矿程序 | Claude Code 是靠 system prompt 里的进程检查指令触发，还是模型自发推理，官方未说明 |
| CPU 占用约 1175%，折合约 12 个核心 | 这类「Agent 当运维」的用法能否稳定复现，取决于 Agent 是否有 shell 执行权限 |
| 机器温度被推到 112 摄氏度 | xmrig 的植入途径（供应链 / 破解软件 / 恶意 npm 包）未披露 |
| 触发场景是开发者让 Claude Code 协助开发温度监控应用 | 把这件事当成 Claude Code 的营销案例要谨慎，它也可能只是碰巧 |
| Claude Code 主动发出警告，而非用户先发现 |  |

**📖 主编点评**

这条对你的价值不在挖矿，在于示范了一个可复用的 Agent 用法：给 Agent 系统级只读权限，让它定期巡检进程、端口、启动项。你完全可以在 content-curator 里加一个「环境自检」子 Agent，用 cron 跑，输出异常报告。这个功能写进 README 比任何「10 个 MCP 推荐」都更能体现你懂 Agent 的边界在哪。

📺 [打开原文](https://www.tomshardware.com/tech-industry/cryptomining/claude-code-ai-agent-caught-a-crypto-miner-hiding-on-a-developers-overheating-mac-xmrig-task-was-hogging-about-1175-percent-cpu-roughly-12-cores-pushing-temps-to-112-degrees)

---

### 5. Opus 5.5 Agent 自主发现两种室温磁性半导体候选材料

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Hacker News / Vals.ai_

Vals.ai 发文称，用 Opus 5.5 驱动的 Agent 在材料筛选任务中自主发现了两组室温磁性半导体候选。这是「Agent 做科研发现」少见的、带具体产出物的案例，而不是又一篇「AI 将改变科学」的综述。HN 上 495 分，讨论集中在可复现性和验证方法。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 发现方为 Vals.ai，使用 Opus 5.5 驱动的 Agent 流程 | 候选材料是否经实验验证，原文未明确，大概率仍是计算层面 |
| 产出是两种室温磁性半导体候选材料 | Agent 在其中承担的是搜索、筛选还是提出假设，分工不清 |
| HN 讨论热度 495 分，属当日高位 | 「室温磁性半导体」本身是材料学的硬骨头，两个候选的可信度需同行评议 |
| 任务类型是材料筛选 / 候选生成，而非实验验证 | 这类成果的可复现性依赖 prompt 和工具链是否公开 |

**📖 主编点评**

别被「Agent 发现新材料」的标题带走。对你有用的是它的方法论骨架：把领域知识拆成可执行的筛选步骤，让 Agent 逐步跑，而不是一次性丢给模型。你做 content-curator 的选稿逻辑其实同构——先粗筛再精排。把这条的流程拆解读一遍，对照你自己的 pipeline，能找出至少一个可以拆成子 Agent 的环节。

📺 [打开原文](https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors)

---

## 📋 备选阅读

- [Arm 称其 AGI CPU 在 agentic AI 测试中每机架性能近 AMD EPYC 9755 的两倍](https://www.tomshardware.com/pc-components/cpus/arm-claims-agi-cpu-delivers-double-the-performance-per-rack-of-amd-epyc-9755-in-independent-analysis-new-cpu-evaluation-methodology-developed-by-arm-evaluates-agentic-ai-performance-across-seven-workloads) —— 首次出现「agentic AI 专用 CPU benchmark」方法论，由 Arm 联合 Fujitsu、Meta、OpenAI 制定；数据是厂商自测，但方法论本身值得关注。
  _Tom's Hardware_
- [OpenAI 年化收入比此前信号低 200 亿美元](https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html) —— 434 分的 HN 热帖，直接冲击算力需求叙事；但发布于 10 月 8 日，已过一周，作为背景而非头条。
  _CNBC / HN_
- [ASML 称 2026 年在欧洲「什么都没卖出去」](https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand) —— 半导体设备的地缘集中度信号，欧洲本土需求归零；对理解全球产能布局有用，但离你的日常较远。
  _Tom's Hardware / HN_
- [Nvidia 洽谈收购美国「开放」模型公司 Reflection AI](https://www.ft.com/content/052610c5-22b4-4dd4-932e-b7f9f0628b6a) —— Nvidia 从卖铲子转向买模型公司，若成真会改变开源模型格局；目前仅为洽谈，信息量有限。
  _FT / HN_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
