# Curio 趋势雷达 · 2026-07-24

> 你的私人主编 · 今日跨域精选 4 条头条 + 14 条备选

_今日最关键的信号是AI资本开支从现金流驱动转向债务扩张，中金测算未来五年或现3.5万亿美元融资缺口，Meta发债成本已上升。同时AMD发布Helios机架系统、MI455X加速器及256核Venice CPU，正面挑战Nvidia；Etched以300M融资和1B预订单证明非GPU推理芯片的商业可行性。你的content-curator项目可关注这些基础设施变化对Agent部署成本的影响。_

---

## 🌟 AI 算力 / 半导体

### 1. AMD向Anthropic供应2吉瓦Instinct MI450 GPU，投资高达50亿美元

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

AMD在Advancing AI 2026上宣布向Anthropic供应2吉瓦（约数十万块）MI450 GPU，首吉瓦于2027上半年在Helios机架系统中上线。同时AMD还发布了MI455X加速器、256核Epyc 9996 Venice CPU，并与Cerebras合作推理方案。这标志着AMD在AI训练/推理领域对Nvidia发起最全面挑战。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| AMD与Anthropic签署协议，供应总计2吉瓦的Instinct MI450 GPU | 2吉瓦GPU的实际总算力未公布，需等具体规格 |
| 首吉瓦预计2027上半年在Helios机架系统中上线 | Anthropic是否会因此减少对Nvidia的依赖尚不明朗 |
| AMD同时发布MI455X加速器（CDNA 5架构）、256核Epyc 9996 Venice CPU（Zen 6） | MI450的软件生态（ROCm）成熟度仍落后CUDA |
| AMD与Cerebras合作，将EPYC处理器与晶圆级引擎结合用于推理 | Helios系统的实际交付时间可能延迟 |
| AMD推出Helios机架级系统，对标Nvidia DGX | AMD与Cerebras合作的具体性能提升数据未披露 |

**📖 主编点评**

你正在用Claude Code做content-curator项目，Anthropic获得AMD大规模算力支持意味着Claude模型训练成本可能下降，API价格有望降低。建议关注AMD ROCm生态进展，如果未来能用AMD卡本地跑推理，你的Agent项目部署成本会更可控。

📺 [打开原文](https://www.tomshardware.com/tech-industry/amd-to-supply-anthropic-with-2-gigawatts-of-instinct-mi450-gpus)

---

## 🌟 股票

### 2. 中金：AI资本开支正从现金流驱动转向债务扩张，未来五年或现3.5万亿美元融资缺口

**[股票]** · ⭐⭐⭐⭐⭐ · _华尔街见闻_

中金报告指出，AI资本开支正从现金流驱动转向债务扩张，未来五年或出现3.5万亿美元融资缺口。投资要回本需每年约1万亿美元收入，意味着未来五年收入须年均近翻倍增长。同日Meta为德州数据中心寻求120亿美元融资，收益率超7%，风险溢价较九个月前高出0.4个百分点。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 中金测算AI资本开支未来五年融资缺口达3.5万亿美元 | 3.5万亿美元缺口是否包含表外负债存在争议 |
| Meta为德州近1吉瓦数据中心寻求120亿美元融资，收益率超7% | AI收入能否年均翻倍增长存疑 |
| Meta上笔270亿美元债券已跌至面值96美分 | 债券市场对科技巨头融资的容忍度可能继续下降 |
| 谷歌将2026年资本开支上限上调至2050亿美元，2027年或达3750亿美元 | 部分项目可能因融资成本上升而推迟或取消 |
| 五大科技巨头表外数据中心负债约1.65万亿美元 | 监管政策变化可能影响融资环境 |

**📖 主编点评**

你正在做个人Agent项目，AI基础设施融资收紧可能推高API价格。建议优先使用开源模型（如通过Ollama本地部署）降低长期依赖，同时关注那些有现金流自给能力的AI公司（如Anthropic有AMD大单支撑）。

📺 [打开原文](https://wallstreetcn.com/articles/3777832)

---

## 🌟 AI

### 3. Claude Code超强平替来了！彻底告别封号——Qoder CLI实测

**[AI]** · ⭐⭐⭐⭐ · _我是阿众_

B站UP主实测Qoder CLI作为Claude Code的国内平替，无需魔法、无需海外订阅，直接使用国产模型。视频展示了从安装到完成项目的完整流程，并对比了与Claude Code的差异。这对国内开发者尤其有价值。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Qoder CLI支持国内直连，无需科学上网 | Qoder CLI的代码生成质量与Claude Code的差距未量化 |
| 可接入DeepSeek等国产模型 | 长期稳定性和更新频率未知 |
| 视频展示了完整的安装和使用流程 | 是否支持复杂项目（多文件、长上下文）待验证 |
| UP主对比了Qoder与Claude Code的优缺点 | 社区生态和插件支持远不如Claude Code |

**📖 主编点评**

如果你因为封号问题困扰，Qoder CLI是一个值得尝试的备选。但你的content-curator项目涉及多文件操作和复杂工作流，建议先在简单任务上测试Qoder，确认其稳定性和能力后再迁移。同时保留Claude Code作为主力。

📺 [打开原文](http://www.bilibili.com/video/av116954828374073)

---

## 🌟 大厂 AI 动态

### 4. AI芯片创企Etched估值103亿美元，获3亿美元融资及10亿美元预订单

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _TechCrunch_

Etched由三名哈佛辍学生创立，开发专用于AI推理的芯片和内存组件，声称无需GPU即可加速任何模型。公司已获3亿美元融资，估值103亿美元，并有10亿美元预订单，今年夏天开始出货。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Etched完成3亿美元融资，估值103亿美元 | 实际性能是否达到宣传水平待第三方评测 |
| 公司获得10亿美元预订单 | 10亿美元预订单的客户构成和退款条款未披露 |
| 产品为专用推理芯片和内存组件 | 专用芯片面临通用GPU的生态优势挑战 |
| 今年夏天开始出货机架系统 | 量产能力和良率未知 |
| 投资者包括知名风投和产业资本 | 与Nvidia、AMD等巨头的竞争格局尚未明朗 |

**📖 主编点评**

Etched的专用推理芯片如果成功，将降低AI推理成本，对你这种Agent开发者是利好。建议关注其出货后的第三方评测，特别是推理速度和性价比。如果效果显著，未来你的content-curator项目可以考虑使用专用推理芯片降低成本。

📺 [打开原文](https://techcrunch.com/2026/07/23/ai-chip-startup-etched-defies-skeptics-hits-10-3b-valuation-from-big-name-investors)

---

## 📋 备选池

### AI 算力 / 半导体

- [TSMC计划2027年提价最高25%，先进制程涨价5%-10%](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes) —— 芯片制造成本上升将传导至AI芯片价格，影响你未来购买算力的预算。
  _Tom's Hardware_
- [美国启动Genesis Mission，首批项目拨款50亿美元](https://www.eetimes.com/u-s-starts-genesis-mission-with-5b-for-first-projects/) —— 美国加大AI基础设施投资，但相比中国的2950亿美元仍显不足，地缘政治风险需关注。
  _EE Times_
- [AMD发布256核Epyc 9996 Venice CPU，性能超Intel Xeon 3.4倍](https://www.tomshardware.com/pc-components/cpus/amds-256-core-epyc-9996-venice-claims-up-to-a-3-4x-jump-over-intel-xeon-competition-20-percent-over-nvidia-vera-zen-6-comes-with-up-to-1024mb-of-l3-16-channel-memory-and-5ghz-clock-speeds) —— 服务器CPU竞争白热化，AMD Zen 6架构带来巨大性能提升，但对你个人项目影响间接。
  _Tom's Hardware_
- [AI内存短缺推高汽车价格，通用汽车警告成本增加15-20亿美元](https://www.tomshardware.com/pc-components/ram/ai-memory-shortage-is-now-increasing-the-price-of-cars-gm-warns-of-vast-cost-increases-byd-hikes-driver-assistance-prices-20-percent) —— HBM和DRAM短缺蔓延至汽车行业，你买电脑/服务器时可能面临内存涨价。
  _Tom's Hardware_
- [两党法案要求最强AI模型配备“杀死开关”，违规每日罚款2000万美元](https://www.tomshardware.com/tech-industry/artificial-intelligence/bipartisan-bill-would-require-kill-switches-on-the-most-powerful-ai-models) —— AI监管趋严，未来你使用的API可能受合规限制，开源模型价值凸显。
  _Tom's Hardware_

### 大厂 AI 动态

- [Claude语音模式扩展至Opus和Sonnet模型](https://www.theverge.com/ai-artificial-intelligence/970065/anthropic-voice-mode-claude-opus-sonnet-haiku-ai) —— Anthropic提升语音交互能力，你的Agent项目可集成语音功能，但API成本可能增加。
  _The Verge_
- [OpenAI向所有美国用户开放ChatGPT Health，可接入Apple Health等数据](https://techcrunch.com/2026/07/23/openai-makes-chatgpt-health-available-to-all-u-s-users/) —— AI健康助手进入大众市场，但数据隐私问题值得警惕，你的项目可借鉴其Agent架构。
  _TechCrunch_
- [Google Gemini月活用户接近7.5亿，有望成为下一个十亿用户产品](https://techcrunch.com/2026/07/23/google-closes-in-on-another-billion-user-product-with-gemini/) —— Gemini用户增长迅速，但对你个人项目而言，关注其API更新比用户数更重要。
  _TechCrunch_
- [Runway推出AI模型路由工具Media Router，自动选择最佳生成模型](https://techcrunch.com/2026/07/23/runway-bets-on-ai-model-routing-as-generative-media-gets-crowded/) —— 模型路由概念可应用于你的Agent项目，根据任务自动选择最优模型以平衡成本和质量。
  _TechCrunch_

### 股票

- [Visa与连连完成大中华区首笔B2B AI智能体真实交易](https://wallstreetcn.com/articles/3777848) —— AI Agent首次完成真实B2B支付闭环，你的content-curator项目未来可集成支付功能。
  _华尔街见闻_
- [DeepSeek反共识判断：国产卡不缺生态只缺产能](https://wallstreetcn.com/premium/articles/3777844?layout=wscn-layout) —— 国产算力瓶颈从软件生态转向硬件产能，你部署Agent时需考虑国产卡可用性。
  _华尔街见闻_
- [谷歌Q2财报：云利润率超预期，但资本开支上调至2050亿美元](https://wallstreetcn.com/articles/3777835) —— 谷歌AI变现初现成效，但资本开支激增压制盈利，你使用的Google API可能面临涨价。
  _华尔街见闻_
- [SpaceX股价跌破IPO发行价，做空者获利87亿美元](https://www.reuters.com/business/media-telecom/short-sellers-rack-up-87-bln-profit-spacex-slips-below-ipo-price-ortex-2026-07-16/) —— SpaceX估值泡沫破裂，提醒你AI领域投资需谨慎，避免追逐概念股。
  _Reuters_

### 金融

- [Stripe与Advent联合出价530亿美元收购PayPal](https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/) —— 支付行业大整合，你的Agent项目若涉及支付，需关注API提供商变化。
  _Reuters_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
