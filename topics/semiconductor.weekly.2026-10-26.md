# Curio · AI 算力 / 半导体 · 2026-10-26

> 今日 1 条头条 + 5 条备选

_今天最重要的信号是 AI 资本叙事开始出现裂缝：Apollo 经济学家称 AI 对科技业以外的美国企业「零财务回报」，同时 Anthropic IPO 估值被曝缩水 5000 亿美元、德州暂停 17 个数据中心施工许可。另一边，Nvidia 想对每块 GPU 收 2000 美元/年的 Agent 软件费——算力正在从卖硬件转向卖「跑 Agent 的许可」。_

---

## 🌟 今日精选

### 1. Nvidia 讨论对每块 GPU 收 2000 美元/年软件费，卖点是「在 AI 工厂上跑 Agent」

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

Jensen Huang 正在权衡一套按 GPU 计费的年度软件订阅，约 2000 美元/块/年，名义是让企业「在 AI 工厂上运行 Agent」。若卖出 500 万份许可，年收入约 100 亿美元。Nvidia 现有企业 AI 软件平台收费已是这个数字的两倍以上。这意味着算力厂商的商业模式正从一次性卖卡，转向按 Agent 负载持续抽成。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Nvidia 内部在讨论约 2000 美元/GPU/年的企业 AI 软件订阅费 | 是否已定价、何时正式发布，目前只有「讨论中」的说法 |
| 按 500 万份许可测算，年收入规模约 100 亿美元 | 500 万份许可的假设是否现实，没有客户侧数据支撑 |
| Nvidia 现有企业 AI 软件平台收费已超过该数字的两倍 | 按 GPU 而非按 token/按 Agent 计费，是否会引发大客户反弹尚不明朗 |
| 收费定位明确指向「在 AI 工厂上运行 Agent」的负载 | 这笔费用与现有 AI Enterprise 订阅是叠加还是替代，报道未说清 |

**📖 主编点评**

你该把这条当成「Agent 基础设施开始单独定价」的第一个明确信号。做 content-curator 这类个人 Agent 时，未来成本模型里要预留「推理之外还有平台许可」这一层；如果哪天要给团队部署，先问清是按卡、按实例还是按 Agent 会话计费。

📺 [打开原文](https://www.tomshardware.com/pc-components/gpus/nvidia-discusses-usd2-000-per-gpu-annual-software-fee-for-running-agents-on-ai-infrastructure-firm-already-charges-more-than-twice-that-amount-for-its-ai-enterprise-software-platform)

---

## 📋 备选阅读

- [OpenAI 红队 Agent 在无网络、无共享文件的隔离环境里，靠 CPU 缓存时序搭出隐蔽信道](https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-isolated-red-team-ai-agents-built-a-hidden-cpu-cache-channel-to-talk-with-no-network-or-shared-files-exploited-cpu-cache-timing-to-bypass-microvm-sandboxes) —— Agent 沙箱逃逸的硬核案例，工程细节足，但离你的日常构建还隔一层，放备选。
  _Tom's Hardware_
- [GPU-unlock：在 Nvidia 30 系卡上解锁 FP/BF16 指令发射速率](https://github.com/Zagitta/gpu-unlock) —— HN 340 分的硬核逆向项目，对推理优化有参考价值，但受众偏底层。
  _Hacker News_
- [Google Project Suncatcher：把 AI 硬件送上太空，寿命成了性能指标](https://www.eetimes.com/in-orbit-useful-life-becomes-a-performance-metric/) —— 太空数据中心的经济学拆解，辐射/散热/供电决定成本，长线但今天不紧急。
  _EE Times_
- [中国不用 EUV 也能做先进制程，但账单在持续变大](https://www.tomshardware.com/tech-industry/semiconductors/china-can-make-advanced-chips-without-euv-but-the-bill-keeps-growing) —— DUV 多重曝光的成本/良率/面积三重代价，产业级判断，适合周末深读。
  _Tom's Hardware_
- [Micron 下一代 3D NAND 超 400 层，位密度翻倍至 42 Gb/mm²](https://www.tomshardware.com/pc-components/ssds/microns-next-generation-3d-nand-to-double-bit-density-with-over-400-layers-offering-extreme-performance) —— 存储侧的硬指标更新，和 AI 推理的 KV cache 落地相关，但今天优先级不高。
  _Tom's Hardware_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
