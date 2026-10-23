# Curio · AI 算力 / 半导体 · 2026-10-23

> 今日 2 条头条 + 4 条备选

_今天最值得盯的两条线：一是资本端开始给 AI 叙事重新定价——Anthropic 估值从高点回落 500B、Firmus 的 300 亿美元 IPO 两天内崩掉、亚洲芯片股与数据中心股同步下挫，而 OpenAI 反手在 IPO 前谈 1.25 万亿美元估值的新一轮 300 亿美元融资；二是算力供给端出现结构性位移——Google TPU 首次外销并跑进 Meta 机房。工程侧则有一个你会直接用到的东西：1Password 让 Agent 代登录而不暴露密码。_

---

## 🌟 今日精选

### 2. Google TPU 首次对外销售并跑进 Meta 数据中心，靠开源引擎原生跑 PyTorch 模型

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

Google 第一次把 TPU 卖给外部客户，第一个大客户是 Meta，而且是在 Meta 的生产环境里跑 AI 负载。配套的是新的开源引擎，让 PyTorch 模型能原生跑在 TPU 上——这一步比卖芯片本身更重要，它把"换芯片"的成本从重写模型降到了改一个 backend。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Google TPU 首次向外部客户销售，Meta 已在生产环境使用 | Meta 采购的具体规模、是租用还是买断，未披露 |
| 配套发布开源引擎，支持 PyTorch 模型原生运行在 TPU 上 | "原生 PyTorch"的性能损失比例没有公开数据，实际可用性待验证 |
| 此前 TPU 基本只服务 Google 内部与 Google Cloud 租用场景 | 开源引擎的成熟度和社区维护力度尚不明朗 |
| Nvidia 目前在 AI 加速器市场占主导地位 | 是否会对 Nvidia 的定价形成实质压力，短期难判断 |

**📖 主编点评**

这条对你的直接价值在工程侧：如果 PyTorch 到 TPU 的迁移真的只是换个 backend，那"多硬件后端"会变成部署 Agent 推理时的常规操作。你现在做推理优化，值得花半小时读一下那个开源引擎的 repo，看它怎么处理算子覆盖和 fallback——这是未来一年最实用的技能之一。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/googles-tpus-for-ai-workloads-now-run-in-at-metas-data-centers-tpus-sold-to-external-customers-for-the-first-time-threaten-nvidias-market-dominance)

---

### 4. Arm v. Qualcomm 只判了 2 美元赔偿，真正的战场是谁控制芯片出厂前的合规测试套件

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _EE Times_

2 美元的赔偿金额是烟雾弹。EE Times 这篇把判决的真正含义挑明了：争议核心是"定制芯片出货前必须通过的那套合规测试"归谁控制。谁掌握测试套件，谁就掌握了架构授权之外的第二道闸门。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Arm 诉 Qualcomm 案判决中损害赔偿金额为 2 美元 | 判决对后续架构授权合同的具体约束力，需看完整判决书 |
| 案件核心争议涉及合规测试套件的控制权 | Qualcomm 是否会上诉、上诉后测试套件归属是否改变，未定 |
| 定制芯片在出货前需通过架构方的合规测试 | 其他架构授权方（如 RISC-V 生态）是否会效仿此模式，属推测 |
| 该测试环节直接影响芯片能否上市 | 对下游手机/PC 芯片出货节奏的实际影响，短期难以量化 |

**📖 主编点评**

你是电子信息工程背景，这条比大多数 AI 新闻更贴近你的专业底盘。它说明架构授权的护城河已经从"专利"挪到了"测试与认证流程"。如果你以后碰 IP 核、SoC 或嵌入式方向，理解这套合规测试链路，比多背两个协议标准更有差异化价值。

📺 [打开原文](https://www.eetimes.com/two-dollars-and-a-test-suite/)

---

## 📋 备选阅读

- [TSMC is seeking chipmaking equipment that doesn't contain Chinese rare-earth magnets](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-is-seeking-chipmaking-equipment-that-doesnt-contain-chinese-rare-earth-magnets-asks-suppliers-to-provide-alternative-motors-as-export-controls-threaten-fab-operations) —— TSMC 要求设备供应商提供不含中国稀土磁体的电机，出口管制正从芯片蔓延到设备零部件。供应链脱钩的又一实证。
  _Tom's Hardware_
- [Micron pulls the plug on future 4F² DRAM after two decades of research](https://www.tomshardware.com/pc-components/dram/micron-pulls-the-plug-on-future-4f2-dram-after-two-decades-of-research-in-dramatic-shift-company-says-architecture-offers-no-meaningful-density-advantages-increases-manufacturing-complexity-and-costs-and-has-fundamental-scaling-limitations) —— 美光放弃研究二十年的 4F² DRAM，理由是密度收益不足、成本反升。存储路线图的一次实质性转向。
  _Tom's Hardware_
- [AMD and Intel will work together to create a single PyTorch code path for AI inference on CPUs](https://www.tomshardware.com/pc-components/cpus/amd-and-intel-will-work-together-to-create-a-single-pytorch-code-path-for-ai-inference-on-cpus-amd-zendnn-library-gets-folded-into-intel-onednn-to-make-cpu-ai-simpler) —— ZenDNN 并入 oneDNN，两家在 CPU 推理上统一 PyTorch 路径。对做本地部署的人是好消息，但进展尚早。
  _Tom's Hardware_
- [FADU puts the filesystem inside the SSD's flash to bypass host CPUs](https://www.tomshardware.com/pc-components/ssds/fadu-puts-the-filesystem-inside-the-ssds-flash-to-bypass-host-cpus-file-semantic-pcie-6-0-ssd-delivers-460-000-ops-s-to-gpus-and-dpus-samples-due-by-q3-2027) —— 把 NFSv3 文件操作塞进 NVMe 命令，让 GPU/DPU 绕过主机文件系统直接读文件。架构很新，但要 2027 才有样品。
  _Tom's Hardware_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
