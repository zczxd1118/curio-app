# Curio · AI 算力 / 半导体 · 2026-11-02

> 今日 1 条头条 + 4 条备选

_今天最重要的信号有两个：一是 Anthropic IPO 叙事开始被公开质疑，S-1 的高增长与算力成本同时摆上台面，配合美股科技股因 AI 成本担忧大跌、Alphabet 单日市值蒸发 5000 亿美元，AI 资本周期的情绪拐点可能已经出现；二是 DeepSeek Harness 生态在中文社区快速成型，Agent 工具链的竞争从模型转向 harness 层。工程侧值得关注的是 Claude Code 官方扩展被植入后门，以及 Nvidia 半速限制被开源工具解锁。_

---

## 🌟 今日精选

### 4. 开源 UEFI 工具解锁 Nvidia 消费级 GPU 的半速 AI 限制，FP16 算力最高提升 65%

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Shane Downing_

开源项目 nv-uefi-unlocker 通过 UEFI 层修改，解除了 Nvidia 在 Windows 下对 RTX 20/30/40 系列消费卡的 tensor rate 限制，FP16 数学性能最高提升 65%。这直接影响本地推理和小规模微调的成本结构——消费卡被软件阉割的那部分算力，现在有办法拿回来了。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 工具名为 nv-uefi-unlocker，通过 USB 在 UEFI 层操作，覆盖 RTX 20/30/40 系列桌面与笔记本 | 65% 是特定 workload 下的峰值，实际推理吞吐提升幅度会小很多，取决于是否 compute-bound |
| 实测 FP16 数学性能提升最高达 65% | 解锁后的稳定性、功耗与保修影响未知，Nvidia 后续驱动可能封堵 |
| 限制是 Nvidia 在 Windows 驱动/固件层对消费卡的 tensor rate 做的半速封顶 | 是否违反许可协议存在法律灰区，个人实验与商用风险不同 |
| 项目已开源 | 对 Mac 统一内存路线和云 GPU 定价的实际冲击，短期可忽略 |

**📖 主编点评**

如果你手上有 RTX 30/40 系台式机，这是低成本提升本地推理吞吐的选项，但先在一台不重要的机器上验证稳定性。更重要的判断是：消费卡算力被软件分层这件事，说明本地推理的成本曲线还有下降空间，值得你在做 Agent 时保留本地 fallback 的设计。

---

## 📋 备选阅读

- [Sam Altman 赴韩会见三星高层，为数据中心抢 RAM](https://www.tomshardware.com/tech-industry/data-centers/sam-altman-travels-to-south-korea-to-meet-samsung-leadership-to-secure-more-ram-for-data-centers-amid-crushing-shortages-openai-ceo-meets-samsung-leadership-to-discuss-future-ai-data-centers) —— 内存短缺已经逼到 CEO 亲自上门，是 AI 成本压力的直接证据，但事件本身信息量有限。
  _Newton Gitonga_
- [Intel 把产能从消费级 CPU 转向服务器 CPU，应对「史无前例」的 AI 需求](https://www.tomshardware.com/pc-components/cpus/intel-shifts-production-capacity-from-consumer-to-server-cpus-in-face-of-unprecedented-ai-demand-company-navigating-one-of-the-most-significant-supply-shortages-in-history) —— PC 市场萎缩 + 数据中心需求暴涨的结构性转移，对理解硬件价格走势有用。
  _Anton Shilov_
- [Google：Agentic AI 将给数据中心 CPU 带来新需求](https://www.eetimes.com/google-agentic-ai-will-drive-new-demands-on-data-center-cpus/) —— Agent 负载是突发性的，CPU 大量空闲，这个观察对你设计 Agent 调度有启发。
  _Sally Ward-Foxton_
- [出租闲置 Mac 跑推理的公司警告 token 价格暴跌，Anthropic token 五个月跌 77%](https://www.tomshardware.com/tech-industry/artificial-intelligence/firm-that-lets-you-rent-out-your-idle-mac-for-ai-inference-workloads-warns-of-plummeting-token-costs-darkbloom-network-sees-earnings-drop-to-usd1-23-a-day-as-anthropic-tokens-fall-77-percent) —— token 价格 5 个月跌 77%，是判断 Agent 项目长期成本最重要的数字，但单一来源。
  _Jowi Morales_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
