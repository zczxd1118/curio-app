# Curio · AI · 2026-10-19

> 今日 1 条头条 + 5 条备选

_今天最值得看的是两条互相咬合的线：一是 AI 资本叙事开始松动——Anthropic 估值被砍 5000 亿美元、Firmus 的 300 亿 IPO 48 小时崩盘、CoreWeave 创始人套现 33 亿，钱在往回收；二是模型侧仍在推进——Gemini 4 Argon 系列铺到机器人、星际争霸，Replit 把默认模型从 Anthropic 换成 OpenAI。工程侧则有一个很具体的信号：Claude Code 每轮对话先 gzip 压缩再送模型。_

---

## 🌟 今日精选

### 5. Claude Code 每轮对话先 gzip 压缩再送模型，以及 GPT-6 Astra Pro 的并行智能体

**[AI]** · ⭐⭐⭐⭐ · _kate人不错_

这期 AI 周更里有一条很具体的工程细节：Claude Code 在每轮对话中先把上下文 gzip 压缩再送到模型，以换取更快的响应。同一条还提到 GPT-6 Astra Pro 升级后支持多个智能体并行干活、插件与工具调用变好。信息密度高于多数中文 AI 周报。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Claude Code 每轮对话先 gzip 压缩上下文再送模型，用于提速 | gzip 压缩的具体实现（压缩比、是否影响长上下文召回）未披露 |
| ChatGPT 内 GPT-6 Astra Pro 升级，回复更快、工具调用更好 | 并行智能体的调度方式与计费口径不明 |
| GPT-6 Astra Pro 支持多个智能体并行执行 | 提速幅度缺少基准数字 |
| Claude Slides 被 Boris Cherny 用于制作幻灯片，支持截图批注自动套壳 | 这些细节来自二手转述，建议回看原视频确认 |
| Grok Bot 同期有更新 |  |

**📖 主编点评**

gzip 这一条值得你直接抄进 content-curator：上下文压缩是低成本提速手段，尤其在你这种多轮抓取+总结的 Agent 里。可以先用简单的 zlib 压缩历史消息做 A/B，看 token 数与延迟的实际变化。另外，并行智能体是 GPT-6 的新能力，值得在你的抓取阶段试一次 fan-out。

📺 [打开原文](http://www.bilibili.com/video/av117453497566792)

---

## 📋 备选阅读

- [Vibe Coding 有哪些高效的做法习惯？](http://www.bilibili.com/video/av117447894045979) —— 跳出提示词技巧，讲 Token 消耗爆炸、Agent 找不准代码、结果不稳定的工程侧解法，契合你的信号偏好。
  _AAA话题批发_
- [Agent-native 开发 [08-Raw/26生成式软件工程/NJU]](http://www.bilibili.com/video/av117432811260250) —— 南大课程录像，讲 Agent-native 开发范式，学术视角稀缺，但信息密度需自行筛。
  _绿导师原谅你了_
- [一个人有四种身份，我给电脑配了一个AI管家](http://www.bilibili.com/video/av117404021626807) —— 用真实任务测 Marvis 接管电脑状态与本地文件，是少见的「个人 Agent 实战」而非教程。
  _三太子敖丙_
- [开源安卓 AI Agent：RikkaHub Agent Pure 能看懂屏幕并操作 App](http://www.bilibili.com/video/av117394643097499) —— 无障碍屏幕自动化 + 专家团系统，AGPL-3.0 开源，可读代码，适合研究移动端 Agent 架构。
  _补药满减哇_
- [连 json 都不会，进了福布斯团队：面试才知道 vibe coding 是什么](http://www.bilibili.com/video/av117436686795057) —— 个人叙事而非技术内容，但反映了 vibe coding 正在改变招聘标准，可作行业侧写。
  _揽星Celeste_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
