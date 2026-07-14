# Curio · AI · 2026-07-14

> 今日 1 条头条 + 3 条备选

_今日最关键的信号是韩国股市因单股杠杆ETF踩踏暴跌后深V反弹，但去杠杆尚未出清，监管会议在即；同时苹果起诉OpenAI窃取商业机密，Siri AI公测版上线，AI竞争进入法律与产品双线战场。半导体方面，SK海力士预警2027年将是内存短缺最严重的一年，供给瓶颈持续至2030年。_

---

## 🌟 今日精选

### 4. 2026年过半，我是怎样使用Agent的？——调度sub-agent的实战经验

**[AI]** · ⭐⭐⭐⭐ · _卡普迪姆_

B站UP主分享了自己半年来的Agent使用心得，核心技巧是用Claude Code调度多个sub-agent，让Codex执行便宜模型（如GPT 5.5）来降低成本。视频包含具体的prompt架构和调度策略，对正在做content-curator项目的你很有参考价值。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| UP主使用Claude Code调度多个sub-agent | 这种多模型调度策略的稳定性有待长期验证 |
| 用Codex exec调用便宜的GPT 5.5模型降低成本 | GPT 5.5的便宜是否意味着质量下降？需要权衡 |
| 分享了调度sub-agent的提示词原图 | sub-agent之间的上下文传递可能成为瓶颈 |
| 参考了Theo的推文和mattpocock的skill库 | 该方法是否适用于非编程类Agent任务？ |

**📖 主编点评**

你的content-curator项目正好需要这种多Agent协作思路——用Claude Code做编排，Codex做执行，可以大幅降低API成本。建议你直接去B站看视频，重点抄作业调度prompt和sub-agent分工模式。但注意：不要照搬，要根据你的RAG流程调整上下文窗口大小。

📺 [打开原文](https://www.bilibili.com/video/av116887417522347)

---

## 📋 备选阅读

- [Claude Code多Agent模式实战分享](https://www.bilibili.com/video/av116454666012312) —— 介绍了Claude Code的两种多Agent模式（subagents和独立agent），对理解Agent架构有帮助，但内容较浅，适合入门。
  _Simon林__
- [别再二选一：Claude Code + Codex 联用才是最强姿势](https://www.bilibili.com/video/av116537746791000) —— 与头条4观点类似但更早发布，核心思路一致，可作为补充参考。
  _星小脉_
- [Claude code接管科研全流程：cc-kaiti 带你从 0 走到开题报告和答辩 PPT](https://www.bilibili.com/video/av116866278233889) —— 展示了Claude Code在科研场景的深度应用，但用户非科研背景，优先级降低。
  _做科研的大师兄_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
