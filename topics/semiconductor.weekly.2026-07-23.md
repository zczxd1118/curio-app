# Curio · AI 算力 / 半导体 · 2026-07-23

> 今日 2 条头条 + 5 条备选

_今天最关键的信号是AI基础设施的财务压力全面暴露：谷歌自由现金流转负、OpenAI承诺750亿美元支出、科技巨头隐藏债务1.65万亿美元。同时，Nvidia Rubin架构和AMD MI450大单表明算力竞赛仍在加速。Agent时代CPU路线之争（Nvidia单核快 vs AMD并发多）将影响你未来做AI工程时的硬件选型。_

---

## 🌟 今日精选

### 1. AMD向Anthropic供应2GW Instinct MI450 GPU，投资50亿美元

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

AMD与Anthropic签署重磅协议：AMD将向Anthropic提供总计2吉瓦（GW）的Instinct MI450 GPU算力，并投资高达50亿美元。首批1GW计划2027年上半年在AMD Helios机架系统中上线。Anthropic已在用AMD MI355X GPU。这笔交易标志着AMD在AI训练芯片市场对Nvidia发起最直接挑战。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| AMD将向Anthropic提供2GW Instinct MI450 GPU算力 | 2GW算力具体对应多少张MI450 GPU尚未披露 |
| AMD将投资Anthropic高达50亿美元 | AMD能否在2027年如期交付MI450并保证良率仍存疑 |
| 首批1GW预计2027年上半年在AMD Helios机架系统中上线 | Anthropic是否会同时保留Nvidia GPU作为备份不确定 |
| Anthropic目前已在AMD MI355X GPU上运行工作负载 | 该协议对AMD数据中心GPU市场份额的实际提升幅度待观察 |
| 协议涵盖AMD下一代Instinct MI450系列加速器 | AMD Helios机架系统的实际性能和能效比尚未公开验证 |

**📖 主编点评**

AMD正在用真金白银和产能承诺撬动Anthropic这个关键客户。如果你做AI推理或微调，2027年AMD MI450可能成为Nvidia之外的性价比选择。建议关注AMD ROCm生态的成熟度——工具链和框架支持将决定你是否能真正用上这些算力。

📺 [打开原文](https://www.tomshardware.com/tech-industry/amd-to-supply-anthropic-with-2-gigawatts-of-instinct-mi450-gpus)

---

### 3. Agent时代CPU路线之争：Nvidia押注单核更快，AMD押注并发更多

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _华尔街见闻_

Nvidia在Hot Chips上首次详细披露Vera CPU架构，强调单线程性能最大化，直接挑战AMD EPYC Turin的高并发路线。AMD测算其EPYC Turin在100千瓦机架场景下吞吐量是Vera的2.4倍。这场争论的核心是：Agentic AI工作负载到底更需要单核推理速度还是多核并行能力？答案将决定未来服务器CPU市场格局。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Nvidia披露Vera CPU架构细节，以单线程最大性能为核心设计目标 | AMD的2.4倍吞吐量对比是否基于公平的功耗和成本条件尚需验证 |
| AMD测算其EPYC Turin在100千瓦机架场景下吞吐量是Vera的2.4倍 | Agentic AI工作负载的实际CPU需求特征尚未有行业共识 |
| Nvidia已出货数十万台Grace standalone服务器 | Nvidia Vera CPU在真实客户部署中的性能数据尚未公开 |
| 两家公司围绕Agentic AI时代CPU核心指标展开公开争论 | 谁先定义行业KPI（单核性能 vs 吞吐量）将影响后续生态走向 |
| 服务器CPU市场规模因AI需求持续膨胀 | Intel在CPU市场的角色被边缘化，但Fortinet订单显示Intel 4仍有竞争力 |

**📖 主编点评**

如果你自己搭建AI推理服务器或做Agent部署，这个路线之争直接影响你的硬件选型。建议：如果你的Agent需要快速响应单次推理（如实时对话），Nvidia路线可能更优；如果你做批量处理或高并发任务（如数据标注、批量评估），AMD路线性价比更高。关注后续第三方基准测试，不要只看厂商自报数据。

📺 [打开原文](https://wallstreetcn.com/articles/3777742)

---

## 📋 备选阅读

- [Nvidia发布DLSS 5，支持三种AI模式实时切换](https://www.tomshardware.com/pc-components/gpus/nvidia-shows-off-dlss-5-with-three-ai-modes-for-different-levels-of-detail-upscaler-can-switch-between-models-in-real-time) —— DLSS 5新增对象级细节调整，开发者可实时切换三种AI模型——对游戏开发者和AI渲染研究者是重要更新，但非游戏玩家可跳过。
  _Tom's Hardware_
- [中国考虑限制AI技术出口，包括禁止使用台积电](https://www.tomshardware.com/tech-industry/artificial-intelligence/china-is-considering-export-controls-on-ai-technologies-including-banning-local-companies-from-using-tsmc-report-claims-restrictions-would-also-advanced-ai-models-training-data-and-overseas-acquisitions) —— 中国商务部拟限制AI模型、训练数据出口，并禁止本土企业使用台积电——地缘政治风险升级，可能影响全球AI芯片供应链。
  _Tom's Hardware_
- [SK海力士纳斯达克上市，全球内存扩张竞赛白热化](https://www.eetimes.com/sk-hynix-nasdaq-debut-shows-global-memory-expansion-race/) —— SK海力士登陆纳斯达克，三星和Micron跟进扩产——HBM和DDR5需求驱动，但DRAM短缺预计持续10年，影响AI服务器成本。
  _EE Times_
- [TSMC计划2027年提价最高25%，先进制程涨5%-10%](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes) —— TSMC涨价将推高AI芯片成本，Nvidia、AMD、Apple等客户利润承压——对个人开发者影响间接，但API价格可能因此上涨。
  _Tom's Hardware_
- [Z.ai（原智谱）建成1GW全国产芯片AI数据中心](https://www.tomshardware.com/tech-industry/artificial-intelligence/z-ai-powers-up-1gw-ai-data-center-built-entirely-on-chinese-chips) —— 智谱用国产芯片建成1GW数据中心，运行多个万卡集群——国产AI算力自主化迈出实质一步，但性能和生态仍是短板。
  _Tom's Hardware_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
