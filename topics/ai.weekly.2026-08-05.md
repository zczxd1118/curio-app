# Curio · AI · 2026-08-05

> 今日 1 条头条 + 2 条备选

_AI 算力与股市冰火两重天：一边是 DeepSeek 重启融资、SpaceX 首份季报显示 AI 烧钱凶猛，另一边是德州暂停数据中心并网、存储价格暴涨引发连锁反应。对做 Agent 的你，DeepSeek V4 Flash 接入 Claude Code 的实测和开源模型安全报告更值得关注。_

---

## 🌟 今日精选

### 1. DeepSeek V4 Flash 实测：Claude Code 接入后连续开发 7 个项目，逼近 Opus 4.8？

**[AI]** · ⭐⭐⭐⭐⭐ · _AI超元域_

DeepSeek 发布 V4 Flash 0731，284B 总参数、13B 激活、100 万上下文，官方基准接近 Claude Opus 4.8。UP 主在 Claude Code 里接入后连做 7 个项目，发现代码生成任务耗时数十分钟，疑似新模型上线算力拥堵。这是国产模型首次在 Agent 场景下如此接近前沿闭源。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DeepSeek V4 Flash 0731 发布，284B 总参数、13B 激活参数、100 万 Token 上下文 | 官方基准接近 Opus 4.8，但真实 Agent 场景是否稳定尚需更多测试 |
| 官方基准表现接近 Claude Opus 4.8，且为最便宜的国产模型之一 | 耗时数十分钟是算力拥堵还是模型本身推理慢，需要后续复测确认 |
| UP 主在 Claude Code 中接入后连续开发 7 个项目，基础指令、24 点运算、密码锁逻辑推理全部答对 | 与 Kimi K3 的对比是否公平，取决于测试用例和配置是否一致 |
| 代码生成任务统一耗时数十分钟，判断为新模型上线调用高峰算力拥堵 | 国产模型在 Agent 工具链的兼容性（如 Claude Code）是否已成熟，仍需观察 |
| 对比 Kimi K3 后优缺点明显，自制桌面操作系统成品完整性不及 Codex 平台 | 价格优势能否持续，取决于 DeepSeek 后续的定价策略和算力成本 |

**📖 主编点评**

你正在做 content-curator 这个 Agent 项目，DeepSeek V4 Flash 可能是降低 API 成本的关键。建议在 Claude Code 里配好 cc-switch，实测一下你的工作流，重点看长任务耗时和代码质量。如果算力拥堵缓解，这可能是目前性价比最高的国产模型。

📺 [打开原文](http://www.bilibili.com/video/av117014605731815)

---

## 📋 备选阅读

- [Claude Code 封号原因曝光：Anthropic 植入隐形代码标记中国用户？](http://www.bilibili.com/video/av116844031774993) —— 逆向发现 Anthropic 在客户端藏了用户标记系统，涉及封号机制，对国内用户影响大，但需验证真实性。
  _程序员鱼皮_
- [OpenAI 和苹果互撕：苹果起诉 OpenAI 窃取商业机密，OpenAI 否认](https://www.tomshardware.com/tech-industry/big-tech/apple-is-getting-this-wrong-says-openai-startup-blasts-iphone-maker-over-lawsuit-alleging-it-stole-confidential-information-through-ex-apple-employees) —— 苹果称更多前员工可能将机密带给 OpenAI，OpenAI 回应“没有也不想要”，法律战升级。
  _Jowi Morales_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
