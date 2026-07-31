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

- 今日日期：`2026-07-31`
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
  "date": "2026-07-31",
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
    "points": 4008396,
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
    "points": 1636667,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1518094,
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
    "points": 1297306,
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
    "points": 1010994,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1007976,
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
    "points": 981212,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1ZzvUBXEoL",
    "domain": "AI",
    "title": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av115818910194374",
    "source": "极客教学",
    "platform": "bilibili",
    "points": 801759,
    "published_at": "2026-01-01T08:40:14+00:00",
    "summary": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 578528,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 438274,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 430610,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 419023,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 376228,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 252488,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 213206,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 193144,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 178186,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 162804,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 160447,
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
    "points": 158361,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "domain": "AI",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 153454,
    "published_at": "2026-01-11T15:43:58+00:00",
    "summary": "🚀开发者必看！Superpowers把专业工程团队方法论固化成Skills，让Claude Code告别越写越乱的困境：规格驱动+代码质量双重保障！AI编程新范式！头脑风暴+计划+执行一条龙自动化\n\n\n🚀🚀🚀 视频简介：\n🎬 本期视频详细演示了开源AI编程工作流系统Superpowers的完整使用方法，并通过开发一款iOS时间线笔记原生应用来实测其效果。\n🔧 核心内容：\nSuperpowers工作"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 149853,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 125954,
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
    "points": 113126,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1t9oZBDENp",
    "domain": "AI",
    "title": "Agent Loop: 多智能体协同，让AI长时工作，从原理到实践",
    "url": "http://www.bilibili.com/video/av116469396413175",
    "source": "费曼学徒冬瓜",
    "platform": "bilibili",
    "points": 106883,
    "published_at": "2026-04-26T12:00:00+00:00",
    "summary": "睡前给AI丢了一句话，醒来直接验收成果——怎么让AI连续干活几小时不拉胯？\n这期我们从原理到实战，彻底讲清楚 Harness 工程：让 AI 长时间自主工作的核心技术。\n内容涵盖两种方案：\nRalph 方案：用 while 循环不断启动新会话，通过文件系统衔接上下文\n多智能体方案（推荐）：主 Agent 只协调不干活，子 Agent 各司其职，开发测试分工明确\n重点讲了多智能体的完整流程设计：怎么"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92855,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1GRKJ6fEgn",
    "domain": "AI",
    "title": "Kimi K3编程能力炸裂！在Claude Code中全方位实测代码能力，能否超越Fable 5和GPT-5.6l？结果远超我的预期！国产模型跻身世界第一梯队！",
    "url": "http://www.bilibili.com/video/av116934511239163",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 87877,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV1Tv3i6LEX1",
    "domain": "AI",
    "title": "用Codex、cursor 还是Claude ？程序员不作选择题，我都要用，还一起用 | Orca ADE 介绍",
    "url": "http://www.bilibili.com/video/av116996217838997",
    "source": "技术胖",
    "platform": "bilibili",
    "points": 69878,
    "published_at": "2026-07-28T06:41:31+00:00",
    "summary": "如果能把 Codex、Claude Code、Grok、Cursor 等智能编程工具整合到同一个工作环境中，再让多个 Agent 像团队成员一样分工协作，软件开发的效率将得到显著提升。Orca ADE 正是为此而生：它是一款开源、免费的 Agent 开发环境，专注于代码管理与命令行工作流，不仅能够接入多种编程 Agent，还支持语音操作和手机远程管理。接下来，我们就来认识一下 Orca ADE，看"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53469,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 50836,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47520,
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
    "points": 44682,
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
    "points": 39456,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 38620,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 33975,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1JU7E6PEar",
    "domain": "AI",
    "title": "Cursor 已死？我为什么要退订 Cursor ？",
    "url": "http://www.bilibili.com/video/av116819553683121",
    "source": "祥子在学AI",
    "platform": "bilibili",
    "points": 33172,
    "published_at": "2026-06-27T01:52:00+00:00",
    "summary": "当了一年多的 Cursor 重度用户，最近把它退订了。\n\n不是它变差了，是 Claude Code 和 Codex 真的太好用了。\n\n几个真实感受： ① 大模型越来越强，我已经不怎么手写代码了 ② Cursor 套的是 VS Code 壳子，只属于程序员 ③ 底层模型不在一个量级——Claude 有 Opus 和 Fable 5，Codex 有 GPT 5.5/5.6，Cursor 的 Compo"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 29907,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28833,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1pkK56aEVG",
    "domain": "AI",
    "title": "GPT-5.6在Claude Code中表现远超Codex | Theo - t3․gg",
    "url": "http://www.bilibili.com/video/av116929612221157",
    "source": "浮生千山路w",
    "platform": "bilibili",
    "points": 25903,
    "published_at": "2026-07-16T12:29:37+00:00",
    "summary": "来源：https://www.youtube.com/watch?v=Noo0NWD0gHU\n原标题：gpt 5.6 is way better in Claude Code\n频道：Theo - t3․gg\n发布时间：2026-07-16\n\n内容简介：\n作者使用GPT-5.6 Sol版本在Claude Code中进行编程，发现其表现相较于Codex有显著提升，体验令人震惊。视频由Coderabbi"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 25824,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV16ggC6DEZK",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116963049212769",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 24216,
    "published_at": "2026-07-22T10:10:42+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22670,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1zjd3BiEzo",
    "domain": "AI",
    "title": "别再二选一：Claude Code + Codex 联用才是最强姿势",
    "url": "http://www.bilibili.com/video/av116537746791000",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 19136,
    "published_at": "2026-05-08T07:34:23+00:00",
    "summary": "Codex 已悄然追上 Claude Code，GPT 5.5 比肩 Opus 4.7、OpenAI Pro 额度更大方。但作者 Chase 想说：别再纠结谁更好，最佳姿势是把两者一起用——Codex 桌面应用直接跑 Claude Code 终端，让两个模型互查方案、互查代码（一次实测 Claude Code 帮 Codex 抓出 20 个 bug）。背后更重要的思路是 tool agnostic"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 18802,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17658,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1hnjGzLE14",
    "domain": "AI",
    "title": "【小智教程】手挽手教你如何接入别人的MCP服务",
    "url": "http://www.bilibili.com/video/av114568722450105",
    "source": "空白泡泡糖果",
    "platform": "bilibili",
    "points": 17572,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 17347,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 17186,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 15842,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "7月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "iwenwikii",
    "platform": "bilibili",
    "points": 14869,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "AI充值站：njzqhy.top"
  },
  {
    "id": "hn:49035303",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, Microsoft, Meta warn against overregulating open-weight models",
    "url": "https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 659,
    "published_at": "2026-07-24T13:32:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49034868",
    "domain": "AI 算力 / 半导体",
    "title": "Half-Life 2 running natively on HaikuOS",
    "url": "https://discuss.haiku-os.org/t/haiku-nvidia-porting-nvidia-driver-for-turing-gpus/16520?page=18",
    "source": "m0do1",
    "platform": "hackernews",
    "points": 339,
    "published_at": "2026-07-24T12:53:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49035751",
    "domain": "AI 算力 / 半导体",
    "title": "Open Weights and American AI Leadership [pdf]",
    "url": "https://images.nvidia.com/pdf/Open-Weights-and-American-AI-Leadership.pdf",
    "source": "lairv",
    "platform": "hackernews",
    "points": 112,
    "published_at": "2026-07-24T13:58:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49071512",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's $750B in Deals Reignite Circular AI Fears",
    "url": "https://www.bloomberg.com/news/articles/2026-07-27/nvidia-s-750-billion-deals-revive-fear-of-ai-circular-financing",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-07-27T16:02:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:48971128",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia DGX Spark as a daily driver",
    "url": "https://daniel.lawrence.lu/blog/2026-07-15-dgx-spark-as-daily-driver/",
    "source": "plun9",
    "platform": "hackernews",
    "points": 102,
    "published_at": "2026-07-19T19:44:44+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/space-grown-semiconductors-the-next-frontier-for-ai-compute/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Is Compressing Software; Space Is Building the Physical Economy",
    "url": "https://www.eetimes.com/space-grown-semiconductors-the-next-frontier-for-ai-compute/",
    "source": "Zaheer Ali",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T21:03:54+00:00",
    "summary": "AI is squeezing software jobs; space and semiconductors are where tech turns physical. The post AI Is Compressing Software; Space Is Building the Physical Economy appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/why-qualcomm-bought-an-open-ai-software-stack/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Qualcomm Bought An Open AI Software Stack",
    "url": "https://www.eetimes.com/why-qualcomm-bought-an-open-ai-software-stack/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T14:43:40+00:00",
    "summary": "Modular says Qualcomm is committed to keeping Mojo and Max hardware-agnostic as heterogeneous AI infrastructure moves from theory to reality. The post Why Qualcomm Bought An Open AI Software Stack app"
  },
  {
    "id": "rss:https://www.eetimes.com/nidec-positions-precision-reducers-for-cobots-humanoids-and-automation/",
    "domain": "AI 算力 / 半导体",
    "title": "Nidec Positions Precision Reducers for Cobots, Humanoids, and Automation",
    "url": "https://www.eetimes.com/nidec-positions-precision-reducers-for-cobots-humanoids-and-automation/",
    "source": "Nidec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T13:00:00+00:00",
    "summary": "Discover Nidec's gear reducer solutions offering precise gear alignment, and low backlash for smooth, reliable operation under load. The post Nidec Positions Precision Reducers for Cobots, Humanoids, "
  },
  {
    "id": "rss:https://www.eetimes.com/indian-startup-vimag-labs-develops-wirelessly-excited-motor-without-rare-earth-magnets/",
    "domain": "AI 算力 / 半导体",
    "title": "Indian Startup Vimag Labs Develops Wirelessly Excited Motor Without Rare-Earth Magnets",
    "url": "https://www.eetimes.com/indian-startup-vimag-labs-develops-wirelessly-excited-motor-without-rare-earth-magnets/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T07:00:00+00:00",
    "summary": "Vimag Labs ditches rare-earth magnets with a wirelessly excited EV motor claiming PMSM-level punch. The post Indian Startup Vimag Labs Develops Wirelessly Excited Motor Without Rare-Earth Magnets appe"
  },
  {
    "id": "rss:https://www.eetimes.com/iot-tech-expo-europe-returns-to-amsterdam-as-industrial-ai-and-edge-intelligence-reshape-connected-industry/",
    "domain": "AI 算力 / 半导体",
    "title": "IoT Tech Expo Europe Returns to Amsterdam as Industrial AI and Edge Intelligence Reshape Connected Industry",
    "url": "https://www.eetimes.com/iot-tech-expo-europe-returns-to-amsterdam-as-industrial-ai-and-edge-intelligence-reshape-connected-industry/",
    "source": "IoT Tech Expo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T00:42:04+00:00",
    "summary": "From autonomous factories and AI-powered robots to connected vehicles and smart cities, organizations are entering a new era where connected systems are expected not only to collect data, but also to "
  },
  {
    "id": "rss:https://www.eetimes.com/dynamic-ai-demands-drive-memory-diversity/",
    "domain": "AI 算力 / 半导体",
    "title": "Dynamic AI Demands Drive Memory Diversity",
    "url": "https://www.eetimes.com/dynamic-ai-demands-drive-memory-diversity/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T18:00:00+00:00",
    "summary": "AI workloads aren't creating new memory categories—they're sharpening the trade-offs between capacity, latency, and power. The post Dynamic AI Demands Drive Memory Diversity appeared first on EE Times"
  },
  {
    "id": "rss:https://www.eetimes.com/commercial-space-screening-approach-for-agile-high-reliability-payloads-2/",
    "domain": "AI 算力 / 半导体",
    "title": "Commercial Space Screening Approach for Agile, High-Reliability Payloads",
    "url": "https://www.eetimes.com/commercial-space-screening-approach-for-agile-high-reliability-payloads-2/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T14:00:00+00:00",
    "summary": "As satellite deployments accelerate and mission economics evolve, engineers face a growing challenge: balancing the reliability demands of space operation with the cost, lead-time, size, and technolog"
  },
  {
    "id": "rss:https://www.eetimes.com/physical-ai-isnt-just-bigger-ai-its-a-systems-architecture-challenge/",
    "domain": "AI 算力 / 半导体",
    "title": "Physical AI Isn’t Just Bigger AI; It’s a Systems Architecture Challenge",
    "url": "https://www.eetimes.com/physical-ai-isnt-just-bigger-ai-its-a-systems-architecture-challenge/",
    "source": "Rahul Patel, president and CEO, board director, Synaptics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T14:00:00+00:00",
    "summary": "Physical AI wins by fusing sensors, edge compute, and feedback loops. Learn why systems, not TOPS, matter. The post Physical AI Isn&#8217;t Just Bigger AI; It&#8217;s a Systems Architecture Challenge "
  },
  {
    "id": "rss:https://www.eetimes.com/designing-efficient-signal-chains-with-easy-drive-adcs/",
    "domain": "AI 算力 / 半导体",
    "title": "Designing Efficient Signal Chains with Easy Drive ADCs",
    "url": "https://www.eetimes.com/designing-efficient-signal-chains-with-easy-drive-adcs/",
    "source": "Analog Devices, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T12:50:29+00:00",
    "summary": "Date: Wednesday, August 19, 2026&#160;or&#160;Wednesday, August 26, 2026 This webcast will explain how and why Easy Drive SAR ADCs from Analog Devices can deliver the precision you need without the he"
  },
  {
    "id": "rss:https://www.eetimes.com/from-co-packaged-optics-to-nanolasers-photonics-moves-inward/",
    "domain": "AI 算力 / 半导体",
    "title": "From Co-Packaged Optics to Nanolasers, Photonics Moves Inward",
    "url": "https://www.eetimes.com/from-co-packaged-optics-to-nanolasers-photonics-moves-inward/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T08:02:27+00:00",
    "summary": "CEA-Leti, Scintil Photonics, and NcodiN show how optical interconnects are moving from data center racks toward co-packaged optics and chiplet-level communication. The post From Co-Packaged Optics to "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/shanghai-aishengna-named-as-the-maker-of-chinas-first-domestic-immersion-duv-scanners",
    "domain": "AI 算力 / 半导体",
    "title": "Shanghai Aishengna named as the maker of China's first domestic immersion DUV chipmaking tools — first viable domestic 7nm-capable scanner to be completed by 2038",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/shanghai-aishengna-named-as-the-maker-of-chinas-first-domestic-immersion-duv-scanners",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T16:23:55+00:00",
    "summary": "Aishengna has been named by a single source who declined to be named, and its shareholders, SMEE, and Yuliangsheng didn’t respond to requests for comment."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-accidentally-spent-usd1-8-million-using-claude-for-menial-coding-task-went-860-percent-over-budget-catastrophically-expensive-coding-blunders-discovered-in-internal-amazon-ai-usage-metrics",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon accidentally spent $1.8 million using Claude for menial coding task, went 860% over budget —'catastrophically expensive' coding blunders discovered in internal Amazon AI usage metrics",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-accidentally-spent-usd1-8-million-using-claude-for-menial-coding-task-went-860-percent-over-budget-catastrophically-expensive-coding-blunders-discovered-in-internal-amazon-ai-usage-metrics",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T16:08:25+00:00",
    "summary": "An internal presentation revealed that a failed AI deployment cost Amazon $1.8 million, while a couple of other projects resulted in hundreds of thousands of extra AI expense. What's worse is that the"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/psa-your-watch-band-may-be-messing-with-your-laptop-magnetic-clasps-can-cause-lid-sensors-to-lock-your-pc",
    "domain": "AI 算力 / 半导体",
    "title": "PSA: Your watch band may be messing with your laptop – magnetic clasps can cause lid sensors to lock your PC",
    "url": "https://www.tomshardware.com/laptops/psa-your-watch-band-may-be-messing-with-your-laptop-magnetic-clasps-can-cause-lid-sensors-to-lock-your-pc",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T15:09:46+00:00",
    "summary": "It’s likely a niche issue, but I discovered recently that my magnetic watch clasp was confusing an Acer laptop into thinking I was closing and opening the lid, causing me to repeatedly get logged out "
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/exploring-apple-silicons-local-ai-performance-with-the-mac-studio-and-m4-max-m4-max-beats-gb10-and-strix-halo-in-decode-throughput-but-memory-bandwidth-isnt-everything",
    "domain": "AI 算力 / 半导体",
    "title": "Exploring Apple Silicon’s local AI performance with the Mac Studio and M4 Max — M4 Max beats GB10 and Strix Halo in decode throughput, but memory bandwidth isn't everything",
    "url": "https://www.tomshardware.com/desktops/exploring-apple-silicons-local-ai-performance-with-the-mac-studio-and-m4-max-m4-max-beats-gb10-and-strix-halo-in-decode-throughput-but-memory-bandwidth-isnt-everything",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T14:52:28+00:00",
    "summary": "Apple Silicon has been a popular choice for local AI exploration thanks to its high memory bandwidth compared to other unified memory platforms. We tested the M4 Max version of Apple's Mac Studio to s"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/google-could-build-more-ai-accelerators-than-nvidia-sells-in-2028-analyst-claims-could-push-the-company-to-use-intel-foundry-to-meet-its-goals",
    "domain": "AI 算力 / 半导体",
    "title": "Google could build more AI accelerators than Nvidia sells in 2028, analyst claims — could push the company to use Intel Foundry to meet its goals",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/google-could-build-more-ai-accelerators-than-nvidia-sells-in-2028-analyst-claims-could-push-the-company-to-use-intel-foundry-to-meet-its-goals",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T14:35:50+00:00",
    "summary": "Google eyes to build more TPU AI accelerators in 2028 than Nvidia, if a report by Fubon Research is correct."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidias-fastest-graphics-cards-get-us-price-increase-at-best-buy-amazon-astral-rtx-5080-now-costs-more-than-5090s-msrp-flagship-card-now-commands-more-than-usd4-300",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's fastest graphics cards get US price increase at Best Buy, Amazon — Astral RTX 5080 now costs more than 5090's MSRP, flagship card now commands more than $4,300",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidias-fastest-graphics-cards-get-us-price-increase-at-best-buy-amazon-astral-rtx-5080-now-costs-more-than-5090s-msrp-flagship-card-now-commands-more-than-usd4-300",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T14:34:51+00:00",
    "summary": "Premium Nvidia GeForce RTX 5080 and RTX 5090 graphics cards are once again selling far above MSRP, with some Asus and MSI models climbing close to $5,000."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/examining-the-best-options-for-pcie-ssds-during-the-rampocalypse-capacity-trumps-raw-speed-for-most-tasks",
    "domain": "AI 算力 / 半导体",
    "title": "Examining the best options for PCIe SSDs during the RAMpocalypse — capacity trumps raw speed for most tasks",
    "url": "https://www.tomshardware.com/pc-components/ssds/examining-the-best-options-for-pcie-ssds-during-the-rampocalypse-capacity-trumps-raw-speed-for-most-tasks",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T14:22:24+00:00",
    "summary": "High SSD speeds are helpful in many applications, but should they trump the capacity of the SSD when it comes to gaming?"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-licenses-atom-class-x86-cores-to-startup-firm-reportedly-sharing-rtl-enabling-customer-to-build-its-own-custom-processors-based-on-x86-general-purpose-cores",
    "domain": "AI 算力 / 半导体",
    "title": "Intel licenses Atom-class x86 cores to startup — firm reportedly sharing RTL, enabling customer to build its own custom processors based on x86 general-purpose cores",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-licenses-atom-class-x86-cores-to-startup-firm-reportedly-sharing-rtl-enabling-customer-to-build-its-own-custom-processors-based-on-x86-general-purpose-cores",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T13:27:05+00:00",
    "summary": "Intel reportedly licenses Atom-class x86 cores to a startup led by Lip-Bu Tan's co-investor and incorporated in May."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/fcc-robot-ban-covers-any-ground-robot-over-4-4-pounds-with-a-200-kbps-connection",
    "domain": "AI 算力 / 半导体",
    "title": "Foreign-made robot vacuums caught up in FCC robot ban — covers any ground robot over 4.4 pounds with a 200 kbps connection",
    "url": "https://www.tomshardware.com/tech-industry/fcc-robot-ban-covers-any-ground-robot-over-4-4-pounds-with-a-200-kbps-connection",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T13:03:45+00:00",
    "summary": "The FCC has added foreign-produced advanced robotic devices and connected power inverters to its Covered List."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/why-you-need-a-macro-pad-even-if-you-have-a-mouse-with-19-buttons-from-usd10-mechanical-numpads-to-multi-screen-window-management",
    "domain": "AI 算力 / 半导体",
    "title": "Why you need a macro pad, even if you have a mouse with 19 buttons — from $10 mechanical numpads to multi-screen window management",
    "url": "https://www.tomshardware.com/peripherals/why-you-need-a-macro-pad-even-if-you-have-a-mouse-with-19-buttons-from-usd10-mechanical-numpads-to-multi-screen-window-management",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T12:21:40+00:00",
    "summary": "You don't need to be a streamer or do tons of data entry to make use of a standalone macro pad. Here are your options and why you should use them."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/a-mac-mini-server-is-running-headless-in-my-closet-it-manages-my-photo-library-and-handles-my-backups",
    "domain": "AI 算力 / 半导体",
    "title": "A Mac Mini server is running headless in my closet — it manages my photo library and handles my backups",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/a-mac-mini-server-is-running-headless-in-my-closet-it-manages-my-photo-library-and-handles-my-backups",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T11:58:11+00:00",
    "summary": "When I wanted to get more serious about backing up my family's data, I bought a refurbished Mac Mini and set it running headless in my closet. It's right for me."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/container-launched-cargo-rocket-promises-250-kg-deliveries-750-km-away-in-15-minutes",
    "domain": "AI 算力 / 半导体",
    "title": "Shipping container-launched cargo rocket promises 550-pound deliveries 750 km away in 15 minutes — $1.25M Air Force contract backs 'Rook' cargo rocket that flies into space to speed deliveries",
    "url": "https://www.tomshardware.com/tech-industry/container-launched-cargo-rocket-promises-250-kg-deliveries-750-km-away-in-15-minutes",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T11:45:00+00:00",
    "summary": "A minimum-energy ballistic arc covering 750 km needs roughly 2.64 km/s at burnout and peaks near 181 km."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/usd21-nintendo-wii-u-upgrade-lets-you-add-tbs-of-storage-to-your-console-with-an-m-2-or-sata-ssd-upgrade-makes-console-slightly-faster-but-requires-homebrew-and-custom-firmware",
    "domain": "AI 算力 / 半导体",
    "title": "$21 Nintendo Wii U upgrade lets you add TBs of storage to your console with an M.2 or SATA SSD — upgrade makes console slightly faster, but requires Homebrew and custom firmware",
    "url": "https://www.tomshardware.com/video-games/nintendo/usd21-nintendo-wii-u-upgrade-lets-you-add-tbs-of-storage-to-your-console-with-an-m-2-or-sata-ssd-upgrade-makes-console-slightly-faster-but-requires-homebrew-and-custom-firmware",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T11:42:22+00:00",
    "summary": "You can now upgrade your Wii U from an 8GB or 32GB internal storage to more than a TB with this SSD kit. You'll have to install the Aroma custom firmware on your console to use it, though."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/are-your-motherboards-m-2-heatsinks-making-good-contact-with-your-ssd-we-tested-20-modern-intel-and-amd-motherboards-to-verify",
    "domain": "AI 算力 / 半导体",
    "title": "Are your motherboard's M.2 heatsinks making good contact with your SSD? We tested 20 modern Intel and AMD motherboards to verify",
    "url": "https://www.tomshardware.com/pc-components/motherboards/are-your-motherboards-m-2-heatsinks-making-good-contact-with-your-ssd-we-tested-20-modern-intel-and-amd-motherboards-to-verify",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T11:23:44+00:00",
    "summary": "We tested 20 motherboards for proper M.2 contact and were surprised at the results – not all make good contact."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/30-georgia-homes-are-being-reclaimed-via-sale-or-eminent-domain-to-expand-power-grid-one-affected-family-member-says-its-for-the-data-centers",
    "domain": "AI 算力 / 半导体",
    "title": "30 Georgia homes are being acquired via sale or eminent domain to expand power grid — one affected family member says it’s ‘for the data centers’",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/30-georgia-homes-are-being-reclaimed-via-sale-or-eminent-domain-to-expand-power-grid-one-affected-family-member-says-its-for-the-data-centers",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T11:20:00+00:00",
    "summary": "Georgia's largest power supply company is reclaiming 30 homes that lay in the path of its power line expansion project through sale or eminent domain. The company says the project is not for a data ce"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/32gb-corsair-vengeance-ddr5-is-usd369-in-this-woot-sale-the-lowest-standalone-ram-price-right-now-thanks-to-a-usd132-discount",
    "domain": "AI 算力 / 半导体",
    "title": "32GB Corsair Vengeance DDR5 is $369 in this Woot sale — the lowest standalone RAM price right now, thanks to a $132 discount",
    "url": "https://www.tomshardware.com/pc-components/32gb-corsair-vengeance-ddr5-is-usd369-in-this-woot-sale-the-lowest-standalone-ram-price-right-now-thanks-to-a-usd132-discount",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T11:14:31+00:00",
    "summary": "Get Corsair Vengeance DDR5 for just $369 at Woot."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/grab-a-great-value-gaming-laptop-with-a-generous-amount-of-memory-for-only-usd1-199-save-usd100-on-gigabytes-aero-x16-gaming-laptop-with-32gb-of-ddr5-and-rtx-5060-graphics",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a great-value gaming laptop with a generous amount of memory for only $1,199 — save $100 on Gigabyte's Aero X16 gaming laptop with 32GB of DDR5 and RTX 5060 graphics",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/grab-a-great-value-gaming-laptop-with-a-generous-amount-of-memory-for-only-usd1-199-save-usd100-on-gigabytes-aero-x16-gaming-laptop-with-32gb-of-ddr5-and-rtx-5060-graphics",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T10:50:54+00:00",
    "summary": "Save $100 on a Gigabyte Aero 16X gaming laptop with a Ryzen AI 7 350 CPU, 32GB of RAM, and an RTX 5060 GPU in today's limited-time sale"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/operating-systems/legendary-windows-developer-codes-task-manager-for-the-mac-says-he-was-inspired-by-the-fact-that-apples-activity-monitor-blows",
    "domain": "AI 算力 / 半导体",
    "title": "Legendary Windows developer codes Task Manager for the Mac, says Apple’s ‘Activity Monitor blows’ — Microsoft gave original Windows Task Manager dev permission to reference Windows XP source code",
    "url": "https://www.tomshardware.com/software/operating-systems/legendary-windows-developer-codes-task-manager-for-the-mac-says-he-was-inspired-by-the-fact-that-apples-activity-monitor-blows",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T10:50:00+00:00",
    "summary": "Legendary Windows developer Dave W. Plummer has shared details and screenshots of a version of Task Manager for Apple Mac computers."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/save-33-percent-on-this-27-inch-lg-oled-1440p-gaming-monitor-with-an-ultra-fast-280hz-refresh-rate-now-just-usd399-limited-time-deal-nets-you-a-big-discount-on-this-high-spec-panel-with-nvidia-g-sync-and-amd-freesync-support",
    "domain": "AI 算力 / 半导体",
    "title": "Save 33% on this 27-inch LG OLED 1440p gaming monitor with an ultra-fast 280Hz refresh rate, now just $399 — limited-time deal nets you a big discount on this high-spec panel with Nvidia G-Sync and AM",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/save-33-percent-on-this-27-inch-lg-oled-1440p-gaming-monitor-with-an-ultra-fast-280hz-refresh-rate-now-just-usd399-limited-time-deal-nets-you-a-big-discount-on-this-high-spec-panel-with-nvidia-g-sync-and-amd-freesync-support",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T10:31:26+00:00",
    "summary": "This 27-inch LG OLED gaming monitor with a 280Hz refresh rate has dropped is on sale right now for $399.99 in a deal that'll save you $200."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/gamers-compress-80tb-map-of-minecrafts-oldest-anarchy-server-down-to-a-15tb-download-custom-zvcr-compression-format-and-28-bots-map-1-million-blocks-on-2b2t",
    "domain": "AI 算力 / 半导体",
    "title": "Gamers compress 80TB map of Minecraft's oldest anarchy server down to a 15TB download — custom .zvcr compression format and 28 bots map 1 million blocks on infamous 2b2t server",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/gamers-compress-80tb-map-of-minecrafts-oldest-anarchy-server-down-to-a-15tb-download-custom-zvcr-compression-format-and-28-bots-map-1-million-blocks-on-2b2t",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T10:25:00+00:00",
    "summary": "Minecraft enthusiasts come together to archive Minecraft's 2b2t server, which currently weighs over 80TB but is compressed to a mere 15TB."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-company-hiring-a-literal-pirate-to-salvage-sunken-treasure-found-by-artificial-intelligence-pays-up-to-usd500k-a-year-mining-80-million-pages-of-spanish-colonial-records-to-find-undiscovered-wrecks-and-lost-cargo",
    "domain": "AI 算力 / 半导体",
    "title": "Firm that uses AI to locate ancient lost shipwrecks is hiring a literal pirate to salvage sunken treasure, paying up to $500,000 a year — AI mines 500 years of Spanish colonial records spanning 80 mil",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-company-hiring-a-literal-pirate-to-salvage-sunken-treasure-found-by-artificial-intelligence-pays-up-to-usd500k-a-year-mining-80-million-pages-of-spanish-colonial-records-to-find-undiscovered-wrecks-and-lost-cargo",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T10:00:00+00:00",
    "summary": "AI and software research firm looking for a real-life pirate — extremely remote lob listing requires nautical and diving experience"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/pennsylvania-town-lists-43-specific-demands-to-approve-new-data-center-project-developer-calls-local-demands-too-difficult-as-council-slams-response-as-approval-by-tantrum",
    "domain": "AI 算力 / 半导体",
    "title": "Pennsylvania town lists 43 specific demands to approve new AI data center project — developer calls local demands 'too difficult' as council slams response as 'approval by tantrum'",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/pennsylvania-town-lists-43-specific-demands-to-approve-new-data-center-project-developer-calls-local-demands-too-difficult-as-council-slams-response-as-approval-by-tantrum",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T09:30:00+00:00",
    "summary": "One township in Pennsylvania gave a specific list of demands for a data center developer to follow if they want to build their project in the area. Instead, they retracted their initial application an"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/xbox/microsoft-says-physical-discs-should-not-have-stopped-working-during-the-xbox-outage-clarifies-issue-with-entitlement-checks-that-failed-to-read-licenses-correctly-update-on-the-way",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft says physical discs should not have stopped working during the Xbox outage — clarifies issue with entitlement checks that failed to read licenses correctly, update on the way",
    "url": "https://www.tomshardware.com/video-games/xbox/microsoft-says-physical-discs-should-not-have-stopped-working-during-the-xbox-outage-clarifies-issue-with-entitlement-checks-that-failed-to-read-licenses-correctly-update-on-the-way",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T18:05:17+00:00",
    "summary": "Microsoft has confirmed that you should've been able to play your discs offline during the Xbox outage yesterday. The company has identified an issue with entitlement checks that prevented the correct"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/hdds/seagate-to-start-qualifying-record-setting-50tb-hdds-in-2027-most-drives-are-sold-out-through-2028",
    "domain": "AI 算力 / 半导体",
    "title": "Seagate to start qualifying record-setting 50TB HDDs in 2027 — most drives are sold out through 2028",
    "url": "https://www.tomshardware.com/pc-components/hdds/seagate-to-start-qualifying-record-setting-50tb-hdds-in-2027-most-drives-are-sold-out-through-2028",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T16:40:53+00:00",
    "summary": "Seagate expects to begin customer qualification of its 50TB-class HAMR hard drives in late 2027 with shipments in 2028 as AI-driven storage demand keeps production largely sold out through 2028."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/nvidia-employee-implicated-in-escalating-supermicro-smuggling-scandal-but-demand-only-intensifies-for-nvidia-hardware",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia employee implicated in escalating AI GPU smuggling scandal, but demand only intensifies for Nvidia hardware",
    "url": "https://www.tomshardware.com/tech-industry/nvidia-employee-implicated-in-escalating-supermicro-smuggling-scandal-but-demand-only-intensifies-for-nvidia-hardware",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T15:10:06+00:00",
    "summary": "An Nvidia employee has been implicated in the AI GPU smuggling scandal, with his home and desk searched. He's been detained over allegations of forgery and breach of trust. Meanwhile, Nvidia is collap"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/valve-says-that-steam-machine-reservations-wont-be-fulfilled-until-the-end-of-this-year-company-also-releases-cad-files-for-the-pc-consoles-external-shell-under-creative-commons",
    "domain": "AI 算力 / 半导体",
    "title": "Valve says that Steam Machine reservations won't be fulfilled until ‘the end of this year’ — company also releases CAD files for the PC console’s external shell under Creative Commons",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/valve-says-that-steam-machine-reservations-wont-be-fulfilled-until-the-end-of-this-year-company-also-releases-cad-files-for-the-pc-consoles-external-shell-under-creative-commons",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T15:03:56+00:00",
    "summary": "Everyone who reserved the Steam Machine can get the chance to buy one before the year ends. Valve says availability differs between models and regions, and that some areas have already completed the r"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/an-inside-tour-of-lenovos-north-carolina-ai-server-manufacturing-line-expansion-chinese-firm-expanding-us-native-production-to-meet-exploding-demand",
    "domain": "AI 算力 / 半导体",
    "title": "An inside tour of Lenovo’s North Carolina AI server manufacturing line expansion — Chinese firm expanding US-native production to meet exploding demand",
    "url": "https://www.tomshardware.com/laptops/an-inside-tour-of-lenovos-north-carolina-ai-server-manufacturing-line-expansion-chinese-firm-expanding-us-native-production-to-meet-exploding-demand",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T14:27:06+00:00",
    "summary": "Lenovo is fulfilling demand for homemade servers to fuel the AI boom."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/gpu-repair-service-will-upgrade-the-11gb-of-vram-on-your-rtx-2080-ti-to-22gb-mod-involves-physically-adjusting-the-strap-resistors-on-the-pcb-to-support-a-new-bios",
    "domain": "AI 算力 / 半导体",
    "title": "GPU repair service will upgrade the 11GB of VRAM on your RTX 2080 Ti to 22GB — mod involves physically adjusting the strap resistors on the PCB to support a new BIOS",
    "url": "https://www.tomshardware.com/pc-components/gpus/gpu-repair-service-will-upgrade-the-11gb-of-vram-on-your-rtx-2080-ti-to-22gb-mod-involves-physically-adjusting-the-strap-resistors-on-the-pcb-to-support-a-new-bios",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T14:00:12+00:00",
    "summary": "A GPU repair shop in the UAE is promising to upgrade the VRAM capacity of an RTX 2080 Ti from 11GB to 22GB by swapping the 1GB GDDR6 modules with 2GB chips and modifying the strap resistors to recogni"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/testing-laptops-on-battery-life-and-ac-power-comparing-intel-qualcomm-apple-and-amd",
    "domain": "AI 算力 / 半导体",
    "title": "Testing laptops on battery and AC power — Comparing Intel, Qualcomm, Apple, and AMD",
    "url": "https://www.tomshardware.com/laptops/testing-laptops-on-battery-life-and-ac-power-comparing-intel-qualcomm-apple-and-amd",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T13:07:18+00:00",
    "summary": "We tested laptops with processors from Intel, AMD, Qualcomm, and Apple to see the differences in how they perform on and off the charger."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/teacher-arrested-for-clapping-in-support-of-opposition-at-an-ai-data-center-meeting-gigawatt-scale-project-gets-approved-anyway-despite-community-resistance",
    "domain": "AI 算力 / 半导体",
    "title": "Teacher arrested for clapping in support of opposition at an AI data center meeting — gigawatt-scale project gets approved anyway despite community resistance",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/teacher-arrested-for-clapping-in-support-of-opposition-at-an-ai-data-center-meeting-gigawatt-scale-project-gets-approved-anyway-despite-community-resistance",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T13:06:16+00:00",
    "summary": "A Physics teacher was arrested for clapping multiple times during a public hearing to rezone land for a proposed gigawatt-scale data center near Emporia, Kansas. The man refused to cooperate when the "
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
    "id": "hn:49070311",
    "domain": "AI 算力 / 半导体",
    "title": "Ilya Sutskever's SSI and Nvidia Announce Long-Term Strategic Partnership",
    "url": "https://nvidianews.nvidia.com/news/ilya-sutskevers-safe-superintelligence-inc-and-nvidia-announce-long-term-strategic-partnership",
    "source": "lanakei",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-27T14:33:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:49093429",
    "domain": "AI 算力 / 半导体",
    "title": "Kospi Plunges After Nvidia CEO's Visits Spark 'Huang Curse' Fears",
    "url": "https://www.chosun.com/english/market-money-en/2026/07/29/6FEUZWQT5BG3HMJ3G2RZPHROGM/",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-29T04:29:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49075171",
    "domain": "AI 算力 / 半导体",
    "title": "Sam Altman says we are in the singularity: 'This is the moment'",
    "url": "https://www.businessinsider.com/sam-altman-openai-the-singularity-agi-prediction-anthropic-nvidia-2026-7",
    "source": "doener",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-27T20:35:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:49069995",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia investing to 10x SSI compute in the next 12 months",
    "url": "https://twitter.com/ssi/status/2081732119194394763",
    "source": "primaprashant",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-07-27T14:11:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49111237",
    "domain": "大厂 AI 动态",
    "title": "Gemini Robotics 2 brings whole body intelligence to robots",
    "url": "https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/",
    "source": "ai2027",
    "platform": "hackernews",
    "points": 526,
    "published_at": "2026-07-30T15:15:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49096188",
    "domain": "大厂 AI 动态",
    "title": "Document-borne AI worms can self-propagate through Copilot for Word",
    "url": "https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/",
    "source": "Canopy9560",
    "platform": "hackernews",
    "points": 380,
    "published_at": "2026-07-29T11:44:33+00:00",
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
    "id": "hn:48936451",
    "domain": "大厂 AI 动态",
    "title": "NotebookLM is now Gemini Notebook",
    "url": "https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/",
    "source": "xnx",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-07-16T16:08:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48925271",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://turntrout.com/why-i-left-google-deepmind",
    "source": "apsec112",
    "platform": "hackernews",
    "points": 390,
    "published_at": "2026-07-15T18:40:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49067285",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://www.lesswrong.com/posts/iKm2FhpWkuuBojm82/why-i-left-google-deepmind",
    "source": "eatitraw",
    "platform": "hackernews",
    "points": 197,
    "published_at": "2026-07-27T09:56:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48965880",
    "domain": "大厂 AI 动态",
    "title": "Ollama: All Aboard Open Models",
    "url": "https://ollama.com/blog/all-aboard-open-models",
    "source": "inferhaven",
    "platform": "hackernews",
    "points": 138,
    "published_at": "2026-07-19T07:59:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48998606",
    "domain": "大厂 AI 动态",
    "title": "Gemini last models: temperature, top_p, and top_k are deprecated and ignored",
    "url": "https://ai.google.dev/gemini-api/docs/latest-model",
    "source": "greatgib",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-07-21T21:27:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49096841",
    "domain": "大厂 AI 动态",
    "title": "Google DeepMind dismantles AlphaFold team",
    "url": "https://www.ft.com/content/61b2953d-ee0d-45de-af6e-a9c1cf524b33",
    "source": "ainch",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-07-29T12:50:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48864507",
    "domain": "大厂 AI 动态",
    "title": "Please don't discontinue Gemini 2.5 Flash",
    "url": "https://discuss.ai.google.dev/t/please-dont-discontinue-gemini-2-5-flash/174246",
    "source": "NickDob",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-07-10T20:00:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:48959297",
    "domain": "大厂 AI 动态",
    "title": "Our Approach to Bioresilience: Isomorphic Labs and Google DeepMind",
    "url": "https://deepmind.google/blog/our-approach-to-bioresilience/",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 83,
    "published_at": "2026-07-18T16:02:45+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/973552/apple-ceo-tim-cook-icloud-plus-ai",
    "domain": "大厂 AI 动态",
    "title": "Tim Cook hints at iCloud Plus tier for AI power users",
    "url": "https://www.theverge.com/tech/973552/apple-ceo-tim-cook-icloud-plus-ai",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T22:29:45+00:00",
    "summary": "Apple may allow users to pay to increase their AI usage limits. During an earnings call on Thursday, Apple CEO Tim Cook said that he believes people will want to use Apple Intelligence and the upcomin"
  },
  {
    "id": "rss:https://www.theverge.com/games/973520/xbox-ceo-memo-one-year-growth",
    "domain": "大厂 AI 动态",
    "title": "Xbox CEO lays out priorities in memo after major &#8216;reset&#8217;",
    "url": "https://www.theverge.com/games/973520/xbox-ceo-memo-one-year-growth",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T22:10:13+00:00",
    "summary": "After a massive Xbox \"reset\" that laid off thousands of employees and spun off four studios, Xbox CEO Asha Sharma wants to get Xbox back to growth. In a memo obtained by The Verge, Sharma told staff b"
  },
  {
    "id": "rss:https://www.theverge.com/tech/973430/apple-q3-2026-earnings",
    "domain": "大厂 AI 动态",
    "title": "Apple&#8217;s iPhone and Mac sales keep growing despite RAM shortages",
    "url": "https://www.theverge.com/tech/973430/apple-q3-2026-earnings",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T20:49:32+00:00",
    "summary": "Apple's iPhone and Mac sales are on the rise even as a global memory shortage squeezes device makers. In its third-quarter earnings report released on Thursday, Apple revealed that iPhone sales jumped"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/973467/ai-bet-situational-awareness-oops-stonks",
    "domain": "大厂 AI 动态",
    "title": "The loss of Situational Awareness",
    "url": "https://www.theverge.com/ai-artificial-intelligence/973467/ai-bet-situational-awareness-oops-stonks",
    "source": "Elizabeth Lopatto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T20:46:25+00:00",
    "summary": "I am not by any means an expert at finance but I think I do now have some advice for people who are: Do not name your hedge fund anything that will be hilarious if it blows up. Don't use a name like \""
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/973211/costco-galaxy-watch-9-preorder-costco-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Samsung’s Galaxy Watch 9 is $40 off at Costco and comes with over $50 in freebies",
    "url": "https://www.theverge.com/gadgets/973211/costco-galaxy-watch-9-preorder-costco-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T19:00:00+00:00",
    "summary": "The Galaxy Watch 9 launches on August 7th, and not only does Costco have the best preorder incentives we’ve seen so far, the watch is also discounted. The deal includes the 40mm Watch 9 in cream or gr"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/973384/linkedin-seems-like-ai-slop-button",
    "domain": "大厂 AI 动态",
    "title": "LinkedIn actually adds a ‘seems like AI slop’ button",
    "url": "https://www.theverge.com/ai-artificial-intelligence/973384/linkedin-seems-like-ai-slop-button",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T18:43:26+00:00",
    "summary": "A lot of content on LinkedIn might seem like AI slop, and now, you'll be able to report those posts. As part of a series of updates to reduce the volume of AI slop on the platform, LinkedIn is introdu"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/973266/govee-table-lamp-classic-back-to-school-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Govee&#8217;s portable smart lamp is down to one of its best prices to date",
    "url": "https://www.theverge.com/gadgets/973266/govee-table-lamp-classic-back-to-school-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T18:01:26+00:00",
    "summary": "Buying multiple lamps for different rooms can get expensive. Govee’s rechargeable Table Lamp Classic gives you one lamp you can use throughout your home instead of getting one for every room, and righ"
  },
  {
    "id": "rss:https://www.theverge.com/science/973314/nasa-curiosity-rover-mars-polygons",
    "domain": "大厂 AI 动态",
    "title": "NASA’s Curiosity rover found a ‘sea of polygons’ on Mars",
    "url": "https://www.theverge.com/science/973314/nasa-curiosity-rover-mars-polygons",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T17:20:06+00:00",
    "summary": "The latest discovery from NASA's Curiosity Mars rover is a field of honeycomb-shaped polygons covering a Martian valley called Valle Grande. As Gizmodo reports, Curiosity has snapped pictures of the u"
  },
  {
    "id": "rss:https://www.theverge.com/tech/973276/google-deepmind-gemini-robotics-2-whole-body",
    "domain": "大厂 AI 动态",
    "title": "Google DeepMind’s new AI model can control a robot’s entire body",
    "url": "https://www.theverge.com/tech/973276/google-deepmind-gemini-robotics-2-whole-body",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T17:18:45+00:00",
    "summary": "Google DeepMind says the latest version of its Gemini Robotics AI model can \"control entire humanoid robots.\" While the previous model focused on controlling a humanoid robot's upper body, Gemini Robo"
  },
  {
    "id": "rss:https://www.theverge.com/policy/973289/abc-fcc-early-license-renewal-opposition",
    "domain": "大厂 AI 动态",
    "title": "ABC demands FCC drop its ‘punitive’ early license renewal of its stations",
    "url": "https://www.theverge.com/policy/973289/abc-fcc-early-license-renewal-opposition",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T17:08:14+00:00",
    "summary": "ABC filed its formal opposition to the Federal Communications Commission's effort to force it to submit to an early renewal of its broadcast station licenses, calling it an effort to chill the speech "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/anthropic-says-its-own-ai-models-breached-three-companies-during-security-tests/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic says its own AI models breached three companies during security tests",
    "url": "https://techcrunch.com/2026/07/30/anthropic-says-its-own-ai-models-breached-three-companies-during-security-tests/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T01:06:54+00:00",
    "summary": "After OpenAI's models broke into Hugging Face, Anthropic checked its own history and found three similar incidents"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/apple-stockpiles-inventory-as-it-braces-for-significant-supply-constraints/",
    "domain": "大厂 AI 动态",
    "title": "Apple stockpiles inventory as it braces for ‘significant supply constraints’",
    "url": "https://techcrunch.com/2026/07/30/apple-stockpiles-inventory-as-it-braces-for-significant-supply-constraints/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T23:28:05+00:00",
    "summary": "Apple is worried enough about supply shortages that it reported about $11.1 billion in inventory, which is almost double the $5.7 billion it reported last September."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/ai-hedge-fund-situational-awareness-may-have-sold-its-public-portfolio-but-it-still-has-its-anthropic-shares/",
    "domain": "大厂 AI 动态",
    "title": "AI hedge fund Situational Awareness may have sold its public portfolio, but it still has its Anthropic shares",
    "url": "https://techcrunch.com/2026/07/30/ai-hedge-fund-situational-awareness-may-have-sold-its-public-portfolio-but-it-still-has-its-anthropic-shares/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T23:25:58+00:00",
    "summary": "The former OpenAI researcher’s fund was forced to unwind public equities after leveraged public bets plummeted. But he still has cards to play."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/reddit-reports-a-solid-quarter-but-shows-signs-of-ais-impact/",
    "domain": "大厂 AI 动态",
    "title": "Reddit reports a solid quarter but shows signs of AI’s impact",
    "url": "https://techcrunch.com/2026/07/30/reddit-reports-a-solid-quarter-but-shows-signs-of-ais-impact/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T23:08:58+00:00",
    "summary": "Reddit's financial situation is looking good but uncertainty about its relationship to Google and the new AI-ified web are stirring market concerns."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/investors-love-ai-as-long-as-youre-a-cloud-host/",
    "domain": "大厂 AI 动态",
    "title": "Investors love AI, as long as you’re a cloud host",
    "url": "https://techcrunch.com/2026/07/30/investors-love-ai-as-long-as-youre-a-cloud-host/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T22:41:41+00:00",
    "summary": "Amazon isn't slowing down on data center spending — but investors don't seem to mind."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/apple-says-gaming-slowdown-and-app-store-changes-hurt-services-growth/",
    "domain": "大厂 AI 动态",
    "title": "Apple says gaming slowdown and App Store changes hurt services growth",
    "url": "https://techcrunch.com/2026/07/30/apple-says-gaming-slowdown-and-app-store-changes-hurt-services-growth/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T22:37:06+00:00",
    "summary": "Apple said a slowdown in mobile gaming and changes to the App Store’s business model — including court-ordered payment rule changes in the U.S. — weighed on its services business, even as the company "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/judge-says-trump-admin-still-lacks-evidence-for-anthropic-supply-chain-risk-label/",
    "domain": "大厂 AI 动态",
    "title": "Judge says Trump admin still lacks evidence for Anthropic ‘supply-chain risk’ label",
    "url": "https://techcrunch.com/2026/07/30/judge-says-trump-admin-still-lacks-evidence-for-anthropic-supply-chain-risk-label/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T20:26:38+00:00",
    "summary": "A federal judge said the Trump administration has not presented enough evidence to justify labeling Anthropic a supply-chain risk, casting doubt on the government's ban on its AI technology."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/carecloud-begins-to-notify-hundreds-of-thousands-after-hackers-stole-medical-records/",
    "domain": "大厂 AI 动态",
    "title": "CareCloud begins to notify hundreds of thousands after hackers stole medical records",
    "url": "https://techcrunch.com/2026/07/30/carecloud-begins-to-notify-hundreds-of-thousands-after-hackers-stole-medical-records/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T20:13:12+00:00",
    "summary": "The health tech data giant, which handles vast amounts of patients' medical data, said hackers struck one of its protected health data stores."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/friend-the-lonely-ai-wearable-returns-with-a-new-voice-and-a-much-bigger-price-tag/",
    "domain": "大厂 AI 动态",
    "title": "Friend, the lonely AI wearable, returns with a new voice and a much bigger price tag",
    "url": "https://techcrunch.com/2026/07/30/friend-the-lonely-ai-wearable-returns-with-a-new-voice-and-a-much-bigger-price-tag/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T19:44:16+00:00",
    "summary": "Friend, the AI wearable, can now talk to its users — for an enhanced price."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/google-says-it-fixed-more-chrome-bugs-in-june-than-over-the-past-two-years-thanks-to-ai/",
    "domain": "大厂 AI 动态",
    "title": "Google says it fixed more Chrome bugs in June than over the past two years, thanks to AI",
    "url": "https://techcrunch.com/2026/07/30/google-says-it-fixed-more-chrome-bugs-in-june-than-over-the-past-two-years-thanks-to-ai/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T18:57:58+00:00",
    "summary": "As experts have warned for the last two years, some companies — like Microsoft and now Google — are finding and patching an exponential number of bugs in their products, thanks to the use of LLMs and "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/florida-plans-to-build-air-taxi-pads-using-200m-intended-for-ev-chargers/",
    "domain": "大厂 AI 动态",
    "title": "Florida plans to build air taxi pads using $200M intended for EV chargers",
    "url": "https://techcrunch.com/2026/07/30/florida-plans-to-build-air-taxi-pads-using-200m-intended-for-ev-chargers/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T18:38:12+00:00",
    "summary": "Florida wants to use federal EV charger funds to build an air taxi network connecting golf courses, luxury apartment buildings, and airports."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/linkedin-adds-a-button-to-report-ai-generated-slop/",
    "domain": "大厂 AI 动态",
    "title": "LinkedIn adds a button to report AI-generated ‘slop’",
    "url": "https://techcrunch.com/2026/07/30/linkedin-adds-a-button-to-report-ai-generated-slop/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T18:05:21+00:00",
    "summary": "LinkedIn is introducing new ways to reduce low-quality AI-generated posts, including a “seems like AI slop” reporting option. It's also replacing its own AI writing feature with a proofreading tool."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/synthetic-user-startup-simile-raises-200m-at-2b-valuation-5-months-after-100m-series-a/",
    "domain": "大厂 AI 动态",
    "title": "Synthetic-user startup Simile raises $200M at $2B valuation 5 months after $100M Series A",
    "url": "https://techcrunch.com/2026/07/30/synthetic-user-startup-simile-raises-200m-at-2b-valuation-5-months-after-100m-series-a/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T17:50:11+00:00",
    "summary": "Add another member to the fast-and-furious AI unicorn club: Simile."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/spotify-launches-user-notes-to-let-users-add-memories-to-songs/",
    "domain": "大厂 AI 动态",
    "title": "Spotify launches ‘User Notes’ to let users add memories to songs",
    "url": "https://techcrunch.com/2026/07/30/spotify-launches-user-notes-to-let-users-add-memories-to-songs/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T17:41:25+00:00",
    "summary": "Spotify says the new feature is designed to let users add personal captions to their favorite songs, such as noting why a track was added to a playlist or when they first discovered it"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/okta-buys-ai-security-startup-permiso-source-says-for-about-200m/",
    "domain": "大厂 AI 动态",
    "title": "Okta buys AI security startup Permiso — source says for about $200M",
    "url": "https://techcrunch.com/2026/07/30/okta-buys-ai-security-startup-permiso-source-says-for-about-200m/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T16:09:42+00:00",
    "summary": "The deal gives Okta identity threat detection capabilities as enterprises seek to secure AI agents and other non-human identities across cloud environments."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/tesla-made-its-10-millionth-ev/",
    "domain": "大厂 AI 动态",
    "title": "Tesla made its 10 millionth EV",
    "url": "https://techcrunch.com/2026/07/30/tesla-made-its-10-millionth-ev/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T16:00:25+00:00",
    "summary": "The milestone means Tesla is halfway to accomplishing one of the four core product goals Elon Musk has to hit to unlock his full $1 trillion pay package."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/when-will-fusion-power-startup-commonwealth-fusion-systems-go-public/",
    "domain": "大厂 AI 动态",
    "title": "When will fusion power startup Commonwealth Fusion Systems go public?",
    "url": "https://techcrunch.com/2026/07/30/when-will-fusion-power-startup-commonwealth-fusion-systems-go-public/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T15:45:36+00:00",
    "summary": "There are fresh signs that fusion power startup Commonwealth Fusion Systems will list in the next two to three years."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/meta-says-ai-is-making-it-easier-to-build-new-apps-and-more-are-coming/",
    "domain": "大厂 AI 动态",
    "title": "Meta says AI is making it easier to build new apps — and more are coming",
    "url": "https://techcrunch.com/2026/07/30/meta-says-ai-is-making-it-easier-to-build-new-apps-and-more-are-coming/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T15:41:16+00:00",
    "summary": "Meta says AI is making it dramatically easier to build and launch new consumer apps, with CEO Mark Zuckerberg telling investors the company has more new consumer products on the way."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/netflix-lands-global-streaming-deal-for-the-walking-dead/",
    "domain": "大厂 AI 动态",
    "title": "Netflix lands global streaming deal for ‘The Walking Dead’",
    "url": "https://techcrunch.com/2026/07/30/netflix-lands-global-streaming-deal-for-the-walking-dead/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T15:27:08+00:00",
    "summary": "Netflix just signed a massive new licensing agreement worth $500 million to bring The Walking Dead Universe to international markets."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/30/nscale-buys-anyscale-as-it-seeks-to-own-more-of-the-ai-compute-stack/",
    "domain": "大厂 AI 动态",
    "title": "Nscale buys Anyscale as it seeks to own more of the AI compute stack",
    "url": "https://techcrunch.com/2026/07/30/nscale-buys-anyscale-as-it-seeks-to-own-more-of-the-ai-compute-stack/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T15:19:15+00:00",
    "summary": "British AI neocloud Nscale is buying software startup Anyscale, which helps companies scale their AI workloads across data centers and servers."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/tim-cooks-last-earnings-call-strong-iphone-sales-but-memory-costs-loom-large/",
    "domain": "大厂 AI 动态",
    "title": "Tim Cook passes the baton in Apple's Q3 2026 earnings call",
    "url": "https://arstechnica.com/gadgets/2026/07/tim-cooks-last-earnings-call-strong-iphone-sales-but-memory-costs-loom-large/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T22:05:35+00:00",
    "summary": "The iPhone and Mac sold well, but memory costs threaten further price increases."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/07/kremlin-hackers-are-exploiting-exchange-flaw-to-backdoor-unpatched-networks/",
    "domain": "大厂 AI 动态",
    "title": "Max-severity Exchange server flaw under active exploitation by Kremlin hackers",
    "url": "https://arstechnica.com/security/2026/07/kremlin-hackers-are-exploiting-exchange-flaw-to-backdoor-unpatched-networks/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T20:57:22+00:00",
    "summary": "Exploits can give persistent server access that survives credential rotation and disk re-imaging."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/trump-fccs-war-on-abc-slammed-by-both-conservatives-and-liberals/",
    "domain": "大厂 AI 动态",
    "title": "Trump FCC faces blowback in attempt to police speech on broadcast TV",
    "url": "https://arstechnica.com/tech-policy/2026/07/trump-fccs-war-on-abc-slammed-by-both-conservatives-and-liberals/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T20:48:47+00:00",
    "summary": "\"Chilling message to all broadcasters: carry speech we don’t like at your peril.\""
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/satellites-spot-new-war-damage-to-amazon-data-centers-and-saudi-oil-site/",
    "domain": "大厂 AI 动态",
    "title": "Iran struck Amazon data centers again amid widening war, satellites show",
    "url": "https://arstechnica.com/gadgets/2026/07/satellites-spot-new-war-damage-to-amazon-data-centers-and-saudi-oil-site/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T20:45:39+00:00",
    "summary": "Satellites show burn scars and fires at AWS data centers and Saudi oil refinery."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/07/the-disc-is-not-the-game-physical-releases-increasingly-require-extra-downloads/",
    "domain": "大厂 AI 动态",
    "title": "Just because a game is on disc doesn’t mean it will work in the future",
    "url": "https://arstechnica.com/gaming/2026/07/the-disc-is-not-the-game-physical-releases-increasingly-require-extra-downloads/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T20:12:50+00:00",
    "summary": "DoesItPlay tracks the many \"physical\" games that don't work without the Internet."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/chrome-may-get-faster-updates-with-no-restart-required/",
    "domain": "大厂 AI 动态",
    "title": "Chrome may get faster updates with no restart required",
    "url": "https://arstechnica.com/ai/2026/07/chrome-may-get-faster-updates-with-no-restart-required/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T19:26:56+00:00",
    "summary": "The last two versions of Chrome have included more patches than the previous 23 combined."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/google-reveals-gemini-robotics-2-0-promising-improved-dexterity-and-safety/",
    "domain": "大厂 AI 动态",
    "title": "Google reveals Gemini Robotics 2.0, promising improved dexterity and safety",
    "url": "https://arstechnica.com/ai/2026/07/google-reveals-gemini-robotics-2-0-promising-improved-dexterity-and-safety/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T17:58:02+00:00",
    "summary": "Gemini Robotics 2 includes three models, but only one is publicly available right now."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/space-force-backed-mission-does-its-best-impression-of-top-gun-in-orbit/",
    "domain": "大厂 AI 动态",
    "title": "Space Force-backed mission does its best impression of Top Gun in orbit",
    "url": "https://arstechnica.com/space/2026/07/space-force-backed-mission-does-its-best-impression-of-top-gun-in-orbit/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T17:35:57+00:00",
    "summary": "\"Dogfighting in space doesn’t quite have the drama of an aerial dogfight.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/if-a-quantum-computer-outperforms-normal-ones-can-you-tell-if-its-right/",
    "domain": "大厂 AI 动态",
    "title": "Quantum computers outperform classical ones, with results you can trust",
    "url": "https://arstechnica.com/science/2026/07/if-a-quantum-computer-outperforms-normal-ones-can-you-tell-if-its-right/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T15:59:37+00:00",
    "summary": "Three approaches to the issue of quantum results that can't be verified classically."
  },
  {
    "id": "hn:49057574",
    "domain": "股票",
    "title": "Google Discloses $94.1B in SpaceX Stock, Marking 6% Stake",
    "url": "https://www.wsj.com/tech/google-discloses-94-1-billion-in-spacex-stock-marking-6-stake-91655d7c",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 341,
    "published_at": "2026-07-26T12:43:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48933344",
    "domain": "股票",
    "title": "SpaceX stock erases all its gains and slides below IPO price in intraday trading",
    "url": "https://www.latimes.com/business/story/2026-07-16/spacex-stock-erases-gains-slides-below-ipo-price-in-intraday-trading",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 314,
    "published_at": "2026-07-16T12:02:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48948435",
    "domain": "股票",
    "title": "Short sellers notch $8.7B profit as SpaceX shares dip to IPO price",
    "url": "https://www.reuters.com/business/media-telecom/short-sellers-rack-up-87-bln-profit-spacex-slips-below-ipo-price-ortex-2026-07-16/",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 168,
    "published_at": "2026-07-17T15:17:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49111879",
    "domain": "股票",
    "title": "Citadel Buys Situational Awareness's Stock Portfolio After Big Losses in AI",
    "url": "https://www.wsj.com/finance/citadel-buys-situational-awarenesss-stock-portfolio-after-big-losses-in-ai-5117159b",
    "source": "mudil",
    "platform": "hackernews",
    "points": 51,
    "published_at": "2026-07-30T16:00:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49092549",
    "domain": "股票",
    "title": "Chip stocks slide in US and Asia as AI jitters rattle investors",
    "url": "https://www.bbc.com/news/articles/cly8zng43npo",
    "source": "yogthos",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-07-29T01:56:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:49115139",
    "domain": "股票",
    "title": "Microsoft's $450B Jump Is Biggest in Stock Market History",
    "url": "https://www.bloomberg.com/news/articles/2026-07-30/microsoft-eyes-history-with-490-billion-pop-in-market-value",
    "source": "signatoremo",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-30T20:12:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49114131",
    "domain": "股票",
    "title": "Citadel buys most of Situational's stock holdings after AI share rout",
    "url": "https://www.reuters.com/technology/citadel-buys-most-situationals-stock-holdings-after-ai-share-rout-sources-say-2026-07-30/",
    "source": "paulpauper",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-30T18:54:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:49095568",
    "domain": "股票",
    "title": "Korean Stocks Plunge 16% in Two-Day Burst of Retail Selling",
    "url": "https://www.bloomberg.com/news/articles/2026-07-29/korean-stocks-tumble-a-second-day-as-sk-hynix-results-disappoint",
    "source": "emsidisii",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-29T10:25:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49110556",
    "domain": "股票",
    "title": "Leopold Aschenbrenner unwinds all public stock positions after steep losses",
    "url": "https://www.cnbc.com/2026/07/30/leopold-aschenbrenners-hedge-fund-is-facing-steep-ai-losses.html",
    "source": "scrlk",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-30T14:29:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49087537",
    "domain": "股票",
    "title": "Chip stocks tumble as AI sell-off deepens",
    "url": "https://www.ft.com/content/f8c03b5b-e194-4236-82c3-389b6f5dd7ae",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-07-28T17:54:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:48938001",
    "domain": "股票",
    "title": "SPCX is now Wall Street's most shorted new stock",
    "url": "https://invezz.com/news/2026/07/16/the-worlds-most-valuable-ipo-spcx-is-now-wall-streets-most-shorted-new-stock/",
    "source": "lbrito",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-07-16T18:03:56+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3778406",
    "domain": "股票",
    "title": "阿迪达斯季度收入创新高，世界杯投入未能兑现利润期待",
    "url": "https://wallstreetcn.com/articles/3778406",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T05:54:00+00:00",
    "summary": "阿迪达斯在世界杯期间卖出了创纪录的产品，却没有交出市场期待的利润表现。\n7月30日，阿迪达斯披露20..."
  },
  {
    "id": "wscn:3778404",
    "domain": "股票",
    "title": "亚马逊财报点评：AWS收入锚定“万亿美元”，但自由现金流正式转负",
    "url": "https://wallstreetcn.com/premium/articles/3778404?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T05:53:59+00:00",
    "summary": "亚马逊CEO Andy Jassy在电话会上首次明确给出AI基建投资的ROI量化指引——约3年即可实现收支平衡，并豪言\"AWS将成为年收入1万亿美元的业务\"。"
  },
  {
    "id": "wscn:3778401",
    "domain": "股票",
    "title": "CPE源峰签约收购猛犸象，能否复制始祖鸟的中国故事？",
    "url": "https://wallstreetcn.com/articles/3778401",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T05:08:34+00:00",
    "summary": "又一个国际高端户外品牌将进入中国资本版图。\n中国私募股权机构CPE源峰已与欧洲私募股权机构Jacob..."
  },
  {
    "id": "wscn:3778391",
    "domain": "股票",
    "title": "上调资本开支预期依旧大涨，亚马逊这份财报意味着什么？",
    "url": "https://wallstreetcn.com/articles/3778391",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T05:00:27+00:00",
    "summary": "亚马逊上调资本开支后，CEO Andy Jassy表示今明两年容量仍无法满足全部需求。巴克莱认为该表态有力反驳了AI基础设施过度建设的担忧，并释放出2028年需求能见度已超寻常的强烈信号，消息利好美股数据中心基础设施板块。"
  },
  {
    "id": "wscn:3778399",
    "domain": "股票",
    "title": "月末好戏不断！日元飙升 科技股满血复活？",
    "url": "https://wallstreetcn.com/articles/3778399",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:43:23+00:00",
    "summary": "市场在7月尾声迎来了戏剧性的反转。\n日本央行的疑似干预帮助日元大幅走强从而脱离了40年低点。微软财报..."
  },
  {
    "id": "wscn:3778386",
    "domain": "股票",
    "title": "创业板大涨5%，算力硬件、芯片半导体爆发，长鑫市值破4万亿，港股AI大模型股暴涨、智谱涨20%",
    "url": "https://wallstreetcn.com/articles/3778386",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:17:14+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市约4500股飘红，上午半天成交1.8万亿。量能明显放大，沪深两市半日成交额1.79万亿，较上个交易日放量超3300亿。板块方面，半导体、算力硬件产业链大幅反弹，CPO、存储器方向领涨；AI应用概念股表现活跃，锂电池、商业航天、机器人题材走强；银行、白酒、煤炭板块走弱。"
  },
  {
    "id": "wscn:3778393",
    "domain": "股票",
    "title": "谁将为AI超级周期买单？",
    "url": "https://wallstreetcn.com/articles/3778393",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:07:29+00:00",
    "summary": "中信建投报告指出，AI超级周期的资金本质上由全球长期储蓄体系买单。科技巨头资本开支预计今年达7800亿美元，已超出自身现金流，融资缺口约1300亿美元。最大脆弱点在于AI云服务提供商，如CoreWeave 2026年固定支付墙高达经营现金流的149%，持续再融资是生存前提，2026至2027年是最危险的流动性风险节点。"
  },
  {
    "id": "wscn:3778293",
    "domain": "股票",
    "title": "不只可远观，更能亲手造：在L'ÉCOLE触摸两千年前的金工温度",
    "url": "https://wallstreetcn.com/articles/3778293",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T03:49:02+00:00",
    "summary": "继巴黎首展、首尔巡展之后，“金手匠艺：铁器时代的金饰重生”终于来到上海。\n由Van Cleef &..."
  },
  {
    "id": "wscn:3778398",
    "domain": "股票",
    "title": "袁记云饺前五月净利增长近1.8倍，线上订单量已过半",
    "url": "https://wallstreetcn.com/articles/3778398",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T03:45:59+00:00",
    "summary": "袁记云饺交出了一份收入、利润、开店和单店经营同步回升的最新成绩单。\n7月30日，袁记云饺母公司袁记食..."
  },
  {
    "id": "wscn:3778397",
    "domain": "股票",
    "title": "欧莱雅2026年上半年营收237.7亿欧元，利润率稳步爬升",
    "url": "https://wallstreetcn.com/articles/3778397",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T03:45:03+00:00",
    "summary": "中国市场成北亚区复苏关键引擎。"
  },
  {
    "id": "wscn:3778395",
    "domain": "股票",
    "title": "日本央行按兵不动维持利率1%，一票反对并主张加息，通胀存在超越2%的风险",
    "url": "https://wallstreetcn.com/articles/3778395",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T03:39:46+00:00",
    "summary": "日本央行维持利率1%不变，但内部现罕见裂痕——委员高田创独排众议，力主继续加息。央行上调经济增长预测，将风险评估从\"偏向下行\"调整为\"基本平衡\"，并罕见点名日元贬值加剧通胀压力。市场押注最快10月再度加息，植田和男发布会措辞将成关键风向标。"
  },
  {
    "id": "wscn:3778390",
    "domain": "股票",
    "title": "韩国拟向主权财富基金注资140亿美元，押注AI与数据中心",
    "url": "https://wallstreetcn.com/articles/3778390",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T02:29:02+00:00",
    "summary": "根据政府声明，新设专项账户将设于KIC现有架构之内，初始规模不低于20万亿韩元，资金来源包括政策性银行等公共机构的股权出资。此次调整最具标志性意义的变化在于，KIC的投资授权将首次延伸至国内资产。"
  },
  {
    "id": "wscn:3778389",
    "domain": "股票",
    "title": "不建数据中心的苹果，正在为AI数据中心买单",
    "url": "https://wallstreetcn.com/articles/3778389",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T02:28:59+00:00",
    "summary": "苹果史上最强六月季报——营收1094亿、毛利率首破50%，盘后股价却暴跌6%，市值一夜蒸发超3000亿美元。真正的危机藏在供应链深处：苹果不建AI数据中心，但AI数据中心的成本正通过芯片和存储两个管道，传导到每一台iPhone和Mac上，悄无声息地吃掉苹果的利润率，Q4毛利率指引骤降至47%-48%。"
  },
  {
    "id": "wscn:3778375",
    "domain": "股票",
    "title": "沃什“暗示”改通胀指标，市场“嗅到不好的味道”",
    "url": "https://wallstreetcn.com/articles/3778375",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T02:16:11+00:00",
    "summary": "美联储主席沃什此前表示，评估通胀时将参考比PCE更广泛的指标，并暗示明年1月后可能调整通胀框架。此言论引发市场震荡，30年期盈亏平衡通胀率创2024年以来最大单日涨幅。经济学家质疑工作组或为重新定义通胀挑战提供掩护，而可替代PCE的指标选项极为有限。"
  },
  {
    "id": "wscn:3778392",
    "domain": "股票",
    "title": "下一个十年，你的资产配置锚在哪里？",
    "url": "https://wallstreetcn.com/articles/3778392",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T02:08:51+00:00",
    "summary": "2026年以来，科创板块走势强劲，科创50过去半年（2026.1.9-2026.7.8）涨幅为38...."
  },
  {
    "id": "wscn:3778260",
    "domain": "股票",
    "title": "韩股连续两日熔断之后：去杠杆是否已接近尾声？",
    "url": "https://wallstreetcn.com/premium/articles/3778260?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T01:57:38+00:00",
    "summary": "韩股去杠杆接近尾声，被动抛售高峰已过，但散户信心重创，市场震荡寻底，反转有待业绩确认。"
  },
  {
    "id": "wscn:3778385",
    "domain": "股票",
    "title": "空谈无益！两次发布会后，华尔街开始质疑沃什“信誉”",
    "url": "https://wallstreetcn.com/articles/3778385",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T01:56:05+00:00",
    "summary": "美联储主席沃什弃用前瞻指引，华尔街正以最直接的方式发出警告，30年期美债收益率飙升至2007年来高点5.24%，摩根大通、摩根士丹利、美银措辞严厉的研报直指“信誉危机”。连续按兵不动却无法自圆其说，市场已开始走上那条\"更艰难的路\"。"
  },
  {
    "id": "wscn:3777967",
    "domain": "股票",
    "title": "黄金4000美元震荡月余：央行与ETF买盘何时回归？",
    "url": "https://wallstreetcn.com/premium/articles/3777967?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T01:50:44+00:00",
    "summary": "黄金围绕4000美元震荡磨底，央行托底但ETF资金未回归，紧缩预期结束与资金共振开启新行情。"
  },
  {
    "id": "wscn:3778387",
    "domain": "股票",
    "title": "中国7月制造业PMI降至49.2，高技术制造业逆势扩张，非制造业商务活动指数降至49",
    "url": "https://wallstreetcn.com/articles/3778387",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T01:45:46+00:00",
    "summary": "数据显示，7月份，装备制造业和高技术制造业PMI分别为51.4%和53.3%，明显高于制造业总体，保持较快扩张，带动制造业发展向新向优。与此同时，文旅行业受暑期消费带动明显回暖，在一定程度上对冲了建筑业和批发业的拖累。"
  },
  {
    "id": "wscn:3778343",
    "domain": "股票",
    "title": "宇树科技：8月10日打新，预计上半年营业收入10.52亿元至11.28亿元",
    "url": "https://wallstreetcn.com/articles/3778343",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T01:18:29+00:00",
    "summary": "7月30日，宇树科技公告称，公司首次公开发行股票并在科创板上市的申请已获上交所上市审核委员会审议通过，并获中国证监会同意注册。初步询价日为2026年8月5日，网下、网上申购日为8月10日，缴款日为8月12日。"
  },
  {
    "id": "hn:48950580",
    "domain": "股票",
    "title": "SpaceX stock drops to a new low and loses $1T in value in a month",
    "url": "https://www.businessinsider.com/spacex-stock-drops-new-low-ipo-price-starship-launch-scrubbed-2026-7",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-07-17T18:26:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:49081705",
    "domain": "股票",
    "title": "AI sell-off intensifies as investors ditch chip stocks",
    "url": "https://www.theguardian.com/business/2026/jul/28/ai-sell-off-chip-stocks-sk-hynix-samsung",
    "source": "lilerjee",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-28T10:08:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:49091512",
    "domain": "股票",
    "title": "Apple becomes second $5T company as investors flee AI stocks",
    "url": "https://www.theguardian.com/technology/2026/jul/28/apple-second-ever-5tn-company-as-investors-flee-ai-stocks",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-28T23:41:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:48946872",
    "domain": "股票",
    "title": "US Corporate Insiders Are Selling Stocks at a Near Record Pace",
    "url": "https://www.bloomberg.com/news/articles/2026-07-17/us-corporate-insiders-are-selling-stocks-at-a-near-record-pace",
    "source": "pimienta",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-07-17T13:00:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48958985",
    "domain": "股票",
    "title": "Traders are increasingly betting against SpaceX just weeks after IPO",
    "url": "https://www.ft.com/content/2b96703d-440b-46db-8d86-9fff9ecc59d5",
    "source": "ethanhawksley",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-07-18T15:26:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48984021",
    "domain": "股票",
    "title": "Mark Cuban: fight inequality by giving all workers company stock",
    "url": "https://fortune.com/2026/07/20/mark-cuban-income-inequality-company-stock-spacex-ipo-cost-plus-drugs/",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-07-20T19:52:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48974426",
    "domain": "股票",
    "title": "Big tech needs to justify AI spending as investors dump stocks",
    "url": "https://www.bloomberg.com/news/articles/2026-07-19/big-tech-needs-to-justify-ai-spending-as-investors-dump-stocks",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-07-20T04:41:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49012630",
    "domain": "股票",
    "title": "Alphabet Announces Second Quarter 2026 Results [pdf]",
    "url": "https://s206.q4cdn.com/479360582/files/doc_financials/2026/q2/2026q2-alphabet-earnings-release.pdf",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-07-22T20:04:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49033778",
    "domain": "股票",
    "title": "Reality Bites Elon Musk and His Tesla, SpaceX Believers",
    "url": "https://www.wsj.com/finance/stocks/reality-bites-elon-musk-and-his-tesla-spacex-believers-1b639591",
    "source": "doener",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-24T10:59:51+00:00",
    "summary": ""
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
    "id": "hn:48923343",
    "domain": "股票",
    "title": "SpaceX stock sinks below $135 IPO price for the first time",
    "url": "https://www.cnbc.com/2026/07/15/spacex-spcx-stock-ipo-price.html",
    "source": "abduhl",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-07-15T16:30:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48967807",
    "domain": "股票",
    "title": "Claude Code skill for searching royalty-free stock photos via the Pexels API",
    "url": "https://github.com/amalshehu/pexels-skill",
    "source": "amalshehu",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-19T12:55:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:49012394",
    "domain": "股票",
    "title": "We got California to intervene about OpenAI's corporate switch from nonprofit",
    "url": "https://fortune.com/2026/07/22/openai-foundation-class-n-stock-board-control-ipo/",
    "source": "SLHamlet",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-22T19:46:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48947500",
    "domain": "股票",
    "title": "A.I. Is Running on Borrowed Money",
    "url": "https://www.nytimes.com/2026/07/17/business/ai-spending-oracle-stocks-bonds.html",
    "source": "ripe",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-17T14:01:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48962049",
    "domain": "股票",
    "title": "Elon Musk Runs from Interview at Last Minute as SpaceX Stock Crashed [video]",
    "url": "https://www.youtube.com/shorts/TFpF7ZzHc3w",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-18T20:30:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48996223",
    "domain": "股票",
    "title": "The AI Bubble Is No Ordinary Bubble",
    "url": "https://www.theatlantic.com/ideas/2026/07/ai-economy-stock-market/688004/",
    "source": "gereshes",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-21T18:31:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48899454",
    "domain": "股票",
    "title": "$65K to work at Anthropic? Debate ensues amid IPO wave",
    "url": "https://missionlocal.org/2026/07/anthropic-sf-affordability-ipo-housing-evictions-rent/",
    "source": "gcheong",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-07-13T21:56:52+00:00",
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
    "id": "hn:48889982",
    "domain": "股票",
    "title": "Xbox CEO Asha Sharma, who laid off 3,200 employees, to lead task force on jobs",
    "url": "https://www.pcgamer.com/gaming-industry/us-federal-reserve-taps-xbox-ceo-asha-sharma-who-just-laid-off-3-200-employees-to-lead-task-force-on-jobs/",
    "source": "robtherobber",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-07-13T09:27:08+00:00",
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
    "id": "hn:48915953",
    "domain": "金融",
    "title": "Stripe and Advent have made a joint offer to acquire PayPal – sources",
    "url": "https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/",
    "source": "rvz",
    "platform": "hackernews",
    "points": 494,
    "published_at": "2026-07-15T03:32:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49082695",
    "domain": "金融",
    "title": "Mondragon Corporation – a federation of co-operatives",
    "url": "https://en.wikipedia.org/wiki/Mondragon_Corporation",
    "source": "brnt",
    "platform": "hackernews",
    "points": 174,
    "published_at": "2026-07-28T12:19:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49118696",
    "domain": "金融",
    "title": "The bond market isn't buying what Fed Chair Warsh is selling",
    "url": "https://www.reuters.com/commentary/reuters-open-interest/bond-market-isnt-buying-what-fed-chair-warsh-is-selling-2026-07-30/",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 107,
    "published_at": "2026-07-31T03:32:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48878126",
    "domain": "金融",
    "title": "Under federal rule, colleges must leave grads better off or lose financial aid",
    "url": "https://www.npr.org/2026/06/30/nx-s1-5835631/turner-camhi-do-no-harm-college-loans",
    "source": "nradov",
    "platform": "hackernews",
    "points": 198,
    "published_at": "2026-07-12T04:00:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:49046525",
    "domain": "金融",
    "title": "The Fedora 45 Sausage Factory",
    "url": "https://supakeen.com/weblog/the-fedora-45-sausage-factory/",
    "source": "6581",
    "platform": "hackernews",
    "points": 156,
    "published_at": "2026-07-25T11:04:57+00:00",
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
    "id": "hn:49097833",
    "domain": "金融",
    "title": "Show HN: The Federalist Papers, typeset as the 1787 newspapers they ran in",
    "url": "https://federalistreader.org/",
    "source": "vhwalke",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-07-29T14:13:54+00:00",
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
    "id": "hn:49082706",
    "domain": "金融",
    "title": "AI revenues are growing fast, but not fast enough",
    "url": "https://www.economist.com/finance-and-economics/2026/07/28/ai-revenues-are-growing-fast-but-not-fast-enough",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-07-28T12:19:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49114620",
    "domain": "金融",
    "title": "'Talk Is Cheap': Wall Street Delivers Harsh Verdict on Warsh Fed",
    "url": "https://www.bloomberg.com/news/articles/2026-07-30/-talk-is-cheap-wall-street-delivers-harsh-verdict-on-warsh-fed",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-30T19:33:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:49100970",
    "domain": "金融",
    "title": "Trump administration Is Repurposing Federal Land for A.I. Data Centers",
    "url": "https://www.nytimes.com/2026/07/29/climate/trump-federal-data-centers.html",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-29T18:09:42+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27461",
    "domain": "金融",
    "title": "Are Three Matrices All You Need To Beat the Market? Observable Matrix Dynamics for Portfolio Optimization",
    "url": "https://arxiv.org/abs/2607.27461",
    "source": "Igor Halperin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.27461v1 Announce Type: new Abstract: We present a simple framework for dynamic portfolio management that uses nothing but daily prices, trading volumes, and market capitalizations. Its stat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27544",
    "domain": "金融",
    "title": "Lucky or Good? Outcome Noise, Effective Sample Size, and the Attribution of Skill",
    "url": "https://arxiv.org/abs/2607.27544",
    "source": "Karl T. Ulrich",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.27544v1 Announce Type: new Abstract: When do outcome records carry enough signal to support reliable inferences about skill? When they do not, what should evaluators substitute? The framewo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27548",
    "domain": "金融",
    "title": "Explaining the Macroeconomic Inertia Puzzle",
    "url": "https://arxiv.org/abs/2607.27548",
    "source": "Michael Cai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.27548v1 Announce Type: new Abstract: Benchmark macroeconomic models require additional frictions to explain the sluggish response of aggregate variables to sudden shocks or changes in polic"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27569",
    "domain": "金融",
    "title": "Consuming Values",
    "url": "https://arxiv.org/abs/2607.27569",
    "source": "Jacob Conway, Levi Boxell",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.27569v1 Announce Type: new Abstract: We study the extent to which individuals' consumption decisions are influenced by firms' stances on controversial social issues and the implied incentiv"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27584",
    "domain": "金融",
    "title": "Who heeds the call to conserve in an energy emergency? Evidence from smart thermostat data",
    "url": "https://arxiv.org/abs/2607.27584",
    "source": "Dylan Brewer, R. Jim Crozier",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.27584v1 Announce Type: new Abstract: In 2019, a fire at a natural gas plant and historically low temperatures caused an emergency shortage of natural gas in Michigan. A statewide emergency "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27588",
    "domain": "金融",
    "title": "Local Stochastic Rough Volatility: Pathwise Filtering and the Conditional Density Equation",
    "url": "https://arxiv.org/abs/2607.27588",
    "source": "Damiano Brigo, Vladimir Lucic",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.27588v1 Announce Type: new Abstract: This note studies the conditional-density equation and its pathwise transformation in local stochastic rough volatility models, with rough Heston (rHest"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27649",
    "domain": "金融",
    "title": "Multi-maturity consistency of option prices under bounded bid-ask spreads: a minimal obstruction and an exact two-date basket operator",
    "url": "https://arxiv.org/abs/2607.27649",
    "source": "Minhyeok Lee (Independent Researcher, Republic of Korea)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.27649v1 Announce Type: new Abstract: Gerhold and G\\\"ul\\\"um derived necessary calendar-vertical-basket conditions for finite call bid-ask quotes when the cash-settlement reference price lies"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27814",
    "domain": "金融",
    "title": "Pricing and Semi-static Hedging of Green Pay-as-produced Power Purchase Agreements",
    "url": "https://arxiv.org/abs/2607.27814",
    "source": "Konstantinos Chatziandreou, Sven Karbach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.27814v1 Announce Type: new Abstract: Pay-as-produced power purchase agreements (PPAs) expose buyers and sellers to the joint risk of power prices and renewable production. This paper develo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27859",
    "domain": "金融",
    "title": "ZAPs: A Reward Attribution Framework for DeFi Ecosystems with Adversarial-Robust Scoring via Parallel Anomaly Ensemble Detection",
    "url": "https://arxiv.org/abs/2607.27859",
    "source": "Girish G N, Ashutosh Sahoo, Ajay Bhat, Akshay SP, Gurukiran S, Parag Paul, Dhanashekar Kandaswamy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.27859v1 Announce Type: new Abstract: Incentive programs are central to user acquisition in decentralized finance, but many reward systems rely on raw volume, transaction count, and wallet c"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28133",
    "domain": "金融",
    "title": "AI Sycophancy and Decisions",
    "url": "https://arxiv.org/abs/2607.28133",
    "source": "John Conlon, Peter Schwardmann",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.28133v1 Announce Type: new Abstract: We examine whether sycophantic AI advice distorts decisions. Our experiment involves 1,500 participants in 30 decision environments spanning core domain"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28222",
    "domain": "金融",
    "title": "Voice AI in Firms: A Natural Field Experiment on Automated Job Interviews",
    "url": "https://arxiv.org/abs/2607.28222",
    "source": "Brian Jabarian, Luca Henkel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.28222v1 Announce Type: new Abstract: This paper studies whether AI automation can improve organizational outcomes by reducing variance when collecting information. We conducted a large-scal"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28230",
    "domain": "金融",
    "title": "Boundary-Induced Apparent Risk Aversion in Nonergodic Multiplicative Growth",
    "url": "https://arxiv.org/abs/2607.28230",
    "source": "Ling Zhang, Boyan Xing, Zhenyu She, Zixiang Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.28230v1 Announce Type: new Abstract: Finite multiplicative systems often cease to evolve when a lower continuation threshold is reached,whereas standard growth-optimal benchmarks assume uni"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28323",
    "domain": "金融",
    "title": "Optimal Execution with Passive Market Impact",
    "url": "https://arxiv.org/abs/2607.28323",
    "source": "Alexander Barzykin, Robert Boyce, Eyal Neuman, Sturmius Tuschmann",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.28323v1 Announce Type: new Abstract: We derive a mesoscopic model for optimal execution with limit orders that incorporates microstructural features of passive price impact. Our framework i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28348",
    "domain": "金融",
    "title": "Economics and Epidemics: Evidence from an Estimated Spatial Econ-SIR Model",
    "url": "https://arxiv.org/abs/2607.28348",
    "source": "Mark Bognanni, Doug Hanley, Daniel Kolliner, Kurt Mitman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.28348v1 Announce Type: new Abstract: Economic analysis of effective policies for managing epidemics requires an integrated economic and epidemiological approach. We develop and estimate a s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28371",
    "domain": "金融",
    "title": "Stop Premature Obsolescence: LessTrash, Fewer Working Hours, Same Pay",
    "url": "https://arxiv.org/abs/2607.28371",
    "source": "Tommaso Luzzati, J. Christopher Proctor, S. D'Alessandro",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.28371v1 Announce Type: new Abstract: About a century ago, Keynes predicted that, thanks to technological progress, today's working week would be reduced to 15 hours. In practice, however, l"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28378",
    "domain": "金融",
    "title": "Do Crises Increase Parochial Behavior? Evidence from Donations During Covid",
    "url": "https://arxiv.org/abs/2607.28378",
    "source": "Esteban Jaimovich, Sarah Smith, Derrick Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.28378v1 Announce Type: new Abstract: Do people behave more favorably towards their in-group during a crisis? Defining in/out-groups by geography, we study donations to local versus non-loca"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.26560",
    "domain": "金融",
    "title": "Emission-Forecasting-Based Spatial-Temporal Carbon Response: A Multi-Agent Attention-Enhanced Deep Learning Framework",
    "url": "https://arxiv.org/abs/2607.26560",
    "source": "Feiyu Cai, Jing Qiu, Yi Yang, Chenxi Zhang, Xinlei Wang, Baichuan Liu, Junhua Zhao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.26560v1 Announce Type: cross Abstract: As a major contributor to carbon emissions, the decarbonization of power systems has garnered significant societal attention. Nodal carbon intensity ("
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27485",
    "domain": "金融",
    "title": "Energy Market and Carbon Emission Spillovers in Critical Minerals Investment: A Dynamic Connectedness Approach",
    "url": "https://arxiv.org/abs/2607.27485",
    "source": "Haibo Wang, Lutfu Sua, Jaime Ortiz, Jun Huang, Bahram Alidaee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.27485v1 Announce Type: cross Abstract: Design/methodology/approach A time-varying parameter vector autoregression (TVP-VAR) model is employed to quantify dynamic connectedness and direction"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27553",
    "domain": "金融",
    "title": "Using Large Language Models for Idea Generation in Innovation",
    "url": "https://arxiv.org/abs/2607.27553",
    "source": "Lennart Meincke, Karan Girotra, Gideon Nave, Christian Terwiesch, Karl T. Ulrich",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.27553v1 Announce Type: cross Abstract: This research evaluates the efficacy of large language models (LLMs) in generating new product ideas. To do so, we compare three pools of ideas for ne"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27853",
    "domain": "金融",
    "title": "FinanceHarness: Autonomous Financial Deep Research Framework",
    "url": "https://arxiv.org/abs/2607.27853",
    "source": "Yijia Xiao, Rujun Han, Yanfei Chen, Zifeng Wang, Ke Jiang, Zhongying CuiZhu, Vishy Tirumalashetty, Wei Wang, Burak Gokturk, Tomas Pfister, Chen-Yu Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.27853v1 Announce Type: cross Abstract: Powered by advances in LLMs and autonomous agents, deep research has become one of the most widely adopted agentic products. However, most deep resear"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27996",
    "domain": "金融",
    "title": "Downsian Competition for the Myerson Value",
    "url": "https://arxiv.org/abs/2607.27996",
    "source": "Daiki Kishishita",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.27996v1 Announce Type: cross Abstract: This paper studies an electoral competition model in which parties maximize legislative power rather than vote shares. Voters are uniformly distribute"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28127",
    "domain": "金融",
    "title": "FinSMART: Financial Sentiment Analysis for Algorithmic Trading through Market-Aligned Reinforcement Learning",
    "url": "https://arxiv.org/abs/2607.28127",
    "source": "Giorgos Iacovides, Wuyang Zhou, Danilo Mandic",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.28127v1 Announce Type: cross Abstract: Recent advances in Generative AI have substantially improved financial sentiment analysis through post-trained financial large language models (LLMs)."
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28215",
    "domain": "金融",
    "title": "Almost stochastic dominance via optimal transport",
    "url": "https://arxiv.org/abs/2607.28215",
    "source": "Alfred M\\\"uller, Johannes Wiesel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.28215v1 Announce Type: cross Abstract: We study parametric classes of almost stochastic dominance on general Polish spaces as order relations for probability distributions with a parameter "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28294",
    "domain": "金融",
    "title": "Bootstrap inference in autoregressive duration models",
    "url": "https://arxiv.org/abs/2607.28294",
    "source": "Giuseppe Cavaliere, Thomas Mikosch, Anders Rahbek, Frederik Vilandt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.28294v1 Announce Type: cross Abstract: This paper develops bootstrap inference for autoregressive conditional duration (ACD) models observed over a fixed calendar span, so that the number o"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28410",
    "domain": "金融",
    "title": "Can Large Language Models Execute Parent Orders?",
    "url": "https://arxiv.org/abs/2607.28410",
    "source": "Zane Shen, Xinli Xu, Guangyi Zhang, Jialong Chen, Jinsong Zhou, Cong Chen, Guibao Shen, Dongyu Yan, Luozhou Wang, Zhen Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.28410v1 Announce Type: cross Abstract: Parent-order execution is a core problem in algorithmic trading, where the goal is to split a large order into smaller orders while reducing execution"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28577",
    "domain": "金融",
    "title": "Train Often, Deploy Selectively: Forward-Gated Model Replacement in Crypto Markets",
    "url": "https://arxiv.org/abs/2607.28577",
    "source": "Aditya Dutta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2607.28577v1 Announce Type: cross Abstract: Production forecasting systems retrain models regularly, but a retrained candidate does not necessarily outperform a continuously maintained incumbent"
  },
  {
    "id": "rss:https://arxiv.org/abs/2203.05595",
    "domain": "金融",
    "title": "Social Networks and Spatial Mobility: Evidence from Facebook in India",
    "url": "https://arxiv.org/abs/2203.05595",
    "source": "Harshil Sahai, Michael Bailey",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2203.05595v2 Announce Type: replace Abstract: This paper studies the role of social networks in spatial mobility across India. Using aggregated and de-identified data from the world's largest on"
  },
  {
    "id": "rss:https://arxiv.org/abs/2408.16443",
    "domain": "金融",
    "title": "The Turing Valley: How AI Capabilities Shape Labor Income",
    "url": "https://arxiv.org/abs/2408.16443",
    "source": "Enrique Ide, Eduard Talam\\`as",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2408.16443v3 Announce Type: replace Abstract: There is concern that progress toward AI systems with strong capabilities across domains will reduce the importance of human input in production and"
  },
  {
    "id": "rss:https://arxiv.org/abs/2505.18687",
    "domain": "金融",
    "title": "When Do AI Gains Become Broadly Shareable? A Policy Threshold for AI-Driven Automation",
    "url": "https://arxiv.org/abs/2505.18687",
    "source": "Aran Nayebi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T04:00:00+00:00",
    "summary": "arXiv:2505.18687v4 Announce Type: replace Abstract: AI-driven automation generates broad-based social benefit only if technical gains become visible, durable, and publicly claimable. We develop a poli"
  },
  {
    "id": "hn:49024958",
    "domain": "金融",
    "title": "DOT cranks up its campaign to strip bike lane references from federal websites",
    "url": "https://text.npr.org/nx-s1-5900901",
    "source": "Jtsummers",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-07-23T17:11:39+00:00",
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
    "id": "hn:48884775",
    "domain": "金融",
    "title": "Storm clouds gather over America's financial supremacy",
    "url": "https://www.economist.com/finance-and-economics/2026/07/12/storm-clouds-gather-over-americas-financial-supremacy",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-07-12T21:04:13+00:00",
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
    "id": "hn:48791799",
    "domain": "金融",
    "title": "Is The Economist Always Wrong?",
    "url": "https://economist.com/interactive/finance-and-economics/2026/07/02/is-the-economist-always-wrong",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 59,
    "published_at": "2026-07-05T06:40:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:49028304",
    "domain": "金融",
    "title": "US announces double-digit tariffs on most of globe to replace expiring duties",
    "url": "https://finance.yahoo.com/economy/policy/article/trump-administration-announces-the-next-phase-of-global-tariffs-with-10-to-125-rates-on-much-of-the-globe-210032314.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-07-23T21:28:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:49047488",
    "domain": "金融",
    "title": "Stripe in talks to acquire OpenRouter in potential $10B deal, WSJ reports",
    "url": "https://finance.yahoo.com/technology/ai/articles/stripe-talks-acquire-openrouter-potential-215104525.html",
    "source": "nlpnerd",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-25T13:38:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48953857",
    "domain": "金融",
    "title": "Nadella Blasts AI Industry's Double Standard",
    "url": "https://finance.biggo.com/news/438f299b-ca23-468d-b37d-0ffe09a4ca55",
    "source": "nittanymount",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-07-18T00:28:46+00:00",
    "summary": ""
  }
]
```
