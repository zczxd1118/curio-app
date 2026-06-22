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

- 今日日期：`2026-06-22`
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
  "date": "2026-06-22",
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
    "points": 3329436,
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
    "points": 1246218,
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
    "points": 1218557,
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
    "points": 1213744,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 745097,
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
    "points": 663760,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1RSFUzVEAG",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码",
    "url": "http://www.bilibili.com/video/av116045469783373",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 524282,
    "published_at": "2026-02-10T08:59:28+00:00",
    "summary": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 465327,
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
    "points": 435549,
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
    "points": 414856,
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
    "points": 391256,
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
    "points": 383463,
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
    "points": 374854,
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
    "points": 329756,
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
    "points": 245618,
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
    "points": 240424,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 175107,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1X8oKBLEdj",
    "domain": "AI",
    "title": "一口气学会AI编程！3个月10万字超详细教学！【项目实操】【0基础教学】【自学教程】【AI编程】【vibecoding】",
    "url": "http://www.bilibili.com/video/av116436177523067",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 174003,
    "published_at": "2026-04-21T03:15:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料，领取方式：关注后 私信“ 1 ”就好！\n\n后面还会出【一口气学会AI漫剧 】【一口气学会AI Agent 】等系列！大家可以蹲蹲！"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 164445,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 157305,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1b5AeeGEFc",
    "domain": "AI",
    "title": "Cursor太贵？分享三个免费AI编程方案+海量编程技巧【如何看待AI编程】",
    "url": "http://www.bilibili.com/video/av114025056699722",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 155902,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 155370,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1RAEz6EE98",
    "domain": "AI",
    "title": "为什么Claude Code+DeepSeekV4是最有性价比的个人AI Agent?",
    "url": "http://www.bilibili.com/video/av116732144392386",
    "source": "呱声一片",
    "platform": "bilibili",
    "points": 144606,
    "published_at": "2026-06-11T15:27:06+00:00",
    "summary": "官方文档地址：https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/claude_code"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 142976,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92218,
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
    "points": 87922,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1wDFszxEGX",
    "domain": "AI",
    "title": "AI 直接操控 UE5.7！AI 读工程+写蓝图+自动实现功能",
    "url": "http://www.bilibili.com/video/av116030487732208",
    "source": "UnrealXu",
    "platform": "bilibili",
    "points": 61298,
    "published_at": "2026-02-07T17:23:41+00:00",
    "summary": "这是一个把 Codex 接入 UE5 编辑器的 AI 助手插件：支持理解项目结构、定位关键蓝图/输入/关卡对象，辅助编写与修改蓝图和 C++，并在 World 场景层面完成落地调整（灯光/天气/Actor 等）。目前功能持续迭代中，欢迎留言交流、提交需求"
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 59739,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 52247,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 50939,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1rKjG6yEh2",
    "domain": "AI",
    "title": "10分钟+300个Agent：保姆级教程学会Agent Skills！【从零开始】",
    "url": "http://www.bilibili.com/video/av116758736279146",
    "source": "Work-Fisher",
    "platform": "bilibili",
    "points": 49489,
    "published_at": "2026-06-16T10:02:41+00:00",
    "summary": "这期我从最基础的概念，一路讲到上手实操，基本上是从 0 到 1，带你完整走一遍——一个 SKILL 到底是怎么从无到有做出来的。\n国内、国外的创建工具，我也都给你捋了一遍。希望看完这期，你也能动手做出一个真正属于自己的 SKIL。"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47166,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 39342,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 36582,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 36561,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1ap2fBvEt9",
    "domain": "AI",
    "title": "如何使用「Operit AI」：你的下一代AI手机助手",
    "url": "http://www.bilibili.com/video/av115677243447909",
    "source": "默睦",
    "platform": "bilibili",
    "points": 32470,
    "published_at": "2025-12-07T08:06:42+00:00",
    "summary": "下载地址：https://github.com/AAswordman/Operit\n\n相关软件资料下载：https://www.123pan.com/s/IKgAjv-Hinsv.html\n\n官方交流群：458862019"
  },
  {
    "id": "bvid:BV1ZEJA6xEds",
    "domain": "AI",
    "title": "最新方法！国内免费无限制，使用Claude Code！",
    "url": "http://www.bilibili.com/video/av116746874848391",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 31518,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29755,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27417,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV1mfJw6uE1Y",
    "domain": "AI",
    "title": "AI Agent 别乱选！2026 AI Agent 深度横评，普通人看完不踩坑｜OpenClaw、Codex、Hermes、WorkBuddy、Claude",
    "url": "http://www.bilibili.com/video/av116747361322195",
    "source": "AI实战派Pro",
    "platform": "bilibili",
    "points": 25003,
    "published_at": "2026-06-14T07:53:12+00:00",
    "summary": "《2026 主流 AI Agent 全维度对比｜OpenClaw / Codex / Claude Cowork / WorkBuddy / Hermes 怎么选？》\n\nHi，我是Alpha，我手把手带大家用AI提升自己工作、生活效率，提升个人竞争力以及用AI赚钱！一起做AI时代的主导者，而不是在焦虑中被AI淘汰！\n关注AI 实战派，让AI替你忙起来！\n\n本期视频介绍：《AI Agent 别乱选！"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 23954,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1hnjGzLE14",
    "domain": "AI",
    "title": "【小智教程】手挽手教你如何接入别人的MCP服务",
    "url": "http://www.bilibili.com/video/av114568722450105",
    "source": "空白泡泡糖果",
    "platform": "bilibili",
    "points": 17173,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV166EC6zEMW",
    "domain": "AI",
    "title": "【6.12最新发布】claude桌面版安装教程！一周快速入门claude code保姆级教程！",
    "url": "http://www.bilibili.com/video/av116735751489240",
    "source": "是蒜七丫",
    "platform": "bilibili",
    "points": 12652,
    "published_at": "2026-06-12T06:50:08+00:00",
    "summary": "求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！求三连！"
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 10502,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1UjJV6qESu",
    "domain": "AI",
    "title": "1 小时 VibeCoding 复刻大神网页教程！",
    "url": "http://www.bilibili.com/video/av116753552114270",
    "source": "ai超级个人",
    "platform": "bilibili",
    "points": 9819,
    "published_at": "2026-06-15T10:05:34+00:00",
    "summary": "几个简单小技巧就复刻了 Awwwards 上大神的获奖作品，欢迎一起交流~~"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9061,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "穷在街头无人问lhj",
    "platform": "bilibili",
    "points": 8952,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1jsEQ6XEw6",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116724292721480",
    "source": "倒计时19",
    "platform": "bilibili",
    "points": 8189,
    "published_at": "2026-06-10T06:04:26+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1etEQ6DETs",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116724192118321",
    "source": "AI产品经理大模型",
    "platform": "bilibili",
    "points": 7525,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1oXjc6CEWK",
    "domain": "AI",
    "title": "（2026版）这才是B站讲的最好的Vibe Coding企业级项目实战，Claude Code+Codex+Cursor丨一周学完，让你少走99%弯路！",
    "url": "http://www.bilibili.com/video/av116769742195971",
    "source": "京东架构师诸葛",
    "platform": "bilibili",
    "points": 6536,
    "published_at": "2026-06-18T06:52:48+00:00",
    "summary": "（2026版）这才是B站讲的最好的Vibe Coding企业级项目实战，Claude Code+Codex+Cursor丨一周学完，让你少走99%弯路！\n【视频配套学习笔记、Agent开发、大模型最新学习路线、系统学习、实战案例、电子书+问题解答】都在这了：https://www.bilibili.com/read/cv39979382/"
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
    "title": "Best Amazon Prime Day tech deals live — PC hardware deals on SSDs, RAM, GPUs, CPUs, gaming laptops, and more",
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
    "id": "rss:https://www.tomshardware.com/pc-components/samsungs-32-inch-1440p-165-hz-gaming-monitor-falls-to-its-lowest-price-yet-with-46-percent-off-for-prime-day-grab-the-curved-odyssey-g55c-at-just-usd189-99",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung's 32-inch 1440p 165 Hz gaming monitor falls to its lowest price yet with 46% off for Prime Day — grab the curved Odyssey G55C at just $189.99",
    "url": "https://www.tomshardware.com/pc-components/samsungs-32-inch-1440p-165-hz-gaming-monitor-falls-to-its-lowest-price-yet-with-46-percent-off-for-prime-day-grab-the-curved-odyssey-g55c-at-just-usd189-99",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T13:56:33+00:00",
    "summary": "Featuring a 32-inch 1000R curved QHD panel, 165 Hz refresh rate, 1 ms MPRT response time, and AMD FreeSync support, the Samsung Odyssey G5 G55C has dropped to its lowest price of $189.99 ahead of Prim"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/mechanical-keyboards/one-of-our-favorite-budget-gaming-keyboards-drops-back-down-to-its-lowest-ever-price-of-usd45-at-amazon-rk-r65-packs-lubed-switches-metallic-knob-and-gasket-mount-for-excellent-sound-and-feel",
    "domain": "AI 算力 / 半导体",
    "title": "One of our favorite budget gaming keyboards drops back down to its lowest-ever price of $45 at Amazon — RK R65 packs lubed switches, metallic knob, and gasket mount for excellent sound and feel",
    "url": "https://www.tomshardware.com/peripherals/mechanical-keyboards/one-of-our-favorite-budget-gaming-keyboards-drops-back-down-to-its-lowest-ever-price-of-usd45-at-amazon-rk-r65-packs-lubed-switches-metallic-knob-and-gasket-mount-for-excellent-sound-and-feel",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T13:41:14+00:00",
    "summary": "Our favorite 60% budget gaming keyboard, the Royal Kludge R65, is back down to just $44 with coupon at Amazon, its lowest-ever price. This wired clacker delivers excellent sound and feel for the price"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/dramatically-redesigned-gmktec-evo-x3-shown-bearing-lisa-sus-signature-of-approval-flagship-ai-mini-pc-workstation-is-built-around-amds-ryzen-ai-max-395-strix-halo-processor-again",
    "domain": "AI 算力 / 半导体",
    "title": "Dramatically redesigned GMKtec EVO-X3 shown bearing Lisa Su’s signature of approval — flagship AI mini PC workstation is built around AMD’s Ryzen AI Max+ 395 'Strix Halo' processor, again",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/dramatically-redesigned-gmktec-evo-x3-shown-bearing-lisa-sus-signature-of-approval-flagship-ai-mini-pc-workstation-is-built-around-amds-ryzen-ai-max-395-strix-halo-processor-again",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T12:46:59+00:00",
    "summary": "GMKtec's dramatically redesigned EVO-X3 'Strix Halo' Mini PC gets Lisa Su’s signature of approval."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/bank-of-korea-flags-samsung-and-sk-hynix-chip-bonuses-as-a-national-inflation-risk",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung and SK hynix bonuses for chip workers flagged as a national inflation risk — Bank of Korea projects full-year inflation significantly above its 2% target",
    "url": "https://www.tomshardware.com/tech-industry/bank-of-korea-flags-samsung-and-sk-hynix-chip-bonuses-as-a-national-inflation-risk",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T11:58:39+00:00",
    "summary": "The Bank of Korea has named performance bonuses at Samsung Electronics and SK hynix as a risk to the country's inflationary stability."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/telehealth-doctor-treats-patients-using-razer-naga-gaming-mouse-12-button-mmo-thumb-grid-simplifies-medical-workflow-automates-medical-scripting",
    "domain": "AI 算力 / 半导体",
    "title": "Telehealth doctor treats patients using Razer Naga gaming mouse — 12-button MMO thumb grid simplifies medical workflow, automates medical scripting",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/telehealth-doctor-treats-patients-using-razer-naga-gaming-mouse-12-button-mmo-thumb-grid-simplifies-medical-workflow-automates-medical-scripting",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T11:30:00+00:00",
    "summary": "Dr. James Ries says that his Razer Naga V2 MMO gaming mouse helps him treat patients by keeping relevant medical responses at his fingertips."
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/creality-falcon-t1-review",
    "domain": "AI 算力 / 半导体",
    "title": "Creality Falcon T1 review: Modular laser engraving",
    "url": "https://www.tomshardware.com/maker-stem/creality-falcon-t1-review",
    "source": "Andrew Sink",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T11:10:00+00:00",
    "summary": "The Creality Falcon T1 is a galvo laser engraver that uses swappable diode, fiber, UV, and MOPA laser modules to engrave wood, crystal, metal, and a wide range of other materials. With a base price of"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/age-of-empires-iis-goats-used-as-ai-building-blocks-to-build-a-neural-network-goaty-experiment-mocks-the-idea-of-chatbot-consciousness-microsoft-ai-researchers-project-makes-an-absurdist-point-about-ai-consciousness",
    "domain": "AI 算力 / 半导体",
    "title": "Age of Empires II’s goats used as AI building blocks to build a neural network — goaty experiment mocks the idea of chatbot consciousness, Microsoft AI researcher’s project makes an absurdist point ab",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/age-of-empires-iis-goats-used-as-ai-building-blocks-to-build-a-neural-network-goaty-experiment-mocks-the-idea-of-chatbot-consciousness-microsoft-ai-researchers-project-makes-an-absurdist-point-about-ai-consciousness",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T11:00:00+00:00",
    "summary": "People seem all-too-ready to anthropomorphize LLMs and AI chatbots like ChatGPT, Claude, and Gemini, reckons a Microsoft AI researcher."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/acoustic-mapping-app-uses-thousands-of-networked-old-android-phones-to-hunt-shahed-drones-crowd-sourced-microphone-network-spots-small-low-rcs-military-targets",
    "domain": "AI 算力 / 半导体",
    "title": "Acoustic mapping app uses thousands of networked old Android phones to hunt Shahed drones — crowd-sourced microphone network spots small, low-RCS military targets",
    "url": "https://www.tomshardware.com/tech-industry/drones/acoustic-mapping-app-uses-thousands-of-networked-old-android-phones-to-hunt-shahed-drones-crowd-sourced-microphone-network-spots-small-low-rcs-military-targets",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T10:30:00+00:00",
    "summary": "This app would crowdsource drone detection and help map their location and direction long before they reach their targets."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-amds-flagship-ryzen-7-9800x3d-with-32gb-of-ddr5-memory-and-an-msi-b850-wi-fi-7-motherboard-at-a-discount-micro-center-bundles-are-now-available-on-amazon",
    "domain": "AI 算力 / 半导体",
    "title": "Get AMD's flagship Ryzen 7 9800X3D with 32GB of DDR5 memory and an MSI B850 Wi-Fi 7 motherboard at a discount — Micro Center bundles are now available on Amazon",
    "url": "https://www.tomshardware.com/pc-components/get-amds-flagship-ryzen-7-9800x3d-with-32gb-of-ddr5-memory-and-an-msi-b850-wi-fi-7-motherboard-at-a-discount-micro-center-bundles-are-now-available-on-amazon",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T17:57:35+00:00",
    "summary": "Micro Center is now selling some of its bundles on Amazon, including this 9800X3D combo that gives you an excellent motherboard and fast RAM without breaking the bank."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/wds-2tb-black-ssd-price-drops-by-nearly-20-percent-ahead-of-prime-day-sale-grab-the-2tb-sn7100-for-usd242-96",
    "domain": "AI 算力 / 半导体",
    "title": "WD's 2TB Black SSD price drops by nearly 20% ahead of Prime Day sale — grab the 2TB SN7100 for $242.96",
    "url": "https://www.tomshardware.com/pc-components/ssds/wds-2tb-black-ssd-price-drops-by-nearly-20-percent-ahead-of-prime-day-sale-grab-the-2tb-sn7100-for-usd242-96",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T16:45:07+00:00",
    "summary": "The WD Black SN7100 stands out for its high-end performance, low operating temperatures, and impressive efficiency. It is one of the few PCIe 4.0 SSDs that can compete with flagship drives while consu"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd300-on-this-1440p-ready-gaming-pc-with-32gb-ddr5-ram-grab-the-asus-rog-gm700-with-amds-ryzen-7-8700f-and-rx-9060-xt-for-just-usd1-199",
    "domain": "AI 算力 / 半导体",
    "title": "Save $300 on this 1440p-ready gaming PC with 32GB DDR5 RAM — grab the Asus ROG GM700 with AMD's Ryzen 7 8700F and RX 9060 XT for just $1,199",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd300-on-this-1440p-ready-gaming-pc-with-32gb-ddr5-ram-grab-the-asus-rog-gm700-with-amds-ryzen-7-8700f-and-rx-9060-xt-for-just-usd1-199",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T15:25:58+00:00",
    "summary": "Asus' ROG GM700 is a great prebuilt, packing powerful components for a solid price without compromising on the details. It just happens to look nice, too, if you're into the gamer aesthetic."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/award-winning-resin-3d-printer-for-beginners-is-36-percent-off-grab-the-anycubic-photon-p1-with-dual-color-material-kit-for-usd619-99",
    "domain": "AI 算力 / 半导体",
    "title": "Award-winning resin 3D printer for beginners is 36% off — grab the Anycubic Photon P1 with dual-color material kit for $619.99",
    "url": "https://www.tomshardware.com/3d-printing/award-winning-resin-3d-printer-for-beginners-is-36-percent-off-grab-the-anycubic-photon-p1-with-dual-color-material-kit-for-usd619-99",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T15:02:44+00:00",
    "summary": "Featuring a precision steel build plate, wireless printing support, and excellent print quality, the Anycubic Photon P1 is now available with a dual-color material kit at its lowest advertised price y"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/china-unifies-tech-sector-to-build-grid-free-orbiting-satellite-ai-data-centers-challenging-elon-musks-spacex-beijings-forced-chip-and-satellite-alliance-announced-a-week-before-musks-ai1-reveal",
    "domain": "AI 算力 / 半导体",
    "title": "China unifies tech sector to build grid-free orbiting satellite AI data centers, challenging Elon Musk's SpaceX — Beijing's forced chip and satellite alliance announced a week before Musk’s AI1 reveal",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/china-unifies-tech-sector-to-build-grid-free-orbiting-satellite-ai-data-centers-challenging-elon-musks-spacex-beijings-forced-chip-and-satellite-alliance-announced-a-week-before-musks-ai1-reveal",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T14:53:42+00:00",
    "summary": "Beijing says the Space Computing Industry Innovation Center will bring together rocket and satellite manufacturers, chip manufacturers, and AI labs to develop a space-based data center system."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/best-uk-amazon-prime-day-tech-deals",
    "domain": "AI 算力 / 半导体",
    "title": "The best UK Amazon Prime Day tech deals 2026 — epic savings on premium gaming PCs and laptops, peripherals, 3D printers at Currys, Argos, Scan and CCL, too",
    "url": "https://www.tomshardware.com/pc-components/best-uk-amazon-prime-day-tech-deals",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T14:06:35+00:00",
    "summary": "The best UK deals on gaming PCs, laptops, tools, and accessories for Amazon Prime Day"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/rare-asml-special-edition-monopoly-board-unearthed-in-social-media-trade-enthusiast-swaps-2007-employee-gift-for-high-na-euv-lego-kit",
    "domain": "AI 算力 / 半导体",
    "title": "Rare ASML Special Edition Monopoly board unearthed in social media trade — enthusiast swaps 2007 employee gift for High-NA EUV Lego kit",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/rare-asml-special-edition-monopoly-board-unearthed-in-social-media-trade-enthusiast-swaps-2007-employee-gift-for-high-na-euv-lego-kit",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T13:49:56+00:00",
    "summary": "We just witnessed a significant semiconductor industry related non-cash trade deal take place on Twitter/X."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/web-app-drives-valves-new-steam-controller-across-the-floor-using-its-rumble-motors",
    "domain": "AI 算力 / 半导体",
    "title": "New web app can make Valve's Steam Controller drift across your desk like an RC car — web app drives the gamepad using its rumble motors",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/web-app-drives-valves-new-steam-controller-across-the-floor-using-its-rumble-motors",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T13:37:38+00:00",
    "summary": "A developer has created a Chromium browser-based tool that turns Valve's second-gen Steam Controller into a self-propelled RC car."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/3d-scanning/best-3d-scanners",
    "domain": "AI 算力 / 半导体",
    "title": "The best 3D scanners 2026 — the top performing models we've benchmarked",
    "url": "https://www.tomshardware.com/3d-printing/3d-scanning/best-3d-scanners",
    "source": "Andrew Sink",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T13:17:22+00:00",
    "summary": "We help you find the best 3D scanners for high accuracy, portability, and more."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-and-amds-new-ace-cpu-extensions-bring-an-efficient-ai-oriented-instruction-set-to-x86-a-new-design-makes-matrix-multiplication-more-power-and-density-efficient",
    "domain": "AI 算力 / 半导体",
    "title": "Intel and AMD's new ACE CPU extensions bring an efficient AI-oriented instruction set to x86 — a new design makes matrix multiplication more power- and density-efficient",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-and-amds-new-ace-cpu-extensions-bring-an-efficient-ai-oriented-instruction-set-to-x86-a-new-design-makes-matrix-multiplication-more-power-and-density-efficient",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T12:00:00+00:00",
    "summary": "ACE CPU extensions bring an efficient AI-oriented instruction set to x86 — new design makes matrix multiplication more power- and density-efficient"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/unlucky-pc-builder-sent-rtx-5070-from-amazon-gets-dvd-rewriter-and-a-busted-logic-board-from-an-early-2000s-kenwood-av-receiver-instead-usd700-gpu-turns-out-to-be-e-waste-thanks-to-return-scam",
    "domain": "AI 算力 / 半导体",
    "title": "Unlucky PC builder sent RTX 5070 from Amazon, gets DVD rewriter and a busted logic board from an early 2000's Kenwood AV receiver instead — $700 GPU turns out to be e-waste thanks to return scam",
    "url": "https://www.tomshardware.com/pc-components/gpus/unlucky-pc-builder-sent-rtx-5070-from-amazon-gets-dvd-rewriter-and-a-busted-logic-board-from-an-early-2000s-kenwood-av-receiver-instead-usd700-gpu-turns-out-to-be-e-waste-thanks-to-return-scam",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T11:30:00+00:00",
    "summary": "Another person has fallen victim to Amazon's generous return policy, as they received a disc drive, a mousepad, and an AV receiver instead of the $700 RTX 5070 they ordered."
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/researcher-turns-wi-fi-smart-lightbulb-into-a-banned-book-library-open-source-project-makes-digital-books-available-via-a-server-and-open-wi-fi-access-point-hacked-into-an-esp32-powered-bulb",
    "domain": "AI 算力 / 半导体",
    "title": "Researcher turns wi-fi smart lightbulb into a Banned Book Library — open source project makes digital books available via a server and open Wi-Fi access point hacked into an ESP32-powered bulb",
    "url": "https://www.tomshardware.com/maker-stem/researcher-turns-wi-fi-smart-lightbulb-into-a-banned-book-library-open-source-project-makes-digital-books-available-via-a-server-and-open-wi-fi-access-point-hacked-into-an-esp32-powered-bulb",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T11:00:00+00:00",
    "summary": "A security researcher has added another dimension to smart lightbulbs by stealthily adding what they call a 'cyberpunk digital dead drop' full of 'banned books.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/china-shows-off-a-backpack-sized-anti-drone-laser-that-one-soldier-can-carry",
    "domain": "AI 算力 / 半导体",
    "title": "China unveils man-portable anti-drone laser that can burn through a drone 1,600 feet away in four seconds — backpack-sized 2-kilowatt weapon uses AI for targeting, weighs 55 pounds, and can be carried",
    "url": "https://www.tomshardware.com/tech-industry/china-shows-off-a-backpack-sized-anti-drone-laser-that-one-soldier-can-carry",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T10:30:00+00:00",
    "summary": "Chinese defense supplier Harbin Xinguang Optic-Electronics Technology demo’d two man-portable anti-drone lasers at a Beijing arms expo this week."
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
    "id": "rss:https://www.eetimes.com/space-industry-is-standardizing-on-risc-v/",
    "domain": "AI 算力 / 半导体",
    "title": "Space Industry Is Standardizing on RISC-V",
    "url": "https://www.eetimes.com/space-industry-is-standardizing-on-risc-v/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T12:00:00+00:00",
    "summary": "Experts at RISC-V Summit Europe outlined how open architectures are transforming computing across the space economy. The post Space Industry Is Standardizing on RISC-V appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-will-reinstate-memory-encryption-on-ryzen-9000-cpus-through-a-bios-update-in-july-tsme-is-coming-back-after-valuable-community-feedback",
    "domain": "AI 算力 / 半导体",
    "title": "AMD will reinstate memory encryption on Ryzen 9000 CPUs through a BIOS update in July — TSME is coming back after 'valuable community feedback'",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-will-reinstate-memory-encryption-on-ryzen-9000-cpus-through-a-bios-update-in-july-tsme-is-coming-back-after-valuable-community-feedback",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T21:02:49+00:00",
    "summary": "AMD says it will reinstate firmware memory encryption (TSME) on non-PRO Ryzen 9000 desktop CPUs through a BIOS update in July, following the feature's removal through an earlier firmware update."
  },
  {
    "id": "rss:https://www.eetimes.com/can-catalonia-deliver-on-its-distributed-semiconductor-network/",
    "domain": "AI 算力 / 半导体",
    "title": "Can Catalonia’s Distributed Semiconductor Network Deliver?",
    "url": "https://www.eetimes.com/can-catalonia-deliver-on-its-distributed-semiconductor-network/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T07:15:00+00:00",
    "summary": "Catalonia is unifying its fragmented tech ecosystem into a coordinated semiconductor cluster spanning photonics, packaging, AI, and chip research. The post Can Catalonia’s Distributed Semiconductor Ne"
  },
  {
    "id": "rss:https://www.eetimes.com/canadian-researchers-reduce-quantum-atmospheric-turbulence/",
    "domain": "AI 算力 / 半导体",
    "title": "Canadian Researchers Reduce Quantum Atmospheric Turbulence",
    "url": "https://www.eetimes.com/canadian-researchers-reduce-quantum-atmospheric-turbulence/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T19:00:00+00:00",
    "summary": "uOttawa cracks quantum turbulence, making ultra-secure communication cheaper. The post Canadian Researchers Reduce Quantum Atmospheric Turbulence appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/reliable-machine-vision-starts-at-the-circuit-level/",
    "domain": "AI 算力 / 半导体",
    "title": "Reliable Machine Vision Starts at the Circuit Level",
    "url": "https://www.eetimes.com/reliable-machine-vision-starts-at-the-circuit-level/",
    "source": "YAGEO Group, Simon Reuning",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T18:01:28+00:00",
    "summary": "Machine vision has become a critical quality gate in modern industrial automation, helping manufacturers inspect products, guide robots, verify assemblies, and reduce production errors. However, relia"
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
    "id": "rss:https://www.theverge.com/entertainment/953324/bose-studios-record-label-media-company",
    "domain": "大厂 AI 动态",
    "title": "Bose thinks it can be a media company for some reason",
    "url": "https://www.theverge.com/entertainment/953324/bose-studios-record-label-media-company",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T18:53:50+00:00",
    "summary": "The history books are littered with the corpses of corporate record labels started by companies that had no business being in the music industry. Bose thinks it can be the exception to the rule. It th"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/953303/cold-court-hands-up-ep-music-review",
    "domain": "大厂 AI 动态",
    "title": "Cold Court’s debut EP is an infectious, glitchy genre mashup",
    "url": "https://www.theverge.com/entertainment/953303/cold-court-hands-up-ep-music-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T17:00:33+00:00",
    "summary": "Cold Court is a brother-sister duo from Philly that seems to love nothing more than shoving all of their influences together in a messy soup that at least superficially resembles the hyperpop you've c"
  },
  {
    "id": "rss:https://www.theverge.com/tech/953285/polymarket-fake-viral-video-bets",
    "domain": "大厂 AI 动态",
    "title": "Polymarket reportedly paid people to post fake videos of themselves placing bets",
    "url": "https://www.theverge.com/tech/953285/polymarket-fake-viral-video-bets",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T14:19:46+00:00",
    "summary": "According to a Wall Street Journal investigation, Polymarket has been paying people to film themselves placing fake bets and celebrating fake wins on social media. WSJ identified over 1,100 deceptive "
  },
  {
    "id": "rss:https://www.theverge.com/podcast/953275/roomba-robot-vacuum-version-history",
    "domain": "大厂 AI 动态",
    "title": "How Roomba started a robot revolution",
    "url": "https://www.theverge.com/podcast/953275/roomba-robot-vacuum-version-history",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T12:29:01+00:00",
    "summary": "If you had a Roomba, especially in the early days of the robot vacuum, it was in many ways a fairly unsophisticated machine. It would just bump around your house, looking for something to suck up, unt"
  },
  {
    "id": "rss:https://www.theverge.com/column/950975/electric-air-taxis-lawsuits",
    "domain": "大厂 AI 动态",
    "title": "Electric air taxis are stuck in the courtroom",
    "url": "https://www.theverge.com/column/950975/electric-air-taxis-lawsuits",
    "source": "Andrew Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T12:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more on aviation, air taxis, and Wi-Fi speeds at 30,000 feet, follow Andrew J. Hawkins. The Stepbac"
  },
  {
    "id": "rss:https://www.theverge.com/tech/952245/sony-xperia-1-viii-review",
    "domain": "大厂 AI 动态",
    "title": "Sony’s Xperia 1 VIII is still a phone for the fans",
    "url": "https://www.theverge.com/tech/952245/sony-xperia-1-viii-review",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T11:00:00+00:00",
    "summary": "The Xperia 1 VIII marks an attempt at a step change for Sony's flagship phone line. Not only has it had an aesthetic overhaul, but Sony has also revamped the camera system, dropping the continuous opt"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/953183/the-atlantic-searchable-database-music-ai-training-data",
    "domain": "大厂 AI 动态",
    "title": "The Atlantic created a searchable database of the music used to train AI",
    "url": "https://www.theverge.com/ai-artificial-intelligence/953183/the-atlantic-searchable-database-music-ai-training-data",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T18:46:48+00:00",
    "summary": "Atlantic reporter Alex Reisner recently uncovered four datasets of music being used to train AI models and made them fully searchable for the public. Two of the sets are absolutely enormous at 12 mill"
  },
  {
    "id": "rss:https://www.theverge.com/report/953116/experimental-musician-youtuber-hainbach-interview",
    "domain": "大厂 AI 动态",
    "title": "Musician and YouTuber Hainbach on ‘Breath of the Wild’ and Swiss Army Knives",
    "url": "https://www.theverge.com/report/953116/experimental-musician-youtuber-hainbach-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T15:20:00+00:00",
    "summary": "Stefan Paul Goetsch, better known as Hainbach, is a German experimental composer, artist, and YouTuber who is perhaps most famous for making music with laboratory equipment and scientific instruments."
  },
  {
    "id": "rss:https://www.theverge.com/games/949875/moves-of-the-diamond-hand-rpg-dice-jazz-noir",
    "domain": "大厂 AI 动态",
    "title": "Moves of the Diamond Hand is an unfinished, irresistibly weird dice-based RPG",
    "url": "https://www.theverge.com/games/949875/moves-of-the-diamond-hand-rpg-dice-jazz-noir",
    "source": "Adi Robertson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T14:00:00+00:00",
    "summary": "From its opening minutes, Moves of the Diamond Hand is upfront about what it offers: You're going to have a lot of strange conversations, and you're going to roll a lot of dice. Get on board with this"
  },
  {
    "id": "rss:https://www.theverge.com/tech/952547/toy-story-5-tech-android-17-snap-specs-installer",
    "domain": "大厂 AI 动态",
    "title": "Toy Story has the right take on tech",
    "url": "https://www.theverge.com/tech/952547/toy-story-5-tech-android-17-snap-specs-installer",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T12:00:00+00:00",
    "summary": "Hi, friends! Welcome to Installer No. 133, your guide to the best and Verge-iest stuff in the world. (If you're new here, welcome, happy belated Juneteenth, and also you can read all the old editions "
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/21/ethan-thornton-is-trying-to-do-everything-all-at-once/",
    "domain": "大厂 AI 动态",
    "title": "Ethan Thornton is trying to do everything all at once",
    "url": "https://techcrunch.com/2026/06/21/ethan-thornton-is-trying-to-do-everything-all-at-once/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T05:31:59+00:00",
    "summary": "Mach's approach differs sharply from some of its peers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/21/ubisoft-co-founder-claude-guillemot-dies-in-plane-crash/",
    "domain": "大厂 AI 动态",
    "title": "Ubisoft co-founder Claude Guillemot dies in plane crash",
    "url": "https://techcrunch.com/2026/06/21/ubisoft-co-founder-claude-guillemot-dies-in-plane-crash/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T18:34:31+00:00",
    "summary": "Claude Guillemot, who founded Ubisoft with his four brothers, has died at the age of 69."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/21/polymarket-reportedly-paid-creators-to-post-deceptive-videos-about-fake-bets/",
    "domain": "大厂 AI 动态",
    "title": "Polymarket reportedly paid creators to post deceptive videos about fake bets",
    "url": "https://techcrunch.com/2026/06/21/polymarket-reportedly-paid-creators-to-post-deceptive-videos-about-fake-bets/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T16:35:00+00:00",
    "summary": "Many of those videos were reportedly filmed on “near-perfect copies” of the Polymarket website, while featuring trades and winnings that were not real."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/21/techcrunch-mobility-a-new-robotaxi-scorecard-shows-chinas-dominance/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: A new robotaxi scorecard shows China’s dominance",
    "url": "https://techcrunch.com/2026/06/21/techcrunch-mobility-a-new-robotaxi-scorecard-shows-chinas-dominance/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T16:05:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility — your central hub for news and insights on the future of transportation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/21/when-the-trump-administration-cracks-down-on-anthropic-who-benefits/",
    "domain": "大厂 AI 动态",
    "title": "When the Trump administration cracks down on Anthropic, who benefits?",
    "url": "https://techcrunch.com/2026/06/21/when-the-trump-administration-cracks-down-on-anthropic-who-benefits/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T15:28:17+00:00",
    "summary": "On the new episode of Equity, we discussed what actually prompted the administration's latest moves against Anthropic, and what this might mean for the AI ecosystem."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/21/beyond-siri-here-are-the-practical-ai-features-coming-to-your-iphone-in-ios-27/",
    "domain": "大厂 AI 动态",
    "title": "Beyond Siri: Here are the practical AI features coming to your iPhone in iOS 27",
    "url": "https://techcrunch.com/2026/06/21/beyond-siri-here-are-the-practical-ai-features-coming-to-your-iphone-in-ios-27/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T14:40:28+00:00",
    "summary": "Siri’s AI overhaul may have grabbed the headlines at WWDC, but some of Apple’s most useful AI features are arriving elsewhere in iOS 27."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/20/signals-meredith-whittaker-wants-you-to-remember-that-ai-chatbots-are-not-your-friends/",
    "domain": "大厂 AI 动态",
    "title": "Signal’s Meredith Whittaker wants you to remember that AI chatbots ‘are not your friends’",
    "url": "https://techcrunch.com/2026/06/20/signals-meredith-whittaker-wants-you-to-remember-that-ai-chatbots-are-not-your-friends/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T20:32:29+00:00",
    "summary": "\"These are not your friends. These are not conscious beings. These are not sentient interlocutors.”"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/20/in-the-weights-is-your-new-ai-centric-vanity-search/",
    "domain": "大厂 AI 动态",
    "title": "In the Weights is your new AI-centric vanity search",
    "url": "https://techcrunch.com/2026/06/20/in-the-weights-is-your-new-ai-centric-vanity-search/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T19:41:11+00:00",
    "summary": "So ... what's your In the Weights score?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/20/founders-funds-outlier-bet-on-humanely-killed-fish/",
    "domain": "大厂 AI 动态",
    "title": "Founders Fund’s outlier bet on humanely killed fish",
    "url": "https://techcrunch.com/2026/06/20/founders-funds-outlier-bet-on-humanely-killed-fish/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T18:26:02+00:00",
    "summary": "Shinkei makes a refrigerator-sized robot called Poseidon to kill fish quickly and humanely."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/20/nobel-laureate-john-jumper-is-leaving-deepmind-for-rival-anthropic/",
    "domain": "大厂 AI 动态",
    "title": "Nobel laureate John Jumper is leaving DeepMind for rival Anthropic",
    "url": "https://techcrunch.com/2026/06/20/nobel-laureate-john-jumper-is-leaving-deepmind-for-rival-anthropic/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T16:39:57+00:00",
    "summary": "Jumper isn't the only big name leaving Google DeepMind."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/20/every-new-ios-27-feature-thats-worth-knowing-about/",
    "domain": "大厂 AI 动态",
    "title": "Every new iOS 27 feature that’s worth knowing about",
    "url": "https://techcrunch.com/2026/06/20/every-new-ios-27-feature-thats-worth-knowing-about/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T15:00:00+00:00",
    "summary": "While it's not flashy like Apple’s new Siri AI and Apple Intelligence upgrades, there are still a number of additions to iOS 27 worth looking at."
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
    "summary": "An eminently binge-able series that honors classic horror tropes while reinventing them in surprising ways"
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/the-uk-will-scan-asylum-seekers-faces-for-age-checks-despite-knowing-the-tech-is-flawed/",
    "domain": "大厂 AI 动态",
    "title": "The UK will scan asylum-seekers’ faces for age checks—despite knowing the tech is flawed",
    "url": "https://arstechnica.com/tech-policy/2026/06/the-uk-will-scan-asylum-seekers-faces-for-age-checks-despite-knowing-the-tech-is-flawed/",
    "source": "Matt Burgess, Maddy Varner, May Bulman, Gabriel Geiger, WIRED.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T11:15:09+00:00",
    "summary": "Tests of age-verification technology show the risks of life-altering errors."
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
    "id": "rss:https://www.producthunt.com/products/mediaseg",
    "domain": "大厂 AI 动态",
    "title": "MediaSeg",
    "url": "https://www.producthunt.com/products/mediaseg",
    "source": "Sho Nishikawa, ExaEdge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T00:40:36+00:00",
    "summary": "Split large media files into upload-ready chunks on macOS Discussion | Link"
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
    "id": "rss:https://www.producthunt.com/products/cloudflare",
    "domain": "大厂 AI 动态",
    "title": "Cloudflare Temporary Accounts",
    "url": "https://www.producthunt.com/products/cloudflare",
    "source": "Zac Zuo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T03:39:10+00:00",
    "summary": "Let agents deploy before signup Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/alai",
    "domain": "大厂 AI 动态",
    "title": "Alai 2.0",
    "url": "https://www.producthunt.com/products/alai",
    "source": "Krishna Gupta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T18:25:40+00:00",
    "summary": "AI design partner for presentations, social posts, and more Discussion | Link"
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
    "id": "rss:https://www.producthunt.com/products/oioi",
    "domain": "大厂 AI 动态",
    "title": "oioi",
    "url": "https://www.producthunt.com/products/oioi",
    "source": "Vishesh Yadav",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T15:05:27+00:00",
    "summary": "a fast, glassy clipboard manager for macOS, Windows & Linux Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/agent-37-38",
    "domain": "大厂 AI 动态",
    "title": "Agent 37 Cloud",
    "url": "https://www.producthunt.com/products/agent-37-38",
    "source": "fmerian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T19:03:23+00:00",
    "summary": "Give every customer their own Hermes or OpenClaw agent Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/notchkin",
    "domain": "大厂 AI 动态",
    "title": "Notchkin",
    "url": "https://www.producthunt.com/products/notchkin",
    "source": "Danny Stankowski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T23:28:02+00:00",
    "summary": "A notes app that lives in your MacBook's notch. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/cloudback",
    "domain": "大厂 AI 动态",
    "title": "Cloudback MCP Server",
    "url": "https://www.producthunt.com/products/cloudback",
    "source": "Evgeniy Kosjakov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T20:46:39+00:00",
    "summary": "Manage your backups from Claude, Cursor, and VS Code Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/poolside",
    "domain": "大厂 AI 动态",
    "title": "Laguna by Poolside",
    "url": "https://www.producthunt.com/products/poolside",
    "source": "fmerian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T15:00:44+00:00",
    "summary": "Foundation models for agentic coding and long-horizon work Discussion | Link"
  },
  {
    "id": "rss:https://36kr.com/p/3864065855706120?f=rss",
    "domain": "大厂 AI 动态",
    "title": "氪星晚报｜赢创计划全球裁员3200人；台积电28nm较年初减产25%；三星电子向韩国所有员工开放ChatGPT和Codex",
    "url": "https://36kr.com/p/3864065855706120?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T08:26:13+00:00",
    "summary": "大公司： 赢创计划全球裁员3200人 赢创近日宣布，将延长“赢创定制”增效计划，涉及赢创全球所有业务及职能部门，拟裁减约3200个岗位，其中德国本土约占2150个。相关措施计划于2027年启动，持续至2029年底。6月22日，赢创确认，德国以外地区将削减1050个职位，中国区包含在内，但具体裁员数量尚未明确。“赢创定制”计划于2023年10月推出，原定目标为2026年底前累计削减约2800个岗位。"
  },
  {
    "id": "rss:https://36kr.com/p/3864054145209602?f=rss",
    "domain": "大厂 AI 动态",
    "title": "圆桌论坛：在没人相信之前，乘风破浪的创er | 36氪WAVES2026新浪潮",
    "url": "https://36kr.com/p/3864054145209602?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T08:10:06+00:00",
    "summary": "每一个创业者，都有一段“没人相信”的日子。但正是那段日子，把他们推向了浪尖。创业是鲜活的，接下来这一场，我们听一听那些在质疑声中长大的创业者，怎么把“不可能”变成“不，可能”。 以下为圆桌对话内容，经36氪整理编辑: 许嘉婧｜36氪后浪研究所 主理人（主持人） 徐子悦 ｜PhotonPay 光子易商务副总裁 程刚｜KOOK语音 创始人兼CEO 徐良威｜智域基石CTO 程二亭｜万拿机器人 创始人&a"
  },
  {
    "id": "rss:https://36kr.com/p/3864033017549832?f=rss",
    "domain": "大厂 AI 动态",
    "title": "圆桌讨论：在番禺，我们造了什么？｜36氪WAVES2026新浪潮",
    "url": "https://36kr.com/p/3864033017549832?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T07:38:54+00:00",
    "summary": "“2026年，创投圈的浪潮再次翻涌：AI从技术概念走进产业深水区，硬科技创业从“小众赛道” 变成“主流共识”，年轻的创业者们正在用代码和双手，重新定义中国创新的未来坐标。 每一年，由36氪 · 暗涌主办的WAVES大会，都是中国创投圈的年度风向标。今年的 WAVES 2026以“今年盛夏”为主题，落地广州番禺良仓新造创意园，在两天的时间里，我们汇聚了顶级投资人、产业领袖、新锐创业者，用14场深度圆"
  },
  {
    "id": "rss:https://36kr.com/p/3864002982286342?f=rss",
    "domain": "大厂 AI 动态",
    "title": "HORWIN号外品牌创始人兼CEO周维：为进化而生，HORWIN的全球出行愿景 | 36氪WAVES2026新浪潮",
    "url": "https://36kr.com/p/3864002982286342?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T07:08:07+00:00",
    "summary": "“2026年，创投圈的浪潮再次翻涌：AI从技术概念走进产业深水区，硬科技创业从“小众赛道” 变成“主流共识”，年轻的创业者们正在用代码和双手，重新定义中国创新的未来坐标。 每一年，由36氪 · 暗涌主办的WAVES大会，都是中国创投圈的年度风向标。今年的 WAVES 2026以“今年盛夏”为主题，落地广州番禺良仓新造创意园，在两天的时间里，我们汇聚了顶级投资人、产业领袖、新锐创业者，用14场深度圆"
  },
  {
    "id": "rss:https://36kr.com/p/3863967437247751?f=rss",
    "domain": "大厂 AI 动态",
    "title": "补齐市场信息差！36氪股市舆情交流群开放，实物抽奖等你来！",
    "url": "https://36kr.com/p/3863967437247751?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T06:56:09+00:00",
    "summary": "一、36氪官方大数据股市舆情工具介绍 36氪企业全情报是36氪联合红麦数据推出的专业资本市场情报平台，依托全网大数据资源，实时同步个股、产业一手资讯，同时通过智能算法识别行情潜藏风险，一站式查询板块、个股完整消息脉络。 小程序直达链接，手机端可直接打开使用，无需下载任何软件： &nbsp;https://channel.36kr.com/api/x/wechat/urlLink?channelId"
  },
  {
    "id": "rss:https://36kr.com/p/3863849524859911?f=rss",
    "domain": "大厂 AI 动态",
    "title": "广州市番禺协诚实业有限公司副总经理龙德洋：真正的城市服务，藏在分分秒秒的坚守里",
    "url": "https://36kr.com/p/3863849524859911?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T05:52:45+00:00",
    "summary": "“2026年，创投圈的浪潮再次翻涌：AI从技术概念走进产业深水区，硬科技创业从“小众赛道” 变成“主流共识”，年轻的创业者们正在用代码和双手，重新定义中国创新的未来坐标。 每一年，由36氪 · 暗涌主办的WAVES大会，都是中国创投圈的年度风向标。今年的 WAVES 2026以“今年盛夏”为主题，落地广州番禺良仓新造创意园，在两天的时间里，我们汇聚了顶级投资人、产业领袖、新锐创业者，用14场深度圆"
  },
  {
    "id": "rss:https://36kr.com/p/3863885024973832?f=rss",
    "domain": "大厂 AI 动态",
    "title": "36氪首发 | 联想之星险峰联合领投，AI算力中心感知与效能管理方案商完成天使轮融资",
    "url": "https://36kr.com/p/3863885024973832?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T05:07:50+00:00",
    "summary": "作者&nbsp;|&nbsp;乔钰杰 编辑&nbsp;|&nbsp;袁斯来 硬氪获悉，芯感通科技有限公司（以下简称“芯感通”）日前完成数千万元天使轮融资，由联想之星与险峰联合领投。本轮融资将主要用于芯片研发迭代、产品验证及市场拓展。 随着大模型训练规模持续扩大和商业服务展开，AI算力基础设施的铺设在快速亟需高效能运营，同时，高性能GPU也将算力推入高能量密度、高功耗时代。 从单柜数十张GPU到万卡"
  },
  {
    "id": "rss:https://36kr.com/p/3863883390194692?f=rss",
    "domain": "大厂 AI 动态",
    "title": "36氪首发 | 核心团队曾攻关国家重点大飞机装配，航空航天智能装备商完成数千万元融资",
    "url": "https://36kr.com/p/3863883390194692?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T05:06:22+00:00",
    "summary": "作者&nbsp;|&nbsp;乔钰杰 编辑&nbsp;|&nbsp;袁斯来 硬氪获悉，大飞机智能装配装备企业大连坤达自动化有限公司（以下简称“大连坤达”）今日完成数千万元A轮融资，投资方为泰州永鑫融堰创业投资合伙企业（有限合伙）（以下简称“永鑫方舟”），大桉资本担任独家财务顾问。本轮资金将主要用于新一代智能装配系统研发、核心产品产能扩充及补充流动资金。 大连坤达成立于2016年，主要面向航空航天等"
  },
  {
    "id": "rss:https://36kr.com/p/3863840829576192?f=rss",
    "domain": "大厂 AI 动态",
    "title": "海川资本创始合伙人曹抒阳：新地缘格局下，中国能源电力产业的星辰大海：算力基建、能源自主、新本土化浪潮 | 36氪WAVES2026新浪潮",
    "url": "https://36kr.com/p/3863840829576192?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T04:23:47+00:00",
    "summary": "“2026年，创投圈的浪潮再次翻涌：AI从技术概念走进产业深水区，硬科技创业从“小众赛道” 变成“主流共识”，年轻的创业者们正在用代码和双手，重新定义中国创新的未来坐标。 每一年，由36氪 · 暗涌主办的WAVES大会，都是中国创投圈的年度风向标。今年的 WAVES 2026以“今年盛夏”为主题，落地广州番禺良仓新造创意园，在两天的时间里，我们汇聚了顶级投资人、产业领袖、新锐创业者，用14场深度圆"
  },
  {
    "id": "rss:https://36kr.com/p/3863831007941638?f=rss",
    "domain": "大厂 AI 动态",
    "title": "淘宝闪购上线新业务\"家宴\"，联合米其林高星餐厅｜独家",
    "url": "https://36kr.com/p/3863831007941638?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T04:14:54+00:00",
    "summary": "文丨彭倩 编辑丨乔芊 36氪独家获悉，淘宝闪购近日在成都、深圳两地启动了一项名为\"家宴\"的高端外卖项目，目前正在灰测中，首批参与的有潮上潮（米其林三星）、许家菜（米其林一星）、柴门荟（米其林一星）、梓楠、王捌院子5个头部中餐品牌，共9家门店。 据了解，后续新荣记（米其林三星）、如院（米其林二星）等品牌也已确认加入。家宴预计将在今年8月前向北京、上海、杭州等城市逐步开放。 从目前的信息来看，淘宝闪购"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3864126988145666?f=rss",
    "domain": "大厂 AI 动态",
    "title": "金融监管总局联合中国人民银行、中国证监会召开金融消费者和投资者保护监管联络员会议",
    "url": "https://36kr.com/newsflashes/3864126988145666?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T09:13:14+00:00",
    "summary": "36氪获悉，近日，金融监管总局联合中国人民银行、中国证监会召开第四次金融消费者和投资者保护监管联络员会议。会议研究了金融消保制度规划以及近期跨领域金融消保和投保重点问题，通报了金融消保和投保领域国际交流与合作情况。会议强调，金融管理部门要持续加强常态化会商会晤、信息共享和协同共治，坚持问题导向，聚焦金融消费者和投资者集中反映的重点领域问题��紧密协作、齐抓共管，共同做好规范金融产品网络营销、个人贷"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3864126176875529?f=rss",
    "domain": "大厂 AI 动态",
    "title": "中国银行：自6月24日收盘清算时起，黄金延期合约保证金比例乘数由666%调整为800%",
    "url": "https://36kr.com/newsflashes/3864126176875529?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T09:12:24+00:00",
    "summary": "36氪获悉，中国银行发布《关于代理个人上金所业务调整部分延期合约业务参数的公告》。根据贵金属风险管理和业务需要，中国银行将对代理个人上金所业务（包括白银延期合约和黄金延期合约）的交易保证金比例进行调整。具体如下：一、自2026年6月24日（星期三）收盘清算时起，中国银行黄金延期合约的保证金比例乘数由666%调整为800%，由此，中国银行黄金延期合约的客户保证金比例由99.9%调整为120%。二、自"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3864120698622984?f=rss",
    "domain": "大厂 AI 动态",
    "title": "四川能源新型能源集团增资至约48.4亿",
    "url": "https://36kr.com/newsflashes/3864120698622984?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T09:06:50+00:00",
    "summary": "36氪获悉，天眼查App显示，近日，四川川投新能源有限公司发生工商变更，企业名称变更为四川能源新型能源集团有限公司，张鹏举卸任法定代表人，由杨昌斌接任，同时，注册资本由28亿人民币增至约48.4亿人民币，增幅约73%。该公司成立于2022年2月，经营范围包括发电技术服务、太阳能发电技术服务、风力发电技术服务等，由四川能源发展集团有限责任公司全资持股。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3864117497074690?f=rss",
    "domain": "大厂 AI 动态",
    "title": "上海亚虹：终止筹划控制权变更事项，股票将于23日复牌",
    "url": "https://36kr.com/newsflashes/3864117497074690?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T09:03:35+00:00",
    "summary": "36氪获悉，上海亚虹公告，控股股东海南宁生旅游集团因交易对方内部未能达成一致，终止筹划控制权变更事项。公司股票将于6月23日开市起复牌，目前公司各项业务经营正常，该事项不会对公司经营业绩和财务状况产生重大不利影响。"
  },
  {
    "id": "wscn:3775193",
    "domain": "股票",
    "title": "财政部：前5月全国一般公共预算收入超10万亿元，证券交易印花税同比大增88.8%",
    "url": "https://wallstreetcn.com/articles/3775193",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T09:12:05+00:00",
    "summary": "1—5月全国一般公共预算收入100465亿元，同比增长4%，支出113877亿元，同比增长0.8%。税收收入中，国内增值税、个人所得税等增长较快，证券交易印花税同比大增88.8%；而契税、土地增值税等有所下降。"
  },
  {
    "id": "wscn:3775195",
    "domain": "股票",
    "title": "斯塔默辞职！英国首相再换人，十年或迎第七任首相",
    "url": "https://wallstreetcn.com/articles/3775195",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T09:08:17+00:00",
    "summary": "英国首相斯塔默于6月22日宣布辞去工党党首职务，将在新领导人产生前留任首相。此举源于党内持续“逼宫”及支持率下滑，距其大选获胜尚不足两年。工党将于7月启动候选人提名，预计9月前产生新党首。呼声最高的接班人为大曼彻斯特市长安迪·伯纳姆。此次更替后，英国将迎来十余年间第七位首相。"
  },
  {
    "id": "wscn:3775196",
    "domain": "股票",
    "title": "美联储转鹰、华尔街纷纷投降，花旗成“最后的倔强”：坚持10月重启降息",
    "url": "https://wallstreetcn.com/articles/3775196",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T08:56:46+00:00",
    "summary": "花旗认为，美联储下一步行动是降息而非加息，基准情景为10月降息25个基点，随后12月和2027年1月再各降25个基点。其核心逻辑在于：油价急速下跌正消除通胀上行风险，失业金人数上升预示劳动力市场季节性走弱，且核心PCE的强势受股价推升，属于各类通胀指标中的“异常值”，不反映广义消费价格压力。"
  },
  {
    "id": "wscn:3775194",
    "domain": "股票",
    "title": "内存涨价冲击，高盛下调手机全球出货预期",
    "url": "https://wallstreetcn.com/articles/3775194",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T08:50:59+00:00",
    "summary": "内存价格飙升成压垮需求的\"最后一根稻草\"——高盛将2026年全球智能手机出货量预测骤降至11.4亿部，同比跌幅从-6%扩大至-10%。但高端化浪潮逆势托底，市场总价值仍将突破5,957亿美元，折叠屏赛道更因苹果入局暗藏爆发潜力。"
  },
  {
    "id": "wscn:3775198",
    "domain": "股票",
    "title": "公告暂停2年分红，这家险企成不分红“吃螃蟹”者",
    "url": "https://wallstreetcn.com/articles/3775198",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T08:48:44+00:00",
    "summary": "增强公司资本实力"
  },
  {
    "id": "wscn:3775197",
    "domain": "股票",
    "title": "27年王者让位：SK海力士市值首超三星，一场AI驱动的韩国芯片权力重构",
    "url": "https://wallstreetcn.com/articles/3775197",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T08:46:20+00:00",
    "summary": "2026年6月22日，曾负债140亿美元、濒临破产的SK海力士，市值首次超越统治韩国资本市场27年的三星电子，登顶韩国\"市值一哥\"。背后是一场精准的历史性赌注——当AI浪潮将HBM从边缘产品推至算力核心，SK海力士以59%的市场份额、每天净赚逾20亿元人民币的惊人成绩，完成了商业史上最震撼的逆袭。"
  },
  {
    "id": "wscn:3775154",
    "domain": "股票",
    "title": "沪指涨近2%，全市场成交额历史第二，培育钻石飙升，大金融崛起，恒科指跌超1%，智谱暴涨15%市值破万亿港元",
    "url": "https://wallstreetcn.com/articles/3775154",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T08:32:13+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市超2900股飘红，今日成交3.76万亿，位列A股历史第二成交天量。沪深两市成交额3.74万亿，创历史第二，较上一个交易日放量超4200亿。板块方面，大金融午后崛起，券商、保险领涨；有色金属、化工板块掀涨停潮，半导体产业链持续走强，金融科技、培育钻石概念股活跃。机器人、商业航天、创新药题材走弱。"
  },
  {
    "id": "wscn:3775190",
    "domain": "股票",
    "title": "高盛首次覆盖瑞幸即看多：价格战中逆势扩张，大陆市场5.5万家门店目标可期",
    "url": "https://wallstreetcn.com/articles/3775190",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T08:27:58+00:00",
    "summary": "高盛首次覆盖瑞幸咖啡并给予买入评级，目标价49美元，较现价隐含61%上行空间。高盛认为，手握9800万月活用户、均价仅14元的瑞幸护城河远比市场认知更深，5.5万家门店目标尚未触顶；随着库迪价格战退潮、外卖补贴正常化，利润率修复叠加3亿美元回购计划，多重催化剂正在聚集。"
  },
  {
    "id": "wscn:3775156",
    "domain": "股票",
    "title": "美伊达成协议文件，美股盘前芯片股集体走高，英镑逼近年内低位，油价冲高回落，金价反弹",
    "url": "https://wallstreetcn.com/articles/3775156",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T08:27:00+00:00",
    "summary": "标普500期货基本持平，美元小幅走强，美债收益率沿整条曲线上行。SpaceX美股盘前下跌4.6%。布伦特原油下跌约1.5%，逼近每桶79美元。当地时间6月22日，英国首相斯塔默宣布辞职。英镑逼近2026年年内最低水平，英国10年期国债收益率小幅回落1个基点至4.83%，此前连续两日上涨的走势暂告中断。"
  },
  {
    "id": "wscn:3775187",
    "domain": "股票",
    "title": "闪迪新专利曝光：处理器直接键合NAND闪存芯片，HBM退居辅助角色",
    "url": "https://wallstreetcn.com/articles/3775187",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T08:16:36+00:00",
    "summary": "闪迪最新专利揭示一项激进存储革命：将多核处理器与NAND闪存直接键合，构建3D堆叠架构，同时将HBM从\"核心主角\"降格为\"辅助配角\"。这一设计剑指HBM容量天花板与现有高带宽闪存的延迟痛点，若落地将从根本上重塑AI加速器的内存架构逻辑，存储与计算深度融合的时代或已提前到来。"
  },
  {
    "id": "wscn:3775137",
    "domain": "股票",
    "title": "K 型分化加剧：科技红利狂飙，消费红利何时到来？",
    "url": "https://wallstreetcn.com/premium/articles/3775137?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T08:15:19+00:00",
    "summary": "消费修复仍缓、科技投资持续扩张，中国经济中期将呈现消费筑底、科技向上的K型分化新常态。"
  },
  {
    "id": "wscn:3775192",
    "domain": "股票",
    "title": "纸尿裤甲酰胺风波追踪：代工产业链隐性风险浮水",
    "url": "https://wallstreetcn.com/articles/3775192",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T08:12:05+00:00",
    "summary": "争议未决"
  },
  {
    "id": "wscn:3775181",
    "domain": "股票",
    "title": "“后悔批准上市”！韩国拟对三星和SK海力士杠杆ETF采取单独措施",
    "url": "https://wallstreetcn.com/articles/3775181",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T08:09:24+00:00",
    "summary": "韩国金融监督院拟联手多方协调合作，评估包括强化交易模式监控在内的一系列稳定举措，以限制杠杆ETF剧烈波动可能造成的损失蔓延。AI热潮推动下，三星与SK海力士杠杆ETF规模在不到一个月内激增至91亿美元，散户高度集中。韩国金融监管机构负责人后悔让三星、SK海力士杠杆ETF上线。"
  },
  {
    "id": "wscn:3775184",
    "domain": "股票",
    "title": "商品传奇Rick Rule：铜油都便宜得超乎想象，铀将是AI狂飙的“意外赢家”，无法确认黄金底部已出现",
    "url": "https://wallstreetcn.com/articles/3775184",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T08:06:24+00:00",
    "summary": "当科技巨头砸万亿美元狂建AI数据中心，自然资源大师Rick Rule却盯上了另一条财富密道：铜与石油因30年投资不足正面临供给断层，价格暴涨已是宿命；而铀，这个被市场遗忘的金属，正凭借\"24/7零碳电力\"的硬刚需，悄然成为AI竞赛最确定的隐形赢家。"
  },
  {
    "id": "wscn:3775191",
    "domain": "股票",
    "title": "京东70万蓝领的涅槃账本：快递员去修机器人，可行性有多高？",
    "url": "https://wallstreetcn.com/articles/3775191",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T08:00:14+00:00",
    "summary": "劳动密集型巨头直面自动化拐点。"
  },
  {
    "id": "wscn:3775183",
    "domain": "股票",
    "title": "目标1nm制程！“马桶大王”TOTO投资800亿日元押注半导体材料",
    "url": "https://wallstreetcn.com/articles/3775183",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T07:37:50+00:00",
    "summary": "日本卫浴巨头TOTO计划未来五年投入800亿日元扩大半导体材料业务，研发并扩产用于1纳米制程芯片制造的静电卡盘等核心陶瓷产品。受益于AI芯片需求爆发，该板块已贡献超半数利润，推动TOTO实现从传统卫浴到先进半导体供应链核心的跨界转型。"
  },
  {
    "id": "wscn:3775188",
    "domain": "股票",
    "title": "曹操出行接入豆包打车灰测  AI助手正探索更多场景",
    "url": "https://wallstreetcn.com/articles/3775188",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T07:35:59+00:00",
    "summary": "此前测试购物与团购。"
  },
  {
    "id": "wscn:3775171",
    "domain": "股票",
    "title": "建筑行业：中东重建大幕开启，建筑央企加速奔赴万亿新战场",
    "url": "https://wallstreetcn.com/premium/articles/3775171?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T07:27:58+00:00",
    "summary": "从“一带一路”到中东重建，中国建筑行业迎来破局与重塑的历史性机遇。"
  },
  {
    "id": "wscn:3775178",
    "domain": "股票",
    "title": "伊朗战争以来首次！科威特石油公司重启港口石脑油招标",
    "url": "https://wallstreetcn.com/articles/3775178",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T07:24:37+00:00",
    "summary": "科威特国家石油公司已发出招标，出售7月从科威特港口装载的石脑油现货货物。这不仅是该公司自美伊冲突爆发以来首次恢复本土港口现货销售，也标志着此前通过海外转运的供应链迎来实质性正常化。"
  },
  {
    "id": "wscn:3775186",
    "domain": "股票",
    "title": "智谱冲上万亿，市场在为什么买单？",
    "url": "https://wallstreetcn.com/articles/3775186",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T07:23:56+00:00",
    "summary": "智谱市值冲破万亿港元，市销率高达1300倍。市场买的不是财报，而是\"中国AI拿下性价比层\"的行业期权。涨价83%、调用量反增400%——这份罕见的定价权，正将万亿叙事一步步兑现为看得见的基本面。"
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
