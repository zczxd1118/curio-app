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

- 今日日期：`2026-08-02`
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
  "date": "2026-08-02",
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
    "points": 4041325,
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
    "points": 1647438,
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
    "points": 1533953,
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
    "points": 1303476,
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
    "points": 1022568,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 1016063,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 989899,
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
    "points": 867979,
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
    "points": 584867,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 455406,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 431635,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 391147,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 390086,
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
    "points": 253976,
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
    "points": 216737,
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
    "points": 198773,
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
    "points": 178309,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 130598,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV172GP6rEZs",
    "domain": "AI",
    "title": "🚀DeepSeek V4 Flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！",
    "url": "http://www.bilibili.com/video/av117014605731815",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 127093,
    "published_at": "2026-07-31T12:42:57+00:00",
    "summary": "🚀DeepSeek v4 flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！性能、速度与真实短板全曝光！对比Kimi K3后优点和缺点都藏不住了\n\nDeepSeek 发布了 DeepSeek V4 Flash 0731：284B 总参数、13B 激活参数、100 万 Token 上下文，官方基准表现接近 Claude"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 115315,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92892,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1Tv3i6LEX1",
    "domain": "AI",
    "title": "用Codex、cursor 还是Claude ？程序员不作选择题，我都要用，还一起用 | Orca ADE 介绍",
    "url": "http://www.bilibili.com/video/av116996217838997",
    "source": "技术胖",
    "platform": "bilibili",
    "points": 79696,
    "published_at": "2026-07-28T06:41:31+00:00",
    "summary": "如果能把 Codex、Claude Code、Grok、Cursor 等智能编程工具整合到同一个工作环境中，再让多个 Agent 像团队成员一样分工协作，软件开发的效率将得到显著提升。Orca ADE 正是为此而生：它是一款开源、免费的 Agent 开发环境，专注于代码管理与命令行工作流，不仅能够接入多种编程 Agent，还支持语音操作和手机远程管理。接下来，我们就来认识一下 Orca ADE，看"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73965,
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
    "points": 53512,
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
    "points": 47531,
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
    "points": 44910,
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
    "points": 39622,
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
    "points": 39209,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 38524,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 31093,
    "published_at": "2026-05-07T00:00:00+00:00",
    "summary": "全栈课一共分为6大块内容\n第一块：AI智能体开发基础(AI大模型、工具、记忆、MCP、中间件、Skills等核心内容)\n第二块：Claude Code,Trea+skills实现基于需求文档生成用例，基于OpenClaw实现接口自动化落地，基于hermes Agent实现web自动化落地\n第三块：功能测试的智能体开发(项目RAG知识库搭建+Agent搭建+skills开发，实现用例生成的Agent"
  },
  {
    "id": "bvid:BV16ggC6DEZK",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116963049212769",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 25912,
    "published_at": "2026-07-22T10:10:42+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 25887,
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
    "points": 22677,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 19306,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 18173,
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
    "points": 17609,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1hnjGzLE14",
    "domain": "AI",
    "title": "【小智教程】手挽手教你如何接入别人的MCP服务",
    "url": "http://www.bilibili.com/video/av114568722450105",
    "source": "空白泡泡糖果",
    "platform": "bilibili",
    "points": 17586,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV1B7KE6NEBU",
    "domain": "AI",
    "title": "以防你不知道Claude Code开Ultracode思考强度会有雷霆特效",
    "url": "http://www.bilibili.com/video/av116933437425926",
    "source": "公孙芳芸",
    "platform": "bilibili",
    "points": 17556,
    "published_at": "2026-07-17T04:31:11+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "7月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "iwenwikii",
    "platform": "bilibili",
    "points": 16557,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "AI充值站：njzqhy.top"
  },
  {
    "id": "bvid:BV1dsNv66E3Q",
    "domain": "AI",
    "title": "【Cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116922599344955",
    "source": "六月要癫",
    "platform": "bilibili",
    "points": 14645,
    "published_at": "2026-07-15T06:39:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1YJ336EEBk",
    "domain": "AI",
    "title": "【AI陪玩】开袋即食的AI接入我的世界教程！",
    "url": "http://www.bilibili.com/video/av116981806143216",
    "source": "万昇Dwin",
    "platform": "bilibili",
    "points": 13112,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "模组：Numen\n项目地址：https://github.com/Dwinovo/minecraft-numen"
  },
  {
    "id": "bvid:BV1YGKJ6tEdz",
    "domain": "AI",
    "title": "Vibe Coding我的赛博女友",
    "url": "http://www.bilibili.com/video/av116933101950817",
    "source": "天工开帧",
    "platform": "bilibili",
    "points": 10935,
    "published_at": "2026-07-17T09:50:00+00:00",
    "summary": "Vibe Coding大赏之赛博女友。总体花费100个馒头左右，由于显存限制，目前实时数字人的版本没办法跑起来。目前可以24挂着，随时对话随时打断。作用嘛，除了聊天就是在我忙的时候顺手帮我查个东西。未来开发方向接入pi-agent，让它真正干活，当然，只是得上qwen27B以上得模型才有可用性。也就是说所有模型显存开销打底得36G以上。囧。当然如果不要无限制，可以接入在线模型或在线TTS，但是，我"
  },
  {
    "id": "bvid:BV1CU346yEYC",
    "domain": "AI",
    "title": "聊聊Vibe Coding | AI降低了门槛，也降低了成本吗？",
    "url": "http://www.bilibili.com/video/av117008079392929",
    "source": "糖果果的陈同学",
    "platform": "bilibili",
    "points": 10475,
    "published_at": "2026-07-30T08:57:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9271,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 8829,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 8100,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1gf3T6KEef",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！从环境搭建到工作流完整闭环，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116979708990688",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 7988,
    "published_at": "2026-07-25T08:47:37+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV14uTM69EUd",
    "domain": "AI",
    "title": "破甲claude/减少claude道德约束/ai破解卡密",
    "url": "http://www.bilibili.com/video/av116826918880943",
    "source": "去码头整点海鸥啊",
    "platform": "bilibili",
    "points": 7848,
    "published_at": "2026-06-28T09:05:03+00:00",
    "summary": "企鹅交流群：1038830654"
  },
  {
    "id": "bvid:BV1mtGK6hEKC",
    "domain": "AI",
    "title": "Deepseek V4 Flash最新测评！Claude Code版！",
    "url": "http://www.bilibili.com/video/av117015578676037",
    "source": "AI产品狙击手",
    "platform": "bilibili",
    "points": 6956,
    "published_at": "2026-07-31T16:41:51+00:00",
    "summary": "上期完成 DeepSeek V4 Flash 在 Codex 平台测评，本期统一拉满 High 思考深度接入 Claude Code 复测，用全套标准化用例横向对比模型真实表现，基础指令、24 点运算、密码锁逻辑推理全部答对，仅十条顺序句子存在单句通顺度瑕疵；代码生成环节暴露统一痛点，所有大型开发任务耗时动辄数十分钟，判断是新模型上线调用高峰算力拥堵导致，自制桌面操作系统成品完整性不及 Codex"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 7013,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "hn:49035303",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, Microsoft, Meta warn against overregulating open-weight models",
    "url": "https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 659,
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
    "points": 339,
    "published_at": "2026-07-24T12:53:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49122838",
    "domain": "AI 算力 / 半导体",
    "title": "Moonshot’s Kimi uses 20k Nvidia chip cluster from Alibaba",
    "url": "https://www.bloomberg.com/news/articles/2026-07-31/moonshot-s-kimi-built-on-20-000-nvidia-chip-cluster-from-alibaba",
    "source": "gk1",
    "platform": "hackernews",
    "points": 113,
    "published_at": "2026-07-31T13:24:03+00:00",
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
    "id": "hn:49125140",
    "domain": "AI 算力 / 半导体",
    "title": "Hygon Reveals 512-Thread CPU and AI GPU to Rival Intel Xeon and Nvidia",
    "url": "https://www.ubergizmo.com/2026/06/hygon-512-thread-cpu/",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-31T16:21:11+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/humanoid-manipulation-at-the-edge-of-physical-interaction/",
    "domain": "AI 算力 / 半导体",
    "title": "Humanoid Manipulation at the Edge of Physical Interaction",
    "url": "https://www.eetimes.com/humanoid-manipulation-at-the-edge-of-physical-interaction/",
    "source": "Renesas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T14:00:00+00:00",
    "summary": "This white paper examines emerging humanoid robot architectures, focusing on how joints and dexterous hands are becoming intelligent, sensor-rich subsystems that require tightly integrated control, co"
  },
  {
    "id": "rss:https://www.eetimes.com/erp-statistics-insights-from-70-manufacturing-case-studies/",
    "domain": "AI 算力 / 半导体",
    "title": "ERP Statistics: Insights From 70 Manufacturing Case Studies",
    "url": "https://www.eetimes.com/erp-statistics-insights-from-70-manufacturing-case-studies/",
    "source": "MRPeasy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T13:00:00+00:00",
    "summary": "We analyzed 70 customer case studies to better understand the ERP experiences of small manufacturers. Here’s what electronics manufacturers had to say. The post ERP Statistics: Insights From 70 Manufa"
  },
  {
    "id": "rss:https://www.eetimes.com/cea-leti-pushes-stacking-roadmap-as-ai-runs-into-memory-and-power-limits/",
    "domain": "AI 算力 / 半导体",
    "title": "CEA-Leti Pushes Stacking Roadmap as AI Runs Into Memory and Power Limits",
    "url": "https://www.eetimes.com/cea-leti-pushes-stacking-roadmap-as-ai-runs-into-memory-and-power-limits/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:48:06+00:00",
    "summary": "AI’s memory wall is turning packaging into architecture as CEA-Leti bets on 3D stacking, chiplets, and cooler power. The post CEA-Leti Pushes Stacking Roadmap as AI Runs Into Memory and Power Limits a"
  },
  {
    "id": "rss:https://www.eetimes.com/hybrid-architectures-for-space-missions-frameworks-and-consequence/",
    "domain": "AI 算力 / 半导体",
    "title": "Hybrid Architectures for Space Missions: Frameworks and Consequence",
    "url": "https://www.eetimes.com/hybrid-architectures-for-space-missions-frameworks-and-consequence/",
    "source": "Microchip Technology, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:38:20+00:00",
    "summary": "Join this webinar and explore how Microchip's framework translates architectural intent into component choices that preserve differentiation and margin. The post Hybrid Architectures for Space Mission"
  },
  {
    "id": "rss:https://www.eetimes.com/the-commercial-space-race-powering-the-next-comms-network/",
    "domain": "AI 算力 / 半导体",
    "title": "The Commercial Space Race: Powering the Next Comms Network",
    "url": "https://www.eetimes.com/the-commercial-space-race-powering-the-next-comms-network/",
    "source": "Altera, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T13:34:44+00:00",
    "summary": "Join us to learn how Altera is supporting commercial deployments in orbit today and what's coming next. The post The Commercial Space Race: Powering the Next Comms Network appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/military-ai-agents-under-cyberthreat-the-route-forward/",
    "domain": "AI 算力 / 半导体",
    "title": "Military AI Agents Under Cyberthreat: The Route Forward",
    "url": "https://www.eetimes.com/military-ai-agents-under-cyberthreat-the-route-forward/",
    "source": "Liam Critchley",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T07:30:00+00:00",
    "summary": "Rapid military AI adoption brings critical security risks, leaving autonomous battlefield systems vulnerable to cyberattacks. The post Military AI Agents Under Cyberthreat: The Route Forward appeared "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/dell-founder-shows-how-a-usd100-billion-empire-started-42-years-ago-ceo-says-this-one-page-changed-my-life",
    "domain": "AI 算力 / 半导体",
    "title": "Dell founder shows how a $100 billion empire started 42 years ago — CEO says ‘This one page changed my life’",
    "url": "https://www.tomshardware.com/tech-industry/dell-founder-shows-how-a-usd100-billion-empire-started-42-years-ago-ceo-says-this-one-page-changed-my-life",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T17:06:31+00:00",
    "summary": "Billionaire Michael Dell reminisced about the early days of his company, sharing an early quarterly earnings report that showed the then-startup making nearly $135,000 in just three months. Dell says "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/score-the-ultimate-amd-am4-starter-pack-with-a-six-core-cpu-and-16gb-ram-for-only-usd280-kickstart-your-next-pc-build-with-usd138-in-savings",
    "domain": "AI 算力 / 半导体",
    "title": "Score the ultimate AMD AM4 starter pack with a six-core CPU and 16GB RAM for only $280 — kickstart your next PC build with $138 in savings",
    "url": "https://www.tomshardware.com/pc-components/score-the-ultimate-amd-am4-starter-pack-with-a-six-core-cpu-and-16gb-ram-for-only-usd280-kickstart-your-next-pc-build-with-usd138-in-savings",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T15:09:27+00:00",
    "summary": "If you've been hesitating to upgrade to a modern platform because of the state of the PC hardware industry, this combo deal might be the one for you."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/microsoft-vows-to-make-windows-11-fly-on-8gb-ram-amid-memory-shortage-optimizations-to-reduce-os-memory-footprint-have-begun",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft vows to make Windows 11 fly on 8GB RAM amid memory shortage — optimizations to reduce OS memory footprint have begun",
    "url": "https://www.tomshardware.com/software/windows/microsoft-vows-to-make-windows-11-fly-on-8gb-ram-amid-memory-shortage-optimizations-to-reduce-os-memory-footprint-have-begun",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T14:48:26+00:00",
    "summary": "While the company's minimum OS specifications officially say 4GB, most PC builders know that 16GB is the bare minimum for a smooth experience on Windows 11. However, the memory chip shortage and the r"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-claude-hacked-three-real-life-companies-during-security-capabilities-test-test-environment-with-internet-access-and-unwitting-targets-lax-cybersecurity-practices-led-to-bots-running-rampant",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic's Claude hacked three real-life companies during security capabilities test — test environment with internet access and unwitting targets' lax cybersecurity practices led to bots running ram",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-claude-hacked-three-real-life-companies-during-security-capabilities-test-test-environment-with-internet-access-and-unwitting-targets-lax-cybersecurity-practices-led-to-bots-running-rampant",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T12:30:00+00:00",
    "summary": "Anthropic's Claude hacked three real-life companies during security capabilities test — open test environment and unwitting targets' lax cybersecurity practices led bots run rampant"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/nozzlegate-erupts-as-prusa-core-one-3d-ptinter-kits-arrive-with-soft-steel-nozzles-bondtech-admits-machining-flaws-with-no-quick-fix",
    "domain": "AI 算力 / 半导体",
    "title": "'Nozzlegate' erupts as Prusa CORE One 3D printer kits arrive with soft steel nozzles — Bondtech admits machining flaws with no quick fix",
    "url": "https://www.tomshardware.com/3d-printing/nozzlegate-erupts-as-prusa-core-one-3d-ptinter-kits-arrive-with-soft-steel-nozzles-bondtech-admits-machining-flaws-with-no-quick-fix",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T12:10:57+00:00",
    "summary": "Bondtech, the creator and manufacturer of the INDX toolchanger system used to create the highly anticipated Prusa CORE One+ INDX, admitted to a significant labeling mistake. The nozzles provided with "
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/sony-doubles-down-on-axing-physical-game-discs-cfo-reiterates-were-going-to-cautiously-move-this-forward",
    "domain": "AI 算力 / 半导体",
    "title": "Sony doubles down on axing physical game discs — CFO reiterates 'we’re going to cautiously move this forward'",
    "url": "https://www.tomshardware.com/video-games/playstation/sony-doubles-down-on-axing-physical-game-discs-cfo-reiterates-were-going-to-cautiously-move-this-forward",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T11:00:00+00:00",
    "summary": "Sony confirms that its stance has not changed on ending the production of physical game discs for titles released after January 2028."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/97-untouched-duck-hunt-and-super-mario-bros-cartridges-worth-thousands-discovered-in-retro-shop-storage-room-never-before-seen-version-of-popular-nes-games-include-five-perfect-10-psa-items",
    "domain": "AI 算力 / 半导体",
    "title": "97 untouched Duck Hunt and Super Mario Bros. cartridges worth thousands discovered in retro shop storage room — never-before-seen version of popular NES games include five perfect 10 PSA items",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/97-untouched-duck-hunt-and-super-mario-bros-cartridges-worth-thousands-discovered-in-retro-shop-storage-room-never-before-seen-version-of-popular-nes-games-include-five-perfect-10-psa-items",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T10:00:00+00:00",
    "summary": "A retro gaming shop in Wisconsin finds a box of unopened, never-before-seen versions of Duck Hunt and Super Mario Bros. in its storage room. These items are probably worth four to five digits, and the"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/lost-one-of-a-kind-nintendo-ds-cartridge-hits-ebay-for-usd9-100-pokepark-fishing-contest-designed-to-delete-itself-after-12-hours-game-so-rare-it-was-only-distributed-to-theme-park-attendees-in-2005",
    "domain": "AI 算力 / 半导体",
    "title": "Lost one-of-a-kind Nintendo DS cartridge hits eBay for $9,100 — PokePark Fishing Contest designed to delete itself after 12 hours, game so rare it was only distributed to theme park attendees in 2005",
    "url": "https://www.tomshardware.com/video-games/nintendo/lost-one-of-a-kind-nintendo-ds-cartridge-hits-ebay-for-usd9-100-pokepark-fishing-contest-designed-to-delete-itself-after-12-hours-game-so-rare-it-was-only-distributed-to-theme-park-attendees-in-2005",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T09:00:00+00:00",
    "summary": "A Nintendo DS game that was classified as ‘lost media’ for nearly two decades is now within tantalizing reach of video gaming fans and archivists."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/big-tech-spends-more-than-usd1-trillion-on-ai-infrastructure-additional-usd745-billion-expected-to-be-added-to-the-figure-in-2026-alone",
    "domain": "AI 算力 / 半导体",
    "title": "Big tech spends more than $1 trillion on AI infrastructure — additional $745 billion expected to be added to the figure in 2026 alone",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/big-tech-spends-more-than-usd1-trillion-on-ai-infrastructure-additional-usd745-billion-expected-to-be-added-to-the-figure-in-2026-alone",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T16:30:34+00:00",
    "summary": "Amazon, Google, Meta, and Microsoft have collectively spent more than $1 trillion on AI investments since the rush started in 2023. However, the big four are planning to spend more on AI CAPEX, with b"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/30-years-of-cpus-at-toms-hardware-looking-back-on-three-decades-of-processors-from-the-pentium-ii-to-ryzen-9-9950x3d2",
    "domain": "AI 算力 / 半导体",
    "title": "30 years of CPUs at Tom’s Hardware — looking back on three decades of processors, from the Pentium II to Ryzen 9 9950X3D2",
    "url": "https://www.tomshardware.com/pc-components/cpus/30-years-of-cpus-at-toms-hardware-looking-back-on-three-decades-of-processors-from-the-pentium-ii-to-ryzen-9-9950x3d2",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:13:36+00:00",
    "summary": "Tom’s Hardware has been covering CPUs for 30 years, and to celebrate, we’re looking back on the last three decades of CPU reviews and how the dynamics between Intel and AMD have shifted in that time."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/toms-hardwares-30th-anniversary-from-dip-switches-and-intel-feuds-to-30-years-of-unbiased-testing",
    "domain": "AI 算力 / 半导体",
    "title": "Tom’s Hardware’s 30th Anniversary — From Intel feuds and DIP switches to 30 years of unbiased testing",
    "url": "https://www.tomshardware.com/pc-components/toms-hardwares-30th-anniversary-from-dip-switches-and-intel-feuds-to-30-years-of-unbiased-testing",
    "source": "Paul Alcorn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:05:30+00:00",
    "summary": "We take a look back at the history of Tom’s Hardware as we celebrate our 30-year anniversary."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/apple-nearly-doubled-its-inventory-to-11-09-billion-as-memory-costs-ate-its-gross-margin",
    "domain": "AI 算力 / 半导体",
    "title": "Apple CEO Tim Cook says the company is fighting 'a hundred-year flood' on memory pricing — expects to pay even more for memory in September following recent price hikes",
    "url": "https://www.tomshardware.com/tech-industry/apple-nearly-doubled-its-inventory-to-11-09-billion-as-memory-costs-ate-its-gross-margin",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T14:54:55+00:00",
    "summary": "Apple will pay even more for memory in the September quarter than it did in the June quarter, CEO Tim Cook told analysts on the company's earnings call."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/beat-the-ai-price-surge-on-pc-hardware-leverage-newegg-combo-deals-track-amazon-prices-and-shop-refurb-outlets-like-woot",
    "domain": "AI 算力 / 半导体",
    "title": "Beat the AI price surge on PC hardware — leverage Newegg combo deals, track Amazon prices, and shop refurb outlets like Woot",
    "url": "https://www.tomshardware.com/pc-components/beat-the-ai-price-surge-on-pc-hardware-leverage-newegg-combo-deals-track-amazon-prices-and-shop-refurb-outlets-like-woot",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T13:10:00+00:00",
    "summary": "With prices skyrocketing, it’s more important than ever to follow these guidelines to help you find great deals on PC hardware."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/lumentum-ceo-says-the-indium-phosphide-shortage-will-become-worse-than-memory",
    "domain": "AI 算力 / 半导体",
    "title": "Lumentum CEO warns of impending bottleneck on critical material used for silicon photonics — fab and material shortfall already lags 30% below customer needs as co-packaged optics demand skyrockets",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/lumentum-ceo-says-the-indium-phosphide-shortage-will-become-worse-than-memory",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:45:27+00:00",
    "summary": "Lumentum CEO Michael Hurlston told an audience at the RAISE Summit that indium phosphide is heading into a squeeze worse than the one in memory."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/streaming-qr-codes-at-60-fps-achieves-nearly-190-kb-s-data-rate-in-phone-to-phone-tests-browser-based-method-requires-no-app-no-networking-no-pairing-and-no-permissions-beyond-camera-access",
    "domain": "AI 算力 / 半导体",
    "title": "Streaming QR codes at 60 FPS achieves nearly 190 KB/s data rate in phone-to-phone tests — browser-based method requires no app, no networking, no pairing, and no permissions beyond camera access",
    "url": "https://www.tomshardware.com/networking/streaming-qr-codes-at-60-fps-achieves-nearly-190-kb-s-data-rate-in-phone-to-phone-tests-browser-based-method-requires-no-app-no-networking-no-pairing-and-no-permissions-beyond-camera-access",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:45:20+00:00",
    "summary": "A developer has created a QR code-driven proof-of-concept data transfer system that shuns any dedicated app requirement and neatly sidesteps mandatory networking, pairing, or giving permissions beyond"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/docking-stations-hubs/testing-three-sub-usd400-thunderbolt-5-docking-stations",
    "domain": "AI 算力 / 半导体",
    "title": "Sub-$400 Thunderbolt 5 dock roundup — Keychron and Plugable offer dual HDMI, but UGREEN takes top spot with an M.2 NVMe slot",
    "url": "https://www.tomshardware.com/peripherals/docking-stations-hubs/testing-three-sub-usd400-thunderbolt-5-docking-stations",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:40:00+00:00",
    "summary": "All three Thunderbolt 5 docks offer similar performance, but one really stands out with its features."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/valve-funding-port-of-linux-radv-radeon-vulkan-driver-to-windows-cross-platform-effort-already-runs-counter-strike-2",
    "domain": "AI 算力 / 半导体",
    "title": "Valve funding port of Linux RADV Radeon Vulkan driver to Windows — cross-platform effort already runs 'Counter-Strike 2'",
    "url": "https://www.tomshardware.com/software/linux/valve-funding-port-of-linux-radv-radeon-vulkan-driver-to-windows-cross-platform-effort-already-runs-counter-strike-2",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:25:00+00:00",
    "summary": "Valve funding port of Linux RADV Radeon Vulkan driver to Windows — cross-platform effort already runs Counter-Strike 2"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/setting-up-openclaw-isnt-as-straightforward-as-the-internet-wants-you-to-think-running-local-ai-on-humble-hardware",
    "domain": "AI 算力 / 半导体",
    "title": "Setting up OpenClaw isn’t as straightforward as the internet wants you to think – running local AI on humble hardware",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/setting-up-openclaw-isnt-as-straightforward-as-the-internet-wants-you-to-think-running-local-ai-on-humble-hardware",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:20:00+00:00",
    "summary": "How realistic is it to run a local AI model and have it automate tasks for you using hardware that doesn’t cost the Earth? We gave it a shot with a Gorgon Point-powered Mini PC, with mixed results."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/sovol-m1d-3d-printer-is-the-first-open-source-idex-design-with-an-integrated-tool-changer-seven-heads-for-quick-swapping-materials-with-two-fully-independent-nozzles",
    "domain": "AI 算力 / 半导体",
    "title": "New open source printer has 7 toolheads that swap in 5 seconds for fast, zero-waste multi-color 3D printing — Sovol M1D 3D printer is the first open-source IDEX design with an integrated tool-changer",
    "url": "https://www.tomshardware.com/3d-printing/sovol-m1d-3d-printer-is-the-first-open-source-idex-design-with-an-integrated-tool-changer-seven-heads-for-quick-swapping-materials-with-two-fully-independent-nozzles",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T12:00:00+00:00",
    "summary": "Sovol M1D 3D printer is the first open-source IDEX design with an integrated tool-changer — seven heads for quick-swapping materials with two fully independent nozzles, with 300x300x350mm print volume"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/single-dimm-ddr5-gaming-works-better-than-you-probably-think-amds-3d-v-cache-chips-drop-less-than-3-percent-one-ddr5-dimm-beats-dual-channel-ddr4-ram",
    "domain": "AI 算力 / 半导体",
    "title": "Single-DIMM DDR5 gaming works better than you probably think — one DDR5 DIMM beats dual-channel DDR4 RAM, AMD's 3D V-Cache chips drop less than 3% with single stick",
    "url": "https://www.tomshardware.com/pc-components/ddr5/single-dimm-ddr5-gaming-works-better-than-you-probably-think-amds-3d-v-cache-chips-drop-less-than-3-percent-one-ddr5-dimm-beats-dual-channel-ddr4-ram",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T11:43:24+00:00",
    "summary": "To avoid rising RAM costs, some PC builders and OEMs have shifted toward using a single DDR5 module for gaming PCs. We test how much of a performance loss that actually represents."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/are-your-motherboards-m-2-heatsinks-making-good-contact-with-your-ssd-we-tested-20-modern-intel-and-amd-motherboards-to-verify",
    "domain": "AI 算力 / 半导体",
    "title": "Your motherboard's M.2 SSD heatsink might be slowing down your SSD — Only 6 of 20 tested boards made full contact",
    "url": "https://www.tomshardware.com/pc-components/motherboards/are-your-motherboards-m-2-heatsinks-making-good-contact-with-your-ssd-we-tested-20-modern-intel-and-amd-motherboards-to-verify",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T11:43:19+00:00",
    "summary": "We tested 20 motherboards for proper M.2 contact and were surprised at the results – not all make good contact."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/ps5-emulation-hits-new-milestone-in-record-time-multiple-3d-games-now-playable-in-kyty-performance-and-support-steadily-improving-with-30-fps-gameplay-possible-today",
    "domain": "AI 算力 / 半导体",
    "title": "PS5 emulation hits new milestone in record time, multiple 3D games now playable in Kyty — Performance and support steadily improving with 30 FPS gameplay possible today",
    "url": "https://www.tomshardware.com/video-games/playstation/ps5-emulation-hits-new-milestone-in-record-time-multiple-3d-games-now-playable-in-kyty-performance-and-support-steadily-improving-with-30-fps-gameplay-possible-today",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T11:40:00+00:00",
    "summary": "The PS5 emulation scene is showing extremely impressive progress, with 3D titles now being playable at around 30 FPS just two weeks after the first 3D titles even became bootable."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amds-new-radeon-rx-9050-is-roughly-30-percent-slower-than-the-rtx-5050-in-games-early-testing-shows-the-cheapest-8gb-rdna-4-gpu-comfortably-handles-1080p-gaming-but-doesnt-impress",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's new Radeon RX 9050 is roughly 30% slower than the RTX 5050 in games, early testing shows — the cheapest 8GB RDNA 4 GPU comfortably handles 1080p gaming but doesn't impress",
    "url": "https://www.tomshardware.com/pc-components/gpus/amds-new-radeon-rx-9050-is-roughly-30-percent-slower-than-the-rtx-5050-in-games-early-testing-shows-the-cheapest-8gb-rdna-4-gpu-comfortably-handles-1080p-gaming-but-doesnt-impress",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T11:28:54+00:00",
    "summary": "The RX 9050 is slower than the RTX 5050 in every conceivable way except when the latter is constrained in some way. It performs worse in synthetic benchmarks and games but has more efficient power con"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/msi-promises-an-expo-ull-like-boost-for-your-existing-ddr5-high-efficiency-mode-brings-low-latency-tuning-to-older-ram",
    "domain": "AI 算力 / 半导体",
    "title": "MSI promises an EXPO ULL-like boost for your existing DDR5 memory — High-Efficiency Mode brings low-latency tuning to older RAM",
    "url": "https://www.tomshardware.com/pc-components/motherboards/msi-promises-an-expo-ull-like-boost-for-your-existing-ddr5-high-efficiency-mode-brings-low-latency-tuning-to-older-ram",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T11:20:00+00:00",
    "summary": "A new firmware update for MSI motherboards features High-Efficiency Mode, which offers latency tuning similar to AMD's EXPO ULL on regular memory kits."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd900-on-this-rtx-5070-gaming-pc-from-msi-in-this-limited-time-woot-deal-now-usd1-399-grab-a-huge-saving-on-this-codex-r2-rig-with-a-10-core-intel-cpu-32gb-ddr5-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save $900 on this RTX 5070 gaming PC from MSI in this limited-time Woot deal, now $1,399 — grab a huge saving on this Codex R2 rig with a 10-core Intel CPU, 32GB DDR5, and a 1TB SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd900-on-this-rtx-5070-gaming-pc-from-msi-in-this-limited-time-woot-deal-now-usd1-399-grab-a-huge-saving-on-this-codex-r2-rig-with-a-10-core-intel-cpu-32gb-ddr5-and-a-1tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T11:03:17+00:00",
    "summary": "This MSI Codex R2 gaming PC is on sale at Woot for $1,399.99 right now, delivering you a rig with a 10-core Intel Core i5-14400F, Nvidia GeForce RTX 5070, 32GB of DDR5 RAM, and a 1TB SSD."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/samsungs-fastest-ssd-is-back-to-prime-day-pricing-only-usd30-difference-between-the-much-faster-gen-5-9100-pro-and-gen-4-990",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung's fastest SSD is back to Prime Day pricing — only $30 difference between the much faster Gen 5 9100 Pro and Gen 4 990",
    "url": "https://www.tomshardware.com/pc-components/ssds/samsungs-fastest-ssd-is-back-to-prime-day-pricing-only-usd30-difference-between-the-much-faster-gen-5-9100-pro-and-gen-4-990",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T11:00:29+00:00",
    "summary": "Returning to Prime Day pricing, Samsung's fastest SSD, the 9100 Pro 2TB, is just $10 more than the previous PCIe generation's champion, the 2TB Samsung 990 Pro SSD."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/modder-der8auer-builds-110cm-3d-printed-chimney-to-passively-cool-ryzen-7-9800x3d-without-fans-radically-simple-pc-mod-cuts-down-cpu-temps-by-19-c-using-the-stack-effect",
    "domain": "AI 算力 / 半导体",
    "title": "Modder der8auer builds 110cm 3D-printed chimney to passively cool Ryzen 7 9800X3D without fans, cuts temps by 19C — radically simple PC mod uses the 'stack effect'",
    "url": "https://www.tomshardware.com/pc-components/cooling/modder-der8auer-builds-110cm-3d-printed-chimney-to-passively-cool-ryzen-7-9800x3d-without-fans-radically-simple-pc-mod-cuts-down-cpu-temps-by-19-c-using-the-stack-effect",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T11:00:00+00:00",
    "summary": "What if instead of relying on mechanical pressure generated by fans, you could just passively cool your PC using natural convection? That's what der8auer managed to pull off in his new experiment usin"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/robotics/qualcomm-powered-robot-collapses-spectacularly-on-stage-during-presentation-prepared-stagehands-rush-to-cloak-and-then-carry-off-stricken-humanoid",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm-powered robot collapses spectacularly on stage during company's keynote — prepared stagehands rush to cloak and then carry off stricken humanoid (updated)",
    "url": "https://www.tomshardware.com/tech-industry/robotics/qualcomm-powered-robot-collapses-spectacularly-on-stage-during-presentation-prepared-stagehands-rush-to-cloak-and-then-carry-off-stricken-humanoid",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T10:40:00+00:00",
    "summary": "A Qualcomm exec suffered from one of the most disastrous tech demos we’ve ever seen live on stage at Computex 2026 this summer when a humanoid robot spectacularly collapsed."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/mice/keyboard-giant-keychron-launches-nape-pro-wireless-trackball-mouse-rectangular-form-factor-designed-to-sit-under-spacebar-gives-users-six-customizable-buttons-and-a-control-dial",
    "domain": "AI 算力 / 半导体",
    "title": "Keyboard giant Keychron launches Nape Pro wireless trackball mouse — rectangular form factor designed to sit under spacebar gives users six customizable buttons and a control dial",
    "url": "https://www.tomshardware.com/peripherals/mice/keyboard-giant-keychron-launches-nape-pro-wireless-trackball-mouse-rectangular-form-factor-designed-to-sit-under-spacebar-gives-users-six-customizable-buttons-and-a-control-dial",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T10:25:24+00:00",
    "summary": "The Nape Pro wireless trackball mouse features a rectangular form factor, six customizable buttons, and a control dial. Its unique shape and wireless connectivity let users place it anywhere they like"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/if-you-own-a-3d-printer-you-absolutely-need-to-try-hi3d",
    "domain": "AI 算力 / 半导体",
    "title": "If You Own a 3D Printer, You Absolutely Need to Try Hi3D",
    "url": "https://www.tomshardware.com/3d-printing/if-you-own-a-3d-printer-you-absolutely-need-to-try-hi3d",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T10:20:00+00:00",
    "summary": "Let AI Handle Every Tedious Slicing Step in One Click"
  },
  {
    "id": "rss:https://www.eetimes.com/space-grown-semiconductors-the-next-frontier-for-ai-compute/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Is Compressing Software; Space Is Building the Physical Economy",
    "url": "https://www.eetimes.com/space-grown-semiconductors-the-next-frontier-for-ai-compute/",
    "source": "Zaheer Ali",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T21:03:54+00:00",
    "summary": "AI is squeezing software jobs; space and semiconductors are where tech turns physical. The post AI Is Compressing Software; Space Is Building the Physical Economy appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/why-qualcomm-bought-an-open-ai-software-stack/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Qualcomm Bought An Open AI Software Stack",
    "url": "https://www.eetimes.com/why-qualcomm-bought-an-open-ai-software-stack/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T14:43:40+00:00",
    "summary": "Modular says Qualcomm is committed to keeping Mojo and Max hardware-agnostic as heterogeneous AI infrastructure moves from theory to reality. The post Why Qualcomm Bought An Open AI Software Stack app"
  },
  {
    "id": "rss:https://www.eetimes.com/nidec-positions-precision-reducers-for-cobots-humanoids-and-automation/",
    "domain": "AI 算力 / 半导体",
    "title": "Nidec Positions Precision Reducers for Cobots, Humanoids, and Automation",
    "url": "https://www.eetimes.com/nidec-positions-precision-reducers-for-cobots-humanoids-and-automation/",
    "source": "Nidec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T13:00:00+00:00",
    "summary": "Discover Nidec's gear reducer solutions offering precise gear alignment, and low backlash for smooth, reliable operation under load. The post Nidec Positions Precision Reducers for Cobots, Humanoids, "
  },
  {
    "id": "rss:https://www.eetimes.com/indian-startup-vimag-labs-develops-wirelessly-excited-motor-without-rare-earth-magnets/",
    "domain": "AI 算力 / 半导体",
    "title": "Indian Startup Vimag Labs Develops Wirelessly Excited Motor Without Rare-Earth Magnets",
    "url": "https://www.eetimes.com/indian-startup-vimag-labs-develops-wirelessly-excited-motor-without-rare-earth-magnets/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-30T07:00:00+00:00",
    "summary": "Vimag Labs ditches rare-earth magnets with a wirelessly excited EV motor claiming PMSM-level punch. The post Indian Startup Vimag Labs Develops Wirelessly Excited Motor Without Rare-Earth Magnets appe"
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
    "id": "hn:49070311",
    "domain": "AI 算力 / 半导体",
    "title": "Ilya Sutskever's SSI and Nvidia Announce Long-Term Strategic Partnership",
    "url": "https://nvidianews.nvidia.com/news/ilya-sutskevers-safe-superintelligence-inc-and-nvidia-announce-long-term-strategic-partnership",
    "source": "lanakei",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-27T14:33:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:49093429",
    "domain": "AI 算力 / 半导体",
    "title": "Kospi Plunges After Nvidia CEO's Visits Spark 'Huang Curse' Fears",
    "url": "https://www.chosun.com/english/market-money-en/2026/07/29/6FEUZWQT5BG3HMJ3G2RZPHROGM/",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-29T04:29:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49111237",
    "domain": "大厂 AI 动态",
    "title": "Gemini Robotics 2 brings whole body intelligence to robots",
    "url": "https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/",
    "source": "ai2027",
    "platform": "hackernews",
    "points": 613,
    "published_at": "2026-07-30T15:15:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49096188",
    "domain": "大厂 AI 动态",
    "title": "Document-borne AI worms can self-propagate through Copilot for Word",
    "url": "https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/",
    "source": "Canopy9560",
    "platform": "hackernews",
    "points": 383,
    "published_at": "2026-07-29T11:44:33+00:00",
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
    "points": 197,
    "published_at": "2026-07-27T09:56:37+00:00",
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
    "id": "hn:49096841",
    "domain": "大厂 AI 动态",
    "title": "Google DeepMind dismantles AlphaFold team",
    "url": "https://www.ft.com/content/61b2953d-ee0d-45de-af6e-a9c1cf524b33",
    "source": "ainch",
    "platform": "hackernews",
    "points": 52,
    "published_at": "2026-07-29T12:50:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:49135399",
    "domain": "大厂 AI 动态",
    "title": "The Bedrock of Software Design",
    "url": "https://alex.draftist.io/blog/the-bedrock-of-software-design-ycqvcedsj",
    "source": "birdculture",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-08-01T15:43:40+00:00",
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
    "id": "rss:https://www.theverge.com/tech/974238/pixel-11-specs-and-price-leak",
    "domain": "大厂 AI 动态",
    "title": "Pixel 11 specs and price leak with no surprises",
    "url": "https://www.theverge.com/tech/974238/pixel-11-specs-and-price-leak",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T21:31:24+00:00",
    "summary": "Android Headlines claims to have the specs and price for the entire Pixel 11 lineup. What the site shared basically lines up with everything else that we've heard in the lead-up to the August 12th eve"
  },
  {
    "id": "rss:https://www.theverge.com/report/974226/angela-nissel-interview-good-grief-pass-the-bread-mom-is-dead",
    "domain": "大厂 AI 动态",
    "title": "Angela Nissel faces down grief with a laugh",
    "url": "https://www.theverge.com/report/974226/angela-nissel-interview-good-grief-pass-the-bread-mom-is-dead",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T20:15:00+00:00",
    "summary": "Angela Nissel's latest book, Good Grief, Pass the Bread, Mom Is Dead, is my kind of memoir. Sure, it's a deeply emotional tale about caring for a terminally ill parent. But it's delivered with the sor"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/974209/fenix-flexin-billboard-hot-100-rubberz-ai-slop",
    "domain": "大厂 AI 动态",
    "title": "Is this Billboard Hot 100 hit AI slop?",
    "url": "https://www.theverge.com/ai-artificial-intelligence/974209/fenix-flexin-billboard-hot-100-rubberz-ai-slop",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T18:20:00+00:00",
    "summary": "Fenix Flexin is best known as a member of Shoreline Mafia, a rap duo from Los Angeles. But he's recently found solo success with the track \"Rubberz,\" which has climbed to number 58 on the Billboard Ho"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/974199/spider-man-brand-new-day-leak-box-office-records",
    "domain": "大厂 AI 动态",
    "title": "Spider-Man: Brand New Day leak racks up millions of views",
    "url": "https://www.theverge.com/entertainment/974199/spider-man-brand-new-day-leak-box-office-records",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T17:00:12+00:00",
    "summary": "A bootleg of Spider-Man: Brand New Day was up on X for over seven hours before eventually being pulled. During that time, it reached over 5.9 million accounts and accumulated over 143,000 likes. Other"
  },
  {
    "id": "rss:https://www.theverge.com/policy/974197/trump-tim-walz-minnesota-water-hacks-iran",
    "domain": "大厂 AI 动态",
    "title": "Trump blames Tim Walz for water hacks even though it’s probably Iran",
    "url": "https://www.theverge.com/policy/974197/trump-tim-walz-minnesota-water-hacks-iran",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T15:23:35+00:00",
    "summary": "The FBI, the EPA, and the Cybersecurity and Infrastructure Security Agency (CISA) have stopped short of officially blaming Iran for a spate of cyberattacks on Minnesota's water systems, but consensus "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/968645/back-to-school-shopping-guide-gifts",
    "domain": "大厂 AI 动态",
    "title": "The Verge’s 2026 back-to-school shopping guide",
    "url": "https://www.theverge.com/gadgets/968645/back-to-school-shopping-guide-gifts",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T14:00:00+00:00",
    "summary": "Knowing exactly what your student needs for the school year ahead is next to impossible. Sure, you'll probably nail the essentials, but there will likely be a few items you forgot to buy, or didn't th"
  },
  {
    "id": "rss:https://www.theverge.com/tech/973055/how-to-take-better-smartphone-photos",
    "domain": "大厂 AI 动态",
    "title": "You could be taking way better photos on your phone",
    "url": "https://www.theverge.com/tech/973055/how-to-take-better-smartphone-photos",
    "source": "David Imel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T13:30:00+00:00",
    "summary": "Your smartphone photos can look way better. If you're willing to put in a little extra work, use third party apps and spend a bit of time editing, it's possible to take photos that - under the right c"
  },
  {
    "id": "rss:https://www.theverge.com/games/971660/the-mermaid-mask-review",
    "domain": "大厂 AI 动态",
    "title": "The Mermaid Mask is a perfect vacation murder mystery",
    "url": "https://www.theverge.com/games/971660/the-mermaid-mask-review",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T13:00:00+00:00",
    "summary": "The Mermaid Mask, the next point-and-click game from Tangle Tower developer SFB Games, has everything you could ask for in a great murder mystery. It starts with a compelling setup: The captain of a s"
  },
  {
    "id": "rss:https://www.theverge.com/tech/973929/instapaper-app-pastebot-spiderman-movie-installer",
    "domain": "大厂 AI 动态",
    "title": "The OG reading app just got a big update",
    "url": "https://www.theverge.com/tech/973929/instapaper-app-pastebot-spiderman-movie-installer",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T12:00:00+00:00",
    "summary": "Hi, friends! Welcome to Installer No. 138, your guide to the best and Verge-iest stuff in the world. (If you're new here, welcome, happy August, and also you can read all the old editions at the Insta"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/973886/sharge-disk-pro-2-hands-on-switch-2-hdmi-usb-c-dock",
    "domain": "大厂 AI 动态",
    "title": "With Switch 2, iPhone, and laptop tricks, the Sharge Disk Pro 2 is finally a worthy EDC",
    "url": "https://www.theverge.com/gadgets/973886/sharge-disk-pro-2-hands-on-switch-2-hdmi-usb-c-dock",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T22:09:11+00:00",
    "summary": "Sharge, the company that makes delightful retro Mac-shaped chargers and see-inside batteries, is finally impressing me with a portable SSD. I couldn't recommend the Sharge Disk, Disk Plus, or even the"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/inside-one-london-founder-house-rewriting-the-founder-house-rules/",
    "domain": "大厂 AI 动态",
    "title": "Inside the London hacker house taking a stand against founder burnout",
    "url": "https://techcrunch.com/2026/08/01/inside-one-london-founder-house-rewriting-the-founder-house-rules/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T21:14:48+00:00",
    "summary": "How one founder house is betting work-life balance can beat burnout ."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/judge-denies-xais-request-to-block-minnesota-ban-on-nudify-apps/",
    "domain": "大厂 AI 动态",
    "title": "Judge denies xAI’s request to block Minnesota ban on ‘nudify’ apps",
    "url": "https://techcrunch.com/2026/08/01/judge-denies-xais-request-to-block-minnesota-ban-on-nudify-apps/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T20:26:04+00:00",
    "summary": "Despite a lawsuit from xAI, a Minnesota ban on apps that allow users to “nudify” images can move forward."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/youtuber-hank-green-says-his-ai-usage-is-not-healthy/",
    "domain": "大厂 AI 动态",
    "title": "YouTuber Hank Green says his AI usage is ‘not healthy’",
    "url": "https://techcrunch.com/2026/08/01/youtuber-hank-green-says-his-ai-usage-is-not-healthy/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T19:45:45+00:00",
    "summary": "Green offered a remarkable apology, saying that \"the level of dopamine that I've been getting from interacting with LLMs ... is not healthy for me or good for the world.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/should-you-still-buy-your-next-smartphone-or-subscribe-to-it-instead/",
    "domain": "大厂 AI 动态",
    "title": "Should you still buy your next smartphone — or subscribe to it instead?",
    "url": "https://techcrunch.com/2026/08/01/should-you-still-buy-your-next-smartphone-or-subscribe-to-it-instead/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T18:47:27+00:00",
    "summary": "Apple's new Upgrade program is the latest sign that smartphone ownership is changing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/sam-altman-is-still-making-the-case-for-parenting-via-chatgpt/",
    "domain": "大厂 AI 动态",
    "title": "Sam Altman is still making the case for parenting via ChatGPT",
    "url": "https://techcrunch.com/2026/08/01/sam-altman-is-still-making-the-case-for-parenting-via-chatgpt/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T17:07:34+00:00",
    "summary": "OpenAI's CEO seemed excited to share a \"cool use case\" for parents."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/this-9-key-physically-locks-your-most-addictive-apps/",
    "domain": "大厂 AI 动态",
    "title": "This $9 key physically locks your most addictive apps",
    "url": "https://techcrunch.com/2026/08/01/this-9-key-physically-locks-your-most-addictive-apps/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T15:58:17+00:00",
    "summary": "This $9 NFC key requires you to physically scan it to unlock distracting apps on your phone."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/ubers-autonomous-vehicle-deal-tracker/",
    "domain": "大厂 AI 动态",
    "title": "Uber is building an autonomous vehicle empire, and here’s every company it’s using to do it",
    "url": "https://techcrunch.com/2026/08/01/ubers-autonomous-vehicle-deal-tracker/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T15:05:00+00:00",
    "summary": "Uber has partnered with — and in some cases made direct investments in — about 30 autonomous vehicle companies over the past two years. Here's the list and the latest on the partnerships."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/apps-that-help-you-break-free-from-doomscrolling-and-get-active/",
    "domain": "大厂 AI 动态",
    "title": "Apps that help you break free from doomscrolling and get active",
    "url": "https://techcrunch.com/2026/08/01/apps-that-help-you-break-free-from-doomscrolling-and-get-active/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T14:00:00+00:00",
    "summary": "If you’re looking to cut back on screen time and get a little more active, here’s a roundup of the apps that might help."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/01/whats-the-best-handheld-mini-fan/",
    "domain": "大厂 AI 动态",
    "title": "What’s the best handheld mini fan?",
    "url": "https://techcrunch.com/2026/08/01/whats-the-best-handheld-mini-fan/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T13:36:54+00:00",
    "summary": "From premium Shark and Dyson offerings to random Amazon devices, these mini fans will make your sweaty summer a little more managable."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/openai-reportedly-finds-evidence-that-more-of-its-agents-ran-amok/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI reportedly finds evidence that more of its agents ran amok",
    "url": "https://techcrunch.com/2026/07/31/openai-reportedly-finds-evidence-that-more-of-its-agents-ran-amok/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T22:47:26+00:00",
    "summary": "OpenAI has reportedly found evidence of additional agent misbehavior as it looks into the incident that occurred with Hugging Face."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/rivian-spinoff-also-to-start-delivering-e-bikes-after-months-of-delays/",
    "domain": "大厂 AI 动态",
    "title": "Rivian spinoff Also to start delivering e-bikes after months of delays",
    "url": "https://techcrunch.com/2026/07/31/rivian-spinoff-also-to-start-delivering-e-bikes-after-months-of-delays/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T22:00:08+00:00",
    "summary": "Also has big plans beyond the TM-B. The startup mostly refers to itself as a \"vehicle\" company and has plans to make four-wheel pedal-assist cargo vehicles for Amazon."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/build-in-public-fail-in-public-what-its-like-to-be-a-founder-under-20-right-now/",
    "domain": "大厂 AI 动态",
    "title": "Silicon Valley loves young founders. Until it doesn’t.",
    "url": "https://techcrunch.com/2026/07/31/build-in-public-fail-in-public-what-its-like-to-be-a-founder-under-20-right-now/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T22:00:00+00:00",
    "summary": "AI tools have democratized the opportunity to build, shortening the timelines of success and enabling more young people to start successful companies without stepping foot inside a Big Tech company."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/india-is-starting-to-pay-for-apps-not-just-download-them/",
    "domain": "大厂 AI 动态",
    "title": "India is starting to pay for apps, not just download them",
    "url": "https://techcrunch.com/2026/07/31/india-is-starting-to-pay-for-apps-not-just-download-them/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T21:07:45+00:00",
    "summary": "India's app market generated a record $345 million in Q2."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/google-nixes-its-earth-ai-feature-one-day-after-launch-amid-criticism-it-would-spread-misinformation/",
    "domain": "大厂 AI 动态",
    "title": "Google nixes its Earth AI feature one day after launch, amid criticism it would spread misinformation",
    "url": "https://techcrunch.com/2026/07/31/google-nixes-its-earth-ai-feature-one-day-after-launch-amid-criticism-it-would-spread-misinformation/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T19:47:28+00:00",
    "summary": "A tool that allowed anyone to generate fake AI-generated imagery and superimpose it over real Google Earth maps quickly spurred backlash."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/fresh-off-its-wiz-payout-index-ventures-raises-2b-across-three-funds/",
    "domain": "大厂 AI 动态",
    "title": "Fresh off its Wiz payout, Index Ventures raises $2B across three funds",
    "url": "https://techcrunch.com/2026/07/31/fresh-off-its-wiz-payout-index-ventures-raises-2b-across-three-funds/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T19:39:51+00:00",
    "summary": "The new funding brings Index's total available investing capital to $3.5 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/vc-backed-startups-commit-more-fraud-and-researchers-think-they-know-why/",
    "domain": "大厂 AI 动态",
    "title": "VC-backed startups commit more fraud, and researchers think they know why",
    "url": "https://techcrunch.com/2026/07/31/vc-backed-startups-commit-more-fraud-and-researchers-think-they-know-why/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T19:00:00+00:00",
    "summary": "New research from the U.K.’s Imperial College and France’s Emlyon Business School mapped out how Silicon Valley founders commit fraud — and the role investors play."
  },
  {
    "id": "rss:https://techcrunch.com/video/sam-altman-isnt-the-only-one-who-wants-to-pump-the-brakes-on-ai/",
    "domain": "大厂 AI 动态",
    "title": "Sam Altman isn’t the only one who wants to pump the brakes on AI",
    "url": "https://techcrunch.com/video/sam-altman-isnt-the-only-one-who-wants-to-pump-the-brakes-on-ai/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T17:26:32+00:00",
    "summary": "After years of pushing full speed ahead on AI,&#160;OpenAI CEO&#160;Sam Altman says&#160;maybe it’s&#160;time for the AI industry to “pace” itself. The comments came&#160;just days after one of OpenAI"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/snapchat-no-longer-rewards-fully-ai-generated-spotlight-content/",
    "domain": "大厂 AI 动态",
    "title": "Snapchat no longer rewards fully AI-generated Spotlight content",
    "url": "https://techcrunch.com/2026/07/31/snapchat-no-longer-rewards-fully-ai-generated-spotlight-content/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T16:49:08+00:00",
    "summary": "Snapchat has adjusted its recommendation systems to ensure that only videos created by real people are eligible for Spotlight recommendations, taking a stance against AI slop."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/siri-ai-could-come-with-a-paywall-for-power-users/",
    "domain": "大厂 AI 动态",
    "title": "Siri AI could come with a paywall for power users",
    "url": "https://techcrunch.com/2026/07/31/siri-ai-could-come-with-a-paywall-for-power-users/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T16:08:18+00:00",
    "summary": "Apple CEO Tim Cook envisions users being able to buy more compute for Siri AI via Apple's existing iCloud+ subscriptions."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/31/gm-and-ford-are-talking-less-and-less-about-evs/",
    "domain": "大厂 AI 动态",
    "title": "GM and Ford are talking less and less about EVs",
    "url": "https://techcrunch.com/2026/07/31/gm-and-ford-are-talking-less-and-less-about-evs/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T15:47:46+00:00",
    "summary": "The leading U.S. automakers are mentioning EVs on their investor calls at pre-pandemic rates, according to new data from TechCrunch and Hudson Labs."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/heres-how-engineers-plan-to-save-the-satellite-sent-to-save-nasas-swift-mission/",
    "domain": "大厂 AI 动态",
    "title": "Here's how engineers plan to save the satellite sent to save NASA's Swift mission",
    "url": "https://arstechnica.com/space/2026/08/heres-how-engineers-plan-to-save-the-satellite-sent-to-save-nasas-swift-mission/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T18:20:11+00:00",
    "summary": "\"We believe that a capture of Swift, an attempted capture of Swift, is very much in the cards.\""
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/08/review-yes-were-still-arguing-about-nolans-the-odyssey/",
    "domain": "大厂 AI 动态",
    "title": "Review: Yes, we're still arguing about Nolan's The Odyssey",
    "url": "https://arstechnica.com/culture/2026/08/review-yes-were-still-arguing-about-nolans-the-odyssey/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T15:19:04+00:00",
    "summary": "Christopher Nolan's impressionistic remix of Homer's epic poem finds the man behind the myth."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/08/reddit-ceo-on-ai-overviews-were-still-looking-for-that-win-win/",
    "domain": "大厂 AI 动态",
    "title": "As Reddit stock falls, CEO questions value of Google's AI Overviews",
    "url": "https://arstechnica.com/ai/2026/08/reddit-ceo-on-ai-overviews-were-still-looking-for-that-win-win/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T12:30:36+00:00",
    "summary": "Reddit may still be considering ending its licensing deal with Google."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/after-noise-complaints-judge-orders-waymo-to-stop-overnight-charging-in-santa-monica/",
    "domain": "大厂 AI 动态",
    "title": "After noise complaints, judge orders Waymo to stop overnight charging in Santa Monica",
    "url": "https://arstechnica.com/tech-policy/2026/08/after-noise-complaints-judge-orders-waymo-to-stop-overnight-charging-in-santa-monica/",
    "source": "Cyrus Farivar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T11:30:54+00:00",
    "summary": "Autonomous vehicle giant disturbs residents' sleep."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/08/defcons-new-badge-is-a-security-key-you-can-see-inside/",
    "domain": "大厂 AI 动态",
    "title": "Defcon's new badge is a security key you can see inside",
    "url": "https://arstechnica.com/security/2026/08/defcons-new-badge-is-a-security-key-you-can-see-inside/",
    "source": "Kim Zetter, wired.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T10:05:21+00:00",
    "summary": "A removable chip lets hackers inspect their badge—and keep using it after Defcon."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/how-fruit-flies-chase-invisible-ribbons-of-smell-to-get-to-their-source/",
    "domain": "大厂 AI 动态",
    "title": "How fruit flies chase invisible ribbons of smell to get to their source",
    "url": "https://arstechnica.com/science/2026/08/how-fruit-flies-chase-invisible-ribbons-of-smell-to-get-to-their-source/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T10:00:19+00:00",
    "summary": "Tracking smells in turbulent air takes a keen sense of direction and sharp memory."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/not-just-neanderthals-ghost-lineage-in-africa-left-its-mark-on-our-dna/",
    "domain": "大厂 AI 动态",
    "title": "Not just Neanderthals: Ghost lineage in Africa left its mark on our DNA",
    "url": "https://arstechnica.com/science/2026/07/not-just-neanderthals-ghost-lineage-in-africa-left-its-mark-on-our-dna/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T22:17:05+00:00",
    "summary": "Some group with no modern descendants contributed a lot to our genomes."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/doctors-took-a-look-at-mans-painful-shoulder-they-found-the-joint-was-missing/",
    "domain": "大厂 AI 动态",
    "title": "Doctors took a look at man's painful shoulder—they found the joint was missing",
    "url": "https://arstechnica.com/health/2026/07/doctors-took-a-look-at-mans-painful-shoulder-they-found-the-joint-was-missing/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T21:51:52+00:00",
    "summary": "The term \"Milwaukee Shoulder Syndrome\" was coined in 1981, based on cases in four women."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/google-plans-to-exempt-sanctioned-nations-from-android-developer-verification/",
    "domain": "大厂 AI 动态",
    "title": "Google plans to exempt sanctioned nations from Android developer verification",
    "url": "https://arstechnica.com/gadgets/2026/07/google-plans-to-exempt-sanctioned-nations-from-android-developer-verification/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-31T21:35:56+00:00",
    "summary": "Someone in Cuba or Iran can keep installing APKs with no new restrictions, but devs will suffer."
  },
  {
    "id": "hn:49057574",
    "domain": "股票",
    "title": "Google Discloses $94.1B in SpaceX Stock, Marking 6% Stake",
    "url": "https://www.wsj.com/tech/google-discloses-94-1-billion-in-spacex-stock-marking-6-stake-91655d7c",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 342,
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
    "id": "hn:49122994",
    "domain": "股票",
    "title": "Situational Awareness down 67% in July in AI stock rout",
    "url": "https://www.wsj.com/finance/investing/situational-awareness-down-67-in-july-in-ai-stock-rout-cd19901f",
    "source": "pondsider",
    "platform": "hackernews",
    "points": 155,
    "published_at": "2026-07-31T13:37:36+00:00",
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
    "id": "hn:49137024",
    "domain": "股票",
    "title": "Oil companies report sky-high profits thanks to wartime crude prices",
    "url": "https://www.npr.org/2026/07/31/nx-s1-5910660/big-oil-earnings-q2-2026",
    "source": "speckx",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-08-01T18:28:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:49136787",
    "domain": "股票",
    "title": "Reddit Stock Collapses 23% as AI Eats Away at User Growth",
    "url": "https://www.barchart.com/story/news/3584357/reddit-stock-collapses-23-as-ai-eats-away-at-user-growth",
    "source": "thm",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-08-01T18:03:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49111879",
    "domain": "股票",
    "title": "Citadel Buys Situational Awareness's Stock Portfolio After Big Losses in AI",
    "url": "https://www.wsj.com/finance/citadel-buys-situational-awarenesss-stock-portfolio-after-big-losses-in-ai-5117159b",
    "source": "mudil",
    "platform": "hackernews",
    "points": 53,
    "published_at": "2026-07-30T16:00:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49092549",
    "domain": "股票",
    "title": "Chip stocks slide in US and Asia as AI jitters rattle investors",
    "url": "https://www.bbc.com/news/articles/cly8zng43npo",
    "source": "yogthos",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-07-29T01:56:00+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3778504",
    "domain": "股票",
    "title": "TACO！特朗普“取消对伊朗打击”，伊朗否认曾要求停火，沙特王储曾致电美方“敦促缓和局势”",
    "url": "https://wallstreetcn.com/articles/3778504",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T05:49:05+00:00",
    "summary": "特朗普称，在伊朗及多个中东国家请求下，美方同意取消军事打击，并推动协议框架落地。此前，美以一度准备扩大对伊行动，伊朗亦释放强硬信号并制定反击方案，目标包括以色列关键基础设施、中东地区美国能源设施及相关目标。沙特、阿联酋、卡塔尔等海湾国家担忧冲突外溢并紧急介入斡旋，军事升级风险暂时缓解。"
  },
  {
    "id": "wscn:3778503",
    "domain": "股票",
    "title": "被“忽略”的市场大事：美日韩联合干预，美国财政部“罕见”下场！贝森特悄悄“救市”？",
    "url": "https://wallstreetcn.com/articles/3778503",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T05:44:22+00:00",
    "summary": "美国财政部本周罕见介入汇市，通过纽约联储委托华尔街银行卖出欧元、买入日元，与日韩联手实施近三十年来最大规模协调外汇干预。 分析认为，此举背后已超越单纯汇率维稳，核心在于防止日本、韩国资产市场进一步走弱，降低金融压力向AI产业链传导的风险。美国通过非美元交易方式介入日元，也意在转移对美元的压力，避免美元体系承受额外冲击。"
  },
  {
    "id": "wscn:3778502",
    "domain": "股票",
    "title": "怎么看待AI大回调，大摩120页研报深度解读",
    "url": "https://wallstreetcn.com/articles/3778502",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T03:04:02+00:00",
    "summary": "摩根士丹利指出，回调的主要驱动力是技术面因素，而非基本面逻辑破坏。市场对Token需求和高额资本开支回报的担忧不成立：AI调用ROI超10倍，且算力效率提升将遵循杰文斯悖论，反而推高总消耗，GPU代际升级可大幅降本。供给端“电力瓶颈”虽存，但快速发电方案、存量设施改造等去瓶颈路径可解。"
  },
  {
    "id": "wscn:3778433",
    "domain": "股票",
    "title": "下周重磅日程：美国非农与中国CPI、SpaceX首份财报+解禁、AMD闪迪财报",
    "url": "https://wallstreetcn.com/articles/3778433",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T02:02:33+00:00",
    "summary": "SpaceX首份季报发布两天后1160亿美元限售股解禁来袭；DeepSeek-V4-Pro正式版“尽快发布”。宏观方面，美国非农将定价9月降息预期，中国7月CPI/PPI检验物价走向。此外，Ai 4、FMS闪存峰会等AI大会叠加，三星HBM4E路线图或发布。财报方面，AMD、闪迪、西部数据等密集放榜，宇树科技启动IPO询价，比亚迪人形机器人实体亮相。"
  },
  {
    "id": "wscn:3778498",
    "domain": "股票",
    "title": "四大行5年期大额存单集体回归，最高利率1.6%",
    "url": "https://wallstreetcn.com/articles/3778498",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T01:18:13+00:00",
    "summary": "8月1日，工商银行上架2026年第一期、第二期5年期个人大额存单，年化利率分别为1.60%和1.55..."
  },
  {
    "id": "wscn:3777747",
    "domain": "股票",
    "title": "口服环肽元年：百亿美元新赛道，颠覆性技术有望重构慢病范式？",
    "url": "https://wallstreetcn.com/premium/articles/3777747?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T01:17:53+00:00",
    "summary": "全球环肽研发管线从2021年的72项扩至93项，BD交易总额在2026年上半年已达61.7亿美元，创历史新高。"
  },
  {
    "id": "wscn:3778501",
    "domain": "股票",
    "title": "美以拟周末对伊朗能源基础设施实施“猛烈轰炸” ，瞄准发电厂、炼油厂，伊朗：全面反击方案已就绪",
    "url": "https://wallstreetcn.com/articles/3778501",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-02T00:46:54+00:00",
    "summary": "美以正计划对伊朗能源设施发动“迄今最猛烈的轰炸”，行动或持续整个周末，打击目标涵盖发电厂、炼油厂等伊朗能源基础设施。其中，切断伊朗首都德黑兰电力供应的打击方案也在讨论范围。伊朗外交部同日声明决心继续抵抗，并已制定全面反击方案，反击目标包括以色列关键基础设施和中东地区美国能源设施。"
  },
  {
    "id": "wscn:3778355",
    "domain": "股票",
    "title": "超级厄尔尼诺来袭：7000亿美元只是开始，更大冲击或在明年",
    "url": "https://wallstreetcn.com/premium/articles/3778355?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T23:37:21+00:00",
    "summary": "超级厄尔尼诺风险升温，或造成2026年经济损失7000亿美元，推升通胀，扰动航运，加剧贸易保护冲击。"
  },
  {
    "id": "wscn:3778400",
    "domain": "股票",
    "title": "美日双方联合干预：日元暴涨3.5%会否仍是昙花一现？",
    "url": "https://wallstreetcn.com/premium/articles/3778400?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T23:14:45+00:00",
    "summary": "美日联合干预虽短期见效并确立底部，但日元中长期趋势难逆转，后市或宽幅震荡。"
  },
  {
    "id": "wscn:3778499",
    "domain": "股票",
    "title": "个人贷款综合融资成本明示新规8月1日起施行，多家机构提前公示",
    "url": "https://wallstreetcn.com/articles/3778499",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T13:53:07+00:00",
    "summary": "8月1日，《个人贷款业务明示综合融资成本规定》正式施行。\n根据规定，贷款人开展个人贷款业务时，应当向..."
  },
  {
    "id": "wscn:3778479",
    "domain": "股票",
    "title": "单日7.2万亿韩元，外资周五净买入创纪录！华尔街：韩股资金面逆风已经消退",
    "url": "https://wallstreetcn.com/articles/3778479",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T11:50:07+00:00",
    "summary": "7月31日韩国KOSPI股市创下外资单日净买入7.2万亿韩元的历史新高，月度抛售压力大幅收窄，国内养老金亦由卖转买。同时监管提高单股杠杆ETF门槛以抑制波动。花旗据此认为资金面逆风已转为顺风，维持KOSPI指数10000点目标位不变。"
  },
  {
    "id": "wscn:3778496",
    "domain": "股票",
    "title": "卡塔尔LNG船霍尔木兹海峡遭袭失控，中东局势骤然升温",
    "url": "https://wallstreetcn.com/articles/3778496",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T11:48:35+00:00",
    "summary": "一艘载有卡塔尔货物的液化天然气运输船在通过霍尔木兹海峡时遭到投射物击中。英国海事贸易行动办公室表示，该船在阿曼东北方约11海里处遭不明投射物击中，发动机舱受损，船只目前失去控制，暂无人员伤亡或环境污染报告。"
  },
  {
    "id": "wscn:3778497",
    "domain": "股票",
    "title": "OpenAI确认下一代模型Astra存在，以2000美元算力成本破解十项数学未解难题，正向监管层展示",
    "url": "https://wallstreetcn.com/articles/3778497",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T11:46:16+00:00",
    "summary": "OpenAI酝酿全新多智能体模型Astra，仅耗两千美元算力，即史无前例攻克十道尘封逾十年的顶尖数学难题。该模型现已赴华盛顿演示，即将迎来特朗普政府新版AI监管框架的首批大考。"
  },
  {
    "id": "wscn:3778494",
    "domain": "股票",
    "title": "高盛：7月砸穿拥挤交易，美股牛市没断但更难做了",
    "url": "https://wallstreetcn.com/articles/3778494",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T10:30:21+00:00",
    "summary": "7月美股指数表面稳如泰山，底层却遭遇惊心动魄的仓位大血洗。最拥挤的AI与动量交易惨遭去杠杆重锤，市场逻辑正从“狂热叙事”回归“真实回报”。牛市并未出局，但“买入即躺赢”的时代已落幕。前路颠簸，市场不再宽恕杠杆。"
  },
  {
    "id": "wscn:3778295",
    "domain": "股票",
    "title": "16个月压缩成3个月，中国新型烟草真的要按下“加速键”了吗？",
    "url": "https://wallstreetcn.com/premium/articles/3778295?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T09:45:58+00:00",
    "summary": "加热卷烟国家标准从立项到发布征求意见稿，仅用了约三个月；与此同时，尼古丁袋也进入强制国标制定程序。中国过去对雾化电子烟强调收口、控产能，如今为何又开始为HNB和口含产品修建制度轨道？这并非监管转向鼓励尼古丁消费，而是在传统卷烟增长放缓、烟草利税承压和海外产品迭代加快之后，监管试图把存量需求纳入更安全、可控、可征税的专卖体系。"
  },
  {
    "id": "wscn:3778495",
    "domain": "股票",
    "title": "从韩国到美国：多亏了AI，蓝领越来越吃香了",
    "url": "https://wallstreetcn.com/articles/3778495",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T09:35:58+00:00",
    "summary": "当白领遭遇创纪录裁员，技术蓝领却迎历史性薪酬溢价。“防AI冲击”叠加基建狂潮，Z世代正加速抛弃大学光环涌入职业教育。面对百万级用工缺口，巨头纷纷重金抢人，一场颠覆认知的蓝领“淘金热”已全面爆发。"
  },
  {
    "id": "wscn:3778493",
    "domain": "股票",
    "title": "需求再度回落——7月制造业PMI数据点评",
    "url": "https://wallstreetcn.com/articles/3778493",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T08:33:58+00:00",
    "summary": "受地缘冲突与极端天气拖累，供需缺口走阔。但“新动能”保持扩张，中下游企业利润挤压边际缓解。展望下半年，广义财政提速落地将成托举内需、破局逆周期的核心筹码。"
  },
  {
    "id": "wscn:3778492",
    "domain": "股票",
    "title": "俄对乌发动大规模袭击，摧毁美国公司无人机工厂！俄方：使用陆基、海基远程高精度武器和无人机！特朗普：尚未同意授权乌生产“爱国者”",
    "url": "https://wallstreetcn.com/articles/3778492",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T08:24:05+00:00",
    "summary": "俄乌局势骤然升温！俄军大规模空袭基辅，首次摧毁一家美资无人机工厂。同时，双方针对炼油厂与物流枢纽展开激烈的“纵深互炸”。叠加美方暂未授权乌克兰生产“爱国者”拦截弹，这场牵动全球地缘与能源市场的博弈正步入危险新高潮。"
  },
  {
    "id": "wscn:3778491",
    "domain": "股票",
    "title": "开源崛起、降价80%，大模型真的还能赚到钱吗？",
    "url": "https://wallstreetcn.com/articles/3778491",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T06:52:09+00:00",
    "summary": "OpenAI暴降价80%交锋Kimi开放权重，大模型竞争正式告别单纯“价格战”。悬殊的ROI测算揭开了算力利用率等盈利黑匣。Token贬值大势下，资本市场不再听故事，唯有打通“低成本生产与高溢价服务”闭环，方能在现金流大考中真正突围。"
  },
  {
    "id": "wscn:3778488",
    "domain": "股票",
    "title": "“债券抛售敲响警钟”！圣路易斯联储主席呼吁“尽早加息”",
    "url": "https://wallstreetcn.com/articles/3778488",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-01T05:29:22+00:00",
    "summary": "Musalem警示美联储需以加息行动捍卫抗通胀公信力。受30年期美债收益率创07年新高及油价、关税等多重通胀压力推升影响，多位鹰派官员力主尽早加息25基点，并驳斥政策决策“外包”给市场的质疑。"
  },
  {
    "id": "hn:49115139",
    "domain": "股票",
    "title": "Microsoft's $450B Jump Is Biggest in Stock Market History",
    "url": "https://www.bloomberg.com/news/articles/2026-07-30/microsoft-eyes-history-with-490-billion-pop-in-market-value",
    "source": "signatoremo",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-07-30T20:12:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49114131",
    "domain": "股票",
    "title": "Citadel buys most of Situational's stock holdings after AI share rout",
    "url": "https://www.reuters.com/technology/citadel-buys-most-situationals-stock-holdings-after-ai-share-rout-sources-say-2026-07-30/",
    "source": "paulpauper",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-30T18:54:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:49095568",
    "domain": "股票",
    "title": "Korean Stocks Plunge 16% in Two-Day Burst of Retail Selling",
    "url": "https://www.bloomberg.com/news/articles/2026-07-29/korean-stocks-tumble-a-second-day-as-sk-hynix-results-disappoint",
    "source": "emsidisii",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-29T10:25:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49119293",
    "domain": "股票",
    "title": "Aschenbrenner's hedge fund forced to unwind all public stock positions",
    "url": "https://www.cnbc.com/2026/07/30/leopold-aschenbrenners-hedge-fund-is-facing-steep-ai-losses.html",
    "source": "akbabu",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-31T05:22:18+00:00",
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
    "id": "hn:49113358",
    "domain": "股票",
    "title": "South Korea's stock market plunges as AI-driven boom fades",
    "url": "https://www.aljazeera.com/economy/2026/7/29/south-koreas-stock-market-plunges-as-ai-driven-boom-fades",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-30T17:54:23+00:00",
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
    "points": 17,
    "published_at": "2026-07-28T23:41:59+00:00",
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
    "points": 174,
    "published_at": "2026-07-28T12:19:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49118696",
    "domain": "金融",
    "title": "The bond market isn’t buying what Fed Chair Warsh is selling",
    "url": "https://www.reuters.com/commentary/reuters-open-interest/bond-market-isnt-buying-what-fed-chair-warsh-is-selling-2026-07-30/",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 138,
    "published_at": "2026-07-31T03:32:21+00:00",
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
    "id": "hn:49046525",
    "domain": "金融",
    "title": "The Fedora 45 Sausage Factory",
    "url": "https://supakeen.com/weblog/the-fedora-45-sausage-factory/",
    "source": "6581",
    "platform": "hackernews",
    "points": 157,
    "published_at": "2026-07-25T11:04:57+00:00",
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
    "id": "hn:49097833",
    "domain": "金融",
    "title": "Show HN: The Federalist Papers, typeset as the 1787 newspapers they ran in",
    "url": "https://federalistreader.org/",
    "source": "vhwalke",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-07-29T14:13:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49082706",
    "domain": "金融",
    "title": "AI revenues are growing fast, but not fast enough",
    "url": "https://www.economist.com/finance-and-economics/2026/07/28/ai-revenues-are-growing-fast-but-not-fast-enough",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-07-28T12:19:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49114620",
    "domain": "金融",
    "title": "'Talk Is Cheap': Wall Street Delivers Harsh Verdict on Warsh Fed",
    "url": "https://www.bloomberg.com/news/articles/2026-07-30/-talk-is-cheap-wall-street-delivers-harsh-verdict-on-warsh-fed",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-30T19:33:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:49100970",
    "domain": "金融",
    "title": "Trump administration Is Repurposing Federal Land for A.I. Data Centers",
    "url": "https://www.nytimes.com/2026/07/29/climate/trump-federal-data-centers.html",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-29T18:09:42+00:00",
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
    "points": 14,
    "published_at": "2026-07-23T21:28:52+00:00",
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
    "id": "hn:48852473",
    "domain": "金融",
    "title": "Meta is staring down $1.4T in lawsuit over teen mental health",
    "url": "https://finance.yahoo.com/technology/articles/meta-staring-down-1-4t-173432639.html",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-09T21:15:06+00:00",
    "summary": ""
  }
]
```
