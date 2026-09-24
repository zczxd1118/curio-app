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

- 今日日期：`2026-09-24`
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
  "date": "2026-09-24",
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
    "points": 1991575,
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
    "points": 1901443,
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
    "points": 1593500,
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
    "points": 1328979,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV14rzQB9EJj",
    "domain": "AI",
    "title": "Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill / Hook / 图片 / 上下文处理/ 后台任务",
    "url": "http://www.bilibili.com/video/av115954889596221",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1319719,
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
    "points": 1274294,
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
    "points": 976050,
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
    "points": 945631,
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
    "points": 890603,
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
    "points": 806646,
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
    "points": 691714,
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
    "points": 673932,
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
    "points": 590220,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1RSFUzVEAG",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码",
    "url": "http://www.bilibili.com/video/av116045469783373",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 581583,
    "published_at": "2026-02-10T08:59:28+00:00",
    "summary": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 443263,
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
    "points": 423644,
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
    "points": 379538,
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
    "points": 342620,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 295932,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 294875,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 284886,
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
    "points": 266908,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV154426xEha",
    "domain": "AI",
    "title": "我的 AI 编程全流程：如何使用 AI 稳定交付一个高质量的产品",
    "url": "http://www.bilibili.com/video/av117178586240848",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 225557,
    "published_at": "2026-08-29T11:38:24+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 214160,
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
    "points": 186079,
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
    "points": 181994,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1YG7G6eEPR",
    "domain": "AI",
    "title": "【全60集】吊打付费！目前B站最全最细的Agent智能体开发全套教程！手把手教你打造专属智能体，七天就能从小白到大神！带你从零基础入门到精通实现商业变现！",
    "url": "http://www.bilibili.com/video/av116815090947614",
    "source": "AI-Agent开发",
    "platform": "bilibili",
    "points": 170387,
    "published_at": "2026-06-26T06:57:42+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 162249,
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
    "points": 157452,
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
    "points": 122858,
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
    "points": 93784,
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
    "points": 75680,
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
    "points": 75170,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 55415,
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
    "points": 48541,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1ApYD6KEkD",
    "domain": "AI",
    "title": "马斯克收购Cursor后，Cursor的性价比现在已经爆表",
    "url": "http://www.bilibili.com/video/av117254955993228",
    "source": "jopatk",
    "platform": "bilibili",
    "points": 43507,
    "published_at": "2026-09-11T23:19:58+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1AJen6SEVQ",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！Agentic AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av117274400790619",
    "source": "吴恩达Agent",
    "platform": "bilibili",
    "points": 43128,
    "published_at": "2026-09-15T09:48:26+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署\n4、使用开放标准格式和最佳实践创建可重复使用的技能，并组合以创建复杂的工作流程。\n5、建立定制代码生成技能，审核你的代"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34387,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30772,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 23038,
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
    "points": 20412,
    "published_at": "2026-07-29T07:25:00+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！"
  },
  {
    "id": "bvid:BV1EReW6pEfv",
    "domain": "AI",
    "title": "14K Star Claude Code 开源桌面端，5个AI自己分工干活了！",
    "url": "http://www.bilibili.com/video/av117276346946735",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 18062,
    "published_at": "2026-09-16T03:30:00+00:00",
    "summary": "上一期让 cc-haha 自动操作电脑，这一期，我让 5 个 AI Agent 一起做开发。\n\n用的还是我一直在维护的开源 Claude Code 桌面端：cc-haha。这次重点演示 Agent Teams：我给出一个开发需求，队长拆任务，前端、后端、测试和 Code Review 分工推进。成员做完手上的工作，还能继续领取可执行的任务，直接给队友发消息。\n\n这期用一个真实任务，从组队、共享任务"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 16765,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15231,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV1oQYL64EJV",
    "domain": "AI",
    "title": "【SRC漏洞挖掘】2026最适合新手的AI+自动化挖漏洞教程，从环境搭建到漏洞验证，手把手带你挖到第一个SRC漏洞！",
    "url": "http://www.bilibili.com/video/av117251248490748",
    "source": "阿盾聊安全",
    "platform": "bilibili",
    "points": 14245,
    "published_at": "2026-09-11T07:39:16+00:00",
    "summary": "这套 18 节教程带你从零跑通 AI 自动化挖漏洞全流程：环境搭建、Hermes部署、Burp/Nuclei 集成、资产侦察、漏洞发现到报告验证，一套打通。\n适合有 Web 安全基础、想从手动挖洞升级到自动化的同学。\n资料和工具包见评论区，三连不迷路。"
  },
  {
    "id": "bvid:BV1ZBT2ztEwp",
    "domain": "AI",
    "title": "一条视频讲清楚 到底什么是MCP！#MCP #Cursor #AI #编程",
    "url": "http://www.bilibili.com/video/av114642592469769",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 14225,
    "published_at": "2025-06-07T14:53:38+00:00",
    "summary": "一条视频讲清楚 到底什么是MCP！#MCP #Cursor #AI #编程"
  },
  {
    "id": "bvid:BV1pfuR69EoF",
    "domain": "AI",
    "title": "【全80集】零基础Vibe Coding教程，Vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av117070675118277",
    "source": "暴龙Boy",
    "platform": "bilibili",
    "points": 13408,
    "published_at": "2026-08-10T10:45:04+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 11731,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV1K3X9BFEBg",
    "domain": "AI",
    "title": "审计小白Agent入门",
    "url": "http://www.bilibili.com/video/av116313452186735",
    "source": "茶瓜子w",
    "platform": "bilibili",
    "points": 11675,
    "published_at": "2026-03-29T16:42:59+00:00",
    "summary": "希望能对大家有所帮助"
  },
  {
    "id": "bvid:BV1MAYd6sEZh",
    "domain": "AI",
    "title": "效率翻倍， 一次讲透AI Agent的用法和技巧",
    "url": "http://www.bilibili.com/video/av117258059847877",
    "source": "数码旭",
    "platform": "bilibili",
    "points": 11593,
    "published_at": "2026-09-12T12:33:07+00:00",
    "summary": "AI Agent作为今年AI应用方式最大的变化，会给普通人带来突破性的效率提升，当然也给我带来的特别大的帮助。我希望通过这期长视频，能帮助你提升工作效率。"
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
    "id": "hn:49673098",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is the central bank of AI",
    "url": "https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai",
    "source": "tolugenius",
    "platform": "hackernews",
    "points": 583,
    "published_at": "2026-09-12T15:08:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49824864",
    "domain": "AI 算力 / 半导体",
    "title": "Virtio-nvgpu: Near-native Nvidia GPU access inside a KVM guest",
    "url": "https://github.com/nestrilabs/virtio-nvgpu",
    "source": "WanjohiRyan",
    "platform": "hackernews",
    "points": 82,
    "published_at": "2026-09-24T01:02:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49682319",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia dismisses \"circular financing\", says every $1 it invests brings back $100",
    "url": "https://invezz.com/news/2026/09/11/nvidia-says-every-1-it-invests-brings-back-100-so-why-does-the-stock-keep-falling/",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 138,
    "published_at": "2026-09-13T10:29:18+00:00",
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
    "id": "rss:https://www.eetimes.com/semicon-india-2026-india-starts-packaging-chips-as-ecosystem-takes-shape/",
    "domain": "AI 算力 / 半导体",
    "title": "SEMICON India 2026: India Starts Packaging Chips as Ecosystem Takes Shape",
    "url": "https://www.eetimes.com/semicon-india-2026-india-starts-packaging-chips-as-ecosystem-takes-shape/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T10:56:15+00:00",
    "summary": "India moves five chip packaging plants into production as $13.5 billion ISM 2.0 expands manufacturing, design, and engineering capabilities. The post SEMICON India 2026: India Starts Packaging Chips a"
  },
  {
    "id": "rss:https://www.eetimes.com/smarter-buildings-safer-occupants-intelligence-meets-privacy/",
    "domain": "AI 算力 / 半导体",
    "title": "Smarter Buildings, Safer Occupants: Intelligence Meets Privacy",
    "url": "https://www.eetimes.com/smarter-buildings-safer-occupants-intelligence-meets-privacy/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T08:05:07+00:00",
    "summary": "Modern building automation systems are designed to optimize energy efficiency while safeguarding the health, safety, and security of occupants. The post Smarter Buildings, Safer Occupants: Intelligenc"
  },
  {
    "id": "rss:https://www.eetimes.com/canadian-startup-sees-success-in-space-qualification/",
    "domain": "AI 算力 / 半导体",
    "title": "Canadian Startup Sees Success in Space Qualification",
    "url": "https://www.eetimes.com/canadian-startup-sees-success-in-space-qualification/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T16:21:10+00:00",
    "summary": "Novigrad is forging a pathway for faster, more accessible radiation testing as a growing wave of space missions drives demand for reliable, resilient electronics. The post Canadian Startup Sees Succes"
  },
  {
    "id": "rss:https://www.eetimes.com/guc-announces-2nm-16-gbps-hbm4e-ip/",
    "domain": "AI 算力 / 半导体",
    "title": "GUC Announces 2nm 16 Gbps HBM4E IP",
    "url": "https://www.eetimes.com/guc-announces-2nm-16-gbps-hbm4e-ip/",
    "source": "Global Unichip Corp. (GUC)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T13:00:00+00:00",
    "summary": "Discover GUC's design-ready HBM4E PHY and Controller IP, adopted in customers' AI ASICs. The post GUC Announces 2nm 16 Gbps HBM4E IP appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/tablets/microsoft-surface/microsoft-brings-snapdragon-x2-plus-to-13-inch-surface-laptop-12-inch-surface-pro-low-end-systems-finally-get-upgrades",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft brings Snapdragon X2 Plus to 13-inch Surface Laptop, 12-inch Surface Pro",
    "url": "https://www.tomshardware.com/tablets/microsoft-surface/microsoft-brings-snapdragon-x2-plus-to-13-inch-surface-laptop-12-inch-surface-pro-low-end-systems-finally-get-upgrades",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T20:30:00+00:00",
    "summary": "Microsoft's lowest-end systems are getting upgrades to Qualcomm's latest Snapdragon X2 Plus processors."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/chinas-ymtc-wins-patent-battle-against-micron-in-ongoing-3-year-legal-war-over-memory-patents-new-injunctions-could-restrict-microns-supply-into-germany",
    "domain": "AI 算力 / 半导体",
    "title": "China's YMTC wins patent battle against Micron in ongoing 3-year legal war over memory patents",
    "url": "https://www.tomshardware.com/pc-components/storage/chinas-ymtc-wins-patent-battle-against-micron-in-ongoing-3-year-legal-war-over-memory-patents-new-injunctions-could-restrict-microns-supply-into-germany",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T15:56:02+00:00",
    "summary": "A Munich court has granted YMTC two injunctions against Micron over 3D NAND patents, the latest development in a years-long cross-border legal battle between the memory rivals."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-claims-new-qwen-image-2-1-ai-model-beats-google-nano-banana-2-0-with-minuscule-7b-parameter-model-benchmarks-show-open-weight-contender-is-competitive-with-openai-and-meta-image-models",
    "domain": "AI 算力 / 半导体",
    "title": "Alibaba claims new Qwen Image 2.1 AI model beats Google Nano Banana 2.0 with minuscule 7B parameter model",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-claims-new-qwen-image-2-1-ai-model-beats-google-nano-banana-2-0-with-minuscule-7b-parameter-model-benchmarks-show-open-weight-contender-is-competitive-with-openai-and-meta-image-models",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T15:34:36+00:00",
    "summary": "Alibaba Group's AI division has released Qwen 2.1 Image, an ultra-lightweight image generation model with just 7B parameters, able to run on local hardware like the RTX 3090."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/case-mods/usd14-000-gaming-pc-features-70-handcrafted-titanium-cherry-blossoms-which-unfurl-as-temperatures-rise-zotac-designed-rtx-5080-system-features-impressive-sculpture-and-an-eye-watering-price-tag-to-match",
    "domain": "AI 算力 / 半导体",
    "title": "$14,000 gaming PC features 70 handcrafted titanium cherry blossoms which unfurl as temperatures rise",
    "url": "https://www.tomshardware.com/pc-components/case-mods/usd14-000-gaming-pc-features-70-handcrafted-titanium-cherry-blossoms-which-unfurl-as-temperatures-rise-zotac-designed-rtx-5080-system-features-impressive-sculpture-and-an-eye-watering-price-tag-to-match",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T13:14:43+00:00",
    "summary": "The Aftershock PC Cherry Bloom includes 70 hand-crafted cherry blossoms made of titanium alloy that open and close with the heat generated by the PC."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/sony-inzone-m10s-ii-27-inch-540-hz-qhd-oled-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Sony INZONE M10S II 27-inch 540 Hz QHD OLED gaming monitor review: A major player in a crowded field",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/sony-inzone-m10s-ii-27-inch-540-hz-qhd-oled-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T13:00:00+00:00",
    "summary": "Sony brings saturated color and speedy gameplay to the OLED genre with its INZONE M10S II 27-inch QHD monitor. It boasts a 540 Hz refresh rate, 720 Hz at HD resolution, Adaptive-Sync, HDR, and wide-ga"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/filing-reveals-how-bytedance-gained-access-to-over-2-000-nvidia-b200-chips-through-nscales-norway-data-center-singaporean-subsidiary-spring-contributed-73-percent-of-uk-neoclouds-2025-revenue",
    "domain": "AI 算力 / 半导体",
    "title": "China's ByteDance gained access to over 2,000 Nvidia B200 chips through Norway data center",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/filing-reveals-how-bytedance-gained-access-to-over-2-000-nvidia-b200-chips-through-nscales-norway-data-center-singaporean-subsidiary-spring-contributed-73-percent-of-uk-neoclouds-2025-revenue",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T12:00:43+00:00",
    "summary": "UK-based Nscale signed a deal with Spring (SG) Pte Ltd, which is a subsidiary of Chinese tech giant ByteDance. The company did not make any direct mention of the TikTok parent in its filings for a U.S"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-unveils-zhenwu-v900-ai-accelerator-claims-its-the-most-powerful-ai-chip-in-china-accelerator-supports-500-000-chip-supercluster-with-a-10t-parameter-qwen-model-on-the-roadmap",
    "domain": "AI 算力 / 半导体",
    "title": "Alibaba unveils Zhenwu V900 AI accelerator, claims it's 'the most powerful AI chip in China'",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-unveils-zhenwu-v900-ai-accelerator-claims-its-the-most-powerful-ai-chip-in-china-accelerator-supports-500-000-chip-supercluster-with-a-10t-parameter-qwen-model-on-the-roadmap",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T12:00:00+00:00",
    "summary": "Alibaba’s T-Head Zhenwu V900 claims three times the M890’s performance with 216GB of memory as Alibaba targets 10T-parameter Qwen"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/upgrade-your-gaming-experience-with-this-27-inch-acer-1440p-270hz-panel-thats-an-incredible-45-percent-off-just-usd179-buys-an-awesome-ips-monitor-with-amd-freesync-premium-and-1ms-response-time",
    "domain": "AI 算力 / 半导体",
    "title": "Upgrade your gaming experience with this 27-inch Acer 1440p 270Hz panel that’s an incredible 45% off",
    "url": "https://www.tomshardware.com/pc-components/upgrade-your-gaming-experience-with-this-27-inch-acer-1440p-270hz-panel-thats-an-incredible-45-percent-off-just-usd179-buys-an-awesome-ips-monitor-with-amd-freesync-premium-and-1ms-response-time",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T11:45:00+00:00",
    "summary": "Jump into high-refresh-rate 1440p gaming without breaking the bank: Acer's 27-inch 1440p 270Hz IPS gaming monitor is just $179, a whopping 45% off"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amd-begins-to-add-gddr7-support-to-its-linux-gpu-drivers-changes-could-herald-use-of-advanced-memory-standard-with-next-gen-radeon-gpus",
    "domain": "AI 算力 / 半导体",
    "title": "AMD begins to add GDDR7 support to its Linux GPU drivers",
    "url": "https://www.tomshardware.com/pc-components/gpus/amd-begins-to-add-gddr7-support-to-its-linux-gpu-drivers-changes-could-herald-use-of-advanced-memory-standard-with-next-gen-radeon-gpus",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T11:30:00+00:00",
    "summary": "Recent changes to AMD's Linux drivers to enable GDDR7 memory and other graphics IP blocks could indicate that that enablement work on its RDNA 5 GPUs is under way."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/metas-new-transoceanic-undersea-cable-boasts-a-whopping-petabit-of-bandwidth-petal-link-between-us-and-france-will-be-twice-as-fast-as-the-last",
    "domain": "AI 算力 / 半导体",
    "title": "Meta's new transoceanic undersea cable boasts a whopping petabit of bandwidth",
    "url": "https://www.tomshardware.com/networking/metas-new-transoceanic-undersea-cable-boasts-a-whopping-petabit-of-bandwidth-petal-link-between-us-and-france-will-be-twice-as-fast-as-the-last",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T11:00:00+00:00",
    "summary": "Meta has announced Petal, a new subsea cable that will carry a petabit of raw bandwidth across the 4,300 miles between the USA and France."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-32gb-corsair-vengeance-ddr5-6000-memory-is-the-cheapest-kit-available-discount-plus-usd40-promo-code-offers-the-least-expensive-ddr5-6000-kit-available-today",
    "domain": "AI 算力 / 半导体",
    "title": "This 32GB Corsair Vengeance DDR5-6000 memory is the cheapest kit available",
    "url": "https://www.tomshardware.com/pc-components/this-32gb-corsair-vengeance-ddr5-6000-memory-is-the-cheapest-kit-available-discount-plus-usd40-promo-code-offers-the-least-expensive-ddr5-6000-kit-available-today",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T10:45:00+00:00",
    "summary": "Get a great deal on 32GB Corsair Vengeance DDR5-6000 RAM. Just $439 after promo code SSF73844 yields one of the lowest priced 32GB kits available today"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/space/china-puts-ai-compute-into-orbit-with-supercomputing-1-satellite-onboard-processing-aims-to-cut-earth-observation-data-processing-from-hours-to-minutes",
    "domain": "AI 算力 / 半导体",
    "title": "China launches 'Supercomputing-1' AI satellite as orbital data centers gather momentum",
    "url": "https://www.tomshardware.com/tech-industry/space/china-puts-ai-compute-into-orbit-with-supercomputing-1-satellite-onboard-processing-aims-to-cut-earth-observation-data-processing-from-hours-to-minutes",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T10:30:00+00:00",
    "summary": "But it's a far cry from an orbital data center."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/airbus-turned-the-steam-deck-into-a-controller-for-a-prototype-mars-rover-valve-handheld-pc-gives-engineers-command-of-the-exomars-platform-during-testing",
    "domain": "AI 算力 / 半导体",
    "title": "Airbus turned the Steam Deck into a controller for a prototype Mars rover",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/airbus-turned-the-steam-deck-into-a-controller-for-a-prototype-mars-rover-valve-handheld-pc-gives-engineers-command-of-the-exomars-platform-during-testing",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T10:00:00+00:00",
    "summary": "Airbus engineers have employed Valve's Steam Deck handheld as a fancy remote control for the firm's new ExoMars"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/microsd-cards/beat-the-switch-2-storage-crisis-with-this-usd99-512gb-microsd-express-card-amazon-deal-slashes-33-percent-off-high-performance-samsung-p9",
    "domain": "AI 算力 / 半导体",
    "title": "Beat the Switch 2 storage crisis with this $99 512GB microSD Express card",
    "url": "https://www.tomshardware.com/pc-components/microsd-cards/beat-the-switch-2-storage-crisis-with-this-usd99-512gb-microsd-express-card-amazon-deal-slashes-33-percent-off-high-performance-samsung-p9",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T18:18:55+00:00",
    "summary": "Amazon has slashed 33% off the price of the Samsung P9 microSD Express card for the Nintendo Switch 2, bringing it down to $99.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/durabook-z14i-dx3-rugged-mobile-workstation-folds-three-screens-into-a-9-8-kg-chassis-luggable-targets-military-emergency-services-and-field-professionals",
    "domain": "AI 算力 / 半导体",
    "title": "Durabook Z14I-DX3 rugged mobile workstation folds three screens into a 9.8 kg chassis",
    "url": "https://www.tomshardware.com/laptops/durabook-z14i-dx3-rugged-mobile-workstation-folds-three-screens-into-a-9-8-kg-chassis-luggable-targets-military-emergency-services-and-field-professionals",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T16:33:41+00:00",
    "summary": "Built for military, emergency services and industrial applications, the Z14I-DX3 packs three sunlight-readable 14-inch touchscreens and up to RTX 5000 Ada graphics into one exceptionally rugged mobile"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/get-this-spiffy-stealthy-msi-rtx-5090-for-just-usd4-299-geforce-week-at-walmart-serves-up-a-rare-deal-on-nvidias-fastest-gaming-gpu",
    "domain": "AI 算力 / 半导体",
    "title": "Get this spiffy, stealthy MSI Gaming Trio RTX 5090 for just $4,299",
    "url": "https://www.tomshardware.com/pc-components/gpus/get-this-spiffy-stealthy-msi-rtx-5090-for-just-usd4-299-geforce-week-at-walmart-serves-up-a-rare-deal-on-nvidias-fastest-gaming-gpu",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T15:00:52+00:00",
    "summary": "Walmart has MSI's GeForce RTX 5090 Gaming Trio for just $4299 as part of its GeForce Week event, a rare deal on the most powerful graphics card around as the AI boom drives prices ever higher."
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/bambu-lab-r1-review",
    "domain": "AI 算力 / 半导体",
    "title": "Bambu Lab R1 Review: This one stands alone",
    "url": "https://www.tomshardware.com/maker-stem/bambu-lab-r1-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T14:00:00+00:00",
    "summary": "Bambu Lab leverages its mastery of motion systems and UI to create a nearly perfect stand-alone laser."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-keyboards/glorious-gmmk-eternal-review",
    "domain": "AI 算力 / 半导体",
    "title": "Glorious GMMK Eternal Review: Fits anywhere, sounds great",
    "url": "https://www.tomshardware.com/peripherals/gaming-keyboards/glorious-gmmk-eternal-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T13:00:00+00:00",
    "summary": "Glorious' new GMMK Eternal is a compact 96-percent wired keyboard with hot-swappable mechanical switches and three layers of sound-dampening in the case."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptomining/well-be-the-first-to-mine-bitcoin-in-space-says-nvidia-backed-startup-starcloud-will-fire-up-its-asics-after-its-second-spacecraft-reaches-orbit-later-this-year",
    "domain": "AI 算力 / 半导体",
    "title": "‘We’ll be the first to mine Bitcoin in space’ says Nvidia-backed startup",
    "url": "https://www.tomshardware.com/tech-industry/cryptomining/well-be-the-first-to-mine-bitcoin-in-space-says-nvidia-backed-startup-starcloud-will-fire-up-its-asics-after-its-second-spacecraft-reaches-orbit-later-this-year",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T12:59:50+00:00",
    "summary": "An Nvidia-backed startup plans to establish a Bitcoin mining operation in space before the year is out."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/us-and-china-propose-hotline-to-de-escalate-ai-threats-ahead-of-washington-summit-comms-channel-between-both-nations-to-be-left-open-in-case-of-national-security-threats-posed-by-autonomous-artificial-intelligence",
    "domain": "AI 算力 / 半导体",
    "title": "US and China propose hotline to de-escalate AI threats ahead of Washington summit",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/us-and-china-propose-hotline-to-de-escalate-ai-threats-ahead-of-washington-summit-comms-channel-between-both-nations-to-be-left-open-in-case-of-national-security-threats-posed-by-autonomous-artificial-intelligence",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T12:13:41+00:00",
    "summary": "The U.S. and China have proposed implementing AI red lines that will not be crossed, as well as a hotline between the two countries to provide rapid communication and opportunities for joint responses"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/gaming-pc-with-rtx-5060-32gb-of-ram-and-1tb-of-storage-gets-usd500-discount-neweggs-capable-abs-cyclone-aqua-prebuilt-is-usd1-199-with-code",
    "domain": "AI 算力 / 半导体",
    "title": "Gaming PC with RTX 5060, 32GB of RAM, and 1TB of storage gets $500 discount",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/gaming-pc-with-rtx-5060-32gb-of-ram-and-1tb-of-storage-gets-usd500-discount-neweggs-capable-abs-cyclone-aqua-prebuilt-is-usd1-199-with-code",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T11:30:00+00:00",
    "summary": "Newegg's ABS Cyclone Aqua prebuilt combines Intel's 20-core Core i7-14700F with Nvidia's RTX 5060 8GB, and 32GB of DDR4 memory for less than the cost of building a comparable system"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/dram-is-now-more-expensive-than-compute-chips-on-per-area-basis-ai-demand-drives-memory-die-value-past-leading-edge-silicon",
    "domain": "AI 算力 / 半导体",
    "title": "Memory chips are now more expensive than compute chips on a per-area basis",
    "url": "https://www.tomshardware.com/pc-components/dram/dram-is-now-more-expensive-than-compute-chips-on-per-area-basis-ai-demand-drives-memory-die-value-past-leading-edge-silicon",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T11:12:35+00:00",
    "summary": "DRAM makers may potentially get more money for their wafers than TSMC gets for its N3 wafers."
  },
  {
    "id": "rss:https://www.tomshardware.com/raspberry-pi/raspberry-pi-locks-boards-to-factory-ram-capacities-in-firmware-engineer-tells-diy-modders-dont-waste-your-time-trying-repairs-or-upgrades-company-cites-shady-reseller-scams",
    "domain": "AI 算力 / 半导体",
    "title": "Raspberry Pi locks boards to factory RAM capacities in firmware",
    "url": "https://www.tomshardware.com/raspberry-pi/raspberry-pi-locks-boards-to-factory-ram-capacities-in-firmware-engineer-tells-diy-modders-dont-waste-your-time-trying-repairs-or-upgrades-company-cites-shady-reseller-scams",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T11:07:17+00:00",
    "summary": "Raspberry Pi users are being firmware blocked from swapping the RAM chips on their SBCs for repairs or upgrades."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-usd299-2tb-msi-ssd-is-one-of-the-least-expensive-pcie-4-0-ssds-you-can-buy-right-now-just-10-cents-per-gb-yields-a-speedy-upgrade-for-your-internal-storage",
    "domain": "AI 算力 / 半导体",
    "title": "This $299 2TB MSI SSD is one of the least expensive PCIe 4.0 SSDs you can buy right now",
    "url": "https://www.tomshardware.com/pc-components/this-usd299-2tb-msi-ssd-is-one-of-the-least-expensive-pcie-4-0-ssds-you-can-buy-right-now-just-10-cents-per-gb-yields-a-speedy-upgrade-for-your-internal-storage",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T10:48:20+00:00",
    "summary": "Get a solid deal on the 2TB MSI Spatium M461 SSD. Just $299 after promo code nets one of the least expensive Gen 4x4 SSDs available today."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/dapustor-splits-qlc-ssd-to-create-a-fast-pslc-region-in-dual-mode-drive-trades-6-percent-to-20-percent-of-its-qlc-capacity-for-more-than-7x-faster-random-writes",
    "domain": "AI 算力 / 半导体",
    "title": "New DapuStor SSD pairs high-capacity QLC with a permanent pSLC region",
    "url": "https://www.tomshardware.com/pc-components/ssds/dapustor-splits-qlc-ssd-to-create-a-fast-pslc-region-in-dual-mode-drive-trades-6-percent-to-20-percent-of-its-qlc-capacity-for-more-than-7x-faster-random-writes",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T10:30:00+00:00",
    "summary": "DapuStor’s dual-mode J5060 QLC SSD runs part of its NAND as pSLC, trading 4TB of a 30.72TB drive for 800GB of fast flash."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/chinas-cxmt-hits-12nm-class-dram-milestone-new-5th-gen-dram-tech-uses-quadruple-patterning-to-boost-die-capacity-by-50-percent",
    "domain": "AI 算力 / 半导体",
    "title": "China's CXMT hits 12nm-class DRAM milestone",
    "url": "https://www.tomshardware.com/pc-components/dram/chinas-cxmt-hits-12nm-class-dram-milestone-new-5th-gen-dram-tech-uses-quadruple-patterning-to-boost-die-capacity-by-50-percent",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T10:00:00+00:00",
    "summary": "China's DRAM champion CXMT has begun mass production using its 5th Geb DRAM process technology"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/openai-and-anthropic-are-reportedly-seeking-out-smaller-data-center-deals-to-meet-current-demand-20-30-mw-facilities-to-provide-capacity-as-mega-structures-undergo-construction",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI and Anthropic scramble for smaller data centers as massive gigawatt projects lag",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/openai-and-anthropic-are-reportedly-seeking-out-smaller-data-center-deals-to-meet-current-demand-20-30-mw-facilities-to-provide-capacity-as-mega-structures-undergo-construction",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T09:30:00+00:00",
    "summary": "OpenAI and Anthropic are seeking to secure immediate capacity, through smaller data center deals, to meet current demand, despite spending billions on massive deals elsewhere."
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
    "id": "rss:https://www.eetimes.com/how-ai-is-accelerating-pcb-design-and-prototyping/",
    "domain": "AI 算力 / 半导体",
    "title": "How AI Is Accelerating PCB Design and Prototyping",
    "url": "https://www.eetimes.com/how-ai-is-accelerating-pcb-design-and-prototyping/",
    "source": "Emily Newton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T07:59:35+00:00",
    "summary": "AI tools compress PCB design timelines from months to hours, enabling faster iteration cycles and letting engineers focus on innovation. The post How AI Is Accelerating PCB Design and Prototyping appe"
  },
  {
    "id": "rss:https://www.eetimes.com/singapore-turning-quantum-research-into-business-opportunity/",
    "domain": "AI 算力 / 半导体",
    "title": "Singapore: Turning Quantum Research into Business Opportunity",
    "url": "https://www.eetimes.com/singapore-turning-quantum-research-into-business-opportunity/",
    "source": "Pietro Guzzetti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T20:00:00+00:00",
    "summary": "Singapore’s government funding, research infrastructure, and commercial focus are creating a booming regional hub for quantum technologies. The post Singapore: Turning Quantum Research into Business O"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-power-demands-push-gan-into-data-center-design/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Power Demands Push GaN into Data Center Design",
    "url": "https://www.eetimes.com/ai-power-demands-push-gan-into-data-center-design/",
    "source": "Stephen Las Marias",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T16:59:04+00:00",
    "summary": "Rising AI power demands are pushing data center designers toward GaN-based power conversion for higher efficiency and density. The post AI Power Demands Push GaN into Data Center Design appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/highly-integrated-multibeam-beamformers-offer-swap-benefits-for-payload-phased-array-antennas/",
    "domain": "AI 算力 / 半导体",
    "title": "Highly Integrated Multibeam Beamformers Offer SWaP Benefits for Payload Phased Array Antennas",
    "url": "https://www.eetimes.com/highly-integrated-multibeam-beamformers-offer-swap-benefits-for-payload-phased-array-antennas/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T14:00:00+00:00",
    "summary": "Satellite payload designers are under growing pressure to deliver more capacity, wider coverage, and greater flexibility while working within strict size, weight, and power constraints. As phased-arra"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/iphone-18-pro-max-storage-can-drop-lower-than-a-hard-drive-at-1-1-mb-s-during-heavy-writes-qlc-nand-offers-higher-capacity-but-reportedly-suffers-38-percent-drop-compared-to-tlc-based-pro",
    "domain": "AI 算力 / 半导体",
    "title": "iPhone 18 Pro Max storage can drop lower than a hard drive at 1.1 MB/s during heavy writes",
    "url": "https://www.tomshardware.com/pc-components/ssds/iphone-18-pro-max-storage-can-drop-lower-than-a-hard-drive-at-1-1-mb-s-during-heavy-writes-qlc-nand-offers-higher-capacity-but-reportedly-suffers-38-percent-drop-compared-to-tlc-based-pro",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T17:34:47+00:00",
    "summary": "Apple's use of QLC NAND allows the iPhone 18 Pro Max to offer higher storage capacity, but Homolab's testing highlights the potential performance trade-off under sustained writes."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/get-the-worlds-fastest-gaming-cpu-and-a-dlss-5-capable-gpu-in-a-gaming-pc-for-usd2-299-fully-loaded-powerhouse-sports-ryzen-7-9800x3d-rtx-5080-founders-edition-32gb-ram-and-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Get the world’s fastest gaming CPU and a DLSS 5-capable GPU in a gaming PC for $2,299",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/get-the-worlds-fastest-gaming-cpu-and-a-dlss-5-capable-gpu-in-a-gaming-pc-for-usd2-299-fully-loaded-powerhouse-sports-ryzen-7-9800x3d-rtx-5080-founders-edition-32gb-ram-and-1tb-ssd",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T17:19:27+00:00",
    "summary": "Walmart is selling a CyberPowerPC gaming PC with a Ryzen 7 9800X3D, GeForce RTX 5080 Founders Edition, 32GB of DDR5-6000 memory, and a 1TB PCIe 4.0 SSD for $2,299."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/local-opposition-blocked-usd68-billion-worth-of-data-center-projects-in-the-second-quarter-of-2026-data-center-investments-reportedly-still-on-track-to-hit-usd32-trillion-by-2050",
    "domain": "AI 算力 / 半导体",
    "title": "Local opposition blocked $68 billion worth of data center projects in the second quarter of 2026",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/local-opposition-blocked-usd68-billion-worth-of-data-center-projects-in-the-second-quarter-of-2026-data-center-investments-reportedly-still-on-track-to-hit-usd32-trillion-by-2050",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T16:00:00+00:00",
    "summary": "Local opposition to data center buildouts has blocked $68 billion worth of data center projects in the second quarter of 2026, despite investments still rising."
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
    "points": 865,
    "published_at": "2026-09-22T08:04:55+00:00",
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
    "id": "hn:49790409",
    "domain": "大厂 AI 动态",
    "title": "Turn off and restrict access to Apple Intelligence features on Mac",
    "url": "https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac",
    "source": "alwillis",
    "platform": "hackernews",
    "points": 347,
    "published_at": "2026-09-21T17:30:21+00:00",
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
    "id": "hn:49817615",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 text-to-speech",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/",
    "source": "swolpers",
    "platform": "hackernews",
    "points": 300,
    "published_at": "2026-09-23T15:29:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49468818",
    "domain": "大厂 AI 动态",
    "title": "Gemini-3.5-Transcribe",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/",
    "source": "k9294",
    "platform": "hackernews",
    "points": 363,
    "published_at": "2026-08-27T18:03:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:49467922",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni 1.1 Flash",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/",
    "source": "saretup",
    "platform": "hackernews",
    "points": 297,
    "published_at": "2026-08-27T17:06:32+00:00",
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
    "id": "hn:49773998",
    "domain": "大厂 AI 动态",
    "title": "Microsoft agentically ports Copilot runtime to Rust for $120K",
    "url": "https://www.theregister.com/devops/2026/09/18/microsoft-agentically-ports-copilot-runtime-to-rust-for-120k/5297549",
    "source": "pjmlp",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-09-20T09:08:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:49762493",
    "domain": "大厂 AI 动态",
    "title": "Gemini hacked three companies in first known breakout by Google's AI",
    "url": "https://www.reuters.com/business/gemini-hacked-three-companies-first-known-breakout-by-google-ai-wsj-reports-2026-09-18/",
    "source": "usernomdeguerre",
    "platform": "hackernews",
    "points": 77,
    "published_at": "2026-09-19T01:40:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49743685",
    "domain": "大厂 AI 动态",
    "title": "Economic policy for AGI",
    "url": "https://institute.deepmind.com/essays/economic-policy-for-agi/",
    "source": "alphabetatango",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-09-17T17:12:51+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/999750/muse-charm-meta-ai-hardware",
    "domain": "大厂 AI 动态",
    "title": "Meta is making a standalone Muse AI gadget",
    "url": "https://www.theverge.com/tech/999750/muse-charm-meta-ai-hardware",
    "source": "Jacob Kastrenakes",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T00:15:20+00:00",
    "summary": "Meta is building a dedicated hardware device for its new Muse AI agent. The product, called Muse Charm, was briefly shown off by Meta CEO Mark Zuckerberg at the end of tonight's Meta Connect presentat"
  },
  {
    "id": "rss:https://www.theverge.com/tech/999593/meta-connect-2026-everything-announced",
    "domain": "大厂 AI 动态",
    "title": "Meta Connect 2026: The 7 biggest announcements",
    "url": "https://www.theverge.com/tech/999593/meta-connect-2026-everything-announced",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T00:00:33+00:00",
    "summary": "Meta announced a slate of new wearables during its annual Meta Connect showcase on Wednesday. The star of the event was the new Meta VR Glasses, which pack virtual reality tech into a lightweight smar"
  },
  {
    "id": "rss:https://www.theverge.com/tech/999517/meta-vr-glasses-connect-2026-hands-on",
    "domain": "大厂 AI 动态",
    "title": "Meta’s next VR device isn’t a headset — it’s glasses",
    "url": "https://www.theverge.com/tech/999517/meta-vr-glasses-connect-2026-hands-on",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T23:42:10+00:00",
    "summary": "Meta is launching new VR hardware: a pair of glasses. The new Meta VR Glasses sit on your ears like a typical pair of glasses instead of being strapped over your head, but they still have immersive di"
  },
  {
    "id": "rss:https://www.theverge.com/tech/999673/meta-connect-2026-muse-glasses-features",
    "domain": "大厂 AI 动态",
    "title": "Muse is coming to Meta smart glasses",
    "url": "https://www.theverge.com/tech/999673/meta-connect-2026-muse-glasses-features",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T23:40:56+00:00",
    "summary": "Just a couple of weeks after launching Muse, Meta announced that it's \"working on\" bringing the agent to its smart glasses, including the new glasses it unveiled at Meta Connect. Users will be able to"
  },
  {
    "id": "rss:https://www.theverge.com/tech/999281/ray-ban-meta-audio-glasses-meta-connect-2026",
    "domain": "大厂 AI 动态",
    "title": "Meta ditches the camera on its newest smart glasses",
    "url": "https://www.theverge.com/tech/999281/ray-ban-meta-audio-glasses-meta-connect-2026",
    "source": "Victoria Song",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T23:37:17+00:00",
    "summary": "Walking around Meta Connect 2026, everyone's sporting smart glasses in all sorts of shapes, colors, and sizes. It's a marked difference here, a tech bubble where \"pervert glasses\" are not a concern. O"
  },
  {
    "id": "rss:https://www.theverge.com/tech/999454/meta-muse-ai-agent-video-chat-connect-2026",
    "domain": "大厂 AI 动态",
    "title": "Meta is making Muse more powerful and will let you video chat with it, too",
    "url": "https://www.theverge.com/tech/999454/meta-muse-ai-agent-video-chat-connect-2026",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T23:19:42+00:00",
    "summary": "Meta is quickly iterating on its new Muse AI agent, announcing a bunch of updates today that make the bot more capable and able to chat with you in more ways. Muse agents are getting their own email a"
  },
  {
    "id": "rss:https://www.theverge.com/tech/998480/meta-connect-2026-biggest-news-announcements",
    "domain": "大厂 AI 动态",
    "title": "Meta Connect 2026: The biggest news and announcements",
    "url": "https://www.theverge.com/tech/998480/meta-connect-2026-biggest-news-announcements",
    "source": "Verge Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T22:45:00+00:00",
    "summary": "It&#8217;s about time for Meta Connect, the company&#8217;s annual product launch event. This year, given the company&#8217;s major focus on AI and wearables like smart glasses, it seems likely that w"
  },
  {
    "id": "rss:https://www.theverge.com/tech/998457/meta-connect-2026-live-blog-mark-zuckerberg-keynote",
    "domain": "大厂 AI 动态",
    "title": "Meta Connect 2026 live blog: On the ground at Mark Zuckerberg’s next big product launch",
    "url": "https://www.theverge.com/tech/998457/meta-connect-2026-live-blog-mark-zuckerberg-keynote",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T22:30:00+00:00",
    "summary": "It's time once again for Meta's annual September product launch event, and The Verge is on the ground in Menlo Park to cover the show live. Meta says that today's keynote by Mark Zuckerberg will be ab"
  },
  {
    "id": "rss:https://www.theverge.com/news/999195/microsoft-surface-pro-12-inch-surface-laptop-13-inch-qualcomm-x2-plus",
    "domain": "大厂 AI 动态",
    "title": "Microsoft refreshes its smaller Surface Pro and Laptop with Qualcomm’s X2 Plus",
    "url": "https://www.theverge.com/news/999195/microsoft-surface-pro-12-inch-surface-laptop-13-inch-qualcomm-x2-plus",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T20:30:00+00:00",
    "summary": "Microsoft is refreshing its Surface Pro 12-inch and Surface Laptop 13-inch devices with Qualcomm's latest Snapdragon X2 Plus chips. The smaller Surface devices retain the same design and hardware feat"
  },
  {
    "id": "rss:https://www.theverge.com/news/999211/microsoft-surface-mouse-haptic-feedback",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s new Surface Mouse has haptic feedback and a customizable action button",
    "url": "https://www.theverge.com/news/999211/microsoft-surface-mouse-haptic-feedback",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T20:30:00+00:00",
    "summary": "Microsoft is launching a second generation of its Surface Mouse next month that includes haptic feedback support. The Surface Mouse also has a customizable action button for the first time, which is p"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/everything-new-coming-to-metas-ai-agent-muse/",
    "domain": "大厂 AI 动态",
    "title": "Everything new coming to Meta’s AI agent Muse",
    "url": "https://techcrunch.com/2026/09/23/everything-new-coming-to-metas-ai-agent-muse/",
    "source": "Kirsten Korosec, Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T01:13:32+00:00",
    "summary": "CEO Mark Zuckerberg kicked off the company’s annual Connect event in Menlo Park on Wednesday with a keynote that made one thing clear: Meta is going all-in on Muse. It's even coming to Meta's AI glass"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/meta-made-a-tamagotchi-like-wearable-for-its-muse-ai-agent/",
    "domain": "大厂 AI 动态",
    "title": "Meta made a Tamagotchi-like wearable for its Muse AI agent",
    "url": "https://techcrunch.com/2026/09/23/meta-made-a-tamagotchi-like-wearable-for-its-muse-ai-agent/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T00:46:17+00:00",
    "summary": "The tiny hardware device creates another mobile home for its AI agent Muse."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/meta-is-trying-vr-glasses-again-this-time-with-more-imax/",
    "domain": "大厂 AI 动态",
    "title": "Meta is trying VR glasses (again), this time with more IMAX",
    "url": "https://techcrunch.com/2026/09/23/meta-is-trying-vr-glasses-again-this-time-with-more-imax/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T23:47:35+00:00",
    "summary": "Meta's return to the VR glasses realm comes with a promising combination of light weight form factor and enhanced entertainment options."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/meta-introduces-camera-free-ai-glasses/",
    "domain": "大厂 AI 动态",
    "title": "Meta introduces camera-free AI glasses",
    "url": "https://techcrunch.com/2026/09/23/meta-introduces-camera-free-ai-glasses/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T23:39:44+00:00",
    "summary": "Meta says the camera-free glasses will be lighter and have up to 12 hours battery life."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/vogue-sent-robots-down-the-runway-at-vogue-world-and-people-were-not-impressed/",
    "domain": "大厂 AI 动态",
    "title": "Vogue sent robots down the runway at Vogue World, and people were not impressed",
    "url": "https://techcrunch.com/2026/09/23/vogue-sent-robots-down-the-runway-at-vogue-world-and-people-were-not-impressed/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T23:33:22+00:00",
    "summary": "Nothing says Italian craftsmanship like a Chinese robot doing a lasso to \"L'Amour Toujours.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/anthropic-says-its-biology-lab-has-already-found-something-big/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic says its biology lab has already found something big",
    "url": "https://techcrunch.com/2026/09/23/anthropic-says-its-biology-lab-has-already-found-something-big/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T22:17:39+00:00",
    "summary": "But maybe the biggest reveal is that Anthropic has not let Claude run loose in its biology lab. Humans are still, so far, in the loop."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/if-amazon-doesnt-know-how-to-eliminate-carbon-emissions-then-who-does/",
    "domain": "大厂 AI 动态",
    "title": "If Amazon doesn’t know how to eliminate carbon emissions, then who does?",
    "url": "https://techcrunch.com/2026/09/23/if-amazon-doesnt-know-how-to-eliminate-carbon-emissions-then-who-does/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T21:21:33+00:00",
    "summary": "Amazon is one of the largest companies in the world. How much responsibility does it have to meet its net-zero pledge?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/vc-firm-bessemer-now-has-another-5-75b-to-invest-in-what-else-ai/",
    "domain": "大厂 AI 动态",
    "title": "VC firm Bessemer now has another $5.75B to invest in (what else?) AI",
    "url": "https://techcrunch.com/2026/09/23/vc-firm-bessemer-now-has-another-5-75b-to-invest-in-what-else-ai/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T20:35:17+00:00",
    "summary": "The VC firm says that AI-native companies are growing faster than any technology, ever."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/enveda-secures-311m-to-bring-more-nature-derived-ai-drugs-into-clinical-trials/",
    "domain": "大厂 AI 动态",
    "title": "Enveda secures $311M to bring more nature-derived AI drugs into clinical trials",
    "url": "https://techcrunch.com/2026/09/23/enveda-secures-311m-to-bring-more-nature-derived-ai-drugs-into-clinical-trials/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T19:31:28+00:00",
    "summary": "The round valued the AI biotech at $2 billion. It is currently testing drugs that treat skin conditions and preserve weight loss after stopping GLP-1s."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/modal-motors-is-trying-to-cut-china-out-of-electric-motors-entirely/",
    "domain": "大厂 AI 动态",
    "title": "Modal Motors is trying to cut China out of electric motors entirely",
    "url": "https://techcrunch.com/2026/09/23/modal-motors-is-trying-to-cut-china-out-of-electric-motors-entirely/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T19:05:00+00:00",
    "summary": "The startup is working on small, light motors with no rare-earth magnets that are suited for drones, fans, and robots."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/disney-and-hulu-add-to-the-growing-trend-of-streaming-inflation/",
    "domain": "大厂 AI 动态",
    "title": "Disney+ and Hulu add to the growing trend of streaming inflation",
    "url": "https://techcrunch.com/2026/09/23/disney-and-hulu-add-to-the-growing-trend-of-streaming-inflation/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T18:06:27+00:00",
    "summary": "At the same time, Disney appears to be exploring new ways to expand its streaming business beyond simply raising subscription prices."
  },
  {
    "id": "rss:https://techcrunch.com/video/the-old-cybersecurity-model-is-breaking/",
    "domain": "大厂 AI 动态",
    "title": "The old cybersecurity model is breaking",
    "url": "https://techcrunch.com/video/the-old-cybersecurity-model-is-breaking/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T17:44:02+00:00",
    "summary": "As concern over AI safety and rogue agents continue to make headlines, it’s no surprise that cybersecurity stocks are rising, or that investors are pouring massive amounts of capital into startups try"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/zoox-grounds-atlanta-test-fleet-after-workers-report-toxic-gas-exposure-symptoms/",
    "domain": "大厂 AI 动态",
    "title": "Zoox grounds Atlanta test fleet after workers report toxic gas exposure symptoms",
    "url": "https://techcrunch.com/2026/09/23/zoox-grounds-atlanta-test-fleet-after-workers-report-toxic-gas-exposure-symptoms/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T17:28:38+00:00",
    "summary": "The repeated incidents led one worker to file a complaint with the Occupational Safety and Health Administration, which opened an inquiry and told Zoox to investigate the exposures."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/chatgpt-mobile-app-gets-voice-based-agentic-features/",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT mobile app gets voice-based agentic features",
    "url": "https://techcrunch.com/2026/09/23/chatgpt-mobile-app-gets-voice-based-agentic-features/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T17:00:00+00:00",
    "summary": "Pro and Plus users will be able to use the Work tab on their phones to complete agentic tasks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/even-americans-who-use-ai-every-day-are-worried-about-it/",
    "domain": "大厂 AI 动态",
    "title": "Even Americans who use AI every day are worried about it",
    "url": "https://techcrunch.com/2026/09/23/even-americans-who-use-ai-every-day-are-worried-about-it/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T16:49:58+00:00",
    "summary": "The report suggests that greater exposure will not resolve the unease around the technology, nor reduce public support for AI regulation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/youtube-is-making-comments-more-fun-and-fandom-more-lucrative-for-creators/",
    "domain": "大厂 AI 动态",
    "title": "YouTube is making comments more fun — and fandom more lucrative for creators",
    "url": "https://techcrunch.com/2026/09/23/youtube-is-making-comments-more-fun-and-fandom-more-lucrative-for-creators/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T16:03:44+00:00",
    "summary": "YouTube is rolling out GIF replies, voice-powered TV comments, personalized moderation, paid members-only communities, and new ways for fans to support their favorite creators."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/youtubes-conversational-video-editing-tool-lets-creators-make-edits-in-natural-language/",
    "domain": "大厂 AI 动态",
    "title": "YouTube’s conversational video editing tool lets creators make edits in natural language",
    "url": "https://techcrunch.com/2026/09/23/youtubes-conversational-video-editing-tool-lets-creators-make-edits-in-natural-language/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T15:46:57+00:00",
    "summary": "Creators will be able to use AI in a conversational chat interface to help them edit videos."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/youtube-music-gets-more-conversational-with-new-ai-features/",
    "domain": "大厂 AI 动态",
    "title": "YouTube Music gets more conversational with new AI features",
    "url": "https://techcrunch.com/2026/09/23/youtube-music-gets-more-conversational-with-new-ai-features/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T15:19:30+00:00",
    "summary": "Built directly into the YouTube Music app, Ask Music lets users describe what they want to hear in everyday language rather than searching for individual songs or artists."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/eight-sleeps-new-pod-6-comes-in-smaller-and-solo-sizes-starting-at-1999/",
    "domain": "大厂 AI 动态",
    "title": "Eight Sleep’s new Pod 6 comes in smaller and solo sizes, starting at $1,999",
    "url": "https://techcrunch.com/2026/09/23/eight-sleeps-new-pod-6-comes-in-smaller-and-solo-sizes-starting-at-1999/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T14:45:00+00:00",
    "summary": "Eight Sleep said the new pod is 20% faster than the previous generation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/23/youtube-releases-new-ai-features-for-creators-within-its-studio-app/",
    "domain": "大厂 AI 动态",
    "title": "YouTube releases new AI features for creators within its Studio app",
    "url": "https://techcrunch.com/2026/09/23/youtube-releases-new-ai-features-for-creators-within-its-studio-app/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T14:30:00+00:00",
    "summary": "YouTube is adding new features to generate ideas and monitor the performance of thumbnails."
  },
  {
    "id": "rss:https://stratechery.com/2026/more-on-muse-amazon-and-walmart-muse-and-expedia-whither-google/",
    "domain": "大厂 AI 动态",
    "title": "More on Muse, Amazon, and Walmart; Muse and Expedia; Whither Google?",
    "url": "https://stratechery.com/2026/more-on-muse-amazon-and-walmart-muse-and-expedia-whither-google/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T10:00:00+00:00",
    "summary": "Meta needs Walmart to wait out Amazon; Expedia seeks to keep its middleware position; meanwhile, where is Google?"
  },
  {
    "id": "rss:https://stratechery.com/2026/amazon-blocks-muse-amazons-moat-aggregator-v-aggregator/",
    "domain": "大厂 AI 动态",
    "title": "Amazon Blocks Muse, Amazon’s Moat, Aggregator v Aggregator",
    "url": "https://stratechery.com/2026/amazon-blocks-muse-amazons-moat-aggregator-v-aggregator/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T10:00:00+00:00",
    "summary": "Amazon predictably blocked Muse, but there is room for a deal based on the reality that Amazon's physical world investments are an AI moat."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/rfk-jr-s-cdc-isnt-letting-states-order-covid-19-shots-for-kids-blocking-access/",
    "domain": "大厂 AI 动态",
    "title": "RFK Jr.'s CDC isn’t letting states order COVID-19 shots for kids, blocking access",
    "url": "https://arstechnica.com/health/2026/09/rfk-jr-s-cdc-isnt-letting-states-order-covid-19-shots-for-kids-blocking-access/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T22:17:25+00:00",
    "summary": "US health deptartment said it wants to ensure the vaccine orders are \"appropriate.\""
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/fbi-rushes-to-investigate-if-shinyhunters-hack-of-thousands-of-employees-is-real/",
    "domain": "大厂 AI 动态",
    "title": "FBI rushes to investigate if ShinyHunters hack of thousands of employees is real",
    "url": "https://arstechnica.com/tech-policy/2026/09/fbi-rushes-to-investigate-if-shinyhunters-hack-of-thousands-of-employees-is-real/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T21:46:36+00:00",
    "summary": "It's unclear what will happen if FBI misses ShinyHunters' deadline."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/09/disney-and-hulu-raise-prices-by-up-to-13-percent-after-doubling-profits/",
    "domain": "大厂 AI 动态",
    "title": "Disney+ and Hulu raise prices by up to 13 percent after doubling profits",
    "url": "https://arstechnica.com/gadgets/2026/09/disney-and-hulu-raise-prices-by-up-to-13-percent-after-doubling-profits/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T21:18:53+00:00",
    "summary": "The Disney+ ad-free plan is now more expensive than Netflix's."
  },
  {
    "id": "hn:49691343",
    "domain": "股票",
    "title": "Nike exits the S&P 100 after 18 years and a $200B market-cap wipeout",
    "url": "https://fortune.com/2026/09/08/nike-stock-plummets-sp500-market-cap-index/",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 316,
    "published_at": "2026-09-14T02:50:40+00:00",
    "summary": ""
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
    "id": "hn:49682946",
    "domain": "股票",
    "title": "Show HN: Analyst Index – analysts who make money telling you good stock calls",
    "url": "https://www.analystidx.com/",
    "source": "haichuan",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-13T11:50:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49672197",
    "domain": "股票",
    "title": "Larry Ellison to sell up to $7.5B worth of Oracle stock",
    "url": "https://www.ft.com/content/25b1abb0-790f-4315-9b0c-530d959a086f",
    "source": "potatobox",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-12T13:37:21+00:00",
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
    "id": "hn:49451482",
    "domain": "股票",
    "title": "Hackers Broke into Justice Department, NASA, Federal Reserve, Senate",
    "url": "https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-platforms-operated-and-used-china-state-sponsored-hackers",
    "source": "2OEH8eoCRo0",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-26T16:05:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49450370",
    "domain": "股票",
    "title": "Chinese Hackers Broke into Justice Department, NASA, Federal Reserve, Senate",
    "url": "https://www.reuters.com/world/china/china-sponsored-hacking-platforms-seized-by-us-justice-department-says-2026-08-26/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-26T14:59:43+00:00",
    "summary": ""
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
    "id": "hn:49778029",
    "domain": "金融",
    "title": "Samsung is expected to more than double output of its HBM4 and HBM4E DRAM",
    "url": "https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 559,
    "published_at": "2026-09-20T17:38:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49686766",
    "domain": "金融",
    "title": "I'm being cyberattacked by Tesla, Inc",
    "url": "https://dreamstation.systems/personal/tesla.html",
    "source": "robinpie",
    "platform": "hackernews",
    "points": 458,
    "published_at": "2026-09-13T18:03:09+00:00",
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
    "points": 199,
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
    "id": "rss:https://arxiv.org/abs/2609.26861",
    "domain": "金融",
    "title": "Rule-Based Pricing Algorithms and Market Outcomes: An Experimental Study",
    "url": "https://arxiv.org/abs/2609.26861",
    "source": "Adrian Hillenbrand, Hans-Theo Normann, Matthias Potarca, Tobias Werner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.26861v1 Announce Type: new Abstract: Rule-based pricing tools are widespread in digital commerce, yet we know little about how their design shapes market outcomes. In a controlled market ex"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.27024",
    "domain": "金融",
    "title": "Loss Choice or Model Choice? The Role of Forecast Level in Cryptocurrency Volatility Forecasting",
    "url": "https://arxiv.org/abs/2609.27024",
    "source": "Andrzej Tokajuk, Jaros{\\l}aw A. Chudziak",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.27024v1 Announce Type: new Abstract: Volatility forecasts play a central role in financial risk management because their overall level and day-to-day movements affect downstream decisions. "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.27113",
    "domain": "金融",
    "title": "Active Portfolio Management in Concentrated Equity Markets",
    "url": "https://arxiv.org/abs/2609.27113",
    "source": "Brian Ceco, Xiaofei Shi, Ting-Kam Leonard Wong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.27113v1 Announce Type: new Abstract: The equal-weighted portfolio is a passive, rule-based strategy that has historically been difficult to outperform, delivering higher returns than the ca"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.27138",
    "domain": "金融",
    "title": "Surface-Driven Stochastic Volatility for Commodity Options: Identification of Stochastic Vol-of-Vol and Leverage from Smile Dynamics",
    "url": "https://arxiv.org/abs/2609.27138",
    "source": "Arthur Steve Tchoneteck, Tingjia Zhang, Frederi Viens",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.27138v1 Announce Type: new Abstract: Commodity option surfaces contain information beyond the at-the-money volatility level. We develop a surface-driven stochastic-volatility framework for "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.27404",
    "domain": "金融",
    "title": "When Trust Attracts Fraud: AI and Trust Arbitrage",
    "url": "https://arxiv.org/abs/2609.27404",
    "source": "Xieyu Yin, Fenghua Wen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.27404v1 Announce Type: new Abstract: Trust can attract fraud when it delays verification. We develop a two-market signaling model in which generative AI lowers fabrication, verification, an"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.27632",
    "domain": "金融",
    "title": "Compliant AI Infrastructure for Regulated Finance: A tiered multi-agent framework with DLT audit trails for financial operations in DACH",
    "url": "https://arxiv.org/abs/2609.27632",
    "source": "Walter Kurz, Reinhard Magg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.27632v1 Announce Type: new Abstract: We present a compliance-first architecture for AI in regulated finance that treats regulation as an orientation layer rather than a deterministic rulese"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.27636",
    "domain": "金融",
    "title": "Multi-Agent AI Architecture for Regulated Insurers: A generic AI framework under Solvency II and the AI Act in Austria and Germany",
    "url": "https://arxiv.org/abs/2609.27636",
    "source": "Walter Kurz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.27636v1 Announce Type: new Abstract: This paper proposes a formal multi-agent architecture for implementing enterprise AI in regulated insurance firms, integrating economic theory with inst"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.27686",
    "domain": "金融",
    "title": "Mining Meaning: Measurement Error in AI-Assisted Literature Reviews",
    "url": "https://arxiv.org/abs/2609.27686",
    "source": "Jeffrey D. Michler, Kieran Douglas, Anna Josephson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.27686v1 Announce Type: new Abstract: Researchers increasingly use generative AI, particularly large language models (LLMs), to automate tasks across the research pipeline. We study the reli"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.27727",
    "domain": "金融",
    "title": "Sovereign Grassroots Currencies: A CBDC Architecture for Credit and Monetary Policy (Full Version)",
    "url": "https://arxiv.org/abs/2609.27727",
    "source": "Ehud Shapiro",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.27727v1 Announce Type: new Abstract: A Central Bank Digital Currency (CBDC) is central-bank money in digital form, held by the public. Leading designs have two limitations: conversion from "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.27732",
    "domain": "金融",
    "title": "Do Drug Consumption Rooms Reduce Drug-Related Hospitalizations? Evidence from Switzerland",
    "url": "https://arxiv.org/abs/2609.27732",
    "source": "Ana Armendariz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.27732v1 Announce Type: new Abstract: This paper estimates the causal effect of drug consumption room (DCR) openings on drug-related hospitalizations in Switzerland. I exploit the staggered "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.27785",
    "domain": "金融",
    "title": "Financial Tail Risk Beyond Lipschitz Continuity via Semi-Discrete Optimal Transport",
    "url": "https://arxiv.org/abs/2609.27785",
    "source": "Ryan M. Engel, Kibaek Lee, Namid Stillman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.27785v1 Announce Type: new Abstract: Financial returns are heavy-tailed, and accurate tail risk estimation is central to portfolio risk management. Modern neural generators sample by pushin"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.27786",
    "domain": "金融",
    "title": "Feasible Multi-Asset Optimal Execution under Cash Constraints",
    "url": "https://arxiv.org/abs/2609.27786",
    "source": "Ryuji Hashimoto, Namid R. Stillman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.27786v1 Announce Type: new Abstract: Optimal execution (OE) in multi-asset settings involves complex interactions across assets, particularly through shared capital constraints during portf"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.28372",
    "domain": "金融",
    "title": "Shopping by algorithm: How agentic AI deploys human heuristics as a surrogate consumer",
    "url": "https://arxiv.org/abs/2609.28372",
    "source": "Davood Wadi, Yu Ma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.28372v1 Announce Type: new Abstract: Consumers increasingly delegate purchasing decisions to Large Language Models (LLMs) acting as surrogate consumers. Using \"Tool-Lab,\" an adaptation of i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.28463",
    "domain": "金融",
    "title": "Market Completeness and Optional Projections under Restricted Information",
    "url": "https://arxiv.org/abs/2609.28463",
    "source": "Levin David Schwab",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.28463v1 Announce Type: new Abstract: In a finite discrete-time market, trading decisions may be predictable with respect to a filtration that does not adapt asset prices. The first fundamen"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.26398",
    "domain": "金融",
    "title": "Weighted universal Value-at-Risk Superadditivity for discrete distributions",
    "url": "https://arxiv.org/abs/2609.26398",
    "source": "Alfred M\\\"uller",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.26398v1 Announce Type: cross Abstract: The concept of weighted universal Value-at-Risk superadditivity (WUVS) was recently introduced by Chen et al. (2026) as a generalization of the questi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.27107",
    "domain": "金融",
    "title": "Local Weak Limits for Equilibrium and Risk in Economic Networks",
    "url": "https://arxiv.org/abs/2609.27107",
    "source": "Hamed Amini, Zhecheng Wu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.27107v1 Announce Type: cross Abstract: We study equilibrium and risk evaluation in large sparse economic networks with heterogeneous responses, shocks, and bilateral exposures. Our approach"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.27614",
    "domain": "金融",
    "title": "Model-agnostic noise reduction for high-dimensional time series data",
    "url": "https://arxiv.org/abs/2609.27614",
    "source": "Bram Wouters, Cees Diks",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.27614v1 Announce Type: cross Abstract: We develop a model-agnostic framework for noise reduction in high-dimensional time series that explicitly targets optimal recovery of a low-dimensiona"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.27654",
    "domain": "金融",
    "title": "FedIncome: Federated Learning for Income Estimation in Digital Lending Under Data Sovereignty Constraints",
    "url": "https://arxiv.org/abs/2609.27654",
    "source": "Sultan Amed, Tanmay Sen, Sayantan Banerjee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.27654v1 Announce Type: cross Abstract: Verified income is often unavailable in digital loan applications, forcing lenders to rely on reported income and potentially leading to over-lending,"
  },
  {
    "id": "rss:https://arxiv.org/abs/2505.08623",
    "domain": "金融",
    "title": "Rough Bergomi turns grey",
    "url": "https://arxiv.org/abs/2505.08623",
    "source": "Antoine Jacquier, Adriano Oliveri Orioles, Zan Zuric",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2505.08623v2 Announce Type: replace Abstract: We propose a tractable extension of the rough Bergomi model, replacing the fractional Brownian motion with a generalised grey Brownian motion, which"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.21115",
    "domain": "金融",
    "title": "Asset price bubbles under model uncertainty and short-sale constraints: A discrete-time analysis",
    "url": "https://arxiv.org/abs/2512.21115",
    "source": "Wenqing Zhang, Lin Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2512.21115v3 Announce Type: replace Abstract: In this study, we investigate asset price bubbles in a discrete-time, discrete-state market under model uncertainty and short-sale constraints. Usin"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.06499",
    "domain": "金融",
    "title": "Cross-Market Alpha: Testing Short-Term Trading Factors in the U.S. Market via Double-Selection LASSO",
    "url": "https://arxiv.org/abs/2601.06499",
    "source": "Jin Du, Alexander Walter, Maxim Ulrich",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2601.06499v3 Announce Type: replace Abstract: We test whether 168 short-horizon price-volume signals from the Alpha191 library, originally developed for China's retail-dominated A-share market, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.15177",
    "domain": "金融",
    "title": "Optimal investment under capital gains taxes",
    "url": "https://arxiv.org/abs/2602.15177",
    "source": "Alexander Dimitrov, Christoph K\\\"uhn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2602.15177v2 Announce Type: replace Abstract: We generalize classical existence results for expected utility maximization in discrete time frictionless market models to models with capital gains"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09003",
    "domain": "金融",
    "title": "Proof of Stake economy under centralized exchanges--a mean field model",
    "url": "https://arxiv.org/abs/2606.09003",
    "source": "Wenpin Tang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2606.09003v2 Announce Type: replace Abstract: We consider the interaction between centralized trading and decentralized Proof of Stake (PoS) blockchain ecosystems. Motivated by the increasing do"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.13618",
    "domain": "金融",
    "title": "A Declining CVaR Glidepath Framework for Target-Date Fund Design with an Application to the Chilean Pension System",
    "url": "https://arxiv.org/abs/2606.13618",
    "source": "Israel Mu\\~noz, Fernando Su\\'arez, Omar Larr\\'e, Arturo Cifuentes",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2606.13618v2 Announce Type: replace Abstract: We propose a framework for designing Target-Date Funds (TDFs) around an explicit return objective while controlling risk directly at the portfolio l"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.01561",
    "domain": "金融",
    "title": "Decomposing Wage Stagnation: Employment Reallocation, Wage Structure,and Demographics",
    "url": "https://arxiv.org/abs/2607.01561",
    "source": "Ken Yamada",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2607.01561v2 Announce Type: replace Abstract: Japan's average log real hourly wages rose until the mid-1990s, declined through the mid-2010s, and partially recovered thereafter. This paper decom"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.13340",
    "domain": "金融",
    "title": "Fee Implied Volatility on Uniswap v3: A DEX Native Proxy and Its Limits",
    "url": "https://arxiv.org/abs/2608.13340",
    "source": "Amy Oumayma Khaldoun",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2608.13340v2 Announce Type: replace Abstract: Narrow Uniswap v3 liquidity ranges resemble short dated options, and Panoptic's streaming premium echoes the short maturity concentration of Black-S"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.05047",
    "domain": "金融",
    "title": "Gatheral's Conjecture Revisited",
    "url": "https://arxiv.org/abs/2609.05047",
    "source": "Vladimir Lucic",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.05047v4 Announce Type: replace Abstract: We consider the Heston model with perfect negative spot--variance correlation and its one-dimensional local-volatility projection. Let $I_T^{\\mathrm"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.12976",
    "domain": "金融",
    "title": "Complements or Substitutes? Technology Adoption and Clinical Care Utilization: Evidence from Automated Insulin Delivery",
    "url": "https://arxiv.org/abs/2609.12976",
    "source": "Moslem Rashidi, Cristina Ugolini, Gianluca Fiorentini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T04:00:00+00:00",
    "summary": "arXiv:2609.12976v2 Announce Type: replace Abstract: Whether medical technology reduces or increases demand for professional care is central to understanding its effects on healthcare utilization and c"
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
    "id": "hn:49439296",
    "domain": "金融",
    "title": "A brief history of federal lift ticket regulation",
    "url": "https://zakpodmore.substack.com/p/a-brief-history-of-federal-lift-ticket",
    "source": "CGMthrowaway",
    "platform": "hackernews",
    "points": 69,
    "published_at": "2026-08-25T19:25:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49731515",
    "domain": "金融",
    "title": "Fed Raises Rates for First Time in Three Years",
    "url": "https://www.wsj.com/economy/central-banking/fed-raises-rates-for-first-time-in-three-years-08539fbe",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-09-16T19:09:22+00:00",
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
    "id": "hn:49730731",
    "domain": "金融",
    "title": "Fed Raises Rates as Warsh Bucks Trump to Contain Inflation",
    "url": "https://www.bloomberg.com/news/articles/2026-09-16/fed-raises-rates-as-warsh-bucks-trump-to-contain-inflation",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-09-16T18:05:30+00:00",
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
    "id": "hn:49432102",
    "domain": "金融",
    "title": "Nostr vs. Fediverse vs. Bluesky: A Comparison of Decentralized Social Protocols",
    "url": "https://soapbox.pub/blog/comparing-protocols",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-08-25T11:27:51+00:00",
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
    "id": "hn:49667360",
    "domain": "金融",
    "title": "A Decade of Hype, 3k Roofs, and One Redirect URL: Tesla Kills the Solar Roof",
    "url": "https://www.gadgetreview.com/a-decade-of-hype-3000-roofs-and-one-redirect-url-tesla-kills-the-solar-roof",
    "source": "upofadown",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-09-12T00:38:23+00:00",
    "summary": ""
  }
]
```
