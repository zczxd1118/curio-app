# Curio · AI · 2026-10-21

> 今日 1 条头条 + 4 条备选

_今天最值得看的两个信号：一是 AI 资本叙事开始松动——Anthropic 估值据报缩水 5000 亿美元、云算力合作变紧张、数据中心 IPO 接连崩盘，11 月 IPO 前的窗口很窄；二是工程侧的真进展，DeepMind 用四个 Gemini 4 Agent 27 小时通关 Minecraft、自己写了 2783 个程序，Agent 从演示走向可验证的长程任务。前者提醒你别把行业热度当个人判断，后者才是你该动手复现的东西。_

---

## 🌟 今日精选

### 5. DeepSeek V4.1 Flash 跑分反超旗舰，一条视频把六大 Agent 工具的接入配置全讲清

**[AI]** · ⭐⭐⭐⭐ · _跟着小陈玩AI_

DeepSeek 发布 V4.1 Flash，据称跑分反超一众旗舰模型。这条视频实测把它接进 DeepSeek Harness、WorkBuddy、Kimi Code、小米 MIMO、ZCode、Codex、Claude Code 等工具，给出两种配置方法、模型名怎么填、哪里会踩坑。对国内网络环境下做 Agent 的人来说，这是少见的「配置级」而非「概念级」内容。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DeepSeek 发布 V4.1 Flash，定位为轻量高速版本 | 「跑分反超旗舰」的具体 benchmark 与对比对象需自行核对，视频口径未必中立 |
| 视频覆盖 DeepSeek Harness、WorkBuddy、Kimi Code、小米 MIMO、ZCode、Codex、Claude Code 等接入 | 各工具对非官方端点的兼容性会随版本变化，配置可能很快失效 |
| 给出两种配置方法与模型名填写方式 | V4.1 Flash 在长上下文与工具调用上的稳定性，视频未给系统性数据 |
| 发布时间为 2026-10-18，属本周新内容 |  |
| 同期另有视频演示在 VSCode 中把 Claude Code 指向 DeepSeek 端点 |  |

**📖 主编点评**

这条对你最实用：content-curator 如果要做成本控制，把部分子 Agent 的推理切到 Flash 级模型是标准做法。建议你按视频配一遍，然后自己测三个指标——工具调用成功率、单次任务 token 数、超时率，这三个数才是你决定「哪个环节用哪个模型」的依据。

📺 [打开原文](http://www.bilibili.com/video/av117459403150912)

---

## 📋 备选阅读

- [Claude Code 四个阶段](http://www.bilibili.com/video/av117449504595834) —— 10 月 19 日新发，讲 Claude Code 使用能力进阶的四个阶段，短小但时间新，适合快速对照自己处在哪一档。
  _程序员牛牛学长_
- [从夯到拉，锐评 32 个 AI 编程工具](http://www.bilibili.com/video/av116578532200786) —— 覆盖 Cursor、Claude Code、Codex、Windsurf、Trae 等 32 款工具的横向实测，信息密度够，但属合集形态，放备选。
  _程序员鱼皮_
- [AI 产品经理作品集：Vibe Coding 实操 ChatBI 落地写进简历](http://www.bilibili.com/video/av117445360618053) —— 讲企业级项目如何用 vibe coding 落地，含 SDD 规范、Harness、测试用例、skill 设计，和你把 content-curator 写进简历的诉求高度重合。
  _AI产品经理PMGao_
- [开源安卓 AI Agent：RikkaHub Agent Pure 能看懂屏幕并自己操作 App](http://www.bilibili.com/video/av117394643097499) —— AGPL-3.0 开源，用无障碍控件树做屏幕自动化而非死坐标脚本，另有专家团分工机制，值得读源码。
  _补药满减哇_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
