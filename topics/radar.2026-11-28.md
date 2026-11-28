# Curio 趋势雷达 · 2026-11-28

> 你的私人主编 · 今日跨域精选 5 条头条 + 14 条备选

_今天最重要的信号有两个：一是 Nvidia 董事会把黄仁勋请回 CEO 位子，但 SEC 会计调查、国会质疑、S&P 警告董事会独立性、东南亚出货暂停同时压上来，这件事已经从人事八卦变成治理与出口管制的双重风险；二是 Anthropic IPO 定价 $83、估值 $1.5T 后迅速跌破发行价，AI 资产的定价逻辑正在被重新校准。对做 Agent 的你来说，工具层今天没有大新闻，但 Claude Code 桌面端整合、Gemini 4 系列迭代仍在推进。_

---

## 🌟 AI 算力 / 半导体

### 1. Nvidia 董事会请回黄仁勋任 CEO，但 SEC 会计调查、国会质疑与东南亚出货暂停同时压顶

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _jaz_

11 月 23 日 Nvidia 董事会宣布恢复黄仁勋总裁兼 CEO 及董事身份，结束了此前数周的权力真空。但这不是一个干净的回归：SEC 正在查潜在会计问题，S&P 警告董事会独立性可能受损，国会直接称这是'性格的失败'，同时公司已要求代工伙伴暂停对马来西亚、新加坡、泰国、印尼的服务器出货。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 11 月 23 日 Nvidia 董事会正式恢复黄仁勋 CEO 与董事职务，官方新闻稿已发布 | SEC 会计调查最终是否升级为正式指控，目前无时间表 |
| SEC 调查正在审查潜在会计问题，多家媒体援引消息人士 | 董事会此次反转是否触发更多机构投资者诉讼或代理权之争 |
| S&P 公开警告 Nvidia 董事会可能已失去独立性 | 东南亚出货暂停是短期合规动作还是长期区域策略收缩，公司未说明 |
| Nvidia 已要求制造伙伴暂停对马来西亚、新加坡、泰国、印尼的服务器出货 | 黄仁勋回归后对华出口政策立场会更强硬还是更务实，尚无公开表态 |
| 此前有报道称超过 1.5GW 受禁 GPU 被走私至中国，被视为黄离职的潜在诱因 | Polymarket 上两个可疑账户在事件中获利超 $34 万，是否涉及内幕交易仍在调查 |
| Nvidia 停止披露新加坡销售额，同期营收达 $104B |  |

**📖 主编点评**

这条不是让你去炒 Nvidia，而是提醒你：AI 算力的供给端正在被地缘政治和公司治理同时扰动。如果你在做需要调用海外模型的 Agent 项目，应该开始假设'API 供给可能因政策突然收紧'，把模型接入层做成可切换的（Claude / Gemini / DeepSeek 多路 fallback），而不是硬绑一家。

📺 [打开原文](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html)

---

## 🌟 股票

### 2. Anthropic 以 $83 定价、$1.5T 估值上市，数日内跌破发行价，AI 资产定价逻辑被重新校准

**[股票]** · ⭐⭐⭐⭐⭐ · _thm_

Anthropic 的 IPO 是本轮 AI 热潮里最受关注的定价事件：发行价 $83、估值约 $1.5T，上市首日冲高后迅速回落，11 月 24 日已跌破发行价。此前 Blackstone 就说过它可能拿不到投资级评级，信用机构预期给'高收益级'（垃圾级），Michael Burry 则称其'把存在押在乐观上'。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Anthropic IPO 定价 $83/股，对应估值约 $1.5T，AP 与 Reuters 均有报道 | 跌破发行价是短期市场情绪还是对 $1.5T 估值的实质性否定，需要看后续几个季度财报 |
| 上市后数日内股价跌破 $83 发行价，首日涨幅回吐 | $900B 的 AI 支出承诺能否转化为收入，目前只有承诺没有兑现路径 |
| IPO 文件披露季度人力成本 $1.7B，人均月成本约 $107K | '接近 RSI'的表述是风险披露还是营销话术，监管是否会介入 |
| 信用机构预期给予高收益级（垃圾级）评级，Blackstone 曾公开质疑其投资级前景 | 垃圾级评级会如何影响其后续融资成本和算力采购能力 |
| 承销银行已平掉原本用于稳定股价的仓位 | AI 板块整体回调是否会传导到创业公司估值和招聘 |
| IPO 文件警告公司可能'即将'接近递归自我改进（RSI） |  |

**📖 主编点评**

你不需要关心股价，但要关心它背后的信号：头部 AI 公司的融资成本在上升，意味着'烧钱换规模'的模式正在被市场质疑。这对你的启示是，做 side project 时优先选'能自己跑起来、边际成本低'的方向，而不是需要大量 API 调用烧钱的产品形态。

📺 [打开原文](https://www.reuters.com/business/anthropic-breaks-below-83-ipo-price-debut-rally-unravels-2026-11-24/)

---

## 🌟 大厂 AI 动态

### 3. Google 发布 Gemini 4 Neon，在 Models Engineering Index 上登顶，被指对标 Opus 5.5

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _yigitdemirag_

Gemini 4 系列今年迭代极快：Carbon、Hydrogen、Neon 接连发布，Neon 上线后直接冲到 Models Engineering Index 第一，社区评价它'看起来像 Opus 5.5 的竞争对手'。同期 Google 还放出了 Gemini Decisions API 和 Genie 4，模型层和工具层一起推。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 4 Neon 已通过 Google 官方博客发布 | Neon 的实际编码与 Agent 任务表现是否真能对标 Opus 5.5，需要独立评测而非榜单 |
| Neon 在 Models Engineering Index 上排名第一，该榜单由第三方维护 | Models Engineering Index 的权威性和评测方法未公开细节，排名需谨慎看待 |
| Gemini 4 Carbon 此前在 Artificial Analysis Intelligence Index v5 上曾登顶 | Gemini 4 系列迭代过快，模型命名（Carbon/Hydrogen/Neon）对开发者选择造成困惑 |
| Google 同期发布 Gemini Decisions API，面向开发者工具场景 | Decisions API 的具体能力和定价尚未清晰 |
| Genie 4 已开放使用，DeepMind 发布相关博客 | Google 内部员工工会化、抗议向学校施压等事件是否影响产品节奏 |
| Gemini 4 Hydrogen 与 Orchestrator 已在 Google Antigravity 平台上线 |  |

**📖 主编点评**

如果你在 content-curator 里做模型路由，现在值得把 Gemini 4 Neon 加进候选池实测一轮，尤其是长上下文和工具调用场景。但别只看榜单——用你自己的真实任务（比如抓取+摘要+结构化输出）跑一遍，比任何 index 都准。

📺 [打开原文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

---

## 🌟 AI

### 4. Claude 桌面端把 Code、Design、Cowork 收进同一个客户端，Claude Code 从命令行进化成桌面完全体

**[AI]** · ⭐⭐⭐⭐ · _技术爬爬虾_

Claude Desktop 近期一波更新把三块能力合并：Claude Code 的编程、Claude Design 的设计、Claude Cowork 的办公，全部收进同一个桌面客户端，配合 Opus 5.5 模型。这意味着 Claude Code 不再是黑乎乎的命令行工具，而是有了完整 GUI 的 Agent 工作台。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Claude Desktop 已整合 Claude Code、Claude Design、Claude Cowork 三项能力 | 桌面端整合后对命令行工作流是替代还是补充，长期看取决于脚本化和 CI 场景 |
| Claude Code 从纯命令行形态扩展为桌面客户端内的完整功能 | 第三方 API 接入（如接 DeepSeek）的稳定性和官方态度不明，有被封风险 |
| 当前搭配的模型为 Opus 5.5 | Claude Design 的实际产出质量是否达到可交付水平，缺少独立评测 |
| 该视频为 11 月 8 日发布，属于近期更新 | Cowork 办公能力的边界（能操作哪些本地应用）未明确 |
| 社区已有多个教程覆盖桌面端安装、第三方 API 接入、Skill 安装 | 桌面端是否会成为 Anthropic 锁定用户的主入口，影响其他 IDE 插件生态 |

**📖 主编点评**

你正在做 content-curator，这是个典型的'需要长时间跑 Agent 任务'的场景。值得花一个周末把 Claude Desktop 装起来，重点试两件事：一是 Skill 机制能不能把你的抓取-筛选-成稿流程固化成一个可复用 Skill；二是桌面端的会话管理是否比命令行更适合你这种'边看边调'的工作方式。

📺 [打开原文](http://www.bilibili.com/video/av117580048108571)

---

## 🌟 金融

### 5. 美联储开始担心 AI Agent 可能触发银行挤兑，金融系统的 Agent 风险进入监管视野

**[金融]** · ⭐⭐⭐⭐ · _pera_

Gizmodo 报道美联储内部已在讨论一个此前只存在于理论中的场景：大量 AI Agent 同时执行提款或转账指令，可能在极短时间内抽干银行流动性，形成算法驱动的挤兑。这不是科幻，而是 Agent 大规模接入金融 API 后的现实风险。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 美联储内部已就 AI Agent 可能引发银行挤兑展开讨论，Gizmodo 报道 | 美联储是否会将 Agent 行为纳入正式监管框架，目前无具体提案 |
| 讨论的核心场景是大量 Agent 同时执行提款/转账导致流动性骤降 | 'Agent 挤兑'是真实概率事件还是预防性讨论，缺少量化模型 |
| 该担忧出现在 Agent 接入金融系统 API 日益普遍的背景下 | 银行是否会限制 Agent 的 API 访问权限，还是选择拥抱 |
| 同期有报道称 Visa、Mastercard、JPMorgan 客户数据被黑客泄露 | Agent 身份认证与速率限制的技术标准由谁制定尚未明朗 |
| Fed 此前已在关注 AI 对金融稳定的影响 | 这类监管讨论对个人开发者调用金融 API 的影响程度未知 |

**📖 主编点评**

这条对你做 Agent 项目有直接含义：如果你的 content-curator 未来要接任何'能触发真实动作'的 API（支付、下单、发消息），现在就该在设计上留出'人工确认闸门'和速率上限。监管迟早会来，提前把'Agent 不能自主执行不可逆操作'写进架构，比事后改便宜得多。

📺 [打开原文](https://gizmodo.com/the-fed-is-worried-ai-agents-could-trigger-a-bank-run-2000840566)

---

## 📋 备选池

### AI 算力 / 半导体

- [Huawei's Next Big AI Move: HBM Workaround](https://www.eetimes.com/huawei-next-big-ai-move-hbm-workaround/) —— 华为将在 ISSCC 2027 公布自研 HBM 方案，绕开出口管制的存储瓶颈，是国产算力链的关键变量。
  _Majeed Ahmad / EE Times_
- [Serving GLM-5.3 at 607.8 tok/s across two Nvidia DGX stations with vLLM](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/) —— NVIDIA 官方博客给出跨两台 DGX 跑 GLM-5.3 的 vLLM 配置，607.8 tok/s，是少见的带具体参数的推理优化实操。
  _NVIDIA Developer Blog_
- [Penguin Revives Retired DDR4 for AI Servers](https://www.eetimes.com/penguin-revives-retired-ddr4-for-ai-servers/) —— 企业级开始回收退役 DDR4 用于 AI 服务器扩容，内存成本压力下的务实选择，硬件侧的小信号。
  _Gary Hilson / EE Times_

### 大厂 AI 动态

- [AMD-specific fork of llama.cpp](https://devnull.land/amd-specific-llama-cpp) —— llama.cpp 的 AMD 专用分支，对没有 N 卡但想本地跑模型的开发者是实用增量，444 分说明需求真实。
  _julianlam / HN_
- [Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU](https://github.com/synchopate/llama-modchip) —— 在 64GB 内存、无 GPU 的机器上跑 284B DeepSeek，工程取巧思路值得一看，但实用性待验证。
  _joshcsimmons / HN_
- [Stacktrace: Real-time steering and guardrails for AI agents](https://www.producthunt.com/products/stacktrace) —— 给 AI Agent 做实时转向和护栏的工具，正好踩在 Agent 可控性这个痛点上，值得关注其实现方式。
  _Nico Lumma / Product Hunt_

### 股票

- [Nasdaq erases all 2026 gains](https://www.cnbc.com/2026/11/19/stock-market-today-live-updates.html) —— 纳指抹平 2026 全年涨幅，与 Anthropic 破发、芯片股回调是同一波叙事，宏观背景参考。
  _mv4 / HN_
- [A Banker's Guide to Anthropic](https://www.netinterest.co/p/a-bankers-guide-to-anthropic) —— 从银行家视角拆解 Anthropic IPO 为何是'信用事件'而非单纯股权事件，比新闻稿深一层。
  _Marc Rubinstein / Net Interest_

### 金融

- [Oracle files to sell $20B in new stock, bonds to finance AI buildout](https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html) —— Oracle 发 $20B 股债为 AI 基建融资，是'AI 资本开支靠债务撑'这条主线的又一实证。
  _smartmic / HN_
- [Intel faced a choice: Give Trump 10% or face the consequences](https://arstechnica.com/tech-policy/2026/11/intel-faced-a-choice-give-trump-10-or-face-the-consequences/) —— Intel 被要求让出 10% 股权换取补贴，政府直接持股半导体的先例，产业政策信号强。
  _Ars Technica_

### 电子信息与芯片

- [Investigation of Polymarket Insider Trading on the Reinstatement of Jensen Huang](https://deucalionn.vercel.app/polymarket-delit-initie-jensen-huang-nvidia/) —— 对 Polymarket 上黄仁勋回归内幕交易的独立调查，481 分，是预测市场被操纵的罕见实证案例。
  _oska / HN_
- [Beyond Lithography: The Battle for Semiconductor Manufacturing Yield](https://www.eetimes.com/beyond-lithography-the-battle-for-semiconductor-manufacturing-yield/) —— MATCH Act 暴露的不只是 ASML 光刻机，还有决定良率的工艺技术，半导体竞争的第二战场。
  _Ron Honig / EE Times_

### AI

- [Claude Code 零基础终极教程：安装、换模型、插件、Hooks、Skills、Subagents、实战项目一次讲透](http://www.bilibili.com/video/av116529475622752) —— 少见的把 Hooks、Skills、Subagents 讲全的中文教程，对做 Agent 工作流有直接参考价值，但发布时间较早（5 月）。
  _木子不写代码_
- [50 分钟速通 Codex 保姆级教程（含 DeepSeek 接入，无需 ChatGPT 订阅）](http://www.bilibili.com/video/av117671517489403) —— 11 月 24 日新发，含 DeepSeek 接入方案，时效性好，但属于教程类，深度待验证。
  _林粒粒呀_

---

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
