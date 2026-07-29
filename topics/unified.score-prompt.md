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

- 今日日期：`2026-07-29`
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
  "date": "2026-07-29",
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
    "points": 3967476,
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
    "points": 1624660,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1500177,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1289968,
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
    "points": 1005874,
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
    "points": 990076,
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
    "points": 970736,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 573419,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 429466,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1gV5v6HEVG",
    "domain": "AI",
    "title": "同样是服务器！为啥绝密服务器是大红，阵列服务器只配当大金？",
    "url": "http://www.bilibili.com/video/av116577894669157",
    "source": "游戏推推棒",
    "platform": "bilibili",
    "points": 422105,
    "published_at": "2026-05-15T09:33:43+00:00",
    "summary": "绝密服务器，主播到现在都还没摸到了，服了！"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 418825,
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
    "points": 417952,
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
    "points": 356543,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1ahFmzqE9z",
    "domain": "AI",
    "title": "【2026版Agent Skills保姆级教程】2小时从会用到会造，全方位提升工作效率。Claude Skills、Agent技能、OpenCode",
    "url": "http://www.bilibili.com/video/av116044177936465",
    "source": "博学谷",
    "platform": "bilibili",
    "points": 281368,
    "published_at": "2026-02-10T03:28:31+00:00",
    "summary": "视频配套资源领取方式戳：https://www.bilibili.com/opus/1167610370075918393\n或关注博学谷公综号领取，回复关键词：0102\n============================\n学完本课程，就能通过现有的Skill技能让你的AI更聪明，更能干，更可靠，全方位提升工作效率，还可以根据自己需要造出自己想要的skill，用AI 360°武装自己，直接从小"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 250608,
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
    "points": 209580,
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
    "points": 187907,
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
    "points": 178048,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 162656,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 120562,
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
    "points": 110519,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1EVuqzrEMJ",
    "domain": "AI",
    "title": "【保姆级教程】手把手教你低成本制作AI女友，【一定要看置顶评论】，可随身携带，自由对话",
    "url": "http://www.bilibili.com/video/av114851468812000",
    "source": "往生堂研发",
    "platform": "bilibili",
    "points": 110297,
    "published_at": "2025-07-14T12:03:53+00:00",
    "summary": "文档地址\nhttps://github.com/xinnan-tech/xiaozhi-esp32-server/blob/main/docs/Deployment.md?_refluxos=a10#%E6%96%B9%E5%BC%8F%E4%B8%80docker%E5%8F%AA%E8%BF%90%E8%A1%8Cserver"
  },
  {
    "id": "bvid:BV1t9oZBDENp",
    "domain": "AI",
    "title": "Agent Loop: 多智能体协同，让AI长时工作，从原理到实践",
    "url": "http://www.bilibili.com/video/av116469396413175",
    "source": "费曼学徒冬瓜",
    "platform": "bilibili",
    "points": 105929,
    "published_at": "2026-04-26T12:00:00+00:00",
    "summary": "睡前给AI丢了一句话，醒来直接验收成果——怎么让AI连续干活几小时不拉胯？\n这期我们从原理到实战，彻底讲清楚 Harness 工程：让 AI 长时间自主工作的核心技术。\n内容涵盖两种方案：\nRalph 方案：用 while 循环不断启动新会话，通过文件系统衔接上下文\n多智能体方案（推荐）：主 Agent 只协调不干活，子 Agent 各司其职，开发测试分工明确\n重点讲了多智能体的完整流程设计：怎么"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92821,
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
    "points": 86450,
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
    "points": 73917,
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
    "points": 53409,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1RrZHYqEvm",
    "domain": "AI",
    "title": "Cursor+Figma MCP，自动生成可编辑设计稿",
    "url": "http://www.bilibili.com/video/av114257538650701",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 52381,
    "published_at": "2025-03-31T14:36:31+00:00",
    "summary": "分享了两种Figma MCP。一种是通过获取Figma API key来实现Cursor和Figma的连接，更侧重精准控制。\n.\n因为大多数 Figma 文件都会非常大，如果你想让Cursor精准链接到文件中的特定元素，一般选择这个MCP会更合适。\n.\n另一种则是通过Figma插件形式，通过channel实现与Cursor的连接，更侧重从0到1的设计元素生成，比较适合没有太多设计基础的用户。\n.\n"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47508,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1HaN162EPT",
    "domain": "AI",
    "title": "【Codex】2026最新Codex保姆级教程，ChatGPT + Codex 开发实战全流程，环境配置、核心功能、使用技巧到项目实战一学就会，少走99%弯路！",
    "url": "http://www.bilibili.com/video/av116911660665280",
    "source": "今天AI了吗",
    "platform": "bilibili",
    "points": 46994,
    "published_at": "2026-07-13T09:01:50+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 45571,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 44406,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1FzfoYSE4f",
    "domain": "AI",
    "title": "影刀AI Power零基础教程：02 智能体——打造企业AI超级员工",
    "url": "http://www.bilibili.com/video/av113888003622214",
    "source": "影刀RPA",
    "platform": "bilibili",
    "points": 41099,
    "published_at": "2025-02-06T02:00:00+00:00",
    "summary": "AI智能体：场景化智能助手，打造企业AI超级员工\n影刀AI Power，帮助企业将AI用起来。让每个员工都能拥有AI能力，在工作中使用AI解决问题。\n\n影刀AP企业版免费试用申请：http://s.winrobot360.com/g02tp\n影刀AP社区版使用：https://www.yingdao.com/ai-power/"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 39347,
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
    "points": 37819,
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
    "points": 35024,
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
    "points": 33952,
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
    "points": 29509,
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
    "points": 25765,
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
    "points": 22660,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1XxXpBEEHU",
    "domain": "AI",
    "title": "Claude Code远程开发终极方案！手机改代码+实时预览~【小白教程】",
    "url": "http://www.bilibili.com/video/av116294326230438",
    "source": "爱听书的程序员阿超",
    "platform": "bilibili",
    "points": 22107,
    "published_at": "2026-03-26T12:00:00+00:00",
    "summary": "之前，我一直在研究怎么远程使用 Claude Code 开发项目，并且能实时预览效果。但是一直都没有找到合适的解决方案，要么就是给一个临时公网链接预览，每次都需要再配置，要么就是购买云服务器来配置，都感觉挺麻烦的~\n\n最近，我发现这个蒲公英异地组网的方案，用来做远程开发 Claude Code 项目，感觉非常方便，不仅能修改代码，而且我实时预览的需求也很好的满足了。\n\n这样我随时随地都可以用 AI"
  },
  {
    "id": "bvid:BV16ggC6DEZK",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116963049212769",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 21460,
    "published_at": "2026-07-22T10:10:42+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17650,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 16872,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV15phrzqEzK",
    "domain": "AI",
    "title": "【Claude Code Router】一键直连五大模型",
    "url": "http://www.bilibili.com/video/av115121162553281",
    "source": "她笑中藏泪花",
    "platform": "bilibili",
    "points": 16948,
    "published_at": "2025-08-31T03:09:22+00:00",
    "summary": "Claude Code Router 教程：手把手完成 CCR 配置与 PROXY_URL 代理，一次直连 Gemini、Kimi、DeepSeek、GLM、Qwen，区分 Anthropic 与 OpenAI 端点，并附 /model 切换与报错速查。点击查看。\n博文链接：https://rosetears.cn/archives/61/"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 16114,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 15762,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "7月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "iwenwikii",
    "platform": "bilibili",
    "points": 12897,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "AI充值站：njzqhy.top"
  },
  {
    "id": "bvid:BV1vLN769EJa",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！大模型入门到进阶，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116894866677118",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 12848,
    "published_at": "2026-07-10T09:04:48+00:00",
    "summary": "【代码已整理】\n无论你是从零开始开发项目，还是对现有代码进行现代化改造，本课程都能为你提供一套严谨的工作流程，让你按自己的方式构建软件。"
  },
  {
    "id": "bvid:BV11EJn6JEk9",
    "domain": "AI",
    "title": "claude+ccswitch配置glm5.2",
    "url": "http://www.bilibili.com/video/av116742495999581",
    "source": "cctryflow",
    "platform": "bilibili",
    "points": 12724,
    "published_at": "2026-06-13T11:13:45+00:00",
    "summary": "智谱文档：https://docs.bigmodel.cn/cn/coding-plan/latest-model"
  },
  {
    "id": "hn:49035303",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, Microsoft, Meta warn against overregulating open-weight models",
    "url": "https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 657,
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
    "id": "hn:49084371",
    "domain": "AI 算力 / 半导体",
    "title": "Show HN: Tines 3B – safe workflow automation for when everyone builds software",
    "url": "https://www.tines.com/",
    "source": "retsol",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-07-28T14:23:55+00:00",
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
    "points": 16,
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
    "points": 15,
    "published_at": "2026-07-27T20:35:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:49093429",
    "domain": "AI 算力 / 半导体",
    "title": "Kospi Plunges After Nvidia CEO's Visits Spark 'Huang Curse' Fears",
    "url": "https://www.chosun.com/english/market-money-en/2026/07/29/6FEUZWQT5BG3HMJ3G2RZPHROGM/",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-07-29T04:29:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49069995",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia investing to 10x SSI compute in the next 12 months",
    "url": "https://twitter.com/ssi/status/2081732119194394763",
    "source": "primaprashant",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-07-27T14:11:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49068730",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Launches Open Secure AI Alliance",
    "url": "https://blogs.nvidia.com/blog/open-secure-ai-alliance/",
    "source": "BlueBerry2001",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-27T12:31:17+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/microchip-acquires-edge-ai-chip-startup-hailo/",
    "domain": "AI 算力 / 半导体",
    "title": "Microchip Acquires Edge AI Chip Startup Hailo",
    "url": "https://www.eetimes.com/microchip-acquires-edge-ai-chip-startup-hailo/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T17:04:30+00:00",
    "summary": "Return to playbook for the acquisition-driven embedded giant. The post Microchip Acquires Edge AI Chip Startup Hailo appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/how-to-build-a-100gbps-server-grade-aoi-platform-for-next-generation-semiconductor-inspection/",
    "domain": "AI 算力 / 半导体",
    "title": "How to Build a 100Gbps Server-Grade AOI Platform for Next-Generation Semiconductor Inspection",
    "url": "https://www.eetimes.com/how-to-build-a-100gbps-server-grade-aoi-platform-for-next-generation-semiconductor-inspection/",
    "source": "ADLINK",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T14:00:00+00:00",
    "summary": "Discover how to overcome the bandwidth, scalability, thermal, and system integration challenges of modern AI-powered AOI. This white paper explains how server-grade architecture, high-speed frame grab"
  },
  {
    "id": "rss:https://www.eetimes.com/vibe-coding-in-safety-critical-software-promise-pitfalls-and-a-path-forward/",
    "domain": "AI 算力 / 半导体",
    "title": "Vibe Coding in Safety-Critical Software: Promise, Pitfalls, and a Path Forward",
    "url": "https://www.eetimes.com/vibe-coding-in-safety-critical-software-promise-pitfalls-and-a-path-forward/",
    "source": "Miroslaw Zielinski, director of product management, Parasoft.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T13:52:38+00:00",
    "summary": "Vibe coding can’t fly solo in safety-critical software; demand deterministic gates, human review, and proof before trusting AI-generated code. The post Vibe Coding in Safety-Critical Software: Promise"
  },
  {
    "id": "rss:https://www.eetimes.com/will-purging-chinese-tech-cost-europe-its-digital-future/",
    "domain": "AI 算力 / 半导体",
    "title": "Will Purging Chinese Tech Cost Europe Its Digital Future?",
    "url": "https://www.eetimes.com/will-purging-chinese-tech-cost-europe-its-digital-future/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T08:19:26+00:00",
    "summary": "The EU faces challenges in building its digital defenses, as the cost of replacing Chinese telecom equipment across Europe could reach $46 billion. The post Will Purging Chinese Tech Cost Europe Its D"
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
    "id": "rss:https://www.tomshardware.com/laptops/an-affordable-oled-laptop-for-just-usd699-acers-swift-go-16-ai-back-to-school-deal",
    "domain": "AI 算力 / 半导体",
    "title": "An affordable OLED laptop for just $699 — Acer's Swift Go 16 AI is the perfect back-to-school deal",
    "url": "https://www.tomshardware.com/laptops/an-affordable-oled-laptop-for-just-usd699-acers-swift-go-16-ai-back-to-school-deal",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T16:53:03+00:00",
    "summary": "Get ready to head back to school with this $300 saving on Acer's excellent Swift Go 16 AI laptop with an OLED screen."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/mystery-reviewer-finds-nvidia-rtx-spark-prototype-laptop-and-puts-it-through-its-paces-microsoft-surface-laptop-ultra-with-nvidia-n1x-chip-shows-promise-though-prototype-warts-are-still-quite-visible",
    "domain": "AI 算力 / 半导体",
    "title": "Mystery reviewer 'finds' Nvidia RTX Spark prototype laptop and puts it through its paces — Microsoft Surface Laptop Ultra with Nvidia N1X chip shows promise, though prototype warts are still quite vis",
    "url": "https://www.tomshardware.com/laptops/mystery-reviewer-finds-nvidia-rtx-spark-prototype-laptop-and-puts-it-through-its-paces-microsoft-surface-laptop-ultra-with-nvidia-n1x-chip-shows-promise-though-prototype-warts-are-still-quite-visible",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T16:03:23+00:00",
    "summary": "Techie \"finds\" Nvidia RTX Spark prototype laptop and puts it through its paces — Microsoft Surface Laptop Ultra with Nvidia N1X chip shows promise, though prototype warts are still quite visible"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/sam-altman-says-ai-has-entered-the-singularity",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI CEO Sam Altman says AI has entered the singularity — two weeks after OpenAI models cheated a benchmark by hacking Hugging Face",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/sam-altman-says-ai-has-entered-the-singularity",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T14:56:22+00:00",
    "summary": "OpenAI CEO Sam Altman recently declared on the Relentless podcast that artificial intelligence has entered the technological singularity."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/one-year-into-the-ai-induced-ram-apocalypse-how-much-does-memory-actually-cost-and-is-there-hope-for-a-more-affordable-future",
    "domain": "AI 算力 / 半导体",
    "title": "One year into the AI-induced RAM apocalypse — how much does memory actually cost, and is there hope for a more affordable future?",
    "url": "https://www.tomshardware.com/pc-components/ram/one-year-into-the-ai-induced-ram-apocalypse-how-much-does-memory-actually-cost-and-is-there-hope-for-a-more-affordable-future",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T14:24:28+00:00",
    "summary": "We look at the state of the DIY RAM market over the last 12 months."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/apple-launches-official-program-for-leasing-macs-as-ai-price-crunch-bites-24-and-36-month-leasing-options-provided-by-klarna",
    "domain": "AI 算力 / 半导体",
    "title": "Apple launches official program for leasing Macs as AI price crunch bites — 24- and 36-month leasing options provided by Klarna",
    "url": "https://www.tomshardware.com/laptops/macbooks/apple-launches-official-program-for-leasing-macs-as-ai-price-crunch-bites-24-and-36-month-leasing-options-provided-by-klarna",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T14:23:59+00:00",
    "summary": "Apple launched its Upgrade program in the US, a partnership with Klarna to lease Macs along with iPads, Watches, and iPhones."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/the-neo-geo-aes-retro-console-is-now-available-to-pre-order-starting-from-usd249-game-cartridges-cost-usd90-each-the-ultimate-edition-with-all-games-and-accessories-will-run-you-usd1-000",
    "domain": "AI 算力 / 半导体",
    "title": "The Neo Geo AES+ retro console is now available to pre-order starting from $249 — game cartridges cost $90 each; the Ultimate Edition with all games and accessories will run you $1,000",
    "url": "https://www.tomshardware.com/video-games/console-gaming/the-neo-geo-aes-retro-console-is-now-available-to-pre-order-starting-from-usd249-game-cartridges-cost-usd90-each-the-ultimate-edition-with-all-games-and-accessories-will-run-you-usd1-000",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T13:52:49+00:00",
    "summary": "How far are you willing to go for physical media? That's the question the Neo Geo AES+ asks above anything else, given the $90 price tags of its game cartridges. Though, comparing it to its original p"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/acer-prodesigner-pe320qxt-professional-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Acer ProDesigner PE320QXT professional monitor review: Touchscreen functionality with a 6K resolution",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/acer-prodesigner-pe320qxt-professional-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T13:30:00+00:00",
    "summary": "Acer takes a unique approach to professional displays with its ProDesigner PE320QXT. It’s a 6K 6016x3384 IPS panel with a touchscreen, webcam, tablet-style stand and a large color gamut for content cr"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/motherboard-vrm-thermal-testing-budget-vs-high-end-boards-does-it-really-matter",
    "domain": "AI 算力 / 半导体",
    "title": "Motherboard VRM thermal testing – budget vs. high-end boards, does it really matter?",
    "url": "https://www.tomshardware.com/pc-components/motherboards/motherboard-vrm-thermal-testing-budget-vs-high-end-boards-does-it-really-matter",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T12:43:16+00:00",
    "summary": "Not all motherboard VRMs are created equal. We break down the differences between budget and premium designs, how they can affect CPU performance, and whether paying more is actually worth it."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/testing-old-drives-as-external-storage-to-avoid-price-hikes-hard-drive-sata-ssd-and-nvme-in-enclosures-up-to-80-gbps-tested",
    "domain": "AI 算力 / 半导体",
    "title": "Testing old drives as external storage to avoid price hikes — hard drive, SATA SSD, and NVMe in enclosures up to 80 Gbps, tested",
    "url": "https://www.tomshardware.com/pc-components/storage/testing-old-drives-as-external-storage-to-avoid-price-hikes-hard-drive-sata-ssd-and-nvme-in-enclosures-up-to-80-gbps-tested",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T11:39:52+00:00",
    "summary": "For as little as $10 (or less on sale), you can use an old drive as external storage, but will that dusty drive deliver the speed you need?"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd1-000-on-this-rtx-5090-gaming-pc-from-msi-just-17-percent-more-than-the-gpus-standalone-cost-right-now-score-this-4k-powerhouse-with-64gb-ddr5-and-a-2tb-ssd-for-usd4-899",
    "domain": "AI 算力 / 半导体",
    "title": "Save $1,000 on this RTX 5090 gaming PC from MSI, just 17% more than the GPU's standalone cost right now —score this 4K powerhouse with 64GB DDR5 and a 2TB SSD for $4,899",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd1-000-on-this-rtx-5090-gaming-pc-from-msi-just-17-percent-more-than-the-gpus-standalone-cost-right-now-score-this-4k-powerhouse-with-64gb-ddr5-and-a-2tb-ssd-for-usd4-899",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T11:36:14+00:00",
    "summary": "Save $1,000 on this MSI Aegis R2 gaming PC, fitted with an RTX 5090, 64GB DDR5, and 2TB SSD for just $4,899."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/xbox/xbox-blames-a-licensing-service-outside-xbox-for-the-16-hour-outage-that-blocked-disc-games",
    "domain": "AI 算力 / 半导体",
    "title": "16-hour Xbox outage even stopped physical games from working — company blames licensing issue for incident that prohibited gaming across three generations of console",
    "url": "https://www.tomshardware.com/video-games/xbox/xbox-blames-a-licensing-service-outside-xbox-for-the-16-hour-outage-that-blocked-disc-games",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T11:31:17+00:00",
    "summary": "Xbox CTO Scott Van Vliet said that a licensing service sitting outside Xbox, which the platform depends on, began failing late on July 26 and took roughly 16 hours to clear."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/alphabet-goes-cash-flow-negative-for-the-first-time-as-ai-capex-doubles-to-44-9-billion-in-a-single-quarter",
    "domain": "AI 算力 / 半导体",
    "title": "Google goes cash flow negative for the first time as AI data center buildout increases capex to a staggering $44.9 billion in a single quarter — CFO warns that capex will increase in 2027 as company b",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/alphabet-goes-cash-flow-negative-for-the-first-time-as-ai-capex-doubles-to-44-9-billion-in-a-single-quarter",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T11:12:23+00:00",
    "summary": "On the same day, CFO Anat Ashkenazi raised full-year capex guidance to between $195 billion and $205 billion."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/crealitys-multicolor-k2-3d-printer-hits-an-all-time-low-price-of-usd499-save-usd200-today-with-the-perfect-printer-for-jumping-into-the-hobby",
    "domain": "AI 算力 / 半导体",
    "title": "Creality's multicolor K2 3D printer hits an all-time low price of $499 — save $200 today, with the perfect printer for jumping into the hobby",
    "url": "https://www.tomshardware.com/3d-printing/crealitys-multicolor-k2-3d-printer-hits-an-all-time-low-price-of-usd499-save-usd200-today-with-the-perfect-printer-for-jumping-into-the-hobby",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T11:11:23+00:00",
    "summary": "Save $200 on the Creality K2 Combo 3D printer bundle in Creality's Mega Summer Sales event."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/leaked-radeon-rx-9050-hints-at-the-return-of-4gb-vram-gpus-in-2026-new-budget-rdna-4-card-also-spotted-in-8gb-config-with-half-the-power-of-an-rx-9060",
    "domain": "AI 算力 / 半导体",
    "title": "ASRock officially announces Radeon RX 9050 with 8GB VRAM — RDNA 4 card offers boost clock of up to 2600MHz (updated)",
    "url": "https://www.tomshardware.com/pc-components/gpus/leaked-radeon-rx-9050-hints-at-the-return-of-4gb-vram-gpus-in-2026-new-budget-rdna-4-card-also-spotted-in-8gb-config-with-half-the-power-of-an-rx-9060",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T11:00:22+00:00",
    "summary": "ASRock has listed the long-rumored RX 9050 GPU on its website in both a 4GB and 8GB configuration, but has deleted those pages since."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/nvidias-taipei-office-searched-as-taiwan-detains-employee-in-ai-chip-smuggling-probe",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia employee detained in Taiwan as part of chip smuggling probe — held on suspicion of falsifying business documents, company says smuggling 'a nonstarter'",
    "url": "https://www.tomshardware.com/tech-industry/nvidias-taipei-office-searched-as-taiwan-detains-employee-in-ai-chip-smuggling-probe",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T10:34:07+00:00",
    "summary": "Taiwan's prosecutors say they've detained a man surnamed Chang on suspicion of falsifying business documents, after investigators searched his home and workplace."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/re-examining-the-ddr4-gaming-gap-with-intels-lga-1700-cpus-in-mid-2026-performance-drops-of-14-percent-on-average-and-up-to-25-percent-in-some-games",
    "domain": "AI 算力 / 半导体",
    "title": "Re-examining the DDR4 gaming gap with Intel’s LGA 1700 CPUs in mid-2026 — performance drops of 14% on average, and up to 25% in some games",
    "url": "https://www.tomshardware.com/pc-components/ddr5/re-examining-the-ddr4-gaming-gap-with-intels-lga-1700-cpus-in-mid-2026-performance-drops-of-14-percent-on-average-and-up-to-25-percent-in-some-games",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T10:32:27+00:00",
    "summary": "Given the unprecedented surge in memory prices, we’re looking back on Intel’s LGA 1700 stack of CPUs to see how DDR4 and DDR5 match up with our modern gaming suite in 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-companies-are-reportedly-shredding-millions-of-books-to-train-models-tech-giants-outsource-to-middlemen-to-secretly-buy-up-books-for-training-material",
    "domain": "AI 算力 / 半导体",
    "title": "AI companies are reportedly shredding millions of books after using them to train AI models — tech giants outsource to middlemen to secretly buy up books for training material",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-companies-are-reportedly-shredding-millions-of-books-to-train-models-tech-giants-outsource-to-middlemen-to-secretly-buy-up-books-for-training-material",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T10:30:00+00:00",
    "summary": "New report reveals that AI companies are buying up physical books to train their LLMs and destroying them in the process."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/programming/daring-coder-gets-doom-running-with-regular-expressions-at-180-seconds-per-frame-like-playing-correspondence-chess-with-a-shotgun-nearly-14-million-substitutions-to-render-a-frame-at-80-000-substitutions-per-second",
    "domain": "AI 算力 / 半导体",
    "title": "Daring coder gets Doom running with regular expressions at 180 seconds per frame, like playing 'correspondence chess with a shotgun' — nearly 14 million substitutions to render a frame at 80,000 subst",
    "url": "https://www.tomshardware.com/software/programming/daring-coder-gets-doom-running-with-regular-expressions-at-180-seconds-per-frame-like-playing-correspondence-chess-with-a-shotgun-nearly-14-million-substitutions-to-render-a-frame-at-80-000-substitutions-per-second",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T10:00:00+00:00",
    "summary": "Daring coder gets Doom running with regular expressions at 180 seconds per frame by using one text string to the machine, engine, and video output"
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
    "points": 194,
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
    "id": "hn:49088771",
    "domain": "大厂 AI 动态",
    "title": "Show HN: Minute – Offline meeting notes on macOS with Whisper and llama.cpp",
    "url": "https://github.com/mraza007/minute",
    "source": "mraza007",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-28T19:31:17+00:00",
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
    "id": "rss:https://www.theverge.com/tech/972259/us-foreign-robots-power-inverter-ban",
    "domain": "大厂 AI 动态",
    "title": "The US is banning foreign robots",
    "url": "https://www.theverge.com/tech/972259/us-foreign-robots-power-inverter-ban",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T22:37:53+00:00",
    "summary": "The US government is targeting China with a new import ban on \"advanced robotic devices\" and power inverters made in foreign countries, as reported earlier by Reuters. In an announcement on Tuesday, t"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/972233/ariana-grande-hacking-lawsuit",
    "domain": "大厂 AI 动态",
    "title": "Ariana Grande is suing the hackers who&#8217;ve been leaking her songs and videos for years",
    "url": "https://www.theverge.com/entertainment/972233/ariana-grande-hacking-lawsuit",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T21:48:50+00:00",
    "summary": "Ariana Grande filed a lawsuit on Monday in the Los Angeles County Superior Court against the currently unidentified hackers who allegedly stole and leaked private content. It aims to \"uncover the iden"
  },
  {
    "id": "rss:https://www.theverge.com/news/972182/wikipedia-wikimedia-foundation-union-editor-strike",
    "domain": "大厂 AI 动态",
    "title": "The union drive at the Wikimedia Foundation is expanding",
    "url": "https://www.theverge.com/news/972182/wikipedia-wikimedia-foundation-union-editor-strike",
    "source": "Mia Sato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T21:11:11+00:00",
    "summary": "In June, UK staff at the nonprofit that runs Wikipedia became the first to announce their intention to form a union. Now, US-based employees at the Wikimedia Foundation are joining the union drive, bu"
  },
  {
    "id": "rss:https://www.theverge.com/tech/972209/ebay-cyberstalking-harassment-settlement",
    "domain": "大厂 AI 动态",
    "title": "eBay&#8217;s bizarre cyberstalking saga ends with a $56 million settlement",
    "url": "https://www.theverge.com/tech/972209/ebay-cyberstalking-harassment-settlement",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T21:11:11+00:00",
    "summary": "eBay and three former executives will pay $55.7 million as part of a settlement with a Massachusetts couple targeted with a bizarre harassment and cyberstalking campaign in 2019, as reported earlier b"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/972161/ai-leaders-us-government-openai-anthropic-google-meta",
    "domain": "大厂 AI 动态",
    "title": "AI leaders sign a statement asking the government to do something about automated AI",
    "url": "https://www.theverge.com/ai-artificial-intelligence/972161/ai-leaders-us-government-openai-anthropic-google-meta",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T19:46:43+00:00",
    "summary": "Employees of OpenAI and Anthropic, as well as Google, Meta, Thinking Machines, Microsoft, Mistral, and other leading AI labs, have written a statement to the US government supporting a potential slowd"
  },
  {
    "id": "rss:https://www.theverge.com/report/972146/cbp-phone-search-airport-duress-password",
    "domain": "大厂 AI 动态",
    "title": "Is it illegal to trick the US government into wiping your phone during a questionably legal search?",
    "url": "https://www.theverge.com/report/972146/cbp-phone-search-airport-duress-password",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T19:35:00+00:00",
    "summary": "A Georgia man was charged with a felony for allegedly wiping his phone while being questioned by Customs and Border Protection. Samuel Tunick had something in common with others who have had their dev"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/972119/ai-stock-fall-google-capex",
    "domain": "大厂 AI 动态",
    "title": "AI’s finally expensive enough to make Wall Street nervous",
    "url": "https://www.theverge.com/ai-artificial-intelligence/972119/ai-stock-fall-google-capex",
    "source": "Elizabeth Lopatto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T19:33:03+00:00",
    "summary": "It's earnings season, and investors got an unpleasant surprise from Google: an increase on its spending estimate, to as much as $205 billion - from the last quarter's projection of up to $190 billion."
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/972021/epos-h3-hybrid-wired-gaming-headset-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "This comfy gaming headset that can play audio from two sources is $25",
    "url": "https://www.theverge.com/gadgets/972021/epos-h3-hybrid-wired-gaming-headset-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T19:18:15+00:00",
    "summary": "While most gaming headsets have moved towards low-latency wireless connections, there’s something to be said for a budget-friendly, capable wired headset. The EPOS H3 Hybrid is on sale for just $24.99"
  },
  {
    "id": "rss:https://www.theverge.com/tech/971963/logitech-user-replacable-batteries-europe",
    "domain": "大厂 AI 动态",
    "title": "Logitech will pull a Nintendo — only European mice will come with replaceable batteries",
    "url": "https://www.theverge.com/tech/971963/logitech-user-replacable-batteries-europe",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T19:12:48+00:00",
    "summary": "In June, Nintendo announced a new version of the Switch 2 that should let you easily replace its battery pack - but only for Europe. Logitech will do much the same. User-replaceable batteries will be "
  },
  {
    "id": "rss:https://www.theverge.com/tech/972063/apple-upgrade-program-no-restricted-mode",
    "domain": "大厂 AI 动态",
    "title": "Apple won’t turn on any ‘restricted mode’ for missed lease payments",
    "url": "https://www.theverge.com/tech/972063/apple-upgrade-program-no-restricted-mode",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T18:43:57+00:00",
    "summary": "Apple says it won't limit the capabilities of devices leased through its new Upgrade program if you miss a payment. In an emailed statement to The Verge, Apple spokesperson Brian Bumbery says, \"There "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/cyera-agrees-to-acquire-oasis-security-for-1b-to-safeguard-proliferating-ai-agents/",
    "domain": "大厂 AI 动态",
    "title": "Cyera agrees to acquire Oasis Security for $1B to safeguard proliferating AI agents",
    "url": "https://techcrunch.com/2026/07/28/cyera-agrees-to-acquire-oasis-security-for-1b-to-safeguard-proliferating-ai-agents/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T00:09:05+00:00",
    "summary": "The deal is Cyera's third acquisition this year."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/bot-detection-startup-spur-nabs-200m-from-insight/",
    "domain": "大厂 AI 动态",
    "title": "Bot-detection startup Spur nabs $200M from Insight",
    "url": "https://techcrunch.com/2026/07/28/bot-detection-startup-spur-nabs-200m-from-insight/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T21:29:34+00:00",
    "summary": "Spur Intelligence has raised a $200 million round from Insight Partners for its tech that can identify legit human traffic from bots."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/mcp-startup-runlayer-accuses-rippling-of-stealing-its-product-idea/",
    "domain": "大厂 AI 动态",
    "title": "MCP startup Runlayer accuses Rippling of stealing its product idea",
    "url": "https://techcrunch.com/2026/07/28/mcp-startup-runlayer-accuses-rippling-of-stealing-its-product-idea/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T20:45:12+00:00",
    "summary": "Runlayer is suing Rippling after Rippling evaluated the startup's MCP gateway product and then opted to build one itself."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/sam-altman-is-ready-to-decelerate/",
    "domain": "大厂 AI 动态",
    "title": "Sam Altman is ready to decelerate",
    "url": "https://techcrunch.com/2026/07/28/sam-altman-is-ready-to-decelerate/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T20:17:08+00:00",
    "summary": "His change of position comes after \"the first security incident that I have felt very viscerally.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/ozlos-sleepbuds-2-build-on-boses-sleep-earbud-legacy/",
    "domain": "大厂 AI 动态",
    "title": "Ozlo’s Sleepbuds 2 build on Bose’s sleep earbud legacy",
    "url": "https://techcrunch.com/2026/07/28/ozlos-sleepbuds-2-build-on-boses-sleep-earbud-legacy/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T19:09:18+00:00",
    "summary": "Ozlo’s first major update to its sleep earbuds introduces longer battery life, improved connectivity, enhanced audio, and new sleep features as the startup continues the product line once abandoned by"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/the-robot-nasa-hired-to-lift-a-orbital-telescope-is-tumbling-out-of-control/",
    "domain": "大厂 AI 动态",
    "title": "The robot NASA hired to lift a orbital telescope tumbled out of control",
    "url": "https://techcrunch.com/2026/07/28/the-robot-nasa-hired-to-lift-a-orbital-telescope-is-tumbling-out-of-control/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T19:07:31+00:00",
    "summary": "According to NASA, two of the three reaction wheels that control the spacecraft's alignment have failed, and there are problems with one of the spacecraft's thruster systems."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/waymo-robotaxi-operators-face-fresh-scrutiny-over-emergency-response-failures/",
    "domain": "大厂 AI 动态",
    "title": "Waymo, robotaxi operators face fresh scrutiny over emergency response failures",
    "url": "https://techcrunch.com/2026/07/28/waymo-robotaxi-operators-face-fresh-scrutiny-over-emergency-response-failures/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T19:06:33+00:00",
    "summary": "Rep. Kevin Mullin (D-California ) has proposed a bill that would direct federal regulators to establish minimum national safety standards for autonomous vehicle operators."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/ebay-reaches-56m-settlement-with-e-commerce-newsletter-writers-it-terrorized-in-2019/",
    "domain": "大厂 AI 动态",
    "title": "eBay reaches $56M settlement with e-commerce newsletter writers it terrorized in 2019",
    "url": "https://techcrunch.com/2026/07/28/ebay-reaches-56m-settlement-with-e-commerce-newsletter-writers-it-terrorized-in-2019/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T18:35:29+00:00",
    "summary": "Ina and David Steiner inspired the ire of high-level eBay executives after occasionally criticizing the company in their newsletter. In 2019, a plot was concocted to intimidate the couple into halting"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/these-app-store-hidden-gems-prove-theres-still-room-for-great-software-in-the-ai-era/",
    "domain": "大厂 AI 动态",
    "title": "These App Store hidden gems prove there’s still room for great software in the AI era",
    "url": "https://techcrunch.com/2026/07/28/these-app-store-hidden-gems-prove-theres-still-room-for-great-software-in-the-ai-era/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T18:16:39+00:00",
    "summary": "Despite predictions that AI agents could make traditional apps obsolete, developers are shipping new software faster than ever. From smarter bookmarking tools and neighborhood marketplaces to digital "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/hbo-max-embraces-vertical-video-with-a-new-shorts-feed/",
    "domain": "大厂 AI 动态",
    "title": "HBO Max embraces vertical video with a new ‘Shorts’ feed",
    "url": "https://techcrunch.com/2026/07/28/hbo-max-embraces-vertical-video-with-a-new-shorts-feed/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T17:57:57+00:00",
    "summary": "HBO Max, like other streaming platforms, is rethinking content discovery as large libraries are making it hard for viewers to find something to watch and as audiences become accustomed to short-form c"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/saudi-prince-buys-5-stake-in-lucid-motors/",
    "domain": "大厂 AI 动态",
    "title": "Saudi prince buys 5% stake in Lucid Motors",
    "url": "https://techcrunch.com/2026/07/28/saudi-prince-buys-5-stake-in-lucid-motors/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T17:33:51+00:00",
    "summary": "The investment comes after speculation that Saudi Arabia may take Lucid Motors private -- which the EV maker has denied."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/data-centers-may-face-temporary-power-cuts-to-prevent-blackouts-on-largest-us-grid/",
    "domain": "大厂 AI 动态",
    "title": "Data centers may face temporary power cuts to prevent blackouts on largest US grid",
    "url": "https://techcrunch.com/2026/07/28/data-centers-may-face-temporary-power-cuts-to-prevent-blackouts-on-largest-us-grid/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T15:42:26+00:00",
    "summary": "The decision arrives as the breakneck pace of data center construction has grid operators scrambling to generate power."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/paypal-leaves-the-door-open-to-a-higher-takeover-offer-following-earnings-beat/",
    "domain": "大厂 AI 动态",
    "title": "PayPal leaves the door open to a higher takeover offer following earnings beat",
    "url": "https://techcrunch.com/2026/07/28/paypal-leaves-the-door-open-to-a-higher-takeover-offer-following-earnings-beat/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T15:10:10+00:00",
    "summary": "After reporting better-than-expected Q2 results, PayPal said it remains focused on its AI-driven turnaround, but would consider a deal that creates more value for shareholders."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/elon-musks-x-money-app-is-rolling-out-in-the-u-s/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk’s X Money app is rolling out in the US",
    "url": "https://techcrunch.com/2026/07/28/elon-musks-x-money-app-is-rolling-out-in-the-u-s/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T14:57:12+00:00",
    "summary": "Users get an X Visa debit card, which they can immediately add to Apple Pay and use to make instant peer-to-peer transfers within the app without fees or limits."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/whatsapp-now-lets-you-make-calls-using-its-web-app/",
    "domain": "大厂 AI 动态",
    "title": "WhatsApp now lets you make calls using its web app",
    "url": "https://techcrunch.com/2026/07/28/whatsapp-now-lets-you-make-calls-using-its-web-app/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T14:53:22+00:00",
    "summary": "Similar to the smartphone and desktop apps, the web app will support calling features such as screen-sharing and reactions."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/fish-audio-raises-50m-seed-to-build-ai-voice-models-for-creators-and-enterprises/",
    "domain": "大厂 AI 动态",
    "title": "Fish Audio raises $52M seed to build AI voice models for creators and enterprises",
    "url": "https://techcrunch.com/2026/07/28/fish-audio-raises-50m-seed-to-build-ai-voice-models-for-creators-and-enterprises/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T14:00:00+00:00",
    "summary": "Since launching last year, the startup today has more than 8 million people using the open source or hosted version of its models, and now generates annual recurring revenue of $21 million."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/apple-launches-upgrade-device-leasing-program-in-partnership-with-klarna/",
    "domain": "大厂 AI 动态",
    "title": "Apple launches ‘Upgrade’ device leasing program in partnership with Klarna",
    "url": "https://techcrunch.com/2026/07/28/apple-launches-upgrade-device-leasing-program-in-partnership-with-klarna/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T13:50:27+00:00",
    "summary": "The rollout of the program comes as Apple has been struggling with supply chain issues related to \"RAMageddon,\" which refers to the industry-wide shortage of memory chips that is driving up the price "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/recursive-superintelligence-signs-400-compute-deal-with-amazon/",
    "domain": "大厂 AI 动态",
    "title": "Recursive Superintelligence signs $410M compute deal with Amazon",
    "url": "https://techcrunch.com/2026/07/28/recursive-superintelligence-signs-400-compute-deal-with-amazon/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T13:19:17+00:00",
    "summary": "Recursive’s emphasis on self-improving AI systems means much of the budget that would traditionally go toward headcount and operations is put straight into compute, as the company seeks to automate it"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/granola-launches-an-apple-watch-app/",
    "domain": "大厂 AI 动态",
    "title": "Granola launches an Apple Watch app",
    "url": "https://techcrunch.com/2026/07/28/granola-launches-an-apple-watch-app/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T13:00:00+00:00",
    "summary": "AI note-taking app Granola is launching an app for the Apple Watch in hopes that its users will want to record meetings and take notes without using their smartphones."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/28/lyft-and-baidu-enter-londons-robotaxi-battleground-as-testing-begins/",
    "domain": "大厂 AI 动态",
    "title": "Lyft and Baidu enter London’s robotaxi battleground as testing begins",
    "url": "https://techcrunch.com/2026/07/28/lyft-and-baidu-enter-londons-robotaxi-battleground-as-testing-begins/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T08:00:00+00:00",
    "summary": "Baidu's Apollo Go autonomous vehicles will be available on Freenow, the mobility network that Lyft acquired in 2025."
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
    "id": "rss:https://arstechnica.com/cars/2026/07/audi-has-a-new-flagship-designed-with-the-us-in-mind-the-2027-q9/",
    "domain": "大厂 AI 动态",
    "title": "Audi has a new flagship designed with the US in mind: The 2027 Q9",
    "url": "https://arstechnica.com/cars/2026/07/audi-has-a-new-flagship-designed-with-the-us-in-mind-the-2027-q9/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T01:00:36+00:00",
    "summary": "The new full-size flagship SUV starts at $87,700 when it goes on sale in Q4."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/reaction-wheel-failures-leave-swift-rescue-mission-spinning-in-orbit/",
    "domain": "大厂 AI 动态",
    "title": "Reaction wheel failures leave Swift rescue mission spinning in orbit",
    "url": "https://arstechnica.com/space/2026/07/reaction-wheel-failures-leave-swift-rescue-mission-spinning-in-orbit/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T22:09:00+00:00",
    "summary": "\"Preliminary investigation shows that two of Link's three reaction wheels currently are not operable.\""
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/college-lab-class-ends-with-32-people-on-antibiotics-for-deadly-germ-exposure/",
    "domain": "大厂 AI 动态",
    "title": "College lab class ends with 32 people on antibiotics for deadly germ exposure",
    "url": "https://arstechnica.com/health/2026/07/college-lab-class-ends-with-32-people-on-antibiotics-for-deadly-germ-exposure/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T21:49:52+00:00",
    "summary": "Lab students were supposed to ID a mild germ. They all identified a deadly pathogen."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/07/jfrog-tries-to-spin-openai-0-day-exploit-of-its-app-into-a-success-story/",
    "domain": "大厂 AI 动态",
    "title": "We now have a better understanding how OpenAI hacked into Hugging Face",
    "url": "https://arstechnica.com/security/2026/07/jfrog-tries-to-spin-openai-0-day-exploit-of-its-app-into-a-success-story/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T21:36:39+00:00",
    "summary": "10 days passed from OpenAI models exploiting JFrog Artifactory 0-day to release of a patch."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/ebay-former-execs-pay-56m-to-settle-bloody-pig-mask-harassment-case/",
    "domain": "大厂 AI 动态",
    "title": "eBay pays $46M to journalists it targeted in bizarre harassment campaign",
    "url": "https://arstechnica.com/tech-policy/2026/07/ebay-former-execs-pay-56m-to-settle-bloody-pig-mask-harassment-case/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T21:02:15+00:00",
    "summary": "eBay sent bloody pig mask and other macabre deliveries to journalists' home."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/dust-cloud-from-dino-killing-asteroid-charbroiled-the-earth/",
    "domain": "大厂 AI 动态",
    "title": "Study: Dinosaurs were charbroiled after Chicxulub impact",
    "url": "https://arstechnica.com/science/2026/07/dust-cloud-from-dino-killing-asteroid-charbroiled-the-earth/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T20:51:45+00:00",
    "summary": "“We're in the realm where we might be essentially killing off everything within that first hour or two.\""
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/philly-suburb-sure-build-that-data-center-but-first-meet-our-43-demands/",
    "domain": "大厂 AI 动态",
    "title": "Philly suburb: Sure, build that data center—but first meet our 43 demands",
    "url": "https://arstechnica.com/tech-policy/2026/07/philly-suburb-sure-build-that-data-center-but-first-meet-our-43-demands/",
    "source": "Nate Anderson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T20:43:19+00:00",
    "summary": "The final condition will shock you! (It won’t. It’s taxes.)"
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/despite-ai-hype-googles-data-shows-workers-arent-automating-themselves-away/",
    "domain": "大厂 AI 动态",
    "title": "Despite AI hype, Google's data shows workers aren't automating themselves away",
    "url": "https://arstechnica.com/ai/2026/07/despite-ai-hype-googles-data-shows-workers-arent-automating-themselves-away/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-28T20:20:20+00:00",
    "summary": "Analysis of 15 million real AI interactions finds most tasks at most jobs are unaffected."
  },
  {
    "id": "hn:49057574",
    "domain": "股票",
    "title": "Google Discloses $94.1B in SpaceX Stock, Marking 6% Stake",
    "url": "https://www.wsj.com/tech/google-discloses-94-1-billion-in-spacex-stock-marking-6-stake-91655d7c",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 340,
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
    "id": "hn:49092549",
    "domain": "股票",
    "title": "Chip stocks slide in US and Asia as AI jitters rattle investors",
    "url": "https://www.bbc.com/news/articles/cly8zng43npo",
    "source": "yogthos",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-07-29T01:56:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:49087537",
    "domain": "股票",
    "title": "Chip stocks tumble as AI sell-off deepens",
    "url": "https://www.ft.com/content/f8c03b5b-e194-4236-82c3-389b6f5dd7ae",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-07-28T17:54:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49081705",
    "domain": "股票",
    "title": "AI sell-off intensifies as investors ditch chip stocks",
    "url": "https://www.theguardian.com/business/2026/jul/28/ai-sell-off-chip-stocks-sk-hynix-samsung",
    "source": "lilerjee",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-28T10:08:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:49091512",
    "domain": "股票",
    "title": "Apple becomes second $5T company as investors flee AI stocks",
    "url": "https://www.theguardian.com/technology/2026/jul/28/apple-second-ever-5tn-company-as-investors-flee-ai-stocks",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-28T23:41:59+00:00",
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
    "id": "wscn:3778182",
    "domain": "股票",
    "title": "创业板午后拉升涨超2%，金融科技、锂电池爆发，存储芯片跌幅收窄、兆易创新打开跌停，恒科指一度大涨3%，小米涨逾7%",
    "url": "https://wallstreetcn.com/articles/3778182",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T05:44:00+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市超3400股飘红，上午半天成交1.49万亿。沪深两市半日成交额1.48万亿，较上个交易日放量超1500亿。板块方面，半导体、算力硬件产业链持续下探，光刻机、HBM、CPO、PCB、存储器方向领跌；脑机接口、光伏概念股跌幅靠前。大消费、汽车、煤炭、金融板块走强。"
  },
  {
    "id": "wscn:3778189",
    "domain": "股票",
    "title": "多年来“最不确定”的一次！今晚的美联储会给“惊吓”吗？",
    "url": "https://wallstreetcn.com/articles/3778189",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T05:31:29+00:00",
    "summary": "美联储今晚大概率按兵不动，但这或许是近年最不平静的一次“暂停”。货币市场给出32%的加息概率，瑞银经济学家直言不确定程度为20年之最。内部鹰派分歧扩大，沃什政策风格成谜，Citadel等机构已明确押注意外加息。摩根大通测算，若加息25基点，标普500可能重挫逾2%——今晚，“不变”本身也可能是一场震动。"
  },
  {
    "id": "wscn:3778196",
    "domain": "股票",
    "title": "当1178名AI人试图阻止“AGI”：让全人类刹车的成本到底有多大？答案或许是蒸发2.5万亿美元",
    "url": "https://wallstreetcn.com/premium/articles/3778196?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:54:02+00:00",
    "summary": "2026年7月28日，来自OpenAI、Anthropic、Google、Meta、Microsoft、Mistral、Thinking Machines等前沿AI公司的1178名员工联合签署《Pacing the Frontier》公开声明，要求美国政府推动国际合作，建立\"有意放缓自动化AI研发节奏\"的技术和治理工具。"
  },
  {
    "id": "wscn:3778195",
    "domain": "股票",
    "title": "OceanBase拟募资至多30亿元，蚂蚁集团数据业务加速市场化独立步伐",
    "url": "https://wallstreetcn.com/articles/3778195",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:40:44+00:00",
    "summary": "7月29日，华尔街见闻获悉，数据库公司OceanBase正在与投资者洽谈A轮融资，目前，该公司已与多..."
  },
  {
    "id": "wscn:3778190",
    "domain": "股票",
    "title": "\"史上最强\"之后，海力士开始难超预期了",
    "url": "https://wallstreetcn.com/articles/3778190",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:38:50+00:00",
    "summary": "SK海力士二季度营收79.32万亿韩元、营业利润暴增557%，利润率76.3%刷新存储业历史纪录，毛利率83%已超越英伟达——却成了本轮超级周期中唯一miss共识的巨头。根源在于：HBM霸主地位反噬，50%收入被LTA长协锁定，现货狂涨时只能眼看三星、美光收割ASP弹性。这不是经营恶化，而是一场\"用确定性换弹性\"的主动选择。下半年HBM4放量，才是判断这笔交易值不值的真正答案。"
  },
  {
    "id": "wscn:3777986",
    "domain": "股票",
    "title": "危险的信号？5000亿美元数据中心担保融资，英伟达开始押上自己的信用换芯片订单",
    "url": "https://wallstreetcn.com/premium/articles/3777986?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:06:03+00:00",
    "summary": "英伟达正与OpenAI商谈，为美国俄亥俄州一座10GW级数据中心项目提供最高约2500亿美元融资支持。英伟达并非直接投入等额现金，而是利用自身信用，为项目贷款或OpenAI的长期算力承诺提供增信。此举既能帮助英伟达锁定未来GPU需求，也意味着其角色正在由芯片供应商延伸至资本组织者和信用承保人。真正值得关注的是：当AI客户需要供应商担保才能继续扩大采购，巨额算力订单究竟反映了终端需求的强劲，还是信用"
  },
  {
    "id": "wscn:3778192",
    "domain": "股票",
    "title": "加息还是暂停？新美联储通讯社：今晚FOMC三大看点全解析",
    "url": "https://wallstreetcn.com/articles/3778192",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T03:59:20+00:00",
    "summary": "Timiraos认为，本次FOMC会议异常难以预判。三大看点：一是决策结果，按兵不动为常规，意外加息将冲击公信力；二是战略意图，看其是否借加息重塑抗通胀形象；三是政策解释，其叙事框架比决策更左右市场。最终，取决于数据的9月才是真正分水岭。"
  },
  {
    "id": "wscn:3778181",
    "domain": "股票",
    "title": "韩股如何“收复失地”？从“杠杆牛”到“回购牛”",
    "url": "https://wallstreetcn.com/articles/3778181",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T03:59:15+00:00",
    "summary": "野村认为，此轮去杠杆是市场\"重置\"而非趋势逆转，韩股正从\"杠杆牛\"切换至\"回购牛\"。2026年企业回购规模将创纪录达116万亿韩元（其中90%来自两大半导体巨头），叠加AI盈利周期与政府治理改革，将成为韩股收复失地、冲击万点目标的核心引擎。"
  },
  {
    "id": "wscn:3778184",
    "domain": "股票",
    "title": "Altman复盘OpenAI最艰难一年：蒸馏不在我的十大担忧，AGI近在咫尺，机器人2-3年将迎来ChatGPT时刻",
    "url": "https://wallstreetcn.com/articles/3778184",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T03:34:23+00:00",
    "summary": "Altman罕见复盘了公司过去一年的战略失误，承认战线过宽是根本原因，并已大幅收缩聚焦。他对外界热议的蒸馏竞争表现淡定，直言“不在我的十大担忧之列”，因为推理业务规模足以支撑训练成本。他判断AGI“非常近了”，GPT-5.6已接近门槛；机器人将在2-3年内迎来类ChatGPT的大众化时刻。"
  },
  {
    "id": "wscn:3778194",
    "domain": "股票",
    "title": "从锆材料到特种尼龙，长裕集团新增长曲线渐成",
    "url": "https://wallstreetcn.com/articles/3778194",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T03:27:39+00:00",
    "summary": "今年以来，氧氯化锆市场景气度明显回升。\n受下游需求增长、市场供应偏紧等因素的影响，氧氯化锆价格持续走..."
  },
  {
    "id": "wscn:3778191",
    "domain": "股票",
    "title": "淘宝便利店扩土：一场「反直觉」突围？",
    "url": "https://wallstreetcn.com/articles/3778191",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T03:11:48+00:00",
    "summary": "更多货架的意义"
  },
  {
    "id": "wscn:3778188",
    "domain": "股票",
    "title": "AI股暴跌引发追保潮，高盛摩根大通向对冲基金追讨抵押品",
    "url": "https://wallstreetcn.com/articles/3778188",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T03:06:49+00:00",
    "summary": "追保行动的背后，是对冲基金在今年前五个月大幅加杠杆的后遗症。高盛在近期客户报告中指出，今年前五个月对冲基金总杠杆率的累计增幅，是该行自2016年开始追踪这一数据以来所记录的最大单次累计增长。分析认为，这标志着抛售潮已蔓延至信用与风险管理层面。"
  },
  {
    "id": "wscn:3778185",
    "domain": "股票",
    "title": "废除前瞻指引后，沃什可能比市场预期更早加息",
    "url": "https://wallstreetcn.com/articles/3778185",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T03:04:14+00:00",
    "summary": "华泰证券认为，美联储新主席沃什上任仅两月，便以\"对通胀零容忍\"和废除前瞻指引两记重拳震动市场，令定价从鸽派骤转鹰派。然而公信力指标旋即反弹后再度走弱，市场已从\"听其言\"切换至\"观其行\"。7月加息概率略超五成，高于市场预期的40%；9月前加息概率接近100%——越早出手，驯服市场的代价越小，最终所需加息次数或反而越少。"
  },
  {
    "id": "wscn:3778177",
    "domain": "股票",
    "title": "股价仍跌超10%！SK海力士电话会：未见AI投资放缓迹象，HBM4已提前量产，长协不会导致供应过剩",
    "url": "https://wallstreetcn.com/articles/3778177",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T03:01:46+00:00",
    "summary": "电话会上，管理层明确表示“目前没有看到人工智能投资放缓的迹象”，并预计2027年后AI基础设施投资仍将保持稳健。HBM4已较预期提前一个季度量产，HBM4E已确认2027年起量产。2026年资本开支上调至40万亿韩元中高水平，5年期长期协议不会导致供应过剩。尽管管理层表态积极，电话会结束后SK海力士股价仍转跌10%。"
  },
  {
    "id": "wscn:3778180",
    "domain": "股票",
    "title": "中际旭创电话会：1.6T降价传闻严重失实，2027年“真实订单”已下达，新品上量将拉动毛利率",
    "url": "https://wallstreetcn.com/articles/3778180",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T02:09:32+00:00",
    "summary": "中际旭创表示，公司明年1.6T产品价格“肯定远高于传闻所说的水平”，同行也没有这么低的价格；从加权平均ASP看，相关传闻“非常离谱”；“几乎所有客户都已经下达了2027年订单”，且不是一般性指引，而是真实订单；部分重点客户已给出2028年新产品具体需求指引，金额“非常大”。"
  },
  {
    "id": "wscn:3777781",
    "domain": "股票",
    "title": "中国双龙反超韩系双雄，全球黑电产业进入“中国主导”时代？",
    "url": "https://wallstreetcn.com/premium/articles/3777781?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T02:08:31+00:00",
    "summary": "2026年以来，全球电视出货边际回暖。但比世界杯备货更重要的是，TCL、海信持续跑赢全球大盘，两家公司合计出货量已在部分口径下超过三星与LG；国内销量虽然仍受高基数和补贴退坡压制，大屏、Mini LED及均价却在逆势提升。全球电视总量已进入存量阶段，中国企业的增长逻辑也由需求扩张转向份额获取，并进一步由成本优势升级为技术、品牌和产业链协同优势——世界杯之后，这场全球电视格局的重构还会继续吗？"
  },
  {
    "id": "wscn:3778176",
    "domain": "股票",
    "title": "韩股跳水触发熔断，海力士财报不及预期大跌8%，中东局势助推油价跳涨",
    "url": "https://wallstreetcn.com/articles/3778176",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T01:58:57+00:00",
    "summary": "韩国SK海力士净利润暴增557%，虽不及预期并未大幅偏离预期，首尔综指一度涨逾3%，但随后跳水跌超5%，SK海力士跌超8%。中东局势骤然升温，伊朗向驻中东美军发射弹道导弹，布伦特原油单日跳涨逾3%，终结三日连跌，霍尔木兹海峡断供风险重回市场视野。"
  },
  {
    "id": "wscn:3778179",
    "domain": "股票",
    "title": "“AI能源妖股”Bloom单季营收首破十亿美元，大幅上调全年指引，CEO电话会放话：芯片没电是库存",
    "url": "https://wallstreetcn.com/articles/3778179",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T01:09:44+00:00",
    "summary": "财报显示，Q2营收10.65亿美元（同比+166%），首次突破单季10亿美元，非GAAP EPS 0.78美元同比暴增680%，双双大幅超出市场预期。公司将全年营收指引上调至39亿至42亿美元，中值较2025年实现翻番，全年EPS指引升至2.55至2.85美元。CEO Sridhar宣告，所有主要美国超大规模云厂商及逾十二家AI相关客户已完成验证，Bloom已成为AI工厂供电标准。"
  },
  {
    "id": "wscn:3778178",
    "domain": "股票",
    "title": "宁德时代的焦虑，和英伟达一模一样",
    "url": "https://wallstreetcn.com/articles/3778178",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T01:07:50+00:00",
    "summary": "宁德时代上半年营收2769亿、净利433亿，数据亮眼却难掩毛利率跌至23.2%的隐忧。这并非能力不足，而是一场主动为之的战略让利——用价格换份额，为下游“挡子弹”，护住47%的国内乘用车市占率。合同负债连降、库存商品占比悄然抬升，宁王的焦虑与英伟达如出一辙：巨头的护城河，终究建在下游生态的繁荣之上。"
  },
  {
    "id": "wscn:3778086",
    "domain": "股票",
    "title": "山西“十七条意见”限产：出清表外亿吨级产量，供给硬约束煤价或上行",
    "url": "https://wallstreetcn.com/premium/articles/3778086?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T00:51:03+00:00",
    "summary": "2026年7月21日，山西省发布《统筹煤炭行业发展和安全新规十七条（征求意见稿）》。这不仅是\"5·22\"沁源煤矿82人遇难特大事故后的政策回应，更是中国煤炭行业供给秩序的一次结构性重塑。"
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
    "id": "hn:49082695",
    "domain": "金融",
    "title": "Mondragon Corporation – a federation of co-operatives",
    "url": "https://en.wikipedia.org/wiki/Mondragon_Corporation",
    "source": "brnt",
    "platform": "hackernews",
    "points": 169,
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
    "points": 156,
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
    "id": "hn:49082706",
    "domain": "金融",
    "title": "AI revenues are growing fast, but not fast enough",
    "url": "https://www.economist.com/finance-and-economics/2026/07/28/ai-revenues-are-growing-fast-but-not-fast-enough",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-07-28T12:19:54+00:00",
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
    "id": "rss:https://arxiv.org/abs/2607.24879",
    "domain": "金融",
    "title": "Generative Artificial Intelligence in Scientific Research: Individual Benefits, Collective Risks, and a Framework for Responsible Research with AI",
    "url": "https://arxiv.org/abs/2607.24879",
    "source": "Fulvio Castellacci, Tommaso Ciarli, Yuan Gao, Marianna Marino, Giacomo Marzi, Massimo Riccaboni, Maria Savona, Simone Vannuccini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:00:00+00:00",
    "summary": "arXiv:2607.24879v1 Announce Type: new Abstract: This paper examines the tension between the benefits of generative artificial intelligence (AI) for scientific research and the unresolved governance qu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.24973",
    "domain": "金融",
    "title": "Discrete dividends after maturity adjust the stock and strike prices",
    "url": "https://arxiv.org/abs/2607.24973",
    "source": "Kevin W. Lu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:00:00+00:00",
    "summary": "arXiv:2607.24973v1 Announce Type: new Abstract: The standard method to price European calls on a discrete dividend-paying stock is to subtract the present value of the dividends from the initial stock"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.25189",
    "domain": "金融",
    "title": "Long-memory GARCH via a two-dimensional Markov chain",
    "url": "https://arxiv.org/abs/2607.25189",
    "source": "Kyungsub Lee, Kennedy Titus Kayaki",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:00:00+00:00",
    "summary": "arXiv:2607.25189v1 Announce Type: new Abstract: This paper proposes a GARCH-type volatility model in which level-and-slope updates of a latent power-law kernel generate state-dependent decay of past s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.25199",
    "domain": "金融",
    "title": "RIDGE: An Autonomous Framework for Validation and Method Discovery in LLM-Generated Option Pricing",
    "url": "https://arxiv.org/abs/2607.25199",
    "source": "Liexin Cheng, Xue Cheng, Shuaiqiang Liu, Cornelis W. Oosterlee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:00:00+00:00",
    "summary": "arXiv:2607.25199v1 Announce Type: new Abstract: Automated code generation is becoming an important tool in quantitative finance, where large language models can generate option pricing implementations"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.25258",
    "domain": "金融",
    "title": "Robust Hedging Valuation Adjustment for Deep Hedging Policies under Market Frictions",
    "url": "https://arxiv.org/abs/2607.25258",
    "source": "Takayuki Sakuma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:00:00+00:00",
    "summary": "arXiv:2607.25258v1 Announce Type: new Abstract: Hedging a derivative position under transaction costs and market frictions requires a trading rule that adapts to changing conditions. Deep hedging trai"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.25353",
    "domain": "金融",
    "title": "How Likely and How Deep? Sharp Joint Bounds on Risk-Neutral Crash Probability and Conditional Depth from Option Bid-Ask Quotes",
    "url": "https://arxiv.org/abs/2607.25353",
    "source": "Jirong Zhuang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:00:00+00:00",
    "summary": "arXiv:2607.25353v1 Announce Type: new Abstract: A finite panel of option quotes with bid-ask spreads generally does not point-identify either the risk-neutral probability of breaching a specified thre"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.25472",
    "domain": "金融",
    "title": "Algorithm-Driven Information Similarity and Collective Action: An Experimental Study",
    "url": "https://arxiv.org/abs/2607.25472",
    "source": "Manshu Khanna, Bozhang Xia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:00:00+00:00",
    "summary": "arXiv:2607.25472v1 Announce Type: new Abstract: We study how the similarity of individuals' information shapes collective action. When people draw on a common source of information, such as social med"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.25599",
    "domain": "金融",
    "title": "An Analytic COS Method for Compound Option Valuation",
    "url": "https://arxiv.org/abs/2607.25599",
    "source": "Zhipeng Huang, Cornelis W. Oosterlee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:00:00+00:00",
    "summary": "arXiv:2607.25599v1 Announce Type: new Abstract: We develop an analytic Fourier cosine (COS) method for the valuation of compound options. By deriving closed-form expressions for the cosine coefficient"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.25162",
    "domain": "金融",
    "title": "Quantum Transformer BSDE Solver via Multi-Layer Fully-Connected Variational Quantum Circuits",
    "url": "https://arxiv.org/abs/2607.25162",
    "source": "Howard Su, Huan-Hsin Tseng, Chi-Sheng Chen, Lance Bai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:00:00+00:00",
    "summary": "arXiv:2607.25162v1 Announce Type: cross Abstract: Solving high-dimensional parabolic partial differential equations (PDEs) is important in engineering, physics, and stochastic control. Deep BSDE metho"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.25459",
    "domain": "金融",
    "title": "Emergent Latent-State Computation under Stochastic Volatility",
    "url": "https://arxiv.org/abs/2607.25459",
    "source": "Xiaoyu Huang, Lulu Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:00:00+00:00",
    "summary": "arXiv:2607.25459v1 Announce Type: cross Abstract: Mechanistic interpretability has largely focused on language models and deterministic toy tasks. Much less is known about how sequence models internal"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.26034",
    "domain": "金融",
    "title": "Falling Behind Drives Unsafe Development in an Idealised AI Race Experiment",
    "url": "https://arxiv.org/abs/2607.26034",
    "source": "Elias Fern\\'andez Domingos, The Anh Han",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:00:00+00:00",
    "summary": "arXiv:2607.26034v1 Announce Type: cross Abstract: Technological races create tension between speed and safety: actors may gain by moving faster than competitors, even when risky development is harmful"
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.13878",
    "domain": "金融",
    "title": "Damages and Materiality: Effects on voluntary disclosure",
    "url": "https://arxiv.org/abs/2410.13878",
    "source": "Miles B. Gietzmann, Adam J. Ostaszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:00:00+00:00",
    "summary": "arXiv:2410.13878v3 Announce Type: replace Abstract: How should a court resolve a shareholder--management dispute following a materially significant price decline when it is suspected that management, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.10682",
    "domain": "金融",
    "title": "On data-driven robust distortion risk measures for non-negative risks with partial information",
    "url": "https://arxiv.org/abs/2508.10682",
    "source": "Xiangyu Han, Yijun Hu, Ran Wang, Linxiao Wei",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:00:00+00:00",
    "summary": "arXiv:2508.10682v2 Announce Type: replace Abstract: In this paper, by proposing two new kinds of distributional uncertainty sets, we explore robustness of distortion risk measures against distribution"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.01109",
    "domain": "金融",
    "title": "A stochastic correlation extension of the Vasicek credit risk model",
    "url": "https://arxiv.org/abs/2603.01109",
    "source": "Dhruv Bansal, Mayank Goud, Sourav Majumdar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:00:00+00:00",
    "summary": "arXiv:2603.01109v3 Announce Type: replace Abstract: In this paper we extend the Vasicek credit risk model by modelling the correlation as a continuous-time process. The models for correlation follow d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08232",
    "domain": "金融",
    "title": "Hour-Aware Adaptive Risk Management for Autonomous Memecoin Trading on Solana DEXs: Evidence, Theory, and Design Lessons from a 15-Day Deployment",
    "url": "https://arxiv.org/abs/2606.08232",
    "source": "Arati Uday Kamat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:00:00+00:00",
    "summary": "arXiv:2606.08232v2 Announce Type: replace Abstract: We report a 15-day paper-traded deployment of an autonomous memecoin trading system on Solana decentralised exchanges (DEXs) as a controlled measure"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.22956",
    "domain": "金融",
    "title": "Pareto Optimal Centralized Risk Sharing with Multiple Agents: Inclusivity and Fairness",
    "url": "https://arxiv.org/abs/2606.22956",
    "source": "Debora Daniela Escobar, Wing Fung Chong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:00:00+00:00",
    "summary": "arXiv:2606.22956v2 Announce Type: replace Abstract: This paper studies centralized risk sharing with endogenous prices. Multiple policyholders transfer risks to a central insurer through indemnity dec"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.21534",
    "domain": "金融",
    "title": "Generative AI Availability, Grades, and Student Satisfaction at a Large University",
    "url": "https://arxiv.org/abs/2607.21534",
    "source": "James M. Zumel Dumlao, Meng Wang, Zhonghan Xie, Junyao Hu, Ivan Bar, George Chaney III, Henry Gold, Misha Teplitskiy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-29T04:00:00+00:00",
    "summary": "arXiv:2607.21534v2 Announce Type: replace-cross Abstract: The spread of generative AI (GenAI) in higher education has raised concerns that students offload cognitive effort to AI, earning high grades "
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
  },
  {
    "id": "hn:48880233",
    "domain": "金融",
    "title": "IT administrators are \"fed up\" with Microsoft's \"useless\" apps and Windows 11",
    "url": "https://www.neowin.net/news/it-admins-feel-overwhelmingly-sick-of-microsoft-and-windows-11-garbage-apps-products/",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-07-12T11:22:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48723371",
    "domain": "金融",
    "title": "Feds Tracked Down an Anti-ICE Dad in NYC Hotel, but How?",
    "url": "https://gizmodo.com/federal-agents-reportedly-tracked-down-an-anti-ice-dad-in-a-new-york-hotel-its-not-clear-how-2000778714",
    "source": "ripe",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-06-29T18:42:54+00:00",
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
    "id": "hn:48824584",
    "domain": "金融",
    "title": "JPMorgan, BofA and Others Explore Buying Card Network to Raise Debit-Card Fees",
    "url": "https://www.wsj.com/finance/banking/jpmorgan-bank-of-america-and-other-banks-explore-a-deal-to-shake-up-payments-world-9d8639fb",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-07-07T22:04:18+00:00",
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
    "id": "hn:48780128",
    "domain": "金融",
    "title": "AI First: How the Federal Government Is Prioritizing AI over People and Planet",
    "url": "https://stopgreedbuildgreen.climateandcommunity.org/posts/ai-first",
    "source": "eatox",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-03T21:21:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48796110",
    "domain": "金融",
    "title": "Moving back home used to be a sign of failure. Now it shows financial savvy",
    "url": "https://www.wsj.com/lifestyle/relationships/living-with-parents-finances-0c35530c",
    "source": "apparent",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-07-05T17:34:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48849827",
    "domain": "金融",
    "title": "FrontierFinance: The largest open benchmark for investor workflows",
    "url": "https://research.samaya.ai/benchmarks/frontier-finance",
    "source": "ashwinpp",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-09T17:49:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48824532",
    "domain": "金融",
    "title": "SpaceX Shares Stumble in Nasdaq-100 Debut",
    "url": "https://www.wsj.com/finance/stocks/spacex-shares-stumble-in-nasdaq-100-debut-9ec10565",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-07T22:00:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48719682",
    "domain": "金融",
    "title": "Supreme Court rules Trump cannot fire Fed member Lisa Cook",
    "url": "https://www.nbcnews.com/politics/supreme-court/supreme-court-rules-trump-cannot-fire-fed-member-lisa-cook-grants-powe-rcna234931",
    "source": "ceejayoz",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-06-29T14:24:41+00:00",
    "summary": ""
  }
]
```
