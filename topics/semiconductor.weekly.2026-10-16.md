# Curio · AI 算力 / 半导体 · 2026-10-16

> 今日 2 条头条 + 4 条备选

_今天最值得盯的是两条线：一是 ASML 交出 130 亿美元创纪录季度、并说客户已经在预订 2029-2030 年的产能，AI 资本开支的紧张程度从下游烧到了最上游的设备端；二是 Meta 联合 Apple 发布能在 Mac 本地跑的开放权重模型 Muse Spark Open，加上 Bluesky 把 Attie 扩成"社交 vibe coding"，端侧与轻量 Agent 的落地速度明显快于预期。_

---

## 🌟 今日精选

### 1. ASML 单季营收 130 亿美元创纪录，客户已开始预订 2029-2030 年光刻机产能

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Anton Shilov / Tom's Hardware_

ASML 交出史上最强单季财报，营收 130 亿美元，同时宣布扩产。CEO 的说法比数字更关键：客户已经在为 2029、2030 年的产出下单，需求可能超过 2027-2028 年的供给。这意味着 AI 算力扩张的瓶颈正从芯片设计、封装一路前移到最上游的光刻设备。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| ASML 本季度营收 130 亿美元，为公司历史最高单季纪录 | "需求超过供给"是 ASML 自己的口径，实际交付节奏仍取决于零部件与供应链 |
| 公司明确承诺扩大产能，并称盈利能力同步创纪录 | 提前数年下单不等于最终不砍单，2027 年后的订单可见度存疑 |
| 客户已提前数年下单，订单窗口延伸到 2029-2030 年产出 | 扩产能否在 2028 年前落地，取决于洁净室与人才而非资本 |
| CEO 表示需求可能超出 2027-2028 年的供给能力 | 若 AI 资本开支在 2027 年降温，这批长单可能被重新议价 |
| 同期另一篇报道称 ASML 正努力跟上设备需求，AI 支出持续繁荣 |  |

**📖 主编点评**

这条不是让你去看半导体股票，而是提醒你：AI 的"算力叙事"已经进入设备与产能的硬约束阶段。你做 content-curator 这类 Agent 项目，未来一两年最现实的变化是推理成本下降速度可能放缓——所以在设计 Agent 时，别默认"模型会越来越便宜"，把缓存、上下文裁剪、本地小模型兜底这些工程手段提前做进去，比事后优化省事得多。

📺 [打开原文](https://www.tomshardware.com/tech-industry/semiconductors/asml-reports-record-usd13-billion-quarter-vows-to-expand-capacity-as-demand-for-lithography-equipment-soars-customers-eager-to-secure-orders-in-2030-as-demand-is-expected-to-outstrip-2027-and-2028-supply)

---

### 3. Nvidia 洽谈收购美国开放模型创业公司 Reflection AI

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _arkj / Hacker News_

FT 报道 Nvidia 正在洽谈收购 Reflection AI，一家主打开放模型的美国创业公司。如果成真，这是 Nvidia 从"卖铲子"往"自己挖矿"再走一步——它已经不满足于只提供算力，开始直接持有模型层资产。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| FT 报道 Nvidia 正与 Reflection AI 洽谈收购事宜 | 交易是否达成、价格与结构均未披露，可能谈崩 |
| Reflection AI 定位为美国开放模型方向的创业公司 | Nvidia 收购模型公司是否触及反垄断审查，尚不明朗 |
| 消息在 Hacker News 上获得 179 点讨论 | Reflection AI 的技术资产（权重、团队、数据）价值未被独立评估 |
|  | 此举是战略投资还是完整收购，报道口径模糊 |

**📖 主编点评**

值得你留意的是"开放模型"这条线的资本化速度。如果 Nvidia 真的把模型层收进体系，未来开放权重模型的发布节奏和许可条款可能被大厂主导。你做个人 Agent 项目时，模型选型别只盯一家，把切换成本压低（抽象一层 provider 接口）是长期正确的做法。

📺 [打开原文](https://www.ft.com/content/052610c5-22b4-4dd4-932e-b7f9f0628b6a)

---

## 📋 备选阅读

- [TSMC 确认正考虑与 Elon Musk 合作 Terafab 扩产，但坚持由台积电运营](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-confirms-it-is-considering-terafab-chipmaking-expansion-with-elon-musk-ceo-insists-tsmc-would-have-to-run-texas-based-project) —— 台积电首次公开回应 Terafab，明确"要合作就得我来运营"，是理解美国本土产能博弈的关键一手表态。
  _Anton Shilov / Tom's Hardware_
- [SK hynix 拿美国建厂换中国设备出口许可，态度强硬](https://www.tomshardware.com/pc-components/ssds/sk-hynix-reportedly-playing-hardball-with-trump-admin-over-3d-nand-fab-company-demands-increased-chipmaking-equipment-exports-to-china-in-exchange-for-us-fab) —— 把建厂当筹码换大连工厂的设备出口，是出口管制下存储厂商少见的主动议价案例。
  _Anton Shilov / Tom's Hardware_
- [Nvidia RTX 5090 从 Micro Center 消失，传产线停摆](https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090-disappears-from-micro-center-amid-rumors-of-a-production-halt-retailer-flags-flagship-as-not-carried-as-stock-mysteriously-vanishes) —— 零售商标注"不再销售"，叠加 GB202 产能转向工作站 GPU 的传闻，消费级旗舰的供给逻辑在变。
  _Zhiye Liu / Tom's Hardware_
- [Sipeed 推出国产 DGX Spark 竞品 MaixStation，预计售价 3999 美元](https://www.tomshardware.com/desktops/mini-pcs/sipeed-reveals-chinese-made-dgx-spark-and-ryzen-ai-halo-rival-expected-to-cost-usd3-999-maixstation-pairs-axeras-ax8860p-with-128gb-of-lpddr5x-at-273-gb-s-with-promising-local-ai-performance-claims) —— 128GB LPDDR5X、273 GB/s 带宽，对标 DGX Spark，是本地跑大模型硬件里值得关注的新选项。
  _Shane Downing / Tom's Hardware_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
