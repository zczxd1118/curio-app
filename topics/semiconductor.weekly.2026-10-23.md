# Curio · AI 算力 / 半导体 · 2026-10-23

> 今日 2 条头条 + 4 条备选

_今天最硬的信号有两个：一是 OpenAI 传出以 1.25 万亿美元估值再融 300 亿美元、抢在 IPO 前落袋，AI 资本周期进入「自我加杠杆」阶段；二是 Google TPU 首次外销并跑进 Meta 数据中心，Nvidia 的算力垄断第一次出现真实裂缝。半导体侧，TSMC 开始要求设备商去中国稀土磁体，供应链脱钩从口号变成采购条款。_

---

## 🌟 今日精选

### 2. Google TPU 首次外销并进入 Meta 数据中心，Nvidia 的算力垄断出现第一道裂缝

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

Google 的 TPU 第一次卖给外部客户，且已经跑在 Meta 的生产环境里，配套的是能在芯片上原生执行 PyTorch 模型的开源引擎。这件事的分量不在「Meta 省了多少钱」，而在于 CUDA 之外第一次出现了有真实超大规模负载背书的第二套栈。对做推理部署的人来说，硬件层的可选项从 1 变成了 2。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| TPU 首次对外销售，Meta 数据中心已承载生产级 AI 负载 | Meta 采购的具体规模、是租用还是买断，报道未给出数字 |
| 配套开源引擎支持 PyTorch 模型在 TPU 上原生运行，不依赖 XLA 重写 | 「原生 PyTorch」的实际性能损耗与算子覆盖率尚不清楚，可能仍是长尾算子回退 |
| 此前 TPU 仅服务 Google 内部与 Google Cloud 租用客户 | 这是否会引发 AWS/Azure 跟进采购第三方加速器，属于推测 |
| Nvidia 目前仍占据 AI 加速器绝大部分份额 | 对 Nvidia 定价权的实际冲击要等 2027 年产能数据才能验证 |

**📖 主编点评**

如果你以后要做推理优化或成本对比，现在值得把「非 CUDA 路径」纳入知识面：至少搞懂 PyTorch → 后端编译（XLA / TVM / Triton）这条链路的基本形状。面试里能讲清「为什么 TPU 难替代 CUDA 生态、以及这次为什么不一样」，比背 benchmark 数字有用得多。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/googles-tpus-for-ai-workloads-now-run-in-at-metas-data-centers-tpus-sold-to-external-customers-for-the-first-time-threaten-nvidias-market-dominance)

---

### 3. TSMC 要求设备供应商提供不含中国稀土磁体的机台，脱钩从政策口号变成采购条款

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

TSMC 正在要求设备商改用不含中国稀土永磁的电机与部件，理由是出口管制可能威胁产线运转。这是第一次由晶圆厂把「去中国稀土」写进设备采购要求——不是政府施压，而是企业自己在做供应链风险对冲。稀土这个长期被当作谈判筹码的品类，开始真实影响先进制程的成本结构。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| TSMC 已向设备供应商提出替代电机/无稀土部件的要求 | 替代方案的成本增幅与交期影响，目前没有量化数据 |
| 动因是中国稀土出口管制对晶圆厂运营构成潜在威胁 | 是否有设备商已具备量产级无稀土方案，尚不明确 |
| 稀土永磁广泛用于半导体设备的精密电机与传动部件 | 这是否会扩散到三星、Intel 等其它晶圆厂，属于趋势判断 |
| 中国在稀土开采与加工环节占主导地位 | 短期内更可能是双供应源并行而非彻底替换 |

**📖 主编点评**

这条对你做电子信息工程的背景是加分项：稀土磁体、精密电机、伺服控制这些是设备层的真实工程问题。如果你在找毕业设计或实习方向，「关键部件的国产替代可行性分析」这类题目既有产业热度又能落到具体器件参数上，比纯软件题目更容易讲出差异化。

📺 [打开原文](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-is-seeking-chipmaking-equipment-that-doesnt-contain-chinese-rare-earth-magnets-asks-suppliers-to-provide-alternative-motors-as-export-controls-threaten-fab-operations)

---

## 📋 备选阅读

- [Opus 5.5 agents discover two room-temperature magnetic semiconductor candidates](https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors) —— 用 Agent 做材料筛选并给出两个室温磁性半导体候选，方法学有意思，但结论未经实验验证，495 分说明社区在关注。
  _Hacker News_
- [Micron pulls the plug on future 4F² DRAM after two decades of research](https://www.tomshardware.com/pc-components/dram/micron-pulls-the-plug-on-future-4f2-dram-after-two-decades-of-research-in-dramatic-shift-company-says-architecture-offers-no-meaningful-density-advantages-increases-manufacturing-complexity-and-costs-and-has-fundamental-scaling-limitations) —— 美光放弃研究 20 年的 4F² DRAM 架构，理由是密度收益不抵成本，是存储路线选择的重要转向，但离你的日常较远。
  _Tom's Hardware_
- [AMD and Intel will work together to create a single PyTorch code path for AI inference on CPUs](https://www.tomshardware.com/pc-components/cpus/amd-and-intel-will-work-together-to-create-a-single-pytorch-code-path-for-ai-inference-on-cpus-amd-zendnn-library-gets-folded-into-intel-onednn-to-make-cpu-ai-simpler) —— ZenDNN 并入 oneDNN，两家死对头统一 CPU 推理路径，对做本地部署的人是实打实的减负，但短期只是工程整合。
  _Tom's Hardware_
- [FADU puts the filesystem inside the SSD's flash to bypass host CPUs](https://www.tomshardware.com/pc-components/ssds/fadu-puts-the-filesystem-inside-the-ssds-flash-to-bypass-host-cpus-file-semantic-pcie-6-0-ssd-delivers-460-000-ops-s-to-gpus-and-dpus-samples-due-by-q3-2027) —— 把 NFSv3 文件操作塞进 NVMe 命令，让 GPU 绕过主机文件系统直接读文件，架构很漂亮，但 2027 年才出样。
  _Tom's Hardware_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
