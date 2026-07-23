# Curio · AI 算力 / 半导体 · 2026-07-23

> 今日 2 条头条 + 3 条备选

_今天最值得关注的信号是AI基础设施的财务现实开始显形：谷歌Q2自由现金流首次转负，巴克莱预测其将连续两年现金流为负，同时OpenAI的750亿美元支出计划曝光。另一边，Nvidia Vera CPU架构细节公布，与AMD在Agent时代的CPU路线之争正式开打。中国AI生态也在加速独立，Z.ai建成1GW纯国产芯片数据中心。_

---

## 🌟 今日精选

### 2. Nvidia Vera CPU架构首度公开，与AMD路线之争白热化

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Jake Roach_

Nvidia在Hot Chips上详细披露了Vera CPU的Olympus架构，SPEC CPU 2026基准测试成绩首次曝光。Vera主打单线程极致性能，而AMD EPYC Turin走多核并发路线。AMD测算在100千瓦机架场景下，其吞吐量是Vera的2.4倍。这场争论的核心是：Agent时代AI工作负载到底更吃单核还是多核？

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Nvidia Vera CPU采用Olympus架构，SPEC CPU 2026基准测试数据已公布 | SPEC CPU 2026基准测试是否公平反映AI Agent工作负载，尚无定论 |
| Nvidia已出货数十万台Grace独立服务器 | AMD的2.4倍吞吐量数据是否包含实际AI推理场景，有待验证 |
| AMD EPYC Turin在100千瓦机架场景下吞吐量是Vera的2.4倍 | Nvidia的Grace/Vera CPU在生态兼容性上能否挑战AMD的x86优势 |
| Nvidia Rubin架构针对推理进行了优化，从GPU到机架级别都有改进 | Agent时代CPU需求是否真的会从多核转向单核，行业尚未达成共识 |
| Nvidia展示了Vera Rubin NVL72运行OpenAI工作负载的实况 | Nvidia CPU的定价策略和供货能力尚未明确 |

**📖 主编点评**

如果你在搭建个人Agent项目，短期内AMD的多核方案可能更经济。但Nvidia的CUDA生态和GPU+CPU协同优势不容忽视。建议关注2027年Vera量产后的实际性价比，以及AMD的ROCm生态进展。你的content-curator如果涉及本地推理，CPU选型会影响成本和延迟。

📺 [打开原文](https://www.tomshardware.com/pc-components/cpus/nvidia-spills-the-beans-on-vera-cpu-spec-benchmarks-revealed-olympus-architecture-detailed-and-more)

---

### 3. Z.ai建成1GW纯国产芯片AI数据中心，中国AI硬件自主化里程碑

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Luke James_

智谱AI（Z.ai）宣布建成一座1GW的AI数据中心，全部采用国产芯片，已部分通电运行。该中心运行多个万卡集群，完全不依赖Nvidia GPU。与此同时，中国商务部考虑对AI技术实施出口管制，包括禁止本土企业使用台积电代工。中美AI硬件脱钩正在从政策走向现实。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Z.ai完成1GW纯国产芯片AI数据中心建设并部分通电 | 国产芯片集群的实际训练效率和稳定性尚未公开 |
| 数据中心运行多个万卡集群，零Nvidia GPU | 出口管制政策仍在讨论阶段，最终版本可能调整 |
| 中国商务部考虑禁止本土企业使用台积电代工 | 纯国产芯片数据中心的运营成本和能效比未知 |
| 中国考虑对AI模型、训练数据和海外收购实施出口管制 | Kimi K3的2.8万亿参数模型在部署时需要大量硬件，实际可用性存疑 |
| Kimi K3（2.8万亿参数）已发布，价格低于美国闭源模型 | 美国可能进一步升级对华芯片出口限制 |

**📖 主编点评**

中美AI硬件脱钩对你的直接影响是：如果你计划使用国产模型（如Kimi、GLM），API成本可能更低，但需要关注数据合规风险。你的content-curator项目可以预留多模型接口，同时支持国产和海外模型。另外，关注国产芯片生态的MCP支持情况，未来可能成为Agent开发的新选择。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/z-ai-powers-up-1gw-ai-data-center-built-entirely-on-chinese-chips)

---

## 📋 备选阅读

- [TSMC计划2027年提价5%-25%，先进制程涨幅最高](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes) —— 台积电涨价将传导至整个AI产业链，芯片设计公司和云厂商成本压力加大。
  _Anton Shilov_
- [Intel 4制程获得首个代工客户Fortinet，用于防火墙ASIC](https://www.tomshardware.com/tech-industry/semiconductors/intel-4-gets-its-first-foundry-customer-in-fortinet-three-years-after-intel-scoped-the-node-to-meteor-lake) —— Intel代工业务终于迎来首个外部客户，但Fortinet的ASIC并非最先进制程，象征意义大于实际。
  _Luke James_
- [SK Hynix纳斯达克上市，全球内存扩张竞赛加速](https://www.eetimes.com/sk-hynix-nasdaq-debut-shows-global-memory-expansion-race/) —— SK海力士赴美上市，HBM产能竞赛白热化，AI内存需求持续推高资本支出。
  _Pablo Valerio_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
