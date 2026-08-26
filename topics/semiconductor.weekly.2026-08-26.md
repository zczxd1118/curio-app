# Curio · AI 算力 / 半导体 · 2026-08-26

> 今日 2 条头条 + 4 条备选

_今日最重磅的信号是 OpenAI 自研 ASIC 芯片 Jalapeño 在 Hot Chips 2026 上首次公开基准测试，宣称能效和吞吐量超越 Nvidia Blackwell，这标志着 AI 算力竞争进入新阶段。同时，苹果发布 M6 和 M5 Ultra 芯片，Mac mini 起售价涨至 $899，AI 终端设备算力竞赛加剧。金融领域，高盛预计日本央行 9 月加息，全球粮食危机警报拉响。半导体方面，SK 海力士和三星在 Hot Chips 上展示了 HBM 和 LPDDR5X-PIM 技术进展，存储成本压力持续。_

---

## 🌟 今日精选

### 1. OpenAI 自研芯片 Jalapeño 首秀：能效超 GB300 1.9 倍，AI 算力格局生变

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

OpenAI 在 Hot Chips 2026 上首次公布自研推理芯片 Jalapeño 的基准测试结果，宣称其 700W 功耗下每千瓦吞吐量比 Nvidia GB300 高 1.9 倍，延迟低 3.6 倍。这颗与 Broadcom 合作的 ASIC 从设计到流片仅用 9 个月，直接挑战 CUDA 生态。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Jalapeño 芯片功耗 700W，GB300 为 1400W | 基准测试由 OpenAI 自行发布，缺乏第三方独立验证 |
| 每千瓦吞吐量比 GB300 高 1.9 倍，延迟低 3.6 倍 | 实际部署性能和成本效益尚待大规模验证 |
| 与 Broadcom 合作开发，9 个月完成设计到流片 | 对 Nvidia 市场地位的长期影响取决于量产能力和生态适配 |
| 在 SemiAnalysis InferenceX 基准上每用户 token 数和每千瓦吞吐量均超现有产品 |  |

**📖 主编点评**

这对你意味着 AI 算力不再被 Nvidia 垄断，未来模型推理成本可能大幅下降。作为 AI 产品开发者，你应该关注 OpenAI 的芯片进展，因为如果 Jalapeño 量产，你使用的 API 价格可能降低，或者你可以考虑在自建推理时采用更高效的硬件方案。同时，这也提醒你关注 ASIC 在特定场景（如推理）的潜力，或许在个人项目中可以探索类似优化。

📺 [打开原文](https://www.tomshardware.com/tech-industry/semiconductors/openai-says-its-jalapeno-chip-beats-nvidias-gb300-in-first-published-benchmarks)

---

### 4. 三星 LPDDR5X-PIM 亮相 Hot Chips：AI 推理速度提升 3 倍，带宽 8 倍

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

三星在 Hot Chips 2026 上展示了业界首款 LPDDR5X-PIM（内存内处理）芯片，通过在内存中集成逻辑单元，AI 推理性能比标准 LPDDR5X 快 3.01 倍，带宽提升 8 倍。这一技术有望缓解 AI 计算中的内存墙问题。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| LPDDR5X-PIM 为业界首款，在内存中集成逻辑单元 | PIM 技术的量产时间和成本尚不明确 |
| AI 推理速度比标准 LPDDR5X 快 3.01 倍 | 对现有 AI 芯片架构的替代性有待验证 |
| 带宽提升 8 倍 | 能否在移动设备等低功耗场景落地 |
| 在 Hot Chips 2026 上公布细节 |  |

**📖 主编点评**

内存墙是 AI 计算的核心瓶颈，PIM 技术可能改变未来 AI 硬件设计。作为开发者，你可以关注这一技术对边缘 AI 设备的影响，未来可能在手机或嵌入式设备上运行更高效的模型。同时，这也意味着内存厂商在 AI 产业链中的地位上升，投资或选型时值得留意。

📺 [打开原文](https://www.tomshardware.com/pc-components/dram/hot-chips-2026-samsung-makes-lpddr5x-smart-with-logic-unit-in-memory-lpddr5x-pim-is-3-01x-faster-than-lpddr5x-in-ai-inference-with-8x-the-bandwidth)

---

## 📋 备选阅读

- [Nvidia 大幅减少对 OpenAI 基础设施融资的担保](https://www.reuters.com/business/nvidia-scales-back-250-billion-openai-data-center-guarantee-wsj-reports-2026-08-14/) —— Nvidia 缩减对 OpenAI 的融资担保，反映 AI 基础设施投资风险上升，值得关注。
  _Reuters_
- [Hot Chips 2026: Intel 详解 Crescent Island AI 加速器](https://www.tomshardware.com/pc-components/gpus/hot-chips-2026-intel-dives-deep-on-crescent-island-ai-accelerator-larger-caches-and-deeper-xmx-engines-target-maximum-ai-flops-per-watt) —— Intel 在 Hot Chips 上展示新一代 AI 加速器，采用 HBM4 和液冷，目标每瓦性能最大化。
  _Tom's Hardware_
- [Hot Chips 2026: SK hynix 将混合键合推迟至 HBM5](https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-says-hybrid-bonding-wont-be-ready-for-hbm4e-as-ai-memory-runs-into-a-775-micron-ceiling) —— SK hynix 因厚度限制，混合键合技术推迟到 HBM5，HBM4E 继续使用 MR-MUF。
  _Tom's Hardware_
- [Hot Chips 2026: Nvidia 详解 88 核 Vera CPU](https://www.tomshardware.com/pc-components/cpus/hot-chips-2026-nvidia-breaks-down-88-core-vera-cpu-spatial-multithreading-benchmarked-1-2-tb-s-socamm2-memory-agentic-workloads-detailed-and-more) —— Nvidia Vera CPU 面向 Agentic 数据中心，支持空间多线程和 1.2TB/s 内存带宽。
  _Tom's Hardware_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
