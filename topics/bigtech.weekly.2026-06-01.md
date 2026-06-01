# Curio · 大厂 AI 动态 · 2026-06-01

> 今日 1 条头条 + 3 条备选

_今天Computex 2026开幕，NVIDIA正式发布RTX Spark超级芯片，标志着AI PC进入新纪元。同时，OpenAI数学突破解决80年难题，AI能力边界再拓宽。但企业AI支出开始理性化，Token经济学遭遇挑战。_

---

## 🌟 今日精选

### 3. Google发布Gemini 3.5 Flash：速度提升2倍，成本降低60%，支持100万token上下文

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Google AI Blog_

Google在5月19日发布了Gemini 3.5 Flash，这是Gemini系列的最新轻量级模型。相比3.0 Flash，推理速度翻倍，价格降低60%，上下文窗口扩展到100万token。同时发布的还有Gemini Omni——一个多模态实时交互模型。但Gemini CLI宣布将于6月18日停用，迁移至Antigravity CLI。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Gemini 3.5 Flash推理速度是3.0 Flash的2倍 | 100万token上下文在实际RAG场景中的检索精度待验证 |
| API价格降低60%，输入$0.08/百万token，输出$0.30/百万token | Gemini Omni的实时交互能力与GPT-4o的对比尚无第三方评测 |
| 上下文窗口100万token，支持多模态输入 | CLI停用可能影响自动化工作流用户 |
| Gemini CLI将于2026年6月18日停止服务 | 价格降低是否会导致质量下降（如更频繁的幻觉） |

**📖 主编点评**

如果你在用Gemini API做content-curator的摘要功能，3.5 Flash的性价比很诱人。100万token上下文意味着你可以直接把整篇论文或代码库塞进去做分析。但注意Gemini CLI即将停用，如果你有自动化脚本依赖它，尽快迁移到Antigravity CLI或直接调用API。

📺 [打开原文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)

---

## 📋 备选阅读

- [GitHub Copilot改用Token计费引发开发者不满](https://techcrunch.com/2026/05/30/what-a-joke-github-copilots-new-token-based-billing-spurs-consternation-among-devs/) —— GitHub Copilot从固定订阅转为Token计费，开发者普遍认为成本将大幅上升，'黄金时代'或终结。
  _TechCrunch_
- [Meta正在开发AI挂坠硬件](https://techcrunch.com/2026/05/30/meta-is-reportedly-developing-an-ai-pendant/) —— Meta继Ray-Ban眼镜后，据报正在开发AI挂坠，可能集成语音助手和摄像头，但产品形态和发布时间未定。
  _TechCrunch_
- [Google Gemini Spark 24/7 AI助手实测：实用但定位尴尬](https://techcrunch.com/2026/05/30/i-put-googles-24-7-ai-assistant-gemini-spark-to-work-and-its-actually-pretty-useful/) —— Gemini Spark作为独立AI助手应用，能自动处理收件箱摘要和日程，但为何不直接集成到现有Google服务中令人费解。
  _TechCrunch_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
