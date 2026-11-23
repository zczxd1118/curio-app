# Curio · 大厂 AI 动态 · 2026-11-23

> 今日 2 条头条 + 4 条备选

_今天两条主线：一是 Nvidia 的权力真空还在发酵——黄仁勋辞职两周后，董事会、白宫、SEC 三方同时介入，公司基本面（104B 营收、新加坡销售停披露）和治理丑闻已经脱钩成两个故事；二是 Google 用 Gemini 4 Neon 一周内连拿两个榜单第一，同时把 Meta Muse 这类第三方 Agent 接进 Walmart 购物链路，Agent 商业化从 demo 走进真实交易。_

---

## 🌟 今日精选

### 2. Gemini 4 Neon 发布即登顶两个评测榜，Google 在 3 周内连发 Carbon、Hydrogen、Neon 三代模型

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _yigitdemirag_

Google 于 11 月 18 日发布 Gemini 4 Neon，次日即在 Models Engineering Index 拿下第一，此前 Carbon 也曾登顶 Artificial Analysis Intelligence Index v5。三周内连发三个版本，节奏明显快于以往。社区评测普遍把 Neon 视为 Opus 5.5 的直接竞品。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 4 Neon 于 11 月 18 日发布，官方博客确认 | 两个榜单的评测方法不同，"第一"的含金量需要看具体任务分布，不能直接等同于全面领先 |
| Neon 在 Models Engineering Index 上排名第一，Carbon 曾在 Artificial Analysis v5 登顶 | 三周三代可能是并行训练的不同规格变体分批放出，而非真正的代际迭代 |
| Google 在 10 月底至 11 月中连续发布 Carbon、Hydrogen、Neon 三个 Gemini 4 变体 | Neon 相对 Opus 5.5 的实际工程体验差距，目前只有零星博客对比，缺系统性评测 |
| Gemini 4 Hydrogen 同步接入 Google Antigravity 开发环境 | 榜单排名与实际 Agent 任务成功率之间的相关性，历来被高估 |
| Genie 4 世界模型也已开放使用 | Google 是否会把这套发布节奏固化为常态，尚无官方说法 |

**📖 主编点评**

你正在做 content-curator，模型选型是绕不开的决策。建议不要只看榜单第一就切换——先拿你自己的真实任务（长文摘要、结构化抽取、多轮工具调用）在 Neon 和现有模型上各跑 20 条，用你自己的数据说话。榜单是别人的任务分布。

📺 [打开原文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

---

### 3. Walmart 开放 Agent 网关，允许 Meta Muse 代用户在站内完成黑五下单

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Jess Weatherbed_

Walmart 将于 11 月 24 日上线 Agent 网关，首批接入 Meta 的 Muse，让 AI Agent 代替用户在 Walmart 网站比价并完成购买。这是大型零售商第一次以官方网关形式向第三方 Agent 开放交易权限，而不是靠爬虫或浏览器自动化绕过。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Walmart 官方确认 Agent 网关于 11 月 24 日上线，首批合作方为 Meta Muse | 支付环节的授权边界与退款责任归属，报道未说明，可能是后续争议点 |
| Agent 可执行的操作包括搜索商品、比价、加入购物车与完成支付 | Walmart 是否会对 Agent 流量单独计价或限制品类，目前未知 |
| 这是零售商首次以官方 API 形式向第三方 Agent 开放交易链路 | 其他零售商是否会跟进开放类似网关，还是选择自建 Agent 封闭生态，尚不明朗 |
| 上线时间点紧贴黑五促销周期 | Agent 代下单的欺诈与误购风险如何兜底，没有公开的风控细节 |

**📖 主编点评**

这是 Agent 从"帮你查资料"跨到"帮你花钱"的标志性一步。你做 content-curator 迟早要碰"Agent 执行副作用操作"的授权设计——Walmart 这套网关的权限粒度、确认机制、失败回滚，值得你去找它的开发者文档读一遍，比看十篇 Agent 架构综述有用。

📺 [打开原文](https://www.theverge.com/ai-artificial-intelligence/1039874/walmart-agent-gateway-meta-muse-black-friday)

---

## 📋 备选阅读

- [Gemini 4 Neon 被视为 Opus 5.5 的直接竞品](https://micjm.com/blog/gemini-4-neon-looks-like-a-top-model/) —— 个人博客的对比评测，样本小但给了具体任务维度，比榜单排名更有信息量。
  _seizethecheese_
- [Google 员工联名要求公司不要惩罚拒绝 AI 的学校](https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/) —— AI 进校园的阻力开始组织化，这是产品落地绕不开的社会摩擦。
  _cdrnsf_
- [Stratechery：Amazon 财报、芯片问题与 Agent](https://stratechery.com/2026/amazon-earnings-the-chip-question-about-agents/) —— Ben Thompson 分析 Amazon 为何愿意牺牲毛利服务前沿客户，Agent 时代的云经济学。
  _Ben Thompson_
- [OpenAI 首席科学家谈如何给 AI 发展设限](https://techcrunch.com/2026/11/22/openais-chief-scientist-has-thoughts-on-how-to-limit-ai-development/) —— 核心观点是"要设速限先得对怎么测速达成共识"，方法论层面值得一读。
  _Anthony Ha_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
