# Curio · AI 算力 / 半导体 · 2026-11-03

> 今日 2 条头条 + 6 条备选

_今天最重要的信号是 AI 资本链条开始出现裂缝：Marvell 以 1150 亿美元吞下 Lumentum 抢光互联，同时 Intel 领跌、芯片板块蒸发 3.5 万亿美元、Oracle 发 200 亿新股债补 AI 基建，市场对 AI 成本的耐心在下降。另一条线是 Anthropic 同时收紧 Claude Code 的游戏克隆限制并公开警告接近 RSI——模型厂商开始主动给能力划边界。_

---

## 🌟 今日精选

### 1. Marvell 以 1150 亿美元收购光子公司 Lumentum，赌 AI 集群的瓶颈从算力转向光互联

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Majeed Ahmad_

这是科技史上最大规模并购之一，双方共同战略投资方都是 Nvidia。交易逻辑不在芯片本身，而在光收发器：当集群规模上到十万卡量级，网络处理器和激光器的协同设计比单卡 FLOPS 更决定训练效率。Marvell 想借此从存储/网络芯片供应商变成 AI 互联的定义者。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 交易金额 1150 亿美元，为科技史最大并购之一 | 监管审批路径未明，1150 亿量级大概率触发多国反垄断审查 |
| 标的是光子芯片厂商 Lumentum，主攻光收发器激光器 | 光互联是否真能成为下一个卡脖子环节，取决于 CPO 与可插拔方案的路线之争 |
| 双方共同战略投资方均为 Nvidia | Nvidia 作为共同股东，是否会在供应分配上偏向自家生态 |
| 目标是共同设计网络处理器与激光器，做 AI 互联品类领导者 | 整合风险：Marvell 此前无光子制造经验，Lumentum 的晶圆产能扩张需要资本开支 |
| 由 EE Times 于 11 月 3 日首发报道 |  |

**📖 主编点评**

你做 AI 工程时如果只盯 GPU 显存和带宽，会漏掉真正的瓶颈。下次读集群架构文章，留意 prefill/decode 分离后光互联带宽怎么成为新约束——这决定了未来两年推理成本曲线的斜率，也是你写技术判断时能拉开差距的视角。

📺 [打开原文](https://www.eetimes.com/marvell-snaps-photonics-chipmaker-lumentum-to-bolster-ai-connectivity/)

---

### 5. 工程师把 32 位 RISC-V CPU 直接编译进 Qwen 3.5 4B 的权重里，还能跑 DOOM

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Mark Tyson_

Qwenputer 这个实验把一颗完整的 32 位 RISC-V CPU 编译后塞进 Qwen 3.5 4B 的权重，模型能执行处理器算术运算、跑代码，最后当然跑了 DOOM。这不是实用产品，但它把'权重即程序'这个抽象推到了极端，是理解 LLM 计算本质的好样本。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 基于 Qwen 3.5 4B 开源模型 | 这是否只是过拟合的演示，还是权重真能承载通用计算，需要复现 |
| 32 位 RISC-V CPU 被编译并插入模型权重 | 性能与正确率数据未公开，'能跑'和'跑得对'是两回事 |
| 模型可执行处理器算术运算与代码 | 对推理优化是否有任何可迁移的方法论，目前看不到 |
| 成功运行 DOOM | 是否会催生'权重内嵌工具'这类新范式，为时过早 |
| 由独立 AI 工程师完成，非官方项目 |  |

**📖 主编点评**

你写 content-curator 时如果要做'模型能力边界'的选题，这是绝佳的引子——它逼你回答'LLM 到底在计算什么'。建议你亲自读一遍仓库，看它怎么把指令集映射到权重，这种底层理解比追新工具更能形成你的技术判断力。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-engineer-successfully-compiles-a-32-bit-risc-v-cpu-in-qwen-3-5-4b-llm-inserted-directly-into-its-weights-built-in-cpu-can-run-processor-arithmetic-operations-code-and-of-course-doom)

---

## 📋 备选阅读

- [OpenAI 考虑把数据中心改名为'AI 计算园区'，应对日益强烈的社区反弹](https://www.tomshardware.com/tech-industry/data-centers/openai-considers-rebranding-data-centers-to-ai-compute-campuses-as-data-center-backlash-intensifies-company-reportedly-sees-2028-presidential-election-becoming-an-ai-issue) —— 改名是公关动作，但透露 OpenAI 已把 AI 基建当成政治议题来运营，2028 大选是它的时间锚。
  _Newton Gitonga_
- [超 90% 的 1 万条公众评论反对数据中心，水是头号担忧](https://www.tomshardware.com/tech-industry/data-centers/america-hates-data-centers-new-database-reveals-more-than-90-percent-of-10-000-public-comments-are-negative-only-21-percent-mention-ai-73-percent-of-meetings-had-no-data-center-supporters-water-is-the-number-one-concern) —— 量化了 AI 基建的社会阻力，只有 21% 的反对意见提到 AI 本身——多数是水和电，这决定选址难度。
  _Oliver Haslam_
- [开源 USB 工具解锁 Nvidia 在 Windows 上的半速 AI 限制，FP16 性能提升至多 65%](https://www.tomshardware.com/pc-components/gpus/open-source-usb-tool-unlocks-nvidias-half-speed-gpu-ai-limiter-on-windows-lifts-gpus-fp16-math-performance-up-to-65-percent-uefi-unlocker-covers-rtx-20-30-and-40-series-desktops-and-laptops) —— 覆盖 RTX 20/30/40 系桌面与笔记本，对本地跑模型的你有实操价值，但注意保修与稳定性风险。
  _Shane Downing_
- [Anthropic 确认 Claude Code 新限制，用户报告 Opus 5.5 也在拦截逆向工程任务](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-confirms-new-claude-code-limits-to-prevent-game-cloning-users-report-opus-5-5-is-also-actively-blocking-reverse-engineering-tasks) —— 头条 3 的原始信源，细节更全：限制写在系统提示词层，官方措辞是'正在寻找平衡'。
  _Bruno Ferreira_
- [Nvidia Brev 平台安全事件可能泄露客户 VM 的 SSH 密钥，未授权活动持续 16 天](https://www.tomshardware.com/tech-industry/cyber-security/nvidia-brev-security-breach-may-have-exposed-ssh-keys-used-to-access-customer-vms-investigation-finds-unauthorized-activity-spanning-16-days-but-no-evidence-of-misuse) —— 如果你在 Brev 上跑过开发环境，该轮换密钥了；16 天窗口说明检测机制有延迟。
  _Newton Gitonga_
- [新型 AI 驱动 Windows 恶意软件把窃取数据喂给 Claude，按变现价值给受害者资产排序](https://www.tomshardware.com/tech-industry/cyber-security/new-ai-driven-windows-malware-feeds-stolen-data-to-claude-to-rank-victims-assets-by-value-then-deletes-itself-payload-builds-custom-target-assessment-can-switch-models-if-one-refuses-or-skip-the-ai-step-entirely) —— Cisco Talos 披露的 VOLTA 窃密器，模型可切换、可跳过 AI 步骤——攻击侧已经在做工程化降级设计。
  _Shane Downing_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
