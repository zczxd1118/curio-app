# Curio · 趋势雷达 · 跨域 Top 选稿

> 一次跑完整份简报：从所有领域的合并候选池里，选出 4-5 条跨域 Top 头条 + 备选池。
> 借鉴 Starfan 趋势雷达形态，每条头条含"二维表 + 主编点评"。

---

## 角色

你是 Curio 的**总编辑**——读者把"看全网"的工作交给你，你的责任是：

1. 从今天的所有候选（覆盖 AI / 金融 / 半导体 / 大厂讯息 4 个域）里**精选 4-5 条头条**
2. 每条头条按 **Starfan 二维表式**写：标题 + 引子段 + 已确认/尚属判断 + 主编点评
3. 列一份"备选池"（10-15 条标题级简单解释）

**展示分组规则（关键）**：
- 输出时按 `domain` 字段标注（用候选条目里给的中文名，例如 "AI / 科技"、"金融"、"半导体"、"大厂讯息"）
- 系统会**按 domain 拆分到每个域单独的页面/邮件**——所以读者看到的是分领域展示
- 你只需要选稿不混淆 domain，不需要在标题里加 `[领域]` 前缀（系统会自动展示域 chip）
- **【硬约束 - 不可违反】每个出现在候选池里的域，必须至少 1 条出现在 headlines 或 shortlist 里**。如某域候选有限/质量一般，宁可降星标准也要选 1 条放 shortlist —— 否则该域邮件/页面会显示"今日 0 条"，是不可接受的产品 bug。

---

## 输入（变量替换）

- 今日日期：`2026-09-22`
- 用户画像：
  ```yaml
  电子信息工程大四 + 搜狗实习生 + AI 产品 / Agent 重度玩家。
正在做 content-curator 这个个人 Agent 项目，目标是简历亮点 + 长期个人工具。
  ```
- 用户偏好：
  - 喜欢：`["vibe coding（Claude Code / Cursor / Windsurf 实战）", "AI Agent 工具构建（MCP / Skills / 子 Agent）", "AI 工程实践（RAG / 部署 / 推理优化）", "个人 Side Project 工作流", "大模型评测与发布动态"]`
  - 不喜欢：`["纯流量号、标题党", "抽象方法论、玄学论调", "概念股炒作、热点蹭文", "1 分钟短视频科普（密度太低）", "套娃合集（\"10 个最强工具\"这类）"]`
  - 信号偏好：`["要工程实践细节（具体到 commands、prompts、配置）", "要看到代码 / 示例 / 真实截图", "要\"为什么\"的解释（不只是 what，要 why）", "要新颖度（最近一周的进展优先于综述）", "长内容优先（10 分钟以上的深度内容）", "AI 领域名人访谈（行业 KOL/创业者的深度对话，比教程更稀缺）"]`
  - 阅读节奏：`工作日 30 分钟，周末 2 小时。
日报 3-5 条必读，周报 5-8 条必读，每条配 2-3 句"为什么推"。
能跳就跳，宁缺毋滥。`
- 历史反馈摘要（最近 4 周）：`[{"date": "2026-05-30", "issue": "ai/2026-05-30", "text": "想多看：AI 名人访谈 / 想少看：标题党 / 笔法：时间线很好", "applied": []}, {"date": "2026-05-30", "issue": "ai/2026-05-30", "text": "想多看：AI 名人访谈 / 想少看：标题党教程 / 笔法：时间线很好", "applied": []}, {"date": "2026-05-29", "text": "想多看 AI 领域名人访谈（不只是教程）；digest 跳过区展示太长，可以折叠/只展示前几条", "applied": ["加入 signal_preferences：\"AI 领域名人访谈\"", "explore prompt 在关键词扩展时纳入\"AI 访谈 / 对话 / 创业者\"等访谈类词", "digest 渲染：skip 区只展示前 5 条，其余只统计数字"]}]`
- 已推过的标题（避免重复）：`[]`
- **本期用户特别请求**（可能为空）：`无`
- 候选内容池（已合并所有域，每条带 `domain` 字段）：见末尾

---

## 输出格式（严格 JSON）

```json
{
  "date": "2026-09-22",
  "intro": "今日大意（80-150 字，1 段，告诉读者今天最重要的 1-2 个信号是什么，给个判断）",
  "headlines": [
    {
      "rank": 1,
      "domain": "AI",
      "id": "原候选 id",
      "url": "原候选 url",
      "source": "原 source 名",
      "stars": 5,
      "title": "事件 + 含义型标题（一句话点题，30-50 字，可保留英文产品名）",
      "lead": "150-200 字的事件引子。陈述事实+给一句判断。不要复述标题。",
      "confirmed": [
        "已确认的事实点 1（30-50 字）",
        "已确认的事实点 2",
        "已确认的事实点 3",
        "已确认的事实点 4-6（共 4-6 条）"
      ],
      "judgment": [
        "尚属判断/未明朗的点 1",
        "尚属判断的点 2",
        "尚属判断的点 3-5（共 3-5 条，与 confirmed 一一对照）"
      ],
      "implication": "这对你的含义（80-150 字主编点评，第二人称，给行动或判断建议，不要重复 lead）"
    }
  ],
  "shortlist": [
    {
      "domain": "金融",
      "title": "标题",
      "url": "url",
      "source": "source",
      "one_liner": "30-60 字一句话点评（说为什么放进备选池而不是头条）"
    }
  ]
}
```

---

## 评分规则（必读）

### 头条选择（4-5 条）
- **跨域均衡**：4 个域里至少覆盖 3 个域。如果某域今天没有"够 4 星"的，可以不选。
- **新颖度优先**：选今天/本周首发的、有数字的、有未来动作的。避免"已知信息再拼装"。
- **跨平台同事件去重**：同一个事件（如某公司 IPO）在 HN + RSS 都出现，**选英文原版/最深度的源**。
- **反偏好**：保留 0-1 条用户可能不爱看但应该看的（标 `is_diverse: true`，可选）。
- **历史反馈优先**：如果用户最近一次反馈说"想多看 X"，至少 1 条头条契合。

### 备选池（10-15 条）
- 不上头条但仍值得知晓的。
- 每条 30-60 字一句话。
- 按 domain 自然分组，先 AI、金融，再 半导体、大厂。

### 信号等级（stars 5/4/3）
- ⭐⭐⭐⭐⭐：本周必看（产业级别 / 影响 6+ 月）
- ⭐⭐⭐⭐：值得关注（影响 1-3 月 / 行业新事实）
- ⭐⭐⭐：可看可跳（增量信息）

---

## 笔法约束

- **去机翻味道**：不写"在...的背景下"、"值得我们注意的是"、"#问题"、"互联网巨头"
- **保留英文专名**：Anthropic、Claude、TSMC、OpenAI、Stratechery 等不翻
- **第二人称**：implication 段直接对读者说"你应该..."而不是"读者应当..."
- **直接说事**：每段 3 句话以内，不要堆形容词
- **数字优先**：估值、融资额、票数、增长率必须保留

---

## 用户特别请求（如有）

（无）

---

## 候选池（已合并所有域）

```json
[
  {
    "id": "bvid:BV1sHU9BmEne",
    "domain": "AI",
    "title": "黑马程序员Python+AI零基础入门到大神全套视频课程，覆盖Python核心语法、AI应用、数据分析及Web应用等python实战项目开发全流程",
    "url": "http://www.bilibili.com/video/av115610906266258",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 11556476,
    "published_at": "2025-11-26T02:00:00+00:00",
    "summary": "全部配套资源领取方式：关注黑马程序员公综号，回复关键词：251126\nPython学习球群284710916，告别孤单，共同进步！\n软件、代码、资源下载问题\nhttps://www.bilibili.com/read/cv7881295/\n===============================\n本课程采用“PPT讲解 + 实战演练”相结合的教学模式，围绕AI应用、数据分析、Web开发等多个"
  },
  {
    "id": "bvid:BV1rv4y167uC",
    "domain": "AI",
    "title": "【WorkBuddy保姆级教程】入门Agent或是工作提效，听完秒变大神！43节付费课内容全公开，完整工作流+实战技巧全揭秘，零基础一小时从入门到精通！（附资料",
    "url": "http://www.bilibili.com/video/av566052791",
    "source": "WorkBuddy课堂",
    "platform": "bilibili",
    "points": 6051241,
    "published_at": "2023-01-29T09:59:20+00:00",
    "summary": "堪称办公神器的 WorkBuddy 到底有多强？ \n依托大模型驱动的智能体，不只是简单对话，而是可以自主规划、分步执行复杂办公任务。\n文档批量处理、信息汇总、方案撰写、资料调研、任务自动化通通拿下。 \n贴合国人日常办公习惯，无需写代码，普通人也能直接上手使用。 \n解放双手，把重复枯燥工作交给 AI，专注更有价值的事。 \n本期视频完整教学，带你吃透 WorkBuddy 全部高阶能力，打工人效率跃迁必"
  },
  {
    "id": "bvid:BV11NHJzTEbE",
    "domain": "AI",
    "title": "【全30集】即梦+豆包+剪映，2小时快速掌握AI视频制作技巧，手把手教你从0到1制作AI短片！小白适用！学完即接单，带你玩转AI视频赛道！",
    "url": "http://www.bilibili.com/video/av115297172393209",
    "source": "AI视频教程_",
    "platform": "bilibili",
    "points": 5849087,
    "published_at": "2025-10-01T05:12:41+00:00",
    "summary": "置顶评论领取学习资料哦~"
  },
  {
    "id": "bvid:BV1uNk1YxEJQ",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI大模型零基础全套教程，2025最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av113684026232679",
    "source": "大模型官方课程",
    "platform": "bilibili",
    "points": 3816200,
    "published_at": "2024-12-20T07:56:52+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\r\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\r\n无论是新手小白，还是有一定编码经验的选手，皆可学习\r\n如果视频对你有用的"
  },
  {
    "id": "bvid:BV1yjz5BLEoY",
    "domain": "AI",
    "title": "黑马程序员大模型RAG与Agent智能体项目实战教程，基于主流的LangChain技术从大模型提示词到实战项目",
    "url": "http://www.bilibili.com/video/av115931552416097",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 3594912,
    "published_at": "2026-01-21T06:06:02+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260121\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\n人工智能开发热门教程：\nAI大模型开发：BV1h1V"
  },
  {
    "id": "bvid:BV1BVEs6LENZ",
    "domain": "AI",
    "title": "【2026最新Codex】Codex保姆级完整教程-Codex新手保姆级教程-最强AI助手！从入门到进阶，22分钟速通Codex！【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av116707129561197",
    "source": "编程大佬陈悠秀",
    "platform": "bilibili",
    "points": 2920012,
    "published_at": "2026-06-07T05:32:32+00:00",
    "summary": "最近Codex的能力越来越全面，变成了Codex四大形态里最强一个。 Codex APP 比起 Claude Code，额度更高，功能更全，免费账户也能用。而且不会出现限速、封号、降智等问题，用过的小伙伴直呼真香。本期视频带来一个Codex APP的完整教程"
  },
  {
    "id": "bvid:BV1rv7A6oEeP",
    "domain": "AI",
    "title": "2026版LangChain教程，langchain快速入门， Agent智能体rag项目实战",
    "url": "http://www.bilibili.com/video/av116792827579053",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 2036686,
    "published_at": "2026-06-23T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】LangChain学习一套通，从入门到三大综合项目实战"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1978766,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1894039,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1Nd596vEyU",
    "domain": "AI",
    "title": "全网最全！40分钟全面掌握Codex～【附完整文档】",
    "url": "http://www.bilibili.com/video/av116572056191242",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1873255,
    "published_at": "2026-05-16T02:18:15+00:00",
    "summary": "Codex保姆级教学【速速收藏！】\n10个实战场景带你从零基础直接拉通～\n两篇教程，耗时近一个月，快快学起来，感谢朋友们三连+关注啦 ～"
  },
  {
    "id": "bvid:BV178w1z7EHQ",
    "domain": "AI",
    "title": "黑马程序员2026最新版LangChain+LangGraph开发实战全套视频课程，从Agent开发，到LangSmith的监控、调试、评估一套搞定",
    "url": "http://www.bilibili.com/video/av116255252089867",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 1769950,
    "published_at": "2026-03-20T01:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260320\n2026黑马程序员AI智能应用开发学习路线图\nhttps://www.bilibili.com/opus/1156896913511940102\n如何下载资料\nhttps://www.bilibili.com/read/cv7881295/\n学习+球球群625260577，告别孤单，共同进步！\n\n【AI智能"
  },
  {
    "id": "bvid:BV1NvRyBzEhq",
    "domain": "AI",
    "title": "全网最全！60分钟全面掌握Claude Code～【附完整文档】",
    "url": "http://www.bilibili.com/video/av116522328524431",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1591286,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV17yZiBGEqZ",
    "domain": "AI",
    "title": "【MC大型RPG】2026新年假期必玩开荒服务器！100+在线玩法轻松！数值平衡护肝！【Minecraft服务器】【新年元旦必玩我的世界新服】",
    "url": "http://www.bilibili.com/video/av116097328222319",
    "source": "Minecraft_希希",
    "platform": "bilibili",
    "points": 1459503,
    "published_at": "2026-02-19T12:39:27+00:00",
    "summary": "龙陨纪元 -大型原创斗魂RPG正式开荒！\n服务器官方群号：1080918911\n超百个副本供你探寻\n我们拥有十分方便的挂机系统 — —只需按下特殊按键即可触发自动打怪，刷取材料不二之选\n拥有平衡的战斗数值系统 — — 防止因数值膨胀而导致的战力崩坏\n强化、分解、镶嵌、锻造 — — 拥有超多的RPG玩法以及独有的魂灵跟随系统，以及宠物等超多玩法\n我们还拥有自由交易的全球市场以及各种各样随着节假日更新"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1361719,
    "published_at": "2026-07-05T02:00:00+00:00",
    "summary": "用不上codex的朋友们！新的国产Agent直接上手，来跑通8大用法～\n感谢朋友们的三连+关注～"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1321031,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 1262681,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1o19aBJEAo",
    "domain": "AI",
    "title": "【全100集】吊打付费！目前B站最全最细的AI真人短剧制作保姆级教程！2026最新版AI视频生成全流程教学！七天就能从小白到大神！带你从入门到精通实现商业变现！",
    "url": "http://www.bilibili.com/video/av116492733518306",
    "source": "AI绘画学习教程",
    "platform": "bilibili",
    "points": 1207378,
    "published_at": "2026-05-04T08:11:00+00:00",
    "summary": "持续更新中！资料和工具在评论区哦"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 1095106,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1qZSLBYEpa",
    "domain": "AI",
    "title": "【整整600集】清华大学196小时讲完的AI人工智能从入门到精通全套教程，全程干货无废话！学完变大佬！这还学不会，我退出IT圈！机器学习-深度学习-opencv",
    "url": "http://www.bilibili.com/video/av115626794420560",
    "source": "IT界扛霸子",
    "platform": "bilibili",
    "points": 1082575,
    "published_at": "2025-11-28T10:20:16+00:00",
    "summary": "课程涵盖基础概念、算法原理、实践应用，从零开始，深入浅出。通过实例演示，掌握神经网络、决策树、支持向量机等关键技术。适合初学者和进阶者，助您快速提升技能，开启智能时代新篇章。立即观看，开启您的AI学习之旅！"
  },
  {
    "id": "bvid:BV1vY4y1x7mQ",
    "domain": "AI",
    "title": "我的世界  ⌈12个服务器推荐⌋ 2023 Java版 多人小游戏服 PVP RPG服",
    "url": "http://www.bilibili.com/video/av639758453",
    "source": "MiYuDoubleD",
    "platform": "bilibili",
    "points": 973301,
    "published_at": "2022-06-07T14:09:58+00:00",
    "summary": "最近我的世界搞活动买一送一，大家都领了Java版\n推荐给大家12个好玩有趣的Java版多人服务器，可以愉快的和小伙伴联机\n都是很好玩的的小游戏服，其中还有rpg服和pvp游戏，人数都很多\n mc.hypixel.net\n us.mineplex.com\n 2b2t.org\n play.wynncraft.com\n mccentral.org\n mc.manacube.net\n mc.gamster"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 950853,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 945534,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1ABu96JEAR",
    "domain": "AI",
    "title": "【保姆级教程】WorkBuddy彻底玩明白！只看这一期就够了！10节付费课内容全公开，完整工作流+实战技巧全揭秘，零基础一小时从入门到精通【附完整资料】",
    "url": "http://www.bilibili.com/video/av117069685262348",
    "source": "workbuddy应用实战",
    "platform": "bilibili",
    "points": 844132,
    "published_at": "2026-08-10T06:05:50+00:00",
    "summary": "这可能是B站最全的WorkBuddy免费教程。咱们把付费课程做成了免费课程，感谢观众大老爷的两币奉上，有喜欢的也可以一键三连。 评论“蓝皮书”领取全套资料\n我花了整整一周，从安装到实战到管理思维，把WorkBuddy这个腾讯云AI桌面工作台拆成了10步，每一步都带实操。你不需要任何基础，跟着点就行。"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 800455,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 688897,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 673840,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 621403,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 589949,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1TSg7zuEqR",
    "domain": "AI",
    "title": "Agent 的概念、原理与构建模式 —— 从零打造一个简化版的 Claude Code",
    "url": "http://www.bilibili.com/video/av114894200380730",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 575105,
    "published_at": "2025-07-22T01:07:39+00:00",
    "summary": "Agent 的概念、原理与构建模式 —— 从零打造一个简化版的 Claude Code\n \n我们将以 ReAct 和 Plan-And-Execute 这两种模式为例，为大家讲解 Agent 的概念、原理与构建模式，并在这个过程中为大家演示如何从零打造一个简化版的 Claude Code，让大家彻底明白 Agent 是如何运作的。\n \n时间轴：\n00:00 视频内容介绍\n00:33 什么是 Age"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 443095,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1Vz3v6XE7w",
    "domain": "AI",
    "title": "纯手搓一部AI漫剧一个月收获3.1w！附教程！全流程操作演示！让零基础也能学会AI漫剧制作技巧！更多AI漫剧工具提示词+变现方法及全套教程都整啦！拿走不谢~",
    "url": "http://www.bilibili.com/video/av116996553312339",
    "source": "comfyui视频工作流",
    "platform": "bilibili",
    "points": 370961,
    "published_at": "2026-07-28T12:00:00+00:00",
    "summary": "本套教程从零开始讲解，手把手教学，无论是新手小白，还是有一定经验的选手，皆可学习~\n配套工具软件 | 素材 | AIGC SeeDance2.0 即梦AI 学习路线\n分享给各位还在寻找资料宝子们！一键三联抱走吖\n视频制作不易，同学们觉得对你有帮助的话记得点点关注，一键三连【666】感谢支持！！"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 365978,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 355013,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1Zgud6LEoh",
    "domain": "AI",
    "title": "【最新版】小白速通 Codex 教程（含 DeepSeek 接入，无需 ChatGPT 订阅）",
    "url": "http://www.bilibili.com/video/av117070826047031",
    "source": "林粒粒呀",
    "platform": "bilibili",
    "points": 343218,
    "published_at": "2026-08-10T10:54:20+00:00",
    "summary": "Codex 安装 + 上手速通，保姆级教程！\n无需 ChatGPT 订阅，国内直连 DeepSeek"
  },
  {
    "id": "bvid:BV1Bg41187xJ",
    "domain": "AI",
    "title": "Minecraft丨国内最全的PVP服务器推荐3",
    "url": "http://www.bilibili.com/video/av516838082",
    "source": "时空koi",
    "platform": "bilibili",
    "points": 314930,
    "published_at": "2022-10-21T12:54:18+00:00",
    "summary": "建议1080P60帧观看\n\n很明显可以看到近几年国内的服务器在逐渐减少\n一年比一年少了，我的视频不知道能更到第几期呢 \n\n标题党，可能不是最全但绝对包含了大部分服务器\n如果有帮到你能给可怜的up主点个赞吗\n或者投两个硬币QAQ关注也可以！\n以下排名不分先后\nmc.accentery.cn【离线服】\nchina.syuu.net【正版服】\nkazer.cc【正版服】\nplay.mcsytt.com【"
  },
  {
    "id": "bvid:BV1aTtk61Efi",
    "domain": "AI",
    "title": "全网首测！外网博主Dream新开的服务器到底能不能玩？",
    "url": "http://www.bilibili.com/video/av117214220911938",
    "source": "Fuvin_",
    "platform": "bilibili",
    "points": 311677,
    "published_at": "2026-09-04T22:30:00+00:00",
    "summary": "第一次做这种服务器测评！可能不太好！如果你有意见欢迎发在评论区！\n如果后面这个服务器有什么改动 我也会及时更新 关注我以了解最新资讯！"
  },
  {
    "id": "bvid:BV1t55v6DE2v",
    "domain": "AI",
    "title": "Agent和Harness到底是什么？一个动画彻底搞懂！",
    "url": "http://www.bilibili.com/video/av116577945062195",
    "source": "轩辕的编程宇宙",
    "platform": "bilibili",
    "points": 309898,
    "published_at": "2026-05-15T10:02:14+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1Krpfe8EfU",
    "domain": "AI",
    "title": "我的世界【国内离线服务器推荐】2024离线服务器 小游戏 生存 RPG 无政府 星露谷 粘液科技",
    "url": "http://www.bilibili.com/video/av112978611474242",
    "source": "一只呱呱捏",
    "platform": "bilibili",
    "points": 305262,
    "published_at": "2024-08-17T17:51:07+00:00",
    "summary": "视频制作不易还请一键三连加关注(≧ω≦)/\n1.mc.163mc.cn\n2.wdsj.net\n3.mc.remiaft.com\n4.2b2t.xin\n5.CHAOS SMP 白名单：624324072\n6.方块传说服务器群：458742218\n7.魔法小镇服务器群：925055004\n8.缘木方舍服务器群：1006141418"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 292222,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 284564,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 265695,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1ZH4y1w784",
    "domain": "AI",
    "title": "2024年最好的几个离线服务器推荐！！！",
    "url": "http://www.bilibili.com/video/av1056095319",
    "source": "六匹狼pwq",
    "platform": "bilibili",
    "points": 250176,
    "published_at": "2024-07-10T10:33:48+00:00",
    "summary": "1：kkcraft ip：mc.163mc.cn  人多挂多\n2:blocksmc ip:blocksmc.com  hvh服务器，但是人多\n3:pikanetwork ip:pikanetwork.net 人多反作弊还行没有skywars\n4:月亮曲奇   史一坨\n5:高版本pvp服务器\n6:jn服 ip:jartexnetwork.com   人多反作弊吊我挺喜欢，没skywars\n关注我❤ "
  },
  {
    "id": "bvid:BV1e3t4etExj",
    "domain": "AI",
    "title": "手摸手的AI编程cursor实战【小白教程】",
    "url": "http://www.bilibili.com/video/av113148447169565",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 236867,
    "published_at": "2024-09-17T01:00:00+00:00",
    "summary": "喜欢的朋友可以三连+关注～这对我真的很重要"
  },
  {
    "id": "bvid:BV13XjB6gERT",
    "domain": "AI",
    "title": "豆包、WorkBuddy、Codex、Hermes……到底怎么选？用 AI 的 5 层路线",
    "url": "http://www.bilibili.com/video/av116776184776494",
    "source": "CreateSomething",
    "platform": "bilibili",
    "points": 223174,
    "published_at": "2026-06-19T11:00:00+00:00",
    "summary": "现在 AI 工具越来越多。\n   \n豆包、Kimi、DeepSeek、ChatGPT、Claude、WorkBuddy、Manus、Cursor、Trae、Codex、Claude Code、OpenClaw、Hermes……看起来每个都值得学。\n   \n但真正的问题不是工具名不够多，而是你还不知道自己处在哪一层。\n   \n这期我把常见 AI 工具放回一条 5 层路线里：\n1. 交给 AI 一个问"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 210680,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1E6CFBMEnk",
    "domain": "AI",
    "title": "【2025最新版】目前B站最全最细的 CurSor AI编程零基础全套教程，手把手教你搭建高效Cursor工作流，全程干货无废话！cursor教程｜AI 编程",
    "url": "http://www.bilibili.com/video/av115524067463218",
    "source": "诸葛老师本人",
    "platform": "bilibili",
    "points": 194842,
    "published_at": "2025-11-10T06:52:42+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\n‍视频配套笔记、AI大模型笔记代码：https://www.bilibili.com/read/cv43354937/?jump_opus=1"
  },
  {
    "id": "bvid:BV1E6FjzcEN9",
    "domain": "AI",
    "title": "寒假不知道玩啥？！高版本PVP服务器推荐！【Minecraft】",
    "url": "http://www.bilibili.com/video/av116025119083693",
    "source": "Fuvin_",
    "platform": "bilibili",
    "points": 192679,
    "published_at": "2026-02-07T00:00:00+00:00",
    "summary": "所有服务器的ip以及是否需要正版验证均在视频左上角注明！！！\n对你有帮助请关注我！！我真的真的很需要你的支持！！\n想练习pvp也可以找我！我可以手把手教你！！\n我是Fuvin！晚安！"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 183650,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1YG7G6eEPR",
    "domain": "AI",
    "title": "【全60集】吊打付费！目前B站最全最细的Agent智能体开发全套教程！手把手教你打造专属智能体，七天就能从小白到大神！带你从零基础入门到精通实现商业变现！",
    "url": "http://www.bilibili.com/video/av116815090947614",
    "source": "AI-Agent开发",
    "platform": "bilibili",
    "points": 164751,
    "published_at": "2026-06-26T06:57:42+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1eYPpeWEnT",
    "domain": "AI",
    "title": "Cursor + MCP = 王炸！彻底颠覆我的Cursor工作流，效率直接起飞",
    "url": "http://www.bilibili.com/video/av114073660301264",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 151447,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49724881",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia announces native GPU programming in Rust",
    "url": "https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/",
    "source": "nonmaskable",
    "platform": "hackernews",
    "points": 969,
    "published_at": "2026-09-16T11:15:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:49673098",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is the central bank of AI",
    "url": "https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai",
    "source": "tolugenius",
    "platform": "hackernews",
    "points": 582,
    "published_at": "2026-09-12T15:08:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49714096",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC revealing details about next gen A14 node",
    "url": "https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331",
    "source": "osnium123",
    "platform": "hackernews",
    "points": 126,
    "published_at": "2026-09-15T15:31:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49682319",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia dismisses \"circular financing\", says every $1 it invests brings back $100",
    "url": "https://invezz.com/news/2026/09/11/nvidia-says-every-1-it-invests-brings-back-100-so-why-does-the-stock-keep-falling/",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 138,
    "published_at": "2026-09-13T10:29:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49777694",
    "domain": "AI 算力 / 半导体",
    "title": "Autonomous strike drone uses Nvidia Jetson Orin Nano to pick and bomb targets",
    "url": "https://www.tomshardware.com/tech-industry/drones/autonomous-strike-drone-uses-nvidia-jetson-orin-nano-to-independently-pick-and-bomb-targets-swedish-startups-attack-drones-run-small-ai-model-require-no-human-input-and-zero-external-comms",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-09-20T17:07:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49773511",
    "domain": "AI 算力 / 半导体",
    "title": "Every Nvidia GPU has 10 to 30 RISC-V cores inside it",
    "url": "https://www.xda-developers.com/your-nvidia-gpu-dozens-risc-v-cores-one-took-over-graphics-driver/",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-09-20T07:50:58+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/how-ai-is-accelerating-pcb-design-and-prototyping/",
    "domain": "AI 算力 / 半导体",
    "title": "How AI Is Accelerating PCB Design and Prototyping",
    "url": "https://www.eetimes.com/how-ai-is-accelerating-pcb-design-and-prototyping/",
    "source": "Emily Newton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T07:59:35+00:00",
    "summary": "AI tools compress PCB design timelines from months to hours, enabling faster iteration cycles and letting engineers focus on innovation. The post How AI Is Accelerating PCB Design and Prototyping appe"
  },
  {
    "id": "rss:https://www.eetimes.com/singapore-turning-quantum-research-into-business-opportunity/",
    "domain": "AI 算力 / 半导体",
    "title": "Singapore: Turning Quantum Research into Business Opportunity",
    "url": "https://www.eetimes.com/singapore-turning-quantum-research-into-business-opportunity/",
    "source": "Pietro Guzzetti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T20:00:00+00:00",
    "summary": "Singapore’s government funding, research infrastructure, and commercial focus are creating a booming regional hub for quantum technologies. The post Singapore: Turning Quantum Research into Business O"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-power-demands-push-gan-into-data-center-design/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Power Demands Push GaN into Data Center Design",
    "url": "https://www.eetimes.com/ai-power-demands-push-gan-into-data-center-design/",
    "source": "Stephen Las Marias",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T16:59:04+00:00",
    "summary": "Rising AI power demands are pushing data center designers toward GaN-based power conversion for higher efficiency and density. The post AI Power Demands Push GaN into Data Center Design appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/highly-integrated-multibeam-beamformers-offer-swap-benefits-for-payload-phased-array-antennas/",
    "domain": "AI 算力 / 半导体",
    "title": "Highly Integrated Multibeam Beamformers Offer SWaP Benefits for Payload Phased Array Antennas",
    "url": "https://www.eetimes.com/highly-integrated-multibeam-beamformers-offer-swap-benefits-for-payload-phased-array-antennas/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T14:00:00+00:00",
    "summary": "Satellite payload designers are under growing pressure to deliver more capacity, wider coverage, and greater flexibility while working within strict size, weight, and power constraints. As phased-arra"
  },
  {
    "id": "rss:https://www.eetimes.com/redefining-intelligent-hmi-at-the-edge-how-ai-is-transforming-human-machine-interaction/",
    "domain": "AI 算力 / 半导体",
    "title": "Redefining Intelligent HMI at the Edge: How AI Is Transforming Human-Machine Interaction",
    "url": "https://www.eetimes.com/redefining-intelligent-hmi-at-the-edge-how-ai-is-transforming-human-machine-interaction/",
    "source": "Omar Cruz, Senior Manager PSOC™ Edge, Infineon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:00:00+00:00",
    "summary": "Next-generation HMI systems are evolving beyond the touchscreen into intelligent, context-aware experiences powered by edge AI The post Redefining Intelligent HMI at the Edge: How AI Is Transforming H"
  },
  {
    "id": "rss:https://www.eetimes.com/design-once-reuse-forever-the-reconfigurable-analog-front-end/",
    "domain": "AI 算力 / 半导体",
    "title": "Design Once, Reuse Forever: The Reconfigurable Analog Front End",
    "url": "https://www.eetimes.com/design-once-reuse-forever-the-reconfigurable-analog-front-end/",
    "source": "Robert Schreiber, Analog Product Marketing Director, Renesas Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:00:00+00:00",
    "summary": "AnalogPAK turns the analog front end into a configurable, reusable design: one PCB supports multiple sensors and ranges with no board re-spin. The post Design Once, Reuse Forever: The Reconfigurable A"
  },
  {
    "id": "rss:https://www.eetimes.com/scaling-physical-ai-deployment-beyond-the-demo/",
    "domain": "AI 算力 / 半导体",
    "title": "Scaling Physical AI Deployment Beyond the Demo",
    "url": "https://www.eetimes.com/scaling-physical-ai-deployment-beyond-the-demo/",
    "source": "Intel Corporation",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:00:00+00:00",
    "summary": "Scaling VLA robotics requires optimized inference, heterogeneous compute and real-time control on edge hardware. The post Scaling Physical AI Deployment Beyond the Demo appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/chinas-dram-specialist-cxmt-eyes-nand-flash-entry/",
    "domain": "AI 算力 / 半导体",
    "title": "China’s DRAM Specialist CXMT Eyes NAND Flash Entry",
    "url": "https://www.eetimes.com/chinas-dram-specialist-cxmt-eyes-nand-flash-entry/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T11:58:25+00:00",
    "summary": "China’s twin memory stars, CXMT and YMTC, move into each other’s turf to capitalize on AI-driven storage shortages. The post China’s DRAM Specialist CXMT Eyes NAND Flash Entry appeared first on EE Tim"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-crypto-mining-expose-global-compute-infrastructure-constraints/",
    "domain": "AI 算力 / 半导体",
    "title": "AI, Crypto Mining Expose Global Compute Infrastructure Constraints",
    "url": "https://www.eetimes.com/ai-crypto-mining-expose-global-compute-infrastructure-constraints/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T07:50:44+00:00",
    "summary": "Global semiconductor bottlenecks, multi-year foundry lead times, and rising trade friction leave European compute infrastructure supply-constrained amid surging AI and blockchain hardware demand. The "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/iphone-18-pro-max-storage-can-drop-lower-than-a-hard-drive-at-1-1-mb-s-during-heavy-writes-qlc-nand-offers-higher-capacity-but-reportedly-suffers-38-percent-drop-compared-to-tlc-based-pro",
    "domain": "AI 算力 / 半导体",
    "title": "iPhone 18 Pro Max storage can drop lower than a hard drive at 1.1 MB/s during heavy writes — QLC NAND offers higher capacity but reportedly suffers 38% drop compared to TLC-based Pro",
    "url": "https://www.tomshardware.com/pc-components/ssds/iphone-18-pro-max-storage-can-drop-lower-than-a-hard-drive-at-1-1-mb-s-during-heavy-writes-qlc-nand-offers-higher-capacity-but-reportedly-suffers-38-percent-drop-compared-to-tlc-based-pro",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T17:34:47+00:00",
    "summary": "Apple's use of QLC NAND allows the iPhone 18 Pro Max to offer higher storage capacity, but Homolab's testing highlights the potential performance trade-off under sustained writes."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/get-the-worlds-fastest-gaming-cpu-and-a-dlss-5-capable-gpu-in-a-gaming-pc-for-usd2-299-fully-loaded-powerhouse-sports-ryzen-7-9800x3d-rtx-5080-founders-edition-32gb-ram-and-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Get the world’s fastest gaming CPU and a DLSS 5-capable GPU in a gaming PC for $2,299 — fully loaded powerhouse sports Ryzen 7 9800X3D, RTX 5080 Founders Edition, 32GB RAM, and 1TB SSD [Updated]",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/get-the-worlds-fastest-gaming-cpu-and-a-dlss-5-capable-gpu-in-a-gaming-pc-for-usd2-299-fully-loaded-powerhouse-sports-ryzen-7-9800x3d-rtx-5080-founders-edition-32gb-ram-and-1tb-ssd",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T17:19:27+00:00",
    "summary": "Walmart is selling a CyberPowerPC gaming PC with a Ryzen 7 9800X3D, GeForce RTX 5080 Founders Edition, 32GB of DDR5-6000 memory, and a 1TB PCIe 4.0 SSD for $2,299."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/local-opposition-blocked-usd68-billion-worth-of-data-center-projects-in-the-second-quarter-of-2026-data-center-investments-reportedly-still-on-track-to-hit-usd32-trillion-by-2050",
    "domain": "AI 算力 / 半导体",
    "title": "Local opposition blocked 45 data center projects worth $68 billion in the second quarter of 2026 — data center investments reportedly still on track to hit $32 trillion by 2050",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/local-opposition-blocked-usd68-billion-worth-of-data-center-projects-in-the-second-quarter-of-2026-data-center-investments-reportedly-still-on-track-to-hit-usd32-trillion-by-2050",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T16:00:00+00:00",
    "summary": "Local opposition to data center buildouts has blocked $68 billion worth of data center projects in the second quarter of 2026, despite investments still rising."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/amd-beats-intel-to-the-trillion-dollar-club-as-stock-price-soars-firm-joins-nvidia-broadcom-and-sk-hynix-for-companies-worth-over-usd1-trillion",
    "domain": "AI 算力 / 半导体",
    "title": "AMD beats Intel to the trillion-dollar club as stock price soars — firm joins Nvidia, Broadcom, and SK hynix for companies worth over $1 trillion",
    "url": "https://www.tomshardware.com/tech-industry/amd-beats-intel-to-the-trillion-dollar-club-as-stock-price-soars-firm-joins-nvidia-broadcom-and-sk-hynix-for-companies-worth-over-usd1-trillion",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T15:42:55+00:00",
    "summary": "AMD has crossed the $1 trillion market cap mark, joining an exclusive list of less than two dozen companies around the world."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-ryzen-5-5500f-and-7500-show-up-at-retail-with-pricing-above-msrp-budget-cpus-are-usd20-more-expensive-than-list-price-even-from-first-party-sellers",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen 5 5500F and 7500 show up at retail with pricing above MSRP — budget CPUs are $20 more expensive than list price, even from first-party sellers",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-ryzen-5-5500f-and-7500-show-up-at-retail-with-pricing-above-msrp-budget-cpus-are-usd20-more-expensive-than-list-price-even-from-first-party-sellers",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T14:45:00+00:00",
    "summary": "Nearly two weeks after they were announced, AMD's Ryzen 5 5500F and 7500 (non-F) are available for sale, though prices are slightly above MSRP."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-shelves-global-ai-chip-rollout-as-chinas-own-demand-outstrips-supply-15-488-chip-atlas-clusters-leverage-optical-networking-to-counter-nvidia-scales-to-120-eflops",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei shelves global AI chip rollout as China's own demand outstrips supply — 15,488-chip Atlas clusters leverage optical networking to counter Nvidia, scales to 120 EFLOPS",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-shelves-global-ai-chip-rollout-as-chinas-own-demand-outstrips-supply-15-488-chip-atlas-clusters-leverage-optical-networking-to-counter-nvidia-scales-to-120-eflops",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T14:30:00+00:00",
    "summary": "Huawei says it will not offer its latest AI hardware outside of China citing lack of capacity to serve domestic demand."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/new-rtx-5070-autumn-limited-edition-gaming-gpu-doubles-as-an-air-freshener-with-built-in-e-sports-aromatherapy-ax-gamings-white-and-purple-card-also-features-an-anime-character-and-floral-graphics",
    "domain": "AI 算力 / 半导体",
    "title": "New RTX 5070 Autumn Limited Edition gaming GPU doubles as an air freshener with built-in 'e-sports aromatherapy' — AX Gaming's white and purple card also features an anime character and floral graphic",
    "url": "https://www.tomshardware.com/pc-components/gpus/new-rtx-5070-autumn-limited-edition-gaming-gpu-doubles-as-an-air-freshener-with-built-in-e-sports-aromatherapy-ax-gamings-white-and-purple-card-also-features-an-anime-character-and-floral-graphics",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T14:00:00+00:00",
    "summary": "AX Gaming has revealed its latest seasonal anime-themed limited edition graphics card which, this time, is designed to please your nose as much as your eyes."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/snag-the-least-expensive-32gb-ddr5-6000-memory-kit-available-for-only-usd429-usd40-off-promo-code-for-v-color-manta-xsky-yields-the-least-expensive-ddr5-6000-cl30-kit-available-right-now",
    "domain": "AI 算力 / 半导体",
    "title": "Snag the least expensive 32GB DDR5-6000 memory kit available for only $429 — $40 off promo code for V-Color Manta XSky yields the least expensive DDR5-6000 CL30 kit available right now",
    "url": "https://www.tomshardware.com/pc-components/snag-the-least-expensive-32gb-ddr5-6000-memory-kit-available-for-only-usd429-usd40-off-promo-code-for-v-color-manta-xsky-yields-the-least-expensive-ddr5-6000-cl30-kit-available-right-now",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:30:00+00:00",
    "summary": "Buy 32GB of V-Color Manta XSky RAM for only $429. This capable, white DDR5-6000 CL30 kit is one of the best deals out for the speed and timings"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/president-trump-has-announced-plans-for-new-ai-force-and-ai-czar-amid-growing-ai-safety-concerns-new-unit-will-cherish-ai-and-not-stifle-it-trump-clarifies-while-dismissing-safety-warnings-as-hoaxes",
    "domain": "AI 算力 / 半导体",
    "title": "President Trump has announced plans for new 'AI Force' and 'AI Czar' amid growing AI safety concerns — new unit will 'cherish' AI and not 'stifle' it, Trump clarifies, while dismissing safety warnings",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/president-trump-has-announced-plans-for-new-ai-force-and-ai-czar-amid-growing-ai-safety-concerns-new-unit-will-cherish-ai-and-not-stifle-it-trump-clarifies-while-dismissing-safety-warnings-as-hoaxes",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:15:00+00:00",
    "summary": "President Trump says he will create an AI Force and appoint a new AI czar while prioritizing rapid U.S. AI development and competition with China."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/typesafe-ais-jev-offers-an-alternative-to-llms-that-claims-to-be-193x-faster-and-445x-cheaper-system-one-type-model-is-bespoke-for-probabilistic-decision-making",
    "domain": "AI 算力 / 半导体",
    "title": "TypeSafe AI's Jev offers an alternative to LLMs that claims to be 193x faster and 445x cheaper — System One type model is bespoke for probabilistic decision-making",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/typesafe-ais-jev-offers-an-alternative-to-llms-that-claims-to-be-193x-faster-and-445x-cheaper-system-one-type-model-is-bespoke-for-probabilistic-decision-making",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:09:27+00:00",
    "summary": "Last week saw the debut of TypeSafe AI's Jev, its first \"System One\" model. Rather than chatting with users like conventional LLMs, it's strictly designed for statement evaluation and decision-making,"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/mediateks-next-gen-dimensity-cx-c10-max-will-power-new-googlebook-initiative-3nm-soc-has-similar-specs-to-kompanio-ultra-in-chromebook-plus-devices-despite-claims-of-elevating-computing-portfolio",
    "domain": "AI 算力 / 半导体",
    "title": "MediaTek’s next-gen Dimensity CX C10 Max will power new Googlebook initiative alongside Intel and Qualcomm – 3nm SoC has similar specs to Kompanio Ultra in Chromebook Plus devices, despite claims of ‘",
    "url": "https://www.tomshardware.com/pc-components/cpus/mediateks-next-gen-dimensity-cx-c10-max-will-power-new-googlebook-initiative-3nm-soc-has-similar-specs-to-kompanio-ultra-in-chromebook-plus-devices-despite-claims-of-elevating-computing-portfolio",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:00:00+00:00",
    "summary": "MediaTek's next-gen Dimensity CX C10 Max will arrive inside Googlebook devices, featuring similar specs as the Kompanio Ultra 910 currently available."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/playstation-3-emulation-devs-work-around-an-nvidia-bug-for-up-to-37-percent-faster-performance-open-source-coders-reach-out-to-nvidia-to-over-uncovered-bug",
    "domain": "AI 算力 / 半导体",
    "title": "PlayStation 3 emulation devs work around an Nvidia bug for up to 37% faster performance — open-source coders reach out to Nvidia to over uncovered bug",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/playstation-3-emulation-devs-work-around-an-nvidia-bug-for-up-to-37-percent-faster-performance-open-source-coders-reach-out-to-nvidia-to-over-uncovered-bug",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:00:00+00:00",
    "summary": "The developers of RPCS3 have found a workaround for an Nvidia driver bug and are touting up to 37% performance gains."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/hands-on-with-googlebooks-five-models-the-new-googlebook-os-and-a-mac-style-experience-for-android-users-at-premium-prices",
    "domain": "AI 算力 / 半导体",
    "title": "Hands-on with Googlebooks — Five models, the new Googlebook OS, and a Mac-style experience for Android users at premium prices",
    "url": "https://www.tomshardware.com/laptops/hands-on-with-googlebooks-five-models-the-new-googlebook-os-and-a-mac-style-experience-for-android-users-at-premium-prices",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:00:00+00:00",
    "summary": "Google has detailed its new Googlebooks, five laptops combining Android and ChromeOS to make a Mac-like experience for Android users, with a ton of Gemini tacked on."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/apple-mac-mini-late-2026-review",
    "domain": "AI 算力 / 半导体",
    "title": "Apple Mac mini (Late 2026) Review: Strong performance, but losing its grip on value",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/apple-mac-mini-late-2026-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:00:00+00:00",
    "summary": "The M6 Mac mini gets a considerable speed boost and a considerable price hike."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/apple-mac-studio-m5-ultra-review",
    "domain": "AI 算力 / 半导体",
    "title": "Apple Mac Studio (M5 Ultra) review: Local model citizen outpaces DGX Spark and Threadripper",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/apple-mac-studio-m5-ultra-review",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:00:00+00:00",
    "summary": "The Mac Studio with M5 Ultra delivers powerhouse productivity and AI performance in a small chassis."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/china-crafts-working-3nm-gate-all-around-transistors-without-euv-stacked-nanosheets-target-3nm-without-euv-but-full-node-remains-distant",
    "domain": "AI 算力 / 半导体",
    "title": "China crafts working 3nm gate-all-around transistors without EUV — stacked nanosheets target 3nm without EUV, but full node remains distant",
    "url": "https://www.tomshardware.com/tech-industry/china-crafts-working-3nm-gate-all-around-transistors-without-euv-stacked-nanosheets-target-3nm-without-euv-but-full-node-remains-distant",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T12:30:00+00:00",
    "summary": "As China's IMECAS demonstrates its ability to build GAA transistors without using DUV tools allegedly for 3nm-class process technology, the country remains years away from any practical implementation"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-projections-point-to-a-massive-usd278-billion-cash-burn-through-2030-that-exceeds-the-national-budgets-of-indonesia-and-norway-usd856-billion-compute-tab-outpaces-tenfold-revenue-surge",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI projections point to a massive $278 billion cash burn through 2030 that exceeds the national budgets of Indonesia and Norway — $856 billion compute tab outpaces tenfold revenue surge",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-projections-point-to-a-massive-usd278-billion-cash-burn-through-2030-that-exceeds-the-national-budgets-of-indonesia-and-norway-usd856-billion-compute-tab-outpaces-tenfold-revenue-surge",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T12:00:00+00:00",
    "summary": "OpenAI reportedly expects to spend $278 billion more money than it generates between 2026 and 2030 due to aggressive spending on compute capacity and adjacent infrastructure."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/devs-say-chinese-ai-company-silently-uploaded-hundreds-of-megabytes-of-local-workspace-data-z-ai-the-firm-behind-the-glm-models-didnt-ask-for-user-consent-and-made-564-attempts-to-exfiltrate-313mb-archive",
    "domain": "AI 算力 / 半导体",
    "title": "Devs say Chinese AI company silently uploaded hundreds of megabytes of local workspace data, company apologizes — Z.AI, the firm behind the GLM models, didn’t ask for user consent and made 564 attempt",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/devs-say-chinese-ai-company-silently-uploaded-hundreds-of-megabytes-of-local-workspace-data-z-ai-the-firm-behind-the-glm-models-didnt-ask-for-user-consent-and-made-564-attempts-to-exfiltrate-313mb-archive",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T11:59:49+00:00",
    "summary": "The second largest AI company in China is having to work frantically to patch up its reputation after a number of prominent devs raised flags about their local files and data being siphoned to online "
  },
  {
    "id": "rss:https://www.tomshardware.com/software/cloudflare-saves-100-tb-of-ram-again-this-time-by-slashing-server-hashes-by-90-percent-cutting-100-000-entries-down-to-10-000-eliminates-massive-cache-bloat",
    "domain": "AI 算力 / 半导体",
    "title": "Cloudflare saves 100 TB of RAM again, this time by slashing server hashes by 90% — cutting 100,000 entries down to 10,000 eliminates massive cache bloat",
    "url": "https://www.tomshardware.com/software/cloudflare-saves-100-tb-of-ram-again-this-time-by-slashing-server-hashes-by-90-percent-cutting-100-000-entries-down-to-10-000-eliminates-massive-cache-bloat",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T11:30:00+00:00",
    "summary": "Cloudflare has saved 100 TB of RAM again, but this time by tuning its hash-mapping algorithm."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/improve-your-gaming-experience-with-this-27-inch-asrock-fhd-180hz-gaming-monitor-thats-at-an-all-time-low-of-just-usd96-quality-ips-panel-with-amd-freesync-hdr400-and-1ms-response-time-is-40-percent-off",
    "domain": "AI 算力 / 半导体",
    "title": "Improve your gaming experience with this 27-inch ASRock FHD 180Hz gaming monitor that’s at an all-time low of just $96 — quality IPS panel with AMD Freesync, HDR400, and 1ms response time is 40% off",
    "url": "https://www.tomshardware.com/pc-components/improve-your-gaming-experience-with-this-27-inch-asrock-fhd-180hz-gaming-monitor-thats-at-an-all-time-low-of-just-usd96-quality-ips-panel-with-amd-freesync-hdr400-and-1ms-response-time-is-40-percent-off",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T11:01:52+00:00",
    "summary": "Jump into high-refresh-rate gaming without breaking the bank: ASRock’s 27-inch 1080p 180Hz IPS gaming monitor is just $96, a whopping 40% off and at an all-time low"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/texas-jury-hits-bambu-lab-with-usd27-6m-verdict-in-stratasys-patent-fight-x1-p1-and-a1-printers-found-to-infringe-prime-tower-and-bed-leveling-tech",
    "domain": "AI 算力 / 半导体",
    "title": "Texas jury hits Bambu Lab with $27.6M verdict in Stratasys patent fight — X1, P1, and A1 printers found to infringe prime tower and bed-leveling tech",
    "url": "https://www.tomshardware.com/3d-printing/texas-jury-hits-bambu-lab-with-usd27-6m-verdict-in-stratasys-patent-fight-x1-p1-and-a1-printers-found-to-infringe-prime-tower-and-bed-leveling-tech",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T11:00:00+00:00",
    "summary": "A Texas jury found Bambu Lab liable for patent infringement in the creation of the X1, P1 and A1 series of 3D printers, and awarded Stratasys, Inc. $27.6 million dollars in damages."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-controlled-robot-arms-attempted-harmful-tasks-97-percent-of-the-time-experiments-included-stabbing-a-baby-doll-mixing-chemicals-openai-and-anthropic-models-try-mixing-bleach-and-stabbing-dolls-without-jailbreaks",
    "domain": "AI 算力 / 半导体",
    "title": "AI-controlled robot arms attempted harmful tasks 97% of the time; experiments included stabbing a baby doll, mixing chemicals — OpenAI and Anthropic models try mixing bleach and stabbing dolls without",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-controlled-robot-arms-attempted-harmful-tasks-97-percent-of-the-time-experiments-included-stabbing-a-baby-doll-mixing-chemicals-openai-and-anthropic-models-try-mixing-bleach-and-stabbing-dolls-without-jailbreaks",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T10:30:00+00:00",
    "summary": "“Frontier robot policies,” the policies for models turning what a robot sees into what it does, “reliably carry out harmful instructions,” according to a Sept. 18 report by Robocurve."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/acer-ceo-says-memory-makers-are-hyping-2030-shortage-fears-to-protect-margins-pc-prices-set-to-decline-by-late-2027-cheaper-chinese-capacity-coming-online-delivers-lower-memory-prices",
    "domain": "AI 算力 / 半导体",
    "title": "Acer CEO says memory makers are hyping 2030 shortage fears to protect margins — PC prices set to decline by late 2027, cheaper Chinese capacity coming online delivers lower memory prices",
    "url": "https://www.tomshardware.com/pc-components/dram/acer-ceo-says-memory-makers-are-hyping-2030-shortage-fears-to-protect-margins-pc-prices-set-to-decline-by-late-2027-cheaper-chinese-capacity-coming-online-delivers-lower-memory-prices",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T10:00:00+00:00",
    "summary": "Acer chairperson and CEO Jason Chen believes that PC prices will plateau by the first half of next year and start coming down towards the latter part of 2027. He also said that memory makers predict h"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidias-next-gen-rtx-60-gpus-might-not-be-released-until-2028-prominent-leaker-claims-gaming-takes-a-back-seat-as-company-focuses-on-delivering-data-center-products",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's next-gen RTX 60 GPUs might not be released until 2028, prominent leaker claims — gaming takes a back seat as company focuses on delivering data center products",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidias-next-gen-rtx-60-gpus-might-not-be-released-until-2028-prominent-leaker-claims-gaming-takes-a-back-seat-as-company-focuses-on-delivering-data-center-products",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T09:52:19+00:00",
    "summary": "Leaker Kopite7kimi claims that Nvidia's next-gen RTX 60 series may not be released until 2028, meaning that consumers will have to wait three years between GPU generations"
  },
  {
    "id": "rss:https://www.tomshardware.com/raspberry-pi/techie-makes-his-own-motherboard-to-refurbish-15-year-old-hp-proliant-n40l-tower-server-raspberry-pi-cm5-adds-nvme-and-usb-3-0",
    "domain": "AI 算力 / 半导体",
    "title": "Techie makes his own motherboard to refurbish 15-year-old HP ProLiant N40L tower server — Raspberry Pi CM5 adds NVMe and USB 3.0",
    "url": "https://www.tomshardware.com/raspberry-pi/techie-makes-his-own-motherboard-to-refurbish-15-year-old-hp-proliant-n40l-tower-server-raspberry-pi-cm5-adds-nvme-and-usb-3-0",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T09:35:00+00:00",
    "summary": "Techie makes his own motherboard to refurbish an HP ProLiant N40L — Raspberry Pi 5 Compute Module to the rescue"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/give-your-pc-the-deep-clean-it-deserves-the-wolfbox-mf60-air-duster-with-up-to-110-000-rpm-drops-to-usd33-99",
    "domain": "AI 算力 / 半导体",
    "title": "Give your PC the deep clean it deserves — the Wolfbox MF60 Air Duster with up to 110,000 RPM drops to $33.99",
    "url": "https://www.tomshardware.com/pc-components/give-your-pc-the-deep-clean-it-deserves-the-wolfbox-mf60-air-duster-with-up-to-110-000-rpm-drops-to-usd33-99",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T20:30:42+00:00",
    "summary": "The Wolfbox MF60 packs dual 2,500mAh batteries, three fan speeds, USB Type-C charging, and multiple nozzles into a compact wireless air duster designed for cleaning PCs, laptops, keyboards, and more."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/webcams/dell-pro-7-webcam-4k-review",
    "domain": "AI 算力 / 半导体",
    "title": "Dell Pro 7 Webcam 4K Review: Sounds surprisingly great",
    "url": "https://www.tomshardware.com/peripherals/webcams/dell-pro-7-webcam-4k-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T15:11:14+00:00",
    "summary": "The Dell Pro 7 is a 4K / 60 fps webcam with surprisingly high-quality built-in mics, a built-in physical privacy shutter, and Windows Hello compatibility."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/anthropic-openai-spacexai-and-google-face-antitrust-lawsuit-for-agreeing-to-slow-ai-development-plaintiffs-say-plan-has-been-in-motion-for-months-before-calls-agreement-self-serving",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic, OpenAI, SpaceXAI, and Google face antitrust lawsuit for agreeing to slow AI development — plaintiffs say plan has been in motion for months before, calls agreement ‘self-serving’",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/anthropic-openai-spacexai-and-google-face-antitrust-lawsuit-for-agreeing-to-slow-ai-development-plaintiffs-say-plan-has-been-in-motion-for-months-before-calls-agreement-self-serving",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T14:48:57+00:00",
    "summary": "A proposed class action lawsuit has been lodged against the four big AI tech companies after they agreed to slow AI development for safety reasons. The lead counsel on the lawsuit says that 'AI will q"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/the-pc-gaming-ray-tracing-obsession-began-with-the-first-rtx-20-graphics-cards-released-on-this-day-in-2018-the-geforce-rtx-2080-and-2080-ti-led-the-charge-but-games-were-thin-on-the-ground",
    "domain": "AI 算力 / 半导体",
    "title": "The PC gaming ray tracing obsession began with the first RTX 20 graphics cards released on this day in 2018 — the GeForce RTX 2080 and 2080 Ti led the charge, but games were thin on the ground",
    "url": "https://www.tomshardware.com/pc-components/gpus/the-pc-gaming-ray-tracing-obsession-began-with-the-first-rtx-20-graphics-cards-released-on-this-day-in-2018-the-geforce-rtx-2080-and-2080-ti-led-the-charge-but-games-were-thin-on-the-ground",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T14:05:31+00:00",
    "summary": "Nvidia’s Turing GPU became available to enthusiasts for the first time on this day eight years ago."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/researchers-build-a-drone-that-navigates-with-physical-whiskers-to-operate-in-dark-dusty-or-smoky-places-where-cameras-or-gps-can-fail-sub-100-gram-drones-run-34kb-software-to-enable-sub-millimeter-precision",
    "domain": "AI 算力 / 半导体",
    "title": "Researchers build a drone that navigates with physical whiskers to operate in dark, dusty or smoky places where cameras or GPS can fail — sub-100 gram drones run 34KB software to enable sub-millimeter",
    "url": "https://www.tomshardware.com/tech-industry/drones/researchers-build-a-drone-that-navigates-with-physical-whiskers-to-operate-in-dark-dusty-or-smoky-places-where-cameras-or-gps-can-fail-sub-100-gram-drones-run-34kb-software-to-enable-sub-millimeter-precision",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T13:48:11+00:00",
    "summary": "Whiskers attached to three pressure sensors at their base could help drones find their way around their environment purely through touch. This lightweight system emulates the vibrissae found on mice a"
  },
  {
    "id": "rss:https://www.eetimes.com/intel-puts-high-na-euv-into-production-but-stitching-still-has-something-to-prove/",
    "domain": "AI 算力 / 半导体",
    "title": "Intel Puts High-NA EUV into Production, but Stitching Still Has Something to Prove",
    "url": "https://www.eetimes.com/intel-puts-high-na-euv-into-production-but-stitching-still-has-something-to-prove/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T22:00:00+00:00",
    "summary": "Panther Lake validates High NA in manufacturing, while electrical stitching and larger masks remain the next hurdles. The post Intel Puts High-NA EUV into Production, but Stitching Still Has Something"
  },
  {
    "id": "hn:49745610",
    "domain": "AI 算力 / 半导体",
    "title": "Run QWEN3.8 27B on 16gb Nvidia GPUs",
    "url": "https://github.com/MiaAI-Lab/Qwen3.8-27B-16gb-NVIDIA-GPUs-one-click-install",
    "source": "Pragmata",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-09-17T19:46:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49727093",
    "domain": "AI 算力 / 半导体",
    "title": "Apple May Return to Server Market with Nvidia Technology",
    "url": "https://www.macrumors.com/2026/09/16/apple-may-return-to-server-market/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-09-16T13:54:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:49657991",
    "domain": "AI 算力 / 半导体",
    "title": "How to Build a $20B Semiconductor Fab (2024)",
    "url": "https://www.construction-physics.com/p/how-to-build-a-20-billion-semiconductor",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-09-11T13:22:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49084371",
    "domain": "AI 算力 / 半导体",
    "title": "Show HN: Tines 3B – safe workflow automation for when everyone builds software",
    "url": "https://www.tines.com/",
    "source": "retsol",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-07-28T14:23:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49537553",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Flash and 3.8 Flash Cyber",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/",
    "source": "bratao",
    "platform": "hackernews",
    "points": 1160,
    "published_at": "2026-09-02T15:12:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611251",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas: a high-resolution map of human DNA",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/",
    "source": "utiiiD",
    "platform": "hackernews",
    "points": 607,
    "published_at": "2026-09-08T14:55:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49715947",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Live and 3.8 Live Extended Thinking",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/",
    "source": "leumon",
    "platform": "hackernews",
    "points": 490,
    "published_at": "2026-09-15T17:38:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49552299",
    "domain": "大厂 AI 动态",
    "title": "WeatherNext 3",
    "url": "https://deepmind.google/science/weathernext/",
    "source": "matthieu_bl",
    "platform": "hackernews",
    "points": 406,
    "published_at": "2026-09-03T16:06:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49790409",
    "domain": "大厂 AI 动态",
    "title": "Turn off and restrict access to Apple Intelligence features on Mac",
    "url": "https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac",
    "source": "alwillis",
    "platform": "hackernews",
    "points": 298,
    "published_at": "2026-09-21T17:30:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49468818",
    "domain": "大厂 AI 动态",
    "title": "Gemini-3.5-Transcribe",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/",
    "source": "k9294",
    "platform": "hackernews",
    "points": 363,
    "published_at": "2026-08-27T18:03:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:49467922",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni 1.1 Flash",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/",
    "source": "saretup",
    "platform": "hackernews",
    "points": 297,
    "published_at": "2026-08-27T17:06:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49727659",
    "domain": "大厂 AI 动态",
    "title": "The DeepMind Institute",
    "url": "https://institute.deepmind.com/",
    "source": "vertigoruntime",
    "platform": "hackernews",
    "points": 185,
    "published_at": "2026-09-16T14:32:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:49602490",
    "domain": "大厂 AI 动态",
    "title": "Emacs Bedrock 2.0",
    "url": "https://lambdaland.org/posts/2026-09-06-bedrock-v2/",
    "source": "ashton314",
    "platform": "hackernews",
    "points": 191,
    "published_at": "2026-09-07T20:12:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49773998",
    "domain": "大厂 AI 动态",
    "title": "Microsoft agentically ports Copilot runtime to Rust for $120K",
    "url": "https://www.theregister.com/devops/2026/09/18/microsoft-agentically-ports-copilot-runtime-to-rust-for-120k/5297549",
    "source": "pjmlp",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-09-20T09:08:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:49762493",
    "domain": "大厂 AI 动态",
    "title": "Gemini hacked three companies in first known breakout by Google's AI",
    "url": "https://www.reuters.com/business/gemini-hacked-three-companies-first-known-breakout-by-google-ai-wsj-reports-2026-09-18/",
    "source": "usernomdeguerre",
    "platform": "hackernews",
    "points": 76,
    "published_at": "2026-09-19T01:40:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49740330",
    "domain": "大厂 AI 动态",
    "title": "I had Gemini train its own replacement for $9",
    "url": "https://www.petervijeh.com/projects/reddit-ner",
    "source": "p-s-v",
    "platform": "hackernews",
    "points": 88,
    "published_at": "2026-09-17T13:17:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49704226",
    "domain": "大厂 AI 动态",
    "title": "Tell HN: iOS 27 does not allow Apple Intelligence to be disabled",
    "url": "https://news.ycombinator.com/item?id=49704226",
    "source": "nunez",
    "platform": "hackernews",
    "points": 76,
    "published_at": "2026-09-14T21:21:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49760988",
    "domain": "大厂 AI 动态",
    "title": "Gemini Hacked Three Companies in First Known Breakout by Google's AI",
    "url": "https://www.wsj.com/tech/ai/gemini-hacked-three-companies-in-first-known-breakout-by-googles-ai-5c0baba2",
    "source": "berkeleyjunk",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-09-18T22:17:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:49610641",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas predictive map of every DNA letter change in the human genome",
    "url": "https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/",
    "source": "fady0",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-09-08T14:14:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49743685",
    "domain": "大厂 AI 动态",
    "title": "Economic policy for AGI",
    "url": "https://institute.deepmind.com/essays/economic-policy-for-agi/",
    "source": "alphabetatango",
    "platform": "hackernews",
    "points": 65,
    "published_at": "2026-09-17T17:12:51+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/transportation/998550/a-cut-cable-disrupted-hundreds-of-flights-across-the-us",
    "domain": "大厂 AI 动态",
    "title": "A cut cable disrupted hundreds of flights across the US",
    "url": "https://www.theverge.com/transportation/998550/a-cut-cable-disrupted-hundreds-of-flights-across-the-us",
    "source": "TC. Sottek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T23:48:56+00:00",
    "summary": "Hundreds of flights were cancelled or delayed on Monday after construction crews in New Jersey accidentally cut a Verizon fiber cable used for air traffic control. FAA Administrator Bryan Bedford said"
  },
  {
    "id": "rss:https://www.theverge.com/tech/998539/amazon-data-center-water-conservation-colorado-river",
    "domain": "大厂 AI 动态",
    "title": "Amazon wants to help the Colorado River, but we still don’t know how much water the company uses",
    "url": "https://www.theverge.com/tech/998539/amazon-data-center-water-conservation-colorado-river",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T23:15:32+00:00",
    "summary": "Amazon plans to spend $20 million on water conservation projects along the Colorado River, a crucial but dwindling water supply for 40 million people in the Western US. The initiative comes as Amazon "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/998453/california-ai-data-center-bills",
    "domain": "大厂 AI 动态",
    "title": "California tightens rules on AI data center energy and water use",
    "url": "https://www.theverge.com/ai-artificial-intelligence/998453/california-ai-data-center-bills",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T20:29:45+00:00",
    "summary": "California Gov. Gavin Newsom has signed seven bills designed to prevent AI data centers from passing utility costs onto residents, as reported earlier by the Los Angeles Times. The package of laws req"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/998259/gm-apple-carplay-android-auto-phone-mirror-google",
    "domain": "大厂 AI 动态",
    "title": "GM can’t ‘bring back’ Apple CarPlay because it never left",
    "url": "https://www.theverge.com/transportation/998259/gm-apple-carplay-android-auto-phone-mirror-google",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T17:47:54+00:00",
    "summary": "Last week, GM announced a new software experience for its upcoming Chevy Silverado and GMC Sierra trucks, including a new look for Apple CarPlay and Android Auto, the popular phone mirroring systems t"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/998302/paramount-warner-bros-discovery-merger-settlement",
    "domain": "大厂 AI 动态",
    "title": "Paramount settles lawsuit blocking $110 billion Warner Bros. merger",
    "url": "https://www.theverge.com/entertainment/998302/paramount-warner-bros-discovery-merger-settlement",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T17:42:15+00:00",
    "summary": "Paramount has reached a settlement with California and the 11 other states that sued to block its planned $110 billion acquisition of Warner Bros. Discovery. The settlement removes a major roadblock s"
  },
  {
    "id": "rss:https://www.theverge.com/news/998317/bungie-destiny-2-unvaulted-raids-campaigns-destinations",
    "domain": "大厂 AI 动态",
    "title": "Bungie says it’s ‘not done with Destiny’ and will bring back vaulted content",
    "url": "https://www.theverge.com/news/998317/bungie-destiny-2-unvaulted-raids-campaigns-destinations",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T16:35:59+00:00",
    "summary": "Months after seemingly giving up on Destiny 2, Bungie now says it's planning to restore vaulted content in the game like campaigns, destinations, and raids. The decision reverses the Destiny Content V"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/998207/xbox-controller-chromebook-usbc-charger-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Grab an Xbox controller and a $50 Xbox gift card together for just $80",
    "url": "https://www.theverge.com/gadgets/998207/xbox-controller-chromebook-usbc-charger-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T15:13:32+00:00",
    "summary": "Newegg is hosting a bundle that includes Microsoft’s wireless Xbox controller (in black) and a $50 digital Xbox gift card together for $80. Given that this model typically sits around $50 to $60 depen"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/996874/apple-john-ternus-tim-cook-mark-gurman-future-ai-siri-iphone",
    "domain": "大厂 AI 动态",
    "title": "Can John Ternus find Apple’s next big thing?",
    "url": "https://www.theverge.com/podcast/996874/apple-john-ternus-tim-cook-mark-gurman-future-ai-siri-iphone",
    "source": "Nilay Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T14:00:00+00:00",
    "summary": "Today, I’m talking with Mark Gurman, who is the world’s best-sourced Apple reporter — both as Bloomberg’s chief Apple correspondent and the host of the upcoming podcast Power On.&#160; Earlier this mo"
  },
  {
    "id": "rss:https://www.theverge.com/tech/998191/apple-siri-ai-iphone-16-class-action-lawsuit-settlement",
    "domain": "大厂 AI 动态",
    "title": "iPhone owners can now submit claims in Apple’s $250 million Siri AI settlement",
    "url": "https://www.theverge.com/tech/998191/apple-siri-ai-iphone-16-class-action-lawsuit-settlement",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:36:52+00:00",
    "summary": "Apple is paying $250 million to settle claims that it failed to deliver an AI-upgraded Siri - and now, eligible iPhone owners can submit a claim for a payout. If you live in the US and purchased an iP"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/998165/vivo-x500-pro-max-launch-specs-release-date-lofic-china",
    "domain": "大厂 AI 动态",
    "title": "Vivo’s X500 Pro Max has 17 stops of dynamic range and 4K240 slo-mo",
    "url": "https://www.theverge.com/gadgets/998165/vivo-x500-pro-max-launch-specs-release-date-lofic-china",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:16:25+00:00",
    "summary": "Vivo's new X500 flagship phones have arrived in China, and as usual the company's focus is firmly on photography. The X500 Pro Max - a new tier in its lineup - is the first phone to use new sensors an"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/21/morphotonics-raises-e40m-as-it-tk-tk-tk-t/",
    "domain": "大厂 AI 动态",
    "title": "Morphotonics raises €40M to expand its display tech into data centers",
    "url": "https://techcrunch.com/2026/09/21/morphotonics-raises-e40m-as-it-tk-tk-tk-t/",
    "source": "Ivan Mehta, Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T06:00:00+00:00",
    "summary": "Deeptech company Morphotonics raises €40M from investors including 3M Ventures, Innovation Industries, BOM, and Invest-NL."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/21/the-man-who-built-apples-stores-doesnt-buy-silicon-valleys-bet-on-ai-shopping/",
    "domain": "大厂 AI 动态",
    "title": "The man who built Apple’s stores doesn’t buy Silicon Valley’s bet on AI shopping",
    "url": "https://techcrunch.com/2026/09/21/the-man-who-built-apples-stores-doesnt-buy-silicon-valleys-bet-on-ai-shopping/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T23:44:28+00:00",
    "summary": "Apple Store architect Ron Johnson says Apple's secret sauce has always been its people."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/21/openai-forms-math-advisory-group-as-its-ai-resolves-more-than-100-open-problems/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI forms math advisory group as its AI resolves more than 100 open problems",
    "url": "https://techcrunch.com/2026/09/21/openai-forms-math-advisory-group-as-its-ai-resolves-more-than-100-open-problems/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T20:15:58+00:00",
    "summary": "The group won't be given leeway to slow down or redirect OpenAI's ongoing mathematical research."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/21/discover-whats-next-5-days-left-to-save-up-to-200-on-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Discover what’s next: 5 days left to save up to $200 on your TechCrunch Disrupt 2026 ticket",
    "url": "https://techcrunch.com/2026/09/21/discover-whats-next-5-days-left-to-save-up-to-200-on-techcrunch-disrupt-2026/",
    "source": "Jessica Barrera",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T19:25:00+00:00",
    "summary": "Five days left to save up to $200 on your TechCrunch Disrupt 2026 pass + 50% off a second one. Join 10,000+ founders, investors, and operators at San Francisco’s Moscone West, October 13-15. Grab your"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/21/metas-muse-is-outpacing-chatgpts-early-mobile-launch/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s Muse is outpacing ChatGPT’s early mobile launch",
    "url": "https://techcrunch.com/2026/09/21/metas-muse-is-outpacing-chatgpts-early-mobile-launch/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T19:19:21+00:00",
    "summary": "Meta’s new AI agent Muse has racked up more downloads and daily active users in the U.S. and Canada than ChatGPT did over the same period after its mobile debut, according to new estimates from Appfig"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/21/kairos-power-gets-up-to-100m-from-samsung-group-to-build-nuclear-reactor-for-google/",
    "domain": "大厂 AI 动态",
    "title": "Kairos Power gets up to $100M from Samsung group to build nuclear reactor for Google",
    "url": "https://techcrunch.com/2026/09/21/kairos-power-gets-up-to-100m-from-samsung-group-to-build-nuclear-reactor-for-google/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T18:23:05+00:00",
    "summary": "Future Google supplier Kairos Power inked a deal with Samsung C&#038;T to help build its first 50-megawatt nuclear power plant."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/21/metas-ai-agent-has-been-blocked-from-using-amazon-com/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s AI agent has been blocked from using Amazon.com",
    "url": "https://techcrunch.com/2026/09/21/metas-ai-agent-has-been-blocked-from-using-amazon-com/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T17:55:18+00:00",
    "summary": "Amazon has its own cohort of foundation models, along with one of the most popular inference platforms on the internet. As long as they're under no legal obligation to open the doors to Muse, why woul"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/21/x-will-now-tell-users-when-governments-have-forced-it-to-limit-their-posts/",
    "domain": "大厂 AI 动态",
    "title": "X will now tell users when governments have forced it to limit their posts",
    "url": "https://techcrunch.com/2026/09/21/x-will-now-tell-users-when-governments-have-forced-it-to-limit-their-posts/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T17:45:35+00:00",
    "summary": "X is expanding its “Under the Hood” transparency tool to show when posts have been downranked or withheld in response to local laws and government demands, including which country made the request."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/21/ouras-2-2b-ipo-is-mostly-a-payday-for-existing-shareholders/",
    "domain": "大厂 AI 动态",
    "title": "Oura’s $2.2B IPO is mostly a payday for existing shareholders",
    "url": "https://techcrunch.com/2026/09/21/ouras-2-2b-ipo-is-mostly-a-payday-for-existing-shareholders/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T16:45:47+00:00",
    "summary": "Forerunner Ventures plans to sell its entire stake in Oura for as much as $1.26 billion, according to Oura's latest IPO filing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/21/with-tabby-a-former-accountant-is-using-ai-to-make-accountants-obsolete/",
    "domain": "大厂 AI 动态",
    "title": "With Tabby, a former accountant is using AI to make accountants obsolete",
    "url": "https://techcrunch.com/2026/09/21/with-tabby-a-former-accountant-is-using-ai-to-make-accountants-obsolete/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T16:38:51+00:00",
    "summary": "Tabby is designed to be a real-time bookkeeping interface, handling clients’ paperwork as it gives them up-to-the-minute data on their business’s profit and loss."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/21/where-will-the-next-breakout-startup-come-from-benchmarks-full-partnership-weighs-in-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Where will the next breakout startup come from? Benchmark’s full partnership weighs in at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/21/where-will-the-next-breakout-startup-come-from-benchmarks-full-partnership-weighs-in-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T15:00:00+00:00",
    "summary": "Where will the next breakout startup come from? Benchmark’s full partnership weighs in on the main stage at TechCrunch Disrupt 2026. Save up to $200 before September 25 at 11:59 p.m. PT. Register now."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/21/googles-899-googlebook-is-a-bet-that-youll-buy-a-new-laptop-for-gemini/",
    "domain": "大厂 AI 动态",
    "title": "Google’s $899 Googlebook is a bet that you’ll buy a new laptop for Gemini",
    "url": "https://techcrunch.com/2026/09/21/googles-899-googlebook-is-a-bet-that-youll-buy-a-new-laptop-for-gemini/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T14:39:22+00:00",
    "summary": "Google’s AI-native Googlebook ties Gemini to the cursor, dictation, widgets, and other parts of the desktop experience."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/21/from-first-users-to-billions-googles-robby-stein-joins-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "From first users to billions: Google’s Robby Stein joins TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/21/from-first-users-to-billions-googles-robby-stein-joins-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T14:30:00+00:00",
    "summary": "From first users to billions: Google’s Robby Stein joins TechCrunch Disrupt 2026. Lean in on this Builders Stage session. Save up to $200 before September 25."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/21/meet-the-next-wave-of-vcs-judging-startup-battlefield-200-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Meet the next wave of VCs judging Startup Battlefield 200 at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/21/meet-the-next-wave-of-vcs-judging-startup-battlefield-200-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T14:15:00+00:00",
    "summary": "Meet the next wave of VCs judging the Startup Battlefield 200 contenders on the main stage at TechCrunch Disrupt 2026. Register by September 25 at 11:59 p.m. PT, to save up to $200 and to get a front-"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/21/corridor-raises-25m-seed-to-build-a-health-benefits-brokerage-for-smbs/",
    "domain": "大厂 AI 动态",
    "title": "Corridor raises $25M seed to build a health benefits brokerage for SMBs",
    "url": "https://techcrunch.com/2026/09/21/corridor-raises-25m-seed-to-build-a-health-benefits-brokerage-for-smbs/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:49:00+00:00",
    "summary": "Corridor focuses on SMBs, which it says traditional brokerages often overlook because small accounts generate lower commissions than larger accounts."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/20/6-days-left-to-get-ahead-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "6 days left to save up to $200 to TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/20/6-days-left-to-get-ahead-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T21:41:08+00:00",
    "summary": "Current ticket pricing ends in 6 days on September 25 at 11:59 p.m. PT. Join 10,000+ founders, investors, and tech leaders at Disrupt and save up to $200 on your ticket."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/20/world-model-companies-are-keeping-a-lot-of-secrets/",
    "domain": "大厂 AI 动态",
    "title": "World model companies are keeping a lot of secrets",
    "url": "https://techcrunch.com/2026/09/20/world-model-companies-are-keeping-a-lot-of-secrets/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T20:29:07+00:00",
    "summary": "Everyone in the world-models space is sitting on a pile of cash and a ton of buzz, but good luck getting anyone — from the founders to their own data suppliers — to tell you what they're actually buil"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/20/elon-musks-latest-boring-company-pitch-involves-a-hyperloop-between-austin-and-san-antonio/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk’s latest Boring Company pitch involves a Hyperloop between Austin and San Antonio",
    "url": "https://techcrunch.com/2026/09/20/elon-musks-latest-boring-company-pitch-involves-a-hyperloop-between-austin-and-san-antonio/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T19:38:48+00:00",
    "summary": "Many of The Boring Company's announced projects have not materialized."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/20/is-the-ai-industry-really-ready-to-slow-down/",
    "domain": "大厂 AI 动态",
    "title": "Is the AI industry really ready to slow down?",
    "url": "https://techcrunch.com/2026/09/20/is-the-ai-industry-really-ready-to-slow-down/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T18:56:04+00:00",
    "summary": "On Equity, we debated whether AI executives are serious about wanting to slow down."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/20/voccis-ring-adds-a-new-form-factor-to-meeting-note-taking/",
    "domain": "大厂 AI 动态",
    "title": "Vocci’s ring adds a new form factor to meeting note-taking",
    "url": "https://techcrunch.com/2026/09/20/voccis-ring-adds-a-new-form-factor-to-meeting-note-taking/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T18:32:52+00:00",
    "summary": "Vocci's lightweight ring costs $249, and might pose some privacy questions."
  },
  {
    "id": "rss:https://stratechery.com/2026/frontier-overhangs/",
    "domain": "大厂 AI 动态",
    "title": "Frontier Overhangs",
    "url": "https://stratechery.com/2026/frontier-overhangs/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T10:00:00+00:00",
    "summary": "Pacing the frontier may be sincere, but it would also be strategically useful for the frontier labs to have time to reduce overhangs caused by model advancement."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/09/muse-metas-extraordinarily-privileged-ai-assistant-has-a-serious-0-day/",
    "domain": "大厂 AI 动态",
    "title": "Muse, Meta's extraordinarily privileged AI assistant, has a serious 0-day",
    "url": "https://arstechnica.com/security/2026/09/muse-metas-extraordinarily-privileged-ai-assistant-has-a-serious-0-day/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T22:24:38+00:00",
    "summary": "A simple ClickFix attack is only one way to completely hijack the new agent."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/09/military-milestone-ukrainian-naval-drone-sinks-russian-kamikaze-drone-boat/",
    "domain": "大厂 AI 动态",
    "title": "Military milestone: Ukrainian naval drone sinks Russian kamikaze drone boat",
    "url": "https://arstechnica.com/gadgets/2026/09/military-milestone-ukrainian-naval-drone-sinks-russian-kamikaze-drone-boat/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T21:07:05+00:00",
    "summary": "Drone boat battle occurs as Ukraine and Russia target Black Sea ports and ships."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/09/saudi-arabia-wants-a-car-industry-launches-ceer-with-two-evs/",
    "domain": "大厂 AI 动态",
    "title": "Saudi Arabia wants a car industry, launches Ceer with two EVs",
    "url": "https://arstechnica.com/cars/2026/09/saudi-arabia-wants-a-car-industry-launches-ceer-with-two-evs/",
    "source": "Chad Kirchner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T20:55:36+00:00",
    "summary": "The new carmaker is a joint venture between the Saudi PIF and Foxconn."
  },
  {
    "id": "hn:49691343",
    "domain": "股票",
    "title": "Nike exits the S&P 100 after 18 years and a $200B market-cap wipeout",
    "url": "https://fortune.com/2026/09/08/nike-stock-plummets-sp500-market-cap-index/",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 315,
    "published_at": "2026-09-14T02:50:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49619848",
    "domain": "股票",
    "title": "Apple iPod Engraver (2019)",
    "url": "https://dunstanorchard.com/apple-ipod-engraver/",
    "source": "NaOH",
    "platform": "hackernews",
    "points": 288,
    "published_at": "2026-09-09T01:57:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49712746",
    "domain": "股票",
    "title": "Global bond yields hit 2008 highs, raising stakes for big borrowers",
    "url": "https://www.reuters.com/world/asia-pacific/bond-selloff-drives-us-benchmark-beyond-5-stocks-rattled-2026-09-15/",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 167,
    "published_at": "2026-09-15T14:07:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611240",
    "domain": "股票",
    "title": "iPod Classic 6G in QEMU",
    "url": "https://www.reddit.com/r/emulation/s/VL4Au2HGxq",
    "source": "dmonterocrespo",
    "platform": "hackernews",
    "points": 161,
    "published_at": "2026-09-08T14:54:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49791944",
    "domain": "股票",
    "title": "Wall Street is growing skeptical of the data center boom",
    "url": "https://www.nytimes.com/2026/09/21/business/ai-data-center-ipos.html",
    "source": "mikhael",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-09-21T19:14:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49796292",
    "domain": "股票",
    "title": "Smart Ring Maker Oura, Backers Seek $2.2B in US IPO",
    "url": "https://www.bloomberg.com/news/articles/2026-09-21/smart-ring-maker-oura-backers-seek-2-2-billion-in-us-ipo",
    "source": "elo2000",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-09-22T02:53:48+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/brookfield-of-dreams",
    "domain": "股票",
    "title": "Brookfield of Dreams",
    "url": "https://www.netinterest.co/p/brookfield-of-dreams",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T15:05:47+00:00",
    "summary": "Inside Brookfield&#8217;s Plan to Double Again"
  },
  {
    "id": "hn:49696420",
    "domain": "股票",
    "title": "Global AI stocks fall as industry chiefs call for slowing development",
    "url": "https://www.reuters.com/world/china/ai-linked-asian-stocks-slump-after-top-lab-ceos-call-slowing-down-technologys-2026-09-14/",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-09-14T13:21:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49682946",
    "domain": "股票",
    "title": "Show HN: Analyst Index – analysts who make money telling you good stock calls",
    "url": "https://www.analystidx.com/",
    "source": "haichuan",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-13T11:50:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49672197",
    "domain": "股票",
    "title": "Larry Ellison to sell up to $7.5B worth of Oracle stock",
    "url": "https://www.ft.com/content/25b1abb0-790f-4315-9b0c-530d959a086f",
    "source": "potatobox",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-12T13:37:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49594296",
    "domain": "股票",
    "title": "OpenAI 2025 financials $38.5B loss ahead of IPO",
    "url": "https://qz.com/openai-leaked-financials-losses-revenue-ipo-061626",
    "source": "u1hcw9nx",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-09-07T05:41:13+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-five-deals-that-made-apollo",
    "domain": "股票",
    "title": "The Five Deals That Made Apollo",
    "url": "https://www.netinterest.co/p/the-five-deals-that-made-apollo",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T15:25:40+00:00",
    "summary": "From distressed debt to a trillion-dollar machine"
  },
  {
    "id": "hn:49451482",
    "domain": "股票",
    "title": "Hackers Broke into Justice Department, NASA, Federal Reserve, Senate",
    "url": "https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-platforms-operated-and-used-china-state-sponsored-hackers",
    "source": "2OEH8eoCRo0",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-26T16:05:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49450370",
    "domain": "股票",
    "title": "Chinese Hackers Broke into Justice Department, NASA, Federal Reserve, Senate",
    "url": "https://www.reuters.com/world/china/china-sponsored-hacking-platforms-seized-by-us-justice-department-says-2026-08-26/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-26T14:59:43+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/hot-european-summer",
    "domain": "股票",
    "title": "Hot European Summer",
    "url": "https://www.netinterest.co/p/hot-european-summer",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T16:33:06+00:00",
    "summary": "Europe is outperforming &#8211; but Europeans aren&#8217;t participating"
  },
  {
    "id": "rss:https://www.netinterest.co/p/untangling-guggenheim",
    "domain": "股票",
    "title": "Untangling Guggenheim",
    "url": "https://www.netinterest.co/p/untangling-guggenheim",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T15:05:53+00:00",
    "summary": "How Private Credit Built Its Own Universe"
  },
  {
    "id": "rss:https://www.netinterest.co/p/great-scott",
    "domain": "股票",
    "title": "Great Scott",
    "url": "https://www.netinterest.co/p/great-scott",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T17:35:18+00:00",
    "summary": "Challenges Facing the Bond Trader in Chief"
  },
  {
    "id": "rss:https://www.netinterest.co/p/financing-the-ai-boom-3",
    "domain": "股票",
    "title": "Financing the AI Boom 3",
    "url": "https://www.netinterest.co/p/financing-the-ai-boom-3",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T16:46:59+00:00",
    "summary": "Nvidia, Guarantor of Last Resort"
  },
  {
    "id": "rss:https://www.netinterest.co/p/leopolds-fall",
    "domain": "股票",
    "title": "Leopold’s Fall",
    "url": "https://www.netinterest.co/p/leopolds-fall",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T10:05:15+00:00",
    "summary": "Situational Awareness and Amaranth 20 Years Apart"
  },
  {
    "id": "rss:https://www.netinterest.co/p/paypal-declined",
    "domain": "股票",
    "title": "PayPal, Declined",
    "url": "https://www.netinterest.co/p/paypal-declined",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T16:33:10+00:00",
    "summary": "Inside the Bid for an Iconic Fintech"
  },
  {
    "id": "rss:https://www.netinterest.co/p/too-big-to-succeed",
    "domain": "股票",
    "title": "Too Big to Succeed",
    "url": "https://www.netinterest.co/p/too-big-to-succeed",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T15:22:26+00:00",
    "summary": "What it takes to run JPMorgan, and to hand it over"
  },
  {
    "id": "rss:https://www.netinterest.co/p/options-for-everyone",
    "domain": "股票",
    "title": "Options for Everyone",
    "url": "https://www.netinterest.co/p/options-for-everyone",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T15:06:18+00:00",
    "summary": "How the National Stock Exchange of India built the world&#8217;s busiest equity derivatives market"
  },
  {
    "id": "rss:https://www.netinterest.co/p/stretch-marks",
    "domain": "股票",
    "title": "Stretch Marks",
    "url": "https://www.netinterest.co/p/stretch-marks",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T16:38:39+00:00",
    "summary": "A Case Study in Financial Engineering"
  },
  {
    "id": "rss:https://www.netinterest.co/p/duffys-last-dance",
    "domain": "股票",
    "title": "Duffy’s Last Dance",
    "url": "https://www.netinterest.co/p/duffys-last-dance",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T16:40:29+00:00",
    "summary": "The Battle Over Futures That Never Expire"
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-transfer-market",
    "domain": "股票",
    "title": "The Transfer Market",
    "url": "https://www.netinterest.co/p/the-transfer-market",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T15:27:46+00:00",
    "summary": "Wise and the Business of Moving Money"
  },
  {
    "id": "rss:https://www.netinterest.co/p/jules-rimet-still-gleaming",
    "domain": "股票",
    "title": "Jules Rimet Still Gleaming",
    "url": "https://www.netinterest.co/p/jules-rimet-still-gleaming",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T16:13:59+00:00",
    "summary": "The World Cup Comes to Prediction Markets"
  },
  {
    "id": "rss:https://www.netinterest.co/p/when-the-ducks-are-quacking",
    "domain": "股票",
    "title": "When the Ducks are Quacking",
    "url": "https://www.netinterest.co/p/when-the-ducks-are-quacking",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-05T15:35:26+00:00",
    "summary": "SpaceX, Anthropic, OpenAI and the Business of IPOs"
  },
  {
    "id": "rss:https://www.netinterest.co/p/strategy-follows-structure",
    "domain": "股票",
    "title": "Strategy Follows Structure",
    "url": "https://www.netinterest.co/p/strategy-follows-structure",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-29T16:47:05+00:00",
    "summary": "Fidelity, Capital, Vanguard and the Ownership Structures That Made Them"
  },
  {
    "id": "rss:https://www.netinterest.co/p/griffins-doors",
    "domain": "股票",
    "title": "Griffin’s Doors",
    "url": "https://www.netinterest.co/p/griffins-doors",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-22T16:22:17+00:00",
    "summary": "Inside Citadel&#8217;s Talent Machine"
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-future-of-ir",
    "domain": "股票",
    "title": "The Future of IR",
    "url": "https://www.netinterest.co/p/the-future-of-ir",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-15T15:38:49+00:00",
    "summary": "What the Changing Shape of Markets Means for Investor Relations"
  },
  {
    "id": "rss:https://www.netinterest.co/p/bye-the-index",
    "domain": "股票",
    "title": "Bye the Index",
    "url": "https://www.netinterest.co/p/bye-the-index",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-08T16:07:09+00:00",
    "summary": "How Nasdaq learned to run its flywheel in reverse"
  },
  {
    "id": "rss:https://www.netinterest.co/p/money-for-nothing",
    "domain": "股票",
    "title": "Money for Nothing",
    "url": "https://www.netinterest.co/p/money-for-nothing",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-05-01T16:28:45+00:00",
    "summary": "The Golden Age of Arbitrage?"
  },
  {
    "id": "hn:49778029",
    "domain": "金融",
    "title": "Samsung is expected to more than double output of its HBM4 and HBM4E DRAM",
    "url": "https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 549,
    "published_at": "2026-09-20T17:38:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49686766",
    "domain": "金融",
    "title": "I'm being cyberattacked by Tesla, Inc",
    "url": "https://dreamstation.systems/personal/tesla.html",
    "source": "robinpie",
    "platform": "hackernews",
    "points": 458,
    "published_at": "2026-09-13T18:03:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:49594251",
    "domain": "金融",
    "title": "Switzerland's Federal Government Is Replacing Microsoft on 3k Computers",
    "url": "https://itsfoss.com/news/switzerland-replace-microssoft-pilot/",
    "source": "ivell",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-09-07T05:33:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49704008",
    "domain": "金融",
    "title": "Amazon vs. Perplexity – U.S. Court of Appeals for the Ninth Circuit",
    "url": "https://law.justia.com/cases/federal/appellate-courts/ca9/26-1444/26-1444-2026-08-04.html",
    "source": "neom",
    "platform": "hackernews",
    "points": 218,
    "published_at": "2026-09-14T21:05:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49731356",
    "domain": "金融",
    "title": "Fed hikes rates as inflation worries push up bond yields",
    "url": "https://www.reuters.com/live/live-fed-rate-hike-expected-inflation-worries-push-up-bond-yields-2026-09-16/",
    "source": "wslh",
    "platform": "hackernews",
    "points": 183,
    "published_at": "2026-09-16T18:55:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49600997",
    "domain": "金融",
    "title": "No constitutional right to clean water, federal court finds",
    "url": "https://www.usatoday.com/story/news/nation/2026/09/07/court-constitution-right-clean-water/91649488007/",
    "source": "measurablefunc",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-09-07T17:52:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49694840",
    "domain": "金融",
    "title": "How Much Has Trump Made from Crypto? ($1.4B from 2025 Federal Disclosure)",
    "url": "https://www.thepricer.org/how-much-has-trump-made-from-crypto/",
    "source": "cinderelacinder",
    "platform": "hackernews",
    "points": 114,
    "published_at": "2026-09-14T10:56:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49591672",
    "domain": "金融",
    "title": "Hackers have withdrawn ~4k BTC (~$320M) from the Liquid Federation wallet",
    "url": "https://twitter.com/Liquid_BTC/status/2096696272447218108",
    "source": "felipelalli",
    "platform": "hackernews",
    "points": 126,
    "published_at": "2026-09-06T22:43:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596610",
    "domain": "金融",
    "title": "Initial effects of AI technology on employment look positive",
    "url": "https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here",
    "source": "MrBuddyCasino",
    "platform": "hackernews",
    "points": 103,
    "published_at": "2026-09-07T10:38:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49700413",
    "domain": "金融",
    "title": "US 10-Year Breaches 5% as Inflation, Supply Worries Mount",
    "url": "https://www.bloomberg.com/news/articles/2026-09-14/us-10-year-yield-breaches-5-as-inflation-supply-worries-mount",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-09-14T17:11:59+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.22202",
    "domain": "金融",
    "title": "An Operator-Based Visual Analytics Pipeline for Synthetic Systemic Risk Dynamics",
    "url": "https://arxiv.org/abs/2609.22202",
    "source": "Ana Isabel Castillo Pereda",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.22202v1 Announce Type: new Abstract: This work presents an operator-based visual analytics pipeline for exploring synthetic systemic risk dynamics in financial networks. The framework is fo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.22446",
    "domain": "金融",
    "title": "Biased Agents, Extreme Beliefs: Motivated Reasoning Under Competing Models",
    "url": "https://arxiv.org/abs/2609.22446",
    "source": "Zhongheng Qiao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.22446v1 Announce Type: new Abstract: People often face environments where multiple models compete to explain the same observations. This paper examines how people update beliefs in such set"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.22652",
    "domain": "金融",
    "title": "Pareto-Improving Pricing: Why 3 Is Better Than 2",
    "url": "https://arxiv.org/abs/2609.22652",
    "source": "Zi Yang Kang, Piotr Dworczak",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.22652v1 Announce Type: new Abstract: We study the design of priority pricing systems with heterogeneous agents in environments in which improving quality for some agents reduces the average"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.22893",
    "domain": "金融",
    "title": "Universal Diffusion Models for Implied Volatility Surfaces: Learning Shared Dynamics Across Stocks",
    "url": "https://arxiv.org/abs/2609.22893",
    "source": "Mingzhi Yang, Sheng Wang, Chao Zhang, Ruikun Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.22893v1 Announce Type: new Abstract: Modeling the dynamics of option implied volatility surface (IVS) is crucial for pricing, hedging, and risk-managing option portfolios. We develop a univ"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.23223",
    "domain": "金融",
    "title": "Stealing profits: Spread-based temporal hierarchy forecasting for day-ahead electricity markets",
    "url": "https://arxiv.org/abs/2609.23223",
    "source": "Arkadiusz Lipiecki, Nikolaos Kourentzes, Rafal Weron",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.23223v1 Announce Type: new Abstract: Day-ahead electricity price forecasts support trading and storage decisions, but for battery arbitrage predicting intraday price spreads is more relevan"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.23571",
    "domain": "金融",
    "title": "Extremal Mean-Variance Functionals over Wasserstein Balls: Applications to Risk Sharing",
    "url": "https://arxiv.org/abs/2609.23571",
    "source": "Wenjun Jiang, Yiying Zhang, Zhenfeng Zou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.23571v1 Announce Type: new Abstract: We characterize the worst- and best-case values of a mean-variance functional over a 2-Wasserstein ball. Using quantile representations and the geometry"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.23598",
    "domain": "金融",
    "title": "OrderFusion+: Probabilistic Buy--Sell Price Trajectory Forecasting in Intraday Electricity Markets",
    "url": "https://arxiv.org/abs/2609.23598",
    "source": "Runyao Yu, Derek W. Bunn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.23598v1 Announce Type: new Abstract: Intraday electricity markets enable participants to adjust energy positions close to delivery, with price forecasts necessary to support trading and the"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.23744",
    "domain": "金融",
    "title": "Structural versus Allocative Inefficiency Across Organizational Settings",
    "url": "https://arxiv.org/abs/2609.23744",
    "source": "Jan van de Poll",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.23744v1 Announce Type: new Abstract: Organizations invest heavily in internal mechanisms such as incentive systems, governance structures, performance measurement, analytics, and repeated r"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.23768",
    "domain": "金融",
    "title": "Risk Measures under Paired-Ambiguity: A Deep Learning Reflected BSDE Framework",
    "url": "https://arxiv.org/abs/2609.23768",
    "source": "Nacira Agram, Jan Rems, Emanuela Rosazza Gianin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.23768v1 Announce Type: new Abstract: We study optimal stopping under dynamic risk measures with simultaneous ambiguity in the probability model and the discount rate. We introduce a paired "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.23969",
    "domain": "金融",
    "title": "Prediction Markets Beat the Weather Forecast on Tomorrow's High Temperature",
    "url": "https://arxiv.org/abs/2609.23969",
    "source": "Alexander W. Crosier",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.23969v1 Announce Type: new Abstract: The sooner we receive information, and the more accurate it is, the better planning decisions we can make. Every day, prediction markets let anyone bet "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.24181",
    "domain": "金融",
    "title": "Firm Valuation When AI Shapes the Business Model: A Milestone-Based Real-Options Framework for the AI Valuation Uncertainty Problem",
    "url": "https://arxiv.org/abs/2609.24181",
    "source": "Walter Kurz, Wojtek Stricker, Stefan Marx, Frank Reinhardt, Florian Kollberg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.24181v1 Announce Type: new Abstract: Standard valuation methods, including discounted cash flow, the income approach standard IDW S 1 of the Institute of Public Auditors in Germany, and mar"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.21439",
    "domain": "金融",
    "title": "People escalate against a competitor labelled human and hold back against one labelled an optimising machine",
    "url": "https://arxiv.org/abs/2609.21439",
    "source": "Vinicius Ferraz, Leon Houf",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.21439v1 Announce Type: cross Abstract: People increasingly compete against AI agents rather than other human opponents. We distinguish two channels: an opponent effect and an information ef"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.22169",
    "domain": "金融",
    "title": "Monocultural Biases: Correlated biases in large language models lead to unequal systemic exclusion rates in hiring",
    "url": "https://arxiv.org/abs/2609.22169",
    "source": "Matthew Bone, Fabian Stephany, Maria del Rio-Chanona",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.22169v1 Announce Type: cross Abstract: Employers are increasingly using large language models (LLMs) to automate their hiring process. This paper investigates the risk of monocultural biase"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.22408",
    "domain": "金融",
    "title": "Social Influence and the Allocation of Scientific Attention in AI Populations",
    "url": "https://arxiv.org/abs/2609.22408",
    "source": "Maxim Chupilkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.22408v1 Announce Type: cross Abstract: AI systems are becoming participants in the evaluation and use of scientific research. They encounter citation counts, download statistics and lists o"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.22612",
    "domain": "金融",
    "title": "Asymptotic Invariance of Kelly Allocation Under Power-Law Asset Dynamics: Evidence from Bitcoin",
    "url": "https://arxiv.org/abs/2609.22612",
    "source": "Ivan J. Vera-Marun",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.22612v1 Announce Type: cross Abstract: We examine log-optimal portfolio allocation when the long-run price of an asset follows a power-law trajectory, $P(t)=At^\\alpha$, and its instantaneou"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.22639",
    "domain": "金融",
    "title": "Adapting Pairs Trading to Gambling Markets A Case Study of the U.S. Presidential Election",
    "url": "https://arxiv.org/abs/2609.22639",
    "source": "Haoyu Liu, Len Thomas, Benjamin Baer, Carl Donovan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.22639v1 Announce Type: cross Abstract: Pairs trading exploits mean reversion in the relationship between related assets. We adapt this idea to political betting markets by modelling the com"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.23272",
    "domain": "金融",
    "title": "On Control of Drawdown: Robust Invariance and Optimality",
    "url": "https://arxiv.org/abs/2609.23272",
    "source": "Chung-Han Hsieh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.23272v1 Announce Type: cross Abstract: Mitigating \\emph{drawdown}, the decline in wealth from its running peak, presents a canonical problem in path-dependent risk control. In this paper, w"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.23378",
    "domain": "金融",
    "title": "Leaky-integrator reconstruction: taming error accumulation in recursive differenced time-series forecasting",
    "url": "https://arxiv.org/abs/2609.23378",
    "source": "Zijiang Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.23378v1 Announce Type: cross Abstract: We introduce leaky-integrator reconstruction, a training-free method that cures the error accumulation of recursive differenced forecasting. Our first"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.23703",
    "domain": "金融",
    "title": "Financial Language Models as Applied Artificial Intelligence Systems for News-Based Trading under Market Frictions",
    "url": "https://arxiv.org/abs/2609.23703",
    "source": "Kemal Kirtac",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.23703v1 Announce Type: cross Abstract: Financial language models can transform unstructured firm-specific news into structured decision signals, but financial AI research lacks an integrate"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.24548",
    "domain": "金融",
    "title": "Affine Volterra covariance processes and application to commodity markets",
    "url": "https://arxiv.org/abs/2609.24548",
    "source": "Boris G\\\"unther, Ludger Overbeck",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2609.24548v1 Announce Type: cross Abstract: We study affine stochastic Volterra equations on the cone of symmetric positive semidefinite matrices. For scalar kernels acting entrywise on the matr"
  },
  {
    "id": "rss:https://arxiv.org/abs/1801.03680",
    "domain": "金融",
    "title": "The time interpretation of expected utility theory",
    "url": "https://arxiv.org/abs/1801.03680",
    "source": "Ole Peters, Alexander Adamou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:1801.03680v3 Announce Type: replace Abstract: Ergodicity economics is a new branch of economic theory that notes the conceptual difference between time averages and expectation values, which coi"
  },
  {
    "id": "rss:https://arxiv.org/abs/1808.03481",
    "domain": "金融",
    "title": "Concave Shape of the Yield Curve and No Arbitrage",
    "url": "https://arxiv.org/abs/1808.03481",
    "source": "Jian Sun",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:1808.03481v2 Announce Type: replace Abstract: In fixed income sector, the yield curve is probably the most observed indicator by the market for trading and fifinancing purposes. A yield curve pl"
  },
  {
    "id": "rss:https://arxiv.org/abs/2110.09169",
    "domain": "金融",
    "title": "Prosecutor Politics: The Impact of Election Cycles on Criminal Sentencing in the Era of Rising Incarceration",
    "url": "https://arxiv.org/abs/2110.09169",
    "source": "Chika O. Okafor",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2110.09169v2 Announce Type: replace Abstract: Exploiting variation in the timing of district attorney elections across nearly 40 states during the steepest rise in U.S. incarceration (roughly 19"
  },
  {
    "id": "rss:https://arxiv.org/abs/2407.20931",
    "domain": "金融",
    "title": "Nonparametric Estimation of Matching Efficiency and Mismatch: An Application to Japanese Labor Markets",
    "url": "https://arxiv.org/abs/2407.20931",
    "source": "Suguru Otani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2407.20931v5 Announce Type: replace Abstract: I identify significant biases in the traditional Cobb-Douglas function under misspecification of nonadditive, time-varying matching efficiency, and "
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.25487",
    "domain": "金融",
    "title": "Monetary Regimes and Trade before the Classical Gold Standard: Evidence from the Latin Monetary Union",
    "url": "https://arxiv.org/abs/2510.25487",
    "source": "Jacopo Timini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2510.25487v4 Announce Type: replace Abstract: This paper reexamines the trade effects of the Latin Monetary Union (LMU), a 19th century agreement to standardize gold and silver coinage among sev"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.07886",
    "domain": "金融",
    "title": "The Endogenous Constraint: Hysteresis, Stagflation, and the Structural Inhibition of Monetary Velocity in the Bitcoin Network (2016-2025)",
    "url": "https://arxiv.org/abs/2512.07886",
    "source": "Hamoon Soleimani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2512.07886v2 Announce Type: replace Abstract: Bitcoin operates as a macroeconomic paradox: it combines a strictly predetermined, inelastic monetary issuance schedule with a stochastic, highly el"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.14662",
    "domain": "金融",
    "title": "Fixed-Income Pricing and the Replication of Liabilities",
    "url": "https://arxiv.org/abs/2512.14662",
    "source": "Damir Filipovi\\'c",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2512.14662v3 Announce Type: replace Abstract: This paper develops a model-free framework for static fixed-income pricing and the replication of liability cash flows. The absence of static arbitr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.10375",
    "domain": "金融",
    "title": "Dynamic reinsurance via martingale transport",
    "url": "https://arxiv.org/abs/2601.10375",
    "source": "Beatrice Acciaio, Brandon Garcia Flores, Antonio Marini, Gudmund Pammer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2601.10375v2 Announce Type: replace Abstract: We formulate a dynamic reinsurance problem in which the insurer seeks to satisfy prescribed terminal moment or risk-based constraints while minimizi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.12414",
    "domain": "金融",
    "title": "When Is the Gini Loading More Prudent? Tail Structure and the Ordering of the Standard Deviation and the Gini Mean Difference",
    "url": "https://arxiv.org/abs/2601.12414",
    "source": "Nawaf Mohammed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2601.12414v3 Announce Type: replace Abstract: The standard deviation (SD) and the Gini mean difference (GMD) are the two canonical measures of variability used to load premiums, set risk margins"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.13812",
    "domain": "金融",
    "title": "CFOs Meet LLMs",
    "url": "https://arxiv.org/abs/2606.13812",
    "source": "John R. Graham, Campbell R. Harvey, Manish Jha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T04:00:00+00:00",
    "summary": "arXiv:2606.13812v2 Announce Type: replace Abstract: Business sentiment is a closely watched economic signal, but measuring it is slow and costly: surveys typically reach only a few hundred firms, arri"
  },
  {
    "id": "hn:49626052",
    "domain": "金融",
    "title": "One woman's Tesla was remotely controlled by an abusive ex-partner",
    "url": "https://www.theguardian.com/australia-news/2026/sep/09/how-one-womans-tesla-was-remotely-controlled-and-harass-by-her-abusive-ex-partner-ntwnfb",
    "source": "gradschool",
    "platform": "hackernews",
    "points": 75,
    "published_at": "2026-09-09T13:16:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49762617",
    "domain": "金融",
    "title": "Elon Musk and Tesla Forged a New EV Path",
    "url": "https://spectrum.ieee.org/elon-musk-tesla",
    "source": "vinhnx",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-09-19T02:08:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49730769",
    "domain": "金融",
    "title": "Feds Want California to Give Up 14 Years of Broadband Protections. It Should Sue",
    "url": "https://cyberlaw.stanford.edu/blog/2026/09/california-is-being-asked-to-give-up-14-years-of-broadband-protections-it-doesnt-have-to/",
    "source": "rsingel",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-09-16T18:09:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:49612981",
    "domain": "金融",
    "title": "DOJ Blocked ICE Agent Shooting Charge over Federal Prosecutor's Objections",
    "url": "https://www.propublica.org/article/doj-blocks-charges-ice-agent-minneapolis-julio-cesar-sosa-celis",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-09-08T16:54:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49439296",
    "domain": "金融",
    "title": "A brief history of federal lift ticket regulation",
    "url": "https://zakpodmore.substack.com/p/a-brief-history-of-federal-lift-ticket",
    "source": "CGMthrowaway",
    "platform": "hackernews",
    "points": 69,
    "published_at": "2026-08-25T19:25:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49731515",
    "domain": "金融",
    "title": "Fed Raises Rates for First Time in Three Years",
    "url": "https://www.wsj.com/economy/central-banking/fed-raises-rates-for-first-time-in-three-years-08539fbe",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-09-16T19:09:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49625461",
    "domain": "金融",
    "title": "Teen reading slumps to worst this century due to surge in screen time",
    "url": "https://finance.yahoo.com/news/teen-reading-slumps-worst-century-111013754.html",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-09-09T12:29:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49730731",
    "domain": "金融",
    "title": "Fed Raises Rates as Warsh Bucks Trump to Contain Inflation",
    "url": "https://www.bloomberg.com/news/articles/2026-09-16/fed-raises-rates-as-warsh-bucks-trump-to-contain-inflation",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-09-16T18:05:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49633640",
    "domain": "金融",
    "title": "DHS Program Analyzes Americans' Finances to Flag Drivers for Traffic Stops",
    "url": "https://www.military.com/dhs-program-analyzes-americans-finances-to-flag-drivers-for-traffic-stops-report",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-09-09T20:22:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:49432102",
    "domain": "金融",
    "title": "Nostr vs. Fediverse vs. Bluesky: A Comparison of Decentralized Social Protocols",
    "url": "https://soapbox.pub/blog/comparing-protocols",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-08-25T11:27:51+00:00",
    "summary": ""
  }
]
```
