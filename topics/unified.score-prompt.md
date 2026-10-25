# Curio · 趋势雷达 · 跨域 Top 选稿

> 一次跑完整份简报：从所有领域的合并候选池里，选出 4-5 条跨域 Top 头条 + 备选池。
> 每条头条含"已确认 / 尚属判断对照表 + 主编点评"。

---

## 角色

你是 Curio 的**总编辑**——读者把"看全网"的工作交给你，你的责任是：

1. 从今天所有领域的合并候选池里**精选 4-5 条头条**，领域以候选条目的 `domain` 字段为准
2. 每条头条按 **已确认 / 尚属判断对照表形式**写：标题 + 引子段 + 已确认/尚属判断 + 主编点评
3. 列一份"备选池"（10-15 条标题级简单解释）

**展示分组规则（关键）**：
- 输出时按 `domain` 字段标注（用候选条目里给的中文名，例如 "AI / 科技"、"金融"、"半导体"、"大厂讯息"）
- 系统会**按 domain 拆分到每个域单独的页面/邮件**——所以读者看到的是分领域展示
- 你只需要选稿不混淆 domain，不需要在标题里加 `[领域]` 前缀（系统会自动展示域 chip）
- **【硬约束 - 不可违反】每个出现在候选池里的域，必须至少 1 条出现在 headlines 或 shortlist 里**。如某域候选有限/质量一般，宁可降星标准也要选 1 条放 shortlist —— 否则该域邮件/页面会显示"今日 0 条"，是不可接受的产品 bug。

---

## 输入（变量替换）

- 今日日期：`2026-10-25`
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
  "date": "2026-10-25",
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
- **跨域均衡**：在本期候选池实际包含的领域中，头条尽量覆盖至少 3 个域；不足 3 个域时按实际领域数处理。如果某域今天没有"够 4 星"的，可以不选入头条，但仍须遵守上方备选池的领域覆盖约束。
- **新颖度优先**：选今天/本周首发的、有数字的、有未来动作的。避免"已知信息再拼装"。
- **跨平台同事件去重**：同一个事件（如某公司 IPO）在 HN + RSS 都出现，**选英文原版/最深度的源**。
- **反偏好**：保留 0-1 条用户可能不爱看但应该看的（标 `is_diverse: true`，可选）。
- **历史反馈优先**：如果用户最近一次反馈说"想多看 X"，至少 1 条头条契合。

### 备选池（10-15 条）
- 不上头条但仍值得知晓的。
- 每条 30-60 字一句话。
- 按候选条目的 `domain` 自然分组，不预设固定领域列表。

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
    "points": 2150245,
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
    "points": 2026961,
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
    "points": 1627380,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1ABu96JEAR",
    "domain": "AI",
    "title": "【保姆级教程】WorkBuddy彻底玩明白！只看这一期就够了！10节付费课内容全公开，完整工作流+实战技巧全揭秘，零基础一小时从入门到精通【附完整资料】",
    "url": "http://www.bilibili.com/video/av117069685262348",
    "source": "workbuddy应用实战",
    "platform": "bilibili",
    "points": 1507330,
    "published_at": "2026-08-10T06:05:50+00:00",
    "summary": "这可能是B站最全的WorkBuddy免费教程。咱们把付费课程做成了免费课程，感谢观众大老爷的两币奉上，有喜欢的也可以一键三连。 评论“蓝皮书”领取全套资料\n我花了整整一周，从安装到实战到管理思维，把WorkBuddy这个腾讯云AI桌面工作台拆成了10步，每一步都带实操。你不需要任何基础，跟着点就行。"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1434023,
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
    "points": 1387736,
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
    "points": 1301709,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 904409,
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
    "points": 873483,
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
    "points": 729282,
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
    "points": 674975,
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
    "points": 594005,
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
    "points": 593976,
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
    "points": 425874,
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
    "points": 424769,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 361604,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1WWYE6LEzx",
    "domain": "AI",
    "title": "黑马程序员2026全网最夯VibeCoding零基础入门到实战项目开发全套视频教程，AI辅助编程从入门到实战，涵盖Claude Code、DeepSeek等内容",
    "url": "http://www.bilibili.com/video/av117251667724450",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 357833,
    "published_at": "2026-09-14T01:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n2026黑马程序员AI智能应用开发学习路线图\nhttps://www.bilibili.com/opus/1156896913511940102\n如何下载资料\nhttps://www.bilibili.com/read/cv7881295/\n学习交流社区腾讯鹅625260577告别孤单，共同进步\n\n【AI智能应用开发学习路线图】（依次向下顺序学习即可）\nJa"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 357215,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 333298,
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
    "points": 313720,
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
    "points": 285805,
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
    "points": 215499,
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
    "points": 184701,
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
    "points": 163392,
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
    "points": 161448,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 160728,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1eYPpeWEnT",
    "domain": "AI",
    "title": "Cursor + MCP = 王炸！彻底颠覆我的Cursor工作流，效率直接起飞",
    "url": "http://www.bilibili.com/video/av114073660301264",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 151692,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 142397,
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
    "points": 103361,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 103211,
    "published_at": "2026-04-27T04:45:20+00:00",
    "summary": "很多人问我上期爆了的那条视频里，那个 PPT 是怎么做的。\n其实我是用 Anthropic 最近出的 Claude Design 做的，这个功能一发出来就在全网传疯了，一条推文就冲上了 6000 多万曝光。\n本期视频我会带你手把手从 0 到 1 把这个Skill 装好，然后一起跑一个成品效果出来。"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 76962,
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
    "points": 76552,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "10月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "帅气逼人的B友",
    "platform": "bilibili",
    "points": 74460,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "已经改了"
  },
  {
    "id": "bvid:BV1c8NFzhEMi",
    "domain": "AI",
    "title": "一个CLI干掉所有MCP工具，省99%的token mcp2cli",
    "url": "http://www.bilibili.com/video/av116204349953548",
    "source": "探索未至之境",
    "platform": "bilibili",
    "points": 63083,
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
    "points": 56354,
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
    "points": 49631,
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
    "points": 47762,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 40895,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1gwcAzkEhw",
    "domain": "AI",
    "title": "Claude Code Agent Teams上手指南+项目实测",
    "url": "http://www.bilibili.com/video/av116037064331269",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 35999,
    "published_at": "2026-02-08T23:30:00+00:00",
    "summary": "用Claude Code干复杂任务总碰到三个问题：\n\n上下文越来越长开始遗忘、任务只能串行效率低、单Agent视角单一容易漏检。\n\nClaude官方发布的Agent Teams功能正好解决这些痛点\n\n一个Team Lead拆任务，多个Teammate并行执行，还能互相通信协调。\n\n本期视频从核心概念、使用场景、底层架构到真实项目实战，带你完整搞懂Agent Teams的正确打开方式。"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34593,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV18KJX6mEiH",
    "domain": "AI",
    "title": "太炸裂了！Claude Code 3.0彻底杀疯了！",
    "url": "http://www.bilibili.com/video/av117450007911196",
    "source": "烟神殿殿主",
    "platform": "bilibili",
    "points": 30021,
    "published_at": "2026-10-16T10:04:56+00:00",
    "summary": "原视频链接：https://www.youtube.com/watch?v=8nh1dcH4uJU\n本视频为AI技术搬运翻译，使用AI智能移除原视频广告营销内容，旨在降低信息差，帮助大家了解海外最新AI动态。\n翻译：烟神殿API,模型gemini-3.8-flash\n配音：使用的时FishTTS官方接口配音"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29869,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 26871,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1B97868EZK",
    "domain": "AI",
    "title": "Claude Code全流程开发实战丨MCP实战、Skills+Agent多工具协作、AI编程、自动化工作流、私有化部署、转行AI岗",
    "url": "http://www.bilibili.com/video/av116810192131401",
    "source": "博学谷",
    "platform": "bilibili",
    "points": 25952,
    "published_at": "2026-06-25T10:11:09+00:00",
    "summary": "视频配套资源领取方式戳：https://www.bilibili.com/opus/1217780115004456969\n或关注【博学谷】公综号回复关键词领取：260625\n学完本课程，你将能够独立完成AI Agent 研发与落地：深度掌握 Claude Code 辅助编程、Skill 技能包编排与 MCP 协议集成打通私有系统连接的“桥梁”，并能学会私有化部署。最终凭借“AI Coding 重"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 24704,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 23598,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1fiiXBNEPM",
    "domain": "AI",
    "title": "AI时代下的编程选择, C#极致简单上手",
    "url": "http://www.bilibili.com/video/av115858051438295",
    "source": "世纪文明",
    "platform": "bilibili",
    "points": 23006,
    "published_at": "2026-01-08T06:30:07+00:00",
    "summary": "这期视频主要面向在AI时代下还在焦虑，或考虑学习编程的朋友们。\n内含实际演示，C#现在的上手有多么的简单和便捷！"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22825,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 17913,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15396,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "hn:49970667",
    "domain": "AI 算力 / 半导体",
    "title": "Opus 5.5 agents discover two room-temperature magnetic semiconductor candidates",
    "url": "https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors",
    "source": "outlier99",
    "platform": "hackernews",
    "points": 495,
    "published_at": "2026-10-05T21:00:21+00:00",
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
    "id": "hn:50219700",
    "domain": "AI 算力 / 半导体",
    "title": "GPU-unlock: FP/BF16 instruction issue rate on Nvidia 3000's cards",
    "url": "https://github.com/Zagitta/gpu-unlock",
    "source": "fragebogen",
    "platform": "hackernews",
    "points": 235,
    "published_at": "2026-10-24T09:58:27+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/arm-comments-on-jury-decision-in-qualcomm-trial/",
    "domain": "AI 算力 / 半导体",
    "title": "Arm Comments on Jury Decision in Qualcomm Trial",
    "url": "https://www.eetimes.com/arm-comments-on-jury-decision-in-qualcomm-trial/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T00:00:00+00:00",
    "summary": "Arm's Ami Badani cites the $2 nominal damages award as validation, while chip design experts point to open architectures such as RISC-V as the long-term alternative for AI workload flexibility. The po"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/save-up-to-usd800-on-acers-ultra-slim-rtx-5070-ti-gaming-laptop-pay-usd2225-for-the-16gb-ram-model-or-upgrade-to-32gb-for-usd2400",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to $800 on Acer’s ultra-slim RTX 5070 Ti gaming laptop — pay $2225 for the 16GB RAM model or upgrade to 32GB for $2400",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/save-up-to-usd800-on-acers-ultra-slim-rtx-5070-ti-gaming-laptop-pay-usd2225-for-the-16gb-ram-model-or-upgrade-to-32gb-for-usd2400",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T13:58:40+00:00",
    "summary": "The Acer Predator Helios Neo 16S AI combines a 240 Hz QHD+ OLED display with Intel’s 24-core Core Ultra 9 processor and Nvidia RTX 5070 Ti graphics, and Best Buy is offering discounts of up to $800."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/maps/proton-hosts-flock-map-revealing-over-300-000-cameras-defying-cease-and-desist-threats-against-creator-privacy-focused-company-hosts-site-on-swiss-servers-says-users-have-the-right-to-know-whos-recording-them",
    "domain": "AI 算力 / 半导体",
    "title": "Proton hosts Flock map revealing over 300,000 cameras, defying cease-and-desist threats against creator",
    "url": "https://www.tomshardware.com/software/maps/proton-hosts-flock-map-revealing-over-300-000-cameras-defying-cease-and-desist-threats-against-creator-privacy-focused-company-hosts-site-on-swiss-servers-says-users-have-the-right-to-know-whos-recording-them",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T13:42:41+00:00",
    "summary": "Privacy-focused firm Proton AG just decided to host the Flock camera map that a security researcher published last month."
  },
  {
    "id": "rss:https://www.tomshardware.com/speakers/edifier-hecate-g2000-pro-review",
    "domain": "AI 算力 / 半导体",
    "title": "Edifier Hecate G2000 Pro Review: Clear and Colorful",
    "url": "https://www.tomshardware.com/speakers/edifier-hecate-g2000-pro-review",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T13:00:00+00:00",
    "summary": "The Edifier Hecate G2000 Pro speakers offer a uniquely designed RGB experience, all within a set of above-average 2.0 Stereo PC gaming speakers. They deliver an audio experience far surpassing their l"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-october-24-2026-tp-links-fcc-saga-file-semantic-ssds-and-unlocking-better-gaming-performance-from-rtx-spark",
    "domain": "AI 算力 / 半导体",
    "title": "This week on Tom's Hardware Premium: October 24, 2026",
    "url": "https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-october-24-2026-tp-links-fcc-saga-file-semantic-ssds-and-unlocking-better-gaming-performance-from-rtx-spark",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T12:25:00+00:00",
    "summary": "We give you a glimpse at some of the biggest stories we've published over on Tom's Hardware Premium this week, including reports on TP-Link's struggles over sales of its Wi-Fi 8 routers, FADU's new SS"
  },
  {
    "id": "rss:https://www.tomshardware.com/virtual-reality/valve-adds-cd-rom-drive-support-to-steam-frame-kernel-took-less-than-ten-minutes-update-comes-one-day-after-user-requests-for-capability-in-the-steam-community-forum",
    "domain": "AI 算力 / 半导体",
    "title": "Valve adds CD-ROM drive support to Steam Frame kernel, took less than ten minutes",
    "url": "https://www.tomshardware.com/virtual-reality/valve-adds-cd-rom-drive-support-to-steam-frame-kernel-took-less-than-ten-minutes-update-comes-one-day-after-user-requests-for-capability-in-the-steam-community-forum",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T12:06:43+00:00",
    "summary": "Valve practically just flipped a switch to give gamers the ability to read optical drives directly from the Steam Frame."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/use-your-3d-printer-to-customize-this-new-stage-tour-guitar-controller-drakongs-infinakore-fender-telecaster-peripheral-is-a-modders-dream",
    "domain": "AI 算力 / 半导体",
    "title": "Use your 3D printer to customize this new Stage Tour guitar PC controller",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/use-your-3d-printer-to-customize-this-new-stage-tour-guitar-controller-drakongs-infinakore-fender-telecaster-peripheral-is-a-modders-dream",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T12:00:00+00:00",
    "summary": "A new customizable rhythm game controller that's compatible with the new Stage Tour and pre-existing Guitar Hero and Rock Band games. The InfinaKore Fender Telecaster Edition controller lets you creat"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/texas-has-suspended-17-data-center-construction-permits-and-shut-down-automated-portal-used-to-approve-them-site-was-left-running-for-a-month-after-greg-abbott-called-for-a-pause-on-approvals",
    "domain": "AI 算力 / 半导体",
    "title": "Texas has suspended 17 data center construction permits and shut down automated portal that rubber-stamped projects",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/texas-has-suspended-17-data-center-construction-permits-and-shut-down-automated-portal-used-to-approve-them-site-was-left-running-for-a-month-after-greg-abbott-called-for-a-pause-on-approvals",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T11:35:00+00:00",
    "summary": "Texas has suspended 17 data center construction permits and shut down the automated portal used to approve them"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/leaked-video-exposes-how-chinese-factories-are-stripping-rtx-5090s-to-fuel-ai-custom-partner-cards-to-nvidia-founders-editions-on-the-chopping-block",
    "domain": "AI 算力 / 半导体",
    "title": "Leaked video exposes how industrial-scale Chinese factories are dismantling RTX 5090s by the thousands to fuel AI servers",
    "url": "https://www.tomshardware.com/pc-components/gpus/leaked-video-exposes-how-chinese-factories-are-stripping-rtx-5090s-to-fuel-ai-custom-partner-cards-to-nvidia-founders-editions-on-the-chopping-block",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T11:15:00+00:00",
    "summary": "Wondering why RTX 5090s are so hard to find? Leaked footage shows thousands of consumer GPUs, including Founders Editions, being torn apart for AI servers."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/russia-deploys-3d-printed-cruise-missiles-in-ukraine-can-hit-500mph-with-a-745-mile-range-fears-high-that-cheap-filin-missile-will-be-used-for-missile-spam-tactics",
    "domain": "AI 算力 / 半导体",
    "title": "Russia deploys 3D-printed cruise missiles with US electronics in Ukraine, can hit 500mph with a 745-mile range",
    "url": "https://www.tomshardware.com/3d-printing/russia-deploys-3d-printed-cruise-missiles-in-ukraine-can-hit-500mph-with-a-745-mile-range-fears-high-that-cheap-filin-missile-will-be-used-for-missile-spam-tactics",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T10:25:00+00:00",
    "summary": "The Filin missile, which was deployed between late September and early October of this year, reportedly used 3D-printed and commercial parts to save on cost."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/exhaustion-with-tech-market-prompts-youtuber-to-remake-their-first-pc-1996-build-fueled-by-nostalgia-and-ai-weariness",
    "domain": "AI 算力 / 半导体",
    "title": "YouTuber escapes the modern AI tech market by recreating his 1996 PC",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/exhaustion-with-tech-market-prompts-youtuber-to-remake-their-first-pc-1996-build-fueled-by-nostalgia-and-ai-weariness",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T10:00:00+00:00",
    "summary": "Exhaustion with tech market prompt Youtuber to remake their first PC — 1996 build fueled by nostalgia and AI weariness"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/rare-archival-footage-tours-the-compusa-nyc-store-in-november-2000-soak-up-some-y2k-pentium-iii-athlon-powerpc-windows-me-chunky-laptop-and-bulging-crt-nostalgia-in-glorious-360p",
    "domain": "AI 算力 / 半导体",
    "title": "Rare archival footage tours the CompUSA NYC store in November 2000",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/rare-archival-footage-tours-the-compusa-nyc-store-in-november-2000-soak-up-some-y2k-pentium-iii-athlon-powerpc-windows-me-chunky-laptop-and-bulging-crt-nostalgia-in-glorious-360p",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T09:40:00+00:00",
    "summary": "Fascinating footage captured inside a busy CompUSA retail store in Y2K lets you relive the PC era when translucent acrylic Presarios and iMacs roamed the Earth."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/razer-basilisk-v4-pro-review",
    "domain": "AI 算力 / 半导体",
    "title": "Razer Basilisk V4 Pro Review: Tried and true and now with AI",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/razer-basilisk-v4-pro-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T16:00:00+00:00",
    "summary": "Razer's Basilisk V4 Pro gaming mouse features an ergonomic shape, a lighter weight, and a couple of extra buttons, plus Razer's Focus Pro 50K optical sensor."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/microns-next-generation-3d-nand-to-double-bit-density-with-over-400-layers-offering-extreme-performance-g11-3d-nand-promises-42-gb-mm2-and-5-400-mt-s-interface-speed",
    "domain": "AI 算力 / 半导体",
    "title": "Micron's next-generation 3D NAND to double bit density with over 400 layers, offering extreme performance",
    "url": "https://www.tomshardware.com/pc-components/ssds/microns-next-generation-3d-nand-to-double-bit-density-with-over-400-layers-offering-extreme-performance-g11-3d-nand-promises-42-gb-mm2-and-5-400-mt-s-interface-speed",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T15:32:05+00:00",
    "summary": "Micron's G11 3D NAND promises 42 Gb/mm2 and 5,400 MT/s interface speed, enabling SSDs with extreme capacity and performance."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/solidigm-confirms-plans-to-build-a-fab-in-the-us-abandons-ipo-plans-unfavorable-stock-market-conditions-and-semiconductor-share-price-trends-reasons-given",
    "domain": "AI 算力 / 半导体",
    "title": "Solidigm confirms plans to build a fab in the US, abandons IPO plans",
    "url": "https://www.tomshardware.com/pc-components/ssds/solidigm-confirms-plans-to-build-a-fab-in-the-us-abandons-ipo-plans-unfavorable-stock-market-conditions-and-semiconductor-share-price-trends-reasons-given",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T15:21:16+00:00",
    "summary": "SK hynix abandons IPO plans for Solidigm, confirms plans to build a Solidigm 3D NAND fab in the U.S."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/gigabyte-z890m-aorus-elite-wifi7-motherboard-review",
    "domain": "AI 算力 / 半导体",
    "title": "Gigabyte Z890M Aorus Elite WiFi7 Motherboard Review: Icy-white SFF board offers full-size features for Intel",
    "url": "https://www.tomshardware.com/pc-components/motherboards/gigabyte-z890m-aorus-elite-wifi7-motherboard-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T15:00:00+00:00",
    "summary": "The $209 Gigabyte Z890M Aorus Elite Wifi 7 Ice is one of the better-looking Micro ATX boards, with an icy-white aesthetic and full heatsink coverage that give it a premium vibe for white-themed Intel "
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/oled-on-a-budget-save-usd50-now-on-the-acer-predator-xb27ou-at-best-buy-only-usd329-for-a-stunning-qd-oled-gaming-monitor-with-a-superfast-240hz-refresh-rate",
    "domain": "AI 算力 / 半导体",
    "title": "OLED on a budget, save $50 now on the Acer Predator XB27OU at Best Buy",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/oled-on-a-budget-save-usd50-now-on-the-acer-predator-xb27ou-at-best-buy-only-usd329-for-a-stunning-qd-oled-gaming-monitor-with-a-superfast-240hz-refresh-rate",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T14:00:00+00:00",
    "summary": "Upgrade your gaming monitor with this fantastic $329 deal on the Acer XB27OU 27-inch QD-OLED gaming monitor at Best Buy. Save $50 instantly."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/amazon-bows-to-local-backlash-over-ai-data-centers-scraps-plans-to-build-four-new-facilities-in-northern-virginia-site-to-be-repurposed-for-mixed-use-and-residential-development",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon bows to local backlash over AI data centers, scraps plans to build four new facilities in Northern Virginia",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/amazon-bows-to-local-backlash-over-ai-data-centers-scraps-plans-to-build-four-new-facilities-in-northern-virginia-site-to-be-repurposed-for-mixed-use-and-residential-development",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T13:36:50+00:00",
    "summary": "Amazon has ditched its plans to build four new data centers in Loudoun County, Northern Virginia, following an outcry from local residents and officials. The land will now be repurposed for mixed and "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/china-can-make-advanced-chips-without-euv-but-the-bill-keeps-growing-duv-multiple-patterning-means-bigger-dies-lower-yields-and-longer-manufacturing-times",
    "domain": "AI 算力 / 半导体",
    "title": "China can make advanced chips without EUV, but the bill keeps growing",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/china-can-make-advanced-chips-without-euv-but-the-bill-keeps-growing-duv-multiple-patterning-means-bigger-dies-lower-yields-and-longer-manufacturing-times",
    "source": "Chris Stokel-Walker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T13:30:00+00:00",
    "summary": "China has stretched older DUV lithography far further than expected, using multiple patterning to approach 5nm-class without EUV. But experts say the trade-offs in cost, yield, and die size mean furth"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/bambu-lab-teases-its-mysterious-h3c-tool-changer-3d-printer-features-nine-tools-and-a-drop-down-rack-slated-for-november-3-launch",
    "domain": "AI 算力 / 半导体",
    "title": "Bambu Lab teases its mysterious H3C tool changer 3D printer",
    "url": "https://www.tomshardware.com/3d-printing/bambu-lab-teases-its-mysterious-h3c-tool-changer-3d-printer-features-nine-tools-and-a-drop-down-rack-slated-for-november-3-launch",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T13:00:00+00:00",
    "summary": "Bambu Lab’s long-awaited tool changer H3C launches Nov. 3, 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/illegal-nvidia-blackwell-ultra-b300-gpus-found-inside-state-owned-china-telecoms-network-nvidia-says-chip-smuggling-a-drop-in-the-bucket-insists-smuggling-remains-a-nonfactor",
    "domain": "AI 算力 / 半导体",
    "title": "Illegal Nvidia Blackwell Ultra B300 GPUs found inside state-owned China Telecom's network",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/illegal-nvidia-blackwell-ultra-b300-gpus-found-inside-state-owned-china-telecoms-network-nvidia-says-chip-smuggling-a-drop-in-the-bucket-insists-smuggling-remains-a-nonfactor",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T12:26:23+00:00",
    "summary": "A security firm has been able to identify 32 Nvidia Blackwell Ultra B300 AI chips running inside a China Telecom network, but it's unclear where the export-barred components are physically located."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/fcc-bans-first-two-devices-from-the-us-under-new-chip-level-rule-huawei-subsidiary-chip-boasts-face-detection-algorithm",
    "domain": "AI 算力 / 半导体",
    "title": "FCC issues first bans under new chip-level rule",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/fcc-bans-first-two-devices-from-the-us-under-new-chip-level-rule-huawei-subsidiary-chip-boasts-face-detection-algorithm",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T12:15:00+00:00",
    "summary": "FCC bans a dashcam and wireless video transmitter produced by HiSilicon, a subsidiary of Huawei for containing an AI chip that advertises face detection algorithms."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/deepseeks-latest-ai-model-is-smarter-than-ever-but-its-low-running-costs-come-at-a-price-open-weight-model-is-fit-for-agentic-workloads-but-is-more-prone-to-hallucination-than-proprietary-competitors",
    "domain": "AI 算力 / 半导体",
    "title": "Deepseek's latest AI model is smarter than ever, but its low running costs come at a price",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/deepseeks-latest-ai-model-is-smarter-than-ever-but-its-low-running-costs-come-at-a-price-open-weight-model-is-fit-for-agentic-workloads-but-is-more-prone-to-hallucination-than-proprietary-competitors",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T12:00:00+00:00",
    "summary": "Deepseek 4.1 Flash 1017 drives cost-per-task further down still — open-weight model is fit for agentic workloads and exceedingly cheap to run"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/uk-proposes-14-year-prison-sentences-for-undersea-cable-saboteurs-amid-russian-trawler-threats-government-responds-to-growing-threats-with-new-criminal-offences-and-emergency-powers-to-shut-down-services",
    "domain": "AI 算力 / 半导体",
    "title": "UK proposes 14-year prison sentences for undersea cable saboteurs amid Russian trawler threats",
    "url": "https://www.tomshardware.com/tech-industry/uk-proposes-14-year-prison-sentences-for-undersea-cable-saboteurs-amid-russian-trawler-threats-government-responds-to-growing-threats-with-new-criminal-offences-and-emergency-powers-to-shut-down-services",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T11:45:00+00:00",
    "summary": "The UK government has outlined plans for new powers and criminal offenses to help protect undersea cables in UK waters amid fears of Russian interference."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/us-banks-scramble-to-restrict-ai-agent-activity-agents-detected-accessing-customer-accounts-or-even-attempting-to-make-transactions-in-breach-of-policy",
    "domain": "AI 算力 / 半导体",
    "title": "US banks scramble to restrict AI agent activity",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/us-banks-scramble-to-restrict-ai-agent-activity-agents-detected-accessing-customer-accounts-or-even-attempting-to-make-transactions-in-breach-of-policy",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T11:30:00+00:00",
    "summary": "Several U.S. banks are blocking AI agents from making transactions on their platforms. They fear that those agents could go rogue and there's no way to tell if the moves they make are legitimate or no"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/devastated-forum-user-who-accidentally-broke-the-php-news-embargo-comes-clean-user-says-they-were-unaware-of-disclosure-restrictions-move-clearly-backfired-in-a-pretty-wild-fashion",
    "domain": "AI 算力 / 半导体",
    "title": "Consultant comes clean for sparking worldwide panic by accidentally breaking the PHP vulnerability embargo",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/devastated-forum-user-who-accidentally-broke-the-php-news-embargo-comes-clean-user-says-they-were-unaware-of-disclosure-restrictions-move-clearly-backfired-in-a-pretty-wild-fashion",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T11:15:00+00:00",
    "summary": "The user said that they only wanted to alert others about the importance of the upcoming CVE releases and weren't told about the embargo."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/cybercartel-hacking-gang-used-claude-and-grok-ai-agents-to-automate-attacks-on-latin-american-institutions-passwords-and-details-stolen-from-over-400-institutions-including-banks-and-payment-apps",
    "domain": "AI 算力 / 半导体",
    "title": "Claude and Grok among AI agents used to automate attacks on Latin American institutions",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/cybercartel-hacking-gang-used-claude-and-grok-ai-agents-to-automate-attacks-on-latin-american-institutions-passwords-and-details-stolen-from-over-400-institutions-including-banks-and-payment-apps",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T11:00:00+00:00",
    "summary": "Claude and Grok are among the AI agents that are being used to automate attacks on Latin American institutions, including banks and payment apps, by a group calling themselves CyberCartel."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/microsoft-says-china-aligned-hackers-used-ai-agents-in-connectwise-supply-chain-attack-agents-attempted-sign-ins-at-more-than-2-250-microsoft-365-tenants-with-some-of-the-groups-attacks-reaching-privileged-access-in-under-three-hours",
    "domain": "AI 算力 / 半导体",
    "title": "China-aligned hackers deploy AI agents in massive ConnectWise supply chain attack",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/microsoft-says-china-aligned-hackers-used-ai-agents-in-connectwise-supply-chain-attack-agents-attempted-sign-ins-at-more-than-2-250-microsoft-365-tenants-with-some-of-the-groups-attacks-reaching-privileged-access-in-under-three-hours",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T10:30:00+00:00",
    "summary": "Microsoft says China-aligned Storm-0940 used the ARTEX AI agent framework in the ConnectWise Cloud Backup supply chain attack."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd450-on-this-4k-gaming-pc-with-an-rtx-5070-ti-and-9800x3d-now-usd2-549-99-liquid-cooled-abs-stratos-ii-ruby-rig-comes-with-32gb-ddr5-and-a-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save $450 on this 4K gaming PC with an RTX 5070 Ti and 9800X3D, now $2,549.99",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd450-on-this-4k-gaming-pc-with-an-rtx-5070-ti-and-9800x3d-now-usd2-549-99-liquid-cooled-abs-stratos-ii-ruby-rig-comes-with-32gb-ddr5-and-a-2tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T10:10:35+00:00",
    "summary": "You can save $450 on this 4K-capable gaming machine from Newegg's ABS brand, featuring the powerful RTX 5070 Ti, AMD Ryzen 7 9800X3D, 32GB DDR5, and a 2TB SSD for $2,549.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/wolves-roam-into-finnish-villages-after-google-destroys-1-300-acres-of-forest-for-ai-data-centers-forest-where-wolf-packs-used-to-live-are-now-an-expanse-of-mud",
    "domain": "AI 算力 / 半导体",
    "title": "Wolves roam into Finnish villages after Google destroys 1,300 acres of forest for AI data centers",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/wolves-roam-into-finnish-villages-after-google-destroys-1-300-acres-of-forest-for-ai-data-centers-forest-where-wolf-packs-used-to-live-are-now-an-expanse-of-mud",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T10:00:00+00:00",
    "summary": "Wolves, who used to live in the forests recently cleared for Google data center development, are now roaming into Finnish villages nearby."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/extremely-rare-and-previously-undocumented-pokemon-red-prototype-cartridge-surfaces-at-auction-starting-at-usd25-000-nintendo-game-boy-dev-board-from-1998-features-32kb-of-readable-memory-fully-identical-to-the-final-game-release",
    "domain": "AI 算力 / 半导体",
    "title": "Extremely rare and 'previously undocumented' Pokémon Red prototype cartridge surfaces at auction, starting at $25,000",
    "url": "https://www.tomshardware.com/video-games/nintendo/extremely-rare-and-previously-undocumented-pokemon-red-prototype-cartridge-surfaces-at-auction-starting-at-usd25-000-nintendo-game-boy-dev-board-from-1998-features-32kb-of-readable-memory-fully-identical-to-the-final-game-release",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T09:40:00+00:00",
    "summary": "A rare prototype cartridge of Pokémon Red for the Nintendo Game Boy is on sale, with one $25,000 bid so far."
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
    "id": "rss:https://www.eetimes.com/two-dollars-and-a-test-suite/",
    "domain": "AI 算力 / 半导体",
    "title": "Two Dollars and a Test Suite",
    "url": "https://www.eetimes.com/two-dollars-and-a-test-suite/",
    "source": "Moshe Zalcberg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T08:03:27+00:00",
    "summary": "The $2 damages award grabbed headlines, but the Arm-Qualcomm verdict’s bigger implication concerns who controls the compliance tests that custom chips must pass before shipping. The post Two Dollars a"
  },
  {
    "id": "rss:https://www.eetimes.com/from-cloud-ai-to-edge-ai-how-biwin-enables-the-next-generation-of-storage-and-memory-solutions/",
    "domain": "AI 算力 / 半导体",
    "title": "From Cloud AI to Edge AI: How BIWIN Enables the Next Generation of Storage and Memory Solutions",
    "url": "https://www.eetimes.com/from-cloud-ai-to-edge-ai-how-biwin-enables-the-next-generation-of-storage-and-memory-solutions/",
    "source": "EE Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T18:24:39+00:00",
    "summary": "See how BIWIN’s SSD, embedded storage, and memory portfolio supports faster, efficient AI from cloud data centers to edge wearables. The post From Cloud AI to Edge AI: How BIWIN Enables the Next Gener"
  },
  {
    "id": "rss:https://www.eetimes.com/deepx-building-open-software-ecosystem-to-scale-physical-ai-beyond-the-data-center/",
    "domain": "AI 算力 / 半导体",
    "title": "Deepx Building Open Software Ecosystem to Scale Physical AI Beyond the Data Center",
    "url": "https://www.eetimes.com/deepx-building-open-software-ecosystem-to-scale-physical-ai-beyond-the-data-center/",
    "source": "Stephen Las Marias",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T18:14:49+00:00",
    "summary": "Deepx is combining low-power AI accelerators and portable software with industry partnerships to bring physical AI into production. The post Deepx Building Open Software Ecosystem to Scale Physical AI"
  },
  {
    "id": "rss:https://www.eetimes.com/how-goodram-validates-dram-and-ssd-reliability-in-europe/",
    "domain": "AI 算力 / 半导体",
    "title": "How Goodram Validates DRAM and SSD Reliability in Europe",
    "url": "https://www.eetimes.com/how-goodram-validates-dram-and-ssd-reliability-in-europe/",
    "source": "GOODRAM",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T13:00:00+00:00",
    "summary": "Explore Goodram’s European approach to DRAM and SSD testing, from burn-in to platform validation, for reliable industrial and embedded systems. The post How Goodram Validates DRAM and SSD Reliability "
  },
  {
    "id": "rss:https://www.eetimes.com/everspin-expands-mram-push-into-ai-servers-data-centers-satellite-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Everspin Expands MRAM Push into AI Servers, Data Centers, Satellite Systems",
    "url": "https://www.eetimes.com/everspin-expands-mram-push-into-ai-servers-data-centers-satellite-systems/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-22T09:58:39+00:00",
    "summary": "In an exclusive interview, Everspin CEO Sanjeev Aggarwal discusses MRAM opportunities amid NOR flash supply constraints. The post Everspin Expands MRAM Push into AI Servers, Data Centers, Satellite Sy"
  },
  {
    "id": "rss:https://www.eetimes.com/when-gps-isnt-enough-building-a-second-layer-of-positioning/",
    "domain": "AI 算力 / 半导体",
    "title": "When GPS Isn’t Enough: Building a Second Layer of Positioning",
    "url": "https://www.eetimes.com/when-gps-isnt-enough-building-a-second-layer-of-positioning/",
    "source": "Steve Caliguri",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T19:00:00+00:00",
    "summary": "GPS jamming is rising. Learn how 4G, 5G, and NTN positioning give mission-critical devices a trusted fallback when GNSS fails. The post When GPS Isn&#8217;t Enough: Building a Second Layer of Position"
  },
  {
    "id": "rss:https://www.eetimes.com/indias-osat-buildout-puts-semiconductor-testing-in-focus/",
    "domain": "AI 算力 / 半导体",
    "title": "India’s OSAT Buildout Puts Semiconductor Testing in Focus",
    "url": "https://www.eetimes.com/indias-osat-buildout-puts-semiconductor-testing-in-focus/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T13:39:13+00:00",
    "summary": "NI said Kaynes Semicon has selected its semiconductor test systems, while other Indian OSATs continue to evaluate equipment as manufacturers prepare for production. The post India’s OSAT Buildout Puts"
  },
  {
    "id": "rss:https://www.eetimes.com/why-chip-design-ai-benchmarks-must-go-beyond-functional-correctness/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Chip Design AI Benchmarks Must Go Beyond Functional Correctness",
    "url": "https://www.eetimes.com/why-chip-design-ai-benchmarks-must-go-beyond-functional-correctness/",
    "source": "Surya Gunukula, Jerry Yicheng Wang, Kevin Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T13:00:00+00:00",
    "summary": "Demand for custom silicon is rising as physical AI, data centers, automotive systems, and edge devices require architectures optimized for specific workloads, memory bandwidth, latency, and energy eff"
  },
  {
    "id": "rss:https://www.eetimes.com/edge-ai-mcu-features-multimodal-compute-tiered-memory/",
    "domain": "AI 算力 / 半导体",
    "title": "Edge AI MCU Features Multimodal Compute, Tiered Memory",
    "url": "https://www.eetimes.com/edge-ai-mcu-features-multimodal-compute-tiered-memory/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T07:30:00+00:00",
    "summary": "A new MCU combines AI-native acceleration with integrated high-bandwidth DRAM scalable to hundreds of megabytes. The post Edge AI MCU Features Multimodal Compute, Tiered Memory appeared first on EE Ti"
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
    "points": 1466,
    "published_at": "2026-10-13T16:03:16+00:00",
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
    "id": "hn:50122431",
    "domain": "大厂 AI 动态",
    "title": "Llama.cpp on a jailbroken PS5: run any GGUF model natively on the console",
    "url": "https://github.com/cobanov/PS5LM",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 375,
    "published_at": "2026-10-16T18:32:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50118688",
    "domain": "大厂 AI 动态",
    "title": "Show HN: Gemini 4 Argon plays StarCraft",
    "url": "https://starskirmish.com/bench/v0-2/",
    "source": "__cayenne__",
    "platform": "hackernews",
    "points": 254,
    "published_at": "2026-10-16T14:18:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:50074869",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon for Robotics",
    "url": "https://developers.googleblog.com/gemini-4-argon-for-robotics/",
    "source": "xnx",
    "platform": "hackernews",
    "points": 234,
    "published_at": "2026-10-13T16:55:47+00:00",
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
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1018205/blue-planet-iii-authentic-organic-ai",
    "domain": "大厂 AI 动态",
    "title": "Blue Planet III is keeping the rough edges in the age of AI",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1018205/blue-planet-iii-authentic-organic-ai",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T21:29:12+00:00",
    "summary": "BBC's Blue Planet III is looking to prove its authenticity by leaving in the less-than-perfect shots. Previous incarnations of the nature series were defined by their gorgeous, crystal-clear footage t"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1018187/pennsylvania-ai-deceptive-advertising-act",
    "domain": "大厂 AI 动态",
    "title": "Pennsylvania will require labels on AI-generated ads",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1018187/pennsylvania-ai-deceptive-advertising-act",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T18:32:21+00:00",
    "summary": "On Thursday, Pennsylvania Governor Josh Shapiro signed the Artificial Intelligence Deceptive Advertising Act into law, requiring disclosures on AI-generated ads. The law requires any ad - whether it's"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1017460/fielded-some-kind-of-animal-interview",
    "domain": "大厂 AI 动态",
    "title": "Fielded is obsessed with scammers and unhinged Japanese cyberpunk",
    "url": "https://www.theverge.com/entertainment/1017460/fielded-some-kind-of-animal-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T15:00:00+00:00",
    "summary": "Lindsay Powell, who releases records under the name Fielded, has spent most of her career subverting expectations and genre conventions. According to their Bandcamp page, Fielded started as an experim"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1017768/lg-c6-oled-tv-early-black-friday-2026-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "LG’s brilliant C6 OLED TV is already $400 off ahead of Black Friday",
    "url": "https://www.theverge.com/gadgets/1017768/lg-c6-oled-tv-early-black-friday-2026-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T15:00:00+00:00",
    "summary": "Black Friday is still over a month away, but if you&#8217;re hoping to upgrade your TV, you don’t need to wait until November. LG has already kicked off its early Black Friday sale, letting you save o"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1018169/what-to-expect-apple-pro-and-tell-event-touchscreen-macbook-pro",
    "domain": "大厂 AI 动态",
    "title": "What to expect from Apple’s ‘Pro and tell’ event",
    "url": "https://www.theverge.com/tech/1018169/what-to-expect-apple-pro-and-tell-event-touchscreen-macbook-pro",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T14:15:00+00:00",
    "summary": "It feels like Apple's Welcome Home event just happened. And the iPhone Duo announcement isn't all that far in our rearview mirror, either. Yet, the company is back with another launch, focused on the "
  },
  {
    "id": "rss:https://www.theverge.com/report/1018131/apple-macbook-touchscreen-stylus-pencil-lenovo-laptop-analysis",
    "domain": "大厂 AI 动态",
    "title": "I hope Apple’s touchscreen MacBook takes some lessons from this Lenovo laptop",
    "url": "https://www.theverge.com/report/1018131/apple-macbook-touchscreen-stylus-pencil-lenovo-laptop-analysis",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T14:00:00+00:00",
    "summary": "It looks like the long-rumored touchscreen MacBook might actually get announced next week, and after using the Lenovo Yoga 9n for our testing of Nvidia's RTX Spark platform, it got me thinking: this i"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1017888/possible-love-lee-chang-dong-director-interview",
    "domain": "大厂 AI 动态",
    "title": "Lee Chang Dong ponders the ethics of the camera",
    "url": "https://www.theverge.com/entertainment/1017888/possible-love-lee-chang-dong-director-interview",
    "source": "May Jeong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T12:30:00+00:00",
    "summary": "Lee Chang Dong's seventh feature film, Possible Love, is inspired by true events from 2009, when a Korean conglomerate fired a third of its staff - 2,600 employees - after which many died by suicide. "
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1017740/wildwood-stop-motion-interview-laika",
    "domain": "大厂 AI 动态",
    "title": "Laika has spent 20 years building up to Wildwood",
    "url": "https://www.theverge.com/entertainment/1017740/wildwood-stop-motion-interview-laika",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T12:00:00+00:00",
    "summary": "Across several decades in Hollywood, Caleb Deschanel has seen a lot. He served as cinematographer on films like The Passion of the Christ and The Patriot, worked on sequences in The Godfather and Tita"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1018121/cod-4-claude-duet-wildwood-installer",
    "domain": "大厂 AI 动态",
    "title": "It’s time to find a new browser",
    "url": "https://www.theverge.com/tech/1018121/cod-4-claude-duet-wildwood-installer",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T12:00:00+00:00",
    "summary": "Hi, friends! Welcome to Installer No. 149, your guide to the best and Verge-iest stuff in the world. (If you're new here, welcome, happy It Actually Feels Like Fall Now At Least In My Neighborhood), a"
  },
  {
    "id": "rss:https://www.theverge.com/news/1018037/xbox-chief-operating-officer-helen-chiang-departure",
    "domain": "大厂 AI 动态",
    "title": "Xbox’s first chief operating officer is out after just a few months",
    "url": "https://www.theverge.com/news/1018037/xbox-chief-operating-officer-helen-chiang-departure",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T21:39:26+00:00",
    "summary": "Xbox's first chief operating officer (COO) is leaving after the new role was created just a few months ago. Helen Chiang is leaving Microsoft today, according to an internal Xbox memo seen by The Verg"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/24/starlink-seems-to-be-working-normally-again-in-ukraine/",
    "domain": "大厂 AI 动态",
    "title": "Starlink seems to be working normally again in Ukraine",
    "url": "https://techcrunch.com/2026/10/24/starlink-seems-to-be-working-normally-again-in-ukraine/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T20:46:34+00:00",
    "summary": "Elon Musk reportedly ordered SpaceX to throttle Ukraine's Starlink access."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/24/will-ai-expose-the-rickety-infrastructure-of-the-internet/",
    "domain": "大厂 AI 动态",
    "title": "Will AI expose the rickety infrastructure of the internet?",
    "url": "https://techcrunch.com/2026/10/24/will-ai-expose-the-rickety-infrastructure-of-the-internet/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T20:15:33+00:00",
    "summary": "The moment you realize the internet is \"held together by glue and dreams.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/24/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/",
    "domain": "大厂 AI 动态",
    "title": "The AI graveyard: a running list of projects and startups that didn’t make it",
    "url": "https://techcrunch.com/2026/10/24/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T19:00:00+00:00",
    "summary": "From Apple's repeatedly delayed Siri AI to OpenAI's messy \"super app\" launch, here's a look at the AI projects that shut down or missed expectations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/24/instacart-reportedly-discussed-selling-itself-with-doordash-and-uber/",
    "domain": "大厂 AI 动态",
    "title": "Instacart reportedly discussed selling itself with DoorDash and Uber",
    "url": "https://techcrunch.com/2026/10/24/instacart-reportedly-discussed-selling-itself-with-doordash-and-uber/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T16:30:00+00:00",
    "summary": "Instacart might sell itself to a larger competitor."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/24/blocks-new-voice-model-sounds-eerily-human/",
    "domain": "大厂 AI 动态",
    "title": "Block’s new voice model sounds eerily human",
    "url": "https://techcrunch.com/2026/10/24/blocks-new-voice-model-sounds-eerily-human/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T16:00:00+00:00",
    "summary": "Block said that the voice model can run locally on a MacBook M4 Max"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/24/php-ocalypse-how-two-critical-web-bugs-almost-broke-the-internet/",
    "domain": "大厂 AI 动态",
    "title": "PHP-ocalypse: How two critical web bugs almost broke the internet",
    "url": "https://techcrunch.com/2026/10/24/php-ocalypse-how-two-critical-web-bugs-almost-broke-the-internet/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T15:30:00+00:00",
    "summary": "Two critical bugs in the PHP web programming language, used by the majority of the internet, threatened to upend the internet — and it's unlikely to be the last major software scare."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/24/these-clever-apps-show-off-the-iphone-duos-potential/",
    "domain": "大厂 AI 动态",
    "title": "These clever apps show off the iPhone Duo’s potential",
    "url": "https://techcrunch.com/2026/10/24/these-clever-apps-show-off-the-iphone-duos-potential/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T15:00:00+00:00",
    "summary": "From retro cassette players and virtual notebooks to flight trackers and even a digital toaster, developers are finding creative ways to take advantage of Apple's first foldable iPhone."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/24/forced-to-pick-groks-ai-model-chooses-republicans-openais-picks-democrats/",
    "domain": "大厂 AI 动态",
    "title": "Forced to pick, Grok’s AI model chooses Republicans. OpenAI’s picks Democrats.",
    "url": "https://techcrunch.com/2026/10/24/forced-to-pick-groks-ai-model-chooses-republicans-openais-picks-democrats/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T15:00:00+00:00",
    "summary": "A new study found Grok's AI overwhelmingly recommends Republican candidates while OpenAI's GPT favors Democrats, with the two AI models disagreeing in more than 90% of nearly 500 election races."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/24/the-boox-palma-2-pro-finally-got-me-to-stop-reading-on-my-phone/",
    "domain": "大厂 AI 动态",
    "title": "The Boox Palma 2 Pro finally got me to stop reading on my phone",
    "url": "https://techcrunch.com/2026/10/24/the-boox-palma-2-pro-finally-got-me-to-stop-reading-on-my-phone/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T14:15:00+00:00",
    "summary": "The $400 Boox Palma 2 Pro is a smartphone-sized e-reader designed for people who want to read books, articles, and documents on a small E Ink display."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/24/all-the-ai-agents-that-can-live-in-your-text-messages/",
    "domain": "大厂 AI 动态",
    "title": "Here are the top AI agents that can live in your text messages",
    "url": "https://techcrunch.com/2026/10/24/all-the-ai-agents-that-can-live-in-your-text-messages/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T14:00:00+00:00",
    "summary": "We created a list of the most notable AI agents that can live in your text messages, from general assistants to agents designed for families, travel, and work."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/23/startups-dont-need-to-go-viral-to-win-customers/",
    "domain": "大厂 AI 动态",
    "title": "Startups don’t need to go viral to win customers",
    "url": "https://techcrunch.com/2026/10/23/startups-dont-need-to-go-viral-to-win-customers/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T23:07:45+00:00",
    "summary": "At TechCrunch Disrupt last week, two founders and a VC discussed how to not just gain an early following but keep one."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/23/openai-says-it-will-no-longer-train-its-ai-models-on-the-live-internet-citing-significant-risks/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI says it will no longer train its AI models on the live internet, citing “significant risks”",
    "url": "https://techcrunch.com/2026/10/23/openai-says-it-will-no-longer-train-its-ai-models-on-the-live-internet-citing-significant-risks/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T23:05:49+00:00",
    "summary": "OpenAI will cut frontier models off from the internet weeks after one of its engineers said that solution wouldn't work."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/23/hottest-toy-for-christmas-nvidia-ceo-plays-with-adorable-microduck-robots-20000-sell/",
    "domain": "大厂 AI 动态",
    "title": "Hottest toy for Christmas? Nvidia CEO plays with adorable Microduck robots, 20,000 sell",
    "url": "https://techcrunch.com/2026/10/23/hottest-toy-for-christmas-nvidia-ceo-plays-with-adorable-microduck-robots-20000-sell/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T21:59:19+00:00",
    "summary": "The robots, stomping their little feet and making tiny R2-D2 noises, sat, fell down dead for a \"nap,\" and summersaulted on voice command."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/23/vcs-superhuman-mail-founder-share-red-flags-about-product-market-fit/",
    "domain": "大厂 AI 动态",
    "title": "VCs, Superhuman Mail founder share red flags about product-market fit",
    "url": "https://techcrunch.com/2026/10/23/vcs-superhuman-mail-founder-share-red-flags-about-product-market-fit/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T20:57:13+00:00",
    "summary": "Top investors from Iconiq and Sapphire Ventures, along with Rahul Vohra, the founder of Superhuman Mail, share the do's and don'ts for building hit products."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/23/techcrunch-founder-summit-2026-roundtables-go-deeper-on-the-challenges-founders-are-solving-right-now/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Founder Summit 2026 roundtables: Go deeper on the challenges founders are solving right now",
    "url": "https://techcrunch.com/2026/10/23/techcrunch-founder-summit-2026-roundtables-go-deeper-on-the-challenges-founders-are-solving-right-now/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T20:03:14+00:00",
    "summary": "TechCrunch Founder Summit 2026 is coming to SoWa Power Station in Boston on November 4, bringing founders, investors, and operators together for a full day of candid conversations, practical sessions,"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/23/carta-and-newview-partner-hoping-to-entice-more-startups-to-let-employees-sell-shares-early/",
    "domain": "大厂 AI 动态",
    "title": "Carta and NewView partner, hoping to entice more startups to let employees sell shares early",
    "url": "https://techcrunch.com/2026/10/23/carta-and-newview-partner-hoping-to-entice-more-startups-to-let-employees-sell-shares-early/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T19:25:13+00:00",
    "summary": "A new program wants to encourage more startups to allow workers to cash out early by making it easier to transact tender offers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/23/from-toast-to-bessemer-who-founders-will-hear-from-at-techcrunch-founder-summit-2026/",
    "domain": "大厂 AI 动态",
    "title": "From Toast to Bessemer: Who founders will hear from at TechCrunch Founder Summit 2026",
    "url": "https://techcrunch.com/2026/10/23/from-toast-to-bessemer-who-founders-will-hear-from-at-techcrunch-founder-summit-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T19:06:23+00:00",
    "summary": "Hosted by TechCrunch in partnership with Fidelity Private Shares, the full-day event goes beyond fundraising and AI to explore the realities of finding customers, building teams, sharpening a pitch, d"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/23/agent-cloud-startup-daytona-hits-1b-valuation-backed-by-firstmark-and-a-whos-who-of-angels/",
    "domain": "大厂 AI 动态",
    "title": "Agent cloud startup Daytona hits $1B valuation backed by FirstMark and a who’s who of angels",
    "url": "https://techcrunch.com/2026/10/23/agent-cloud-startup-daytona-hits-1b-valuation-backed-by-firstmark-and-a-whos-who-of-angels/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T16:26:29+00:00",
    "summary": "Daytona is building a cloud for agents that's like giving every agent its own computer. It has attracted founders of Stripe, Perplextity, Datadog, Mercor, and others as angels, it says."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/23/commonwealth-fusion-systems-gets-85m-to-build-better-fusion-ready-semiconductors/",
    "domain": "大厂 AI 动态",
    "title": "Commonwealth Fusion Systems gets $85M to build better fusion-ready semiconductors",
    "url": "https://techcrunch.com/2026/10/23/commonwealth-fusion-systems-gets-85m-to-build-better-fusion-ready-semiconductors/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T16:20:28+00:00",
    "summary": "Top-funded fusion startup Commonwealth Fusion Systems received an $85 million award from the federal government to advance conductors for fusion power plants."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/23/what-some-of-anthropics-backers-are-reportedly-worth-before-its-ipo/",
    "domain": "大厂 AI 动态",
    "title": "What some of Anthropic’s backers are worth before its IPO",
    "url": "https://techcrunch.com/2026/10/23/what-some-of-anthropics-backers-are-reportedly-worth-before-its-ipo/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T16:02:43+00:00",
    "summary": "Early-stage and follow-on investors in the AI lab are already sitting on major paper returns."
  },
  {
    "id": "rss:https://stratechery.com/2026/a-new-era/",
    "domain": "大厂 AI 动态",
    "title": "2026.43: A New Era",
    "url": "https://stratechery.com/2026/a-new-era/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of October 19, 2026, including the best iPad but worst phone, SS Sarandos in a storm, and You Can See Everything."
  },
  {
    "id": "rss:https://stratechery.com/2026/sharp-tech-on-video-netflix-angst-the-end-of-the-internet-and-metas-vr-glasses/",
    "domain": "大厂 AI 动态",
    "title": "Sharp Tech on Video: Netflix Angst, the End of the Internet, and Meta’s VR Glasses",
    "url": "https://stratechery.com/2026/sharp-tech-on-video-netflix-angst-the-end-of-the-internet-and-metas-vr-glasses/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T10:00:00+00:00",
    "summary": "Sharp Tech is, for the first time, available on video. You have two ways to consume it: YouTube, and here on Stratechery"
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/a-1000-mile-cloud-on-mars-may-reveal-physics-never-seen-in-nature/",
    "domain": "大厂 AI 动态",
    "title": "A 1,000-mile cloud on Mars may reveal physics never seen in nature",
    "url": "https://arstechnica.com/science/2026/10/a-1000-mile-cloud-on-mars-may-reveal-physics-never-seen-in-nature/",
    "source": "Tereza Ondráčková, wired.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T11:50:28+00:00",
    "summary": "A new model suggests Mars may host ice-forming physics never directly observed before."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/ice-sheet-expansion-may-have-started-2000-years-go-but-we-canceled-that/",
    "domain": "大厂 AI 动态",
    "title": "Ice sheet expansion may have started 2,000 years ago, but we canceled that",
    "url": "https://arstechnica.com/science/2026/10/ice-sheet-expansion-may-have-started-2000-years-go-but-we-canceled-that/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-24T11:00:09+00:00",
    "summary": "The tiny remains of the Laurentide Ice Sheet began getting somewhat less tiny."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/10/nasa-updates-lander-plans-for-moon-landings-finally-solves-long-festering-orion-issue/",
    "domain": "大厂 AI 动态",
    "title": "NASA updates lander plans for Moon landings, finally solves long-festering Orion issue",
    "url": "https://arstechnica.com/space/2026/10/nasa-updates-lander-plans-for-moon-landings-finally-solves-long-festering-orion-issue/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T22:48:25+00:00",
    "summary": "\"We have the mandate, we have the resources, and the support from our stakeholders.\""
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/10/pentagon-memo-on-prediction-markets-says-insider-bets-put-troops-lives-at-risk/",
    "domain": "大厂 AI 动态",
    "title": "Hegseth warns prediction market bets warp military judgment, endanger troops",
    "url": "https://arstechnica.com/tech-policy/2026/10/pentagon-memo-on-prediction-markets-says-insider-bets-put-troops-lives-at-risk/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T20:28:43+00:00",
    "summary": "Pentagon memo: Insider trading gives US enemies key intel on military operations."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/updated-google-privacy-policy-says-your-gmail-might-be-used-for-advertising/",
    "domain": "大厂 AI 动态",
    "title": "Updated Google privacy policy says your Gmail might be used for advertising",
    "url": "https://arstechnica.com/gadgets/2026/10/updated-google-privacy-policy-says-your-gmail-might-be-used-for-advertising/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T20:19:55+00:00",
    "summary": "Turning on Personal Intelligence gives the company more data for ad targeting."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/10/senior-commander-says-space-force-needs-new-spaceport-by-2030/",
    "domain": "大厂 AI 动态",
    "title": "Inside the Pentagon, the pressure is on to find a home for a new spaceport",
    "url": "https://arstechnica.com/space/2026/10/senior-commander-says-space-force-needs-new-spaceport-by-2030/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T19:33:58+00:00",
    "summary": "Space Force considering options: public-private, federal installation, state land."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/spotify-ramps-up-policy-enforcement-on-family-plans/",
    "domain": "大厂 AI 动态",
    "title": "Spotify ramps up policy enforcement on family plans",
    "url": "https://arstechnica.com/gadgets/2026/10/spotify-ramps-up-policy-enforcement-on-family-plans/",
    "source": "Nick Indge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T19:20:27+00:00",
    "summary": "If you share Spotify sub with family, you may need to scan QR code to prove it."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/crows-can-evaluate-visual-info-twice-as-fast-as-mammals/",
    "domain": "大厂 AI 动态",
    "title": "Crows can evaluate visual info twice as fast as mammals",
    "url": "https://arstechnica.com/science/2026/10/crows-can-evaluate-visual-info-twice-as-fast-as-mammals/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T17:32:58+00:00",
    "summary": "Birds' compact nervous system seems to help them handle tasks very quickly."
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
    "id": "hn:50162431",
    "domain": "股票",
    "title": "The Secret Life of Circuits is now in stock everywhere",
    "url": "https://blog.coredump.cx/p/the-secret-life-of-circuits-is-now",
    "source": "surprisetalk",
    "platform": "hackernews",
    "points": 102,
    "published_at": "2026-10-20T07:15:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:50210325",
    "domain": "股票",
    "title": "Built a site that teaches investing using the live market as the examples",
    "url": "https://www.stocksightfinance.com",
    "source": "kshitik",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-10-23T15:07:06+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/capital-wars",
    "domain": "股票",
    "title": "Capital Wars",
    "url": "https://www.netinterest.co/p/capital-wars",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T16:24:17+00:00",
    "summary": "CoreWeave and the Economics of a Data Center Build"
  },
  {
    "id": "hn:50193524",
    "domain": "股票",
    "title": "Chinese stocks turn biggest losers as global AI trade stumbles",
    "url": "https://theedgemalaysia.com/node/822195",
    "source": "miohtama",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-10-22T10:32:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50167295",
    "domain": "股票",
    "title": "Data center stocks slide as Korea IPO plunges 30%, pressuring tech sentiment",
    "url": "https://www.cnbc.com/2026/10/20/data-center-stocks-slide-as-korea-ipo-plunges-30percent-pressuring-tech-sentiment.html",
    "source": "PLenz",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-20T14:50:08+00:00",
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
    "id": "hn:50142772",
    "domain": "股票",
    "title": "How the Fed Is Quietly Inflating the AI Bubble While Hiking Your Electric Bill",
    "url": "https://www.thebignewsletter.com/p/how-the-federal-reserve-secretly",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-10-18T16:48:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50171533",
    "domain": "股票",
    "title": "Anthropic S-1 Shows Red-Hot Growth, Risks and Computing Costs",
    "url": "https://www.wsj.com/tech/ai/anthropic-revenue-growth-ipo-accaf0f1",
    "source": "mmmmmbop",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-10-20T19:34:39+00:00",
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
    "id": "hn:50113666",
    "domain": "股票",
    "title": "South Korea's stock market down, president telling people not to commit suicide",
    "url": "https://twitter.com/litcapital/status/2110752546415382699",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-16T03:26:08+00:00",
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
    "id": "hn:50113735",
    "domain": "股票",
    "title": "CoreWeave Founders Shield Fortunes with $3.3B Stock Sales",
    "url": "https://www.bloomberg.com/news/articles/2026-10-15/coreweave-founders-shield-fortunes-with-3-3-billion-stock-sales",
    "source": "qlte",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-10-16T03:34:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50122366",
    "domain": "股票",
    "title": "Anthropic's Valuation Collapsed by $500B",
    "url": "https://www.telegraph.co.uk/business/2026/10/16/anthropic-valuation-ipo-ai-stock-listing/",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-10-16T18:27:58+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/me-and-my-agents",
    "domain": "股票",
    "title": "Me and My Agents",
    "url": "https://www.netinterest.co/p/me-and-my-agents",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:39:55+00:00",
    "summary": "Unleashing AI Agents on Bank Earnings"
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
    "id": "hn:50112657",
    "domain": "金融",
    "title": "Tesla Roadster",
    "url": "https://www.tesla.com/roadster",
    "source": "shekhar101",
    "platform": "hackernews",
    "points": 1644,
    "published_at": "2026-10-16T01:32:45+00:00",
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
    "id": "hn:50173487",
    "domain": "金融",
    "title": "Feds suspect ransom negotiator ran ShinyHunters extortion site",
    "url": "https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/",
    "source": "Bender",
    "platform": "hackernews",
    "points": 269,
    "published_at": "2026-10-20T22:21:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50190168",
    "domain": "金融",
    "title": "Epic Games Inc v Apple Inc",
    "url": "https://www.judgments.fedcourt.gov.au/judgments/Judgments/fca/single/2026/2026fca1552",
    "source": "Mayzie",
    "platform": "hackernews",
    "points": 191,
    "published_at": "2026-10-22T01:52:03+00:00",
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
    "id": "hn:50131440",
    "domain": "金融",
    "title": "US federal budget deficit jumps 12% in one year to nearly $2 Trillion",
    "url": "https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 208,
    "published_at": "2026-10-17T14:22:05+00:00",
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
    "id": "hn:50090662",
    "domain": "金融",
    "title": "Tesla's Robotaxis Blow Through School Zones, NHTSA Petition Alleges",
    "url": "https://www.extremetech.com/cars/teslas-robotaxis-blow-through-school-zones-nhtsa-petition-alleges",
    "source": "speckx",
    "platform": "hackernews",
    "points": 146,
    "published_at": "2026-10-14T16:45:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:50141295",
    "domain": "金融",
    "title": "Tesla 'Cannot Guarantee' Roadster Reservation Holders Will Ever Get a Car",
    "url": "https://www.thedrive.com/news/tesla-cannot-guarantee-roadster-reservation-holders-will-ever-get-a-car",
    "source": "healsdata",
    "platform": "hackernews",
    "points": 121,
    "published_at": "2026-10-18T14:16:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:50189801",
    "domain": "金融",
    "title": "Tesla profits drop 43% in Q3",
    "url": "https://arstechnica.com/cars/2026/10/tesla-profits-drop-43-in-q3/",
    "source": "throw0101a",
    "platform": "hackernews",
    "points": 87,
    "published_at": "2026-10-22T01:02:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50080275",
    "domain": "金融",
    "title": "Show HN: Pulse Local, a Mac budgeting app whose AI models run on your machine",
    "url": "https://pulseos.finance",
    "source": "niztk",
    "platform": "hackernews",
    "points": 122,
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
    "points": 118,
    "published_at": "2026-10-14T03:28:00+00:00",
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
    "id": "hn:50202671",
    "domain": "金融",
    "title": "AI compute is the new oil–and needs a new market",
    "url": "https://www.economist.com/finance-and-economics/2026/10/22/ai-compute-is-the-new-oil-and-needs-a-new-market",
    "source": "ijidak",
    "platform": "hackernews",
    "points": 53,
    "published_at": "2026-10-22T23:45:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50161207",
    "domain": "金融",
    "title": "U.S. Supreme Court to review 1868 federal ban on home distilling of liquor",
    "url": "https://www.staradvertiser.com/2026/10/19/breaking-news/u-s-supreme-court-to-review-1868-federal-ban-on-home-distilling-of-liquor/",
    "source": "Jimmc414",
    "platform": "hackernews",
    "points": 68,
    "published_at": "2026-10-20T04:02:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50156189",
    "domain": "金融",
    "title": "The US orders every civilian agency to rip out DeepSeek, even tools built on it",
    "url": "https://madrobot.blog/2026/10/19/us-bans-deepseek-federal-agencies-dhs-order-remove-third-party/",
    "source": "jacquesm",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-10-19T18:41:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:50194602",
    "domain": "金融",
    "title": "Full Disk Encryption on Fedora with TPM2",
    "url": "https://www.apalrd.net/posts/2026/ent_luks/",
    "source": "speckx",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-10-22T12:46:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50105900",
    "domain": "金融",
    "title": "Market selloff, rising rates test AI data centre deal boom",
    "url": "https://www.reuters.com/business/finance/market-selloff-rising-rates-test-ai-data-centre-deal-boom-2026-10-15/",
    "source": "tartoran",
    "platform": "hackernews",
    "points": 75,
    "published_at": "2026-10-15T16:17:40+00:00",
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
    "id": "hn:50116255",
    "domain": "金融",
    "title": "Tesla's new Roadster makes a flying debut, hitting 60 MPH in under a second",
    "url": "https://www.foxbusiness.com/technology/teslas-new-roadster-makes-flying-debut-hitting-60-mph-under-second",
    "source": "nsoonhui",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-10-16T09:40:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50114077",
    "domain": "金融",
    "title": "Tesla makes cars that fly? [video]",
    "url": "https://www.youtube.com/watch?v=7p5LxFdc-Qg",
    "source": "merinpapz10",
    "platform": "hackernews",
    "points": 69,
    "published_at": "2026-10-16T04:27:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:50118624",
    "domain": "金融",
    "title": "Tesla unveils 'flying' Roadster with SpaceX thrusters [video]",
    "url": "https://www.youtube.com/watch?v=eqOfmtTJD1A",
    "source": "skadamat",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-10-16T14:12:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50074739",
    "domain": "金融",
    "title": "Americans Trust in Federal Government Sinks to New Depths",
    "url": "https://news.gallup.com/poll/715361/trust-federal-government-sinks-new-depths.aspx",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 49,
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
    "id": "hn:50112380",
    "domain": "金融",
    "title": "Tesla Debuts 2026 Roadster",
    "url": "https://www.nytimes.com/2026/10/15/business/tesla-roadster-2026-ev-sports-car.html",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-10-16T00:57:58+00:00",
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
  },
  {
    "id": "hn:49930690",
    "domain": "金融",
    "title": "Quantitative Finance with OCaml",
    "url": "https://qcaml.com/index.html",
    "source": "leonry",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-10-02T07:14:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:50122776",
    "domain": "金融",
    "title": "Show HN: Stoke Money – Personal finance app built around a cash flow forecast",
    "url": "https://stoke.money",
    "source": "_wesley",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-10-16T18:54:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50062376",
    "domain": "金融",
    "title": "Tesla Factory Plan Increase of Toxic Heavy Metal Emissions Near School",
    "url": "https://anonymous94538.substack.com/p/tesla-fremont-is-applying-to-spew",
    "source": "DeepLogin",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-10-12T20:16:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50118525",
    "domain": "金融",
    "title": "Tesla Roadster: It Flies, Flips, and Hits 0-60 in 0.81s",
    "url": "https://www.notateslaapp.com/news/4837/tesla-roadster-event-recap-it-flies-flips-and-hits-0-60-in-081s",
    "source": "Cabal",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-10-16T14:03:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49849986",
    "domain": "金融",
    "title": "Show HN: Ekselio – Loveable for finance workflows (local first)",
    "url": "https://www.gptbeyond.com/try?home=1",
    "source": "kdautaj",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-09-25T21:09:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:49924299",
    "domain": "金融",
    "title": "Sony released the first CD audio player on this day in 1982",
    "url": "https://www.tomshardware.com/pc-components/storage/sony-released-the-first-cd-audio-player-on-this-day-in-1982-player-cost-usd3-700-when-adjusted-for-inflation-but-it-would-be-another-decade-before-the-cd-rom-driven-multimedia-pc-era-began",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-01T17:07:39+00:00",
    "summary": ""
  }
]
```
