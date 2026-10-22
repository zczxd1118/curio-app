# Curio · AI · 2026-10-22

> 今日 2 条头条 + 5 条备选

_今天最重要的信号有两个：一是 AI 发现漏洞的能力第一次以「PHP2Shell」这种形态砸到整个互联网头上——OpenAI 和 Google Wiz 找到的 PHP 核心未认证 RCE，4chan、Wikipedia、DeviantArt 当天中招，AI 攻防的双刃性从论文变成了运维事故。二是资本端开始给 AI 泡沫定价：Anthropic 估值被传缩水 5000 亿美元、Firmus 数据中心 IPO 48 小时崩盘、Meta 靠发新股给 AI 输血。工程侧则有一条值得你细读的：Claude 工程负责人说「别再用 2024 年的方式用 Claude」。_

---

## 🌟 今日精选

### 1. AI 挖出 PHP 核心未认证 RCE「PHP2Shell」，半个互联网当天被打穿

**[AI]** · ⭐⭐⭐⭐⭐ · _TechCrunch_

10 月 21 日 PHP 官方紧急发布安全更新，修复 CVE-2026-109618 与 CVE-2026-109619 两个无需登录即可远程执行代码的漏洞，CVSS 9.2，修复版本为 8.2.35 / 8.3.36 / 8.4.27 / 8.5.12。漏洞由 OpenAI 与 Google 旗下 Wiz 的 AI 系统发现，4chan、DeviantArt、Wikipedia 等站点当天出现故障。这是「AI 找漏洞」第一次以大规模生产事故的形式落地。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| PHP 官方 10 月 21 日紧急发布修复，覆盖 8.2.35、8.3.36、8.4.27、8.5.12 四个版本 | 「AI 发现」是否意味着同类漏洞的披露节奏会整体加快，目前只有单点证据 |
| 两个漏洞均为未认证远程代码执行，CVSS 评分 9.2 | 受影响站点数量与真实被利用情况尚未有权威统计 |
| 漏洞由 OpenAI 与 Google Wiz 的 AI 系统发现，非人工审计 | AI 辅助挖洞会不会同时降低攻击方门槛，官方口径未涉及 |
| 4chan、DeviantArt、Wikipedia 等站点当天出现服务异常 | PHP 生态里大量长尾站点能否在一周内完成升级，存疑 |
| PHP 8.1 及以下已 EOL，8.2 的安全支持将在 2026 年 12 月 31 日结束 |  |

**📖 主编点评**

你做 content-curator 这类自建 Agent 项目，大概率跑在某个 VPS 的 PHP 或 Node 环境上。今天就去确认运行时的 PHP 版本，顺手把 LiteLLM 和 Node.js 本周的补丁也过一遍——这次事件里被点名的 AI 工具链不止 PHP。更值得记一笔的是：AI 攻防已经从「能力演示」进入「运维日程」，你的 Agent 项目该有一个最小化的依赖升级 checklist。

📺 [打开原文](https://techcrunch.com/2026/10/21/php-armageddon-openai-googles-wiz-find-ancient-holes-panicking-the-internet/)

---

### 3. Claude 工程负责人 Felix Rieseberg：多数人交给 AI 的任务，远低于它现在的能力

**[AI]** · ⭐⭐⭐⭐ · _-spacecaps-_

Felix Rieseberg 曾在 Anthropic 负责 Claude.ai、Cowork 和 Claude Code 桌面端的工程，10 月 21 日发布的这期访谈里，他的核心论点是：如果你只让 Claude 总结邮件，你浪费的是整整一代能力。访谈还谈了为什么「你是一位专家」这种提示不够、以及当 AI 回答听起来很有说服力时怎么发现错误。这是你反馈里反复要的「名人访谈」类型。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Felix Rieseberg 在 Anthropic 负责过 Claude.ai、Cowork 与 Claude Code 桌面端工程 | 访谈中的具体方法论是否可复现到个人项目，需看原片判断 |
| 访谈主题包括把更大目标交给 AI、角色提示的局限、以及识别 AI 错误答案的方法 | 「更大目标」的边界在哪，访谈未给出可操作的判据 |
| 视频 10 月 21 日发布，为海外访谈的翻译搬运 | 翻译版是否完整保留原对话上下文，存疑 |

**📖 主编点评**

你天天用 Claude Code，但很可能还停在「让它改这个函数」的粒度。这期值得花 30 分钟看原片，重点抓两点：他怎么描述「把整个任务而不是一步交给 Agent」，以及他判断 AI 答案可信度的具体动作。看完直接拿 content-curator 试一次——把「选稿 + 写点评 + 出 JSON」整条链一次性丢给它，而不是分段喂。

📺 [打开原文](http://www.bilibili.com/video/av117478881497342)

---

## 📋 备选阅读

- [AI 写得比你读得快，code review 要怎么做？](http://www.bilibili.com/video/av117479686802808) —— 把 code review 拆成挑错、对齐上下文、担责三件事，AI 时代捆不住了——观点扎实，但偏方法论，放备选。
  _grapeot_
- [DeepSeek Harness 首发实测 + 入门教程](http://www.bilibili.com/video/av117093710237975) —— 国产版 Codex 的实测，播放量 247 万，但教程属性强、信息密度一般，适合当工具速查。
  _程序员鱼皮_
- [Recursive 发布 Flint：一个主要由 AI 自己造出来的笔记本级编码模型](https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/) —— 免费、笔记本可跑、号称由自家 AI 研究系统造出，是「AI 自我改进」的早期实测样本。
  _TechCrunch_
- [Blacksmith 获 Sequoia 领投 6600 万美元 C 轮，估值 10 亿美元](https://techcrunch.com/2026/10/21/blacksmith-hits-unicorn-valuation-after-sequoia-leads-series-c/) —— 做 AI 代码构建与测试的平台成了独角兽，说明 AI 工程链路本身在变成生意。
  _TechCrunch_
- [llama.cpp 跑在越狱 PS5 上，原生运行任意 GGUF 模型](https://github.com/cobanov/PS5LM) —— 纯极客玩具，但展示了 GGUF 生态的移植性有多强，375 分。
  _HN_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
