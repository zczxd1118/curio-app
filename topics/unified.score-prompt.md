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

- 今日日期：`2026-10-21`
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
  "date": "2026-10-21",
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
    "points": 3354398,
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
    "points": 2128843,
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
    "points": 2005442,
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
    "points": 1420844,
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
    "points": 1371580,
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
    "points": 1257069,
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
    "points": 902531,
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
    "points": 866199,
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
    "points": 724362,
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
    "points": 593481,
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
    "points": 425458,
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
    "points": 423606,
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
    "points": 359010,
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
    "points": 356903,
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
    "points": 328286,
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
    "points": 311104,
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
    "points": 282618,
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
    "points": 211936,
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
    "points": 184324,
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
    "points": 163055,
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
    "points": 161328,
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
    "points": 160281,
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
    "points": 139455,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 84703,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 68858,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1f3J96AETa",
    "domain": "AI",
    "title": "Claude code四个阶段",
    "url": "http://www.bilibili.com/video/av117449504595834",
    "source": "程序员牛牛学长",
    "platform": "bilibili",
    "points": 66953,
    "published_at": "2026-10-19T10:55:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 49473,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV126pk6sETS",
    "domain": "AI",
    "title": "连 json都不会，进了福布斯团队。面试的时候才知道vibe coding是什么，两天后他给我发了offer。",
    "url": "http://www.bilibili.com/video/av117436686795057",
    "source": "揽星Celeste",
    "platform": "bilibili",
    "points": 30572,
    "published_at": "2026-10-14T01:35:05+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29852,
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
    "points": 29008,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 23727,
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
    "points": 22887,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22823,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV18KJX6mEiH",
    "domain": "AI",
    "title": "太炸裂了！Claude Code 3.0彻底杀疯了！",
    "url": "http://www.bilibili.com/video/av117450007911196",
    "source": "烟神殿殿主",
    "platform": "bilibili",
    "points": 21843,
    "published_at": "2026-10-16T10:04:56+00:00",
    "summary": "原视频链接：https://www.youtube.com/watch?v=8nh1dcH4uJU\n本视频为AI技术搬运翻译，使用AI智能移除原视频广告营销内容，旨在降低信息差，帮助大家了解海外最新AI动态。\n翻译：烟神殿API,模型gemini-3.8-flash\n配音：使用的时FishTTS官方接口配音"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 19277,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1g5nM6tEBf",
    "domain": "AI",
    "title": "DeepSeek V4.1 Flash 接入指南｜六大 Agent 工具一次配好",
    "url": "http://www.bilibili.com/video/av117459403150912",
    "source": "跟着小陈玩AI",
    "platform": "bilibili",
    "points": 15489,
    "published_at": "2026-10-18T02:13:56+00:00",
    "summary": "DeepSeek 发布 V4.1 Flash，跑分反超一众旗舰。本期实测把它接进 DeepSeek Harness、WorkBuddy、Kimi Code、小米 MIMO、ZCode、Codex、Claude Code 等工具，两种配置方法、模型名怎么填、哪里要避坑，一条视频全部讲清。"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 12886,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 11366,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1bBHm6MEG5",
    "domain": "AI",
    "title": "这绝对是b站讲的最好的Claude Code全套实战教程，手把手带你搞定国内环境安装配置，全程干货无废话！AI大模型/MCP/Skill/智能体/Agent",
    "url": "http://www.bilibili.com/video/av117402847155229",
    "source": "大模型饼饼",
    "platform": "bilibili",
    "points": 10994,
    "published_at": "2026-10-08T02:13:21+00:00",
    "summary": "这绝对是B站讲得最好的Claude Code全套实战教程！手把手带你搞定国内环境安装配置、基础操作、高阶实战技巧，课程不堆砌冗余理论，聚焦真实开发场景，带你吃透Claude Code核心能力，打通MCP、Skill与Agent智能体联动开发。不管你是想提升日常编码效率，还是入门AI智能体开发，这套教程都非常适合你，全程干货无废话！"
  },
  {
    "id": "bvid:BV1gJJB6kERk",
    "domain": "AI",
    "title": "【实操】claude稳定不封的方法",
    "url": "http://www.bilibili.com/video/av117457104672336",
    "source": "程序员大龙虾",
    "platform": "bilibili",
    "points": 10661,
    "published_at": "2026-10-17T16:10:46+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1Yhb66LEaF",
    "domain": "AI",
    "title": "3分钟，教你什么是vibe coding",
    "url": "http://www.bilibili.com/video/av117115000524101",
    "source": "开聊pro",
    "platform": "bilibili",
    "points": 10040,
    "published_at": "2026-08-18T06:12:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 8273,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "bvid:BV1xFJ26tEoG",
    "domain": "AI",
    "title": "AI产品经理作品集：Vibe Coding实操 ChatBI落地写进简历",
    "url": "http://www.bilibili.com/video/av117445360618053",
    "source": "AI产品经理PMGao",
    "platform": "bilibili",
    "points": 7174,
    "published_at": "2026-10-15T14:22:53+00:00",
    "summary": "有很多同学用过codex、claude code等就觉得有vibecoding经验了，很多同学其实站在一个使用AI的普通用户跟AI交流而已，还远远达不到作为AI产品经理的能力。所以这个实操案例系统化的讲解了企业级项目是如何通过vibecoding落地的详细步骤，这里面包括了产品规划+竞品分析+SDD开发规范+Harness+测试用例+测评+skill设计等等。\n\n这个实操结合企业级案例深度讲解，完"
  },
  {
    "id": "bvid:BV1UaYK6nEjP",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av117244419903051",
    "source": "茶子兀",
    "platform": "bilibili",
    "points": 6939,
    "published_at": "2026-09-10T02:39:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1wFpP6uE1s",
    "domain": "AI",
    "title": "【开源】让手机自己操作 App！手上的 ai Agent！GitHub开源安卓App推荐",
    "url": "http://www.bilibili.com/video/av117394643097499",
    "source": "补药满减哇",
    "platform": "bilibili",
    "points": 6748,
    "published_at": "2026-10-07T01:05:00+00:00",
    "summary": "开源安卓 AI Agent：RikkaHub Agent Pure\n它能「看懂」屏幕、自己操作各种 App，也能组队干活。\n\n⬇️ 下载 &amp; 源码（AGPL-3.0）\nhttps://github.com/wuyhong715/rikkahub-agent-pure\n\n▶ 本片讲两件事\n① 无障碍屏幕自动化：读控件树定位、实时决策，不是死坐标脚本\n② 专家团系统：每个专家有自己的模型/工具"
  },
  {
    "id": "bvid:BV1t9pt6JETF",
    "domain": "AI",
    "title": "Cursor vs Claude Code vs Codex哪个好？三大AI编程工具区别与选择指南",
    "url": "http://www.bilibili.com/video/av117411437090209",
    "source": "不管这么多",
    "platform": "bilibili",
    "points": 6008,
    "published_at": "2026-10-09T14:35:26+00:00",
    "summary": "三大编程工具要如何选？"
  },
  {
    "id": "bvid:BV1sM6xB5EEE",
    "domain": "AI",
    "title": "基于LabVIEW的AI Agent智能体实现教程",
    "url": "http://www.bilibili.com/video/av115993393238477",
    "source": "三易电子工作室",
    "platform": "bilibili",
    "points": 4734,
    "published_at": "2026-02-01T04:12:23+00:00",
    "summary": "基于LabVIEW的AI Agent智能体实现教程，made by 三易电子工作室。"
  },
  {
    "id": "bvid:BV1c2Ei6pEfW",
    "domain": "AI",
    "title": "首发 AI agent 接入音乐软件FLStudio完整教程--小白十分钟上手编曲",
    "url": "http://www.bilibili.com/video/av116731758516894",
    "source": "Melydic",
    "platform": "bilibili",
    "points": 3867,
    "published_at": "2026-06-12T09:30:00+00:00",
    "summary": "up制作的视频中的指令网站地址：FLStudio.hajimi8.ggff.net\n如有问题以及不会的，请在评论区问"
  },
  {
    "id": "bvid:BV1yEWw63EM2",
    "domain": "AI",
    "title": "2026 最新版】大佬亲授 Claude Code 全栈教程，从入门到精通全覆盖，小白 10 分钟上手，干货无废话，建议收藏！",
    "url": "http://www.bilibili.com/video/av117432844813498",
    "source": "绕着宇宙飞一圈",
    "platform": "bilibili",
    "points": 3545,
    "published_at": "2026-10-13T09:20:48+00:00",
    "summary": "求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！求三连！！！"
  },
  {
    "id": "bvid:BV1VkK4zcEas",
    "domain": "AI",
    "title": "mcp-server-chart",
    "url": "http://www.bilibili.com/video/av114729532002481",
    "source": "二师兄说AI",
    "platform": "bilibili",
    "points": 3147,
    "published_at": "2025-06-22T23:15:07+00:00",
    "summary": "MCP Server Chart 是由阿里 AntV 团队开发的可视化图表生成服务，支持 AI 工具自动生成 20 多种主流可视化图表，极大提升数据可视化的自动化和智能化能力。#MCP #AI工具 #图表生成 #AntV #可视化"
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
    "id": "rss:https://www.eetimes.com/innovasea-packs-long-life-electronics-into-fish-tags/",
    "domain": "AI 算力 / 半导体",
    "title": "Innovasea Packs Long-Life Electronics into Fish Tags",
    "url": "https://www.eetimes.com/innovasea-packs-long-life-electronics-into-fish-tags/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T22:06:10+00:00",
    "summary": "A company on Canada’s east coast is pushing acoustic telemetry toward lighter payloads and decade-scale deployments by treating energy, sensing, and animal welfare as a single systems problem. The pos"
  },
  {
    "id": "rss:https://www.eetimes.com/chris-lattner-ai-code-generation-doesnt-solve-software-engineering/",
    "domain": "AI 算力 / 半导体",
    "title": "Chris Lattner: AI Code Generation Doesn’t Solve Software Engineering",
    "url": "https://www.eetimes.com/chris-lattner-ai-code-generation-doesnt-solve-software-engineering/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T11:00:00+00:00",
    "summary": "AI can generate low-level code, but code generation is also making it harder to build and maintain the software ecosystems we need. The post Chris Lattner: AI Code Generation Doesn&#8217;t Solve Softw"
  },
  {
    "id": "rss:https://www.eetimes.com/how-singapore-connects-chip-research-startups-and-manufacturing/",
    "domain": "AI 算力 / 半导体",
    "title": "How Singapore Connects Chip Research, Startups, and Manufacturing",
    "url": "https://www.eetimes.com/how-singapore-connects-chip-research-startups-and-manufacturing/",
    "source": "Susan Hong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T10:55:00+00:00",
    "summary": "From SiC power devices to silicon photonics, Singapore is building the infrastructure and industrial partnerships needed to bring deep-tech research to market. The post How Singapore Connects Chip Res"
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
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/amds-fsr-4-1-now-works-on-radeon-rx-6000-gpus-xbox-series-x-and-s-and-ryzen-ai-max-ai-9-and-z2-socs-new-release-brings-cutting-edge-tech-to-older-hardware-with-a-small-performance-cost",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's FSR 4.1 now works on Radeon RX 6000 cards, Xbox Series X and S, and Ryzen AI Max, AI 9, and Z2 SoCs",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/amds-fsr-4-1-now-works-on-radeon-rx-6000-gpus-xbox-series-x-and-s-and-ryzen-ai-max-ai-9-and-z2-socs-new-release-brings-cutting-edge-tech-to-older-hardware-with-a-small-performance-cost",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T17:47:35+00:00",
    "summary": "AMD has released a version of its cutting-edge FSR 4.1 upscaler that now works on Radeon RX 6000 GPUs, Xbox Series X and Series S consoles, and Ryzen AI Max, AI 9, and Z2 chips."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/tp-link-proposes-usd1-billion-us-wi-fi-router-manufacturing-alliance-with-key-tronic-potential-deal-seeks-to-end-ongoing-saga-blocking-its-wi-fi-8-products-from-american-homes",
    "domain": "AI 算力 / 半导体",
    "title": "TP-Link proposes $1 billion US Wi-Fi router manufacturing alliance with Key Tronic",
    "url": "https://www.tomshardware.com/networking/routers/tp-link-proposes-usd1-billion-us-wi-fi-router-manufacturing-alliance-with-key-tronic-potential-deal-seeks-to-end-ongoing-saga-blocking-its-wi-fi-8-products-from-american-homes",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T16:25:55+00:00",
    "summary": "TP-Link is at the mercy of the FCC regarding its ready-to-go Wi-Fi 8 routers, so it has a sweetener in mind to move things along."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/mysterious-amd-zen-6-apu-with-24gb-of-lpddr5-memory-appears-in-benchmarks-chip-may-be-for-next-gen-steam-deck-or-gaming-handhelds",
    "domain": "AI 算力 / 半导体",
    "title": "Mysterious AMD Zen 6 APU with 24GB of LPDDR5 memory appears in benchmarks",
    "url": "https://www.tomshardware.com/pc-components/cpus/mysterious-amd-zen-6-apu-with-24gb-of-lpddr5-memory-appears-in-benchmarks-chip-may-be-for-next-gen-steam-deck-or-gaming-handhelds",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T13:59:43+00:00",
    "summary": "The engineering sample features six CPU cores, 24GB of LPDDR5 memory running at 9,600 MT/s, and an integrated GPU clocked at 2.4 GHz, although its connection to a future Steam Deck remains unconfirmed"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/us-army-reportedly-developing-program-that-would-deploy-ai-agents-to-autonomously-seek-and-destroy-targets-in-enemy-digital-infrastructures-experts-warn-echotribble-program-could-have-disastrous-consequences",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Army developing program that would deploy AI agents to autonomously seek and destroy targets in enemy digital infrastructures",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/us-army-reportedly-developing-program-that-would-deploy-ai-agents-to-autonomously-seek-and-destroy-targets-in-enemy-digital-infrastructures-experts-warn-echotribble-program-could-have-disastrous-consequences",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T13:30:00+00:00",
    "summary": "The U.S. Army is developing a program to deploy autonomous AI agents that can navigate digital and network infrastructures, identify targets, and “neutralize” them."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/us-takes-unprecedented-step-of-recommissioning-nuclear-plants-due-to-ai-power-demand-2-25-gw-currently-on-tap-from-refurbished-reactors",
    "domain": "AI 算力 / 半导体",
    "title": "US restarts three shut-down nuclear reactors to feed AI data centers",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/us-takes-unprecedented-step-of-recommissioning-nuclear-plants-due-to-ai-power-demand-2-25-gw-currently-on-tap-from-refurbished-reactors",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T12:50:00+00:00",
    "summary": "The U.S. government is helping fund projects to bring nuclear reactors back online in an attempt to provide more energy capacity to AI data centers."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/oblivion-gamer-uses-claude-ai-to-boost-average-fps-gains-up-to-48-percent-stutters-slashed-by-90-percent-performance-mod-doesnt-change-game-assets-or-alter-visuals",
    "domain": "AI 算力 / 半导体",
    "title": "Oblivion gamer uses Claude AI to boost average FPS gains up to 48%, stutters slashed by 90%",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/oblivion-gamer-uses-claude-ai-to-boost-average-fps-gains-up-to-48-percent-stutters-slashed-by-90-percent-performance-mod-doesnt-change-game-assets-or-alter-visuals",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T12:30:00+00:00",
    "summary": "The new Oblivion Remastered Performance Fix mod is a pure code fix, with no changes to game assets or the game's visuals, yet it offers massive gains."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/buy-a-complete-rtx-5070-ti-gaming-pc-from-newegg-and-save-usd450-get-a-16gb-gpu-32gb-of-ram-an-i9-14900kf-processor-a-2tb-ssd-and-more-for-only-usd2-549",
    "domain": "AI 算力 / 半导体",
    "title": "Buy a complete RTX 5070 Ti gaming PC from Newegg and save $450",
    "url": "https://www.tomshardware.com/pc-components/buy-a-complete-rtx-5070-ti-gaming-pc-from-newegg-and-save-usd450-get-a-16gb-gpu-32gb-of-ram-an-i9-14900kf-processor-a-2tb-ssd-and-more-for-only-usd2-549",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T12:15:38+00:00",
    "summary": "Save $450 on Newegg’s ABS Stratos II Aqua prebuilt – open the box and start gaming tomorrow saving the trouble of building and supporting your own"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/chinas-tech-giants-drop-usd35-billion-on-export-compliant-nvidia-rtx-pro-5500-workstation-gpu-orders-to-power-ai-ambitions-according-to-reports-bytedance-alibaba-and-tencent-order-3-million-cards-despite-warnings-that-only-10-percent-of-orders-are-fulfillable",
    "domain": "AI 算力 / 半导体",
    "title": "China’s tech giants drop $35 billion on export-compliant Nvidia RTX Pro 5500 workstation GPU orders to power AI ambitions, according to reports",
    "url": "https://www.tomshardware.com/pc-components/gpus/chinas-tech-giants-drop-usd35-billion-on-export-compliant-nvidia-rtx-pro-5500-workstation-gpu-orders-to-power-ai-ambitions-according-to-reports-bytedance-alibaba-and-tencent-order-3-million-cards-despite-warnings-that-only-10-percent-of-orders-are-fulfillable",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T12:10:00+00:00",
    "summary": "$35 billion worth of Nvidia RTX Pro 5500 GPUs have been bought by Chinese trio Tencent, Alibaba and ByteDance, with demand far exceeding Nvidia's planned production, according to report."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/modern-software-is-built-on-the-backs-of-low-paid-maintainers-opening-the-door-to-potential-threats-report-details-critically-underfunded-projects-that-remain-understaffed-or-unfunded",
    "domain": "AI 算力 / 半导体",
    "title": "Modern software is built on the backs of low-paid maintainers, opening the door to potential threats",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/modern-software-is-built-on-the-backs-of-low-paid-maintainers-opening-the-door-to-potential-threats-report-details-critically-underfunded-projects-that-remain-understaffed-or-unfunded",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T12:10:00+00:00",
    "summary": "Modern computing remains vulnerable to the low bus factor of many open-source projects — continued lack of funding and manpower for voluntary-maintained infrastructure makes for a perennial threat"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/mods-can-almost-double-dlss-5-performance-through-foveation-reducing-resolution-at-the-edges-of-frames-technique-makes-dlss-5-possible-on-high-resolution-ultrawide-monitors",
    "domain": "AI 算力 / 半导体",
    "title": "Mods can almost double DLSS 5 performance through Foveation, reducing resolution at the edges of frames",
    "url": "https://www.tomshardware.com/pc-components/gpus/mods-can-almost-double-dlss-5-performance-through-foveation-reducing-resolution-at-the-edges-of-frames-technique-makes-dlss-5-possible-on-high-resolution-ultrawide-monitors",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T11:54:18+00:00",
    "summary": "VR rendering technique of foveated imaging gets integrated into DLSS 5, making it much easier to run"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nvidia-vera-cpu-deployed-at-ai-startup-modal-alongside-existing-x86-fleet-internal-testing-showed-2x-throughput-compared-to-amd-and-intel",
    "domain": "AI 算力 / 半导体",
    "title": "Modal taps Nvidia Vera CPUs after firm's internal tests show 2x throughput over Intel and AMD chips",
    "url": "https://www.tomshardware.com/pc-components/cpus/nvidia-vera-cpu-deployed-at-ai-startup-modal-alongside-existing-x86-fleet-internal-testing-showed-2x-throughput-compared-to-amd-and-intel",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T11:50:00+00:00",
    "summary": "Nvidia's Vera CPU delivers twice the performance of Intel and AMD chips in AI agent workloads, Modal claims."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-asks-fcc-for-waiver-to-buy-foreign-robots-chipmakers-automated-guided-vehicles-could-run-afoul-of-agencys-sweeping-robot-ban",
    "domain": "AI 算力 / 半导体",
    "title": "Intel asks FCC for waiver to buy foreign robots",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-asks-fcc-for-waiver-to-buy-foreign-robots-chipmakers-automated-guided-vehicles-could-run-afoul-of-agencys-sweeping-robot-ban",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T11:45:01+00:00",
    "summary": "Intel is concerned that the sweeping ban on foreign-made robots means that it could not update or maintain its fleet of AGVs."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/thunderbolt/windows-98-se-users-get-a-thunderbolt-4-driver-thanks-to-ai-assistance-vibe-coded-xhci98-driver-works-in-microsoft-oses-up-to-windows-7",
    "domain": "AI 算力 / 半导体",
    "title": "Windows 98 SE users get a Thunderbolt 4 driver, thanks to AI assistance",
    "url": "https://www.tomshardware.com/peripherals/thunderbolt/windows-98-se-users-get-a-thunderbolt-4-driver-thanks-to-ai-assistance-vibe-coded-xhci98-driver-works-in-microsoft-oses-up-to-windows-7",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T11:30:00+00:00",
    "summary": "Windows 98 devotees now have (experimental) support for USB4 and Thunderbolt 3/4. Vibe coded driver also supports Windows Me, XP, Vista, and 7."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/electronics-hobbyist-converts-usd120-ddr5-sodimm-kit-into-usd1000-desktop-kit-to-fight-ram-crisis-ics-from-sk-hynix-ddr5-5600-16gb-modules-used-to-create-ddr5-7800-desktop-sticks",
    "domain": "AI 算力 / 半导体",
    "title": "Electronics hobbyist converts $120 DDR5 SODIMM kit into ‘$1000’ desktop kit to fight RAM crisis",
    "url": "https://www.tomshardware.com/pc-components/ddr5/electronics-hobbyist-converts-usd120-ddr5-sodimm-kit-into-usd1000-desktop-kit-to-fight-ram-crisis-ics-from-sk-hynix-ddr5-5600-16gb-modules-used-to-create-ddr5-7800-desktop-sticks",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T11:10:00+00:00",
    "summary": "A hobbyist converted a SK hynix 2x 16GB DDR5-5600 SODIMM kit they got off Facebook Marketplace for $120 into a DDR5-7800 desktop kit."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/chinese-crime-ring-steals-millions-of-dollars-in-gift-cards-from-staples-customer-service-system-group-acquired-more-than-15-000-gift-cards-worth-more-than-usd5-million",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese crime ring steals more than $5 million in gift cards from Staples customer service",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/chinese-crime-ring-steals-millions-of-dollars-in-gift-cards-from-staples-customer-service-system-group-acquired-more-than-15-000-gift-cards-worth-more-than-usd5-million",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T10:50:00+00:00",
    "summary": "Over $5 million worth of gift cards for retailers like Target and Sephora were stolen from Staples when thieves gained access to an internal system."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/pick-up-this-ddr5-gaming-pc-for-only-usd899-save-usd300-off-the-ibuypower-slate-pc-with-10gb-of-graphics-vram",
    "domain": "AI 算力 / 半导体",
    "title": "Pick up this DDR5 gaming PC for only $899",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/pick-up-this-ddr5-gaming-pc-for-only-usd899-save-usd300-off-the-ibuypower-slate-pc-with-10gb-of-graphics-vram",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T10:37:47+00:00",
    "summary": "Pick up a brand-new iBuypower Slate PC for just $899, a great entry-level gaming PC option for 1080p gaming."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/save-usd60-on-this-tp-link-wireless-router-with-ultra-fast-wi-fi-7-support-now-usd189-98-archer-be9700-ships-with-six-antennas-and-class-leading-6-ghz-performance-to-upgrade-your-home-network",
    "domain": "AI 算力 / 半导体",
    "title": "Save $60 on this TP-Link wireless router with ultra-fast Wi-Fi 7 support, now $189.98",
    "url": "https://www.tomshardware.com/networking/routers/save-usd60-on-this-tp-link-wireless-router-with-ultra-fast-wi-fi-7-support-now-usd189-98-archer-be9700-ships-with-six-antennas-and-class-leading-6-ghz-performance-to-upgrade-your-home-network",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T10:29:58+00:00",
    "summary": "The TP-Link Archer BE9700 Wi-Fi 7 router is on sale for a limited-time only, down to $189.98, with six external antennas, a 10G WAN port, and four 2.5G Ethernet ports."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/google-deepmind-claims-four-gemini-4-agents-beat-minecraft-in-27-hours-by-writing-2-783-programs-of-their-own-the-ai-team-died-605-times-on-easy-difficulty-and-ran-up-an-estimated-usd520-in-tokens",
    "domain": "AI 算力 / 半导体",
    "title": "Google DeepMind claims four AI agents beat Minecraft in 27 hours by writing 2,783 programs of their own",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/google-deepmind-claims-four-gemini-4-agents-beat-minecraft-in-27-hours-by-writing-2-783-programs-of-their-own-the-ai-team-died-605-times-on-easy-difficulty-and-ran-up-an-estimated-usd520-in-tokens",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T10:25:00+00:00",
    "summary": "Google DeepMind researchers say four Gemini 4 Argon agents beat Minecraft in 27 hours, writing 2,783 programs with no human help."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/ukraine-rescues-wounded-soldier-using-hexacopter-drone-in-daring-first-heavy-lift-uav-brought-the-injured-infantryman-11-miles-back-to-safety",
    "domain": "AI 算力 / 半导体",
    "title": "Ukraine rescues wounded soldier using drone in daring 'world's first' UAV evacuation of a human",
    "url": "https://www.tomshardware.com/tech-industry/drones/ukraine-rescues-wounded-soldier-using-hexacopter-drone-in-daring-first-heavy-lift-uav-brought-the-injured-infantryman-11-miles-back-to-safety",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T10:00:00+00:00",
    "summary": "The Ukrainian military is claiming a world’s first after using an unmanned drone to rescue an injured soldier on the eastern Kharkiv front."
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
    "points": 375,
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
    "id": "rss:https://www.theverge.com/streaming/1015099/youtube-dislike-button-hide-menu",
    "domain": "大厂 AI 动态",
    "title": "YouTube might be testing hiding the dislike button",
    "url": "https://www.theverge.com/streaming/1015099/youtube-dislike-button-hide-menu",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T00:00:56+00:00",
    "summary": "YouTube appears to be testing hiding the dislike button on videos, as reported by 9to5Google. At least two users on X have recently shared screenshots of the dislike button now being placed in the thr"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1014976/sam-altman-ann-altman-lawsuit-dismissed",
    "domain": "大厂 AI 动态",
    "title": "Judge dismisses Sam Altman’s sister’s sexual abuse lawsuit",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1014976/sam-altman-ann-altman-lawsuit-dismissed",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T23:04:19+00:00",
    "summary": "On Tuesday, US District Judge Zachary Bluestone dismissed the lawsuit Ann Altman filed last year alleging that her brother, OpenAI CEO Sam Altman, had sexually abused her throughout her childhood. As "
  },
  {
    "id": "rss:https://www.theverge.com/news/1014989/trump-fraud-tips-program-nick-shirley-influencers",
    "domain": "大厂 AI 动态",
    "title": "Trump is giving Nick Shirley $10,000 and launching a $25 million fraud bounty program",
    "url": "https://www.theverge.com/news/1014989/trump-fraud-tips-program-nick-shirley-influencers",
    "source": "Mia Sato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T22:20:11+00:00",
    "summary": "Donald Trump and Vice President JD Vance said on Tuesday that the Trump administration was giving right-wing YouTuber Nick Shirley $10,000 and launching a $25 million bounty program for members of the"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1014999/google-gemini-ai-cars-android-auto",
    "domain": "大厂 AI 动态",
    "title": "Google’s more personalized Gemini AI is heading to your car",
    "url": "https://www.theverge.com/tech/1014999/google-gemini-ai-cars-android-auto",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T22:11:34+00:00",
    "summary": "Google is bringing Personal Intelligence to Gemini AI in your car. With this update, Gemini in Android Auto and cars with Google built-in can tap into your information across Google apps, including Gm"
  },
  {
    "id": "rss:https://www.theverge.com/science/1014984/spacex-tesla-merger-elon-musk-special-committees",
    "domain": "大厂 AI 动态",
    "title": "Tesla and SpaceX are discussing a possible merger, Musk says",
    "url": "https://www.theverge.com/science/1014984/spacex-tesla-merger-elon-musk-special-committees",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T21:30:24+00:00",
    "summary": "Tesla and SpaceX have formed special committees to discuss a possible merger, Elon Musk said during the latter's third quarter earnings call Tuesday. Musk, who serves as CEO of both companies, said th"
  },
  {
    "id": "rss:https://www.theverge.com/science/1014913/spacex-will-try-catching-starship-and-its-booster-for-first-time-musk-says",
    "domain": "大厂 AI 动态",
    "title": "SpaceX will try catching Starship and its booster for first time, Musk says",
    "url": "https://www.theverge.com/science/1014913/spacex-will-try-catching-starship-and-its-booster-for-first-time-musk-says",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T21:02:53+00:00",
    "summary": "SpaceX CEO Elon Musk said the company would attempt to catch Starship and its booster next month, with the goal of recovering the entire orbital launch system for the first time. If successful, Musk s"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/1014826/netflix-earnings-q3-2026-viewing-time",
    "domain": "大厂 AI 动态",
    "title": "Netflix is telling investors not to worry, even though you&#8217;re watching less and less",
    "url": "https://www.theverge.com/streaming/1014826/netflix-earnings-q3-2026-viewing-time",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T20:52:07+00:00",
    "summary": "Netflix is making monetization a top priority amid reports of falling viewing time. As part of its third-quarter earnings report on Tuesday, Netflix lists improvements to monetization as one of its ma"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1014869/snap-specs-robert-downey-jr",
    "domain": "大厂 AI 动态",
    "title": "Snap is paying Robert Downey Jr. to do the Iron Man thing",
    "url": "https://www.theverge.com/tech/1014869/snap-specs-robert-downey-jr",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T20:32:09+00:00",
    "summary": "Snap has a new brand ambassador for its Specs AR glasses: Iron Man actor Robert Downey Jr. The company has brought on Downey as Specs' \"Chief Customer Experience Officer\" and has published several vid"
  },
  {
    "id": "rss:https://www.theverge.com/science/1014150/spacex-q3-2026-earnings",
    "domain": "大厂 AI 动态",
    "title": "SpaceX says big AI growth fueled revenue jump",
    "url": "https://www.theverge.com/science/1014150/spacex-q3-2026-earnings",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T20:26:58+00:00",
    "summary": "SpaceX announced revenues of $14.6 billion in its Q3 earnings on Tuesday, which it says was a growth of 161 percent year-over-year \"fueled by our Super Intelligence (SI) segment and accelerated growth"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1014712/oura-smart-rings-track-cardio-effort-vo2-max-cardiovascular",
    "domain": "大厂 AI 动态",
    "title": "Oura adds two new cardiovascular health tracking features to its smart rings",
    "url": "https://www.theverge.com/tech/1014712/oura-smart-rings-track-cardio-effort-vo2-max-cardiovascular",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T20:26:04+00:00",
    "summary": "Oura is introducing two new cardiovascular-focused health tracking features to its smart rings designed to help users better understand the effect regular workouts and exercise are having on their lon"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/anthropic-pitches-ai-safety-bill-that-may-block-a-model-if-50-people-could-be-killed/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic pitches AI safety bill that may block a model if 50+ people could be killed",
    "url": "https://techcrunch.com/2026/10/20/anthropic-pitches-ai-safety-bill-that-may-block-a-model-if-50-people-could-be-killed/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T23:01:23+00:00",
    "summary": "The proposed policy seems to offer protections against AI running amok but actually forbids federal agencies from blocking a model's release without the permission of a judge."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/spacex-and-tesla-boards-form-special-committees-to-review-merger/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX and Tesla boards form special committees to review merger",
    "url": "https://techcrunch.com/2026/10/20/spacex-and-tesla-boards-form-special-committees-to-review-merger/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T22:57:57+00:00",
    "summary": "Elon Musk likes the idea but says he is not on either committee, which is made up of independent directors."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/hugging-face-ceo-warns-that-netflixs-openai-hack-documentary-isnt-accurate/",
    "domain": "大厂 AI 动态",
    "title": "Hugging Face CEO warns that Netflix’s OpenAI hack documentary isn’t accurate",
    "url": "https://techcrunch.com/2026/10/20/hugging-face-ceo-warns-that-netflixs-openai-hack-documentary-isnt-accurate/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T22:24:02+00:00",
    "summary": "Before you share the Netflix documentary \"AI Gone Rogue,\" take note. Clem Delangue, Hugging Face's co-founder who is featured in the film, says it went \"full doomer mode\" and isn't accurate."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/anthropics-cloud-partnerships-are-getting-messy/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s cloud partnerships are getting messy",
    "url": "https://techcrunch.com/2026/10/20/anthropics-cloud-partnerships-are-getting-messy/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T21:25:22+00:00",
    "summary": "Anthropic is reportedly struggling to secure enough compute from cloud providers that increasingly view it as a competitor, even as its infrastructure spending balloons ahead of a planned November IPO"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/spacexs-ai-business-is-beating-expectations/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX’s AI business is beating expectations",
    "url": "https://techcrunch.com/2026/10/20/spacexs-ai-business-is-beating-expectations/",
    "source": "Tim Fernholz, Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T20:40:41+00:00",
    "summary": "SpaceX hit profitability in the third quarter, with net income of $4.4 billion. AI was the engine."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/openai-acquires-startup-orchestra-bio%e2%81%a0-to-beef-up-its-biotech-business/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI acquires startup Orchestra Bio⁠ to beef up its biotech business",
    "url": "https://techcrunch.com/2026/10/20/openai-acquires-startup-orchestra-bio%e2%81%a0-to-beef-up-its-biotech-business/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T20:35:10+00:00",
    "summary": "OpenAI says it's adding Orchestra's team and technology to work on Rosalind, its AI model for life sciences research, and to its related Rosalind Workbench tool, a harness that aims to help researcher"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/google-is-bringing-a-more-personal-version-of-its-gemini-ai-assistant-to-your-car/",
    "domain": "大厂 AI 动态",
    "title": "Google is bringing a more personal version of its Gemini AI assistant to your car",
    "url": "https://techcrunch.com/2026/10/20/google-is-bringing-a-more-personal-version-of-its-gemini-ai-assistant-to-your-car/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T20:00:00+00:00",
    "summary": "Google is bringing Gemini's Personal Intelligence feature to cars, allowing its AI assistant to draw on information from Gmail, Calendar, Maps, YouTube, and other Google services to deliver more perso"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/gm-to-close-detroit-battery-assembly-plant-but-not-for-reasons-you-might-think/",
    "domain": "大厂 AI 动态",
    "title": "GM to close Detroit battery-assembly plant, but not for reasons you might think",
    "url": "https://techcrunch.com/2026/10/20/gm-to-close-detroit-battery-assembly-plant-but-not-for-reasons-you-might-think/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T19:32:43+00:00",
    "summary": "GM is shuttering the Brownstown Battery Assembly Plant, though the closure has nothing to do with the automaker's electrification strategy."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/google-has-joined-amazon-in-attacking-nvidias-stronghold-with-ai-app-developers/",
    "domain": "大厂 AI 动态",
    "title": "Google has joined Amazon in attacking Nvidia’s stronghold with AI app developers",
    "url": "https://techcrunch.com/2026/10/20/google-has-joined-amazon-in-attacking-nvidias-stronghold-with-ai-app-developers/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T18:38:24+00:00",
    "summary": "Google has joined Amazon in releasing a developer tool that makes it easy for PyTorch users to move their apps off Nvidia GPUs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/chatgpt-now-lets-you-lock-your-chats/",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT now lets you lock your chats",
    "url": "https://techcrunch.com/2026/10/20/chatgpt-now-lets-you-lock-your-chats/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T18:36:53+00:00",
    "summary": "The company says the feature is designed for situations where users might be discussing something personal or planning a surprise and want to keep those conversations private when handing their device"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/eric-schmidt-reportedly-owns-about-half-as-much-of-anthropic-as-ceo-dario-amodei/",
    "domain": "大厂 AI 动态",
    "title": "Eric Schmidt reportedly owns about half as much of Anthropic as CEO Dario Amodei",
    "url": "https://techcrunch.com/2026/10/20/eric-schmidt-reportedly-owns-about-half-as-much-of-anthropic-as-ceo-dario-amodei/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T17:55:12+00:00",
    "summary": "Eric Schmidt’s fortune is about to get even bigger."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/metas-muse-hits-10m-u-s-downloads-in-40-days-a-milestone-reached-by-only-11-other-apps/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s Muse hits 10M US downloads in 40 days, a milestone reached by only 11 other apps",
    "url": "https://techcrunch.com/2026/10/20/metas-muse-hits-10m-u-s-downloads-in-40-days-a-milestone-reached-by-only-11-other-apps/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T17:12:48+00:00",
    "summary": "New data also shows Muse is retaining users at higher rates than its AI rivals."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/ex-nvidia-turned-vc-amulya-vishwanath-physical-ai-is-in-its-lego-era/",
    "domain": "大厂 AI 动态",
    "title": "Ex-Nvidia-turned-VC Amulya Vishwanath: ‘Physical AI is in its LEGO era’",
    "url": "https://techcrunch.com/2026/10/20/ex-nvidia-turned-vc-amulya-vishwanath-physical-ai-is-in-its-lego-era/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T16:20:06+00:00",
    "summary": "It’s the moment everyone is waiting for — the ChatGPT moment for robotics, Amulya Vishwanath explained to TechCrunch’s Equity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/streaming-guide-justwatch-becomes-a-streamer-itself/",
    "domain": "大厂 AI 动态",
    "title": "Streaming guide JustWatch becomes a streamer itself",
    "url": "https://techcrunch.com/2026/10/20/streaming-guide-justwatch-becomes-a-streamer-itself/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T16:01:24+00:00",
    "summary": "JustWatch, the popular streaming search guide used by 50 million people, is launching its own streaming service, offering free, ad-supported movies and shows alongside a $3.99-per-month ad-free tier a"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/plants-can-speak-using-electricity-so-this-startup-built-an-ai-model-to-decipher-their-language/",
    "domain": "大厂 AI 动态",
    "title": "Plants can speak using electricity, so this startup built an AI model to decipher their language",
    "url": "https://techcrunch.com/2026/10/20/plants-can-speak-using-electricity-so-this-startup-built-an-ai-model-to-decipher-their-language/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T16:00:00+00:00",
    "summary": "Electric Plant has built an AI-powered translator to help humans listen to what plants are saying with the subtle electricity coursing through their stems."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/tiktok-staff-raised-child-safety-concerns-but-executives-reportedly-failed-to-act/",
    "domain": "大厂 AI 动态",
    "title": "TikTok staff raised child safety concerns, but executives reportedly failed to act",
    "url": "https://techcrunch.com/2026/10/20/tiktok-staff-raised-child-safety-concerns-but-executives-reportedly-failed-to-act/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T15:03:41+00:00",
    "summary": "Court documents show TikTok employees were frustrated with how executives responded to their concerns about risks to children."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/figma-co-founder-dylan-field-thinks-mcp-is-not-a-perfect-protocol/",
    "domain": "大厂 AI 动态",
    "title": "Figma co-founder Dylan Field thinks MCP is not a perfect protocol",
    "url": "https://techcrunch.com/2026/10/20/figma-co-founder-dylan-field-thinks-mcp-is-not-a-perfect-protocol/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T14:13:32+00:00",
    "summary": "Figma said it plans to support as many standards as possible without exposing all of its data."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/spacex-alums-aviation-startup-reliable-robotics-lands-115m-topping-1b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX alum’s aviation startup, Reliable Robotics, lands $115M, topping $1B valuation",
    "url": "https://techcrunch.com/2026/10/20/spacex-alums-aviation-startup-reliable-robotics-lands-115m-topping-1b-valuation/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T13:17:36+00:00",
    "summary": "Reliable Robotics extended its Series D round with $115 million in equity and $25 million in debt."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/us-orders-federal-agencies-to-remove-chinas-deepseek-ai-from-their-systems/",
    "domain": "大厂 AI 动态",
    "title": "US orders federal agencies to remove China’s DeepSeek AI from their systems",
    "url": "https://techcrunch.com/2026/10/20/us-orders-federal-agencies-to-remove-chinas-deepseek-ai-from-their-systems/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T13:07:24+00:00",
    "summary": "The U.S. has ordered federal civilian agencies to remove DeepSeek products and third-party services built using its technology, citing national security concerns."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/20/eka-is-worth-1-45-billion-thanks-to-a-physical-ai-model-that-has-experts-raving/",
    "domain": "大厂 AI 动态",
    "title": "Eka is worth $1.45B thanks to a physical AI model that has experts raving",
    "url": "https://techcrunch.com/2026/10/20/eka-is-worth-1-45-billion-thanks-to-a-physical-ai-model-that-has-experts-raving/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T13:00:00+00:00",
    "summary": "Eka Robotics may be the first robotic arm that is actually good at picking up a wide range of objects, and it is so smooth and human-like, it is wowing the industry."
  },
  {
    "id": "rss:https://stratechery.com/2026/muse-spark-open-meta-apple-thin-and-thick/",
    "domain": "大厂 AI 动态",
    "title": "Muse Spark Open, Meta + Apple, Thin and Thick",
    "url": "https://stratechery.com/2026/muse-spark-open-meta-apple-thin-and-thick/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T10:00:00+00:00",
    "summary": "Meta has a new open source model, and to everyone's surprise, they are are partnering with Apple to make sure you can run it locally."
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
    "id": "rss:https://arstechnica.com/security/2026/10/php-maintainers-tell-web-devs-to-prepare-themselves-for-critical-security-patches/",
    "domain": "大厂 AI 动态",
    "title": "PHP warns it plans to release 2 emergency patches imminently",
    "url": "https://arstechnica.com/security/2026/10/php-maintainers-tell-web-devs-to-prepare-themselves-for-critical-security-patches/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T02:12:18+00:00",
    "summary": "Unconfirmed report claims PHP2Shell exploit remotely executes code on PHP sites."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/10/spacex-and-tesla-into-a-single-company-has-a-lot-of-merit-musk-says/",
    "domain": "大厂 AI 动态",
    "title": "Merging SpaceX and Tesla would be a \"good idea,\" Musk says",
    "url": "https://arstechnica.com/space/2026/10/spacex-and-tesla-into-a-single-company-has-a-lot-of-merit-musk-says/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T22:04:54+00:00",
    "summary": "\"I do think there's a lot of merit to combining the companies.\""
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/10/cops-raid-office-of-rfk-jr-allies-planning-unethical-vaccine-trial-on-babies/",
    "domain": "大厂 AI 动态",
    "title": "Cops raid office of RFK Jr. allies planning “unethical” vaccine trial on babies",
    "url": "https://arstechnica.com/health/2026/10/cops-raid-office-of-rfk-jr-allies-planning-unethical-vaccine-trial-on-babies/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T21:44:34+00:00",
    "summary": "Guinea-Bissau police said hepatitis B vaccine doses were taken as part of an investigation."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/10/report-microsofts-project-helix-planned-for-2028-at-1200-to-1800-price/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft reportedly projects $1,200 to $1,800 price for 2028 Project Helix",
    "url": "https://arstechnica.com/gaming/2026/10/report-microsofts-project-helix-planned-for-2028-at-1200-to-1800-price/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-20T21:14:33+00:00",
    "summary": "Xbox maker is also apparently planning its own gaming handheld for next year."
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
    "points": 29,
    "published_at": "2026-10-18T16:48:25+00:00",
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
    "points": 1642,
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
    "id": "hn:50173487",
    "domain": "金融",
    "title": "Feds suspect ransom negotiator ran ShinyHunters extortion site",
    "url": "https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/",
    "source": "Bender",
    "platform": "hackernews",
    "points": 188,
    "published_at": "2026-10-20T22:21:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50131440",
    "domain": "金融",
    "title": "US federal budget deficit jumps 12% in one year to nearly $2 Trillion",
    "url": "https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 206,
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
    "points": 121,
    "published_at": "2026-10-18T14:16:41+00:00",
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
    "id": "hn:50161207",
    "domain": "金融",
    "title": "U.S. Supreme Court to review 1868 federal ban on home distilling of liquor",
    "url": "https://www.staradvertiser.com/2026/10/19/breaking-news/u-s-supreme-court-to-review-1868-federal-ban-on-home-distilling-of-liquor/",
    "source": "Jimmc414",
    "platform": "hackernews",
    "points": 67,
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
    "id": "rss:https://arxiv.org/abs/2610.26919",
    "domain": "金融",
    "title": "Dynamic portfolio selection under range value-at-risk with logarithmic returns",
    "url": "https://arxiv.org/abs/2610.26919",
    "source": "Hui Mi, Yuzhe Pan, Zuo Quan Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T04:00:00+00:00",
    "summary": "arXiv:2610.26919v1 Announce Type: new Abstract: This paper studies continuous-time portfolio selection under Range Value-at-Risk (RVaR), with both portfolio performance and risk evaluated in terms of "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.27100",
    "domain": "金融",
    "title": "LOB-Impact Benchmark: Emergent Market Impact in Generative Limit Order Book Models",
    "url": "https://arxiv.org/abs/2610.27100",
    "source": "George Nigmatulin, Valentin Mohl, Sascha Frey, Kang Li, Aramis Marti-Shahandeh, Mihai Cucuringu, Anisoara Calinescu, Jakob Foerster, Stefan Zohren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T04:00:00+00:00",
    "summary": "arXiv:2610.27100v1 Announce Type: new Abstract: Realistic market impact is essential for generative limit order book (LOB) models to serve as world models for trading agents. If a simulator misprices "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.27576",
    "domain": "金融",
    "title": "Who Gains When the Umpire Is a Machine? Evidence from the Automated Ball-Strike System (ABS)",
    "url": "https://arxiv.org/abs/2610.27576",
    "source": "Seung Jin Cho, Jun Yeong Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T04:00:00+00:00",
    "summary": "arXiv:2610.27576v1 Announce Type: new Abstract: In 2024 the Korea Baseball Organization became the first top-tier league to replace the home-plate umpires ball-strike judgment with an automated system"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.27751",
    "domain": "金融",
    "title": "Market Regime-Based Multi-Asset Portfolio Optimization Using Nested Clustered Optimization for Tactical Asset Allocation",
    "url": "https://arxiv.org/abs/2610.27751",
    "source": "Supriadi, Bambang Siswoyo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T04:00:00+00:00",
    "summary": "arXiv:2610.27751v1 Announce Type: new Abstract: We propose a regime-aware tactical asset allocation (TAA) framework integrating market regime detection with Nested Clustered Optimization (NCO) for mul"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.28071",
    "domain": "金融",
    "title": "Arithmetic Models for Commodity Futures, Vanilla, and Calendar Spread Options",
    "url": "https://arxiv.org/abs/2610.28071",
    "source": "Malthe Rauh Johansen, Nina Lange, David Skovmand",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T04:00:00+00:00",
    "summary": "arXiv:2610.28071v1 Announce Type: new Abstract: We develop an arithmetic multi-factor stochastic volatility model for commodity futures and options. The arithmetic specification yields a low-dimension"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.28133",
    "domain": "金融",
    "title": "Occupational Uniqueness and Wage Growth",
    "url": "https://arxiv.org/abs/2610.28133",
    "source": "R. Vestrelli, A. Fronzetti Colladon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T04:00:00+00:00",
    "summary": "arXiv:2610.28133v1 Announce Type: new Abstract: Changes in occupational task content may have different economic implications depending on whether the tasks gained or lost are occupation-specific or a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.27296",
    "domain": "金融",
    "title": "Stronger artificial intelligence breakthroughs hasten their own exhaustion",
    "url": "https://arxiv.org/abs/2610.27296",
    "source": "Beichen Lu, Honglin Bao, Qi Huang, Qingguo Meng, James A. Evans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T04:00:00+00:00",
    "summary": "arXiv:2610.27296v1 Announce Type: cross Abstract: Progress in artificial intelligence is widely assumed to scale with effort: more researchers, papers and investment should accelerate discovery. Theor"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.27390",
    "domain": "金融",
    "title": "Choose your own adventure: How data source selection shapes urban accessibility analyses",
    "url": "https://arxiv.org/abs/2610.27390",
    "source": "Geoff Boeing, Jiyoon Kim, Daniele Simon-Thompson, Jaehyun Ha, Ruoyu Chen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T04:00:00+00:00",
    "summary": "arXiv:2610.27390v1 Announce Type: cross Abstract: Urban park accessibility shapes mental health, physical well-being, and community cohesion. Measuring it is thus central to urban and landscape planni"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.28075",
    "domain": "金融",
    "title": "Speculative Imbalance Positions by Non-Physical Traders: Impacts on Electricity System Balancing in Great Britain",
    "url": "https://arxiv.org/abs/2610.28075",
    "source": "Joseph Cary, Thomas Morstyn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T04:00:00+00:00",
    "summary": "arXiv:2610.28075v1 Announce Type: cross Abstract: The electricity system in Great Britain (GB) allows participants to deliberately produce or consume a different volume to their traded position and ha"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.28154",
    "domain": "金融",
    "title": "Digital Nudge Effects in Optimal Stopping Games: Antagonistic Interactions in Layered Choice Architectures",
    "url": "https://arxiv.org/abs/2610.28154",
    "source": "Batisse Manhardt, Ja-Nae Duane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T04:00:00+00:00",
    "summary": "arXiv:2610.28154v1 Announce Type: cross Abstract: Digital nudges have become a prominent area of research in human-centered interaction, yet little is known about how they interact when deployed toget"
  },
  {
    "id": "rss:https://arxiv.org/abs/1809.05643",
    "domain": "金融",
    "title": "Kernel-based collocation methods for Heath-Jarrow-Morton models with Musiela parametrization",
    "url": "https://arxiv.org/abs/1809.05643",
    "source": "Yuki Kinoshita, Yumiharu Nakano",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T04:00:00+00:00",
    "summary": "arXiv:1809.05643v5 Announce Type: replace Abstract: We study kernel-based collocation methods for numerical solutions of Heath-Jarrow-Morton models in Musiela parametrization. The methods are Euler-Ma"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.06584",
    "domain": "金融",
    "title": "Two Types of Tertiarization: Household Demand, Production Networks, and the Rise of Services",
    "url": "https://arxiv.org/abs/2608.06584",
    "source": "Li Gan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T04:00:00+00:00",
    "summary": "arXiv:2608.06584v2 Announce Type: replace Abstract: I measure whether the rise of services is ultimately supported by household consumption or by non-household demand through production networks, inve"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.07819",
    "domain": "金融",
    "title": "The friendship paradox: Causal evidence of its behavioral consequences",
    "url": "https://arxiv.org/abs/2608.07819",
    "source": "Gary Charness, Francesco Feri, Matthew O. Jackson, Miguel A. Melendez-Jimenez, Matthias Sutter",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T04:00:00+00:00",
    "summary": "arXiv:2608.07819v2 Announce Type: replace Abstract: We provide a first causal analysis of the behavioral consequences of the friendship paradox-the fact that people's friends in a network have more co"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.25802",
    "domain": "金融",
    "title": "Amortized Neural Filtering for Calibrated Posteriors in Statistical Arbitrage",
    "url": "https://arxiv.org/abs/2610.25802",
    "source": "Minkey Chang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T04:00:00+00:00",
    "summary": "arXiv:2610.25802v2 Announce Type: replace Abstract: Statistical arbitrage trades on an estimate of the state of a residual spread, and conventional practice discards the uncertainty of that estimate. "
  },
  {
    "id": "rss:https://arxiv.org/abs/2412.16655",
    "domain": "金融",
    "title": "Direct Inversion for Chi-Square Sampling, the Squared Bessel Process, and Applications",
    "url": "https://arxiv.org/abs/2412.16655",
    "source": "Simon J. A. Malham, Anke Wiese, Yifan Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T04:00:00+00:00",
    "summary": "arXiv:2412.16655v2 Announce Type: replace-cross Abstract: In this paper we derive a new direct inversion method to simulate squared Bessel processes. Since the transition probability of these processe"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.07898",
    "domain": "金融",
    "title": "Disclosure under Noisy Information Processing",
    "url": "https://arxiv.org/abs/2609.07898",
    "source": "Jeremy Bertomeu, Edwige Cheynel, Peicong Hu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-21T04:00:00+00:00",
    "summary": "arXiv:2609.07898v2 Announce Type: replace-cross Abstract: Capital markets process disclosures with noise. Adding this single friction overturns the standard characterization of costly voluntary disclo"
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
