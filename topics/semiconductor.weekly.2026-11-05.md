# Curio · AI 算力 / 半导体 · 2026-11-05

> 今日 1 条头条 + 4 条备选

_今天最重要的信号有两个：一是美国中期选举把 AI 数据中心投成了政治议题，45 项地方公投几乎全线否决，Stratechery 和 TechCrunch 都在追问"如果反对建设是长期民意，算力扩张还怎么走"；二是内存/存储涨价已经从 DRAM 蔓延到 Nintendo 卡带供应链，Team Group CEO 直接说"钱也买不到货"。对做 Agent 的你来说，另一条值得盯的是 Meta 收购 Conductor——多 Agent 并行写代码正在被大厂收编。_

---

## 🌟 今日精选

### 2. 内存危机升级：Team Group CEO 称"钱也买不到货"，明年价格无下行趋势，Apple 制造成本多出 330 亿美元

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Jowi Morales_

存储涨价不再是"贵一点"的问题。Team Group CEO 陈庆文在财报电话会上说，价格明年没有任何下行趋势，极端情况是"有钱也拿不到货"。同一天，Apple 因内存成本上升制造成本增加 330 亿美元，Nintendo 的 ROM 芯片供应商 Macronix 直接退出该业务转做 AI 数据中心闪存。AI 数据中心对 HBM 和服务器内存的挤占，正在把消费电子和游戏卡带的供应链一起拖下水。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Team Group CEO 明确表态：明年内存价格无任何下行趋势 | 涨价周期会持续多久，取决于 AI 数据中心资本开支何时见顶，目前无人给出可信拐点 |
| Apple 制造成本因内存涨价增加 330 亿美元，压力延续到 2027 | 消费级 GPU/整机价格是否会被同步推高，RTX 5090 街价已破 9000 美元但样本有限 |
| Macronix 退出 Nintendo ROM 芯片业务，转产 AI 数据中心用 NOR/NAND | 国产存储厂商能否填补中低端缺口，尚无产能数据 |
| Samsung、SK hynix、Micron 优先把产能分配给高毛利服务器产品与 HBM | 游戏实体卡带是否真的涨价，取决于库存消化速度 |
| Micron 公布 DRAM/NAND 新路线图，含 3D NAND 与 High-NA EUV |  |

**📖 主编点评**

如果你近期要买机器跑本地模型或做推理实验，别等降价——这轮周期的方向是单边的。更实际的建议：把本地推理需求往云端或按需租用迁移，或者优先考虑二手/租赁。做 Agent 项目时也要意识到，token 单价的长期趋势不再是无脑下降，成本模型里该留出涨价缓冲。

📺 [打开原文](https://www.tomshardware.com/pc-components/dram/team-group-ceo-warns-memory-crisis-could-reach-point-where-even-money-cant-buy-goods-will-get-worse-next-year-with-no-downward-trend-in-price-whatsoever)

---

## 📋 备选阅读

- [Nvidia 讨论按 GPU 每年 2000 美元收软件费，用于在 AI 基建上跑 Agent](https://www.tomshardware.com/pc-components/gpus/nvidia-discusses-usd2-000-per-gpu-annual-software-fee-for-running-agents-on-ai-infrastructure-firm-already-charges-more-than-twice-that-amount-for-its-ai-enterprise-software-platform) —— 如果 Agent 运行要按 GPU 年费计费，会直接改变 Agent 产品的成本结构，值得提前知道定价风向。
  _gscott_
- [Nvidia 只能满足中国 700 亿美元 GPU 订单的 1%](https://www.tomshardware.com/pc-components/gpus/nvidia-can-only-fulfill-1-percent-of-chinas-massive-usd70-billion-gpu-order-for-ai-chips-report-claims-supply-constraints-choke-export-friendly-rtx-pro-5500-deliveries-despite-huge-demand) —— 供给约束 + 出口管制的双重挤压，1% 的履约率是个极端数字，反映全球算力分配的紧张程度。
  _Ben Stockton_
- [Nvidia RTX Spark 加密固件让 Linux 上推理速度降到 35%](https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop) —— HN 600 分热帖，加密固件拖慢 Linux 推理，对想用消费级卡跑本地模型的人是直接的坏消息。
  _novaRom_
- [Google 发布 Gemini 4 Carbon，微弱超过 Claude Opus 5.5，号称最不易幻觉](https://www.tomshardware.com/tech-industry/artificial-intelligence/google-reveals-new-gemini-4-carbon-ai-model-narrowly-beating-claude-opus-5-5-frontier-ai-model-is-also-the-least-likely-to-hallucinate-benchmarks-claim) —— 模型发布动态，Carbon 在 Artificial Analysis 榜单登顶，但"微弱超过"意味着前沿模型差距已进入噪声区间。
  _Jon Martindale_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
