# Curio · AI 算力 / 半导体 · 2026-11-21

> 今日 2 条头条 + 3 条备选

_今天最重要的信号有两个：一是 Anthropic 以 $83/股、约 $1.5T 估值完成 IPO，七位创始人合计套现近 $2B，AI 资本周期进入新阶段；二是 Nvidia 的 Huang 事件从丑闻升级为治理与监管危机——SEC 查会计、加州总检察长发传票、Q3 财报首次不披露新加坡收入。两件事叠加，意味着 AI 叙事正从「技术突破」转向「钱和治理怎么收场」。_

---

## 🌟 今日精选

### 2. SEC 调查 Nvidia 潜在会计问题，加州总检察长同步发传票，Huang 事件升级为治理危机

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _ftchd_

Huang 的离职丑闻已经从「CEO 私德」扩散成公司层面的监管问题。SEC 正在查 Nvidia 的会计处理，加州总检察长就 Huang 与中国的关系发出传票，措辞是「亮起红灯，公司可能误导了投资者」。与此同时，Nvidia Q3 财报首次不再单独披露新加坡收入——而新加坡正是此前被质疑的转口通道。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| SEC 调查聚焦 Nvidia 潜在会计问题，消息源向媒体确认 | 会计问题具体指向哪一项（收入确认、关联方、转口销售）尚未公开 |
| 加州总检察长 Rob Bonta 已就 Huang 与中国的关系向 Nvidia 发传票 | 新加坡收入停止披露是合规调整还是回避，需要看下一季 10-Q 的附注 |
| Nvidia Q3 财报不再单独披露新加坡销售收入，此前该地区收入曾达 $104B 量级 | 加州总检察长的传票是否会升级为正式诉讼，时间表不明 |
| Nvidia 董事会在 Huang 离职后表示不打算让其回归，Arm CEO Rene Haas 曾被接触 | Arm CEO 被接触一事若属实，说明董事会已在准备长期接班方案 |
| 一名 Nvidia 董事在丑闻曝光前数周卖出近 $1B 股票 |  |

**📖 主编点评**

如果你关注 AI 算力供应链，这条比任何 GPU 参数都重要：Nvidia 的治理风险会传导到整个 AI 基建的融资成本。建议你把 Q3 财报的「地区收入」附注和 SEC 调查进展放在一起看，判断这是短期噪音还是结构性转折。

📺 [打开原文](https://www.marketscreener.com/news/us-sec-s-nvidia-probe-is-examining-potential-accounting-issues-sources-say-ce785ed3dd8ff627)

---

### 5. Anthropic 数学家称用 Claude 证明 167 年未解的黎曼猜想，同时有人类给出竞争性证明

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Stephen Warwick_

Anthropic 数学家 Levent Alpöge 声称借助 Claude 证明了黎曼猜想——数学界最著名的未解问题之一，悬赏百年。戏剧性的是，几乎同时有另一位人类数学家给出了独立证明。两件事撞在一起，让这条从「AI 攻克数学」变成了「AI 与人类同时逼近同一个证明」，验证工作才刚开始。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Anthropic 数学家 Levent Alpöge 声称用 Claude 证明了黎曼猜想 | AI 辅助证明的具体贡献比例（是 Claude 独立完成还是人机协作）尚不清楚 |
| 黎曼猜想提出至今 167 年，属千禧年大奖难题之一 | 两项证明是否等价、是否都成立，需要数学界数月甚至数年的验证 |
| 同时有一位人类数学家给出竞争性证明 | 若成立，对 AI for Math 的叙事影响远大于对 Anthropic 商业价值的影响 |
| 两项证明目前均未经同行验证 |  |

**📖 主编点评**

别急着转发「AI 证明黎曼猜想」——先看验证。但这件事值得你关注的是方法：如果 Claude 真在证明里起了实质作用，那它用的推理链和工具调用方式，对你做 Agent 的「长链推理」设计有直接参考价值。

---

## 📋 备选阅读

- [Phison 展示内置 NPU + 64GB 内存的 SSD，可在盘上跑 PyTorch 和 llama.cpp](https://www.tomshardware.com/pc-components/ssds/phison-details-ssd-with-a-built-in-npu-and-64gb-of-memory-that-supports-pytorch-and-llama-cpp-running-on-the-drive-second-design-merges-fast-pslc-cache-and-qlc-capacity-behind-one-controller) —— 计算存储（computational storage）的实机方案，SC26 展出，对推理部署的硬件形态有长期影响。
  _Shane Downing_
- [律师用 12 张二手 V100 搭 $9,450 私有 AI 服务器，跑满 DeepSeek V4.1 Flash 全部专家](https://www.tomshardware.com/tech-industry/artificial-intelligence/lawyers-usd9-450-private-ai-server-of-12-used-nvidia-v100s-now-runs-every-deepseek-v4-1-flash-expert-at-4-bit-nvfp4-up-to-184-tokens-per-second-on-code-and-long-documents-start-answering-in-about-half-the-time) —— 4-bit NVFP4 + 二手 V100 的推理优化实例，184 tok/s，是「低成本私有部署」的硬核参考。
  _Shane Downing_
- [电力与散热限制迫使 10 万+ 加速器 AI 集群拆到多个数据中心](https://www.tomshardware.com/tech-industry/supercomputers/power-and-cooling-limits-push-100-000-accelerator-ai-clusters-past-single-data-centers-google-cisco-and-marvell-target-scale-across-networking-across-regions) —— 单机房已装不下顶级 AI 集群，跨区域组网成为新工程问题，Google/Cisco/Marvell 在押注。
  _Anton Shilov_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
