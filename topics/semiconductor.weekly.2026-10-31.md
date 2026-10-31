# Curio · AI 算力 / 半导体 · 2026-10-31

> 今日 2 条头条 + 4 条备选

_今天最重要的信号有两个：一是 AI 资本叙事开始出现裂缝——Intel 一天蒸发 1 万亿美元半导体市值、Alphabet 单日市值缩水 5000 亿、Anthropic 被研究机构称为"年度最荒谬 IPO"，同时 TechCrunch 直指 AI 支出热潮出现裂痕；二是 Google 把 TPU 送上卫星并跑通 Gemma 4，算力开始离开地面。对做 Agent 的你来说，真正的可操作信息在工程侧：Cisco 让一个 27 岁工程师用无限 token 重写 98% 遗留代码，以及 Anthropic 官方 Cursor 扩展被植入后门近 12 小时。_

---

## 🌟 今日精选

### 2. Cisco 给一个 27 岁工程师无限 AI token，要求 24 个月重写 98% 遗留代码

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

Cisco 总裁 Jeetu Patel 把一件几乎不可能的事交给了一个 27 岁的前创业者：24 个月内用 AI 重写公司 98% 的遗留代码，token 不设上限。这是目前公开可见的最大规模"AI 重写存量系统"实验，也是对企业级 Agent 工作流最直接的一次压力测试。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Cisco 总裁 Jeetu Patel 直接任命该工程师，授权不限量 AI token 消耗 | 98% 这个数字大概率指代码行数覆盖率，而非业务逻辑等价性 |
| 目标是在 24 个月内重写公司 98% 的遗留代码 | 遗留系统重写的真正瓶颈在测试与回归验证，不在生成代码本身 |
| 被任命者为 27 岁，此前是创业者，非 Cisco 资深员工 | 若成功，会催生一批"AI 重写服务商"；若失败，会成为企业 AI 落地的反面教材 |
| Cisco 官方口径是让该工程师"放开手干"（go nuts） | Cisco 未披露如何验证重写后的系统正确性 |

**📖 主编点评**

这条对你的价值不在新闻本身，而在它暴露的工程问题：AI 重写存量代码时，验证成本远高于生成成本。你做 content-curator 时如果考虑让 Agent 改自己的代码库，先把测试和 diff 审查链路搭好——这正是简历上能讲清楚的"AI 工程实践"细节。

📺 [打开原文](https://www.tomshardware.com/tech-industry/big-tech/cisco-gives-27-year-old-engineer-unlimited-ai-tokens-to-rewrite-98-percent-of-the-companys-legacy-code-in-24-months-president-plucks-former-startup-founder-telling-him-to-go-nuts)

---

### 4. Tom's Hardware 发布首个 Agentic AI 的 CPU 基准测试：不涉及 GPU 的吞吐量测量

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

Tom's Hardware 用半年时间观察到 Agent 负载正在把 CPU 推回中心位置，于是做了第一个专门测 Agentic AI 的 CPU 基准。核心发现是 Agent 负载呈突发性，CPU 大量时间处于空闲，这直接挑战了"Agent 只需要 GPU"的直觉。Google 同期也提出 Agentic AI 会对数据中心 CPU 提出新需求。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Tom's Hardware 发布首个针对 agentic AI 工作负载的 CPU 基准测试方法 | 单一媒体的基准方法尚未经过社区复现，结论需谨慎对待 |
| 测试全程不涉及 GPU，只测 CPU 吞吐 | bursty 负载下真正的瓶颈可能是调度与内存带宽，而非核心数 |
| 结论是 Agent 负载呈 bursty 特征，CPU 频繁空闲 | 若结论成立，Agent 部署的成本模型会与纯推理服务显著不同 |
| Google 在 EE Times 上提出 agentic AI 将驱动数据中心 CPU 新需求 | 目前没有公开的 Agent 负载标准数据集 |
| 该基准基于过去六个月的实测数据构建 |  |

**📖 主编点评**

这条对你部署 content-curator 有直接参考价值：如果你打算把 Agent 常驻跑（定时抓取、增量总结），瓶颈很可能不在模型调用而在调度与 IO。可以拿这个基准思路自测一下你的 Agent 在空闲期的资源占用，把"低峰期批处理 + 事件触发"写进架构，这是能讲出 why 的工程细节。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/our-first-step-at-defining-a-cpu-benchmark-for-agentic-ai)

---

## 📋 备选阅读

- [Nvidia 官网悄悄下架 RTX 5080，零售价涨到 MSRP 的 2.2 倍](https://www.tomshardware.com/pc-components/gpus/nvidia-store-quietly-pulls-the-rtx-5080-following-rtx-5090-removal-street-prices-climb-to-2-2x-over-msrp) —— 消费级 GPU 被 AI 需求挤出的直接证据，如果你想升级本地跑模型的机器，现在不是好时机。
  _Tom's Hardware_
- [AI 需求引发 PCB 大缺货，订单排到 2030 年，交期拉到 30 个月](https://www.tomshardware.com/pc-components/ai-demand-triggers-massive-pcb-shortage-for-pc-makers-as-order-books-full-until-2030-lead-times-stretch-to-30-months-as-material-costs-surge-12x) —— 供应链最上游的卡点，比 GPU 更早反映真实需求强度，电子信息专业值得看。
  _Tom's Hardware_
- [Intel Fab 28 爆炸致两周停产，损失 6 亿美元，服务器芯片供货受扰半年](https://www.tomshardware.com/pc-components/cpus/deadly-intel-fab-28-explosion-causes-two-week-shutdown-to-cost-usd600-million-and-severely-disrupt-server-chip-manufacturing-for-six-months-10nm-xeon-shipments-stall-during-largest-shortage-in-memory) —— 叠加内存短缺，服务器 CPU 供给雪上加霜，是本周半导体最硬的实体事件。
  _Tom's Hardware_
- [PsiQuantum 把光子技术做成 AI 数据中心光交换，8x8 原型插损仅 1.2 dB](https://www.tomshardware.com/tech-industry/photonics/psiquantum-turns-its-photonics-know-how-into-an-optical-switch-for-supercharging-ai-data-center-gpu-networks-8x8-lab-prototype-loses-less-light-than-rivals-with-plans-to-develop-larger-devices) —— 光交换是 GPU 集群的下一个瓶颈解法，1.2 dB 对比行业 3 dB 上限，数字有说服力。
  _Tom's Hardware_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
