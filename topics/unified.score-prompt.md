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

- 今日日期：`2026-10-12`
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
  "date": "2026-10-12",
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
    "id": "bvid:BV1rv4y167uC",
    "domain": "AI",
    "title": "【WorkBuddy保姆级教程】入门Agent或是工作提效，听完秒变大神！43节付费课内容全公开，完整工作流+实战技巧全揭秘，零基础一小时从入门到精通！（附资料",
    "url": "http://www.bilibili.com/video/av566052791",
    "source": "WorkBuddy课堂",
    "platform": "bilibili",
    "points": 6163955,
    "published_at": "2023-01-29T09:59:20+00:00",
    "summary": "堪称办公神器的 WorkBuddy 到底有多强？ \n依托大模型驱动的智能体，不只是简单对话，而是可以自主规划、分步执行复杂办公任务。\n文档批量处理、信息汇总、方案撰写、资料调研、任务自动化通通拿下。 \n贴合国人日常办公习惯，无需写代码，普通人也能直接上手使用。 \n解放双手，把重复枯燥工作交给 AI，专注更有价值的事。 \n本期视频完整教学，带你吃透 WorkBuddy 全部高阶能力，打工人效率跃迁必"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 2076373,
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
    "points": 1956749,
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
    "points": 1611077,
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
    "points": 1386810,
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
    "points": 1333198,
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
    "points": 1144789,
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
    "points": 946277,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 845238,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 674604,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 496539,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1rBRQBSEwB",
    "domain": "AI",
    "title": "Claude Code+DeepSeek V4 Pro安装教程｜3步从零装好开始用 | Mac Windows",
    "url": "http://www.bilibili.com/video/av116543199385810",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 420801,
    "published_at": "2026-05-09T10:10:00+00:00",
    "summary": "上期vibe coding零基础教程10万多人看了，私信和评论里问最多的居然不是怎么写需求。\n 而是Claude Code怎么装？DeepSeek怎么接进去？🫣\n\n所以这期作为补丁教程，专门帮大家搞定这3件事：\n 1️⃣ 安装Claude Code\n 2️⃣ 把DeepSeek V4 Pro百万上下文满血版接入Claude Code\n 3️⃣ 在VS Code里正式用起来\n\nMac和Windows"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 315777,
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
    "points": 304718,
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
    "points": 286432,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV154426xEha",
    "domain": "AI",
    "title": "我的 AI 编程全流程：如何使用 AI 稳定交付一个高质量的产品",
    "url": "http://www.bilibili.com/video/av117178586240848",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 280421,
    "published_at": "2026-08-29T11:38:24+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 276117,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1WWYE6LEzx",
    "domain": "AI",
    "title": "黑马程序员2026全网最夯VibeCoding零基础入门到实战项目开发全套视频教程，AI辅助编程从入门到实战，涵盖Claude Code、DeepSeek等内容",
    "url": "http://www.bilibili.com/video/av117251667724450",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 256150,
    "published_at": "2026-09-14T01:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260914\n2026黑马程序员AI智能应用开发学习路线图\nhttps://www.bilibili.com/opus/1156896913511940102\n如何下载资料\nhttps://www.bilibili.com/read/cv7881295/\n学习+球球群625260577，告别孤单，共同进步！\n\n【AI智能"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 238242,
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
    "points": 201238,
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
    "points": 183342,
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
    "points": 162560,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 133151,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1sZMq6qEko",
    "domain": "AI",
    "title": "从0做出你的第一个App ｜ 零基础AI编程保姆教程",
    "url": "http://www.bilibili.com/video/av117038647352026",
    "source": "木子不写代码",
    "platform": "bilibili",
    "points": 112169,
    "published_at": "2026-08-07T12:15:00+00:00",
    "summary": "这期视频，我会手把手带你，用 AI 做出你的第一个 App。\n全程假设你没有任何编程和AI的基础，\n我们从如何写需求提示词开始，\n到确定页面结构和设计，\n产品需求文档，\n开发计划，\n第一版APP验收，\ngit代码存档，\n二次开发，\n界面美化，\n做好的APP也会开源给到大家，\n我也会演示如何获取这个项目源代码并且用AI继续定制开发，\n视频到最后，\n你会收获一个为自己的工作和生活定制的专属APP！\n和"
  },
  {
    "id": "bvid:BV1KocTzHE3Z",
    "domain": "AI",
    "title": "2027版 Cursor+Claude AI编程 1天快速上手 视频教程",
    "url": "http://www.bilibili.com/video/av116040285622077",
    "source": "java1234官方",
    "platform": "bilibili",
    "points": 68246,
    "published_at": "2026-02-09T10:57:55+00:00",
    "summary": "本课程主要讲解Cursor简介，Cursor下载安装，Cursor生成helloWorld网页，Cursor会话里的Cursor会话里的Agent,Plan,Debug,Ask区别以及使用，Cursor常用模型介绍，Cursor模型会话上下文介绍，以及最后利用Cursor Opus4.6快速生成一个Java项目 -SpringBoot4+Vue3的学生信息管理系统，利用Cursor Opus4.6"
  },
  {
    "id": "bvid:BV15Vhy6cEhd",
    "domain": "AI",
    "title": "通俗易懂地讲解什么是Agent？",
    "url": "http://www.bilibili.com/video/av117330906449673",
    "source": "洪涛同学LovTech",
    "platform": "bilibili",
    "points": 37167,
    "published_at": "2026-09-25T09:12:59+00:00",
    "summary": "从0到1搭建一个简易Agent，从小白的角度出发解释Agent是如何运行的？"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30910,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1WwD9BEES7",
    "domain": "AI",
    "title": "保姆级ClaudeCode从0到1完整实战项目",
    "url": "http://www.bilibili.com/video/av116391835343750",
    "source": "是茂宇呀",
    "platform": "bilibili",
    "points": 30274,
    "published_at": "2026-04-12T12:59:04+00:00",
    "summary": "花了两天录制了这个教程帮助到家从0到1的完整做一个项目并带大家入门，项目中用到的相关提示词及文档教我都分享了在了www.maoyu.site"
  },
  {
    "id": "bvid:BV1BnTf6EET5",
    "domain": "AI",
    "title": "API 接入原理篇：学会一次，所有模型都能接入所有 Agent",
    "url": "http://www.bilibili.com/video/av116859332462355",
    "source": "霄Clouds",
    "platform": "bilibili",
    "points": 26262,
    "published_at": "2026-07-04T02:27:07+00:00",
    "summary": "很多人都会用 AI，却不会接 API到某个Agent，\n由于目前网上的教程大多都是&quot;手把手接某一个软件&quot;，今天教 Cursor，明天教 Claude Code，没有一个完整的体系，导致主播在学习的时候，找不到合适的教程，大部分靠自己摸索，因此，主播决定推出一个系列，用来教大家，关于API如何接入Agent的视频，\n\n本视频纯属公益，没有任何广，纯技术分享，里面大部分知识也是主播"
  },
  {
    "id": "bvid:BV1Fopg6sEyb",
    "domain": "AI",
    "title": "【必看】豆包、WorkBuddy、Codex、Claude Code、Muse...史上最全Agent使用指南",
    "url": "http://www.bilibili.com/video/av117415849563537",
    "source": "爱思考的老梨",
    "platform": "bilibili",
    "points": 25533,
    "published_at": "2026-10-10T09:30:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1LQaN6RE3v",
    "domain": "AI",
    "title": "【 豆包Agent保姆级教程】吊打付费!  豆包彻底玩明白！只看这一期就够了！10节付费课内容全公开，零基础也能学会!",
    "url": "http://www.bilibili.com/video/av117325671961695",
    "source": "豆包Agent官方教程",
    "platform": "bilibili",
    "points": 25237,
    "published_at": "2026-09-26T09:57:00+00:00",
    "summary": "资料工具评论区！\nAI智能体全自动制作漫剧工作流！小白也能快速学会！完全零基础适配AI软件，门槛低，反馈快！安装简单！不用魔法！不吃电脑配置！包含：技能，专家模块，怎么操作你电脑自动办公，怎么搭建自己的工作模型。一次性跑通！你再也不用因为人物不一致，提示词不停调整而头疼了。教你快速批量产出多个漫剧"
  },
  {
    "id": "bvid:BV1B97868EZK",
    "domain": "AI",
    "title": "Claude Code全流程开发实战丨MCP实战、Skills+Agent多工具协作、AI编程、自动化工作流、私有化部署、转行AI岗",
    "url": "http://www.bilibili.com/video/av116810192131401",
    "source": "博学谷",
    "platform": "bilibili",
    "points": 24545,
    "published_at": "2026-06-25T10:11:09+00:00",
    "summary": "视频配套资源领取方式戳：https://www.bilibili.com/opus/1217780115004456969\n或关注【博学谷】公综号回复关键词领取：260625\n学完本课程，你将能够独立完成AI Agent 研发与落地：深度掌握 Claude Code 辅助编程、Skill 技能包编排与 MCP 协议集成打通私有系统连接的“桥梁”，并能学会私有化部署。最终凭借“AI Coding 重"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22808,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 20973,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1tBuq65Epg",
    "domain": "AI",
    "title": "【前端必看】B站最细最全的前端转AI Agent开发教程，7天带你从入门到精通，2026最新版，包含所有干货！比付费强10倍，学完既可就业！",
    "url": "http://www.bilibili.com/video/av117075959876425",
    "source": "AI开发应用",
    "platform": "bilibili",
    "points": 20873,
    "published_at": "2026-08-11T09:21:12+00:00",
    "summary": "【前端必看】B站最细最全的前端转AI Agent开发教程，7天带你从入门到精通，2026最新版，包含所有干货！比付费强10倍，学完既可就业！"
  },
  {
    "id": "bvid:BV1VQYC6AEjs",
    "domain": "AI",
    "title": "【全748集】目前B站最详细的AI Agent智能体搭建全套教程，手把手带你从0到1搭建企业级智能体！全程干货无废话！让你少走99%弯路！AI大模型|LLM",
    "url": "http://www.bilibili.com/video/av117267891225919",
    "source": "Agent智能体搭建-",
    "platform": "bilibili",
    "points": 20794,
    "published_at": "2026-09-14T06:16:41+00:00",
    "summary": "【全748集】目前B站最详细的AI Agent智能体搭建全套教程，手把手带你从0到1搭建企业级智能体！全程干货无废话！让你少走99%弯路！！AI大模型|LLM"
  },
  {
    "id": "bvid:BV1E8Tk6MEkw",
    "domain": "AI",
    "title": "AI Agent教程全集丨从入门到进阶丨适合99%小白入行的Agent教程！360°讲解大模型合集（比例RAG +langchain+Agent)全程干货无废话",
    "url": "http://www.bilibili.com/video/av116848259498783",
    "source": "Agent教程",
    "platform": "bilibili",
    "points": 19016,
    "published_at": "2026-07-02T03:38:47+00:00",
    "summary": "陆陆续续也整理了不少资源，希望能帮大家少走一些弯路！无论是学业还是事业，都希望你顺顺利利  看在UP这么努力的份上，求个三连+关注嘛\n\n1️⃣ 大模型入门学习路线图（附学习资源）\n2️⃣ 大模型方向必读书籍PDF版\n3️⃣ 大模型面试题库\n4️⃣ 大模型项目源码\n5️⃣ 超详细海量大模型LLM实战项目\n6️⃣ Langchain/RAG/Agent学习资源\n7️⃣ LLM大模型系统0到1入门学习教"
  },
  {
    "id": "bvid:BV1pfuR69EoF",
    "domain": "AI",
    "title": "【全80集】零基础Vibe Coding教程，Vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av117070675118277",
    "source": "暴龙Boy",
    "platform": "bilibili",
    "points": 17428,
    "published_at": "2026-08-10T10:45:04+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1mZ8F6tE8q",
    "domain": "AI",
    "title": "本地大模型保姆级教程｜安装、概念、接入Agent，你自己的AI",
    "url": "http://www.bilibili.com/video/av117126056643965",
    "source": "老陈爱刷机",
    "platform": "bilibili",
    "points": 15762,
    "published_at": "2026-08-20T04:58:51+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV18j5DzyEmD",
    "domain": "AI",
    "title": "Cursor-AI编程完整版入门教程",
    "url": "http://www.bilibili.com/video/av114379827713362",
    "source": "SiKi老师",
    "platform": "bilibili",
    "points": 12935,
    "published_at": "2025-04-22T11:00:00+00:00",
    "summary": "更多编程教程请访问我们官网www.sikiedu.com\n\nHi，我是SiKi老师，这个课程里面老师会带着大家学习使用全球目前最火的AI编程工具-Cursor的使用。\n\n教学内容：\n1、Cursor的下载和安装\n2、Cursor的基本设置\n3、使用Cursor开发贪吃蛇游戏\n4、使用Cursor开发一个博客网站\n5、Trae（字节旗下AI编程工具）的使用初体验"
  },
  {
    "id": "bvid:BV1Q4NczHEwg",
    "domain": "AI",
    "title": "Anthropic《Claude Code 实战 | Claude Code in Action》中英字幕",
    "url": "http://www.bilibili.com/video/av116203729259669",
    "source": "GPT中英字幕课程资源",
    "platform": "bilibili",
    "points": 11318,
    "published_at": "2026-03-14T00:00:00+00:00",
    "summary": "https://anthropic.skilljar.com/claude-code-in-action"
  },
  {
    "id": "bvid:BV195ydBxEfq",
    "domain": "AI",
    "title": "低成本小智MCP服务器",
    "url": "http://www.bilibili.com/video/av115478752140541",
    "source": "小闹一起",
    "platform": "bilibili",
    "points": 9975,
    "published_at": "2025-11-02T06:59:56+00:00",
    "summary": "低成本小智MCP服务器部署\n工具作者https://www.bilibili.com/video/BV1hxMbzqEzU/?spm_id_from=333.1391.0.0\n用到的工具:https://www.123865.com/s/zN6vjv-QH6av"
  },
  {
    "id": "bvid:BV1iShJ6bEAL",
    "domain": "AI",
    "title": "【全748集】目前B站最细最全的AI Agent零基础全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！",
    "url": "http://www.bilibili.com/video/av117314045350194",
    "source": "Agent产品",
    "platform": "bilibili",
    "points": 8716,
    "published_at": "2026-10-04T06:22:00+00:00",
    "summary": "【全748集】目前B站最细最全的AI Agent零基础全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！"
  },
  {
    "id": "bvid:BV1snhi6WE5P",
    "domain": "AI",
    "title": "【Cursor使用教程】史上最强AI编程工具Cursor！Cursor入门到精通保姆级教程！安装搭建/高阶技巧使用/开发小游戏/应用场景案例实战",
    "url": "http://www.bilibili.com/video/av117308156614035",
    "source": "图灵课堂",
    "platform": "bilibili",
    "points": 7582,
    "published_at": "2026-09-21T08:55:13+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n全套AI大模型笔记/学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1UDPWzgEFH",
    "domain": "AI",
    "title": "AI帮你写完+测完，编程丝滑到飞起！Cursor 一镜到底全流程：规则 → 方案 → Agent编码 → 自动化测试 | 2026 独立开发者必备神器",
    "url": "http://www.bilibili.com/video/av116182002701930",
    "source": "南哥AGI研习社",
    "platform": "bilibili",
    "points": 7390,
    "published_at": "2026-03-06T11:33:46+00:00",
    "summary": "YouTube、B站频道关于AI Coding Cursor等开发经验分享，所有资源全部开源免费\n\n🙏🏻如果内容对你有帮助，拜托给我的视频点个赞，你们的支持就是我持续开源分享的功力                    \n个人项目GitHub地址：https://github.com/NanGePlus                    \n个人项目Gitee地址：https://gitee.c"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 7305,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔~\n【视频配套籽料+1V1问题解答请看 ”置顶平论” 哦】"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6868,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1xLtS6WEVG",
    "domain": "AI",
    "title": "DeepSeek Harness的MCP应用教程、MCP安装、MCP迁移、MCP删除与卸载",
    "url": "http://www.bilibili.com/video/av117201218635665",
    "source": "eogee",
    "platform": "bilibili",
    "points": 6827,
    "published_at": "2026-09-02T11:33:53+00:00",
    "summary": "MCP 是扩展 Agent 能力的主要方式：接入一个 MCP 服务器，Agent 就能获得一整套现成的外部工具。DeepSeek Harness（命令名 `dsh`，简称 DSH）内置了 MCP 客户端桥插件，配置即可接入社区海量 MCP 服务。本教程以实战为主线，介绍在 dsh 中接入现成 MCP 服务、接入自定义 MCP 服务的完整流程，给出从 Claude Code、Codex 迁移配置的对"
  },
  {
    "id": "bvid:BV1NxcCzEEBq",
    "domain": "AI",
    "title": "【Claude Code 实战】一次搞懂 OpenSpec，让专案每次迭代都有依据",
    "url": "http://www.bilibili.com/video/av116217436182465",
    "source": "西技大神",
    "platform": "bilibili",
    "points": 6795,
    "published_at": "2026-03-12T18:04:11+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1UaYK6nEjP",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av117244419903051",
    "source": "茶子兀",
    "platform": "bilibili",
    "points": 6114,
    "published_at": "2026-09-10T02:39:36+00:00",
    "summary": ""
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
    "id": "hn:49906100",
    "domain": "AI 算力 / 半导体",
    "title": "OpenDLSS: A Vulkan Reimplementation of Nvidia's DLSS 5 Neural Rendering Network",
    "url": "https://github.com/maanHimself/OpenDLSS-NR",
    "source": "sagacity",
    "platform": "hackernews",
    "points": 279,
    "published_at": "2026-09-30T08:43:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:50035886",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia in talks to acquire US 'open' model startup Reflection AI",
    "url": "https://www.ft.com/content/052610c5-22b4-4dd4-932e-b7f9f0628b6a",
    "source": "arkj",
    "platform": "hackernews",
    "points": 176,
    "published_at": "2026-10-10T18:48:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49714096",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC revealing details about next gen A14 node",
    "url": "https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331",
    "source": "osnium123",
    "platform": "hackernews",
    "points": 129,
    "published_at": "2026-09-15T15:31:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49926773",
    "domain": "AI 算力 / 半导体",
    "title": "Show HN: Janus – Go binary that runs GGUF models via Vulkan on AMD/Intel/Nvidia",
    "url": "https://github.com/Vibra-Ingenn/Janus",
    "source": "Maverick617",
    "platform": "hackernews",
    "points": 106,
    "published_at": "2026-10-01T20:36:47+00:00",
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
    "id": "rss:https://www.eetimes.com/security-becomes-a-sign-off-item/",
    "domain": "AI 算力 / 半导体",
    "title": "Security Becomes a Sign-off Item",
    "url": "https://www.eetimes.com/security-becomes-a-sign-off-item/",
    "source": "Moshe Zalcberg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T07:10:22+00:00",
    "summary": "Europe’s CRA turns chip security into auditable sign-off, pushing silicon teams to prove resilience before 2027. The post Security Becomes a Sign-off Item appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/reddit-user-pays-usd35-for-a-crypto-mining-rig-left-in-a-garage-and-gets-54gb-of-vram-at-65-cents-per-gb-the-first-test-for-2017-era-gpus-a-35b-parameter-ai-model-running-locally-at-over-30-tokens-per-second",
    "domain": "AI 算力 / 半导体",
    "title": "Reddit user pays $35 for a crypto mining rig left in a garage and gets 54GB of VRAM at 65 cents per GB",
    "url": "https://www.tomshardware.com/pc-components/gpus/reddit-user-pays-usd35-for-a-crypto-mining-rig-left-in-a-garage-and-gets-54gb-of-vram-at-65-cents-per-gb-the-first-test-for-2017-era-gpus-a-35b-parameter-ai-model-running-locally-at-over-30-tokens-per-second",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T10:00:00+00:00",
    "summary": "A Reddit user bought a nine-GPU Nvidia P106-100 mining rig with 54GB of VRAM for $35 and ran Qwen3.6-35B-A3B on it locally."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/console-market-craters-as-xbox-sales-crash-33-percent-to-the-lowest-since-launch-25-years-ago-ps5-sales-drop-25-percent-steep-price-hikes-push-series-x-to-usd800-and-ps5-pro-to-usd900",
    "domain": "AI 算力 / 半导体",
    "title": "Console market craters as Xbox sales crash 33% to the lowest since launch 25 years ago, PS5 sales drop 25%",
    "url": "https://www.tomshardware.com/video-games/console-gaming/console-market-craters-as-xbox-sales-crash-33-percent-to-the-lowest-since-launch-25-years-ago-ps5-sales-drop-25-percent-steep-price-hikes-push-series-x-to-usd800-and-ps5-pro-to-usd900",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T16:30:00+00:00",
    "summary": "PlayStation sales dropped by 25% YTD compared to last year, while Xbox contracted by 33%, marking the biggest decline in retail sales over the past decade."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/cyberleek-threatens-full-gta-6-build-leak-unless-take-two-apologizes-and-his-usd30-million-crypto-memecoin-goal-is-met-leaker-demands-physical-release-while-pumping-solana-memecoin-to-usd30m",
    "domain": "AI 算力 / 半导体",
    "title": "Cyberleek threatens full GTA 6 build leak unless Take-Two apologizes and his $30 million crypto memecoin goal is met",
    "url": "https://www.tomshardware.com/software/linux/cyberleek-threatens-full-gta-6-build-leak-unless-take-two-apologizes-and-his-usd30-million-crypto-memecoin-goal-is-met-leaker-demands-physical-release-while-pumping-solana-memecoin-to-usd30m",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T16:10:00+00:00",
    "summary": "Notorious GTA VI leaker Cyberleek is threatening to release a full build of GTA VI if Take-Two doesn't release a physical build, but only if its memecoin hits $30 million."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/canadian-youtuber-builds-flock-like-camera-to-exclusively-track-police-vehicles-officers-visit-his-home-to-express-privacy-concerns",
    "domain": "AI 算力 / 半导体",
    "title": "Canadian YouTuber builds 'Flock-like' camera to exclusively track police vehicles",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/canadian-youtuber-builds-flock-like-camera-to-exclusively-track-police-vehicles-officers-visit-his-home-to-express-privacy-concerns",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T15:11:18+00:00",
    "summary": "Canadian YouTuber Anthony Sistilli says police questioned him after he built an ALPR camera designed to track police vehicles, leading to an ironic discussion over the privacy risks of mass license-pl"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/modder-discovers-that-putting-a-gpu-in-the-wrong-place-can-deliver-a-19-degree-cooler-hotspot-breaking-convention-can-produce-great-results-despite-decades-of-pc-diy-evolution",
    "domain": "AI 算力 / 半导体",
    "title": "Modder discovers that putting a GPU in the 'wrong place' can deliver a 19 degree cooler hotspot",
    "url": "https://www.tomshardware.com/pc-components/gpus/modder-discovers-that-putting-a-gpu-in-the-wrong-place-can-deliver-a-19-degree-cooler-hotspot-breaking-convention-can-produce-great-results-despite-decades-of-pc-diy-evolution",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T14:23:20+00:00",
    "summary": "In PC DIY it might still be worth challenging convention, as TrashBench shows with his GPU hotspot getting up to 19C cooler."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/russian-disinformation-bot-traffic-nearly-eliminated-overnight-after-ukraine-drone-strikes-cripple-multiple-of-russias-google-data-centers-ukraine-intensifies-bombing-of-yandex-data-centers-in-response-to-moscows-strikes-on-kyiv-data-centers",
    "domain": "AI 算力 / 半导体",
    "title": "Russia's Yandex bot traffic nearly eliminated overnight after Ukraine drone strikes cripple multiple of 'Russia's Google' data centers",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/russian-disinformation-bot-traffic-nearly-eliminated-overnight-after-ukraine-drone-strikes-cripple-multiple-of-russias-google-data-centers-ukraine-intensifies-bombing-of-yandex-data-centers-in-response-to-moscows-strikes-on-kyiv-data-centers",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T13:15:09+00:00",
    "summary": "Russian bot traffic falls dramatically as Ukraine takes out several Yandex data centers."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/sandisk-nas-800-1-92tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "Sandisk NAS 800 1.92TB SSD Review: Endurance at a premium",
    "url": "https://www.tomshardware.com/pc-components/ssds/sandisk-nas-800-1-92tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T13:05:59+00:00",
    "summary": "The Sandisk NAS 800 is a high-end PCIe 5.0 NVMe SSD built for NAS workloads, with high endurance, strong sustained write performance, and low 4KB random latency. It’s mainly held back by its high pric"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/developer-turns-classic-windows-minesweeper-into-hand-holding-big-budget-triple-a-parody-browser-reboot-mocks-modern-gaming-with-chatty-npcs-internal-monologues-and-promised-loot-boxes",
    "domain": "AI 算力 / 半导体",
    "title": "Developer turns classic Windows Minesweeper into hand-holding 'big-budget, Triple-A’ parody",
    "url": "https://www.tomshardware.com/video-games/developer-turns-classic-windows-minesweeper-into-hand-holding-big-budget-triple-a-parody-browser-reboot-mocks-modern-gaming-with-chatty-npcs-internal-monologues-and-promised-loot-boxes",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T12:50:00+00:00",
    "summary": "This reboot of Minesweeper makes it feel like a big budget game created by a massive game studio."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/programmer-ports-super-mario-64-to-microsofts-zune-hd-media-player-the-2009-ipod-rival-runs-the-game-natively-on-its-nvidia-tegra-chip-with-touchscreen-controls-and-saves",
    "domain": "AI 算力 / 半导体",
    "title": "Programmer ports Super Mario 64 to Microsoft’s Zune HD media player",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/programmer-ports-super-mario-64-to-microsofts-zune-hd-media-player-the-2009-ipod-rival-runs-the-game-natively-on-its-nvidia-tegra-chip-with-touchscreen-controls-and-saves",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T12:30:00+00:00",
    "summary": "A fan port of Nintendo’s Super Mario 64 runs natively on Microsoft’s 2009 Zune HD media player, with touch controls and saves."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/two-steam-games-generated-usd560-000-across-135-000-sales-but-the-co-creator-only-took-home-usd15-000-annually-high-chinese-refund-rates-steams-30-percent-fee-and-publisher-cuts-eat-most-of-the-profit-leaving-the-co-creator-driving-a-2012-mazda",
    "domain": "AI 算力 / 半导体",
    "title": "Two Steam games generated $560,000 across 135,000 sales, but the co-creator only took home $15,000 annually",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/two-steam-games-generated-usd560-000-across-135-000-sales-but-the-co-creator-only-took-home-usd15-000-annually-high-chinese-refund-rates-steams-30-percent-fee-and-publisher-cuts-eat-most-of-the-profit-leaving-the-co-creator-driving-a-2012-mazda",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T12:10:00+00:00",
    "summary": "Game developer explains how $560,000 in Steam sales gets reduced to $146,000 in pockets — breakdown highlights harsh realities of gaming business"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/cryptomining-malware-used-poetry-to-infect-more-than-3-400-servers-researchers-say-four-words-in-the-poellm-verse-changed-11-times-point-the-botnet-to-new-servers",
    "domain": "AI 算力 / 半导体",
    "title": "Cryptomining malware used poetry to infect more than 3,400 servers, researchers say",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/cryptomining-malware-used-poetry-to-infect-more-than-3-400-servers-researchers-say-four-words-in-the-poellm-verse-changed-11-times-point-the-botnet-to-new-servers",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T11:45:00+00:00",
    "summary": "Lumen's Black Lotus Labs says PoeLLM malware has hit more than 3,400 servers, most of them exposed AI tools like LiteLLM and Ollama."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/state-of-california-sues-3d-printer-filament-company-polymaker-for-promoting-ghost-guns-by-marketing-to-3d-printed-gun-community-state-alleges-company-turns-harmless-pla-filament-into-a-regulated-firearm-precursor-part",
    "domain": "AI 算力 / 半导体",
    "title": "State of California sues 3D printer filament company Polymaker for promoting ghost guns by marketing to 3D-printed gun community",
    "url": "https://www.tomshardware.com/3d-printing/state-of-california-sues-3d-printer-filament-company-polymaker-for-promoting-ghost-guns-by-marketing-to-3d-printed-gun-community-state-alleges-company-turns-harmless-pla-filament-into-a-regulated-firearm-precursor-part",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T11:15:00+00:00",
    "summary": "The newly formed Consumer Fairness and Public Protection Division is also targeting Roblox and AppLovin."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/microsoft-office/creator-of-free-adobe-clones-unveils-open-source-microsoft-office-excel-powerpoint-and-word-replications-autodesk-tools-and-other-subscription-based-services-may-come-next",
    "domain": "AI 算力 / 半导体",
    "title": "Creator of free Adobe clones unveils open-source Microsoft Office Excel, PowerPoint, and Word replications",
    "url": "https://www.tomshardware.com/software/microsoft-office/creator-of-free-adobe-clones-unveils-open-source-microsoft-office-excel-powerpoint-and-word-replications-autodesk-tools-and-other-subscription-based-services-may-come-next",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T10:50:00+00:00",
    "summary": "ArtCraft is expanding its roster of open-source creative tools as cross-platform alternatives to predatory subscription models."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/supercomputers/working-cray-1-supercomputer-replica-packs-30-vintage-mac-minis-and-1-5-tflops-passively-cooled-tribute-is-9-375x-faster-than-the-1976-supercomputer",
    "domain": "AI 算力 / 半导体",
    "title": "New Cray-1 supercomputer replica built with 30 vintage Mac Minis and packs 1.5 TFLOPS of compute",
    "url": "https://www.tomshardware.com/tech-industry/supercomputers/working-cray-1-supercomputer-replica-packs-30-vintage-mac-minis-and-1-5-tflops-passively-cooled-tribute-is-9-375x-faster-than-the-1976-supercomputer",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T10:20:00+00:00",
    "summary": "Legendary 1975 supercomputer gets a modernized replica with old Mac Minis, showcasing decades of innovation."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/space/u-s-military-backed-cargo-pod-promises-90-minute-orbital-delivery-anywhere-on-earth-10-ton-ghost-vehicle-gets-first-real-world-test-sierra-space-drops-radio-and-whiskey-from-68-500-feet-to-test-starcraft-like-supply-drops",
    "domain": "AI 算力 / 半导体",
    "title": "US military-backed cargo pod promises 90-minute orbital delivery anywhere on Earth, 10-ton Ghost vehicle gets first real-world test",
    "url": "https://www.tomshardware.com/tech-industry/space/u-s-military-backed-cargo-pod-promises-90-minute-orbital-delivery-anywhere-on-earth-10-ton-ghost-vehicle-gets-first-real-world-test-sierra-space-drops-radio-and-whiskey-from-68-500-feet-to-test-starcraft-like-supply-drops",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T10:00:00+00:00",
    "summary": "Sierra Space is testing its Ghost reentry vehicle, which is designed to deliver supplies to any unit across the world within 90 minutes."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ugreens-100w-4-port-gan-charger-drops-27-percent-today-get-100w-of-power-and-four-ports-for-just-usd39-98",
    "domain": "AI 算力 / 半导体",
    "title": "Ugreen’s 100W 4-port GaN charger drops 27% today",
    "url": "https://www.tomshardware.com/pc-components/ugreens-100w-4-port-gan-charger-drops-27-percent-today-get-100w-of-power-and-four-ports-for-just-usd39-98",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T16:20:56+00:00",
    "summary": "Whether you need to charge a laptop before work, top up your smartphone, or keep your tablet ready for travel, this four-port Ugreen GaN charger delivers up to 100W via USB Type-C and is currently $15"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/softbank-seeks-usd100-billion-for-ai-refined-projects-from-middle-eastern-investors-fund-would-be-used-to-acquire-companies-and-improve-their-operations-using-artificial-intelligence-and-robotics",
    "domain": "AI 算力 / 半导体",
    "title": "SoftBank seeks $100 billion for AI-refined projects from Middle Eastern investors",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/softbank-seeks-usd100-billion-for-ai-refined-projects-from-middle-eastern-investors-fund-would-be-used-to-acquire-companies-and-improve-their-operations-using-artificial-intelligence-and-robotics",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T15:40:00+00:00",
    "summary": "SoftBank plans to buy companies that do not use AI or robotics, then apply new technologies to improve their operations and valuation."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/super-micro-smuggling-co-conspirator-pleads-guilty-to-sending-ai-chips-to-china-broker-admits-breaking-export-control-rules-as-company-co-founder-denies-charges",
    "domain": "AI 算力 / 半导体",
    "title": "Super Micro smuggling co-conspirator pleads guilty to sending AI chips to China",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/super-micro-smuggling-co-conspirator-pleads-guilty-to-sending-ai-chips-to-china-broker-admits-breaking-export-control-rules-as-company-co-founder-denies-charges",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T15:35:00+00:00",
    "summary": "Ting-Wei \"Willy\" Sun, one of the three people charged of smuggling Super Micro servers with advanced Nvidia AI chips to China, has pleaded guilty, with sentencing set for September of next year."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/ps5-hack-delivers-native-ps2-disc-support-and-4k-upscaling-where-sony-refused-to-after-ps2-breakthrough-homebrew-dev-confirms-ps3-disc-support-is-next-for-ps5",
    "domain": "AI 算力 / 半导体",
    "title": "PS5 hack delivers native PS2 disc support and 4K upscaling where Sony refused to",
    "url": "https://www.tomshardware.com/video-games/playstation/ps5-hack-delivers-native-ps2-disc-support-and-4k-upscaling-where-sony-refused-to-after-ps2-breakthrough-homebrew-dev-confirms-ps3-disc-support-is-next-for-ps5",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T15:17:15+00:00",
    "summary": "Modder Sword has released PS5SX2 for the PlayStation 5, allowing gamers to play discs from previous PlayStation 2 games."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-october-10-2026-tencent-grabs-bargain-chips-qualcomm-huawei-ip-deal-groq-lawsuit-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "This week on Tom's Hardware Premium: October 10, 2026",
    "url": "https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-october-10-2026-tencent-grabs-bargain-chips-qualcomm-huawei-ip-deal-groq-lawsuit-and-more",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T15:00:00+00:00",
    "summary": "This week on Tom's Hardware Premium, we covered how the AI buildout is affecting the industry supporting it across all axioms, including in law, chip design, manufacturing, and finance."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/senate-investigation-says-that-some-ai-data-center-claims-are-misleading-senators-question-number-of-permanent-jobs-projects-bring-to-communities-but-companies-refuse-to-divulge-data",
    "domain": "AI 算力 / 半导体",
    "title": "Senate investigation says that some AI data center claims are misleading",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/senate-investigation-says-that-some-ai-data-center-claims-are-misleading-senators-question-number-of-permanent-jobs-projects-bring-to-communities-but-companies-refuse-to-divulge-data",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T14:40:00+00:00",
    "summary": "A Senate investigation on AI data centers question that costs and benefits that AI hyperscalers show when they apply for permits to put up their developments. The report says that these claims are mis"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/we-tested-gaming-performance-in-17-year-old-windows-7-against-windows-11-on-a-modern-gaming-pc-older-operating-system-delivers-advantages-in-some-scenarios",
    "domain": "AI 算力 / 半导体",
    "title": "We tested gaming performance in 17-year-old Windows 7 on a modern gaming PC against Windows 11",
    "url": "https://www.tomshardware.com/software/windows/we-tested-gaming-performance-in-17-year-old-windows-7-against-windows-11-on-a-modern-gaming-pc-older-operating-system-delivers-advantages-in-some-scenarios",
    "source": "Dan Mateescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T13:40:00+00:00",
    "summary": "We managed to install Windows 7 on a modern PC and put it to the test across eight DirectX 11 games and two DirectX 9 titles to see how its gaming performance compares to Windows 11 today."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/top-ai-labs-reportedly-planning-for-catastrophic-ai-event-fallout-anthropic-openai-and-others-reportedly-building-contingency-plans-and-running-scenarios-of-a-runaway-ai-wreaking-havoc",
    "domain": "AI 算力 / 半导体",
    "title": "Top AI labs reportedly planning for catastrophic AI event fallout",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/top-ai-labs-reportedly-planning-for-catastrophic-ai-event-fallout-anthropic-openai-and-others-reportedly-building-contingency-plans-and-running-scenarios-of-a-runaway-ai-wreaking-havoc",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T13:20:00+00:00",
    "summary": "One focus of these contingency plans is how to manage Congress after a catastrophic event puts these labs in the spotlight."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/free-steam-demo-runs-up-usd1-000-daily-ai-bill-and-forces-devs-to-take-out-bank-loan-studio-eyes-local-hardware-models-to-escape-cloud-limits-as-cheaper-automatic-fallback-ai-models-create-problems-game-uses-ai-to-process-your-voice-and-build-responses",
    "domain": "AI 算力 / 半导体",
    "title": "Free Steam demo runs up $1,000 daily AI bill and forces devs to take out bank loan",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/free-steam-demo-runs-up-usd1-000-daily-ai-bill-and-forces-devs-to-take-out-bank-loan-studio-eyes-local-hardware-models-to-escape-cloud-limits-as-cheaper-automatic-fallback-ai-models-create-problems-game-uses-ai-to-process-your-voice-and-build-responses",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T12:52:20+00:00",
    "summary": "Easy Fox were surprised by the number of users and didn't expect that the demo's popularity would cause its AI expenses to go that high."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-halts-geforce-rtx-5090-production-in-favor-of-ai-data-center-and-professional-gpus-impending-supply-drought-expected-to-drive-up-prices-rtx-5080-24gb-rumored-as-new-gaming-flagship",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia reportedly halts GeForce RTX 5090 production in favor of AI data center and professional GPUs",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-halts-geforce-rtx-5090-production-in-favor-of-ai-data-center-and-professional-gpus-impending-supply-drought-expected-to-drive-up-prices-rtx-5080-24gb-rumored-as-new-gaming-flagship",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T12:20:00+00:00",
    "summary": "Nvidia reportedly discontinues GeForce RTX 5090-series products leaving GB202 for data center and professional graphics boards. GeForce RTX 5080 24 GB rumored to become de-facto flagship from the gree"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/dlss-5-on-pac-man-is-a-creepypasta-one-rendering-mode-even-removes-the-eyes-of-a-ghost",
    "domain": "AI 算力 / 半导体",
    "title": "Ukranian modder slaps DLSS 5 onto Pac-Man with 4x Multipass",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/dlss-5-on-pac-man-is-a-creepypasta-one-rendering-mode-even-removes-the-eyes-of-a-ghost",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T12:00:00+00:00",
    "summary": "Russian YouTube channel dedicated to DLSS 5 experiments tries Pac-Man, and it's genuinely cursed."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/anyps5-reaches-critical-gpu-milestone-with-100-percent-shader-instruction-coverage-ps5-games-running-natively-on-pc-still-far-off",
    "domain": "AI 算力 / 半导体",
    "title": "AnyPS5 project reaches critical GPU milestone in race to enable running PS5 games natively on PC",
    "url": "https://www.tomshardware.com/video-games/playstation/anyps5-reaches-critical-gpu-milestone-with-100-percent-shader-instruction-coverage-ps5-games-running-natively-on-pc-still-far-off",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T11:30:00+00:00",
    "summary": "The open-source AnyPS5 project has reached 100% GPU shader instruction coverage."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/crazed-modder-straps-360mm-aio-radiator-to-laptop-cuts-temps-below-40-degrees-performance-gains-an-average-of-14-percent-in-games-and-benchmarks",
    "domain": "AI 算力 / 半导体",
    "title": "Crazed modder straps 360mm AIO radiator to laptop, cuts temps to below 40 degrees",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/crazed-modder-straps-360mm-aio-radiator-to-laptop-cuts-temps-below-40-degrees-performance-gains-an-average-of-14-percent-in-games-and-benchmarks",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T11:00:00+00:00",
    "summary": "PC modder TrashBench attached a 360mm radiator and custom cooling to a laptop and gained up to 14% in performance at the cost of the definition of a laptop."
  },
  {
    "id": "hn:49879032",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang says AI distillation is 'competition.'",
    "url": "https://www.cnbc.com/2026/09/28/nvidias-jensen-huang-ai-distillation-china.html",
    "source": "cramer4next",
    "platform": "hackernews",
    "points": 73,
    "published_at": "2026-09-28T14:55:34+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/manfred-horstmann-globalfoundries-bets-on-fdx-fusion-for-physical-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Manfred Horstmann: GlobalFoundries Bets on FDX Fusion for Physical AI",
    "url": "https://www.eetimes.com/manfred-horstmann-globalfoundries-bets-on-fdx-fusion-for-physical-ai/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T22:00:00+00:00",
    "summary": "GlobalFoundries said strained-silicon FD-SOI can deliver 7-nm-class performance without EUV and open a new market for Europe. The post Manfred Horstmann: GlobalFoundries Bets on FDX Fusion for Physica"
  },
  {
    "id": "rss:https://www.eetimes.com/solid-state-transformers-accelerate-your-sst-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Solid-State Transformers: Accelerate Your SST Design",
    "url": "https://www.eetimes.com/solid-state-transformers-accelerate-your-sst-design/",
    "source": "Infineon Technologies, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T15:38:47+00:00",
    "summary": "Join our expert-led webinar to explore Infineon's comprehensive portfolio for Solid-State Transformers (SSTs). The post Solid-State Transformers: Accelerate Your SST Design appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/connecting-chiplets-isnt-enough-solving-the-data-movement-challenge-in-multi-die-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Connecting Chiplets Isn’t Enough – Solving the Data Movement Challenge in Multi-Die Systems",
    "url": "https://www.eetimes.com/connecting-chiplets-isnt-enough-solving-the-data-movement-challenge-in-multi-die-systems/",
    "source": "Arteris",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T14:21:07+00:00",
    "summary": "Join this BitCast and explore how extending NoC connectivity across die boundaries enables engineering teams to scale from monolithic SoCs to multi-die architectures. The post Connecting Chiplets Isn’"
  },
  {
    "id": "rss:https://www.eetimes.com/u-s-manufacturing-activity-sustains-growth-in-september-as-backlogs-surge/",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Manufacturing Activity Sustains Growth in September as Backlogs Surge",
    "url": "https://www.eetimes.com/u-s-manufacturing-activity-sustains-growth-in-september-as-backlogs-surge/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T12:11:04+00:00",
    "summary": "Manufacturing maintains nine-month growth streak despite soaring costs and trade barriers. The post U.S. Manufacturing Activity Sustains Growth in September as Backlogs Surge appeared first on EE Time"
  },
  {
    "id": "rss:https://www.eetimes.com/physical-ai-needs-a-neuromorphic-path-from-sensor-to-silicon/",
    "domain": "AI 算力 / 半导体",
    "title": "Physical AI Needs a Neuromorphic Path from Sensor to Silicon",
    "url": "https://www.eetimes.com/physical-ai-needs-a-neuromorphic-path-from-sensor-to-silicon/",
    "source": "Xabier Iturbe",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T08:39:41+00:00",
    "summary": "Physical AI will be limited in the real world if we keep pretending that physical data comes packaged like the digital world. The post Physical AI Needs a Neuromorphic Path from Sensor to Silicon appe"
  },
  {
    "id": "rss:https://www.eetimes.com/worlds-first-single-chip-multiturn-position-sensor-in-smaller-form-factor/",
    "domain": "AI 算力 / 半导体",
    "title": "Worlds First Single Chip Multiturn Position Sensor in Smaller Form Factor",
    "url": "https://www.eetimes.com/worlds-first-single-chip-multiturn-position-sensor-in-smaller-form-factor/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T08:08:26+00:00",
    "summary": "Join this webinar, where our expert will explore the technology behind the ADMT4000 and how its ability to track multiple rotations and angular movement without power is transforming the design of bot"
  },
  {
    "id": "rss:https://www.eetimes.com/scaling-3d-ic-design-trends-challenges-and-practical-workflows/",
    "domain": "AI 算力 / 半导体",
    "title": "Scaling 3D IC design: Trends, Challenges and Practical Workflows",
    "url": "https://www.eetimes.com/scaling-3d-ic-design-trends-challenges-and-practical-workflows/",
    "source": "Siemens EDA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-09T07:32:29+00:00",
    "summary": "Join us to discover how Siemens Innovator3D IC streamlines 3D IC design from planning to implementation! The post Scaling 3D IC design: Trends, Challenges and Practical Workflows appeared first on EE "
  },
  {
    "id": "rss:https://www.eetimes.com/why-custom-silicon-matters-in-ai-data-centers/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Custom Silicon Matters in AI Data Centers",
    "url": "https://www.eetimes.com/why-custom-silicon-matters-in-ai-data-centers/",
    "source": "Scott Seal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T19:16:44+00:00",
    "summary": "Custom silicon lets AI data centers cut power, latency and data movement while improving economics at scale. The post Why Custom Silicon Matters in AI Data Centers appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/schiederwerk-showcases-novel-power-supply-solutions-for-mission-critical-applications-at-electronica-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "SCHIEDERWERK Showcases Novel Power Supply Solutions for Mission-Critical Applications at electronica 2026",
    "url": "https://www.eetimes.com/schiederwerk-showcases-novel-power-supply-solutions-for-mission-critical-applications-at-electronica-2026/",
    "source": "SCHIEDERWERK",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-08T14:23:33+00:00",
    "summary": "Nuremberg / Munich, Germany, 2026 — SCHIEDERWERK GmbH, a specialist in custom power electronics solutions engineered and manufactured in Germany, will showcase its latest platform-based power supplies"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/second-russian-data-center-targeted-by-ukrainian-drones-in-just-two-days-as-yandex-reels-from-another-service-outage-russian-state-media-admits-that-multiple-modules-completely-taken-out",
    "domain": "AI 算力 / 半导体",
    "title": "Ukrainian drones strike largest data center in Russia, multiple parts of 1.4 million square foot campus knocked offline",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/second-russian-data-center-targeted-by-ukrainian-drones-in-just-two-days-as-yandex-reels-from-another-service-outage-russian-state-media-admits-that-multiple-modules-completely-taken-out",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T10:30:00+00:00",
    "summary": "Following a Ukrainian drone strike on a D.C. in Sasovo, Russia, a Yandex facility in Kaluga has suffered a similar fate with multiple modules completely out of service."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/worlds-first-3d-printed-remote-control-aircraft-with-a-jet-turbine-takes-flight-aims-for-mach-0-8-to-beat-world-record-for-fastest-model-aircraft-mostly-printed-using-standard-petg-materials",
    "domain": "AI 算力 / 半导体",
    "title": "World’s first 3D-printed remote control aircraft with a jet turbine takes flight, aims for Mach 0.8 to beat world record for fastest model aircraft",
    "url": "https://www.tomshardware.com/3d-printing/worlds-first-3d-printed-remote-control-aircraft-with-a-jet-turbine-takes-flight-aims-for-mach-0-8-to-beat-world-record-for-fastest-model-aircraft-mostly-printed-using-standard-petg-materials",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T10:00:00+00:00",
    "summary": "Team of graduates attempts to beat Guiness World Record for fastest jet-powered model aircraft using PETG and clever engineering."
  },
  {
    "id": "hn:49346906",
    "domain": "AI 算力 / 半导体",
    "title": "Ask HN: Do you feel comfortable admitting that you use AI?",
    "url": "https://news.ycombinator.com/item?id=49346906",
    "source": "var0xyz",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-18T15:16:15+00:00",
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
    "id": "hn:49913571",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/",
    "source": "bradleyg223",
    "platform": "hackernews",
    "points": 1704,
    "published_at": "2026-09-30T20:04:37+00:00",
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
    "points": 773,
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
    "id": "hn:49715947",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Live and 3.8 Live Extended Thinking",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/",
    "source": "leumon",
    "platform": "hackernews",
    "points": 493,
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
    "id": "hn:50042149",
    "domain": "大厂 AI 动态",
    "title": "What driving across Europe costs in tolls, vignettes, bridges and fuel",
    "url": "https://copilot.travel/tolls/europe-2026",
    "source": "heikkikalliokos",
    "platform": "hackernews",
    "points": 52,
    "published_at": "2026-10-11T11:39:10+00:00",
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
    "id": "hn:49697014",
    "domain": "大厂 AI 动态",
    "title": "Notes on gotchas while migrating 35kb preprompts from Opus to self-hosted Ollama",
    "url": "https://patrickmccanna.net/notes-on-migrating-large-prompts-away-from-anthropic-openai-to-self-hosted-llms/",
    "source": "0o_MrPatrick_o0",
    "platform": "hackernews",
    "points": 140,
    "published_at": "2026-09-14T13:59:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:49914236",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon (High): Intelligence, Performance and Price Analysis",
    "url": "https://artificialanalysis.ai/models/gemini-4-argon",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 112,
    "published_at": "2026-09-30T20:50:28+00:00",
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
    "id": "rss:https://www.theverge.com/tech/1009411/elgin-community-college-flock-safety-cameras",
    "domain": "大厂 AI 动态",
    "title": "A college in Illinois tried to cancel its Flock contact and it refused",
    "url": "https://www.theverge.com/tech/1009411/elgin-community-college-flock-safety-cameras",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T20:06:43+00:00",
    "summary": "In April of 2025, Elgin Community College had six Flock safety cameras installed to \"enhance the safety and security of students.\" But by September of that year, the school's administration grew conce"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1009406/silicon-valley-is-falling-in-line-with-trumps-attempt-to-rename-ai",
    "domain": "大厂 AI 动态",
    "title": "Silicon Valley is falling in line with Trump’s attempt to rename AI",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1009406/silicon-valley-is-falling-in-line-with-trumps-attempt-to-rename-ai",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T18:33:56+00:00",
    "summary": "When President Donald Trump announced his plans to rebrand artificial intelligence as \"super intelligence,\" you'd be forgiven for being skeptical that it would catch on. While most of the broader popu"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1009397/apple-tv-refresh-built-in-mic-remote-speaker",
    "domain": "大厂 AI 动态",
    "title": "The new Apple TV could have a built-in mic and a remote with a speaker",
    "url": "https://www.theverge.com/tech/1009397/apple-tv-refresh-built-in-mic-remote-speaker",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T17:31:07+00:00",
    "summary": "The latest rumors are that the new Apple TV will have a built-in microphone, while the upgraded remote will get a speaker. The mic would let users control the set-top box using Siri without having to "
  },
  {
    "id": "rss:https://www.theverge.com/science/1009379/nasa-800gb-artemis-ii-data",
    "domain": "大厂 AI 动态",
    "title": "NASA dumped over 800GB of Artemis II data online",
    "url": "https://www.theverge.com/science/1009379/nasa-800gb-artemis-ii-data",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T15:34:40+00:00",
    "summary": "If you thought you'd seen all there is to see from the Artemis II mission, you're wrong. This week NASA posted over 800GB worth of science data, images, and videos on the Artemis II: Sights &#38; Soun"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1009346/george-a-romero-season-of-the-witch-feminist-horror-review",
    "domain": "大厂 AI 动态",
    "title": "George A. Romero’s Season of the Witch is a slow-burn feminist occult drama",
    "url": "https://www.theverge.com/entertainment/1009346/george-a-romero-season-of-the-witch-feminist-horror-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T15:15:00+00:00",
    "summary": "George A. Romero is obviously best known as the father of the modern zombie movie. But between inventing the genre with Night of the Living Dead and his outbreak horror, The Crazies, Romero made two m"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1008720/vurt-microdramas-verticals-interview-hilmon-sorey",
    "domain": "大厂 AI 动态",
    "title": "Vurt wants you to look at vertical videos as a genre of their own",
    "url": "https://www.theverge.com/entertainment/1008720/vurt-microdramas-verticals-interview-hilmon-sorey",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T13:00:00+00:00",
    "summary": "From Disney Plus to HBO Max, almost every major established streaming service is experimenting with ways to get into vertical content. It's clear that these companies see video-focused social media pl"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1009317/apple-what-to-expect-welcome-home",
    "domain": "大厂 AI 动态",
    "title": "What to expect from Apple’s ‘Welcome Home’ event",
    "url": "https://www.theverge.com/tech/1009317/apple-what-to-expect-welcome-home",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T13:00:00+00:00",
    "summary": "We are quickly coming up on Apple's \"Welcome Home\" launch event, where we expect a host of smart home-related announcements. We are expecting refreshes to Apple TV and HomePod Mini, as well as a brand"
  },
  {
    "id": "rss:https://www.theverge.com/column/1008432/horror-popular-widows-bay-resident-evil",
    "domain": "大厂 AI 动态",
    "title": "Horror is big business",
    "url": "https://www.theverge.com/column/1008432/horror-popular-widows-bay-resident-evil",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T12:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more on how pervasive horror has become, follow Andrew Webster. The Stepback, arrives in our subscr"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/1008578/leapfrog-leappad-technology-version-history",
    "domain": "大厂 AI 动态",
    "title": "Why the LeapPad couldn&#8217;t survive the iPad",
    "url": "https://www.theverge.com/podcast/1008578/leapfrog-leappad-technology-version-history",
    "source": "Verge Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T12:00:00+00:00",
    "summary": "For multiple years, the hottest toy in the United States was a book. But not just any book: a smart book that could play sounds and respond to taps and help kids learn to read. It was the kind of gadg"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1008484/learning-local-ai-hermes-qwen-model-mac-studio-testing-diary-progress",
    "domain": "大厂 AI 动态",
    "title": "Learning to use local AI is exciting, overwhelming, and frustrating",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1008484/learning-local-ai-hermes-qwen-model-mac-studio-testing-diary-progress",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T11:00:00+00:00",
    "summary": "I'm embarking on a journey I've so far been hesitant to go on: actually using AI on the regular. Giving my most personal data to cloud services has been a major hold up for me, but it's increasingly p"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/11/the-founders-guide-to-techcrunch-disrupt-2026-everything-you-need-to-know/",
    "domain": "大厂 AI 动态",
    "title": "The founder’s guide to TechCrunch Disrupt 2026: Everything you need to know",
    "url": "https://techcrunch.com/2026/10/11/the-founders-guide-to-techcrunch-disrupt-2026-everything-you-need-to-know/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T00:59:01+00:00",
    "summary": "TechCrunch Disrupt 2026 is built around one question: How do you build an enduring company in the AI era? Our programming and speaker lineup reflect that."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/11/will-the-homeview-be-apples-first-smart-home-success/",
    "domain": "大厂 AI 动态",
    "title": "Will the HomeView be Apple’s first smart home success?",
    "url": "https://techcrunch.com/2026/10/11/will-the-homeview-be-apples-first-smart-home-success/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T21:14:40+00:00",
    "summary": "Over the past couple of years, we’ve seen multiple reports that Apple was working on a new smart home product, but now it seems the product has a name and a launch date."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/11/aaron-sorkins-social-reckoning-is-off-to-a-weak-start/",
    "domain": "大厂 AI 动态",
    "title": "Aaron Sorkin’s ‘Social Reckoning’ is off to a weak start",
    "url": "https://techcrunch.com/2026/10/11/aaron-sorkins-social-reckoning-is-off-to-a-weak-start/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T20:51:47+00:00",
    "summary": "What does this mean for a fall full of movies starring villainous tech CEOs?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/11/48-hours-to-techcrunch-disrupt-2026-hear-directly-from-the-people-building-whats-next/",
    "domain": "大厂 AI 动态",
    "title": "48 hours to TechCrunch Disrupt 2026 — hear directly from the people building what’s next",
    "url": "https://techcrunch.com/2026/10/11/48-hours-to-techcrunch-disrupt-2026-hear-directly-from-the-people-building-whats-next/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T19:00:00+00:00",
    "summary": "Less than 48 hours, TechCrunch Disrupt 2026 starts in San Francisco’s Moscone West. Save up to $100 on your pass before prices increase at the door, plus get 50% on a second pass. Or score other deals"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/11/the-investors-guide-to-techcrunch-disrupt-2026-everything-you-need-to-know/",
    "domain": "大厂 AI 动态",
    "title": "The investor’s guide to TechCrunch Disrupt 2026: Everything you need to know",
    "url": "https://techcrunch.com/2026/10/11/the-investors-guide-to-techcrunch-disrupt-2026-everything-you-need-to-know/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T17:53:37+00:00",
    "summary": "Year after year, investors who've explored the Expo Halls, met founders, and learned from peers have proven why you need to be on the ground at Disrupt Oct. 13."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/11/can-the-ai-industry-persuade-data-center-opponents-by-getting-rid-of-ndas/",
    "domain": "大厂 AI 动态",
    "title": "Can the AI industry persuade data center opponents by getting rid of NDAs?",
    "url": "https://techcrunch.com/2026/10/11/can-the-ai-industry-persuade-data-center-opponents-by-getting-rid-of-ndas/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T16:52:33+00:00",
    "summary": "On Equity, we debate the impact of data center moratoriums and whether the AI industry has a communication problem."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/11/techcrunch-mobility-a-roadblock-clears-for-self-driving-trucks/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: A roadblock clears for self-driving trucks",
    "url": "https://techcrunch.com/2026/10/11/techcrunch-mobility-a-roadblock-clears-for-self-driving-trucks/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T16:02:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, the role AI is playing in it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/11/dawn-myers-is-making-it-easier-to-style-detangle-and-care-for-curly-hair/",
    "domain": "大厂 AI 动态",
    "title": "Dawn Myers is making it easier to style, detangle, and care for curly hair",
    "url": "https://techcrunch.com/2026/10/11/dawn-myers-is-making-it-easier-to-style-detangle-and-care-for-curly-hair/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T16:00:00+00:00",
    "summary": "Richualist is one of TechCrunch's Battlefield 200 Companies!"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/11/efferon-wants-to-eradicate-the-devastating-toll-of-pediatric-sepsis/",
    "domain": "大厂 AI 动态",
    "title": "Efferon wants to eradicate the devastating toll of pediatric sepsis",
    "url": "https://techcrunch.com/2026/10/11/efferon-wants-to-eradicate-the-devastating-toll-of-pediatric-sepsis/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T15:00:00+00:00",
    "summary": "This Battlefield 200 startup has developed blood-purification tech to save children"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/11/warner-bros-netflix-paramount-acquisition-timeline-wbd/",
    "domain": "大厂 AI 动态",
    "title": "What to know about the landmark Warner Bros. Discovery sale",
    "url": "https://techcrunch.com/2026/10/11/warner-bros-netflix-paramount-acquisition-timeline-wbd/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T14:15:00+00:00",
    "summary": "Learn more about Paramount's planned acquisition of Warner Bros. Discovery — a historic Hollywood megadeal valued at $111 billion — as it continues to develop."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/11/these-execs-think-voice-ai-hasnt-reached-its-chatgpt-moment-yet/",
    "domain": "大厂 AI 动态",
    "title": "These execs think voice AI hasn’t reached its ChatGPT moment yet",
    "url": "https://techcrunch.com/2026/10/11/these-execs-think-voice-ai-hasnt-reached-its-chatgpt-moment-yet/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T14:00:00+00:00",
    "summary": "Voice AI's often misses important points for its context layer, and causes the whole pipeline to break"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/10/microsofts-satya-nadella-says-ai-models-need-an-emergency-brake/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s Satya Nadella says AI models need an ‘emergency brake’",
    "url": "https://techcrunch.com/2026/10/10/microsofts-satya-nadella-says-ai-models-need-an-emergency-brake/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T21:47:51+00:00",
    "summary": "In a Saturday morning post, Microsoft's CEO wrote that it’s time “to step back and assess the trust architecture” of AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/10/apple-discloses-deal-to-hire-team-and-license-tech-from-personalized-podcast-startup-huxe/",
    "domain": "大厂 AI 动态",
    "title": "Apple discloses deal to hire team and license tech from personalized podcast startup Huxe",
    "url": "https://techcrunch.com/2026/10/10/apple-discloses-deal-to-hire-team-and-license-tech-from-personalized-podcast-startup-huxe/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T19:50:00+00:00",
    "summary": "Is Apple hoping to get into the AI-generated podcast business?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/10/petra-power-looks-to-modernize-energy-for-data-centers-and-defense-vehicles/",
    "domain": "大厂 AI 动态",
    "title": "Petra Power looks to modernize energy for data centers and defense vehicles",
    "url": "https://techcrunch.com/2026/10/10/petra-power-looks-to-modernize-energy-for-data-centers-and-defense-vehicles/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T17:00:00+00:00",
    "summary": "The startup says its fuel cells are super efficient and cut fuel costs during a time when the tech industry can’t get enough electricity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/10/cloudflare-acquires-deno-to-improve-its-workers-programming-model/",
    "domain": "大厂 AI 动态",
    "title": "Cloudflare acquires Deno to improve its Workers programming model",
    "url": "https://techcrunch.com/2026/10/10/cloudflare-acquires-deno-to-improve-its-workers-programming-model/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T16:25:42+00:00",
    "summary": "Cloudflare will use this acquisition to improve its Workers programming model and platform."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/10/3-days-to-disrupt-2026-meet-the-startups-before-they-hit-mainstream/",
    "domain": "大厂 AI 动态",
    "title": "3 days to TechCrunch Disrupt 2026: Meet the startups before they hit mainstream",
    "url": "https://techcrunch.com/2026/10/10/3-days-to-disrupt-2026-meet-the-startups-before-they-hit-mainstream/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T15:00:00+00:00",
    "summary": "TechCrunch Disrupt 2026 takes place October 13-15 in San Francisco. Over 300 startups will show what they’ve built to 10,000 tech leaders. Plus, 250+ speakers are ready to share insights across 200+ s"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/10/all-the-ai-agents-that-can-live-in-your-text-messages/",
    "domain": "大厂 AI 动态",
    "title": "Here are the top AI agents that can live in your text messages",
    "url": "https://techcrunch.com/2026/10/10/all-the-ai-agents-that-can-live-in-your-text-messages/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T14:00:00+00:00",
    "summary": "We created a list of the most notable AI agents that can live in your text messages, from general assistants to agents designed for families, travel, and work."
  },
  {
    "id": "rss:https://stratechery.com/2026/personal-day-4/",
    "domain": "大厂 AI 动态",
    "title": "Personal Day",
    "url": "https://stratechery.com/2026/personal-day-4/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T10:00:00+00:00",
    "summary": "Personal Day — No Update"
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/10/review-4-hour-musk-documentary-feels-like-two-different-films/",
    "domain": "大厂 AI 动态",
    "title": "Review: 4-hour Musk documentary feels like two different films",
    "url": "https://arstechnica.com/culture/2026/10/review-4-hour-musk-documentary-feels-like-two-different-films/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T18:10:54+00:00",
    "summary": "Alex Gibney's provocative film is compelling but overlong, and there's not much new here for Ars readers."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/10/prime-video-unveils-blade-runner-2099-full-trailer-at-nycc/",
    "domain": "大厂 AI 动态",
    "title": "Prime Video unveils Blade Runner 2099 full trailer at NYCC",
    "url": "https://arstechnica.com/culture/2026/10/prime-video-unveils-blade-runner-2099-full-trailer-at-nycc/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T14:50:24+00:00",
    "summary": "Also: new trailer for Godzilla Minus Zero, the sequel to Takashi Yamazaki’s kaiju epic Godzilla Minus One"
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/the-psychedelic-brain-looks-like-chaos-underneath-theres-order/",
    "domain": "大厂 AI 动态",
    "title": "One with the world? A new look at brains transformed by psychedelics.",
    "url": "https://arstechnica.com/science/2026/10/the-psychedelic-brain-looks-like-chaos-underneath-theres-order/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T11:15:35+00:00",
    "summary": "Participants meditated inside an MRI tube, with and without psilocybin."
  },
  {
    "id": "rss:https://www.producthunt.com/products/kudos-smart-wallet",
    "domain": "大厂 AI 动态",
    "title": "Kudos 3.0",
    "url": "https://www.producthunt.com/products/kudos-smart-wallet",
    "source": "Tikue Anazodo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T01:58:06+00:00",
    "summary": "The AI that finds money you're missing and gets it back Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/manifold-mcp",
    "domain": "大厂 AI 动态",
    "title": "Manifold MCP",
    "url": "https://www.producthunt.com/products/manifold-mcp",
    "source": "Jesse Sibley",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T21:01:27+00:00",
    "summary": "SEO, AI answers, social, ads and leads data for your agent Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/dropstone-cli",
    "domain": "大厂 AI 动态",
    "title": "Dropstone CLI",
    "url": "https://www.producthunt.com/products/dropstone-cli",
    "source": "Likhit Kumar V P",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T19:00:02+00:00",
    "summary": "The self-learning coding agent for your terminal Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/excaliclaw",
    "domain": "大厂 AI 动态",
    "title": "ExcaliClaw",
    "url": "https://www.producthunt.com/products/excaliclaw",
    "source": "Mounir Bella",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T21:09:34+00:00",
    "summary": "Hand-drawn diagrams your AI agent can draw with you Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/context-dev",
    "domain": "大厂 AI 动态",
    "title": "Scrape Anything by Context.dev",
    "url": "https://www.producthunt.com/products/context-dev",
    "source": "Ely",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-11T19:23:53+00:00",
    "summary": "Turn any website into clean data with one API call. Discussion | Link"
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
    "id": "hn:50029452",
    "domain": "股票",
    "title": "Data Center Darling Firmus's $30B IPO Dream Crushed in 48 Hours",
    "url": "https://www.bloomberg.com/news/articles/2026-10-09/data-center-darling-s-30-billion-ipo-dream-crushed-in-48-hours",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 53,
    "published_at": "2026-10-10T04:04:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:49930086",
    "domain": "股票",
    "title": "US tells France and Germany to release diesel stocks or face US export ban",
    "url": "https://www.reuters.com/business/energy/us-tells-france-germany-release-diesel-stocks-or-face-us-export-ban-sources-say-2026-10-01/",
    "source": "geox",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-10-02T05:22:20+00:00",
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
    "points": 502,
    "published_at": "2026-10-03T22:07:13+00:00",
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
    "id": "hn:50049302",
    "domain": "金融",
    "title": "Governments are mishandling the affordability crisis",
    "url": "https://www.economist.com/finance-and-economics/2026/10/08/governments-are-mishandling-the-affordability-crisis",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 94,
    "published_at": "2026-10-11T23:40:06+00:00",
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
    "id": "hn:49904408",
    "domain": "金融",
    "title": "Tesla takes on $30B in credit as it approaches unprofitability",
    "url": "https://electrek.co/2026/09/29/tesla-takes-on-30-billion-in-credit-as-it-approaches-unprofitability/",
    "source": "ciconia",
    "platform": "hackernews",
    "points": 161,
    "published_at": "2026-09-30T04:37:37+00:00",
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
    "id": "hn:50023065",
    "domain": "金融",
    "title": "Tesla Rebrands Full Self-Driving as Tesla Assisted Driving in Europe",
    "url": "https://qz.com/tesla-full-self-driving-rebranding-europe-assisted-driving-100926",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 52,
    "published_at": "2026-10-09T16:38:20+00:00",
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
    "id": "rss:https://arxiv.org/abs/2610.12477",
    "domain": "金融",
    "title": "Crisis without Collapse: A Theory of Capitalist Persistence",
    "url": "https://arxiv.org/abs/2610.12477",
    "source": "Murat Ova",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2610.12477v1 Announce Type: new Abstract: The terminal crisis of capitalism has been predicted regularly since 1848. It has not occurred. We treat this 175-year forecasting record as a stylized "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.12587",
    "domain": "金融",
    "title": "On the Optimality of Mental Accounting",
    "url": "https://arxiv.org/abs/2610.12587",
    "source": "Jarrod Burgh, Emerson Melo, Matthew Shum",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2610.12587v1 Announce Type: new Abstract: Mental accounting is usually explained by self-control, and two-stage budgeting by separable preferences. We propose a third explanation based on seller"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.12594",
    "domain": "金融",
    "title": "Restricted Entropic and Quadratic Hedging in the Small-Risk-Aversion Limit",
    "url": "https://arxiv.org/abs/2610.12594",
    "source": "Jonas Hanetho",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2610.12594v1 Announce Type: new Abstract: In incomplete markets, contingent claims cannot in general be replicated exactly, and hedging must therefore be formulated as an optimization problem ov"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.12718",
    "domain": "金融",
    "title": "A Distributional Framework for Behavioral Characterization and Risk Management of Large Language Models",
    "url": "https://arxiv.org/abs/2610.12718",
    "source": "David Garc\\'ia-Lorite, Raul Merino",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2610.12718v1 Announce Type: new Abstract: Large language models are stochastic by nature. Repeated executions under the same experimental conditions may produce different responses. We propose a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.12875",
    "domain": "金融",
    "title": "The Financing of Debt Relief: Intermediary Liquidity and the Value of Borrower Information",
    "url": "https://arxiv.org/abs/2610.12875",
    "source": "Arka P. Bandyopadhyay",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2610.12875v1 Announce Type: new Abstract: I study how intermediary liquidity affects mortgage resolution using 1.9 million Ginnie Mae buyout options from 2019 to 2022. When funding markets froze"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.13044",
    "domain": "金融",
    "title": "FOMO: FLEX Options and Market Outcomes",
    "url": "https://arxiv.org/abs/2610.13044",
    "source": "Shivesh Prakash, Frank Ferstler, Nicholas Pezolano",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2610.13044v1 Announce Type: new Abstract: FLEX options are customized exchange-traded contracts allowing participants to choose nonstandard strikes, expirations, exercise styles, and settlement "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.13126",
    "domain": "金融",
    "title": "MLP-Initialized Reinforcement Learning for Exit Timing in SPX Short-Straddle Portfolios",
    "url": "https://arxiv.org/abs/2610.13126",
    "source": "Jianning Wang, Robert \\'Slepaczuk, Pawe{\\l} Sakowski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2610.13126v1 Announce Type: new Abstract: This paper studies exit timing for SPX short-straddle portfolios using a two-stage supervised and reinforcement-learning framework. Historical episodes "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.13162",
    "domain": "金融",
    "title": "Entropy Regularization under No-Shorting: Structure Preservation and Convexity in Dynamic Mean-Variance Portfolio Selection",
    "url": "https://arxiv.org/abs/2610.13162",
    "source": "Xinagyu Cui, Xun Li, Ziyan Li, Yun Shi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2610.13162v1 Announce Type: new Abstract: This paper studies entropy regularization for the discrete-time dynamic mean--variance portfolio problem with no-shorting constraints. In the unconstrai"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.13199",
    "domain": "金融",
    "title": "Enhancing credit risk scorecards with transactional-based behavioural features",
    "url": "https://arxiv.org/abs/2610.13199",
    "source": "Dian Prinsloo, Tanja Verster, Neill Smit",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2610.13199v1 Announce Type: new Abstract: Background: Credit risk modelling is fundamental in financial institutions, typically using credit history, repayment behaviour, income, and outstanding"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.13543",
    "domain": "金融",
    "title": "Three options are roughly enough - Variance-optimal semi-static hedging in the rough Heston model",
    "url": "https://arxiv.org/abs/2610.13543",
    "source": "Paolo Di Tella, Martin Keller-Ressel, Beatrice Ongarato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2610.13543v1 Announce Type: new Abstract: This paper studies semi-static variance-optimal hedging of variance swaps in the rough Heston model under a risk-neutral measure. We combine dynamic tra"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.13785",
    "domain": "金融",
    "title": "Linear Demand Systems are Consistent with Discrete Choice",
    "url": "https://arxiv.org/abs/2610.13785",
    "source": "Afonso Rodrigues",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2610.13785v1 Announce Type: new Abstract: Aggregate linear demand systems can be micro-founded by a population of heterogeneous consumers making discrete choices. They can also be extended to in"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.13446",
    "domain": "金融",
    "title": "Realized Tail-Risk Conditional Autoregressive Expectile Models: Accurate and Stable Forecasting Performance",
    "url": "https://arxiv.org/abs/2610.13446",
    "source": "Keisuke Sasaki, Yasuhiro Omori",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2610.13446v1 Announce Type: cross Abstract: A realized tail-risk conditional autoregressive expectile (RTCARE) model is proposed for joint forecasting of value-at-risk (VaR) and expected shortfa"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.13574",
    "domain": "金融",
    "title": "$L_0$ Feature Selection via Monte Carlo Tree Search in High-Dimensional Financial Regression",
    "url": "https://arxiv.org/abs/2610.13574",
    "source": "Cameron Mouangue, Tristan Cazenave",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2610.13574v1 Announce Type: cross Abstract: Feature selection is a central problem in high-dimensional financial regression, where large numbers of engineered variables and strong correlations a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.13606",
    "domain": "金融",
    "title": "CorrFlow: Exact and Permutation-Equivariant Flow Matching on the Correlation Elliptope",
    "url": "https://arxiv.org/abs/2610.13606",
    "source": "Gautier Marti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2610.13606v1 Announce Type: cross Abstract: Correlation matrices combine nonlinear positive-definiteness constraints with a simultaneous row-column permutation symmetry. Their generation therefo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2109.14360",
    "domain": "金融",
    "title": "Systemic risk in interbank networks: disentangling balance sheets and network effects",
    "url": "https://arxiv.org/abs/2109.14360",
    "source": "Alessandro Ferracci, Giulio Cimini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2109.14360v3 Announce Type: replace Abstract: We study how the level of systemic risk empirically observed in an interbank network differs from the expected risk implied by the balance sheets co"
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.12848",
    "domain": "金融",
    "title": "Two-Sided Market Power in Firm-to-Firm Trade",
    "url": "https://arxiv.org/abs/2507.12848",
    "source": "Alviarez Vanessa, Fioretti Michele, Kikkawa Ken, Morlacco Monica",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2507.12848v3 Announce Type: replace Abstract: We develop and estimate a model of two-sided market power to study tariff pass-through in firm-to-firm trade. A tariff moves the negotiated price th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.00212",
    "domain": "金融",
    "title": "Economic Impacts of Climate Change in the United States: Integrating and Harmonizing Evidence from Recent Studies",
    "url": "https://arxiv.org/abs/2509.00212",
    "source": "Elizabeth Kopits, Daniel Kraynak, Bryan Parthum, Lisa Rennels, David Smith, Elizabeth Spink, Joseph Perla, Nshan Burns",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2509.00212v2 Announce Type: replace Abstract: This paper synthesizes evidence on climate change impacts specific to U.S. populations. We develop an apples-to-apples comparison of econometric stu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.06670",
    "domain": "金融",
    "title": "Stochastic Policy Gradient Methods in the Uncertain Volatility Model",
    "url": "https://arxiv.org/abs/2605.06670",
    "source": "Lokman A Abbas-Turki (LPSM), Jean-Fran\\c{c}ois Chassagneux (ENSAE Paris), Jean-Philippe Lemor (LPSM), Gr\\'egoire Loeper (LPSM), Simon Sananes (LPSM)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2605.06670v3 Announce Type: replace Abstract: The multidimensional Uncertain Volatility Model leads to robust option pricing problems under joint volatility and correlation uncertainty. Their nu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.22892",
    "domain": "金融",
    "title": "Is TabPFN the Silver Bullet for Insurance Pricing?",
    "url": "https://arxiv.org/abs/2605.22892",
    "source": "Bruno Deprez, Wouter Verbeke, Tim Verdonck",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2605.22892v3 Announce Type: replace Abstract: Modelling claim frequency and severity for non-life insurance pricing predominantly relies on generalised linear models (GLMs), with gradient-booste"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.10606",
    "domain": "金融",
    "title": "The Gendered Impacts of Perceived Skin Tone: Evidence from African American Siblings in 1870-1940",
    "url": "https://arxiv.org/abs/2610.10606",
    "source": "Ran Abramitzky, Jacob Conway, Roy Mill, Luke C. D. Stein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2610.10606v2 Announce Type: replace Abstract: We study differences in economic outcomes by perceived skin tone among African Americans using full-count U.S. decennial census data from the late-1"
  },
  {
    "id": "rss:https://arxiv.org/abs/2503.09637",
    "domain": "金融",
    "title": "Complementarity, Augmentation, or Substitutivity? The Impact of Generative Artificial Intelligence on the U.S. Federal Workforce",
    "url": "https://arxiv.org/abs/2503.09637",
    "source": "William G. Resh, Yi Ming, Xinyao Xia, Michael Overton, Gul Nisa Gurbuz, Brandon De Bruhl",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2503.09637v2 Announce Type: replace-cross Abstract: This study applies a multi-stage Retrieval-Augmented Generation system, which grounds large language model assessments in curated evidence, to"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.13732",
    "domain": "金融",
    "title": "On the First Hitting Time Problems for Diffusion Processes: Local Time-Space Approach",
    "url": "https://arxiv.org/abs/2608.13732",
    "source": "Jerome Detemple, Yerkin Kitapbayev, Danila Shabalin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-12T04:00:00+00:00",
    "summary": "arXiv:2608.13732v3 Announce Type: replace-cross Abstract: Using the local time-space calculus of Peskir (2005) and the method developed in Mijatovic (2010), we derive a new integral representation for"
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
    "id": "hn:49908455",
    "domain": "金融",
    "title": "European Network for Payments – An EU Alternative to Visa/Mastercard",
    "url": "https://www.reuters.com/business/finance/european-payments-groups-join-forces-lessen-us-reliance-2026-09-30/",
    "source": "monegator",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-09-30T13:11:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:49769668",
    "domain": "金融",
    "title": "OpenAI and Anthropic oversold AI security breaches",
    "url": "https://nypost.com/2026/09/19/us-news/openai-anthropic-oversold-security-breaches-to-pressure-feds-into-protecting-turf-insiders/",
    "source": "hei-lima",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-09-19T19:59:28+00:00",
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
    "id": "hn:49924299",
    "domain": "金融",
    "title": "Sony released the first CD audio player on this day in 1982",
    "url": "https://www.tomshardware.com/pc-components/storage/sony-released-the-first-cd-audio-player-on-this-day-in-1982-player-cost-usd3-700-when-adjusted-for-inflation-but-it-would-be-another-decade-before-the-cd-rom-driven-multimedia-pc-era-began",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-01T17:07:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49828019",
    "domain": "金融",
    "title": "Show HN: Trader News – Hacker News for Finance",
    "url": "https://news.ycombinator.com/item?id=49828019",
    "source": "FailMore",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-09-24T08:54:57+00:00",
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
  }
]
```
