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

- 今日日期：`2026-06-29`
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
  "date": "2026-06-29",
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
    "points": 3465098,
    "published_at": "2026-01-15T03:56:12+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署"
  },
  {
    "id": "bvid:BV1yjz5BLEoY",
    "domain": "AI",
    "title": "黑马程序员大模型RAG与Agent智能体项目实战教程，基于主流的LangChain技术从大模型提示词到实战项目",
    "url": "http://www.bilibili.com/video/av115931552416097",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 2812747,
    "published_at": "2026-01-21T06:06:02+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260121\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\n人工智能开发热门教程：\nAI大模型开发：BV1h1V"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1269631,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV14rzQB9EJj",
    "domain": "AI",
    "title": "Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill / Hook / 图片 / 上下文处理/ 后台任务",
    "url": "http://www.bilibili.com/video/av115954889596221",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1197944,
    "published_at": "2026-01-25T08:55:20+00:00",
    "summary": "时间戳如下，方便大家跳转观看：\n \n第一部分：环境搭建与基础交互\n- 01:09 安装 Claude Code\n- 01:43 登录与授权\n- 02:55 第一个实战问题\n- 03:12 三种模式详解 (默认/自动/规划)\n \n第二部分：复杂任务处理与终端控制\n- 06:00 执行终端命令 (Bash)\n- 06:49 使用规划模式 (Plan Mode)\n- 11:06 跳过所有权限检测 (da"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 799400,
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
    "points": 664829,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 627169,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1RSFUzVEAG",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码",
    "url": "http://www.bilibili.com/video/av116045469783373",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 542260,
    "published_at": "2026-02-10T08:59:28+00:00",
    "summary": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码"
  },
  {
    "id": "bvid:BV1BVEs6LENZ",
    "domain": "AI",
    "title": "【2026最新Codex】Codex保姆级完整教程-Codex新手保姆级教程-最强AI助手！从入门到进阶，22分钟速通Codex！【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av116707129561197",
    "source": "编程大佬陈悠秀",
    "platform": "bilibili",
    "points": 495681,
    "published_at": "2026-06-07T05:32:32+00:00",
    "summary": "最近Codex的能力越来越全面，变成了Codex四大形态里最强一个。 Codex APP 比起 Claude Code，额度更高，功能更全，免费账户也能用。而且不会出现限速、封号、降智等问题，用过的小伙伴直呼真香。本期视频带来一个Codex APP的完整教程"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 473828,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1TSg7zuEqR",
    "domain": "AI",
    "title": "Agent 的概念、原理与构建模式 —— 从零打造一个简化版的 Claude Code",
    "url": "http://www.bilibili.com/video/av114894200380730",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 468562,
    "published_at": "2025-07-22T01:07:39+00:00",
    "summary": "Agent 的概念、原理与构建模式 —— 从零打造一个简化版的 Claude Code\n \n我们将以 ReAct 和 Plan-And-Execute 这两种模式为例，为大家讲解 Agent 的概念、原理与构建模式，并在这个过程中为大家演示如何从零打造一个简化版的 Claude Code，让大家彻底明白 Agent 是如何运作的。\n \n时间轴：\n00:00 视频内容介绍\n00:33 什么是 Age"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 465473,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 377347,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1BFouBYERu",
    "domain": "AI",
    "title": "手把手教你在Claude Code中熟练使用SKILL技能！",
    "url": "http://www.bilibili.com/video/av116453927814340",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 334441,
    "published_at": "2026-04-23T12:09:57+00:00",
    "summary": "本期视频耗时半个月制作，希望大家能够点赞三连加关注，感谢！\n\n内容包括了一下几个方面：\n00:27 Skill简介\n01:39 Skill和Plugin的区别\n02:51 安装他人的Skill\n04:44 手动创建自己的SKill\n07:30 控制Skill的触发行为\n08:01 Skill的查看和管理\n08:20 Skill的停用和删除\n08:55 找优质Skill的三种渠道"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 261105,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 249634,
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
    "points": 245703,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1e3t4etExj",
    "domain": "AI",
    "title": "手摸手的AI编程cursor实战【小白教程】",
    "url": "http://www.bilibili.com/video/av113148447169565",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 227578,
    "published_at": "2024-09-17T01:00:00+00:00",
    "summary": "喜欢的朋友可以三连+关注～这对我真的很重要"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 227057,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1rv7A6oEeP",
    "domain": "AI",
    "title": "2026版LangChain教程，langchain快速入门， Agent智能体rag项目实战",
    "url": "http://www.bilibili.com/video/av116792827579053",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 177828,
    "published_at": "2026-06-23T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】LangChain学习一套通，从入门到三大综合项目实战"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 175755,
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
    "points": 158264,
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
    "points": 158075,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1HM7C6BEnF",
    "domain": "AI",
    "title": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！",
    "url": "http://www.bilibili.com/video/av116696929076767",
    "source": "AIAgent开发",
    "platform": "bilibili",
    "points": 148238,
    "published_at": "2026-06-05T10:11:18+00:00",
    "summary": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 145370,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1KoGE6cE53",
    "domain": "AI",
    "title": "🚀Claude Code重大突破：Workflow功能完整实战教程！ultrawork召唤无数个Agent协同！自动生成JS脚本实现可复用的精准可控工作流",
    "url": "http://www.bilibili.com/video/av116629702777532",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 110820,
    "published_at": "2026-05-24T13:11:48+00:00",
    "summary": "视频简介：\n 全球首测！Anthropic未官宣的Claude Code Workflow隐藏功能完整使用指南，三大阶段六种形态精准解析！AI编程进入脚本化新纪元\n\n 本期视频详细演示了Anthropic为Claude Code V2.1.47和V2.1.48秘密新增的颠覆性Workflow功能！这个被官方从Changelog中紧急删除却未从代码中移除的&quot;隐藏神器&quot;，将成为继M"
  },
  {
    "id": "bvid:BV1fRSfBWE5X",
    "domain": "AI",
    "title": "vlog｜白天上班 晚上vibe coding，准备一个月上架我的第一款App！",
    "url": "http://www.bilibili.com/video/av116357526003120",
    "source": "chocpink_AI版",
    "platform": "bilibili",
    "points": 98355,
    "published_at": "2026-04-06T11:33:25+00:00",
    "summary": "想了很久终于开始了这件事——vibe coding！\n\n下面快速总结了我用到的一些工具：\nApptweak：竞品调研\nfigma make、google stitch、impeccable插件：生成UI页面\nfigma mcp/plugin：连接到cursor\npinterest/小红书/iconfont：找图片/icon素材\nGrok：生图、素材优化\ncursor+Xcode（swift）：落地"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 90264,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1KocTzHE3Z",
    "domain": "AI",
    "title": "2027版 Cursor+Claude AI编程 1天快速上手 视频教程",
    "url": "http://www.bilibili.com/video/av116040285622077",
    "source": "java1234官方",
    "platform": "bilibili",
    "points": 64374,
    "published_at": "2026-02-09T10:57:55+00:00",
    "summary": "本课程主要讲解Cursor简介，Cursor下载安装，Cursor生成helloWorld网页，Cursor会话里的Cursor会话里的Agent,Plan,Debug,Ask区别以及使用，Cursor常用模型介绍，Cursor模型会话上下文介绍，以及最后利用Cursor Opus4.6快速生成一个Java项目 -SpringBoot4+Vue3的学生信息管理系统，利用Cursor Opus4.6"
  },
  {
    "id": "bvid:BV1VnEi6gELD",
    "domain": "AI",
    "title": "【B站强推】清华大佬终于把Agent教程做成动画片了，教学通俗易懂，2026最新版，学完即可就业！拿走不谢，别再走弯路了，学不会我退出IT界！Agent智能体",
    "url": "http://www.bilibili.com/video/av116729829131968",
    "source": "Agent产品经理",
    "platform": "bilibili",
    "points": 64208,
    "published_at": "2026-06-11T05:41:11+00:00",
    "summary": "【B站强推】清华大佬终于把Agent教程做成动画片了，教学通俗易懂，2026最新版，学完即可就业！拿走不谢，别再走弯路了，学不会我退出IT界！Agent智能体"
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 61224,
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
    "points": 57173,
    "published_at": "2026-02-06T03:17:18+00:00",
    "summary": "如何像传统互联网大厂一样指挥AI干活？本期视频通过一个“个人工作台”的实战项目，拆解了一套利用 LLM (Gemini) 辅助 Cursor 开发的高效工作流。\n\n核心内容：\n角色转换：你不是程序员，你是产品经理（PM）。\n文档驱动：如何用 AI 生成标准的产品文档 (PRD)、UI 文档和技术方案。\n避坑指南：如何防止 Cursor “手搓核弹”或开发中途“失忆”。\n\n实操流程：\nStep 1："
  },
  {
    "id": "bvid:BV1ZEJA6xEds",
    "domain": "AI",
    "title": "最新方法！国内免费无限制，使用Claude Code！",
    "url": "http://www.bilibili.com/video/av116746874848391",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 53556,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 52545,
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
    "points": 52405,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 32375,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1EZd3BBEB5",
    "domain": "AI",
    "title": "手把手实战教学：我是如何用一个周末掌握Claude Code的",
    "url": "http://www.bilibili.com/video/av116539105739515",
    "source": "AliAbdaal",
    "platform": "bilibili",
    "points": 30383,
    "published_at": "2026-05-09T13:00:00+00:00",
    "summary": "朋友们，有个叫Claude Code的工具，过去两个月我用它做了很多事情，它真的改变了我的整个工作方式，而且我感觉到Claude Code让人与人之间的差距加速变大。。。这个视频做完我就要发给还没尝试过的亲友！\n看完这条视频，你会了解如何让AI采访你来生成AI工具点子，如何筛选高杠杆项目，如何一边制作工具一边学习AI知识和开发技术概念。你会意识到，在AI时代，你最大的资产也许就是好奇心和突破技术摩"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29823,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1uBXVBJE7T",
    "domain": "AI",
    "title": "2026最新版保姆级Cursor安装教程来啦！史上最强AI编程工具Cursor！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116304660992022",
    "source": "爱学布鞋尼",
    "platform": "bilibili",
    "points": 23890,
    "published_at": "2026-03-28T03:29:22+00:00",
    "summary": "对小伙伴有帮助的话一键三连（点赞、投币、收藏）+关注支持一下UP，\n我也提供Zi liao 来帮助你们哦~~谢谢大家~~"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22568,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV18j5DzyEmD",
    "domain": "AI",
    "title": "Cursor-AI编程完整版入门教程",
    "url": "http://www.bilibili.com/video/av114379827713362",
    "source": "SiKi老师",
    "platform": "bilibili",
    "points": 12761,
    "published_at": "2025-04-22T11:00:00+00:00",
    "summary": "更多编程教程请访问我们官网www.sikiedu.com\n\nHi，我是SiKi老师，这个课程里面老师会带着大家学习使用全球目前最火的AI编程工具-Cursor的使用。\n\n教学内容：\n1、Cursor的下载和安装\n2、Cursor的基本设置\n3、使用Cursor开发贪吃蛇游戏\n4、使用Cursor开发一个博客网站\n5、Trae（字节旗下AI编程工具）的使用初体验"
  },
  {
    "id": "bvid:BV1o87764Ebs",
    "domain": "AI",
    "title": "我做 AI Agent 一年,90% 在做表面功夫——直到我换了思路",
    "url": "http://www.bilibili.com/video/av116818060512695",
    "source": "数字黑魔法",
    "platform": "bilibili",
    "points": 11158,
    "published_at": "2026-06-26T23:55:00+00:00",
    "summary": "本视频不构成任何投资建议。DYOR。"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 10585,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1Zftnz6Ewx",
    "domain": "AI",
    "title": "动手实现一个做PPT的MCP服务器",
    "url": "http://www.bilibili.com/video/av114975435658126",
    "source": "ModelScope官方账号",
    "platform": "bilibili",
    "points": 10572,
    "published_at": "2025-08-05T09:33:29+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Q4NczHEwg",
    "domain": "AI",
    "title": "Anthropic《Claude Code 实战 | Claude Code in Action》中英字幕",
    "url": "http://www.bilibili.com/video/av116203729259669",
    "source": "GPT中英字幕课程资源",
    "platform": "bilibili",
    "points": 10571,
    "published_at": "2026-03-14T00:00:00+00:00",
    "summary": "https://anthropic.skilljar.com/claude-code-in-action"
  },
  {
    "id": "bvid:BV1jsEQ6XEw6",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116724292721480",
    "source": "倒计时19",
    "platform": "bilibili",
    "points": 10545,
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
    "points": 10181,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV13mV46AEwq",
    "domain": "AI",
    "title": "干货！Vibe Coding 经验小结—从需求分析到agent hook",
    "url": "http://www.bilibili.com/video/av116655204141991",
    "source": "白玩dev",
    "platform": "bilibili",
    "points": 9873,
    "published_at": "2026-05-29T11:00:00+00:00",
    "summary": "本期聊聊vibe coding，同时分享一个好用的AI绘图工具支持绘制流程图、架构图、技术路线图、海报等280多种图形。电脑端工具安装包：https://sourl.cn/KuvRNV"
  },
  {
    "id": "bvid:BV1oUVc6vEEY",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的 AI 编程工具Cursor保姆级教程！Cursor保姆级安装使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116639383159883",
    "source": "AI大模型教学",
    "platform": "bilibili",
    "points": 8414,
    "published_at": "2026-05-26T06:24:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV16uj266EET",
    "domain": "AI",
    "title": "WorkBuddy Agent保姆级教程：Skill、MCP、自动化，桌面AI Agent到底能替你干多少活、WorkBuddy实测教程",
    "url": "http://www.bilibili.com/video/av116799320366596",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 8003,
    "published_at": "2026-06-23T12:03:43+00:00",
    "summary": "这期用一条完整实测，带你从 0 搞懂 Work Buddy 到底能做什么。\n我会先讲清楚桌面端 AI Agent 和普通聊天 AI 的区别，然后用 3 个真实办公案例演示它怎么干活：\n自动调研国产游戏出海趋势，生成带数据分析的 Word 报告 \n批量读取产品评价文件，生成 Excel 汇总表和运营分析报告 \n通过飞书连接器，把行业动态整理成简报并自动推送\n视频里也会讲到 Work Buddy 的几"
  },
  {
    "id": "rss:https://www.eetimes.com/satvu-targets-industrial-intelligence-with-thermal-imaging/",
    "domain": "AI 算力 / 半导体",
    "title": "SatVu Targets Industrial Intelligence with Thermal Imaging",
    "url": "https://www.eetimes.com/satvu-targets-industrial-intelligence-with-thermal-imaging/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T07:20:00+00:00",
    "summary": "With HotSat-2 in orbit and fresh funding, U.K. startup SatVu is demonstrating how high-resolution thermal satellite data can reveal real-world industrial activity. The post SatVu Targets Industrial In"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pnys-performance-32gb-ddr5-5600-ram-becomes-the-cheapest-2x16gb-kit-ddr5-kit-gets-a-usd70-discount",
    "domain": "AI 算力 / 半导体",
    "title": "PNY's Performance 32GB DDR5-5600 RAM becomes the cheapest 2x16GB kit— DDR5 kit gets a $70 discount",
    "url": "https://www.tomshardware.com/pc-components/pnys-performance-32gb-ddr5-5600-ram-becomes-the-cheapest-2x16gb-kit-ddr5-kit-gets-a-usd70-discount",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T14:32:37+00:00",
    "summary": "This 32GB DDR5 memory kit won't impress enthusiasts with its timings or design, but its aggressive price makes it difficult to overlook."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/lenovo-says-the-ramageddon-is-the-new-normal-outlines-survival-guide-at-isc-2026-an-exec-said-it-will-never-be-like-it-was-last-year",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo says the 'RAMageddon' is the new normal, outlines survival guide — at ISC 2026 an exec said 'it will never be like it was last year'",
    "url": "https://www.tomshardware.com/pc-components/ram/lenovo-says-the-ramageddon-is-the-new-normal-outlines-survival-guide-at-isc-2026-an-exec-said-it-will-never-be-like-it-was-last-year",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T13:50:59+00:00",
    "summary": "At the International Supercomputing Conference this past week, Lenovo reportedly said the memory market 'it will never be like it was last year.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/diy-3d-printed-steam-machine-a-like-uses-diagonal-mobo-mounting-parts-include-a-mini-itx-motherboard-rtx-5060-and-a-flex-atx-psu",
    "domain": "AI 算力 / 半导体",
    "title": "AMD engineer 3D-prints Steam Machine-a-like with diagonal mobo mounting — parts include a Mini ITX motherboard, RTX 5060, and a flex ATX PSU",
    "url": "https://www.tomshardware.com/desktops/pc-building/diy-3d-printed-steam-machine-a-like-uses-diagonal-mobo-mounting-parts-include-a-mini-itx-motherboard-rtx-5060-and-a-flex-atx-psu",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T12:36:37+00:00",
    "summary": "The Terk Box v1.1 looks like the closest DIY alternative to Valve's Steam Machine yet. 3D print source files are available."
  },
  {
    "id": "rss:https://www.tomshardware.com/service-providers/streaming/us-seizes-nearly-400-domains-streaming-the-2026-world-cup",
    "domain": "AI 算力 / 半导体",
    "title": "400 domains used for illegal 2026 World Cup streams seized by US Justice Department — operation is five times the scale of the previous crackdown",
    "url": "https://www.tomshardware.com/service-providers/streaming/us-seizes-nearly-400-domains-streaming-the-2026-world-cup",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T12:18:15+00:00",
    "summary": "The US Department of Justice has announced that it has seized nearly 400 domains that were illegally streaming live matches from the 2026 FIFA World Cup."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/chinas-loongson-launches-homegrown-16-core-server-cpu-built-on-loongarch-architecture-40w-chip-with-ddr4-ecc-and-32-pcie-lanes-targets-cheap-smb-file-database-and-web-servers",
    "domain": "AI 算力 / 半导体",
    "title": "China’s Loongson launches homegrown 16-core server CPU built on LoongArch architecture — 40W chip with DDR4 ECC and 32 PCIe lanes targets cheap SMB file, database, and web servers",
    "url": "https://www.tomshardware.com/pc-components/cpus/chinas-loongson-launches-homegrown-16-core-server-cpu-built-on-loongarch-architecture-40w-chip-with-ddr4-ecc-and-32-pcie-lanes-targets-cheap-smb-file-database-and-web-servers",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T12:00:00+00:00",
    "summary": "Loongson has announced the 3C3000, a 16-core LoongArch server CPU with DDR4 ECC, 32 PCIe lanes, 40W typical power, and performance claimed to match the earlier 3C5000."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/ai-coding-agents-can-be-tricked-into-installing-malware-via-clean-github-repositories-mozillas-0din-team-shows-how-claude-code-can-be-exploited-by-its-own-helpfulness",
    "domain": "AI 算力 / 半导体",
    "title": "AI coding agents can be tricked into installing malware via 'clean' GitHub repositories — Mozilla's 0din team shows how Claude Code can be exploited by its own helpfulness",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/ai-coding-agents-can-be-tricked-into-installing-malware-via-clean-github-repositories-mozillas-0din-team-shows-how-claude-code-can-be-exploited-by-its-own-helpfulness",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T11:30:00+00:00",
    "summary": "Claude and other AI agents fooled into running malware with just a minimal GitHub repository — ask the bot to initialize the project and you get hacked"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/playstation-is-removing-over-500-movies-from-uk-customers-accounts-with-no-refunds-iconic-films-like-terminator-2-apocalypse-now-and-mulholland-drive-are-getting-deleted",
    "domain": "AI 算力 / 半导体",
    "title": "PlayStation is removing over 500 movies from UK customers' accounts with no refunds — Iconic films like Terminator 2, Apocalypse Now, and Mulholland Drive are getting deleted",
    "url": "https://www.tomshardware.com/video-games/playstation/playstation-is-removing-over-500-movies-from-uk-customers-accounts-with-no-refunds-iconic-films-like-terminator-2-apocalypse-now-and-mulholland-drive-are-getting-deleted",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T11:00:00+00:00",
    "summary": "Sony will delete 551 movies from PlayStation users' accounts in the UK on September 1, 2026. These are films distributed by StudioCanal that no longer come under licensing agreements between the two c"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/japanese-firm-launches-hyper-realistic-capsule-toy-pc-parts-you-can-assemble-and-play-with-tiny-motherboards-cases-and-cpus-are-coming-after-tarlin-inks-collab-with-the-big-four-pc-parts-makers",
    "domain": "AI 算力 / 半导体",
    "title": "Japanese firm launches hyper-realistic capsule toy PC parts ‘you can assemble and play with’ — tiny motherboards, cases, and CPUs are coming after Tarlin inks collab with the ‘big four’ PC parts maker",
    "url": "https://www.tomshardware.com/desktops/pc-building/japanese-firm-launches-hyper-realistic-capsule-toy-pc-parts-you-can-assemble-and-play-with-tiny-motherboards-cases-and-cpus-are-coming-after-tarlin-inks-collab-with-the-big-four-pc-parts-makers",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T10:30:00+00:00",
    "summary": "A Japanese capsule toy maker has announced an official collaboration with ASRock, Gigabyte, MSI, and Intel to make tiny PC components that buyers 'can assemble and play with.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/get-an-rtx-5060-gaming-laptop-loaded-with-ryzen-7-cpu-and-32gb-ram-for-usd1-099-mobile-gaming-upgrade-just-got-usd300-cheaper",
    "domain": "AI 算力 / 半导体",
    "title": "Get an RTX 5060 gaming laptop loaded with Ryzen 7 CPU and 32GB RAM for $1,099 — mobile gaming upgrade just got $300 cheaper",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/get-an-rtx-5060-gaming-laptop-loaded-with-ryzen-7-cpu-and-32gb-ram-for-usd1-099-mobile-gaming-upgrade-just-got-usd300-cheaper",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T17:10:07+00:00",
    "summary": "The Gigabyte Aero X16 positions itself as a compelling mid-range gaming laptop offering a smooth high-refresh display, capable RTX 5060 graphics performance, and future-ready upgrade options."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/apple-reportedly-lobbies-uncle-sam-for-access-to-chinese-memory-chips-tech-giant-allegedly-wants-to-buy-from-blacklisted-cxmt",
    "domain": "AI 算力 / 半导体",
    "title": "Apple reportedly lobbies Uncle Sam for access to Chinese memory chips — tech giant allegedly wants to buy from blacklisted CXMT",
    "url": "https://www.tomshardware.com/tech-industry/apple-reportedly-lobbies-uncle-sam-for-access-to-chinese-memory-chips-tech-giant-allegedly-wants-to-buy-from-blacklisted-cxmt",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T14:51:29+00:00",
    "summary": "Following a historic price hike, the Financial Times reports that Apple is lobbying in Washington to secure approval to buy cheaper RAM from CXMT. The manufacturer is currently designated as a Chinese"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/steam-machine-scalping-hits-usd3-000-on-ebay-as-sellers-list-preorder-reservations-scalpers-already-flipping-queues-for-2x-the-msrp-of-the-2tb-model",
    "domain": "AI 算力 / 半导体",
    "title": "Steam Machine scalping hits $3,000 on eBay as sellers list preorder reservations — scalpers already flipping queues for 2X the MSRP of the 2TB model",
    "url": "https://www.tomshardware.com/video-games/console-gaming/steam-machine-scalping-hits-usd3-000-on-ebay-as-sellers-list-preorder-reservations-scalpers-already-flipping-queues-for-2x-the-msrp-of-the-2tb-model",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T14:24:10+00:00",
    "summary": "Several listings for Steam Machine pre-orders are being sold at markups so high that buyers will have to pay 140% to 167% above Valve's selling price."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intels-next-gen-52-core-nova-lake-cpu-could-pull-up-to-474w-high-end-lga1954-motherboards-may-need-three-8-pin-power-connectors-to-feed-the-monster",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's next-gen 52-core Nova Lake CPU could pull up to 474W — high-end LGA1954 motherboards may need three 8-pin power connectors to feed the monster",
    "url": "https://www.tomshardware.com/pc-components/cpus/intels-next-gen-52-core-nova-lake-cpu-could-pull-up-to-474w-high-end-lga1954-motherboards-may-need-three-8-pin-power-connectors-to-feed-the-monster",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T14:05:30+00:00",
    "summary": "Intel's flagship 52-core Nova Lake processor could feature a 474W PL2 power limit. At the same time, the new LGA1954 platform may introduce motherboard tiers for up to 175W CPUs and optional triple EP"
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/best-amazon-prime-day-deals-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Best Amazon Prime Day tech deals you can still get LIVE, last chance for hot deals — PC hardware deals on GPUs, CPUs, SSDs, and more",
    "url": "https://www.tomshardware.com/live/news/best-amazon-prime-day-deals-2026",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T13:18:26+00:00",
    "summary": "Find the very best PC hardware deals during Amazon Prime Day."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/bambu-lab-a2l-3d-printer-review",
    "domain": "AI 算力 / 半导体",
    "title": "Bambu Lab A2L 3D printer review: The A1 grows up",
    "url": "https://www.tomshardware.com/3d-printing/bambu-lab-a2l-3d-printer-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T13:05:02+00:00",
    "summary": "Bambu Lab adds a bigger bed slinger to their lineup."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/modded-steam-controller-can-automatically-charge-itself-like-a-robot-vacuum-enthusiast-creates-github-program-that-uses-the-vibration-motor-to-walk-it-back-to-its-docking-station",
    "domain": "AI 算力 / 半导体",
    "title": "Modded Steam Controller can automatically charge itself like a robot vacuum — enthusiast creates GitHub program that uses the vibration motor to walk it back to its docking station",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/modded-steam-controller-can-automatically-charge-itself-like-a-robot-vacuum-enthusiast-creates-github-program-that-uses-the-vibration-motor-to-walk-it-back-to-its-docking-station",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T11:00:00+00:00",
    "summary": "Ray Foss built this program that uses computer vision to let your Steam Controller slide back towards its charging puck by just using its built-in haptic motors. You can also try it for yourself by vi"
  },
  {
    "id": "rss:https://www.tomshardware.com/phones/commodore-drops-callback-flip-ohine-to-399-by-defaulting-to-recycled-memory-chips",
    "domain": "AI 算力 / 半导体",
    "title": "Commodore drops Callback flip phone by $100 by defaulting to recycled memory chips and unbundling the earphones — Callback 8020 drops to $399 as skyrocketing memory prices punish smartphone buyers",
    "url": "https://www.tomshardware.com/phones/commodore-drops-callback-flip-ohine-to-399-by-defaulting-to-recycled-memory-chips",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T10:30:00+00:00",
    "summary": "Commodore has slashed the starting price of its Callback 8020 flip phone to $399, down from $499."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/ram-crisis-provokes-enthusiast-to-try-windows-11-on-ddr1-era-hardware-other-key-vintage-components-included-the-core-2-q6600-and-ati-radeon-hd-4650-agp",
    "domain": "AI 算力 / 半导体",
    "title": "RAM crisis provokes enthusiast to try Windows 11 on DDR1-era hardware — other key vintage components included the Core 2 Q6600 and ATI Radeon HD 4650 AGP",
    "url": "https://www.tomshardware.com/software/windows/ram-crisis-provokes-enthusiast-to-try-windows-11-on-ddr1-era-hardware-other-key-vintage-components-included-the-core-2-q6600-and-ati-radeon-hd-4650-agp",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T10:00:00+00:00",
    "summary": "Enthusiast demos Microsoft’s newest OS running 'completely stable' on a Core 2 Quad Q6600, using a DDR1 motherboard, supported by an ATi Radeon HD 4650 AGP graphics card."
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
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/958804/chinas-z-ai-glm-52-mythos-cybersecurity",
    "domain": "大厂 AI 动态",
    "title": "China’s Z.ai claims it can match Mythos on cybersecurity",
    "url": "https://www.theverge.com/ai-artificial-intelligence/958804/chinas-z-ai-glm-52-mythos-cybersecurity",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T21:42:51+00:00",
    "summary": "China's Zhipu AI (Z.ai) released its open-weight GLM-5.2, and some researchers have claimed that it matches Mythos in certain bug-finding and cybersecurity scenarios. While GLM lags behind models from"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/958801/suno-launches-spark-incubator-program-to-feed-independent-artists-to-its-ai-machine",
    "domain": "大厂 AI 动态",
    "title": "Suno launches Spark incubator program to feed independent artists to its AI machine",
    "url": "https://www.theverge.com/ai-artificial-intelligence/958801/suno-launches-spark-incubator-program-to-feed-independent-artists-to-its-ai-machine",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T20:27:36+00:00",
    "summary": "Suno has ambitions to be more than just a toy to churn out AI slop, it also wants to be a streaming destination and to break new artists. Spark is their new incubator program for independent artists t"
  },
  {
    "id": "rss:https://www.theverge.com/tech/958768/china-claims-the-worlds-fastest-supercomputer",
    "domain": "大厂 AI 动态",
    "title": "China claims the world&#8217;s fastest supercomputer",
    "url": "https://www.theverge.com/tech/958768/china-claims-the-worlds-fastest-supercomputer",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T17:20:59+00:00",
    "summary": "Despite trade restrictions, China has reclaimed the title of the world's fastest supercomputer for the first time since 2018. LineShine has pushed El Capitan out of number one on the TOP500 ranking. T"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/958757/jim-henson-the-cube-black-mirror-tv-movie-review",
    "domain": "大厂 AI 动态",
    "title": "The Cube is Jim Henson’s little-known proto-Black Mirror masterpiece",
    "url": "https://www.theverge.com/entertainment/958757/jim-henson-the-cube-black-mirror-tv-movie-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T16:30:00+00:00",
    "summary": "I'm sure we're all familiar with Dark Crystal, so we know that Jim Henson can be weird and tackle slightly more mature subject matter. But there is little in his oeuvre that is quite as mind-bending a"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/958751/prosecutors-chatgpt-palisades-wildfire-arson-mistrial",
    "domain": "大厂 AI 动态",
    "title": "Prosecutors used ChatGPT logs as evidence in the Palisades fire trial",
    "url": "https://www.theverge.com/ai-artificial-intelligence/958751/prosecutors-chatgpt-palisades-wildfire-arson-mistrial",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T14:12:06+00:00",
    "summary": "Jonathan Rinderknecht was facing arson charges for setting a fire on New Year's Day in 2025, which became one of the deadliest wildfires in LA history. To make their case, prosecutors turned to locati"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/958735/nest-thermostat-version-history",
    "domain": "大厂 AI 动态",
    "title": "Nest&#8217;s quest to fix your thermostat",
    "url": "https://www.theverge.com/podcast/958735/nest-thermostat-version-history",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T12:02:44+00:00",
    "summary": "The founding story of Nest is pretty much a perfect tech myth. A legendary product maker (in this case, Tony Fadell) helps create one of the most successful products ever (the iPhone) and then rides o"
  },
  {
    "id": "rss:https://www.theverge.com/column/958379/streaming-industry-ads",
    "domain": "大厂 AI 动态",
    "title": "Ad-free streaming is a luxury now",
    "url": "https://www.theverge.com/column/958379/streaming-industry-ads",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T12:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more news about the streaming industry, follow Emma Roth. The Stepback arrives in our subscribers' "
  },
  {
    "id": "rss:https://www.theverge.com/tech/957603/tmd-smart-keyless-bike-lock-review",
    "domain": "大厂 AI 动态",
    "title": "TMD’s keyless bike lock is a $280 solution to a $60 problem",
    "url": "https://www.theverge.com/tech/957603/tmd-smart-keyless-bike-lock-review",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T07:00:00+00:00",
    "summary": "I've seen lots of so-called \"smart\" bike locks over the years, but none so far could justify the added cost. A newcomer that got its start securing ATMs for banks is trying to change that. There's not"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/958723/teenage-engineering-os-25-ep-133-ko-ii-sampler",
    "domain": "大厂 AI 动态",
    "title": "Teenage Engineering adds lo-fi mode, USB audio, and more to its KO II sampler",
    "url": "https://www.theverge.com/entertainment/958723/teenage-engineering-os-25-ep-133-ko-ii-sampler",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T21:20:32+00:00",
    "summary": "Teenage Engineering has already issued multiple substantial updates for its surprisingly capable $329 EP-133 KO II sampler. Its latest is one of the biggest yet. OS 2.5 adds audio over USB, selectable"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/958715/margaret-atwood-ai-problem-garbage-in-garbage-out",
    "domain": "大厂 AI 动态",
    "title": "Margaret Atwood says the problem with AI is &#8216;garbage in, garbage out&#8217;",
    "url": "https://www.theverge.com/ai-artificial-intelligence/958715/margaret-atwood-ai-problem-garbage-in-garbage-out",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T18:39:32+00:00",
    "summary": "Maraget Atwood, the storied author of The Handmaid's Tale and The Blind Assassin, was interviewed as part of the Babell Literary and Cultural Festival in Porto, Portugal. As it usually does at these t"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/28/california-law-targeting-loud-streaming-ads-takes-effect-on-july-1/",
    "domain": "大厂 AI 动态",
    "title": "California law targeting loud streaming ads takes effect on July 1",
    "url": "https://techcrunch.com/2026/06/28/california-law-targeting-loud-streaming-ads-takes-effect-on-july-1/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T21:34:14+00:00",
    "summary": "Streaming ads might be getting a lot quieter."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/28/ford-rehires-gray-beard-engineers-after-ai-falls-short/",
    "domain": "大厂 AI 动态",
    "title": "Ford rehires ‘gray beard’ engineers after AI falls short",
    "url": "https://techcrunch.com/2026/06/28/ford-rehires-gray-beard-engineers-after-ai-falls-short/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T19:05:39+00:00",
    "summary": "\"Mistakenly we thought that by just introducing artificial intelligence ... that would produce a high-quality product.”"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/28/writer-ian-bogost-says-the-small-stuff-can-help-us-reclaim-our-lives-from-dematerialization/",
    "domain": "大厂 AI 动态",
    "title": "Writer Ian Bogost says ‘The Small Stuff’ can help us reclaim our lives from too much convenience",
    "url": "https://techcrunch.com/2026/06/28/writer-ian-bogost-says-the-small-stuff-can-help-us-reclaim-our-lives-from-dematerialization/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T17:03:16+00:00",
    "summary": "Has Silicon Valley been building the wrong things?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/28/techcrunch-mobility-all-eyes-on-tesla-fsd/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: All eyes on Tesla FSD",
    "url": "https://techcrunch.com/2026/06/28/techcrunch-mobility-all-eyes-on-tesla-fsd/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T16:05:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, how AI is playing a part."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/28/why-wall-street-thinks-us-memory-maker-micron-is-the-next-nvidia/",
    "domain": "大厂 AI 动态",
    "title": "Why Wall Street thinks US memory maker Micron is the next Nvidia",
    "url": "https://techcrunch.com/2026/06/28/why-wall-street-thinks-us-memory-maker-micron-is-the-next-nvidia/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T15:00:00+00:00",
    "summary": "Eager to find more public AI-related companies that may do as well as Nvidia, Wall Street investors think they've found a winner with Micron."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/28/govees-smart-nugget-ice-maker-makes-every-iced-drink-feel-like-a-luxury/",
    "domain": "大厂 AI 动态",
    "title": "Govee’s smart nugget ice maker makes every iced drink feel like a luxury",
    "url": "https://techcrunch.com/2026/06/28/govees-smart-nugget-ice-maker-makes-every-iced-drink-feel-like-a-luxury/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T14:00:00+00:00",
    "summary": "For some people, the ice in a beverage is almost as important as the drink itself. That&#8217;s the audience Govee had in mind when designing its latest ice maker, the GoveeLife Smart Nugget Ice Maker"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/27/indian-payments-chief-thinks-ai-will-be-heavily-involved-in-next-era-of-digital-payment-growth/",
    "domain": "大厂 AI 动态",
    "title": "Indian payments chief thinks AI will be heavily involved in next era of digital payment growth",
    "url": "https://techcrunch.com/2026/06/27/indian-payments-chief-thinks-ai-will-be-heavily-involved-in-next-era-of-digital-payment-growth/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T05:00:00+00:00",
    "summary": "Dilip Asbe said that newer UPI apps could be more competitive with a viable commercial model"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/27/instagram-is-testing-more-ways-for-users-to-customize-your-algorithm/",
    "domain": "大厂 AI 动态",
    "title": "Instagram is testing more ways to customize ‘Your Algorithm’",
    "url": "https://techcrunch.com/2026/06/27/instagram-is-testing-more-ways-for-users-to-customize-your-algorithm/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T21:27:37+00:00",
    "summary": "Instagram users could soon see more ways to tune their content."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/27/softbanks-ceo-isnt-the-only-one-with-questions-about-elon-musks-orbital-data-center-hype/",
    "domain": "大厂 AI 动态",
    "title": "SoftBank’s CEO isn’t the only one with questions about Elon Musk’s orbital data center hype",
    "url": "https://techcrunch.com/2026/06/27/softbanks-ceo-isnt-the-only-one-with-questions-about-elon-musks-orbital-data-center-hype/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T20:42:36+00:00",
    "summary": "Not everyone is buying Elon Musk’s vision for orbital data centers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/27/apple-vision-pro-exec-is-reportedly-leaving-for-openai/",
    "domain": "大厂 AI 动态",
    "title": "Apple Vision Pro exec is reportedly leaving for OpenAI",
    "url": "https://techcrunch.com/2026/06/27/apple-vision-pro-exec-is-reportedly-leaving-for-openai/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T16:45:09+00:00",
    "summary": "Paul Meade, the Apple vice president in charge of the Vision Pro headset, is reportedly leaving the company to join OpenAI’s hardware team."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/27/the-fittest-founder-in-the-room-got-cancer-heres-how-he-used-ai-to-fight-back/",
    "domain": "大厂 AI 动态",
    "title": "The fittest founder in the room got cancer. Here’s how he used AI to fight back.",
    "url": "https://techcrunch.com/2026/06/27/the-fittest-founder-in-the-room-got-cancer-heres-how-he-used-ai-to-fight-back/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T14:00:00+00:00",
    "summary": "When confronted with cancer, Connor Christou fed everything tied tied to his regime — blood results, scan data, wearable output, journal entries — into Claude."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/",
    "domain": "大厂 AI 动态",
    "title": "Asian AI startups launch Mythos-like models as Anthropic’s export ban drags on",
    "url": "https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T12:00:00+00:00",
    "summary": "New models are launching in Asia that promise Mythos-like capabilities without fear of an export ban. U.S. AI labs may never recover this enormous market."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/why-did-this-journal-retract-two-1940s-papers-by-max-planck/",
    "domain": "大厂 AI 动态",
    "title": "Why did this journal retract two 1940s papers by Max Planck?",
    "url": "https://arstechnica.com/science/2026/06/why-did-this-journal-retract-two-1940s-papers-by-max-planck/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T18:49:21+00:00",
    "summary": "Clicking on the links now reveals blank pages and empty PDFs. \"Intellectually, it’s not acceptable.”"
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/06/apple-and-audi-alumni-have-made-a-luxe-ev-based-on-the-moon-buggy/",
    "domain": "大厂 AI 动态",
    "title": "Apple and Audi alumni have made a luxe EV based on the moon buggy",
    "url": "https://arstechnica.com/cars/2026/06/apple-and-audi-alumni-have-made-a-luxe-ev-based-on-the-moon-buggy/",
    "source": "Jeremy White, WIRED.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T11:07:05+00:00",
    "summary": "The Amble One is a street-legal $25,000 electric buggy designed for luxury resorts."
  },
  {
    "id": "rss:https://www.producthunt.com/products/receiptor-ai",
    "domain": "大厂 AI 动态",
    "title": "Receiptor AI — Agent Mode",
    "url": "https://www.producthunt.com/products/receiptor-ai",
    "source": "Rohan Chaubey",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T12:16:36+00:00",
    "summary": "Bookkeeping that keeps itself Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/pmb-local-first-memory-for-ai",
    "domain": "大厂 AI 动态",
    "title": "PMB",
    "url": "https://www.producthunt.com/products/pmb-local-first-memory-for-ai",
    "source": "Oleksii Bondar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T04:10:11+00:00",
    "summary": "Stop re-explaining your project to AI coding agents Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/crest-3",
    "domain": "大厂 AI 动态",
    "title": "Crest",
    "url": "https://www.producthunt.com/products/crest-3",
    "source": "zack",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T19:50:38+00:00",
    "summary": "System stats and translation on your Mac's notch Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/readhere-2",
    "domain": "大厂 AI 动态",
    "title": "ReadHere",
    "url": "https://www.producthunt.com/products/readhere-2",
    "source": "Quazi Marufur Rahman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T17:22:17+00:00",
    "summary": "Lightweight PDF & EPUB reader in your browser Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/dotient",
    "domain": "大厂 AI 动态",
    "title": "Dotient",
    "url": "https://www.producthunt.com/products/dotient",
    "source": "Declan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T02:55:46+00:00",
    "summary": "Your local semantic search app Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/lyto",
    "domain": "大厂 AI 动态",
    "title": "Lyto",
    "url": "https://www.producthunt.com/products/lyto",
    "source": "Arystan Tanekov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T15:17:01+00:00",
    "summary": "\"One AI agent across your browser, tools, and messages \" Discussion | Link"
  },
  {
    "id": "rss:https://36kr.com/p/3873965241931014?f=rss",
    "domain": "大厂 AI 动态",
    "title": "独家｜获超亿美元融资，Sand.ai 曹越：为什么视频是通往世界模型最重要的路径",
    "url": "https://36kr.com/p/3873965241931014?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T08:04:11+00:00",
    "summary": "“每一代模型，我们都在押注一个非共识。” 文｜邓咏仪 编辑｜张雨忻 Sand.ai 创始人曹越，不太关心自己站在共识的哪一边。 Sand.ai 是一家视频生成模型和产品公司，成立于2024年1月。曹越创立Sand.ai 的故事也已经被讲过很多遍：在上一段创业“光年之外”戛然而止后，曹越很快就投入到 Sand.ai 的创业中，做视频生成模型。 彼时，市场的主流叙事是 Diffusion 路线，几乎没"
  },
  {
    "id": "rss:https://36kr.com/p/3873902389794053?f=rss",
    "domain": "大厂 AI 动态",
    "title": "智能血糖管理需求旺盛，微泰医疗海外营收大增227.2%",
    "url": "https://36kr.com/p/3873902389794053?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T07:02:23+00:00",
    "summary": "继创新药之后，医疗器械出海正在迎来爆发期。据智研咨询数据，2026年1-4月，中国医疗仪器及器械出口金额达到70.90亿美元，同比上涨12.40%。 其中，动态血糖仪（CGM）品类的出海趋势可以看作一个从“进口替代”到全球突围的典型行业样本。CGM学名称作“持续葡萄糖监测系统”，能够连续监测人体血糖变化，在“控糖”成为流行生活方式的当下，迅速走进普罗大众的生活。 2020年前，中国CGM市场几乎被"
  },
  {
    "id": "rss:https://36kr.com/p/3873806295274756?f=rss",
    "domain": "大厂 AI 动态",
    "title": "36氪首发 | 海思、中兴团队创业，领域顶尖科学家加持，数字相控阵芯片厂商获厦门投资",
    "url": "https://36kr.com/p/3873806295274756?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T05:20:38+00:00",
    "summary": "作者&nbsp;|&nbsp;乔钰杰 编辑&nbsp;|&nbsp;袁斯来 硬氪获悉，广州宸思通讯科技有限公司（以下简称“宸思科技”）近日完成新一轮融资，由厦门高新投独家投资。本轮资金将主要用于核心技术研发和产品储备，加速数字相控阵芯片及模组产品的迭代升级。 宸思科技成立于2020年，总部位于广州黄埔区，聚焦数字相控阵芯片及模组研发，具备“芯片+模组+产品”的垂直整合能力，可为低空经济、卫星互联网"
  },
  {
    "id": "rss:https://36kr.com/p/3873786445813001?f=rss",
    "domain": "大厂 AI 动态",
    "title": "被健康家电「背刺」后，这届年轻人更会买了",
    "url": "https://36kr.com/p/3873786445813001?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T04:59:48+00:00",
    "summary": "那些年，��们交过的“健康”智商税 马上就要撞到墙了。 王焱的大脑还没反应过来，身体已经感觉到了一股推背感。在试驾这辆主打“智能”与“安全”的新能源汽车时，他不小心把油门当成了刹车，一脚踩了下去，等他意识到的时候，车子正在像头野兽一般往前猛窜。 在极其危险的几秒里，王焱以为这款车在发布会上被吹上天的风险预警与瞬间干预能立刻奏效。然而，智驾系统一片死寂，没有任何警报声，更没有主动刹停的迹象。最终，还"
  },
  {
    "id": "rss:https://36kr.com/p/3873710996902912?f=rss",
    "domain": "大厂 AI 动态",
    "title": "36氪首发 | URTOPIA联创做了款智能指环，众筹已破千万元",
    "url": "https://36kr.com/p/3873710996902912?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T03:43:03+00:00",
    "summary": "作者&nbsp;|&nbsp;张子怡 编辑&nbsp;|&nbsp;袁斯来 近日，AI可穿戴品牌AIVELA宣布完成数百万美元首轮融资。本轮融资由线性资本领投，锋领资本跟投，智能电助力自行车品牌URTOPIA等产业方共同加注。 本轮融资将主要用于下一代AI可穿戴产品研发、健康数据与AI Agent能力建设、全球市场拓展以及核心团队扩张。AIVELA将以智能指环、智能手链等贴身可穿戴产品为起点，面向"
  },
  {
    "id": "rss:https://36kr.com/p/3873706225751296?f=rss",
    "domain": "大厂 AI 动态",
    "title": "36氪首发 | Ebike公司获Brizan Ventures、高秉强参与超数亿融资，要进军外骨骼市场",
    "url": "https://36kr.com/p/3873706225751296?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T03:38:16+00:00",
    "summary": "作者&nbsp;|&nbsp;张子怡 编辑&nbsp;|&nbsp;袁斯来 硬氪获悉，全球智能电助力自行车品牌「URTOPIA」近日已完成B轮融资，融资总额超2亿元人民币。本轮融资由Brizan Ventures与桐乡市政府产业基金领投，高秉强、Kungho Fund、光远和声等机构持续加注。 本轮融资完成后，URTOPIA将继续加大在核心技术研发、全球市场拓展、供应链建设和组织能力升级方面的投入"
  },
  {
    "id": "rss:https://36kr.com/p/3873681978840071?f=rss",
    "domain": "大厂 AI 动态",
    "title": "秋声 | 海光芯正IPO背后，卖铲生意为何越做越亏？",
    "url": "https://36kr.com/p/3873681978840071?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T03:13:49+00:00",
    "summary": "本文约2500字，建议阅读5分钟 作者&nbsp;|&nbsp;彭孝秋 编者按：AI大爆发之际，越来越多公司走向资本市场。每一份招股书翻动的声音里，都藏着一家公司想说与未曾明说的全部。 鉴于此，硬氪特推出「秋声」专栏。秋声取自欧阳修《秋声赋》，借“听秋声”之意，产业冷暖，辨公司成色，记录企业冲刺IPO途中那些被写下与被隐藏的真实。这是我们第四期，海光芯正。 6月29日，北京海光芯正（01191.H"
  },
  {
    "id": "rss:https://36kr.com/p/3872276297618436?f=rss",
    "domain": "大厂 AI 动态",
    "title": "36氪首发 | 「CAYE咖爷科技」完成近4亿元B轮融资，系商用全自动咖啡机赛道单笔最大规模融资",
    "url": "https://36kr.com/p/3872276297618436?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T02:18:44+00:00",
    "summary": "作者 | 钟艺璇 36氪获悉，商用全自动咖啡机品牌「CAYE咖爷科技」已完成近4亿元B轮融资，本轮融资由老股东美团龙珠领投，柏睿资本、高瓴创投、苏创投、嘉宾资本等机构联合跟投。这也是目前商用全自动咖啡机赛道规模最大的单笔融资。&nbsp; CAYE咖爷是36氪持续关注的公司，该公司成立于2022年12月，围绕自研&nbsp;Bionic Barista&nbsp;仿生咖啡师系统，CAYE咖爷对咖啡"
  },
  {
    "id": "rss:https://36kr.com/p/3868055841641476?f=rss",
    "domain": "大厂 AI 动态",
    "title": "港大教授李弘扬创业做通用全身具身大脑，获真格高榕IDG五源等数亿种子轮融资｜硬氪独家",
    "url": "https://36kr.com/p/3868055841641476?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T01:27:07+00:00",
    "summary": "作者｜黄楠 编辑｜袁斯来 硬氪独家获悉，通用全身具身大脑公司「源策未来Archon Robotics」近日完成数亿元种子轮融资，本轮投资方包括真格基金、高榕创投、IDG资本、五源资本等头部美元基金，以及戈壁创投与香港大学联名基金、奇绩创坛、上海创智学院等。光源资本担任独家财务顾问。 本轮资金将主要用于全身人形基础模型研发、多模态全身动作数据采集、人才团队扩充，以及多地研发中心与产业合作生态搭建，加"
  },
  {
    "id": "rss:https://36kr.com/p/3873539789034501?f=rss",
    "domain": "大厂 AI 动态",
    "title": "中国卖家涌向拉美：高增长与合规门槛齐升丨最前线",
    "url": "https://36kr.com/p/3873539789034501?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T00:49:00+00:00",
    "summary": "作者丨欧雪 编辑丨袁斯来 6月26日，亚马逊全球开店在杭州宣布推出“拉美速通计划”，计划在2026年内面向3000个具备长期投入意愿的中国品牌，提供巴西本土公司注册协助、墨西哥RFC税号解决方案、最高12000美元补贴及物流费用减免等支持，帮助卖家全面扎根拉美市场。 拉美正在成为跨境电商的新热土。据eMarketer数据，2025年拉美零售电商市场规模接近1900亿美元，增速是全球平均水平的1.5"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3873972964955145?f=rss",
    "domain": "大厂 AI 动态",
    "title": "长裕集团：公司锆类产品在6月中旬发布了涨价函",
    "url": "https://36kr.com/newsflashes/3873972964955145?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T08:17:00+00:00",
    "summary": "36氪获悉，长裕集团在互动平台表示，公司锆类产品在6月中旬发布了涨价函。有关氧化锆产品目前正在验证中。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3873979081626631?f=rss",
    "domain": "大厂 AI 动态",
    "title": "豆包回应“内测社交功能”传闻：没有该计划",
    "url": "https://36kr.com/newsflashes/3873979081626631?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T08:15:18+00:00",
    "summary": "近期，有传言称，字节跳动旗下豆包大模型正在内测社交功能。6月29日，豆包相关负责人回复，在企业办公场景，豆包是和飞书有一些协同的尝试，未来也会合作更紧密。但豆包没有传闻所说的社交功能计划。（澎湃）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3873971541365762?f=rss",
    "domain": "大厂 AI 动态",
    "title": "西部黄金：全资子公司临时停产整改",
    "url": "https://36kr.com/newsflashes/3873971541365762?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T08:13:34+00:00",
    "summary": "36氪获悉，西部黄金公告，公司全资子公司阿克陶百源丰矿业有限公司和蒙新天霸矿业投资有限公司因安全治理专项自查发现多项安全隐患，决定对百源丰停产整改不超过30天，对蒙新天霸井下采掘作业停产整改不超过30天(选厂作业正常进行)。百源丰2025年营收4.9亿元，净利润1.3亿元；蒙新天霸2025年营收6630.53万元，净利润2575万元。恢复生产时间不确定，影响尚无法准确估计。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3873977231774978?f=rss",
    "domain": "大厂 AI 动态",
    "title": "国家能源局：1-5月全国电力市场交易电量同比增长24.8%",
    "url": "https://36kr.com/newsflashes/3873977231774978?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T08:13:25+00:00",
    "summary": "36氪获悉，据国家能源局消息，2026年5月，全国完成电力市场交易电量6268亿千瓦时，同比增长23.6%。从交易范围看，省内交易电量4906亿千瓦时，同比增长26.9%；跨省跨区交易电量1362亿千瓦时，同比增长12.9%。2026年1-5月，全国累计完成电力市场交易电量30573亿千瓦时，同比增长24.8%。从交易范围看，省内交易电量24361亿千瓦时，同比增长28.5%；跨省跨区交易电量62"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3873974641185794?f=rss",
    "domain": "大厂 AI 动态",
    "title": "恒指收涨1.57%，恒生科技指数涨3.23%",
    "url": "https://36kr.com/newsflashes/3873974641185794?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T08:10:47+00:00",
    "summary": "36氪获悉，恒指收涨1.57%，恒生科技指数涨3.23%；半导体、科技股领涨，兆易创新涨超14%，知乎涨超7%，澜起科技、网易涨超6%，美团、百度、哔哩哔哩涨超5%；医药股走强，礼邦医药涨超103%，药捷安康涨近40%；硬件设备、机械板块跌幅居前，联想集团跌超9%，潍柴动力跌超6%；南向资金净流出103.39亿港元。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3873922201375750?f=rss",
    "domain": "大厂 AI 动态",
    "title": "娃哈哈旗下天水饮料公司更名宏胜",
    "url": "https://36kr.com/newsflashes/3873922201375750?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T08:03:13+00:00",
    "summary": "36氪获悉，天眼查App显示，近日，天水娃哈哈饮料有限公司发生工商变更，企业名称变更为天水宏胜饮料有限公司。该公司成立于2010年3月，法定代表人为曾哲泉，注册资本825万美元，经营范围包括食品生产、食品用塑料包装容器工具制品生产、食品销售等，由盛佳集团有限公司、丽水宏博饮料有限公司共同持股。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3873961627325440?f=rss",
    "domain": "大厂 AI 动态",
    "title": "高盛：美股或再迎强劲财报季，经济增长和AI热潮料推动每股收益增长",
    "url": "https://36kr.com/newsflashes/3873961627325440?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T07:57:33+00:00",
    "summary": "高盛策略师表示，在“稳健的宏观背景”和人工智能投资热潮推动下，美国股市可能迎来又一个强劲的财报季。Ben Snider领导的团队表示，标普500指数盈利趋势强劲，足以超过分析师此前的高预期。Snider在一份报告中写道，AI基础设施类股票预计将在第二季度贡献约60%的每股收益增长，其中美光科技和英伟达合计将占40%以上。（财联社）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3873959791613185?f=rss",
    "domain": "大厂 AI 动态",
    "title": "消息称快手社科线两位技术高管转岗可灵事业部，或为上市做准备",
    "url": "https://36kr.com/newsflashes/3873959791613185?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T07:55:41+00:00",
    "summary": "有市场消息称，快手社区科学线人事调整，两位核心技术高管李晗、洪立印已完成岗位划转，正式加入可灵AI事业部，该事业部负责人为快手高级副总裁盖坤。两位技术负责人同步转岗，直接增强可灵在底层大模型、视频生成、商业算法等板块的技术实力。业内分析认为，两位推荐与电商算法领域的核心大将同时调入，是为可灵冲刺资本市场进行的关键技术底盘补强。对此消息，快手官方暂无回应。（新浪科技）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3873920663508230?f=rss",
    "domain": "大厂 AI 动态",
    "title": "歌尔股份旗下精密制造公司增资至约10.7亿",
    "url": "https://36kr.com/newsflashes/3873920663508230?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T07:46:56+00:00",
    "summary": "36氪获悉，天眼查App显示，近日，怡力精密制造有限公司发生工商变更，注册资本由约10.1亿人民币增至约10.7亿人民币。该公司成立于2013年7月，法定代表人为何朝明，经营范围包括开发、制造、销售光电子器件及其他电子器件等，由歌尔股份、香港歌尔泰克有限公司共同持股。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3873950707733767?f=rss",
    "domain": "大厂 AI 动态",
    "title": "三星正式宣布2655万亿韩元的投资计划，涉及半导体、AI算力数据中心等",
    "url": "https://36kr.com/newsflashes/3873950707733767?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T07:46:26+00:00",
    "summary": "三星正式宣布投资计划，总额达2655万亿韩元（约合11.68万亿元人民币），将在韩国龙仁市和平泽市的半导体产业集群投资2030万亿韩元。此前韩国方面称，三星集团和SK海力士将宣布未来10年总额达2000万亿韩元（约合8.8万亿元人民币）的重大投资计划，重点布局半导体、AI算力数据中心与物理AI领域。（财联社）"
  },
  {
    "id": "wscn:3775751",
    "domain": "股票",
    "title": "苹果，向长鑫投下一张信任票？",
    "url": "https://wallstreetcn.com/articles/3775751",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T07:56:12+00:00",
    "summary": "花旗认为，无论美国政府审批结果如何，苹果此举已将长鑫存储从\"国产替代\"重新定义为\"全球第四大可信赖DRAM制造商\"。而且这张\"信任票\"正沿供应链传导，封测及设备领域有望迎来估值重估。"
  },
  {
    "id": "wscn:3775737",
    "domain": "股票",
    "title": "Switch交换芯片：AI组网革新的\"第三核心硬件\"，国产替代能否破局？",
    "url": "https://wallstreetcn.com/premium/articles/3775737?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T07:50:32+00:00",
    "summary": "全球以太网交换机市场收入达551亿美元，同比增长31.5%，其中数据中心交换机收入达325亿美元，同比增长53.5%。AI训练与推理对超低延迟、高带宽互联的需求急剧上升，正直接带动Switch产品量价齐升。"
  },
  {
    "id": "wscn:3775752",
    "domain": "股票",
    "title": "宇树验证一个新趋势：具身智能的核心战场，不只是模型",
    "url": "https://wallstreetcn.com/articles/3775752",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T07:43:04+00:00",
    "summary": "具身智能告别“唯模型论”！宇树无遥操落地与NXP架构释放明确信号：竞争壁垒正转向软硬协同、边缘控制与实体数据。掌控全栈能力的玩家，正构筑纯云端难以逾越的超级护城河。"
  },
  {
    "id": "wscn:3775754",
    "domain": "股票",
    "title": "央行公告：首次3000亿元落地！",
    "url": "https://wallstreetcn.com/articles/3775754",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T07:33:13+00:00",
    "summary": "6月29日，央行首次开展3000亿元隔夜逆回购操作，同步开展1575亿元7天期逆回购，以应对半年末跨季流动性压力。此举既是精准\"削峰填谷\"的短期应对，也是货币政策框架转型的重要举措——隔夜逆回购从临时工具升级为常规品种，与7天期形成期限搭配，有助于完善短端利率调控机制。"
  },
  {
    "id": "wscn:3775753",
    "domain": "股票",
    "title": "GPT5.6惨遭切脑！Fable 5回归要变弱鸡版？",
    "url": "https://wallstreetcn.com/articles/3775753",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T07:30:46+00:00",
    "summary": "受AI安全监管影响，两大顶尖模型双双受限：GPT-5.6被迫拆分，最强版被限制访问，惨遭“切脑”；Fable 5因暴露网络攻击风险遭下架，预计将以加固护栏的“阉割版”回归。开发者担忧，严苛审查将导致AI模型严重降智，并面临重重使用限制。"
  },
  {
    "id": "wscn:3775749",
    "domain": "股票",
    "title": "地震冲击委内瑞拉能源基础设施：最大炼油厂因停电停产",
    "url": "https://wallstreetcn.com/articles/3775749",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T07:26:57+00:00",
    "summary": "委内瑞拉强震造成重大伤亡，并严重冲击该国能源系统。最大炼油厂阿穆艾及另一重要炼油厂因断电、缺水被迫停产，国内燃油及石化产品供应面临严峻挑战。"
  },
  {
    "id": "wscn:3775744",
    "domain": "股票",
    "title": "美团王兴再谈AI投资 称不超财务能力盲目投入",
    "url": "https://wallstreetcn.com/articles/3775744",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T07:26:43+00:00",
    "summary": "“还没看到爆发性的结果”"
  },
  {
    "id": "wscn:3775690",
    "domain": "股票",
    "title": "超万亿美元顺差之后：中国资本输出格局逐渐成形",
    "url": "https://wallstreetcn.com/premium/articles/3775690?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T07:26:22+00:00",
    "summary": "中国正由贸易顺差驱动迈向资本输出时代，人民币国际化逻辑加速转向资本输出、全球投融资与离岸金融生态建设。"
  },
  {
    "id": "wscn:3775745",
    "domain": "股票",
    "title": "极端天气成AI数据中心新威胁：险企、运营商同时拉响警报",
    "url": "https://wallstreetcn.com/articles/3775745",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T06:51:42+00:00",
    "summary": "AI基建狂飙正遭极端天气“背刺”！全球近八成数据中心面临气候威胁，已跃升为相关保险首要损失来源。高温与高能耗危机正倒逼险企重新定价，并迫使微软、英伟达等巨头加速冷却技术重构，气候风险正全面重塑AI底层逻辑。"
  },
  {
    "id": "wscn:3775741",
    "domain": "股票",
    "title": "存储三巨头三星、海力士、美光遭美国集体诉讼，HBM转型被指操纵DRAM价格",
    "url": "https://wallstreetcn.com/articles/3775741",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T06:41:22+00:00",
    "summary": "原告指控三星、SK海力士与美光以转型HBM为名，协同削减DDR3、DDR4等传统DRAM产能，致价格四年内暴涨700%，直接引发苹果iPad和Mac提价。Jefferies预测内存高价将成新常态，三季度环比再涨40%至50%，高位或延续至2028年。"
  },
  {
    "id": "wscn:3775727",
    "domain": "股票",
    "title": "韩国重磅芯片计划支撑市场，韩股收复跌幅，SK海力士转涨，油价一度回到70上方",
    "url": "https://wallstreetcn.com/articles/3775727",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T06:11:12+00:00",
    "summary": "韩国政府宣布将在西南部建设四座芯片厂，总投资约800万亿韩元。Kospi应声由跌转涨，SK海力士此前一度下跌近6%后也随之收复失地。标普500指数期货和纳斯达克100指数期货均上涨至少0.7%，欧洲股指期货同步走高。布伦特原油则抹去早间涨幅，转为基本持平，报每桶约72美元。"
  },
  {
    "id": "wscn:3775739",
    "domain": "股票",
    "title": "韩国史上最大规模产业投资计划！五年内DRAM产能翻倍，三星、SK海力士各新建两座芯片厂",
    "url": "https://wallstreetcn.com/articles/3775739",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T06:07:05+00:00",
    "summary": "韩国总统李在明宣布\"三大超级项目\"：三星与SK海力士将在西南部合建四座芯片工厂，投资规模约800万亿韩元，目标五年内DRAM产能翻倍；AI数据中心领域投入更高达1000万亿韩元。消息一出，此前重挫的韩国股市迅速逆转，KOSDAQ大涨逾8%。"
  },
  {
    "id": "wscn:3775164",
    "domain": "股票",
    "title": "功率半导体行业：AI算力与新能源双轮驱动，供给紧俏开启景气上行周期",
    "url": "https://wallstreetcn.com/premium/articles/3775164?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T06:04:06+00:00",
    "summary": "AI算力+新能源+供给收缩，功率半导体迎来新一轮上行周期。"
  },
  {
    "id": "wscn:3775742",
    "domain": "股票",
    "title": "韩国股市绑架日本？高盛警告：“北亚半导体联合体”正在放大AI交易风险",
    "url": "https://wallstreetcn.com/articles/3775742",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T06:03:50+00:00",
    "summary": "年内5次熔断！韩国股市正沦为高杠杆“踩踏温床”。高盛警告，日韩股市已异化为深度绑定的“北亚半导体联合体”。如今买日股，实则是买首尔内存周期的高危门票。AI硬件底盘虽稳，但极端波动已成新常态。"
  },
  {
    "id": "wscn:3775723",
    "domain": "股票",
    "title": "创业板午后拉升翻红，创新药大爆发，科技股集体调整，恒科指暴涨近4%，科网股集体反攻",
    "url": "https://wallstreetcn.com/articles/3775723",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T06:01:38+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市超3500股飘绿，上午半天成交2.52万亿。沪深两市半日成交额2.5万亿，较上个交易日放量不足800亿。板块方面，医药生物板块爆发，创新药、CRO方向领涨。晶圆产业、白酒、大基建、煤炭、黄金、氟化工题材走强。算力硬件产业链下挫，PCB、CPO方向大跌。"
  },
  {
    "id": "wscn:3775740",
    "domain": "股票",
    "title": "Claude Mythos让梁文锋决定融资",
    "url": "https://wallstreetcn.com/articles/3775740",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T05:43:09+00:00",
    "summary": "受Claude刺激，DeepSeek完成74亿美元巨额融资，创始人梁文锋狂砸200亿重仓AGI！公司团队招人翻倍并全力死磕国产芯片。无惧15个月研发空窗期，其开源模型凭借极致性价比，在美单月市场份额狂飙至17%。一场打破AI垄断的硬核突围战已全面打响！"
  },
  {
    "id": "wscn:3775738",
    "domain": "股票",
    "title": "“豆包手机”获得半年豆包会员 尝试软件补贴硬件",
    "url": "https://wallstreetcn.com/articles/3775738",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T05:15:42+00:00",
    "summary": "软硬绑定。"
  },
  {
    "id": "wscn:3775579",
    "domain": "股票",
    "title": "半导体材料\"去日化\"：从依赖到重构，14种日本垄断材料国产替代进行时？",
    "url": "https://wallstreetcn.com/premium/articles/3775579?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T03:53:19+00:00",
    "summary": "日本在19种关键半导体材料中占据14种全球市占率第一，总市场份额达52%，构成中国半导体产业链安全的“命门”。"
  },
  {
    "id": "wscn:3775735",
    "domain": "股票",
    "title": "智平方完成50亿融资，估值升至200亿",
    "url": "https://wallstreetcn.com/articles/3775735",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T03:45:00+00:00",
    "summary": "加速推进“机器人大脑”的迭代升级与规模化量产进程"
  },
  {
    "id": "wscn:3775734",
    "domain": "股票",
    "title": "油价跌至战前水平，美元利率为何不跟？",
    "url": "https://wallstreetcn.com/articles/3775734",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T03:41:07+00:00",
    "summary": "美伊达成协议以来，国际两油价格已不知不觉逼近3月初水平，超出市场预期。然而1Y SOFR却自5月以来逆势走高，美国强劲基本面叠加鹰派新主席沃什的不确定性溢价，令美元利率对油价“跟涨不跟跌”，短端利率大跌或只能等CPI破3%或美股崩盘。"
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
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.27525",
    "domain": "金融",
    "title": "Measuring Racial Disparities in Rent Growth Under Algorithmic Landlord Concentration in U.S. Metros",
    "url": "https://arxiv.org/abs/2606.27525",
    "source": "Advay Ranade",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T04:00:00+00:00",
    "summary": "arXiv:2606.27525v1 Announce Type: new Abstract: The 2024 Department of Justice antitrust complaint against RealPage, Inc. named five major residential REITs for coordinating algorithmic rent pricing a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.27804",
    "domain": "金融",
    "title": "Methods for Uncertainty Representation in Risk Management: A Comparative Review and Decision-Oriented Framework",
    "url": "https://arxiv.org/abs/2606.27804",
    "source": "Albert Kutej, Stefan Rass",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T04:00:00+00:00",
    "summary": "arXiv:2606.27804v1 Announce Type: new Abstract: The consideration of uncertainty is a central but frequently inadequately addressed component of risk management. A systematic treatment of uncertainty "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.27845",
    "domain": "金融",
    "title": "LLM Agents as Static Level-k Players in Behavioural Games",
    "url": "https://arxiv.org/abs/2606.27845",
    "source": "Po Han Teo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T04:00:00+00:00",
    "summary": "arXiv:2606.27845v1 Announce Type: new Abstract: Large Language Models (LLMs) are increasingly used as stand-ins in behavioural games. These stand-ins rely on the assumption that the LLM's distribution"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.27924",
    "domain": "金融",
    "title": "Heterogeneous Diffusion of Electric Vehicles in China: Demand, Learning, Product Entry, and the Incidence of Industrial Policy",
    "url": "https://arxiv.org/abs/2606.27924",
    "source": "Yu (Jasmine), Hao, Jinge Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T04:00:00+00:00",
    "summary": "arXiv:2606.27924v1 Announce Type: new Abstract: China's electric-vehicle (EV) sales share rose from about 1% in 2015 to roughly 45% in 2024. We evaluate this technology transition with an equilibrium "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.27932",
    "domain": "金融",
    "title": "(In)Efficient Market States and Rough Volatility Detected via Grunwald-Letnikov Fractional Derivative",
    "url": "https://arxiv.org/abs/2606.27932",
    "source": "Daniele Angelini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T04:00:00+00:00",
    "summary": "arXiv:2606.27932v1 Announce Type: new Abstract: Testing self-similarity in fractional processes from a single observed trajectory is difficult under long-range dependence, because the associated Kolmo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.28063",
    "domain": "金融",
    "title": "How to deal with machine learning bias in economic history",
    "url": "https://arxiv.org/abs/2606.28063",
    "source": "Torben S. D. Johansen, Julius Koschnick, Christian Vedel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T04:00:00+00:00",
    "summary": "arXiv:2606.28063v1 Announce Type: new Abstract: Machine learning (ML) has rapidly transformed economic history, lowering costs of digitization, data linkage, and imputation, and making information in "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.28312",
    "domain": "金融",
    "title": "Optimal Deployment of Electric Aircraft for Canadian Domestic Flights",
    "url": "https://arxiv.org/abs/2606.28312",
    "source": "Elham Soufiani, Mehrdad Pirnia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T04:00:00+00:00",
    "summary": "arXiv:2606.28312v1 Announce Type: new Abstract: This paper presents a multi-period mixed-integer linear programming (MILP) framework for planning the transition from conventional to electric aircraft "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.27462",
    "domain": "金融",
    "title": "The Decision Geometry of Covariance Estimation for the Global Minimum-Variance Portfolio under Heavy Tails",
    "url": "https://arxiv.org/abs/2606.27462",
    "source": "Xavier Fonseca",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T04:00:00+00:00",
    "summary": "arXiv:2606.27462v1 Announce Type: cross Abstract: The global minimum-variance portfolio (GMVP) is the canonical decision built from an estimated covariance matrix, yet covariance estimators are univer"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.27670",
    "domain": "金融",
    "title": "CryptoGAT: Are Time Series Models Effective for Cryptocurrency Forecasting?",
    "url": "https://arxiv.org/abs/2606.27670",
    "source": "Yu Peng, Matloob Khushi, Josiah Poon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T04:00:00+00:00",
    "summary": "arXiv:2606.27670v1 Announce Type: cross Abstract: Cryptocurrency price prediction is a significant challenge in quantitative investment. In recent years, time series models have made significant progr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.18342",
    "domain": "金融",
    "title": "The Emergency-Care Consequences of Disrupted Prevention: Evidence from Mammography Screening Pathway",
    "url": "https://arxiv.org/abs/2512.18342",
    "source": "Moslem Rashidi, Luke B. Connelly, Gianluca Fiorentini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T04:00:00+00:00",
    "summary": "arXiv:2512.18342v5 Announce Type: replace Abstract: Do disruptions to organized preventive-care pathways increase the likelihood of downstream overnight emergency hospitalizations? We study this quest"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.10517",
    "domain": "金融",
    "title": "From rough to multifractal multidimensional volatility: A multidimensional Log S-fBM model",
    "url": "https://arxiv.org/abs/2601.10517",
    "source": "Othmane Zarhali, Emmanuel Bacry, Jean-Fran\\c{c}ois Muzy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T04:00:00+00:00",
    "summary": "arXiv:2601.10517v2 Announce Type: replace Abstract: We introduce the multivariate Log S-fBM model (mLog S-fBM), extending the univariate framework proposed by Wu \\textit{et al.} to the multidimensiona"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.23596",
    "domain": "金融",
    "title": "Anatomy of the Market: A Body-Tail Test of Factor Models",
    "url": "https://arxiv.org/abs/2606.23596",
    "source": "Useong Shin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T04:00:00+00:00",
    "summary": "arXiv:2606.23596v3 Announce Type: replace Abstract: In an ideal stochastic discount factor, zero pricing errors and the maximum Sharpe ratio coincide; in a low-dimensional approximation they need not."
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.26731",
    "domain": "金融",
    "title": "Robust Hedging Valuation Adjustment under Liquidity--Demand Stress",
    "url": "https://arxiv.org/abs/2606.26731",
    "source": "Takayuki Sakuma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T04:00:00+00:00",
    "summary": "arXiv:2606.26731v2 Announce Type: replace Abstract: This paper develops a robust hedging valuation adjustment (HVA) measure for dynamic hedging. Simulated rebalancing and maturity-unwind trades genera"
  },
  {
    "id": "rss:https://arxiv.org/abs/2308.05201",
    "domain": "金融",
    "title": "\"Generate\" the Future of Work through AI: Empirical Evidence from Online Labor Markets",
    "url": "https://arxiv.org/abs/2308.05201",
    "source": "Jin Liu, Xingchen Xu, Xi Nan, Yongjun Li, Yong Tan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T04:00:00+00:00",
    "summary": "arXiv:2308.05201v4 Announce Type: replace-cross Abstract: Large Language Model (LLM)-based generative AI systems are general-purpose tools capable of augmenting or even automating a wide range of job "
  },
  {
    "id": "rss:https://arxiv.org/abs/2412.18032",
    "domain": "金融",
    "title": "Major Space Weather Risks Identified via Coupled Physics-Engineering-Economic Modeling",
    "url": "https://arxiv.org/abs/2412.18032",
    "source": "Edward J. Oughton, Dennies K. Bor, Robert Weigel, C. Trevor Gaunt, Ridvan Dogan, Liling Huang, Jeffrey J. Love, Michael Wiltberger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T04:00:00+00:00",
    "summary": "arXiv:2412.18032v3 Announce Type: replace-cross Abstract: Space weather poses an important but under-quantified threat to society. While severe geomagnetic storms are recognized as potential global ca"
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.16862",
    "domain": "金融",
    "title": "Action-Space Entropy Regularization in Bayesian Markowitz",
    "url": "https://arxiv.org/abs/2602.16862",
    "source": "Andy Au",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T04:00:00+00:00",
    "summary": "arXiv:2602.16862v4 Announce Type: replace-cross Abstract: We solve the entropy-regularized mean--variance portfolio problem under Bayesian drift uncertainty. We combine continuous-time Bayesian filter"
  }
]
```
