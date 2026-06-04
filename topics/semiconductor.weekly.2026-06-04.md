# Curio · AI 算力 / 半导体 · 2026-06-04

> 今日 2 条头条 + 4 条备选

_今日 Computex 2026 进入高潮：Nvidia 发布 RTX Spark AI PC 芯片，微软推出 Agent-first 的 Project Solara 平台，AI 硬件战局从云端烧到终端。同时博通财报指引不及预期引发盘后暴跌 14%，ASIC 阵营出现分化信号。DRAM 价格飙至 15 年新高，32GB DDR5 最低 $375，AI 内存短缺正在冲击全行业。_

---

## 🌟 今日精选

### 1. Nvidia 发布 RTX Spark 个人 AI 超级计算机芯片，PC 端 AI 算力竞赛正式开打

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _shenli3514_

Nvidia 在 Computex 2026 上正式发布 RTX Spark 系列芯片，面向个人电脑和工作站，内置 Grace CPU 和 Blackwell GPU 架构，目标是在本地运行大模型和 AI Agent。微软同步推出搭载 RTX Spark 的 Surface Laptop Ultra，AMD 高管则回应称 Strix Halo 笔记本才是正确选择。一场围绕「AI PC 芯片」的战争已经打响。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Nvidia 发布 RTX Spark N1/N1X 芯片，集成 Grace CPU 和 Blackwell GPU | RTX Spark 实际推理性能 vs Strix Halo 尚无第三方基准测试 |
| 微软推出 Surface Laptop Ultra，搭载 RTX Spark，定位 MacBook Pro 竞品 | PC 端 AI Agent 应用场景是否足够支撑大规模换机需求存疑 |
| AMD 高管公开回应，认为 Strix Halo 笔记本性能优于 RTX Spark 方案 | Nvidia 在消费级市场的品牌认知和渠道能力有待验证 |
| Nvidia 已规划后续 N2X、N3X 芯片，目标直指 Star Trek 级 AI 计算机 | Intel 和 AMD 的 AI PC 路线图（Lunar Lake、Strix Halo）将如何反制 |
|  | RTX Spark 定价和功耗细节尚未公布，影响实际竞争力 |

**📖 主编点评**

你正在做 content-curator Agent 项目，RTX Spark 意味着未来你可以用一台笔记本本地运行 Claude 或 Gemini 级别的模型，而不依赖云 API。建议关注 RTX Spark 的开发者工具链（CUDA、TensorRT）是否开放给个人开发者，这决定了你的 Agent 项目能否真正「离线可用」。

📺 [打开原文](https://www.nvidia.com/en-us/products/rtx-spark/)

---

### 4. DRAM 价格飙至 15 年新高：32GB DDR5 最低 $375，AI 内存短缺冲击全行业

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Stephen Warwick_

DRAM 合约价本季度预计再涨 58%-63%，32GB DDR5 套条最低价已涨至 $374.97，创 15 年新高。AI 对 HBM 和 DDR5 的抢购正在挤压消费级市场，GoPro 甚至警告「持续经营能力存在重大疑问」。AMD 的 Gorgon Halo 芯片虽支持 192GB 本地 AI 内存，但高昂的 DRAM 成本正在成为本地 Agentic Computing 落地的最大障碍。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 32GB DDR5 最低价 $374.97，较年初翻倍 | DRAM 涨价周期何时见顶？三星和 SK 海力士增产节奏是关键 |
| DRAM 合约价本季度预计再涨 58%-63% | 消费级 PC 市场是否会因内存成本过高而萎缩 |
| GoPro 在监管文件中警告持续经营能力存疑，归因于内存成本飙升 | 本地 AI 推理的经济账是否还成立？32GB $375 意味着 64GB 配置成本超 $750 |
| AMD Gorgon Halo 支持 192GB 内存，但 DRAM 成本制约普及 | HBM5 的推出能否缓解 DDR5 的供给压力？ |
|  | 中国 DRAM 厂商（长鑫存储）的产能爬坡能否改变格局 |

**📖 主编点评**

你正在做本地 Agent 项目，DRAM 涨价直接影响你的硬件成本。如果计划用本地模型（如 7B/13B 参数），至少需要 32GB 内存，当前 $375 的成本可能让 Side Project 的硬件门槛变高。建议考虑量化模型（GGUF/GPTQ）或云 API 混合方案，在成本可控的前提下验证产品逻辑。

📺 [打开原文](https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-now-costs-usd375-minimum-ai-shortage-continues-to-squeeze-pc-building)

---

## 📋 备选阅读

- [三星展示首款 HBM5 原型，采用 Heat Path Block 散热](https://www.tomshardware.com/tech-industry/semiconductors/samsung-shows-first-hbm5-mockup-at-computex-with-heat-path-block-cooling) —— HBM5 散热方案竞争白热化，三星与 SK 海力士的热管理技术路线分化值得关注。
  _Luke James_
- [Astera Labs 展示 320 通道 PCIe 6.0 交换机，支持 80 个加速器扩展](https://www.tomshardware.com/desktops/servers/astera-labs-showcases-320-lane-pcie-6-0-switch-for-vendor-agnostic-scaling-in-data-centers-up-to-80-accelerators-can-be-scaled-up-using-pcie-alone) —— PCIe 6.0 交换机为 AI 数据中心提供供应商无关的扩展方案，降低对 NVLink 的依赖。
  _Anton Shilov_
- [微软发布 Majorana 2 量子芯片，目标 2029 年实用化](https://www.tomshardware.com/tech-industry/quantum-computing/microsoft-announces-majorana-2-quantum-computing-chip-claims-a-practical-machine-will-come-in-2029) —— 微软改用铅基材料推进拓扑量子计算，路线图加速，但 2029 年目标仍极具挑战。
  _Andrew E. Freedman_
- [Intel 承认 Arrow Lake 失误，Arrow Lake Refresh 低价策略意在重建声誉](https://www.tomshardware.com/pc-components/cpus/intel-addresses-arrow-lake-blunder-we-needed-to-build-back-our-reputation-says-arrow-lake-refreshs-low-price-a-key-first-step-laying-the-groundwork-for-nova-lake) —— Intel 公开反思 Arrow Lake 性能问题，Refresh 降价为 Nova Lake 铺路，态度诚恳但执行力待验证。
  _Jake Roach_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
