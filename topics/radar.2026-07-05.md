# Curio 趋势雷达 · 2026-07-05

> 你的私人主编 · 今日跨域精选 4 条头条 + 13 条备选

_今日核心信号：阿里因后门风险全面禁用Claude Code，国内AI工具链面临信任危机；OpenAI Scaling Law被曝基础bug，全球算力配置可能长期错配。两条新闻叠加，提示AI工程实践需要更审慎的评估框架。_

---

## 🌟 大厂 AI 动态

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

## 🌟 AI

### 2. OpenAI Scaling Law被曝基础bug，全球或浪费万亿算力

**[AI]** · ⭐⭐⭐⭐⭐ · _华尔街见闻_

DeepMind研究员指出，OpenAI最初的Scaling Law论文存在方法论错误，导致行业长期「重参数、轻数据」，大量模型训练不足、算力配置失衡。后续研究证实模型与数据应同步放大，此前方向可能浪费了海量GPU资源。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DeepMind研究员指出OpenAI Scaling Law论文存在方法论缺陷 | 具体浪费的算力规模尚无精确估算，但可能达数千亿美元 |
| 原论文错误引导行业优先增加参数而非数据量 | OpenAI是否已在新模型中修正该错误未公开 |
| 后续实验证明模型与数据需同步缩放才能达到最优 | 对已训练完成的大模型（如GPT-4）影响程度未知 |
| 多家实验室已开始调整训练策略，重新评估数据配比 | 该发现是否会导致行业训练范式根本性转变待观察 |

**📖 主编点评**

这对你理解AI行业走向很重要：如果你在做Agent项目，不要盲目追求大参数模型，数据质量和配比可能更关键。建议关注DeepMind后续的修正论文，这可能会改变未来6-12个月的模型选型策略。

📺 [打开原文](https://wallstreetcn.com/articles/3776218)

---

## 🌟 AI 算力 / 半导体

### 3. DRAM价格暴涨成AI算力瓶颈，技术路线被迫转向分层内存架构

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _华尔街见闻_

DRAM价格持续攀升，根源在于HBM挤占产能。AMD、Apple、Marvell等厂商已开始转向AI调度冷数据至闪存、模型常驻NAND等分层策略，纯DRAM堆砌时代正在结束。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| DRAM价格因HBM产能挤占持续上涨，PC内存一天三个价 | 分层内存架构能否完全替代DRAM堆砌尚不确定 |
| AMD推出AI调度方案将冷数据迁移至闪存 | 闪迪HBF新架构的成熟度与量产时间未知 |
| Apple将部分模型参数常驻NAND以降低DRAM需求 | HBM4的出货节奏可能缓解部分压力 |
| Marvell发布硬件压缩方案扩容内存带宽 | 消费者端涨价趋势至少持续到2027年 |

**📖 主编点评**

如果你在部署AI应用或做推理优化，需要重新评估内存预算。可以考虑使用量化、模型剪枝等技术减少DRAM占用，或者关注支持闪存直存的推理框架。

📺 [打开原文](https://wallstreetcn.com/articles/3776211)

---

### 4. SK海力士宣布7130亿美元国内投资计划，并筹备纳斯达克上市

**[AI 算力 / 半导体]** · ⭐⭐⭐⭐ · _EE Times_

SK海力士计划投资7130亿美元（约合713B韩元）扩大韩国本土半导体制造产能，同时正在筹备纳斯达克上市。这是韩国存储芯片史上最大规模投资，旨在巩固HBM市场领导地位。

| ✅ 已确认 | ⚖️ 尚属判断 |
|---|---|
| SK海力士宣布7130亿美元国内投资计划 | 投资落地时间表尚未公布，可能分5-10年完成 |
| 投资将用于扩建HBM和先进DRAM产能 | 纳斯达克上市估值和具体时间未定 |
| 公司正在筹备纳斯达克上市 | 对全球DRAM供需格局的影响需观察 |
| 韩国政府将提供税收优惠和补贴支持 | 三星和美光可能跟进类似投资计划 |

**📖 主编点评**

存储芯片产能扩张对AI算力成本有长期利好，但短期涨价压力仍在。关注SK海力士美股上市后的融资用途，可能影响HBM4的研发进度。

📺 [打开原文](https://www.eetimes.com/sk-hynix-plans-713b-domestic-investment/)

---

## 📋 备选池

### AI

- [Claude Code封号原因曝光：Anthropic植入隐蔽用户标记系统](http://www.bilibili.com/video/av116844031774993) —— B站up主逆向Claude Code源码发现隐蔽标记系统，与阿里禁用事件互为补充，但深度不及TechCrunch报道。
  _程序员鱼皮_
- [Claude官方发布科研神器Claude Science](http://www.bilibili.com/video/av116840541984361) —— 内置科学渲染器、持久化Python/R内核，可连接本地GPU/HPC集群，对科研场景有价值但非用户当前关注点。
  _旭光升_
- [Vibe Coding零基础入门教程（黑马程序员）](http://www.bilibili.com/video/av116838327388595) —— 涵盖Claude Code、Cursor、Codex等工具，适合新手但内容偏基础，用户可能已掌握。
  _黑马程序员_
- [Cursor已死？退订Cursor转投Claude Code和Codex](http://www.bilibili.com/video/av116819553683121) —— 个人体验分享，观点有参考价值但缺乏工程细节，作为头条深度不够。
  _小狗瑞恩Ryan_

### AI 算力 / 半导体

- [Intel 18A wafer-to-wafer yield issues fixed](https://www.tomshardware.com/tech-industry/semiconductors/intel-18a-wafer-to-wafer-yield-issues-fixed-report-claims-says-production-up-to-15-000-wafers-per-month-at-both-sites) —— Intel 18A良率问题修复，月产能达1.5万片，对先进制程竞争有影响但用户关注度较低。
  _Tom's Hardware_
- [美光日本90亿美元扩建项目开工，预计2028年出货HBM](https://wallstreetcn.com/articles/3776210) —— 美光93亿美元扩建广岛工厂，日本政府补贴5000亿日元，HBM产能竞赛加剧。
  _华尔街见闻_
- [SK hynix, Samsung, Micron面临第三起DRAM价格操纵诉讼](https://www.tomshardware.com/pc-components/dram/samsung-sk-hynix-and-micron-face-a-third-dram-price-fixing-lawsuit) —— 17名原告在加州北区法院起诉三大存储厂商，HBM分配可能成为新焦点。
  _Tom's Hardware_

### 大厂 AI 动态

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

## 💬 反馈

觉得选稿好/不好？想多看/少看哪类？[提一条 GitHub Issue](https://github.com/zczxd1118/curio-app/issues/new?labels=curio-feedback) 让 Agent 下次调整。
