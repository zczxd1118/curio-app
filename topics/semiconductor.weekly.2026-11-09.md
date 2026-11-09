# Curio · AI 算力 / 半导体 · 2026-11-09

> 今日 1 条头条 + 4 条备选

_今天最重要的信号有两个：一是 Nvidia CEO 黄仁勋承认与疑似中国间谍有私情、董事会启动独立调查，这条从产业新闻升级成治理与地缘风险事件，直接牵动 AI 算力叙事；二是 AI 泡沫论在二级市场兑现——纳指跌入回调区间、2.5 万亿美元市值蒸发、Anthropic IPO 被质疑 1.5 万亿估值。对做 Agent 的你来说，工具层仍在快速迭代（Claude 桌面端整合 Code、DeepSeek Harness 生态），但融资和估值环境在收紧，值得把注意力放在能自己跑起来的东西上。_

---

## 🌟 今日精选

### 4. DeepX 二代 AI 加速器流片：LPDDR5x-PIM 架构，宣称 6.7 倍性能提升、5W 内跑大模型

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Sally Ward-Foxton_

韩国边缘 AI 芯片公司 DeepX 完成第二代加速器流片，采用 LPDDR5x 存内计算（PIM）架构，官方称性能提升 6.7 倍，可在 5W 功耗内于设备端运行大语言模型，目标市场包括机器人。这是存内计算从论文走向量产芯片的一个具体节点。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DeepX 第二代 AI 加速器已完成流片（tape-out） | 6.7 倍是与自家一代还是竞品对比，报道未明确 |
| 采用 LPDDR5x-PIM 存内计算架构 | 5W 跑'大模型'的具体参数量与量化方式未披露 |
| 官方宣称性能提升 6.7 倍 | 量产时间与良率仍是未知数 |
| 可在 5W 功耗内运行大模型，面向机器人与边缘市场 | PIM 架构的软件生态成熟度存疑 |

**📖 主编点评**

你是电子信息工程背景，这条是少见的'架构级'信号：存内计算正在从概念变成流片产品。如果你对推理优化感兴趣，PIM 是值得提前建立认知的方向——它改变的是'内存墙'这个根本约束，而不只是又一个加速卡。

📺 [打开原文](https://www.eetimes.com/deepx-tapes-out-second-gen-chip-projects-6-7x-performance-gain-with-lpddr5x-pim/)

---

## 📋 备选阅读

- [Diamond Foundry 造出全球首片 200mm 单晶金刚石晶圆](https://www.tomshardware.com/pc-components/cooling/diamond-foundry-creates-worlds-first-200mm-single-crystal-diamond-wafer-massive-gem-aims-to-solve-ai-chip-cooling-crisis-envisioned-as-a-cooling-material-for-semiconductors) —— 用金刚石做 AI 芯片散热，从材料端解热点问题，是散热瓶颈里少见的硬进展。
  _Jowi Morales_
- [家用玩家用二代 Optane 内存条在纯 CPU 上跑 2.8 万亿参数 Kimi K3](https://www.tomshardware.com/tech-industry/artificial-intelligence/homelabber-uses-second-gen-optane-memory-sticks-to-run-a-2-8-trillion-parameter-ai-model-on-cpu-alone-warns-that-optanes-extreme-heat-can-burn-out-nearby-memory-dram-used-blower-fans-to-prevent-melting-ram) —— 1-bit 量化下 0.85 tokens/s，慢但能跑，是'内存层级决定推理可行性'的极端案例。
  _Shane Downing_
- [TSMC 否认应 Nvidia 要求探索 3D DRAM](https://www.tomshardware.com/pc-components/dram/tsmc-denies-exploring-3d-dram-at-nvidias-request-advanced-memory-tech-is-still-years-from-market-viability) —— 内存短缺逼得 Nvidia 找代工谈 3D DRAM，台积电泼冷水说离量产还有数年——存储墙是真问题。
  _Anton Shilov_
- [64GB 内存 PC 占比同比暴跌 18%，AI DRAM 涨价反噬消费端](https://www.tomshardware.com/pc-components/ram/pcs-with-64gb-of-ram-plummet-18-percent-as-memory-prices-soar-cpu-z-install-base-data-shows-ddr4-making-a-surprise-comeback) —— CPU-Z 数据显示内存容量首次下滑，AI 抢产能的代价落到普通装机用户头上。
  _Zhiye Liu_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
