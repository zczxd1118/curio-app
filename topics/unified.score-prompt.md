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

- 今日日期：`2026-06-28`
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
  "date": "2026-06-28",
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
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1346848,
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
    "points": 1277886,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 939768,
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
    "points": 792359,
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
    "points": 602353,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 459993,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 346963,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 249149,
    "published_at": "2026-04-04T15:19:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 245538,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 244871,
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
    "points": 175658,
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
    "points": 159373,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1b5AeeGEFc",
    "domain": "AI",
    "title": "Cursor太贵？分享三个免费AI编程方案+海量编程技巧【如何看待AI编程】",
    "url": "http://www.bilibili.com/video/av114025056699722",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 156474,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 156144,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1TTR8BaEnL",
    "domain": "AI",
    "title": "Claude Code 零基础终极教程：安装、换模型、插件、Hooks、Skills、Subagents、实战项目一次讲透！",
    "url": "http://www.bilibili.com/video/av116529475622752",
    "source": "木子不写代码",
    "platform": "bilibili",
    "points": 121342,
    "published_at": "2026-05-07T08:00:00+00:00",
    "summary": "这是你能看到的最完整的 Claude Code 零基础系统教程。\n\n\n我们将深度拆解：\n\n1️⃣ 基础入门：安装、第三方模型接入、权限系统。\n\n2️⃣ 核心进阶：Tools、Hooks、Skills、Subagents 及自动化流程。\n\n3️⃣ 项目实战：从零构建一个真实可用的 AI 网页 App。\n\n\n视频跟到最后，你不只是学会写代码，而是掌握 AI 智能体的工作逻辑。我是木子，只提供 AI 时"
  },
  {
    "id": "bvid:BV1SY7C6nEwU",
    "domain": "AI",
    "title": "【开源】我制作了一个vibe coding键盘",
    "url": "http://www.bilibili.com/video/av116696660576856",
    "source": "工科男孙老师",
    "platform": "bilibili",
    "points": 119992,
    "published_at": "2026-06-05T10:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1rKjG6yEh2",
    "domain": "AI",
    "title": "10分钟+300个Agent：保姆级教程学会Agent Skills！【从零开始】",
    "url": "http://www.bilibili.com/video/av116758736279146",
    "source": "Work-Fisher",
    "platform": "bilibili",
    "points": 110595,
    "published_at": "2026-06-16T10:02:41+00:00",
    "summary": "这期我从最基础的概念，一路讲到上手实操，基本上是从 0 到 1，带你完整走一遍——一个 SKILL 到底是怎么从无到有做出来的。\n国内、国外的创建工具，我也都给你捋了一遍。希望看完这期，你也能动手做出一个真正属于自己的 SKIL。"
  },
  {
    "id": "bvid:BV1fRSfBWE5X",
    "domain": "AI",
    "title": "vlog｜白天上班 晚上vibe coding，准备一个月上架我的第一款App！",
    "url": "http://www.bilibili.com/video/av116357526003120",
    "source": "chocpink_AI版",
    "platform": "bilibili",
    "points": 98240,
    "published_at": "2026-04-06T11:33:25+00:00",
    "summary": "想了很久终于开始了这件事——vibe coding！\n\n下面快速总结了我用到的一些工具：\nApptweak：竞品调研\nfigma make、google stitch、impeccable插件：生成UI页面\nfigma mcp/plugin：连接到cursor\npinterest/小红书/iconfont：找图片/icon素材\nGrok：生图、素材优化\ncursor+Xcode（swift）：落地"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92272,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 82842,
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
    "points": 64263,
    "published_at": "2026-02-09T10:57:55+00:00",
    "summary": "本课程主要讲解Cursor简介，Cursor下载安装，Cursor生成helloWorld网页，Cursor会话里的Cursor会话里的Agent,Plan,Debug,Ask区别以及使用，Cursor常用模型介绍，Cursor模型会话上下文介绍，以及最后利用Cursor Opus4.6快速生成一个Java项目 -SpringBoot4+Vue3的学生信息管理系统，利用Cursor Opus4.6"
  },
  {
    "id": "bvid:BV12NK1zMESx",
    "domain": "AI",
    "title": "如何用Cursor开发大项目，全流程讲解，干货十足",
    "url": "http://www.bilibili.com/video/av114758657246726",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 58535,
    "published_at": "2025-06-28T02:37:22+00:00",
    "summary": "视频主题&amp;项目背景\n主题： 分享个人如何使用cursor 从0到1开发一个比较大的项目，使用的技术栈是vue+小程序+java\n项目\n一个B2B的订货商城及供应链全流程管理，包含的端有：\n小程序商城端\n供应商端\n仓储物流端\n司机配送端\n销售端\n后台管理系统\n以上小程序端都是使用webview的方式\n核心功能：\n商城的基本功能: 正逆向订单、商品、购物车、优惠券、积分、钱包、充值、工单等\n供"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 49804,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1e7VA6vEJU",
    "domain": "AI",
    "title": "【2026最新】绝对是B站No.1的Claude Code教程：国内安装+实战开发案例+个人使用心得总结，手把手带你拥抱Vibe Coding！",
    "url": "http://www.bilibili.com/video/av116640356304890",
    "source": "码士集团-马小安",
    "platform": "bilibili",
    "points": 43830,
    "published_at": "2026-05-26T10:22:46+00:00",
    "summary": "绝对是B站No.1的Claude Code教程：国内安装+实战开发案例+个人使用心得总结，手把手带你拥抱Vibe Coding！\n配套课件笔记/PPT已备好，另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景题移步评论置顶即可~"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 40339,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1EZd3BBEB5",
    "domain": "AI",
    "title": "手把手实战教学：我是如何用一个周末掌握Claude Code的",
    "url": "http://www.bilibili.com/video/av116539105739515",
    "source": "AliAbdaal",
    "platform": "bilibili",
    "points": 30164,
    "published_at": "2026-05-09T13:00:00+00:00",
    "summary": "朋友们，有个叫Claude Code的工具，过去两个月我用它做了很多事情，它真的改变了我的整个工作方式，而且我感觉到Claude Code让人与人之间的差距加速变大。。。这个视频做完我就要发给还没尝试过的亲友！\n看完这条视频，你会了解如何让AI采访你来生成AI工具点子，如何筛选高杠杆项目，如何一边制作工具一边学习AI知识和开发技术概念。你会意识到，在AI时代，你最大的资产也许就是好奇心和突破技术摩"
  },
  {
    "id": "bvid:BV1HFDSBPE7b",
    "domain": "AI",
    "title": "3分钟教你部署ai我的世界陪玩！",
    "url": "http://www.bilibili.com/video/av116390124067729",
    "source": "我叫非主流_",
    "platform": "bilibili",
    "points": 30154,
    "published_at": "2026-04-12T11:45:00+00:00",
    "summary": "这是上期视频的教程，求求大家给个三连把="
  },
  {
    "id": "bvid:BV17YPqzcES4",
    "domain": "AI",
    "title": "挑战用Cursor30分钟搭建完整小程序",
    "url": "http://www.bilibili.com/video/av116171517069277",
    "source": "前端老兵AI",
    "platform": "bilibili",
    "points": 30110,
    "published_at": "2026-03-05T12:00:00+00:00",
    "summary": "用AI写小程序，到底能有多快？ 我做了9年前端，小程序项目做了不下20个。今天我做一个实验——完全用Cursor从零搭建一个完整的待办清单 小程序，包含首页列表、新增编辑、分类筛选、本地存储，全程计时。"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29813,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29384,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV13tuqzwEm9",
    "domain": "AI",
    "title": "一个视频彻底掌握ClaudeCode使用MCP",
    "url": "http://www.bilibili.com/video/av114851586252599",
    "source": "创哥的AI实验室",
    "platform": "bilibili",
    "points": 26581,
    "published_at": "2025-07-14T12:32:55+00:00",
    "summary": "Claude Code命令行的方式，让MCP的操作也令很多朋友感觉不适，这个视频专门做了一些介绍。\n\n希望能帮助到大家。"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 24748,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1sMWyeSEPz",
    "domain": "AI",
    "title": "🤖 Cursor：AI 编程神器｜LangChain 初体验",
    "url": "http://www.bilibili.com/video/av113023373149781",
    "source": "沧海九粟",
    "platform": "bilibili",
    "points": 23344,
    "published_at": "2024-08-26T00:30:00+00:00",
    "summary": "Cursor：https://www.cursor.com/"
  },
  {
    "id": "bvid:BV1jYRRBDExF",
    "domain": "AI",
    "title": "让AI直接操作godot开发游戏，免费开源MCP插件",
    "url": "http://www.bilibili.com/video/av116545648860073",
    "source": "Yurineko73",
    "platform": "bilibili",
    "points": 22724,
    "published_at": "2026-05-10T03:00:00+00:00",
    "summary": "因为想找一个好用的mcp工具，结果发现不是要收费就是不可商用，于是借助ai直接搓了一个出来。\n目前已经发布1.0.1版本，在godot asset library搜索 [godot mcp native]即可下载使用，\n也可以去GitHub上下载完整项目 https://github.com/yurineko73/Godot-MCP-Native\n免费开源，可以随意扩展和修改，如果有需要的功能或遇"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22565,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17437,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1mmdBBFErq",
    "domain": "AI",
    "title": "【吊打付费】目前B站最全最细的Claude Code入门到精通教程，手把手教你Claude Code企业级实战案例，包含所有干货！这还没人看! 我不更了！",
    "url": "http://www.bilibili.com/video/av116419148647031",
    "source": "AI大模型学习教程",
    "platform": "bilibili",
    "points": 15902,
    "published_at": "2026-04-17T08:50:48+00:00",
    "summary": "给大家准备了一份大模型学习资料包！ 包含了ChatGLM、LLM、LangChain、Lora等大语言模型预训练及微调教程和源码资料、2026最新大模型相关面试题、大模型前沿论文、大模型全流程学习路径 大家统一评论区置顶获取哦~\n视频制作不易，如果视频对你有用的话请一键三连【长按点赞】支持一下up哦，拜托，这对我真的很重要"
  },
  {
    "id": "bvid:BV1hEVd6yEcn",
    "domain": "AI",
    "title": "【2026最新】全B站最详细AI Agent开发教程，手把手教你搭建企业级Agent智能体！从入门到实战，学完即就业，带你玩转AI Agent！",
    "url": "http://www.bilibili.com/video/av116673440909829",
    "source": "Agent开发",
    "platform": "bilibili",
    "points": 12490,
    "published_at": "2026-06-01T06:35:48+00:00",
    "summary": "【2026最新】全B站最详细AI Agent开发教程，手把手教你搭建企业级Agent智能体！从入门到实战，学完即就业，带你玩转AI Agent！"
  },
  {
    "id": "bvid:BV1nQE76TEmf",
    "domain": "AI",
    "title": "为什么你的 Vibe Coding 做不出高级感？",
    "url": "http://www.bilibili.com/video/av116719561608598",
    "source": "派大鑫",
    "platform": "bilibili",
    "points": 10860,
    "published_at": "2026-06-09T10:02:20+00:00",
    "summary": "为什么同样是AI 开发，别人做的页面看起来就很高级，而你的总是差一点感觉？ 其实不是你代码不行，而是你少做了一件事：设计系统搭建。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "穷在街头无人问lhj",
    "platform": "bilibili",
    "points": 10470,
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
    "points": 10231,
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
    "points": 9673,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV195ydBxEfq",
    "domain": "AI",
    "title": "低成本小智MCP服务器",
    "url": "http://www.bilibili.com/video/av115478752140541",
    "source": "小闹一起",
    "platform": "bilibili",
    "points": 9597,
    "published_at": "2025-11-02T06:59:56+00:00",
    "summary": "低成本小智MCP服务器部署\n工具作者https://www.bilibili.com/video/BV1hxMbzqEzU/?spm_id_from=333.1391.0.0\n用到的工具:https://www.123865.com/s/zN6vjv-QH6av"
  },
  {
    "id": "bvid:BV1oXjc6CEWK",
    "domain": "AI",
    "title": "（2026版）这才是B站讲的最好的Vibe Coding企业级项目实战，Claude Code+Codex+Cursor丨一周学完，让你少走99%弯路！",
    "url": "http://www.bilibili.com/video/av116769742195971",
    "source": "京东架构师诸葛",
    "platform": "bilibili",
    "points": 9267,
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
    "points": 8348,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 7783,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1o87764Ebs",
    "domain": "AI",
    "title": "我做 AI Agent 一年,90% 在做表面功夫——直到我换了思路",
    "url": "http://www.bilibili.com/video/av116818060512695",
    "source": "数字黑魔法",
    "platform": "bilibili",
    "points": 7323,
    "published_at": "2026-06-26T23:55:00+00:00",
    "summary": "本视频不构成任何投资建议。DYOR。"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 7074,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 6862,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1Wkjy6gEFx",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战（2026最新版）Claude Code+Codex+Cursor，从环境安装到实战，全部都讲明白了！！",
    "url": "http://www.bilibili.com/video/av116798397616142",
    "source": "程序员码哥",
    "platform": "bilibili",
    "points": 6507,
    "published_at": "2026-06-23T08:12:47+00:00",
    "summary": "B站讲的最好的Vibe Coding企业级项目实战（2026最新版）Claude Code+Codex+Cursor，从环境安装到实战，全部都讲明白了！！\n【视频配套学习笔记、Agent开发、大模型最新学习路线、系统学习、实战案例、电子书+问题解答】都在这了：https://www.bilibili.com/read/cv39979382/"
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
    "id": "rss:https://www.theverge.com/tech/958707/apple-ram-buy-memory-blacklisted-china-cxmt",
    "domain": "大厂 AI 动态",
    "title": "Apple wants permission to buy memory from a blacklisted Chinese supplier",
    "url": "https://www.theverge.com/tech/958707/apple-ram-buy-memory-blacklisted-china-cxmt",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T17:28:18+00:00",
    "summary": "Apple is looking to alleviate some of the pressure on its supply chain by seeking an exception from the Trump administration to buy RAM chips from CXMT, a company blacklisted by the Pentagon over ties"
  },
  {
    "id": "rss:https://www.theverge.com/report/958695/kai-wright-npr-guardian-interview-questionnaire",
    "domain": "大厂 AI 动态",
    "title": "The Guardian&#8217;s Kai Wright refuses to buy a new phone",
    "url": "https://www.theverge.com/report/958695/kai-wright-npr-guardian-interview-questionnaire",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T15:15:00+00:00",
    "summary": "Kai Wright is the co-host of Stateside with Kai and Carter over at the Guardian. But Wright has been bringing his unique insights to listeners for years. He's also hosted Notes From America, The Unite"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/957679/indie-developers-star-fox-games",
    "domain": "大厂 AI 动态",
    "title": "Indie developers got tired of waiting for a new Star Fox, so they’re making their own",
    "url": "https://www.theverge.com/entertainment/957679/indie-developers-star-fox-games",
    "source": "Geoffrey Bunting",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T14:00:00+00:00",
    "summary": "Nostalgia remains a powerful force. So much so that, in exploring the echoes of a late-'90s childhood spent skimming the water of Corneria and sneering \"cocky little freaks!\" in time with a monkey enc"
  },
  {
    "id": "rss:https://www.theverge.com/report/958678/apple-consumer-price-increase-ai-big-tech",
    "domain": "大厂 AI 动态",
    "title": "Why is Apple asking me to pay more for Big Tech’s AI obsession?",
    "url": "https://www.theverge.com/report/958678/apple-consumer-price-increase-ai-big-tech",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T13:30:00+00:00",
    "summary": "Tim Cook recently said price increases were \"unavoidable\" and described the company's pricing as \"unsustainable.\" The 16-inch MacBook Pro saw its price go up by $300. The 11-inch iPad Air went from $5"
  },
  {
    "id": "rss:https://www.theverge.com/tech/958008/matter-unify-conference-csa-apple-google-amazon-samsung-smart-home-interoperability",
    "domain": "大厂 AI 动态",
    "title": "Inside the room where the smart home industry is still betting on Matter",
    "url": "https://www.theverge.com/tech/958008/matter-unify-conference-csa-apple-google-amazon-samsung-smart-home-interoperability",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T13:00:00+00:00",
    "summary": "Four years ago, overlooking a canal in Amsterdam, the smart home industry collectively launched Matter, the one interoperability standard to rule them all. Heralded as the solution to the industry's s"
  },
  {
    "id": "rss:https://www.theverge.com/games/957474/whats-the-password-review-pc-ios-android",
    "domain": "大厂 AI 动态",
    "title": "This puzzle game&#8217;s simple premise hides surprising depth",
    "url": "https://www.theverge.com/games/957474/whats-the-password-review-pc-ios-android",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T12:00:00+00:00",
    "summary": "What's the Password? has a simple concept: To solve each of the game's more than 100 puzzles, you have to type in the right four-digit password on a number pad. That might sound like a limited constra"
  },
  {
    "id": "rss:https://www.theverge.com/tech/958127/google-home-speaker-star-fox-installer",
    "domain": "大厂 AI 动态",
    "title": "This might be the new best smart speaker",
    "url": "https://www.theverge.com/tech/958127/google-home-speaker-star-fox-installer",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T12:00:00+00:00",
    "summary": "Hi, friends! Welcome to Installer No. 134, your guide to the best and Verge-iest stuff in the world. (If you're new here, welcome, hope you're okay in all this heat, and also you can read all the old "
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
    "id": "rss:https://www.producthunt.com/products/supra-player",
    "domain": "大厂 AI 动态",
    "title": "Supra Player",
    "url": "https://www.producthunt.com/products/supra-player",
    "source": "Jesse Ngatai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T21:19:41+00:00",
    "summary": "Compare & Sync Videos Fast Discussion | Link"
  },
  {
    "id": "rss:https://36kr.com/p/3867976058803459?f=rss",
    "domain": "大厂 AI 动态",
    "title": "一折买 Miu Miu，谁在做奢侈品牌的\"拼多多\"？｜商业Friday",
    "url": "https://36kr.com/p/3867976058803459?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T00:37:08+00:00",
    "summary": "文｜贺哲馨 编辑｜乔芊 Judy第一次意识到，原来打折的奢侈品也有准入门槛，是在申请加入On The List的一次特卖活动时。提交申请后的第三天，她依旧没有收到邀请消息。“我还以为填完资料就能进去。”她说。 按照平台规则，特卖活动需要邀请码才能进入。如果迟迟没有通过，则需要邀请两位好友注册，才能获得进入候补名单的机会。至于最终能否收到邀请码，没人说得清楚。 “有点像抽签，也有点像开盲盒。”Jud"
  },
  {
    "id": "rss:https://36kr.com/p/3871109381035011?f=rss",
    "domain": "大厂 AI 动态",
    "title": "秋声 | 大秦储能冲港股IPO：锂价50万山顶囤货血泪史，亏本三年才清完",
    "url": "https://36kr.com/p/3871109381035011?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T07:37:59+00:00",
    "summary": "本文约2500字，建议阅读5分钟 作者&nbsp;|&nbsp;彭孝秋 编者按：AI 大爆发之际，越来越多公司走向资本市场。每一份招股书翻动的声音里，都藏着一家公司想说与未曾明说的全部。 鉴于此，硬氪特推出「秋声」专栏。秋声取自欧阳修《秋声赋》，借“听秋声”之意，观产业冷暖，辨公司成色，记录企业冲刺 IPO 途中那些被写下与被隐藏的真实。这是我们第三期，大秦数字能源。 6月26日，储能公司大秦数字"
  },
  {
    "id": "wscn:3775694",
    "domain": "股票",
    "title": "算力告急：谷歌悄然对Meta实施Gemini使用上限",
    "url": "https://wallstreetcn.com/articles/3775694",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T06:57:01+00:00",
    "summary": "全球AI算力告急！因不堪负荷，谷歌被迫对巨头Meta实施算力限流，致其多个项目延误。这场风波不仅逼迫谷歌急向SpaceX租借算力救场，更倒逼Meta加速转向自研模型。AI推理算力争夺战已全面白热化！"
  },
  {
    "id": "wscn:3775691",
    "domain": "股票",
    "title": "利率破 5，黄金崩？长江证券想证明：加息未必利空黄金",
    "url": "https://wallstreetcn.com/articles/3775691",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T06:40:49+00:00",
    "summary": "“利率破5，黄金必崩”已成历史偏见！在史无前例的“高债务+高利率”共振下，美国巨额利息支出首超国防预算。黄金定价正从“机会成本”向“信用替代”颠覆性切换，高利率持续反噬美元信用，系统性强化黄金中期配置价值。"
  },
  {
    "id": "wscn:3775690",
    "domain": "股票",
    "title": "超万亿美元顺差之后：中国资本输出格局逐渐成形",
    "url": "https://wallstreetcn.com/premium/articles/3775690?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T05:18:51+00:00",
    "summary": "中国正由贸易顺差驱动迈向资本输出时代，人民币国际化逻辑加速转向资本输出、全球投融资与离岸金融生态建设。"
  },
  {
    "id": "wscn:3775689",
    "domain": "股票",
    "title": "美联储的集权式改革以及沃什的阳谋",
    "url": "https://wallstreetcn.com/articles/3775689",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T04:31:07+00:00",
    "summary": "美联储正掀起隐秘的集权风暴！新主席沃什悄然将货币框架转至“稀缺准备金”，近期短端收益率正挂实为资金缺口而非加息预期。此举不仅彻底铲除点阵图根基，更令“资金投放量”重夺定价权。抛弃旧历，紧盯美联储的实际操作才是当下破局关键！"
  },
  {
    "id": "wscn:3775688",
    "domain": "股票",
    "title": "“战略模糊”、“数据驱动”！沃什要做格林斯潘？那“看跌期权”要学吗？",
    "url": "https://wallstreetcn.com/articles/3775688",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T04:11:40+00:00",
    "summary": "美联储新帅沃什全面致敬格林斯潘，重拾“战略模糊”与数据驱动，为市场复刻昔日暴涨繁荣打开想象空间。但暗礁已现：他能否在缔造高增长、低通胀奇迹的同时，避开资产泡沫，并亲手击碎“美联储兜底股市”的危险幻觉？"
  },
  {
    "id": "wscn:3775687",
    "domain": "股票",
    "title": "7月美联储决议前，沃什有两次\"重要亮相\"，下周是第一次！",
    "url": "https://wallstreetcn.com/articles/3775687",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T02:42:34+00:00",
    "summary": "美联储新主席沃什的政策底牌仍是“黑箱”！下周他将迎来海外首秀，与欧英加三大央行巨头同台。面对强劲非农或再燃加息预期及AI过热风险，这场巅峰对话将是市场拿着放大镜“解码”美联储利率路径的最关键窗口。"
  },
  {
    "id": "wscn:3775686",
    "domain": "股票",
    "title": "下周重磅日程：美国非农、中国PMI、沃什出席欧洲央行论坛，半导体“7月涨价潮”",
    "url": "https://wallstreetcn.com/articles/3775686",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T02:26:17+00:00",
    "summary": "下周宏观焦点集中于美国6月非农报告与中国官方PMI，数据将直接关乎美联储加息预期与中国制造业增长成色。事件方面，欧洲央行年度论坛汇聚沃什、拉加德等全球央行舵手，货币政策信号密集。产业端，三星计划宣布历史性的1000万亿韩元本土投资计划，AI需求驱动全球半导体涨价潮7月全面引爆，村田、英飞凌等十余家企业集体提价。"
  },
  {
    "id": "wscn:3775684",
    "domain": "股票",
    "title": "欧洲遭遇史上最严酷热浪，空调卖爆了，美的PortaSlit“二手价格超过新机”",
    "url": "https://wallstreetcn.com/articles/3775684",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T02:00:09+00:00",
    "summary": "极端高温暴露欧洲基建短板，亚洲家电巨头狂揽“气候红利”。美的PortaSlit凭借精准规避严苛法规的免安装设计，强势击穿欧洲制冷市场壁垒。"
  },
  {
    "id": "wscn:3775585",
    "domain": "股票",
    "title": "“K型分化”时代启幕：中国楼市的复苏，不再是一条直线",
    "url": "https://wallstreetcn.com/premium/articles/3775585?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T01:47:37+00:00",
    "summary": "中国地产市场进入K型分化时代。"
  },
  {
    "id": "wscn:3775685",
    "domain": "股票",
    "title": "什么导致本周市场大动荡？高盛合伙人：不是沃什，而是AI再平衡",
    "url": "https://wallstreetcn.com/articles/3775685",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T01:35:23+00:00",
    "summary": "“目前仍是股市在驱动宏观，而非宏观在驱动股市”。这场波动并非AI投资周期终结的信号——\"我们仍处于一场历史性投资热潮的进行之中\"——但市场对这轮热潮中净赢家与净输家的判断，正在经历一次深层次的重估。"
  },
  {
    "id": "wscn:3775683",
    "domain": "股票",
    "title": "特朗普威胁：伊朗或将不复存在；美军连续第二天空袭伊朗，伊朗革命卫队威胁对美军基地发起“地狱”式打击",
    "url": "https://wallstreetcn.com/articles/3775683",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T00:40:02+00:00",
    "summary": "中东地缘风暴升级！特朗普强硬警告“伊朗或将不复存在”，美军连续两天空袭伊朗，霍尔木兹海峡能源动脉拉响警报。同时，以黎停火框架遭真主党强烈抵制。中东火药桶一触即发，全球市场避险情绪或再迎巨震！"
  },
  {
    "id": "wscn:3775485",
    "domain": "股票",
    "title": "mSAP大分歧：精密线路\"最后的堡垒\"，15微米能否重构450亿美元PCB产业链条？",
    "url": "https://wallstreetcn.com/premium/articles/3775485?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-28T00:01:14+00:00",
    "summary": "mSAP工艺已不仅是一项改良技术,而是半导体后道再分布层(RDL)与高端硬件主板融合的核心咽喉。"
  },
  {
    "id": "wscn:3775582",
    "domain": "股票",
    "title": "逼近40年低点！日元跌向162，美日是否会联合干预？",
    "url": "https://wallstreetcn.com/premium/articles/3775582?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T23:59:50+00:00",
    "summary": "日元逼近162干预红线，美日联合干预预期升温，但利差未改，汇率中长期仍面临贬值压力。"
  },
  {
    "id": "wscn:3775504",
    "domain": "股票",
    "title": "钽：AI敞口最大、上涨斜率最陡战略稀有金属，年内为何大涨超150%？",
    "url": "https://wallstreetcn.com/premium/articles/3775504?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T23:51:35+00:00",
    "summary": "2026年，全球钽精矿价格从不到80美元/磅飙升至257.5美元/磅，年内涨幅超150%。这轮暴涨的底层驱动力来自一个历史性的供需错配。"
  },
  {
    "id": "wscn:3775579",
    "domain": "股票",
    "title": "半导体材料\"去日化\"：从依赖到重构，14种日本垄断材料国产替代进行时？",
    "url": "https://wallstreetcn.com/premium/articles/3775579?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T14:09:00+00:00",
    "summary": "日本在19种关键半导体材料中占据14种全球市占率第一，总市场份额达52%，构成中国半导体产业链安全的“命门”。"
  },
  {
    "id": "wscn:3775681",
    "domain": "股票",
    "title": "东鹏饮料回应网络不实传言：相关视频系凭空捏造，已报警追责",
    "url": "https://wallstreetcn.com/articles/3775681",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T11:59:45+00:00",
    "summary": "6月27日，东鹏饮料发布《关于网络不实谣言的澄清声明》，回应近期围绕公司的网络传言。\n东鹏饮料在声明..."
  },
  {
    "id": "wscn:3775680",
    "domain": "股票",
    "title": "下半年美元指数何去何从",
    "url": "https://wallstreetcn.com/articles/3775680",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T11:43:10+00:00",
    "summary": "信达证券认为，全球流动性已触及紧缩区间，地缘冲突推升通胀驱动多国央行转向收紧。历史显示美联储加息周期中美元指数多呈震荡。下半年中东局势缓和或缓解油价压力，美联储加息动力减弱，美元或步入宽幅震荡阶段。"
  },
  {
    "id": "wscn:3775678",
    "domain": "股票",
    "title": "铜价走到哪了？",
    "url": "https://wallstreetcn.com/articles/3775678",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T10:56:18+00:00",
    "summary": "招商宏观认为，铜正从“铜博士”蜕变为战略资源：AI算力与能源转型引爆需求，全球供给受资源集中、开发周期长等令铜市场持续偏紧。短期看，全球逾10家央行已启动加息，流动性边际收紧压制铜价上移空间。但以3—5年维度审视，若29—30年全球步入新一轮康波周期，铜价中枢上行仍值得期待。"
  },
  {
    "id": "wscn:3775679",
    "domain": "股票",
    "title": "美伊交火击碎停火幻象！伊革命卫队实质打击美军据点，霍尔木兹海峡“法理争夺”推升能源断航溢价",
    "url": "https://wallstreetcn.com/articles/3775679",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T09:26:10+00:00",
    "summary": "美伊再度交火：伊朗6月25日以无人机袭击一艘新加坡籍商船，美军26日随即空袭伊朗锡里克地区，伊朗革命卫队随后宣布打击美军在中东多处据点。这是美伊签署谅解备忘录后首次互相动武。双方围绕“谁先违约”展开激烈交锋。冲突升级直接推升霍尔木兹海峡断航风险溢价，对原油、航运及避险资产定价构成压力。"
  },
  {
    "id": "wscn:3775674",
    "domain": "股票",
    "title": "英伟达AI版图再扩张！数据中心以太网交换机收入暴增193%，悄然登顶全球第一",
    "url": "https://wallstreetcn.com/articles/3775674",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-27T09:05:20+00:00",
    "summary": "数据显示，英伟达在Q1 2026首次登顶全球数据中心以太网交换机市场，季度营收21亿美元，同比暴增192.7%，市场份额达21.5%。这是一个传统上由博通、思科等网络巨头主导的领域。而英伟达的核心驱动力是其Spectrum-X平台——专为大规模GPU集群设计的端到端网络方案。"
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
