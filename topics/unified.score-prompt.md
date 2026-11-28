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

- 今日日期：`2026-11-28`
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
  "date": "2026-11-28",
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
    "id": "bvid:BV1BVEs6LENZ",
    "domain": "AI",
    "title": "【2026最新Codex】Codex保姆级完整教程-Codex新手保姆级教程-最强AI助手！从入门到进阶，22分钟速通Codex！【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av116707129561197",
    "source": "编程大佬陈悠秀",
    "platform": "bilibili",
    "points": 3702052,
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
    "points": 2302421,
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
    "points": 2170191,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1523474,
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
    "points": 1502939,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1PwBuBtEZo",
    "domain": "AI",
    "title": "Trae 保姆级教程｜AI 编程工具完整入门，实战项目手把手教学",
    "url": "http://www.bilibili.com/video/av115768712893172",
    "source": "韩顺平",
    "platform": "bilibili",
    "points": 1101240,
    "published_at": "2025-12-23T11:55:45+00:00",
    "summary": "如果这个视频对你有帮助，记得【一键三连】，支持一下老韩\n【视频配套工具包+学习资料，”评论区置顶” 免费领取】"
  },
  {
    "id": "bvid:BV1mtDEYPEDg",
    "domain": "AI",
    "title": "吃透AI Agent项目：手撸 Agent 框架 +Harness+ Agent开发实战+ Agent记忆系统 + MCP/A2A 协议实战！",
    "url": "http://www.bilibili.com/video/av113422133888695",
    "source": "卢菁博士",
    "platform": "bilibili",
    "points": 924400,
    "published_at": "2024-11-04T01:45:43+00:00",
    "summary": "【北大博士后亲授】AI大模型实战集训营🔥企业级大模型实战： ai agent原理 aiagent智能体搭建！\n AI智能体搭建教程：ai agent智能体搭建 langmanus MCP A2A源码级实战！"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 918298,
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
    "points": 766407,
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
    "points": 675908,
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
    "points": 598038,
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
    "points": 494117,
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
    "points": 469568,
    "published_at": "2026-11-08T09:14:07+00:00",
    "summary": "最近Claude桌面端（Claude Desktop） 有了一大波功能更新。随着一步步的迭代，它已经把 Claude Code 的编程、Claude Design 的设计，以及 Claude Cowork 的办公等核心能力，全部收入了同一个桌面客户端，特别是Claude Code已经从原本黑乎乎的命令行工具，进化成了桌面客户端的完全体形态。再搭配上超强的Opus5.5 模型，已经能称得上是地表顶级"
  },
  {
    "id": "bvid:BV1rBRQBSEwB",
    "domain": "AI",
    "title": "Claude Code+DeepSeek V4 Pro安装教程｜3步从零装好开始用 | Mac Windows",
    "url": "http://www.bilibili.com/video/av116543199385810",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 460608,
    "published_at": "2026-05-09T10:10:00+00:00",
    "summary": "上期vibe coding零基础教程10万多人看了，私信和评论里问最多的居然不是怎么写需求。\n 而是Claude Code怎么装？DeepSeek怎么接进去？🫣\n\n所以这期作为补丁教程，专门帮大家搞定这3件事：\n 1️⃣ 安装Claude Code\n 2️⃣ 把DeepSeek V4 Pro百万上下文满血版接入Claude Code\n 3️⃣ 在VS Code里正式用起来\n\nMac和Windows"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 439660,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 429340,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1ZRbe6eENh",
    "domain": "AI",
    "title": "DeepSeek Harness安装和使用教程【最新完整版】零基础小白速通deepseek harness入门教程怎么下载插件如何安装如何使用全搞定！",
    "url": "http://www.bilibili.com/video/av117110286062691",
    "source": "鹏哥C语言",
    "platform": "bilibili",
    "points": 385584,
    "published_at": "2026-08-17T10:10:51+00:00",
    "summary": "欢迎大家来到鹏哥课堂！这份DeepSeek Harness教程专为零基础小白打造，全程手把手演示安装、启动Web界面、模型接入、基础任务实操。 很多小白卡在环境配置、命令报错、参数设置，本教程能让你避开各种坑，跟着操作就能成功运行。 搞懂 Agent = 模型 + Harness，让 AI 读写文件、执行命令、自主完成项目任务。本教程适合程序员、AI 爱好者及想上手本地智能体的同学等。希望大家把视"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 373025,
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
    "points": 359272,
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
    "points": 335276,
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
    "points": 310407,
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
    "points": 307575,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1qJs16WEJj",
    "domain": "AI",
    "title": "今天体验的人生副本是:沉迷vibe coding走火入魔的AI嘉豪",
    "url": "http://www.bilibili.com/video/av117635899524333",
    "source": "vibe睦头人",
    "platform": "bilibili",
    "points": 294717,
    "published_at": "2026-11-18T06:01:48+00:00",
    "summary": "ai生成，仅供娱乐，如有雷同，纯属巧合（（"
  },
  {
    "id": "bvid:BV1RdLm6PEFF",
    "domain": "AI",
    "title": "ClaudeCode桌面版 = 中文汉化 + 免登录 + 接入DeekSeek + 安装自己的Skill",
    "url": "http://www.bilibili.com/video/av116606717919919",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 294274,
    "published_at": "2026-05-20T11:45:46+00:00",
    "summary": "全B站最详细的 ClaudeCode 桌面版教程，从安装到免登录，中文汉化，接入DeepSeek，安装使用自己的Skill，ClaudeCode真正的AI编程工具，恐怖如斯！\nAgent Skills课程在这里：https://www.bilibili.com/video/BV1ugdgBQED4/?spm_id_from=333.1387.homepage.video_card.click&am"
  },
  {
    "id": "bvid:BV1Cx6oBAETu",
    "domain": "AI",
    "title": "巅峰对决，Cursor TRAE 对比评测",
    "url": "http://www.bilibili.com/video/av115876875469556",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 260333,
    "published_at": "2026-01-12T03:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 242971,
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
    "points": 218752,
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
    "points": 216389,
    "published_at": "2026-04-13T09:00:00+00:00",
    "summary": "opencodeopencode使用全攻略opencode教程opencode和claudecodeopencode使用技巧opencode实战opencode coworkopencode安装opencode开发opencode使用教程opencode教程opencode安装教程opencode使用全攻略opencode和claudecodeopencode skillsopencode插件op"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 166876,
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
    "points": 162412,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 160842,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1PgCmY9EKu",
    "domain": "AI",
    "title": "Cursor教程：实现自动化写文章，让AI 7*24小时为你打工｜ChatGPT｜AI进化论-花生",
    "url": "http://www.bilibili.com/video/av113328902905646",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 135598,
    "published_at": "2024-10-18T14:35:55+00:00",
    "summary": "👏 欢迎加入我的知识星球「AI编程：从入门到精通」：https://t.zsxq.com/BFTPI\n🤖 OpenAI API充值入口：https://platform.openai.com/settings/organization/billing/overview\n\n这期视频主要是像你介绍如何使用Cursor写自动化脚本，实现让ChatGPT为你自动化写作的目的。以小红书读书博主为例，演示了使"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 124831,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1SCpx6EEVj",
    "domain": "AI",
    "title": "【40集全】AI大模型应用实战全家桶零基础教程，包括LLM、RAG、Agent、MCP、工作流、工具调用等，支持FastAPI和Springboot双版本",
    "url": "http://www.bilibili.com/video/av117408501139977",
    "source": "武哥聊编程",
    "platform": "bilibili",
    "points": 109736,
    "published_at": "2026-10-09T02:06:20+00:00",
    "summary": "Springboot版：https://aigcbaba.com/course/123\nFastAPI版：https://aigcbaba.com/course/124"
  },
  {
    "id": "bvid:BV1677s6UErR",
    "domain": "AI",
    "title": "分享一下我对于 Codex 和 Claude 的一些看法",
    "url": "http://www.bilibili.com/video/av116822120602930",
    "source": "oil欧呦",
    "platform": "bilibili",
    "points": 108671,
    "published_at": "2026-06-27T12:42:40+00:00",
    "summary": "深度用过 Codex 和 Claude 之后，分享我对桌面端产品设计、模型体验和日常工作流的真实感受。"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 105322,
    "published_at": "2026-04-27T04:45:20+00:00",
    "summary": "很多人问我上期爆了的那条视频里，那个 PPT 是怎么做的。\n其实我是用 Anthropic 最近出的 Claude Design 做的，这个功能一发出来就在全网传疯了，一条推文就冲上了 6000 多万曝光。\n本期视频我会带你手把手从 0 到 1 把这个Skill 装好，然后一起跑一个成品效果出来。"
  },
  {
    "id": "bvid:BV1PUWX69EDC",
    "domain": "AI",
    "title": "DeepSeek Harness 省 token 终极指南！8 个省钱技巧",
    "url": "http://www.bilibili.com/video/av117602210876639",
    "source": "林粒粒呀",
    "platform": "bilibili",
    "points": 99688,
    "published_at": "2026-11-12T11:05:00+00:00",
    "summary": "8 个 DeepSeek Harness 省钱\n省 Token 实用技巧！"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 94396,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1LjC7BmE8H",
    "domain": "AI",
    "title": "硅谷爆火AI神器Cursor教程！从入门到实战，轻松做图表、写文档、搞开发、自动化全能办公！",
    "url": "http://www.bilibili.com/video/av115536717484104",
    "source": "韩顺平",
    "platform": "bilibili",
    "points": 90016,
    "published_at": "2025-11-12T12:31:09+00:00",
    "summary": "《Cursor快速入门到实战》带你全面掌握Cursor！从安装配置到Chat对话、规则、提示词模板，再到数据可视化、文档生成、游戏开发、智能助手、Figma联动实战，全流程提升AI编程与办公效率，轻松打造高效智能开发环境。"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 82587,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 71528,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1RtGU6hEDd",
    "domain": "AI",
    "title": "DeepSeek-Reasonix 【保姆级教程】：专为 DeepSeek 打造的 AI 编程 Agent客户端，长会话成本到底能省多少？",
    "url": "http://www.bilibili.com/video/av116647486556383",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 60070,
    "published_at": "2026-05-27T16:33:52+00:00",
    "summary": "本期体验 DeepSeek-Reasonix 这个开源项目，主要看客户端界面、模型模式、会话导入、MCP 配置、记忆与缓存等功能。内容基于个人使用记录，不做夸张结论，适合对 DeepSeek 生态和 AI 编程工具感兴趣的朋友参考。"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 50867,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1TyfuBnEEY",
    "domain": "AI",
    "title": "ClaudeCode接入第三方中转API使用官方模型配置教程；省下一半费用还能用官方模型",
    "url": "http://www.bilibili.com/video/av116102092822203",
    "source": "掌舵者AI实验室",
    "platform": "bilibili",
    "points": 50388,
    "published_at": "2026-02-20T08:52:21+00:00",
    "summary": "很多小伙伴问怎么用中转API调用Claude官方模型， 本期视频手把手教你配置。"
  },
  {
    "id": "bvid:BV1wpxq6VEXx",
    "domain": "AI",
    "title": "【AI时代的STM32教程】AI Agent 初体验",
    "url": "http://www.bilibili.com/video/av117529699682124",
    "source": "keysking",
    "platform": "bilibili",
    "points": 50120,
    "published_at": "2026-10-30T11:52:06+00:00",
    "summary": "一句话，让 AI 帮我们完成第一个 STM32C5 程序！🚀\n本期我们一起认识 AI Agent，学习如何描述开发需求，并借助开源的 STM32C5DevSkills，让 AI 完成工程创建、芯片配置、代码编写和编译烧录，让律动小板上的小灯闪烁起来！\n也特别感谢 @意法半导体中国   对本系列教程的支持～下期我们再亲手走一遍开发流程，把 Agent 替我们完成的工作，一步步搞明白！"
  },
  {
    "id": "bvid:BV1YS1czoEJ4",
    "domain": "AI",
    "title": "50 分钟速通 Codex 保姆级教程（含 DeepSeek 接入，无需 ChatGPT 订阅）【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av117671517489403",
    "source": "林粒粒呀",
    "platform": "bilibili",
    "points": 46768,
    "published_at": "2026-11-24T13:01:46+00:00",
    "summary": "50 分钟速通 Codex 保姆级教程\n无需 ChatGPT 订阅，国内直连 DeepSeek"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 44248,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV1hEVY6jEGT",
    "domain": "AI",
    "title": "最新【Claude pro Max】保姆级充值教程 Claude code国内购买教程 注册+订阅一个视频教会你",
    "url": "http://www.bilibili.com/video/av116657754277772",
    "source": "codex充值",
    "platform": "bilibili",
    "points": 43340,
    "published_at": "2026-05-29T12:07:14+00:00",
    "summary": "aipayok.com"
  },
  {
    "id": "bvid:BV1NddKBvEsY",
    "domain": "AI",
    "title": "claude code 桌面端安装并且配置第三方api使用教程，想体验的尽早吧，因为这公司可能不知道哪天抽风就会禁用了！#claude #ai #人工智能",
    "url": "http://www.bilibili.com/video/av116535968466799",
    "source": "菜鸡的老黎",
    "platform": "bilibili",
    "points": 43157,
    "published_at": "2026-05-07T23:56:28+00:00",
    "summary": "claude code 桌面端安装并且配置第三方api使用教程，想体验的尽早吧，因为这公司可能不知道哪天抽风就会禁用了！#claude #ai #人工智能 #agent"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 41664,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "hn:50611576",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Reinstates Jensen Huang as CEO",
    "url": "https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html",
    "source": "jaz",
    "platform": "hackernews",
    "points": 2860,
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
    "points": 356,
    "published_at": "2026-11-25T04:31:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50626861",
    "domain": "AI 算力 / 半导体",
    "title": "Who in Washington owns and trades Nvidia stock",
    "url": "https://www.kadoa.com/congress/insights/trump-nvidia",
    "source": "hubraumhugo",
    "platform": "hackernews",
    "points": 292,
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
    "id": "hn:50630245",
    "domain": "AI 算力 / 半导体",
    "title": "Ex-Nvidia partner Megaspeed hit with U.S. Commerce Department export ban",
    "url": "https://www.upi.com/Top_News/US/2026/11/24/NVIDIA-partner-Megaspeed/1701795520063/",
    "source": "nephihaha",
    "platform": "hackernews",
    "points": 130,
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
    "id": "hn:50659532",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia was right to bring back Jensen Huang, writes Sarah Guo",
    "url": "https://www.economist.com/by-invitation/2026/11/25/nvidia-was-right-to-bring-back-jensen-huang-writes-sarah-guo",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-11-26T20:39:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50668828",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO's comeback fuels debate on misogyny or impunity for rich and powerful",
    "url": "https://www.pbs.org/newshour/nation/nvidia-ceos-comeback-fuels-debate-over-misogyny-and-impunity-for-the-rich-and-powerful",
    "source": "Betelbuddy",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-11-27T16:43:06+00:00",
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
    "id": "hn:50629620",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia board's Huang reversal raises doubts about independence, critics say",
    "url": "https://www.reuters.com/legal/transactional/nvidia-boards-huang-reversal-raises-doubts-about-independence-critics-say-2026-11-24/",
    "source": "onemoresoop",
    "platform": "hackernews",
    "points": 44,
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
    "id": "hn:50648903",
    "domain": "AI 算力 / 半导体",
    "title": "S&P warns Nvidia's board may be compromised",
    "url": "https://www.reuters.com/technology/us-finds-no-evidence-china-directed-executive-spy-nvidia-ceo-wsj-reports-2026-11-25/",
    "source": "narmiouh",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-11-25T23:03:16+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/gta-grand-three-assumptions/",
    "domain": "AI 算力 / 半导体",
    "title": "GTA: Grand Three Assumptions",
    "url": "https://www.eetimes.com/gta-grand-three-assumptions/",
    "source": "Moshe Zalcberg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-28T02:00:00+00:00",
    "summary": "GTA 6 broke sales records, but consoles running it rest on assumptions that failed: cheaper hardware, commodity memory, frozen platforms. The post GTA: Grand Three Assumptions appeared first on EE Tim"
  },
  {
    "id": "rss:https://www.eetimes.com/penguin-revives-retired-ddr4-for-ai-servers/",
    "domain": "AI 算力 / 半导体",
    "title": "Penguin Revives Retired DDR4 for AI Servers",
    "url": "https://www.eetimes.com/penguin-revives-retired-ddr4-for-ai-servers/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T19:17:00+00:00",
    "summary": "Hyperscalers are already reclaiming older DRAM, but enterprises have been slower to reuse DDR4 to meet their memory expansion demands. The post Penguin Revives Retired DDR4 for AI Servers appeared fir"
  },
  {
    "id": "rss:https://www.eetimes.com/beyond-lithography-the-battle-for-semiconductor-manufacturing-yield/",
    "domain": "AI 算力 / 半导体",
    "title": "Beyond Lithography: The Battle for Semiconductor Manufacturing Yield",
    "url": "https://www.eetimes.com/beyond-lithography-the-battle-for-semiconductor-manufacturing-yield/",
    "source": "Ron Honig",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T14:22:45+00:00",
    "summary": "The proposed MATCH Act exposes a strategic vulnerability extending beyond ASML to the technologies that determine manufacturing productivity and yield. The post Beyond Lithography: The Battle for Semi"
  },
  {
    "id": "rss:https://www.eetimes.com/nuvolta-technical-sharing-pcb-grounding-design-and-return-path/",
    "domain": "AI 算力 / 半导体",
    "title": "NuVolta Technical Sharing: PCB Grounding Design and Return Path",
    "url": "https://www.eetimes.com/nuvolta-technical-sharing-pcb-grounding-design-and-return-path/",
    "source": "Luke, Engineer, NuVolta Technologies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T14:00:00+00:00",
    "summary": "Many PCB design guidelines reduce grounding to a few rules: These rules are not wrong, but they are incomplete. They do not answer a fundamental question: where does the current return? If a ground pl"
  },
  {
    "id": "rss:https://www.eetimes.com/huawei-next-big-ai-move-hbm-workaround/",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei’s Next Big AI Move: HBM Workaround",
    "url": "https://www.eetimes.com/huawei-next-big-ai-move-hbm-workaround/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T08:56:46+00:00",
    "summary": "The Shenzhen-based tech firm will provide details about its custom HBM design at ISSCC 2027 in San Francisco early next year. The post Huawei’s Next Big AI Move: HBM Workaround appeared first on EE Ti"
  },
  {
    "id": "rss:https://www.eetimes.com/siemens-adds-soc-verification-and-software-debug-with-two-planned-deals/",
    "domain": "AI 算力 / 半导体",
    "title": "Siemens Adds SoC Verification and Software Debug with Two Planned Deals",
    "url": "https://www.eetimes.com/siemens-adds-soc-verification-and-software-debug-with-two-planned-deals/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T18:00:00+00:00",
    "summary": "The planned Breker and Lauterbach acquisitions would expand Siemens’s development tools, but an analyst expects integration benefits to take time. The post Siemens Adds SoC Verification and Software D"
  },
  {
    "id": "rss:https://www.eetimes.com/bridging-the-research-to-manufacturing-gap-in-canadas-semiconductor-industry/",
    "domain": "AI 算力 / 半导体",
    "title": "Bridging the Research-to-Manufacturing Gap in Canada’s Semiconductor Industry",
    "url": "https://www.eetimes.com/bridging-the-research-to-manufacturing-gap-in-canadas-semiconductor-industry/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T14:00:00+00:00",
    "summary": "Quantum computing, sovereign AI, ocean electronics, and advanced materials: six stories on how Canada is connecting its technology strengths—and confronting the challenge of scale. The post Bridging t"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-nifty-usd35-dual-hard-drive-dock-can-support-up-to-64tb-of-storage-for-your-pc-clone-duplicate-and-connect-2-5-inch-and-3-5-inch-ssds-and-hdds-with-ease",
    "domain": "AI 算力 / 半导体",
    "title": "This nifty $35 dual hard drive dock can support up to 64TB of storage for your PC",
    "url": "https://www.tomshardware.com/pc-components/this-nifty-usd35-dual-hard-drive-dock-can-support-up-to-64tb-of-storage-for-your-pc-clone-duplicate-and-connect-2-5-inch-and-3-5-inch-ssds-and-hdds-with-ease",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-28T11:16:34+00:00",
    "summary": "Pick up this dual-bay docking station and hook up two 3.5-inch or 2.5-inch drives simultaneously. It even has a built-in offline duplicator and cloning function."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/hair-dye-that-turns-your-head-into-a-brain-computer-interface-ehair-coats-strands-in-conductive-polymers-to-amplify-eeg-signals-without-surgery",
    "domain": "AI 算力 / 半导体",
    "title": "Hair dye that turns your head into a brain-computer interface",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/hair-dye-that-turns-your-head-into-a-brain-computer-interface-ehair-coats-strands-in-conductive-polymers-to-amplify-eeg-signals-without-surgery",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-28T11:00:00+00:00",
    "summary": "eHAIR is claimed to transform hair 'from a barrier into a functional bioelectronic interface.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/thermaltakes-budget-rtx-5060-ti-gaming-desktops-are-as-little-as-usd1-299-choose-between-ddr4-and-ddr5-configurations-with-up-to-usd100-off",
    "domain": "AI 算力 / 半导体",
    "title": "Thermaltake’s budget RTX 5060 Ti gaming desktops are as little as $1,299",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/thermaltakes-budget-rtx-5060-ti-gaming-desktops-are-as-little-as-usd1-299-choose-between-ddr4-and-ddr5-configurations-with-up-to-usd100-off",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-28T10:45:00+00:00",
    "summary": "Both prebuilt gaming PCs come with Nvidia's RTX 5060 Ti 8GB graphics, 1TB of storage, RGB cooling, and an Intel AI software bundle, while also including a holiday bundle with two PC games."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/corsairs-xeneon-edge-pc-touchscreen-is-usd50-off-in-all-colors-tiny-14-5-inch-under-monitor-display-is-just-usd200",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair's Xeneon Edge PC touchscreen is $50 off in all colors",
    "url": "https://www.tomshardware.com/pc-components/corsairs-xeneon-edge-pc-touchscreen-is-usd50-off-in-all-colors-tiny-14-5-inch-under-monitor-display-is-just-usd200",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-28T10:30:00+00:00",
    "summary": "Corsair's 14.5-inch touchscreen is $50 off in all five colors for Black Friday."
  },
  {
    "id": "rss:https://www.tomshardware.com/speakers/onkyos-incredible-creator-series-desktop-pc-speakers-are-almost-50-percent-off-great-sound-and-plenty-of-connections",
    "domain": "AI 算力 / 半导体",
    "title": "Onkyo's incredible Creator Series desktop PC speakers are almost 50% off — great sound and plenty of connections",
    "url": "https://www.tomshardware.com/speakers/onkyos-incredible-creator-series-desktop-pc-speakers-are-almost-50-percent-off-great-sound-and-plenty-of-connections",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-28T10:00:00+00:00",
    "summary": "Both Onkyo's Creator GX-10DB and Creator GX-30ARC desktop speakers are on a pretty decent sale at Amazon for Black Friday."
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/best-black-friday-3d-printer-deals-day-two",
    "domain": "AI 算力 / 半导体",
    "title": "Best Black Friday 2026 3D Printer deals live",
    "url": "https://www.tomshardware.com/live/news/best-black-friday-3d-printer-deals-day-two",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-28T08:22:48+00:00",
    "summary": "The best Black Friday 3D printer deals that you can still buy this weekend."
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/best-black-friday-gaming-laptop-deals-day-two",
    "domain": "AI 算力 / 半导体",
    "title": "Best Black Friday Gaming laptop deals live",
    "url": "https://www.tomshardware.com/live/news/best-black-friday-gaming-laptop-deals-day-two",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-28T08:01:57+00:00",
    "summary": "The best Black Friday gaming laptops still live this weekend."
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/black-friday-gaming-pc-deals-2026-day-two",
    "domain": "AI 算力 / 半导体",
    "title": "Best Black Friday Gaming PC Deals live",
    "url": "https://www.tomshardware.com/live/news/black-friday-gaming-pc-deals-2026-day-two",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-28T07:42:15+00:00",
    "summary": "All the best Black Friday gaming PC deals you can still buy this weekend."
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/black-friday-2026-day-four",
    "domain": "AI 算力 / 半导体",
    "title": "Best Black Friday 2026 tech deals live",
    "url": "https://www.tomshardware.com/live/news/black-friday-2026-day-four",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-28T07:20:57+00:00",
    "summary": "All the best Black Friday deals for tech and PC hardware you can still buy this weekend."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/this-lenovo-loq-notebook-with-arc-b390-graphics-is-just-usd799-this-black-friday-get-a-gaming-ready-panther-lake-laptop-for-a-super-low-price",
    "domain": "AI 算力 / 半导体",
    "title": "This Lenovo LOQ notebook with Arc B390 graphics is just $799 this Black Friday",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/this-lenovo-loq-notebook-with-arc-b390-graphics-is-just-usd799-this-black-friday-get-a-gaming-ready-panther-lake-laptop-for-a-super-low-price",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T23:33:28+00:00",
    "summary": "Good cheap gaming notebooks are hard to find this Black Friday, but Lenovo's LOQ laptop with Arc B390 graphics gets you there for just $799."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-a-perfect-alienware-4k-oled-32-display-with-rgb-subpixels-for-usd150-off-165-hz-refresh-rate-1000-nits-hdr-and-dolby-vision-support-with-the-aw3226q",
    "domain": "AI 算力 / 半导体",
    "title": "Get a perfect Alienware 4K OLED 32\" display with RGB subpixels for $150 off",
    "url": "https://www.tomshardware.com/pc-components/get-a-perfect-alienware-4k-oled-32-display-with-rgb-subpixels-for-usd150-off-165-hz-refresh-rate-1000-nits-hdr-and-dolby-vision-support-with-the-aw3226q",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T23:10:19+00:00",
    "summary": "Get a perfect Alienware AW3226Q 4K OLED 32\" display with RGB subpixels for $549.99, or $150 off — 165 Hz refresh rate, 1000-nits HDR, and Dolby Vision support"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/sandisks-lightning-fast-optimus-gx-pro-8100-2tb-nvme-ssd-is-21-percent-off-and-usd0-18-cents-per-gb-usd349-for-a-pcie-5-0-m-2-ssd-is-about-as-good-as-it-gets-for-black-friday",
    "domain": "AI 算力 / 半导体",
    "title": "SanDisk’s lightning-fast Optimus GX Pro 8100 2TB NVMe SSD is 21% off and $0.18 cents per GB",
    "url": "https://www.tomshardware.com/pc-components/sandisks-lightning-fast-optimus-gx-pro-8100-2tb-nvme-ssd-is-21-percent-off-and-usd0-18-cents-per-gb-usd349-for-a-pcie-5-0-m-2-ssd-is-about-as-good-as-it-gets-for-black-friday",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T22:19:56+00:00",
    "summary": "2TB SanDisk Optimus GX Pro 8100 PCIe 5.0 SSD is down to an all-time low of $349, making it one of the cheapest 2TB Gen5 drives around."
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/black-friday-2026-monitor-deals-oled-4k-gaming",
    "domain": "AI 算力 / 半导体",
    "title": "Black Friday 2026 gaming monitor deals live",
    "url": "https://www.tomshardware.com/live/news/black-friday-2026-monitor-deals-oled-4k-gaming",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T21:49:59+00:00",
    "summary": "The best Black Friday monitor sales, live round-the-clock coverage of all the best deals."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-ultimate-ryzen-9-9950x3d2-cpu-is-down-to-its-lowest-price-with-usd140-savings-single-cache-ryzen-9-9950x3d-is-also-on-a-deep-usd115-discount",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's ultimate Ryzen 9 9950X3D2 CPU is down to its lowest price with $140 savings",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-ultimate-ryzen-9-9950x3d2-cpu-is-down-to-its-lowest-price-with-usd140-savings-single-cache-ryzen-9-9950x3d-is-also-on-a-deep-usd115-discount",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T21:29:33+00:00",
    "summary": "Grab AMD's most powerful CPUs, the Ryzen 9 9950X3D2 or 9950X3D, at all-time-low prices during Black Friday."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/samsungs-49-inch-oled-gaming-monitor-returns-to-its-lowest-price-ever-at-amazon-take-your-gpu-on-an-ultrawide-odyssey-for-usd854",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung's 49-inch OLED gaming monitor drops to a new low price of $854",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/samsungs-49-inch-oled-gaming-monitor-returns-to-its-lowest-price-ever-at-amazon-take-your-gpu-on-an-ultrawide-odyssey-for-usd854",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T21:06:27+00:00",
    "summary": "Amazon is offering the Samsung Odyssey G9 G93SC at a price of $854, a new all-time low. The gaming monitor often sells for above $1,20"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/protect-your-pc-console-or-tv-with-a-cyberpower-st900u-ups-for-just-usd99-95-or-17-percent-off-a-complement-of-12-outlets-available-with-surge-protection",
    "domain": "AI 算力 / 半导体",
    "title": "Protect your PC, console, or TV with a CyberPower ST900U UPS for just $99.95, or 17% off",
    "url": "https://www.tomshardware.com/pc-components/protect-your-pc-console-or-tv-with-a-cyberpower-st900u-ups-for-just-usd99-95-or-17-percent-off-a-complement-of-12-outlets-available-with-surge-protection",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T20:30:00+00:00",
    "summary": "Protect your PC, console, or TV with a CyberPower ST900U UPS for just $99.95, or 20% off — a complement of 12 outlets available with surge protection"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-a-sony-wh-1000-mx5-headset-with-anc-for-only-usd169-99-aural-bliss-for-your-games-and-movies",
    "domain": "AI 算力 / 半导体",
    "title": "Get a Sony WH-1000 XM5 headset with ANC for only $169.99 — aural bliss for your games and movies",
    "url": "https://www.tomshardware.com/pc-components/get-a-sony-wh-1000-mx5-headset-with-anc-for-only-usd169-99-aural-bliss-for-your-games-and-movies",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T19:49:01+00:00",
    "summary": "Get a Sony WH-1000 XM5 headset with ANC for only $169.99 — aural bliss for your games and movies"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/get-the-cheapest-rtx-5070-around-this-black-friday-with-gigabytes-usd839-gaming-oc-card-midrange-blackwell-continues-to-shine-with-dlss-4-5-and-dlss-5",
    "domain": "AI 算力 / 半导体",
    "title": "Get the cheapest RTX 5070 around this Black Friday with Gigabyte's $839 Gaming OC card",
    "url": "https://www.tomshardware.com/pc-components/gpus/get-the-cheapest-rtx-5070-around-this-black-friday-with-gigabytes-usd839-gaming-oc-card-midrange-blackwell-continues-to-shine-with-dlss-4-5-and-dlss-5",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T19:38:08+00:00",
    "summary": "Looking for a midrange RTX 50-series upgrade this Black Friday? The Gigabyte Gaming RTX 5070 gets you a big cooler and RGB flair for the lowest price we've seen this week."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/this-silicon-power-ssd-is-selling-for-a-stunning-10-cents-per-gb-at-only-usd209-this-is-the-best-2tb-ssd-deal-on-newegg",
    "domain": "AI 算力 / 半导体",
    "title": "This Silicon Power SSD is selling for a stunning 10 cents per GB — at only $209, this is the best 2TB SSD deal on Newegg",
    "url": "https://www.tomshardware.com/pc-components/ssds/this-silicon-power-ssd-is-selling-for-a-stunning-10-cents-per-gb-at-only-usd209-this-is-the-best-2tb-ssd-deal-on-newegg",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T19:35:21+00:00",
    "summary": "Grab 2TB of storage for 10 cents per GB at Newegg. Silicon Power's P34A60 is one of the best-value SSD deals during the Black Friday sales."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-a-29-percent-discount-on-the-280-000-rpm-miaepic-z3-electric-air-duster-keeping-your-pc-clean-doesnt-have-to-be-pricey",
    "domain": "AI 算力 / 半导体",
    "title": "Get a 29% discount on the 280,000-RPM MiaEpic Z3 electric air duster",
    "url": "https://www.tomshardware.com/pc-components/get-a-29-percent-discount-on-the-280-000-rpm-miaepic-z3-electric-air-duster-keeping-your-pc-clean-doesnt-have-to-be-pricey",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T19:20:00+00:00",
    "summary": "The MiaEpic Z3 electric air duster comes with four nozzles and two brush attachments, allowing you to use it for your PC, accessories, and other things around the house. It also has a massive battery "
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/best-pc-building-tool-deals-screwdrivers-blowers",
    "domain": "AI 算力 / 半导体",
    "title": "Best Black Friday deals on tools for building PCs",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/best-pc-building-tool-deals-screwdrivers-blowers",
    "source": "Les Pounder",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T18:48:17+00:00",
    "summary": "We've scoured the internet and found the best Black Friday deals on tools."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/here-are-the-best-retro-tech-deals-weve-found-for-black-friday-deals-on-retro-tech-for-the-modern-pc-setup",
    "domain": "AI 算力 / 半导体",
    "title": "Here are the best retro tech deals we've found for Black Friday",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/here-are-the-best-retro-tech-deals-weve-found-for-black-friday-deals-on-retro-tech-for-the-modern-pc-setup",
    "source": "Les Pounder",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T18:30:12+00:00",
    "summary": "Retro tech is cool, and we've scoured the internet for the best deals on nostalgic technology."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/get-a-staggering-usd1-400-off-an-rtx-5070-powered-hp-omen-35l-gaming-desktop-sporting-an-intel-core-ultra-7-cpu-and-32gb-of-ddr5-at-38-percent-discount-this-performant-mid-tower-prebuilt-pc-packs-a-punch",
    "domain": "AI 算力 / 半导体",
    "title": "Get 38% off an RTX 5070-powered HP Omen 35L gaming desktop sporting an Intel Core Ultra 7 CPU and 32GB of DDR5",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/get-a-staggering-usd1-400-off-an-rtx-5070-powered-hp-omen-35l-gaming-desktop-sporting-an-intel-core-ultra-7-cpu-and-32gb-of-ddr5-at-38-percent-discount-this-performant-mid-tower-prebuilt-pc-packs-a-punch",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T18:20:00+00:00",
    "summary": "TKTK"
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
    "id": "hn:50657265",
    "domain": "大厂 AI 动态",
    "title": "AMD-specific fork of llama.cpp",
    "url": "https://devnull.land/amd-specific-llama-cpp",
    "source": "julianlam",
    "platform": "hackernews",
    "points": 444,
    "published_at": "2026-11-26T17:11:29+00:00",
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
    "id": "hn:50638320",
    "domain": "大厂 AI 动态",
    "title": "Gemini refused to give me the lyrics to Twinkle Twinkle Little Star",
    "url": "https://www.comentr.com/technology/01M88DWQ0R4NCMYR17AFEWRG1F",
    "source": "hoodied",
    "platform": "hackernews",
    "points": 224,
    "published_at": "2026-11-25T04:03:33+00:00",
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
    "id": "rss:https://www.theverge.com/gadgets/1044771/m5-macbook-air-black-friday-2026-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The M5 MacBook Air just got its biggest discount since Apple raised the price",
    "url": "https://www.theverge.com/gadgets/1044771/m5-macbook-air-black-friday-2026-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-28T03:30:00+00:00",
    "summary": "If you’ve been holding off on buying a new MacBook Air since Apple raised prices by $200 in June, you’re in luck. The 13-inch M5 MacBook Air is on sale at Amazon and Best Buy with 16GB of RAM and 512G"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1039190/best-black-friday-2026-deals-tech-gadgets-gift-ideas",
    "domain": "大厂 AI 动态",
    "title": "The absolute best Black Friday deals you can still get",
    "url": "https://www.theverge.com/gadgets/1039190/best-black-friday-2026-deals-tech-gadgets-gift-ideas",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-28T03:28:32+00:00",
    "summary": "Black Friday is nearly over, but many of this year’s best deals are still available. You can still find some of the lowest prices we’ve seen in-store and online for video games, wireless earbuds, TVs,"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1043445/black-friday-best-cheap-tech-deals-under-100-2026",
    "domain": "大厂 AI 动态",
    "title": "We found 60-odd Black Friday deals we love for $100 or less",
    "url": "https://www.theverge.com/gadgets/1043445/black-friday-best-cheap-tech-deals-under-100-2026",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-28T01:30:00+00:00",
    "summary": "Between holiday travel, gifts, and the rising cost of just about everything, expenses can quickly add up during this time of year. Thankfully, you don’t have to dip too far into your savings to take a"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1044706/this-purple-electric-chinese-minivan-can-go-up-to-559-miles-on-a-charge",
    "domain": "大厂 AI 动态",
    "title": "This purple electric Chinese minivan can go up to 559 miles on a charge",
    "url": "https://www.theverge.com/transportation/1044706/this-purple-electric-chinese-minivan-can-go-up-to-559-miles-on-a-charge",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-28T00:02:49+00:00",
    "summary": "Electric minivans could be the ultimate in utility, with room for passengers, gear, and huge batteries. While VW's ID Buzz only gave us 200 miles of real-world driving on a charge in 2023, China's BYD"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1043935/best-black-friday-apple-deals-2026",
    "domain": "大厂 AI 动态",
    "title": "The best Black Friday deals you can still get on AirPods, Macs, and other Apple gear",
    "url": "https://www.theverge.com/gadgets/1043935/best-black-friday-apple-deals-2026",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T23:53:19+00:00",
    "summary": "Black Friday is entering the evening, which means one of the best times of the year to save some cash on a new pair of AirPods or the latest Apple Watch is coming to a close. After all, the holiday sa"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1044487/best-black-friday-robot-vacuum-mop-deals-2026",
    "domain": "大厂 AI 动态",
    "title": "The best robot vacuums we’ve tested are up to 60 percent off for Black Friday",
    "url": "https://www.theverge.com/gadgets/1044487/best-black-friday-robot-vacuum-mop-deals-2026",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T23:32:17+00:00",
    "summary": "Black Friday is here, and if you want a little help keeping your floors clean this holiday season, now is a great time to pick up a robot vacuum. Some of the best models we’ve tested over the last yea"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1043976/sony-wh1000xm4c-noise-canceling-headphones-black-friday-2026-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Sony’s 1000XM4C headphones are a Black Friday bargain at $198",
    "url": "https://www.theverge.com/gadgets/1043976/sony-wh1000xm4c-noise-canceling-headphones-black-friday-2026-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T23:32:00+00:00",
    "summary": "Instead of purely looking forward with its headphone designs, Sony went back to its popular WH-1000XM4 design and made some improvements to make it even better. The 2026 version, called the WH-1000XM4"
  },
  {
    "id": "rss:https://www.theverge.com/games/1044715/yooka-laylees-free-upgrade-is-skipping-xbox",
    "domain": "大厂 AI 动态",
    "title": "Yooka-Laylee’s free upgrade is skipping Xbox",
    "url": "https://www.theverge.com/games/1044715/yooka-laylees-free-upgrade-is-skipping-xbox",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T23:30:32+00:00",
    "summary": "Playtronic Games is getting ready to launch Yooka-Laylee and the Impossible Lair: Definitive Edition as a free update on PlayStation 5, Switch 2, and PC on December 15th. Unfortunately for Xbox owners"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1040471/4k-bluray-movie-film-black-friday-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Many of our favorite Blu-ray movies are over 50 percent off for Black Friday",
    "url": "https://www.theverge.com/gadgets/1040471/4k-bluray-movie-film-black-friday-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T23:30:00+00:00",
    "summary": "No shade to those who love their subscription services, but viewing physical movies is a time-honored tradition that shouldn’t go away. Watching them doesn’t feel all that different, but deciding whic"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1042705/ipad-mini-black-friday-deal-sale-2026",
    "domain": "大厂 AI 动态",
    "title": "The new iPad Mini is getting its first major discount for Black Friday",
    "url": "https://www.theverge.com/gadgets/1042705/ipad-mini-black-friday-deal-sale-2026",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T22:30:00+00:00",
    "summary": "We were big fans of Apple’s new iPad Mini when we reviewed it in early November, but its steep starting price of $699 was hard to swallow. Thankfully, the small tablet is already getting a sizable dis"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/26/nvidia-hits-pause-on-chip-shipments-to-southeast-asia/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia hits pause on chip shipments to Southeast Asia",
    "url": "https://techcrunch.com/2026/11/26/nvidia-hits-pause-on-chip-shipments-to-southeast-asia/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T20:03:54+00:00",
    "summary": "Nvidia has told manufacturing partners to pause server shipments to Malaysia, Singapore, Thailand and Indonesia as the U.S. tightens its push to keep AI chips out of China."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/26/is-alice-huang-a-spy-or-not/",
    "domain": "大厂 AI 动态",
    "title": "Is Alice Huang a spy or not?",
    "url": "https://techcrunch.com/2026/11/26/is-alice-huang-a-spy-or-not/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T20:00:00+00:00",
    "summary": "The central, still-unproven claim in the Nvidia scandal is that Alice Huang, the former Megaspeed exec with whom Nvidia CEO Jensen Huang had an extramarital affair, is a Chinese spy."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/26/x-finally-gets-parental-controls-after-20-years/",
    "domain": "大厂 AI 动态",
    "title": "X finally gets parental controls after 20 years",
    "url": "https://techcrunch.com/2026/11/26/x-finally-gets-parental-controls-after-20-years/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T19:31:50+00:00",
    "summary": "Elon Musk's social network X has finally added parental controls for teenagers, giving parents and guardians a way to manage what their kids see on the platform."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/26/a-month-with-the-iphone-duo-has-changed-how-i-use-my-phone/",
    "domain": "大厂 AI 动态",
    "title": "A month with the iPhone Duo has changed how I use my phone",
    "url": "https://techcrunch.com/2026/11/26/a-month-with-the-iphone-duo-has-changed-how-i-use-my-phone/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T17:00:00+00:00",
    "summary": "From reading more books to breaking mindless scrolling habits, Apple's foldable has changed my daily routines in ways I didn't anticipate."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/26/as-anthropic-ipos-grand-theft-auto-vi-proves-why-efficiency-isnt-a-virtue/",
    "domain": "大厂 AI 动态",
    "title": "Grand Theft Auto VI proves why efficiency isn’t a virtue",
    "url": "https://techcrunch.com/2026/11/26/as-anthropic-ipos-grand-theft-auto-vi-proves-why-efficiency-isnt-a-virtue/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T16:00:00+00:00",
    "summary": "On the same day that Anthropic entered the public market, a painstakingly human video game became one of most successful entertainment launches of all time."
  },
  {
    "id": "rss:https://arstechnica.com/shopping/2026/11/the-best-black-friday-deals-ars-could-find/",
    "domain": "大厂 AI 动态",
    "title": "The best Black Friday deals Ars could find",
    "url": "https://arstechnica.com/shopping/2026/11/the-best-black-friday-deals-ars-could-find/",
    "source": "Lee Hutchinson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T17:05:37+00:00",
    "summary": "Perhaps some commerce, to help all the Turkey Day leftovers go down easier?"
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/11/intel-faced-a-choice-give-trump-10-or-face-the-consequences/",
    "domain": "大厂 AI 动态",
    "title": "Intel faced a choice: Give Trump 10% or face the consequences",
    "url": "https://arstechnica.com/tech-policy/2026/11/intel-faced-a-choice-give-trump-10-or-face-the-consequences/",
    "source": "Noah Shachtman, wired.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T12:05:01+00:00",
    "summary": "Intel faced pressure to surrender a 10% stake to unlock billions in promised grants."
  },
  {
    "id": "rss:https://arstechnica.com/shopping/2026/11/books-bikes-and-the-burbs-these-are-ars-staffs-holiday-gift-picks-for-2026/",
    "domain": "大厂 AI 动态",
    "title": "Books, bikes, and The Burbs: These are Ars staff’s holiday gift picks for 2026",
    "url": "https://arstechnica.com/shopping/2026/11/books-bikes-and-the-burbs-these-are-ars-staffs-holiday-gift-picks-for-2026/",
    "source": "Ars Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T11:30:04+00:00",
    "summary": "We polled the Ars staff about their favorite pickups this year; here's the list."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/11/volvos-big-batteries-we-drive-its-updated-2028-plug-in-hybrids/",
    "domain": "大厂 AI 动态",
    "title": "Volvo's big batteries: We drive its updated 2028 plug-in hybrids",
    "url": "https://arstechnica.com/cars/2026/11/volvos-big-batteries-we-drive-its-updated-2028-plug-in-hybrids/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T08:00:53+00:00",
    "summary": "There’s just one thing we still don’t know: How much will they cost?"
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/11/ford-unveils-the-gt41-as-it-hopes-to-win-le-mans-again/",
    "domain": "大厂 AI 动态",
    "title": "Ford unveils the GT41 as it hopes to win Le Mans again",
    "url": "https://arstechnica.com/cars/2026/11/ford-unveils-the-gt41-as-it-hopes-to-win-le-mans-again/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T18:00:29+00:00",
    "summary": "Ford enters the World Endurance Championship in 2027 with the new prototype."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/11/draining-peatlands-is-responsible-for-a-few-percent-of-our-global-warming/",
    "domain": "大厂 AI 动态",
    "title": "Draining peatlands is responsible for a few percent of our global warming",
    "url": "https://arstechnica.com/science/2026/11/draining-peatlands-is-responsible-for-a-few-percent-of-our-global-warming/",
    "source": "Scott K. Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T12:15:42+00:00",
    "summary": "Detailed estimate going back to 1800 shows how much carbon is being liberated."
  },
  {
    "id": "rss:https://arstechnica.com/features/2026/11/from-minimalist-to-maximalist-ars-staffers-show-off-their-home-offices/",
    "domain": "大厂 AI 动态",
    "title": "From minimalist to maximalist: Ars staffers show off their home offices",
    "url": "https://arstechnica.com/features/2026/11/from-minimalist-to-maximalist-ars-staffers-show-off-their-home-offices/",
    "source": "Ars Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T12:00:14+00:00",
    "summary": "Our home offices range from tasteful to \"please explain yourself.\""
  },
  {
    "id": "rss:https://www.producthunt.com/products/rankthesearch",
    "domain": "大厂 AI 动态",
    "title": "RankTheSearch",
    "url": "https://www.producthunt.com/products/rankthesearch",
    "source": "Bugrahan Zeki Kadak",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T21:53:53+00:00",
    "summary": "Make the TikTok posts your buyers are already searching for Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/nova-26",
    "domain": "大厂 AI 动态",
    "title": "NOVA",
    "url": "https://www.producthunt.com/products/nova-26",
    "source": "Bridgeye",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T13:04:35+00:00",
    "summary": "Development to deployment, and everything after. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/stacktrace",
    "domain": "大厂 AI 动态",
    "title": "Stacktrace",
    "url": "https://www.producthunt.com/products/stacktrace",
    "source": "Nico Lumma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T22:38:05+00:00",
    "summary": "Real-time steering and guardrails for AI agents Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/opencrawl",
    "domain": "大厂 AI 动态",
    "title": "OpenCrawl",
    "url": "https://www.producthunt.com/products/opencrawl",
    "source": "Nico Lumma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T22:38:08+00:00",
    "summary": "Multiplayer for your coding agents Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/wender",
    "domain": "大厂 AI 动态",
    "title": "Wender Desktop",
    "url": "https://www.producthunt.com/products/wender",
    "source": "Josh Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-27T17:15:03+00:00",
    "summary": "A 100% free Paper alternative Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/rightfont",
    "domain": "大厂 AI 动态",
    "title": "RightFont 2026",
    "url": "https://www.producthunt.com/products/rightfont",
    "source": "Chris Messina",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T23:17:29+00:00",
    "summary": "The right font, right now. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/onset",
    "domain": "大厂 AI 动态",
    "title": "Onset",
    "url": "https://www.producthunt.com/products/onset",
    "source": "Nirav Suthar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-26T19:18:34+00:00",
    "summary": "AI reviews, titles and thumbnails for YouTube creators Discussion | Link"
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
    "points": 151,
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
    "id": "hn:50617640",
    "domain": "股票",
    "title": "Two \"suspicious clusters\" on Polymarket Made Over $340k on Huang Comeback",
    "url": "https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-23-2026/card/two-groups-of-polymarket-accounts-made-over-340-000-on-huang-comeback-Lan2T0TwbJPNsyhmQHGq",
    "source": "qlte",
    "platform": "hackernews",
    "points": 60,
    "published_at": "2026-11-23T19:25:21+00:00",
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
    "id": "hn:50492993",
    "domain": "金融",
    "title": "Nvidia director sold nearly $1B in stock weeks before the Jensen Huang scandal",
    "url": "https://finance.yahoo.com/markets/stocks/articles/nvidia-director-sold-nearly-1b-160000846.html",
    "source": "LopRabbit",
    "platform": "hackernews",
    "points": 218,
    "published_at": "2026-11-14T02:21:36+00:00",
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
    "id": "hn:50605699",
    "domain": "金融",
    "title": "'It's greed': Zohran Mamdani blasts Amazon over new $5 fee hike in NYC",
    "url": "https://finance.yahoo.com/economy/policy/articles/greed-zohran-mamdani-blasts-amazon-121000124.html",
    "source": "madihaa",
    "platform": "hackernews",
    "points": 59,
    "published_at": "2026-11-23T00:23:37+00:00",
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
    "id": "hn:50528073",
    "domain": "金融",
    "title": "Elderly people are buying Teslas for the 'full self-driving.' This is a problem",
    "url": "https://www.fastcompany.com/91641371/elderly-people-are-buying-tesla-for-full-self-driving-this-is-a-problem",
    "source": "watermelon0",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-11-17T06:20:11+00:00",
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
  },
  {
    "id": "hn:50626578",
    "domain": "电子信息与芯片",
    "title": "Investigation of Polymarket Insider Trading on the Reinstatement of Jensen Huang",
    "url": "https://deucalionn.vercel.app/polymarket-delit-initie-jensen-huang-nvidia/",
    "source": "oska",
    "platform": "hackernews",
    "points": 481,
    "published_at": "2026-11-24T11:13:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50620822",
    "domain": "电子信息与芯片",
    "title": "Huang's Return Is the Biggest National Security Scandal in U.S. History",
    "url": "https://foreignpolicy.com/2026/11/23/jensen-huang-nvidia-return-ceo-national-security-scandal/",
    "source": "ortusdux",
    "platform": "hackernews",
    "points": 351,
    "published_at": "2026-11-23T23:11:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50534044",
    "domain": "电子信息与芯片",
    "title": "Jensen Huang says he’s open to returning in first statement since resignation",
    "url": "https://www.cnbc.com/2026/11/17/nvidia-jensen-huang-statement.html",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 100,
    "published_at": "2026-11-17T16:40:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50622668",
    "domain": "电子信息与芯片",
    "title": "WSJ Editorial: Restoring Huang as CEO will have major NatSec and political costs",
    "url": "https://www.wsj.com/opinion/nvidia-jensen-huang-donald-trump-130e644c",
    "source": "tedd4u",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-11-24T02:11:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:50498051",
    "domain": "电子信息与芯片",
    "title": "Smuggling of 1.5M AI GPUs could be the cause of Huang's departure",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/mass-smuggling-of-nvidia-ai-gpus-could-be-the-underlying-cause-of-jensen-huangs-departure-analysts-claim-more-than-1-5-gigawatts-of-banned-chips-tracked-to-china-despite-export-controls",
    "source": "marginalia_nu",
    "platform": "hackernews",
    "points": 61,
    "published_at": "2026-11-14T15:58:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:50527905",
    "domain": "电子信息与芯片",
    "title": "Tech leaders are convinced that Jensen Huang's exit was a plot against him",
    "url": "https://www.theverge.com/tech/1035027/tech-leaders-nvidia-jensen-huang-theories",
    "source": "madihaa",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-11-17T05:50:41+00:00",
    "summary": ""
  }
]
```
