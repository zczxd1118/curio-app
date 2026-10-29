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

- 今日日期：`2026-10-29`
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
  "date": "2026-10-29",
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
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 2048981,
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
    "points": 1449997,
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
    "points": 1407165,
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
    "points": 1359878,
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
    "points": 906452,
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
    "points": 881566,
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
    "points": 734769,
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
    "points": 594604,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 426354,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 357538,
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
    "points": 339352,
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
    "points": 316740,
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
    "points": 289106,
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
    "points": 219522,
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
    "points": 185102,
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
    "points": 163899,
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
    "points": 161551,
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
    "points": 161302,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1renJ6VEuZ",
    "domain": "AI",
    "title": "DeepSeekHarness装进手机",
    "url": "http://www.bilibili.com/video/av117467271666305",
    "source": "文大师啵啵",
    "platform": "bilibili",
    "points": 77300,
    "published_at": "2026-10-19T11:14:25+00:00",
    "summary": "如果把 DeepSeek Harness 完整搬进 Android，手机会变成什么？\n\n它不是又一个聊天助手，而是一台随身 AI 工作站：有自己的工作区、Linux 环境、终端、文件管理系统、插件系统，也能通过无障碍或者 Shizuku 操作手机，并通过内置浏览器实现网页自动化。\n\n这个项目叫 DSHBox，让 DeepSeek Harness 运行在手机上。\n\n本视频展示从首页进入、选择工作区、"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 72892,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1PznU6YEZE",
    "domain": "AI",
    "title": "如何审核 AI 写的代码？从写代码到上线，一套保证产品质量的全流程",
    "url": "http://www.bilibili.com/video/av117502453488457",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 56645,
    "published_at": "2026-10-26T12:23:49+00:00",
    "summary": "最近，Anthropic 发了一篇文章，介绍了 Claude Code 团队是怎么审核 AI 写的代码的。因为代码审核和整个发布流程是紧密关联的，所以文章其实把他们从写代码到上线的整个流程都讲了一遍。本期视频，我会结合自己的理解，带大家把这个流程从头到尾走一遍。看完之后，你不仅能了解该怎么审核 AI 写的代码，还能知道怎样搭建一套可靠的流程，保证 AI 写出来的产品的质量。\n\n本期视频的具体内容包"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 56498,
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
    "points": 49833,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1EfY76YEwp",
    "domain": "AI",
    "title": "14k Star Claude Code 开源桌面端，能自动操作电脑了！",
    "url": "http://www.bilibili.com/video/av117251936293145",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 49041,
    "published_at": "2026-09-11T10:30:01+00:00",
    "summary": "基于此前泄露的 Claude Code 源代码，我做了一个开源桌面端 cc-haha，并持续迭代。\n这次重构了 Computer Use 电脑操控功能：AI 能自己看屏幕、操作 APP，在 Mac 后台搭建小镇，也不占用我的鼠标键盘。\n本期从下载安装、模型配置到权限授权，带你一步步用起来。支持自选模型，不需要 Claude 账号。"
  },
  {
    "id": "bvid:BV1woHQ6kEtv",
    "domain": "AI",
    "title": "【2026最新版】Workbuddy财务自动化办公实战教程，搭建数字员工，能够秒做账、报税、报销、出报表、做财务分析、编制预算、处理合并报表",
    "url": "http://www.bilibili.com/video/av117404038466491",
    "source": "Max极客菌",
    "platform": "bilibili",
    "points": 44416,
    "published_at": "2026-10-08T07:22:21+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 41024,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34617,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 34045,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 31941,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 31097,
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
    "points": 29893,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1EReW6pEfv",
    "domain": "AI",
    "title": "14K Star Claude Code 开源桌面端，5个AI自己分工干活了！",
    "url": "http://www.bilibili.com/video/av117276346946735",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 29457,
    "published_at": "2026-09-16T03:30:00+00:00",
    "summary": "上一期让 cc-haha 自动操作电脑，这一期，我让 5 个 AI Agent 一起做开发。\n\n用的还是我一直在维护的开源 Claude Code 桌面端：cc-haha。这次重点演示 Agent Teams：我给出一个开发需求，队长拆任务，前端、后端、测试和 Code Review 分工推进。成员做完手上的工作，还能继续领取可执行的任务，直接给队友发消息。\n\n这期用一个真实任务，从组队、共享任务"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 29135,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 29025,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV14rxM6qEnL",
    "domain": "AI",
    "title": "最新Skills开发教程，Agent skill实战|WorkBuddy+Codex+DeepSeek Harness",
    "url": "http://www.bilibili.com/video/av117511429295044",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 26709,
    "published_at": "2026-10-28T02:00:00+00:00",
    "summary": "【课程简介】Agent Skills零基础教程，从WorkBuddy、Codex上手到项目落地实战。"
  },
  {
    "id": "bvid:BV1B97868EZK",
    "domain": "AI",
    "title": "Claude Code全流程开发实战丨MCP实战、Skills+Agent多工具协作、AI编程、自动化工作流、私有化部署、转行AI岗",
    "url": "http://www.bilibili.com/video/av116810192131401",
    "source": "博学谷",
    "platform": "bilibili",
    "points": 26561,
    "published_at": "2026-06-25T10:11:09+00:00",
    "summary": "视频配套资源领取方式戳：https://www.bilibili.com/opus/1217780115004456969\n或关注【博学谷】公综号回复关键词领取：260625\n学完本课程，你将能够独立完成AI Agent 研发与落地：深度掌握 Claude Code 辅助编程、Skill 技能包编排与 MCP 协议集成打通私有系统连接的“桥梁”，并能学会私有化部署。最终凭借“AI Coding 重"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 24491,
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
    "points": 21173,
    "published_at": "2024-11-18T07:04:36+00:00",
    "summary": "欢迎关注我的知识星球：https://t.zsxq.com/FF0He\n\n我会分享最新AI资讯、源代码、回答你的提问。\n\n视频亮点：\n\n双工具对比：解析 Cursor 和 Windsurf 各自优势\n实战案例：从五子棋到卡路里计算AI应用的完整开发过程\n专业部署：Android Studio 配置与构建技巧\n\n时间戳：\n\n0:00 - 引言\n\n0:26 - 我开发的应用演示\n\n2:33 - Rea"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15435,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV1Uwj863EPS",
    "domain": "AI",
    "title": "IDEA中集成claudecode和codex，全程无废话，提升编程效率",
    "url": "http://www.bilibili.com/video/av116788633340919",
    "source": "阿秀_love",
    "platform": "bilibili",
    "points": 14843,
    "published_at": "2026-06-22T01:00:00+00:00",
    "summary": "IDEA中集成claudecode和codex，全程无废话，提升编程效率，先看上一个视频下载安装claudecode和codex，关注后自动获取安装包。"
  },
  {
    "id": "bvid:BV1Vd8i6iEjd",
    "domain": "AI",
    "title": "AI办公实战课，AI助力工作学习效率提升N倍--从提示词、写作到数据分析与 AI 绘画，一课打通",
    "url": "http://www.bilibili.com/video/av117132901815801",
    "source": "1620谷爱凌",
    "platform": "bilibili",
    "points": 14642,
    "published_at": "2026-08-21T10:04:22+00:00",
    "summary": "AI办公实战课，AI助力工作学习效率提升N倍--从提示词、写作到数据分析与 AI 绘画，一课打通"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 13301,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1wFpP6uE1s",
    "domain": "AI",
    "title": "【开源】让手机自己操作 App！手上的 ai Agent！GitHub开源安卓App推荐",
    "url": "http://www.bilibili.com/video/av117394643097499",
    "source": "补药满减哇",
    "platform": "bilibili",
    "points": 9686,
    "published_at": "2026-10-07T01:05:00+00:00",
    "summary": "开源安卓 AI Agent：RikkaHub Agent Pure\n它能「看懂」屏幕、自己操作各种 App，也能组队干活。\n\n⬇️ 下载 &amp; 源码（AGPL-3.0）\nhttps://github.com/wuyhong715/rikkahub-agent-pure\n\n▶ 本片讲两件事\n① 无障碍屏幕自动化：读控件树定位、实时决策，不是死坐标脚本\n② 专家团系统：每个专家有自己的模型/工具"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 9350,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 8624,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "bvid:BV1UaYK6nEjP",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av117244419903051",
    "source": "茶子兀",
    "platform": "bilibili",
    "points": 7435,
    "published_at": "2026-09-10T02:39:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1t9pt6JETF",
    "domain": "AI",
    "title": "Cursor vs Claude Code vs Codex哪个好？三大AI编程工具区别与选择指南",
    "url": "http://www.bilibili.com/video/av117411437090209",
    "source": "不管这么多",
    "platform": "bilibili",
    "points": 7048,
    "published_at": "2026-10-09T14:35:26+00:00",
    "summary": "三大编程工具要如何选？"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6912,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1fN7D6XEBE",
    "domain": "AI",
    "title": "【战锤3Mod教程】03-进阶向：使用AI Agent来制作MOD",
    "url": "http://www.bilibili.com/video/av116700955609851",
    "source": "Wyccc威力加强版",
    "platform": "bilibili",
    "points": 6794,
    "published_at": "2026-06-06T03:12:27+00:00",
    "summary": "没有剪辑和草稿一次录制完成，想到哪说到哪。"
  },
  {
    "id": "bvid:BV1vtHL6dEPa",
    "domain": "AI",
    "title": "【10月最新】Claude安装汉化教程！接入opus5.5！Sonnet 5.5！",
    "url": "http://www.bilibili.com/video/av117382496589012",
    "source": "小小_072",
    "platform": "bilibili",
    "points": 6503,
    "published_at": "2026-10-04T11:56:28+00:00",
    "summary": "视频所需文件：\nhttps://pan.quark.cn/s/3758f2408ea9"
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
    "id": "hn:50219700",
    "domain": "AI 算力 / 半导体",
    "title": "GPU-unlock: FP/BF16 instruction issue rate on Nvidia 3000's cards",
    "url": "https://github.com/Zagitta/gpu-unlock",
    "source": "fragebogen",
    "platform": "hackernews",
    "points": 350,
    "published_at": "2026-10-24T09:58:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50236073",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia and Micron Make Up 34% of America's Earnings Boom",
    "url": "https://www.wsj.com/finance/stocks/the-earnings-boom-is-heavily-reliant-on-just-a-handful-of-stocks-21decb53",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 171,
    "published_at": "2026-10-25T21:07:38+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/how-ai-redefines-semiconductor-manufacturing-from-materials-up/",
    "domain": "AI 算力 / 半导体",
    "title": "How AI Redefines Semiconductor Manufacturing, From Materials Up",
    "url": "https://www.eetimes.com/how-ai-redefines-semiconductor-manufacturing-from-materials-up/",
    "source": "Mahiro Tsujino",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T08:30:08+00:00",
    "summary": "AI chip advances depend on more than design, requiring new materials, manufacturing equipment, and packaging technologies to meet rising performance demands. The post How AI Redefines Semiconductor Ma"
  },
  {
    "id": "rss:https://www.eetimes.com/canadian-startup-aims-to-be-quantums-picks-and-shovels/",
    "domain": "AI 算力 / 半导体",
    "title": "Canadian Startup Aims to Be Quantum’s ‘Picks’ and ‘Shovels’",
    "url": "https://www.eetimes.com/canadian-startup-aims-to-be-quantums-picks-and-shovels/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T20:50:32+00:00",
    "summary": "Toronto-based Meissner Technologies uses AI and laboratory testing to discover superconducting materials that could cut cooling costs and help quantum computers scale. The post Canadian Startup Aims t"
  },
  {
    "id": "rss:https://www.eetimes.com/sk-hynix-reports-record-q3-results-driven-by-ai-memory-surge/",
    "domain": "AI 算力 / 半导体",
    "title": "SK Hynix Reports Record Q3 Results Driven by AI Memory Surge",
    "url": "https://www.eetimes.com/sk-hynix-reports-record-q3-results-driven-by-ai-memory-surge/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T16:43:42+00:00",
    "summary": "Long-term customer contracts and rising chip prices point to a change in how memory manufacturers manage multi-year production capacity and capex. The post SK Hynix Reports Record Q3 Results Driven by"
  },
  {
    "id": "rss:https://www.eetimes.com/secure-safety-and-security-communications/",
    "domain": "AI 算力 / 半导体",
    "title": "Secure Safety and Security Communications",
    "url": "https://www.eetimes.com/secure-safety-and-security-communications/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T14:00:00+00:00",
    "summary": "This whitepaper explores how building safety and security systems can overcome the limitations of legacy RS-485 networks by adopting Single Pair Ethernet (SPE). It examines the growing demands of AI-e"
  },
  {
    "id": "rss:https://www.eetimes.com/full-stack-semiconductor-solutions-for-embodied-ai-robotics/",
    "domain": "AI 算力 / 半导体",
    "title": "Full-Stack Semiconductor Solutions for Embodied AI & Robotics",
    "url": "https://www.eetimes.com/full-stack-semiconductor-solutions-for-embodied-ai-robotics/",
    "source": "NSING",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T14:00:00+00:00",
    "summary": "NSING Technologies, a Singapore-founded semiconductor company, presents this whitepaper on its full-stack semiconductor solutions for embodied AI and robotics, built around high-performance MCUs, secu"
  },
  {
    "id": "rss:https://www.eetimes.com/intel-wants-a-quantum-business-classiq-could-help-build-one/",
    "domain": "AI 算力 / 半导体",
    "title": "Intel Wants a Quantum Business, Classiq Could Help Build One",
    "url": "https://www.eetimes.com/intel-wants-a-quantum-business-classiq-could-help-build-one/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T08:05:29+00:00",
    "summary": "After years of hardware research, Intel plans to acquire a software platform that connects quantum developers with enterprise users. The post Intel Wants a Quantum Business, Classiq Could Help Build O"
  },
  {
    "id": "rss:https://www.eetimes.com/transitioning-legacy-aircraft-power-architectures-to-high-density-switching-supplies/",
    "domain": "AI 算力 / 半导体",
    "title": "Transitioning Legacy Aircraft Power Architectures to High-Density Switching Supplies",
    "url": "https://www.eetimes.com/transitioning-legacy-aircraft-power-architectures-to-high-density-switching-supplies/",
    "source": "Emily Newton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T23:00:00+00:00",
    "summary": "High-density switching supplies help modernize legacy aircraft power systems while addressing obsolescence, efficiency, integration, and compliance challenges. The post Transitioning Legacy Aircraft P"
  },
  {
    "id": "rss:https://www.eetimes.com/copperpilot-raises-pre-seed-to-develop-ai-agent-for-pcb-design/",
    "domain": "AI 算力 / 半导体",
    "title": "CopperPilot Raises Pre-seed to Develop AI Agent for PCB Design",
    "url": "https://www.eetimes.com/copperpilot-raises-pre-seed-to-develop-ai-agent-for-pcb-design/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T13:58:33+00:00",
    "summary": "CopperPilot’s CEO said the startup has built its AI design agent so that “no hardware team is ever blocked because a board is too hard to design.” The post CopperPilot Raises Pre-seed to Develop AI Ag"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/apple-launches-new-macbook-with-touchscreen-and-oled-starts-at-usd2-899",
    "domain": "AI 算力 / 半导体",
    "title": "Apple launches new MacBook Pro with touchscreen and OLED — starts at $2,899",
    "url": "https://www.tomshardware.com/laptops/apple-launches-new-macbook-with-touchscreen-and-oled-starts-at-usd2-899",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T17:15:39+00:00",
    "summary": "The computer is also lighter and has an updated speaker system."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/malaysia-seizes-usd12-million-worth-of-advanced-ai-chips-hidden-inside-30-servers-customs-says-suspected-smuggling-network-used-the-country-as-a-transit-hub",
    "domain": "AI 算力 / 半导体",
    "title": "Malaysia seizes $12 million worth of advanced AI chips hidden inside 30 servers",
    "url": "https://www.tomshardware.com/tech-industry/policy/malaysia-seizes-usd12-million-worth-of-advanced-ai-chips-hidden-inside-30-servers-customs-says-suspected-smuggling-network-used-the-country-as-a-transit-hub",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T17:02:14+00:00",
    "summary": "Malaysian customs seized 30 servers containing more than $12 million worth of advanced AI chips at Kuala Lumpur International Airport, as authorities investigate a suspected smuggling network linked t"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/manufacturing/ai-component-hikes-force-the-worlds-largest-pc-makers-to-return-manufacturing-capacity-to-china-brands-to-seek-lower-production-costs-and-efficiency-in-established-supply-chain",
    "domain": "AI 算力 / 半导体",
    "title": "AI component hikes force the world's largest PC makers to return manufacturing capacity to China",
    "url": "https://www.tomshardware.com/tech-industry/manufacturing/ai-component-hikes-force-the-worlds-largest-pc-makers-to-return-manufacturing-capacity-to-china-brands-to-seek-lower-production-costs-and-efficiency-in-established-supply-chain",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T15:24:16+00:00",
    "summary": "PC manufacturing in China tends to be cheaper because of an established supply chain and workforce. Smaller Chinese suppliers are also winning orders by offering easier access to domestic chip manufac"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-tells-engineers-to-stop-tokenmaxxing-to-look-productive-says-ai-will-be-central-to-software-development-but-usage-is-not-the-goal-new-guidelines-claim",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon tells engineers to stop ‘tokenmaxxing’ to look productive",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-tells-engineers-to-stop-tokenmaxxing-to-look-productive-says-ai-will-be-central-to-software-development-but-usage-is-not-the-goal-new-guidelines-claim",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T15:13:48+00:00",
    "summary": "Amazon has published new engineering guidelines warning developers and managers against ‘tokenmaxxing,’ arguing that AI usage metrics are ‘deeply flawed’ unless tied to long-term outcomes. The move fo"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/fcc-rebuffs-tp-link-again-as-it-attempts-to-sell-wi-fi-8-gear-in-the-us-fcc-alleges-inaccurate-documentation-and-out-of-spec-power-levels-for-routers",
    "domain": "AI 算力 / 半导体",
    "title": "FCC rebuffs TP-Link again as it attempts to sell Wi-Fi 8 gear in the US",
    "url": "https://www.tomshardware.com/networking/routers/fcc-rebuffs-tp-link-again-as-it-attempts-to-sell-wi-fi-8-gear-in-the-us-fcc-alleges-inaccurate-documentation-and-out-of-spec-power-levels-for-routers",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T15:07:35+00:00",
    "summary": "TP-Link just can’t seem to catch a break with the FCC, as it’s not under fire for exceeding power limits on its routers"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/corsair-warthog-case-review",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair Warthog case review: A rugged, military-themed chassis with plenty of airflow",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/corsair-warthog-case-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T14:00:00+00:00",
    "summary": "The military-inspired Warthog mid-tower borrows from Corsair’s Vengeance C70 and takes the military aesthetic up a couple of notches. Is the rugged look worth it?"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/us-marines-join-nato-mission-in-the-baltic-sea-to-protect-undersea-cables-from-sabotage-as-russia-continues-to-lurk-around-four-dozen-recon-and-intel-specialists-deployed-to-deter-seabed-threats",
    "domain": "AI 算力 / 半导体",
    "title": "US Marines join NATO mission in the Baltic Sea to protect undersea cables from sabotage as Russia continues to lurk",
    "url": "https://www.tomshardware.com/tech-industry/us-marines-join-nato-mission-in-the-baltic-sea-to-protect-undersea-cables-from-sabotage-as-russia-continues-to-lurk-around-four-dozen-recon-and-intel-specialists-deployed-to-deter-seabed-threats",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T13:24:14+00:00",
    "summary": "50 U.S. marines are joining a NATO mission to help protect and monitor undersea infrastructure in the Baltic Sea."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/manufacturing/sk-hynix-owned-solidigm-is-plotting-a-new-usd45-billion-flash-memory-factory-for-the-us-report-claims-wants-go-ahead-to-export-equipment-for-china-upgrades-in-return",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix-owned Solidigm is plotting a new $45 billion flash memory factory for the US, report claims",
    "url": "https://www.tomshardware.com/tech-industry/manufacturing/sk-hynix-owned-solidigm-is-plotting-a-new-usd45-billion-flash-memory-factory-for-the-us-report-claims-wants-go-ahead-to-export-equipment-for-china-upgrades-in-return",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T13:01:21+00:00",
    "summary": "Solidigm, an American subsidiary of SK hynix, is in discussions about potentially investing $45 billion in a new flash chip factory that would be built in the United States."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/external-hdds/seagates-16tb-external-hdd-falls-to-0-025-cents-per-gb-at-newegg-this-storage-deal-is-usd50-cheaper-than-even-its-prime-day-sale-price",
    "domain": "AI 算力 / 半导体",
    "title": "Seagate's 16TB external HDD falls to 0.025 cents per GB at Newegg",
    "url": "https://www.tomshardware.com/pc-components/external-hdds/seagates-16tb-external-hdd-falls-to-0-025-cents-per-gb-at-newegg-this-storage-deal-is-usd50-cheaper-than-even-its-prime-day-sale-price",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T13:00:00+00:00",
    "summary": "Save $150 on this 16TB Seagate Expansion Desktop External HDD when you make use of this Newegg deal."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/why-native-pc-ports-of-console-games-are-suddenly-everywhere-reverse-engineer-anything-gives-ai-agents-a-unified-toolkit-and-byte-for-byte-checks-keep-hallucinations-in-line",
    "domain": "AI 算力 / 半导体",
    "title": "Why native PC ports of console games are suddenly everywhere",
    "url": "https://www.tomshardware.com/video-games/why-native-pc-ports-of-console-games-are-suddenly-everywhere-reverse-engineer-anything-gives-ai-agents-a-unified-toolkit-and-byte-for-byte-checks-keep-hallucinations-in-line",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T12:00:00+00:00",
    "summary": "With dozens of titles unofficially ported to PC over the past few months, the big questions are: why is this now possible, and what changed?"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-gpu-vendor-palit-denies-its-galax-factory-has-closed-due-to-a-shortage-of-chips-company-says-brand-continues-to-operate-as-usual",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX GPU vendor Palit denies its Galax factory has closed due to a shortage of chips",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-gpu-vendor-palit-denies-its-galax-factory-has-closed-due-to-a-shortage-of-chips-company-says-brand-continues-to-operate-as-usual",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T11:56:26+00:00",
    "summary": "Palit denies news that Galax is going out of production."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd249-on-32gb-of-ddr5-with-this-9800x3d-parts-bundle-grab-one-of-amds-top-cpus-with-an-msi-x870e-motherboard-and-a-free-aio-cooler-for-under-usd1-100",
    "domain": "AI 算力 / 半导体",
    "title": "Save $249 on 32GB of DDR5 with this 9800X3D parts bundle",
    "url": "https://www.tomshardware.com/pc-components/save-usd249-on-32gb-of-ddr5-with-this-9800x3d-parts-bundle-grab-one-of-amds-top-cpus-with-an-msi-x870e-motherboard-and-a-free-aio-cooler-for-under-usd1-100",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T11:48:55+00:00",
    "summary": "Save $248.99 on this AMD Ryzen 7 9800X3D bundle at Newegg with an MSI MAG X870E Tomahawk Max Wifi motherboard and 32GB of DDR5-6000 RAM, now just $1,094.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/taiwan-working-on-autonomous-drone-swarms-to-counter-chinas-increasingly-aggressive-grey-zone-military-tactics-island-has-already-completed-flight-simulations-now-working-towards-flight-trials-over-maritime-areas",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan working on autonomous drone swarms to counter China’s increasingly aggressive grey-zone military tactics",
    "url": "https://www.tomshardware.com/tech-industry/drones/taiwan-working-on-autonomous-drone-swarms-to-counter-chinas-increasingly-aggressive-grey-zone-military-tactics-island-has-already-completed-flight-simulations-now-working-towards-flight-trials-over-maritime-areas",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T11:30:00+00:00",
    "summary": "The island is building an autonomous system that would work with various drones, allowing it to extend the reach and endurance of its coast guard ships."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-and-oracle-bring-vera-cpu-instances-online-in-multi-gigawatt-deployment-oci-superclusters-also-set-to-expand-with-rubin-only-clusters-attached-to-dual-xeon-6-hosts",
    "domain": "AI 算力 / 半导体",
    "title": "Standalone Nvidia Vera CPUs land in Oracle Cloud's multi-gigawatt deployment",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-and-oracle-bring-vera-cpu-instances-online-in-multi-gigawatt-deployment-oci-superclusters-also-set-to-expand-with-rubin-only-clusters-attached-to-dual-xeon-6-hosts",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T11:00:00+00:00",
    "summary": "Nvidia’s Vera CPU is now generally available on Oracle’s OCI Superclusters, a win for Nvidia as it moves past NVL72 to a standalone Vera deployment at a major hyperscaler."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/servers/it-vendor-lists-massive-usd60-million-ai-cluster-on-ebay-300x-racks-of-decommissioned-gpus-includes-9-600-nvidia-a100-gpus-and-4-200-amd-epyc-cpus-plus-free-shipping",
    "domain": "AI 算力 / 半导体",
    "title": "IT vendor lists massive $60 million AI supercomputer on eBay with 300 racks of decommissioned GPUs",
    "url": "https://www.tomshardware.com/desktops/servers/it-vendor-lists-massive-usd60-million-ai-cluster-on-ebay-300x-racks-of-decommissioned-gpus-includes-9-600-nvidia-a100-gpus-and-4-200-amd-epyc-cpus-plus-free-shipping",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T10:30:00+00:00",
    "summary": "Someone listed a massive 300-rack AI supercomputer on eBay for $59.7M. Packed with 9,600 A100 GPUs and 4,200 EPYC CPUs, it even ships for free."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/sound-cards/usd4-700-audiophile-grade-network-hub-promises-a-noise-free-experience-and-music-with-emotional-impact-seven-isolation-stages-per-port-were-chosen-with-listening-comparisons",
    "domain": "AI 算力 / 半导体",
    "title": "$4,700 audiophile-grade network hub promises a noise-free experience and music with 'emotional impact'",
    "url": "https://www.tomshardware.com/pc-components/sound-cards/usd4-700-audiophile-grade-network-hub-promises-a-noise-free-experience-and-music-with-emotional-impact-seven-isolation-stages-per-port-were-chosen-with-listening-comparisons",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T10:00:00+00:00",
    "summary": "$4,700 audiophile-grade network hub promises a noise-free experience and music with \"emotional impact.\" Seven isolation stages per port were chosen with \"listening comparisons\""
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/robotics/japan-experiments-with-autonomous-ai-chainsaw-wielding-robots-video-shows-rail-truck-mounted-metal-humanoid-cutting-down-tree-branches",
    "domain": "AI 算力 / 半导体",
    "title": "Japan experiments with autonomous AI chainsaw-wielding robots",
    "url": "https://www.tomshardware.com/tech-industry/robotics/japan-experiments-with-autonomous-ai-chainsaw-wielding-robots-video-shows-rail-truck-mounted-metal-humanoid-cutting-down-tree-branches",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T09:40:00+00:00",
    "summary": "A scary-looking humanoid robot with a chainsaw arm was shown in action on Japanese TV news trimming tree branches that had begun encroaching on railway lines."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/fields-medal-winning-uc-berkeley-professor-ends-graded-homework-due-to-ai-cheating-says-in-person-exams-are-the-only-solution-left-to-widespread-ai-use",
    "domain": "AI 算力 / 半导体",
    "title": "Fields Medal-winning UC Berkeley professor ends graded homework due to AI cheating",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/fields-medal-winning-uc-berkeley-professor-ends-graded-homework-due-to-ai-cheating-says-in-person-exams-are-the-only-solution-left-to-widespread-ai-use",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T20:09:05+00:00",
    "summary": "Award-winning mathematician Richard Brocherds says that it's a waste of time and money to grade AI answers, so he now only uses in-person exams to see how well his students are doing in his classes."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/military-drone-outfit-anduril-partners-with-qualcomm-to-build-laptops-on-us-soil-with-new-bluechip-venture-defense-contractor-targets-a-100-percent-domestic-supply-chain-in-the-future",
    "domain": "AI 算力 / 半导体",
    "title": "Military drone outfit Anduril partners with Qualcomm to build laptops on US soil with new BlueChip venture",
    "url": "https://www.tomshardware.com/laptops/military-drone-outfit-anduril-partners-with-qualcomm-to-build-laptops-on-us-soil-with-new-bluechip-venture-defense-contractor-targets-a-100-percent-domestic-supply-chain-in-the-future",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T17:42:49+00:00",
    "summary": "The defense contractor aims to fully bring back laptop manufacturing on U.S. shores, with its first BlueChip laptop prototypes having 90% procurement cost coming from suppliers in the U.S. and other a"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/israeli-ad-tech-firm-tied-to-suspected-starlink-tracking-effort-report-claims-researchers-say-it-outbid-everyone-for-starlink-linked-ads-in-100-countries-including-where-the-service-is-banned",
    "domain": "AI 算力 / 半导体",
    "title": "Israeli ad tech firm tied to suspected Starlink tracking effort, report claims",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/israeli-ad-tech-firm-tied-to-suspected-starlink-tracking-effort-report-claims-researchers-say-it-outbid-everyone-for-starlink-linked-ads-in-100-countries-including-where-the-service-is-banned",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T17:37:00+00:00",
    "summary": "Citizen Lab and Confiant linked Israeli firm Discover-Tech to suspected surveillance through online advertising. Researchers said its ads appeared across nearly 200,000 websites and mobile apps. Trend"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tsmc-reportedly-weighs-20-percent-cowos-price-increase-as-nvidia-blackwell-and-rubin-chips-put-pressure-on-packaging-capacity-equipment-lead-times-stretch-to-eight-months",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC reportedly weighs 20% CoWoS price increase as Nvidia Blackwell and Rubin chips put pressure on packaging capacity",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-reportedly-weighs-20-percent-cowos-price-increase-as-nvidia-blackwell-and-rubin-chips-put-pressure-on-packaging-capacity-equipment-lead-times-stretch-to-eight-months",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T14:30:00+00:00",
    "summary": "TSMC is reportedly weighing a price increase of up to 20% for its CoWoS advanced packaging technology as Nvidia’s Blackwell and upcoming Rubin chips intensify pressure on capacity. Equipment deliverie"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/external-ssds/samsung-portable-ssd-p9-review",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung Portable SSD P9 review: speedy USB4 in a slim, pricey package",
    "url": "https://www.tomshardware.com/pc-components/external-ssds/samsung-portable-ssd-p9-review",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T14:00:00+00:00",
    "summary": "Samsung’s Portable SSD P9 is the new USB4 external drive to beat. It feels premium and performed very well in our testing. But you’ll have to pay a lot for it, or any similarly performing drive, these"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/police-reportedly-pulling-motorists-over-because-ai-algorithms-deem-their-driving-patterns-suspicious-rights-group-report-warns-ai-surveillance-systems-will-sweep-in-more-innocent-people-than-wrongdoers",
    "domain": "AI 算力 / 半导体",
    "title": "Police are reportedly pulling motorists over because AI algorithms deem their driving patterns 'suspicious'",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/police-reportedly-pulling-motorists-over-because-ai-algorithms-deem-their-driving-patterns-suspicious-rights-group-report-warns-ai-surveillance-systems-will-sweep-in-more-innocent-people-than-wrongdoers",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T13:53:32+00:00",
    "summary": "An ACLU report claims police are increasingly using AI to analyze license plate-reader data and flag motorists based on travel patterns, raising concerns that innocent drivers could be pulled over bec"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/walmart-slashes-usd750-off-this-msi-gaming-laptop-16-inch-crosshair-sports-an-rtx-5060-gpu-and-a-fast-240hz-qhd-display",
    "domain": "AI 算力 / 半导体",
    "title": "Walmart slashes $750 off this MSI RTX 5060 gaming laptop",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/walmart-slashes-usd750-off-this-msi-gaming-laptop-16-inch-crosshair-sports-an-rtx-5060-gpu-and-a-fast-240hz-qhd-display",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T13:47:15+00:00",
    "summary": "A massive $750 discount at Walmart brings the price of MSI's Crosshair gaming laptop crashing down. RTX 5060 graphics and a bright 240Hz IPS display are just two of the standout features of this lapto"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/mechanical-keyboards/keybytes-truly-modular-keyboard-starts-with-one-key-and-is-assembled-like-legos-each-magnetic-key-module-has-its-own-risc-v-microcontroller-for-the-ultimate-in-customizability",
    "domain": "AI 算力 / 半导体",
    "title": "Keybytes ‘truly modular keyboard’ starts with one key and is assembled like Legos",
    "url": "https://www.tomshardware.com/peripherals/mechanical-keyboards/keybytes-truly-modular-keyboard-starts-with-one-key-and-is-assembled-like-legos-each-magnetic-key-module-has-its-own-risc-v-microcontroller-for-the-ultimate-in-customizability",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T13:34:43+00:00",
    "summary": "The modular Keybytes project combines a Keyword hub that is magnetically connected to Keybit keys, with each key having its own microcontroller."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/apple-adds-m6-to-14-inch-macbook-pro-and-imac-starts-at-usd1-999",
    "domain": "AI 算力 / 半导体",
    "title": "Apple adds M6 to 14-inch MacBook Pro and iMac",
    "url": "https://www.tomshardware.com/laptops/macbooks/apple-adds-m6-to-14-inch-macbook-pro-and-imac-starts-at-usd1-999",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T13:28:23+00:00",
    "summary": "Apple updated its 14-inch MacBook Pro and iMac lineup with the M6 chip."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/hacker-awarded-usd50k-bounty-for-reporting-bug-to-sony-that-allowed-ps5-linux-exploit-move-sparks-backlash-from-jailbreaking-community",
    "domain": "AI 算力 / 半导体",
    "title": "Hacker awarded $50k bounty for reporting bug to Sony that allowed PS5 Linux exploit",
    "url": "https://www.tomshardware.com/video-games/playstation/hacker-awarded-usd50k-bounty-for-reporting-bug-to-sony-that-allowed-ps5-linux-exploit-move-sparks-backlash-from-jailbreaking-community",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T13:22:04+00:00",
    "summary": "The hypervisor bug that allowed PS5 users to install Linux on their consoles was patched before the launch of GTA VI, meaning they have to choose between experimenting with Linux and running the game."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/open3dlab-accuses-roblox-of-downloading-145gb-of-3d-assets-for-ai-training-purposes-automated-crawler-ignored-site-rules-to-grab-over-1-000-files-including-adult-content-during-scraping-spree",
    "domain": "AI 算力 / 半导体",
    "title": "Roblox accused of downloading 145GB of 3D assets, including adult content, for AI training purposes during scraping spree",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/open3dlab-accuses-roblox-of-downloading-145gb-of-3d-assets-for-ai-training-purposes-automated-crawler-ignored-site-rules-to-grab-over-1-000-files-including-adult-content-during-scraping-spree",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T12:26:13+00:00",
    "summary": "Independent 3D modeling community Open3DLab has publicly claimed that a web crawler, attributed to Roblox, downloaded 145.5GB of its data, for what it assumes is for AI training purposes."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/intels-apx-offers-better-performance-in-windows-11-according-to-new-insider-setting-microsoft-begins-early-enablement-for-advanced-performance-extensions-on-nova-lake-cpus",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's APX offers 'better performance' in Windows 11 according to new Insider setting",
    "url": "https://www.tomshardware.com/software/windows/intels-apx-offers-better-performance-in-windows-11-according-to-new-insider-setting-microsoft-begins-early-enablement-for-advanced-performance-extensions-on-nova-lake-cpus",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T11:30:00+00:00",
    "summary": "Microsoft has begun testing the option to enable Intel's Advanced Performance Extensions, or APX, which will bring a performance boost to some apps — although no chips with APX support are available a"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-32gb-of-ddr5-ram-for-just-usd151-in-this-4-in-1-newegg-bundle-with-the-9800x3d-and-a-2tb-ssd-start-building-a-high-end-4k-gaming-pc-with-this-combo-deal-that-also-includes-an-am5-gigabyte-motherboard-and-a-free-msi-aio-liquid-cooler",
    "domain": "AI 算力 / 半导体",
    "title": "Grab 32GB of DDR5 RAM for just $151 in this 4-in-1 Newegg bundle with the 9800X3D and a 2TB SSD",
    "url": "https://www.tomshardware.com/pc-components/grab-32gb-of-ddr5-ram-for-just-usd151-in-this-4-in-1-newegg-bundle-with-the-9800x3d-and-a-2tb-ssd-start-building-a-high-end-4k-gaming-pc-with-this-combo-deal-that-also-includes-an-am5-gigabyte-motherboard-and-a-free-msi-aio-liquid-cooler",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T11:11:37+00:00",
    "summary": "Grab the 9800X3D with a matching Gigabyte motherboard, 32GB of DDR5 RAM, and a 2TB SSD, all for just $1,180.99, giving you a $358.98 discount that makes the equivalent RAM price just $151."
  },
  {
    "id": "rss:https://www.eetimes.com/quantum-computing-energy-bill-is-coming-and-we-havent-priced-it-in/",
    "domain": "AI 算力 / 半导体",
    "title": "Quantum Computing’s Energy Bill Is Coming, and We Haven’t Priced It In",
    "url": "https://www.eetimes.com/quantum-computing-energy-bill-is-coming-and-we-havent-priced-it-in/",
    "source": "Matt Rijlaarsdam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T09:05:54+00:00",
    "summary": "Quantum computing’s future depends on measuring useful processing power against energy consumption and cost, not just qubit counts. The post Quantum Computing’s Energy Bill Is Coming, and We Haven’t P"
  },
  {
    "id": "rss:https://www.eetimes.com/using-a-single-image-to-optimize-urban-solar-panel-orientation/",
    "domain": "AI 算力 / 半导体",
    "title": "Using a Single Image to Optimize Urban Solar-Panel Orientation",
    "url": "https://www.eetimes.com/using-a-single-image-to-optimize-urban-solar-panel-orientation/",
    "source": "Bill Schweber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T22:00:00+00:00",
    "summary": "Getting the most power from an urban-sited panel requires deep understanding of its surroundings. The post Using a Single Image to Optimize Urban Solar-Panel Orientation appeared first on EE Times."
  },
  {
    "id": "hn:50128597",
    "domain": "AI 算力 / 半导体",
    "title": "EU negotiates sanctions swap with China to rescue critical ASML supplier",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/eu-negotiates-sanction-swap-with-china-to-rescue-critical-asml-supplier-german-coatings-firm-faces-shutdown-without-chinese-rare-earths",
    "source": "anigbrowl",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-17T06:49:52+00:00",
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
    "points": 1467,
    "published_at": "2026-10-13T16:03:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50261319",
    "domain": "大厂 AI 动态",
    "title": "Genie 4",
    "url": "https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/",
    "source": "acossta",
    "platform": "hackernews",
    "points": 1029,
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
    "points": 931,
    "published_at": "2026-10-28T17:01:23+00:00",
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
    "points": 235,
    "published_at": "2026-10-13T16:55:47+00:00",
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
    "id": "rss:https://www.theverge.com/policy/1021554/anduril-bluechip-65-percent-domestic-buy-american",
    "domain": "大厂 AI 动态",
    "title": "Anduril now says its BlueChip laptop will meet Buy American standards at launch",
    "url": "https://www.theverge.com/policy/1021554/anduril-bluechip-65-percent-domestic-buy-american",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T02:22:46+00:00",
    "summary": "On Tuesday, defense contractor Anduril and chipmaker Qualcomm announced a partnership to build laptops entirely in the United States, starting with a single model in 2027. They also announced a \"long-"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1021644/adam-mosseri-instagram-ai-negativity",
    "domain": "大厂 AI 动态",
    "title": "Adam Mosseri says negativity around AI is ‘going to get worse’",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1021644/adam-mosseri-instagram-ai-negativity",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T23:05:39+00:00",
    "summary": "Asked about AI and the trend of college students booing tech CEOs at graduation ceremonies, Instagram head Adam Mosseri acknowledged in an interview that a lot of people really don't like AI, and it's"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1021528/ice-cbp-data-leak",
    "domain": "大厂 AI 动态",
    "title": "A hacker stole more than 40,000 DHS employee records",
    "url": "https://www.theverge.com/tech/1021528/ice-cbp-data-leak",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T21:57:45+00:00",
    "summary": "A hacker stole a trove of personal information from the Department of Homeland Security (DHS). The breach exposes the names, job titles, phone numbers, email addresses, and office locations of more th"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1021405/akai-open-source-mpc-sample-key",
    "domain": "大厂 AI 动态",
    "title": "Akai is embracing vibe-coded mods with an open-source MPC",
    "url": "https://www.theverge.com/gadgets/1021405/akai-open-source-mpc-sample-key",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T21:34:04+00:00",
    "summary": "The MPC Sample Key isn't even formally announced yet, but Akai is already showing off what the modding community is cooking up through vibe coding. Akai has decided to embrace the explosion of hackers"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1020264/readwise-books-launch-ebook-store",
    "domain": "大厂 AI 动态",
    "title": "Readwise is taking on Kindle and Kobo for ebook supremacy",
    "url": "https://www.theverge.com/tech/1020264/readwise-books-launch-ebook-store",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T21:16:18+00:00",
    "summary": "For the last several years, Readwise has been building tools for power readers. There's the eponymous product, Readwise, which stores and categorizes your Kindle highlights to help you remember what y"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1020811/alphabet-google-earnings-q3-2026",
    "domain": "大厂 AI 动态",
    "title": "Google says its investments in AI are driving more searches",
    "url": "https://www.theverge.com/tech/1020811/alphabet-google-earnings-q3-2026",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T20:22:26+00:00",
    "summary": "Google parent company Alphabet says that its AI investments are leading to a big growth in searches year-over-year, as noted in its Q3 2026 earnings today. \"Our AI investments are driving overall Sear"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1020785/microsoft-earnings-revenue-q1-2027",
    "domain": "大厂 AI 动态",
    "title": "Microsoft reveals strong cloud growth amid financial reporting overhaul",
    "url": "https://www.theverge.com/tech/1020785/microsoft-earnings-revenue-q1-2027",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T20:20:00+00:00",
    "summary": "Microsoft just posted the first quarter of its 2027 fiscal financial results. The software maker made $92.3 billion in revenue and a net income of $33.6 billion during Q1. Revenue is up 19 percent, an"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1021308/apple-touchscreen-macbook-pro-proled-xdr-fully-specced",
    "domain": "大厂 AI 动态",
    "title": "Apple charges $14,549 for a fully specced touchscreen MacBook Pro",
    "url": "https://www.theverge.com/tech/1021308/apple-touchscreen-macbook-pro-proled-xdr-fully-specced",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T20:12:44+00:00",
    "summary": "With an OLED display and touchscreen capabilities, it's no surprise that the new MacBook Pro Apple announced today is more expensive than the MBP announced earlier this year. But upgrading the base mo"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1021339/google-gemini-4-carbon-cybersecurity-frontier",
    "domain": "大厂 AI 动态",
    "title": "Google launches Gemini 4 Carbon with a ‘significant leap’ in cybersecurity",
    "url": "https://www.theverge.com/tech/1021339/google-gemini-4-carbon-cybersecurity-frontier",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T20:03:00+00:00",
    "summary": "Google has released its latest frontier model, Gemini 4 Carbon, offering \"significant gains\" in coding, agentic tasks, and cybersecurity. In an announcement on Wednesday, Google highlights Carbon's to"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1019851/fcc-foreign-gadget-ban-drone-robot-roomba-storystream",
    "domain": "大厂 AI 动态",
    "title": "Foreign gadget bans: all the news about the FCC’s clampdown on Chinese tech",
    "url": "https://www.theverge.com/policy/1019851/fcc-foreign-gadget-ban-drone-robot-roomba-storystream",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T19:37:31+00:00",
    "summary": "What do drones, routers, and Roombas have in common? The US government wants to keep Chinese ones from entering the country. They’re the first consumer gadgets that are facing de facto import bans bec"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/upwind-raises-400m-after-walking-away-from-datadog-acquisition-offer/",
    "domain": "大厂 AI 动态",
    "title": "Upwind raises $400M after walking away from Datadog acquisition offer",
    "url": "https://techcrunch.com/2026/10/28/upwind-raises-400m-after-walking-away-from-datadog-acquisition-offer/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T23:15:00+00:00",
    "summary": "The cloud security startup raised a Series C at a $3.8B valuation, instead of selling itself for the same price."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/apples-touchscreen-macbook-pro-pushes-laptop-pricing-to-a-new-extreme/",
    "domain": "大厂 AI 动态",
    "title": "Apple’s touchscreen MacBook Pro pushes laptop pricing to a new extreme",
    "url": "https://techcrunch.com/2026/10/28/apples-touchscreen-macbook-pro-pushes-laptop-pricing-to-a-new-extreme/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T22:47:50+00:00",
    "summary": "Prepare to cough up around $14,549 if you want the new touchscreen MacBook Pro to have every upgrade."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/microsoft-just-shared-azures-actual-revenue-in-dollars-33-2-billion/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft just shared Azure’s actual revenue in dollars: $33.2 billion",
    "url": "https://techcrunch.com/2026/10/28/microsoft-just-shared-azures-actual-revenue-in-dollars-33-2-billion/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T21:58:32+00:00",
    "summary": "Microsoft has never disclosed Azure's quarterly revenue in dollars. But for the first time, we can see just how close it is getting to besting the biggest competitor in the market, AWS."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/google-expands-ai-search-ads-globally-as-core-ad-growth-slows/",
    "domain": "大厂 AI 动态",
    "title": "Google expands AI Search ads globally as core ad growth slows",
    "url": "https://techcrunch.com/2026/10/28/google-expands-ai-search-ads-globally-as-core-ad-growth-slows/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T21:48:37+00:00",
    "summary": "The announcement came alongside parent company Alphabet's third-quarter earnings report, which saw revenue grow 25% year over year to $127.6 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/microsoft-recorded-10-billion-in-revenue-from-openai/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft recorded $10 billion in revenue from OpenAI",
    "url": "https://techcrunch.com/2026/10/28/microsoft-recorded-10-billion-in-revenue-from-openai/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T21:34:30+00:00",
    "summary": "Microsoft said it made $10 billion in revenue from commercial arrangements with OpenAI, including revenue-sharing payments, in the quarter ending September 30. It underscores the still-enormous financ"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/microsoft-hits-10-quarters-of-record-breaking-revenue-in-a-row/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft hits 10 quarters of record-breaking revenue in a row",
    "url": "https://techcrunch.com/2026/10/28/microsoft-hits-10-quarters-of-record-breaking-revenue-in-a-row/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T21:25:30+00:00",
    "summary": "Whatever the future of AI might be, the current situation is still very good for Microsoft. The tech giant reported yet another record for quarterly revenue on Wednesday: $92.3 billion, a 19% increase"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/hacker-stole-personnel-data-about-thousands-of-homeland-security-employees-including-cbp-and-ice-agents/",
    "domain": "大厂 AI 动态",
    "title": "Hacker stole personnel data about thousands of Homeland Security employees, including CBP and ICE agents",
    "url": "https://techcrunch.com/2026/10/28/hacker-stole-personnel-data-about-thousands-of-homeland-security-employees-including-cbp-and-ice-agents/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T20:01:00+00:00",
    "summary": "A hacker obtained personally identifiable information about more than 40,000 Homeland Security staffers, which has since been published online."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/anthropic-just-launched-tools-to-show-companies-what-their-ai-spending-is-buying/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic just launched tools to show companies what their AI spending is buying",
    "url": "https://techcrunch.com/2026/10/28/anthropic-just-launched-tools-to-show-companies-what-their-ai-spending-is-buying/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T19:19:58+00:00",
    "summary": "The frontier lab is lifting the curtain on how users spend money on its models ahead of a planned IPO."
  },
  {
    "id": "rss:https://techcrunch.com/video/wizs-cto-on-php2shell-and-the-coming-vulnpocalypse/",
    "domain": "大厂 AI 动态",
    "title": "Wiz’s CTO on PHP2Shell and the coming ‘vulnpocalypse’",
    "url": "https://techcrunch.com/video/wizs-cto-on-php2shell-and-the-coming-vulnpocalypse/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T19:05:46+00:00",
    "summary": "The PHP scare may have faded from your feed, but the cleanup is far from over. Last week, two critical bugs in the open source language behind roughly 70% of websites left organizations scrambling to "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/apple-launches-its-new-touchscreen-macbook-pro/",
    "domain": "大厂 AI 动态",
    "title": "Apple launches its new touchscreen MacBook Pro",
    "url": "https://techcrunch.com/2026/10/28/apple-launches-its-new-touchscreen-macbook-pro/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T17:26:10+00:00",
    "summary": "Apple's new touchscreen MacBook Pro starts at $2,899."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/xreal-aura-is-a-new-wired-headset-powered-by-android-xr/",
    "domain": "大厂 AI 动态",
    "title": "Xreal Aura is a new wired headset powered by Android XR",
    "url": "https://techcrunch.com/2026/10/28/xreal-aura-is-a-new-wired-headset-powered-by-android-xr/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T17:00:00+00:00",
    "summary": "Xreal Aura will start at $1,279 and will have multiple XR specific apps at launch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/as-ai-agents-reshape-the-web-google-opens-gemini-and-search-to-more-apps/",
    "domain": "大厂 AI 动态",
    "title": "As AI agents reshape the web, Google opens Gemini and Search to more apps",
    "url": "https://techcrunch.com/2026/10/28/as-ai-agents-reshape-the-web-google-opens-gemini-and-search-to-more-apps/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T17:00:00+00:00",
    "summary": "A new developer platform will let businesses bring their services to Google's AI experiences, potentially changing how consumers discover and use apps."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/chromes-ai-powered-autofill-can-now-dig-through-your-gmail-to-fill-out-forms/",
    "domain": "大厂 AI 动态",
    "title": "Chrome’s AI-powered Autofill can now dig through your Gmail to fill out forms",
    "url": "https://techcrunch.com/2026/10/28/chromes-ai-powered-autofill-can-now-dig-through-your-gmail-to-fill-out-forms/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T17:00:00+00:00",
    "summary": "The autofill update lets Chrome pull flight confirmations, tracking info, order details, and other information from your inbox, with your permission."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/reddit-is-the-latest-platform-to-embrace-the-for-you-feed/",
    "domain": "大厂 AI 动态",
    "title": "Reddit is the latest platform to embrace the ‘For You’ feed",
    "url": "https://techcrunch.com/2026/10/28/reddit-is-the-latest-platform-to-embrace-the-for-you-feed/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T16:00:00+00:00",
    "summary": "The For You feed combines posts from communities users have joined with recommendations tailored to their interests."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/ai-execs-may-be-too-out-of-touch-to-build-for-the-general-public/",
    "domain": "大厂 AI 动态",
    "title": "AI execs may be too out of touch to build for the general public",
    "url": "https://techcrunch.com/2026/10/28/ai-execs-may-be-too-out-of-touch-to-build-for-the-general-public/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T15:53:52+00:00",
    "summary": "Tech leaders are flaunting how out of touch they are when they brag about using AI to connect with their families."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/trump-doe-loans-5b-to-nuclear-plants-that-will-power-data-centers/",
    "domain": "大厂 AI 动态",
    "title": "Trump DOE loans $5B to nuclear plants that will power data centers",
    "url": "https://techcrunch.com/2026/10/28/trump-doe-loans-5b-to-nuclear-plants-that-will-power-data-centers/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T15:53:21+00:00",
    "summary": "Constellation Energy will get $5 billion in government loans to modernize nuclear reactors. Most of the new capacity is already committed to Google, Amazon, and Meta."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/south-koreas-financial-industry-hit-by-fresh-wave-of-cyberattacks/",
    "domain": "大厂 AI 动态",
    "title": "South Korea’s financial industry hit by fresh wave of cyberattacks",
    "url": "https://techcrunch.com/2026/10/28/south-koreas-financial-industry-hit-by-fresh-wave-of-cyberattacks/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T15:41:18+00:00",
    "summary": "South Korea’s financial institutions have been hit by another wave of cyberattacks, highlighting the growing risk of AI-driven hacking in Asia."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/voice-ai-in-vogue-nvidia-releases-new-open-transcription-model/",
    "domain": "大厂 AI 动态",
    "title": "Voice AI in vogue: Nvidia releases new open transcription model",
    "url": "https://techcrunch.com/2026/10/28/voice-ai-in-vogue-nvidia-releases-new-open-transcription-model/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T15:00:00+00:00",
    "summary": "Nvidia just released a free speech-to-text model that can transcribe up to 40 languages, but it only works on recordings, not live audio, so it’s a big step for meeting and medical transcription tools"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/amazon-debuts-the-alexa-photo-frame-and-echo-time-smart-clock-plus-other-upgraded-devices/",
    "domain": "大厂 AI 动态",
    "title": "Amazon debuts the Alexa Photo Frame and Echo Time smart clock, plus other upgraded devices",
    "url": "https://techcrunch.com/2026/10/28/amazon-debuts-the-alexa-photo-frame-and-echo-time-smart-clock-plus-other-upgraded-devices/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T14:34:25+00:00",
    "summary": "Amazon's other new devices include an upgraded Echo Dot, an Echo Studio with visual intelligence features, and the Echo Show 16."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/28/tiktok-expands-into-restaurant-guides-with-must-eat-feature/",
    "domain": "大厂 AI 动态",
    "title": "TikTok expands into restaurant guides with ‘Must Eat’ feature",
    "url": "https://techcrunch.com/2026/10/28/tiktok-expands-into-restaurant-guides-with-must-eat-feature/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T14:26:36+00:00",
    "summary": "The move puts TikTok in more direct competition with platforms like Yelp and Google."
  },
  {
    "id": "rss:https://stratechery.com/2026/meta-earnings-muse-and-the-frontier-musebook/",
    "domain": "大厂 AI 动态",
    "title": "Meta Earnings, Muse and the Frontier, Musebook",
    "url": "https://stratechery.com/2026/meta-earnings-muse-and-the-frontier-musebook/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T10:06:13+00:00",
    "summary": "Meta's earnings come in the context of Zuckerberg delivering on his promise; if investors believe in Muse they must support Meta's spending on compute."
  },
  {
    "id": "rss:https://stratechery.com/2026/anthropic-s-1-the-cost-of-compute-who-is-paying/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic S-1, The Cost of Compute, Who Is Paying?",
    "url": "https://stratechery.com/2026/anthropic-s-1-the-cost-of-compute-who-is-paying/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T10:32:57+00:00",
    "summary": "Anthropic's IPO is finally here; the core business is very profitable, but competition may eat all of the profits, even as investors are set up for endless dilution."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/10/ulas-vulcan-rocket-is-set-to-return-to-flight-on-friday-the-13th/",
    "domain": "大厂 AI 动态",
    "title": "ULA's Vulcan rocket is set to return to flight on Friday the 13th",
    "url": "https://arstechnica.com/space/2026/10/ulas-vulcan-rocket-is-set-to-return-to-flight-on-friday-the-13th/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T22:51:15+00:00",
    "summary": "This Vulcan launch will be the first to utilize a full complement of six solid rocket boosters."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/as-us-ties-fray-europe-plans-first-undersea-cable-link-to-greenland/",
    "domain": "大厂 AI 动态",
    "title": "As US ties fray, Europe plans first undersea cable link to Greenland",
    "url": "https://arstechnica.com/gadgets/2026/10/as-us-ties-fray-europe-plans-first-undersea-cable-link-to-greenland/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T22:35:50+00:00",
    "summary": "Europe's Pan-Arctic Cable will bypass US to link Canada, Japan, and South Korea."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/10/peptide-peddlers-cheer-as-rfk-jr-unilaterally-grants-access-overruling-fda/",
    "domain": "大厂 AI 动态",
    "title": "Peptide peddlers cheer as RFK Jr. unilaterally grants access, overruling FDA",
    "url": "https://arstechnica.com/health/2026/10/peptide-peddlers-cheer-as-rfk-jr-unilaterally-grants-access-overruling-fda/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T22:17:15+00:00",
    "summary": "Six unproven peptides popular with MAHA now under \"enforcement discretion policy.\""
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/10/trump-admin-sues-utah-to-save-kalshi-from-the-states-total-ban-on-gambling/",
    "domain": "大厂 AI 动态",
    "title": "Trump admin sues Utah to save Kalshi from the state's total ban on gambling",
    "url": "https://arstechnica.com/tech-policy/2026/10/trump-admin-sues-utah-to-save-kalshi-from-the-states-total-ban-on-gambling/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T19:30:33+00:00",
    "summary": "US agency has sued 10 states for trying to stop gambling on prediction markets."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/10/the-last-best-hope-for-space-tourism-just-rolled-onto-a-runway-in-arizona/",
    "domain": "大厂 AI 动态",
    "title": "The last, best hope for space tourism just rolled onto a runway in Arizona",
    "url": "https://arstechnica.com/space/2026/10/the-last-best-hope-for-space-tourism-just-rolled-onto-a-runway-in-arizona/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T19:20:36+00:00",
    "summary": "It has been nearly a year since any space tourism flights occurred."
  },
  {
    "id": "rss:https://arstechnica.com/apple/2026/10/touchscreen-macbook-pro-hands-on-oled-looks-great-on-a-mac/",
    "domain": "大厂 AI 动态",
    "title": "Touchscreen MacBook Pro hands-on: OLED looks great on a Mac",
    "url": "https://arstechnica.com/apple/2026/10/touchscreen-macbook-pro-hands-on-oled-looks-great-on-a-mac/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T19:10:29+00:00",
    "summary": "It's not as different from the previous model as you might have expected."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/10/google-announces-gemini-4-carbon-its-latest-frontier-ai-model-that-you-cant-use/",
    "domain": "大厂 AI 动态",
    "title": "Google announces Gemini 4 Carbon, its latest frontier AI model that you can't use",
    "url": "https://arstechnica.com/ai/2026/10/google-announces-gemini-4-carbon-its-latest-frontier-ai-model-that-you-cant-use/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T18:47:27+00:00",
    "summary": "Gemini 4 Carbon is essentially a slightly better version of Argon."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/amazon-adds-a-camera-to-its-best-sounding-smart-speaker-for-30-extra/",
    "domain": "大厂 AI 动态",
    "title": "Amazon turns its most capable smart speaker into a smart camera, too",
    "url": "https://arstechnica.com/gadgets/2026/10/amazon-adds-a-camera-to-its-best-sounding-smart-speaker-for-30-extra/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T18:05:22+00:00",
    "summary": "The Echo Studio with Home Camera can \"see and understand what's in front of the camera.\""
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/10/cadillac-escalade-iq-review-4-tons-of-electric-american-luxury-on-wheels/",
    "domain": "大厂 AI 动态",
    "title": "Cadillac Escalade IQ review: Huge battery, huge range, huge SUV",
    "url": "https://arstechnica.com/cars/2026/10/cadillac-escalade-iq-review-4-tons-of-electric-american-luxury-on-wheels/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T17:55:45+00:00",
    "summary": "With more than 200 kWh, this luxury three-row can go 460 miles on a charge."
  },
  {
    "id": "hn:50051583",
    "domain": "股票",
    "title": "Research Firm Calls Anthropic's IPO 'Unprecedented Test of Investor Gullibity'",
    "url": "https://www.cnbc.com/2026/10/07/anthropic-will-be-most-ridiculous-ipo-of-year-analyst-says.html",
    "source": "m463",
    "platform": "hackernews",
    "points": 244,
    "published_at": "2026-10-12T05:03:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50280197",
    "domain": "股票",
    "title": "Alphabet Announces Third Quarter 2026 Results [pdf]",
    "url": "https://s206.q4cdn.com/479360582/files/doc_financials/2026/q3/2026q3-alphabet-earnings-release.pdf",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 76,
    "published_at": "2026-10-28T20:11:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50232604",
    "domain": "股票",
    "title": "Microsoft and others tell crypto platform not to tokenize their stocks",
    "url": "https://gizmodo.com/microsoft-mcdonalds-verizon-and-others-tell-crypto-platform-not-to-tokenize-their-stocks-2000830368",
    "source": "gumby",
    "platform": "hackernews",
    "points": 100,
    "published_at": "2026-10-25T15:28:40+00:00",
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
    "id": "hn:50265525",
    "domain": "股票",
    "title": "In China, the AI bubble has burst",
    "url": "https://finance.yahoo.com/markets/stocks/articles/analysis-china-ai-bubble-already-120038616.html",
    "source": "smurda",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-10-27T20:44:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:50243343",
    "domain": "股票",
    "title": "Anthropic rushing IPO before AI bubble bursts",
    "url": "https://nypost.com/2026/10/23/business/wall-street-is-urging-anthropic-openai-to-do-their-ipos-in-a-hurry-heres-why/",
    "source": "nothrowaways",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-26T13:30:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50251762",
    "domain": "股票",
    "title": "Anthropic Is the Most Ridiculous IPO of 2026 [pdf]",
    "url": "https://www.newconstructs.com/wp-content/uploads/2026/10/Anthropic-Is-The-Most-Ridiculous-IPO-of-2026.pdf",
    "source": "simonebrunozzi",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-10-26T22:06:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50254255",
    "domain": "股票",
    "title": "Pentagon orders bases to plan for 90 days without the grid",
    "url": "https://fortune.com/2026/10/26/pentagon-fortress-bases-90-days-off-grid-uk-be-ready-stockpile/",
    "source": "russfink",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-27T03:02:29+00:00",
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
    "id": "hn:50210325",
    "domain": "股票",
    "title": "Built a site that teaches investing using the live market as the examples",
    "url": "https://www.stocksightfinance.com",
    "source": "kshitik",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-10-23T15:07:06+00:00",
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
    "id": "hn:50159963",
    "domain": "股票",
    "title": "Investors temper Anthropic IPO valuation expectations over growth slowdown",
    "url": "https://www.reuters.com/business/finance/investors-temper-anthropic-ipo-valuation-expectations-over-revenue-growth-2026-10-15/",
    "source": "xqcgrek2",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-20T00:49:40+00:00",
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
    "id": "hn:50046896",
    "domain": "股票",
    "title": "Nvidia-backed data centre firm Firmus scraps IPO as AI valuation concerns deepen",
    "url": "https://www.bbc.com/news/articles/ck9dzpw4ll8po",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-11T19:26:05+00:00",
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
    "points": 1645,
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
    "id": "hn:50260526",
    "domain": "金融",
    "title": "A $300B 'Debt Wall' Is Looming over Private-Equity Backed Companies",
    "url": "https://www.wsj.com/finance/investing/a-300-billion-debt-wall-is-looming-over-private-equity-backed-companies-d6359497",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 175,
    "published_at": "2026-10-27T15:09:27+00:00",
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
    "id": "hn:50274706",
    "domain": "金融",
    "title": "Tesla Semi catches fire on I-880",
    "url": "https://electrek.co/2026/10/28/tesla-semi-fire-i-880-hayward-no-crash/",
    "source": "metadat",
    "platform": "hackernews",
    "points": 94,
    "published_at": "2026-10-28T14:54:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:50239430",
    "domain": "金融",
    "title": "Tesla cancels Cybertruck in Australia and NZ after 7 years of deposits",
    "url": "https://electrek.co/2026/10/23/tesla-cancels-cybertruck-australia-new-zealand/",
    "source": "MilnerRoute",
    "platform": "hackernews",
    "points": 97,
    "published_at": "2026-10-26T05:13:15+00:00",
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
    "id": "hn:50194602",
    "domain": "金融",
    "title": "Full Disk Encryption on Fedora with TPM2",
    "url": "https://www.apalrd.net/posts/2026/ent_luks/",
    "source": "speckx",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-10-22T12:46:40+00:00",
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
    "id": "hn:50159683",
    "domain": "金融",
    "title": "Trump Appointees Asked a Federal Agency to Acquire a Voting Machine and Hack It",
    "url": "https://www.propublica.org/article/cisa-election-security-donald-trump",
    "source": "soundworlds",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-10-20T00:09:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50152041",
    "domain": "金融",
    "title": "Federal judge rules Flock violated the fourth amendment",
    "url": "https://twitter.com/scotus_wire/status/2106487374624514071",
    "source": "vessenes",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-10-19T13:14:41+00:00",
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
