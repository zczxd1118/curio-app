# Curio · 大厂 AI 动态 · 2026-10-22

> 今日 2 条头条 + 4 条备选

_今天最重要的信号有两个：一是 AI 发现漏洞的能力第一次以「互联网级事故」的形式落地——PHP 核心两个未认证 RCE 由 OpenAI 与 Google Wiz 用 AI 挖出，4chan、Wikipedia、DeviantArt 同日中招；二是资本端开始给 AI 建设降温定价，Anthropic S-1 与估值缩水、Firmus IPO 48 小时崩盘、数据中心股集体下挫，叙事从「无限扩张」转向「谁来付账」。工程侧值得你留意的第三条线：Claude 工程负责人公开说「别再用 2024 年的方式用 Claude」，这是对你日常 Agent 工作流最直接的一次校准。_

---

## 🌟 今日精选

### 1. AI 挖出 PHP 核心两个未认证 RCE（CVSS 9.2），4chan、Wikipedia 同日宕机

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _TechCrunch_

10 月 21 日 PHP 官方紧急发布 8.2.35 / 8.3.36 / 8.4.27 / 8.5.12，修复 CVE-2026-109618 与 CVE-2026-109619——两个无需登录即可远程执行代码的漏洞，被社区称为 PHP2Shell。漏洞由 OpenAI 与 Google Wiz 的 AI 系统发现，同一天 4chan、DeviantArt、Wikipedia 等站点出现故障。这是「AI 找漏洞」第一次以全网事故的规模进入公众视野。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| PHP 官方 10 月 21 日发布 8.2.35、8.3.36、8.4.27、8.5.12 四个修复版本 | 「AI 发现」是否意味着同类漏洞存量远大于以往披露节奏，尚无统计口径 |
| 两个 CVE 均为未认证远程代码执行，CVSS 评分 9.2 | 受影响站点是否全部由该漏洞直接导致，官方尚未逐一确认 |
| 漏洞由 OpenAI 与 Google Wiz 的 AI 系统发现并上报 | 攻击面扩散速度是否已被控制，缺少公开的扫描数据 |
| 8.1 及以下已 EOL，8.2 安全支持将于 2026 年 12 月 31 日结束 | AI 辅助挖洞是否会成为常态化的漏洞披露主渠道，仍待观察 |
| 同日 4chan、DeviantArt、Wikipedia 等站点出现服务异常 |  |

**📖 主编点评**

你手上任何跑 PHP 的 side project 或实习项目，今天就去核版本号，8.2 以下等于裸奔。更值得记的是方法论：AI 把「找漏洞」的边际成本压到接近零，意味着你以后写代码时安全 review 不能再靠人肉抽查，得把静态扫描和依赖检查塞进 CI。这条也是你简历里「AI 工程实践」最好的谈资——不是调 API，而是理解 AI 改变了什么成本结构。

📺 [打开原文](https://techcrunch.com/2026/10/21/php-armageddon-openai-googles-wiz-find-ancient-holes-panicking-the-internet/)

---

### 5. Amazon 封杀 AI Agent 购物，Walmart 反手开放：Agent 电商的入口之争开打

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _TechCrunch_

同一天两家零售巨头给出相反答案：Amazon 阻止 AI Agent 在其站点代客下单，Walmart 则上线新机制，允许 AI Agent 在用户授权下代为购买，并提供消费额度控制。这不是产品细节之争，而是「Agent 能不能成为流量入口」的路线分歧——谁先定义 Agent 的接入协议，谁就掌握下一层分发。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Amazon 正在阻止 AI Agent 在其站点执行购物操作 | Walmart 的 Agent 接入是否有开放协议或仅限合作方，报道未明确 |
| Walmart 推出允许 AI Agent 代客下单的技术，并带消费控制 | Amazon 的封禁是技术手段还是条款约束，尚不清楚 |
| 两家动作均于 10 月 21 日被 TechCrunch 报道 | 用户对「Agent 代买」的信任度与授权粒度，缺少数据 |

**📖 主编点评**

这条对你做 content-curator 有直接类比价值：Agent 的价值不在「能调用工具」，而在「被允许调用哪些工具、授权边界怎么设计」。Walmart 那套「额度控制 + 用户授权」的形态，正是你给 Agent 加写操作时该抄的作业。另外，这也是一个很好的简历叙事——你能说清楚 Agent 落地的真正瓶颈是权限与信任，而不是模型能力。

📺 [打开原文](https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/)

---

## 📋 备选阅读

- [Gemini 4 Argon 发布，HN 两帖合计 3000+ 分](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) —— 9 月底发布，已不算新；但热度极高，若你还没看评测，Artificial Analysis 那篇性价比分析更值得先读。
  _Google Blog / Hacker News_
- [Tesla Q3 利润下滑 43%，同时启动 Optimus 机器人在加州量产](https://techcrunch.com/2026/10/21/tesla-stars-optimus-robot-production-in-california-as-profit-falls-43/) —— 收入持平、开支飙升、利润腰斩，同时押注机器人与自动驾驶——是「AI 资本开支」主线的另一面。
  _TechCrunch_
- [Stratechery：Muse Spark 开源，Meta 与 Apple 合作让模型本地跑](https://stratechery.com/2026/muse-spark-open-meta-apple-thin-and-thick/) —— Ben Thompson 的「thin and thick」框架值得一读，尤其对本地模型的分发逻辑；但需订阅，且是 10 月 20 日内容。
  _Ben Thompson_
- [Meta Muse 用户破 1000 万，购物是主要场景之一](https://techcrunch.com/2026/10/21/meta-says-muse-has-over-10m-users-with-shopping-a-top-activity/) —— AI 应用的用户规模数据点，可与 Walmart/Amazon 的 Agent 之争对照看。
  _TechCrunch_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
