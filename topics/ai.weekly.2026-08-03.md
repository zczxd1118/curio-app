# Curio · AI · 2026-08-03

> 今日 2 条头条 + 9 条备选

_今日核心信号：AI 算力链遭遇全球性去杠杆，韩国 KOSPI 暴跌、存储股重挫，但阿里发布千问 3.8-Max 开源模型，性能对标 Anthropic Fable 5，为市场注入强心剂。同时，SpaceX 首份季报在即，股价已跌去近半，成为观察 AI 泡沫成色的关键。_

---

## 🌟 今日精选

### 1. 阿里发布千问 3.8-Max：2.4 万亿参数开源，性能对标 Anthropic Fable 5

**[AI]** · ⭐⭐⭐⭐⭐ · _华尔街见闻_

阿里巴巴今日发布千问 3.8-Max，参数规模达 2.4 万亿，是千问家族最强模型，也是首个开源 Max 级权重的版本（下周发布）。API 定价输入 2.0 美元/百万 tokens、输出 6.0 美元/百万 tokens。基准测试显示其编程与通用智能体能力与 Anthropic Fable 5 相当，部分指标超越，并在芯片设计、量化研究、电商模拟等长程任务中展现出显著的自主执行能力。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 千问 3.8-Max 参数规模 2.4 万亿，为千问家族迄今最强模型 | 基准测试的具体方法论和测试集尚未公开，需独立验证 |
| API 定价：输入 2.0 美元/百万 tokens，输出 6.0 美元/百万 tokens | 与 Anthropic Fable 5 的对比是否涵盖所有关键场景，尚不明确 |
| 基准测试显示编程与通用智能体能力与 Anthropic Fable 5 相当，部分指标超越 | 开源版本的实际推理成本和部署难度有待评估 |
| 在芯片设计、量化研究、电商模拟等长程任务中展现显著自主执行能力 | 长程任务能力是否能在真实生产环境中稳定复现，仍需观察 |
| 下周将发布开源 Max 级权重版本 |  |

**📖 主编点评**

千问 3.8-Max 的开源策略直接冲击闭源模型市场，你应该关注其权重发布后的社区评测和微调案例。对于你的 Agent 项目，可以尝试用其 API 或本地部署测试长程任务处理能力，尤其在工具调用和自主规划方面。同时，留意阿里云生态的配套工具链，可能成为你构建 content-curator 的替代方案。

📺 [打开原文](https://wallstreetcn.com/articles/3778546)

---

### 5. DeepSeek V4 Flash 实测：Claude Code 接入后连续开发 7 个项目，逼近 Opus 4.8

**[AI]** · ⭐⭐⭐⭐ · _AI超元域_

DeepSeek 发布 V4 Flash 0731 版本，284B 总参数、13B 激活参数、100 万 Token 上下文，官方基准表现接近 Claude Opus 4.8。UP 主实测将其接入 Claude Code，连续开发 7 个项目，评估其性能、速度与真实短板，并与 Kimi K3 对比。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DeepSeek V4 Flash 0731 版本发布 | 官方基准与真实场景表现可能存在差距 |
| 284B 总参数、13B 激活参数、100 万 Token 上下文 | 13B 激活参数的实际推理效率，需进一步验证 |
| 官方基准表现接近 Claude Opus 4.8 | 100 万 Token 上下文的实用性，取决于具体任务 |
| UP 主实测接入 Claude Code 连续开发 7 个项目 | 与 Claude Opus 4.8 的差距在哪些方面，尚不明确 |
| 与 Kimi K3 进行了对比 |  |

**📖 主编点评**

DeepSeek V4 Flash 的低成本和高性能，可能成为你构建 Agent 的性价比之选。建议你观看视频，了解其在 Claude Code 中的实际表现，特别是长上下文和复杂任务处理能力。如果表现稳定，可以尝试将其作为 content-curator 的底层模型，降低 API 成本。

📺 [打开原文](http://www.bilibili.com/video/av117014605731815)

---

## 📋 备选阅读

- [【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！](http://www.bilibili.com/video/av115897075242856) —— 吴恩达的 Agent 教程，系统覆盖设计模式、工具集成与评估，适合作为 Agent 构建的系统性参考。
  _吴恩达Agent_
- [从零开始，学会让桌面Agent帮你干活！【小白教程】](http://www.bilibili.com/video/av116861865887789) —— 国产桌面 Agent 实操教程，覆盖 8 大用法，适合快速上手桌面自动化。
  _秋芝2046_
- [零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor](http://www.bilibili.com/video/av116711944620974) —— 尚硅谷的 Vibe Coding 实战教程，从零开始用自然语言指挥 AI 开发项目，适合入门。
  _尚硅谷_
- [从夯到拉，锐评 32 个 AI 编程工具！](http://www.bilibili.com/video/av116578532200786) —— 鱼皮实测 32 个 AI 编程工具，帮你快速找到最适合自己的，避免踩坑。
  _程序员鱼皮_
- [Claude Code Agent Teams上手指南+项目实测](http://www.bilibili.com/video/av116037064331269) —— 深入讲解 Claude Code Agent Teams 的架构与实战，解决复杂任务并行处理问题。
  _程序员阿江-Relakkes_
- [MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。](http://www.bilibili.com/video/av114155298228756) —— MCP 概念与实战全覆盖，适合理解 Agent 工具调用的底层原理。
  _技术爬爬虾_
- [【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！](http://www.bilibili.com/video/av116951003242391) —— 吴恩达的 Vibe Coding 教程，强调标准化流水线，适合建立规范开发流程。
  _吴恩达AIAgent_
- [用Codex、cursor 还是Claude ？程序员不作选择题，我都要用，还一起用 | Orca ADE 介绍](http://www.bilibili.com/video/av116996217838997) —— Orca ADE 整合多 Agent 协作，开源免费，适合探索多工具协同工作流。
  _技术胖_
- [10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型](http://www.bilibili.com/video/av116579891153749) —— 快速在 Ubuntu 上配置 Claude Code 并接入 DeepSeek V4，低成本体验。
  _不倒翁lhj_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
