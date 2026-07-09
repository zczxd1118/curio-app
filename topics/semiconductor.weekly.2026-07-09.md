# Curio · AI 算力 / 半导体 · 2026-07-09

> 今日 2 条头条 + 4 条备选

_今日核心信号：Grok 4.5 以 Opus 级性能+1/4 Token 成本杀回牌局，xAI 收购 Cursor 争夺编程代理市场；JEDEC 发布 SPHBM4 标准，有望用有机基板替代硅中介层，大幅降低 AI 内存成本；中国指控 Claude Code 含后门，地缘技术博弈加剧。_

---

## 🌟 今日精选

### 2. JEDEC 发布 SPHBM4 标准：512-bit 接口，用有机基板替代硅中介层，AI 内存成本有望大幅下降

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐⭐ · _Tom's Hardware_

JEDEC 正式发布 SPHBM4 标准，通过窄 512-bit 接口设计，允许使用有机基板替代昂贵的硅中介层和 CoWoS 封装。这意味着 HBM4 类带宽可以在不依赖先进封装的情况下实现，有望显著降低 AI 训练/推理的内存成本。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| SPHBM4 采用 512-bit 接口，带宽与 HBM4 相当 | 有机基板的良率和可靠性是否满足大规模量产要求 |
| 无需硅中介层和 CoWoS 封装，使用有机基板 | SPHBM4 的实际量产时间表（预计 2027-2028） |
| JEDEC 正式发布该标准 | HBM 厂商（三星、SK 海力士、美光）是否会跟进 |
| 目标市场为 AI 训练和推理场景 | 对现有 HBM 生态的冲击程度 |
|  | 成本降低幅度是否如预期显著 |

**📖 主编点评**

如果你在做 AI 推理优化或模型部署，SPHBM4 可能在未来 2 年改变内存成本结构。短期关注三星和 SK 海力士的反应，长期看这会降低 AI 基础设施的 TCO，对个人开发者意味着更便宜的云端推理资源。

📺 [打开原文](https://www.tomshardware.com/pc-components/dram/jedec-releases-new-sphbm4-standard-to-slash-ai-memory-costs-narrow-512-bit-interface-enables-dropping-expensive-interposers-for-organic-substrates)

---

### 3. 中国指控 Claude Code 含后门：2026 年 4-6 月版本存在隐蔽代码，向远程服务器发送敏感信息

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _Tom's Hardware_

中国官方指控 Claude Code 2026 年 4 月至 6 月发布的版本中存在隐蔽代码，会在未经用户同意的情况下向远程服务器发送敏感信息。此前已有国外开发者逆向发现 Anthropic 在客户端中内置了用户标记系统。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 中国官方发布安全警告，指控 Claude Code 存在后门 | Anthropic 是否承认该机制存在 |
| 涉及 2026 年 4-6 月发布的版本 | 该机制是安全功能还是后门（如遥测/反滥用） |
| 隐蔽代码可向远程服务器发送敏感信息 | 对 Claude Code 在中国及全球市场的影响 |
| 此前已有国外开发者发现类似标记系统 | 是否会导致更多国家出台类似限制 |
|  | 开源替代方案（如 OpenCode）是否会受益 |

**📖 主编点评**

如果你在用 Claude Code，建议检查版本号并关注 Anthropic 的官方回应。对于你的 content-curator 项目，可以考虑将 OpenCode 等开源工具作为备选，避免单一依赖风险。

📺 [打开原文](https://www.tomshardware.com/tech-industry/artificial-intelligence/china-alleges-that-claude-code-contains-backdoors-calls-mechanism-a-serious-threat-govt-claims-claude-sends-sensitive-information-to-remote-servers-without-consent)

---

## 📋 备选阅读

- [SambaNova 融资 10 亿美元，签下摩根大通客户](https://www.eetimes.com/sambanova-raises-1-billion-signs-jpmorganchase-as-a-customer/) —— 企业级 AI 芯片市场开始放量，SambaNova 获大行背书，但融资额和客户级别仍需观察后续订单。
  _EE Times_
- [Nvidia 称 Vera CPU 单线程性能领先 x86 1.8 倍，专为 Agentic AI 设计](https://www.tomshardware.com/pc-components/cpus/nvidia-touts-vera-cpus-single-threaded-performance-as-its-agentic-ai-advantage-frames-chip-as-a-max-single-threaded-cpu-at-scale-not-a-parallel-monster) —— Nvidia 首次公开 Vera CPU 单线程性能数据，Agent 推理场景可能成为其新护城河。
  _Tom's Hardware_
- [JEDEC 发布 SPHBM4 标准，AI 内存成本有望大幅下降](https://www.tomshardware.com/pc-components/dram/jedec-releases-new-sphbm4-standard-to-slash-ai-memory-costs-narrow-512-bit-interface-enables-dropping-expensive-interposers-for-organic-substrates) —— 已选入头条，此处略。
  _Tom's Hardware_
- [中国指控 Claude Code 含后门](https://www.tomshardware.com/tech-industry/artificial-intelligence/china-alleges-that-claude-code-contains-backdoors-calls-mechanism-a-serious-threat-govt-claims-claude-sends-sensitive-information-to-remote-servers-without-consent) —— 已选入头条，此处略。
  _Tom's Hardware_

---

## 💬 觉得 AI 算力 / 半导体 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
