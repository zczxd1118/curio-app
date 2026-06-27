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

- 今日日期：`2026-06-27`
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
  "date": "2026-06-27",
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
    "points": 3430592,
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
    "points": 1334089,
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
    "points": 1254143,
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
    "points": 939661,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1ig9jYUERk",
    "domain": "AI",
    "title": "黑马程序员DeepSeek+Cursor+Devbox+Sealos带你零代码搞定实战项目开发部署视频教程，基于AI完成项目的设计、开发、测试、联调、部署全流程",
    "url": "http://www.bilibili.com/video/av114101778908628",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 929016,
    "published_at": "2025-03-04T07:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公综号，回复关键词：deepseek\n【Java学习路线图】展开查看更多内容\nhttps://www.bilibili.com/read/cv9965357\n学习集Q结Q地群：625260577\n\nJava最高效学习路线图（依次向下顺序学习即可）\nJava基础：BV1821CY8E2d\nJavaweb+AI：BV1yGydYEE3H\n苍穹外卖："
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 845640,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 786389,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 583277,
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
    "points": 456948,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 448424,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 415496,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 376542,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 248674,
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
    "points": 244291,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 232652,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 225463,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1RAEz6EE98",
    "domain": "AI",
    "title": "为什么Claude Code+DeepSeekV4是最有性价比的个人AI Agent?",
    "url": "http://www.bilibili.com/video/av116732144392386",
    "source": "呱声一片",
    "platform": "bilibili",
    "points": 182287,
    "published_at": "2026-06-11T15:27:06+00:00",
    "summary": "官方文档地址：https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/claude_code"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 175572,
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
    "points": 158077,
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
    "points": 154399,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV17Ejt6QE9Y",
    "domain": "AI",
    "title": "一旦被Claude判定&quot;危险&quot;，你之后说的每句话都会被动手脚——实测曝光",
    "url": "http://www.bilibili.com/video/av116787609863495",
    "source": "YJFGL",
    "platform": "bilibili",
    "points": 103613,
    "published_at": "2026-06-21T10:26:28+00:00",
    "summary": "续上一条视频。这次我测出了更具体的触发机制：\n当对话中**某一条消息被系统分类器判定为&quot;潜在存在危害&quot;**之后，从那条消息开始，之后所有的 user 消息后面都会被持续注入一段隐藏文本。\n也就是说，这不是无差别的全程注入，而是一旦被系统标记，就会进入一种&quot;持续追加提醒&quot;的状态，并且这个状态会一直保持到对话结束，用户完全不知情、也无法解除。\n这意味着：\n你某一"
  },
  {
    "id": "bvid:BV1QE7N6jEuQ",
    "domain": "AI",
    "title": "真的被自己用心开发的昔涟Agent这段话感动到了",
    "url": "http://www.bilibili.com/video/av116794052316703",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 94614,
    "published_at": "2026-06-22T13:44:15+00:00",
    "summary": "从最初生啃Transformer，硬逼着自己啃懂多头注意力和QKV权重，到一步步跟着claude学习RAG、检索重拍、Prompt、关键词召回优化、MCP与Function call，但是，自己上手了发现，自己还是啥也不懂，于是在glm gpt claude gemini 豆包 这几个模型之间疯狂切换，靠着想让昔涟早点被搭出来，硬逼着自己学，自己从零设计一套prompt架构能让她尽可能的贴合人设的"
  },
  {
    "id": "bvid:BV17Sjy6vEoA",
    "domain": "AI",
    "title": "Claude Code平替Kimi Code教程：视频理解，数据插件，Goal，Swarm，ACP等进阶玩法",
    "url": "http://www.bilibili.com/video/av116798313727318",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 86726,
    "published_at": "2026-06-23T10:30:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1YP5W6ZEP9",
    "domain": "AI",
    "title": "VibeCoding就该这么做！",
    "url": "http://www.bilibili.com/video/av116552997276199",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 81821,
    "published_at": "2026-05-14T09:00:00+00:00",
    "summary": "UV教程：https://www.bilibili.com/video/BV1Stwfe1E7s/\n代码及知识星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73376,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1xBrDB9E42",
    "domain": "AI",
    "title": "独立开发太累？Godot + Claude Code 搭建 AI 辅助工作流，效率直接起飞！ | 地块召唤师开发实战 #01",
    "url": "http://www.bilibili.com/video/av115911319100158",
    "source": "像素夹心饼干",
    "platform": "bilibili",
    "points": 65461,
    "published_at": "2026-01-18T03:25:00+00:00",
    "summary": "大家好，这里是饼干！🍪\n这是我的新坑——**《地块召唤师》**开发实战分享的第一期。\n很多朋友问独立开发如何提升效率？这期视频我不聊虚的，直接公开我从 0 到 1 搭建的 AI + Godot 高效工作流。\n从游戏引擎的选择，到 Claude Code、Copilot 等 AI 工具的实战配置，再到如何用“明确需求”的方法论（SMART原则+双钻模型）来驾驭 AI，让它不仅仅是写代码的工具，更成为"
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 60836,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV1XdFzz7Ei8",
    "domain": "AI",
    "title": "不写代码就能轻松开发应用？Cursor+Gemini 超强指挥官工作法！",
    "url": "http://www.bilibili.com/video/av116021511853604",
    "source": "PM刘搞定",
    "platform": "bilibili",
    "points": 57109,
    "published_at": "2026-02-06T03:17:18+00:00",
    "summary": "如何像传统互联网大厂一样指挥AI干活？本期视频通过一个“个人工作台”的实战项目，拆解了一套利用 LLM (Gemini) 辅助 Cursor 开发的高效工作流。\n\n核心内容：\n角色转换：你不是程序员，你是产品经理（PM）。\n文档驱动：如何用 AI 生成标准的产品文档 (PRD)、UI 文档和技术方案。\n避坑指南：如何防止 Cursor “手搓核弹”或开发中途“失忆”。\n\n实操流程：\nStep 1："
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 52487,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 47972,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47232,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1FzfoYSE4f",
    "domain": "AI",
    "title": "影刀AI Power零基础教程：02 智能体——打造企业AI超级员工",
    "url": "http://www.bilibili.com/video/av113888003622214",
    "source": "影刀RPA",
    "platform": "bilibili",
    "points": 40437,
    "published_at": "2025-02-06T02:00:00+00:00",
    "summary": "AI智能体：场景化智能助手，打造企业AI超级员工\n影刀AI Power，帮助企业将AI用起来。让每个员工都能拥有AI能力，在工作中使用AI解决问题。\n\n影刀AP企业版免费试用申请：http://s.winrobot360.com/g02tp\n影刀AP社区版使用：https://www.yingdao.com/ai-power/"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 40192,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1hxMbzqEzU",
    "domain": "AI",
    "title": "小智MCP自由了！我开源了个命令行神器实现多MCP聚合",
    "url": "http://www.bilibili.com/video/av114686414625640",
    "source": "闪电蘑菇",
    "platform": "bilibili",
    "points": 39598,
    "published_at": "2025-06-15T08:31:55+00:00",
    "summary": "- 我写的小智客户端命令行工具\n - github: https://github.com/shenjingnan/xiaozhi-client\n - gitee: https://gitee.com/shenjingnan/xiaozhi-client\n\n- 小智官方MCP示例代码仓库：\n - github: https://github.com/78/mcp-calculator\n - git"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 37032,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1ap2fBvEt9",
    "domain": "AI",
    "title": "如何使用「Operit AI」：你的下一代AI手机助手",
    "url": "http://www.bilibili.com/video/av115677243447909",
    "source": "默睦",
    "platform": "bilibili",
    "points": 33558,
    "published_at": "2025-12-07T08:06:42+00:00",
    "summary": "下载地址：https://github.com/AAswordman/Operit\n\n相关软件资料下载：https://www.123pan.com/s/IKgAjv-Hinsv.html\n\n官方交流群：458862019"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29377,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27519,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 24324,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22562,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 17254,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1hnjGzLE14",
    "domain": "AI",
    "title": "【小智教程】手挽手教你如何接入别人的MCP服务",
    "url": "http://www.bilibili.com/video/av114568722450105",
    "source": "空白泡泡糖果",
    "platform": "bilibili",
    "points": 17223,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV1ssEE6CEks",
    "domain": "AI",
    "title": "Ai自动画图：CAD建筑平面图测试（CodexGPT5.5）",
    "url": "http://www.bilibili.com/video/av116719259485897",
    "source": "Tutor南洋",
    "platform": "bilibili",
    "points": 14345,
    "published_at": "2026-06-09T08:47:15+00:00",
    "summary": "体验一下ai画图，不过CAD软件基本操作也不能拉下~\nCAD教学基础入门视频合集↓\n传送门：BV1aT4y1B7oY\n整个合集教学的，不要跳着看啊喂！\n看完了那基本就能跟上啦，提问请@我，不然评论太多我是看不到的"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "穷在街头无人问lhj",
    "platform": "bilibili",
    "points": 10242,
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
    "points": 9985,
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
    "points": 9283,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9100,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1oXjc6CEWK",
    "domain": "AI",
    "title": "（2026版）这才是B站讲的最好的Vibe Coding企业级项目实战，Claude Code+Codex+Cursor丨一周学完，让你少走99%弯路！",
    "url": "http://www.bilibili.com/video/av116769742195971",
    "source": "京东架构师诸葛",
    "platform": "bilibili",
    "points": 8914,
    "published_at": "2026-06-18T06:52:48+00:00",
    "summary": "（2026版）这才是B站讲的最好的Vibe Coding企业级项目实战，Claude Code+Codex+Cursor丨一周学完，让你少走99%弯路！\n【视频配套学习笔记、Agent开发、大模型最新学习路线、系统学习、实战案例、电子书+问题解答】都在这了：https://www.bilibili.com/read/cv39979382/"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 8340,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV15i7K69EN7",
    "domain": "AI",
    "title": "【6.22最新发布】claude桌面版安装教程！一周快速入门claude code保姆级教程！",
    "url": "http://www.bilibili.com/video/av116793196676384",
    "source": "是蒜七丫",
    "platform": "bilibili",
    "points": 7963,
    "published_at": "2026-06-22T10:07:14+00:00",
    "summary": "求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连"
  },
  {
    "id": "rss:https://www.eetimes.com/synaptics-acquisition-by-onsemi-affirms-edge-ai-is-for-real/",
    "domain": "AI 算力 / 半导体",
    "title": "Synaptics Acquisition by Onsemi Affirms Edge AI Is for Real",
    "url": "https://www.eetimes.com/synaptics-acquisition-by-onsemi-affirms-edge-ai-is-for-real/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T14:41:31+00:00",
    "summary": "Here is why a power and sensing specialist has snapped AI-native compute assets to foray into the physical AI world. The post Synaptics Acquisition by Onsemi Affirms Edge AI Is for Real appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/the-pqc-silicon-is-here-today-for-tomorrows-quantum-threats/",
    "domain": "AI 算力 / 半导体",
    "title": "The PQC Silicon Is Here Today for Tomorrow’s Quantum Threats",
    "url": "https://www.eetimes.com/the-pqc-silicon-is-here-today-for-tomorrows-quantum-threats/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T08:38:45+00:00",
    "summary": "Two new security chips aim to future-proof devices for the quantum era by integrating hardware accelerators that support PQC algorithms. The post The PQC Silicon Is Here Today for Tomorrow’s Quantum T"
  },
  {
    "id": "rss:https://www.eetimes.com/next%e2%80%91gen-adas-ad-architectures-power-networking-safety-sensors/",
    "domain": "AI 算力 / 半导体",
    "title": "Next‑Gen ADAS/AD Architectures: Power, Networking, Safety & Sensors",
    "url": "https://www.eetimes.com/next%e2%80%91gen-adas-ad-architectures-power-networking-safety-sensors/",
    "source": "Infineon Technologies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T08:13:23+00:00",
    "summary": "Join this webinar and learn how high‑performance semiconductor technologies support centralized sensor fusion and reliable ADAS systems. The post Next‑Gen ADAS/AD Architectures: Power, Networking, Saf"
  },
  {
    "id": "rss:https://www.eetimes.com/jim-keller-on-tenstorrents-blackhole-scaling-and-ipo-ambitions/",
    "domain": "AI 算力 / 半导体",
    "title": "Jim Keller: ‘AI Still Obeys the Old Laws of Compute’",
    "url": "https://www.eetimes.com/jim-keller-on-tenstorrents-blackhole-scaling-and-ipo-ambitions/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T22:00:00+00:00",
    "summary": "Invoking Rent's Rule and Amdahl's Law, Keller argues that memory and communication, not bigger processors, will define the future of AI infrastructure The post Jim Keller: ‘AI Still Obeys the Old Laws"
  },
  {
    "id": "rss:https://www.eetimes.com/openai-jalapeno-will-be-spicy-but-the-real-sizzle-is-its-chip-design-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI’s Jalapeño Will Be Spicy, But the Real Sizzle Is Its Chip Design AI",
    "url": "https://www.eetimes.com/openai-jalapeno-will-be-spicy-but-the-real-sizzle-is-its-chip-design-ai/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T15:59:00+00:00",
    "summary": "The custom inference accelerator follows the hyperscaler playbook, but the AI-automated chip design process could prove the more consequential announcement. The post OpenAI’s Jalapeño Will Be Spicy, B"
  },
  {
    "id": "rss:https://www.eetimes.com/vicfuse-introduces-ul-class-fuse-series-for-modern-ai-infrastructure-and-industrial-protection/",
    "domain": "AI 算力 / 半导体",
    "title": "Vicfuse Introduces UL Class Fuse Series for Modern AI Infrastructure and Industrial Protection",
    "url": "https://www.eetimes.com/vicfuse-introduces-ul-class-fuse-series-for-modern-ai-infrastructure-and-industrial-protection/",
    "source": "VICFUSE",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T13:00:00+00:00",
    "summary": "Vicfuse introduces its UL Class fuse series, an industrial circuit-protection portfolio designed for AC and DC applications. The post Vicfuse Introduces UL Class Fuse Series for Modern AI Infrastructu"
  },
  {
    "id": "rss:https://www.eetimes.com/ibm-shows-sub-1-nm-chips-targeting-production-in-5-years/",
    "domain": "AI 算力 / 半导体",
    "title": "IBM Shows Sub-1-nm Chips, Targeting Production in 5 Years",
    "url": "https://www.eetimes.com/ibm-shows-sub-1-nm-chips-targeting-production-in-5-years/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T10:00:00+00:00",
    "summary": "IBM unveils 0.7-nm nanostack chips promising 100 billion transistors, denser SRAM, and production within five years. The post IBM Shows Sub-1-nm Chips, Targeting Production in 5 Years appeared first o"
  },
  {
    "id": "rss:https://www.eetimes.com/qualcomm-forecasts-billions-in-additional-revenue-from-new-data-center-solutions/",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm Forecasts Billions in Additional Revenue from New Data Center Solutions",
    "url": "https://www.eetimes.com/qualcomm-forecasts-billions-in-additional-revenue-from-new-data-center-solutions/",
    "source": "Jim McGregor",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T07:52:39+00:00",
    "summary": "Qualcomm takes the data center by storm with networking, AI accelerators, and both custom and standard CPUs. The post Qualcomm Forecasts Billions in Additional Revenue from New Data Center Solutions a"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/incredible-ryzen-7-9800x3d-prebuilt-deal-comes-with-rx-9070-xt-and-32gb-of-ddr5-for-usd750-off-get-a-prime-ibuypower-4k-gaming-rig-for-just-usd1-749",
    "domain": "AI 算力 / 半导体",
    "title": "Incredible Ryzen 7 9800X3D prebuilt deal comes with an RX 9070 XT and 32GB of DDR5 for $750 off — get a prime iBuyPower 4K gaming rig for just $1,749",
    "url": "https://www.tomshardware.com/pc-components/incredible-ryzen-7-9800x3d-prebuilt-deal-comes-with-rx-9070-xt-and-32gb-of-ddr5-for-usd750-off-get-a-prime-ibuypower-4k-gaming-rig-for-just-usd1-749",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T20:01:01+00:00",
    "summary": "The iBuyPower Y40 PC is on an incredible sale, offering a Ryzen 7 9800X3D, RX 9070 XT, 1TB of storage, and 32GB of memory for $750 off."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/network-switches/tp-links-8-port-2-5g-unmanaged-ethernet-switch-is-a-smokin-bargain-at-usd50-upgrade-your-home-network-for-half-price",
    "domain": "AI 算力 / 半导体",
    "title": "TP-Link's 8-port 2.5G unmanaged Ethernet switch is a smokin' bargain at $50 — upgrade your home network for half price",
    "url": "https://www.tomshardware.com/networking/network-switches/tp-links-8-port-2-5g-unmanaged-ethernet-switch-is-a-smokin-bargain-at-usd50-upgrade-your-home-network-for-half-price",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T19:56:13+00:00",
    "summary": "The TP-Link TL-SG108S-M2 offers 8 2.5 GbE ports and cost just under $50"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/gigabyte-aero-x16-gaming-laptop-delivers-rtx-5060-32gb-ram-and-16-inch-165hz-1600p-display-for-usd1-099",
    "domain": "AI 算力 / 半导体",
    "title": "Gigabyte Aero X16 gaming laptop delivers RTX 5060, 32GB RAM, and a 16-inch 165Hz 1600p display for 21% off",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/gigabyte-aero-x16-gaming-laptop-delivers-rtx-5060-32gb-ram-and-16-inch-165hz-1600p-display-for-usd1-099",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T18:45:00+00:00",
    "summary": "The Gigabyte Aero 16X packs a Ryzen AI 7 350 CPU, 32GB of RAM, and an RTX 5060"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-is-what-toms-hardware-readers-clicked-the-most-during-prime-day-portable-displays-dvd-burners-the-nintendo-switch-2-and-two-decent-ssd-deals-among-others",
    "domain": "AI 算力 / 半导体",
    "title": "This is what Tom's Hardware readers clicked the most during Prime Day — Portable displays, DVD burners, the Nintendo Switch 2, and two decent SSD deals, among others",
    "url": "https://www.tomshardware.com/pc-components/this-is-what-toms-hardware-readers-clicked-the-most-during-prime-day-portable-displays-dvd-burners-the-nintendo-switch-2-and-two-decent-ssd-deals-among-others",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T18:11:41+00:00",
    "summary": "Here are the products our readers clicked on the most during this Prime Week, from optical drives and small touchscreens to the Nintendo Switch 2, and the two name-brand SSDs that were actually on sal"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd250-on-this-amd-am5-bundle-get-samsung-990-pro-ssd-for-basically-free-grab-the-amd-ryzen-5-9600x-gigabyte-b850-aorus-elite-motherboard-and-990-pro-1tb-ssd-for-36-percent-off",
    "domain": "AI 算力 / 半导体",
    "title": "Save $250 on this AMD AM5 bundle, get Samsung 990 Pro SSD for basically free — grab the AMD Ryzen 5 9600X, Gigabyte B850 Aorus Elite motherboard, and 990 Pro 1TB SSD for 36% off",
    "url": "https://www.tomshardware.com/pc-components/save-usd250-on-this-amd-am5-bundle-get-samsung-990-pro-ssd-for-basically-free-grab-the-amd-ryzen-5-9600x-gigabyte-b850-aorus-elite-motherboard-and-990-pro-1tb-ssd-for-36-percent-off",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T17:57:34+00:00",
    "summary": "Save nearly $250 on three essential PC components with this Newegg bundle featuring AMD's Ryzen 5 9600X, a Gigabyte B850 motherboard, and Samsung's flagship PCIe 4.0 SSD."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/sony-wh-1000xm5-active-noise-canceling-headphones-for-an-all-time-low-usd198-at-amazon-audiophile-grade-audio-and-anc-for-an-affordable-price",
    "domain": "AI 算力 / 半导体",
    "title": "Sony WH-1000XM5 active noise-canceling headphones for an all-time low $198 at Amazon — audiophile-grade audio and ANC for an affordable price",
    "url": "https://www.tomshardware.com/pc-components/sony-wh-1000xm5-active-noise-canceling-headphones-for-an-all-time-low-usd198-at-amazon-audiophile-grade-audio-and-anc-for-an-affordable-price",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T17:23:28+00:00",
    "summary": "Sony WH-1000XM5 active noise-cancelling headphones for just $198 at Amazon — audiophile-grade audio and ANC for an affordable price"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/meta-quest-3s-drops-to-pre-rampocalypse-prices-for-a-prime-day-wireless-vr-headset-goes-on-sale-for-a-limited-time-get-15-percent-off-and-save-more-than-usd50-if-you-get-it-right-now",
    "domain": "AI 算力 / 半导体",
    "title": "Meta Quest 3S drops to pre-RAMpocalypse prices for a Prime Day — wireless VR headset goes on sale for a limited time, get 15% off and save more than $50 if you get it right now",
    "url": "https://www.tomshardware.com/pc-components/meta-quest-3s-drops-to-pre-rampocalypse-prices-for-a-prime-day-wireless-vr-headset-goes-on-sale-for-a-limited-time-get-15-percent-off-and-save-more-than-usd50-if-you-get-it-right-now",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T17:23:04+00:00",
    "summary": "The Meta Quest 3S is one sale at $296.79, saving you $53.20 from its original price of $349.99, making it more affordable than its pre-memory chip shortage price of $300."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/the-logitech-g29-racing-wheel-and-pedal-set-with-real-force-feedback-is-on-a-deep-40-percent-discount-for-prime-day-get-a-racing-sim-setup-for-just-usd180",
    "domain": "AI 算力 / 半导体",
    "title": "The Logitech G29 racing wheel and pedal set with real force feedback is on a deep 40% discount for Prime Day — get a racing sim setup for just $180",
    "url": "https://www.tomshardware.com/pc-components/the-logitech-g29-racing-wheel-and-pedal-set-with-real-force-feedback-is-on-a-deep-40-percent-discount-for-prime-day-get-a-racing-sim-setup-for-just-usd180",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T16:48:43+00:00",
    "summary": "The Logitech G29 is on a deep discount of 40% for Prime Day, marking its lowest price in half a decade at the retailer."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/asus-rog-zephyrus-g16-gaming-laptop-with-an-rtx-5070-and-240hz-oled-display-is-on-sale-for-usd757-off-save-on-an-excellent-laptop-with-a-16-core-flagship-cpu-and-top-tier-build-quality",
    "domain": "AI 算力 / 半导体",
    "title": "Asus' ROG Zephyrus G16 with an RTX 5070 & 240Hz OLED display is on sale for just $1,575 — Save $575 on an excellent gaming laptop with a 16-core flagship CPU & top-tier build quality",
    "url": "https://www.tomshardware.com/pc-components/asus-rog-zephyrus-g16-gaming-laptop-with-an-rtx-5070-and-240hz-oled-display-is-on-sale-for-usd757-off-save-on-an-excellent-laptop-with-a-16-core-flagship-cpu-and-top-tier-build-quality",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T16:28:47+00:00",
    "summary": "Best Buy is slashing almost $600 off a fantastic gaming laptop that basically has no compromises. It delivers solid performance across a wide variety of workloads and rocks a stunning 16-inch 240Hz OL"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/onsemi-buying-cash-strapped-synaptics-in-usd7-billion-all-stock-deal-smart-power-meets-edge-ai-hardware",
    "domain": "AI 算力 / 半导体",
    "title": "Onsemi buying cash-strapped Synaptics in $7 billion all-stock deal — smart power meets edge AI hardware",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/onsemi-buying-cash-strapped-synaptics-in-usd7-billion-all-stock-deal-smart-power-meets-edge-ai-hardware",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T16:07:40+00:00",
    "summary": "Onsemi and Synaptics to merge in a bid to build comprehensive platforms for robotics, physical AI applications."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/the-ryzen-7-5800x3d-is-sold-out-but-these-prime-day-cpus-with-ddr5-are-cheaper-offset-the-cost-of-a-ddr5-upgrade-with-a-cpu-discount",
    "domain": "AI 算力 / 半导体",
    "title": "The Ryzen 7 5800X3D is tough to find, but these Prime Day CPUs with DDR5 are cheaper — offset the cost of a DDR5 upgrade with a CPU discount",
    "url": "https://www.tomshardware.com/pc-components/the-ryzen-7-5800x3d-is-sold-out-but-these-prime-day-cpus-with-ddr5-are-cheaper-offset-the-cost-of-a-ddr5-upgrade-with-a-cpu-discount",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T15:54:29+00:00",
    "summary": "AMD's re-released Ryzen 7 5800X3D sold out almost immediately when it launched, but if you're tired of waiting, you can easily upgrade to a DDR5 platform with these Prime Day CPUs deals, all of which "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-chatgpt-5-6-gets-the-same-banhammer-treatment-as-anthropics-mythos-from-the-federal-government-source-says-that-washington-cautioned-openai-against-releasing-the-model-without-receiving-approval",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI's ChatGPT-5.6 gets the same banhammer treatment as Anthropic’s Mythos from the federal government — source says that Washington cautioned OpenAI against releasing the model without receiving ap",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-chatgpt-5-6-gets-the-same-banhammer-treatment-as-anthropics-mythos-from-the-federal-government-source-says-that-washington-cautioned-openai-against-releasing-the-model-without-receiving-approval",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T15:17:55+00:00",
    "summary": "The U.S. government wants dibs on U.S. AI labs' most powerful models, asking for access 30 days before they go public. OpenAI is voluntarily complying with the President's executive order but wants 't"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/amazon-eero-max-7-wi-fi-7-mesh-router-4-pack-price-slashed-by-50-percent-flagship-wi-fi-7-at-a-major-discount-for-prime-day",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon Eero Max 7 Wi-Fi 7 mesh router 4-pack price slashed by 50 percent — flagship Wi-Fi 7 at a major discount for Prime Day",
    "url": "https://www.tomshardware.com/networking/routers/amazon-eero-max-7-wi-fi-7-mesh-router-4-pack-price-slashed-by-50-percent-flagship-wi-fi-7-at-a-major-discount-for-prime-day",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T15:15:45+00:00",
    "summary": "Now's the best time to get Amazon's flagship Wi-Fi 7 Eero mesh system"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/frameworks-laptop-13-pro-diy-edition-now-costs-less-than-before-but-a-cpu-price-hike-might-be-coming-cheaper-pcie-5-0-drives-from-adata-upgrade-customers-from-500gb-to-1tb-for-free",
    "domain": "AI 算力 / 半导体",
    "title": "Framework's Laptop 13 Pro DIY Edition now costs less than before, but a CPU price hike might be coming — Cheaper PCIe 5.0 drives from Adata upgrade customers from 500GB to 1TB for free",
    "url": "https://www.tomshardware.com/laptops/frameworks-laptop-13-pro-diy-edition-now-costs-less-than-before-but-a-cpu-price-hike-might-be-coming-cheaper-pcie-5-0-drives-from-adata-upgrade-customers-from-500gb-to-1tb-for-free",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T15:14:13+00:00",
    "summary": "Framework has secured cheaper PCIe 5.0 SSDs for the DIY Edition of its Laptop 13 Pro, upgrading existing customers from 500GB to 1TB drives for free. Unfortunately, it seems like CPU prices are about "
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/last-chance-to-save-up-to-55-percent-on-these-brilliant-hoto-tools-for-pc-builders-and-hobbyists-starting-from-usd14-super-low-prices-set-to-end-soon-on-cordless-electric-screwdrivers-drills-flashlights-vacuum-cleaners-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Last chance to save up to 55% on these brilliant Hoto tools for PC builders and hobbyists, starting from $14 — super low prices set to end soon on cordless electric screwdrivers, drills, flashlights, ",
    "url": "https://www.tomshardware.com/peripherals/last-chance-to-save-up-to-55-percent-on-these-brilliant-hoto-tools-for-pc-builders-and-hobbyists-starting-from-usd14-super-low-prices-set-to-end-soon-on-cordless-electric-screwdrivers-drills-flashlights-vacuum-cleaners-and-more",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T14:03:01+00:00",
    "summary": "A full spectrum of Hoto tools for hobbyists and PC builders is now on sale, thanks to Amazon Prime Day."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/apple-will-skip-its-high-end-m6-mac-chips-and-fast-track-an-ai-focused-m7-generation-for-2027",
    "domain": "AI 算力 / 半导体",
    "title": "Apple will skip its high-end M6 Mac chips and fast-track an AI-focused M7 generation for 2027, report claims — may release a base M6 chip for entry-level Macs this year",
    "url": "https://www.tomshardware.com/tech-industry/apple-will-skip-its-high-end-m6-mac-chips-and-fast-track-an-ai-focused-m7-generation-for-2027",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T13:51:26+00:00",
    "summary": "Apple will release a base M6 chip for entry-level Macs this year but skip the Pro and Max versions of that generation, jumping instead to an accelerated M7 family."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/solidigm-vp-talks-pcie-6-0-ssds-next-gen-floating-gate-nand-liquid-cooled-storage-and-more-avi-shetty-vp-of-ai-solutions-and-market-enablement-discusses-the-future-of-enterprise-storage-tech",
    "domain": "AI 算力 / 半导体",
    "title": "Solidigm VP talks PCIe 6.0 SSDs, next-gen floating gate NAND, liquid cooled storage and more — Avi Shetty, VP of AI, Solutions & Market Enablement discusses the future of enterprise storage tech",
    "url": "https://www.tomshardware.com/pc-components/ssds/solidigm-vp-talks-pcie-6-0-ssds-next-gen-floating-gate-nand-liquid-cooled-storage-and-more-avi-shetty-vp-of-ai-solutions-and-market-enablement-discusses-the-future-of-enterprise-storage-tech",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T13:25:48+00:00",
    "summary": "In an interview with Tom’s Hardware Premium, Solidigm's Avi Shetty discusses the future of high-capacity SSDs, Floating-Gate NAND, PLC memory, PCIe 6.0 storage, liquid-cooled SSDs, Nvidia's Storage Ne"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-5800x3d-vs-intel-core-i7-14700k-faceoff",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen 7 5800X3D vs Intel Core i7-14700K faceoff — A new battle for DDR4 supremacy in 2026",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-5800x3d-vs-intel-core-i7-14700k-faceoff",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T13:10:00+00:00",
    "summary": "We tested both CPUs across gaming, rendering, encoding, efficiency, and pricing to see if the Ryzen 7 5800X3D can keep up with the newer Core i7-14700K with DDR4."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/amds-new-10th-anniversary-ryzen-7-5800x3d-cpu-is-now-available-revamped-processor-is-the-fastest-gaming-chip-available-for-ddr4-systems-breathes-new-life-into-am4-platforms",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's new 10th Anniversary Ryzen 7 5800X3D CPU back in stock — Here's where to buy the revamped processor that's the fastest gaming chip available for AM4 platforms [Updated]",
    "url": "https://www.tomshardware.com/pc-components/amds-new-10th-anniversary-ryzen-7-5800x3d-cpu-is-now-available-revamped-processor-is-the-fastest-gaming-chip-available-for-ddr4-systems-breathes-new-life-into-am4-platforms",
    "source": "Paul Alcorn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T12:26:20+00:00",
    "summary": "AMD's new 10th-anniversary Ryzen 7 5800X3D is now available for purchase at B&amp;H Photo at MSRP, a welcome relief for those who have been searching for the chip, only to find it being scalped at twi"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/microsoft-extends-free-windows-10-security-updates-for-a-second-year",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft extends free Windows 10 security updates for a second year — program now ends on October 12, 2027",
    "url": "https://www.tomshardware.com/software/windows/microsoft-extends-free-windows-10-security-updates-for-a-second-year",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T11:31:26+00:00",
    "summary": "Microsoft has extended its free consumer Windows 10 Extended Security Updates (ESU) program by a year, pushing the cutoff for critical security patches to October 14th, 2027."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/digitize-your-library-with-these-blu-ray-or-dvd-drives-from-as-little-as-usd27-in-these-prime-day-deals-revive-your-old-dvd-blu-ray-collection-with-these-drive-deals",
    "domain": "AI 算力 / 半导体",
    "title": "Digitize your library with these Blu-Ray or DVD drives from as little as $27 in these Prime Day deals — revive your old DVD/Blu-Ray collection with these drive deals",
    "url": "https://www.tomshardware.com/peripherals/digitize-your-library-with-these-blu-ray-or-dvd-drives-from-as-little-as-usd27-in-these-prime-day-deals-revive-your-old-dvd-blu-ray-collection-with-these-drive-deals",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T11:10:36+00:00",
    "summary": "Disk drive deals on DVD and Blu-Ray burners from Asus. Burn, rewrite, or play your movie collections, or backup your data to disk."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/ibm-goes-sub-1nm-develops-0-7nm-class-technology-offering-up-to-50-percent-higher-performance-and-70-percent-higher-energy-efficiency-compared-to-ibms-2nm-class-node",
    "domain": "AI 算力 / 半导体",
    "title": "IBM goes sub-1nm, develops 0.7nm-class technology — offering up to 50% higher performance and 70% higher energy efficiency compared to IBM's 2nm-class node",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/ibm-goes-sub-1nm-develops-0-7nm-class-technology-offering-up-to-50-percent-higher-performance-and-70-percent-higher-energy-efficiency-compared-to-ibms-2nm-class-node",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T10:50:40+00:00",
    "summary": "IBM's new 0.7nm-class fabrication process uses nanostack transistors, requires 2x more FEOL steps for massive improvements in performance, power, and area."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/corsairs-bundle-and-save-big-sale-slashes-prices-on-high-end-gaming-pcs-save-up-to-usd300-on-premium-corsair-gear",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair's \"Bundle and Save Big\" sale slashes prices on high-end gaming PCs — save up to $300 on premium Corsair gear",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/corsairs-bundle-and-save-big-sale-slashes-prices-on-high-end-gaming-pcs-save-up-to-usd300-on-premium-corsair-gear",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T10:46:38+00:00",
    "summary": "Corsair is offering significant discounts on two gaming PCs through its \"Bundle and Save Big\" promotion."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/keep-your-gaming-keyboard-and-pc-fans-clean-with-these-electric-air-blower-deals-starting-from-usd17-high-rpm-cordless-air-dusters-are-great-replacements-for-canned-air-to-blast-away-the-dust-and-dirt",
    "domain": "AI 算力 / 半导体",
    "title": "Keep your gaming keyboard and PC fans clean with these electric air blower deals, starting from $17 — high-RPM cordless air dusters are great replacements for canned air to blast away the dust and dir",
    "url": "https://www.tomshardware.com/peripherals/keep-your-gaming-keyboard-and-pc-fans-clean-with-these-electric-air-blower-deals-starting-from-usd17-high-rpm-cordless-air-dusters-are-great-replacements-for-canned-air-to-blast-away-the-dust-and-dirt",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T09:21:30+00:00",
    "summary": "Prime Day is the perfect time to pick up an air blower to deal with grime and dust in your PC fans, keyboard keys, and elsewhere."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/rosewills-m-2-ssd-cloner-and-eraser-drops-to-its-lowest-ever-price-of-usd47-become-an-it-hero-or-just-save-yourself-some-time-and-frustration",
    "domain": "AI 算力 / 半导体",
    "title": "Rosewill’s M.2 SSD Cloner and Eraser drops to its lowest-ever price of $47 — become an IT hero, or just save yourself some time and frustration",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/rosewills-m-2-ssd-cloner-and-eraser-drops-to-its-lowest-ever-price-of-usd47-become-an-it-hero-or-just-save-yourself-some-time-and-frustration",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T08:20:16+00:00",
    "summary": "Clone and erase NVMe drives, offline, or connected to a PC, for less than $50."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-usd79-99-mini-lcd-screen-is-the-ultimate-retro-pc-gadget-and-its-on-sale-at-its-lowest-ever-price-3-5-inch-ips-display-includes-multiple-usb-ports-and-an-sd-card-reader-to-upgrade-your-desk-setup",
    "domain": "AI 算力 / 半导体",
    "title": "This $79.99 mini LCD screen is the ultimate retro PC gadget and it's on sale at its lowest-ever price — 3.5-inch IPS display includes multiple USB ports and an SD card reader to upgrade your desk setu",
    "url": "https://www.tomshardware.com/pc-components/this-usd79-99-mini-lcd-screen-is-the-ultimate-retro-pc-gadget-and-its-on-sale-at-its-lowest-ever-price-3-5-inch-ips-display-includes-multiple-usb-ports-and-an-sd-card-reader-to-upgrade-your-desk-setup",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T06:45:29+00:00",
    "summary": "Pick up this quirky retro mini monitor, with a built-in SD card reader and USB hub, for just $79.99 as a fun upgrade for your PC."
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/best-amazon-prime-day-deals-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Best Amazon Prime Day tech deals you can still get, live on day four — PC hardware deals on GPUs, CPUs, SSDs, and more",
    "url": "https://www.tomshardware.com/live/news/best-amazon-prime-day-deals-2026",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T06:34:44+00:00",
    "summary": "Find the very best PC hardware deals during Amazon Prime Day."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/prime-day-gaming-mouse-deals-round-up-up-your-game-with-a-new-mouse-on-sale",
    "domain": "AI 算力 / 半导体",
    "title": "Prime Day gaming mouse deals round-up — up your game with a new mouse on sale",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/prime-day-gaming-mouse-deals-round-up-up-your-game-with-a-new-mouse-on-sale",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T02:12:15+00:00",
    "summary": "We've rounded up the best Prime Day deals on gaming mice for every type of gamer — whether you're looking for ultra-lightweight, tons of buttons, or even modular mice, we've got you covered."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/asus-offers-up-to-36-percent-off-its-zenwifi-mesh-routers-tri-band-wi-fi-7-mesh-routers-starting-from-usd297-for-prime-day",
    "domain": "AI 算力 / 半导体",
    "title": "Asus offers up to 36% off its ZenWiFi mesh routers — tri-band Wi-Fi 7 mesh routers starting from $297",
    "url": "https://www.tomshardware.com/networking/routers/asus-offers-up-to-36-percent-off-its-zenwifi-mesh-routers-tri-band-wi-fi-7-mesh-routers-starting-from-usd297-for-prime-day",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T01:28:58+00:00",
    "summary": "Asus is taking up to 36% off its ZenWiFi mesh Wi-Fi 7 routers."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/nintendo-switch-2-is-once-again-usd399-at-woot-for-new-customers-usd419-for-returning-customers-with-code-save-up-to-usd50-while-supplies-last",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo Switch 2 is once again $399 at Woot for new customers, $419 for returning customers with code — save up to $50 while supplies last",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/nintendo-switch-2-is-once-again-usd399-at-woot-for-new-customers-usd419-for-returning-customers-with-code-save-up-to-usd50-while-supplies-last",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T00:33:25+00:00",
    "summary": "Get a brand new Nintendo Switch 2 for less."
  },
  {
    "id": "rss:https://www.eetimes.com/the-rise-of-autonomous-drone-warfare/",
    "domain": "AI 算力 / 半导体",
    "title": "The Rise of Autonomous Drone Warfare",
    "url": "https://www.eetimes.com/the-rise-of-autonomous-drone-warfare/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T22:14:58+00:00",
    "summary": "Cheap, autonomous drones developed in Ukraine are driving a new era of drone-on-drone warfare. The post The Rise of Autonomous Drone Warfare appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/deep-uv-lithography-processing-the-best-kept-secret-of-euv-lithography/",
    "domain": "AI 算力 / 半导体",
    "title": "Deep UV Lithography Processing, the Best Kept Secret of EUV Lithography",
    "url": "https://www.eetimes.com/deep-uv-lithography-processing-the-best-kept-secret-of-euv-lithography/",
    "source": "Drew Chambers",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T15:35:14+00:00",
    "summary": "EUV grabs the glory, but DUV does the dirty work that keeps advanced chips alive. The post Deep UV Lithography Processing, the Best Kept Secret of EUV Lithography appeared first on EE Times."
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
    "id": "rss:https://www.theverge.com/gadgets/949350/amazon-prime-day-sale-best-apple-deals-2026",
    "domain": "大厂 AI 动态",
    "title": "Prime Day is almost over, but these are still the best Apple deals I&#8217;ve seen",
    "url": "https://www.theverge.com/gadgets/949350/amazon-prime-day-sale-best-apple-deals-2026",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T02:56:52+00:00",
    "summary": "Amazon&#8217;s Prime Day is now in its final hours, but whether you&#8217;re looking for a new pair of wireless earbuds or a smartwatch, there’s a good chance you’ll still find a discount. The Apple W"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/957435/prime-day-2026-best-tech-deals-sale-day-four",
    "domain": "大厂 AI 动态",
    "title": "It’s the last day of Prime Day — here are over 140 great deals to choose from",
    "url": "https://www.theverge.com/gadgets/957435/prime-day-2026-best-tech-deals-sale-day-four",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T02:54:45+00:00",
    "summary": "We’ve arrived at the final day of Prime Day, which at this point should probably be called “Prime Week.” We’ve found discounts on all manner of gadgets, including TVs, smart home tech, chargers, headp"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/954880/amazon-prime-day-2026-popular-products-verge-readers",
    "domain": "大厂 AI 动态",
    "title": "24 Prime Day deals Verge readers are grabbing before Prime Day ends",
    "url": "https://www.theverge.com/gadgets/954880/amazon-prime-day-2026-popular-products-verge-readers",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T02:33:54+00:00",
    "summary": "There are an overwhelming number of Prime Day deals to sort through, which is why we spend so much time highlighting products we&#8217;ve already tested and can stand behind. But our recommendations a"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/951081/robot-vacuum-mop-deals-amazon-prime-day-2026",
    "domain": "大厂 AI 动态",
    "title": "The 17 best robot vacuum deals you can still get before Prime Day ends",
    "url": "https://www.theverge.com/gadgets/951081/robot-vacuum-mop-deals-amazon-prime-day-2026",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T00:42:42+00:00",
    "summary": "If you&#8217;ve been wanting to buy a robot vacuum but have been put off by how much it can cost to get a good one, now is not a bad time to start looking. We&#8217;re now on the final day of Prime Da"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/958458/anthropic-mythos-5-is-back-trump-negotiations",
    "domain": "大厂 AI 动态",
    "title": "Anthropic&#8217;s Mythos 5 is back",
    "url": "https://www.theverge.com/ai-artificial-intelligence/958458/anthropic-mythos-5-is-back-trump-negotiations",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T00:33:44+00:00",
    "summary": "After a rollercoaster negotiation process with the Trump administration that dragged on for two weeks, Anthropic's Mythos 5 is finally back in action - at least, somewhat, for a select group of organi"
  },
  {
    "id": "rss:https://www.theverge.com/tech/957269/philips-hue-amazon-prime-day-2026-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Prime Day&#8217;s final hours bring rare discounts on Philips Hue smart lights",
    "url": "https://www.theverge.com/tech/957269/philips-hue-amazon-prime-day-2026-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T00:20:50+00:00",
    "summary": "Philips Hue products don&#8217;t often see major discounts, which makes this year&#8217;s Prime Day deals especially notable. Prices have dropped significantly across much of the company&#8217;s smart"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/958313/govee-table-lamp-2-classic-floor-uplighter-prime-day-2026-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "My favorite Govee smart lamps are at their lowest prices ever for Prime Day",
    "url": "https://www.theverge.com/gadgets/958313/govee-table-lamp-2-classic-floor-uplighter-prime-day-2026-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T22:51:28+00:00",
    "summary": "We&#8217;ve already rounded up the best Philips Hue deals of Prime Day, but if you&#8217;re looking for something a little more budget-friendly, Govee&#8217;s latest sale is worth checking out. The co"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/958179/prime-day-what-i-bought-vampliers-stripped-screw-extractor",
    "domain": "大厂 AI 动态",
    "title": "After covering Prime Day for 36 hours over four days, this is the one thing I bought",
    "url": "https://www.theverge.com/gadgets/958179/prime-day-what-i-bought-vampliers-stripped-screw-extractor",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T22:09:46+00:00",
    "summary": "We&#8217;ve covered so many deals during Prime Day that my head is spinning. But after four days of doing our damndest to try and help folks save money, the thing I&#8217;m most hyped for is a simple "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/957473/prime-day-2026-fun-gadgets-under-100-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Our favorite Prime Day gadgets under $100 you don&#8217;t need but will really want",
    "url": "https://www.theverge.com/gadgets/957473/prime-day-2026-fun-gadgets-under-100-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T21:25:22+00:00",
    "summary": "Prime Day has a funny way of convincing you to buy things you weren&#8217;t shopping for in the first place. You sign on intending to buy something sensible you actually need, like a pack of USB-C cab"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/956830/prime-day-macbook-deals-apple-price-hikes",
    "domain": "大厂 AI 动态",
    "title": "These are the best deals you can still get on MacBooks before Apple&#8217;s price hike kicks in",
    "url": "https://www.theverge.com/gadgets/956830/prime-day-macbook-deals-apple-price-hikes",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T19:42:52+00:00",
    "summary": "Apple just raised the prices on Macs and iPads in response to the rising costs of memory chips, right in the middle of Amazon Prime Day. That means existing discounts (even small ones) on Apple laptop"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/26/trump-admin-releases-anthropic-mythos-to-be-used-by-more-than-100-us-companies-agencies/",
    "domain": "大厂 AI 动态",
    "title": "Trump Admin releases Anthropic Mythos to be used by more than 100 US companies, agencies",
    "url": "https://techcrunch.com/2026/06/26/trump-admin-releases-anthropic-mythos-to-be-used-by-more-than-100-us-companies-agencies/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T01:01:37+00:00",
    "summary": "Over 100 companies and government agencies are reportedly authorized to use Mythos 5, including their non-American employees."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/26/ftc-gives-musk-the-ok-to-acquire-spacex-alumni-startup-mesh/",
    "domain": "大厂 AI 动态",
    "title": "FTC gives Musk the OK to acquire SpaceX alumni startup Mesh",
    "url": "https://techcrunch.com/2026/06/26/ftc-gives-musk-the-ok-to-acquire-spacex-alumni-startup-mesh/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T00:38:34+00:00",
    "summary": "Mesh came out of stealth in February with a $50 million Series A."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/26/corgi-the-buzzy-y-combinator-backed-insurance-tech-startup-says-it-didnt-steal-an-open-source-product/",
    "domain": "大厂 AI 动态",
    "title": "Corgi, the buzzy Y Combinator-backed insurance tech startup, says it didn’t steal an open source product",
    "url": "https://techcrunch.com/2026/06/26/corgi-the-buzzy-y-combinator-backed-insurance-tech-startup-says-it-didnt-steal-an-open-source-product/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T22:00:37+00:00",
    "summary": "Corgi became embroiled in controversy when Papermark accused it of stealing its software. Corgi says it did not, raising new questions about vibe coding."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/26/novak-djokovic-has-a-new-job-advisor-to-private-equity-firm-general-atlantic/",
    "domain": "大厂 AI 动态",
    "title": "Novak Djokovic has a new job — advisor to private equity firm General Atlantic",
    "url": "https://techcrunch.com/2026/06/26/novak-djokovic-has-a-new-job-advisor-to-private-equity-firm-general-atlantic/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T19:13:40+00:00",
    "summary": "General Atlantic has tapped tennis legend Novak Djokovic to serve as a global strategic advisor."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/26/openai-limits-gpt-5-6-rollout-after-government-request-says-restrictions-shouldnt-be-the-norm/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI limits GPT-5.6 rollout after government request, says restrictions shouldn’t be the norm",
    "url": "https://techcrunch.com/2026/06/26/openai-limits-gpt-5-6-rollout-after-government-request-says-restrictions-shouldnt-be-the-norm/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T18:32:14+00:00",
    "summary": "“We don’t believe this kind of government access process should become the long-term default,” says OpenAI. “It keeps the best tools from users, developers, enterprises, cyber defenders, and global pa"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/26/openai-poaches-uber-india-chief-to-lead-its-biggest-market-outside-the-u-s/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI poaches Uber India chief to lead its biggest market outside the US",
    "url": "https://techcrunch.com/2026/06/26/openai-poaches-uber-india-chief-to-lead-its-biggest-market-outside-the-u-s/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T18:19:36+00:00",
    "summary": "The hire marks OpenAI's latest push into India, expanding offices, partnerships and hiring."
  },
  {
    "id": "rss:https://techcrunch.com/video/why-everyone-from-openai-to-spacex-is-building-their-own-chips-and-turning-up-the-heat-on-nvidia/",
    "domain": "大厂 AI 动态",
    "title": "Why everyone from OpenAI to SpaceX is building their own chips (and turning up the heat on Nvidia)",
    "url": "https://techcrunch.com/video/why-everyone-from-openai-to-spacex-is-building-their-own-chips-and-turning-up-the-heat-on-nvidia/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T17:43:22+00:00",
    "summary": "Nvidia has dominated the AI chip market for years, but the era of total dependence might be ending.&#160;&#160; OpenAI just shared its plans to spice things up with&#160;Jalapeño, its custom inference"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/26/russian-hackers-were-behind-2-5-billion-hack-of-jaguar-land-rover-report/",
    "domain": "大厂 AI 动态",
    "title": "Russian hackers were behind $2.5B hack of Jaguar Land Rover: Report",
    "url": "https://techcrunch.com/2026/06/26/russian-hackers-were-behind-2-5-billion-hack-of-jaguar-land-rover-report/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T17:29:29+00:00",
    "summary": "The hack on car giant Jaguar Land Rover last year was one of the most disrupting, damaging, and costly hacks of the last few years."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/26/tesla-settles-fsd-crash-lawsuit-as-federal-investigations-continue/",
    "domain": "大厂 AI 动态",
    "title": "Tesla settles FSD crash lawsuit as federal investigations continue",
    "url": "https://techcrunch.com/2026/06/26/tesla-settles-fsd-crash-lawsuit-as-federal-investigations-continue/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T16:32:55+00:00",
    "summary": "The lawsuit was connected to a fatal 2023 crash involving a vehicle using the company's advanced driver assistance system known as Full Self-Driving."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/26/tiktoks-road-to-becoming-a-super-app/",
    "domain": "大厂 AI 动态",
    "title": "TikTok’s road to becoming a super app",
    "url": "https://techcrunch.com/2026/06/26/tiktoks-road-to-becoming-a-super-app/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T16:29:48+00:00",
    "summary": "TikTok may be working to become the app that people use for most of their digital activities."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/26/its-not-about-anthropic-vs-openai-anymore/",
    "domain": "大厂 AI 动态",
    "title": "It’s not about Anthropic vs. OpenAI anymore",
    "url": "https://techcrunch.com/2026/06/26/its-not-about-anthropic-vs-openai-anymore/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T16:24:47+00:00",
    "summary": "AI models have progressed to the point where their capabilities have real political consequences. Dealing with those consequences will require collective action."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/26/xprize-founder-says-humans-behave-better-when-theyre-being-watched/",
    "domain": "大厂 AI 动态",
    "title": "Xprize founder says ‘humans behave better when they’re being watched’",
    "url": "https://techcrunch.com/2026/06/26/xprize-founder-says-humans-behave-better-when-theyre-being-watched/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T15:46:05+00:00",
    "summary": "Peter Diamandis is the latest tech executive to argue that global surveillance will make the world a better place, following Larry Ellison's comments in 2024."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/26/this-silicon-valley-startup-has-raised-10m-to-build-pitstops-to-clean-and-charge-robotaxis/",
    "domain": "大厂 AI 动态",
    "title": "Robotaxis drive miles just to get cleaned and charged; this new startup wants to fix that",
    "url": "https://techcrunch.com/2026/06/26/this-silicon-valley-startup-has-raised-10m-to-build-pitstops-to-clean-and-charge-robotaxis/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T13:00:00+00:00",
    "summary": "Aseon Labs, which came out of Y Combinator's 2026 spring cohort, has raised $10 million from Crane Venture Partners and others."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/26/early-bird-pricing-ends-tonight-for-techcrunch-founder-summit/",
    "domain": "大厂 AI 动态",
    "title": "Early Bird pricing ends tonight for TechCrunch Founder Summit",
    "url": "https://techcrunch.com/2026/06/26/early-bird-pricing-ends-tonight-for-techcrunch-founder-summit/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T13:00:00+00:00",
    "summary": "Save up to $190 on your pass to TechCrunch Founder Summit 2026. Early Bird pricing ends today, at 11:59 p.m. PT, after which rates increase. Register now."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/the-white-house-is-asking-openai-to-slow-roll-the-release-of-its-new-model-over-safety-concerns/",
    "domain": "大厂 AI 动态",
    "title": "The White House is asking OpenAI to slow roll the release of its new model over safety concerns",
    "url": "https://techcrunch.com/2026/06/25/the-white-house-is-asking-openai-to-slow-roll-the-release-of-its-new-model-over-safety-concerns/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T23:34:39+00:00",
    "summary": "OpenAI reportedly plans to share its newest model, GPT 5.6, with a select group of partners instead of with the broader public. The reason: the Trump administration told it to."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/youtube-shorts-are-getting-even-shorter-with-an-update-that-lets-you-double-the-playback-speed/",
    "domain": "大厂 AI 动态",
    "title": "YouTube Shorts are getting even shorter with an update that lets you double the playback speed",
    "url": "https://techcrunch.com/2026/06/25/youtube-shorts-are-getting-even-shorter-with-an-update-that-lets-you-double-the-playback-speed/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T22:02:12+00:00",
    "summary": "YouTube Shorts is getting a makeover."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/patronus-ai-lands-50m-to-build-digital-worlds-that-stress-test-ai-agents/",
    "domain": "大厂 AI 动态",
    "title": "Patronus AI lands $50M to build ‘digital worlds’ that stress-test AI agents",
    "url": "https://techcrunch.com/2026/06/25/patronus-ai-lands-50m-to-build-digital-worlds-that-stress-test-ai-agents/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T20:19:25+00:00",
    "summary": "Agent-testing startup Patronus AI, founded by former Meta AI researchers, is experiencing nearly insatiable demand, its investor says."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/polymarket-says-hackers-stole-users-funds/",
    "domain": "大厂 AI 动态",
    "title": "Polymarket says hackers stole users’ funds",
    "url": "https://techcrunch.com/2026/06/25/polymarket-says-hackers-stole-users-funds/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T19:58:46+00:00",
    "summary": "The prediction market giant Polymarket said it's refunding users who had funds stolen due to a third-party breach."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/xbox-follows-apple-with-price-increases/",
    "domain": "大厂 AI 动态",
    "title": "Xbox follows Apple with price increases",
    "url": "https://techcrunch.com/2026/06/25/xbox-follows-apple-with-price-increases/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T19:39:55+00:00",
    "summary": "The company says the increases are being driven by rising memory and console storage prices, with costs more than 2.5x higher than previous levels."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/notion-mail-shuts-down-amid-agent-takeover/",
    "domain": "大厂 AI 动态",
    "title": "Notion Mail shuts down amid agent takeover",
    "url": "https://techcrunch.com/2026/06/25/notion-mail-shuts-down-amid-agent-takeover/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T19:14:46+00:00",
    "summary": "The company said it is discontinuing its email inbox in favor of its AI agent offering as users are increasingly handing over the reins of their email to the agents."
  },
  {
    "id": "rss:https://stratechery.com/2026/summer-vibes/",
    "domain": "大厂 AI 动态",
    "title": "2026.26: Summer Vibes",
    "url": "https://stratechery.com/2026/summer-vibes/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of June 22, 2026, including a vibe coding adventure, Apple in Europe, and a midsummer mailbag."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-figma-ceo-dylan-field-about-design-and-ai/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with Figma CEO Dylan Field About Design and AI",
    "url": "https://stratechery.com/2026/an-interview-with-figma-ceo-dylan-field-about-design-and-ai/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T10:00:00+00:00",
    "summary": "An interview with Figma CEO Dylan Field about building Figma, and why he believes AI gives the company a tailwind."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/south-korea-plans-to-train-entire-military-as-drone-warriors/",
    "domain": "大厂 AI 动态",
    "title": "South Korea plans to train entire military as \"drone warriors\"",
    "url": "https://arstechnica.com/ai/2026/06/south-korea-plans-to-train-entire-military-as-drone-warriors/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T22:19:05+00:00",
    "summary": "Half-million strong military will train on drones as “universal combat tool.”"
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/06/doctors-suspected-man-had-brain-cancer-he-actually-had-worms/",
    "domain": "大厂 AI 动态",
    "title": "Doctors suspected man had brain cancer. He actually had worms.",
    "url": "https://arstechnica.com/health/2026/06/doctors-suspected-man-had-brain-cancer-he-actually-had-worms/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T21:43:57+00:00",
    "summary": "His doctors went looking for cancer, then they saw the worms' heads."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/streaming-services-obnoxiously-loud-ads-become-illegal-on-july-1-in-california/",
    "domain": "大厂 AI 动态",
    "title": "Streaming services’ obnoxiously loud ads become illegal on July 1 in California",
    "url": "https://arstechnica.com/gadgets/2026/06/streaming-services-obnoxiously-loud-ads-become-illegal-on-july-1-in-california/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T21:12:07+00:00",
    "summary": "Illinois passed a similar law, giving services more incentive to make ads less booming."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/russian-citizens-told-switch-to-android-after-apple-blocks-key-russian-apps/",
    "domain": "大厂 AI 动态",
    "title": "Russian citizens told \"switch to Android\" after Apple blocks key Russian apps",
    "url": "https://arstechnica.com/gadgets/2026/06/russian-citizens-told-switch-to-android-after-apple-blocks-key-russian-apps/",
    "source": "Nate Anderson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T20:58:02+00:00",
    "summary": "Russian government lashes out at Apple's \"bizarre\" decisions."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/microsoft-built-supercomputer-to-help-openai-infringe-copyrights-nyt-alleged/",
    "domain": "大厂 AI 动态",
    "title": "NYT slams Microsoft for building copyright-infringing supercomputer for OpenAI",
    "url": "https://arstechnica.com/tech-policy/2026/06/microsoft-built-supercomputer-to-help-openai-infringe-copyrights-nyt-alleged/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T20:04:55+00:00",
    "summary": "NYT shifts OpenAI/Microsoft copyright claims after SCOTUS ruling against Sony."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/fcc-accused-of-hiding-chairman-carrs-messages-with-doge-and-musk/",
    "domain": "大厂 AI 动态",
    "title": "FCC accused of hiding Chairman Carr's messages with DOGE and Musk",
    "url": "https://arstechnica.com/tech-policy/2026/06/fcc-accused-of-hiding-chairman-carrs-messages-with-doge-and-musk/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T18:51:04+00:00",
    "summary": "FCC refuses to provide messages, has \"wasted a year\" of court's time, filing says."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/netflix-now-requires-every-user-profile-to-be-tied-to-unique-email-address/",
    "domain": "大厂 AI 动态",
    "title": "Netflix now requires every user profile to be tied to unique email address",
    "url": "https://arstechnica.com/gadgets/2026/06/netflix-now-requires-every-user-profile-to-be-tied-to-unique-email-address/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T18:19:58+00:00",
    "summary": "Update began June 15 and will no longer allow you to share your login info."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/06/antibiotic-megacluster-discovery-provides-new-strategy-to-fight-superbugs/",
    "domain": "大厂 AI 动态",
    "title": "Antibiotic \"megacluster\" discovery provides new strategy to fight superbugs",
    "url": "https://arstechnica.com/health/2026/06/antibiotic-megacluster-discovery-provides-new-strategy-to-fight-superbugs/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T17:46:07+00:00",
    "summary": "It's \"an exciting advance in efforts to restock the antibiotic arsenal.\""
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/ars-live-whats-the-latest-in-the-aftermath-of-the-new-glenn-catastrophe/",
    "domain": "大厂 AI 动态",
    "title": "Ars Live: What's the latest in the aftermath of the New Glenn catastrophe?",
    "url": "https://arstechnica.com/space/2026/06/ars-live-whats-the-latest-in-the-aftermath-of-the-new-glenn-catastrophe/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T16:24:59+00:00",
    "summary": "Join us on the livestream at 1 pm ET and ask questions about the aftermath of New Glenn."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/06/vw-may-close-four-factories-to-adapt-to-the-future-report-says/",
    "domain": "大厂 AI 动态",
    "title": "VW may close four factories to adapt to the future, report says",
    "url": "https://arstechnica.com/cars/2026/06/vw-may-close-four-factories-to-adapt-to-the-future-report-says/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T15:10:03+00:00",
    "summary": "With falling sales in the US and especially China, VW Group wants to restructure."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/feedbacks-upon-feedbacks-rock-weathering-and-the-climate/",
    "domain": "大厂 AI 动态",
    "title": "Feedbacks upon feedbacks: Rock weathering and the climate",
    "url": "https://arstechnica.com/science/2026/06/feedbacks-upon-feedbacks-rock-weathering-and-the-climate/",
    "source": "Howard Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T14:41:18+00:00",
    "summary": "Rock weathering may release or draw down carbon dioxide—it depends on the rock."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/spacex-plans-to-launch-starlink-mobile-service-in-the-us/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX plans to launch Starlink mobile service in the US",
    "url": "https://arstechnica.com/space/2026/06/spacex-plans-to-launch-starlink-mobile-service-in-the-us/",
    "source": "Kieran Smith, George Steer, James Fontanella-Khan, and Michelle Chan, Financial Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T13:22:59+00:00",
    "summary": "Move would test whether group can turn ambition into a mass-market phone business."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/rocket-report-china-may-soon-attempt-booster-landing-rocket-lab-does-rapid-response/",
    "domain": "大厂 AI 动态",
    "title": "Rocket Report: China may soon attempt booster landing; Rocket Lab does rapid response",
    "url": "https://arstechnica.com/space/2026/06/rocket-report-china-may-soon-attempt-booster-landing-rocket-lab-does-rapid-response/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T11:00:59+00:00",
    "summary": "Is SpaceX planning to end its Transporter program?"
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/microsoft-adds-another-year-to-windows-10-extended-update-program/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft adds another year to Windows 10 extended update program",
    "url": "https://arstechnica.com/gadgets/2026/06/microsoft-adds-another-year-to-windows-10-extended-update-program/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T20:24:09+00:00",
    "summary": "About a quarter of PCs are still running Microsoft's previous operating system."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/fcc-may-kill-2b-program-that-connects-schools-and-libraries-to-internet/",
    "domain": "大厂 AI 动态",
    "title": "FCC may kill $2B program that connects schools and libraries to Internet",
    "url": "https://arstechnica.com/tech-policy/2026/06/fcc-may-kill-2b-program-that-connects-schools-and-libraries-to-internet/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T20:01:08+00:00",
    "summary": "Carr cites screen time concerns, is accused of trying to be \"the nation’s parent.\""
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/notion-killing-skiff-influenced-email-app-since-most-users-use-ai-agents-instead/",
    "domain": "大厂 AI 动态",
    "title": "Notion killing Skiff-influenced email app since most users use AI agents instead",
    "url": "https://arstechnica.com/gadgets/2026/06/notion-killing-skiff-influenced-email-app-since-most-users-use-ai-agents-instead/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T19:04:57+00:00",
    "summary": "Notion is \"going all in on using agents to run your inbox.\""
  },
  {
    "id": "rss:https://arstechnica.com/google/2026/06/google-finance-finally-gets-a-mobile-app-as-ai-powered-overhaul-leaves-beta/",
    "domain": "大厂 AI 动态",
    "title": "Google finally releases a Finance Android app, promises iOS version later in 2026",
    "url": "https://arstechnica.com/google/2026/06/google-finance-finally-gets-a-mobile-app-as-ai-powered-overhaul-leaves-beta/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T18:38:51+00:00",
    "summary": "It took 20 years, but the Finance app arrives just in time to be packed full of AI."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/anthropic-claims-alibaba-defied-trump-to-attack-claude-and-steal-capabilities/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic says Alibaba must be punished for largest Claude cloning attack",
    "url": "https://arstechnica.com/tech-policy/2026/06/anthropic-claims-alibaba-defied-trump-to-attack-claude-and-steal-capabilities/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T18:01:48+00:00",
    "summary": "Alibaba allegedly used 25,000 accounts to mine Claude over 28.8 million exchanges."
  },
  {
    "id": "wscn:3775671",
    "domain": "股票",
    "title": "太空算力真火，创企3个月融资已3轮",
    "url": "https://wallstreetcn.com/articles/3775671",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T05:55:10+00:00",
    "summary": "太空算力新星轨道辰光三个月内完成三轮密集融资，累计获超577亿元银行授信及多家顶尖机构投资，硬科技赛道融资节奏与规模均创行业纪录。"
  },
  {
    "id": "wscn:3775665",
    "domain": "股票",
    "title": "IPO后又天量发债“惹毛”市场，SpaceX债券直逼“垃圾级”，跌速之快让交易员惊讶",
    "url": "https://wallstreetcn.com/articles/3775665",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T04:07:05+00:00",
    "summary": "SpaceX 250亿美元债券发行后48小时内遭遇猛烈抛售，10年期债券利差扩大至1.6个百分点以上，长端债券利差逼近垃圾级水平，账面损失约4亿美元。此次暴跌源于快钱套利退出、公司持续亏损及治理风险。这折射出更广泛的科技债务泡沫隐患，AI相关债务发行同比激增357%，信用市场承压加剧。"
  },
  {
    "id": "wscn:3775666",
    "domain": "股票",
    "title": "签了协议也没用？特朗普：欧洲敢征数字税，就加100%关税",
    "url": "https://wallstreetcn.com/articles/3775666",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T03:11:20+00:00",
    "summary": "特朗普周五警告，任何对美国企业征收数字服务税的国家将立即面临100%关税，且该关税凌驾于任何贸易协议之上。他称多个欧洲国家已接近实施此类税收。欧盟表示将“迅速果断”反制。白宫计划援引1974年《贸易法》第301条作为法律依据，此举被视为绕开最高法院违宪裁定的替代路径。"
  },
  {
    "id": "wscn:3775650",
    "domain": "股票",
    "title": "OpenAI发布GPT-5.6系列模型，Sol基准测试超越Claude Mythos，应美政府要求限量开放",
    "url": "https://wallstreetcn.com/articles/3775650",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T02:52:19+00:00",
    "summary": "GPT-5.6系列包括旗舰版Sol、兼顾效率与日常工作的Terra、快速且低价版Luna，定价最高的Sol收费为5美元/百万输入token 、30美元/百万输出token，只有Anthropic Fable 5模型的一半左右，旗舰版Sol在智能体编程基准上超越Mythos 5。但这一轮模型发布因美国政府介入而显得与众不同。OpenAI称，目前GPT-5.6仅向有限数量的可信合作伙伴开放预览，计划未"
  },
  {
    "id": "wscn:3775667",
    "domain": "股票",
    "title": "中国5月规模以上工业企业利润同比增长21.1%，计算机、通信和其他电子设备制造业前五个月大增103.9%",
    "url": "https://wallstreetcn.com/articles/3775667",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T02:13:03+00:00",
    "summary": "1—5月份，有色金属冶炼和压延加工业利润同比增长117.1%，计算机、通信和其他电子设备制造业增长103.9%。电子行业与原材料制造业是本轮利润增长的主要支撑力量，前者受益于全球人工智能技术变革带动的芯片需求爆发，后者则受新能源及AI产业需求拉动，铜、铝等有色金属价格维持高位。"
  },
  {
    "id": "wscn:3775663",
    "domain": "股票",
    "title": "“OpenAI推迟上市”之下：甲骨文、Nebius带头硬件股下跌，ServiceNow和Workday领衔软件股全线大涨",
    "url": "https://wallstreetcn.com/articles/3775663",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T01:42:22+00:00",
    "summary": "OpenAI财务困境或推迟IPO，引发市场重估AI冲击预期。软件股ServiceNow、Workday涨逾9%，Figma涨超10%，昔日\"重灾区\"领涨。分析师指出，企业全面用AI替代软件的说法不切实际，最悲观时刻或已过去。"
  },
  {
    "id": "wscn:3775664",
    "domain": "股票",
    "title": "美股连跌的“核心逻辑”:“最大权重”Mag 7陨落",
    "url": "https://wallstreetcn.com/articles/3775664",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T01:18:06+00:00",
    "summary": "Mag 7本周重挫6%，并拖累纳指跌约4%。同时，Mag 7本月市值蒸发约3万亿美元，相关ETF 6月跌13%，创史上最差月度表现。AI投入高企但回报不明，叠加芯片、算力等“AI受益方”板块崛起，Mag 7领导地位承压。分析称这更像拥挤头寸出清，非全面去风险，但波动料将持续。"
  },
  {
    "id": "wscn:3775668",
    "domain": "股票",
    "title": "澳大利亚旅游局延续“来澳大利亚，道一声G’day”品牌叙事",
    "url": "https://wallstreetcn.com/articles/3775668",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T01:16:40+00:00",
    "summary": "澳大利亚旅游局宣布在中国市场延续并深化“来澳大利亚，道一声G’day”（Come and say G..."
  },
  {
    "id": "wscn:3775662",
    "domain": "股票",
    "title": "欧盟明显缺乏诚意，中方做好反制准备，中欧正密集举行贸易磋商",
    "url": "https://wallstreetcn.com/articles/3775662",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T00:52:35+00:00",
    "summary": "据环球时报，欧盟在解决中方关切问题上缺乏诚意。例如，双方就中国企业电动汽车价格承诺具体谈判没有取得新进展。在出口管制方面，欧方要求中方解决欧盟在稀土方面的关切，但在解决中国自欧盟进口遇阻个案方面没有取得任何进展。"
  },
  {
    "id": "wscn:3775661",
    "domain": "股票",
    "title": "370万亿日元投资计划背后的财政魔术，高市早苗“过桥国债”引发赤字担忧",
    "url": "https://wallstreetcn.com/articles/3775661",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T00:42:56+00:00",
    "summary": "为规避增税阻力，高市早苗政府引入\"过桥国债\"机制，并以模糊\"税外收入\"作为偿还来源。财政专家警告，该机制本质上是变相赤字国债，将进一步恶化日本本已高企的债务状况。"
  },
  {
    "id": "wscn:3775659",
    "domain": "股票",
    "title": "AI监管松绑！报道：美国放行Anthropic最强模型，超100家机构获准使用",
    "url": "https://wallstreetcn.com/articles/3775659",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T00:09:05+00:00",
    "summary": "据媒体报道，美国政府周五宣布解除对该公司Claude Mythos 5模型的出口限制，允许超过100家获政府批准的企业和联邦机构访问该模型。同样遭到封禁的另一旗舰模型Fable 5的限制并未在此次解除之列，出口禁令仍然有效。"
  },
  {
    "id": "wscn:3775571",
    "domain": "股票",
    "title": "半导体拖累美股，标普、纳指五连跌，美光跌6%，金银走高，原油一度跌4%",
    "url": "https://wallstreetcn.com/articles/3775571",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T23:31:06+00:00",
    "summary": "标普500指数创下去年8月来最长的连跌纪录。费城半导体指数重挫5.3%。安森美半导体暴跌23%。2年期美债收益率走低3基点。美元走V仍跌0.15%，本周站稳101关口上方。Solana最近24小时大涨10%。现货黄金一度较日低涨2.8%。白银日内反弹2%。纽约油价自美伊战事以来首次跌破70美元。"
  },
  {
    "id": "wscn:3775660",
    "domain": "股票",
    "title": "华尔街见闻早餐FM-Radio | 2026年6月27日",
    "url": "https://wallstreetcn.com/articles/3775660",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T23:30:58+00:00",
    "summary": "五分钟看懂全球市场，尽在财经早餐。"
  },
  {
    "id": "wscn:3775657",
    "domain": "股票",
    "title": "苹果再失大将！报道：Vision Pro与智能眼镜掌舵人转投OpenAI",
    "url": "https://wallstreetcn.com/articles/3775657",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T22:43:45+00:00",
    "summary": "据媒体报道，苹果Vision Pro和智能眼镜业务最高主管Paul Meade将于本周离职加入OpenAI。智能眼镜被视为苹果切入AI可穿戴赛道、对抗Meta的关键产品。消息公布后，曾导致苹果股价周五盘中涨幅收窄，不过后续涨势重启，最终收涨3.14%。此前苹果CEO更迭触发高层架构调整，Meade及多名硬件负责人遭到降级。"
  },
  {
    "id": "wscn:3775655",
    "domain": "股票",
    "title": "美联储独立性再受冲击：亚特兰大联储行长遴选陷僵局，白宫寻机介入",
    "url": "https://wallstreetcn.com/articles/3775655",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T22:43:30+00:00",
    "summary": "“新美联储通讯社”Nick Timiraos撰文指出，亚特兰大联储行长遴选已历时七个月陷入僵局，而该职位明年将获FOMC利率决策投票权。同时本无正式介入权限的白宫顾问正试图影响这一任命，力推亲政府候选人，令外界对美联储政治独立性的担忧再度升温。"
  },
  {
    "id": "wscn:3775658",
    "domain": "股票",
    "title": "AI交易退潮席卷科技股：安森美暴跌24%，甲骨文创2001年来最大周跌，七巨头全线周跌",
    "url": "https://wallstreetcn.com/articles/3775658",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T22:40:03+00:00",
    "summary": "宣布70亿美元收购Synaptics进军物理AI后，安森美周五创将近六年来最大日跌。甲骨文本周累跌逾19%。“科技七巨头”中，五连跌的英伟达和谷歌本周累跌近9%，微软周五收涨近6%、全周仍跌近2%。SpaceX上市第二周跌超17%，抹平首周涨幅。"
  },
  {
    "id": "wscn:3775656",
    "domain": "股票",
    "title": "IPO承诺加速落地！马斯克获批收购光通信企业Mesh，推进太空算力战略",
    "url": "https://wallstreetcn.com/articles/3775656",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T21:47:32+00:00",
    "summary": "马斯克已获监管机构批准，收购光通信企业Mesh。Mesh表示，其光学收发器与现有方案相比具有更高能效与更低延迟。Mesh由前星链工程师创立，表示希望未来将其技术应用于太空领域，这与SpaceX IPO期间向投资者描述的太空算力战略高度契合。"
  },
  {
    "id": "wscn:3775654",
    "domain": "股票",
    "title": "美伊签协议后美军首次开火，称空袭伊朗回应商船在霍尔木兹遭袭，伊方称挫败美袭击、将严厉回应",
    "url": "https://wallstreetcn.com/articles/3775654",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T21:41:05+00:00",
    "summary": "美军称，伊朗袭击商船显然违反停火协议，美军将继续为商船提供安全通航方面支援，确保协议“全面有效”执行。原油收窄跌幅，美油跌不足3%。伊媒称周五晚伊朗南部港口城市锡里克的码头传爆炸声。伊军方称将迅速且果断回应美方袭击，“任何新的愚蠢行为”都将遭严厉回应。"
  },
  {
    "id": "wscn:3775652",
    "domain": "股票",
    "title": "黎以美达成三方框架协议，以总理：黎真主党解除武装前，以军将驻留黎南部“安全区”",
    "url": "https://wallstreetcn.com/articles/3775652",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T21:03:19+00:00",
    "summary": "以色列官员称，在“安全区”内，以军将保留军事行动自由，可随时采取行动消除潜在的安全威胁；以色列和黎巴嫩同意，在“安全区”以外的两个地区，以色列逐步撤军并由黎巴嫩政府军接管控制。鲁比奥称，设立美国推动的军事协调小组协助落实三方框架协议。黎巴嫩总统：达成框架协议是恢复黎主权的第一步。"
  },
  {
    "id": "wscn:3775653",
    "domain": "股票",
    "title": "沃什首批重要任命之一：任命两位美联储经济学家为顾问，聚焦利率研究",
    "url": "https://wallstreetcn.com/articles/3775653",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T20:46:22+00:00",
    "summary": "“新美联储通讯社”Nick Timiraos撰文指出，美联储新任主席沃什从内部擢升两位深耕近三十年的资深经济学家Covitz与Engstrom出任核心顾问。两人研究方向为金融稳定、信贷市场与货币政策等，曾联合研究揭示美债长端利率走高背后的供给冲击与财政赤字逻辑。"
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
  }
]
```
