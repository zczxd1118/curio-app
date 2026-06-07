# Curio · 大厂 AI 动态 · 2026-06-07

> 今日 1 条头条 + 4 条备选

_本周最重磅信号：SpaceX下周四IPO定价1.77万亿美元，但Morningstar估值仅一半，散户入场门槛降至2000美元；Anthropic同日递交IPO文件，AI公司上市潮全面开启。同时，ChatGPT将迎最大改版，从聊天机器人转型为集成编程与Agent的超级应用。市场方面，非农超预期引发全球风险资产去杠杆，纳指单日暴跌4%，警惕6月变盘点。_

---

## 🌟 今日精选

### 5. OpenAI推出Lockdown Mode防御提示注入攻击，保护敏感数据

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _TechCrunch_

OpenAI发布Lockdown Mode，旨在保护敏感数据免受提示注入攻击。该模式限制模型在特定上下文中执行非授权操作，但仍可能被绕过。这是AI安全领域的重要进展，尤其对企业级Agent应用至关重要。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| OpenAI推出Lockdown Mode防御提示注入 | Lockdown Mode是否足够防御所有类型的提示注入？ |
| 该模式限制模型执行非授权操作 | 对Agent工作流的影响：是否会限制合法功能？ |
| 但仍可能被高级提示注入绕过 | Claude Code是否有类似的安全机制？ |
| 目标是减少敏感数据泄露风险 | 企业用户是否会因此加速采用ChatGPT？ |
| 适用于企业级ChatGPT部署 | 开源社区能否复现类似机制？ |

**📖 主编点评**

这对你的Agent项目是重要参考：在构建content-curator时，应该内置类似的安全机制——限制Agent访问敏感数据、设置操作白名单、实现人工审核回路。建议研究OpenAI Lockdown Mode的实现原理，将其作为你项目安全设计的基线。同时，提示注入是Agent开发中最容易被忽视的风险，务必在早期就纳入防御。

📺 [打开原文](https://techcrunch.com/2026/06/06/openai-unveils-lockdown-mode-to-protect-sensitive-data-from-prompt-injection-attacks/)

---

## 📋 备选阅读

- [Google to pay SpaceX $920M per month for compute](https://techcrunch.com/2026/06/05/google-will-pay-spacex-920m-per-month-for-compute/) —— Google每月向SpaceX支付9.2亿美元算力租赁费，AI算力需求已催生天价基础设施合同。
  _TechCrunch_
- [Reid Hoffman leaves Microsoft board to focus on AI drug discovery startup Manus](https://techcrunch.com/2026/06/05/reid-hoffman-is-leaving-microsofts-board-to-go-founder-mode-with-startup-manus/) —— LinkedIn联合创始人离开微软董事会，全职投入AI药物发现创业，标志AI+生物技术赛道升温。
  _TechCrunch_
- [Supabase doubles valuation to $10B in 8 months, boosted by AI coding tools](https://techcrunch.com/2026/06/05/supabase-doubles-valuation-to-10b-in-8-months/) —— 开源BaaS平台Supabase估值8个月翻倍至100亿美元，受益于Claude Code、Codex等AI编程工具生态。
  _TechCrunch_
- [Meta AI app creates its own clickbait news feed with AI-generated articles](https://www.theverge.com/ai-artificial-intelligence/944235/meta-app-ai-clickbait-articles) —— Meta AI应用推出AI生成点击诱饵文章信息流，内容质量堪忧，但用户增长迅猛。
  _The Verge_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
