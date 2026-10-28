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

- 今日日期：`2026-10-28`
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
  "date": "2026-10-28",
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
    "points": 2168597,
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
    "points": 2043624,
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
    "points": 1446060,
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
    "points": 1402511,
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
    "points": 1345815,
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
    "points": 905964,
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
    "points": 879633,
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
    "points": 733376,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 426238,
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
    "points": 357455,
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
    "points": 337959,
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
    "points": 316001,
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
    "points": 288275,
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
    "points": 218500,
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
    "points": 185000,
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
    "points": 163775,
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
    "points": 161525,
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
    "points": 161165,
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
    "points": 144643,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 103453,
    "published_at": "2026-04-27T04:45:20+00:00",
    "summary": "很多人问我上期爆了的那条视频里，那个 PPT 是怎么做的。\n其实我是用 Anthropic 最近出的 Claude Design 做的，这个功能一发出来就在全网传疯了，一条推文就冲上了 6000 多万曝光。\n本期视频我会带你手把手从 0 到 1 把这个Skill 装好，然后一起跑一个成品效果出来。"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 103392,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 93021,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 92572,
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
    "points": 77140,
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
    "points": 76644,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 56460,
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
    "points": 49777,
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
    "points": 47770,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1woHQ6kEtv",
    "domain": "AI",
    "title": "【2026最新版】Workbuddy财务自动化办公实战教程，搭建数字员工，能够秒做账、报税、报销、出报表、做财务分析、编制预算、处理合并报表",
    "url": "http://www.bilibili.com/video/av117404038466491",
    "source": "Max极客菌",
    "platform": "bilibili",
    "points": 41240,
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
    "points": 40986,
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
    "points": 34612,
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
    "points": 31076,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 30243,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29885,
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
    "points": 29023,
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
    "points": 28721,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 25652,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 24283,
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
    "points": 23100,
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
    "points": 22830,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV188UHYkEdg",
    "domain": "AI",
    "title": "Cursor / Windsurf + Android Studio 高效AI编程：零基础也能开发安卓应用",
    "url": "http://www.bilibili.com/video/av113502647750313",
    "source": "kate人不错",
    "platform": "bilibili",
    "points": 21172,
    "published_at": "2024-11-18T07:04:36+00:00",
    "summary": "欢迎关注我的知识星球：https://t.zsxq.com/FF0He\n\n我会分享最新AI资讯、源代码、回答你的提问。\n\n视频亮点：\n\n双工具对比：解析 Cursor 和 Windsurf 各自优势\n实战案例：从五子棋到卡路里计算AI应用的完整开发过程\n专业部署：Android Studio 配置与构建技巧\n\n时间戳：\n\n0:00 - 引言\n\n0:26 - 我开发的应用演示\n\n2:33 - Rea"
  },
  {
    "id": "bvid:BV1uTnP62Eu1",
    "domain": "AI",
    "title": "【AI开发单片机系统】不写一行代码：STM32从零到成品全流程实战",
    "url": "http://www.bilibili.com/video/av117472841697065",
    "source": "叶江航",
    "platform": "bilibili",
    "points": 18762,
    "published_at": "2026-10-20T10:50:16+00:00",
    "summary": "该教程用 AI 辅助开发，零代码编写，快速从想法到成品做出一套完整的 STM32 物联网系统。\n以STM32 智能温控风扇系统为实战案例，带你从 0 到 1 完成整个单片机系统的设计与制作。\n\n全程演示一套可复用的「AI 开发六步法」：\n需求分析 → 硬件选型 → 功能拆解 → 硬件搭建 → 模块编程 → 系统联调\n学会这套方法，你也能快速做出自己的单片机系统。"
  },
  {
    "id": "bvid:BV1htCnY4ET6",
    "domain": "AI",
    "title": "用 Cursor AI 写 flutter 直接喂设计图就行 | flutter教程",
    "url": "http://www.bilibili.com/video/av113723805008238",
    "source": "独立开发者_猫哥",
    "platform": "bilibili",
    "points": 18170,
    "published_at": "2024-12-27T08:21:35+00:00",
    "summary": "✏️【关于本期视频】\n在上一篇文章《Flutter 使用 Cursor 和 Figma 快速生成界面代码》中，有同学提到他直接使用了设计稿的图片进行生成。我试了一下，效果确实很好。因此，我整理了一些文档，希望对大家有所帮助。\n下图展示了我没有手动编写任何代码实现的消息首页，支持上下滑动刷新数据。\n👉 文档 https://ducafecat.com/blog/use-cursor-ai-flutt"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15427,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 15285,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 13256,
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
    "points": 11427,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV14rxM6qEnL",
    "domain": "AI",
    "title": "最新Skills开发教程，Agent skill实战|WorkBuddy+Codex+DeepSeek Harness",
    "url": "http://www.bilibili.com/video/av117511429295044",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 11304,
    "published_at": "2026-10-28T02:00:00+00:00",
    "summary": "【课程简介】Agent Skills零基础教程，从WorkBuddy、Codex上手到项目落地实战。"
  },
  {
    "id": "bvid:BV1wFpP6uE1s",
    "domain": "AI",
    "title": "【开源】让手机自己操作 App！手上的 ai Agent！GitHub开源安卓App推荐",
    "url": "http://www.bilibili.com/video/av117394643097499",
    "source": "补药满减哇",
    "platform": "bilibili",
    "points": 9273,
    "published_at": "2026-10-07T01:05:00+00:00",
    "summary": "开源安卓 AI Agent：RikkaHub Agent Pure\n它能「看懂」屏幕、自己操作各种 App，也能组队干活。\n\n⬇️ 下载 &amp; 源码（AGPL-3.0）\nhttps://github.com/wuyhong715/rikkahub-agent-pure\n\n▶ 本片讲两件事\n① 无障碍屏幕自动化：读控件树定位、实时决策，不是死坐标脚本\n② 专家团系统：每个专家有自己的模型/工具"
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 8581,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
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
    "points": 349,
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
    "points": 145,
    "published_at": "2026-10-25T21:07:38+00:00",
    "summary": ""
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
    "id": "rss:https://www.eetimes.com/automakers-reconsider-in-cabin-sensing-for-euro-ncap-ratings/",
    "domain": "AI 算力 / 半导体",
    "title": "Automakers Reconsider In-Cabin Sensing for Euro NCAP Ratings",
    "url": "https://www.eetimes.com/automakers-reconsider-in-cabin-sensing-for-euro-ncap-ratings/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T17:00:11+00:00",
    "summary": "Stricter European safety assessment criteria are prompting car companies to replace steering-wheel sensors with consolidated in-cabin systems. The post Automakers Reconsider In-Cabin Sensing for Euro "
  },
  {
    "id": "rss:https://www.eetimes.com/framing-the-shift-to-48v/",
    "domain": "AI 算力 / 半导体",
    "title": "Framing the Shift to 48V",
    "url": "https://www.eetimes.com/framing-the-shift-to-48v/",
    "source": "Vasanth Sista, Field Application Engineer, TE Connectivity",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T13:00:00+00:00",
    "summary": "From lighter wiring to automated assembly, 48V architectures are reshaping vehicle connectivity and laying the groundwork for next generation mobility. The post Framing the Shift to 48V appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/the-ai-packaging-challenge-5-reasons-panels-are-gaining-momentum/",
    "domain": "AI 算力 / 半导体",
    "title": "The AI Packaging Challenge: 5 Reasons Panels Are Gaining Momentum",
    "url": "https://www.eetimes.com/the-ai-packaging-challenge-5-reasons-panels-are-gaining-momentum/",
    "source": "Aaron Fellis, corporate vice president and general manager, Wet Equipment Technology Systems, Lam Research",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T13:00:00+00:00",
    "summary": "As AI pushes chip packages beyond traditional wafer limits, panel-level processing is emerging as a critical path to scale advanced packaging. The post The AI Packaging Challenge: 5 Reasons Panels Are"
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
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/nvidia-is-bankrolling-ai-accelerator-supply-chain-buildout-to-reserve-production-capacity-announces-billion-dollar-deals-with-six-major-suppliers-across-substrates-advanced-packaging-semiconductor-testing-and-optical-engines",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is bankrolling AI accelerator supply chain buildout to reserve production capacity",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/nvidia-is-bankrolling-ai-accelerator-supply-chain-buildout-to-reserve-production-capacity-announces-billion-dollar-deals-with-six-major-suppliers-across-substrates-advanced-packaging-semiconductor-testing-and-optical-engines",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T11:00:00+00:00",
    "summary": "Nvidia is committing billions to expand substrate, co-packaged optics, advanced packaging, and chip-testing capacity through 2028, reserving capacity at nearly every stage of its AI accelerator supply"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/60-000-microsoft-employees-offered-voluntary-buyouts-as-ai-buildout-costs-bite-program-covers-roughly-27-percent-of-workforce-across-us-canada-india-and-the-uk",
    "domain": "AI 算力 / 半导体",
    "title": "60,000 Microsoft employees offered voluntary buyouts as AI buildout costs bite",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/60-000-microsoft-employees-offered-voluntary-buyouts-as-ai-buildout-costs-bite-program-covers-roughly-27-percent-of-workforce-across-us-canada-india-and-the-uk",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T10:30:00+00:00",
    "summary": "Microsoft is offering buyouts to around 60,000 members of its workforce as it looks to balance the books amid a ramp-up in AI data center spending."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-prepares-for-potential-usd2-trillion-ipo-valuation-after-reporting-billions-in-revenue-company-warns-ai-could-pose-catastrophic-existential-risks-to-humanity",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic prepares for potential $2 trillion IPO valuation after reporting billions in revenue",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-prepares-for-potential-usd2-trillion-ipo-valuation-after-reporting-billions-in-revenue-company-warns-ai-could-pose-catastrophic-existential-risks-to-humanity",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T10:00:00+00:00",
    "summary": "Anthropic has filed to go public as it pursues a potential multitrillion-dollar valuation, reporting $16.3 billion in revenue for the first half of 2026. The company’s filing also warns that its AI sa"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/data-center-gear-is-being-hijacked-in-transit-to-the-tune-of-hundreds-of-millions-grand-theft-gpu-thieves-hack-accounts-perform-hit-and-runs-spoof-gps-signals-and-funnel-hardware-to-china",
    "domain": "AI 算力 / 半导体",
    "title": "Data center gear is being hijacked in transit to the tune of hundreds of millions",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/data-center-gear-is-being-hijacked-in-transit-to-the-tune-of-hundreds-of-millions-grand-theft-gpu-thieves-hack-accounts-perform-hit-and-runs-spoof-gps-signals-and-funnel-hardware-to-china",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T09:40:00+00:00",
    "summary": "Data center gear is being stolen in transit to the tune of hundreds of millions — grand-theft-GPU thieves hack accounts, perform hit-and-runs, and spoof GPS signals"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/spacex-closes-usd40-billion-debt-financing-for-gpus-expected-in-the-first-half-of-2027-musk-says-company-faces-up-to-usd40-billion-in-additional-fourth-quarter-capital-spending-as-ai-infrastructure-costs-soar",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceX closes $40 billion debt financing for GPUs expected in the first half of 2027, Musk says",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/spacex-closes-usd40-billion-debt-financing-for-gpus-expected-in-the-first-half-of-2027-musk-says-company-faces-up-to-usd40-billion-in-additional-fourth-quarter-capital-spending-as-ai-infrastructure-costs-soar",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T09:20:00+00:00",
    "summary": "SpaceX expects fourth-quarter capital expenditure of $35 billion to $40 billion, CFO Bret Johnsen said, as Elon Musk pushes to expand the company’s AI computing infrastructure."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-quietly-confirms-raptor-lake-next-cpus-through-internal-driver-publication-lga-1700-chips-also-appear-in-shipping-manifests-dating-back-to-august",
    "domain": "AI 算力 / 半导体",
    "title": "Intel quietly confirms Raptor Lake Next CPUs through internal driver publication",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-quietly-confirms-raptor-lake-next-cpus-through-internal-driver-publication-lga-1700-chips-also-appear-in-shipping-manifests-dating-back-to-august",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T18:50:28+00:00",
    "summary": "An internal driver and a shipping manifest reveal that Intel's desktop Raptor Lake Next parts may be on the way right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/portable-monitors/jsaux-flipgo-dual-screen-portable-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "JSAUX FlipGo dual-screen portable monitor review: Gorgeous displays with touch support and a built-in USB hub",
    "url": "https://www.tomshardware.com/monitors/portable-monitors/jsaux-flipgo-dual-screen-portable-monitor-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T16:33:31+00:00",
    "summary": "The JSAUX FlipGo features dual 16-inch touch displays and a built-in hub."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/hdds/save-usd134-on-this-wd-red-plus-10tb-hdd-bundle-at-newegg-this-double-drive-deal-lands-you-with-20tb-of-total-capacity-for-your-nas",
    "domain": "AI 算力 / 半导体",
    "title": "Save $134 on this WD Red Plus 10TB HDD bundle at Newegg",
    "url": "https://www.tomshardware.com/pc-components/hdds/save-usd134-on-this-wd-red-plus-10tb-hdd-bundle-at-newegg-this-double-drive-deal-lands-you-with-20tb-of-total-capacity-for-your-nas",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T16:00:00+00:00",
    "summary": "Grab two 10TB NAS Hard Disk Drives and save $134 — this two-pack WD Red Plus bundle is the best deal for adding capacity to your NAS"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/asus-rog-xbox-ally-x20-tested-same-performance-more-comfortable-and-a-glorious-oled-screen",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Xbox Ally X20 tested: Same performance, more comfortable, and a glorious OLED screen",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/asus-rog-xbox-ally-x20-tested-same-performance-more-comfortable-and-a-glorious-oled-screen",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T15:00:00+00:00",
    "summary": "Asus adds an OLED screen, TMR sticks, and more comfortable grips to its AMD-powered gaming handheld."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/3-2-pb-s-real-time-optical-fiber-transfer-speed-world-record-claimed-by-chinese-team-speed-fast-enough-to-download-more-than-20-000-4k-movies-in-one-second",
    "domain": "AI 算力 / 半导体",
    "title": "3.2 Petabits per second real-time optical fiber transfer speed world record claimed by Chinese team",
    "url": "https://www.tomshardware.com/networking/3-2-pb-s-real-time-optical-fiber-transfer-speed-world-record-claimed-by-chinese-team-speed-fast-enough-to-download-more-than-20-000-4k-movies-in-one-second",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T14:43:37+00:00",
    "summary": "A Chinese team has claimed a new world record for real-time transfer speeds across a 24-core optical fiber cable."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/leaked-256-core-zen-6c-epyc-cpu-destroys-zen-5-in-early-single-threaded-benchmarks-hints-at-24-percent-ipc-gain-early-single-threaded-benchmarks-point-to-huge-amd-zen-6-improvements",
    "domain": "AI 算力 / 半导体",
    "title": "Leaked 256-core Zen 6c EPYC CPU destroys Zen 5 in early single-threaded benchmarks hints at 24% IPC gain",
    "url": "https://www.tomshardware.com/pc-components/cpus/leaked-256-core-zen-6c-epyc-cpu-destroys-zen-5-in-early-single-threaded-benchmarks-hints-at-24-percent-ipc-gain-early-single-threaded-benchmarks-point-to-huge-amd-zen-6-improvements",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T14:31:43+00:00",
    "summary": "A benchmark leak and a direct clock-matched comparison from an enthusiast seed the idea that Zen 6 may come with a decent IPC bump as well as increased clocks."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/micron-plans-to-use-wafer-bonding-and-high-na-euv-for-next-gen-dram-company-also-developing-vertical-high-bandwidth-memory-and-vertical-edge-inference-memory-integrated-directly-on-top-of-processors",
    "domain": "AI 算力 / 半导体",
    "title": "Micron plans to use wafer bonding and High-NA EUV for next-gen DRAM",
    "url": "https://www.tomshardware.com/pc-components/dram/micron-plans-to-use-wafer-bonding-and-high-na-euv-for-next-gen-dram-company-also-developing-vertical-high-bandwidth-memory-and-vertical-edge-inference-memory-integrated-directly-on-top-of-processors",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T14:00:00+00:00",
    "summary": "Micron rejects 4F2, intends to use wafer bonding and High-NA EUV before going 3D NAND over the next few years."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/windows-11s-whole-iso-squeezed-into-a-cd-rom-sub-700mb-disk-boots-to-the-desktop-runs-apps-just-like-the-microsoft-original",
    "domain": "AI 算力 / 半导体",
    "title": "Windows 11’s ‘whole ISO’ squeezed into a CD-ROM",
    "url": "https://www.tomshardware.com/software/windows/windows-11s-whole-iso-squeezed-into-a-cd-rom-sub-700mb-disk-boots-to-the-desktop-runs-apps-just-like-the-microsoft-original",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T13:40:00+00:00",
    "summary": "Professional Windows crusher NTDEV has showcased their next-generation tool for compressing Windows 11 with a video of an install that fits on a single CD-ROM."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/cadence-reveals-maestro-fine-tuned-ai-models-built-to-run-specialized-chip-design-agents-with-early-access-coming-for-select-customers-in-q4-2026-claims-up-to-30-percent-higher-quality-results-and-up-to-5x-token-efficiency-over-a-general-purpose-ai-model",
    "domain": "AI 算力 / 半导体",
    "title": "Cadence reveals Maestro, fine-tuned AI models built to run specialized chip design agents, with early access coming for 'select customers' in Q4 2026",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/cadence-reveals-maestro-fine-tuned-ai-models-built-to-run-specialized-chip-design-agents-with-early-access-coming-for-select-customers-in-q4-2026-claims-up-to-30-percent-higher-quality-results-and-up-to-5x-token-efficiency-over-a-general-purpose-ai-model",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T13:20:00+00:00",
    "summary": "Cadence unveiled Maestro, domain-specialized AI models for its chip design agents, with early access for select customers in Q4 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/chinese-research-vessels-loiter-near-pacific-undersea-cables-more-than-any-other-nation-report-finds-civilian-fleet-using-lawnmower-patterns-may-be-mapping-seafloor-for-future-sabotage",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese research vessels loiter near Pacific undersea cables more than any other nation, report finds",
    "url": "https://www.tomshardware.com/tech-industry/chinese-research-vessels-loiter-near-pacific-undersea-cables-more-than-any-other-nation-report-finds-civilian-fleet-using-lawnmower-patterns-may-be-mapping-seafloor-for-future-sabotage",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T13:00:00+00:00",
    "summary": "Chinese vessels are spending more time near undersea cables in the Pacific than nearly 50 other nations, according to a new report by the Center for Strategic and International Studies."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-explores-potential-collaboration-with-amd-as-lip-bu-tan-pushes-customer-focused-turnaround-ceo-targets-custom-chips-advanced-packaging-and-stronger-foundry-business",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's Lip-Bu Tan has spoken with Lisa Su about potential collaboration with AMD",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-explores-potential-collaboration-with-amd-as-lip-bu-tan-pushes-customer-focused-turnaround-ceo-targets-custom-chips-advanced-packaging-and-stronger-foundry-business",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T12:40:00+00:00",
    "summary": "Intel CEO Lip-Bu Tan has reportedly discussed potential areas of cooperation with AMD chief Lisa Su as Intel works to rebuild its CPU business and expand its foundry operations. The companies have alr"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-over-usd1-000-on-this-alienware-gaming-pc-with-an-rtx-5070-and-32gb-ddr5-unlock-1440p-and-4k-gameplay-with-this-aurora-act1250-rig-with-a-20-core-intel-cpu-and-a-1tb-ssd-for-usd2-199-99",
    "domain": "AI 算力 / 半导体",
    "title": "Save over $1,000 on this Alienware gaming PC with an RTX 5070 and 32GB DDR5",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-over-usd1-000-on-this-alienware-gaming-pc-with-an-rtx-5070-and-32gb-ddr5-unlock-1440p-and-4k-gameplay-with-this-aurora-act1250-rig-with-a-20-core-intel-cpu-and-a-1tb-ssd-for-usd2-199-99",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T12:20:00+00:00",
    "summary": "Newegg have cut this Alienware Aurora gaming PC by over $1,000, netting yo ua 4K-ready machine with an RTX 5070 and 32GB of DDR5 RAM for $2,199.99."
  },
  {
    "id": "hn:50086363",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's first GPU: GeForce 256",
    "url": "https://dfarq.homeip.net/nvidias-first-gpu-geforce-256/",
    "source": "ibobev",
    "platform": "hackernews",
    "points": 80,
    "published_at": "2026-10-14T12:05:44+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/in-orbit-useful-life-becomes-a-performance-metric/",
    "domain": "AI 算力 / 半导体",
    "title": "In Orbit, Useful Life Becomes a Performance Metric",
    "url": "https://www.eetimes.com/in-orbit-useful-life-becomes-a-performance-metric/",
    "source": "Ron Honig",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T08:25:36+00:00",
    "summary": "Google’s Project Suncatcher is testing AI hardware in space, where radiation, cooling, power, and hardware lifetime determine the economics of computing. The post In Orbit, Useful Life Becomes a Perfo"
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
    "id": "rss:https://semianalysis.com/2025/09/08/huawei-ascend-production-ramp/",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei Ascend Production Ramp: Die Banks, TSMC Continued Production, HBM is The Bottleneck",
    "url": "https://semianalysis.com/2025/09/08/huawei-ascend-production-ramp/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-08T09:54:57+00:00",
    "summary": "Compute is the lifeblood of AI. He who controls the spice controls the universe the compute will control the production of tokens and reap the benefits of AI. Without compute you do not have a seat at"
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/03/amazons-ai-resurgence-aws-anthropics-multi-gigawatt-trainium-expansion/",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon’s AI Resurgence: AWS & Anthropic’s Multi-Gigawatt Trainium Expansion",
    "url": "https://semianalysis.com/2025/09/03/amazons-ai-resurgence-aws-anthropics-multi-gigawatt-trainium-expansion/",
    "source": "Jeremie Eliahou Ontiveros",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-03T20:55:46+00:00",
    "summary": "Two-and-a-half years ago, we flagged a looming “cloud crisis” at AWS. Today, the evidence has mounted. AWS is the crown jewel of the Amazon empire, generating ~60% of group profits, and dominating the"
  },
  {
    "id": "rss:https://semianalysis.com/2025/08/20/h100-vs-gb200-nvl72-training-benchmarks/",
    "domain": "AI 算力 / 半导体",
    "title": "H100 vs GB200 NVL72 Training Benchmarks – Power, TCO, and Reliability Analysis, Software Improvement Over Time",
    "url": "https://semianalysis.com/2025/08/20/h100-vs-gb200-nvl72-training-benchmarks/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-20T04:56:35+00:00",
    "summary": "Frontier model training has pushed GPUs and AI systems to their absolute limits, making cost, efficiency, power, performance per TCO, and reliability central to the discussion on effective training. T"
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
    "points": 886,
    "published_at": "2026-10-27T16:06:01+00:00",
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
    "id": "rss:https://www.theverge.com/tech/1020145/iphone-duo-crackgate-broken-screen-hinge",
    "domain": "大厂 AI 动态",
    "title": "Here’s why the iPhone Duo’s hinge could be cracking the screen",
    "url": "https://www.theverge.com/tech/1020145/iphone-duo-crackgate-broken-screen-hinge",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T22:55:05+00:00",
    "summary": "Within hours of the iPhone Duo launch last Friday, people reported that the inner screen on some brand new foldable phones was already broken. The issue was similar across many photos shared on social"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1019921/openai-breakthrough-math-computer-science-physics",
    "domain": "大厂 AI 动态",
    "title": "Researchers are getting tired of OpenAI gatekeeping its breakthroughs",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1019921/openai-breakthrough-math-computer-science-physics",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T20:48:58+00:00",
    "summary": "On Monday, OpenAI announced impressive breakthroughs in mathematics, computer science, and physics, along with what the company says is an evolving approach to communicating its findings. But despite "
  },
  {
    "id": "rss:https://www.theverge.com/science/1019879/elon-musk-starlink-ukraine-terms-of-service",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk says Ukraine&#8217;s military violated Starlink&#8217;s terms of service",
    "url": "https://www.theverge.com/science/1019879/elon-musk-starlink-ukraine-terms-of-service",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T19:24:06+00:00",
    "summary": "Elon Musk claims Ukraine violated Starlink's terms of service before the recent slowdown, as reported earlier by Ars Technica. According to Musk, \"Ukraine military violated Starlink terms of service a"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1019691/gas-leak-methane-rule-rollback-trump",
    "domain": "大厂 AI 动态",
    "title": "Trump is making it easier for fossil fuel companies to leak methane",
    "url": "https://www.theverge.com/policy/1019691/gas-leak-methane-rule-rollback-trump",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T18:25:13+00:00",
    "summary": "In its latest gift to oil and gas companies, the Trump administration is expected to announce plans today to weaken rules that guard against methane leaks. Methane is a smog-forming pollutant and a po"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1017064/visionquest-marvel-rogue-ai",
    "domain": "大厂 AI 动态",
    "title": "VisionQuest is what happens when AI really goes rogue",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1017064/visionquest-marvel-rogue-ai",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T17:30:00+00:00",
    "summary": "In Marvel's VisionQuest, a superpowered robot tries to better understand humanity by getting lost in elaborate, digital daydreams in which he and other artificial intelligence-powered beings live toge"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1019484/super-mouse-touchscreen-shortcuts-macros-kickstarter",
    "domain": "大厂 AI 动态",
    "title": "The Super Mouse puts a touchscreen macro pad under your hand",
    "url": "https://www.theverge.com/tech/1019484/super-mouse-touchscreen-shortcuts-macros-kickstarter",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T17:00:00+00:00",
    "summary": "A company called Arctic Fox Technologies has announced a new multifunction mouse that forgoes a myriad of customizable shortcut buttons peppered across its surface for a compact touchscreen sitting be"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1019470/anthropic-ipo-resist-investor-pressure-cut-corners-safety",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s elaborate plan to keep Wall Street at bay",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1019470/anthropic-ipo-resist-investor-pressure-cut-corners-safety",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T16:51:22+00:00",
    "summary": "Anthropic wants to have it both ways. With its impending IPO, it wants to tap the vast riches of the public markets and insists it doesn't want to compromise its core mission of developing AI safely a"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1019604/new-mexico-meta-cambridge-analytica-kids-safety-settlement",
    "domain": "大厂 AI 动态",
    "title": "Meta’s $25 billion legal loss just put blood in the water",
    "url": "https://www.theverge.com/policy/1019604/new-mexico-meta-cambridge-analytica-kids-safety-settlement",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T16:44:40+00:00",
    "summary": "When attorneys general from across the US announced a $17 billion settlement with Meta this summer, the sum was unprecedented. But a ruling last week by a New Mexico judge blew that number out of the "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1019551/firefox-smart-window-ai-fill-forms",
    "domain": "大厂 AI 动态",
    "title": "Firefox’s Smart Window adds AI form filling and webpage monitoring",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1019551/firefox-smart-window-ai-fill-forms",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T16:14:18+00:00",
    "summary": "Mozilla is updating Smart Window - Firefox's AI-powered browsing experience - with a new feature that can help you fill out online forms based on your open tabs. As an example, Mozilla says Smart Wind"
  },
  {
    "id": "rss:https://www.theverge.com/report/1019478/major-league-baseball-fandom-social-media-world-series-influencers",
    "domain": "大厂 AI 动态",
    "title": "Major League Baseball is looking for a new kind of fan",
    "url": "https://www.theverge.com/report/1019478/major-league-baseball-fandom-social-media-world-series-influencers",
    "source": "Mia Sato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T16:02:43+00:00",
    "summary": "On October 2nd, just as Major League Baseball's Division Series was kicking off, the main MLB Instagram and TikTok accounts posted a video hyping up the teams still in the running for the World Series"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/jio-shares-surge-21-in-market-debut-after-blockbuster-india-ipo/",
    "domain": "大厂 AI 动态",
    "title": "Jio shares surge 21% in market debut after blockbuster India IPO",
    "url": "https://techcrunch.com/2026/10/27/jio-shares-surge-21-in-market-debut-after-blockbuster-india-ipo/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T05:20:32+00:00",
    "summary": "Jio has debuted as India's second-most valuable listed company, behind its parent, Reliance Industries."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/vcs-will-make-billions-on-anthropics-ipo-but-amazon-is-set-to-make-much-much-more/",
    "domain": "大厂 AI 动态",
    "title": "VCs will make billions on Anthropic’s IPO, but Amazon is set to make much (much) more",
    "url": "https://techcrunch.com/2026/10/27/vcs-will-make-billions-on-anthropics-ipo-but-amazon-is-set-to-make-much-much-more/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T01:15:28+00:00",
    "summary": "Massive note conversions reveal the true extent of Amazon's ownership in Anthropic."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/parents-sue-openai-alleging-gpt-4o-coached-their-daughter-off-seizure-medication/",
    "domain": "大厂 AI 动态",
    "title": "Parents sue OpenAI, alleging GPT-4o coached their daughter off seizure medication",
    "url": "https://techcrunch.com/2026/10/27/parents-sue-openai-alleging-gpt-4o-coached-their-daughter-off-seizure-medication/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T23:34:27+00:00",
    "summary": "A family is suing OpenAI, saying ChatGPT coached their daughter to quietly taper off her seizure medication and keep it from her doctors before she died in February."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/the-data-center-boom-has-an-upside-innovation-for-the-us-grid/",
    "domain": "大厂 AI 动态",
    "title": "The data center boom has an upside: innovation for the US grid",
    "url": "https://techcrunch.com/2026/10/27/the-data-center-boom-has-an-upside-innovation-for-the-us-grid/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T22:55:41+00:00",
    "summary": "As the AI boom stresses the existing power grid, all sorts of new opportunities for grid modernization are also emerging as a result, industry insiders say."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/guidewire-buys-hyperexponential-for-1-7b-in-cash/",
    "domain": "大厂 AI 动态",
    "title": "Guidewire buys Hyperexponential for $1.7B in cash",
    "url": "https://techcrunch.com/2026/10/27/guidewire-buys-hyperexponential-for-1-7b-in-cash/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T22:26:03+00:00",
    "summary": "The deal, expected to close sometime next year, is to help bring AI agents to work alongside humans to underwrite, analyze, and price decisions."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/from-8vc-to-benchmark-heres-whats-hiding-in-october-sec-filings/",
    "domain": "大厂 AI 动态",
    "title": "From 8VC to Benchmark, here’s what’s hiding in October SEC filings",
    "url": "https://techcrunch.com/2026/10/27/from-8vc-to-benchmark-heres-whats-hiding-in-october-sec-filings/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T22:17:18+00:00",
    "summary": "A whole crop of venture capital firms are raising significant new funds."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/gm-is-embracing-hybrids-now/",
    "domain": "大厂 AI 动态",
    "title": "GM is embracing hybrids now",
    "url": "https://techcrunch.com/2026/10/27/gm-is-embracing-hybrids-now/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T21:47:02+00:00",
    "summary": "GM eschewed hybrids in favor of battery-electric vehicles. Now it's gearing up to offer hybrid versions of its SUVs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/bank-of-america-kindly-asks-that-you-dont-share-your-banking-password-with-your-ai-assistant/",
    "domain": "大厂 AI 动态",
    "title": "Bank of America kindly asks that you don’t share your banking password with your AI assistant",
    "url": "https://techcrunch.com/2026/10/27/bank-of-america-kindly-asks-that-you-dont-share-your-banking-password-with-your-ai-assistant/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T21:44:34+00:00",
    "summary": "The banking giant reminds customers that \"you're responsible for activity\" resulting from your AI agents' access."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/whos-really-in-charge-at-anthropic-after-the-ipo/",
    "domain": "大厂 AI 动态",
    "title": "Who’s really in charge at Anthropic after the IPO?",
    "url": "https://techcrunch.com/2026/10/27/whos-really-in-charge-at-anthropic-after-the-ipo/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T21:38:28+00:00",
    "summary": "Here's a clear explanation of Anthropic's incredibly complex governance structure."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/discord-is-making-its-public-communities-more-searchable-and-people-have-concerns/",
    "domain": "大厂 AI 动态",
    "title": "Discord is making its public communities more searchable, and people have concerns",
    "url": "https://techcrunch.com/2026/10/27/discord-is-making-its-public-communities-more-searchable-and-people-have-concerns/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T21:22:35+00:00",
    "summary": "In December, messages from Discord's public discoverable servers will begin appearing in search engine results."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/rebuild-which-spun-out-slate-auto-raises-2-1b/",
    "domain": "大厂 AI 动态",
    "title": "Re:Build, which spun out Slate Auto, raises $2.1B",
    "url": "https://techcrunch.com/2026/10/27/rebuild-which-spun-out-slate-auto-raises-2-1b/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T20:31:17+00:00",
    "summary": "The manufacturing accelerator bills itself as \"America’s answer to Shenzhen.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/disruptive-raises-10b-fund-to-make-big-bets-on-at-least-10-companies/",
    "domain": "大厂 AI 动态",
    "title": "Disruptive raises $10B fund to make big bets on at least 10 companies",
    "url": "https://techcrunch.com/2026/10/27/disruptive-raises-10b-fund-to-make-big-bets-on-at-least-10-companies/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T18:55:35+00:00",
    "summary": "Disruptive has made headlines in recent years for pouring money into companies like chip startup Groq and the AI voice-generation startup ElevenLabs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/frontier-ai-labs-say-their-models-refuted-the-exponential-time-hypothesis-what-does-that-mean/",
    "domain": "大厂 AI 动态",
    "title": "Frontier AI labs say their models refuted the Exponential Time Hypothesis. What does that mean?",
    "url": "https://techcrunch.com/2026/10/27/frontier-ai-labs-say-their-models-refuted-the-exponential-time-hypothesis-what-does-that-mean/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T17:08:08+00:00",
    "summary": "TechCrunch spoke to the MIT computer scientist charged with explaining OpenAI's latest mind-bending discovery."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/googles-genie-4-world-model-adds-audio-more-realistic-worlds-and-real-time-steering/",
    "domain": "大厂 AI 动态",
    "title": "Google’s Genie 4 world model adds audio, more realistic worlds, and real-time steering",
    "url": "https://techcrunch.com/2026/10/27/googles-genie-4-world-model-adds-audio-more-realistic-worlds-and-real-time-steering/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T16:30:57+00:00",
    "summary": "Genie 4 can maintain a consistent scene for up to two minutes, double Genie 3's limit, and offers better physics and more humanlike characters."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/meta-ai-director-rohit-patel-leaves-to-take-on-microsoft-office-and-google-workspace/",
    "domain": "大厂 AI 动态",
    "title": "Meta AI director Rohit Patel leaves to take on Microsoft Office and Google Workspace",
    "url": "https://techcrunch.com/2026/10/27/meta-ai-director-rohit-patel-leaves-to-take-on-microsoft-office-and-google-workspace/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T14:59:09+00:00",
    "summary": "Rohit Patel is departing Meta after eight years working on AI evaluations and reinforcement learning, TechCrunch has exclusively learned. His startup, Ndoc, aims to take on Microsoft Office Suite."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/ford-fathom-will-be-the-cheapest-american-ev-capable-of-powering-a-house/",
    "domain": "大厂 AI 动态",
    "title": "Ford Fathom will be the cheapest American EV capable of powering a house",
    "url": "https://techcrunch.com/2026/10/27/ford-fathom-will-be-the-cheapest-american-ev-capable-of-powering-a-house/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T14:51:33+00:00",
    "summary": "Ford is rolling out two new chargers capable of powering a home or the grid — so-called V2X capability."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/us-government-says-hackers-are-now-exploiting-critical-php-web-bugs/",
    "domain": "大厂 AI 动态",
    "title": "US government says hackers are now exploiting critical PHP web bugs",
    "url": "https://techcrunch.com/2026/10/27/us-government-says-hackers-are-now-exploiting-critical-php-web-bugs/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T14:40:39+00:00",
    "summary": "The U.S. government cyber agency warns that hackers have figured out a way to exploit the popular PHP software, used in 70% of the web's software."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/apple-unveils-new-14-inch-macbook-pro-with-m6-chip/",
    "domain": "大厂 AI 动态",
    "title": "Apple unveils new 14-inch MacBook Pro with M6 chip",
    "url": "https://techcrunch.com/2026/10/27/apple-unveils-new-14-inch-macbook-pro-with-m6-chip/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T14:25:11+00:00",
    "summary": "The new MacBook Pro comes with 24 hours of battery life, and now features support for Wi-Fi 7 and Bluetooth 6 connectivity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/apple-rolls-out-ios-27-2-with-new-siri-ai-languages-and-security-fixes/",
    "domain": "大厂 AI 动态",
    "title": "Apple rolls out iOS 27.2 with new Siri AI languages and security fixes",
    "url": "https://techcrunch.com/2026/10/27/apple-rolls-out-ios-27-2-with-new-siri-ai-languages-and-security-fixes/",
    "source": "Ivan Mehta, Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T13:54:51+00:00",
    "summary": "The latest Apple software update for iPhones and iPads includes new features and important security updates."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/27/japan-internet-giant-gmo-says-hackers-posted-stolen-customer-data/",
    "domain": "大厂 AI 动态",
    "title": "Japan internet giant GMO says hackers posted stolen customer data",
    "url": "https://techcrunch.com/2026/10/27/japan-internet-giant-gmo-says-hackers-posted-stolen-customer-data/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T13:32:57+00:00",
    "summary": "Japan's GMO Internet is verifying alleged customer data posted by suspected hackers following a cloud service breach."
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
    "id": "rss:https://stratechery.com/2026/the-end-of-the-internet/",
    "domain": "大厂 AI 动态",
    "title": "The End of the Internet",
    "url": "https://stratechery.com/2026/the-end-of-the-internet/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-26T10:00:00+00:00",
    "summary": "The old Internet, where anyone could host a server is over, but it's just the final blow in an ending that has been coming for years. The future, though, is brighter than it appears."
  },
  {
    "id": "rss:https://arstechnica.com/apple/2026/10/apple-refreshes-the-imac-entry-level-macbook-pro-with-the-m6-chip/",
    "domain": "大厂 AI 动态",
    "title": "Apple refreshes the iMac, entry-level MacBook Pro with the M6 chip",
    "url": "https://arstechnica.com/apple/2026/10/apple-refreshes-the-imac-entry-level-macbook-pro-with-the-m6-chip/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T22:37:30+00:00",
    "summary": "Additionally, the N1 chip brings Wi-Fi 7 and Bluetooth 6."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/10/domestic-travel-poses-growing-risk-for-measles-and-a-new-challenge-for-states/",
    "domain": "大厂 AI 动态",
    "title": "South Carolina's measles outbreak jumped to Washington state 5 times in 2 weeks",
    "url": "https://arstechnica.com/health/2026/10/domestic-travel-poses-growing-risk-for-measles-and-a-new-challenge-for-states/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T22:22:32+00:00",
    "summary": "International travel used to be the main risk of measles cases in the US—not anymore."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/10/chinas-top-secret-spaceplane-cant-hide-in-low-earth-orbit/",
    "domain": "大厂 AI 动态",
    "title": "China's top-secret spaceplane can't hide in low-Earth orbit",
    "url": "https://arstechnica.com/space/2026/10/chinas-top-secret-spaceplane-cant-hide-in-low-earth-orbit/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T22:04:50+00:00",
    "summary": "The DIA's threat assessment suggests China may soon place directed energy weapons in space."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/10/no-human-at-the-helm-delaware-plan-would-let-ai-agents-run-entire-businesses/",
    "domain": "大厂 AI 动态",
    "title": "\"No human at the helm\": Delaware plan would let AI agents run entire businesses",
    "url": "https://arstechnica.com/tech-policy/2026/10/no-human-at-the-helm-delaware-plan-would-let-ai-agents-run-entire-businesses/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T21:50:04+00:00",
    "summary": "Owners of AI-run firms would evade liability for \"reckless\" AI, US Rep. Comer says."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/10/anthropic-ipo-warns-its-ai-could-blackmail-people-become-sentient-end-humanity/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic IPO warns its AI could blackmail people, become sentient, end humanity",
    "url": "https://arstechnica.com/ai/2026/10/anthropic-ipo-warns-its-ai-could-blackmail-people-become-sentient-end-humanity/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T21:31:14+00:00",
    "summary": "Seven potential AI nightmares pulled from Anthropic's 93-page \"Risk Factor\" tome."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/10/code-execution-flaw-in-uefi-firmware-threatens-most-servers-on-planet-earth/",
    "domain": "大厂 AI 动态",
    "title": "Code-execution flaw in UEFI firmware affects most servers on planet Earth",
    "url": "https://arstechnica.com/security/2026/10/code-execution-flaw-in-uefi-firmware-threatens-most-servers-on-planet-earth/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T20:25:55+00:00",
    "summary": "Critical flaw in EDK2 allows attackers to execute code early in the boot process."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/googles-android-registered-app-stores-program-launches-dec-1-applications-now-open/",
    "domain": "大厂 AI 动态",
    "title": "Google begins certifying Registered App Stores for Android, but not in the US",
    "url": "https://arstechnica.com/gadgets/2026/10/googles-android-registered-app-stores-program-launches-dec-1-applications-now-open/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T19:32:07+00:00",
    "summary": "Easier app installs are coming to third-party stores, pending Google's stamp of approval."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/vibe-genes-naturalish-language-comes-to-protein-genome-design-software/",
    "domain": "大厂 AI 动态",
    "title": "Vibe genes? Natural(ish) language comes to protein, genome design software",
    "url": "https://arstechnica.com/science/2026/10/vibe-genes-naturalish-language-comes-to-protein-genome-design-software/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T18:49:08+00:00",
    "summary": "You can apparently now tell AI tools what sort of protein you want them to make."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/10/warner-bros-drops-final-trailer-for-dune-part-three/",
    "domain": "大厂 AI 动态",
    "title": "Warner Bros. drops final trailer for Dune: Part Three",
    "url": "https://arstechnica.com/culture/2026/10/warner-bros-drops-final-trailer-for-dune-part-three/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T18:05:55+00:00",
    "summary": "\"After years of combat, I've become the oppressor Chani had sworn to fight.\""
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/10/ford-builds-bidrectional-charging-into-its-30k-electric-truck/",
    "domain": "大厂 AI 动态",
    "title": "Ford simplifies using your EV as a home battery with the $30K Fathom",
    "url": "https://arstechnica.com/cars/2026/10/ford-builds-bidrectional-charging-into-its-30k-electric-truck/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-27T16:17:58+00:00",
    "summary": "The Fathom pickup won’t need a wall-mounted inverter to output 10 kW to your house."
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
    "id": "hn:50232604",
    "domain": "股票",
    "title": "Microsoft and others tell crypto platform not to tokenize their stocks",
    "url": "https://gizmodo.com/microsoft-mcdonalds-verizon-and-others-tell-crypto-platform-not-to-tokenize-their-stocks-2000830368",
    "source": "gumby",
    "platform": "hackernews",
    "points": 98,
    "published_at": "2026-10-25T15:28:40+00:00",
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
    "id": "hn:50254255",
    "domain": "股票",
    "title": "Pentagon orders bases to plan for 90 days without the grid",
    "url": "https://fortune.com/2026/10/26/pentagon-fortress-bases-90-days-off-grid-uk-be-ready-stockpile/",
    "source": "russfink",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-10-27T03:02:29+00:00",
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
    "points": 168,
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
    "id": "hn:50239430",
    "domain": "金融",
    "title": "Tesla cancels Cybertruck in Australia and NZ after 7 years of deposits",
    "url": "https://electrek.co/2026/10/23/tesla-cancels-cybertruck-australia-new-zealand/",
    "source": "MilnerRoute",
    "platform": "hackernews",
    "points": 96,
    "published_at": "2026-10-26T05:13:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50253630",
    "domain": "金融",
    "title": "The 'Buy, Borrow and Die' Wealth Strategy Has Become a $5T Market",
    "url": "https://www.wsj.com/finance/the-buy-borrow-and-die-wealth-strategy-has-become-a-5-trillion-market-d9149a9d",
    "source": "tysone",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-10-27T01:30:08+00:00",
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
    "id": "rss:https://arxiv.org/abs/2610.35986",
    "domain": "金融",
    "title": "Leveraging US Commercial Adjustments: MFN Tariffs and Trade Diversion",
    "url": "https://arxiv.org/abs/2610.35986",
    "source": "Maria Cipollina, Luca De Benedictis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.35986v1 Announce Type: new Abstract: Most-favored-nation (MFN) tariff increases do more than raise trade costs. By changing the relative tariff treatment of competing exporters, they increa"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.36008",
    "domain": "金融",
    "title": "Practice Makes Perfect: Tacit Knowledge, Generative AI, and Returns to Schooling and Experience",
    "url": "https://arxiv.org/abs/2610.36008",
    "source": "Eduardo Levy Yeyati, Dar\\'io Judzik, Juan Ignacio Barbiero",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.36008v1 Announce Type: new Abstract: Generative AI changes the scarcity of different forms of human capital. It makes codified knowledge cheaply available at the point of production, while "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.36171",
    "domain": "金融",
    "title": "From Tariff Changes to Trade Effects: A Practical Framework for Empirical Trade Policy Analysis",
    "url": "https://arxiv.org/abs/2610.36171",
    "source": "Maria Cipollina, Luca De Benedictis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.36171v1 Announce Type: new Abstract: After decades of trade liberalization, the 2020s mark a profound shift in the globalization narrative, with tariffs once again becoming a central instru"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.36274",
    "domain": "金融",
    "title": "Does Ecosystem Activity Validate TVL?",
    "url": "https://arxiv.org/abs/2610.36274",
    "source": "Matthew Brigida",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.36274v1 Announce Type: new Abstract: Total value locked (TVL) is widely used to assess decentralized finance ecosystems. Prior evidence finds that portfolios formed on TVL alone are spanned"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.36317",
    "domain": "金融",
    "title": "Event definition and the branching ratio: Hawkes estimates of price-change clustering in the consolidated quote feed",
    "url": "https://arxiv.org/abs/2610.36317",
    "source": "Hyoeun Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.36317v1 Announce Type: new Abstract: Hawkes models of price changes in the consolidated US quote feed find a sub-millisecond kernel component and a branching ratio near criticality. We show"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.36392",
    "domain": "金融",
    "title": "The Term Structure of Implied Fee Rates in Liquidity Pools",
    "url": "https://arxiv.org/abs/2610.36392",
    "source": "Diogo Duarte, Lucas X. Ferreira, Emmanuel Gobet, Yuri F. Saporito",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.36392v1 Announce Type: new Abstract: We develop a no-arbitrage framework to recover implied fee rates from option-implied information and quantify fee compensation for liquidity providers i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.36491",
    "domain": "金融",
    "title": "Simple Portfolios that Deliver Consistent Decent Returns",
    "url": "https://arxiv.org/abs/2610.36491",
    "source": "Oskar Ed\\'en Wallberg, Alexander Karolin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.36491v1 Announce Type: new Abstract: Portfolio construction has been studied extensively in both academia and industry. Its applications range from pension funds and hedge funds to private "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.36899",
    "domain": "金融",
    "title": "Depositing More Should Not Earn Less: Supplier Income Monotonicity and Rate Curve Design in Pooled Lending Markets",
    "url": "https://arxiv.org/abs/2610.36899",
    "source": "Ahzam Khan, Cavey Cool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.36899v1 Announce Type: new Abstract: In utilization dependent interest rate models, adding liquidity can reduce a supplier's total interest income even as the supplier's balance increases. "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.36921",
    "domain": "金融",
    "title": "A Deep Learning-Driven Operator Splitting Scheme for Free Boundary Problems: An Application to American Option Pricing in Incomplete Markets",
    "url": "https://arxiv.org/abs/2610.36921",
    "source": "Dong Yan, Haocheng Zhu, Yao Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.36921v1 Announce Type: new Abstract: This paper proposes a deep learning-driven operator splitting scheme for high-dimensional free-boundary problems, with American option pricing as a repr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.37171",
    "domain": "金融",
    "title": "An Application of Geometric Riemannian Pricing Algorithm for Valuing Catastrophe Bonds in Incomplete Markets: Market-Consistent Financial Entropy and the Split of Frequency and Severity Risk Premia",
    "url": "https://arxiv.org/abs/2610.37171",
    "source": "Saeid Safarveisi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.37171v1 Announce Type: new Abstract: This paper presents a framework for pricing catastrophe (CAT) bonds in incomplete markets through Riemannian geometric optimization of financial entropy"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.37306",
    "domain": "金融",
    "title": "Climate change, sea level rise, and the agricultural revolution",
    "url": "https://arxiv.org/abs/2610.37306",
    "source": "Ridhika Mishra, Richard S. J. Tol",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.37306v1 Announce Type: new Abstract: We test various hypotheses for the invention and spread of agriculture: higher temperatures, increased seasonality, carbon dioxide fertilization, sea le"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.37324",
    "domain": "金融",
    "title": "Optimal Order Placement under a State-Dependent Hawkes Process Limit Order Book model",
    "url": "https://arxiv.org/abs/2610.37324",
    "source": "Jonathan Ch\\'avez Casillas, Li Gan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.37324v1 Announce Type: new Abstract: We study optimal quote placement for a market maker facing order flow modeled by a state-dependent Hawkes process. A block-based linear demand specifica"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.37445",
    "domain": "金融",
    "title": "Hosting is not capturing: an exposure-capability framework and Hungary's electric-vehicle battery bet",
    "url": "https://arxiv.org/abs/2610.37445",
    "source": "Zoltan Bartha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.37445v1 Announce Type: new Abstract: How should a dependent economy respond when a polycrisis turns economic integration from a source of efficiency into a surface of vulnerability? This pa"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.37487",
    "domain": "金融",
    "title": "Contemporaneous Transmission Networks and Systemic Risk in European Banking",
    "url": "https://arxiv.org/abs/2610.37487",
    "source": "Minh Duc Duong, Alessio Moneta, Fabrizio Lillo, Caterina Giannetti, Tu Anh Doan Nguyen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.37487v1 Announce Type: new Abstract: We study how contemporaneous equity-return transmission shapes systemic exposure among 51 listed European banks. Using a recursive non-Gaussian network "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.35887",
    "domain": "金融",
    "title": "Evaluating the Predictive Validity of ICT's Accumulation-Manipulation-Distribution (AMD) Model on CME E-Mini NASDAQ-100 Futures",
    "url": "https://arxiv.org/abs/2610.35887",
    "source": "Veer Taylor",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.35887v1 Announce Type: cross Abstract: To our knowledge, this paper provides the first systematic quantitative evaluation of the ICT Accumulation-Manipulation-Distribution (AMD) model on CM"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.35893",
    "domain": "金融",
    "title": "Reconstructing the Human Development Index at the Individual Level from Survey Microdata: Development and Validation of a Methodology",
    "url": "https://arxiv.org/abs/2610.35893",
    "source": "Tcharlies Bachmann Schmitz (PX Center, Brazil), Natalia Veronez da Cunha (Universidade do Planalto Catarinense, UNIPLAC), Isabelle Ferreira (Universidade do Planalto Catarinense, UNIPLAC)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.35893v1 Announce Type: cross Abstract: This study proposes and validates a methodology for reconstructing the Human Development Index (HDI) from individual-level survey microdata, enabling "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.36473",
    "domain": "金融",
    "title": "Risk measures for infinite-server queues driven by a Cox-BESQ process",
    "url": "https://arxiv.org/abs/2610.36473",
    "source": "Jos\\'{e} Da Fonseca, Yajun Shi, Wenjun Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.36473v1 Announce Type: cross Abstract: This paper introduces a model for infinite-server queues driven by a Cox process with stochastic intensity given by a squared Bessel (BESQ) process. E"
  },
  {
    "id": "rss:https://arxiv.org/abs/2411.01582",
    "domain": "金融",
    "title": "Matching-LLM: Historically Anchored Synthetic Prediction of Public Opinion and Elections",
    "url": "https://arxiv.org/abs/2411.01582",
    "source": "Shapeng Jiang, Lijia Wei, Chen Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2411.01582v3 Announce Type: replace Abstract: Large language models (LLMs) offer new opportunities for predicting public opinion and electoral behavior, but their synthetic responses may not ful"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.17866",
    "domain": "金融",
    "title": "Narratives to Numbers: Large Language Models and Economic Policy Uncertainty",
    "url": "https://arxiv.org/abs/2511.17866",
    "source": "Ethan Hartley",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2511.17866v3 Announce Type: replace Abstract: We study the implications of adopting machine-generated data in economic analysis. Rather than taking the data-generating process as given and corre"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04529",
    "domain": "金融",
    "title": "Low-rank and graphon limits for dynamic threshold distress contagion in heterogeneous financial networks",
    "url": "https://arxiv.org/abs/2608.04529",
    "source": "Pengbin Feng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2608.04529v5 Announce Type: replace Abstract: We study how financial distress propagates through a directed network when institutions can recover and become distressed again. Each institution's "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.24035",
    "domain": "金融",
    "title": "TRACE: Governing AI-Assisted Research with Principles from Computer Science",
    "url": "https://arxiv.org/abs/2610.24035",
    "source": "Amirhossein Zohrehvand, Aldona Kapacinskaite",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.24035v2 Announce Type: replace Abstract: Artificial intelligence (AI) has made it easier than ever to produce research outputs. Adding an agentic tool to a research team's work potentially "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.27751",
    "domain": "金融",
    "title": "Market Regime-Based Multi-Asset Portfolio Optimization Using Nested Clustered Optimization for Tactical Asset Allocation",
    "url": "https://arxiv.org/abs/2610.27751",
    "source": "Supriadi, Bambang Siswoyo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.27751v3 Announce Type: replace Abstract: We investigate the interaction between market regime detection and Nested Clustered Optimization (NCO) for tactical asset allocation across heteroge"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.29578",
    "domain": "金融",
    "title": "What Prediction-Market Contracts Reveal at Launch: Trading Volume and Dispute Risk",
    "url": "https://arxiv.org/abs/2610.29578",
    "source": "Ahmed Mahrous, Roberto Di Pietro",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.29578v2 Announce Type: replace Abstract: Using a near-census of 802,863 resolved markets listed on Polymarket between January 2023 and May 2026, and only information available at listing (t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.34153",
    "domain": "金融",
    "title": "Certifying Reward Alignment in Portfolio Reinforcement Learning",
    "url": "https://arxiv.org/abs/2610.34153",
    "source": "Matin Tavakoli, Seyedreza Tavakoli, Faezeh Salmani, Amir Amini, Mohammad Hosein Rohban, Gholamali Aminian, Ali Habibnia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-28T04:00:00+00:00",
    "summary": "arXiv:2610.34153v2 Announce Type: replace Abstract: Financial reinforcement learning often translates an investment objective into an additive risk-adjusted reward. An agent can optimise that reward a"
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
    "points": 53,
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
  }
]
```
