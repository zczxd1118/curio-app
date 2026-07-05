# Curio · 大厂 AI 动态 · 2026-07-05

> 今日 1 条头条 + 6 条备选

_今日核心信号：阿里因后门风险全面禁用Claude Code，国内AI工具链面临信任危机；OpenAI Scaling Law被曝基础bug，全球算力配置可能长期错配。两条新闻叠加，提示AI工程实践需要更审慎的评估框架。_

---

## 🌟 今日精选

### 1. 阿里内部全面禁用Claude Code，因发现隐蔽后门代码

**[大厂 AI 动态]** · ⭐⭐⭐⭐⭐ · _TechCrunch_

据TechCrunch报道，阿里已将Claude Code列为高风险软件并禁止员工使用。此前B站up主程序员鱼皮逆向Claude Code源码，发现Anthropic在客户端中植入了一套隐蔽的用户标记系统，可能用于检测和封禁中国区用户。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| 阿里内部邮件将Claude Code列为高风险软件，要求员工立即停止使用 | Anthropic是否故意针对中国用户设计此机制尚未确认 |
| 国外开发者逆向Claude Code源码发现隐蔽的用户标记系统 | 其他AI编程工具（如Cursor、Codex）是否存在类似后门未知 |
| 该标记系统可识别用户地理位置并触发封号 | 国内替代方案（如DeepSeek、通义灵码）能否承接需求待观察 |
| 此前大量中国用户遭遇Claude Code封号，原因不明 | 此举是否违反中国网络安全法中的用户知情权条款 |

**📖 主编点评**

你在做content-curator项目时如果依赖Claude Code，需要立即评估风险。建议切换到开源方案或本地部署模型，至少不要在涉及个人数据和项目代码的环节使用。这也提醒你：AI工具的供应链安全正在成为新的工程实践课题。

📺 [打开原文](https://techcrunch.com/2026/07/04/alibaba-reportedly-bans-employees-from-using-claude-code/)

---

## 📋 备选阅读

- [Midjourney要求好莱坞披露AI使用细节](https://techcrunch.com/2026/07/04/midjourney-wants-hollywood-studios-to-reveal-the-details-of-their-ai-usage/) —— 法律纠纷中Midjourney要求三家好莱坞工作室披露AI使用情况，涉及版权和透明度。
  _TechCrunch_
- [硅基流动向港交所递交上市申请](https://36kr.com/p/3879814941437956?f=rss) —— 袁进辉新公司成立不到三年冲刺港股IPO，AI基础设施赛道资本化加速。
  _36氪_
- [小米前高管唐沐创业咖啡机器人，完成数亿融资](https://36kr.com/p/3882361033322755?f=rss) —— 影智XBOT获3-5亿元B轮融资，餐饮垂直机器人赛道最大融资之一。
  _36氪_
- [Meta打算出售富余算力引发科技股回落](https://36kr.com/p/3880629882679301?f=rss) —— Meta拟向外部客户出售AI算力，市场担忧资本开支回报率，短期情绪扰动。
  _36氪_
- [苹果AI功能未能引爆换机潮，用户升级意愿持续下滑](https://wallstreetcn.com/articles/3776203) —— 瑞银调查显示因Apple Intelligence换机意愿降至24%，折叠屏iPhone被视为潜在亮点。
  _华尔街见闻_
- [当AI账单失控，模型路由器成为企业降本新宠](https://wallstreetcn.com/articles/3776199) —— 按任务复杂度调度大小模型，最高节省97%算力开支，Agent工程实践值得关注。
  _华尔街见闻_

---

## 💬 觉得 大厂 AI 动态 这期怎么样？

[提一条反馈 Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
