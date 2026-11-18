# Curio · AI 算力 / 半导体 · 2026-11-18

> 今日 2 条头条 + 4 条备选

_今天真正的信号只有一个：Nvidia 的权力交接已经落地成事实——董事会明确表态不打算让 Jensen Huang 回归，同时公司宣布退出中国市场、继续推进收购 Hugging Face、并给出继续增长的营收指引。围绕这条主线，Anthropic IPO 的信用评级与估值争议、以及 AI 资本市场的整体回撤，是第二层信号。AI 编程工具侧今天没有硬新闻，候选池里多是教程存量，我按你的口味只挑了有工程细节的。_

---

## 🌟 今日精选

### 1. Jensen Huang 出局时间线整理：从董事会到国会听证，Nvidia 的权力真空已经成型

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Jowi Morales_

过去一周 Nvidia 的新闻密度是产业级的：11 月 12 日 Huang 辞职生效，董事会全票接受；11 月 17 日财报电话会上新任董事长 Harvey Jones 明确表示不打算让他回来；同期公司宣布不再向中国销售芯片、确认收购 Hugging Face 的意向不变、并给出继续创纪录的营收指引。这不是一次普通的 CEO 更替，而是全球 AI 算力最大供应商在需求最紧的时刻换掉了决策核心。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 11 月 12 日 Jensen Huang 辞去 Nvidia CEO 职务，董事会全票接受，CFO Colette Kress 出任临时 CEO | 「停止对华销售」是永久战略还是过渡期表态，公司未给出时间表与收入影响量化 |
| 11 月 17 日财报电话会上，董事长 Harvey Jones 表示董事会不打算恢复 Huang 的 CEO 职位 | Hugging Face 收购在管理层动荡期能否走完监管与交割流程，尚无任何官方时间点 |
| 临时 CEO 确认 Nvidia 已停止向中国销售芯片，并重申开源 AI 战略与收购 Hugging Face 的计划不变 | Huang 与疑似中国间谍的关联指控目前只有媒体报道，国会听证前无法判断严重程度 |
| Huang 本人发表声明称若被允许回归将感到「荣幸」，但董事会层面已明确拒绝 | Nvidia 声称营收将继续创纪录，但这一指引建立在供应链与客户资本开支不变的前提上 |
| SEC 据 WSJ 报道已就相关事项对 Nvidia 展开调查，Huang 将于 12 月 1 日出席众议院外交事务委员会闭门听证 | Arm CEO Rene Haas 被接触接任的传闻未获任何一方确认 |

**📖 主编点评**

你不需要关心八卦，但要关心一件事：Nvidia 是当前所有 AI 产品（包括你用的 Claude、Gemini）的算力底座，决策层动荡会传导到 GPU 供给和云厂商定价。建议你把这条当成背景变量记着——如果未来两个月你看到推理 API 涨价或限流，回头查这条时间线。另外，Huang 12 月 1 日的国会听证是下一个明确的信息节点。

📺 [打开原文](https://www.tomshardware.com/tech-industry/the-downfall-of-jensen-huang-a-timeline-of-allegations-and-scandals-that-brought-down-the-king-of-ai-infrastructure)

---

### 4. Nvidia 在 SC26 称 Vera CPU 靠软件优化还能再涨 39%，Olympus 自研核尚未吃满

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Anton Shilov_

SC26 上 Nvidia 给出的数字是：Vera CPU（基于自研 Olympus Arm 核）在未优化代码下性能已经不错，但通过软件优化还能再提升最多 39%。这条的价值在于它暴露了一个工程事实——自研核的微架构调优还没做完，性能上限取决于编译器与运行时而非硅片本身。对做推理部署的人来说，这是「同一块硬件，不同软件栈差距有多大」的又一个例证。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Nvidia 在 SC26 展示 Vera CPU，采用自研 Olympus Arm 核心 | 39% 是特定工作负载下的峰值还是普遍水平，官方未说明测试条件 |
| 官方称通过软件优化可获得最高 39% 的性能提升 | 优化需要改编译器还是只需改应用代码，决定了这个数字对普通开发者是否可达 |
| 当前性能是在未针对微架构优化的代码下测得的 | Vera 的量产时间与定价未公布 |
| 同场还有 GLM-5.3 在两台 DGX Station 上用 vLLM 跑到 607.8 tok/s 的部署案例 |  |

**📖 主编点评**

如果你以后要做推理优化方向，这条给的是一个可复用的判断：性能瓶颈经常在软件栈而不是硬件。那个 607.8 tok/s 的 vLLM 部署案例更值得你点进去看——它给了具体的双 DGX Station 配置，属于你要的「具体到配置」的工程细节。

📺 [打开原文](https://www.tomshardware.com/pc-components/cpus/nvidia-claims-its-vera-cpu-can-gain-up-to-39-percent-performance-boost-via-software-optimization-at-sc26-architectural-fine-tuning-is-needed-to-fully-unleash-custom-olympus-cores)

---

## 📋 备选阅读

- [Nvidia 员工警告：若不恢复 Huang，不可替代的人才将流失](https://www.tomshardware.com/tech-industry/big-tech/nvidia-employee-warns-of-irreplaceable-talent-exodus-if-jensen-huang-not-reinstated-cautions-board-and-top-brass-that-talent-at-nvidia-is-now-contemplating-departing) —— 内部信警告董事会「不可替代的人才」可能出走。是头条时间线的补充证据，单独看信息量不足以成头条。
  _Jhet Borja_
- [中国威胁就新的 AI GPU 租赁与出口限制采取反制措施](https://www.tomshardware.com/pc-components/gpus/china-threatens-countermeasures-on-the-face-of-new-ai-gpu-rental-and-export-restrictions-beijing-threatens-retaliation-ahead-of-thursdays-xi-jinping-meeting-sino-american-trade-war-may-be-renewed-for-a-new-season) —— 今天上午发布，针对 Blackwell 租赁与出口新限制。与 Nvidia 退出中国是同一条链上的另一端，值得跟进但尚无具体措施。
  _Bruno Ferreira_
- [Nvidia 停止披露新加坡销售额，营收达到 1040 亿美元](https://www.ft.com/content/dbde7a30-548c-4f9d-a4be-7898a0c24dcf) —— 新加坡销售额消失与 Megaspeed 的疑点相关，是理解 Nvidia 收入真实构成的线索，但需要配合其他报道读。
  _louiereederson_
- [Marc Hijink 谈 ASML 的文化、供应链与地缘政治](https://www.eetimes.com/marc-hijink-on-asmls-culture-supply-chain-and-geopolitics/) —— 关于 ASML 的 EUV 主导地位与地缘压力的深度访谈。符合你要的访谈类长内容，但与今日主线关联较弱。
  _Nitin Dahad_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
