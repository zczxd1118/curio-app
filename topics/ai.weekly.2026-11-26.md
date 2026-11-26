# Curio · AI · 2026-11-26

> 今日 1 条头条 + 2 条备选

_今天真正的信号是 Nvidia 治理危机进入第二阶段：Jensen Huang 被董事会火速复职，但 S&P 已在考虑下调其信用评级，国会、SEC 与 Polymarket 异常交易同时压上来，AI 算力叙事第一次被公司治理而非需求打断。另一条主线是 Anthropic IPO 破发——$83 发行价上市后迅速跌破，$1.5T 估值被市场当场打折，AI 泡沫的定价开始由二级市场说了算。_

---

## 🌟 今日精选

### 4. T3 Code：开源 AI IDE，一条指令拉起多个 Agent 线程并行改代码，统一调度 Claude Code 与 Codex

**[AI]** · ⭐⭐⭐⭐ · _AI超元域_

T3 Code 是这两天 B 站上少见的、有真实工程细节的 Agent 工具内容：手机下发任务、一条指令并行拉起多个 AI 线程、统一调度 Claude Code / Codex / Pi / Antigravity，核心卖点是「代码改动如何隔离」。11 月 24 日发布，正好卡在你关注的 MCP / 子 Agent 方向上。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| T3 Code 是开源项目，视频演示了安装配置到多 Agent 工作流的完整流程 | 多线程并行改同一项目时的代码隔离机制，视频只做了演示，未给冲突合并的完整方案 |
| 支持一条指令并行拉起多个 AI 线程处理同一项目 | 开源协议与长期维护意愿未在简介中说明 |
| 可统一调度 Claude Code、Codex、Pi、Antigravity 等已有订阅 | 与 Orca 的对比是 UP 主主观判断，缺独立基准 |
| 支持手机端下发任务 | 手机下发任务的实现方式（自建中继还是第三方）未披露，涉及安全边界 |
| 视频发布于 2026-11-24，属于本周新内容 |  |

**📖 主编点评**

这正是你 content-curator 项目可以直接借鉴的架构参照：多个子 Agent 并行跑任务、统一调度、结果隔离。建议你花一个周末把 T3 Code 跑起来，重点看它怎么处理并行改动的冲突——这个问题的解法，比任何「10 个最强工具」的合集都有价值。

📺 [打开原文](http://www.bilibili.com/video/av117671802705979)

---

## 📋 备选阅读

- [Claude Code 从 0 到 1 全攻略：环境、权限、MCP、Skills、子智能体、Hooks 一次讲透](http://www.bilibili.com/video/av117642291582518) —— 11 月 19 日的新内容，覆盖你要的 Skills / Hooks / 子 Agent 全套，但属于教程合集，密度不如 T3 Code 那条。
  _大模型分享员_
- [DeepSeek Harness 实测对比 Claude Code：同一模型，工具链差距比想象大](http://www.bilibili.com/video/av117100337236191) —— 「模型重要还是 Harness 重要」的实证对比，结论对你的 Agent 架构选型有参考，但发布于 8 月，新颖度不足。
  _程序员晓刘_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
