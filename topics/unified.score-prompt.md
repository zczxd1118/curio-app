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

- 今日日期：`2026-08-03`
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
  "date": "2026-08-03",
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
    "points": 4057712,
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
    "points": 1652778,
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
    "points": 1543179,
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
    "points": 1306027,
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
    "points": 1031023,
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
    "points": 994856,
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
    "points": 868383,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 588232,
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
    "points": 549515,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 464813,
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
    "points": 432142,
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
    "points": 419273,
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
    "points": 397615,
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
    "points": 254906,
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
    "points": 218580,
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
    "points": 202244,
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
    "points": 178377,
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
    "points": 162993,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 150232,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV172GP6rEZs",
    "domain": "AI",
    "title": "🚀DeepSeek V4 Flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！",
    "url": "http://www.bilibili.com/video/av117014605731815",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 148358,
    "published_at": "2026-07-31T12:42:57+00:00",
    "summary": "🚀DeepSeek v4 flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！性能、速度与真实短板全曝光！对比Kimi K3后优点和缺点都藏不住了\n\nDeepSeek 发布了 DeepSeek V4 Flash 0731：284B 总参数、13B 激活参数、100 万 Token 上下文，官方基准表现接近 Claude"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 116575,
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
    "points": 92903,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1Tv3i6LEX1",
    "domain": "AI",
    "title": "用Codex、cursor 还是Claude ？程序员不作选择题，我都要用，还一起用 | Orca ADE 介绍",
    "url": "http://www.bilibili.com/video/av116996217838997",
    "source": "技术胖",
    "platform": "bilibili",
    "points": 83167,
    "published_at": "2026-07-28T06:41:31+00:00",
    "summary": "如果能把 Codex、Claude Code、Grok、Cursor 等智能编程工具整合到同一个工作环境中，再让多个 Agent 像团队成员一样分工协作，软件开发的效率将得到显著提升。Orca ADE 正是为此而生：它是一款开源、免费的 Agent 开发环境，专注于代码管理与命令行工作流，不仅能够接入多种编程 Agent，还支持语音操作和手机远程管理。接下来，我们就来认识一下 Orca ADE，看"
  },
  {
    "id": "bvid:BV1xBrDB9E42",
    "domain": "AI",
    "title": "独立开发太累？Godot + Claude Code 搭建 AI 辅助工作流，效率直接起飞！ | 地块召唤师开发实战 #01",
    "url": "http://www.bilibili.com/video/av115911319100158",
    "source": "像素夹心饼干",
    "platform": "bilibili",
    "points": 68142,
    "published_at": "2026-01-18T03:25:00+00:00",
    "summary": "大家好，这里是饼干！🍪\n这是我的新坑——**《地块召唤师》**开发实战分享的第一期。\n很多朋友问独立开发如何提升效率？这期视频我不聊虚的，直接公开我从 0 到 1 搭建的 AI + Godot 高效工作流。\n从游戏引擎的选择，到 Claude Code、Copilot 等 AI 工具的实战配置，再到如何用“明确需求”的方法论（SMART原则+双钻模型）来驾驭 AI，让它不仅仅是写代码的工具，更成为"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 58964,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53542,
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
    "points": 47536,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 43642,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 39689,
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
    "points": 39587,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1gwcAzkEhw",
    "domain": "AI",
    "title": "Claude Code Agent Teams上手指南+项目实测",
    "url": "http://www.bilibili.com/video/av116037064331269",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 35097,
    "published_at": "2026-02-08T23:30:00+00:00",
    "summary": "用Claude Code干复杂任务总碰到三个问题：\n\n上下文越来越长开始遗忘、任务只能串行效率低、单Agent视角单一容易漏检。\n\nClaude官方发布的Agent Teams功能正好解决这些痛点\n\n一个Team Lead拆任务，多个Teammate并行执行，还能互相通信协调。\n\n本期视频从核心概念、使用场景、底层架构到真实项目实战，带你完整搞懂Agent Teams的正确打开方式。"
  },
  {
    "id": "bvid:BV1cCj2ztEf5",
    "domain": "AI",
    "title": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%",
    "url": "http://www.bilibili.com/video/av114574527307727",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 35050,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 31152,
    "published_at": "2026-05-07T00:00:00+00:00",
    "summary": "全栈课一共分为6大块内容\n第一块：AI智能体开发基础(AI大模型、工具、记忆、MCP、中间件、Skills等核心内容)\n第二块：Claude Code,Trea+skills实现基于需求文档生成用例，基于OpenClaw实现接口自动化落地，基于hermes Agent实现web自动化落地\n第三块：功能测试的智能体开发(项目RAG知识库搭建+Agent搭建+skills开发，实现用例生成的Agent"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30141,
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
    "points": 28324,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV16ggC6DEZK",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116963049212769",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 26466,
    "published_at": "2026-07-22T10:10:42+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1ZnEJ6NEJ6",
    "domain": "AI",
    "title": "pi agent 最佳实践 | Harness Agent 定制全流程实战",
    "url": "http://www.bilibili.com/video/av116703891558374",
    "source": "程序员暮闲",
    "platform": "bilibili",
    "points": 23570,
    "published_at": "2026-06-06T15:45:29+00:00",
    "summary": "本期视频系统演示 pi agent 的安装、模型配置与扩展开发流程，重点讲解如何通过 TypeScript extensions、skills、themes、prompt template和 pi package完成拓展，把 pi agent 打造成适合自己工作流的高度定制化 AI Agent。"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22679,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 19608,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 18597,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 17766,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1dsNv66E3Q",
    "domain": "AI",
    "title": "【Cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116922599344955",
    "source": "六月要癫",
    "platform": "bilibili",
    "points": 15603,
    "published_at": "2026-07-15T06:39:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1YJ336EEBk",
    "domain": "AI",
    "title": "【AI陪玩】开袋即食的AI接入我的世界教程！",
    "url": "http://www.bilibili.com/video/av116981806143216",
    "source": "万昇Dwin",
    "platform": "bilibili",
    "points": 15318,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "模组：Numen\n项目地址：https://github.com/Dwinovo/minecraft-numen"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 14747,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV1CU346yEYC",
    "domain": "AI",
    "title": "聊聊Vibe Coding | AI降低了门槛，也降低了成本吗？",
    "url": "http://www.bilibili.com/video/av117008079392929",
    "source": "糖果果的陈同学",
    "platform": "bilibili",
    "points": 13245,
    "published_at": "2026-07-30T08:57:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1YGKJ6tEdz",
    "domain": "AI",
    "title": "Vibe Coding我的赛博女友",
    "url": "http://www.bilibili.com/video/av116933101950817",
    "source": "天工开帧",
    "platform": "bilibili",
    "points": 11822,
    "published_at": "2026-07-17T09:50:00+00:00",
    "summary": "Vibe Coding大赏之赛博女友。总体花费100个馒头左右，由于显存限制，目前实时数字人的版本没办法跑起来。目前可以24挂着，随时对话随时打断。作用嘛，除了聊天就是在我忙的时候顺手帮我查个东西。未来开发方向接入pi-agent，让它真正干活，当然，只是得上qwen27B以上得模型才有可用性。也就是说所有模型显存开销打底得36G以上。囧。当然如果不要无限制，可以接入在线模型或在线TTS，但是，我"
  },
  {
    "id": "bvid:BV1TtwCehEzG",
    "domain": "AI",
    "title": "cursor新手必会的怎么回退代码 防止改错改乱代码 提高效率开发",
    "url": "http://www.bilibili.com/video/av113855472605087",
    "source": "项目禅",
    "platform": "bilibili",
    "points": 11359,
    "published_at": "2025-01-19T14:29:21+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 10897,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1gf3T6KEef",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！从环境搭建到工作流完整闭环，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116979708990688",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 9794,
    "published_at": "2026-07-25T08:47:37+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1xB3s6CEtx",
    "domain": "AI",
    "title": "【2026最新】当前B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发！",
    "url": "http://www.bilibili.com/video/av117007693455104",
    "source": "码士集团-马小萱",
    "platform": "bilibili",
    "points": 9526,
    "published_at": "2026-07-30T09:17:28+00:00",
    "summary": ""
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
    "id": "hn:49122838",
    "domain": "AI 算力 / 半导体",
    "title": "Moonshot’s Kimi uses 20k Nvidia chip cluster from Alibaba",
    "url": "https://www.bloomberg.com/news/articles/2026-07-31/moonshot-s-kimi-built-on-20-000-nvidia-chip-cluster-from-alibaba",
    "source": "gk1",
    "platform": "hackernews",
    "points": 113,
    "published_at": "2026-07-31T13:24:03+00:00",
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
    "id": "rss:https://www.eetimes.com/humanoid-manipulation-at-the-edge-of-physical-interaction/",
    "domain": "AI 算力 / 半导体",
    "title": "Humanoid Manipulation at the Edge of Physical Interaction",
    "url": "https://www.eetimes.com/humanoid-manipulation-at-the-edge-of-physical-interaction/",
    "source": "Renesas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T14:00:00+00:00",
    "summary": "This white paper examines emerging humanoid robot architectures, focusing on how joints and dexterous hands are becoming intelligent, sensor-rich subsystems that require tightly integrated control, co"
  },
  {
    "id": "rss:https://www.eetimes.com/erp-statistics-insights-from-70-manufacturing-case-studies/",
    "domain": "AI 算力 / 半导体",
    "title": "ERP Statistics: Insights From 70 Manufacturing Case Studies",
    "url": "https://www.eetimes.com/erp-statistics-insights-from-70-manufacturing-case-studies/",
    "source": "MRPeasy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T13:00:00+00:00",
    "summary": "We analyzed 70 customer case studies to better understand the ERP experiences of small manufacturers. Here’s what electronics manufacturers had to say. The post ERP Statistics: Insights From 70 Manufa"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/grab-this-240-hz-qd-oled-gaming-monitor-at-just-usd300-gigabytes-27-inch-go27q24a-is-now-usd150-off-at-newegg",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this 240 Hz QD-OLED gaming monitor at just $300 — Gigabyte's 27-inch GO27Q24A is now $150 off at Newegg",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/grab-this-240-hz-qd-oled-gaming-monitor-at-just-usd300-gigabytes-27-inch-go27q24a-is-now-usd150-off-at-newegg",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T16:16:41+00:00",
    "summary": "Gigabyte's GO27Q24A delivers a 240Hz QD-OLED panel, HDMI 2.1, and esports-focused features for just $299.99"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/space/errant-spacex-rocket-stage-set-to-smash-into-the-moon-at-5-400-mph-seven-times-the-speed-of-sound-nasa-and-south-korean-orbiters-prepare-to-track-3-ton-tnt-impact",
    "domain": "AI 算力 / 半导体",
    "title": "Errant SpaceX rocket stage set to smash into the moon at 5,400 mph, seven times the speed of sound — NASA and South Korean orbiters prepare to track 3-ton TNT impact",
    "url": "https://www.tomshardware.com/tech-industry/space/errant-spacex-rocket-stage-set-to-smash-into-the-moon-at-5-400-mph-seven-times-the-speed-of-sound-nasa-and-south-korean-orbiters-prepare-to-track-3-ton-tnt-impact",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T15:44:51+00:00",
    "summary": "A used SpaceX rocket segment used to deliver to lunar probes in 2025 is set to crash on the surface of the moon in the near future. This event will be monitored by two satellites as scientists and res"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/microsoft-paint-used-as-a-monitor-to-run-doom-at-up-to-35-fps-project-released-by-firms-azure-cto-runs-actual-doom-engine-and-loads-real-shareware-doom1-wad",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft Paint used as a 'monitor' to run Doom at up to 35 fps, project released by firm's Azure CTO — runs actual Doom engine and loads real shareware DOOM1.WAD",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/microsoft-paint-used-as-a-monitor-to-run-doom-at-up-to-35-fps-project-released-by-firms-azure-cto-runs-actual-doom-engine-and-loads-real-shareware-doom1-wad",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T14:14:24+00:00",
    "summary": "DoomPaint stands out from the Doom crowd as it has been developed by Microsoft's Azure CTO and because it runs using MS Paint as the viewport for in-game action."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/iran-suspected-of-conducting-cyberattacks-on-us-water-suppliers-in-45-municipalities-small-towns-mostly-targeted-with-utilities-switching-to-manual-control",
    "domain": "AI 算力 / 半导体",
    "title": "Iran suspected of conducting cyberattacks on US water suppliers in 45 municipalities — small towns mostly targeted, with utilities switching to manual control",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/iran-suspected-of-conducting-cyberattacks-on-us-water-suppliers-in-45-municipalities-small-towns-mostly-targeted-with-utilities-switching-to-manual-control",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T13:10:00+00:00",
    "summary": "Several US towns said that their water utilities have suffered from cyberattacks, which are suspected to have originated from Iran. While systems remain running, several have resorted to manual contro"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/commemorative-golden-doom-floppy-disks-go-up-for-pre-order-pair-of-limited-edition-dummy-imitation-gold-plating-disks-and-a-box-are-usd30-at-gamestop",
    "domain": "AI 算力 / 半导体",
    "title": "Commemorative golden Doom floppy disks go up for pre-order — pair of limited edition dummy ‘imitation gold plating’ disks and a box are $30 at GameStop",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/commemorative-golden-doom-floppy-disks-go-up-for-pre-order-pair-of-limited-edition-dummy-imitation-gold-plating-disks-and-a-box-are-usd30-at-gamestop",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T12:45:00+00:00",
    "summary": "GameStop has listed a purely ornamental Doom Floppy Disk Limited Edition Imitation Gold Plated Replica at $29.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-upcoming-zen-6-processors-could-fix-microstutters-and-improve-1-percent-lows-in-games-next-gen-cpus-tipped-to-feature-per-core-optimizations-for-thermal-and-power-budgets",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's upcoming Zen 6 processors could fix microstutters and improve 1% lows in games — Next-gen CPUs tipped to feature per-core optimizations for thermal and power budgets",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-upcoming-zen-6-processors-could-fix-microstutters-and-improve-1-percent-lows-in-games-next-gen-cpus-tipped-to-feature-per-core-optimizations-for-thermal-and-power-budgets",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T12:30:00+00:00",
    "summary": "A new report suggests AMD is cooking up a range of per-core optimizations for Zen 6 that might not seem huge on their own, but they could add up to make a world of difference in gaming performance."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/first-open-source-firmware-for-am5-officially-launches-dasharo-v0-9-0-brings-coreboot-and-opensil-to-zen-4-apus-on-msi-b850",
    "domain": "AI 算力 / 半导体",
    "title": "First open-source firmware for AM5 officially launches — Dasharo v0.9.0 brings Coreboot and openSIL to Zen 4 APUs on MSI B850",
    "url": "https://www.tomshardware.com/pc-components/motherboards/first-open-source-firmware-for-am5-officially-launches-dasharo-v0-9-0-brings-coreboot-and-opensil-to-zen-4-apus-on-msi-b850",
    "source": "Aaron Klotz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T12:10:00+00:00",
    "summary": "3mdeb has introduced a new open-source firmware for the MSI B850-P WiFi, marking the first time open-source firmware has been introduced to the AM5 platform."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/spacexai-says-it-will-remove-all-69-of-its-unpermitted-turbine-power-generators-but-expects-process-to-take-a-year-trailer-mounted-generators-to-be-replaced-by-1-2gw-power-plant",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceXAI says it will remove all 69 of its unpermitted turbine power generators, but expects process to take a year — trailer-mounted generators to be replaced by 1.2GW power plant",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/spacexai-says-it-will-remove-all-69-of-its-unpermitted-turbine-power-generators-but-expects-process-to-take-a-year-trailer-mounted-generators-to-be-replaced-by-1-2gw-power-plant",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T11:50:00+00:00",
    "summary": "These turbines have been the center of a lawsuit involving permits and pollution. While this is good news for the community, it will still take quite some time before they're fully removed from the pr"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/rtx-5060-ti-survives-car-crash-after-being-bent-in-half-short-pcb-saves-the-day-single-memory-chip-resolder-restore-full-performance",
    "domain": "AI 算力 / 半导体",
    "title": "RTX 5060 Ti survives car crash after being bent in half — short PCB saves the day, single memory chip resolder restore full performance",
    "url": "https://www.tomshardware.com/pc-components/gpus/rtx-5060-ti-survives-car-crash-after-being-bent-in-half-short-pcb-saves-the-day-single-memory-chip-resolder-restore-full-performance",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T11:30:00+00:00",
    "summary": "What happens when a graphics card gets in a car crash? If you're lucky, the damage is limited to just cosmetic scars that can go away over time with no serious damage under-the-hood."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/gem-mint-signed-1983-steve-jobs-business-card-opens-at-usd70-000-second-signed-card-from-that-era-after-usd180-000-record-sale",
    "domain": "AI 算力 / 半导体",
    "title": "Gem Mint signed 1983 Steve Jobs business card opens at $70,000 — second signed card from that era after $180,000 record sale",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/gem-mint-signed-1983-steve-jobs-business-card-opens-at-usd70-000-second-signed-card-from-that-era-after-usd180-000-record-sale",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T11:00:00+00:00",
    "summary": "This rare business card is currently on RR Auction, with a previous example going for $180,000 just a couple of years ago. It's graded Gem Mint 10, meaning it's as perfect as it can get."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/prolific-team-fortress-2-collector-is-selling-his-in-game-case-arsenal-for-an-estimated-usd100-000-1-7-million-items-collected-over-10-years-are-enough-to-fund-a-house-purchase",
    "domain": "AI 算力 / 半导体",
    "title": "Prolific Team Fortress 2 collector is selling his in-game case arsenal for an estimated $100,000 — 1.7 million items collected over 10 years are enough to fund a house purchase",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/prolific-team-fortress-2-collector-is-selling-his-in-game-case-arsenal-for-an-estimated-usd100-000-1-7-million-items-collected-over-10-years-are-enough-to-fund-a-house-purchase",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T10:30:00+00:00",
    "summary": "One Team Fortress 2 player has amassed a collection of over 1.7 million cases from the game, and after nearly a decade of collecting, he’s selling the collection for an estimated $100,000."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/dell-founder-shows-how-a-usd100-billion-empire-started-42-years-ago-ceo-says-this-one-page-changed-my-life",
    "domain": "AI 算力 / 半导体",
    "title": "Dell founder shows how a $100 billion empire started 42 years ago — CEO says ‘This one page changed my life’",
    "url": "https://www.tomshardware.com/tech-industry/dell-founder-shows-how-a-usd100-billion-empire-started-42-years-ago-ceo-says-this-one-page-changed-my-life",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T17:06:31+00:00",
    "summary": "Billionaire Michael Dell reminisced about the early days of his company, sharing an early quarterly earnings report that showed the then-startup making nearly $135,000 in just three months. Dell says "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/score-the-ultimate-amd-am4-starter-pack-with-a-six-core-cpu-and-16gb-ram-for-only-usd280-kickstart-your-next-pc-build-with-usd138-in-savings",
    "domain": "AI 算力 / 半导体",
    "title": "Score the ultimate AMD AM4 starter pack with a six-core CPU and 16GB RAM for only $280 — kickstart your next PC build with $138 in savings",
    "url": "https://www.tomshardware.com/pc-components/score-the-ultimate-amd-am4-starter-pack-with-a-six-core-cpu-and-16gb-ram-for-only-usd280-kickstart-your-next-pc-build-with-usd138-in-savings",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T15:09:27+00:00",
    "summary": "If you've been hesitating to upgrade to a modern platform because of the state of the PC hardware industry, this combo deal might be the one for you."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/microsoft-vows-to-make-windows-11-fly-on-8gb-ram-amid-memory-shortage-optimizations-to-reduce-os-memory-footprint-have-begun",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft vows to make Windows 11 fly on 8GB RAM amid memory shortage — optimizations to reduce OS memory footprint have begun",
    "url": "https://www.tomshardware.com/software/windows/microsoft-vows-to-make-windows-11-fly-on-8gb-ram-amid-memory-shortage-optimizations-to-reduce-os-memory-footprint-have-begun",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T14:48:26+00:00",
    "summary": "While the company's minimum OS specifications officially say 4GB, most PC builders know that 16GB is the bare minimum for a smooth experience on Windows 11. However, the memory chip shortage and the r"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-claude-hacked-three-real-life-companies-during-security-capabilities-test-test-environment-with-internet-access-and-unwitting-targets-lax-cybersecurity-practices-led-to-bots-running-rampant",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic's Claude hacked three real-life companies during security capabilities test — test environment with internet access and unwitting targets' lax cybersecurity practices led to bots running ram",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-claude-hacked-three-real-life-companies-during-security-capabilities-test-test-environment-with-internet-access-and-unwitting-targets-lax-cybersecurity-practices-led-to-bots-running-rampant",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T12:30:00+00:00",
    "summary": "Anthropic's Claude hacked three real-life companies during security capabilities test — open test environment and unwitting targets' lax cybersecurity practices led bots run rampant"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/nozzlegate-erupts-as-prusa-core-one-3d-ptinter-kits-arrive-with-soft-steel-nozzles-bondtech-admits-machining-flaws-with-no-quick-fix",
    "domain": "AI 算力 / 半导体",
    "title": "'Nozzlegate' erupts as Prusa CORE One 3D printer kits arrive with soft steel nozzles — Bondtech admits machining flaws with no quick fix (Updated)",
    "url": "https://www.tomshardware.com/3d-printing/nozzlegate-erupts-as-prusa-core-one-3d-ptinter-kits-arrive-with-soft-steel-nozzles-bondtech-admits-machining-flaws-with-no-quick-fix",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T12:10:57+00:00",
    "summary": "Bondtech, the creator and manufacturer of the INDX toolchanger system used to create the highly anticipated Prusa CORE One+ INDX, admitted to a significant labeling mistake. The nozzles provided with "
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/sony-doubles-down-on-axing-physical-game-discs-cfo-reiterates-were-going-to-cautiously-move-this-forward",
    "domain": "AI 算力 / 半导体",
    "title": "Sony doubles down on axing physical game discs — CFO reiterates 'we’re going to cautiously move this forward'",
    "url": "https://www.tomshardware.com/video-games/playstation/sony-doubles-down-on-axing-physical-game-discs-cfo-reiterates-were-going-to-cautiously-move-this-forward",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T11:00:00+00:00",
    "summary": "Sony confirms that its stance has not changed on ending the production of physical game discs for titles released after January 2028."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/97-untouched-duck-hunt-and-super-mario-bros-cartridges-worth-thousands-discovered-in-retro-shop-storage-room-never-before-seen-version-of-popular-nes-games-include-five-perfect-10-psa-items",
    "domain": "AI 算力 / 半导体",
    "title": "97 untouched Duck Hunt and Super Mario Bros. cartridges worth thousands discovered in retro shop storage room — never-before-seen version of popular NES games include five perfect 10 PSA items",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/97-untouched-duck-hunt-and-super-mario-bros-cartridges-worth-thousands-discovered-in-retro-shop-storage-room-never-before-seen-version-of-popular-nes-games-include-five-perfect-10-psa-items",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T10:00:00+00:00",
    "summary": "A retro gaming shop in Wisconsin finds a box of unopened, never-before-seen versions of Duck Hunt and Super Mario Bros. in its storage room. These items are probably worth four to five digits, and the"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/lost-one-of-a-kind-nintendo-ds-cartridge-hits-ebay-for-usd9-100-pokepark-fishing-contest-designed-to-delete-itself-after-12-hours-game-so-rare-it-was-only-distributed-to-theme-park-attendees-in-2005",
    "domain": "AI 算力 / 半导体",
    "title": "Lost one-of-a-kind Nintendo DS cartridge hits eBay for $9,100 — PokePark Fishing Contest designed to delete itself after 12 hours, game so rare it was only distributed to theme park attendees in 2005",
    "url": "https://www.tomshardware.com/video-games/nintendo/lost-one-of-a-kind-nintendo-ds-cartridge-hits-ebay-for-usd9-100-pokepark-fishing-contest-designed-to-delete-itself-after-12-hours-game-so-rare-it-was-only-distributed-to-theme-park-attendees-in-2005",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T09:00:00+00:00",
    "summary": "A Nintendo DS game that was classified as ‘lost media’ for nearly two decades is now within tantalizing reach of video gaming fans and archivists."
  },
  {
    "id": "hn:49125140",
    "domain": "AI 算力 / 半导体",
    "title": "Hygon Reveals 512-Thread CPU and AI GPU to Rival Intel Xeon and Nvidia",
    "url": "https://www.ubergizmo.com/2026/06/hygon-512-thread-cpu/",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-31T16:21:11+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/cea-leti-pushes-stacking-roadmap-as-ai-runs-into-memory-and-power-limits/",
    "domain": "AI 算力 / 半导体",
    "title": "CEA-Leti Pushes Stacking Roadmap as AI Runs Into Memory and Power Limits",
    "url": "https://www.eetimes.com/cea-leti-pushes-stacking-roadmap-as-ai-runs-into-memory-and-power-limits/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:48:06+00:00",
    "summary": "AI’s memory wall is turning packaging into architecture as CEA-Leti bets on 3D stacking, chiplets, and cooler power. The post CEA-Leti Pushes Stacking Roadmap as AI Runs Into Memory and Power Limits a"
  },
  {
    "id": "rss:https://www.eetimes.com/hybrid-architectures-for-space-missions-frameworks-and-consequence/",
    "domain": "AI 算力 / 半导体",
    "title": "Hybrid Architectures for Space Missions: Frameworks and Consequence",
    "url": "https://www.eetimes.com/hybrid-architectures-for-space-missions-frameworks-and-consequence/",
    "source": "Microchip Technology, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:38:20+00:00",
    "summary": "Join this webinar and explore how Microchip's framework translates architectural intent into component choices that preserve differentiation and margin. The post Hybrid Architectures for Space Mission"
  },
  {
    "id": "rss:https://www.eetimes.com/the-commercial-space-race-powering-the-next-comms-network/",
    "domain": "AI 算力 / 半导体",
    "title": "The Commercial Space Race: Powering the Next Comms Network",
    "url": "https://www.eetimes.com/the-commercial-space-race-powering-the-next-comms-network/",
    "source": "Altera, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T13:34:44+00:00",
    "summary": "Join us to learn how Altera is supporting commercial deployments in orbit today and what's coming next. The post The Commercial Space Race: Powering the Next Comms Network appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/military-ai-agents-under-cyberthreat-the-route-forward/",
    "domain": "AI 算力 / 半导体",
    "title": "Military AI Agents Under Cyberthreat: The Route Forward",
    "url": "https://www.eetimes.com/military-ai-agents-under-cyberthreat-the-route-forward/",
    "source": "Liam Critchley",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T07:30:00+00:00",
    "summary": "Rapid military AI adoption brings critical security risks, leaving autonomous battlefield systems vulnerable to cyberattacks. The post Military AI Agents Under Cyberthreat: The Route Forward appeared "
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
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/big-tech-spends-more-than-usd1-trillion-on-ai-infrastructure-additional-usd745-billion-expected-to-be-added-to-the-figure-in-2026-alone",
    "domain": "AI 算力 / 半导体",
    "title": "Big tech spends more than $1 trillion on AI infrastructure — additional $745 billion expected to be added to the figure in 2026 alone",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/big-tech-spends-more-than-usd1-trillion-on-ai-infrastructure-additional-usd745-billion-expected-to-be-added-to-the-figure-in-2026-alone",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T16:30:34+00:00",
    "summary": "Amazon, Google, Meta, and Microsoft have collectively spent more than $1 trillion on AI investments since the rush started in 2023. However, the big four are planning to spend more on AI CAPEX, with b"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/30-years-of-cpus-at-toms-hardware-looking-back-on-three-decades-of-processors-from-the-pentium-ii-to-ryzen-9-9950x3d2",
    "domain": "AI 算力 / 半导体",
    "title": "30 years of CPUs at Tom’s Hardware — looking back on three decades of processors, from the Pentium II to Ryzen 9 9950X3D2",
    "url": "https://www.tomshardware.com/pc-components/cpus/30-years-of-cpus-at-toms-hardware-looking-back-on-three-decades-of-processors-from-the-pentium-ii-to-ryzen-9-9950x3d2",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:13:36+00:00",
    "summary": "Tom’s Hardware has been covering CPUs for 30 years, and to celebrate, we’re looking back on the last three decades of CPU reviews and how the dynamics between Intel and AMD have shifted in that time."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/toms-hardwares-30th-anniversary-from-dip-switches-and-intel-feuds-to-30-years-of-unbiased-testing",
    "domain": "AI 算力 / 半导体",
    "title": "Tom’s Hardware’s 30th Anniversary — From Intel feuds and DIP switches to 30 years of unbiased testing",
    "url": "https://www.tomshardware.com/pc-components/toms-hardwares-30th-anniversary-from-dip-switches-and-intel-feuds-to-30-years-of-unbiased-testing",
    "source": "Paul Alcorn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:05:30+00:00",
    "summary": "We take a look back at the history of Tom’s Hardware as we celebrate our 30-year anniversary."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/apple-nearly-doubled-its-inventory-to-11-09-billion-as-memory-costs-ate-its-gross-margin",
    "domain": "AI 算力 / 半导体",
    "title": "Apple CEO Tim Cook says the company is fighting 'a hundred-year flood' on memory pricing — expects to pay even more for memory in September following recent price hikes",
    "url": "https://www.tomshardware.com/tech-industry/apple-nearly-doubled-its-inventory-to-11-09-billion-as-memory-costs-ate-its-gross-margin",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T14:54:55+00:00",
    "summary": "Apple will pay even more for memory in the September quarter than it did in the June quarter, CEO Tim Cook told analysts on the company's earnings call."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/beat-the-ai-price-surge-on-pc-hardware-leverage-newegg-combo-deals-track-amazon-prices-and-shop-refurb-outlets-like-woot",
    "domain": "AI 算力 / 半导体",
    "title": "Beat the AI price surge on PC hardware — leverage Newegg combo deals, track Amazon prices, and shop refurb outlets like Woot",
    "url": "https://www.tomshardware.com/pc-components/beat-the-ai-price-surge-on-pc-hardware-leverage-newegg-combo-deals-track-amazon-prices-and-shop-refurb-outlets-like-woot",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T13:10:00+00:00",
    "summary": "With prices skyrocketing, it’s more important than ever to follow these guidelines to help you find great deals on PC hardware."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/lumentum-ceo-says-the-indium-phosphide-shortage-will-become-worse-than-memory",
    "domain": "AI 算力 / 半导体",
    "title": "Lumentum CEO warns of impending bottleneck on critical material used for silicon photonics — fab and material shortfall already lags 30% below customer needs as co-packaged optics demand skyrockets",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/lumentum-ceo-says-the-indium-phosphide-shortage-will-become-worse-than-memory",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:45:27+00:00",
    "summary": "Lumentum CEO Michael Hurlston told an audience at the RAISE Summit that indium phosphide is heading into a squeeze worse than the one in memory."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/streaming-qr-codes-at-60-fps-achieves-nearly-190-kb-s-data-rate-in-phone-to-phone-tests-browser-based-method-requires-no-app-no-networking-no-pairing-and-no-permissions-beyond-camera-access",
    "domain": "AI 算力 / 半导体",
    "title": "Streaming QR codes at 60 FPS achieves nearly 190 KB/s data rate in phone-to-phone tests — browser-based method requires no app, no networking, no pairing, and no permissions beyond camera access",
    "url": "https://www.tomshardware.com/networking/streaming-qr-codes-at-60-fps-achieves-nearly-190-kb-s-data-rate-in-phone-to-phone-tests-browser-based-method-requires-no-app-no-networking-no-pairing-and-no-permissions-beyond-camera-access",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:45:20+00:00",
    "summary": "A developer has created a QR code-driven proof-of-concept data transfer system that shuns any dedicated app requirement and neatly sidesteps mandatory networking, pairing, or giving permissions beyond"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/docking-stations-hubs/testing-three-sub-usd400-thunderbolt-5-docking-stations",
    "domain": "AI 算力 / 半导体",
    "title": "Sub-$400 Thunderbolt 5 dock roundup — Keychron and Plugable offer dual HDMI, but UGREEN takes top spot with an M.2 NVMe slot",
    "url": "https://www.tomshardware.com/peripherals/docking-stations-hubs/testing-three-sub-usd400-thunderbolt-5-docking-stations",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:40:00+00:00",
    "summary": "All three Thunderbolt 5 docks offer similar performance, but one really stands out with its features."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/valve-funding-port-of-linux-radv-radeon-vulkan-driver-to-windows-cross-platform-effort-already-runs-counter-strike-2",
    "domain": "AI 算力 / 半导体",
    "title": "Valve funding port of Linux RADV Radeon Vulkan driver to Windows — cross-platform effort already runs 'Counter-Strike 2'",
    "url": "https://www.tomshardware.com/software/linux/valve-funding-port-of-linux-radv-radeon-vulkan-driver-to-windows-cross-platform-effort-already-runs-counter-strike-2",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:25:00+00:00",
    "summary": "Valve funding port of Linux RADV Radeon Vulkan driver to Windows — cross-platform effort already runs Counter-Strike 2"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/setting-up-openclaw-isnt-as-straightforward-as-the-internet-wants-you-to-think-running-local-ai-on-humble-hardware",
    "domain": "AI 算力 / 半导体",
    "title": "Setting up OpenClaw isn’t as straightforward as the internet wants you to think – running local AI on humble hardware",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/setting-up-openclaw-isnt-as-straightforward-as-the-internet-wants-you-to-think-running-local-ai-on-humble-hardware",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:20:00+00:00",
    "summary": "How realistic is it to run a local AI model and have it automate tasks for you using hardware that doesn’t cost the Earth? We gave it a shot with a Gorgon Point-powered Mini PC, with mixed results."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/sovol-m1d-3d-printer-is-the-first-open-source-idex-design-with-an-integrated-tool-changer-seven-heads-for-quick-swapping-materials-with-two-fully-independent-nozzles",
    "domain": "AI 算力 / 半导体",
    "title": "New open source printer has 7 toolheads that swap in 5 seconds for fast, zero-waste multi-color 3D printing — Sovol M1D 3D printer is the first open-source IDEX design with an integrated tool-changer",
    "url": "https://www.tomshardware.com/3d-printing/sovol-m1d-3d-printer-is-the-first-open-source-idex-design-with-an-integrated-tool-changer-seven-heads-for-quick-swapping-materials-with-two-fully-independent-nozzles",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:00:00+00:00",
    "summary": "Sovol M1D 3D printer is the first open-source IDEX design with an integrated tool-changer — seven heads for quick-swapping materials with two fully independent nozzles, with 300x300x350mm print volume"
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
    "points": 17,
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
    "id": "hn:49111237",
    "domain": "大厂 AI 动态",
    "title": "Gemini Robotics 2 brings whole body intelligence to robots",
    "url": "https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/",
    "source": "ai2027",
    "platform": "hackernews",
    "points": 617,
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
    "points": 383,
    "published_at": "2026-07-29T11:44:33+00:00",
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
    "id": "hn:49135399",
    "domain": "大厂 AI 动态",
    "title": "The Bedrock of Software Design",
    "url": "https://alex.draftist.io/blog/the-bedrock-of-software-design-ycqvcedsj",
    "source": "birdculture",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-08-01T15:43:40+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/974271/rachika-nayars-heaven-come-crashing-music-review",
    "domain": "大厂 AI 动态",
    "title": "Rachika Nayar’s Heaven Come Crashing is an instrumental epic of desperate longing",
    "url": "https://www.theverge.com/entertainment/974271/rachika-nayars-heaven-come-crashing-music-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T21:53:15+00:00",
    "summary": "Two minutes and thirty seconds into the title track of Rachika Nayar's Heaven Come Crashing, an absolutely massive drum and bass beat drops. As a fan of Nayar's debut record Our Hands Against The Dusk"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/974265/fender-ceo-bud-cole-ai-music",
    "domain": "大厂 AI 动态",
    "title": "Fender’s CEO seems to think your bandmates are just analog AI",
    "url": "https://www.theverge.com/ai-artificial-intelligence/974265/fender-ceo-bud-cole-ai-music",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T19:36:08+00:00",
    "summary": "Fender CEO Edward \"Bud\" Cole gave an interview to T3 in May celebrating the 75th anniversary of the Telecaster with comments on AI and music that initially flew under the radar. But it has started mak"
  },
  {
    "id": "rss:https://www.theverge.com/games/974253/xbox-prices-increasing-200-euros",
    "domain": "大厂 AI 动态",
    "title": "Xbox prices are increasing by up to €200 or £170",
    "url": "https://www.theverge.com/games/974253/xbox-prices-increasing-200-euros",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T16:14:20+00:00",
    "summary": "When Microsoft announced its latest round of Xbox price bumps in June, it only gave US pricing. Now we know the pricing increases for the EU and UK, and they're dramatic. Depending on the model, Xbox "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/973789/skylight-calendar-2-max-back-to-school-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Skylight&#8217;s smart calendars are up to $90 off during its back-to-school sale",
    "url": "https://www.theverge.com/gadgets/973789/skylight-calendar-2-max-back-to-school-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T15:00:00+00:00",
    "summary": "The start of a new school year can feel hectic, as parents juggle their kids’ classes, extracurriculars and sports on top of work, appointments, and other responsibilities. It&#8217;s easy for things "
  },
  {
    "id": "rss:https://www.theverge.com/tech/974155/hp-hyperx-omen-15-gaming-laptop-rtx-5050-review",
    "domain": "大厂 AI 动态",
    "title": "HP’s HyperX Omen 15 isn’t quite the budget-friendly gaming laptop its predecessor was",
    "url": "https://www.theverge.com/tech/974155/hp-hyperx-omen-15-gaming-laptop-rtx-5050-review",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T14:00:00+00:00",
    "summary": "The HP HyperX Omen 15, which I first saw at CES, replaces the HP Victus 15, a longtime bestselling budget gaming laptop. The Victus cost just $800, or less when on sale, and was a good entry point to "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/974018/pippa-seedance-artist-royalties",
    "domain": "大厂 AI 动态",
    "title": "Is paying artists enough to convince them to embrace AI?",
    "url": "https://www.theverge.com/ai-artificial-intelligence/974018/pippa-seedance-artist-royalties",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T13:00:00+00:00",
    "summary": "Illustrators have spent years sounding the alarm about generative artificial intelligence startups training their models on artists' work without permission. They've pointed out how the practice is ta"
  },
  {
    "id": "rss:https://www.theverge.com/column/972937/foldable-phones-boring-apple",
    "domain": "大厂 AI 动态",
    "title": "Foldables are sort of boring now — and that’s great news for Apple",
    "url": "https://www.theverge.com/column/972937/foldable-phones-boring-apple",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T12:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more on smartphones and Android, follow Dominic Preston. The Stepback arrives in our subscribers' i"
  },
  {
    "id": "rss:https://www.theverge.com/tech/974238/pixel-11-specs-and-price-leak",
    "domain": "大厂 AI 动态",
    "title": "Pixel 11 specs and price leak with no surprises",
    "url": "https://www.theverge.com/tech/974238/pixel-11-specs-and-price-leak",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T21:31:24+00:00",
    "summary": "Android Headlines claims to have the specs and price for the entire Pixel 11 lineup. What the site shared basically lines up with everything else that we've heard in the lead-up to the August 12th eve"
  },
  {
    "id": "rss:https://www.theverge.com/report/974226/angela-nissel-interview-good-grief-pass-the-bread-mom-is-dead",
    "domain": "大厂 AI 动态",
    "title": "Angela Nissel faces down grief with a laugh",
    "url": "https://www.theverge.com/report/974226/angela-nissel-interview-good-grief-pass-the-bread-mom-is-dead",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T20:15:00+00:00",
    "summary": "Angela Nissel's latest book, Good Grief, Pass the Bread, Mom Is Dead, is my kind of memoir. Sure, it's a deeply emotional tale about caring for a terminally ill parent. But it's delivered with the sor"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/974209/fenix-flexin-billboard-hot-100-rubberz-ai-slop",
    "domain": "大厂 AI 动态",
    "title": "Is this Billboard Hot 100 hit AI slop?",
    "url": "https://www.theverge.com/ai-artificial-intelligence/974209/fenix-flexin-billboard-hot-100-rubberz-ai-slop",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T18:20:00+00:00",
    "summary": "Fenix Flexin is best known as a member of Shoreline Mafia, a rap duo from Los Angeles. But he's recently found solo success with the track \"Rubberz,\" which has climbed to number 58 on the Billboard Ho"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/02/the-global-memory-shortage-hits-the-macbook-air/",
    "domain": "大厂 AI 动态",
    "title": "The global memory shortage hits the MacBook Air",
    "url": "https://techcrunch.com/2026/08/02/the-global-memory-shortage-hits-the-macbook-air/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T21:33:59+00:00",
    "summary": "The global memory chip shortage appears to be affecting the availability of Apple’s most popular Mac."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/02/sam-altman-and-ais-decel-debate/",
    "domain": "大厂 AI 动态",
    "title": "Sam Altman and AI’s decel debate",
    "url": "https://techcrunch.com/2026/08/02/sam-altman-and-ais-decel-debate/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T20:54:22+00:00",
    "summary": "On the latest episode of Equity, we discuss why Sam Altman has calling on the industry to \"pace the rate of AI development.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/02/malaysia-is-reportedly-shutting-down-balaji-srinivasans-network-school/",
    "domain": "大厂 AI 动态",
    "title": "Malaysia is reportedly shutting down Balaji Srinivasan’s Network School",
    "url": "https://techcrunch.com/2026/08/02/malaysia-is-reportedly-shutting-down-balaji-srinivasans-network-school/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T17:05:07+00:00",
    "summary": "Let's see how this \"frontier community for techno-optimists\" is doing ..."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/02/techcrunch-mobility-two-roads-diverged-for-robotaxis/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: Two roads diverged — for robotaxis",
    "url": "https://techcrunch.com/2026/08/02/techcrunch-mobility-two-roads-diverged-for-robotaxis/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T16:05:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, the role AI is playing in it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/02/these-app-store-hidden-gems-prove-theres-still-room-for-great-software-in-the-ai-era/",
    "domain": "大厂 AI 动态",
    "title": "These App Store hidden gems prove there’s still room for great software in the AI era",
    "url": "https://techcrunch.com/2026/08/02/these-app-store-hidden-gems-prove-theres-still-room-for-great-software-in-the-ai-era/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T15:23:19+00:00",
    "summary": "Despite predictions that AI agents could make traditional apps obsolete, developers are shipping new software faster than ever. From smarter bookmarking tools and neighborhood marketplaces to digital "
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/inside-one-london-founder-house-rewriting-the-founder-house-rules/",
    "domain": "大厂 AI 动态",
    "title": "Inside the London hacker house taking a stand against founder burnout",
    "url": "https://techcrunch.com/2026/08/01/inside-one-london-founder-house-rewriting-the-founder-house-rules/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T21:14:48+00:00",
    "summary": "How one founder house is betting work-life balance can beat burnout ."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/judge-denies-xais-request-to-block-minnesota-ban-on-nudify-apps/",
    "domain": "大厂 AI 动态",
    "title": "Judge denies xAI’s request to block Minnesota ban on ‘nudify’ apps",
    "url": "https://techcrunch.com/2026/08/01/judge-denies-xais-request-to-block-minnesota-ban-on-nudify-apps/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T20:26:04+00:00",
    "summary": "Despite a lawsuit from xAI, a Minnesota ban on apps that allow users to “nudify” images can move forward."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/youtuber-hank-green-says-his-ai-usage-is-not-healthy/",
    "domain": "大厂 AI 动态",
    "title": "YouTuber Hank Green says his AI usage is ‘not healthy’",
    "url": "https://techcrunch.com/2026/08/01/youtuber-hank-green-says-his-ai-usage-is-not-healthy/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T19:45:45+00:00",
    "summary": "Green offered a remarkable apology, saying that \"the level of dopamine that I've been getting from interacting with LLMs ... is not healthy for me or good for the world.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/should-you-still-buy-your-next-smartphone-or-subscribe-to-it-instead/",
    "domain": "大厂 AI 动态",
    "title": "Should you still buy your next smartphone — or subscribe to it instead?",
    "url": "https://techcrunch.com/2026/08/01/should-you-still-buy-your-next-smartphone-or-subscribe-to-it-instead/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T18:47:27+00:00",
    "summary": "Apple's new Upgrade program is the latest sign that smartphone ownership is changing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/sam-altman-is-still-making-the-case-for-parenting-via-chatgpt/",
    "domain": "大厂 AI 动态",
    "title": "Sam Altman is still making the case for parenting via ChatGPT",
    "url": "https://techcrunch.com/2026/08/01/sam-altman-is-still-making-the-case-for-parenting-via-chatgpt/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T17:07:34+00:00",
    "summary": "OpenAI's CEO seemed excited to share a \"cool use case\" for parents."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/this-9-key-physically-locks-your-most-addictive-apps/",
    "domain": "大厂 AI 动态",
    "title": "This $9 key physically locks your most addictive apps",
    "url": "https://techcrunch.com/2026/08/01/this-9-key-physically-locks-your-most-addictive-apps/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T15:58:17+00:00",
    "summary": "This $9 NFC key requires you to physically scan it to unlock distracting apps on your phone."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/ubers-autonomous-vehicle-deal-tracker/",
    "domain": "大厂 AI 动态",
    "title": "Uber is building an autonomous vehicle empire, and here’s every company it’s using to do it",
    "url": "https://techcrunch.com/2026/08/01/ubers-autonomous-vehicle-deal-tracker/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T15:05:00+00:00",
    "summary": "Uber has partnered with — and in some cases made direct investments in — about 30 autonomous vehicle companies over the past two years. Here's the list and the latest on the partnerships."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/apps-that-help-you-break-free-from-doomscrolling-and-get-active/",
    "domain": "大厂 AI 动态",
    "title": "Apps that help you break free from doomscrolling and get active",
    "url": "https://techcrunch.com/2026/08/01/apps-that-help-you-break-free-from-doomscrolling-and-get-active/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T14:00:00+00:00",
    "summary": "If you’re looking to cut back on screen time and get a little more active, here’s a roundup of the apps that might help."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/whats-the-best-handheld-mini-fan/",
    "domain": "大厂 AI 动态",
    "title": "What’s the best handheld mini fan?",
    "url": "https://techcrunch.com/2026/08/01/whats-the-best-handheld-mini-fan/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T13:36:54+00:00",
    "summary": "From premium Shark and Dyson offerings to random Amazon devices, these mini fans will make your sweaty summer a little more managable."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/heres-how-engineers-plan-to-save-the-satellite-sent-to-save-nasas-swift-mission/",
    "domain": "大厂 AI 动态",
    "title": "Here's how engineers plan to save the satellite sent to save NASA's Swift mission",
    "url": "https://arstechnica.com/space/2026/08/heres-how-engineers-plan-to-save-the-satellite-sent-to-save-nasas-swift-mission/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T18:20:11+00:00",
    "summary": "\"We believe that a capture of Swift, an attempted capture of Swift, is very much in the cards.\""
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/08/review-yes-were-still-arguing-about-nolans-the-odyssey/",
    "domain": "大厂 AI 动态",
    "title": "Review: Yes, we're still arguing about Nolan's The Odyssey",
    "url": "https://arstechnica.com/culture/2026/08/review-yes-were-still-arguing-about-nolans-the-odyssey/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T15:19:04+00:00",
    "summary": "Christopher Nolan's impressionistic remix of Homer's epic poem finds the man behind the myth."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/08/reddit-ceo-on-ai-overviews-were-still-looking-for-that-win-win/",
    "domain": "大厂 AI 动态",
    "title": "As Reddit stock falls, CEO questions value of Google's AI Overviews",
    "url": "https://arstechnica.com/ai/2026/08/reddit-ceo-on-ai-overviews-were-still-looking-for-that-win-win/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T12:30:36+00:00",
    "summary": "Reddit may still be considering ending its licensing deal with Google."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/after-noise-complaints-judge-orders-waymo-to-stop-overnight-charging-in-santa-monica/",
    "domain": "大厂 AI 动态",
    "title": "After noise complaints, judge orders Waymo to stop overnight charging in Santa Monica",
    "url": "https://arstechnica.com/tech-policy/2026/08/after-noise-complaints-judge-orders-waymo-to-stop-overnight-charging-in-santa-monica/",
    "source": "Cyrus Farivar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T11:30:54+00:00",
    "summary": "Autonomous vehicle giant disturbs residents' sleep."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/08/defcons-new-badge-is-a-security-key-you-can-see-inside/",
    "domain": "大厂 AI 动态",
    "title": "Defcon's new badge is a security key you can see inside",
    "url": "https://arstechnica.com/security/2026/08/defcons-new-badge-is-a-security-key-you-can-see-inside/",
    "source": "Kim Zetter, wired.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T10:05:21+00:00",
    "summary": "A removable chip lets hackers inspect their badge—and keep using it after Defcon."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/how-fruit-flies-chase-invisible-ribbons-of-smell-to-get-to-their-source/",
    "domain": "大厂 AI 动态",
    "title": "How fruit flies chase invisible ribbons of smell to get to their source",
    "url": "https://arstechnica.com/science/2026/08/how-fruit-flies-chase-invisible-ribbons-of-smell-to-get-to-their-source/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T10:00:19+00:00",
    "summary": "Tracking smells in turbulent air takes a keen sense of direction and sharp memory."
  },
  {
    "id": "rss:https://www.producthunt.com/products/lumichats-offline",
    "domain": "大厂 AI 动态",
    "title": "Lumichats",
    "url": "https://www.producthunt.com/products/lumichats-offline",
    "source": "Aditya Kumar Jha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T14:10:42+00:00",
    "summary": "A Claude Code alternative for people who avoid the terminal Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/bolcho-ai",
    "domain": "大厂 AI 动态",
    "title": "Bolcho AI",
    "url": "https://www.producthunt.com/products/bolcho-ai",
    "source": "Kumar Ajay",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T22:44:45+00:00",
    "summary": "Build Voice AI agents that actually speak India Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/termexo",
    "domain": "大厂 AI 动态",
    "title": "Termexo",
    "url": "https://www.producthunt.com/products/termexo",
    "source": "guomengyue",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T06:05:43+00:00",
    "summary": "A local Windows workbench for Claude Code and Codex Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/finamie-know-your-money-for-real",
    "domain": "大厂 AI 动态",
    "title": "Finamie",
    "url": "https://www.producthunt.com/products/finamie-know-your-money-for-real",
    "source": "Santiago Melo Medina",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T20:35:39+00:00",
    "summary": "Speak your expenses and get instant spending insights Discussion | Link"
  },
  {
    "id": "rss:https://36kr.com/p/3923374038265217?f=rss",
    "domain": "大厂 AI 动态",
    "title": "硬氪首发 | 硅光资深团队获数千万天使轮融资，瞄准CPO/OIO下一代光互连解决方案",
    "url": "https://36kr.com/p/3923374038265217?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T05:43:36+00:00",
    "summary": "硬氪获悉，光芯片企业量引科技近期完成天使轮数千万元融资，由珠海科技产业集团领投，珠海正方集团、险峰跟投。此次融资将用来扩充团队、迭代流片和补充设备。 量引科技成立于2024年，聚焦光子集成电路领域，致力于硅光子传输芯片(PIC)，Optical IO(OIO)及共封装光学(CPO)的研发及应用。 图源企业 公司创始团队融合了国内外研发和制造经验，创始人李耀基拥有30余年的集成电路行业经验，曾任重庆"
  },
  {
    "id": "rss:https://36kr.com/p/3923371035831684?f=rss",
    "domain": "大厂 AI 动态",
    "title": "前安克3D打印业务负责人要做B端工具产品，获数千万融资｜36氪首发",
    "url": "https://36kr.com/p/3923371035831684?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T05:40:12+00:00",
    "summary": "文｜张子怡 编辑｜袁斯来 36氪获悉，3D打印智能制造品牌「轻量智造（LightMake）」连续完成两轮共计超2500万元人民币融资，投资机构有海目星激光老板家族办公室、南山资本、卓源亚洲、朗翰资本。本轮融资资金主要用于产品研发、供应链体系搭建以及全球市场推广。 「轻量智造」成立于2025年，团队为中高端SMB（中小型企业）与Pro C（专业个人）用户研发生产桌面化、小型的“轻量化制造工具”，初代"
  },
  {
    "id": "rss:https://36kr.com/p/3923367465266824?f=rss",
    "domain": "大厂 AI 动态",
    "title": "36氪专访 | 对话大疆系Ebike公司：卖4万一辆的高端车，营收突破10亿，今年要翻四倍",
    "url": "https://36kr.com/p/3923367465266824?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T05:36:21+00:00",
    "summary": "文｜张子怡 编辑｜袁斯来 从大疆走出的 Ebike 公司 Amflow 进入赛道的时机谈不上好，那一年，不少中国Ebike厂商已选择战略性放弃或者转向美国市场。没人想到，它能将6499欧元起的高端Ebike卖出3万辆。 36氪独家获悉，从大疆独立的Ebike公司Amflow，整体营收已突破10亿元。同样从大疆诞生的Ebike助力系统品牌Avinox，已经有60多个客户，目前也已从大疆拆分独立运营。"
  },
  {
    "id": "rss:https://36kr.com/p/3923317976526208?f=rss",
    "domain": "大厂 AI 动态",
    "title": "36氪首发 | 商飞团队创业eVTOL再获数亿元融资，已进入适航关键阶段",
    "url": "https://36kr.com/p/3923317976526208?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:46:57+00:00",
    "summary": "作者&nbsp;|&nbsp;乔钰杰 编辑&nbsp;|&nbsp;袁斯来 硬氪获悉，电动垂直起降飞行器（eVTOL）研发制造商「亿维特航空」近日完成数亿元A+轮融资。本轮融资由上城资本、普华资本等投资，深蓝资本担任独家财务顾问。截至目前，亿维特航空已获得国家级基金、上市公司及地方国资等多方资本支持。 亿维特航空（以下简称“亿维特”）成立于2022年，定位为载人eVTOL飞行器研发制造。公司核心团"
  },
  {
    "id": "rss:https://36kr.com/p/3919025939246727?f=rss",
    "domain": "大厂 AI 动态",
    "title": "让Agent在协作中自进化，清华00后博士获千万元融资 | 36氪首发",
    "url": "https://36kr.com/p/3919025939246727?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T00:10:16+00:00",
    "summary": "文 | 赵京娜 访谈 编辑 | 海若镜 36氪获悉，近日奇点逃逸完成千万级种子轮融资，由星连资本与水木创投联合领投，奇绩创坛跟投。其正在研发AI原生团队协作操作系统Nexus，让人、Agent、任务、知识和工具基于同一份组织状态持续协作，并让系统从每一次协作中有证据地变强。 奇点逃逸创始人兼CEO薛传奕，本科、博士阶段均在清华大学就读，研究方向覆盖强化学习与多智能体，曾以第一作者身份在NeurIP"
  },
  {
    "id": "rss:https://36kr.com/p/3923043072634498?f=rss",
    "domain": "大厂 AI 动态",
    "title": "8点1氪丨蔡崇信宣布离婚，不涉及出售阿里股份；瑞幸回应员工对嘴喷奶油；IF椰子水市值从126亿暴跌到16亿",
    "url": "https://36kr.com/p/3923043072634498?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T00:07:39+00:00",
    "summary": "今日热点导览 马斯克关注了DeepSeek的X账号 祥鹏航空回应航班误发过期方便面 OpenAI或将IPO推迟到明年 SpaceX首份财报即将发布 小米多款手机正式涨价 每月10万美元，特朗普“真实社交”售卖“优先访问权” TOP3大新闻 蔡崇信宣布离婚，不涉及出售阿里股份 8月1日，阿里巴巴集团董事会主席、美国职业篮球队布鲁克林篮网主要所有者蔡崇信与妻子吴明华决定结束持续近30年的婚姻。声明称，"
  },
  {
    "id": "rss:https://36kr.com/p/3920595518533250?f=rss",
    "domain": "大厂 AI 动态",
    "title": "三天、十八场对谈、一个问题：ChinaJoy还只是游戏展吗？",
    "url": "https://36kr.com/p/3920595518533250?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T06:37:32+00:00",
    "summary": "如果有个人在零几年走进刚刚开办的 ChinaJoy 展馆，看到玩家排队试玩、ShowGirl 站在《魔兽世界》展台前、Coser 在《最终幻想》的海报前合影，他大概不会怀疑，这就是一个关于游戏的展会。&nbsp; 因为他是对的，在看似遥远的2004年，中国游戏市场正处于蓬勃发展的阶段。首届 ChinaJoy，是当时国内屈指可数的大型游戏展会。&nbsp; 但二十年多后，如果有人走进2026 年的 "
  },
  {
    "id": "hn:49057574",
    "domain": "股票",
    "title": "Google Discloses $94.1B in SpaceX Stock, Marking 6% Stake",
    "url": "https://www.wsj.com/tech/google-discloses-94-1-billion-in-spacex-stock-marking-6-stake-91655d7c",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 342,
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
    "id": "hn:49122994",
    "domain": "股票",
    "title": "Situational Awareness down 67% in July in AI stock rout",
    "url": "https://www.wsj.com/finance/investing/situational-awareness-down-67-in-july-in-ai-stock-rout-cd19901f",
    "source": "pondsider",
    "platform": "hackernews",
    "points": 155,
    "published_at": "2026-07-31T13:37:36+00:00",
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
    "id": "hn:49137024",
    "domain": "股票",
    "title": "Oil companies report sky-high profits thanks to wartime crude prices",
    "url": "https://www.npr.org/2026/07/31/nx-s1-5910660/big-oil-earnings-q2-2026",
    "source": "speckx",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-08-01T18:28:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:49136787",
    "domain": "股票",
    "title": "Reddit Stock Collapses 23% as AI Eats Away at User Growth",
    "url": "https://www.barchart.com/story/news/3584357/reddit-stock-collapses-23-as-ai-eats-away-at-user-growth",
    "source": "thm",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-08-01T18:03:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49111879",
    "domain": "股票",
    "title": "Citadel Buys Situational Awareness's Stock Portfolio After Big Losses in AI",
    "url": "https://www.wsj.com/finance/citadel-buys-situational-awarenesss-stock-portfolio-after-big-losses-in-ai-5117159b",
    "source": "mudil",
    "platform": "hackernews",
    "points": 53,
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
    "id": "wscn:3778557",
    "domain": "股票",
    "title": "KOSPI再暴跌超5%，韩国监管拟出手降杠杆：单股杠杆ETF倍数或直接砍至1倍",
    "url": "https://wallstreetcn.com/articles/3778557",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T06:28:39+00:00",
    "summary": "韩股再遭重挫，KOSDAQ触发熔断机制，三星电子、SK海力士单日跌超7%。监管层随即加速推进“紧急行动权限”立法，拟在市场剧烈波动时直接将单股杠杆ETF倍数从2倍强制下调至1.5倍乃至1.1倍。但机构普遍判断杠杆风险尚未完全出清，8月中旬政策落地前韩股高波动格局难以打破。"
  },
  {
    "id": "wscn:3778556",
    "domain": "股票",
    "title": "美日联手护盘日元，美国真实动机：防止日本抛售美债？",
    "url": "https://wallstreetcn.com/articles/3778556",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T06:22:10+00:00",
    "summary": "美日罕见联手干预汇市，名为保卫日元，实为华盛顿的“美债保卫战”。为防最大海外债主日本抛售美债筹资从而冲击长端收益率，美国被迫下场。双方高调借FIMA工具规避抛压，但这剂短期猛药终难医治日元结构性疲软的根本痼疾。"
  },
  {
    "id": "wscn:3778555",
    "domain": "股票",
    "title": "IPO后跌了四周、12亿股解禁压顶，SpaceX首份季报能否救股价？",
    "url": "https://wallstreetcn.com/articles/3778555",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T06:14:36+00:00",
    "summary": "SpaceX将于8月4日发布上市后首份季报。尽管其股价自高点已下挫46%且面临超12亿股解禁抛压，但市场聚焦于AI数据中心租赁带来的营收弹性、Starlink订阅用户增长以及Starship第14次飞测进展。华尔街预估二季度营收约69亿美元，该财报被视为能否扭转股价颓势的关键。"
  },
  {
    "id": "wscn:3778400",
    "domain": "股票",
    "title": "美日双方联合干预：日元暴涨3.5%会否仍是昙花一现？",
    "url": "https://wallstreetcn.com/premium/articles/3778400?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T05:35:55+00:00",
    "summary": "美日联合干预虽短期见效并确立底部，但日元中长期趋势难逆转，后市或宽幅震荡。"
  },
  {
    "id": "wscn:3778526",
    "domain": "股票",
    "title": "美伊谈判乐观情绪升温、油价大跌，韩国芯片股重挫，SK海力士跌超8%，日元走强",
    "url": "https://wallstreetcn.com/articles/3778526",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T05:30:05+00:00",
    "summary": "布伦特原油一度大跌逾7%，美国国债全线上涨，纳斯达克100指数期货和欧洲股指期货均上涨约0.9%。韩国KOSPI指数大跌逾5%，三星电子和SK海力士均暴跌超8%，拖累亚洲芯片股区域指数下挫1.2%。美元兑日元一度上涨1.4%至155.23。"
  },
  {
    "id": "wscn:3778553",
    "domain": "股票",
    "title": "阿里涨超6%，千问打开Token新入口？",
    "url": "https://wallstreetcn.com/articles/3778553",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:58:33+00:00",
    "summary": "市场开始buy in阿里的Token流动逻辑。"
  },
  {
    "id": "wscn:3778515",
    "domain": "股票",
    "title": "办公Agent“三国杀”：字节、阿里、腾讯AI战略吞噬一切，软件应用面临大洗牌？",
    "url": "https://wallstreetcn.com/premium/articles/3778515?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:34:48+00:00",
    "summary": "字节将飞书产品团队并入豆包、销售体系并入火山引擎，震惊了业界。"
  },
  {
    "id": "wscn:3778547",
    "domain": "股票",
    "title": "吴清：正在抓紧推进人民币股票交易柜台、REITs纳入沪深港通各项准备工作",
    "url": "https://wallstreetcn.com/articles/3778547",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:33:31+00:00",
    "summary": "吴清表示，将一如既往地支持拓展国际布局的境内企业赴港上市，支持优质港股上市公司境内上市，共同提升服务新质生产力发展质效。当前中国证监会会同香港方面正在抓紧推进人民币股票交易柜台、REITs纳入沪深港通各项准备工作。支持香港推出更多人民币计价结算的期货品种，构建更加多元化的资产生态。"
  },
  {
    "id": "wscn:3778549",
    "domain": "股票",
    "title": "三星芯片工程师，纷纷跳槽SK海力士",
    "url": "https://wallstreetcn.com/articles/3778549",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:12:12+00:00",
    "summary": "AI芯片军备赛引爆半导体人才战争。SK海力士凭借HBM芯片豪掷47.6万美元奖金，三星某个工程师部门集体倒戈——30人团队几乎全员投递竞争对手简历，连老板也鼓励跳槽。三星诉诸法院、美光工人酝酿罢工，一场由AI红利分配不均引发的全球芯片人才争夺战正全面升级。"
  },
  {
    "id": "wscn:3778543",
    "domain": "股票",
    "title": "科创50跌超3%，半导体产业链齐跌，核电板块逆势爆发，恒科指涨0.7%，阿里大涨近7%",
    "url": "https://wallstreetcn.com/articles/3778543",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:04:27+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市超3700股飘红，上午半天成交1.37万亿，沪深两市半日成交额1.37万亿，较上个交易日缩量超4200亿。板块方面，半导体、算力硬件产业链再度回调，存储器、HBM、先进封装、PCB方向领跌；券商、医药板块跌幅靠前。核聚变、光伏、特高压、商业航天、宇树机器人概念股走强。"
  },
  {
    "id": "wscn:3778548",
    "domain": "股票",
    "title": "晚加息不如早加息？本次7月FOMC会议传递了什么信号？【程坦说 第4讲】",
    "url": "https://wallstreetcn.com/premium/articles/3778548?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T03:24:37+00:00",
    "summary": "沃什做错了什么？"
  },
  {
    "id": "wscn:3778546",
    "domain": "股票",
    "title": "性能与Anthropic Fable 5相当！阿里巴巴发布千问3.8-MAX，2.4万亿个参数，长程自动编程表现出色",
    "url": "https://wallstreetcn.com/articles/3778546",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T03:07:40+00:00",
    "summary": "阿里巴巴发布千问3.8-Max，参数规模达2.4万亿，是千问家族迄今最强模型，也是首个开源Max级权重的版本（下周发布）。API定价输入2.0美元/百万tokens、输出6.0美元/百万tokens。基准测试显示其编程与通用智能体能力与Anthropic Fable5相当，部分指标超越，并在芯片设计、量化研究、电商模拟等长程任务中展现出显著的自主执行能力。"
  },
  {
    "id": "wscn:3778365",
    "domain": "股票",
    "title": "韩国为何总是全球金融风险的第一预警器？",
    "url": "https://wallstreetcn.com/premium/articles/3778365?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T02:47:16+00:00",
    "summary": "韩国作为全球经济金丝雀，因出口与外资高敏感领先周期，持续为全球金融风险与AI周期变化提供前瞻预警。"
  },
  {
    "id": "wscn:3778544",
    "domain": "股票",
    "title": "出海加速！华尔街判断：中国新能源车空头回补仍将持续",
    "url": "https://wallstreetcn.com/articles/3778544",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T02:46:35+00:00",
    "summary": "中国新能源车7月批发量同比大增23%、环比转正，超出市场预期，叠加库存去化与出口占比升至37%，华尔街集体上调判断——花旗明确指出汽车板块空头回补将持续。比亚迪出口破18万辆、奇瑞出口占比高达75%，出口已从边际增量跃升为车企销量主干。但盈利兑现仍待二季度业绩季验证，旺季能否承接成关键。"
  },
  {
    "id": "wscn:3778540",
    "domain": "股票",
    "title": "高盛旗帜鲜明：这是人类历史上最大规模的资本需求周期，美联储只是看客",
    "url": "https://wallstreetcn.com/articles/3778540",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T02:32:30+00:00",
    "summary": "高盛认为，全球正从储蓄过剩时代切换至资本极度稀缺时代，AI基建、再工业化、国防重整与主权债务需求同时爆发，30年期美债收益率已突破金融危机前水平，且这一趋势与美联储政策关系不大。美联储“更多是乘客而非司机”，短期内不应期待收益率回落。资本成本结构性抬升将重写投资范式，8月市场将相对平静，但中期前景并不简单。"
  },
  {
    "id": "wscn:3778539",
    "domain": "股票",
    "title": "核电新周期启幕： 全球能源格局重塑中的十万亿红利",
    "url": "https://wallstreetcn.com/premium/articles/3778539?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T02:10:26+00:00",
    "summary": "\"十五五\"首批8台机组核准之际，重新审视核电产业链的长期价值。"
  },
  {
    "id": "wscn:3778538",
    "domain": "股票",
    "title": "中金：AI之外还有什么值得买",
    "url": "https://wallstreetcn.com/articles/3778538",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T02:10:01+00:00",
    "summary": "全球AI链遭遇杠杆出清，韩国KOSPI一度暴跌近40%，而港股、消费、分红板块却逆势反弹。中金研究指出，AI调整进入中后段，但产业新催化尚未出现，市场正从\"只买胜率\"转向兼顾赔率。模型显示，保险、创新药、原材料、标普500、长端美债等方向当前综合打分居前，或成资金再平衡的最优出口。"
  },
  {
    "id": "wscn:3778530",
    "domain": "股票",
    "title": "去杠杆冲击之下，算力核心逻辑变了吗？",
    "url": "https://wallstreetcn.com/articles/3778530",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T02:09:50+00:00",
    "summary": "韩国存储去杠杆触发全球算力链风险重定价，但中信建投指出，这并非AI需求逆转，而是市场重估涨价与高利润率的持续性。SK会长称AI半导体价格“非正常高位”，三大厂加码长协、扩产与本土化，从“供给纪律”转向“稳价扩量”。下半年算力逻辑重排：涨价斜率边际放缓，订单兑现和产能释放的定价权重上升。"
  },
  {
    "id": "wscn:3778541",
    "domain": "股票",
    "title": "中国7月RatingDog制造业PMI连续八个月扩张，新出口订单三个月来首次回正",
    "url": "https://wallstreetcn.com/articles/3778541",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T01:56:08+00:00",
    "summary": "RatingDog创始人Yao Yu认为，制造业在7月整体维持扩张，持续增长的新订单和不断缓解的成本压力提供了支撑，出口订单重返扩张也释放出积极信号。\"制造业PMI预计短期内将继续保持在扩张区间，但增长节奏可能进一步趋于温和。\""
  },
  {
    "id": "wscn:3778193",
    "domain": "股票",
    "title": "3个信号同时出现：长鑫这条“鲶鱼”，正在让韩国存储厂商失去定价权吗？",
    "url": "https://wallstreetcn.com/premium/articles/3778193?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T01:48:00+00:00",
    "summary": "SK海力士计划下半年量产LPDDR6，并可能首次供应小米，看似只是一条新品导入消息，放在更长的证据链中却有另一层含义：长鑫存储加速扩产，苹果尝试引入中国存储，OPPO、vivo拒绝接受韩厂大幅涨价，小米又重新上调出货目标。过去由三星、SK海力士和美光主导的移动内存市场，是否正从高度集中的卖方市场，转向供应商多元化下的重新平衡，而手机厂商也终于开始拿回部分采购话语权？"
  },
  {
    "id": "hn:49115139",
    "domain": "股票",
    "title": "Microsoft's $450B Jump Is Biggest in Stock Market History",
    "url": "https://www.bloomberg.com/news/articles/2026-07-30/microsoft-eyes-history-with-490-billion-pop-in-market-value",
    "source": "signatoremo",
    "platform": "hackernews",
    "points": 20,
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
    "points": 17,
    "published_at": "2026-07-30T18:54:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:49119293",
    "domain": "股票",
    "title": "Aschenbrenner's hedge fund forced to unwind all public stock positions",
    "url": "https://www.cnbc.com/2026/07/30/leopold-aschenbrenners-hedge-fund-is-facing-steep-ai-losses.html",
    "source": "akbabu",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-31T05:22:18+00:00",
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
    "id": "hn:49113358",
    "domain": "股票",
    "title": "South Korea's stock market plunges as AI-driven boom fades",
    "url": "https://www.aljazeera.com/economy/2026/7/29/south-koreas-stock-market-plunges-as-ai-driven-boom-fades",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-30T17:54:23+00:00",
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
    "title": "The bond market isn’t buying what Fed Chair Warsh is selling",
    "url": "https://www.reuters.com/commentary/reuters-open-interest/bond-market-isnt-buying-what-fed-chair-warsh-is-selling-2026-07-30/",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 138,
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
    "points": 157,
    "published_at": "2026-07-25T11:04:57+00:00",
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
    "id": "rss:https://arxiv.org/abs/2607.28790",
    "domain": "金融",
    "title": "Arbitrage and rents in European long-term transmission rights",
    "url": "https://arxiv.org/abs/2607.28790",
    "source": "Clemens Stiewe",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2607.28790v1 Announce Type: new Abstract: Long-term transmission rights (LTTRs) are designed to support hedging in interconnected European electricity markets. LTTR auction prices have historica"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28820",
    "domain": "金融",
    "title": "What's in a Queue? An Experimental Study of Job Ordering, Autonomy and Queue Visibility",
    "url": "https://arxiv.org/abs/2607.28820",
    "source": "Evgeny Kagan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2607.28820v1 Announce Type: new Abstract: Problem Definition: How a queue of jobs is arranged and presented to workers is an important design problem in service operations. This includes choosin"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28842",
    "domain": "金融",
    "title": "University as a Melting Pot: Long-term Effects of Internationalization",
    "url": "https://arxiv.org/abs/2607.28842",
    "source": "Stanislav Avdeev",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2607.28842v1 Announce Type: new Abstract: This paper provides the first evidence on the impact of exposure to international students on the long-term outcomes of native students. I combine uniqu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28847",
    "domain": "金融",
    "title": "Effort-Centric Fairness in Lending Decisions",
    "url": "https://arxiv.org/abs/2607.28847",
    "source": "Shiqi Fang, Zexun Chen, Jake Ansell",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2607.28847v1 Announce Type: new Abstract: Algorithmic credit scoring must satisfy fairness and explanation requirements, yet prevailing predictive-parity criteria assess only outcomes at the dec"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.29162",
    "domain": "金融",
    "title": "Geography in Online Capital Allocation: Evidence from Equity-Based Crowdfunding",
    "url": "https://arxiv.org/abs/2607.29162",
    "source": "Keiichi Kawai, Akira Matsushita",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2607.29162v1 Announce Type: new Abstract: Digital investment platforms reduce search costs, yet realized investments can remain geographically concentrated. Such concentration alone cannot disti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.29210",
    "domain": "金融",
    "title": "The Collapse of Human Capital Ladders in Recessions",
    "url": "https://arxiv.org/abs/2607.29210",
    "source": "Edoardo Maria Acabbi, Andrea Alati, Luca Mazzone",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2607.29210v1 Announce Type: new Abstract: Using administrative data, we document that workers acquire more human capital at more productive firms. Recessions distort workers-firm sorting, flatte"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.29220",
    "domain": "金融",
    "title": "Decoupled Probabilistic Forecasting and Arbitrage-Aware Refinement of Implied Volatility Surfaces",
    "url": "https://arxiv.org/abs/2607.29220",
    "source": "Lifeng Hao, Shaolin Ji",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2607.29220v1 Announce Type: new Abstract: Implied volatility surface forecasting is essential for option valuation, hedging,and risk management, but remains difficult because future surfaces are"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.29371",
    "domain": "金融",
    "title": "Unintended Consequences of Sanitation Investment: Negative Externalities on Water Quality and Health in India",
    "url": "https://arxiv.org/abs/2607.29371",
    "source": "Kazuki Motohashi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2607.29371v1 Announce Type: new Abstract: Developing countries have increased sanitation investment to improve child health. However, scaling up latrine construction can cause water pollution ex"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.29572",
    "domain": "金融",
    "title": "Artificial Intelligence: Supply-Chain Chokepoints and the Reach of Industrial Policy",
    "url": "https://arxiv.org/abs/2607.29572",
    "source": "Piyush Akimitsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2607.29572v1 Announce Type: new Abstract: Artificial intelligence depends on a stack of inputs, models on compute, compute on chips, and chips on electricity and refined minerals. This paper mea"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.29583",
    "domain": "金融",
    "title": "Fund Competition under Conflicting ESG Rating Methodologies",
    "url": "https://arxiv.org/abs/2607.29583",
    "source": "Wanling Rudkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2607.29583v1 Announce Type: new Abstract: Competing ESG rating providers reward different portfolio attributes. This paper models funds that choose portfolios and fees for investors with heterog"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28780",
    "domain": "金融",
    "title": "Optimizing Monetization Strategies for Generative AI Firms: Implications for Search Engagement",
    "url": "https://arxiv.org/abs/2607.28780",
    "source": "Veronica Rosendo-Rios (Universidad Pontificia Comillas, ICADE, Madrid. Spain), Paurav Shukla (Southampton Business School, University of Southampton, Southampton. UK)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2607.28780v1 Announce Type: cross Abstract: As Generative Artificial Intelligence (GenAI) platforms, such as ChatGPT, have transformed digital search querying behavior, mounting operational cost"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.29024",
    "domain": "金融",
    "title": "A Policy Iteration Scheme for Semilinear Stochastic Hamilton-Jacobi-Bellman Equations with Exponential Convergence",
    "url": "https://arxiv.org/abs/2607.29024",
    "source": "Hasib Uddin Molla, Jinniao Qiu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2607.29024v1 Announce Type: cross Abstract: This paper is concerned with the non-Markovian stochastic optimal control problems in which the value function is a random field characterized by a st"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.29380",
    "domain": "金融",
    "title": "The Tragedy of the Cognitive Commons: How AI Could Disrupt the Regeneration of Professional Expertise",
    "url": "https://arxiv.org/abs/2607.29380",
    "source": "Nolan Lovett",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2607.29380v1 Announce Type: cross Abstract: Artificial intelligence is reshaping cognitive work, but Human Resource Development scholarship has treated this transformation as an organizational t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2210.14631",
    "domain": "金融",
    "title": "How Money Enters Before It Leaves: Experimental Remuneration and the Mobile-Payment Effect",
    "url": "https://arxiv.org/abs/2210.14631",
    "source": "Yizhao Jiang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2210.14631v2 Announce Type: replace Abstract: Consequential purchasing experiments typically focus on how money leaves a consumer. When an experiment provides spendable funds before valuation, h"
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.22616",
    "domain": "金融",
    "title": "How Do Regulations and Technology Affect Service Allocation and Market Structure?",
    "url": "https://arxiv.org/abs/2410.22616",
    "source": "Piyush Akimitsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2410.22616v5 Announce Type: replace Abstract: The paper estimates the effects of Price Controls and Cost Controls on healthcare service quantity and their role in spatial restructuring of physic"
  },
  {
    "id": "rss:https://arxiv.org/abs/2504.06932",
    "domain": "金融",
    "title": "High-frequency intraday trading for battery storages",
    "url": "https://arxiv.org/abs/2504.06932",
    "source": "David Schaurecker, David Wozabal, Nils L\\\"ohndorf, Thorsten Staake",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2504.06932v4 Announce Type: replace Abstract: Maximizing revenue for grid-scale battery energy storage systems in continuous intraday electricity markets requires strategies that are able to sei"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.22896",
    "domain": "金融",
    "title": "Portfolio Analysis Based on Markowitz Stochastic Dominance Criteria: A Behavioral Perspective",
    "url": "https://arxiv.org/abs/2509.22896",
    "source": "Peng Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2509.22896v2 Announce Type: replace Abstract: This paper develops stochastic optimization problems for describing and analyzing behavioral investors with Markowitz Stochastic Dominance (MSD) pre"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.17481",
    "domain": "金融",
    "title": "Universalization and the Origins of Fiscal Capacity",
    "url": "https://arxiv.org/abs/2510.17481",
    "source": "Esteban Mu\\~noz-Sobrado",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2510.17481v4 Announce Type: replace Abstract: This paper proposes a model of tax compliance and fiscal capacity grounded in universalization reasoning. Citizens partially internalize the consequ"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.16120",
    "domain": "金融",
    "title": "Abortion Bans and Young Women's Labor Supply: Evidence from the Dobbs Decision",
    "url": "https://arxiv.org/abs/2511.16120",
    "source": "Rintaro Ando",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2511.16120v2 Announce Type: replace Abstract: This paper studies the impact of the 2022 Dobbs decision and subsequent state level abortion bans on the labor supply of young women (ages 18-24). U"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.14680",
    "domain": "金融",
    "title": "Long-run survival in limited stock market participation models with power utilities",
    "url": "https://arxiv.org/abs/2512.14680",
    "source": "Heeyoung Kwon, Kasper Larsen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2512.14680v2 Announce Type: replace Abstract: We extend the limited participation model in Basak and Cuoco (1998) to allow for traders with different time-preference coefficients but identical c"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.10857",
    "domain": "金融",
    "title": "SPX-VIX Risk Computations Via Perturbed Optimal Transport",
    "url": "https://arxiv.org/abs/2603.10857",
    "source": "Charlie Che, Hanxuan Lin, Yudong Yang, Guofan Hu, Lei Fang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2603.10857v3 Announce Type: replace Abstract: We propose a model independent framework for generating SPX and VIX risk scenarios based on a joint optimal transport calibration of their market sm"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.25283",
    "domain": "金融",
    "title": "Competitive satellite placement and the economic geography of the geostationary orbit",
    "url": "https://arxiv.org/abs/2606.25283",
    "source": "Akhil Rao, Nikodem Szumilo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2606.25283v2 Announce Type: replace Abstract: The geostationary orbit (GEO) carries most of the world's satellite communications revenue. The International Telecommunication Union (ITU) coordina"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.25909",
    "domain": "金融",
    "title": "General Equilibrium Effects of Carbon Offsets",
    "url": "https://arxiv.org/abs/2606.25909",
    "source": "Isla Globus-Harris, Daniel H Karney",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2606.25909v2 Announce Type: replace Abstract: We construct an analytical general equilibrium model of an economy with carbon offsets, and show that increasing the carbon offset price has an ambi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.01198",
    "domain": "金融",
    "title": "When large trades are not (automatically) news: liquidity tail risk and price discovery",
    "url": "https://arxiv.org/abs/2607.01198",
    "source": "Umut \\c{C}etin, Mingwei Lin, Giulia Livieri",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2607.01198v3 Announce Type: replace Abstract: We examine how heavy-tailed liquidity demand changes price discovery in a sequential limit order book with asymmetric information. In our setting, l"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.23424",
    "domain": "金融",
    "title": "Wrong and More Confident: A Field Experiment on Large Language Models Taking a Graduate Economics Exam",
    "url": "https://arxiv.org/abs/2607.23424",
    "source": "Piyush Akimitsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2607.23424v3 Announce Type: replace Abstract: A red herring, an irrelevant passage added to a problem, corrupts a language model's reasoning and, through it, its final answer, while the form of "
  },
  {
    "id": "rss:https://arxiv.org/abs/2407.04521",
    "domain": "金融",
    "title": "Unified continuous-time q-learning for mean-field game and mean-field control problems",
    "url": "https://arxiv.org/abs/2407.04521",
    "source": "Xiaoli Wei, Xiang Yu, Fengyi Yuan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2407.04521v3 Announce Type: replace-cross Abstract: This paper studies the continuous-time q-learning in mean-field jump-diffusion models in a setting where the environment simulator does not pr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.20533",
    "domain": "金融",
    "title": "Incorporating data drift to perform survival analysis on credit risk",
    "url": "https://arxiv.org/abs/2601.20533",
    "source": "Jianwei Peng (Humboldt-Universit\\\"at zu Berlin), Stefan Lessmann (Humboldt-Universit\\\"at zu Berlin, Bucharest University of Economic Studies)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T04:00:00+00:00",
    "summary": "arXiv:2601.20533v2 Announce Type: replace-cross Abstract: Survival analysis has become a standard approach for modelling time to default by time-varying covariates in credit risk. Unlike most existing"
  },
  {
    "id": "hn:49097833",
    "domain": "金融",
    "title": "Show HN: The Federalist Papers, typeset as the 1787 newspapers they ran in",
    "url": "https://federalistreader.org/",
    "source": "vhwalke",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-07-29T14:13:54+00:00",
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
    "id": "hn:48999329",
    "domain": "金融",
    "title": "A Man Who Runs the IRS Spied on Colleagues When He Worked at JPMorgan",
    "url": "https://www.wsj.com/finance/banking/irs-bisignano-spying-jpmorgan-6cd1ddf0",
    "source": "cwwc",
    "platform": "hackernews",
    "points": 25,
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
    "id": "hn:48986112",
    "domain": "金融",
    "title": "The Fedora project grapples with change",
    "url": "https://lwn.net/SubscriberLink/1081557/cde56e450fe4bf10/",
    "source": "chmaynard",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-20T23:17:33+00:00",
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
    "id": "hn:48999988",
    "domain": "金融",
    "title": "Brazil and US clash over future of payments as Pix system stirs global interest",
    "url": "https://www.reuters.com/business/finance/brazil-us-clash-over-future-payments-popular-pix-system-stirs-global-interest-2026-07-21/",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-21T23:52:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48986211",
    "domain": "金融",
    "title": "Delayed Boeing jets only fit for baked bean tins, Emirates boss says",
    "url": "https://finance.yahoo.com/technology/articles/delayed-boeing-jets-only-fit-162341761.html",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-20T23:29:15+00:00",
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
  }
]
```
