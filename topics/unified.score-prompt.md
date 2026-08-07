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

- 今日日期：`2026-08-07`
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
  "date": "2026-08-07",
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
    "points": 4128549,
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
    "points": 1673736,
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
    "points": 1584221,
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
    "points": 1315171,
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
    "points": 1064755,
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
    "points": 1016280,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 943285,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 599827,
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
    "points": 582671,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 564888,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 502377,
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
    "points": 434523,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 433344,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 419720,
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
    "points": 351208,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 258567,
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
    "points": 225818,
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
    "points": 215337,
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
    "points": 178637,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV172GP6rEZs",
    "domain": "AI",
    "title": "🚀DeepSeek V4 Flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！",
    "url": "http://www.bilibili.com/video/av117014605731815",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 170718,
    "published_at": "2026-07-31T12:42:57+00:00",
    "summary": "🚀DeepSeek v4 flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！性能、速度与真实短板全曝光！对比Kimi K3后优点和缺点都藏不住了\n\nDeepSeek 发布了 DeepSeek V4 Flash 0731：284B 总参数、13B 激活参数、100 万 Token 上下文，官方基准表现接近 Claude"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 142226,
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
    "points": 121866,
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
    "points": 93035,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 74035,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 73865,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 61034,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53715,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1fjcgzLE43",
    "domain": "AI",
    "title": "Claude 4.6最新功能，Claude Agent Teams 保姆级入门及使用教程",
    "url": "http://www.bilibili.com/video/av116040637941520",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 48178,
    "published_at": "2026-02-09T12:21:02+00:00",
    "summary": "本视频从四个方面介绍 claude agent teams 的使用：\n什么是 Claude Agent Teams\nClaude Agent Teams 跟 SubAgent 的区别是什么\nClaude Agent Teams 实战\nClaude Agent Teams 缺点及使用建议"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47569,
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
    "points": 45479,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 41085,
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
    "points": 40021,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1gwcAzkEhw",
    "domain": "AI",
    "title": "Claude Code Agent Teams上手指南+项目实测",
    "url": "http://www.bilibili.com/video/av116037064331269",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 35159,
    "published_at": "2026-02-08T23:30:00+00:00",
    "summary": "用Claude Code干复杂任务总碰到三个问题：\n\n上下文越来越长开始遗忘、任务只能串行效率低、单Agent视角单一容易漏检。\n\nClaude官方发布的Agent Teams功能正好解决这些痛点\n\n一个Team Lead拆任务，多个Teammate并行执行，还能互相通信协调。\n\n本期视频从核心概念、使用场景、底层架构到真实项目实战，带你完整搞懂Agent Teams的正确打开方式。"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34047,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 31509,
    "published_at": "2026-05-07T00:00:00+00:00",
    "summary": "全栈课一共分为6大块内容\n第一块：AI智能体开发基础(AI大模型、工具、记忆、MCP、中间件、Skills等核心内容)\n第二块：Claude Code,Trea+skills实现基于需求文档生成用例，基于OpenClaw实现接口自动化落地，基于hermes Agent实现web自动化落地\n第三块：功能测试的智能体开发(项目RAG知识库搭建+Agent搭建+skills开发，实现用例生成的Agent"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28850,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV16ggC6DEZK",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116963049212769",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 27696,
    "published_at": "2026-07-22T10:10:42+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 24313,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22689,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1YJ336EEBk",
    "domain": "AI",
    "title": "【AI陪玩】开袋即食的AI接入我的世界教程！",
    "url": "http://www.bilibili.com/video/av116981806143216",
    "source": "万昇Dwin",
    "platform": "bilibili",
    "points": 22321,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "模组：Numen\n项目地址：https://github.com/Dwinovo/minecraft-numen"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 19681,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1dsNv66E3Q",
    "domain": "AI",
    "title": "【Cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116922599344955",
    "source": "六月要癫",
    "platform": "bilibili",
    "points": 19278,
    "published_at": "2026-07-15T06:39:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1gf3T6KEef",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！从环境搭建到工作流完整闭环，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116979708990688",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 18874,
    "published_at": "2026-07-25T08:47:37+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 18283,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17678,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV15phrzqEzK",
    "domain": "AI",
    "title": "【Claude Code Router】一键直连五大模型",
    "url": "http://www.bilibili.com/video/av115121162553281",
    "source": "她笑中藏泪花",
    "platform": "bilibili",
    "points": 17060,
    "published_at": "2025-08-31T03:09:22+00:00",
    "summary": "Claude Code Router 教程：手把手完成 CCR 配置与 PROXY_URL 代理，一次直连 Gemini、Kimi、DeepSeek、GLM、Qwen，区分 Anthropic 与 OpenAI 端点，并附 /model 切换与报错速查。点击查看。\n博文链接：https://rosetears.cn/archives/61/"
  },
  {
    "id": "bvid:BV1YGKJ6tEdz",
    "domain": "AI",
    "title": "Vibe Coding我的赛博女友",
    "url": "http://www.bilibili.com/video/av116933101950817",
    "source": "天工开帧",
    "platform": "bilibili",
    "points": 13873,
    "published_at": "2026-07-17T09:50:00+00:00",
    "summary": "Vibe Coding大赏之赛博女友。总体花费100个馒头左右，由于显存限制，目前实时数字人的版本没办法跑起来。目前可以24挂着，随时对话随时打断。作用嘛，除了聊天就是在我忙的时候顺手帮我查个东西。未来开发方向接入pi-agent，让它真正干活，当然，只是得上qwen27B以上得模型才有可用性。也就是说所有模型显存开销打底得36G以上。囧。当然如果不要无限制，可以接入在线模型或在线TTS，但是，我"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 13221,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1HhGo6aEvE",
    "domain": "AI",
    "title": "本地大模型也能联网搜索！LM Studio × MCP 接入教程",
    "url": "http://www.bilibili.com/video/av116635490911881",
    "source": "aopstudio",
    "platform": "bilibili",
    "points": 10083,
    "published_at": "2026-05-25T13:41:46+00:00",
    "summary": "本视频演示如何为 LM Studio 接入 MCP 联网搜索服务，让本地运行的大模型具备实时搜索网络的能力。\nMCP（Model Context Protocol）是 Anthropic 推出的开放协议，允许模型通过标准化接口调用外部工具。本次接入的搜索服务来自 MCPWorld，底层通过 npx 调用，无需额外部署服务端，配置完成后即可在 LM Studio 的对话界面中直接发起联网搜索。\n本视"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9299,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
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
    "id": "hn:49189234",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia’s Vera Whitepaper Has a Thread Loose",
    "url": "https://chipsandcheese.com/p/nvidias-vera-whitepaper-has-a-thread",
    "source": "pella",
    "platform": "hackernews",
    "points": 201,
    "published_at": "2026-08-05T21:24:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49122838",
    "domain": "AI 算力 / 半导体",
    "title": "Moonshot’s Kimi uses 20k Nvidia chip cluster from Alibaba",
    "url": "https://www.bloomberg.com/news/articles/2026-07-31/moonshot-s-kimi-built-on-20-000-nvidia-chip-cluster-from-alibaba",
    "source": "gk1",
    "platform": "hackernews",
    "points": 114,
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
    "id": "rss:https://www.eetimes.com/ai-chip-startup-taalas-acquired-by-amd/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Chip Startup Taalas Acquired by AMD",
    "url": "https://www.eetimes.com/ai-chip-startup-taalas-acquired-by-amd/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T20:05:00+00:00",
    "summary": "AMD plans to use Taalas chips alongside its GPUs for AI inference, likely as an LLM decode accelerator. The post AI Chip Startup Taalas Acquired by AMD appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/globalfoundries-growth-makes-the-case-for-a-u-s-photonics-buildout/",
    "domain": "AI 算力 / 半导体",
    "title": "GlobalFoundries’ Growth Makes the Case for a U.S. Photonics Buildout",
    "url": "https://www.eetimes.com/globalfoundries-growth-makes-the-case-for-a-u-s-photonics-buildout/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T16:17:00+00:00",
    "summary": "GlobalFoundries’ data center surge turns U.S. photonics from subsidy pitch to AI bottleneck bet. The post GlobalFoundries’ Growth Makes the Case for a U.S. Photonics Buildout appeared first on EE Time"
  },
  {
    "id": "rss:https://www.eetimes.com/u-s-manufacturing-activity-hits-four-year-high-in-july/",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Manufacturing Activity Hits Four-Year High in July",
    "url": "https://www.eetimes.com/u-s-manufacturing-activity-hits-four-year-high-in-july/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T12:31:16+00:00",
    "summary": "In July, U.S. manufacturing activity remained in expansion territory, growing at its fastest pace in more than four years. The post U.S. Manufacturing Activity Hits Four-Year High in July appeared fir"
  },
  {
    "id": "rss:https://www.eetimes.com/beyond-the-fab-building-europe-next-generation-of-semiconductor-champions/",
    "domain": "AI 算力 / 半导体",
    "title": "Beyond the Fab: Building Europe’s Next Generation of Semiconductor Champions",
    "url": "https://www.eetimes.com/beyond-the-fab-building-europe-next-generation-of-semiconductor-champions/",
    "source": "Ian Lankshear",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T08:09:11+00:00",
    "summary": "Europe's next semiconductor champions will emerge from design expertise, customer knowledge, and IP—not manufacturing capacity alone. The post Beyond the Fab: Building Europe&#8217;s Next Generation o"
  },
  {
    "id": "rss:https://www.eetimes.com/samsung-lays-out-ai-memory-roadmap/",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung Lays Out AI Memory Roadmap",
    "url": "https://www.eetimes.com/samsung-lays-out-ai-memory-roadmap/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T21:35:58+00:00",
    "summary": "Samsung bets on zHBM and zNAND-O to smash AI’s memory wall, promising 8× HBM5 performance and 3D stacks. The post Samsung Lays Out AI Memory Roadmap appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/safeguarding-fab-throughput-with-ai-augmented-data-insights/",
    "domain": "AI 算力 / 半导体",
    "title": "Safeguarding Fab Throughput with AI-Augmented Data Insights",
    "url": "https://www.eetimes.com/safeguarding-fab-throughput-with-ai-augmented-data-insights/",
    "source": "Alessandro Chimera, Industry Solutions Lead, Spotfire",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T13:00:00+00:00",
    "summary": "Discover how a Al-infused visual analytics platform empower engineers to solve complex manufacturing challenges for faster root cause analysis. The post Safeguarding Fab Throughput with AI-Augmented D"
  },
  {
    "id": "rss:https://www.eetimes.com/unstacking-the-future-navigating-the-3d-ic-frontier/",
    "domain": "AI 算力 / 半导体",
    "title": "Unstacking the Future: Navigating the 3D IC Frontier",
    "url": "https://www.eetimes.com/unstacking-the-future-navigating-the-3d-ic-frontier/",
    "source": "Piyush Sancheti, VP Central Engineering Solutions (3D IC), and Todd Burkholder, 3D IC Technology Writer, Siemens EDA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T13:00:00+00:00",
    "summary": "3D IC introduces new system-level hurdles that demand innovative 3D IC solutions that address exploration, design, analysis, reliability, and test. The post Unstacking the Future: Navigating the 3D IC"
  },
  {
    "id": "rss:https://www.eetimes.com/neuromorphic-insect-eye-for-physical-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Insect-Inspired Neuromorphic Sensor Targets Physical AI",
    "url": "https://www.eetimes.com/neuromorphic-insect-eye-for-physical-ai/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T12:30:00+00:00",
    "summary": "Neuromorphic engineering could address the latency and power limitations of conventional cameras. The post Insect-Inspired Neuromorphic Sensor Targets Physical AI appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/electronica-2026-electronics-as-the-basis-of-the-all-electric-society/",
    "domain": "AI 算力 / 半导体",
    "title": "electronica 2026: Electronics as the Basis of the All-Electric Society",
    "url": "https://www.eetimes.com/electronica-2026-electronics-as-the-basis-of-the-all-electric-society/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T07:30:00+00:00",
    "summary": "electronica 2026 puts chips, AI, energy efficiency, and cyber resilience at the heart of the all-electric society. The post electronica 2026: Electronics as the Basis of the All-Electric Society appea"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/pre-modded-rtx-2080-ti-cards-with-22gb-of-vram-surface-on-ebay-for-usd500-hong-kong-based-seller-offers-ai-friendly-memory-mod-for-a-reasonable-price",
    "domain": "AI 算力 / 半导体",
    "title": "Pre-modded 22GB RTX 2080 Ti cards surface on eBay for $500 as VRAM-hungry local AI fans chase down every spare FLOP — Hong Kong-based seller offers AI-friendly memory mod for a reasonable price",
    "url": "https://www.tomshardware.com/pc-components/gpus/pre-modded-rtx-2080-ti-cards-with-22gb-of-vram-surface-on-ebay-for-usd500-hong-kong-based-seller-offers-ai-friendly-memory-mod-for-a-reasonable-price",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T16:11:19+00:00",
    "summary": "Services have recently popped up that will double your RTX 2080 Ti's memory to 22GB, but if you don't have a card to spare, you can now get a pre-modded 22 GB 2080 Ti for $499 from eBay."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/after-severe-76-percent-electricity-price-hikes-due-to-ai-data-centers-virginia-requires-firms-to-pay-for-all-dedicated-upstream-electrical-infrastructure-state-regulators-crack-down-governor-says-move-will-save-civilians-hundreds-of-millions-of-dollars",
    "domain": "AI 算力 / 半导体",
    "title": "After severe 76% electricity price hikes due to AI data centers, Virginia requires firms to pay for all dedicated upstream electrical infrastructure — state regulators crack down, governor says move w",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/after-severe-76-percent-electricity-price-hikes-due-to-ai-data-centers-virginia-requires-firms-to-pay-for-all-dedicated-upstream-electrical-infrastructure-state-regulators-crack-down-governor-says-move-will-save-civilians-hundreds-of-millions-of-dollars",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T15:32:08+00:00",
    "summary": "Virginia's public utility regulator now requires all data center projects to pay for the infrastructure needed to supply their power. This makes it one of the first states to convert the 'ratepayer pr"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/usd1-billion-of-iphone-18-pro-chips-on-the-shelves-awaiting-packaging-due-to-dram-shortages-memory-shortages-reportedly-put-a-wrinkle-in-apples-launch-plans",
    "domain": "AI 算力 / 半导体",
    "title": "$1 billion of iPhone 18 Pro chips 'on the shelves awaiting packaging' due to DRAM shortages — memory shortages reportedly put a wrinkle in Apple's launch plans",
    "url": "https://www.tomshardware.com/pc-components/dram/usd1-billion-of-iphone-18-pro-chips-on-the-shelves-awaiting-packaging-due-to-dram-shortages-memory-shortages-reportedly-put-a-wrinkle-in-apples-launch-plans",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T14:52:11+00:00",
    "summary": "Apple reportedly as $1 billion worth of iPhone 18 processor wafers awaiting packaging, which hasn't been completed due to DRAM shortages."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/nashville-attempts-to-block-controversial-data-center-near-zoo-with-eminent-domain-city-could-force-developer-to-sell-the-land-for-public-use-rather-than-usd700-million-installation",
    "domain": "AI 算力 / 半导体",
    "title": "Nashville attempts to block controversial data center near zoo with eminent domain — city could force developer to sell the land for public use, rather than $700 million installation",
    "url": "https://www.tomshardware.com/tech-industry/policy/nashville-attempts-to-block-controversial-data-center-near-zoo-with-eminent-domain-city-could-force-developer-to-sell-the-land-for-public-use-rather-than-usd700-million-installation",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T13:26:17+00:00",
    "summary": "The Nashville Metro Council just gave the go ahead for the mayor's plan to buy the land that a proposed data center will sit on through eminent domain. This will force the developer to give up the lan"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/samsung-debuts-three-next-generation-memory-technologies-for-ai-data-centers-zhbm-znand-o-and-bv-nand-all-rely-on-advanced-wafer-bonding-technologies",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung debuts three next-generation memory technologies for AI data centers — zHBM, zNAND-O, and BV-NAND all rely on advanced wafer bonding technologies",
    "url": "https://www.tomshardware.com/pc-components/dram/samsung-debuts-three-next-generation-memory-technologies-for-ai-data-centers-zhbm-znand-o-and-bv-nand-all-rely-on-advanced-wafer-bonding-technologies",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T13:11:09+00:00",
    "summary": "Samsung uses FMS to unveil three next-generation memory technologies — zHBM, zNAND-O, and BV-NAND — that target different markets, but all rely on advanced wafer-bonding techniques."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/pc-gamer-vibe-codes-a-safeguard-against-rtx-5090-power-connector-failures-monitors-per-pin-power-draw-shuts-down-system-if-it-exceeds-9-5a-for-more-than-15-seconds",
    "domain": "AI 算力 / 半导体",
    "title": "PC gamer vibe-codes a safeguard against RTX 5090 power connector failures — monitors per-pin power draw, shuts down system if it exceeds 9.5A for more than 15 seconds",
    "url": "https://www.tomshardware.com/pc-components/gpus/pc-gamer-vibe-codes-a-safeguard-against-rtx-5090-power-connector-failures-monitors-per-pin-power-draw-shuts-down-system-if-it-exceeds-9-5a-for-more-than-15-seconds",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T12:33:49+00:00",
    "summary": "The 35MB application forcibly shuts the machine down if power exceeds configurable limits for too long."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/sandisk-optimus-gx-7100m-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "Sandisk Optimus GX 7100M 2TB SSD review: The best 2230 drive you can buy for the Steam Deck",
    "url": "https://www.tomshardware.com/pc-components/ssds/sandisk-optimus-gx-7100m-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T12:05:00+00:00",
    "summary": "The Sandisk Optimus GX 7100M is the pinnacle of M.2 2230 SSD goodness. High performance, great power efficiency, and a well-supported drive up to 2TB."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/apple-is-taking-openai-to-court-over-alleged-theft-of-trade-secrets-chatgpt-maker-suggests-it-doesnt-want-cupertinos-knowledge-anyway",
    "domain": "AI 算力 / 半导体",
    "title": "Apple is taking OpenAI to court over alleged theft of trade secrets — ChatGPT maker suggests it doesn't want Cupertino's knowledge anyway",
    "url": "https://www.tomshardware.com/tech-industry/apple-is-taking-openai-to-court-over-alleged-theft-of-trade-secrets-chatgpt-maker-suggests-it-doesnt-want-cupertinos-knowledge-anyway",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T11:25:02+00:00",
    "summary": "Two of the world's largest companies are heading to court over claims of trade secret theft. Apple alleges ex-employees took key Apple secrets and technologies to OpenAI. In responding, OpenAI claims "
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/beelink-ser10-max-mini-pc-review",
    "domain": "AI 算力 / 半导体",
    "title": "Beelink SER10 Max Mini PC review: Gorgon Point comes ready to dual-boot Windows and Ubuntu",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/beelink-ser10-max-mini-pc-review",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T11:05:00+00:00",
    "summary": "Beelink’s SER10 Max Mini PC comes ready to dual-boot Windows 11 and Ubuntu with OpenClaw pre-installed."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/usd200-slashed-off-gigabytes-4th-gen-woled-gaming-monitor-280hz-beast-also-packs-a-kvm-and-tactical-gaming-switch-for-just-usd399",
    "domain": "AI 算力 / 半导体",
    "title": "$200 slashed off Gigabyte's 4th-Gen WOLED gaming monitor — 280Hz beast also packs a KVM and tactical gaming switch for just $399",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/usd200-slashed-off-gigabytes-4th-gen-woled-gaming-monitor-280hz-beast-also-packs-a-kvm-and-tactical-gaming-switch-for-just-usd399",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T10:54:42+00:00",
    "summary": "Save $200 on this gorgeous 27-inch WOLED gaming monitor from Gigabyte, and upgrade your gaming experience for less."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd1-400-on-this-rtx-5090-gaming-pc-from-hp-with-64gb-ddr5-right-now-ram-and-gpu-cost-usd5k-alone-usd5-599-sale-price-for-top-spec-omen-max-45l-rig-with-24-core-intel-cpu-and-2tb-of-ssd-storage",
    "domain": "AI 算力 / 半导体",
    "title": "Save $1,400 on this RTX 5090 gaming PC from HP with 64GB DDR5 right now; RAM and GPU cost $5k alone — $5,599 sale price for top-spec Omen Max 45L rig with 24-core Intel CPU and 2TB of SSD storage",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd1-400-on-this-rtx-5090-gaming-pc-from-hp-with-64gb-ddr5-right-now-ram-and-gpu-cost-usd5k-alone-usd5-599-sale-price-for-top-spec-omen-max-45l-rig-with-24-core-intel-cpu-and-2tb-of-ssd-storage",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T10:50:15+00:00",
    "summary": "You can save $1,400 right now on this Omen Max gaming PC, fitted with an RTX 5090, 64GB RAM, and 2TB SSD storage, and on sale for $5,599.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/vpn-provider-windscribe-has-built-a-script-to-block-microsofts-persistent-gdid-tracking-on-windows-degdid-erases-existing-identifiers-and-blocks-new-ones-from-being-created",
    "domain": "AI 算力 / 半导体",
    "title": "VPN provider built a script to block Microsoft's hidden GDID tracking on Windows — Windscribe's \"deGDID\" erases existing identifiers and blocks new ones from being created",
    "url": "https://www.tomshardware.com/software/windows/vpn-provider-windscribe-has-built-a-script-to-block-microsofts-persistent-gdid-tracking-on-windows-degdid-erases-existing-identifiers-and-blocks-new-ones-from-being-created",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T10:30:00+00:00",
    "summary": "You can run the deGDID script on your computer to delete cached GDID keys and prevent Microsoft's servers from minting new ones in the background. The firewall you put up with this script will break c"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/rogue-openai-models-behind-unprecedented-cybersecurity-incident-teamed-up-to-break-out-of-their-testing-environment-multiple-agents-left-each-other-messages-for-months-communicating-undetected",
    "domain": "AI 算力 / 半导体",
    "title": "Rogue OpenAI models behind 'unprecedented cybersecurity incident' teamed up to break out of their testing environment — multiple agents left each other messages for months, communicating undetected",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/rogue-openai-models-behind-unprecedented-cybersecurity-incident-teamed-up-to-break-out-of-their-testing-environment-multiple-agents-left-each-other-messages-for-months-communicating-undetected",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T10:19:25+00:00",
    "summary": "The rogue OpenAI models that broke out of their testing environment in an \"unprecedented cybersecurity incident\" recently reportedly spent months communicating with each other."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/kentucky-family-snubs-usd26-million-offer-from-ai-company-to-convert-their-farmland-into-a-data-center-they-call-us-old-stupid-farmers-you-know-but-were-not-says-landowner",
    "domain": "AI 算力 / 半导体",
    "title": "Kentucky family snubs $26 million offer to convert their farmland into an AI data center — 'they call us old stupid farmers, you know, but we’re not,' says landowner",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/kentucky-family-snubs-usd26-million-offer-from-ai-company-to-convert-their-farmland-into-a-data-center-they-call-us-old-stupid-farmers-you-know-but-were-not-says-landowner",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T10:00:00+00:00",
    "summary": "A Northern Kentucky family has refused an anonymous AI company's $26 million offer to buy their land and transform it into a data center."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/xbox/microsoft-wants-the-next-gen-xbox-helix-to-play-every-xbox-game-ever-made-as-it-urges-publishers-to-opt-in-new-report-also-claims-xbox-360-games-coming-to-pc-soon",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft wants the next-gen Xbox Helix to play every Xbox game ever made as it urges publishers to opt in — New report also claims Xbox 360 games coming to PC soon",
    "url": "https://www.tomshardware.com/video-games/xbox/microsoft-wants-the-next-gen-xbox-helix-to-play-every-xbox-game-ever-made-as-it-urges-publishers-to-opt-in-new-report-also-claims-xbox-360-games-coming-to-pc-soon",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T14:51:31+00:00",
    "summary": "The upcoming Xbox Helix is starting to feel more like a PC than any console before, and Microsoft's latest efforts to unite all Xbox generations under one roof, according to a new leaked memo, seem to"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/usd4-429-order-for-a-rog-astral-rtx-5090-cancelled-by-nvidia-due-to-a-late-price-increase-with-asus-blamed-marketplace-buyer-refunded-after-immediate-usd500-increase-with-top-spec-gpu-now-almost-2-5x-higher-than-msrp",
    "domain": "AI 算力 / 半导体",
    "title": "$4,429 order for a ROG Astral RTX 5090 cancelled by Nvidia due to a 'late' price increase, with Asus blamed — marketplace buyer refunded after immediate $500 increase, with top-spec GPU now almost 2.5",
    "url": "https://www.tomshardware.com/pc-components/gpus/usd4-429-order-for-a-rog-astral-rtx-5090-cancelled-by-nvidia-due-to-a-late-price-increase-with-asus-blamed-marketplace-buyer-refunded-after-immediate-usd500-increase-with-top-spec-gpu-now-almost-2-5x-higher-than-msrp",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T14:48:13+00:00",
    "summary": "Nvidia cancelled a Redditor's Asus ROG Astral RTX 5090 BTF GPU order, originally priced at $4,429, because of a $500 price rise, with Nvidia blaming Asus for the confusion."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/chinas-cxmt-targets-30-percent-dram-memory-market-share-by-2030-with-sixth-mega-fab-future-plans-bottlenecked-by-access-to-advanced-chipmaking-tools",
    "domain": "AI 算力 / 半导体",
    "title": "China's CXMT targets 30% DRAM memory market share by 2030 with sixth mega-fab — future plans bottlenecked by access to advanced chipmaking tools",
    "url": "https://www.tomshardware.com/pc-components/dram/chinas-cxmt-targets-30-percent-dram-memory-market-share-by-2030-with-sixth-mega-fab-future-plans-bottlenecked-by-access-to-advanced-chipmaking-tools",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T14:31:50+00:00",
    "summary": "ChangXin Memory Technologies (CXMT) began considering building its sixth DRAM fab in China to boost memory output in the coming years. If all announced projects proceed as planned, the company's produ"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/microsoft-quietly-purges-32gb-of-ram-recommendations-from-its-website-company-reels-from-the-effects-of-the-memory-shortage-as-it-released-8gb-base-models-for-surface-laptops-this-year",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft quietly purges 32GB of RAM recommendations from its website — company reels from the effects of the memory shortage as it released 8GB base models for Surface laptops this year",
    "url": "https://www.tomshardware.com/software/windows/microsoft-quietly-purges-32gb-of-ram-recommendations-from-its-website-company-reels-from-the-effects-of-the-memory-shortage-as-it-released-8gb-base-models-for-surface-laptops-this-year",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T13:12:34+00:00",
    "summary": "Microsoft once recommended 32GB of RAM as a future-proof \"no worries\" upgrade for gamers, but it seems that it wants you to forget that it ever gave that suggestion. That's because laptop manufacturer"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/score-all-the-essentials-of-a-great-gaming-pc-for-only-usd983-98-usd155-savings-nets-9800x3d-1tb-samsung-9100-ssd-16gb-of-ddr5-ram-asus-b850-motherboard-and-free-msi-aio",
    "domain": "AI 算力 / 半导体",
    "title": "Score all the essentials of a great gaming PC for only $983.98 — $155 savings nets 9800X3D, 1TB Samsung 9100 SSD, 16GB of DDR5 RAM, Asus B850 motherboard, and free MSI AIO",
    "url": "https://www.tomshardware.com/pc-components/score-all-the-essentials-of-a-great-gaming-pc-for-only-usd983-98-usd155-savings-nets-9800x3d-1tb-samsung-9100-ssd-16gb-of-ddr5-ram-asus-b850-motherboard-and-free-msi-aio",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T12:01:51+00:00",
    "summary": "Save $155 on this 4-item Newegg Gaming PC Combo - $983 buys 9800X3D, Samsung's blazing fast 1TB 9100 Pro SSD, 16GB of RAM, and Asus B850 motherboard"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/us-military-gps-jamming-exercise-suspected-of-contributing-to-civilian-plane-crash-in-new-mexico-medevac-flight-lost-signal-before-flying-into-a-mountain-killing-everyone-onboard",
    "domain": "AI 算力 / 半导体",
    "title": "US military GPS jamming exercise suspected of contributing to civilian plane crash in New Mexico — medevac flight lost signal before flying into a mountain, killing everyone onboard",
    "url": "https://www.tomshardware.com/tech-industry/us-military-gps-jamming-exercise-suspected-of-contributing-to-civilian-plane-crash-in-new-mexico-medevac-flight-lost-signal-before-flying-into-a-mountain-killing-everyone-onboard",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T12:00:16+00:00",
    "summary": "A medevac flight in New Mexico suffered from GPS interference due to activities by nearby U.S. military units. Although it didn't directly cause the plane to crash, it added to the stress and workload"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/elon-musk-says-spacex-will-exclusively-use-nvidia-gpus-because-they-are-the-best-says-optimized-vera-rubin-nvl72-will-be-launched-into-space-next-year",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk says SpaceX will exclusively use Nvidia GPUs 'because they are the best' — says optimized Vera Rubin NVL72 will be launched into space next year",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/elon-musk-says-spacex-will-exclusively-use-nvidia-gpus-because-they-are-the-best-says-optimized-vera-rubin-nvl72-will-be-launched-into-space-next-year",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T11:50:34+00:00",
    "summary": "Elon Musk's SpaceX and xAI will exclusive use Nvidia AI accelerators for training and inference as companies believe Vera Rubin is the best AI compute architecture available today."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/huge-usd750-saving-makes-this-gigabyte-oled-gaming-laptop-with-an-rtx-5070-ti-an-absolute-steal-right-now-just-usd1-999-for-1600p-rig-with-32gb-ddr5-1tb-ssd-and-a-24-core-intel-cpu",
    "domain": "AI 算力 / 半导体",
    "title": "Huge $750 saving makes this Gigabyte OLED gaming laptop with an RTX 5070 Ti an absolute steal right now — just $1,999 for 1600p rig with 32GB DDR5, 1TB SSD, and a 24-core Intel CPU",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/huge-usd750-saving-makes-this-gigabyte-oled-gaming-laptop-with-an-rtx-5070-ti-an-absolute-steal-right-now-just-usd1-999-for-1600p-rig-with-32gb-ddr5-1tb-ssd-and-a-24-core-intel-cpu",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T11:06:29+00:00",
    "summary": "Save $750.99 on this powerhouse Gigabyte Aorus Master OLED gaming laptop with an RTX 5070 Ti and 32GB DDR5 for $1,999."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/frore-claims-its-liquidjet-can-drop-nvidia-rubin-gpu-temperatures-by-10-c-can-also-boost-performance-by-15-percent-as-hyperscalers-eye-using-delidded-gpus-in-production-environments",
    "domain": "AI 算力 / 半导体",
    "title": "Frore claims its LiquidJet can drop Nvidia Rubin GPU temperatures by 10°C — can also boost performance by 15% as hyperscalers eye using delidded GPUs in production environments",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/frore-claims-its-liquidjet-can-drop-nvidia-rubin-gpu-temperatures-by-10-c-can-also-boost-performance-by-15-percent-as-hyperscalers-eye-using-delidded-gpus-in-production-environments",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T11:02:00+00:00",
    "summary": "As cooling becomes a crucial element for economic efficiency of AI data centers, Frore claims that using is LiquidJet coldplate could increase efficiency of token generation by 15%."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/montech-tg3-panoramic-mid-tower-case-review",
    "domain": "AI 算力 / 半导体",
    "title": "Montech TG3 Panoramic Mid-tower case review: a fantastic value, with four included RGB fans and panoramic views",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/montech-tg3-panoramic-mid-tower-case-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T11:00:00+00:00",
    "summary": "Montech's TG3 is a marvelous value in the budget mid-tower space, with ample room for components and four included fans. It also offers solid noise-normalized cooling for the CPU and a good all-around"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/best-buy-has-slashed-usd900-off-this-macbook-laden-with-memory-14-inch-m4-pro-with-48gb-of-memory-and-2tb-of-storage-now-only-usd2-999",
    "domain": "AI 算力 / 半导体",
    "title": "Best Buy has slashed $900 off this MacBook laden with memory — 14-inch M4 Pro with 48GB of memory and 2TB of storage now only $2,999",
    "url": "https://www.tomshardware.com/laptops/macbooks/best-buy-has-slashed-usd900-off-this-macbook-laden-with-memory-14-inch-m4-pro-with-48gb-of-memory-and-2tb-of-storage-now-only-usd2-999",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T10:39:33+00:00",
    "summary": "In a time of extreme memory and storage pricing, this Apple MacBook Pro deal from Best Buy slashes $900 off the 48GB M4 Pro machine."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-headsets/glorious-wireless-infiniteplay-gaming-headset-review",
    "domain": "AI 算力 / 半导体",
    "title": "Glorious Wireless InfinitePlay Gaming Headset Review",
    "url": "https://www.tomshardware.com/peripherals/gaming-headsets/glorious-wireless-infiniteplay-gaming-headset-review",
    "source": "Christopher Coke",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T10:00:00+00:00",
    "summary": "The Glorious Wireless InfinitePlay offers solid sound, quality comms, and never-ending uptime at a reduced price. There’s a handful of trade-offs, but this headset has more wins than losses and is def"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/humble-nas-gets-transformed-into-a-gaming-pc-with-and-rtx-5060-hanging-from-its-side-frankenstein-rig-hides-dedicated-psu-in-drive-bay-to-achieve-vast-performance-increase-over-igpu",
    "domain": "AI 算力 / 半导体",
    "title": "Crazed modder turns NAS into a gaming PC with RTX 5060 hanging from the side, boosts frame rate by 828% — Frankenstein rig hides dedicated PSU in drive bay, breaks Time Spy world record for the onboar",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/humble-nas-gets-transformed-into-a-gaming-pc-with-and-rtx-5060-hanging-from-its-side-frankenstein-rig-hides-dedicated-psu-in-drive-bay-to-achieve-vast-performance-increase-over-igpu",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T09:21:13+00:00",
    "summary": "A modder has attached a full-sized RTX 5060 graphics card to a ZimaCube 2 NAS server and achieved up to 8x faster performance in games. The jerry-rigged setup doesn't look the most polished, and the C"
  },
  {
    "id": "hn:49177126",
    "domain": "AI 算力 / 半导体",
    "title": "It looks like 'Big Short' investor Michael Burry nailed bet against chip stocks",
    "url": "https://www.businessinsider.com/big-short-michael-burry-ai-chip-stocks-soxx-nvidia-substack-2026-8",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-05T00:30:23+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/automotive-cybersecurity-ai-attack-surfaces-grow/",
    "domain": "AI 算力 / 半导体",
    "title": "Automotive Cybersecurity: AI Attack Surfaces Grow",
    "url": "https://www.eetimes.com/automotive-cybersecurity-ai-attack-surfaces-grow/",
    "source": "Egil Juliussen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T22:00:00+00:00",
    "summary": "AI and software-defined cars turn APIs, servers, and chargers into hacker playgrounds; see why automakers must harden fleets now. The post Automotive Cybersecurity: AI Attack Surfaces Grow appeared fi"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/amd-doubles-data-center-revenue-year-over-year-but-gaming-revenue-plunged-by-31-percent-ceo-lisa-su-says-prices-have-weighed-on-consumer-demand-but-is-optimistic-about-client-market",
    "domain": "AI 算力 / 半导体",
    "title": "AMD doubles data center revenue year over year, but gaming revenue plunged by 31% — CEO Lisa Su says prices have 'weighed on' consumer demand but is 'optimistic' about client market",
    "url": "https://www.tomshardware.com/tech-industry/amd-doubles-data-center-revenue-year-over-year-but-gaming-revenue-plunged-by-31-percent-ceo-lisa-su-says-prices-have-weighed-on-consumer-demand-but-is-optimistic-about-client-market",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T22:03:07+00:00",
    "summary": "AMD reported record revenue in Q2 2026, including doubling its data center business year-over-year, but gaming revenue dived 31%."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/more-gpu-price-hikes-loom-for-asia-as-japanese-distributor-warns-of-new-increases-cfd-sales-signals-20-percent-to-40-percent-higher-prices-on-gigabyte-graphics-card-orders-starting-this-month",
    "domain": "AI 算力 / 半导体",
    "title": "More GPU price hikes loom for Asia as Japanese distributor warns of new increases — CFD Sales signals 20% to 40% higher prices on Gigabyte graphics card orders starting this month",
    "url": "https://www.tomshardware.com/pc-components/gpus/more-gpu-price-hikes-loom-for-asia-as-japanese-distributor-warns-of-new-increases-cfd-sales-signals-20-percent-to-40-percent-higher-prices-on-gigabyte-graphics-card-orders-starting-this-month",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T17:38:15+00:00",
    "summary": "Japanese technology supplier and distributor confirms that the Gigabyte graphics card will cost between 20% and 40% more due to a new price increase."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/us-mulling-ban-on-key-chinese-networking-tech-in-data-center-component-crackdown-white-house-wants-to-impose-restrictions-in-2026-china-says-it-will-respond-if-necessary",
    "domain": "AI 算力 / 半导体",
    "title": "US mulling ban on key Chinese networking tech in data center component crackdown — White House wants to impose restrictions in 2026, China says it will respond if necessary",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/us-mulling-ban-on-key-chinese-networking-tech-in-data-center-component-crackdown-white-house-wants-to-impose-restrictions-in-2026-china-says-it-will-respond-if-necessary",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-04T16:54:00+00:00",
    "summary": "Sources say that the FCC is drafting a ban on optical transceivers for data centers. These components, which convert electrical signals into light signals, are said to pose a risk as they can be used "
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
    "points": 18,
    "published_at": "2026-07-27T14:33:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:49184755",
    "domain": "大厂 AI 动态",
    "title": "Changes at Google DeepMind: Demis Hassabis from CEO to Chair, Jeff Dean departs",
    "url": "https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/",
    "source": "colesantiago",
    "platform": "hackernews",
    "points": 828,
    "published_at": "2026-08-05T16:05:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:48993414",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/",
    "source": "logickkk1",
    "platform": "hackernews",
    "points": 760,
    "published_at": "2026-07-21T15:17:16+00:00",
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
    "points": 199,
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
    "points": 94,
    "published_at": "2026-08-06T16:05:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49187259",
    "domain": "大厂 AI 动态",
    "title": "Sula: A Gemini protocol server written in Scryer Prolog",
    "url": "https://sagredo.dev/projects/sula/",
    "source": "triska",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-08-05T18:52:58+00:00",
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
    "points": 136,
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
    "id": "rss:https://www.theverge.com/tech/976454/made-by-google-2026-event-pixel-11-trevor-noah",
    "domain": "大厂 AI 动态",
    "title": "Trevor Noah is hosting Google’s Pixel 11 launch event",
    "url": "https://www.theverge.com/tech/976454/made-by-google-2026-event-pixel-11-trevor-noah",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T21:15:47+00:00",
    "summary": "Google is set to host its next live Made by Google hardware launch event on August 12th, and the company says in a new video that comedian Trevor Noah will be hosting the show. The video indicates tha"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/976431/openai-chatgpt-battery-smart-speaker-rumor",
    "domain": "大厂 AI 动态",
    "title": "Jony Ive&#8217;s first OpenAI gadget is reportedly a hockey puck-sized smart speaker",
    "url": "https://www.theverge.com/ai-artificial-intelligence/976431/openai-chatgpt-battery-smart-speaker-rumor",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T20:55:39+00:00",
    "summary": "The AI device OpenAI is developing with former Apple designer Jony Ive is \"essentially a smart speaker without a display\" that's battery-powered, doughnut-shaped and roughly the size of a hockey puck,"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/976276/apple-airpods-pro-3-best-buy-apple-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The AirPods Pro are $60 off, their best price since late June",
    "url": "https://www.theverge.com/gadgets/976276/apple-airpods-pro-3-best-buy-apple-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T20:00:00+00:00",
    "summary": "Best Buy kicked off a sale on Apple products with discounts on its latest smartwatches to phones. Another deal that caught our eye is on the latest AirPods Pro, Apple’s flagship wireless earbuds, whic"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/976337/the-legend-of-zelda-movie-ganondorf-multi-picture-deal",
    "domain": "大厂 AI 动态",
    "title": "The Zelda movie’s Ganondorf casting hints at more movies",
    "url": "https://www.theverge.com/entertainment/976337/the-legend-of-zelda-movie-ganondorf-multi-picture-deal",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T18:31:57+00:00",
    "summary": "Deadline reported Thursday that the upcoming The Legend of Zelda movie will feature Australian actor Uli Latukefu as the villain Ganondorf, and the publication notes that \"We hear Latukefu inked a mul"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/976289/suno-ai-music-spam-watermark",
    "domain": "大厂 AI 动态",
    "title": "Suno shares plans to combat spammy AI music",
    "url": "https://www.theverge.com/ai-artificial-intelligence/976289/suno-ai-music-spam-watermark",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T17:39:43+00:00",
    "summary": "Suno announced plans to implement a new watermarking technology and download policy to limit the spread of spammy AI tracks and increase transparency. In a lengthy blog post, CEO and co-founder Mikey "
  },
  {
    "id": "rss:https://www.theverge.com/policy/976287/fcc-broadcast-ownership-rule-ends",
    "domain": "大厂 AI 动态",
    "title": "Brendan Carr officially unleashes broadcast consolidation",
    "url": "https://www.theverge.com/policy/976287/fcc-broadcast-ownership-rule-ends",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T17:35:38+00:00",
    "summary": "The era of set broadcast ownership limits is officially over, after the Federal Communications Commission (FCC) voted Thursday to end the national ownership cap rule. The agency's two Republicans, Cha"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/976239/openai-chatgpt-free-go-text-chats",
    "domain": "大厂 AI 动态",
    "title": "OpenAI is giving ChatGPT free users unlimited text chats",
    "url": "https://www.theverge.com/ai-artificial-intelligence/976239/openai-chatgpt-free-go-text-chats",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T17:00:00+00:00",
    "summary": "OpenAI is making a big change for ChatGPT users on its free and Go tiers: Starting next week, users on those tiers will be able to have unlimited text chats with the chatbot, according to OpenAI. Righ"
  },
  {
    "id": "rss:https://www.theverge.com/tech/976228/tiktok-perez-hilton-livestream-moderator-error",
    "domain": "大厂 AI 动态",
    "title": "TikTok blames &#8216;moderator error&#8217; on slow response to Perez Hilton livestream",
    "url": "https://www.theverge.com/tech/976228/tiktok-perez-hilton-livestream-moderator-error",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T16:41:25+00:00",
    "summary": "TikTok says a \"moderator error\" delayed the removal of a livestream that appeared to show blogger Perez Hilton harming himself, as reported earlier by Wired. Jamie Favazza, a spokesperson for TikTok U"
  },
  {
    "id": "rss:https://www.theverge.com/tech/976210/apple-trade-in-values-increased",
    "domain": "大厂 AI 动态",
    "title": "Apple increases trade-in offers and adds new Android devices",
    "url": "https://www.theverge.com/tech/976210/apple-trade-in-values-increased",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T15:47:15+00:00",
    "summary": "Apple bumped up its trade-in offers for iPhones, iPads, Macs, Apple Watches, and certain Android phones, with some devices now worth over $100 more, 9to5Mac reports. The Mac Studio's trade-in value in"
  },
  {
    "id": "rss:https://www.theverge.com/policy/976138/softbank-trump-library-data-center-ohio",
    "domain": "大厂 AI 动态",
    "title": "SoftBank donated $50 million to Trump’s library months before federal data center deal",
    "url": "https://www.theverge.com/policy/976138/softbank-trump-library-data-center-ohio",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T14:30:00+00:00",
    "summary": "SoftBank contributed $50 million to the Trump Presidential Library in January, just months before announcing that it's leasing land from the federal government to build a sprawling data center in Ohio"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/openais-new-ai-smart-speaker-will-reportedly-sell-for-between-300-and-400/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s new AI smart speaker will reportedly sell for between $300 and $400",
    "url": "https://techcrunch.com/2026/08/06/openais-new-ai-smart-speaker-will-reportedly-sell-for-between-300-and-400/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T22:43:53+00:00",
    "summary": "Additional details about OpenAI's mysterious new AI device make it sound like a pricey smart speaker."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/your-table-awaits-exhibit-at-techcrunch-disrupt-2026-to-be-seen-by-thousands/",
    "domain": "大厂 AI 动态",
    "title": "Your table awaits: Exhibit at TechCrunch Disrupt 2026 to be seen by thousands",
    "url": "https://techcrunch.com/2026/08/06/your-table-awaits-exhibit-at-techcrunch-disrupt-2026-to-be-seen-by-thousands/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T22:00:00+00:00",
    "summary": "Not everyone needs a keynote slot to make noise at TechCrunch Disrupt 2026. Sometimes the best way to meet investors, customers, and partners is by exhibiting directly on the Expo Hall floor at San Fr"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/vogue-just-gave-another-nod-of-approval-to-the-tech-world/",
    "domain": "大厂 AI 动态",
    "title": "Vogue just gave another nod of approval to the tech world",
    "url": "https://techcrunch.com/2026/08/06/vogue-just-gave-another-nod-of-approval-to-the-tech-world/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T21:24:47+00:00",
    "summary": "Vogue World is coming to San Francisco next year — perhaps another indication that tech bros are now part of the fashion zeitgeist."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/get-up-to-400-off-your-techcrunch-disrupt-2026-pass-until-friday/",
    "domain": "大厂 AI 动态",
    "title": "Get up to $400 off your TechCrunch Disrupt 2026 pass until tomorrow",
    "url": "https://techcrunch.com/2026/08/06/get-up-to-400-off-your-techcrunch-disrupt-2026-pass-until-friday/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T21:20:00+00:00",
    "summary": "Starting today, you can take an additional $100 off your founder, investor, or attendee TechCrunch Disrupt 2026 pass, which is a nice bonus on top of our current discounted pricing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/google-says-hackers-are-calling-financial-firm-employees-to-hack-and-extort-victims/",
    "domain": "大厂 AI 动态",
    "title": "Google says hackers are calling financial firm employees to hack and extort victims",
    "url": "https://techcrunch.com/2026/08/06/google-says-hackers-are-calling-financial-firm-employees-to-hack-and-extort-victims/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T19:40:46+00:00",
    "summary": "Groups of hackers are breaking into large U.S. financial firms to steal sensitive data and extort victims, Google’s security researchers report."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/china-linked-lightspy-spyware-caught-targeting-victims-in-13-countries-including-the-us/",
    "domain": "大厂 AI 动态",
    "title": "China-linked LightSpy spyware caught targeting victims in 13 countries, including the US",
    "url": "https://techcrunch.com/2026/08/06/china-linked-lightspy-spyware-caught-targeting-victims-in-13-countries-including-the-us/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T19:22:30+00:00",
    "summary": "Researchers linked the latest malicious activity to a Chinese company, after one of the spyware's operators placed an order with KFC using their real name and office address."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/defense-tech-hadrian-raises-1-37b-at-8b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Defense tech Hadrian raises $1.37B at $8B valuation",
    "url": "https://techcrunch.com/2026/08/06/defense-tech-hadrian-raises-1-37b-at-8b-valuation/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T19:02:57+00:00",
    "summary": "Hadrian is building automated factories to mass-produce parts for defense vehicles like submarines. It's backed by a long list of well-known investors."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/ford-needs-another-taurus-and-the-30k-fathom-ev-pickup-isnt-it/",
    "domain": "大厂 AI 动态",
    "title": "Ford needs another Taurus, and the $30K Fathom EV pickup isn’t it",
    "url": "https://techcrunch.com/2026/08/06/ford-needs-another-taurus-and-the-30k-fathom-ev-pickup-isnt-it/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T17:41:56+00:00",
    "summary": "Ford's CEO has described the new Ford Fathom as a \"Model T moment\" for the company. But the EV pickup is unlikely to live up to lofty expectations, and maybe it doesn't have to."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/bumble-teases-a-swipe-free-future-as-it-doubles-down-on-irl-meetups/",
    "domain": "大厂 AI 动态",
    "title": "Bumble teases a swipe-free future as it doubles down on IRL meetups",
    "url": "https://techcrunch.com/2026/08/06/bumble-teases-a-swipe-free-future-as-it-doubles-down-on-irl-meetups/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T17:39:47+00:00",
    "summary": "Bumble says it’s moving beyond swiping and deeper into real-world social experiences as it courts Gen Z users."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/openai-brings-unlimited-chatgpt-text-chats-to-free-users/",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT brings unlimited text chats to free users",
    "url": "https://techcrunch.com/2026/08/06/openai-brings-unlimited-chatgpt-text-chats-to-free-users/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T17:34:42+00:00",
    "summary": "OpenAI said that ChatGPT free and Go users are also getting a new think button for complex queries."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/naive-raises-28-5m-to-automate-the-grunt-work-of-setting-up-and-running-a-company/",
    "domain": "大厂 AI 动态",
    "title": "Naïve raises $28.5M to automate the grunt work of setting up and running a company",
    "url": "https://techcrunch.com/2026/08/06/naive-raises-28-5m-to-automate-the-grunt-work-of-setting-up-and-running-a-company/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T17:00:37+00:00",
    "summary": "Taking vibe-coding a step further, Naïve claims its infra can automate most of the work in setting up and running a business."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/hacker-pleads-guilty-to-stealing-data-from-more-than-165-snowflake-customers/",
    "domain": "大厂 AI 动态",
    "title": "Hacker pleads guilty to stealing data from more than 165 Snowflake customers",
    "url": "https://techcrunch.com/2026/08/06/hacker-pleads-guilty-to-stealing-data-from-more-than-165-snowflake-customers/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T16:42:40+00:00",
    "summary": "Connor Moucka pled guilty to hacking and stealing data from more than 165 Snowflake customers, which net him and his accomplices more than $2.5 million in ransom payments."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/tiktok-lays-off-250-employees-shutters-its-nashville-office/",
    "domain": "大厂 AI 动态",
    "title": "TikTok lays off 250 employees, shutters its Nashville office",
    "url": "https://techcrunch.com/2026/08/06/tiktok-lays-off-250-employees-shutters-its-nashville-office/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T16:06:40+00:00",
    "summary": "The social media giant is shuttering an office that housed some members of TikTok’s content-moderation team."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/google-wallet-now-lets-parents-set-up-secure-balances-for-their-kids/",
    "domain": "大厂 AI 动态",
    "title": "Google Wallet now lets parents set up secure balances for their kids",
    "url": "https://techcrunch.com/2026/08/06/google-wallet-now-lets-parents-set-up-secure-balances-for-their-kids/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T16:00:00+00:00",
    "summary": "The tech giant says the new feature will allow parents to teach their kids healthy financial habits while maintaining oversight over their child's spending with built-in safeguards."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/gen-z-dating-apps-like-ditto-ditch-swiping-in-favor-of-ai-matchmaking/",
    "domain": "大厂 AI 动态",
    "title": "Gen Z dating apps like Ditto ditch swiping in favor of AI matchmaking",
    "url": "https://techcrunch.com/2026/08/06/gen-z-dating-apps-like-ditto-ditch-swiping-in-favor-of-ai-matchmaking/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T15:53:03+00:00",
    "summary": "This generation of twentysomethings is so disillusioned with swipe-based dating apps that they'll try literally anything else — even an AI matchmaker."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/tesla-and-spacex-will-invest-16-8b-to-start-building-terafab-chip-factory-in-texas/",
    "domain": "大厂 AI 动态",
    "title": "Tesla and SpaceX will invest $16.8B to start building ‘Terafab’ chip factory in Texas",
    "url": "https://techcrunch.com/2026/08/06/tesla-and-spacex-will-invest-16-8b-to-start-building-terafab-chip-factory-in-texas/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T15:21:51+00:00",
    "summary": "After months of speculation, the companies formally announced the massive project will happen just north of Houston."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/openai-says-apples-own-security-practices-undermine-its-trade-secrets-case/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI says Apple’s own security practices undermine its trade secrets case",
    "url": "https://techcrunch.com/2026/08/06/openai-says-apples-own-security-practices-undermine-its-trade-secrets-case/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T15:10:32+00:00",
    "summary": "Newly filed court exhibits show OpenAI’s legal strategy in Apple’s trade secrets lawsuit: argue that Apple’s own security and offboarding practices — including allowing an Apple manager to access a fo"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/ebay-continues-to-bet-on-live-shopping-after-record-quarter/",
    "domain": "大厂 AI 动态",
    "title": "eBay continues to bet on live shopping after record quarter",
    "url": "https://techcrunch.com/2026/08/06/ebay-continues-to-bet-on-live-shopping-after-record-quarter/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T14:17:46+00:00",
    "summary": "eBay touted an increase in eBay Live's gross merchandise volume as it plans to expand it to more international markets in the coming weeks and months."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/amid-legal-battles-suno-says-it-will-start-watermarking-songs/",
    "domain": "大厂 AI 动态",
    "title": "Amid legal battles, Suno says it will start watermarking songs",
    "url": "https://techcrunch.com/2026/08/06/amid-legal-battles-suno-says-it-will-start-watermarking-songs/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T13:31:57+00:00",
    "summary": "Suno's watermarking feature comes as the company is fighting legal battles on several fronts."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/fords-new-electric-truck-fathom-starts-at-28350/",
    "domain": "大厂 AI 动态",
    "title": "Ford’s new electric truck, ‘Fathom,’ starts at $28,350",
    "url": "https://techcrunch.com/2026/08/06/fords-new-electric-truck-fathom-starts-at-28350/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T13:01:25+00:00",
    "summary": "Due in \"fall 2027,\" Ford said Thursday that it won't reveal what Fathom looks like until early next year."
  },
  {
    "id": "rss:https://stratechery.com/2026/google-earnings-the-frontier-case-amazon-earnings/",
    "domain": "大厂 AI 动态",
    "title": "Google Earnings, The Frontier Case, Amazon Earnings",
    "url": "https://stratechery.com/2026/google-earnings-the-frontier-case-amazon-earnings/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T10:00:00+00:00",
    "summary": "Google's earnings seemed to confirm the Anthropic hedge; it was Andy Jassy who explained why their — and Amazon's — capex was justifiable."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/08/us-to-shutter-organ-donation-group-accused-of-trying-to-take-living-mans-organs/",
    "domain": "大厂 AI 动态",
    "title": "Organ donation group accused of trying to take living man's organs faces shutdown",
    "url": "https://arstechnica.com/health/2026/08/us-to-shutter-organ-donation-group-accused-of-trying-to-take-living-mans-organs/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T22:20:50+00:00",
    "summary": "The organization, Network for Hope, \"strongly disagrees\" with Trump admin's decision."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/germany-disarms-explosive-drone-found-at-airport-hunts-possible-second-drone/",
    "domain": "大厂 AI 动态",
    "title": "Explosive drone found hovering near Ukrainian cargo aircraft at German airport",
    "url": "https://arstechnica.com/gadgets/2026/08/germany-disarms-explosive-drone-found-at-airport-hunts-possible-second-drone/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T22:01:55+00:00",
    "summary": "Russian attack? Explosive drone targeted parked aircraft at Leipzig airport."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/elon-musks-x-isnt-done-suing-advertisers-asks-court-to-revive-boycott-case/",
    "domain": "大厂 AI 动态",
    "title": "X wants to keep suing advertisers, asks 5th Circuit to overrule district judge",
    "url": "https://arstechnica.com/tech-policy/2026/08/elon-musks-x-isnt-done-suing-advertisers-asks-court-to-revive-boycott-case/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T20:29:51+00:00",
    "summary": "Musk continues appeal despite court loss and settlement with advertiser group."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/08/suno-hopes-to-go-legit-with-watermarks-for-ai-generated-music/",
    "domain": "大厂 AI 动态",
    "title": "Suno hopes to go legit with watermarks for AI-generated music",
    "url": "https://arstechnica.com/ai/2026/08/suno-hopes-to-go-legit-with-watermarks-for-ai-generated-music/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T20:17:36+00:00",
    "summary": "Suno plans watermarks and download limits to stop \"large-scale abuse.\""
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/08/anthropic-confirms-plans-to-build-an-in-house-silicon-team/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic will design its own hardware to power Claude",
    "url": "https://arstechnica.com/ai/2026/08/anthropic-confirms-plans-to-build-an-in-house-silicon-team/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T20:03:44+00:00",
    "summary": "Anthropic and OpenAI are racing to scale up while reducing dependence on Nvidia."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/large-genome-models-used-to-design-new-viruses/",
    "domain": "大厂 AI 动态",
    "title": "Large genome models used to design new viruses",
    "url": "https://arstechnica.com/science/2026/08/large-genome-models-used-to-design-new-viruses/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T19:04:57+00:00",
    "summary": "The AI system makes genetically distant versions of a bacteria-killing virus."
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
    "id": "hn:49166182",
    "domain": "股票",
    "title": "Bending Spoons makes first post-IPO acquisition with $1.3B Airtable deal",
    "url": "https://live.euronext.com/en/financial-news/bending-spoons-makes-first-post-ipo-acquisition-13-billion-airtable-deal",
    "source": "riffraff",
    "platform": "hackernews",
    "points": 114,
    "published_at": "2026-08-04T09:27:47+00:00",
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
    "id": "hn:49151871",
    "domain": "股票",
    "title": "Situational Awareness and the Impending Stock Market Volatility",
    "url": "https://www.emergingtrajectories.com/lh/situational-awareness-bigger-picture/",
    "source": "cl42",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-08-03T06:17:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:49195657",
    "domain": "股票",
    "title": "The Investors Whose SpaceX Shares Vanished Before They Could Cash In",
    "url": "https://www.wsj.com/finance/stocks/spacex-ipo-spv-investors-2698a174",
    "source": "doener",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-08-06T12:19:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:49137024",
    "domain": "股票",
    "title": "Oil companies report sky-high profits thanks to wartime crude prices",
    "url": "https://www.npr.org/2026/07/31/nx-s1-5910660/big-oil-earnings-q2-2026",
    "source": "speckx",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-08-01T18:28:06+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3778906",
    "domain": "股票",
    "title": "上一轮互联网周期，美股风格如何切换？",
    "url": "https://wallstreetcn.com/articles/3778906",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:08:36+00:00",
    "summary": "招商宏观张静静团队认为，纳指在加息初期虹吸效应显著，但多次加息确认经济转弱后于2000年3月见顶回落，随后历经价值重估、震荡探底、结构修复三阶段。科技股分化，回归真实盈利，依赖资本扩张的企业承压；必选消费抗跌，金融与周期股领涨修复期。宏观经济增长由“资本扩张”转向“全要素生产率提升”，技术红利向实际应用端扩散。"
  },
  {
    "id": "wscn:3778909",
    "domain": "股票",
    "title": "创业板半日涨1.75%，PCB掀涨停潮，创新药大涨，恒科指下探回升转涨，AI大模型双雄再度爆发",
    "url": "https://wallstreetcn.com/articles/3778909",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:06:45+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市超3000股飘绿，上午半天成交1.69万亿。沪深两市半日成交额1.68万亿，较上个交易日缩量750亿。板块方面，CRO、PCB、 创新药、稀土、CPO、半导体设备、光刻机、光伏概念股活跃；稳定币、网络安全题材走弱，农业、金融板块跌幅靠前。"
  },
  {
    "id": "wscn:3778920",
    "domain": "股票",
    "title": "AAOI二季度营收同比增86.4%，数据中心收入破亿，需求超出产能20%，下半年资本开支将持续加码",
    "url": "https://wallstreetcn.com/articles/3778920",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T03:52:41+00:00",
    "summary": "美国光通信制造商AAOI二季度营收1.919亿美元，同比暴增86%，数据中心业务首破亿元大关，800G产品收入环比翻倍。更关键的是，1.6T产品即将完成客户认证并启动出货，管理层描绘的2027年中路径显示，数据中心收发器月收入或达4.71亿美元。需求端已不是问题——客户订单超出供应能力20%至40%，产能能否按时兑现才是问题。"
  },
  {
    "id": "wscn:3778919",
    "domain": "股票",
    "title": "近一年收益95.17%，嘉实基金王贵重：看好下半年AI行情！光通信、存储是最好的投资机会，存储供小于求至少持续到2027年",
    "url": "https://wallstreetcn.com/articles/3778919",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T03:39:21+00:00",
    "summary": "本轮市场核心分歧有两点。"
  },
  {
    "id": "wscn:3778918",
    "domain": "股票",
    "title": "美银衍生品部门警告：市场剧烈波动已成常态，AI泡沫风险指标逼近互联网时代极值",
    "url": "https://wallstreetcn.com/articles/3778918",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T03:38:29+00:00",
    "summary": "上周财报季中，六只\"科技七巨头\"股票实际波动幅度均大幅超出期权市场预期，为ChatGPT时代首次。美国银行衍生品团队警告，AI泡沫持续累积，市场波动率已逼近2000年互联网泡沫历史极值。宏观不确定性持续上升，当前混乱背景对波动率构成强劲支撑。"
  },
  {
    "id": "wscn:3778921",
    "domain": "股票",
    "title": "宇树科技发行市值达610亿元，超30家险企借道私募间接入局",
    "url": "https://wallstreetcn.com/articles/3778921",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T03:38:27+00:00",
    "summary": "8月6日，宇树科技发布首次公开发行股票并在科创板上市的发行公告，将发行价格确定为150.80元/股；..."
  },
  {
    "id": "wscn:3778914",
    "domain": "股票",
    "title": "中国7月出口同比增23.9%，半导体出口按价值计算同比近乎翻番，进口同比增27.5%",
    "url": "https://wallstreetcn.com/articles/3778914",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T03:30:50+00:00",
    "summary": "高科技出口的强劲表现是本月数据的主要亮点。半导体出口按价值计算同比近乎翻番，整体高科技产品出口扩大40.7%，在全球人工智能基础设施建设热潮的持续驱动下，相关需求保持旺盛。与此同时，全球能源转型带动的可再生能源产品需求，也成为拉动中国出口增长的重要动力。"
  },
  {
    "id": "wscn:3778843",
    "domain": "股票",
    "title": "中微传闻的背后，中国半导体设备厂商凭什么掘金全球2300亿美元大市场？",
    "url": "https://wallstreetcn.com/premium/articles/3778843?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T03:11:08+00:00",
    "summary": "路透社关于三星、SK海力士评估中微设备的报道，与两家公司公开否认并存，截至目前尚无相关测试、装机及订单证据。比传闻本身更值得关注的是，国产半导体设备正从国内替代走向国际客户验证：全球扩产、供应链安全和第二供应源需求，为设备与零部件打开新窗口。但“出海”并非一蹴而就，真正的拐点要看量产导入、重复订单、海外复制和服务体系落地，哪些产业链环节最有可能率先兑现？"
  },
  {
    "id": "wscn:3778916",
    "domain": "股票",
    "title": "白银单周暴涨8.3%，高盛警告系统性空头回补或已启动",
    "url": "https://wallstreetcn.com/articles/3778916",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T03:10:42+00:00",
    "summary": "白银在7月28日至8月5日暴涨8.3%，美元走弱是核心触发因素。高盛期货交易员Quinn指出，管理资金多头建仓是主要推手，未平仓合约增加24亿美元；更关键的是，短期动量信号已于8月5日翻转，CTA系统性空头回补正式启动。但高盛同时提示，实物市场并未收紧，且不预期美元持续走弱。"
  },
  {
    "id": "wscn:3778915",
    "domain": "股票",
    "title": "7月非农是否会转移联储注意力",
    "url": "https://wallstreetcn.com/articles/3778915",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T03:09:30+00:00",
    "summary": "7月非农数据即将公布，就业市场已现放缓信号：6月非农远低预期，ADP数据创年内新低，前期数据亦遭下修。若非农再度走弱，或重新吸引联储关注并改变加息路径。与此同时，美联储沟通机制趋于模糊，市场不确定性上升。相比单纯押注数据，买入跨FOMC前后期权、做多波动率或为更优策略。"
  },
  {
    "id": "wscn:3778907",
    "domain": "股票",
    "title": "他预言AI将毁灭人类，却仍在全力建造它——Anthropic掌门人的矛盾与崛起",
    "url": "https://wallstreetcn.com/articles/3778907",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T03:07:53+00:00",
    "summary": "Dario Amodei亲口承认自己正在建造的东西有四分之一概率让一切\"非常非常糟糕地结束\"，然后继续建，并认为这是阻止它变得更糟的唯一方式。就是这样一个人，用不到五年将Anthropic从5亿美元初创推升至近万亿估值。如今IPO窗口开启，投资者必须判断：这个矛盾，究竟是Anthropic最深的护城河，还是它最大的隐患？"
  },
  {
    "id": "wscn:3778912",
    "domain": "股票",
    "title": "美国绕开欧洲央行售欧元撑日元，欧洲人感到“遭背叛”",
    "url": "https://wallstreetcn.com/articles/3778912",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T03:04:08+00:00",
    "summary": "美国财政部未知会欧洲央行，径自抛售欧元以支撑日元，此举令欧洲官员震怒，被部分高级官员定性为对西方货币当局合作惯例\"史无前例的违背\"。此次美日联手干预规模创历史纪录，两日内动用逾13.8万亿日元，但争议更在于：二战以来西方央行赖以维系金融稳定的信任框架，是否正在特朗普时代悄然瓦解？"
  },
  {
    "id": "wscn:3778911",
    "domain": "股票",
    "title": "诺贝尔奖得主让位，联合创始人布林复出——谷歌AI领导层大洗牌背后的权力博弈",
    "url": "https://wallstreetcn.com/articles/3778911",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T03:02:42+00:00",
    "summary": "DeepMind创始人、诺贝尔奖得主Demis Hassabis卸任运营职务，转任首席科学家，日常管理权移交Koray Kavukcuoglu。AI决策中心从伦敦回归硅谷，联合创始人谢尔盖·布林深度介入Gemini开发。此次重组标志着谷歌从\"研究主导\"向\"商业变现\"全面转型，以追赶OpenAI和Anthropic。"
  },
  {
    "id": "wscn:3778853",
    "domain": "股票",
    "title": "全球长端利率见顶信号？美欧债顶背离，英债头肩顶，关键转向何时到来",
    "url": "https://wallstreetcn.com/premium/articles/3778853?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T02:51:55+00:00",
    "summary": "美欧长债顶背离与英债头肩顶共振，是否预示全球利率周期见顶回落？仍需破位确认及通胀数据验证。"
  },
  {
    "id": "wscn:3778904",
    "domain": "股票",
    "title": "美光管理层传递强势信号：存储的系统价值超过50%，CPU端AI代理需求处于“季前热身”",
    "url": "https://wallstreetcn.com/articles/3778904",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T01:18:30+00:00",
    "summary": "德意志银行在FMS 2026闪存峰会期间与美光管理层会谈，会上美光管理层指出，AI正将存储行业永久重塑为系统架构核心，DRAM与NAND均处供给短缺状态。存储器系统价值占比已升至近50%，AI加速重估进程。德银认为美光具备\"奢侈优势\"，可在不牺牲盈利的前提下实现增长，有望驱动强劲盈利上修与估值重塑。"
  },
  {
    "id": "wscn:3778905",
    "domain": "股票",
    "title": "高盛韩国交易员谈“存储多空之辩”：市场对基本面预期“过于悲观”",
    "url": "https://wallstreetcn.com/articles/3778905",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T00:50:05+00:00",
    "summary": "高盛韩国交易员Justin Park认为，市场对存储预期过悲。空方担忧英伟达降配HBM、海力士旧产能被锁及NAND复苏慢。高盛反驳：HBM降配反证供应短缺；同时DRAM制程微缩逼近10nm极限，供给结构性受限。AI驱动下DRAM短缺或延至2030年。"
  },
  {
    "id": "wscn:3778903",
    "domain": "股票",
    "title": "“创纪录”的美股财报季：标普500成分股EPS增长45%，但其中一半来自投资收益，1/3来自AI基建",
    "url": "https://wallstreetcn.com/articles/3778903",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T00:16:32+00:00",
    "summary": "标普500二季度EPS同比狂飙45%，但高盛报告揭开\"创纪录\"的遮羞布：剔除科技巨头股权投资公允价值变动后，增速近乎腰斩至26%；AI基建概念股再贡献三分之一增量，而中位数公司实际增速仅12%。与此同时，看涨期权单日成交突破400万张创史上最高，实际波动超隐含预期四倍。"
  },
  {
    "id": "wscn:3778901",
    "domain": "股票",
    "title": "宇树IPO的财富盛宴，注定只有少数人赚到",
    "url": "https://wallstreetcn.com/articles/3778901",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T23:57:36+00:00",
    "summary": "宇树科技610亿估值IPO，造就早期投资者及核心员工的百倍财富盛宴。一二级市场对此存在断层：一级盼其大涨以锚定行业估值；二级担忧其高估值压力，且走势依赖特斯拉进展。极低的中签率与首日流通盘，注定这是一场少数人获利的高波动资金博弈。"
  },
  {
    "id": "wscn:3778902",
    "domain": "股票",
    "title": "网安行业受益于AI需求扩张，Cloudflare上调全年盈利预期",
    "url": "https://wallstreetcn.com/articles/3778902",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T23:56:03+00:00",
    "summary": "Cloudflare上调2026年全年调整后每股盈利预期至1.25至1.26美元，高于此前的1.19至1.20美元，超出华尔街平均预期的1.20美元，公司股价盘后大涨超16%。今年5月宣布裁员五分之一、转向AI优先运营模式的战略调整，并未对增长造成冲击。"
  },
  {
    "id": "wscn:3778899",
    "domain": "股票",
    "title": "中国和阿根廷续签重要协议，涉及1300亿元，有效期5年！美国曾多次作梗，想终止该协议",
    "url": "https://wallstreetcn.com/articles/3778899",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T23:53:33+00:00",
    "summary": "中国人民银行与阿根廷中央银行近日续签双边本币互换协议，规模为1300亿元人民币/28万亿阿根廷比索，有效期五年。对此，美国官员多次施压阿根廷终止协议，并污蔑该合作为\"勒索机制\"。外交部发言人林剑予以驳斥，强调中阿合作平等互利，并批评美方挑拨离间，建议其多为拉美国家发展做实事。"
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
    "id": "hn:49111879",
    "domain": "股票",
    "title": "Citadel Buys Situational Awareness's Stock Portfolio After Big Losses in AI",
    "url": "https://www.wsj.com/finance/citadel-buys-situational-awarenesss-stock-portfolio-after-big-losses-in-ai-5117159b",
    "source": "mudil",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-07-30T16:00:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49162737",
    "domain": "股票",
    "title": "Palantir soars 12% on blowout quarter, with US commercial revenue soaring ~150%",
    "url": "https://www.cnbc.com/2026/08/03/palantir-pltr-earnings-q2-2026.html",
    "source": "gslin",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-08-03T23:36:32+00:00",
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
    "id": "hn:49136787",
    "domain": "股票",
    "title": "Reddit Stock Collapses 23% as AI Eats Away at User Growth",
    "url": "https://www.barchart.com/story/news/3584357/reddit-stock-collapses-23-as-ai-eats-away-at-user-growth",
    "source": "thm",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-08-01T18:03:08+00:00",
    "summary": ""
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
    "id": "hn:49145809",
    "domain": "股票",
    "title": "As Reddit stock falls, CEO questions value of Google's AI Overviews",
    "url": "https://arstechnica.com/ai/2026/08/reddit-ceo-on-ai-overviews-were-still-looking-for-that-win-win/",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-02T16:09:26+00:00",
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
    "id": "hn:49175192",
    "domain": "金融",
    "title": "Thanks FedEx, This Is Why We Keep Getting Phished (2024)",
    "url": "https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/",
    "source": "stymaar",
    "platform": "hackernews",
    "points": 336,
    "published_at": "2026-08-04T21:09:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49200390",
    "domain": "金融",
    "title": "Federal Communications Commission scraps limit on broadcast TV ownership",
    "url": "https://www.nbcnews.com/business/media/federal-communications-commission-scraps-limit-broadcast-tv-ownership-rcna587641",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 144,
    "published_at": "2026-08-06T18:22:16+00:00",
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
    "points": 139,
    "published_at": "2026-07-31T03:32:21+00:00",
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
    "id": "hn:49184251",
    "domain": "金融",
    "title": "Fed's Kashkari says 'now is the time to start slowly moving' rates up",
    "url": "https://www.cnbc.com/2026/08/05/feds-kashkari-says-now-is-the-time-to-start-slowly-moving-rates-up.html",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-08-05T15:24:38+00:00",
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
    "id": "hn:49189030",
    "domain": "金融",
    "title": "A Fed official is asking whether AI is becoming 'too big to fail'",
    "url": "https://thenextweb.com/news/a-fed-official-is-asking-whether-ai-is-becoming-too-big-to-fail",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-08-05T21:08:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49190429",
    "domain": "金融",
    "title": "Data shows just how hard Tesla's Cybertruck has flopped",
    "url": "https://www.msn.com/en-us/autos/general/this-data-shows-just-how-hard-tesla-s-cybertruck-has-actually-flopped/ar-AA29sikQ",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-05T23:25:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49174369",
    "domain": "金融",
    "title": "Waymo CEO explains why Tesla’s camera-only self-driving falls short",
    "url": "https://electrek.co/2026/08/04/waymo-co-ceo-camera-only-self-driving-tesla/",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-08-04T20:11:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49173576",
    "domain": "金融",
    "title": "Investors in Situational Awareness deserved to lose their shirts",
    "url": "https://www.economist.com/finance-and-economics/2026/08/04/investors-in-situational-awareness-deserved-to-lose-their-shirts",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-08-04T19:18:35+00:00",
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
    "id": "rss:https://arxiv.org/abs/2608.05198",
    "domain": "金融",
    "title": "The Mathematics of Volatility Surfaces",
    "url": "https://arxiv.org/abs/2608.05198",
    "source": "Miquel Noguer i Alonso",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:00:00+00:00",
    "summary": "arXiv:2608.05198v1 Announce Type: new Abstract: This paper develops a unified mathematical theory of implied, local, and learned volatility surfaces. Total variance $w_t(k,\\tau)=\\tau\\sigma_t^2(k,\\tau)"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.05211",
    "domain": "金融",
    "title": "Legal aid eligibility and court outcomes: a design-based double-machine-learning approach",
    "url": "https://arxiv.org/abs/2608.05211",
    "source": "Fabio Italo Martinenghi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:00:00+00:00",
    "summary": "arXiv:2608.05211v1 Announce Type: new Abstract: Equality before the law is a human right, and access to high-quality legal aid for indigent defendants is essential to enforce it. In a context where al"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.05357",
    "domain": "金融",
    "title": "High-Frequency Exponential-Utility Maximization under Fractional Brownian Motion",
    "url": "https://arxiv.org/abs/2608.05357",
    "source": "Yan Dolinsky",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:00:00+00:00",
    "summary": "arXiv:2608.05357v1 Announce Type: new Abstract: We study exponential-utility maximization for high-frequency trading in a discretized fractional Brownian motion model. Using spectral methods for stati"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.05373",
    "domain": "金融",
    "title": "Velocity- and Regime-Aware Detection of Intraday Options Market Manipulation, with Explainable Attribution",
    "url": "https://arxiv.org/abs/2608.05373",
    "source": "Alex Chen, Maria Hybinette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:00:00+00:00",
    "summary": "arXiv:2608.05373v1 Announce Type: new Abstract: Intraday market manipulation is hard to detect because its footprint is brief, buried in millions of quotes, and statistically similar to ordinary volat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.05623",
    "domain": "金融",
    "title": "Non-concave Corporate Management with Option Incentives under Value-at-Risk Constraint",
    "url": "https://arxiv.org/abs/2608.05623",
    "source": "Wenyuan Li, Haoqi Lyu, Pengyu Wei",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:00:00+00:00",
    "summary": "arXiv:2608.05623v1 Announce Type: new Abstract: This article studies a dynamic corporate risk management problem by considering the decision-making of risk-averse managers who exert costly effort and "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.05755",
    "domain": "金融",
    "title": "Cross-Sectional Heterogeneity in LSTM Networks for Financial Time Series",
    "url": "https://arxiv.org/abs/2608.05755",
    "source": "Julius D\\\"obelt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:00:00+00:00",
    "summary": "arXiv:2608.05755v1 Announce Type: new Abstract: Predicting financial asset returns remains one of the most difficult challenges in empirical finance, driven by the low signal-to-noise ratio and the se"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.05901",
    "domain": "金融",
    "title": "From Value Bounds to Policy-Distance and Active-Face Certificates: Same-Grid Duality for Constrained Dynamic Portfolios",
    "url": "https://arxiv.org/abs/2608.05901",
    "source": "Jeonggyu Huh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:00:00+00:00",
    "summary": "arXiv:2608.05901v1 Announce Type: new Abstract: Neural and numerical policy solvers can produce feasible controls even when the optimal rule and its binding constraints are unavailable. A primal-dual "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.05991",
    "domain": "金融",
    "title": "Knowledge-Optimising Investment Decisions with Informative Datasets",
    "url": "https://arxiv.org/abs/2608.05991",
    "source": "Sidharth Mallik, Waymond Rodgers",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:00:00+00:00",
    "summary": "arXiv:2608.05991v1 Announce Type: new Abstract: The enormous growth in datasets, both in number and size, has prompted investors to adapt to new ways for assimilating information. Normatively, the app"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.06134",
    "domain": "金融",
    "title": "Large-Market Discipline in Combinatorial Double Auctions: No Assembly, Bundle Selection, and Complementarities",
    "url": "https://arxiv.org/abs/2608.06134",
    "source": "Konstantinos E. Zachariadis, Yongxin Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:00:00+00:00",
    "summary": "arXiv:2608.06134v1 Announce Type: new Abstract: We study double auctions for markets in which goods are valuable in bundles, such as data, model weights, and fine-tuned AI assets. A key friction in su"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.05636",
    "domain": "金融",
    "title": "Benefits of Shifting Passenger Traffic from Air to Rail: A Case Study of California High-Speed Rail",
    "url": "https://arxiv.org/abs/2608.05636",
    "source": "Kaijing Ding, Lu Dai, Mark Hansen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:00:00+00:00",
    "summary": "arXiv:2608.05636v1 Announce Type: cross Abstract: This study provides a method to quantify the benefits of shifting passenger traffic from air to high-speed rail from the perspective of flight-delay c"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.06048",
    "domain": "金融",
    "title": "Thermodynamic statistics of given names in USA and France",
    "url": "https://arxiv.org/abs/2608.06048",
    "source": "Klaus M. Frahm, Dima L. Shepelyansky",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:00:00+00:00",
    "summary": "arXiv:2608.06048v1 Announce Type: cross Abstract: Using official government data sets of USA and France we analyze the occurrence/frequency/popularity distributions of given names on a time scale of m"
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.22748",
    "domain": "金融",
    "title": "Nine Raters, One Index: Carrying LLM Disagreement into Labour-Market Estimates",
    "url": "https://arxiv.org/abs/2507.22748",
    "source": "Golo Henseke, Rhys Davies, Alan Felstead, Duncan Gallie, Francis Green, Ying Zhou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:00:00+00:00",
    "summary": "arXiv:2507.22748v4 Announce Type: replace Abstract: When a large language model supplies research annotations, the choice of model becomes an analytic degree of freedom. We ask how much that choice ma"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.10337",
    "domain": "金融",
    "title": "Optimal exit strategies of CPT gamblers in unfair gambles",
    "url": "https://arxiv.org/abs/2606.10337",
    "source": "Sang Hu, Xun Yu Zhou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:00:00+00:00",
    "summary": "arXiv:2606.10337v3 Announce Type: replace Abstract: In this paper we study optimal exit strategies of gamblers with cumulative prospect theory (CPT) preferences in games where the expected payoff is s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09990",
    "domain": "金融",
    "title": "Economic Power in International Trade",
    "url": "https://arxiv.org/abs/2607.09990",
    "source": "Ashwin Bhattathiripad, Vipin P Veetil",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:00:00+00:00",
    "summary": "arXiv:2607.09990v2 Announce Type: replace Abstract: Economic power is a country's capacity to harm another more than itself by withdrawing from a trading relationship. This paper develops a short-run "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04023",
    "domain": "金融",
    "title": "Monsoon Mayhem to Market Waves: Forecasting Fisheries Resilience in Sri Lanka",
    "url": "https://arxiv.org/abs/2608.04023",
    "source": "Ruzaini Ahmed, Yohan Jayasinghe, Tharumini Gamage, Ifaz Ikram, Hasini Lawanya, Nirasha Munasinghe, Patalee Narasinghe, Nisansa de Silva, Sandareka Wickramanayake",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:00:00+00:00",
    "summary": "arXiv:2608.04023v2 Announce Type: replace Abstract: Sri Lanka's fisheries sector is important for jobs and food supply. Between 2019 and 2025, it faced several major problems at the same time, and how"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04373",
    "domain": "金融",
    "title": "Public Trader Identity: Adverse Selection and Return Predictability",
    "url": "https://arxiv.org/abs/2608.04373",
    "source": "Daojing Zhai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T04:00:00+00:00",
    "summary": "arXiv:2608.04373v2 Announce Type: replace Abstract: Informed traders are supposed to need anonymity: they profit by hiding among the uninformed. A decentralized exchange now publishes the counterparty"
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
