# Curio · AI · 2026-10-19

> 今日 1 条头条 + 1 条备选

_今天最重要的信号是 AI 资本叙事开始出现裂缝：OpenAI 年化收入比此前对外暗示的低 200 亿美元，Anthropic 估值据报缩水 5000 亿，Firmus 的 300 亿美元 IPO 在 48 小时内崩掉——算力基建的钱开始被重新定价。另一条线是 Anthropic 一边把 5% 股份捐给公益基金、一边给外部监督机构「准员工级」权限，AI 治理从口号进入可审计阶段。_

---

## 🌟 今日精选

### 4. GPT-6 Astra Pro 升级、Claude Code 每轮对话先 gzip 压缩再送模型，本周模型侧三个工程细节

**[AI]** · ⭐⭐⭐ · _kate人不错_

这期周更汇总了三条有工程含量的动态：ChatGPT 里的 GPT-6 Astra Pro 升级后支持多智能体并行；Claude Code 每轮对话先把上下文 gzip 压缩再送模型以降低延迟；Claude Slides 支持在截图上留言自动套模板。其中 gzip 压缩上下文这条最有信息量——它说明上下文工程的优化点已经从「少放 token」转向「压缩传输」。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| GPT-6 Astra Pro 在 ChatGPT 内升级，支持多智能体并行 | gzip 压缩的具体压缩比与延迟收益未给出数字 |
| Claude Code 每轮对话先 gzip 压缩再送模型 | 多智能体并行的调度策略与失败回退机制不明 |
| Claude Slides 支持截图批注自动生成版式 | 这些改动是否已全量推送尚不确定 |
| Grok Bot 同期更新八条帖子 |  |

**📖 主编点评**

Claude Code 的 gzip 做法你可以直接抄进自己的 Agent 项目：在把长上下文塞进 prompt 前先做一次无损压缩，尤其是重复的代码文件和工具返回结果。这是低成本、可立刻验证的推理优化点，比换模型便宜。

📺 [打开原文](http://www.bilibili.com/video/av117453497566792)

---

## 📋 备选阅读

- [Vibe Coding 有哪些高效的做法习惯？](http://www.bilibili.com/video/av117447894045979) —— 讲 token 消耗爆炸、Agent 找不准代码、结果不稳定这些真实痛点，比教程类内容密度高，但标题太泛。
  _AAA话题批发_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
