# Curio · AI 算力 / 半导体 · 2026-11-08

> 今日 1 条头条 + 4 条备选

_今天最重要的信号只有一个：AI 交易在中期选举后遭遇系统性重估——Nasdaq 单日跌 4-5%，两天蒸发 2.5 万亿美元，芯片股创 1896 年以来最差中期选举后表现。与此同时，Anthropic 的 METR 报告显示 AI 自我加速研发已跑出斜率，OpenAI 估值冲到 1.25 万亿。基本面在加速，估值在崩塌，这两件事同时成立，是本周最值得盯的张力。_

---

## 🌟 今日精选

### 4. TSMC 否认应 Nvidia 要求研发 3D DRAM：先进内存离量产仍有数年

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Anton Shilov_

Tom's Hardware 报道，Nvidia 据称要求 TSMC 生产 3D DRAM 以缓解内存短缺，TSMC 公开否认正在探索该方向，并指出这类先进内存技术距市场可行仍有数年。这条否认本身比传闻更有信息量：它暴露了 AI 算力的下一个瓶颈在内存，而不在逻辑制程。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| TSMC 公开否认正在为 Nvidia 探索 3D DRAM | Nvidia 是否真的提出请求，目前只有单一信源 |
| 报道称 Nvidia 曾就 3D DRAM 提出请求以应对内存短缺 | 3D DRAM 与 HBM 路线是替代还是互补，业界未定 |
| TSMC 表示该技术距量产可行仍有数年 | 内存短缺对 2027 年 GPU 出货的实际约束程度未知 |
| 同期 Nvidia 与 Micron 合计占美国盈利增长约 34% | TSMC 否认是技术判断还是客户关系考量，无法区分 |

**📖 主编点评**

如果你关注推理优化，这条提醒你：未来两年的瓶颈会从 FLOPS 转向内存带宽和容量。做 RAG 或长上下文 Agent 时，优先考虑能减少 KV cache 占用的方案（量化、分页注意力、上下文压缩），这些在内存受限的硬件上收益最大。

---

## 📋 备选阅读

- [Nvidia RTX Spark 加密固件把 Linux 上推理速度压到 35%](https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop) —— HN 615 分，加密固件拖慢本地推理，对想本地跑模型的人是硬约束。
  _novaRom_
- [Nvidia 讨论按 GPU 收每年 2000 美元软件费，用于跑 Agent 负载](https://www.tomshardware.com/pc-components/gpus/nvidia-discusses-usd2-000-per-gpu-annual-software-fee-for-running-agents-on-ai-infrastructure-firm-already-charges-more-than-twice-that-amount-for-its-ai-enterprise-software-platform) —— 按 GPU 收软件订阅费，是 Nvidia 从卖硬件转向收租的关键一步。
  _gscott_
- [Gelsinger 支持的 Nagare Labs 发布 Z2RAM：SRAM 速度、DRAM 密度](https://www.tomshardware.com/tech-industry/semiconductors/gelsinger-backed-nagare-labs-capacitorless-z2ram-promises-sram-speed-with-dram-density-latest-published-cell-retains-data-for-over-300-seconds-at-85-c-but-further-figures-are-projected) —— 无电容存储堆叠在 AI 加速器上，85°C 下保持 300 秒，数据尚属早期。
  _Shane Downing_
- [Tesla 公布 AI 加速器路线图，SI6 带来 80 倍算力，Dojo 3 要上太空](https://www.tomshardware.com/tech-industry/artificial-intelligence/tesla-unveils-ai-accelerator-roadmap-adopts-new-si-branding-in-super-intelligence-push-si6-to-bring-80x-more-compute-performance-dojo-3-headed-to-space) —— 自研芯片野心很大，但 80 倍和上太空都缺时间表，先记着。
  _Anton Shilov_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
