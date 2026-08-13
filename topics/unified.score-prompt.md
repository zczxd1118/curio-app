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

- 今日日期：`2026-08-13`
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
  "date": "2026-08-13",
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
    "id": "bvid:BV1834y1676P",
    "domain": "AI",
    "title": "黑马程序员前端微信小程序开发教程，微信小程序从基础到发布全流程_企业级商城实战(含uni-app项目多端部署)",
    "url": "http://www.bilibili.com/video/av807451085",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 6441912,
    "published_at": "2021-12-17T01:30:11+00:00",
    "summary": "传智教育·黑马程序员前端研究院全新录制的前端入门教程\n全部配套资源领取方式：关注黑马程序员公众号，回复关键词:领取资源02\n===============================\n本课程从小程序账号注册、开发环境搭建、基础语法、路由导航、数据请求、分包、组件化等方面详细阐述了小程序开发必备的基础知识。\n学完小程序基础之后，利用 uni-app 技术实现微信小程序的开发，可以做到一次开发多端"
  },
  {
    "id": "bvid:BV1DfrdByE2H",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！Agentic AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av115897075242856",
    "source": "吴恩达Agent",
    "platform": "bilibili",
    "points": 4213484,
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
    "points": 1701032,
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
    "points": 1640789,
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
    "points": 1325819,
    "published_at": "2026-07-05T02:00:00+00:00",
    "summary": "用不上codex的朋友们！新的国产Agent直接上手，来跑通8大用法～\n感谢朋友们的三连+关注～"
  },
  {
    "id": "bvid:BV14rzQB9EJj",
    "domain": "AI",
    "title": "Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill / Hook / 图片 / 上下文处理/ 后台任务",
    "url": "http://www.bilibili.com/video/av115954889596221",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1268503,
    "published_at": "2026-01-25T08:55:20+00:00",
    "summary": "时间戳如下，方便大家跳转观看：\n \n第一部分：环境搭建与基础交互\n- 01:09 安装 Claude Code\n- 01:43 登录与授权\n- 02:55 第一个实战问题\n- 03:12 三种模式详解 (默认/自动/规划)\n \n第二部分：复杂任务处理与终端控制\n- 06:00 执行终端命令 (Bash)\n- 06:49 使用规划模式 (Plan Mode)\n- 11:06 跳过所有权限检测 (da"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1109246,
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
    "points": 1045362,
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
    "points": 943583,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 670769,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 550905,
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
    "points": 482423,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 436646,
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
    "points": 420258,
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
    "points": 396072,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 263692,
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
    "points": 234341,
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
    "points": 230975,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1i9Z8YhEja",
    "domain": "AI",
    "title": "学 AI，看这个视频就够了！最全程序员 AI 指南：AI核心概念、实用AI工具、AI编程技巧、AI开发技术",
    "url": "http://www.bilibili.com/video/av114262957626976",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 180378,
    "published_at": "2025-04-01T13:56:58+00:00",
    "summary": "AI 时代，程序员要学什么才能不被淘汰呢？这个视频给你答案。带你快速了解 AI 核心概念、AI 常用工具、AI 编程技巧、AI + 编程技术，走在时代的前沿，算是一期硬核的程序员 AI 学习指南视频了~\n还为大家准备了免费开源 AI 知识库：https://ai.codefather.cn，有帮助的话记得三连哦~\n涉及知识点：大模型、Prompt、AI开发平台、RAG知识库、MCP、Ollama本"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 179025,
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
    "points": 163564,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 163531,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "domain": "AI",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 154440,
    "published_at": "2026-01-11T15:43:58+00:00",
    "summary": "🚀开发者必看！Superpowers把专业工程团队方法论固化成Skills，让Claude Code告别越写越乱的困境：规格驱动+代码质量双重保障！AI编程新范式！头脑风暴+计划+执行一条龙自动化\n\n\n🚀🚀🚀 视频简介：\n🎬 本期视频详细演示了开源AI编程工作流系统Superpowers的完整使用方法，并通过开发一款iOS时间线笔记原生应用来实测其效果。\n🔧 核心内容：\nSuperpowers工作"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 153482,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1eYPpeWEnT",
    "domain": "AI",
    "title": "Cursor + MCP = 王炸！彻底颠覆我的Cursor工作流，效率直接起飞",
    "url": "http://www.bilibili.com/video/av114073660301264",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 150935,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV16Luq6FEmP",
    "domain": "AI",
    "title": "当不懂代码的老婆，第一次接触vibe coding……",
    "url": "http://www.bilibili.com/video/av117076211536327",
    "source": "糖果果的未来要发光",
    "platform": "bilibili",
    "points": 141199,
    "published_at": "2026-08-11T09:50:27+00:00",
    "summary": "当不懂代码的老婆，第一次接触vibe coding……"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 128780,
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
    "points": 93151,
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
    "points": 90981,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 76453,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 74101,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 73891,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53964,
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
    "points": 47592,
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
    "points": 45987,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 43288,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 40405,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29590,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28865,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1FSLgz9EX6",
    "domain": "AI",
    "title": "强烈推荐！这绝对是2025年AI Agent入门天花板教程！AI大佬86集精讲，全篇通俗易懂！让你少走99%弯路！agent实战/agent开发/AI大模型",
    "url": "http://www.bilibili.com/video/av114392762943758",
    "source": "从零学AI_李沐",
    "platform": "bilibili",
    "points": 27694,
    "published_at": "2025-04-24T11:49:09+00:00",
    "summary": "感谢小伙伴们的收看，配套籽料已全部整理。"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 26292,
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
    "points": 22700,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1gf3T6KEef",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！从环境搭建到工作流完整闭环，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116979708990688",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 21167,
    "published_at": "2026-07-25T08:47:37+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 21138,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 20456,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1zjd3BiEzo",
    "domain": "AI",
    "title": "别再二选一：Claude Code + Codex 联用才是最强姿势",
    "url": "http://www.bilibili.com/video/av116537746791000",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 19980,
    "published_at": "2026-05-08T07:34:23+00:00",
    "summary": "Codex 已悄然追上 Claude Code，GPT 5.5 比肩 Opus 4.7、OpenAI Pro 额度更大方。但作者 Chase 想说：别再纠结谁更好，最佳姿势是把两者一起用——Codex 桌面应用直接跑 Claude Code 终端，让两个模型互查方案、互查代码（一次实测 Claude Code 帮 Codex 抓出 20 个 bug）。背后更重要的思路是 tool agnostic"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 19015,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1htCnY4ET6",
    "domain": "AI",
    "title": "用 Cursor AI 写 flutter 直接喂设计图就行 | flutter教程",
    "url": "http://www.bilibili.com/video/av113723805008238",
    "source": "独立开发者_猫哥",
    "platform": "bilibili",
    "points": 17929,
    "published_at": "2024-12-27T08:21:35+00:00",
    "summary": "✏️【关于本期视频】\n在上一篇文章《Flutter 使用 Cursor 和 Figma 快速生成界面代码》中，有同学提到他直接使用了设计稿的图片进行生成。我试了一下，效果确实很好。因此，我整理了一些文档，希望对大家有所帮助。\n下图展示了我没有手动编写任何代码实现的消息首页，支持上下滑动刷新数据。\n👉 文档 https://ducafecat.com/blog/use-cursor-ai-flutt"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 16201,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 10973,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
  },
  {
    "id": "hn:49255710",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Risky Business",
    "url": "https://stratechery.com/2026/nvidias-risky-business/",
    "source": "jonbaer",
    "platform": "hackernews",
    "points": 349,
    "published_at": "2026-08-11T10:02:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:49263340",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Lightning and NeMo Switchyard",
    "url": "https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/",
    "source": "droidjj",
    "platform": "hackernews",
    "points": 258,
    "published_at": "2026-08-11T19:35:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:49189234",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia’s Vera Whitepaper Has a Thread Loose",
    "url": "https://chipsandcheese.com/p/nvidias-vera-whitepaper-has-a-thread",
    "source": "pella",
    "platform": "hackernews",
    "points": 208,
    "published_at": "2026-08-05T21:24:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49257947",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Lightning",
    "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4",
    "source": "beklein",
    "platform": "hackernews",
    "points": 121,
    "published_at": "2026-08-11T13:26:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:49122838",
    "domain": "AI 算力 / 半导体",
    "title": "Moonshot’s Kimi uses 20k Nvidia chip cluster from Alibaba",
    "url": "https://www.bloomberg.com/news/articles/2026-07-31/moonshot-s-kimi-built-on-20-000-nvidia-chip-cluster-from-alibaba",
    "source": "gk1",
    "platform": "hackernews",
    "points": 114,
    "published_at": "2026-07-31T13:24:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49279812",
    "domain": "AI 算力 / 半导体",
    "title": "Why space is a terrible place to cool a data center",
    "url": "https://thenewstack.io/spacex-and-nvidias-orbital-ai-datacenter-fantasy/",
    "source": "CrankyBear",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-12T23:08:21+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/revolutionizing-safety-unveiling-the-power-of-safety-bubble-detectors-in-robotics/",
    "domain": "AI 算力 / 半导体",
    "title": "Revolutionizing Safety: Unveiling the Power of Safety Bubble Detectors in Robotics",
    "url": "https://www.eetimes.com/revolutionizing-safety-unveiling-the-power-of-safety-bubble-detectors-in-robotics/",
    "source": "\"Rajesh Mahapatra , Senior Manager, Anil Sripadarao , Principal Engineer, Prasanna Bhat , Engineer, Colm Prendergast , Senior Principal Engineer, Shane O’Meara, Senior Manager, Dara O’Sullivan, Director, Anders Frederiksen, Principal Specialist, and",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T19:34:18+00:00",
    "summary": "This article will explain the architecture of real-time safety bubble detection that includes challenges for developing a modular solution, optimizing such a high data bandwidth application to run at "
  },
  {
    "id": "rss:https://www.eetimes.com/meta-cuts-server-count-25-by-reusing-old-memory-can-anyone-else-do-it/",
    "domain": "AI 算力 / 半导体",
    "title": "Meta Cuts Server Count 25% by Reusing Old Memory: Can Anyone Else Do It?",
    "url": "https://www.eetimes.com/meta-cuts-server-count-25-by-reusing-old-memory-can-anyone-else-do-it/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T18:40:03+00:00",
    "summary": "Meta squeezes 25% fewer servers from old DDR4 via CXL, but most firms face messy DIMM, power, and telemetry traps. The post Meta Cuts Server Count 25% by Reusing Old Memory: Can Anyone Else Do It? app"
  },
  {
    "id": "rss:https://www.eetimes.com/navigating-gmsl-how-pixel-and-tunnel-modes-enhance-system-performance/",
    "domain": "AI 算力 / 半导体",
    "title": "Navigating GMSL: How Pixel and Tunnel Modes Enhance System Performance",
    "url": "https://www.eetimes.com/navigating-gmsl-how-pixel-and-tunnel-modes-enhance-system-performance/",
    "source": "Flavius Luntrașu , Senior Engineer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T18:34:51+00:00",
    "summary": "This article explores how GMSL™ technology transports high-speed CSI-2 video data and compares the advantages of pixel mode and tunnel mode in modern imaging systems. Learn how each approach impacts d"
  },
  {
    "id": "rss:https://www.eetimes.com/building-supply-chain-resilience-selecting-reliable-capacitor-suppliers/",
    "domain": "AI 算力 / 半导体",
    "title": "Building Supply Chain Resilience: Selecting Reliable Capacitor Suppliers",
    "url": "https://www.eetimes.com/building-supply-chain-resilience-selecting-reliable-capacitor-suppliers/",
    "source": "Shanghai Yongming Electronic Co.,Ltd",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T13:00:00+00:00",
    "summary": "Supply chain stability is becoming a key consideration for companies when selecting electronic components. Discover more! The post Building Supply Chain Resilience: Selecting Reliable Capacitor Suppli"
  },
  {
    "id": "rss:https://www.eetimes.com/sony-tsmc-4-7b-deal-helps-thwart-samsung-analysts-say/",
    "domain": "AI 算力 / 半导体",
    "title": "Sony-TSMC $4.7B Deal Helps Thwart Samsung, Analysts Say",
    "url": "https://www.eetimes.com/sony-tsmc-4-7b-deal-helps-thwart-samsung-analysts-say/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T10:06:27+00:00",
    "summary": "Sony and TSMC have joined forces to counter Samsung's growing presence in smartphone image sensors, particularly for Apple. The post Sony-TSMC $4.7B Deal Helps Thwart Samsung, Analysts Say appeared fi"
  },
  {
    "id": "rss:https://www.eetimes.com/agentic-ai-multi-physics-and-standards-will-redefine-chips-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Agentic AI, Multi‑Physics, and Standards Will Redefine Chips Design",
    "url": "https://www.eetimes.com/agentic-ai-multi-physics-and-standards-will-redefine-chips-design/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T22:00:00+00:00",
    "summary": "Agentic AI, brutal physics bottlenecks, and standards are remaking chip design from silicon to systems. The post Agentic AI, Multi‑Physics, and Standards Will Redefine Chips Design appeared first on E"
  },
  {
    "id": "rss:https://www.eetimes.com/amd-challenges-gpu-centric-architectures-as-it-takes-aim-at-nvidia-in-robotics/",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Challenges GPU-Centric Architectures as It Takes Aim at Nvidia in Robotics",
    "url": "https://www.eetimes.com/amd-challenges-gpu-centric-architectures-as-it-takes-aim-at-nvidia-in-robotics/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T14:09:45+00:00",
    "summary": "AMD’s new SoC for robots combines CPU, GPU, NPU on one chip with unified memory. The post AMD Challenges GPU-Centric Architectures as It Takes Aim at Nvidia in Robotics appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/managing-your-component-library-for-supply-chain-resilience/",
    "domain": "AI 算力 / 半导体",
    "title": "Managing Your Component Library for Supply Chain Resilience",
    "url": "https://www.eetimes.com/managing-your-component-library-for-supply-chain-resilience/",
    "source": "Cadence Design Systems",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T14:00:00+00:00",
    "summary": "To take a PCB from design to production, an unmanaged component library is a hidden liability. Obsolete parts, single-source vulnerabilities, long lead times, counterfeit exposure, and compliance gaps"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-hardwares-next-frontier-is-integration/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Hardware’s Next Frontier Is Integration",
    "url": "https://www.eetimes.com/ai-hardwares-next-frontier-is-integration/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T09:25:50+00:00",
    "summary": "The LID World Summit 2026 showed why AI progress now depends on system-level advances in memory, packaging, photonics, and power. The post AI Hardware’s Next Frontier Is Integration appeared first on "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/qualcomm-details-snapdragon-c-specs-for-usd300-laptops-for-the-first-time-claims-67-percent-faster-performance-on-battery-than-intel-n250-ac-performance-remains-a-mystery",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm details Snapdragon C specs for $300 laptops for the first time — claims 67% faster performance on battery than Intel N250, AC performance remains a mystery",
    "url": "https://www.tomshardware.com/pc-components/cpus/qualcomm-details-snapdragon-c-specs-for-usd300-laptops-for-the-first-time-claims-67-percent-faster-performance-on-battery-than-intel-n250-ac-performance-remains-a-mystery",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T21:14:33+00:00",
    "summary": "Qualcomm has detailed the specs for its Snapdragon C processor, with 8 cores and claimed \"all-day\" battery life."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/oracle-plans-more-layoffs-weeks-after-spending-most-of-its-2-1-billion-restructuring-budget",
    "domain": "AI 算力 / 半导体",
    "title": "Oracle plans more layoffs weeks after spending most of its $2.1 billion restructuring budget, report claims — some teams face double-digit percentage reductions, 21,000 full-time positions already eli",
    "url": "https://www.tomshardware.com/tech-industry/oracle-plans-more-layoffs-weeks-after-spending-most-of-its-2-1-billion-restructuring-budget",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T17:00:04+00:00",
    "summary": "Oracle plans to cut more jobs this month, with reductions on some teams reaching double-digit percentages."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-doubles-rtx-pro-6000-blackwells-msrp-to-a-staggering-usd16-000-96gb-card-started-pre-orders-below-usd8-000-last-year",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia doubles RTX PRO 6000 Blackwell's MSRP to a staggering $16,000 — 96GB card started pre-orders below $8,000 last year",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-doubles-rtx-pro-6000-blackwells-msrp-to-a-staggering-usd16-000-96gb-card-started-pre-orders-below-usd8-000-last-year",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T15:53:19+00:00",
    "summary": "A data center GPU has become more expensive because of the AI boom enabled by unprecedented data center buildouts — shocking. Nvidia's RTX 6000 Pro Blackwell is now twice as costly as it was last year"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-developers-begin-suing-local-jurisdictions-behind-bans-and-moratoriums-claims-range-from-officials-exceeding-authority-to-violations-of-due-process-and-equal-protection-laws",
    "domain": "AI 算力 / 半导体",
    "title": "AI data center developers begin suing local jurisdictions behind bans and moratoriums — claims range from officials exceeding authority to violations of due process and equal protection laws",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-developers-begin-suing-local-jurisdictions-behind-bans-and-moratoriums-claims-range-from-officials-exceeding-authority-to-violations-of-due-process-and-equal-protection-laws",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T15:46:55+00:00",
    "summary": "Some data center developers are suing local governments for passing temporary bans and moratorium, saying that they such moves violated their rights to due process and equal protection. This move has "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/coreweave-ceo-mike-intrator-says-it-has-signed-an-a100-contract-running-into-2029",
    "domain": "AI 算力 / 半导体",
    "title": "CoreWeave proves Nvidia's aging AI GPUs from 2020 can generate profit nine years after deployment, signs A100 contracts into 2029 — power constraints and legacy infrastructure keep old GPUs profitable",
    "url": "https://www.tomshardware.com/tech-industry/coreweave-ceo-mike-intrator-says-it-has-signed-an-a100-contract-running-into-2029",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T15:41:47+00:00",
    "summary": "CoreWeave reported $2.58 billion in quarterly revenue, up 112% year over year."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/suspected-china-linked-hackers-used-ai-to-run-the-first-ever-end-to-end-autonomous-cyberattack-on-taiwans-government-israeli-firm-says-open-source-built-tool-continuously-devised-effective-hack-strategies-in-real-time",
    "domain": "AI 算力 / 半导体",
    "title": "Suspected China-linked hackers used AI to run the first-ever end-to-end autonomous cyberattack on Taiwan's government, Israeli firm says — open-source-built tool continuously devised effective hack st",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/suspected-china-linked-hackers-used-ai-to-run-the-first-ever-end-to-end-autonomous-cyberattack-on-taiwans-government-israeli-firm-says-open-source-built-tool-continuously-devised-effective-hack-strategies-in-real-time",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T14:58:54+00:00",
    "summary": "Suspected China-linked hackers used autonomous AI agents to breach Taiwanese government systems, compromising 85 accounts and stealing 2,500+ records."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/qidi-plus5-3d-printer-review",
    "domain": "AI 算力 / 半导体",
    "title": "QIDI Plus5 3D printer review: The best one yet",
    "url": "https://www.tomshardware.com/3d-printing/qidi-plus5-3d-printer-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T14:08:09+00:00",
    "summary": "QIDI Plus5 is polished, huge, and produces excellent prints with some of the toughest technical filaments."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nova-lake-cpus-with-cut-down-e-core-clusters-may-still-retain-full-cache-pool-says-new-leak-8p-12e-config-predictions-revised-from-33mb-to-36mb-4p-4e-config-from-15mb-to-18mb",
    "domain": "AI 算力 / 半导体",
    "title": "Nova Lake CPUs with cut-down E-core clusters may still retain full cache pool, says new leak — 8P+12E config predictions revised from 33MB to 36MB, 4P+4E config from 15MB to 18MB",
    "url": "https://www.tomshardware.com/pc-components/cpus/nova-lake-cpus-with-cut-down-e-core-clusters-may-still-retain-full-cache-pool-says-new-leak-8p-12e-config-predictions-revised-from-33mb-to-36mb-4p-4e-config-from-15mb-to-18mb",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T13:37:47+00:00",
    "summary": "A new leak from Jaykihn says some Nova Lake SKUs, including mobile counterparts, will retain the cache config of their fully-enabled variants despite having reduced E-cores."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/photonics/how-optical-interconnects-and-silicon-photonics-emerged-as-ais-next-hot-commodity-looming-us-china-summit-puts-photonics-into-the-crosshairs",
    "domain": "AI 算力 / 半导体",
    "title": "How optical interconnects and silicon photonics emerged as AI's next hot commodity — looming US-China summit puts photonics into the crosshairs",
    "url": "https://www.tomshardware.com/tech-industry/photonics/how-optical-interconnects-and-silicon-photonics-emerged-as-ais-next-hot-commodity-looming-us-china-summit-puts-photonics-into-the-crosshairs",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T12:42:23+00:00",
    "summary": "The U.S. wants Chinese optical transceivers out of future AI data centers, but China’s current dominance of the rapidly evolving photonics supply chain could make a ban complicated"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/ymtc-breaks-into-the-top-three-nand-makers-for-the-first-time",
    "domain": "AI 算力 / 半导体",
    "title": "YMTC breaks into the top three NAND makers for the first time as AI servers swallow 48% of all flash — Chinese vendor has 14% share, according to research",
    "url": "https://www.tomshardware.com/tech-industry/ymtc-breaks-into-the-top-three-nand-makers-for-the-first-time",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T12:35:44+00:00",
    "summary": "Samsung led with 25%, SK hynix followed at 22%, and Micron rounded out the top five."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/gmktec-evo-t2-review",
    "domain": "AI 算力 / 半导体",
    "title": "GMKtec Evo-T2 review: Panther Lake for a price",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/gmktec-evo-t2-review",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T12:05:00+00:00",
    "summary": "GMKtec has positioned its new Evo-T2 mini PC, built around Intel’s 18A Panther Lake silicon, as a compact personal AI workstation. It is also plenty capable of performing well in office productivity a"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-will-begin-digitally-watermarking-marking-ai-generated-text-and-images-anthropic-details-how-itll-comply-with-the-eus-artificial-intelligence-act",
    "domain": "AI 算力 / 半导体",
    "title": "Claude will begin digitally watermarking marking AI-generated text and images — Anthropic details how it'll comply with the EU's Artificial Intelligence Act",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-will-begin-digitally-watermarking-marking-ai-generated-text-and-images-anthropic-details-how-itll-comply-with-the-eus-artificial-intelligence-act",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T11:30:00+00:00",
    "summary": "European users of Anthropic's Claude models can expect that future versions of those tools will begin embedding digital marks in generated text and images to identify them as the product of AI."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/asobi-remote-play-app-lets-gamers-stream-ps4-and-ps5-games-on-the-steam-deck-even-without-a-console-dev-breaks-playstation-plus-premium-cloud-gaming-support-free-of-the-playstation-portal",
    "domain": "AI 算力 / 半导体",
    "title": "Asobi Remote Play app lets gamers stream PS4 and PS5 games on the Steam Deck, even without a console — dev breaks PlayStation Plus Premium cloud gaming support free of the PlayStation Portal",
    "url": "https://www.tomshardware.com/video-games/playstation/asobi-remote-play-app-lets-gamers-stream-ps4-and-ps5-games-on-the-steam-deck-even-without-a-console-dev-breaks-playstation-plus-premium-cloud-gaming-support-free-of-the-playstation-portal",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T11:00:00+00:00",
    "summary": "PlayStation Remote Play allows you to stream games from your PS4 or PS5 console to a variety of devices locally, but the Asobi: Remote Play service goes farther by extending the PlayStation Portal's e"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/samsung-foundry-updates-process-roadmap-to-move-1-4nm-node-to-2029-high-na-euv-will-enable-1nm-class-and-smaller-nodes-in-2030-and-beyond",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung Foundry updates process roadmap to move 1.4nm node to 2029 — high-NA EUV will enable 1nm-class and smaller nodes in 2030 and beyond",
    "url": "https://www.tomshardware.com/tech-industry/samsung-foundry-updates-process-roadmap-to-move-1-4nm-node-to-2029-high-na-euv-will-enable-1nm-class-and-smaller-nodes-in-2030-and-beyond",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T11:00:00+00:00",
    "summary": "Samsung Foundry has delayed its 1.4nm-class node to 2029, making SF2 one of its longest-lasting process technologies ever. The company also aims to start using High-NA EUV for its 1nm-class process te"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/save-over-usd600-on-a-massive-18-inch-gaming-laptop-as-it-falls-to-a-new-all-time-low-price-at-amazon-acers-predator-helios-neo-18-ai-packs-an-rtx-5070-ti-and-32gb-of-memory",
    "domain": "AI 算力 / 半导体",
    "title": "Save over $600 on a massive 18-inch gaming laptop as it falls to a new all-time low price at Amazon — Acer's Predator Helios Neo 18 AI packs an RTX 5070 Ti and 32GB of memory",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/save-over-usd600-on-a-massive-18-inch-gaming-laptop-as-it-falls-to-a-new-all-time-low-price-at-amazon-acers-predator-helios-neo-18-ai-packs-an-rtx-5070-ti-and-32gb-of-memory",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T10:40:20+00:00",
    "summary": "Acer's Predator Helios Neo 18 AI gaming laptop hits a new all-time low price at Amazon. This massive 18-inch laptop freefalls by $600 in price."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/passenger-returning-from-def-con-34-spoofs-delta-wi-fi-network-while-in-flight-using-pentest-tool-pilots-tell-ground-crew-to-alert-corporate-security-after-attendee-from-hacking-conference-brings-the-party-to-the-sky",
    "domain": "AI 算力 / 半导体",
    "title": "Passenger returning from DEF CON 34 spoofs Delta Wi-Fi network while in flight using pentest tool — pilots tell ground crew to alert corporate security after attendee from hacking conference brings th",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/passenger-returning-from-def-con-34-spoofs-delta-wi-fi-network-while-in-flight-using-pentest-tool-pilots-tell-ground-crew-to-alert-corporate-security-after-attendee-from-hacking-conference-brings-the-party-to-the-sky",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T10:30:00+00:00",
    "summary": "A flight carrying passengers who attended a cybersecurity convention reportedly had its Wi-Fi network victimized by deauthentication attacks while an 'evil twin' hotspot rerouted potential victims to "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/intel-ceo-hints-at-return-to-the-memory-business-says-market-is-ripe-for-innovation-hints-at-stacking-memory-and-cpu",
    "domain": "AI 算力 / 半导体",
    "title": "Intel CEO hints at return to the memory business — says market is ripe for innovation, hints at stacking memory and CPU",
    "url": "https://www.tomshardware.com/pc-components/dram/intel-ceo-hints-at-return-to-the-memory-business-says-market-is-ripe-for-innovation-hints-at-stacking-memory-and-cpu",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T10:05:28+00:00",
    "summary": "Lip-Bu Tan says he has a pet project related to a new memory architecture."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/save-usd106-on-this-4tb-team-group-ssd-with-gen-4-speeds-now-10-2-cents-per-gb-newegg-coupon-deal-makes-this-t-force-g50-one-of-the-cheapest-pcie-4-0-drives-on-sale-right-now-with-this-amount-of-storage",
    "domain": "AI 算力 / 半导体",
    "title": "Save $106 on this 4TB Team Group SSD with Gen 4 speeds, now 10.2 cents per GB — Newegg coupon deal makes this T-Force G50 one of the cheapest PCIe 4.0 drives on sale right now with this amount of stor",
    "url": "https://www.tomshardware.com/pc-components/ssds/save-usd106-on-this-4tb-team-group-ssd-with-gen-4-speeds-now-10-2-cents-per-gb-newegg-coupon-deal-makes-this-t-force-g50-one-of-the-cheapest-pcie-4-0-drives-on-sale-right-now-with-this-amount-of-storage",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T10:03:01+00:00",
    "summary": "Get $106 off this 4TB TeamGroup T-Force G50 SSD, offering Gen 4 speeds and a huge capacity for a price that's hard to rival right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/commodore-re-releases-tac-2-joystick-after-40-years-for-just-usd49-says-retro-controller-is-tougher-than-ever-and-now-comes-in-five-colorways",
    "domain": "AI 算力 / 半导体",
    "title": "Commodore re-releases TAC-2 joystick after 40 years for just $49 — says retro-controller is tougher than ever and now comes in five colorways",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/commodore-re-releases-tac-2-joystick-after-40-years-for-just-usd49-says-retro-controller-is-tougher-than-ever-and-now-comes-in-five-colorways",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T10:00:11+00:00",
    "summary": "After 40 years, Commodore has brought back the 'Totally Accurate Controller' joystick, better known among C64 and Amiga aficionados as the TAC-2."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/independent-bookstores-in-europe-receive-suspicious-orders-for-thousands-of-books-prompting-fears-theyll-be-destroyed-to-train-ai-sellers-believe-acquisitions-are-part-of-ai-tech-companies-push-to-get-more-data",
    "domain": "AI 算力 / 半导体",
    "title": "Independent bookstores in Europe receive suspicious orders for thousands of books, prompting fears they'll be destroyed to train AI — sellers believe acquisitions are part of AI tech companies’ push t",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/independent-bookstores-in-europe-receive-suspicious-orders-for-thousands-of-books-prompting-fears-theyll-be-destroyed-to-train-ai-sellers-believe-acquisitions-are-part-of-ai-tech-companies-push-to-get-more-data",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T10:00:00+00:00",
    "summary": "Bookstores in Europe receive massive online purchases for obscure titles that haven't seen interest in years. They fear that these orders were made by AI firms looking to find more data to train their"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/resourceful-gamer-shrinks-valves-steam-deck-into-game-boy-with-custom-3d-printed-cooling-plans-display-around-1200x1080-90hz-amoled-panel",
    "domain": "AI 算力 / 半导体",
    "title": "Resourceful gamer shrinks Valve’s Steam Deck into Game Boy, with custom 3D-printed cooling — plans display around 1200x1080, 90Hz AMOLED panel",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/resourceful-gamer-shrinks-valves-steam-deck-into-game-boy-with-custom-3d-printed-cooling-plans-display-around-1200x1080-90hz-amoled-panel",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T09:30:00+00:00",
    "summary": "A Steam Deck enthusiast and modder is close to finalizing their ‘SteamBoy’ design."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/two-undersea-cables-reportedly-damaged-off-the-coast-of-perth-following-suspicious-vessel-activity-company-ceo-says-faults-happened-straight-after-each-other-and-in-close-proximity",
    "domain": "AI 算力 / 半导体",
    "title": "Two undersea cables reportedly damaged off the coast of Perth following suspicious vessel activity — company CEO says faults happened ‘straight after each other and in close proximity'",
    "url": "https://www.tomshardware.com/networking/two-undersea-cables-reportedly-damaged-off-the-coast-of-perth-following-suspicious-vessel-activity-company-ceo-says-faults-happened-straight-after-each-other-and-in-close-proximity",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T09:00:00+00:00",
    "summary": "Subco CEO Bevan Slattery said that the Australian Federal Police should determine what caused the shunt faults on two undersea cables, which happened in suspicious circumstances. They also noted that "
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/razer-naga-v3-pro-review",
    "domain": "AI 算力 / 半导体",
    "title": "Razer Naga V3 Pro Review: My new 23-button mouse",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/razer-naga-v3-pro-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T20:18:32+00:00",
    "summary": "Razer's Naga V3 Pro has the same form factor as its predecessor, but it features more buttons, an upgraded sensor and switches, and better battery life."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/sk-hynix-to-expand-production-capacity-in-china-as-it-mulls-solidigm-ipo-report-claims-second-phase-of-fab-could-boost-local-production-by-50-percent",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix to expand production capacity in China as it mulls Solidigm IPO, report claims — second phase of fab could boost local production by 50%",
    "url": "https://www.tomshardware.com/pc-components/ssds/sk-hynix-to-expand-production-capacity-in-china-as-it-mulls-solidigm-ipo-report-claims-second-phase-of-fab-could-boost-local-production-by-50-percent",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T16:39:42+00:00",
    "summary": "As demand for high-end data center SSDs peak, SK hynix upgrades its Chinese facilities and plans Solidigm listing at NASDAQ."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-highlights-ryzen-5-5500-briefly-topping-amazon-cpu-best-sellers-beating-9800x3d-usd80-ddr4-cpu-remains-a-top-seller-during-memory-crunch",
    "domain": "AI 算力 / 半导体",
    "title": "AMD highlights Ryzen 5 5500 briefly topping Amazon CPU best sellers, beating 9800X3D — $80 DDR4 CPU remains a top seller during memory crunch",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-highlights-ryzen-5-5500-briefly-topping-amazon-cpu-best-sellers-beating-9800x3d-usd80-ddr4-cpu-remains-a-top-seller-during-memory-crunch",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T15:06:35+00:00",
    "summary": "AMD's marketing director shared a screenshot of the Amazon CPU best sellers list, but the four-year-old, $80 Ryzen 5 5500 was at the top of the charts."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-raises-usd19-7-billion-to-help-fund-future-projects-as-14a-production-looms-share-sale-attracted-usd100-billion-in-demand-report-claims",
    "domain": "AI 算力 / 半导体",
    "title": "Intel raises $19.7 billion to help fund future projects as 14A production looms — share sale attracted $100 billion in demand, report claims",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-raises-usd19-7-billion-to-help-fund-future-projects-as-14a-production-looms-share-sale-attracted-usd100-billion-in-demand-report-claims",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T13:35:25+00:00",
    "summary": "Intel is raising $19.7 billion through a stock offering to strengthen its finances as it expands manufacturing capacity, develops next-generation process technologies, and is trying to attract major e"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/benchmarking-amds-bc-250-offering-steam-machine-like-performance-at-half-the-price-unlocking-40-cus-eight-zen-2-cores-on-the-repurposed-ps5-apu",
    "domain": "AI 算力 / 半导体",
    "title": "Benchmarking AMD's BC-250, offering Steam Machine-like performance at half the price — unlocking 40 CUs, eight Zen 2 cores on the repurposed PS5 APU",
    "url": "https://www.tomshardware.com/pc-components/cpus/benchmarking-amds-bc-250-offering-steam-machine-like-performance-at-half-the-price-unlocking-40-cus-eight-zen-2-cores-on-the-repurposed-ps5-apu",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T13:13:49+00:00",
    "summary": "The popular BC-250 APU has seen some major advancements over the past few months, including a 40CU unlock and enabling all eight Zen 2 cores. We put together a BC-250 machine to see how it works, and "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/air-cooling/deepcool-ak620-and-ak400-g2-review-quiet-and-powerful-with-woodgrain-or-a-digital-display",
    "domain": "AI 算力 / 半导体",
    "title": "DeepCool AK620 and AK400 G2 Review: Quiet and powerful, with woodgrain or a digital display",
    "url": "https://www.tomshardware.com/pc-components/air-cooling/deepcool-ak620-and-ak400-g2-review-quiet-and-powerful-with-woodgrain-or-a-digital-display",
    "source": "Albert Thomas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T12:05:00+00:00",
    "summary": "DeepCool’s latest AK G2 series air coolers feature your choice of woodgrain tops or a digital display. We’ve tested both AK620 and AK400 G2 coolers with AMD’s Ryzen 9 9950X3D to benchmark their therma"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/fcc-proposes-import-ban-on-chinese-optical-transceivers-blockade-targets-key-ai-interconnects-as-china-holds-56-percent-global-market-share",
    "domain": "AI 算力 / 半导体",
    "title": "FCC proposes import ban on Chinese optical transceivers — blockade targets key AI interconnects as China holds 56% global market share",
    "url": "https://www.tomshardware.com/tech-industry/fcc-proposes-import-ban-on-chinese-optical-transceivers-blockade-targets-key-ai-interconnects-as-china-holds-56-percent-global-market-share",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T12:03:36+00:00",
    "summary": "The FCC is drafting a proposal that would expand its list of equipment and services covered by the Secure Networks Act to include imports of new-model optical transceivers manufactured in China."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/usd580-million-undersea-cable-rerouted-to-avoid-the-grave-of-dobby-the-house-elf-company-caves-to-fan-demands-to-safeguard-harry-potter-filming-location-will-instead-pass-by-bronze-age-burial-site",
    "domain": "AI 算力 / 半导体",
    "title": "$580 million undersea cable rerouted to avoid the grave of Dobby the House Elf — company caves to fan demands to safeguard Harry Potter filming location, will instead pass by Bronze Age burial site",
    "url": "https://www.tomshardware.com/networking/usd580-million-undersea-cable-rerouted-to-avoid-the-grave-of-dobby-the-house-elf-company-caves-to-fan-demands-to-safeguard-harry-potter-filming-location-will-instead-pass-by-bronze-age-burial-site",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-11T11:47:22+00:00",
    "summary": "The Greenlink Connector project, which will connect the grid of Ireland and Wales, had to reroute its path after Harry Potter fans complained that it would 'desecrate' the 'grave' of beloved character"
  },
  {
    "id": "hn:49248477",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is pulling Wall Street into the AI buildout",
    "url": "https://thenextweb.com/news/nvidia-500-billion-wall-street-ai-infrastructure-funding-package",
    "source": "berkeleyjunk",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-10T19:25:07+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/why-ai-adoption-in-materials-rd-depends-more-on-people-than-technology/",
    "domain": "AI 算力 / 半导体",
    "title": "Why AI Adoption in Materials R&D Depends More on People Than Technology",
    "url": "https://www.eetimes.com/why-ai-adoption-in-materials-rd-depends-more-on-people-than-technology/",
    "source": "Ryo Matsushima",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T21:21:39+00:00",
    "summary": "The technology works. The organization has to catch up. The post Why AI Adoption in Materials R&amp;D Depends More on People Than Technology appeared first on EE Times."
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
    "id": "hn:49177126",
    "domain": "AI 算力 / 半导体",
    "title": "It looks like 'Big Short' investor Michael Burry nailed bet against chip stocks",
    "url": "https://www.businessinsider.com/big-short-michael-burry-ai-chip-stocks-soxx-nvidia-substack-2026-8",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-05T00:30:23+00:00",
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
    "id": "hn:49184755",
    "domain": "大厂 AI 动态",
    "title": "Changes at Google DeepMind: Demis Hassabis from CEO to Chair, Jeff Dean departs",
    "url": "https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/",
    "source": "colesantiago",
    "platform": "hackernews",
    "points": 864,
    "published_at": "2026-08-05T16:05:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:48993414",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/",
    "source": "logickkk1",
    "platform": "hackernews",
    "points": 760,
    "published_at": "2026-07-21T15:17:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49111237",
    "domain": "大厂 AI 动态",
    "title": "Gemini Robotics 2 brings whole body intelligence to robots",
    "url": "https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/",
    "source": "ai2027",
    "platform": "hackernews",
    "points": 620,
    "published_at": "2026-07-30T15:15:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49220126",
    "domain": "大厂 AI 动态",
    "title": "DeepMind's WeatherNext model achieves breakthrough forecasting cyclones",
    "url": "https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/",
    "source": "bhavansig",
    "platform": "hackernews",
    "points": 447,
    "published_at": "2026-08-08T09:18:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49267928",
    "domain": "大厂 AI 动态",
    "title": "llama.cpp",
    "url": "https://llama.app",
    "source": "kristianpaul",
    "platform": "hackernews",
    "points": 351,
    "published_at": "2026-08-12T04:51:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49184757",
    "domain": "大厂 AI 动态",
    "title": "Demis Hassabis is moving from CEO to Chairman at Google DeepMind",
    "url": "https://www.axios.com/2026/08/05/google-deepmind-demis-hassabis-ai",
    "source": "ot",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-08-05T16:05:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49096188",
    "domain": "大厂 AI 动态",
    "title": "Document-borne AI worms can self-propagate through Copilot for Word",
    "url": "https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/",
    "source": "Canopy9560",
    "platform": "hackernews",
    "points": 384,
    "published_at": "2026-07-29T11:44:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49259339",
    "domain": "大厂 AI 动态",
    "title": "Apple Silicon and macOS VMs: Faster LLM Inference with llama.cpp",
    "url": "https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md",
    "source": "frabonacci",
    "platform": "hackernews",
    "points": 302,
    "published_at": "2026-08-11T14:50:33+00:00",
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
    "id": "hn:49256057",
    "domain": "大厂 AI 动态",
    "title": "What I learned by putting GitHub Copilot behind a MitM proxy",
    "url": "https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm",
    "source": "j0selit0",
    "platform": "hackernews",
    "points": 189,
    "published_at": "2026-08-11T10:40:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49067285",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://www.lesswrong.com/posts/iKm2FhpWkuuBojm82/why-i-left-google-deepmind",
    "source": "eatitraw",
    "platform": "hackernews",
    "points": 200,
    "published_at": "2026-07-27T09:56:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49198583",
    "domain": "大厂 AI 动态",
    "title": "Show HN: The Channels SDK – Bring Any Agent to Any Channel (Slack, MS Teams)",
    "url": "https://github.com/CopilotKit/channels-sdk",
    "source": "davidmckayv",
    "platform": "hackernews",
    "points": 121,
    "published_at": "2026-08-06T16:05:51+00:00",
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
    "points": 136,
    "published_at": "2026-07-21T21:27:54+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/979241/made-by-google-2026-live-blog-pixel-11-trevor-noah",
    "domain": "大厂 AI 动态",
    "title": "Pixel 11 event live blog: Let&#8217;s watch Trevor Noah introduce Google&#8217;s new phones",
    "url": "https://www.theverge.com/tech/979241/made-by-google-2026-live-blog-pixel-11-trevor-noah",
    "source": "David Imel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T21:30:00+00:00",
    "summary": "It's almost time for the Made by Google keynote, where the company will show off the brand-new Pixel hardware it announced today. Like last year, it'll be a celebrity-packed live show, though Trevor N"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/979263/8bitdo-mechanical-keyboard-galaxy-25-edge-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "This 8BitDo mechanical keyboard has an extra keypad and is 30 percent off",
    "url": "https://www.theverge.com/gadgets/979263/8bitdo-mechanical-keyboard-galaxy-25-edge-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T21:21:09+00:00",
    "summary": "If you’re looking for a mechanical keyboard that can give your desk a touch of retro flair, Amazon has 8BitDo’s Retro Mechanical Keyboard with Dual Super Buttons on sale for $69.99, one of the lowest "
  },
  {
    "id": "rss:https://www.theverge.com/tech/979295/petlibro-outage-smart-pet-feeders",
    "domain": "大厂 AI 动态",
    "title": "Cats and dogs are missing meals after a popular smart feeder went down",
    "url": "https://www.theverge.com/tech/979295/petlibro-outage-smart-pet-feeders",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T21:07:17+00:00",
    "summary": "A Petlibro outage is preventing its smart pet feeders and other devices from performing scheduled tasks, like dispensing food. The outage began on Tuesday, with users across Reddit reporting that thei"
  },
  {
    "id": "rss:https://www.theverge.com/games/977985/kinetic-publishing-showcase-sam-barlow-precognition",
    "domain": "大厂 AI 动态",
    "title": "The next big indie game publisher is taking some exciting swings",
    "url": "https://www.theverge.com/games/977985/kinetic-publishing-showcase-sam-barlow-precognition",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T19:30:00+00:00",
    "summary": "Kinetic Publishing, a new indie publisher from the development team behind the co-op horror game Phasmophobia, just hosted its first games showcase, and it includes five ambitious new titles set to re"
  },
  {
    "id": "rss:https://www.theverge.com/tech/979231/apple-base-iphone-18-launch-delayed",
    "domain": "大厂 AI 动态",
    "title": "It looks like Apple&#8217;s iPhone 18 really will skip the fall launch this year",
    "url": "https://www.theverge.com/tech/979231/apple-base-iphone-18-launch-delayed",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T19:27:47+00:00",
    "summary": "According to an Economic Daily News report spotted by MacRumors, executives for Apple supplier Pegatron confirmed during an earnings call that the iPhone 18 Pro series phones will launch this fall, bu"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/975970/google-pixel-11-series-where-to-buy-preorder-release-date",
    "domain": "大厂 AI 动态",
    "title": "Google’s Pixel 11 phone preorders come with up to $350 in gift cards",
    "url": "https://www.theverge.com/gadgets/975970/google-pixel-11-series-where-to-buy-preorder-release-date",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T17:47:54+00:00",
    "summary": "Looking to get your hands on the latest Pixel devices? After weeks of leaks and rumors, Google has officially announced its next generation of Pixel phones and watches. The base Pixel 11 starts at $89"
  },
  {
    "id": "rss:https://www.theverge.com/tech/979112/twitch-streamers-can-now-opt-out-from-training-amazons-ai",
    "domain": "大厂 AI 动态",
    "title": "Twitch streamers can now opt out from training Amazon’s AI",
    "url": "https://www.theverge.com/tech/979112/twitch-streamers-can-now-opt-out-from-training-amazons-ai",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T17:29:10+00:00",
    "summary": "Twitch users can now opt out of allowing their content to be used to train Amazon's generative AI models. Opting out means that \"your streams, VODs, clips, stream chats, and pictures and text on your "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/975237/google-pixel-11-pro-comparison-specs-price-features",
    "domain": "大厂 AI 动态",
    "title": "How Google’s new Pixel 11 phones compare to last year’s models",
    "url": "https://www.theverge.com/gadgets/975237/google-pixel-11-pro-comparison-specs-price-features",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T17:00:00+00:00",
    "summary": "Google just added four new phones to the Pixel family: the Pixel 11, Pixel 11 Pro, Pixel 11 Pro XL, and the Pixel 11 Pro Fold. They're slightly more expensive than their predecessors, but they come wi"
  },
  {
    "id": "rss:https://www.theverge.com/policy/979010/ice-agents-electric-shock-gloves",
    "domain": "大厂 AI 动态",
    "title": "ICE wants to give agents electrified gloves that shock people into compliance",
    "url": "https://www.theverge.com/policy/979010/ice-agents-electric-shock-gloves",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T16:58:29+00:00",
    "summary": "Immigration and Customs Enforcement (ICE) is aiming to spend up to $20 million on equipping officers and agents with specialized gloves that deliver painful electric shocks. These plans were outlined "
  },
  {
    "id": "rss:https://www.theverge.com/tech/979070/amazon-mmo-throne-and-liberty-lost-ark-live-operations",
    "domain": "大厂 AI 动态",
    "title": "Amazon gets out of the MMO game",
    "url": "https://www.theverge.com/tech/979070/amazon-mmo-throne-and-liberty-lost-ark-live-operations",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T16:46:05+00:00",
    "summary": "Amazon is fully stepping back from MMOs. After saying last year that it would be halting \"a significant amount\" of its work on first-party AAA games, \"specifically around MMOs,\" Amazon will be handing"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/some-claude-users-are-mad-that-anthropics-new-watermarks-will-catch-them-cheating-at-their-jobs-classes/",
    "domain": "大厂 AI 动态",
    "title": "Some Claude users are mad that Anthropic’s new watermarks will catch them using it at their jobs, classes",
    "url": "https://techcrunch.com/2026/08/12/some-claude-users-are-mad-that-anthropics-new-watermarks-will-catch-them-cheating-at-their-jobs-classes/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T22:26:37+00:00",
    "summary": "Is Anthropic's new watermarking system a travesty? Some have taken to social media to complain that it is."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/ai-nuclear-power-firm-fermi-finally-has-a-new-ceo/",
    "domain": "大厂 AI 动态",
    "title": "AI nuclear power firm Fermi finally has a new CEO",
    "url": "https://techcrunch.com/2026/08/12/ai-nuclear-power-firm-fermi-finally-has-a-new-ceo/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T22:24:00+00:00",
    "summary": "Lee McIntire, an independent member of Fermi's board, has been hired as CEO, more than three months since the company fired co-founder Toby Neugebauer from the top post."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/northrops-robot-space-mechanic-is-a-new-way-to-keep-satellites-at-work-longer/",
    "domain": "大厂 AI 动态",
    "title": "Northrop’s robot space mechanic is a new way to keep satellites at work longer",
    "url": "https://techcrunch.com/2026/08/12/northrops-robot-space-mechanic-is-a-new-way-to-keep-satellites-at-work-longer/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T20:53:41+00:00",
    "summary": "The Mission Robotic Vehicle is making the first attempt to attach a new thruster to an aging satellite."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/amazon-will-train-on-twitch-streamers-content-by-default-unless-they-opt-out/",
    "domain": "大厂 AI 动态",
    "title": "Amazon will train on Twitch streamers’ content by default, unless they opt out",
    "url": "https://techcrunch.com/2026/08/12/amazon-will-train-on-twitch-streamers-content-by-default-unless-they-opt-out/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T20:10:40+00:00",
    "summary": "\"If this was opt-in, nobody would opt in,\" Twitch CPO Mike Minton said on a livestream responding to user feedback. \"That's honestly the answer.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/grubhubs-24m-ftc-settlement-is-finally-reaching-diners-and-drivers/",
    "domain": "大厂 AI 动态",
    "title": "Grubhub’s $24M FTC settlement is finally reaching diners and drivers",
    "url": "https://techcrunch.com/2026/08/12/grubhubs-24m-ftc-settlement-is-finally-reaching-diners-and-drivers/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T18:34:21+00:00",
    "summary": "Checks are being mailed from Grubhub's $23.8 million fine from the FTC after it settled allegations over its business practices."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/ai-coding-startup-cognition-reportedly-already-in-talks-to-raise-at-40b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "AI coding startup Cognition reportedly already in talks to raise at $40B valuation",
    "url": "https://techcrunch.com/2026/08/12/ai-coding-startup-cognition-reportedly-already-in-talks-to-raise-at-40b-valuation/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T18:19:12+00:00",
    "summary": "Cognition may be looking to raise another mega round just a few months after raising $1 billion at a $26 billion valuation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/as-ai-safety-concerns-mount-three-pioneers-make-the-case-for-staying-open/",
    "domain": "大厂 AI 动态",
    "title": "As AI safety concerns mount, three pioneers make the case for staying open",
    "url": "https://techcrunch.com/2026/08/12/as-ai-safety-concerns-mount-three-pioneers-make-the-case-for-staying-open/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T17:51:00+00:00",
    "summary": "At Ai4, three of the world's most respected AI experts — Geoffrey Hinton, Fei-Fei Li, and Andrew Ng — debated regulation, open source access, and how America can compete as China advances in Asia."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/openai-backed-thrive-holdings-raises-2b-to-bring-ai-to-the-enterprise/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI-backed Thrive Holdings raises $2B to bring AI to the enterprise",
    "url": "https://techcrunch.com/2026/08/12/openai-backed-thrive-holdings-raises-2b-to-bring-ai-to-the-enterprise/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T17:41:29+00:00",
    "summary": "Thrive Holdings has raised $2 billion in new funding at a $12 billion valuation from investors like SoftBank, D1 Capital Partners, and Altimeter Capital."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/uber-freight-reportedly-investigating-after-hacking-group-claims-data-breach/",
    "domain": "大厂 AI 动态",
    "title": "Uber Freight reportedly investigating after hacking group claims data breach",
    "url": "https://techcrunch.com/2026/08/12/uber-freight-reportedly-investigating-after-hacking-group-claims-data-breach/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T17:15:41+00:00",
    "summary": "An extortion gang known for targeting transportation companies and private equity firms has taken credit for a breach at Uber Freight."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/mesh-automattics-crm-for-everyone-comes-to-android/",
    "domain": "大厂 AI 动态",
    "title": "Mesh, Automattic’s CRM for everyone, comes to Android",
    "url": "https://techcrunch.com/2026/08/12/mesh-automattics-crm-for-everyone-comes-to-android/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T16:57:58+00:00",
    "summary": "Mesh, an AI-powered contacts app and relationship manager from Automattic, is now an Android app."
  },
  {
    "id": "rss:https://techcrunch.com/video/why-stream-ring-maker-sandbar-says-the-future-of-ai-wearables-is-voice/",
    "domain": "大厂 AI 动态",
    "title": "Why Stream ring-maker Sandbar says the future of AI wearables is voice",
    "url": "https://techcrunch.com/video/why-stream-ring-maker-sandbar-says-the-future-of-ai-wearables-is-voice/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T16:46:02+00:00",
    "summary": "AI notetaking hardware has taken off&#160;over&#160;the past&#160;couple of years, with credit-card-sized devices, pendants, pins,&#160;and&#160;even transcribing earbuds all promising to capture your"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/tesla-wants-to-build-a-10b-solar-factory-in-texas/",
    "domain": "大厂 AI 动态",
    "title": "Tesla wants to build a $10B solar factory in Texas",
    "url": "https://techcrunch.com/2026/08/12/tesla-wants-to-build-a-10b-solar-factory-in-texas/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T16:18:31+00:00",
    "summary": "Tesla wants to build a massive solar factory in Texas, but first it wants the state to chip in to defray the costs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/form-energy-raises-750m-to-build-more-100-hour-batteries-for-the-grid/",
    "domain": "大厂 AI 动态",
    "title": "Form Energy raises $750M to build more 100-hour batteries for the grid",
    "url": "https://techcrunch.com/2026/08/12/form-energy-raises-750m-to-build-more-100-hour-batteries-for-the-grid/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T16:18:23+00:00",
    "summary": "Form Energy has landed Google and Crusoe as customers. Now, it has raised $750 million to expand manufacturing to deliver its massive, 100-hour batteries."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/lovable-confirms-new-13-3b-valuation-raises-another-400m/",
    "domain": "大厂 AI 动态",
    "title": "Lovable confirms new $13.3B valuation, raises another $400M",
    "url": "https://techcrunch.com/2026/08/12/lovable-confirms-new-13-3b-valuation-raises-another-400m/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T16:04:27+00:00",
    "summary": "This new funding comes after Lovable hit $500 million in annualized run rate revenue in June, the startup told TechCrunch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/facebook-officially-rolls-out-its-standalone-creator-studio-app-with-ai-tools-for-creators/",
    "domain": "大厂 AI 动态",
    "title": "Facebook officially rolls out its stand-alone Creator Studio app with AI tools for creators",
    "url": "https://techcrunch.com/2026/08/12/facebook-officially-rolls-out-its-standalone-creator-studio-app-with-ai-tools-for-creators/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T15:56:13+00:00",
    "summary": "The new app launches with Facebook's AI creator assistant built into it, providing creators with personalized recommendations based on their content style, performance, audience engagement, and goals."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/how-a-250-million-acquisition-collapsed-into-allegations-of-fraud-and-forged-signatures/",
    "domain": "大厂 AI 动态",
    "title": "How a $250 million acquisition collapsed into allegations of fraud and forged signatures",
    "url": "https://techcrunch.com/2026/08/12/how-a-250-million-acquisition-collapsed-into-allegations-of-fraud-and-forged-signatures/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T15:44:56+00:00",
    "summary": "Investors are still waiting for their share of the $250 million windfall, and VideoVerse co-founder Vinayak Shrivastav is now at the center of multiple legal cases."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/after-microsoft-threatened-legal-action-a-security-researcher-publishes-a-new-windows-zero-day-bug/",
    "domain": "大厂 AI 动态",
    "title": "After Microsoft threatened legal action, a security researcher publishes a new Windows zero-day bug",
    "url": "https://techcrunch.com/2026/08/12/after-microsoft-threatened-legal-action-a-security-researcher-publishes-a-new-windows-zero-day-bug/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T15:18:55+00:00",
    "summary": "This is the latest zero-day released by security researcher Nightmare Eclipse, despite Microsoft publicly threatening to take legal action against them."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/silkroad-innovation-hubs-road-to-battlefield-competition-continues/",
    "domain": "大厂 AI 动态",
    "title": "Silkroad Innovation Hub’s Road to Battlefield competition continues",
    "url": "https://techcrunch.com/2026/08/12/silkroad-innovation-hubs-road-to-battlefield-competition-continues/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T15:02:00+00:00",
    "summary": "The Road to Battlefield competition is now in its second year, and its purpose is to give founders across Central Eurasia a direct route to Startup Battlefield"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/google-unveils-pixel-11-lineup-new-airtag-rival-and-gemini-features-at-made-by-google-2026/",
    "domain": "大厂 AI 动态",
    "title": "Everything announced at Made by Google ’26: Pixel 11, Pixel Watch 5, Pixel Tag, and tons of Gemini features",
    "url": "https://techcrunch.com/2026/08/12/google-unveils-pixel-11-lineup-new-airtag-rival-and-gemini-features-at-made-by-google-2026/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T14:20:33+00:00",
    "summary": "From the Pixel 11 series and a brand new competitor to Apple’s AirTag, here are all the announcements from the Made by Google 2026 event."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/12/googles-quick-share-adds-a-tap-to-share-mode/",
    "domain": "大厂 AI 动态",
    "title": "Google’s Quick Share adds a tap-to-share mode",
    "url": "https://techcrunch.com/2026/08/12/googles-quick-share-adds-a-tap-to-share-mode/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T14:13:03+00:00",
    "summary": "Google's Quick Share feature is getting a tap-to-share mode for quickly exchanging contacts, photos, videos, and more."
  },
  {
    "id": "rss:https://stratechery.com/2026/anthropics-watermarking-how-it-probably-works-worse-than-it-seems/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s Watermarking, How It (Probably) Works, Worse Than It Seems",
    "url": "https://stratechery.com/2026/anthropics-watermarking-how-it-probably-works-worse-than-it-seems/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T10:00:00+00:00",
    "summary": "Anthropic is adding watermarking in response to the E.U.'s AI law. It's a terrible idea, first and foremost for philosophical reasons."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/08/an-ultra-rare-amoeba-was-destroying-a-toddlers-brain-doctors-missed-it/",
    "domain": "大厂 AI 动态",
    "title": "Toddler's tragic death from brain-destroying amoeba offers lessons for doctors",
    "url": "https://arstechnica.com/health/2026/08/an-ultra-rare-amoeba-was-destroying-a-toddlers-brain-doctors-missed-it/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T22:31:19+00:00",
    "summary": "Boy's unusual symptoms could help identify the next case sooner."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/08/new-font-turns-ordinary-webpages-into-nonsense-for-ai-scrapers/",
    "domain": "大厂 AI 动态",
    "title": "The web’s newest weapon against AI scrapers is a font",
    "url": "https://arstechnica.com/ai/2026/08/new-font-turns-ordinary-webpages-into-nonsense-for-ai-scrapers/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T22:02:25+00:00",
    "summary": "“ShieldFont” aims to poison AI training data without making pages unreadable for people."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/08/terabytes-of-credentials-leaked-in-massive-supply-chain-attack/",
    "domain": "大厂 AI 动态",
    "title": "Terabytes of credentials leaked in massive supply-chain attack",
    "url": "https://arstechnica.com/security/2026/08/terabytes-of-credentials-leaked-in-massive-supply-chain-attack/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T21:43:21+00:00",
    "summary": "The data was scraped and exfiltrated from 2,500 users of a compromised AI package."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/have-physicists-finally-discovered-glueballs-new-evidence-points-to-yes/",
    "domain": "大厂 AI 动态",
    "title": "Have physicists finally discovered glueballs? New evidence points to yes.",
    "url": "https://arstechnica.com/science/2026/08/have-physicists-finally-discovered-glueballs-new-evidence-points-to-yes/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-12T21:13:39+00:00",
    "summary": "“It’s the strongest evidence yet that particles dominated by a glueball component can exist in nature.”"
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
    "points": 157,
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
    "id": "hn:49261857",
    "domain": "股票",
    "title": "The SpaceX Sham",
    "url": "https://dissentmagazine.org/online_articles/spacex-ipo-elon-musk-trillionaire/",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-08-11T17:47:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49166182",
    "domain": "股票",
    "title": "Bending Spoons makes first post-IPO acquisition with $1.3B Airtable deal",
    "url": "https://live.euronext.com/en/financial-news/bending-spoons-makes-first-post-ipo-acquisition-13-billion-airtable-deal",
    "source": "riffraff",
    "platform": "hackernews",
    "points": 116,
    "published_at": "2026-08-04T09:27:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49257407",
    "domain": "股票",
    "title": "I backtested my own stock rankings. They lost to the index",
    "url": "https://holderdashboard.com/learn/backtest-that-lost-to-the-index",
    "source": "caiocmpaes",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-08-11T12:44:43+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3779352",
    "domain": "股票",
    "title": "盈利超预期、回购破纪录、散户回归——Citadel十大理由看多8月美股",
    "url": "https://wallstreetcn.com/articles/3779352",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:08:45+00:00",
    "summary": "“8月可能是买家回归的月份。9月可能要问的是，还剩多少买入弹药。”Citadel10大理由看多8月美股：Q2盈利增速约33%，创后衰退期以来最强；ETF年初至今净流入1.6万亿美元，7月单月创纪录；超1万亿美元回购本周重新开窗等，该机构认为，去杠杆已趋成熟，多股买力正同步增强，卖压正在消退。"
  },
  {
    "id": "wscn:3779351",
    "domain": "股票",
    "title": "逆周期加码与流动性破局：宽松条件是否已具备？",
    "url": "https://wallstreetcn.com/premium/articles/3779351?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:04:31+00:00",
    "summary": "银行负债缺口、政府债供给高峰与资金回笼压力叠加，宽松客观条件正在逐步成熟。"
  },
  {
    "id": "wscn:3779335",
    "domain": "股票",
    "title": "创业板、科创50均涨1%，CRO、创新药爆发，算力硬件延续强势，恒科指震荡涨0.3%，腾讯跌近4%",
    "url": "https://wallstreetcn.com/articles/3779335",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:03:57+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市超3000股飘绿，上午半天成交1.6万亿。沪深两市半日成交额1.59万亿，较上个交易日放量超2000亿。板块方面，CRO、创新药概念股持续爆发；算力硬件、半导体产业链反弹，CPO、GPU方向领涨；脑机接口、大消费、商业航天概念股活跃。工业金属、黄金、油气、地产、煤炭板块跌幅靠前。"
  },
  {
    "id": "wscn:3779348",
    "domain": "股票",
    "title": "Kalshi寻求400亿美元估值融资，红杉与Wellington洽谈领投",
    "url": "https://wallstreetcn.com/articles/3779348",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T03:20:24+00:00",
    "summary": "预测市场龙头Kalshi正以400亿美元估值寻求至少7.5亿美元新融资，红杉资本与Wellington Management洽谈共同领投。距其今年5月完成220亿美元估值的10亿美元融资仅约三个月，估值近乎翻倍。7月年化营收突破40亿美元、世界杯效应推动流量爆发等共同构成本轮高估值的支撑逻辑。"
  },
  {
    "id": "wscn:3779347",
    "domain": "股票",
    "title": "日本PPI连续高位运行，日央行9月加息预期升温",
    "url": "https://wallstreetcn.com/articles/3779347",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T03:18:34+00:00",
    "summary": "日本7月PPI同比涨7.2%，持续高位运行，石油、化工、有色金属三大类别齐涨，叠加日元跌至40年低位加剧输入性通胀，上半年\"通胀型破产\"更创历史同期新高。企业成本压力、工资上涨与日元贬值三重共振，日央行行长植田和男此前释放9月加息信号，货币政策正常化进程或加速。"
  },
  {
    "id": "wscn:3779349",
    "domain": "股票",
    "title": "CPI数据为黄金多头扫清最后障碍？",
    "url": "https://wallstreetcn.com/articles/3779349",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T03:08:10+00:00",
    "summary": "美国7月通胀数据公布后，黄金再次冲上4400美元大关。\n美国7月CPI从3.5%降至3.4%，核心C..."
  },
  {
    "id": "wscn:3779342",
    "domain": "股票",
    "title": "华尔街解读腾讯财报：基本盘稳住了，但AI投入周期拉长，利润兑现仍需时间",
    "url": "https://wallstreetcn.com/articles/3779342",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T03:02:24+00:00",
    "summary": "腾讯二季度基本盘稳健，但资本开支单季暴增至528亿元，自由现金流转负，AI账单已实质冲击利润表，下半年资本开支预计进一步扩大，瑞银测算显示全年资本开支预期已由此前的1700亿元上调至2500亿元。高盛、瑞银等四大投行集体下调盈利预测，核心问题在于：混元模型、微信Agent、WorkBuddy的商业化速度，能否追上持续攀升的训练与推理成本。"
  },
  {
    "id": "wscn:3779056",
    "domain": "股票",
    "title": "解密央行版“权力的游戏”：原美联储高级经济学家胡捷带你看清全球第一央行的变局与冲击",
    "url": "https://wallstreetcn.com/articles/3779056",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T03:00:24+00:00",
    "summary": "2026年9月6日，上海交通大学高级金融学院教授，原美联储高级经济学家胡捷带你读懂美联储背后的权利博弈"
  },
  {
    "id": "wscn:3779346",
    "domain": "股票",
    "title": "上半年营收增速创近5年新高，浦发银行迎来盈利修复与资本考验",
    "url": "https://wallstreetcn.com/articles/3779346",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T02:55:09+00:00",
    "summary": "随着半年度业绩快报的发布，浦发银行上半年经营状况浮出水面。\n8月12日，浦发银行披露，2026年上半..."
  },
  {
    "id": "wscn:3779345",
    "domain": "股票",
    "title": "「0碳未来·ESG创新实践榜」第四届，正式启动",
    "url": "https://wallstreetcn.com/articles/3779345",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T02:53:54+00:00",
    "summary": "报名快速通道：https://forms.wallstreetcn.com/f/FqqnZa\nES..."
  },
  {
    "id": "wscn:3779344",
    "domain": "股票",
    "title": "文远知行在海外卖“虚拟司机”",
    "url": "https://wallstreetcn.com/articles/3779344",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T02:48:50+00:00",
    "summary": "海外L4收技术费，L2++规模装车。"
  },
  {
    "id": "wscn:3779339",
    "domain": "股票",
    "title": "高盛：日本外汇储备逾万亿美元，为进一步干预日元提供充足弹药",
    "url": "https://wallstreetcn.com/articles/3779339",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T02:41:26+00:00",
    "summary": "高盛指出，日本约1万亿美元外汇储备中，约2000亿美元可立即动用，足以支撑“再来几轮”上月规模的干预；若借道美联储FIMA回购工具，理论上全部储备均可变现。这一判断已推动客户情绪明显转向看多日元。但高盛同时警告，干预只是“争取时间”，能否持续取决于日本央行9月是否加息及美国经济数据走向。"
  },
  {
    "id": "wscn:3779338",
    "domain": "股票",
    "title": "AI交易回暖，韩股重回技术牛市，三星电子、SK海力士双双涨逾4%",
    "url": "https://wallstreetcn.com/articles/3779338",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T02:40:51+00:00",
    "summary": "周四亚太时段，MSCI亚太指数整体上涨约1%，日经225指数上涨1.2%，欧洲斯托克50期货上扬0.3%。韩国综合股价指数领涨，盘中一度涨逾4.8%，较7月30日低点累计反弹约22%，正式进入技术性牛市区间。三星电子和SK海力士双双涨逾4%。通胀不及预期打压加息预期，为金价反弹提供了支撑，黄金一度上涨0.5%。"
  },
  {
    "id": "wscn:3779343",
    "domain": "股票",
    "title": "汇丰财富洞察：美联储减少前瞻性指引对美国利率意味着什么？|汇听环球财富",
    "url": "https://wallstreetcn.com/premium/articles/3779343?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T02:36:18+00:00",
    "summary": "美联储强调依赖经济数据做出决策，这意味着利率预期可能会更频繁地发生变化，导致市场波动加剧。我们..."
  },
  {
    "id": "wscn:3779328",
    "domain": "股票",
    "title": "特朗普宣称“已完全控制霍尔木兹”，但油轮还是不敢走",
    "url": "https://wallstreetcn.com/articles/3779328",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T02:14:35+00:00",
    "summary": "特朗普高调宣称\"完全控制霍尔木兹海峡\"，现实却截然相反——战前日均逾130艘船只通行，周二降至14艘，跌幅超九成，周三更是骤降至仅1艘。伊朗无需击败美国海军，仅凭间歇性袭击与不确定性，便将单次过境战争险保费从0.25%推高至船值10%。恐惧本身已成武器，全球能源供应与通胀压力正悄然向美国中期选举逼近。"
  },
  {
    "id": "wscn:3779337",
    "domain": "股票",
    "title": "智谱领衔33只中国股票入选MSCI指数，海外被动资金将于月底集中涌入",
    "url": "https://wallstreetcn.com/articles/3779337",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T01:48:34+00:00",
    "summary": "MSCI公布2026年8月指数审议结果，智谱以新兴市场新增成分股市值第一的身份入选MSCI中国指数，凯莱英、华峰测控、燕东微等共33只中国股票同步纳入，万科A、智飞生物等32只遭剔除。所有变动8月31日收盘后生效，相关个股届时将迎来海外被动资金集中调仓。"
  },
  {
    "id": "wscn:3779334",
    "domain": "股票",
    "title": "美日联合干预效力消退，日元回到159关口考验政策极限",
    "url": "https://wallstreetcn.com/articles/3779334",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T01:48:08+00:00",
    "summary": "尽管7月底美日联手将日元从163拉升至155，但美债收益率高企与油价攀升令套利交易重燃，美日利差逾180基点持续压制日元。市场普遍认为，干预仅能抑制投机、争取时间，160被视为当局政治红线。日元持续反弹的关键，在于日本央行加快政策正常化及提升本国资产吸引力。"
  },
  {
    "id": "wscn:3779276",
    "domain": "股票",
    "title": "国产化率1%的静电卡盘： 半导体制造\"隐形心脏\"，百亿赛道能否实现技术突破？",
    "url": "https://wallstreetcn.com/premium/articles/3779276?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T01:36:39+00:00",
    "summary": "静电卡盘是中国半导体零部件领域卡脖子排名第一的方向，2026-2028年是国产替代从\"验证导入\"向\"批量交付\"跃迁的关键窗口期。国产化率不足1%，是否能够实现技术突破？"
  },
  {
    "id": "wscn:3779333",
    "domain": "股票",
    "title": "WorkBuddy存在感极强——腾讯Q2财报电话会的10点观察与思考",
    "url": "https://wallstreetcn.com/articles/3779333",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T01:22:39+00:00",
    "summary": "WorkBuddy跃升中国AI生产力服务互动量第一，腾讯果断向其倾斜资源、压降元宝优先级；资本开支暴增至527亿元、自由现金流首次转负，每天烧钱超1亿。混元Hy4年底发布、小微能力仍在“收着”——这场AI豪赌，腾讯正全力以赴。"
  },
  {
    "id": "wscn:3779331",
    "domain": "股票",
    "title": "新美联储通讯社：通胀数据\"不冷不热\"，美联储暂获喘息但前路未明",
    "url": "https://wallstreetcn.com/articles/3779331",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T01:13:04+00:00",
    "summary": "Nick Timiraos指出，美国7月通胀数据符合预期，市场对美联储9月加息的押注已跌破50%，短期加息压力有所缓解。然而，美联储内部鹰鸽分歧激烈，超半数投票委员倾向加息，旧金山联储主席更暗示若通胀失控或需一次性加息50个基点。主席沃什态度模糊，真正的政策走向或要等到9月11日8月通胀数据出炉后方能揭晓。"
  },
  {
    "id": "hn:49151871",
    "domain": "股票",
    "title": "Situational Awareness and the Impending Stock Market Volatility",
    "url": "https://www.emergingtrajectories.com/lh/situational-awareness-bigger-picture/",
    "source": "cl42",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-08-03T06:17:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:49137024",
    "domain": "股票",
    "title": "Oil companies report sky-high profits thanks to wartime crude prices",
    "url": "https://www.npr.org/2026/07/31/nx-s1-5910660/big-oil-earnings-q2-2026",
    "source": "speckx",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-08-01T18:28:06+00:00",
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
    "id": "hn:49111879",
    "domain": "股票",
    "title": "Citadel Buys Situational Awareness's Stock Portfolio After Big Losses in AI",
    "url": "https://www.wsj.com/finance/citadel-buys-situational-awarenesss-stock-portfolio-after-big-losses-in-ai-5117159b",
    "source": "mudil",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-07-30T16:00:33+00:00",
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
    "id": "hn:49195657",
    "domain": "股票",
    "title": "The Investors Whose SpaceX Shares Vanished Before They Could Cash In",
    "url": "https://www.wsj.com/finance/stocks/spacex-ipo-spv-investors-2698a174",
    "source": "doener",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-06T12:19:44+00:00",
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
    "id": "hn:49162737",
    "domain": "股票",
    "title": "Palantir soars 12% on blowout quarter, with US commercial revenue soaring ~150%",
    "url": "https://www.cnbc.com/2026/08/03/palantir-pltr-earnings-q2-2026.html",
    "source": "gslin",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-08-03T23:36:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49145809",
    "domain": "股票",
    "title": "As Reddit stock falls, CEO questions value of Google's AI Overviews",
    "url": "https://arstechnica.com/ai/2026/08/reddit-ceo-on-ai-overviews-were-still-looking-for-that-win-win/",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-02T16:09:26+00:00",
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
    "id": "rss:https://www.netinterest.co/p/leopolds-fall",
    "domain": "股票",
    "title": "Leopold’s Fall",
    "url": "https://www.netinterest.co/p/leopolds-fall",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T10:05:15+00:00",
    "summary": "Situational Awareness and Amaranth 20 Years Apart"
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
    "id": "hn:49175192",
    "domain": "金融",
    "title": "Thanks FedEx, This Is Why We Keep Getting Phished (2024)",
    "url": "https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/",
    "source": "stymaar",
    "platform": "hackernews",
    "points": 337,
    "published_at": "2026-08-04T21:09:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49200390",
    "domain": "金融",
    "title": "Federal Communications Commission scraps limit on broadcast TV ownership",
    "url": "https://www.nbcnews.com/business/media/federal-communications-commission-scraps-limit-broadcast-tv-ownership-rcna587641",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 179,
    "published_at": "2026-08-06T18:22:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49245487",
    "domain": "金融",
    "title": "Study links GLP-1 drugs to bigger jump in women's employment than a degree",
    "url": "https://finance.yahoo.com/healthcare/articles/harvard-study-links-glp-1-123000637.html",
    "source": "metadat",
    "platform": "hackernews",
    "points": 130,
    "published_at": "2026-08-10T16:02:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49259043",
    "domain": "金融",
    "title": "Federal vendor with $50M in contracts leaves portal broken for a month",
    "url": "https://www.propublica.org/article/foia-requests-responses",
    "source": "ams1",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-08-11T14:32:21+00:00",
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
    "id": "hn:49245071",
    "domain": "金融",
    "title": "Force-Fed by ICE",
    "url": "https://www.theguardian.com/us-news/2026/aug/10/ice-force-feeding-detention-gabar-choli",
    "source": "HotGarbage",
    "platform": "hackernews",
    "points": 97,
    "published_at": "2026-08-10T15:35:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:49118696",
    "domain": "金融",
    "title": "The bond market isn’t buying what Fed Chair Warsh is selling",
    "url": "https://www.reuters.com/commentary/reuters-open-interest/bond-market-isnt-buying-what-fed-chair-warsh-is-selling-2026-07-30/",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 139,
    "published_at": "2026-07-31T03:32:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49046525",
    "domain": "金融",
    "title": "The Fedora 45 Sausage Factory",
    "url": "https://supakeen.com/weblog/the-fedora-45-sausage-factory/",
    "source": "6581",
    "platform": "hackernews",
    "points": 158,
    "published_at": "2026-07-25T11:04:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49243531",
    "domain": "金融",
    "title": "China is now the world's greatest oil power",
    "url": "https://www.economist.com/finance-and-economics/2026/08/09/china-is-now-the-worlds-great-oil-power",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-08-10T13:40:46+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.11371",
    "domain": "金融",
    "title": "Do People Follow AI Advice? Evidence from a Pension Portfolio Choice Experiment",
    "url": "https://arxiv.org/abs/2608.11371",
    "source": "Hongseok Choi, Jeongbin Kim, Matthew Kovach, Kyu-Min Lee, Euncheol Shin, Hector Tzavellas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2608.11371v1 Announce Type: new Abstract: We study how differences in AI-generated financial recommendations are transmitted into individual portfolio choices. In an experiment with 400 employed"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.11626",
    "domain": "金融",
    "title": "Organizational Technology Ladders: Remote Work and Generative AI Adoption",
    "url": "https://arxiv.org/abs/2608.11626",
    "source": "Gregor Schubert",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2608.11626v1 Announce Type: new Abstract: This study proposes that firms move along an \"organizational technology ladder\": adopting one technology transforms hiring and work processes and builds"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12016",
    "domain": "金融",
    "title": "Term structure shapes in the Hull-White model with Svensson-parameterized initial yield curves",
    "url": "https://arxiv.org/abs/2608.12016",
    "source": "Felix Sachse",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2608.12016v1 Announce Type: new Abstract: We examine the shapes attainable by the forward and yield curve in the Hull-White model with Svensson-parameterized initial yield curves. For Nelson-Sie"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12236",
    "domain": "金融",
    "title": "How Organizations Use AI: Evidence from ChatGPT",
    "url": "https://arxiv.org/abs/2608.12236",
    "source": "Aaron Chatterji, David Holtz, Neel Rakholia, Prasanna Tambe, Gawesha Weeratunga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2608.12236v1 Announce Type: new Abstract: We study how organizations use frontier generative AI by linking ChatGPT Enterprise account records to usage, worker roles, task classifications, and pu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12251",
    "domain": "金融",
    "title": "Regime-Gated Residual Mixture-of-Experts for Cross-Sectional Volatility Forecasting",
    "url": "https://arxiv.org/abs/2608.12251",
    "source": "Junyi Ye, Gargi Vijay Borde",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2608.12251v1 Announce Type: new Abstract: Financial volatility is regime dependent, yet incorporating regime information into neural networks can also destabilize training. This paper asks where"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12283",
    "domain": "金融",
    "title": "Large Language Model-Driven Small-Capitalization Trading: Integrating Financial News Sentiment, Macroeconomic Indicators, and Technical Signals",
    "url": "https://arxiv.org/abs/2608.12283",
    "source": "Alireza Kargarzadeh, Nariman Khaledian, Navid Parvini, Arman Khaledian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2608.12283v1 Announce Type: new Abstract: Large language models can extract richer signals from financial news than fixed sentiment lexicons, and recent work has explored feeding such signals in"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.11266",
    "domain": "金融",
    "title": "Bank Run Exposure in a Paycheck-to-Paycheck Economy with Loss-Averse Depositors",
    "url": "https://arxiv.org/abs/2608.11266",
    "source": "G. Charles-Cadogan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2608.11266v1 Announce Type: cross Abstract: We develop a behavioural model of bank run exposure in a paycheck-to-paycheck economy with loss averse depositors. Income is received through demand d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.11344",
    "domain": "金融",
    "title": "Governing Agentic AI in FinTech",
    "url": "https://arxiv.org/abs/2608.11344",
    "source": "Henry Han",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2608.11344v1 Announce Type: cross Abstract: Financial institutions are delegating consequential decisions to agentic AI systems that decompose goals, coordinate models and tools, and act with li"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.11404",
    "domain": "金融",
    "title": "Technology interactions reshape the economics of China's coal power decarbonization",
    "url": "https://arxiv.org/abs/2608.11404",
    "source": "Yun-Long Zhang, Jia-Ning Kang, Xiaoming Kan, Lan-Cui Liu, Zhimin Huang, Song Peng, Biying Yu, Yi-Ming Wei",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2608.11404v1 Announce Type: cross Abstract: Decarbonizing existing coal-fired power plants can contribute to near-term climate mitigation, but identifying cost-effective retrofit strategies is c"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.11505",
    "domain": "金融",
    "title": "Does a Structural Model Add Anything to the Closing Price? Calibrated forecasting, incremental information, and match leverage in the Italian Serie A",
    "url": "https://arxiv.org/abs/2608.11505",
    "source": "Yannik Pitcan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2608.11505v1 Announce Type: cross Abstract: Studies of association-football forecasting routinely report three-way accuracy in the low fifties and present it as competitive with the betting mark"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12023",
    "domain": "金融",
    "title": "Sectoral inter-dependencies drive the loss of structural balance in signed financial networks",
    "url": "https://arxiv.org/abs/2608.12023",
    "source": "Kartik Dahake, Abhijit Chakraborty",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2608.12023v1 Announce Type: cross Abstract: Signed graphs provide an effective architecture for portraying a system in which cooperation and conflict coexist. Emerging from the concept of balanc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12143",
    "domain": "金融",
    "title": "Robustness over efficiency in climate coalitions: a bistable model and a map of architectures",
    "url": "https://arxiv.org/abs/2608.12143",
    "source": "Juergen Renn (Max Planck Institute of Geoanthropology, Jena, Germany)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2608.12143v1 Announce Type: cross Abstract: Designs for international climate cooperation face a trade-off between allocative efficiency and robustness to the erosion of institutions by defectio"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12259",
    "domain": "金融",
    "title": "Calibration Bets on the Past: Post-Training Quantization for Financial Time-Series Forecasting",
    "url": "https://arxiv.org/abs/2608.12259",
    "source": "Junyi Ye, Ivy Gateri Wanjiku",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2608.12259v1 Announce Type: cross Abstract: Financial forecasting models are typically developed in full precision, yet production deployment often requires low-precision inference to reduce mem"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12281",
    "domain": "金融",
    "title": "Oil price shocks reveal unequal capacities for mobility adaptation",
    "url": "https://arxiv.org/abs/2608.12281",
    "source": "Zihao Zhang, Yuanbo Zhang, Xiaolei Ma, Yuan Liao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2608.12281v1 Announce Type: cross Abstract: Urban decarbonization often raises the cost of travel, yet which neighbourhoods can adapt remains largely invisible under normal conditions. We levera"
  },
  {
    "id": "rss:https://arxiv.org/abs/2403.09045",
    "domain": "金融",
    "title": "Entangled vs. Separable Choice",
    "url": "https://arxiv.org/abs/2403.09045",
    "source": "Nail Kashaev, Martin Pl\\'avala, Victor H. Aguiar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2403.09045v4 Announce Type: replace Abstract: A judge observes the joint probabilistic choice rule of two decision makers: the frequency of action pairs across pairs of local covariates. The rul"
  },
  {
    "id": "rss:https://arxiv.org/abs/2411.04616",
    "domain": "金融",
    "title": "Optimal Execution under Incomplete Information",
    "url": "https://arxiv.org/abs/2411.04616",
    "source": "Etienne Chevalier, Yadh Hafsi, Vathana Ly Vath",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2411.04616v2 Announce Type: replace Abstract: We study optimal liquidation strategies under partial information for a single asset within a finite time horizon. We propose a model tailored for h"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.23300",
    "domain": "金融",
    "title": "Designing Agentic AI-Based Screening for Portfolio Investment",
    "url": "https://arxiv.org/abs/2603.23300",
    "source": "Mehmet Caner, Agostino Capponi, Nathan Sun, Jonathan Y. Tan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2603.23300v2 Announce Type: replace Abstract: We introduce a new agentic artificial intelligence (AI) platform for portfolio management. Our architecture consists of three layers. First, two lar"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04392",
    "domain": "金融",
    "title": "Adapted Law Invariance and Time-Consistent Dynamic Risk Measures",
    "url": "https://arxiv.org/abs/2607.04392",
    "source": "Mathias Beiglb\\\"ock, Silvana M. Pesenti, Maxime Sylvestre",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2607.04392v2 Announce Type: replace Abstract: In static risk measurement, law invariance expresses the principle that the risk of a position should depend only on its distribution, and not on th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.23162",
    "domain": "金融",
    "title": "SolarChain: A Physics-Grounded Embodied IoT System for Verifiable Urban Solar Market Design",
    "url": "https://arxiv.org/abs/2605.23162",
    "source": "Shilin Ou, Yifan Xu, Zhenshan Zhang, Luyao Zhang, Ming-Chun Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2605.23162v2 Announce Type: replace-cross Abstract: Distributed solar markets must coordinate physical reports, economic allocation, and public settlement even when IoT data can be manipulated. "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.20781",
    "domain": "金融",
    "title": "The Human-AI Substitution Principle: When will you be replaced by AI in your organization?",
    "url": "https://arxiv.org/abs/2607.20781",
    "source": "Bonny Banerjee, Shreya Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": "arXiv:2607.20781v2 Announce Type: replace-cross Abstract: Artificial Intelligence (AI) is rapidly transforming organizations, raising a fundamental organizational and economic question: when will a hu"
  },
  {
    "id": "hn:49197127",
    "domain": "金融",
    "title": "Former Federal Prosecutors to Senate: Stop Confirming Election Deniers as Judges",
    "url": "https://abovethelaw.com/2026/08/former-federal-prosecutors-to-senate-stop-confirming-election-deniers-to-the-federal-bench/",
    "source": "hn_acker",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-08-06T14:25:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49184251",
    "domain": "金融",
    "title": "Fed's Kashkari says 'now is the time to start slowly moving' rates up",
    "url": "https://www.cnbc.com/2026/08/05/feds-kashkari-says-now-is-the-time-to-start-slowly-moving-rates-up.html",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-08-05T15:24:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49097833",
    "domain": "金融",
    "title": "Show HN: The Federalist Papers, typeset as the 1787 newspapers they ran in",
    "url": "https://federalistreader.org/",
    "source": "vhwalke",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-07-29T14:13:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49215292",
    "domain": "金融",
    "title": "Mykhailo Fedorov reveals struggle to secure Patriot missiles and Western support",
    "url": "https://www.uawire.org/former-ukrainian-defense-minister-mykhailo-fedorov-reveals-struggles-to-secure-patriot-missiles-and-western-support",
    "source": "greedo",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-08-07T19:38:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:49182971",
    "domain": "金融",
    "title": "OpenAI settles claims of discrimination against US workers for $3.2M",
    "url": "https://finance.yahoo.com/technology/ai/articles/openai-settles-claims-discrimination-against-221429616.html",
    "source": "declan_roberts",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-08-05T13:57:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:49174369",
    "domain": "金融",
    "title": "Waymo CEO explains why Tesla’s camera-only self-driving falls short",
    "url": "https://electrek.co/2026/08/04/waymo-co-ceo-camera-only-self-driving-tesla/",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-08-04T20:11:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49173576",
    "domain": "金融",
    "title": "Investors in Situational Awareness deserved to lose their shirts",
    "url": "https://www.economist.com/finance-and-economics/2026/08/04/investors-in-situational-awareness-deserved-to-lose-their-shirts",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-08-04T19:18:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49189030",
    "domain": "金融",
    "title": "A Fed official is asking whether AI is becoming 'too big to fail'",
    "url": "https://thenextweb.com/news/a-fed-official-is-asking-whether-ai-is-becoming-too-big-to-fail",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-08-05T21:08:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49214813",
    "domain": "金融",
    "title": "US Sold Euros to Save the Yen, Europe Found Out After",
    "url": "https://finance.yahoo.com/markets/currencies/articles/us-sold-euros-save-yen-033819315.html",
    "source": "amarcheschi",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-07T18:54:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49190429",
    "domain": "金融",
    "title": "Data shows just how hard Tesla's Cybertruck has flopped",
    "url": "https://www.msn.com/en-us/autos/general/this-data-shows-just-how-hard-tesla-s-cybertruck-has-actually-flopped/ar-AA29sikQ",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-05T23:25:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49157782",
    "domain": "金融",
    "title": "US Schools Are Ditching Chromebooks for MacBooks by the Thousands",
    "url": "https://finance.yahoo.com/technology/articles/us-schools-ditching-chromebooks-macbooks-233015401.html",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-08-03T16:16:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:49082706",
    "domain": "金融",
    "title": "AI revenues are growing fast, but not fast enough",
    "url": "https://www.economist.com/finance-and-economics/2026/07/28/ai-revenues-are-growing-fast-but-not-fast-enough",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-07-28T12:19:54+00:00",
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
  }
]
```
