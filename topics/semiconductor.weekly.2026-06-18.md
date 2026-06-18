# Curio · AI 算力 / 半导体 · 2026-06-18

> 今日 2 条头条 + 5 条备选

_今日最重磅的信号是 Anthropic 的 Fable 5 模型被美国政府突然切断出口，引发全球盟友对 AI 供应链安全的恐慌——这比任何技术发布都更影响你的 Agent 项目部署策略。同时 AMD 收购 MEXT 打破内存墙、Intel 18A-P 进入风险量产，半导体制造端迎来关键转折。金融端全球央行同步加息，美联储新主席沃什鹰派首秀，宏观环境正在快速收紧。_

---

## 🌟 今日精选

### 2. AMD 收购 MEXT 打破 AI 内存墙，成本有望大幅下降

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _EE Times_

AMD 宣布收购内存计算初创公司 MEXT，旨在解决 AI 推理和训练中的“内存墙”瓶颈。MEXT 的技术可减少数据在 GPU 和内存之间的搬运，据称能显著降低 AI 推理的总体拥有成本（TCO）。这笔交易金额未披露，但信号明确：AMD 正在从芯片设计转向系统级优化。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| AMD 已签署收购 MEXT 的最终协议 | MEXT 技术是否能在 AMD 的 CDNA 架构中快速集成 |
| MEXT 的技术专注于近内存计算和内存内处理 | 与 NVIDIA 的 NVLink/C2C 相比，实际性能提升幅度 |
| 目标是将 AI 推理的每 token 成本降低 40% 以上 | 收购价格是否合理（MEXT 此前融资约 1.2 亿美元） |
| 收购后 MEXT 团队将并入 AMD 数据中心事业部 | 对 AMD 在 AI 推理市场份额的拉动作用 |

**📖 主编点评**

如果你在构建 AI Agent 或 RAG 系统，内存墙是实际瓶颈——长上下文推理成本极高。AMD 的这一步可能在未来 1-2 年内降低推理硬件成本，但短期内建议关注软件层面的优化（如 KV cache 量化、投机解码）。你的 content-curator 项目可以提前预留对 AMD ROCm 的支持。

📺 [打开原文](https://www.eetimes.com/amd-snaps-mext-to-break-the-memory-wall/)

---

### 3. Intel 18A-P 进入风险生产，性能提升 9% 且热阻降低 40%

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

Intel 宣布其增强型 18A-P 工艺已进入风险生产阶段，这是 18A 节点的性能优化版本，承诺在同等功耗下性能提升 9%，同时热阻降低 40%。该节点面向高性能计算和 AI 芯片，是 Intel 代工业务的关键里程碑。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 18A-P 是 18A 的 drop-in 升级，客户无需重新设计 | 18A-P 能否在 2027 年如期进入量产 |
| 性能提升 9% 来自工艺优化而非架构变化 | 良率是否达到客户接受水平（尤其是外部代工客户） |
| 热阻降低 40% 意味着更好的散热表现 | 与台积电 N2P 相比的实际竞争力 |
| 风险生产已在俄亥俄州工厂启动 | 苹果与 Intel 合作（见今日其他新闻）是否基于此节点 |

**📖 主编点评**

Intel 代工业务的进展直接影响 AI 芯片的供应格局。如果你关注硬件成本，Intel 18A-P 可能为 AI 推理芯片提供新的选择。但风险生产到量产仍有距离，短期内台积电仍占主导。建议在项目规划中保持硬件无关性。

📺 [打开原文](https://www.tomshardware.com/tech-industry/semiconductors/intels-performance-enhanced-18a-p-process-enters-risk-production-enhanced-node-promises-9-percent-performance-improvement-at-iso-power)

---

## 📋 备选阅读

- [SMI 称 NVIDIA 驱动消费级 PCIe 6.0 路线图，RTX Spark 平台推动存储带宽需求](https://www.tomshardware.com/pc-components/ssds/silicon-motions-client-pcie-6-x-roadmap-is-driven-by-nvidia-not-by-amd-and-intel-rtx-spark-agentic-ai-platform-could-fuel-a-hunger-for-storage-bandwidth) —— NVIDIA 的客户端 AI 平台 RTX Spark 对存储带宽的需求正在推动 PCIe 6.0 的消费级落地。
  _Tom's Hardware_
- [AMD 下一代 Threadripper “Mustang Peak” 曝光：支持 DDR5、PCIe 6.0](https://www.tomshardware.com/pc-components/cpus/first-official-details-of-amds-next-gen-mustang-peak-threadripper-cpus-come-into-view-chips-feature-ddr5-pcie-6-0-and-a-new-socket) —— Zen 6 架构的 Threadripper 首次曝光，工作站平台将迎来大升级。
  _Tom's Hardware_
- [Qualcomm 考虑以 80-100 亿美元收购 Jim Keller 的 Tenstorrent](https://www.tomshardware.com/tech-industry/artificial-intelligence/qualcomm-mulls-taking-over-jim-kellers-tenstorrent-report-claims-deal-for-ai-chipmaker-would-value-the-company-at-between-usd8-billion-and-usd10-billion) —— RISC-V AI 芯片公司 Tenstorrent 可能被 Qualcomm 收购，估值 80-100 亿美元。
  _Tom's Hardware_
- [中国内存品牌抛弃三星、美光，改用国产 CXMT 和 YMTC 芯片](https://www.tomshardware.com/pc-components/ram/chinese-memory-vendors-snub-industry-giants-in-favor-of-homegrown-ram-chips-samsung-micron-and-sk-hynix-face-a-chinese-supply-chain-revolt) —— 国产 DDR5 内存开始替代进口，Corsair、HP、Dell 已采用中国产芯片。
  _Tom's Hardware_
- [NVIDIA 展示自学习安装 GPU 的机器人：AI 编码 Agent 自主指导机器人训练](https://arstechnica.com/ai/2026/06/ai-coding-agents-can-autonomously-direct-robot-training/) —— NVIDIA 用 AI 编码 Agent 团队教会机器人高精度操作，如安装 GPU 和剪扎带。
  _Ars Technica_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
