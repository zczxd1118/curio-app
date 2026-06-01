# Curio · AI · 2026-06-01

> 今日 1 条头条 + 0 条备选

_今天三条主线交叉：一是 OpenAI 计划本周递交 IPO 招股书，叠加 SpaceX 1.8 万亿美元 IPO 倒逼指数规则改写，AI 独角兽集体进入定价时刻；二是 Computex 2026 + GTC Taipei 同步开锣，Nvidia Vera Rubin 量产 + N1X PC 处理器入场，Intel 18A Xeon 6+ 反扑，AI 硬件竞争从 GPU 蔓延到 CPU/PC 全栈；三是股票域：SpaceX IPO 招股书极度不公平条款（禁止股东诉讼、Musk 永久控制），多家媒体警告散户慎打新——这是 2026 年下半年股市最大的风险事件。Stratechery 本周新增 Eric Seufert 访谈值得你听完。_

---

## 🌟 今日精选

### 5. Claude Code Workflow 隐藏功能首测：脚本化 + 多 Agent 协同的可复用工作流

**[AI]** · ⭐⭐⭐⭐ · _AI超元域_

Anthropic 在 Claude Code V2.1.47 / 48 秘密上线了 Workflow 功能，被官方从 Changelog 删除但代码里还在。这条 B 站视频是目前最早的实测，演示三个阶段六种形态：自动生成 JS 脚本、ultrawork 召唤多 Agent 协同、可复用的精准可控工作流。对你这种自己用 Claude Code 写 Agent 项目的人，是把 "一次性 prompt" 升级到 "工程化工作流" 的关键转折。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Claude Code V2.1.47 / V2.1.48 已包含 Workflow 代码（B 站 5/24 实测） | 因为官方未官宣，API 与稳定性可能在后续小版本被改 |
| Workflow 支持脚本化（自动生成 JS）、多 Agent 协同（ultrawork）、可复用模板 | ultrawork 召唤的多 Agent 是否真有 token 节省 / 还是单纯多轮拆解，缺独立 benchmark |
| Anthropic 官方未在 Changelog 公布，目前是 "半地下" 功能 | 对接 Skills 体系后是否会和 WorkBuddy 当前的 skill / subagent 模式撞车，需要你自己 diff |
| 另一条相关视频：Simon 林《Claude Code 多 Agent 模式实战》验证 subagents + 独立 agent 两种模式（4/23） |  |

**📖 主编点评**

你 content-curator 已经在用 Skills + automation，这个 Workflow 功能正好补上 "多步任务可复用" 的缺口。建议这周抽 30 分钟把视频里的 ultrawork demo 跑一遍，然后对照你现有的 cli_generate prepare_unified → finalize_unified 这条链路，看能不能把脚本逻辑搬到 Claude Code 里——如果能，每周一的 daily automation 就可以变成 Claude 直接驱动。

📺 [打开原文](http://www.bilibili.com/video/av116629702777532)

---

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
