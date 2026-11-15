# Curio · AI 算力 / 半导体 · 2026-11-15

> 今日 1 条头条 + 3 条备选

_今天只有一个真信号：黄仁勋因丑闻即刻辞任 Nvidia CEO，董事会已接触 Arm CEO Rene Haas，员工请愿、马斯克联署、亚洲政府表态、AI 初创融资预期下修全在同一周发生。第二条线是 Anthropic IPO 被信用评级机构按"高收益债"定价，1.4T 估值与"垃圾级"同时出现，说明这轮 AI 资本周期开始被当成信用事件而非成长故事来审。_

---

## 🌟 今日精选

### 4. 研究者称通过权重统计分析判定 DeepSeek、Kimi 用了被禁的 Nvidia Blackwell 训练

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Bruno Ferreira_

一项新研究用模型权重的统计特征反推训练硬件，称 DeepSeek、Kimi 等中国模型的权重与 Nvidia Blackwell 高度相关，即使用了受出口管制的芯片。方法本身比结论更值得看：它把"你用了什么卡"从供应链审计问题变成了可以从公开权重推断的技术问题。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Tom's Hardware 报道该研究对多个中国开源模型的权重做了统计分析 | 权重统计能否可靠区分 Blackwell 与 Hopper，学界尚无同行评审共识 |
| 结论指向与 Nvidia Blackwell 硬件的高相关性 | 相关性不等于因果，也可能来自蒸馏或微调路径的间接痕迹 |
| 同期马来西亚、新加坡加强了对 Nvidia AI 芯片转运的调查，新加坡已就 917 台服务器起诉一名中国籍高管 | 这一结论若被监管采信，会改变开源模型发布的风险评估方式 |
|  | 对国内开发者使用这些开源权重是否有合规风险，目前无明确说法 |
|  | 研究方法是否可复现，取决于是否放出代码与数据集 |

**📖 主编点评**

你做模型评测相关的内容时，可以关注这类"从产物反推过程"的方法论——它和 RAG 里做来源归因是同一类思路。如果代码开源，值得跑一遍看看结论稳不稳，这比转述结论有价值得多。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/researchers-allege-deepseek-kimi-and-other-chinese-ai-models-were-trained-on-export-controlled-nvidia-blackwell-chips-statistical-analysis-on-model-weights-reveals-high-correlation-to-nvidia-hardware)

---

## 📋 备选阅读

- [两台 DGX Station 跑 GLM-5.3，vLLM 下达到 607.8 tok/s](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/) —— Nvidia 官方博客的部署细节，有具体吞吐数字和 vLLM 配置，属于你要的工程实践类内容。
  _wondersky_
- [律师用 8 张 V100 把 DeepSeek V4.1 Flash 从 2-bit 提到接近 NVFP4 精度](https://www.tomshardware.com/tech-industry/artificial-intelligence/lawyer-upgrades-eight-v100-private-ai-server-to-run-80-percent-of-deepseek-v4-1-flash-at-4-bit-nvfp4-precision-adds-1tb-of-ram-an-nvidia-rtx-3090-and-fixes-crashes-caused-by-a-bad-psu) —— 个人自建推理服务器的真实调优记录，含加内存、换电源、精度取舍，比教程有信息量。
  _Shane Downing_
- [Nvidia RTX Spark 加密固件把 Linux 上的推理速度压到 35%](https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop) —— 如果你考虑用消费级卡做本地推理，这条是反面教材：固件层的限制可能直接砍掉三分之二性能。
  _novaRom_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
