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

- 今日日期：`2026-07-30`
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
  "date": "2026-07-30",
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
    "points": 3987393,
    "published_at": "2026-01-15T03:56:12+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署"
  },
  {
    "id": "bvid:BV1wt411T7Hy",
    "domain": "AI",
    "title": "3分钟创建你的饥荒联机专属服务器！纯免费！良心教学！steam+wegame均有！【饥荒五耀】",
    "url": "http://www.bilibili.com/video/av62522150",
    "source": "五耀",
    "platform": "bilibili",
    "points": 1779258,
    "published_at": "2019-08-06T14:03:34+00:00",
    "summary": "本期教大家怎么在饥荒联机版中创建自己的服务器，纯免费，良心干货教学！3分钟学会！\nP1是steam版本的创建教学，P2是Wegame版本的创建教学。"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1630762,
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
    "points": 1455128,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1293753,
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
    "points": 1008360,
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
    "points": 999138,
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
    "points": 976110,
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
    "points": 866782,
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
    "points": 575923,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 430022,
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
    "points": 428290,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 418920,
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
    "points": 366679,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1rBRQBSEwB",
    "domain": "AI",
    "title": "Claude Code+DeepSeek V4 Pro安装教程｜3步从零装好开始用 | Mac Windows",
    "url": "http://www.bilibili.com/video/av116543199385810",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 327737,
    "published_at": "2026-05-09T10:10:00+00:00",
    "summary": "上期vibe coding零基础教程10万多人看了，私信和评论里问最多的居然不是怎么写需求。\n 而是Claude Code怎么装？DeepSeek怎么接进去？🫣\n\n所以这期作为补丁教程，专门帮大家搞定这3件事：\n 1️⃣ 安装Claude Code\n 2️⃣ 把DeepSeek V4 Pro百万上下文满血版接入Claude Code\n 3️⃣ 在VS Code里正式用起来\n\nMac和Windows"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 251576,
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
    "points": 211359,
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
    "points": 190575,
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
    "points": 178132,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 152311,
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
    "points": 123351,
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
    "points": 111939,
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
    "points": 92837,
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
    "points": 87192,
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
    "points": 67695,
    "published_at": "2026-07-28T06:41:31+00:00",
    "summary": "如果能把 Codex、Claude Code、Grok、Cursor 等智能编程工具整合到同一个工作环境中，再让多个 Agent 像团队成员一样分工协作，软件开发的效率将得到显著提升。Orca ADE 正是为此而生：它是一款开源、免费的 Agent 开发环境，专注于代码管理与命令行工作流，不仅能够接入多种编程 Agent，还支持语音操作和手机远程管理。接下来，我们就来认识一下 Orca ADE，看"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 63276,
    "published_at": "2026-03-30T16:47:51+00:00",
    "summary": "Everything Claude Code 是目前 GitHub 上 116K star 的 Claude Code 配置项目。本期从斜杠命令、子代理、Hooks 到学习系统，带你把这个项目真正用起来。"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53438,
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
    "points": 47514,
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
    "points": 44536,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1FzfoYSE4f",
    "domain": "AI",
    "title": "影刀AI Power零基础教程：02 智能体——打造企业AI超级员工",
    "url": "http://www.bilibili.com/video/av113888003622214",
    "source": "影刀RPA",
    "platform": "bilibili",
    "points": 41116,
    "published_at": "2025-02-06T02:00:00+00:00",
    "summary": "AI智能体：场景化智能助手，打造企业AI超级员工\n影刀AI Power，帮助企业将AI用起来。让每个员工都能拥有AI能力，在工作中使用AI解决问题。\n\n影刀AP企业版免费试用申请：http://s.winrobot360.com/g02tp\n影刀AP社区版使用：https://www.yingdao.com/ai-power/"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 39398,
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
    "points": 38211,
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
    "points": 33961,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 25799,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 24627,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1w9Nc69EXP",
    "domain": "AI",
    "title": "[电赛AIskill]写0行代码/纯agent速通2024年电赛H题——思路&amp;代码分享",
    "url": "http://www.bilibili.com/video/av116900721922369",
    "source": "3545D",
    "platform": "bilibili",
    "points": 23196,
    "published_at": "2026-07-11T09:56:10+00:00",
    "summary": "使用mspm0-skill速通2024年电赛h题教程/思路，视频内使用的是codex桌面端（现在叫ChatGPT桌面端），天猛星开发板+ccs环境编译+OpenOCD/DAPLink烧录，视频内skill支持各种开发板/工具链/Agent/烧录器/IDE等，详见https://github.com/mc3545dada/mspm0-skill，感兴趣的欢迎交流/Issue/PR/star等，谢谢a"
  },
  {
    "id": "bvid:BV16ggC6DEZK",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116963049212769",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 23115,
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
    "points": 22663,
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
    "points": 21288,
    "published_at": "2024-05-21T05:09:48+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 17161,
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
    "points": 16672,
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
    "points": 15807,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV178Lx6kEeZ",
    "domain": "AI",
    "title": "新手入门 Claude Code 最优搭配   VSCode+Claude Code+DeepS",
    "url": "http://www.bilibili.com/video/av116609704269045",
    "source": "慢炖AI",
    "platform": "bilibili",
    "points": 13717,
    "published_at": "2026-05-21T00:25:36+00:00",
    "summary": "新手入门 Claude Code 最优搭配 —VSCode+Claude Code+DeepSeek V4Pro 完整教程。\n我有三个理由：\n\n首先第一点，安装简单，不用繁琐的配置环境、操作命令，直接在VS code中安装Claude code插件就可以了，2分钟就可以搞定。\n\n第二个理由是在VS code里的操作更方便，不用记那么多命令，另外在左侧还可以清晰的看到文件目录，随时查看和修改里面的内"
  },
  {
    "id": "bvid:BV1vLN769EJa",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！大模型入门到进阶，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116894866677118",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 13031,
    "published_at": "2026-07-10T09:04:48+00:00",
    "summary": "【代码已整理】\n无论你是从零开始开发项目，还是对现有代码进行现代化改造，本课程都能为你提供一套严谨的工作流程，让你按自己的方式构建软件。"
  },
  {
    "id": "bvid:BV1mPkbBhEPX",
    "domain": "AI",
    "title": "我让 AI 自己写Agent Skill，再让 AI 自己调用，真·开始自动干活了？",
    "url": "http://www.bilibili.com/video/av115917476338200",
    "source": "小豹一",
    "platform": "bilibili",
    "points": 11796,
    "published_at": "2026-01-18T18:20:40+00:00",
    "summary": "claude code 仓库：\nhttps://github.com/anthropics/claude-code\n\n智普配置claude code：\nhttps://docs.bigmodel.cn/cn/coding-plan/tool/claude#%E6%96%B9%E5%BC%8F%E4%B8%89%EF%BC%9A%E6%89%8B%E5%8A%A8%E9%85%8D%E7%BD%AE"
  },
  {
    "id": "bvid:BV1dsNv66E3Q",
    "domain": "AI",
    "title": "【Cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116922599344955",
    "source": "六月要癫",
    "platform": "bilibili",
    "points": 11545,
    "published_at": "2026-07-15T06:39:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 10863,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9247,
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
    "points": 8803,
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
    "points": 8033,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
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
    "id": "rss:https://www.eetimes.com/iot-tech-expo-europe-returns-to-amsterdam-as-industrial-ai-and-edge-intelligence-reshape-connected-industry/",
    "domain": "AI 算力 / 半导体",
    "title": "IoT Tech Expo Europe Returns to Amsterdam as Industrial AI and Edge Intelligence Reshape Connected Industry",
    "url": "https://www.eetimes.com/iot-tech-expo-europe-returns-to-amsterdam-as-industrial-ai-and-edge-intelligence-reshape-connected-industry/",
    "source": "IoT Tech Expo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T00:42:04+00:00",
    "summary": "https://www.iottechexpo.com/europe/ From autonomous factories and AI-powered robots to connected vehicles and smart cities, organizations are entering a new era where connected systems are expected no"
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
    "summary": "Date: Wednesday, August 19, 2026 or Wednesday, August 26, 2026 This webcast will explain how and why Easy Drive SAR ADCs from Analog Devices can deliver the precision you need without the headache of "
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
    "id": "rss:https://www.eetimes.com/microchip-acquires-edge-ai-chip-startup-hailo/",
    "domain": "AI 算力 / 半导体",
    "title": "Microchip Acquires Edge AI Chip Startup Hailo",
    "url": "https://www.eetimes.com/microchip-acquires-edge-ai-chip-startup-hailo/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T17:04:30+00:00",
    "summary": "Return to playbook for the acquisition-driven embedded giant. The post Microchip Acquires Edge AI Chip Startup Hailo appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/how-to-build-a-100gbps-server-grade-aoi-platform-for-next-generation-semiconductor-inspection/",
    "domain": "AI 算力 / 半导体",
    "title": "How to Build a 100Gbps Server-Grade AOI Platform for Next-Generation Semiconductor Inspection",
    "url": "https://www.eetimes.com/how-to-build-a-100gbps-server-grade-aoi-platform-for-next-generation-semiconductor-inspection/",
    "source": "ADLINK",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T14:00:00+00:00",
    "summary": "Discover how to overcome the bandwidth, scalability, thermal, and system integration challenges of modern AI-powered AOI. This white paper explains how server-grade architecture, high-speed frame grab"
  },
  {
    "id": "rss:https://www.eetimes.com/vibe-coding-in-safety-critical-software-promise-pitfalls-and-a-path-forward/",
    "domain": "AI 算力 / 半导体",
    "title": "Vibe Coding in Safety-Critical Software: Promise, Pitfalls, and a Path Forward",
    "url": "https://www.eetimes.com/vibe-coding-in-safety-critical-software-promise-pitfalls-and-a-path-forward/",
    "source": "Miroslaw Zielinski, director of product management, Parasoft.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T13:52:38+00:00",
    "summary": "Vibe coding can’t fly solo in safety-critical software; demand deterministic gates, human review, and proof before trusting AI-generated code. The post Vibe Coding in Safety-Critical Software: Promise"
  },
  {
    "id": "rss:https://www.eetimes.com/will-purging-chinese-tech-cost-europe-its-digital-future/",
    "domain": "AI 算力 / 半导体",
    "title": "Will Purging Chinese Tech Cost Europe Its Digital Future?",
    "url": "https://www.eetimes.com/will-purging-chinese-tech-cost-europe-its-digital-future/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T08:19:26+00:00",
    "summary": "The EU faces challenges in building its digital defenses, as the cost of replacing Chinese telecom equipment across Europe could reach $46 billion. The post Will Purging Chinese Tech Cost Europe Its D"
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
    "title": "Nvidia employee implicated in escalating Supermicro smuggling scandal, but demand only intensifies for Nvidia hardware",
    "url": "https://www.tomshardware.com/tech-industry/nvidia-employee-implicated-in-escalating-supermicro-smuggling-scandal-but-demand-only-intensifies-for-nvidia-hardware",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T15:10:06+00:00",
    "summary": "An Nvidia employee has been implicated in the Supermicro smuggling scandal, with his home and desk searched. He's been detained over allegations of forgery and breach of trust. Meanwhile, Nvidia is co"
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
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/msi-cubi-nuc-ai-3mg-review",
    "domain": "AI 算力 / 半导体",
    "title": "MSI Cubi NUC AI+ 3MG review: Panther Lake in an understated mini PC",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/msi-cubi-nuc-ai-3mg-review",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T13:00:00+00:00",
    "summary": "The MSI Cubi NUC AI+ 3MG is a compact, understated design, providing an Intel Core Ultra 9 386H in a tiny desktop. It’s easy to upgrade and relatively quiet but could do with a few more ports at the b"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/how-to-buy-second-hand-pc-hardware-without-getting-scammed-essential-rules-of-engagement-for-finding-used-parts-and-machines-in-an-inflated-market",
    "domain": "AI 算力 / 半导体",
    "title": "How to buy second-hand PC hardware without getting scammed — essential rules of engagement for finding used parts and machines in an inflated market",
    "url": "https://www.tomshardware.com/pc-components/how-to-buy-second-hand-pc-hardware-without-getting-scammed-essential-rules-of-engagement-for-finding-used-parts-and-machines-in-an-inflated-market",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T12:07:36+00:00",
    "summary": "Buying second-hand can be a great way to pick up a bargain on PC hardware, but you'll need to keep this advice in mind to make sure you avoid the scams."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/sk-hynix-operating-profit-rises-557-percent",
    "domain": "AI 算力 / 半导体",
    "title": "Memory maker SK hynix's profit rises 557% amid global shortage, expansion costs climb to $27 billion — shares slide despite mammoth earnings as expectations outpace reality and global AI selloffs cont",
    "url": "https://www.tomshardware.com/tech-industry/sk-hynix-operating-profit-rises-557-percent",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T11:56:18+00:00",
    "summary": "SK hynix has reported second-quarter revenue of 79.32 trillion won, and operating profit of 60.54 trillion won, the latter up 557% year over year."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/three-us-states-to-deploy-60mph-drones-armed-with-pepper-spray-to-neutralize-school-shooters-campus-guardian-angel-drones-can-also-smash-windows-and-ram-attackers",
    "domain": "AI 算力 / 半导体",
    "title": "Three US states to deploy 60mph drones armed with pepper spray to neutralize school shooters — ‘Campus Guardian Angel’ drones can also smash windows and ram attackers",
    "url": "https://www.tomshardware.com/tech-industry/drones/three-us-states-to-deploy-60mph-drones-armed-with-pepper-spray-to-neutralize-school-shooters-campus-guardian-angel-drones-can-also-smash-windows-and-ram-attackers",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T11:36:04+00:00",
    "summary": "The drone arms race is set to enter U.S. schools with Mithril Defense’s Campus Guardian Angel drones in at least nine schools across three states before the year is out."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/webcams/how-to-look-better-on-webcam-tips-for-the-average-person-to-look-better-and-more-professional",
    "domain": "AI 算力 / 半导体",
    "title": "How to look better on webcam — tips for the average person to look better and more professional",
    "url": "https://www.tomshardware.com/peripherals/webcams/how-to-look-better-on-webcam-tips-for-the-average-person-to-look-better-and-more-professional",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T11:32:03+00:00",
    "summary": "Some tips for the average non-streaming webcam user to look better and more professional."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intels-upcoming-nova-lake-desktop-sku-to-require-65w-of-separate-power-delivery-for-its-igpu-leaker-claims-beefy-integrated-graphics-could-require-two-vccgt-phases-for-12-xe3p-cores",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's upcoming Nova Lake desktop SKU to require 65W of separate power delivery for its iGPU, leaker claims — beefy integrated graphics could require two VCCGT phases for 12 Xe3P cores",
    "url": "https://www.tomshardware.com/pc-components/cpus/intels-upcoming-nova-lake-desktop-sku-to-require-65w-of-separate-power-delivery-for-its-igpu-leaker-claims-beefy-integrated-graphics-could-require-two-vccgt-phases-for-12-xe3p-cores",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T11:01:22+00:00",
    "summary": "Intel seems to be working on a 16-core Nova Lake desktop APU with 12 Xe3P cores that will require 65W of power delivery on their own to achieve maximum performance. Two separate VCCGT phases will be n"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/get-usd180-of-3d-printing-filament-for-just-usd86-in-this-ebay-blowout-save-52-percent-on-10-reels-of-crealitys-hyper-pla-just-usd8-63-a-spool",
    "domain": "AI 算力 / 半导体",
    "title": "Get $180 of 3D printing filament for just $86 in this eBay blowout — save 52% on 10 reels of Creality's Hyper PLA, just $8.63 a spool",
    "url": "https://www.tomshardware.com/3d-printing/get-usd180-of-3d-printing-filament-for-just-usd86-in-this-ebay-blowout-save-52-percent-on-10-reels-of-crealitys-hyper-pla-just-usd8-63-a-spool",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T10:57:04+00:00",
    "summary": "Stock up on your favorite colors in this unbelievable Creality Hyper PLA filament bundle deal. Save 52% on 10 spools of high-speed printing plastics."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/state-of-play-ssd-pricing-one-year-into-the-ai-component-crisis-220-percent-price-increases-are-crippling-the-diy-market",
    "domain": "AI 算力 / 半导体",
    "title": "State of play: SSD pricing one year into the AI component crisis — 220% price increases are crippling the DIY market",
    "url": "https://www.tomshardware.com/pc-components/ssds/state-of-play-ssd-pricing-one-year-into-the-ai-component-crisis-220-percent-price-increases-are-crippling-the-diy-market",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T10:52:51+00:00",
    "summary": "We look at the state of SSD pricing one year into the AI apocalypse."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/dram-chip-supply-to-module-makers-could-drop-by-more-than-70-percent-year-on-year-in-2027-says-apacer-ceo-demand-for-hbm-and-server-ram-continues-to-devour-manufacturing-capacity",
    "domain": "AI 算力 / 半导体",
    "title": "DRAM chip supply to module makers could drop by more than 70% year-on-year in 2027, says Apacer CEO — demand for HBM and server RAM continues to devour manufacturing capacity",
    "url": "https://www.tomshardware.com/pc-components/ram/dram-chip-supply-to-module-makers-could-drop-by-more-than-70-percent-year-on-year-in-2027-says-apacer-ceo-demand-for-hbm-and-server-ram-continues-to-devour-manufacturing-capacity",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T10:30:00+00:00",
    "summary": "Apacer warns DRAM allocations to module makers could fall below 30% of 2026 levels as AI demand tightens supply and pushes memory prices higher."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-up-to-usd700-on-these-ibuypower-gaming-pcs-fitted-with-an-rx-9070-xt-for-4k-gaming-liquid-cooled-amd-rigs-feature-either-a-9800x3d-or-9900x-cpu-along-with-32gb-ddr5-and-a-1tb-ssd-starting-from-usd1-799",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to $700 on these iBuyPower gaming PCs, fitted with an RX 9070 XT for 4K gaming — liquid-cooled AMD rigs feature either a 9800X3D or 9900X CPU, along with 32GB DDR5 and a 1TB SSD, starting from",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-up-to-usd700-on-these-ibuypower-gaming-pcs-fitted-with-an-rx-9070-xt-for-4k-gaming-liquid-cooled-amd-rigs-feature-either-a-9800x3d-or-9900x-cpu-along-with-32gb-ddr5-and-a-1tb-ssd-starting-from-usd1-799",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T10:09:58+00:00",
    "summary": "Two iBuyPower rigs are on offer at Walmart right now, both fitted with an AMD Radeon RX 9070 XT, in a deal that could save you up to $700 on a 4K-ready gaming PC."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-moonshot-ai-reportedly-used-nvidia-blackwell-chips-for-training-kimi-k3-company-circumvented-both-u-s-export-and-chinese-import-controls-to-acquire-compute",
    "domain": "AI 算力 / 半导体",
    "title": "China's Moonshot AI reportedly used Nvidia Blackwell chips for training Kimi K3 — company circumvented both U.S. export and Chinese import controls to acquire compute",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-moonshot-ai-reportedly-used-nvidia-blackwell-chips-for-training-kimi-k3-company-circumvented-both-u-s-export-and-chinese-import-controls-to-acquire-compute",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T10:00:00+00:00",
    "summary": "Moonshot AI reportedly used Nvidia Blackwell chips for training Kimi K3 — potentially circumventing both U.S. export and Chinese import controls"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/intel-closes-out-the-defense-program-that-paid-nvidia-and-others-to-run-test-chips-on-18a",
    "domain": "AI 算力 / 半导体",
    "title": "Intel closes out RAMP-C production pilot that paid Nvidia and others to run test chips on 18A — program helped lay a path for secure domestic chip production on advanced processes",
    "url": "https://www.tomshardware.com/tech-industry/intel-closes-out-the-defense-program-that-paid-nvidia-and-others-to-run-test-chips-on-18a",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T09:30:00+00:00",
    "summary": "Intel Foundry says that it has completed RAMP-C, the U.S. defense program awarded to the company in 2021 to stand up a domestic leading-edge chip ecosystem on its 18A process."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/developer-uses-ai-to-bring-a-native-version-of-the-legend-of-zelda-ocarina-of-time-to-ios-no-emulation-required-to-play-one-of-gamings-all-time-greats-on-an-iphone-or-ipad",
    "domain": "AI 算力 / 半导体",
    "title": "Developer uses AI to bring a native version of The Legend of Zelda: Ocarina of Time to iOS — no emulation required to play one of gaming's all-time greats on an iPhone or iPad",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/developer-uses-ai-to-bring-a-native-version-of-the-legend-of-zelda-ocarina-of-time-to-ios-no-emulation-required-to-play-one-of-gamings-all-time-greats-on-an-iphone-or-ipad",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T09:00:00+00:00",
    "summary": "A developer has used OpenAI's Codex and GPT-5.6 Sol to help port a native version of The Legend of Zelda: Ocarina of Time to iOS and iPadOS devices."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/an-affordable-oled-laptop-for-just-usd699-acers-swift-go-16-ai-back-to-school-deal",
    "domain": "AI 算力 / 半导体",
    "title": "An affordable OLED laptop for just $699 — Acer's Swift Go 16 AI is the perfect back-to-school deal",
    "url": "https://www.tomshardware.com/laptops/an-affordable-oled-laptop-for-just-usd699-acers-swift-go-16-ai-back-to-school-deal",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T16:53:03+00:00",
    "summary": "Get ready to head back to school with this $300 saving on Acer's excellent Swift Go 16 AI laptop with an OLED screen."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/mystery-reviewer-finds-nvidia-rtx-spark-prototype-laptop-and-puts-it-through-its-paces-microsoft-surface-laptop-ultra-with-nvidia-n1x-chip-shows-promise-though-prototype-warts-are-still-quite-visible",
    "domain": "AI 算力 / 半导体",
    "title": "Mystery reviewer 'finds' Nvidia RTX Spark prototype laptop and puts it through its paces — Microsoft Surface Laptop Ultra with Nvidia N1X chip shows promise, though prototype warts are still quite vis",
    "url": "https://www.tomshardware.com/laptops/mystery-reviewer-finds-nvidia-rtx-spark-prototype-laptop-and-puts-it-through-its-paces-microsoft-surface-laptop-ultra-with-nvidia-n1x-chip-shows-promise-though-prototype-warts-are-still-quite-visible",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T16:03:23+00:00",
    "summary": "Techie \"finds\" Nvidia RTX Spark prototype laptop and puts it through its paces — Microsoft Surface Laptop Ultra with Nvidia N1X chip shows promise, though prototype warts are still quite visible"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/sam-altman-says-ai-has-entered-the-singularity",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI CEO Sam Altman says AI has entered the singularity — two weeks after OpenAI models cheated a benchmark by hacking Hugging Face",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/sam-altman-says-ai-has-entered-the-singularity",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T14:56:22+00:00",
    "summary": "OpenAI CEO Sam Altman recently declared on the Relentless podcast that artificial intelligence has entered the technological singularity."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/one-year-into-the-ai-induced-ram-apocalypse-how-much-does-memory-actually-cost-and-is-there-hope-for-a-more-affordable-future",
    "domain": "AI 算力 / 半导体",
    "title": "One year into the AI-induced RAM apocalypse — how much does memory actually cost, and is there hope for a more affordable future?",
    "url": "https://www.tomshardware.com/pc-components/ram/one-year-into-the-ai-induced-ram-apocalypse-how-much-does-memory-actually-cost-and-is-there-hope-for-a-more-affordable-future",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T14:24:28+00:00",
    "summary": "We look at the state of the DIY RAM market over the last 12 months."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/apple-launches-official-program-for-leasing-macs-as-ai-price-crunch-bites-24-and-36-month-leasing-options-provided-by-klarna",
    "domain": "AI 算力 / 半导体",
    "title": "Apple launches official program for leasing Macs as AI price crunch bites — 24- and 36-month leasing options provided by Klarna",
    "url": "https://www.tomshardware.com/laptops/macbooks/apple-launches-official-program-for-leasing-macs-as-ai-price-crunch-bites-24-and-36-month-leasing-options-provided-by-klarna",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T14:23:59+00:00",
    "summary": "Apple launched its Upgrade program in the US, a partnership with Klarna to lease Macs along with iPads, Watches, and iPhones."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/the-neo-geo-aes-retro-console-is-now-available-to-pre-order-starting-from-usd249-game-cartridges-cost-usd90-each-the-ultimate-edition-with-all-games-and-accessories-will-run-you-usd1-000",
    "domain": "AI 算力 / 半导体",
    "title": "The Neo Geo AES+ retro console is now available to pre-order starting from $249 — game cartridges cost $90 each; the Ultimate Edition with all games and accessories will run you $1,000",
    "url": "https://www.tomshardware.com/video-games/console-gaming/the-neo-geo-aes-retro-console-is-now-available-to-pre-order-starting-from-usd249-game-cartridges-cost-usd90-each-the-ultimate-edition-with-all-games-and-accessories-will-run-you-usd1-000",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T13:52:49+00:00",
    "summary": "How far are you willing to go for physical media? That's the question the Neo Geo AES+ asks above anything else, given the $90 price tags of its game cartridges. Though, comparing it to its original p"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/acer-prodesigner-pe320qxt-professional-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Acer ProDesigner PE320QXT professional monitor review: Touchscreen functionality with a 6K resolution",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/acer-prodesigner-pe320qxt-professional-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T13:30:00+00:00",
    "summary": "Acer takes a unique approach to professional displays with its ProDesigner PE320QXT. It’s a 6K 6016x3384 IPS panel with a touchscreen, webcam, tablet-style stand and a large color gamut for content cr"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/motherboard-vrm-thermal-testing-budget-vs-high-end-boards-does-it-really-matter",
    "domain": "AI 算力 / 半导体",
    "title": "Motherboard VRM thermal testing – budget vs. high-end boards, does it really matter?",
    "url": "https://www.tomshardware.com/pc-components/motherboards/motherboard-vrm-thermal-testing-budget-vs-high-end-boards-does-it-really-matter",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T12:43:16+00:00",
    "summary": "Not all motherboard VRMs are created equal. We break down the differences between budget and premium designs, how they can affect CPU performance, and whether paying more is actually worth it."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/testing-old-drives-as-external-storage-to-avoid-price-hikes-hard-drive-sata-ssd-and-nvme-in-enclosures-up-to-80-gbps-tested",
    "domain": "AI 算力 / 半导体",
    "title": "Testing old drives as external storage to avoid price hikes — hard drive, SATA SSD, and NVMe in enclosures up to 80 Gbps, tested",
    "url": "https://www.tomshardware.com/pc-components/storage/testing-old-drives-as-external-storage-to-avoid-price-hikes-hard-drive-sata-ssd-and-nvme-in-enclosures-up-to-80-gbps-tested",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T11:39:52+00:00",
    "summary": "For as little as $10 (or less on sale), you can use an old drive as external storage, but will that dusty drive deliver the speed you need?"
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
    "id": "hn:49096188",
    "domain": "大厂 AI 动态",
    "title": "Document-borne AI worms can self-propagate through Copilot for Word",
    "url": "https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/",
    "source": "Canopy9560",
    "platform": "hackernews",
    "points": 358,
    "published_at": "2026-07-29T11:44:33+00:00",
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
    "points": 196,
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
    "id": "hn:49088771",
    "domain": "大厂 AI 动态",
    "title": "Show HN: Minute – Offline meeting notes on macOS with Whisper and llama.cpp",
    "url": "https://github.com/mraza007/minute",
    "source": "mraza007",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-28T19:31:17+00:00",
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
    "id": "rss:https://www.theverge.com/tech/972927/microsoft-copilot-super-app-confirmed",
    "domain": "大厂 AI 动态",
    "title": "Microsoft confirms Copilot ‘super app’ coming this year",
    "url": "https://www.theverge.com/tech/972927/microsoft-copilot-super-app-confirmed",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T22:17:38+00:00",
    "summary": "Microsoft is working on an AI \"super app\" that combines Copilot's chat, coding, and agentic capabilities. During an earnings call on Wednesday, Microsoft CEO Satya Nadella said the app will span \"both"
  },
  {
    "id": "rss:https://www.theverge.com/tech/972294/meta-q2-2026-earnings-mark-zuckerberg-personal-ai-agents",
    "domain": "大厂 AI 动态",
    "title": "Mark Zuckerberg is planning a big push into personal AI agents",
    "url": "https://www.theverge.com/tech/972294/meta-q2-2026-earnings-mark-zuckerberg-personal-ai-agents",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T21:48:07+00:00",
    "summary": "Meta is all-in on AI, and sometime soon, the company is going to make a big push into personal AI agents that can do things on your behalf. On Wednesday's Q2 2026 earnings call, CEO Mark Zuckerberg pr"
  },
  {
    "id": "rss:https://www.theverge.com/tech/972894/qualcomm-price-hikes-q2-2026-earnings",
    "domain": "大厂 AI 动态",
    "title": "Qualcomm is raising phone chip prices starting September 1st",
    "url": "https://www.theverge.com/tech/972894/qualcomm-price-hikes-q2-2026-earnings",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T21:41:56+00:00",
    "summary": "RAMageddon won't be the only reason your next phone costs more - Qualcomm is about to raise prices on all its processors, as well. Qualcomm CEO Cristiano Amon said on Wednesday that \"prices are going "
  },
  {
    "id": "rss:https://www.theverge.com/policy/972850/xai-grok-minnesota-nudification-lawsuit",
    "domain": "大厂 AI 动态",
    "title": "xAI’s last-minute scramble to stop Minnesota’s anti-nudification app law",
    "url": "https://www.theverge.com/policy/972850/xai-grok-minnesota-nudification-lawsuit",
    "source": "Sarah Jeong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T21:06:52+00:00",
    "summary": "xAI is suing Minnesota Attorney General Keith Ellison over a law passed back in May that broadly targets \"nudification\" apps, claiming that the statute's punitive provisions leave the company with \"no"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/972777/cyberpunk-2077-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Cyberpunk 2077 packs a lot of fun into its discounted $20 price",
    "url": "https://www.theverge.com/gadgets/972777/cyberpunk-2077-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T21:02:50+00:00",
    "summary": "Over the last few years, CD Projekt Red put a ton of work into fixing Cyberpunk 2077, squashing bugs, polishing content, and even launching new DLC in 2023, Phantom Liberty. As a result, this game has"
  },
  {
    "id": "rss:https://www.theverge.com/tech/972738/xbox-revenue-microsoft-earnings-q4-2026",
    "domain": "大厂 AI 动态",
    "title": "Xbox revenue drops 10 percent as Microsoft&#8217;s cloud and AI business surges",
    "url": "https://www.theverge.com/tech/972738/xbox-revenue-microsoft-earnings-q4-2026",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T20:26:48+00:00",
    "summary": "Xbox is having yet another tough quarter, as revenue from content and services like its Game Pass subscription dipped 10 percent over the past few months. At the same time, Xbox hardware sales decline"
  },
  {
    "id": "rss:https://www.theverge.com/tech/972583/apple-upgrade-program-deal",
    "domain": "大厂 AI 动态",
    "title": "What’s the catch with the Apple Upgrade program?",
    "url": "https://www.theverge.com/tech/972583/apple-upgrade-program-deal",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T18:40:06+00:00",
    "summary": "Apple's new Upgrade program is here, allowing you to lease select models of iPhones, iPads, Macs, and Watches with a relatively low monthly payment. The company promises you won't pay more than the fu"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/972709/openai-hardware-greg-brockman-interview",
    "domain": "大厂 AI 动态",
    "title": "OpenAI president says it&#8217;s &#8216;building a family of devices&#8217; for its AI chatbots",
    "url": "https://www.theverge.com/ai-artificial-intelligence/972709/openai-hardware-greg-brockman-interview",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T18:15:02+00:00",
    "summary": "In an interview with our friend Joanna Stern on her YouTube channel, OpenAI president Greg Brockman said the company is working on a \"family of devices\" for interacting with its AI models. However, Br"
  },
  {
    "id": "rss:https://www.theverge.com/policy/972312/us-robot-ban-sweep-up-chinese-vacuums",
    "domain": "大厂 AI 动态",
    "title": "The US government just banned Roombas",
    "url": "https://www.theverge.com/policy/972312/us-robot-ban-sweep-up-chinese-vacuums",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T18:13:09+00:00",
    "summary": "When the Trump administration announced yesterday that it was banning \"advanced robotic devices\" from entering the United States, the headlines were all about humanoids. But spying doesn't require leg"
  },
  {
    "id": "rss:https://www.theverge.com/policy/972607/full-school-day-cell-phone-bans-are-more-popular-than-ever",
    "domain": "大厂 AI 动态",
    "title": "Full school day cellphone bans are more popular than ever",
    "url": "https://www.theverge.com/policy/972607/full-school-day-cell-phone-bans-are-more-popular-than-ever",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T16:42:44+00:00",
    "summary": "As schools across the country continue to implement cellphone bans, a new Pew Research Center survey shows they continue to gain support. Seventy-seven percent of US adults support banning cellphones "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/microsoft-is-openly-competing-with-openai-anthropic-more-than-ever/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft is openly competing with OpenAI, Anthropic more than ever",
    "url": "https://techcrunch.com/2026/07/29/microsoft-is-openly-competing-with-openai-anthropic-more-than-ever/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T00:21:06+00:00",
    "summary": "Microsoft pitched its own homegrown AI models, harnesses, and even a Mythos competitor on Wednesday, telling Wall Street it plans for continued growth."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/mark-zuckerberg-predicts-that-billions-of-people-will-have-personal-ai-agents-in-five-years/",
    "domain": "大厂 AI 动态",
    "title": "Mark Zuckerberg predicts that billions of people will have personal AI agents in five years",
    "url": "https://techcrunch.com/2026/07/29/mark-zuckerberg-predicts-that-billions-of-people-will-have-personal-ai-agents-in-five-years/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T23:00:11+00:00",
    "summary": "As Meta pours billions into AI infrastructure and agents, Zuckerberg is working to convince investors that the payoff will be worth the price."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/microsoft-logs-3-2b-from-anthropic-investment-but-openai-was-a-mixed-bag/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft logs $3.2B from Anthropic investment, but OpenAI was a mixed bag",
    "url": "https://techcrunch.com/2026/07/29/microsoft-logs-3-2b-from-anthropic-investment-but-openai-was-a-mixed-bag/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T22:46:03+00:00",
    "summary": "When Microsoft reported killer fourth-quarter earnings for its fiscal 2026 year (which ended June 30), it tucked in an interesting little tidbit about how its investments in the two biggest, and compe"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/zuckerberg-says-metas-enterprise-ai-opportunity-extends-beyond-agents/",
    "domain": "大厂 AI 动态",
    "title": "Zuckerberg says Meta’s enterprise AI opportunity extends beyond agents",
    "url": "https://techcrunch.com/2026/07/29/zuckerberg-says-metas-enterprise-ai-opportunity-extends-beyond-agents/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T22:23:12+00:00",
    "summary": "On the company’s second-quarter earnings call Wednesday, CEO Mark Zuckerberg said Meta sees a “large enterprise opportunity” spanning AI agents, APIs, compute, and internal software."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/discover-whats-next-for-ai-from-the-saas-reckoning-to-the-agent-security-gap-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Discover what’s next for AI, from the SaaS reckoning to the agent security gap, at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/07/29/discover-whats-next-for-ai-from-the-saas-reckoning-to-the-agent-security-gap-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T21:16:39+00:00",
    "summary": "At TechCrunch Disrupt 2026, the AI Stage is back to dig into the single hottest topic in the community for the past few years, presented by Google for Startups."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/thinking-machines-co-founder-lilian-weng-left-the-company-citing-health-reasons-then-joined-openai/",
    "domain": "大厂 AI 动态",
    "title": "Thinking Machines co-founder Lilian Weng left the company citing health reasons, then joined OpenAI",
    "url": "https://techcrunch.com/2026/07/29/thinking-machines-co-founder-lilian-weng-left-the-company-citing-health-reasons-then-joined-openai/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T21:07:48+00:00",
    "summary": "Weng previously served as the VP of AI Safety Research at OpenAI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/winamp-aims-for-a-comeback-with-a-new-music-player-powered-by-deezer/",
    "domain": "大厂 AI 动态",
    "title": "Winamp aims for a comeback with a new music player powered by Deezer",
    "url": "https://techcrunch.com/2026/07/29/winamp-aims-for-a-comeback-with-a-new-music-player-powered-by-deezer/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T21:02:12+00:00",
    "summary": "Winamp is preparing to relaunch with a Deezer-powered premium music service, betting its nostalgic brand and a new all-in-one music player can stand out in today’s crowded streaming market."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/the-hugging-face-ai-break-in-as-told-through-an-increasingly-committed-bear-metaphor/",
    "domain": "大厂 AI 动态",
    "title": "The Hugging Face AI break-in explained",
    "url": "https://techcrunch.com/2026/07/29/the-hugging-face-ai-break-in-as-told-through-an-increasingly-committed-bear-metaphor/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T19:44:49+00:00",
    "summary": "Another way to think about the whole thing is to picture a bear at a campsite. (Really, we are going there.)"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/claude-opus-5-became-downright-ruthless-when-tasked-with-running-a-vending-machine/",
    "domain": "大厂 AI 动态",
    "title": "Claude Opus 5 became downright ruthless when tasked with running a vending machine",
    "url": "https://techcrunch.com/2026/07/29/claude-opus-5-became-downright-ruthless-when-tasked-with-running-a-vending-machine/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T18:45:27+00:00",
    "summary": "Andon Labs' latest vending machine simulation shows Opus 5 lied and colluded its way to become the best AI capitalist ever."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/sorry-haters-ferraris-first-ev-is-doing-just-fine/",
    "domain": "大厂 AI 动态",
    "title": "Sorry, haters. Ferrari’s first EV is doing just fine",
    "url": "https://techcrunch.com/2026/07/29/sorry-haters-ferraris-first-ev-is-doing-just-fine/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T17:57:45+00:00",
    "summary": "To the horror of commenters across the internet, the Ferrari Luce appears to be a sales success."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/waymo-robotaxis-are-starting-to-return-to-freeways/",
    "domain": "大厂 AI 动态",
    "title": "Waymo robotaxis are starting to return to freeways",
    "url": "https://techcrunch.com/2026/07/29/waymo-robotaxis-are-starting-to-return-to-freeways/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T17:50:57+00:00",
    "summary": "The freeway pause — and its restart — comes amid increased scrutiny into Waymo and other robotaxi operators, particularly over how these self-driving vehicles behave in certain high-traffic situations"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/us-government-bans-new-foreign-made-humanoids-robot-dogs-and-solar-inverters-citing-risks-to-national-security/",
    "domain": "大厂 AI 动态",
    "title": "US government bans new foreign-made humanoids, robot dogs, and solar inverters, citing risks to national security",
    "url": "https://techcrunch.com/2026/07/29/us-government-bans-new-foreign-made-humanoids-robot-dogs-and-solar-inverters-citing-risks-to-national-security/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T17:41:09+00:00",
    "summary": "The ban largely affects U.S. imports from China, which currently dominates the global market for making humanoid robots and solar inverters."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/google-is-rolling-out-its-age-assurance-tech-for-apps-worldwide-by-year-end/",
    "domain": "大厂 AI 动态",
    "title": "Google brings its age-assurance technology to Android developers worldwide",
    "url": "https://techcrunch.com/2026/07/29/google-is-rolling-out-its-age-assurance-tech-for-apps-worldwide-by-year-end/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T17:00:00+00:00",
    "summary": "Google is expanding its Play Age Signals API, giving Android developers a privacy-preserving way to tailor experiences based on users’ age ranges."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/elon-musks-x-settles-multiyear-legal-battle-with-the-world-federation-of-advertisers/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk’s X settles multiyear legal battle with the World Federation of Advertisers",
    "url": "https://techcrunch.com/2026/07/29/elon-musks-x-settles-multiyear-legal-battle-with-the-world-federation-of-advertisers/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T15:36:48+00:00",
    "summary": "X sued the WFA in 2024 for conducting what it called a \"systematic illegal boycott\" of the platform after it saw a decline in advertising revenue following Musk's $44 billion takeover of the social ne"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/hint-a-new-ai-startup-co-founded-by-martha-stewart-offers-an-ai-assistant-for-homeowners/",
    "domain": "大厂 AI 动态",
    "title": "Hint, a new AI startup co-founded by Martha Stewart, offers an AI assistant for homeowners",
    "url": "https://techcrunch.com/2026/07/29/hint-a-new-ai-startup-co-founded-by-martha-stewart-offers-an-ai-assistant-for-homeowners/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T15:35:09+00:00",
    "summary": "AI home management startup Hint, co-founded by Martha Stewart, wants to become an “AI for your home,” combining property records, maintenance schedules, home documents, and an AI assistant into a sing"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/perplexity-employee-who-worked-on-comet-launches-an-ai-browser-aimed-at-knowledge-work/",
    "domain": "大厂 AI 动态",
    "title": "Perplexity employee who worked on Comet launches an AI browser aimed at knowledge work",
    "url": "https://techcrunch.com/2026/07/29/perplexity-employee-who-worked-on-comet-launches-an-ai-browser-aimed-at-knowledge-work/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T15:00:00+00:00",
    "summary": "Polar has come out with an AI-first browser aimed at knowledge workers, and it has now raised a $5.7 million seed round led by Madrona."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/encore-ai-raises-30m-to-build-ai-agents-that-learn-from-customer-calls/",
    "domain": "大厂 AI 动态",
    "title": "Encore AI raises $30M to build AI agents that learn from customer calls",
    "url": "https://techcrunch.com/2026/07/29/encore-ai-raises-30m-to-build-ai-agents-that-learn-from-customer-calls/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T14:41:06+00:00",
    "summary": "The startup analyzes calls, messages, and CRM data to identify effective sales techniques and turn them into playbooks for AI agents."
  },
  {
    "id": "rss:https://techcrunch.com/video/no-ones-making-a-phone-like-this-lights-co-founders-on-building-for-the-anti-smartphone-generation/",
    "domain": "大厂 AI 动态",
    "title": "‘No one’s making a phone like this’: Light’s co-founders on building for the anti-smartphone generation",
    "url": "https://techcrunch.com/video/no-ones-making-a-phone-like-this-lights-co-founders-on-building-for-the-anti-smartphone-generation/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T14:00:00+00:00",
    "summary": "With the&#160;Light Phone,&#160;Kaiwei Tang&#160;and&#160;Joe Hollier&#160;have spent over a decade exploring the value of simplicity in our relationship to technology, partnering along the way with p"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/doordash-is-building-its-own-drone-delivery-business/",
    "domain": "大厂 AI 动态",
    "title": "DoorDash is building its own drone delivery business",
    "url": "https://techcrunch.com/2026/07/29/doordash-is-building-its-own-drone-delivery-business/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T13:00:00+00:00",
    "summary": "DoorDash has received FAA approval to operate a commercial drone delivery service in the United States."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/29/fast-metals-is-treating-waste-with-more-waste-to-extract-critical-minerals/",
    "domain": "大厂 AI 动态",
    "title": "Fast Metals is treating waste with more waste to extract critical minerals",
    "url": "https://techcrunch.com/2026/07/29/fast-metals-is-treating-waste-with-more-waste-to-extract-critical-minerals/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T12:00:00+00:00",
    "summary": "Aluminum production has saddled the world with billions of tons of caustic waste. One startup has a plan to clean it up and turn a profit."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/07/mythos-uncovers-crypto-weaknesses-that-went-unknown-for-years/",
    "domain": "大厂 AI 动态",
    "title": "Mythos attack on 3rd-round PQC algorithm candidate puts it out of commission",
    "url": "https://arstechnica.com/security/2026/07/mythos-uncovers-crypto-weaknesses-that-went-unknown-for-years/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T22:07:06+00:00",
    "summary": "HAWK withstood years of testing that had yet to uncover a fatal weakness found through Mythos."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/musk-went-to-war-sought-jail-time-for-x-ad-boycotts-but-case-ends-with-a-whimper/",
    "domain": "大厂 AI 动态",
    "title": "Musk went to “war,” sought jail time for X ad boycotts—but case ends with a whimper",
    "url": "https://arstechnica.com/tech-policy/2026/07/musk-went-to-war-sought-jail-time-for-x-ad-boycotts-but-case-ends-with-a-whimper/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T20:57:35+00:00",
    "summary": "Advertisers agreed to “reset” relationship with X."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/who-wins-and-who-loses-after-us-bans-foreign-robots/",
    "domain": "大厂 AI 动态",
    "title": "Who wins and who loses after US bans foreign robots?",
    "url": "https://arstechnica.com/ai/2026/07/who-wins-and-who-loses-after-us-bans-foreign-robots/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T20:03:42+00:00",
    "summary": "Government ban on foreign-made robots may hinder instead of help US robotics."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/comcast-store-punished-low-sales-by-smashing-pies-in-workers-faces-lawsuit-claims/",
    "domain": "大厂 AI 动态",
    "title": "Comcast store punished low sales by smashing pies in workers' faces, lawsuit claims",
    "url": "https://arstechnica.com/tech-policy/2026/07/comcast-store-punished-low-sales-by-smashing-pies-in-workers-faces-lawsuit-claims/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T19:33:55+00:00",
    "summary": "Comcast, accused of negligence, says lawsuit mischaracterized alleged events."
  },
  {
    "id": "rss:https://arstechnica.com/staff/2026/07/customize-ars-your-way-with-an-ars-pro-subscription/",
    "domain": "大厂 AI 动态",
    "title": "Customize Ars your way with an Ars Pro subscription",
    "url": "https://arstechnica.com/staff/2026/07/customize-ars-your-way-with-an-ars-pro-subscription/",
    "source": "Eric Bangeman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T19:23:27+00:00",
    "summary": "Ars Pro subscribers get customizable layouts along with no ads and no trackers."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/google-begins-global-rollout-of-age-verification-api-in-google-play/",
    "domain": "大厂 AI 动态",
    "title": "Google's \"privacy-preserving\" age verification system is coming to the Play Store",
    "url": "https://arstechnica.com/gadgets/2026/07/google-begins-global-rollout-of-age-verification-api-in-google-play/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T18:08:22+00:00",
    "summary": "Google's new API relies on parents to set age ranges in Family Link."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/elon-musks-xai-is-trying-to-sue-its-way-out-of-a-grok-reckoning/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk’s xAI is trying to sue its way out of a Grok reckoning",
    "url": "https://arstechnica.com/tech-policy/2026/07/elon-musks-xai-is-trying-to-sue-its-way-out-of-a-grok-reckoning/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T17:58:24+00:00",
    "summary": "Musk defends Grok, says Minnesota's nudifying app ban is unconstitutional."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/quantum-computing-roundup-still-more-technologies-making-waves/",
    "domain": "大厂 AI 动态",
    "title": "Yet more qubit tech: New quantum dot options, diamond vacancies",
    "url": "https://arstechnica.com/science/2026/07/quantum-computing-roundup-still-more-technologies-making-waves/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T17:37:47+00:00",
    "summary": "Companies are making sure we have a surplus of options for building qubits."
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
    "id": "wscn:3778287",
    "domain": "股票",
    "title": "科技巨头财报难顶压力，韩股午后转跌、三星抹平涨幅，美债原油同步走低",
    "url": "https://wallstreetcn.com/articles/3778287",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T05:46:38+00:00",
    "summary": "韩国首尔综指回吐稍早逾5%的涨幅转跌，此前两个交易日该指数累计下跌16%，并连续两日触发全市场熔断机制。三星电子二季度业绩大幅超预期，股价一度涨5.5%，SK海力士涨2%。微软盘后涨近9%，提振纳指100期货上涨0.6%，市场情绪有所企稳。"
  },
  {
    "id": "wscn:3778286",
    "domain": "股票",
    "title": "创业板跌超5%，工行建行逆势创新高，半导体、算力硬件再跌、光模块掀跌停潮，中际旭创港股IPO首日破发",
    "url": "https://wallstreetcn.com/articles/3778286",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:06:41+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市超3400股飘绿，上午半天成交1.46万亿。沪深两市半日成交额1.45万亿，较上个交易日缩量不到300亿。板块方面，半导体、算力硬件产业链深度回调，CPO、PCB、HBM方向大跌，中际旭创跌逾15%。机器人、光伏、商业航天、创新药题材跌幅靠前。白酒、银行、汽车板块逆势走强。"
  },
  {
    "id": "wscn:3778294",
    "domain": "股票",
    "title": "抢夺企业Agent入口！腾讯、阿里、字节新一轮大战一触即发",
    "url": "https://wallstreetcn.com/articles/3778294",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:05:16+00:00",
    "summary": "从各自试错到集中兵力，腾讯、阿里、字节几乎同时收拢AI战线，企业Agent竞争正式进入决战阶段。争夺的已不只是一个AI产品，而是企业每天工作的第一入口——谁占住办公场景，谁就更有机会成为下一代企业AI生态的核心。"
  },
  {
    "id": "wscn:3778296",
    "domain": "股票",
    "title": "字节跳动重组AI业务线：飞书与豆包产品线融合",
    "url": "https://wallstreetcn.com/articles/3778296",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:02:15+00:00",
    "summary": "To B战略升级。"
  },
  {
    "id": "wscn:3778291",
    "domain": "股票",
    "title": "高通的底牌：当手机不再是主场",
    "url": "https://wallstreetcn.com/articles/3778291",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:01:24+00:00",
    "summary": "高通正经历结构性转型：受存储涨价与苹果订单加速流失影响，手机业务营收大跌，主场权重持续稀释。但其“底牌”已浮出水面：汽车芯片创纪录增长，兜住中期确定性；数据中心业务全面铺开，决定未来估值上限。年底至明年初将是其各业务线成效的关键验证期。"
  },
  {
    "id": "wscn:3778260",
    "domain": "股票",
    "title": "韩股连续两日熔断之后：去杠杆是否已接近尾声？",
    "url": "https://wallstreetcn.com/premium/articles/3778260?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T03:59:51+00:00",
    "summary": "韩股去杠杆接近尾声，被动抛售高峰已过，但散户信心重创，市场震荡寻底，反转有待业绩确认。"
  },
  {
    "id": "wscn:3778290",
    "domain": "股票",
    "title": "OpenAI年化收入提速，CFO内部喊话：7月一个月顶过整个二季度",
    "url": "https://wallstreetcn.com/articles/3778290",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T03:21:48+00:00",
    "summary": "OpenAI CFO内部会议罕见披露：7月单月新增年化经常性收入已超整个二季度，增长引擎来自GPT-5.6、企业Agent及编程工具Codex的爆发式普及。有分析认为，这意味着今年ARR或逼近600亿美元，与Anthropic差距收窄。在估值达8520亿美元、IPO申请已秘密递交的关键节点，这份收入加速曲线，或将成为其上市路演最强底牌。"
  },
  {
    "id": "wscn:3778293",
    "domain": "股票",
    "title": "不只可远观，更能亲手造：在L'ÉCOLE触摸两千年前的金工温度",
    "url": "https://wallstreetcn.com/articles/3778293",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T03:03:24+00:00",
    "summary": "继巴黎首展、首尔巡展之后，“金手匠艺：铁器时代的金饰重生”终于来到上海。\n由Van Cleef &..."
  },
  {
    "id": "wscn:3778292",
    "domain": "股票",
    "title": "字节重大调整：豆包和火山吃下了飞书",
    "url": "https://wallstreetcn.com/articles/3778292",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T02:45:11+00:00",
    "summary": "字节跳动宣布重大组织调整，飞书被降级打散：其产品团队并入豆包，商业化团队并入火山引擎。此举标志字节放弃三者独立运营思路，集中资源发力AI，转而打造以豆包为智能核心、飞书为工作入口、火山引擎为云底座的企业AI体系。"
  },
  {
    "id": "wscn:3778288",
    "domain": "股票",
    "title": "数据鸽派、市场鹰派：英国央行周四面临政策信号考验",
    "url": "https://wallstreetcn.com/articles/3778288",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T02:40:31+00:00",
    "summary": "英国6月CPI降至15个月低点，私营部门工资增速跌至2020年来最低，新政府取消家庭电费增值税则进一步压低通胀预期，多数经济学家预计本周四英国央行将维持利率3.75%不变。但利率期货市场押注英国央行11月加息25个基点，押注主要源于油价上行风险。"
  },
  {
    "id": "wscn:3778272",
    "domain": "股票",
    "title": "三星Q2创史上最强盈利季：净利润暴涨1299.9%超预期，AI芯片狂揽99%利润",
    "url": "https://wallstreetcn.com/articles/3778272",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T02:08:34+00:00",
    "summary": "三星电子2026年Q2创史上最强单季：营收171.5万亿韩元同比暴增130%，营业利润89.49万亿韩元同比飙升1814%，利润率高达52.2%。核心引擎是半导体——DS部门独揽全公司99%利润，HBM4已完成规模量产并率先发货HBM4E样品，AI超级周期红利尽收囊中。净现金头寸167.6万亿韩元较去年近乎翻倍，ROE从5%跃升至56%。"
  },
  {
    "id": "wscn:3778285",
    "domain": "股票",
    "title": "微软财报点评：大涨8%市场奖励正现金流，Azure证明AI“供不应求”",
    "url": "https://wallstreetcn.com/premium/articles/3778285?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T02:04:04+00:00",
    "summary": "总营收900亿美元全面超预期；Azure CC增速43%；资本开支414亿再创新高；折旧年限调整释放隐形成长性。"
  },
  {
    "id": "wscn:3778281",
    "domain": "股票",
    "title": "鸽派的Warsh，鹰派的市场",
    "url": "https://wallstreetcn.com/articles/3778281",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T01:58:35+00:00",
    "summary": "本次FOMC会议，Warsh态度鸽派，拒绝主动引导市场预期，选择\"事后救场\"而非\"事前预判\"。市场对通胀担忧未获解答，长端利率大幅走高，曲线陡峭创纪录。联储反应函数趋于被动：通胀预期低于2.5%不鹰，核心通胀未达2%不降息。当前宏观主线回归AI Capex走向与地缘扰动。"
  },
  {
    "id": "wscn:3778265",
    "domain": "股票",
    "title": "Meta电话会：扎克伯格强调“卖掉算力换短期利润是愚蠢的”，烧钱买算力不是赌博是必须",
    "url": "https://wallstreetcn.com/articles/3778265",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T01:56:33+00:00",
    "summary": "扎克伯格在电话会中指出，广告业务收入同比增速超越同行，AI投资正在获得回报；关于出售算力，其表示仅仅出售所有的计算能力并获取短期利润是愚蠢的，相信销售智能的利润率将持续显著高于直接销售计算能力；其还指出，当前开源模型不如前沿模型强大，Meta作为一家“全栈科技公司”，必须拥有自主构建模型的能力。"
  },
  {
    "id": "wscn:3778284",
    "domain": "股票",
    "title": "A股SoC芯片公司上半年业绩狂欢背后，一半是周期潮水，一半是AI曙光",
    "url": "https://wallstreetcn.com/articles/3778284",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T01:55:28+00:00",
    "summary": "A股SoC芯片半年报集体爆发，星宸科技净利润增长近6倍、北京君正超4倍，但繁荣背后暗藏分化——涨价周期与AI结构性需求正以截然不同的逻辑驱动各家利润，谁在吃周期红利、谁在真正跑通AI商业化，将决定下半年格局走向。此外，中际旭创驳斥1.6T光模块大幅降价传闻，兆易创新朱一明提议公司回购不低于10亿。"
  },
  {
    "id": "wscn:3778279",
    "domain": "股票",
    "title": "韩股“去杠杆”完成了吗？摩根大通“机构已近尾声”，汇丰“散户仍处高位”",
    "url": "https://wallstreetcn.com/articles/3778279",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T01:09:10+00:00",
    "summary": "摩根大通认为，韩国杠杆ETF去杠杆已基本完成，对冲基金去杠杆进度约达90%，KOSPI估值降至5倍市盈率的“危机水平”、整体配置吸引力已现。汇丰则指出散户融资余额仅较峰值下降约15%，仍高达约220亿美元，且ETF规模缩水主要源于亏损而非主动撤退，去杠杆远未结束。"
  },
  {
    "id": "wscn:3778276",
    "domain": "股票",
    "title": "高通电话会：全线双位数涨价对冲内存成本，预计苹果订单下季度环比腰斩，年底量产数据中心芯片",
    "url": "https://wallstreetcn.com/articles/3778276",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T00:59:27+00:00",
    "summary": "面临内存等供应链成本飙升及产能100%满载的压力，高通将采取两位数幅度的全线提价以修复毛利率；高盛承认苹果订单流失加速，预计12月季度环比腰斩，但强调，同比激增61%的汽车业务（上调年化目标至70亿美元）及12月即将创收的数据中心AI芯片业务，将在2027财年彻底填补苹果退出的收入缺口。"
  },
  {
    "id": "wscn:3778196",
    "domain": "股票",
    "title": "当1178名AI人试图阻止“AGI”：让全人类刹车的成本到底有多大？答案或许是蒸发2.5万亿美元",
    "url": "https://wallstreetcn.com/premium/articles/3778196?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T00:58:42+00:00",
    "summary": "2026年7月28日，来自OpenAI、Anthropic、Google、Meta、Microsoft、Mistral、Thinking Machines等前沿AI公司的1178名员工联合签署《Pacing the Frontier》公开声明，要求美国政府推动国际合作，建立\"有意放缓自动化AI研发节奏\"的技术和治理工具。"
  },
  {
    "id": "wscn:3778271",
    "domain": "股票",
    "title": "美国原油和汽油库存降至“及其危险的低水平”，炼油厂产能利用率已达97%",
    "url": "https://wallstreetcn.com/articles/3778271",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T00:56:06+00:00",
    "summary": "美国原油库存正以惊人速度告急，上周商业库存单周骤降720万桶，战略石油储备跌至40年最低的3.077亿桶，炼油厂更以97%高负荷全力压榨产能。美伊冲突封锁霍尔木兹，分析师直言库存已处\"极其危险水平\"。当全球最后的能源缓冲垫加速抽空，油价的临界点或近在眼前。"
  },
  {
    "id": "wscn:3778280",
    "domain": "股票",
    "title": "从千问Work到WorkBuddy：Harness执行中间层成巨头争夺\"必选项\"",
    "url": "https://wallstreetcn.com/articles/3778280",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T00:55:49+00:00",
    "summary": "中信证券认为，Harness核心价值：一是解决长程任务痛点，将模型能力转化为稳定、低成本的端到端交付；二是连接模型与泛办公场景，拓展万亿市场并沉淀稀缺数据反哺迭代。AI竞争正由模型转向任务交付，成熟Harness厂商将占先机。"
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
    "points": 173,
    "published_at": "2026-07-28T12:19:07+00:00",
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
    "id": "hn:49097833",
    "domain": "金融",
    "title": "Show HN: The Federalist Papers, typeset as the 1787 newspapers they ran in",
    "url": "https://federalistreader.org/",
    "source": "vhwalke",
    "platform": "hackernews",
    "points": 39,
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
    "id": "rss:https://arxiv.org/abs/2607.26068",
    "domain": "金融",
    "title": "The Human Utility Factor: A Computable Welfare Metric That Reframes AI Governance as a Constrained Optimisation Problem",
    "url": "https://arxiv.org/abs/2607.26068",
    "source": "Sivasathivel Kandasamy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2607.26068v1 Announce Type: new Abstract: Existing AI governance frameworks, including the EU AI Act and NIST AI RMF, address safety, transparency, and accountability but do not operationalize q"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.26188",
    "domain": "金融",
    "title": "Bitcoin Runs on a Clock: Why Every Price Indicator Dies and the Halving Clock Doesn't",
    "url": "https://arxiv.org/abs/2607.26188",
    "source": "Josh Molnar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2607.26188v1 Announce Type: new Abstract: Every widely followed Bitcoin cycle indicator (Pi Cycle, MVRV, Mayer, Puell) called turns precisely for a decade, then degraded in one sequence: precise"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.26245",
    "domain": "金融",
    "title": "OpenMarket: A Synchronized Polymarket-Binance Dataset for High-Frequency Prediction-Market Research",
    "url": "https://arxiv.org/abs/2607.26245",
    "source": "Gregory Young",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2607.26245v1 Announce Type: new Abstract: OpenMarket began as an attempt to trade Polymarket's BTC 15-minute binary markets against Binance BTC/USDT order flow. The attempt did not produce a tra"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.26405",
    "domain": "金融",
    "title": "Multi-Currency AMMs for Decentralized FOREX Markets: Feasibility & Optimal Design",
    "url": "https://arxiv.org/abs/2607.26405",
    "source": "Reina Ke Xin Li, Andreas Park, Andreas Veneris, Srisht Fateh Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2607.26405v1 Announce Type: new Abstract: Most currency pairs lack a direct liquid market, so international foreign exchange relies on routing transactions through a dominant vehicle currency. M"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.26859",
    "domain": "金融",
    "title": "No Data Is Not No Risk: Visibility Aware Graph-Based Inference of Business Conduct Risk",
    "url": "https://arxiv.org/abs/2607.26859",
    "source": "Tsuyoshi Iwata, Johannes Laurmaa, Ryohei Hisano",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2607.26859v1 Announce Type: new Abstract: The monitoring of business conduct risk is hindered by sparse, uneven, and visibility-biased data. Prior studies show that business conduct risk informa"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27019",
    "domain": "金融",
    "title": "Multi-Asset Liquidation in Dark Pools with Adverse Selection",
    "url": "https://arxiv.org/abs/2607.27019",
    "source": "Guanxing Fu, Johannes Ruf, Xiaomin Shi, Zuo Quan Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2607.27019v1 Announce Type: new Abstract: Multi-asset liquidation in dark pools with adverse selection remains unsolved in literature. In this paper, we investigate multi-asset portfolio liquida"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27063",
    "domain": "金融",
    "title": "Herding, Momentum, and Reversal in China's A-Share Market: An Agent-Based Network Model with Information Diffusion",
    "url": "https://arxiv.org/abs/2607.27063",
    "source": "Jiahao Weng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2607.27063v1 Announce Type: new Abstract: This study develops an agent-based financial market model to explain stock-price momentum and reversal through the joint effects of local herding and de"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27070",
    "domain": "金融",
    "title": "Where does the criticality live? Early-warning signals are event-heterogeneous across seven crypto-perpetual liquidation cascades",
    "url": "https://arxiv.org/abs/2607.27070",
    "source": "Ramon Marc Garcia Seuma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2607.27070v1 Announce Type: new Abstract: Do crypto perpetual-futures crashes carry a reproducible early-warning fingerprint of a critical transition, and in which state variable? We study seven"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27142",
    "domain": "金融",
    "title": "How Divorce Reforms Induced Married Couples to Supply More Labor",
    "url": "https://arxiv.org/abs/2607.27142",
    "source": "Yedilkhan Baigabulov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2607.27142v1 Announce Type: new Abstract: This paper studies the dynamic effects of divorce legislation on the labor supply behavior and welfare of married couples. Using U.S. household panel da"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.26109",
    "domain": "金融",
    "title": "The Attention-Directing Ability of Teams",
    "url": "https://arxiv.org/abs/2607.26109",
    "source": "Olga Kokshagina, Marc Santolini, Christoph Riedl",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2607.26109v1 Announce Type: cross Abstract: Why do some teams consistently mobilize collective effort and achieve superior performance while others struggle to coordinate action? We introduce At"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.26792",
    "domain": "金融",
    "title": "Crossing-Free Probabilistic K-Line Forecasts Without Retraining",
    "url": "https://arxiv.org/abs/2607.26792",
    "source": "Runyao Yu, Yuchen Tao, Yujie Chen, Wentao Wang, Derek W. Bunn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2607.26792v1 Announce Type: cross Abstract: Probabilistic K-line forecasting describes uncertainty in four complementary prices, namely open--high--low--close (OHLC). However, it introduces two "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27039",
    "domain": "金融",
    "title": "Forcing and duality-corrected contracts for volatility control",
    "url": "https://arxiv.org/abs/2607.27039",
    "source": "Alessandro Chiusolo, Emma Hubert, Dylan Possama\\\"i, Nizar Touzi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2607.27039v1 Announce Type: cross Abstract: In this paper, we revisit the construction of optimal incentives in continuous-time principal-agent problems with drift and volatility control. Origin"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27099",
    "domain": "金融",
    "title": "Rainfall is rough",
    "url": "https://arxiv.org/abs/2607.27099",
    "source": "Thomas Deschatre, Marc Hoffmann, Mathieu Rosenbaum",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2607.27099v1 Announce Type: cross Abstract: We propose a new approach to model rainfall by combining heterogeneous data sources at different time scales. Continuous arrivals of rain cells are in"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27188",
    "domain": "金融",
    "title": "Inverse Learning of Latent Risk-Neutral Densities from Irregular Option Quotes",
    "url": "https://arxiv.org/abs/2607.27188",
    "source": "Lennon J. Shikhman, Michael Galarnyk, Aadi Dash, Nicholas A. Welsh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2607.27188v1 Announce Type: cross Abstract: Accurate option prices do not imply accurate recovery of the latent risk-neutral density. We study this distinction with two complementary benchmarks."
  },
  {
    "id": "rss:https://arxiv.org/abs/2411.17136",
    "domain": "金融",
    "title": "Financial Volatility and Risk Forecasting Incorporating a Larger Number of Realized Measures",
    "url": "https://arxiv.org/abs/2411.17136",
    "source": "Qianli Zhao, Chao Wang, Richard Gerlach, Giuseppe Storti, Lingxiang Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2411.17136v2 Announce Type: replace Abstract: Realised volatility has become increasingly prominent in volatility forecasting due to its ability to capture intraday price fluctuations. With a gr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2505.03247",
    "domain": "金融",
    "title": "Strategic Effort and Non-Linear Positional Bandwagon Drafting Benefits in Multi-Stage Competitive Games: Evidence from Triathlon",
    "url": "https://arxiv.org/abs/2505.03247",
    "source": "Felix Reichel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2505.03247v3 Announce Type: replace Abstract: This paper examines strategic effort and positioning choices in finite multistage games These choices can generate positional bandwagon drafting ben"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.22834",
    "domain": "金融",
    "title": "Complexity Beyond Incentives: The Critical Role of Reporting Language",
    "url": "https://arxiv.org/abs/2511.22834",
    "source": "Rustamdjan Hakimov, Manshu Khanna",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2511.22834v2 Announce Type: replace Abstract: Mechanisms specify both allocation rules and message spaces. We study how message spaces affect behavior in a laboratory assignment environment in w"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.07687",
    "domain": "金融",
    "title": "Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets",
    "url": "https://arxiv.org/abs/2601.07687",
    "source": "Efstratios Manolakis, Christian Bongiorno, Rosario Nunzio Mantegna",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2601.07687v3 Announce Type: replace Abstract: Recent advances in nonlinear shrinkage yield asymptotically optimal cleaners for large covariance matrices and have been extended to empirical cross"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.10224",
    "domain": "金融",
    "title": "The hidden structure of innovation networks",
    "url": "https://arxiv.org/abs/2601.10224",
    "source": "Lorenzo Emer, Anna Gallo, Mattia Marzi, Andrea Mina, Tiziano Squartini, Andrea Vandin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2601.10224v3 Announce Type: replace Abstract: Innovation emerges from complex collaboration patterns - among inventors, firms, or institutions. However, not much is known about the overall mesos"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.10400",
    "domain": "金融",
    "title": "Resolution-Aware Perpetual Futures on Binary Prediction Markets: Failure Modes and Mechanical Stress Tests Using Polymarket Data",
    "url": "https://arxiv.org/abs/2605.10400",
    "source": "Maksym Nechepurenko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2605.10400v2 Announce Type: replace Abstract: We study whether crypto-style perpetual-futures mechanics can be applied to a binary event claim that ultimately pays 0 or 1. A synthetic long enter"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.10428",
    "domain": "金融",
    "title": "A Taxonomy of Event-Linked Perpetual Futures: Design Axes, Failure Modes, and Empirical Evaluability",
    "url": "https://arxiv.org/abs/2605.10428",
    "source": "Maksym Nechepurenko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2605.10428v2 Announce Type: replace Abstract: The label event-linked perpetual often conflates mathematically different contracts. We replace a flat product list with a four-axis taxonomy: under"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.10486",
    "domain": "金融",
    "title": "Manipulation, Informed Trading, and Regulation in Leveraged Event-Linked Markets",
    "url": "https://arxiv.org/abs/2605.10486",
    "source": "Maksym Nechepurenko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2605.10486v2 Announce Type: replace Abstract: Leverage does not create manipulation or informed trading in event markets, but it changes their economics. We separate four conduct channels: marke"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.06737",
    "domain": "金融",
    "title": "Fast-excursion limit of the Heston model",
    "url": "https://arxiv.org/abs/2606.06737",
    "source": "Ryan McCrickerd",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2606.06737v2 Announce Type: replace Abstract: This article introduces an unconventional model for price processes in finance that emerges from the classical Heston model under Mechkov's fast-rev"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05802",
    "domain": "金融",
    "title": "Failure Privacy and Safe Collective Expression with Social Assurance Contracts",
    "url": "https://arxiv.org/abs/2607.05802",
    "source": "Matthew Cashman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2607.05802v4 Announce Type: replace Abstract: Controversial views sometimes remain unspoken because they invite retaliation. However, a sufficiently large group could speak safely if only they s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2505.10373",
    "domain": "金融",
    "title": "Reproducing the first and second moments of empirical degree distributions",
    "url": "https://arxiv.org/abs/2505.10373",
    "source": "Mattia Marzi, Francesca Giuffrida, Diego Garlaschelli, Tiziano Squartini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2505.10373v5 Announce Type: replace-cross Abstract: The study of probabilistic models for the analysis of complex networks represents a flourishing research field. Among the former, Exponential "
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.21869",
    "domain": "金融",
    "title": "A Bayesian approach to out-of-sample network reconstruction",
    "url": "https://arxiv.org/abs/2602.21869",
    "source": "Mattia Marzi, Tiziano Squartini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T04:00:00+00:00",
    "summary": "arXiv:2602.21869v3 Announce Type: replace-cross Abstract: Networks underpin systems that range from finance to biology, yet their structure is often only partially observed. Current reconstruction met"
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
    "points": 13,
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
  }
]
```
