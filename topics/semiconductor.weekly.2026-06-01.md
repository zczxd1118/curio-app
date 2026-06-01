# Curio · AI 算力 / 半导体 · 2026-06-01

> 今日 1 条头条 + 5 条备选

_今天三条主线交叉：一是 OpenAI 计划本周递交 IPO 招股书，叠加 SpaceX 1.8 万亿美元 IPO 倒逼指数规则改写，AI 独角兽集体进入定价时刻；二是 Computex 2026 + GTC Taipei 同步开锣，Nvidia Vera Rubin 量产 + N1X PC 处理器入场，Intel 18A Xeon 6+ 反扑，AI 硬件竞争从 GPU 蔓延到 CPU/PC 全栈；三是股票域：SpaceX IPO 招股书极度不公平条款（禁止股东诉讼、Musk 永久控制），多家媒体警告散户慎打新——这是 2026 年下半年股市最大的风险事件。Stratechery 本周新增 Eric Seufert 访谈值得你听完。_

---

## 🌟 今日精选

### 2. 黄仁勋 Computex 表态：Vera Rubin 已全面量产，Nvidia 自己造 PC 处理器进军 AI PC 入口

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _华尔街见闻 API_

Computex 2026 + GTC Taipei 同步召开，黄仁勋宣布下一代数据中心平台 Vera Rubin 已全面量产，并推出面向 AI Agent 的 Vera CPU；Phoronix 实测 Vera 的 Olympus 核心性能强劲。同时 Nvidia 长期酝酿的 N1/N1X PC SoC 规格泄露——20 个 Arm 核 + 6144 CUDA 核心，对标桌面 RTX 5070，Dell XPS 笔记本将首发。这意味着 Nvidia 不再只卖加速卡，而是要从数据中心一直吃到 AI PC 端点。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 黄仁勋官宣 Vera Rubin 全面量产，AI Agent 是 Nvidia 下一阶段重点（华尔街见闻 6/1） | N1X 真实出货时间和良率受 TSMC 产能影响，2026 年 Q3 前应不会上量 |
| N1X SoC 顶配 20 Arm 核 + 6144 CUDA 核心，标准 N1 提供 12 核 / 10 核两档（Tom's Hardware 5/31） | Nvidia 自己做 PC 处理器，Intel / AMD 在 AI PC 这条线的话语权会被压缩 |
| Dell 在 Computex 确认搭载 Nvidia N1X 的 XPS 笔记本（VideoCardz / hn:48343372） | Vera Rubin 量产后 H200 / B200 的二手市场价格可能松动，国内白手套渠道留意 |
| Vera 的 Olympus 核心 Phoronix 评测：每线程性能优秀（hn:48291230） | AI Agent 重点意味着 Nvidia 软件栈（NeMo / Blueprints）会进一步绑客户，自研推理框架的窗口在收窄 |
| AI 需求已从 GPU 蔓延到 "传统 PC 大厂"，戴尔股价涨至 420 美元，大摩公开 "认错"（华尔街见闻 6/1） |  |

**📖 主编点评**

你做 Agent 项目时，部署侧别再默认 "租 H100 / 用 Together"。Nvidia 把 Vera + N1 推下来后，本地化 inference 的成本曲线会变陡——尤其 Mac mini / Snapdragon X 这种 30W 级设备未来一年会承接更多个人 Agent 推理。content-curator 这种轻量场景，未来直接跑在用户机器上是主流路径，不是 fallback。

📺 [打开原文](https://wallstreetcn.com/articles/3773548)

---

## 📋 备选阅读

- [Intel Xeon 6+ Clearwater Forest 用 18A 工艺杀回数据中心，288 核 / 576MB L3](https://www.tomshardware.com/pc-components/cpus/intel-xeon-6-clearwater-forest-puts-18a-in-the-data-center-with-up-to-288-cores-576-mb-of-l3-cache-new-xeon-6990e-is-30-percent-faster-per-thread-than-192-core-amd-epyc-9965-says-intel) —— Intel 自报每线程比 AMD EPYC 9965 快 30%，18A 工艺真正进数据中心——AMD 在云厂的优势第一次受真正威胁。
  _Tom's Hardware_
- [Intel Crescent Island AI GPU 在 Computex 详细披露：480GB LPDDR5X 对抗 HBM 短缺](https://www.tomshardware.com/pc-components/gpus/intel-details-long-awaited-crescent-island-ai-gpu-at-computex-boasts-up-to-480-gb-of-lpddr5x-to-combat-memory-shortages-company-shares-more-details-of-its-xe3p-inference-accelerator-at-computex) —— Intel 用 LPDDR5X 绕开 HBM 短缺，主打推理场景——如果价格够低，是 H200 在中端推理市场的真实替代。
  _Tom's Hardware_
- [SoftBank 计划在法国投 870 亿美元建 AI 数据中心](https://www.tomshardware.com/tech-industry/softbank-to-spend-up-to-75-billion-on-french-ai-data-centers) —— 选址法国是冲着核电网；SoftBank 自己背着 1300 亿美元债务、3 月又借 400 亿过桥——杠杆已经打满。
  _Tom's Hardware_
- [Nikon 用低价反扑 ASML 的光刻机垄断](https://www.tomshardware.com/tech-industry/nikon-plans-to-undercut-asml-on-price-to-win-back-chipmaking-lithography-customers) —— 用 ArF 工具自有制造低价反扑美国客户，是中美芯片博弈下日本企业的策略调整，不只是商业新闻。
  _Tom's Hardware_
- [TSMC 间谍案宣判：被告最高 10 年监禁](https://www.taipeitimes.com/News/front/archives/2026/04/28/2003856358) —— 中国台湾首次按《国安法》重判 TSMC 内部泄密，对所有大陆背景半导体从业者的招聘背景调查会更严。
  _Taipei Times_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
