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

- 今日日期：`2026-06-23`
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
  "date": "2026-06-23",
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
    "id": "bvid:BV1DfrdByE2H",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！Agentic AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av115897075242856",
    "source": "吴恩达Agent",
    "platform": "bilibili",
    "points": 3353383,
    "published_at": "2026-01-15T03:56:12+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1262330,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1NvRyBzEhq",
    "domain": "AI",
    "title": "全网最全！60分钟全面掌握Claude Code～【附完整文档】",
    "url": "http://www.bilibili.com/video/av116522328524431",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1232182,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1221080,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 939147,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 752631,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 663884,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1mzFVzPEB6",
    "domain": "AI",
    "title": "（比刷剧爽！）2026公认最好的《Claude Code》教程，附课件代码—Claude Code探索-测试-重构-调试代码库",
    "url": "http://www.bilibili.com/video/av116005959505146",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 550975,
    "published_at": "2026-02-03T09:29:30+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1.使用 Claude 代码来探索、开发、测试、重构和调试代码库。\n2.使用 MCP 服务器（例如 Playwright 和 Figma MCP 服务器）扩展 Claude Code 的功能。\n3.将 Claude Code 最佳实践应用于三个项目：探索和开发 RAG 聊天机器人的代码库，重构电子商务数据的 Ju"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 488542,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 439236,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 414965,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 401728,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "domain": "AI",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 383478,
    "published_at": "2025-03-22T04:02:08+00:00",
    "summary": "很多人都想学编程,但被高门槛劝退。本期给大家介绍一款零门槛的AI编程工具-豆包电脑版。通过3个实战案例,带你体验如何用AI轻松实现编程。\n\n豆包电脑版特点:\n- 中文界面,所见即所得\n- 支持html代码预览\n- 支持Python运行\n- 可生成完整项目代码\n- 历史版本管理\n- 代码一键导出\n\n时间戳\n00:00 为什么要学AI编程\n03:19 案例1:图片压缩网站实战\n04:15 案例2:数据"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 375203,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1EduzzDEMM",
    "domain": "AI",
    "title": "Vibe Coding零基础教程，智能代码生成实战与原理解析。淘汰你的不是AI是另一个会Vibe Coding的人。Vibe Coding最新教程！",
    "url": "http://www.bilibili.com/video/av114852173515955",
    "source": "芝士好猫meme",
    "platform": "bilibili",
    "points": 329770,
    "published_at": "2025-07-14T15:01:39+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 246119,
    "published_at": "2026-04-04T15:19:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 241138,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 222249,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1kxLD6HEYN",
    "domain": "AI",
    "title": "Claude Code怎么全自动跑13小时？实测GLM 5.2开源天花板",
    "url": "http://www.bilibili.com/video/av116763920438810",
    "source": "小白debug",
    "platform": "bilibili",
    "points": 203519,
    "published_at": "2026-06-17T10:14:02+00:00",
    "summary": "我手搓了一个Openclaw"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 177086,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 175197,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 157505,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 145088,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 144363,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1j67k6oENA",
    "domain": "AI",
    "title": "Claude Ultracode 超码 上线 | 操控100个Agent并行开发  保姆级实战教程",
    "url": "http://www.bilibili.com/video/av116697163896598",
    "source": "技术胖",
    "platform": "bilibili",
    "points": 105210,
    "published_at": "2026-06-05T11:05:27+00:00",
    "summary": "Ultracode 功能太好用了，就是Claude Code昨天新出的“超码”功能，如果你Vibe Coding ，那这个技巧一定要掌握。他解决了Claude Code 一次性跑不完大型任务的问题。\n本期视频很长，但看完你的AI Coding能力将超越整个团队。并且把视频内容整理成了文字版，放在评论区，方便你学习使用。视频很干，可以先喝口水润润喉咙。"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 94736,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92224,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 90166,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73301,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 59971,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 55641,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 52299,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47180,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1fjcgzLE43",
    "domain": "AI",
    "title": "Claude 4.6最新功能，Claude Agent Teams 保姆级入门及使用教程",
    "url": "http://www.bilibili.com/video/av116040637941520",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 46173,
    "published_at": "2026-02-09T12:21:02+00:00",
    "summary": "本视频从四个方面介绍 claude agent teams 的使用：\n什么是 Claude Agent Teams\nClaude Agent Teams 跟 SubAgent 的区别是什么\nClaude Agent Teams 实战\nClaude Agent Teams 缺点及使用建议"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 39521,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 38663,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 36661,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1cCj2ztEf5",
    "domain": "AI",
    "title": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%",
    "url": "http://www.bilibili.com/video/av114574527307727",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 34656,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV1gwcAzkEhw",
    "domain": "AI",
    "title": "Claude Code Agent Teams上手指南+项目实测",
    "url": "http://www.bilibili.com/video/av116037064331269",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 34281,
    "published_at": "2026-02-08T23:30:00+00:00",
    "summary": "用Claude Code干复杂任务总碰到三个问题：\n\n上下文越来越长开始遗忘、任务只能串行效率低、单Agent视角单一容易漏检。\n\nClaude官方发布的Agent Teams功能正好解决这些痛点\n\n一个Team Lead拆任务，多个Teammate并行执行，还能互相通信协调。\n\n本期视频从核心概念、使用场景、底层架构到真实项目实战，带你完整搞懂Agent Teams的正确打开方式。"
  },
  {
    "id": "bvid:BV1ap2fBvEt9",
    "domain": "AI",
    "title": "如何使用「Operit AI」：你的下一代AI手机助手",
    "url": "http://www.bilibili.com/video/av115677243447909",
    "source": "默睦",
    "platform": "bilibili",
    "points": 32673,
    "published_at": "2025-12-07T08:06:42+00:00",
    "summary": "下载地址：https://github.com/AAswordman/Operit\n\n相关软件资料下载：https://www.123pan.com/s/IKgAjv-Hinsv.html\n\n官方交流群：458862019"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29758,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1EZd3BBEB5",
    "domain": "AI",
    "title": "手把手实战教学：我是如何用一个周末掌握Claude Code的",
    "url": "http://www.bilibili.com/video/av116539105739515",
    "source": "AliAbdaal",
    "platform": "bilibili",
    "points": 29369,
    "published_at": "2026-05-09T13:00:00+00:00",
    "summary": "朋友们，有个叫Claude Code的工具，过去两个月我用它做了很多事情，它真的改变了我的整个工作方式，而且我感觉到Claude Code让人与人之间的差距加速变大。。。这个视频做完我就要发给还没尝试过的亲友！\n看完这条视频，你会了解如何让AI采访你来生成AI工具点子，如何筛选高杠杆项目，如何一边制作工具一边学习AI知识和开发技术概念。你会意识到，在AI时代，你最大的资产也许就是好奇心和突破技术摩"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29356,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28667,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1FMEP6FE4S",
    "domain": "AI",
    "title": "2026 AI Agent哪家强？新手应该怎么选？",
    "url": "http://www.bilibili.com/video/av116692332187087",
    "source": "saysky96",
    "platform": "bilibili",
    "points": 27919,
    "published_at": "2026-06-04T14:38:26+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1mfJw6uE1Y",
    "domain": "AI",
    "title": "AI Agent 别乱选！2026 AI Agent 深度横评，普通人看完不踩坑｜OpenClaw、Codex、Hermes、WorkBuddy、Claude",
    "url": "http://www.bilibili.com/video/av116747361322195",
    "source": "AI实战派Pro",
    "platform": "bilibili",
    "points": 26623,
    "published_at": "2026-06-14T07:53:12+00:00",
    "summary": "《2026 主流 AI Agent 全维度对比｜OpenClaw / Codex / Claude Cowork / WorkBuddy / Hermes 怎么选？》\n\nHi，我是Alpha，我手把手带大家用AI提升自己工作、生活效率，提升个人竞争力以及用AI赚钱！一起做AI时代的主导者，而不是在焦虑中被AI淘汰！\n关注AI 实战派，让AI替你忙起来！\n\n本期视频介绍：《AI Agent 别乱选！"
  },
  {
    "id": "bvid:BV1hEVY6jEGT",
    "domain": "AI",
    "title": "最新【Claude pro Max】保姆级充值教程 Claude code国内购买教程 注册+订阅一个视频教会你",
    "url": "http://www.bilibili.com/video/av116657754277772",
    "source": "小轩AI-",
    "platform": "bilibili",
    "points": 22307,
    "published_at": "2026-05-29T12:07:14+00:00",
    "summary": "aipayok.com"
  },
  {
    "id": "bvid:BV1nf42127MW",
    "domain": "AI",
    "title": "用AI Agent做一个法律咨询助手，罗老看了都直呼内行 feat.通义千问大模型&amp;阿里云百炼平台",
    "url": "http://www.bilibili.com/video/av1204786228",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 21236,
    "published_at": "2024-05-21T05:09:48+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 19202,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17391,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "rss:https://www.eetimes.com/critical-components-for-reliable-factory-automation-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Critical Components for Reliable Factory Automation Design",
    "url": "https://www.eetimes.com/critical-components-for-reliable-factory-automation-design/",
    "source": "Same Sky and Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T17:15:13+00:00",
    "summary": "This webinar will provide a practical overview of product selection and implementation within factory automation applications. The post Critical Components for Reliable Factory Automation Design appea"
  },
  {
    "id": "rss:https://www.eetimes.com/globalfoundries-qualinx-put-europes-chip-sovereignty-to-the-fab-test/",
    "domain": "AI 算力 / 半导体",
    "title": "GlobalFoundries, Qualinx Put Europe’s Chip Sovereignty to the Fab Test",
    "url": "https://www.eetimes.com/globalfoundries-qualinx-put-europes-chip-sovereignty-to-the-fab-test/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T17:00:00+00:00",
    "summary": "GlobalFoundries and Qualinx deliver Europe's first fully secure chip supply chain. The post GlobalFoundries, Qualinx Put Europe’s Chip Sovereignty to the Fab Test appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/software-to-silicon-with-risc-v-for-physical-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Software to Silicon With RISC-V for Physical AI",
    "url": "https://www.eetimes.com/software-to-silicon-with-risc-v-for-physical-ai/",
    "source": "EE Times Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T14:13:07+00:00",
    "summary": "Discover how RISC-V is reshaping AI chip design—watch to see why it's becoming the default ISA. The post Software to Silicon With RISC-V for Physical AI appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/beyond-isolation-novosenses-isolation-platform-elevates-system-safety-for-advanced-power-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Beyond Isolation: NOVOSENSE’s Isolation+ Platform Elevates System Safety for Advanced Power Systems",
    "url": "https://www.eetimes.com/beyond-isolation-novosenses-isolation-platform-elevates-system-safety-for-advanced-power-systems/",
    "source": "Christopher McGrady",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T10:00:00+00:00",
    "summary": "Isolation+ is the strategic framework that unifies NOVOSENSE’s entire isolation portfolio. The post Beyond Isolation: NOVOSENSE&#8217;s Isolation+ Platform Elevates System Safety for Advanced Power Sy"
  },
  {
    "id": "rss:https://www.eetimes.com/securing-next-generation-defense-by-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Securing Next-Generation Defense by Design",
    "url": "https://www.eetimes.com/securing-next-generation-defense-by-design/",
    "source": "Daryl Flack",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T07:00:00+00:00",
    "summary": "In an environment of cloud platforms and AI models, security must be embedded into defense systems from the outset. The post Securing Next-Generation Defense by Design appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/get-this-asus-prime-rtx-5070-ti-for-just-usd900-our-pick-for-the-best-all-around-enthusiast-graphics-card-in-2026-hits-its-lowest-price-this-year",
    "domain": "AI 算力 / 半导体",
    "title": "Get this Asus Prime RTX 5070 Ti for just $900 — our pick for the best all-around enthusiast graphics card in 2026 hits its lowest price this year",
    "url": "https://www.tomshardware.com/pc-components/gpus/get-this-asus-prime-rtx-5070-ti-for-just-usd900-our-pick-for-the-best-all-around-enthusiast-graphics-card-in-2026-hits-its-lowest-price-this-year",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T21:39:01+00:00",
    "summary": "Asus' Prime RTX 5070 Ti graphics card is on sale for just $900 at Best Buy and Newegg, putting a high-end gaming upgrade in reach."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/the-motherboard-market-is-so-bad-that-flagship-boards-are-selling-at-entry-level-prices-save-up-to-57-percent-of-premium-motherboard-designs-while-ram-prices-surge",
    "domain": "AI 算力 / 半导体",
    "title": "The motherboard market is so bad that flagship boards are selling at entry-level prices — save up to 57% of premium motherboard designs while RAM prices surge",
    "url": "https://www.tomshardware.com/pc-components/motherboards/the-motherboard-market-is-so-bad-that-flagship-boards-are-selling-at-entry-level-prices-save-up-to-57-percent-of-premium-motherboard-designs-while-ram-prices-surge",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T20:38:04+00:00",
    "summary": "Motherboards are down to some unbelievable prices for Prime Day, which makes sense given how rough RAM prices are right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/servers/arm-servers-capture-over-45-percent-of-data-center-market-revenue-gpu-clusters-and-high-end-ai-infrastructure-fuel-a-tectonic-shift-away-from-x86",
    "domain": "AI 算力 / 半导体",
    "title": "Arm servers capture over 45% of data center market revenue — GPU clusters and high-end AI infrastructure fuel a tectonic shift away from x86",
    "url": "https://www.tomshardware.com/desktops/servers/arm-servers-capture-over-45-percent-of-data-center-market-revenue-gpu-clusters-and-high-end-ai-infrastructure-fuel-a-tectonic-shift-away-from-x86",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T20:34:17+00:00",
    "summary": "Arm-based servers accounted for nearly half of server revenue in Q1 2026, challenging x86. But in the coming years, they might catch up unit wise as well."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/this-usd1-089-msi-cyborg-15-gaming-laptop-sports-an-rtx-5070-and-1tb-ssd-32-percent-off-ahead-of-amazon-prime-day",
    "domain": "AI 算力 / 半导体",
    "title": "This $1,089 MSI Cyborg 15 gaming laptop sports an RTX 5070 and 1TB SSD — 32% off ahead of Amazon Prime Day",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/this-usd1-089-msi-cyborg-15-gaming-laptop-sports-an-rtx-5070-and-1tb-ssd-32-percent-off-ahead-of-amazon-prime-day",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T18:12:44+00:00",
    "summary": "The MSI Cyborg 15 is $1,089 at Walmart during Amazon Prime Day."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/valve-engineers-talk-steam-machine-pricing-and-the-benefits-of-massive-heatsinks-explain-why-valve-hardware-needs-to-be-a-self-sustained-program",
    "domain": "AI 算力 / 半导体",
    "title": "Valve engineers talk Steam Machine, pricing, and the benefits of massive heatsinks — explain why Valve hardware needs to be a 'self-sustained program'",
    "url": "https://www.tomshardware.com/video-games/console-gaming/valve-engineers-talk-steam-machine-pricing-and-the-benefits-of-massive-heatsinks-explain-why-valve-hardware-needs-to-be-a-self-sustained-program",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T18:00:00+00:00",
    "summary": "We talked to Valve engineers Pierre-Loup Griffais and Yazan Aldehayyat ahead of the Steam Machine's launch to learn more about its pricing, engineering, and how the company is handling availability."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/get-a-half-price-precision-electric-screwdriver-set-for-pc-builders-and-diyers-ultimate-prime-day-71-in-1-set-slashed-to-under-usd50",
    "domain": "AI 算力 / 半导体",
    "title": "Get a half-price precision electric screwdriver set for PC builders and DIYers — ultimate Prime Day 71-in-1 set slashed to under $50",
    "url": "https://www.tomshardware.com/desktops/pc-building/get-a-half-price-precision-electric-screwdriver-set-for-pc-builders-and-diyers-ultimate-prime-day-71-in-1-set-slashed-to-under-usd50",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T17:44:51+00:00",
    "summary": "The TanSon Precision Electric Screwdriver 71-in-1 cordless rechargeable 3.7V portable repair tool set has been slashed from $99.99 to $49.99 for Prime Day."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-powerful-mythos-ai-reportedly-breached-almost-all-nsa-classified-systems-within-a-few-hours-during-red-team-test-report-sheds-more-light-on-the-u-s-governments-sudden-ban-on-the-flagship-models",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic’s powerful Mythos AI reportedly breached ‘almost all’ NSA classified systems within a few hours during red-team test — report sheds more light on the U.S. government's sudden ban on the flag",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-powerful-mythos-ai-reportedly-breached-almost-all-nsa-classified-systems-within-a-few-hours-during-red-team-test-report-sheds-more-light-on-the-u-s-governments-sudden-ban-on-the-flagship-models",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T17:26:29+00:00",
    "summary": "Anthropic’s Mythos AI reportedly breached nearly all NSA classified systems during a controlled red-team test, according to a quote cited by The Economist. The report adds context to the U.S. governme"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/valve-steam-machine-review",
    "domain": "AI 算力 / 半导体",
    "title": "Valve Steam Machine review: Couch gaming unboxed, but not always at 4K",
    "url": "https://www.tomshardware.com/video-games/console-gaming/valve-steam-machine-review",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T17:00:00+00:00",
    "summary": "Valve's Steam Machine is nice box to play PC games on your TV, and is well-designed. But you're not getting the latest hardware, despite a starting price above $1,000."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/valve-opens-steam-machine-reservations-details-usd1-049-starting-price-randomized-queue-to-stop-scalpers-and-limited-inventory",
    "domain": "AI 算力 / 半导体",
    "title": "Valve opens Steam Machine reservations — details $1,049 starting price, randomized queue to stop scalpers, and limited inventory",
    "url": "https://www.tomshardware.com/video-games/console-gaming/valve-opens-steam-machine-reservations-details-usd1-049-starting-price-randomized-queue-to-stop-scalpers-and-limited-inventory",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T17:00:00+00:00",
    "summary": "In a blog post, Valve explained its new randomized reservation systems, new tactics to stop scalpers, and why it has limited inventory."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/amd-brings-official-fsr-4-1-support-to-rx-7000-series-gpus-int8-model-now-available-in-300-games-rdna-3-apus-also-getting-fsr-4-1-soon",
    "domain": "AI 算力 / 半导体",
    "title": "AMD brings official FSR 4.1 support to RX 7000 series GPUs — INT8 model now available in 300+ games, RDNA 3 APUs also getting FSR 4.1 soon",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/amd-brings-official-fsr-4-1-support-to-rx-7000-series-gpus-int8-model-now-available-in-300-games-rdna-3-apus-also-getting-fsr-4-1-soon",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T16:55:30+00:00",
    "summary": "If you own an RX 7000 series GPU, you can update your graphics driver today and enjoy native FSR 4.1 in over 300 games thanks to INT8 fallback."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/the-secret-to-building-a-pc-during-the-rampocalypse-are-bundles-here-are-some-of-the-best-ones-and-why-theyre-so-popular",
    "domain": "AI 算力 / 半导体",
    "title": "The secret to building a PC during the RAMpocalypse are bundles — here are some of the best ones, and why they're so popular",
    "url": "https://www.tomshardware.com/pc-components/cpus/the-secret-to-building-a-pc-during-the-rampocalypse-are-bundles-here-are-some-of-the-best-ones-and-why-theyre-so-popular",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T16:38:14+00:00",
    "summary": "PC component bundles are one of the few ways to still build a PC at a reasonable price. Here are some of the best deals, and why bundles are so popular."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-usd1-479-alienware-gaming-pc-features-an-rtx-5070-and-a-core-ultra-7-265f-cpu-4k-ready-aurora-desktop-is-up-to-usd850-off",
    "domain": "AI 算力 / 半导体",
    "title": "This $1,479 Alienware gaming PC features an RTX 5070 and a Core Ultra 7 265F CPU — 4K-ready Aurora desktop is up to $850 off",
    "url": "https://www.tomshardware.com/pc-components/this-usd1-479-alienware-gaming-pc-features-an-rtx-5070-and-a-core-ultra-7-265f-cpu-4k-ready-aurora-desktop-is-up-to-usd850-off",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T15:20:10+00:00",
    "summary": "Save 36% on this Alienware Aurora R16 system when configurating it with an RTX 5070, bringing it down from its original price of $2,330 to just $1,479, and that's with a free Lego Batman game."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/best-pc-tool-deals",
    "domain": "AI 算力 / 半导体",
    "title": "These are the best Prime Day deals I've found on tools I use to maintain my PC — from screwdrivers to air blowers, these tools will keep your PC in tip-top shape",
    "url": "https://www.tomshardware.com/desktops/pc-building/best-pc-tool-deals",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T15:03:31+00:00",
    "summary": "You really do need all of these tools to keep your electronics in good order, and luckily they are all on offer."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/ddr2-memory-prices-jump-up-to-60-percent",
    "domain": "AI 算力 / 半导体",
    "title": "2003-era DDR2 memory prices jump up to 60% — AI-driven DRAM shortage reaches the oldest standard still in production",
    "url": "https://www.tomshardware.com/pc-components/dram/ddr2-memory-prices-jump-up-to-60-percent",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T14:02:07+00:00",
    "summary": "DDR2 contract prices rose 55% to 60% in the second quarter of the year and are projected to climb another 35% to 40% in the third."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/quake-changed-gaming-forever-30-years-ago-today-seminal-title-established-online-multiplayer-culture-and-made-3d-graphics-accelerators-essential-pc-components",
    "domain": "AI 算力 / 半导体",
    "title": "Quake changed gaming forever 30 years ago today — seminal title established online multiplayer culture and made 3D graphics accelerators essential PC components",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/quake-changed-gaming-forever-30-years-ago-today-seminal-title-established-online-multiplayer-culture-and-made-3d-graphics-accelerators-essential-pc-components",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T13:53:11+00:00",
    "summary": "On this day in 1996, id Software unleashed Quake on the unsuspecting public. The game’s influence is difficult to overstate, with its pioneering 3D engine inspiring the first wave of 3D accelerator PC"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/massive-3d-printer-sales-bonanza-kicks-off-with-prime-day",
    "domain": "AI 算力 / 半导体",
    "title": "Massive 3D Printer sales bonanza kicks off with Prime Day — these are the best deals we've found so far",
    "url": "https://www.tomshardware.com/3d-printing/massive-3d-printer-sales-bonanza-kicks-off-with-prime-day",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T13:47:30+00:00",
    "summary": "There are some great 3D printer deals happening right now, and we've found the best and put them all into one page for you."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/one-of-the-best-looking-gaming-chairs-of-2026-is-more-than-half-price-ahead-of-prime-day-porsche-inspired-thermaltake-argent-e700-is-only-usd620-but-stock-is-low",
    "domain": "AI 算力 / 半导体",
    "title": "One of the best-looking gaming chairs of 2026 is less than half price ahead of Prime Day — Porsche-inspired Thermaltake Argent E700 is only $620, but stock is low",
    "url": "https://www.tomshardware.com/pc-components/one-of-the-best-looking-gaming-chairs-of-2026-is-more-than-half-price-ahead-of-prime-day-porsche-inspired-thermaltake-argent-e700-is-only-usd620-but-stock-is-low",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T13:19:02+00:00",
    "summary": "Made in collaboration with Studio F.A. Porsche, the Thermaltake Argent E700 combines genuine leather upholstery, polished aluminum accents, solid construction."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/anycubic-kobra-4-combo-3d-printer-review",
    "domain": "AI 算力 / 半导体",
    "title": "Anycubic Kobra 4 Combo 3D printer review: Evolution, not revolution",
    "url": "https://www.tomshardware.com/3d-printing/anycubic-kobra-4-combo-3d-printer-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T11:10:00+00:00",
    "summary": "The Kobra 4 Combo is a nice evolution of the Kobra 3 without any revolutionary changes."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/ludicrous-usd999-steam-game-lasts-just-10-minutes-congratulations-on-your-purchase-is-pure-conspicuous-consumption-with-its-golden-ticket-steam-achievement",
    "domain": "AI 算力 / 半导体",
    "title": "Ludicrous $999 Steam game lasts just 10 minutes — ‘Congratulations On Your Purchase’ is pure conspicuous consumption with its golden ticket Steam Achievement",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/ludicrous-usd999-steam-game-lasts-just-10-minutes-congratulations-on-your-purchase-is-pure-conspicuous-consumption-with-its-golden-ticket-steam-achievement",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T10:56:12+00:00",
    "summary": "'Congratulations On Your Purchase' recently appeared on PC digital marketplaces priced at $999. Its main claim to fame is that it is proudly 'the most expensive game on Steam.' Buyers get a golden tic"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/get-a-4tb-ssd-for-usd399-this-prime-day-9-7-cents-per-gb-is-as-good-as-it-gets-thanks-to-the-ai-pricing-crisis",
    "domain": "AI 算力 / 半导体",
    "title": "Get a 4TB SSD for $399 this Prime Day — 9.7 cents per GB is as good as it gets thanks to the AI pricing crisis",
    "url": "https://www.tomshardware.com/pc-components/ssds/get-a-4tb-ssd-for-usd399-this-prime-day-9-7-cents-per-gb-is-as-good-as-it-gets-thanks-to-the-ai-pricing-crisis",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T10:53:18+00:00",
    "summary": "Get a 4TB SSD for $399 ahead of Prime Day, the cheapest one you can buy."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/save-hundreds-during-this-storage-pricing-hellscape-by-turning-an-ssd-or-hard-drive-you-arent-using-into-a-useful-external-drive-for-as-little-as-usd8-put-an-old-drive-to-good-use-as-external-storage",
    "domain": "AI 算力 / 半导体",
    "title": "Save hundreds during this storage pricing hellscape by turning an SSD or hard drive you aren’t using into a useful external drive for as little as $8 – put an old drive to good use as external storage",
    "url": "https://www.tomshardware.com/pc-components/storage/save-hundreds-during-this-storage-pricing-hellscape-by-turning-an-ssd-or-hard-drive-you-arent-using-into-a-useful-external-drive-for-as-little-as-usd8-put-an-old-drive-to-good-use-as-external-storage",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T10:28:34+00:00",
    "summary": "Good storage deals are sadly dead, but an affordable enclosure can bring an old drive back to useful life."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/m3-macbook-air-plunges-to-usd799-in-early-amazon-prime-day-sale-38-percent-discount-blows-the-macbook-neo-out-of-the-water",
    "domain": "AI 算力 / 半导体",
    "title": "M3 MacBook Air plunges to $799 in early Amazon Prime Day sale — 38% discount blows the MacBook Neo out of the water",
    "url": "https://www.tomshardware.com/laptops/macbooks/m3-macbook-air-plunges-to-usd799-in-early-amazon-prime-day-sale-38-percent-discount-blows-the-macbook-neo-out-of-the-water",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T09:24:45+00:00",
    "summary": "The M3 MacBook Air from 2024 is now just $799 at Amazon."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/powerhouse-amd-ryzen-7-9800x3d-hits-record-low-price-at-amazon-uk-now-just-gbp339-99-get-one-of-our-favourite-gaming-cpus-with-its-game-changing-amd-3d-v-cache-technology",
    "domain": "AI 算力 / 半导体",
    "title": "Powerhouse AMD Ryzen 7 9800X3D hits record-low price at Amazon UK, now just £339.99 — get one of our favourite gaming CPUs with its game-changing AMD 3D V-cache technology",
    "url": "https://www.tomshardware.com/pc-components/cpus/powerhouse-amd-ryzen-7-9800x3d-hits-record-low-price-at-amazon-uk-now-just-gbp339-99-get-one-of-our-favourite-gaming-cpus-with-its-game-changing-amd-3d-v-cache-technology",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T08:00:05+00:00",
    "summary": "The AMD Ryzen 7 9800X3D has hit a record low Amazon UK price of £339.99, making it a must-buy option for any gaming PC build or upgrade."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/nintendo-switch-2-is-usd399-at-woot-for-new-customers-usd419-for-returning-customers-with-code-save-up-to-usd100-on-gaming-handheld-while-stocks-last",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo Switch 2 is $399 at Woot for new customers, $419 for returning customers with code — save up to $100 on gaming handheld while stocks last",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/nintendo-switch-2-is-usd399-at-woot-for-new-customers-usd419-for-returning-customers-with-code-save-up-to-usd100-on-gaming-handheld-while-stocks-last",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T07:42:42+00:00",
    "summary": "Get a brand new Nintendo Switch 2 for less."
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/amazon-prime-day-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Best Amazon Prime Day tech deals live — PC hardware deals on GPUs, CPUs, SSDs, and more",
    "url": "https://www.tomshardware.com/live/news/amazon-prime-day-2026",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T06:11:33+00:00",
    "summary": "Find the very best PC hardware deals during Amazon Prime Day."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooler-master-nr2-pro-mini-itx-system-packing-an-rtx-5080-is-usd400-off-in-newegg-deal-grab-a-compact-yet-powerful-liquid-cooled-gaming-pc-for-usd2-799-99",
    "domain": "AI 算力 / 半导体",
    "title": "Cooler Master NR2 Pro mini-ITX system packing an RTX 5080 is $400 off in Newegg deal — grab a compact yet powerful liquid cooled gaming PC for $2,799.99",
    "url": "https://www.tomshardware.com/pc-components/cooler-master-nr2-pro-mini-itx-system-packing-an-rtx-5080-is-usd400-off-in-newegg-deal-grab-a-compact-yet-powerful-liquid-cooled-gaming-pc-for-usd2-799-99",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T16:47:16+00:00",
    "summary": "The Cooler Master NR2 Pro combines a Gigabyte RTX 5080, Intel Core Ultra 7 265F, 2TB Gen 4.0 SSD, and the NR200P Max chassis into a compact gaming machine that can tackle 4K titles with ease."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/corsairs-tiny-touchscreen-display-is-on-sale-at-20-percent-off-ahead-of-prime-day-get-the-xeneon-edge-14-5-inch-lcd-touchscreen-for-just-usd199-99",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair’s tiny touchscreen display is on sale at 20% off ahead of Prime Day — get the Xeneon Edge 14.5-inch LCD touchscreen for just $199.99.",
    "url": "https://www.tomshardware.com/pc-components/corsairs-tiny-touchscreen-display-is-on-sale-at-20-percent-off-ahead-of-prime-day-get-the-xeneon-edge-14-5-inch-lcd-touchscreen-for-just-usd199-99",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T15:41:18+00:00",
    "summary": "Corsair just put a 20% discount on the 14.5-inch Xeneon Edge touchscreen display. This brings its price down to just $199.99, saving you $50 from its original purchase price."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/ingenious-modder-converts-countertop-ice-machine-into-an-rtx-3060-gpu-cooler-with-a-beer-fridge-thermostat-mod-reduces-temps-by-up-to-62-percent-in-games-cyberpunk-2077-runs-at-22-c",
    "domain": "AI 算力 / 半导体",
    "title": "Ingenious modder converts countertop ice machine into an RTX 3060 GPU cooler with a beer fridge thermostat — mod reduces temps by up to 62% in games, Cyberpunk 2077 runs at 22°C",
    "url": "https://www.tomshardware.com/pc-components/gpus/ingenious-modder-converts-countertop-ice-machine-into-an-rtx-3060-gpu-cooler-with-a-beer-fridge-thermostat-mod-reduces-temps-by-up-to-62-percent-in-games-cyberpunk-2077-runs-at-22-c",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T14:40:14+00:00",
    "summary": "Turns out, an ice machine can cool a GPU perfectly fine as long as you're willing to modify it to the extreme and are patient enough to deal with the leaks."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/open-source-nvidia-vulkan-driver-nvk-gains-experimental-dlss-support-by-importing-pre-baked-cuda-binaries",
    "domain": "AI 算力 / 半导体",
    "title": "Open-source Vulkan driver NVK gains experimental DLSS support — bringing Nvidia’s upscaling tech to Linux via imported CUDA binaries",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/open-source-nvidia-vulkan-driver-nvk-gains-experimental-dlss-support-by-importing-pre-baked-cuda-binaries",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T14:27:19+00:00",
    "summary": "NVK, the community-built open-source Vulkan driver for Nvidia GPUs in Mesa, has gained experimental DLSS support."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/ubisoft-co-founder-claude-guillemot-dies-in-plane-crash-french-publisher-established-in-1986-became-one-of-the-biggest-entertainment-companies-in-the-world",
    "domain": "AI 算力 / 半导体",
    "title": "Ubisoft co-founder Claude Guillemot dies in plane crash — French publisher established in 1986 became one of the biggest entertainment companies in the world",
    "url": "https://www.tomshardware.com/video-games/ubisoft-co-founder-claude-guillemot-dies-in-plane-crash-french-publisher-established-in-1986-became-one-of-the-biggest-entertainment-companies-in-the-world",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T14:04:20+00:00",
    "summary": "Ubisoft co-founder Claude Guillemot was killed when his twin-engine private plane crashed enroute to an airshow. Aside from building the French gaming empire, Guillemot was also a licensed and avid pi"
  },
  {
    "id": "rss:https://www.eetimes.com/defense-sends-clear-signal-to-canadian-semiconductor-industry/",
    "domain": "AI 算力 / 半导体",
    "title": "Defense Sends Clear Signal to Canadian Semiconductor Industry",
    "url": "https://www.eetimes.com/defense-sends-clear-signal-to-canadian-semiconductor-industry/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T22:00:00+00:00",
    "summary": "Canada sharpens its defense and tech edge with policies to boost homegrown chip power. The post Defense Sends Clear Signal to Canadian Semiconductor Industry appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/amazon-newest-gambit-selling-ai-chips/",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon’s Newest Gambit: Selling AI Chips",
    "url": "https://www.eetimes.com/amazon-newest-gambit-selling-ai-chips/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T12:19:36+00:00",
    "summary": "The world’s largest hyperscaler wants to seize the semiconductor moment by selling AI accelerators at scale. The post Amazon’s Newest Gambit: Selling AI Chips appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/all-semiconductor-roads-lead-to-taiwan/",
    "domain": "AI 算力 / 半导体",
    "title": "All Semiconductor Roads Lead to Taiwan",
    "url": "https://www.eetimes.com/all-semiconductor-roads-lead-to-taiwan/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T07:45:00+00:00",
    "summary": "Small in size but outsized in influence, Taiwan has become a linchpin of the global semiconductor supply chain. The post All Semiconductor Roads Lead to Taiwan appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/billions-pour-into-autonomous-defense-as-ai-redefines-warfare/",
    "domain": "AI 算力 / 半导体",
    "title": "Billions Pour into Autonomous Defense as AI Redefines Warfare",
    "url": "https://www.eetimes.com/billions-pour-into-autonomous-defense-as-ai-redefines-warfare/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T19:09:37+00:00",
    "summary": "Record investment is accelerating autonomous military tech, putting edge AI and drones at the center of modern conflict. The post Billions Pour into Autonomous Defense as AI Redefines Warfare appeared"
  },
  {
    "id": "rss:https://www.eetimes.com/the-new-software-standard-for-physical-ai-insert-return-here-for-new-line-accelerating-development-and-deployment-from-months-to-days/",
    "domain": "AI 算力 / 半导体",
    "title": "The New Software Standard for Physical AI",
    "url": "https://www.eetimes.com/the-new-software-standard-for-physical-ai-insert-return-here-for-new-line-accelerating-development-and-deployment-from-months-to-days/",
    "source": "Manuel Roldan, Software Product Manager, SiMa.ai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T14:00:00+00:00",
    "summary": "Building real-time physical AI applications—such as high-performance, multimodal object tracking for autonomous systems within a constrained power envelope—is notoriously difficult. It requires coordi"
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/16/xais-colossus-2-first-gigawatt-datacenter/",
    "domain": "AI 算力 / 半导体",
    "title": "xAI’s Colossus 2 – First Gigawatt Datacenter In The World, Unique RL Methodology, Capital Raise",
    "url": "https://semianalysis.com/2025/09/16/xais-colossus-2-first-gigawatt-datacenter/",
    "source": "Jeremie Eliahou Ontiveros",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-16T17:38:01+00:00",
    "summary": "Much has been written about xAI’s Colossus 1. The Memphis build belongs in the history books: the largest AI training cluster, erected from scratch in 122 days. With roughly 200,000 H100/H200s and ~30"
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/10/another-giant-leap-the-rubin-cpx-specialized-accelerator-rack/",
    "domain": "AI 算力 / 半导体",
    "title": "Another Giant Leap: The Rubin CPX Specialized Accelerator & Rack",
    "url": "https://semianalysis.com/2025/09/10/another-giant-leap-the-rubin-cpx-specialized-accelerator-rack/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-10T19:57:18+00:00",
    "summary": "Nvidia announced the Rubin CPX, a solution that is specifically designed to be optimized for the prefill phase, with the single-die Rubin CPX heavily emphasizing compute FLOPS over memory bandwidth. T"
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/08/huawei-ascend-production-ramp/",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei Ascend Production Ramp: Die Banks, TSMC Continued Production, HBM is The Bottleneck",
    "url": "https://semianalysis.com/2025/09/08/huawei-ascend-production-ramp/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-08T09:54:57+00:00",
    "summary": "Compute is the lifeblood of AI. He who controls the spice controls the universe the compute will control the production of tokens and reap the benefits of AI. Without compute you do not have a seat at"
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/03/amazons-ai-resurgence-aws-anthropics-multi-gigawatt-trainium-expansion/",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon’s AI Resurgence: AWS & Anthropic’s Multi-Gigawatt Trainium Expansion",
    "url": "https://semianalysis.com/2025/09/03/amazons-ai-resurgence-aws-anthropics-multi-gigawatt-trainium-expansion/",
    "source": "Jeremie Eliahou Ontiveros",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-03T20:55:46+00:00",
    "summary": "Two-and-a-half years ago, we flagged a looming “cloud crisis” at AWS. Today, the evidence has mounted. AWS is the crown jewel of the Amazon empire, generating ~60% of group profits, and dominating the"
  },
  {
    "id": "rss:https://semianalysis.com/2025/08/20/h100-vs-gb200-nvl72-training-benchmarks/",
    "domain": "AI 算力 / 半导体",
    "title": "H100 vs GB200 NVL72 Training Benchmarks – Power, TCO, and Reliability Analysis, Software Improvement Over Time",
    "url": "https://semianalysis.com/2025/08/20/h100-vs-gb200-nvl72-training-benchmarks/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-20T04:56:35+00:00",
    "summary": "Frontier model training has pushed GPUs and AI systems to their absolute limits, making cost, efficiency, power, performance per TCO, and reliability central to the discussion on effective training. T"
  },
  {
    "id": "rss:https://semianalysis.com/2025/08/13/gpt-5-ad-monetization-and-the-superapp/",
    "domain": "AI 算力 / 半导体",
    "title": "GPT-5 Set the Stage for Ad Monetization and the SuperApp",
    "url": "https://semianalysis.com/2025/08/13/gpt-5-ad-monetization-and-the-superapp/",
    "source": "Doug OLaughlin",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-13T00:27:14+00:00",
    "summary": "To many power users (Pro and Plus), GPT5 was a disappointing release. But with closer inspection, the real release is focused on the vast majority of ChatGPT’s users, which is the 700m+ free userbase "
  },
  {
    "id": "rss:https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/",
    "domain": "AI 算力 / 半导体",
    "title": "Scaling the Memory Wall: The Rise and Roadmap of HBM",
    "url": "https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-12T01:16:06+00:00",
    "summary": "The first portion of this report will explain HBM, the manufacturing process, dynamics between vendors, KVCache offload, disaggregated prefill decode, and wide / high-rank EP. The rest of the report w"
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/30/robotics-levels-of-autonomy/",
    "domain": "AI 算力 / 半导体",
    "title": "Robotics Levels of Autonomy",
    "url": "https://semianalysis.com/2025/07/30/robotics-levels-of-autonomy/",
    "source": "Reyk Knuhtsen",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-30T17:02:25+00:00",
    "summary": "Robots have powered manufacturing for decades, yet they stayed single-purpose and thrived only in perfect settings. Previous attempts at intelligent machines overpromised and underdelivered. But they "
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/21/vlsi2025/",
    "domain": "AI 算力 / 半导体",
    "title": "Intel 18A Details & Cost, Future of DRAM 4F2 vs 3D, Backside Power Adoption (or Not), China’s FlipFET, Digital Twins from Atoms to Fabs, and More",
    "url": "https://semianalysis.com/2025/07/21/vlsi2025/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-21T14:23:37+00:00",
    "summary": "Long time readers will recall that SemiAnalysis covers more than just datacenters and AMD. Today we’re back to semiconductors with a tech-focused roundup of the best from this year’s VLSI conference, "
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/11/meta-superintelligence-leadership-compute-talent-and-data/",
    "domain": "AI 算力 / 半导体",
    "title": "Meta Superintelligence – Leadership Compute, Talent, and Data",
    "url": "https://semianalysis.com/2025/07/11/meta-superintelligence-leadership-compute-talent-and-data/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-11T20:12:19+00:00",
    "summary": "Meta’s shocking purchase of 49% of Scale AI at a ~$30B valuation shows that money is of no concern for the $100B annual cashflow ad machine. Despite seemingly unlimited resources, Meta has been fallin"
  },
  {
    "id": "rss:https://www.theverge.com/tech/954139/nvidia-data-centers-rubin-liquid-cooling",
    "domain": "大厂 AI 动态",
    "title": "Nvidia says its AI data center design runs hotter to use a lot less water",
    "url": "https://www.theverge.com/tech/954139/nvidia-data-centers-rubin-liquid-cooling",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T23:24:32+00:00",
    "summary": "Public pushback against data centers has emphasized their water and energy consumption, and now Nvidia is highlighting its claim that the Rubin generation reference design for a fully liquid-cooled da"
  },
  {
    "id": "rss:https://www.theverge.com/games/953945/valve-steam-machine-memory-component-crisis",
    "domain": "大厂 AI 动态",
    "title": "Valve describes just how brutal RAM negotiations are in 2026",
    "url": "https://www.theverge.com/games/953945/valve-steam-machine-memory-component-crisis",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T21:07:14+00:00",
    "summary": "Valve's Steam Machine finally has a price: a whopping $1,049 for the 512GB configuration or $1,349 for the 2TB version. And those are without bundled controllers, which drive up the cost more. The pri"
  },
  {
    "id": "rss:https://www.theverge.com/report/953888/ai-virtual-staging-real-estate-apartment-listings",
    "domain": "大厂 AI 动态",
    "title": "AI is cursing renters with the promise of impossible homes",
    "url": "https://www.theverge.com/report/953888/ai-virtual-staging-real-estate-apartment-listings",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T20:00:00+00:00",
    "summary": "Joyce, a native New Yorker, didn't think finding her first solo apartment in the city would be easy. But she also didn't think it'd be \"hell.\" After looking at a lot of tiny, overpriced places she des"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/953458/apple-watch-se-3-prime-day-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The Apple Watch SE 3 is just $199 for Prime Day",
    "url": "https://www.theverge.com/gadgets/953458/apple-watch-se-3-prime-day-deal-sale",
    "source": "Victoria Song",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T18:00:00+00:00",
    "summary": "The Apple Watch SE 3 is at an all-time low of $199, making the sleeper hit of last year’s Apple Watches an even better value. While the Series 11 and Ultra 3 were iterative updates, the SE 3 was a wid"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/953615/steam-machine-price-game-consoles-future-ps6-project-helix",
    "domain": "大厂 AI 动态",
    "title": "The Steam Machine is the start of an even more expensive future for game consoles",
    "url": "https://www.theverge.com/entertainment/953615/steam-machine-price-game-consoles-future-ps6-project-helix",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T18:00:00+00:00",
    "summary": "It's no secret that just about every aspect of video games is getting more expensive. Game consoles are getting regular price hikes, PC components are spiking in cost, and the golden age of affordable"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/953596/google-deepmind-a24-studio-ai-partnership",
    "domain": "大厂 AI 动态",
    "title": "Google invests in A24 to build AI movie tools",
    "url": "https://www.theverge.com/entertainment/953596/google-deepmind-a24-studio-ai-partnership",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T17:18:13+00:00",
    "summary": "Google's DeepMind AI lab is teaming up with A24 to develop new movie production technologies that aim to help future filmmakers \"expand their storytelling possibilities.\" As part of this new research "
  },
  {
    "id": "rss:https://www.theverge.com/games/952210/valve-steam-machine-fsr4-amd-upscaler",
    "domain": "大厂 AI 动态",
    "title": "Valve is working with AMD to bring FSR 4 to the Steam Machine",
    "url": "https://www.theverge.com/games/952210/valve-steam-machine-fsr4-amd-upscaler",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T17:10:00+00:00",
    "summary": "The Steam Machine is a cool little console that's about as powerful as a PlayStation 5, according to my colleague Sean Hollister's in-depth review. But one area where it lags behind is with its earlie"
  },
  {
    "id": "rss:https://www.theverge.com/games/952191/valve-steam-machine-reservation-preorder-process",
    "domain": "大厂 AI 动态",
    "title": "Here’s how you can reserve a Steam Machine",
    "url": "https://www.theverge.com/games/952191/valve-steam-machine-reservation-preorder-process",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T17:07:01+00:00",
    "summary": "The Steam Machine is here, but getting one is a little complicated. Valve is taking preorders using a reservation system, which is intended to make the process more fair and harder for bots to exploit"
  },
  {
    "id": "rss:https://www.theverge.com/games/953411/valve-steamos-desktop-nvidia",
    "domain": "大厂 AI 动态",
    "title": "Valve will finally let you build your own Steam Machine with SteamOS for desktop",
    "url": "https://www.theverge.com/games/953411/valve-steamos-desktop-nvidia",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T17:05:00+00:00",
    "summary": "If you don't get lucky with Valve's Steam Machine reservation system, you can make your own Steam Machine instead. Valve says that \"starting with the SteamOS 3.8 release, you can put together your own"
  },
  {
    "id": "rss:https://www.theverge.com/games/952004/valve-steam-machine-price-not-subsidizing",
    "domain": "大厂 AI 动态",
    "title": "Valve explains why it isn&#8217;t subsidizing the Steam Machine",
    "url": "https://www.theverge.com/games/952004/valve-steam-machine-price-not-subsidizing",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T17:02:00+00:00",
    "summary": "Valve finally announced the price of the Steam Machine, and like a lot of new gadgets these days, it's not cheap: It starts at $1,049 for a 512GB model, and a 2TB model costs $300 more. Configurations"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/",
    "domain": "大厂 AI 动态",
    "title": "The running list: major tech layoffs in 2026 where employers cited AI",
    "url": "https://techcrunch.com/2026/06/22/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/",
    "source": "Rebecca Bellan, Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T01:27:55+00:00",
    "summary": "A running look — in reverse chronological order — at the bigger tech companies that have announced significant layoffs this year with AI as a stated factor."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/openai-launches-new-initiative-to-help-find-and-patch-open-source-bugs/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI launches new initiative to help find and patch open source bugs",
    "url": "https://techcrunch.com/2026/06/22/openai-launches-new-initiative-to-help-find-and-patch-open-source-bugs/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T00:11:31+00:00",
    "summary": "OpenAI is using AI to help the open source community better protect itself."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/tesla-pushes-back-on-autopilot-narrative-after-fatal-texas-crash/",
    "domain": "大厂 AI 动态",
    "title": "Tesla pushes back on Autopilot narrative after fatal Texas crash",
    "url": "https://techcrunch.com/2026/06/22/tesla-pushes-back-on-autopilot-narrative-after-fatal-texas-crash/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T22:59:57+00:00",
    "summary": "Whether the Autopilot system was truly active, overridden, or malfunctioning likely won't be resolved until investigators finish combing through the vehicle's data logs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/shareholders-sue-ubers-board-over-sexual-assaults-other-incidents/",
    "domain": "大厂 AI 动态",
    "title": "Shareholders sue Uber’s board over sexual assaults, other incidents",
    "url": "https://techcrunch.com/2026/06/22/shareholders-sue-ubers-board-over-sexual-assaults-other-incidents/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T22:43:12+00:00",
    "summary": "The lawsuit, led by a Detroit pension fund, alleges Uber's board and management has cut too many compliance corners, resulting in thousands of lawsuits."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/the-ai-world-is-getting-loopy/",
    "domain": "大厂 AI 动态",
    "title": "The AI world is getting ‘loopy’",
    "url": "https://techcrunch.com/2026/06/22/the-ai-world-is-getting-loopy/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T20:53:11+00:00",
    "summary": "The loop takes agentic AI a step further by authorizing a swarm of agents to work continuously in the background, endlessly."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/microsoft-and-chevron-plan-one-of-the-largest-gas-powered-data-center-projects-in-us/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft and Chevron plan one of the largest gas-powered data center projects in US",
    "url": "https://techcrunch.com/2026/06/22/microsoft-and-chevron-plan-one-of-the-largest-gas-powered-data-center-projects-in-us/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T20:37:19+00:00",
    "summary": "Microsoft inked a 20-year power purchase agreement with Chevron, locking in decades of carbon emissions from a new natural gas power plant."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/ai-chipmaker-groq-confirms-650m-raise-re-staffs-after-nvidias-20b-not-acqui-hire-deal/",
    "domain": "大厂 AI 动态",
    "title": "AI chipmaker Groq confirms $650M raise, re-staffs after Nvidia’s $20B not-acqui-hire deal",
    "url": "https://techcrunch.com/2026/06/22/ai-chipmaker-groq-confirms-650m-raise-re-staffs-after-nvidias-20b-not-acqui-hire-deal/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T20:13:58+00:00",
    "summary": "What does an AI company do after one of those not-acqui-hire deals? Groq raised money, is leaning into its neocloud business, and is hiring new execs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/nvidia-wants-to-cut-data-center-water-use-but-thats-not-the-same-as-fixing-ais-water-problem/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia wants to cut data center water use, but that’s not the same as fixing AI’s water problem",
    "url": "https://techcrunch.com/2026/06/22/nvidia-wants-to-cut-data-center-water-use-but-thats-not-the-same-as-fixing-ais-water-problem/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T20:08:15+00:00",
    "summary": "Nvidia announced a new cooling system that cuts water use inside the data center. But it does nothing to address AI's biggest water use — fossil fuel power plants."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/tata-electronics-a-major-tech-supplier-to-apple-and-tesla-confirms-data-breach/",
    "domain": "大厂 AI 动态",
    "title": "Tata Electronics, a major tech supplier to Apple and Tesla, confirms data breach",
    "url": "https://techcrunch.com/2026/06/22/tata-electronics-a-major-tech-supplier-to-apple-and-tesla-confirms-data-breach/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T19:25:00+00:00",
    "summary": "The incident comes as Tata Electronics expands its role in global technology supply chains."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/a-new-unpatchable-flaw-in-apple-chips-opens-the-door-to-an-iphone-jailbreak/",
    "domain": "大厂 AI 动态",
    "title": "A new unpatchable flaw in Apple chips opens the door to an iPhone jailbreak",
    "url": "https://techcrunch.com/2026/06/22/a-new-unpatchable-flaw-in-apple-chips-opens-the-door-to-an-iphone-jailbreak/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T18:50:24+00:00",
    "summary": "European offensive cybersecurity company Paradigm Shift released details of a flaw and a technique to exploit it that opens the door for hackers to unlock and break into older iPhones."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/google-deepmind-bets-75m-on-ais-future-in-hollywood-with-a24-deal/",
    "domain": "大厂 AI 动态",
    "title": "Google DeepMind bets $75M on AI’s future in Hollywood with A24 deal",
    "url": "https://techcrunch.com/2026/06/22/google-deepmind-bets-75m-on-ais-future-in-hollywood-with-a24-deal/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T18:49:44+00:00",
    "summary": "Google DeepMind and A24 are teaming up to build AI filmmaking tools."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/anthropic-says-claude-may-want-to-see-your-id/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic says Claude may want to see your ID",
    "url": "https://techcrunch.com/2026/06/22/anthropic-says-claude-may-want-to-see-your-id/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T18:05:13+00:00",
    "summary": "Claude's chatbot may ask to verify your age and identity \"in certain circumstances,\" such as with a passport or driver's license, according to a privacy policy change."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/amazon-is-testing-alexa-in-india-with-hindi-support/",
    "domain": "大厂 AI 动态",
    "title": "Amazon is testing Alexa+ in India with Hindi support",
    "url": "https://techcrunch.com/2026/06/22/amazon-is-testing-alexa-in-india-with-hindi-support/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T17:31:29+00:00",
    "summary": "Amazon is planning to increase the footprint of its new conversational AI assistant Alexa+ to India and is inviting users in the country to test out a Hindi-language version."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/spacex-inks-compute-deal-with-reflection-ai-an-open-source-ai-lab/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX inks compute deal with Reflection AI, an open source AI lab",
    "url": "https://techcrunch.com/2026/06/22/spacex-inks-compute-deal-with-reflection-ai-an-open-source-ai-lab/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T16:51:29+00:00",
    "summary": "Reflection AI will pay $150 million a month beginning July 1, 2026 through 2029 for immediate access to Nvidia's latest GB300 AI chips and supporting hardware across SpaceX's Colossus 2 data center ne"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/whatsapp-gets-new-chief-as-meta-taps-indias-cred-founder-kunal-shah-and-invests-900m-in-startup/",
    "domain": "大厂 AI 动态",
    "title": "WhatsApp gets new chief as Meta taps India’s CRED founder Kunal Shah and invests $900M in startup",
    "url": "https://techcrunch.com/2026/06/22/whatsapp-gets-new-chief-as-meta-taps-indias-cred-founder-kunal-shah-and-invests-900m-in-startup/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T15:21:42+00:00",
    "summary": "WhatsApp gets a new boss, as Will Cathcart moves to a new role at Meta, while Shah steps down as CEO of Indian fintech giant CRED to replace Cathcart."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/instagram-looks-to-take-on-streaming-services-with-longer-form-episodic-and-live-formats-for-its-tv-app/",
    "domain": "大厂 AI 动态",
    "title": "Instagram looks to take on streaming services with longer-form, episodic and live formats for its TV app",
    "url": "https://techcrunch.com/2026/06/22/instagram-looks-to-take-on-streaming-services-with-longer-form-episodic-and-live-formats-for-its-tv-app/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T14:14:10+00:00",
    "summary": "Instagram is coming for streaming services like Netflix and Amazon Prime Video as it sets its ambitions for living room viewing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/the-founder-conference-built-for-growth-techcrunch-founder-summit-pass-rates-increase-june-26/",
    "domain": "大厂 AI 动态",
    "title": "The founder conference built for growth: TechCrunch Founder Summit pass rates increase June 26",
    "url": "https://techcrunch.com/2026/06/22/the-founder-conference-built-for-growth-techcrunch-founder-summit-pass-rates-increase-june-26/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T14:00:00+00:00",
    "summary": "Save up to $190 on your pass to TechCrunch Founder Summit 2026 by June 26, 11:59 p.m. PT. Designed for founders first on November 4 in Boston. Register today."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/lucid-motors-new-ceo-cuts-18-of-staff-to-simplify-the-company/",
    "domain": "大厂 AI 动态",
    "title": "Lucid Motors’ new CEO cuts 18% of staff to ‘simplify the company’",
    "url": "https://techcrunch.com/2026/06/22/lucid-motors-new-ceo-cuts-18-of-staff-to-simplify-the-company/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T13:42:59+00:00",
    "summary": "The company is also eliminating a production shift at its Arizona factory to align \"production plans with anticipated demand.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/seedcamp-raises-320m-for-its-new-fund-to-expand-its-us-footprint/",
    "domain": "大厂 AI 动态",
    "title": "Seedcamp raises $320M for its new fund to expand its US footprint",
    "url": "https://techcrunch.com/2026/06/22/seedcamp-raises-320m-for-its-new-fund-to-expand-its-us-footprint/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T13:37:25+00:00",
    "summary": "After 18 years of focusing on Europe, early-stage investor Seedcamp said that it has raised $320 million for its latest fund, which will see it expanding its presence in the United States."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/klue-hack-results-in-data-breach-at-several-cybersecurity-firms/",
    "domain": "大厂 AI 动态",
    "title": "Klue hack results in data breach at several cybersecurity firms",
    "url": "https://techcrunch.com/2026/06/22/klue-hack-results-in-data-breach-at-several-cybersecurity-firms/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T13:36:08+00:00",
    "summary": "Huntress, HackerOne, Jamf, Recorded Future, and Tanium are among the cybersecurity companies that had data stolen following an earlier breach at market research firm Klue."
  },
  {
    "id": "rss:https://stratechery.com/2026/apple-price-increases-apple-intelligence-and-the-e-u/",
    "domain": "大厂 AI 动态",
    "title": "Apple Price Increases, Apple Intelligence and the E.U.",
    "url": "https://stratechery.com/2026/apple-price-increases-apple-intelligence-and-the-e-u/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T10:00:00+00:00",
    "summary": "Apple is (finally) raising prices, but they're not shipping Siri AI to the E.U."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/with-starfall-spacex-eyes-an-edge-in-global-cargo-delivery-from-orbit/",
    "domain": "大厂 AI 动态",
    "title": "With Starfall, SpaceX eyes an edge in global cargo delivery from orbit",
    "url": "https://arstechnica.com/space/2026/06/with-starfall-spacex-eyes-an-edge-in-global-cargo-delivery-from-orbit/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T05:25:16+00:00",
    "summary": "The purpose of Starfall is to support the \"transport and delivery of goods through space.\""
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/gm-installs-robots-at-flagship-ev-factory-after-laying-off-1300-workers/",
    "domain": "大厂 AI 动态",
    "title": "GM installs robots at flagship EV factory after laying off 1,300 workers",
    "url": "https://arstechnica.com/ai/2026/06/gm-installs-robots-at-flagship-ev-factory-after-laying-off-1300-workers/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T21:52:39+00:00",
    "summary": "US autoworkers union warns of robot automation as dark factory future looms."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/report-kennedy-space-center-not-ready-for-era-of-super-heavy-rockets/",
    "domain": "大厂 AI 动态",
    "title": "Report: Kennedy Space Center not ready for era of super heavy rockets",
    "url": "https://arstechnica.com/space/2026/06/report-kennedy-space-center-not-ready-for-era-of-super-heavy-rockets/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T21:28:19+00:00",
    "summary": "SpaceX has told NASA it plans to launch Starship every eight days from Kennedy."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/06/man-used-massage-gun-on-his-tired-eyeballs-it-went-as-well-as-youd-expect/",
    "domain": "大厂 AI 动态",
    "title": "Man used massage gun on his tired eyeballs. It went as well as you'd expect.",
    "url": "https://arstechnica.com/health/2026/06/man-used-massage-gun-on-his-tired-eyeballs-it-went-as-well-as-youd-expect/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T21:02:08+00:00",
    "summary": "He had retinal tears and bruises from squishing his eyeballs with the gun."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/polymarkets-viral-videos-showed-people-winning-big-but-the-bets-were-fake/",
    "domain": "大厂 AI 动态",
    "title": "Polymarket's viral videos showed people winning big, but the bets were fake",
    "url": "https://arstechnica.com/tech-policy/2026/06/polymarkets-viral-videos-showed-people-winning-big-but-the-bets-were-fake/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T20:10:34+00:00",
    "summary": "\"Winning\" bets were made on cloned website and would have lost money, WSJ finds."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/06/following-user-outcry-amd-reinstates-memory-encryption-in-consumer-cpus/",
    "domain": "大厂 AI 动态",
    "title": "Following user outcry, AMD reinstates memory encryption in consumer CPUs",
    "url": "https://arstechnica.com/security/2026/06/following-user-outcry-amd-reinstates-memory-encryption-in-consumer-cpus/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T19:16:52+00:00",
    "summary": "Critics saw the move as an underhanded way to steer them toward more costly chips."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/06/valves-steam-machine-ships-june-29-for-1049-but-you-probably-wont-be-able-to-buy-one-yet/",
    "domain": "大厂 AI 动态",
    "title": "Valve's Steam Machine ships June 29 for $1,049, but you probably won't be able to buy one yet",
    "url": "https://arstechnica.com/gaming/2026/06/valves-steam-machine-ships-june-29-for-1049-but-you-probably-wont-be-able-to-buy-one-yet/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T19:02:45+00:00",
    "summary": "Valve says it's using a randomized purchase queue to make the experience \"less frustrating and more fair.\""
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/woman-killed-when-tesla-driver-using-autopilot-crashed-into-her-home/",
    "domain": "大厂 AI 动态",
    "title": "NHTSA investigating alleged Tesla Autopilot crash that killed woman in her home",
    "url": "https://arstechnica.com/tech-policy/2026/06/woman-killed-when-tesla-driver-using-autopilot-crashed-into-her-home/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T17:10:52+00:00",
    "summary": "Tesla touts Autopilot as lifesaving a day after grandmother died in crash."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/06/lucid-lays-off-1500-workers-in-second-big-cut-of-the-year/",
    "domain": "大厂 AI 动态",
    "title": "Lucid lays off 1,500 workers in second big cut of the year",
    "url": "https://arstechnica.com/cars/2026/06/lucid-lays-off-1500-workers-in-second-big-cut-of-the-year/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T15:22:46+00:00",
    "summary": "The cuts and redundancies are part of a plan to \"simplify the company,\" the CEO says."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/a-us-military-exercise-in-space-got-underway-with-barely-anyone-noticing/",
    "domain": "大厂 AI 动态",
    "title": "A US military exercise in space got underway with barely anyone noticing",
    "url": "https://arstechnica.com/space/2026/06/a-us-military-exercise-in-space-got-underway-with-barely-anyone-noticing/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T15:18:23+00:00",
    "summary": "The Space Force wants to cut the time to field new satellites from years to weeks, days, or hours."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/06/pikes-peak-2026-was-a-battle-of-propulsion-with-an-ev-and-a-hybrid-winning-out/",
    "domain": "大厂 AI 动态",
    "title": "1,250 hp hybrid Corvette shatters the Pikes Peak production record",
    "url": "https://arstechnica.com/cars/2026/06/pikes-peak-2026-was-a-battle-of-propulsion-with-an-ev-and-a-hybrid-winning-out/",
    "source": "Tim Stevens",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T15:07:00+00:00",
    "summary": "The high-altitude race is a unique test of car and driver."
  },
  {
    "id": "rss:https://arstechnica.com/features/2026/06/this-former-hacker-saw-the-light-and-now-wants-to-collect-all-of-it/",
    "domain": "大厂 AI 动态",
    "title": "This former hacker saw the light—and now wants to collect all of it",
    "url": "https://arstechnica.com/features/2026/06/this-former-hacker-saw-the-light-and-now-wants-to-collect-all-of-it/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T14:11:03+00:00",
    "summary": "\"I don’t know of a bigger question we can answer as humans.\""
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/how-anthropic-may-have-talked-itself-into-an-ai-export-ban/",
    "domain": "大厂 AI 动态",
    "title": "How Anthropic may have talked itself into an AI export ban",
    "url": "https://arstechnica.com/ai/2026/06/how-anthropic-may-have-talked-itself-into-an-ai-export-ban/",
    "source": "Clara Murray, Financial Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T13:45:24+00:00",
    "summary": "The company warned about dangers of advanced AI far more than rival OpenAI."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/trump-admins-coal-investments-assist-plants-with-repeated-violations/",
    "domain": "大厂 AI 动态",
    "title": "Trump admin’s coal investments assist plants with repeated violations",
    "url": "https://arstechnica.com/science/2026/06/trump-admins-coal-investments-assist-plants-with-repeated-violations/",
    "source": "Ajani Stella, Inside Climate News",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T17:49:35+00:00",
    "summary": "At least three coal plants have been repeatedly cited for violating environmental regulations."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/06/review-widows-bay-is-a-boldly-original-take-on-comedic-horror/",
    "domain": "大厂 AI 动态",
    "title": "Review: Widow's Bay is a boldly original take on comedic horror",
    "url": "https://arstechnica.com/culture/2026/06/review-widows-bay-is-a-boldly-original-take-on-comedic-horror/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T10:00:11+00:00",
    "summary": "An eminently binge-able series that honors classic horror tropes while reinventing them in surprising ways."
  },
  {
    "id": "rss:https://www.producthunt.com/products/algofly-ai",
    "domain": "大厂 AI 动态",
    "title": "AlgoFly AI",
    "url": "https://www.producthunt.com/products/algofly-ai",
    "source": "Nitin Rai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T13:51:27+00:00",
    "summary": "The all-in-one place to build and deploy vision AI Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/agentx",
    "domain": "大厂 AI 动态",
    "title": "AgentX",
    "url": "https://www.producthunt.com/products/agentx",
    "source": "Rohan Chaubey",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T07:13:56+00:00",
    "summary": "Evaluate AI agent, pinpoint issues, and fix with one click. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/md-html-reader",
    "domain": "大厂 AI 动态",
    "title": "MD+HTML Reader",
    "url": "https://www.producthunt.com/products/md-html-reader",
    "source": "Ahab",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T06:24:17+00:00",
    "summary": "Review AI-generated Markdown and HTML in a focused workspace Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/selector-forge",
    "domain": "大厂 AI 动态",
    "title": "Selector Forge",
    "url": "https://www.producthunt.com/products/selector-forge",
    "source": "Ahmad Ilaiwi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T12:47:39+00:00",
    "summary": "Browser extension for AI-generated resilient selectors Discussion | Link"
  },
  {
    "id": "wscn:3775276",
    "domain": "股票",
    "title": "Token调用量增长超10倍！豆包大模型2.1上线，Seedance 2.5预计7月初正式上线",
    "url": "https://wallstreetcn.com/articles/3775276",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T06:53:22+00:00",
    "summary": "火山引擎发布豆包大模型2.1系列，包含Pro和Turbo版本，并预告Seedance 2.5视频生成模型。新模型在编程、智能体及多模态领域性能逼近或超越国际顶尖模型，Pro版在特定场景综合成本降至每百万Tokens 1.96元。截至今年6月，豆包大模型日均Token调用量已突破180万亿，较去年增长超10倍。"
  },
  {
    "id": "wscn:3775262",
    "domain": "股票",
    "title": "科技热潮降温 ，全球股市“黑色星期二”，韩股收跌10%，纳指期货跌2%，黄金回吐隔夜涨幅",
    "url": "https://wallstreetcn.com/articles/3775262",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T06:51:53+00:00",
    "summary": "日经225指数收跌3.5%，报69788.38点。韩国首尔综指收跌10%，报8203.84点。铠侠股价一度下跌16%，为自2025年11月以来最大跌幅。美股纳斯达克100指数期货跌2%；黄金下跌逾1%，白银跌幅超过3%，比特币下跌逾1%。美元兑多数主要货币走强，日元徘徊于1986年以来最低水平附近。"
  },
  {
    "id": "wscn:3775254",
    "domain": "股票",
    "title": "AH股齐跌：创业板跌逾4%，PCB、CPO齐跌、有色金属重挫，港股“大模型双雄”大跌",
    "url": "https://wallstreetcn.com/articles/3775254",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T06:47:50+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市约3400股飘红，上午半天成交2.34万亿。沪深两市半日成交额2.32万亿，较上个交易日缩量1870亿。板块方面，能源金属、工业金属概念股携手领跌；半导体、算力产业链回调，PCB、CPO方向跌幅明显；光伏、商业航天、AI应用题材走弱。创新药概念股开启反弹，大金融延续强势。"
  },
  {
    "id": "wscn:3775274",
    "domain": "股票",
    "title": "高盛之后，德银也大砍金价预期，最高下调22%",
    "url": "https://wallstreetcn.com/articles/3775274",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T06:36:11+00:00",
    "summary": "华尔街看多黄金的集体热情正在降温。德意志银行将三季度金价预测最高下调22%至4300美元，高盛此前亦将2026年底目标价砍去500美元——美联储鹰派转向、ETF持续净流出、中国进口需求疲软，多重压力叠加令金价本季度已跌逾11%。不过，两大投行均强调央行购金构成关键支撑，高盛更预判中期金价存在突破6000美元的可能。"
  },
  {
    "id": "wscn:3774769",
    "domain": "股票",
    "title": "下一个六氟化钨？金属铋7月或将迎来大变局",
    "url": "https://wallstreetcn.com/premium/articles/3774769?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T06:27:57+00:00",
    "summary": "日本泰和热磁（全球碲化铋市场60%份额）7N碲化铋库存预计6月底耗尽，已停止接受800G和1.6T光模块用TEC的新订货，全球AI光模块供应链正面临实质性断裂风险。"
  },
  {
    "id": "wscn:3775272",
    "domain": "股票",
    "title": "特斯拉Optimus 3量产倒计时，供应商已开始备货",
    "url": "https://wallstreetcn.com/articles/3775272",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T06:24:01+00:00",
    "summary": "特斯拉人形机器人量产进入倒计时——中国台湾供应商已开始向Optimus 3输送谐波减速器与光学镜头，弗里蒙特年产百万台生产线同步推进，马斯克的\"机器人帝国\"正从构想加速走向产线，供应链端的实质备货为这场豪赌提供了最有力的外部背书。"
  },
  {
    "id": "wscn:3775270",
    "domain": "股票",
    "title": "商务部等9部门：全链条扩大汽车消费！改革试点40城名单公布",
    "url": "https://wallstreetcn.com/articles/3775270",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T05:34:45+00:00",
    "summary": "商务部等8部门公布40个汽车流通消费改革试点城市，天津聚焦汽车改装、沈阳深耕二手车、扬州发力房车露营……9部门推出17条硬核措施，从改装、露营、经典车到赛事运动、租赁创新全面发力，一场覆盖汽车消费全链条的政策组合拳正式落地。"
  },
  {
    "id": "wscn:3775267",
    "domain": "股票",
    "title": "六氟化钨暴涨：一条被忽略的半导体上游咽喉",
    "url": "https://wallstreetcn.com/articles/3775267",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T05:11:23+00:00",
    "summary": "一种冷门造芯气体六氟化钨，正引爆A股865%的暴涨神话。日本巨头停产危机，彻底揭开中国蛰伏20年、从“低端卖矿”到“高端突围”的产业逆袭史。资本狂欢背后，全球半导体供应链的权力重构已然打响。"
  },
  {
    "id": "wscn:3775269",
    "domain": "股票",
    "title": "甲骨文一年裁员2.1万人，承认AI取代部分岗位",
    "url": "https://wallstreetcn.com/articles/3775269",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T05:10:38+00:00",
    "summary": "甲骨文披露，过去一年全球裁员约2.1万人（降幅13%），并首次在文件中承认AI技术的部署导致了岗位消失。大规模削减人力成本旨在缓解因兴建AI数据中心、服务OpenAI等客户带来的高额资本开支与重组财务压力。"
  },
  {
    "id": "wscn:3774904",
    "domain": "股票",
    "title": "硅电容：MLCC潜在颠覆者？AI先进封装时代的百亿冠军赛道",
    "url": "https://wallstreetcn.com/premium/articles/3774904?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T04:19:25+00:00",
    "summary": "三星电机宣布签下1.5万亿韩元（约合人民币68亿元）硅电容供应大单，标志着这一长期隐身于MLCC阴影下的细分赛道正式进入资本市场的聚光灯。"
  },
  {
    "id": "wscn:3775137",
    "domain": "股票",
    "title": "K 型分化加剧：科技红利狂飙，消费红利何时到来？",
    "url": "https://wallstreetcn.com/premium/articles/3775137?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T04:10:11+00:00",
    "summary": "消费修复仍缓、科技投资持续扩张，中国经济中期将呈现消费筑底、科技向上的K型分化新常态。"
  },
  {
    "id": "wscn:3775265",
    "domain": "股票",
    "title": "美国最大锂矿即将投产，锂供应链重塑在即",
    "url": "https://wallstreetcn.com/articles/3775265",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T03:42:19+00:00",
    "summary": "美国最大锂矿Thacker Pass预计明年底投产，产量将是美国现有锂产量的10倍，通用汽车已包揽第一阶段全部20年产能，美国政府亦直接入股并提供22亿美元低息贷款。然而，该矿山采用从未在商业规模验证的黏土提锂工艺，公司股价已较去年峰值跌逾56%。CEO表示，首批产出将是估值重新定价的关键节点。"
  },
  {
    "id": "wscn:3775259",
    "domain": "股票",
    "title": "打破在离岸资金池壁垒：六大行直连离岸交易，央行重塑人民币定价权",
    "url": "https://wallstreetcn.com/articles/3775259",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T03:38:47+00:00",
    "summary": "中国央行通过打通在岸与离岸人民币市场壁垒，重塑汇率定价权。六大国有银行获准直接从内地总部开展离岸人民币交易，首批430亿元清算已完成。此举终结了依赖自贸区分支机构的繁琐流程，压缩在离岸价差、抬高做空成本，强化央行对汇率的管控能力。"
  },
  {
    "id": "wscn:3775264",
    "domain": "股票",
    "title": "日本财长确认与贝森特通话，日元徘徊近40年低位，干预预期升温",
    "url": "https://wallstreetcn.com/articles/3775264",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T03:21:37+00:00",
    "summary": "日本财务大臣片山皋月周二确认，已于周一晚间与美财长贝森特通话近一小时，称美日在汇率问题上“合作与协调更加紧密”，并重申“必要时将采取大胆行动”的干预立场。通话时日元一度触及161.93，接近40年低位，消息提振效果短暂。日本上月干预规模已创纪录达11.73万亿日元，但干预效果难以为继。"
  },
  {
    "id": "wscn:3774507",
    "domain": "股票",
    "title": "金刚石散热：超越液冷，它是AI“热力学终极圣杯”？",
    "url": "https://wallstreetcn.com/premium/articles/3774507?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T03:20:40+00:00",
    "summary": "传统铜基散热材料的热导率天花板（约400W/m·K）与热膨胀系数不匹配（铜约17×10⁻⁶/K vs 硅约2.6×10⁻⁶/K）两大物理瓶颈已难以支撑下一代AI芯片的散热需求。金刚石材料凭借2200W/m·K的超高热导率（铜的5倍以上）、与硅接近的热膨胀系数（约1.1ppm/K）以及优异的化学稳定性，成为目前唯一能够同时满足高导热、低热应力、长寿命三大要求的散热方案候选者。"
  },
  {
    "id": "wscn:3775256",
    "domain": "股票",
    "title": "芯片扩产+液冷双引擎爆发，氟化工站上AI超级风口！",
    "url": "https://wallstreetcn.com/articles/3775256",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T03:14:16+00:00",
    "summary": "AI算力狂飙，氟化工迎来历史性重估窗口。芯片制造端，电子级氢氟酸供应偏紧、3M退场留下13亿美元缺口、六氟化钨价格大涨；数据中心端，液冷市场2030年或达310亿美元。瑞银指出，氟化工材料供应商相较电子化学品公司仍存明显折价，市场远未充分定价AI增长红利。"
  },
  {
    "id": "wscn:3775260",
    "domain": "股票",
    "title": "油价下跌，美债为什么不跟？",
    "url": "https://wallstreetcn.com/articles/3775260",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T02:56:22+00:00",
    "summary": "国泰君安国际认为，本轮油价下跌源于地缘风险溢价回吐而非需求走弱，属\"良性通缩\"，未触发避险买盘；油价虽压低通胀预期约20-30bp，但实际利率同步上行将其对冲。根本驱动在于，沃什主导下美联储政策框架转向\"价格稳定优先\"，市场重新上修利率路径，实际利率已取代通胀预期成为定价核心变量。"
  },
  {
    "id": "wscn:3775252",
    "domain": "股票",
    "title": "特朗普高调宣称伊朗接受武器检查，智库揭底：霍尔木兹海峡重开实为美方“付费”妥协",
    "url": "https://wallstreetcn.com/articles/3775252",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T02:17:40+00:00",
    "summary": "美伊临时协议落地，霍尔木兹海峡26艘超级油轮顺利通行，布伦特原油应声跌破79美元。智库直指协议本质：伊朗核计划未作实质让步，美方不过是\"付费开路\"——以经济利益换取航道短期畅通。强硬修辞之下，暗流涌动的核风险仍是悬于全球能源市场的定时炸弹。"
  },
  {
    "id": "wscn:3775225",
    "domain": "股票",
    "title": "印尼股市“保级”成功，但更大的考验还在后面？",
    "url": "https://wallstreetcn.com/premium/articles/3775225?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T02:05:20+00:00",
    "summary": "印尼股市料将保住新兴市场地位，避免被动资金出逃，但宏观逆风与政策不确定性压制估值，反转需待信心修复。"
  },
  {
    "id": "wscn:3775251",
    "domain": "股票",
    "title": "十年七相，英国到底怎么了？",
    "url": "https://wallstreetcn.com/articles/3775251",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T01:55:51+00:00",
    "summary": "英国十年七相，斯塔默辞职再掀政坛风暴。德银直指深层病灶：脱欧撕裂政治生态、财政空间持续收窄、选民耐心耗尽三重困境叠加，令历任首相政治资本迅速燃尽。Truss仅45天的前车之鉴警示市场——当财政公信力动摇，债市可直接压缩政治时间表。德银判断，破局关键或寄望于AI能否真正重振生产率。"
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
    "id": "rss:https://www.netinterest.co/p/apple-turnover",
    "domain": "股票",
    "title": "Apple Turnover",
    "url": "https://www.netinterest.co/p/apple-turnover",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-24T16:38:20+00:00",
    "summary": "How Tim Cook reshaped payments &#8211; and what he leaves behind"
  },
  {
    "id": "rss:https://www.netinterest.co/p/defying-the-surveys",
    "domain": "股票",
    "title": "Defying the Surveys",
    "url": "https://www.netinterest.co/p/defying-the-surveys",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-17T16:54:51+00:00",
    "summary": "Banks report a resilient quarter &#8211; and a lurking threat"
  },
  {
    "id": "rss:https://www.netinterest.co/p/shuffling-risk",
    "domain": "股票",
    "title": "Shuffling Risk",
    "url": "https://www.netinterest.co/p/shuffling-risk",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-10T15:10:44+00:00",
    "summary": "An Asset Class Reborn"
  },
  {
    "id": "rss:https://www.netinterest.co/p/new-pod-the-race-to-secure-a-bank",
    "domain": "股票",
    "title": "NEW POD! The Race to Secure a Bank Charter with Adam Shapiro of Klaros Group",
    "url": "https://www.netinterest.co/p/new-pod-the-race-to-secure-a-bank",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-31T15:45:44+00:00",
    "summary": "Net Interest Extra ep 21"
  },
  {
    "id": "rss:https://www.netinterest.co/p/revolut-unbound",
    "domain": "股票",
    "title": "Revolut Unbound",
    "url": "https://www.netinterest.co/p/revolut-unbound",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-27T16:20:38+00:00",
    "summary": "The Quest to Build the World&#8217;s First Truly Global Bank"
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-underwriters-of-hormuz",
    "domain": "股票",
    "title": "The Underwriters of Hormuz",
    "url": "https://www.netinterest.co/p/the-underwriters-of-hormuz",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-20T16:23:35+00:00",
    "summary": "A post on marine insurance &#8211; by popular demand"
  },
  {
    "id": "rss:https://www.netinterest.co/p/new-pod-market-intelligence-in-the",
    "domain": "股票",
    "title": "🎙️ Market Intelligence in the Age of AI: An Interview with Morningstar CEO, Kunal Kapoor",
    "url": "https://www.netinterest.co/p/new-pod-market-intelligence-in-the",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-17T16:30:34+00:00",
    "summary": "Net Interest Extra ep 20"
  },
  {
    "id": "rss:https://www.netinterest.co/p/redemption-day",
    "domain": "股票",
    "title": "Redemption Day",
    "url": "https://www.netinterest.co/p/redemption-day",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-13T18:09:28+00:00",
    "summary": "When the exit is smaller than the entrance"
  },
  {
    "id": "rss:https://www.netinterest.co/p/learning-from-lloyd",
    "domain": "股票",
    "title": "Learning from Lloyd",
    "url": "https://www.netinterest.co/p/learning-from-lloyd",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-06T17:42:54+00:00",
    "summary": "Blankfein, Goldman and the Next Market Reckoning"
  },
  {
    "id": "rss:https://www.netinterest.co/p/new-pod-how-credit-markets-shaped",
    "domain": "股票",
    "title": "🎙️ How Credit Markets Shaped a Nation: An Interview with Sarah Quinn",
    "url": "https://www.netinterest.co/p/new-pod-how-credit-markets-shaped",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-03T16:45:21+00:00",
    "summary": "Net Interest Extra ep 19"
  },
  {
    "id": "rss:https://www.netinterest.co/p/two-tribes",
    "domain": "股票",
    "title": "Two Tribes",
    "url": "https://www.netinterest.co/p/two-tribes",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-02-27T17:42:58+00:00",
    "summary": "Private Credit, Public Markets and the AI Reckoning"
  },
  {
    "id": "rss:https://www.netinterest.co/p/ai-and-i",
    "domain": "股票",
    "title": "AI and I",
    "url": "https://www.netinterest.co/p/ai-and-i",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-02-20T17:21:53+00:00",
    "summary": "Claude Code, Bloomberg and the Battle for Data"
  }
]
```
