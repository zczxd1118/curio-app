# Curio · AI 算力 / 半导体 · 2026-11-08

> 今日 1 条头条 + 4 条备选

_今天最重要的信号只有一个：AI 叙事在资本市场被重新定价。中期选举后 Nasdaq 两日跌 5%、2.5 万亿美元市值蒸发、芯片股创 1896 年以来最差中期选举后单日表现，而 Ramp 数据显示企业 AI 支出在 Anthropic IPO 前夕停滞。另一条线是 Anthropic 用 AI 造 AI 的 METR 报告——如果模型迭代速度真的翻倍，那估值和算力支出的分歧只会更大。_

---

## 🌟 今日精选

### 4. Nvidia RTX Spark 加密固件被指在 Linux 下把推理速度压到 35%，本地跑模型的硬件自由度在收缩

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _novaRom_

HN 上一条 615 分的帖子指出，Nvidia RTX Spark 笔记本的加密固件在 Linux 环境下把推理性能限制到约 35%。这不是驱动 bug，而是固件层面的策略性限制。对依赖本地 GPU 跑开源模型的开发者来说，这是硬件厂商收紧控制权的一个具体信号。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| RTX Spark 笔记本存在加密固件 | 35% 的测量方法与测试模型未在帖子中完整披露 |
| Linux 下推理性能约为满速的 35% | 是否为反盗版/反挖矿策略的副作用，Nvidia 尚未回应 |
| 该现象在 HN 获得 615 分讨论 | Windows 下是否存在同等限制，目前无对照数据 |
| 限制发生在固件层而非驱动层 | 是否会影响消费级以外的产品线，暂无证据 |

**📖 主编点评**

如果你考虑用消费级 Nvidia 卡做本地推理或 Agent 沙箱，这条是明确的预警：买之前先查该型号在 Linux 下的实测吞吐，别只看纸面 TFLOPS。长期看，本地推理的硬件选择会越来越需要在「性能」和「可控性」之间做取舍，AMD/Apple Silicon 的性价比权重会上升。

📺 [打开原文](https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop)

---

## 📋 备选阅读

- [TSMC 否认应 Nvidia 要求探索 3D DRAM：先进内存技术距量产仍有数年](https://www.tomshardware.com/pc-components/dram/tsmc-denies-exploring-3d-dram-at-nvidias-request-advanced-memory-tech-is-still-years-from-market-viability) —— HBM 之后的下一代内存路线被官方否认，说明内存墙短期无解，对推理成本判断有参考价值。
  _Anton Shilov_
- [Nvidia 拟对每块 GPU 收取 2000 美元/年软件费，用于在 AI 基建上跑 Agent](https://www.tomshardware.com/pc-components/gpus/nvidia-discusses-usd2-000-per-gpu-annual-software-fee-for-running-agents-on-ai-infrastructure-firm-already-charges-more-than-twice-that-amount-for-its-ai-enterprise-software-platform) —— 如果成真，Agent 推理的边际成本结构会变，直接影响你做 Agent 产品的成本模型。
  _gscott_
- [GlobalFoundries 详解 FDX Fusion：无需 EUV 做到 7nm 级性能，目标 2030 量产](https://www.tomshardware.com/tech-industry/semiconductors/globalfoundries-vp-details-fdx-fusion-technology-sporting-7nm-class-performance-without-the-need-for-euv-tools-company-targets-2030-for-high-volume-manufacturing-with-planar-transistors-in-tow) —— 非 EUV 路线的具体技术参数首次公开，是半导体供应链去风险叙事里少见的硬信息。
  _Anton Shilov_
- [Tesla 公布 AI 加速器路线图，启用 SI 品牌：SI6 带来 80 倍算力，Dojo 3 要上太空](https://www.tomshardware.com/tech-industry/artificial-intelligence/tesla-unveils-ai-accelerator-roadmap-adopts-new-si-branding-in-super-intelligence-push-si6-to-bring-80x-more-compute-performance-dojo-3-headed-to-space) —— 自研推理芯片路线图，80 倍是营销数字还是实测口径需要打问号，但方向值得记录。
  _Anton Shilov_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
