# Curio · 大厂 AI 动态 · 2026-11-12

> 今日 2 条头条 + 6 条备选

_今天最重要的信号只有一个：Nvidia 董事会据报准备罢免黄仁勋，股价自丑闻爆发以来已跌 20%，国会要求闭门简报、FBI 介入。这不只是公司治理事件，而是整个 AI 算力叙事的定价锚在松动——同期 Nasdaq 已跌入回调区间、AI 相关股票被系统性抛售。另一条线是 Anthropic 在 IPO 前夕自曝"关键 AI 安全警报已被触发"，目标估值 1.4 万亿美元。两条线合起来看：AI 资本周期的风险溢价正在被重新定价。_

---

## 🌟 今日精选

### 2. OpenAI 单季营收首次突破 100 亿美元，环比 Q2 的 67 亿增长近 50%

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _TechCrunch_

据 TechCrunch 报道，OpenAI 季度营收首次跨过 100 亿美元，相比第二季度 67 亿美元增长近 50%。这个数字出现在 AI 股票被系统性抛售、Anthropic IPO 估值遭质疑的同一周，构成一个有意思的对照：终端付费需求仍在加速，但资本市场对 AI 公司的定价在收缩。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| OpenAI 单季营收首次突破 100 亿美元 | 100 亿是营收不是利润，OpenAI 的推理成本与算力支出是否同步扩大，报道未披露 |
| 上一季度（Q2）营收为 67 亿美元，环比增长近 50% | 增长中有多少来自 API/企业合同、多少来自 ChatGPT 订阅，结构不明 |
| 该数据由 TechCrunch 引述知情人士报道，非官方财报 | 若算力成本随 Nvidia 供应波动上升，这个增速的可持续性存疑 |
| 同期 Nasdaq 跌入回调区间，AI 相关股票遭抛售 | 与 Anthropic 1.4 万亿 IPO 估值对照，市场可能在重新分配"谁配得上高倍数" |

**📖 主编点评**

对你做 Agent 项目有直接含义：API 价格短期不会因为资本寒冬而上涨，反而可能继续打。现在是把重活（批量摘要、embedding、评测跑批）往 API 上搬的好窗口，别急着自建推理。同时留意 OpenAI 的收入结构披露——如果企业 API 占比在涨，说明 Agent 类产品的付费意愿是真的。

📺 [打开原文](https://techcrunch.com/2026/11/11/openais-quarterly-revenue-reportedly-crosses-10b-for-the-first-time/)

---

### 4. 美联航明确拒绝个人 AI Agent 代订机票，理由是隐私与监管

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _The Verge_

United 公开表示不会允许个人 AI 助手在其系统上代订机票，援引隐私与监管顾虑。公司称目前实际尝试用 Agent 订票的用户还不多，但选择提前划线。这是主流服务商第一次明确对"Agent 代操作"说不，对做 Agent 产品的人是重要的边界信号。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| United 明确表示不允许个人 AI Agent 代订机票 | "监管顾虑"具体指哪条法规未说明，可能是身份验证与授权链条问题 |
| 官方理由是隐私与监管顾虑 | 实际执行层面如何识别 Agent 流量（UA、行为指纹、支付信息）未披露 |
| 公司称目前尝试用 Agent 订票的用户数量还不多 | 其他航司与平台是否会跟进形成行业惯例，目前未知 |
| 这是主流航空公司首次公开对 Agent 代操作表态 | 对 Agent 生态的长期影响取决于是否有标准化授权协议出现 |

**📖 主编点评**

你在做 content-curator 时迟早会遇到同类问题：Agent 去抓取/操作第三方服务，对方是否授权。这条新闻的价值在于它给了你一个判断框架——先问"对方有没有明确的拒绝声明"，再设计自动化路径。把 Agent 的对外操作做成"可插拔的 connector + 显式授权记录"，比事后补救便宜得多。

📺 [打开原文](https://www.theverge.com/ai-artificial-intelligence/1031623/united-unauthorized-ai-agents)

---

## 📋 备选阅读

- [Google DeepMind 发布 AlphaGenome 2，从细胞层面解析疾病](https://www.theverge.com/ai-artificial-intelligence/1031524/google-deepmind-alphagenome-2-genetic-ai-model) —— DeepMind 在科学 AI 上的持续投入，与你偏好相关度低但属于"AI 真正落地"的少数方向。
  _The Verge_
- [Google 实验性产品 Tabletop：用 AI 生成定制协作应用](https://www.theverge.com/tech/1031526/google-tabletop-ai-experiment-waitlist-availability) —— 生成式 UI 的又一次尝试，目前是 waitlist 实验，值得关注但还没有工程细节可学。
  _The Verge_
- [Databricks 给 CEO 造了个 AI Agent，专门说"不加滤镜的真话"](https://techcrunch.com/2026/11/11/databricks-new-ai-agent-tells-ceo-ali-ghodsi-the-unvarnished-truth/) —— 1.2 万人公司的内部 Agent 实践，方向有意思（向上反馈），但报道偏故事、缺实现细节。
  _TechCrunch_
- [Meta 基础设施负责人 Santosh Janardhan 离职](https://techcrunch.com/2026/11/11/meta-is-losing-its-longtime-head-of-infrastructure/) —— 2009 年入职的老将离开，在 AI 算力军备竞赛节点上的人事变动，值得记一笔。
  _TechCrunch_
- [英国 Fractile 完成 7.2 亿美元融资，押注专用 AI 芯片](https://techcrunch.com/2026/11/11/with-720m-round-britains-fractile-gets-a-leg-up-in-the-race-for-ai-chips/) —— Nvidia 动荡周里，欧洲 AI 芯片挑战者拿到大额融资，是算力供应链多元化的一个注脚。
  _TechCrunch_
- [Ben Thompson：Intel 与 AMD 财报分化，Intel 可能需要找回"新（旧）路"](https://stratechery.com/2026/intel-earnings-amd-earnings-intel-and-amds-divergence/) —— Stratechery 的框架性分析，适合周末慢读，但今天不是最紧急的一条。
  _Stratechery_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
