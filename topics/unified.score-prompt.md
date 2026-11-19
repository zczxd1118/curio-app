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

- 今日日期：`2026-11-19`
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
  "date": "2026-11-19",
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
    "points": 2267502,
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
    "points": 2136546,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 1552127,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1504561,
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
    "points": 1477981,
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
    "points": 915361,
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
    "points": 905488,
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
    "points": 758103,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 597117,
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
    "points": 482665,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 435885,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 433592,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 428505,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 361593,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 358808,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 329932,
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
    "points": 301783,
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
    "points": 237037,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1TTR8BaEnL",
    "domain": "AI",
    "title": "Claude Code 零基础终极教程：安装、换模型、插件、Hooks、Skills、Subagents、实战项目一次讲透！",
    "url": "http://www.bilibili.com/video/av116529475622752",
    "source": "木子不写代码",
    "platform": "bilibili",
    "points": 215498,
    "published_at": "2026-05-07T08:00:00+00:00",
    "summary": "这是你能看到的最完整的 Claude Code 零基础系统教程。\n\n\n我们将深度拆解：\n\n1️⃣ 基础入门：安装、第三方模型接入、权限系统。\n\n2️⃣ 核心进阶：Tools、Hooks、Skills、Subagents 及自动化流程。\n\n3️⃣ 项目实战：从零构建一个真实可用的 AI 网页 App。\n\n\n视频跟到最后，你不只是学会写代码，而是掌握 AI 智能体的工作逻辑。我是木子，只提供 AI 时"
  },
  {
    "id": "bvid:BV15XDfBSE2t",
    "domain": "AI",
    "title": "ClaudeCode平替:OpenCode详细使用教程看这一个就够了（内含超详细安装文档+软件安装包）",
    "url": "http://www.bilibili.com/video/av116379604881806",
    "source": "鹏哥C语言",
    "platform": "bilibili",
    "points": 210019,
    "published_at": "2026-04-13T09:00:00+00:00",
    "summary": "opencodeopencode使用全攻略opencode教程opencode和claudecodeopencode使用技巧opencode实战opencode coworkopencode安装opencode开发opencode使用教程opencode教程opencode安装教程opencode使用全攻略opencode和claudecodeopencode skillsopencode插件op"
  },
  {
    "id": "bvid:BV1h3W76wEem",
    "domain": "AI",
    "title": "Claude(Code)桌面APP，保姆级全攻略，一期视频精通，顶级Agent软件长什么样？",
    "url": "http://www.bilibili.com/video/av117580048108571",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 193245,
    "published_at": "2026-11-08T09:14:07+00:00",
    "summary": "最近Claude桌面端（Claude Desktop） 有了一大波功能更新。随着一步步的迭代，它已经把 Claude Code 的编程、Claude Design 的设计，以及 Claude Cowork 的办公等核心能力，全部收入了同一个桌面客户端，特别是Claude Code已经从原本黑乎乎的命令行工具，进化成了桌面客户端的完全体形态。再搭配上超强的Opus5.5 模型，已经能称得上是地表顶级"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 187281,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1sZMq6qEko",
    "domain": "AI",
    "title": "从0做出你的第一个App ｜ 零基础AI编程保姆教程",
    "url": "http://www.bilibili.com/video/av117038647352026",
    "source": "木子不写代码",
    "platform": "bilibili",
    "points": 181935,
    "published_at": "2026-08-07T12:15:00+00:00",
    "summary": "这期视频，我会手把手带你，用 AI 做出你的第一个 App。\n全程假设你没有任何编程和AI的基础，\n我们从如何写需求提示词开始，\n到确定页面结构和设计，\n产品需求文档，\n开发计划，\n第一版APP验收，\ngit代码存档，\n二次开发，\n界面美化，\n做好的APP也会开源给到大家，\n我也会演示如何获取这个项目源代码并且用AI继续定制开发，\n视频到最后，\n你会收获一个为自己的工作和生活定制的专属APP！\n和"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 166424,
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
    "points": 163913,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1b5AeeGEFc",
    "domain": "AI",
    "title": "Cursor太贵？分享三个免费AI编程方案+海量编程技巧【如何看待AI编程】",
    "url": "http://www.bilibili.com/video/av114025056699722",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 162131,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1eYPpeWEnT",
    "domain": "AI",
    "title": "Cursor + MCP = 王炸！彻底颠覆我的Cursor工作流，效率直接起飞",
    "url": "http://www.bilibili.com/video/av114073660301264",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 151865,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 116634,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 99480,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 94360,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1cVW86JE2e",
    "domain": "AI",
    "title": "Vibe Coding 完不会获客？我用 AI 做了一个「营销数据库」！【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av117587245599812",
    "source": "熠辉IndieDev",
    "platform": "bilibili",
    "points": 76114,
    "published_at": "2026-11-10T01:00:00+00:00",
    "summary": "产品做出来了，第一批用户去哪找？我用两个月做了 BizPeel，收录700多个公开营收的产品，拆解真实获客动作。本期演示在 Google Antigravity 接入 BizPeel MCP，由 Gemini 4 Argon 查找同类产品、整理增长实验；报告生成时用 Gemini Flash 清洗数据，再由 Gemini 4 Argon 撰写。\n\n注： 部分Google技术仅适用于出海场景。"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 60543,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 57050,
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
    "points": 50614,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 46813,
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。"
  },
  {
    "id": "bvid:BV1hxMbzqEzU",
    "domain": "AI",
    "title": "小智MCP自由了！我开源了个命令行神器实现多MCP聚合",
    "url": "http://www.bilibili.com/video/av114686414625640",
    "source": "闪电蘑菇",
    "platform": "bilibili",
    "points": 43662,
    "published_at": "2025-06-15T08:31:55+00:00",
    "summary": "- 我写的小智客户端命令行工具\n - github: https://github.com/shenjingnan/xiaozhi-client\n - gitee: https://gitee.com/shenjingnan/xiaozhi-client\n\n- 小智官方MCP示例代码仓库：\n - github: https://github.com/78/mcp-calculator\n - git"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 41505,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 41315,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34717,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1uwxG6DEra",
    "domain": "AI",
    "title": "3分钟讲透：Vibe Coding如何避免💩屎山代码",
    "url": "http://www.bilibili.com/video/av117513727838880",
    "source": "鲤哥builder",
    "platform": "bilibili",
    "points": 31074,
    "published_at": "2026-10-27T16:09:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29984,
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
    "points": 29073,
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
    "points": 27026,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1FQsu6oEGB",
    "domain": "AI",
    "title": "Claude Fable 5.2：老大我们拿这个IPO真的能赚钱吗？ | AI 前端/3D 能力测试",
    "url": "http://www.bilibili.com/video/av117630329626222",
    "source": "无机酸-_-",
    "platform": "bilibili",
    "points": 25329,
    "published_at": "2026-11-17T06:31:04+00:00",
    "summary": "测试结果均在 https://gallery.arenaofbias.icu/#/ 上可浏览。测试排行榜来源于亿模亿样的双盲测试，欢迎大家前往 https://gallery.arenaofbias.icu/#/ 参与提问、上传结果与双盲测试，共同建造可维护的、贴合实践的 AI 前端/3D 测试基准！\n\nQQ交流群一群：1105331319（已满） 二群：763499012（已满） 三群：7715"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22864,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV17YsJ6UEnW",
    "domain": "AI",
    "title": "国内稳定使用 Claude Code 保姆级教程-3 步搞定",
    "url": "http://www.bilibili.com/video/av117619675890528",
    "source": "小杨同学-毕业辅导",
    "platform": "bilibili",
    "points": 22298,
    "published_at": "2026-11-15T09:15:58+00:00",
    "summary": "实测稳定使用半个多月、零封号（个人经验，仅供参考）。\n这期分享我在国内使用 Claude Code 的完整流程，以及用了半年 Codex 之后转到 Claude 的真实感受。"
  },
  {
    "id": "bvid:BV1f57C6YErb",
    "domain": "AI",
    "title": "手把手教你Codex安装和使用MCP！新手必备~",
    "url": "http://www.bilibili.com/video/av116696861907147",
    "source": "Raina测试",
    "platform": "bilibili",
    "points": 19694,
    "published_at": "2026-06-06T11:29:00+00:00",
    "summary": "这一期给大家分享下在codex里面如何配置和使用MCP，和skill一样，MCP也是我们平时用得比较多的，所以建议大家也可以学一下它的基础配置和使用~\n步骤都不难，跟着操作就可以了"
  },
  {
    "id": "bvid:BV1rvW761E7x",
    "domain": "AI",
    "title": "【全748集】目前B站最细最全的AI Agent搭建零基础全套教程，2026最新版，手把手教你搭建企业级Agent智能体！学完即可就业！让你少走99%弯路！！",
    "url": "http://www.bilibili.com/video/av117579779742632",
    "source": "Agent产品",
    "platform": "bilibili",
    "points": 19277,
    "published_at": "2026-11-08T08:11:42+00:00",
    "summary": "【全748集】目前B站最细最全的AI Agent搭建零基础全套教程，2026最新版，手把手教你搭建企业级Agent智能体！学完即可就业！让你少走99%弯路！！"
  },
  {
    "id": "bvid:BV1uaWq6JEEa",
    "domain": "AI",
    "title": "【ClaudeCode】这绝对是b站讲的最好的Claude Code保姆级全套教程，2027最新版，包含所有干货！七天就能从小白到大神！学完即就业，玩转AI技术",
    "url": "http://www.bilibili.com/video/av117608149945028",
    "source": "AI大模型技术",
    "platform": "bilibili",
    "points": 18210,
    "published_at": "2026-11-13T08:25:56+00:00",
    "summary": "视频制作不易，如果视频对你有用的话请一键三连【长按点赞】支持一下up哦，拜托，这真的对我很重要！"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 16664,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "hn:50459703",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is preparing to oust Jensen Huang",
    "url": "https://www.wsj.com/business/nvidia-is-preparing-to-oust-nvidia-ceo-jensen-huang-30f421ad",
    "source": "jbredeche",
    "platform": "hackernews",
    "points": 1227,
    "published_at": "2026-11-11T22:31:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50493251",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia allegedly engineered scarcity by funding AI startups to buy its GPUs",
    "url": "https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus",
    "source": "speckx",
    "platform": "hackernews",
    "points": 1114,
    "published_at": "2026-11-14T02:52:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:50418016",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang's letter to staff about affair",
    "url": "https://nvidianews.nvidia.com/news/a-message-to-our-company",
    "source": "karimf",
    "platform": "hackernews",
    "points": 988,
    "published_at": "2026-11-08T22:20:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:50477231",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia employees petition to bring back Jensen Huang",
    "url": "https://www.wired.com/story/nvidia-employees-petition-for-jensen-huangs-return/",
    "source": "lavendermon",
    "platform": "hackernews",
    "points": 819,
    "published_at": "2026-11-13T02:16:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:50534631",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia stopped disclosing Singapore sales as revenues hit $104B",
    "url": "https://www.ft.com/content/dbde7a30-548c-4f9d-a4be-7898a0c24dcf",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 664,
    "published_at": "2026-11-17T17:12:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50512235",
    "domain": "AI 算力 / 半导体",
    "title": "What's Next for Nvidia?",
    "url": "https://steveblank.com/2026/11/15/whats-next-for-nvidia/",
    "source": "zdw",
    "platform": "hackernews",
    "points": 485,
    "published_at": "2026-11-15T23:55:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50416801",
    "domain": "AI 算力 / 半导体",
    "title": "Statement from Nvidia board of directors",
    "url": "https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors",
    "source": "vincentchau",
    "platform": "hackernews",
    "points": 495,
    "published_at": "2026-11-08T20:26:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:50473190",
    "domain": "AI 算力 / 半导体",
    "title": "Former Nvidia CEO Huang had a relationship with a second employee, sources say",
    "url": "https://www.reuters.com/technology/former-nvidia-ceo-huang-had-relationship-with-second-employee-sources-say-2026-11-12/",
    "source": "jbredeche",
    "platform": "hackernews",
    "points": 460,
    "published_at": "2026-11-12T19:51:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:50501631",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia deliberately kept GPU prices high through circular financing deals",
    "url": "https://www.techspot.com/news/114558-nvidia-deliberately-kept-gpu-prices-high-through-circular.html",
    "source": "madihaa",
    "platform": "hackernews",
    "points": 452,
    "published_at": "2026-11-14T22:26:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:50487864",
    "domain": "AI 算力 / 半导体",
    "title": "$11.4M in Nvidia hardware vanishes during shipment from CA to TX",
    "url": "https://www.freightwaves.com/news/11-4-million-in-nvidia-hardware-vanishes-during-shipment-from-california-to-texas",
    "source": "crescit_eundo",
    "platform": "hackernews",
    "points": 386,
    "published_at": "2026-11-13T18:40:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:50467132",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang resigns as Nvidia CEO immediately",
    "url": "https://www.reuters.com/live/nvidia-live-board-meets-fate-ceo-jensen-huang-after-affair-reports-2026-11-12/",
    "source": "ksec",
    "platform": "hackernews",
    "points": 375,
    "published_at": "2026-11-12T13:56:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:50518567",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia was in trouble before the Jensen Huang mess",
    "url": "https://www.wired.com/story/nvidia-was-already-in-trouble-before-the-jensen-huang-mess/",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 289,
    "published_at": "2026-11-16T15:24:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:50459776",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia prepares to fire CEO Jensen Huang, WSJ reports",
    "url": "https://twitter.com/watcherguru/status/2120645607866188008",
    "source": "alexmolas",
    "platform": "hackernews",
    "points": 225,
    "published_at": "2026-11-11T22:36:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50492993",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia director sold nearly $1B in stock weeks before the Jensen Huang scandal",
    "url": "https://finance.yahoo.com/markets/stocks/articles/nvidia-director-sold-nearly-1b-160000846.html",
    "source": "LopRabbit",
    "platform": "hackernews",
    "points": 218,
    "published_at": "2026-11-14T02:21:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:50511982",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang might return to Nvidia as CEO",
    "url": "https://www.reuters.com/world/china/jensen-huang-discusses-comeback-nvidia-ceo-with-allies-ft-reports-2026-11-15/",
    "source": "YakubYilmaz",
    "platform": "hackernews",
    "points": 177,
    "published_at": "2026-11-15T23:24:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50467139",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang resigns after reports of second affair deepened scandal",
    "url": "https://www.bbc.co.uk/news/live/c6zjry11v8w1t",
    "source": "cognoboffin",
    "platform": "hackernews",
    "points": 169,
    "published_at": "2026-11-12T13:56:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50509883",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang discusses comeback as Nvidia CEO with allies",
    "url": "https://www.ft.com/content/45383d86-33c4-4d99-86e5-5e058d3567c1",
    "source": "eyalitki",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-11-15T19:31:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:50327058",
    "domain": "AI 算力 / 半导体",
    "title": "Seoul Viosys begins production of rare-earth-free white light emitter",
    "url": "https://www.semiconductor-today.com/news_items/2026/oct/seoul-291026.shtml",
    "source": "gmays",
    "platform": "hackernews",
    "points": 195,
    "published_at": "2026-11-01T16:23:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50497155",
    "domain": "AI 算力 / 半导体",
    "title": "Serving GLM-5.3 at 607.8 tok/s across two Nvidia DGX stations with vLLM",
    "url": "https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/",
    "source": "wondersky",
    "platform": "hackernews",
    "points": 149,
    "published_at": "2026-11-14T14:09:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50479721",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Hacked",
    "url": "https://www.sec.gov/Archives/edgar/data/1046179/000104617926000800/a20261112statementregardin.htm",
    "source": "gmays",
    "platform": "hackernews",
    "points": 115,
    "published_at": "2026-11-13T07:39:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50538942",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Chair Harvey Jones says board doesn't intend to reinstate Huang as CEO",
    "url": "https://www.cnbc.com/2026/11/17/nvidia-nvda-earnings-report-q3-2027.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-11-17T22:08:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:50387738",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Kubernetes Engine (NVKE)",
    "url": "https://github.com/dsx-ai-factory/nvke",
    "source": "gkapur",
    "platform": "hackernews",
    "points": 124,
    "published_at": "2026-11-06T03:16:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50546253",
    "domain": "AI 算力 / 半导体",
    "title": "Dutch resist 'unacceptable' US bid to tighten semiconductor export controls",
    "url": "https://www.politico.eu/article/dutch-resist-unacceptable-us-bid-to-tighten-semiconductor-export-controls-asml/",
    "source": "sergdigon",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-11-18T13:46:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50483391",
    "domain": "AI 算力 / 半导体",
    "title": "The Downfall of Jensen Huang: Nvidia's Greed and Corruption [video]",
    "url": "https://www.youtube.com/watch?v=YYU_geUwQoA",
    "source": "belst",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-11-13T13:45:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50467191",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang resigns after reports of extramarital relationships",
    "url": "https://www.nbcnews.com/tech/tech-news/nvidia-ceo-jensen-huang-resigns-reports-extramarital-relationships-rcna608402",
    "source": "sonabinu",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-11-12T14:00:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:50520867",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia board not considering reinstating Jensen Huang as chief executive",
    "url": "https://www.ft.com/content/e5275763-d7e2-4857-8ac6-6b888111986a",
    "source": "doener",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-11-16T18:17:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:50513876",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Days as an Open Checkbook for the AI Economy Are Numbered",
    "url": "https://www.wsj.com/tech/ai/nvidias-days-as-an-open-checkbook-for-the-ai-economy-are-numbered-90c7b388",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-11-16T04:03:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:50486489",
    "domain": "AI 算力 / 半导体",
    "title": "Arm boss Rene Haas approached in Nvidia CEO search",
    "url": "https://www.ft.com/content/2a64f698-46dd-4178-a3f4-4c5f4c0a0926",
    "source": "bazzmt",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-11-13T17:10:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:50511763",
    "domain": "AI 算力 / 半导体",
    "title": "Huang Discusses Comeback as Nvidia Chief with Allies, FT Says",
    "url": "https://www.bloomberg.com/news/articles/2026-11-15/huang-discusses-comeback-as-nvidia-chief-with-allies-ft-says",
    "source": "nstj",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-11-15T22:53:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:50392256",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia was in 1 in 11 startup rounds over $100M last year",
    "url": "https://datahyena.com/research/a-chipmaker-was-in-one-of-every-eleven-100m-rounds/",
    "source": "ghostfoxgod",
    "platform": "hackernews",
    "points": 82,
    "published_at": "2026-11-06T13:48:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50521575",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. tightens controls on remote access to AI technology amid Nvidia fallout",
    "url": "https://www.npr.org/2026/11/16/nx-s1-6042883/nvidia-jensen-huang-commerce-department",
    "source": "jethronethro",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-11-16T19:09:05+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/nvidia-reports-115-8b-in-quarterly-revenue-under-interim-ceo/",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Reports $115.8B in Quarterly Revenue Under Interim CEO",
    "url": "https://www.eetimes.com/nvidia-reports-115-8b-in-quarterly-revenue-under-interim-ceo/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T10:26:18+00:00",
    "summary": "Strong AI infrastructure demand helped Nvidia revenue and profit as the company deals with leadership changes. The post Nvidia Reports $115.8B in Quarterly Revenue Under Interim CEO appeared first on "
  },
  {
    "id": "rss:https://www.eetimes.com/quantum-stocks-are-headed-for-a-correction-investor-charles-beyrouthy-says/",
    "domain": "AI 算力 / 半导体",
    "title": "Quantum Stocks Are Headed for a Correction, Investor Charles Beyrouthy Says",
    "url": "https://www.eetimes.com/quantum-stocks-are-headed-for-a-correction-investor-charles-beyrouthy-says/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T23:39:34+00:00",
    "summary": "Charles Beyrouthy warns quantum stocks face a correction as investors ignore revenue and tech differences; watch where he sees opportunity next. The post Quantum Stocks Are Headed for a Correction, In"
  },
  {
    "id": "rss:https://www.eetimes.com/beyond-one-turn-how-a-single-chip-multiturn-position-sensor-is-reshaping-actuator-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Beyond One Turn: How a Single-Chip Multiturn Position Sensor Is Reshaping Actuator Design",
    "url": "https://www.eetimes.com/beyond-one-turn-how-a-single-chip-multiturn-position-sensor-is-reshaping-actuator-design/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T15:00:00+00:00",
    "summary": "Discover how advanced multiturn position sensing can transform industrial motion control without the limitations of traditional mechanical solutions. Explore how magnetic sensing technology enables ac"
  },
  {
    "id": "rss:https://www.eetimes.com/qnity-at-one-randy-king-on-shrink-stack-and-the-materials-behind-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Qnity at One: Randy King on Shrink, Stack and the Materials Behind AI",
    "url": "https://www.eetimes.com/qnity-at-one-randy-king-on-shrink-stack-and-the-materials-behind-ai/",
    "source": "Randal King, Senior Vice President and Chief Technology and Sustainability Officer, Qnity",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T14:00:00+00:00",
    "summary": "Qnity CTO Randy King on year one as an independent company, shrink-and-stack chips and the materials challenges of advanced packaging for AI. The post Qnity at One: Randy King on Shrink, Stack and the"
  },
  {
    "id": "rss:https://www.eetimes.com/koduri-oxmiq-offers-ip-tools-for-indian-teams-to-design-ai-chips/",
    "domain": "AI 算力 / 半导体",
    "title": "Koduri’s Oxmiq Offers IP, Tools for Indian Teams to Design AI Chips",
    "url": "https://www.eetimes.com/koduri-oxmiq-offers-ip-tools-for-indian-teams-to-design-ai-chips/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T13:30:00+00:00",
    "summary": "India's AI infrastructure needs could exceed 6 GW by 2030. Oxmiq Labs CEO Raja Koduri explains why domestic chip design and custom systems matter. The post Koduri’s Oxmiq Offers IP, Tools for Indian T"
  },
  {
    "id": "rss:https://www.eetimes.com/edge-ai-moves-agricultural-intelligence-from-the-cloud-to-the-field/",
    "domain": "AI 算力 / 半导体",
    "title": "Edge AI Moves Agricultural Intelligence from the Cloud to the Field",
    "url": "https://www.eetimes.com/edge-ai-moves-agricultural-intelligence-from-the-cloud-to-the-field/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T06:59:00+00:00",
    "summary": "NXP and Nvidia tackle the challenges of delivering computing power, energy efficiency, and safety as agricultural machinery becomes autonomous. The post Edge AI Moves Agricultural Intelligence from th"
  },
  {
    "id": "rss:https://www.eetimes.com/marc-hijink-on-asmls-culture-supply-chain-and-geopolitics/",
    "domain": "AI 算力 / 半导体",
    "title": "Marc Hijink on ASML’s Culture, Supply Chain, and Geopolitics",
    "url": "https://www.eetimes.com/marc-hijink-on-asmls-culture-supply-chain-and-geopolitics/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T22:37:22+00:00",
    "summary": "Explore how ASML’s partner-driven culture, EUV dominance, and geopolitical pressures reshaped chipmaking in Marc Hijink’s interview. The post Marc Hijink on ASML’s Culture, Supply Chain, and Geopoliti"
  },
  {
    "id": "rss:https://www.eetimes.com/everspin-looks-to-broaden-mram-adoption-with-lpddr-standard/",
    "domain": "AI 算力 / 半导体",
    "title": "Everspin Looks to Broaden MRAM Adoption with LPDDR Standard",
    "url": "https://www.eetimes.com/everspin-looks-to-broaden-mram-adoption-with-lpddr-standard/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T17:26:57+00:00",
    "summary": "An exploratory JEDEC task group is weighing how controller vendors could support MRAM with hard IP to work with newer LPDDR implementations. The post Everspin Looks to Broaden MRAM Adoption with LPDDR"
  },
  {
    "id": "rss:https://www.eetimes.com/ltcc-solutions-for-next-generation-uwb-ble-devices/",
    "domain": "AI 算力 / 半导体",
    "title": "LTCC Solutions for Next Generation UWB/BLE Devices",
    "url": "https://www.eetimes.com/ltcc-solutions-for-next-generation-uwb-ble-devices/",
    "source": "TAIYO YUDEN (U.S.A.) INC.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T15:00:00+00:00",
    "summary": "Discover TAIYO YUDEN’s advanced LTCC (Low Temperature Co-fired Ceramic) solutions for UWB and Bluetooth Low Energy (BLE) applications. Featuring high-performance RF components, these solutions address"
  },
  {
    "id": "rss:https://www.eetimes.com/minimising-acoustic-noise-in-space-constrained-medical-and-life-science-applications/",
    "domain": "AI 算力 / 半导体",
    "title": "Minimizing Acoustic Noise in Space-Constrained Medical and Life Science Applications",
    "url": "https://www.eetimes.com/minimising-acoustic-noise-in-space-constrained-medical-and-life-science-applications/",
    "source": "Giulio Bocciolini, Senior Product Marketing Manager EMEA, TDK-Lambda EMEA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-17T15:00:00+00:00",
    "summary": "Design engineers and technical decision-makers working on medical and life science equipment must balance competing demands: high power density, thermal performance, compact dimensions, and low acoust"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/ukraine-deploys-homemade-flying-modems-in-daring-drone-attack-to-destroy-crimean-bridge-ditching-elon-musks-starlink-airborne-relay-stations-allow-pilots-to-dodge-russian-air-defences-to-deliver-1-200kg-payload",
    "domain": "AI 算力 / 半导体",
    "title": "Ukraine deploys homemade 'flying modems' in daring drone attack to destroy Crimean Bridge, ditching Elon Musk's Starlink",
    "url": "https://www.tomshardware.com/networking/ukraine-deploys-homemade-flying-modems-in-daring-drone-attack-to-destroy-crimean-bridge-ditching-elon-musks-starlink-airborne-relay-stations-allow-pilots-to-dodge-russian-air-defences-to-deliver-1-200kg-payload",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T11:11:29+00:00",
    "summary": "Ukrainian forces ditched Elon Musk's Starlink and used a network of \"flying modems\" to build a relay network that allowed them to maintain a live feed of an attack on the Crimean Bridge, even as Russi"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/three-e-waste-nvidia-v100s-hit-100-tokens-per-second-on-qwen-3-6-35b-in-a-usd1-042-homelab-rig-decommissioned-gpus-outpace-a-usd5-399-m5-max-mac-studio-at-long-contexts",
    "domain": "AI 算力 / 半导体",
    "title": "Three 'e-waste' Nvidia V100s hit 100 tokens per second on Qwen 3.6 35B in a $1,042 homelab rig",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/three-e-waste-nvidia-v100s-hit-100-tokens-per-second-on-qwen-3-6-35b-in-a-usd1-042-homelab-rig-decommissioned-gpus-outpace-a-usd5-399-m5-max-mac-studio-at-long-contexts",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T11:00:00+00:00",
    "summary": "A homelab builder runs Qwen 3.6 35B on three used Nvidia Tesla V100 GPUs at about 100 tokens per second, in a $1,042 build."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-32gb-of-ddr5-for-usd240-with-this-blistering-intel-gaming-pc-bundle-the-270k-plus-cpu-also-comes-with-a-1tb-990-pro-ssd-z890-and-a-cooler-for-just-usd1-079",
    "domain": "AI 算力 / 半导体",
    "title": "Get 32GB of DDR5 for $240 with this blistering Intel gaming PC bundle",
    "url": "https://www.tomshardware.com/pc-components/get-32gb-of-ddr5-for-usd240-with-this-blistering-intel-gaming-pc-bundle-the-270k-plus-cpu-also-comes-with-a-1tb-990-pro-ssd-z890-and-a-cooler-for-just-usd1-079",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T10:54:03+00:00",
    "summary": "Score Intel's latest Core Ultra 7 270K Plus with a Z890 motherboard and 32GB of DDR5-6000 memory for $240 off with this bundle."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/save-36-percent-on-this-4tb-samsung-990-pro-ssd-upgrade-for-your-gaming-pc-now-just-17-5-cents-per-gb-our-top-gen-4-drive-recommendation-is-now-usd100-cheaper-than-last-week",
    "domain": "AI 算力 / 半导体",
    "title": "Save 36% on this 4TB Samsung 990 Pro SSD upgrade for your gaming PC, now just 17.5 cents per GB",
    "url": "https://www.tomshardware.com/pc-components/ssds/save-36-percent-on-this-4tb-samsung-990-pro-ssd-upgrade-for-your-gaming-pc-now-just-17-5-cents-per-gb-our-top-gen-4-drive-recommendation-is-now-usd100-cheaper-than-last-week",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T10:52:20+00:00",
    "summary": "Grab this 4TB Samsung 990 Pro SSD with Gen 4 speeds for $699.99, a 36% price drop compared to its list price and a $100 drop since last week."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/critical-java-vulnerability-puts-millions-of-sites-services-and-devices-at-risk-of-remote-code-execution-triggers-with-64-as-and-an-sign-openjdk-optimization-bug-lets-an-attacker-trigger-it-just-by-inputting-repeated-text",
    "domain": "AI 算力 / 半导体",
    "title": "Critical Java vulnerability puts millions of sites, services, and devices at risk of remote code execution",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/critical-java-vulnerability-puts-millions-of-sites-services-and-devices-at-risk-of-remote-code-execution-triggers-with-64-as-and-an-sign-openjdk-optimization-bug-lets-an-attacker-trigger-it-just-by-inputting-repeated-text",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T10:30:00+00:00",
    "summary": "Millions of sites, services, and devices are at risk of remote code execution thanks to a critical bug in the widely-used Java software. Attackers can trigger the bug by just inputting repeated text"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/ddr6-ram-shrinks-by-44-percent-while-delivering-4x-ddr5s-baseline-bandwidth-jedec-previews-12-8-gt-s-modules-with-up-to-1-terabyte-of-capacity-per-slot",
    "domain": "AI 算力 / 半导体",
    "title": "DDR6 RAM shrinks by 44% while delivering 4X DDR5's baseline bandwidth — JEDEC previews 12.8 GT/s modules with up to 1 terabyte of capacity per slot",
    "url": "https://www.tomshardware.com/pc-components/ram/ddr6-ram-shrinks-by-44-percent-while-delivering-4x-ddr5s-baseline-bandwidth-jedec-previews-12-8-gt-s-modules-with-up-to-1-terabyte-of-capacity-per-slot",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T10:00:00+00:00",
    "summary": "Upcoming DDR6 memory cuts module length from 133mm to 74mm while kicking off at 12.8 GT/s, more than doubling DDR5’s baseline transfer rate."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/amds-twitter-brag-that-it-loves-gamers-met-with-savage-community-note-post-met-with-backlash-over-the-companys-pivot-to-ai",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s Twitter brag that it ‘loves gamers’ met with savage Community Note",
    "url": "https://www.tomshardware.com/pc-components/amds-twitter-brag-that-it-loves-gamers-met-with-savage-community-note-post-met-with-backlash-over-the-companys-pivot-to-ai",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T21:00:00+00:00",
    "summary": "Following a post on X, AMD Japan's claim that the company values gamers \"above all else\" saw those gamers point out that its own CEO believes the company is more focused on data centers."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/nvidia-geforce-driver-bug-reportedly-hammers-ssds-with-up-to-30gb-of-writes-per-hour-users-trace-massive-idle-wear-to-background-service-newer-driver-reportedly-still-affected",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia GeForce driver bug reportedly hammers SSDs with up to 30GB of writes per hour",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/nvidia-geforce-driver-bug-reportedly-hammers-ssds-with-up-to-30gb-of-writes-per-hour-users-trace-massive-idle-wear-to-background-service-newer-driver-reportedly-still-affected",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T21:00:00+00:00",
    "summary": "Nvidia’s GeForce 621.14 and 621.24 drivers reportedly rewrite a log file nonstop, writing gigabytes to SSDs every hour."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/nvidia-promises-employee-pay-raises-equity-before-december-to-quell-unrest-in-wake-of-jensen-huang-scandal-at-first-all-hands-meeting-since-ceos-departure-staff-offered-perks-told-were-going-to-be-fine",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia promises employee pay raises, equity before December to quell unrest in wake of Jensen Huang scandal",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/nvidia-promises-employee-pay-raises-equity-before-december-to-quell-unrest-in-wake-of-jensen-huang-scandal-at-first-all-hands-meeting-since-ceos-departure-staff-offered-perks-told-were-going-to-be-fine",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T18:40:28+00:00",
    "summary": "Interim CEO Collete Kress reportedly offered staffers higher wages and more equity on an advanced schedule at the company's first all-hands after Jensen Huang resigned."
  },
  {
    "id": "hn:50261319",
    "domain": "大厂 AI 动态",
    "title": "Genie 4",
    "url": "https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/",
    "source": "acossta",
    "platform": "hackernews",
    "points": 1044,
    "published_at": "2026-10-27T16:06:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:50276792",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/",
    "source": "acossta",
    "platform": "hackernews",
    "points": 1019,
    "published_at": "2026-10-28T17:01:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50552424",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Neon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/",
    "source": "yigitdemirag",
    "platform": "hackernews",
    "points": 854,
    "published_at": "2026-11-18T21:34:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:50403097",
    "domain": "大厂 AI 动态",
    "title": "Every Mac comes with an (undocumented) family member classifier",
    "url": "https://8rank.ai/game/apple-intelligence-personal-knowledge-graph",
    "source": "infwhispers",
    "platform": "hackernews",
    "points": 872,
    "published_at": "2026-11-07T09:46:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50429426",
    "domain": "大厂 AI 动态",
    "title": "Google Gemini routes personal Drive files and emails to human annotators",
    "url": "https://github.com/thisisme6598/gemini_files/",
    "source": "gf74918",
    "platform": "hackernews",
    "points": 740,
    "published_at": "2026-11-09T18:24:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50363461",
    "domain": "大厂 AI 动态",
    "title": "Tell HN: Gemini trains on chat history, even for subscribers (personal accounts)",
    "url": "https://news.ycombinator.com/item?id=50363461",
    "source": "jameslk",
    "platform": "hackernews",
    "points": 738,
    "published_at": "2026-11-04T10:10:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50439193",
    "domain": "大厂 AI 动态",
    "title": "AlphaProof Code",
    "url": "https://deepmind.google/blog/introducing-alphaproof-code/",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 679,
    "published_at": "2026-11-10T12:11:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:50471431",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Hydrogen",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/",
    "source": "dvaplima",
    "platform": "hackernews",
    "points": 573,
    "published_at": "2026-11-12T18:01:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50456791",
    "domain": "大厂 AI 动态",
    "title": "Gemini Decisions API",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/",
    "source": "iamdelirium",
    "platform": "hackernews",
    "points": 570,
    "published_at": "2026-11-11T18:32:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:50472260",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Hydrogen and Orchestrator",
    "url": "https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/",
    "source": "jonbaer",
    "platform": "hackernews",
    "points": 508,
    "published_at": "2026-11-12T18:52:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:50411961",
    "domain": "大厂 AI 动态",
    "title": "Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU",
    "url": "https://github.com/synchopate/llama-modchip",
    "source": "joshcsimmons",
    "platform": "hackernews",
    "points": 487,
    "published_at": "2026-11-08T10:22:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:50392118",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni 1.2 Flash",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 369,
    "published_at": "2026-11-06T13:35:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50541790",
    "domain": "大厂 AI 动态",
    "title": "Why is Gemini 4 Carbon taking so long?",
    "url": "https://kernel.dev/blog/why-is-gemini-4-carbon-taking-so-long/",
    "source": "deenadz",
    "platform": "hackernews",
    "points": 271,
    "published_at": "2026-11-18T04:14:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:50550415",
    "domain": "大厂 AI 动态",
    "title": "Genie 4 is now available",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/",
    "source": "leumon",
    "platform": "hackernews",
    "points": 262,
    "published_at": "2026-11-18T18:49:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:50288019",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon is the new #1 on the Artificial Analysis Intelligence Index v5",
    "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1",
    "source": "theHocineSaad",
    "platform": "hackernews",
    "points": 339,
    "published_at": "2026-10-29T12:41:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:50554374",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Neon looks like an Opus 5.5 competitor",
    "url": "https://micjm.com/blog/gemini-4-neon-looks-like-a-top-model/",
    "source": "seizethecheese",
    "platform": "hackernews",
    "points": 233,
    "published_at": "2026-11-19T00:29:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:50442303",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon is now available",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/",
    "source": "meetpateltech",
    "platform": "hackernews",
    "points": 296,
    "published_at": "2026-11-10T16:07:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50551601",
    "domain": "大厂 AI 动态",
    "title": "Google Gemini's \"Tasks\" Personal Assistant Is Now Free",
    "url": "https://blog.google/innovation-and-ai/products/gemini-app/tasks-in-gemini-free-new-features/",
    "source": "hackeratrandom",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-11-18T20:20:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:50557885",
    "domain": "大厂 AI 动态",
    "title": "DeepMind Employees Are Unionising",
    "url": "https://www.gdmunion.co.uk",
    "source": "nervai",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-11-19T09:28:56+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/1037448/elon-musk-ukraine-starlink-starshield-nyt-dealbook",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk tries to explain what&#8217;s going on with Ukraine and Starlink",
    "url": "https://www.theverge.com/tech/1037448/elon-musk-ukraine-starlink-starshield-nyt-dealbook",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T01:39:45+00:00",
    "summary": "Elon Musk said Ukrainian president Volodymyr Zelenskyy is lying about disruptions to Starshield in Ukraine and that he's trying to misuse SpaceX's consumer service, Starlink, for military purposes. Mu"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1037151/school-districts-ditching-google",
    "domain": "大厂 AI 动态",
    "title": "The nation’s largest school districts consider ditching Google Search",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1037151/school-districts-ditching-google",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T23:18:35+00:00",
    "summary": "New York, Los Angeles, and Chicago schools are considering Google alternatives after the company said it will disable Search for schools that opt out of its AI features, according to The New York Time"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1037134/democrats-boycott-fcc-nomination-vote-danielle-thumann-severs",
    "domain": "大厂 AI 动态",
    "title": "Democrats skip a vote on adding Brendan Carr’s adviser to the FCC",
    "url": "https://www.theverge.com/policy/1037134/democrats-boycott-fcc-nomination-vote-danielle-thumann-severs",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T22:05:48+00:00",
    "summary": "Senate commerce committee Chair Ted Cruz (R-TX) began a meeting Wednesday meant to confirm President Donald Trump's nominee to the Federal Communications Commission with a lopsided dais. To his right "
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1035722/absolute-batman-can-save-dc-studios",
    "domain": "大厂 AI 动态",
    "title": "Absolute Batman can save DC Studios",
    "url": "https://www.theverge.com/entertainment/1035722/absolute-batman-can-save-dc-studios",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T21:20:00+00:00",
    "summary": "With James Gunn and Peter Safran out as the co-heads of DC Studios following Skydance's acquisition of Warner Bros. Discovery, it's unclear what will become of the cinematic universe that was building"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1036749/trump-ai-chip-data-center-us-philippines-pax-silica",
    "domain": "大厂 AI 动态",
    "title": "Trump’s latest land grab is an AI hub in the Philippines",
    "url": "https://www.theverge.com/policy/1036749/trump-ai-chip-data-center-us-philippines-pax-silica",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T19:40:36+00:00",
    "summary": "President Donald Trump was greeted by no less than five beauty queens when he landed in the Philippines on Tuesday, according to local news outlet Rappler. As he stepped onto the tarmac, a child hande"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1035924/nvidia-visualized-revenue-profit-earnings-after-huang",
    "domain": "大厂 AI 动态",
    "title": "Nvidia’s rise, visualized",
    "url": "https://www.theverge.com/tech/1035924/nvidia-visualized-revenue-profit-earnings-after-huang",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T19:30:00+00:00",
    "summary": "If someone handed you $8,300 every second, what would you do? That's how much pure profit Nvidia now makes. By the time you finish reading this paragraph, Nvidia will likely have cleared $45,000 and c"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1036693/sony-bravia-8-ii-oled-black-friday-2026-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Sony’s impressive Bravia 8 II OLED hits a new low price ahead of Black Friday",
    "url": "https://www.theverge.com/gadgets/1036693/sony-bravia-8-ii-oled-black-friday-2026-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T19:30:00+00:00",
    "summary": "Black Friday is a great time to save on a new OLED television for your winter movie nights. Though, it turns out that you can already get a great deal on the 65-inch Sony Bravia 8 II, one of our favor"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1036941/instagram-now-lets-you-edit-your-stories-after-you-post-them",
    "domain": "大厂 AI 动态",
    "title": "Instagram now lets you edit your stories after you post them",
    "url": "https://www.theverge.com/tech/1036941/instagram-now-lets-you-edit-your-stories-after-you-post-them",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T19:29:10+00:00",
    "summary": "Instagram's latest update will allow you to edit your Stories without losing your views, likes, or replies. You can now edit the text, music, stickers, and drawings for up to 15 minutes after sharing "
  },
  {
    "id": "rss:https://www.theverge.com/games/1036819/the-leaked-lenovo-legion-go-beam-could-be-the-affordable-handheld-we-need",
    "domain": "大厂 AI 动态",
    "title": "The leaked Lenovo Legion Go Beam could be the affordable handheld we need",
    "url": "https://www.theverge.com/games/1036819/the-leaked-lenovo-legion-go-beam-could-be-the-affordable-handheld-we-need",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T19:11:50+00:00",
    "summary": "For a while there, it seemed like Lenovo had given up on selling handheld gaming PCs, hiking the price of its Legion Go 2 and Legion Go S far higher than other RAM-starved competitors. A decent one ca"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1036935/congress-forced-arbitration-deepfakes-defiance-act",
    "domain": "大厂 AI 动态",
    "title": "Tech lawsuits defined 2026 — and lawmakers want more",
    "url": "https://www.theverge.com/policy/1036935/congress-forced-arbitration-deepfakes-defiance-act",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T19:07:29+00:00",
    "summary": "With just a few weeks remaining, lawmakers are trying to pass new protections for victims of online harm before the end of 2026, targeting deepfake creators and online platforms that block users from "
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/microsoft-ceo-satya-nadella-explains-why-he-asked-60k-employees-to-quit/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft CEO Satya Nadella explains why he asked 60K employees to quit",
    "url": "https://techcrunch.com/2026/11/18/microsoft-ceo-satya-nadella-explains-why-he-asked-60k-employees-to-quit/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T00:42:56+00:00",
    "summary": "Microsoft CEO Satya Nadella explained why he offered buyouts to 60,000 of his employees in October, essentially urging them to voluntarily quit, rather than reducing the workforce via another massive "
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/elon-musk-says-im-not-maga/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk says: ‘I’m not MAGA’",
    "url": "https://techcrunch.com/2026/11/18/elon-musk-says-im-not-maga/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T00:40:49+00:00",
    "summary": "During his appearance Wednesday at The New York Times' DealBook Summit, Elon Musk said that he wasn't sure what the term \"MAGA\" meant and also commented that he felt \"pretty foolish\" for having spent "
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/amidst-fears-of-ai-cyberattacks-satya-nadella-says-lots-of-critical-infrastructure-is-unpatchable/",
    "domain": "大厂 AI 动态",
    "title": "Amidst fears of AI cyberattacks, Satya Nadella says lots of critical infrastructure is ‘unpatchable’",
    "url": "https://techcrunch.com/2026/11/18/amidst-fears-of-ai-cyberattacks-satya-nadella-says-lots-of-critical-infrastructure-is-unpatchable/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T23:45:00+00:00",
    "summary": "The Microsoft CEO downplayed the recent Outlook outage while noting that AI was causing both opportunities and new challenges for securing much of the connected world."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/elon-musk-says-ousting-jensen-huang-is-like-kicking-michael-jordan-off-your-team/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk says ousting Jensen Huang is like ‘kicking Michael Jordan off your team’",
    "url": "https://techcrunch.com/2026/11/18/elon-musk-says-ousting-jensen-huang-is-like-kicking-michael-jordan-off-your-team/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T23:25:17+00:00",
    "summary": "“I don’t think [Huang is] disloyal to the United States,\" Musk said."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/microsoft-ceo-satya-nadella-remains-confident-in-nvidia-after-huangs-exit/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft CEO Satya Nadella remains confident in Nvidia after Huang’s exit",
    "url": "https://techcrunch.com/2026/11/18/microsoft-ceo-satya-nadella-remains-confident-in-nvidia-after-huangs-exit/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T23:17:28+00:00",
    "summary": "Microsoft CEO Satya Nadella expressed confidence in Jensen Huang's successor Colette Kress, who is serving as Nvidia's interim CEO."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/satya-nadella-predicts-ai-agents-will-reshuffle-the-economics-of-the-web/",
    "domain": "大厂 AI 动态",
    "title": "Satya Nadella predicts AI agents will reshuffle the economics of the web",
    "url": "https://techcrunch.com/2026/11/18/satya-nadella-predicts-ai-agents-will-reshuffle-the-economics-of-the-web/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T22:58:11+00:00",
    "summary": "Microsoft's CEO says AI agents could disrupt advertising-driven business models, forcing companies like Amazon to rethink how they compete for customers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/anthropic-reportedly-prices-ipo-at-83-a-share-above-projected-range/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic prices IPO at $83 a share, above projected range",
    "url": "https://techcrunch.com/2026/11/18/anthropic-reportedly-prices-ipo-at-83-a-share-above-projected-range/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T22:11:15+00:00",
    "summary": "The long-awaited IPO reportedly values the company at $1.5 trillion on a fully diluted basis."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/palmer-luckey-doesnt-deny-that-hes-a-prepper/",
    "domain": "大厂 AI 动态",
    "title": "Palmer Luckey doesn’t deny that he’s a prepper",
    "url": "https://techcrunch.com/2026/11/18/palmer-luckey-doesnt-deny-that-hes-a-prepper/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T22:04:03+00:00",
    "summary": "The Anduril founder said Wednesday that Americans should always have three days of food, water, and medicine — just in case."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/nvidia-created-a-weird-bit-of-intrigue-by-not-filing-a-routine-sec-report/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia created a weird bit of intrigue by not filing a routine SEC report",
    "url": "https://techcrunch.com/2026/11/18/nvidia-created-a-weird-bit-of-intrigue-by-not-filing-a-routine-sec-report/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T21:57:40+00:00",
    "summary": "One Wall Street analyst got to the bottom of Nvidia's surprise announcement that it wouldn't be filing its formal quarterly results document, the 10-Q, for weeks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/palmer-luckey-warns-ai-powered-cyberattacks-are-outpacing-defenses-its-time-to-start-running/",
    "domain": "大厂 AI 动态",
    "title": "Palmer Luckey warns AI-powered cyberattacks are outpacing defenses: ‘It’s time to start running’",
    "url": "https://techcrunch.com/2026/11/18/palmer-luckey-warns-ai-powered-cyberattacks-are-outpacing-defenses-its-time-to-start-running/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T21:34:13+00:00",
    "summary": "The Anduril co-founder says outdated technology is leaving systems vulnerable to a new wave of AI-enabled attacks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/palmer-luckey-thinks-china-is-thrilled-to-have-jensen-out-so-he-wants-the-ousted-nvidia-ceo-reinstated/",
    "domain": "大厂 AI 动态",
    "title": "Palmer Luckey thinks China is ‘thrilled to have Jensen out,’ so he wants the ousted Nvidia CEO reinstated",
    "url": "https://techcrunch.com/2026/11/18/palmer-luckey-thinks-china-is-thrilled-to-have-jensen-out-so-he-wants-the-ousted-nvidia-ceo-reinstated/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T21:31:21+00:00",
    "summary": "\"It makes America weaker to knock him out,\" the Anduril CEO said about ousted Nvidia leader Jensen Huang."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/sam-altman-says-his-life-is-so-weird-that-hes-unfazed-by-andrew-garfield-portraying-him-in-upcoming-movie/",
    "domain": "大厂 AI 动态",
    "title": "Sam Altman says his life is so weird that he’s unfazed by Andrew Garfield portraying him in upcoming movie",
    "url": "https://techcrunch.com/2026/11/18/sam-altman-says-his-life-is-so-weird-that-hes-unfazed-by-andrew-garfield-portraying-him-in-upcoming-movie/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T20:07:01+00:00",
    "summary": "\"It doesn't feel like it's in like the top 10 weirdest things about my life,\" Altman said."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/snapchat-now-lets-developers-build-ar-lenses-with-ai-coding-assistants-like-claude-code-and-cursor/",
    "domain": "大厂 AI 动态",
    "title": "Snapchat now lets developers build AR Lenses with AI assistants like Claude Code and Cursor",
    "url": "https://techcrunch.com/2026/11/18/snapchat-now-lets-developers-build-ar-lenses-with-ai-coding-assistants-like-claude-code-and-cursor/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T19:56:39+00:00",
    "summary": "Lens creators can describe the Lens they want in plain language, and their AI assistant handles the process from start to finish, Snapchat says."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/spend-management-platform-payhawk-announces-280m-raise-2b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Spend management platform Payhawk announces $280M raise, 2B valuation",
    "url": "https://techcrunch.com/2026/11/18/spend-management-platform-payhawk-announces-280m-raise-2b-valuation/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T19:29:41+00:00",
    "summary": "Founded in 2018, Payhawk is an enterprise financial management platform that helps companies track and manage expenses and procurement using AI agents."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/googles-ai-feature-in-search-gets-its-own-incognito-mode/",
    "domain": "大厂 AI 动态",
    "title": "Google’s AI feature in Search gets its own incognito mode",
    "url": "https://techcrunch.com/2026/11/18/googles-ai-feature-in-search-gets-its-own-incognito-mode/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T18:04:05+00:00",
    "summary": "Google's new temporary threads let users have conversations in AI Mode without adding them to their search history or influencing future recommendations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/more-banks-says-customers-using-ai-agents-are-on-their-own-even-if-they-get-hacked/",
    "domain": "大厂 AI 动态",
    "title": "More banks say customers using AI agents are on their own — even if they get hacked",
    "url": "https://techcrunch.com/2026/11/18/more-banks-says-customers-using-ai-agents-are-on-their-own-even-if-they-get-hacked/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T17:32:10+00:00",
    "summary": "Citi is the latest major financial institution to put the breaks on personal finance AI agents."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/david-ellison-says-hbo-will-air-critical-elon-musk-documentary-despite-1b-investment-in-skydance/",
    "domain": "大厂 AI 动态",
    "title": "David Ellison says HBO will air critical Elon Musk documentary despite his $1B investment in Skydance",
    "url": "https://techcrunch.com/2026/11/18/david-ellison-says-hbo-will-air-critical-elon-musk-documentary-despite-1b-investment-in-skydance/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T17:30:56+00:00",
    "summary": "Following news of the investment, questions emerged over how Musk's sizable stake in the company might affect Skydance's plans to distribute a documentary that is highly critical of him."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/sam-altman-warns-against-a-future-where-ai-not-humans-calls-the-shots/",
    "domain": "大厂 AI 动态",
    "title": "Sam Altman warns against a future where AI, not humans, calls the shots",
    "url": "https://techcrunch.com/2026/11/18/sam-altman-warns-against-a-future-where-ai-not-humans-calls-the-shots/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T16:59:00+00:00",
    "summary": "Sam Altman and Greg Brockman pushed back against Silicon Valley's growing debate over an AI takeover, while acknowledging the challenges of keeping advanced models under human control."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/openai-ceo-sam-altman-says-its-hard-to-imagine-the-ai-industry-without-jensen/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI CEO Sam Altman says it’s ‘hard to imagine the AI industry without Jensen’",
    "url": "https://techcrunch.com/2026/11/18/openai-ceo-sam-altman-says-its-hard-to-imagine-the-ai-industry-without-jensen/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T16:14:09+00:00",
    "summary": "Nvidia founder and former CEO Jensen Huang stepped down last week amid several scandals, including an affair with an alleged Chinese spy."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/18/sonys-updated-turntable-is-an-easy-entry-into-the-world-of-vinyl/",
    "domain": "大厂 AI 动态",
    "title": "Sony’s updated turntable is an easy entry into the world of vinyl",
    "url": "https://techcrunch.com/2026/11/18/sonys-updated-turntable-is-an-easy-entry-into-the-world-of-vinyl/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-18T16:00:00+00:00",
    "summary": "Sony's updated turntable for beginners features automatic playback, USB connectivity, and aptX Adaptive Bluetooth."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-eric-seufert-about-agentic-commerce/",
    "domain": "大厂 AI 动态",
    "title": "An Interview With Eric Seufert About Agentic Commerce",
    "url": "https://stratechery.com/2026/an-interview-with-eric-seufert-about-agentic-commerce/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T11:00:00+00:00",
    "summary": "An interview with Eric Seufert about agentic commerce, including why he thinks ads will be the answer, and why I want retailers who cater to agents."
  },
  {
    "id": "hn:50344919",
    "domain": "股票",
    "title": "The SEC Should Block Anthropic's IPO to Protect the Public",
    "url": "https://www.techpolicy.press/the-sec-should-block-anthropics-ipo-to-protect-the-public/",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 406,
    "published_at": "2026-11-02T22:30:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50307219",
    "domain": "股票",
    "title": "Anthropic may not secure investment-grade rating after IPO, Blackstone says",
    "url": "https://www.ft.com/content/59383c7f-8d82-493f-bf01-d2e862a1018f",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 327,
    "published_at": "2026-10-30T17:27:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50556287",
    "domain": "股票",
    "title": "Ruby2ßhell: Pre-authentication RCE on stock Rails",
    "url": "https://verialabs.com/ruby2shell/",
    "source": "jdns",
    "platform": "hackernews",
    "points": 156,
    "published_at": "2026-11-19T05:09:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:50381623",
    "domain": "股票",
    "title": "Nasdaq plummets 4% into correction territory",
    "url": "https://www.cnbc.com/2026/11/04/stock-market-today-live-updates.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 227,
    "published_at": "2026-11-05T17:11:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50510005",
    "domain": "股票",
    "title": "Do House members' stock trades beat the market? A test of 8,900 trades",
    "url": "https://arkanumdata.com/research/house-trades",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 127,
    "published_at": "2026-11-15T19:46:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50337454",
    "domain": "股票",
    "title": "Jobless tech workers are being left out of San Francisco's AI boom",
    "url": "https://www.bloomberg.com/news/features/2026-09-17/san-francisco-s-ai-wealth-boom-skirts-engineers-as-openai-anthropic-ipos-near",
    "source": "mancerayder",
    "platform": "hackernews",
    "points": 188,
    "published_at": "2026-11-02T14:40:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50384822",
    "domain": "股票",
    "title": "$2.5T has been wiped from US stocks",
    "url": "https://finlaws.substack.com/p/25t-has-been-wiped-from-us-stocks",
    "source": "madihaa",
    "platform": "hackernews",
    "points": 164,
    "published_at": "2026-11-05T21:39:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50382179",
    "domain": "股票",
    "title": "Nasdaq Sinks 5% as Investors Retreat from AI Trade After Election",
    "url": "https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-05-2026",
    "source": "armcat",
    "platform": "hackernews",
    "points": 163,
    "published_at": "2026-11-05T18:00:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:50549623",
    "domain": "股票",
    "title": "Just say no to Anthropic's IPO",
    "url": "https://garymarcus.substack.com/p/just-say-no-to-anthropics-ipo",
    "source": "Betelbuddy",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-11-18T17:54:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50401029",
    "domain": "股票",
    "title": "The AI sell-off compared to well-known stock market crashes",
    "url": "https://www.kadoa.com/companies/insights/ai-selloff-perspective",
    "source": "hubraumhugo",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-11-07T02:20:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50542361",
    "domain": "股票",
    "title": "Interesting Learnings Working for a Startup",
    "url": "https://news.ycombinator.com/item?id=50542361",
    "source": "Jessiejia11",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-11-18T05:52:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50553581",
    "domain": "股票",
    "title": "Anthropic reportedly prices its IPO at $83 per share, valuing at $1.5T",
    "url": "https://apnews.com/article/anthropic-ipo-pricing-70b660ddf900d90bbf484ecdf1fb441c",
    "source": "6thbit",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-11-18T23:00:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50311311",
    "domain": "股票",
    "title": "Anthropic to receive high 'junk' rating from credit agencies following IPO",
    "url": "https://techcrunch.com/2026/10/30/anthropic-expected-to-receive-high-junk-rating-from-credit-agencies-following-ipo-report-says/",
    "source": "jnord",
    "platform": "hackernews",
    "points": 104,
    "published_at": "2026-10-30T23:08:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:50507517",
    "domain": "股票",
    "title": "A Human Reads the Anthropic IPO Filing",
    "url": "https://www.nytimes.com/2026/11/15/business/anthropic-ipo-filing-prospectus.html",
    "source": "saikatsg",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-11-15T15:18:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50529644",
    "domain": "股票",
    "title": "Who Is Anthropic Kidding?",
    "url": "https://www.theatlantic.com/economy/2026/11/anthropic-ipo-ai-safety/689440/",
    "source": "nothrowaways",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-11-17T10:25:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:50350560",
    "domain": "股票",
    "title": "Anthropic IPO filing: $1.7B quarterly payroll, about $107K per employee monthly",
    "url": "https://www.techspot.com/news/114428-anthropic-ipo-filing-reveals-17-billion-quarterly-personnel.html",
    "source": "entryleveljobsc",
    "platform": "hackernews",
    "points": 84,
    "published_at": "2026-11-03T11:16:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:50342424",
    "domain": "股票",
    "title": "Anthropic reveals $900B AI spending commitments ahead of IPO",
    "url": "https://www.ft.com/content/4d91dbab-6fe4-45ab-beee-d77e091cb37f",
    "source": "zomtorg",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-11-02T19:36:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50484110",
    "domain": "股票",
    "title": "Amodei Says AI Will Cure Cancer in a Decade. Doctors Are Skeptical",
    "url": "https://www.businessinsider.com/dario-amodei-anthropic-cancer-cure-ipo-roadshow-backlash-doctors-2026-11",
    "source": "robin_reala",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-11-13T14:34:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50467092",
    "domain": "股票",
    "title": "Jensen Huang resigning effective immediately",
    "url": "https://www.stocktitan.net/news/NVDA/nvidia-announces-ceo-03al5m45ne1p.html",
    "source": "chrisss395",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-11-12T13:52:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50386909",
    "domain": "股票",
    "title": "Investors wipe $2.5T off Nasdaq as blue tsunami prompts AI fears",
    "url": "https://www.reuters.com/legal/transactional/ai-data-center-stocks-slip-democratic-sweep-clouds-expansion-plans-2026-11-05/",
    "source": "lilerjee",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-11-06T01:11:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50463421",
    "domain": "股票",
    "title": "Nvidia's Disappearing Singapore Sales Deepen Mystery Around Megaspeed",
    "url": "https://www.wsj.com/business/earnings/nvidias-disappearing-singapore-sales-deepen-mystery-around-megaspeed-7d483180",
    "source": "ea016",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-11-12T05:31:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:50389401",
    "domain": "股票",
    "title": "Global stocks tumble as AI panic grips markets after Democrats' midterm success",
    "url": "https://www.theguardian.com/business/live/2026/nov/06/global-stocks-tumble-ai-panic-markets-democrats-midterms-success-jobs-oil-dollar-latest-news-updates",
    "source": "drayfield",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-11-06T07:52:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50384382",
    "domain": "股票",
    "title": "Chip stocks get slaughtered as Wall Street in worst post-midterm day since 1896",
    "url": "https://finance.yahoo.com/markets/article/chip-stocks-get-slaughtered-as-wall-street-heads-for-its-worst-post-midterm-day-since-1896-163413900.html",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-11-05T20:58:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:50383675",
    "domain": "股票",
    "title": "Wipeout for AI stocks sends Wall Street reeling and S&P 500 tumbles more than 3%",
    "url": "https://apnews.com/article/stocks-markets-ai-midterm-oil-trump-7ee9c212805aa5e70cf34d25aab7a36e",
    "source": "jethronethro",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-11-05T19:58:06+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/a-bankers-guide-to-anthropic",
    "domain": "股票",
    "title": "A Banker’s Guide to Anthropic",
    "url": "https://www.netinterest.co/p/a-bankers-guide-to-anthropic",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T18:00:43+00:00",
    "summary": "Why the IPO is a credit event"
  },
  {
    "id": "hn:50385642",
    "domain": "股票",
    "title": "Michael Burry says Anthropic is 'betting its existence' on optimism",
    "url": "https://www.businessinsider.com/michael-burry-anthropic-ipo-outlook-ant-big-short-2026-11",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-11-05T22:49:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50445463",
    "domain": "股票",
    "title": "Anthropic Targets $1.4T Valuation in IPO",
    "url": "https://www.bloomberg.com/news/videos/2026-11-10/anthropic-targets-1-4-trillion-valuation-in-ipo-video",
    "source": "rndsignals",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-11-10T19:56:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:50351712",
    "domain": "股票",
    "title": "Anthropic's IPO Filing Warns It May Be 'Imminently' Close to RSI",
    "url": "https://epyhia.com/anthropic-s-ipo-filing-warns-it-may-be-imminently-close-to-recursive",
    "source": "arbuge",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-11-03T13:26:43+00:00",
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
    "id": "rss:https://www.netinterest.co/p/the-insatiable-demand-for-alpha",
    "domain": "股票",
    "title": "The Insatiable Demand for Alpha",
    "url": "https://www.netinterest.co/p/the-insatiable-demand-for-alpha",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T17:59:24+00:00",
    "summary": "Why a market shakedown could leave the biggest pod shops stronger"
  },
  {
    "id": "hn:50326281",
    "domain": "股票",
    "title": "Ant: Can unprecedented revenue growth outrun irresponsibly large investment",
    "url": "https://leonlins.com/writing/anthropic_ipo",
    "source": "avoidboringppl",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-11-01T14:56:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50323575",
    "domain": "股票",
    "title": "We're Living in the Age of the Imperial CEO",
    "url": "https://www.wsj.com/tech/ai/anthropic-ipo-dual-class-stock-founder-control-4c43a56d",
    "source": "pretext",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-11-01T08:09:48+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/follow-the-money-ece",
    "domain": "股票",
    "title": "Follow the Money",
    "url": "https://www.netinterest.co/p/follow-the-money-ece",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T17:48:55+00:00",
    "summary": "What six years and 300+ posts of Net Interest say about where finance is heading"
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
    "id": "hn:50391456",
    "domain": "金融",
    "title": "Tesla to wind down Cybertruck production",
    "url": "https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817",
    "source": "PLenz",
    "platform": "hackernews",
    "points": 1167,
    "published_at": "2026-11-06T12:13:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:50385870",
    "domain": "金融",
    "title": "Cuban: Facebook knowingly runs AI deepfake scam ads; docs say $16B fraud revenue",
    "url": "https://finance.yahoo.com/technology/ai/articles/mark-cuban-says-facebook-knowingly-213000020.html",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 525,
    "published_at": "2026-11-05T23:09:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:50305573",
    "domain": "金融",
    "title": "The federated code forge",
    "url": "https://tangled.org/blog/forge/",
    "source": "zlliang",
    "platform": "hackernews",
    "points": 333,
    "published_at": "2026-10-30T15:44:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50173487",
    "domain": "金融",
    "title": "Feds suspect ransom negotiator ran ShinyHunters extortion site",
    "url": "https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/",
    "source": "Bender",
    "platform": "hackernews",
    "points": 270,
    "published_at": "2026-10-20T22:21:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50346153",
    "domain": "金融",
    "title": "Intel stock collapse worsens as $3.5T chip rout spreads",
    "url": "https://finance.yahoo.com/markets/article/the-intel-stock-collapse-is-getting-worse--and-the-37-trillion-chip-rout-is-spreading-212154947.html",
    "source": "entryleveljobsc",
    "platform": "hackernews",
    "points": 237,
    "published_at": "2026-11-03T00:08:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50414427",
    "domain": "金融",
    "title": "Tesla Hasn't Had a Successful New Product Launch Since JB Straubel Stepped Down",
    "url": "https://cleantechnica.com/2026/11/07/tesla-hasnt-had-a-successful-new-product-launch-since-jb-straubel-stepped-down-as-cto/",
    "source": "gumby",
    "platform": "hackernews",
    "points": 208,
    "published_at": "2026-11-08T16:07:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:50525658",
    "domain": "金融",
    "title": "Pentagon fails ninth straight audit despite progress in organizing finances",
    "url": "https://www.reuters.com/business/aerospace-defense/pentagon-fails-ninth-straight-audit-despite-progress-organizing-finances-2026-11-16/",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 150,
    "published_at": "2026-11-17T00:23:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:50342284",
    "domain": "金融",
    "title": "Oracle files to sell $20B in new stock, bonds to finance AI buildout",
    "url": "https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html",
    "source": "smartmic",
    "platform": "hackernews",
    "points": 200,
    "published_at": "2026-11-02T19:27:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50190168",
    "domain": "金融",
    "title": "Epic Games Inc v Apple Inc",
    "url": "https://www.judgments.fedcourt.gov.au/judgments/Judgments/fca/single/2026/2026fca1552",
    "source": "Mayzie",
    "platform": "hackernews",
    "points": 193,
    "published_at": "2026-10-22T01:52:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50532322",
    "domain": "金融",
    "title": "A US Federal Women's Prison Became a \"Rape Club\"",
    "url": "https://www.propublica.org/article/federal-womens-prison-sexual-abuse-reform-dublin-bop",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 86,
    "published_at": "2026-11-17T15:03:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50260526",
    "domain": "金融",
    "title": "A $300B 'Debt Wall' Is Looming over Private-Equity Backed Companies",
    "url": "https://www.wsj.com/finance/investing/a-300-billion-debt-wall-is-looming-over-private-equity-backed-companies-d6359497",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 178,
    "published_at": "2026-10-27T15:09:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50236073",
    "domain": "金融",
    "title": "Nvidia and Micron Make Up 34% of America's Earnings Boom",
    "url": "https://www.wsj.com/finance/stocks/the-earnings-boom-is-heavily-reliant-on-just-a-handful-of-stocks-21decb53",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 176,
    "published_at": "2026-10-25T21:07:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50543108",
    "domain": "金融",
    "title": "Firefox opens hotline for users sick of Microsoft shoving Edge down their throat",
    "url": "https://www.neowin.net/news/firefox-opens-hotline-for-windows-users-fed-up-with-microsoft-shoving-edge-down-their-throat/",
    "source": "bundie",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-11-18T07:51:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:50505905",
    "domain": "金融",
    "title": "Jensen Huang allegedly manufactured the GPU shortage",
    "url": "https://wccftech.com/jensen-huang-financed-ai-startups-absorb-excess-silicon/",
    "source": "bobsoap",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-11-15T10:53:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50387406",
    "domain": "金融",
    "title": "Tesla and SpaceX lose over $420B in combined market cap in the two days",
    "url": "https://techlaws.pages.dev/tesla-and-spacex-lose-over-420b-in-combined-market-cap-in-the-two-days/",
    "source": "Pepitobombito",
    "platform": "hackernews",
    "points": 84,
    "published_at": "2026-11-06T02:30:25+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.23354",
    "domain": "金融",
    "title": "AI, Specialization, and the Organization of Knowledge Work: Evidence from Legal Services",
    "url": "https://arxiv.org/abs/2611.23354",
    "source": "Liu Zhang, Mark Esposito, Isabel Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2611.23354v1 Announce Type: new Abstract: Artificial intelligence makes specialized knowledge cheaper to use, but its effects on professional-service firms depend on how clients reallocate work "
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.23495",
    "domain": "金融",
    "title": "Total Positivity Properties of American Options",
    "url": "https://arxiv.org/abs/2611.23495",
    "source": "Paul Glasserman, Mike Li, Dan Pirjol",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2611.23495v1 Announce Type: new Abstract: Call option prices, viewed as functions of strike and time-to-expiration, are totally positive of order 2 (TP2) if the ratio of the price of a higher-st"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.23587",
    "domain": "金融",
    "title": "Spectral Pricing of Corridor Products under Layered Local Volatility",
    "url": "https://arxiv.org/abs/2611.23587",
    "source": "Andrey Itkin, Dmitry Muravey",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2611.23587v1 Announce Type: new Abstract: We price corridor products under a $N$-layered local volatility, piecewise constant in the price and in time, with knock-out barriers. A spatial scale t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.23723",
    "domain": "金融",
    "title": "When Price Charts Rhyme: Historical Visual Retrieval for Stock Return Prediction",
    "url": "https://arxiv.org/abs/2611.23723",
    "source": "Hui Chen, Haoyu Liu, Ke Wu, Dexin Zhou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2611.23723v1 Announce Type: new Abstract: We study whether visually similar price histories predict similar future returns, using a vision model to retrieve each stock's most similar charts from"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.24266",
    "domain": "金融",
    "title": "Sensitivity analysis in real options studies: systematic review and recommendations",
    "url": "https://arxiv.org/abs/2611.24266",
    "source": "Mariia Kozlova, Julian Scott Yeomans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2611.24266v1 Announce Type: new Abstract: Real options (RO) modeling provides a powerful framework for valuing managerial flexibility under uncertainty in capital-intensive investments across va"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.24912",
    "domain": "金融",
    "title": "Stock bubbles in limited participation models with power utilities",
    "url": "https://arxiv.org/abs/2611.24912",
    "source": "Kasper Larsen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2611.24912v1 Announce Type: new Abstract: We prove that the equilibrium state-price deflated cum-dividend stock-price process in Guasoni, Larsen, and Leoni (2025) is a strict local martingale. O"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.24028",
    "domain": "金融",
    "title": "Algorithmic Market Making Can Lead to Rough Volatility Through the Order Book",
    "url": "https://arxiv.org/abs/2611.24028",
    "source": "Sai Niranjan Ramachandran",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2611.24028v1 Announce Type: cross Abstract: Existing work suggests that markets can show volatility with paths rougher than those of Brownian motion. In theory this can happen when the order flo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.24659",
    "domain": "金融",
    "title": "ChainIT Transaction Truth: Stablecoins, Web3 Wallets, and Multi-Rail Commerce. A Zero-Trust Control Plane for Verified Identity, Organizational Authority, Runtime Compliance, Secure Wallet Execution, ",
    "url": "https://arxiv.org/abs/2611.24659",
    "source": "Eric Tacl, Matthew Koepp, Tim Hines, Russell Lessard, Jason Patrick, Jeremy Blackburn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2611.24659v1 Announce Type: cross Abstract: Stablecoins can move value continuously across programmable networks, and Web3 wallets can authorize those transfers with cryptographic signatures, bu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.24714",
    "domain": "金融",
    "title": "The Structural Number of Parties: An Electoral-Outcome-Independent Baseline for Comparing Party-System Scale",
    "url": "https://arxiv.org/abs/2611.24714",
    "source": "Adama Nouboukpo, Kodzo Michel Aladji, Bappa Muktar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2611.24714v1 Announce Type: cross Abstract: How many parties can a country structurally sustain? Standard measures such as the effective number of parties (ENP) cannot answer this question. They"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.24845",
    "domain": "金融",
    "title": "Vibe-Trading: Towards Agent-Native Trading",
    "url": "https://arxiv.org/abs/2611.24845",
    "source": "Haozhe Wu, Zhonghang Li, Chao Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2611.24845v1 Announce Type: cross Abstract: Existing AI agents can retrieve information, call tools, run experiments, and produce multi-step outputs. Yet most are built around relatively static "
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.03964",
    "domain": "金融",
    "title": "Where Are the Rates? Derivative-Implied Interest Rates in Cryptocurrency Markets",
    "url": "https://arxiv.org/abs/2509.03964",
    "source": "Philippe Bergault, S\\'ebastien Bieber, Olivier Gu\\'eant, Wenkai Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2509.03964v4 Announce Type: replace Abstract: In traditional finance, liquid markets for bonds, interest rate swaps, and other interest rate derivatives provide a basis for constructing yield cu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04753",
    "domain": "金融",
    "title": "Fooling Yourself: how narratives shape beliefs",
    "url": "https://arxiv.org/abs/2607.04753",
    "source": "Andrea Albertazzi, Paolo Pin, Marco Stimolo, Alessandro Stringhi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2607.04753v4 Announce Type: replace Abstract: Narratives often combine diagnostic evidence with truthful but nondiagnostic details. In a two-state experiment with known signal likelihoods, we te"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.06618",
    "domain": "金融",
    "title": "Beyond Co-Movement: Locality by Exposures Enables a Joint Factor-Graph Framework for Portfolio Diversification",
    "url": "https://arxiv.org/abs/2608.06618",
    "source": "Sara Chehab, Giorgos Iacovides, Parisa Yazdanparast, Danilo Mandic",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2608.06618v3 Announce Type: replace Abstract: Current portfolio construction methods are either agnostic to the effects of idiosyncratic shocks (standard factor models) or to the latent data str"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.21274",
    "domain": "金融",
    "title": "Recommendation Quality and the Concentration of Consumption: Experimental Evidence from Netflix",
    "url": "https://arxiv.org/abs/2608.21274",
    "source": "Guy Aridor, Winston Chou, Nathan Kallus, Antoine Scheid, Allen Tren, Kevin Zielincki",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2608.21274v2 Announce Type: replace Abstract: We study an experiment with 8.5 million users on Netflix's recommender system to measure how improvements in recommendation technology affect the se"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.16540",
    "domain": "金融",
    "title": "Dynamic Scenario-Based Portfolio Optimization for Multi-Asset ETFs",
    "url": "https://arxiv.org/abs/2611.16540",
    "source": "Abigail A. Mensah, Ali M. Jaffri, Nicholas Appiah, W. Brent Lindquist, Svetlozar T. Rachev, Frank J. Fabozzi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2611.16540v2 Announce Type: replace Abstract: Portfolio outcomes may depend as much on trading restrictions as on how returns are modeled. We compared historical moving-window returns with condi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.18660",
    "domain": "金融",
    "title": "The effect of policy cancellation on the risk of an insurance portfolio",
    "url": "https://arxiv.org/abs/2611.18660",
    "source": "Stefan Gerhold, Friedrich Hubalek, Manuel Schranzhofer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2611.18660v2 Announce Type: replace Abstract: For an insurance portfolio modelled by a large number of i.i.d. losses, the average loss converges to its expected value by the law of large numbers"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.20242",
    "domain": "金融",
    "title": "Markets for Compute and Inference: Structure, Financing, and Risk Transfer",
    "url": "https://arxiv.org/abs/2611.20242",
    "source": "Dr Gabriel Borrageiro",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2611.20242v2 Announce Type: replace Abstract: Capacity to run large language models is rented by the accelerator-hour, and their output is sold by the million tokens. Both goods now have publish"
  },
  {
    "id": "rss:https://arxiv.org/abs/2309.10448",
    "domain": "金融",
    "title": "Human-AI Interactions and Societal Pitfalls",
    "url": "https://arxiv.org/abs/2309.10448",
    "source": "Francisco Castro, Jian Gao, S\\'ebastien Martin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2309.10448v5 Announce Type: replace-cross Abstract: When working with generative artificial intelligence (AI), users may see productivity gains, but the AI-generated content may not match their "
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.13323",
    "domain": "金融",
    "title": "AI Behavioral Science: A Framework and Agenda",
    "url": "https://arxiv.org/abs/2509.13323",
    "source": "Matthew O. Jackson, Qiaozhu Mei, Stephanie W. Wang, Yutong Xie, Walter Yuan, Seth Benzell, Erik Brynjolfsson, Colin F. Camerer, James Evans, Brian Jabarian, Jon Kleinberg, Juanjuan Meng, Sendhil Mullainathan, Asuman Ozdaglar, Thomas Pfeiffer, Moshe Tennenholtz, Robb Willer, Diyi Yang, Teng Ye",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2509.13323v4 Announce Type: replace-cross Abstract: We discuss the challenges and opportunities present in the rapidly emerging area of ``AI Behavioral Science.'' We frame it via three themes. F"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.15612",
    "domain": "金融",
    "title": "SoK: Market Microstructure for Decentralized Prediction Markets (DePMs)",
    "url": "https://arxiv.org/abs/2510.15612",
    "source": "Nahid Rahman, Joseph Al-Chami, Jeremy Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2510.15612v5 Announce Type: replace-cross Abstract: Decentralized prediction markets (DePMs) allow open participation in event-based wagering without fully relying on centralized intermediaries."
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.33122",
    "domain": "金融",
    "title": "The Digital-Energy Recomposition of the Kitchin Cycle: Exploratory Evidence from U.S. IT and Irish Data-Centre Series (1995-2025)",
    "url": "https://arxiv.org/abs/2610.33122",
    "source": "Bartosz Zi\\'o{\\l}ko, Adam Niedzialkowski, Bartosz Szyma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-19T05:00:00+00:00",
    "summary": "arXiv:2610.33122v2 Announce Type: replace-cross Abstract: Using quarterly FRED and CSO Ireland data over 1995Q1-2025Q4, we examine whether U.S.\\ IT investment and Irish data-centre electricity are rec"
  },
  {
    "id": "hn:50523346",
    "domain": "金融",
    "title": "The Fed Is Worried AI Agents Could Trigger a Bank Run",
    "url": "https://gizmodo.com/the-fed-is-worried-ai-agents-could-trigger-a-bank-run-2000840566",
    "source": "pera",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-11-16T21:12:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50475829",
    "domain": "金融",
    "title": "Richard Posner has died",
    "url": "https://www.law.uchicago.edu/news/senior-lecturer-richard-posner-law-and-economics-pioneer-and-former-federal-appellate-judge",
    "source": "sebg",
    "platform": "hackernews",
    "points": 52,
    "published_at": "2026-11-12T23:19:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50278678",
    "domain": "金融",
    "title": "Show HN: A proof-of-concept formalization of the IRS federal tax forms",
    "url": "https://github.com/emmilco/us-tax-model",
    "source": "RGS1811",
    "platform": "hackernews",
    "points": 84,
    "published_at": "2026-10-28T18:30:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50492178",
    "domain": "金融",
    "title": "Tesla Opens Cybercab Orders to 'Select Customers' at $29,990 Plus $299 per Month",
    "url": "https://insideevs.com/news/815473/tesla-cybercab-pricing-sales-announced/",
    "source": "iBelieve",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-11-14T00:33:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50253630",
    "domain": "金融",
    "title": "The 'Buy, Borrow and Die' Wealth Strategy Has Become a $5T Market",
    "url": "https://www.wsj.com/finance/the-buy-borrow-and-die-wealth-strategy-has-become-a-5-trillion-market-d9149a9d",
    "source": "tysone",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-10-27T01:30:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:50291902",
    "domain": "金融",
    "title": "Alphabet heads for a $500B drop in market value, biggest in its history",
    "url": "https://finance.yahoo.com/markets/article/alphabet-heads-for-a-500-billion-drop-in-market-value-the-biggest-in-its-history-134824763.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-10-29T16:39:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50372038",
    "domain": "金融",
    "title": "Harmony: Chat like Discord. Federated like email",
    "url": "https://mony.lol/",
    "source": "FinalDestiny",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-11-04T21:49:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50202671",
    "domain": "金融",
    "title": "AI compute is the new oil–and needs a new market",
    "url": "https://www.economist.com/finance-and-economics/2026/10/22/ai-compute-is-the-new-oil-and-needs-a-new-market",
    "source": "ijidak",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-10-22T23:45:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50394771",
    "domain": "金融",
    "title": "Only 16% of U.S. fast-charging stations meet federal NEVI standards (open data)",
    "url": "https://chargingnear.me/data",
    "source": "parkgraph",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-11-06T16:45:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:50394130",
    "domain": "金融",
    "title": "Tesla Ends Cybertruck Production",
    "url": "https://www.heise.de/en/news/Tesla-ends-Cybertruck-production-in-Texas-11515739.html",
    "source": "Betelbuddy",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-11-06T16:05:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:50352405",
    "domain": "金融",
    "title": "US Hedge Funds Just Sold Every AI Stock They Bought Since 2025",
    "url": "https://finance.yahoo.com/markets/stocks/articles/us-hedge-funds-just-sold-113114644.html",
    "source": "robin_reala",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-11-03T14:27:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50328462",
    "domain": "金融",
    "title": "US Jobs Pickup May Keep Fed on Track to Hike Rates Again",
    "url": "https://www.bloomberg.com/news/articles/2026-10-31/us-jobs-pickup-may-keep-fed-on-track-to-hike-rates-again",
    "source": "frank_clover",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-11-01T18:51:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50194602",
    "domain": "金融",
    "title": "Full Disk Encryption on Fedora with TPM2",
    "url": "https://www.apalrd.net/posts/2026/ent_luks/",
    "source": "speckx",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-10-22T12:46:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50236506",
    "domain": "金融",
    "title": "F45 (Fedora 45) Final Is No-Go",
    "url": "https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/EWDOYT6TOMFY4XPL5MJC2QWCDJBOR6MU/",
    "source": "gnabgib",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-25T22:09:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:50467087",
    "domain": "电子信息与芯片",
    "title": "Jensen Huang resigns",
    "url": "https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f",
    "source": "lldb",
    "platform": "hackernews",
    "points": 4059,
    "published_at": "2026-11-12T13:52:29+00:00",
    "summary": ""
  }
]
```
