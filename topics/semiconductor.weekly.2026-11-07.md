# Curio · AI 算力 / 半导体 · 2026-11-07

> 今日 1 条头条 + 4 条备选

_今天最重要的信号是 AI 资本叙事第一次被政治和账本同时打脸：中期选举民主党大胜后，41 项数据中心公投几乎全数通过限制性条款，纳指两天跌进修正区间、2.5 万亿美元市值蒸发；同一时间 OpenAI 又在新一轮拿到 110 亿美元、估值 1.25 万亿。钱还在往里冲，但"无限扩张"的假设已经开始被定价。另一个信号是 Nvidia 的供应链正在从"卖卡"变成"管卡"——东南亚追踪、130 处旧电信机房改造、11.4M GPU 被盗，都在说明算力已经稀缺到需要治安。_

---

## 🌟 今日精选

### 3. Nvidia 想把 130 多处旧电信机房改成小型数据中心，估算可产出 1GW 算力

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Jowi Morales_

Nvidia 正在和 Brightspeed 谈，把后者在全美 130 多处闲置电信设施改造成分布式小型数据中心，估算总算力可达 1GW。同期它要求东南亚云厂商加入 Fleet Intelligence 追踪计划才能拿到官方合作伙伴资格。两件事指向同一个方向：算力稀缺到需要重新分配存量基础设施，并且需要治安。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Nvidia 与 Brightspeed 就 130+ 处旧电信设施改造进行谈判 | 1GW 是理论上限，实际受供电与散热改造限制，落地比例未知 |
| Nvidia 估算这些设施合计可产出最高 1GW 算力 | 旧电信机房的网络时延能否满足训练集群需求，报告未说明 |
| Brightspeed 母公司为 Apollo Global Management | Fleet Intelligence 的实际监控粒度（序列号级还是批次级）未公开 |
| Nvidia 要求东南亚云厂商加入 Fleet Intelligence 追踪计划才可获得 Nvidia Cloud Partner 资格 | 分布式小机房是否会成为推理主力、训练仍集中，取决于互联带宽成本 |
| 同期加州发生 6 托盘、价值 1140 万美元 Nvidia GPU 被盗案 |  |

**📖 主编点评**

如果你关注推理部署成本，这条是本周最值得记的结构性变化：算力供给正在从"建超大园区"转向"盘活存量机房"。对个人项目的含义是，未来一两年边缘侧推理节点的地理分布会更密，延迟敏感型 Agent（语音、实时检索）的可行性会上升。可以开始留意支持多区域 endpoint 的推理服务商。

📺 [打开原文](https://www.tomshardware.com/tech-industry/data-centers/nvidia-wants-to-repurpose-over-130-old-telco-buildings-as-tiny-data-centers-report-claims-company-in-talks-with-brightspeed-after-pitching-idea-to-parent-company-apollo-global-management)

---

## 📋 备选阅读

- [Marvell 以 1150 亿美元全股票收购 Lumentum，押注 AI 数据中心光互联](https://www.tomshardware.com/tech-industry/semiconductors/marvell-to-buy-lumentum-in-usd115-billion-all-stock-deal-combined-company-to-supply-scale-up-and-scale-in-optics-for-ai-data-centers) —— 全股票 1150 亿是本周最大并购，光互联正在成为算力瓶颈的下一个战场，但全股票交易的对价含金量需打折看。
  _Etiido Uko_
- [GlobalFoundries 公布 FDX Fusion：不用 EUV 做到 7nm 级性能，目标 2030 量产](https://www.tomshardware.com/tech-industry/semiconductors/globalfoundries-vp-details-fdx-fusion-technology-sporting-7nm-class-performance-without-the-need-for-euv-tools-company-targets-2030-for-high-volume-manufacturing-with-planar-transistors-in-tow) —— 绕开 EUV 的路线对非美供应链有战略意义，但 2030 量产太远，短期不影响任何选型决策。
  _Anton Shilov_
- [Nvidia RTX Spark 加密固件被指在 Linux 上把推理速度压到 35%](https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop) —— 本地推理玩家必看，但只有单一来源与 614 分讨论，缺独立复现，先当线索不当结论。
  _novaRom_
- [Gelsinger 支持的 Nagare Labs 发布 Z2RAM：SRAM 速度、DRAM 密度](https://www.tomshardware.com/tech-industry/semiconductors/gelsinger-backed-nagare-labs-capacitorless-z2ram-promises-sram-speed-with-dram-density-latest-published-cell-retains-data-for-over-300-seconds-at-85-c-but-further-figures-are-projected) —— 85°C 下保持 300 秒的数据点很具体，但仍是实验室单元级结果，离可堆叠量产有距离。
  _Shane Downing_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
