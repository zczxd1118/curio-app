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

- 今日日期：`2026-10-20`
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
  "date": "2026-10-20",
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
    "points": 2122547,
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
    "points": 1998943,
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
    "points": 1416884,
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
    "points": 1366555,
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
    "points": 902087,
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
    "points": 864012,
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
    "points": 722871,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 562697,
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
    "points": 425356,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 358225,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 356835,
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
    "points": 327045,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1WWYE6LEzx",
    "domain": "AI",
    "title": "黑马程序员2026全网最夯VibeCoding零基础入门到实战项目开发全套视频教程，AI辅助编程从入门到实战，涵盖Claude Code、DeepSeek等内容",
    "url": "http://www.bilibili.com/video/av117251667724450",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 318260,
    "published_at": "2026-09-14T01:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n2026黑马程序员AI智能应用开发学习路线图\nhttps://www.bilibili.com/opus/1156896913511940102\n如何下载资料\nhttps://www.bilibili.com/read/cv7881295/\n学习交流社区腾讯鹅625260577告别孤单，共同进步\n\n【AI智能应用开发学习路线图】（依次向下顺序学习即可）\nJa"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 310260,
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
    "points": 281836,
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
    "points": 210787,
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
    "points": 184203,
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
    "points": 162998,
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
    "points": 161305,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 103312,
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
    "points": 94090,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 83409,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 76694,
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
    "points": 56183,
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
    "points": 49436,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 40731,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1f3J96AETa",
    "domain": "AI",
    "title": "Claude code四个阶段",
    "url": "http://www.bilibili.com/video/av117449504595834",
    "source": "程序员牛牛学长",
    "platform": "bilibili",
    "points": 36981,
    "published_at": "2026-10-19T10:55:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29849,
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
    "points": 29007,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV126pk6sETS",
    "domain": "AI",
    "title": "连 json都不会，进了福布斯团队。面试的时候才知道vibe coding是什么，两天后他给我发了offer。",
    "url": "http://www.bilibili.com/video/av117436686795057",
    "source": "揽星Celeste",
    "platform": "bilibili",
    "points": 28558,
    "published_at": "2026-10-14T01:35:05+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 24944,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22817,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 22797,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 22638,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV188UHYkEdg",
    "domain": "AI",
    "title": "Cursor / Windsurf + Android Studio 高效AI编程：零基础也能开发安卓应用",
    "url": "http://www.bilibili.com/video/av113502647750313",
    "source": "kate人不错",
    "platform": "bilibili",
    "points": 21168,
    "published_at": "2024-11-18T07:04:36+00:00",
    "summary": "欢迎关注我的知识星球：https://t.zsxq.com/FF0He\n\n我会分享最新AI资讯、源代码、回答你的提问。\n\n视频亮点：\n\n双工具对比：解析 Cursor 和 Windsurf 各自优势\n实战案例：从五子棋到卡路里计算AI应用的完整开发过程\n专业部署：Android Studio 配置与构建技巧\n\n时间戳：\n\n0:00 - 引言\n\n0:26 - 我开发的应用演示\n\n2:33 - Rea"
  },
  {
    "id": "bvid:BV15mnJ6YELj",
    "domain": "AI",
    "title": "DSH搭AI工作台，养成赛博“自己”！",
    "url": "http://www.bilibili.com/video/av117466852495477",
    "source": "马上淋雨",
    "platform": "bilibili",
    "points": 17559,
    "published_at": "2026-10-19T09:35:56+00:00",
    "summary": "自己基于dsh搭建工作台的思路焚决，随着ai越来越强它一定可以变成赛博“自己”，内容是思路，方法直接找ai就可以！"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 17628,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1HhGo6aEvE",
    "domain": "AI",
    "title": "本地大模型也能联网搜索！LM Studio × MCP 接入教程",
    "url": "http://www.bilibili.com/video/av116635490911881",
    "source": "aopstudio",
    "platform": "bilibili",
    "points": 15439,
    "published_at": "2026-05-25T13:41:46+00:00",
    "summary": "本视频演示如何为 LM Studio 接入 MCP 联网搜索服务，让本地运行的大模型具备实时搜索网络的能力。\nMCP（Model Context Protocol）是 Anthropic 推出的开放协议，允许模型通过标准化接口调用外部工具。本次接入的搜索服务来自 MCPWorld，底层通过 npx 调用，无需额外部署服务端，配置完成后即可在 LM Studio 的对话界面中直接发起联网搜索。\n本视"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 12831,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV17NJS6QEfE",
    "domain": "AI",
    "title": "Vibe Coding 有哪些高效的做法习惯？",
    "url": "http://www.bilibili.com/video/av117447894045979",
    "source": "AAA话题批发",
    "platform": "bilibili",
    "points": 12578,
    "published_at": "2026-10-16T01:30:00+00:00",
    "summary": "随着 AI 编程 Agent 普及，Vibe Coding 已经成为很多开发者的日常工作方式。不少人把精力耗费在打磨各种花式提示词上，但实际项目中经常遇到 Token 消耗爆炸、Agent 找不准代码、结果不稳定、大量人工兜底的问题。这篇文章结合多项行业实验与大厂内部项目实践，跳出提示词技巧，分享 Vibe Coding 真正高效的工作习惯与项目配置思路。\n文章开篇借助真实工程实验案例，展示合理拆"
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 11359,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1ovuC66EuG",
    "domain": "AI",
    "title": "老 k 带你手搓 AI 交易智能体",
    "url": "http://www.bilibili.com/video/av117080372351441",
    "source": "老K聊交易系统",
    "platform": "bilibili",
    "points": 10409,
    "published_at": "2026-08-12T03:43:43+00:00",
    "summary": "这是一套使用 Codex开发 AI 交易智能体的系列课程，内容包括：智能体功能介绍到软件安装配置，再到开发自动化交易工具，策略优化与训练，实现交易 skill 稳定自动运行。\n课程资料包下载：www.jujijiaoyi.com"
  },
  {
    "id": "bvid:BV1bBHm6MEG5",
    "domain": "AI",
    "title": "这绝对是b站讲的最好的Claude Code全套实战教程，手把手带你搞定国内环境安装配置，全程干货无废话！AI大模型/MCP/Skill/智能体/Agent",
    "url": "http://www.bilibili.com/video/av117402847155229",
    "source": "大模型饼饼",
    "platform": "bilibili",
    "points": 10233,
    "published_at": "2026-10-08T02:13:21+00:00",
    "summary": "这绝对是B站讲得最好的Claude Code全套实战教程！手把手带你搞定国内环境安装配置、基础操作、高阶实战技巧，课程不堆砌冗余理论，聚焦真实开发场景，带你吃透Claude Code核心能力，打通MCP、Skill与Agent智能体联动开发。不管你是想提升日常编码效率，还是入门AI智能体开发，这套教程都非常适合你，全程干货无废话！"
  },
  {
    "id": "bvid:BV11LWw6VEHW",
    "domain": "AI",
    "title": "Agent-native 开发 [08-Raw/26生成式软件工程/NJU]",
    "url": "http://www.bilibili.com/video/av117432811260250",
    "source": "绿导师原谅你了",
    "platform": "bilibili",
    "points": 10115,
    "published_at": "2026-10-13T09:10:24+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 8224,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "bvid:BV1gJJB6kERk",
    "domain": "AI",
    "title": "【实操】claude稳定不封的方法",
    "url": "http://www.bilibili.com/video/av117457104672336",
    "source": "程序员大龙虾",
    "platform": "bilibili",
    "points": 8001,
    "published_at": "2026-10-17T16:10:46+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1pRDUBqEbS",
    "domain": "AI",
    "title": "Claude Code Worktree: 一个人干五个人的活",
    "url": "http://www.bilibili.com/video/av116390241502827",
    "source": "全栈观察员",
    "platform": "bilibili",
    "points": 7633,
    "published_at": "2026-04-12T06:18:06+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1b4Hr6HE53",
    "domain": "AI",
    "title": "【卫戍协议】一键部署服务器&amp;各种方法联机教程 by Ausevay﻿【功能演示/部署教学】",
    "url": "http://www.bilibili.com/video/av117381070329620",
    "source": "Starst星尘子",
    "platform": "bilibili",
    "points": 7050,
    "published_at": "2026-10-04T05:50:25+00:00",
    "summary": "项目名称：卫戍协议：盟约 · 服务器启动器（https://github.com/Starst796/Stronghold-Protocol-Server-Launcher）\n项目介绍：为 sganggs/Stronghold-Protocol 做的跨平台一键服务器启动器。\n服务器源：https://github.com/sganggs/Stronghold-Protocol\n\n如何获取：\n百度网"
  },
  {
    "id": "bvid:BV1YmJ36BEsf",
    "domain": "AI",
    "title": "告别手动，AI代劳：Claude Code + MCP 实现ABAQUS全自动建模",
    "url": "http://www.bilibili.com/video/av116754189653546",
    "source": "CAE老白",
    "platform": "bilibili",
    "points": 6916,
    "published_at": "2026-06-15T12:47:08+00:00",
    "summary": "用Claude Code + MCP给ABAQUS装上“AI大脑”：从自然语言到仿真模型的全自动之路"
  },
  {
    "id": "bvid:BV1UaYK6nEjP",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av117244419903051",
    "source": "茶子兀",
    "platform": "bilibili",
    "points": 6840,
    "published_at": "2026-09-10T02:39:36+00:00",
    "summary": ""
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
    "id": "hn:50008187",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI annualised revenues $20B less than previously signalled",
    "url": "https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 434,
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
    "points": 180,
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
    "id": "rss:https://www.eetimes.com/building-physical-ai-systems-that-can-work-in-the-real-world/",
    "domain": "AI 算力 / 半导体",
    "title": "Building Physical AI Systems That Can Work in the Real World",
    "url": "https://www.eetimes.com/building-physical-ai-systems-that-can-work-in-the-real-world/",
    "source": "Dermot O’Driscoll",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T08:00:00+00:00",
    "summary": "Build scalable physical AI by balancing compute, power, safety, and cost—see why system architecture outperforms raw model size. The post Building Physical AI Systems That Can Work in the Real World a"
  },
  {
    "id": "rss:https://www.eetimes.com/precision-timing-special-report/",
    "domain": "AI 算力 / 半导体",
    "title": "Precision Timing Special Report",
    "url": "https://www.eetimes.com/precision-timing-special-report/",
    "source": "SiTime, Micro Crystal, Abracon, ECS Inc. International, Kyocera AVX",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T20:30:16+00:00",
    "summary": "Choose timing with confidence: compare crystals, oscillators, RTCs, MEMS, and atomic references for reliable designs—download the guide. The post Precision Timing Special Report appeared first on EE T"
  },
  {
    "id": "rss:https://www.eetimes.com/video-interview-applied-materials-ceo-on-the-economics-behind-its-5b-epic-bet/",
    "domain": "AI 算力 / 半导体",
    "title": "Video Interview: Applied Materials CEO on the Economics Behind Its $5B EPIC Bet",
    "url": "https://www.eetimes.com/video-interview-applied-materials-ceo-on-the-economics-behind-its-5b-epic-bet/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T20:00:00+00:00",
    "summary": "Following the unveiling of its EPIC Center, Applied Materials revealed strong financial projections. We look at how it all ties together and feature a new video interview with CEO Gary Dickerson. The "
  },
  {
    "id": "rss:https://www.eetimes.com/qualcomm-wins-key-claims-against-arm-but-damages-total-just-2/",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm Wins Key Claims Against Arm, but Damages Total Just $2",
    "url": "https://www.eetimes.com/qualcomm-wins-key-claims-against-arm-but-damages-total-just-2/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T16:13:37+00:00",
    "summary": "The verdict is the latest chapter in a four-year IP dispute between the two chip giants, safeguarding Qualcomm's custom processors while placing financial pressure on Arm. The post Qualcomm Wins Key C"
  },
  {
    "id": "rss:https://www.eetimes.com/from-macro-to-micro-and-back/",
    "domain": "AI 算力 / 半导体",
    "title": "From Macro to Micro, and Back",
    "url": "https://www.eetimes.com/from-macro-to-micro-and-back/",
    "source": "Moshe Zalcberg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T08:19:07+00:00",
    "summary": "This year’s Nobel prizes explained large systems through their smallest parts. What can chip design learn from them, and can AI help us design in the other direction too? The post From Macro to Micro,"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/vbios-on-rtx-cards-can-be-modified-without-flashing-thanks-to-a-solo-developers-project-provides-a-ui-for-quick-vbios-configuration",
    "domain": "AI 算力 / 半导体",
    "title": "You can now modify the vBIOS on Nvidia gaming GPUs without flashing thanks to a solo developer’s project",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/vbios-on-rtx-cards-can-be-modified-without-flashing-thanks-to-a-solo-developers-project-provides-a-ui-for-quick-vbios-configuration",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T16:30:39+00:00",
    "summary": "Flashing the VBIOS is risky and can brick a GPU, but this VBIOS configurator uses an Nvidia register key to override VBIOS settings without flashing."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/a-chinese-hacker-used-ai-agents-to-break-into-more-than-100-company-websites-deere-and-sharkninja-among-websites-hit-by-open-source-ai-powered-problem-solving-platform-demo",
    "domain": "AI 算力 / 半导体",
    "title": "A Chinese hacker used AI agents to break into more than 100 company websites",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/a-chinese-hacker-used-ai-agents-to-break-into-more-than-100-company-websites-deere-and-sharkninja-among-websites-hit-by-open-source-ai-powered-problem-solving-platform-demo",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T15:36:50+00:00",
    "summary": "A Chinese hacker reportedly used a fleet of AI agents to break into more than 100 company websites, including farm equipment maker Deers and appliance outfit SharkNinja."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/french-rioters-ransack-esports-team-premises-and-are-seen-looting-ram-sticks-from-pcs-team-vitalitys-v-hive-paris-hq-was-wrecked-during-unrest",
    "domain": "AI 算力 / 半导体",
    "title": "French rioters ransack eSports team premises and are seen looting RAM sticks from PCs",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/french-rioters-ransack-esports-team-premises-and-are-seen-looting-ram-sticks-from-pcs-team-vitalitys-v-hive-paris-hq-was-wrecked-during-unrest",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T13:32:42+00:00",
    "summary": "Leading French eSports club Team Vitality has confirmed that its Paris HQ has been smashed up, with trophies, computer equipment, and more looted over the weekend."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/norwegian-undersea-cable-builder-pitches-2-800-mile-transatlantic-data-link-between-canada-and-europe-to-bypass-the-us-canadian-majority-partner-sought-to-help-fund-and-build-new-usd620-million-fiber-connection-to-reduce-reliance-on-american-routes",
    "domain": "AI 算力 / 半导体",
    "title": "Norwegian undersea cable builder pitches 2,800-mile transatlantic data link between Canada and Europe to bypass the US",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/norwegian-undersea-cable-builder-pitches-2-800-mile-transatlantic-data-link-between-canada-and-europe-to-bypass-the-us-canadian-majority-partner-sought-to-help-fund-and-build-new-usd620-million-fiber-connection-to-reduce-reliance-on-american-routes",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T12:26:15+00:00",
    "summary": "Norway's Bulk Infrastructure Group AS is looking for a partner to build transatlantic undersea cabling to connect Canada with Europe to bypass the United States."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/3d-scanning/creality-pika-3d-scanner-review",
    "domain": "AI 算力 / 半导体",
    "title": "Creality Pika 3D scanner review: Good things come in small packages",
    "url": "https://www.tomshardware.com/3d-printing/3d-scanning/creality-pika-3d-scanner-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T12:05:00+00:00",
    "summary": "The tiny, portable Creality Pika is a joy to use, especially if you have a high end computer or a recent model phone to pair it with."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptomining/claude-code-ai-agent-caught-a-crypto-miner-hiding-on-a-developers-overheating-mac-xmrig-task-was-hogging-about-1175-percent-cpu-roughly-12-cores-pushing-temps-to-112-degrees",
    "domain": "AI 算力 / 半导体",
    "title": "Claude Code AI agent caught a crypto miner hiding on a developer’s overheating Mac",
    "url": "https://www.tomshardware.com/tech-industry/cryptomining/claude-code-ai-agent-caught-a-crypto-miner-hiding-on-a-developers-overheating-mac-xmrig-task-was-hogging-about-1175-percent-cpu-roughly-12-cores-pushing-temps-to-112-degrees",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T11:36:20+00:00",
    "summary": "A developer using Claude Code to help build a temperature monitor app was warned by the coding agent about a hidden crypto miner running on their system."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/arm-claims-agi-cpu-delivers-double-the-performance-per-rack-of-amd-epyc-9755-in-independent-analysis-new-cpu-evaluation-methodology-developed-by-arm-evaluates-agentic-ai-performance-across-seven-workloads",
    "domain": "AI 算力 / 半导体",
    "title": "Arm says its AGI CPU delivers nearly 2X the performance per rack of AMD EPYC 9755 in new agentic AI CPU tests",
    "url": "https://www.tomshardware.com/pc-components/cpus/arm-claims-agi-cpu-delivers-double-the-performance-per-rack-of-amd-epyc-9755-in-independent-analysis-new-cpu-evaluation-methodology-developed-by-arm-evaluates-agentic-ai-performance-across-seven-workloads",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T11:00:00+00:00",
    "summary": "Arm claims its AGI CPU delivers nearly 2X the modeled rack performance of AMD’s EPYC 9755 across seven agentic AI workloads, using a new evaluation methodology developed with Fujitsu, Meta, and OpenAI"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/score-a-budget-gaming-monitor-with-a-blistering-200hz-refresh-rate-for-just-usd79-25-inch-ultragear-g5-reduced-by-a-staggering-47-percent-in-walmart-discount",
    "domain": "AI 算力 / 半导体",
    "title": "Score a budget gaming monitor with a blistering 200Hz refresh rate for just $79",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/score-a-budget-gaming-monitor-with-a-blistering-200hz-refresh-rate-for-just-usd79-25-inch-ultragear-g5-reduced-by-a-staggering-47-percent-in-walmart-discount",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T10:53:38+00:00",
    "summary": "With 47% off the list price, LG's UltrGear G5 gaming monitor is the perfect impulse purchase at just $79. An IPS panel, a 200Hz refresh rate, and FHD resolution for an unbelievable price."
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/engineer-builds-tiny-3d-printed-single-motor-drone-in-their-bedroom-45-degree-hinged-rotor-and-sub-0-2ms-firmware-control-pitch-and-roll",
    "domain": "AI 算力 / 半导体",
    "title": "Engineer builds tiny 3D-printed single-motor drone in their bedroom",
    "url": "https://www.tomshardware.com/maker-stem/engineer-builds-tiny-3d-printed-single-motor-drone-in-their-bedroom-45-degree-hinged-rotor-and-sub-0-2ms-firmware-control-pitch-and-roll",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T10:30:00+00:00",
    "summary": "Joshua Bird designed, built, and tested this drone in their home, even resorting to building their own high-speed camera to check their build while spinning at a high speed."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd500-on-this-1440p-gaming-pc-with-an-rtx-5070-now-under-usd1-800-abs-flux-ii-aqua-rig-ships-with-a-20-core-intel-cpu-32gb-ddr5-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save $500 on this 1440p gaming PC with an RTX 5070, now under $1,800",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd500-on-this-1440p-gaming-pc-with-an-rtx-5070-now-under-usd1-800-abs-flux-ii-aqua-rig-ships-with-a-20-core-intel-cpu-32gb-ddr5-and-a-1tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T10:01:38+00:00",
    "summary": "This Newegg deal on an ABS Flux II Aqua gaming PC gives you a machine ready for 1440p and 4K gameplay for $1,799.99. This pre-built comes with a 20-core Intel Core i7-14700F CPU, an Nvidia GeForce RTX"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/space/russian-military-satellite-closes-from-200-miles-to-3-miles-of-us-radar-satellite-aiding-ukraine-astronomer-says-it-may-be-the-first-unapproved-rendezvous-in-low-earth-orbit",
    "domain": "AI 算力 / 半导体",
    "title": "Russian military satellite closes from 200 miles to 3 miles of US radar craft aiding Ukraine",
    "url": "https://www.tomshardware.com/tech-industry/space/russian-military-satellite-closes-from-200-miles-to-3-miles-of-us-radar-satellite-aiding-ukraine-astronomer-says-it-may-be-the-first-unapproved-rendezvous-in-low-earth-orbit",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T10:00:00+00:00",
    "summary": "Russia’s Cosmos 2612 moved from more than 200 miles to about three miles from ICEYE-X36, a U.S.-owned radar satellite."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amd-cards-now-run-all-dlss-features-thanks-to-one-developers-project-plans-to-match-native-nvidia-gpu-performance",
    "domain": "AI 算力 / 半导体",
    "title": "Modder brings full Nvidia DLSS 5 suite to three generations of AMD gaming GPUs",
    "url": "https://www.tomshardware.com/pc-components/gpus/amd-cards-now-run-all-dlss-features-thanks-to-one-developers-project-plans-to-match-native-nvidia-gpu-performance",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T16:03:01+00:00",
    "summary": "Radeon GPUs get the full DLSS experience as solo project ports all the DLSS features for RDNA2-4 GPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/anycubics-award-winning-3d-printer-hits-all-time-low-pricing-kobra-x-is-an-excellent-entry-level-four-color-printer-thats-now-just-usd299-99-for-amazon-prime-members",
    "domain": "AI 算力 / 半导体",
    "title": "Anycubic's award-winning 3D printer hits all-time low pricing",
    "url": "https://www.tomshardware.com/3d-printing/anycubics-award-winning-3d-printer-hits-all-time-low-pricing-kobra-x-is-an-excellent-entry-level-four-color-printer-thats-now-just-usd299-99-for-amazon-prime-members",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T15:24:22+00:00",
    "summary": "The Editor's Choice Anycubic Kobra X Multicolor 3D Printer is at the lowest price we've ever seen."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/f-22-raptor-pilot-successfully-demonstrates-command-of-wingman-fighter-drone-in-simulated-combat-anduril-yfq-44a-fury-test-advances-usafs-program-to-integrate-uncrewed-aircraft-into-fighter-squadrons",
    "domain": "AI 算力 / 半导体",
    "title": "F-22 Raptor pilot successfully demonstrates command of 'wingman' fighter drone in simulated combat",
    "url": "https://www.tomshardware.com/tech-industry/drones/f-22-raptor-pilot-successfully-demonstrates-command-of-wingman-fighter-drone-in-simulated-combat-anduril-yfq-44a-fury-test-advances-usafs-program-to-integrate-uncrewed-aircraft-into-fighter-squadrons",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T15:02:19+00:00",
    "summary": "The USAF's latest test proves that an F-22 Raptor can command a YFQ-44A Fury drone in combat conditions."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/overclocking/cinebench-world-record-that-stood-for-12-years-gets-toppled-oc-expert-scores-10-8cb-in-cinebench-r11-5-using-an-intel-core-i5-4670k-at-6-3-ghz",
    "domain": "AI 算力 / 半导体",
    "title": "Cinebench world record that stood for 12 years gets toppled",
    "url": "https://www.tomshardware.com/pc-components/overclocking/cinebench-world-record-that-stood-for-12-years-gets-toppled-oc-expert-scores-10-8cb-in-cinebench-r11-5-using-an-intel-core-i5-4670k-at-6-3-ghz",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T14:02:53+00:00",
    "summary": "You don’t need the latest and greatest PC hardware to have fun or even break overclocking world records, as Luumi shows with an ancient Haswell system."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/asus-rog-strix-xg27aqgnv-27-inch-g-sync-pulsar-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Strix XG27AQGNV 27-inch G-Sync Pulsar gaming monitor review: Super smooth with unprecedented control",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/asus-rog-strix-xg27aqgnv-27-inch-g-sync-pulsar-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T13:25:00+00:00",
    "summary": "Asus delivers its take on G-Sync Pulsar with the ROG Strix XG27AQGNV. This 27-inch IPS panel sports smooth motion with 360 Hz, QHD resolution, HDR and wide gamut color."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090-shipment-worth-usd470-000-goes-missing-in-brazilian-airport-two-pallets-disappear-distributor-seeks-explanations-but-met-with-zero-answers",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX 5090 shipment worth $470,000 goes missing in Brazilian airport",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090-shipment-worth-usd470-000-goes-missing-in-brazilian-airport-two-pallets-disappear-distributor-seeks-explanations-but-met-with-zero-answers",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T13:24:23+00:00",
    "summary": "Brazilian electronics and IT distributor Oderço claims that two pallets of Zotac RTX 5090 GPUs have arrived at the airport but has since completely disappeared."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/chip-fab-engineering-game-goes-viral-in-taiwan-realistic-and-stressful-simulation-is-basically-a-horror-game-say-some-players",
    "domain": "AI 算力 / 半导体",
    "title": "Web-based chip fab engineering game goes viral in Taiwan",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/chip-fab-engineering-game-goes-viral-in-taiwan-realistic-and-stressful-simulation-is-basically-a-horror-game-say-some-players",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T12:50:33+00:00",
    "summary": "A new 3D web game where you live 'A Day in the Life of a Semiconductor Wafer Factory Worker' has gone viral in Taiwan, where it was developed."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/modders-used-the-official-dlss-5-release-on-unsupported-games-and-are-seeing-up-to-90-percent-better-performance-than-the-leaked-dlss-5-nvidia-says-new-nr-model-uses-20-percent-less-vram-and-processes-neural-workloads-up-to-2x-faster",
    "domain": "AI 算力 / 半导体",
    "title": "Official DLSS 5 running on unsupported games delivers up to 90% better performance than the leaked version",
    "url": "https://www.tomshardware.com/pc-components/gpus/modders-used-the-official-dlss-5-release-on-unsupported-games-and-are-seeing-up-to-90-percent-better-performance-than-the-leaked-dlss-5-nvidia-says-new-nr-model-uses-20-percent-less-vram-and-processes-neural-workloads-up-to-2x-faster",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T12:45:00+00:00",
    "summary": "Nvidia's latest DLSS Neural Renderer, extracted from NBA 2K27 (again), is being tested on unsupported games and shows up to a 90% performance gain over the previous NR model."
  },
  {
    "id": "rss:https://www.tomshardware.com/virtual-reality/mit-engineers-build-soft-3d-shape-sensing-skin-for-gaming-and-vr-tracks-3d-movement-and-touch-with-sub-half-centimeter-error",
    "domain": "AI 算力 / 半导体",
    "title": "MIT engineers build soft 3D shape-sensing skin for gaming and VR",
    "url": "https://www.tomshardware.com/virtual-reality/mit-engineers-build-soft-3d-shape-sensing-skin-for-gaming-and-vr-tracks-3d-movement-and-touch-with-sub-half-centimeter-error",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T12:25:00+00:00",
    "summary": "MIT engineers embedded soft optical fibers in a silicone sheet that reconstructs its own 3D shape, aimed at gaming, VR, and physical therapy."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/typo-squatting-attacks-with-major-domains-are-still-viable-corner-cases-with-cyrillic-characters-still-evade-the-best-checks",
    "domain": "AI 算力 / 半导体",
    "title": "Typo-squatting attacks with major domains are still viable",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/typo-squatting-attacks-with-major-domains-are-still-viable-corner-cases-with-cyrillic-characters-still-evade-the-best-checks",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T12:05:00+00:00",
    "summary": "Typo-squatting attacks with major domains are still viable — corner cases with Cyrillic characters still evade the best checks"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/300-plus-local-data-center-bans-have-only-delayed-just-three-us-projects-bans-much-more-bark-than-bite-only-2-3-gigawatts-of-data-centers-are-held-up-versus-38-gigawatts-expected-online-in-2027",
    "domain": "AI 算力 / 半导体",
    "title": "300-plus local data center bans have only delayed just three US projects",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/300-plus-local-data-center-bans-have-only-delayed-just-three-us-projects-bans-much-more-bark-than-bite-only-2-3-gigawatts-of-data-centers-are-held-up-versus-38-gigawatts-expected-online-in-2027",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T11:45:00+00:00",
    "summary": "SemiAnalysis mapped more than 300 local data center moratoriums against the US pipeline and found only three projects actually delayed."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/researchers-train-ai-to-detect-concealed-handguns-using-wi-fi-signals-open-source-wifirenet-achieves-precision-detection-on-older-802-11a-standard-by-analyzing-how-weapons-distort-wireless-signals",
    "domain": "AI 算力 / 半导体",
    "title": "Researchers train AI to detect concealed handguns using Wi-Fi signals",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/researchers-train-ai-to-detect-concealed-handguns-using-wi-fi-signals-open-source-wifirenet-achieves-precision-detection-on-older-802-11a-standard-by-analyzing-how-weapons-distort-wireless-signals",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T11:00:00+00:00",
    "summary": "Researchers have developed WiFireNet, an AI system that detects concealed handguns from Wi-Fi channel-state information, achieving 72.5% average precision in controlled indoor tests without cameras or"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/djis-first-battery-swapping-dock-gets-drones-recharged-and-back-in-the-air-in-under-45-seconds-but-dock-4-has-no-fcc-clearance-for-u-s-sale",
    "domain": "AI 算力 / 半导体",
    "title": "DJI’s first battery-swapping dock gets drones recharged and back in the air in under 45 seconds",
    "url": "https://www.tomshardware.com/tech-industry/drones/djis-first-battery-swapping-dock-gets-drones-recharged-and-back-in-the-air-in-under-45-seconds-but-dock-4-has-no-fcc-clearance-for-u-s-sale",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T10:30:00+00:00",
    "summary": "DJI Dock 4 swaps the Matrice 5TD drone’s battery in 25 seconds, but the system has no FCC clearance for sale in the U.S."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/maps/flock-camera-locations-revealed-on-mapquests-new-surveillance-layer-users-can-now-see-placement-and-direction-of-known-license-plate-readers-from-multiple-companies",
    "domain": "AI 算力 / 半导体",
    "title": "Flock camera locations revealed on MapQuest’s new Surveillance Layer",
    "url": "https://www.tomshardware.com/software/maps/flock-camera-locations-revealed-on-mapquests-new-surveillance-layer-users-can-now-see-placement-and-direction-of-known-license-plate-readers-from-multiple-companies",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-18T10:00:00+00:00",
    "summary": "This new feature could help users avoid Flock and other ALPR cameras."
  },
  {
    "id": "rss:https://www.eetimes.com/semicon-west-2026-displays-ai-era-chipmaking-workforce-development/",
    "domain": "AI 算力 / 半导体",
    "title": "SEMICON West 2026 Displays AI-Era Chipmaking, Workforce Development",
    "url": "https://www.eetimes.com/semicon-west-2026-displays-ai-era-chipmaking-workforce-development/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T20:59:50+00:00",
    "summary": "The trillion-dollar semiconductor industry is ready to adapt and expand its fab infrastructure for the AI wave. The post SEMICON West 2026 Displays AI-Era Chipmaking, Workforce Development appeared fi"
  },
  {
    "id": "rss:https://www.eetimes.com/data-center-power-a-prominent-highlight-of-ocp-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "Data Center Power a Prominent Highlight of OCP 2026",
    "url": "https://www.eetimes.com/data-center-power-a-prominent-highlight-of-ocp-2026/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T15:00:00+00:00",
    "summary": "The OCP Summit showcased power delivery boards, PSU designs, hot-swap controllers, and event-based telemetry. The post Data Center Power a Prominent Highlight of OCP 2026 appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/taiwans-ai-ambitions-run-into-talent-gap/",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan’s AI Ambitions Run into Talent Gap",
    "url": "https://www.eetimes.com/taiwans-ai-ambitions-run-into-talent-gap/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T10:55:42+00:00",
    "summary": "AMD’s David Wang told EE Times that while Taiwan has huge opportunities in rack-scale AI, physical AI, and AI PC markets, the sticking point may well be talent. The post Taiwan’s AI Ambitions Run into"
  },
  {
    "id": "rss:https://www.eetimes.com/your-chip-works-prove-it-is-secure/",
    "domain": "AI 算力 / 半导体",
    "title": "Your Chip Works. Prove It Is Secure.",
    "url": "https://www.eetimes.com/your-chip-works-prove-it-is-secure/",
    "source": "Arteris",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T08:37:49+00:00",
    "summary": "Join this 30-Minute BitCast as our expert demonstrates how information flow tracking follows security-sensitive assets during existing simulation or emulation runs. The post Your Chip Works. Prove It "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/grab-an-rtx-5090-for-discounted-usd5-300-as-part-of-an-msi-infinite-zs-prebuilt-gaming-pc-usd7-599-price-includes-other-components-worth-about-usd2-300-on-their-own",
    "domain": "AI 算力 / 半导体",
    "title": "Grab an RTX 5090 for a discounted $5,300 as part of an MSI Infinite ZS prebuilt gaming PC",
    "url": "https://www.tomshardware.com/pc-components/gpus/grab-an-rtx-5090-for-discounted-usd5-300-as-part-of-an-msi-infinite-zs-prebuilt-gaming-pc-usd7-599-price-includes-other-components-worth-about-usd2-300-on-their-own",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T20:30:58+00:00",
    "summary": "Grab an RTX 5090 for $5,300 as part of an MSI Infinite ZS prebuilt — $7,599 price includes other components worth about $2,300 on their own"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-headsets/hyperx-cloud-alpha-air-review",
    "domain": "AI 算力 / 半导体",
    "title": "HyperX Cloud Alpha Air Review: Open-back and budget-friendly",
    "url": "https://www.tomshardware.com/peripherals/gaming-headsets/hyperx-cloud-alpha-air-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T15:40:00+00:00",
    "summary": "The HyperX Cloud Alpha Air is the brand's first open-back gaming headset. It's lightweight and comfortable, and it sounds very good. But microphone pickup is low, and it doesn't seem to work with the "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/quad-8-pin-mod-protects-the-usd8-500-rtx-5090-you-cant-replace-from-melting-modders-custom-power-solution-claims-to-fix-nvidia-16-pin-gpu-meltdowns",
    "domain": "AI 算力 / 半导体",
    "title": "Quad 8-pin mod protects the $8,500 RTX 5090 you can’t replace from melting",
    "url": "https://www.tomshardware.com/pc-components/gpus/quad-8-pin-mod-protects-the-usd8-500-rtx-5090-you-cant-replace-from-melting-modders-custom-power-solution-claims-to-fix-nvidia-16-pin-gpu-meltdowns",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T15:20:00+00:00",
    "summary": "Redditor showcases a new quad 8-pin power-conversion kit for the 16-pin power connector on Nvidia GeForce RTX graphics cards."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/moza-ay210-force-feedback-base-and-mfy-yoke-review",
    "domain": "AI 算力 / 半导体",
    "title": "MOZA AY210 Force Feedback Base and MFY Yoke review: Taking flight sim immersion to the next level",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/moza-ay210-force-feedback-base-and-mfy-yoke-review",
    "source": "Dan Mateescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T15:00:00+00:00",
    "summary": "The MOZA AY210 Force Feedback Base and MFY Yoke Bundle brings force feedback and autopilot following to the world of desktop flight simulators."
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
    "id": "hn:50122431",
    "domain": "大厂 AI 动态",
    "title": "Llama.cpp on a jailbroken PS5: run any GGUF model natively on the console",
    "url": "https://github.com/cobanov/PS5LM",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 374,
    "published_at": "2026-10-16T18:32:35+00:00",
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
    "id": "hn:50118688",
    "domain": "大厂 AI 动态",
    "title": "Show HN: Gemini 4 Argon plays StarCraft",
    "url": "https://starskirmish.com/bench/v0-2/",
    "source": "__cayenne__",
    "platform": "hackernews",
    "points": 252,
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
    "points": 233,
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
    "id": "rss:https://www.theverge.com/tech/1005073/baseus-security-primesentinel-u2-pro-outdoor-3k-dual-camera-tracking-spotlight",
    "domain": "大厂 AI 动态",
    "title": "Baseus’ new security camera has a spotlight that tracks and follows moving targets",
    "url": "https://www.theverge.com/tech/1005073/baseus-security-primesentinel-u2-pro-outdoor-3k-dual-camera-tracking-spotlight",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T04:00:00+00:00",
    "summary": "Baseus announced a new addition to its lineup of AI-assisted security cameras that's more proactive about discouraging unwanted visitors instead of just recording and alerting you to their presence. T"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1014115/elon-musk-spacex-trump-account",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk’s proposed SpaceX stock giveaway would go into &#8216;Trump Accounts&#8217;",
    "url": "https://www.theverge.com/tech/1014115/elon-musk-spacex-trump-account",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T22:30:42+00:00",
    "summary": "President Donald Trump announced this afternoon that Elon Musk's SpaceX shares for children will be given through Trump Accounts. Musk said earlier today that he would give one of his SpaceX shares to"
  },
  {
    "id": "rss:https://www.theverge.com/science/1013954/fossil-fuel-power-infrastructure-data-centers-report",
    "domain": "大厂 AI 动态",
    "title": "The fossil fuel comeback is here",
    "url": "https://www.theverge.com/science/1013954/fossil-fuel-power-infrastructure-data-centers-report",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T21:48:01+00:00",
    "summary": "The US is building more fossil fuel infrastructure than it has in a decade while renewable energy growth slows down, a new report shows. Electricity demand is also climbing faster than it has in more "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1014045/coreweave-stock-debt-sector-ai",
    "domain": "大厂 AI 动态",
    "title": "CoreWeave&#8217;s debt is becoming the whole AI industry&#8217;s problem",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1014045/coreweave-stock-debt-sector-ai",
    "source": "Elizabeth Lopatto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T21:28:20+00:00",
    "summary": "CoreWeave had a bad week last week. Its bonds slipped into distressed territory by a common definition - when investors demand 1,000 basis points more in yield than they'd get from government bonds. L"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1013918/miles-plug-vehicle-tracking-data-privacy-specs-price-launch-date",
    "domain": "大厂 AI 动态",
    "title": "I tried a $99 plug that promises to track your car and send help when needed — without selling your data",
    "url": "https://www.theverge.com/tech/1013918/miles-plug-vehicle-tracking-data-privacy-specs-price-launch-date",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T21:00:17+00:00",
    "summary": "My 15-year-old daughter just got her learner's permit, so when I was pitched a new gadget tailored to teen drivers, I was intrigued. The Miles Plug is a small device that plugs into your car's OBD-II "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1013911/sonys-best-noise-canceling-earbuds-are-nearly-100-off-today-only",
    "domain": "大厂 AI 动态",
    "title": "Sony’s best noise-canceling earbuds are nearly $100 off today only",
    "url": "https://www.theverge.com/gadgets/1013911/sonys-best-noise-canceling-earbuds-are-nearly-100-off-today-only",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T18:52:41+00:00",
    "summary": "For a very limited time, Sony’s latest high-end noise-canceling earbuds are actually cheaper than their last-gen counterpart, the WF-1000XM5. B&#38;H Photo is selling Sony’s latest WF-1000XM6 in black"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1013028/apple-second-october-product-launch-announcement",
    "domain": "大厂 AI 动态",
    "title": "Apple teases MacBook Pro event next week",
    "url": "https://www.theverge.com/tech/1013028/apple-second-october-product-launch-announcement",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T16:04:29+00:00",
    "summary": "Apple has sent invites to a second product launch this month, and it's scheduled for October 28th at 1PM ET in Los Angeles. At the event, Apple is set to announce new Macs and a refreshed iPad Mini, a"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1013735/amazon-x-energy-aep-nuclear-indiana",
    "domain": "大厂 AI 动态",
    "title": "Amazon is funding a new nuclear plant in Indiana",
    "url": "https://www.theverge.com/tech/1013735/amazon-x-energy-aep-nuclear-indiana",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T15:44:20+00:00",
    "summary": "Amazon has signed an agreement with X-energy and American Electric Power (AEP) to fund the building of a new nuclear energy facility in Indiana. The proposed plant, which would replace the now defunct"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1013645/apple-mac-mini-m4-lg-c6-oled-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Apple’s last-gen Mac Mini with the M4 is $150 off",
    "url": "https://www.theverge.com/gadgets/1013645/apple-mac-mini-m4-lg-c6-oled-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T14:41:48+00:00",
    "summary": "Best Buy has a great deal for the rest of the day on the M4 Mac Mini base model that has 16GB RAM and a 256GB SSD. Normally, it doesn’t make a ton of sense to buy the M4 model for its usual $799 price"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/1012839/pritzker-ai-privacy-data-centers-flock-congress-laws",
    "domain": "大厂 AI 动态",
    "title": "JB Pritzker thinks AI could help us live to 100 — or threaten us like nukes",
    "url": "https://www.theverge.com/podcast/1012839/pritzker-ai-privacy-data-centers-flock-congress-laws",
    "source": "Nilay Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T14:30:00+00:00",
    "summary": "Today, I’m talking with Illinois Gov. JB Pritzker, who has a lot of thoughts about AI, tech, and privacy. If you’ve been listening to the show, you know that one of my running theories is that those i"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/blackwall-quadruples-valuation-to-2-2b-as-websites-wrangle-an-increasingly-crowded-internet/",
    "domain": "大厂 AI 动态",
    "title": "Blackwall quadruples valuation to $2.2B as websites wrangle an increasingly crowded internet",
    "url": "https://techcrunch.com/2026/10/20/blackwall-quadruples-valuation-to-2-2b-as-websites-wrangle-an-increasingly-crowded-internet/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T07:01:00+00:00",
    "summary": "Blackwall has raised $100M at a $2.2B valuation to continue building security and filtering tools that help websites grapple with growing bot and AI traffic."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/walmarts-flipkart-is-quietly-building-a-food-delivery-challenger-in-india/",
    "domain": "大厂 AI 动态",
    "title": "Walmart’s Flipkart is quietly building a food delivery challenger in India",
    "url": "https://techcrunch.com/2026/10/19/walmarts-flipkart-is-quietly-building-a-food-delivery-challenger-in-india/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T02:00:00+00:00",
    "summary": "Flipkart has expanded access to its food-delivery service to thousands of employees ahead of its public launch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/mamdani-says-feds-have-abdicated-on-ai-urges-new-yorkers-to-push-back/",
    "domain": "大厂 AI 动态",
    "title": "Mamdani says feds have abdicated on AI, urges New Yorkers to push back",
    "url": "https://techcrunch.com/2026/10/19/mamdani-says-feds-have-abdicated-on-ai-urges-new-yorkers-to-push-back/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T01:27:03+00:00",
    "summary": "Mayor Zohran Mamdani said Monday night that New Yorkers must resist the narrative that an AI takeover is inevitable and demand regulations that protect the public and put power back in their hands."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/nscale-and-anthropic-are-reportedly-in-talks-for-yet-another-45-billion-compute-deal/",
    "domain": "大厂 AI 动态",
    "title": "Nscale and Anthropic are reportedly in talks for yet another $45B compute deal",
    "url": "https://techcrunch.com/2026/10/19/nscale-and-anthropic-are-reportedly-in-talks-for-yet-another-45-billion-compute-deal/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T23:39:38+00:00",
    "summary": "If the deal goes through, it would be the latest in a long string of giant compute deals Anthropic has struck over the past year."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/embedded-ai-evaluators-wont-be-an-easy-solution-hugging-faces-policy-chief-says/",
    "domain": "大厂 AI 动态",
    "title": "Embedded AI evaluators won’t be an easy solution, Hugging Face’s policy chief says",
    "url": "https://techcrunch.com/2026/10/19/embedded-ai-evaluators-wont-be-an-easy-solution-hugging-faces-policy-chief-says/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T22:49:27+00:00",
    "summary": "The idea of embedded evaluators — in which supposedly \"neutral\" third-party observers are placed inside AI organizations — has been popularized over the last several months, as AI labs grapple with a "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/microsoft-says-ai-agents-are-like-insider-threats-as-frontier-models-cant-be-trusted/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft says AI agents are like insider threats as ‘frontier models can’t be trusted’",
    "url": "https://techcrunch.com/2026/10/19/microsoft-says-ai-agents-are-like-insider-threats-as-frontier-models-cant-be-trusted/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T22:04:28+00:00",
    "summary": "Microsoft wants enterprises to closely watch the agents that employees use with systems not controlled by AI labs like OpenAI and Anthropic."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/amazon-is-taking-its-biggest-shot-at-nvidia-yet-with-new-torchneuron-dev-tool/",
    "domain": "大厂 AI 动态",
    "title": "Amazon is taking its biggest shot at Nvidia yet with new TorchNeuron dev tool",
    "url": "https://techcrunch.com/2026/10/19/amazon-is-taking-its-biggest-shot-at-nvidia-yet-with-new-torchneuron-dev-tool/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T20:09:24+00:00",
    "summary": "Amazon wants to break Nvidia’s hold on PyTorch, the free toolkit used to build most AI apps, so that more developers run their apps on alternative chips like its own."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/",
    "domain": "大厂 AI 动态",
    "title": "Hackers hit AI coding tool OpenCode, running up charges on users’ AI accounts",
    "url": "https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T19:28:34+00:00",
    "summary": "OpenCode is an open source AI coding agent that's become a popular alternative to Claude Code and Cursor. But hackers got into part of its online platform and stole some users’ API keys, and the AI to"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/tolan-snags-30m-for-its-ai-companion-that-helps-users-navigate-life/",
    "domain": "大厂 AI 动态",
    "title": "Tolan snags $30M for its AI companion that helps users navigate life",
    "url": "https://techcrunch.com/2026/10/19/tolan-snags-30m-for-its-ai-companion-that-helps-users-navigate-life/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T19:00:12+00:00",
    "summary": "AI companion app Tolan has raised another $30 million after attracting more than 250,000 active users."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/replikas-founder-built-the-ai-assistant-she-pitched-at-disrupt-12-years-ago/",
    "domain": "大厂 AI 动态",
    "title": "Replika’s founder built the AI assistant she pitched at Disrupt 12 years ago",
    "url": "https://techcrunch.com/2026/10/19/replikas-founder-built-the-ai-assistant-she-pitched-at-disrupt-12-years-ago/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T18:49:04+00:00",
    "summary": "Eugenia Kuyda's newest startup Wabi is positioned to take advantage of an idea she had more than a decade ago. Wabi offers a personal AI assistant with a twist, free and downloadable to anyone today."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/tenstorrent-hits-6-2b-valuation-to-scale-open-weight-ai-chips/",
    "domain": "大厂 AI 动态",
    "title": "Tenstorrent hits $6.2B valuation to scale open-weight AI chips",
    "url": "https://techcrunch.com/2026/10/19/tenstorrent-hits-6-2b-valuation-to-scale-open-weight-ai-chips/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T18:37:27+00:00",
    "summary": "After drawing acquisition interest earlier this year, the Nvidia challenger raised $1.5 billion to remain independent."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/ai-assistant-startup-town-nabs-unicorn-valuation-four-months-after-launch/",
    "domain": "大厂 AI 动态",
    "title": "AI assistant startup Town nabs unicorn valuation 4 months after launch",
    "url": "https://techcrunch.com/2026/10/19/ai-assistant-startup-town-nabs-unicorn-valuation-four-months-after-launch/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T18:00:39+00:00",
    "summary": "AI assistant startup Town nabbed a unicorn valuation on Monday, announcing a $108 million Series B round co-led by Forerunner Ventures and Menlo Ventures."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/rivians-ceo-says-autonomy-will-enable-dramatically-different-vehicle-designs/",
    "domain": "大厂 AI 动态",
    "title": "Rivian’s CEO says autonomy will enable ‘dramatically different’ vehicle designs",
    "url": "https://techcrunch.com/2026/10/19/rivians-ceo-says-autonomy-will-enable-dramatically-different-vehicle-designs/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T17:39:51+00:00",
    "summary": "Founder and CEO RJ Scaringe said he thinks autonomy will allow his company to build radically different kinds of vehicles than the outdoorsy SUVs and trucks it currently makes."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/amazon-to-fund-12-small-nuclear-reactors-at-former-indiana-coal-plant/",
    "domain": "大厂 AI 动态",
    "title": "Amazon to fund 12 small nuclear reactors at former Indiana coal plant",
    "url": "https://techcrunch.com/2026/10/19/amazon-to-fund-12-small-nuclear-reactors-at-former-indiana-coal-plant/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T16:55:56+00:00",
    "summary": "Amazon and X-energy have inked another deal to deploy nuclear power to the grid. This one will generate nearly 1 gigawatt of electricity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/people-are-using-ai-to-make-their-smart-tvs-dumb-again/",
    "domain": "大厂 AI 动态",
    "title": "People are using AI to make their smart TVs dumb again",
    "url": "https://techcrunch.com/2026/10/19/people-are-using-ai-to-make-their-smart-tvs-dumb-again/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T16:13:22+00:00",
    "summary": "Fed up with ads, tracking, and sluggish interfaces, some smart TV owners are turning to AI agents to strip away bloatware and take back control of their TVs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/nvidia-launches-new-open-models-to-run-agents-in-the-enterprise-and-on-pcs/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia launches new open models to run agents in the enterprise and on PCs",
    "url": "https://techcrunch.com/2026/10/19/nvidia-launches-new-open-models-to-run-agents-in-the-enterprise-and-on-pcs/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T15:37:09+00:00",
    "summary": "Nvidia is leaning hard into the trend of enterprise companies wanting to run their own open models in their own data centers and also trying to make on-device, private AI agents a thing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/apple-updates-guidelines-to-ban-nudify-apps-masquerading-as-regular-apps-to-pass-review/",
    "domain": "大厂 AI 动态",
    "title": "Apple updates guidelines to ban nudify apps masquerading as regular apps to pass review",
    "url": "https://techcrunch.com/2026/10/19/apple-updates-guidelines-to-ban-nudify-apps-masquerading-as-regular-apps-to-pass-review/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T12:56:14+00:00",
    "summary": "The company updated its guidelines with strong language around AI and user-generated content, and how app developers should include enough preventative measures to moderate objectionable or offensive "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/musk-pledges-to-give-every-kid-in-america-one-of-his-spacex-shares/",
    "domain": "大厂 AI 动态",
    "title": "Musk pledges to give ‘every kid in America’ one of his SpaceX shares",
    "url": "https://techcrunch.com/2026/10/19/musk-pledges-to-give-every-kid-in-america-one-of-his-spacex-shares/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T12:42:55+00:00",
    "summary": "Musk's post came just a few hours after Anthropic promised to put 5% of its shares into a new \"public benefit fund,\" which it intends to use to make \"large donations to traditional nonprofits or direc"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/laplace-intelligence-red-teams-robots-and-self-driving-cars-before-they-hit-the-real-world/",
    "domain": "大厂 AI 动态",
    "title": "Laplace Intelligence red-teams robots and self-driving cars before they hit the real world",
    "url": "https://techcrunch.com/2026/10/19/laplace-intelligence-red-teams-robots-and-self-driving-cars-before-they-hit-the-real-world/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T12:30:00+00:00",
    "summary": "University of Michigan spinout Laplace Intelligence uses AI agents and interactive simulation to stress-test robots and self-driving vehicles before deployment. The profitable startup is competing in "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/19/khosla-ventures-doubles-down-on-even-healthcare-to-challenge-indias-hospital-economics/",
    "domain": "大厂 AI 动态",
    "title": "Khosla Ventures doubles down on Even Healthcare to challenge India’s hospital economics",
    "url": "https://techcrunch.com/2026/10/19/khosla-ventures-doubles-down-on-even-healthcare-to-challenge-indias-hospital-economics/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T07:30:00+00:00",
    "summary": "Even Healthcare reaches a $300 million valuation in a Khosla Ventures-led round as it plans to expand its hospital network in India."
  },
  {
    "id": "rss:https://stratechery.com/2026/do-you-trust-apple/",
    "domain": "大厂 AI 动态",
    "title": "Do You Trust Apple?",
    "url": "https://stratechery.com/2026/do-you-trust-apple/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T10:00:00+00:00",
    "summary": "Apple has a lot of trust in terms of delivering integrated products and preserving privacy; the real trust question is if you think Siri AI will justify investing more in their ecosystem."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/10/japan-launches-mission-to-bring-home-a-piece-of-the-martian-moon-phobos/",
    "domain": "大厂 AI 动态",
    "title": "Japan launches mission to bring home a piece of the Martian moon Phobos",
    "url": "https://arstechnica.com/space/2026/10/japan-launches-mission-to-bring-home-a-piece-of-the-martian-moon-phobos/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T05:59:56+00:00",
    "summary": "The climax for MMX will come in 2029, when the spacecraft will attempt up to two landings on Phobos."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/10/pennsylvania-issues-alert-on-congenital-measles-something-us-hasnt-seen-for-decades/",
    "domain": "大厂 AI 动态",
    "title": "Pennsylvania issues alert on congenital measles—something US hasn't seen for decades",
    "url": "https://arstechnica.com/health/2026/10/pennsylvania-issues-alert-on-congenital-measles-something-us-hasnt-seen-for-decades/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T22:44:26+00:00",
    "summary": "Congenital measles can be fatal, and survivors require monitoring for years."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/10/russian-spacecraft-maneuvers-in-extreme-proximity-to-satellite-used-by-ukraine/",
    "domain": "大厂 AI 动态",
    "title": "Russian spacecraft maneuvers in \"extreme proximity\" to satellite used by Ukraine",
    "url": "https://arstechnica.com/space/2026/10/russian-spacecraft-maneuvers-in-extreme-proximity-to-satellite-used-by-ukraine/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T20:54:17+00:00",
    "summary": "\"Kosmos 2612 closed from hundreds of kilometers away to extreme proximity to ICEYE-X36.\""
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/10/accused-openai-spy-had-folder-called-saudi-gov-docs-fbi-says/",
    "domain": "大厂 AI 动态",
    "title": "Accused OpenAI spy had folder called “Saudi Gov Docs,” FBI says",
    "url": "https://arstechnica.com/tech-policy/2026/10/accused-openai-spy-had-folder-called-saudi-gov-docs-fbi-says/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T20:21:53+00:00",
    "summary": "US fears Saudi government will help ex-OpenAI engineer flee spying charges."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/batteries-have-a-small-carbon-footprint-we-can-make-it-smaller/",
    "domain": "大厂 AI 动态",
    "title": "Batteries help reduce emissions, but how do we reduce their emissions?",
    "url": "https://arstechnica.com/science/2026/10/batteries-have-a-small-carbon-footprint-we-can-make-it-smaller/",
    "source": "Scott K. Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-19T20:03:55+00:00",
    "summary": "One way to make batteries cleaner is to make fewer of them."
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
    "id": "hn:50142772",
    "domain": "股票",
    "title": "How the Fed Is Quietly Inflating the AI Bubble While Hiking Your Electric Bill",
    "url": "https://www.thebignewsletter.com/p/how-the-federal-reserve-secretly",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-10-18T16:48:25+00:00",
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
    "id": "hn:50112657",
    "domain": "金融",
    "title": "Tesla Roadster",
    "url": "https://www.tesla.com/roadster",
    "source": "shekhar101",
    "platform": "hackernews",
    "points": 1641,
    "published_at": "2026-10-16T01:32:45+00:00",
    "summary": ""
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
    "id": "hn:50131440",
    "domain": "金融",
    "title": "US federal budget deficit jumps 12% in one year to nearly $2 Trillion",
    "url": "https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 203,
    "published_at": "2026-10-17T14:22:05+00:00",
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
    "id": "hn:50141295",
    "domain": "金融",
    "title": "Tesla 'Cannot Guarantee' Roadster Reservation Holders Will Ever Get a Car",
    "url": "https://www.thedrive.com/news/tesla-cannot-guarantee-roadster-reservation-holders-will-ever-get-a-car",
    "source": "healsdata",
    "platform": "hackernews",
    "points": 120,
    "published_at": "2026-10-18T14:16:41+00:00",
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
    "id": "hn:50161207",
    "domain": "金融",
    "title": "U.S. Supreme Court to review 1868 federal ban on home distilling of liquor",
    "url": "https://www.staradvertiser.com/2026/10/19/breaking-news/u-s-supreme-court-to-review-1868-federal-ban-on-home-distilling-of-liquor/",
    "source": "Jimmc414",
    "platform": "hackernews",
    "points": 52,
    "published_at": "2026-10-20T04:02:26+00:00",
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
