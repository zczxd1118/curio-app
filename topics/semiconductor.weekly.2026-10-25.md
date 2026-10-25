# Curio · AI 算力 / 半导体 · 2026-10-25

> 今日 2 条头条 + 5 条备选

_今天最值得看的两条信号：一是 OpenAI 宣布前沿模型不再吃「活的互联网」数据，训练数据供应链开始主动收缩；二是 AI 资本侧明显降温——Anthropic 估值被传缩水 5000 亿美元、数据中心类 IPO 接连折戟、10 年期美债收益率破 5.3%。算力与半导体侧则是另一条线：中国用 DUV 多重曝光硬撑 5nm 级，代价是良率与成本。_

---

## 🌟 今日精选

### 3. 中国用 DUV 多重曝光逼近 5nm 级，代价是更大 die、更低良率、更长工时

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

Tom's Hardware 梳理了中国在无 EUV 条件下把老一代 DUV 光刻推到极限的路径：靠多重曝光做到接近 5nm 级别。结论不是「做不出来」，而是「做得出来但账单越来越贵」——die 面积变大、良率下降、制造周期拉长，三重成本叠加。这是对「卡脖子」叙事的一次量化修正。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 中国厂商通过 DUV 多重曝光实现接近 5nm 级别的工艺 | 「5nm 级」是性能对标还是密度对标，报道口径偏模糊 |
| 代价包括 die 面积增大、良率下降、制造时间延长 | 实际量产良率数字未公开，成本差距难以精确量化 |
| 报道明确指出进一步微缩的成本曲线在恶化 | 这套路线能撑到几代之后，业内无共识 |
| ASML 同期表示 2026 年在欧洲「几乎没卖出任何设备」 | 对国产 AI 芯片实际供货能力的影响仍需观察 |

**📖 主编点评**

你做的是电子信息工程，这条值得存下来当工艺课的活案例：多重曝光的成本结构比「能不能做」更能说明产业现实。面试聊到国产替代时，讲清 trade-off 比喊口号有说服力得多。

📺 [打开原文](https://www.tomshardware.com/tech-industry/semiconductors/china-can-make-advanced-chips-without-euv-but-the-bill-keeps-growing-duv-multiple-patterning-means-bigger-dies-lower-yields-and-longer-manufacturing-times)

---

### 4. DeepSeek 4.1 Flash 1017：单任务成本再压低，适合 Agent 负载但幻觉率更高

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

DeepSeek 新版本把 cost-per-task 又往下压了一档，明确定位在 agentic workload——便宜、能跑工具调用链。代价写在标题里：相比闭源竞品更容易幻觉。这条对做 Agent 的人是直接的工程取舍题：省钱换准确率，值不值取决于你的任务能不能容忍重试。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DeepSeek 4.1 Flash 1017 为开放权重模型 | 具体成本数字与幻觉率对比基线未在摘要中给出 |
| 单任务成本进一步下降，主打 agentic 工作负载 | 「适合 agentic」是厂商定位还是第三方实测结论，需看原评测 |
| 评测显示其幻觉率高于闭源竞品 | 在长链路工具调用中的稳定性尚无公开数据 |
| 定位明确偏向低成本、高吞吐的 Agent 场景 | 对国内开发者可及性（API 稳定性、限流）未提及 |

**📖 主编点评**

如果你在 content-curator 里做多步 Agent 编排，可以拿它当「便宜的执行层」——让贵模型做规划、它做批量执行，再用校验步骤兜幻觉。这比单纯换模型更接近真实工程解法。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/deepseeks-latest-ai-model-is-smarter-than-ever-but-its-low-running-costs-come-at-a-price-open-weight-model-is-fit-for-agentic-workloads-but-is-more-prone-to-hallucination-than-proprietary-competitors)

---

## 📋 备选阅读

- [Opus 5.5 agents 发现两种室温磁性半导体候选材料](https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors) —— 用 Agent 做材料发现的具体案例，495 分讨论，但结论未经实验验证，先观察。
  _Hacker News_
- [ASML：2026 年在欧洲「什么都没卖出去」](https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand) —— 一句话把欧洲半导体产业空心化说透，配合中国 DUV 那条一起看更有意思。
  _Hacker News_
- [泄露视频：中国工厂成规模拆解 RTX 5090 供 AI 服务器](https://www.tomshardware.com/pc-components/gpus/leaked-video-exposes-how-chinese-factories-are-stripping-rtx-5090s-to-fuel-ai-custom-partner-cards-to-nvidia-founders-editions-on-the-chopping-block) —— 消费卡被拆成 AI 算力，是出口管制下的市场扭曲实证，画面感强。
  _Tom's Hardware_
- [GPU-unlock：解锁 Nvidia 30 系卡的 FP/BF16 指令发射率](https://github.com/Zagitta/gpu-unlock) —— 纯工程向的逆向与指令级优化，235 分，适合你这种想看底层的人。
  _Hacker News_
- [Arm 就 Qualcomm 陪审团裁决表态：2 美元赔偿背后的合规测试控制权](https://www.eetimes.com/two-dollars-and-a-test-suite/) —— 赔偿只有 2 美元，真正争的是定制芯片出厂前必须通过的合规测试归谁管。
  _EE Times_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
