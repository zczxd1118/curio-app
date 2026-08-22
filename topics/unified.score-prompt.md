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

- 今日日期：`2026-08-22`
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
  "date": "2026-08-22",
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
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1337082,
    "published_at": "2026-07-05T02:00:00+00:00",
    "summary": "用不上codex的朋友们！新的国产Agent直接上手，来跑通8大用法～\n感谢朋友们的三连+关注～"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1164990,
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
    "points": 1087867,
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
    "points": 876600,
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
    "points": 611232,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 563477,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 439059,
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
    "points": 420985,
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
    "points": 400038,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 270657,
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
    "points": 248362,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 243981,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 179632,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV16Luq6FEmP",
    "domain": "AI",
    "title": "当不懂代码的老婆，第一次接触vibe coding……",
    "url": "http://www.bilibili.com/video/av117076211536327",
    "source": "糖果果的未来要发光",
    "platform": "bilibili",
    "points": 175831,
    "published_at": "2026-08-11T09:50:27+00:00",
    "summary": "当不懂代码的老婆，第一次接触vibe coding……"
  },
  {
    "id": "bvid:BV1b5AeeGEFc",
    "domain": "AI",
    "title": "Cursor太贵？分享三个免费AI编程方案+海量编程技巧【如何看待AI编程】",
    "url": "http://www.bilibili.com/video/av114025056699722",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 159415,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV14egj6nELQ",
    "domain": "AI",
    "title": "一个导演Agent，帮你榨干Seedance2.5",
    "url": "http://www.bilibili.com/video/av117083006376875",
    "source": "AI视次方",
    "platform": "bilibili",
    "points": 152456,
    "published_at": "2026-08-13T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 139856,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1kGo6BdEsT",
    "domain": "AI",
    "title": "如何用Claude Skill 做高质量 PPT（附完整教程）",
    "url": "http://www.bilibili.com/video/av116474832361424",
    "source": "阿西_出海",
    "platform": "bilibili",
    "points": 97304,
    "published_at": "2026-04-27T04:45:20+00:00",
    "summary": "很多人问我上期爆了的那条视频里，那个 PPT 是怎么做的。\n其实我是用 Anthropic 最近出的 Claude Design 做的，这个功能一发出来就在全网传疯了，一条推文就冲上了 6000 多万曝光。\n本期视频我会带你手把手从 0 到 1 把这个Skill 装好，然后一起跑一个成品效果出来。"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93319,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 93074,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 63567,
    "published_at": "2026-03-30T16:47:51+00:00",
    "summary": "Everything Claude Code 是目前 GitHub 上 116K star 的 Claude Code 配置项目。本期从斜杠命令、子代理、Hooks 到学习系统，带你把这个项目真正用起来。"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54317,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1myM96nETU",
    "domain": "AI",
    "title": "AI 赛博女友！本地部署教程，无需 API、完全免费，8G显存就能跑！实时语音聊天，几乎零延迟，太上头了！| 零度解说",
    "url": "http://www.bilibili.com/video/av117032322339286",
    "source": "零度解说",
    "platform": "bilibili",
    "points": 53706,
    "published_at": "2026-08-04T12:00:00+00:00",
    "summary": "AI 赛博女友一键安装包下载：https://www.freedidi.com/24984.html"
  },
  {
    "id": "bvid:BV1TxqXY4Egj",
    "domain": "AI",
    "title": "Cursor、WindSurf大乱斗，AI编程哪家强？",
    "url": "http://www.bilibili.com/video/av113635540079115",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 48024,
    "published_at": "2024-12-11T23:05:00+00:00",
    "summary": "我的个人主页：huasheng.ai\n\nCursor最近推出了agent模式,与Windsurf的Cascade功能非常相似。本期视频通过一个实际的小例子,对比了Cursor和Windsurf在代码编辑方面的差异和优势。\n\n时间戳:\n00:00 Windsurf的出现与Cursor的更新\n00:33 Cursor新增agent模式\n01:20 本期视频主要内容介绍\n01:40 案例背景:花生校对网"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47641,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 45511,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 40896,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1cCj2ztEf5",
    "domain": "AI",
    "title": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%",
    "url": "http://www.bilibili.com/video/av114574527307727",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 35152,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34164,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29644,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 29432,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1vwXPYkEGx",
    "domain": "AI",
    "title": "Cursor+mcp配置，手把手教你配置任意MCP服务，学不会你打我，小白保姆级教程~MCP服务配置指南 - 提升AI编程助手能力",
    "url": "http://www.bilibili.com/video/av114193181183930",
    "source": "三少科技",
    "platform": "bilibili",
    "points": 27193,
    "published_at": "2025-03-20T05:51:23+00:00",
    "summary": "我的知识星球，https://t.zsxq.com/jVAk9\n\n📌 本期教程通过实战演示，教你在Cursor中配置和使用MCP服务器，特别是filesystem MCP服务，解决Cursor无法写入文件的常见问题。\n⏱️ 内容概要：\n00:00 介绍MCP及其重要性\n02:00 Cursor抽风问题与MCP解决方案\n04:00 配置第一个MCP服务器（filesystem）\n07:00 Wind"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 26644,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22728,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 22220,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 19866,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1PmMk6SEm1",
    "domain": "AI",
    "title": "用Codex智能体自动跑通全流程，一人公司简直不要太爽！",
    "url": "http://www.bilibili.com/video/av117041650474867",
    "source": "公司就我一个人-",
    "platform": "bilibili",
    "points": 18913,
    "published_at": "2026-08-05T07:17:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17733,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1e5j2z7Ekb",
    "domain": "AI",
    "title": "让Cursor编程更Vibe的专业显示器？",
    "url": "http://www.bilibili.com/video/av114572631542889",
    "source": "熠辉IndieDev",
    "platform": "bilibili",
    "points": 13943,
    "published_at": "2025-05-27T03:00:00+00:00",
    "summary": "我终于发现了用Cursor来AI编程的完美搭子！"
  },
  {
    "id": "bvid:BV11EJn6JEk9",
    "domain": "AI",
    "title": "claude+ccswitch配置glm5.2",
    "url": "http://www.bilibili.com/video/av116742495999581",
    "source": "cctryflow",
    "platform": "bilibili",
    "points": 13901,
    "published_at": "2026-06-13T11:13:45+00:00",
    "summary": "智谱文档：https://docs.bigmodel.cn/cn/coding-plan/latest-model"
  },
  {
    "id": "bvid:BV1tU8q6FEEC",
    "domain": "AI",
    "title": "打造全能家用服务器，结果炸了！物理意义上的...",
    "url": "http://www.bilibili.com/video/av117132398433505",
    "source": "脏小豆",
    "platform": "bilibili",
    "points": 11789,
    "published_at": "2026-08-22T02:00:00+00:00",
    "summary": "我才发现，电源好像是一直吃cpu的尾气....\n这nas里还有好多没剪的片子，要是炸了我也炸了。"
  },
  {
    "id": "bvid:BV1rEJ8znEoj",
    "domain": "AI",
    "title": "Cursor+Stagewise插件，给ＡI装上眼睛，前端可视化编程，开发效率提升10倍！",
    "url": "http://www.bilibili.com/video/av114540016572317",
    "source": "为梦想的旅途助力",
    "platform": "bilibili",
    "points": 11389,
    "published_at": "2025-05-20T11:55:43+00:00",
    "summary": "想象一下，您可以将浏览器环境变成轻量级的可视化编辑器，以便您可以直接在浏览器中与 AI 聊天来修改屏幕上的任何 UI，并且它会立即在您的 Cursor 中完成工作。\n\nStagewise能够将您的浏览器用户界面与代码编辑器相连接，为您的 AI 代理提供实时上下文。\n\n大白话就是你可以在网页上任意地方选择，然后一键发送需要修改或者完善的内容给AI编辑器，Cursor这类编辑器就收到了指令，然后开始工"
  },
  {
    "id": "bvid:BV1Nu3M6bEXE",
    "domain": "AI",
    "title": "【上海交大张倬胜】大模型系列课程从入门到精通，手把手教学，保姆级教程！涵盖预训练模型微调与部署、提示学习与思维链、模型水印、多模态大模型，比啃书效果好多了",
    "url": "http://www.bilibili.com/video/av116979859984479",
    "source": "大模型新手教程",
    "platform": "bilibili",
    "points": 11134,
    "published_at": "2026-07-25T09:34:49+00:00",
    "summary": "【上海交大张倬胜】大模型系列课程从入门到精通，手把手教学，保姆级教程！涵盖预训练模型微调与部署、提示学习与思维链、模型水印、多模态大模型，比啃书效果好多了，草履虫都能学会！"
  },
  {
    "id": "bvid:BV1zbduYgEBH",
    "domain": "AI",
    "title": "Cursor新手教程⑤：Cursor降智真相+解决办法",
    "url": "http://www.bilibili.com/video/av114311359891940",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 10899,
    "published_at": "2025-04-10T02:53:27+00:00",
    "summary": "你是不是经常碰到这种情况：\n你试图修复一个小错误\n人工智能给出一个看似合理的更改建议\n这个修复导致其他地方出错\n你要求人工智能修复新出现的问题\n这又产生了另外两个问题\n如此反复\n本视频带你拆解Cursor降智的真相以及解决办法"
  },
  {
    "id": "bvid:BV14uTM69EUd",
    "domain": "AI",
    "title": "破甲claude/减少claude道德约束/ai破解卡密",
    "url": "http://www.bilibili.com/video/av116826918880943",
    "source": "去码头整点海鸥啊",
    "platform": "bilibili",
    "points": 9684,
    "published_at": "2026-06-28T09:05:03+00:00",
    "summary": "企鹅交流群：1038830654"
  },
  {
    "id": "bvid:BV1GvmzBUEfj",
    "domain": "AI",
    "title": "【AI杂谈】3 claude code概念讲解与配置",
    "url": "http://www.bilibili.com/video/av115718414668601",
    "source": "左-岚",
    "platform": "bilibili",
    "points": 9585,
    "published_at": "2025-12-14T14:38:05+00:00",
    "summary": "飞书的ai杂谈目录下\nhttps://my.feishu.cn/wiki/space/7600816265116011716\n\n米醋工作室 AI 开发环境配置完整指南https://www.micu.wiki/t/topic/571\nClaude Code 常见问题与故障排查https://www.micu.wiki/t/topic/570\nClaude Code 核心概念详解\nhttps://w"
  },
  {
    "id": "bvid:BV1jbXKBGECC",
    "domain": "AI",
    "title": "从零实现自己的agent第一期：什么是agent",
    "url": "http://www.bilibili.com/video/av116300500178517",
    "source": "小单说AI",
    "platform": "bilibili",
    "points": 9513,
    "published_at": "2026-03-27T09:48:18+00:00",
    "summary": "源码地址放这里了：\n\n📦 教学仓库：https://\ngithub.com/TheSyart/claude-agent-examples\n⚔️ 实战项目：https://github.com/TheSyart/emperor-agent\n\n我会持续更新 Agent 教学与实战内容。\n\n觉得有用的话，帮忙点个 Star ⭐\n谢谢大家支持。"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9388,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 9038,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 8753,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "hn:49255710",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Risky Business",
    "url": "https://stratechery.com/2026/nvidias-risky-business/",
    "source": "jonbaer",
    "platform": "hackernews",
    "points": 356,
    "published_at": "2026-08-11T10:02:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:49323686",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia dramatically reduces amount of OpenAI infra financing it may guarantee",
    "url": "https://www.reuters.com/business/nvidia-scales-back-250-billion-openai-data-center-guarantee-wsj-reports-2026-08-14/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 252,
    "published_at": "2026-08-16T21:07:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49263340",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Lightning and NeMo Switchyard",
    "url": "https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/",
    "source": "droidjj",
    "platform": "hackernews",
    "points": 262,
    "published_at": "2026-08-11T19:35:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:49387755",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia AVO scores 100% on the ARC-AGI-3 interactive reasoning benchmark",
    "url": "https://twitter.com/NVIDIAAI/status/2090786258981466231",
    "source": "dsrtslnd23",
    "platform": "hackernews",
    "points": 67,
    "published_at": "2026-08-21T13:26:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49257947",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Lightning",
    "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4",
    "source": "beklein",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-08-11T13:26:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:49388268",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia AVO achieves 100% in ARC-AGI-3",
    "url": "https://developer.nvidia.com/blog/nvidia-avo-reaches-100-on-arc-agi-3-demonstrating-a-frontier-level-general-purpose-architecture-for-long-horizon-autonomous-agents/",
    "source": "rochansinha",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-08-21T14:05:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49393647",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia just showed that the harness, not the AI model, is now the real hero",
    "url": "https://techcrunch.com/2026/08/21/nvidia-just-showed-that-the-harness-not-the-ai-model-is-now-the-real-hero/",
    "source": "dthread3",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-08-21T20:52:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49342314",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discloses $21B stake in SpaceX",
    "url": "https://arstechnica.com/information-technology/2026/08/nvidia-discloses-21b-stake-in-spacex/",
    "source": "joozio",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-08-18T07:02:04+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/chinas-nand-specialist-ymtc-moves-closer-to-ipo/",
    "domain": "AI 算力 / 半导体",
    "title": "China’s NAND Specialist YMTC Moves Closer to IPO",
    "url": "https://www.eetimes.com/chinas-nand-specialist-ymtc-moves-closer-to-ipo/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T13:51:09+00:00",
    "summary": "YMTC must raise capital to explore demand for AI-driven memory while balancing domestic and overseas markets. The post China’s NAND Specialist YMTC Moves Closer to IPO appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/the-human-brain-versus-ai-similar-results-very-different-machines/",
    "domain": "AI 算力 / 半导体",
    "title": "The Human Brain Versus AI: Similar Results, Very Different Machines",
    "url": "https://www.eetimes.com/the-human-brain-versus-ai-similar-results-very-different-machines/",
    "source": "Lauro Rizzatti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T07:43:42+00:00",
    "summary": "Contrast 20 watts with a megawatt: The brain and the LLM aren’t in the same race. The post The Human Brain Versus AI: Similar Results, Very Different Machines appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/synopsys-updates-cxl-ip-portfolio-for-ai-era-infrastructure/",
    "domain": "AI 算力 / 半导体",
    "title": "Synopsys Updates CXL IP Portfolio for AI-Era Infrastructure",
    "url": "https://www.eetimes.com/synopsys-updates-cxl-ip-portfolio-for-ai-era-infrastructure/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T14:07:45+00:00",
    "summary": "Synopsys’s CXL 4.0 IP aims to help designers build faster, more flexible and secure disaggregated computing architectures as AI systems demand more memory capacity and bandwidth. The post Synopsys Upd"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-a-full-size-keychron-mechanical-keyboard-for-just-usd29-50-percent-off-this-104-key-wired-keeb-with-your-choice-of-keychron-super-brown-or-red-switches",
    "domain": "AI 算力 / 半导体",
    "title": "Get a full-size Keychron mechanical keyboard for just $29 — 50% off this 104-key wired keeb with your choice of Keychron Super Brown or Red switches",
    "url": "https://www.tomshardware.com/pc-components/get-a-full-size-keychron-mechanical-keyboard-for-just-usd29-50-percent-off-this-104-key-wired-keeb-with-your-choice-of-keychron-super-brown-or-red-switches",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T16:45:23+00:00",
    "summary": "Keychron’s C2 Pro full-size wired mechanical keyboard hits an all time low of $29.99 at W00t with code KEYCHRON ($24.99 if you’re new to Woot) - QMK programmability, pre-lubed switches, make this a gr"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-a-usd75-discount-on-your-next-corsair-upgrade-stack-your-cart-up-to-usd350-to-enjoy-big-savings",
    "domain": "AI 算力 / 半导体",
    "title": "Get a $75 discount on your next Corsair upgrade — stack your cart up to $350 to enjoy big savings",
    "url": "https://www.tomshardware.com/pc-components/get-a-usd75-discount-on-your-next-corsair-upgrade-stack-your-cart-up-to-usd350-to-enjoy-big-savings",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T15:27:27+00:00",
    "summary": "Corsair launches a back-to-school promotion offering $75 off qualifying purchases of $350 or more in the U.S."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/external-ssds/sandisk-expansion-cards-for-xbox-series-x-s-now-available-on-amazon-alternative-storage-solution-to-seagate-wd-arrives-on-the-market-five-years-after-the-launch-of-the-consoles",
    "domain": "AI 算力 / 半导体",
    "title": "SanDisk expansion cards for Xbox Series X|S now available on Amazon — alternative storage solution to Seagate, WD arrives on the market five years after the launch of the consoles",
    "url": "https://www.tomshardware.com/pc-components/external-ssds/sandisk-expansion-cards-for-xbox-series-x-s-now-available-on-amazon-alternative-storage-solution-to-seagate-wd-arrives-on-the-market-five-years-after-the-launch-of-the-consoles",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T15:25:29+00:00",
    "summary": "The SanDisk Optimus GX C50 expansion cards for the Xbox Series X|S are now available on Amazon starting at $249.99 for the 1TB variant. While gamers can use external drives to copy and backup games fr"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-fights-to-keep-chatgpt-lawsuit-away-from-a-state-jury",
    "domain": "AI 算力 / 半导体",
    "title": "Florida seeks court ruling to officially classify Sam Altman and ChatGPT as a 'public nuisance' — OpenAI fights to keep lawsuit away from a state jury",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-fights-to-keep-chatgpt-lawsuit-away-from-a-state-jury",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T15:11:18+00:00",
    "summary": "Florida's lawsuit against OpenAI and Sam Altman has now been sitting before U.S. District Judge Aileen Cannon in Fort Pierce for seven weeks."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/worlds-largest-open-library-calls-for-volunteers-to-scan-and-preserve-physical-books-as-ai-companies-buy-scan-and-destroy-them-annas-archive-says-time-is-running-out-as-knowledge-is-permanently-monopolized-on-private-servers",
    "domain": "AI 算力 / 半导体",
    "title": "World's largest open library calls for volunteers to scan and preserve physical books as AI companies buy, scan, and destroy them — Anna's Archive says ‘time is running out’ as ‘knowledge is permanent",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/worlds-largest-open-library-calls-for-volunteers-to-scan-and-preserve-physical-books-as-ai-companies-buy-scan-and-destroy-them-annas-archive-says-time-is-running-out-as-knowledge-is-permanently-monopolized-on-private-servers",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T14:33:36+00:00",
    "summary": "A volunteer for Anna's Archive is calling for volunteers to scan and upload books to the shadow library to help preserve human knowledge for the public. The move comes as more AI companies buy, scan, "
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/elegoo-centauri-2-combo-review",
    "domain": "AI 算力 / 半导体",
    "title": "Elegoo Centauri 2 Combo review: A budget-friendly printer made even more budget-friendly",
    "url": "https://www.tomshardware.com/3d-printing/elegoo-centauri-2-combo-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T14:05:33+00:00",
    "summary": "The Elegoo Centauri 2 Combo is an excellent four-color printer, but is it worth the savings without an enclosure?"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/toms-hardware-innovation-awards-2026-progress-amid-turmoil",
    "domain": "AI 算力 / 半导体",
    "title": "Tom’s Hardware Innovation Awards 2026: Progress amid turmoil",
    "url": "https://www.tomshardware.com/pc-components/toms-hardware-innovation-awards-2026-progress-amid-turmoil",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T14:02:24+00:00",
    "summary": "The continued industry advancements give us several new picks for our annual Tom's Hardware Innovation Awards: a set of products that set or expand the standard for others."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/lg-enters-chip-packaging-arena-with-laser-direct-imaging-machine-as-tsmcs-cowos-remains-constrained-maskless-machine-is-designed-to-pattern-fine-interconnects-trading-resolution-for-higher-throughput",
    "domain": "AI 算力 / 半导体",
    "title": "LG enters chip packaging arena with Laser Direct Imaging machine, as TSMC's CoWoS remains constrained — maskless machine is designed to pattern fine interconnects, trading resolution for higher throug",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/lg-enters-chip-packaging-arena-with-laser-direct-imaging-machine-as-tsmcs-cowos-remains-constrained-maskless-machine-is-designed-to-pattern-fine-interconnects-trading-resolution-for-higher-throughput",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T13:35:14+00:00",
    "summary": "LG rolls-out laser direct imaging lithography machine for chip packaging and high-density PCBs."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/unlock-toms-hardware-premiums-hot-chips-2026-coverage-for-free-sign-up-for-an-account-to-read-technical-breakdowns-from-the-show",
    "domain": "AI 算力 / 半导体",
    "title": "Unlock Tom's Hardware Premium's Hot Chips 2026 coverage for free — sign up for an account to read technical breakdowns from the show",
    "url": "https://www.tomshardware.com/tech-industry/unlock-toms-hardware-premiums-hot-chips-2026-coverage-for-free-sign-up-for-an-account-to-read-technical-breakdowns-from-the-show",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T13:00:00+00:00",
    "summary": "For a limited time, you’ll be able to read all of our latest reports from Hot Chips 2026 with a Tom’s Hardware account, no payment required."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/lg-display-introduces-new-oled-deposition-technique-that-uses-lithography-instead-of-metal-masks-flipp-photolithography-delivers-1-6x-brightness-and-2-4x-longer-lifespan",
    "domain": "AI 算力 / 半导体",
    "title": "LG Display introduces new OLED deposition technique that uses lithography instead of metal masks — \"FLiPP\" photolithography delivers 1.6x brightness and 2.4x longer lifespan",
    "url": "https://www.tomshardware.com/monitors/lg-display-introduces-new-oled-deposition-technique-that-uses-lithography-instead-of-metal-masks-flipp-photolithography-delivers-1-6x-brightness-and-2-4x-longer-lifespan",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T12:40:00+00:00",
    "summary": "OLED displays have long been manufacturer using a metal mask for deposition that wastes material, is expensive, and can sag under its own weight. LG Display's FLiPP solves this by using photolithograp"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/supermicro-fires-several-employees-following-investigation-into-usd2-5-billion-china-ai-chip-smuggling-claims-that-senior-management-had-no-knowledge-of-illicit-transactions",
    "domain": "AI 算力 / 半导体",
    "title": "Supermicro fires several employees following investigation into $2.5 billion China AI chip smuggling — claims that senior management had no knowledge of illicit transactions",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/supermicro-fires-several-employees-following-investigation-into-usd2-5-billion-china-ai-chip-smuggling-claims-that-senior-management-had-no-knowledge-of-illicit-transactions",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T12:20:54+00:00",
    "summary": "An independent investigation on Supermicro clears senior management from any wrong-doing and also says that its financial statements were still reliable, despite the alleged diversion of its restricte"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/applications/cpu-z-gets-biggest-update-since-2001-with-v3-100-health-checks-built-in-stress-testing-and-xoc-effective-clock-tracking",
    "domain": "AI 算力 / 半导体",
    "title": "CPU-Z gets biggest update since 2001 with V3 — 100+ health checks, built-in stress testing, and XOC effective clock tracking",
    "url": "https://www.tomshardware.com/software/applications/cpu-z-gets-biggest-update-since-2001-with-v3-100-health-checks-built-in-stress-testing-and-xoc-effective-clock-tracking",
    "source": "Aaron Klotz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T12:20:00+00:00",
    "summary": "CPU-Z V3 introduces an overhauled validation system with over 100 detection points, and a new advanced validation feature that will check PC health with a stress test."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/micron-commits-usd10-billion-to-new-us-based-research-labs-boise-hub-to-target-post-dram-and-nand-technologies-and-packaging",
    "domain": "AI 算力 / 半导体",
    "title": "Micron commits $10 billion to new US-based Research Labs — Boise hub to target post-DRAM and NAND technologies and packaging",
    "url": "https://www.tomshardware.com/tech-industry/micron-commits-usd10-billion-to-new-us-based-research-labs-boise-hub-to-target-post-dram-and-nand-technologies-and-packaging",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T12:00:00+00:00",
    "summary": "Micron's Research Labs to bring together the company's own research with research by customers, partners, universities, startups, and government organizations to develop pre-competitive IP for next-ge"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/china-approves-first-nvidia-h200-deliveries-to-bytedance-and-tencent-under-case-by-case-import-licenses",
    "domain": "AI 算力 / 半导体",
    "title": "H200 AI GPUs finally reach China under case-by-case import licenses, but it's already too late for Nvidia — homemade chips corner the China market as country seeks semiconductor independence",
    "url": "https://www.tomshardware.com/pc-components/gpus/china-approves-first-nvidia-h200-deliveries-to-bytedance-and-tencent-under-case-by-case-import-licenses",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T11:40:00+00:00",
    "summary": "Most of each company's U.S.-licensed allowance, understood to be up to 100,000 units apiece, must stay outside the mainland."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/nvidia-denies-report-it-will-ship-groq-based-lpus-to-china-by-year-end",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia denies report it will ship Groq-based LPUs to China by year-end — says there is 'no China-specific LPU product in our roadmap'",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/nvidia-denies-report-it-will-ship-groq-based-lpus-to-china-by-year-end",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T11:39:39+00:00",
    "summary": "Nvidia has rejected a report published by The Information that it plans to begin small-batch shipments of an LPU tailored for Chinese customers by the end of 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/sandisks-new-nas-ssd-lets-you-fill-the-drive-every-day-for-five-years-7-68tb-m-2-flaunts-eye-popping-14-000-tbw-rating",
    "domain": "AI 算力 / 半导体",
    "title": "Sandisk's new $2,200 NAS SSD lets you fill the drive every day for five years — 7.68TB M.2 flaunts eye-popping 14,000 TBW rating",
    "url": "https://www.tomshardware.com/pc-components/ssds/sandisks-new-nas-ssd-lets-you-fill-the-drive-every-day-for-five-years-7-68tb-m-2-flaunts-eye-popping-14-000-tbw-rating",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T11:20:00+00:00",
    "summary": "Sandisk has announced the NAS 600 SATA and NAS 800 NVMe SSD lineups that target NAS environments."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/slovakia-discovers-russian-backdoors-in-279-new-traffic-cameras-national-security-service-deactivates-offending-units",
    "domain": "AI 算力 / 半导体",
    "title": "Slovakia discovers Russian backdoors in 279 new traffic cameras — SMS-triggered shell access and passwordless live feeds found in EU-funded rollout",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/slovakia-discovers-russian-backdoors-in-279-new-traffic-cameras-national-security-service-deactivates-offending-units",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T11:00:00+00:00",
    "summary": "Slovakia sought to modernize its traffic control systems by acquiring a batch of 279 new speed cameras, but they have Russian backdoors and multiple other security issues."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/enterprise-ssds-now-cost-18-times-more-than-hard-drives-per-terabyte",
    "domain": "AI 算力 / 半导体",
    "title": "Enterprise SSDs cost 18.6 times more than HDDs as 30TB drives hit $22,600 — hard drive supply is sold out through 2027",
    "url": "https://www.tomshardware.com/pc-components/ssds/enterprise-ssds-now-cost-18-times-more-than-hard-drives-per-terabyte",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T10:30:00+00:00",
    "summary": "A 30TB TLC enterprise SSD now costs $22,600, 6.5 times higher the $3,460 it fetched around this time last year."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/save-usd900-on-this-2-in-1-asus-rog-touchscreen-gaming-laptop-with-64gb-ram-the-14-inch-flow-z13-machine-ships-with-a-16-core-amd-strix-halo-cpu-and-a-1tb-ssd-perfect-for-games-and-ai",
    "domain": "AI 算力 / 半导体",
    "title": "Save $900 on this 2-in-1 Asus ROG touchscreen gaming laptop with 64GB RAM — the 14-inch Flow Z13 machine ships with a 16-core AMD Strix Halo CPU and a 1TB SSD, perfect for games and AI",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/save-usd900-on-this-2-in-1-asus-rog-touchscreen-gaming-laptop-with-64gb-ram-the-14-inch-flow-z13-machine-ships-with-a-16-core-amd-strix-halo-cpu-and-a-1tb-ssd-perfect-for-games-and-ai",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T10:23:49+00:00",
    "summary": "Save a huge $900 on this touch screen gaming laptop combo, the Asus ROG Flow Z13, now just $2,099.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/scalper-bots-now-outnumber-human-shoppers-10-to-1-on-one-retailers-ddr5-pages",
    "domain": "AI 算力 / 半导体",
    "title": "DDR5 scalper bots now outnumber shoppers 10 to 1 — automated scraping hits listings every 6.5 seconds as 32GB kits surge from $72 to $392, DataDome researcher says",
    "url": "https://www.tomshardware.com/pc-components/ddr5/scalper-bots-now-outnumber-human-shoppers-10-to-1-on-one-retailers-ddr5-pages",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T10:00:00+00:00",
    "summary": "Bad bots account for 91% of the traffic reaching one retailer's DDR5 memory product pages, roughly 10 automated requests for every legitimate visit."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/cooler-master-v-platinum-3000-workstation-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "Cooler Master V Platinum 3000 power supply review: Verified Platinum efficiency for workstations, with a stellar 12-year warranty",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/cooler-master-v-platinum-3000-workstation-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T16:44:34+00:00",
    "summary": "The Cooler Master V Platinum 3000 is a 3000W, 230V-only workstation supply built by CWT, carrying four native 12V-2x6 connectors, verified Platinum efficiency, and a twelve-year warranty."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/mechanical-keyboards/grab-keychrons-compact-k8-wireless-mechanical-keyboard-for-an-all-time-low-of-usd34-87-keys-gateron-red-switches-and-white-backlight-keeb-is-56-percent-off",
    "domain": "AI 算力 / 半导体",
    "title": "Grab Keychron's compact K8 wireless mechanical keyboard for an all-time low of $34 — 87-keys, Gateron Red switches, and white backlight keeb is 56% off",
    "url": "https://www.tomshardware.com/peripherals/mechanical-keyboards/grab-keychrons-compact-k8-wireless-mechanical-keyboard-for-an-all-time-low-of-usd34-87-keys-gateron-red-switches-and-white-backlight-keeb-is-56-percent-off",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T15:40:54+00:00",
    "summary": "If you need a solid compact wireless gaming or productivy keyboard and you don't have a lot to spend, Keychron's K8 87-key option is down to its lowest price of just $34.99 (or $5 less if you're a new"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/michigan-township-combats-nuclear-weapons-data-center-by-passing-ban-on-new-electrical-infrastructure-220-000-square-foot-hyperscale-project-is-backed-by-university-of-michigan-and-the-los-alamos-national-laboratory",
    "domain": "AI 算力 / 半导体",
    "title": "Michigan township combats nuclear weapons data center by passing ban on new electrical infrastructure — 220,000-square-foot hyperscale project is backed by University of Michigan and the Los Alamos Na",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/michigan-township-combats-nuclear-weapons-data-center-by-passing-ban-on-new-electrical-infrastructure-220-000-square-foot-hyperscale-project-is-backed-by-university-of-michigan-and-the-los-alamos-national-laboratory",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T15:37:29+00:00",
    "summary": "Ypsilanti Township is blocking a University of Michigan data center designed for researching nuclear weapons by temporarily stopping the electrical substation it needs to operate. It also put a one-ye"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/cxmt-planned-to-use-stolen-samsung-ip-to-develop-its-dram-court-hears-former-samsung-engineer-who-jumped-to-chinese-memory-maker-now-behind-bars",
    "domain": "AI 算力 / 半导体",
    "title": "CXMT planned to use stolen Samsung IP to develop its DRAM, court hears — former Samsung engineer who jumped to Chinese memory maker now behind bars",
    "url": "https://www.tomshardware.com/pc-components/dram/cxmt-planned-to-use-stolen-samsung-ip-to-develop-its-dram-court-hears-former-samsung-engineer-who-jumped-to-chinese-memory-maker-now-behind-bars",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T15:37:14+00:00",
    "summary": "Former Samsung engineers stole process recipe of the company's 18nm-class DRAM node to sell it to CXMT, according to a new report from Korea."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/dell-xps-13-2026-review",
    "domain": "AI 算力 / 半导体",
    "title": "Dell XPS 13 (2026) review: the new bar for mainstream Windows laptop excellence",
    "url": "https://www.tomshardware.com/laptops/dell-xps-13-2026-review",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T14:07:31+00:00",
    "summary": "The return of the XPS 13 is a triumph of (somewhat) affordable premium portable computing. It’s no powerhouse in terms of performance, but it gets more than enough right to recommend for Windows users"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/catastrophic-gta-vi-leak-is-a-full-working-build-notorious-hacker-cyberleek-taunts-rockstar-games-by-spraying-the-word-leek-onto-a-wall-in-game-with-bullets",
    "domain": "AI 算力 / 半导体",
    "title": "Catastrophic GTA VI leak is a full working build — notorious hacker CyberLeek taunts Rockstar Games by spraying the word 'leek' onto a wall in-game with bullets",
    "url": "https://www.tomshardware.com/video-games/catastrophic-gta-vi-leak-is-a-full-working-build-notorious-hacker-cyberleek-taunts-rockstar-games-by-spraying-the-word-leek-onto-a-wall-in-game-with-bullets",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T13:55:32+00:00",
    "summary": "Cyberleek has leaked another in-game footage of GTA VI, with some social media users claiming that it an actual build of the title. This is the second leak coming from the hacker, who claimed that the"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/synopsys-validates-a-pcie-6-phy-inside-a-face-to-face-3d-stack",
    "domain": "AI 算力 / 半导体",
    "title": "Synopsys validates a PCIe 6.0 PHY inside a face-to-face 3D stack at 64 GT/s — says it got there by pulling apart an existing 2D test chip",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/synopsys-validates-a-pcie-6-phy-inside-a-face-to-face-3d-stack",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T13:32:00+00:00",
    "summary": "Synopsys has published silicon results for what it calls the first 3D PCIe 6.0 test chip, a 5nm PHY built into a face-to-face stacked package."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/virginia-county-with-250-data-centers-begins-to-rein-in-building-loudouns-more-than-250-data-centers-made-it-one-of-the-richest-counties-in-the-us-but-residents-are-pushing-back",
    "domain": "AI 算力 / 半导体",
    "title": "Virginia county with 250 data centers begins to rein in building — Loudoun’s more than 250 data centers made it one of the richest counties in the US, but residents are pushing back",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/virginia-county-with-250-data-centers-begins-to-rein-in-building-loudouns-more-than-250-data-centers-made-it-one-of-the-richest-counties-in-the-us-but-residents-are-pushing-back",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T13:19:34+00:00",
    "summary": "Loudoun County recently changed its zoning policy which treated data centers as office parks. These projects now have to go through an approval process from the people and the local government, a sign"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/sk-hynix-reaches-tentative-agreement-with-disgruntled-workers-usd1-79-billion-potential-profit-pool-could-see-staff-get-usd50-000-each",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix will pay staff $50,000 apiece according to a tentative agreement with disgruntled workers — $1.79 billion potential profit pool will be split between cash and stock grants",
    "url": "https://www.tomshardware.com/pc-components/dram/sk-hynix-reaches-tentative-agreement-with-disgruntled-workers-usd1-79-billion-potential-profit-pool-could-see-staff-get-usd50-000-each",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T13:15:05+00:00",
    "summary": "SK hynix removes 10% operating profit cap for employee profit-sharing program; union agrees to get bonuses in cash and stock."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/seasonic-introduces-the-worlds-first-80-plus-ruby-certified-psu-using-a-standard-atx-form-factor",
    "domain": "AI 算力 / 半导体",
    "title": "Seasonic unveils world's first 80 Plus Ruby ATX power supply — Prime Enterprise RX-1600 delivers 1600W with up to 95.4% efficiency",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/seasonic-introduces-the-worlds-first-80-plus-ruby-certified-psu-using-a-standard-atx-form-factor",
    "source": "Aaron Klotz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T12:00:00+00:00",
    "summary": "Seasonic has introduced the world's first 80 Plus Ruby certified 115V ATX PSU, the Prime RX-1600. The new unit features an efficiency rating of up to 95% at 20% to 50% load."
  },
  {
    "id": "hn:49322519",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discloses $21B stake in SpaceX at end of second quarter",
    "url": "https://www.cnbc.com/2026/08/14/nvidia-discloses-21-billion-stake-in-spacex-at-end-of-second-quarter.html",
    "source": "johnbarron",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-08-16T18:40:54+00:00",
    "summary": ""
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
    "id": "rss:https://www.eetimes.com/andes-condor-closure-came-amid-broader-cost-cutting-effort/",
    "domain": "AI 算力 / 半导体",
    "title": "Andes Condor Closure Came Amid Broader Cost-Cutting Effort",
    "url": "https://www.eetimes.com/andes-condor-closure-came-amid-broader-cost-cutting-effort/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T22:00:00+00:00",
    "summary": "Andes Technology’s decision to close Condor was part of a broader 10-20% operational cost-cutting exercise, with Condor probably considered too expensive a bet. The post Andes Condor Closure Came Amid"
  },
  {
    "id": "rss:https://www.eetimes.com/ibm-makes-quantum-cryogenics-modular-but-scaling-problems-remain/",
    "domain": "AI 算力 / 半导体",
    "title": "IBM Makes Quantum Cryogenics Modular, but Scaling Problems Remain",
    "url": "https://www.eetimes.com/ibm-makes-quantum-cryogenics-modular-but-scaling-problems-remain/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T13:55:51+00:00",
    "summary": "IBM’s new cryogenic architecture tackles one obstacle to fault-tolerant quantum computing, while exposing wiring, control, interconnect, and reliability challenges. The post IBM Makes Quantum Cryogeni"
  },
  {
    "id": "rss:https://www.eetimes.com/running-local-llms-on-the-arduino-uno-q-board-a-practical-guide/",
    "domain": "AI 算力 / 半导体",
    "title": "Running Local LLMs on the Arduino® UNO™ Q Board: a Practical Guide",
    "url": "https://www.eetimes.com/running-local-llms-on-the-arduino-uno-q-board-a-practical-guide/",
    "source": "Arduino Team",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T13:00:00+00:00",
    "summary": "Learn how to run local LLMs on Arduino UNO Q — from model selection and quantization to memory constraints and real-world edge AI use cases. The post Running Local LLMs on the Arduino® UNO™ Q Board: a"
  },
  {
    "id": "rss:https://www.eetimes.com/when-interoperability-becomes-infrastructure/",
    "domain": "AI 算力 / 半导体",
    "title": "When Interoperability Becomes Infrastructure",
    "url": "https://www.eetimes.com/when-interoperability-becomes-infrastructure/",
    "source": "Peter Hunt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T07:43:30+00:00",
    "summary": "As Matter matures, manufacturers face a new challenge: maintaining visibility into connected products after deployment. The post When Interoperability Becomes Infrastructure appeared first on EE Times"
  },
  {
    "id": "rss:https://www.eetimes.com/marvell-targets-ai-bottlenecks-with-memory-disaggregation-portfolio/",
    "domain": "AI 算力 / 半导体",
    "title": "Marvell Targets AI Bottlenecks with Memory-Disaggregation Portfolio",
    "url": "https://www.eetimes.com/marvell-targets-ai-bottlenecks-with-memory-disaggregation-portfolio/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T14:39:27+00:00",
    "summary": "Marvell attacks AI’s memory choke point with SSD, CXL, and photonic fabrics to push data nearer compute. The post Marvell Targets AI Bottlenecks with Memory-Disaggregation Portfolio appeared first on "
  },
  {
    "id": "rss:https://www.eetimes.com/why-standardized-interfaces-are-critical-to-accelerating-humanoid-development/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Standardized Interfaces Are Critical to Accelerating Humanoid Development",
    "url": "https://www.eetimes.com/why-standardized-interfaces-are-critical-to-accelerating-humanoid-development/",
    "source": "Edo Cohen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T08:15:00+00:00",
    "summary": "Humanoids won’t scale on AI hype alone; standardized MIPI interfaces can cut power, wiring, and cost. The post Why Standardized Interfaces Are Critical to Accelerating Humanoid Development appeared fi"
  },
  {
    "id": "hn:49325115",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Uses Old Fabs to Make New Chips [video]",
    "url": "https://www.youtube.com/watch?v=cDxVYQrxeiQ",
    "source": "eig",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-08-17T00:07:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:49289112",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.7 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 968,
    "published_at": "2026-08-13T17:23:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49184755",
    "domain": "大厂 AI 动态",
    "title": "Changes at Google DeepMind: Demis Hassabis from CEO to Chair, Jeff Dean departs",
    "url": "https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/",
    "source": "colesantiago",
    "platform": "hackernews",
    "points": 867,
    "published_at": "2026-08-05T16:05:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49111237",
    "domain": "大厂 AI 动态",
    "title": "Gemini Robotics 2 brings whole body intelligence to robots",
    "url": "https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/",
    "source": "ai2027",
    "platform": "hackernews",
    "points": 620,
    "published_at": "2026-07-30T15:15:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49220126",
    "domain": "大厂 AI 动态",
    "title": "DeepMind's WeatherNext model achieves breakthrough forecasting cyclones",
    "url": "https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/",
    "source": "bhavansig",
    "platform": "hackernews",
    "points": 449,
    "published_at": "2026-08-08T09:18:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49096188",
    "domain": "大厂 AI 动态",
    "title": "Document-borne AI worms can self-propagate through Copilot for Word",
    "url": "https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/",
    "source": "Canopy9560",
    "platform": "hackernews",
    "points": 384,
    "published_at": "2026-07-29T11:44:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49267928",
    "domain": "大厂 AI 动态",
    "title": "llama.cpp",
    "url": "https://llama.app",
    "source": "kristianpaul",
    "platform": "hackernews",
    "points": 364,
    "published_at": "2026-08-12T04:51:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49184757",
    "domain": "大厂 AI 动态",
    "title": "Demis Hassabis is moving from CEO to Chairman at Google DeepMind",
    "url": "https://www.axios.com/2026/08/05/google-deepmind-demis-hassabis-ai",
    "source": "ot",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-08-05T16:05:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49259339",
    "domain": "大厂 AI 动态",
    "title": "Apple Silicon and macOS VMs: Faster LLM Inference with llama.cpp",
    "url": "https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md",
    "source": "frabonacci",
    "platform": "hackernews",
    "points": 307,
    "published_at": "2026-08-11T14:50:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49383326",
    "domain": "大厂 AI 动态",
    "title": "Codex on AWS bedrock bug causing 10x charges",
    "url": "https://github.com/openai/codex/issues/37674",
    "source": "TheP1000",
    "platform": "hackernews",
    "points": 146,
    "published_at": "2026-08-21T03:17:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49256057",
    "domain": "大厂 AI 动态",
    "title": "What I learned by putting GitHub Copilot behind a MitM proxy",
    "url": "https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm",
    "source": "j0selit0",
    "platform": "hackernews",
    "points": 200,
    "published_at": "2026-08-11T10:40:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49067285",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://www.lesswrong.com/posts/iKm2FhpWkuuBojm82/why-i-left-google-deepmind",
    "source": "eatitraw",
    "platform": "hackernews",
    "points": 200,
    "published_at": "2026-07-27T09:56:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49198583",
    "domain": "大厂 AI 动态",
    "title": "Show HN: The Channels SDK – Bring Any Agent to Any Channel (Slack, MS Teams)",
    "url": "https://github.com/CopilotKit/channels-sdk",
    "source": "davidmckayv",
    "platform": "hackernews",
    "points": 121,
    "published_at": "2026-08-06T16:05:51+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/983500/hoverair-versa-halted-us-fcc-drone-ban-indiegogo",
    "domain": "大厂 AI 动态",
    "title": "HoverAir’s transforming modular drone has already been halted in the US",
    "url": "https://www.theverge.com/tech/983500/hoverair-versa-halted-us-fcc-drone-ban-indiegogo",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T22:14:11+00:00",
    "summary": "I am so sorry, fellow US gadget fans: the FCC's drone ban appears to have struck again. The HoverAir Versa - a baby steadycam with snap-on propeller wings that transform it into a drone - has already "
  },
  {
    "id": "rss:https://www.theverge.com/tech/983531/tiktok-settle-doj-lawsuit-coppa",
    "domain": "大厂 AI 动态",
    "title": "TikTok will pay $400 million to settle DOJ child privacy lawsuit",
    "url": "https://www.theverge.com/tech/983531/tiktok-settle-doj-lawsuit-coppa",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T22:13:34+00:00",
    "summary": "The US Department of Justice announced on Friday that TikTok will pay $400 million to settle a lawsuit filed in 2024 over allegedly violating the Children's Online Privacy Protection Act (COPPA). In t"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/983502/linkedin-ai-slop-button-one-million-people-message",
    "domain": "大厂 AI 动态",
    "title": "Over 1 million people have clicked LinkedIn’s AI slop button",
    "url": "https://www.theverge.com/ai-artificial-intelligence/983502/linkedin-ai-slop-button-one-million-people-message",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T21:25:50+00:00",
    "summary": "LinkedIn actually announced a \"Seems like AI slop\" button on July 30th, and the company says that a lot of people have already used it. According to a Thursday post from chief product officer Hari Sri"
  },
  {
    "id": "rss:https://www.theverge.com/tech/983451/apple-layoffs-vision-pro-siri",
    "domain": "大厂 AI 动态",
    "title": "Apple is laying off staffers working on the Vision Pro and Siri",
    "url": "https://www.theverge.com/tech/983451/apple-layoffs-vision-pro-siri",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T19:44:55+00:00",
    "summary": "Apple is laying off staff on the Siri and the Vision Pro teams, according to Bloomberg. The cuts include \"largely shutting down\" a Vision Pro gaming team and \"reducing the size\" of the team that makes"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/982513/best-buy-gift-card-in-store-deal",
    "domain": "大厂 AI 动态",
    "title": "$100 Best Buy gift cards will be $60 at stores Saturday",
    "url": "https://www.theverge.com/gadgets/982513/best-buy-gift-card-in-store-deal",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T18:00:00+00:00",
    "summary": "The best gift card deal we’ve spotted this year is happening Saturday, August 22nd, at Best Buy stores for one day only. In celebration of the retailer’s 60th anniversary, you can purchase a $100 Best"
  },
  {
    "id": "rss:https://www.theverge.com/tech/983336/walmart-apple-google-pay-launch",
    "domain": "大厂 AI 动态",
    "title": "Walmart is finally adding Apple Pay and Google Pay",
    "url": "https://www.theverge.com/tech/983336/walmart-apple-google-pay-launch",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T17:01:59+00:00",
    "summary": "Walmart will soon allow you to pay for your items with Google Pay or Apple Pay. In an announcement on Friday, Walmart says it's going to bring tap-to-pay capabilities to \"select\" Walmart and Sam's Clu"
  },
  {
    "id": "rss:https://www.theverge.com/games/983323/grand-theft-auto-vi-gta-leaks-microsoft-discord-subpoenaed",
    "domain": "大厂 AI 动态",
    "title": "Microsoft and Discord subpoenaed over GTA VI gameplay leaks",
    "url": "https://www.theverge.com/games/983323/grand-theft-auto-vi-gta-leaks-microsoft-discord-subpoenaed",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T16:52:56+00:00",
    "summary": "Following several apparent video leaks of Grand Theft Auto VI, Take-Two Interactive has subpoenaed Microsoft and Discord over content that \"infringes copyrights\" held for the game, Kotaku reports. In "
  },
  {
    "id": "rss:https://www.theverge.com/podcast/983288/pixel-11-gets-in-on-the-digicam-trend",
    "domain": "大厂 AI 动态",
    "title": "Pixel 11 gets in on the digicam trend",
    "url": "https://www.theverge.com/podcast/983288/pixel-11-gets-in-on-the-digicam-trend",
    "source": "Jacob Kastrenakes",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T16:27:05+00:00",
    "summary": "I recently looked back at a photo I'd taken on a smartphone in 2014, and I was struck by just how good it looked. The details were soft, the shadows were dark. It was the kind of photo I felt like I h"
  },
  {
    "id": "rss:https://www.theverge.com/science/983241/food-recalls-bigger-out-of-control",
    "domain": "大厂 AI 动态",
    "title": "Why does it seem like food recalls are out of control this year?",
    "url": "https://www.theverge.com/science/983241/food-recalls-bigger-out-of-control",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T14:45:00+00:00",
    "summary": "Just weeks after Taylor Farms issued a recall of its iceberg lettuce amid a massive cyclospora outbreak, the Food and Drug Administration recalled more than one million eggs that may be contaminated w"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/983171/google-pixel-10a-steelseries-gaming-headset-soldering-4k-bluray-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Google’s Pixel 10A is a great deal at 15 percent off",
    "url": "https://www.theverge.com/gadgets/983171/google-pixel-10a-steelseries-gaming-headset-soldering-4k-bluray-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T14:35:22+00:00",
    "summary": "This week, all of Google’s Pixel 11 phones launched, including the $899 Pixel 11, the $1,099 Pixel 11 Pro (with the same processor and starting 12GB RAM as the standard model, but with better cameras)"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/michael-polansky-is-training-an-ai-model-on-skin-thats-still-alive/",
    "domain": "大厂 AI 动态",
    "title": "Michael Polansky is training an AI model on skin that’s still alive",
    "url": "https://techcrunch.com/2026/08/21/michael-polansky-is-training-an-ai-model-on-skin-thats-still-alive/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T01:31:04+00:00",
    "summary": "Michael Polansky — better known publicly as Lady Gaga's partner and a former top deputy to Sean Parker — has quietly spent years building an AI-driven startup that keeps living human skin tissue alive"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/japanese-space-tech-startup-letara-expands-beyond-satellite-thrusters-with-16m/",
    "domain": "大厂 AI 动态",
    "title": "Japanese space tech startup Letara expands beyond satellite thrusters with $16M",
    "url": "https://techcrunch.com/2026/08/21/japanese-space-tech-startup-letara-expands-beyond-satellite-thrusters-with-16m/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T01:03:06+00:00",
    "summary": "Japanese space startup Letara is betting its hybrid rocket technology can move beyond small satellite thrusters into a broader market for space, defense and security, after raising ¥2.6 billion ($16 m"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/anthropics-opus-4-6-is-a-smut-machine/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s Opus 4.6 is a smut-machine",
    "url": "https://techcrunch.com/2026/08/21/anthropics-opus-4-6-is-a-smut-machine/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T23:07:25+00:00",
    "summary": "Anthropic forbids its Claude models from generating sexually explicit content. But a series of tests conducted by TechCrunch found that it didn't take much to get past the restriction."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/nvidia-partners-with-data-center-developer-cloverleaf/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia partners with data center developer Cloverleaf",
    "url": "https://techcrunch.com/2026/08/21/nvidia-partners-with-data-center-developer-cloverleaf/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T22:37:38+00:00",
    "summary": "Nvidia continues to pour money into data center development — just as AI data centers bring lots of money into Nvidia."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/how-ai-accounting-startup-rillet-raised-100m-and-became-a-unicorn-in-48-hours/",
    "domain": "大厂 AI 动态",
    "title": "How AI accounting startup Rillet raised $100M and became a unicorn in 48 hours",
    "url": "https://techcrunch.com/2026/08/21/how-ai-accounting-startup-rillet-raised-100m-and-became-a-unicorn-in-48-hours/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T22:10:01+00:00",
    "summary": "Rillet CEO Nicolas Kopp shared growth numbers at a board meeting and set off a fundraising frenzy from Iconiq, Sequoia and others. Without even trying."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/apple-is-reportedly-cutting-hundreds-of-jobs-from-siri-vision-pro-teams/",
    "domain": "大厂 AI 动态",
    "title": "Apple is reportedly cutting hundreds of jobs from Siri, Vision Pro teams",
    "url": "https://techcrunch.com/2026/08/21/apple-is-reportedly-cutting-hundreds-of-jobs-from-siri-vision-pro-teams/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T20:58:07+00:00",
    "summary": "Apple has admitted that some roles are being impacted as it shifts its focus away from certain initiatives."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/tiktok-reaches-400m-settlement-over-childrens-privacy-lawsuit/",
    "domain": "大厂 AI 动态",
    "title": "TikTok reaches $400M settlement over children’s privacy lawsuit",
    "url": "https://techcrunch.com/2026/08/21/tiktok-reaches-400m-settlement-over-childrens-privacy-lawsuit/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T20:25:21+00:00",
    "summary": "Two years after the U.S. Department of Justice alleged that TikTok violated the Children’s Online Privacy Protection Act, it has reached a $400 million settlement."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/the-225-pebble-time-2-is-a-refreshingly-fun-smartwatch/",
    "domain": "大厂 AI 动态",
    "title": "The $225 Pebble Time 2 is a refreshingly fun smartwatch",
    "url": "https://techcrunch.com/2026/08/21/the-225-pebble-time-2-is-a-refreshingly-fun-smartwatch/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T19:57:46+00:00",
    "summary": "The $225 Pebble Time 2 pairs quirky watch faces and apps with physical buttons, an e-paper display, weeks of battery life, and a playful hacker spirit."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/last-chance-save-up-to-300-on-your-techcrunch-disrupt-2026-ticket-today/",
    "domain": "大厂 AI 动态",
    "title": "Last chance: Save up to $300 on your TechCrunch Disrupt 2026 ticket today",
    "url": "https://techcrunch.com/2026/08/21/last-chance-save-up-to-300-on-your-techcrunch-disrupt-2026-ticket-today/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T19:16:15+00:00",
    "summary": "If you’ve been circling around Disrupt, then now’s the best time to lock in your pass and start getting ready to join the rest of the startup community gathering in San Francisco from October 13-15 at"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/teslas-solar-roof-is-dead-heres-what-went-wrong/",
    "domain": "大厂 AI 动态",
    "title": "Tesla’s solar roof is dead — here’s what went wrong",
    "url": "https://techcrunch.com/2026/08/21/teslas-solar-roof-is-dead-heres-what-went-wrong/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T18:09:53+00:00",
    "summary": "Tesla's solar roof was an experiment that never really caught on for the company. But does that mean the concept of roof-integrated solar is dead?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/waymo-hands-over-documents-in-nhtsas-child-collision-probe/",
    "domain": "大厂 AI 动态",
    "title": "Waymo hands over documents in NHTSA’s child collision probe",
    "url": "https://techcrunch.com/2026/08/21/waymo-hands-over-documents-in-nhtsas-child-collision-probe/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T17:49:58+00:00",
    "summary": "The responses to NHTSA's questions so far are redacted entirely, citing \"confidential business information.\""
  },
  {
    "id": "rss:https://techcrunch.com/video/why-is-the-doj-investigating-andreessen-horowitzs-board-seats/",
    "domain": "大厂 AI 动态",
    "title": "Why is the DOJ investigating Andreessen Horowitz’s board seats?",
    "url": "https://techcrunch.com/video/why-is-the-doj-investigating-andreessen-horowitzs-board-seats/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T16:53:39+00:00",
    "summary": "Andreessen Horowitz has two partners sitting on the boards of companies that now&#160;compete with each other: Ben Horowitz at Databricks and Martin Casado at&#160;Fivetran. Nothing too scandalous on "
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/us-government-lab-is-probing-chinese-lidar-for-security-vulnerabilities/",
    "domain": "大厂 AI 动态",
    "title": "US government lab is probing Chinese lidar for security vulnerabilities",
    "url": "https://techcrunch.com/2026/08/21/us-government-lab-is-probing-chinese-lidar-for-security-vulnerabilities/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T16:01:54+00:00",
    "summary": "The security review is being performed by the Idaho National Laboratory, and the research is being funded by a company -- or a group of companies -- in the electric and autonomous vehicle industries."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/oura-faces-lawsuit-accusing-it-of-misleading-consumers-about-sleep-tracking-accuracy/",
    "domain": "大厂 AI 动态",
    "title": "Oura faces lawsuit accusing it of misleading consumers about sleep-tracking accuracy",
    "url": "https://techcrunch.com/2026/08/21/oura-faces-lawsuit-accusing-it-of-misleading-consumers-about-sleep-tracking-accuracy/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T14:39:24+00:00",
    "summary": "The lawsuit alleges that Oura rings are unable to measure any of the physiological signals needed to assess sleep quality or determine sleep stages."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/walmart-to-finally-start-accepting-apple-pay-and-google-pay/",
    "domain": "大厂 AI 动态",
    "title": "Walmart to finally start accepting Apple Pay and Google Pay",
    "url": "https://techcrunch.com/2026/08/21/walmart-to-finally-start-accepting-apple-pay-and-google-pay/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T14:30:23+00:00",
    "summary": "Are pigs flying? Walmart has finally caved on its refusal to support Apple Pay and Google Pay."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/starcloud-raises-200-million-for-orbital-data-centers-as-launch-options-dry-up/",
    "domain": "大厂 AI 动态",
    "title": "Starcloud raises $250 million for orbital data centers as launch options dry up",
    "url": "https://techcrunch.com/2026/08/21/starcloud-raises-200-million-for-orbital-data-centers-as-launch-options-dry-up/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T14:00:00+00:00",
    "summary": "There's about to be a big fight to secure access to space."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/tesla-recalls-3-million-cars-as-part-of-china-wide-push-to-stop-hidden-door-handles/",
    "domain": "大厂 AI 动态",
    "title": "Tesla recalls 3 million cars as part of China-wide push to stop hidden door handles",
    "url": "https://techcrunch.com/2026/08/21/tesla-recalls-3-million-cars-as-part-of-china-wide-push-to-stop-hidden-door-handles/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T13:48:26+00:00",
    "summary": "Tesla and eight other automakers will install warning labels that help occupants identify the often hard-to-find manual door releases."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/private-equity-firm-apollo-confirms-data-breach-amid-hacking-wave-targeting-financial-giants/",
    "domain": "大厂 AI 动态",
    "title": "Private equity firm Apollo confirms data breach amid hacking wave targeting financial giants",
    "url": "https://techcrunch.com/2026/08/21/private-equity-firm-apollo-confirms-data-breach-amid-hacking-wave-targeting-financial-giants/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T13:35:23+00:00",
    "summary": "The private equity giant confirms a breach, weeks after Google researchers said hackers were targeting financial companies."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/21/senator-asks-us-federal-watchdog-to-review-how-feds-use-hacking-tools/",
    "domain": "大厂 AI 动态",
    "title": "Senator asks US government watchdog to review how feds use hacking tools",
    "url": "https://techcrunch.com/2026/08/21/senator-asks-us-federal-watchdog-to-review-how-feds-use-hacking-tools/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T13:05:00+00:00",
    "summary": "Senator Ron Wyden sent a letter to the U.S. federal watchdog requesting a comprehensive review of how the FBI, DEA, ICE's HSI, and the Secret Service use hacking tools and spyware against Americans."
  },
  {
    "id": "rss:https://stratechery.com/2026/app-snore/",
    "domain": "大厂 AI 动态",
    "title": "2026.34: App Snore",
    "url": "https://stratechery.com/2026/app-snore/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of August 17, 2026, including Apple making compromises in the EU, Truth (Social) and reconciliation, and August fun with the Clippers and Lakers."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/trump-admin-calls-for-more-spaceports-to-handle-surge-in-launches/",
    "domain": "大厂 AI 动态",
    "title": "Trump's space transportation policy calls for new spaceport on federal land",
    "url": "https://arstechnica.com/space/2026/08/trump-admin-calls-for-more-spaceports-to-handle-surge-in-launches/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T23:32:17+00:00",
    "summary": "\"We probably need another site that's capable of heavy and super heavy launch capability.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/researchers-use-thunderquakes-to-study-structure-of-earths-surface/",
    "domain": "大厂 AI 动态",
    "title": "Thunder + fiber-optic cabling used for seismic imaging",
    "url": "https://arstechnica.com/science/2026/08/researchers-use-thunderquakes-to-study-structure-of-earths-surface/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T20:26:46+00:00",
    "summary": "Thunderstorms make seismic waves that can be used to find sub-surface features."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/class-action-accuses-brokers-of-hiding-zillow-listings-driving-up-nyc-rents/",
    "domain": "大厂 AI 动态",
    "title": "Hidden Zillow listings created fake supply shock, raising NYC rents, lawsuit says",
    "url": "https://arstechnica.com/tech-policy/2026/08/class-action-accuses-brokers-of-hiding-zillow-listings-driving-up-nyc-rents/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T20:10:50+00:00",
    "summary": "Renters say hidden Zillow listings make it harder to afford living in New York City."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/motorolas-grapheneos-phones-will-launch-in-2027-priced-higher-than-pixels/",
    "domain": "大厂 AI 动态",
    "title": "Motorola's GrapheneOS phones will launch in 2027 priced higher than Pixels",
    "url": "https://arstechnica.com/gadgets/2026/08/motorolas-grapheneos-phones-will-launch-in-2027-priced-higher-than-pixels/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T19:32:29+00:00",
    "summary": "The private Android-based OS will expand beyond Pixels next year."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/lawsuit-demands-logitech-hand-tariff-refunds-over-to-customers/",
    "domain": "大厂 AI 动态",
    "title": "Lawsuit demands Logitech hand tariff refunds over to customers",
    "url": "https://arstechnica.com/tech-policy/2026/08/lawsuit-demands-logitech-hand-tariff-refunds-over-to-customers/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T19:04:41+00:00",
    "summary": "Logitech increased prices by up to 25 percent last year."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/08/chinese-regulators-tell-tesla-to-fix-nearly-3-million-cars/",
    "domain": "大厂 AI 动态",
    "title": "Chinese regulators tell Tesla to fix nearly 3 million cars",
    "url": "https://arstechnica.com/cars/2026/08/chinese-regulators-tell-tesla-to-fix-nearly-3-million-cars/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T18:07:15+00:00",
    "summary": "Chinese safety regulators have cracked down on doors that don't open in a crash."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/explosive-russian-drone-boat-destroyed-near-european-offshore-gas-site/",
    "domain": "大厂 AI 动态",
    "title": "Fighter jets help destroy Russian drone boat near European offshore gas platform",
    "url": "https://arstechnica.com/gadgets/2026/08/explosive-russian-drone-boat-destroyed-near-european-offshore-gas-site/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T16:48:59+00:00",
    "summary": "Romania blew up drone boat to protect lives of several hundred rig workers."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/critics-ftc-limits-on-personalized-pricing-may-increase-costs-kill-discounts/",
    "domain": "大厂 AI 动态",
    "title": "Personalized pricing is “abhorrent,” but FTC limits may increase costs, critics say",
    "url": "https://arstechnica.com/tech-policy/2026/08/critics-ftc-limits-on-personalized-pricing-may-increase-costs-kill-discounts/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T16:38:25+00:00",
    "summary": "Some Americans fear the FTC may be thinking about personalized pricing all wrong."
  },
  {
    "id": "hn:49166182",
    "domain": "股票",
    "title": "Bending Spoons makes first post-IPO acquisition with $1.3B Airtable deal",
    "url": "https://live.euronext.com/en/financial-news/bending-spoons-makes-first-post-ipo-acquisition-13-billion-airtable-deal",
    "source": "riffraff",
    "platform": "hackernews",
    "points": 118,
    "published_at": "2026-08-04T09:27:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49335271",
    "domain": "股票",
    "title": "30-year Treasury yield tops 5.31%, the highest in 19 years",
    "url": "https://www.cnbc.com/2026/08/17/treasury-yields-federal-reserve-fomc-minutes.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-08-17T18:14:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49342823",
    "domain": "股票",
    "title": "OpenAI disbanded the team that assessed catastrophic model risks",
    "url": "https://thenextweb.com/news/openai-preparedness-team-disbanded-ipo-streamlining",
    "source": "nyku",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-08-18T08:06:58+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3780044",
    "domain": "股票",
    "title": "集中资源押注AI，苹果裁撤Siri与Vision Pro逾200个岗位",
    "url": "https://wallstreetcn.com/articles/3780044",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T03:03:33+00:00",
    "summary": "苹果公司裁减职位涉及约100个Vision Pro相关岗位及约100个Siri与软件工程岗位。Vision Pro方面，游戏团队近乎解散，沉浸式视频部门缩减，因高昂制作成本与有限用户规模难以为继。Siri方面，裁员源于技术架构全面切换，新版Siri将基于全新底层重建，带动人才结构重组。"
  },
  {
    "id": "wscn:3780048",
    "domain": "股票",
    "title": "一文读懂：市场焦点！下周的杰克逊霍尔大会，你该关注什么？",
    "url": "https://wallstreetcn.com/articles/3780048",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T02:32:47+00:00",
    "summary": "沃什将于美东时间8月28日在杰克逊霍尔首次发表主旨演讲，但尚未决定是谈宏观经济“大局观”，还是直接为9月至12月政策路径提供指引。这种不确定性意味着，市场对措辞变化的敏感度可能明显提高。会议期间预计约有5名美联储官员接受媒体采访，需重点关注这些官员的连续表态。高盛认为，杰克逊霍尔历来会放大外汇波动，但美元并无稳定的单边方向。"
  },
  {
    "id": "wscn:3780050",
    "domain": "股票",
    "title": "比亚迪派“大汉”补位",
    "url": "https://wallstreetcn.com/articles/3780050",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T02:20:39+00:00",
    "summary": "补销量，也要守住成交价。"
  },
  {
    "id": "wscn:3780049",
    "domain": "股票",
    "title": "大众要拿回“国民家轿”宝座",
    "url": "https://wallstreetcn.com/articles/3780049",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T02:16:06+00:00",
    "summary": "携手地平线发起大反攻。"
  },
  {
    "id": "wscn:3780047",
    "domain": "股票",
    "title": "黄金冲破200日均线，高盛交易台多头增持至六成，大客户押注白银三个月内涨至90美元",
    "url": "https://wallstreetcn.com/articles/3780047",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T02:09:25+00:00",
    "summary": "现货黄金自7月低点以来上涨约15%，突破200日均线并重回4600美元/盎司。高盛交易台多头仓位已升至六成，随着看涨期权需求激增，做市商动态对冲可能进一步强化“越涨越买”的正反馈，放大金价上行弹性。与此同时，美联储政策预期转鸽、美元承压，叠加央行购金和ETF需求改善，黄金上涨的基本面支撑持续增强。"
  },
  {
    "id": "wscn:3780034",
    "domain": "股票",
    "title": "从“AI股神”抄底的“带血筹码”，Citadel已卖掉80%！",
    "url": "https://wallstreetcn.com/articles/3780034",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T01:26:59+00:00",
    "summary": "城堡投资创始人表示，公司已将从对冲基金Situational Awareness接手的股票组合风险敞口削减逾80%。这批超40亿美元的仓位主要集中于AI和半导体板块，包括美光科技、闪迪等多头，以及英伟达、博通、AMD相关头寸。与此同时，旗舰多策略基金Wellington 7月回报率达5.94%，创2022年以来最佳单月表现。"
  },
  {
    "id": "wscn:3780046",
    "domain": "股票",
    "title": "环球时报社评：中国不会陪美国在伊朗问题上“胡闹”",
    "url": "https://wallstreetcn.com/articles/3780046",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T01:08:51+00:00",
    "summary": "美国所谓“要么站在我们这边，要么与我们为敌”的说法，某种意义上暴露出华盛顿“自己已经搞不定这个烂摊子”的战略窘迫。中方一贯反对单边霸凌和“长臂管辖”，不是因为中国是伊朗最大贸易伙伴并与伊朗保持长期友好关系，而是因为一旦接受美国这套逻辑，国际贸易就是由美国自行划设规则，所有商品流动都要经过美国拍板的荒唐局面。"
  },
  {
    "id": "wscn:3780041",
    "domain": "股票",
    "title": "贝森特没救成美债却点燃“美元贬值交易”！黄金创三个月新高，比特币单周暴涨超25%",
    "url": "https://wallstreetcn.com/articles/3780041",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-22T00:56:12+00:00",
    "summary": "继贝森特宣布扩大美国长债回购之后，美债收益率短暂下挫后重返高位，但却彻底点燃“货币贬值交易”——黄金创三月新高、比特币单周暴涨超25%。市场对美元公信力的担忧不断升温，但也有分析指出，货币创造是美联储的权利，认为本轮贬值交易能否持续存疑。"
  },
  {
    "id": "wscn:3779789",
    "domain": "股票",
    "title": "银行还只是红利资产吗？二季度金融数据正在给出不同答案",
    "url": "https://wallstreetcn.com/premium/articles/3779789?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T23:24:50+00:00",
    "summary": "2026年二季度，银行业出现了几个值得重视的边际变化。国家金融监督管理总局数据显示，商业银行净息差升至1.41%，为2021年四季度以来首次环比回升，国有大行利润增速同步转正；与此同时，人民银行公布的7月金融数据显示，人民币贷款出现单月负增长，银行经营逐步进入低扩表阶段。在负债成本下降、盈利预期趋稳、长端利率处于低位的环境下，银行板块的关注逻辑正在从单纯的高股息，逐渐延伸至ROE稳定和估值约束缓解"
  },
  {
    "id": "wscn:3780043",
    "domain": "股票",
    "title": "华尔街见闻早餐FM-Radio | 2026年8月22日",
    "url": "https://wallstreetcn.com/articles/3780043",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T23:20:28+00:00",
    "summary": "五分钟看懂全球市场，尽在财经早餐。"
  },
  {
    "id": "wscn:3779986",
    "domain": "股票",
    "title": "美股止跌反弹，道指涨近1%，数字货币再猛涨，黄金升破4600",
    "url": "https://wallstreetcn.com/articles/3779986",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T23:12:35+00:00",
    "summary": "本周整体道指跌0.85%，标普500指数跌1.43%，纳指跌2.05%。当日芯片股涨跌不一。银行、黄金股普涨，埃尔拉多黄金涨超7%，高盛、摩根士丹利涨超3%。10年期美债收益率小幅升2.99个基点。比特币延续强势涨6.7%，本周累涨逾24%、创2023年3月以来最大单周涨幅。现货黄金大涨2.2%。"
  },
  {
    "id": "wscn:3780042",
    "domain": "股票",
    "title": "报道：Anthropic招股书或把美国公众对AI的抵制情绪列为风险因素",
    "url": "https://wallstreetcn.com/articles/3780042",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T23:04:40+00:00",
    "summary": "估值或高达2万亿美元的Anthropic正筹备IPO，却面临一场棘手的民意逆风——盖洛普调查显示，70%的美国人反对在当地建设AI数据中心。中期选举之际，两党政客亦回应选民情绪，宾州数据中心限制法案落地。据媒体报道，对于算力即营收的AI公司而言，这场公众情绪反弹或将被列为IPO招股书核心风险。"
  },
  {
    "id": "wscn:3780040",
    "domain": "股票",
    "title": "英伟达拟斥资60亿美元获Poolside AI模型授权，另投10亿美元并吸纳百余名员工",
    "url": "https://wallstreetcn.com/articles/3780040",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T22:59:10+00:00",
    "summary": "据媒体报道，英伟达已同意向AI初创公司Poolside支付60亿美元的模型许可费，并将向其逾100名员工发出工作邀约。英伟达还以120亿美元估值（不含许可费）对Poolside追加10亿美元战略投资。"
  },
  {
    "id": "wscn:3780038",
    "domain": "股票",
    "title": "美债扩大回购宣布前，资产管理公司增持5年期和10年期期货多头",
    "url": "https://wallstreetcn.com/articles/3780038",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T22:10:20+00:00",
    "summary": "CFTC截至8月18日当周的数据显示，资产管理公司在5年期和10年期美债期货上的净多头头寸有所增加。杠杆基金等投机资金在长久期美债期货上的净头寸进一步转向空头。整体来看，在美国财政部宣布扩大回购之前，长期美债市场呈现长期资金偏多，投机资金偏空的仓位分化。"
  },
  {
    "id": "wscn:3780039",
    "domain": "股票",
    "title": "特朗普称对伊转向“经济战”不意味着美军事选项受限",
    "url": "https://wallstreetcn.com/articles/3780039",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T22:05:03+00:00",
    "summary": "特朗普称，美国对霍尔木兹海峡周边整个地区拥有完全的控制权，伊朗很希望达成协议，但他认为伊方尚未准备好达成“合适的协议”，美方正在观察冲突中“事态的发展”；。"
  },
  {
    "id": "wscn:3780037",
    "domain": "股票",
    "title": "特朗普：未指示贝森特干预美国债市，经济增长将自行化解债务问题",
    "url": "https://wallstreetcn.com/articles/3780037",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T21:29:16+00:00",
    "summary": "特朗普称，是贝森特自行决定干预债市，还称赞他很有能力、天生对债券和利率就有非常好的直觉。谈及贸易协议，特朗普称美加谈判进展顺利，理应能达成协议。"
  },
  {
    "id": "wscn:3780036",
    "domain": "股票",
    "title": "房利美12名高管突遭解雇，美国房贷市场稳定性担忧升温",
    "url": "https://wallstreetcn.com/articles/3780036",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T21:07:25+00:00",
    "summary": "据媒体报道，美国抵押贷款市场支柱机构房利美约12名高管遭突然解雇，被裁撤职位涵盖多家庭贷款、财务、监管等核心部门。目前正值美债收益率走高，借贷成本飙升之际，该消息引发外界对这一万亿级抵押贷款体系的稳定性忧虑升温。联邦住房金融局局长回应裁员是技术进步所致。"
  },
  {
    "id": "wscn:3780035",
    "domain": "股票",
    "title": "报道：博通的债务交易预计将达到700亿美元以上",
    "url": "https://wallstreetcn.com/articles/3780035",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T20:58:47+00:00",
    "summary": "博通正就700亿至800亿美元债务融资展开谈判，资金将用于支持Anthropic等AI公司的芯片采购需求。融资拟采用分层结构，优先档约450亿美元，次级档约350亿美元"
  },
  {
    "id": "wscn:3780033",
    "domain": "股票",
    "title": "瑞士央行官员：必要时将重启负利率，AI短期或推高通胀",
    "url": "https://wallstreetcn.com/articles/3780033",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T20:51:17+00:00",
    "summary": "瑞士央行政策委员会成员Petra Tschudin表示，若有必要，瑞士央行将再度实施负利率以维持通胀在0%至2%目标区间内，这是迄今最直接的负利率重启表态。当前瑞士基准利率为零，7月通胀仅0.4%。她同时指出，AI大规模投资短期内可能因芯片短缺推高价格，但长期压低通胀效果存疑。"
  },
  {
    "id": "wscn:3780032",
    "domain": "股票",
    "title": "伊朗回应美国经济战威胁：美方“注定失败”，中国表态：反对非法单边制裁",
    "url": "https://wallstreetcn.com/articles/3780032",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T20:36:02+00:00",
    "summary": "伊朗议会官员称，美国已证明其“不懂外交语言”，“实力的语言”将迫使美国解除对伊制裁、释放伊方资产并撤出该地区。中国外交部回应“美国威胁对伊制裁”：军事手段和制裁施压无助于解决问题。伊朗总统呼吁结束战争，但强调应从“实力地位”出发谈判。伊朗海军司令称“完全控制”霍尔木兹海峡、将在海上给敌人“历史性教训”。阿曼外交大臣与伊朗外长通话，讨论该海峡航运。"
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
    "id": "hn:49366252",
    "domain": "股票",
    "title": "OpenAI 'will be a public company in 2027' or sooner, CFO Friar tells employees",
    "url": "https://www.cnbc.com/2026/08/19/open-ai-ipo-timing-2027-friar.html",
    "source": "thm",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-19T19:42:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49311379",
    "domain": "股票",
    "title": "OpenAI talent exodus raises 'huge red flag' ahead of IPO",
    "url": "https://www.cnbc.com/2026/08/14/open-ai-ipo-red-flag.html",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-08-15T15:25:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49261857",
    "domain": "股票",
    "title": "The SpaceX Sham",
    "url": "https://dissentmagazine.org/online_articles/spacex-ipo-elon-musk-trillionaire/",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-08-11T17:47:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49305685",
    "domain": "股票",
    "title": "Backtesting Congress members stock trades by the disclosure date",
    "url": "https://investingpaths.com/tools/congress",
    "source": "ProdRatSuperior",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-14T23:08:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:49322233",
    "domain": "股票",
    "title": "AI is not just one bubble, strategist says – but a 'rolling sequence of bubbles'",
    "url": "https://fortune.com/2026/08/16/ai-bubble-sequence-saas-software-stocks-silver-prices-chipmakers/",
    "source": "pessimizer",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-16T18:05:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49338121",
    "domain": "股票",
    "title": "US tech stock correction likely, warn ECB economists",
    "url": "https://www.ft.com/content/cb4b22ab-4183-4d19-be60-6d2fab86d86d",
    "source": "aanet",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-17T21:46:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49024958",
    "domain": "股票",
    "title": "DOT cranks up its campaign to strip bike lane references from federal websites",
    "url": "https://text.npr.org/nx-s1-5900901",
    "source": "Jtsummers",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-07-23T17:11:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49253785",
    "domain": "股票",
    "title": "OpenAI wraps $7B share sale ahead of potential IPO",
    "url": "https://www.cnbc.com/2026/08/10/openai-wraps-7-billion-share-sale-ahead-of-potential-ipo-.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-08-11T05:40:35+00:00",
    "summary": ""
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
    "id": "hn:49257407",
    "domain": "股票",
    "title": "I backtested my own stock rankings. They lost to the index",
    "url": "https://holderdashboard.com/learn/backtest-that-lost-to-the-index",
    "source": "caiocmpaes",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-08-11T12:44:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49195657",
    "domain": "股票",
    "title": "The Investors Whose SpaceX Shares Vanished Before They Could Cash In",
    "url": "https://www.wsj.com/finance/stocks/spacex-ipo-spv-investors-2698a174",
    "source": "doener",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-06T12:19:44+00:00",
    "summary": ""
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
    "id": "rss:https://www.netinterest.co/p/apple-turnover",
    "domain": "股票",
    "title": "Apple Turnover",
    "url": "https://www.netinterest.co/p/apple-turnover",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-24T16:38:20+00:00",
    "summary": "How Tim Cook reshaped payments &#8211; and what he leaves behind"
  },
  {
    "id": "hn:49355142",
    "domain": "金融",
    "title": "Sticky wage norms and the real wage cost of unexpected inflation",
    "url": "https://bfi.uchicago.edu/wp-content/uploads/2026/08/BFI_WP_2026-108-1.pdf",
    "source": "jplusequalt",
    "platform": "hackernews",
    "points": 390,
    "published_at": "2026-08-19T00:53:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49175192",
    "domain": "金融",
    "title": "Thanks FedEx, This Is Why We Keep Getting Phished (2024)",
    "url": "https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/",
    "source": "stymaar",
    "platform": "hackernews",
    "points": 338,
    "published_at": "2026-08-04T21:09:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49325159",
    "domain": "金融",
    "title": "The federal keyword lists that canceled billions in research funding",
    "url": "https://www.highereddive.com/news/inside-the-federal-keyword-lists-that-canceled-billions-in-research-funding/826203/",
    "source": "walrus01",
    "platform": "hackernews",
    "points": 284,
    "published_at": "2026-08-17T00:14:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49200390",
    "domain": "金融",
    "title": "Federal Communications Commission scraps limit on broadcast TV ownership",
    "url": "https://www.nbcnews.com/business/media/federal-communications-commission-scraps-limit-broadcast-tv-ownership-rcna587641",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 179,
    "published_at": "2026-08-06T18:22:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49082695",
    "domain": "金融",
    "title": "Mondragon Corporation – a federation of co-operatives",
    "url": "https://en.wikipedia.org/wiki/Mondragon_Corporation",
    "source": "brnt",
    "platform": "hackernews",
    "points": 174,
    "published_at": "2026-07-28T12:19:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49046525",
    "domain": "金融",
    "title": "The Fedora 45 Sausage Factory",
    "url": "https://supakeen.com/weblog/the-fedora-45-sausage-factory/",
    "source": "6581",
    "platform": "hackernews",
    "points": 158,
    "published_at": "2026-07-25T11:04:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49122994",
    "domain": "金融",
    "title": "Situational Awareness down 67% in July in AI stock rout",
    "url": "https://www.wsj.com/finance/investing/situational-awareness-down-67-in-july-in-ai-stock-rout-cd19901f",
    "source": "pondsider",
    "platform": "hackernews",
    "points": 157,
    "published_at": "2026-07-31T13:37:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:49245487",
    "domain": "金融",
    "title": "Study links GLP-1 drugs to bigger jump in women's employment than a degree",
    "url": "https://finance.yahoo.com/healthcare/articles/harvard-study-links-glp-1-123000637.html",
    "source": "metadat",
    "platform": "hackernews",
    "points": 131,
    "published_at": "2026-08-10T16:02:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49118696",
    "domain": "金融",
    "title": "The bond market isn’t buying what Fed Chair Warsh is selling",
    "url": "https://www.reuters.com/commentary/reuters-open-interest/bond-market-isnt-buying-what-fed-chair-warsh-is-selling-2026-07-30/",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 139,
    "published_at": "2026-07-31T03:32:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49335163",
    "domain": "金融",
    "title": "Meta faces 'astronomical' consequences as legal fight reaches critical moment",
    "url": "https://www.cnbc.com/2026/08/17/meta-attorneys-general-california-federal-trial-astronomical-consequences.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 86,
    "published_at": "2026-08-17T18:06:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49259043",
    "domain": "金融",
    "title": "Federal vendor with $50M in contracts leaves portal broken for a month",
    "url": "https://www.propublica.org/article/foia-requests-responses",
    "source": "ams1",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-08-11T14:32:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49391382",
    "domain": "金融",
    "title": "Tesla sunsets its Solar Roof tiles",
    "url": "https://www.theverge.com/tech/983167/tesla-solar-roof-tiles-discontinued",
    "source": "doener",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-08-21T17:32:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49245071",
    "domain": "金融",
    "title": "Force-Fed by ICE",
    "url": "https://www.theguardian.com/us-news/2026/aug/10/ice-force-feeding-detention-gabar-choli",
    "source": "HotGarbage",
    "platform": "hackernews",
    "points": 97,
    "published_at": "2026-08-10T15:35:44+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.19217",
    "domain": "金融",
    "title": "CAT Bond Pricing with Kolmogorov--Arnold Networks",
    "url": "https://arxiv.org/abs/2608.19217",
    "source": "Sean Seow Cheng Hong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T04:00:00+00:00",
    "summary": "arXiv:2608.19217v1 Announce Type: new Abstract: We study the approximation of CAT bond prices under a compound Poisson loss model with lognormal severities using Kolmogorov--Arnold Networks (KANs). Bu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.19221",
    "domain": "金融",
    "title": "Filtering Credit Risk with Stochastic Discontinuities",
    "url": "https://arxiv.org/abs/2608.19221",
    "source": "F\\'elix B. Tambe-Ndonfack",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T04:00:00+00:00",
    "summary": "arXiv:2608.19221v1 Announce Type: new Abstract: We develop a structural credit-risk model under incomplete information in which investors observe firm value only indirectly through noisy market signal"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.19223",
    "domain": "金融",
    "title": "Henstock--Kurzweil Path Integral in Financial Mathematics: A Machine-Verified Pricing of European and Barrier Options",
    "url": "https://arxiv.org/abs/2608.19223",
    "source": "Alexander S. Ushakov, Yury N. Berdinsky",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T04:00:00+00:00",
    "summary": "arXiv:2608.19223v1 Announce Type: new Abstract: We apply the Henstock--Kurzweil (HK) gauge integral to the Black--Scholes model of option pricing and obtain the European call price directly from a Gau"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.19227",
    "domain": "金融",
    "title": "M3: A State-Event Generative Foundation Model for Market Microstructure Dynamics",
    "url": "https://arxiv.org/abs/2608.19227",
    "source": "Yanzhi Zhang, Yu Ma, Yilin Cheng, Jian Li, Yitong Duan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T04:00:00+00:00",
    "summary": "arXiv:2608.19227v1 Announce Type: new Abstract: Market microstructure simulation aims to model how liquidity, prices, and order flow evolve in electronic financial markets. Since market data reveal on"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.19389",
    "domain": "金融",
    "title": "Concentrated Liquidity Provision: a Reinforcement Learning Perspective",
    "url": "https://arxiv.org/abs/2608.19389",
    "source": "Georgios Chionas, Charalampos Kleitsikas, Stefanos Leonardos, Leandro S\\'anchez-Betancourt, Carmine Ventre",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T04:00:00+00:00",
    "summary": "arXiv:2608.19389v1 Announce Type: new Abstract: Automated market makers (AMMs) are a cornerstone of decentralised finance (DeFi). Constant product markets with concentrated liquidity, such as UniswapV"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.19394",
    "domain": "金融",
    "title": "Deep-MKV-TS: Path-Dependent McKean--Vlasov Control for Financial Time Series Generation",
    "url": "https://arxiv.org/abs/2608.19394",
    "source": "Samer El Boustany, Th\\'eo Basseras, Samy Mekkaoui, Alexandre Alouadi, Yadh Hafsi, Huy\\^en Pham",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T04:00:00+00:00",
    "summary": "arXiv:2608.19394v1 Announce Type: new Abstract: We introduce Deep-MKV-TS, a path-dependent McKean-Vlasov framework for financial scenario generation. The stochastic dynamics are chosen by matching sel"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.20020",
    "domain": "金融",
    "title": "The Reconfiguration Premium: Co-movement Structure as an Unspanned Dimension of the Variance Risk Premium",
    "url": "https://arxiv.org/abs/2608.20020",
    "source": "Lucas Carvalho",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T04:00:00+00:00",
    "summary": "arXiv:2608.20020v1 Announce Type: new Abstract: Hedge ratios, factor models and diversified portfolios all rest on an estimate of which firms move together. That estimate is not stable: firms migrate "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.20304",
    "domain": "金融",
    "title": "Calibration-Induced Degeneracy in LLM Financial Forecasting: An Audit-Trailed Case Study on Next-Day Market Risk",
    "url": "https://arxiv.org/abs/2608.20304",
    "source": "Arin Mohanty",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T04:00:00+00:00",
    "summary": "arXiv:2608.20304v1 Announce Type: new Abstract: Costly LLM features matter only if calibration lets them affect the forecast. We document a failure of this link in a next-day risk study of two broad-m"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.20179",
    "domain": "金融",
    "title": "Dynamic Portfolio Optimization under CVaR Constraints",
    "url": "https://arxiv.org/abs/2608.20179",
    "source": "Anran Hu, Silvana M. Pesenti, Xiaofei Shi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T04:00:00+00:00",
    "summary": "arXiv:2608.20179v1 Announce Type: cross Abstract: We study continuous-time dynamic portfolio optimization under a Conditional Value-at-Risk (CVaR) constraint on the investor's terminal loss. For a gen"
  },
  {
    "id": "rss:https://arxiv.org/abs/2411.11589",
    "domain": "金融",
    "title": "The Impact of the General Data Protection Regulation (GDPR) on Online Usage Behavior",
    "url": "https://arxiv.org/abs/2411.11589",
    "source": "Klaus M. Miller, Bernd Skiera, Julia Schmitt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T04:00:00+00:00",
    "summary": "arXiv:2411.11589v2 Announce Type: replace Abstract: Privacy regulations aim to safeguard consumers, but can have unintended consequences on how users interact with websites. This article estimates the"
  },
  {
    "id": "rss:https://arxiv.org/abs/2504.15985",
    "domain": "金融",
    "title": "Modeling and Forecasting Realized Volatility with Multivariate Fractional Brownian Motion",
    "url": "https://arxiv.org/abs/2504.15985",
    "source": "Markus Bibinger, Jun Yu, Chen Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T04:00:00+00:00",
    "summary": "arXiv:2504.15985v2 Announce Type: replace Abstract: A multivariate fractional Brownian motion (mfBm) with component-wise Hurst exponents is used to model and forecast realized volatility (RV). We inve"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.00554",
    "domain": "金融",
    "title": "ContestTrade: A Multi-Agent Trading System Based on Internal Contest Mechanism",
    "url": "https://arxiv.org/abs/2508.00554",
    "source": "Li Zhao, Rui Sun, Zuoyou Jiang, Bo Yang, Yuxiao Bai, Mengting Chen, Jing Li, Zuo Bai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T04:00:00+00:00",
    "summary": "arXiv:2508.00554v5 Announce Type: replace Abstract: In financial trading, large language model (LLM)-based agents demonstrate significant potential, but their decisions can be sensitive to noisy and n"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.14645",
    "domain": "金融",
    "title": "Are Final Market Prices Sufficient for Information Aggregation? Evidence from Last-Minute Dynamics in Parimutuel Betting",
    "url": "https://arxiv.org/abs/2509.14645",
    "source": "Hiroaki Hanyu, Shunsuke Ishii, Suguru Otani, Kazuhiro Teramoto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T04:00:00+00:00",
    "summary": "arXiv:2509.14645v3 Announce Type: replace Abstract: This study presents evidence challenging the practice of inferring risk preferences, probability perceptions, and beliefs from parimutuel betting ma"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.07045",
    "domain": "金融",
    "title": "Machine-learning a family of solutions to an optimal pension investment problem",
    "url": "https://arxiv.org/abs/2511.07045",
    "source": "John Armstrong, Cristin Buescu, James Dalby, Rohan Hobbs",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T04:00:00+00:00",
    "summary": "arXiv:2511.07045v2 Announce Type: replace Abstract: We use a neural network to identify the optimal solutions to a family of pension investment problems, where the parameters determining an investor's"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.23325",
    "domain": "金融",
    "title": "Happy Birthday? Age Labels, Search Criteria, and Matching from Dating to Marriage",
    "url": "https://arxiv.org/abs/2607.23325",
    "source": "Suguru Otani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T04:00:00+00:00",
    "summary": "arXiv:2607.23325v2 Announce Type: replace Abstract: Age is a match trait and a prominent label on search platforms. Using confidential records from a large Japanese marriage platform, I study how a bi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.23955",
    "domain": "金融",
    "title": "From Accuracy to Auditability: A Survey of Determinism in Financial AI Systems",
    "url": "https://arxiv.org/abs/2605.23955",
    "source": "Ruizhe Zhou, Xiaoyang Liu, Gaoyuan Du, Yi Zheng, Shouxi Ren, Deepayan Chakrabarti, Dengdu Jiang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T04:00:00+00:00",
    "summary": "arXiv:2605.23955v3 Announce Type: replace-cross Abstract: Deploying machine learning in regulated financial environments -- credit risk, fraud detection, and anti-money laundering -- exposes critical "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.12143",
    "domain": "金融",
    "title": "Robustness over efficiency in climate coalitions: a bistable model and a map of architectures",
    "url": "https://arxiv.org/abs/2608.12143",
    "source": "Juergen Renn (Max Planck Institute of Geoanthropology, Jena, Germany)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T04:00:00+00:00",
    "summary": "arXiv:2608.12143v3 Announce Type: replace-cross Abstract: Designs for international climate cooperation face a trade-off between efficiency and robustness to institutional erosion by defection, renego"
  },
  {
    "id": "hn:49206115",
    "domain": "金融",
    "title": "Anthropic CEO reportedly worried new hires only care about money",
    "url": "https://finance.yahoo.com/technology/ai/articles/anthropic-ceo-reportedly-worried-hires-160000647.html",
    "source": "frays",
    "platform": "hackernews",
    "points": 65,
    "published_at": "2026-08-07T05:15:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49304409",
    "domain": "金融",
    "title": "Make a 6-Tesla-class high-temperature superconducting dipole magnet at 4.2 K",
    "url": "https://journals.aps.org/prab/abstract/10.1103/4nhs-bkwh",
    "source": "supermagnet",
    "platform": "hackernews",
    "points": 44,
    "published_at": "2026-08-14T20:49:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:49352830",
    "domain": "金融",
    "title": "The most influential economist is oddly unconvincing",
    "url": "https://www.economist.com/finance-and-economics/2026/08/17/the-worlds-most-influential-economist-is-oddly-unconvincing",
    "source": "aragonite",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-18T21:15:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49350858",
    "domain": "金融",
    "title": "AI Is Upending One of Finance's Cushiest Jobs",
    "url": "https://www.bloomberg.com/news/features/2026-06-05/ai-is-upending-traditional-financial-advisor-jobs",
    "source": "theriddlr",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-18T18:59:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49243531",
    "domain": "金融",
    "title": "China is now the world's greatest oil power",
    "url": "https://www.economist.com/finance-and-economics/2026/08/09/china-is-now-the-worlds-great-oil-power",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-08-10T13:40:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:49097833",
    "domain": "金融",
    "title": "Show HN: The Federalist Papers, typeset as the 1787 newspapers they ran in",
    "url": "https://federalistreader.org/",
    "source": "vhwalke",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-07-29T14:13:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49215292",
    "domain": "金融",
    "title": "Mykhailo Fedorov reveals struggle to secure Patriot missiles and Western support",
    "url": "https://www.uawire.org/former-ukrainian-defense-minister-mykhailo-fedorov-reveals-struggles-to-secure-patriot-missiles-and-western-support",
    "source": "greedo",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-08-07T19:38:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:49111879",
    "domain": "金融",
    "title": "Citadel Buys Situational Awareness's Stock Portfolio After Big Losses in AI",
    "url": "https://www.wsj.com/finance/citadel-buys-situational-awarenesss-stock-portfolio-after-big-losses-in-ai-5117159b",
    "source": "mudil",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-07-30T16:00:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49082706",
    "domain": "金融",
    "title": "AI revenues are growing fast, but not fast enough",
    "url": "https://www.economist.com/finance-and-economics/2026/07/28/ai-revenues-are-growing-fast-but-not-fast-enough",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-07-28T12:19:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49197127",
    "domain": "金融",
    "title": "Former Federal Prosecutors to Senate: Stop Confirming Election Deniers as Judges",
    "url": "https://abovethelaw.com/2026/08/former-federal-prosecutors-to-senate-stop-confirming-election-deniers-to-the-federal-bench/",
    "source": "hn_acker",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-08-06T14:25:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49173576",
    "domain": "金融",
    "title": "Investors in Situational Awareness deserved to lose their shirts",
    "url": "https://www.economist.com/finance-and-economics/2026/08/04/investors-in-situational-awareness-deserved-to-lose-their-shirts",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-08-04T19:18:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49184251",
    "domain": "金融",
    "title": "Fed's Kashkari says 'now is the time to start slowly moving' rates up",
    "url": "https://www.cnbc.com/2026/08/05/feds-kashkari-says-now-is-the-time-to-start-slowly-moving-rates-up.html",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-08-05T15:24:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49214813",
    "domain": "金融",
    "title": "US Sold Euros to Save the Yen, Europe Found Out After",
    "url": "https://finance.yahoo.com/markets/currencies/articles/us-sold-euros-save-yen-033819315.html",
    "source": "amarcheschi",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-07T18:54:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49157782",
    "domain": "金融",
    "title": "US Schools Are Ditching Chromebooks for MacBooks by the Thousands",
    "url": "https://finance.yahoo.com/technology/articles/us-schools-ditching-chromebooks-macbooks-233015401.html",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-08-03T16:16:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:49289340",
    "domain": "金融",
    "title": "Hooray for index funds–just don't call them passive",
    "url": "https://www.economist.com/finance-and-economics/2026/08/11/hooray-for-index-funds-just-dont-call-them-passive",
    "source": "thm",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-13T17:37:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49208461",
    "domain": "金融",
    "title": "New Intelligence Warns Russia May Provoke NATO Amid Dwindling U.S. Munitions",
    "url": "https://www.wsj.com/finance/investing/new-intelligence-warns-russia-may-provoke-nato-amid-dwindling-u-s-munitions-68f497c7",
    "source": "doener",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-07T10:52:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49182971",
    "domain": "金融",
    "title": "OpenAI settles claims of discrimination against US workers for $3.2M",
    "url": "https://finance.yahoo.com/technology/ai/articles/openai-settles-claims-discrimination-against-221429616.html",
    "source": "declan_roberts",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-08-05T13:57:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:49033778",
    "domain": "金融",
    "title": "Reality Bites Elon Musk and His Tesla, SpaceX Believers",
    "url": "https://www.wsj.com/finance/stocks/reality-bites-elon-musk-and-his-tesla-spacex-believers-1b639591",
    "source": "doener",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-24T10:59:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49028304",
    "domain": "金融",
    "title": "US announces double-digit tariffs on most of globe to replace expiring duties",
    "url": "https://finance.yahoo.com/economy/policy/article/trump-administration-announces-the-next-phase-of-global-tariffs-with-10-to-125-rates-on-much-of-the-globe-210032314.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-07-23T21:28:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:49047488",
    "domain": "金融",
    "title": "Stripe in talks to acquire OpenRouter in potential $10B deal, WSJ reports",
    "url": "https://finance.yahoo.com/technology/ai/articles/stripe-talks-acquire-openrouter-potential-215104525.html",
    "source": "nlpnerd",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-25T13:38:45+00:00",
    "summary": ""
  }
]
```
