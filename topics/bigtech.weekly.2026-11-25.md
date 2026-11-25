# Curio · 大厂 AI 动态 · 2026-11-25

> 今日 2 条头条 + 5 条备选

_今天最重要的信号有两个：一是 Nvidia 董事会把 Jensen Huang 请回来了，从辞职到复职只隔一周，但国会、SEC 调查、Polymarket 内幕下注全在发酵，这家公司治理的可信度被打了个洞；二是 Anthropic IPO 跌破 83 美元发行价，承销商稳定盘也撤了，AI 一级市场估值开始被公开市场重新定价。这两件事叠在一起，说明 AI 叙事正在从「无限乐观」切换到「要交财报」。_

---

## 🌟 今日精选

### 3. 新 benchmark 显示最强 AI Agent 连日常任务都做不可靠，还会引入新问题

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Rebecca Bellan / TechCrunch_

TechCrunch 报道了一个针对个人 AI 助手的新 benchmark，结论是即使最先进的模型，在完成日常任务时也无法稳定、安全地交付，甚至会引入原本不存在的新问题。这条对你做 content-curator 有直接参考价值——它说明 Agent 的失败模式不在「能不能做」，而在「做的时候会不会搞出新麻烦」。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 新 benchmark 专门评测 AI Agent 在日常生活任务上的完成率与安全性 | benchmark 的具体任务集与评分方法未在报道中完整披露，复现性待验证 |
| 结论是当前最强模型也无法可靠完成日常任务 | 「引入新问题」的严重程度分级不明，是数据污染还是真实世界副作用 |
| 评测同时记录了 Agent 在执行过程中引入的新问题（side effects） | 是否会被 OpenAI / Anthropic / Google 引用为下一代模型的优化目标 |
| 报道时间 11 月 24 日，与 Walmart 接入 Meta Muse、Meta 把 Muse 塞进 Instagram DM 同期 | 个人助手场景的失败率是否显著高于编码场景，报道未做对比 |

**📖 主编点评**

这条应该直接改变你 content-curator 的设计思路：不要只测「Agent 能不能选出好稿」，要专门测「Agent 会不会把不该推的稿推出去、会不会重复推、会不会在失败时静默跳过某个域」。给你的 Agent 加一个 side-effect 检查层（比如推送前的 domain 覆盖断言），比再调一轮 prompt 更能提升可靠性。

📺 [打开原文](https://techcrunch.com/2026/11/24/even-the-best-ai-agents-struggle-with-everyday-life/)

---

### 4. Amazon 以 75 亿美元收购 Decart，赌软件能缩小与 Nvidia 的芯片差距

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Anna Heim / TechCrunch_

Amazon 收购 Decart，报道价 75 亿美元，目的是提升自家 Trainium 芯片的效率。TechCrunch 的框架很清楚：这不是买模型，是买「用软件榨干自研硅片」的能力。同期 Google DeepMind 用 AlphaProof Code 形式化验证了 Signal 的加密协议，两件事指向同一个方向——算力竞争正在从硬件转向软硬协同。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Amazon 收购 Decart，报道价 75 亿美元（TechCrunch） | 75 亿美元价格是否属实，TechCrunch 用的是 reported，未见双方官方确认 |
| 收购目标明确为提升 Trainium 芯片效率 | Decart 的软件优化能否实质缩小与 Nvidia 的代际差距，还是只是营销叙事 |
| Google DeepMind 的 AlphaProof Code 完成了 Signal 加密协议的数学证明（Tom's Hardware 11 月 25 日） | Trainium 的实际客户采用率与 Nvidia 的差距，报道未给数字 |
| 同期 Oracle 发行 200 亿美元股票与债券为 AI 基建融资 | AlphaProof Code 的形式化验证能否推广到通用软件正确性证明，目前只看到一个案例 |

**📖 主编点评**

如果你以后想做推理优化方向，这条给了你一个明确的技能坐标：软硬协同（编译器、算子融合、量化）比纯算法调参更值钱。你电子信息工程的背景在这里是优势——懂一点硬件约束再写 CUDA/Triton，比纯 CS 出身的人更容易进这类团队。

📺 [打开原文](https://techcrunch.com/2026/11/24/amazons-decart-acquisition-is-a-bet-on-using-software-to-narrow-the-silicon-gap-with-nvidia/)

---

## 📋 备选阅读

- [Microsoft 因 Outlook 近 24 小时宕机内部宣布「Code Red」](https://www.theverge.com/news/1042025/microsoft-code-red-outlook-outage) —— 大厂基础设施可靠性问题，对做 Agent 的人是提醒：你的依赖链上游随时会断，要有降级方案。
  _The Verge_
- [Walmart 把黑五折扣接进 Meta 的 AI Agent Muse](https://techcrunch.com/2026/11/24/walmart-teams-up-with-meta-to-bring-black-friday-deals-to-ai-agent-muse/) —— Agent 商业化落地的真实案例，但本质是渠道合作，工程细节为零，放备选。
  _TechCrunch_
- [Meta 把 Muse AI 助手直接塞进 Instagram 私信](https://techcrunch.com/2026/11/24/meta-brings-its-muse-ai-assistant-directly-into-instagram-dms/) —— 和上一条同属 Meta Agent 分发策略，两条可以合并看：Meta 在把 Agent 铺到所有有流量的入口。
  _TechCrunch_
- [Tidal 将下架数百万首全 AI 生成曲目](https://techcrunch.com/2026/11/24/tidal-to-ban-and-remove-millions-of-ai-generated-tracks-as-ai-slop-inundates-music-streaming/) —— 平台开始对 AI 生成内容做质量分层（辅助可以，全生成不行），这个标准未来可能被内容平台普遍采用。
  _TechCrunch_
- [Uber 与 Nuro 开始在旧金山湾区公开道路测试 Lucid 无人出租车](https://techcrunch.com/2026/11/24/uber-and-nuro-begin-driverless-testing-of-lucid-robotaxis-ahead-of-2027-launch/) —— 2027 年上线前的实测阶段，对 Robotaxi 时间表是个正向信号，但离你太远。
  _TechCrunch_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
