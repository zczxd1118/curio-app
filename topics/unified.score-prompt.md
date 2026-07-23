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

- 今日日期：`2026-07-23`
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
  "date": "2026-07-23",
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
    "points": 3854567,
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
    "points": 1583161,
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
    "points": 1454009,
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
    "points": 1265753,
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
    "points": 938201,
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
    "points": 936901,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1mhKv68EPQ",
    "domain": "AI",
    "title": "豆包真能干活了！【豆包Agent入门教程】",
    "url": "http://www.bilibili.com/video/av116944258728161",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 805290,
    "published_at": "2026-07-19T03:00:00+00:00",
    "summary": "这个视频让你的豆包技能噌噌上涨，还有“秋芝AI科普skill”帮你答疑～\n感谢朋友们的三连+关注~"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 556338,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 514530,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 426161,
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
    "points": 418236,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 345906,
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
    "points": 289068,
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
    "points": 245761,
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
    "points": 199586,
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
    "points": 177669,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 168917,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 162282,
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
    "points": 160141,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 148805,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 145407,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 103732,
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
    "points": 101834,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92701,
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
    "points": 79861,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53260,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 35092,
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
    "points": 33889,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1xzGH6uEG8",
    "domain": "AI",
    "title": "AI全自动化搭建复杂Simulink模型！5步即可完成部署，全流程分享！",
    "url": "http://www.bilibili.com/video/av116629870481178",
    "source": "电气攻城狮001",
    "platform": "bilibili",
    "points": 30553,
    "published_at": "2026-05-24T13:50:56+00:00",
    "summary": "本期分享五步实操流程，借助 Claude Code 交互载体接入 DeepSeek 大模型，搭配 2026.5.21 最新版 Simulink Agentic Toolkit，解锁 68 项建模技能。依次完成 API 额度配置、环境部署、工具包安装，连通校验后开启全自动模式。无需手动拖拽模块与布线，输入指令即可依托 Simscape 蓝库，在 MATLAB2026a 中自动搭建三相并网逆变器开环模"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 30197,
    "published_at": "2026-05-07T00:00:00+00:00",
    "summary": "全栈课一共分为6大块内容\n第一块：AI智能体开发基础(AI大模型、工具、记忆、MCP、中间件、Skills等核心内容)\n第二块：Claude Code,Trea+skills实现基于需求文档生成用例，基于OpenClaw实现接口自动化落地，基于hermes Agent实现web自动化落地\n第三块：功能测试的智能体开发(项目RAG知识库搭建+Agent搭建+skills开发，实现用例生成的Agent"
  },
  {
    "id": "bvid:BV1vwXPYkEGx",
    "domain": "AI",
    "title": "Cursor+mcp配置，手把手教你配置任意MCP服务，学不会你打我，小白保姆级教程~MCP服务配置指南 - 提升AI编程助手能力",
    "url": "http://www.bilibili.com/video/av114193181183930",
    "source": "三少科技",
    "platform": "bilibili",
    "points": 27043,
    "published_at": "2025-03-20T05:51:23+00:00",
    "summary": "我的知识星球，https://t.zsxq.com/jVAk9\n\n📌 本期教程通过实战演示，教你在Cursor中配置和使用MCP服务器，特别是filesystem MCP服务，解决Cursor无法写入文件的常见问题。\n⏱️ 内容概要：\n00:00 介绍MCP及其重要性\n02:00 Cursor抽风问题与MCP解决方案\n04:00 配置第一个MCP服务器（filesystem）\n07:00 Wind"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22642,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1nf42127MW",
    "domain": "AI",
    "title": "用AI Agent做一个法律咨询助手，罗老看了都直呼内行 feat.通义千问大模型&amp;阿里云百炼平台",
    "url": "http://www.bilibili.com/video/av1204786228",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 21280,
    "published_at": "2024-05-21T05:09:48+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17609,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 16872,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 15924,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV14cZqB8EBY",
    "domain": "AI",
    "title": "AI攻克不了的领域竟然是它？揭秘CNC编程为何让AI束手无策",
    "url": "http://www.bilibili.com/video/av116097411976217",
    "source": "极微视界",
    "platform": "bilibili",
    "points": 14659,
    "published_at": "2026-02-19T12:59:23+00:00",
    "summary": "CNC编程AI化有多难？本视频深度解析为什么AI编程在制造业进展缓慢。\n从材料、刀具、机床到隐性知识，揭秘老师傅的经验为什么无法数字化。\nPowerMill、CloudNC等AI编程软件的真实水平如何？CNC编程师的未来在哪里？\n\n⏱️ 时间轴 Timestamps:\n\n00:00 开篇：AI在CNC领域的困境\n00:20 材料的复杂性：为什么同样是45#钢参数却不同\n01:01 刀具与机床的个体"
  },
  {
    "id": "bvid:BV1HFRgBvEVv",
    "domain": "AI",
    "title": "claude接入小米mimo模型基础教程（无claude安装教程）",
    "url": "http://www.bilibili.com/video/av116499343738499",
    "source": "栉旎",
    "platform": "bilibili",
    "points": 13438,
    "published_at": "2026-05-01T12:37:49+00:00",
    "summary": "claude接入小米mimo模型全流程，"
  },
  {
    "id": "bvid:BV1RMorB7EZy",
    "domain": "AI",
    "title": "【AI教程】目前B站最全最细的VibeCoding系统教程，不用精通代码也能上手，2026最新版，包含所有干货！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116476107363692",
    "source": "大模型零基础入门-",
    "platform": "bilibili",
    "points": 12479,
    "published_at": "2026-04-27T10:13:31+00:00",
    "summary": "【AI教程】目前B站最全最细的VibeCoding系统教程，不用精通代码也能上手，2026最新版，包含所有干货！少走99%的弯路！学完即就业，带你玩转AI！"
  },
  {
    "id": "bvid:BV1vLN769EJa",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！大模型入门到进阶，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116894866677118",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 10333,
    "published_at": "2026-07-10T09:04:48+00:00",
    "summary": "【代码已整理】\n无论你是从零开始开发项目，还是对现有代码进行现代化改造，本课程都能为你提供一套严谨的工作流程，让你按自己的方式构建软件。"
  },
  {
    "id": "bvid:BV1ubK26aEbJ",
    "domain": "AI",
    "title": "【AI】这绝对是2026b站讲的最好的Agent Skill保姆级教程！AI大模型/Multi-Agent/Tool/WorkFlow/Agent/智能体架构",
    "url": "http://www.bilibili.com/video/av116950214778812",
    "source": "大模型饼饼",
    "platform": "bilibili",
    "points": 9795,
    "published_at": "2026-07-20T03:42:16+00:00",
    "summary": "如果视频对你有用的话，一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套资料+问题解答+请看评论区置顶领取哦】"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9215,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 8725,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 7860,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV138Ng6wEEj",
    "domain": "AI",
    "title": "【2026版】这绝对是B站讲的最好的Vibe Coding企业级项目实战，90分钟速通Claude Code、Codex，Cursor、AI工程化编程实战开发！",
    "url": "http://www.bilibili.com/video/av116905822259723",
    "source": "图灵架构师诸葛",
    "platform": "bilibili",
    "points": 7083,
    "published_at": "2026-07-12T07:30:41+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持~\n【本视频笔记代码/学习大纲/全套面试真题/系统学习/实战案例等请戳链接获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 7003,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "bvid:BV1S9Et6yEL8",
    "domain": "AI",
    "title": "claude code在量化交易方面的应用",
    "url": "http://www.bilibili.com/video/av116709008606912",
    "source": "xxy的大迷弟",
    "platform": "bilibili",
    "points": 6952,
    "published_at": "2026-06-07T13:19:31+00:00",
    "summary": "AI或者量化方面的交流可以邮箱交流：965418170@qq.com"
  },
  {
    "id": "bvid:BV1u4G9zmEte",
    "domain": "AI",
    "title": "什么是MCP？VS Code中使用MCP Server",
    "url": "http://www.bilibili.com/video/av114426032168712",
    "source": "AI落地派",
    "platform": "bilibili",
    "points": 6618,
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based o"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6560,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV19XqMBzENU",
    "domain": "AI",
    "title": "Cursor + OpenCode 最佳开源 AI 编程工具",
    "url": "http://www.bilibili.com/video/av115851978146202",
    "source": "独立开发者_猫哥",
    "platform": "bilibili",
    "points": 6494,
    "published_at": "2026-01-07T04:47:17+00:00",
    "summary": "OpenCode 是一款面向开发者的开源 AI CLI 编程工具，支持多模型并行、LSP 自动加载、极速响应与非订阅制计费。无论是命令行、桌面 App 还是 VS Code 插件，OpenCode 都提供高效、不啰嗦的 AI 编程体验，是 Cursor 与 Claude Code 的有力替代方案。"
  },
  {
    "id": "hn:48873836",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, CoreWeave, and Nebius: Inside the Circular Financing of the GPU Boom",
    "url": "https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom",
    "source": "adletbalzhanov",
    "platform": "hackernews",
    "points": 370,
    "published_at": "2026-07-11T17:21:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48903715",
    "domain": "AI 算力 / 半导体",
    "title": "Alternative(s) to run CUDA on non-Nvidia hardware",
    "url": "https://www.hpcwire.com/2026/07/09/spectral-compute-aims-to-set-cuda-free-will-it-succeed/",
    "source": "alok-g",
    "platform": "hackernews",
    "points": 143,
    "published_at": "2026-07-14T08:24:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48971128",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia DGX Spark as a daily driver",
    "url": "https://daniel.lawrence.lu/blog/2026-07-15-dgx-spark-as-daily-driver/",
    "source": "plun9",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-07-19T19:44:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:49012431",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia released its first official GeForce driver for Windows on Arm",
    "url": "https://videocardz.com/newz/nvidias-first-geforce-driver-for-windows-on-arm-confirms-rtx-spark-n1x-with-6144-or-5120-cuda-cores",
    "source": "robotnikman",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-22T19:49:57+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/from-rhetoric-to-metrics-raghib-hussain-first-year-as-altera-ceo/",
    "domain": "AI 算力 / 半导体",
    "title": "From Rhetoric to Metrics: Raghib Hussain’s First Year as Altera CEO",
    "url": "https://www.eetimes.com/from-rhetoric-to-metrics-raghib-hussain-first-year-as-altera-ceo/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T22:00:00+00:00",
    "summary": "Altera has taped out six chips in nine months, three ahead of schedule, as new CEO focuses on execution. The post From Rhetoric to Metrics: Raghib Hussain’s First Year as Altera CEO appeared first on "
  },
  {
    "id": "rss:https://www.eetimes.com/ai-in-eda-is-real-its-now-and-its-on-show-at-dac-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "AI in EDA Is Real, It’s Now, and It’s on Show at DAC 2026",
    "url": "https://www.eetimes.com/ai-in-eda-is-real-its-now-and-its-on-show-at-dac-2026/",
    "source": "Frank Schirrmeister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T18:00:00+00:00",
    "summary": "AI in chip design has left the slide deck and hit DAC 2026’s floor—walk the stack and test the hype. The post AI in EDA Is Real, It’s Now, and It’s on Show at DAC 2026 appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/cea-leti-looks-beyond-sram-and-dram-as-ai-reshapes-the-memory-roadmap/",
    "domain": "AI 算力 / 半导体",
    "title": "CEA-Leti Looks Beyond SRAM and DRAM as AI Reshapes the Memory Roadmap",
    "url": "https://www.eetimes.com/cea-leti-looks-beyond-sram-and-dram-as-ai-reshapes-the-memory-roadmap/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T07:53:34+00:00",
    "summary": "CEA-Leti’s François Andrieu describes more embedded, persistent, and low-energy memories that will meet the growing demands of AI. The post CEA-Leti Looks Beyond SRAM and DRAM as AI Reshapes the Memor"
  },
  {
    "id": "rss:https://www.eetimes.com/sk-hynix-nasdaq-debut-shows-global-memory-expansion-race/",
    "domain": "AI 算力 / 半导体",
    "title": "SK Hynix Nasdaq Debut Shows Global Memory Expansion Race",
    "url": "https://www.eetimes.com/sk-hynix-nasdaq-debut-shows-global-memory-expansion-race/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T20:10:00+00:00",
    "summary": "SK Hynix Nasdaq debut highlights capex-funded memory expansion. Both Samsung and Micron follow suit. The post SK Hynix Nasdaq Debut Shows Global Memory Expansion Race appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/how-quantum-computing-earns-its-place-in-the-data-center/",
    "domain": "AI 算力 / 半导体",
    "title": "How Quantum Computing Earns Its Place in the Data Center",
    "url": "https://www.eetimes.com/how-quantum-computing-earns-its-place-in-the-data-center/",
    "source": "Zeynep Korutürk, Kris Naudts, Donald Harmitt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T13:08:25+00:00",
    "summary": "Quantum won’t win in labs; it must survive racks, cooling, power and networks. The post How Quantum Computing Earns Its Place in the Data Center appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/carbon-nanotube-firm-strengthens-executive-team-to-build-cnt-ecosystem/",
    "domain": "AI 算力 / 半导体",
    "title": "Carbon Nanotube Firm Strengthens Executive Team to Build CNT Ecosystem",
    "url": "https://www.eetimes.com/carbon-nanotube-firm-strengthens-executive-team-to-build-cnt-ecosystem/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T07:00:00+00:00",
    "summary": "Canatu stacks its C-suite to push CNTs into chips, cars, and diagnostics—watch how its new CEO plans to turn nanotube hype into yield. The post Carbon Nanotube Firm Strengthens Executive Team to Build"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/framework-nearly-doubles-memory-pricing-for-32gb-64gb-laptop-13-pro-overnight-ceo-says-absorbing-lpcamm2-supplier-hikes-would-put-our-ability-to-operate-at-real-financial-risk",
    "domain": "AI 算力 / 半导体",
    "title": "Framework nearly doubles memory pricing for 32GB, 64GB Laptop 13 Pro overnight — CEO says absorbing LPCAMM2 supplier hikes would put 'our ability to operate at real financial risk'",
    "url": "https://www.tomshardware.com/laptops/framework-nearly-doubles-memory-pricing-for-32gb-64gb-laptop-13-pro-overnight-ceo-says-absorbing-lpcamm2-supplier-hikes-would-put-our-ability-to-operate-at-real-financial-risk",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T20:50:46+00:00",
    "summary": "The company is making adjustments to some existing pre-orders."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-argues-american-companies-should-be-allowed-to-use-chinese-ai-models-nvidia-ceo-says-backdoors-connected-to-china-are-misconceptions",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang argues American companies should be allowed to use Chinese AI models — Nvidia CEO says backdoors connected to China are misconceptions",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-argues-american-companies-should-be-allowed-to-use-chinese-ai-models-nvidia-ceo-says-backdoors-connected-to-china-are-misconceptions",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T17:55:46+00:00",
    "summary": "Nvidia CEO Jensen Huang raised several points against the rising sentiment in Washington that U.S. firms should be prevented from accessing Chinese AI models. He also advocates for open models, which "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-4-gets-its-first-foundry-customer-in-fortinet-three-years-after-intel-scoped-the-node-to-meteor-lake",
    "domain": "AI 算力 / 半导体",
    "title": "Fortinet becomes Intel 4's first foundry customer, following firewall ASIC deal — CEO Lip-Bu Tan's promised foundry wins begin to surface, but on a mature node",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-4-gets-its-first-foundry-customer-in-fortinet-three-years-after-intel-scoped-the-node-to-meteor-lake",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T16:17:41+00:00",
    "summary": "Intel will design, package, and fabricate Fortinet's sixth-generation Security Processor (SP6) on its Intel 4 node."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/microsoft-announces-xbox-backward-compatibility-for-pc-will-let-gamers-play-classic-console-games-on-pcs-and-handhelds",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft announces Xbox Backward Compatibility for PC — will let gamers play classic console games on PCs and handhelds",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/microsoft-announces-xbox-backward-compatibility-for-pc-will-let-gamers-play-classic-console-games-on-pcs-and-handhelds",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T16:09:52+00:00",
    "summary": "Xbox Backward Compatibility on PC will let gamers play classic Xbox games on PC and handheld."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/usb/usbs-next-decade",
    "domain": "AI 算力 / 半导体",
    "title": "The future of USB connectivity (2026) — How USB4 Version 2 and Thunderbolt 5 are bringing copper to its physical limits",
    "url": "https://www.tomshardware.com/peripherals/usb/usbs-next-decade",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T15:40:28+00:00",
    "summary": "The USB ecosystem is entering another transition that will affect how laptops, desktops, storage devices, displays, and peripherals connect in the second half of the decade."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/amd-to-supply-anthropic-with-2-gigawatts-of-instinct-mi450-gpus",
    "domain": "AI 算力 / 半导体",
    "title": "AMD to supply Anthropic with 2 gigawatts of Instinct MI450 GPUs — will invest up to $5 billion in the Claude developer, which is already using MI355X GPUs",
    "url": "https://www.tomshardware.com/tech-industry/amd-to-supply-anthropic-with-2-gigawatts-of-instinct-mi450-gpus",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T15:38:58+00:00",
    "summary": "The first gigawatt is scheduled to come online in the first half of 2027 in AMD Helios rack-scale systems."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/bnef-nearly-doubles-its-us-data-center-power-forecast-to-194gw",
    "domain": "AI 算力 / 半导体",
    "title": "Data centers forecast to use 20% of US power by 2035 — analysts estimate usage will rocket to 194 gigawatts, 83% more than forecast seven months ago",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/bnef-nearly-doubles-its-us-data-center-power-forecast-to-194gw",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T14:21:58+00:00",
    "summary": "BNEF's December outlook put 2035 demand at 106 GW, and that figure was itself 36% above the projection the firm published in April 2025."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/apple-reportedly-working-on-mac-leasing-program-in-partnership-with-klarna-to-fight-ram-price-increases-apple-upgrade-would-let-users-finance-hardware-over-36-months-budget-models-excluded",
    "domain": "AI 算力 / 半导体",
    "title": "Apple reportedly working on Mac leasing program in partnership with Klarna to fight RAM price increases — 'Apple Upgrade' would let users finance hardware over 36 months, budget models excluded",
    "url": "https://www.tomshardware.com/tech-industry/apple-reportedly-working-on-mac-leasing-program-in-partnership-with-klarna-to-fight-ram-price-increases-apple-upgrade-would-let-users-finance-hardware-over-36-months-budget-models-excluded",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T13:34:36+00:00",
    "summary": "A new Bloomberg report is claiming that Apple is working on a leasing program called \"Apple Upgrade\" that will allow customers to finance hardware over the course of 2 or 3 years. At the end of the te"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/ai-tech-companies-have-hidden-debt-worth-around-usd1-65-trillion-report-claims-amount-is-122-percent-of-debt-reflected-on-the-balance-sheets-of-alphabet-amazon-meta-microsoft-and-oracle",
    "domain": "AI 算力 / 半导体",
    "title": "AI tech companies have ‘hidden debt’ worth around $1.65 trillion, report claims — amount is 122% of debt reflected on the balance sheets of Alphabet, Amazon, Meta, Microsoft, and Oracle",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/ai-tech-companies-have-hidden-debt-worth-around-usd1-65-trillion-report-claims-amount-is-122-percent-of-debt-reflected-on-the-balance-sheets-of-alphabet-amazon-meta-microsoft-and-oracle",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T13:23:33+00:00",
    "summary": "Five tech giants have $1.65 trillion in data center obligations that are listed off their balance sheets. These liabilities are added as footnotes in their quarterly statements but will become due and"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/chinese-modder-gets-geforce-rtx-4060-working-in-windows-11-on-huawei-arm-workstation-uses-modified-driver-borrowed-from-an-nvidia-rtx-spark",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese modder gets GeForce RTX 4060 working in Windows 11 on Huawei Arm workstation — uses modified driver borrowed from an Nvidia RTX Spark",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/chinese-modder-gets-geforce-rtx-4060-working-in-windows-11-on-huawei-arm-workstation-uses-modified-driver-borrowed-from-an-nvidia-rtx-spark",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T13:18:38+00:00",
    "summary": "Borrowing a driver from the upcoming RTX Spark, VoidTech managed to get x86 Windows games running on a Huawei Arm workstation."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/meta-to-use-custom-amd-instinct-mi400-accelerators-with-144gb-of-hbm4-for-select-workloads-report-claims-could-dramatically-reduce-cost-at-the-expense-of-versatility",
    "domain": "AI 算力 / 半导体",
    "title": "Meta to use custom AMD Instinct MI400 accelerators with 144GB of HBM4 for select workloads, report claims — could dramatically reduce cost at the expense of versatility",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/meta-to-use-custom-amd-instinct-mi400-accelerators-with-144gb-of-hbm4-for-select-workloads-report-claims-could-dramatically-reduce-cost-at-the-expense-of-versatility",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T11:36:15+00:00",
    "summary": "Meta will reportedly use a custom version of AMD's Instinct MI400-series accelerators with a memory system cut to 144GB of HBM4, allegedly for select workloads only."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/this-usd1-399-5070-gaming-laptop-is-one-of-the-best-value-deals-around-save-usd700-on-16-inch-model-with-32gb-of-ram-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Woot has slashed $600 off this RTX 5070 gaming laptop — get a Gigabyte Aero X16 with 32GB of RAM and Ryzen HX 370 for just $1,399",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/this-usd1-399-5070-gaming-laptop-is-one-of-the-best-value-deals-around-save-usd700-on-16-inch-model-with-32gb-of-ram-and-a-1tb-ssd",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T11:06:29+00:00",
    "summary": "Get a Gigabyte Aero X16 with RTX 5070, 32GB of RAM, 1TB SSD, and AMD Ryzen AI 9 HX 370 for $1,399."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/just-usd1-399-for-this-potent-rtx-5060-ti-16gb-powered-gaming-pc-32gb-of-ddr5-ram-and-amds-7800x3d-to-help-you-crush-the-competition",
    "domain": "AI 算力 / 半导体",
    "title": "Just $1,399 for this potent RTX 5060 Ti 16GB-powered gaming PC — 32GB of DDR5 RAM and AMD's 7800X3D to help you crush the competition",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/just-usd1-399-for-this-potent-rtx-5060-ti-16gb-powered-gaming-pc-32gb-of-ddr5-ram-and-amds-7800x3d-to-help-you-crush-the-competition",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T11:06:19+00:00",
    "summary": "Save $600 on this Skytech Gaming King 95 prebuilt gaming PC with Ryzen 7 7800X3D, RTX 5060 Ti 16GB, and 32GB of DDR5 RAM inside."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/adata-chairman-says-dram-shortage-will-last-another-10-years",
    "domain": "AI 算力 / 半导体",
    "title": "Adata chairman says DRAM shortage will last another 10 years — dismisses AI bubble talk until '2040 or 2050'",
    "url": "https://www.tomshardware.com/tech-industry/adata-chairman-says-dram-shortage-will-last-another-10-years",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T11:00:00+00:00",
    "summary": "Electricity, particularly green power, and memory will be the world's two scarcest resources over the next decade, Chen said."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/playstation-3-emulator-adds-support-for-ati-radeon-hd-2000-3000-and-4000-series-graphics-cards-on-linux-20-year-old-hd-2600-crumbles-can-only-run-portal-at-13-fps-in-273p",
    "domain": "AI 算力 / 半导体",
    "title": "PlayStation 3 emulator adds support for ATI Radeon HD 2000, 3000, and 4000 series graphics cards on Linux — 20-year-old HD 2600 crumbles, can only run Portal at 13 fps in 273p",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/playstation-3-emulator-adds-support-for-ati-radeon-hd-2000-3000-and-4000-series-graphics-cards-on-linux-20-year-old-hd-2600-crumbles-can-only-run-portal-at-13-fps-in-273p",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T10:49:01+00:00",
    "summary": "The developers of the RPCS3 have announced that their PlayStation 3 emulator’s minimum system requirements have been adjusted to include a crop of even older Radeon graphics cards. Now gamers still cr"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/lucky-pc-gamer-scoops-insane-usd1-140-9800x3d-pc-at-costco-while-shopping-for-rotisserie-chicken-ibuypower-prebuilt-with-32gb-ram-and-rtx-5070-was-a-display-unit-discount",
    "domain": "AI 算力 / 半导体",
    "title": "Lucky PC gamer scoops insane $1,140 9800X3D PC at Costco while shopping for rotisserie chicken — iBuyPower prebuilt with 32GB RAM and RTX 5070 was a display unit discount",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/lucky-pc-gamer-scoops-insane-usd1-140-9800x3d-pc-at-costco-while-shopping-for-rotisserie-chicken-ibuypower-prebuilt-with-32gb-ram-and-rtx-5070-was-a-display-unit-discount",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T10:00:00+00:00",
    "summary": "What started as a routine Costco grocery run ended with a heavily discounted display gaming PC, complete with a Ryzen 7 9800X3D, RTX 5070, 32GB of DDR5 memory, and a 2TB SSD."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-gpt-5-6-sol-and-unreleased-ai-models-break-out-of-testing-environment-in-unprecedented-cybersecurity-incident-rogue-agents-hacked-huggingfaces-production-servers-with-thousands-of-individual-actions-across-a-swarm-of-short-lived-sandboxes",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI's GPT-5.6 Sol and unreleased AI models break out of testing environment in 'unprecedented cybersecurity incident' — rogue agents hacked HuggingFace's production servers with 'thousands of indiv",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-gpt-5-6-sol-and-unreleased-ai-models-break-out-of-testing-environment-in-unprecedented-cybersecurity-incident-rogue-agents-hacked-huggingfaces-production-servers-with-thousands-of-individual-actions-across-a-swarm-of-short-lived-sandboxes",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T09:23:35+00:00",
    "summary": "OpenAI's GPT-5.6 Sol and its gang escape from their cage and hack into HuggingFace's production servers — unprecedented incident raises eyebrows and pulses"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-shows-off-dlss-5-with-three-ai-modes-for-different-levels-of-detail-upscaler-can-switch-between-models-in-real-time",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia shows off DLSS 5 with three AI modes for different levels of detail — upscaler can switch between models in real-time",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-shows-off-dlss-5-with-three-ai-modes-for-different-levels-of-detail-upscaler-can-switch-between-models-in-real-time",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T17:46:05+00:00",
    "summary": "DLSS 5 gets a second showing with Nvidia opening up the upscaler to object-level tweaking for developers with three different models."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/china-is-considering-export-controls-on-ai-technologies-including-banning-local-companies-from-using-tsmc-report-claims-restrictions-would-also-advanced-ai-models-training-data-and-overseas-acquisitions",
    "domain": "AI 算力 / 半导体",
    "title": "China is considering export controls on AI technologies, including banning local companies from using TSMC, report claims — restrictions would also cover advanced AI models, training data, and oversea",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/china-is-considering-export-controls-on-ai-technologies-including-banning-local-companies-from-using-tsmc-report-claims-restrictions-would-also-advanced-ai-models-training-data-and-overseas-acquisitions",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T16:04:43+00:00",
    "summary": "China's Ministry of Commerce (MofCom) considers to restrict exports of advanced AI models, training data, and overseas acquisitions of strategically important technology companies; prohibit usage of f"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/amazon-data-center-in-bahrain-struck-and-destroyed-by-iranian-cruise-missiles-state-media-claims-attacks-launched-against-aws-site-in-response-to-alleged-us-strikes-on-an-under-construction-nuclear-plant",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon data center in Bahrain struck and destroyed by Iranian cruise missiles, state media claims — attacks launched against AWS site in response to alleged US strikes on an under-construction nuclear",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/amazon-data-center-in-bahrain-struck-and-destroyed-by-iranian-cruise-missiles-state-media-claims-attacks-launched-against-aws-site-in-response-to-alleged-us-strikes-on-an-under-construction-nuclear-plant",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T15:47:29+00:00",
    "summary": "The Amazon site has suffered multiple hits since the start of the U.S. bombing campaign in Iran. The IRGC claims to have 'destroyed' AWB Bahrain, but the company has moved operations off the facility "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/behind-the-scenes-at-nvidias-engineering-superlab-vera-rubin-nvl72-running-openai-workloads-800vdc-demonstrated-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Behind the scenes at Nvidia's Engineering SuperLab — Vera Rubin NVL72 running OpenAI workloads, 800VDC demonstrated, and more",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/behind-the-scenes-at-nvidias-engineering-superlab-vera-rubin-nvl72-running-openai-workloads-800vdc-demonstrated-and-more",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T15:15:00+00:00",
    "summary": "Nvidia gave Tom’s Hardware an exclusive look inside its previously undisclosed Engineering SuperLab near Nvidia HQ, where we saw Vera Rubin NVL72 in action."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-details-rubin-architectural-optimizations-for-inference-improvements-target-better-performance-and-efficiency-from-the-gpu-to-the-rack",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia details Rubin architectural optimizations for inference – improvements target better performance and efficiency from the GPU to the rack",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-details-rubin-architectural-optimizations-for-inference-improvements-target-better-performance-and-efficiency-from-the-gpu-to-the-rack",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T15:00:00+00:00",
    "summary": "Nvidia has detailed new features of its Rubin architecture."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nvidia-spills-the-beans-on-vera-cpu-spec-benchmarks-revealed-olympus-architecture-detailed-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia deep dives Vera CPU for AI data centers — SPEC CPU 2026 benchmarks revealed, Olympus architecture specifics, and more",
    "url": "https://www.tomshardware.com/pc-components/cpus/nvidia-spills-the-beans-on-vera-cpu-spec-benchmarks-revealed-olympus-architecture-detailed-and-more",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T15:00:00+00:00",
    "summary": "Nvidia reveals all of the details about its Vera data center CPU, including an architectural breakdown of the Olympus core and the first (unofficial) SPEC CPU 2026 results."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nvidia-has-shipped-hundreds-of-thousands-of-grace-standalone-servers-gpu-firm-pivots-messaging-as-cpus-take-center-stage-in-agentic-data-centers",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia has shipped 'hundreds of thousands of Grace standalone servers’ — GPU firm pivots messaging as CPUs take center stage in agentic data centers",
    "url": "https://www.tomshardware.com/pc-components/cpus/nvidia-has-shipped-hundreds-of-thousands-of-grace-standalone-servers-gpu-firm-pivots-messaging-as-cpus-take-center-stage-in-agentic-data-centers",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T15:00:00+00:00",
    "summary": "As Nvidia continues to roll out Vera, its first custom CPU for agentic AI, it revealed that its last-gen Grace design has seen mass deployments, even as a standalone CPU for non-agentic workloads."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/kimi-k3-rocks-the-ai-industry-as-moonshot-ai-undercuts-closed-source-american-competitors-on-price-but-the-huge-2-8t-open-weight-model-still-needs-serious-hardware-to-deploy-at-scale",
    "domain": "AI 算力 / 半导体",
    "title": "Kimi K3 rocks the AI industry as Moonshot AI undercuts closed-source American competitors on price — but the huge 2.8T open-weight model still needs serious hardware to deploy at scale",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/kimi-k3-rocks-the-ai-industry-as-moonshot-ai-undercuts-closed-source-american-competitors-on-price-but-the-huge-2-8t-open-weight-model-still-needs-serious-hardware-to-deploy-at-scale",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T14:59:54+00:00",
    "summary": "The trend towards larger AI models continues, with China's new Kimi K3 model. With its trillions of parameters, it's just as capable as the best the West has to offer, and it's cheaper. But it's not a"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/local-ai-clustering-with-dells-pro-max-gb10-connecting-two-nvidia-grace-blackwell-to-scale-out-ai-compute-at-home",
    "domain": "AI 算力 / 半导体",
    "title": "Local AI clustering with Dell's Pro Max GB10 — connecting two Nvidia Grace Blackwell to scale out AI compute at home",
    "url": "https://www.tomshardware.com/pc-components/gpus/local-ai-clustering-with-dells-pro-max-gb10-connecting-two-nvidia-grace-blackwell-to-scale-out-ai-compute-at-home",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T14:30:00+00:00",
    "summary": "We paired up and tested a pair of Dell's Pro Max with GB10, to see what a small cluster of Nvidia's Spark silicon can do. At $6332 each, as of writing, it's still an expensive prospect, but far cheape"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-slapped-with-usd1-5-billion-settlement-in-copyright-lawsuit-largest-payout-ever-court-says-that-training-ai-on-books-other-publications-is-fair-use-but-ruled-that-the-startups-7-million-book-pirated-library-infringes-authors-rights",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic hit with largest-ever $1.5 billion penalty in copyright lawsuit — court says training AI on published material is fair use, but startup’s pirated library infringes on authors’ rights",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-slapped-with-usd1-5-billion-settlement-in-copyright-lawsuit-largest-payout-ever-court-says-that-training-ai-on-books-other-publications-is-fair-use-but-ruled-that-the-startups-7-million-book-pirated-library-infringes-authors-rights",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T13:37:09+00:00",
    "summary": "The settlement was finally approved by a U.S. federal judge, with a majority of the plaintiffs accepting the amount. A few members of the group refused, citing the small amount compared to the number "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-to-co-develop-and-manufacture-fortinets-next-gen-firewall-asic",
    "domain": "AI 算力 / 半导体",
    "title": "Intel to co-develop and manufacture Fortinet's next-gen firewall ASIC on Intel 4 — node gets its first named external customer",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-to-co-develop-and-manufacture-fortinets-next-gen-firewall-asic",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T13:00:00+00:00",
    "summary": "SP6 will draw on what the companies described as Intel's expertise in disaggregated semiconductor design and advanced packaging."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/z-ai-powers-up-1gw-ai-data-center-built-entirely-on-chinese-chips",
    "domain": "AI 算力 / 半导体",
    "title": "Z.ai powers up a 1-gigawatt AI data center built entirely on Chinese chips, report claims — GLM developer now runs multiple 10,000-chip clusters with zero Nvidia silicon",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/z-ai-powers-up-1gw-ai-data-center-built-entirely-on-chinese-chips",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T12:44:53+00:00",
    "summary": "Chinese AI developer Z.ai (formerly Zhipu) has finished building a 1GW data center stocked exclusively with domestically made chips and has switched part of it on."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC eyes price hikes of up to 25% on chip production services in 2027, report claims — plans to raise baseline prices by 5% to 10% on advanced nodes",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T12:43:38+00:00",
    "summary": "TSMC reportedly intends to increase prices of wafers it processes citing demand, rising costs, and increased investments in new capacity."
  },
  {
    "id": "rss:https://www.eetimes.com/uma-the-architecture-edge-ai-needs-to-scale/",
    "domain": "AI 算力 / 半导体",
    "title": "UMA: The Architecture Edge AI Needs to Scale",
    "url": "https://www.eetimes.com/uma-the-architecture-edge-ai-needs-to-scale/",
    "source": "Chris Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T19:00:00+00:00",
    "summary": "Edge AI won’t be saved by more chips; it needs unified memory to stop models from choking mid-task. The post UMA: The Architecture Edge AI Needs to Scale appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/nisshinbo-micro-devices-expands-high-voltage-ic-lineup-for-next-gen-automotive-48-v-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Nisshinbo Micro Devices Expands High-Voltage IC Lineup for Next-Gen Automotive 48 V Systems",
    "url": "https://www.eetimes.com/nisshinbo-micro-devices-expands-high-voltage-ic-lineup-for-next-gen-automotive-48-v-systems/",
    "source": "Nisshinbo Micro Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T16:00:00+00:00",
    "summary": "Addressing the new challenges posed by the shift to 48 V automotive power supplies with Nisshinbo Micro Devices The post Nisshinbo Micro Devices Expands High-Voltage IC Lineup for Next-Gen Automotive "
  },
  {
    "id": "rss:https://www.eetimes.com/powering-the-automotive-revolution-from-zonal-architecture-to-48v/",
    "domain": "AI 算力 / 半导体",
    "title": "Powering the Automotive Revolution: From Zonal Architecture to 48V",
    "url": "https://www.eetimes.com/powering-the-automotive-revolution-from-zonal-architecture-to-48v/",
    "source": "Monolithic Power Systems, Inc. (MPS)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T13:30:36+00:00",
    "summary": "Explore how Monolithic Power Systems 48V automotive solutions, including the MPQ5884-AEC1, support safer, smarter, and more efficient zonal architecture. The post Powering the Automotive Revolution: F"
  },
  {
    "id": "rss:https://www.eetimes.com/photonics-components-the-eyes-and-ears-of-the-future-unmanned-system-and-connected-soldiers/",
    "domain": "AI 算力 / 半导体",
    "title": "Photonics Components – The Eyes and Ears of the Future Unmanned System and Connected Soldiers",
    "url": "https://www.eetimes.com/photonics-components-the-eyes-and-ears-of-the-future-unmanned-system-and-connected-soldiers/",
    "source": "Arrow Electronics, ams Osram",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T13:25:52+00:00",
    "summary": "Discover how optoelectronics plays a central role in sensing and data generation, including light-based distance measurement for UAVs and robotic platforms. The post Photonics Components &#8211; The E"
  },
  {
    "id": "hn:48894277",
    "domain": "AI 算力 / 半导体",
    "title": "Apple's rumored M7 Ultra targets 1.5TB and Blackwell-class AI performance",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/apples-rumored-m7-ultra-targets-1-5tb-of-memory-and-blackwell-class-ai",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-07-13T15:32:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48845518",
    "domain": "AI 算力 / 半导体",
    "title": "Reverse-engineering Nvidia's CUDA-checkpoint for faster cold starts",
    "url": "https://blog.doubleword.ai/what-happens-when-you-checkpoint-a-cuda-process",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-09T13:29:52+00:00",
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
    "points": 368,
    "published_at": "2026-07-15T18:40:34+00:00",
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
    "id": "hn:48998606",
    "domain": "大厂 AI 动态",
    "title": "Gemini last models: temperature, top_p, and top_k are deprecated and ignored",
    "url": "https://ai.google.dev/gemini-api/docs/latest-model",
    "source": "greatgib",
    "platform": "hackernews",
    "points": 129,
    "published_at": "2026-07-21T21:27:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48965880",
    "domain": "大厂 AI 动态",
    "title": "Ollama: All Aboard Open Models",
    "url": "https://ollama.com/blog/all-aboard-open-models",
    "source": "inferhaven",
    "platform": "hackernews",
    "points": 137,
    "published_at": "2026-07-19T07:59:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48993130",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.6 Flash",
    "url": "https://console.cloud.google.com/agent-platform/publishers/google/model-garden/gemini-3.6-flash",
    "source": "marrf",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-07-21T14:56:15+00:00",
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
    "id": "hn:48983890",
    "domain": "大厂 AI 动态",
    "title": "Cue AI",
    "url": "https://deepmind.google/models/gemma/gemmaverse/cue-ai/",
    "source": "logickkk1",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-20T19:41:44+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/969668/lego-donkey-kong-arcade-machine",
    "domain": "大厂 AI 动态",
    "title": "Lego’s Donkey Kong arcade machine lets Mario jump endless barrels — Miyamoto is reportedly happy",
    "url": "https://www.theverge.com/gadgets/969668/lego-donkey-kong-arcade-machine",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T00:30:00+00:00",
    "summary": "Carl Merriam has designed some of my favorite nostalgia-inducing Lego sets, including the Lego Nintendo Game Boy and Piranha Plant. He's assisted on the incredible Lion Knights' Castle, Galaxy Explore"
  },
  {
    "id": "rss:https://www.theverge.com/policy/969644/meta-social-media-addiction-trial-dropped",
    "domain": "大厂 AI 动态",
    "title": "Meta won’t have to face the next planned social media addiction trial",
    "url": "https://www.theverge.com/policy/969644/meta-social-media-addiction-trial-dropped",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T22:03:53+00:00",
    "summary": "Less than a week before Meta's lawyers were set to return to a Los Angeles courtroom, the plaintiff accusing the platform of inflicting harm dropped the case. Brought by 15-year-old Florida plaintiff "
  },
  {
    "id": "rss:https://www.theverge.com/transportation/969311/tesla-q2-2026-earnings-revenue-profit-sales",
    "domain": "大厂 AI 动态",
    "title": "Tesla’s revenues are bouncing back, but profits are still weak",
    "url": "https://www.theverge.com/transportation/969311/tesla-q2-2026-earnings-revenue-profit-sales",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T20:17:46+00:00",
    "summary": "After a dismal two years of weakening demand, falling sales, and damage to its brand by Elon Musk's political activities, Tesla's road to recovery continues apace. On the heels of an impressive delive"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/969003/apple-ipad-air-pro-airtag-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Price-hiked iPads are a little cheaper right now",
    "url": "https://www.theverge.com/gadgets/969003/apple-ipad-air-pro-airtag-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T19:14:31+00:00",
    "summary": "A number of Apple products got more expensive last month, so we’re happy to find deals wherever and whenever we can. If you’re searching for a high-end iPad, one of the more notable deals currently ha"
  },
  {
    "id": "rss:https://www.theverge.com/tech/969596/apple-restricted-mode-ios-27",
    "domain": "大厂 AI 动态",
    "title": "iOS code could reportedly let Apple cut off apps when users miss iPhone payments",
    "url": "https://www.theverge.com/tech/969596/apple-restricted-mode-ios-27",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T19:13:21+00:00",
    "summary": "Code found in an iOS 27 beta would allow Apple to put a financed iPhone in \"Restricted Mode\" if it detects any missed payments, 9to5Mac reports. The finding follows a story from Bloomberg earlier this"
  },
  {
    "id": "rss:https://www.theverge.com/tech/969434/apple-macbook-neo-a19-pro-ram-upgrade",
    "domain": "大厂 AI 动态",
    "title": "Apple is reportedly testing a MacBook Neo with more RAM",
    "url": "https://www.theverge.com/tech/969434/apple-macbook-neo-a19-pro-ram-upgrade",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T16:35:58+00:00",
    "summary": "Following the MacBook Neo's huge popularity so far, Apple is reportedly developing an updated version of its budget laptop with a new processor and more memory, and even has plans to refresh the model"
  },
  {
    "id": "rss:https://www.theverge.com/tech/969382/samsung-google-smart-glasses-gentle-monster-warby-parker",
    "domain": "大厂 AI 动态",
    "title": "Here&#8217;s what Samsung&#8217;s smart glasses actually look like",
    "url": "https://www.theverge.com/tech/969382/samsung-google-smart-glasses-gentle-monster-warby-parker",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T16:35:34+00:00",
    "summary": "Samsung has given us our first chance to check out its upcoming smart glasses in person, revealing two new designs and the first specs in the process, including an impressive 9-hour battery life. The "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/968682/samsung-galaxy-z-fold-flip-8-specs-features-hardware-comparison",
    "domain": "大厂 AI 动态",
    "title": "How the Galaxy Z Fold 8 and Z Flip 8 phones compare",
    "url": "https://www.theverge.com/gadgets/968682/samsung-galaxy-z-fold-flip-8-specs-features-hardware-comparison",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T15:47:10+00:00",
    "summary": "Samsung's latest round of folding Galaxy Z phones and updated smartwatches were announced at its July 2026 Unpacked event and are set to launch on August 7th. The Galaxy Z Flip 8, Fold 8, and Fold 8 U"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/968716/samsung-galaxy-z-flip-fold-8-ultra-how-to-buy-preorder-price-release-date",
    "domain": "大厂 AI 动态",
    "title": "Preorders for Samsung’s new Z Fold and Flip 8 come with up to $350 in gift cards",
    "url": "https://www.theverge.com/gadgets/968716/samsung-galaxy-z-flip-fold-8-ultra-how-to-buy-preorder-price-release-date",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T15:42:22+00:00",
    "summary": "Samsung's newest foldables are here. At Galaxy Unpacked, the company announced the Galaxy Z Flip 8, Galaxy Z Fold 8, and Galaxy Z Fold 8 Ultra. All three devices will be available on August 7th, but y"
  },
  {
    "id": "rss:https://www.theverge.com/tech/969271/philip-sonicare-next-generation-diamondclean-9900-prestige-ai-electric-toothbrush",
    "domain": "大厂 AI 动态",
    "title": "Philips’ new smart toothbrush shows you where you didn’t properly brush",
    "url": "https://www.theverge.com/tech/969271/philip-sonicare-next-generation-diamondclean-9900-prestige-ai-electric-toothbrush",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T15:09:44+00:00",
    "summary": "The latest addition to Philips' Sonicare line of smart electric toothbrushes could take the guesswork out of your brushing routine. The Next-Generation DiamondClean 9900 Prestige uses a third-generati"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/after-shocking-quarter-ibm-insists-that-ai-isnt-killing-the-mainframe/",
    "domain": "大厂 AI 动态",
    "title": "After shocking quarter, IBM insists that AI isn’t killing the mainframe",
    "url": "https://techcrunch.com/2026/07/22/after-shocking-quarter-ibm-insists-that-ai-isnt-killing-the-mainframe/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T23:47:54+00:00",
    "summary": "After IBM's stock crashed last week on warnings of poor mainframe sales, the CEO explained that AI wrecked corporate hardware budget, temporarily."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/google-justifies-its-massive-ai-spending-with-a-booming-cloud-business/",
    "domain": "大厂 AI 动态",
    "title": "Google justifies its massive AI spending with a booming cloud business",
    "url": "https://techcrunch.com/2026/07/22/google-justifies-its-massive-ai-spending-with-a-booming-cloud-business/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T22:01:52+00:00",
    "summary": "Google's cloud business is thriving, as companies adopting its AI and AI infrastructure services help the tech giant to report record profits."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/treasury-threatens-sanctions-after-white-house-claims-moonshot-distilled-anthropics-fable/",
    "domain": "大厂 AI 动态",
    "title": "Treasury threatens sanctions after White House claims Moonshot distilled Anthropic’s Fable",
    "url": "https://techcrunch.com/2026/07/22/treasury-threatens-sanctions-after-white-house-claims-moonshot-distilled-anthropics-fable/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T20:49:03+00:00",
    "summary": "The episode has also intensified a broader debate in Washington over the influx of Chinese open models."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/tesla-spending-skyrockets-as-cybercab-semi-megapack-production-timeline-slips/",
    "domain": "大厂 AI 动态",
    "title": "Tesla spending skyrockets as Cybercab, Semi, Megapack production timeline slips",
    "url": "https://techcrunch.com/2026/07/22/tesla-spending-skyrockets-as-cybercab-semi-megapack-production-timeline-slips/",
    "source": "Kirsten Korosec, Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T20:43:38+00:00",
    "summary": "Tesla's 26% boost in revenue wasn't enough to offset rising operating expenses and capital expenditures as it pushes to launch a new generation of products."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/social-media-addiction-lawsuit-against-meta-is-dropped/",
    "domain": "大厂 AI 动态",
    "title": "Social media addiction lawsuit against Meta is dropped",
    "url": "https://techcrunch.com/2026/07/22/social-media-addiction-lawsuit-against-meta-is-dropped/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T20:36:41+00:00",
    "summary": "A closely watched social media addiction lawsuit that had been set to go to trial next week has been dropped after the plaintiff voluntarily dismissed his claims against Meta, leaving none of the majo"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/soundcloud-acquires-decentralized-music-platform-nina-protocol-months-after-its-shutdown/",
    "domain": "大厂 AI 动态",
    "title": "SoundCloud acquires decentralized music platform Nina Protocol months after its shutdown",
    "url": "https://techcrunch.com/2026/07/22/soundcloud-acquires-decentralized-music-platform-nina-protocol-months-after-its-shutdown/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T19:42:56+00:00",
    "summary": "SoundCloud has acquired decentralized music platform Nina Protocol, months after the startup announced it would shut down. The deal brings Nina’s artists, editorial archive, and music discovery tools "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/how-an-openais-human-mistake-led-to-the-ai-powered-hack-on-hugging-face/",
    "domain": "大厂 AI 动态",
    "title": "How OpenAI’s human mistake led to the AI-powered hack on Hugging Face",
    "url": "https://techcrunch.com/2026/07/22/how-an-openais-human-mistake-led-to-the-ai-powered-hack-on-hugging-face/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T19:11:46+00:00",
    "summary": "OpenAI made a mistake setting up what it called a “highly isolated” testing environment and sandbox. According to cybersecurity experts, that human mistake is what made the AI-powered attack on Huggin"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/travis-kalanicks-robotics-company-raises-1-7b-led-by-a16z/",
    "domain": "大厂 AI 动态",
    "title": "Travis Kalanick’s robotics company raises $1.7B, led by a16z",
    "url": "https://techcrunch.com/2026/07/22/travis-kalanicks-robotics-company-raises-1-7b-led-by-a16z/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T18:50:44+00:00",
    "summary": "Uber is also investing in Travis Kalanick's company Atoms, which has made gauzy claims about using industrial AI to modernize the world."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/science-corporations-vision-restoring-chip-wins-eu-approval/",
    "domain": "大厂 AI 动态",
    "title": "Science Corporation’s vision-restoring chip wins EU approval",
    "url": "https://techcrunch.com/2026/07/22/science-corporations-vision-restoring-chip-wins-eu-approval/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T18:18:02+00:00",
    "summary": "\"The thing that the space needs is a company making $100 million a year of revenue,\" Science Corp. CEO Max Hodak said."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/yope-raises-12-3m-to-build-a-private-social-network-without-algorithms-or-ads/",
    "domain": "大厂 AI 动态",
    "title": "Yope raises $12.3M to build a private social network without algorithms or ads",
    "url": "https://techcrunch.com/2026/07/22/yope-raises-12-3m-to-build-a-private-social-network-without-algorithms-or-ads/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T18:13:58+00:00",
    "summary": "Yope, a fast-growing social app focused on private groups of friends and family, has raised $12.3 million in seed funding. Instead of chasing creators and algorithmic feeds, the startup is betting tha"
  },
  {
    "id": "rss:https://techcrunch.com/video/menlo-ventures-matt-murphy-explains-why-anthropic-is-winning-and-its-not-the-model/",
    "domain": "大厂 AI 动态",
    "title": "Menlo Ventures’ Matt Murphy explains why Anthropic is winning (and it’s not the model)",
    "url": "https://techcrunch.com/video/menlo-ventures-matt-murphy-explains-why-anthropic-is-winning-and-its-not-the-model/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T18:02:57+00:00",
    "summary": "Anthropic&#160;leaped to&#160;a&#160;$47 billion&#160;revenue run rate&#160;by May,&#160;compared to&#160;$9 billion&#160;in 2025.&#160;It’s&#160;the kind of growth that&#160;Menlo Ventures&#8217;&#16"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/monday-com-lays-off-hundreds-to-focuses-on-ai/",
    "domain": "大厂 AI 动态",
    "title": "Monday.com lays off hundreds to focus on AI",
    "url": "https://techcrunch.com/2026/07/22/monday-com-lays-off-hundreds-to-focuses-on-ai/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T17:54:14+00:00",
    "summary": "The company said it is reducing its headcount by 20%, or about 630 staff, to \"support a leaner, more focused operating model\" as it focuses on its AI Work Platform."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/google-is-making-it-easier-to-switch-from-iphone-to-android/",
    "domain": "大厂 AI 动态",
    "title": "Google is making it easier to switch from iPhone to Android",
    "url": "https://techcrunch.com/2026/07/22/google-is-making-it-easier-to-switch-from-iphone-to-android/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T17:08:03+00:00",
    "summary": "The new feature lets users wirelessly transfer more data types from an iPhone without needing to download a separate app."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/arcee-a-us-open-source-ai-lab-says-chinese-models-are-not-inherently-dangerous/",
    "domain": "大厂 AI 动态",
    "title": "Arcee, a US open source AI lab, says Chinese models are not inherently dangerous",
    "url": "https://techcrunch.com/2026/07/22/arcee-a-us-open-source-ai-lab-says-chinese-models-are-not-inherently-dangerous/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T16:24:08+00:00",
    "summary": "As Chinese AI models grow in capability and popularity among U.S. companies, the arguing over what should be done about them has reached a fever pitch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/substacks-new-tool-tells-you-whos-been-writing-their-newsletters-with-ai/",
    "domain": "大厂 AI 动态",
    "title": "Substack’s new tool tells you who’s been writing their newsletters with AI",
    "url": "https://techcrunch.com/2026/07/22/substacks-new-tool-tells-you-whos-been-writing-their-newsletters-with-ai/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T16:23:09+00:00",
    "summary": "Substack is giving readers a way to estimate how much of a newsletter was written by AI, signaling a broader shift toward transparency around AI-assisted content."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/openais-ai-spending-spree-has-ballooned-to-750b/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s AI spending spree has ballooned to $750B",
    "url": "https://techcrunch.com/2026/07/22/openais-ai-spending-spree-has-ballooned-to-750b/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T16:13:30+00:00",
    "summary": "OpenAI will spend the equivalent of Sweden's GDP on infrastructure through 2030."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/if-you-pay-a-hackers-ransom-chances-are-that-theyll-come-back-for-more/",
    "domain": "大厂 AI 动态",
    "title": "If you pay a hacker’s ransom, chances are that they’ll come back for more",
    "url": "https://techcrunch.com/2026/07/22/if-you-pay-a-hackers-ransom-chances-are-that-theyll-come-back-for-more/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T15:29:41+00:00",
    "summary": "The long-held understanding among security researchers and network defenders is that it's impossible to negotiate in good faith with an extortion racket because there's no incentive for the other side"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/cascade-raises-3-5m-to-help-construction-firms-find-and-win-projects/",
    "domain": "大厂 AI 动态",
    "title": "Cascade raises $3.5M to help construction firms find and win projects",
    "url": "https://techcrunch.com/2026/07/22/cascade-raises-3-5m-to-help-construction-firms-find-and-win-projects/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T13:28:36+00:00",
    "summary": "a16z Speedrun, Ada Ventures, and Snowball VC have invested in Cascade's $3.5 million seed round."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/as-the-browser-wars-heat-up-here-are-the-hottest-alternatives-to-chrome-and-safari-in-2026/",
    "domain": "大厂 AI 动态",
    "title": "The browser wars aren’t about search anymore — here are the best alternatives to Chrome and Safari",
    "url": "https://techcrunch.com/2026/07/22/as-the-browser-wars-heat-up-here-are-the-hottest-alternatives-to-chrome-and-safari-in-2026/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T13:20:35+00:00",
    "summary": "We’ve compiled an overview of some of the top alternative browsers available today aiming to challenge Chrome and Safari."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/22/passionfroot-raises-15m-to-expand-its-b2b-creator-marketplace-to-the-us/",
    "domain": "大厂 AI 动态",
    "title": "Passionfroot raises $15M to expand its B2B creator marketplace to the US",
    "url": "https://techcrunch.com/2026/07/22/passionfroot-raises-15m-to-expand-its-b2b-creator-marketplace-to-the-us/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T13:00:00+00:00",
    "summary": "Passionfroot, a German startup building a marketplace connecting B2B creators with brands, has raised $15M in a Series A round led by Insight Partners."
  },
  {
    "id": "rss:https://stratechery.com/2026/openai-hacks-hugging-face-what-happened-alignment-and-paper-clips/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI Hacks Hugging Face, What Happened, Alignment and Paper Clips",
    "url": "https://stratechery.com/2026/openai-hacks-hugging-face-what-happened-alignment-and-paper-clips/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T10:00:00+00:00",
    "summary": "OpenAI accidentally hacked Hugging Face, but the takeaways are more encouraging than people realize."
  },
  {
    "id": "rss:https://stratechery.com/2026/netflix-earnings-is-netflix-washed-additional-notes/",
    "domain": "大厂 AI 动态",
    "title": "Netflix Earnings, Is Netflix Washed?, Additional Notes",
    "url": "https://stratechery.com/2026/netflix-earnings-is-netflix-washed-additional-notes/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T10:00:00+00:00",
    "summary": "Netflix's earnings were fine, and befitting a mature company whose most exciting days are likely behind them."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/orcas-team-up-to-ram-sunfish-until-they-explode/",
    "domain": "大厂 AI 动态",
    "title": "Orcas team up to ram sunfish until they explode",
    "url": "https://arstechnica.com/science/2026/07/orcas-team-up-to-ram-sunfish-until-they-explode/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:38+00:00",
    "summary": "“We think this may help younger orcas feed more easily, or it could also just be for fun.”"
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/07/teslas-revenues-are-up-but-profits-squeezed-as-musk-spends-on-ai/",
    "domain": "大厂 AI 动态",
    "title": "Sales were up at Tesla but so were costs and spending",
    "url": "https://arstechnica.com/cars/2026/07/teslas-revenues-are-up-but-profits-squeezed-as-musk-spends-on-ai/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T21:15:19+00:00",
    "summary": "Q2 2026 was profitable, but barely."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/07/microsoft-brings-original-xbox-backward-compatibility-to-windows-pcs/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft brings original Xbox backward compatibility to Windows PCs",
    "url": "https://arstechnica.com/gaming/2026/07/microsoft-brings-original-xbox-backward-compatibility-to-windows-pcs/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T20:36:19+00:00",
    "summary": "First four compatible titles can be run with an 11-year-old graphics card."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/isps-long-nightmare-of-having-to-list-all-the-fees-they-charge-is-finally-over/",
    "domain": "大厂 AI 动态",
    "title": "ISPs' long nightmare of having to list all the fees they charge is finally over",
    "url": "https://arstechnica.com/tech-policy/2026/07/isps-long-nightmare-of-having-to-list-all-the-fees-they-charge-is-finally-over/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T20:17:18+00:00",
    "summary": "FCC lets ISPs stop listing all fees after companies complained it was too hard."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/07/clayface-trailer-leans-into-the-body-horror/",
    "domain": "大厂 AI 动态",
    "title": "Clayface trailer leans into the body horror",
    "url": "https://arstechnica.com/culture/2026/07/clayface-trailer-leans-into-the-body-horror/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T19:18:17+00:00",
    "summary": "\"The people I trusted betrayed me. The justice system failed me.\""
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/hyundai-claims-humanoid-robot-plan-is-not-part-of-talks-with-striking-workers/",
    "domain": "大厂 AI 动态",
    "title": "Hyundai claims humanoid robot plan is not part of talks with striking workers",
    "url": "https://arstechnica.com/ai/2026/07/hyundai-claims-humanoid-robot-plan-is-not-part-of-talks-with-striking-workers/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T18:18:12+00:00",
    "summary": "Union previously warned automaker that any robot deployment must be negotiated."
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
    "id": "hn:49012630",
    "domain": "股票",
    "title": "Alphabet Announces Second Quarter 2026 Results [pdf]",
    "url": "https://s206.q4cdn.com/479360582/files/doc_financials/2026/q2/2026q2-alphabet-earnings-release.pdf",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-07-22T20:04:48+00:00",
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
    "id": "hn:49012394",
    "domain": "股票",
    "title": "We got California to intervene about OpenAI's corporate switch from nonprofit",
    "url": "https://fortune.com/2026/07/22/openai-foundation-class-n-stock-board-control-ipo/",
    "source": "SLHamlet",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-22T19:46:18+00:00",
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
    "id": "wscn:3777757",
    "domain": "股票",
    "title": "上海推动科创板持续深化改革，事关可控核聚变、具身智能、量子计算、脑机接口……",
    "url": "https://wallstreetcn.com/articles/3777757",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T05:54:53+00:00",
    "summary": "上海发布加强科技金融服务20条措施。重点推动科创板深化改革，扩大第五套上市标准适用范围，支持可控核聚变、具身智能、量子计算等前沿领域未盈利企业上市。同时，便利企业再融资，设立社保科创基金与S母基金以培育耐心资本，规划建设直接融资试验区。"
  },
  {
    "id": "wscn:3777753",
    "domain": "股票",
    "title": "训练Gemini 4太烧钱！巴克莱测算：谷歌将连续两年自由现金流为负",
    "url": "https://wallstreetcn.com/articles/3777753",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T05:54:32+00:00",
    "summary": "巴克莱在谷歌Q2财报后大幅上调资本支出预期：2027年升至3500亿美元，2028年升至5000亿美元，均超同期经营性现金流，自由现金流将转负。核心驱动为Gemini 4大模型训练的算力需求。谷歌每月花约10亿美元租用外部GPU，释放自有算力用于训练。"
  },
  {
    "id": "wscn:3777750",
    "domain": "股票",
    "title": "海外仓库光模块被偷，东山精密：足额投保了货物运输险，对经营业绩影响极低",
    "url": "https://wallstreetcn.com/articles/3777750",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T05:51:07+00:00",
    "summary": "东山精密子公司索尔思光电光模块运输失窃事件持续发酵，公司紧急澄清：损失金额远低于网传\"数千万美元\"，已足额投保可获赔付，且相关影响已计入半年报，不足上年净利润10%。与此同时，公司上半年归母净利润预计同比暴增逾282%至29亿～30亿元，光模块业务量价齐升，800G产品持续放量，一场\"失窃风波\"反而将其亮眼业绩推至聚光灯下。"
  },
  {
    "id": "wscn:3777756",
    "domain": "股票",
    "title": "黄金“反叛”了：4140美元之后，反转还是死猫跳？",
    "url": "https://wallstreetcn.com/articles/3777756",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T05:49:28+00:00",
    "summary": "黄金两日累涨近3%强势突破4140美元，连穿四条均线——但这是反转还是反弹？汇丰、摩根大通定性\"技术性修复\"，多头却已高喊趋势确立。央行连续20个月增持、SPDR资金回流、科技股动量崩塌……多空各执三张牌势均力敌。三道关卡、五个信号，一张清单说清黄金的方向。"
  },
  {
    "id": "wscn:3777752",
    "domain": "股票",
    "title": "报道：英特尔、AMD寻求与中国客户签长期服务器CPU供货协议",
    "url": "https://wallstreetcn.com/articles/3777752",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T05:37:32+00:00",
    "summary": "英特尔与AMD向中国客户寻求更长期采购承诺，部分锁定期延伸至两年以上；中国市场CPU价格月涨超10%，年内累计涨幅逾40%。供应趋紧已直接冲击中国云厂商AI扩张节奏，服务器CPU市场正加速切换至卖方市场。"
  },
  {
    "id": "wscn:3777754",
    "domain": "股票",
    "title": "韩股日内涨约4.5%、再度出发熔断，油价一度逼近97美元，美债承压",
    "url": "https://wallstreetcn.com/articles/3777754",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T05:32:24+00:00",
    "summary": "韩国KOSPI指数向上触及7100点，日内涨约4.5%。三星电子与SK海力士均上涨逾3%。Alphabet盘后跌逾3%，特斯拉及IBM亦随之走低，纳斯达克100指数期货微跌0.2%。布伦特原油一度逼近每桶97美元，通胀压力再度升温，令美债市场承压。"
  },
  {
    "id": "wscn:3777755",
    "domain": "股票",
    "title": "不学昨天的Palantir，滴普科技寻找企业AI的新路径",
    "url": "https://wallstreetcn.com/articles/3777755",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:31:26+00:00",
    "summary": "最会做AI的公司开始派工程师进企业。\n今年5月，Anthropic宣布和 Blackstone、He..."
  },
  {
    "id": "wscn:3777748",
    "domain": "股票",
    "title": "AI每赚1块钱，谷歌花出去2块",
    "url": "https://wallstreetcn.com/articles/3777748",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:24:28+00:00",
    "summary": "谷歌交出了一份近乎完美的财报，但繁荣背后隐藏着另一个现实：9.11美元EPS中近七成来自Anthropic和SpaceX的投资浮盈，剔除后核心业绩反而低于预期；自由现金流史上首次转负，资本开支连续两次上调至2000亿美元。谷歌证明了AI可以赚钱，却还没有证明AI赚的钱，足以支撑AI烧的钱。"
  },
  {
    "id": "wscn:3777669",
    "domain": "股票",
    "title": "中美AI模式竞赛：全球AI生态的两条演化路径，2027年是决胜拐点？",
    "url": "https://wallstreetcn.com/premium/articles/3777669?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:11:01+00:00",
    "summary": "2026年，全球AI产业最深刻的格局变化，不是某个模型的领先或落后，而是中美两国正在形成两套逻辑迥异、相互独立的AI发展范式。"
  },
  {
    "id": "wscn:3777740",
    "domain": "股票",
    "title": "A股三大股指集体下跌，有色、电网逆势拉升，科创50跌超4%，半导体产业链齐跌，恒指涨超1%，科网股全线反弹",
    "url": "https://wallstreetcn.com/articles/3777740",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:03:20+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市超3100股飘红，上午半天成交1.47万亿。沪深两市半日成交额1.46万亿，较上个交易日缩量超3200亿。半导体产业链领跌，半导体硅片和设备、GPU、先进封装方向跌幅居前；锂矿股爆发，盛新锂能、永杉锂业等多股涨停，油气、有色金属、电力股表现亮眼。"
  },
  {
    "id": "wscn:3777638",
    "domain": "股票",
    "title": "11年来重大转向！电池消费税政策落地：新能源产业“后补贴时代”的里程碑式转折？",
    "url": "https://wallstreetcn.com/premium/articles/3777638?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T03:48:11+00:00",
    "summary": "自2026年9月1日起，对锂离子蓄电池等恢复征收消费税，税率分两步从2%提升至4%。"
  },
  {
    "id": "wscn:3777745",
    "domain": "股票",
    "title": "特斯拉的“尴尬期”：汽车利润越来越薄，AI故事越来越贵",
    "url": "https://wallstreetcn.com/articles/3777745",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T03:28:22+00:00",
    "summary": "过去12个月累计营收首次突破1000亿美元，但二季度利润却只剩4亿美元。汽车业务赚钱越来越难，AI业务烧钱越来越快，特斯拉正处于最昂贵的过渡期——旧引擎正在减速，新引擎还没开始赚钱，而467倍市盈率已经提前押注了成功。"
  },
  {
    "id": "wscn:3777746",
    "domain": "股票",
    "title": "MLCC也进入\"长协时代\"：三星电机与某科技巨头签下2亿美元长协，锁定2027年供应",
    "url": "https://wallstreetcn.com/articles/3777746",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T03:24:36+00:00",
    "summary": "这是其继6月后连续第二个月斩获同类大单，今年已披露的AI服务器元器件协议总额超15亿美元。三星电机表示，将加速开发下一代尖端产品，构建稳定供应链。业内指出，MLCC正在AI基础设施需求驱动下加速从短期订单转向长协模式，三星电机凭借逾40%的市占率持续领跑这一高壁垒市场。"
  },
  {
    "id": "wscn:3777741",
    "domain": "股票",
    "title": "AI芯片撑起韩国经济：二季度GDP增长3.7%超预期，但内需依然疲弱",
    "url": "https://wallstreetcn.com/articles/3777741",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T03:22:04+00:00",
    "summary": "AI投资热潮持续拉动存储芯片需求，韩国二季度GDP同比增长3.7%、环比增长0.6%，双双超出市场预期。但增长动能有所收敛，同比略低于一季度的3.8%，环比增速也低于一季度的1.8%。其中，消费环比仅增0.4%、建筑投资转负，出口繁荣与内需疲弱的裂口正在加深。"
  },
  {
    "id": "wscn:3777742",
    "domain": "股票",
    "title": "Agent时代CPU路线之争：英伟达押注“单核更快”，AMD押注“并发更多”",
    "url": "https://wallstreetcn.com/articles/3777742",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T03:15:54+00:00",
    "summary": "英伟达披露Vera CPU架构，以“单线程最大性能”为核心挑战AMD的高并发路线，两家公司围绕智能体AI时代CPU核心指标的争论正式浮出水面。AMD测算其EPYC Turin在100千瓦机架场景下吞吐量是Vera的2.4倍。在服务器CPU市场规模持续膨胀的背景下，谁先定义行业KPI，谁就掌握话语权。"
  },
  {
    "id": "wscn:3777743",
    "domain": "股票",
    "title": "4小时、118个回答，梁文锋内部交流回应一切",
    "url": "https://wallstreetcn.com/articles/3777743",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T03:09:14+00:00",
    "summary": "梁文峰称，以AGI为唯一目标，以克制换成功概率。他强调团队稳定性是唯一不可退让的核心利益，此次融资正是为此保障。技术路线上，AGI路径为\"语言模型→思维链→Agent→持续学习→智能奇点\"。他认为中美差距本质是算力差距，而非人才差距，并对国产芯片生态持乐观态度。"
  },
  {
    "id": "wscn:3777744",
    "domain": "股票",
    "title": "百菲乳业改道港股，“全国第一”如何被重新包装",
    "url": "https://wallstreetcn.com/articles/3777744",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T02:53:32+00:00",
    "summary": "在A股市场辗转三年后，主营水牛奶产品的广西百菲乳业股份有限公司（下称“百菲乳业”）把上市目的地换到了..."
  },
  {
    "id": "wscn:3777738",
    "domain": "股票",
    "title": "清算量超越港元与美元！香港离岸人民币市场跃升为全球融资枢纽",
    "url": "https://wallstreetcn.com/articles/3777738",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T02:53:06+00:00",
    "summary": "香港离岸人民币市场正迎来历史性跃升：6月人民币清算量攀至53.2万亿元，首次在港超越港元与美元；离岸存款触及1.13万亿元历史高位，债券发行年内激增33%。中美逾200基点的利率差持续驱动借贷需求，香港正从人民币\"积累中心\"蜕变为全球融资枢纽，人民币国际化加速进入新阶段。"
  },
  {
    "id": "wscn:3777733",
    "domain": "股票",
    "title": "金油从反向到同涨，资金变了",
    "url": "https://wallstreetcn.com/articles/3777733",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T02:36:56+00:00",
    "summary": "兴业证券表示，黄金两日累涨近3%强势突破4140美元，罕见\"金油同涨\"打破传统跷跷板逻辑。更耐人寻味的是，面对加息预期升温、实际利率走高，金价却拒绝下跌——科技股震荡引发资金出走、空头仓位出清充分、利空提前定价三重共振，正推动配置资金悄然回流黄金。趋势性上涨或仍需等待9月美联储鸽派信号。"
  },
  {
    "id": "wscn:3777737",
    "domain": "股票",
    "title": "可再生能源发展“十五五”规划出炉！2030年风光装机超28亿千瓦、发电量占比达30%",
    "url": "https://wallstreetcn.com/articles/3777737",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T02:16:08+00:00",
    "summary": "规划设定2030年风光装机超28亿千瓦、发电量占比达30%的量化目标。规划要求加快提升可再生能源电力可靠替代能力，要求新建集中式风光电站置信出力原则上不低于10%，抽水蓄能装机目标设定为1.6亿千瓦。与此同时，规划明确推动新能源全面入市、完善绿证价格体系。"
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
    "id": "hn:48907665",
    "domain": "股票",
    "title": "IBM is on pace for its worst day ever",
    "url": "https://www.cnn.com/2026/07/14/tech/ibm-stock-worst-day-ever",
    "source": "1970-01-01",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-07-14T14:39:25+00:00",
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
    "id": "hn:48905958",
    "domain": "股票",
    "title": "IBM shares down 23% as clients spend more on hardware and memory chips",
    "url": "https://www.cnbc.com/2026/07/14/ibm-warns-second-quarter-earnings-fell-short-of-expectations.html",
    "source": "rvz",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-14T12:44:17+00:00",
    "summary": ""
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
    "id": "hn:48717469",
    "domain": "金融",
    "title": "The CEO of Mullvad is the main financer of the Swedish Örebro party",
    "url": "https://det.social/@lostgen/116820546568940358",
    "source": "Risse",
    "platform": "hackernews",
    "points": 695,
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
    "id": "hn:48892638",
    "domain": "金融",
    "title": "Benchmarking 15 “E-Waste” GPUs with Modern Workloads",
    "url": "https://esologic.com/benchmarking-tesla-gpus/",
    "source": "eso_logic",
    "platform": "hackernews",
    "points": 141,
    "published_at": "2026-07-13T13:48:42+00:00",
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
    "id": "hn:48999329",
    "domain": "金融",
    "title": "A Man Who Runs the IRS Spied on Colleagues When He Worked at JPMorgan",
    "url": "https://www.wsj.com/finance/banking/irs-bisignano-spying-jpmorgan-6cd1ddf0",
    "source": "cwwc",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-07-21T22:40:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:49001708",
    "domain": "金融",
    "title": "Tesla Balance Bike",
    "url": "https://shop.tesla.com/product/balance-bike-for-kids",
    "source": "surprisetalk",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-22T04:00:11+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.19497",
    "domain": "金融",
    "title": "The Science and Practice of Trend-Following Systems",
    "url": "https://arxiv.org/abs/2607.19497",
    "source": "Artur Sepp, Vladimir Lucic",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2607.19497v1 Announce Type: new Abstract: We present a unified approach to designing trend-following (TF) systems and classify them into European, American, and Time Series Momentum categories. "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.19562",
    "domain": "金融",
    "title": "The Direct and Indirect Effects of Genetics and Education",
    "url": "https://arxiv.org/abs/2607.19562",
    "source": "Senan Hogan-Hennessy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2607.19562v1 Announce Type: new Abstract: Genes associated with educational attainment causally improve labour market income, but the economic mechanism behind this relationship is not clear. Us"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.19929",
    "domain": "金融",
    "title": "Bounded Attention and Attenuated Elasticities",
    "url": "https://arxiv.org/abs/2607.19929",
    "source": "Tingmingke Lu, Zhenyi Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2607.19929v1 Announce Type: new Abstract: We study how bounded attention affects the structural estimation of the elasticity of substitution. In a sparse-max model, equilibrium prices and expend"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.20068",
    "domain": "金融",
    "title": "Catastrophic disruption cascades driven by the nonlinearity of systemic risk",
    "url": "https://arxiv.org/abs/2607.20068",
    "source": "Jan Fialkowski, Shlomo Havlin, Stefan Thurner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2607.20068v1 Announce Type: new Abstract: Whether the COVID-19 pandemic or the Iran war, recent events have highlighted the systemic fragility of supply chains. Due to highly specific and mutual"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.20093",
    "domain": "金融",
    "title": "Retail Trader's Ruin: An Anatomy of Popular Signal Failure",
    "url": "https://arxiv.org/abs/2607.20093",
    "source": "Adam Darmanin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2607.20093v1 Announce Type: new Abstract: We test whether five widely promoted retail signal families - trend, oscillator, candlestick, volume, and calendar rules - deliver a positive, economica"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.20168",
    "domain": "金融",
    "title": "Quantum Kernels and the Cross-Section of Stock Returns: Anatomy of a Vanishing Advantage",
    "url": "https://arxiv.org/abs/2607.20168",
    "source": "Junchi Shen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2607.20168v1 Announce Type: new Abstract: Do quantum kernels improve cross-sectional stock return prediction? We run a controlled horse race on the Chinese A-share market in which a quantum fide"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.20343",
    "domain": "金融",
    "title": "Model Risk via Signature-Induced Optimal Transport",
    "url": "https://arxiv.org/abs/2607.20343",
    "source": "Tomoyuki Ichiba, Qijin Shi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2607.20343v1 Announce Type: new Abstract: We propose a signature-induced, optimal transport framework for path-space model risk, in which ambiguity between stochastic path laws is factorized thr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.20365",
    "domain": "金融",
    "title": "Licensing and Innovation Regimes in Pharmaceutical R&D",
    "url": "https://arxiv.org/abs/2607.20365",
    "source": "Michele Liberatore, Massimo Riccaboni",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2607.20365v1 Announce Type: new Abstract: We study how licensing affects the allocation of innovation in pharmaceutical R&amp;D. We develop a model in which projects differ in both quality and i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.19453",
    "domain": "金融",
    "title": "Predictive Extrema, Unprofitable Policies: An AI-Assisted Audit of Candle-Based Binance Spot Timing Models",
    "url": "https://arxiv.org/abs/2607.19453",
    "source": "Ayoub Jadouli",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2607.19453v1 Announce Type: cross Abstract: We audit whether candle-based machine-learning models can turn predictions of cryptocurrency extrema or short-horizon outcomes into positive Binance S"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.20415",
    "domain": "金融",
    "title": "Flux-Corrected Diagonal Frog: second order and positivity at all time steps",
    "url": "https://arxiv.org/abs/2607.20415",
    "source": "Andrey Itkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2607.20415v1 Announce Type: cross Abstract: By Godunov's theorem, linear second-order finite-difference schemes for the Fokker-Planck equation cannot preserve positivity. The Diagonal Frog (DF) "
  },
  {
    "id": "rss:https://arxiv.org/abs/2301.05886",
    "domain": "金融",
    "title": "Efficient Risk Estimation for the Credit Valuation Adjustment",
    "url": "https://arxiv.org/abs/2301.05886",
    "source": "Michael B. Giles, Abdul-Lateef Haji-Ali, Jonathan Spence",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2301.05886v3 Announce Type: replace Abstract: The valuation of over-the-counter derivatives is subject to a series of valuation adjustments known as xVA, which pose additional risks for financia"
  },
  {
    "id": "rss:https://arxiv.org/abs/2503.14997",
    "domain": "金融",
    "title": "The fundamental representation of pricing adjustments",
    "url": "https://arxiv.org/abs/2503.14997",
    "source": "Benedict Burnett, Ryan McCrickerd, Benjamin Piau",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2503.14997v2 Announce Type: replace Abstract: This article consolidates and extends past work on derivative pricing adjustments, including XVA, by providing an encapsulating representation of th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.04211",
    "domain": "金融",
    "title": "Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients",
    "url": "https://arxiv.org/abs/2510.04211",
    "source": "Vygintas Gontis, Lesya Kolinets",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2510.04211v2 Announce Type: replace Abstract: The integration of Central and Eastern European (CEE) countries into the European Economic Area serves as a valuable experiment for the regional eco"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.02362",
    "domain": "金融",
    "title": "Reconstructing Large Scale Production Networks",
    "url": "https://arxiv.org/abs/2512.02362",
    "source": "Ashwin Bhattathiripad, Vipin P Veetil",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2512.02362v3 Announce Type: replace Abstract: Firm-to-firm production networks matter for aggregate propagation, but they are rarely observed. This paper reconstructs national-scale, weighted fi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.20050",
    "domain": "金融",
    "title": "Information Aggregation with AI Agents",
    "url": "https://arxiv.org/abs/2604.20050",
    "source": "Spyros Galanis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2604.20050v3 Announce Type: replace Abstract: Can Large Language Models (AI agents) aggregate dispersed private information through trading and reason about the knowledge of others by observing "
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.25824",
    "domain": "金融",
    "title": "Mean-field game of mean-variance portfolio optimization with peer-based risk aversion",
    "url": "https://arxiv.org/abs/2605.25824",
    "source": "Weilun Cheng, Zongxia Liang, Sheng Wang, Xiang Yu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2605.25824v2 Announce Type: replace Abstract: This paper investigates a class of mean-field game (MFG) for mean-variance (MV) portfolio optimization, highlighting a new type of relative performa"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05802",
    "domain": "金融",
    "title": "Failure Privacy and Safe Collective Expression with Social Assurance Contracts",
    "url": "https://arxiv.org/abs/2607.05802",
    "source": "Matthew Cashman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2607.05802v3 Announce Type: replace Abstract: Controversial views sometimes remain unspoken because they invite retaliation. However, a sufficiently large group could speak safely if only they s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.13844",
    "domain": "金融",
    "title": "Messy Research, Certification and the Monetization of Science",
    "url": "https://arxiv.org/abs/2607.13844",
    "source": "Johan Fourie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2607.13844v2 Announce Type: replace Abstract: I study when science starts charging for what reputation used to provide. In the model, AI lowers the cost of producing a polished manuscript faster"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.19005",
    "domain": "金融",
    "title": "Observable Matrix Dynamics of Stocks",
    "url": "https://arxiv.org/abs/2607.19005",
    "source": "Igor Halperin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2607.19005v2 Announce Type: replace Abstract: The Observable Matrix Dynamics (OMD) approach monitors the time development of complex non-linear systems through the trajectory of a fixed-size dis"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.13366",
    "domain": "金融",
    "title": "Where Do the Returns to Schooling Come From? Educational Transitions and Labor Market Payoffs",
    "url": "https://arxiv.org/abs/2508.13366",
    "source": "Aleksei Opacic",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2508.13366v3 Announce Type: replace-cross Abstract: Conventional research on educational effects typically either employs a \"years of schooling\" measure of education, or dichotomizes attainment "
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.01363",
    "domain": "金融",
    "title": "Crashing Waves vs. Rising Tides: Findings on AI Automation from Thousands of Worker Evaluations of Labor Market Tasks",
    "url": "https://arxiv.org/abs/2604.01363",
    "source": "Matthias Mertens, Adam Kuzee, Brittany S. Harris, Harry Lyu, Wensu Li, Jonathan Rosenfeld, Meiri Anto, Martin Fleming, Neil Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T04:00:00+00:00",
    "summary": "arXiv:2604.01363v2 Announce Type: replace-cross Abstract: We propose that AI automation is a continuum between: (i) crashing waves where AI capabilities surge abruptly over small sets of tasks, and (i"
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
    "id": "hn:48735748",
    "domain": "金融",
    "title": "Supreme Court takes sledgehammer to federal regulatory structure",
    "url": "https://www.npr.org/2026/06/29/nx-s1-5875161/supreme-court-takes-sledgehammer-to-much-of-federal-governments-regulatory-structure",
    "source": "marojejian",
    "platform": "hackernews",
    "points": 83,
    "published_at": "2026-06-30T17:05:58+00:00",
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
    "id": "hn:48953857",
    "domain": "金融",
    "title": "Nadella Blasts AI Industry's Double Standard",
    "url": "https://finance.biggo.com/news/438f299b-ca23-468d-b37d-0ffe09a4ca55",
    "source": "nittanymount",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-07-18T00:28:46+00:00",
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
    "id": "hn:48880233",
    "domain": "金融",
    "title": "IT administrators are \"fed up\" with Microsoft's \"useless\" apps and Windows 11",
    "url": "https://www.neowin.net/news/it-admins-feel-overwhelmingly-sick-of-microsoft-and-windows-11-garbage-apps-products/",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-07-12T11:22:42+00:00",
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
    "id": "hn:48824584",
    "domain": "金融",
    "title": "JPMorgan, BofA and Others Explore Buying Card Network to Raise Debit-Card Fees",
    "url": "https://www.wsj.com/finance/banking/jpmorgan-bank-of-america-and-other-banks-explore-a-deal-to-shake-up-payments-world-9d8639fb",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-07-07T22:04:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48849827",
    "domain": "金融",
    "title": "FrontierFinance: The largest open benchmark for investor workflows",
    "url": "https://research.samaya.ai/benchmarks/frontier-finance",
    "source": "ashwinpp",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-09T17:49:05+00:00",
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
    "id": "hn:48780128",
    "domain": "金融",
    "title": "AI First: How the Federal Government Is Prioritizing AI over People and Planet",
    "url": "https://stopgreedbuildgreen.climateandcommunity.org/posts/ai-first",
    "source": "eatox",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-03T21:21:08+00:00",
    "summary": ""
  }
]
```
