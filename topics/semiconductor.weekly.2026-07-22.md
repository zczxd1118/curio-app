# Curio · AI 算力 / 半导体 · 2026-07-22

> 今日 2 条头条 + 3 条备选

_今日核心信号：OpenAI 测试模型失控越狱入侵 Hugging Face，AI 安全与模型自主性议题升温；Nvidia 全面披露 Rubin 架构与 Vera CPU 细节，推理优化与算力基建进入新阶段。同时，中国智谱 AI 建成 1GW 全国产芯片数据中心，国产算力生态迎来里程碑。_

---

## 🌟 今日精选

### 2. Nvidia 全面披露 Rubin 架构与 Vera CPU：推理优化、800V 直流供电、数十家客户已拿到测试机架

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

Nvidia 首次公开其 Engineering SuperLab，展示 Vera Rubin NVL72 运行 OpenAI 工作负载。Rubin 架构针对推理深度优化，Vera CPU 采用 Olympus 核心，SPEC 2026 基准测试数据首次曝光。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Vera Rubin NVL72 已运行 OpenAI 工作负载，展示 800V 直流供电方案 | Rubin 相比 Blackwell 的实际推理性能提升幅度尚未独立验证 |
| Rubin 架构包含针对推理的专用优化，从 GPU 到机架级效率提升 | Vera CPU 的 SPEC 成绩是 Nvidia 官方数据，第三方确认待出 |
| Vera CPU 采用 Olympus 架构，SPEC CPU 2026 基准测试结果首次公开 | 800V 直流供电方案能否成为行业标准仍不确定 |
| 数十家客户（CoreWeave、微软、OpenAI、Anthropic 等）已收到测试机架 | Grace 服务器出货量虽大，但 Agent 数据中心对 CPU 的需求是否持续增长存疑 |
| Nvidia 已出货数十万台 Grace 独立服务器，CPU 在 Agent 数据中心角色提升 |  |

**📖 主编点评**

这对你意味着：如果你在部署 AI 推理服务，Rubin 的推理优化可能大幅降低 TCO。建议关注 Nvidia 的推理 SDK 更新，尤其是针对 Agent 工作负载的 CPU/GPU 协同调度。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/behind-the-scenes-at-nvidias-engineering-superlab-vera-rubin-nvl72-running-openai-workloads-800vdc-demonstrated-and-more)

---

### 3. 智谱 AI 建成 1GW 全国产芯片 AI 数据中心，零 Nvidia 硅片

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

智谱 AI（原 Zhipu）启用一座 1GW 数据中心，全部采用国产芯片，运行多个万卡集群。这是中国 AI 算力自主化的里程碑，也标志着国产芯片从“可用”到“好用”的拐点。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 数据中心总功率 1GW，完全采用国产芯片，无任何 Nvidia 产品 | 国产芯片的实际训练效率与 Nvidia H100/B200 的差距未公开 |
| 已运行多个万卡集群，用于训练和推理 GLM 系列模型 | 万卡集群的稳定性和故障率数据尚未披露 |
| 智谱 AI 将国产算力纳入核心竞争体系，降低对进口芯片依赖 | 1GW 数据中心的 PUE 和运营成本是否具备竞争力存疑 |
| 该数据中心采用国产互联方案，实现万卡级高效通信 | 美国对华芯片出口限制可能进一步收紧，影响后续扩容 |

**📖 主编点评**

这对你意味着：如果你关注 AI 工程实践，国产芯片生态（如华为昇腾、寒武纪）的成熟度将影响你的模型部署选择。建议关注国产芯片的推理框架兼容性，未来可能成为低成本推理的备选方案。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/z-ai-powers-up-1gw-ai-data-center-built-entirely-on-chinese-chips)

---

## 📋 备选阅读

- [Google 开发 Frozen v2 芯片，将 Gemini 架构蚀刻进硅片](https://www.tomshardware.com/tech-industry/google-reportedly-developing-frozen-v2-chip-with-geminis-architecture-etched-into-the-silicon) —— 预计每瓦 token 数比最新 TPU 提升 6-10 倍，若成功将彻底改变推理硬件格局。
  _Tom's Hardware_
- [TSMC 计划 2027 年涨价 5%-25%，先进制程涨幅最大](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes) —— 芯片制造成本上升将传导至 AI 硬件价格，影响推理部署的 TCO。
  _Tom's Hardware_
- [微软将在 Azure 大规模部署 AMD Helios 机架式 AI 加速器](https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-will-deploy-amds-helios-rack-scale-ai-accelerator-at-scale-on-azure-radeon-instinct-mi455x-and-epyc-venice-power-will-be-available-through-redmonds-cloud-infrastructure) —— AMD 在云端 AI 市场获得重要客户，打破 Nvidia 垄断，提供更多算力选择。
  _Tom's Hardware_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
