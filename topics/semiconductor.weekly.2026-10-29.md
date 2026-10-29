# Curio · AI 算力 / 半导体 · 2026-10-29

> 今日 1 条头条 + 4 条备选

_今天最重要的信号是 Google 一天内连发 Gemini 4 Carbon 和 Genie 4，前沿模型迭代节奏已经压到周级；同时 Anthropic IPO 的估值争议和微软单季从 OpenAI 拿到 100 亿美元收入，说明 AI 资本叙事正在从'讲故事'转向'算账'。对做 Agent 的你，值得盯的是 Google 把 Gemini/Search 开放给第三方 App 的开发者平台——这是 Agent 生态的入口之争。_

---

## 🌟 今日精选

### 2. TSMC 考虑 CoWoS 封装涨价 20%，Nvidia Blackwell 与 Rubin 把产能压到设备交期 8 个月

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

据 Tom's Hardware 报道，TSMC 正评估把 CoWoS 先进封装价格上调最多 20%，原因是 Nvidia Blackwell 和即将到来的 Rubin 芯片把封装产能逼到极限，相关设备交付周期已拉长到 8 个月。这不是单点涨价，而是 AI 算力供应链最紧的那一环在重新定价。叠加 SK Hynix 创纪录的 Q3 业绩（AI 内存驱动），上游'卖铲子'的议价权还在加强。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| TSMC 据报正评估 CoWoS 封装涨价，幅度最高 20% | 涨价是否落地、幅度是否真到 20%，TSMC 未官方确认，属'据报'级别 |
| 涨价压力来自 Nvidia Blackwell 与 Rubin 芯片的封装需求 | 封装涨价会传导到 GPU 售价还是被 Nvidia 吸收，取决于双方长约条款，未公开 |
| CoWoS 相关设备交付周期已拉长至 8 个月 | 8 个月设备交期意味着 2027 年产能扩张节奏已被锁定，短期缓解无望 |
| SK Hynix 同日公布创纪录 Q3 业绩，明确归因于 AI 内存需求激增 | Solidigm 450 亿美元建厂仍在讨论阶段，落地时间和补贴条件不明 |
| SK Hynix 旗下 Solidigm 据报筹划在美国建 450 亿美元闪存工厂 |  |

**📖 主编点评**

这条对你不是'买显卡'的问题，而是判断 AI 推理成本曲线：封装和内存双双涨价，意味着未来 6-12 个月云端推理单价难降。你做 content-curator 如果打算长期跑 LLM 调用，现在就该把'本地小模型兜底 + 云端大模型精选'的混合架构写进设计，而不是假设 API 会越来越便宜。

📺 [打开原文](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-reportedly-weighs-20-percent-cowos-price-increase-as-nvidia-blackwell-and-rubin-chips-put-pressure-on-packaging-capacity-equipment-lead-times-stretch-to-eight-months)

---

## 📋 备选阅读

- [Nvidia 联合 Oracle 把独立 Vera CPU 实例上线 OCI，多吉瓦级部署](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-and-oracle-bring-vera-cpu-instances-online-in-multi-gigawatt-deployment-oci-superclusters-also-set-to-expand-with-rubin-only-clusters-attached-to-dual-xeon-6-hosts) —— Nvidia 从 GPU 往 CPU 延伸的信号，影响未来云上推理实例选型，但离你较远。
  _Tom's Hardware_
- [马来西亚查获 30 台服务器内藏价值 1200 万美元先进 AI 芯片，疑为走私中转](https://www.tomshardware.com/tech-industry/policy/malaysia-seizes-usd12-million-worth-of-advanced-ai-chips-hidden-inside-30-servers-customs-says-suspected-smuggling-network-used-the-country-as-a-transit-hub) —— 出口管制的现实执行案例，说明高端算力仍是稀缺品，但事件本身对开发者无直接行动项。
  _Tom's Hardware_
- [AI 元件涨价迫使全球最大 PC 厂商把产能迁回中国](https://www.tomshardware.com/tech-industry/manufacturing/ai-component-hikes-force-the-worlds-largest-pc-makers-to-return-manufacturing-capacity-to-china-brands-to-seek-lower-production-costs-and-efficiency-in-established-supply-chain) —— AI 挤占元件产能的连锁反应，供应链视角有意思，但和你的项目无直接关系。
  _Tom's Hardware_
- [GPU-unlock：在 Nvidia 30 系卡上解锁 FP/BF16 指令发射率](https://github.com/Zagitta/gpu-unlock) —— HN 350 分的硬核项目，对本地推理优化有参考价值，但门槛高、受众窄，放备选。
  _Hacker News_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
