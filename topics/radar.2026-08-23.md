# Curio 趋势雷达 · 2026-08-23

> 你的私人主编 · 今日跨域精选 5 条头条 + 12 条备选

_今日信号：AI 竞争从模型转向 Harness 与 Agent 执行层，Nvidia 与 DeepSeek 同时验证这一趋势；存储涨价潮正传导至终端与服务器，英伟达高端服务器明年或涨 15%；OpenAI 加速 IPO 进程，但人才流失与安全团队解散埋下隐患。_

---

## 🌟 AI 算力 / 半导体

### 1. Nvidia AVO 满分通过 ARC-AGI-3，Harness 成为 AI 竞争新焦点

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _TechCrunch_

Nvidia 的 AVO 智能体在 ARC-AGI-3 交互推理基准上拿下 100% 满分，引发行业讨论：模型能力之外，控制框架（Harness）正成为决定智能体上限的关键。TechCrunch 评论指出，Harness 而非模型本身才是真正的英雄。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Nvidia AVO 在 ARC-AGI-3 基准上达到 100% 准确率 | ARC-AGI-3 基准是否被过度拟合，尚未有第三方独立验证 |
| Nvidia 官方博客与开发者博客均发布了相关技术细节 | AVO 的 100% 得分能否推广到真实世界复杂任务，仍属未知 |
| TechCrunch 发表评论文章，认为 Harness 是 AI 竞争的新焦点 | Harness 与模型能力的相对重要性，行业尚无定论 |
| Nvidia 同时发布了 Nemotron 3.5 Lightning 模型和 NeMo Switchyard 工具 | Nvidia 在软件生态的投入能否转化为硬件销售优势，有待观察 |

**📖 主编点评**

你在构建 content-curator Agent 时，别只盯着模型选型。Nvidia 和 DeepSeek 都在证明：同样的模型，换一套 Harness（如 DeepSeek Harness）效果可能天差地别。建议你花时间研究 Claude Code 的 Hooks、SubAgent 机制，以及 DeepSeek Harness 的开源实现，把这些控制层能力用到你的项目里，比单纯换模型更能提升 Agent 的可靠性和效率。

📺 [打开原文](https://techcrunch.com/2026/08/21/nvidia-just-showed-that-the-harness-not-the-ai-model-is-now-the-real-hero/)

---

## 🌟 AI

### 2. DeepSeek Harness 开源，编程 Agent 工具链迎来新选择

**[AI]** · ⭐⭐⭐⭐ · _Lau博士的云组会_

DeepSeek 开源了其 Harness 工具，Lau 博士在视频中解读了它的独特之处。与此同时，有 Up 主实测对比 DeepSeek Harness 与 Claude Code，发现工具链对最终效果的影响可能比模型本身更大。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DeepSeek Harness 已开源，视频解读了其核心设计 | DeepSeek Harness 与 Claude Code 的差距是否如视频所说，需更多验证 |
| 实测视频使用同一 DeepSeek 模型，对比 Harness 与 Claude Code 的表现 | Harness 的插件生态和社区支持能否快速成长，尚不明朗 |
| 实测项目包括 FPS 游戏 Demo、灯塔预警沙盘等 | DeepSeek Harness 对国内用户是否更友好（如 API 接入），需实际测试 |
| DeepSeek Harness 强调插件化、流程记录和缓存命中 |  |

**📖 主编点评**

你正在做 Agent 项目，DeepSeek Harness 开源值得你花时间研究。它可能提供比 Claude Code 更灵活的插件机制和成本控制（尤其在国内网络环境下）。建议你下载源码，重点看它的插件化流程和缓存设计，说不定能借鉴到你的 content-curator 里，让 Agent 更省 Token、更可控。

📺 [打开原文](http://www.bilibili.com/video/av117089415204498)

---

## 🌟 股票

### 3. 存储芯片成本飙升，英伟达高端服务器明年或涨价 15%

**[股票]** · ⭐⭐⭐⭐ · _华尔街见闻_

据知情人士透露，因存储芯片成本上涨，英伟达高端服务器（搭载 Vera Rubin 和 Grace Blackwell）将从明年初开始涨价约 15%，代工厂已收到通知。这将影响微软、谷歌等大厂的 AI 基础设施采购成本。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 涨价将从明年初出货的系统开始生效 | 涨价幅度是否最终落地为 15%，尚待官方确认 |
| 影响范围包括 Vera Rubin 和 Grace Blackwell 芯片的系统 | 大厂是否会因此调整 AI 资本开支计划，需观察 |
| 代工厂已发出涨价通知，具体涨幅取决于芯片代际和存储配置 | 存储涨价趋势能持续多久，影响后续服务器价格走势 |
| 存储芯片成本飙升是主要原因 |  |

**📖 主编点评**

如果你在关注 AI 基础设施成本，这个信号很重要。存储涨价会推高服务器价格，可能影响你未来部署模型的成本。建议你关注存储芯片（如 HBM、NAND）的供需动态，同时考虑在项目中使用更高效的模型量化或缓存策略，降低对存储带宽的依赖。

📺 [打开原文](https://wallstreetcn.com/articles/3780066)

---

## 🌟 大厂 AI 动态

### 4. Codex on AWS Bedrock 计费 bug 导致 10 倍费用，开发者需警惕

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _GitHub_

OpenAI Codex 在 AWS Bedrock 上出现计费 bug，导致用户被收取高达 10 倍的费用。GitHub issue 已引发广泛关注，提醒开发者在使用云服务集成 AI 工具时需仔细核对账单。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| GitHub issue 报告了 Codex on AWS Bedrock 的计费异常 | bug 的具体原因和修复时间尚不明确 |
| 用户被收取的费用高达正常值的 10 倍 | 是否影响所有 Bedrock 用户，还是特定配置触发，需进一步确认 |
| 该问题已获得 148 分关注，影响范围可能较大 | OpenAI 是否会主动退款，有待观察 |

**📖 主编点评**

你在使用 Codex 或类似云服务时，务必开启费用警报，并定期检查账单。这个 bug 提醒我们，AI 工具链的计费系统可能不透明，尤其是通过第三方平台（如 AWS）使用时。建议你记录每次调用的 Token 数和费用，建立自己的成本监控机制。

📺 [打开原文](https://github.com/openai/codex/issues/37674)

---

## 🌟 金融

### 5. 芝加哥大学研究：工资粘性使意外通胀对实际工资影响复杂化

**[金融]** · ⭐⭐⭐ · _Hacker News_

芝加哥大学 BFI 发布工作论文，研究工资粘性如何影响意外通胀对实际工资的冲击。论文指出，在工资调整缓慢的情况下，意外通胀可能导致实际工资下降，但长期影响取决于通胀预期。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 论文由芝加哥大学 BFI 发布 | 研究结论是否适用于当前高通胀环境，需更多实证 |
| 研究聚焦于工资粘性与意外通胀的关系 | 政策制定者是否会参考该研究调整货币政策，尚不确定 |
| 论文提出实际工资成本受通胀预期影响 | 工资粘性的测量方法可能存在争议 |
| 该研究在 Hacker News 上获得 391 分关注 |  |

**📖 主编点评**

虽然这篇论文偏学术，但对你理解宏观环境有帮助。当前通胀和工资数据波动大，如果你在关注经济走势或投资，了解工资粘性可以帮你判断通胀对消费和企业利润的传导。不过，作为工程师，你可以跳过，除非你对宏观经济特别感兴趣。

📺 [打开原文](https://bfi.uchicago.edu/wp-content/uploads/2026/08/BFI_WP_2026-108-1.pdf)

---

## 📋 备选池

### AI

- [【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！](http://www.bilibili.com/video/av116951003242391) —— 吴恩达亲自讲解 Vibe Coding 工作流，适合系统学习，但内容偏基础，与你的实战经验可能重叠。
  _吴恩达AIAgent_
- [从零编写MCP并发布上线，超简单！手把手教程](http://www.bilibili.com/video/av114630814862349) —— MCP 实战教程，教你从零开发并发布 MCP 服务，对你的 Agent 项目有直接参考价值。
  _技术爬爬虾_
- [【入站必看】B站史上最全Codex零基础教程！90分钟入门到进阶！](http://www.bilibili.com/video/av117131979134458) —— Codex 深度教程，包含 22 个案例，适合想深入掌握 Codex 的开发者，但时长较长。
  _GenJi是真想教会你_

### AI 算力 / 半导体

- [Micron commits $10 billion to new US-based Research Labs](https://www.tomshardware.com/tech-industry/micron-commits-usd10-billion-to-new-us-based-research-labs-boise-hub-to-target-post-dram-and-nand-technologies-and-packaging) —— 美光投 100 亿美元建研发实验室，瞄准下一代存储技术，对存储行业影响深远。
  _Tom's Hardware_
- [China approves first Nvidia H200 deliveries to ByteDance and Tencent](https://www.tomshardware.com/pc-components/gpus/china-approves-first-nvidia-h200-deliveries-to-bytedance-and-tencent-under-case-by-case-import-licenses) —— H200 终于获批进入中国，但国产芯片已抢占市场，Nvidia 或已错失良机。
  _Tom's Hardware_

### 大厂 AI 动态

- [Gemini 3.7 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) —— Google 发布 Gemini 3.7 Flash，性能提升，值得关注，但信息量不如头条。
  _Google_
- [Inherent, founded by DeepMind alumni, says its AI 'teammate' just outperformed Anthropic and OpenAI at replicating research](https://techcrunch.com/2026/08/22/inherent-founded-by-deepmind-alumni-says-its-ai-teammate-just-outperformed-anthropic-and-openai-at-replicating-research/) —— DeepMind 校友创业，AI 智能体在复现研究上超越 Anthropic 和 OpenAI，值得关注。
  _TechCrunch_
- [Apple is laying off staffers working on the Vision Pro and Siri](https://www.theverge.com/tech/983451/apple-layoffs-vision-pro-siri) —— 苹果裁员 Vision Pro 和 Siri 团队，反映 AI 硬件和助手业务调整。
  _The Verge_

### 股票

- [高盛：存储“股价业绩差”最具吸引力，金融和硬资产成为新热点](https://wallstreetcn.com/articles/3780070) —— 高盛认为 AI 交易躺赢时代结束，存储和数据中心最具战术吸引力，适合关注。
  _华尔街见闻_
- [OpenAI 'will be a public company in 2027' or sooner, CFO Friar tells employees](https://www.cnbc.com/2026/08/19/open-ai-ipo-timing-2027-friar.html) —— OpenAI CFO 透露 2027 年上市，IPO 进程加速，但人才流失是风险。
  _CNBC_

### 金融

- [30-year Treasury yield tops 5.31%, the highest in 19 years](https://www.cnbc.com/2026/08/17/treasury-yields-federal-reserve-fomc-minutes.html) —— 30 年期美债收益率创 19 年新高，反映市场对通胀和财政的担忧。
  _CNBC_
- [The bond market isn’t buying what Fed Chair Warsh is selling](https://www.reuters.com/commentary/reuters-open-interest/bond-market-isnt-buying-what-fed-chair-warsh-is-selling-2026-07-30/) —— 债市不信任美联储主席沃什的政策，收益率高企，宏观风险需留意。
  _Reuters_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
