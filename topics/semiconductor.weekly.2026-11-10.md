# Curio · AI 算力 / 半导体 · 2026-11-10

> 今日 1 条头条 + 5 条备选

_今天只有一个真正的信号：Nvidia 的 Jensen Huang 丑闻从八卦升级成公司治理与监管事件——董事会立案、国会传唤、集体诉讼、股价跌超 4%，同时 Anthropic 一边发新模型一边推进 IPO。AI 资本叙事正在被两件事同时拉扯：算力军备竞赛（Anthropic 花 34 亿美元买燃气轮机）和信任危机。_

---

## 🌟 今日精选

### 4. DeepX 第二代 AI 加速器流片，LPDDR5x-PIM 架构宣称 6.7 倍性能提升、5W 内跑大模型

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Sally Ward-Foxton_

韩国 DeepX 宣布第二代 AI 加速器完成流片，采用 LPDDR5x 存内计算（PIM）架构，官方给出的数字是 6.7 倍性能提升，目标是在 5W 功耗内本地运行大语言模型，主攻机器人与边缘设备。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 第二代芯片已完成 tape-out，进入流片后阶段 | 6.7 倍是与自家上一代还是与竞品对比，官方口径需要核实 |
| 架构采用 LPDDR5x-PIM（存内计算），宣称性能提升 6.7 倍 | "5W 内跑大模型"的具体模型规模与 token/s 未披露 |
| 目标场景是机器人等边缘市场，可在 5W 以内运行大模型 | PIM 架构的软件栈成熟度是落地关键，目前没有生态信息 |
| 同期 Tom's Hardware 报道其 DX-M1 处理器用"黄油散热器"演示比竞品低 40 度 | 边缘端跑 LLM 的实际需求规模，仍待市场验证 |

**📖 主编点评**

你是电子信息工程背景，这条是少见的"架构层面"而非"产品层面"的进展。存内计算解决的是内存墙问题，值得你花 10 分钟读原文搞清楚 PIM 到底把计算单元放在哪一层——这个概念在面试里比背参数值钱。

📺 [打开原文](https://www.eetimes.com/deepx-tapes-out-second-gen-chip-projects-6-7x-performance-gain-with-lpddr5x-pim/)

---

## 📋 备选阅读

- [Nvidia RTX Spark 加密固件让 Linux 上推理速度掉到 35%](https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop) —— HN 617 分，本地跑模型的硬件自由度在收缩，对自建推理的人是实打实的坏消息。
  _Hacker News_
- [Nvidia 收紧海外云 GPU 对华租赁，合作伙伴面临 51% 非中国配额](https://www.tomshardware.com/tech-industry/policy/nvidia-cracks-down-on-overseas-cloud-ai-gpu-rentals-for-china-partners-face-51-percent-non-chinese-quota-as-black-market-b300-rack-prices-surge-to-usd2-8-million) —— 黑市 B300 整机架价格涨到 280 万美元，出口管制的实际执行细节比政策本身更值得看。
  _Tom's Hardware_
- [内存短缺逼手机厂商把旧设备内存熔下来重新焊到新机上](https://www.tomshardware.com/pc-components/dram/memory-shortage-spurs-smartphone-makers-to-melt-used-memory-off-old-devices-then-re-solder-it-onto-new-products-recycled-memory-to-keep-budget-phones-affordable-reballing-adoption-to-double-by-2027) —— DRAM 涨价传导到消费电子的最直观证据，reballing 采用率预计 2027 年翻倍。
  _Tom's Hardware_
- [律师用 8 张二手 V100 搭私有 AI 服务器，跑 DeepSeek V4.1 Flash 达 215 tokens/s](https://www.tomshardware.com/tech-industry/artificial-intelligence/lawyer-builds-private-ai-server-with-eight-used-nvidia-v100-gpus-up-to-215-tokens-per-second-to-keep-legal-files-offline-costing-about-usd2-400-per-four-gpu-board) —— 四卡板约 2400 美元，2018 年的卡跑 2026 年的模型，本地部署的性价比参考样本。
  _Tom's Hardware_
- [中国建成 800MW AI 数据中心园区对标 Stargate，首期 120MW 一年内交付、成本仅五分之一](https://www.tomshardware.com/tech-industry/data-centers/china-builds-massive-800-megawatt-ai-data-center-campus-to-rival-us-stargate-project-galaxy-campus-delivers-first-120-megawatts-in-a-year-at-one-fifth-the-cost) —— 远景的 Galaxy 园区结合风电、储能和非常规散热，建设速度与成本是这条的重点。
  _Tom's Hardware_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
