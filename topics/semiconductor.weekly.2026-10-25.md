# Curio · AI 算力 / 半导体 · 2026-10-25

> 今日 2 条头条 + 3 条备选

_今天最重要的两个信号：一是 AI 资本叙事开始松动——Anthropic 估值被传缩水 5000 亿美元、Firmus 30 亿美元 IPO 48 小时崩盘、数据中心股集体下挫，钱开始重新定价算力；二是工程侧出现真东西，Opus 5.5 agent 自主发现两个室温磁性半导体候选材料，这是 agent 从写代码走向做科研的第一个可验证样本。_

---

## 🌟 今日精选

### 1. Opus 5.5 agent 自主筛出两个室温磁性半导体候选材料，AI 开始做真科研

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _outlier99_

Vals.ai 放出一份实验报告：用 Opus 5.5 驱动的多 agent 流水线，从材料数据库检索、假设生成到第一性原理筛选全流程无人干预，最终给出两个室温磁性半导体候选。室温铁磁半导体是自旋电子学的圣杯级难题，几十年没有实用材料。这件事的分量不在结果本身，而在于它第一次把 agent 的产出放到了可被实验证伪的位置。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Vals.ai 公开博客，完整描述 agent 流水线的检索、假设、筛选三段结构 | 候选材料尚未经实验合成验证，室温铁磁性是否成立仍是开放问题 |
| 产出为两个室温磁性半导体候选材料，附具体筛选路径 | agent 的筛选逻辑是否只是复述已有文献结论，报告未给出消融实验 |
| 使用 Opus 5.5 作为推理内核，多 agent 协作完成 | 这类'AI 发现材料'此前多次被质疑为事后挑选，需要第三方复现 |
| HN 上 495 分，讨论集中在筛选标准是否可复现 | 若成立，对自旋电子学与低功耗存储的影响量级尚无法估计 |

**📖 主编点评**

你正在做 content-curator，这条是绝佳的方法论参照：agent 的价值不在'能查'，而在'能给出可被证伪的结论'。建议你去看它的 agent 编排结构，尤其是假设生成和筛选之间怎么交接上下文——这正好是你项目里最缺的一环。

📺 [打开原文](https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors)

---

### 4. 中国用 DUV 多重曝光摸到 5nm 级，代价是更大的 die、更低的良率、更长的周期

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Chris Stokel-Walker_

Tom's Hardware 梳理了一条被低估的技术路径：中国把老一代 DUV 光刻的多重曝光推到极限，已经接近 5nm 级。但代价明确——die 面积变大、良率下降、制造周期拉长。这不是'突破封锁'的爽文，而是一份成本账单，而且账单还在涨。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DUV 多重曝光已能逼近 5nm 级制程 | '5nm 级'的具体定义与实测参数未公开 |
| 代价包括 die 面积增大、良率下降、制造时间延长 | 良率数字没有第三方验证 |
| 专家判断继续微缩的成本曲线会持续恶化 | 该路径在多少层以上会撞到物理与经济双重天花板，尚无共识 |
| 同期 ASML 称 2026 年在欧洲销售额为零 | 对国内 AI 芯片实际供给量的影响，短期内难以量化 |

**📖 主编点评**

你是电子信息工程背景，这条值得精读——多重曝光的成本结构是理解'为什么 EUV 是分水岭'的最好切口。面试聊到制程时，能讲清 die size、良率、周期三者的权衡，比背参数有说服力得多。

📺 [打开原文](https://www.tomshardware.com/tech-industry/semiconductors/china-can-make-advanced-chips-without-euv-but-the-bill-keeps-growing-duv-multiple-patterning-means-bigger-dies-lower-yields-and-longer-manufacturing-times)

---

## 📋 备选阅读

- [GPU-unlock：解锁 Nvidia 30 系显卡的 FP/BF16 指令发射率](https://github.com/Zagitta/gpu-unlock) —— HN 235 分，逆向解锁消费卡的半精度指令发射限制，硬件层面的工程细节很硬，但离你的产品方向较远。
  _fragebogen_
- [泄露视频：中国工厂规模化拆解 RTX 5090 供 AI 服务器](https://www.tomshardware.com/pc-components/gpus/leaked-video-exposes-how-chinese-factories-are-stripping-rtx-5090s-to-fuel-ai-custom-partner-cards-to-nvidia-founders-editions-on-the-chopping-block) —— 解释了 5090 为何一卡难求，是算力紧缺最直观的物证，但属于现象报道而非趋势分析。
  _Zhiye Liu_
- [Arm 就 Qualcomm 陪审团裁决表态：2 美元赔偿背后的合规测试控制权](https://www.eetimes.com/two-dollars-and-a-test-suite/) —— 赔偿只有 2 美元，真正的争点是自定义芯片出货前必须通过的合规测试由谁掌控，这个角度比裁决本身重要。
  _Moshe Zalcberg_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
