# Curio · AI 算力 / 半导体 · 2026-06-17

> 今日 2 条头条 + 6 条备选

_今日核心信号：AI算力成本飙升与硬件军备竞赛加速。英伟达B200租赁价将翻倍，交付周期拉长至12-15个月，同时AMD收购MEXT、Intel 18A-P进入风险生产，半导体制造端竞争白热化。大厂动态方面，SpaceX以600亿美元收购Cursor，Anthropic暂停Agent SDK按token计费，AI应用层格局生变。_

---

## 🌟 今日精选

### 1. 英伟达B200租赁价将翻倍，GPU采购新订单排到明年Q2

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _华尔街见闻_

AI推理基础设施服务商Baseten CEO透露，其云服务商已通知B200 GPU租赁价格将于10月续约时上涨约94%，同时采购1000块GPU的交付周期已长达12至15个月。交付瓶颈与租赁涨价叠加，AI推理的算力成本正遭受系统性抬升。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| B200 GPU租赁价格将在10月续约时上涨约94% | 涨价是否仅限B200，还是将蔓延至H100/H200等型号 |
| 采购1000块GPU的交付周期已延长至12-15个月 | 云服务商能否通过增加供应缓解交付瓶颈 |
| Baseten CEO公开透露涨价信息 | 涨价是否会导致部分AI公司转向替代方案（如AMD MI系列） |
| AI推理算力成本面临系统性上升 | 长期看，算力成本上升是否会抑制AI应用创新 |
|  | 是否触发新一轮GPU囤货潮 |

**📖 主编点评**

如果你正在做AI产品，尤其是依赖第三方推理API的，建议立即锁定长期合约或评估自建推理集群的成本。B200涨价只是开始，算力成本将成为2026下半年AI创业公司的核心风险。

📺 [打开原文](https://wallstreetcn.com/articles/3774898)

---

### 3. AMD收购MEXT：用内存分层技术打破AI内存墙，让Flash充当DRAM

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _EE Times_

AMD收购MEXT，获得其Predictive Memory Engine技术，该技术可将不常访问的数据从DRAM卸载到NAND存储，使Flash在应用层表现为DRAM。这直接针对AI数据中心日益严重的内存瓶颈——大模型推理时，KVCache等数据占用大量DRAM，而MEXT技术可显著降低内存成本。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| AMD收购MEXT，获得Predictive Memory Engine技术 | MEXT技术在实际AI工作负载中的性能表现如何 |
| 该技术实现内存分层，让Flash充当DRAM | 与Intel的CXL内存分层方案相比优劣如何 |
| 针对AI数据中心的内存瓶颈问题 | AMD是否会将该技术集成到EPYC或Instinct产品线 |
| 可降低AI推理的内存成本 | 对现有DRAM市场格局的潜在冲击 |
|  | 软件生态适配难度 |

**📖 主编点评**

内存分层是AI基础设施的关键趋势。如果你在搭建推理集群，关注AMD的MEXT技术路线，它可能在未来1-2年显著降低你的内存成本。同时留意Intel的CXL方案，两者将形成竞争。

📺 [打开原文](https://www.eetimes.com/amd-snaps-mext-to-break-the-memory-wall/)

---

## 📋 备选阅读

- [Intel 18A-P进入风险生产，性能提升9%](https://www.tomshardware.com/tech-industry/semiconductors/intels-performance-enhanced-18a-p-process-enters-risk-production-enhanced-node-promises-9-percent-performance-improvement-at-iso-power) —— Intel 18A-P是18A的增强版，承诺等功率下性能提升9%，热阻降低40%，已进入风险生产阶段，是Intel代工业务的关键节点。
  _Tom's Hardware_
- [TSMC：面板级封装短期内不会取代CoWoS](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-says-panel-packaging-wont-replace-cowos-anytime-soon-for-the-largest-future-ai-processors-wafer-level-tech-can-scale-to-58-massive-dies-in-one-package) —— TSMC表示晶圆级封装（CoWoS）仍将主导AI芯片封装，可支持单个封装内集成58个大型芯片，面板级封装（CoPoS）短期内无法替代。
  _Tom's Hardware_
- [Qualcomm拟以80-100亿美元收购Tenstorrent](https://www.tomshardware.com/tech-industry/artificial-intelligence/qualcomm-mulls-taking-over-jim-kellers-tenstorrent-report-claims-deal-for-ai-chipmaker-would-value-the-company-at-between-usd8-billion-and-usd10-billion) —— Qualcomm正在洽谈收购Jim Keller的RISC-V AI芯片公司Tenstorrent，估值80-100亿美元，将直接挑战NVIDIA在AI加速器领域的地位。
  _Tom's Hardware_
- [SMIC 7nm金属间距优于Intel 18A，但密度落后38%](https://www.tomshardware.com/tech-industry/semiconductors/semianalysis-opens-its-own-chip-teardown-lab) —— SemiAnalysis拆解发现，SMIC第三代7nm工艺的最小金属间距为32.5nm，优于Intel 18A，但晶体管密度落后38%，显示中国半导体在特定指标上取得进展。
  _Tom's Hardware_
- [Tensordyne流片基于LNS的AI芯片，功耗比GPU低一个数量级](https://www.eetimes.com/tensordyne-tapes-out-lns-based-ai-chip-claims-huge-power-advantages/) —— Tensordyne流片了基于对数数系（LNS）的AI芯片，声称每token功耗比GPU低一个数量级，可能改变AI推理的能效格局。
  _EE Times_
- [SiMa发布面向物理AI的Agentic开发环境](https://www.eetimes.com/sima-launches-agentic-development-environment-for-physical-ai/) —— 边缘AI芯片公司SiMa推出Agentic开发环境，声称可将工程师迁移到其硬件的时间从数月缩短到数小时，面向机器人等物理AI应用。
  _EE Times_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
