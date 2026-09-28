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

- 今日日期：`2026-09-28`
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
  "date": "2026-09-28",
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
    "id": "bvid:BV1BVEs6LENZ",
    "domain": "AI",
    "title": "【2026最新Codex】Codex保姆级完整教程-Codex新手保姆级教程-最强AI助手！从入门到进阶，22分钟速通Codex！【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av116707129561197",
    "source": "编程大佬陈悠秀",
    "platform": "bilibili",
    "points": 3008580,
    "published_at": "2026-06-07T05:32:32+00:00",
    "summary": "最近Codex的能力越来越全面，变成了Codex四大形态里最强一个。 Codex APP 比起 Claude Code，额度更高，功能更全，免费账户也能用。而且不会出现限速、封号、降智等问题，用过的小伙伴直呼真香。本期视频带来一个Codex APP的完整教程"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 2010695,
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
    "points": 1912334,
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
    "points": 1596997,
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
    "points": 1341515,
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
    "points": 1289429,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 1100848,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 1011388,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 945769,
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
    "points": 892169,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1GsY76dEqW",
    "domain": "AI",
    "title": "一口气搞懂Agent到底怎么用！",
    "url": "http://www.bilibili.com/video/av117252103997988",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 815565,
    "published_at": "2026-09-11T11:30:00+00:00",
    "summary": "AI Agent这两年大家都听麻了，但真到上手，claude、codex这些又是注册、又是命令行，人还没踏进Agent大门，就先被劝退了。这期视频我用0门槛的国产Agent——字节旗下的TraeWork，用六个超真实的案例，手把手带你玩转Agent！完整的文字教程和GitHub神级Skill清单，打包放置顶评论了。教程制作不易，觉得有一点点帮助的话，记得一键三连～"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 815458,
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
    "points": 696072,
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
    "points": 674076,
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
    "points": 590638,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 443483,
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
    "points": 423837,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 401064,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 344699,
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
    "points": 299176,
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
    "points": 297939,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 285241,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 268835,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1X8oKBLEdj",
    "domain": "AI",
    "title": "一口气学会AI编程！3个月10万字超详细教学！【项目实操】【0基础教学】【自学教程】【AI编程】【vibecoding】",
    "url": "http://www.bilibili.com/video/av116436177523067",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 228349,
    "published_at": "2026-04-21T03:15:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料，领取方式：关注后 私信“ 1 ”就好！\n\n后面还会出【一口气学会AI漫剧 】【一口气学会AI Agent 】等系列！大家可以蹲蹲！"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 219449,
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
    "points": 189333,
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
    "points": 182243,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 157842,
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
    "points": 125087,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93829,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 75789,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 75392,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1c8NFzhEMi",
    "domain": "AI",
    "title": "一个CLI干掉所有MCP工具，省99%的token mcp2cli",
    "url": "http://www.bilibili.com/video/av116204349953548",
    "source": "探索未至之境",
    "platform": "bilibili",
    "points": 61814,
    "published_at": "2026-03-10T10:18:17+00:00",
    "summary": "深度解析GitHub热门项目mcp2cli——一个能把任何MCP服务器或OpenAPI规范变成命令行工具的Python项目。它用&quot;懒发现&quot;机制，把MCP协议的token浪费从数十万降到几千，节省高达99%。整个核心实现只有一个Python文件，却支持三种接入模式、OAuth认证和智能缓存。发布仅一天就获得372颗星，但社区也有激烈争议：CLI真的能取代MCP吗？准确率会不会受影"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 55529,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 55012,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1ApYD6KEkD",
    "domain": "AI",
    "title": "马斯克收购Cursor后，Cursor的性价比现在已经爆表",
    "url": "http://www.bilibili.com/video/av117254955993228",
    "source": "jopatk",
    "platform": "bilibili",
    "points": 49508,
    "published_at": "2026-09-11T23:19:58+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 48693,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28964,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1wqeb6gEDY",
    "domain": "AI",
    "title": "Claude Code 百分百不封号",
    "url": "http://www.bilibili.com/video/av117297150694473",
    "source": "DUNHKPcc",
    "platform": "bilibili",
    "points": 28004,
    "published_at": "2026-09-19T10:14:15+00:00",
    "summary": "如果需要文档，私信主播，主页送免费的token，文件在群里 Q群1124987353"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 23307,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1k73y6fEDx",
    "domain": "AI",
    "title": "【ClaudeCode】这绝对是b站讲的最好的Claude Code保姆级全套教程，2026最新版，包含所有干货！七天就能从小白到大神！学完即就业，玩转AI技术",
    "url": "http://www.bilibili.com/video/av117001821488596",
    "source": "爬虫逆向",
    "platform": "bilibili",
    "points": 20815,
    "published_at": "2026-07-29T07:25:00+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！"
  },
  {
    "id": "bvid:BV1XGaA6CEwe",
    "domain": "AI",
    "title": "【2026最新】Claude Code保姆级完整教程-最强AI助手！从入门到进阶，速通Claude Code！一个方法教你规避封号风险！【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av117325537810666",
    "source": "大模型小阳",
    "platform": "bilibili",
    "points": 18590,
    "published_at": "2026-09-24T10:36:14+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~"
  },
  {
    "id": "bvid:BV1E8Tk6MEkw",
    "domain": "AI",
    "title": "AI Agent教程全集丨从入门到进阶丨适合99%小白入行的Agent教程！360°讲解大模型合集（比例RAG +langchain+Agent)全程干货无废话",
    "url": "http://www.bilibili.com/video/av116848259498783",
    "source": "Agent教程",
    "platform": "bilibili",
    "points": 18246,
    "published_at": "2026-07-02T03:38:47+00:00",
    "summary": "陆陆续续也整理了不少资源，希望能帮大家少走一些弯路！无论是学业还是事业，都希望你顺顺利利  看在UP这么努力的份上，求个三连+关注嘛\n\n1️⃣ 大模型入门学习路线图（附学习资源）\n2️⃣ 大模型方向必读书籍PDF版\n3️⃣ 大模型面试题库\n4️⃣ 大模型项目源码\n5️⃣ 超详细海量大模型LLM实战项目\n6️⃣ Langchain/RAG/Agent学习资源\n7️⃣ LLM大模型系统0到1入门学习教"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 17907,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1MAYd6sEZh",
    "domain": "AI",
    "title": "效率翻倍， 一次讲透AI Agent的用法和技巧",
    "url": "http://www.bilibili.com/video/av117258059847877",
    "source": "数码旭",
    "platform": "bilibili",
    "points": 15646,
    "published_at": "2026-09-12T12:33:07+00:00",
    "summary": "AI Agent作为今年AI应用方式最大的变化，会给普通人带来突破性的效率提升，当然也给我带来的特别大的帮助。我希望通过这期长视频，能帮助你提升工作效率。"
  },
  {
    "id": "bvid:BV1dogD6aERB",
    "domain": "AI",
    "title": "2026年医学生必看的【AI+医学】最强教程来了（学习路线+完整教程）手把手教你医学方向如何结合AI搞定论文和项目！",
    "url": "http://www.bilibili.com/video/av116968686359676",
    "source": "迪哥AI大讲堂-",
    "platform": "bilibili",
    "points": 14899,
    "published_at": "2026-07-23T17:38:08+00:00",
    "summary": "迪哥给大家准备了医学人工智能学习资料包，可在评论区获取！\n包含：\n1、上百篇医学方向人工智能顶会论文+源码\n2、90+各种疾病医疗数据集\n3、人工智能医学领域经典实战项目\n4、医学生必备的学习路线图"
  },
  {
    "id": "bvid:BV1pfuR69EoF",
    "domain": "AI",
    "title": "【全80集】零基础Vibe Coding教程，Vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av117070675118277",
    "source": "暴龙Boy",
    "platform": "bilibili",
    "points": 14517,
    "published_at": "2026-08-10T10:45:04+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ZBT2ztEwp",
    "domain": "AI",
    "title": "一条视频讲清楚 到底什么是MCP！#MCP #Cursor #AI #编程",
    "url": "http://www.bilibili.com/video/av114642592469769",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 14278,
    "published_at": "2025-06-07T14:53:38+00:00",
    "summary": "一条视频讲清楚 到底什么是MCP！#MCP #Cursor #AI #编程"
  },
  {
    "id": "bvid:BV1Jnti6kE1C",
    "domain": "AI",
    "title": "【AI➕生信分析】目前B站最全最细的巧用Agent零代码完成一篇生信分析全套教程，一周从AI分析工作站的搭建到自动数据的获取，看完这一套生信分析教程就够了！",
    "url": "http://www.bilibili.com/video/av117211637222989",
    "source": "生信学不会1",
    "platform": "bilibili",
    "points": 13482,
    "published_at": "2026-09-04T07:43:34+00:00",
    "summary": "本套教程适合想学习生信分析的同学，生信分析+AI，巧用Agent零代码完成一篇生信分析，零基础教学\n如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！！！"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 12184,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "hn:49724881",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia announces native GPU programming in Rust",
    "url": "https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/",
    "source": "nonmaskable",
    "platform": "hackernews",
    "points": 970,
    "published_at": "2026-09-16T11:15:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:49872723",
    "domain": "AI 算力 / 半导体",
    "title": "Owed a billion dollars in Nvidia stock",
    "url": "https://colo.to/nvidia-stock-narrative.html",
    "source": "Eric_Gullichsen",
    "platform": "hackernews",
    "points": 669,
    "published_at": "2026-09-28T02:05:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49844663",
    "domain": "AI 算力 / 半导体",
    "title": "ASML says it sold 'absolutely nothing' in Europe in 2026",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand",
    "source": "MC995",
    "platform": "hackernews",
    "points": 395,
    "published_at": "2026-09-25T13:49:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:49824864",
    "domain": "AI 算力 / 半导体",
    "title": "Virtio-nvgpu: Near-native Nvidia GPU access inside a KVM guest",
    "url": "https://github.com/nestrilabs/virtio-nvgpu",
    "source": "WanjohiRyan",
    "platform": "hackernews",
    "points": 155,
    "published_at": "2026-09-24T01:02:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49714096",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC revealing details about next gen A14 node",
    "url": "https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331",
    "source": "osnium123",
    "platform": "hackernews",
    "points": 128,
    "published_at": "2026-09-15T15:31:55+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/xcena-cuts-data-movement-to-address-memory-bottlenecks/",
    "domain": "AI 算力 / 半导体",
    "title": "Xcena Cuts Data Movement to Address Memory Bottlenecks",
    "url": "https://www.eetimes.com/xcena-cuts-data-movement-to-address-memory-bottlenecks/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T07:30:00+00:00",
    "summary": "Xcena’s MX1 uses CXL to push compute into memory by combining DDR5, SSDs, and RISC-V cores while easing programmability. The post Xcena Cuts Data Movement to Address Memory Bottlenecks appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/full-stack-semiconductor-solutions-for-industry-and-digital-energy-applications/",
    "domain": "AI 算力 / 半导体",
    "title": "Full-Stack Semiconductor Solutions for Smart, Secure Industry and Digital Energy",
    "url": "https://www.eetimes.com/full-stack-semiconductor-solutions-for-industry-and-digital-energy-applications/",
    "source": "NSING Technologies Pte. Ltd",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T14:00:00+00:00",
    "summary": "NSING Technologies, a Singapore-founded semiconductor company, delivers full-stack chip solutions for industrial automation, AI data centers, and digital energy.The N32-series MCUs (144–600 MHz, Corte"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd300-on-this-1440p-ready-gaming-pc-with-an-rtx-5060-ti-16gb-now-usd1-399-99-newegg-deal-on-abs-cyclone-aqua-rig-nets-you-a-20-core-intel-cpu-along-with-16gb-of-ddr5-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save $300 on this 1440p-ready gaming PC with an RTX 5060 Ti 16GB, now $1,399.99",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd300-on-this-1440p-ready-gaming-pc-with-an-rtx-5060-ti-16gb-now-usd1-399-99-newegg-deal-on-abs-cyclone-aqua-rig-nets-you-a-20-core-intel-cpu-along-with-16gb-of-ddr5-and-a-1tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T09:15:46+00:00",
    "summary": "This ABS Cyclone Aqua gaming PC, featuring an RTX 5060 Ti 16GB, Intel Core i7-14700F, 16GB DDR5, and a 1TB SSD has a $300 discount, now $1,399.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/grab-this-14-inch-compact-gaming-laptop-powerhouse-for-usd1000-off-hp-omen-transcend-14-with-rtx-5070-and-3k-oled-display-drops-to-usd1-999-99-at-best-buy",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this 14-inch compact gaming laptop powerhouse for $1000 off",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/grab-this-14-inch-compact-gaming-laptop-powerhouse-for-usd1000-off-hp-omen-transcend-14-with-rtx-5070-and-3k-oled-display-drops-to-usd1-999-99-at-best-buy",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T15:21:30+00:00",
    "summary": "The gaming laptop pairs Intel’s Core Ultra 9 285H with Nvidia’s RTX 5070 Laptop GPU and a 3K 120Hz OLED display, giving buyers a powerful compact machine at a reduced price."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/custom-24-carat-gold-mini-pc-costs-around-usd1-7-million-weighs-nearly-29-pounds-for-up-to-50-percent-faster-heat-transfer-copper-would-have-been-far-cheaper-and-offers-even-better-thermal-conductivity",
    "domain": "AI 算力 / 半导体",
    "title": "Custom 24-carat gold mini PC costs around $1.7 million, weighs nearly 29 pounds for up to 50% faster heat transfer",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/custom-24-carat-gold-mini-pc-costs-around-usd1-7-million-weighs-nearly-29-pounds-for-up-to-50-percent-faster-heat-transfer-copper-would-have-been-far-cheaper-and-offers-even-better-thermal-conductivity",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T14:40:00+00:00",
    "summary": "A chrysophile has ordered a special edition mini PC with a pure 24-carat gold passive chassis which will cost around $1.7 million."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/thieves-steal-nvidia-labeled-trailers-expecting-massive-ai-gpu-payday-but-score-40-000-pounds-of-sand-instead-crooks-duped-by-20-tons-of-ballast-sand",
    "domain": "AI 算力 / 半导体",
    "title": "Thieves steal Nvidia-labeled trailers expecting massive AI GPU payday, but score 40,000 pounds of sand instead",
    "url": "https://www.tomshardware.com/pc-components/gpus/thieves-steal-nvidia-labeled-trailers-expecting-massive-ai-gpu-payday-but-score-40-000-pounds-of-sand-instead-crooks-duped-by-20-tons-of-ballast-sand",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T14:14:40+00:00",
    "summary": "The two PlusAI trailers with Nvidia-partner markings were apparently left outside the startup's warehouse, making it a juicy target for criminals looking to make easy money on AI GPUs. However, they w"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/gigabyte-1000gm-pg5-1000w-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "Gigabyte 1000GM PG5 1000W power supply review: Impressive Platinum-level efficiency with T-Guard thermal protection",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/gigabyte-1000gm-pg5-1000w-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T13:00:00+00:00",
    "summary": "Gigabyte's new Gaming series flagship, the Gigabyte 1000GM PG5 1000W, pairs an HEC-built platform with all-Japanese capacitors, Platinum-level efficiency, and T-Guard thermal protection for the 12V-2x"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/ps5-emulator-successfully-runs-six-titles-at-a-playable-60-fps-ps5-emulation-continues-to-gather-momentum-as-developers-improve-shader-translation-and-vulkan-support",
    "domain": "AI 算力 / 半导体",
    "title": "PS5 emulator successfully runs six titles at a playable 60 FPS",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/ps5-emulator-successfully-runs-six-titles-at-a-playable-60-fps-ps5-emulation-continues-to-gather-momentum-as-developers-improve-shader-translation-and-vulkan-support",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T12:40:00+00:00",
    "summary": "SharpEmu’s latest release can run six tested PS5 games at 60 FPS, with 12 of 55 titles now reaching gameplay state, as developers improve shader translation and Vulkan support."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/linux-enthusiasts-see-10-second-kernel-compilation-times-on-the-horizon-ai-assisted-patches-cut-build-times-by-nearly-a-third-without-a-ramdisk",
    "domain": "AI 算力 / 半导体",
    "title": "Linux enthusiasts see 10-second kernel compilation times on the horizon",
    "url": "https://www.tomshardware.com/software/linux/linux-enthusiasts-see-10-second-kernel-compilation-times-on-the-horizon-ai-assisted-patches-cut-build-times-by-nearly-a-third-without-a-ramdisk",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T12:20:00+00:00",
    "summary": "It won’t be long until Linux enthusiasts will be able to complete a clean kernel build in under 10 seconds thanks to advances in PC hardware and the AI-assisted optimization of compilers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/flock-seeks-to-have-security-researchers-map-of-flock-cameras-taken-down-unauthenticated-flaw-exposed-335-701-camera-locations-nationwide",
    "domain": "AI 算力 / 半导体",
    "title": "Flock seeks to have security researchers' map of Flock cameras taken down",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/flock-seeks-to-have-security-researchers-map-of-flock-cameras-taken-down-unauthenticated-flaw-exposed-335-701-camera-locations-nationwide",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T12:00:00+00:00",
    "summary": "A vulnerability on the Flock website allowed a security researcher to access its third-party provider to download the locations and descriptions of over 300,000 Flock cameras. He also pointed out how "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/developer-says-jev-decision-model-beat-pokemon-red-in-under-a-week-non-llm-engine-succeeds-where-traditional-chatbots-stalled-for-months-but-claude-opus-5-coached-the-model-through-its-dead-ends",
    "domain": "AI 算力 / 半导体",
    "title": "Developer says AI decision model Jev beat Pokémon Red in under a week",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/developer-says-jev-decision-model-beat-pokemon-red-in-under-a-week-non-llm-engine-succeeds-where-traditional-chatbots-stalled-for-months-but-claude-opus-5-coached-the-model-through-its-dead-ends",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T11:30:00+00:00",
    "summary": "TypeSafe AI's Jev beat Pokémon Red in under a week, eventually reaching the Hall of Fame."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/u-s-and-uk-navies-successfully-launch-3-700-pound-submarine-sinking-torpedo-from-robotic-drone-submarine-in-historic-first-project-broadsword-proves-weapon-interchangeability-in-just-seven-months",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. and UK navies successfully launch 3,700-pound submarine-sinking torpedo from robotic drone submarine in historic first",
    "url": "https://www.tomshardware.com/tech-industry/u-s-and-uk-navies-successfully-launch-3-700-pound-submarine-sinking-torpedo-from-robotic-drone-submarine-in-historic-first-project-broadsword-proves-weapon-interchangeability-in-just-seven-months",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T10:30:00+00:00",
    "summary": "The U.S. Navy and Royal Navy have successfully launched a 3,700-pound Mk 48 heavyweight torpedo from Britain’s uncrewed XV Excalibur submarine, marking the first time the weapon has been fired from an"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/counterfeit-vinyl-record-maker-sentenced-to-three-years-in-the-slammer-police-bust-largest-fake-vinyl-operation-in-uk-history-raid-uncovers-four-70-year-old-presses-and-3-000-metal-stampers",
    "domain": "AI 算力 / 半导体",
    "title": "Counterfeit vinyl record maker sentenced to three years in the slammer after making $3.5 million",
    "url": "https://www.tomshardware.com/tech-industry/counterfeit-vinyl-record-maker-sentenced-to-three-years-in-the-slammer-police-bust-largest-fake-vinyl-operation-in-uk-history-raid-uncovers-four-70-year-old-presses-and-3-000-metal-stampers",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T10:00:00+00:00",
    "summary": "Authorities seized thousands of counterfeit records and specialist manufacturing equipment after a BPI test purchase helped expose the long-running operation."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/taiwans-chip-talisman-snack-faces-production-halt-after-94-percent-strike-vote-workers-demand-share-of-usd176-million-factory-sale-to-ase",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan's chip talisman snack faces production halt after 94% strike vote",
    "url": "https://www.tomshardware.com/tech-industry/taiwans-chip-talisman-snack-faces-production-halt-after-94-percent-strike-vote-workers-demand-share-of-usd176-million-factory-sale-to-ase",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T09:30:00+00:00",
    "summary": "Taiwan's tech talisman snack production could be halted as the Guai Guai company faces strike action."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/27-year-old-gta-2-gets-full-path-tracing-and-60-fps-frame-generation-via-rtx-remix-custom-direct3d-9-wrapper-modernizes-classic-with-custom-direct3d-9-bridge-unlocks-dynamic-lighting",
    "domain": "AI 算力 / 半导体",
    "title": "27-year-old GTA 2 gets full path tracing and 60 FPS frame generation via RTX Remix",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/27-year-old-gta-2-gets-full-path-tracing-and-60-fps-frame-generation-via-rtx-remix-custom-direct3d-9-wrapper-modernizes-classic-with-custom-direct3d-9-bridge-unlocks-dynamic-lighting",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T15:10:00+00:00",
    "summary": "Modder releases GTA2 RTX Remix, a mod that adds path tracing and a dynamic time of day to the 27-year-old Grand Theft Auto 2."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/russia-bombs-ukrainian-data-centers-in-latest-escalation-100-000-households-lose-connectivity-as-firms-migrate-data-abroad-zelensky-says-ordinary-life-is-simply-a-target",
    "domain": "AI 算力 / 半导体",
    "title": "Russia bombs Ukrainian data centers in latest escalation",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/russia-bombs-ukrainian-data-centers-in-latest-escalation-100-000-households-lose-connectivity-as-firms-migrate-data-abroad-zelensky-says-ordinary-life-is-simply-a-target",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T14:30:59+00:00",
    "summary": "Russia has begun targeting data centers and internet infrastructure in its latest attacks, disrupting critical services for Ukrainian civilians. The attacks have left 100,000 households in the area wi"
  },
  {
    "id": "rss:https://www.tomshardware.com/tablets/microsoft-surface/microsoft-quietly-drops-copilot-branding-from-its-new-laptops-surface-cvp-confirms-new-devices-meet-hardware-requirements-but-lack-controversial-branding",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft quietly drops Copilot+ branding from new laptops",
    "url": "https://www.tomshardware.com/tablets/microsoft-surface/microsoft-quietly-drops-copilot-branding-from-its-new-laptops-surface-cvp-confirms-new-devices-meet-hardware-requirements-but-lack-controversial-branding",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T14:00:00+00:00",
    "summary": "Microsoft's latest Surface laptops dropped the Copilot+ PC branding despite hitting the minimum requirements. Even high-end AI devices like the Nvidia RTX Spark and Microsoft's own Project Zenith are "
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/open-source-anyps5-dumps-emulation-to-run-playstation-5-console-games-natively-on-pc-amd-zen-2-architecture-enables-proton-like-binary-translation-for-windows-and-linux",
    "domain": "AI 算力 / 半导体",
    "title": "Open-source AnyPS5 dumps emulation to run PlayStation 5 console games natively on PC",
    "url": "https://www.tomshardware.com/video-games/playstation/open-source-anyps5-dumps-emulation-to-run-playstation-5-console-games-natively-on-pc-amd-zen-2-architecture-enables-proton-like-binary-translation-for-windows-and-linux",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T13:59:04+00:00",
    "summary": "Traditional PS5 emulators attempt to recreate the console's hardware and software environment, but AnyPS5 is experimenting with a compatibility layer that translates PlayStation 5 executables into for"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/an-nvidia-chatbot-could-one-day-help-developers-better-optimize-their-games-patent-filing-show-requests-can-be-made-in-plain-english",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia patents AI chatbot to streamline PC game optimization",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/an-nvidia-chatbot-could-one-day-help-developers-better-optimize-their-games-patent-filing-show-requests-can-be-made-in-plain-english",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T13:00:00+00:00",
    "summary": "An Nvidia patent suggests the company could push developers to use a new chatbot as a way to get guidance on how to optimize their new games before release."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/sandisk-optimus-gx-pro-850p-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "Sandisk Optimus GX Pro 850P 2TB SSD review: A PS5 SSD you recognize at a price you don’t",
    "url": "https://www.tomshardware.com/pc-components/ssds/sandisk-optimus-gx-pro-850p-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T13:00:00+00:00",
    "summary": "The Sandisk Optimus GX Pro 850P is a WD Black SN850P by another name. It’s a great PS5 SSD with good performance in a mature package, but with a stiff premium."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidias-rtx-mega-geometry-2-0-streams-ray-tracing-geometry-into-vram-on-demand-nanite-inspired-design-drops-detail-instead-of-dropping-out",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia’s RTX Mega Geometry 2.0 streams ray-tracing geometry into VRAM on demand",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidias-rtx-mega-geometry-2-0-streams-ray-tracing-geometry-into-vram-on-demand-nanite-inspired-design-drops-detail-instead-of-dropping-out",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T12:30:00+00:00",
    "summary": "Nvidia’s RTX Mega Geometry 2.0 SDK arrives alongside RTX Kit 2026.3 with on-demand ray-tracing geometry streaming."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/novel-attack-on-rsa-cryptography-might-bring-computation-requirements-for-cracking-down-to-manageable-levels",
    "domain": "AI 算力 / 半导体",
    "title": "Novel attack slashes computing power needed to crack textbook RSA cryptography",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/novel-attack-on-rsa-cryptography-might-bring-computation-requirements-for-cracking-down-to-manageable-levels",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T12:00:00+00:00",
    "summary": "Not very practical yet, but could serve as the basis for future improvements."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/pny-allegedly-refuses-to-cover-melted-rtx-5090-powered-by-native-power-supply-cable-company-closes-users-ticket-when-questioned-on-policy",
    "domain": "AI 算力 / 半导体",
    "title": "PNY allegedly refuses to cover melted RTX 5090 powered by native power supply cable",
    "url": "https://www.tomshardware.com/pc-components/gpus/pny-allegedly-refuses-to-cover-melted-rtx-5090-powered-by-native-power-supply-cable-company-closes-users-ticket-when-questioned-on-policy",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T11:30:00+00:00",
    "summary": "A user's GeForce RTX 5090 died when his 12V-2x6 connector melted, and then PNY denied his warranty claim based on technicalities that aren't even present in the warranty policy."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/enthusiast-cooled-iphone-18-pro-with-cold-can-of-la-croix-sparkling-water-benchmarks-show-25-percent-higher-sustained-performance-liquid-cooling-surprisingly-reduced-thermal-throttling",
    "domain": "AI 算力 / 半导体",
    "title": "Enthusiast cooled iPhone 18 Pro with cold can of La Croix sparkling water; benchmarks show 25% higher sustained performance",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/enthusiast-cooled-iphone-18-pro-with-cold-can-of-la-croix-sparkling-water-benchmarks-show-25-percent-higher-sustained-performance-liquid-cooling-surprisingly-reduced-thermal-throttling",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T11:00:00+00:00",
    "summary": "Matt Birchler put a cold drink can on the back of an iPhone 18 Pro to see how much performance uplift it would get in a prolonged benchmarking session. The results showed up to 25% higher sustained pe"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/vpn/federal-bill-would-force-vpn-providers-isps-and-dns-services-to-block-foreign-piracy-sites-yet-fuzzy-location-rules-could-trigger-heavy-handed-bans",
    "domain": "AI 算力 / 半导体",
    "title": "Federal bill would force VPN providers, ISPs, and DNS services to block foreign piracy sites",
    "url": "https://www.tomshardware.com/software/vpn/federal-bill-would-force-vpn-providers-isps-and-dns-services-to-block-foreign-piracy-sites-yet-fuzzy-location-rules-could-trigger-heavy-handed-bans",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T10:30:00+00:00",
    "summary": "Proposed federal bill would force ISPs, DNS services, and VPN providers to block foreign piracy sites — yet the definition of \"from the United states\" gets murky"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/chatgpt-6-astra-cracks-1941-enigma-coded-message-in-two-days-autonomous-ai-coded-its-own-simulator-to-crack-code-that-was-unsolved-since-it-was-shared-online-back-in-2005",
    "domain": "AI 算力 / 半导体",
    "title": "ChatGPT-6 Astra cracks 85-year-old 1941 Enigma-coded message in two days",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/chatgpt-6-astra-cracks-1941-enigma-coded-message-in-two-days-autonomous-ai-coded-its-own-simulator-to-crack-code-that-was-unsolved-since-it-was-shared-online-back-in-2005",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T10:00:00+00:00",
    "summary": "A German Army Enigma transmission from 85 years ago, known as the MVUEH message, has been cracked by GTP-Astra in just two days."
  },
  {
    "id": "rss:https://www.eetimes.com/huaweis-tau-law-takes-commercial-form/",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei’s Tau Law Takes Commercial Form",
    "url": "https://www.eetimes.com/huaweis-tau-law-takes-commercial-form/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T14:18:57+00:00",
    "summary": "Kirin 9050 Pro rests on the Tau (τ) Scaling Law, marking a major change in chip architecture designed to bypass EUV lithography limits. The post Huawei’s Tau Law Takes Commercial Form appeared first o"
  },
  {
    "id": "rss:https://www.eetimes.com/balancing-bandwidth-range-and-power-in-intelligent-buildings/",
    "domain": "AI 算力 / 半导体",
    "title": "Balancing Bandwidth, Range, and Power in Intelligent Buildings",
    "url": "https://www.eetimes.com/balancing-bandwidth-range-and-power-in-intelligent-buildings/",
    "source": "Andy McFarlane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T08:00:34+00:00",
    "summary": "As edge AI transforms smart buildings, Wi-Fi HaLow bridges the gap between bandwidth, long range, and low power. The post Balancing Bandwidth, Range, and Power in Intelligent Buildings appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/delos-data-targets-heterogeneous-ai-with-data-interface/",
    "domain": "AI 算力 / 半导体",
    "title": "Delos Data Targets Heterogeneous AI with Data Interface",
    "url": "https://www.eetimes.com/delos-data-targets-heterogeneous-ai-with-data-interface/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T18:43:38+00:00",
    "summary": "Delos’s Apollo chiplet is designed to bridge different endpoint semantics and interconnects, creating a low-latency domain spanning GPUs, accelerators, CPUs and memory The post Delos Data Targets Hete"
  },
  {
    "id": "rss:https://www.eetimes.com/inside-tsmcs-evolving-design-ecosystem-shaping-the-future-of-ai-with-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside TSMC’s Evolving Design Ecosystem: Shaping the Future of AI, with AI",
    "url": "https://www.eetimes.com/inside-tsmcs-evolving-design-ecosystem-shaping-the-future-of-ai-with-ai/",
    "source": "Aveek Sarkar, Director, Ecosystem and Alliance Management Division, TSMC",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T14:10:55+00:00",
    "summary": "TSMC shares updates about the Open Innovation Platform Ecosystem and vision for enabling AI-driven agentic workflows using TSMC AI Design Kit The post Inside TSMC’s Evolving Design Ecosystem: Shaping "
  },
  {
    "id": "rss:https://www.eetimes.com/after-ionq-buyout-skywater-reiterates-role-as-quantum-foundry/",
    "domain": "AI 算力 / 半导体",
    "title": "After IonQ Buyout, SkyWater Reiterates Role as Quantum Foundry",
    "url": "https://www.eetimes.com/after-ionq-buyout-skywater-reiterates-role-as-quantum-foundry/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T14:08:18+00:00",
    "summary": "As SkyWater scales its 200-mm and 300-mm manufacturing platforms to support diverse quantum modalities, leadership emphasizes that protecting customer IP remains its top priority. The post After IonQ "
  },
  {
    "id": "rss:https://www.eetimes.com/tis-october-price-hike-how-to-secure-adi-ti-stock-without-the-panic/",
    "domain": "AI 算力 / 半导体",
    "title": "TI’s October Price Hike: How to Secure ADI/TI Stock Without the Panic",
    "url": "https://www.eetimes.com/tis-october-price-hike-how-to-secure-adi-ti-stock-without-the-panic/",
    "source": "Skyeast International Group Limited",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T10:23:24+00:00",
    "summary": "acing TI's October price hike? SKYEAST offers $30M+ ADI/TI spot stock, 2-hour quotes, and 7×24 support across time zones. Lock in supply now. The post TI&#8217;s October Price Hike: How to Secure ADI/"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/elon-musks-spacexai-to-add-another-660-000-ai-gpus-this-year-nearing-a-total-of-1-44-million-in-operation-firm-is-building-1-2-gigawatt-power-plant-to-bring-systems-fully-online",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk's SpaceXAI to add another 660,000 AI GPUs this year, nearing a total of 1.44 million in operation",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/elon-musks-spacexai-to-add-another-660-000-ai-gpus-this-year-nearing-a-total-of-1-44-million-in-operation-firm-is-building-1-2-gigawatt-power-plant-to-bring-systems-fully-online",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T15:40:00+00:00",
    "summary": "Elon Musk says that the Colossus 2 will receive 220,000 GB300 GPUs by next week, with another two tranches of the same amount expected to arrive later this year. This will put the site at over a milli"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/photonics/tower-semiconductor-to-invest-usd4-billion-in-japanese-ops-to-set-up-massive-optical-connectivity-hub-dual-track-expansion-aims-to-increase-output-by-40-times-by-2029",
    "domain": "AI 算力 / 半导体",
    "title": "Tower Semiconductor to invest $4 billion in Japanese ops to set up massive optical connectivity hub",
    "url": "https://www.tomshardware.com/tech-industry/photonics/tower-semiconductor-to-invest-usd4-billion-in-japanese-ops-to-set-up-massive-optical-connectivity-hub-dual-track-expansion-aims-to-increase-output-by-40-times-by-2029",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T15:00:22+00:00",
    "summary": "Tower's new optical connectivity hub in Japan will increase its output by 40 times in 2029 compared to 2025 level."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/meta-muse-runs-agents-on-amd-epyc-turin-hosts-with-two-cores-and-8gb-of-memory-ai-agent-can-pass-terminal-commands-to-ubuntu-host-system",
    "domain": "AI 算力 / 半导体",
    "title": "Meta Muse runs agents on AMD EPYC Turin hosts with two cores and 8GB of memory",
    "url": "https://www.tomshardware.com/pc-components/cpus/meta-muse-runs-agents-on-amd-epyc-turin-hosts-with-two-cores-and-8gb-of-memory-ai-agent-can-pass-terminal-commands-to-ubuntu-host-system",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T14:56:36+00:00",
    "summary": "Meta's new Muse AI agent is powered by AMD EPYC Turin hosts, with each user getting a private sandbox with two vCPUs and 8GB of memory."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/air-cooling/noctua-explores-2-000w-micro-channel-air-cooling-partners-with-forced-physics-to-develop-vacuum-pump-level-airflow-for-desktop-pcs",
    "domain": "AI 算力 / 半导体",
    "title": "Noctua explores 2,000W micro-channel air cooling",
    "url": "https://www.tomshardware.com/pc-components/air-cooling/noctua-explores-2-000w-micro-channel-air-cooling-partners-with-forced-physics-to-develop-vacuum-pump-level-airflow-for-desktop-pcs",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T14:42:58+00:00",
    "summary": "Noctua and Forced Physics are exploring whether densely packed micro-channels can provide extreme cooling performance without the noise associated with high-pressure airflow"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/save-usd250-on-this-award-winning-elegoo-resin-3d-printer-with-an-integrated-heater-and-16k-resolution-39-percent-discount-on-the-saturn-4-ultra-16k-gets-you-a-hugely-accurate-printer-with-fast-speeds-and-a-tilt-release-vat",
    "domain": "AI 算力 / 半导体",
    "title": "Save $250 on this award-winning Elegoo resin 3D printer with an integrated heater and 16K resolution",
    "url": "https://www.tomshardware.com/3d-printing/save-usd250-on-this-award-winning-elegoo-resin-3d-printer-with-an-integrated-heater-and-16k-resolution-39-percent-discount-on-the-saturn-4-ultra-16k-gets-you-a-hugely-accurate-printer-with-fast-speeds-and-a-tilt-release-vat",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T13:33:16+00:00",
    "summary": "This Elegoo Saturn 4 Ultra, one of the best resin 3D printers you can buy, is on sale for $359 right now, saving you 40% on its usual price."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/laptop-maker-says-ddr5-so-dimms-are-6x-pricier-than-last-year-schenker-says-other-component-costs-are-rising-too-announces-price-hikes",
    "domain": "AI 算力 / 半导体",
    "title": "DDR5 laptop memory prices surge 6X in 12 months",
    "url": "https://www.tomshardware.com/laptops/laptop-maker-says-ddr5-so-dimms-are-6x-pricier-than-last-year-schenker-says-other-component-costs-are-rising-too-announces-price-hikes",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T13:00:00+00:00",
    "summary": "XMG noted that SO-DIMM prices have jumped 6x, with other components like PCBs, CPUs, and GPUs also facing increasing costs. This has forced the niche laptop manufacturer to bump their SRPs between $11"
  },
  {
    "id": "hn:49773511",
    "domain": "AI 算力 / 半导体",
    "title": "Every Nvidia GPU has 10 to 30 RISC-V cores inside it",
    "url": "https://www.xda-developers.com/your-nvidia-gpu-dozens-risc-v-cores-one-took-over-graphics-driver/",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-09-20T07:50:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49777694",
    "domain": "AI 算力 / 半导体",
    "title": "Autonomous strike drone uses Nvidia Jetson Orin Nano to pick and bomb targets",
    "url": "https://www.tomshardware.com/tech-industry/drones/autonomous-strike-drone-uses-nvidia-jetson-orin-nano-to-independently-pick-and-bomb-targets-swedish-startups-attack-drones-run-small-ai-model-require-no-human-input-and-zero-external-comms",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-09-20T17:07:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49745610",
    "domain": "AI 算力 / 半导体",
    "title": "Run QWEN3.8 27B on 16gb Nvidia GPUs",
    "url": "https://github.com/MiaAI-Lab/Qwen3.8-27B-16gb-NVIDIA-GPUs-one-click-install",
    "source": "Pragmata",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-09-17T19:46:57+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/semicon-india-2026-startup-mitra-sheds-light-on-early-stage-silicon-startup-funding/",
    "domain": "AI 算力 / 半导体",
    "title": "SEMICON India 2026: Startup Mitra Sheds Light on Early-Stage Silicon Startup Funding",
    "url": "https://www.eetimes.com/semicon-india-2026-startup-mitra-sheds-light-on-early-stage-silicon-startup-funding/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T08:15:06+00:00",
    "summary": "Indian semiconductor startups are seeking capital beyond seed rounds as they advance from prototypes and tape-out toward volume production. The post SEMICON India 2026: Startup Mitra Sheds Light on Ea"
  },
  {
    "id": "rss:https://www.eetimes.com/from-qubits-to-workflows-rethinking-quantum-computing/",
    "domain": "AI 算力 / 半导体",
    "title": "From Qubits to Workflows: Rethinking Quantum Computing",
    "url": "https://www.eetimes.com/from-qubits-to-workflows-rethinking-quantum-computing/",
    "source": "Kevin Hein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T19:00:00+00:00",
    "summary": "IBM’s quantum-centric push makes QPUs another accelerator in hybrid AI-HPC workflows. The post From Qubits to Workflows: Rethinking Quantum Computing appeared first on EE Times."
  },
  {
    "id": "hn:49727093",
    "domain": "AI 算力 / 半导体",
    "title": "Apple May Return to Server Market with Nvidia Technology",
    "url": "https://www.macrumors.com/2026/09/16/apple-may-return-to-server-market/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-09-16T13:54:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:49657991",
    "domain": "AI 算力 / 半导体",
    "title": "How to Build a $20B Semiconductor Fab (2024)",
    "url": "https://www.construction-physics.com/p/how-to-build-a-20-billion-semiconductor",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-09-11T13:22:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49537553",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Flash and 3.8 Flash Cyber",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/",
    "source": "bratao",
    "platform": "hackernews",
    "points": 1160,
    "published_at": "2026-09-02T15:12:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49797982",
    "domain": "大厂 AI 动态",
    "title": "I said no and Apple said yes",
    "url": "https://dbushell.com/2026/09/22/apple-intelligence/",
    "source": "thatslast",
    "platform": "hackernews",
    "points": 881,
    "published_at": "2026-09-22T08:04:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49848269",
    "domain": "大厂 AI 动态",
    "title": "Ollaya – Ollama for open-source, Jev-style decision models",
    "url": "https://ollaya.dev/",
    "source": "Ardakilic",
    "platform": "hackernews",
    "points": 608,
    "published_at": "2026-09-25T18:33:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611251",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas: a high-resolution map of human DNA",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/",
    "source": "utiiiD",
    "platform": "hackernews",
    "points": 607,
    "published_at": "2026-09-08T14:55:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49715947",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Live and 3.8 Live Extended Thinking",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/",
    "source": "leumon",
    "platform": "hackernews",
    "points": 492,
    "published_at": "2026-09-15T17:38:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49552299",
    "domain": "大厂 AI 动态",
    "title": "WeatherNext 3",
    "url": "https://deepmind.google/science/weathernext/",
    "source": "matthieu_bl",
    "platform": "hackernews",
    "points": 406,
    "published_at": "2026-09-03T16:06:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49790409",
    "domain": "大厂 AI 动态",
    "title": "Turn off and restrict access to Apple Intelligence features on Mac",
    "url": "https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac",
    "source": "alwillis",
    "platform": "hackernews",
    "points": 353,
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
    "points": 330,
    "published_at": "2026-09-23T15:29:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49844896",
    "domain": "大厂 AI 动态",
    "title": "Microsoft abandons personal AI chatbot race with Copilot reboot",
    "url": "https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 155,
    "published_at": "2026-09-25T14:07:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49854945",
    "domain": "大厂 AI 动态",
    "title": "The Copilot+ PC brand is dead",
    "url": "https://www.windowscentral.com/microsoft/windows-11/the-copilot-pc-brand-is-dead-microsoft-and-pc-makers-quietly-pull-back-on-tarnished-windows-11-ai-pc-branding",
    "source": "bj-rn",
    "platform": "hackernews",
    "points": 114,
    "published_at": "2026-09-26T09:55:38+00:00",
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
    "id": "hn:49602490",
    "domain": "大厂 AI 动态",
    "title": "Emacs Bedrock 2.0",
    "url": "https://lambdaland.org/posts/2026-09-06-bedrock-v2/",
    "source": "ashton314",
    "platform": "hackernews",
    "points": 191,
    "published_at": "2026-09-07T20:12:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49859982",
    "domain": "大厂 AI 动态",
    "title": "Faster prompt lookup drafting in llama.cpp",
    "url": "https://jadidbourbaki.github.io/blog/prompt-lookup-llama-cpp/",
    "source": "pptadversary",
    "platform": "hackernews",
    "points": 78,
    "published_at": "2026-09-26T19:57:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:49829472",
    "domain": "大厂 AI 动态",
    "title": "Fourier Analysis: Drawing Llamas with Circles",
    "url": "https://adekau.github.io/posts/2020/llamas.html",
    "source": "cebert",
    "platform": "hackernews",
    "points": 78,
    "published_at": "2026-09-24T12:03:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49740330",
    "domain": "大厂 AI 动态",
    "title": "I had Gemini train its own replacement for $9",
    "url": "https://www.petervijeh.com/projects/reddit-ner",
    "source": "p-s-v",
    "platform": "hackernews",
    "points": 88,
    "published_at": "2026-09-17T13:17:16+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/1001219/honor-magic-9-pro-max-arri-cameras-snapdragon-battery-design-china",
    "domain": "大厂 AI 动态",
    "title": "Honor’s Magic 9 Pro Max has a big camera and a bigger battery",
    "url": "https://www.theverge.com/tech/1001219/honor-magic-9-pro-max-arri-cameras-snapdragon-battery-design-china",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T08:00:36+00:00",
    "summary": "Honor launches its new Magic 9 flagship phones in China today, and the 9 Pro Max features a design revamp, a capable camera, and a colossal battery. This is Honor's first flagship launch - Robot Phone"
  },
  {
    "id": "rss:https://www.theverge.com/games/1001206/out-of-the-park-baseball-cozy-sim-video-game-review",
    "domain": "大厂 AI 动态",
    "title": "Out of the Park Baseball lets me enjoy baseball even when the Mets suck",
    "url": "https://www.theverge.com/games/1001206/out-of-the-park-baseball-cozy-sim-video-game-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T21:59:57+00:00",
    "summary": "If you were to ask me what game or game series I've sunk the most time into, the answer would be easy: Out of the Park Baseball (OOTP). I have spent roughly 2,300 hours, according to Steam, playing va"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1001193/engram-sampler-ai-hallucinations-music",
    "domain": "大厂 AI 动态",
    "title": "Engram is a sampler that turns broken AI hallucinations into music",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1001193/engram-sampler-ai-hallucinations-music",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T20:46:36+00:00",
    "summary": "Music startup Thoughtful Things has just launched the Kickstarter campaign for its first instrument, Engram. It's a sampler and groovebox that uses AI to mangle incoming audio and even hallucinate com"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1001178/openai-agents-bruteforce-un-website",
    "domain": "大厂 AI 动态",
    "title": "OpenAI agents tried to ‘bruteforce’ a UN website",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1001178/openai-agents-bruteforce-un-website",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T17:21:07+00:00",
    "summary": "Security researcher Rowan Howard-Jones says that OpenAI agents scanned the UN Conference on Trade and Development's (UNCTAD) statistics site over 16,000 times between April and June. While the inciden"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/1000517/why-olpcs-100-laptop-never-stood-a-chance",
    "domain": "大厂 AI 动态",
    "title": "Why OLPC’s $100 laptop never stood a chance",
    "url": "https://www.theverge.com/podcast/1000517/why-olpcs-100-laptop-never-stood-a-chance",
    "source": "Verge Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T12:25:00+00:00",
    "summary": "The idea was big, exciting, and inspiring: What if we could get every kid in the world access to a computer? For a bunch of thinkers and executives in Silicon Valley, it felt like the way to fix every"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1000424/googlebooks-meta-ray-ban-audio-control-resonant-microsoft-surface-mouse",
    "domain": "大厂 AI 动态",
    "title": "Googlebooks might be the real deal",
    "url": "https://www.theverge.com/tech/1000424/googlebooks-meta-ray-ban-audio-control-resonant-microsoft-surface-mouse",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T12:00:00+00:00",
    "summary": "Hi, friends! Welcome to Installer No. 145, your guide to the best and Verge-iest stuff in the world. (If you're new here, welcome, I'm happy to be done traveling for a bit, and also you can read all t"
  },
  {
    "id": "rss:https://www.theverge.com/column/1000778/smart-home-june-oven-graveyard",
    "domain": "大厂 AI 动态",
    "title": "The smart home graveyard is getting crowded",
    "url": "https://www.theverge.com/column/1000778/smart-home-june-oven-graveyard",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T12:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more on the fragile state of your connected devices, follow Jennifer Pattison Tuohy. The Stepback a"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1001118/apple-hit-with-5-7-billion-in-damages-over-haptic-patents",
    "domain": "大厂 AI 动态",
    "title": "Apple hit with $5.7 billion in damages over haptic patents",
    "url": "https://www.theverge.com/tech/1001118/apple-hit-with-5-7-billion-in-damages-over-haptic-patents",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T21:30:01+00:00",
    "summary": "Haptics tech company Taction sued Apple in 2021, alleging it infringed two of its patents. Now a federal jury in San Diego has awarded Taction over $5.7 billion in damages. According to CNBC, \"The law"
  },
  {
    "id": "rss:https://www.theverge.com/report/1000994/decap-drums-that-knock-interview",
    "domain": "大厂 AI 动态",
    "title": "Decap is the man behind the drums behind your favorite song",
    "url": "https://www.theverge.com/report/1000994/decap-drums-that-knock-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T19:30:00+00:00",
    "summary": "I don't think I'm going to hurt anyone's feelings by pointing out that Decap doesn't have the name recognition of Kendrick Lamar, Olivia Rodrigo, or Charli XCX. But his fingerprints are all over track"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1001056/this-american-life-npr-kids-group-chat-comment-section",
    "domain": "大厂 AI 动态",
    "title": "Kids turned the comment section of an NPR podcast into a group chat",
    "url": "https://www.theverge.com/entertainment/1001056/this-american-life-npr-kids-group-chat-comment-section",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T17:32:35+00:00",
    "summary": "Middle schoolers, likely blocked from other apps and social networks, apparently turned the Spotify comment section under an episode of NPR's Wild Card into an impromptu group chat. In a new episode o"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/27/truecaller-takes-its-scam-intelligence-to-the-open-web-as-it-looks-beyond-caller-id/",
    "domain": "大厂 AI 动态",
    "title": "Truecaller takes its scam intelligence to the open web as it looks beyond caller ID",
    "url": "https://techcrunch.com/2026/09/27/truecaller-takes-its-scam-intelligence-to-the-open-web-as-it-looks-beyond-caller-id/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:30:00+00:00",
    "summary": "Truecaller finds a new way to reach users as pressure grows on its traditional caller ID business in India, its biggest market."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/27/anthropics-ceo-is-about-to-have-dinner-with-president-trump/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s CEO is about to have dinner with President Trump",
    "url": "https://techcrunch.com/2026/09/27/anthropics-ceo-is-about-to-have-dinner-with-president-trump/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T20:34:28+00:00",
    "summary": "This will be the first one-on-one meeting between Dario Amodei and Donald Trump"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/27/can-muse-overcome-metas-trust-issues/",
    "domain": "大厂 AI 动态",
    "title": "Can Muse overcome Meta’s trust issues?",
    "url": "https://techcrunch.com/2026/09/27/can-muse-overcome-metas-trust-issues/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T19:57:30+00:00",
    "summary": "On Equity, we discussed how Meta's AI announcement managed to steal the spotlight from OpenAI and Anthropic."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/27/anthropics-dario-amodei-gets-the-snl-treatment/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s Dario Amodei gets the SNL treatment",
    "url": "https://techcrunch.com/2026/09/27/anthropics-dario-amodei-gets-the-snl-treatment/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T16:30:00+00:00",
    "summary": "\"AI is the devil and I its maker.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/27/techcrunch-mobility-av-companies-pick-their-lanes/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: AV companies pick their lanes",
    "url": "https://techcrunch.com/2026/09/27/techcrunch-mobility-av-companies-pick-their-lanes/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T16:02:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, the role AI is playing in it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/27/sennheiser-momentum-5-review-great-sound-incredible-battery-life-and-few-compromises/",
    "domain": "大厂 AI 动态",
    "title": "Sennheiser Momentum 5 review: Great sound, incredible battery life, and few compromises",
    "url": "https://techcrunch.com/2026/09/27/sennheiser-momentum-5-review-great-sound-incredible-battery-life-and-few-compromises/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T15:00:00+00:00",
    "summary": "I spent the last few weeks with the Sennheiser Momentum 5 to determine if this pair actually stands out, testing everything from sound quality and noise cancellation to comfort and battery life."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/26/pnoes-new-face-mask-wants-to-make-lab-grade-breath-testing-a-self-serve-affair/",
    "domain": "大厂 AI 动态",
    "title": "PNOE’s new face mask wants to make lab-grade breath testing a self-serve affair",
    "url": "https://techcrunch.com/2026/09/26/pnoes-new-face-mask-wants-to-make-lab-grade-breath-testing-a-self-serve-affair/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T01:40:30+00:00",
    "summary": "PNOĒ, the Malden, Mass.-based startup whose breath-analyzing mask used to bear an unfortunate resemblance to Bane's, is launching a sleeker self-serve version on October 1 that lets gym-goers measure "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/26/google-tests-buying-from-walmart-owned-flipkart-through-gemini-and-ai-mode-in-india/",
    "domain": "大厂 AI 动态",
    "title": "Google tests buying from Walmart-owned Flipkart through Gemini and AI Mode in India",
    "url": "https://techcrunch.com/2026/09/26/google-tests-buying-from-walmart-owned-flipkart-through-gemini-and-ai-mode-in-india/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T01:30:00+00:00",
    "summary": "The limited test covers select products and users, with a broader rollout planned for later in October."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/26/insurers-claim-ai-is-already-increasing-healthcare-costs/",
    "domain": "大厂 AI 动态",
    "title": "Insurers claim AI is already increasing healthcare costs",
    "url": "https://techcrunch.com/2026/09/26/insurers-claim-ai-is-already-increasing-healthcare-costs/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T21:02:06+00:00",
    "summary": "Blue Cross Blue Shield says hospital use of AI tools led to an additional $942M in healthcare spending over a two-year period."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/26/tiktok-agrees-to-pay-at-least-100m-in-alabama-settlement/",
    "domain": "大厂 AI 动态",
    "title": "TikTok agrees to pay at least $100M in Alabama settlement",
    "url": "https://techcrunch.com/2026/09/26/tiktok-agrees-to-pay-at-least-100m-in-alabama-settlement/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T20:24:45+00:00",
    "summary": "TikTok will pay Alabama at least $100 million in a settlement tied to allegations that the short-form video platform misled users about safety and was designed to addict children."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/26/meta-says-it-will-run-ads-for-musk-documentary-after-all/",
    "domain": "大厂 AI 动态",
    "title": "Meta and YouTube say they will run ads for ‘Musk’ documentary after all",
    "url": "https://techcrunch.com/2026/09/26/meta-says-it-will-run-ads-for-musk-documentary-after-all/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T17:44:00+00:00",
    "summary": "Two companies now say they will accept advertising for director Alex Gibney’s upcoming documentary about Elon Musk, following earlier reporting that a number of social media platforms had rejected the"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/26/levoits-new-air-purifier-is-for-the-pet-odors-that-have-taken-over-your-apartment/",
    "domain": "大厂 AI 动态",
    "title": "Levoit’s new air purifier is for the pet odors that have taken over your apartment",
    "url": "https://techcrunch.com/2026/09/26/levoits-new-air-purifier-is-for-the-pet-odors-that-have-taken-over-your-apartment/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T17:00:00+00:00",
    "summary": "This $189.99 air purifier is specifically designed to tackle pet odors, removing up to 70% in one hour."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/26/i-created-an-interactive-digital-avatar-of-myself-and-you-can-talk-to-it/",
    "domain": "大厂 AI 动态",
    "title": "I created an interactive digital avatar of myself — and you can talk to it",
    "url": "https://techcrunch.com/2026/09/26/i-created-an-interactive-digital-avatar-of-myself-and-you-can-talk-to-it/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T14:00:00+00:00",
    "summary": "After obtaining an interactive avatar and training it to discuss venture fraud, I have mixed feelings about making AI clones of ourselves."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/how-the-smithsonian-became-the-latest-front-in-trumps-culture-war/",
    "domain": "大厂 AI 动态",
    "title": "How the Smithsonian became the latest front in Trump’s culture war",
    "url": "https://arstechnica.com/tech-policy/2026/09/how-the-smithsonian-became-the-latest-front-in-trumps-culture-war/",
    "source": "Alec MacGillis, ProPublica",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T11:00:12+00:00",
    "summary": "The Smithsonian has faced withering pressure from the Trump administration."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/09/teslas-big-electric-truck-faces-an-even-bigger-infrastructure-challenge/",
    "domain": "大厂 AI 动态",
    "title": "Tesla’s big electric truck faces an even bigger infrastructure challenge",
    "url": "https://arstechnica.com/cars/2026/09/teslas-big-electric-truck-faces-an-even-bigger-infrastructure-challenge/",
    "source": "Aarian Marshall, wired.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T10:45:09+00:00",
    "summary": "The 500-mile Semi arrives as charging gaps still limit electric trucking."
  },
  {
    "id": "rss:https://www.producthunt.com/products/shotcandy",
    "domain": "大厂 AI 动态",
    "title": "Shotcandy",
    "url": "https://www.producthunt.com/products/shotcandy",
    "source": "Bilal Tahir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T06:43:23+00:00",
    "summary": "Make Your Screenshots Look Amazing Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/mum-multi-project-markdown",
    "domain": "大厂 AI 动态",
    "title": "MuM",
    "url": "https://www.producthunt.com/products/mum-multi-project-markdown",
    "source": "IceskYsl",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T05:04:26+00:00",
    "summary": "A reading-first Markdown engine for macOS Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/ryu-journal",
    "domain": "大厂 AI 动态",
    "title": "Ryu Journal",
    "url": "https://www.producthunt.com/products/ryu-journal",
    "source": "Chris Messina",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T04:28:31+00:00",
    "summary": "A journal to help busy minds let go Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/arc-ai-screen-assistant",
    "domain": "大厂 AI 动态",
    "title": "Arc",
    "url": "https://www.producthunt.com/products/arc-ai-screen-assistant",
    "source": "Mamata",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T17:11:05+00:00",
    "summary": "Your mobile AI assistant on any screen Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/harness-103",
    "domain": "大厂 AI 动态",
    "title": "Harness Router",
    "url": "https://www.producthunt.com/products/harness-103",
    "source": "Kamil Mosciszko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T07:03:34+00:00",
    "summary": "Fast AI tool routing powered by Jev. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/sayble",
    "domain": "大厂 AI 动态",
    "title": "Sayble",
    "url": "https://www.producthunt.com/products/sayble",
    "source": "Alexis Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T19:46:24+00:00",
    "summary": "AI copilot for calls that tells you what to say next Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/favenest",
    "domain": "大厂 AI 动态",
    "title": "FaveNest",
    "url": "https://www.producthunt.com/products/favenest",
    "source": "Dion Purushotham",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T21:25:00+00:00",
    "summary": "Bookmarks that organize themselves with Apple Intelligence Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/pip-9",
    "domain": "大厂 AI 动态",
    "title": "PIP",
    "url": "https://www.producthunt.com/products/pip-9",
    "source": "Victorr",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-27T16:48:56+00:00",
    "summary": "AI buddy on your computer Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/dina",
    "domain": "大厂 AI 动态",
    "title": "Dina 4.5",
    "url": "https://www.producthunt.com/products/dina",
    "source": "Zaid",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:18:46+00:00",
    "summary": "Beautiful screen recordings, screenshots, and 3D motion Discussion | Link"
  },
  {
    "id": "hn:49619848",
    "domain": "股票",
    "title": "Apple iPod Engraver (2019)",
    "url": "https://dunstanorchard.com/apple-ipod-engraver/",
    "source": "NaOH",
    "platform": "hackernews",
    "points": 288,
    "published_at": "2026-09-09T01:57:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49826087",
    "domain": "股票",
    "title": "16GB iPod Nano 3G Upgrade",
    "url": "https://tuckerosman.com/projects/16gb-ipod-nano",
    "source": "Ivoah",
    "platform": "hackernews",
    "points": 160,
    "published_at": "2026-09-24T03:58:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49712746",
    "domain": "股票",
    "title": "Global bond yields hit 2008 highs, raising stakes for big borrowers",
    "url": "https://www.reuters.com/world/asia-pacific/bond-selloff-drives-us-benchmark-beyond-5-stocks-rattled-2026-09-15/",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 167,
    "published_at": "2026-09-15T14:07:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611240",
    "domain": "股票",
    "title": "iPod Classic 6G in QEMU",
    "url": "https://www.reddit.com/r/emulation/s/VL4Au2HGxq",
    "source": "dmonterocrespo",
    "platform": "hackernews",
    "points": 162,
    "published_at": "2026-09-08T14:54:57+00:00",
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
    "id": "rss:https://www.netinterest.co/p/the-agents-revolt",
    "domain": "股票",
    "title": "The Agents Revolt",
    "url": "https://www.netinterest.co/p/the-agents-revolt",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:33:27+00:00",
    "summary": "What happens to finance when customers start paying attention"
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
    "id": "hn:49816810",
    "domain": "股票",
    "title": "Trump's 1,156 July Stock Trades Involved AI, Big Oil, Weapons-Makers, and More",
    "url": "https://www.commondreams.org/news/donald-trump-stock-trades",
    "source": "cirelli94",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-23T14:33:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49819274",
    "domain": "股票",
    "title": "Morgan Stanley Investment-Bank Deal List Leaked in Email Misfire",
    "url": "https://finance.yahoo.com/markets/stocks/articles/morgan-stanley-investment-bank-deal-124657863.html",
    "source": "wslh",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-09-23T17:08:35+00:00",
    "summary": ""
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
    "id": "hn:49594296",
    "domain": "股票",
    "title": "OpenAI 2025 financials $38.5B loss ahead of IPO",
    "url": "https://qz.com/openai-leaked-financials-losses-revenue-ipo-061626",
    "source": "u1hcw9nx",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-09-07T05:41:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49696420",
    "domain": "股票",
    "title": "Global AI stocks fall as industry chiefs call for slowing development",
    "url": "https://www.reuters.com/world/china/ai-linked-asian-stocks-slump-after-top-lab-ceos-call-slowing-down-technologys-2026-09-14/",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-09-14T13:21:51+00:00",
    "summary": ""
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
    "id": "hn:49778029",
    "domain": "金融",
    "title": "Samsung is expected to more than double output of its HBM4 and HBM4E DRAM",
    "url": "https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 561,
    "published_at": "2026-09-20T17:38:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49594251",
    "domain": "金融",
    "title": "Switzerland's Federal Government Is Replacing Microsoft on 3k Computers",
    "url": "https://itsfoss.com/news/switzerland-replace-microssoft-pilot/",
    "source": "ivell",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-09-07T05:33:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49822556",
    "domain": "金融",
    "title": "OpenAI breaches Medicare, Albanese reveals",
    "url": "https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html",
    "source": "jonnonz",
    "platform": "hackernews",
    "points": 255,
    "published_at": "2026-09-23T21:01:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49704008",
    "domain": "金融",
    "title": "Amazon vs. Perplexity – U.S. Court of Appeals for the Ninth Circuit",
    "url": "https://law.justia.com/cases/federal/appellate-courts/ca9/26-1444/26-1444-2026-08-04.html",
    "source": "neom",
    "platform": "hackernews",
    "points": 219,
    "published_at": "2026-09-14T21:05:22+00:00",
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
    "id": "hn:49832844",
    "domain": "金融",
    "title": "Federal judge orders Texas to air condition all prisons by the end of 2029",
    "url": "https://www.texastribune.org/2026/09/22/texas-prison-air-conditioning-lawsuit-ruling/",
    "source": "bonefishgrill",
    "platform": "hackernews",
    "points": 118,
    "published_at": "2026-09-24T16:15:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49600997",
    "domain": "金融",
    "title": "No constitutional right to clean water, federal court finds",
    "url": "https://www.usatoday.com/story/news/nation/2026/09/07/court-constitution-right-clean-water/91649488007/",
    "source": "measurablefunc",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-09-07T17:52:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49694840",
    "domain": "金融",
    "title": "How Much Has Trump Made from Crypto? ($1.4B from 2025 Federal Disclosure)",
    "url": "https://www.thepricer.org/how-much-has-trump-made-from-crypto/",
    "source": "cinderelacinder",
    "platform": "hackernews",
    "points": 114,
    "published_at": "2026-09-14T10:56:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49591672",
    "domain": "金融",
    "title": "Hackers have withdrawn ~4k BTC (~$320M) from the Liquid Federation wallet",
    "url": "https://twitter.com/Liquid_BTC/status/2096696272447218108",
    "source": "felipelalli",
    "platform": "hackernews",
    "points": 126,
    "published_at": "2026-09-06T22:43:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49849986",
    "domain": "金融",
    "title": "Show HN: Ekselio – Loveable for finance workflows (local first)",
    "url": "https://www.gptbeyond.com/try?home=1",
    "source": "kdautaj",
    "platform": "hackernews",
    "points": 40,
    "published_at": "2026-09-25T21:09:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596610",
    "domain": "金融",
    "title": "Initial effects of AI technology on employment look positive",
    "url": "https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here",
    "source": "MrBuddyCasino",
    "platform": "hackernews",
    "points": 103,
    "published_at": "2026-09-07T10:38:32+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.30269",
    "domain": "金融",
    "title": "When a Few Misfits Trigger Digital Adoption Cascades: Network Reach, Threshold Heterogeneity, and Performance-Conditioned Complex Contagion in an Agent-Based Model of Firms",
    "url": "https://arxiv.org/abs/2609.30269",
    "source": "Esteve Almirall, Steve Willmott, Ulises Cort\\'es",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.30269v1 Announce Type: new Abstract: Why does a superior technology sometimes spread and sometimes stall, even when its expected returns are much higher? We develop an agent-based model in "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.31236",
    "domain": "金融",
    "title": "Catch-Up and Come Home: Economic Convergence and Return Migration",
    "url": "https://arxiv.org/abs/2609.31236",
    "source": "Kinga Varga, Bence Koll\\'anyi, Johannes Wachs",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.31236v1 Announce Type: new Abstract: The return migration of skilled workers provides origin countries many important benefits. The likelihood of return migration is thought to depend on re"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.31260",
    "domain": "金融",
    "title": "Agentic Limit Order Books: Phase Transitions and Market Impact",
    "url": "https://arxiv.org/abs/2609.31260",
    "source": "Jan Rosenzweig",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.31260v1 Announce Type: new Abstract: We investigate the systemic macroscopic dynamics emerging from Limit Order Books (LOBs) populated exclusively by autonomous reinforcement-learning agent"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.31263",
    "domain": "金融",
    "title": "Taming the Option Factor Zoo: A High-Dimensional Analysis",
    "url": "https://arxiv.org/abs/2609.31263",
    "source": "Alexander Walter, Lukas Zimmer, Maxim Ulrich",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.31263v1 Announce Type: new Abstract: Option-implied factors are largely, but not entirely, spanned by the equity factor zoo. We construct 137 option-implied characteristics for optionable U"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.31468",
    "domain": "金融",
    "title": "PriceBench: A Diagnostic Benchmark for Price, Quality, and Brand Preferences in LLM Booking Agents",
    "url": "https://arxiv.org/abs/2609.31468",
    "source": "Pavel Kireyev",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.31468v1 Announce Type: new Abstract: LLMs increasingly act as purchasing agents, which makes the LLM, not the user, the one choosing among the options that satisfy a request; its preference"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.31512",
    "domain": "金融",
    "title": "Tolerable Inflation, Intolerable Uncertainty",
    "url": "https://arxiv.org/abs/2609.31512",
    "source": "Eric Vansteenberghe",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.31512v1 Announce Type: new Abstract: Numerical inflation targets anchor beliefs. Across euro-area and US professional forecasts, inflation swaps and options, and realized inflation, uncerta"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.30316",
    "domain": "金融",
    "title": "PALM: Point-in-Time Adaptation for Financial Language Models",
    "url": "https://arxiv.org/abs/2609.30316",
    "source": "Seunghan Lee, Jun Seo, Jaehoon Lee, Junhyeok Kang, Sangjun Han, Sungdong Yoo, Minjae Kim, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Soonyoung Lee, Wonbin Ahn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.30316v1 Announce Type: cross Abstract: Language models used in financial backtests suffer from look-ahead bias, as a model trained on text published after the study period has already obser"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.30329",
    "domain": "金融",
    "title": "Stability of Change-of-Num\\'eraire Reweighting: An Exact Wasserstein Boundary",
    "url": "https://arxiv.org/abs/2609.30329",
    "source": "Shaosai Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.30329v1 Announce Type: cross Abstract: Reweighting a probability law by a positive num\\'eraire and pushing forward the payoff-to-num\\'eraire ratio yields the change-of-num\\'eraire reweighti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.30684",
    "domain": "金融",
    "title": "PixSim: a calibrated open-source simulator of instant-payment fraud, recovery and interdiction under analyst capacity constraints",
    "url": "https://arxiv.org/abs/2609.30684",
    "source": "Bashir Zeimarani, Alireza Khatib, Somayeh Mousavinasr, Carlos Maur\\'icio Serodio Figueiredo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.30684v1 Announce Type: cross Abstract: Brazil's Pix settles about 5.9 billion instant, irreversible transfers a month. A fraudulent transfer can be recovered only while the funds remain in "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.30940",
    "domain": "金融",
    "title": "Financial Fragility in Societies of LLM Agents: Coordination Failures and Stabilizing Mechanisms",
    "url": "https://arxiv.org/abs/2609.30940",
    "source": "Zhenhao Fu, Ruipeng Xu, Qibing Ren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.30940v1 Announce Type: cross Abstract: Individually protective decisions can produce avoidable collective failures. As large language model (LLM) agents take on greater roles in financial d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.31013",
    "domain": "金融",
    "title": "Same Text, Different Numbers: The Divergence of LLM-Based Measures",
    "url": "https://arxiv.org/abs/2609.31013",
    "source": "Hamid Boustanifar, Sasan Mansouri",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.31013v1 Announce Type: cross Abstract: Researchers increasingly use generative large language models (LLMs) to convert corporate text into empirical variables. We examine the extent to whic"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.31345",
    "domain": "金融",
    "title": "On the asymptotic shape of quantile surfaces",
    "url": "https://arxiv.org/abs/2609.31345",
    "source": "Florian Gach, Simon Hochgerner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.31345v1 Announce Type: cross Abstract: This article is concerned with the asymptotic shape of quantile surfaces, defined as the set of quantiles at a given level $\\alpha$ generated by a con"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.31379",
    "domain": "金融",
    "title": "How Much Must a Private Mempool Hide? Exact Leakage Thresholds for Sandwich Attacks",
    "url": "https://arxiv.org/abs/2609.31379",
    "source": "Tingyi Lin, Jiazhuo Li, Ruoran Lai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.31379v1 Announce Type: cross Abstract: Private and encrypted mempools hide pending transactions to stop sandwich attacks and other forms of maximal extractable value (MEV), but what they hi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.31578",
    "domain": "金融",
    "title": "Algorithmic trading and stochastic integration",
    "url": "https://arxiv.org/abs/2609.31578",
    "source": "Aleksandar Arandjelovic, Uwe Schmock",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.31578v1 Announce Type: cross Abstract: We study simple predictable processes whose coefficients are represented by neural networks. On finite measure spaces, we establish density results fo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2310.09295",
    "domain": "金融",
    "title": "On the Impact of Insurance on Households Susceptible to Random Proportional Losses: An Analysis of Poverty Trapping",
    "url": "https://arxiv.org/abs/2310.09295",
    "source": "Kira Henshaw, Jorge Ramirez, Jos\\'e Miguel Flores-Contr\\'o, Sooie-Hoe Loke, Enrique A. Thomann, Corina Constantinescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2310.09295v3 Announce Type: replace Abstract: The trapping probability is studied for households' capital assuming that losses are proportional to the accumulated capital. We consider households"
  },
  {
    "id": "rss:https://arxiv.org/abs/2405.04352",
    "domain": "金融",
    "title": "Return to Office and the Tenure Distribution",
    "url": "https://arxiv.org/abs/2405.04352",
    "source": "David Van Dijcke, Florian Gunsilius, Austin Wright",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2405.04352v2 Announce Type: replace Abstract: Debates over return-to-office mandates have intensified since the COVID-19 pandemic ended, though their economic implications remain poorly understo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2409.05397",
    "domain": "金融",
    "title": "The Global Minimum Tax, Investment Incentives and Asymmetric Tax Competition",
    "url": "https://arxiv.org/abs/2409.05397",
    "source": "Xuyang Chen, Rui Sun",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2409.05397v4 Announce Type: replace Abstract: This paper investigates the OECD's global minimum tax (GMT) in a formal model of tax competition between asymmetric countries. We consider both prof"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.10857",
    "domain": "金融",
    "title": "SPX-VIX Risk Computations Via Perturbed Optimal Transport",
    "url": "https://arxiv.org/abs/2603.10857",
    "source": "Charlie Che, Hanxuan Lin, Yudong Yang, Guofan Hu, Lei Fang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2603.10857v4 Announce Type: replace Abstract: We propose a model independent framework for generating SPX and VIX risk scenarios based on a joint optimal transport calibration of their market sm"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.20050",
    "domain": "金融",
    "title": "Information Aggregation with AI Agents",
    "url": "https://arxiv.org/abs/2604.20050",
    "source": "Spyros Galanis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2604.20050v4 Announce Type: replace Abstract: Can Large Language Models (AI agents) aggregate dispersed private information through trading and reason about the knowledge of others by observing "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.05357",
    "domain": "金融",
    "title": "High-Frequency Exponential-Utility Maximization under Fractional Brownian Motion",
    "url": "https://arxiv.org/abs/2608.05357",
    "source": "Yan Dolinsky",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2608.05357v2 Announce Type: replace Abstract: We study utility maximization for high-frequency trading in fractional Brownian motion models. We first consider exponential utility in the discreti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.30558",
    "domain": "金融",
    "title": "A note on markets with semi-static trading strategies",
    "url": "https://arxiv.org/abs/2608.30558",
    "source": "Mikl\\'os R\\'asonyi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2608.30558v2 Announce Type: replace Abstract: We consider a discrete-time financial market model where, in addition to finitely many dynamically traded assets, there are also (possibly infinitel"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.05047",
    "domain": "金融",
    "title": "Gatheral's Conjecture Revisited",
    "url": "https://arxiv.org/abs/2609.05047",
    "source": "Vladimir Lucic",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.05047v5 Announce Type: replace Abstract: We consider the Heston model with perfect negative spot--variance correlation and its one-dimensional local-volatility projection. Let $I_T^{\\mathrm"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.15452",
    "domain": "金融",
    "title": "Computing Endogenous Transformations in Processing Networks: A Dynamic Calibration Approach",
    "url": "https://arxiv.org/abs/2609.15452",
    "source": "Satoshi Nakano, Kazuhiko Nishimura",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.15452v4 Announce Type: replace Abstract: Understanding how global supply chains endogenously transform in response to disruptions requires a parametric model of processing networks with non"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.22893",
    "domain": "金融",
    "title": "Universal Diffusion Models for Implied Volatility Surfaces: Learning Shared Dynamics Across Stocks",
    "url": "https://arxiv.org/abs/2609.22893",
    "source": "Mingzhi Yang, Sheng Wang, Chao Zhang, Ruikun Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.22893v2 Announce Type: replace Abstract: Modeling the dynamics of option implied volatility surface (IVS) is crucial for pricing, hedging, and risk-managing option portfolios. We develop a "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.28504",
    "domain": "金融",
    "title": "AI in Science: Early Insights",
    "url": "https://arxiv.org/abs/2609.28504",
    "source": "Mihai Codreanu, Alex Imas, Juan Mateos-Garcia, Joseph Emmens, Evalyne Muiruri, Arthur Turrell, Julian Jacobs, Atoosa Kasirzadeh, Ana Trisovic, Yiyuan Chen, Tanya Rodchenko, Catherine Pollard, Scott Strand, Daniel Rock, Zanna Iscenko, Fabien Curto Millet, Neil Thompson, James Manyika",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-28T04:00:00+00:00",
    "summary": "arXiv:2609.28504v2 Announce Type: replace Abstract: Scientific progress is a key driver of economic growth and prosperity. There is great excitement - but also concerns - about the impacts of AI on sc"
  },
  {
    "id": "hn:49700413",
    "domain": "金融",
    "title": "US 10-Year Breaches 5% as Inflation, Supply Worries Mount",
    "url": "https://www.bloomberg.com/news/articles/2026-09-14/us-10-year-yield-breaches-5-as-inflation-supply-worries-mount",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-09-14T17:11:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49828019",
    "domain": "金融",
    "title": "Show HN: Trader News – Hacker News for Finance",
    "url": "https://news.ycombinator.com/item?id=49828019",
    "source": "FailMore",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-09-24T08:54:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49730769",
    "domain": "金融",
    "title": "Feds Want California to Give Up 14 Years of Broadband Protections. It Should Sue",
    "url": "https://cyberlaw.stanford.edu/blog/2026/09/california-is-being-asked-to-give-up-14-years-of-broadband-protections-it-doesnt-have-to/",
    "source": "rsingel",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-09-16T18:09:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:49612981",
    "domain": "金融",
    "title": "DOJ Blocked ICE Agent Shooting Charge over Federal Prosecutor's Objections",
    "url": "https://www.propublica.org/article/doj-blocks-charges-ice-agent-minneapolis-julio-cesar-sosa-celis",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-09-08T16:54:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49564189",
    "domain": "金融",
    "title": "Norway's Oil Fund Proposes Selling Roughly $80B in U.S. Treasurys",
    "url": "https://www.wsj.com/finance/investing/norways-oil-fund-proposes-cut-to-government-bond-holdings-d930893f",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-09-04T13:15:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:49625461",
    "domain": "金融",
    "title": "Teen reading slumps to worst this century due to surge in screen time",
    "url": "https://finance.yahoo.com/news/teen-reading-slumps-worst-century-111013754.html",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-09-09T12:29:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49514224",
    "domain": "金融",
    "title": "Monero Inflation Checker – FCMP++",
    "url": "https://www.reddit.com/r/Monero/comments/1w3hcos/monero_inflation_checker_fcmp/",
    "source": "Cider9986",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-08-31T20:00:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49762617",
    "domain": "金融",
    "title": "Elon Musk and Tesla Forged a New EV Path",
    "url": "https://spectrum.ieee.org/elon-musk-tesla",
    "source": "vinhnx",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-09-19T02:08:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49633640",
    "domain": "金融",
    "title": "DHS Program Analyzes Americans' Finances to Flag Drivers for Traffic Stops",
    "url": "https://www.military.com/dhs-program-analyzes-americans-finances-to-flag-drivers-for-traffic-stops-report",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-09-09T20:22:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:49548497",
    "domain": "金融",
    "title": "Mark Cuban: Why US hospitals \"don't know their costs\"",
    "url": "https://www.beckershospitalreview.com/finance/mark-cuban-why-us-hospitals-dont-know-their-costs/",
    "source": "elo2000",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-09-03T11:07:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49515596",
    "domain": "金融",
    "title": "Congress to vote on denying federal funding to universities that boycott Israel",
    "url": "https://twitter.com/dylanotes/status/2094229210889965634",
    "source": "slowin",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-08-31T22:24:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49551601",
    "domain": "金融",
    "title": "Inside Google’s $200bn Wall Street finance machine for Anthropic",
    "url": "https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c",
    "source": "porridgeraisin",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-09-03T15:26:27+00:00",
    "summary": ""
  }
]
```
