# Curio · 半导体 · 2026-10-22

> 今日 1 条头条 + 4 条备选

_今天最重要的信号有两个：一是 AI 发现漏洞的能力第一次以「PHP2Shell」这种形态砸到整个互联网头上——OpenAI 和 Google Wiz 找到的 PHP 核心未认证 RCE，4chan、Wikipedia、DeviantArt 当天中招，AI 攻防的双刃性从论文变成了运维事故。二是资本端开始给 AI 泡沫定价：Anthropic 估值被传缩水 5000 亿美元、Firmus 数据中心 IPO 48 小时崩盘、Meta 靠发新股给 AI 输血。工程侧则有一条值得你细读的：Claude 工程负责人说「别再用 2024 年的方式用 Claude」。_

---

## 🌟 今日精选

### 5. AMD 与 Intel 罕见联手：把 CPU 推理统一到一条 PyTorch 路径

**[半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

AMD 的 ZenDNN 库将被并入 Intel 的 oneDNN，两家要为 CPU 上的 AI 推理提供单一 PyTorch 代码路径。这是 x86 阵营面对 Nvidia 在推理侧扩张的一次防守性合作，对跑本地模型的人来说，意味着以后不用再为两家 CPU 分别调优。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| AMD ZenDNN 库将被折叠进 Intel oneDNN | 合并后的性能是否对两家都无损，尚无基准数据 |
| 目标是让 PyTorch 的 CPU 推理走统一代码路径 | 统一路径会不会牺牲各家专有指令集优化，需看实现 |
| 双方为直接竞争对手，此次为罕见工程层合作 | 对 ARM 阵营和 Apple Silicon 的影响，未涉及 |
|  | 落地时间表未公布 |

**📖 主编点评**

如果你在本地跑小模型做 RAG 或 Agent 的工具调用，这条意味着未来半年内 CPU 推理的踩坑成本会下降。现在别急着为某一家 CPU 写特化代码，等 oneDNN 统一路径出来再优化——你的 content-curator 如果要做本地 embedding，保持标准 PyTorch 接口就是最省事的策略。

📺 [打开原文](https://www.tomshardware.com/pc-components/cpus/amd-and-intel-will-work-together-to-create-a-single-pytorch-code-path-for-ai-inference-on-cpus-amd-zendnn-library-gets-folded-into-intel-onednn-to-make-cpu-ai-simpler)

---

## 📋 备选阅读

- [Nvidia 洽谈收购美国「开放」模型初创 Reflection AI](https://www.ft.com/content/052610c5-22b4-4dd4-932e-b7f9f0628b6a) —— 芯片公司直接买模型公司，垂直整合再进一步，但交易未定。
  _FT / HN_
- [中国三大厂下单 350 亿美元 Nvidia RTX Pro 5500， reportedly 仅 10% 可交付](https://www.tomshardware.com/pc-components/gpus/chinas-tech-giants-drop-usd35-billion-on-export-compliant-nvidia-rtx-pro-5500-workstation-gpu-orders-to-power-ai-ambitions-according-to-reports-bytedance-alibaba-and-tencent-order-3-million-cards-despite-warnings-that-only-10-percent-of-orders-are-fulfillable) —— 字节、阿里、腾讯合计 300 万张卡的需求，供需缺口本身就是信息。
  _Tom's Hardware_
- [Intel 亚利桑那 Fab 62 装机，确认 2028 年 High-NA EUV 量产](https://www.tomshardware.com/tech-industry/semiconductors/intel-installs-production-tools-at-fab-62-in-arizona-provides-updates-on-ohio-chip-fab-confirms-high-na-euv-for-high-volume-manufacturing-in-2028) —— Intel 代工路线图的关键节点确认，High-NA 量产时间表落地。
  _Tom's Hardware_
- [Nvidia Vera CPU 在 Modal 内部测试中吞吐达 Intel/AMD 两倍](https://www.tomshardware.com/pc-components/cpus/nvidia-vera-cpu-deployed-at-ai-startup-modal-alongside-existing-x86-fleet-internal-testing-showed-2x-throughput-compared-to-amd-and-intel) —— Nvidia 从 GPU 往 CPU 侧伸手的第一份第三方实测数据，但来自单一客户。
  _Tom's Hardware_

---

## 💬 觉得 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
