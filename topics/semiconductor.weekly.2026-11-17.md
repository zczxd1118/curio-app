# Curio · AI 算力 / 半导体 · 2026-11-17

> 今日 1 条头条 + 5 条备选

_今天全网只有一个真信号：Nvidia 的权力真空。Jensen Huang 因丑闻即刻辞职，董事会另设国家安全委员会、Arm 的 Rene Haas 被接触、Huang 又在谈回归，同时美国商务部收紧远程算力出口管制。另一条线是 Anthropic IPO 的信用面——$1.4T 目标估值对上垃圾级评级，AI 泡沫的定价权正在从叙事转向债市。_

---

## 🌟 今日精选

### 2. 美国 BIS 新规堵住「云租算力」漏洞：出口管制的对象从芯片变成算力本身

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Oliver Haslam_

BIS 发布临时最终规则，要求企业若可能向中国等受限国家提供算力，出口 AI 芯片需先取得许可，明确针对通过海外数据中心远程调用绕开实体出口管制的做法。这是管制逻辑的一次换轨：过去管的是硬件过境，现在管的是算力可达性。对做推理部署和跨境 API 的人来说，这是基础设施层的规则变化。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| BIS 已发布 interim final rule，将远程访问纳入出口管制范围 | 具体执行口径（如何判定「可能提供算力」）尚未明确，合规成本可能被低估 |
| 规则要求对可能向中国提供算力的芯片出口申请许可证 | 对已建成海外集群的中国公司实际封堵效果存疑，取证难度大 |
| NPR 与 Tom's Hardware 均确认此举是对 Nvidia 事件的直接政策回应 | 是否会波及第三国云厂商的转售业务，目前无明确豁免条款 |
| 该规则与 Nvidia 董事会新设的出口管制监督委员会同期出现 | 政策是否会在 Nvidia 新 CEO 落定后调整，存在变数 |

**📖 主编点评**

如果你在评估任何跨境推理方案（海外 API、海外 GPU 租用），现在要把「合规可持续性」当成和延迟、价格同级的选型维度。具体动作：查一遍你依赖的推理服务商的机房所在地与实体归属，别等到限流那天才发现链路在管制清单上。

---

## 📋 备选阅读

- [Nvidia 被指通过投资 AI 初创、再让它们回购 GPU 来人为制造稀缺](https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus) —— 1112 分的指控性报道，与 Anthropic 的 $900B 承诺互为注脚，但证据链仍是「allegedly」，放备选。
  _speckx_
- [Nvidia 在 Supercomputing 2026 发布 Rubin HPC GPU，5 万+ CUDA 核心，2028 到货](https://www.tomshardware.com/pc-components/gpus/nvidia-announces-rubin-hpc-gpu-with-record-number-of-cuda-cores-at-supercomputing-2026-new-chip-accelerates-agentic-hpc-workloads-arrives-in-2028) —— 路线图本身是硬事实，但 2028 太远，且现在由临时 CEO 背书，可信度打折。
  _Jeffrey Kampman_
- [哈佛研究：403 个美国超大规模数据中心一年耗电 82 TWh，超密歇根全州 80%](https://www.tomshardware.com/tech-industry/data-centers/403-hyperscale-us-data-centers-used-staggering-82-terawatts-of-electricity-in-a-year-more-than-80-percent-of-michigans-entire-consumption-generated-26-million-tons-of-co2-in-a-single-year-gas-and-coal-supplied-54-percent-of-the-power-harvard-led-study-estimates) —— Nature Sustainability 上的硬数据，54% 电力来自煤和气，是 AI 成本叙事里最容易被忽略的一项。
  _Shane Downing_
- [TSMC 向 SEC 提交文件披露遭黑客入侵](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000800/a20261112statementregardin.htm) —— 一手监管文件，但披露内容极简，影响面待评估，先记一笔。
  _gmays_
- [Nvidia DGX 双机跑 GLM-5.3，vLLM 下达到 607.8 tok/s](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/) —— 有具体吞吐数字和 vLLM 配置的工程文，符合你的偏好，但属于官方博客的软性内容。
  _wondersky_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
