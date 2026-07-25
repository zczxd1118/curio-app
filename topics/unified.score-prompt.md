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

- 今日日期：`2026-07-25`
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
  "date": "2026-07-25",
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
    "points": 3889156,
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
    "points": 1597822,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1273437,
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
    "points": 954974,
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
    "points": 948555,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 942350,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 562284,
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
    "points": 523175,
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
    "points": 427333,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 370755,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 350009,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 311195,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1RAEz6EE98",
    "domain": "AI",
    "title": "为什么Claude Code+DeepSeekV4是最有性价比的个人AI Agent?",
    "url": "http://www.bilibili.com/video/av116732144392386",
    "source": "呱声一片",
    "platform": "bilibili",
    "points": 283422,
    "published_at": "2026-06-11T15:27:06+00:00",
    "summary": "官方文档地址：https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/claude_code"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 247355,
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
    "points": 202612,
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
    "points": 177779,
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
    "points": 175437,
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
    "points": 162423,
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
    "points": 160224,
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
    "points": 158131,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1gtKx6rEHr",
    "domain": "AI",
    "title": "Claude Code超强平替来了！彻底告别封号！",
    "url": "http://www.bilibili.com/video/av116954828374073",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 117186,
    "published_at": "2026-07-21T10:09:52+00:00",
    "summary": "不可否认 Claude Code确实很强\n但国内小伙伴想要安稳用上它  \n真的太折腾了\n首先你得会用魔法  \n然后 你还得想尽各种办法折腾海外订阅\n最狠的是\n不知道哪天你的账号可能就被封了\nAI工具本来就是为我们服务的\n可现在却成了每天提心吊胆伺候的大爷\n其实咱们真没必要非得死磕\n国内也有一个非常强的 Claude Code 平替工具\n那就是 Qoder CLI  \n今天咱们就不吹不黑  \n直接上"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 115863,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 109039,
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
    "points": 104651,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 99640,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92738,
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
    "points": 83072,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73884,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 43956,
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
    "points": 39029,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 37521,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1HaN162EPT",
    "domain": "AI",
    "title": "【Codex】2026最新Codex保姆级教程，ChatGPT + Codex 开发实战全流程，环境配置、核心功能、使用技巧到项目实战一学就会，少走99%弯路！",
    "url": "http://www.bilibili.com/video/av116911660665280",
    "source": "今天AI了吗",
    "platform": "bilibili",
    "points": 36564,
    "published_at": "2026-07-13T09:01:50+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 36098,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1cCj2ztEf5",
    "domain": "AI",
    "title": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%",
    "url": "http://www.bilibili.com/video/av114574527307727",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 34997,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV1JU7E6PEar",
    "domain": "AI",
    "title": "Cursor 已死？我为什么要退订 Cursor ？",
    "url": "http://www.bilibili.com/video/av116819553683121",
    "source": "祥子在学AI",
    "platform": "bilibili",
    "points": 30488,
    "published_at": "2026-06-27T01:52:00+00:00",
    "summary": "当了一年多的 Cursor 重度用户，最近把它退订了。\n\n不是它变差了，是 Claude Code 和 Codex 真的太好用了。\n\n几个真实感受： ① 大模型越来越强，我已经不怎么手写代码了 ② Cursor 套的是 VS Code 壳子，只属于程序员 ③ 底层模型不在一个量级——Claude 有 Opus 和 Fable 5，Codex 有 GPT 5.5/5.6，Cursor 的 Compo"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 30442,
    "published_at": "2026-05-07T00:00:00+00:00",
    "summary": "全栈课一共分为6大块内容\n第一块：AI智能体开发基础(AI大模型、工具、记忆、MCP、中间件、Skills等核心内容)\n第二块：Claude Code,Trea+skills实现基于需求文档生成用例，基于OpenClaw实现接口自动化落地，基于hermes Agent实现web自动化落地\n第三块：功能测试的智能体开发(项目RAG知识库搭建+Agent搭建+skills开发，实现用例生成的Agent"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28820,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 28071,
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
    "points": 25640,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1pkK56aEVG",
    "domain": "AI",
    "title": "GPT-5.6在Claude Code中表现远超Codex | Theo - t3․gg",
    "url": "http://www.bilibili.com/video/av116929612221157",
    "source": "浮生千山路w",
    "platform": "bilibili",
    "points": 24135,
    "published_at": "2026-07-16T12:29:37+00:00",
    "summary": "来源：https://www.youtube.com/watch?v=Noo0NWD0gHU\n原标题：gpt 5.6 is way better in Claude Code\n频道：Theo - t3․gg\n发布时间：2026-07-16\n\n内容简介：\n作者使用GPT-5.6 Sol版本在Claude Code中进行编程，发现其表现相较于Codex有显著提升，体验令人震惊。视频由Coderabbi"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22649,
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
    "points": 17310,
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
    "points": 16279,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 15612,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV1ZFc2epE4s",
    "domain": "AI",
    "title": "Cursor+VS2022编译器 准备cursor的c++开发环境",
    "url": "http://www.bilibili.com/video/av113820676655607",
    "source": "新手村养牛人",
    "platform": "bilibili",
    "points": 14452,
    "published_at": "2025-01-13T11:00:14+00:00",
    "summary": "cmake_minimum_required(VERSION 3.23)\nproject(CursorVs2022)\nset(CMAKE_CXX_STANDARD 17)\n\nset(CMAKE_INCLUDE_CURRENT_DIR ON)\nSET(CMAKE_BUILD_TYPE Debug)\nset(CMAKE_AUTOMOC ON)\nset(CMAKE_AUTOUIC ON)\nset(CMA"
  },
  {
    "id": "bvid:BV16ggC6DEZK",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116963049212769",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 13104,
    "published_at": "2026-07-22T10:10:42+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1TNKu6pEUW",
    "domain": "AI",
    "title": "一个人用 Fable5 vibe coding 的游戏已上线",
    "url": "http://www.bilibili.com/video/av116926860761026",
    "source": "鲨鱼恶魔哒",
    "platform": "bilibili",
    "points": 11884,
    "published_at": "2026-07-16T00:43:23+00:00",
    "summary": "《探索！猪猪岛》游戏已经上线啦，电脑网页端以及手机端都可以玩，不需要下载。整体就是一个休闲游戏，你在小岛四处探索收集、养猪、种田、钓鱼，以及和各种角色对话，解锁新的故事线（后续会加入）。\n\n我大概花了3整天的时间用 Fable5 完成了大部分游戏内容，之后又断断续续花了一点时间debug 和优化。感兴趣的小伙伴可以戳我要游戏链接，欢迎大家给我反馈游戏体验以及遇到的bugs呀～"
  },
  {
    "id": "bvid:BV1vLN769EJa",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！大模型入门到进阶，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116894866677118",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 11250,
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
    "points": 9945,
    "published_at": "2026-07-20T03:42:16+00:00",
    "summary": "如果视频对你有用的话，一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套资料+问题解答+请看评论区置顶领取哦】"
  },
  {
    "id": "bvid:BV1SfKQ6LEnp",
    "domain": "AI",
    "title": "Cursor+Qoder+Trae三合一 一键续杯！",
    "url": "http://www.bilibili.com/video/av116834669959773",
    "source": "无忧小助手",
    "platform": "bilibili",
    "points": 8924,
    "published_at": "2026-06-29T17:54:50+00:00",
    "summary": "全网独家Cursor、Qoder、trae三合一一键续杯工具，Qoder、Trae切换账号不丢失上下文！"
  },
  {
    "id": "hn:49035303",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, Microsoft, Meta warn against overregulating open-weight models",
    "url": "https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 570,
    "published_at": "2026-07-24T13:32:30+00:00",
    "summary": ""
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
    "id": "hn:49034868",
    "domain": "AI 算力 / 半导体",
    "title": "Half-Life 2 running natively on HaikuOS",
    "url": "https://discuss.haiku-os.org/t/haiku-nvidia-porting-nvidia-driver-for-turing-gpus/16520?page=18",
    "source": "m0do1",
    "platform": "hackernews",
    "points": 288,
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
    "points": 111,
    "published_at": "2026-07-24T13:58:12+00:00",
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
    "points": 101,
    "published_at": "2026-07-19T19:44:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48992221",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC eyes price hikes of up to 25% on chip production services in 2027",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes",
    "source": "speckx",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-21T13:40:51+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/intel-foundry-improves-execution-but-external-customers-remain-the-test/",
    "domain": "AI 算力 / 半导体",
    "title": "Intel Foundry Improves Execution, but External Customers Remain the Test",
    "url": "https://www.eetimes.com/intel-foundry-improves-execution-but-external-customers-remain-the-test/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T22:00:00+00:00",
    "summary": "Intel’s fabs are healing, but $293M in outside revenue won’t scare TSMC yet. The post Intel Foundry Improves Execution, but External Customers Remain the Test appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/dac-2026-what-does-it-actually-take-to-create-ai-chips/",
    "domain": "AI 算力 / 半导体",
    "title": "DAC 2026: What Does It Actually Take to Create AI Chips?",
    "url": "https://www.eetimes.com/dac-2026-what-does-it-actually-take-to-create-ai-chips/",
    "source": "Frank Schirrmeister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:00:00+00:00",
    "summary": "AI chips don’t need hype—they need power, memory, IP, thermal, and verification fights. See what DAC 2026 engineers will expose. The post DAC 2026: What Does It Actually Take to Create AI Chips? appea"
  },
  {
    "id": "rss:https://www.eetimes.com/supply-chain-leaders-new-math-for-network-decisions/",
    "domain": "AI 算力 / 半导体",
    "title": "Supply Chain Leaders’ New Math for Network Decisions",
    "url": "https://www.eetimes.com/supply-chain-leaders-new-math-for-network-decisions/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T08:00:00+00:00",
    "summary": "Gartner urges supply chain leaders to quantify daily operational friction, making network investments more resilient and easier to justify. The post Supply Chain Leaders&#8217; New Math for Network De"
  },
  {
    "id": "rss:https://www.eetimes.com/u-s-starts-genesis-mission-with-5b-for-first-projects/",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Starts Genesis Mission with $5B for First Projects",
    "url": "https://www.eetimes.com/u-s-starts-genesis-mission-with-5b-for-first-projects/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T23:00:00+00:00",
    "summary": "America drops $5B on AI’s Genesis Mission while China lines up $295B; see why the opening bet may already be too small. The post U.S. Starts Genesis Mission with $5B for First Projects appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/the-story-behind-fuse-eda-ai-system/",
    "domain": "AI 算力 / 半导体",
    "title": "The Story Behind Fuse EDA AI system",
    "url": "https://www.eetimes.com/the-story-behind-fuse-eda-ai-system/",
    "source": "Siemens EDA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T19:35:36+00:00",
    "summary": "What does it take to build agentic AI for EDA that users can trust and verify? Listen in on this behind-the-scenes conversation around the development of a groundbreaking new platform. The post The St"
  },
  {
    "id": "rss:https://www.eetimes.com/etched-raises-300m-with-1b-in-pre-orders/",
    "domain": "AI 算力 / 半导体",
    "title": "Etched Raises $300M with $1B in Pre-Orders",
    "url": "https://www.eetimes.com/etched-raises-300m-with-1b-in-pre-orders/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T15:00:00+00:00",
    "summary": "AI chip startup Etched will start shipping its racks this summer. The post Etched Raises $300M with $1B in Pre-Orders appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/dac-2026-users-are-not-waiting-diy-ai-is-now-in-vogue/",
    "domain": "AI 算力 / 半导体",
    "title": "DAC 2026: Users Are Not Waiting; DIY AI Is Now in Vogue",
    "url": "https://www.eetimes.com/dac-2026-users-are-not-waiting-diy-ai-is-now-in-vogue/",
    "source": "Frank Schirrmeister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T07:45:00+00:00",
    "summary": "At DAC 2026, chip giants stop waiting for EDA vendors and build their own AI brains—see who’s seizing control. The post DAC 2026: Users Are Not Waiting; DIY AI Is Now in Vogue appeared first on EE Tim"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-and-24-other-companies-sign-open-weights-letter-as-washington-weighs-chinese-ai-model-ban",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia and 24 other companies sign open-weights letter as Washington weighs Chinese AI model ban — OpenAI, Anthropic, and Google absent from the list",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-and-24-other-companies-sign-open-weights-letter-as-washington-weighs-chinese-ai-model-ban",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T18:31:48+00:00",
    "summary": "Signatories include chipmakers, server vendors, cloud operators, enterprise software firms, security companies, and venture funds"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-commits-to-14a-mass-production-in-2028-as-its-sales-rise-25-percent-year-over-year",
    "domain": "AI 算力 / 半导体",
    "title": "Intel commits to 14A mass production in 2028 as its sales rise 25% year-over-year",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-commits-to-14a-mass-production-in-2028-as-its-sales-rise-25-percent-year-over-year",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:49:43+00:00",
    "summary": "Intel posts 25% higher year-over-year sales and above-the-guidance earnings, and confirms that its 14A technology is on-track to start high volume ramp in 2028."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/geekom-a9-max-2026-mini-pc-review",
    "domain": "AI 算力 / 半导体",
    "title": "Geekom A9 Max 2026 review: Gorgon Point in a compact Mini PC",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/geekom-a9-max-2026-mini-pc-review",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T16:30:00+00:00",
    "summary": "Mini PC specialist Geekom has updated its A9 Max design with AMD’s latest mobile silicon. The incremental improvements of the AMD Ryzen AI 9 HX470 are supported by a revamped Ice Blast 3.0 cooling sol"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-huggingface-breach-heralds-an-unprecedented-age-of-ai-cyber-warfare-contemporary-llms-have-caused-massive-upheaval-in-cybersecurity-and-its-only-going-to-get-worse",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI's HuggingFace breach heralds an unprecedented age of AI cyber warfare — contemporary LLMs have caused massive upheaval in cybersecurity, and it's only going to get worse",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-huggingface-breach-heralds-an-unprecedented-age-of-ai-cyber-warfare-contemporary-llms-have-caused-massive-upheaval-in-cybersecurity-and-its-only-going-to-get-worse",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T16:12:08+00:00",
    "summary": "Contemporary AI bots are far too competent at cybersecurity, and humanity may have reached a tipping point where it's hard to keep up."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/dell-14s-review",
    "domain": "AI 算力 / 半导体",
    "title": "Dell 14S review: High-class design and 20+ hour battery life",
    "url": "https://www.tomshardware.com/laptops/dell-14s-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T16:10:39+00:00",
    "summary": "The Dell 14S makes good on its promise of serving as a cheaper alternative to the pricier XPS 14."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-working-on-new-x3d-v-cache-mobile-chip-for-gaming-laptops-leaker-claims-ryzen-7-9800hx3d-could-launch-with-8-cores-16-threads-and-96mb-cache",
    "domain": "AI 算力 / 半导体",
    "title": "AMD working on new X3D V-cache mobile chip for gaming laptops, leaker claims — Ryzen 7 9800HX3D could launch with 8 cores, 16 threads, and 96MB cache",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-working-on-new-x3d-v-cache-mobile-chip-for-gaming-laptops-leaker-claims-ryzen-7-9800hx3d-could-launch-with-8-cores-16-threads-and-96mb-cache",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T15:07:53+00:00",
    "summary": "A fresh leak suggests AMD is preparing an 8-core, 16-thread Zen 5 mobile processor with 96MB of L3 cache, potentially bringing the desktop Ryzen 7 9800X3D experience to gaming laptops."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/gigabyte-announces-support-for-chinese-made-cxmt-memory-pushes-it-to-8200-mt-s-on-socket-am5",
    "domain": "AI 算力 / 半导体",
    "title": "Gigabyte announces support for Chinese-made CXMT memory — pushes it to 8200 MT/s on Socket AM5",
    "url": "https://www.tomshardware.com/pc-components/ddr5/gigabyte-announces-support-for-chinese-made-cxmt-memory-pushes-it-to-8200-mt-s-on-socket-am5",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T14:44:58+00:00",
    "summary": "The performance is impressive and it's good to see official support, but the question remains whether you can actually buy any of it."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/south-korean-memory-giants-samsung-and-sk-hynix-are-set-to-announce-massive-deals-with-leading-u-s-tech-firms-report-claims-korean-president-arrives-in-silicon-valley-for-meetings-and-high-profile-ai-summit",
    "domain": "AI 算力 / 半导体",
    "title": "South Korean memory giants Samsung and SK Hynix are set to announce massive deals with leading U.S. tech firms, report claims — Korean president arrives in Silicon Valley for meetings and high-profile",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/south-korean-memory-giants-samsung-and-sk-hynix-are-set-to-announce-massive-deals-with-leading-u-s-tech-firms-report-claims-korean-president-arrives-in-silicon-valley-for-meetings-and-high-profile-ai-summit",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T14:43:04+00:00",
    "summary": "Samsung and SK Hynix are expected to unveil multibillion-dollar memory-chip partnerships with major U.S. technology companies during South Korean President Lee Jae Myung’s visit to San Francisco"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-exec-was-very-happy-to-see-nvidias-vera-performance-results-i-actually-thought-we-were-beating-them-by-smaller-numbers",
    "domain": "AI 算力 / 半导体",
    "title": "AMD exec was ‘very happy’ to see Nvidia‘s Vera performance results – ‘I actually thought we were beating them by smaller numbers’",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-exec-was-very-happy-to-see-nvidias-vera-performance-results-i-actually-thought-we-were-beating-them-by-smaller-numbers",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T14:39:03+00:00",
    "summary": "Nvidia took the first stab with its Vera results earlier this week, and now AMD is biting back with SPEC results for its Zen 6 ‘Venice’ CPUs, as well."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/when-will-the-ea-greed-end-fans-vent-their-fury-as-company-announces-usd150-version-of-fc-27-annual-game-release-comes-in-three-editions-but-top-tier-option-is-50-percent-more-expensive-than-gta-vi-ultimate",
    "domain": "AI 算力 / 半导体",
    "title": "'When will the EA greed end': Fans vent their fury as company announces $150 version of FC 27 — annual game release comes in three editions, but top-tier option is 50% more expensive than GTA VI Ultim",
    "url": "https://www.tomshardware.com/video-games/when-will-the-ea-greed-end-fans-vent-their-fury-as-company-announces-usd150-version-of-fc-27-annual-game-release-comes-in-three-editions-but-top-tier-option-is-50-percent-more-expensive-than-gta-vi-ultimate",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T14:15:33+00:00",
    "summary": "EA's FC 27 is available in three options, starting at $69.99 for the base game and going up to $149.99 for the Ultimate Plus Edition. The top-tier option, which costs more than double than the Standar"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-took-ten-days-to-tell-hugging-face-its-models-were-behind-the-july-11-weekend-hack",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI took ten days to tell Hugging Face its models were behind the July 11 weekend hack, report claims — rogue AI agents reportedly active on the open Internet for several days",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-took-ten-days-to-tell-hugging-face-its-models-were-behind-the-july-11-weekend-hack",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T13:47:15+00:00",
    "summary": "OpenAI confirmed to Hugging Face only this week that models it was testing carried out the July 11 attack on the AI platform's production infrastructure."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/president-trump-expands-ai-data-center-ratepayer-protection-pledge-to-include-state-governors-and-utility-companies-white-house-claims-this-will-make-electricity-more-affordable",
    "domain": "AI 算力 / 半导体",
    "title": "President Trump expands AI data center ‘ratepayer protection pledge’ to include state governors and utility companies — White House claims this will make electricity more affordable",
    "url": "https://www.tomshardware.com/tech-industry/policy/president-trump-expands-ai-data-center-ratepayer-protection-pledge-to-include-state-governors-and-utility-companies-white-house-claims-this-will-make-electricity-more-affordable",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T11:42:41+00:00",
    "summary": "U.S. President Donald Trump expands the 'ratepayer protection pledge' to include states, utility companies, and data center developers. He claims that the pledge will help electricity costs go down, e"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/45-percent-off-slashed-to-just-usd1-099-this-bargain-rtx-5060-powered-gaming-laptop-is-discounted-by-usd900-at-hp-near-half-price-hyperx-omen-16-is-the-perfect-gaming-laptop-for-heading-back-to-school",
    "domain": "AI 算力 / 半导体",
    "title": "45% off: Slashed to just $1,099, this bargain RTX 5060-powered gaming laptop is discounted by $900 at HP — near half-price HyperX Omen 16 is the perfect gaming laptop for heading back to school",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/45-percent-off-slashed-to-just-usd1-099-this-bargain-rtx-5060-powered-gaming-laptop-is-discounted-by-usd900-at-hp-near-half-price-hyperx-omen-16-is-the-perfect-gaming-laptop-for-heading-back-to-school",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T11:21:42+00:00",
    "summary": "Save a massive $900 on HP's HyperX Omen 16 with RTX 5060. The perfect back-to-school gaming laptop is now only $1,099."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd460-on-this-amd-9800x3d-gaming-pc-with-rtx-5080-get-blistering-4k-performance-for-less",
    "domain": "AI 算力 / 半导体",
    "title": "Save $460 on this AMD 9800X3D gaming PC with RTX 5080 — get blistering 4K performance for less",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd460-on-this-amd-9800x3d-gaming-pc-with-rtx-5080-get-blistering-4k-performance-for-less",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T10:48:02+00:00",
    "summary": "Get an RTX 5080 gaming PC with 9800X3D for $2,829 at Newegg."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amd-confirmed-usd5-4-billion-ati-acquisition-20-years-ago-today-deal-to-reinvent-our-industry-paved-the-way-for-radeon-gpu-innovation-apus-and-games-console-domination",
    "domain": "AI 算力 / 半导体",
    "title": "AMD confirmed $5.4 billion ATI acquisition 20 years ago today — deal to 'reinvent our industry' paved the way for Radeon GPU innovation, APUs, and games console domination",
    "url": "https://www.tomshardware.com/pc-components/gpus/amd-confirmed-usd5-4-billion-ati-acquisition-20-years-ago-today-deal-to-reinvent-our-industry-paved-the-way-for-radeon-gpu-innovation-apus-and-games-console-domination",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T10:00:00+00:00",
    "summary": "On this day in 2006, AMD confirmed its acquisition of graphics chip firm ATI. AMD stumped up a cash-and-stock deal worth a total of $5.4B for the Canadian PC graphics innovators."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-reveals-cpu-architecture-roadmap-through-2028-following-zen-6-venice-launch-zen-7-florence-to-debut-in-2028-alongside-diversified-product-family-confirms-zen-8-ravenna-in-development",
    "domain": "AI 算力 / 半导体",
    "title": "AMD reveals CPU architecture roadmap through 2028, following Zen 6 'Venice' launch — Zen 7 'Florence' to debut in 2028 alongside diversified product family, confirms Zen 8 'Ravenna' in development",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-reveals-cpu-architecture-roadmap-through-2028-following-zen-6-venice-launch-zen-7-florence-to-debut-in-2028-alongside-diversified-product-family-confirms-zen-8-ravenna-in-development",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T09:27:05+00:00",
    "summary": "AMD's Lisa Su shows off the company's roadmap through 2030, including teases of Zen 7 and Zen 8 CPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-new-x100-chip-lineup-puts-strix-halo-into-robots-apus-for-physical-ai-bring-zen-5-cpu-rdna-3-5-gpu-cores-to-compete-with-intels-panther-lake",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s new X100 chip lineup puts embedded Ryzen AI 'Strix Halo' chips into robots – APUs for physical AI bring Zen 5 CPU, RDNA 3.5 GPU cores to compete with Intel’s Panther Lake",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-new-x100-chip-lineup-puts-strix-halo-into-robots-apus-for-physical-ai-bring-zen-5-cpu-rdna-3-5-gpu-cores-to-compete-with-intels-panther-lake",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T18:30:00+00:00",
    "summary": "Countering Intel’s recent moves, AMD is bringing its Strix Halo APUs to the realm of robots, and physical AI. Designed for 24/7 operation and a 10-year embedded lifecycle, X100 will also be offered as"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amd-takes-the-wraps-off-its-instinct-mi455x-ai-accelerator-cdna-5-and-helios-rack-scale-architecture-combine-to-take-the-fight-to-nvidia-in-the-data-center",
    "domain": "AI 算力 / 半导体",
    "title": "AMD takes the wraps off its Instinct MI455X AI accelerator — CDNA 5 and Helios rack-scale architecture combine to take the fight to Nvidia in the data center",
    "url": "https://www.tomshardware.com/pc-components/gpus/amd-takes-the-wraps-off-its-instinct-mi455x-ai-accelerator-cdna-5-and-helios-rack-scale-architecture-combine-to-take-the-fight-to-nvidia-in-the-data-center",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T18:05:44+00:00",
    "summary": "AMD showed off its MI455X accelerator at its Advancing AI 2026 event, demonstrating its strong competitive performance, large HBM memory capacity, and Helios rack-scale architecture."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-and-cerebras-partner-on-low-latency-high-throughput-ai-inference-epyc-processors-in-helios-rack-scale-infrastructure-paired-with-cerebras-wafer-scale-engine-wse-solutions",
    "domain": "AI 算力 / 半导体",
    "title": "AMD and Cerebras partner on low-latency, high-throughput AI inference — EPYC processors in Helios rack-scale infrastructure paired with Cerebras' Wafer-Scale Engine (WSE) solutions",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-and-cerebras-partner-on-low-latency-high-throughput-ai-inference-epyc-processors-in-helios-rack-scale-infrastructure-paired-with-cerebras-wafer-scale-engine-wse-solutions",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:45:00+00:00",
    "summary": "When AMD's Helios meets giant wafers from Cerebras, it is not like when Odysseus meets with the Laestrygonian Giants, they collaborate to build an ultimate data center solution."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-3090-and-rtx-3050-team-up-to-hit-144-fps-at-4k-lossless-scaling-turns-old-ampere-gpus-into-a-gaming-powerhouse",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX 3090 and RTX 3050 team up to hit 144 FPS at 4K — Lossless Scaling turns old Ampere GPUs into a gaming powerhouse",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-3090-and-rtx-3050-team-up-to-hit-144-fps-at-4k-lossless-scaling-turns-old-ampere-gpus-into-a-gaming-powerhouse",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:39:03+00:00",
    "summary": "A gaming enthusiast leverages Lossless Scaling to supercharge a gaming PC with a GeForce RTX 3090 and GeForce RTX 3050 to deliver up to 144 FPS at 4K."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/new-semiconductor-firm-breaks-cover-backed-by-usd43-million-in-early-stage-funding-tylsemi-aims-to-deliver-custom-silicon-to-customers-without-breaking-the-bank",
    "domain": "AI 算力 / 半导体",
    "title": "New semiconductor firm breaks cover, backed by $43 million in early-stage funding — TYLsemi aims to deliver custom silicon to customers without breaking the bank",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/new-semiconductor-firm-breaks-cover-backed-by-usd43-million-in-early-stage-funding-tylsemi-aims-to-deliver-custom-silicon-to-customers-without-breaking-the-bank",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:34:06+00:00",
    "summary": "TYLsemi is set to offer pre-validated chiplets, along with custom ASIC design services, and build highly custom multi-tile processors at relatively low costs."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-256-core-epyc-9996-venice-claims-up-to-a-3-4x-jump-over-intel-xeon-competition-20-percent-over-nvidia-vera-zen-6-comes-with-up-to-1024mb-of-l3-16-channel-memory-and-5ghz-clock-speeds",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s 256-core Epyc 9996 ‘Venice’ claims up to a 3.4x jump over Intel Xeon competition, 20% over Nvidia Vera – Zen 6 comes with up to 1024MB of L3, 16-channel memory, and 5GHz+ clock speeds",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-256-core-epyc-9996-venice-claims-up-to-a-3-4x-jump-over-intel-xeon-competition-20-percent-over-nvidia-vera-zen-6-comes-with-up-to-1024mb-of-l3-16-channel-memory-and-5ghz-clock-speeds",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:24:50+00:00",
    "summary": "After over a year of teases, AMD has finally provided details on its 256-core Venice CPU with the Zen 6 architecture, now known as the Epyc 9996."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-venice-x-cpu-launches-in-2027-with-1152-mb-of-3d-v-cache-96-cores-and-5-15-ghz-boost-clock-zen-6-cpu-for-high-performance-computing-comes-with-major-pillars-of-venice",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s Venice-X CPU launches in 2027 with 1152 MB of 3D V-Cache, 96 cores, and 5.15 GHz boost clock – Zen 6 CPU for high-performance computing comes with major pillars of Venice",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-venice-x-cpu-launches-in-2027-with-1152-mb-of-3d-v-cache-96-cores-and-5-15-ghz-boost-clock-zen-6-cpu-for-high-performance-computing-comes-with-major-pillars-of-venice",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:17:54+00:00",
    "summary": "AMD is returning to 3D V-Cache in its data center range of CPUs with Venice-X, which it has confirmed will launch in the second half of 2027, with 1152 MB of L3 and clock speeds up to 5.15 GHz."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/geekbench-7-introduces-biggest-overhaul-yet-real-world-cpu-testing-new-media-workloads-ai-benchmarks-and-cuda-support",
    "domain": "AI 算力 / 半导体",
    "title": "Geekbench 7 introduces biggest overhaul yet — real-world CPU testing, new media workloads, AI benchmarks, and CUDA support",
    "url": "https://www.tomshardware.com/software/geekbench-7-introduces-biggest-overhaul-yet-real-world-cpu-testing-new-media-workloads-ai-benchmarks-and-cuda-support",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T17:00:00+00:00",
    "summary": "The latest update introduces more realistic CPU and GPU workloads, redesigned multi-core testing, AI-focused benchmarks, larger datasets, and CUDA support for Nvidia GPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/ai-memory-shortage-is-now-increasing-the-price-of-cars-gm-warns-of-vast-cost-increases-byd-hikes-driver-assistance-prices-20-percent",
    "domain": "AI 算力 / 半导体",
    "title": "AI memory shortage is now increasing the price of cars — GM warns of vast cost increases, BYD hikes driver assistance prices 20%",
    "url": "https://www.tomshardware.com/pc-components/ram/ai-memory-shortage-is-now-increasing-the-price-of-cars-gm-warns-of-vast-cost-increases-byd-hikes-driver-assistance-prices-20-percent",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T15:57:19+00:00",
    "summary": "GM CFO Paul Jacobson says that the company's costs are expected to increase by $1.5 to $2 billion, primarily due to increasing memory chip costs. The move comes as the RAM shortage is affecting the au"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/bipartisan-bill-would-require-kill-switches-on-the-most-powerful-ai-models",
    "domain": "AI 算力 / 半导体",
    "title": "Kill switches for most powerful AI models proposed by Bipartisan bill — DHS could order throttling or full shutdown, with fines up to $20 million per day",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/bipartisan-bill-would-require-kill-switches-on-the-most-powerful-ai-models",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T15:02:31+00:00",
    "summary": "The bill amends the Homeland Security Act and covers companies earning at least $500 million in annual revenue from a model trained with compute costing more than $100 million."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/inside-optical-and-the-battle-for-scale-how-the-ai-industry-is-racing-to-integrate-photonic-interconnects",
    "domain": "AI 算力 / 半导体",
    "title": "Inside optical and the battle for scale – how the AI industry is racing to integrate photonic interconnects",
    "url": "https://www.tomshardware.com/tech-industry/inside-optical-and-the-battle-for-scale-how-the-ai-industry-is-racing-to-integrate-photonic-interconnects",
    "source": "Chris Stokel-Walker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T14:22:54+00:00",
    "summary": "With the limitations of copper looming, the industry is transitioning to photonic interconnects to scale data center capabilities. We spoke to experts such as Lightmatter chief executive Nick Harris a"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-and-amd-sign-long-term-server-cpu-deals-with-chinese-customers-as-prices-jump-over-40-percent",
    "domain": "AI 算力 / 半导体",
    "title": "Intel and AMD sign long-term server CPU deals with Chinese customers as prices jump over 40%, report claims — agreements purportedly guarantee purchase volumes for about a year without fixing prices",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-and-amd-sign-long-term-server-cpu-deals-with-chinese-customers-as-prices-jump-over-40-percent",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T13:49:39+00:00",
    "summary": "Some customers have discussed commitments running two years or longer, one source told Reuters."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/arctic-senza-ai-370-fanless-mini-pc-review",
    "domain": "AI 算力 / 半导体",
    "title": "Arctic Senza AI 370 review: Strix Point in a stealthy under-desk fanless design",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/arctic-senza-ai-370-fanless-mini-pc-review",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T13:00:54+00:00",
    "summary": "The Arctic Senza AI 370 is a fanless mini PC designed to mount under your desk. Everyday performance isn’t held back by the lack of active cooling, and its soldered dual-channel 32GB LPDDR5X-8000 is a"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-10-percent-on-the-brand-new-creality-pika-3d-scanner-easily-scan-models-and-textures-for-usd629",
    "domain": "AI 算力 / 半导体",
    "title": "Save 10% on the brand-new Creality Pika 3D scanner — easily scan models and textures for $629",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-10-percent-on-the-brand-new-creality-pika-3d-scanner-easily-scan-models-and-textures-for-usd629",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T11:55:18+00:00",
    "summary": "Pre-purchase Creality's portable Pika 3D scanner at a discount. First come, first served: a 10% saving if you act within 19 days."
  },
  {
    "id": "hn:49012431",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia released its first official GeForce driver for Windows on Arm",
    "url": "https://videocardz.com/newz/nvidias-first-geforce-driver-for-windows-on-arm-confirms-rtx-spark-n1x-with-6144-or-5120-cuda-cores",
    "source": "robotnikman",
    "platform": "hackernews",
    "points": 21,
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
    "id": "hn:48993130",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.6 Flash",
    "url": "https://console.cloud.google.com/agent-platform/publishers/google/model-garden/gemini-3.6-flash",
    "source": "marrf",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-07-21T14:56:15+00:00",
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
    "id": "rss:https://www.theverge.com/tech/970970/after-backlash-meta-pauses-plan-to-rate-limit-its-smart-glasses",
    "domain": "大厂 AI 动态",
    "title": "After backlash, Meta pauses plan to ‘rate limit’ its smart glasses",
    "url": "https://www.theverge.com/tech/970970/after-backlash-meta-pauses-plan-to-rate-limit-its-smart-glasses",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T22:27:46+00:00",
    "summary": "Remember when Meta was planning to charge a $20 monthly subscription fee for the smart glasses feature that lets people hear each other more clearly - even though that feature runs locally on your gla"
  },
  {
    "id": "rss:https://www.theverge.com/report/970901/instagram-meta-glasses-prank-harassment-ban",
    "domain": "大厂 AI 动态",
    "title": "Meta just created a moderation nightmare for its smart glasses",
    "url": "https://www.theverge.com/report/970901/instagram-meta-glasses-prank-harassment-ban",
    "source": "Mia Sato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T19:23:44+00:00",
    "summary": "Meta's smart glasses have been a PR headache for the company. Public backlash has been swift, and fierce; people are concerned about the erosion of privacy and expansion of surveillance. Some especial"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/970910/qualcomm-raising-prices-bloomberg",
    "domain": "大厂 AI 动态",
    "title": "Qualcomm is about to raise prices and that&#8217;s bad news for everyone",
    "url": "https://www.theverge.com/gadgets/970910/qualcomm-raising-prices-bloomberg",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T19:14:23+00:00",
    "summary": "Qualcomm sent a letter to customers on Friday warning of plans to increase its prices by \"a percentage in the double digits,\" Bloomberg reports. The price hikes will go into effect starting with produ"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/970894/midjourney-co-star-acquisition",
    "domain": "大厂 AI 动态",
    "title": "Midjourney bought the astrology app Co-Star",
    "url": "https://www.theverge.com/ai-artificial-intelligence/970894/midjourney-co-star-acquisition",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T19:06:58+00:00",
    "summary": "Midjourney, which has gone from generating AI cat images to full-body ultrasound scans, is getting into a new field: astrology. The AI startup announced on Thursday that it has acquired the personaliz"
  },
  {
    "id": "rss:https://www.theverge.com/policy/970742/dji-camera-clone-company-xtra-is-halting-and-refunding-all-preorders",
    "domain": "大厂 AI 动态",
    "title": "DJI camera clone company Xtra is halting and refunding all preorders",
    "url": "https://www.theverge.com/policy/970742/dji-camera-clone-company-xtra-is-halting-and-refunding-all-preorders",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T18:27:00+00:00",
    "summary": "After selling a barely disguised version of the hit DJI Osmo Pocket 3 in the United States last year, Xtra Technology seemed ready to sneak in its version of the new dual-lens Osmo Pocket 4 Pro, too. "
  },
  {
    "id": "rss:https://www.theverge.com/tech/970848/nothing-layoffs-rumors-phone-4b",
    "domain": "大厂 AI 动态",
    "title": "Nothing confirms layoffs, but calls market exit rumors &#8216;fake news&#8217;",
    "url": "https://www.theverge.com/tech/970848/nothing-layoffs-rumors-phone-4b",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T18:10:22+00:00",
    "summary": "In response to a report that Nothing is planning to \"exit 12 markets as global shipments decline,\" Nothing cofounder Akis Evangelidis said the company is \"reorganizing\" and laying off some of its staf"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/970814/roku-streaming-price-increase",
    "domain": "大厂 AI 动态",
    "title": "Roku raises streaming hardware prices by up to $50",
    "url": "https://www.theverge.com/streaming/970814/roku-streaming-price-increase",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T18:07:19+00:00",
    "summary": "Roku has increased prices across its streaming hardware, with the cheapest HD Streaming Stick now priced at $39.99 instead of $29.99, as first reported by The Desk. The price hike affects all of Roku'"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/970524/blade-runner-2099-date-trailer-amazon-prime-video",
    "domain": "大厂 AI 动态",
    "title": "Blade Runner 2099’s moody dystopia streams on Amazon in November",
    "url": "https://www.theverge.com/entertainment/970524/blade-runner-2099-date-trailer-amazon-prime-video",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:40:00+00:00",
    "summary": "After teasing the series with some first-look images yesterday, Amazon is finally properly unveiling its Blade Runner streaming series. Called Blade Runner 2099, the show hits Prime Video on November "
  },
  {
    "id": "rss:https://www.theverge.com/podcast/970735/google-zero-reddit-ai-publishers-vergecast",
    "domain": "大厂 AI 动态",
    "title": "You can’t ignore Google Zero anymore",
    "url": "https://www.theverge.com/podcast/970735/google-zero-reddit-ai-publishers-vergecast",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:29:48+00:00",
    "summary": "The web and Google once had a deal: Google collects data and indexes webpages and in exchange sends oceans of traffic to websites. The deal wasn't perfect and certainly made Google more money than it "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/970105/claude-opus-5-announced-anthropic-ai-model-release",
    "domain": "大厂 AI 动态",
    "title": "Anthropic releases Opus 5 with ‘close’ to Fable 5’s capabilities",
    "url": "https://www.theverge.com/ai-artificial-intelligence/970105/claude-opus-5-announced-anthropic-ai-model-release",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:00:00+00:00",
    "summary": "Weeks after Anthropic's latest toe-to-toe with the US government, and days after an OpenAI security incident that dominated tech industry discussions, Anthropic on Thursday released its newest model, "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/i-tried-out-openais-new-ai-keypad-which-will-be-fun-for-coders-and-slightly-mystifying-to-everyone-else/",
    "domain": "大厂 AI 动态",
    "title": "I tried out OpenAI’s new AI keypad — which will be fun for some coders and slightly mystifying to everyone else",
    "url": "https://techcrunch.com/2026/07/24/i-tried-out-openais-new-ai-keypad-which-will-be-fun-for-coders-and-slightly-mystifying-to-everyone-else/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T00:23:11+00:00",
    "summary": "OpenAI's fancy new AI keypad will be a lot of fun for some, while many others are probably not going to touch it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/spacex-launches-new-v3-starlink-satellites-but-suffers-another-booster-failure/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX launches new V3 Starlink satellites but suffers another booster failure",
    "url": "https://techcrunch.com/2026/07/24/spacex-launches-new-v3-starlink-satellites-but-suffers-another-booster-failure/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T23:25:47+00:00",
    "summary": "The company ticked off a few more boxes on the second Starship V3 flight, but appears to have had another issue relighting the booster's rocket engines."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/prentis-new-ai-lab-co-founded-by-reid-hoffman-mark-pincus-in-talks-to-raise-100m/",
    "domain": "大厂 AI 动态",
    "title": "Prentis, new AI lab co-founded by Reid Hoffman, Mark Pincus in talks to raise $100M",
    "url": "https://techcrunch.com/2026/07/24/prentis-new-ai-lab-co-founded-by-reid-hoffman-mark-pincus-in-talks-to-raise-100m/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T22:25:58+00:00",
    "summary": "The neolab is betting that automating routine computer tasks will soon outpace coding as AI's biggest use case."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/techcrunch-disrupt-2026s-new-smart-money-stage-explores-fintech-payments-ai-and-everything-between/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Disrupt 2026’s new Smart Money Stage explores fintech, payments, AI, and everything between",
    "url": "https://techcrunch.com/2026/07/24/techcrunch-disrupt-2026s-new-smart-money-stage-explores-fintech-payments-ai-and-everything-between/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T22:10:00+00:00",
    "summary": "Money has evolved into far more than the cash in your wallet or your bank account. And at TechCrunch Disrupt 2026, we’re devoting an entire stage to that progression."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/social-media-ban-children-countries-list/",
    "domain": "大厂 AI 动态",
    "title": "Vietnam is looking to restrict social media for kids; here are the growing number of other countries doing the same",
    "url": "https://techcrunch.com/2026/07/24/social-media-ban-children-countries-list/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T21:15:00+00:00",
    "summary": "Australia was the first country to issue a ban in late 2025, aiming to reduce the pressures and risks that young users may face on social media, including cyberbullying, social media addiction, and ex"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/waymo-reportedly-mulling-a-breakup-with-uber/",
    "domain": "大厂 AI 动态",
    "title": "Waymo reportedly mulling a breakup with Uber",
    "url": "https://techcrunch.com/2026/07/24/waymo-reportedly-mulling-a-breakup-with-uber/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T20:43:35+00:00",
    "summary": "The contract between the two companies ends in May 2028, Uber told TechCrunch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/volkswagen-engineers-charged-with-insider-trading-tied-to-rivian-joint-venture/",
    "domain": "大厂 AI 动态",
    "title": "Volkswagen engineers charged with insider trading tied to Rivian joint venture",
    "url": "https://techcrunch.com/2026/07/24/volkswagen-engineers-charged-with-insider-trading-tied-to-rivian-joint-venture/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T19:56:23+00:00",
    "summary": "The indictment, which was unsealed Friday, alleges the Volkswagen engineers used confidential insider information to buy stock in Rivian."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/why-cognition-bought-poke-ai-personality-is-becoming-a-competitive-advantage/",
    "domain": "大厂 AI 动态",
    "title": "Why Cognition bought Poke: AI personality is becoming a competitive advantage",
    "url": "https://techcrunch.com/2026/07/24/why-cognition-bought-poke-ai-personality-is-becoming-a-competitive-advantage/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T18:07:32+00:00",
    "summary": "The acquisition brings Poke’s conversational style and interaction model to Cognition’s coding agent Devin, reflecting a growing belief that how AI assistants interact with users is as important as th"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/us-accuses-american-of-allegedly-wiping-his-phone-using-a-duress-password-during-border-search/",
    "domain": "大厂 AI 动态",
    "title": "US accuses American of allegedly wiping his phone using a ‘duress’ password during border search",
    "url": "https://techcrunch.com/2026/07/24/us-accuses-american-of-allegedly-wiping-his-phone-using-a-duress-password-during-border-search/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:53:30+00:00",
    "summary": "A U.S. citizen has asked a court to throw out the government's claim that he gave over a passcode to border authorities that wiped his phone's data, opening up fresh questions about a person's constit"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/anduril-reportedly-in-talks-to-raise-funding-at-100b-valuation-more-than-3x-last-years-mark/",
    "domain": "大厂 AI 动态",
    "title": "Anduril reportedly in talks to raise funding at $100B valuation, more than 3x last year’s mark",
    "url": "https://techcrunch.com/2026/07/24/anduril-reportedly-in-talks-to-raise-funding-at-100b-valuation-more-than-3x-last-years-mark/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:33:19+00:00",
    "summary": "Anduril is said to be raising a new round of funding that may push its valuation up to about $100 billion, per Reuters."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/build-in-public-fail-in-public-what-its-like-to-be-a-founder-under-20-right-now/",
    "domain": "大厂 AI 动态",
    "title": "Build in public, fail in public: what it’s like to be a founder under 20 right now",
    "url": "https://techcrunch.com/2026/07/24/build-in-public-fail-in-public-what-its-like-to-be-a-founder-under-20-right-now/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:00:00+00:00",
    "summary": "AI tools have democratized the opportunity to build, shortening the timelines of success and enabling more young people to start successful companies without stepping foot inside a Big Tech company."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic launches Opus 5",
    "url": "https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:00:00+00:00",
    "summary": "Opus 5 will be both cheaper and less restrictive than Fable, likely making it preferable in most use cases."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/indias-move-against-jack-dorseys-bitchat-sparks-legal-debate/",
    "domain": "大厂 AI 动态",
    "title": "India’s move against Jack Dorsey’s Bitchat sparks legal debate",
    "url": "https://techcrunch.com/2026/07/24/indias-move-against-jack-dorseys-bitchat-sparks-legal-debate/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T16:54:58+00:00",
    "summary": "The offline messaging app surged in popularity in India amid protests in New Delhi."
  },
  {
    "id": "rss:https://techcrunch.com/video/openais-own-model-went-rogue-before-kimi-had-wall-street-sweating/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s own model went rogue before Kimi had Wall Street sweating",
    "url": "https://techcrunch.com/video/openais-own-model-went-rogue-before-kimi-had-wall-street-sweating/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T16:50:08+00:00",
    "summary": "Chinese AI lab Moonshot&#8217;s&#160;open model Kimi went viral this week&#160;for reasons that had less to do with the model itself and more to do with&#160;how the U.S. AI industry reacted to it. Me"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/sam-altmans-biometric-startup-world-raises-52-5-million-via-crypto-sale/",
    "domain": "大厂 AI 动态",
    "title": "Sam Altman’s biometric startup World raises $52.5M via crypto sale",
    "url": "https://techcrunch.com/2026/07/24/sam-altmans-biometric-startup-world-raises-52-5-million-via-crypto-sale/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T16:11:56+00:00",
    "summary": "Sam Altman's side project — which seeks to scan the world's eyeballs and turn them into unique digital identifiers — has raised some fresh cash through a crypto sale."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/as-us-weighs-response-to-chinese-ai-industry-urges-against-broad-open-weight-restrictions/",
    "domain": "大厂 AI 动态",
    "title": "As US weighs response to Chinese AI, industry urges against broad open-weight restrictions",
    "url": "https://techcrunch.com/2026/07/24/as-us-weighs-response-to-chinese-ai-industry-urges-against-broad-open-weight-restrictions/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T15:51:49+00:00",
    "summary": "AI companies, including Nvidia and Mistral, urge policymakers to avoid broad restrictions on open-weight AI models as Washington debates responses to Chinese AI and alleged model distillation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/rivian-sues-the-us-government-for-full-refund-of-trump-tariffs/",
    "domain": "大厂 AI 动态",
    "title": "Rivian sues the US government for ‘full refund’ of Trump tariffs",
    "url": "https://techcrunch.com/2026/07/24/rivian-sues-the-us-government-for-full-refund-of-trump-tariffs/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T15:16:31+00:00",
    "summary": "The automaker joins a long line of companies seeking such refunds. In April, Rivian CFO Claire McDonough said she expected the company stood to reap a refund in the \"tens of millions of dollars.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/blueskys-ai-assistant-attie-expands-into-an-open-social-research-tool/",
    "domain": "大厂 AI 动态",
    "title": "Bluesky’s AI assistant Attie expands into an open social research tool",
    "url": "https://techcrunch.com/2026/07/24/blueskys-ai-assistant-attie-expands-into-an-open-social-research-tool/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T15:13:57+00:00",
    "summary": "Users can now ask Attie questions about news, trends, and conversations on Bluesky and other apps on the AT Protocol."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/midjourney-acquired-the-astrology-app-co-star/",
    "domain": "大厂 AI 动态",
    "title": "Midjourney acquired the astrology app Co-Star",
    "url": "https://techcrunch.com/2026/07/24/midjourney-acquired-the-astrology-app-co-star/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T15:09:55+00:00",
    "summary": "The AI lab Midjourney continues to expand its purview beyond image and video generation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/openais-new-voice-mode-makes-it-to-the-chatgpt-desktop-app/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s new voice mode makes it to the ChatGPT desktop app",
    "url": "https://techcrunch.com/2026/07/24/openais-new-voice-mode-makes-it-to-the-chatgpt-desktop-app/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T13:36:42+00:00",
    "summary": "ChatGPT Voice on desktop can work with both ChatGPT Work and Codex to complete tasks and control agents."
  },
  {
    "id": "rss:https://stratechery.com/2026/the-copium-wars/",
    "domain": "大厂 AI 动态",
    "title": "2026.30: The Copium Wars",
    "url": "https://stratechery.com/2026/the-copium-wars/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of July 20, 2026 including Chinese models and frontier futures, what happened to Hugging Face, and the NBA and its second apron bet."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/wildfire-forces-evacuation-of-nasas-deep-space-network-complex-in-spain/",
    "domain": "大厂 AI 动态",
    "title": "Wildfire forces evacuation of NASA's Deep Space Network complex in Spain",
    "url": "https://arstechnica.com/space/2026/07/wildfire-forces-evacuation-of-nasas-deep-space-network-complex-in-spain/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T22:28:20+00:00",
    "summary": "\"Any potential damage will be assessed when it is safe to do so.\""
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/after-court-loss-paramount-agrees-to-delay-warner-bros-merger-until-trial/",
    "domain": "大厂 AI 动态",
    "title": "Paramount/WBD merger delayed for months as states' lawsuit moves toward trial",
    "url": "https://arstechnica.com/tech-policy/2026/07/after-court-loss-paramount-agrees-to-delay-warner-bros-merger-until-trial/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T21:56:02+00:00",
    "summary": "“Halting this merger while our case proceeds is a critical victory,\" NY AG said."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/canadian-legislator-reads-out-apparent-llm-response-in-floor-speech/",
    "domain": "大厂 AI 动态",
    "title": "Canadian legislator reads out apparent LLM response in floor speech",
    "url": "https://arstechnica.com/ai/2026/07/canadian-legislator-reads-out-apparent-llm-response-in-floor-speech/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T21:25:15+00:00",
    "summary": "\"Here’s a more natural, flowing version of that section...\""
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/anthropics-opus-5-is-about-token-efficiency-not-a-capability-leap/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic's Opus 5 is about token efficiency, not a capability leap",
    "url": "https://arstechnica.com/ai/2026/07/anthropics-opus-5-is-about-token-efficiency-not-a-capability-leap/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T21:05:51+00:00",
    "summary": "Models are improving quickly, but the cheaper options are often good enough."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/roku-raises-streaming-stick-prices-by-up-to-60-percent/",
    "domain": "大厂 AI 动态",
    "title": "Roku raises streaming stick prices by up to 60 percent",
    "url": "https://arstechnica.com/gadgets/2026/07/roku-raises-streaming-stick-prices-by-up-to-60-percent/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T19:41:06+00:00",
    "summary": "Roku blames RAM shortage after CEO called it \"great\" for business in May."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/rfk-jr-s-hand-picked-committee-approves-manufacture-of-peptides-he-uses/",
    "domain": "大厂 AI 动态",
    "title": "RFK Jr.'s handpicked committee approves manufacture of peptides he uses",
    "url": "https://arstechnica.com/health/2026/07/rfk-jr-s-hand-picked-committee-approves-manufacture-of-peptides-he-uses/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T19:10:09+00:00",
    "summary": "There's no human safety or efficacy data, but that no longer seems to matter."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/judge-rebuffs-trump-admin-demand-for-phone-records-from-nyt-reporters/",
    "domain": "大厂 AI 动态",
    "title": "Judge rebuffs Trump admin demand for phone records from NYT reporters",
    "url": "https://arstechnica.com/tech-policy/2026/07/judge-rebuffs-trump-admin-demand-for-phone-records-from-nyt-reporters/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T18:02:21+00:00",
    "summary": "\"We can quash the subpoenas, or you could withdraw the subpoenas,” judge told US."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/european-union-grants-us-request-to-restrict-satellite-images-of-iran-war-region/",
    "domain": "大厂 AI 动态",
    "title": "European Union grants US request to restrict satellite images of Iran War region",
    "url": "https://arstechnica.com/space/2026/07/european-union-grants-us-request-to-restrict-satellite-images-of-iran-war-region/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:45:05+00:00",
    "summary": "New delay on Copernicus satellite pics comes as US ramps up war with Iran again."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/team-uses-alphafold-ai-to-redesign-gene-editing-proteins-to-make-them-safer/",
    "domain": "大厂 AI 动态",
    "title": "Team uses AlphaFold AI to redesign gene-editing proteins to make them safer",
    "url": "https://arstechnica.com/science/2026/07/team-uses-alphafold-ai-to-redesign-gene-editing-proteins-to-make-them-safer/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:31:26+00:00",
    "summary": "Google's AlphaFold can help ID what parts of a gene editing protein enable mistakes."
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
    "id": "hn:49024958",
    "domain": "股票",
    "title": "DOT cranks up its campaign to strip bike lane references from federal websites",
    "url": "https://text.npr.org/nx-s1-5900901",
    "source": "Jtsummers",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-07-23T17:11:39+00:00",
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
    "id": "hn:49033778",
    "domain": "股票",
    "title": "Reality Bites Elon Musk and His Tesla, SpaceX Believers",
    "url": "https://www.wsj.com/finance/stocks/reality-bites-elon-musk-and-his-tesla-spacex-believers-1b639591",
    "source": "doener",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-24T10:59:51+00:00",
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
    "id": "wscn:3777924",
    "domain": "股票",
    "title": "Anthropic也要自研AI芯片了！已向SK海力士寻求供应",
    "url": "https://wallstreetcn.com/articles/3777924",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T05:11:53+00:00",
    "summary": "继谷歌、亚马逊、Meta之后，AI开发商Anthropic加入芯片自研竞赛——SK集团董事长崔泰源称之\"令人瞩目\"。"
  },
  {
    "id": "wscn:3777922",
    "domain": "股票",
    "title": "三大“反身性”阴霾笼罩市场",
    "url": "https://wallstreetcn.com/articles/3777922",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T04:07:11+00:00",
    "summary": "高盛警告全球市场面临三重负反馈循环：油价飙升叠加利率上行压制市场，政策迟迟未至加剧风险；谷歌将2026年资本支出上调至逾2000亿美元，自由现金流转负，引发超大规模云厂商叙事危机；AI基础设施债券价格大幅回落，产能扩张或演变为算力过剩。三重循环相互强化，反身性信号\"极度负面\"。"
  },
  {
    "id": "wscn:3777919",
    "domain": "股票",
    "title": "百元油价、AI反噬、关税重启--股市多头的“艰难盛夏”",
    "url": "https://wallstreetcn.com/articles/3777919",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T02:52:34+00:00",
    "summary": "霍尔木兹海峡通行量降至战前十分之一，超大规模科技公司CDS利差升至历史新高，10年期美债收益率升至4.66%——牛市的三根支柱同时承压。"
  },
  {
    "id": "wscn:3777920",
    "domain": "股票",
    "title": "罚没51.79亿元 市场监管总局对携程作出处罚",
    "url": "https://wallstreetcn.com/articles/3777920",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T02:07:44+00:00",
    "summary": "市场监管总局认定，携程实施了两种垄断行为：一是要求部分酒店开展独家合作，构成反垄断法禁止的限定交易行为；二是强制部分酒店给予“全网最低价”，构成反垄断法禁止的附加不合理交易条件行为。"
  },
  {
    "id": "wscn:3777916",
    "domain": "股票",
    "title": "下周“大波动”？市场严阵以待",
    "url": "https://wallstreetcn.com/articles/3777916",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T01:51:16+00:00",
    "summary": "标普500指数成分股中约34%将在下周集中发布财报，其中Mag7科技巨头中有四家将相继登场——微软与Meta定于周三披露业绩，苹果与亚马逊将于周四跟进。与此同时，美联储将于周三公布利率决议，目前市场对本次会议加息的概率定价约为30%。财报与政策信号的高度集中，令下周成为三季度行情走向的关键节点。"
  },
  {
    "id": "wscn:3777875",
    "domain": "股票",
    "title": "日元逼近164：日本当局干预紧迫性下降？",
    "url": "https://wallstreetcn.com/premium/articles/3777875?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T01:50:40+00:00",
    "summary": "日元逼近四十年低位暴露日本干预困境，利差与财政约束下政策空间收窄，短期震荡难改贬值趋势。"
  },
  {
    "id": "wscn:3777915",
    "domain": "股票",
    "title": "“TACO指数”预测：最晚7月30日，最可能是周日",
    "url": "https://wallstreetcn.com/articles/3777915",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T01:08:23+00:00",
    "summary": "Signum地缘政治咨询机构构建\"TACO指数\"，以布伦特原油、美债收益率、霍尔木兹海峡通行量及标普500为变量，量化特朗普在伊朗危机中的决策阈值。回测显示，当综合市场压力达约2.9个标准差时，特朗普历史上均会采取降级行动。基于当前市场线性外推，\"TACO时刻\"最可能出现在7月26日。"
  },
  {
    "id": "wscn:3777914",
    "domain": "股票",
    "title": "SpaceX星舰第13次试飞成功，发动机重启、溅落精准，马斯克：星舰完好无损",
    "url": "https://wallstreetcn.com/articles/3777914",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T00:34:18+00:00",
    "summary": "SpaceX星舰于美国中部时间24日成功完成第13次试飞，这也是公司IPO后首次成功飞行。本次试飞中，V3版本星舰成功在真空中重新点燃发动机，弥补了上次飞行缺憾；上级飞船在印度洋完成\"最平稳\"溅落，超重型助推器在墨西哥湾回收，全程无明显异常。"
  },
  {
    "id": "wscn:3777833",
    "domain": "股票",
    "title": "美伊谈判希望重燃，原油一度跌超5%，科技股压制美股反弹，芯片指数暴跌4%",
    "url": "https://wallstreetcn.com/articles/3777833",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T23:15:34+00:00",
    "summary": "标普惊险收涨，和道指扭转两连跌，纳指三连跌、收创近三个月新低。闪迪跌超10%，英特尔绩优仍跌近8%；特斯拉财报周跌近18%、创2022年来最大周跌幅。日元暂别1986年来低谷、创逾两月最大周跌幅；比特币盘中跌破6.4万美元、较日高跌超3%。原油止步五连涨、仍连涨三周，布油一周涨近10%。"
  },
  {
    "id": "wscn:3777908",
    "domain": "股票",
    "title": "华尔街见闻早餐FM-Radio | 2026年7月25日",
    "url": "https://wallstreetcn.com/articles/3777908",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T23:00:35+00:00",
    "summary": "五分钟看懂全球市场，尽在财经早餐。"
  },
  {
    "id": "wscn:3777913",
    "domain": "股票",
    "title": "特朗普新一轮全球关税遭小企业起诉，美贸易战再陷法律争议",
    "url": "https://wallstreetcn.com/articles/3777913",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T22:51:17+00:00",
    "summary": "最高法院此前已裁定IEEPA全球关税违法，特朗普政府转而祭出《1974年贸易法》第301条，以\"强迫劳动\"为由对60余个经济体征收10%-12.5%关税。多家小企业随即起诉，指控政府借新条款复制被推翻的旧关税体系，且未依法开展针对性调查。"
  },
  {
    "id": "wscn:3777911",
    "domain": "股票",
    "title": "马斯克“至暗一周”：特斯拉暴跌18%创2022年以来最大周跌幅，SpaceX星舰试飞前再跌7%",
    "url": "https://wallstreetcn.com/articles/3777911",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T22:47:53+00:00",
    "summary": "当前油价推升加息预期叠加AI回报担忧升温压制科技股，特斯拉Q2财报不及预期、现金流转负，SpaceX限售股即将解禁、星舰试飞两度取消。马斯克个人财富一周蒸发约1300亿美元，其在X平台发帖调侃称：“（前）万亿美元富翁。”"
  },
  {
    "id": "wscn:3777912",
    "domain": "股票",
    "title": "沙特主导的多国联军称打击也门胡塞武装军事目标",
    "url": "https://wallstreetcn.com/articles/3777912",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T22:21:04+00:00",
    "summary": "多国联军声明称，此次行动针对与胡塞武装海上威胁直接相关的军事目标展开；联军将继续采取一切必要行动保护航运安全，维护沙特的国家利益，如胡塞武装继续实施敌对行动，联军将继续回应。"
  },
  {
    "id": "wscn:3777910",
    "domain": "股票",
    "title": "大摩：若SpaceX跌至100美元，意味对其AI业务估值为零",
    "url": "https://wallstreetcn.com/articles/3777910",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T21:42:00+00:00",
    "summary": "摩根士丹利分析师Jonas指出，许多投资者预计SpaceX股价可能在首批限售股解禁后跌至100美元。他认为若股价跌至100美元，意味着市场对SpaceX的AI业务估值归零。Jonas给出300美元目标价，其中逾半来自AI业务，表示市场严重低估了Grok和Cursor的价值。"
  },
  {
    "id": "wscn:3777909",
    "domain": "股票",
    "title": "特朗普称美方正与伊朗谈判，不排除加大军事打击",
    "url": "https://wallstreetcn.com/articles/3777909",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T21:21:12+00:00",
    "summary": "特朗普称，美国有两种选择，一是继续军事行动并可能加大打击力度，二是通过谈判达成协议，他仍倾向于通过谈判解决问题，并认为，伊朗目前展现出的认真程度是迄今为止最高的。"
  },
  {
    "id": "wscn:3777903",
    "domain": "股票",
    "title": "英特尔与蓝思科技合作，探索基于玻璃基板的封装解决方案",
    "url": "https://wallstreetcn.com/articles/3777903",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T20:38:14+00:00",
    "summary": "双方聚焦玻璃基板封装解决方案，融合英特尔半导体架构优势与蓝思精密玻璃加工能力，合力攻克数据中心对高性能、高互连密度的迫切需求。双方认为未来潜在合作方向还包括AI PC组件、数据中心服务器散热解决方案以及边缘计算硬件设备。"
  },
  {
    "id": "wscn:3777905",
    "domain": "股票",
    "title": "营收指引上修、EPS原地踏步：美国运通利润超预期后暴跌6%，市场在为“增长代价”重新定价",
    "url": "https://wallstreetcn.com/articles/3777905",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T20:33:39+00:00",
    "summary": "美国运通二季度净利润31.1亿美元，每股收益4.53美元超预期，营收196.4亿美元同比增10%，全年营收增长指引上调至10%。然而，受费用端扩张压力及每股收益指引维持不变影响，股价盘中一度重挫逾6%。"
  },
  {
    "id": "wscn:3777907",
    "domain": "股票",
    "title": "香港微调杠杆及反向产品监管框架，引入投资者保障新措施",
    "url": "https://wallstreetcn.com/articles/3777907",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T20:33:27+00:00",
    "summary": "香港证监会修订杠杆及反向产品监管框架，核心变化为引入灵活杠杆机制，允许产品提供者在现行上限（杠杆2倍、反向-2倍）内每日调整杠杆倍数，以应对市场剧烈波动时的容量压力。新规同步强化信息披露要求，提供者须每日公布次日目标杠杆倍数，产品名称亦须反映灵活杠杆特点。"
  },
  {
    "id": "wscn:3777898",
    "domain": "股票",
    "title": "黄仁勋首推支持开源AI模型，奥特曼意外呼应，马斯克称所有涉及X系统的代码将开源",
    "url": "https://wallstreetcn.com/articles/3777898",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T20:01:16+00:00",
    "summary": "黄仁勋发布首条推文——英伟达等逾20家科技公司联署公开信支持开放权重AI模型。马斯克、微软CEO均公开表态支持。随后马斯克再次发帖称“下个月所有涉及X系统的代码都将开源并接受审计”。OpenAI和Anthropic未在信上署名，OpenAI CEO奥特曼表态称，希望美国在开源AI领域胜出，“乐见”黄仁勋在社交媒体上的表态。"
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
    "id": "hn:49028304",
    "domain": "金融",
    "title": "US announces double-digit tariffs on most of globe to replace expiring duties",
    "url": "https://finance.yahoo.com/economy/policy/article/trump-administration-announces-the-next-phase-of-global-tariffs-with-10-to-125-rates-on-much-of-the-globe-210032314.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-23T21:28:52+00:00",
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
    "id": "hn:48824532",
    "domain": "金融",
    "title": "SpaceX Shares Stumble in Nasdaq-100 Debut",
    "url": "https://www.wsj.com/finance/stocks/spacex-shares-stumble-in-nasdaq-100-debut-9ec10565",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-07T22:00:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48678979",
    "domain": "金融",
    "title": "Trump administration asks OpenAI to stagger release of new model",
    "url": "https://ca.finance.yahoo.com/news/trump-administration-asks-openai-stagger-204300837.html",
    "source": "fla",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-25T20:47:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:48852473",
    "domain": "金融",
    "title": "Meta is staring down $1.4T in lawsuit over teen mental health",
    "url": "https://finance.yahoo.com/technology/articles/meta-staring-down-1-4t-173432639.html",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-09T21:15:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:48767569",
    "domain": "金融",
    "title": "Trump Made $1B on Crypto Deals While His Fans Lost a Fortune",
    "url": "https://www.wsj.com/finance/currencies/trump-made-1-billion-on-crypto-deals-while-his-fans-lost-a-fortune-408754c9",
    "source": "doener",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-07-02T21:25:54+00:00",
    "summary": ""
  }
]
```
