# Curio · AI 算力 / 半导体 · 2026-11-19

> 今日 2 条头条 + 4 条备选

_今天最重要的信号有两个：一是 Nvidia 在黄仁勋辞职后首次交出季报，营收 1158 亿美元、利润依旧强劲，但董事会明确不打算让黄回归，公司进入「后黄仁勋时代」的过渡期；二是 Anthropic 以每股 83 美元、1.5 万亿美元估值完成 IPO 定价，AI 一级市场的泡沫争论被推到台前。对做 Agent 的你来说，今天还有一条值得细读的工程实践：用三块二手 V100 跑出 100 tok/s 的家庭实验室方案，成本只要 1042 美元。_

---

## 🌟 今日精选

### 1. Nvidia 过渡期首份季报：营收 1158 亿美元，董事会明确不迎回黄仁勋

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _EE Times_

黄仁勋 11 月 12 日辞职后，Nvidia 由临时 CEO Colette Kress 主持，交出的第一份季报营收 1158 亿美元，AI 基础设施需求仍是主引擎。但董事会主席 Harvey Jones 同日表态「不打算让黄回归」，意味着这家 AI 算力霸主正式进入没有创始人的治理结构。短期业绩无虞，长期战略连续性才是真问题。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Nvidia 在临时 CEO Colette Kress 治下公布季度营收 1158 亿美元，AI 基础设施需求是主要拉动 | 1158 亿美元是否包含一次性订单前置，需等 10-Q 补交后才能确认 |
| 黄仁勋于 2026 年 11 月 12 日因第二段办公室恋情曝光而立即辞职 | Colette Kress 能否在 CES 2027 前稳住大客户（微软、Meta、xAI）的多年采购承诺，尚无公开信号 |
| 董事会主席 Harvey Jones 公开表示董事会不打算让黄仁勋重新担任 CEO | 黄仁勋通过盟友讨论「回归」的传闻仍在，董事会表态能否顶住员工联名请愿的压力存疑 |
| 公司未按惯例按时提交 10-Q 季报文件，引发华尔街分析师追问 | 新加坡销售披露中断是否与 Megaspeed 转口争议有关，监管层尚未定性 |
| Nvidia 同期停止披露新加坡地区销售数据，该地区此前是营收关键披露项 | 「后黄仁勋时代」Nvidia 的 CUDA 生态投入节奏会不会放缓，目前只有高管口头承诺 |

**📖 主编点评**

你不需要现在判断 Nvidia 的股价，但需要盯住两件事：一是 10-Q 补交后营收结构里有没有「渠道压货」的痕迹，二是 Colette Kress 在下次财报电话会上对 CUDA 路线图的表述。如果你在做依赖 Nvidia 推理卡的 Agent 项目，短期供应不会断，但 2027 年的 GPU 租赁定价可能因为治理不确定性而波动，签长约前多留一个退出条款。

📺 [打开原文](https://www.eetimes.com/nvidia-reports-115-8b-in-quarterly-revenue-under-interim-ceo/)

---

### 4. 三块「电子垃圾」V100 组 1042 美元家庭实验室，Qwen 3.6 35B 跑到 100 tok/s，长上下文反超 5399 美元 Mac Studio

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

一位 homelab 玩家用三块退役的 Nvidia Tesla V100，搭出总成本 1042 美元的推理机，跑 Qwen 3.6 35B 达到约 100 tokens/s，在长上下文场景下反超售价 5399 美元的 M5 Max Mac Studio。这条的价值不在「省钱」，而在于它给出了一个可复现的二手卡推理配置，对预算有限的独立开发者是真实可用的基线。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 配置为三块二手 Nvidia Tesla V100，整机成本约 1042 美元 | 100 tok/s 的具体 batch size 和上下文长度未在摘要中给出，需看原文表格 |
| 在 Qwen 3.6 35B 模型上达到约 100 tokens/s 的推理速度 | V100 不支持 FP8，实际能效比和电费成本未计入 1042 美元 |
| 在长上下文场景下吞吐超过售价 5399 美元的 M5 Max Mac Studio | 二手卡无保修，长期故障率是隐藏成本 |
| V100 为 16GB/32GB HBM2 版本，二手市场供应来自数据中心退役 | 该配置能否稳定跑 128K 上下文，取决于具体推理框架和量化方案 |

**📖 主编点评**

如果你认真考虑过「自己搭一台推理机跑本地 Agent」，这条是本周最值得存的工程参考。重点抄三样东西：V100 的型号（16GB 还是 32GB）、用的推理框架（vLLM 还是 llama.cpp）、以及长上下文测试的具体 prompt 长度。但先算一笔电费——三块 V100 满载约 900W，按你所在城市电价跑一个月，可能比 API 账单还贵。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/three-e-waste-nvidia-v100s-hit-100-tokens-per-second-on-qwen-3-6-35b-in-a-usd1-042-homelab-rig-decommissioned-gpus-outpace-a-usd5-399-m5-max-mac-studio-at-long-contexts)

---

## 📋 备选阅读

- [Nvidia 被曝通过循环融资抬高 GPU 价格、制造稀缺](https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus) —— HN 1114 分，指控 Nvidia 投资 AI 初创再让它们买自家 GPU，是理解「AI 算力金融化」的关键背景，但属指控未定论。
  _TechPowerUp_
- [TSMC 遭黑客攻击，SEC 文件披露](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000800/a20261112statementregardin.htm) —— 11 月 12 日的 SEC 披露，台积电确认安全事件，对全球先进制程供应的影响尚未量化，值得跟踪。
  _SEC Filing_
- [荷兰拒绝美国进一步收紧半导体出口管制的要求](https://www.politico.eu/article/dutch-resist-unacceptable-us-bid-to-tighten-semiconductor-export-controls-asml/) —— 11 月 18 日，荷兰称美方要求「不可接受」，ASML 对华出口的政策博弈进入新回合，影响 2027 年设备供应预期。
  _Politico_
- [DDR6 标准预览：模块缩小 44%，带宽 4 倍于 DDR5 基线](https://www.tomshardware.com/pc-components/ram/ddr6-ram-shrinks-by-44-percent-while-delivering-4x-ddr5s-baseline-bandwidth-jedec-previews-12-8-gt-s-modules-with-up-to-1-terabyte-of-capacity-per-slot) —— JEDEC 预览 12.8 GT/s、单槽最高 1TB，对做本地推理的人意味着 2028 年的内存墙会松动，但离落地还远。
  _Tom's Hardware_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
