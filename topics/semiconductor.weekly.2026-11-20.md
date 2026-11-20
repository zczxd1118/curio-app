# Curio · AI 算力 / 半导体 · 2026-11-20

> 今日 2 条头条 + 3 条备选

_今天最重要的两个信号：一是 Anthropic 以 $83 定价、开盘 $111（+33%）登陆纳斯达克，估值约 $1.5T，AI 的"循环融资"第一次被公开市场定价；二是 Nvidia 在黄仁勋辞职后由临时 CEO 交出 $115.8B 季度营收，业绩没塌但治理真空叠加芯片走私、新加坡销售停披露，风险在累积。这两件事合起来说明：AI 资本叙事进入"兑现期"，接下来看的是现金流而不是故事。_

---

## 🌟 今日精选

### 2. Nvidia 临时 CEO 交出 $115.8B 季度营收，业绩没塌但治理真空叠加走私与新加坡停披露

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _EE Times_

黄仁勋因丑闻辞职后，临时 CEO Colette Kress 主持了首个财报：季度营收 $115.8B，AI 基础设施需求仍在托底。但同期公司停止披露新加坡销售额、高管家属卷入芯片走私案、董事在丑闻前抛售近 $10 亿股票，治理层面的裂缝比业绩更值得盯。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 临时 CEO Colette Kress 主持财报，季度营收 $115.8B | $115.8B 是否可持续，取决于下季度 AI 资本开支是否放缓 |
| AI 基础设施需求仍是营收主引擎，利润维持 | 新加坡销售停披露是否与 Megaspeed 相关的转口贸易有关，尚无定论 |
| 公司已停止披露新加坡地区销售额 | 董事会明确表示不打算让黄仁勋回归，但员工请愿要求其回归，内部张力未解 |
| 一名高级副总裁的妻子被卷入 AI 芯片走私案 | Arm CEO Rene Haas 被接触接任，最终人选未定 |
| 一名董事在丑闻曝光前数周抛售近 $10 亿股票 |  |

**📖 主编点评**

如果你在做 AI 产品，短期不用慌——算力供给和价格没变。但要开始关注"治理风险如何传导到供应链"：出口管制收紧、转口贸易被查，都可能让某些型号的交付周期变长。给你的 Agent 项目留一条备用推理通道（比如本地小模型兜底）是低成本保险。

📺 [打开原文](https://www.eetimes.com/nvidia-reports-115-8b-in-quarterly-revenue-under-interim-ceo/)

---

### 4. OpenAI 帮 AMD 把旗舰 GPU 设计 PPA 提升 14%，GPT 模型也在帮苏姿丰优化新 CPU

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

OpenAI 用模型参与 AMD 下一代旗舰 GPU 的设计优化，PPA（性能/功耗/面积）提升 14%，同样的方法也用在了新 CPU 上。这是"AI 设计芯片"从论文走进真实产品线的标志性案例——不是概念演示，是进了流片前的设计流程。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| OpenAI 协助 AMD 优化下一代旗舰 GPU 设计，PPA 提升 14% | 14% PPA 提升的具体测试条件与可复现性未公开 |
| GPT 模型同样用于 AMD 新 CPU 的设计优化 | AI 参与设计后，最终芯片的良率与量产表现仍待验证 |
| 优化发生在设计阶段，非后期调优 | 这种合作是否会被复制到其他芯片厂商，尚无迹象 |

**📖 主编点评**

这条对你这个电子信息工程背景的人是硬信号：AI for chip design 不再是玄学，已经进了真实 PPA 指标。如果你简历上想加一个差异化亮点，"用 LLM 辅助某个电路/布局优化的小实验"比再刷一个 Agent demo 更稀缺。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-helped-amd-improve-its-upcoming-flagship-gpu-design-by-14-percent-ppa-gpt-models-also-helping-lisa-sus-outfit-boost-its-new-cpus)

---

## 📋 备选阅读

- [Serving GLM-5.3 at 607.8 tok/s across two Nvidia DGX stations with vLLM](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/) —— 双 DGX + vLLM 跑到 607.8 tok/s 的部署细节，命中你"推理优化"偏好。偏 infra，头条位让给了更宏观的芯片新闻。
  _NVIDIA Developer_
- [AI 数据中心电力需求到 2030 年翻倍，$4 万亿投入相当于多出一个英国的用电量](https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-power-demand-will-double-by-2030-thanks-to-usd4-trillion-in-spending-adding-an-entire-great-britain-to-energy-strain-93-large-ai-factories-with-projected-capacity-of-around-50-gigawatts) —— IEA 报告：93 座大型 AI 工厂、约 50GW 新增容量。数字硬，是理解算力长期约束的好材料。
  _Tom's Hardware_
- [TSMC 遭黑客攻击（SEC 8-K 披露）](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000800/a20261112statementregardin.htm) —— 官方 8-K 文件，事实确凿但细节少。和支付泄露同属本周安全主题，放备选。
  _SEC / Hacker News_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
