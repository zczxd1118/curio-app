# Curio · AI 算力 / 半导体 · 2026-08-13

> 今日 2 条头条 + 5 条备选

_今日信号：AI 监管与合规进入深水区——Anthropic 为欧盟 AI 法案引入数字水印，引发效率与隐私之争；与此同时，AI 基础设施军备竞赛白热化，Nvidia 发布 Nemotron 3.5 Lightning 模型，CoreWeave 证明老旧 A100 仍能盈利，而 FCC 拟禁中国光模块，供应链博弈加剧。金融市场上，腾讯财报揭示 AI 投入对利润表的冲击，Citadel 看多 8 月美股。_

---

## 🌟 今日精选

### 2. Nvidia 发布 Nemotron 3.5 Lightning 与 NeMo Switchyard，推理效率再升级

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Hacker News_

Nvidia 推出 Nemotron 3.5 Lightning 模型（30B-A3B，NVFP4 量化）及配套的 NeMo Switchyard 工具，旨在提升推理效率并简化模型部署。该模型在 Hugging Face 上同步发布，引发开发者关注。此前 Nvidia 的 Vera 白皮书被 Chips and Cheese 指出存在漏洞，此次发布或为巩固其软件生态。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Nvidia 发布 Nemotron 3.5 Lightning 模型，采用 30B-A3B 架构，支持 NVFP4 量化。 | Nemotron 3.5 Lightning 的实际性能与推理速度尚未有第三方基准测试。 |
| 同时推出 NeMo Switchyard 工具，用于优化模型部署。 | NeMo Switchyard 是否能在企业级应用中普及，尚待观察。 |
| 模型已在 Hugging Face 上线，供开发者下载。 | Nvidia 在软件生态上的投入能否对抗 AMD 等竞争对手，仍不确定。 |
| Nvidia 的 Vera 白皮书此前被 Chips and Cheese 批评存在技术漏洞。 | Vera 白皮书的问题是否会影响 Nvidia 的硬件路线图，尚未明确。 |

**📖 主编点评**

作为 AI 产品开发者，你可以关注 Nemotron 3.5 Lightning 的量化版本，它可能适合在本地或边缘设备运行。NeMo Switchyard 或许能简化你的模型部署流程，值得研究。同时，Nvidia 的软件生态正在成为其护城河，你的 Agent 项目若依赖推理优化，可考虑跟进。

📺 [打开原文](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/)

---

### 4. CoreWeave 证明 2020 年的 A100 仍能盈利，签下 2029 年合同，季度营收 25.8 亿美元

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

CoreWeave  CEO 透露，公司已签下基于 A100 的合同，持续到 2029 年，证明老旧的 AI GPU 在电力受限和遗留基础设施下仍可盈利。CoreWeave 季度营收达 25.8 亿美元，同比增长 112%。这挑战了“AI 硬件快速迭代”的普遍认知，也为算力租赁市场提供了新视角。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| CoreWeave 已签署 A100 合同，有效期至 2029 年。 | A100 合同的利润率是否与新一代 GPU 相当，未披露。 |
| CoreWeave 季度营收 25.8 亿美元，同比增长 112%。 | 其他算力提供商是否会效仿，延长旧 GPU 的使用周期，尚不确定。 |
| A100 是 Nvidia 在 2020 年发布的 GPU。 | 电力成本上升是否会影响 A100 的长期盈利能力，需观察。 |
| CoreWeave 认为电力约束和遗留基础设施使旧 GPU 仍具经济性。 | CoreWeave 的商业模式是否可持续，取决于 AI 算力需求是否持续。 |

**📖 主编点评**

这对你的 AI 工程实践有启示：不必一味追求最新硬件，优化推理效率、利用现有资源同样重要。你的个人 Agent 项目如果依赖云端算力，可以考虑使用 A100 等性价比更高的实例，降低成本。

📺 [打开原文](https://www.tomshardware.com/tech-industry/coreweave-ceo-mike-intrator-says-it-has-signed-an-a100-contract-running-into-2029)

---

## 📋 备选阅读

- [Nvidia's Risky Business (Stratechery)](https://stratechery.com/2026/nvidias-risky-business/) —— Stratechery 深度分析 Nvidia 的商业模式风险，值得一读，但偏宏观，非紧急。
  _Hacker News_
- [Sony-TSMC $4.7B Deal Helps Thwart Samsung, Analysts Say](https://www.eetimes.com/sony-tsmc-4-7b-deal-helps-thwart-samsung-analysts-say/) —— 索尼与台积电联手对抗三星，影响图像传感器市场，对半导体行业有参考价值。
  _EE Times_
- [FCC proposes import ban on Chinese optical transceivers](https://www.tomshardware.com/tech-industry/fcc-proposes-import-ban-on-chinese-optical-transceivers-blockade-targets-key-ai-interconnects-as-china-holds-56-percent-global-market-share) —— FCC 拟禁中国光模块，影响 AI 数据中心供应链，地缘政治风险需关注。
  _Tom's Hardware_
- [Meta Cuts Server Count 25% by Reusing Old Memory: Can Anyone Else Do It?](https://www.eetimes.com/meta-cuts-server-count-25-by-reusing-old-memory-can-anyone-else-do-it/) —— Meta 通过 CXL 复用旧内存减少服务器数量，对成本优化有启发，但技术门槛高。
  _EE Times_
- [Intel raises $19.7 billion to help fund future projects as 14A production looms](https://www.tomshardware.com/tech-industry/semiconductors/intel-raises-usd19-7-billion-to-help-fund-future-projects-as-14a-production-looms-share-sale-attracted-usd100-billion-in-demand-report-claims) —— Intel 融资 197 亿美元，为 14A 工艺做准备，半导体竞争加剧。
  _Tom's Hardware_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
