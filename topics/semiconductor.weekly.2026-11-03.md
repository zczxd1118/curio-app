# Curio · AI 算力 / 半导体 · 2026-11-03

> 今日 2 条头条 + 5 条备选

_今天最值得看的两条线：一是 AI 资本结构开始承压——Marvell 1150 亿美元吞下 Lumentum、Oracle 发 200 亿股债、Intel 领跌 3.5 万亿芯片股回调，钱在往光互联和算力上压重注，同时市场开始怀疑回报；二是 Anthropic 一边限制 Claude Code 复刻游戏 IP，一边自曝接近 RSI，模型厂商的自我约束和自加速同时发生。_

---

## 🌟 今日精选

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

## 📋 备选阅读

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

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
