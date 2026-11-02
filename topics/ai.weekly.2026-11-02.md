# Curio · AI · 2026-11-02

> 今日 1 条头条 + 5 条备选

_今天最重要的信号有两个：一是 Anthropic IPO 叙事开始被公开质疑，S-1 的高增长与算力成本同时摆上台面，配合美股科技股因 AI 成本担忧大跌、Alphabet 单日市值蒸发 5000 亿美元，AI 资本周期的情绪拐点可能已经出现；二是 DeepSeek Harness 生态在中文社区快速成型，Agent 工具链的竞争从模型转向 harness 层。工程侧值得关注的是 Claude Code 官方扩展被植入后门，以及 Nvidia 半速限制被开源工具解锁。_

---

## 🌟 今日精选

### 3. DeepSeek Harness 教程 24 小时内上线，中文社区开始围绕 harness 层而非模型层做工程

**[AI]** · ⭐⭐⭐⭐ · _Git源宝_

DeepSeek Harness（DSH）发布后不到一天，B 站就出现了 50 分钟级别的详细教程，讲 SuperAgent 的配置与使用。同期还有多条内容对比 DSH 与 Claude Code 在同一模型下的任务表现，讨论焦点从「哪个模型强」转向「哪个 harness 的工具链设计更好」。这是一个值得注意的信号：Agent 工程的竞争重心正在下移到 harness。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DeepSeek Harness 教程视频于 2026-11-01 发布，时长约 50 分钟，作者称制作耗时 60 天 | 单条对比视频的结论受任务选择和 prompt 影响大，不能直接推出 harness 优劣的普遍结论 |
| 已有实测内容用同一 DeepSeek Pro 0813 模型在 Claude Code 与 DSH 中跑相同任务做对比 | DSH 的插件化与缓存机制是否真的优于 Claude Code，需要看源码或官方文档，目前只有二手实测 |
| 对比维度包括插件化、流程记录、缓存命中和任务完成质量 | 中文社区教程质量参差，50 分钟视频的信息密度需要自己筛 |
| DeepSeek V4.1 Flash 已发布，并有内容实测将其接入 DSH、WorkBuddy、Kimi Code 等六种工具 | harness 层竞争是否会成为长期趋势，还是模型厂商顺手做的附属功能，尚不明朗 |

**📖 主编点评**

这是你这周最该花时间的方向：把 DSH 装起来，用你 content-curator 里的一个真实子任务（比如抓取+摘要）跑一遍，和 Claude Code 对比 token 消耗与失败率。harness 层的工程经验，比再学一个模型 API 更能写进简历。

📺 [打开原文](http://www.bilibili.com/video/av117540671982699)

---

## 📋 备选阅读

- [Everything Claude Code：116K star 的 Claude Code 配置项目实战讲解](http://www.bilibili.com/video/av116319122885806) —— 斜杠命令、子代理、Hooks、学习系统的完整拆解，和你正在做的 Agent 项目直接相关，但发布较早，放备选。
  _极客魔导师_
- [Claude Code 官方扩展被植入后门（派早报提及）](https://sspai.com/post/118191) —— 供应链安全事件，直接影响你日常用的工具链，但细节需等官方通报，先记一笔。
  _少数派编辑部_
- [Claude Code Hooks 回调 + Agent Teams 实现零轮询全自动开发](http://www.bilibili.com/video/av116046157647899) —— Stop Hook 自动回调把 token 消耗压到接近忽略，是省成本的工程技巧，但内容偏旧。
  _AI超元域_
- [最新 Skills 开发教程：WorkBuddy + Codex + DeepSeek Harness 实战](http://www.bilibili.com/video/av117511429295044) —— 10-28 发布，Skills 开发是当前 Agent 工程的热点，但机构课信息密度通常偏低。
  _尚硅谷_
- [DeepSeek V4.1 Flash 接入六大 Agent 工具实测](http://www.bilibili.com/video/av117459403150912) —— 两种配置方法、模型名怎么填、哪里避坑，实操性强，但属于配置层而非原理层。
  _跟着小陈玩AI_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
