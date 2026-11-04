# Curio · AI 算力 / 半导体 · 2026-11-04

> 今日 1 条头条 + 4 条备选

_今天最值得看的两条信号：一是 Gemini 4 Carbon 在 Artificial Analysis 智能指数上登顶、同时 Anthropic 的 IPO 文件把"算力经济学"和"可能接近递归自我改进"写进风险披露，前沿模型竞赛已经进入"能力+资本"双线叙事；二是芯片股集体大跌、Intel 单日崩盘叠加 Oracle 发 200 亿美元债融资 AI 基建，市场开始给 AI 资本开支重新定价。工程侧则有一条极硬的料：有人把 32 位 RISC-V CPU 编译进 Qwen 3.5 4B 的权重里并跑起 DOOM。_

---

## 🌟 今日精选

### 3. 工程师把 32 位 RISC-V CPU 编译进 Qwen 3.5 4B 的权重里，然后在上面跑 DOOM

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Mark Tyson_

一个叫 Qwenputer 的实验把 32 位 RISC-V CPU 直接编译并插入 Qwen 3.5 4B 的模型权重，让这个 CPU 能执行处理器算术运算、跑代码，当然还有 DOOM。这不是产品，但它把"权重即程序"这件事推到了一个很具体的边界：模型参数里可以装下一台可运行的计算机。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Qwenputer 基于开源 Qwen 3.5 4B 构建 | "编译进权重"的具体实现方式（是嵌入权重张量还是利用量化空间）尚未有论文级说明 |
| 32 位 RISC-V CPU 被编译后直接插入模型权重 | 这种做法的推理开销与实际可用性存疑，更像概念验证 |
| 该内置 CPU 可执行算术运算与代码，并能运行 DOOM | 是否会影响模型原有语言能力，没有公开评测 |
| 项目由一名 AI 工程师完成，属实验性质 | 对模型安全与可解释性研究可能是个新切口，但还没人系统分析 |

**📖 主编点评**

这条对你做 Agent 项目有直接启发：模型的"能力边界"正在从 prompt 层下沉到权重层。你不需要复现它，但值得读一遍实现思路——它提示了一种把确定性逻辑（比如你的 JSON schema 校验）硬编码进推理路径的可能性，比纯 prompt 约束更可靠。

---

## 📋 备选阅读

- [Marvell 以 1150 亿美元收购光子公司 Lumentum，押注 AI 互联](https://www.eetimes.com/marvell-snaps-photonics-chipmaker-lumentum-to-bolster-ai-connectivity/) —— 1150 亿美元是本周最大并购数字，co-packaged optics 是 AI 集群互联的关键路径，值得知道但离你的工程实践较远。
  _Majeed Ahmad_
- [Nvidia 要求数据中心运营商对华客户业务不超过 49%](https://www.tomshardware.com/tech-industry/data-centers/nvidia-tells-data-center-operators-to-limit-business-from-chinese-customers-with-new-global-restrictions-report-claims-allegedly-restricted-to-49-percent-of-the-total-ensuring-51-percent-are-non-chinese-outfits) —— 出口管制从卖芯片延伸到卖算力服务，49/51 的比例规则是个新机制，但目前仍是报道口径。
  _Oliver Haslam_
- [Intel 14A 进入 PDK 0.9，2027 年冲刺 1.0](https://www.tomshardware.com/tech-industry/semiconductors/intel-14a-moves-closer-to-production-as-pdk-0-9-becomes-available-process-design-kit-gives-developers-important-production-milestone-ahead-of-1-0-in-2027) —— Intel 代工的关键里程碑，但 PDK 版本号对非芯片从业者信息密度偏低。
  _Anton Shilov_
- [中国部署全球首个 800V 直流供电 AI 数据中心](https://www.tomshardware.com/tech-industry/data-centers/china-deploys-worlds-first-800-volt-dc-power-system-for-massive-ai-data-center-seeks-to-quench-power-needs-with-higher-conversion-and-efficiency-inside-a-smaller-footprint) —— 供电架构是 AI 数据中心被低估的瓶颈，800V DC 是个有工程含量的具体进展。
  _Mark Tyson_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
