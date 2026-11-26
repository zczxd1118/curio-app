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

- 今日日期：`2026-11-26`
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
  "date": "2026-11-26",
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
    "points": 2295951,
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
    "points": 2163395,
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
    "points": 1607223,
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
    "points": 1519869,
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
    "points": 1498244,
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
    "points": 917669,
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
    "points": 911938,
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
    "points": 764866,
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
    "points": 597865,
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
    "points": 491818,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1h3W76wEem",
    "domain": "AI",
    "title": "Claude(Code)桌面APP，保姆级全攻略，一期视频精通，顶级Agent软件长什么样？",
    "url": "http://www.bilibili.com/video/av117580048108571",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 460502,
    "published_at": "2026-11-08T09:14:07+00:00",
    "summary": "最近Claude桌面端（Claude Desktop） 有了一大波功能更新。随着一步步的迭代，它已经把 Claude Code 的编程、Claude Design 的设计，以及 Claude Cowork 的办公等核心能力，全部收入了同一个桌面客户端，特别是Claude Code已经从原本黑乎乎的命令行工具，进化成了桌面客户端的完全体形态。再搭配上超强的Opus5.5 模型，已经能称得上是地表顶级"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 438992,
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
    "points": 435899,
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
    "points": 429168,
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
    "points": 370680,
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
    "points": 334276,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1phaq6bEyQ",
    "domain": "AI",
    "title": "自费实测！这堆 AI Agent，到底哪个值得你用？【Agent大横评】",
    "url": "http://www.bilibili.com/video/av117346291157971",
    "source": "三颗门牙X",
    "platform": "bilibili",
    "points": 306402,
    "published_at": "2026-09-28T11:00:00+00:00",
    "summary": "现在的 AI Agent，一个比一个能吹，到底哪个真能干活？\n这期我自费充了会员，把 Codex、WorkBuddy、DeepSeek Harness、千问办公、豆包工作、Kimi、GLM、MiniMax 拉出来试了一圈。从 PPT、Excel、网页，到动画、3D 看房和交互原型，看看实际效果，也聊聊日常用起来顺不顺手。\n同一个模型，换个 Agent，效果和花费能差多少？模型够强，软件就一定好用？"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 306401,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1468g6DEWs",
    "domain": "AI",
    "title": "【全100集】(允许白嫖) 2026最全最细的AI教程零基础入门到精通，一周带你小白变大神！全程干货无废话！存下吧，少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av117115386404821",
    "source": "AI产品经理入门教程-",
    "platform": "bilibili",
    "points": 247412,
    "published_at": "2026-08-18T13:11:45+00:00",
    "summary": "【2026最新版AI教程零基础入门到精通｜配套学习路线+工具包+实战项目，看置顶评论自取】\n 本套教程专为零基础设计，从AI是什么到独立用AI解决实际问题，手把手带你系统走完从入门到精通的完整路径。 ✅ AI认知入门：什么是AI/大模型、它们能做什么不能做什么、别被营销话术忽悠\n✅ 核心技能掌握：提示词工程、多轮对话技巧、让AI稳定输出的方法论\n✅ 进阶能力突破：AI工作流搭建、智能体开发、多工具"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 241797,
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
    "points": 218092,
    "published_at": "2026-05-07T08:00:00+00:00",
    "summary": "这是你能看到的最完整的 Claude Code 零基础系统教程。\n\n\n我们将深度拆解：\n\n1️⃣ 基础入门：安装、第三方模型接入、权限系统。\n\n2️⃣ 核心进阶：Tools、Hooks、Skills、Subagents 及自动化流程。\n\n3️⃣ 项目实战：从零构建一个真实可用的 AI 网页 App。\n\n\n视频跟到最后，你不只是学会写代码，而是掌握 AI 智能体的工作逻辑。我是木子，只提供 AI 时"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 187853,
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
    "points": 166811,
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
    "points": 164818,
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
    "points": 162341,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1Qcg6zgEhU",
    "domain": "AI",
    "title": "【AI Agent实战】从零开始教你搭建Agent智能体，小白也能学会的保姆级教程！让你少走99%弯路！",
    "url": "http://www.bilibili.com/video/av114771105945944",
    "source": "讲AI的小坛",
    "platform": "bilibili",
    "points": 129091,
    "published_at": "2025-06-30T07:26:07+00:00",
    "summary": "【AI Agent实战】从零开始的智能体搭建，小白也能学会的保姆级教程！让你少走99%弯路，最简单易懂的大模型教程"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 101058,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 77204,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 69786,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 50826,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1wpxq6VEXx",
    "domain": "AI",
    "title": "【AI时代的STM32教程】AI Agent 初体验",
    "url": "http://www.bilibili.com/video/av117529699682124",
    "source": "keysking",
    "platform": "bilibili",
    "points": 48966,
    "published_at": "2026-10-30T11:52:06+00:00",
    "summary": "一句话，让 AI 帮我们完成第一个 STM32C5 程序！🚀\n本期我们一起认识 AI Agent，学习如何描述开发需求，并借助开源的 STM32C5DevSkills，让 AI 完成工程创建、芯片配置、代码编写和编译烧录，让律动小板上的小灯闪烁起来！\n也特别感谢 @意法半导体中国   对本系列教程的支持～下期我们再亲手走一遍开发流程，把 Agent 替我们完成的工作，一步步搞明白！"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 48830,
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 43516,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV1BygA6KEAi",
    "domain": "AI",
    "title": "DeepSeek Harness + ComfyUI：Agent开始自己跑AI工作流了！",
    "url": "http://www.bilibili.com/video/av117093508910174",
    "source": "啦啦啦的小黄瓜",
    "platform": "bilibili",
    "points": 42004,
    "published_at": "2026-08-14T11:01:16+00:00",
    "summary": "小助理联系方式：zhuli240614\nComfyUI节点详解网址：uinodes.com，网站使用教程：\n[ComfyUI]全网最详细节点测试以及参数详解，近千节点持续更新，纯干货教程总结梳理。\n\nMiniMax Music3模型以及工作流：https://pan.quark.cn/s/f19f1109a481\n所有模型以及工作流分享：https://pan.quark.cn/s/ef8c640"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 41632,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 35210,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 31355,
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
    "points": 30013,
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
    "points": 29082,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1p5ZbYuEzd",
    "domain": "AI",
    "title": "Cursor 新手教程： Cursor rules 让 AI 更懂你",
    "url": "http://www.bilibili.com/video/av114261833549161",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 24323,
    "published_at": "2025-04-01T08:55:51+00:00",
    "summary": "Cursor 新手教程： Cursor rules 让 AI 更懂你\n1、 什么是cursor rules\n2、配置cursor rules\n3、通用cursor rules 和自定义rules"
  },
  {
    "id": "bvid:BV1yNy5z3Em4",
    "domain": "AI",
    "title": "突发 | Claude Saga 6断层登顶！Gemini Cobalt现身！MiniMax神秘模型MIM？GLM-5.5现身仓库？ | AI日报11.22",
    "url": "http://www.bilibili.com/video/av117658666144193",
    "source": "一只AI风向标",
    "platform": "bilibili",
    "points": 23934,
    "published_at": "2026-11-22T06:31:00+00:00",
    "summary": "💡 今日趋势：Claude新模型Saga 6以2294分断层登顶网传榜单，Gemini 4 Cobalt代码现身、社区指其或为Neon内部代号，MiniMax神秘模型MIM首次破解NIST后量子候选算法并提速43400倍，GLM-5.5现身Z.ai仓库提交，各大实验室新模型密集偷跑，竞争白热化\n\n📌 今日要闻\n1. Gemini 4 Cobalt 代码曝光，社区指其为 Neon 内部代号\n2. C"
  },
  {
    "id": "bvid:BV1YS1czoEJ4",
    "domain": "AI",
    "title": "50 分钟速通 Codex 保姆级教程（含 DeepSeek 接入，无需 ChatGPT 订阅）【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av117671517489403",
    "source": "林粒粒呀",
    "platform": "bilibili",
    "points": 22986,
    "published_at": "2026-11-24T13:01:46+00:00",
    "summary": "50 分钟速通 Codex 保姆级教程\n无需 ChatGPT 订阅，国内直连 DeepSeek"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22873,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV13Asb6cE17",
    "domain": "AI",
    "title": "Claude Code 从0到1全攻略：装环境、设权限、接 MCP、写可复用技能、拆子智能体、配自动钩子，全程讲透从装到用的整套流程，建议收藏慢慢看！AI大模型",
    "url": "http://www.bilibili.com/video/av117642291582518",
    "source": "大模型分享员",
    "platform": "bilibili",
    "points": 20097,
    "published_at": "2026-11-19T09:13:50+00:00",
    "summary": "这个合集用大白话讲清 Claude Code，先说清楚它到底是什么、能帮你做什么，再带你装好并配好环境；接着讲权限与控制模式、内置命令的用法，让它按你的规矩干活；然后一步步接上 MCP 用外部工具、写 Skill 复用常用能力、配 Hooks 做自动化、拆子智能体分工，最后用 SDD 规范把需求到代码的流程固定下来。全程按真实操作演示，每集都能跟着做，遇到坑也能提前避开，建议先收藏慢慢看。"
  },
  {
    "id": "bvid:BV1ovuC66EuG",
    "domain": "AI",
    "title": "老 k 带你手搓 AI 交易智能体",
    "url": "http://www.bilibili.com/video/av117080372351441",
    "source": "老K聊交易系统",
    "platform": "bilibili",
    "points": 18552,
    "published_at": "2026-08-12T03:43:43+00:00",
    "summary": "这是一套使用 Codex开发 AI 交易智能体的系列课程，内容包括：智能体功能介绍到软件安装配置，再到开发自动化交易工具，策略优化与训练，实现交易 skill 稳定自动运行。\n课程资料包下载：www.jujijiaoyi.com"
  },
  {
    "id": "bvid:BV1wz4b6WEpd",
    "domain": "AI",
    "title": "【2026最新版】AI Agent智能体零基础全套教程（MCP+Agent Skills+多智能体+工作流自动化+项目实战）手把手教你从0搭建能干活的AI智能体",
    "url": "http://www.bilibili.com/video/av117563270961193",
    "source": "AI大模型全栈",
    "platform": "bilibili",
    "points": 18519,
    "published_at": "2026-11-06T00:00:00+00:00",
    "summary": "【全栈 AI 大模型工程师】 本套 AI 大模型系统教程专为零基础用户打造，全方位覆盖了从 LLM 底层原理到 Prompt 提示词工程、以及 2026 热门 AI Agent 智能体构建的实战全流程，不仅包含 DeepSeek、Claude、OpenClaw 等前沿模型的高效使用技巧，更深度解析了私有化部署、知识库搭建及工作流自动化的落地场景，旨在带你从零入门到精通，手把手教你如何利用 AI 大"
  },
  {
    "id": "bvid:BV1C81cz6Ed9",
    "domain": "AI",
    "title": "🚀T3 Code完整使用教程！比Orca更好用的开源AI IDE？手机下发任务！1条指令拉起多个AI线程并行改代码！统一调度Claude Code、Codex",
    "url": "http://www.bilibili.com/video/av117671802705979",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 17283,
    "published_at": "2026-11-24T14:09:25+00:00",
    "summary": "视频简介：\nT3 Code完整使用教程！比Orca更好用的开源AI IDE？手机下发任务！1条指令拉起多个AI线程并行改代码！统一调度Claude Code、Codex、Pi、Antigravity等，效率倍增\n\n从安装配置到多 Agent 工作流实战：T3 Code 完整教程，把现有 AI 编程订阅全部装进一个工作台，多模型同时处理同一项目，代码改动到底如何隔离？\n\n还在多个 AI 编程工具之间"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 17143,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV1VqHM6iEXn",
    "domain": "AI",
    "title": "从零实现自己的agent第十一期：多agent协作",
    "url": "http://www.bilibili.com/video/av117496514418485",
    "source": "小单说AI",
    "platform": "bilibili",
    "points": 16782,
    "published_at": "2026-10-25T02:00:00+00:00",
    "summary": "源码地址放这里了：\n📦 教学仓库：https:// github.com/TheSyart/claude-agent-examples\n⚔️ 实战项目：https://github.com/TheSyart/emperor-agent\n我会持续更新 Agent 教学与实战内容。\n觉得有用的话，帮忙点个 Star ⭐\n谢谢大家支持。"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15731,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "hn:50611576",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Reinstates Jensen Huang as CEO",
    "url": "https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html",
    "source": "jaz",
    "platform": "hackernews",
    "points": 2843,
    "published_at": "2026-11-23T14:00:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:50611588",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang Reinstated as Nvidia CEO",
    "url": "https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director",
    "source": "alanwong",
    "platform": "hackernews",
    "points": 1714,
    "published_at": "2026-11-23T14:01:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50493251",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia allegedly engineered scarcity by funding AI startups to buy its GPUs",
    "url": "https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus",
    "source": "speckx",
    "platform": "hackernews",
    "points": 1117,
    "published_at": "2026-11-14T02:52:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:50477231",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia employees petition to bring back Jensen Huang",
    "url": "https://www.wired.com/story/nvidia-employees-petition-for-jensen-huangs-return/",
    "source": "lavendermon",
    "platform": "hackernews",
    "points": 820,
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
    "points": 671,
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
    "points": 486,
    "published_at": "2026-11-15T23:55:55+00:00",
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
    "points": 453,
    "published_at": "2026-11-14T22:26:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:50638503",
    "domain": "AI 算力 / 半导体",
    "title": "Show HN: Old Nvidia and ATI tech demos, running again in the browser",
    "url": "https://gpu-demo-gallery.pages.dev/",
    "source": "arkits",
    "platform": "hackernews",
    "points": 347,
    "published_at": "2026-11-25T04:31:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50487864",
    "domain": "AI 算力 / 半导体",
    "title": "$11.4M in Nvidia hardware vanishes during shipment from CA to TX",
    "url": "https://www.freightwaves.com/news/11-4-million-in-nvidia-hardware-vanishes-during-shipment-from-california-to-texas",
    "source": "crescit_eundo",
    "platform": "hackernews",
    "points": 387,
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
    "id": "hn:50626861",
    "domain": "AI 算力 / 半导体",
    "title": "Who in Washington owns and trades Nvidia stock",
    "url": "https://www.kadoa.com/congress/insights/trump-nvidia",
    "source": "hubraumhugo",
    "platform": "hackernews",
    "points": 291,
    "published_at": "2026-11-24T11:51:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50581438",
    "domain": "AI 算力 / 半导体",
    "title": "US SEC's Nvidia probe is examining potential accounting issues – sources",
    "url": "https://www.marketscreener.com/news/us-sec-s-nvidia-probe-is-examining-potential-accounting-issues-sources-say-ce785ed3dd8ff627",
    "source": "ftchd",
    "platform": "hackernews",
    "points": 309,
    "published_at": "2026-11-20T20:22:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:50518567",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia was in trouble before the Jensen Huang mess",
    "url": "https://www.wired.com/story/nvidia-was-already-in-trouble-before-the-jensen-huang-mess/",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 291,
    "published_at": "2026-11-16T15:24:09+00:00",
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
    "id": "hn:50630245",
    "domain": "AI 算力 / 半导体",
    "title": "Ex-Nvidia partner Megaspeed hit with U.S. Commerce Department export ban",
    "url": "https://www.upi.com/Top_News/US/2026/11/24/NVIDIA-partner-Megaspeed/1701795520063/",
    "source": "nephihaha",
    "platform": "hackernews",
    "points": 128,
    "published_at": "2026-11-24T16:08:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50511982",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang might return to Nvidia as CEO",
    "url": "https://www.reuters.com/world/china/jensen-huang-discusses-comeback-nvidia-ceo-with-allies-ft-reports-2026-11-15/",
    "source": "YakubYilmaz",
    "platform": "hackernews",
    "points": 178,
    "published_at": "2026-11-15T23:24:53+00:00",
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
    "id": "hn:50497155",
    "domain": "AI 算力 / 半导体",
    "title": "Serving GLM-5.3 at 607.8 tok/s across two Nvidia DGX stations with vLLM",
    "url": "https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/",
    "source": "wondersky",
    "platform": "hackernews",
    "points": 150,
    "published_at": "2026-11-14T14:09:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50509883",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang discusses comeback as Nvidia CEO with allies",
    "url": "https://www.ft.com/content/45383d86-33c4-4d99-86e5-5e058d3567c1",
    "source": "eyalitki",
    "platform": "hackernews",
    "points": 136,
    "published_at": "2026-11-15T19:31:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:50629620",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia board's Huang reversal raises doubts about independence, critics say",
    "url": "https://www.reuters.com/legal/transactional/nvidia-boards-huang-reversal-raises-doubts-about-independence-critics-say-2026-11-24/",
    "source": "onemoresoop",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-11-24T15:28:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50618490",
    "domain": "AI 算力 / 半导体",
    "title": "Congress shreds Nvidia's 'outrageous' return of Huang: 'Failure of character'",
    "url": "https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-congress-trump.html",
    "source": "MilnerRoute",
    "platform": "hackernews",
    "points": 69,
    "published_at": "2026-11-23T20:13:18+00:00",
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
    "id": "hn:50648903",
    "domain": "AI 算力 / 半导体",
    "title": "S&P warns Nvidia's board may be compromised",
    "url": "https://www.reuters.com/technology/us-finds-no-evidence-china-directed-executive-spy-nvidia-ceo-wsj-reports-2026-11-25/",
    "source": "narmiouh",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-11-25T23:03:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50621127",
    "domain": "AI 算力 / 半导体",
    "title": "Short Nvidia Fund Halted After 91% Wipeout",
    "url": "https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-23-2026/card/short-nvidia-fund-halted-after-91-wipeout-myoKEHNFkGcseucDUC48",
    "source": "devy",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-11-23T23:36:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50616243",
    "domain": "AI 算力 / 半导体",
    "title": "Trump Is Said to Have Directed Effort to Reinstate Nvidia Chief",
    "url": "https://www.nytimes.com/2026/11/23/us/politics/trump-nvidia-huang.html",
    "source": "johnny313",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-11-23T18:03:59+00:00",
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
    "id": "rss:https://www.eetimes.com/eu-rules-bring-new-safety-requirements-for-farm-robots/",
    "domain": "AI 算力 / 半导体",
    "title": "EU Rules Bring New Safety Requirements for Farm Robots",
    "url": "https://www.eetimes.com/eu-rules-bring-new-safety-requirements-for-farm-robots/",
    "source": "Liam Critchley",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T08:55:48+00:00",
    "summary": "New EU regulations will tighten safety and compliance requirements for farms deploying AI-powered robots and autonomous machinery. The post EU Rules Bring New Safety Requirements for Farm Robots appea"
  },
  {
    "id": "rss:https://www.eetimes.com/unikey-electronics-named-recom-global-authorized-distributor-at-electronica-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "Unikey Electronics Named RECOM Global Authorized Distributor at electronica 2026",
    "url": "https://www.eetimes.com/unikey-electronics-named-recom-global-authorized-distributor-at-electronica-2026/",
    "source": "Unikey Electronics Pte. Ltd.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T08:31:51+00:00",
    "summary": "Unikey signs a distribution agreement with RECOM, launching an online sourcing platform, and starting an industry interview series. The post Unikey Electronics Named RECOM Global Authorized Distributo"
  },
  {
    "id": "rss:https://www.eetimes.com/infineon-coolset-sip-enables-efficient-first-time-right-auxiliary-power-designs/",
    "domain": "AI 算力 / 半导体",
    "title": "Infineon CoolSET™ SiP Enables Efficient, ‘First-Time-Right’ Auxiliary Power Designs",
    "url": "https://www.eetimes.com/infineon-coolset-sip-enables-efficient-first-time-right-auxiliary-power-designs/",
    "source": "Hubert Baierl, marketing director, Infineon Technologies AG",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T22:02:21+00:00",
    "summary": "Auxiliary supply is indispensable, and designers need to facilitate high-efficiency solutions across a wide range of loads, in a limited PCB area, and deliver first-time-right designs. The post Infine"
  },
  {
    "id": "rss:https://www.eetimes.com/mcrps-power-supply-for-enterprise-data-centers/",
    "domain": "AI 算力 / 半导体",
    "title": "MCRPS Power Supply for Enterprise Data Centers",
    "url": "https://www.eetimes.com/mcrps-power-supply-for-enterprise-data-centers/",
    "source": "Antonello Laneve, Manuel Escudero, David Meneses, M.A. Kutschak, Theodoros Mouselinos, Alex Rossi, and Sam Abdel-Rahman, all at Infineon Technologies AG",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T20:36:47+00:00",
    "summary": "The 5.6 kW MCRPS reference design from Infineon provides a viable solution for next-generation common redundant PSUs in enterprise servers. The post MCRPS Power Supply for Enterprise Data Centers appe"
  },
  {
    "id": "rss:https://www.eetimes.com/turning-optical-telemetry-into-cluster-reliability-integrating-link-health-data-into-monitoring-and-ticketing/",
    "domain": "AI 算力 / 半导体",
    "title": "Turning Optical Telemetry into Cluster Reliability: Integrating Link Health Data into Monitoring and Ticketing",
    "url": "https://www.eetimes.com/turning-optical-telemetry-into-cluster-reliability-integrating-link-health-data-into-monitoring-and-ticketing/",
    "source": "Credo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T18:00:22+00:00",
    "summary": "Explore how integrating optical link health data into monitoring and ticketing can help teams improve cluster reliability. The post Turning Optical Telemetry into Cluster Reliability: Integrating Link"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-makes-formal-verification-practical/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Makes Formal Verification Practical",
    "url": "https://www.eetimes.com/ai-makes-formal-verification-practical/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T17:34:58+00:00",
    "summary": "AI model startup Harmonic is expanding into formal verification for software and hardware. The post AI Makes Formal Verification Practical appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/understanding-accuracy-and-resolution-for-magnetic-angle-sensors/",
    "domain": "AI 算力 / 半导体",
    "title": "Understanding Accuracy and Resolution for Magnetic Angle Sensors",
    "url": "https://www.eetimes.com/understanding-accuracy-and-resolution-for-magnetic-angle-sensors/",
    "source": "Monolithic Power Systems, Inc. (MPS)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T14:00:00+00:00",
    "summary": "Learn how magnetic angle sensor accuracy and resolution affect position measurement, and explore key factors for precise, reliable sensing applications. The post Understanding Accuracy and Resolution "
  },
  {
    "id": "rss:https://www.eetimes.com/amd-tackles-dram-shortages-with-ai-and-flash-storage/",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Tackles DRAM Shortages with AI and Flash Storage",
    "url": "https://www.eetimes.com/amd-tackles-dram-shortages-with-ai-and-flash-storage/",
    "source": "Lucas Sideco",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T14:00:00+00:00",
    "summary": "AMD MEXT uses AI to park cold memory pages in flash, cutting DRAM costs and easing data center shortages. The post AMD Tackles DRAM Shortages with AI and Flash Storage appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/winbond-widens-edge-ai-reach-certifies-nor-flash/",
    "domain": "AI 算力 / 半导体",
    "title": "Winbond Widens Edge AI Reach, Certifies NOR Flash",
    "url": "https://www.eetimes.com/winbond-widens-edge-ai-reach-certifies-nor-flash/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T08:59:51+00:00",
    "summary": "Winbond is pairing bandwidth and density to meet the edge’s demand for faster, safer memory without the custom-design price tag. The post Winbond Widens Edge AI Reach, Certifies NOR Flash appeared fir"
  },
  {
    "id": "rss:https://www.eetimes.com/southchip-showcases-automotive-power-charging-and-load-control-solutions-at-electronica-munich/",
    "domain": "AI 算力 / 半导体",
    "title": "Southchip Showcases Automotive Power, Charging, and Load-Control Solutions at electronica Munich",
    "url": "https://www.eetimes.com/southchip-showcases-automotive-power-charging-and-load-control-solutions-at-electronica-munich/",
    "source": "Christopher McGrady",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T08:32:46+00:00",
    "summary": "Southchip presented its automotive PMICs, 240W USB charging, wireless charging, ambient lighting, and high-side drivers at electronica Munich. The post Southchip Showcases Automotive Power, Charging, "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-dominant-ryzen-7-9800x3d-plummets-to-all-time-low-of-usd369-at-amazon-astonishing-gaming-performance-for-am5",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen 7 9800X3D plummets to an all-time low of $369 at Amazon",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-dominant-ryzen-7-9800x3d-plummets-to-all-time-low-of-usd369-at-amazon-astonishing-gaming-performance-for-am5",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T12:00:47+00:00",
    "summary": "One of the very best gaming CPUs on the market is now cheaper than ever."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/export-banned-nvidia-blackwell-b300-servers-are-openly-for-sale-in-china-for-up-to-usd3-4-million-a-5x-to-6x-markup-over-u-s-prices",
    "domain": "AI 算力 / 半导体",
    "title": "Export-banned Nvidia Blackwell B300 servers are openly for sale in China for up to $3.4 million",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/export-banned-nvidia-blackwell-b300-servers-are-openly-for-sale-in-china-for-up-to-usd3-4-million-a-5x-to-6x-markup-over-u-s-prices",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T12:00:00+00:00",
    "summary": "It's easy to find Blackwell chips for sale in China even today — uneven enforcement of export controls and gray market trading ensure continued availability"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/grab-a-prebuilt-rtx-5060-ti-gaming-pc-for-under-usd1-500-at-amazon-20-percent-off-nets-you-a-core-i7-14400f-16gb-ddr5-memory-and-1-tb-of-storage",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a prebuilt RTX 5060 Ti gaming PC for under $1,300 at Amazon",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/grab-a-prebuilt-rtx-5060-ti-gaming-pc-for-under-usd1-500-at-amazon-20-percent-off-nets-you-a-core-i7-14400f-16gb-ddr5-memory-and-1-tb-of-storage",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T11:45:00+00:00",
    "summary": "If you're looking for an entry-level prebuilt gaming PC this Black Friday, you can't go wrong with Cyberpower's Gamer Xtreme, now just $1,299 at Amazon. I"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/take-two-wipes-out-3-007-gta-6-pc-port-repos-from-github-in-massive-dmca-crackdown-as-ai-tools-fuel-wave-of-unofficial-builds",
    "domain": "AI 算力 / 半导体",
    "title": "Take-Two wipes out 3,007 GTA 6 PC port repos from GitHub in massive DMCA crackdown",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/take-two-wipes-out-3-007-gta-6-pc-port-repos-from-github-in-massive-dmca-crackdown-as-ai-tools-fuel-wave-of-unofficial-builds",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T11:30:00+00:00",
    "summary": "Despite Take-Two's effort to shut down projects to port GTA VI, multiple projects have reported progress and could now run the game at lower frame rates on PCs."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/samsungs-giant-57-inch-ultra-sized-display-tumbles-to-usd1-349-curved-1000r-dual-4k-display-is-the-ultimate-desktop-monitor",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung's giant 57-inch ultra-sized display tumbles to $1,349",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/samsungs-giant-57-inch-ultra-sized-display-tumbles-to-usd1-349-curved-1000r-dual-4k-display-is-the-ultimate-desktop-monitor",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T11:20:56+00:00",
    "summary": "Two become one with this giant 57-inch dual-4K behemoth from Samsung. The Odyssey Neo G9's price is slashed by $750 on Amazon."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/trump-says-a-pardon-for-nvidia-ceo-jensen-huang-is-always-an-option-urges-him-not-to-plead-the-fifth-ahead-of-house-committee-grilling",
    "domain": "AI 算力 / 半导体",
    "title": "Trump says a pardon for Nvidia CEO Jensen Huang is 'always an option'",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/trump-says-a-pardon-for-nvidia-ceo-jensen-huang-is-always-an-option-urges-him-not-to-plead-the-fifth-ahead-of-house-committee-grilling",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T11:00:00+00:00",
    "summary": "U.S. President Donald Trump says that he could pardon Nvidia CEO Jensen Huang if he finds himself in legal hot water over his affair with an alleged Chinese spy. Huang is set to meet with the House Fo"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tsmc-files-for-usd22-6-billion-texas-fab-campus-with-local-tax-breaks-just-one-county-over-from-musks-terafab-proposed-brazos-county-plant-wont-make-2nm-class-chips-until-2031",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC’s $22.6 billion Texas plan wouldn’t make 2nm-or-better chips until 2031",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-files-for-usd22-6-billion-texas-fab-campus-with-local-tax-breaks-just-one-county-over-from-musks-terafab-proposed-brazos-county-plant-wont-make-2nm-class-chips-until-2031",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T10:30:00+00:00",
    "summary": "TSMC’s Texas filing describes a $22.6 billion project in Brazos County for 2nm or more advanced chips, starting production in 2031."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/save-usd1300-on-this-rtx-5090-equipped-16-inch-lenovo-legion-pro-7i-gaming-laptop-core-ultra-9-system-with-1tb-storage-and-32gb-of-ddr5-drops-to-usd3999",
    "domain": "AI 算力 / 半导体",
    "title": "Save $1300 on this RTX 5090-equipped 16-inch Lenovo Legion Pro 7i gaming laptop",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/save-usd1300-on-this-rtx-5090-equipped-16-inch-lenovo-legion-pro-7i-gaming-laptop-core-ultra-9-system-with-1tb-storage-and-32gb-of-ddr5-drops-to-usd3999",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T10:30:00+00:00",
    "summary": "If you're looking to gear up with a powerful new gaming laptop this Black Friday, Lenovo's 16-inch Legion Pro 7i is now $1300 off at B&amp;H."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/score-a-huge-usd1-700-discount-on-an-rtx-5080-gaming-pc-from-hp-now-usd2-699-99-massive-deal-on-a-hyperx-omen-rig-with-a-24-core-intel-cpu-and-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Score a huge $1,700 discount on an RTX 5080 gaming PC from HP, now $2,699.99",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/score-a-huge-usd1-700-discount-on-an-rtx-5080-gaming-pc-from-hp-now-usd2-699-99-massive-deal-on-a-hyperx-omen-rig-with-a-24-core-intel-cpu-and-1tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T10:15:00+00:00",
    "summary": "A huge discount at HP has knocked $1,700 off a HyperX Omen 35L rig with an RTX 5080 and Intel Core Ultra 7 270K, bringing it down to $2,699.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/black-friday-2026-day-two",
    "domain": "AI 算力 / 半导体",
    "title": "Best Black Friday 2026 tech deals",
    "url": "https://www.tomshardware.com/live/news/black-friday-2026-day-two",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T07:23:03+00:00",
    "summary": "All the best Black Friday deals for tech and PC hardware."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/get-an-rtx-5060-prebuilt-for-just-usd750-in-deal-that-seems-too-good-to-be-true-deep-usd650-discount-on-gaming-pc-offers-core-i5-14400f-16gb-ddr4-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Get an RTX 5060 prebuilt for just $750 in deal that seems too good to be true",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/get-an-rtx-5060-prebuilt-for-just-usd750-in-deal-that-seems-too-good-to-be-true-deep-usd650-discount-on-gaming-pc-offers-core-i5-14400f-16gb-ddr4-and-a-1tb-ssd",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T23:18:00+00:00",
    "summary": "Walmart has an exceptional deal on an RTX 5060-powered gaming desktop, which is on sale for just $750 right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/get-2tb-of-pcie-5-0-storage-for-less-than-usd300-in-stellar-crucial-p510-sale-drive-is-available-for-just-usd294-99-less-than-some-1tb-alternatives",
    "domain": "AI 算力 / 半导体",
    "title": "Get 2TB of PCIe 5.0 storage for less than $300 in stellar Crucial P510 sale",
    "url": "https://www.tomshardware.com/pc-components/ssds/get-2tb-of-pcie-5-0-storage-for-less-than-usd300-in-stellar-crucial-p510-sale-drive-is-available-for-just-usd294-99-less-than-some-1tb-alternatives",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T22:10:45+00:00",
    "summary": "Snag 2TB of PCIe 5.0 storage for just $294.99 with a deal on the Crucial P510 SSD over at Adorama."
  },
  {
    "id": "hn:50552424",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Neon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/",
    "source": "yigitdemirag",
    "platform": "hackernews",
    "points": 1071,
    "published_at": "2026-11-18T21:34:07+00:00",
    "summary": ""
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
    "id": "hn:50403097",
    "domain": "大厂 AI 动态",
    "title": "Every Mac comes with an (undocumented) family member classifier",
    "url": "https://8rank.ai/game/apple-intelligence-personal-knowledge-graph",
    "source": "infwhispers",
    "platform": "hackernews",
    "points": 873,
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
    "points": 576,
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
    "points": 571,
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
    "points": 509,
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
    "id": "hn:50568130",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Neon is the new #1 on the Models Engineering Index",
    "url": "https://git-aarvin.github.io/mei/",
    "source": "hn-aarvin",
    "platform": "hackernews",
    "points": 376,
    "published_at": "2026-11-19T23:35:35+00:00",
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
    "id": "hn:50550415",
    "domain": "大厂 AI 动态",
    "title": "Genie 4 is now available",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/",
    "source": "leumon",
    "platform": "hackernews",
    "points": 294,
    "published_at": "2026-11-18T18:49:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:50577901",
    "domain": "大厂 AI 动态",
    "title": "Google workers tell their employer not to punish schools that don't want AI",
    "url": "https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 285,
    "published_at": "2026-11-20T16:59:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50638320",
    "domain": "大厂 AI 动态",
    "title": "Gemini refused to give me the lyrics to Twinkle Twinkle Little Star",
    "url": "https://www.comentr.com/technology/01M88DWQ0R4NCMYR17AFEWRG1F",
    "source": "hoodied",
    "platform": "hackernews",
    "points": 218,
    "published_at": "2026-11-25T04:03:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:50541790",
    "domain": "大厂 AI 动态",
    "title": "Why is Gemini 4 Carbon taking so long?",
    "url": "https://kernel.dev/blog/why-is-gemini-4-carbon-taking-so-long/",
    "source": "deenadz",
    "platform": "hackernews",
    "points": 288,
    "published_at": "2026-11-18T04:14:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:50554374",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Neon looks like an Opus 5.5 competitor",
    "url": "https://micjm.com/blog/gemini-4-neon-looks-like-a-top-model/",
    "source": "seizethecheese",
    "platform": "hackernews",
    "points": 259,
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
    "id": "hn:50569519",
    "domain": "大厂 AI 动态",
    "title": "What Comes After AGI?",
    "url": "https://institute.deepmind.com/essays/what-comes-after-agi/",
    "source": "jdkee",
    "platform": "hackernews",
    "points": 178,
    "published_at": "2026-11-20T02:44:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50557885",
    "domain": "大厂 AI 动态",
    "title": "DeepMind Employees Are Unionising",
    "url": "https://www.gdmunion.co.uk",
    "source": "nervai",
    "platform": "hackernews",
    "points": 124,
    "published_at": "2026-11-19T09:28:56+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/news/1043078/x-parental-controls-features",
    "domain": "大厂 AI 动态",
    "title": "X is finally getting its first parental controls",
    "url": "https://www.theverge.com/news/1043078/x-parental-controls-features",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T10:45:50+00:00",
    "summary": "X is finally rolling out parental controls that allow parents and guardians to manage teens' accounts on the platform. While teens will retain ownership of their own account, parents and guardians wil"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1042620/character-ai-sale-state-ags-block-selling-users-chats",
    "domain": "大厂 AI 动态",
    "title": "42 state AGs are trying to stop Character.AI from selling users’ chats",
    "url": "https://www.theverge.com/policy/1042620/character-ai-sale-state-ags-block-selling-users-chats",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T09:54:40+00:00",
    "summary": "A coalition of 42 state attorneys general is trying to prevent Character.AI from selling off user data as it navigates Chapter 11 bankruptcy proceedings. In a deluge of nearly identical press releases"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1042938/google-home-familiar-faces-onn-cameras",
    "domain": "大厂 AI 动态",
    "title": "Now Google’s Familiar Faces AI feature works on Walmart’s $35 smart home camera too",
    "url": "https://www.theverge.com/tech/1042938/google-home-familiar-faces-onn-cameras",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T00:04:34+00:00",
    "summary": "A couple of Walmart's budget-friendly smart home cameras will be able to recognize people around your house now using Google's familiar face detection feature. A new Google Home update brings Familiar"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1042870/amazon-recall-order-cpsc",
    "domain": "大厂 AI 动态",
    "title": "Amazon loses its latest attempt to get out of handling more recall notices",
    "url": "https://www.theverge.com/tech/1042870/amazon-recall-order-cpsc",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T23:56:44+00:00",
    "summary": "Amazon is on the hook to recall more than 400,000 hazardous products after losing its legal battle against the US Consumer Product Safety Commission (CPSC). The US District Court for the District of M"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1042221/google-my-channel-ai-video-patent",
    "domain": "大厂 AI 动态",
    "title": "Google’s patent for custom AI video feeds paints a bleak picture of entertainment’s future",
    "url": "https://www.theverge.com/entertainment/1042221/google-my-channel-ai-video-patent",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T21:51:26+00:00",
    "summary": "Last year, Google filed a patent for a system called My Channel that's designed to create feeds filled with personalized, AI-generated videos and advertisements based on information the company knows "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1021917/best-gifts-for-travelers-2026",
    "domain": "大厂 AI 动态",
    "title": "The Verge’s 2026 holiday gift guide for travelers",
    "url": "https://www.theverge.com/gadgets/1021917/best-gifts-for-travelers-2026",
    "source": "Ryan Waniata",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T21:48:00+00:00",
    "summary": "Everyone has that traveler in their life. That person who feels more at home on a 14-hour train ride than a quiet Sunday on the couch. They speak multiple languages, have a gut like a goat, and make f"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1042532/whatsapp-scheduled-messages",
    "domain": "大厂 AI 动态",
    "title": "WhatsApp’s new scheduled messages let you choose the right time to send",
    "url": "https://www.theverge.com/tech/1042532/whatsapp-scheduled-messages",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T20:31:48+00:00",
    "summary": "WhatsApp's 3 billion users are getting an option that Meta says is one of the most requested features, with the ability to schedule messages in advance for both private conversations and group chats. "
  },
  {
    "id": "rss:https://www.theverge.com/science/1042109/us-army-detonation-lead-azide-explosives-iowa-ammunition-plant",
    "domain": "大厂 AI 动态",
    "title": "EPA reports ‘zero’ airborne lead following controlled Army detonation in Iowa",
    "url": "https://www.theverge.com/science/1042109/us-army-detonation-lead-azide-explosives-iowa-ammunition-plant",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T19:45:51+00:00",
    "summary": "Saying it was necessary to prevent the possible spontaneous explosion of a stockpile of material used in igniters and blasting caps, the US Army conducted a controlled detonation of over 9,700 pounds "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1042409/1password-data-breach-leak",
    "domain": "大厂 AI 动态",
    "title": "1Password breach leaked customer names and emails, but not passwords",
    "url": "https://www.theverge.com/tech/1042409/1password-data-breach-leak",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T19:10:15+00:00",
    "summary": "1Password says a hacker stole customer names and email addresses after gaining access to its backend systems. The breach didn't expose passwords or other information stored in customer vaults, but cou"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1041460/fairphone-6-plus-repairable-phone-black-friday-2026-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The Fairphone 6 Plus is modular, repairable, and $100 off right now",
    "url": "https://www.theverge.com/gadgets/1041460/fairphone-6-plus-repairable-phone-black-friday-2026-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T18:00:00+00:00",
    "summary": "Unlike most smartphones, the Fairphone 6 Plus is designed for home repair, with easily replaceable parts that could help extend its lifespan well into the future. That makes its midrange price point e"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/25/sp-considers-nvidia-credit-downgrade-over-governance-and-key-man-risks/",
    "domain": "大厂 AI 动态",
    "title": "S&P considers Nvidia credit downgrade over governance and ‘key man’ risks",
    "url": "https://techcrunch.com/2026/11/25/sp-considers-nvidia-credit-downgrade-over-governance-and-key-man-risks/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T22:44:32+00:00",
    "summary": "The credit rating agency may lower Nvidia's credit rating to AA-, the fourth-highest rating."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/25/fcc-approves-spacex-plan-to-put-ai-data-centers-in-space/",
    "domain": "大厂 AI 动态",
    "title": "FCC approves SpaceX plan to put AI data centers in space",
    "url": "https://techcrunch.com/2026/11/25/fcc-approves-spacex-plan-to-put-ai-data-centers-in-space/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T20:56:44+00:00",
    "summary": "The FCC dismissed some of the key concerns raised by opponents, including potential threats to scientific research, because the agency determined they fell outside its regulatory authority."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/25/openai-says-heavy-chatgpt-users-may-hit-limits-sooner-as-it-merges-chat-and-work/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI says heavy ChatGPT users may hit limits sooner as it merges Chat and Work",
    "url": "https://techcrunch.com/2026/11/25/openai-says-heavy-chatgpt-users-may-hit-limits-sooner-as-it-merges-chat-and-work/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T20:03:27+00:00",
    "summary": "OpenAI will introduce a single usage meter across ChatGPT as it combines the Chat and Work experiences."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/25/jensen-huang-broke-nvidias-code-of-conduct-and-his-employees-may-not-forget-it/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang broke Nvidia’s code of conduct, and his employees may not forget it",
    "url": "https://techcrunch.com/2026/11/25/jensen-huang-broke-nvidias-code-of-conduct-and-his-employees-may-not-forget-it/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T19:54:57+00:00",
    "summary": "Most codes of conduct serve as a reflection of corporate culture. In Nvidia's case, that could have consequences."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/25/the-canceled-tesla-cybertruck-is-the-fastest-selling-used-truck-in-america/",
    "domain": "大厂 AI 动态",
    "title": "The canceled Tesla Cybertruck is the fastest-selling used truck in America",
    "url": "https://techcrunch.com/2026/11/25/the-canceled-tesla-cybertruck-is-the-fastest-selling-used-truck-in-america/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T19:54:32+00:00",
    "summary": "The Tesla Cybertruck was the fastest-selling used truck last month, averaging just 39.1 days on the market compared to 65.5 days for trucks overall."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/25/anthropics-dario-amodei-calls-accusations-of-surrendering-human-control-to-ai-absurd/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s Dario Amodei calls accusations of surrendering human control to AI ‘absurd’",
    "url": "https://techcrunch.com/2026/11/25/anthropics-dario-amodei-calls-accusations-of-surrendering-human-control-to-ai-absurd/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T19:44:24+00:00",
    "summary": "Anthropic CEO Dario Amodei pushes back against rivals’ accusations that he favors surrendering human agency to AI, even as leading AI companies increasingly automate their own research and model devel"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/25/1password-said-hackers-broke-into-its-internal-systems-but-customer-passwords-are-safe/",
    "domain": "大厂 AI 动态",
    "title": "1Password said hackers broke into its internal systems, but customer passwords are safe",
    "url": "https://techcrunch.com/2026/11/25/1password-said-hackers-broke-into-its-internal-systems-but-customer-passwords-are-safe/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T18:49:52+00:00",
    "summary": "The password manager maker said an attacker gained access to an employee's corporate account and took some information about customers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/25/want-to-buy-your-kid-an-ai-toy-this-christmas-not-in-new-york/",
    "domain": "大厂 AI 动态",
    "title": "Want to buy your kid an AI toy this Christmas? Not in New York",
    "url": "https://techcrunch.com/2026/11/25/want-to-buy-your-kid-an-ai-toy-this-christmas-not-in-new-york/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T18:11:46+00:00",
    "summary": "New York has banned AI chatbot toys for five years as new research from Common Sense Media reveals troubling safety failures, including exposure to inappropriate content and risks to emotional develop"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/25/doj-accuses-former-cyber-executive-of-defrauding-ransomware-victims-by-secretly-paying-hackers/",
    "domain": "大厂 AI 动态",
    "title": "DOJ accuses former cyber executive of defrauding ransomware victims by secretly paying hackers",
    "url": "https://techcrunch.com/2026/11/25/doj-accuses-former-cyber-executive-of-defrauding-ransomware-victims-by-secretly-paying-hackers/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T17:36:51+00:00",
    "summary": "U.S. prosecutors accused the former executive of defrauding victims of ransomware by paying the hackers, charging victims more, and pocketing the difference."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/25/state-ags-fight-character-ais-plan-to-auction-off-users-private-chats/",
    "domain": "大厂 AI 动态",
    "title": "Character.AI’s plan to auction off users’ private chats challenged by state AGs",
    "url": "https://techcrunch.com/2026/11/25/state-ags-fight-character-ais-plan-to-auction-off-users-private-chats/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T17:35:58+00:00",
    "summary": "The proposed Character.ai bankruptcy sale includes sensitive personal data from more than 21 million U.S. accounts, including 2.1 million registered to minors, the state AGs said."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/25/xs-latest-update-for-creators-focuses-on-vertical-video/",
    "domain": "大厂 AI 动态",
    "title": "X’s latest update for creators focuses on vertical video",
    "url": "https://techcrunch.com/2026/11/25/xs-latest-update-for-creators-focuses-on-vertical-video/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T17:28:29+00:00",
    "summary": "As short-form video ramps up in popularity, X's new creation tools are part of its effort to compete with YouTube and Instagram."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/25/whatsapp-now-lets-you-schedule-messages-in-group-and-individual-chats/",
    "domain": "大厂 AI 动态",
    "title": "WhatsApp now lets you schedule messages in group and individual chats",
    "url": "https://techcrunch.com/2026/11/25/whatsapp-now-lets-you-schedule-messages-in-group-and-individual-chats/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T16:57:51+00:00",
    "summary": "Users can schedule messages from 10 minutes later to after 14 days."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/25/allstate-suffers-multi-day-tech-outage-ahead-of-thanksgiving/",
    "domain": "大厂 AI 动态",
    "title": "Allstate suffers multiday tech outage ahead of Thanksgiving",
    "url": "https://techcrunch.com/2026/11/25/allstate-suffers-multi-day-tech-outage-ahead-of-thanksgiving/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T15:08:37+00:00",
    "summary": "The disruption comes at a particularly bad time for the insurance giant, as millions of Americans prepare to travel for the Thanksgiving holiday weekend."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/25/todoist-confirms-6-of-customers-details-were-stolen-in-data-breach/",
    "domain": "大厂 AI 动态",
    "title": "Todoist confirms 6% of customers’ details were stolen in data breach",
    "url": "https://techcrunch.com/2026/11/25/todoist-confirms-6-of-customers-details-were-stolen-in-data-breach/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T14:20:28+00:00",
    "summary": "Todoist said a hacker gained access to its production systems and stole customer data, including email IDs, password hashes, and account creation dates."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/25/amazon-and-meta-reportedly-in-talks-to-lift-blockade-on-ai-agent-muse/",
    "domain": "大厂 AI 动态",
    "title": "Amazon and Meta reportedly in talks to lift blockade on AI agent Muse",
    "url": "https://techcrunch.com/2026/11/25/amazon-and-meta-reportedly-in-talks-to-lift-blockade-on-ai-agent-muse/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T14:10:18+00:00",
    "summary": "Amazon and Meta are discussing a potential deal that would end a two-month-long blockade of Muse."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/25/flipkart-ceo-kalyan-krishnamurthy-to-step-down-next-week-amid-ipo-uncertainty/",
    "domain": "大厂 AI 动态",
    "title": "Flipkart CEO Kalyan Krishnamurthy to step down next week amid IPO uncertainty",
    "url": "https://techcrunch.com/2026/11/25/flipkart-ceo-kalyan-krishnamurthy-to-step-down-next-week-amid-ipo-uncertainty/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T13:08:19+00:00",
    "summary": "Flipkart's product and technology chief Balaji Thiagarajan will lead the company alongside its board until a successor is found."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/25/the-questions-jensen-huang-and-nvidia-will-still-have-to-answer-about-megaspeed/",
    "domain": "大厂 AI 动态",
    "title": "The questions Jensen Huang and Nvidia will still have to answer about Megaspeed",
    "url": "https://techcrunch.com/2026/11/25/the-questions-jensen-huang-and-nvidia-will-still-have-to-answer-about-megaspeed/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T13:00:00+00:00",
    "summary": "The central question for investigators is what Nvidia knew about where those chips ended up and whether Huang's affair with a Megaspeed executive gave the company reason to doubt Megaspeed's assurance"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/yales-sonnenfeld-nvidia-is-a-detriment-to-u-s-industrial-might-not-a-champion/",
    "domain": "大厂 AI 动态",
    "title": "Yale’s Sonnenfeld: Nvidia is a ‘detriment’ to US industrial might — not a champion",
    "url": "https://techcrunch.com/2026/11/24/yales-sonnenfeld-nvidia-is-a-detriment-to-u-s-industrial-might-not-a-champion/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T00:12:02+00:00",
    "summary": "Yale's Jeffrey Sonnenfeld warns that what the market cheered Monday, Jensen Huang's White House–backed return as Nvidia's CEO and board member, could prove a giant mistake, exposing the directors to \""
  },
  {
    "id": "hn:50465829",
    "domain": "股票",
    "title": "Anthropic IPO",
    "url": "https://ipo.anthropic.com/us/",
    "source": "josephljohnston",
    "platform": "hackernews",
    "points": 1009,
    "published_at": "2026-11-12T11:46:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:50556287",
    "domain": "股票",
    "title": "Ruby2ßhell: Pre-authentication RCE on stock Rails",
    "url": "https://verialabs.com/ruby2shell/",
    "source": "jdns",
    "platform": "hackernews",
    "points": 409,
    "published_at": "2026-11-19T05:09:11+00:00",
    "summary": ""
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
    "id": "hn:50394906",
    "domain": "股票",
    "title": "Anthropic IPO buyers see valuation as low as $1.1T",
    "url": "https://www.bloomberg.com/news/articles/2026-11-06/anthropic-ipo-valuation-expectations-pressured-after-ai-rout",
    "source": "dgellow",
    "platform": "hackernews",
    "points": 322,
    "published_at": "2026-11-06T16:54:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:50620721",
    "domain": "股票",
    "title": "Freeing the iPod Nano 5G",
    "url": "https://viktorkrapivin.com/blog/nano5g-priv-prvd",
    "source": "rpm_conservatio",
    "platform": "hackernews",
    "points": 148,
    "published_at": "2026-11-23T23:03:13+00:00",
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
    "id": "hn:50583254",
    "domain": "股票",
    "title": "Nasdaq erases all 2026 gains",
    "url": "https://www.cnbc.com/2026/11/19/stock-market-today-live-updates.html",
    "source": "mv4",
    "platform": "hackernews",
    "points": 134,
    "published_at": "2026-11-20T22:29:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50510005",
    "domain": "股票",
    "title": "Do House members' stock trades beat the market? A test of 8,900 trades",
    "url": "https://arkanumdata.com/research/house-trades",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 129,
    "published_at": "2026-11-15T19:46:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50617640",
    "domain": "股票",
    "title": "Two \"suspicious clusters\" on Polymarket Made Over $340k on Huang Comeback",
    "url": "https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-23-2026/card/two-groups-of-polymarket-accounts-made-over-340-000-on-huang-comeback-Lan2T0TwbJPNsyhmQHGq",
    "source": "qlte",
    "platform": "hackernews",
    "points": 59,
    "published_at": "2026-11-23T19:25:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:50634815",
    "domain": "股票",
    "title": "Nasdaq Resumes Selloff as Nvidia, Anthropic Shares Slump",
    "url": "https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-24-2026",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-11-24T21:14:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50629413",
    "domain": "股票",
    "title": "Anthropic falls below $83 IPO price in Swift reversal after record listing",
    "url": "https://www.reuters.com/business/anthropic-breaks-below-83-ipo-price-debut-rally-unravels-2026-11-24/",
    "source": "thm",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-11-24T15:15:50+00:00",
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
    "id": "hn:50395318",
    "domain": "股票",
    "title": "Anthropic IPO valuation talks drop to $1.3T",
    "url": "https://epyhia.com/anthropic-ipo-valuation-talks-drop-to-1-3-trillion-as-major-investors",
    "source": "arbuge",
    "platform": "hackernews",
    "points": 93,
    "published_at": "2026-11-06T17:21:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50386597",
    "domain": "股票",
    "title": "Major Investors Are Skeptical Anthropic IPO Can Achieve $1.5T Valuation",
    "url": "https://www.wsj.com/finance/major-investors-are-skeptical-anthropic-ipo-can-achieve-1-5-trillion-valuation-ca965d8b’",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-11-06T00:31:11+00:00",
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
    "id": "hn:50588647",
    "domain": "股票",
    "title": "Anthropic's IPO bank closed position meant to stabilize stock",
    "url": "https://www.reuters.com/markets/us/anthropics-ipo-bank-closed-position-meant-stabilize-stock-removing-source-2026-11-20",
    "source": "anon373839",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-11-21T12:43:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:50581060",
    "domain": "股票",
    "title": "Army delays detonating \"catastrophically hazardous\" lead azide amid fear, anger",
    "url": "https://arstechnica.com/science/2026/11/outrage-questions-swirl-as-army-delays-blowing-up-stockpile-of-toxic-lead-azide/",
    "source": "Bender",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-11-20T20:01:48+00:00",
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
    "id": "rss:https://www.netinterest.co/p/supply-and-demand",
    "domain": "股票",
    "title": "Supply and Demand",
    "url": "https://www.netinterest.co/p/supply-and-demand",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T15:38:25+00:00",
    "summary": "Finding Equilibrium Inside the AI Economy"
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
    "id": "hn:50439616",
    "domain": "股票",
    "title": "Anthropic to Seek $1.3T Valuation in IPO",
    "url": "https://www.wsj.com/finance/stocks/anthropic-to-seek-1-3-trillion-valuation-in-ipo-8337b669",
    "source": "sonabinu",
    "platform": "hackernews",
    "points": 60,
    "published_at": "2026-11-10T12:49:32+00:00",
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
    "id": "hn:50542361",
    "domain": "股票",
    "title": "Interesting Learnings Working for a Startup",
    "url": "https://news.ycombinator.com/item?id=50542361",
    "source": "Jessiejia11",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-11-18T05:52:37+00:00",
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
    "id": "hn:50532613",
    "domain": "金融",
    "title": "Brazil's tax authority open-sources its tax calculator on GitHub under MIT",
    "url": "https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/novembro/receita-federal-publica-primeiro-codigo-fonte-aberto-no-github-e-amplia-transparencia-da-reforma-tributaria",
    "source": "dvaplima",
    "platform": "hackernews",
    "points": 790,
    "published_at": "2026-11-17T15:22:57+00:00",
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
    "id": "hn:50568082",
    "domain": "金融",
    "title": "Visa, Mastercard and JPMorgan Customer Data Leaked by Hackers",
    "url": "https://www.wsj.com/finance/banking/visa-mastercard-and-jpmorgan-customer-data-leaked-by-hackers-3b5a0f87",
    "source": "mikhael",
    "platform": "hackernews",
    "points": 198,
    "published_at": "2026-11-19T23:32:11+00:00",
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
    "id": "hn:50602847",
    "domain": "金融",
    "title": "Canada recommits to federal funding for news",
    "url": "https://www.niemanlab.org/2026/11/a-government-that-gets-it-canada-recommits-to-federal-funding-for-news/",
    "source": "DeepLogin",
    "platform": "hackernews",
    "points": 127,
    "published_at": "2026-11-22T19:10:38+00:00",
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
    "id": "hn:50525658",
    "domain": "金融",
    "title": "Pentagon fails ninth straight audit despite progress in organizing finances",
    "url": "https://www.reuters.com/business/aerospace-defense/pentagon-fails-ninth-straight-audit-despite-progress-organizing-finances-2026-11-16/",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 152,
    "published_at": "2026-11-17T00:23:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:50605699",
    "domain": "金融",
    "title": "'It's greed': Zohran Mamdani blasts Amazon over new $5 fee hike in NYC",
    "url": "https://finance.yahoo.com/economy/policy/articles/greed-zohran-mamdani-blasts-amazon-121000124.html",
    "source": "madihaa",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-11-23T00:23:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50532322",
    "domain": "金融",
    "title": "A US Federal Women's Prison Became a \"Rape Club\"",
    "url": "https://www.propublica.org/article/federal-womens-prison-sexual-abuse-reform-dublin-bop",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 87,
    "published_at": "2026-11-17T15:03:25+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.33458",
    "domain": "金融",
    "title": "The Information Content of News Embeddings",
    "url": "https://arxiv.org/abs/2611.33458",
    "source": "Chun He",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T05:00:00+00:00",
    "summary": "arXiv:2611.33458v1 Announce Type: new Abstract: Does the predictive success of news embeddings reflect a better measure of news surprises or other sources of return predictability in text? We decompos"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.33584",
    "domain": "金融",
    "title": "How LLM Agents Reshape Financial Knowledge Graphs: A Survey",
    "url": "https://arxiv.org/abs/2611.33584",
    "source": "Yunbai Zhang, Heze Ma, Nan Jiang, Wenxuan Liu, Ze Chen, Yunyi Gao, Winnie Gao, Han-Tai Shiao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T05:00:00+00:00",
    "summary": "arXiv:2611.33584v1 Announce Type: new Abstract: Financial knowledge graphs (KGs) link information across sources to support risk assessment, investment research, asset recommendations, and forecasting"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.33603",
    "domain": "金融",
    "title": "Retirement Planning with Borrowing Constraints and Income Support",
    "url": "https://arxiv.org/abs/2611.33603",
    "source": "Tae Ung Gang, Seyoung Park, Yong Hyun Shin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T05:00:00+00:00",
    "summary": "arXiv:2611.33603v1 Announce Type: new Abstract: We study how pension income, its pledgeability, and government support that supplements effective consumption shape an irreversible retirement decision."
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.34099",
    "domain": "金融",
    "title": "Will AI Replace Juniors? How Task Complexity Reduces Automation Risk",
    "url": "https://arxiv.org/abs/2611.34099",
    "source": "Vincent Rost, Fabian Stephany",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T05:00:00+00:00",
    "summary": "arXiv:2611.34099v1 Announce Type: new Abstract: How does task complexity shape firms' willingness to substitute entry-level labour with artificial intelligence (AI) tools? We study this question using"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.33593",
    "domain": "金融",
    "title": "Optimization of a Hybrid Solar-Biogas-Battery Energy Storage Microgrid: A Case Study",
    "url": "https://arxiv.org/abs/2611.33593",
    "source": "John Elomunait, Jesse Thornburg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T05:00:00+00:00",
    "summary": "arXiv:2611.33593v1 Announce Type: cross Abstract: Low-income regions like eastern Uganda often lack reliable grid power. This paper presents the techno-economic optimization of the Soroti Integrated R"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.34068",
    "domain": "金融",
    "title": "Budget, Readout or Reasoning? Where Small Reasoning Models Lose Value in Auction Bidding",
    "url": "https://arxiv.org/abs/2611.34068",
    "source": "Mahbod Khaleti, Seyed Reza Tavakoli, Baran Hoseini, Alireza Noori, Amir Amini, Koorosh Aslansefat, Marjan Alirezaie, Ali Habibnia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T05:00:00+00:00",
    "summary": "arXiv:2611.34068v1 Announce Type: cross Abstract: Ad platforms and marketplaces show bidders a bid landscape, the estimated chance of winning at each candidate bid, and increasingly let agents built o"
  },
  {
    "id": "rss:https://arxiv.org/abs/2506.07928",
    "domain": "金融",
    "title": "Predicting Realized Variance Out of Sample: Can Anything Beat The Benchmark?",
    "url": "https://arxiv.org/abs/2506.07928",
    "source": "Austin Pollok",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T05:00:00+00:00",
    "summary": "arXiv:2506.07928v2 Announce Type: replace Abstract: The discrepancy between realized volatility and the market's view of volatility has been known to predict individual equity options at the monthly h"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.05659",
    "domain": "金融",
    "title": "AI and the Division of Labor in Public Sector Jobs and Teams",
    "url": "https://arxiv.org/abs/2512.05659",
    "source": "Andrew Ledingham, Michael Hollins, Matthew Lyon, David Gillespie, Umar Yunis-Guerra, Jamie Siviter, David Duncan, Oliver P. Hauser",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T05:00:00+00:00",
    "summary": "arXiv:2512.05659v2 Announce Type: replace Abstract: How artificial intelligence (AI) affects an organization depends not only on which jobs are exposed, but on how more (versus less) exposed tasks are"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.20145",
    "domain": "金融",
    "title": "Volatility Forecasts with Market Trends",
    "url": "https://arxiv.org/abs/2606.20145",
    "source": "Sara A. Safari, Christoph Schmidhuber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T05:00:00+00:00",
    "summary": "arXiv:2606.20145v2 Announce Type: replace Abstract: We show how volatility forecasts for financial markets can be refined by accounting for the current trends in these markets. Empirically, volatiliti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09951",
    "domain": "金融",
    "title": "Macroeconomic Risks from Maritime Trade Disruptions",
    "url": "https://arxiv.org/abs/2607.09951",
    "source": "Vipin P. Veetil, Fathimath S. Vemmarath",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T05:00:00+00:00",
    "summary": "arXiv:2607.09951v3 Announce Type: replace Abstract: This paper develops a model of maritime chokepoint closures in which interrupting a shipping passage produces losses that are not measured, or even "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04987",
    "domain": "金融",
    "title": "Portfolio Allocation under Heterogeneous Scales and Multifractality",
    "url": "https://arxiv.org/abs/2608.04987",
    "source": "Shinji Kakinaka, Ken Umeno",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T05:00:00+00:00",
    "summary": "arXiv:2608.04987v2 Announce Type: replace Abstract: Cross-correlations between financial signals are neither scale-free nor amplitude-independent: they vary with the time scale over which they are mea"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.04070",
    "domain": "金融",
    "title": "Evaluating LLM Research Agents as Tests of Return Predictability",
    "url": "https://arxiv.org/abs/2611.04070",
    "source": "Chang Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T05:00:00+00:00",
    "summary": "arXiv:2611.04070v3 Announce Type: replace Abstract: How often do research agents built on large language models report that they can forecast returns when the data contain no signal? We score the conc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.20589",
    "domain": "金融",
    "title": "Beyond Marginal Risk: ESG and Multidimensional Fragility in Equity Markets",
    "url": "https://arxiv.org/abs/2611.20589",
    "source": "Minxuan Hu, Jiayu Yi, Ziheng Chen, Wenxi Sun, Qishi Zhan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T05:00:00+00:00",
    "summary": "arXiv:2611.20589v2 Announce Type: replace Abstract: Do ESG characteristics provide financial resilience beyond conventional risk, and is that inference stable to the financial state and ESG score bein"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.26652",
    "domain": "金融",
    "title": "Distributional Deep Hedging",
    "url": "https://arxiv.org/abs/2611.26652",
    "source": "El-Amine Cherrat, Skander Kazdaghli, Iordanis Kerenidis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T05:00:00+00:00",
    "summary": "arXiv:2611.26652v2 Announce Type: replace Abstract: Deep hedging learns a hedging strategy by optimising a risk preference over a neural-network policy. The preference is fixed before training, so eac"
  },
  {
    "id": "rss:https://arxiv.org/abs/2611.30843",
    "domain": "金融",
    "title": "Cleaning correlation matrices with external information: the Maximum Variance estimator",
    "url": "https://arxiv.org/abs/2611.30843",
    "source": "S\\'ebastien Valeyre",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T05:00:00+00:00",
    "summary": "arXiv:2611.30843v3 Announce Type: replace Abstract: Rotationally invariant estimators clean the eigenvalues of an empirical correlation matrix but keep its noisy eigenvectors. We study an estimator th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.24514",
    "domain": "金融",
    "title": "Incremental SVD for Large-Scale Dynamic Matrices: Accuracy, Subspace Stability, Refresh Strategies, and Financial Factor-Based Risk Models",
    "url": "https://arxiv.org/abs/2605.24514",
    "source": "Stilyan Staykov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T05:00:00+00:00",
    "summary": "arXiv:2605.24514v2 Announce Type: replace-cross Abstract: Return panels, covariances, and large feature matrices evolve one observation or entry at a time, yet downstream models require an up-to-date "
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.35744",
    "domain": "金融",
    "title": "FinAutoRubric: Expert-Guided Automatic Rubric Generation for Evaluating Financial Research Agents",
    "url": "https://arxiv.org/abs/2609.35744",
    "source": "Hoyoung Lee, Suyeol Yun, Jack Haverty, Yunju Cho, Meesong Kim, Daekyung Park, Sumin Kim, Jihoon Kwon, Jasmine Jia Geng, Andrew Chin, Yin Luo, Edward Tong, Yu Yu, Zach Golkhou, Minkyu Kim, Igor Halperin, Young Cha, Alejandro Lopez-Lira, Chanyeol Choi, Yongjae Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T05:00:00+00:00",
    "summary": "arXiv:2609.35744v3 Announce Type: replace-cross Abstract: Evaluating finance research agents requires rubrics that reflect expert standards and fix the values correct as of an information cutoff. Expe"
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
    "id": "hn:50594937",
    "domain": "金融",
    "title": "Tesla launches FSD v15, targets its biggest weaknesses, from signs to potholes",
    "url": "https://electrek.co/2026/11/21/tesla-fsd-v15-rollout-25x-safety-reality-view/",
    "source": "m348e912",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-11-22T00:14:05+00:00",
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
    "id": "hn:50543108",
    "domain": "金融",
    "title": "Firefox opens hotline for users sick of Microsoft shoving Edge down their throat",
    "url": "https://www.neowin.net/news/firefox-opens-hotline-for-windows-users-fed-up-with-microsoft-shoving-edge-down-their-throat/",
    "source": "bundie",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-11-18T07:51:58+00:00",
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
    "id": "hn:50384382",
    "domain": "金融",
    "title": "Chip stocks get slaughtered as Wall Street in worst post-midterm day since 1896",
    "url": "https://finance.yahoo.com/markets/article/chip-stocks-get-slaughtered-as-wall-street-heads-for-its-worst-post-midterm-day-since-1896-163413900.html",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-11-05T20:58:36+00:00",
    "summary": ""
  }
]
```
