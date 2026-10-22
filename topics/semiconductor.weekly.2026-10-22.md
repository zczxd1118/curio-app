# Curio · AI 算力 / 半导体 · 2026-10-22

> 今日 1 条头条 + 4 条备选

_今天最重要的信号有两个：一是 AI 发现漏洞的能力第一次以「互联网级事故」的形式落地——PHP 核心两个未认证 RCE 由 OpenAI 与 Google Wiz 用 AI 挖出，4chan、Wikipedia、DeviantArt 同日中招；二是资本端开始给 AI 建设降温定价，Anthropic S-1 与估值缩水、Firmus IPO 48 小时崩盘、数据中心股集体下挫，叙事从「无限扩张」转向「谁来付账」。工程侧值得你留意的第三条线：Claude 工程负责人公开说「别再用 2024 年的方式用 Claude」，这是对你日常 Agent 工作流最直接的一次校准。_

---

## 🌟 今日精选

### 4. AMD 与 Intel 联手：ZenDNN 并入 oneDNN，CPU 推理统一成一条 PyTorch 路径

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

10 月 21 日，AMD 与 Intel 宣布把 AMD 的 ZenDNN 库并入 Intel 主导的 oneDNN，目标是让 PyTorch 在 CPU 上的推理优化收敛到单一代码路径。这是两家在 x86 上罕见的工程级合作，直接后果是开发者不必再为两家 CPU 分别调优。对做本地推理和边缘部署的人来说，这是一次实打实的复杂度下降。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| AMD 的 ZenDNN 将被折叠进 Intel 的 oneDNN 库 | 统一后的性能是否对两家对称，尚无第三方 benchmark |
| 目标是形成统一的 PyTorch CPU 推理代码路径 | 合并的时间表与首个稳定版本未公布 |
| 消息由 Tom's Hardware 于 10 月 21 日报道 | 是否会影响其他框架（如 ONNX Runtime）的后端策略，未提及 |

**📖 主编点评**

如果你在本地跑小模型做 Agent 的子任务（分类、抽取、路由），这条意味着未来「一份代码两家 CPU 都能跑好」会变成默认。短期不用改代码，但值得在你的项目 README 里记一笔：CPU 推理的碎片化正在收敛，选型时不必再为 AMD/Intel 分别留后手。这也是半导体域今天最像「工程事实」而非「产业口水」的一条。

📺 [打开原文](https://www.tomshardware.com/pc-components/cpus/amd-and-intel-will-work-together-to-create-a-single-pytorch-code-path-for-ai-inference-on-cpus-amd-zendnn-library-gets-folded-into-intel-onednn-to-make-cpu-ai-simpler)

---

## 📋 备选阅读

- [Nvidia Vera CPU 在 Modal 实测吞吐是 Intel/AMD 的两倍](https://www.tomshardware.com/pc-components/cpus/nvidia-vera-cpu-deployed-at-ai-startup-modal-alongside-existing-x86-fleet-internal-testing-showed-2x-throughput-compared-to-amd-and-intel) —— Agent 负载下 2x 吞吐是厂商自测口径，但方向值得记：Agent 推理的 CPU 侧正在被重新设计。
  _Tom's Hardware_
- [中国三家大厂下单 350 亿美元 Nvidia RTX Pro 5500，仅 10% 可交付](https://www.tomshardware.com/pc-components/gpus/chinas-tech-giants-drop-usd35-billion-on-export-compliant-nvidia-rtx-pro-5500-workstation-gpu-orders-to-power-ai-ambitions-according-to-reports-bytedance-alibaba-and-tencent-order-3-million-cards-despite-warnings-that-only-10-percent-of-orders-are-fulfillable) —— 字节、阿里、腾讯合计 300 万张卡的需求，交付率仅一成——供需缺口的量级比新闻标题更有信息量。
  _Tom's Hardware_
- [美国重启三座核反应堆为 AI 数据中心供电，已上线 2.25GW](https://www.tomshardware.com/tech-industry/big-tech/us-takes-unprecedented-step-of-recommissioning-nuclear-plants-due-to-ai-power-demand-2-25-gw-currently-on-tap-from-refurbished-reactors) —— 电力成了 AI 建设的硬约束，重启核电站是最直白的证据；但离你的日常较远。
  _Tom's Hardware_
- [Chris Lattner：AI 代码生成解决不了软件工程](https://www.eetimes.com/chris-lattner-ai-code-generation-doesnt-solve-software-engineering/) —— LLVM 作者的观点，与第 2 条形成互补；但摘要太薄，需读原文才好评判。
  _EE Times_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
