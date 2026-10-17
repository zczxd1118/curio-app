# Curio · AI 算力 / 半导体 · 2026-10-17

> 今日 1 条头条 + 5 条备选

_今天最值得盯的两个信号：一是 AI 资本叙事开始松动——Anthropic 估值一周内被砍 5000 亿美元、Firmus 的 300 亿 IPO 48 小时崩盘、亚洲芯片股随 AI 融资担忧下挫，钱开始重新定价；二是工程侧的真实进展反而更硬——Linus 提交了首个 LLM 辅助内核补丁、Meta 放出能在 Mac 本地跑的开放权重模型、Vercel 的 Jev 成为其史上采用最快的模型。一句话：估值在退潮，工具在变强，你该把注意力放在后者。_

---

## 🌟 今日精选

### 2. Linus Torvalds 提交首个 LLM 辅助的 Linux 内核补丁，合成测试显示 23 倍性能提升

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

在明确表态支持 AI 工具之后，Linus 自己交出了第一个 LLM 辅助的内核补丁，配套的合成测试跑出 23 倍性能提升。这不是营销数字，是内核维护者用行动给 AI 辅助编程投的票。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Linus Torvalds 提交了首个 LLM 辅助编写的 Linux 内核补丁 | 23 倍提升来自特定合成测试场景，不代表通用负载 |
| 此前他已发布明确支持 AI 工具的内部指令 | LLM 在补丁中的实际贡献比例未披露，可能只是辅助生成测试代码 |
| 相关合成测试显示 23 倍性能提升 | 内核社区对 AI 生成代码的长期接受度仍有争议 |
| 补丁已进入内核邮件列表公开评审流程 | 是否会形成正式的 AI 辅助提交规范尚不确定 |

**📖 主编点评**

这条的意义不在数字，在信号：最保守的开源内核社区都开始接纳 LLM 辅助提交。你做 vibe coding 时可以把这条当论据——不是「AI 帮我写代码」很酷，而是「连内核维护者都在用，问题只剩怎么用得可审计」。建议你留意内核邮件列表里对这类补丁的评审意见，那是最真实的「AI 代码质量」反馈样本。

📺 [打开原文](https://www.tomshardware.com/software/linux/linus-torvalds-posts-his-first-llm-assisted-patch-to-the-linux-kernel-after-issuing-clear-pro-ai-directives-the-bossman-makes-use-of-ai-tooling-himself)

---

## 📋 备选阅读

- [ASML 单季营收创纪录 130 亿美元，客户已开始预订 2030 年产能](https://www.tomshardware.com/tech-industry/semiconductors/asml-reports-record-usd13-billion-quarter-vows-to-expand-capacity-as-demand-for-lithography-equipment-soars-customers-eager-to-secure-orders-in-2030-as-demand-is-expected-to-outstrip-2027-and-2028-supply) —— 光刻机需求旺到客户提前四年锁产能，AI 算力扩张的最上游信号，但离你的日常有点远，放备选。
  _Tom's Hardware_
- [中国初创公司展示 EUV 光源原型：15W 输出功率、90% 国产部件](https://www.tomshardware.com/tech-industry/semiconductors/china-startup-demoes-prototype-euv-light-source-15w-of-output-power-and-90-percent-domestic-components-still-years-away-from-viability) —— 国产 EUV 从 0 到 1 的进展，但 15W 功率离商用差得远，象征意义大于实际。
  _Tom's Hardware_
- [日本向 GlobalFoundries 提供 210 亿美元，扩建纽约两座晶圆厂](https://www.eetimes.com/japan-offers-globalfoundries-21b-for-u-s-fab-expansion/) —— 美国芯片产能再 +10%，地缘产能转移的又一笔，产业层面值得知道。
  _EE Times_
- [Nvidia 洽谈收购美国开放模型初创 Reflection AI](https://www.ft.com/content/052610c5-22b4-4dd4-932e-b7f9f0628b6a) —— Nvidia 从卖铲子转向买模型公司，开放权重阵营可能被收编，值得跟后续。
  _Hacker News / FT_
- [越狱 PS5 可本地跑 AI 模型，Qwen3.8-27B 达 20 tokens/s](https://www.tomshardware.com/video-games/playstation/jailbroken-ps5s-can-now-run-local-ai-models-at-over-100-tokens-per-second-fork-of-ps5lm-goes-native-and-accesses-gpu-and-more-ram) —— 本地推理的极客玩法，硬件复用思路有意思，但对你做 Agent 的实用价值有限。
  _Tom's Hardware_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
