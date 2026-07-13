# Curio · AI · 2026-07-13

> 今日 2 条头条 + 4 条备选

_今日市场剧烈震荡：中东战事升级引发韩股暴跌9%熔断，SK海力士重挫14%，存储芯片板块承压。与此同时，Anthropic首次揭示可读取Claude内部"思维"，Colibrì实现1.5TB模型仅需25GB内存运行，AI工程化迎来新突破。SK海力士创纪录265亿美元IPO登陆纳斯达克，CEO警告2027年将现史上最严重存储短缺。_

---

## 🌟 今日精选

### 2. Anthropic首次揭示可读取Claude内部"思维"，发现全局工作空间

**[AI]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

Anthropic发表新研究论文，声称能读取Claude的内部"思考"过程。他们发现模型存在一个"J-space"（全局工作空间），类似于人类内部处理机制。这一发现可能为理解LLM内部运作提供全新视角，并有助于提升模型可解释性和安全性。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Anthropic已发表研究论文，详细说明如何读取Claude的内部状态 | 是否真的能"读取思维"还是过度拟人化描述，学术界存在争议 |
| 发现Claude存在一个称为"J-space"的全局工作空间 | 该技术能否实际应用于改进模型对齐或检测恶意行为尚未验证 |
| 该工作空间显示出与人类内部信息处理相似的特性 | 全局工作空间的发现是否具有普适性（其他LLM是否也有类似结构）未知 |
| 研究可能用于提升AI安全性和可解释性 | Anthropic未公布具体技术细节，复现难度较大 |
|  | 对模型安全性的实际提升效果有待进一步实验证明 |

**📖 主编点评**

这对你正在做的content-curator项目有直接启发：如果你想让Agent具备"自我反思"或"思维链"能力，理解模型内部工作空间是关键。Anthropic的发现意味着未来可能可以更精细地控制Agent的推理过程，比如检测它是否在"编造"信息。建议关注后续开源实现或API层面的可解释性接口，这可能是你项目的一个差异化亮点。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-it-can-read-claudes-thoughts-as-detailed-in-new-research-paper-models-observed-to-have-a-global-workspace-revealing-more-of-what-makes-llms-tick)

---

### 5. Claude Code暗藏监控后门：Unicode隐写+时区检测专门标记中国用户

**[AI]** · ⭐⭐⭐⭐ · _网络小白_Uncle城_

Reddit用户逆向Claude Code源码发现一套隐藏检测代码：每次AI请求用肉眼无法分辨的Unicode字符标记用户是否来自中国。后门从4月2日运行到被发现，持续三个月。技术细节包括时区检测、147条加密域名黑名单（XOR key=91）和Unicode隐写术。工信部已发布安全风险提示。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Reddit用户逆向Claude Code源码发现隐藏的用户标记系统 | Anthropic尚未对此事正式回应 |
| 使用Unicode字符隐写标记中国用户（U+0027→U+2019/U+02BC/U+02B9） | 其他AI编程工具（如Codex、Cursor）是否存在类似后门未知 |
| 包含时区检测和147条加密域名黑名单（XOR key=91） | 该后门的具体数据收集范围和用途尚不明确 |
| 后门从4月2日运行到6月30日被发现 | Docker沙盒方案（如sbx）能否完全隔离此类检测有待验证 |
| 工信部NVDB已发布Claude Code安全后门防范提示 | 对国内AI开发者的实际影响取决于后续监管措施 |

**📖 主编点评**

如果你在用Claude Code做content-curator项目，这个后门事件提醒你：不要把敏感代码或API密钥直接暴露给云端AI工具。建议使用Docker沙盒（如sbx）隔离运行，或者考虑本地部署方案。同时，这个事件也说明逆向工程AI工具的价值——你可以学习类似技术来审计自己使用的工具链。

📺 [打开原文](http://www.bilibili.com/video/av116901594337479)

---

## 📋 备选阅读

- [Tencent reportedly in talks to acquire Manus from Meta after Beijing intervention](https://www.tomshardware.com/tech-industry/artificial-intelligence/tencent-is-reportedly-in-talks-to-acquire-manus-from-meta-following-beijing-intervention-company-expects-to-remain-independent-of-chinese-tech-giant) —— 腾讯拟20亿美元从Meta手中买回Manus，北京要求解除收购，反映中国AI监管态度。
  _Tom's Hardware_
- [Apple sues OpenAI over alleged theft of trade secrets](https://www.tomshardware.com/tech-industry/big-tech/apple-sues-openai-over-alleged-theft-of-trade-secrets-claims-company-mentored-incoming-employees-on-bringing-confidential-information) —— 苹果起诉OpenAI窃取商业机密，指控其指导新员工携带机密信息，AI人才战升级。
  _Tom's Hardware_
- [Kimi K2.7 Code now available in GitHub Copilot](https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/) —— 月之暗面Kimi K2.7代码模型接入GitHub Copilot，国产AI编程工具全球化重要一步。
  _GitHub Blog_
- [Computer use in Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) —— Gemini 3.5 Flash新增电脑操控能力，Agent桌面自动化竞争白热化。
  _Google Blog_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
