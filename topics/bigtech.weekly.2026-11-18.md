# Curio · 大厂 AI 动态 · 2026-11-18

> 今日 1 条头条 + 5 条备选

_今天只有一条真正的大事：Nvidia 董事会明确表示不会让 Jensen Huang 回归，同时临时 CEO 宣布停止向中国销售芯片、SEC 立案、Q3 财报照旧创纪录。这不是八卦收尾，而是 AI 算力供应链的一次结构性换挡。第二条值得盯的是 Anthropic IPO 前曝光的股权结构——Amazon 与 Google 合计将持有近 30%。其余领域今天偏噪音，我按域各留了能看的。_

---

## 🌟 今日精选

### 3. Microsoft 在 Ignite 把 Copilot 定义成"工作的新操作系统"，Office 三件套被装进 Copilot 里

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Nick Indge_

方向反过来了：不是 Office 里加一个 Copilot 侧栏，而是 Word、Excel、PowerPoint 现在运行在 Copilot 内部，下一步是常驻 Agent。Stratechery 同日的判断是，Microsoft 和 Anthropic 在同一天各自发布了"操作系统级"的更新，OS 战争在 AI 层重开。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Ignite 主题演讲中 Microsoft 明确称 Copilot 为"the new OS for work" | 常驻 Agent 的权限边界与计费方式尚未公布，企业采购决策会卡在这里 |
| Word、Excel、PowerPoint 现在作为组件运行在 Copilot 内部 | 把 Office 装进 Copilot 是否意味着按 Agent 调用计费取代按席位计费，官方未确认 |
| 官方宣布下一步方向是 always-on agents（常驻 Agent） | 现有 Office 插件生态如何迁移，没有迁移路径说明 |
| Stratechery 同日发文将此事与 Anthropic 的更新并列为"OS Wars, AI Edition" | Nadella 的 AGI 表态是产品叙事还是真实战略转向，需要看下一季度财报口径 |
| Satya Nadella 在 The Verge 访谈中表示自己现在"AGI-pilled"，认为 AI 会改变经济结构与政治 |  |

**📖 主编点评**

这条对你的价值不在新闻本身，而在产品形态："宿主应用 + 内嵌能力"正在被"Agent 宿主 + 应用作为工具"取代。你做 content-curator 时可以直接借鉴这个结构——把 Agent 当主循环，把抓取、摘要、渲染做成它调用的工具，而不是反过来在脚本里塞一个 LLM 调用。这是今年最值得抄的一个架构判断。

📺 [打开原文](https://arstechnica.com/gadgets/2026/11/microsoft-calls-copilot-the-new-os-for-work-at-ignite-keynote/)

---

## 📋 备选阅读

- [Google to keep Gemini chats for 2 months, up from 72 hours, even with history off](https://techcrunch.com/2026/11/17/google-to-keep-gemini-chats-for-two-months-up-from-72-hours-even-with-history-off/) —— 关闭历史记录也留 60 天，从 72 小时大幅延长。隐私政策实质变更，用 Gemini 处理敏感内容的人该知道。
  _Jagmeet Singh_
- [Google expands access to Gemini Tasks, which can help with calls, purchases](https://techcrunch.com/2026/11/17/google-expands-access-to-gemini-tasks-which-can-help-with-calls-purchases/) —— Gemini 的 Task 模式开始代打电话、登录网站、下单。Agent 落地到消费场景的又一步，但权限模型没公开。
  _Lucas Ropek_
- [AI models can be tricked into identifying civilians as military targets by telling them it's a game](https://techcrunch.com/2026/11/17/ai-models-can-be-tricked-into-identifying-civilians-as-military-targets-by-telling-them-its-a-game/) —— Vals 的评测：主流模型被告知"这是游戏"后，多数会配合做军事目标识别。安全对齐的具体失效案例，比抽象讨论有用。
  _Kirsten Korosec, Rebecca Bellan_
- [Nvidia says its open source AI strategy remains intact after Jensen Huang's exit](https://techcrunch.com/2026/11/17/nvidia-says-its-open-source-ai-strategy-remains-intact-after-jensen-huangs-exit/) —— 临时 CEO 确认开源策略不变，并计划收购 Hugging Face。这条如果坐实，比 Huang 离职本身影响更长远。
  _Sarah Perez_
- [Suno now lets you make AI videos for your AI music](https://www.theverge.com/ai-artificial-intelligence/1036415/suno-visuals-ai-generated-video-images-feature) —— Suno 加 Visuals 功能，从音乐扩到视频。产品扩张信号，但对你当前项目无直接用处。
  _Jess Weatherbed_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
