# Curio · AI · 2026-11-02

> 今日 1 条头条 + 3 条备选

_今天最重要的信号有两个：一是 Anthropic IPO 的定价争议已经从投行圈烧到 HN 首页，'史上最荒谬 IPO'与'前所未有的收入增长'两种叙事同时成立，说明 AI 泡沫的分歧已进入公开定价阶段；二是 Gemini 4 Carbon 在 Artificial Analysis 指数上登顶，Google 一周内连发 Argon/Carbon 两个型号，模型迭代节奏重新加速。工程侧值得看的是 nv-uefi-unlocker 这类硬核解锁，以及 Claude Code 被植入后门的供应链风险。_

---

## 🌟 今日精选

### 4. DeepSeek Harness 50 分钟完整教程发布，SuperAgent 工作流首次被系统性拆解

**[AI]** · ⭐⭐⭐⭐ · _Git源宝_

DeepSeek Harness 是 DeepSeek 自家的 Agent 执行框架，此前中文社区只有零散的接入视频。这条 11 月 1 日发布的教程用 50 分钟把 DSH 的安装、SuperAgent 配置和任务编排完整走了一遍，制作周期 60 天。对比 8 月那条'DSH vs Claude Code 实测'，这次是正向的完整教学。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 视频于 2026-11-01 发布，时长约 50 分钟，作者称制作耗时 60 天 | DSH 的插件化与缓存命中机制是否真的优于 Claude Code，需要自己跑同一任务验证 |
| 内容覆盖 DeepSeek Harness 安装与 SuperAgent 使用 | 教程质量未经社区交叉验证，单条视频不足以定论 |
| 此前已有实测视频对比 DSH 与 Claude Code 在同一模型下的工具链差异 | DSH 的长期维护投入是否稳定，取决于 DeepSeek 的商业化节奏 |
| 尚硅谷同期发布了 Agent Skills 教程，覆盖 WorkBuddy、Codex、DSH 三件套 | SuperAgent 在多步任务上的失败率没有公开数据 |

**📖 主编点评**

你的 content-curator 如果要接国产模型，DSH 是绕不开的执行层。建议先看这条教程的前 20 分钟把环境跑通，然后用同一个摘要任务分别跑 DSH 和 Claude Code，重点记录失败重试次数和 token 消耗——这两个数字才是你项目文档里最有价值的部分。

📺 [打开原文](http://www.bilibili.com/video/av117540671982699)

---

## 📋 备选阅读

- [最新Skills开发教程，Agent skill实战｜WorkBuddy+Codex+DeepSeek Harness](http://www.bilibili.com/video/av117511429295044) —— 尚硅谷 10 月 28 日发布的 Agent Skills 实战课，覆盖三套工具链，与头条 DSH 教程互补。
  _尚硅谷_
- [认真用 Claude Code 的人，迟早会遇见 Everything Claude Code](http://www.bilibili.com/video/av116319122885806) —— 拆解 GitHub 116K star 的 Claude Code 配置项目，斜杠命令/子代理/Hooks 全覆盖，对你的 Agent 项目直接可用。
  _极客魔导师_
- [DeepSeek V4.1 Flash 接入指南｜六大 Agent 工具一次配好](http://www.bilibili.com/video/av117459403150912) —— V4.1 Flash 跑分反超旗舰，这条把六套工具的配置方法和避坑点一次讲清，工程细节密度高。
  _跟着小陈玩AI_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
