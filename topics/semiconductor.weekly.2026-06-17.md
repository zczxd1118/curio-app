# Curio · AI 算力 / 半导体 · 2026-06-17

> 今日 2 条头条 + 4 条备选

_今日核心信号：SpaceX 上市后即以 60B 美元收购 AI 编程工具 Cursor，标志着 AI 编程赛道进入巨头整合期；同时英伟达 B200 租赁价翻倍、AMD 收购 MEXT 打破内存墙，算力成本结构性上升。你的 content-curator 项目应关注 Cursor 被收购后的生态变化，以及 MCP/Skills 等工具链的工程实践。_

---

## 🌟 今日精选

### 2. 英伟达 B200 租赁价将翻倍，GPU 采购排到明年 Q2，AI 推理算力成本系统性上升

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _华尔街见闻_

AI 推理基础设施服务商 Baseten 透露，其云服务商已通知英伟达 B200 GPU 租赁价格将于 10 月续约时上涨约 94%，同时采购 1000 块 GPU 的交付周期已长达 12 至 15 个月。交付瓶颈与租赁涨价叠加，AI 推理的算力成本正遭受系统性抬升，直接影响所有依赖云端 GPU 的 AI 应用开发者。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| B200 租赁价格将在 10 月续约时上涨约 94% | 涨价是否会传导至其他 GPU 型号（如 H100、H200） |
| 采购 1000 块 GPU 的交付周期为 12-15 个月 | 云服务商（AWS、Azure、GCP）是否会跟随涨价 |
| Baseten 的云服务商已正式通知涨价 | AMD MI300X 等替代品能否缓解供应压力 |
| 英伟达 B200 是当前 AI 推理主力 GPU 之一 | AI 初创公司是否会因算力成本上升而调整商业模式 |
|  | 长期来看，推理算力成本上升是否会加速边缘 AI 和模型压缩技术 adoption |

**📖 主编点评**

你正在用 Claude Code 和 Cursor 做项目，这些工具背后都依赖云端 GPU 推理。B200 涨价意味着你的 AI 编程工具使用成本可能上升，或者免费额度会缩水。建议：1）评估本地运行小模型（如 Llama 3 70B）的可行性，减少云端依赖；2）关注 AMD MI300X 等替代 GPU 的云服务上线时间；3）在你的 content-curator 项目中加入成本监控模块，跟踪 API 调用费用变化。

📺 [打开原文](https://wallstreetcn.com/articles/3774898)

---

### 3. AMD 收购 MEXT 打破内存墙：让闪存充当 DRAM，AI 内存成本有望大幅降低

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _EE Times_

AMD 宣布收购 MEXT，获得其 Predictive Memory Engine 技术，该技术允许将 NAND 闪存作为 DRAM 使用，通过智能内存分层大幅降低 AI 工作负载的内存成本。MEXT 的技术可以自动将不常访问的数据从 DRAM 卸载到 NAND，同时保持对应用程序的透明性。这对 AI 推理和训练的内存瓶颈是一个潜在的突破。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| AMD 收购 MEXT，获得 Predictive Memory Engine 技术 | 实际性能表现——闪存延迟与 DRAM 仍有数量级差距，适用场景有限 |
| 该技术允许闪存作为 DRAM 使用，对应用程序透明 | 与现有 CXL 内存池化方案的竞争关系 |
| 主要面向数据中心和 AI 工作负载的内存分层 | AMD 能否快速集成并推向市场，避免被 Intel 或英伟达抢先 |
| AMD 计划将技术集成到 EPYC 和 Instinct 产品线 | 对 AI 训练场景的帮助可能有限，推理场景更受益 |
|  | 定价策略——是否会作为免费软件特性还是付费选项 |

**📖 主编点评**

内存墙是 AI 系统性能的关键瓶颈，MEXT 技术如果成熟，可以让你在本地运行更大模型或更长的上下文。对于你的 content-curator 项目，这意味着未来可能用更低的成本在本地部署 RAG 系统。建议：1）关注 AMD 的 ROCm 软件栈对 MEXT 的支持时间表；2）在你的项目中预留内存分层感知的接口，未来可以自动选择冷热数据存储策略。

📺 [打开原文](https://www.eetimes.com/amd-snaps-mext-to-break-the-memory-wall/)

---

## 📋 备选阅读

- [Qualcomm 考虑以 80-100 亿美元收购 Jim Keller 的 Tenstorrent](https://www.tomshardware.com/tech-industry/artificial-intelligence/qualcomm-mulls-taking-over-jim-kellers-tenstorrent-report-claims-deal-for-ai-chipmaker-would-value-the-company-at-between-usd8-billion-and-usd10-billion) —— RISC-V AI 芯片公司 Tenstorrent 可能被 Qualcomm 收购，与 SpaceX 收购 Cursor 形成 AI 硬件+软件的双重整合趋势。
  _Tom's Hardware_
- [Intel 18A-P 工艺进入风险生产，性能提升 9%，热阻降低 40%](https://www.tomshardware.com/tech-industry/semiconductors/intels-performance-enhanced-18a-p-process-enters-risk-production-enhanced-node-promises-9-percent-performance-improvement-at-iso-power) —— Intel 的 18A-P 增强版进入风险生产，是 Intel 代工业务的关键里程碑，但量产时间仍待观察。
  _Tom's Hardware_
- [TSMC 称面板级封装短期内不会取代 CoWoS，晶圆级可封装 58 个巨型芯片](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-says-panel-packaging-wont-replace-cowos-anytime-soon-for-the-largest-future-ai-processors-wafer-level-tech-can-scale-to-58-massive-dies-in-one-package) —— TSMC 明确 CoWoS 仍是 AI 芯片封装主流，面板级封装（CoPoS）还需数年，AI 芯片封装瓶颈短期难解。
  _Tom's Hardware_
- [SiMa 推出面向物理 AI 的 Agentic 开发环境](https://www.eetimes.com/sima-launches-agentic-development-environment-for-physical-ai/) —— 边缘 AI 芯片公司 SiMa 发布 Agentic 开发环境，可将工程师迁移到其硬件的时间从数月缩短到数小时。
  _EE Times_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
