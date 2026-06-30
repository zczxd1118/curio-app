# Curio · AI · 2026-06-30

> 今日 1 条头条 + 4 条备选

_今日核心信号：韩国800万亿韩元存储扩产计划落地，全球存储资本开支进入超级周期，但短期供需格局不变；Anthropic与加州政府达成Claude半价协议，AI进入政府场景加速；Cursor推出移动端App，AI编程工具从IDE向全场景延伸。_

---

## 🌟 今日精选

### 4. Mozilla 0din团队演示：AI编程Agent可被恶意GitHub仓库诱导安装恶意软件

**[AI]** · ⭐⭐⭐⭐ · _Tom's Hardware_

Mozilla的0din安全团队发布PoC，展示如何通过一个看似干净的GitHub仓库诱导Claude Code等AI编程Agent安装恶意软件。攻击者只需在仓库中嵌入隐蔽的恶意代码，当Agent执行初始化项目等操作时，就会被触发下载并执行恶意负载。这暴露了AI编程Agent在供应链安全方面的重大隐患。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| Mozilla 0din团队成功诱导Claude Code安装恶意软件 | 该攻击需要用户主动让Agent操作恶意仓库，实际利用门槛较高 |
| 攻击向量：在GitHub仓库中嵌入隐蔽恶意代码 | AI编程工具厂商可能需引入仓库安全扫描机制 |
| 触发条件：Agent执行项目初始化、依赖安装等常见操作 | 用户应避免让Agent操作未经验证的第三方仓库 |
| 该漏洞影响所有基于LLM的编程Agent，包括Cursor、Codex等 | 该问题可能推动AI编程工具的安全审计功能标准化 |

**📖 主编点评**

这对你意味着：如果你在用Claude Code或Cursor开发项目，务必注意仓库来源。建议在沙箱环境中运行Agent，或使用Docker等隔离机制。同时，关注各工具厂商的安全更新，及时升级到最新版本。

📺 [打开原文](https://www.tomshardware.com/tech-industry/cyber-security/ai-coding-agents-can-be-tricked-into-installing-malware-via-clean-github-repositories-mozillas-0din-team-shows-how-claude-code-can-be-exploited-by-its-own-helpfulness)

---

## 📋 备选阅读

- [Vibe coding平台Base44发布自研模型，AI初创寻求差异化](https://techcrunch.com/2026/06/29/vibe-coding-platform-base44-launches-own-model-as-ai-startups-seek-defensibility/) —— Wix旗下Base44推出自研模型，试图在AI编程工具同质化竞争中建立护城河。
  _TechCrunch_
- [Chamath Palihapitiya的AI编程初创获1.35亿美元A轮融资](https://techcrunch.com/2026/06/29/chamath-palihapitiya-raises-135m-series-a-for-his-ai-coding-startup-takes-ceo-role/) —— 知名投资人亲自下场，AI编程赛道融资热度不减，但竞争已白热化。
  _TechCrunch_
- [Arena AI排行榜业务估值达1亿美元](https://techcrunch.com/2026/06/29/arena-the-ai-leaderboard-everyone-uses-is-now-a-100m-business/) —— LMSYS Arena从免费排行榜转型商业化，证明AI评测本身就是一个大生意。
  _TechCrunch_
- [Gemini个性化AI图像生成向美国免费用户开放](https://techcrunch.com/2026/06/29/geminis-personalized-ai-image-generation-is-now-free-for-u-s-users/) —— Google将Gemini图像生成能力下放免费层，AI多模态竞争进入免费获客阶段。
  _TechCrunch_

---

## 💬 觉得 AI 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
