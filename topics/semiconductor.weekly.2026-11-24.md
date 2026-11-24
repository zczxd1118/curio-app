# Curio · AI 算力 / 半导体 · 2026-11-24

> 今日 1 条头条 + 4 条备选

_今天全网只有一个真信号：Jensen Huang 被 Nvidia 董事会请回 CEO，距他因丑闻辞职不到两周，Trump 亲自打电话进董事会施压。这件事的产业含义不是八卦——它把「Nvidia 的公司治理、SEC 会计调查、Megaspeed 出口管制、国会听证」四条线拧成一根绳，接下来一周 Nvidia 的每一次表态都会牵动算力供给和 AI 资本叙事。另一条值得单独拎出来的是 Anthropic 发布 Claude Ship，让 Agent 自己 review、修、批准代码——这是把 vibe coding 从「人写 prompt」推进到「Agent 管合并」的一步。_

---

## 🌟 今日精选

### 1. Nvidia 董事会把 Jensen Huang 请回 CEO，距辞职不到两周，Trump 称「我打电话说服了他们」

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _alanwong_

11 月 12 日 Huang 因与 Megaspeed 高管 Alice Huang 的关系及疑似中国间谍传闻辞职，董事会一度启动调查。11 月 23 日官方新闻稿宣布复职，CNBC 与 NYT 均报道 Trump 直接致电董事会推动此事。Huang 对员工说「第二次我会做个更好的 CEO」。这不是一次普通的人事反复，而是把公司治理、出口管制与政治干预三件事同时摆上了台面。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Nvidia 官方新闻稿确认董事会重新任命 Huang 为总裁、CEO 及董事 | 董事会调查结论是否公开、以何种措辞收尾，目前只有「复职」这一结果，没有披露调查细节 |
| 辞职发生在 11 月 12 日，复职在 11 月 23 日，间隔不到两周 | Megaspeed 是否真被列入美国实体清单尚未落地，TechCrunch 用的是「appears headed for」 |
| Trump 对 CNBC 表示「我跟他们谈了……我说服了他们」，NYT 报道其直接介入董事会 | 国会两党已公开批评此次复职（CNBC 报道称「failure of character」），听证会是否会升级为对 Nvidia 出口许可的实质审查仍不明 |
| Huang 已安排下周出席参议院听证，就相关传闻作证 | Huang 复职对 Nvidia 对华销售政策、对新加坡收入披露口径的实际影响，短期看不到可验证动作 |
| SEC 对 Nvidia 的会计问题调查仍在进行，涉及新加坡销售披露与 Megaspeed 关系 | 员工内部并非一致欢迎，Tom's Hardware 报道有员工称「这是最糟的结果」 |

**📖 主编点评**

你不需要追这条的八卦细节，但要盯两个可操作的点：一是下周参议院听证会不会牵出对华出口许可的新限制，那会直接改变国内可拿到的算力档位；二是 Nvidia 下季度财报是否恢复披露新加坡销售——这是判断「算力到底卖给了谁」的最硬指标。如果你在做任何依赖云端大模型 API 的项目，把供应商冗余当成默认前提，别把单点押在一条供给链上。

📺 [打开原文](https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director)

---

## 📋 备选阅读

- [Nvidia 被指通过给 AI 初创注资、让其回购自家 GPU 来人为制造稀缺](https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus) —— 与 Huang 复职同一条线，讲的是「循环融资推高 GPU 价格」的指控，是理解 Nvidia 收入结构质疑的关键背景，但本身是旧闻重提。
  _speckx_
- [TSMC 遭黑客攻击，已向 SEC 提交声明](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000800/a20261112statementregardin.htm) —— 半导体供应链安全事件，SEC 8-K 原文可查，但细节披露有限，等后续报道再深看。
  _gmays_
- [日本把光刻机装进卡车，用 mobileFab 应对十年半导体工程师荒](https://www.tomshardware.com/tech-industry/semiconductors/japan-puts-chipmaking-labs-inside-trucks-with-mobilefab-trucks-pack-30-cm-lithography-gear-to-tackle-a-10-year-semiconductor-engineer-shortage) —— 车载 30cm 光刻教学平台，是半导体人才短缺的具体解法，对电子信息的你有职业参考价值，但产业影响偏长期。
  _Bruno Ferreira_
- [共享 CXL 内存池的软件同步开销可能拖住多机扩展](https://www.tomshardware.com/pc-components/dram/shared-cxl-memory-pools-come-with-steep-software-tax-that-could-stall-multi-server-scaling-ut-arlington-shares-real-world-test-that-measured-four-servers-sharing-the-same-pool-at-sc26) —— UT Arlington 与 Intel 在 SC26 实测四机共享 CXL 池的同步成本，是推理 KV cache 扩展的硬核数据，但偏学术。
  _Shane Downing_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
