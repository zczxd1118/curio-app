# Curio · 大厂 AI 动态 · 2026-11-19

> 今日 1 条头条 + 3 条备选

_今天最重要的信号有两个：一是 Nvidia 在黄仁勋辞职后首次交出季报，营收 1158 亿美元、利润依旧强劲，但董事会明确不打算让黄回归，公司进入「后黄仁勋时代」的过渡期；二是 Anthropic 以每股 83 美元、1.5 万亿美元估值完成 IPO 定价，AI 一级市场的泡沫争论被推到台前。对做 Agent 的你来说，今天还有一条值得细读的工程实践：用三块二手 V100 跑出 100 tok/s 的家庭实验室方案，成本只要 1042 美元。_

---

## 🌟 今日精选

### 3. Ben Thompson 对话 Eric Seufert：Agentic Commerce 为什么最终会回到广告模式

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _Stratechery_

Stratechery 本期访谈请来 Mobile Dev Memo 的 Eric Seufert，主题是 agentic commerce。核心论点：当 AI Agent 替用户比价、下单，广告不会消失，而是从「对人展示」变成「对 Agent 竞价」；零售商真正的护城河是「愿意为 Agent 优化商品数据」的能力。这是本周对「Agent 如何改变互联网经济」最系统的一篇长访谈。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 访谈对象 Eric Seufert 是 Mobile Dev Memo 主笔，长期跟踪移动广告与变现结构 | 「Agent 竞价广告」的定价机制尚无真实市场验证，目前是推演 |
| 核心判断：Agent 购物不会消灭广告，而是把广告库存从展示位转向「Agent 可读的商品数据」 | 零售商开放商品数据给第三方 Agent 的动力，取决于流量分成怎么谈，访谈未给具体方案 |
| Ben Thompson 在文中提出零售商应主动「为 Agent 优化」商品目录与库存 API | 监管层（FTC、欧盟 DMA）对 Agent 比价是否构成「自动化合谋」尚未表态 |
| 讨论覆盖 Amazon、Google Shopping 和独立 DTC 品牌在 Agent 时代的相对位置 | 中小独立站能否负担 Agent 优化成本，可能加剧而非缓解平台集中度 |

**📖 主编点评**

你正在做 content-curator 这个 Agent 项目，这篇访谈直接相关：它讨论的「Agent 读什么数据、怎么被喂数据」就是你设计 MCP 工具时的接口哲学。建议你边读边记一个问题——如果你的 Agent 要替用户筛选内容，你会把「广告/推广内容」的标识放在 schema 的哪一层？这个设计决策以后会变成产品差异点。

📺 [打开原文](https://stratechery.com/2026/an-interview-with-eric-seufert-about-agentic-commerce/)

---

## 📋 备选阅读

- [Gemini 4 Neon 发布，被评「看起来像 Opus 5.5 的竞争对手」](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/) —— 11 月 18 日发布，HN 854 分，是本周最新的模型发布，但摘要信息有限，适合先记名字、等评测。
  _Google Blog_
- [Snapchat 允许开发者用 Claude Code 和 Cursor 构建 AR Lens](https://techcrunch.com/2026/11/18/snapchat-now-lets-developers-build-ar-lenses-with-ai-coding-assistants-like-claude-code-and-cursor/) —— 平台级动作：Snap 把 AI 编程助手接进 AR 创作流程，是「Vibe Coding 进入垂直平台」的早期信号。
  _TechCrunch_
- [微软 CEO Nadella：AI Agent 将重塑互联网经济，广告模式受冲击](https://techcrunch.com/2026/11/18/satya-nadella-predicts-ai-agents-will-reshuffle-the-economics-of-the-web/) —— Nadella 在 DealBook 上的判断，和 Stratechery 那篇访谈互为印证，但信息密度低于长访谈，放备选。
  _TechCrunch_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
