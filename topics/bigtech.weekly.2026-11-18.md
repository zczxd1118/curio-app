# Curio · 大厂 AI 动态 · 2026-11-18

> 今日 1 条头条 + 3 条备选

_今天真正的信号只有一个：Nvidia 的权力交接已经落地成事实——董事会明确表态不打算让 Jensen Huang 回归，同时公司宣布退出中国市场、继续推进收购 Hugging Face、并给出继续增长的营收指引。围绕这条主线，Anthropic IPO 的信用评级与估值争议、以及 AI 资本市场的整体回撤，是第二层信号。AI 编程工具侧今天没有硬新闻，候选池里多是教程存量，我按你的口味只挑了有工程细节的。_

---

## 🌟 今日精选

### 3. Microsoft 在 Ignite 上把 Copilot 定义成「工作的新操作系统」，Office 反过来跑在它里面

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Nick Indge_

Ignite 主题演讲里 Microsoft 给出的定位变化值得注意：不再是「Office 里加一个 AI 助手」，而是 Word、Excel、PowerPoint 作为组件运行在 Copilot 之内，下一步是常驻的 always-on agent。这是产品架构层面的重排，不是功能叠加。对做 Agent 的人来说，这意味着微软在赌「Agent 是宿主、应用是工具」这一侧。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Microsoft 在 Ignite 主题演讲中称 Copilot 为「the new OS for work」 | always-on agent 的计费方式、权限模型与失败回滚机制均未公布 |
| Word、Excel、PowerPoint 现在作为组件运行在 Copilot 内部 | 「应用跑在 Copilot 里」目前是产品叙事还是已落地的架构，需要看实际客户端行为 |
| 官方宣布下一步方向是 always-on agents（常驻代理） | 企业侧的合规与数据驻留方案没有细节，这通常决定大客户是否采用 |
| 同一周 Anthropic 也发布了对应的操作系统级更新，两家形成对打 |  |

**📖 主编点评**

这条和你的 Agent 项目直接相关：微软在押「宿主 + 工具」的架构，和你用 MCP 把外部能力挂到 Claude Code 上的思路是同一个方向，只是层级不同。建议你关注它的权限模型怎么设计——always-on agent 最大的工程难题不是能力，而是「它在你不在的时候能做什么」。这正是你项目里迟早要回答的问题。

📺 [打开原文](https://arstechnica.com/gadgets/2026/11/microsoft-calls-copilot-the-new-os-for-work-at-ignite-keynote/)

---

## 📋 备选阅读

- [Satya Nadella 说他现在是「AGI-pilled」](https://www.theverge.com/tech/1036111/satya-nadella-says-hes-agi-pilled-now) —— Nadella 谈 AGI 对经济结构与政治的影响，属于你要的 KOL 深度对话。今天头条位置被更硬的事实占了，放备选。
  _Nilay Patel_
- [Stratechery：Nvidia 财报、Office 融合、AI 版操作系统战争](https://stratechery.com/2026/nvidia-earnings-office-convergence-os-wars-ai-edition/) —— Ben Thompson 把 Nvidia 财报、微软与 Anthropic 的操作系统级更新串成一条线。是今天最好的框架性解读，但属评论而非新事实。
  _Ben Thompson_
- [Google 将 Gemini 聊天记录保留期从 72 小时延长到 2 个月，即使关闭历史记录](https://techcrunch.com/2026/11/17/google-to-keep-gemini-chats-for-two-months-up-from-72-hours-even-with-history-off/) —— 隐私默认值的一次实质后退，与 HN 上「Gemini 把个人 Drive 文件路由给人工标注员」是同一类问题，值得你知道。
  _Jagmeet Singh_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
