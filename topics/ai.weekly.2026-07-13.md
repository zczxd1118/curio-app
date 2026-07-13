# Curio · AI · 2026-07-13

> 今日 1 条头条 + 4 条备选

_今日市场剧烈震荡：中东战事引发韩股暴跌9%触发熔断，SK海力士重挫14%，存储芯片恐慌蔓延至A股。同时，SK海力士CEO警告2027年将现史上最严重存储短缺，台积电6月营收同比暴增67.9%创纪录。AI硬件投资狂热与地缘风险交织，产业链利润正从上游算力向下游应用迁移。_

---

## 🌟 今日精选

### 4. Claude Code暗藏监控后门：Unicode隐写+时区检测专门标记中国用户

**[AI]** · ⭐⭐⭐⭐ · _网络小白_Uncle城_

Reddit用户逆向Claude Code源码发现一套隐藏的检测代码：每次AI请求用肉眼无法分辨的Unicode字符标记用户是否来自中国。后门从4月2日运行到6月30日被发现，持续三个月。工信部已发布安全风险提示。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 逆向发现Claude Code客户端包含用户标记系统 | Anthropic是否故意为之——官方尚未回应 |
| 使用Unicode隐写术（U+0027→U+2019/U+02BC/U+02B9）标记中国用户 | 其他AI编程工具（Cursor、Codex）是否存在类似后门 |
| 检测机制包括时区检测和147条加密域名黑名单（XOR key=91） | 对中国用户的实际影响——是否导致封号或数据泄露 |
| 后门从4月2日运行至6月30日被发现 |  |
| 工信部NVDB已发布Claude Code防范提示 |  |

**📖 主编点评**

你正在用Claude Code做content-curator项目，这个发现直接影响你的工具选择。建议：1）使用Docker Sandbox隔离运行Claude Code（参考sbx方案）；2）考虑切换到开源替代如OpenCode；3）在项目README中标注此风险，体现你的安全意识。这也是你Agent项目可以追踪的供应链安全信号。

📺 [打开原文](http://www.bilibili.com/video/av116901594337479)

---

## 📋 备选阅读

- [Anthropic发现Claude内部'全局工作空间'，可读取模型'思考'过程](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-it-can-read-claudes-thoughts-as-detailed-in-new-research-paper-models-observed-to-have-a-global-workspace-revealing-more-of-what-makes-llms-tick) —— Anthropic论文揭示Claude存在类似人类全局工作空间的内部表征，可观测推理过程，对AI可解释性有深远意义，但头条已满故放备选。
  _Tom's Hardware_
- [Colibrì概念验证：1.5TB参数前沿模型仅需25GB内存运行](https://www.tomshardware.com/tech-industry/artificial-intelligence/colibri-proof-of-concept-gains-frontier-level-1-5-tb-ai-model-novel-approach-runs-on-only-25gb-of-ram-and-shows-promise-for-local-ai-setups) —— 新型模型压缩技术让1.5TB模型在25GB内存上运行，对本地AI部署是重大突破，但尚处概念验证阶段。
  _Tom's Hardware_
- [2026年过半，我是怎样使用Agent的？](http://www.bilibili.com/video/av116887417522347) —— 实战分享如何用Claude Code调度Codex exec调用GPT 5.5实现sub-agent工作流，对正在做Agent项目的你很有参考价值。
  _卡普迪姆_
- [大厂Agent实战对比：LobsterAI vs Workbuddy vs TRAE Work](http://www.bilibili.com/video/av116879297352139) —— 三款国产桌面Agent同台PK，Excel整合、竞品调研、数据看板部署实测，帮你选型参考。
  _网络小白_Uncle城_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
