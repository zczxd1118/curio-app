# Curio · 大厂 AI 动态 · 2026-10-16

> 今日 2 条头条 + 4 条备选

_今天最值得看的两条线：一是 ASML 单季营收 130 亿美元创纪录、客户已排到 2029-2030 年产能，AI 算力需求把上游设备商逼到扩产极限；二是 Meta 联合 Apple 发布可在 Mac 本地跑的开放权重模型 Muse Spark Open，端侧模型开始有真正的产品级落地。金融侧则相反——亚洲芯片股因 AI 融资担忧回落，Firmus 数据中心 IPO 48 小时崩盘，热钱正在重新定价。_

---

## 🌟 今日精选

### 2. Meta 联合 Apple 发布 Muse Spark Open，首个可在 Mac 本地运行的开放权重模型

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _TechCrunch_

Meta 发布开放权重模型 Muse Spark Open，自称'迄今最强的美国开放权重模型'，并称是同类中首个能在 Apple Silicon 上本地运行、通过 MLX 框架优化的模型。Apple 罕见地参与了联合发布。这条的意义不在参数规模，而在'开放权重 + 端侧可跑'第一次被两家大厂同时背书。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Meta 发布 Muse Spark Open，定位为美国最强开放权重模型 | '最强开放权重'是 Meta 自评，尚无独立评测（如 Artificial Analysis）佐证 |
| 模型可在 Apple Silicon 上本地运行，使用 Apple 的 MLX 框架 | 本地运行的具体硬件门槛（内存、芯片代际）未披露 |
| Apple 官方参与了此次联合发布 | Apple 参与程度是技术合作还是市场联合，尚不清楚 |
| Meta 称其为同类中首个具备该本地运行能力的模型 | 对开发者生态的实际吸引力取决于许可证条款，目前细节不足 |

**📖 主编点评**

端侧开放权重模型对你这种做个人 Agent 的人直接相关：如果 Muse Spark Open 真能在 Mac 上跑出可用质量，你的 content-curator 可以考虑把一部分摘要/分类任务从 API 挪到本地，省成本也省延迟。建议先跑一个 20 条样本的对比测试，别急着迁移。

📺 [打开原文](https://techcrunch.com/2026/10/15/meta-launches-an-open-weight-model-that-runs-on-macs/)

---

### 5. Anthropic 给 METR 研究员员工级访问权限，并放弃否决其评估报告的权利

**[大厂 AI 动态]** · ⭐⭐⭐⭐ · _TechCrunch_

Anthropic 允许独立评估机构 METR 的研究员以接近员工的权限查看其模型内部，并主动放弃阻止 METR 发布评估结论的权利。METR 将自行发布对 Anthropic 风险、事故和实践的评估。这是前沿实验室在透明度上少见的实质性让步，不是公关声明。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Anthropic 给 METR 研究员接近员工级别的模型访问权限 | '员工级访问'的具体范围未披露，可能仍有边界 |
| Anthropic 放弃阻止 METR 发布评估报告的权利 | METR 的独立性最终取决于其资金来源和发布节奏 |
| METR 将独立发布对 Anthropic 风险与事故的评估 | 其他前沿实验室（OpenAI、Google）是否会跟进，未知 |
| 这是双方合作的具体条款，非泛泛承诺 | 评估结果的实际约束力有限，Anthropic 仍可选择性回应 |

**📖 主编点评**

如果你关心 AI 治理，这条比任何'AI 安全宣言'都实在——可验证的第三方访问权是硬约束。对你的项目没有直接用处，但值得作为'如何设计可信评估机制'的参考案例存进素材库。

📺 [打开原文](https://techcrunch.com/2026/10/15/anthropic-is-letting-metr-researchers-look-under-the-hood-with-employee-level-access/)

---

## 📋 备选阅读

- [ChatGPT 现在能读取你的 Chrome 标签页](https://www.theverge.com/ai-artificial-intelligence/1012510/openai-chatgpt-google-chrome-tabs) —— Atlas 浏览器没了，但 Chrome 扩展升级后能直接读已打开的标签，是 Agent 接管浏览器的又一步。
  _The Verge_
- [Bluesky 的 Attie 扩展成'社交 vibe coding'，人人可做游戏和网站](https://techcrunch.com/2026/10/15/bluesky-expands-its-ai-powered-attie-app-to-let-anyone-build-websites-games-and-more/) —— 把 vibe coding 塞进社交网络，产物可直接分享，是'AI 生成 + 社交分发'的新形态。
  _TechCrunch_
- [Figma 发布新功能，定义 Agent 在其平台上的工作方式](https://techcrunch.com/2026/10/14/figma-announces-new-features-to-define-how-agents-work-on-its-platform/) —— 设计工具开始为 Agent 定义接口规范，code layers 进入开放 beta，对做工具的人有参考价值。
  _TechCrunch_
- [Stratechery 对话 Ari Emanuel：娱乐业与 AI](https://stratechery.com/2026/a-conversation-with-ari-emanuel-about-entertainment-and-ai/) —— 好莱坞顶级经纪人对 AI 冲击娱乐业的深度对话，符合你'想看名人访谈'的偏好。
  _Ben Thompson_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
