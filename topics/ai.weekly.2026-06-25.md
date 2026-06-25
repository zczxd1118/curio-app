# Curio · AI · 2026-06-25

> 今日 5 条头条 + 15 条备选

_今日核心信号：美光财报炸裂，HBM产能提前售罄，存储短缺可能延续到2027年，AI需求见顶的担忧被击碎。同时，OpenAI与Broadcom发布自研推理芯片Jalapeño，AI芯片竞争进入新阶段。但瑞银调研显示60%企业已开始控制AI支出，模型路由策略兴起，高端模型收入增速承压。_

---

## 🌟 今日精选

### 1. OpenAI联合Broadcom发布首款自研推理芯片Jalapeño，9个月流片，性能功耗比领先

**[AI]** · ⭐⭐⭐⭐⭐ · _Russell Brandom_

OpenAI与Broadcom合作推出的Jalapeño芯片，是一款针对LLM推理优化的巨型ASIC，采用reticle-sized设计，开发周期仅9个月。该芯片宣称在性能功耗比上超越现有方案，标志着OpenAI从模型公司向芯片设计公司的关键一步。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Jalapeño是OpenAI首款自研芯片，由Broadcom代工设计 | 具体性能数据尚未公开，需第三方验证 |
| 芯片为reticle-sized ASIC，专为推理优化 | 量产时间和规模未披露 |
| 开发周期仅9个月，远超行业常规 | 对NVIDIA的替代效应尚不明朗 |
| 性能功耗比宣称超越现有领先方案 | 成本与定价策略未知 |
|  | 与Broadcom的长期合作排他性未说明 |

**📖 主编点评**

你应该关注Jalapeño的能效比数据，如果属实，将显著降低你的推理部署成本。对于正在做content-curator Agent的你，未来可能用上更便宜的API。同时，这预示着AI芯片格局正在松动，NVIDIA的垄断地位面临挑战。

📺 [打开原文](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/)

---

### 2. 美光财报炸裂：HBM产能提前售罄，存储短缺延续至2027年，AI需求见顶论被击碎

**[AI]** · ⭐⭐⭐⭐⭐ · _华尔街见闻 API_

美光最新财报显示数据中心收入超预期近七成，HBM产能已提前售罄，第四财季指引大幅上修，并签下覆盖数千亿美元收入的长期协议。这直接回应了市场对AI基建降温的担忧，存储短缺可能持续到2027年以后。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 数据中心收入超预期近70% | 存储涨价能否持续取决于AI需求实际增速 |
| HBM产能已提前售罄 | HBM盈利能力仍低于通用DRAM约30个百分点 |
| 第四财季指引大幅上修 | 2027年HBM盈利能力能否追上通用DRAM存不确定性 |
| 签下覆盖数千亿美元收入的长期协议 | 其他存储厂商产能扩张速度可能影响供需平衡 |
|  | 宏观经济下行风险可能抑制需求 |

**📖 主编点评**

美光财报对你意味着：AI基础设施投资远未结束，你的Agent项目依赖的算力成本短期内不会下降。但存储短缺可能导致硬件涨价，如果你计划部署本地模型，建议提前锁定存储资源。

📺 [打开原文](https://wallstreetcn.com/articles/3775486)

---

### 3. 瑞银调研：60%企业已开始控制AI支出，模型路由策略兴起，中国开源模型受益

**[AI]** · ⭐⭐⭐⭐ · _华尔街见闻 API_

瑞银调研显示约60%企业已为Token使用加设护栏，有公司单用户单月花费3.5万美元。企业普遍采用"模型路由"策略，简单任务转向低价甚至中国开源模型，高端模型收入增速承压。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 60%企业已实施AI支出控制措施 | 模型路由是否会导致高端模型降价尚不确定 |
| 模型路由策略成为主流，简单任务用低成本模型 | 企业控制支出是否长期趋势有待观察 |
| 中国开源模型（如DeepSeek）被纳入路由选项 | 中国开源模型的质量和可靠性仍需验证 |
| 高端模型收入增速面临压力 | 对AI初创公司估值的影响可能滞后 |
|  | 开源模型商业化路径尚不清晰 |

**📖 主编点评**

这对你是个好消息：模型路由意味着你可以用更低的成本运行简单任务，把预算留给复杂推理。建议你在content-curator项目中集成模型路由逻辑，根据任务复杂度动态选择模型，能省下不少Token费。

📺 [打开原文](https://wallstreetcn.com/articles/3775468)

---

### 4. Ben Thompson深度体验Vibe Coding：10条经验总结，从App构思到上线的完整实录

**[AI]** · ⭐⭐⭐⭐ · _Ben Thompson_

Stratechery作者Ben Thompson分享了他用Vibe Coding（Claude Code等工具）开发一个实际App的全过程，并总结了10条经验。这不是教程，而是一个资深科技分析师对AI编程范式的第一手反思，包括如何定义需求、管理AI输出、以及最终产品的质量评估。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Thompson使用Claude Code等工具开发了一个实际可用的App | Thompson的经验是否适用于非技术用户存疑 |
| 他总结了10条关于Vibe Coding的经验教训 | Vibe Coding生成代码的可维护性未经长期验证 |
| App已上线并计划日常使用 | 对复杂项目的适用性尚不明确 |
| 文章包含对AI编程效率与质量的真实评估 | AI编程工具的依赖风险未充分讨论 |
|  | 成本效益分析缺乏具体数字 |

**📖 主编点评**

作为正在做content-curator Agent的你，这篇文章值得细读。Thompson的10条经验可以直接指导你的开发实践，比如如何编写清晰的Prompt、如何管理AI的上下文窗口、以及如何评估AI生成的代码质量。建议你把这篇文章当作项目参考。

📺 [打开原文](https://stratechery.com/2026/my-vibe-coding-adventure-the-app-and-the-experience-ten-takeaways/)

---

### 5. 10分钟+300个Agent：保姆级教程学会Agent Skills，从概念到实战

**[AI]** · ⭐⭐⭐⭐ · _Work-Fisher_

这期视频从基础概念讲到上手实操，完整演示了一个Skill从无到有的创建过程，并对比了国内外创建工具。对于正在构建Agent的你，这是直接可用的实战指南。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 视频完整演示了Agent Skill的创建流程 | Skill的复杂场景适用性未深入探讨 |
| 对比了国内外多个创建工具 | 工具间的优劣对比可能不够全面 |
| 提供了从0到1的实操步骤 | 视频中的示例可能偏简单 |
| 视频时长10分钟，效率高 | 长期维护Skill的最佳实践未涉及 |

**📖 主编点评**

如果你正在用Agent Skills构建content-curator的工作流，这个视频可以帮你快速上手。建议你跟着视频实操一遍，然后尝试将你的内容筛选逻辑封装成可复用的Skill。

📺 [打开原文](http://www.bilibili.com/video/av116758736279146)

---

## 📋 备选阅读

- [SK hynix Nasdaq上市申请：融资290亿美元用于AI内存扩产](https://www.tomshardware.com/tech-industry/sk-hynix-files-to-raise-up-to-29-billion-in-nasdaq-listing) —— SK海力士申请在美上市，融资额创纪录，全部投入AI内存和EUV设备，进一步确认存储超级周期。
  _Luke James_
- [TSMC计划涨价：先进节点涨价5-10%，波及NVIDIA/AMD/Apple](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-is-reportedly-hiking-prices-for-all-advanced-nodes-accounting-for-74-percent-of-the-companys-wafer-business-nvidia-amd-apple-qualcomm-and-others-will-face-higher-wafer-costs) —— 台积电拟对7nm以下全线涨价，AI芯片成本将上升，但产能依然紧张。
  _Etiido Uko_
- [AI数据中心的"人肉瓶颈"：熟练工人短缺可能拖慢部署](https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-boom-hits-a-human-bottleneck-critical-skilled-labor-shortages-could-slow-deployment-despite-billions-in-funding) —— 尽管资本涌入，但数据中心建设缺乏熟练工人，可能成为AI基建的隐形瓶颈。
  _Zak Killian_
- [中国黑市NVIDIA A100服务器价格飙升至8.2万美元](https://www.tomshardware.com/pc-components/gpu-drivers/five-year-old-nvidia-a100-servers-triple-in-price-in-china) —— 美国制裁导致中国二手A100服务器价格暴涨3倍，反映AI算力供需极度失衡。
  _Luke James_
- [Meta暂停强制AI培训项目：因数据泄露暴露员工键盘记录](https://www.tomshardware.com/tech-industry/big-tech/meta-pauses-mandatory-ai-training-program-that-tracked-employee-keystrokes-after-internal-data-leak-exposed-sensitive-staff-information-company-wide-employees-express-frustration-over-poor-handling-of-data) —— Meta内部AI训练项目因数据泄露暂停，暴露了企业AI数据治理的脆弱性。
  _Etiido Uko_
- [AI研究人员持续从Google流向Anthropic](https://techcrunch.com/2026/06/24/ai-researchers-continue-to-leave-google-for-its-rivals/) —— 两位顶级AI研究员离开Google加入Anthropic，人才争夺战持续升温。
  _Amanda Silberling, Lucas Ropek_
- [Agility Robotics计划通过SPAC上市，估值25亿美元](https://techcrunch.com/2026/06/24/agility-robotics-plans-to-go-public-via-spac-in-a-2-5b-deal/) —— 人形机器人公司Agility Robotics拟SPAC上市，预计融资6.2亿美元，机器人商业化加速。
  _Kirsten Korosec_
- [Figma新更新：支持代码层、动画和更多AI功能](https://techcrunch.com/2026/06/24/figma-adds-code-layers-support-for-animations-more-ai-features-in-new-update/) —— Figma新增代码层和AI插件功能，设计到开发的衔接更紧密，对前端开发者是利好。
  _Ivan Mehta_
- [Cerebras财报后股价暴跌：毛利率展望被误解](https://techcrunch.com/2026/06/24/cerebras-stock-plunges-after-earnings-as-ceo-says-margin-outlook-was-misunderstood/) —— AI芯片公司Cerebras上市后首份财报引发股价大跌，市场对AI芯片盈利模式存疑。
  _Aisha Malik_
- [瑞银：高端PI膜供需失衡，英伟达锁定产能至2027年](https://wallstreetcn.com/premium/articles/3775139) —— AI算力需求带动高端PI膜紧缺，国产替代空间达220亿，供应链机会值得关注。
  _华尔街见闻 API_
- [SambaNova估值或达百亿：英特尔背书，能耗仅为NVIDIA GPU十分之一](https://wallstreetcn.com/articles/3775477) —— AI芯片新秀SambaNova获英特尔支持，RDU芯片能效优势显著，估值四个月暴涨五倍。
  _华尔街见闻 API_
- [中国超算LineShine登顶TOP500：纯CPU实现2.198 Exaflops](https://www.tomshardware.com/tech-industry/supercomputers/china-tops-the-top500-with-a-cpu-only-supercomputer-ending-el-capitans-reign) —— 中国纯CPU超算LineShine以2.198 Exaflops性能登顶，显示CPU架构仍有潜力。
  _Luke James_
- [Google Play Store开放第三方支付：降低开发者佣金](https://www.theverge.com/policy/956296/google-play-app-store-alternative-billing-fee-antitrust) —— Google在Epic诉讼和解后，正式允许开发者使用替代支付系统，佣金将下降。
  _Richard Lawler_
- [微软推出低价Surface：8GB内存版849美元起](https://www.theverge.com/tech/956504/microsoft-surface-pro-laptop-ram) —— 微软推出8GB内存版Surface Pro和Laptop，起售价849美元，降低入门门槛。
  _Emma Roth_
- [Nature论文质疑微软量子芯片Majorana 1：基础技术被指夸大](https://www.theverge.com/tech/956450/nature-microsoft-quantum-computing-majorana-1-claims) —— Nature发表批评文章，质疑微软Majorana 1量子芯片的基础技术，量子计算商业化再添变数。
  _Sophia Chen_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
