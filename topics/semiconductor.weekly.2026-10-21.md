# Curio · AI 算力 / 半导体 · 2026-10-21

> 今日 2 条头条 + 4 条备选

_今天最值得盯的是两条反向信号：一边是 SpaceX 靠 AI 业务把季度营收推到 146 亿美元、净利 44 亿，另一边是 Anthropic 估值被传缩水 5000 亿、云算力拿不到、IPO 前夜承压。AI 泡沫的分歧已经从口水战变成财报和估值数字，同时 Google 和 Amazon 都在推工具把 PyTorch 应用搬离 Nvidia GPU，算力层的护城河开始被撬。_

---

## 🌟 今日精选

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

## 📋 备选阅读

- [China's tech giants drop $35B on Nvidia RTX Pro 5500 orders](https://www.tomshardware.com/pc-components/gpus/chinas-tech-giants-drop-usd35-billion-on-export-compliant-nvidia-rtx-pro-5500-workstation-gpu-orders-to-power-ai-ambitions-according-to-reports-bytedance-alibaba-and-tencent-order-3-million-cards-despite-warnings-that-only-10-percent-of-orders-are-fulfillable) —— 字节、阿里、腾讯下单 35 亿美元合规版 GPU，但据报仅 10% 订单可交付，供需缺口惊人。
  _Tom's Hardware_
- [US restarts three shut-down nuclear reactors to feed AI data centers](https://www.tomshardware.com/tech-industry/big-tech/us-takes-unprecedented-step-of-recommissioning-nuclear-plants-due-to-ai-power-demand-2-25-gw-currently-on-tap-from-refurbished-reactors) —— 美国重启三座核反应堆供电 AI 数据中心，现有 2.25GW 容量，电力正成为算力瓶颈。
  _Tom's Hardware_
- [Chris Lattner: AI Code Generation Doesn't Solve Software Engineering](https://www.eetimes.com/chris-lattner-ai-code-generation-doesnt-solve-software-engineering/) —— LLVM 之父谈 AI 生成代码反而让软件生态更难维护，观点稀缺，适合你这种重度 vibe coding 玩家反刍。
  _EE Times_
- [Qualcomm Wins Key Claims Against Arm, but Damages Total Just $2](https://www.eetimes.com/qualcomm-wins-key-claims-against-arm-but-damages-total-just-2/) —— 高通在四年 IP 诉讼中赢下关键主张，但赔偿仅 2 美元，象征意义大于财务意义。
  _EE Times_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
