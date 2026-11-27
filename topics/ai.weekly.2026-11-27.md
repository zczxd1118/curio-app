# Curio · AI · 2026-11-27

> 今日 1 条头条 + 3 条备选

_今天最重的信号来自 Nvidia：Jensen Huang 被董事会重新任命为 CEO，同时公司暂停向东南亚出货、SEC 调查会计问题、S&P 考虑下调信用评级——一家公司的治理风险正在变成整个 AI 算力供应链的风险。另一条线是 Anthropic 上市后跌破 83 美元发行价，AI 资本叙事第一次出现公开市场的反向定价。对做 Agent 的你来说，工具链层面真正的新东西是 T3 Code 这类多 Agent 并行工作台。_

---

## 🌟 今日精选

### 4. T3 Code 开源 AI IDE 实测：一条指令拉起多个 Agent 线程并行改代码，统一调度 Claude Code 与 Codex

**[AI]** · ⭐⭐⭐⭐ · _AI超元域_

T3 Code 是一个开源 AI IDE，核心能力是把 Claude Code、Codex、Pi、Antigravity 等订阅统一装进一个工作台，用一条指令并行拉起多个 Agent 线程处理同一项目，并支持手机下发任务。视频发布于 11 月 24 日，是目前少见的、带完整安装配置到多 Agent 工作流实战的中文内容。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| T3 Code 为开源项目，支持统一调度 Claude Code、Codex、Pi、Antigravity 等多个 AI 编程后端 | 多 Agent 并行改同一项目时代码改动如何隔离，视频提出这个问题但未给出完整工程答案 |
| 支持一条指令并行启动多个 Agent 线程处理同一项目 | 「比 Orca 更好用」是 UP 主主观判断，缺少横向基准 |
| 支持从手机端下发任务 | 并行线程的实际 token 消耗与冲突解决成本没有量化数据 |
| 视频包含从安装配置到多 Agent 工作流实战的完整演示 | 项目成熟度与长期维护情况未知，开源仓库活跃度需自行核实 |
| 发布时间为 2026 年 11 月 24 日，属本周新内容 | 手机下发任务的链路是否稳定、是否需要自建中转，视频未展开 |

**📖 主编点评**

这条正对你的痛点：你在做 content-curator，多 Agent 分工（抓取 / 筛选 / 写作）是迟早要碰的。T3 Code 值得花一个晚上装一遍，重点不是用它写业务代码，而是观察它怎么隔离并行 Agent 的文件改动——这个设计思路可以直接搬到你的项目里。看的时候跳过安装段，直接看多线程冲突处理那部分。

📺 [打开原文](http://www.bilibili.com/video/av117671802705979)

---

## 📋 备选阅读

- [Claude Code 从 0 到 1 全攻略：权限、MCP、Skills、Hooks、子智能体](http://www.bilibili.com/video/av117642291582518) —— 11 月 19 日发布，覆盖你关心的 Skills / Hooks / Subagents 全链路。内容对路但属教程合集，密度不如头条那条 T3 Code 实测。
  _大模型分享员_
- [一期视频搞懂 58 个 AI 术语：从大模型到 Agent、MCP、Skill](http://www.bilibili.com/video/av117587144940374) —— 11 月 9 日发布，术语梳理做得细，最后用真实模型更新日志做练习这个设计不错。对你偏基础，但可以转给刚入门的人。
  _亚里今天也要AI_
- [DeepSeek Harness 与 Claude Code 同模型对比实测](http://www.bilibili.com/video/av117100337236191) —— 用同一个 DeepSeek 模型在两个 harness 里跑同样任务，结论是工具链影响大于模型。观点对你有用，但发布于 8 月，新颖度不够。
  _程序员晓刘_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
