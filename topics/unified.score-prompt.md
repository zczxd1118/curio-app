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

- 今日日期：`2026-10-16`
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
  "date": "2026-10-16",
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
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 2101312,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1978628,
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
    "points": 1616503,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1402447,
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
    "points": 1350184,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 1199849,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 1123799,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 946546,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 900157,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 856030,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 717260,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 674751,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 592761,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 536395,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 424979,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 415566,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV1Nyp96pEGD",
    "domain": "AI",
    "title": "人人都要学！Agent 视觉创作全流程～【小白教程】",
    "url": "http://www.bilibili.com/video/av117427342017510",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 413381,
    "published_at": "2026-10-12T10:30:00+00:00",
    "summary": "做PPT、商品图、广告片！\n从活动策划到TVC成片，一期带你跑通创作型Agent全流程！\n感谢铁铁们的三连+关注～"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 355501,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 321694,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 307655,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1WWYE6LEzx",
    "domain": "AI",
    "title": "黑马程序员2026全网最夯VibeCoding零基础入门到实战项目开发全套视频教程，AI辅助编程从入门到实战，涵盖Claude Code、DeepSeek等内容",
    "url": "http://www.bilibili.com/video/av117251667724450",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 291055,
    "published_at": "2026-09-14T01:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260914\n2026黑马程序员AI智能应用开发学习路线图\nhttps://www.bilibili.com/opus/1156896913511940102\n如何下载资料\nhttps://www.bilibili.com/read/cv7881295/\n学习+球球群625260577，告别孤单，共同进步！\n\n【AI智能"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 278915,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 206698,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 183751,
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
    "points": 162690,
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
    "points": 159688,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 136023,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 103273,
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
    "points": 94058,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1jCaq6nESn",
    "domain": "AI",
    "title": "【Opus 5.5半价】零基础小白友好，15分钟彻底学习Claude桌面版",
    "url": "http://www.bilibili.com/video/av117346425374831",
    "source": "LeaderAI",
    "platform": "bilibili",
    "points": 92093,
    "published_at": "2026-09-28T03:03:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 76372,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 76256,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV15Vhy6cEhd",
    "domain": "AI",
    "title": "通俗易懂地讲解什么是Agent？",
    "url": "http://www.bilibili.com/video/av117330906449673",
    "source": "洪涛同学LovTech",
    "platform": "bilibili",
    "points": 70392,
    "published_at": "2026-09-25T09:12:59+00:00",
    "summary": "从0到1搭建一个简易Agent，从小白的角度出发解释Agent是如何运行的？"
  },
  {
    "id": "bvid:BV1e8dmBYEms",
    "domain": "AI",
    "title": "国内零门槛安装Claude Code(Win/Mac都支持｜新手友好｜建议收藏)",
    "url": "http://www.bilibili.com/video/av116441546230371",
    "source": "栗氪聊AI",
    "platform": "bilibili",
    "points": 69829,
    "published_at": "2026-04-21T07:38:25+00:00",
    "summary": "喜欢的朋友可以三连+关注支持一下，这对我帮助很大，感谢～"
  },
  {
    "id": "bvid:BV1713u6XE1D",
    "domain": "AI",
    "title": "Claude Code 完全接管了 Blender，然后创造了这个",
    "url": "http://www.bilibili.com/video/av116980883398142",
    "source": "stefan_3d_ai",
    "platform": "bilibili",
    "points": 68173,
    "published_at": "2026-07-26T11:00:00+00:00",
    "summary": "如果你给一个完全自主的 AI 代理提供对 Blender 的完整终端控制权限，并让它完完全全靠自己独立运行整整一个小时，到底会发生什么可怕的事情？\n\n在这个视频中，我远远超越了简单的代码复制粘贴，结合 Claude Code 和全新发布的官方 Blender MCP 服务器，深入探索了真正的 3D 工作流自动化究竟长什么样。\n\n---\n\n🔹 试用 Tripo AI 并免费获取 500 生成积分：h"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 64021,
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
    "points": 56050,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 49281,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47753,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1EfY76YEwp",
    "domain": "AI",
    "title": "14k Star Claude Code 开源桌面端，能自动操作电脑了！",
    "url": "http://www.bilibili.com/video/av117251936293145",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 47467,
    "published_at": "2026-09-11T10:30:01+00:00",
    "summary": "基于此前泄露的 Claude Code 源代码，我做了一个开源桌面端 cc-haha，并持续迭代。\n这次重构了 Computer Use 电脑操控功能：AI 能自己看屏幕、操作 APP，在 Mac 后台搭建小镇，也不占用我的鼠标键盘。\n本期从下载安装、模型配置到权限授权，带你一步步用起来。支持自选模型，不需要 Claude 账号。"
  },
  {
    "id": "bvid:BV1oQYL64EJV",
    "domain": "AI",
    "title": "【SRC漏洞挖掘】2026最适合新手的AI+自动化挖漏洞教程，从环境搭建到漏洞验证，手把手带你挖到第一个SRC漏洞！",
    "url": "http://www.bilibili.com/video/av117251248490748",
    "source": "阿盾聊安全",
    "platform": "bilibili",
    "points": 40543,
    "published_at": "2026-09-11T07:39:16+00:00",
    "summary": "这套 18 节教程带你从零跑通 AI 自动化挖漏洞全流程：环境搭建、Hermes部署、Burp/Nuclei 集成、资产侦察、漏洞发现到报告验证，一套打通。\n适合有 Web 安全基础、想从手动挖洞升级到自动化的同学。\n资料和工具包见评论区，三连不迷路。"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30961,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28999,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 24629,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1SmpD6QEuX",
    "domain": "AI",
    "title": "【Opus5.6】灰测性能前瞻 Claude Opus56 多则测试例「前端 工程」表现速览",
    "url": "http://www.bilibili.com/video/av117424707865238",
    "source": "小小小名不是小明",
    "platform": "bilibili",
    "points": 22386,
    "published_at": "2026-10-11T22:50:10+00:00",
    "summary": "**注意！！** 此视频中所有成果都来自于网页code模式"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 21829,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1E8Tk6MEkw",
    "domain": "AI",
    "title": "AI Agent教程全集丨从入门到进阶丨适合99%小白入行的Agent教程！360°讲解大模型合集（比例RAG +langchain+Agent)全程干货无废话",
    "url": "http://www.bilibili.com/video/av116848259498783",
    "source": "Agent教程",
    "platform": "bilibili",
    "points": 19293,
    "published_at": "2026-07-02T03:38:47+00:00",
    "summary": "陆陆续续也整理了不少资源，希望能帮大家少走一些弯路！无论是学业还是事业，都希望你顺顺利利  看在UP这么努力的份上，求个三连+关注嘛\n\n1️⃣ 大模型入门学习路线图（附学习资源）\n2️⃣ 大模型方向必读书籍PDF版\n3️⃣ 大模型面试题库\n4️⃣ 大模型项目源码\n5️⃣ 超详细海量大模型LLM实战项目\n6️⃣ Langchain/RAG/Agent学习资源\n7️⃣ LLM大模型系统0到1入门学习教"
  },
  {
    "id": "bvid:BV1mZ8F6tE8q",
    "domain": "AI",
    "title": "本地大模型保姆级教程｜安装、概念、接入Agent，你自己的AI",
    "url": "http://www.bilibili.com/video/av117126056643965",
    "source": "老陈爱刷机",
    "platform": "bilibili",
    "points": 18962,
    "published_at": "2026-08-20T04:58:51+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1JgVq6ME6v",
    "domain": "AI",
    "title": "超详细Claude Code+Harness教程",
    "url": "http://www.bilibili.com/video/av116679111610655",
    "source": "知了传课",
    "platform": "bilibili",
    "points": 14507,
    "published_at": "2026-06-02T06:33:18+00:00",
    "summary": "面向2026最新版超详细Claude Code+Harness教程，保姆级教程，高效AI编程技巧。资料领取请关注置顶评论。"
  },
  {
    "id": "bvid:BV1cyVv6TEG6",
    "domain": "AI",
    "title": "Claude Code CLI 小白极简入门 - 装了之后必会的命令与快捷键",
    "url": "http://www.bilibili.com/video/av116677635217424",
    "source": "五里墩茶社",
    "platform": "bilibili",
    "points": 13767,
    "published_at": "2026-06-02T00:20:19+00:00",
    "summary": "一个key用全球大模型🔴 https://DMXAPI.cn 🚀 国内直连OpenAI、Claude、Gemini,💰￥1元起充!\n\n加入我的知识星球:https://t.zsxq.com/W5Oj7\n\n本期视频面向已经装好 Claude Code、想真正用起来的新手。\n\n装了 Claude Code、却只会跟它对话？这一期按一次真实会话的顺序，把每天都会用到的命令和快捷键过一遍 - 怎么发现命令"
  },
  {
    "id": "hn:50008187",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI annualised revenues $20B less than previously signalled",
    "url": "https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 432,
    "published_at": "2026-10-08T16:45:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49844663",
    "domain": "AI 算力 / 半导体",
    "title": "ASML says it sold 'absolutely nothing' in Europe in 2026",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand",
    "source": "MC995",
    "platform": "hackernews",
    "points": 403,
    "published_at": "2026-09-25T13:49:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50035886",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia in talks to acquire US 'open' model startup Reflection AI",
    "url": "https://www.ft.com/content/052610c5-22b4-4dd4-932e-b7f9f0628b6a",
    "source": "arkj",
    "platform": "hackernews",
    "points": 179,
    "published_at": "2026-10-10T18:48:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50086363",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's first GPU: GeForce 256",
    "url": "https://dfarq.homeip.net/nvidias-first-gpu-geforce-256/",
    "source": "ibobev",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-10-14T12:05:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:50110301",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, Apple, Google, Microsoft, Amazon, Meta gave Trump $92M for his ballroom",
    "url": "https://www.theverge.com/policy/1012047/nvidia-apple-google-microsoft-amazon-meta-trump-ballroom",
    "source": "jacquesm",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-15T21:11:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:49933958",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon seeks to offload $8B of Nvidia chips to investors",
    "url": "https://www.reuters.com/business/retail-consumer/amazon-seeks-offload-8-billion-nvidia-chips-investors-ft-reports-2026-10-02/",
    "source": "wslh",
    "platform": "hackernews",
    "points": 82,
    "published_at": "2026-10-02T14:30:32+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/ai-moves-to-system-level-co-design-how-can-taiwan-capture-more-value/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Moves to System-Level Co-Design: How Can Taiwan Capture More Value",
    "url": "https://www.eetimes.com/ai-moves-to-system-level-co-design-how-can-taiwan-capture-more-value/",
    "source": "Susan Hong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T07:18:34+00:00",
    "summary": "During a panel session at iTechCon 2026, discussions explored how Taiwan can build on its strengths in semiconductors, advanced packaging, and system design to support AI development. The post AI Move"
  },
  {
    "id": "rss:https://www.eetimes.com/japan-offers-globalfoundries-21b-for-u-s-fab-expansion/",
    "domain": "AI 算力 / 半导体",
    "title": "Japan Offers GlobalFoundries $21B for U.S. Fab Expansion",
    "url": "https://www.eetimes.com/japan-offers-globalfoundries-21b-for-u-s-fab-expansion/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T19:00:00+00:00",
    "summary": "Japan’s $21B offer to GlobalFoundries would add two New York fabs and lift U.S. chip capacity 10%; see why analysts warn on state support. The post Japan Offers GlobalFoundries $21B for U.S. Fab Expan"
  },
  {
    "id": "rss:https://www.eetimes.com/data-orchestration-the-foundation-for-the-next-generation-semiconductor-enterprise/",
    "domain": "AI 算力 / 半导体",
    "title": "Data Orchestration: The Foundation for the Next-generation Semiconductor Enterprise",
    "url": "https://www.eetimes.com/data-orchestration-the-foundation-for-the-next-generation-semiconductor-enterprise/",
    "source": "Siemens Digital Industries",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T14:00:00+00:00",
    "summary": "Data orchestration gives semiconductor engineering teams a practical way to unify disconnected equipment, systems, and data without replacing existing infrastructure. By creating a connected execution"
  },
  {
    "id": "rss:https://www.eetimes.com/husb237-the-cost-effective-pd-sink-with-just-2-passives/",
    "domain": "AI 算力 / 半导体",
    "title": "HUSB237: The Cost-Effective PD Sink with Just 2 Passives",
    "url": "https://www.eetimes.com/husb237-the-cost-effective-pd-sink-with-just-2-passives/",
    "source": "Hynetek Semiconductor Co., Ltd.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T13:00:00+00:00",
    "summary": "Discover Hynetek’s HUSB237, a compact USB-PD sink controller enabling firmware-free USB-C upgrades up to 100W with only two external components. The post HUSB237: The Cost-Effective PD Sink with Just "
  },
  {
    "id": "rss:https://www.eetimes.com/small-volumes-big-impact-europes-hidden-role-in-advanced-chipmaking/",
    "domain": "AI 算力 / 半导体",
    "title": "Small Volumes, Big Impact: Europe’s Hidden Role in Advanced Chipmaking",
    "url": "https://www.eetimes.com/small-volumes-big-impact-europes-hidden-role-in-advanced-chipmaking/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T10:54:08+00:00",
    "summary": "A Fraunhofer–IMS Nanofabrication partnership illustrates how Europe's low-volume semiconductor manufacturing can support the world's most advanced chipmaking. The post Small Volumes, Big Impact: Europ"
  },
  {
    "id": "rss:https://www.eetimes.com/grid-modernization-hidden-cost-a-growing-attack-surface-few-are-watching/",
    "domain": "AI 算力 / 半导体",
    "title": "Grid Modernization’s Hidden Cost: A Growing Attack Surface Few Are Watching",
    "url": "https://www.eetimes.com/grid-modernization-hidden-cost-a-growing-attack-surface-few-are-watching/",
    "source": "David Montoya",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T08:00:00+00:00",
    "summary": "Grid modernization is expanding the energy sector’s cyberattack surface, while limited visibility across IT and OT networks leaves connected assets exposed. The post Grid Modernization’s Hidden Cost: "
  },
  {
    "id": "rss:https://www.eetimes.com/benchmark-electronics-thailand-operations-focus-on-high-mix-manufacturing/",
    "domain": "AI 算力 / 半导体",
    "title": "Benchmark Electronics’ Thailand Operations Focus on High-Mix Manufacturing",
    "url": "https://www.eetimes.com/benchmark-electronics-thailand-operations-focus-on-high-mix-manufacturing/",
    "source": "Stephen Las Marias",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T19:34:54+00:00",
    "summary": "Benchmark Electronics combines engineering expertise, workforce development, and flexible production to expand high-mix electronics manufacturing across Thailand. The post Benchmark Electronics’ Thail"
  },
  {
    "id": "rss:https://www.eetimes.com/beyond-lithography-3d-scaling-puts-new-demands-on-materials/",
    "domain": "AI 算力 / 半导体",
    "title": "Beyond Lithography: 3D Scaling Puts New Demands on Materials",
    "url": "https://www.eetimes.com/beyond-lithography-3d-scaling-puts-new-demands-on-materials/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T18:29:24+00:00",
    "summary": "ASM International shows how building increasingly complex 3D devices requires advances in materials and processes. The post Beyond Lithography: 3D Scaling Puts New Demands on Materials appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/co-packaged-optics-moves-from-promise-to-production-planning/",
    "domain": "AI 算力 / 半导体",
    "title": "Co-Packaged Optics Moves from Promise to Production Planning",
    "url": "https://www.eetimes.com/co-packaged-optics-moves-from-promise-to-production-planning/",
    "source": "Ayar Labs",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T15:41:12+00:00",
    "summary": "At Ayar Labs CPO Summit, Meta, Broadcom, AMD, and others weighed in on readiness for a 2028 co-packaged optics demand surge and the OCI MSA’s role. The post Co-Packaged Optics Moves from Promise to Pr"
  },
  {
    "id": "rss:https://www.eetimes.com/vicfuse-ul-standard-class-series-fuse-holders-quality-reliability-and-industrial-protection/",
    "domain": "AI 算力 / 半导体",
    "title": "VICFUSE UL Standard Class Series Fuse Holders: Quality, Reliability, and Industrial Protection",
    "url": "https://www.eetimes.com/vicfuse-ul-standard-class-series-fuse-holders-quality-reliability-and-industrial-protection/",
    "source": "ALI",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T13:00:00+00:00",
    "summary": "Explore VICFUSE's Class CF fuse line, which offers current-limiting technology and meets Class J performance standards in a compact design. The post VICFUSE UL Standard Class Series Fuse Holders: Qual"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/formlabs-form-studio-1-review",
    "domain": "AI 算力 / 半导体",
    "title": "Formlabs Form Studio 1 Review: Professional status, consumer price tag",
    "url": "https://www.tomshardware.com/3d-printing/formlabs-form-studio-1-review",
    "source": "Matt Farmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T18:00:00+00:00",
    "summary": "The Form Studio 1 is Formlabs first consumer-grade printer. It combines a 200 × 125 × 235 mm build volume with resin heating, automatic dispensing, and a free Open Material Mode."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/sk-hynix-reportedly-playing-hardball-with-trump-admin-over-3d-nand-fab-company-demands-increased-chipmaking-equipment-exports-to-china-in-exchange-for-us-fab",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix reportedly playing hardball with Trump admin over 3D NAND fab",
    "url": "https://www.tomshardware.com/pc-components/ssds/sk-hynix-reportedly-playing-hardball-with-trump-admin-over-3d-nand-fab-company-demands-increased-chipmaking-equipment-exports-to-china-in-exchange-for-us-fab",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T17:40:09+00:00",
    "summary": "SK hynix reportedly conditions building new Solidigm 3D NAND fab in the U.S. to equipment exports to the Solidigm fab in Dalian, China."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090-disappears-from-micro-center-amid-rumors-of-a-production-halt-retailer-flags-flagship-as-not-carried-as-stock-mysteriously-vanishes",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX 5090 disappears from Micro Center amid rumors of a production halt",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090-disappears-from-micro-center-amid-rumors-of-a-production-halt-retailer-flags-flagship-as-not-carried-as-stock-mysteriously-vanishes",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T15:37:41+00:00",
    "summary": "Micro Center has reclassified Nvidia GeForce RTX 5090 graphics cards as 'Not Carried,' and almost all units are out of stock at its stores."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/googlebooks-from-dell-lenovo-and-hp-tested-nice-hardware-but-the-os-isnt-ready-yet",
    "domain": "AI 算力 / 半导体",
    "title": "Googlebooks from Dell, Lenovo, and HP tested: Nice hardware, but the OS isn't ready yet",
    "url": "https://www.tomshardware.com/laptops/googlebooks-from-dell-lenovo-and-hp-tested-nice-hardware-but-the-os-isnt-ready-yet",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T15:00:00+00:00",
    "summary": "Googlebook OS needs a lot of love to feel like something other than Android on a PC."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/sipeed-reveals-chinese-made-dgx-spark-and-ryzen-ai-halo-rival-expected-to-cost-usd3-999-maixstation-pairs-axeras-ax8860p-with-128gb-of-lpddr5x-at-273-gb-s-with-promising-local-ai-performance-claims",
    "domain": "AI 算力 / 半导体",
    "title": "Sipeed reveals Chinese-made DGX Spark and Ryzen AI Halo rival, expected to cost $3,999",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/sipeed-reveals-chinese-made-dgx-spark-and-ryzen-ai-halo-rival-expected-to-cost-usd3-999-maixstation-pairs-axeras-ax8860p-with-128gb-of-lpddr5x-at-273-gb-s-with-promising-local-ai-performance-claims",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T14:30:00+00:00",
    "summary": "Sipeed’s MaixStation pairs Axera’s AX8860P with 128GB of LPDDR5X at 273 GB/s to take on Nvidia’s DGX Spark and AMD’s Ryzen AI Halo."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/the-internet-isnt-the-best-place-for-finding-pc-components-to-upgrade-your-computer-brick-and-mortar-stores-still-reign-supreme-thanks-to-bundled-deals",
    "domain": "AI 算力 / 半导体",
    "title": "The internet isn’t the best place to find upgrades for your computer — brick-and-mortar stores still reign supreme thanks to bundled deals",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/the-internet-isnt-the-best-place-for-finding-pc-components-to-upgrade-your-computer-brick-and-mortar-stores-still-reign-supreme-thanks-to-bundled-deals",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T14:00:00+00:00",
    "summary": "Component bundles are a great way of offsetting high prices on certain parts, but your proximity to a Micro Center may save you even more."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/eu-negotiates-sanction-swap-with-china-to-rescue-critical-asml-supplier-german-coatings-firm-faces-shutdown-without-chinese-rare-earths",
    "domain": "AI 算力 / 半导体",
    "title": "EU negotiates sanction swap with China to rescue critical ASML supplier",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/eu-negotiates-sanction-swap-with-china-to-rescue-critical-asml-supplier-german-coatings-firm-faces-shutdown-without-chinese-rare-earths",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T13:30:00+00:00",
    "summary": "The EU is reportedly negotiating with Beijing to remove Chinese restrictions on German ASML supplier Sindlhauser Materials, to prevent the China-dependent company from going out of business"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/alienware-aw3226q-32-inch-4k-oled-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Alienware AW3226Q 32-inch 4K OLED gaming monitor review: Sleek design with performance and value to match",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/alienware-aw3226q-32-inch-4k-oled-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T13:00:00+00:00",
    "summary": "Alienware rolls Tandem RGB Stripe OLED tech into a stylish 32-inch gaming monitor for a low price. The AW3226Q delivers 4K resolution, 165 Hz, Adaptive-Sync, HDR400 True Black, Dolby Vision, and wide-"
  },
  {
    "id": "rss:https://www.tomshardware.com/service-providers/network-providers/malicious-russian-disinformation-bot-traffic-barely-flinches-after-ukraine-strikes-yandex-data-centers-and-auto-migration-kicks-in-cloudflare-tracks-170-million-automated-attacks-shifting-to-alternate-cloud-hosts",
    "domain": "AI 算力 / 半导体",
    "title": "Malicious Russian disinformation bot traffic barely flinches after Ukraine strikes Yandex data centers and auto-migration kicks in",
    "url": "https://www.tomshardware.com/service-providers/network-providers/malicious-russian-disinformation-bot-traffic-barely-flinches-after-ukraine-strikes-yandex-data-centers-and-auto-migration-kicks-in-cloudflare-tracks-170-million-automated-attacks-shifting-to-alternate-cloud-hosts",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T12:28:24+00:00",
    "summary": "Ukraine's strikes on Russian data centers have caused legitimate bot traffic to go down, but malicious bots remain operational."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/we-test-the-rtx-spark-superchip-in-microsofts-surface-laptop-ultra-nvidias-windows-on-arm-platform-impresses-in-local-ai-but-gaming-isnt-its-strong-suit",
    "domain": "AI 算力 / 半导体",
    "title": "We tested the RTX Spark Superchip in Microsoft's Surface Laptop Ultra",
    "url": "https://www.tomshardware.com/laptops/we-test-the-rtx-spark-superchip-in-microsofts-surface-laptop-ultra-nvidias-windows-on-arm-platform-impresses-in-local-ai-but-gaming-isnt-its-strong-suit",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T12:00:21+00:00",
    "summary": "We've tested Nvidia's RTX Spark against the latest and greatest from Apple and AMD to see how Nvidia's efforts to transform the PC for the agentic AI era stack up."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/asml-reports-record-usd13-billion-quarter-vows-to-expand-capacity-as-demand-for-lithography-equipment-soars-customers-eager-to-secure-orders-in-2030-as-demand-is-expected-to-outstrip-2027-and-2028-supply",
    "domain": "AI 算力 / 半导体",
    "title": "ASML reports record $13 billion quarter, vows to expand capacity as demand for lithography equipment soars",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-reports-record-usd13-billion-quarter-vows-to-expand-capacity-as-demand-for-lithography-equipment-soars-customers-eager-to-secure-orders-in-2030-as-demand-is-expected-to-outstrip-2027-and-2028-supply",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T12:00:00+00:00",
    "summary": "ASML vows to expand production capacity amid growing demand, record earnings and profitability."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd249-on-32gb-of-ddr5-with-this-3-item-newegg-bundle-score-32gb-of-g-skill-trident-z5-neox-ram-a-ryzen-7-9800x3d-and-an-msi-x870e-motherboard-for-only-usd1-094-99",
    "domain": "AI 算力 / 半导体",
    "title": "Save $249 on 32GB of DDR5 with this 3-item Newegg bundle",
    "url": "https://www.tomshardware.com/pc-components/save-usd249-on-32gb-of-ddr5-with-this-3-item-newegg-bundle-score-32gb-of-g-skill-trident-z5-neox-ram-a-ryzen-7-9800x3d-and-an-msi-x870e-motherboard-for-only-usd1-094-99",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T11:56:24+00:00",
    "summary": "Score 32GB of G.Skill DDR5-6000 RAM for just $321 in Newegg’s new AM5 combo. For $1,094 ($249 off), you also get a Ryzen 7 9800X3D and an MSI X870E Tomahawk MAX WiFi board, plus a free AIO cooler."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/asml-struggling-to-keep-up-with-demand-for-chipmaking-equipment-as-ai-spending-continues-to-boom-chipmakers-are-already-looking-to-place-orders-for-2029-and-2030-output-ceo-says-demand-could-surpass-capacity-despite-massive-expansion-plans",
    "domain": "AI 算力 / 半导体",
    "title": "ASML struggling to keep up with demand for chipmaking equipment as AI spending continues to boom",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-struggling-to-keep-up-with-demand-for-chipmaking-equipment-as-ai-spending-continues-to-boom-chipmakers-are-already-looking-to-place-orders-for-2029-and-2030-output-ceo-says-demand-could-surpass-capacity-despite-massive-expansion-plans",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T11:30:00+00:00",
    "summary": "ASML says customers are already placing orders for advanced chipmaking tools years in advance, with AI-driven semiconductor demand remaining strong enough to strain capacity despite planned expansions"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tsmc-confirms-it-is-considering-terafab-chipmaking-expansion-with-elon-musk-ceo-insists-tsmc-would-have-to-run-texas-based-project",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC confirms it is considering Terafab chipmaking expansion with Elon Musk",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-confirms-it-is-considering-terafab-chipmaking-expansion-with-elon-musk-ceo-insists-tsmc-would-have-to-run-texas-based-project",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T11:15:39+00:00",
    "summary": "TSMC's management confirms that the company is looking forward to expand U.S. capacity beyond Arizona and Texas is one of its options. However, to become a part of the Terafab project, it insists on r"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/elon-musk-accuses-samsung-sk-hynix-of-unreasonable-memory-pricing",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk calls out memory makers over 'extortionate' chip pricing, says Micron is playing smart for long-term loyalty",
    "url": "https://www.tomshardware.com/pc-components/dram/elon-musk-accuses-samsung-sk-hynix-of-unreasonable-memory-pricing",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T11:00:00+00:00",
    "summary": "Elon Musk condemns memory makers citing unreasonable prices of memory, but claims Micron is different."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/russian-semiconductor-players-shows-off-bespoke-cpu-and-soc-designs-arm-and-elbrus-architectures-on-display",
    "domain": "AI 算力 / 半导体",
    "title": "Russian chipmakers demo homegrown RISC-V and Arm chips with retro games",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/russian-semiconductor-players-shows-off-bespoke-cpu-and-soc-designs-arm-and-elbrus-architectures-on-display",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T10:30:00+00:00",
    "summary": "Russian semiconductor players shows off bespoke CPU and SoC designs — Arm and Elbrus architectures on display"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/save-30-percent-on-this-asus-rog-gaming-laptop-with-rtx-5060-usd600-discount-makes-this-hefty-machine-just-usd1-399",
    "domain": "AI 算力 / 半导体",
    "title": "Save 30% on this ASUS ROG Gaming laptop with RTX 5060 — $600 discount makes this hefty machine just $1,399",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/save-30-percent-on-this-asus-rog-gaming-laptop-with-rtx-5060-usd600-discount-makes-this-hefty-machine-just-usd1-399",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T10:15:53+00:00",
    "summary": "Get an RTX 5060 gaming laptop for just $1,400."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-agent-deletes-tv-shows-entire-edit-weeks-before-release-backup-failure-means-production-team-needs-to-re-edit",
    "domain": "AI 算力 / 半导体",
    "title": "Unsupervised AI agent deletes TV show’s entire edit weeks before release; program can't air",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-agent-deletes-tv-shows-entire-edit-weeks-before-release-backup-failure-means-production-team-needs-to-re-edit",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T10:00:00+00:00",
    "summary": "The Challenge Sweden's season 2 edit was deleted by an AI agent put on the production server. The program director blames \"the human factor\" instead of AI."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/two-killed-one-seriously-hurt-in-explosion-at-intels-chip-plant-in-israel-police-suspect-a-gas-cylinder-malfunction-and-the-fire-involved-a-toxic-gas-used-to-clean-chipmaking-tools",
    "domain": "AI 算力 / 半导体",
    "title": "Two killed, one seriously hurt in explosion at Intel’s chip plant in Israel",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/two-killed-one-seriously-hurt-in-explosion-at-intels-chip-plant-in-israel-police-suspect-a-gas-cylinder-malfunction-and-the-fire-involved-a-toxic-gas-used-to-clean-chipmaking-tools",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T09:34:15+00:00",
    "summary": "Two workers have died in an explosion at Intel’s Kiryat Gat chip plant; police suspect a gas cylinder malfunction."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/grace-hopper-celebration-for-women-in-computing-canceled-two-weeks-out-anitab-org-says-registrations-and-sponsorships-fell-short-of-covering-costs",
    "domain": "AI 算力 / 半导体",
    "title": "Grace Hopper Celebration canceled two weeks out as AnitaB.org runs short of funds",
    "url": "https://www.tomshardware.com/tech-industry/grace-hopper-celebration-for-women-in-computing-canceled-two-weeks-out-anitab-org-says-registrations-and-sponsorships-fell-short-of-covering-costs",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T18:09:38+00:00",
    "summary": "AnitaB.org canceled this month’s Grace Hopper Celebration in Anaheim, saying registrations and sponsorships couldn’t cover its costs."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/gfiber-and-qualcomm-announce-wi-fi-8-gateway-20-gig-customers-to-be-first-to-receive-next-gen-wireless-upgrade",
    "domain": "AI 算力 / 半导体",
    "title": "GFiber and Qualcomm announce Wi-Fi 8 gateway",
    "url": "https://www.tomshardware.com/networking/routers/gfiber-and-qualcomm-announce-wi-fi-8-gateway-20-gig-customers-to-be-first-to-receive-next-gen-wireless-upgrade",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T16:28:03+00:00",
    "summary": "Wi-Fi 8 hasn't been certified by the IEEE yet, but hardware announcements are still ramping up"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/epic-games-vibe-codes-new-launcher-because-programming-is-hard-starts-46-percent-faster-than-steam-preview-is-available-now-but-not-recommended-for-competitive-players",
    "domain": "AI 算力 / 半导体",
    "title": "Epic Games vibe codes new launcher because 'programming is hard,' claims it starts 46% faster than Steam",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/epic-games-vibe-codes-new-launcher-because-programming-is-hard-starts-46-percent-faster-than-steam-preview-is-available-now-but-not-recommended-for-competitive-players",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T15:44:45+00:00",
    "summary": "Epic Games has introduced a redesigned launcher into preview, which the company says it vibe coded because \"programming is hard.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/fbi-shuts-down-over-40-north-korean-laptop-farms-used-by-fake-remote-workers-over-200-devices-seized-in-texas-although-no-arrests-were-made-so-far",
    "domain": "AI 算力 / 半导体",
    "title": "FBI shuts down over 40 North Korean laptop farms used by fake remote workers",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/fbi-shuts-down-over-40-north-korean-laptop-farms-used-by-fake-remote-workers-over-200-devices-seized-in-texas-although-no-arrests-were-made-so-far",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T14:41:34+00:00",
    "summary": "CrowdStrike has helped the FBI identify these sites, which Pyongyang uses to earn as much as $500 million annually to help fund its nuclear and other weapons programs."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/applications/the-official-toms-hardware-app-is-here-30-years-of-tech-coverage-and-benchmarks-in-your-pocket",
    "domain": "AI 算力 / 半导体",
    "title": "The official Tom’s Hardware app is here — 30 years of tech coverage and benchmarks in your pocket",
    "url": "https://www.tomshardware.com/software/applications/the-official-toms-hardware-app-is-here-30-years-of-tech-coverage-and-benchmarks-in-your-pocket",
    "source": "Paul Alcorn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T14:10:00+00:00",
    "summary": "Today we’re introducing the Tom's Hardware app, a faster, easier way to access all of our content while on the go."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/sk-hynix-to-place-custom-tiny-cpu-cores-in-its-ssd-controllers-to-ease-arm-load-as-drive-speeds-rocket-each-h-tpu-reportedly-draws-2-5-percent-of-a-cpu-cores-power",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix to place custom tiny CPU cores in its SSD controllers to ease Arm load as drive speeds rocket",
    "url": "https://www.tomshardware.com/pc-components/ssds/sk-hynix-to-place-custom-tiny-cpu-cores-in-its-ssd-controllers-to-ease-arm-load-as-drive-speeds-rocket-each-h-tpu-reportedly-draws-2-5-percent-of-a-cpu-cores-power",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T14:00:00+00:00",
    "summary": "SK hynix detailed H-TPU, tiny in-house cores that offload routine I/O from the Arm CPUs in its next enterprise SSD controllers."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/ps5-homebrew-storefront-with-over-1-600-free-ps5-and-ps4-games-taken-down-by-sony-company-plays-piracy-whack-a-mole-as-two-further-repos-spring-up",
    "domain": "AI 算力 / 半导体",
    "title": "PS5 homebrew storefront with over 1,600 free PS5 and PS4 games taken down by Sony",
    "url": "https://www.tomshardware.com/video-games/playstation/ps5-homebrew-storefront-with-over-1-600-free-ps5-and-ps4-games-taken-down-by-sony-company-plays-piracy-whack-a-mole-as-two-further-repos-spring-up",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T13:45:22+00:00",
    "summary": "Over 1,600 PS4 and PS5 games have been made free on jailbroken PS5 units thanks to Overdrive. The homebrew was quickly shut down after going viral, but was quickly revived through forks and re-release"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/spacex-limits-starlink-service-for-ukraines-high-speed-military-drones-without-prior-warning-ukrainian-officials-say-limitation-significantly-complicates-logistics-and-drone-operations",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceX limits Starlink service for Ukraine’s high-speed military drones without prior warning",
    "url": "https://www.tomshardware.com/tech-industry/drones/spacex-limits-starlink-service-for-ukraines-high-speed-military-drones-without-prior-warning-ukrainian-officials-say-limitation-significantly-complicates-logistics-and-drone-operations",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T13:04:33+00:00",
    "summary": "Ukrainian officials say SpaceX imposed new speed restrictions on military-grade Starlink terminals without warning, disrupting drone and logistics missions and forcing some operations to be canceled"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/analyzing-intels-emib-and-foveros-advanced-packaging-roadmaps-how-intel-plans-to-scale-chips-in-every-direction",
    "domain": "AI 算力 / 半导体",
    "title": "Analyzing Intel's EMIB and Foveros advanced packaging roadmaps",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/analyzing-intels-emib-and-foveros-advanced-packaging-roadmaps-how-intel-plans-to-scale-chips-in-every-direction",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T12:50:00+00:00",
    "summary": "Intel was the first large chipmaker to start using advanced packaging methods in 2017 – 2019. But where are Intel's EMIB and Foveros technologies today and where are they heading?"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/elon-musks-terafab-will-reportedly-receive-its-first-euv-tool-from-asml-in-mid-2027-cutting-edge-scanner-could-sit-idle-for-some-time-as-experimental-facility-is-completed",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk's Terafab will reportedly receive its first EUV tool from ASML in mid-2027",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/elon-musks-terafab-will-reportedly-receive-its-first-euv-tool-from-asml-in-mid-2027-cutting-edge-scanner-could-sit-idle-for-some-time-as-experimental-facility-is-completed",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T12:30:00+00:00",
    "summary": "Elon Musk may prefer FEL light sources for in-house chip production, but Terafab will start with proven tech from ASML."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/qualcomm-wins-architecture-breach-verdict-against-arm-but-gets-just-usd2-judge-could-still-suspend-royalty-fees-for-five-years",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm wins architecture breach verdict against Arm but gets just $2",
    "url": "https://www.tomshardware.com/pc-components/cpus/qualcomm-wins-architecture-breach-verdict-against-arm-but-gets-just-usd2-judge-could-still-suspend-royalty-fees-for-five-years",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T12:10:00+00:00",
    "summary": "A federal jury sides with Arm on select issues, rules in favor of Qualcomm in other cases. The legal battle set to continue."
  },
  {
    "id": "hn:50062098",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia accused of trying to cut a deal with Anna's Archive",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-accused-of-trying-to-cut-a-deal-with-annas-archive-for-high-speed-access-to-the-massive-pirated-book-haul-allegedly-chased-stolen-data-to-fuel-its-llms",
    "source": "amai",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-10-12T19:57:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50081435",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Reportedly Ending the RTX 5090, Reserves GB202 for Workstation GPUs",
    "url": "https://www.techpowerup.com/353578/nvidia-reportedly-ending-the-rtx-5090-reserves-gb202-silicon-for-workstation-gpus",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-10-14T01:52:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:50046896",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia-backed data centre firm Firmus scraps IPO as AI valuation concerns deepen",
    "url": "https://www.bbc.com/news/articles/ck9dzpw4ll8po",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-11T19:26:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:49937995",
    "domain": "AI 算力 / 半导体",
    "title": "CA tech executive arrested for allegedly smuggling $300M in Nvidia chips to CN",
    "url": "https://qz.com/greg-lui-earthmade-nvidia-ai-chips-smuggling-china-100226",
    "source": "littlexsparkee",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-10-02T20:07:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49913571",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/",
    "source": "bradleyg223",
    "platform": "hackernews",
    "points": 1705,
    "published_at": "2026-09-30T20:04:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50073879",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://deepmind.google/models/gemini/",
    "source": "737max",
    "platform": "hackernews",
    "points": 1457,
    "published_at": "2026-10-13T16:03:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49797982",
    "domain": "大厂 AI 动态",
    "title": "I said no and Apple said yes",
    "url": "https://dbushell.com/2026/09/22/apple-intelligence/",
    "source": "thatslast",
    "platform": "hackernews",
    "points": 886,
    "published_at": "2026-09-22T08:04:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49957116",
    "domain": "大厂 AI 动态",
    "title": "Turn off Apple Intelligence on macOS 27 and get its disk space back",
    "url": "https://github.com/omlahore/RemoveMacAI",
    "source": "privacyisntdead",
    "platform": "hackernews",
    "points": 775,
    "published_at": "2026-10-04T19:42:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49848269",
    "domain": "大厂 AI 动态",
    "title": "Ollaya – Ollama for open-source, Jev-style decision models",
    "url": "https://ollaya.dev/",
    "source": "Ardakilic",
    "platform": "hackernews",
    "points": 618,
    "published_at": "2026-09-25T18:33:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49790409",
    "domain": "大厂 AI 动态",
    "title": "Turn off and restrict access to Apple Intelligence features on Mac",
    "url": "https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac",
    "source": "alwillis",
    "platform": "hackernews",
    "points": 354,
    "published_at": "2026-09-21T17:30:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49817615",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 text-to-speech",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/",
    "source": "swolpers",
    "platform": "hackernews",
    "points": 331,
    "published_at": "2026-09-23T15:29:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50074869",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon for Robotics",
    "url": "https://developers.googleblog.com/gemini-4-argon-for-robotics/",
    "source": "xnx",
    "platform": "hackernews",
    "points": 232,
    "published_at": "2026-10-13T16:55:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49727659",
    "domain": "大厂 AI 动态",
    "title": "The DeepMind Institute",
    "url": "https://institute.deepmind.com/",
    "source": "vertigoruntime",
    "platform": "hackernews",
    "points": 186,
    "published_at": "2026-09-16T14:32:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:49844896",
    "domain": "大厂 AI 动态",
    "title": "Microsoft abandons personal AI chatbot race with Copilot reboot",
    "url": "https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 157,
    "published_at": "2026-09-25T14:07:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49829387",
    "domain": "大厂 AI 动态",
    "title": "Hackers influence ChatGPT and Gemini to direct users to scam centers",
    "url": "https://medium.com/@arielsimon/dark-sourcery-how-hackers-manipulate-ai-to-scam-you-88df434d2073",
    "source": "ArielSimon",
    "platform": "hackernews",
    "points": 143,
    "published_at": "2026-09-24T11:54:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49854945",
    "domain": "大厂 AI 动态",
    "title": "The Copilot+ PC brand is dead",
    "url": "https://www.windowscentral.com/microsoft/windows-11/the-copilot-pc-brand-is-dead-microsoft-and-pc-makers-quietly-pull-back-on-tarnished-windows-11-ai-pc-branding",
    "source": "bj-rn",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-09-26T09:55:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49914236",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon (High): Intelligence, Performance and Price Analysis",
    "url": "https://artificialanalysis.ai/models/gemini-4-argon",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 113,
    "published_at": "2026-09-30T20:50:28+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1012552/tesla-roadster-next-gen-reveal-elon-musk",
    "domain": "大厂 AI 动态",
    "title": "The Tesla Roadster flew, drove upside down, and hit 60mph in under a second",
    "url": "https://www.theverge.com/transportation/1012552/tesla-roadster-next-gen-reveal-elon-musk",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T01:28:27+00:00",
    "summary": "Elon Musk promised a flying car. And the Tesla Roadster did exactly that. Tesla demonstrated its next-generation Roadster at an event in Waco, Texas, where the electric supercar drove upside down, bri"
  },
  {
    "id": "rss:https://www.theverge.com/games/1012541/valve-steam-achievement-sets",
    "domain": "大厂 AI 动态",
    "title": "Steam can now show game achievements in separate ‘sets’",
    "url": "https://www.theverge.com/games/1012541/valve-steam-achievement-sets",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T23:18:28+00:00",
    "summary": "Valve is introducing a major new feature for Steam achievements called \"achievement sets\" that lets developers list different groups of achievements for a base game and DLCs. \"In games that support se"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1012510/openai-chatgpt-google-chrome-tabs",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT can peek at your Chrome tabs now",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1012510/openai-chatgpt-google-chrome-tabs",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T22:43:23+00:00",
    "summary": "OpenAI's ChatGPT Atlas browser is gone, but now ChatGPT's Google Chrome extension is getting some upgrades that allow it to use the browser tabs you already have open. With the extension installed, Op"
  },
  {
    "id": "rss:https://www.theverge.com/games/1012512/sega-total-war-shogun-2-remaster-pulled",
    "domain": "大厂 AI 动态",
    "title": "Sega pulls Total War: Shogun 2 remaster from sale following disastrous launch",
    "url": "https://www.theverge.com/games/1012512/sega-total-war-shogun-2-remaster-pulled",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T22:35:55+00:00",
    "summary": "Sega is removing Total War: Shogun 2 - Complete Edition from storefronts following a disastrous launch where users complained about issues like bugs and upscaling that appears to have been done by AI."
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1012438/hollywood-tech-backlash-you-can-see-everything-musk-the-social-reckoning-artificial",
    "domain": "大厂 AI 动态",
    "title": "The tech backlash is now in theaters",
    "url": "https://www.theverge.com/entertainment/1012438/hollywood-tech-backlash-you-can-see-everything-musk-the-social-reckoning-artificial",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T21:39:52+00:00",
    "summary": "Though movies about disruptive tech founders are nothing new, 2026 has been unusually stacked with features that take a much more critical look at how Silicon Valley is reshaping our reality. Aaron So"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1012445/donald-trump-ai-photo-white-house-rennovation-column",
    "domain": "大厂 AI 动态",
    "title": "Trump posts AI-edited photo to brag about White House restoration work",
    "url": "https://www.theverge.com/policy/1012445/donald-trump-ai-photo-white-house-rennovation-column",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T21:09:33+00:00",
    "summary": "President Donald Trump posted a series of photos on Truth Social showing off renovations to the White House - but one of them appears to be modified with AI. The picture, which compares an old White H"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1012374/bluesky-ai-attie-small-social-games-apps",
    "domain": "大厂 AI 动态",
    "title": "Bluesky&#8217;s AI tool now lets you make games and apps to share on social",
    "url": "https://www.theverge.com/tech/1012374/bluesky-ai-attie-small-social-games-apps",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T19:57:16+00:00",
    "summary": "Bluesky's Attie AI tool, which initially launched earlier this year as a way to use AI to build your own feeds, now lets you make \"small\" social apps like games, polls, and dashboards that you can the"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1012350/withings-plus-subscription-new-users-october-13-2026",
    "domain": "大厂 AI 动态",
    "title": "Withings now charges $100 per year to sync your data to other apps",
    "url": "https://www.theverge.com/tech/1012350/withings-plus-subscription-new-users-october-13-2026",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T19:52:13+00:00",
    "summary": "If you're a new user of Withings' fitness-tracking smartwatches or smart scales and want to sync and access your health data through third party apps like Apple Health or Google Health it's now going "
  },
  {
    "id": "rss:https://www.theverge.com/news/1012293/meta-apple-muse-spark-open-ai-model-mlx",
    "domain": "大厂 AI 动态",
    "title": "Meta and Apple team up to make Muse AI models run better on Macs",
    "url": "https://www.theverge.com/news/1012293/meta-apple-muse-spark-open-ai-model-mlx",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T18:15:36+00:00",
    "summary": "Meta announced the Muse Spark Open AI model today, claiming that it's the \"most capable US open-weight model to date.\" But the company also says that it's the \"the first model in its class\" that can \""
  },
  {
    "id": "rss:https://www.theverge.com/tech/1012200/sony-made-a-5900-gold-plated-walkman-mp3-player",
    "domain": "大厂 AI 动态",
    "title": "Sony made a $5,900 gold-plated Walkman MP3 player",
    "url": "https://www.theverge.com/tech/1012200/sony-made-a-5900-gold-plated-walkman-mp3-player",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T17:48:57+00:00",
    "summary": "Sony has announced a trio of new Walkman portable media players that start at an already absurd $1,899.99 for the NW-ZX900 and climb all the way up to $5,899 for the gold-plated NW-WM1ZM3. Sandwiched "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/even-benchmark-thinks-ai-is-eroding-the-venture-pact-against-backing-rivals/",
    "domain": "大厂 AI 动态",
    "title": "Even Benchmark thinks AI is eroding the venture pact against backing rivals",
    "url": "https://techcrunch.com/2026/10/15/even-benchmark-thinks-ai-is-eroding-the-venture-pact-against-backing-rivals/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T05:16:46+00:00",
    "summary": "Benchmark says the Valley’s rule against backing rivals is getting harder to keep."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/tesla-reveals-spacex-powered-roadster-that-flies-and-falls-with-style/",
    "domain": "大厂 AI 动态",
    "title": "Tesla reveals SpaceX-powered Roadster that flies and falls with style",
    "url": "https://techcrunch.com/2026/10/15/tesla-reveals-spacex-powered-roadster-that-flies-and-falls-with-style/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T01:17:43+00:00",
    "summary": "The new car used thrusters to leap over a Cybercab, Cybertruck, Tesla Semi, Model Y, and Model 3 at a demo in Texas."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/when-it-came-to-cal-ais-viral-success-a-small-army-of-influencers-paid-off/",
    "domain": "大厂 AI 动态",
    "title": "When it came to Cal AI’s viral success, a small army of influencers paid off",
    "url": "https://techcrunch.com/2026/10/15/when-it-came-to-cal-ais-viral-success-a-small-army-of-influencers-paid-off/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T23:44:56+00:00",
    "summary": "The company generated over $30 million in revenue in two years and was acquired by MyFitnessPal for an undisclosed amount of money in March."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/and-the-winner-of-startup-battlefield-at-disrupt-2026-is-intero-biosystems/",
    "domain": "大厂 AI 动态",
    "title": "And the winner of Startup Battlefield at Disrupt 2026 is: Intero Biosystems",
    "url": "https://techcrunch.com/2026/10/15/and-the-winner-of-startup-battlefield-at-disrupt-2026-is-intero-biosystems/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T23:33:45+00:00",
    "summary": "Intero Biosystems beat out 199 other Startup Battlefield companies to take home the $100,000 grand prize at TechCrunch Disrupt 2026."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/amazon-devices-chief-panos-panay-on-the-importance-of-failure-and-bouncing-back-from-it/",
    "domain": "大厂 AI 动态",
    "title": "Amazon devices chief Panos Panay on the importance of failure and bouncing back from it",
    "url": "https://techcrunch.com/2026/10/15/amazon-devices-chief-panos-panay-on-the-importance-of-failure-and-bouncing-back-from-it/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T20:38:13+00:00",
    "summary": "Panay said that it's possible to recover and learn from all sorts of failures, even catastrophic ones, when building products."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/meta-launches-an-open-weight-model-that-runs-on-macs/",
    "domain": "大厂 AI 动态",
    "title": "Meta launches an open-weight AI model that runs on Macs",
    "url": "https://techcrunch.com/2026/10/15/meta-launches-an-open-weight-model-that-runs-on-macs/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T20:04:53+00:00",
    "summary": "Meta and Apple have teamed up for the launch of the social media giant's newest model, Muse Spark Open, which will run locally on Apple silicon."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/amazon-devices-chief-panos-panay-sees-a-future-where-ai-devices-replace-the-need-to-use-apps/",
    "domain": "大厂 AI 动态",
    "title": "Amazon devices chief Panos Panay sees a future where AI devices replace the need to use apps",
    "url": "https://techcrunch.com/2026/10/15/amazon-devices-chief-panos-panay-sees-a-future-where-ai-devices-replace-the-need-to-use-apps/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T19:55:25+00:00",
    "summary": "Speaking at TechCrunch Disrupt, Amazon devices chief Panos Panay described a future where ambient AI devices work in the background, anticipating users' needs instead of waiting for commands."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/bluesky-wants-to-make-it-easier-to-buy-sell-and-fundraise-on-the-network/",
    "domain": "大厂 AI 动态",
    "title": "Bluesky wants to make it easier to buy, sell, and fundraise on the network",
    "url": "https://techcrunch.com/2026/10/15/bluesky-wants-to-make-it-easier-to-buy-sell-and-fundraise-on-the-network/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T19:29:05+00:00",
    "summary": "The executives argued that advertising isn’t the only path to monetization, and that there are alternative models that are feasible when it comes to monetization."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/anthropic-is-letting-metr-researchers-look-under-the-hood-with-employee-level-access/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic is letting METR researchers look under the hood with employee-level access",
    "url": "https://techcrunch.com/2026/10/15/anthropic-is-letting-metr-researchers-look-under-the-hood-with-employee-level-access/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T19:14:26+00:00",
    "summary": "METR will publish its own assessments of Anthropic’s risks, incidents, and practices, and the frontier AI model maker has given up the right to block them."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/bluesky-expands-its-ai-powered-attie-app-to-let-anyone-build-websites-games-and-more/",
    "domain": "大厂 AI 动态",
    "title": "Bluesky expands its AI-powered Attie app to let anyone build websites, games, and more",
    "url": "https://techcrunch.com/2026/10/15/bluesky-expands-its-ai-powered-attie-app-to-let-anyone-build-websites-games-and-more/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T18:56:46+00:00",
    "summary": "Bluesky is bringing “social vibe coding” to its experimental Attie platform, allowing users to create interactive experiences like games, quizzes, and websites that can tap into the social network's a"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/last-chance-to-save-up-to-200-on-techcrunch-founder-summit-early-booking-ends-oct-16/",
    "domain": "大厂 AI 动态",
    "title": "Last chance to save up to $200 on your TechCrunch Founder Summit pass: Early booking ends October 16",
    "url": "https://techcrunch.com/2026/10/15/last-chance-to-save-up-to-200-on-techcrunch-founder-summit-early-booking-ends-oct-16/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T18:00:00+00:00",
    "summary": "Savings of up to $200 end October 16 for TechCrunch Founder Summit. These savings for Founder and Investor Passes vanish after Friday. Join 1,000 founders and investors on November 4 at Boston’s SoWa "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/volvo-makes-a-bigger-bet-on-nvidia/",
    "domain": "大厂 AI 动态",
    "title": "Volvo makes a bigger bet on Nvidia for hands-free automated driving",
    "url": "https://techcrunch.com/2026/10/15/volvo-makes-a-bigger-bet-on-nvidia/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T17:34:40+00:00",
    "summary": "Volvo is leveling up its automated driving system through an expansion of its nearly decade-long partnership with Nvidia that will extend beyond its battery electric vehicles."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/sk-hynix-bargains-for-chip-equipment-exports-to-its-china-facility-in-return-for-building-a-factory-in-us/",
    "domain": "大厂 AI 动态",
    "title": "SK Hynix bargains for chip equipment exports to its China facility in return for building a factory in US",
    "url": "https://techcrunch.com/2026/10/15/sk-hynix-bargains-for-chip-equipment-exports-to-its-china-facility-in-return-for-building-a-factory-in-us/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T16:45:37+00:00",
    "summary": "SK Hynix’s Solidigm is reportedly seeking U.S. approval to send more chipmaking equipment to China as it weighs building a new NAND chip factory in America."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/ai-agents-are-coming-to-rivians-cars/",
    "domain": "大厂 AI 动态",
    "title": "AI agents are coming to Rivian’s cars",
    "url": "https://techcrunch.com/2026/10/15/ai-agents-are-coming-to-rivians-cars/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T15:02:36+00:00",
    "summary": "We'll likely learn more about how this will work at the company's upcoming \"AI &#038; Autonomy Day\" event in December."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/ramp-reaches-60b-valuation-as-it-pushes-deeper-into-ai/",
    "domain": "大厂 AI 动态",
    "title": "Ramp reaches $60B valuation as it pushes deeper into AI",
    "url": "https://techcrunch.com/2026/10/15/ramp-reaches-60b-valuation-as-it-pushes-deeper-into-ai/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T14:47:09+00:00",
    "summary": "The funding comes as Ramp's annualized revenue crosses $2B, and its customer count reaches 85,000."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/googles-universal-cart-shopping-tool-launches-in-the-us/",
    "domain": "大厂 AI 动态",
    "title": "Google’s Universal Cart shopping tool launches in the US",
    "url": "https://techcrunch.com/2026/10/15/googles-universal-cart-shopping-tool-launches-in-the-us/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T14:29:33+00:00",
    "summary": "The new shopping tool is available in the U.S. across Google Search and the Gemini app."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/techcrunch-disrupt-2026-last-day/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Disrupt 2026: Last day",
    "url": "https://techcrunch.com/2026/10/15/techcrunch-disrupt-2026-last-day/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T14:00:00+00:00",
    "summary": "Last day to be part of TechCrunch Disrupt 2026. Join 10,000+ tech leaders for a day of connections and insights. Save 75% on your pass now."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/amazons-bee-launches-two-new-personal-ai-devices-starting-at-75/",
    "domain": "大厂 AI 动态",
    "title": "Amazon’s Bee launches two new personal AI devices, starting at $75",
    "url": "https://techcrunch.com/2026/10/15/amazons-bee-launches-two-new-personal-ai-devices-starting-at-75/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T12:00:00+00:00",
    "summary": "Amazon-owned Bee has launched its first new AI devices since its acquisition, including an updated wearable and a credit-card-sized recorder that attaches to smartphones. The devices can summarize con"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/15/citizen-lab-says-governments-are-abusing-online-ads-to-hack-people-with-zero-click-spyware/",
    "domain": "大厂 AI 动态",
    "title": "Governments are hacking people with ‘zero-click’ spyware by showing them online ads",
    "url": "https://techcrunch.com/2026/10/15/citizen-lab-says-governments-are-abusing-online-ads-to-hack-people-with-zero-click-spyware/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T10:00:00+00:00",
    "summary": "The digital rights unit found evidence that dozens of devices at media organization Al Jazeera were hacked after being shown malicious online ads."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/14/figma-announces-new-features-to-define-how-agents-work-on-its-platform/",
    "domain": "大厂 AI 动态",
    "title": "Figma announces new features to define how agents work on its platform",
    "url": "https://techcrunch.com/2026/10/14/figma-announces-new-features-to-define-how-agents-work-on-its-platform/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T04:30:00+00:00",
    "summary": "Figma is also releasing its code layers feature in open beta."
  },
  {
    "id": "rss:https://stratechery.com/2026/a-conversation-with-ari-emanuel-about-entertainment-and-ai/",
    "domain": "大厂 AI 动态",
    "title": "A Conversation With Ari Emanuel About Entertainment and AI",
    "url": "https://stratechery.com/2026/a-conversation-with-ari-emanuel-about-entertainment-and-ai/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T10:00:00+00:00",
    "summary": "A conversation with Hollywood super-agent Ari Emanuel about his memoir, the impact of AI on Hollywood, and the power of a phone call."
  },
  {
    "id": "rss:https://stratechery.com/2026/apple-homeview-the-new-apple-tv-the-app-story/",
    "domain": "大厂 AI 动态",
    "title": "Apple HomeView, The New Apple TV, The App Story",
    "url": "https://stratechery.com/2026/apple-homeview-the-new-apple-tv-the-app-story/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-14T10:00:00+00:00",
    "summary": "The Apple Homeview is official, and the question is how big is the addressable market for expensive devices based on subpar AI."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/kde-turns-30-with-plasma-6-8-remote-upgrades-and-an-x11-farewell/",
    "domain": "大厂 AI 动态",
    "title": "KDE turns 30 with Plasma 6.8, remote upgrades, and an X11 farewell",
    "url": "https://arstechnica.com/gadgets/2026/10/kde-turns-30-with-plasma-6-8-remote-upgrades-and-an-x11-farewell/",
    "source": "Nick Indge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T22:21:06+00:00",
    "summary": "KDE celebrates 30 years with a new Plasma release, a farewell to X11, and a movie."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/plex-now-helps-sell-movie-theater-tickets/",
    "domain": "大厂 AI 动态",
    "title": "Plex now helps sell movie theater tickets",
    "url": "https://arstechnica.com/gadgets/2026/10/plex-now-helps-sell-movie-theater-tickets/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T21:22:15+00:00",
    "summary": "Discovery data from Plex users will help studios, advertisers."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/10/hegseths-dubious-low-t-screening-may-flag-up-to-25-percent-of-the-army/",
    "domain": "大厂 AI 动态",
    "title": "Hegseth’s dubious low-T screening may flag up to 25 percent of the Army",
    "url": "https://arstechnica.com/health/2026/10/hegseths-dubious-low-t-screening-may-flag-up-to-25-percent-of-the-army/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T21:09:57+00:00",
    "summary": "Medical experts explicitly recommend against blanket screenings."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/10/targeted-ads-delivered-0-click-exploits-to-install-mercenary-malware/",
    "domain": "大厂 AI 动态",
    "title": "Targeted ads delivered 0-click exploits to install mercenary malware",
    "url": "https://arstechnica.com/security/2026/10/targeted-ads-delivered-0-click-exploits-to-install-mercenary-malware/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T20:32:41+00:00",
    "summary": "The incident is likely 1st confirmation of mercenary spyware delivered by targeted ads."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/10/porsche-previews-its-future-with-mission-s-supercar-concept/",
    "domain": "大厂 AI 动态",
    "title": "Above the 911? Porsche previews a new mid-engined supercar.",
    "url": "https://arstechnica.com/cars/2026/10/porsche-previews-its-future-with-mission-s-supercar-concept/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T20:30:02+00:00",
    "summary": "Porsche’s turnaround plan for 2035 involves less volume but more expensive cars."
  },
  {
    "id": "hn:49826087",
    "domain": "股票",
    "title": "16GB iPod Nano 3G Upgrade",
    "url": "https://tuckerosman.com/projects/16gb-ipod-nano",
    "source": "Ivoah",
    "platform": "hackernews",
    "points": 167,
    "published_at": "2026-09-24T03:58:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49886005",
    "domain": "股票",
    "title": "Anthropic's IPO prospectus shows AI vision, surging costs",
    "url": "https://www.reuters.com/business/finance/anthropics-ipo-prospectus-shows-sweeping-ai-vision-surging-costs-2026-09-28/",
    "source": "6thbit",
    "platform": "hackernews",
    "points": 145,
    "published_at": "2026-09-28T23:40:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:50098423",
    "domain": "股票",
    "title": "Asia chip stocks fall, AI funding worries",
    "url": "https://www.cnbc.com/2026/10/15/sk-hynix-samsung-softbank-stocks-asia-tech-rout-ai-funding-worries.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-15T02:29:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:50086344",
    "domain": "股票",
    "title": "Humxn Commits $50M to Buy Skilled Trades Data for Robotics Training",
    "url": "https://markets.businessinsider.com/news/stocks/humxn-research-labs-wants-to-buy-50-million-worth-of-skilled-trades-farming-and-manufacturing-data-for-ai-robotics-training-1036622854",
    "source": "howdoweknowit",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-14T12:04:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:50029452",
    "domain": "股票",
    "title": "Data Center Darling Firmus's $30B IPO Dream Crushed in 48 Hours",
    "url": "https://www.bloomberg.com/news/articles/2026-10-09/data-center-darling-s-30-billion-ipo-dream-crushed-in-48-hours",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-10-10T04:04:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:50071744",
    "domain": "股票",
    "title": "Sprout Pi Mainboard – A modern, RP2350-powered motherboard for iPods",
    "url": "https://www.crowdsupply.com/certain-things/sprout-pi-mainboard",
    "source": "esskay",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-10-13T13:49:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:50082283",
    "domain": "股票",
    "title": "US Says Chinese Hackers Attacked DOJ, NASA, Federal Reserve, Senate",
    "url": "https://www.usatoday.com/story/news/politics/2026/08/26/chinese-hackers-cyberattack-us-government/91473585007/",
    "source": "gmays",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-10-14T04:09:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50019535",
    "domain": "股票",
    "title": "Meadows – a small language for stock-and-flow diagrams that run",
    "url": "https://lorezzed.github.io/meadows/",
    "source": "jjsalamon",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-09T12:29:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49791944",
    "domain": "股票",
    "title": "Wall Street is growing skeptical of the data center boom",
    "url": "https://www.nytimes.com/2026/09/21/business/ai-data-center-ipos.html",
    "source": "mikhael",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-09-21T19:14:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49914149",
    "domain": "股票",
    "title": "Anthropic's IPO Prospectus Is a Fucking Doozy",
    "url": "https://daringfireball.net/linked/2026/09/30/reuters-anthropic-ipo-prospectus",
    "source": "danaris",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-09-30T20:44:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:49997175",
    "domain": "股票",
    "title": "The world has nearly burned through its oil stockpile buffer",
    "url": "https://www.reuters.com/business/energy/world-has-nearly-burned-through-its-oil-stockpile-buffer-executives-say-2026-10-06/",
    "source": "geox",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-10-07T18:50:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:50029232",
    "domain": "股票",
    "title": "Data centre company's much-hyped Australian stock market listing imploded",
    "url": "https://www.theguardian.com/australia-news/2026/oct/09/firmus-australian-stock-market-listing-bust-finance",
    "source": "stubish",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-10-10T03:23:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:50008977",
    "domain": "股票",
    "title": "Frontier AI models outperform analysts on earnings prediction",
    "url": "https://samaya.ai/blog/frontier-ai-models-outperform-human-experts-on-earnings-prediction",
    "source": "ashwinpp",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-10-08T17:33:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50020096",
    "domain": "股票",
    "title": "Ask HN: What if no AIpocalypse, no AI bubble, what if it just keeps advancing?",
    "url": "https://news.ycombinator.com/item?id=50020096",
    "source": "consumer451",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-10-09T13:18:05+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/when-saturday-comes",
    "domain": "股票",
    "title": "When Saturday Comes",
    "url": "https://www.netinterest.co/p/when-saturday-comes",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T12:42:20+00:00",
    "summary": "Football as an Asset Class"
  },
  {
    "id": "hn:49796292",
    "domain": "股票",
    "title": "Smart Ring Maker Oura, Backers Seek $2.2B in US IPO",
    "url": "https://www.bloomberg.com/news/articles/2026-09-21/smart-ring-maker-oura-backers-seek-2-2-billion-in-us-ipo",
    "source": "elo2000",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-09-22T02:53:48+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-art-of-doing-financial-engineering",
    "domain": "股票",
    "title": "The Art of Doing Financial Engineering",
    "url": "https://www.netinterest.co/p/the-art-of-doing-financial-engineering",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T11:57:49+00:00",
    "summary": "AI Financing at the Frontier"
  },
  {
    "id": "hn:49810905",
    "domain": "股票",
    "title": "In 2025, 49 percent of adults under age 30 lived with a parent [pdf]",
    "url": "https://www.federalreserve.gov/publications/files/2025-report-economic-well-being-us-households-202605.pdf",
    "source": "gscott",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-09-23T02:26:49+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-agents-revolt",
    "domain": "股票",
    "title": "Agents Revolt",
    "url": "https://www.netinterest.co/p/the-agents-revolt",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:33:27+00:00",
    "summary": "What happens to finance when customers start paying attention"
  },
  {
    "id": "rss:https://www.netinterest.co/p/brookfield-of-dreams",
    "domain": "股票",
    "title": "Brookfield of Dreams",
    "url": "https://www.netinterest.co/p/brookfield-of-dreams",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T15:05:47+00:00",
    "summary": "Inside Brookfield&#8217;s Plan to Double Again"
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-five-deals-that-made-apollo",
    "domain": "股票",
    "title": "The Five Deals That Made Apollo",
    "url": "https://www.netinterest.co/p/the-five-deals-that-made-apollo",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T15:25:40+00:00",
    "summary": "From distressed debt to a trillion-dollar machine"
  },
  {
    "id": "rss:https://www.netinterest.co/p/hot-european-summer",
    "domain": "股票",
    "title": "Hot European Summer",
    "url": "https://www.netinterest.co/p/hot-european-summer",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T16:33:06+00:00",
    "summary": "Europe is outperforming &#8211; but Europeans aren&#8217;t participating"
  },
  {
    "id": "rss:https://www.netinterest.co/p/untangling-guggenheim",
    "domain": "股票",
    "title": "Untangling Guggenheim",
    "url": "https://www.netinterest.co/p/untangling-guggenheim",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T15:05:53+00:00",
    "summary": "How Private Credit Built Its Own Universe"
  },
  {
    "id": "rss:https://www.netinterest.co/p/great-scott",
    "domain": "股票",
    "title": "Great Scott",
    "url": "https://www.netinterest.co/p/great-scott",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T17:35:18+00:00",
    "summary": "Challenges Facing the Bond Trader in Chief"
  },
  {
    "id": "rss:https://www.netinterest.co/p/financing-the-ai-boom-3",
    "domain": "股票",
    "title": "Financing the AI Boom 3",
    "url": "https://www.netinterest.co/p/financing-the-ai-boom-3",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T16:46:59+00:00",
    "summary": "Nvidia, Guarantor of Last Resort"
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
    "id": "hn:49778029",
    "domain": "金融",
    "title": "Samsung is expected to more than double output of its HBM4 and HBM4E DRAM",
    "url": "https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 562,
    "published_at": "2026-09-20T17:38:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49948254",
    "domain": "金融",
    "title": "Federal judge calls Flock 'indiscriminate mass surveillance'",
    "url": "https://techcrunch.com/2026/10/03/federal-judge-calls-flock-indiscriminate-mass-surveillance/",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 503,
    "published_at": "2026-10-03T22:07:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50112657",
    "domain": "金融",
    "title": "Tesla Roadster",
    "url": "https://www.tesla.com/roadster",
    "source": "shekhar101",
    "platform": "hackernews",
    "points": 370,
    "published_at": "2026-10-16T01:32:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49824686",
    "domain": "金融",
    "title": "Feds Target AI Critics as \"Foreign Agents\"",
    "url": "https://www.kenklippenstein.com/p/feds-think-ai-critics-are-foreign",
    "source": "nmeagent",
    "platform": "hackernews",
    "points": 396,
    "published_at": "2026-09-24T00:41:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49875913",
    "domain": "金融",
    "title": "Parley: Federated, decentralised chat that speaks plain IRC",
    "url": "https://git.mills.io/prologic/parley",
    "source": "davidcollantes",
    "platform": "hackernews",
    "points": 330,
    "published_at": "2026-09-28T10:30:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49921118",
    "domain": "金融",
    "title": "Meta Uses A.I. Data Centers to Avoid Billions in Federal Taxes",
    "url": "https://www.nytimes.com/2026/09/30/technology/meta-ai-data-centers-taxes.html",
    "source": "gmays",
    "platform": "hackernews",
    "points": 259,
    "published_at": "2026-10-01T13:05:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:50059446",
    "domain": "金融",
    "title": "Feds got warrants to use fake cell towers to hunt down Don Lemon's producer",
    "url": "https://www.wired.com/story/feds-got-warrants-to-use-fake-cell-towers-to-hunt-down-don-lemons-producer/",
    "source": "rndsignals",
    "platform": "hackernews",
    "points": 196,
    "published_at": "2026-10-12T17:08:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49822556",
    "domain": "金融",
    "title": "OpenAI breaches Medicare, Albanese reveals",
    "url": "https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html",
    "source": "jonnonz",
    "platform": "hackernews",
    "points": 256,
    "published_at": "2026-09-23T21:01:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50090662",
    "domain": "金融",
    "title": "Tesla's Robotaxis Blow Through School Zones, NHTSA Petition Alleges",
    "url": "https://www.extremetech.com/cars/teslas-robotaxis-blow-through-school-zones-nhtsa-petition-alleges",
    "source": "speckx",
    "platform": "hackernews",
    "points": 145,
    "published_at": "2026-10-14T16:45:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:50057956",
    "domain": "金融",
    "title": "French supermarkets suffer fridge shutdown after 'unprecedented' cyberattack",
    "url": "https://uk.finance.yahoo.com/news/french-supermarket-chains-cyberattack-forced-115141288.html",
    "source": "thinkcontext",
    "platform": "hackernews",
    "points": 155,
    "published_at": "2026-10-12T15:36:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:50080275",
    "domain": "金融",
    "title": "Show HN: Pulse Local, a Mac budgeting app whose AI models run on your machine",
    "url": "https://pulseos.finance",
    "source": "niztk",
    "platform": "hackernews",
    "points": 119,
    "published_at": "2026-10-13T23:13:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50082021",
    "domain": "金融",
    "title": "Strafe: A new open-source, E2E Encrypted, and federated alternative to Discord",
    "url": "https://strafe.chat/",
    "source": "brydencalaway",
    "platform": "hackernews",
    "points": 117,
    "published_at": "2026-10-14T03:28:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:49731356",
    "domain": "金融",
    "title": "Fed hikes rates as inflation worries push up bond yields",
    "url": "https://www.reuters.com/live/live-fed-rate-hike-expected-inflation-worries-push-up-bond-yields-2026-09-16/",
    "source": "wslh",
    "platform": "hackernews",
    "points": 184,
    "published_at": "2026-09-16T18:55:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:50105900",
    "domain": "金融",
    "title": "Market selloff, rising rates test AI data centre deal boom",
    "url": "https://www.reuters.com/business/finance/market-selloff-rising-rates-test-ai-data-centre-deal-boom-2026-10-15/",
    "source": "tartoran",
    "platform": "hackernews",
    "points": 69,
    "published_at": "2026-10-15T16:17:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50114077",
    "domain": "金融",
    "title": "Tesla makes cars that fly? [video]",
    "url": "https://www.youtube.com/watch?v=7p5LxFdc-Qg",
    "source": "merinpapz10",
    "platform": "hackernews",
    "points": 68,
    "published_at": "2026-10-16T04:27:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49981063",
    "domain": "金融",
    "title": "Former German spy chief arrested for attempted treason",
    "url": "https://www.reuters.com/business/finance/former-german-spy-chief-detained-suspicion-espionage-treason-bild-reports-2026-10-06/",
    "source": "semiquaver",
    "platform": "hackernews",
    "points": 130,
    "published_at": "2026-10-06T16:51:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50049302",
    "domain": "金融",
    "title": "Governments are mishandling the affordability crisis",
    "url": "https://www.economist.com/finance-and-economics/2026/10/08/governments-are-mishandling-the-affordability-crisis",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 105,
    "published_at": "2026-10-11T23:40:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:49916668",
    "domain": "金融",
    "title": "10-year Treasury yield climbs above 5.3% to a level not seen in 24 years",
    "url": "https://www.wsj.com/finance/investing/surging-yields-bring-the-bond-market-back-to-the-turn-of-the-century-2b74773f",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 125,
    "published_at": "2026-10-01T01:40:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49832844",
    "domain": "金融",
    "title": "Federal judge orders Texas to air condition all prisons by the end of 2029",
    "url": "https://www.texastribune.org/2026/09/22/texas-prison-air-conditioning-lawsuit-ruling/",
    "source": "bonefishgrill",
    "platform": "hackernews",
    "points": 120,
    "published_at": "2026-09-24T16:15:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:50074739",
    "domain": "金融",
    "title": "Americans Trust in Federal Government Sinks to New Depths",
    "url": "https://news.gallup.com/poll/715361/trust-federal-government-sinks-new-depths.aspx",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-10-13T16:48:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:50062076",
    "domain": "金融",
    "title": "\"Today we're laying off a large part of the Airtable team \"",
    "url": "https://twitter.com/fedesimio/status/2109713695165329511",
    "source": "tortilla",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-10-12T19:56:16+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.21057",
    "domain": "金融",
    "title": "Loss-versus-rebalancing with external proportional transaction costs",
    "url": "https://arxiv.org/abs/2610.21057",
    "source": "Masaaki Fukasawa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.21057v1 Announce Type: new Abstract: We study liquidity provision in automated market makers when trading in the external market incurs proportional transaction costs. We consider both sepa"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.21145",
    "domain": "金融",
    "title": "Pricing American Commodity Options Under the Schwartz Two-Factor Model Using the Alternating Direction Explicit (ADE) Method",
    "url": "https://arxiv.org/abs/2610.21145",
    "source": "Sanjith Prabhu, Daniel J. Duffy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.21145v1 Announce Type: new Abstract: This project investigates the valuation of American commodity options using the Schwartz two-factor model. We employ the double-sweep Alternating Direct"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.21196",
    "domain": "金融",
    "title": "The end-of-month option in futures contracts and the Gittins index of holding the underlying",
    "url": "https://arxiv.org/abs/2610.21196",
    "source": "Erhan Bayraktar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.21196v1 Announce Type: new Abstract: The end-of-month option allows the short in a futures contract to choose when to deliver during a window in which the delivery price is fixed. We charac"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.21442",
    "domain": "金融",
    "title": "Fundamental Theorem of Discrete Asset Pricing",
    "url": "https://arxiv.org/abs/2610.21442",
    "source": "Masaaki Fukasawa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.21442v1 Announce Type: new Abstract: Motivated by discrete price quotes in continuous time, we seek a fundamental theorem based on no arbitrage rather than a condition on limiting trading o"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.21447",
    "domain": "金融",
    "title": "Long-Horizon Investment with Delayed Information in a Mean-Reverting Market",
    "url": "https://arxiv.org/abs/2610.21447",
    "source": "Yan Dolinsky",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.21447v1 Announce Type: new Abstract: We study long-term investment in an Ornstein-Uhlenbeck diffusion model with exponential utility. We solve the finite-horizon problem explicitly and show"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.21491",
    "domain": "金融",
    "title": "NEST: Stale-Robust Tokenized-Stock Measurement for a Crypto-Treasury LETF Stack",
    "url": "https://arxiv.org/abs/2610.21491",
    "source": "Doohwi Cha, Minsuk Sung, Minjae Lee, Hyeonjun Yeo, Hanhee Kim, Seunghan Son, Donghwa Seo, Juyeong Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.21491v1 Announce Type: new Abstract: Tokenized equities trade while listed markets are closed, so their marks could improve off-hours measurement along layered exposures that link Bitcoin, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.21510",
    "domain": "金融",
    "title": "How Much Screening Buys a Second? Speed, Selection, and the Maker's Spread",
    "url": "https://arxiv.org/abs/2610.21510",
    "source": "Aleksei Adadurov, Eduard Airapetian, Anton Chtepine, Antero Eloranta, Boris Pletenev, Andrei Sebyakin, Arsenii Valitov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.21510v1 Announce Type: new Abstract: We study the spread a liquidity provider needs to break even against counterparties that can exploit a stale quote, and we place two defenses on a singl"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.21540",
    "domain": "金融",
    "title": "Pricing the Unprovable: Ambiguity, Turnstile Runs, and the Verifiability Discount in Crypto Protocols",
    "url": "https://arxiv.org/abs/2610.21540",
    "source": "Doohwi Cha, Hanhee Kim, Hyeonjun Yeo, Minsuk Sung, Minjae Lee, Seunghan Son, Donghwa Seo, Juyeong Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.21540v1 Announce Type: new Abstract: Privacy-preserving protocols can repair a vulnerability without establishing whether it was exploited beforehand, even when no theft is reported and agg"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.21659",
    "domain": "金融",
    "title": "When Does \"Post-Call\" Begin? An Availability Contract for Earnings-Call NLP Benchmarks",
    "url": "https://arxiv.org/abs/2610.21659",
    "source": "Xiaoyu Ma, Kelvin J. L. Koa, Yuncong Liu, Ke-Wei Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.21659v1 Announce Type: new Abstract: Corporate financial disclosures often unfold over time, with announcements, prepared remarks, and discussion spanning multiple high-frequency return int"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.21841",
    "domain": "金融",
    "title": "Feeling the generalised rough SABR boundary",
    "url": "https://arxiv.org/abs/2610.21841",
    "source": "Masaaki Fukasawa, Antoine Jacquier, Mugad Oumgari",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.21841v1 Announce Type: new Abstract: We provide an in-depth analysis of a generalised rough version of the SABR volatility model, widely used in the financial industry. We specifically focu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.21846",
    "domain": "金融",
    "title": "Where Backtests and Live Trading Part Ways: Six Defects from One Intraday System",
    "url": "https://arxiv.org/abs/2610.21846",
    "source": "Alex Vidovich, Zivana Zerjal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.21846v1 Announce Type: new Abstract: Backtests of intraday strategies can drift away from what the live system actually does; in our case, the drift never showed in summary statistics. We r"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.21867",
    "domain": "金融",
    "title": "Algorithmic Collusion Without Deterrence: Auditing the Punishment Mechanism in Q-Learning Pricing Agents",
    "url": "https://arxiv.org/abs/2610.21867",
    "source": "Kaue Lopes de Moraes, Rodrigo De-Losso",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.21867v1 Announce Type: new Abstract: Independent tabular Q-learning agents repricing in a simulated Bertrand duopoly converge to supracompetitive prices, and the seminal evidence attributes"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.34004",
    "domain": "金融",
    "title": "RICE-Alpha: Reliability-Informed Correction with Event Graphs for LLM-Agent Stock Forecasting",
    "url": "https://arxiv.org/abs/2609.34004",
    "source": "Tong Liu, Lanmiao Liu, Xiang Hu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2609.34004v2 Announce Type: cross Abstract: Equity-relevant news evolves through temporally dependent corporate events, making historical information useful only when event continuity, informati"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.20920",
    "domain": "金融",
    "title": "$q_x$-Bass Martingales: Optimality, Existence and Convergence",
    "url": "https://arxiv.org/abs/2610.20920",
    "source": "Antonio Marini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.20920v1 Announce Type: cross Abstract: We introduce the class of $q_x$-Bass martingales, extending the notion of $q$-Bass martingales. These are martingale couplings with prescribed margina"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.21081",
    "domain": "金融",
    "title": "StochLOB: Heavy-Tailed Score Matching for Robust Limit Order Book Trend Prediction",
    "url": "https://arxiv.org/abs/2610.21081",
    "source": "Arshia Abolghasemi, Seyed Reza Tavakoli, Parsa Naderi, Nazanin Mirzaei, Behrad Jahani, Saba Yousefzadeh, Tahereh Javaheri, Mohammad Hosein Rohban, Gholamali Aminian, Ali Habibnia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.21081v1 Announce Type: cross Abstract: Score-based diffusion methods usually perturb data with Brownian Gaussian noise, corresponding to a light-tailed forward stochastic differential equat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.22043",
    "domain": "金融",
    "title": "Momentum, Commentary Tone, and Earnings Surprise in LLM Financial Forecasts",
    "url": "https://arxiv.org/abs/2610.22043",
    "source": "Alina Khaybullina",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.22043v1 Announce Type: cross Abstract: Which inputs drive a language model's financial forecast? We construct synthetic earnings announcements that independently reverse 20-day momentum, no"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.22144",
    "domain": "金融",
    "title": "Extending the Oracle Approximating Shrinkage to General Distributions",
    "url": "https://arxiv.org/abs/2610.22144",
    "source": "Michael J. Lewis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.22144v1 Announce Type: cross Abstract: The Oracle Approximating Shrinkage (OAS) estimator provides a closed-form, data-driven shrinkage intensity for regularizing sample covariance matrices"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.07863",
    "domain": "金融",
    "title": "Choice of Collateral Currency in Differential Swaps",
    "url": "https://arxiv.org/abs/2603.07863",
    "source": "Yining Ding, Ruyi Liu, Marek Rutkowski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2603.07863v2 Announce Type: replace Abstract: The role of collateral in derivative pricing has evolved beyond credit risk mitigation, particularly following the global financial crisis, when fun"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.31475",
    "domain": "金融",
    "title": "Real-time identification of the onset of financial rogue waves",
    "url": "https://arxiv.org/abs/2606.31475",
    "source": "Rosie Hayward, Orla Lennon, Fabio Biancalana",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2606.31475v4 Announce Type: replace Abstract: Extreme events in financial systems, often captured by indicators such as volatility, remain difficult to identify close to their onset. Volatility "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12587",
    "domain": "金融",
    "title": "DYSANOS Generative Dynamic Smooth Arbitrage-free Non-parametric Option Surfaces",
    "url": "https://arxiv.org/abs/2608.12587",
    "source": "Hans Buehler, Blanka Horvath, Anastasis Kratsios, Magnus Wiese",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2608.12587v4 Announce Type: replace Abstract: This article presents with DYSANOS the first generative market model for smooth SANOS option surfaces for all strikes and expiries which are free of"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.04087",
    "domain": "金融",
    "title": "Global Multi-Maturity SPX-VIX Calibration Beyond Markovian Stitching",
    "url": "https://arxiv.org/abs/2609.04087",
    "source": "Atithi Acharya, Charlie Che, Yue Sun, Brandon Augustino, Shouvanik Chakrabarti, Shree Hari Sureshbabu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2609.04087v2 Announce Type: replace Abstract: We develop a global martingale optimal transport framework for joint S&amp;P 500 (SPX)-VIX smile calibration across multiple maturities, without the"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.16151",
    "domain": "金融",
    "title": "Neural Estimation of Irreversibility in Real and Simulated Limit Order Book Paths",
    "url": "https://arxiv.org/abs/2610.16151",
    "source": "Hyeonjun Yeo, Doohwi Cha, Yoontae Hwang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.16151v2 Announce Type: replace Abstract: A path indistinguishable from its own reverse carries no arrow of time, so time irreversibility is a necessary condition for a directed mechanism to"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.20550",
    "domain": "金融",
    "title": "Principal component error in high-dimensional factor models",
    "url": "https://arxiv.org/abs/2609.20550",
    "source": "Alex Bernstein, Lisa R. Goldberg, Nicholas Gunther, Alec N. Kercheval, Tian Lan, Yian Lin, Dayi Yao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2609.20550v2 Announce Type: replace-cross Abstract: In a statistical factor model, principal components (or eigenvectors) of a sample covariance matrix serve as estimates of principal directions"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.31345",
    "domain": "金融",
    "title": "On the asymptotic shape of quantile surfaces",
    "url": "https://arxiv.org/abs/2609.31345",
    "source": "Florian Gach, Simon Hochgerner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2609.31345v3 Announce Type: replace-cross Abstract: This article is concerned with the asymptotic shape of quantile surfaces, defined as the set of quantiles at a given level $\\alpha$ generated "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.14959",
    "domain": "金融",
    "title": "AlphaRLM: Aligning Language Models for Literature-Grounded Symbolic Factor Discovery",
    "url": "https://arxiv.org/abs/2610.14959",
    "source": "Jie Huang, Yuecheng Hong, Yao Chen, Hao Zhong, Linfeng Xiao, Xudong Liu, Qiang Ye, Hao Xia, Jianxuan Xin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.14959v3 Announce Type: replace-cross Abstract: Formulaic alpha mining seeks to discover executable expressions that capture predictive market signals in a vast, noisy search space. Recent L"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.14969",
    "domain": "金融",
    "title": "Allocative Efficiency and the Returns to Innovation",
    "url": "https://arxiv.org/abs/2610.14969",
    "source": "Koki Okumura",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T04:00:00+00:00",
    "summary": "arXiv:2610.14969v2 Announce Type: replace-cross Abstract: Innovation changes welfare through the technology it adds and the reallocation it causes between producers with different markups. When produc"
  },
  {
    "id": "hn:50023065",
    "domain": "金融",
    "title": "Tesla Rebrands Full Self-Driving as Tesla Assisted Driving in Europe",
    "url": "https://qz.com/tesla-full-self-driving-rebranding-europe-assisted-driving-100926",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 53,
    "published_at": "2026-10-09T16:38:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:49916955",
    "domain": "金融",
    "title": "Cities Are Forced to Funnel License Plate Data to a Federal Surveillance Program",
    "url": "https://www.404media.co/how-cities-are-forced-to-funnel-license-plate-data-to-a-massive-federal-surveillance-program-hidta/",
    "source": "ripe",
    "platform": "hackernews",
    "points": 93,
    "published_at": "2026-10-01T02:26:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:49938815",
    "domain": "金融",
    "title": "Federal Judge Rules a Flock Search Was Unconstitutional",
    "url": "https://www.404media.co/federal-judge-rules-a-flock-search-was-indiscriminate-mass-surveillance-and-unconstitutional/",
    "source": "pavel_lishin",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-10-02T21:28:59+00:00",
    "summary": ""
  }
]
```
