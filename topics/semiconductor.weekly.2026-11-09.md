# Curio · AI 算力 / 半导体 · 2026-11-09

> 今日 1 条头条 + 5 条备选

_今天最重要的信号有两个：一是 Nvidia 董事会正式调查黄仁勋与疑似中国间谍的关系，Yale 的 Sonnenfeld 给出「50-50 留任概率」——这不只是花边，是 AI 算力供应链最大单一节点的治理风险；二是 AI 交易在中期选举后遭遇 2.5 万亿美元级别的抛售，Nasdaq 进入回调区间，算力叙事第一次被政治与融资成本同时定价。工程侧则有一条被低估的：284B 参数 DeepSeek 在 64GB 内存、无 GPU 上跑起来了。_

---

## 🌟 今日精选

### 3. llama-modchip：284B 参数 DeepSeek 在 64GB 内存、无 GPU 的机器上跑起来，HN 429 分

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _joshcsimmons_

一个 GitHub 项目把 284B 参数的 DeepSeek 模型塞进了 64GB 内存的纯 CPU 环境，不依赖 GPU。同期还有 homelab 玩家用二代 Optane 持久内存跑 2.8 万亿参数的 Kimi K3，1-bit 量化下 0.85 tokens/s。这两条放在一起说明：内存带宽与量化技术正在把「大模型必须上 GPU」这条假设撕开一个口子。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| llama-modchip 项目在 HN 获 429 分，实现 284B DeepSeek 模型在 64GB RAM 无 GPU 环境运行 | 0.85 tokens/s 的实际可用性极低，这类方案目前是技术验证而非生产可用 |
| Reddit homelab 用户用 Optane PMem 200 跑 Kimi K3（2.8T 参数），1-bit 量化下 0.85 tokens/s | llama-modchip 的具体量化方案与内存布局未在摘要中说明，需读源码判断可复现性 |
| 该用户警告 Optane 发热会烧毁邻近 DRAM，需用鼓风机散热 | Optane 已停产，这条路线依赖二手硬件，不具备规模化意义 |
| 同期 CPU-Z 数据显示 64GB 内存 PC 占比同比下滑 18%，因 AI DRAM 涨价 | 内存涨价是否会反过来压制本地推理社区的增长，尚待观察 |
| TSMC 否认应 Nvidia 要求探索 3D DRAM，称该技术距量产仍有数年 | 「无 GPU 跑大模型」与「边缘设备跑小模型」是两条不同路线，别混为一谈 |

**📖 主编点评**

这条对你的价值不在「能不能用」，而在「为什么能」——去读 llama-modchip 的 README，看它怎么做权重分片和量化调度，这套思路直接能迁移到你的 Agent 项目的本地推理降本上。如果你哪天要给 content-curator 加一个本地小模型做初筛，这就是现成的工程参考。

📺 [打开原文](https://github.com/synchopate/llama-modchip)

---

## 📋 备选阅读

- [DeepX 流片二代芯片，LPDDR5x-PIM 架构宣称 6.7 倍性能提升](https://www.eetimes.com/deepx-tapes-out-second-gen-chip-projects-6-7x-performance-gain-with-lpddr5x-pim/) —— 5W 以内跑大模型，存内计算路线在边缘侧的又一次下注，数字漂亮但需等实测。
  _Sally Ward-Foxton_
- [Diamond Foundry 造出全球首片 200mm 单晶金刚石晶圆](https://www.tomshardware.com/pc-components/cooling/diamond-foundry-creates-worlds-first-200mm-single-crystal-diamond-wafer-massive-gem-aims-to-solve-ai-chip-cooling-crisis-envisioned-as-a-cooling-material-for-semiconductors) —— 冲着 AI 芯片散热危机去的材料突破，200mm 尺寸是关键，但离量产还远。
  _Jowi Morales_
- [Nvidia RTX Spark 加密固件把 Linux 上推理速度压到 35%](https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop) —— HN 617 分，本地推理玩家必看：买卡之前先确认固件策略，这是实打实的踩坑预警。
  _novaRom_
- [开源 GPU 任务管理器 gputaskman 精确显示谁在吃你的 VRAM](https://www.tomshardware.com/pc-components/gpus/open-source-gpu-task-manager-reveals-exactly-whats-eating-your-vram-microsoft-vps-new-gpu-taskman-tool-reveals-every-process-using-your-gpu-how-much-memory-each-uses-and-breaks-down-ai-and-llm-workloads) —— 微软 VP Scott Hanselman 发布的小工具，能拆分 AI/LLM 负载，本地调试刚需。
  _Mark Tyson_
- [Synaptics 向开源 DisplayLink 驱动作者发律师函，还「激将」其公开威胁](https://www.tomshardware.com/peripherals/docking-stations-hubs/synaptics-sends-cease-and-desist-order-to-creator-of-open-source-displaylink-driver-dares-him-to-publicize-its-threats-dev-reverse-engineers-displaylink-using-claude-ai-and-rust-synaptics-threatens-to-bill-creator-for-legal-documentation) —— 开发者用 Claude AI + Rust 逆向 DisplayLink 被发函，AI 辅助逆向的法律边界案例。
  _Jowi Morales_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
