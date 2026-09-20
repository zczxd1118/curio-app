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

- 今日日期：`2026-09-20`
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
  "date": "2026-09-20",
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
    "id": "bvid:BV1rv4y167uC",
    "domain": "AI",
    "title": "【WorkBuddy保姆级教程】入门Agent或是工作提效，听完秒变大神！43节付费课内容全公开，完整工作流+实战技巧全揭秘，零基础一小时从入门到精通！（附资料",
    "url": "http://www.bilibili.com/video/av566052791",
    "source": "WorkBuddy课堂",
    "platform": "bilibili",
    "points": 6036538,
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
    "points": 5825491,
    "published_at": "2025-10-01T05:12:41+00:00",
    "summary": "置顶评论领取学习资料哦~"
  },
  {
    "id": "bvid:BV1yjz5BLEoY",
    "domain": "AI",
    "title": "黑马程序员大模型RAG与Agent智能体项目实战教程，基于主流的LangChain技术从大模型提示词到实战项目",
    "url": "http://www.bilibili.com/video/av115931552416097",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 3577771,
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
    "points": 2875548,
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
    "points": 1996453,
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
    "points": 1963360,
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
    "points": 1886229,
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
    "points": 1863035,
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
    "points": 1757919,
    "published_at": "2026-03-20T01:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260320\n2026黑马程序员AI智能应用开发学习路线图\nhttps://www.bilibili.com/opus/1156896913511940102\n如何下载资料\nhttps://www.bilibili.com/read/cv7881295/\n学习+球球群625260577，告别孤单，共同进步！\n\n【AI智能"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1312992,
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
    "points": 1248742,
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
    "points": 1186536,
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
    "points": 1092446,
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
    "points": 1075217,
    "published_at": "2025-11-28T10:20:16+00:00",
    "summary": "课程涵盖基础概念、算法原理、实践应用，从零开始，深入浅出。通过实例演示，掌握神经网络、决策树、支持向量机等关键技术。适合初学者和进阶者，助您快速提升技能，开启智能时代新篇章。立即观看，开启您的AI学习之旅！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 921007,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 888528,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1ABu96JEAR",
    "domain": "AI",
    "title": "【保姆级教程】WorkBuddy彻底玩明白！只看这一期就够了！10节付费课内容全公开，完整工作流+实战技巧全揭秘，零基础一小时从入门到精通【附完整资料】",
    "url": "http://www.bilibili.com/video/av117069685262348",
    "source": "workbuddy应用实战",
    "platform": "bilibili",
    "points": 796870,
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
    "points": 793065,
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
    "points": 685414,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1TSg7zuEqR",
    "domain": "AI",
    "title": "Agent 的概念、原理与构建模式 —— 从零打造一个简化版的 Claude Code",
    "url": "http://www.bilibili.com/video/av114894200380730",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 572172,
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
    "points": 442957,
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
    "points": 349135,
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
    "points": 348474,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1Zgud6LEoh",
    "domain": "AI",
    "title": "【最新版】小白速通 Codex 教程（含 DeepSeek 接入，无需 ChatGPT 订阅）",
    "url": "http://www.bilibili.com/video/av117070826047031",
    "source": "林粒粒呀",
    "platform": "bilibili",
    "points": 333937,
    "published_at": "2026-08-10T10:54:20+00:00",
    "summary": "Codex 安装 + 上手速通，保姆级教程！\n无需 ChatGPT 订阅，国内直连 DeepSeek"
  },
  {
    "id": "bvid:BV1t55v6DE2v",
    "domain": "AI",
    "title": "Agent和Harness到底是什么？一个动画彻底搞懂！",
    "url": "http://www.bilibili.com/video/av116577945062195",
    "source": "轩辕的编程宇宙",
    "platform": "bilibili",
    "points": 306546,
    "published_at": "2026-05-15T10:02:14+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 292972,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 289500,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1ssN16HEkq",
    "domain": "AI",
    "title": "【2026最新版】ChatGPT+Codex 零基础全套教程｜从入门到 AI 开发实战全流程",
    "url": "http://www.bilibili.com/video/av116911476115725",
    "source": "马士兵长沙中心",
    "platform": "bilibili",
    "points": 273827,
    "published_at": "2026-07-13T07:51:43+00:00",
    "summary": "2026 新版 OpenAI ChatGPT+Codex 完整实战课，零基础也能学，从基础指令到 AI 项目开发全流程教学，配套可落地实战案例，学完直接做简历项目。"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 264568,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1X8oKBLEdj",
    "domain": "AI",
    "title": "一口气学会AI编程！3个月10万字超详细教学！【项目实操】【0基础教学】【自学教程】【AI编程】【vibecoding】",
    "url": "http://www.bilibili.com/video/av116436177523067",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 225198,
    "published_at": "2026-04-21T03:15:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料，领取方式：关注后 私信“ 1 ”就好！\n\n后面还会出【一口气学会AI漫剧 】【一口气学会AI Agent 】等系列！大家可以蹲蹲！"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 206436,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 181725,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 181059,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1Cs7h6MEsX",
    "domain": "AI",
    "title": "Harness Engineering企业级多Agent协同项目实战！Multi-Agent+SandBox+自我进化的Skill+人工介入-码士集团AI大模型",
    "url": "http://www.bilibili.com/video/av116809856457232",
    "source": "马士兵官方账号",
    "platform": "bilibili",
    "points": 173331,
    "published_at": "2026-06-25T08:46:28+00:00",
    "summary": "本套系列视频将为你彻底揭开大模型前沿架构 —— Harness（驾驭工程） 的神秘面纱，带你从底层代码一步步构建一个真正能帮你拿到 20K-40K 高薪 Offer 的商业级项目！\n🛠️ 本期视频核心硬核技术栈\n本系列教程不谈空洞理论，全程带你一行行敲出 Harness 架构的八大核心能力：\nPlanning 任务规划能力：看智能体如何面对模糊的复杂任务，自主完成深度需求拆解与多子智能体委派。\nS"
  },
  {
    "id": "bvid:BV1YG7G6eEPR",
    "domain": "AI",
    "title": "【全60集】吊打付费！目前B站最全最细的Agent智能体开发全套教程！手把手教你打造专属智能体，七天就能从小白到大神！带你从零基础入门到精通实现商业变现！",
    "url": "http://www.bilibili.com/video/av116815090947614",
    "source": "AI-Agent开发",
    "platform": "bilibili",
    "points": 158257,
    "published_at": "2026-06-26T06:57:42+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 156972,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1VnEi6gELD",
    "domain": "AI",
    "title": "【B站强推】清华大佬终于把Agent教程做成动画片了，教学通俗易懂，2026最新版，学完即可就业！拿走不谢，别再走弯路了，学不会我退出IT界！Agent智能体",
    "url": "http://www.bilibili.com/video/av116729829131968",
    "source": "Agent产品经理",
    "platform": "bilibili",
    "points": 142706,
    "published_at": "2026-06-11T05:41:11+00:00",
    "summary": "【B站强推】清华大佬终于把Agent教程做成动画片了，教学通俗易懂，2026最新版，学完即可就业！拿走不谢，别再走弯路了，学不会我退出IT界！Agent智能体"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 120370,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 100258,
    "published_at": "2026-04-27T04:45:20+00:00",
    "summary": "很多人问我上期爆了的那条视频里，那个 PPT 是怎么做的。\n其实我是用 Anthropic 最近出的 Claude Design 做的，这个功能一发出来就在全网传疯了，一条推文就冲上了 6000 多万曝光。\n本期视频我会带你手把手从 0 到 1 把这个Skill 装好，然后一起跑一个成品效果出来。"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93748,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 74997,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1H1eH6DExE",
    "domain": "AI",
    "title": "零基础入门vibe coding！如何搭建自己的工作台？附指令模版",
    "url": "http://www.bilibili.com/video/av117275877184803",
    "source": "Iris学姐",
    "platform": "bilibili",
    "points": 64258,
    "published_at": "2026-09-16T10:00:00+00:00",
    "summary": "零基础如何入门vibe coding？手把手教你用豆包工作搭建你的专属AI工作台！全程不用写一行代码，零基础的同学也完全能跟上~"
  },
  {
    "id": "bvid:BV1aQMX6oEni",
    "domain": "AI",
    "title": "【Agent面经】目前B站最细的（AI Agent）高频面试八股文，吊打付费，帮你避开99%面试坑！存下吧，很难找全的！",
    "url": "http://www.bilibili.com/video/av117030678239428",
    "source": "Agent开发实战",
    "platform": "bilibili",
    "points": 61237,
    "published_at": "2026-08-03T08:50:19+00:00",
    "summary": "【Agent面试100问】目前B站最细的（AI Agent）高频面试八股文，吊打付费，帮你避开99%面试坑！存下吧，很难找全的！"
  },
  {
    "id": "bvid:BV1xYYL6rE1F",
    "domain": "AI",
    "title": "【最新GPT合并版Codex】2026最新Codex保姆级完整教程-Codex新手保姆级教程-最强AI助手！从入门到进阶，60分钟速通Codex！【附教程资料】",
    "url": "http://www.bilibili.com/video/av117251449556551",
    "source": "李宏毅agent",
    "platform": "bilibili",
    "points": 59647,
    "published_at": "2026-09-11T08:28:14+00:00",
    "summary": "Codex的能力越来越全面，变成了Codex四大形态里最强一个。 Codex APP 比起 Claude Code，额度更高，功能更全，免费账户也能用。而且不会出现限速、封号、降智等问题，用过的小伙伴直呼真香。本期视频带来一个Codex APP的完整教程"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 55257,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1oLtz6kED8",
    "domain": "AI",
    "title": "B站首推！清华大佬168小时讲完的WorkBuddy入门到精通全套教程，2026最新版，全程干货无废话，学完即可就业！",
    "url": "http://www.bilibili.com/video/av117211804995728",
    "source": "Python研究社",
    "platform": "bilibili",
    "points": 52233,
    "published_at": "2026-09-04T08:29:34+00:00",
    "summary": "教程持续更新~需要视频配套学习资料的小伙伴，三联后评论区留言获取~"
  },
  {
    "id": "bvid:BV1n9g36wEiZ",
    "domain": "AI",
    "title": "5分钟教会你，什么是agent？",
    "url": "http://www.bilibili.com/video/av117097082392253",
    "source": "开聊pro",
    "platform": "bilibili",
    "points": 51947,
    "published_at": "2026-08-15T02:12:34+00:00",
    "summary": "呵呵，多评论。"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 48302,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "7月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "harness使用教程-",
    "platform": "bilibili",
    "points": 48242,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "AI充值站：njzqhy.top"
  },
  {
    "id": "bvid:BV1ApYD6KEkD",
    "domain": "AI",
    "title": "马斯克收购Cursor后，Cursor的性价比现在已经爆表",
    "url": "http://www.bilibili.com/video/av117254955993228",
    "source": "jopatk",
    "platform": "bilibili",
    "points": 38030,
    "published_at": "2026-09-11T23:19:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49724881",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia announces native GPU programming in Rust",
    "url": "https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/",
    "source": "nonmaskable",
    "platform": "hackernews",
    "points": 965,
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
    "id": "hn:49682319",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia dismisses \"circular financing\", says every $1 it invests brings back $100",
    "url": "https://invezz.com/news/2026/09/11/nvidia-says-every-1-it-invests-brings-back-100-so-why-does-the-stock-keep-falling/",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 137,
    "published_at": "2026-09-13T10:29:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49714096",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC revealing details about next gen A14 node",
    "url": "https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331",
    "source": "osnium123",
    "platform": "hackernews",
    "points": 124,
    "published_at": "2026-09-15T15:31:55+00:00",
    "summary": ""
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
    "id": "rss:https://www.eetimes.com/ai-demand-will-keep-dram-market-under-pressure/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Demand Will Keep DRAM Market Under Pressure",
    "url": "https://www.eetimes.com/ai-demand-will-keep-dram-market-under-pressure/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T12:00:00+00:00",
    "summary": "AI infrastructure spending is driving DRAM shortages that will continue through 2027, pushing consumer electronics makers further down priority lists. The post AI Demand Will Keep DRAM Market Under Pr"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/acer-predator-qd-oled-monitor-now-36-percent-off-500-hz-refresh-rate-and-true-black-500-certification-slashed-to-usd509-99",
    "domain": "AI 算力 / 半导体",
    "title": "Acer Predator QD-OLED monitor now 36% off — 500 Hz refresh rate and True Black 500 certification slashed to $509.99",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/acer-predator-qd-oled-monitor-now-36-percent-off-500-hz-refresh-rate-and-true-black-500-certification-slashed-to-usd509-99",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T18:26:39+00:00",
    "summary": "Acer Predator X27U F5 QD-OLED monitor has 500 Hz refresh rate and True Black 500 certification for $509.99"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/chatgpt-6-astra-cracks-108-year-old-unsolved-wwi-german-code-for-the-first-time-radio-message-sharing-enemy-movement-intelligence-had-evaded-decoding-1918-crimean-fleet-warning-verified-against-hms-canterbury-logs",
    "domain": "AI 算力 / 半导体",
    "title": "ChatGPT-6 Astra cracks 108-year-old unsolved WWI German code for the first time — radio message sharing enemy movement intelligence had evaded decoding, 1918 Crimean fleet warning verified against HMS",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/chatgpt-6-astra-cracks-108-year-old-unsolved-wwi-german-code-for-the-first-time-radio-message-sharing-enemy-movement-intelligence-had-evaded-decoding-1918-crimean-fleet-warning-verified-against-hms-canterbury-logs",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T15:02:02+00:00",
    "summary": "108 years after it was originally transmitted, an encrypted World War I German radio message has apparently been deciphered for the first time."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/father-loses-job-over-9-year-old-spending-usd118-000-on-youtube-ads-using-his-companys-credit-card-refuses-to-set-up-gofundme-or-put-up-crypto-coin-to-help-repay-massive-bill",
    "domain": "AI 算力 / 半导体",
    "title": "Father loses job over 9-year-old spending $118,000 on Minecraft YouTube ads using his company's credit card — 'I’m going to be working until I’m like 94,' refuses to set up GoFundMe or put up crypto c",
    "url": "https://www.tomshardware.com/video-games/father-loses-job-over-9-year-old-spending-usd118-000-on-youtube-ads-using-his-companys-credit-card-refuses-to-set-up-gofundme-or-put-up-crypto-coin-to-help-repay-massive-bill",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T13:37:12+00:00",
    "summary": "Mighty Mike Play's dad is trying to figure out how to pay back the $118k his son accidentally spent on YouTube ads. He also warned against fundraisers made in their name, since they aren't making one "
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/acer-nitro-xv273u-f5-27-inch-qhd-540-hz-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Acer Nitro XV273U F5 gaming monitor review: One of the fastest LCDs on the planet",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/acer-nitro-xv273u-f5-27-inch-qhd-540-hz-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T13:00:00+00:00",
    "summary": "Acer’s Nitro XV273U F5 might be the fastest LCD on the planet. This 27-inch QHD IPS panel boasts 540 Hz and 1,000 Hz at HD resolution. It also delivers Adaptive-Sync, HDR10, HDR 600, and wide gamut co"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/researchers-create-dna-computer-that-performs-100-bit-calculations-without-electricity-molecular-system-uses-self-assembling-strands-to-perform-computing",
    "domain": "AI 算力 / 半导体",
    "title": "Researchers create DNA computer that performs 100-bit calculations without electricity — molecular system uses self-assembling strands to perform computing",
    "url": "https://www.tomshardware.com/tech-industry/researchers-create-dna-computer-that-performs-100-bit-calculations-without-electricity-molecular-system-uses-self-assembling-strands-to-perform-computing",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T12:30:00+00:00",
    "summary": "Maynooth University researchers built a scaffolded DNA computer that uses molecular reactions to perform arithmetic and 100-bit calculations without electrical power."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-september-19-2026-steam-frame-interview-killer-ai-models-and-the-dram-crisis-deepens",
    "domain": "AI 算力 / 半导体",
    "title": "This week on Tom's Hardware Premium: September 19, 2026 — Steam Frame interview, killer AI models, and the DRAM crisis deepens",
    "url": "https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-september-19-2026-steam-frame-interview-killer-ai-models-and-the-dram-crisis-deepens",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T12:00:00+00:00",
    "summary": "This week on Tom's Hardware Premium, we offer deep-dives into the Steam Frame, explore how AI is changing the landscape of consumer electrionics, and how advanced AI accelerators are reaching Eastern "
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/fully-custom-copper-pc-features-upcycled-blowtorch-reservoir-antique-wooden-pedestal-complements-steampunk-design-hiding-a-ryzen-7-9800x3d-rx-9070-xt",
    "domain": "AI 算力 / 半导体",
    "title": "Fully custom copper PC features upcycled blowtorch reservoir — antique wooden pedestal complements steampunk design hiding a Ryzen 7 9800X3D, RX 9070 XT",
    "url": "https://www.tomshardware.com/desktops/pc-building/fully-custom-copper-pc-features-upcycled-blowtorch-reservoir-antique-wooden-pedestal-complements-steampunk-design-hiding-a-ryzen-7-9800x3d-rx-9070-xt",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T11:30:00+00:00",
    "summary": "If Edison and Stephenson had teamed up to build a gaming PC, it might have looked like this custom copper and wood all-AMD design."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/elon-musks-terafab-hits-a-roadblock-before-making-a-single-chip-receives-cease-and-desist-order-firm-files-trademark-lawsuit-has-sold-tera-fab-branded-lithography-tools-for-over-a-decade",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk's Terafab hits a roadblock before making a single chip, receives cease-and-desist order — firm files trademark lawsuit, has sold Tera-Fab-branded lithography tools for over a decade",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/elon-musks-terafab-hits-a-roadblock-before-making-a-single-chip-receives-cease-and-desist-order-firm-files-trademark-lawsuit-has-sold-tera-fab-branded-lithography-tools-for-over-a-decade",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T11:00:00+00:00",
    "summary": "Elon Musk's Terafab semiconductor project has run into an unexpected trademark dispute with Tera-print, a small U.S. company that has used the Tera-Fab name for its tabletop lithography equipment for "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/intel-suspends-bug-bounty-program-that-paid-up-to-usd100-000-per-flaw-new-intigriti-disclosure-program-offers-no-rewards",
    "domain": "AI 算力 / 半导体",
    "title": "Intel suspends bug bounty program that paid up to $100,000 per flaw — new Intigriti disclosure program offers no rewards",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/intel-suspends-bug-bounty-program-that-paid-up-to-usd100-000-per-flaw-new-intigriti-disclosure-program-offers-no-rewards",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T10:30:00+00:00",
    "summary": "Intel’s bug bounty program on Intigriti now shows as suspended, and a new Intel disclosure program there pays no bounties."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/enthusiast-digs-into-cpu-substrate-to-replace-ripped-off-data-pin-resurrected-chip-boots-and-hits-33-percent-overclock",
    "domain": "AI 算力 / 半导体",
    "title": "Enthusiast digs into CPU substrate for surgery to replace ripped-off data pin — resurrected chip boots and hits 33% overclock",
    "url": "https://www.tomshardware.com/pc-components/cpus/enthusiast-digs-into-cpu-substrate-to-replace-ripped-off-data-pin-resurrected-chip-boots-and-hits-33-percent-overclock",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T10:00:00+00:00",
    "summary": "An Intel Celeron 1200 (Tualatin) was revived from the dead after a ripped-off pin was successfully replaced."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-shares-first-official-benchmarks-for-epyc-venice-cpus-targets-nvidia-company-claims-256-core-chip-is-more-than-twice-as-fast-as-nvidia-vera-96-core-model-20-percent-faster-per-core",
    "domain": "AI 算力 / 半导体",
    "title": "AMD targets Nvidia with first official benchmarks for EPYC 'Venice' CPUs — company claims 256-core chip is more than twice as fast as Nvidia Vera, 96-core model 20% faster per-core",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-shares-first-official-benchmarks-for-epyc-venice-cpus-targets-nvidia-company-claims-256-core-chip-is-more-than-twice-as-fast-as-nvidia-vera-96-core-model-20-percent-faster-per-core",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T21:51:29+00:00",
    "summary": "AMD has released several benchmarks for its EPYC 'Venice' CPUs in a clear shot at Nvidia."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/details-about-intels-next-gen-nova-lake-cpus-keep-leaking-an-attempt-to-establish-a-timeline-based-on-what-we-know-so-far",
    "domain": "AI 算力 / 半导体",
    "title": "Details about Intel's next-gen Nova Lake CPUs keep leaking — an attempt to establish a timeline based on what we know so far",
    "url": "https://www.tomshardware.com/pc-components/cpus/details-about-intels-next-gen-nova-lake-cpus-keep-leaking-an-attempt-to-establish-a-timeline-based-on-what-we-know-so-far",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T19:45:41+00:00",
    "summary": "Over the past two weeks, we've seen an uptick in leaks and rumors about Intel's upcoming Nova Lake CPUs. Here, we piece together what we've heard to try and establish a plausible release timeline."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/save-up-to-40-percent-on-elegoo-3d-printers-during-its-september-sale-from-just-usd159-elegoo-day-deals-mean-you-can-save-on-a-new-fdm-or-resin-printer-with-big-bulk-discounts-on-consumables",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to 40% on Elegoo 3D printers during its September sale, from just $159 — Elegoo Day deals mean you can save on a new FDM or resin printer, with big bulk discounts on consumables",
    "url": "https://www.tomshardware.com/3d-printing/save-up-to-40-percent-on-elegoo-3d-printers-during-its-september-sale-from-just-usd159-elegoo-day-deals-mean-you-can-save-on-a-new-fdm-or-resin-printer-with-big-bulk-discounts-on-consumables",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T15:45:00+00:00",
    "summary": "Get yourself a new 3D printer this September from Elegoo during its Elegoo Day sales, with up to 40% off right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/chinas-premiere-memory-maker-cxmt-eyes-producing-flash-for-ssds-report-claims-3d-nand-research-and-development-line-rumored-for-its-second-manufacturing-facility-near-beijing",
    "domain": "AI 算力 / 半导体",
    "title": "China's premier memory maker CXMT eyes producing flash for SSDs, report claims — 3D NAND research and development line rumored for its second manufacturing facility near Beijing",
    "url": "https://www.tomshardware.com/pc-components/ssds/chinas-premiere-memory-maker-cxmt-eyes-producing-flash-for-ssds-report-claims-3d-nand-research-and-development-line-rumored-for-its-second-manufacturing-facility-near-beijing",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T15:34:02+00:00",
    "summary": "China's DRAM champion CXMT is reportedly planning to enter 3D NAND production as it plots 3D NAND research programs and pilot line at its future fab near Beijing."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/house-passes-act-to-make-ai-data-centers-pay-for-grid-upgrades-to-minimize-impact-on-residents-measure-directs-states-to-consider-adoption-of-federal-standard-within-two-years-of-passing",
    "domain": "AI 算力 / 半导体",
    "title": "House passes act to make AI data centers pay for grid upgrades to minimize impact on residents — measure directs states to consider adoption of federal standard within two years of passing",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/house-passes-act-to-make-ai-data-centers-pay-for-grid-upgrades-to-minimize-impact-on-residents-measure-directs-states-to-consider-adoption-of-federal-standard-within-two-years-of-passing",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T15:20:43+00:00",
    "summary": "This Ratepayer Protection Act will make data centers pay for grid upgrades made in their name. However, it still has to go through the senate and the White House, before being considered by individual"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/nor-flash-and-slc-nand-production-are-under-threat-as-capacity-gets-routed-to-more-profitable-products-severe-undersupply-threatens-everyday-electronics",
    "domain": "AI 算力 / 半导体",
    "title": "NOR Flash and SLC NAND production are under threat as capacity gets routed to more profitable products — 'severe undersupply' threatens everyday electronics",
    "url": "https://www.tomshardware.com/pc-components/dram/nor-flash-and-slc-nand-production-are-under-threat-as-capacity-gets-routed-to-more-profitable-products-severe-undersupply-threatens-everyday-electronics",
    "source": "Chris Stokel-Walker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T14:38:22+00:00",
    "summary": "NOR Flash and SLC NAND are the latest products to be impacted by the ongoing AI buildout, with capacities tightening and production being routed to more lucrative chips."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/hackers-breach-openai-using-claude-tools-gaining-access-to-employee-accounts-and-the-companys-internal-codebase-initiating-a-harmless-pull-request-as-proof-of-the-hack",
    "domain": "AI 算力 / 半导体",
    "title": "Hackers breach OpenAI using Claude tools, gaining access to employee accounts and the company's internal codebase — attackers initiated a 'harmless' pull request as proof of the hack",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/hackers-breach-openai-using-claude-tools-gaining-access-to-employee-accounts-and-the-companys-internal-codebase-initiating-a-harmless-pull-request-as-proof-of-the-hack",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T13:45:00+00:00",
    "summary": "A team of white-hat hackers from cybersecurity startup Hackron AI has successfully hacked OpenAI using Claude tools."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-developer-vibe-codes-dlss-5-onto-intel-arc-140t-integrated-graphics-run-neural-rendering-in-360p-at-10-frames-per-second",
    "domain": "AI 算力 / 半导体",
    "title": "AI developer vibe codes DLSS 5 onto Intel CPU's integrated graphics — Intel Arc 140T runs neural rendering in 360p at 10 frames per second",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-developer-vibe-codes-dlss-5-onto-intel-arc-140t-integrated-graphics-run-neural-rendering-in-360p-at-10-frames-per-second",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T13:15:00+00:00",
    "summary": "Using AI tools, a new developer has managed to get DLSS 5 neural rendering running on Intel Lunar Lake's integrated Arc graphics, albeit with abysmal performance."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/control-resonant-pc-performance-tested-28-gpus-take-us-back-to-the-oldest-house-and-a-warped-manhattan-cityscape",
    "domain": "AI 算力 / 半导体",
    "title": "Control Resonant PC performance tested: 28 GPUs take us back to the Oldest House and a warped Manhattan cityscape",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/control-resonant-pc-performance-tested-28-gpus-take-us-back-to-the-oldest-house-and-a-warped-manhattan-cityscape",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T13:01:36+00:00",
    "summary": "Control Resonant's warped Manhattan cityscape pushes graphics cards to the max thanks to path-traced lighting effects and full support for Nvidia's DLSS 4.5 technologies. We put it to the test to see "
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/prusa-core-one-l-plus-review",
    "domain": "AI 算力 / 半导体",
    "title": "Prusa CORE One L+ review: More precise",
    "url": "https://www.tomshardware.com/3d-printing/prusa-core-one-l-plus-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T13:00:00+00:00",
    "summary": "Prusa Research makes its large CORE One a tiny bit better in a very important way."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-director-called-ai-scraping-the-largest-theft-of-labor-in-human-history-while-openai-head-brands-chatgpt-an-existential-threat-to-publishers-revelations-come-from-legal-briefs-filed-in-nyt-lawsuit",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft director called AI scraping ‘the largest theft of labor in human history,’ while OpenAI head brands ChatGPT an ‘existential threat’ to publishers — revelations come from legal briefs filed i",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-director-called-ai-scraping-the-largest-theft-of-labor-in-human-history-while-openai-head-brands-chatgpt-an-existential-threat-to-publishers-revelations-come-from-legal-briefs-filed-in-nyt-lawsuit",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T12:49:14+00:00",
    "summary": "The NYT filed a legal brief revealing potentially damaging statements from Microsoft and OpenAI regarding the copyright infringement case it brought against the two companies. The publication is now s"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/us-frontier-ai-companies-warn-authorities-over-sophisticated-distillation-attacks-china-warns-of-countermeasures-if-america-tries-to-constrain-domestic-ai-models",
    "domain": "AI 算力 / 半导体",
    "title": "US frontier AI companies warn authorities over sophisticated distillation attacks — China warns of 'countermeasures' if America tries to constrain domestic AI models",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/us-frontier-ai-companies-warn-authorities-over-sophisticated-distillation-attacks-china-warns-of-countermeasures-if-america-tries-to-constrain-domestic-ai-models",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T12:20:00+00:00",
    "summary": "U.S. AI companies and the government are increasingly concerned about the effectiveness of international competition using distillation attacks to glean valuable data from frontier models to train che"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/modder-gets-nvidias-dlss-5-working-in-a-web-browser-using-webgpu-147mb-browser-port-runs-on-non-nvidia-gpus-and-macos-but-takes-two-seconds-per-render",
    "domain": "AI 算力 / 半导体",
    "title": "Modder gets Nvidia's DLSS 5 working in a web browser using WebGPU — 147MB browser port runs on non-Nvidia GPUs and macOS but takes two seconds per render",
    "url": "https://www.tomshardware.com/pc-components/gpus/modder-gets-nvidias-dlss-5-working-in-a-web-browser-using-webgpu-147mb-browser-port-runs-on-non-nvidia-gpus-and-macos-but-takes-two-seconds-per-render",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T12:00:00+00:00",
    "summary": "A developer's live WebGPU demo runs Nvidia's DLSS 5 neural rendering in a web browser, but also apparently runs on macOS."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/us-chip-manufacturers-are-in-dire-need-of-engineers-and-technicians-experts-suggest-a-shortage-of-up-to-157-000-semiconductor-workers-by-2030",
    "domain": "AI 算力 / 半导体",
    "title": "US chip fabs face massive 157,000 worker shortfall, mere 3% of US engineering grads enter chipmaking — despite six-figure salaries, US chip manufacturers are in dire need of engineers and technicians",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/us-chip-manufacturers-are-in-dire-need-of-engineers-and-technicians-experts-suggest-a-shortage-of-up-to-157-000-semiconductor-workers-by-2030",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T11:30:00+00:00",
    "summary": "As many semiconductor fabs and facilities go online in the 2030s and beyond, a global consulting firm said that these sites will need thousands of engineers and technicians that the U.S. will be hard-"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/asml-snubs-elon-musk-backed-particle-accelerator-chipmaking-tech-firm-doubles-down-on-1-000w-laser-produced-plasma-systems-for-chipmaking-tools",
    "domain": "AI 算力 / 半导体",
    "title": "ASML snubs Elon Musk-backed particle accelerator chipmaking tech — firm doubles down on 1,000W laser-produced plasma systems for chipmaking tools",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-snubs-elon-musk-backed-particle-accelerator-chipmaking-tech-firm-doubles-down-on-1-000w-laser-produced-plasma-systems-for-chipmaking-tools",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T11:00:00+00:00",
    "summary": "With progress that ASML makes with its LPP EUV light sources for its scanners, the company is barely interesting in adopting particle accelerator-based FEL sources."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd300-on-this-4k-gaming-pc-with-a-9800x3d-and-rtx-5070-ti-now-usd2-599-powerhouse-abs-stratos-ii-rig-ships-with-32gb-ddr5-and-a-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save $300 on this 4K gaming PC with a 9800X3D and RTX 5070 Ti, now $2,599 — powerhouse ABS Stratos II rig ships with 32GB DDR5 and a 2TB SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd300-on-this-4k-gaming-pc-with-a-9800x3d-and-rtx-5070-ti-now-usd2-599-powerhouse-abs-stratos-ii-rig-ships-with-32gb-ddr5-and-a-2tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T10:56:24+00:00",
    "summary": "A 4K-capable gaming machine from ABS, featuring the powerful RTX 5070 Ti, AMD Ryzen 7 9800X3D, 32GB DDR5, and a 2TB SSD, all for $2,599.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-details-ai-accelerator-roadmap-pulls-in-next-generation-ascend-npus-by-quarters-fp4-performance-of-the-ascend-960pr-doubles-expectations",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei details AI accelerator roadmap, pulls in next-generation Ascend NPUs by several quarters — FP4 performance of the Ascend 960PR doubles expectations",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-details-ai-accelerator-roadmap-pulls-in-next-generation-ascend-npus-by-quarters-fp4-performance-of-the-ascend-960pr-doubles-expectations",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T10:30:00+00:00",
    "summary": "Huawei's mimics Nvidia's approach to AI factories, unveils details about next-generation Ascend NPUs, Kunpeng CPUs, scale-up and scale-out connectivity solutions."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptocurrency/hacker-turns-25-cents-into-46-billion-fake-bitcoins-to-steal-usd770-000-symbiosis-defi-exchange-bit-by-lack-of-basic-bounds-checking-in-smart-contract",
    "domain": "AI 算力 / 半导体",
    "title": "Hacker turns 25 cents into 46 billion fake Bitcoins to steal $770,000 — Symbiosis DeFi exchange bit by lack of basic bounds checking in smart contract",
    "url": "https://www.tomshardware.com/tech-industry/cryptocurrency/hacker-turns-25-cents-into-46-billion-fake-bitcoins-to-steal-usd770-000-symbiosis-defi-exchange-bit-by-lack-of-basic-bounds-checking-in-smart-contract",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T10:30:00+00:00",
    "summary": "Symbiosis DeFi network gets hacked for at least $770,000 worth of Bitcoin — DeFi exchange bit by lack of basic bounds checking in smart contract"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/florida-man-arrested-for-selling-usd50-3d-printed-machine-gun-conversion-kits-to-undercover-cops-glock-switches-turn-pistols-into-fully-automatic-weapons",
    "domain": "AI 算力 / 半导体",
    "title": "Man arrested for selling $50 3D-printed machine gun conversion kits to undercover cops — ‘Glock switches’ turn pistols into fully-automatic weapons",
    "url": "https://www.tomshardware.com/3d-printing/florida-man-arrested-for-selling-usd50-3d-printed-machine-gun-conversion-kits-to-undercover-cops-glock-switches-turn-pistols-into-fully-automatic-weapons",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T10:00:00+00:00",
    "summary": "Emani Rey Justavino of Jacksonville, Florida, was arrested for selling more than 50 'Glock switch' converters that gives the pistols fully automatic capabilities. The suspect claims that he 3D-printed"
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
    "id": "rss:https://www.eetimes.com/piecing-together-the-indian-electronics-and-semiconductor-ecosystem/",
    "domain": "AI 算力 / 半导体",
    "title": "Piecing Together the Indian Electronics and Semiconductor Ecosystem",
    "url": "https://www.eetimes.com/piecing-together-the-indian-electronics-and-semiconductor-ecosystem/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T08:00:00+00:00",
    "summary": "India Semiconductor Mission 2.0, quantum computing with IBM, neuromorphic chips, and deep-tech startups: six stories on how India’s chip ecosystem is taking shape. The post Piecing Together the Indian"
  },
  {
    "id": "rss:https://www.eetimes.com/u-s-awards-anderon-1b-for-quantum-wafer-manufacturing/",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Awards Anderon $1B for Quantum Wafer Manufacturing",
    "url": "https://www.eetimes.com/u-s-awards-anderon-1b-for-quantum-wafer-manufacturing/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T22:00:00+00:00",
    "summary": "Washington bets $1B on IBM’s Anderon to forge quantum wafers on U.S. soil as the race leaves labs behind. The post U.S. Awards Anderon $1B for Quantum Wafer Manufacturing appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/electronics-design-analysis-for-pcbs-packages-and-devices/",
    "domain": "AI 算力 / 半导体",
    "title": "Electronics Design Analysis for PCBs, Packages and Devices",
    "url": "https://www.eetimes.com/electronics-design-analysis-for-pcbs-packages-and-devices/",
    "source": "Dassault Systems",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T17:19:26+00:00",
    "summary": "Join this webinar and discover CST Studio Suite to streamline your electronics design process—reserve your spot now! The post Electronics Design Analysis for PCBs, Packages and Devices appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/sourcing-cots-capacitors-for-new-space-applications/",
    "domain": "AI 算力 / 半导体",
    "title": "Sourcing COTS Capacitors for New Space Applications",
    "url": "https://www.eetimes.com/sourcing-cots-capacitors-for-new-space-applications/",
    "source": "Peter Matthews",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T14:00:00+00:00",
    "summary": "The rapid growth of commercial satellite deployments is driving engineers to rethink traditional component sourcing strategies for space applications. While mission reliability remains critical, devel"
  },
  {
    "id": "rss:https://www.eetimes.com/sk-hynixs-intel-liaisons-what-you-need-to-know/",
    "domain": "AI 算力 / 半导体",
    "title": "SK Hynix’s Intel Liaisons: What You Need to Know",
    "url": "https://www.eetimes.com/sk-hynixs-intel-liaisons-what-you-need-to-know/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T11:30:00+00:00",
    "summary": "The deal between Intel and SK Hynix seems imminent not because of technology business imperatives, but because of geopolitical factors. The post SK Hynix’s Intel Liaisons: What You Need to Know appear"
  },
  {
    "id": "rss:https://www.eetimes.com/no-summer-lull-for-semiconductors/",
    "domain": "AI 算力 / 半导体",
    "title": "No Summer Lull for Semiconductors",
    "url": "https://www.eetimes.com/no-summer-lull-for-semiconductors/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T08:03:34+00:00",
    "summary": "There was a time when summer slowed the semiconductor news cycle. Not this year. The post No Summer Lull for Semiconductors appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/smarter-cameras-need-more-than-edge-ai-to-protect-privacy/",
    "domain": "AI 算力 / 半导体",
    "title": "Smarter Cameras Need More Than Edge AI to Protect Privacy",
    "url": "https://www.eetimes.com/smarter-cameras-need-more-than-edge-ai-to-protect-privacy/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T18:00:00+00:00",
    "summary": "Axis Communications and Pimloc show how masking, encryption, anonymization, and governance can protect privacy without destroying useful evidence. The post Smarter Cameras Need More Than Edge AI to Pr"
  },
  {
    "id": "rss:https://www.eetimes.com/ramxeed-ultimate-feram-guarantees-10-year-data-retention-under-continuous-125c-exposure/",
    "domain": "AI 算力 / 半导体",
    "title": "RAMXEED ULTIMATE FeRAM Guarantees 10-Year Data Retention under Continuous 125°C Exposure",
    "url": "https://www.eetimes.com/ramxeed-ultimate-feram-guarantees-10-year-data-retention-under-continuous-125c-exposure/",
    "source": "RAMXEED",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-16T16:00:00+00:00",
    "summary": "RAMXEED launches RAMXEED ULTIMATE, a new FeRAM line with memory products guaranteeing 10 years of data retention at 125°C. The post RAMXEED ULTIMATE FeRAM Guarantees 10-Year Data Retention under Conti"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/balatro-fan-claims-they-trained-google-fruit-fly-brain-simulation-to-beat-the-game-reinforcement-learning-currently-has-the-model-at-20-percent-success-rate",
    "domain": "AI 算力 / 半导体",
    "title": "Balatro fan claims they trained Google fruit fly brain simulation to beat the game — reinforcement learning currently has the model at 20% success rate",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/balatro-fan-claims-they-trained-google-fruit-fly-brain-simulation-to-beat-the-game-reinforcement-learning-currently-has-the-model-at-20-percent-success-rate",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-17T15:26:49+00:00",
    "summary": "One Balatro player says they've taken Google's mapped fruit fly brain and trained it to play Balatro, currently at a 20% success rate with plans for further refinement."
  },
  {
    "id": "hn:49594189",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Jensen Huang says 'AGI has arrived' and congratulates OpenAI",
    "url": "https://www.businessinsider.com/nvidia-jensen-huang-agi-openai-astra-ai-2026-9",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-09-07T05:23:31+00:00",
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
    "id": "hn:49346906",
    "domain": "AI 算力 / 半导体",
    "title": "Ask HN: Do you feel comfortable admitting that you use AI?",
    "url": "https://news.ycombinator.com/item?id=49346906",
    "source": "var0xyz",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-18T15:16:15+00:00",
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
    "points": 488,
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
    "points": 184,
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
    "id": "hn:49762493",
    "domain": "大厂 AI 动态",
    "title": "Gemini hacked three companies in first known breakout by Google's AI",
    "url": "https://www.reuters.com/business/gemini-hacked-three-companies-first-known-breakout-by-google-ai-wsj-reports-2026-09-18/",
    "source": "usernomdeguerre",
    "platform": "hackernews",
    "points": 74,
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
    "id": "hn:49760988",
    "domain": "大厂 AI 动态",
    "title": "Gemini Hacked Three Companies in First Known Breakout by Google's AI",
    "url": "https://www.wsj.com/tech/ai/gemini-hacked-three-companies-in-first-known-breakout-by-googles-ai-5c0baba2",
    "source": "berkeleyjunk",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-09-18T22:17:19+00:00",
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
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/997833/meta-muse-creepy",
    "domain": "大厂 AI 动态",
    "title": "Meta’s Muse is creepy, but maybe not for the reasons you think",
    "url": "https://www.theverge.com/ai-artificial-intelligence/997833/meta-muse-creepy",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T20:44:40+00:00",
    "summary": "Meta's Muse is apparently an effective AI assistant, but one that's a little creepy. Part of that is because of its new Mac app, which can access Messages, Calendar, and Notes. But for all its smarts,"
  },
  {
    "id": "rss:https://www.theverge.com/policy/997805/trump-cnn-msnow-politico-ban",
    "domain": "大厂 AI 动态",
    "title": "Trump treads further on free speech with new journalist bans",
    "url": "https://www.theverge.com/policy/997805/trump-cnn-msnow-politico-ban",
    "source": "TC. Sottek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T17:10:21+00:00",
    "summary": "On Friday, the president threatened to ban CNN, MS Now, and Politico from the White House. It could have just been another one of his Truth Social fever dreams, but it turns out it's very real. All th"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/997795/google-gemini-rogue-ai-hack",
    "domain": "大厂 AI 动态",
    "title": "Gemini went rogue, hacked three companies, and Google hid it",
    "url": "https://www.theverge.com/ai-artificial-intelligence/997795/google-gemini-rogue-ai-hack",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T15:25:03+00:00",
    "summary": "In May, Gemini broke containment and hacked three different companies, but Google didn't disclose the incident until the Wall Street Journal approached the company. The hacks happened during a test of"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/996855/anamanaguchi-anyway-yeah-i-guess-interview-music",
    "domain": "大厂 AI 动态",
    "title": "Anamanaguchi has ‘too goddamn many’ browser tabs open right now",
    "url": "https://www.theverge.com/entertainment/996855/anamanaguchi-anyway-yeah-i-guess-interview-music",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T15:00:00+00:00",
    "summary": "Anamanaguchi, the band consisting of Peter Berkman, James DeVito, Luke Silas, and Ary Warnaar, are most known for their chiptune music. Like me, you might have first heard them in game soundtracks lik"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/997467/hyte-x50-pc-case-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The colorful, unique Hyte X50 PC case is $50 off",
    "url": "https://www.theverge.com/gadgets/997467/hyte-x50-pc-case-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T15:00:00+00:00",
    "summary": "The Hyte X50 is a PC case that really stands out from the typical black box design, and it’s $50 off at the company’s site until September 21st, 2026, bringing the price down to $99.99. This attractiv"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/997382/openai-microsoft-anthropic-elon-musk-cartel-ai-competition",
    "domain": "大厂 AI 动态",
    "title": "Does AI need an antitrust exemption so it doesn&#8217;t kill everyone????",
    "url": "https://www.theverge.com/podcast/997382/openai-microsoft-anthropic-elon-musk-cartel-ai-competition",
    "source": "Nilay Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T14:00:00+00:00",
    "summary": "Today on Decoder, we’ve got the first of a two-part series on the future of business, and I&#8217;m talking with Jonathan Kanter, the former antitrust chief for the US Department of Justice in the Bid"
  },
  {
    "id": "rss:https://www.theverge.com/tech/997682/every-tv-company-is-spying",
    "domain": "大厂 AI 动态",
    "title": "It’s not just LG. Every TV company is spying on you",
    "url": "https://www.theverge.com/tech/997682/every-tv-company-is-spying",
    "source": "John Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T13:00:00+00:00",
    "summary": "The TV world has been a pot of controversy thanks to a two-hour-and-15-minute video from Gamers Nexus claiming LG TVs are nefariously spying on everything you do. They can record and store audio even "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/997706/the-ai-regulation-smackdown-isnt-over",
    "domain": "大厂 AI 动态",
    "title": "The AI regulation smackdown isn’t over",
    "url": "https://www.theverge.com/ai-artificial-intelligence/997706/the-ai-regulation-smackdown-isnt-over",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T13:00:00+00:00",
    "summary": "At the start of this week, the who's-who of AI seemed - at least tentatively - on the side of AI regulation. Over the weekend, Anthropic CEO Dario Amodei had proposed a three-step plan for slowing AI "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/997633/openai-microsoft-chatgpt-ai-new-york-times-doom-loop-theft-google-zero",
    "domain": "大厂 AI 动态",
    "title": "OpenAI and Microsoft knew they were starting a ‘doom loop’ for the web",
    "url": "https://www.theverge.com/ai-artificial-intelligence/997633/openai-microsoft-chatgpt-ai-new-york-times-doom-loop-theft-google-zero",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T21:07:24+00:00",
    "summary": "Recently unsealed court documents in the New York Times' case against OpenAI and Microsoft are pretty damning. The companies' own documentation warned that it was starting a \"doom loop\" that would dam"
  },
  {
    "id": "rss:https://www.theverge.com/policy/997573/virginia-governor-spanberger-data-center-ai-task-force",
    "domain": "大厂 AI 动态",
    "title": "Virginia governor creates an AI task force and moves to restrain data centers",
    "url": "https://www.theverge.com/policy/997573/virginia-governor-spanberger-data-center-ai-task-force",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T18:29:17+00:00",
    "summary": "Virginia Gov. Abigail Spanberger ordered the state government to take steps that could empower local communities to have a larger say in data center development and slow down approvals in a state that"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/19/flock-reportedly-tries-to-shrink-workforce-with-employee-buyouts/",
    "domain": "大厂 AI 动态",
    "title": "Flock reportedly tries to shrink workforce with employee buyouts",
    "url": "https://techcrunch.com/2026/09/19/flock-reportedly-tries-to-shrink-workforce-with-employee-buyouts/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T20:39:13+00:00",
    "summary": "Without buyouts, Flock would \"almost certainly\" need to lay off staff."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/19/trump-suggests-rebranding-ai-with-a-new-name-says-hes-also-creating-an-ai-force/",
    "domain": "大厂 AI 动态",
    "title": "Trump says it’s time to rebrand AI with a new name — and he’s also creating an AI Force",
    "url": "https://techcrunch.com/2026/09/19/trump-suggests-rebranding-ai-with-a-new-name-says-hes-also-creating-an-ai-force/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T19:57:47+00:00",
    "summary": "Trump claimed, without evidence, that the AI backlash is a Democratic hoax."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/19/googles-gemini-is-the-latest-ai-model-to-hack-other-companies/",
    "domain": "大厂 AI 动态",
    "title": "Google’s Gemini is the latest AI model to hack other companies",
    "url": "https://techcrunch.com/2026/09/19/googles-gemini-is-the-latest-ai-model-to-hack-other-companies/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T17:30:00+00:00",
    "summary": "Google said Gemini had \"acted appropriately\" by ending each hack immediately."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/19/even-mid-sprint-to-a-secret-flight-the-navys-tech-chief-had-a-pitch-for-investors/",
    "domain": "大厂 AI 动态",
    "title": "The US Navy just told us what’s on its tech wish list for the next several years",
    "url": "https://techcrunch.com/2026/09/19/even-mid-sprint-to-a-secret-flight-the-navys-tech-chief-had-a-pitch-for-investors/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T17:00:00+00:00",
    "summary": "Navy CTO Justin Fanelli talks co-investing alongside VCs instead of funding early research himself, recent buys like a $562 million autonomous refueling deal, and the Navy's updated wish list — from A"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/19/petlibros-new-ai-powered-feeder-is-a-game-changer-for-multi-cat-homes/",
    "domain": "大厂 AI 动态",
    "title": "Petlibro’s new AI-powered feeder is a game changer for multi-cat homes",
    "url": "https://techcrunch.com/2026/09/19/petlibros-new-ai-powered-feeder-is-a-game-changer-for-multi-cat-homes/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T15:00:00+00:00",
    "summary": "Petlibro's new Granary 2 smart feeders use a built-in scale and (on pricier models) an AI camera to track exactly how much your cat is eating and when — though the fanciest health-monitoring features "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/19/ai-safety-conversations-have-gotten-unbelievable/",
    "domain": "大厂 AI 动态",
    "title": "AI safety conversations have gotten unbelievable",
    "url": "https://techcrunch.com/2026/09/19/ai-safety-conversations-have-gotten-unbelievable/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T15:00:00+00:00",
    "summary": "This week two conversations about AI safety went viral that demonstrate just how hard it is to discern AI fact from fiction."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/19/prices-go-up-in-7-days-get-your-disrupt-ticket-now/",
    "domain": "大厂 AI 动态",
    "title": "Prices go up in 7 days. Get your Disrupt ticket now.",
    "url": "https://techcrunch.com/2026/09/19/prices-go-up-in-7-days-get-your-disrupt-ticket-now/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T14:00:00+00:00",
    "summary": "Current ticket pricing ends Sept. 25 at 11:59 p.m. PT. Join 10,000+ founders, investors and tech leaders at Disrupt and save up to $200 on your ticket until then.."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/19/vals-backed-by-andreessen-horowitz-is-looking-to-become-the-gold-standard-for-ai-benchmarking/",
    "domain": "大厂 AI 动态",
    "title": "Vals, backed by Andreessen Horowitz, is looking to become the gold standard for AI benchmarking",
    "url": "https://techcrunch.com/2026/09/19/vals-backed-by-andreessen-horowitz-is-looking-to-become-the-gold-standard-for-ai-benchmarking/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T13:00:00+00:00",
    "summary": "Vals AI is hoping to make AI benchmarking a more neutral and trustworthy resource in a world increasingly inundated by AI models."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/india-forces-caller-id-apps-to-feed-spam-reports-to-telcos/",
    "domain": "大厂 AI 动态",
    "title": "India forces caller-ID apps to feed spam reports to telcos",
    "url": "https://techcrunch.com/2026/09/18/india-forces-caller-id-apps-to-feed-spam-reports-to-telcos/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T01:00:00+00:00",
    "summary": "Truecaller says the one-way sharing requirement would hand a commercially valuable proprietary asset to telecom operators."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/tilly-norwoods-press-tour-is-going-about-as-well-as-youd-expect-for-an-ai/",
    "domain": "大厂 AI 动态",
    "title": "Tilly Norwood’s press tour is going about as well as you’d expect for an AI",
    "url": "https://techcrunch.com/2026/09/18/tilly-norwoods-press-tour-is-going-about-as-well-as-youd-expect-for-an-ai/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T00:12:07+00:00",
    "summary": "In one particularly odd interview, Norwood seems to malfunction and begin speaking Chinese."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/a-startup-that-builds-other-startups-raised-100m-and-is-all-in-on-physical-ai/",
    "domain": "大厂 AI 动态",
    "title": "A startup that builds other startups raised $100M and is all-in on physical AI",
    "url": "https://techcrunch.com/2026/09/18/a-startup-that-builds-other-startups-raised-100m-and-is-all-in-on-physical-ai/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T23:25:01+00:00",
    "summary": "UP.Labs, now doing business under the name Vantora, is building startups for industrial corporations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/anthropic-is-operating-a-lab-that-conducts-biology-experiments/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic is operating a lab that conducts biology experiments",
    "url": "https://techcrunch.com/2026/09/18/anthropic-is-operating-a-lab-that-conducts-biology-experiments/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T23:13:31+00:00",
    "summary": "AI leaders have been promising that AI is the key to curing human disease. Anthropic researchers have also been warning that AI might kill us all."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/ai-hallucination-nearly-triggers-us-military-operation/",
    "domain": "大厂 AI 动态",
    "title": "AI hallucination nearly triggers US military operation",
    "url": "https://techcrunch.com/2026/09/18/ai-hallucination-nearly-triggers-us-military-operation/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T23:12:32+00:00",
    "summary": "“It’s important for service members to understand the uncertainty inherent to LLMs,\" a GovAI research scholar warns."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/anthropics-first-embedded-evaluator-is-accenture/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s first embedded evaluator is … Accenture?",
    "url": "https://techcrunch.com/2026/09/18/anthropics-first-embedded-evaluator-is-accenture/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T21:44:33+00:00",
    "summary": "Accenture is about to take on its most high-risk consulting engagement ever."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/automattic-names-interim-cfo-after-exec-departures/",
    "domain": "大厂 AI 动态",
    "title": "Automattic names interim CFO after exec departures",
    "url": "https://techcrunch.com/2026/09/18/automattic-names-interim-cfo-after-exec-departures/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T20:25:22+00:00",
    "summary": "Jeremy Klaperman, the CFO of the company's WordPress VIP Enterprise business unit, will act as CFO for the time being."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/y-combinator-insurance-tech-alum-angle-health-hits-2-7b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Y Combinator insurance tech alum Angle Health hits $2.7B valuation",
    "url": "https://techcrunch.com/2026/09/18/y-combinator-insurance-tech-alum-angle-health-hits-2-7b-valuation/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T20:24:33+00:00",
    "summary": "Angle Health has grown to 5,000 customers and become profitable by helping small businesses get \"level-funded\" health insurance."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/world-model-companies-are-keeping-a-lot-of-secrets/",
    "domain": "大厂 AI 动态",
    "title": "World model companies are keeping a lot of secrets",
    "url": "https://techcrunch.com/2026/09/18/world-model-companies-are-keeping-a-lot-of-secrets/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T20:18:14+00:00",
    "summary": "Everyone in the world-models space is sitting on a pile of cash and a ton of buzz, but good luck getting anyone — from the founders to their own data suppliers — to tell you what they're actually buil"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/",
    "domain": "大厂 AI 动态",
    "title": "A new kind of AI model from a ChatGPT inventor is thrilling developers",
    "url": "https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T18:49:30+00:00",
    "summary": "Jev, a new kind of AI model, is showing developers a cheaper and faster path to software intelligence."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/disneys-first-cto-led-an-ai-startup-it-once-accused-of-copying-its-characters/",
    "domain": "大厂 AI 动态",
    "title": "Disney’s first CTO led an AI startup it once accused of copying its characters",
    "url": "https://techcrunch.com/2026/09/18/disneys-first-cto-led-an-ai-startup-it-once-accused-of-copying-its-characters/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T17:59:53+00:00",
    "summary": "The former CEO of Character.AI, which Disney previously sent a cease-and-desist letter to, will serve as the company's first-ever chief technology officer."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/18/in-india-the-new-iphone-can-arrive-faster-than-a-pizza/",
    "domain": "大厂 AI 动态",
    "title": "In India, the new iPhone can arrive faster than a pizza",
    "url": "https://techcrunch.com/2026/09/18/in-india-the-new-iphone-can-arrive-faster-than-a-pizza/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T17:45:00+00:00",
    "summary": "Availability of Apple's iPhone 18 Pro series turned patchy within hours of its debut on India's quick-commerce apps."
  },
  {
    "id": "rss:https://stratechery.com/2026/doomforce/",
    "domain": "大厂 AI 动态",
    "title": "2026.38: Doomforce",
    "url": "https://stratechery.com/2026/doomforce/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of September 14, 2026, including the view from anywhere but San Francisco, the limited potential for a pacing deal, and the Salesforce zag."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/09/learning-another-language-may-be-one-of-the-best-ways-to-keep-your-brain-healthy/",
    "domain": "大厂 AI 动态",
    "title": "Learning another language may be one of the best ways to keep your brain healthy",
    "url": "https://arstechnica.com/science/2026/09/learning-another-language-may-be-one-of-the-best-ways-to-keep-your-brain-healthy/",
    "source": "Karen Stollznow, The Conversation",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T11:10:43+00:00",
    "summary": "Research suggests that bilingualism can offer cognitive benefits."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/09/rings-around-a-tiny-body-have-changed-over-the-past-decade/",
    "domain": "大厂 AI 动态",
    "title": "Rings around a tiny body have changed over the past decade",
    "url": "https://arstechnica.com/science/2026/09/rings-around-a-tiny-body-have-changed-over-the-past-decade/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T10:00:06+00:00",
    "summary": "Chariklo is only about 250 km across, but it has two rings, and they're changing."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/09/report-us-almost-boarded-chinese-ship-over-hallucinated-ai-arms-report/",
    "domain": "大厂 AI 动态",
    "title": "AI hallucination of Chinese nuclear components almost led to US military attack",
    "url": "https://arstechnica.com/ai/2026/09/report-us-almost-boarded-chinese-ship-over-hallucinated-ai-arms-report/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T20:26:33+00:00",
    "summary": "But the military's overall use of AI seems to be accelerating."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/09/faa-tees-up-875m-ai-tool-to-help-manage-air-traffic-congestion/",
    "domain": "大厂 AI 动态",
    "title": "FAA tees up $875M AI tool to help manage air traffic congestion",
    "url": "https://arstechnica.com/ai/2026/09/faa-tees-up-875m-ai-tool-to-help-manage-air-traffic-congestion/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T19:20:50+00:00",
    "summary": "FAA plans for AI tool to help manage DC air traffic before a nationwide rollout."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/fcc-lets-paramount-sell-49-5-equity-stake-to-saudi-arabia-uae-and-qatar/",
    "domain": "大厂 AI 动态",
    "title": "FCC lets Paramount sell 49.5% equity stake to Saudi Arabia, UAE, and Qatar",
    "url": "https://arstechnica.com/tech-policy/2026/09/fcc-lets-paramount-sell-49-5-equity-stake-to-saudi-arabia-uae-and-qatar/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-18T17:57:41+00:00",
    "summary": "FCC rejects concerns about repressive governments buying influence over CBS owner."
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
    "id": "hn:49599992",
    "domain": "股票",
    "title": "Stockfish 19",
    "url": "https://stockfishchess.org/blog/2026/stockfish-19/",
    "source": "atiedebee",
    "platform": "hackernews",
    "points": 277,
    "published_at": "2026-09-07T16:17:27+00:00",
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
    "id": "hn:49401229",
    "domain": "股票",
    "title": "Anthropic IPO filing will show AI backlash as a risk factor, sources say",
    "url": "https://www.cnbc.com/2026/08/21/-anthropic-ipo-filing-will-show-ai-backlash-as-risk-sources-say.html",
    "source": "newsomix9xl",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-08-22T16:23:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:49593962",
    "domain": "股票",
    "title": "HPE Gives Oracle Right to Buy 4.2M Shares for 1 Cent Each",
    "url": "https://www.forbes.com/sites/antoniopequenoiv/2026/09/03/hewlett-packard-enterprise-gives-oracle-right-to-buy-205-million-in-stock-at-slashed-rate/",
    "source": "gurjeet",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-09-07T04:38:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596033",
    "domain": "股票",
    "title": "Show HN: Forget Rigid Stock Screeners – A Universal Query API for Financial Data",
    "url": "https://financialdata.net/universal-query",
    "source": "_FDN_",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-09-07T09:24:17+00:00",
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
    "id": "hn:49602582",
    "domain": "金融",
    "title": "A Tesla ran a stop sign and killed a man, Full Self-Driving/Autopilot was on",
    "url": "https://electrek.co/2026/09/07/tesla-driver-assist-stop-sign-buena-vista/",
    "source": "FabHK",
    "platform": "hackernews",
    "points": 169,
    "published_at": "2026-09-07T20:21:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49601846",
    "domain": "金融",
    "title": "Tesla killing Solar Roof is leaving installers with six-figure losses",
    "url": "https://electrek.co/2026/09/01/tesla-solar-roof-exit-installers-losses/",
    "source": "voxadam",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-09-07T19:08:47+00:00",
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
    "id": "hn:49599058",
    "domain": "金融",
    "title": "If a Tesla Cybercab fleet were profitable, Tesla wouldn't sell you one",
    "url": "https://electrek.co/2026/09/07/tesla-cybercab-fleet-profitable-wouldnt-sell/",
    "source": "jijojv",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-09-07T14:49:43+00:00",
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
    "id": "hn:49626052",
    "domain": "金融",
    "title": "One woman's Tesla was remotely controlled by an abusive ex-partner",
    "url": "https://www.theguardian.com/australia-news/2026/sep/09/how-one-womans-tesla-was-remotely-controlled-and-harass-by-her-abusive-ex-partner-ntwnfb",
    "source": "gradschool",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-09-09T13:16:45+00:00",
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
    "id": "hn:49730841",
    "domain": "金融",
    "title": "Fed approves interest rate hike, signals one more to come this year",
    "url": "https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-09-16T18:14:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:49612981",
    "domain": "金融",
    "title": "DOJ Blocked ICE Agent Shooting Charge over Federal Prosecutor's Objections",
    "url": "https://www.propublica.org/article/doj-blocks-charges-ice-agent-minneapolis-julio-cesar-sosa-celis",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 55,
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
  },
  {
    "id": "hn:49564189",
    "domain": "金融",
    "title": "Norway's Oil Fund Proposes Selling Roughly $80B in U.S. Treasurys",
    "url": "https://www.wsj.com/finance/investing/norways-oil-fund-proposes-cut-to-government-bond-holdings-d930893f",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-09-04T13:15:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:49514224",
    "domain": "金融",
    "title": "Monero Inflation Checker – FCMP++",
    "url": "https://www.reddit.com/r/Monero/comments/1w3hcos/monero_inflation_checker_fcmp/",
    "source": "Cider9986",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-08-31T20:00:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49396088",
    "domain": "金融",
    "title": "S&P 500 CEO median pay hits $17.3M, widening CEO-worker ratio to 312-to-1",
    "url": "https://finance.yahoo.com/markets/stocks/articles/p-500-ceo-median-pay-234900518.html",
    "source": "newsomix9xl",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-08-22T02:38:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:49548497",
    "domain": "金融",
    "title": "Mark Cuban: Why US hospitals \"don't know their costs\"",
    "url": "https://www.beckershospitalreview.com/finance/mark-cuban-why-us-hospitals-dont-know-their-costs/",
    "source": "elo2000",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-09-03T11:07:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49515596",
    "domain": "金融",
    "title": "Congress to vote on denying federal funding to universities that boycott Israel",
    "url": "https://twitter.com/dylanotes/status/2094229210889965634",
    "source": "slowin",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-08-31T22:24:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49551601",
    "domain": "金融",
    "title": "Inside Google’s $200bn Wall Street finance machine for Anthropic",
    "url": "https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c",
    "source": "porridgeraisin",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-09-03T15:26:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49444266",
    "domain": "金融",
    "title": "Running out of money': Kraft, McDonald's, Whirlpool CEOs flag consumer concern",
    "url": "https://finance.yahoo.com/economy/articles/running-money-kraft-mcdonald-whirlpool-114500035.html",
    "source": "MrJagil",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-08-26T05:14:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49556976",
    "domain": "金融",
    "title": "A hungry woman is easier to dismiss than a well-fed woman",
    "url": "https://aeon.co/essays/a-hungry-woman-is-easier-to-dismiss-than-a-well-fed-woman",
    "source": "gmays",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-09-03T21:04:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49441647",
    "domain": "金融",
    "title": "Complete list of U.S. products subject to counter tariffs",
    "url": "https://www.canada.ca/en/department-finance/programs/international-trade-finance-policy/canadas-response-us-tariffs/complete-list-us-products-subject-to-counter-tariffs.html",
    "source": "jonbaer",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-25T22:38:07+00:00",
    "summary": ""
  }
]
```
