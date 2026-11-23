# Curio · AI 算力 / 半导体 · 2026-11-23

> 今日 2 条头条 + 4 条备选

_今天最重要的信号有两个：一是 Nvidia 的治理危机已经从八卦升级成财务与监管问题——SEC 开始查会计口径、新加坡 104B 营收口径被藏起来，黄仁勋去留成了政治议题；二是 Anthropic IPO 定价 83 美元、估值 1.5 万亿，但信用评级是垃圾级，AI 泡沫的定价权正从叙事转向债券市场。这两条其实是同一件事的两面：AI 资本循环开始被审计。_

---

## 🌟 今日精选

### 1. SEC 调查 Nvidia 会计问题，黄仁勋去留之外，真正的风险是营收口径

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _ftchd_

Nvidia 的危机已经从 CEO 私德问题转向财务披露。SEC 的 probe 聚焦会计处理，而此前 FT 已报道公司停止单独披露新加坡销售额——同期营收冲到 104B 美元。把这两件事放一起看：市场真正担心的不是谁当 CEO，而是 GPU 需求里有多少是 Nvidia 自己出资的创业公司买回去的。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| SEC 正在调查 Nvidia 潜在的会计问题，消息源对 MarketScreener 确认 | SEC 调查目前只是"潜在会计问题"，尚未定性为违规，最终可能无实质处罚 |
| Nvidia 已停止单独披露新加坡地区销售额，同期总营收达 104B 美元 | 新加坡口径消失与 Megaspeed 关联公司的关系仍是推测，官方未解释 |
| 此前 TechPowerUp 等媒体报道 Nvidia 通过投资 AI 创业公司让其回购 GPU，被指人为制造稀缺 | 循环融资（circular financing）是否构成收入确认问题，取决于审计对"实质控制"的认定 |
| 黄仁勋已于 11 月 12 日辞去 CEO，公司董事在丑闻前数周卖出近 10 亿美元股票 | 黄仁勋回归的可能性存在，但会与 SEC 调查进度绑定 |
| 特朗普公开表态称董事会重新聘用黄仁勋对公司与美国都最好 |  |

**📖 主编点评**

如果你在跟踪 AI 算力链，别只盯黄仁勋的新闻热度，去翻 Nvidia 下一份 10-Q 里地区收入拆分和应收账款周转——那才是判断 GPU 真实需求的硬指标。对你的 content-curator 项目也是个提醒：信源里"高管八卦"和"财务披露"要分开打标签，前者噪声大、后者才是信号。

📺 [打开原文](https://www.marketscreener.com/news/us-sec-s-nvidia-probe-is-examining-potential-accounting-issues-sources-say-ce785ed3dd8ff627)

---

### 4. Architect Labs 称 AI agent 从零设计出全新 CPU 架构 Frostbite，能效比达 4.59 倍

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Shane Downing_

初创公司 Architect Labs 声称其 AI agent 从零设计了一款叫 Frostbite 的 CPU，采用 interaction-net 架构，在流片前测试中每瓦性能是传统顺序执行核心的 4.59 倍。这是"AI 设计硬件"从论文走向公司声明的又一步，但注意关键词：pre-silicon，也就是还没流片验证。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Architect Labs 称 AI agent 从零设计了 Frostbite CPU 架构 | 4.59 倍是仿真/建模结果，流片后能否复现是最大不确定性 |
| 宣称 interaction-net 设计在流片前测试中达到 4.59 倍每瓦性能 | "AI 从零设计"里人类工程师参与度未披露，可能是 AI 辅助而非自主设计 |
| 目前处于 pre-silicon 阶段，尚无实测芯片 | interaction-net 架构的可制造性与良率完全未知 |

**📖 主编点评**

对你这种硬件背景 + AI 产品的人，这条的价值在方法论：AI agent 做架构探索（design space exploration）是真实可落地的方向，比"AI 写代码"更硬核。如果你想给简历加一个差异化项目，可以做一个小的 agent 驱动的 Verilog/参数化硬件搜索 demo，成本低、故事性强。

---

## 📋 备选阅读

- [TSMC 据报暂停向中国设计公司发货，16nm/14nm 老节点被新规波及](https://www.tomshardware.com/tech-industry/policy/tsmc-reportedly-pauses-shipments-to-chinese-designers-after-u-s-export-rules-flag-decade-old-16nm-and-14nm-nodes-new-bis-controls-threaten-smartphone-tv-and-automotive-chips) —— 出口管制下沉到十年前的成熟制程，影响面比先进制程更广，但对你个人短期无行动点。
  _Jowi Morales_
- [Moore Threads 下一代 Lushan 游戏 GPU 或配 64GB 显存](https://www.tomshardware.com/pc-components/gpus/moore-threads-next-lushan-gaming-gpu-could-pack-a-record-64gb-of-vram-doubles-the-rtx-5090s-32gb-lofty-claims-of-15x-gaming-and-50x-ray-tracing-over-mtt-s80) —— 国产 GPU 显存翻倍到 64GB，宣称 15x 游戏性能，但都是发布会口径，等实测。
  _Shane Downing_
- [3500 美元四卡 V100 家庭实验室：128GB 显存跑 Qwen3-8-27B 达 285 tok/s](https://www.tomshardware.com/tech-industry/artificial-intelligence/homelabbers-usd3-500-build-straps-four-32gb-nvidia-v100s-to-a-lenovo-mini-pc-for-128gb-of-vram-coreboot-oculink-docks-and-a-solder-bridge-unlock-285-tokens-sec-in-qwen3-8-27b) —— OCuLink + Coreboot + 焊桥的硬核 homelab 方案，工程细节拉满，适合你这种电子背景看。
  _Shane Downing_
- [开发者把语言模型塞进一张软盘，跑在 486DX / Pentium 上](https://www.tomshardware.com/tech-industry/artificial-intelligence/dev-squeezes-an-ai-language-model-onto-a-floppy-for-486dx-and-pentium-pc-stalwarts-tiny-2-1-needs-540kb-of-memory-and-speaks-via-pc-speaker-is-a-question-answering-transformer-with-367k-parameters) —— 367K 参数、540KB 内存、用 PC 喇叭输出，纯极客趣味，但展示了极致量化思路。
  _Mark Tyson_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
