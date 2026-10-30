# Curio · 大厂 AI 动态 · 2026-10-30

> 今日 2 条头条 + 5 条备选

_今天最硬的两个信号：一是 Anthropic 的 S-1 把 AI 公司的真实成本结构摊开了——89 亿美元半年算力账单里，大部分烧在 R&D 而不是服务客户，同时华尔街在质疑它的 IPO 估值；二是 AI 需求开始反向挤压硬件供应链，PCB 订单排到 2030 年、Intel Fab 28 爆炸让服务器 CPU 断供两个季度。前者是叙事，后者是物理约束，后者更值得你盯。_

---

## 🌟 今日精选

### 3. Gemini 4 Carbon 登顶 Artificial Analysis 智能指数 v5，Google 一周内连发 Argon 与 Carbon 两代

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Hacker News / Artificial Analysis_

Google 在 10 月底连续放出 Gemini 4 Argon 和 Gemini 4 Carbon，Carbon 直接拿下 Artificial Analysis Intelligence Index v5 第一。一周两代模型，加上 Genie 4 世界模型同期发布，说明 DeepMind 的发布节奏已经从「季度级」压到「周级」。对做 Agent 的人来说，模型选型的半衰期正在肉眼可见地缩短。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 4 Carbon 在 Artificial Analysis Intelligence Index v5 上排名第一 | 榜单第一与实际 Agent 任务表现的差距，仍需自测验证 |
| Gemini 4 Argon 于 9 月底发布，Carbon 于 10 月 28 日发布 | Carbon 相对 Argon 的具体架构改动未公开 |
| 同期 DeepMind 发布 Genie 4 世界模拟模型 | 一周两代是否意味着内部存在并行实验线，还是营销节奏，无法确认 |
| Gemini 4 Argon 已有面向机器人的专门版本 | 定价与速率限制是否同步调整，报道未涉及 |

**📖 主编点评**

你的 content-curator 如果绑定了具体模型，现在就该把模型层做成可替换的抽象，别硬编码。另外，榜单排名对你选型的参考价值有限——真正该测的是你的实际任务上的通过率和 token 成本，花半小时跑一遍自己的 eval 比看榜单有用。

📺 [打开原文](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)

---

### 4. Ben Thompson 对话 Palantir CTO Shyam Sankar：AI 的「宗教战争」、前置工程师与扩散之争

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Stratechery_

这期访谈的核心不是产品，是路线之争：Sankar 把当前 AI 圈的分歧描述成一场宗教战争——一边相信模型能力会自然扩散，一边相信必须靠前置工程师把 AI 嵌进真实业务。Palantir 押的是后者，这也是它估值逻辑的根基。对做 Agent 的人，这场争论直接对应「通用 Agent 还是垂直工作流」的选择。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 访谈对象为 Palantir CTO Shyam Sankar，主持人为 Ben Thompson | Sankar 的立场带有明显的公司利益色彩，需打折听 |
| 讨论主题包括 AI 扩散、安全、forward-deployed engineer 模式 | 「扩散 vs 落地」的二分法可能过度简化，实际是混合路径 |
| Sankar 将当前技术路线分歧定性为「宗教战争」 | 访谈未给出 Palantir 具体项目的量化效果数据 |
| Palantir 的核心方法论是派工程师进驻客户现场做落地 | 前置工程师模式的可复制性与成本结构未被深入讨论 |

**📖 主编点评**

你做 content-curator 时其实就在选边：是做一个通用 Agent 让用户自己调，还是把某个具体工作流（比如选题、去重、评分）做到极致。Sankar 的论点值得听，但别全信——个人项目没有前置工程师，你的优势恰恰是把一个窄场景做到别人懒得做的深度。

📺 [打开原文](https://stratechery.com/2026/an-interview-with-palantir-cto-shyam-sankar-about-the-ai-religious-war/)

---

## 📋 备选阅读

- [Mistral 开源万亿参数模型权重，主打网络安全场景](https://techcrunch.com/2026/10/29/mistral-releases-weights-for-its-trillion-parameter-ai-model-targeting-cybersecurity/) —— 万亿参数还放权重，欧洲厂在开源路线上继续加注，值得关注其实际可部署性。
  _TechCrunch_
- [Amazon 内部新规：禁止工程师「tokenmaxxing」刷 AI 使用量](https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-tells-engineers-to-stop-tokenmaxxing-to-look-productive-says-ai-will-be-central-to-software-development-but-usage-is-not-the-goal-new-guidelines-claim) —— 大厂开始反思「AI 使用率」这类虚荣指标，对做 Agent 评测的人是个方法论提醒。
  _Tom's Hardware_
- [Gemini 聊天内可直接生成并编辑 Google Docs、Sheets、PDF 与代码文件](https://www.theverge.com/ai-artificial-intelligence/1022519/google-gemini-file-editing-documents-pdfs) —— Gemini 从对话走向文档工作区，这是 Agent 产品形态的一次正面挤压。
  _The Verge_
- [Reddit 宣布转向「强制登录」体验，CEO 称 Google AI Mode 不带来流量](https://techcrunch.com/2026/10/29/as-search-traffic-dries-up-reddit-announces-its-shifting-to-a-logged-in-experience/) —— 开放网络被 AI 搜索抽干流量的标志性事件，内容平台的商业模式正在被迫重构。
  _TechCrunch_
- [Waymo 联手 Toyota，用 bZ4X 进军日本与英国 robotaxi 市场](https://techcrunch.com/2026/10/30/waymos-next-robotaxi-will-be-a-toyota-bz4x-destined-for-japan-and-the-uk/) —— Waymo 首次走出美国，选 Toyota 而非自研车型，是规模化路线的务实转向。
  _TechCrunch_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
