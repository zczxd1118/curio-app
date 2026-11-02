# Curio · AI 算力 / 半导体 · 2026-11-02

> 今日 1 条头条 + 5 条备选

_今天最重要的信号有两个：一是 Anthropic IPO 的定价争议已经从投行圈烧到 HN 首页，'史上最荒谬 IPO'与'前所未有的收入增长'两种叙事同时成立，说明 AI 泡沫的分歧已进入公开定价阶段；二是 Gemini 4 Carbon 在 Artificial Analysis 指数上登顶，Google 一周内连发 Argon/Carbon 两个型号，模型迭代节奏重新加速。工程侧值得看的是 nv-uefi-unlocker 这类硬核解锁，以及 Claude Code 被植入后门的供应链风险。_

---

## 🌟 今日精选

### 3. 开源 UEFI 工具 nv-uefi-unlocker 解除 Nvidia 消费卡 FP16 限速，RTX 20/30/40 系性能最高提升 65%

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Shane Downing_

Nvidia 在消费级 GeForce 上长期把 tensor 的 FP16 速率压到数据中心卡的一半，这个限制写在 vBIOS/UEFI 层。一个开源工具直接在 UEFI 阶段把它解开，覆盖 RTX 20、30、40 系的台式与笔记本。对做本地推理的人来说，这是免费算力。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 工具名为 nv-uefi-unlocker，开源，通过 UEFI 层解除 Nvidia 的 tensor rate cap | 65% 是特定 benchmark 的峰值，实际推理吞吐提升幅度需自行实测 |
| 覆盖 RTX 20、30、40 系列桌面与笔记本型号 | 固件修改的稳定性与保修风险未评估 |
| 官方描述 FP16 数学性能最高提升 65% | 是否会被后续驱动或 vBIOS 更新封堵，未知 |
| 在 Windows 下生效，属于固件层修改而非驱动层 | 对 FP8/INT8 路径是否有同等影响，尚无数据 |

**📖 主编点评**

如果你手上有 30/40 系卡，这是本周性价比最高的一次动手实验：拿一个本地 7B/14B 模型，改前改后各跑一次 tokens/s，把数字记下来。这类'固件层解锁'的实测记录在简历上比任何教程都有说服力，但要先备份原 vBIOS。

---

## 📋 备选阅读

- [Open-source USB tool unlocks Nvidia's half-speed GPU AI limiter（HN 讨论）](https://github.com/Zagitta/gpu-unlock) —— 与头条同一事件的 GitHub 仓库版本，351 分讨论里有实测数据，动手前值得先翻评论区。
  _fragebogen_
- [Sam Altman meets with Samsung leadership to secure more RAM for data centers](https://www.tomshardware.com/tech-industry/data-centers/sam-altman-travels-to-south-korea-to-meet-samsung-leadership-to-secure-more-ram-for-data-centers-amid-crushing-shortages-openai-ceo-meets-samsung-leadership-to-discuss-future-ai-data-centers) —— Altman 赴韩会见约 50 名三星高管抢内存，内存短缺已从供应链问题变成 CEO 级外交问题。
  _Newton Gitonga_
- [Intel shifts production capacity from consumer to server CPUs in face of 'unprecedented' AI demand](https://www.tomshardware.com/pc-components/cpus/intel-shifts-production-capacity-from-consumer-to-server-cpus-in-face-of-unprecedented-ai-demand-company-navigating-one-of-the-most-significant-supply-shortages-in-history) —— Intel 把产能从消费级转向服务器 CPU，官方称正经历'史上最严重供应短缺之一'，PC 涨价的上游原因。
  _Anton Shilov_
- [New AI-driven Windows malware feeds stolen data to Claude to rank victims' assets by value](https://www.tomshardware.com/tech-industry/cyber-security/new-ai-driven-windows-malware-feeds-stolen-data-to-claude-to-rank-victims-assets-by-value-then-deletes-itself-payload-builds-custom-target-assessment-can-switch-models-if-one-refuses-or-skip-the-ai-step-entirely) —— Cisco Talos 披露 VOLTA 窃密木马把赃物喂给 Claude Opus 4.6 做资产估值排序，模型被武器化的具体案例。
  _Shane Downing_
- [Firm that lets you rent out your idle Mac for AI inference warns of plummeting token costs](https://www.tomshardware.com/tech-industry/artificial-intelligence/firm-that-lets-you-rent-out-your-idle-mac-for-ai-inference-workloads-warns-of-plummeting-token-costs-darkbloom-network-sees-earnings-drop-to-usd1-23-a-day-as-anthropic-tokens-fall-77-percent) —— Anthropic token 价格五个月内跌 77%，闲置 Mac 出租收益跌到每天 1.23 美元——推理成本崩塌的一线数据。
  _Jowi Morales_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
