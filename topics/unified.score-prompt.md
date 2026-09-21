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

- 今日日期：`2026-09-21`
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
  "date": "2026-09-21",
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
    "points": 11493305,
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
    "points": 6044005,
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
    "points": 5837948,
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
    "points": 3586287,
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
    "points": 2897871,
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
    "points": 2016914,
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
    "points": 1971320,
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
    "points": 1890166,
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
    "points": 1868442,
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
    "points": 1764217,
    "published_at": "2026-03-20T01:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260320\n2026黑马程序员AI智能应用开发学习路线图\nhttps://www.bilibili.com/opus/1156896913511940102\n如何下载资料\nhttps://www.bilibili.com/read/cv7881295/\n学习+球球群625260577，告别孤单，共同进步！\n\n【AI智能"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1361258,
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
    "points": 1317293,
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
    "points": 1255848,
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
    "points": 1196718,
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
    "points": 1093781,
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
    "points": 1079033,
    "published_at": "2025-11-28T10:20:16+00:00",
    "summary": "课程涵盖基础概念、算法原理、实践应用，从零开始，深入浅出。通过实例演示，掌握神经网络、决策树、支持向量机等关键技术。适合初学者和进阶者，助您快速提升技能，开启智能时代新篇章。立即观看，开启您的AI学习之旅！"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 945493,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 936457,
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
    "points": 889076,
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
    "points": 821709,
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
    "points": 796986,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1SQo5BAEBo",
    "domain": "AI",
    "title": "trae使用教程【B站最详细，零基础必看！】trae小白入门到精通traeCN教程traeexceltrae项目实战trae安装教程用教程trae开发小程序",
    "url": "http://www.bilibili.com/video/av116458407336746",
    "source": "trae教程",
    "platform": "bilibili",
    "points": 741417,
    "published_at": "2026-04-24T07:10:58+00:00",
    "summary": "trae使用教程trae小白入门到精通traeCN教程traeexceltrae项目实战trae安装教程用trae开发小程序traecn使用教程"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 687227,
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
    "points": 673795,
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
    "points": 621164,
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
    "points": 589793,
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
    "points": 573658,
    "published_at": "2025-07-22T01:07:39+00:00",
    "summary": "Agent 的概念、原理与构建模式 —— 从零打造一个简化版的 Claude Code\n \n我们将以 ReAct 和 Plan-And-Execute 这两种模式为例，为大家讲解 Agent 的概念、原理与构建模式，并在这个过程中为大家演示如何从零打造一个简化版的 Claude Code，让大家彻底明白 Agent 是如何运作的。\n \n时间轴：\n00:00 视频内容介绍\n00:33 什么是 Age"
  },
  {
    "id": "bvid:BV1YRG46eE1n",
    "domain": "AI",
    "title": "Agent、Skill、Harness啥意思？一次性讲明白AI技术名词！",
    "url": "http://www.bilibili.com/video/av116617757459999",
    "source": "通义实验室",
    "platform": "bilibili",
    "points": 517420,
    "published_at": "2026-05-22T10:30:39+00:00",
    "summary": "AI圈名词一波又一波\nLLM、Token、Prompt、RAG、Skill、Agent、Harness...\n这些词究竟怎么出现的，又各自解决什么问题？\n一条视频带你彻底搞懂"
  },
  {
    "id": "bvid:BV1cV3b67Ehs",
    "domain": "AI",
    "title": "同济博一｜我的Codex论文辅助全流程",
    "url": "http://www.bilibili.com/video/av117009639670939",
    "source": "艺雨YiLight",
    "platform": "bilibili",
    "points": 361342,
    "published_at": "2026-07-30T15:36:34+00:00",
    "summary": "同济博一 | 我的Codex论文辅助全流程\n【中科大少年班+同济博一】\n介绍一下我自己的codex论文辅助全流程！\n\n分为以下几个部分:\n1、综合能力最强5个学术skill\n2、文献管理（skill、AI文献网站、zotero)\n3、idea与架构\n4、论文写作（不同学科）\n5、数据分析与绘图\n6、科研PPT制作\n7、论文日报/周报"
  },
  {
    "id": "bvid:BV1Vz3v6XE7w",
    "domain": "AI",
    "title": "纯手搓一部AI漫剧一个月收获3.1w！附教程！全流程操作演示！让零基础也能学会AI漫剧制作技巧！更多AI漫剧工具提示词+变现方法及全套教程都整啦！拿走不谢~",
    "url": "http://www.bilibili.com/video/av116996553312339",
    "source": "comfyui视频工作流",
    "platform": "bilibili",
    "points": 360386,
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
    "points": 357588,
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
    "points": 354934,
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
    "points": 338768,
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
    "points": 308220,
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
    "points": 293729,
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
    "points": 290800,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 265150,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1otokBpENn",
    "domain": "AI",
    "title": "【大模型RAG】2026年B站最全最细的RAG知识库搭建系统教程，手把手教你搭建私有知识库，从入门到实战全流程教学！全程干货！少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116475234882601",
    "source": "AI应用开发-",
    "platform": "bilibili",
    "points": 258715,
    "published_at": "2026-04-27T06:29:15+00:00",
    "summary": "【大模型RAG】2026年B站最全最细的RAG知识库搭建系统教程，手把手教你搭建私有知识库，从入门到实战全流程教学！全程干货！少走99%的弯路！"
  },
  {
    "id": "bvid:BV1o3wvzUEDD",
    "domain": "AI",
    "title": "（B站首推）2026李宏毅智能体【AI Agent】系列课程全集，公认体验感最好的入门课程！--人工智能/机器学习/深度学习/大模型/LLM",
    "url": "http://www.bilibili.com/video/av116249128340244",
    "source": "李宏毅agent",
    "platform": "bilibili",
    "points": 258151,
    "published_at": "2026-03-18T08:07:24+00:00",
    "summary": "李宏毅最新课程的学习资料和课程PPT都已经打包好了!!\n有需要的话可以在下方置顶或三连+留言领取！！！"
  },
  {
    "id": "bvid:BV13XjB6gERT",
    "domain": "AI",
    "title": "豆包、WorkBuddy、Codex、Hermes……到底怎么选？用 AI 的 5 层路线",
    "url": "http://www.bilibili.com/video/av116776184776494",
    "source": "CreateSomething",
    "platform": "bilibili",
    "points": 221393,
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
    "points": 208601,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 182406,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 181813,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1YG7G6eEPR",
    "domain": "AI",
    "title": "【全60集】吊打付费！目前B站最全最细的Agent智能体开发全套教程！手把手教你打造专属智能体，七天就能从小白到大神！带你从零基础入门到精通实现商业变现！",
    "url": "http://www.bilibili.com/video/av116815090947614",
    "source": "AI-Agent开发",
    "platform": "bilibili",
    "points": 161512,
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
    "points": 157091,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 121067,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1WWYE6LEzx",
    "domain": "AI",
    "title": "黑马程序员2026全网最夯VibeCoding零基础入门到实战项目开发全套视频教程，AI辅助编程从入门到实战，涵盖Claude Code、DeepSeek等内容",
    "url": "http://www.bilibili.com/video/av117251667724450",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 106573,
    "published_at": "2026-09-14T01:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260914\n2026黑马程序员AI智能应用开发学习路线图\nhttps://www.bilibili.com/opus/1156896913511940102\n如何下载资料\nhttps://www.bilibili.com/read/cv7881295/\n学习+球球群625260577，告别孤单，共同进步！\n\n【AI智能"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93755,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1sZMq6qEko",
    "domain": "AI",
    "title": "从0做出你的第一个App ｜ 零基础AI编程保姆教程",
    "url": "http://www.bilibili.com/video/av117038647352026",
    "source": "木子不写代码",
    "platform": "bilibili",
    "points": 82778,
    "published_at": "2026-08-07T12:15:00+00:00",
    "summary": "这期视频，我会手把手带你，用 AI 做出你的第一个 App。\n全程假设你没有任何编程和AI的基础，\n我们从如何写需求提示词开始，\n到确定页面结构和设计，\n产品需求文档，\n开发计划，\n第一版APP验收，\ngit代码存档，\n二次开发，\n界面美化，\n做好的APP也会开源给到大家，\n我也会演示如何获取这个项目源代码并且用AI继续定制开发，\n视频到最后，\n你会收获一个为自己的工作和生活定制的专属APP！\n和"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 75045,
    "published_at": "2025-07-12T04:00:00+00:00",
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
    "id": "hn:49714096",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC revealing details about next gen A14 node",
    "url": "https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331",
    "source": "osnium123",
    "platform": "hackernews",
    "points": 125,
    "published_at": "2026-09-15T15:31:55+00:00",
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
    "id": "rss:https://www.tomshardware.com/video-games/final-fantasy-vii-revelation-might-use-upwards-of-200-gb-and-requires-an-additional-download-latest-entry-in-the-series-of-remakes-may-set-a-new-record-for-the-size-of-a-base-install",
    "domain": "AI 算力 / 半导体",
    "title": "Final Fantasy VII Revelation might use upwards of 200 GB and requires an additional download — latest entry in the series of remakes may set a new record for the size of a base install",
    "url": "https://www.tomshardware.com/video-games/final-fantasy-vii-revelation-might-use-upwards-of-200-gb-and-requires-an-additional-download-latest-entry-in-the-series-of-remakes-may-set-a-new-record-for-the-size-of-a-base-install",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T13:30:00+00:00",
    "summary": "Final Fantasy VII Revelation might use upwards of 200 GB and requires an additional download — latest entry in the series of remakes may set a new record for the size of a base install"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/prusa-core-one-plus-indx-review",
    "domain": "AI 算力 / 半导体",
    "title": "Prusa CORE One+ INDX review: Time for a 'Tool' change",
    "url": "https://www.tomshardware.com/3d-printing/prusa-core-one-plus-indx-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T13:00:00+00:00",
    "summary": "Prusa Research reenters the toolchanger category with a little help from Bondtech."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/microsoft-patents-system-to-freeze-games-and-inject-ads-during-downtimes-watching-commercials-earns-ad-free-playtime-credits",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft patents system to freeze games and inject ads during downtimes — watching commercials earns ad-free playtime credits",
    "url": "https://www.tomshardware.com/video-games/microsoft-patents-system-to-freeze-games-and-inject-ads-during-downtimes-watching-commercials-earns-ad-free-playtime-credits",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T13:00:00+00:00",
    "summary": "This patent uses the game engine and machine learning to determine the best time to serve an ad."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/massive-192gb-gta-leak-reveals-early-gta-vi-map-and-canceled-dlcs-files-show-liquid-nitrogen-death-for-trevor-and-scrapped-liberty-city-expansion",
    "domain": "AI 算力 / 半导体",
    "title": "Massive 192GB GTA leak reveals early GTA VI map and canceled DLCs — files show liquid nitrogen death for Trevor and scrapped Liberty City expansion",
    "url": "https://www.tomshardware.com/video-games/massive-192gb-gta-leak-reveals-early-gta-vi-map-and-canceled-dlcs-files-show-liquid-nitrogen-death-for-trevor-and-scrapped-liberty-city-expansion",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T12:35:00+00:00",
    "summary": "The massive leak revealed early efforts in the development of GTA VI, as well as unreleased side missions, alternate endings, and even planned DLCs that never came to fruition."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/air-cooling/noctua-fans-prevent-the-caim1-anti-ai-4k-camera-from-throttling-unusual-cameras-processor-gets-toasty-as-it-records-while-performing-cryptographic-calculations",
    "domain": "AI 算力 / 半导体",
    "title": "Noctua fans prevent the CAIM1 ‘Anti-AI’ 4K camera from throttling — unusual camera’s processor gets toasty as it records while performing cryptographic calculations",
    "url": "https://www.tomshardware.com/pc-components/air-cooling/noctua-fans-prevent-the-caim1-anti-ai-4k-camera-from-throttling-unusual-cameras-processor-gets-toasty-as-it-records-while-performing-cryptographic-calculations",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T12:20:57+00:00",
    "summary": "A premium PC DIY fan brand has announced that one of its prized spinners is being used in an 'Anti-AI' 4K camera to prevent throttling."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/north-korea-used-job-interviews-to-deploy-malware-on-30-000-devices-during-coding-tests-waterplum-group-loots-usd10-7-million-in-crypto-and-plants-persistent-rats",
    "domain": "AI 算力 / 半导体",
    "title": "North Korea used job interviews to deploy malware on 30,000 devices during coding tests — WaterPlum group loots $10.7 million in crypto and plants persistent RATs",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/north-korea-used-job-interviews-to-deploy-malware-on-30-000-devices-during-coding-tests-waterplum-group-loots-usd10-7-million-in-crypto-and-plants-persistent-rats",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T12:10:00+00:00",
    "summary": "Multiple government agencies across the world released a warning that North Korean hackers are posting fake jobs to install malware on unsuspecting applicants' computers. They then steal credentials a"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/kash-patel-says-that-ai-use-at-the-fbi-has-increased-by-605-percent-since-he-became-director-claims-that-every-major-tech-player-is-embedded-in-the-agency",
    "domain": "AI 算力 / 半导体",
    "title": "Kash Patel says that AI use at the FBI has 'increased by 605%' since he became director — claims that every major tech player is 'embedded' in the agency",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/kash-patel-says-that-ai-use-at-the-fbi-has-increased-by-605-percent-since-he-became-director-claims-that-every-major-tech-player-is-embedded-in-the-agency",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T11:45:00+00:00",
    "summary": "FBI Director Kash Patel stated in an interview that he's responsible for a \"605% increase\" in the bureau's usage of AI. The problem is that it's hard to pin down what the figure refers to."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/autonomous-strike-drone-uses-nvidia-jetson-orin-nano-to-independently-pick-and-bomb-targets-swedish-startups-attack-drones-run-small-ai-model-require-no-human-input-and-zero-external-comms",
    "domain": "AI 算力 / 半导体",
    "title": "Autonomous NATO strike drone uses Nvidia Jetson Orin Nano to independently pick and bomb targets — Swedish startup's attack drones run small AI model, require no human input and zero external comms",
    "url": "https://www.tomshardware.com/tech-industry/drones/autonomous-strike-drone-uses-nvidia-jetson-orin-nano-to-independently-pick-and-bomb-targets-swedish-startups-attack-drones-run-small-ai-model-require-no-human-input-and-zero-external-comms",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T11:20:00+00:00",
    "summary": "Drones built with small, non-frontier computer-vision models autonomously identified and attacked targets in a recent demo."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-says-there-is-0-percent-chance-ai-destroys-the-world-by-2030-we-should-go-as-fast-as-we-can-irrespective-of-anyone-else-dismisses-anthropic-doom-warnings-and-rejects-new-regulations",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang says there is '0% chance' AI destroys the world by 2030 — 'We should go as fast as we can, irrespective of anyone else,' dismisses Anthropic doom warnings and rejects new regulations",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-says-there-is-0-percent-chance-ai-destroys-the-world-by-2030-we-should-go-as-fast-as-we-can-irrespective-of-anyone-else-dismisses-anthropic-doom-warnings-and-rejects-new-regulations",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T10:55:00+00:00",
    "summary": "Chief executive of Nvidia claims that fears that AI will destroy humanity in the coming years are unsubstantiated as safety mechanisms can preserve that."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/putin-casts-online-vote-using-unlicensed-windows-on-an-american-dell-pc-activate-windows-watermark-visible-in-official-kremlin-clip-uses-foreign-dell-pc-despite-russian-tech-mandate",
    "domain": "AI 算力 / 半导体",
    "title": "Putin casts online vote using unlicensed Windows on an American Dell PC — 'Activate Windows' watermark visible in official Kremlin clip, uses foreign Dell PC despite Russian tech mandate",
    "url": "https://www.tomshardware.com/software/windows/putin-casts-online-vote-using-unlicensed-windows-on-an-american-dell-pc-activate-windows-watermark-visible-in-official-kremlin-clip-uses-foreign-dell-pc-despite-russian-tech-mandate",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T10:30:00+00:00",
    "summary": "An official Russian media clip shows Putin voting on a Dell PC with an unlicensed copy of Windows."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/audiophiles-in-trouble-as-manufacturers-cease-optical-drive-production-hi-fi-cd-players-require-extensive-rework-to-use-components-from-other-companies",
    "domain": "AI 算力 / 半导体",
    "title": "Collapse of mainstream optical drive supply kills high-end CD players — PS Audio and Naim halt production as component costs double",
    "url": "https://www.tomshardware.com/peripherals/audiophiles-in-trouble-as-manufacturers-cease-optical-drive-production-hi-fi-cd-players-require-extensive-rework-to-use-components-from-other-companies",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T10:05:00+00:00",
    "summary": "PS Audio and Naim had to cease production of two Hi-Fi models as manufacturers quit making optical drives, even as CD and vinyl have hit record sales in recent months."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptomining/googles-simulated-fruit-fly-brain-mines-bitcoin-in-web-browser-proof-of-concept-futurebit-says-real-organic-neuron-miner-could-have-10x-the-efficiency-of-the-best-silicon-3nm-asics",
    "domain": "AI 算力 / 半导体",
    "title": "Google's simulated fruit fly brain 'mines Bitcoin' in web browser proof of concept — FutureBit says real organic neuron miner could have '10x the efficiency of the best silicon 3nm ASICs'",
    "url": "https://www.tomshardware.com/tech-industry/cryptomining/googles-simulated-fruit-fly-brain-mines-bitcoin-in-web-browser-proof-of-concept-futurebit-says-real-organic-neuron-miner-could-have-10x-the-efficiency-of-the-best-silicon-3nm-asics",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T09:40:00+00:00",
    "summary": "A project claimed to represent 'the first organic neuron Bitcoin miner based on the fly brain' has gone live."
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
    "id": "hn:49773998",
    "domain": "大厂 AI 动态",
    "title": "Microsoft agentically ports Copilot runtime to Rust for $120K",
    "url": "https://www.theregister.com/devops/2026/09/18/microsoft-agentically-ports-copilot-runtime-to-rust-for-120k/5297549",
    "source": "pjmlp",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-09-20T09:08:52+00:00",
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
    "id": "hn:49760988",
    "domain": "大厂 AI 动态",
    "title": "Gemini Hacked Three Companies in First Known Breakout by Google's AI",
    "url": "https://www.wsj.com/tech/ai/gemini-hacked-three-companies-in-first-known-breakout-by-googles-ai-5c0baba2",
    "source": "berkeleyjunk",
    "platform": "hackernews",
    "points": 42,
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
    "id": "rss:https://www.theverge.com/report/997948/no-dogs-in-space-is-back-punk-2-0-music-history-podcast",
    "domain": "大厂 AI 动态",
    "title": "No Dogs in Space is back to feed your need for obsessive music history",
    "url": "https://www.theverge.com/report/997948/no-dogs-in-space-is-back-punk-2-0-music-history-podcast",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T20:51:57+00:00",
    "summary": "In August, I wrote about my love of the music history podcast No Dogs in Space, but mourned the fact that there hadn't been a new episode in over two years. Little did I know that hosts Carolina Hidal"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/997936/nvidia-jensen-huang-ai-fears-overblown",
    "domain": "大厂 AI 动态",
    "title": "No one is surprised that Nvidia&#8217;s Jensen Huang thinks AI fears are overblown",
    "url": "https://www.theverge.com/ai-artificial-intelligence/997936/nvidia-jensen-huang-ai-fears-overblown",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T18:50:18+00:00",
    "summary": "The man who may stand to make the most money from the AI boom seems to think he knows better than anyone else, including researchers who have studied and worked on AI for decades. In an interview with"
  },
  {
    "id": "rss:https://www.theverge.com/games/997880/hideo-kojima-productions-physint-xbox-sony-playstation",
    "domain": "大厂 AI 动态",
    "title": "Kojima Productions disputes reports the studio is in trouble",
    "url": "https://www.theverge.com/games/997880/hideo-kojima-productions-physint-xbox-sony-playstation",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T18:15:10+00:00",
    "summary": "After it was announced that Sony was dropping Hideo Kojima's Physint, and that instead the Metal Gear Solid creator's latest title would be coming to Xbox, there were a flurry of rumors about the fall"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/997867/trump-ai-force-ai-czar",
    "domain": "大厂 AI 动态",
    "title": "Trump now says he wants to form an ‘AI Force’",
    "url": "https://www.theverge.com/ai-artificial-intelligence/997867/trump-ai-force-ai-czar",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T15:39:22+00:00",
    "summary": "The president posted on Truth Social that he wanted to appoint an \"AI czar\" to lead a new \"AI force.\" He made the announcement amid growing calls from across the political spectrum and even within the"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/997853/a24-scp-movie-creative-commons-license",
    "domain": "大厂 AI 动态",
    "title": "A24’s reputation is on the line with the SCP Foundation movie",
    "url": "https://www.theverge.com/entertainment/997853/a24-scp-movie-creative-commons-license",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T12:45:48+00:00",
    "summary": "After the success of Backrooms, it looks like A24 is trying to cash in on yet another internet horror craze with a new installment in the V/H/S horror anthology series set in the SCP Foundation univer"
  },
  {
    "id": "rss:https://www.theverge.com/tech/997322/resident-evil-steam-frame-fire-emblem-fortunes-weave",
    "domain": "大厂 AI 动态",
    "title": "A great new video game movie",
    "url": "https://www.theverge.com/tech/997322/resident-evil-steam-frame-fire-emblem-fortunes-weave",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T12:00:00+00:00",
    "summary": "Hi, friends! Welcome to Installer No. 144, your guide to the best and Verge-iest stuff in the world. (If you're new here, welcome, new tech season is here, and also you can read all the old editions a"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/997725/the-hidden-monopoly-behind-your-ti-graphing-calculator",
    "domain": "大厂 AI 动态",
    "title": "The hidden monopoly behind your TI graphing calculator",
    "url": "https://www.theverge.com/podcast/997725/the-hidden-monopoly-behind-your-ti-graphing-calculator",
    "source": "Verge Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T12:00:00+00:00",
    "summary": "The same calculator has been on most kids' back to school shopping list since the early 2000's and the dominance of Texas Instruments' calculator division goes back even farther. In the next episode o"
  },
  {
    "id": "rss:https://www.theverge.com/science/997834/ai-cyberattack-energy-critical-infrastructure",
    "domain": "大厂 AI 动态",
    "title": "Humans, not rogue AI, are still the biggest cybersecurity risk to energy systems",
    "url": "https://www.theverge.com/science/997834/ai-cyberattack-energy-critical-infrastructure",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T12:00:00+00:00",
    "summary": "Before recent high-profile hacks raised the specter of AI possibly \"killing all humans,\" our energy systems were already disturbingly vulnerable to cyberattack - and the risk is growing. \"We were alwa"
  },
  {
    "id": "rss:https://www.theverge.com/column/997843/streamers-cable-fast-channels",
    "domain": "大厂 AI 动态",
    "title": "All roads lead to cable",
    "url": "https://www.theverge.com/column/997843/streamers-cable-fast-channels",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T12:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more on streaming platforms, FAST channels, and the future of entertainment, follow Charles Pulliam"
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
    "id": "rss:https://techcrunch.com/2026/09/20/6-days-left-to-get-ahead-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "6 days left to save up to $200 to TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/20/6-days-left-to-get-ahead-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T21:41:08+00:00",
    "summary": "Current ticket pricing ends in 6 days on Sept. 25 at 11:59 p.m. PT. Join 10,000+ founders, investors and tech leaders at Disrupt and save up to $200 on your ticket until then."
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
    "summary": "Many of The Boring Company's announced project have not materialized."
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
    "summary": "On Equity, we debated whether Ai executives are serious about wanting to slow down."
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
    "summary": "Vocci's lightweight ring costs $249, and might pose some privacy questions"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/20/scrolled-wants-to-turn-textbooks-into-tiktok/",
    "domain": "大厂 AI 动态",
    "title": "ScrollEd wants to turn textbooks into TikTok",
    "url": "https://techcrunch.com/2026/09/20/scrolled-wants-to-turn-textbooks-into-tiktok/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T18:00:00+00:00",
    "summary": "ScrollEd turns textbooks into a scrollable, Instagram-like feed with video, audio, and quizzes. The Palo Alto startup, founded by student co-founders (and spouses) Utsav Gupta and Rebecca Neff, pitche"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/20/new-california-law-will-penalize-influencers-dont-disclose-political-ads/",
    "domain": "大厂 AI 动态",
    "title": "New California law will penalize influencers who don’t disclose political ads",
    "url": "https://techcrunch.com/2026/09/20/new-california-law-will-penalize-influencers-dont-disclose-political-ads/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T16:30:00+00:00",
    "summary": "The new legislation adds teeth to disclosure requirements for online influencers who are paid to post about politics."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/20/techcrunch-mobility-how-do-we-know-when-an-av-is-safe-enough/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: How do we know when an AV is safe enough?",
    "url": "https://techcrunch.com/2026/09/20/techcrunch-mobility-how-do-we-know-when-an-av-is-safe-enough/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T16:02:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, the role AI is playing in it. To get this in your inbox, sign up here for free — just click Tech"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/20/a-small-but-growing-number-of-founders-are-betting-that-bringing-people-together-is-its-own-industry/",
    "domain": "大厂 AI 动态",
    "title": "A small but growing number of founders are betting on bringing people together offline",
    "url": "https://techcrunch.com/2026/09/20/a-small-but-growing-number-of-founders-are-betting-that-bringing-people-together-is-its-own-industry/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T15:00:00+00:00",
    "summary": "On the surface, a game console and a leathercraft school don't appear to have much in common. But both founders think there's money in fostering the kind of connection that technology has eroded over "
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
    "summary": "Current ticket pricing ends Sept. 25 at 11:59 p.m. PT. Join 10,000+ founders, investors and tech leaders at Disrupt and save up to $200 on your ticket until then."
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
    "id": "rss:https://arstechnica.com/security/2026/09/an-undercover-google-analyst-infiltrated-a-notorious-supply-chain-hacking-gang/",
    "domain": "大厂 AI 动态",
    "title": "An undercover Google analyst infiltrated a notorious supply-chain hacking gang",
    "url": "https://arstechnica.com/security/2026/09/an-undercover-google-analyst-infiltrated-a-notorious-supply-chain-hacking-gang/",
    "source": "Andy Greenberg, WIRED.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T11:07:00+00:00",
    "summary": "Google’s threat intelligence group said it had a mole inside TeamPCP's inner circle."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/09/dont-call-it-an-suv-the-ferrari-purosangue-review/",
    "domain": "大厂 AI 动态",
    "title": "Don't call it an SUV: The Ferrari Purosangue review",
    "url": "https://arstechnica.com/cars/2026/09/dont-call-it-an-suv-the-ferrari-purosangue-review/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T10:00:02+00:00",
    "summary": "Unlike previous Ferrari four-seaters, this one is better for humans than cargo."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/09/t-rex-teeth-indicate-it-ran-as-warm-as-an-elephant/",
    "domain": "大厂 AI 动态",
    "title": "T. rex teeth indicate it ran as warm as an elephant",
    "url": "https://arstechnica.com/science/2026/09/t-rex-teeth-indicate-it-ran-as-warm-as-an-elephant/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T09:00:11+00:00",
    "summary": "Isotope ratios provide a hint that the giants were actively managing temperatures."
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
    "id": "rss:https://www.producthunt.com/products/google",
    "domain": "大厂 AI 动态",
    "title": "Google Flow for iOS & Android",
    "url": "https://www.producthunt.com/products/google",
    "source": "Chris Messina",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:12:23+00:00",
    "summary": "Google's AI creative studio now on mobile Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/omnidicom",
    "domain": "大厂 AI 动态",
    "title": "OmniDICOM",
    "url": "https://www.producthunt.com/products/omnidicom",
    "source": "Youngrak Choi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T03:53:39+00:00",
    "summary": "DICOM viewing and metadata editing on Mac and Windows Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/appgrowthkit",
    "domain": "大厂 AI 动态",
    "title": "AppGrowthKit",
    "url": "https://www.producthunt.com/products/appgrowthkit",
    "source": "Sarthak Gupta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-20T09:25:25+00:00",
    "summary": "Automate your App Store Screenshots and print money... Discussion | Link"
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
    "id": "hn:49778029",
    "domain": "金融",
    "title": "Samsung is expected to more than double output of its HBM4 and HBM4E DRAM",
    "url": "https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 463,
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
    "id": "rss:https://arxiv.org/abs/2609.21173",
    "domain": "金融",
    "title": "Adapting the Actor Model of Concurrency for High-Frequency Trading: Synchronous Message Delivery (fast_send) and a Tick-to-Book Latency Study",
    "url": "https://arxiv.org/abs/2609.21173",
    "source": "Vincent Maciejewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2609.21173v1 Announce Type: new Abstract: The actor model - state isolation, data-race freedom, deadlock resistance, and sequential single-message reasoning - has long been dismissed as unsuitab"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.21232",
    "domain": "金融",
    "title": "Stochastic Mortality Model with Fractional L\\'evy Dynamics",
    "url": "https://arxiv.org/abs/2609.21232",
    "source": "Congxin He, Lilian Hu, Yue Kuen Kwok, Yifan Ye",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2609.21232v1 Announce Type: new Abstract: A substantial body of empirical evidence suggests that stochastic mortality models ignoring long range dependence tend to underestimate life expectancy,"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.21271",
    "domain": "金融",
    "title": "Nested Clustered Optimization Is One End of a Schur Bridge, and the Interior Is Sometimes Provably Better",
    "url": "https://arxiv.org/abs/2609.21271",
    "source": "Peter Cotton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2609.21271v1 Announce Type: new Abstract: Nested clustered optimization allocates within each cluster from the cluster's own covariance block and then across the resulting cluster portfolios. Bl"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.21291",
    "domain": "金融",
    "title": "Efficient simulation schemes for pricing options under the Ornstein--Uhlenbeck driven stochastic volatility model",
    "url": "https://arxiv.org/abs/2609.21291",
    "source": "Congxin He, Yue Kuen Kwok",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2609.21291v1 Announce Type: new Abstract: We develop an efficient Monte Carlo simulation scheme for pricing options under the Ornstein-Uhlenbeck driven stochastic volatility model via the operat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.21301",
    "domain": "金融",
    "title": "Simulation of stochastic volatility models via operator splitting schemes",
    "url": "https://arxiv.org/abs/2609.21301",
    "source": "Lilian Hu, Congxin He, Yue Kuen Kwok, Gongqiu Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2609.21301v1 Announce Type: new Abstract: The standard Euler discretization schemes for numerical option pricing under stochastic volatility models are known to exhibit high biases and potential"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.21478",
    "domain": "金融",
    "title": "Bricks or Cash? Externalities of Housing Upgrading in High-density Cities",
    "url": "https://arxiv.org/abs/2609.21478",
    "source": "Sumit Agarwal, Ying Deng, Yi Fan, Qi Gao, Jing Li, Lin Ma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2609.21478v1 Announce Type: new Abstract: We estimate housing externalities in a high-density city, exploiting the staggered rollout of Singapore's nationwide Main Upgrading Programme for public"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.21684",
    "domain": "金融",
    "title": "Equilibrium prices under hidden Markov fundamentals",
    "url": "https://arxiv.org/abs/2609.21684",
    "source": "Henri Pag\\`es, Dylan Possama\\\"i, Mateo Rodriguez Polo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2609.21684v1 Announce Type: new Abstract: We study a representative-agent Epstein-Zin economy with geometric dividends and a hidden finite-state Markov drift. We allow the price-dividend ratio t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.22052",
    "domain": "金融",
    "title": "Design and pricing of a transparent parametric-modeled loss CAT bond: application to German windstorm",
    "url": "https://arxiv.org/abs/2609.22052",
    "source": "John Ery, Erwan Koch",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2609.22052v1 Announce Type: new Abstract: Catastrophe (cat) bonds overcome some lack of reinsurance by sourcing capacity from the wider capital markets. We present a new type of cat bond address"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.21688",
    "domain": "金融",
    "title": "Quadratic and $p$-th variation of random signed Takagi--Landsberg bridges",
    "url": "https://arxiv.org/abs/2609.21688",
    "source": "Purba Das, Alexander Schied",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2609.21688v1 Announce Type: cross Abstract: We study random signed Takagi--Landsberg bridges with independent Rademacher Faber--Schauder coefficients. At index $H=1/2$, we prove that every fixed"
  },
  {
    "id": "rss:https://arxiv.org/abs/2504.17468",
    "domain": "金融",
    "title": "Risk-minimizing reinsurance with adverse selection",
    "url": "https://arxiv.org/abs/2504.17468",
    "source": "Ka Chun Cheung, Sheung Chi Phillip Yam, Fei Lung Yuen, Yiying Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2504.17468v3 Announce Type: replace Abstract: This paper provides a comprehensive characterization of optimal reinsurance mechanisms under adverse selection when a monopolistic reinsurer faces a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.20674",
    "domain": "金融",
    "title": "The geometry of higher order modern portfolio theory",
    "url": "https://arxiv.org/abs/2511.20674",
    "source": "Emil Horobet",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2511.20674v2 Announce Type: replace Abstract: In this article, we study the generalized modern portfolio theory, with utility functions admitting higher-order cumulants. We establish that under "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08228",
    "domain": "金融",
    "title": "Post-Rejection Follow-up Sampling: Measuring Outcomes of Rejected Decisions in Algorithmic DEX Trading",
    "url": "https://arxiv.org/abs/2606.08228",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2606.08228v2 Announce Type: replace Abstract: Filter-gated algorithmic trading systems on decentralised exchanges reject most candidate tokens they evaluate, yet the observed forward market traj"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.10542",
    "domain": "金融",
    "title": "Optimal credit portfolio and consumption with regime switching and default contagion",
    "url": "https://arxiv.org/abs/2607.10542",
    "source": "Fei Sun, Wenyuan Wang, Kaixin Yan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2607.10542v2 Announce Type: replace Abstract: We study an optimal portfolio and consumption problem in a regime-switching multi-name credit market with default contagion. Default events not only"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.25353",
    "domain": "金融",
    "title": "The Risk-Neutral Crash Frontier: Sharp Joint Bounds on Crash Probability and Conditional Depth from Option Bid-Ask Quotes",
    "url": "https://arxiv.org/abs/2607.25353",
    "source": "Jirong Zhuang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2607.25353v4 Announce Type: replace Abstract: Index put prices are the market's quotes for crash insurance, and a put's value equals the probability of a crash times the expected shortfall given"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.07358",
    "domain": "金融",
    "title": "Access to Live AI Advice and Behavior Under Risk: An Incentivized Experiment",
    "url": "https://arxiv.org/abs/2609.07358",
    "source": "Paul Althaus, Leon Houf, Christiane Schwieren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2609.07358v2 Announce Type: replace Abstract: Generative AI has become an everyday advisor, and the systems people consult are live and interactive, not pre-scripted. We ask whether access to su"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.12666",
    "domain": "金融",
    "title": "Exact calibration of structural models via time-change",
    "url": "https://arxiv.org/abs/2609.12666",
    "source": "Fr\\'ed\\'eric Vrins, Damiano Brigo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2609.12666v2 Announce Type: replace Abstract: In this note, we propose a general structural approach to model a default time $\\tau$ as the first-passage time (FPT) of a (``firm-value'') process "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.14029",
    "domain": "金融",
    "title": "Special Markowitz: Thermodynamic Formalism for the Joint Regularisation of Returns and Covariance",
    "url": "https://arxiv.org/abs/2609.14029",
    "source": "David Reinhardt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2609.14029v3 Announce Type: replace Abstract: Special Markowitz (SM) regularises returns and covariance jointly, relative to a reference state (mu_ref, Sigma_ref). Each eigendirection of the whi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.19660",
    "domain": "金融",
    "title": "Screening Out the Needy: The Effects of SNAP Work Requirements",
    "url": "https://arxiv.org/abs/2609.19660",
    "source": "Lexin Cai, Hyewon Kim, Pauline Leung",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2609.19660v2 Announce Type: replace Abstract: We examine the effectiveness of work requirements as a screening device in the Supplemental Nutrition Assistance Program (SNAP). Work requirements f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.00853",
    "domain": "金融",
    "title": "Ranking Quantilized Mean-Field Games with an Application to Early-Stage Venture Investments",
    "url": "https://arxiv.org/abs/2507.00853",
    "source": "Rinel Foguen Tchuendom, Dena Firoozi, Mich\\`ele Breton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2507.00853v3 Announce Type: replace-cross Abstract: Quantilized mean-field game models involve quantiles of the population's distribution. We study a class of such games with a capacity for rank"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.21646",
    "domain": "金融",
    "title": "Stochastic Optimal Control of Interacting Particle Systems in Hilbert Spaces and Applications",
    "url": "https://arxiv.org/abs/2511.21646",
    "source": "Filippo de Feo, Fausto Gozzi, Andrzej \\'Swi\\k{e}ch, Lukas Wessels",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T04:00:00+00:00",
    "summary": "arXiv:2511.21646v2 Announce Type: replace-cross Abstract: Optimal control of interacting particles governed by stochastic evolution equations in Hilbert spaces is an open area of research. Such system"
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
