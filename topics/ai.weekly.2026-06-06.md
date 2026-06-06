# Curio · AI · 2026-06-06

> 今日 1 条头条 + 4 条备选

_今天全球AI牛市遭遇黑色星期五，费城半导体指数暴跌超10%，美光因内存需求降温担忧单日重挫13%。与此同时，SpaceX IPO进入倒计时，与Anthropic和谷歌签下合计700亿美元算力大单，但Morningstar估值仅为IPO目标一半。Anthropic IPO也箭在弦上，年化营收已达470亿美元。Claude Code的Ultracode功能悄然上线，可操控100个Agent并行开发，是本周最值得关注的工程实践。_

---

## 🌟 今日精选

### 1. Claude Code Ultracode上线：操控100个Agent并行开发，Vibe Coding进入脚本化新纪元

**[AI]** · ⭐⭐⭐⭐⭐ · _技术胖_

Anthropic为Claude Code V2.1.47/48秘密新增了Workflow功能，被官方从Changelog中删除但未从代码中移除。该功能允许用户通过JS脚本定义多Agent协同工作流，单个任务可拆解给100个子Agent并行执行。这是自MCP以来Claude Code最重要的架构升级，直接解决了大型项目单Agent跑不完的痛点。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Claude Code V2.1.47/48新增Workflow功能，支持JS脚本定义多Agent工作流 | 官方删除Changelog的原因不明，可能是功能尚未稳定或策略调整 |
| 单个Workflow可调度最多100个Agent并行执行子任务 | 100个Agent并行实际效果取决于任务拆分粒度，存在边际收益递减 |
| 功能被官方从Changelog中删除但代码中保留，可通过特定方式启用 | 脚本化工作流对非开发者用户门槛较高，可能限制普及速度 |
| Ultracode（超码）为同一功能的中文社区命名 | 与Anthropic即将IPO的节奏是否相关，有待观察 |

**📖 主编点评**

你应该立即尝试这个功能。如果你在用Claude Code做Side Project，Workflow能让你把"写一个记账App"拆成"设计数据库→写API→写前端→部署"四个子任务并行执行，效率翻倍。关注技术胖视频中的具体配置方法，尤其是JS脚本的编写模板——这是未来AI编程的标配能力。

📺 [打开原文](http://www.bilibili.com/video/av116697163896598)

---

## 📋 备选阅读

- [Anthropic：Claude现在编写超过80%的合并代码，警告递归自我改进风险](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-claude-now-writes-more-than-80-percent-of-its-merged-code) —— Anthropic内部报告显示Claude已主导自身代码编写，同时呼吁建立前沿AI暂停机制——既是技术里程碑也是IPO前的风险提示。
  _Tom's Hardware_
- [NSA被曝使用Anthropic Mythos进行网络攻击，6名Anthropic工程师嵌入该机构](https://www.tomshardware.com/tech-industry/artificial-intelligence/nsa-using-clause-mythos-for-offensive-cyber-operations-report-claims-says-half-a-dozen-anthropic-engineers-embedded-inside-the-agency) —— AI军事化应用加速，Anthropic与NSA的合作可能影响其IPO合规审查。
  _Tom's Hardware_
- [Reid Hoffman离开微软董事会，全职投入AI药物发现初创Manus](https://techcrunch.com/2026/06/05/reid-hoffman-is-leaving-microsofts-board-to-go-founder-mode-with-startup-manus/) —— LinkedIn联合创始人从微软董事会抽身，All in AI+生物——信号：AI制药赛道正在吸引顶级人才。
  _TechCrunch_
- [Google将每月向SpaceX支付9.2亿美元算力费](https://techcrunch.com/2026/06/05/google-will-pay-spacex-920m-per-month-for-compute/) —— Google成为SpaceX算力租赁第二大客户，显示云巨头对GPU的渴求已突破传统供应商边界。
  _TechCrunch_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
