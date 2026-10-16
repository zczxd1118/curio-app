# Curio · 大厂 AI 动态 · 2026-10-16

> 今日 2 条头条 + 4 条备选

_今天最值得盯的是两条线：一是 ASML 交出 130 亿美元创纪录季度、并说客户已经在预订 2029-2030 年的产能，AI 资本开支的紧张程度从下游烧到了最上游的设备端；二是 Meta 联合 Apple 发布能在 Mac 本地跑的开放权重模型 Muse Spark Open，加上 Bluesky 把 Attie 扩成"社交 vibe coding"，端侧与轻量 Agent 的落地速度明显快于预期。_

---

## 🌟 今日精选

### 2. Meta 联合 Apple 发布开放权重模型 Muse Spark Open，直接在 Apple Silicon 上本地跑

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _Lucas Ropek / TechCrunch_

Meta 发布 Muse Spark Open，自称"迄今最强的美国开放权重模型"，并称它是同类中第一个能在 Apple Silicon 上本地运行的模型。Apple 与 Meta 罕见联手，用 MLX 做了适配。对做 Agent 的人来说，这是端侧推理从"能跑"走向"能用"的一个具体节点。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Meta 发布开放权重模型 Muse Spark Open，宣称是迄今最强美国开放权重模型 | "最强开放权重"是厂商自评，尚无第三方基准验证 |
| Meta 称其为同类中首个可在 Apple Silicon 上本地运行的模型 | 本地运行的量化版本与云端版本能力差距未公布 |
| Apple 与 Meta 合作为该模型做了 Mac 端适配（MLX 相关） | Apple 参与适配的深度不明，是否进入系统级 API 未知 |
| The Verge 与 TechCrunch 同日报道，口径一致 | 对 Agent 场景的实际可用性（工具调用、长上下文）还没实测数据 |

**📖 主编点评**

你正在做 content-curator，这条直接相关：如果 Muse Spark Open 的本地版本在工具调用上够用，你的 Agent 就能把"摘要、分类、去重"这类高频低难度任务放到本地跑，只把真正需要强推理的环节交给云端 API。建议这周就找一台 M 系列 Mac 实测一次，重点看它能不能稳定输出结构化 JSON——这决定你的项目能不能把成本压下来。

📺 [打开原文](https://techcrunch.com/2026/10/15/meta-launches-an-open-weight-model-that-runs-on-macs/)

---

### 4. Bluesky 把 Attie 扩成"社交 vibe coding"平台：任何人都能生成小游戏、测验和网页

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _Sarah Perez / TechCrunch_

Bluesky 的实验性 AI 工具 Attie 从"生成自定义 feed"扩展到让用户直接构建小游戏、测验、仪表盘和网页，并把这些产物接入社交网络的数据。官方把它叫作"社交 vibe coding"。这是 vibe coding 从个人工具走向社交分发的一个具体样本。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Attie 最初是 Bluesky 的 AI 生成自定义 feed 工具 | 生成产物的质量与稳定性没有公开评测 |
| 本次扩展支持生成小游戏、测验、仪表盘、网页等"小型社交应用" | "社交 vibe coding"能否形成留存，尚无数据 |
| 产物可以调用 Bluesky 社交网络的数据 | 平台对生成内容的审核与滥用防护策略未说明 |
| The Verge 与 TechCrunch 同日报道，细节一致 | 是否开放给第三方开发者接入，暂不明确 |

**📖 主编点评**

这条对你的 content-curator 有直接启发：Attie 的思路是"把生成结果直接放进社交分发链路"，而不是让用户下载一个孤立产物。你的 Agent 也可以照这个思路设计——不要只输出一份 markdown 简报，而是让结果能一键变成可分享的页面或卡片。分发本身就是产品的一部分。

📺 [打开原文](https://techcrunch.com/2026/10/15/bluesky-expands-its-ai-powered-attie-app-to-let-anyone-build-websites-games-and-more/)

---

## 📋 备选阅读

- [Anthropic 给 METR 研究员员工级访问权限，并放弃否决其发布结论的权利](https://techcrunch.com/2026/10/15/anthropic-is-letting-metr-researchers-look-under-the-hood-with-employee-level-access/) —— 让外部机构独立评估风险并保留发布权，是前沿实验室在安全透明度上少见的实质性让步。
  _Aditya Mehta / TechCrunch_
- [ChatGPT 的 Chrome 扩展现在能读取你已打开的标签页](https://www.theverge.com/ai-artificial-intelligence/1012510/openai-chatgpt-google-chrome-tabs) —— Atlas 浏览器没了，但能力转移到 Chrome 扩展上，Agent 获取浏览器上下文的路径变得更直接。
  _Stevie Bonifield / The Verge_
- [Figma 发布新功能，定义 Agent 在其平台上的工作方式](https://techcrunch.com/2026/10/14/figma-announces-new-features-to-define-how-agents-work-on-its-platform/) —— 同时把 code layers 功能开放公测，是设计工具主动为 Agent 定义接口的早期样本。
  _Ivan Mehta / TechCrunch_
- [Stratechery：与 Ari Emanuel 谈娱乐业与 AI](https://stratechery.com/2026/a-conversation-with-ari-emanuel-about-entertainment-and-ai/) —— 好莱坞顶级经纪人对 AI 冲击娱乐业的判断，属于你偏好里的"名人深度访谈"类型。
  _Ben Thompson / Stratechery_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
