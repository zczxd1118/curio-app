# Curio · AI 算力 / 半导体 · 2026-11-07

> 今日 1 条头条 + 3 条备选

_今天最重要的信号是同一件事的两面：中期选举民主党大胜后，市场把数据中心和 AI 资本开支当成政治风险来定价，Nasdaq 两天跌进修正区间、蒸发 2.5 万亿美元；但 OpenAI 同一天以 1.25 万亿美元估值再融 110 亿。资本在重新给 AI 定价，而不是离场。另一条线是 Nvidia 的 RTX Spark 加密固件把 Linux 推理压到 35% 速度，硬件层的封闭化开始影响实际算力。_

---

## 🌟 今日精选

### 3. Nvidia RTX Spark 加密固件被指把 Linux 推理速度压到 35%

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _novaRom_

HN 上 614 分的讨论指出，Nvidia 新款 RTX Spark 笔记本的加密固件在 Linux 下把推理速度限制到约 35%，Windows 下不受影响。如果属实，这是消费级 GPU 上'平台锁定'从驱动层下沉到固件层的信号，直接影响本地跑模型的开发者。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| HN 讨论帖获得 614 分，指向 mindstudio.ai 的实测博客 | 35% 这个数字是否可复现、是否只影响特定模型和驱动版本，需要独立验证 |
| 报告称加密固件在 Linux 环境下限制推理性能至约 35% | 限制是反盗版/反挖矿设计还是刻意压制 Linux 生态，Nvidia 未回应 |
| 同期 RTX 5090 街价突破 9000 美元，5080 从官方商店下架、街价达 MSRP 的 2.2 倍 | 消费级 GPU 的固件封闭化会不会蔓延到数据中心卡，目前无证据 |
| Nvidia 收紧东南亚云厂商的 GPU 追踪，要求加入 Fleet Intelligence 才能获得官方合作伙伴资格 | 社区是否有绕过方案（如开源驱动或固件降级）尚不明朗 |

**📖 主编点评**

如果你打算在本地跑推理或做 Agent 的离线实验，这条直接影响你的硬件选型——别急着买 RTX Spark 系列做 Linux 开发机。更值得记的是这个趋势：消费级硬件的封闭化正在从驱动层往固件层走，你选设备时要把'Linux 下能不能跑满'当成一个必查项。

📺 [打开原文](https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop)

---

## 📋 备选阅读

- [Marvell 以 1150 亿美元全股票收购 Lumentum](https://www.tomshardware.com/tech-industry/semiconductors/marvell-to-buy-lumentum-in-usd115-billion-all-stock-deal-combined-company-to-supply-scale-up-and-scale-in-optics-for-ai-data-centers) —— AI 数据中心光互连的整合大单，1150 亿美元全股票，产业级别但离你的日常关注稍远。
  _Etiido Uko_
- [GlobalFoundries 详解 FDX Fusion：不用 EUV 做到 7nm 级性能，目标 2030 量产](https://www.tomshardware.com/tech-industry/semiconductors/globalfoundries-vp-details-fdx-fusion-technology-sporting-7nm-class-performance-without-the-need-for-euv-tools-company-targets-2030-for-high-volume-manufacturing-with-planar-transistors-in-tow) —— 平面 FD-SOI 绕开 EUV 的路线，对半导体工艺格局有意义，但 2030 量产太远，短期无行动价值。
  _Anton Shilov_
- [IBM、AMD 与美国国家实验室共建量子-经典混合系统](https://www.eetimes.com/ibm-amd-mix-quantum-and-ai-at-u-s-national-lab/) —— 在 Oak Ridge 部署混合量子-经典系统加速纠错研究，目标 2028，属长期基础设施布局。
  _Alan Patterson_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
