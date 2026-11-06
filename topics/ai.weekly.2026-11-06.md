# Curio · AI · 2026-11-06

> 今日 1 条头条 + 2 条备选

_今天只有一个信号值得记住：美国中期选举把 AI 数据中心投成了政治议题，45 项地方公投几乎全数否决，纳指两天跌掉 5%、2.5 万亿美元市值蒸发，芯片股创 1896 年以来最差中期选举后表现。这不是技术问题，是 AI 基建的融资与选址逻辑被政治重定价。第二条线是 DeepSeek Harness 的 Super-agent 在中文社区持续发酵，工具链层面的竞争开始和模型本身脱钩。_

---

## 🌟 今日精选

### 4. DeepSeek Harness 开源 Super-agent 实测：和传统 Agent 差在哪，插件化工具链是不是真能提升效率

**[AI]** · ⭐⭐⭐⭐ · _程序员鱼皮_

DeepSeek Harness 团队开源的 Super-agent 在中文社区已经跑出一批实测。这条视频的价值是它没有停在「是什么」，而是拿同一个模型在 Claude Code 和 DSH 里跑相同任务，对比工具链对最终产出的影响——这正是你关心的「模型之外的那一半」。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DeepSeek Harness 团队开源了 Super-agent 项目 | 「工具链比模型更重要」这个结论目前只有小样本实测支撑 |
| 社区已有多个实测视频对比 DSH 与 Claude Code 的同任务表现 | DSH 的插件生态成熟度与 Claude Code 差距多大，尚无系统对比 |
| DSH 采用插件化架构，强调流程记录与缓存命中 | 开源协议与商用限制细节未在视频中展开 |
| 实测覆盖游戏 Demo、动画、源码流程等多类任务 | 长期维护是否跟得上，取决于 DeepSeek 团队投入 |

**📖 主编点评**

你正在做 content-curator，这条值得看的是「插件化 + 流程记录」这套设计思路，而不是照抄 DSH。建议你重点看它怎么记录 Agent 的中间步骤——这对你调试自己的子 Agent 编排会直接有用。看完可以拿你的项目跑一次同任务对比，成本很低。

📺 [打开原文](http://www.bilibili.com/video/av117564076202051)

---

## 📋 备选阅读

- [14k Star 的 Claude Code 开源桌面端 cc-haha：能自己看屏幕、操作 APP](http://www.bilibili.com/video/av117251936293145) —— Computer Use 的民间实现，工程细节可能对你有用，但基于泄露源码，合规性存疑。
  _程序员阿江-Relakkes_
- [OpenClaw 高级用法：用 Claude Code Hooks 回调 + Agent Teams 把轮询 Token 消耗压到接近零](http://www.bilibili.com/video/av116046157647899) —— Hooks 回调省 Token 是实打实的工程技巧，契合你的偏好，但发布时间较早（2 月），新颖度不足。
  _AI超元域_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
