# Curio · 大厂 AI 动态 · 2026-06-08

> 今日 1 条头条 + 3 条备选

_全球科技股暴跌，AI芯片板块遭去杠杆式抛售，但黄仁勋在首尔喊话「打折买入」并宣布与SK海力士、LG集团合作，AI基建叙事未破。与此同时，Anthropic、SpaceX、OpenAI相继推进IPO，AI公司上市潮与市场恐慌形成鲜明对比。本周关注美联储议息及CPI数据，决定调整深度。_

---

## 🌟 今日精选

### 4. OpenAI 推出 Lockdown Mode：防止提示注入攻击，保护敏感数据

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _TechCrunch_

OpenAI 发布了 Lockdown Mode，一项旨在防止提示注入攻击的新安全功能。该模式限制ChatGPT在对话中共享敏感数据，即使攻击者试图通过恶意提示绕过限制。这是OpenAI在安全方面的重要一步，尤其适合企业级部署。不过TechCrunch指出，Lockdown Mode并不能完全免疫所有提示注入攻击。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| OpenAI 于6月6日发布 Lockdown Mode | Lockdown Mode 的具体实现机制（基于规则还是模型微调）未公开 |
| 该模式旨在防止提示注入攻击导致敏感数据泄露 | 该功能是否适用于API调用，还是仅限ChatGPT界面 |
| Lockdown Mode 会限制模型在对话中输出特定类型的信息 | 与Anthropic的Constitutional AI等安全方案相比效果如何 |
| OpenAI 承认该模式不能完全消除提示注入风险 | 企业用户是否愿意为安全功能支付溢价 |

**📖 主编点评**

如果你正在用AI Agent处理用户数据或内部文档，Lockdown Mode 是一个必须关注的安全更新。建议在 content-curator 项目中集成该模式，防止用户通过恶意提示窃取你的爬虫配置或API密钥。同时注意，它并非银弹，仍需配合输入验证和权限控制。

📺 [打开原文](https://techcrunch.com/2026/06/06/openai-unveils-lockdown-mode-to-protect-sensitive-data-from-prompt-injection-attacks/)

---

## 📋 备选阅读

- [OpenAI is still working on that 'super app'](https://techcrunch.com/2026/06/07/openai-is-still-working-on-that-super-app/) —— OpenAI高级员工称「Chat已死」，暗示超级应用方向，但细节有限。
  _TechCrunch_
- [What to expect from WWDC 2026: Siri's highly anticipated revamp and Apple Intelligence updates](https://techcrunch.com/2026/06/06/what-to-expect-from-wwdc-2026-siris-highly-anticipated-revamp-and-apple-intelligence-updates/) —— WWDC 2026前瞻：Siri大改版和Apple Intelligence更新，值得关注但尚未发生。
  _TechCrunch_
- [NSA using Claude Mythos for 'offensive cyber operations,' report claims](https://www.tomshardware.com/tech-industry/artificial-intelligence/nsa-using-clause-mythos-for-offensive-cyber-operations-report-claims-says-half-a-dozen-anthropic-engineers-embedded-inside-the-agency) —— NSA被曝使用Claude Mythos进行网络攻击，Anthropic工程师嵌入，争议性大但需核实。
  _Tom's Hardware_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
