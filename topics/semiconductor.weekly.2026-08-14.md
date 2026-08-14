# Curio · AI 算力 / 半导体 · 2026-08-14

> 今日 1 条头条 + 3 条备选

_今日核心信号：AI 算力军备竞赛进入新阶段——Nvidia 发布 Nemotron 3.5 Lightning 与 NeMo Switchyard，xAI 计划 2027 年将数据中心容量扩至 10GW，而 OpenAI 年化收入破 400 亿美元并推出 Ultrafast 模式。同时，DeepSeek Harness 开源引发自进化软件讨论，CXMT 上市 17 天市值超腾讯，存储芯片涨价潮持续。_

---

## 🌟 今日精选

### 1. Nvidia 发布 Nemotron 3.5 Lightning 与 NeMo Switchyard，推理效率与部署灵活性双突破

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _droidjj_

Nvidia 官方博客今日发布 Nemotron 3.5 Lightning 模型及 NeMo Switchyard 框架，前者主打高效推理，后者支持动态切换模型。这是 Nvidia 从训练向推理市场进攻的信号，直接对标 vLLM 等开源方案。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Nemotron 3.5 Lightning 已上线 Hugging Face，30B 参数采用 A3B 架构，支持 NVFP4 量化 | Lightning 系列是否能在实际推理任务中超越同等规模开源模型（如 Llama 3.1）尚未有第三方评测 |
| NeMo Switchyard 提供模型路由与动态切换能力，可优化推理成本 | Switchyard 的框架生态能否吸引开发者迁移，仍待观察 |
| Nvidia 同步更新 RTX DGX 平台支持，强化端侧部署 | Nvidia 此举是否意味着其战略重心从硬件转向软件栈，还需更多产品线验证 |
| 博客发布当日 HN 热度 261 分，社区关注度高 |  |

**📖 主编点评**

你应该关注 Nemotron 3.5 Lightning 的实际性能，特别是 NVFP4 量化下的推理速度。如果它能在消费级 GPU 上跑出好效果，可能会成为你本地部署 Agent 的优选模型。同时，NeMo Switchyard 的模型路由思路，对你正在做的 content-curator 项目也有借鉴——可以用它来动态选择不同模型处理不同任务。

📺 [打开原文](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/)

---

## 📋 备选阅读

- [CXMT 上市 17 天市值超腾讯，成中国最值钱公司，估值 5240 亿美元](https://www.tomshardware.com/tech-industry/cxmt-overtakes-tencent-to-become-chinas-most-valuable-company-17-days-after-its-ipo) —— 存储芯片涨价潮推动 CXMT 市值飙升，反映中国半导体自主化加速，但估值泡沫风险需警惕。
  _Luke James_
- [TSMC 2027 年拟将芯片代工价格上调最高 25%](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes) —— 先进制程涨价将推高 AI 芯片成本，影响下游硬件价格，值得关注。
  _speckx_
- [Meta 通过复用旧内存将服务器数量削减 25%](https://www.eetimes.com/meta-cuts-server-count-25-by-reusing-old-memory-can-anyone-else-do-it/) —— CXL 技术让旧 DDR4 焕发新生，对数据中心降本有借鉴意义，但实施门槛高。
  _Yashasvini Razdan_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
