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

- 今日日期：`2026-07-28`
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
  "date": "2026-07-28",
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
    "id": "bvid:BV1DfrdByE2H",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！Agentic AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av115897075242856",
    "source": "吴恩达Agent",
    "platform": "bilibili",
    "points": 3946986,
    "published_at": "2026-01-15T03:56:12+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1617724,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1286220,
    "published_at": "2026-07-05T02:00:00+00:00",
    "summary": "用不上codex的朋友们！新的国产Agent直接上手，来跑通8大用法～\n感谢朋友们的三连+关注～"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 1003153,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 980610,
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
    "points": 965232,
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
    "points": 865823,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 428927,
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
    "points": 418711,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 405595,
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
    "points": 344503,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 249714,
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
    "points": 207686,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 184724,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 177964,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 149431,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 117461,
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
    "points": 109105,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 99658,
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
    "points": 92796,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1GRKJ6fEgn",
    "domain": "AI",
    "title": "Kimi K3编程能力炸裂！在Claude Code中全方位实测代码能力，能否超越Fable 5和GPT-5.6l？结果远超我的预期！国产模型跻身世界第一梯队！",
    "url": "http://www.bilibili.com/video/av116934511239163",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 85713,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73904,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53380,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47500,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 44294,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 39270,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 37354,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1cCj2ztEf5",
    "domain": "AI",
    "title": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%",
    "url": "http://www.bilibili.com/video/av114574527307727",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 35016,
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
    "points": 33935,
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
    "points": 29505,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 25707,
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
    "points": 22658,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1w9Nc69EXP",
    "domain": "AI",
    "title": "[电赛AIskill]写0行代码/纯agent速通2024年电赛H题——思路&amp;代码分享",
    "url": "http://www.bilibili.com/video/av116900721922369",
    "source": "3545D",
    "platform": "bilibili",
    "points": 20813,
    "published_at": "2026-07-11T09:56:10+00:00",
    "summary": "使用mspm0-skill速通2024年电赛h题教程/思路，视频内使用的是codex桌面端（现在叫ChatGPT桌面端），天猛星开发板+ccs环境编译+OpenOCD/DAPLink烧录，视频内skill支持各种开发板/工具链/Agent/烧录器/IDE等，详见https://github.com/mc3545dada/mspm0-skill，感兴趣的欢迎交流/Issue/PR/star等，谢谢a"
  },
  {
    "id": "bvid:BV16ggC6DEZK",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116963049212769",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 19056,
    "published_at": "2026-07-22T10:10:42+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1vDKh6cE1E",
    "domain": "AI",
    "title": "【全500集】目前B站最全最细的AI大模型零基础全套教程，5天从入门到精通AI大模型，学完即可就业！看完这一套大模型教程就够了！",
    "url": "http://www.bilibili.com/video/av116957412069393",
    "source": "AI智能应用-",
    "platform": "bilibili",
    "points": 18497,
    "published_at": "2026-07-21T12:30:05+00:00",
    "summary": "【全500集】目前B站最全最细的AI大模型零基础全套教程，5天从入门到精通AI大模型，学完即可就业！看完这一套大模型教程就够了！"
  },
  {
    "id": "bvid:BV13sJcz9Egm",
    "domain": "AI",
    "title": "让AI替你打工！教你用Trae+MCP自动操作网页，采集数据，有手就能学会！mcp教程，mcp实战，mcp开发",
    "url": "http://www.bilibili.com/video/av114521544852773",
    "source": "大模型实战课程",
    "platform": "bilibili",
    "points": 17218,
    "published_at": "2025-05-17T05:36:05+00:00",
    "summary": "让AI替你打工！教你用Trae+MCP自动操作网页，采集数据，有手就能学会！mcp教程，mcp实战，mcp开发"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 16836,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 15721,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 14784,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1jZ5F6eEzQ",
    "domain": "AI",
    "title": "答应我，别再和AI一起拉屎了；Vibe Coding如何避免屎山",
    "url": "http://www.bilibili.com/video/av116677031236717",
    "source": "写代码小猴子Tong",
    "platform": "bilibili",
    "points": 14572,
    "published_at": "2026-06-01T23:00:00+00:00",
    "summary": "复杂度之战05：答应我，不要再和AI一起拉屎了；Vibe Coding如何避免写出屎山\n\n为什么你的项目越写越难改?\n为什么 AI 写的代码局部没有问题,合在一起就是一坨屎山?\n\n从一个最简单的数学事实讲起:软件复杂度的增长为啥会这么快。用一个圆的动画,直观演示&quot;解耦&quot;是如何降低屎山的规模的。\n\n本期内容: \n▸ 为什么屎山会膨胀得如此之快 \n▸ 一个圆讲清楚解耦的威力 \n▸ "
  },
  {
    "id": "bvid:BV1HFRgBvEVv",
    "domain": "AI",
    "title": "claude接入小米mimo模型基础教程（无claude安装教程）",
    "url": "http://www.bilibili.com/video/av116499343738499",
    "source": "栉旎",
    "platform": "bilibili",
    "points": 13503,
    "published_at": "2026-05-01T12:37:49+00:00",
    "summary": "claude接入小米mimo模型全流程，"
  },
  {
    "id": "bvid:BV1vLN769EJa",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！大模型入门到进阶，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116894866677118",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 12643,
    "published_at": "2026-07-10T09:04:48+00:00",
    "summary": "【代码已整理】\n无论你是从零开始开发项目，还是对现有代码进行现代化改造，本课程都能为你提供一套严谨的工作流程，让你按自己的方式构建软件。"
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "7月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "iwenwikii",
    "platform": "bilibili",
    "points": 11795,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "AI充值站：aipayok.com"
  },
  {
    "id": "bvid:BV1dsNv66E3Q",
    "domain": "AI",
    "title": "【Cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116922599344955",
    "source": "六月要癫",
    "platform": "bilibili",
    "points": 9304,
    "published_at": "2026-07-15T06:39:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 8774,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV1qNS8BNESd",
    "domain": "AI",
    "title": "AI黑客实战：Cloud Code自动化渗透测试Hack the Box",
    "url": "http://www.bilibili.com/video/av115652480209157",
    "source": "黑客酒吧",
    "platform": "bilibili",
    "points": 8745,
    "published_at": "2025-12-03T01:11:01+00:00",
    "summary": "Teja挑战AI极限，用Cloud Code CLI在Hack the Box上实现全自动渗透测试！视频展示如何配置AI代理，一键扫描、漏洞利用、权限提升，并自动生成详细渗透报告。亮点包括MCP集成实战、沙盒环境安全测试，以及AI在网络安全中的颠覆性应用。"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 7986,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV19GM36GEdo",
    "domain": "AI",
    "title": "2026最新版！上海交大【动手学大模型】全套教程，手把手带你零基础吃透大模型智能体！人工智能/具身智能/LLM/Agent/RAG/LangChain/模型微调",
    "url": "http://www.bilibili.com/video/av116883760092440",
    "source": "深度学习神经网络",
    "platform": "bilibili",
    "points": 7684,
    "published_at": "2026-07-08T11:24:05+00:00",
    "summary": "上海交大带你入门大模型智能体，一起学起来吧！"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 7007,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 6713,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "hn:49035303",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, Microsoft, Meta warn against overregulating open-weight models",
    "url": "https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 655,
    "published_at": "2026-07-24T13:32:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49034868",
    "domain": "AI 算力 / 半导体",
    "title": "Half-Life 2 running natively on HaikuOS",
    "url": "https://discuss.haiku-os.org/t/haiku-nvidia-porting-nvidia-driver-for-turing-gpus/16520?page=18",
    "source": "m0do1",
    "platform": "hackernews",
    "points": 338,
    "published_at": "2026-07-24T12:53:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49035751",
    "domain": "AI 算力 / 半导体",
    "title": "Open Weights and American AI Leadership [pdf]",
    "url": "https://images.nvidia.com/pdf/Open-Weights-and-American-AI-Leadership.pdf",
    "source": "lairv",
    "platform": "hackernews",
    "points": 112,
    "published_at": "2026-07-24T13:58:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49071512",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's $750B in Deals Reignite Circular AI Fears",
    "url": "https://www.bloomberg.com/news/articles/2026-07-27/nvidia-s-750-billion-deals-revive-fear-of-ai-circular-financing",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-07-27T16:02:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:48903715",
    "domain": "AI 算力 / 半导体",
    "title": "Alternative(s) to run CUDA on non-Nvidia hardware",
    "url": "https://www.hpcwire.com/2026/07/09/spectral-compute-aims-to-set-cuda-free-will-it-succeed/",
    "source": "alok-g",
    "platform": "hackernews",
    "points": 143,
    "published_at": "2026-07-14T08:24:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48971128",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia DGX Spark as a daily driver",
    "url": "https://daniel.lawrence.lu/blog/2026-07-15-dgx-spark-as-daily-driver/",
    "source": "plun9",
    "platform": "hackernews",
    "points": 102,
    "published_at": "2026-07-19T19:44:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:49070311",
    "domain": "AI 算力 / 半导体",
    "title": "Ilya Sutskever's SSI and Nvidia Announce Long-Term Strategic Partnership",
    "url": "https://nvidianews.nvidia.com/news/ilya-sutskevers-safe-superintelligence-inc-and-nvidia-announce-long-term-strategic-partnership",
    "source": "lanakei",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-07-27T14:33:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:49075171",
    "domain": "AI 算力 / 半导体",
    "title": "Sam Altman says we are in the singularity: 'This is the moment'",
    "url": "https://www.businessinsider.com/sam-altman-openai-the-singularity-agi-prediction-anthropic-nvidia-2026-7",
    "source": "doener",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-07-27T20:35:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:49069995",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia investing to 10x SSI compute in the next 12 months",
    "url": "https://twitter.com/ssi/status/2081732119194394763",
    "source": "primaprashant",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-27T14:11:31+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/warning-shots-fired-as-amd-announces-new-data-center-gpus-at-advancing-ai-event/",
    "domain": "AI 算力 / 半导体",
    "title": "Warning Shots Fired as AMD Announces New Data Center GPUs",
    "url": "https://www.eetimes.com/warning-shots-fired-as-amd-announces-new-data-center-gpus-at-advancing-ai-event/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T16:58:23+00:00",
    "summary": "Red team’s new Helios racks offer 30% more tokens per dollar than Nvidia. The post Warning Shots Fired as AMD Announces New Data Center GPUs appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/automotive-ethernet-and-time-sensitive-networking-tsn-for-next-generation-vehicles/",
    "domain": "AI 算力 / 半导体",
    "title": "Automotive Ethernet and Time Sensitive Networking (TSN) for Next Generation Vehicles",
    "url": "https://www.eetimes.com/automotive-ethernet-and-time-sensitive-networking-tsn-for-next-generation-vehicles/",
    "source": "eInfochips",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T15:59:39+00:00",
    "summary": "In this session, our expert will provide a practical overview of Automotive Ethernet, TSN, and much more. The post Automotive Ethernet and Time Sensitive Networking (TSN) for Next Generation Vehicles "
  },
  {
    "id": "rss:https://www.eetimes.com/bringing-inference-to-the-patient-systems-architecture-for-healthcare-edge-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Bringing Inference to the Patient: Systems Architecture for Healthcare Edge AI",
    "url": "https://www.eetimes.com/bringing-inference-to-the-patient-systems-architecture-for-healthcare-edge-ai/",
    "source": "Beenish Zia, Principal Engineer, Intel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T13:00:00+00:00",
    "summary": "Scaling healthcare AI effectively—starting with the right edge infrastructure. The post Bringing Inference to the Patient: Systems Architecture for Healthcare Edge AI appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/adaptive-hardware-could-change-how-ev-chargers-are-designed/",
    "domain": "AI 算力 / 半导体",
    "title": "Adaptive Hardware Could Change How EV Chargers Are Designed",
    "url": "https://www.eetimes.com/adaptive-hardware-could-change-how-ev-chargers-are-designed/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T13:00:00+00:00",
    "summary": "Vanix bets adaptive AMD hardware can make India’s EV chargers upgradeable, not disposable. The post Adaptive Hardware Could Change How EV Chargers Are Designed appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/cxmt-ipo-where-chinas-largest-dram-maker-stands/",
    "domain": "AI 算力 / 半导体",
    "title": "CXMT IPO: Where China’s Largest DRAM Maker Stands?",
    "url": "https://www.eetimes.com/cxmt-ipo-where-chinas-largest-dram-maker-stands/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T07:20:00+00:00",
    "summary": "CXMT eyes one of China’s largest semiconductor IPOs amid once-in-four-decades memory shortage. The post CXMT IPO: Where China’s Largest DRAM Maker Stands? appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/msi-and-colorful-raise-nvidia-rtx-50-series-prices-in-china-by-up-to-59-percent-across-the-entire-lineup-change-in-distributer-pricing-suggests-gpu-price-hikes-are-on-the-way",
    "domain": "AI 算力 / 半导体",
    "title": "MSI and Colorful raise Nvidia RTX 50-series prices in China by up to 59% across the entire lineup — change in distributer pricing suggests GPU price hikes are on the way",
    "url": "https://www.tomshardware.com/pc-components/gpus/msi-and-colorful-raise-nvidia-rtx-50-series-prices-in-china-by-up-to-59-percent-across-the-entire-lineup-change-in-distributer-pricing-suggests-gpu-price-hikes-are-on-the-way",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T19:47:49+00:00",
    "summary": "GPU prices seem to be on the rise once again with official distributor announcements in China hiking up the entire Blackwell lineup overnight. Compared to MSRP, we're witnessing a staggering bump of u"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-google-and-anthropic-absent-from-nvidia-led-open-secure-ai-alliance-30-companies-join-security-alliance-after-openai-agent-breach",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI, Google, and Anthropic absent from Nvidia-led Open Secure AI Alliance — 30+ companies join security alliance after OpenAI agent breach",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-google-and-anthropic-absent-from-nvidia-led-open-secure-ai-alliance-30-companies-join-security-alliance-after-openai-agent-breach",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T19:03:47+00:00",
    "summary": "Industry leading tech companies have formed an \"Open Secure AI Alliance\" that will build open-source models, agent harnesses, and cybersecurity tools, arguing that defenders need locally controlled AI"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-ai-releases-weights-for-kimi-k3-firing-a-shot-across-the-bow-of-openai-and-anthropic-open-weight-model-performs-almost-as-well-as-frontier-models-while-being-2-3x-easier-to-run",
    "domain": "AI 算力 / 半导体",
    "title": "Moonshot AI releases weights for Kimi-K3, firing a shot across the bow of OpenAI and Anthropic — open-weight model performs almost as well as frontier models while being 2-3x easier to run",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-ai-releases-weights-for-kimi-k3-firing-a-shot-across-the-bow-of-openai-and-anthropic-open-weight-model-performs-almost-as-well-as-frontier-models-while-being-2-3x-easier-to-run",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T18:40:58+00:00",
    "summary": "Moonshot AI has released the weights for its recent Kimi-K3 model, directly going against OpenAI and Anthropic."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/china-begins-mass-production-of-domestic-immersion-duv-lithography-machines",
    "domain": "AI 算力 / 半导体",
    "title": "China begins mass production of homegrown immersion chipmaking machines in major breakthrough, report claims — first DUV lithography units will be delivered this year to SMIC, Hua Hong, and CXMT",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/china-begins-mass-production-of-domestic-immersion-duv-lithography-machines",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T16:51:35+00:00",
    "summary": "A state-backed company in Shanghai has begun mass-producing immersion deep ultraviolet lithography machines and is due to deliver the first units this year."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/why-an-mmo-mouse-isnt-just-for-gaming-make-use-of-the-myriad-of-buttons-for-enhancing-your-productivity-workflows-in-popular-software-applications",
    "domain": "AI 算力 / 半导体",
    "title": "Why an MMO mouse isn’t just for gaming — make use of the myriad of buttons for enhancing your productivity workflows in popular software applications",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/why-an-mmo-mouse-isnt-just-for-gaming-make-use-of-the-myriad-of-buttons-for-enhancing-your-productivity-workflows-in-popular-software-applications",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T15:39:54+00:00",
    "summary": "MMO mice are designed with many buttons to make it easier to play games with lots of spells and abilities, but MMO mice are also fantastic for automating your productivity workflows."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/upgrading-an-msi-claw-8-ex-ai-handheld-gaming-pc-with-a-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Upgrading an MSI Claw 8 EX AI+ handheld gaming PC with a 2TB SSD",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/upgrading-an-msi-claw-8-ex-ai-handheld-gaming-pc-with-a-2tb-ssd",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T15:04:32+00:00",
    "summary": "I go through the steps of replacing the standard 1TB SSD in an MSI Claw 8 EX AI+ with a 2TB SSD."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-unveiled-its-iconic-core-2-duo-family-20-years-ago-legendary-chip-dethroned-amd-athlon-restoring-the-chipmakers-performance-lead",
    "domain": "AI 算力 / 半导体",
    "title": "Intel unveiled its iconic Core 2 Duo family 20 years ago — legendary chip dethroned AMD Athlon, restoring the chipmaker’s performance lead",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-unveiled-its-iconic-core-2-duo-family-20-years-ago-legendary-chip-dethroned-amd-athlon-restoring-the-chipmakers-performance-lead",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T15:01:11+00:00",
    "summary": "Today marks 20 years since the first raft of Intel Core 2 Duo processors, codename Conroe, was launched."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/framework-laptop-13-pro-review",
    "domain": "AI 算力 / 半导体",
    "title": "Framework Laptop 13 Pro review: It cleans up nice",
    "url": "https://www.tomshardware.com/laptops/framework-laptop-13-pro-review",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T15:00:00+00:00",
    "summary": "The Framework Laptop 13 Pro is its most solidly built laptop ever, with a bright display and long battery life sweetening the deal — if you can afford it."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/nvidia-weighs-250-billion-guarantee-so-openai-can-lease-softbanks-10-gigawatt-ohio-campus",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia weighs $250 billion guarantee so OpenAI can lease SoftBank's 10-gigawatt Ohio campus, report claims — Nvidia also said to be discussing $350 billion deal to finance chips for the site",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/nvidia-weighs-250-billion-guarantee-so-openai-can-lease-softbanks-10-gigawatt-ohio-campus",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T13:34:28+00:00",
    "summary": "OpenAI is in advanced talks to lease SB Energy's 10 GW data center campus in Piketon, Ohio, with Nvidia in discussions to guarantee roughly $250 billion of the financing behind it."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-developer-runs-28-9-million-parameter-model-on-usd10-esp32-s3-microcontroller-uses-googles-per-layer-embeddings-technique-stores-table-on-16mb-flash-memory",
    "domain": "AI 算力 / 半导体",
    "title": "AI developer runs 28.9-million-parameter model on $10 ESP32-S3 microcontroller — uses Google's Per-Layer Embeddings technique, stores table on 16MB Flash memory",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-developer-runs-28-9-million-parameter-model-on-usd10-esp32-s3-microcontroller-uses-googles-per-layer-embeddings-technique-stores-table-on-16mb-flash-memory",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T13:07:53+00:00",
    "summary": "Getting a local language model running on a sub-$10 microcontroller is impressive despite its obvious limitations."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/disgruntled-gamer-builds-booby-trapped-steam-deck-with-3d-printed-spikes-and-a-built-in-taser-raspberry-pi-powers-speaker-camera-and-alarm-to-stop-family-members-draining-his-battery",
    "domain": "AI 算力 / 半导体",
    "title": "Disgruntled gamer builds booby-trapped Steam Deck with 3D-printed spikes and a built-in taser — Raspberry Pi powers speaker, camera, and alarm to stop family members draining his battery",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/disgruntled-gamer-builds-booby-trapped-steam-deck-with-3d-printed-spikes-and-a-built-in-taser-raspberry-pi-powers-speaker-camera-and-alarm-to-stop-family-members-draining-his-battery",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T12:10:35+00:00",
    "summary": "A Steam Deck devotee was so fed up with their family borrowing their handheld and leaving it with a flat battery that they have resorted to quite extreme anti-sharing measures."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-splits-zen-7-into-three-epyc-families-for-2028-and-starts-selling-server-cpus-by-the-agent",
    "domain": "AI 算力 / 半导体",
    "title": "AMD splits Zen 7 into three EPYC families for 2028 and starts selling server CPUs by the agent — Florence, Ferrara, and Fidenza to be applied across AI-focused product stack",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-splits-zen-7-into-three-epyc-families-for-2028-and-starts-selling-server-cpus-by-the-agent",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T12:04:52+00:00",
    "summary": "The company named Florence, Ferrara, and Fidenza in its launch release, extended its annual CPU, GPU, networking, and rack cadence out to 2030."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/it-sounds-like-someone-set-up-a-vacuum-like-in-your-living-room-michigan-residents-sue-ai-data-center-emitting-noise-24-7-company-fined-for-industrial-noise-ordinance-violations-offers-to-buy-homes-from-residents",
    "domain": "AI 算力 / 半导体",
    "title": "'It sounds like someone set up a vacuum, like in your living room': Michigan residents sue AI data center emitting noise 24/7 — company fined for industrial noise ordinance violations, offers to buy h",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/it-sounds-like-someone-set-up-a-vacuum-like-in-your-living-room-michigan-residents-sue-ai-data-center-emitting-noise-24-7-company-fined-for-industrial-noise-ordinance-violations-offers-to-buy-homes-from-residents",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T12:02:21+00:00",
    "summary": "Residents of Dowagiac, Michigan, filed a case against a data center for generating noise pollution 24/7 for over two years. They said that the site has violated city noise ordinances but hasn't made a"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cxmt-closes-up-466-percent-in-shanghai-debut-with-no-hbm-project-in-its-ipo-prospectus",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese memory maker CXMT posts blistering 466% leap in Shanghai IPO — bulk of spending to be focused on DRAM production, no HBM in sight",
    "url": "https://www.tomshardware.com/tech-industry/cxmt-closes-up-466-percent-in-shanghai-debut-with-no-hbm-project-in-its-ipo-prospectus",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T11:48:56+00:00",
    "summary": "The prospectus splits 29.5 billion yuan across three projects."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-16gb-of-ddr5-ram-for-just-usd16-when-you-buy-it-with-amds-brand-new-7700x3d-ryzen-7-with-an-x870-motherboard-g-skill-ripjaws-and-an-aio-for-just-usd588",
    "domain": "AI 算力 / 半导体",
    "title": "Get 16GB of DDR5 RAM for just $16 when you buy it with AMD's brand-new 7700X3D — Ryzen 7 with an X870 motherboard, G.Skill Ripjaws, and an AIO for just $588",
    "url": "https://www.tomshardware.com/pc-components/get-16gb-of-ddr5-ram-for-just-usd16-when-you-buy-it-with-amds-brand-new-7700x3d-ryzen-7-with-an-x870-motherboard-g-skill-ripjaws-and-an-aio-for-just-usd588",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T10:56:30+00:00",
    "summary": "Get a single stick of 16GB DDR5 RAM for just $16 when you buy it with a Ryzen 7 7700X3D and MSI Pro X870-P motherboard."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/save-usd1-000-on-lenovos-over-the-top-rtx-5090-gaming-laptop-this-18-inch-monster-packs-64gb-of-ram-and-up-to-a-440hz-refresh-rate",
    "domain": "AI 算力 / 半导体",
    "title": "Save $1,000 on Lenovo's over-the-top RTX 5090 gaming laptop — this 18-inch monster packs 64GB of RAM and up to a 440Hz refresh rate",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/save-usd1-000-on-lenovos-over-the-top-rtx-5090-gaming-laptop-this-18-inch-monster-packs-64gb-of-ram-and-up-to-a-440hz-refresh-rate",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T10:56:18+00:00",
    "summary": "B&amp;H Photo has chopped $1,000 off the price of this super-powerful RTX 5090-laden Lenovo Legion 9i gaming laptop with 64GB of RAM"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/californias-largest-ai-data-center-project-suing-for-access-to-287-million-gallons-of-colorado-river-water-0-03-percent-of-imperial-valleys-supply-plaintiffs-claim-project-equivalent-to-160-acre-farm-amidst-about-jobs-and-reallocation-of-farmland",
    "domain": "AI 算力 / 半导体",
    "title": "California's largest AI data center project suing for access to 287 million gallons of Colorado River water, 0.03% of Imperial Valley’s supply — plaintiffs claim project equivalent to 160-acre farm am",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/californias-largest-ai-data-center-project-suing-for-access-to-287-million-gallons-of-colorado-river-water-0-03-percent-of-imperial-valleys-supply-plaintiffs-claim-project-equivalent-to-160-acre-farm-amidst-about-jobs-and-reallocation-of-farmland",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T09:56:17+00:00",
    "summary": "Buildout of large AI data centers in regions historically specializing in agriculture may have long-lasting consequences."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/physicists-build-a-computer-from-400-particles-orbiting-in-liquid-with-10-times-the-error-of-memristor-rivals",
    "domain": "AI 算力 / 半导体",
    "title": "Physicists turn particles in chaotic orbits into liquid computers — but this fluid hardware still trails memristor rivals",
    "url": "https://www.tomshardware.com/tech-industry/physicists-build-a-computer-from-400-particles-orbiting-in-liquid-with-10-times-the-error-of-memristor-rivals",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T15:05:00+00:00",
    "summary": "Each oscillator is a silica sphere of 3μm radius, capped on one side with 80nm of carbon and suspended in a water-lutidine mixture held at 28°C."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/open-source-3d-printed-portable-mri-machine-built-for-under-usd70-000-diy-medical-equipment-costs-less-than-7-percent-of-a-full-sized-mri-machines-usd1-1-million-starting-price",
    "domain": "AI 算力 / 半导体",
    "title": "Open-source 3D-printed portable MRI machine built for under $70,000 — DIY medical equipment costs less than 7% of a full-sized MRI machine’s $1.1 million starting price",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/open-source-3d-printed-portable-mri-machine-built-for-under-usd70-000-diy-medical-equipment-costs-less-than-7-percent-of-a-full-sized-mri-machines-usd1-1-million-starting-price",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T14:36:50+00:00",
    "summary": "This open-source project uses 3D printing to build the core of a portable MRI machine, although it still has a lower resolution compared to multi-million-dollar full-sized machines. One tech expert su"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/chinese-cxmt-dram-doesnt-look-like-the-budget-savior-many-were-expecting-new-modules-enter-the-market-but-prices-still-track-the-big-three",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese CXMT DRAM doesn't look like the budget savior many were expecting — new modules enter the market, but prices still track the big three",
    "url": "https://www.tomshardware.com/pc-components/dram/chinese-cxmt-dram-doesnt-look-like-the-budget-savior-many-were-expecting-new-modules-enter-the-market-but-prices-still-track-the-big-three",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T13:25:30+00:00",
    "summary": "Chinese retail listings indicate that CXMT-based memory modules are priced similarly to those featuring chips from the big three, despite expectations that they must be cheaper."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/xfx-radeon-rx-9070-xt-drops-to-its-lowest-price-of-the-summer-save-usd90-on-amds-flagship-rdna-4-graphics-card",
    "domain": "AI 算力 / 半导体",
    "title": "XFX Radeon RX 9070 XT drops to its lowest price of the summer — save $90 on AMD's flagship RDNA 4 graphics card",
    "url": "https://www.tomshardware.com/pc-components/xfx-radeon-rx-9070-xt-drops-to-its-lowest-price-of-the-summer-save-usd90-on-amds-flagship-rdna-4-graphics-card",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T12:31:14+00:00",
    "summary": "If you've been waiting for RX 9070 XT prices to fall, this $90 discount on XFX's triple-fan Quicksilver model is one of the best deals currently available."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/minecraft-system-requirements-raised-for-the-first-time-in-17-years-microsoft-now-recommends-16gb-of-ram-and-a-2020s-or-newer-cpu-to-run-the-java-edition",
    "domain": "AI 算力 / 半导体",
    "title": "Minecraft system requirements raised for the first time in 17 years — Microsoft now recommends 16GB of RAM and a 2020s or newer CPU to run the Java Edition",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/minecraft-system-requirements-raised-for-the-first-time-in-17-years-microsoft-now-recommends-16gb-of-ram-and-a-2020s-or-newer-cpu-to-run-the-java-edition",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T12:30:00+00:00",
    "summary": "Microsoft is increasing the minimum and recommended system requirements for Minecraft for the first time, 17 years after it launched. Although the system upgrade is quite reasonable and the hardware f"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/hp-omnibook-x-flip-14-review",
    "domain": "AI 算力 / 半导体",
    "title": "HP OmniBook X Flip 14 Review: Premium design, middling performance",
    "url": "https://www.tomshardware.com/laptops/hp-omnibook-x-flip-14-review",
    "source": "Charles Jefferies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T12:05:00+00:00",
    "summary": "Though HP’s OmniBook X Flip 14 offers premium quality and features, rivals offer better display value or stronger performance for the money."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/3d-printed-f-14-tomcat-uses-an-fpga-recreation-of-the-worlds-first-microprocessor-cadcs-mp944-chip-controls-the-fighters-swing-wing-system-among-other-things",
    "domain": "AI 算力 / 半导体",
    "title": "3D-printed F-14 Tomcat uses an FPGA recreation of the ‘world’s first microprocessor' — CADC’s MP944 chip controls the fighter’s swing-wing system, among other things",
    "url": "https://www.tomshardware.com/pc-components/cpus/3d-printed-f-14-tomcat-uses-an-fpga-recreation-of-the-worlds-first-microprocessor-cadcs-mp944-chip-controls-the-fighters-swing-wing-system-among-other-things",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T12:05:00+00:00",
    "summary": "An FPGA and embedded systems expert has recreated the US Navy’s F-14 Tomcat’s Central Air Data Computer (CADC) in an FPGA. It is demonstrated in a scale 3D printed model aircraft"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/zeiss-expands-german-site-that-caps-asmls-euv-scanner-output",
    "domain": "AI 算力 / 半导体",
    "title": "Zeiss expands German site that caps ASML's EUV scanner output — first new building opens four years after Oberkochen site groundbreaking",
    "url": "https://www.tomshardware.com/tech-industry/zeiss-expands-german-site-that-caps-asmls-euv-scanner-output",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T11:46:59+00:00",
    "summary": "Zeiss Semiconductor Manufacturing Technology is adding around 25,000 square meters of production and production-adjacent space at Oberkochen in southern Germany."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/ai-enthusiast-adds-nvidia-tesla-v100-as-loud-as-a-lawnmower-to-gaming-pc-for-usd266-32gb-of-vram-rig-can-run-27-billion-parameter-model-at-32-tokens-per-second",
    "domain": "AI 算力 / 半导体",
    "title": "AI enthusiast adds Nvidia Tesla V100 as loud as a lawnmower to gaming PC for $266 — 32GB of VRAM rig can run 27 billion parameter model at 32 tokens per second",
    "url": "https://www.tomshardware.com/pc-components/gpus/ai-enthusiast-adds-nvidia-tesla-v100-as-loud-as-a-lawnmower-to-gaming-pc-for-usd266-32gb-of-vram-rig-can-run-27-billion-parameter-model-at-32-tokens-per-second",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T10:00:00+00:00",
    "summary": "A computing enthusiast has repurposed a very noisy and largely obsolete enterprise GPU (with lots of VRAM) for local LLM inference purposes."
  },
  {
    "id": "hn:48992221",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC eyes price hikes of up to 25% on chip production services in 2027",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes",
    "source": "speckx",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-21T13:40:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49025890",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's 256-core Epyc 9996 'Venice' claims up to a 3.4x jump over Intel Xeon",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-256-core-epyc-9996-venice-claims-up-to-a-3-4x-jump-over-intel-xeon-competition-20-percent-over-nvidia-vera-zen-6-comes-with-up-to-1024mb-of-l3-16-channel-memory-and-5ghz-clock-speeds",
    "source": "rndsignals",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-23T18:16:54+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/intel-foundry-improves-execution-but-external-customers-remain-the-test/",
    "domain": "AI 算力 / 半导体",
    "title": "Intel Foundry Improves Execution, but External Customers Remain the Test",
    "url": "https://www.eetimes.com/intel-foundry-improves-execution-but-external-customers-remain-the-test/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T22:00:00+00:00",
    "summary": "Intel’s fabs are healing, but $293M in outside revenue won’t scare TSMC yet. The post Intel Foundry Improves Execution, but External Customers Remain the Test appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/dac-2026-what-does-it-actually-take-to-create-ai-chips/",
    "domain": "AI 算力 / 半导体",
    "title": "DAC 2026: What Does It Actually Take to Create AI Chips?",
    "url": "https://www.eetimes.com/dac-2026-what-does-it-actually-take-to-create-ai-chips/",
    "source": "Frank Schirrmeister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:00:00+00:00",
    "summary": "AI chips don’t need hype—they need power, memory, IP, thermal, and verification fights. See what DAC 2026 engineers will expose. The post DAC 2026: What Does It Actually Take to Create AI Chips? appea"
  },
  {
    "id": "rss:https://www.eetimes.com/supply-chain-leaders-new-math-for-network-decisions/",
    "domain": "AI 算力 / 半导体",
    "title": "Supply Chain Leaders’ New Math for Network Decisions",
    "url": "https://www.eetimes.com/supply-chain-leaders-new-math-for-network-decisions/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T08:00:00+00:00",
    "summary": "Gartner urges supply chain leaders to quantify daily operational friction, making network investments more resilient and easier to justify. The post Supply Chain Leaders&#8217; New Math for Network De"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/security-flaw-in-vaticans-click-to-pray-app-leaves-over-700-000-global-users-exposed-app-has-been-leaking-user-data-for-over-six-months-and-still-does",
    "domain": "AI 算力 / 半导体",
    "title": "Security flaw in Vatican’s ‘Click to Pray’ app leaves over 700,000 global users exposed — app has been leaking user data for over six months and still does",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/security-flaw-in-vaticans-click-to-pray-app-leaves-over-700-000-global-users-exposed-app-has-been-leaking-user-data-for-over-six-months-and-still-does",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T17:56:07+00:00",
    "summary": "An app linked to the Vatican with hundreds of thousands of users was found to have zero authentication and security. That means anyone can access its backend and siphon users' data, including names, e"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-agent-goes-rogue-and-hacks-popular-ai-community-left-escape-plans-for-future-models-inside-the-companys-infrastructure",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI agent goes rogue and hacks popular AI community — left escape plans for future models inside the company's infrastructure",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-agent-goes-rogue-and-hacks-popular-ai-community-left-escape-plans-for-future-models-inside-the-companys-infrastructure",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T16:41:59+00:00",
    "summary": "OpenAI tests multiple autonomous AI agents at once and has difficulty identifying the threats each of them represents, if a new report from Reuters is accurate."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/ram-machine-case-probably-costs-more-than-the-entire-build-nvidia-rtx-5060-core-ultra-5-cpu-and-32gb-ddr5-8200-ram-are-hiding-inside",
    "domain": "AI 算力 / 半导体",
    "title": "'RAM Machine' case probably costs more than the entire build — Nvidia RTX 5060, Core Ultra 5 CPU, and 32GB DDR5-8200 RAM are hiding inside",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/ram-machine-case-probably-costs-more-than-the-entire-build-nvidia-rtx-5060-core-ultra-5-cpu-and-32gb-ddr5-8200-ram-are-hiding-inside",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T15:34:57+00:00",
    "summary": "A Redditor is giving away an RTX 5060 gaming PC that's covered by RAM on the outside and has 32GB of RAM on the inside. You can join the sweepstakes simply by leaving a comment on the post."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-an-nvidia-rtx-5060-ti-gaming-pc-with-core-ultra-7-cpu-and-32gb-ram-for-under-usd1-200-thermaltakes-view-u2660t-170-slashed-by-33-percent",
    "domain": "AI 算力 / 半导体",
    "title": "Grab an Nvidia RTX 5060 Ti gaming PC with Core Ultra 7 CPU and 32GB RAM for under $1,200 — Thermaltake's View u2660T-170 slashed by 33%",
    "url": "https://www.tomshardware.com/pc-components/grab-an-nvidia-rtx-5060-ti-gaming-pc-with-core-ultra-7-cpu-and-32gb-ram-for-under-usd1-200-thermaltakes-view-u2660t-170-slashed-by-33-percent",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T15:18:22+00:00",
    "summary": "Thermaltake has a no-brainer deal up on Woot right now where it'll let you have an $1,800 PC for as little as 1,177. For that price, you're getting an RTX 5060 Ti (8GB), a Core Ultra 7 265KF, 32GB of "
  },
  {
    "id": "hn:49012431",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia released its first official GeForce driver for Windows on Arm",
    "url": "https://videocardz.com/newz/nvidias-first-geforce-driver-for-windows-on-arm-confirms-rtx-spark-n1x-with-6144-or-5120-cuda-cores",
    "source": "robotnikman",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-22T19:49:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:48735444",
    "domain": "大厂 AI 动态",
    "title": "Nano Banana 2 Lite",
    "url": "https://deepmind.google/models/gemini-image/flash-lite/",
    "source": "minimaxir",
    "platform": "hackernews",
    "points": 435,
    "published_at": "2026-06-30T16:48:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48756602",
    "domain": "大厂 AI 动态",
    "title": "Kimi K2.7 Code is generally available in GitHub Copilot",
    "url": "https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/",
    "source": "unliftedq",
    "platform": "hackernews",
    "points": 417,
    "published_at": "2026-07-02T04:32:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48925271",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://turntrout.com/why-i-left-google-deepmind",
    "source": "apsec112",
    "platform": "hackernews",
    "points": 390,
    "published_at": "2026-07-15T18:40:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:48936451",
    "domain": "大厂 AI 动态",
    "title": "NotebookLM is now Gemini Notebook",
    "url": "https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/",
    "source": "xnx",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-07-16T16:08:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49067285",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://www.lesswrong.com/posts/iKm2FhpWkuuBojm82/why-i-left-google-deepmind",
    "source": "eatitraw",
    "platform": "hackernews",
    "points": 188,
    "published_at": "2026-07-27T09:56:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48998606",
    "domain": "大厂 AI 动态",
    "title": "Gemini last models: temperature, top_p, and top_k are deprecated and ignored",
    "url": "https://ai.google.dev/gemini-api/docs/latest-model",
    "source": "greatgib",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-07-21T21:27:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48707103",
    "domain": "大厂 AI 动态",
    "title": "Google limits Meta's use of its Gemini AI models",
    "url": "https://www.cnbc.com/2026/06/28/google-limits-metas-use-of-its-gemini-ai-models-ft-reports.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 162,
    "published_at": "2026-06-28T13:30:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:48965880",
    "domain": "大厂 AI 动态",
    "title": "Ollama: All Aboard Open Models",
    "url": "https://ollama.com/blog/all-aboard-open-models",
    "source": "inferhaven",
    "platform": "hackernews",
    "points": 138,
    "published_at": "2026-07-19T07:59:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48864507",
    "domain": "大厂 AI 动态",
    "title": "Please don't discontinue Gemini 2.5 Flash",
    "url": "https://discuss.ai.google.dev/t/please-dont-discontinue-gemini-2-5-flash/174246",
    "source": "NickDob",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-07-10T20:00:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:48993130",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.6 Flash",
    "url": "https://console.cloud.google.com/agent-platform/publishers/google/model-garden/gemini-3.6-flash",
    "source": "marrf",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-07-21T14:56:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:48959297",
    "domain": "大厂 AI 动态",
    "title": "Our Approach to Bioresilience: Isomorphic Labs and Google DeepMind",
    "url": "https://deepmind.google/blog/our-approach-to-bioresilience/",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 83,
    "published_at": "2026-07-18T16:02:45+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/971649/x-money-launch-elon-musk",
    "domain": "大厂 AI 动态",
    "title": "X Money is launching in the US starting today",
    "url": "https://www.theverge.com/tech/971649/x-money-launch-elon-musk",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T22:10:18+00:00",
    "summary": "X Money, a core part of Elon Musk's mission to turn X into an \"everything app,\" is rolling out starting today, 9to5Mac reports. The payment platform offers a digital wallet and peer-to-peer payments s"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/971557/razer-huntsman-v3-pro-tkl-optical-analog-gaming-keyboard-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Razer’s analog Huntsman V3 Pro is over 20 percent off",
    "url": "https://www.theverge.com/gadgets/971557/razer-huntsman-v3-pro-tkl-optical-analog-gaming-keyboard-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T21:29:22+00:00",
    "summary": "Gaming keyboards have evolved over the years to add RGB LEDs, extra knobs, and buttons with screens, but one feature has remained fairly consistent: the mechanical switch. That’s slowly changing, with"
  },
  {
    "id": "rss:https://www.theverge.com/games/971545/xbox-outage-disc-physical-games",
    "domain": "大厂 AI 动态",
    "title": "Xbox’s huge outage even blocked games on disc",
    "url": "https://www.theverge.com/games/971545/xbox-outage-disc-physical-games",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T19:53:50+00:00",
    "summary": "An extended Xbox outage that began Sunday evening didn't just cause issues for people trying to play digital games - it blocked people from playing their disc-based games, too. Xbox's status page init"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/971535/nanoleaf-blocks-combo-xl-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Nanoleaf&#8217;s colorful pegboard and shelf kit is half off",
    "url": "https://www.theverge.com/gadgets/971535/nanoleaf-blocks-combo-xl-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T19:24:55+00:00",
    "summary": "Nanoleaf&#8217;s Blocks Combo XL Smarter Kit is a fun back-to-school buy that can add pops of customizable light and storage to your wall. It combines colorful smart lighting panels with a low-profile"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/971444/how-chinese-open-weight-ai-models-impact-us-companies",
    "domain": "大厂 AI 动态",
    "title": "Why China is giving away its best AI models",
    "url": "https://www.theverge.com/ai-artificial-intelligence/971444/how-chinese-open-weight-ai-models-impact-us-companies",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T16:51:50+00:00",
    "summary": "Silicon Valley has spent much of the past week on red alert, digesting the arrival of Moonshot AI's Kimi K3, a Chinese AI model that can allegedly beat some of the best systems built by US companies a"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/971452/youtube-premium-peacock-streaming-deal",
    "domain": "大厂 AI 动态",
    "title": "YouTube Premium will include Peacock starting next year",
    "url": "https://www.theverge.com/streaming/971452/youtube-premium-peacock-streaming-deal",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T16:18:52+00:00",
    "summary": "YouTube's ad-free Premium subscription is getting another perk: access to Peacock. In an announcement on Monday, NBCUniversal says the multi-year agreement will allow Premium subscribers to stream Pea"
  },
  {
    "id": "rss:https://www.theverge.com/tech/971437/amazon-leo-direct-to-device-satellite-network",
    "domain": "大厂 AI 动态",
    "title": "Amazon&#8217;s trying to launch a global satellite cellphone network in 2028",
    "url": "https://www.theverge.com/tech/971437/amazon-leo-direct-to-device-satellite-network",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T15:40:38+00:00",
    "summary": "Amazon filed an FCC application on Saturday to launch a new Leo satellite constellation that will provide direct-to-device satellite service for \"voice, messaging, data, and emergency services.\" If ap"
  },
  {
    "id": "rss:https://www.theverge.com/tech/971160/framework-laptop-13-pro-intel-review",
    "domain": "大厂 AI 动态",
    "title": "This is my new favorite laptop, but thanks to RAMageddon the price already went up by $800",
    "url": "https://www.theverge.com/tech/971160/framework-laptop-13-pro-intel-review",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T15:00:00+00:00",
    "summary": "Framework laptops always come with compromises in exchange for their unique DIY premise. Even though you pay extra for one compared to sleeker options from competitors, it's easier to excuse minor fla"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/971306/tariffs-liberation-day-ai-trade-shipping-jobs-canada",
    "domain": "大厂 AI 动态",
    "title": "Tariffs didn’t bring manufacturing jobs back to the US",
    "url": "https://www.theverge.com/podcast/971306/tariffs-liberation-day-ai-trade-shipping-jobs-canada",
    "source": "Nilay Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T15:00:00+00:00",
    "summary": "Today, I’m talking with Evan Smith, who is cofounder and CEO of Altana, a company that develops software tools to manage big, messy supply chain networks around the world. We last had Evan on in early"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/971332/samsung-qdoled-gaming-monitor-find-my-tracker-ps5-logitech-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Samsung’s 27-inch QD-OLED gaming monitor is priced right at $299.99",
    "url": "https://www.theverge.com/gadgets/971332/samsung-qdoled-gaming-monitor-find-my-tracker-ps5-logitech-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T14:56:38+00:00",
    "summary": "The cost of QD-OLED gaming monitors is going down, even as many other PC components are still soaring above their normal prices. If your budget is locked at $300, Samsung’s 27-inch 1440p model costs e"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/cursor-makes-its-biggest-india-push-yet-ahead-of-spacex-acquisition-with-localized-pricing/",
    "domain": "大厂 AI 动态",
    "title": "Cursor makes its biggest India push yet ahead of SpaceX acquisition with localized pricing",
    "url": "https://techcrunch.com/2026/07/27/cursor-makes-its-biggest-india-push-yet-ahead-of-spacex-acquisition-with-localized-pricing/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:30:00+00:00",
    "summary": "Cursor says India is now its third-largest market globally and plans to expand local hiring and enterprise sales."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/anthropics-dario-amodei-responds-doesnt-oppose-open-weight-models-but-fears-chinese-ai/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s Dario Amodei responds: doesn’t oppose open-weight models, but fears Chinese AI",
    "url": "https://techcrunch.com/2026/07/27/anthropics-dario-amodei-responds-doesnt-oppose-open-weight-models-but-fears-chinese-ai/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T00:13:33+00:00",
    "summary": "Anthropic founder and CEO Dario Amodei made his views clear about open-weight models and China's growing AI capabilities."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/satya-nadella-says-companies-that-trust-one-ai-for-everything-may-not-survive/",
    "domain": "大厂 AI 动态",
    "title": "Satya Nadella says companies that trust one AI for everything may not survive",
    "url": "https://techcrunch.com/2026/07/27/satya-nadella-says-companies-that-trust-one-ai-for-everything-may-not-survive/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T21:17:11+00:00",
    "summary": "Companies without their own models — or without a layer of AI infrastructure known as AI gateways to separate their prompts from the model itself — will be in trouble, Nadella says."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/thea-energy-lands-20m-federal-grant-to-build-its-magnets-for-fusion-reactors/",
    "domain": "大厂 AI 动态",
    "title": "Thea Energy lands $20M federal grant to build its magnets for fusion reactors",
    "url": "https://techcrunch.com/2026/07/27/thea-energy-lands-20m-federal-grant-to-build-its-magnets-for-fusion-reactors/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T20:40:12+00:00",
    "summary": "Fusion power startup Thea Energy snagged a $20 million award from ARPA-E to scale production of its high-temperature superconducting magnets."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/as-rivals-chase-acquisitions-peacock-bets-on-bundles-through-a-new-deal-with-youtube/",
    "domain": "大厂 AI 动态",
    "title": "As rivals chase acquisitions, Peacock bets on bundles through a new deal with YouTube",
    "url": "https://techcrunch.com/2026/07/27/as-rivals-chase-acquisitions-peacock-bets-on-bundles-through-a-new-deal-with-youtube/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T20:40:00+00:00",
    "summary": "The deal means content will be integrated into the YouTube experience, allowing viewers to discover and watch Peacock content without leaving the platform."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/psa-your-claude-shared-chats-and-artifacts-may-have-ended-up-on-google/",
    "domain": "大厂 AI 动态",
    "title": "PSA: Your Claude shared chats and Artifacts may have ended up on Google",
    "url": "https://techcrunch.com/2026/07/27/psa-your-claude-shared-chats-and-artifacts-may-have-ended-up-on-google/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T20:19:42+00:00",
    "summary": "The issue appears to have originated from Claude’s “share chat” feature, which allows users to create links that enable anyone with the assigned URL view a conversation or project."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/microsoft-launches-its-first-cyber-model-and-a-new-agentic-cybersecurity-system/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft launches its first cybersecurity model, plus a new agentic cybersecurity system",
    "url": "https://techcrunch.com/2026/07/27/microsoft-launches-its-first-cyber-model-and-a-new-agentic-cybersecurity-system/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T18:32:11+00:00",
    "summary": "Microsoft bolstered its AI cybersecurity offerings this week with the launch of its first AI security model and a new security platform."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/apple-sued-after-alleged-app-store-crypto-scam-cost-users-1-8m/",
    "domain": "大厂 AI 动态",
    "title": "Apple sued after alleged App Store crypto scam cost users $1.8M",
    "url": "https://techcrunch.com/2026/07/27/apple-sued-after-alleged-app-store-crypto-scam-cost-users-1-8m/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T18:28:15+00:00",
    "summary": "Apple is facing a lawsuit from three users who say they collectively lost more than $1.8 million after downloading a fraudulent crypto wallet from the App Store, challenging the company’s longstanding"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/amazons-new-satellite-network-for-mobile-phones-could-turn-up-the-heat-on-spacex/",
    "domain": "大厂 AI 动态",
    "title": "Amazon’s new satellite network for mobile phones could turn up the heat on SpaceX",
    "url": "https://techcrunch.com/2026/07/27/amazons-new-satellite-network-for-mobile-phones-could-turn-up-the-heat-on-spacex/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T18:08:29+00:00",
    "summary": "Amazon is expanding its plans for providing satellite connectivity to mobile phones."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/antares-raises-470m-to-build-nuclear-reactors-for-the-u-s-military/",
    "domain": "大厂 AI 动态",
    "title": "Antares raises $470M to build nuclear reactors for the US military",
    "url": "https://techcrunch.com/2026/07/27/antares-raises-470m-to-build-nuclear-reactors-for-the-u-s-military/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T17:49:28+00:00",
    "summary": "Antares has raised $470 million to build small modular reactors — 100 kW to 1 MW — for U.S. Air Force bases."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/openais-hugging-face-breach-has-reignited-the-debate-over-alignment-and-control/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s Hugging Face breach has reignited the debate over alignment and control",
    "url": "https://techcrunch.com/2026/07/27/openais-hugging-face-breach-has-reignited-the-debate-over-alignment-and-control/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T17:28:42+00:00",
    "summary": "OpenAI's Hugging Face breach has reignited debate over AI alignment and control, exposing competing views on whether increasingly capable AI should be better aligned, better contained, or both."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/threads-users-can-now-chat-with-meta-ai-in-their-dms/",
    "domain": "大厂 AI 动态",
    "title": "Threads users can now chat with Meta AI in their DMs",
    "url": "https://techcrunch.com/2026/07/27/threads-users-can-now-chat-with-meta-ai-in-their-dms/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T16:45:24+00:00",
    "summary": "Meta on Monday said it is rolling out its Meta AI chatbot within Threads' DMs, giving users a way to chat with the AI assistant."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/googles-ai-search-is-rapidly-becoming-the-default-new-data-shows/",
    "domain": "大厂 AI 动态",
    "title": "Google’s AI search is rapidly becoming the default, new data shows",
    "url": "https://techcrunch.com/2026/07/27/googles-ai-search-is-rapidly-becoming-the-default-new-data-shows/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T15:57:12+00:00",
    "summary": "Google’s AI Overviews now appear in 43% of searches, underscoring how quickly AI-generated answers are becoming the default way people discover information online."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/power-up-your-ai-infrastructure-a-first-look-at-the-smart-systems-stage-agenda-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Power up your AI infrastructure! A first look at the Smart Systems Stage agenda at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/07/27/power-up-your-ai-infrastructure-a-first-look-at-the-smart-systems-stage-agenda-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T15:30:00+00:00",
    "summary": "At TechCrunch Disrupt 2026, the Smart Systems Stage will be where energy, infrastructure, and technology collide, covering everything from fusion breakthroughs to the grid strain AI is putting on the "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/this-9-key-physically-locks-your-most-addictive-apps/",
    "domain": "大厂 AI 动态",
    "title": "This $9 key physically locks your most addictive apps",
    "url": "https://techcrunch.com/2026/07/27/this-9-key-physically-locks-your-most-addictive-apps/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T15:25:37+00:00",
    "summary": "This $9 NFC key requires you to physically scan it to unlock distracting apps on your phone."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/ilya-sutskevers-safe-superintelligence-partners-with-nvidia-to-scale-its-ai-research/",
    "domain": "大厂 AI 动态",
    "title": "Ilya Sutskever’s Safe Superintelligence partners with Nvidia to scale its AI research",
    "url": "https://techcrunch.com/2026/07/27/ilya-sutskevers-safe-superintelligence-partners-with-nvidia-to-scale-its-ai-research/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T15:01:50+00:00",
    "summary": "After two years in stealth, Safe Superintelligence has announced a long-term partnership with Nvidia as it prepares to scale to its next phase."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/snapchat-now-lets-you-share-what-youre-listening-to-in-real-time/",
    "domain": "大厂 AI 动态",
    "title": "Snapchat now lets you share what you’re listening to in real time",
    "url": "https://techcrunch.com/2026/07/27/snapchat-now-lets-you-share-what-youre-listening-to-in-real-time/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T13:00:00+00:00",
    "summary": "Starting with Spotify, Snapchat users will be able to link their accounts, choose who can see their listening activity, and see what their friends are listening to in real time."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/enigma-raises-70m-to-make-controlling-a-robot-as-easy-as-adjusting-the-volume/",
    "domain": "大厂 AI 动态",
    "title": "Enigma raises $71M to make controlling a robot as easy as adjusting the volume",
    "url": "https://techcrunch.com/2026/07/27/enigma-raises-70m-to-make-controlling-a-robot-as-easy-as-adjusting-the-volume/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T13:00:00+00:00",
    "summary": "The massive seed round was led by Index Ventures and Ribbit Capital, with participation from Sarah Guo's Conviction Partners."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/27/europe-got-its-own-tbpn-style-live-show-and-its-already-a-hot-spot-on-a-press-tour/",
    "domain": "大厂 AI 动态",
    "title": "Europe got its own TBPN-style live show, and everyone’s angling for a guest spot",
    "url": "https://techcrunch.com/2026/07/27/europe-got-its-own-tbpn-style-live-show-and-its-already-a-hot-spot-on-a-press-tour/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T10:00:00+00:00",
    "summary": "The five-day format will look quite similar to the two-day format. There will be a live show from 12 p.m. U.K. time to 3 p.m., breaking down trending stories, and then for two hours, they will have gu"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/26/are-brain-waves-the-next-unlock-for-physical-ai/",
    "domain": "大厂 AI 动态",
    "title": "Are brain waves the next unlock for physical AI?",
    "url": "https://techcrunch.com/2026/07/26/are-brain-waves-the-next-unlock-for-physical-ai/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T00:19:14+00:00",
    "summary": "Forget YouTube videos — frontier physical AI models need multiple camera angles, dense annotation, and, soon, brain wave readings."
  },
  {
    "id": "rss:https://stratechery.com/2026/vacation-week-of-july-27/",
    "domain": "大厂 AI 动态",
    "title": "Vacation: Week of July 27",
    "url": "https://stratechery.com/2026/vacation-week-of-july-27/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T10:00:00+00:00",
    "summary": "Stratechery is on vacation the week of July 27. There will be no Weekly Article or Updates. The next Update will be on Monday, August 3. Sharp Tech, and Greatest of All Talk&#160;&#160;will also retur"
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/07/microsoft-unveils-ai-security-tools-it-says-outperform-competing-platforms/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft unveils AI security tools it says outperform competing platforms",
    "url": "https://arstechnica.com/security/2026/07/microsoft-unveils-ai-security-tools-it-says-outperform-competing-platforms/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T21:56:14+00:00",
    "summary": "Microsoft says tools cost less than competing ones and outperform them, too."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/starlink-gets-exemption-from-fcc-ban-on-routers-made-outside-the-us/",
    "domain": "大厂 AI 动态",
    "title": "Trump admin exempts SpaceX's Starlink from FCC ban on foreign-made routers",
    "url": "https://arstechnica.com/tech-policy/2026/07/starlink-gets-exemption-from-fcc-ban-on-routers-made-outside-the-us/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T21:40:27+00:00",
    "summary": "Starlink has a Texas factory but also makes routers in Vietnam."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/epic-diarrhea-outbreak-has-40-of-americans-avoiding-fruits-and-veggies/",
    "domain": "大厂 AI 动态",
    "title": "Epic diarrhea outbreak has 40% of Americans avoiding fruits and veggies",
    "url": "https://arstechnica.com/health/2026/07/epic-diarrhea-outbreak-has-40-of-americans-avoiding-fruits-and-veggies/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T20:42:13+00:00",
    "summary": "Kennedy has focused on nutrition but has neglected food safety, critics say."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/ios-and-macos-26-6-arrive-today-paving-the-way-for-ios-and-macos-27/",
    "domain": "大厂 AI 动态",
    "title": "iOS and macOS 26.6 arrive today, paving the way for iOS and macOS 27",
    "url": "https://arstechnica.com/gadgets/2026/07/ios-and-macos-26-6-arrive-today-paving-the-way-for-ios-and-macos-27/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T20:32:45+00:00",
    "summary": "These are likely the last updates of note before Apple's bigger fall updates."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/police-missed-one-underscore-and-sent-the-wrong-man-to-prison/",
    "domain": "大厂 AI 动态",
    "title": "A missing underscore sent innocent man to prison for 18 months",
    "url": "https://arstechnica.com/tech-policy/2026/07/police-missed-one-underscore-and-sent-the-wrong-man-to-prison/",
    "source": "Nate Anderson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T20:22:03+00:00",
    "summary": "When the first step goes wrong, bad results follow."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/google-wont-give-up-odd-war-against-ai-web-scraping-despite-court-loss/",
    "domain": "大厂 AI 动态",
    "title": "“Google and Reddit do not own the Internet,\" web scraper says after court win",
    "url": "https://arstechnica.com/tech-policy/2026/07/google-wont-give-up-odd-war-against-ai-web-scraping-despite-court-loss/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T20:12:42+00:00",
    "summary": "Google's and Reddit's use of DMCA to fight web scraper is bizarre, expert says."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/5th-circuit-blocks-texas-law-requiring-websites-to-filter-harmful-speech/",
    "domain": "大厂 AI 动态",
    "title": "5th Circuit blocks Texas law requiring websites to filter \"harmful\" speech",
    "url": "https://arstechnica.com/tech-policy/2026/07/5th-circuit-blocks-texas-law-requiring-websites-to-filter-harmful-speech/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T19:18:02+00:00",
    "summary": "Age verification is okay, but filtering is preempted by Section 230, judges find."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/verizon-seeks-ai-profits-with-mini-data-centers-1b-dark-fiber-deal-with-google/",
    "domain": "大厂 AI 动态",
    "title": "Verizon touts $1B dark fiber deal for Google data centers as first of many",
    "url": "https://arstechnica.com/ai/2026/07/verizon-seeks-ai-profits-with-mini-data-centers-1b-dark-fiber-deal-with-google/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-27T18:48:41+00:00",
    "summary": "Telecom expects AI revenue from dark fiber deals and retrofitted data centers."
  },
  {
    "id": "hn:49057574",
    "domain": "股票",
    "title": "Google Discloses $94.1B in SpaceX Stock, Marking 6% Stake",
    "url": "https://www.wsj.com/tech/google-discloses-94-1-billion-in-spacex-stock-marking-6-stake-91655d7c",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 337,
    "published_at": "2026-07-26T12:43:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48933344",
    "domain": "股票",
    "title": "SpaceX stock erases all its gains and slides below IPO price in intraday trading",
    "url": "https://www.latimes.com/business/story/2026-07-16/spacex-stock-erases-gains-slides-below-ipo-price-in-intraday-trading",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 314,
    "published_at": "2026-07-16T12:02:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48948435",
    "domain": "股票",
    "title": "Short sellers notch $8.7B profit as SpaceX shares dip to IPO price",
    "url": "https://www.reuters.com/business/media-telecom/short-sellers-rack-up-87-bln-profit-spacex-slips-below-ipo-price-ortex-2026-07-16/",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 168,
    "published_at": "2026-07-17T15:17:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48938001",
    "domain": "股票",
    "title": "SPCX is now Wall Street's most shorted new stock",
    "url": "https://invezz.com/news/2026/07/16/the-worlds-most-valuable-ipo-spcx-is-now-wall-streets-most-shorted-new-stock/",
    "source": "lbrito",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-07-16T18:03:56+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3778103",
    "domain": "股票",
    "title": "中国启动人工智能大模型IPv6能力提升专项行动",
    "url": "https://wallstreetcn.com/articles/3778103",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T05:34:20+00:00",
    "summary": "中央网信办联合京沪浙深四地、携手5家头部大模型企业，在雄安新区启动\"人工智能大模型IPv6能力提升专项行动\"，推动生成式大模型全面支持IPv6。与此同时，雄安新区宣布启动IPv6单栈部署，剑指2030年新建片区全面实现单栈规模化运行。"
  },
  {
    "id": "wscn:3778100",
    "domain": "股票",
    "title": "商务部发布《关于所谓“产能过剩”问题的中方立场》",
    "url": "https://wallstreetcn.com/articles/3778100",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T05:01:52+00:00",
    "summary": "产能问题是世界经济发展过程中伴随产业迭代、市场波动、分工演变出现的正常现象。各国应坚持以市场眼光和全球视野，从经济规律出发，客观、辩证看待所谓的产能“争议”，多探讨合作而非制造对立，共同致力于打通全球供需堵点，优化全球资源配置，推动全球产业健康可持续发展。"
  },
  {
    "id": "wscn:3778099",
    "domain": "股票",
    "title": "SpaceX已经“跌去一个特斯拉”",
    "url": "https://wallstreetcn.com/articles/3778099",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:56:42+00:00",
    "summary": "SpaceX股价自6月高点225美元跌至约113美元，市值蒸发逾1.2万亿美元。8月6日起，近9亿股解禁，年底前可流通股将从6.39亿骤增至53.3亿股，供应压力巨大。100美元成多空博弈关键线，机构构建下行保护，散户仍押注反转。星舰故障及AI估值逻辑切换加剧基本面隐忧，首份季报将成重新定价关键节点。"
  },
  {
    "id": "wscn:3778088",
    "domain": "股票",
    "title": "创业板跌超5%，光刻机逆势活跃，芯片半导体、算力硬件齐跌，恒科指涨0.2%，科网股多反弹，老铺黄金大跌超20%",
    "url": "https://wallstreetcn.com/articles/3778088",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:06:32+00:00",
    "summary": "盘面上，个股涨跌互现，全市场超2800只个股上涨。上午半天成交1.34万亿。沪深两市半日成交额1.33万亿，较上个交易日缩量超200亿。板块方面，算力硬件产业链全面回调，CPO、PCB、存储器方向领跌。稀有金属、光伏、锂电池、氟化工概念股跌幅靠前。金融科技、白酒、脑机接口、短剧游戏题材逆势走强。"
  },
  {
    "id": "wscn:3778098",
    "domain": "股票",
    "title": "浦发银行500亿可转债到期收官，注册资本获批增至333亿元",
    "url": "https://wallstreetcn.com/articles/3778098",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T03:57:35+00:00",
    "summary": "7月27日，浦发银行发布公告称，已收到监管部门关于变更注册资本的批复，监管已同意该行注册资本由约29..."
  },
  {
    "id": "wscn:3778080",
    "domain": "股票",
    "title": "AI烧钱疑虑重燃，韩股重挫10%再熔断，日股跌4%、铠侠大跌18%，芯片股全线承压",
    "url": "https://wallstreetcn.com/articles/3778080",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T03:44:09+00:00",
    "summary": "韩国Kospi指数跌10%，三星电子、SK海力士等芯片股领跌，韩国交易所被迫启动SIDECAR熔断机制。这是费城半导体指数连续第三日下跌后的亚洲传导。本周市场面临美联储、日本央行利率决议与科技巨头财报密集来袭。AI投入能否换来真实回报，将是本周市场最核心的叙事主线。"
  },
  {
    "id": "wscn:3777952",
    "domain": "股票",
    "title": "英伟达CUDA的“冰与火”：算力底座正在发生一场结构性大变局？20年护城河一夜之间崩塌？",
    "url": "https://wallstreetcn.com/premium/articles/3777952?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T03:37:25+00:00",
    "summary": "从「静态壁垒」到「动态演进」——英伟达软件帝国的防守战与进攻者们的破局路径。"
  },
  {
    "id": "wscn:3778096",
    "domain": "股票",
    "title": "京东伦敦买楼，重资产发力欧洲供应链与零售",
    "url": "https://wallstreetcn.com/articles/3778096",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T03:36:45+00:00",
    "summary": "京东在英员工超千名。"
  },
  {
    "id": "wscn:3778095",
    "domain": "股票",
    "title": "美团推出全场景AI Agent平台CatPaw，内部已覆盖9万员工",
    "url": "https://wallstreetcn.com/articles/3778095",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T03:34:25+00:00",
    "summary": "已搭建超过3万个Agent。"
  },
  {
    "id": "wscn:3778094",
    "domain": "股票",
    "title": "英伟达惨遭抛售，苹果重夺全球市值第一，释放什么信号？",
    "url": "https://wallstreetcn.com/articles/3778094",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T03:34:17+00:00",
    "summary": "苹果以4.95万亿美元市值将英伟达挤下全球第一，但更值得关注的是债市同步拉响的警报——英伟达正洽谈的2500亿美元融资担保约为其现金储备的4倍，CDS创活跃交易以来最大单日涨幅。而苹果的“轻资产”AI路径获正市场重估，“苹果曾因AI投入不足而遭受批评，但现在来看它成功规避了资本支出陷阱。”"
  },
  {
    "id": "wscn:3778093",
    "domain": "股票",
    "title": "与纳斯达克深度绑定！韩国股市蜕变为\"半导体指数\"，引发投资者忧虑",
    "url": "https://wallstreetcn.com/articles/3778093",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T03:33:08+00:00",
    "summary": "韩国KOSPI与纳斯达克100的60日相关系数升至2021年以来最高的约0.50，根源在于三星和SK海力士合计占KOSPI权重逾50%，两者深度嵌入美国AI硬件供应链。分析师警告，这一绑定关系已令韩国股市实质蜕变为“半导体指数”，投资者持有美韩两市的地理分散化价值正在消失；一旦超大规模云厂商资本开支放缓，韩国市场将首当其冲。"
  },
  {
    "id": "wscn:3778017",
    "domain": "股票",
    "title": "巨鲸转身：NPS年内首度净买入KOSPI，韩股国家队开始托底？",
    "url": "https://wallstreetcn.com/premium/articles/3778017?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T03:22:24+00:00",
    "summary": "7月以来，韩国国民年金转为净买入韩股，终结半年减持，缓解再平衡抛压，去杠杆进程与外资回流仍将决定后续修复空间。"
  },
  {
    "id": "wscn:3778089",
    "domain": "股票",
    "title": "英伟达的AI账本：谁在为这轮烧钱兜底？",
    "url": "https://wallstreetcn.com/articles/3778089",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T03:08:31+00:00",
    "summary": "英伟达CDS飙升触发暴跌，市场恐慌的并非AI泡沫，而是背后的循环融资黑洞：当芯片商开始为客户购买自己的芯片提供信用支持， AI 的增长开始越来越依赖同一条信用链，市场开始关心的已经不是算力，而是谁来承担最后一棒的风险。"
  },
  {
    "id": "wscn:3778091",
    "domain": "股票",
    "title": "新美联储通讯社：沃什改革雄心遭遇\"家庭内战\"，利率前景扑朔迷离",
    "url": "https://wallstreetcn.com/articles/3778091",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T03:07:20+00:00",
    "summary": "新美联储通讯社Nick Timiraos表示，新任美联储主席沃什上任仅两个月，便以五大外部工作组审查旧有框架、刻意保持政策沉默的\"组合拳\"，在美联储内部引爆一场真实的权力博弈。理事沃勒公开炮轰其\"少说话\"哲学，市场困惑与内部裂痕同步加深。本周议息会议将成为这套策略最残酷的压力测试——维持利率显软，意外加息恐慌，沃什的改革野心正走在最窄的钢丝上。"
  },
  {
    "id": "wscn:3778092",
    "domain": "股票",
    "title": "为什么中国企业AI落地更需要FDE",
    "url": "https://wallstreetcn.com/articles/3778092",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T02:56:41+00:00",
    "summary": "对今天的中国企业来说，模型似乎已不是AI落地中最明显的瓶颈。\n7月14日，月之暗面发布总参数2.8万..."
  },
  {
    "id": "wscn:3778090",
    "domain": "股票",
    "title": "英伟达CDS创纪录飙升，甲骨文遭降级——当“循环融资”撞上债券天花板",
    "url": "https://wallstreetcn.com/articles/3778090",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T02:34:48+00:00",
    "summary": "英伟达五年期CDS盘中创历史最大单日涨幅，甲骨文遭标普降级至BBB-、CDS升至215个基点，Alphabet自由现金流上市以来首次转负——AI“循环融资”引发的信贷市场信心危机正从英伟达向整个超大规模云服务商蔓延。债市压力已向股市传导，韩国KOSPI单日跌幅接近8%。"
  },
  {
    "id": "wscn:3778084",
    "domain": "股票",
    "title": "“救日元”的代价：日股会重演两年前的大跌吗？",
    "url": "https://wallstreetcn.com/articles/3778084",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T01:03:12+00:00",
    "summary": "2024年8月，TOPIX单月暴跌24%的噩梦仍历历在目。高盛分析师警告：尽管日元闪崩概率低于两年前，但当前日本股市的仓位拥挤程度已全面超越崩盘前水平——外资净头寸高出逾20%，对冲基金配置更达五年第99百分位。一旦AI叙事瓦解或地缘政治黑天鹅降临，这场风暴或比上次更猛烈。"
  },
  {
    "id": "wscn:3778087",
    "domain": "股票",
    "title": "AI硬件周期转折点：从\"烧钱扩张\"到\"算账扩产\"",
    "url": "https://wallstreetcn.com/articles/3778087",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T01:02:43+00:00",
    "summary": "华泰证券认为，AI硬件周期正从\"烧钱扩张\"转向理性算账：企业侧从\"多烧token\"转向核算投入产出；谷歌上调资本开支却引发股价下跌，投资人开始关注现金流质量而非规模；行业驱动力由涨价切换至扩产，存储涨价放缓成共识，分歧在2027年后走向。"
  },
  {
    "id": "wscn:3778085",
    "domain": "股票",
    "title": "中金：预期回稳阶段买什么？",
    "url": "https://wallstreetcn.com/articles/3778085",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T00:44:08+00:00",
    "summary": "A股低位回稳，悲观预期集中释放。中金研报指出，经历大幅回撤后，从上游黄金、锡到中游光伏、AI硬件，众多细分领域正显露“跌出来”的机遇。国内电网、创新药景气共振，年内二次买点或已浮现，924以来的震荡上行趋势有望延续。"
  },
  {
    "id": "wscn:3778075",
    "domain": "股票",
    "title": "市场“用脚投票”！给OpenAI担保2500亿美元，英伟达市值应声蒸发2500亿美元",
    "url": "https://wallstreetcn.com/articles/3778075",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T00:43:30+00:00",
    "summary": "英伟达正就为OpenAI提供2500亿美元财务担保进行磋商，并可能额外提供3500亿美元融资，用于OpenAI采购该数据中心所需芯片。这笔交易在华尔街交易员中引发强烈不安。不少人认为，这将成为AI循环融资狂潮走向顶点的标志性时刻。英伟达CDS价差单日飙升14个基点，股价重挫5%，市值蒸发约2500亿美元。"
  },
  {
    "id": "hn:48950580",
    "domain": "股票",
    "title": "SpaceX stock drops to a new low and loses $1T in value in a month",
    "url": "https://www.businessinsider.com/spacex-stock-drops-new-low-ipo-price-starship-launch-scrubbed-2026-7",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-07-17T18:26:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48984021",
    "domain": "股票",
    "title": "Mark Cuban: fight inequality by giving all workers company stock",
    "url": "https://fortune.com/2026/07/20/mark-cuban-income-inequality-company-stock-spacex-ipo-cost-plus-drugs/",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-07-20T19:52:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:49033778",
    "domain": "股票",
    "title": "Reality Bites Elon Musk and His Tesla, SpaceX Believers",
    "url": "https://www.wsj.com/finance/stocks/reality-bites-elon-musk-and-his-tesla-spacex-believers-1b639591",
    "source": "doener",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-24T10:59:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:48946872",
    "domain": "股票",
    "title": "US Corporate Insiders Are Selling Stocks at a Near Record Pace",
    "url": "https://www.bloomberg.com/news/articles/2026-07-17/us-corporate-insiders-are-selling-stocks-at-a-near-record-pace",
    "source": "pimienta",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-07-17T13:00:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:49012630",
    "domain": "股票",
    "title": "Alphabet Announces Second Quarter 2026 Results [pdf]",
    "url": "https://s206.q4cdn.com/479360582/files/doc_financials/2026/q2/2026q2-alphabet-earnings-release.pdf",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-07-22T20:04:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48958985",
    "domain": "股票",
    "title": "Traders are increasingly betting against SpaceX just weeks after IPO",
    "url": "https://www.ft.com/content/2b96703d-440b-46db-8d86-9fff9ecc59d5",
    "source": "ethanhawksley",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-07-18T15:26:13+00:00",
    "summary": ""
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
    "id": "hn:48907665",
    "domain": "股票",
    "title": "IBM is on pace for its worst day ever",
    "url": "https://www.cnn.com/2026/07/14/tech/ibm-stock-worst-day-ever",
    "source": "1970-01-01",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-07-14T14:39:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48974426",
    "domain": "股票",
    "title": "Big tech needs to justify AI spending as investors dump stocks",
    "url": "https://www.bloomberg.com/news/articles/2026-07-19/big-tech-needs-to-justify-ai-spending-as-investors-dump-stocks",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-07-20T04:41:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48923343",
    "domain": "股票",
    "title": "SpaceX stock sinks below $135 IPO price for the first time",
    "url": "https://www.cnbc.com/2026/07/15/spacex-spcx-stock-ipo-price.html",
    "source": "abduhl",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-07-15T16:30:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:49012394",
    "domain": "股票",
    "title": "We got California to intervene about OpenAI's corporate switch from nonprofit",
    "url": "https://fortune.com/2026/07/22/openai-foundation-class-n-stock-board-control-ipo/",
    "source": "SLHamlet",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-22T19:46:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48996223",
    "domain": "股票",
    "title": "The AI Bubble Is No Ordinary Bubble",
    "url": "https://www.theatlantic.com/ideas/2026/07/ai-economy-stock-market/688004/",
    "source": "gereshes",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-21T18:31:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48899454",
    "domain": "股票",
    "title": "$65K to work at Anthropic? Debate ensues amid IPO wave",
    "url": "https://missionlocal.org/2026/07/anthropic-sf-affordability-ipo-housing-evictions-rent/",
    "source": "gcheong",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-07-13T21:56:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48889982",
    "domain": "股票",
    "title": "Xbox CEO Asha Sharma, who laid off 3,200 employees, to lead task force on jobs",
    "url": "https://www.pcgamer.com/gaming-industry/us-federal-reserve-taps-xbox-ceo-asha-sharma-who-just-laid-off-3-200-employees-to-lead-task-force-on-jobs/",
    "source": "robtherobber",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-07-13T09:27:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48905958",
    "domain": "股票",
    "title": "IBM shares down 23% as clients spend more on hardware and memory chips",
    "url": "https://www.cnbc.com/2026/07/14/ibm-warns-second-quarter-earnings-fell-short-of-expectations.html",
    "source": "rvz",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-14T12:44:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:48947500",
    "domain": "股票",
    "title": "A.I. Is Running on Borrowed Money",
    "url": "https://www.nytimes.com/2026/07/17/business/ai-spending-oracle-stocks-bonds.html",
    "source": "ripe",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-17T14:01:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48962049",
    "domain": "股票",
    "title": "Elon Musk Runs from Interview at Last Minute as SpaceX Stock Crashed [video]",
    "url": "https://www.youtube.com/shorts/TFpF7ZzHc3w",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-18T20:30:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48787052",
    "domain": "股票",
    "title": "Elon Musk posted twice as often on UK race and immigration as about SpaceX IPO",
    "url": "https://www.theguardian.com/technology/2026/jul/04/elon-musk-uk-race-immigration-spacex-ipo",
    "source": "iamflimflam1",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-07-04T17:18:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48781228",
    "domain": "股票",
    "title": "After $18B IPO, Bending Spoons founder says success comes from minimizing luck",
    "url": "https://techcrunch.com/2026/07/01/after-18b-ipo-bending-spoons-founder-says-success-comes-from-minimizing-luck/",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-03T23:31:08+00:00",
    "summary": ""
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
    "id": "hn:48750160",
    "domain": "股票",
    "title": "Tech giants lose $2T in SpaceX's IPO month",
    "url": "https://english.elpais.com/economy-and-business/2026-07-01/tech-giants-lose-2-trillion-in-spacexs-ipo-month-the-valuations-were-unsustainable.html",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-07-01T17:14:01+00:00",
    "summary": ""
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
    "id": "hn:48717469",
    "domain": "金融",
    "title": "The CEO of Mullvad is the main financer of the Swedish Örebro party",
    "url": "https://det.social/@lostgen/116820546568940358",
    "source": "Risse",
    "platform": "hackernews",
    "points": 695,
    "published_at": "2026-06-29T10:45:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:48759634",
    "domain": "金融",
    "title": "PeerTube is a free, decentralized and federated video platform",
    "url": "https://github.com/Chocobozzz/PeerTube",
    "source": "doener",
    "platform": "hackernews",
    "points": 680,
    "published_at": "2026-07-02T11:17:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48915953",
    "domain": "金融",
    "title": "Stripe and Advent have made a joint offer to acquire PayPal – sources",
    "url": "https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/",
    "source": "rvz",
    "platform": "hackernews",
    "points": 494,
    "published_at": "2026-07-15T03:32:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49046525",
    "domain": "金融",
    "title": "The Fedora 45 Sausage Factory",
    "url": "https://supakeen.com/weblog/the-fedora-45-sausage-factory/",
    "source": "6581",
    "platform": "hackernews",
    "points": 155,
    "published_at": "2026-07-25T11:04:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:48878126",
    "domain": "金融",
    "title": "Under federal rule, colleges must leave grads better off or lose financial aid",
    "url": "https://www.npr.org/2026/06/30/nx-s1-5835631/turner-camhi-do-no-harm-college-loans",
    "source": "nradov",
    "platform": "hackernews",
    "points": 198,
    "published_at": "2026-07-12T04:00:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:48777266",
    "domain": "金融",
    "title": "International chess federation sanctions Kramnik",
    "url": "https://www.fide.com/fide-ethics-disciplinary-commission-issues-a-decision-in-case-involving-gm-vladimir-kramnik/",
    "source": "DarkContinent",
    "platform": "hackernews",
    "points": 169,
    "published_at": "2026-07-03T17:04:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48826703",
    "domain": "金融",
    "title": "Is The Economist Always Wrong?",
    "url": "https://www.economist.com/interactive/finance-and-economics/2026/07/02/is-the-economist-always-wrong",
    "source": "nreece",
    "platform": "hackernews",
    "points": 138,
    "published_at": "2026-07-08T02:17:01+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.23068",
    "domain": "金融",
    "title": "Neural Network-Driven Volatility Drag Mitigation under Aggressive Leverage",
    "url": "https://arxiv.org/abs/2607.23068",
    "source": "Christian Bongiorno, Efstratios Manolakis, Rosario Nunzio Mantegna",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.23068v1 Announce Type: new Abstract: This paper introduces a compact reformulation of a modular end-to-end neural network for global minimum-variance portfolio optimization that decouples m"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.23161",
    "domain": "金融",
    "title": "Risk Aversion in the Small and in the Large: Beyond Arrow-Pratt A Wiener Chaos Hierarchy of Dynamic Risk Premia",
    "url": "https://arxiv.org/abs/2607.23161",
    "source": "Christian Oliver Ewald",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.23161v1 Announce Type: new Abstract: The Arrow-Pratt approximation is one of the cornerstones of expected utility theory, providing the classical local approximation of certainty equivalent"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.23303",
    "domain": "金融",
    "title": "Ranking-based competitive balance measures in Formula One",
    "url": "https://arxiv.org/abs/2607.23303",
    "source": "D\\'ora Gr\\'eta Petr\\'oczy, L\\'aszl\\'o Csat\\'o",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.23303v1 Announce Type: new Abstract: Competitiveness in racing sports can be measured by comparing the start and finish rankings within races, as well as the start and finish rankings acros"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.23313",
    "domain": "金融",
    "title": "Agentic AI Orchestration of Heterogeneous Economic Models for Rapid, Multi-scenario Analysis of Energy Crises",
    "url": "https://arxiv.org/abs/2607.23313",
    "source": "Dana Golden, Brett Indelicato, Lav R. Varshney, Carlos D. Messina, Suzanne Thornsbury",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.23313v1 Announce Type: new Abstract: Rigorous economic models can take months to construct, yet energy crises demand decisions from policymakers within days or even hours. Any disruption in"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.23325",
    "domain": "金融",
    "title": "Happy Birthday? Age Labels, Search Criteria, and Matching from Dating to Marriage",
    "url": "https://arxiv.org/abs/2607.23325",
    "source": "Suguru Otani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.23325v1 Announce Type: new Abstract: Age is a match trait and a prominent label on search platforms. Using confidential records from a large Japanese marriage platform, I study how a birthd"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.23424",
    "domain": "金融",
    "title": "Wrong and More Confident: A Field Experiment on Language Models Taking a Graduate Economics Exam",
    "url": "https://arxiv.org/abs/2607.23424",
    "source": "Piyush Akimitsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.23424v1 Announce Type: new Abstract: A red herring, an irrelevant passage added to a problem, makes a language model reason incorrectly and answer incorrectly far more often. Yet the model "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.23426",
    "domain": "金融",
    "title": "Do Carbon Price Forecasts Improve Compliance Procurement? Evidence from European Union Allowances",
    "url": "https://arxiv.org/abs/2607.23426",
    "source": "Muzi Chen, Difang Huang, Shouyang Wang, Xinghan Xia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.23426v1 Announce Type: new Abstract: Firms covered by emissions trading systems need forecasts not only to value allowances, but also to decide when to buy them. This paper asks whether Eur"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.24150",
    "domain": "金融",
    "title": "Approximation of stochastic insurer balance-sheet results using signatures of economic scenarios",
    "url": "https://arxiv.org/abs/2607.24150",
    "source": "Herv\\'e Andr\\`es, Alexandre Boumezoued, Arthur Bourdon, Benjamin Jourdain",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.24150v1 Announce Type: new Abstract: In the insurance industry, Asset and Liability Management (ALM) models are key tools for numerous applications, including Solvency Capital Requirement ("
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.24175",
    "domain": "金融",
    "title": "A World of Ginis",
    "url": "https://arxiv.org/abs/2607.24175",
    "source": "Lidia Ceriani, Paolo Verme",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.24175v1 Announce Type: new Abstract: The Gini index remains the most important measure of economic inequality worldwide, and accurate estimates of this index are essential for effective pub"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.24372",
    "domain": "金融",
    "title": "Randomness in large language models: What researchers need to know (and report)",
    "url": "https://arxiv.org/abs/2607.24372",
    "source": "Guillaume Coqueret, Joan Llull, Florian Oswald, Christophe P\\'erignon, Christoph Scheuch, Lars Vilhuber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.24372v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly used to generate data for research. Typical use cases are classifications, annotations, information extrac"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.24389",
    "domain": "金融",
    "title": "How to Disrupt a Market",
    "url": "https://arxiv.org/abs/2607.24389",
    "source": "Edoardo Gallo, Rebecca Heath, Jonathan Lusthaus, Federico Varese",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.24389v1 Announce Type: new Abstract: Market design research in economics naturally focusses on how to improve market efficiency. Our objective here is exactly the opposite - how to design i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.24410",
    "domain": "金融",
    "title": "The Fundamental Structure of Risk: From Characteristics to Covariance",
    "url": "https://arxiv.org/abs/2607.24410",
    "source": "Alexandre Alouadi, Charles-Albert Lehalle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.24410v1 Announce Type: new Abstract: Estimating the covariance structure of financial assets typically relies on his- torical returns, making risk models dependent on noisy and asset-specif"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.24680",
    "domain": "金融",
    "title": "One Other Option Pricing Scheme",
    "url": "https://arxiv.org/abs/2607.24680",
    "source": "Jimin Lin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.24680v1 Announce Type: new Abstract: We present a distinctive approach to parameterizing the risk neutral distribution. Using parsimonious and interpretable parameters, the model provides d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.28031",
    "domain": "金融",
    "title": "Insurance risk models in a heterogeneous time-dependent population: scaling limits and ruin probabilities",
    "url": "https://arxiv.org/abs/2606.28031",
    "source": "H\\'el\\`ene Gu\\'erin, Michel Mandjes, Jean-Fran\\c{c}ois Renaud, Arsene Brice Zotsa Ngoufack",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2606.28031v1 Announce Type: cross Abstract: Epidemic dynamics introduce time-varying heterogeneity into insured populations, as individuals' risk profiles depend on their evolving health status,"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.23733",
    "domain": "金融",
    "title": "AI Strategy: How to Choose What AI Product to Implement",
    "url": "https://arxiv.org/abs/2607.23733",
    "source": "Foster Provost, Panos Ipeirotis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.23733v1 Announce Type: cross Abstract: Firms struggle to choose AI projects that pay off: two projects can look equally promising to smart, motivated stakeholders and yet deserve opposite d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.24065",
    "domain": "金融",
    "title": "Variational Quantum Conditional Boltzmann Machines for Time-Series Forecasting: Architectures, Symmetric Hyperparameter Evaluation, and a Nonlinear Benchmark",
    "url": "https://arxiv.org/abs/2607.24065",
    "source": "Gerhard Hellstern, Danyal Maheshwari, Martin Zaefferer, Martin Braun, Tanja D\\\"ohler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.24065v1 Announce Type: cross Abstract: In this study, we developed and evaluated four conditional energy-based forecasting architectures: a classical Gaussian-Bernoulli CRBM, a hybrid quant"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.24114",
    "domain": "金融",
    "title": "Optimal Control with Expectation Constraint in a Smooth Boundary Case",
    "url": "https://arxiv.org/abs/2607.24114",
    "source": "Bruno Bouchard (CEREMADE), Lucas Gnecco Heredia (LAMSADE), Ludovic Moreau (CEREMADE), Kim-Anh Pham (CEREMADE)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.24114v1 Announce Type: cross Abstract: As in Bouchard et al. (2010) and Bouchard and Nutz (2014), we study a utility maximization problem with expectation constraint. We first consider a un"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.05080",
    "domain": "金融",
    "title": "MM-ARC: Multimodal Adaptive Routing of Capital with Robustness-Audited Strategy Pools",
    "url": "https://arxiv.org/abs/2509.05080",
    "source": "Yang Chen, Yuchen Cao, Jacky Keung, Leilei Gan, Kun Kuang, Yueheng Jiang, Zhaozhao Ma, Jianping Zhu, Fei Wu, Jinpeng Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2509.05080v3 Announce Type: replace Abstract: Financial trading systems must convert multimodal market history into executable positions while limiting overfitting from repeated strategy search."
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.14774",
    "domain": "金融",
    "title": "The unintended effects of universalizing social pensions: Evidence from Mexico",
    "url": "https://arxiv.org/abs/2602.14774",
    "source": "Oscar Galvez-Soriano, Raymundo Ramirez Peralta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2602.14774v2 Announce Type: replace Abstract: We examine the effects of the 2019 expansion of Mexico's Social Pension Program. This reform simultaneously increased benefit generosity and expande"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.20406",
    "domain": "金融",
    "title": "Bond Market Making with a Hit-Ratio Target",
    "url": "https://arxiv.org/abs/2604.20406",
    "source": "Alexander Barzykin, Axel Ciceri",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2604.20406v2 Announce Type: replace Abstract: We study OTC bond market making on a size ladder with quadratic inventory penalty and a running target on the dealer's size-weighted hit ratio withi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.15614",
    "domain": "金融",
    "title": "Type-Specific Wages as a Distributional Buffer in TANK",
    "url": "https://arxiv.org/abs/2605.15614",
    "source": "Kenji Miyazaki",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2605.15614v2 Announce Type: replace Abstract: How does type-specific wage adjustment change the cross-type incidence of aggregate shocks? The model maintains that financial type coincides with a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.12893",
    "domain": "金融",
    "title": "Technology Shocks, Relative Performance Measures, and Outcomes: Evidence from Classical Chess",
    "url": "https://arxiv.org/abs/2606.12893",
    "source": "Dan Ben-Moshe, David Genesove",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2606.12893v2 Announce Type: replace Abstract: In the fall of 2020, neural-network methods produced a large improvement in chess engines that became freely and widely available. By the end of 202"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.19562",
    "domain": "金融",
    "title": "The Direct and Indirect Effects of Genetics and Education",
    "url": "https://arxiv.org/abs/2607.19562",
    "source": "Senan Hogan-Hennessy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.19562v3 Announce Type: replace Abstract: Genes associated with educational attainment causally improve labour market income, but the economic mechanism behind this relationship is not clear"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.19929",
    "domain": "金融",
    "title": "Bounded Attention and Attenuated Elasticities",
    "url": "https://arxiv.org/abs/2607.19929",
    "source": "Tingmingke Lu, Zhenyi Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2607.19929v2 Announce Type: replace Abstract: We study how bounded attention affects the structural estimation of the elasticity of substitution. In a sparse-max model, equilibrium prices and ex"
  },
  {
    "id": "rss:https://arxiv.org/abs/2306.05433",
    "domain": "金融",
    "title": "Equilibrium in Functional Stochastic Games with Mean-Field Interaction",
    "url": "https://arxiv.org/abs/2306.05433",
    "source": "Eduardo Abi Jaber, Eyal Neuman, Moritz Vo{\\ss}",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2306.05433v3 Announce Type: replace-cross Abstract: We consider a general class of finite-player stochastic games with mean-field interaction, in which the linear-quadratic cost functional inclu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.25001",
    "domain": "金融",
    "title": "Cylindrical Projections of Occupied Diffusions",
    "url": "https://arxiv.org/abs/2604.25001",
    "source": "Valentin Tissot-Daguette, Xin Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T04:00:00+00:00",
    "summary": "arXiv:2604.25001v2 Announce Type: replace-cross Abstract: Occupied diffusions offer a Markovian framework for path-dependent dynamics by lifting the state space with a flow of occupation measures. Bec"
  },
  {
    "id": "hn:48735748",
    "domain": "金融",
    "title": "Supreme Court takes sledgehammer to federal regulatory structure",
    "url": "https://www.npr.org/2026/06/29/nx-s1-5875161/supreme-court-takes-sledgehammer-to-much-of-federal-governments-regulatory-structure",
    "source": "marojejian",
    "platform": "hackernews",
    "points": 83,
    "published_at": "2026-06-30T17:05:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49024958",
    "domain": "金融",
    "title": "DOT cranks up its campaign to strip bike lane references from federal websites",
    "url": "https://text.npr.org/nx-s1-5900901",
    "source": "Jtsummers",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-07-23T17:11:39+00:00",
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
  },
  {
    "id": "hn:48783175",
    "domain": "金融",
    "title": "The LLVM Compiler Infrastructure",
    "url": "https://cacm.acm.org/federal-funding-of-academic-research/the-llvm-compiler-infrastructure/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 80,
    "published_at": "2026-07-04T06:43:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:48884775",
    "domain": "金融",
    "title": "Storm clouds gather over America's financial supremacy",
    "url": "https://www.economist.com/finance-and-economics/2026/07/12/storm-clouds-gather-over-americas-financial-supremacy",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-07-12T21:04:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48785077",
    "domain": "金融",
    "title": "The Fediverse Is Not the Way Forward",
    "url": "https://trialandfailure.net/the-fediverse-is-not-the-way-forward/",
    "source": "ExMachina73",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-07-04T12:53:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:48734220",
    "domain": "金融",
    "title": "Supreme Court strikes down limits on party spending in federal elections",
    "url": "https://apnews.com/article/supreme-court-campaign-finance-party-spending-ohio-91e49ee112197ae1210a9abfa46986ed",
    "source": "khriss",
    "platform": "hackernews",
    "points": 67,
    "published_at": "2026-06-30T15:34:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:48756848",
    "domain": "金融",
    "title": "He sent a harsh email to ICE's top official. Federal agents tracked him down",
    "url": "https://www.npr.org/2026/07/01/nx-s1-5874124/dhs-tracks-ice-critic",
    "source": "OutOfHere",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-07-02T05:20:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:48999329",
    "domain": "金融",
    "title": "A Man Who Runs the IRS Spied on Colleagues When He Worked at JPMorgan",
    "url": "https://www.wsj.com/finance/banking/irs-bisignano-spying-jpmorgan-6cd1ddf0",
    "source": "cwwc",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-07-21T22:40:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:49001708",
    "domain": "金融",
    "title": "Tesla Balance Bike",
    "url": "https://shop.tesla.com/product/balance-bike-for-kids",
    "source": "surprisetalk",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-22T04:00:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48986112",
    "domain": "金融",
    "title": "The Fedora project grapples with change",
    "url": "https://lwn.net/SubscriberLink/1081557/cde56e450fe4bf10/",
    "source": "chmaynard",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-20T23:17:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48791799",
    "domain": "金融",
    "title": "Is The Economist Always Wrong?",
    "url": "https://economist.com/interactive/finance-and-economics/2026/07/02/is-the-economist-always-wrong",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 59,
    "published_at": "2026-07-05T06:40:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48999988",
    "domain": "金融",
    "title": "Brazil and US clash over future of payments as Pix system stirs global interest",
    "url": "https://www.reuters.com/business/finance/brazil-us-clash-over-future-payments-popular-pix-system-stirs-global-interest-2026-07-21/",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-21T23:52:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48986211",
    "domain": "金融",
    "title": "Delayed Boeing jets only fit for baked bean tins, Emirates boss says",
    "url": "https://finance.yahoo.com/technology/articles/delayed-boeing-jets-only-fit-162341761.html",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-20T23:29:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49028304",
    "domain": "金融",
    "title": "US announces double-digit tariffs on most of globe to replace expiring duties",
    "url": "https://finance.yahoo.com/economy/policy/article/trump-administration-announces-the-next-phase-of-global-tariffs-with-10-to-125-rates-on-much-of-the-globe-210032314.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-23T21:28:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48953857",
    "domain": "金融",
    "title": "Nadella Blasts AI Industry's Double Standard",
    "url": "https://finance.biggo.com/news/438f299b-ca23-468d-b37d-0ffe09a4ca55",
    "source": "nittanymount",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-07-18T00:28:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:48754128",
    "domain": "金融",
    "title": "US feds are actively hiring \"person who decides which models to ban\"",
    "url": "https://www.usajobs.gov/job/856265200",
    "source": "arm32",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-07-01T22:45:41+00:00",
    "summary": ""
  }
]
```
