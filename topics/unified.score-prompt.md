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

- 今日日期：`2026-06-11`
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
  "date": "2026-06-11",
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
    "points": 3043673,
    "published_at": "2026-01-15T03:56:12+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署"
  },
  {
    "id": "bvid:BV1NvRyBzEhq",
    "domain": "AI",
    "title": "全网最全！60分钟全面掌握Claude Code～【附完整文档】",
    "url": "http://www.bilibili.com/video/av116522328524431",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1088614,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1041733,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1onb6zwEkk",
    "domain": "AI",
    "title": "【Ai教程】100集（全）从零开始学illustrator软件基础 (Ai2025新手入门实用版)Ai2025零基础入门教程！！！",
    "url": "http://www.bilibili.com/video/av115025985412548",
    "source": "天才AI设计鲨",
    "platform": "bilibili",
    "points": 1021984,
    "published_at": "2025-08-14T11:00:00+00:00",
    "summary": "设计行业5年 是一名资深设计师~PS学习交流 （南极有什么→ 动物 群 ：211582457）\n你的三连是我最大的动力！！你的三连是我最大的动力！！你的三连是我最大的动力！！"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 835640,
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
    "points": 651378,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1ty4y1S7mC",
    "domain": "AI",
    "title": "VS Code 零基础教程 | 持续更新中",
    "url": "http://www.bilibili.com/video/av798033193",
    "source": "兔子不吃米饭",
    "platform": "bilibili",
    "points": 623648,
    "published_at": "2020-12-10T12:00:08+00:00",
    "summary": "不卖课，不广告。\n\nVS Code 基础教程，求点赞，求投币，求分享，求收藏。\n\n谢谢大家。"
  },
  {
    "id": "bvid:BV116w5zuEbo",
    "domain": "AI",
    "title": "黑马程序员零基础玩转Dify，5小时极速入门Agent开发，从Prompt到企业级项目实战，涵盖RAG+Text2SQL、电商客服+LOL助手全实战",
    "url": "http://www.bilibili.com/video/av116236176392460",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 539946,
    "published_at": "2026-03-16T02:40:47+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260316\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\n人工智能开发热门教程：\nAI大模型开发：BV1h1V"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 382885,
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
    "points": 369960,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 267768,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 231568,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1FuXpBcEuo",
    "domain": "AI",
    "title": "Comfyui工作流从零基础到精通（2026新手入门实用版comfyui教程）详细从零开始学习comfyui工作流搭建，全程干货无废话！AI绘画AI视频生成",
    "url": "http://www.bilibili.com/video/av116294712102434",
    "source": "ComfyUl官方教学",
    "platform": "bilibili",
    "points": 229906,
    "published_at": "2026-03-26T09:21:12+00:00",
    "summary": "视频中的整合包以及up整理的AI绘画全套籽料包敲【7】全部抱走哦～只求换大家的一个[热词系列_三连]\n大家不要白嫖啊(┯_┯)，一个小小的赞也可谢谢了"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中使用Claude Code agent并配置DeepSeek v4 model【闲谈】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸voov",
    "platform": "bilibili",
    "points": 218179,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "setting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, &quot;value&quot;: &quot;xxxx&"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 213349,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 174035,
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
    "points": 165881,
    "published_at": "2026-04-21T03:15:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料，领取方式：关注后 私信“ 1 ”就好！\n\n后面还会出【一口气学会AI漫剧 】【一口气学会AI Agent 】等系列！大家可以蹲蹲！"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 154573,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 147342,
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
    "points": 142122,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 141294,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "domain": "AI",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 133691,
    "published_at": "2026-01-11T15:43:58+00:00",
    "summary": "🚀开发者必看！Superpowers把专业工程团队方法论固化成Skills，让Claude Code告别越写越乱的困境：规格驱动+代码质量双重保障！AI编程新范式！头脑风暴+计划+执行一条龙自动化\n\n\n🚀🚀🚀 视频简介：\n🎬 本期视频详细演示了开源AI编程工作流系统Superpowers的完整使用方法，并通过开发一款iOS时间线笔记原生应用来实测其效果。\n🔧 核心内容：\nSuperpowers工作"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 127728,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 115198,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1P3XTYPEJm",
    "domain": "AI",
    "title": "MCP是怎么对接大模型的？抓取AI提示词，拆解MCP的底层原理",
    "url": "http://www.bilibili.com/video/av114177964246439",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 99455,
    "published_at": "2025-03-17T13:21:11+00:00",
    "summary": "MCP 简单来说是AI大模型的标准化工具箱。 可大模型是怎么知道工具箱里面有哪些工具，使用什么样的参数格式进行调用呢？ MCP与Function Call的关系是什么？ 是不是只有支持Function Call的模型才能使用MCP？ 在上期视频里，爬爬虾介绍了MCP的概念与基础使用，本期视频我们从大模型与提示词的角度再次探讨下MCP协议的底层原理。这次我使用Cloudflare AI Gatewa"
  },
  {
    "id": "bvid:BV1F7EQ6tE7i",
    "domain": "AI",
    "title": "「实测」怒砸800大洋！测试Claude“神话”Fable 5 模型，4个任务把额度干爆了...",
    "url": "http://www.bilibili.com/video/av116724108105054",
    "source": "神烦老狗",
    "platform": "bilibili",
    "points": 99084,
    "published_at": "2026-06-10T05:18:02+00:00",
    "summary": "个人博客:\nhttps://www.laogou717.com\n\n最低价解锁 GPT-5、Claude 、Midjourney、Runway、Netflix等会员服务:\nhttps://nf.video/RnmdW  优惠码:laogou"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 87314,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1xBrDB9E42",
    "domain": "AI",
    "title": "独立开发太累？Godot + Claude Code 搭建 AI 辅助工作流，效率直接起飞！ | 地块召唤师开发实战 #01",
    "url": "http://www.bilibili.com/video/av115911319100158",
    "source": "像素夹心饼干",
    "platform": "bilibili",
    "points": 62947,
    "published_at": "2026-01-18T03:25:00+00:00",
    "summary": "大家好，这里是饼干！🍪\n这是我的新坑——**《地块召唤师》**开发实战分享的第一期。\n很多朋友问独立开发如何提升效率？这期视频我不聊虚的，直接公开我从 0 到 1 搭建的 AI + Godot 高效工作流。\n从游戏引擎的选择，到 Claude Code、Copilot 等 AI 工具的实战配置，再到如何用“明确需求”的方法论（SMART原则+双钻模型）来驾驭 AI，让它不仅仅是写代码的工具，更成为"
  },
  {
    "id": "bvid:BV1XdFzz7Ei8",
    "domain": "AI",
    "title": "不写代码就能轻松开发应用？Cursor+Gemini 超强指挥官工作法！",
    "url": "http://www.bilibili.com/video/av116021511853604",
    "source": "PM刘搞定",
    "platform": "bilibili",
    "points": 56364,
    "published_at": "2026-02-06T03:17:18+00:00",
    "summary": "如何像传统互联网大厂一样指挥AI干活？本期视频通过一个“个人工作台”的实战项目，拆解了一套利用 LLM (Gemini) 辅助 Cursor 开发的高效工作流。\n\n核心内容：\n角色转换：你不是程序员，你是产品经理（PM）。\n文档驱动：如何用 AI 生成标准的产品文档 (PRD)、UI 文档和技术方案。\n避坑指南：如何防止 Cursor “手搓核弹”或开发中途“失忆”。\n\n实操流程：\nStep 1："
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 52931,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 51309,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1yXE963ERm",
    "domain": "AI",
    "title": "🚀Claude Fable 5将编程门槛被彻底击穿！史上最强大模型真正碾压GPT 5.5！全面实测：SVG动画、流体模拟、自动化APP测试，零基础也能开发项目",
    "url": "http://www.bilibili.com/video/av116724829525887",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 50096,
    "published_at": "2026-06-10T08:32:28+00:00",
    "summary": "视频简介：\nClaude Fable 5将编程门槛被彻底击穿！史上最强大模型真正碾压GPT 5.5！全面实测：SVG动画、流体模拟、自动化APP测试，这个模型对物理世界的理解太可怕了！零基础也能做出完美App\n\n本期视频详细演示了Anthropic最新发布的Claude Fable 5模型的全方位实测！\n\n测试内容包括：几维鸟vs渡渡鸟土星环赛车SVG动画、复合弓开弓放箭物理模拟、可交互黑洞渲染、"
  },
  {
    "id": "bvid:BV15sNiecEZc",
    "domain": "AI",
    "title": "五款AI聚合客户端，这次不用跑来跑去了",
    "url": "http://www.bilibili.com/video/av113983935747114",
    "source": "果核次元",
    "platform": "bilibili",
    "points": 41745,
    "published_at": "2025-02-11T07:01:27+00:00",
    "summary": "全网AI，一网打尽。只要你配置好，直接无敌"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 35110,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1HM7C6BEnF",
    "domain": "AI",
    "title": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！",
    "url": "http://www.bilibili.com/video/av116696929076767",
    "source": "AIAgent开发",
    "platform": "bilibili",
    "points": 29593,
    "published_at": "2026-06-05T10:11:18+00:00",
    "summary": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29632,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV17YPqzcES4",
    "domain": "AI",
    "title": "挑战用Cursor30分钟搭建完整小程序",
    "url": "http://www.bilibili.com/video/av116171517069277",
    "source": "前端老兵AI",
    "platform": "bilibili",
    "points": 29427,
    "published_at": "2026-03-05T12:00:00+00:00",
    "summary": "用AI写小程序，到底能有多快？ 我做了9年前端，小程序项目做了不下20个。今天我做一个实验——完全用Cursor从零搭建一个完整的待办清单 小程序，包含首页列表、新增编辑、分类筛选、本地存储，全程计时。"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27138,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV1HFDSBPE7b",
    "domain": "AI",
    "title": "3分钟教你部署ai我的世界陪玩！",
    "url": "http://www.bilibili.com/video/av116390124067729",
    "source": "我叫非主流_",
    "platform": "bilibili",
    "points": 25867,
    "published_at": "2026-04-12T11:45:00+00:00",
    "summary": "这是上期视频的教程，求求大家给个三连把="
  },
  {
    "id": "bvid:BV1woEJ6rEi5",
    "domain": "AI",
    "title": "翻遍整个B站，这绝对是2026讲的最好的AI Agent智能体教程，手把手教你从0基础开始搭建企业级Agent智能体，全程干货无废话，让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116703220535567",
    "source": "AI学习课堂",
    "platform": "bilibili",
    "points": 22573,
    "published_at": "2026-06-06T12:49:16+00:00",
    "summary": "【视频配套籽料,学习路线、系统学习，实战项目案例、电子书+问题解答问题解答请看”平论区置顶”自取哦】\n视频制作不易，如果视频对你有用的话请一键三连【长按点赞】支持一下up哦，拜托，这对我真的很重要！"
  },
  {
    "id": "bvid:BV1RUDsBWEHb",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的Cursor+Skills实战指南教程，手把手带你开发爆款app，全程干货无废话！比付费效果强十倍！",
    "url": "http://www.bilibili.com/video/av116373464350785",
    "source": "AI大模型技术教程",
    "platform": "bilibili",
    "points": 21644,
    "published_at": "2026-04-09T10:15:00+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\nCursor+Skills频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV1GLdABKEaR",
    "domain": "AI",
    "title": "【自用】Claude Code 驱动 Comsol 复现论文仿真",
    "url": "http://www.bilibili.com/video/av116534089482864",
    "source": "Ricardo_Tsang",
    "platform": "bilibili",
    "points": 20226,
    "published_at": "2026-05-07T16:10:32+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1mkRtBfED9",
    "domain": "AI",
    "title": "终于实现AI自动剪视频！Claudecode太强大了",
    "url": "http://www.bilibili.com/video/av116528183777029",
    "source": "大厂转型人强哥",
    "platform": "bilibili",
    "points": 20106,
    "published_at": "2026-05-06T14:54:06+00:00",
    "summary": "终于实现了 AI 自动化剪辑，分享下我的内容工作流。这条视频也是 Claudecode 给我剪辑的，14分钟视频2分钟剪辑完毕，正常实习生剪辑需要 90分钟"
  },
  {
    "id": "bvid:BV14aEo6pEdi",
    "domain": "AI",
    "title": "Claude Fable 5最强实测！我用它 5 小时做了个 macOS App，已开源！【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av116727111228188",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 19532,
    "published_at": "2026-06-11T00:05:00+00:00",
    "summary": "Claude 刚发布的 Fable 5，是目前最强的 agentic 编程模型。这期先聊它的特性、价格和基准表现，再演示我用它 5 小时做出的第一个 macOS 开源应用「翻箱」，还有顺手做的浏览器录屏、多平台发文两个小工具。限免到 6 月 22 日，建议抓紧体验。\n\n时间戳：\n00:00 Fable 5 发布\n01:41 模型特性与定价\n04:02 基准实测成绩\n08:15 Claude Cod"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 15552,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 14723,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1wuLHzDEGA",
    "domain": "AI",
    "title": "【Godot&amp;Cursor】0.亲测一个月后，我选择Godot+Cursor组合做独立游戏",
    "url": "http://www.bilibili.com/video/av114398869853632",
    "source": "破妄-胖",
    "platform": "bilibili",
    "points": 13593,
    "published_at": "2025-04-25T13:43:22+00:00",
    "summary": "飞书文档：https://sh67ozct1z.feishu.cn/docx/Hn5jd0cE6op1Sux9RrFcl8Npnbd"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 13010,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1rCJdzFEQg",
    "domain": "AI",
    "title": "让AI帮你干活：WindowsMCP安装和使用！",
    "url": "http://www.bilibili.com/video/av115242814212549",
    "source": "磊哥聊AI",
    "platform": "bilibili",
    "points": 11826,
    "published_at": "2025-09-22T00:00:00+00:00",
    "summary": "AI 自动操作你的电脑，解放双手，提升工作效率。"
  },
  {
    "id": "bvid:BV1hEVY6jEGT",
    "domain": "AI",
    "title": "最新【Claude pro Max】保姆级充值教程 Claude code国内购买教程 注册+订阅一个视频教会你",
    "url": "http://www.bilibili.com/video/av116657754277772",
    "source": "小轩AI-",
    "platform": "bilibili",
    "points": 11743,
    "published_at": "2026-05-29T12:07:14+00:00",
    "summary": "aipayok.com"
  },
  {
    "id": "hn:48377404",
    "domain": "AI 算力 / 半导体",
    "title": "Use your Nvidia GPU's VRAM as swap space on Linux",
    "url": "https://github.com/c0dejedi/nbd-vram",
    "source": "tanelpoder",
    "platform": "hackernews",
    "points": 471,
    "published_at": "2026-06-02T22:55:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48352939",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX Spark",
    "url": "https://www.nvidia.com/en-us/products/rtx-spark/",
    "source": "shenli3514",
    "platform": "hackernews",
    "points": 427,
    "published_at": "2026-06-01T05:24:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48424605",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is proposing a beast of a CPU system for Windows PCs",
    "url": "https://twitter.com/lemire/status/2062880075117113739",
    "source": "tosh",
    "platform": "hackernews",
    "points": 330,
    "published_at": "2026-06-06T12:52:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48355720",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft builds MacBook Pro rival with NVIDIA-powered Surface Laptop Ultra",
    "url": "https://www.windowslatest.com/2026/06/01/microsoft-builds-its-ultimate-macbook-pro-rival-with-the-nvidia-powered-surface-laptop-ultra/",
    "source": "jbk",
    "platform": "hackernews",
    "points": 286,
    "published_at": "2026-06-01T12:04:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:48356654",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Cosmos 3",
    "url": "https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 149,
    "published_at": "2026-06-01T13:32:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48444451",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia partners with LG robotics to build humanoid robots in South Korea",
    "url": "https://blogs.nvidia.com/blog/nvidia-and-lg-group-ai-factory/",
    "source": "spwa4",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-06-08T12:25:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:48356312",
    "domain": "AI 算力 / 半导体",
    "title": "Launch HN: Expanse (YC P26) – Unlock Wasted GPU Capacity",
    "url": "https://news.ycombinator.com/item?id=48356312",
    "source": "ismaeel_bashir",
    "platform": "hackernews",
    "points": 103,
    "published_at": "2026-06-01T13:05:02+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/startup-ricursive-to-create-an-end-to-end-ai-model-for-chip-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Startup Ricursive to Create an End-to-End AI Model for Chip Design",
    "url": "https://www.eetimes.com/startup-ricursive-to-create-an-end-to-end-ai-model-for-chip-design/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T16:26:51+00:00",
    "summary": "“We are definitely not an EDA company,” Ricursive co-founders told EE Times. The post Startup Ricursive to Create an End-to-End AI Model for Chip Design appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/massive-ai-storage-demand-creates-a-new-memory-wall/",
    "domain": "AI 算力 / 半导体",
    "title": "Massive AI Storage Demand Creates a New Memory Wall",
    "url": "https://www.eetimes.com/massive-ai-storage-demand-creates-a-new-memory-wall/",
    "source": "Alper Ilkbahar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T14:22:01+00:00",
    "summary": "As AI models scale to trillions of parameters, conventional memory architectures face mounting capacity and efficiency constraints. The post Massive AI Storage Demand Creates a New Memory Wall appeare"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-driven-memory-shortage-upends-it-budgets/",
    "domain": "AI 算力 / 半导体",
    "title": "AI-Driven Memory Shortage Upends IT Budgets",
    "url": "https://www.eetimes.com/ai-driven-memory-shortage-upends-it-budgets/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T07:47:11+00:00",
    "summary": "IT departments find that purchasing servers and computers has become much more difficult because of surging memory prices and shortages. The post AI-Driven Memory Shortage Upends IT Budgets appeared f"
  },
  {
    "id": "rss:https://www.eetimes.com/indias-2035-chip-ambitions-focus-on-targeted-design-manufacturing-leadership/",
    "domain": "AI 算力 / 半导体",
    "title": "India’s 2035 Chip Ambitions Focus on Targeted Design, Manufacturing Leadership",
    "url": "https://www.eetimes.com/indias-2035-chip-ambitions-focus-on-targeted-design-manufacturing-leadership/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T22:00:00+00:00",
    "summary": "India maps out a bold $150B chip strategy for 2035—see why this time might be different. The post India’s 2035 Chip Ambitions Focus on Targeted Design, Manufacturing Leadership appeared first on EE Ti"
  },
  {
    "id": "rss:https://www.eetimes.com/efinix-rethinking-the-logic-routing-tradeoff-in-fpgas/",
    "domain": "AI 算力 / 半导体",
    "title": "Rethinking the Logic-Routing Tradeoff in FPGAs",
    "url": "https://www.eetimes.com/efinix-rethinking-the-logic-routing-tradeoff-in-fpgas/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T17:00:00+00:00",
    "summary": "Efinix’ exchangeable logic-and-routing technology aims to cut power and die area while enabling memory integration and greater flexibility for AI edge designs. The post Rethinking the Logic-Routing Tr"
  },
  {
    "id": "rss:https://www.eetimes.com/the-concerning-unchecked-rise-of-e2e-ai-in-physical-applications/",
    "domain": "AI 算力 / 半导体",
    "title": "The Concerning, Unchecked Rise of E2E AI in Physical Applications",
    "url": "https://www.eetimes.com/the-concerning-unchecked-rise-of-e2e-ai-in-physical-applications/",
    "source": "Girish Mhatre",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T13:24:48+00:00",
    "summary": "Don’t let the bodies pile up The post The Concerning, Unchecked Rise of E2E AI in Physical Applications appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/xensiv-tmr-based-sensors-unlocking-new-possibilities-in-magnetic-sensing/",
    "domain": "AI 算力 / 半导体",
    "title": "XENSIV™ TMR-based Sensors: Unlocking New Possibilities in Magnetic Sensing",
    "url": "https://www.eetimes.com/xensiv-tmr-based-sensors-unlocking-new-possibilities-in-magnetic-sensing/",
    "source": "Marc Biehn, Head of Product Group Industrial Consumer Magnetic Sensing; Sebastian Maerz, Business Developer Magnetic Sensing, Infineon Technologies AG",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T13:00:00+00:00",
    "summary": "Explore how Infineon's TMR-based XENSIV™ sensors deliver high-sensitivity, low-noise magnetic sensing for position, current, and overcurrent protection. The post XENSIV™ TMR-based Sensors: Unlocking N"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/chipsets/intels-upcoming-z790-and-z990-flagship-chipsets-will-reportedly-consume-up-to-14w-at-peak-load-courtesy-of-more-pcie-5-0-support-nova-lake-motherboards-may-feature-a-22-percent-smaller-pch-than-z890",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's upcoming Z970 and Z990 flagship chipsets will reportedly consume up to 14W at peak load, courtesy of more PCIe 5.0 support — Nova Lake motherboards may feature a 22% smaller PCH than Z890",
    "url": "https://www.tomshardware.com/pc-components/chipsets/intels-upcoming-z790-and-z990-flagship-chipsets-will-reportedly-consume-up-to-14w-at-peak-load-courtesy-of-more-pcie-5-0-support-nova-lake-motherboards-may-feature-a-22-percent-smaller-pch-than-z890",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T16:35:19+00:00",
    "summary": "The Z990 PCH for Nova Lake motherboards is apparently 22% smaller than Z890, despite featuring a higher power maximum power draw of up to 14W. The leaked picture of the PCH shows a 11.15 x 6.5mm die a"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-fires-back-at-nvidia-claiming-256-core-zen-6-venice-cpu-beats-vera-by-3-3x-in-rack-level-performance-company-shares-first-estimated-epyc-venice-benchmarks",
    "domain": "AI 算力 / 半导体",
    "title": "AMD fires back at Nvidia, claiming 256-core Zen 6 'Venice' CPU beats Vera by 3.3x in rack-level performance — company shares first estimated EPYC Venice benchmarks",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-fires-back-at-nvidia-claiming-256-core-zen-6-venice-cpu-beats-vera-by-3-3x-in-rack-level-performance-company-shares-first-estimated-epyc-venice-benchmarks",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T16:00:29+00:00",
    "summary": "AMD has shared the first official results for its 256-core EPYC Venice CPU, saying it beats Nvidia's Vera by 3.3x in a rack-level deployment."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/google-reportedly-books-intel-for-more-than-3-million-tpus-in-2028",
    "domain": "AI 算力 / 半导体",
    "title": "Google reportedly books Intel for packaging more than 3 million TPUs in 2028 — SK hynix is testing Intel's EMIB packaging for HBM integration",
    "url": "https://www.tomshardware.com/tech-industry/google-reportedly-books-intel-for-more-than-3-million-tpus-in-2028",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T15:49:41+00:00",
    "summary": "Google has placed an order for Intel to build more than 3 million of its TPUs in 2028 after months of testing Intel's advanced packaging."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/samsung-heavy-industries-recruits-greek-shipowner-and-supermicro-to-bring-50mw-floating-ai-data-centers-to-market",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung Heavy Industries recruits Greek shipowner and Supermicro to bring 50MW floating AI data centers to market — can be powered by solid oxide fuel cells running on liquefied natural gas",
    "url": "https://www.tomshardware.com/tech-industry/samsung-heavy-industries-recruits-greek-shipowner-and-supermicro-to-bring-50mw-floating-ai-data-centers-to-market",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T14:42:30+00:00",
    "summary": "Besides Samsung Heavy, Japan’s MOL is also building a 73 MW floating data center with Karpowership for a 2027 deployment."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/valve-to-discontinue-physical-steam-gift-cards-by-the-end-of-2026-due-to-scammers-says-nefarious-actors-continue-to-exploit-them-despite-years-of-restrictions",
    "domain": "AI 算力 / 半导体",
    "title": "Valve to discontinue physical Steam gift cards by the end of 2026 due to scammers — says nefarious actors continue to exploit them despite years of restrictions",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/valve-to-discontinue-physical-steam-gift-cards-by-the-end-of-2026-due-to-scammers-says-nefarious-actors-continue-to-exploit-them-despite-years-of-restrictions",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T13:20:50+00:00",
    "summary": "Physical Steam gift cards will no longer be restocked at retail stores, though digital gifting options and existing cards will remain supported."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/overenthusiastic-gta-6-fan-claims-to-be-monitoring-oxygen-levels-acoustic-noise-from-the-bushes-at-rockstar-north-hq-promises-trailer-3-launch-is-imminent-based-on-heightened-activity",
    "domain": "AI 算力 / 半导体",
    "title": "Overenthusiastic GTA 6 fan claims to be monitoring oxygen levels, acoustic noise from the bushes at Rockstar North HQ — promises trailer 3 launch is imminent based on heightened activity",
    "url": "https://www.tomshardware.com/video-games/console-gaming/overenthusiastic-gta-6-fan-claims-to-be-monitoring-oxygen-levels-acoustic-noise-from-the-bushes-at-rockstar-north-hq-promises-trailer-3-launch-is-imminent-based-on-heightened-activity",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T12:11:06+00:00",
    "summary": "Either a dedicated jokester or a deranged fan has been posting advanced surveillance on Reddit in an attempt to predict the next GTA 6 trailer."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/analyzing-tsmcs-fab-expansion-roadmap-multi-fab-n2-ramp-cowos-soic-and-uncorking-bottlenecks",
    "domain": "AI 算力 / 半导体",
    "title": "Analyzing TSMC's fab expansion roadmap — multi-fab N2 ramp, CoWoS, SoIC, and uncorking bottlenecks",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/analyzing-tsmcs-fab-expansion-roadmap-multi-fab-n2-ramp-cowos-soic-and-uncorking-bottlenecks",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T11:41:11+00:00",
    "summary": "TSMC is executing the largest manufacturing expansion in semiconductor industry history that combines simultaneous multi-fab N2 ramps, AI-driven manufacturing optimizations, and massive CoWoS/SoIC pac"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/grab-an-usd800-saving-on-this-rtx-5070-ti-gaming-laptop-from-hp-with-customizable-specs-and-a-20-core-cpu-base-model-costs-just-usd1-999-for-16-inch-rig-with-16gb-ddr5-with-oled-costing-just-usd60-extra",
    "domain": "AI 算力 / 半导体",
    "title": "Grab an $800 saving on this RTX 5070 Ti gaming laptop from HP with customizable specs and a 20-core CPU — base model costs just $1,999 for 16-inch rig with 16GB DDR5, with OLED costing just $60 extra",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/grab-an-usd800-saving-on-this-rtx-5070-ti-gaming-laptop-from-hp-with-customizable-specs-and-a-20-core-cpu-base-model-costs-just-usd1-999-for-16-inch-rig-with-16gb-ddr5-with-oled-costing-just-usd60-extra",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T11:30:01+00:00",
    "summary": "Save $800 on this customizable RTX 5070 Ti HP Omen Max 16 gaming laptop with 16GB DDR5, 1TB SSD, and a 16-inch display."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/gigabytes-sensational-rtx-5070-ti-aorus-prime-5-gaming-pc-has-had-usd500-slashed-off-the-list-price-at-walmart-32gb-of-ddr5-ram-and-2tb-of-storage-for-just-usd1-999",
    "domain": "AI 算力 / 半导体",
    "title": "Gigabyte's sensational RTX 5070 Ti Aorus Prime 5 gaming PC has had $500 slashed off the list price at Walmart — 32GB of DDR5 RAM, and 2TB of storage for just $1,999",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/gigabytes-sensational-rtx-5070-ti-aorus-prime-5-gaming-pc-has-had-usd500-slashed-off-the-list-price-at-walmart-32gb-of-ddr5-ram-and-2tb-of-storage-for-just-usd1-999",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T11:09:29+00:00",
    "summary": "A powerful gaming desktop with a 16GB RTX 5070 Ti GPU at its heart, discounted by a massive $500 at Walmart right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/china-drafts-295-billion-plan-to-build-a-national-ai-data-center-grid-running-on-80-percent-domestic-chips",
    "domain": "AI 算力 / 半导体",
    "title": "China drafts $295 billion plan to build national AI data center grid running on 80% homemade silicon — projected 2028 timeline could run into limits of local chip production",
    "url": "https://www.tomshardware.com/tech-industry/china-drafts-295-billion-plan-to-build-a-national-ai-data-center-grid-running-on-80-percent-domestic-chips",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T10:00:00+00:00",
    "summary": "China is drafting a plan to spend roughly 2 trillion yuan over five years on a nationwide grid of AI data centers."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/3d-printed-triaxial-electrospray-nozzles-could-revolutionize-drug-and-self-healing-material-manufacturing-mit-developed-technique-makes-cleanroom-fabrication-optional",
    "domain": "AI 算力 / 半导体",
    "title": "3D-printed nozzles could revolutionize drug and self-healing material manufacturing — MIT-developed triaxial electrospray design makes cleanroom fabrication optional",
    "url": "https://www.tomshardware.com/3d-printing/3d-printed-triaxial-electrospray-nozzles-could-revolutionize-drug-and-self-healing-material-manufacturing-mit-developed-technique-makes-cleanroom-fabrication-optional",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T09:30:00+00:00",
    "summary": "MIT's 3D-printed triaxial electrospray nozzles could revolutionize drug and self-healing material manufacturing. By using a relatively inexpensive resin printing approach, the new nozzle fabrication t"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-fable-5-brings-mythos-to-the-masses-anthropics-next-frontier-model-is-state-of-the-art-on-nearly-all-tested-benchmarks",
    "domain": "AI 算力 / 半导体",
    "title": "Claude Fable 5 brings Mythos to the masses — Anthropic's new frontier model is 'state-of-the-art on nearly all tested benchmarks'",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-fable-5-brings-mythos-to-the-masses-anthropics-next-frontier-model-is-state-of-the-art-on-nearly-all-tested-benchmarks",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T20:34:10+00:00",
    "summary": "After first announcing its scarily capable Mythos Preview model back in April, Anthropic is releasing a public version of Mythos, called Fable 5, that it says is \"safe for general use.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/microphones/razer-seiren-v3-pro-review",
    "domain": "AI 算力 / 半导体",
    "title": "Razer Seiren V3 Pro Review: USB, XLR, and 32-bit float",
    "url": "https://www.tomshardware.com/peripherals/microphones/razer-seiren-v3-pro-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T17:45:00+00:00",
    "summary": "Razer's new Seiren V3 Pro is an end-address mic with both USB-C and XLR connectivity, and it also supports 32-bit float."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-warns-ai-self-improvement-could-end-in-lost-human-control",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic's warning over AI self-improvement has a hidden message — accelerating development requires more compute before companies ever risk losing control of frontier AI models",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-warns-ai-self-improvement-could-end-in-lost-human-control",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T17:03:06+00:00",
    "summary": "The company that just a few weeks ago told us that its Mythos model was much too powerful to be released is now saying that we might need to hit the pause button."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-chairs/secretlab-atlas-review",
    "domain": "AI 算力 / 半导体",
    "title": "Secretlab Atlas review: The one you’ve been waiting for",
    "url": "https://www.tomshardware.com/peripherals/gaming-chairs/secretlab-atlas-review",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T17:00:00+00:00",
    "summary": "Secretlab has unveiled its new Atlas task chair with an emphasis on productivity."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/taiwan-weighs-criminal-ban-on-ai-chip-exports-to-all-of-china-as-us-trade-talks-continue",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan weighs criminal ban on AI chip exports to all of China — stricter measures beyond blacklisted firms would make smuggling servers a crime",
    "url": "https://www.tomshardware.com/tech-industry/taiwan-weighs-criminal-ban-on-ai-chip-exports-to-all-of-china-as-us-trade-talks-continue",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T15:53:39+00:00",
    "summary": "Taiwan is considering far stricter export controls that would restrict AI chip sales to every customer in China."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/spacex-details-its-ai1-compute-satellite",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk's first-gen orbital data center craft spans wider than a Boeing 747 and runs an interchangeable chip payload — AI1 satellite compute payload is 120 kW, peaks at 150 kW",
    "url": "https://www.tomshardware.com/tech-industry/spacex-details-its-ai1-compute-satellite",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T15:30:00+00:00",
    "summary": "Elon Musk laid out the first detailed design of SpaceX's AI1 satellite in a 30-minute video posted to the company's X account."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/hvac-tech-finds-former-amd-ceo-rory-reads-pc-in-a-customers-basement-signed-by-lisa-su-unused-2014-desktop-had-bulldozer-era-hardware-inside-and-a-wrapped-windows-8-1-cd",
    "domain": "AI 算力 / 半导体",
    "title": "HVAC tech finds former AMD CEO Rory Read's PC in a customer's basement, signed by Lisa Su — unused 2014 desktop had Bulldozer-era hardware inside and a wrapped Windows 8.1 CD",
    "url": "https://www.tomshardware.com/desktops/pc-building/hvac-tech-finds-former-amd-ceo-rory-reads-pc-in-a-customers-basement-signed-by-lisa-su-unused-2014-desktop-had-bulldozer-era-hardware-inside-and-a-wrapped-windows-8-1-cd",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T15:12:27+00:00",
    "summary": "Someone on Reddit has stumbled upon former AMD CEO Rory Read's PC that might've been given to him as a parting gift. Read was AMD's CEO between 2011 and 2014. He helped AMD navigate the failure of Bul"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/spacex-unveils-11-million-square-foot-gigasat-factory-a-new-manufacturing-facility-for-space-based-data-centers-aims-for-1-gw-year-of-space-ai-compute-by-late-2027-from-its-satellites",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceX unveils 11-million-square-foot Gigasat factory, a new manufacturing facility for space-based data centers — aims for 1 GW/year of space AI compute by late 2027 from its satellites",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/spacex-unveils-11-million-square-foot-gigasat-factory-a-new-manufacturing-facility-for-space-based-data-centers-aims-for-1-gw-year-of-space-ai-compute-by-late-2027-from-its-satellites",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T14:38:59+00:00",
    "summary": "SpaceX's new Gigasat factory will mass-produce AI satellites for orbital data centers. Musk says the company is targeting 1 GW of space AI compute by 2027 and 100 GW per year by 2030."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/startups-miracle-solid-state-battery-actually-uses-lithium-ion-chemistry-according-to-third-party-tests-donut-lab-raised-usd25m-and-is-valued-at-usd1-25b-on-what-now-appear-to-be-debunked-claims",
    "domain": "AI 算力 / 半导体",
    "title": "Startup’s ‘miracle’ solid-state battery actually uses lithium-ion chemistry, according to third-party tests — Donut Lab raised $25M and is valued at $1.25B on what now appear to be debunked claims",
    "url": "https://www.tomshardware.com/tech-industry/startups-miracle-solid-state-battery-actually-uses-lithium-ion-chemistry-according-to-third-party-tests-donut-lab-raised-usd25m-and-is-valued-at-usd1-25b-on-what-now-appear-to-be-debunked-claims",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T12:26:43+00:00",
    "summary": "A Finnish startup’s startling claims to have a production-ready ‘miracle’ solid-state battery have thoroughly collapsed under independent scrutiny."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/grab-a-huge-usd550-saving-on-this-4k-ready-gaming-pc-with-an-rtx-5070-and-7800x3d-right-now-just-usd1-449-for-this-liquid-cooled-ibuypower-rig-with-16gb-ddr5-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a huge $550 saving on this 4K-ready gaming PC with an RTX 5070 and 7800X3D right now — just $1,449 for this liquid-cooled iBuyPower rig with 16GB DDR5 and a 1TB SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/grab-a-huge-usd550-saving-on-this-4k-ready-gaming-pc-with-an-rtx-5070-and-7800x3d-right-now-just-usd1-449-for-this-liquid-cooled-ibuypower-rig-with-16gb-ddr5-and-a-1tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T11:12:15+00:00",
    "summary": "Save $550 on this AMD pre-built from iBuyPower, featuring an AMD Ryzen 7 7800X3D, RTX 5070, 16GB of DDR5 RAM, and a 1TB SSD, all for just $1,449 right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amds-radeon-rx-9070-xt-graphics-card-drops-to-just-usd649-gigabytes-16gb-gaming-oc-gpu-is-usd90-cheaper-in-todays-amazon-deal",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's Radeon RX 9070 XT graphics card drops to just $649 — Gigabyte's 16GB Gaming OC GPU is $90 cheaper in today's Amazon deal",
    "url": "https://www.tomshardware.com/pc-components/gpus/amds-radeon-rx-9070-xt-graphics-card-drops-to-just-usd649-gigabytes-16gb-gaming-oc-gpu-is-usd90-cheaper-in-todays-amazon-deal",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T10:58:44+00:00",
    "summary": "Gigabyte's Gaming OC Radeon RX 9070 XT is now just $649 in today's Amazon deal."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/servers/nashville-zoo-pushes-back-on-1-6-acre-data-center-build-near-animal-habitats-zoo-says-it-planned-to-use-lot-for-education-and-conservation-center",
    "domain": "AI 算力 / 半导体",
    "title": "Nashville Zoo pushes back on 1.6-acre data center build near animal habitats — Zoo says it planned to use lot for education and conservation center",
    "url": "https://www.tomshardware.com/desktops/servers/nashville-zoo-pushes-back-on-1-6-acre-data-center-build-near-animal-habitats-zoo-says-it-planned-to-use-lot-for-education-and-conservation-center",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T10:00:00+00:00",
    "summary": "The Nashville Zoo is pushing back on a proposed data center build, which would place servers in proximity with animal habitats."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/linux-developers-are-using-ai-vibe-coding-to-keep-vintage-amd-gpus-alive-r600-driver-cleaned-up-with-github-copilot-gives-hd-2000-to-hd-6000-series-a-new-lease-of-life",
    "domain": "AI 算力 / 半导体",
    "title": "Linux developers are using AI vibe coding to keep vintage AMD GPUs alive — R600 driver cleaned up with GitHub Copilot gives HD 2000 to HD 6000 series a new lease of life",
    "url": "https://www.tomshardware.com/software/linux/linux-developers-are-using-ai-vibe-coding-to-keep-vintage-amd-gpus-alive-r600-driver-cleaned-up-with-github-copilot-gives-hd-2000-to-hd-6000-series-a-new-lease-of-life",
    "source": "Aaron Klotz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T09:40:06+00:00",
    "summary": "Linux developer uses AI to help update Linux GPU driver support for vintage HD 2000 - HD 6000 series."
  },
  {
    "id": "hn:48234574",
    "domain": "AI 算力 / 半导体",
    "title": "How do you build a semiconductor company on something that's free?",
    "url": "https://www.siliconimist.com/p/the-open-source-silicon-business",
    "source": "johncole",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-05-22T11:49:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:48431367",
    "domain": "AI 算力 / 半导体",
    "title": "The Russian who invented semiconductors 25 years before the USA",
    "url": "https://www.semidoped.com/p/til-the-man-who-invented-the-future",
    "source": "johncole",
    "platform": "hackernews",
    "points": 53,
    "published_at": "2026-06-07T03:00:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48439316",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei executive credits bans for accelerating domestic chip independence",
    "url": "https://www.techradar.com/pro/huaweis-chairman-officially-thanks-the-us-government-for-enabling-chinas-semiconductor-industry-chain-to-truly-grow",
    "source": "yogthos",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-06-07T22:38:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48220446",
    "domain": "AI 算力 / 半导体",
    "title": "IBM invented semiconductor manufacturing automation",
    "url": "https://spectrum.ieee.org/semiconductor-fabrication",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-05-21T10:39:48+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/as-chips-go-vertical-metrology-struggles-to-keep-up/",
    "domain": "AI 算力 / 半导体",
    "title": "As Chips Go Vertical, Metrology Struggles to Keep Up",
    "url": "https://www.eetimes.com/as-chips-go-vertical-metrology-struggles-to-keep-up/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T07:00:00+00:00",
    "summary": "Chip technology dives deeper into the Z-axis, pushing metrology to innovate or risk becoming a bottleneck. The post As Chips Go Vertical, Metrology Struggles to Keep Up appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/risc-v-summit-europe-2026-industry-and-academia-unite-in-bologna-to-advance-open-hardware/",
    "domain": "AI 算力 / 半导体",
    "title": "RISC-V Summit Europe 2026: Industry and Academia Unite in Bologna to Advance Open Hardware",
    "url": "https://www.eetimes.com/risc-v-summit-europe-2026-industry-and-academia-unite-in-bologna-to-advance-open-hardware/",
    "source": "RISC-V Summit",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T16:10:19+00:00",
    "summary": "RISC-V Summit Europe is coming to Bologna, Italy, with a program that reflects just how far the ecosystem has come since we gathered in Paris a year ago. Taking place June 8–12 2026 at the Palazzo dei"
  },
  {
    "id": "rss:https://www.eetimes.com/chips-act-2-0-inside-europes-semiconductor-rethink/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside Europe’s Chip Rethink: Why Fabs Weren’t Enough and Why Spain Matters",
    "url": "https://www.eetimes.com/chips-act-2-0-inside-europes-semiconductor-rethink/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T12:00:00+00:00",
    "summary": "Spain is emerging as a more influential player in Europe’s next chip debate—through design startups, photonics, quantum technologies, and a growing talent base. The post Inside Europe’s Chip Rethink: "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/levelplay-shows-off-magnetically-attached-fans-that-are-reversible-connect-via-pogo-pins-and-usb-c-plus-an-aio-that-trades-a-screen-for-a-big-knob",
    "domain": "AI 算力 / 半导体",
    "title": "Levelplay shows off magnetically attached fans that are reversible, connect via pogo pins and USB-C – plus an AIO that trades a screen for a big knob",
    "url": "https://www.tomshardware.com/pc-components/cooling/levelplay-shows-off-magnetically-attached-fans-that-are-reversible-connect-via-pogo-pins-and-usb-c-plus-an-aio-that-trades-a-screen-for-a-big-knob",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T19:32:35+00:00",
    "summary": "Levelplay took to Computex with some interesting cooling concepts, like magnetic fans that can be reversed in seconds, and an AIO that puts a big tactile knob for fan control on top of your CPU."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/chinese-startup-claims-photonic-chip-production-without-duv-lithography-says-nanoimprint-process-cuts-costs-by-90-percent-8-inch-wafers-produced-without-conventional-optical-lithography",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese startup claims photonic chip production without DUV lithography, says nanoimprint process cuts costs by 90% — 8-inch wafers produced without conventional optical lithography",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/chinese-startup-claims-photonic-chip-production-without-duv-lithography-says-nanoimprint-process-cuts-costs-by-90-percent-8-inch-wafers-produced-without-conventional-optical-lithography",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T18:54:45+00:00",
    "summary": "Chinese startup Prinano claims it produced 8-inch photonic chip wafers without DUV lithography, using nanoimprint technology that cuts costs by 90%."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/macos/apple-demonstrates-cross-platform-siri-upgrades-in-macos-27-golden-gate-at-wwdc-update-brings-liquid-glass-improvements-and-unifies-ai-strategy",
    "domain": "AI 算力 / 半导体",
    "title": "Apple demonstrates cross-platform Siri upgrades in macOS 27 Golden Gate at WWDC — update brings Liquid Glass improvements and unifies AI strategy",
    "url": "https://www.tomshardware.com/software/macos/apple-demonstrates-cross-platform-siri-upgrades-in-macos-27-golden-gate-at-wwdc-update-brings-liquid-glass-improvements-and-unifies-ai-strategy",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T18:40:17+00:00",
    "summary": "At WWDC, Apple revealed its upcoming macOS update, macOS 27 Golden Gate, with a more refined Liquid Glass design and cross-platform Siri and Apple Intelligence features."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-expands-new-game-boosting-ibot-software-with-seven-more-games-up-to-a-27-percent-improvement-team-blue-claims-12-percent-average-jump-in-newly-supported-titles",
    "domain": "AI 算力 / 半导体",
    "title": "Intel expands new game-boosting iBOT software with seven more games, up to a 27% improvement — Team Blue claims 12% average jump in newly-supported titles",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-expands-new-game-boosting-ibot-software-with-seven-more-games-up-to-a-27-percent-improvement-team-blue-claims-12-percent-average-jump-in-newly-supported-titles",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T17:49:06+00:00",
    "summary": "Intel is expanding its performance-boosting iBOT feature with seven new games."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/most-new-us-ai-data-centers-are-going-up-on-drought-land",
    "domain": "AI 算力 / 半导体",
    "title": "Most new U.S. AI data centers are being built in drought zones — two-thirds of 809 planned projects set for areas with water shortages",
    "url": "https://www.tomshardware.com/tech-industry/most-new-us-ai-data-centers-are-going-up-on-drought-land",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-08T16:39:27+00:00",
    "summary": "About two-thirds of the 809 data centers planned across the U.S. are slated for land that has been in drought over the past year."
  },
  {
    "id": "hn:48196570",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.5 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/",
    "source": "spectraldrift",
    "platform": "hackernews",
    "points": 962,
    "published_at": "2026-05-19T17:43:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48450142",
    "domain": "大厂 AI 动态",
    "title": "Apple reveals new AI architecture built around Google Gemini models",
    "url": "https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/",
    "source": "unclefuzzy",
    "platform": "hackernews",
    "points": 730,
    "published_at": "2026-06-08T19:14:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:48111896",
    "domain": "大厂 AI 动态",
    "title": "Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model",
    "url": "https://github.com/cactus-compute/needle",
    "source": "HenryNdubuaku",
    "platform": "hackernews",
    "points": 776,
    "published_at": "2026-05-12T18:03:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48449084",
    "domain": "大厂 AI 动态",
    "title": "Siri AI",
    "url": "https://www.apple.com/apple-intelligence/",
    "source": "0xedb",
    "platform": "hackernews",
    "points": 671,
    "published_at": "2026-06-08T18:17:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:48192224",
    "domain": "大厂 AI 动态",
    "title": "Apple unveils new accessibility features",
    "url": "https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/",
    "source": "interpol_p",
    "platform": "hackernews",
    "points": 726,
    "published_at": "2026-05-19T12:04:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48233563",
    "domain": "大厂 AI 动态",
    "title": "Steve Wozniak cheered after telling students they have AI – actual intelligence",
    "url": "https://www.businessinsider.com/steve-wozniak-apple-ai-graduation-speech-2026-5",
    "source": "signa11",
    "platform": "hackernews",
    "points": 650,
    "published_at": "2026-05-22T09:04:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48196867",
    "domain": "大厂 AI 动态",
    "title": "Gemini CLI will stop working from June 18, 2026",
    "url": "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/",
    "source": "primaprashant",
    "platform": "hackernews",
    "points": 406,
    "published_at": "2026-05-19T18:03:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48196609",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni",
    "url": "https://deepmind.google/models/gemini-omni/",
    "source": "meetpateltech",
    "platform": "hackernews",
    "points": 323,
    "published_at": "2026-05-19T17:46:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48272354",
    "domain": "大厂 AI 动态",
    "title": "Microsoft Copilot Cowork Exfiltrates Files",
    "url": "https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files",
    "source": "Kneenex",
    "platform": "hackernews",
    "points": 264,
    "published_at": "2026-05-25T21:45:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:48111581",
    "domain": "大厂 AI 动态",
    "title": "Reimagining the mouse pointer for the AI era",
    "url": "https://deepmind.google/blog/ai-pointer/",
    "source": "devhouse",
    "platform": "hackernews",
    "points": 252,
    "published_at": "2026-05-12T17:40:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48297467",
    "domain": "大厂 AI 动态",
    "title": "Gemini, Gophers, and Fingers. Oh My Alternative Internets Beyond HTTPS",
    "url": "https://brennan.day/gemini-gophers-and-fingers-oh-my-alternative-internets-beyond-https/",
    "source": "ChrisArchitect",
    "platform": "hackernews",
    "points": 147,
    "published_at": "2026-05-27T17:24:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48373764",
    "domain": "大厂 AI 动态",
    "title": "GitHub Copilot App",
    "url": "https://github.com/features/preview/github-app",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 124,
    "published_at": "2026-06-02T17:58:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48475307",
    "domain": "大厂 AI 动态",
    "title": "Google Gemini Is Down",
    "url": "https://www.techradar.com/news/live/gemini-down-june-2026",
    "source": "axsaucedo",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-06-10T12:28:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48413924",
    "domain": "大厂 AI 动态",
    "title": "Leak Reveals Microsoft Wants Its AI to Be 'Addictive'",
    "url": "https://kotaku.com/microsoft-ai-scout-addictive-satya-nadella-404-media-copilot-2000702924",
    "source": "thm",
    "platform": "hackernews",
    "points": 67,
    "published_at": "2026-06-05T15:32:58+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/948153/deezer-ai-music-detector-spotify-apple",
    "domain": "大厂 AI 动态",
    "title": "Deezer launches an AI music detector for other streaming services",
    "url": "https://www.theverge.com/ai-artificial-intelligence/948153/deezer-ai-music-detector-spotify-apple",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T08:00:00+00:00",
    "summary": "Deezer will now scan your playlists on other streaming platforms to detect AI-generated music. Deezer was the first of the big streaming services to start labeling AI-generated music. It even offered "
  },
  {
    "id": "rss:https://www.theverge.com/tech/948215/bluesky-communities-at-protocol-atmosphere-reddit",
    "domain": "大厂 AI 动态",
    "title": "Bluesky is getting ‘communities’",
    "url": "https://www.theverge.com/tech/948215/bluesky-communities-at-protocol-atmosphere-reddit",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T00:05:48+00:00",
    "summary": "Bluesky will be getting \"communities,\" which will function as smaller spaces where you can \"go deeper and hang out with people who care about the same stuff\" sometime this year, according to head of p"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/948044/framework-laptop-13-pro-delay-shipment-july-august",
    "domain": "大厂 AI 动态",
    "title": "Framework delays its first Laptop 13 Pro shipments by a month",
    "url": "https://www.theverge.com/gadgets/948044/framework-laptop-13-pro-delay-shipment-july-august",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T23:12:51+00:00",
    "summary": "The Framework Laptop 13 Pro is delayed. The new 13-inch Framework flagship was set to launch in June, but shipments from the first batch are now expected in July - and there's still a chance some ship"
  },
  {
    "id": "rss:https://www.theverge.com/tech/948155/apple-siri-ai-chatbot-personality",
    "domain": "大厂 AI 动态",
    "title": "Apple’s new Siri AI knows when to shut up",
    "url": "https://www.theverge.com/tech/948155/apple-siri-ai-chatbot-personality",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T22:52:17+00:00",
    "summary": "Apple's new Siri AI is finally here, and so far, it seems like it works. I have access and have been messing around with it, and my biggest impression so far is that Siri AI is quite curt - which I me"
  },
  {
    "id": "rss:https://www.theverge.com/tech/947157/passports-data-breach-cannabis-club-systems-nefos-puffpal",
    "domain": "大厂 AI 动态",
    "title": "Nearly a million passports and photo IDs were left unprotected on the public internet",
    "url": "https://www.theverge.com/tech/947157/passports-data-breach-cannabis-club-systems-nefos-puffpal",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T21:55:00+00:00",
    "summary": "Typing a few letters and numbers into my web browser, I find myself gaping at the identity documents of complete strangers. The passport of a young woman from Germany. The passport of a man from Spain"
  },
  {
    "id": "rss:https://www.theverge.com/games/948142/microsoft-xbox-layoffs-reset-asha-sharma",
    "domain": "大厂 AI 动态",
    "title": "Xbox warns of a &#8216;reset&#8217; as it prepares for layoffs",
    "url": "https://www.theverge.com/games/948142/microsoft-xbox-layoffs-reset-asha-sharma",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T21:28:53+00:00",
    "summary": "Microsoft's Xbox division will be hit with significant layoffs next month, according to people familiar with Microsoft's plans. The company has been preparing for the layoffs internally for weeks, wit"
  },
  {
    "id": "rss:https://www.theverge.com/tech/947888/apple-google-add-support-for-thread-1-4",
    "domain": "大厂 AI 动态",
    "title": "Apple, Google add support for Thread 1.4",
    "url": "https://www.theverge.com/tech/947888/apple-google-add-support-for-thread-1-4",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T20:25:46+00:00",
    "summary": "Apple and Google are updating their smart home streaming devices to Thread 1.4. As first spotted by Matter Alpha and 9to5 Google, the latest spec has arrived on compatible Apple TVs in the tvOS 27 dev"
  },
  {
    "id": "rss:https://www.theverge.com/business/948083/kalshi-prediction-markets-insider-trading",
    "domain": "大厂 AI 动态",
    "title": "Kalshi adds required employment verification for some prediction market bets",
    "url": "https://www.theverge.com/business/948083/kalshi-prediction-markets-insider-trading",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T20:18:16+00:00",
    "summary": "The CFTC is considering its first regulation for prediction markets, as arrests over \"insider trading\" on everything from military operations to Google Search data continue to stack up. As CoinDesk re"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/947973/fable-wont-answer-basic-biology-questions",
    "domain": "大厂 AI 动态",
    "title": "Claude Fable won’t answer basic biology questions",
    "url": "https://www.theverge.com/ai-artificial-intelligence/947973/fable-wont-answer-basic-biology-questions",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T18:43:34+00:00",
    "summary": "Anthropic just released Claude Fable 5, calling it the most powerful AI model it has ever made widely available and praising its skills in biology, among others. But the model won't answer basic biolo"
  },
  {
    "id": "rss:https://www.theverge.com/news/947831/college-speakers-booed-ai-microsoft",
    "domain": "大厂 AI 动态",
    "title": "Microsoft, like, totally gets why students are booing AI-pilled graduation speakers",
    "url": "https://www.theverge.com/news/947831/college-speakers-booed-ai-microsoft",
    "source": "Mia Sato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T17:45:11+00:00",
    "summary": "New college graduates around the country have been booing and heckling commencement speakers who hype up AI. Microsoft would like everyone to talk it out. In a blog post running more than 3,100 words,"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/opendoors-india-exit-is-fueling-a-bigger-conversation-about-ai-and-outsourcing/",
    "domain": "大厂 AI 动态",
    "title": "Opendoor’s India exit is fueling a bigger conversation about AI and outsourcing",
    "url": "https://techcrunch.com/2026/06/10/opendoors-india-exit-is-fueling-a-bigger-conversation-about-ai-and-outsourcing/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T04:02:19+00:00",
    "summary": "The decision comes as India emerges as the world’s largest GCC market."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/anthropics-dario-amodei-has-just-one-direct-report/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s Dario Amodei has just one direct report",
    "url": "https://techcrunch.com/2026/06/10/anthropics-dario-amodei-has-just-one-direct-report/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T03:53:06+00:00",
    "summary": "If you doubted his genius, doubt no more."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/xai-fired-an-engineer-who-raised-alarms-about-grok-safety-new-lawsuit-claims/",
    "domain": "大厂 AI 动态",
    "title": "xAI fired an engineer who raised alarms about Grok safety, new lawsuit claims",
    "url": "https://techcrunch.com/2026/06/10/xai-fired-an-engineer-who-raised-alarms-about-grok-safety-new-lawsuit-claims/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T22:31:19+00:00",
    "summary": "A former xAI engineer is suing the company and SpaceX, alleging he was fired for raising AI safety concerns about Grok days before SpaceX's historic IPO."
  },
  {
    "id": "rss:https://techcrunch.com/video/why-andrew-yang-is-building-instead-of-waiting-for-washington/",
    "domain": "大厂 AI 动态",
    "title": "Why Andrew Yang is building instead of waiting for Washington",
    "url": "https://techcrunch.com/video/why-andrew-yang-is-building-instead-of-waiting-for-washington/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T22:24:12+00:00",
    "summary": "Andrew Yang’s 2020 presidential campaign&#160;was based on a&#160;warning that automation and AI would hollow out the labor market and concentrate wealth in the hands of a few. At the time, ideas like"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/cybercriminals-claim-breach-of-oracle-peoplesoft-servers-at-100-plus-organizations/",
    "domain": "大厂 AI 动态",
    "title": "Cybercriminals claim breach of Oracle PeopleSoft servers at 100-plus organizations",
    "url": "https://techcrunch.com/2026/06/10/cybercriminals-claim-breach-of-oracle-peoplesoft-servers-at-100-plus-organizations/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T21:33:32+00:00",
    "summary": "The ShinyHunters hacking gang claims to have compromised the Oracle PeopleSoft servers of more than 100 organizations, including many universities."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/everyone-wants-a-piece-of-teslas-battery-business/",
    "domain": "大厂 AI 动态",
    "title": "Everyone wants a piece of Tesla’s battery business",
    "url": "https://techcrunch.com/2026/06/10/everyone-wants-a-piece-of-teslas-battery-business/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T20:21:25+00:00",
    "summary": "Electricity demand from AI data centers is pushing everyone — including automakers like GM and Ford — into the energy storage business."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/fresh-off-bond-sale-amazon-borrows-17-5-billion-from-banks-as-ai-spending-continues/",
    "domain": "大厂 AI 动态",
    "title": "Fresh off bond sale, Amazon borrows $17.5B from banks as AI spending continues",
    "url": "https://techcrunch.com/2026/06/10/fresh-off-bond-sale-amazon-borrows-17-5-billion-from-banks-as-ai-spending-continues/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T20:19:31+00:00",
    "summary": "Companies are burning through exorbitant sums of money to keep pace in the AI arms race. Debt is climbing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/north-koreans-behind-nearly-half-of-us-tech-industry-hacks-says-crowdstrike/",
    "domain": "大厂 AI 动态",
    "title": "North Koreans behind nearly half of US tech industry hacks, says CrowdStrike",
    "url": "https://techcrunch.com/2026/06/10/north-koreans-behind-nearly-half-of-us-tech-industry-hacks-says-crowdstrike/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T19:57:04+00:00",
    "summary": "North Korean hackers posing as remote IT workers and recruiters remain a major threat to U.S., European, and Asian companies, accounting for about half of all attacks over the past 12 months."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/wing-drone-delivery-might-not-be-a-novelty-anymore/",
    "domain": "大厂 AI 动态",
    "title": "Wing drone delivery might not be a novelty anymore",
    "url": "https://techcrunch.com/2026/06/10/wing-drone-delivery-might-not-be-a-novelty-anymore/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T19:52:09+00:00",
    "summary": "Wing is expanding into seven more U.S. cities through its partnership with Walmart."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/netflix-expands-revamped-mobile-app-across-asia-and-doubles-down-on-kids-gaming/",
    "domain": "大厂 AI 动态",
    "title": "Netflix expands revamped mobile app across Asia and doubles down on kids’ gaming",
    "url": "https://techcrunch.com/2026/06/10/netflix-expands-revamped-mobile-app-across-asia-and-doubles-down-on-kids-gaming/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T17:13:02+00:00",
    "summary": "The media giant is pushing to expand its mobile and gaming business."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/ai-pilled-firms-spend-7500-per-employee-each-month-on-ai/",
    "domain": "大厂 AI 动态",
    "title": "‘AI-pilled’ firms spend $7,500 per employee each month on AI",
    "url": "https://techcrunch.com/2026/06/10/ai-pilled-firms-spend-7500-per-employee-each-month-on-ai/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T17:07:35+00:00",
    "summary": "The most AI-obsessed firms are spending roughly $7,500 monthly per employee on AI, per Ramp AI Index. That's not more than an engineer's salary — yet."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/the-indian-government-got-cold-feet-on-starlink-just-before-spacexs-ipo/",
    "domain": "大厂 AI 动态",
    "title": "The Indian government got cold feet on Starlink just before SpaceX’s IPO",
    "url": "https://techcrunch.com/2026/06/10/the-indian-government-got-cold-feet-on-starlink-just-before-spacexs-ipo/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T16:43:11+00:00",
    "summary": "Problems with Starlink's India expansion could challenge SpaceX's IPO growth story."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/how-memory-tools-can-make-ai-models-worse/",
    "domain": "大厂 AI 动态",
    "title": "How memory tools can make AI models worse",
    "url": "https://techcrunch.com/2026/06/10/how-memory-tools-can-make-ai-models-worse/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T16:11:08+00:00",
    "summary": "New research suggests that AI memory systems can degrade model performance and encourage sycophantic tendencies."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/zest-launches-a-restaurant-discovery-app-powered-by-where-people-actually-eat/",
    "domain": "大厂 AI 动态",
    "title": "Zest launches a restaurant discovery app powered by where people actually eat",
    "url": "https://techcrunch.com/2026/06/10/zest-launches-a-restaurant-discovery-app-powered-by-where-people-actually-eat/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T15:53:07+00:00",
    "summary": "Backed by Alexis Ohanian’s 776 and Kindred Ventures, Zest uses transaction data and AI to generate restaurant recommendations based on users’ real dining habits and the places they frequent."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/why-enterprise-ai-will-be-a-major-focus-at-vivatech-2026/",
    "domain": "大厂 AI 动态",
    "title": "Why enterprise AI will be a major focus at VivaTech 2026",
    "url": "https://techcrunch.com/2026/06/10/why-enterprise-ai-will-be-a-major-focus-at-vivatech-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T15:16:00+00:00",
    "summary": "While Silicon Valley continues pushing aggressively into large language models and consumer-facing AI products, many European companies are focused on applying AI to complex systems already embedded i"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/datadog-veterans-launch-ai-coding-startup-niteshift-on-a-bet-against-big-ai-lock-in/",
    "domain": "大厂 AI 动态",
    "title": "Datadog veterans launch AI coding startup Niteshift on a bet against Big AI lock-in",
    "url": "https://techcrunch.com/2026/06/10/datadog-veterans-launch-ai-coding-startup-niteshift-on-a-bet-against-big-ai-lock-in/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T15:00:00+00:00",
    "summary": "AI coding agent startup Niteshift has raised a $7 million seed round from a who's who of angels. It's betting companies will want power over, not lock-in with model makers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/the-three-hard-tech-moonshots-fueling-spacexs-unbelievable-ipo/",
    "domain": "大厂 AI 动态",
    "title": "The three hard-tech moonshots fueling SpaceX’s unbelievable IPO",
    "url": "https://techcrunch.com/2026/06/10/the-three-hard-tech-moonshots-fueling-spacexs-unbelievable-ipo/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T14:48:01+00:00",
    "summary": "Most of the value in SpaceX's IPO is effectively a call option on the company's ambitious space data center plans."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/pinterest-bets-on-creators-with-amazon-storefront-integration/",
    "domain": "大厂 AI 动态",
    "title": "Pinterest bets on creators with Amazon Storefront integration",
    "url": "https://techcrunch.com/2026/06/10/pinterest-bets-on-creators-with-amazon-storefront-integration/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T14:34:45+00:00",
    "summary": "Pinterest is adding support for Amazon Storefronts, allowing creators to earn affiliate commissions more easily while showcasing their product recommendations in one place."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/10/warner-music-acquires-ai-attribution-startup-sureel-ai/",
    "domain": "大厂 AI 动态",
    "title": "Warner Music acquires AI attribution startup Sureel AI",
    "url": "https://techcrunch.com/2026/06/10/warner-music-acquires-ai-attribution-startup-sureel-ai/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T14:31:30+00:00",
    "summary": "Through the acquisition, WMG aims to better track when its artists' work is used in AI-generated content or for training AI models."
  },
  {
    "id": "rss:https://stratechery.com/2026/fable-5-anthropic-alignment-ai-tiers/",
    "domain": "大厂 AI 动态",
    "title": "Fable 5, Anthropic Alignment, AI Tiers",
    "url": "https://stratechery.com/2026/fable-5-anthropic-alignment-ai-tiers/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T10:00:00+00:00",
    "summary": "Fable 5 is the public version of Mythos, and while it is very capable it sets some troubling new precedents."
  },
  {
    "id": "rss:https://stratechery.com/2026/the-iphones-last-stand/",
    "domain": "大厂 AI 动态",
    "title": "The iPhone’s Last Stand",
    "url": "https://stratechery.com/2026/the-iphones-last-stand/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-09T10:00:00+00:00",
    "summary": "Siri isn't state of the art, but as long as it works — and it appears it does — it's good enough for the consumer market."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/06/diabetes-org-apologizes-for-ejecting-scientists-over-criticism-of-trump/",
    "domain": "大厂 AI 动态",
    "title": "Diabetes org apologizes for ejecting scientists over criticism of Trump",
    "url": "https://arstechnica.com/health/2026/06/diabetes-org-apologizes-for-ejecting-scientists-over-criticism-of-trump/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T22:16:57+00:00",
    "summary": "For days after the stunning incident, the ADA had doubled-down on the choice."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/man-jailed-due-to-faulty-face-recognition-says-florida-cops-ignored-other-evidence/",
    "domain": "大厂 AI 动态",
    "title": "Man sues Florida cops over arrest spurred by \"93% match\" in facial recognition",
    "url": "https://arstechnica.com/tech-policy/2026/06/man-jailed-due-to-faulty-face-recognition-says-florida-cops-ignored-other-evidence/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T21:30:44+00:00",
    "summary": "Lawsuit: \"Police let an error-prone AI system stand in for an investigation.\""
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/logitechs-mobi-fold-folds-for-travel-but-i-prefer-a-different-portable-mouse/",
    "domain": "大厂 AI 动态",
    "title": "Logitech’s foldable mouse is for people who refuse to carry a mouse with them",
    "url": "https://arstechnica.com/gadgets/2026/06/logitechs-mobi-fold-folds-for-travel-but-i-prefer-a-different-portable-mouse/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T19:57:56+00:00",
    "summary": "The Mobi Fold is an $80 Bluetooth mouse with a silicone-wrapped hinge."
  },
  {
    "id": "rss:https://arstechnica.com/google/2026/06/googles-latest-diffusiongemma-open-ai-model-comes-with-a-4x-speed-boost/",
    "domain": "大厂 AI 动态",
    "title": "Google DeepMind releases DiffusionGemma, a model that runs local AI 4x faster",
    "url": "https://arstechnica.com/google/2026/06/googles-latest-diffusiongemma-open-ai-model-comes-with-a-4x-speed-boost/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T19:29:21+00:00",
    "summary": "Diffusion AI is most common in image generation, but it can make text outputs much faster."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/we-managed-to-glean-some-interesting-details-about-the-artemis-iii-mission/",
    "domain": "大厂 AI 动态",
    "title": "We managed to glean some interesting details about the Artemis III mission",
    "url": "https://arstechnica.com/space/2026/06/we-managed-to-glean-some-interesting-details-about-the-artemis-iii-mission/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T17:31:13+00:00",
    "summary": "\"I was on the phone with Blue Origin leadership that night, all the next day, all through the weekend.\""
  },
  {
    "id": "hn:48405718",
    "domain": "股票",
    "title": "SpaceX, Other Mega IPOs Denied Fast Index Entry by S&P",
    "url": "https://www.bloomberg.com/news/articles/2026-06-04/s-p-dow-jones-keeps-megacap-ipo-rules-as-is-after-consultation",
    "source": "tristanj",
    "platform": "hackernews",
    "points": 1059,
    "published_at": "2026-06-04T22:48:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48455233",
    "domain": "股票",
    "title": "We Think the SpaceX IPO Is Overvalued",
    "url": "https://www.morningstar.com/stocks/why-we-think-spacex-ipo-is-overvalued?content_id=20768396545",
    "source": "0xedb",
    "platform": "hackernews",
    "points": 262,
    "published_at": "2026-06-09T01:56:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48314363",
    "domain": "股票",
    "title": "Sam Altman and Dario Amodei are both walking back AI jobs apocalypse predictions",
    "url": "https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/",
    "source": "ianrahman",
    "platform": "hackernews",
    "points": 236,
    "published_at": "2026-05-28T19:43:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:48373909",
    "domain": "股票",
    "title": "Morningstar values SpaceX at $780B, half its IPO target",
    "url": "https://www.reuters.com/business/media-telecom/morningstar-values-spacex-780-billion-half-its-ipo-target-2026-06-02/",
    "source": "berkeleyjunk",
    "platform": "hackernews",
    "points": 211,
    "published_at": "2026-06-02T18:09:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:48210226",
    "domain": "股票",
    "title": "OpenAI Is Preparing to File for an IPO Soon",
    "url": "https://www.wsj.com/tech/ai/openai-is-preparing-to-file-for-an-ipo-very-soon-0ec95af5",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 206,
    "published_at": "2026-05-20T16:24:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48134429",
    "domain": "股票",
    "title": "Sam Altman's Business Dealings Under GOP Scrutiny Ahead of OpenAI's IPO",
    "url": "https://www.wsj.com/tech/ai/sam-altmans-business-dealings-under-gop-scrutiny-ahead-of-openais-ipo-52c1cc4d",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 199,
    "published_at": "2026-05-14T12:27:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:48446310",
    "domain": "股票",
    "title": "Italy's Bending Spoons, owner of AOL and Vimeo, files for Nasdaq IPO",
    "url": "https://www.reuters.com/legal/transactional/italys-bending-spoons-files-us-ipo-2026-06-08/",
    "source": "mmarian",
    "platform": "hackernews",
    "points": 123,
    "published_at": "2026-06-08T15:04:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:48394034",
    "domain": "股票",
    "title": "The SpaceX IPO will be the theft of the century",
    "url": "https://montanaskeptic.substack.com/p/the-spacex-ipo-will-be-the-theft",
    "source": "400thecat",
    "platform": "hackernews",
    "points": 142,
    "published_at": "2026-06-04T04:52:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48217052",
    "domain": "股票",
    "title": "OpenAI to confidentially file for IPO as soon as Friday",
    "url": "https://www.cnbc.com/2026/05/20/openai-ipo-filing.html",
    "source": "doppp",
    "platform": "hackernews",
    "points": 137,
    "published_at": "2026-05-21T02:24:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48385866",
    "domain": "股票",
    "title": "SpaceX's IPO is a disaster waiting to happen for your pension fund",
    "url": "https://www.irishtimes.com/business/2026/06/03/heavily-in-debt-loss-making-with-eyes-on-sending-people-to-mars-why-would-anyone-invest-in-spacex/",
    "source": "anonymousDan",
    "platform": "hackernews",
    "points": 92,
    "published_at": "2026-06-03T16:02:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48390053",
    "domain": "股票",
    "title": "Iran war drains US oil stocks to lowest level since 2004",
    "url": "https://www.ft.com/content/d0be73c8-b8d8-4ffd-874e-e97a6ecffef7",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 61,
    "published_at": "2026-06-03T21:06:30+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3774410",
    "domain": "股票",
    "title": "甲骨文暴跌？AI基建补不了的硬伤——“高息、高债+歇菜软件”",
    "url": "https://wallstreetcn.com/articles/3774410",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T08:03:39+00:00",
    "summary": "甲骨文26财年Q4业绩喜忧参半：OCI业务同比增长92%如期加速，但符合预期无惊喜；毛利率68.8%环比触底却仍低于预期；RPO超预期达6380亿；Capex共担模式覆盖46亿支出，自由现金流明显改善。但传统软件业务持续走弱，利息支出环比增22%，高债压力未解。"
  },
  {
    "id": "wscn:3774414",
    "domain": "股票",
    "title": "顺丰早期孵化的零售柜，要IPO了",
    "url": "https://wallstreetcn.com/articles/3774414",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T08:00:40+00:00",
    "summary": "定位“轻场景”。"
  },
  {
    "id": "wscn:3774411",
    "domain": "股票",
    "title": "郭明錤：预计台积电CoPoS 2028下半年量产，英伟达最新AI芯片或率先用上",
    "url": "https://wallstreetcn.com/articles/3774411",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T07:41:12+00:00",
    "summary": "台积电下一代先进封装技术CoPoS量产时间表曝光——2028年下半年正式投产，英伟达Feynman芯片有望首发采用。分析师郭明錤详解三层玻璃核心基板架构，并逐一击破\"玻璃取代ABF\"等三大行业误读。台积电凭此或将封装领域竞争优势锁定至2032年。"
  },
  {
    "id": "wscn:3774409",
    "domain": "股票",
    "title": "泄露三分之二人口数据？韩国“亚马逊”被重罚",
    "url": "https://wallstreetcn.com/articles/3774409",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T07:37:54+00:00",
    "summary": "韩国最大电商平台Coupang因数据泄露及违规收集个人信息，被处以6246亿韩元（约合4.09亿美元）罚款，创韩国同类罚单新高。事件波及全国近三分之二人口，凸显其网络安全管控严重缺位。当前Coupang正面临用户信任危机与业绩下滑双重压力，今年一季度已录得2.42亿美元运营亏损。"
  },
  {
    "id": "wscn:3774405",
    "domain": "股票",
    "title": "Anthropic CEO：我只有1个直接下属，其余全交给妹妹",
    "url": "https://wallstreetcn.com/articles/3774405",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T07:35:14+00:00",
    "summary": "Anthropic CEO Dario Amodei透露，他仅设一名直接下属——其幕僚长，其余高管均向担任总裁的妹妹Daniela汇报。这一架构让他得以专注战略、研究与文化，而非日常运营。该公司成立仅五年多，估值已近万亿美元。相比之下，OpenAI的Altman有六名直接下属，英伟达的黄仁勋则多达数十人。"
  },
  {
    "id": "wscn:3774398",
    "domain": "股票",
    "title": "美国政府砸20亿扶持量子计算，谷歌为何缺席？",
    "url": "https://wallstreetcn.com/articles/3774398",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T07:33:36+00:00",
    "summary": "美国政府向IBM等九家企业发放共计20亿美元拨款，谷歌却主动出局。谷歌量子AI首席运营官Chou公开披露，拒绝特朗普政府量子计算资助的核心原因，在于资金附带条件将拖慢研发节奏。谷歌同时警告，签证政策收紧正威胁全球顶尖人才招募，或动摇美国量子竞争力根基。"
  },
  {
    "id": "wscn:3774403",
    "domain": "股票",
    "title": "软银抵押OpenAI借钱再碰壁，市场开始质疑其偿债能力",
    "url": "https://wallstreetcn.com/articles/3774403",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T07:29:49+00:00",
    "summary": "软银以OpenAI股权为抵押的60亿美元保证金贷款谈判陷入僵局，消息一出股价单日重挫近10%。贷款方对非上市资产估值心存疑虑，而软银背后还悬着2027年到期的400亿美元过桥债务。孙正义押注AI的豪情与债务压顶的现实，正形成一场愈发难以回避的张力。"
  },
  {
    "id": "wscn:3774407",
    "domain": "股票",
    "title": "美国拟从战略石油储备再出借4000万桶原油，以压低燃油价格",
    "url": "https://wallstreetcn.com/articles/3774407",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T07:27:40+00:00",
    "summary": "美能源部周三宣布计划出借最多4000万桶战略石油储备，以平抑中东冲突下的国内油价。目前美国SPR库存已降至3.492亿桶的三年低点。官方预计今明两年将通过最高24%的实物溢价机制回收3500万至4000万桶原油以补充储备。"
  },
  {
    "id": "wscn:3774379",
    "domain": "股票",
    "title": "黄金看空情绪升温！交易员押注未来两年将再跌40%",
    "url": "https://wallstreetcn.com/articles/3774379",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T07:25:50+00:00",
    "summary": "GLD ETF较历史高点累跌25%，期权市场已现极端押注：有交易员买入2028年到期的深度看跌合约，预判黄金两年内再跌40%。土耳其央行抛售、海湾国家变现军费、印度加征进口关税三重利空叠加，技术支撑失守更触发程序性止损。"
  },
  {
    "id": "wscn:3774295",
    "domain": "股票",
    "title": "软磁破局，量价齐升：人工智能掀起电感革命，国产替代迎来关键窗口期",
    "url": "https://wallstreetcn.com/premium/articles/3774295?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T07:20:36+00:00",
    "summary": "AI供电架构升级浪潮中，TLVR与MLCC系统性共振。"
  },
  {
    "id": "wscn:3774404",
    "domain": "股票",
    "title": "报道：SK海力士罕见上调设备采购价，多家供应商提出涨价3%-4%的要求",
    "url": "https://wallstreetcn.com/articles/3774404",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T07:05:52+00:00",
    "summary": "HBM热潮将SK海力士单季营业利润率推至72%历史峰值，这家韩国存储巨头正将红利向上游传导，罕见地允许设备供应商提出3%至4%的涨价请求。设备厂商五年未涨价的惯例正在松动，超级周期重塑供应链话语权，一场半导体产业链的利润再分配悄然展开。"
  },
  {
    "id": "wscn:3774400",
    "domain": "股票",
    "title": "补贴→Token计费→降价！OpenAI打响价格战，Token经济学拐点将至？",
    "url": "https://wallstreetcn.com/articles/3774400",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T07:05:04+00:00",
    "summary": "当Token价格战真正打响，AI行业靠什么赚钱？整条AI商业化的估值逻辑，都到了需要被重写的时刻。拼“性价比”和“稀缺性”的时期可能到了。对于OpenAI而言“局势进一步恶化”，分析指“一旦OpenAI走下坡路，很可能会拖垮英伟达、甲骨文、Coreweave等。”"
  },
  {
    "id": "wscn:3774384",
    "domain": "股票",
    "title": "创业板跌超1%，北证50大跌超3%，新易盛大跌9%，恒科指跌近2%，阿里跌超5%，多晶硅涨停",
    "url": "https://wallstreetcn.com/articles/3774384",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T06:54:45+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市约4500股飘绿，上午半天成交1.61万亿。沪深两市半日成交额1.59万亿，较上个交易日缩量1350余亿。板块方面，AI应用、短剧游戏、云计算、人工智能、人形机器人、算力租赁、商业航天、离境退税概念股跌幅靠前，工业气体、PCB、半导体材料、能源金属题材逆势走强。"
  },
  {
    "id": "wscn:3774389",
    "domain": "股票",
    "title": "美伊再度交火，日韩股市集体收涨，债市汇市承压，布油涨幅收窄",
    "url": "https://wallstreetcn.com/articles/3774389",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T06:50:29+00:00",
    "summary": "韩国综合股价指数收涨0.42%至7762.94点。科技巨头股价持续下挫，追踪\"Mag7\"的指数连续第四日下跌；芝加哥期权交易所波动率指数（VIX）攀升至4月以来最高点。日元兑美元持平于160.50附近。布伦特原油一度走高，但随后涨幅收窄，报每桶93.35美元，涨幅0.2%。"
  },
  {
    "id": "wscn:3774402",
    "domain": "股票",
    "title": "6·18监管直击：5家电商被约谈，百亿补贴“水分”被戳穿",
    "url": "https://wallstreetcn.com/articles/3774402",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T06:28:37+00:00",
    "summary": "七年“百亿补贴”走到转折。"
  },
  {
    "id": "wscn:3774401",
    "domain": "股票",
    "title": "国际油价仍低于100美元的十大原因",
    "url": "https://wallstreetcn.com/articles/3774401",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T06:12:36+00:00",
    "summary": "分析认为，油价未破百元主要受中国进口减少、全球需求萎缩、绕行管道输出、战前供过于求、4亿桶战略储备史诗级释放以及美洲大增产六大供需因素压制；叠加炼厂灵活性、期权分流、特朗普干预与卫星技术等四大结构性力量，共同化解了供应冲击。"
  },
  {
    "id": "wscn:3774397",
    "domain": "股票",
    "title": "紧跟黄仁勋！OpenAI CEO下周访韩，或讨论AI合作",
    "url": "https://wallstreetcn.com/articles/3774397",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T06:06:01+00:00",
    "summary": "Sam Altman下周或将再度访韩，与三星探讨工作创新及基础设施项目“星际之门”，并与Kakao推进ChatGPT接入其最大社交软件KakaoTalk的合作。上次访韩期间OpenAI已与三星电子、SK集团分别签署战略合作协议。"
  },
  {
    "id": "wscn:3774399",
    "domain": "股票",
    "title": "极兔被国家邮政局立案调查 紧急回应并全面整改",
    "url": "https://wallstreetcn.com/articles/3774399",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T06:01:49+00:00",
    "summary": "中国如今是极兔最大单一市场。"
  },
  {
    "id": "wscn:3774043",
    "domain": "股票",
    "title": "SpaceX上市倒计时：美股肥尾风险有多大？",
    "url": "https://wallstreetcn.com/premium/articles/3774043?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T05:34:54+00:00",
    "summary": "SpaceX超级IPO或引发被动资金调仓、散户FOMO及杠杆去化风险，并对AI牛市估值扩张与市场流动性形成考验。"
  },
  {
    "id": "wscn:3774393",
    "domain": "股票",
    "title": "被骂翻了！Anthropic认错：曾暗中降低Claude性能“阻止”竞品开发，现已撤回",
    "url": "https://wallstreetcn.com/articles/3774393",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T05:24:11+00:00",
    "summary": "Anthropic被迫撤回一项藏匿于319页系统文件中的隐秘政策——对竞争对手的AI开发请求\"静默降级\"，在用户毫不知情的情况下注水回答。研究社区怒斥此举是\"秘密破坏\"与\"拉高梯子\"，公司随即道歉并宣布改为透明拦截。这是Anthropic首次公开承认对模型实施静默干预，深层矛盾就此暴露。"
  },
  {
    "id": "hn:48452224",
    "domain": "股票",
    "title": "OpenAI Confidentially Files for IPO",
    "url": "https://www.cnbc.com/2026/06/08/openai-confidentially-files-for-ipo-prepping-wall-street-for-ai-debut.html",
    "source": "rvz",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-06-08T21:16:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48436328",
    "domain": "股票",
    "title": "Musk's SpaceX IPO Narrative Is a Whole New Level of Bullshit",
    "url": "https://text.tchncs.de/chronik-des-laufenden-wahnsinns/h1elon-musk-has-spouted-his-fair-share-of-bullshit-but-his-latest-claims-about",
    "source": "doener",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-06-07T16:24:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48193111",
    "domain": "股票",
    "title": "Anthropic Is Preparing for IPO and We Should Be Worried",
    "url": "https://www.vincentschmalbach.com/anthropic-ipo-developers-should-be-worried-v2/",
    "source": "vincent_s",
    "platform": "hackernews",
    "points": 89,
    "published_at": "2026-05-19T13:30:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48451099",
    "domain": "股票",
    "title": "Why Morningstar believes the SpaceX IPO is overvalued",
    "url": "https://www.morningstar.com/stocks/why-we-think-spacex-ipo-is-overvalued",
    "source": "ForHackernews",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-06-08T20:07:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48391046",
    "domain": "股票",
    "title": "We Uncovered a Hidden Wealth Transfer in the SpaceX IPO. You're Holding the Bag [video]",
    "url": "https://www.youtube.com/watch?v=sYA-z0Y8WRQ",
    "source": "CharlesW",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-06-03T22:32:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48382926",
    "domain": "股票",
    "title": "Goldman Sachs CEO says markets in 'greed' mode as AI companies seek billions",
    "url": "https://www.cnbc.com/2026/06/02/goldman-ceo-david-solomon-greed-mode-ai-firms-ipos.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-06-03T12:08:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48404734",
    "domain": "股票",
    "title": "Fidelity lowers SpaceX IPO entry requirement from $500,000 to just $2,000",
    "url": "https://finance.yahoo.com/markets/stocks/articles/fidelity-cuts-spacex-ipo-eligibility-183319186.html",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-06-04T21:15:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48231815",
    "domain": "股票",
    "title": "SpaceX not the behemoth everyone thought",
    "url": "https://www.axios.com/2026/05/21/spacex-ipo-musk-ai",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 61,
    "published_at": "2026-05-22T04:03:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48383625",
    "domain": "股票",
    "title": "Dell inks $9.7B Pentagon contract after Trump acquires stock",
    "url": "https://www.washingtonpost.com/politics/2026/05/28/dell-inks-97-billion-pentagon-contract-after-trump-acquires-stock-praises-company/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-06-03T13:19:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48419956",
    "domain": "股票",
    "title": "Nasdaq falls 4% and suffers worst day since April 2025 traders flee chip stocks",
    "url": "https://www.cnbc.com/2026/06/04/stock-market-today-live-updates.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-06-06T00:02:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:48390904",
    "domain": "股票",
    "title": "SpaceX Sets Price for $1.77T IPO",
    "url": "https://www.cnbc.com/2026/06/03/spacex-ipo-stock-price-roadshow-musk.html",
    "source": "gen220",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-06-03T22:19:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48229528",
    "domain": "股票",
    "title": "The SpaceX IPO It's Worse Than You Think [video]",
    "url": "https://www.youtube.com/watch?v=-X6YzlY_8tM",
    "source": "ZeljkoS",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-05-21T22:19:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:48359035",
    "domain": "股票",
    "title": "Anthropic Files to Go Public, Setting Stage for Huge I.P.O.",
    "url": "https://www.nytimes.com/2026/06/01/technology/anthropic-ipo.html",
    "source": "jbegley",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-06-01T16:27:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48369063",
    "domain": "股票",
    "title": "Elon Musk Laid Out 602 Goals. We Counted How Many He Hit",
    "url": "https://www.nytimes.com/interactive/2026/06/02/technology/elon-musk-promises-spacex-ipo.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-06-02T11:56:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48354214",
    "domain": "股票",
    "title": "How Not to Buy SpaceX Stock (It's Harder Than You Think)",
    "url": "https://cranberries.medium.com/how-not-to-buy-spacex-stock-its-harder-than-you-think-a37610cb8bd3",
    "source": "clktmr",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-06-01T08:50:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48343303",
    "domain": "股票",
    "title": "The SpaceX IPO is great for Elon Musk and terrible for you",
    "url": "https://www.theverge.com/ai-artificial-intelligence/940001/elon-musk-spacex-ipo-ai",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-05-31T05:34:42+00:00",
    "summary": ""
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
    "id": "hn:48368083",
    "domain": "股票",
    "title": "Ask HN: What is your opinion on index rule changes to accommodate Mega-Cap IPOs?",
    "url": "https://news.ycombinator.com/item?id=48368083",
    "source": "figmert",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-06-02T09:55:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48330421",
    "domain": "股票",
    "title": "The record divide between corporate profits and worker pay",
    "url": "https://www.wsj.com/finance/stocks/the-record-divide-between-corporate-profits-and-worker-pay-ea4c75bc",
    "source": "hhs",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-05-29T22:55:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48108313",
    "domain": "金融",
    "title": "US inflation jumps to 3.8% as energy costs surge from Iran war",
    "url": "https://www.bbc.com/news/articles/c202pgxx89lo",
    "source": "tartoran",
    "platform": "hackernews",
    "points": 260,
    "published_at": "2026-05-12T13:51:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48454210",
    "domain": "金融",
    "title": "Federal judge blocks H1B visa $100K fee",
    "url": "https://www.alaskasnewssource.com/2026/06/08/federal-judge-blocks-h1-b-visa-100k-fee/",
    "source": "naturalmovement",
    "platform": "hackernews",
    "points": 189,
    "published_at": "2026-06-09T00:01:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48479537",
    "domain": "金融",
    "title": "Meta steals a tactic from Tesla and builds data centers in tents",
    "url": "https://techcrunch.com/2026/06/04/meta-steals-a-tactic-from-tesla-and-builds-data-centers-in-tents/",
    "source": "gnabgib",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-06-10T17:18:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48483445",
    "domain": "金融",
    "title": "US President says 'I love the inflation'",
    "url": "https://www.cnbc.com/2026/06/10/trump-inflation-cpi-iran-oil.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-06-10T22:12:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48206387",
    "domain": "金融",
    "title": "The quadratic sandwich",
    "url": "https://fedemagnani.github.io/math/2026/04/08/the-quadratic-sandwich.html",
    "source": "cpp_frog",
    "platform": "hackernews",
    "points": 147,
    "published_at": "2026-05-20T12:06:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:48476514",
    "domain": "金融",
    "title": "GnuCash is right. It's also why I built my own finance app",
    "url": "https://k-id.app/blog/gnucash-is-right/",
    "source": "tinosar",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-06-10T14:06:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:48384810",
    "domain": "金融",
    "title": "Tesla retroactively added 'supervised' to FSD contracts owners signed years ago",
    "url": "https://electrek.co/2026/06/03/tesla-retroactively-modified-fsd-contracts-supervised/",
    "source": "breve",
    "platform": "hackernews",
    "points": 73,
    "published_at": "2026-06-03T14:43:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48360414",
    "domain": "金融",
    "title": "Making Debian or Fedora persistent live images",
    "url": "https://sigwait.org/~alex/blog/2026/05/28/smdBC8.html",
    "source": "henry_flower",
    "platform": "hackernews",
    "points": 89,
    "published_at": "2026-06-01T18:02:10+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.11223",
    "domain": "金融",
    "title": "Scenario Constraints with Memory: A Finite-State Approach to Quantitative Financial Analysis",
    "url": "https://arxiv.org/abs/2606.11223",
    "source": "Vitaly N\\\"urnberg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T04:00:00+00:00",
    "summary": "arXiv:2606.11223v1 Announce Type: new Abstract: Quantifying worst-case and best-case performance under complex market scenarios is a persistent challenge in financial risk management and the verificat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.11237",
    "domain": "金融",
    "title": "A Hybrid LSMC-PDE Method for Bermudan Option Pricing under the Gatheral Double Mean-Reverting Model",
    "url": "https://arxiv.org/abs/2606.11237",
    "source": "Mara Kalicanin Dimitrov, Ying Ni",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T04:00:00+00:00",
    "summary": "arXiv:2606.11237v1 Announce Type: new Abstract: We study Bermudan option pricing under the Gatheral Double Mean-Reverting (GDMR) stochastic volatility model. The model features a variance process toge"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.11238",
    "domain": "金融",
    "title": "Artificial Intelligence in Ship Finance: Applications, Opportunities, and a Case Study in AI-Augmented Loan Origination",
    "url": "https://arxiv.org/abs/2606.11238",
    "source": "Lasse Dierich, Orestis Schinas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T04:00:00+00:00",
    "summary": "arXiv:2606.11238v1 Announce Type: new Abstract: Ship finance is a data-intensive and document-heavy segment of asset-based lending, requiring the integration of financial, technical, contractual, and "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.11318",
    "domain": "金融",
    "title": "Mean-Variance Optimization in Ambiguous Financial Markets with Learning",
    "url": "https://arxiv.org/abs/2606.11318",
    "source": "Nicole B\\\"auerle, Anne MacKay",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T04:00:00+00:00",
    "summary": "arXiv:2606.11318v1 Announce Type: new Abstract: We consider a continuous time investment problem in a multi-asset Black-Scholes market with the following features: The assets' drifts are not known and"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.11566",
    "domain": "金融",
    "title": "Credit Capacity and the Propagation of Funding Shocks: Evidence from U.S. and Brazilian Financial Intermediaries",
    "url": "https://arxiv.org/abs/2606.11566",
    "source": "Ayush Jha, Ali Jaffri, Frank Fabozzi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T04:00:00+00:00",
    "summary": "arXiv:2606.11566v1 Announce Type: new Abstract: Why do similar funding shocks generate sharply different credit outcomes across countries? We develop and estimate a dynamic structural model in which i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.11798",
    "domain": "金融",
    "title": "Deterministic Policy Gradient for Learning Equilibrium in Time-Inconsistent Control Problems",
    "url": "https://arxiv.org/abs/2606.11798",
    "source": "Xin Guo, Yijie Huang, Xiang Yu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T04:00:00+00:00",
    "summary": "arXiv:2606.11798v1 Announce Type: new Abstract: In this paper, we develop a continuous-time model-free reinforcement learning algorithm to learn deterministic equilibrium policies in general time-inco"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.11859",
    "domain": "金融",
    "title": "Scenario Generation for Time Series and Curves: A Comparison of Nonparametric and Semiparametric Bootstrap",
    "url": "https://arxiv.org/abs/2606.11859",
    "source": "Nicola Baldoni, Michele Sparviero, Lorenzo Viola",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T04:00:00+00:00",
    "summary": "arXiv:2606.11859v1 Announce Type: new Abstract: Generating stochastic trajectories for asset classes is an increasingly relevant task in quantitative finance. Traditional approaches, such as the stati"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.12201",
    "domain": "金融",
    "title": "Materealistic? How European energy system models exceed raw material reserves",
    "url": "https://arxiv.org/abs/2606.12201",
    "source": "Jan Mutke, Jonas Finke, Katharina Esser, Heidi Heinrichs",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T04:00:00+00:00",
    "summary": "arXiv:2606.12201v1 Announce Type: new Abstract: Decarbonising energy systems reduces emissions and fossil fuel dependency, but expanding renewables increases demands for critical raw materials. Most e"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.11962",
    "domain": "金融",
    "title": "Composite likelihood inference of fractional Gaussian processes with sequentially optimal subset selection",
    "url": "https://arxiv.org/abs/2606.11962",
    "source": "Mathis Fourreau, Matthieu Garcin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T04:00:00+00:00",
    "summary": "arXiv:2606.11962v1 Announce Type: cross Abstract: The composite likelihood method reduces the computational cost of parameter estimation in time series by considering several subsets of observations i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2411.13579",
    "domain": "金融",
    "title": "Optimal portfolio under ratio-type periodic evaluation in stochastic factor models under convex trading constraints",
    "url": "https://arxiv.org/abs/2411.13579",
    "source": "Wenyuan Wang, Kaixin Yan, Xiang Yu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T04:00:00+00:00",
    "summary": "arXiv:2411.13579v2 Announce Type: replace Abstract: This paper studies a type of periodic utility maximization problem for portfolio management in incomplete stochastic factor models with convex tradi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2411.19444",
    "domain": "金融",
    "title": "Capital Asset Pricing Model with Size Factor and Normalizing by Volatility Index",
    "url": "https://arxiv.org/abs/2411.19444",
    "source": "Abraham Atsiwo, Andrey Sarantsev",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T04:00:00+00:00",
    "summary": "arXiv:2411.19444v5 Announce Type: replace Abstract: The Capital Asset Pricing Model (CAPM) relates a well-diversified stock portfolio to a benchmark portfolio. We insert size effect in CAPM, capturing"
  },
  {
    "id": "rss:https://arxiv.org/abs/2504.06717",
    "domain": "金融",
    "title": "Optimal Execution and Macroscopic Market Making",
    "url": "https://arxiv.org/abs/2504.06717",
    "source": "Ivan Guo, Shijia Jin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T04:00:00+00:00",
    "summary": "arXiv:2504.06717v2 Announce Type: replace Abstract: We propose a stochastic game modelling the strategic interaction between market makers and traders. From the trader's perspective, the conventional "
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.18343",
    "domain": "金融",
    "title": "Explicit Rational Formulae for Bachelier (Normal) Implied Volatility",
    "url": "https://arxiv.org/abs/2605.18343",
    "source": "Fabien Le Floc'h",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T04:00:00+00:00",
    "summary": "arXiv:2605.18343v3 Announce Type: replace Abstract: We present two explicit rational formulae for Bachelier, or normal, implied volatility. The formulae take the option price, forward, strike, and exp"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.01650",
    "domain": "金融",
    "title": "Post Selection Estimation of Sharpe Ratios",
    "url": "https://arxiv.org/abs/2606.01650",
    "source": "Steven E. Pav",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T04:00:00+00:00",
    "summary": "arXiv:2606.01650v2 Announce Type: replace Abstract: We consider the problem of estimating the true Sharpe ratio of an asset selected for having the highest observed in-sample Sharpe ratio among many a"
  },
  {
    "id": "rss:https://arxiv.org/abs/1911.04090",
    "domain": "金融",
    "title": "A post hoc test on the Sharpe ratio",
    "url": "https://arxiv.org/abs/1911.04090",
    "source": "Steven E. Pav",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T04:00:00+00:00",
    "summary": "arXiv:1911.04090v3 Announce Type: replace-cross Abstract: We describe a post hoc test for the Sharpe ratio, analogous to Tukey's test for pairwise equality of means. The test can be applied after reje"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.19225",
    "domain": "金融",
    "title": "FinTradeBench: A Financial Reasoning Benchmark for LLMs",
    "url": "https://arxiv.org/abs/2603.19225",
    "source": "Yogesh Agrawal, Aniruddha Dutta, Md Mahadi Hasan, Santu Karmaker, Aritra Dutta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T04:00:00+00:00",
    "summary": "arXiv:2603.19225v5 Announce Type: replace-cross Abstract: Real-world financial decision-making is a challenging problem that requires reasoning over heterogeneous signals, including company fundamenta"
  },
  {
    "id": "hn:48436542",
    "domain": "金融",
    "title": "Ripping a DVD, a federal crime in 1999, requires $22 and free software in 2026",
    "url": "https://ringmast4r.substack.com/p/in-1999-this-was-a-federal-crime",
    "source": "akkartik",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-06-07T16:48:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48438281",
    "domain": "金融",
    "title": "Boomers are hoarding most of America's wealth and power",
    "url": "https://finance.yahoo.com/economy/articles/golden-years-not-golden-boomers-113000201.html",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-06-07T20:35:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48451917",
    "domain": "金融",
    "title": "Federal judge rules Trump's $100k fee for H-1B visas unlawful",
    "url": "https://www.theguardian.com/us-news/2026/jun/08/trump-h-1b-visa-fee-invalidated",
    "source": "xpl",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-06-08T20:57:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48406282",
    "domain": "金融",
    "title": "S&P Global keeps fast index entry rules unchanged as SpaceX listing looms",
    "url": "https://www.reuters.com/business/finance/sp-global-keeps-fast-entry-proposal-unchanged-spacex-listing-looms-2026-06-04/",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-06-04T23:55:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48317563",
    "domain": "金融",
    "title": "Microsoft data suggests using AI is more expensive than hiring people",
    "url": "https://finance.yahoo.com/sectors/technology/articles/microsoft-data-suggests-using-ai-225900743.html",
    "source": "voxadam",
    "platform": "hackernews",
    "points": 68,
    "published_at": "2026-05-29T00:49:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48449003",
    "domain": "金融",
    "title": "Half of Americans say they're worse off financially than a year ago",
    "url": "https://www.cbsnews.com/news/americans-worse-off-financially-year-ago-fed-survey/",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-06-08T18:12:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:48210413",
    "domain": "金融",
    "title": "Standard Chartered CEO walks back comment about 'lower-value human capital'",
    "url": "https://www.wsj.com/finance/banking/ceo-walks-back-comment-about-replacing-lower-value-human-capital-with-ai-15bdfc5c",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-05-20T16:38:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48401755",
    "domain": "金融",
    "title": "Fedora 43 Upgrade revealed 20 years old Outlook Security Bug",
    "url": "https://fedoramagazine.org/fedora-43-upgrade-revealed-20-years-old-outlook-security-bug/",
    "source": "thewebguyd",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-06-04T17:24:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:48403461",
    "domain": "金融",
    "title": "Open Letter to President of Russian Federation from President of Ukraine",
    "url": "https://www.president.gov.ua/en/news/vidkritij-list-prezidentu-rosijskoyi-federaciyi-vid-preziden-104769",
    "source": "defly",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-04T19:27:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48371952",
    "domain": "金融",
    "title": "Amazon joins Microsoft in sending message to employees",
    "url": "https://finance.yahoo.com/sectors/technology/articles/amazon-joins-microsoft-sending-shocking-171700630.html",
    "source": "hereticles",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-06-02T15:58:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:48377347",
    "domain": "金融",
    "title": "Feds failing in bid to take a supercomputer from a climate research center",
    "url": "https://arstechnica.com/science/2026/06/judge-blocks-part-of-trump-admins-effort-to-hurt-colorado-research-center/",
    "source": "yodon",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-06-02T22:46:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48328797",
    "domain": "金融",
    "title": "Federal judge orders Trump's name be removed from Kennedy Center",
    "url": "https://www.msn.com/en-us/news/politics/federal-judge-orders-trump-s-name-be-removed-from-kennedy-center/ar-AA24neRw",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-05-29T20:29:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48327518",
    "domain": "金融",
    "title": "Americans Are Falling Behind on Their $1.25T Credit-Card Bill",
    "url": "https://www.wsj.com/personal-finance/credit/us-credit-card-debt-af5c7c77",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-05-29T18:41:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48349067",
    "domain": "金融",
    "title": "Nearly Half of Home Insurance Claims Result in Zero Payout",
    "url": "https://www.wsj.com/finance/the-home-insurance-coin-flip-nearly-half-of-claims-result-in-zero-payout-4b49acaf",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-05-31T19:45:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48338988",
    "domain": "金融",
    "title": "Driver, 87, dies after Tesla on Autopilot mode crashes into pond",
    "url": "https://www.usatoday.com/story/news/nation/2026/05/29/tesla-on-autopilot-mode-crashes-into-pond-87-year-old-driver-dies/90319482007/",
    "source": "thinkcontext",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-05-30T17:59:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:48333813",
    "domain": "金融",
    "title": "Tesla Self-Certifies Level 4 Autonomous Vehicles in Texas",
    "url": "https://www.notateslaapp.com/news/4216/tesla-self-certifies-l4-autonomy-in-texas",
    "source": "frankacter",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-05-30T07:58:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48307404",
    "domain": "金融",
    "title": "Why Tesla's AI trainers don't trust its self-driving tech – or its safety stats",
    "url": "https://www.reuters.com/investigations/why-teslas-ai-trainers-dont-trust-its-self-driving-tech-or-its-safety-stats-2026-05-28/",
    "source": "puzzlingcaptcha",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-05-28T11:21:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48341005",
    "domain": "金融",
    "title": "Tesla's 'Full Self-Driving' fraud lawsuit gets first hearing in China",
    "url": "https://electrek.co/2026/05/30/tesla-fsd-china-lawsuit-first-hearing-10-owners/",
    "source": "breve",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-05-30T21:58:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48364392",
    "domain": "金融",
    "title": "How to Silence the Federal Workforce",
    "url": "https://www.theatlantic.com/ideas/2026/06/trumps-intimidation-whistleblowers-nda/687377/",
    "source": "paulpauper",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-06-02T00:38:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48271942",
    "domain": "金融",
    "title": "Show HN: Fungible – A local personal finance app in the terminal",
    "url": "https://github.com/tomfunk/fungible",
    "source": "tomfunk",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-05-25T21:35:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:48377419",
    "domain": "金融",
    "title": "FBI charges two NIH researchers with smuggling monkeypox to US from Congo",
    "url": "https://www.justice.gov/usao-edmi/pr/feds-charge-foreign-nationals-working-national-institutes-health-smuggling-monkeypox",
    "source": "delichon",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-02T22:58:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48271001",
    "domain": "金融",
    "title": "Stablecoins Are Private Money. That's Why They're a Risk to the Economy",
    "url": "https://www.wsj.com/finance/currencies/stablecoins-are-private-money-thats-why-theyre-a-risk-to-the-economy-d3498171",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-05-25T20:02:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:48284628",
    "domain": "金融",
    "title": "Trump's 25% cut on Nvidia chips to China backfired as Beijing blocks H200 sales",
    "url": "https://finance.yahoo.com/markets/stocks/articles/trumps-25-cut-nvidia-chips-194500691.html",
    "source": "frasermarlow",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-05-26T19:21:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48199462",
    "domain": "金融",
    "title": "Invisible_playwright: Stealth Firefox that passes every bot detection test",
    "url": "https://github.com/feder-cr/invisible_playwright",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-05-19T20:51:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:48115538",
    "domain": "金融",
    "title": "America is experiencing a productivity miracle",
    "url": "https://www.economist.com/finance-and-economics/2026/05/11/america-is-experiencing-a-productivity-miracle",
    "source": "mackmcconnell",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-05-12T22:39:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:48229518",
    "domain": "金融",
    "title": "Show HN: Smithereen – an early-Facebook-style Fediverse server",
    "url": "https://smithereen.software",
    "source": "grishka",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-05-21T22:18:25+00:00",
    "summary": ""
  }
]
```
