# Curio · AI · 2026-10-22

> 今日 1 条头条 + 3 条备选

_今天最重要的信号有两个：一是 AI 发现漏洞的能力第一次以「互联网级事故」的形式落地——PHP 核心两个未认证 RCE 由 OpenAI 与 Google Wiz 用 AI 挖出，4chan、Wikipedia、DeviantArt 同日中招；二是资本端开始给 AI 建设降温定价，Anthropic S-1 与估值缩水、Firmus IPO 48 小时崩盘、数据中心股集体下挫，叙事从「无限扩张」转向「谁来付账」。工程侧值得你留意的第三条线：Claude 工程负责人公开说「别再用 2024 年的方式用 Claude」，这是对你日常 Agent 工作流最直接的一次校准。_

---

## 🌟 今日精选

### 2. Claude 工程负责人 Felix Rieseberg：多数人交给 AI 的任务，远低于它现在的能力

**[AI]** · ⭐⭐⭐⭐⭐ · _-spacecaps-_

Felix Rieseberg 在 Anthropic 负责过 Claude.ai、Cowork 和 Claude Code 桌面端的工程，10 月 21 日的访谈里他给了一个刺人的判断：很多人只是让 Claude 总结邮件，而它现在能承接的目标要大得多。他同时讲了两个工程细节——为什么一句「你是一位专家」不够，以及当 AI 的回答听起来很可信时怎么找出错误。这是本周最贴近你日常工作流的一份一手材料。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Felix Rieseberg 曾在 Anthropic 负责 Claude.ai、Cowork 与 Claude Code 桌面端工程 | 「更大目标」的具体边界（多长的任务链、多少工具调用）访谈中未量化 |
| 访谈主题包括如何把更大目标交给 AI、角色提示的局限、以及识别可信但错误的回答 | 角色提示失效的结论是否适用于所有模型家族，缺少对照实验 |
| 内容为 10 月 21 日发布，属本周新内容 | 该访谈为二手翻译/搬运，原始英文版本信息密度可能更高 |

**📖 主编点评**

你正在做 content-curator，这条几乎是直接对着你的项目说的：如果你现在的 prompt 还是「你是资深主编，请选稿」，那正是他批评的那类用法。值得花 20 分钟看完，然后回头改你的 Agent——把「角色」换成「可验证的产出约束 + 自检步骤」，比如让子 Agent 先列候选再打分再反驳自己。这类访谈比教程稀缺，也正好对上你「想多看名人访谈」的偏好。

📺 [打开原文](http://www.bilibili.com/video/av117478881497342)

---

## 📋 备选阅读

- [AI 写得比你读得快，code review 要怎么做？](http://www.bilibili.com/video/av117479686802808) —— 把「读代码」拆成挑错、对齐上下文、担责三件事，指出 AI 高产下三者必须解耦——观点密度高，但属方法论讨论，放备选。
  _grapeot_
- [DeepSeek Harness 首发实测 + 入门教程](http://www.bilibili.com/video/av117093710237975) —— 国产版 Codex 的实测，播放量 247 万说明关注度高；但教程属性强、信息密度一般，适合周末补课而非今日必读。
  _程序员鱼皮_
- [Recursive 发布 Flint：一个笔记本能跑的编码模型，号称大部分由 AI 自己造](https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/) —— 「AI 造 AI」的早期样本，本地可跑这点对你很实用；但技术细节披露少，先记名字。
  _TechCrunch_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
