# Curio · AI 算力 / 半导体 · 2026-11-12

> 今日 2 条头条 + 4 条备选

_今天最重要的信号是 Nvidia 的治理危机：董事会据报准备罢免黄仁勋，股价自丑闻发酵以来已跌 20%，第二段婚外情与「中国间谍」指控叠加国会传唤。另一条是 AI 资本面的裂缝——OpenAI 单季营收首破 100 亿美元，但 Nasdaq 已跌入回调区间，AI 交易正在被重新定价。这两件事共同说明：算力叙事进入「人」与「钱」的检验期。_

---

## 🌟 今日精选

### 1. Nvidia 董事会据报准备罢免黄仁勋：第二段婚外情曝光，股价自丑闻以来已跌 20%

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

WSJ 与多家媒体在 11 月 11 日晚同步报道，Nvidia 董事会正就黄仁勋的去留召开紧急会议，最早周三晚可能做出决定。触发点是第二段婚外情——对象是向他直接汇报的 Nvidia 高管，此前他已承认与一名被指为中国情报人员的女性有染。公司 33 年来只有这一位 CEO，没有公开的继任方案。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| WSJ 首发报道董事会准备罢免黄仁勋，Tom's Hardware、TechCrunch、Ars Technica 同日跟进 | 「准备罢免」目前仍是匿名信源，董事会是否真投票、何时投票未确认 |
| 第二段婚外情对象为向其直接汇报的 Nvidia 高管，另有掩盖指控 | 黄仁勋是否会主动辞职或以其他方式留任，尚无任何一方表态 |
| 股价自丑闻爆发以来累计下跌约 20% | 继任者人选完全空白，TechCrunch 的名单只是媒体推测 |
| 美国众议院三个委员会主席要求黄仁勋出席闭门简报，否则可能发传票 | 对华出口与 Megaspeed 调查是否与此次治理危机直接挂钩，仍不明朗 |
| FBI 已介入调查，Nvidia 董事会同步调查间谍案 | 股价 20% 跌幅中有多少来自丑闻、多少来自大盘 AI 回调，无法拆分 |
| 黄仁勋任 CEO 已 33 年，公司无公开继任计划 |  |

**📖 主编点评**

你不需要关心八卦，但要关心治理风险如何传导到算力供给。Nvidia 一旦进入 CEO 过渡期，Rubin 出货节奏、对华政策口径、云厂商长约都可能被重新谈判。如果你在做任何依赖 GPU 成本假设的项目或判断，这周先把「Nvidia 供应稳定」从前提里拿掉，改成情景假设。

📺 [打开原文](https://www.tomshardware.com/pc-components/gpus/nvidias-board-reportedly-preparing-to-oust-ceo-jensen-huang-as-second-extra-marital-affair-emerges-stock-has-plunged-20-percent-since-scandals-began-huang-has-been-first-and-only-ceo-for-33-years)

---

### 5. Linux 内核内存管理审阅者因 AI 生成补丁泛滥辞职：「浪费的时间已经太多，而这只是开始」

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

一位 Linux 内核内存管理子系统的审阅者宣布卸任该职责，直接原因是 AI 生成的低质量补丁（AI slop）大量涌入。他的原话是「浪费在 AI slop 上的时间已经太多，而这只是这股提交量的开始」，叠加人力不足，只能退出。这是开源治理被 LLM 输出规模冲击的第一个高知名度案例。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Linux 内核内存管理子系统的审阅者因 AI 生成补丁泛滥卸任 | AI slop 补丁在总提交量中的占比没有量化数据 |
| 当事人称「浪费在 AI slop 上的时间已经太多，而这只是开始」 | 内核社区是否会引入 AI 生成内容标注或自动过滤机制，尚未讨论 |
| 人力不足是辞职的叠加因素 | 其他子系统是否出现同类退出，未提及 |
| Tom's Hardware 于 11 月 11 日报道 | 这是否会改变开源项目对 AI 辅助贡献的整体态度，属于推测 |

**📖 主编点评**

这条对你有两层用处。一是提醒：你用 Claude Code 生成代码提交 PR 时，审阅者的时间成本是真实的外部性，别把「能生成」当成「该提交」。二是它揭示了一个产品机会——AI 生成内容的过滤与质量门禁，正在从「nice to have」变成基础设施级需求，这可能是你 side project 值得切入的方向。

📺 [打开原文](https://www.tomshardware.com/software/linux/linux-kernel-reviewer-steps-down-from-memory-management-duties-due-to-influx-of-ai-slop-patches-the-amount-of-time-wasted-on-ai-slop-is-already-too-much-and-were-only-at-the-start-of-this-volume-of-submissions-and-low-manpower-forces-the-step-back)

---

## 📋 备选阅读

- [Nvidia Vera CPU 评测：2TB/s 内存带宽，真正的 x86 对手](https://www.storagereview.com/review/nvidia-vera-cpu-review) —— Vera CPU 的实测数据首次公开，2TB/s 带宽是硬指标。被黄仁勋丑闻淹没，但对理解 Nvidia 从 GPU 走向整机架的战略很关键。
  _StorageReview / HN_
- [AMD Venice-X 最高 5.3GHz，3D V-Cache 四年后回归数据中心](https://www.tomshardware.com/pc-components/cpus/amds-venice-x-maxes-out-family-at-5-3-ghz-returning-3d-v-cache-to-data-center-after-four-years-chips-target-hpc-workloads-with-pcie-6-0-and-1-6-tb-s-memory-bandwidth) —— 2027 下半年上市，PCIe 6.0 + 1.6TB/s 带宽。是 AMD 对 Nvidia Vera 的正面回应，时间线偏远所以放备选。
  _Tom's Hardware_
- [AMD 用 MEXT 技术在半数 DRAM 下保住 95% 服务器性能](https://www.tomshardware.com/pc-components/cpus/amd-shares-how-it-can-retain-95-percent-of-server-performance-with-just-half-the-dram-sidestepping-memory-shortages-with-mext-tech-powers-over-100-servers-already-running-with-plans-to-expand-to-2-000-servers-in-2027) —— 已有 100+ 台服务器在跑，2027 扩到 2000 台。内存短缺背景下的实用工程方案，数字扎实，但受众偏基础设施。
  _Tom's Hardware_
- [Linux 桌面 OS Kora 把 AI 模型拆分到 CPU/GPU/NPU 上跑](https://www.tomshardware.com/software/linux/cyanogen-co-founder-unveils-kora-a-linux-os-that-splits-ai-models-across-the-cpu-gpu-and-npu-snapdragon-x2-elite-and-hexagon-npu-get-full-support-first) —— Cyanogen 联合创始人新项目，2027 上 PC，首发支持 Snapdragon X2 Elite。本地推理的异构调度思路有意思，但离落地还远。
  _Tom's Hardware_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
