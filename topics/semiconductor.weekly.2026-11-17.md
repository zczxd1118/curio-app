# Curio · AI 算力 / 半导体 · 2026-11-17

> 今日 2 条头条 + 4 条备选

_今天最重要的信号只有一个：Nvidia 的权力真空已经从八卦变成产业事件——黄仁勋辞职、董事会设国家安全委员会、美国收紧远程算力出口、Anthropic 以 1.4 万亿美元估值推进 IPO 同时被质疑信用评级。第二条线是 AI Agent 开始产生法律后果：加州总检察长起诉 OpenAI 的越界 Agent，Apple 在 macOS 27.3 加权限闸门。你该把注意力从"模型发布"挪到"谁为 Agent 行为负责"。_

---

## 🌟 今日精选

### 1. 黄仁勋即刻辞任 Nvidia CEO，4055 分登顶 HN：一次绯闻如何演变成 4 万亿美元公司的治理危机

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _lldb_

11 月 12 日黄仁勋即刻辞任，导火索是与直接下属的关系及新加坡 Megaspeed 相关的对华走私调查。董事会随后设立国家安全与出口管制监督委员会，临时 CEO 由 CFO Colette Kress 接手，周二财报成为她职业生涯最大的一天。这不是一次普通换帅，而是把 Nvidia 的出口合规风险从法务部推到了董事会层面。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 黄仁勋于 2026-11-12 即刻辞任 Nvidia CEO，结束 33 年任期 | "绯闻导致辞职"与"走私调查导致辞职"的因果顺序尚未被独立证实，多数为匿名信源 |
| 董事会新设国家安全与出口管制监督委员会，聘请外部法律与贸易合规专家 | 董事会称不考虑让黄仁勋回归，但 FT 报道其正与盟友讨论复出，两种说法互相矛盾 |
| 临时 CEO 为长期 CFO Colette Kress，Q3 财报定于本周二发布 | 1.5GW 走私芯片的规模数字来自分析师估算，非官方口径 |
| 报道称其与一名直接下属存在关系，新加坡 Megaspeed 公司被指涉对华 GPU 转运 | Kress 能否稳住大客户与供应链关系，要看周二财报电话会的措辞 |
| 美国 BIS 同期发布临时最终规则，限制通过远程访问绕开芯片出口管制 | Nvidia 长期护城河是否依赖黄仁勋个人，Stratechery 已给出悲观判断但缺乏数据支撑 |

**📖 主编点评**

你不需要关心绯闻细节，需要关心的是：Nvidia 的软件栈（CUDA、TensorRT-LLM、DGX 云）会不会因为治理动荡而放缓迭代。如果你在做推理部署选型，这周别急着锁定 Nvidia 专有栈，把 vLLM 这类可迁移层的抽象做厚一点，成本很低。

📺 [打开原文](https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f)

---

### 5. 哈佛研究：403 座美国超大规模数据中心一年耗电 82 TWh，超过密歇根州全州 80%，54% 来自煤电与气电

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Shane Downing_

发表在 Nature Sustainability 的哈佛主导研究给出迄今最细的一份账单：403 座美国超大规模数据中心年耗电约 82 TWh，占全美用电 2%，一年排放 2600 万吨 CO2，54% 电力来自天然气与煤。同期 Constellation Energy 在财报会上表示不担心民主党放缓数据中心建设。算力的环境成本正在从公关话题变成财务与监管变量。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 403 座美国超大规模数据中心年耗电约 82 TWh | 82 TWh 的统计口径是否包含自备电厂与备用容量未说明 |
| 相当于密歇根州全年用电量的 80% 以上，占全美约 2% | "超大规模"的界定标准会影响总量可比性 |
| 一年排放约 2600 万吨 CO2 | 各州后续的电价与碳约束政策走向不明 |
| 54% 电力来自天然气与煤炭 | 数据中心自建核电/绿电的替代速度尚无统一数据 |
| 研究由哈佛主导，发表于 Nature Sustainability | AI 训练与推理的耗电拆分仍缺公开数据 |

**📖 主编点评**

这条和你做推理优化直接挂钩：能耗正在变成可量化的成本项，也是可写进简历的优化目标。下次做模型部署实验时，顺手记录 tokens/s per watt，比只报延迟更有说服力。

---

## 📋 备选阅读

- [Nvidia 董事会设国家安全与出口管制监督委员会](https://www.tomshardware.com/tech-industry/policy/nvidia-board-establishes-national-security-and-export-control-oversight-committee-in-wake-of-jensen-huang-scandal) —— 今日发布，是头条 1 的治理侧补充。信息量小于主事件，放备选避免重复。
  _Jowi Morales_
- [美国新规限制中国企业远程访问 AI 服务器与算力基础设施](https://www.tomshardware.com/tech-industry/artificial-intelligence/new-us-rules-aim-to-restrict-remote-access-to-ai-servers-and-infrastructure-seeks-to-combat-cloud-rental-workarounds-to-gpu-export-controls) —— BIS 临时最终规则，堵云租用绕道。对国内做推理部署的人是硬约束，值得单独知道。
  _Oliver Haslam_
- [Nvidia 发布 Rubin HPC GPU：5 万+ CUDA 核心，2028 年到货](https://www.tomshardware.com/pc-components/gpus/nvidia-announces-rubin-hpc-gpu-with-record-number-of-cuda-cores-at-supercomputing-2026-new-chip-accelerates-agentic-hpc-workloads-arrives-in-2028) —— SC26 发布，主打 agentic HPC 负载。时间线到 2028，对当下选型影响有限。
  _Jeffrey Kampman_
- [AMD 拿下新 TOP500 榜单 40%+ 份额，同比涨 14%](https://www.tomshardware.com/tech-industry/supercomputers/amd-grabs-over-40-percent-of-new-top500-list-for-supercomputers-up-14-percent-since-last-year-new-lux-system-developed-between-amd-and-doe-debuts-at-no-14-with-epyc-cpus-and-instinct-mi355x-gpus) —— Lux 系统首秀第 14 名，AMD 与 DOE 的 10 亿美元合作落地。硬件格局的慢变量。
  _Jake Roach_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
