# Curio · AI · 2026-07-05

> 今日 2 条头条 + 4 条备选

_今日核心信号：Claude Code 封号事件持续发酵，阿里内部全面禁用，暴露AI编程工具的安全隐忧；同时，Scaling Law 被曝存在方向性错误，可能意味着过去数年大量算力投入效率打折。半导体方面，SK海力士、美光等扩产与HBM竞赛白热化，DRAM价格高企倒逼技术路线转向。_

---

## 🌟 今日精选

### 1. Claude Code 封号原因曝光：Anthropic 植入隐形用户标记系统，阿里内部全面禁用

**[AI]** · ⭐⭐⭐⭐⭐ · _程序员鱼皮_

国外开发者逆向 Claude Code 源码发现，Anthropic 在客户端里藏了一套隐蔽的用户标记系统，用于识别并封禁非合规用户。阿里内部已将此工具列为高风险软件，全面禁用。事件折射出AI编程工具的安全性与供应链风险。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 国外开发者逆向 Claude Code 源码发现隐蔽用户标记系统 | 标记系统具体触发条件尚不明确 |
| Anthropic 客户端内置了针对中国用户的隐形代码 | Anthropic 官方尚未公开回应此事 |
| 阿里内部将 Claude Code 列为高风险软件并全面禁用 | 其他中国科技公司是否跟进禁用未知 |
| 36氪从阿里内部人士处确认该消息 | 该事件对Claude Code用户信任的长期影响待观察 |
|  | 是否涉及数据合规问题需进一步确认 |

**📖 主编点评**

如果你在用 Claude Code 做 side project，建议暂时切换到 Cursor 或 Codex，并关注 Anthropic 的官方回应。对于 content-curator 项目，可以考虑用本地模型或开源工具替代，避免依赖单一闭源服务。

📺 [打开原文](http://www.bilibili.com/video/av116844031774993)

---

### 2. OpenAI Scaling Law 原作被曝存在 bug：方向错误导致万亿算力浪费

**[AI]** · ⭐⭐⭐⭐⭐ · _华尔街见闻_

DeepMind 研究员指出，OpenAI 最初的 Scaling Law 错误引导行业长期“重参数、轻数据”，让大量模型训练不足、算力配置失衡。后续研究证实模型与数据应同步放大，此前方向可能浪费了海量 GPU 资源。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DeepMind 研究员指出 OpenAI Scaling Law 存在方向性错误 | 具体浪费的算力规模尚无精确估算 |
| 错误引导行业长期“重参数、轻数据” | OpenAI 是否已内部修正该方向未知 |
| 后续研究证实模型与数据应同步放大 | 对现有大模型训练策略的调整影响待评估 |
| 全球可能因此浪费了数年研发时间和海量 GPU 资源 | 该发现是否会改变行业共识尚不确定 |
|  | 对下游应用（如 Agent 工具）的间接影响需观察 |

**📖 主编点评**

这对你的 content-curator 项目是个提醒：不要盲目追求大模型参数，数据质量和配比同样关键。在构建 Agent 时，优先优化 prompt 和工具调用效率，而非单纯堆模型能力。

📺 [打开原文](https://wallstreetcn.com/articles/3776218)

---

## 📋 备选阅读

- [吴恩达 2026 Agent 智能体教程（附课件代码）](http://www.bilibili.com/video/av115897075242856) —— 经典教程但发布于1月，时效性一般，适合入门但非今日必读。
  _吴恩达Agent_
- [Claude Science 发布：专为科研打造的 AI 工具](http://www.bilibili.com/video/av116840541984361) —— Anthropic 新工具，内置科学渲染器和持久化内核，但面向科研场景，与你的 Agent 项目关联度较低。
  _旭光升_
- [零基础 Vibe Coding 教程（尚硅谷）](http://www.bilibili.com/video/av116711944620974) —— 2026年6月发布的系统教程，适合入门但内容偏基础，对已有经验的你帮助有限。
  _尚硅谷_
- [MCP 终极指南 - 从原理到实战（基础篇）](http://www.bilibili.com/video/av114339210073708) —— MCP 深度教程，但发布于4月，且你已熟悉 MCP，可作为备查。
  _马克的技术工作坊_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
