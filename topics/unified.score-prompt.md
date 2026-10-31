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

- 今日日期：`2026-10-31`
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
  "date": "2026-10-31",
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
    "points": 2058266,
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
    "points": 1455329,
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
    "points": 1414139,
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
    "points": 1381173,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1DLGV6XEbH",
    "domain": "AI",
    "title": "全球首个科研全家桶 Agent：LaTeX、绘图、文献库、免费云服务器全都有丨ClawsGO Science 正式发布",
    "url": "http://www.bilibili.com/video/av117020041486082",
    "source": "Nitres",
    "platform": "bilibili",
    "points": 1140650,
    "published_at": "2026-08-01T11:35:43+00:00",
    "summary": "全球首个科研全家桶 Agent：LaTeX、绘图、文献库、免费云服务器全都有丨ClawsGO Science 正式发布"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 907301,
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
    "points": 884443,
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
    "points": 737053,
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
    "points": 426574,
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
    "points": 365269,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 341642,
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
    "points": 317995,
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
    "points": 290391,
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
    "points": 221129,
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
    "points": 185319,
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
    "points": 164148,
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
    "points": 161590,
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
    "points": 146514,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 103413,
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
    "points": 94192,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 94018,
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
    "points": 76709,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 73812,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1713u6XE1D",
    "domain": "AI",
    "title": "Claude Code 完全接管了 Blender，然后创造了这个",
    "url": "http://www.bilibili.com/video/av116980883398142",
    "source": "stefan_3d_ai",
    "platform": "bilibili",
    "points": 70187,
    "published_at": "2026-07-26T11:00:00+00:00",
    "summary": "如果你给一个完全自主的 AI 代理提供对 Blender 的完整终端控制权限，并让它完完全全靠自己独立运行整整一个小时，到底会发生什么可怕的事情？\n\n在这个视频中，我远远超越了简单的代码复制粘贴，结合 Claude Code 和全新发布的官方 Blender MCP 服务器，深入探索了真正的 3D 工作流自动化究竟长什么样。\n\n---\n\n🔹 试用 Tripo AI 并免费获取 500 生成积分：h"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 64081,
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
    "points": 56571,
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
    "points": 49908,
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
    "points": 47779,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1hxMbzqEzU",
    "domain": "AI",
    "title": "小智MCP自由了！我开源了个命令行神器实现多MCP聚合",
    "url": "http://www.bilibili.com/video/av114686414625640",
    "source": "闪电蘑菇",
    "platform": "bilibili",
    "points": 42884,
    "published_at": "2025-06-15T08:31:55+00:00",
    "summary": "- 我写的小智客户端命令行工具\n - github: https://github.com/shenjingnan/xiaozhi-client\n - gitee: https://gitee.com/shenjingnan/xiaozhi-client\n\n- 小智官方MCP示例代码仓库：\n - github: https://github.com/78/mcp-calculator\n - git"
  },
  {
    "id": "bvid:BV14rxM6qEnL",
    "domain": "AI",
    "title": "最新Skills开发教程，Agent skill实战|WorkBuddy+Codex+DeepSeek Harness",
    "url": "http://www.bilibili.com/video/av117511429295044",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 41785,
    "published_at": "2026-10-28T02:00:00+00:00",
    "summary": "【课程简介】Agent Skills零基础教程，从WorkBuddy、Codex上手到项目落地实战。"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 41503,
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 41072,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 34520,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 29944,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29903,
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
    "points": 29028,
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
    "points": 25879,
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
    "points": 24831,
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
    "points": 22837,
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
    "points": 21173,
    "published_at": "2024-11-18T07:04:36+00:00",
    "summary": "欢迎关注我的知识星球：https://t.zsxq.com/FF0He\n\n我会分享最新AI资讯、源代码、回答你的提问。\n\n视频亮点：\n\n双工具对比：解析 Cursor 和 Windsurf 各自优势\n实战案例：从五子棋到卡路里计算AI应用的完整开发过程\n专业部署：Android Studio 配置与构建技巧\n\n时间戳：\n\n0:00 - 引言\n\n0:26 - 我开发的应用演示\n\n2:33 - Rea"
  },
  {
    "id": "bvid:BV1koJt6iE7N",
    "domain": "AI",
    "title": "AI 操作手机教程｜超爽！",
    "url": "http://www.bilibili.com/video/av117450377004656",
    "source": "黄白AIGC",
    "platform": "bilibili",
    "points": 20205,
    "published_at": "2026-10-16T11:37:54+00:00",
    "summary": "我把手机接到Agent后，试着让它自己处理开发票。它能看着手机画面点击、滑动，找到订单、填写资料，再把开好的发票整理到电脑。看着屏幕自己动起来，确实有点爽。\n这期也拍了接入过程：iPhone 配 Mac 用「iPhone 镜像」；安卓用数据线、ADB 和 scrcpy。接好后，打开 Computer Use，把要处理的订单、固定资料和例外情况交代清楚。开票、填表、查物流这类重复操作，都可以从一个小"
  },
  {
    "id": "bvid:BV1f57C6YErb",
    "domain": "AI",
    "title": "手把手教你Codex安装和使用MCP！新手必备~",
    "url": "http://www.bilibili.com/video/av116696861907147",
    "source": "Raina测试",
    "platform": "bilibili",
    "points": 18348,
    "published_at": "2026-06-06T11:29:00+00:00",
    "summary": "这一期给大家分享下在codex里面如何配置和使用MCP，和skill一样，MCP也是我们平时用得比较多的，所以建议大家也可以学一下它的基础配置和使用~\n步骤都不难，跟着操作就可以了"
  },
  {
    "id": "bvid:BV1HhGo6aEvE",
    "domain": "AI",
    "title": "本地大模型也能联网搜索！LM Studio × MCP 接入教程",
    "url": "http://www.bilibili.com/video/av116635490911881",
    "source": "aopstudio",
    "platform": "bilibili",
    "points": 16516,
    "published_at": "2026-05-25T13:41:46+00:00",
    "summary": "本视频演示如何为 LM Studio 接入 MCP 联网搜索服务，让本地运行的大模型具备实时搜索网络的能力。\nMCP（Model Context Protocol）是 Anthropic 推出的开放协议，允许模型通过标准化接口调用外部工具。本次接入的搜索服务来自 MCPWorld，底层通过 npx 调用，无需额外部署服务端，配置完成后即可在 LM Studio 的对话界面中直接发起联网搜索。\n本视"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 15454,
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
    "points": 15448,
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
    "points": 13423,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1tDnV6ME79",
    "domain": "AI",
    "title": "当我把claude code搬进安卓设备……",
    "url": "http://www.bilibili.com/video/av117462439826705",
    "source": "Grey-Oak",
    "platform": "bilibili",
    "points": 12610,
    "published_at": "2026-10-18T14:44:02+00:00",
    "summary": "cccodroid 是一个开源的安卓应用，把 Claude Code 装进你的安卓设备。不用 root，不刷机，也不套 Linux 虚拟环境，工具直接在安卓上原生运行。\n\n视频全程实机录屏（联想y700二代平板，骁龙 8+），没有连电脑：\n· 一句话让它改代码，先给计划，你点批准才动手\n· 终端里 pkg install rust，现场打包 APK 装上\n· docx / xlsx / pptx "
  },
  {
    "id": "bvid:BV1Yhb66LEaF",
    "domain": "AI",
    "title": "3分钟，教你什么是vibe coding",
    "url": "http://www.bilibili.com/video/av117115000524101",
    "source": "开聊pro",
    "platform": "bilibili",
    "points": 11432,
    "published_at": "2026-08-18T06:12:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Nxxr6oES2",
    "domain": "AI",
    "title": "耗资上万！我重制了网页版MC！【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av117533474559602",
    "source": "土豆味小哲",
    "platform": "bilibili",
    "points": 11019,
    "published_at": "2026-10-31T03:55:11+00:00",
    "summary": "全程使用Claude Opus 5.5开发~\n三连+关注可以获得披风+联机权限！\n游玩链接：https://www.bilibili.com/toy/OpusMC\n\n往期开发过程：\nBV1HkJ66vEk9\nBV126Hw6uEgW"
  },
  {
    "id": "bvid:BV1rhdgBMEK2",
    "domain": "AI",
    "title": "Claude Code + Figma MCP：传统 UI 开发流程已死？",
    "url": "http://www.bilibili.com/video/av116538183124050",
    "source": "犬哥网站",
    "platform": "bilibili",
    "points": 10800,
    "published_at": "2026-05-08T12:00:00+00:00",
    "summary": "▬▬▬▬▬ 🏆️ 犬哥专业服务 🏆️ ▬▬▬▬▬\n网页设计＆数位行销服务 ➜ https://frankknow.com\nWordPress 优质主机：https://frankknow.com/wordpress-hosting/\n\n▬▬▬▬▬ 🏆️ 精选架站系列 🏆️ ▬▬▬▬▬\n新手自学架站（网域＋主机＋WordPress 架站，一次学会）➜ https://frankknow.com/wp"
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
    "id": "hn:50293047",
    "domain": "AI 算力 / 半导体",
    "title": "Alleged Chinese spy had 'close relationship' with Nvidia boss Jensen Huang",
    "url": "https://nypost.com/2026/10/29/business/alleged-chinese-spy-had-close-relationship-with-nvidia-boss-jensen-huang-report/",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 355,
    "published_at": "2026-10-29T17:43:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50219700",
    "domain": "AI 算力 / 半导体",
    "title": "GPU-unlock: FP/BF16 instruction issue rate on Nvidia 3000's cards",
    "url": "https://github.com/Zagitta/gpu-unlock",
    "source": "fragebogen",
    "platform": "hackernews",
    "points": 351,
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
    "points": 175,
    "published_at": "2026-10-25T21:07:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50275128",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Transcribe: open ASR for 40 languages",
    "url": "https://huggingface.co/blog/nvidia/nemotron-transcribe-granary",
    "source": "wondersky",
    "platform": "hackernews",
    "points": 133,
    "published_at": "2026-10-28T15:17:53+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/google-agentic-ai-will-drive-new-demands-on-data-center-cpus/",
    "domain": "AI 算力 / 半导体",
    "title": "Google: Agentic AI Will Drive New Demands on Data Center CPUs",
    "url": "https://www.eetimes.com/google-agentic-ai-will-drive-new-demands-on-data-center-cpus/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T20:13:41+00:00",
    "summary": "Agents present a bursty workload, leaving CPUs frequently idle, which is placing new demands on CPU infrastructure. The post Google: Agentic AI Will Drive New Demands on Data Center CPUs appeared firs"
  },
  {
    "id": "rss:https://www.eetimes.com/intels-q3-results-show-supply-chain-disruptions-and-pc-plunge/",
    "domain": "AI 算力 / 半导体",
    "title": "Intel’s Q3 Results Show Supply Chain Disruptions and PC Plunge",
    "url": "https://www.eetimes.com/intels-q3-results-show-supply-chain-disruptions-and-pc-plunge/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T16:37:20+00:00",
    "summary": "Intel faces a tough challenge as manufacturing bottlenecks and rising memory costs impact PC sales despite strong data center growth. The post Intel’s Q3 Results Show Supply Chain Disruptions and PC P"
  },
  {
    "id": "rss:https://www.eetimes.com/why-shrinking-component-geometries-force-a-rethink-of-bga-rework-heating-methods/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Shrinking Component Geometries Force a Rethink of BGA Rework Heating Methods",
    "url": "https://www.eetimes.com/why-shrinking-component-geometries-force-a-rethink-of-bga-rework-heating-methods/",
    "source": "Emily Newton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T10:32:26+00:00",
    "summary": "As components shrink to 01005 scale and board densities rise, BGA rework requires more precise heat control. The post Why Shrinking Component Geometries Force a Rethink of BGA Rework Heating Methods a"
  },
  {
    "id": "rss:https://www.eetimes.com/infineons-oktobertech-edge-ai-sdvs-and-the-road-to-800-vdc/",
    "domain": "AI 算力 / 半导体",
    "title": "Infineon’s OktoberTech: Edge AI, SDVs, and the Road to 800 VDC",
    "url": "https://www.eetimes.com/infineons-oktobertech-edge-ai-sdvs-and-the-road-to-800-vdc/",
    "source": "Aalyia Shaukat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T20:59:28+00:00",
    "summary": "Explore Infineon’s OktoberTech takeaways on edge AI, SDVs, GaN power, and the shift toward 800 V DC data centers. The post Infineon’s OktoberTech: Edge AI, SDVs, and the Road to 800 VDC appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/samsung-electronics-posts-80b-operating-profit-on-ai-memory-demand/",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung Electronics Posts $80B Operating Profit on AI Memory Demand",
    "url": "https://www.eetimes.com/samsung-electronics-posts-80b-operating-profit-on-ai-memory-demand/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T16:20:34+00:00",
    "summary": "Samsung reported third-quarter operating profit of $80 billion, but rising component prices caused an operating loss in mobile. The post Samsung Electronics Posts $80B Operating Profit on AI Memory De"
  },
  {
    "id": "rss:https://www.eetimes.com/how-vision-and-connectivity-enable-autonomous-agriculture/",
    "domain": "AI 算力 / 半导体",
    "title": "How Vision and Connectivity Enable Autonomous Agriculture",
    "url": "https://www.eetimes.com/how-vision-and-connectivity-enable-autonomous-agriculture/",
    "source": "Analog Devices, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T16:07:54+00:00",
    "summary": "Join this webinar to explore how Gigabit Multimedia Serial Link (GMSL) technology helps enable the next generation of autonomous agricultural equipment. The post How Vision and Connectivity Enable Aut"
  },
  {
    "id": "rss:https://www.eetimes.com/smarter-power-sequencing-with-greenpak/",
    "domain": "AI 算力 / 半导体",
    "title": "Smarter Power Sequencing with GreenPAK™",
    "url": "https://www.eetimes.com/smarter-power-sequencing-with-greenpak/",
    "source": "Dima Mymrikov, Sr. Director of GreenPAK Product Marketing, Renesas Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T13:00:00+00:00",
    "summary": "Programmable mixed-signal devices can replace sprawling RC networks and firmware-dependent control with compact, deterministic, and adaptable multi-rail sequencing. The post Smarter Power Sequencing w"
  },
  {
    "id": "rss:https://www.eetimes.com/stmicroelectronics-weighs-developing-more-powerful-mcus-mpus-for-humanoid-robots/",
    "domain": "AI 算力 / 半导体",
    "title": "STMicroelectronics Weighs Developing More Powerful MCUs, MPUs for Humanoid Robots",
    "url": "https://www.eetimes.com/stmicroelectronics-weighs-developing-more-powerful-mcus-mpus-for-humanoid-robots/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T11:48:02+00:00",
    "summary": "With humanoid robot designs still evolving and volumes low, STMicroelectronics is watching how the market develops before deciding what to build. The post STMicroelectronics Weighs Developing More Pow"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-store-quietly-pulls-the-rtx-5080-following-rtx-5090-removal-street-prices-climb-to-2-2x-over-msrp",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia store quietly pulls the RTX 5080 following RTX 5090 removal",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-store-quietly-pulls-the-rtx-5080-following-rtx-5090-removal-street-prices-climb-to-2-2x-over-msrp",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T20:13:10+00:00",
    "summary": "First the RTX 5090, now the RTX 5080. Nvidia quietly removes the RTX 5080 listing from the marketplace as prices explode to 2.2X MSRP on the retail market."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intels-woes-wipe-out-usd1-trillion-of-semiconductor-market-cap-in-one-day-pc-market-bloodbath-leaves-few-chip-stocks-unscathed",
    "domain": "AI 算力 / 半导体",
    "title": "Intel’s woes wipe out $1 trillion of semiconductor market cap in one day",
    "url": "https://www.tomshardware.com/pc-components/cpus/intels-woes-wipe-out-usd1-trillion-of-semiconductor-market-cap-in-one-day-pc-market-bloodbath-leaves-few-chip-stocks-unscathed",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T20:06:11+00:00",
    "summary": "Intel's gloomy outlook for its PC business wipes out $1 trillion of semiconductor market capitalization in a day, barely affects Apple."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/celebrate-warhammer-day-on-the-31st-of-october-with-these-20-warhammer-40k-themed-products-the-best-space-marine-gear-this-side-of-the-warp",
    "domain": "AI 算力 / 半导体",
    "title": "Celebrate Warhammer Day on the 31st of October with these 20 Warhammer 40K-themed products",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/celebrate-warhammer-day-on-the-31st-of-october-with-these-20-warhammer-40k-themed-products-the-best-space-marine-gear-this-side-of-the-warp",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T18:30:00+00:00",
    "summary": "Warhammer Day is celebrated on October 31st 2026, 2026. Check out these great gift ideas for all fans of the grimdark future."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/openai-ceo-says-its-quite-terrible-for-your-pc-to-have-ram-sam-altman-says-data-centers-offer-better-utilization",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI CEO says it's 'quite terrible' for your PC to have RAM",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/openai-ceo-says-its-quite-terrible-for-your-pc-to-have-ram-sam-altman-says-data-centers-offer-better-utilization",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T16:28:11+00:00",
    "summary": "OpenAI CEO Sam Altman said in a podcast interview that \"it's quite terrible\" for people to have RAM in their own PCs when it could go into AI data centers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/photonics/psiquantum-turns-its-photonics-know-how-into-an-optical-switch-for-supercharging-ai-data-center-gpu-networks-8x8-lab-prototype-loses-less-light-than-rivals-with-plans-to-develop-larger-devices",
    "domain": "AI 算力 / 半导体",
    "title": "PsiQuantum turns its photonics know-how into an optical switch for supercharging AI data center GPU networks",
    "url": "https://www.tomshardware.com/tech-industry/photonics/psiquantum-turns-its-photonics-know-how-into-an-optical-switch-for-supercharging-ai-data-center-gpu-networks-8x8-lab-prototype-loses-less-light-than-rivals-with-plans-to-develop-larger-devices",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T14:30:00+00:00",
    "summary": "PsiQuantum’s eight-port optical switch typically loses 1.2 dB, under a quarter of its light, where data centers allow up to 3 dB."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/tcl-27c2a-pro-27-inch-qd-mini-led-4k-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "TCL 27C2A Pro 27-inch QD-Mini LED 4K gaming monitor review: Extreme color and brightness",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/tcl-27c2a-pro-27-inch-qd-mini-led-4k-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T14:00:00+00:00",
    "summary": "TCL’s 27C2A Pro is a super-bright 27-inch 4K Mini LED gaming monitor with full-array local dimming (2,304 zones), Quantum Dot color, 160 Hz, 320 Hz/FHD mode, HDR10 and Adaptive-Sync. It’s also color-a"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/usb-flash-drives/intelligence-agency-misplaced-a-very-significant-number-of-removable-drives-storage-media-have-been-missing-for-years-but-exact-number-of-lost-devices-remain-unknown",
    "domain": "AI 算力 / 半导体",
    "title": "Intelligence agency misplaced 'a very significant number' of removable drives",
    "url": "https://www.tomshardware.com/pc-components/usb-flash-drives/intelligence-agency-misplaced-a-very-significant-number-of-removable-drives-storage-media-have-been-missing-for-years-but-exact-number-of-lost-devices-remain-unknown",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T13:35:48+00:00",
    "summary": "An investigation revealed that thousands of drives have been lost, with officials having no idea where they could be."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/a-primer-on-key-ai-llm-concepts-kv-cache-weights-quantization-and-how-inference-actually-works",
    "domain": "AI 算力 / 半导体",
    "title": "A primer on key AI LLM concepts — KV cache, weights, quantization, and how inference actually works",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/a-primer-on-key-ai-llm-concepts-kv-cache-weights-quantization-and-how-inference-actually-works",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T13:30:00+00:00",
    "summary": "How do AI models work? This primer explains crucial concepts to understand how LLMs work, with definitions and explanations for all of AI's new nomenclature."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/this-is-your-chance-to-secure-an-entire-entry-level-abs-gaming-pc-for-only-usd849-amazing-walmart-deal-sets-you-up-with-an-rtx-5060-graphics-card-and-shaves-usd350-off-the-list-price",
    "domain": "AI 算力 / 半导体",
    "title": "This is your chance to secure an entire entry-level ABS gaming PC for only $849",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/this-is-your-chance-to-secure-an-entire-entry-level-abs-gaming-pc-for-only-usd849-amazing-walmart-deal-sets-you-up-with-an-rtx-5060-graphics-card-and-shaves-usd350-off-the-list-price",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T13:00:00+00:00",
    "summary": "An affordable desktop gaming PC with an RTX 5060 GPU inside for under $850."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/5-years-worth-of-salary-in-bonuses-given-to-700-eligible-micron-workers-as-company-continues-to-battle-union-more-than-4-300-production-line-staff-to-receive-three-bonuses-of-more-than-usd31-000-plus-quarterly-profit-bonuses-starting-next-year",
    "domain": "AI 算力 / 半导体",
    "title": "5 years’ worth of salary in bonuses given to 700 eligible Micron workers as company continues to battle union",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/5-years-worth-of-salary-in-bonuses-given-to-700-eligible-micron-workers-as-company-continues-to-battle-union-more-than-4-300-production-line-staff-to-receive-three-bonuses-of-more-than-usd31-000-plus-quarterly-profit-bonuses-starting-next-year",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T11:44:03+00:00",
    "summary": "Eligible employees get an annual performance bonus, a mass-production bonus, and a one-time appreciation bonus. A quarterly profit bonus has also been introduced starting January 2027."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-leaker-reveals-moon-lake-chip-as-a-likely-replacement-for-n-series-socs-four-lower-power-efficiency-cores-no-performance-cores-and-a-6-w-tdp",
    "domain": "AI 算力 / 半导体",
    "title": "Intel leaker reveals Moon Lake chip as a likely replacement for N-series SoCs",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-leaker-reveals-moon-lake-chip-as-a-likely-replacement-for-n-series-socs-four-lower-power-efficiency-cores-no-performance-cores-and-a-6-w-tdp",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T11:40:00+00:00",
    "summary": "An Intel leaker revealed Moon Lake chip as a likely replacement for N-series SoCs with four lower-power-efficiency cores, no performance cores, and a 6-watt TDP"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/cisco-gives-27-year-old-engineer-unlimited-ai-tokens-to-rewrite-98-percent-of-the-companys-legacy-code-in-24-months-president-plucks-former-startup-founder-telling-him-to-go-nuts",
    "domain": "AI 算力 / 半导体",
    "title": "Cisco gives 27-year-old engineer unlimited AI tokens to rewrite 98% of the company's legacy code in 24 months",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/cisco-gives-27-year-old-engineer-unlimited-ai-tokens-to-rewrite-98-percent-of-the-companys-legacy-code-in-24-months-president-plucks-former-startup-founder-telling-him-to-go-nuts",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T11:26:56+00:00",
    "summary": "Cisco President Jeetu Patel has handed a 27-year-old ex-startup founder a huge job to rewrite 98% of Cisco's legacy code within 24 months."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/esports-commentator-builds-his-own-custom-mouse-shell-generator-for-3d-printing-that-doesnt-use-ai-mausstudio-automatically-detects-buttons-screwholes-and-sensor-locations",
    "domain": "AI 算力 / 半导体",
    "title": "Former esports commentator builds his own custom mouse shell generator for 3D printing that doesn’t use AI",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/esports-commentator-builds-his-own-custom-mouse-shell-generator-for-3d-printing-that-doesnt-use-ai-mausstudio-automatically-detects-buttons-screwholes-and-sensor-locations",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T11:20:00+00:00",
    "summary": "A Counter-Strike commentator just showed the demo of his customizable gaming mouse shell generator for 3D printing that detects key components like mouse buttons, the scroll wheel, and screw hole loca"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/benchmarking-nvidias-vera-cpu-for-the-data-center-standalone-vera-tested-against-granite-rapids-ap-and-epyc-turin",
    "domain": "AI 算力 / 半导体",
    "title": "Benchmarking Nvidia’s Vera CPU for the data center — standalone Vera tested against Granite Rapids-AP and EPYC Turin",
    "url": "https://www.tomshardware.com/pc-components/cpus/benchmarking-nvidias-vera-cpu-for-the-data-center-standalone-vera-tested-against-granite-rapids-ap-and-epyc-turin",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T11:00:00+00:00",
    "summary": "Nvidia gave us access to its Vera data center CPU for testing against Intel's Granite Rapids-AP and AMD's EPYC Turin."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/grab-a-nintendo-switch-2-with-a-free-game-for-as-low-as-usd459-in-this-limited-time-deal-coupon-code-knocks-usd60-off-sale-price-for-new-woot-customers-usd40-for-existing-ones",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a Nintendo Switch 2 with a free game for as low as $459 in this limited-time deal",
    "url": "https://www.tomshardware.com/video-games/nintendo/grab-a-nintendo-switch-2-with-a-free-game-for-as-low-as-usd459-in-this-limited-time-deal-coupon-code-knocks-usd60-off-sale-price-for-new-woot-customers-usd40-for-existing-ones",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T10:44:01+00:00",
    "summary": "Grab the Nintendo Switch 2 with a free digital game for as low as $459 for a limited-time only at Woot! if you use coupon code SAVETOBER."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/criminal-investigation-launched-into-googles-ai-data-center-deforestation-in-finland-local-police-act-over-multiple-complaints-about-breaches-of-environmental-law",
    "domain": "AI 算力 / 半导体",
    "title": "Google hit with criminal probe over unapproved AI data center deforestation",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/criminal-investigation-launched-into-googles-ai-data-center-deforestation-in-finland-local-police-act-over-multiple-complaints-about-breaches-of-environmental-law",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T10:40:00+00:00",
    "summary": "A criminal investigation into the environmental damage caused by Google’s Finnish subsidiary has been launched."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptocurrency/binance-withdrawals-frozen-after-thieves-steal-usd5-6-billion-in-crypto-in-record-breaking-cryptocurrency-heist-firm-says-it-will-cover-losses-as-stablecoin-networks-move-to-freeze-usd2-4b-in-stolen-assets",
    "domain": "AI 算力 / 半导体",
    "title": "Suspected North Korean hackers steal $5.6 billion in crypto in record-breaking cryptocurrency heist, Binance withdrawals frozen",
    "url": "https://www.tomshardware.com/tech-industry/cryptocurrency/binance-withdrawals-frozen-after-thieves-steal-usd5-6-billion-in-crypto-in-record-breaking-cryptocurrency-heist-firm-says-it-will-cover-losses-as-stablecoin-networks-move-to-freeze-usd2-4b-in-stolen-assets",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T10:31:11+00:00",
    "summary": "Binance withdrawals frozen after thieves run off with $5.6 billion in crypto — firm says it will cover losses as stablecoin networks move to freeze $2.4b in stolen assets"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/south-korea-clamps-down-on-tesla-drivers-for-unlocking-restricted-fsd-usd15-000-fines-and-prison-possible-sentences-suspects-imported-hardware-from-europe-and-china-then-traded-tips-on-concealing-activation-logs",
    "domain": "AI 算力 / 半导体",
    "title": "South Korea clamps down on Tesla drivers for unlocking restricted full self-driving feature, $15,000 fines and prison possible sentences",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/south-korea-clamps-down-on-tesla-drivers-for-unlocking-restricted-fsd-usd15-000-fines-and-prison-possible-sentences-suspects-imported-hardware-from-europe-and-china-then-traded-tips-on-concealing-activation-logs",
    "source": "Newton Gitonga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T10:20:00+00:00",
    "summary": "South Korean police have booked 80 Tesla owners for bypassing regional restrictions on Full Self-Driving (FSD), seizing 21 devices allegedly used to unlock the driver-assistance software. Some suspect"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/deadly-intel-fab-28-explosion-causes-two-week-shutdown-to-cost-usd600-million-and-severely-disrupt-server-chip-manufacturing-for-six-months-10nm-xeon-shipments-stall-during-largest-shortage-in-memory",
    "domain": "AI 算力 / 半导体",
    "title": "Deadly Intel Fab 28 explosion causes two-week shutdown, to cost $600 million and severely disrupt server chip manufacturing for six months",
    "url": "https://www.tomshardware.com/pc-components/cpus/deadly-intel-fab-28-explosion-causes-two-week-shutdown-to-cost-usd600-million-and-severely-disrupt-server-chip-manufacturing-for-six-months-10nm-xeon-shipments-stall-during-largest-shortage-in-memory",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T09:30:00+00:00",
    "summary": "A two-week shutdown of Intel's Fab 28 in Israel will affect server CPU shipments for two consecutive quarters."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-confirms-nova-lake-will-use-advanced-18a-p-node-more-details-at-ces-company-says-its-taking-panther-lake-capacity-offline-to-build-more-granite-rapids-data-center-cpus",
    "domain": "AI 算力 / 半导体",
    "title": "Intel confirms Nova Lake CPUs will use advanced 18A-P node, more details at CES",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-confirms-nova-lake-will-use-advanced-18a-p-node-more-details-at-ces-company-says-its-taking-panther-lake-capacity-offline-to-build-more-granite-rapids-data-center-cpus",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T21:55:48+00:00",
    "summary": "Intel's next-gen Nova Lake desktop processors will be the first client product to use Intel's enhanced 18A-P node, CEO Lip-Bu Tan confirmed in the company's Q3 2026 earnings call."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/elon-musks-spacex-buying-out-418-homes-near-flagship-ai-data-center-but-only-if-they-drop-participation-in-lawsuit-report-claims-the-company-is-targeting-an-entire-neighborhood-but-will-only-buy-from-people-who-dont-pursue-noise-pollution-complaints",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk's SpaceX buying out 418 homes near flagship AI data center, but only if they drop participation in lawsuit",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/elon-musks-spacex-buying-out-418-homes-near-flagship-ai-data-center-but-only-if-they-drop-participation-in-lawsuit-report-claims-the-company-is-targeting-an-entire-neighborhood-but-will-only-buy-from-people-who-dont-pursue-noise-pollution-complaints",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T15:40:20+00:00",
    "summary": "The properties will supposedly house SpaceXSI staff while also giving a chance to those who don't want to live near the data center to sell their homes."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ai-demand-triggers-massive-pcb-shortage-for-pc-makers-as-order-books-full-until-2030-lead-times-stretch-to-30-months-as-material-costs-surge-12x",
    "domain": "AI 算力 / 半导体",
    "title": "AI demand triggers massive PCB shortage for PC makers as order books full until 2030",
    "url": "https://www.tomshardware.com/pc-components/ai-demand-triggers-massive-pcb-shortage-for-pc-makers-as-order-books-full-until-2030-lead-times-stretch-to-30-months-as-material-costs-surge-12x",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T15:25:25+00:00",
    "summary": "The AI industry continues to gobble up manufacturing resources that were once dedicated to serving PC, smart device, and gadget makers. Inevitably, the PCB industry has started to feel its effects."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/us-data-centers-could-wipe-out-15-years-worth-of-progress-in-greenhouse-gas-emissions-report-claims-buildouts-could-emit-as-much-carbon-dioxide-as-all-of-mexico",
    "domain": "AI 算力 / 半导体",
    "title": "US data centers could wipe out 15 years' worth of progress in greenhouse gas emissions, report claims",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/us-data-centers-could-wipe-out-15-years-worth-of-progress-in-greenhouse-gas-emissions-report-claims-buildouts-could-emit-as-much-carbon-dioxide-as-all-of-mexico",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T14:34:54+00:00",
    "summary": "The Sierra Club, one of the oldest environmental preservation organizations in the U.S., has now put forth an estimate that by 2030, U.S. data center buildouts will be outputting as much carbon dioxid"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-geforce-rtx-5080-prices-hit-usd2-000-costing-more-than-the-rtx-5090-did-at-launch-and-with-limited-stock-available-original-usd999-msrp-long-forgotten-with-prices-now-2-3x-higher",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia GeForce RTX 5080 prices hit $2,000, costing more than the RTX 5090 did at launch and with limited stock available",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-geforce-rtx-5080-prices-hit-usd2-000-costing-more-than-the-rtx-5090-did-at-launch-and-with-limited-stock-available-original-usd999-msrp-long-forgotten-with-prices-now-2-3x-higher",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T14:21:59+00:00",
    "summary": "It costs just as much to buy an Nvidia GeForce RTX 5080 right now as the launch price for the RTX 5090, with prices now at least two times higher for this high spec GPU."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/hyperx-omen-35l-review",
    "domain": "AI 算力 / 半导体",
    "title": "HyperX Omen 35L review: A polished gaming PC for deep pockets",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/hyperx-omen-35l-review",
    "source": "Charles Jefferies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T14:00:00+00:00",
    "summary": "Premium styling, quiet operation, and impressive performance elevates the HyperX Omen 35L into competition with the best the market has to offer. But whether it's worth the money depends on which conf"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/nvidia-ceo-jensen-huang-may-have-been-the-target-of-a-spy-plot-through-chinese-intelligence-asset-report-claims-exec-from-firm-under-investigation-for-smuggling-banned-ai-chips-to-china-accused-of-being-a-spy-was-also-feeding-information-to-beijing",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang may have been the target of a spy plot through 'Chinese intelligence asset,' report claims",
    "url": "https://www.tomshardware.com/tech-industry/policy/nvidia-ceo-jensen-huang-may-have-been-the-target-of-a-spy-plot-through-chinese-intelligence-asset-report-claims-exec-from-firm-under-investigation-for-smuggling-banned-ai-chips-to-china-accused-of-being-a-spy-was-also-feeding-information-to-beijing",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T13:04:23+00:00",
    "summary": "Sources say that Alice Huang, a senior executive at an Nvidia cloud partner who has close ties with Jensen Huang, is suspected of passing information to Beijing."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/dept-of-justice-reportedly-probes-nvidia-over-usd13-billion-hugging-face-ai-platform-acquisition-concerns-raised-over-competition-in-ai-and-pressure-on-customers",
    "domain": "AI 算力 / 半导体",
    "title": "Dept of Justice reportedly probes Nvidia over $13 billion Hugging Face AI platform acquisition",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/dept-of-justice-reportedly-probes-nvidia-over-usd13-billion-hugging-face-ai-platform-acquisition-concerns-raised-over-competition-in-ai-and-pressure-on-customers",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T12:49:19+00:00",
    "summary": "Nvidia's near $13 billion buyout of Hugging Face has come under scrutiny over concerns that it will impact competition in the AI space."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/tech-whizzs-internet-accessible-synology-nas-gets-bit-by-ransomware-attack-from-18-month-old-remote-code-execution-flaw-security-updates-neglected-in-a-series-of-catastrophic-errors",
    "domain": "AI 算力 / 半导体",
    "title": "Tech whiz's internet-accessible Synology NAS gets bit by ransomware attack from 18-month-old remote code execution flaw",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/tech-whizzs-internet-accessible-synology-nas-gets-bit-by-ransomware-attack-from-18-month-old-remote-code-execution-flaw-security-updates-neglected-in-a-series-of-catastrophic-errors",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T12:41:14+00:00",
    "summary": "Tech whizz' internet-accessible Synology NAS gets bit by transomware attack — security updates 18 months out of date in a series of catastrophic errors"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/our-first-step-at-defining-a-cpu-benchmark-for-agentic-ai-how-we-can-measure-throughput-of-agentic-ai-workloads-without-any-gpu-involved",
    "domain": "AI 算力 / 半导体",
    "title": "Our first step at defining a CPU benchmark for agentic AI",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/our-first-step-at-defining-a-cpu-benchmark-for-agentic-ai-how-we-can-measure-throughput-of-agentic-ai-workloads-without-any-gpu-involved",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T12:20:00+00:00",
    "summary": "Over the past six months, CPUs have taken center stage as agentic AI workloads evolve. Here’s our first attempt at trying to measure CPU performance when running agentic workloads."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/score-a-huge-usd1-250-saving-on-this-alienware-gaming-pc-with-an-rtx-5070-ti-and-32gb-ddr5-right-now-big-newegg-price-drop-means-you-can-grab-this-4k-ready-rig-with-a-24-core-intel-cpu-and-1tb-ssd-for-usd2-599-99",
    "domain": "AI 算力 / 半导体",
    "title": "Score a huge $1,250 saving on this Alienware gaming PC with an RTX 5070 Ti and 32GB DDR5 right now",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/score-a-huge-usd1-250-saving-on-this-alienware-gaming-pc-with-an-rtx-5070-ti-and-32gb-ddr5-right-now-big-newegg-price-drop-means-you-can-grab-this-4k-ready-rig-with-a-24-core-intel-cpu-and-1tb-ssd-for-usd2-599-99",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T11:55:45+00:00",
    "summary": "You can save $1,250 on this Alienware Aurora gaming PC with an RTX 5070 Ti and 32GB of DDR5 RAM, now priced at just $2,599.99."
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
    "source": "AJ Kourabi",
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
    "source": "Ivan Chiam",
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
    "source": "Jeff Koch",
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
    "source": "Myron Xie",
    "platform": "rss",
    "points": null,
    "published_at": "2025-09-03T20:55:46+00:00",
    "summary": "Two-and-a-half years ago, we flagged a looming “cloud crisis” at AWS. Today, the evidence has mounted. AWS is the crown jewel of the Amazon empire, generating ~60% of group profits, and dominating the"
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
    "points": 1041,
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
    "points": 1011,
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
    "id": "hn:50288019",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon is the new #1 on the Artificial Analysis Intelligence Index v5",
    "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1",
    "source": "theHocineSaad",
    "platform": "hackernews",
    "points": 336,
    "published_at": "2026-10-29T12:41:56+00:00",
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
    "id": "hn:50299212",
    "domain": "大厂 AI 动态",
    "title": "AGI Economics: Coordination vs. Competence",
    "url": "https://institute.deepmind.com/essays/the-economics-of-intelligence/",
    "source": "simonpure",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-10-30T02:36:33+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/1023974/apple-intelligence-china-ios-27-3",
    "domain": "大厂 AI 动态",
    "title": "Apple Intelligence is finally coming to China with iOS 27.3",
    "url": "https://www.theverge.com/tech/1023974/apple-intelligence-china-ios-27-3",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T22:32:53+00:00",
    "summary": "Apple will launch Apple Intelligence in China with iOS 27.3, the company announced on its Chinese newsroom website, as reported by MacRumors. The Apple Intelligence features will be available first in"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1023649/akai-mpc-sample-key-exclusive",
    "domain": "大厂 AI 动态",
    "title": "Exclusive details about Akai’s MPC Sample Key",
    "url": "https://www.theverge.com/gadgets/1023649/akai-mpc-sample-key-exclusive",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T21:01:32+00:00",
    "summary": "Akai teased its new MPC Sample Key on Instagram earlier this week, and said it plans to open-source its software so the modding community can hack it to their hearts' delight. While there's no word ye"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1023820/sam-altman-ram-shortage-cloud-servers",
    "domain": "大厂 AI 动态",
    "title": "Sam Altman says it’s better for RAM to be in a data center than on your desk",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1023820/sam-altman-ram-shortage-cloud-servers",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T20:48:43+00:00",
    "summary": "Asked about supply chain shortages, like the ongoing RAM shortage, OpenAI CEO Sam Altman said in an interview that it's \"terrible\" to have RAM in personal PCs instead of data centers. During his appea"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1023763/openai-google-microsoft-ai-scraping-standard-opt-out",
    "domain": "大厂 AI 动态",
    "title": "The biggest names in AI are backing a new way to opt out of scraping",
    "url": "https://www.theverge.com/tech/1023763/openai-google-microsoft-ai-scraping-standard-opt-out",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T20:26:10+00:00",
    "summary": "OpenAI, Google, Microsoft, and Anthropic say they will adopt a new standard that publishers can use to opt out of being scraped by AI, as reported earlier by Search Engine Roundtable. With this contro"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1023528/google-project-suncatcher-ai-satellite-transmission",
    "domain": "大厂 AI 动态",
    "title": "Google&#8217;s satellite AI server transmits its first response to Earth",
    "url": "https://www.theverge.com/tech/1023528/google-project-suncatcher-ai-satellite-transmission",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T18:21:38+00:00",
    "summary": "Google's AI chip-equipped satellite has generated its first response from space. In a blog post on Friday, Google says it successfully booted up the satellite's Tensor Processing Units (TPUs), allowin"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1023440/starbucks-ai-personalized-menu-drive-thru",
    "domain": "大厂 AI 动态",
    "title": "Starbucks wants to use AI to show you a ‘personalized digital menu’ at the drive-thru",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1023440/starbucks-ai-personalized-menu-drive-thru",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T17:38:04+00:00",
    "summary": "Starbucks could eventually show you a personalized digital menu when you pull up to the drive-thru. During an earnings call on Thursday, Starbucks CEO Brian Niccol said the company is going to explore"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/1023194/the-delightfully-messy-state-of-apple-gadgets",
    "domain": "大厂 AI 动态",
    "title": "The delightfully messy state of Apple gadgets",
    "url": "https://www.theverge.com/podcast/1023194/the-delightfully-messy-state-of-apple-gadgets",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T17:25:20+00:00",
    "summary": "The iPhone has more screens! The MacBook has a touchscreen! The HomeView does CarPlay apps! For the first time in a long time, Apple is in a period of unabashed gadget experimentation, and while the f"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1023143/rivian-autonomy-point-to-point-robotaxi-q3-2026",
    "domain": "大厂 AI 动态",
    "title": "Rivian’s autonomy gamble faces its first real test",
    "url": "https://www.theverge.com/transportation/1023143/rivian-autonomy-point-to-point-robotaxi-q3-2026",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T17:16:09+00:00",
    "summary": "During an hourlong earnings call last night, Rivian CEO RJ Scaringe spent less time talking about the production ramp of the all-important R2 SUV than he did hyping the company's still-unproven autono"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1022794/vizio-mini-led-quantum-tv-65-inch-walmart-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Vizio’s discounted Mini LED TV lets you skip the sign-ups and smarts",
    "url": "https://www.theverge.com/gadgets/1022794/vizio-mini-led-quantum-tv-65-inch-walmart-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T17:01:07+00:00",
    "summary": "Modern smart TVs let you skip the streaming device, which is convenient, but they also come with their own issues, including privacy concerns and frequent updates. The Vizio Mini LED Quantum TV lets y"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1022819/google-nest-learning-thermostat-4th-gen-casio-ws-b1000-watch-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Google’s latest Nest Learning Thermostat is $60 off just in time for sweater weather",
    "url": "https://www.theverge.com/gadgets/1022819/google-nest-learning-thermostat-4th-gen-casio-ws-b1000-watch-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T15:29:02+00:00",
    "summary": "As the weather cools, it may be worth investing in a smart thermostat to help lower your energy bills. Right now, Google&#8217;s fourth-gen Nest Learning Thermostat is on sale in all three colors for "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/pile-ins-payouts-and-pacing-pressure-the-investors-behind-the-vcs-open-up/",
    "domain": "大厂 AI 动态",
    "title": "Pile-ins, payouts, and pacing pressure: the investors behind the VCs open up",
    "url": "https://techcrunch.com/2026/10/30/pile-ins-payouts-and-pacing-pressure-the-investors-behind-the-vcs-open-up/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T04:16:50+00:00",
    "summary": "The money behind the money is thrilled, mostly."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/nvidia-weighs-playing-the-cosigner-for-nscales-ai-data-center-in-west-virginia/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia weighs playing the cosigner for Nscale’s AI data center in West Virginia",
    "url": "https://techcrunch.com/2026/10/30/nvidia-weighs-playing-the-cosigner-for-nscales-ai-data-center-in-west-virginia/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T01:20:05+00:00",
    "summary": "When investors get nervous about AI spending, it helps to have the chipmaker that sells the chips offer to cosign the loan."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/salesforces-ma-spree-continues-with-a-reported-375m-deal-for-defense-tech-startup-rune/",
    "domain": "大厂 AI 动态",
    "title": "Salesforce’s M&A spree continues with a reported $375M deal for defense tech startup Rune",
    "url": "https://techcrunch.com/2026/10/30/salesforces-ma-spree-continues-with-a-reported-375m-deal-for-defense-tech-startup-rune/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T23:21:23+00:00",
    "summary": "The AI logistics startup will bolster the CRM giant's Missionforce defense platform."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/ollie-a-privacy-focused-ai-assistant-is-shutting-down/",
    "domain": "大厂 AI 动态",
    "title": "Ollie, a privacy-focused AI assistant, is shutting down",
    "url": "https://techcrunch.com/2026/10/30/ollie-a-privacy-focused-ai-assistant-is-shutting-down/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T22:56:13+00:00",
    "summary": "As an increasing number of AI assistants flood the market, the founder of Ollie, an assistant that respected its users' privacy, says it will be shutting down in a week."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/intels-stock-crashes-knocking-12b-from-governments-stake/",
    "domain": "大厂 AI 动态",
    "title": "Intel’s stock crashes, knocking $12B from government’s stake",
    "url": "https://techcrunch.com/2026/10/30/intels-stock-crashes-knocking-12b-from-governments-stake/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T21:54:34+00:00",
    "summary": "Intel is being hurt by PC sales as the AI industry gobbles memory and other components causing PC prices to rise."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/applebees-exposed-customers-personal-data-after-leaving-database-password-in-app/",
    "domain": "大厂 AI 动态",
    "title": "Applebee’s exposed customers’ personal data after leaving database password in app",
    "url": "https://techcrunch.com/2026/10/30/applebees-exposed-customers-personal-data-after-leaving-database-password-in-app/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T21:48:53+00:00",
    "summary": "EXCLUSIVE: A security researcher discovered the hardcoded credential in Applebee's app, allowing unrestricted access to customers' personal data."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/last-minute-halloween-costumes-for-tech-nerds/",
    "domain": "大厂 AI 动态",
    "title": "Last-minute Halloween costumes for tech nerds",
    "url": "https://techcrunch.com/2026/10/30/last-minute-halloween-costumes-for-tech-nerds/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T21:26:59+00:00",
    "summary": "No Halloween costume? Just be a deceptively cute AI agent icon, a PHP vulnerability, or sleepy time Bryan Johnson."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/cracks-are-emerging-in-the-ai-spending-boom/",
    "domain": "大厂 AI 动态",
    "title": "Cracks are emerging in the AI spending boom",
    "url": "https://techcrunch.com/2026/10/30/cracks-are-emerging-in-the-ai-spending-boom/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T21:17:40+00:00",
    "summary": "Big Tech is pouring billions into AI infrastructure, but mounting debt, negative cash flow, and growing investor skepticism are raising questions about the sustainability of the AI spending boom."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/ai-law-firm-crosby-bids-on-disintegrating-famed-firm-weil-gotshal/",
    "domain": "大厂 AI 动态",
    "title": "AI law firm Crosby bids on disintegrating, famed firm Weil Gotshal",
    "url": "https://techcrunch.com/2026/10/30/ai-law-firm-crosby-bids-on-disintegrating-famed-firm-weil-gotshal/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T19:55:13+00:00",
    "summary": "Like a real-life episode of \"Suits,\" the demise of famed white-shoe Wall Street law firm Weil, Gotshal &#038; Manges has been the talk of the legal industry. And now an AI firm has entered the picture"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/satlyt-takes-another-step-toward-turning-satellites-into-space-data-centers/",
    "domain": "大厂 AI 动态",
    "title": "Satlyt takes another step toward turning satellites into space data centers",
    "url": "https://techcrunch.com/2026/10/30/satlyt-takes-another-step-toward-turning-satellites-into-space-data-centers/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T18:01:24+00:00",
    "summary": "Satlyt ran a successful test this month bringing it closer to turning spacecraft, starting with satellites, into virtual data centers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/zests-new-ai-agent-finds-restaurants-and-books-reservations-over-text/",
    "domain": "大厂 AI 动态",
    "title": "Zest’s new AI agent finds restaurants and books reservations over text",
    "url": "https://techcrunch.com/2026/10/30/zests-new-ai-agent-finds-restaurants-and-books-reservations-over-text/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T17:47:12+00:00",
    "summary": "Can't agree on where to eat? Zest's AI concierge can combine everyone's tastes, put restaurant options to a vote, and make the reservation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/googles-first-data-center-satellite-is-online-and-writing-poetry/",
    "domain": "大厂 AI 动态",
    "title": "Google’s first data center satellite is online and writing poetry",
    "url": "https://techcrunch.com/2026/10/30/googles-first-data-center-satellite-is-online-and-writing-poetry/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T17:00:00+00:00",
    "summary": "The first TPU in space is running a Google DeepMind Gemma 4 model and writing cheesy poetry."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/theranos-whistleblower-tyler-shultz-warns-that-the-ai-boom-is-a-great-opportunity-to-go-deceive-people/",
    "domain": "大厂 AI 动态",
    "title": "Theranos whistleblower Tyler Shultz warns that the AI boom is ‘a great opportunity to go deceive people’",
    "url": "https://techcrunch.com/2026/10/30/theranos-whistleblower-tyler-shultz-warns-that-the-ai-boom-is-a-great-opportunity-to-go-deceive-people/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T16:03:45+00:00",
    "summary": "The cautionary Theranos tale takes on a new significance in the AI era, when companies that have never turned a profit are raising capital at trillion-dollar valuations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/north-korean-hackers-blamed-for-stealing-record-6-3b-in-binance-breach/",
    "domain": "大厂 AI 动态",
    "title": "North Korean hackers blamed for stealing record $6.3B in Binance breach",
    "url": "https://techcrunch.com/2026/10/30/north-korean-hackers-blamed-for-stealing-record-6-3b-in-binance-breach/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T14:00:25+00:00",
    "summary": "Hackers working for North Korea are suspected of hacking a Binance employee's laptop, which allowed the theft of billions in crypto."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/skip-the-small-talk-make-game-changing-connections-at-techcrunch-founder-summit-with-braindate/",
    "domain": "大厂 AI 动态",
    "title": "Skip the small talk: Make game-changing connections at TechCrunch Founder Summit with Braindate",
    "url": "https://techcrunch.com/2026/10/30/skip-the-small-talk-make-game-changing-connections-at-techcrunch-founder-summit-with-braindate/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T14:00:00+00:00",
    "summary": "At TechCrunch Founder Summit 2026, happening November 4 at SoWa Power Station in Boston, networking powered by Braindate is designed to make those conversations easier to find, whether they are in 1:1"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/doordash-said-its-only-received-several-hundred-orders-from-ai-agents/",
    "domain": "大厂 AI 动态",
    "title": "DoorDash said it’s only received ‘several hundred’ orders from AI agents",
    "url": "https://techcrunch.com/2026/10/30/doordash-said-its-only-received-several-hundred-orders-from-ai-agents/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T13:54:25+00:00",
    "summary": "DoorDash said that it is open to working with third-party agent makers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/can-ai-data-centers-be-mass-produced-like-cars-and-online-in-48-hours-this-startup-aims-to-find-out/",
    "domain": "大厂 AI 动态",
    "title": "Can AI data centers be mass-produced like cars? This startup aims to find out",
    "url": "https://techcrunch.com/2026/10/30/can-ai-data-centers-be-mass-produced-like-cars-and-online-in-48-hours-this-startup-aims-to-find-out/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T13:00:00+00:00",
    "summary": "Runware is building a factory to turn out prefabricated AI data centers on an assembly line. The real test will be whether it can deliver at that scale."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/5-days-left-your-last-chance-to-connect-scale-and-save-at-techcrunch-founder-summit-2026/",
    "domain": "大厂 AI 动态",
    "title": "5 days left: Your last chance to connect, scale, and save at TechCrunch Founder Summit 2026",
    "url": "https://techcrunch.com/2026/10/30/5-days-left-your-last-chance-to-connect-scale-and-save-at-techcrunch-founder-summit-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T13:00:00+00:00",
    "summary": "5 days to save up to $100, plus a second pass for free to TechCrunch Founder Summit 2026 in Boston on November 4. Register now."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/30/waymos-next-robotaxi-will-be-a-toyota-bz4x-destined-for-japan-and-the-uk/",
    "domain": "大厂 AI 动态",
    "title": "Waymo taps Toyota to supply robotaxis for Japan and the UK",
    "url": "https://techcrunch.com/2026/10/30/waymos-next-robotaxi-will-be-a-toyota-bz4x-destined-for-japan-and-the-uk/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T07:01:00+00:00",
    "summary": "Waymo will begin testing self-driving versions of Toyota's electric bZ4X vehicles in Japan next year as part of a broader partnership with the automaker."
  },
  {
    "id": "rss:https://stratechery.com/2026/at-long-last/",
    "domain": "大厂 AI 动态",
    "title": "2026.44: At Long Last…",
    "url": "https://stratechery.com/2026/at-long-last/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of October 26, 2026 including Anthropic numbers, the end of the Internet as we know it, and autocracies then and now."
  },
  {
    "id": "rss:https://stratechery.com/2026/sharp-tech-on-video-anthropics-s-1-and-what-it-means-for-meta-and-muse-you-can-see-everything-and-brewers/",
    "domain": "大厂 AI 动态",
    "title": "Sharp Tech on Video: Anthropic’s S-1 and What It Means for Meta and Muse, You Can See Everything, and Brewers!",
    "url": "https://stratechery.com/2026/sharp-tech-on-video-anthropics-s-1-and-what-it-means-for-meta-and-muse-you-can-see-everything-and-brewers/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T10:00:00+00:00",
    "summary": "Sharp Tech is, for the first time, available on video. You have three ways to consume it: YouTube, Spotify, and here on Stratechery."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-palantir-cto-shyam-sankar-about-the-ai-religious-war/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with Palantir CTO Shyam Sankar About the AI Religious War",
    "url": "https://stratechery.com/2026/an-interview-with-palantir-cto-shyam-sankar-about-the-ai-religious-war/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-29T10:00:00+00:00",
    "summary": "An interview with Palantir CTO Shyam Sankar about AI diffusion and safety, forward-deployed engineer, and what the battle in tech is actually about."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/10/think-you-can-save-the-hubble-space-telescope-nasa-wants-to-know/",
    "domain": "大厂 AI 动态",
    "title": "Once again, NASA is asking for ideas to rescue Hubble from certain death",
    "url": "https://arstechnica.com/space/2026/10/think-you-can-save-the-hubble-space-telescope-nasa-wants-to-know/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-31T00:07:22+00:00",
    "summary": "The space agency solicited ideas for reboosting Hubble four years ago, but they didn't go anywhere."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/10/flesh-eating-screwworms-are-feasting-on-pets-4-dogs-and-cat-attacked-this-week/",
    "domain": "大厂 AI 动态",
    "title": "Flesh-eating screwworms spread to third state and are attacking pets",
    "url": "https://arstechnica.com/health/2026/10/flesh-eating-screwworms-are-feasting-on-pets-4-dogs-and-cat-attacked-this-week/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T22:36:41+00:00",
    "summary": "USDA has identified 74 animal cases in US since parasitic flies invaded in June."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/10/oh-captain-our-captain-ars-staff-remembers-patrick-stewart/",
    "domain": "大厂 AI 动态",
    "title": "Oh captain, our captain: Ars staff remembers Patrick Stewart",
    "url": "https://arstechnica.com/culture/2026/10/oh-captain-our-captain-ars-staff-remembers-patrick-stewart/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T22:21:05+00:00",
    "summary": "\"For huge numbers of people, I will always be Jean-Luc Picard. ... We created an admirable individual.\""
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/united-airlines-ceo-doubts-supersonic-airliner-from-boom-will-be-ready-by-2029/",
    "domain": "大厂 AI 动态",
    "title": "Supersonic airliner in doubt as company shifts to powering AI data centers",
    "url": "https://arstechnica.com/gadgets/2026/10/united-airlines-ceo-doubts-supersonic-airliner-from-boom-will-be-ready-by-2029/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T21:41:54+00:00",
    "summary": "Boom’s airliner may be delayed, and its data center power business lost a customer."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/10/anthropic-vs-code-extension-on-cursor-backdoored-for-nearly-12-hours/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic VS code extension on Cursor backdoored for nearly 12 hours",
    "url": "https://arstechnica.com/security/2026/10/anthropic-vs-code-extension-on-cursor-backdoored-for-nearly-12-hours/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T21:09:54+00:00",
    "summary": "It's still unknown how attackers got access to Anthropic's verified Cursor account."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/10/dartmouths-provost-warned-us-about-ai-cheating-but-his-own-ai-use-cost-him-his-job/",
    "domain": "大厂 AI 动态",
    "title": "Dartmouth's provost warned us about AI cheating—but his own AI use cost him his job",
    "url": "https://arstechnica.com/tech-policy/2026/10/dartmouths-provost-warned-us-about-ai-cheating-but-his-own-ai-use-cost-him-his-job/",
    "source": "Nate Anderson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T20:40:13+00:00",
    "summary": "People who love AI don't always love telling others they used it."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/10/over-25-of-people-lie-to-get-antibiotics-and-their-lies-arent-even-good/",
    "domain": "大厂 AI 动态",
    "title": "Over 25% of people lie to get antibiotics—and their lies aren't even good",
    "url": "https://arstechnica.com/health/2026/10/over-25-of-people-lie-to-get-antibiotics-and-their-lies-arent-even-good/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T20:17:50+00:00",
    "summary": "Faked symptoms still point to infections that antibiotics don't treat."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/10/doordash-says-outside-ai-agents-have-only-led-to-hundreds-of-orders-so-far/",
    "domain": "大厂 AI 动态",
    "title": "Basically no one is using AI agents for their DoorDash orders",
    "url": "https://arstechnica.com/ai/2026/10/doordash-says-outside-ai-agents-have-only-led-to-hundreds-of-orders-so-far/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T19:30:52+00:00",
    "summary": "But it's still early days for the relatively new e-commerce use case."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/rare-meteorite-from-mars-gives-us-a-view-into-its-ancient-crust/",
    "domain": "大厂 AI 动态",
    "title": "Rare meteorite from Mars gives us a view into its ancient crust",
    "url": "https://arstechnica.com/science/2026/10/rare-meteorite-from-mars-gives-us-a-view-into-its-ancient-crust/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T18:13:42+00:00",
    "summary": "A meteorite found in the Sahara is a rare piece of Mars' ancient crust."
  },
  {
    "id": "hn:50306008",
    "domain": "股票",
    "title": "US tech stocks see sharp falls over AI cost fears",
    "url": "https://www.bbc.co.uk/news/articles/cvwy72e0n72yo",
    "source": "mindracer",
    "platform": "hackernews",
    "points": 254,
    "published_at": "2026-10-30T16:13:02+00:00",
    "summary": ""
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
    "points": 80,
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
    "id": "hn:50311339",
    "domain": "股票",
    "title": "Federal Bureau of Prisons employees serve as election monitors at polling sites",
    "url": "https://www.corrections1.com/federal-prison/bop-employees-to-serve-as-election-monitors-at-polling-sites-doj-filing-says",
    "source": "MadrasTh0rn",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-30T23:12:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50297025",
    "domain": "股票",
    "title": "Intel stock plunges after posting disappointing Q4 outlook",
    "url": "https://finance.yahoo.com/video/intel-stock-plunges-after-posting-disappointing-q4-outlook-200731652.html",
    "source": "baal80spam",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-29T22:21:29+00:00",
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
    "id": "hn:50265525",
    "domain": "股票",
    "title": "In China, the AI bubble has burst",
    "url": "https://finance.yahoo.com/markets/stocks/articles/analysis-china-ai-bubble-already-120038616.html",
    "source": "smurda",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-10-27T20:44:20+00:00",
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
    "id": "hn:50251762",
    "domain": "股票",
    "title": "Anthropic Is the Most Ridiculous IPO of 2026 [pdf]",
    "url": "https://www.newconstructs.com/wp-content/uploads/2026/10/Anthropic-Is-The-Most-Ridiculous-IPO-of-2026.pdf",
    "source": "simonebrunozzi",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-26T22:06:15+00:00",
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
    "id": "hn:50305573",
    "domain": "金融",
    "title": "The federated code forge",
    "url": "https://tangled.org/blog/forge/",
    "source": "zlliang",
    "platform": "hackernews",
    "points": 284,
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
    "id": "hn:50260526",
    "domain": "金融",
    "title": "A $300B 'Debt Wall' Is Looming over Private-Equity Backed Companies",
    "url": "https://www.wsj.com/finance/investing/a-300-billion-debt-wall-is-looming-over-private-equity-backed-companies-d6359497",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 177,
    "published_at": "2026-10-27T15:09:27+00:00",
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
    "points": 95,
    "published_at": "2026-10-28T14:54:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:50291902",
    "domain": "金融",
    "title": "Alphabet heads for a $500B drop in market value, biggest in its history",
    "url": "https://finance.yahoo.com/markets/article/alphabet-heads-for-a-500-billion-drop-in-market-value-the-biggest-in-its-history-134824763.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 60,
    "published_at": "2026-10-29T16:39:55+00:00",
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
    "id": "hn:50278678",
    "domain": "金融",
    "title": "Show HN: A proof-of-concept formalization of the IRS federal tax forms",
    "url": "https://github.com/emmilco/us-tax-model",
    "source": "RGS1811",
    "platform": "hackernews",
    "points": 80,
    "published_at": "2026-10-28T18:30:53+00:00",
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
