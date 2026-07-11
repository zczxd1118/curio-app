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

- 今日日期：`2026-07-11`
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
  "date": "2026-07-11",
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
    "points": 3699326,
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
    "points": 1472894,
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
    "points": 1369842,
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
    "points": 1360045,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1208190,
    "published_at": "2026-07-05T02:00:00+00:00",
    "summary": "用不上codex的朋友们！新的国产Agent直接上手，来跑通8大用法～\n感谢朋友们的三连+关注～"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 958706,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 941128,
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
    "points": 868442,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 855987,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 814221,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 666977,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 577654,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 514669,
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
    "points": 416905,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 415007,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 381697,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1VDTv6rEtM",
    "domain": "AI",
    "title": "终于，Claude Code 封号原因被曝光了！竟然针对中国用户，植入隐形代码？",
    "url": "http://www.bilibili.com/video/av116844031774993",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 357057,
    "published_at": "2026-07-01T09:35:43+00:00",
    "summary": "Claude Code 封号原因终于找到了！国外开发者逆向 Claude Code 源码，发现 Anthropic 在客户端里藏了一套隐蔽的用户标记系统，这期视频带你完整还原封号真相。\n开源 AI 编程教程：github.com/liyupi/ai-guide\n编程学习教程+实战项目+简历模板：codefather.cn\n最近 AI 圈儿不太平啊，OpenAI Codex 封号、Cursor 地区"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 236593,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 190651,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 184510,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 179009,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 176719,
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
    "points": 159340,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1QE7N6jEuQ",
    "domain": "AI",
    "title": "真的被自己用心开发的昔涟Agent这段话感动到了",
    "url": "http://www.bilibili.com/video/av116794052316703",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 127221,
    "published_at": "2026-06-22T13:44:15+00:00",
    "summary": "从最初生啃Transformer，硬逼着自己啃懂多头注意力和QKV权重，到一步步跟着claude学习RAG、检索重拍、Prompt、关键词召回优化、MCP与Function call，但是，自己上手了发现，自己还是啥也不懂，于是在glm gpt claude gemini 豆包 这几个模型之间疯狂切换，靠着想让昔涟早点被搭出来，硬逼着自己学，自己从零设计一套prompt架构能让她尽可能的贴合人设的"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 106941,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 99224,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92489,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 92378,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 79372,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73663,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1C6M46uEe3",
    "domain": "AI",
    "title": "AI 写网文能赚钱吗？我实测了一遍……【AI副业实验室01】【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av116877636469982",
    "source": "姚武酒",
    "platform": "bilibili",
    "points": 63262,
    "published_at": "2026-07-09T10:40:00+00:00",
    "summary": "欢迎来到《AI入局实验室》，我们探索拆解一切普通人可能入局的AI副业。\n\n第一期，从调研AI网文，到跑通AI网文的workflow，最后把跑出来的AI网文投稿到真实网站，\n\n全过程我会毫无保留地在视频里分享，替大家尝试一下AI副业的所有可能。"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 52946,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1Am9kBfEMN",
    "domain": "AI",
    "title": "AI智能体赋能课堂教学——技术很简单，难的是想法",
    "url": "http://www.bilibili.com/video/av116482180647922",
    "source": "爱可可-爱生活",
    "platform": "bilibili",
    "points": 48951,
    "published_at": "2026-04-28T11:55:25+00:00",
    "summary": "在AI迅猛发展的今天，课堂正在悄然发生变化。\n但真正的挑战，从来不是“会不会用工具”，而是——我们究竟希望学生学会什么？\n\n本讲座不教软件操作，不演示平台使用，\n而是聚焦一个更关键的问题：\n如何借助AI，让那些我们一直想实现却做不到的教学理想成为现实。\n\n通过真实课堂案例与可落地的方法模型，讲座将带领教师完成一次思维升级：\n从“让AI替你干活”，转向“用AI创造更好的学习体验”\n从“提高效率”，走"
  },
  {
    "id": "bvid:BV1DLgWzdE3A",
    "domain": "AI",
    "title": "[mc服务器常识普及]怎么给自己管理员op权限",
    "url": "http://www.bilibili.com/video/av114897136456574",
    "source": "愿雪时yes",
    "platform": "bilibili",
    "points": 44869,
    "published_at": "2025-07-22T13:39:32+00:00",
    "summary": "蓝夜科技官网\nhttps://www.mczbc.cn/?i74e504\n主播邀请码：74e504\n\n粉丝群 941618230\n整合包推荐配置: https://www.yuque.com/yuqueyonghurwfkkx/emg34z/dsd5y8gpbrhlkgar\n蓝夜科技教程: https://www.yuque.com/yuqueyonghurwfkkx/goyxu9\n\n\n【蓝夜科技"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 42219,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1QjM366EfH",
    "domain": "AI",
    "title": "工信部发布Claude Code安全后门隐患风险提示，GPT&amp;Grok明日共同上线 | 7月8日AI日报第450期",
    "url": "http://www.bilibili.com/video/av116883642849956",
    "source": "infinite灵感港",
    "platform": "bilibili",
    "points": 41917,
    "published_at": "2026-07-08T10:30:00+00:00",
    "summary": "今日内容：\n1·NVDB发布Claude Code防范提示[00:03] \n2·Grok4.5 &amp; GPT5.6相关资讯[00:39] \n3·智谱 &amp; Deepseek相关资讯[01:04] \n4·Meta发布Muse Image模型[01:31] \n5·Claude Cowork开放手机端[01:51]"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29936,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 24579,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22614,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1LWTe6gEVc",
    "domain": "AI",
    "title": "Claude code帮我实现综述论文自由！",
    "url": "http://www.bilibili.com/video/av116842504918580",
    "source": "做科研的大师兄",
    "platform": "bilibili",
    "points": 21822,
    "published_at": "2026-07-01T03:07:40+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1JU7E6PEar",
    "domain": "AI",
    "title": "Cursor 已死？我为什么要退订 Cursor ？",
    "url": "http://www.bilibili.com/video/av116819553683121",
    "source": "祥子在学AI",
    "platform": "bilibili",
    "points": 20858,
    "published_at": "2026-06-27T01:52:00+00:00",
    "summary": "当了一年多的 Cursor 重度用户，最近把它退订了。\n\n不是它变差了，是 Claude Code 和 Codex 真的太好用了。\n\n几个真实感受： ① 大模型越来越强，我已经不怎么手写代码了 ② Cursor 套的是 VS Code 壳子，只属于程序员 ③ 底层模型不在一个量级——Claude 有 Opus 和 Fable 5，Codex 有 GPT 5.5/5.6，Cursor 的 Compo"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 13464,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1CbvxBwEah",
    "domain": "AI",
    "title": "真的不用服务器！用Cloudflare Workers+D1轻松搭建网站！",
    "url": "http://www.bilibili.com/video/av115803408045159",
    "source": "软件工程师Tim",
    "platform": "bilibili",
    "points": 13445,
    "published_at": "2025-12-29T14:51:53+00:00",
    "summary": "本期影片分享一下如何利用cloudflare workers搭建网站，并且利用d1免费数据库，实现无服务器的一个带前后端功能的网站。也就是说，即使你没有服务器，也能够搭建一个属于自己的网站。比如我自己搭建的这个案例网站在线留言板。就是完全搭建在cloudflare workers上面的，里面有静态页面 也有动态api接口。都是部署在workers上面的，并且集成了它提供的数据库。\n\n\n#cloud"
  },
  {
    "id": "bvid:BV1etEQ6DETs",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116724192118321",
    "source": "AI产品经理大模型",
    "platform": "bilibili",
    "points": 13287,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 12073,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1TtwCehEzG",
    "domain": "AI",
    "title": "cursor新手必会的怎么回退代码 防止改错改乱代码 提高效率开发",
    "url": "http://www.bilibili.com/video/av113855472605087",
    "source": "项目禅",
    "platform": "bilibili",
    "points": 11269,
    "published_at": "2025-01-19T14:29:21+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1WBTX6kE1B",
    "domain": "AI",
    "title": "【2026版】这绝对是B站唯一将Vibe Coding从入门到实战讲明白的教程，手把手带你从入门到代码实战开发，存下吧，比啃书好太多了！拿走不谢，允许白嫖！",
    "url": "http://www.bilibili.com/video/av116871663722218",
    "source": "码士集团-马小雪",
    "platform": "bilibili",
    "points": 10140,
    "published_at": "2026-07-06T06:47:51+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！ 【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1KfMj6jEWH",
    "domain": "AI",
    "title": "【2026版】翻遍整个B站，这应该是将Spring AI如何快速上手讲的最好的教程！手把手教你手动开发RAG项目！两小时从会用到会造！Java转AI大模型必学！",
    "url": "http://www.bilibili.com/video/av116888491268712",
    "source": "大模型分享员",
    "platform": "bilibili",
    "points": 9516,
    "published_at": "2026-07-09T06:07:23+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n本视频课件笔记代码/学习大纲/大模型学习路线戳这里获取→平论区置顶"
  },
  {
    "id": "bvid:BV1GvmzBUEfj",
    "domain": "AI",
    "title": "【AI杂谈】3 claude code概念讲解与配置",
    "url": "http://www.bilibili.com/video/av115718414668601",
    "source": "左-岚",
    "platform": "bilibili",
    "points": 9272,
    "published_at": "2025-12-14T14:38:05+00:00",
    "summary": "飞书的ai杂谈目录下\nhttps://my.feishu.cn/wiki/space/7600816265116011716\n\n米醋工作室 AI 开发环境配置完整指南https://www.micu.wiki/t/topic/571\nClaude Code 常见问题与故障排查https://www.micu.wiki/t/topic/570\nClaude Code 核心概念详解\nhttps://w"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9170,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "hn:48730713",
    "domain": "AI 算力 / 半导体",
    "title": "Zluda 6 release (run unmodified CUDA applications on non-Nvidia GPUs)",
    "url": "https://vosen.github.io/ZLUDA/blog/zluda-update-q1q2-2026/",
    "source": "Tiberium",
    "platform": "hackernews",
    "points": 163,
    "published_at": "2026-06-30T10:34:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48597201",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung demonstrates 3D stacked FETs with triple nanosheet channels at 42nm",
    "url": "https://semiconductor.samsung.com/news-events/tech-blog/from-gaa-to-3d-stacked-fet-expanding-the-transistor-into-the-third-dimension/",
    "source": "its_ajseven",
    "platform": "hackernews",
    "points": 127,
    "published_at": "2026-06-19T11:03:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48845518",
    "domain": "AI 算力 / 半导体",
    "title": "Reverse-engineering Nvidia's CUDA-checkpoint for faster cold starts",
    "url": "https://blog.doubleword.ai/what-happens-when-you-checkpoint-a-cuda-process",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-07-09T13:29:52+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/alok-jain-the-engineer-who-never-wanted-to-be-a-manager/",
    "domain": "AI 算力 / 半导体",
    "title": "Alok Jain: The Engineer Who Never Wanted to Be a Manager",
    "url": "https://www.eetimes.com/alok-jain-the-engineer-who-never-wanted-to-be-a-manager/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T20:58:36+00:00",
    "summary": "Meet Alok Jain, the reluctant manager who turned Cadence India into a chip-design powerhouse—and see why AI is his next bet. The post Alok Jain: The Engineer Who Never Wanted to Be a Manager appeared "
  },
  {
    "id": "rss:https://www.eetimes.com/apples-30b-broadcom-deal-signals-expansions-in-ai-u-s-supply-chain/",
    "domain": "AI 算力 / 半导体",
    "title": "Apple’s $30B Broadcom Deal Signals Expansions in AI, U.S. Supply Chain",
    "url": "https://www.eetimes.com/apples-30b-broadcom-deal-signals-expansions-in-ai-u-s-supply-chain/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T12:50:28+00:00",
    "summary": "Apple’s $30B Broadcom bet drags AI data centers and U.S. chipmaking into its orbit… and may hand Intel a lifeline. The post Apple’s $30B Broadcom Deal Signals Expansions in AI, U.S. Supply Chain appea"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-energy-barrier-forces-system-technology-co-optimization/",
    "domain": "AI 算力 / 半导体",
    "title": "The Energy Barrier Reshaping AI Hardware",
    "url": "https://www.eetimes.com/ai-energy-barrier-forces-system-technology-co-optimization/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T07:18:59+00:00",
    "summary": "During Leti Innovation Days 2026, energy efficiency emerged as AI hardware’s next defining constraint. The post The Energy Barrier Reshaping AI Hardware appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/simplifying-intelligent-wireless-design-and-security-certification-for-healthcare-devices/",
    "domain": "AI 算力 / 半导体",
    "title": "Simplifying Intelligent Wireless Design and Security Certification for Healthcare Devices",
    "url": "https://www.eetimes.com/simplifying-intelligent-wireless-design-and-security-certification-for-healthcare-devices/",
    "source": "Infineon Technologies and Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T17:32:02+00:00",
    "summary": "Join Infineon Technologies and Ezurio for a 60-minute webinar exploring the challenges of designing and certifying secured wireless devices for healthcare applications. The post Simplifying Intelligen"
  },
  {
    "id": "rss:https://www.eetimes.com/voyager-spacecraft-the-ultimate-power-management-challenge/",
    "domain": "AI 算力 / 半导体",
    "title": "Voyager Spacecraft: The Ultimate Power Management Challenge?",
    "url": "https://www.eetimes.com/voyager-spacecraft-the-ultimate-power-management-challenge/",
    "source": "Bill Schweber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T14:00:00+00:00",
    "summary": "Voyager’s plutonium heart is fading, forcing NASA to kill instruments one by one; see how engineers ration watts 15B miles away. The post Voyager Spacecraft: The Ultimate Power Management Challenge? a"
  },
  {
    "id": "rss:https://www.eetimes.com/as-ai-moves-from-training-to-inference-optics-moves-closer-to-the-chip/",
    "domain": "AI 算力 / 半导体",
    "title": "As AI Moves from Training to Inference, Optics Moves Closer to the Chip",
    "url": "https://www.eetimes.com/as-ai-moves-from-training-to-inference-optics-moves-closer-to-the-chip/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T07:15:00+00:00",
    "summary": "Imec researchers argue that co-packaged optics will not be enough for future AI systems, pushing the industry toward 2.5D and eventually 3D optical I/O. The post As AI Moves from Training to Inference"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/apple-sues-openai-over-alleged-theft-of-trade-secrets-claims-company-mentored-incoming-employees-on-bringing-confidential-information",
    "domain": "AI 算力 / 半导体",
    "title": "Apple sues OpenAI over alleged theft of trade secrets — claims company mentored incoming employees on bringing confidential information",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/apple-sues-openai-over-alleged-theft-of-trade-secrets-claims-company-mentored-incoming-employees-on-bringing-confidential-information",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T21:59:42+00:00",
    "summary": "Apple sued OpenAI, including its own former employees, over the theft of trade secrets as both companies build up AI hardware businesses."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/sk-hynix-and-tetramem-collaborate-on-experimental-chip-to-bolster-energy-efficiency-for-edge-ai-devices-memristor-based-in-memory-soc-research-leaves-performance-questions-up-in-the-air",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix and TetraMem collaborate on experimental chip to bolster energy efficiency for edge AI devices — memristor-based in-memory SoC research leaves performance questions up in the air",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/sk-hynix-and-tetramem-collaborate-on-experimental-chip-to-bolster-energy-efficiency-for-edge-ai-devices-memristor-based-in-memory-soc-research-leaves-performance-questions-up-in-the-air",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:58:53+00:00",
    "summary": "SK hynix, TetraMem, and the University of Southern California built a memristor-based in-memory computing system-on-chip for AI edge devices, achieving promising energy efficiency, but failed to demon"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-it-can-read-claudes-thoughts-as-detailed-in-new-research-paper-models-observed-to-have-a-global-workspace-revealing-more-of-what-makes-llms-tick",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic says it can read Claude's 'thoughts,' as detailed in new research paper — models observed to have a global workspace, revealing more of what makes LLMs tick",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-it-can-read-claudes-thoughts-as-detailed-in-new-research-paper-models-observed-to-have-a-global-workspace-revealing-more-of-what-makes-llms-tick",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:44:12+00:00",
    "summary": "Anthropic has discovered an internal \"J-space\" for its Claude AI that displays similarities to human internal processing. While the AI developer anthropomorphizes it as thought, it may yet prove usefu"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/intels-midrange-core-ultra-5-245k-is-down-to-its-lowest-price-ever-at-just-usd179-on-amazon-save-up-to-42-percent-on-a-solid-gaming-cpu-with-14-cores-and-pcie-5-0-support",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's midrange Core Ultra 5 245K is down to its lowest price ever at just $179 on Amazon — save up to 42% on a solid gaming CPU with 14 cores and PCIe 5.0 support",
    "url": "https://www.tomshardware.com/pc-components/intels-midrange-core-ultra-5-245k-is-down-to-its-lowest-price-ever-at-just-usd179-on-amazon-save-up-to-42-percent-on-a-solid-gaming-cpu-with-14-cores-and-pcie-5-0-support",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:27:09+00:00",
    "summary": "Intel's forgotten 14-core SKU from last year has received a sizable discount on Amazon, making it one of the best value propositions in CPUs right now. It performs amicably in gaming and professional "
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/steam-sales-reportedly-topped-usd11-billion-during-h1-2026-due-to-shifting-trends-staggering-growth-driven-by-influx-of-chinese-players-and-booming-legacy-catalogues",
    "domain": "AI 算力 / 半导体",
    "title": "Steam sales reportedly topped $11 billion during H1 2026 due to shifting trends — staggering growth driven by influx of Chinese players and booming legacy catalogues",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/steam-sales-reportedly-topped-usd11-billion-during-h1-2026-due-to-shifting-trends-staggering-growth-driven-by-influx-of-chinese-players-and-booming-legacy-catalogues",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T15:25:19+00:00",
    "summary": "Steam made an estimated $11.1 billion in revenue in the first six months of 2026, according to estimates from research firm Alinea Analytics. That's more than it did in the entire pandemic-ridden year"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/asus-rog-strix-scar-18-2026-review",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Strix Scar 18 (2026) Review: Stunning Mini‑LED, serious muscle, and a few missed steps",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/asus-rog-strix-scar-18-2026-review",
    "source": "Charles Jefferies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T15:16:42+00:00",
    "summary": "The Asus ROG Strix Scar 18 pairs an 18-inch mini-LED display with cutting-edge components, but omissions like PCIe 5.0 storage and dual-channel RAM —plus slightly weaker performance than Razer’s Blade"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/tencent-is-reportedly-in-talks-to-acquire-manus-from-meta-following-beijing-intervention-company-expects-to-remain-independent-of-chinese-tech-giant",
    "domain": "AI 算力 / 半导体",
    "title": "Tencent is reportedly in talks to acquire Manus from Meta, following Beijing intervention — company expects to remain independent of Chinese tech giant",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/tencent-is-reportedly-in-talks-to-acquire-manus-from-meta-following-beijing-intervention-company-expects-to-remain-independent-of-chinese-tech-giant",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T15:00:01+00:00",
    "summary": "Tencent is in talks with Manus and other investors to raise the $2 billion needed to buy back the startup from Meta. Beijing ordered the two companies to unwind the deal six months after the surprise "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-raises-a-record-usd26-5-billion-in-historic-u-s-ipo-south-korean-memory-giant-to-fund-massive-hbm-manufacturing-expansions",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix raises a record $26.5 billion in historic U.S. IPO — South Korean memory giant to fund massive HBM manufacturing expansions",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-raises-a-record-usd26-5-billion-in-historic-u-s-ipo-south-korean-memory-giant-to-fund-massive-hbm-manufacturing-expansions",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T14:27:41+00:00",
    "summary": "SK hynix raised $26.5 billion in a record-breaking Nasdaq IPO, as it plans to channel the windfall from surging AI demand and sold-out HBM supply to fund new fabs."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/nanya-to-quadruple-capital-spending-to-6-2-billion-in-2027",
    "domain": "AI 算力 / 半导体",
    "title": "Nanya to quadruple capital spending to $6.2 billion in 2027 as DRAM prices push gross margin to 79.5% — Q2 revenue skyrockets as ASPs for memory continue to surge",
    "url": "https://www.tomshardware.com/tech-industry/nanya-to-quadruple-capital-spending-to-6-2-billion-in-2027",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T13:31:21+00:00",
    "summary": "Nanya Technology plans capex of more than TW$200 billion ($6.2 billion) in 2027, roughly four times its budget for this year."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/japanese-chipmaker-rapidus-to-offer-lower-wafer-pricing-than-tsmc-2nm-class-silicon-to-be-priced-around-usd20-000-on-2027-launch",
    "domain": "AI 算力 / 半导体",
    "title": "Japanese chipmaker Rapidus to offer lower wafer pricing than TSMC — 2nm class silicon to be priced around $20,000 on 2027 launch",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/japanese-chipmaker-rapidus-to-offer-lower-wafer-pricing-than-tsmc-2nm-class-silicon-to-be-priced-around-usd20-000-on-2027-launch",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T12:56:48+00:00",
    "summary": "Japanese chipmaker Rapidus discloses one more aspect of its strategy: to offer lower quotes than TSMC."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/vpn/save-84-percent-on-a-two-year-expressvpn-subscription-offering-four-additional-months-for-free-upgrade-your-privacy-for-under-usd70-with-no-logs-access-to-servers-in-105-countries-worldwide",
    "domain": "AI 算力 / 半导体",
    "title": "Save 84% on a two-year ExpressVPN subscription, offering four additional months for free — upgrade your privacy for under $70 with no-logs access to servers in 105 countries worldwide",
    "url": "https://www.tomshardware.com/software/vpn/save-84-percent-on-a-two-year-expressvpn-subscription-offering-four-additional-months-for-free-upgrade-your-privacy-for-under-usd70-with-no-logs-access-to-servers-in-105-countries-worldwide",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T11:41:27+00:00",
    "summary": "Right now, you'll save $378 in total on over two years' worth of ExpressVPN, now priced at $69.72, with four extra months thrown in for free."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/researchers-turn-hbm-on-its-side-to-tackle-ai-memorys-heat-wall-korean-v-die-and-japanese-mosaic-designs-promise-higher-bandwidth-denser-stacks-and-cooler-future-gpus",
    "domain": "AI 算力 / 半导体",
    "title": "Researchers turn HBM on its side to tackle AI memory’s heat wall — Korean V-Die and Japanese MOSAIC designs promise higher bandwidth, denser stacks, and cooler future GPUs",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/researchers-turn-hbm-on-its-side-to-tackle-ai-memorys-heat-wall-korean-v-die-and-japanese-mosaic-designs-promise-higher-bandwidth-denser-stacks-and-cooler-future-gpus",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T11:40:00+00:00",
    "summary": "Researchers in Korea and Japan have proposed sideways-stacked DRAM designs that could push future AI memory beyond conventional HBM limits by improving cooling, bandwidth, and capacity while reducing "
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/mice/logitechs-mx-master-4-hits-usd102-at-lenovo-up-your-productivity-game-with-haptic-feedback-and-effortless-scrolling",
    "domain": "AI 算力 / 半导体",
    "title": "Logitech's MX Master 4 hits $102 at Lenovo — up your productivity game with haptic feedback and effortless scrolling",
    "url": "https://www.tomshardware.com/peripherals/mice/logitechs-mx-master-4-hits-usd102-at-lenovo-up-your-productivity-game-with-haptic-feedback-and-effortless-scrolling",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T11:34:15+00:00",
    "summary": "Pick up the fantastic Logitech MX Master 4 productivity mouse from Lenovo and make a saving when you stack these two Lenovo e-coupon codes."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/chat-control-1-0-sneaks-through-the-eu-parliament-letting-companies-scan-user-data-without-warrants-legal-tactic-used-to-force-a-majority-required-re-vote-on-eve-of-parliament-break",
    "domain": "AI 算力 / 半导体",
    "title": "Chat Control 1.0 sneaks through the EU Parliament, letting companies scan user data without warrants — legal tactic used to force a majority-required re-vote on eve of Parliament break",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/chat-control-1-0-sneaks-through-the-eu-parliament-letting-companies-scan-user-data-without-warrants-legal-tactic-used-to-force-a-majority-required-re-vote-on-eve-of-parliament-break",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T11:00:00+00:00",
    "summary": "Chat Control 1.0 sneaks through the EU Parliament, letting companies scan user data without warrants — legal skullduggery used to force a majority-required re-vote on eve of Parliament break"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/micron-takes-a-500-million-position-in-americas-only-300mm-wafer-plant",
    "domain": "AI 算力 / 半导体",
    "title": "Micron lifts U.S. spending to $250 billion — company takes $500 million position in America's only 300 mm wafer plant",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/micron-takes-a-500-million-position-in-americas-only-300mm-wafer-plant",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T10:40:00+00:00",
    "summary": "Micron has said it will invest up to $3 billion in the US semiconductor supply chain, with $500 million of that going to GlobalWafers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/samsung-readies-gaia-ai-accelerator-for-client-devices-hp-and-lenovo-are-reportedly-validating-the-npu",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung readies Gaia AI accelerator for PCs — HP and Lenovo are reportedly validating the NPU",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/samsung-readies-gaia-ai-accelerator-for-client-devices-hp-and-lenovo-are-reportedly-validating-the-npu",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T10:20:00+00:00",
    "summary": "Samsung reportedly preps Gaia AI accelerator for client devices that is already being tested by HP and Lenovo."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/minecraft-shown-running-on-game-boy-color-and-game-boy-in-3d-with-textures-developer-coaxed-3d-look-out-of-old-hardware",
    "domain": "AI 算力 / 半导体",
    "title": "Minecraft shown running on Game Boy Color and Game Boy in 3D with textures — developer coaxed 3D look out of barely-there hardware",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/minecraft-shown-running-on-game-boy-color-and-game-boy-in-3d-with-textures-developer-coaxed-3d-look-out-of-old-hardware",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T10:00:00+00:00",
    "summary": "Because getting it to run on the Game Boy Advance clearly wasn't hard enough."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/teamgroup-g70-pro-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "TeamGroup G70 Pro 2TB SSD Review: Low latency meets affordable DRAM",
    "url": "https://www.tomshardware.com/pc-components/ssds/teamgroup-g70-pro-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T17:17:56+00:00",
    "summary": "The TeamGroup G70 Pro is a high-end drive without a high-end price. Good performance, but poor power efficiency keeps it in check."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/external-ssds/redditor-buys-suspicious-drives-on-ebay-just-to-report-the-scamming-sellers-if-they-get-a-fake-ssd-or-hdd-latest-16tb-find-has-weights-and-microsd-card-hot-glued-inside-the-enclosure-to-make-it-feel-legit",
    "domain": "AI 算力 / 半导体",
    "title": "Redditor buys suspicious drives on eBay just to report the scamming sellers if they get a fake SSD or HDD — latest '16TB' find has weights and microSD card hot-glued inside the enclosure to make it fe",
    "url": "https://www.tomshardware.com/pc-components/external-ssds/redditor-buys-suspicious-drives-on-ebay-just-to-report-the-scamming-sellers-if-they-get-a-fake-ssd-or-hdd-latest-16tb-find-has-weights-and-microsd-card-hot-glued-inside-the-enclosure-to-make-it-feel-legit",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T16:03:35+00:00",
    "summary": "u/Hartkralle says that eBay refunds them when they report these fake drives, so getting scammers banned from the platform is worth their effort. While fake sellers would likely just create a new accou"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/ingenious-father-fixes-dead-rtx-3070-with-a-jerry-rigged-capacitor-from-an-old-radio-saves-worried-son-usd120-in-repair-costs-gpu-works-better-than-before-now",
    "domain": "AI 算力 / 半导体",
    "title": "Ingenious father fixes dead RTX 3070 with a jerry-rigged capacitor from an old radio — Saves worried son $120 in repair costs, GPU 'works better than before' now",
    "url": "https://www.tomshardware.com/pc-components/gpus/ingenious-father-fixes-dead-rtx-3070-with-a-jerry-rigged-capacitor-from-an-old-radio-saves-worried-son-usd120-in-repair-costs-gpu-works-better-than-before-now",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T15:53:52+00:00",
    "summary": "A Russian family has just saved the house $120 in GPU repairs after the father fixed it with a salvaged capacitor from an old radio."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/while-the-u-s-flip-flops-on-chip-sanctions-china-is-building-its-own-chip-supply-market-export-controls-are-creating-conditions-for-a-sino-russian-chip-trade-alliance",
    "domain": "AI 算力 / 半导体",
    "title": "While the U.S. flip-flops on chip sanctions, China is building its own chip supply market — export controls are creating conditions for a Sino-Russian chip trade alliance",
    "url": "https://www.tomshardware.com/tech-industry/while-the-u-s-flip-flops-on-chip-sanctions-china-is-building-its-own-chip-supply-market-export-controls-are-creating-conditions-for-a-sino-russian-chip-trade-alliance",
    "source": "Chris Stokel-Walker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T15:24:39+00:00",
    "summary": "As the U.S. makes up its mind on export controls for Chinese chips, China has been developing its own supply chain, and associated trade network."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-revives-aging-zen-2-processor-for-budget-pcs-ryzen-7-4700le-resurfaces-in-a-new-usd800-rtx-3050-prebuilt",
    "domain": "AI 算力 / 半导体",
    "title": "AMD revives aging Zen 2 processor for budget PCs — Ryzen 7 4700LE resurfaces in a new $800 RTX 3050 prebuilt",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-revives-aging-zen-2-processor-for-budget-pcs-ryzen-7-4700le-resurfaces-in-a-new-usd800-rtx-3050-prebuilt",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T14:30:22+00:00",
    "summary": "AMD's quiet revival of older Ryzen processors continues, with the Ryzen 7 4700LE now appearing in a prebuilt gaming desktop priced at $799.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-preps-28-core-nova-lake-s-cpus-for-dunlow-workstation-platform-entry-level-xeon-chip-features-lga1954-socket",
    "domain": "AI 算力 / 半导体",
    "title": "Intel preps 28-core Nova Lake-S CPUs for Dunlow workstation platform — Entry-level Xeon chip features LGA1954 socket",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-preps-28-core-nova-lake-s-cpus-for-dunlow-workstation-platform-entry-level-xeon-chip-features-lga1954-socket",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T14:24:21+00:00",
    "summary": "Intel readies Xeon 'Dunlow' platform with 28 cores in LGA1954 packaging for entry-level servers and workstations."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-shows-off-geforce-trading-cards-series-1-collectible-cards-show-off-games-gpus-and-tech-demos-and-will-be-available-for-free-at-upcoming-events",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia shows off GeForce Trading Cards Series 1 — collectible cards show off games, GPUs, and tech demos, and will be available for free at upcoming events",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-shows-off-geforce-trading-cards-series-1-collectible-cards-show-off-games-gpus-and-tech-demos-and-will-be-available-for-free-at-upcoming-events",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T14:12:10+00:00",
    "summary": "Nvidia is creating a set of collectible trading cards that will be given away for free during live events and giveaways this summer."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/professor-suspected-ai-powered-cheating-on-take-home-midterms-makes-finals-in-person-only-two-students-scored-within-10-percent-of-their-midterm-score",
    "domain": "AI 算力 / 半导体",
    "title": "Professor suspected AI-powered cheating on take-home midterms, makes finals in-person — only two students scored within 10% of their midterm score",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/professor-suspected-ai-powered-cheating-on-take-home-midterms-makes-finals-in-person-only-two-students-scored-within-10-percent-of-their-midterm-score",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T14:10:43+00:00",
    "summary": "A Brown University professor suspected that almost his entire class cheated on take-home mid-term exams using AI tools after they scored unusually high. In-person final exams showed that only two stud"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/segas-usd5m-investment-saved-nvidia-in-1996-now-jensen-huang-is-heading-to-tokyo-to-mark-30-years-of-partnership-akihabara-event-will-include-a-geforce-rtx-5090-fe-lottery-an-rtx-spark-presentation-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Sega’s $5M investment saved Nvidia in 1996, now Jensen Huang is heading to Tokyo to mark 30 years of partnership — Akihabara event will include a GeForce RTX 5090 FE lottery, an RTX Spark presentation",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/segas-usd5m-investment-saved-nvidia-in-1996-now-jensen-huang-is-heading-to-tokyo-to-mark-30-years-of-partnership-akihabara-event-will-include-a-geforce-rtx-5090-fe-lottery-an-rtx-spark-presentation-and-more",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T13:32:50+00:00",
    "summary": "Nvidia and Sega have scheduled an event next week to celebrate their history and longstanding friendship."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/alienware-aw3426dw-34-inch-qd-oled-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Alienware AW3426DW gaming monitor review: Premium gaming and OLED goodness in a value-priced package",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/alienware-aw3426dw-34-inch-qd-oled-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T13:00:00+00:00",
    "summary": "Alienware delivers value from a 34-inch ultra-wide OLED with the AW3426DW. This WQHD curved screen sports Quantum Dot wide gamut color, HDR500, Dolby Vision, 280 Hz, and Adaptive-Sync."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/save-32-percent-on-this-samsung-1440p-gaming-monitor-with-a-fast-240hz-refresh-rate-now-usd169-score-this-27-inch-ips-display-upgrade-with-a-fast-200hz-refresh-rate-for-your-gaming-pc-with-an-usd80-discount",
    "domain": "AI 算力 / 半导体",
    "title": "Save 32% on this Samsung 1440p gaming monitor with a fast 240Hz refresh rate, now $169 — score this 27-inch IPS display upgrade with a fast 200Hz refresh rate for your gaming PC with an $80 discount",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/save-32-percent-on-this-samsung-1440p-gaming-monitor-with-a-fast-240hz-refresh-rate-now-usd169-score-this-27-inch-ips-display-upgrade-with-a-fast-200hz-refresh-rate-for-your-gaming-pc-with-an-usd80-discount",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T12:54:10+00:00",
    "summary": "This 27-inch Samsung Odyssey G53F gaming monitor is on sale for $169.99 right now, offering a 1440p resolution and fast 200Hz refresh rate at a great price."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-upcoming-zen-6-medusa-point-10-core-apu-pops-up-on-geekbench-chip-is-faster-than-ryzen-ai-9-hx-370-and-even-ryzen-ai-max-395",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's upcoming Zen 6 Medusa Point 10-core APU pops up on Geekbench — chip is faster than Ryzen AI 9 HX 370 & even Ryzen AI Max+ 395",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-upcoming-zen-6-medusa-point-10-core-apu-pops-up-on-geekbench-chip-is-faster-than-ryzen-ai-9-hx-370-and-even-ryzen-ai-max-395",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T12:47:57+00:00",
    "summary": "A new 10-core engineering sample from AMD has surfaced on Geekbench, being identified as part of the Medusa Point family. It's likely the Ryzen AI 9 565 and its scores easily beat the Ryzen AI 9 HX 37"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/elon-musk-receives-ftc-greenlight-to-buy-mesh-optical-as-interconnects-emerge-as-ais-tightest-bottleneck-the-move-will-expand-musks-growing-stack-of-critical-ai-infrastructure",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk receives FTC greenlight to buy Mesh Optical as interconnects emerge as AI's tightest bottleneck — the move will expand Musk's growing stack of critical AI infrastructure",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/elon-musk-receives-ftc-greenlight-to-buy-mesh-optical-as-interconnects-emerge-as-ais-tightest-bottleneck-the-move-will-expand-musks-growing-stack-of-critical-ai-infrastructure",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T12:42:23+00:00",
    "summary": "FTC clearance to acquire Mesh Optical hands Musk the missing layer between Terafab's chips and Gigasat's satellites, amid tightening interconnect AI bottleneck"
  },
  {
    "id": "hn:48554206",
    "domain": "AI 算力 / 半导体",
    "title": "Semiconductor Lifeline Keeps Fighter Jets in the Air",
    "url": "https://spectrum.ieee.org/phoenix-semiconductors-legacychips-oems",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-06-16T12:31:02+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/white-house-executive-order-brings-new-urgency-to-post-quantum-cryptography/",
    "domain": "AI 算力 / 半导体",
    "title": "White House Executive Order Brings New Urgency to Post-Quantum Cryptography",
    "url": "https://www.eetimes.com/white-house-executive-order-brings-new-urgency-to-post-quantum-cryptography/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T17:00:00+00:00",
    "summary": "Quantum hackers won’t wait: White House orders PQC by 2030, forcing contractors and tech firms to move now. The post White House Executive Order Brings New Urgency to Post-Quantum Cryptography appeare"
  },
  {
    "id": "rss:https://www.eetimes.com/rise-of-the-ai-data-center-why-infrastructure-strategy-is-now-a-board-level-issue/",
    "domain": "AI 算力 / 半导体",
    "title": "Rise of the AI Data Center – Why Infrastructure Strategy Is Now a Board-Level Issue",
    "url": "https://www.eetimes.com/rise-of-the-ai-data-center-why-infrastructure-strategy-is-now-a-board-level-issue/",
    "source": "Delta Electronics Americas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T14:00:00+00:00",
    "summary": "This white paper describes the critical engineering and strategic pain points behind today&#8217;s AI data center infrastructure gap and offers practical frameworks for resolving them. Whether you&#82"
  },
  {
    "id": "rss:https://www.eetimes.com/sambanova-raises-1-billion-signs-jpmorganchase-as-a-customer/",
    "domain": "AI 算力 / 半导体",
    "title": "SambaNova Raises $1B, Signs JPMorganChase as a Customer",
    "url": "https://www.eetimes.com/sambanova-raises-1-billion-signs-jpmorganchase-as-a-customer/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T07:45:00+00:00",
    "summary": "The enterprise market is beginning to kick in, SambaNova CEO tells EE Times. The post SambaNova Raises $1B, Signs JPMorganChase as a Customer appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/mems-heralds-an-overdue-step-change-in-switching-technology/",
    "domain": "AI 算力 / 半导体",
    "title": "MEMS Heralds an Overdue Step Change in Switching Technology",
    "url": "https://www.eetimes.com/mems-heralds-an-overdue-step-change-in-switching-technology/",
    "source": "Russ Garcia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T07:40:00+00:00",
    "summary": "Ditch creaky relays: MEMS switches slash heat, power draw and bulk for AI data centers and automation. The post MEMS Heralds an Overdue Step Change in Switching Technology appeared first on EE Times."
  },
  {
    "id": "hn:48759308",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia offers startup customers chance to swap compute power for revenue share",
    "url": "https://www.cnbc.com/2026/07/02/nvidia-plans-to-offer-start-up-customers-access-to-revenue-sharing-deals.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-07-02T10:41:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48734960",
    "domain": "AI 算力 / 半导体",
    "title": "Etched has officially come out of stealth",
    "url": "https://www.bloomberg.com/news/articles/2026-06-30/ai-chip-startup-etched-says-jane-street-tsmc-linked-vc-invested",
    "source": "seventeen29",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-30T16:21:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48601996",
    "domain": "AI 算力 / 半导体",
    "title": "ASML denies US Government report that EUV chipmaking tool was shipped to China",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-denies-us-government-report-that-its-euv-chipmaking-tool-was-shipped-to-china-says-rumors-are-inaccurate-and-damaging-to-our-reputation",
    "source": "srameshc",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-19T19:03:30+00:00",
    "summary": ""
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
    "id": "hn:48735444",
    "domain": "大厂 AI 动态",
    "title": "Nano Banana 2 Lite",
    "url": "https://deepmind.google/models/gemini-image/flash-lite/",
    "source": "minimaxir",
    "platform": "hackernews",
    "points": 435,
    "published_at": "2026-06-30T16:48:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48756602",
    "domain": "大厂 AI 动态",
    "title": "Kimi K2.7 Code is generally available in GitHub Copilot",
    "url": "https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/",
    "source": "unliftedq",
    "platform": "hackernews",
    "points": 417,
    "published_at": "2026-07-02T04:32:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48662999",
    "domain": "大厂 AI 动态",
    "title": "Computer use in Gemini 3.5 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/",
    "source": "swolpers",
    "platform": "hackernews",
    "points": 242,
    "published_at": "2026-06-24T17:21:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:48864507",
    "domain": "大厂 AI 动态",
    "title": "Please don't discontinue Gemini 2.5 Flash",
    "url": "https://discuss.ai.google.dev/t/please-dont-discontinue-gemini-2-5-flash/174246",
    "source": "NickDob",
    "platform": "hackernews",
    "points": 119,
    "published_at": "2026-07-10T20:00:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:48707103",
    "domain": "大厂 AI 动态",
    "title": "Google limits Meta's use of its Gemini AI models",
    "url": "https://www.cnbc.com/2026/06/28/google-limits-metas-use-of-its-gemini-ai-models-ft-reports.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 162,
    "published_at": "2026-06-28T13:30:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:48844268",
    "domain": "大厂 AI 动态",
    "title": "LLama.cpp Got Screwd",
    "url": "https://github.com/ggml-org/llama.cpp/discussions/25482",
    "source": "trilogic",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-09T11:40:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:48774429",
    "domain": "大厂 AI 动态",
    "title": "Gemini Code Assist will be shut down on July 17",
    "url": "https://docs.cloud.google.com/gemini/docs/code-review/review-repo-code",
    "source": "ushakov",
    "platform": "hackernews",
    "points": 64,
    "published_at": "2026-07-03T12:52:48+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/964425/flock-safety-cease-and-desist-letter",
    "domain": "大厂 AI 动态",
    "title": "No, Flock isn&#8217;t threatening people for debating surveillance",
    "url": "https://www.theverge.com/tech/964425/flock-safety-cease-and-desist-letter",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T00:10:38+00:00",
    "summary": "On Thursday, the Instagram account for a lecture series in Newport Beach, CA posted a photo of what appeared to be a cease and desist letter from the surveillance technology company Flock Safety. Floc"
  },
  {
    "id": "rss:https://www.theverge.com/tech/964416/meta-instagram-ai-muse-image-deepfakes",
    "domain": "大厂 AI 动态",
    "title": "Meta turns off the Instagram feature that let users make AI deepfakes of public accounts",
    "url": "https://www.theverge.com/tech/964416/meta-instagram-ai-muse-image-deepfakes",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T23:49:50+00:00",
    "summary": "Following significant backlash, Meta is turning off the feature it announced this week that let users generate AI images based on content from public Instagram accounts just by tagging them. The featu"
  },
  {
    "id": "rss:https://www.theverge.com/policy/964342/fcc-crack-down-dji-front-companies-xtra-skyrover-sgs-lab",
    "domain": "大厂 AI 动态",
    "title": "The FCC is cracking down on DJI tech that dodged the foreign drone ban",
    "url": "https://www.theverge.com/policy/964342/fcc-crack-down-dji-front-companies-xtra-skyrover-sgs-lab",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T22:35:18+00:00",
    "summary": "Last year, we told you about Xtra, the company that lets DJI sneak its popular cameras into the US, and Skyrover, a brand seemingly selling DJI drones in disguise. They're just two of the many firms D"
  },
  {
    "id": "rss:https://www.theverge.com/tech/964350/apple-openai-lawsuit-trade-secrets",
    "domain": "大厂 AI 动态",
    "title": "Apple sues OpenAI for allegedly stealing hardware secrets",
    "url": "https://www.theverge.com/tech/964350/apple-openai-lawsuit-trade-secrets",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T21:36:51+00:00",
    "summary": "Apple has sued OpenAI, alleging that engineers stole Apple secrets to advance the AI startup's hardware plans. In its complaint, Apple says it uncovered \"a pattern of theft of Apple's trade secrets by"
  },
  {
    "id": "rss:https://www.theverge.com/games/964022/pokemon-go-10th-anniversary-mewtwo-nyc-go-fest-2026",
    "domain": "大厂 AI 动态",
    "title": "A decade later, Pokémon Go finally made good on its original promise",
    "url": "https://www.theverge.com/games/964022/pokemon-go-10th-anniversary-mewtwo-nyc-go-fest-2026",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T19:51:10+00:00",
    "summary": "When Niantic dropped the first Pok&#233;mon Go trailer in 2015, it was hard to grasp how a bunch of players could work together to catch a pok&#233;mon like Mewtwo. But this week at the game's 10th an"
  },
  {
    "id": "rss:https://www.theverge.com/policy/964294/ice-shooting-houston-lorenzo-salgado-araujo",
    "domain": "大厂 AI 动态",
    "title": "ICE is threatening to deport witnesses of its latest shooting",
    "url": "https://www.theverge.com/policy/964294/ice-shooting-houston-lorenzo-salgado-araujo",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T19:20:00+00:00",
    "summary": "Advocates are demanding that the Department of Homeland Security release bodycam footage of the fatal shooting of Lorenzo Salgado Araujo, a Mexican immigrant who was killed by ICE officers in Houston "
  },
  {
    "id": "rss:https://www.theverge.com/tech/964121/sk-hynix-nvidia-ram-stock-market-debut",
    "domain": "大厂 AI 动态",
    "title": "Nvidia&#8217;s biggest RAM supplier just had a trillion-dollar debut on Wall Street",
    "url": "https://www.theverge.com/tech/964121/sk-hynix-nvidia-ram-stock-market-debut",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T17:31:35+00:00",
    "summary": "As the AI boom boosts demand for RAM, SK Hynix - one of the world's biggest suppliers of memory chips - launched on Wall Street Friday. The South Korean chipmaker opened at $170 per share and raised $"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/964021/spotify-release-radar-algorithm-controls",
    "domain": "大厂 AI 动态",
    "title": "Spotify will let you fine-tune your weekly Release Radar playlist",
    "url": "https://www.theverge.com/entertainment/964021/spotify-release-radar-algorithm-controls",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T17:02:13+00:00",
    "summary": "Spotify is giving listeners control to fine-tune what gets surfaced for them in Release Radar - one of its most popular weekly playlists. The new options allow you to narrow the playlist to a specific"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/964082/netflix-youtube-smart-glasses-vergecast",
    "domain": "大厂 AI 动态",
    "title": "Netflix is turning into YouTube",
    "url": "https://www.theverge.com/podcast/964082/netflix-youtube-smart-glasses-vergecast",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:29:50+00:00",
    "summary": "Netflix has shows and movies. And video games. And live sports. And podcasts. And also, apparently, YouTube videos? For a company that used to seem like the next big thing in TV, it all feels a little"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/964056/disney-plus-free-tier-report",
    "domain": "大厂 AI 动态",
    "title": "Disney Plus is reportedly looking into a free streaming tier",
    "url": "https://www.theverge.com/streaming/964056/disney-plus-free-tier-report",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T15:33:58+00:00",
    "summary": "Disney Plus is considering making some of its content free to watch, according to a report from Business Insider. A source tells the outlet that Adam Smith, Disney's chief product and technology offic"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/us-cyber-agency-cisa-had-to-build-its-incident-playbook-during-the-incident-agency-reveals/",
    "domain": "大厂 AI 动态",
    "title": "US cybersecurity agency CISA had to build its incident playbook during the incident, agency reveals",
    "url": "https://techcrunch.com/2026/07/10/us-cyber-agency-cisa-had-to-build-its-incident-playbook-during-the-incident-agency-reveals/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T01:01:28+00:00",
    "summary": "Independent cybersecurity journalist Brian Krebs reported in May that a security researcher with cyber firm GitGuardian alerted him to reams of exposed passwords stored in a publicly accessible GitHub"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/phia-accused-of-cookie-stuffing-taking-affiliate-credit-on-purchases-it-didnt-earn/",
    "domain": "大厂 AI 动态",
    "title": "Phia accused of ‘cookie stuffing,’ taking affiliate credit on purchases it didn’t earn",
    "url": "https://techcrunch.com/2026/07/10/phia-accused-of-cookie-stuffing-taking-affiliate-credit-on-purchases-it-didnt-earn/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T00:29:25+00:00",
    "summary": "Phia, the shopping startup founded by Bill Gates’ daughter, Phoebe, and her friend Sophia Kianni is under fire for a practice known as “cookie stuffing,” which helped the product receive commissions a"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/meta-removes-controversial-ai-feature-on-instagram-after-backlash/",
    "domain": "大厂 AI 动态",
    "title": "Meta removes controversial AI feature on Instagram after backlash",
    "url": "https://techcrunch.com/2026/07/10/meta-removes-controversial-ai-feature-on-instagram-after-backlash/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T23:55:07+00:00",
    "summary": "\"Our intent was to provide a useful creative tool and to give people control over whether their public content could be referenced in this way,\" the company said in a blog post. \"We've heard the feedb"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/blueskys-interim-ceo-toni-schneider-drops-the-interim/",
    "domain": "大厂 AI 动态",
    "title": "Bluesky’s interim CEO, Toni Schneider, drops the ‘interim’",
    "url": "https://techcrunch.com/2026/07/10/blueskys-interim-ceo-toni-schneider-drops-the-interim/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T21:51:55+00:00",
    "summary": "Schneider, who formerly served as the CEO of Automattic and is a partner at True Ventures, says he is \"all in\" on the unconventional social media platform."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/apple-sues-openai-over-alleged-trade-secret-theft/",
    "domain": "大厂 AI 动态",
    "title": "Apple sues OpenAI over alleged trade secret theft",
    "url": "https://techcrunch.com/2026/07/10/apple-sues-openai-over-alleged-trade-secret-theft/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T21:00:29+00:00",
    "summary": "Apple alleges the misconduct was directed by OpenAI's senior leadership, including a longtime former employee."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/filing-college-app-fizz-accuses-vc-of-sharing-confidential-startup-information-with-rival-sidechat/",
    "domain": "大厂 AI 动态",
    "title": "Filing: College app Fizz accuses VC of sharing confidential startup information with rival Sidechat",
    "url": "https://techcrunch.com/2026/07/10/filing-college-app-fizz-accuses-vc-of-sharing-confidential-startup-information-with-rival-sidechat/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T17:42:36+00:00",
    "summary": "Fizz has expanded its lawsuit against rival Sidechat, alleging that a Maveron VC shared its confidential information obtained during a fundraising meeting with the competing startup."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/sk-hynix-raises-26-5b-in-the-biggest-foreign-ipo-in-us-history-is-urged-to-build-new-us-fabs/",
    "domain": "大厂 AI 动态",
    "title": "SK Hynix raises $26.5B in the biggest foreign IPO in US history, is urged to build new US fabs",
    "url": "https://techcrunch.com/2026/07/10/sk-hynix-raises-26-5b-in-the-biggest-foreign-ipo-in-us-history-is-urged-to-build-new-us-fabs/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T17:17:12+00:00",
    "summary": "The AI chip boom just produced its biggest Wall Street moment yet. Now SK Hynix and Samsung are being asked to build U.S. factories."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/a-new-app-hypertexting-turns-the-open-web-into-a-scrollable-social-media-like-feed/",
    "domain": "大厂 AI 动态",
    "title": "A new app, HyperTexting, turns the open web into a scrollable social media-like feed",
    "url": "https://techcrunch.com/2026/07/10/a-new-app-hypertexting-turns-the-open-web-into-a-scrollable-social-media-like-feed/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T17:11:51+00:00",
    "summary": "HyperTexting's new app aims to make the open web feel more like social media by turning websites, blogs, newsletters, and podcasts into a scrollable feed, while also making it easier to post to your o"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/china-is-catching-up-to-elon-musks-reusable-rockets/",
    "domain": "大厂 AI 动态",
    "title": "China is catching up to Elon Musk’s reusable rockets",
    "url": "https://techcrunch.com/2026/07/10/china-is-catching-up-to-elon-musks-reusable-rockets/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:51:07+00:00",
    "summary": "China's state-owned space company recovered its first orbital rocket booster after launch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/disney-is-considering-a-free-streaming-tier-report-says/",
    "domain": "大厂 AI 动态",
    "title": "Disney+ is considering a free streaming tier, report says",
    "url": "https://techcrunch.com/2026/07/10/disney-is-considering-a-free-streaming-tier-report-says/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:29:05+00:00",
    "summary": "The launch of free content would allow Disney+ to better compete with free services like YouTube and Tubi, which are capturing a growing share of consumers’ viewing time."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/dumb-co-dared-me-to-trade-my-iphone-for-a-hacked-flip-phone/",
    "domain": "大厂 AI 动态",
    "title": "Dumb Co dared me to trade my iPhone for a hacked flip phone",
    "url": "https://techcrunch.com/2026/07/10/dumb-co-dared-me-to-trade-my-iphone-for-a-hacked-flip-phone/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:06:49+00:00",
    "summary": "Dumb Co sells flip phones that sync to your smartphone, bridging the infinite connectivity of the iPhone and the unrealistic limitations of an early 2000s relic."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/oratomic-raises-300m-to-build-a-viable-quantum-computer-that-needs-only-20k-qubits/",
    "domain": "大厂 AI 动态",
    "title": "Oratomic raises $300M to build a viable quantum computer that needs only 20K qubits",
    "url": "https://techcrunch.com/2026/07/10/oratomic-raises-300m-to-build-a-viable-quantum-computer-that-needs-only-20k-qubits/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T15:00:09+00:00",
    "summary": "The massive round was co-led by ARCH Venture Partners, Spark Capital, and Khosla Ventures."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/netflix-could-be-planning-always-on-live-tv-channels/",
    "domain": "大厂 AI 动态",
    "title": "Netflix could be planning ‘always-on’ live TV channels",
    "url": "https://techcrunch.com/2026/07/10/netflix-could-be-planning-always-on-live-tv-channels/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T14:53:08+00:00",
    "summary": "Amid signs of slowing engagement, Netflix is reportedly considering launching \"always-on\" live channels, giving subscribers something to tune into 24/7."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/eu-threatens-meta-with-fines-over-addictive-features-on-facebook-and-instagram/",
    "domain": "大厂 AI 动态",
    "title": "EU threatens Meta with fines over addictive features on Facebook and Instagram",
    "url": "https://techcrunch.com/2026/07/10/eu-threatens-meta-with-fines-over-addictive-features-on-facebook-and-instagram/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T14:19:40+00:00",
    "summary": "The tech giant is in breach of the Digital Services Act by focusing on features like infinite scroll, autoplay, push notifications, and the highly personalized recommendation algorithms, the European "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/florida-ransomware-negotiator-convicted-for-helping-ransomware-gang-extort-us-companies/",
    "domain": "大厂 AI 动态",
    "title": "Florida ransomware negotiator convicted for helping ransomware gang extort US companies",
    "url": "https://techcrunch.com/2026/07/10/florida-ransomware-negotiator-convicted-for-helping-ransomware-gang-extort-us-companies/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T14:11:03+00:00",
    "summary": "A third ransomware negotiator has been jailed for helping a notorious ransomware group extort American victim companies into paying the hackers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/hugging-faces-ceo-on-why-companies-are-done-renting-their-ai/",
    "domain": "大厂 AI 动态",
    "title": "Hugging Face’s CEO on why companies are done renting their AI",
    "url": "https://techcrunch.com/2026/07/10/hugging-faces-ceo-on-why-companies-are-done-renting-their-ai/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T14:00:00+00:00",
    "summary": "Open source AI is booming, according to&#160;Hugging Face&#160;CEO&#160;Clem Delangue. The company has grown into something like a GitHub for AI in recent years, where AI builders can share and downlo"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/after-apple-indias-smartphone-manufacturing-boom-enters-new-phase-with-vivo-jv/",
    "domain": "大厂 AI 动态",
    "title": "After Apple, India’s smartphone manufacturing boom enters new phase with Vivo JV",
    "url": "https://techcrunch.com/2026/07/09/after-apple-indias-smartphone-manufacturing-boom-enters-new-phase-with-vivo-jv/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T04:36:20+00:00",
    "summary": "Vivo's joint venture could become a template for Chinese smartphone makers in India."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/openai-says-gpt-5-6-is-the-preferred-model-for-microsoft-copilot-amid-breakup-chatter/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI says GPT 5.6 is the ‘preferred model’ for Microsoft Copilot 365 amid breakup chatter",
    "url": "https://techcrunch.com/2026/07/09/openai-says-gpt-5-6-is-the-preferred-model-for-microsoft-copilot-amid-breakup-chatter/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T00:16:54+00:00",
    "summary": "OpenAI's new family of models will continue to power Microsoft's suite of workplace and productivity apps."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/dont-want-to-invest-in-elon-musk-two-new-etfs-explicitly-exclude-him/",
    "domain": "大厂 AI 动态",
    "title": "Don’t want to invest in Elon Musk? Two new ETFs explicitly exclude him",
    "url": "https://techcrunch.com/2026/07/09/dont-want-to-invest-in-elon-musk-two-new-etfs-explicitly-exclude-him/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T00:13:00+00:00",
    "summary": "The new exchange-traded funds exclude companies that are founded, controlled, or led by Elon Musk. That means no SpaceX or Tesla."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/09/fidji-simo-steps-down-from-openais-no-2-role/",
    "domain": "大厂 AI 动态",
    "title": "Fidji Simo steps down from OpenAI’s No. 2 role",
    "url": "https://techcrunch.com/2026/07/09/fidji-simo-steps-down-from-openais-no-2-role/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T23:38:00+00:00",
    "summary": "OpenAI's No. 2 executive, Fidji Simo, is stepping down from her full-time role after her medical leave proved longer than expected — a leadership vacuum that comes at a tricky time as the company eyes"
  },
  {
    "id": "rss:https://stratechery.com/2026/xbox-on-the-rocks/",
    "domain": "大厂 AI 动态",
    "title": "2026.28: XBOX On the Rocks",
    "url": "https://stratechery.com/2026/xbox-on-the-rocks/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of July 6, 2026, including a word from Mark Zuckerberg*, pulling the plug on XBOX, and toilet talk."
  },
  {
    "id": "rss:https://stratechery.com/2026/muse-image-grok-4-5-alex-karp-on-cnbc/",
    "domain": "大厂 AI 动态",
    "title": "Muse Image, Grok 4.5, Alex Karp on CNBC",
    "url": "https://stratechery.com/2026/muse-image-grok-4-5-alex-karp-on-cnbc/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T10:00:00+00:00",
    "summary": "The battle for verifiable data is increasingly defining the AI race, from Meta to Grok to the frontier labs."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/quantum-error-correction-can-constantly-recalibrate-a-processor/",
    "domain": "大厂 AI 动态",
    "title": "Quantum error correction can constantly recalibrate a processor",
    "url": "https://arstechnica.com/science/2026/07/quantum-error-correction-can-constantly-recalibrate-a-processor/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T23:02:30+00:00",
    "summary": "Reinforcement learning uses error information to adjust control algorithms."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/on-americas-250th-more-cities-used-drone-surveillance-to-spot-illegal-fireworks/",
    "domain": "大厂 AI 动态",
    "title": "Increased drone surveillance of illegal July 4th fireworks led to $100K fine",
    "url": "https://arstechnica.com/gadgets/2026/07/on-americas-250th-more-cities-used-drone-surveillance-to-spot-illegal-fireworks/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T22:37:22+00:00",
    "summary": "More police and firefighters use drones to catch and deter illegal fireworks."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/china-recovered-its-first-reusable-rocket-and-showed-a-new-way-to-do-it/",
    "domain": "大厂 AI 动态",
    "title": "China recovered its first reusable rocket and showed a new way to do it",
    "url": "https://arstechnica.com/space/2026/07/china-recovered-its-first-reusable-rocket-and-showed-a-new-way-to-do-it/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T21:41:43+00:00",
    "summary": "\"Clearly, they admire the work that's being done by SpaceX and are trying to replicate it.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/expedition-captures-first-images-of-shackletons-last-ship/",
    "domain": "大厂 AI 动态",
    "title": "Check out the first images of Quest shipwreck",
    "url": "https://arstechnica.com/science/2026/07/expedition-captures-first-images-of-shackletons-last-ship/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T19:59:31+00:00",
    "summary": "The Quest shipwreck is in worse shape than expected, but it has turned into a thriving marine ecosystem."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/ransomware-negotiator-helped-attackers-extort-his-own-clients-gets-6-year-sentence/",
    "domain": "大厂 AI 动态",
    "title": "Ransomware negotiator hired to represent victims was working for the attackers",
    "url": "https://arstechnica.com/tech-policy/2026/07/ransomware-negotiator-helped-attackers-extort-his-own-clients-gets-6-year-sentence/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T19:40:11+00:00",
    "summary": "Six years in prison for man who \"sold out the very victims he was hired to represent.\""
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/anti-vaccine-changes-under-rfk-jr-will-hurt-vulnerable-toddlers-study-confirms/",
    "domain": "大厂 AI 动态",
    "title": "Study shows how toxic RFK Jr.’s change to measles vaccine is for US toddlers",
    "url": "https://arstechnica.com/health/2026/07/anti-vaccine-changes-under-rfk-jr-will-hurt-vulnerable-toddlers-study-confirms/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T19:25:04+00:00",
    "summary": "The children who get a combination shot are some of the most vulnerable."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/07/valves-steam-machine-verified-ratings-offer-more-questions-than-answers/",
    "domain": "大厂 AI 动态",
    "title": "Valve's new Steam Machine verification system is silent on these Steam Deck-busters",
    "url": "https://arstechnica.com/gaming/2026/07/valves-steam-machine-verified-ratings-offer-more-questions-than-answers/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:53:31+00:00",
    "summary": "Dozens of titles too taxing for Steam Deck are still unrated for the new hardware."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/firmware-update-bricks-hue-bridge-pro-devices-philips-gives-free-replacements/",
    "domain": "大厂 AI 动态",
    "title": "Firmware update bricks Hue Bridge Pro devices; Philips gives free replacements",
    "url": "https://arstechnica.com/gadgets/2026/07/firmware-update-bricks-hue-bridge-pro-devices-philips-gives-free-replacements/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:36:09+00:00",
    "summary": "Affected users will have to configure their lights and settings all over again."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/an-orbiting-disco-ball-gave-einsteins-theory-its-most-precise-test-yet/",
    "domain": "大厂 AI 动态",
    "title": "An orbiting disco ball gave Einstein’s theory its most precise test yet",
    "url": "https://arstechnica.com/science/2026/07/an-orbiting-disco-ball-gave-einsteins-theory-its-most-precise-test-yet/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:11:35+00:00",
    "summary": "The Earth may not be that massive, but it still distorts space-time."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/disable-auto-play-and-infinite-scroll-or-risk-massive-fines-eu-tells-meta/",
    "domain": "大厂 AI 动态",
    "title": "Disable autoplay and infinite scroll or risk massive fines, EU tells Meta",
    "url": "https://arstechnica.com/tech-policy/2026/07/disable-auto-play-and-infinite-scroll-or-risk-massive-fines-eu-tells-meta/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T15:46:18+00:00",
    "summary": "Digital Services Act may force Meta to make big changes on its platforms."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/nasa-finally-releases-a-critical-planning-document-for-private-space-stations/",
    "domain": "大厂 AI 动态",
    "title": "NASA sure seems to be asking an awful lot of private space stations",
    "url": "https://arstechnica.com/space/2026/07/nasa-finally-releases-a-critical-planning-document-for-private-space-stations/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T15:15:58+00:00",
    "summary": "\"Industry finally knows what NASA is asking of them.\""
  },
  {
    "id": "hn:48678873",
    "domain": "股票",
    "title": "OpenAI leans toward waiting until next year for IPO",
    "url": "https://www.nytimes.com/2026/06/25/technology/openai-ipo-artificial-intelligence.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 179,
    "published_at": "2026-06-25T20:36:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48853145",
    "domain": "股票",
    "title": "California universities stockpiling AR-15s, grenades and submachine guns",
    "url": "https://www.theguardian.com/us-news/2026/jul/09/california-universities-military-equipment",
    "source": "sizzle",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-09T22:20:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:48846617",
    "domain": "股票",
    "title": "Sony CEO Just Sold over Half His Stock",
    "url": "https://gamerant.com/sony-ceo-sells-stock/",
    "source": "josephcsible",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-09T14:37:45+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3776698",
    "domain": "股票",
    "title": "1个月上涨25%后，美国生物医药板块周五重挫",
    "url": "https://wallstreetcn.com/articles/3776698",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T05:26:59+00:00",
    "summary": "美股生物医药板块因集中获利了结引发急跌，高贝塔代表性ETF（XBI）单日大跌4%。Moderna、ImmunityBio等年内暴涨股在无基本面利空的情况下回撤8%~11%，资金呈现从高风险小盘股向强防御大市值药企跨板块结构性轮动。"
  },
  {
    "id": "wscn:3776573",
    "domain": "股票",
    "title": "去杠杆风暴下半场：美韩半导体风险释放到什么程度？",
    "url": "https://wallstreetcn.com/premium/articles/3776573?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T04:21:16+00:00",
    "summary": "美韩半导体去杠杆或正进入中后期，流动性出清仍未完成，估值修复仍需等待基本面接力。"
  },
  {
    "id": "wscn:3776695",
    "domain": "股票",
    "title": "中美一样的困惑：硅碳能从分化到共赢吗？",
    "url": "https://wallstreetcn.com/articles/3776695",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T03:02:13+00:00",
    "summary": "国信证券认为，美股分化更早、A股分化程度更大，根源是硅基盈利明显强于碳基。AI红利尚未惠及碳基。AI 资本开支成为中美经济亮点，我国 Token 调用量激增 81 倍。展望未来，硅碳终将走向共赢。当AI从大模型步入物理应用时，中国智造有工程师红利与算力成本优势，届时新老经济融合共赢。"
  },
  {
    "id": "wscn:3776697",
    "domain": "股票",
    "title": "“权益高地”诺安基金高管更替：刘翔升任总经理",
    "url": "https://wallstreetcn.com/articles/3776697",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T02:52:01+00:00",
    "summary": "公募基金公司再现“掌门”更替。\n7月10日晚间，诺安基金公告齐斌因个人原因离任总经理职位，原副总经理..."
  },
  {
    "id": "wscn:3776696",
    "domain": "股票",
    "title": "对话即刻2.5 lab技术负责人：做AI应用会优先考虑利润",
    "url": "https://wallstreetcn.com/articles/3776696",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T02:41:16+00:00",
    "summary": "中小AI应用的现实生存样本。"
  },
  {
    "id": "wscn:3776694",
    "domain": "股票",
    "title": "美股处于“极度脆弱”的时候，财报季开启了",
    "url": "https://wallstreetcn.com/articles/3776694",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T01:50:01+00:00",
    "summary": "美股指数表面平静（VIX低迷），但瑞银市场脆弱度指标飙升至0.9的历史高位。在二季度盈利预期大涨24%的“高期望”财报季拉开帷幕之际，市场内部压力正加速积聚：单股波动率已超出指数三倍，债市收益率逼近4.6%，且油价走高（布油逼近80美元）正威胁通胀及欧洲股市。"
  },
  {
    "id": "wscn:3776692",
    "domain": "股票",
    "title": "重回AI一线？Meta单周大涨15%",
    "url": "https://wallstreetcn.com/articles/3776692",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T01:42:40+00:00",
    "summary": "Meta创2024年2月以来单周最强表现。核心驱动来自多重AI利好，最新AI模型性能超越Gemini，且定价仅为竞品四分之一。自研芯片\"Iris\"或9月量产，算力规模于2027年扩至14吉瓦。研究机构SemiAnalysis预测，Meta有望半年内在前沿AI能力上超越谷歌，行业格局或重塑为Meta、OpenAI、Anthropic三足鼎立。"
  },
  {
    "id": "wscn:3776691",
    "domain": "股票",
    "title": "“以打促谈”还是“战略转变”？美国给出“周六开通霍尔木兹海峡”的“最后通牒”",
    "url": "https://wallstreetcn.com/articles/3776691",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T01:04:20+00:00",
    "summary": "特朗普政府高级官员周五罕见承认，通过和平谈判达成核协议的可能性正日益降低，与此同时，美方向伊朗发出限期警告——要求其在周六前作出承诺，声明霍尔木兹海峡已开放并停止对船只开火。"
  },
  {
    "id": "wscn:3776690",
    "domain": "股票",
    "title": "硅谷疯狂举债，市场凶猛抛售",
    "url": "https://wallstreetcn.com/articles/3776690",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T00:56:42+00:00",
    "summary": "AI相关债券今年发行规模达2700亿美元，供给过剩压垮需求。投资者对AI资本支出长期回报存疑，叠加高利率环境下短端美债已具吸引力，机构纷纷转向短期债券。债券市场正以行动表明，对AI建设浪潮的长远承诺，远比股市更为审慎。"
  },
  {
    "id": "wscn:3776623",
    "domain": "股票",
    "title": "科技股续撑纳指三连阳，SK海力士ADR首日大涨13%，布油冲高转跌，黄金走V仍收跌",
    "url": "https://wallstreetcn.com/articles/3776623",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T23:11:15+00:00",
    "summary": "标普收创一个多月新高，和纳指连涨两周。Meta收涨6%，全周涨近15%。英伟达收涨4%。特朗普重燃美伊谈判希望，十年期美债收益率刷新日高，美元指数一度转跌。离岸人民币两周多来首次盘中涨破6.78。比特币盘中创逾两周新高、较日低涨近3%。原油跳涨超1%后重回跌势，黄金跌超1%后收窄多数跌幅。"
  },
  {
    "id": "wscn:3776687",
    "domain": "股票",
    "title": "华尔街见闻早餐FM-Radio | 2026年7月11日",
    "url": "https://wallstreetcn.com/articles/3776687",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T23:05:12+00:00",
    "summary": "五分钟看懂全球市场，尽在财经早餐。"
  },
  {
    "id": "wscn:3776688",
    "domain": "股票",
    "title": "硅谷巨头反目！苹果起诉OpenAI窃取商业机密，要求销毁涉密资料并重设计AI硬件",
    "url": "https://wallstreetcn.com/articles/3776688",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T22:39:37+00:00",
    "summary": "苹果指控OpenAI蓄意策动苹果员工泄露未发布产品的相关信息，服务于其硬件自主研发计划。要求OpenAI销毁所有涉案材料，重新设计产品，确保不含苹果技术。现任OpenAI首席硬件官Tang Tan是本案核心被告之一，其曾任苹果产品设计副总裁。OpenAI回应称，对其他公司的商业秘密没兴趣。"
  },
  {
    "id": "wscn:3776689",
    "domain": "股票",
    "title": "AI加剧美国通胀？高盛：内存、电力和软件涨价年底或推高核心PCE 0.5个百分点",
    "url": "https://wallstreetcn.com/articles/3776689",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T22:16:00+00:00",
    "summary": "高盛最新测算显示，AI驱动的内存价格暴涨、软件提价、电费攀升三重冲击已推高美国核心PCE逾0.2个百分点，预计至年底该贡献将升至0.5个百分点。这一估算尚未完全反映各类溢出效应，实际冲击可能更大。多数美联储官员认为，在某些情景下，AI相关需求强劲可能导致通胀持续高企。"
  },
  {
    "id": "wscn:3776680",
    "domain": "股票",
    "title": "AI狂欢持续！SK海力士创海外赴美最大IPO，美股首秀收涨13%",
    "url": "https://wallstreetcn.com/articles/3776680",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T20:53:59+00:00",
    "summary": "SK海力士ADR开盘涨14%，盘中一度涨近19%。此次IPO发行近1.8亿ADR、融资265亿美元，刷新阿里保持十余年的海外企业赴美IPO融资纪录。据称三家基石投资者合计获配50亿美元ADR。"
  },
  {
    "id": "wscn:3776677",
    "domain": "股票",
    "title": "特朗普称美国已同意继续和伊朗谈判，美媒称新一轮谈判或下周举行、伊媒否认",
    "url": "https://wallstreetcn.com/articles/3776677",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T20:19:28+00:00",
    "summary": "伊朗外交部：从未提出与美谈判诉求，同意调解方访伊。据美媒，卡塔尔谈判代表周五在与美方协调后前往伊朗，与伊朗官员会面，为美伊谈判恢复创造条件；外交官称，美伊都希望回到谅解备忘录框架下；美官员称，特朗普政府的策略是实施打击后暂停军事行动，避免局势进一步升级并留出外交斡旋空间。"
  },
  {
    "id": "wscn:3776685",
    "domain": "股票",
    "title": "SK海力士CEO：2027年将迎来史上最严重存储芯片短缺，供不应求或持续至2030年后",
    "url": "https://wallstreetcn.com/articles/3776685",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T20:18:18+00:00",
    "summary": "SK海力士CEOKwak Noh-Jung在美国存托凭证发行后接受采访时表示，预计2027年将成为存储芯片行业供应短缺最严重的一年。预计存储芯片需求将持续超过公司的生产能力，并一直延续到2030年以后。同时表示，越来越多客户选择签订长期供货合同，由于其普遍认为供应紧张将持续较长时间。"
  },
  {
    "id": "wscn:3776686",
    "domain": "股票",
    "title": "大摩泼冷水：芯片制造商定价权承压、AI资本开支开始放缓、美股半导体“明显超买”",
    "url": "https://wallstreetcn.com/articles/3776686",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T19:53:30+00:00",
    "summary": "摩根士丹利财富管理首席投资官表示，超大规模云服务商加速自研低成本芯片，正蚕食芯片制造商的定价权；企业已经开始讨论AI投资的节奏及回报率，目前正处于AI资本开支增速开始放缓的初期阶段；费城半导体指数市盈率自2022年以来上涨逾三倍，半导体板块已经出现“明显超买”迹象。"
  },
  {
    "id": "wscn:3776683",
    "domain": "股票",
    "title": "财相\"点名\"1.8万亿GPIF引发日元脉冲跳涨，高盛泼冷水：不过是\"过度反应\"",
    "url": "https://wallstreetcn.com/articles/3776683",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T18:54:53+00:00",
    "summary": "日本财务大臣表示，包括全球最大养老基金之一GPIF在内的养老金机构应增加对日本国内金融资产的投资。日元兑美元短线急涨至161.29，日本国债收益率曲线整体下行约10个基点。然而，高盛指出这一债市反弹是\"过度反应\"，维持对超长期日本国债的看空立场，认为此次反弹并非趋势逆转。"
  },
  {
    "id": "wscn:3776682",
    "domain": "股票",
    "title": "SK集团董事长：若股价稳定，考虑增发美国股票、扩大在美投资、推出\"内存即服务\"新模式",
    "url": "https://wallstreetcn.com/articles/3776682",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T18:34:19+00:00",
    "summary": "SK海力士在美股首日开盘涨14%。SK集团董事长崔泰源表示，若股价保持稳定，SK海力士有意发行更多美国存托凭证；SK集团在美投资规模将远超目前已公布的350亿美元。其还提出了\"内存即服务\"的新商业模式构想，允许客户租用内存芯片使用权。SK海力士CEO郭鲁正表示，存储芯片供应短缺可能会持续至2030年之后。"
  },
  {
    "id": "wscn:3776684",
    "domain": "股票",
    "title": "一天940万桶缺口！IEA警告美伊再交火或颠覆明年石油过剩预期",
    "url": "https://wallstreetcn.com/articles/3776684",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T18:13:56+00:00",
    "summary": "IEA报告称，6月全球石油供应因霍尔木兹海峡重新开放而回升410万桶/日，但相比战前水平缺口仍高达940万桶/日；持久和平协议是油市正常化的“必要条件”；当前原油表面供应充裕，成品油却持续偏紧，这一“割裂”推动裂解价差和炼油利润率本月初飙升至四年高位；预计今年全球油需下降100万桶/日，为疫情以来六年内首次年度下滑。"
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
    "id": "hn:48824532",
    "domain": "股票",
    "title": "SpaceX Shares Stumble in Nasdaq-100 Debut",
    "url": "https://www.wsj.com/finance/stocks/spacex-shares-stumble-in-nasdaq-100-debut-9ec10565",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-07T22:00:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48826804",
    "domain": "股票",
    "title": "AI has taken over the stock market. The bond market is next",
    "url": "https://www.economist.com/finance-and-economics/2026/07/07/ai-has-taken-over-the-stock-market-the-bond-market-is-next",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-08T02:32:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:48504013",
    "domain": "股票",
    "title": "SpaceX's president is floating a Tesla merger as the company begins trading",
    "url": "https://qz.com/spacex-tesla-merger-gwynne-shotwell-ipo-061226",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-06-12T13:47:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48612095",
    "domain": "股票",
    "title": "Show HN: My Windows XP portfolio with working Game Boy and iPod",
    "url": "https://mitchivin.com/",
    "source": "mitchivin",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-06-20T19:18:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48787052",
    "domain": "股票",
    "title": "Elon Musk posted twice as often on UK race and immigration as about SpaceX IPO",
    "url": "https://www.theguardian.com/technology/2026/jul/04/elon-musk-uk-race-immigration-spacex-ipo",
    "source": "iamflimflam1",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-07-04T17:18:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48774424",
    "domain": "股票",
    "title": "X has suddenly banned an account documenting Trump's corrupt stock trades",
    "url": "https://twitter.com/HQNewsNow/status/2072699828337864871",
    "source": "doener",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-07-03T12:52:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:48634931",
    "domain": "股票",
    "title": "SpaceX Drops 14% in One Day, Price Now Below IPO Launch",
    "url": "https://finance.yahoo.com/quote/SPCX/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-06-22T19:33:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48781228",
    "domain": "股票",
    "title": "After $18B IPO, Bending Spoons founder says success comes from minimizing luck",
    "url": "https://techcrunch.com/2026/07/01/after-18b-ipo-bending-spoons-founder-says-success-comes-from-minimizing-luck/",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-03T23:31:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48777130",
    "domain": "股票",
    "title": "Tesla stock sinks 7% despite strong deliveries report, worst day in nearly 1y",
    "url": "https://www.cnbc.com/2026/07/02/tesla-tsla-q2-2026-vehicle-delivery-production.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-03T16:52:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:48789829",
    "domain": "股票",
    "title": "Ask HN: When will the stock market crash?",
    "url": "https://news.ycombinator.com/item?id=48789829",
    "source": "roschdal",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-04T22:55:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:48505968",
    "domain": "股票",
    "title": "Elon Musk Becomes First Trillionaire as SpaceX Starts Trading",
    "url": "https://www.nytimes.com/live/2026/06/12/business/spacex-ipo-elon-musk/heres-the-latest",
    "source": "droidjj",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-06-12T16:13:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48748464",
    "domain": "股票",
    "title": "The Stockholm Telephone Tower with Approximately 5,500 Telephone Lines, 1890",
    "url": "https://rarehistoricalphotos.com/the-stockholm-telephone-tower-1890/",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-07-01T15:27:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48598558",
    "domain": "股票",
    "title": "The average SpaceX buyer post-IPO is almost under water after two-day slide",
    "url": "https://www.cnbc.com/2026/06/18/the-average-spacex-buyer-post-ipo-is-almost-under-water-after-two-day-slide.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 40,
    "published_at": "2026-06-19T13:48:28+00:00",
    "summary": ""
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
    "id": "hn:48750160",
    "domain": "股票",
    "title": "Tech giants lose $2T in SpaceX's IPO month",
    "url": "https://english.elpais.com/economy-and-business/2026-07-01/tech-giants-lose-2-trillion-in-spacexs-ipo-month-the-valuations-were-unsustainable.html",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-07-01T17:14:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:48714428",
    "domain": "股票",
    "title": "SpaceX just landed in 401(k)s due to key index rule changes",
    "url": "https://moneywise.com/news/top-stories/spacex-401k-anthropic-openai-ipo-index-fund-rules",
    "source": "voxadam",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-06-29T03:25:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48700725",
    "domain": "股票",
    "title": "Cheap Drones Are Rewriting Warfare",
    "url": "https://www.barrons.com/articles/best-military-drone-stocks-4f90e7c6",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-27T18:56:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:48506701",
    "domain": "股票",
    "title": "SpaceX increases almost 30% after biggest IPO",
    "url": "https://www.cnbc.com/2026/06/12/spacex-ipo-spcx-live-updates.html",
    "source": "somenameforme",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-06-12T17:10:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:48553976",
    "domain": "股票",
    "title": "SpaceX to acquire Cursor for $60B in stock, days after blockbuster IPO",
    "url": "https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/",
    "source": "frb",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-06-16T12:09:34+00:00",
    "summary": ""
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
    "id": "hn:48496263",
    "domain": "股票",
    "title": "Musk's SpaceX prices record $75B IPO at $135 a share",
    "url": "https://www.reuters.com/world/musks-spacex-prices-record-75-billion-ipo-135-share-2026-06-11/",
    "source": "TechTechTech",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-11T20:53:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48497351",
    "domain": "股票",
    "title": "SpaceX officially prices shares at $135 in the largest IPO ever",
    "url": "https://techcrunch.com/2026/06/11/spacex-officially-prices-shares-at-135-in-the-largest-ipo-ever/",
    "source": "7777777phil",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-11T22:36:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48506306",
    "domain": "股票",
    "title": "SpaceX vaults over $2T valuation as stock jumps after record IPO",
    "url": "https://www.reuters.com/legal/transactional/after-record-ipo-musks-spacex-faces-next-test-market-debut-2026-06-12/",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-12T16:39:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48611631",
    "domain": "股票",
    "title": "The Myth of SpaceX",
    "url": "https://www.theatlantic.com/technology/2026/06/spacex-starlink-ipo-elon-musk-trillionaire/687651/",
    "source": "paulpauper",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-06-20T18:30:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48518603",
    "domain": "股票",
    "title": "SpaceX IPO made Musk a trillionaire. The old rules of capitalism no longer apply",
    "url": "https://www.theguardian.com/commentisfree/2026/jun/12/spacex-ipo-elon-musk-trillionaire",
    "source": "jmngomes",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-06-13T16:09:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48552280",
    "domain": "股票",
    "title": "SpaceX IPO Is a Giant Unworkable Con",
    "url": "https://karlbode.com/the-spacex-ipo-is-a-giant-unworkable-con-orchestrated-by-an-overt-white-supremacist-huckster/",
    "source": "only_in_america",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-06-16T08:30:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48717469",
    "domain": "金融",
    "title": "The CEO of Mullvad is the main financer of the Swedish Örebro party",
    "url": "https://det.social/@lostgen/116820546568940358",
    "source": "Risse",
    "platform": "hackernews",
    "points": 694,
    "published_at": "2026-06-29T10:45:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:48759634",
    "domain": "金融",
    "title": "PeerTube is a free, decentralized and federated video platform",
    "url": "https://github.com/Chocobozzz/PeerTube",
    "source": "doener",
    "platform": "hackernews",
    "points": 680,
    "published_at": "2026-07-02T11:17:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48552687",
    "domain": "金融",
    "title": "Feds freaked over Fable 5 after 'fix this code', not jailbreak, say researchers",
    "url": "https://www.theregister.com/security/2026/06/15/feds-freaked-over-fable-5-after-simple-fix-this-code-prompt-not-jailbreak-says-researcher/5255827",
    "source": "_tk_",
    "platform": "hackernews",
    "points": 613,
    "published_at": "2026-06-16T09:26:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:48634585",
    "domain": "金融",
    "title": "Canada plans 'nuclear renaissance' with up to 10 reactors built by 2040",
    "url": "https://www.cbc.ca/news/politics/federal-nuclear-strategy-9.7244509",
    "source": "geox",
    "platform": "hackernews",
    "points": 593,
    "published_at": "2026-06-22T19:06:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48647444",
    "domain": "金融",
    "title": "Digital euro clears key hurdle as EU seeks to break free from U.S. credit cards",
    "url": "https://finance.yahoo.com/markets/currencies/articles/ecb-secures-key-parliamentary-backing-102718449.html",
    "source": "madars",
    "platform": "hackernews",
    "points": 232,
    "published_at": "2026-06-23T16:27:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48673787",
    "domain": "金融",
    "title": "Federal agents track down woman, demand she remove Instagram post about ICE",
    "url": "https://www.syracuse.com/news/2026/06/federal-agents-track-down-syracuse-woman-demand-she-remove-instagram-post-about-ice.html",
    "source": "coloneltcb",
    "platform": "hackernews",
    "points": 217,
    "published_at": "2026-06-25T14:16:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:48777266",
    "domain": "金融",
    "title": "International chess federation sanctions Kramnik",
    "url": "https://www.fide.com/fide-ethics-disciplinary-commission-issues-a-decision-in-case-involving-gm-vladimir-kramnik/",
    "source": "DarkContinent",
    "platform": "hackernews",
    "points": 169,
    "published_at": "2026-07-03T17:04:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48826703",
    "domain": "金融",
    "title": "Is The Economist Always Wrong?",
    "url": "https://www.economist.com/interactive/finance-and-economics/2026/07/02/is-the-economist-always-wrong",
    "source": "nreece",
    "platform": "hackernews",
    "points": 138,
    "published_at": "2026-07-08T02:17:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:48703613",
    "domain": "金融",
    "title": "Feds Killed Polestar and Spared Volvo",
    "url": "https://www.thedrive.com/news/feds-killed-polestar-and-spared-volvo-that-should-terrify-you",
    "source": "mraniki",
    "platform": "hackernews",
    "points": 175,
    "published_at": "2026-06-28T01:55:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48783175",
    "domain": "金融",
    "title": "The LLVM Compiler Infrastructure",
    "url": "https://cacm.acm.org/federal-funding-of-academic-research/the-llvm-compiler-infrastructure/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 80,
    "published_at": "2026-07-04T06:43:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:48849827",
    "domain": "金融",
    "title": "FrontierFinance: The largest open benchmark for investor workflows",
    "url": "https://research.samaya.ai/benchmarks/frontier-finance",
    "source": "ashwinpp",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-09T17:49:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48785077",
    "domain": "金融",
    "title": "The Fediverse Is Not the Way Forward",
    "url": "https://trialandfailure.net/the-fediverse-is-not-the-way-forward/",
    "source": "ExMachina73",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-07-04T12:53:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:48824584",
    "domain": "金融",
    "title": "JPMorgan, BofA and Others Explore Buying Card Network to Raise Debit-Card Fees",
    "url": "https://www.wsj.com/finance/banking/jpmorgan-bank-of-america-and-other-banks-explore-a-deal-to-shake-up-payments-world-9d8639fb",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-07-07T22:04:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48735748",
    "domain": "金融",
    "title": "Supreme Court takes sledgehammer to federal regulatory structure",
    "url": "https://www.npr.org/2026/06/29/nx-s1-5875161/supreme-court-takes-sledgehammer-to-much-of-federal-governments-regulatory-structure",
    "source": "marojejian",
    "platform": "hackernews",
    "points": 82,
    "published_at": "2026-06-30T17:05:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48791799",
    "domain": "金融",
    "title": "Is The Economist Always Wrong?",
    "url": "https://economist.com/interactive/finance-and-economics/2026/07/02/is-the-economist-always-wrong",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-07-05T06:40:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48653311",
    "domain": "金融",
    "title": "Prairieland defendants sentenced today to prison terms ranging from 30-100 years",
    "url": "https://prairielanddefendants.com/press-release/eight-federal-prairieland-defendants-sentenced-today-to-prison-terms-ranging-from-30-100-years-for-common-protest-activity/",
    "source": "panic",
    "platform": "hackernews",
    "points": 88,
    "published_at": "2026-06-23T23:54:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:48734220",
    "domain": "金融",
    "title": "Supreme Court strikes down limits on party spending in federal elections",
    "url": "https://apnews.com/article/supreme-court-campaign-finance-party-spending-ohio-91e49ee112197ae1210a9abfa46986ed",
    "source": "khriss",
    "platform": "hackernews",
    "points": 67,
    "published_at": "2026-06-30T15:34:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:48756848",
    "domain": "金融",
    "title": "He sent a harsh email to ICE's top official. Federal agents tracked him down",
    "url": "https://www.npr.org/2026/07/01/nx-s1-5874124/dhs-tracks-ice-critic",
    "source": "OutOfHere",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-07-02T05:20:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:48780128",
    "domain": "金融",
    "title": "AI First: How the Federal Government Is Prioritizing AI over People and Planet",
    "url": "https://stopgreedbuildgreen.climateandcommunity.org/posts/ai-first",
    "source": "eatox",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-03T21:21:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48754128",
    "domain": "金融",
    "title": "US feds are actively hiring \"person who decides which models to ban\"",
    "url": "https://www.usajobs.gov/job/856265200",
    "source": "arm32",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-07-01T22:45:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48609233",
    "domain": "金融",
    "title": "Big Tech is borrowing like never before",
    "url": "https://startupfortune.com/big-tech-is-borrowing-like-never-before-and-the-fed-just-made-that-a-lot-more-expensive/",
    "source": "krupan",
    "platform": "hackernews",
    "points": 64,
    "published_at": "2026-06-20T13:49:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:48796110",
    "domain": "金融",
    "title": "Moving back home used to be a sign of failure. Now it shows financial savvy",
    "url": "https://www.wsj.com/lifestyle/relationships/living-with-parents-finances-0c35530c",
    "source": "apparent",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-07-05T17:34:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48723371",
    "domain": "金融",
    "title": "Feds Tracked Down an Anti-ICE Dad in NYC Hotel, but How?",
    "url": "https://gizmodo.com/federal-agents-reportedly-tracked-down-an-anti-ice-dad-in-a-new-york-hotel-its-not-clear-how-2000778714",
    "source": "ripe",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-06-29T18:42:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48779065",
    "domain": "金融",
    "title": "Tesla Robotaxi Launches in Miami",
    "url": "https://twitter.com/robotaxi/status/2073030246161367153",
    "source": "spikels",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-07-03T19:38:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:48678494",
    "domain": "金融",
    "title": "Feds deny Polestar authorization to sell cars in US from model year 2027",
    "url": "https://arstechnica.com/cars/2026/06/feds-deny-polestar-authorization-to-sell-cars-in-us-from-model-year-2027/",
    "source": "Quinner",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-06-25T20:00:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48546358",
    "domain": "金融",
    "title": "US Government Reportedly Allowing Federal Data Center Rules to Expire",
    "url": "https://gizmodo.com/us-government-reportedly-allowing-federal-data-center-rules-to-expire-2000772083",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-06-15T20:06:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48763600",
    "domain": "金融",
    "title": "Married couple killed in first known fatal Tesla Semi crash",
    "url": "https://www.sfchronicle.com/tech/article/tesla-semi-fatal-crash-22329122.php",
    "source": "FireBeyond",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-02T16:09:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:48673197",
    "domain": "金融",
    "title": "Federating Clusters for Zero-Downtime Kubernetes",
    "url": "https://linkerd.io/2026/06/24/federating-clusters-for-zero-downtime-kubernetes/index.html",
    "source": "PagCatOli",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-06-25T13:37:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48518434",
    "domain": "金融",
    "title": "Gas Prices Wipe Out More Than a Year of Wage Gains",
    "url": "https://www.wsj.com/economy/inflation-wages-american-workers-cbe3f187",
    "source": "karakoram",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-06-13T15:49:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:48613112",
    "domain": "金融",
    "title": "Dallas Fed: 30% of housing cost increase driven by unauthorized immigration [pdf]",
    "url": "https://www.dallasfed.org/~/media/documents/research/papers/2026/wp2607.pdf",
    "source": "silexia",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-06-20T21:25:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48523232",
    "domain": "金融",
    "title": "Monero Inflation Checker",
    "url": "https://www.moneroinflation.com/",
    "source": "Cider9986",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-06-14T01:16:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48500251",
    "domain": "金融",
    "title": "Infineon to open fab in Germany as part of sovereignty push",
    "url": "https://sg.finance.yahoo.com/news/infineon-open-german-chip-fab-225013833.html?guccounter=1",
    "source": "SanjayMehta",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-06-12T05:26:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:48677039",
    "domain": "金融",
    "title": "The AI Data-Center Boom Is Sparking a Third Wave of Inflation",
    "url": "https://www.wsj.com/economy/the-data-center-boom-is-sparking-a-third-wave-of-inflation-926adc6e",
    "source": "gmays",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-06-25T17:58:44+00:00",
    "summary": ""
  }
]
```
