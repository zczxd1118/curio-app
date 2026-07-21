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

- 今日日期：`2026-07-21`
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
  "date": "2026-07-21",
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
    "points": 3819046,
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
    "points": 1565156,
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
    "points": 1435998,
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
    "points": 1256662,
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
    "points": 987405,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 942048,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 923485,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 917668,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1mhKv68EPQ",
    "domain": "AI",
    "title": "豆包真能干活了！【豆包Agent入门教程】",
    "url": "http://www.bilibili.com/video/av116944258728161",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 726920,
    "published_at": "2026-07-19T03:00:00+00:00",
    "summary": "这个视频让你的豆包技能噌噌上涨，还有“秋芝AI科普skill”帮你答疑～\n感谢朋友们的三连+关注~"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 548719,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 502866,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 410129,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 316389,
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
    "points": 267452,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 260042,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 244074,
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
    "points": 196136,
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
    "points": 177529,
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
    "points": 162126,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 160020,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 155104,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 148503,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 113307,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1EVuqzrEMJ",
    "domain": "AI",
    "title": "【保姆级教程】手把手教你低成本制作AI女友，【一定要看置顶评论】，可随身携带，自由对话",
    "url": "http://www.bilibili.com/video/av114851468812000",
    "source": "往生堂研发",
    "platform": "bilibili",
    "points": 108728,
    "published_at": "2025-07-14T12:03:53+00:00",
    "summary": "文档地址\nhttps://github.com/xinnan-tech/xiaozhi-esp32-server/blob/main/docs/Deployment.md?_refluxos=a10#%E6%96%B9%E5%BC%8F%E4%B8%80docker%E5%8F%AA%E8%BF%90%E8%A1%8Cserver"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 98635,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 97763,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92642,
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
    "points": 73823,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1xBrDB9E42",
    "domain": "AI",
    "title": "独立开发太累？Godot + Claude Code 搭建 AI 辅助工作流，效率直接起飞！ | 地块召唤师开发实战 #01",
    "url": "http://www.bilibili.com/video/av115911319100158",
    "source": "像素夹心饼干",
    "platform": "bilibili",
    "points": 67518,
    "published_at": "2026-01-18T03:25:00+00:00",
    "summary": "大家好，这里是饼干！🍪\n这是我的新坑——**《地块召唤师》**开发实战分享的第一期。\n很多朋友问独立开发如何提升效率？这期视频我不聊虚的，直接公开我从 0 到 1 搭建的 AI + Godot 高效工作流。\n从游戏引擎的选择，到 Claude Code、Copilot 等 AI 工具的实战配置，再到如何用“明确需求”的方法论（SMART原则+双钻模型）来驾驭 AI，让它不仅仅是写代码的工具，更成为"
  },
  {
    "id": "bvid:BV1GRKJ6fEgn",
    "domain": "AI",
    "title": "Kimi K3编程能力炸裂！在Claude Code中全方位实测代码能力，能否超越Fable 5和GPT-5.6l？结果远超我的预期！国产模型跻身世界第一梯队！",
    "url": "http://www.bilibili.com/video/av116934511239163",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 65750,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53205,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1DLgWzdE3A",
    "domain": "AI",
    "title": "[mc服务器常识普及]怎么给自己管理员op权限",
    "url": "http://www.bilibili.com/video/av114897136456574",
    "source": "愿雪时yes",
    "platform": "bilibili",
    "points": 47011,
    "published_at": "2025-07-22T13:39:32+00:00",
    "summary": "蓝夜科技官网\nhttps://www.mczbc.cn/?i74e504\n主播邀请码：74e504\n\n粉丝群 941618230\n整合包推荐配置: https://www.yuque.com/yuqueyonghurwfkkx/emg34z/dsd5y8gpbrhlkgar\n蓝夜科技教程: https://www.yuque.com/yuqueyonghurwfkkx/goyxu9\n\n\n【蓝夜科技"
  },
  {
    "id": "bvid:BV1ap2fBvEt9",
    "domain": "AI",
    "title": "如何使用「Operit AI」：你的下一代AI手机助手",
    "url": "http://www.bilibili.com/video/av115677243447909",
    "source": "默睦",
    "platform": "bilibili",
    "points": 42615,
    "published_at": "2025-12-07T08:06:42+00:00",
    "summary": "下载地址：https://github.com/AAswordman/Operit\n\n相关软件资料下载：https://www.123pan.com/s/IKgAjv-Hinsv.html\n\n官方交流群：458862019"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 38719,
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
    "points": 34976,
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
    "points": 33871,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 32329,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1xzGH6uEG8",
    "domain": "AI",
    "title": "AI全自动化搭建复杂Simulink模型！5步即可完成部署，全流程分享！",
    "url": "http://www.bilibili.com/video/av116629870481178",
    "source": "电气攻城狮001",
    "platform": "bilibili",
    "points": 30146,
    "published_at": "2026-05-24T13:50:56+00:00",
    "summary": "本期分享五步实操流程，借助 Claude Code 交互载体接入 DeepSeek 大模型，搭配 2026.5.21 最新版 Simulink Agentic Toolkit，解锁 68 项建模技能。依次完成 API 额度配置、环境部署、工具包安装，连通校验后开启全自动模式。无需手动拖拽模块与布线，输入指令即可依托 Simscape 蓝库，在 MATLAB2026a 中自动搭建三相并网逆变器开环模"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28801,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1vwXPYkEGx",
    "domain": "AI",
    "title": "Cursor+mcp配置，手把手教你配置任意MCP服务，学不会你打我，小白保姆级教程~MCP服务配置指南 - 提升AI编程助手能力",
    "url": "http://www.bilibili.com/video/av114193181183930",
    "source": "三少科技",
    "platform": "bilibili",
    "points": 27025,
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
    "points": 25484,
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
    "points": 22637,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1HaN162EPT",
    "domain": "AI",
    "title": "【Codex】2026最新Codex保姆级教程，ChatGPT + Codex 开发实战全流程，环境配置、核心功能、使用技巧到项目实战一学就会，少走99%弯路！",
    "url": "http://www.bilibili.com/video/av116911660665280",
    "source": "今天AI了吗",
    "platform": "bilibili",
    "points": 22286,
    "published_at": "2026-07-13T09:01:50+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1ymNv6REs2",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent智能体零基础全套教程，2026最新版，从入门到实战！包含所有干货！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116922347686666",
    "source": "Agent智能体搭建-",
    "platform": "bilibili",
    "points": 17379,
    "published_at": "2026-07-15T05:35:41+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 16111,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 15478,
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
    "points": 15444,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV1zcSuB7EnM",
    "domain": "AI",
    "title": "【Palworld】幻兽帕鲁服务器，管理员指令简易介绍！",
    "url": "http://www.bilibili.com/video/av115620620339739",
    "source": "GssHosting",
    "platform": "bilibili",
    "points": 14593,
    "published_at": "2025-11-27T08:04:56+00:00",
    "summary": "帕鲁，物品id：https://gsshosting.com/knowledge/172\n管理员指令大全：https://gsshosting.com/knowledge/170\nGssHosting官网：https://gsshosting.com/ \n✅ 流畅不卡：独享服务器，告别延迟掉线，操作丝滑如德芙～ \n✅ 好友专属：和兄弟一起搞事，打造属于你们的帕鲁世界！ \n✅ 自由开挂：GM权限随心"
  },
  {
    "id": "bvid:BV14cZqB8EBY",
    "domain": "AI",
    "title": "AI攻克不了的领域竟然是它？揭秘CNC编程为何让AI束手无策",
    "url": "http://www.bilibili.com/video/av116097411976217",
    "source": "极微视界",
    "platform": "bilibili",
    "points": 14563,
    "published_at": "2026-02-19T12:59:23+00:00",
    "summary": "CNC编程AI化有多难？本视频深度解析为什么AI编程在制造业进展缓慢。\n从材料、刀具、机床到隐性知识，揭秘老师傅的经验为什么无法数字化。\nPowerMill、CloudNC等AI编程软件的真实水平如何？CNC编程师的未来在哪里？\n\n⏱️ 时间轴 Timestamps:\n\n00:00 开篇：AI在CNC领域的困境\n00:20 材料的复杂性：为什么同样是45#钢参数却不同\n01:01 刀具与机床的个体"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 14332,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "hn:48873836",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, CoreWeave, and Nebius: Inside the Circular Financing of the GPU Boom",
    "url": "https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom",
    "source": "adletbalzhanov",
    "platform": "hackernews",
    "points": 370,
    "published_at": "2026-07-11T17:21:49+00:00",
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
    "id": "rss:https://www.eetimes.com/uma-the-architecture-edge-ai-needs-to-scale/",
    "domain": "AI 算力 / 半导体",
    "title": "UMA: The Architecture Edge AI Needs to Scale",
    "url": "https://www.eetimes.com/uma-the-architecture-edge-ai-needs-to-scale/",
    "source": "Chris Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T19:00:00+00:00",
    "summary": "Edge AI won’t be saved by more chips; it needs unified memory to stop models from choking mid-task. The post UMA: The Architecture Edge AI Needs to Scale appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/nisshinbo-micro-devices-expands-high-voltage-ic-lineup-for-next-gen-automotive-48-v-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Nisshinbo Micro Devices Expands High-Voltage IC Lineup for Next-Gen Automotive 48 V Systems",
    "url": "https://www.eetimes.com/nisshinbo-micro-devices-expands-high-voltage-ic-lineup-for-next-gen-automotive-48-v-systems/",
    "source": "Nisshinbo Micro Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T16:00:00+00:00",
    "summary": "Addressing the new challenges posed by the shift to 48 V automotive power supplies with Nisshinbo Micro Devices The post Nisshinbo Micro Devices Expands High-Voltage IC Lineup for Next-Gen Automotive "
  },
  {
    "id": "rss:https://www.eetimes.com/powering-the-automotive-revolution-from-zonal-architecture-to-48v/",
    "domain": "AI 算力 / 半导体",
    "title": "Powering the Automotive Revolution: From Zonal Architecture to 48V",
    "url": "https://www.eetimes.com/powering-the-automotive-revolution-from-zonal-architecture-to-48v/",
    "source": "Monolithic Power Systems, Inc. (MPS)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T13:30:36+00:00",
    "summary": "Explore how Monolithic Power Systems 48V automotive solutions, including the MPQ5884-AEC1, support safer, smarter, and more efficient zonal architecture. The post Powering the Automotive Revolution: F"
  },
  {
    "id": "rss:https://www.eetimes.com/photonics-components-the-eyes-and-ears-of-the-future-unmanned-system-and-connected-soldiers/",
    "domain": "AI 算力 / 半导体",
    "title": "Photonics Components – The Eyes and Ears of the Future Unmanned System and Connected Soldiers",
    "url": "https://www.eetimes.com/photonics-components-the-eyes-and-ears-of-the-future-unmanned-system-and-connected-soldiers/",
    "source": "Arrow Electronics, ams Osram",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T13:25:52+00:00",
    "summary": "Discover how optoelectronics plays a central role in sensing and data generation, including light-based distance measurement for UAVs and robotic platforms. The post Photonics Components &#8211; The E"
  },
  {
    "id": "rss:https://www.eetimes.com/post-quantum-cryptography-incorporated-into-socs-via-efpga/",
    "domain": "AI 算力 / 半导体",
    "title": "Post-Quantum Cryptography Incorporated into SoCs via eFPGA",
    "url": "https://www.eetimes.com/post-quantum-cryptography-incorporated-into-socs-via-efpga/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T12:00:00+00:00",
    "summary": "Unlike hard-wired security engines, PQC algorithm mapped into eFPGA fabric claims to avoid costly silicon re-spins. The post Post-Quantum Cryptography Incorporated into SoCs via eFPGA appeared first o"
  },
  {
    "id": "rss:https://www.eetimes.com/risc-v-europe-summit-2026-beyond-embedded-electronics/",
    "domain": "AI 算力 / 半导体",
    "title": "RISC-V Europe Summit 2026: Beyond Embedded Electronics",
    "url": "https://www.eetimes.com/risc-v-europe-summit-2026-beyond-embedded-electronics/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T07:42:44+00:00",
    "summary": "The recent RISC-V Europe Summit in Bologna reflected the open standard's evolution toward data center, edge AI, and space applications. The post RISC-V Europe Summit 2026: Beyond Embedded Electronics "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/the-enduring-paradox-of-the-ai-economy-models-get-better-and-more-efficient-yet-costs-can-still-easily-spiral-out-of-control",
    "domain": "AI 算力 / 半导体",
    "title": "The enduring paradox of the AI economy — models get better and more efficient, yet costs can still easily spiral out of control",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/the-enduring-paradox-of-the-ai-economy-models-get-better-and-more-efficient-yet-costs-can-still-easily-spiral-out-of-control",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T19:35:42+00:00",
    "summary": "Token amplification creates a paradox in the AI economy, as more capable models beget more complicated tasks."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/taiwan-inducts-ex-tsmc-manager-for-allegedly-stealing-chip-secrets-for-china",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan indicts ex-TSMC manager for allegedly stealing chip secrets for China — first case of its kind links managers to Chinese semiconductor materials analysis company",
    "url": "https://www.tomshardware.com/tech-industry/taiwan-inducts-ex-tsmc-manager-for-allegedly-stealing-chip-secrets-for-china",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T18:13:21+00:00",
    "summary": "Taiwanese prosecutors indicted a former TSMC deputy manager on Monday for allegedly copying 21 confidential documents."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/new-plugin-unlocks-granular-vram-temperature-tracking-on-nvidia-rtx-50-series-gpus-community-cracks-open-blackwells-forbidden-telemetry-sensors",
    "domain": "AI 算力 / 半导体",
    "title": "New plugin unlocks granular VRAM temperature tracking on Nvidia RTX 50-series GPUs — community cracks open Blackwell's forbidden telemetry sensors",
    "url": "https://www.tomshardware.com/pc-components/gpus/new-plugin-unlocks-granular-vram-temperature-tracking-on-nvidia-rtx-50-series-gpus-community-cracks-open-blackwells-forbidden-telemetry-sensors",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T17:48:35+00:00",
    "summary": "Modders have discovered a method to monitor every single memory module on Nvidia's GeForce RTX 50-series (codenamed Blackwell) graphics cards."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/trump-administration-reportedly-reviving-push-to-ban-chinese-ai-models-following-kimi-k3-launch-citing-cybersecurity-concerns-downloadable-open-weights-could-make-an-outright-u-s-ban-nearly-impossible-to-enforce-amid-growing-adoption",
    "domain": "AI 算力 / 半导体",
    "title": "Trump administration reportedly reviving push to ban Chinese AI models following Kimi K3 launch, citing cybersecurity concerns — downloadable open weights could make an outright U.S. ban nearly imposs",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/trump-administration-reportedly-reviving-push-to-ban-chinese-ai-models-following-kimi-k3-launch-citing-cybersecurity-concerns-downloadable-open-weights-could-make-an-outright-u-s-ban-nearly-impossible-to-enforce-amid-growing-adoption",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T17:39:23+00:00",
    "summary": "The U.S. may be reigniting efforts to push companies away from Chinese open-weight AI models such as Kimi and DeepSeek."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/shrink-your-pc-setup-with-up-to-25-percent-off-on-kamrui-mini-pcs-big-savings-on-the-h1-for-gamers-and-the-hyper-h2-for-pros",
    "domain": "AI 算力 / 半导体",
    "title": "Shrink your PC setup with up to 25% off on Kamrui mini-PCs — big savings on the H1 for gamers and the Hyper H2 for pros",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/shrink-your-pc-setup-with-up-to-25-percent-off-on-kamrui-mini-pcs-big-savings-on-the-h1-for-gamers-and-the-hyper-h2-for-pros",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T16:32:31+00:00",
    "summary": "Kamrui's H1 and Hyper H2 mini-PCs go on sale at Amazon with discounts up to 25%."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/government-funded-dutch-report-rates-chip-sector-at-very-high-risk-of-chinese-interference",
    "domain": "AI 算力 / 半导体",
    "title": "Dutch chip sector at very high risk of Chinese interference, government-funded study warns — calls for stricter vetting at sites like ASML",
    "url": "https://www.tomshardware.com/tech-industry/government-funded-dutch-report-rates-chip-sector-at-very-high-risk-of-chinese-interference",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T15:04:14+00:00",
    "summary": "The Hague Centre for Strategic Studies has rated the Dutch semiconductor industry as being at very high risk of Chinese foreign interference."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-will-deploy-amds-helios-rack-scale-ai-accelerator-at-scale-on-azure-radeon-instinct-mi455x-and-epyc-venice-power-will-be-available-through-redmonds-cloud-infrastructure",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft will deploy AMD’s Helios rack-scale AI accelerator ‘at scale’ on Azure – Radeon Instinct MI455X and Epyc Venice power will be available through Redmond’s cloud infrastructure",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-will-deploy-amds-helios-rack-scale-ai-accelerator-at-scale-on-azure-radeon-instinct-mi455x-and-epyc-venice-power-will-be-available-through-redmonds-cloud-infrastructure",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T13:05:00+00:00",
    "summary": "Microsoft and AMD are teaming up to get Redmond more AI FLOPS for both internal and external use."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/power-companies-can-seize-private-land-to-make-way-for-new-ai-data-center-transmission-lines-report-says-takeovers-could-be-implemented-using-eminent-domain-law-when-private-citizens-refuse-to-sell-land",
    "domain": "AI 算力 / 半导体",
    "title": "Government can seize private land to make way for new AI data center transmission lines, report says — takeovers could be implemented using eminent domain law when private citizens refuse to sell land",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/power-companies-can-seize-private-land-to-make-way-for-new-ai-data-center-transmission-lines-report-says-takeovers-could-be-implemented-using-eminent-domain-law-when-private-citizens-refuse-to-sell-land",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T13:00:47+00:00",
    "summary": "Utilities can use eminent domain to seize private land for new transmission lines needed to power data centers, though public-use and state-law limits still apply."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/samsung-now-supplying-new-vesa-displayhdr-true-black-1400-laptop-displays-lenovo-asus-dell-and-msi-set-to-launch-portables-with-the-first-1-600-nits-tandem-oled-panels",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung now supplying new VESA DisplayHDR True Black 1400 laptop displays — Lenovo, Asus, Dell, and MSI set to launch portables with the first 1,600 nits tandem OLED panels",
    "url": "https://www.tomshardware.com/monitors/samsung-now-supplying-new-vesa-displayhdr-true-black-1400-laptop-displays-lenovo-asus-dell-and-msi-set-to-launch-portables-with-the-first-1-600-nits-tandem-oled-panels",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T12:18:52+00:00",
    "summary": "Samsung Display has announced that it is now supplying its first mass-produced VESA DisplayHDR True Black 1400 monitor panels to laptop makers including Lenovo, Asus, Dell, and MSI."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/3d-printing-enthusiast-resurrects-cancelled-dbrand-steam-machine-companion-cube-as-diy-project-project-shelved-due-to-copyright-can-now-be-made-and-assembled-at-home",
    "domain": "AI 算力 / 半导体",
    "title": "3D printing enthusiast resurrects cancelled dbrand Steam Machine Companion Cube as DIY project — project shelved due to copyright can now be made and assembled at home",
    "url": "https://www.tomshardware.com/3d-printing/3d-printing-enthusiast-resurrects-cancelled-dbrand-steam-machine-companion-cube-as-diy-project-project-shelved-due-to-copyright-can-now-be-made-and-assembled-at-home",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T11:25:46+00:00",
    "summary": "A 3D printing enthusiast has resurrected dbrand's cancelled Steam Machine Companion Cube as a DIY project."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd148-on-an-amd-ryzen-7-9800x3d-bundle-with-32gb-of-ram-motherboard-and-liquid-aio-start-your-am5-gaming-build-for-just-usd1-039",
    "domain": "AI 算力 / 半导体",
    "title": "Save $148 on an AMD Ryzen 7 9800X3D bundle with 32GB of RAM, motherboard, and liquid AIO — start your AM5 gaming build for just $1,039",
    "url": "https://www.tomshardware.com/pc-components/save-usd148-on-an-amd-ryzen-7-9800x3d-bundle-with-32gb-of-ram-motherboard-and-liquid-aio-start-your-am5-gaming-build-for-just-usd1-039",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T11:06:38+00:00",
    "summary": "Grab an AMD Ryzen 7 9800X3D, Gigabyte B850 motherboard, 32GB of Corsair Vengeance DDR5, and a CPU cooler for $1,039."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/logitechs-g-pro-x2-superstrike-gaming-mouse-is-usd125-99-after-getting-a-massive-usd54-discount-hall-effect-haptic-switches-8k-polling-and-30-ms-faster-clicks-for-peak-gaming-performance",
    "domain": "AI 算力 / 半导体",
    "title": "Logitech's G Pro X2 Superstrike gaming mouse is $125.99 after getting a massive $54 discount — hall-effect haptic switches, 8K polling, and 30 ms faster clicks for peak gaming performance",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/logitechs-g-pro-x2-superstrike-gaming-mouse-is-usd125-99-after-getting-a-massive-usd54-discount-hall-effect-haptic-switches-8k-polling-and-30-ms-faster-clicks-for-peak-gaming-performance",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T11:06:02+00:00",
    "summary": "The first big discount on Logitech's new G Pro X2 Superstrike haptic gaming mouse. Save $54 at Amazon, and grab this high-tech mouse at its lowest-ever price."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/creality-k2-se-3d-printer-price-slashed-by-17-percent-now-under-usd250-grab-a-competitive-entry-level-high-speed-multicolor-device-at-a-bargain-price",
    "domain": "AI 算力 / 半导体",
    "title": "Creality K2 SE 3D printer price slashed by 17%, now under $250 — grab a competitive entry-level high-speed multicolor device at a bargain price",
    "url": "https://www.tomshardware.com/pc-components/creality-k2-se-3d-printer-price-slashed-by-17-percent-now-under-usd250-grab-a-competitive-entry-level-high-speed-multicolor-device-at-a-bargain-price",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T15:04:07+00:00",
    "summary": "The Creality K2 SE drops to $248.99 in this limited-time deal, making it a great option for anyone looking to start 3D printing but want to have access to some advanced features."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-next-gen-10-core-medusa-point-apu-shows-up-on-geekbench-again-with-its-best-score-yet-leaked-sku-outpaces-every-other-x86-mobile-chip-in-the-single-core-test",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's next-gen 10-core 'Medusa Point' APU shows up on Geekbench again, with its best score yet — leaked SKU outpaces every other x86 mobile chip in the single-core test",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-next-gen-10-core-medusa-point-apu-shows-up-on-geekbench-again-with-its-best-score-yet-leaked-sku-outpaces-every-other-x86-mobile-chip-in-the-single-core-test",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T14:35:00+00:00",
    "summary": "AMD's next 10-core mobile part from the Medusa Point family is looking a lot faster than its previous two Gorgon Point and Strix Point SKUs, respectively. Early leaks keep highlighting an ever-improvi"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/zilog-z80-turns-50-as-open-source-replacement-heads-for-drop-in-dip40-silicon",
    "domain": "AI 算力 / 半导体",
    "title": "Zilog Z80 turns 50 as an open-source replacement heads to drop-in DIP40 silicon — iconic 8-bit CPU launched in July 1976 and was discontinued in 2024",
    "url": "https://www.tomshardware.com/tech-industry/zilog-z80-turns-50-as-open-source-replacement-heads-for-drop-in-dip40-silicon",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T14:12:55+00:00",
    "summary": "The original Z80 packed 8,500 transistors on a 4μm process and typically ran at 2.5 MHz."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/memory-chip-boss-admits-ram-prices-are-abnormally-high-sk-group-chairman-considering-building-a-semiconductor-plant-in-the-us-to-expand-supply-calm-chipflation",
    "domain": "AI 算力 / 半导体",
    "title": "Memory chip boss admits RAM prices are 'abnormally high' — SK Group chairman considering building a semiconductor plant in the US to expand supply, calm ‘chipflation’",
    "url": "https://www.tomshardware.com/tech-industry/policy/memory-chip-boss-admits-ram-prices-are-abnormally-high-sk-group-chairman-considering-building-a-semiconductor-plant-in-the-us-to-expand-supply-calm-chipflation",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T13:55:00+00:00",
    "summary": "SK Group Chairman Chey Tae-won said that prices for memory chips are \"abnormally high\" and that the industry must take steps to increase production and reduce prices. If it fails to do that, new entra"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/phantom-twist-drone-spins-so-fast-that-it-is-nearly-invisible-flying-device-adds-motion-blur-to-the-real-world",
    "domain": "AI 算力 / 半导体",
    "title": "‘Phantom Twist’ drone spins so fast that it is nearly invisible — flying device adds motion blur to the real world",
    "url": "https://www.tomshardware.com/tech-industry/drones/phantom-twist-drone-spins-so-fast-that-it-is-nearly-invisible-flying-device-adds-motion-blur-to-the-real-world",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T13:27:34+00:00",
    "summary": "Researchers from Northwestern University in Illinois have built a drone that rotates so fast it is cloaked by motion blur."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/samsung-cuts-hundreds-of-us-consumer-electronics-jobs-ahead-of-texas-hq-move",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung cuts hundreds of US consumer electronics jobs ahead of Texas HQ move — 739 roles affected in New Jersey as chip division posts record profit",
    "url": "https://www.tomshardware.com/tech-industry/samsung-cuts-hundreds-of-us-consumer-electronics-jobs-ahead-of-texas-hq-move",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T12:48:01+00:00",
    "summary": "Samsung told Reuters that a majority of the affected New Jersey employees received relocation offers, while others were let go."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/russian-drones-spotted-using-screwed-on-magnetic-compasses-as-navigation-aids-the-on-board-camera-can-occasionally-tilt-down-to-check-bearings-if-satellite-comms-are-lost",
    "domain": "AI 算力 / 半导体",
    "title": "Russian drones spotted using screwed-on magnetic compasses as navigation aids — the on-board camera can occasionally tilt down to check bearings if satellite comms are lost",
    "url": "https://www.tomshardware.com/tech-industry/drones/russian-drones-spotted-using-screwed-on-magnetic-compasses-as-navigation-aids-the-on-board-camera-can-occasionally-tilt-down-to-check-bearings-if-satellite-comms-are-lost",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T12:05:34+00:00",
    "summary": "Russian drone troops are adding cheap magnetic compasses to help find their bearings. Crude add-on helps them find their bearings and locate their targets even without GPS."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/coil-whine-can-be-musical-demonstrates-engineering-student-this-usually-hated-noise-can-make-some-people-happy",
    "domain": "AI 算力 / 半导体",
    "title": "Coil whine can be musical, demonstrates engineering student — this usually hated noise can make some people happy",
    "url": "https://www.tomshardware.com/pc-components/coil-whine-can-be-musical-demonstrates-engineering-student-this-usually-hated-noise-can-make-some-people-happy",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T11:20:34+00:00",
    "summary": "Video shows that electronic noise pollution can become music."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/clever-hacker-fits-537-000-domains-in-a-tiny-usd5-esp32-ad-blocking-dongle-firmware-uses-only-around-50kb-of-ram-and-can-answer-blocked-lookups-in-10-milliseconds",
    "domain": "AI 算力 / 半导体",
    "title": "Clever hacker fits 537,000 domains in a tiny $5 ESP32 ad-blocking dongle — firmware uses only around 50KB of RAM and can answer blocked lookups in 10 milliseconds",
    "url": "https://www.tomshardware.com/networking/clever-hacker-fits-537-000-domains-in-a-tiny-usd5-esp32-ad-blocking-dongle-firmware-uses-only-around-50kb-of-ram-and-can-answer-blocked-lookups-in-10-milliseconds",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T10:00:00+00:00",
    "summary": "This project uses a clever hashing trick to fit over half a million blocked domains into just 4MB of flash memory."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/crazed-enthusiast-runs-pc-on-192-aa-batteries-successfully-boots-into-hannah-montana-linux-system-is-stable-during-stress-testing-and-even-plays-freedoom",
    "domain": "AI 算力 / 半导体",
    "title": "Crazed enthusiast runs PC on 192 AA batteries, successfully boots into Hannah Montana Linux — System is stable during stress testing and even plays FreeDoom",
    "url": "https://www.tomshardware.com/desktops/pc-building/crazed-enthusiast-runs-pc-on-192-aa-batteries-successfully-boots-into-hannah-montana-linux-system-is-stable-during-stress-testing-and-even-plays-freedoom",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T10:00:00+00:00",
    "summary": "A creator by the name of \"Uwoslab\" just jerry-rigged three battery banks together, each made up of 64 AA Alkaline cells, to form a giant 192-cell array that's enough to power an AM4 system."
  },
  {
    "id": "rss:https://www.eetimes.com/new-material-beats-coppers-thermal-conductivity/",
    "domain": "AI 算力 / 半导体",
    "title": "New Material Beats Copper’s Thermal Conductivity",
    "url": "https://www.eetimes.com/new-material-beats-coppers-thermal-conductivity/",
    "source": "Bill Schweber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T19:00:00+00:00",
    "summary": "Meet θ-TaN, a metal that moves heat nearly 3× better than copper—and could upend chip cooling layers. The post New Material Beats Copper’s Thermal Conductivity appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/asml-raises-outlook-plans-more-euv-capacity/",
    "domain": "AI 算力 / 半导体",
    "title": "ASML Raises Outlook, Plans More EUV Capacity",
    "url": "https://www.eetimes.com/asml-raises-outlook-plans-more-euv-capacity/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T14:00:00+00:00",
    "summary": "ASML raised its full-year outlook as AI demand prompted plans to expand lithography capacity through at least 2028. The post ASML Raises Outlook, Plans More EUV Capacity appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/gta-3-and-vice-city-are-now-playable-inside-san-andreas-a-mod-lets-you-revisit-liberty-city-and-vice-city-without-leaving-san-andreas",
    "domain": "AI 算力 / 半导体",
    "title": "GTA 3 and Vice City are now playable inside San Andreas — a mod lets you revisit Liberty City and Vice City without leaving San Andreas",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/gta-3-and-vice-city-are-now-playable-inside-san-andreas-a-mod-lets-you-revisit-liberty-city-and-vice-city-without-leaving-san-andreas",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T17:48:22+00:00",
    "summary": "A GTA modder has embedded GTA 3 and Vice City within San Andreas, even nesting Vice City within GTA 3, with all three games continuing to run simultaneously."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-new-ryzen-7-7700x3d-plummets-to-usd279-days-after-launch-the-x3d-chip-rules-the-mid-range-at-its-discounted-price",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s new Ryzen 7 7700X3D plummets to $279 days after launch — the X3D chip rules the mid-range at its discounted price",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-new-ryzen-7-7700x3d-plummets-to-usd279-days-after-launch-the-x3d-chip-rules-the-mid-range-at-its-discounted-price",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T17:40:13+00:00",
    "summary": "The Ryzen 7 7700X3D has suddenly become a solid value thanks to a $50 promo code, knocking its price down from $329 to just $279 on Newegg."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/strapping-11-fans-and-a-360mm-aio-to-an-rtx-3080-sounds-crazy-until-you-see-the-30-c-temp-drop-modded-gpu-delivered-less-than-5-fps-uplift",
    "domain": "AI 算力 / 半导体",
    "title": "Strapping 11 fans and a 360mm AIO to an RTX 3080 sounds crazy until you see the 30°C temp drop — modded GPU delivered less than 5 FPS uplift at turbojet noise levels",
    "url": "https://www.tomshardware.com/pc-components/cooling/strapping-11-fans-and-a-360mm-aio-to-an-rtx-3080-sounds-crazy-until-you-see-the-30-c-temp-drop-modded-gpu-delivered-less-than-5-fps-uplift",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T17:22:49+00:00",
    "summary": "TrashBench recently decided to test whether adding more and more fans to a powerful GPU would improve its performance."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/jurassic-park-packed-usd4-million-of-legit-1993-computer-hardware-a-software-engineer-detailed-every-single-piece-of-hardware-in-the-film",
    "domain": "AI 算力 / 半导体",
    "title": "Jurassic Park packed $4 million of legit 1993 computer hardware — a software engineer detailed every single piece of hardware in the film",
    "url": "https://www.tomshardware.com/desktops/jurassic-park-packed-usd4-million-of-legit-1993-computer-hardware-a-software-engineer-detailed-every-single-piece-of-hardware-in-the-film",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T17:12:53+00:00",
    "summary": "Google software engineer Fabien Sanglard meticulously listed the computer hardware and software used in the first Jurassic Park film. He even added details for each device, turning the film into somet"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/grab-amds-ryzen-7-5800x3d-10th-anniversary-cpu-with-motherboard-and-16gb-ram-for-just-usd529-save-over-usd100-on-this-epic-amd-gaming-bundle",
    "domain": "AI 算力 / 半导体",
    "title": "Grab AMD’s Ryzen 7 5800X3D 10th Anniversary CPU with motherboard and 16GB RAM for just $529 — save over $100 on this epic AMD gaming bundle",
    "url": "https://www.tomshardware.com/pc-components/cpus/grab-amds-ryzen-7-5800x3d-10th-anniversary-cpu-with-motherboard-and-16gb-ram-for-just-usd529-save-over-usd100-on-this-epic-amd-gaming-bundle",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T15:19:27+00:00",
    "summary": "Newegg has a great combo bundle on sale with over $100 in savings for the fastest DDR4 gaming system you can build today. It pairs a Ryzen 7 5800X3D with 16GB of CL16 DDR4-3200 RAM and an Asus TUF Gam"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-50-super-gpus-are-reportedly-ready-but-stuck-in-limbo-due-to-excessive-gddr7-pricing-3gb-gddr7-module-costs-triple-the-price-of-2gb",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX 50 Super GPUs are reportedly ready, but stuck in limbo due to excessive GDDR7 pricing — 3GB GDDR7 module costs triple the price of 2GB",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-50-super-gpus-are-reportedly-ready-but-stuck-in-limbo-due-to-excessive-gddr7-pricing-3gb-gddr7-module-costs-triple-the-price-of-2gb",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T13:45:42+00:00",
    "summary": "The 3GB GDDR7 chips that the RTX 50 Super GPUs will use reportedly cost twice to thrice as much as the 2GB chips found on vanilla RTX 50-series graphics cards. This would likely push the retail price "
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/nvidia-ceo-jensen-huangs-trademark-leather-jacket-raises-nearly-usd1-million-at-charity-auction-bidding-makes-usd60-000-valuation-look-like-pocket-change",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang’s trademark leather jacket raises nearly $1 Million at charity auction — bidding makes $60,000 valuation look like pocket change",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/nvidia-ceo-jensen-huangs-trademark-leather-jacket-raises-nearly-usd1-million-at-charity-auction-bidding-makes-usd60-000-valuation-look-like-pocket-change",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T13:22:12+00:00",
    "summary": "‘The Jensen Jacket’ achieved a hammer price of $960,000 this weekend."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/security-engineer-ports-password-cracker-hashcat-to-gameboy-advance-16-8-mhz-chip-can-perform-a-meager-727-hashes-a-second-30-million-times-slower-than-a-modern-rig",
    "domain": "AI 算力 / 半导体",
    "title": "Security engineer ports password cracker hashcat to Gameboy Advance — 16.8 MHz chip can perform a meager 727 hashes a second, 30 million times slower than a modern rig",
    "url": "https://www.tomshardware.com/video-games/nintendo/security-engineer-ports-password-cracker-hashcat-to-gameboy-advance-16-8-mhz-chip-can-perform-a-meager-727-hashes-a-second-30-million-times-slower-than-a-modern-rig",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T11:30:00+00:00",
    "summary": "Gameboy Advance port of hashcat allows for advanced password cracking in meager hardware — so long as you're willing to wait"
  },
  {
    "id": "hn:48894277",
    "domain": "AI 算力 / 半导体",
    "title": "Apple's rumored M7 Ultra targets 1.5TB and Blackwell-class AI performance",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/apples-rumored-m7-ultra-targets-1-5tb-of-memory-and-blackwell-class-ai",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-07-13T15:32:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48845518",
    "domain": "AI 算力 / 半导体",
    "title": "Reverse-engineering Nvidia's CUDA-checkpoint for faster cold starts",
    "url": "https://blog.doubleword.ai/what-happens-when-you-checkpoint-a-cuda-process",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-09T13:29:52+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/tsmc-boosts-2026-expansion-budget-adds-100b-to-u-s-investment/",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Boosts 2026 Expansion Budget, Adds $100B to U.S. Investment",
    "url": "https://www.eetimes.com/tsmc-boosts-2026-expansion-budget-adds-100b-to-u-s-investment/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T05:55:59+00:00",
    "summary": "TSMC is raising its 2026 capital budget to $64 billion and adding $100 billion to its U.S. investment for AI. The post TSMC Boosts 2026 Expansion Budget, Adds $100B to U.S. Investment appeared first o"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-data-centers-push-silicon-photonics-toward-300-mm-scale/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Data Centers Push Silicon Photonics Toward 300-mm Scale",
    "url": "https://www.eetimes.com/ai-data-centers-push-silicon-photonics-toward-300-mm-scale/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T14:00:00+00:00",
    "summary": "AI data centers are torching copper’s reign as ST pushes 300-mm silicon photonics for faster, denser optical links. The post AI Data Centers Push Silicon Photonics Toward 300-mm Scale appeared first o"
  },
  {
    "id": "hn:48734960",
    "domain": "AI 算力 / 半导体",
    "title": "Etched has officially come out of stealth",
    "url": "https://www.bloomberg.com/news/articles/2026-06-30/ai-chip-startup-etched-says-jane-street-tsmc-linked-vc-invested",
    "source": "seventeen29",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-30T16:21:13+00:00",
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
    "id": "hn:48925271",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://turntrout.com/why-i-left-google-deepmind",
    "source": "apsec112",
    "platform": "hackernews",
    "points": 364,
    "published_at": "2026-07-15T18:40:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:48662999",
    "domain": "大厂 AI 动态",
    "title": "Computer use in Gemini 3.5 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/",
    "source": "swolpers",
    "platform": "hackernews",
    "points": 242,
    "published_at": "2026-06-24T17:21:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:48965880",
    "domain": "大厂 AI 动态",
    "title": "Ollama: All Aboard Open Models",
    "url": "https://ollama.com/blog/all-aboard-open-models",
    "source": "inferhaven",
    "platform": "hackernews",
    "points": 136,
    "published_at": "2026-07-19T07:59:44+00:00",
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
    "id": "hn:48983890",
    "domain": "大厂 AI 动态",
    "title": "Cue AI",
    "url": "https://deepmind.google/models/gemma/gemmaverse/cue-ai/",
    "source": "logickkk1",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-07-20T19:41:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48980930",
    "domain": "大厂 AI 动态",
    "title": "Chrome installed a global Ctrl+G keyboard shortcut to launch Gemini",
    "url": "https://mastodon.online/users/mwichary/statuses/116952836351215165",
    "source": "jervant",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-20T16:17:17+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/968375/sony-udio-lawsuit-songs-ai-copyright",
    "domain": "大厂 AI 动态",
    "title": "Here are the 30,000 songs Sony is suing Udio&#8217;s AI music generator over",
    "url": "https://www.theverge.com/tech/968375/sony-udio-lawsuit-songs-ai-copyright",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T22:19:12+00:00",
    "summary": "Sony Music Entertainment has filed another lawsuit against Udio, accusing the AI music generator of infringing the copyright of more than 30,000 of its songs, ranging from Elvis Presley's Hound Dog to"
  },
  {
    "id": "rss:https://www.theverge.com/news/968310/fcc-dji-drone-camera-ban-skyrover-xtra",
    "domain": "大厂 AI 动态",
    "title": "The FCC is planning to retroactively ban disguised DJI gadgets",
    "url": "https://www.theverge.com/news/968310/fcc-dji-drone-camera-ban-skyrover-xtra",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T22:16:14+00:00",
    "summary": "Last October, we told you how the FCC had given itself the power to retroactively ban gadgets that have already received its approval to be imported and sold in the United States. Now, the FCC's getti"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/968337/the-odyssey-imax-screenings-christopher-nolan",
    "domain": "大厂 AI 动态",
    "title": "The Odyssey turned me into an IMAX believer",
    "url": "https://www.theverge.com/entertainment/968337/the-odyssey-imax-screenings-christopher-nolan",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T21:47:37+00:00",
    "summary": "After seeing Christopher Nolan's The Odyssey for the first time early last week, I came away impressed, but somewhat conflicted about two of the film's more fantastical set pieces. While those scenes "
  },
  {
    "id": "rss:https://www.theverge.com/business/968257/spacex-in-your-index-fund-explained",
    "domain": "大厂 AI 动态",
    "title": "SpaceX in your index fund, explained",
    "url": "https://www.theverge.com/business/968257/spacex-in-your-index-fund-explained",
    "source": "Elizabeth Lopatto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T21:00:00+00:00",
    "summary": "Index funds are touted as one of the safest ways to invest. Rather than picking and choosing individual stocks, index funds let you bet on the market as a whole. So what happens when a company like Sp"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/968191/humble-2k-megahits-bundle-xcom-borderlands-duke-nukem-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Get Borderlands 3, Risk of Rain 2 and 13 other great PC games for $15",
    "url": "https://www.theverge.com/gadgets/968191/humble-2k-megahits-bundle-xcom-borderlands-duke-nukem-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T20:08:51+00:00",
    "summary": "The aptly-named “2K Megahits 2026 Bundle” from Humble includes 15 Steam games for $15. It’s a smattering of the publisher 2K’s biggest games of the 2010s, including BioShock Infinite, Risk of Rain 2, "
  },
  {
    "id": "rss:https://www.theverge.com/tech/967989/hallmark-keepsake-playstation-ornament-hands-on",
    "domain": "大厂 AI 动态",
    "title": "The PlayStation replica ornament is an homage to a great, yet fragile console",
    "url": "https://www.theverge.com/tech/967989/hallmark-keepsake-playstation-ornament-hands-on",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T20:06:40+00:00",
    "summary": "You probably know the signature PlayStation boot sound. Did you know that it's technically a multi-part chime? There's the synthy section where \"Sony Computer Entertainment\" shows onscreen with a whit"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/968205/ford-electric-truck-uev-30000-affordable",
    "domain": "大厂 AI 动态",
    "title": "Ford&#8217;s $30,000 electric truck: all the news about the company&#8217;s big EV re-do",
    "url": "https://www.theverge.com/transportation/968205/ford-electric-truck-uev-30000-affordable",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T19:18:45+00:00",
    "summary": "The end of the Ford F-150 Lightning was also the start of a new era for the automaker. After failing to capture the market with the electric version of its popular F-Series truck, Ford is going back t"
  },
  {
    "id": "rss:https://www.theverge.com/business/968055/paramount-wbd-merger-pause-tro",
    "domain": "大厂 AI 动态",
    "title": "Judge pauses Paramount’s attempt to buy Warner Bros. Discovery",
    "url": "https://www.theverge.com/business/968055/paramount-wbd-merger-pause-tro",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T17:37:53+00:00",
    "summary": "A judge partially granted the request from a dozen state attorneys general to temporarily place the $110 billion merger of Paramount and Warner Bros. Discovery on hold, as reported by Variety and Reut"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/967993/lg-27-inch-ultragear-glossy-oled-gaming-monitor-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "LG&#8217;s glossy OLED gaming monitor is rare to find under $400",
    "url": "https://www.theverge.com/gadgets/967993/lg-27-inch-ultragear-glossy-oled-gaming-monitor-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T16:34:24+00:00",
    "summary": "If you&#8217;ve been thinking about upgrading your gaming monitor, LG&#8217;s 27-inch 27GX704A-B pairs a glossy WOLED panel with a fast refresh rate, and it’s currently on sale for $379.99 (about $70 "
  },
  {
    "id": "rss:https://www.theverge.com/tech/967983/lg-monitors-mcafee-adware-gamers-nexus",
    "domain": "大厂 AI 动态",
    "title": "LG’s monitors come with an unwanted addition for Windows: McAfee pop-up ads",
    "url": "https://www.theverge.com/tech/967983/lg-monitors-mcafee-adware-gamers-nexus",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T16:14:58+00:00",
    "summary": "A video from Gamers Nexus explains how, after connecting a new LG UltraGear monitor to a PC running Windows 11 for the first time, Windows Update is silently installing LG driver updates and the LG Mo"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/20/anthropics-landmark-1-5b-copyright-settlement-is-approved/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s landmark $1.5B copyright settlement is approved",
    "url": "https://techcrunch.com/2026/07/20/anthropics-landmark-1-5b-copyright-settlement-is-approved/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T00:12:24+00:00",
    "summary": "The final approval settles one case, but it doesn't resolve the broader issue of using copyrighted works to train AI models."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/20/colossal-biosciences-reportedly-in-talks-to-raise-new-capital-at-20b-30b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Colossal Biosciences reportedly in talks to raise new capital at $20B–$30B valuation",
    "url": "https://techcrunch.com/2026/07/20/colossal-biosciences-reportedly-in-talks-to-raise-new-capital-at-20b-30b-valuation/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T23:39:35+00:00",
    "summary": "The de-extinction startup is looking to double or triple its previous valuation, according to the report."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/20/trumps-latest-ai-czar-has-already-resigned/",
    "domain": "大厂 AI 动态",
    "title": "Trump’s latest AI czar has already resigned",
    "url": "https://techcrunch.com/2026/07/20/trumps-latest-ai-czar-has-already-resigned/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T22:21:04+00:00",
    "summary": "The director role for the Center for AI Standards and Innovation (CAISI) has become a revolving door since David Sacks left his position as czar."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/20/google-is-working-on-a-new-ai-chip-designed-to-make-gemini-more-efficient/",
    "domain": "大厂 AI 动态",
    "title": "Google is working on a new AI chip designed to make Gemini more efficient",
    "url": "https://techcrunch.com/2026/07/20/google-is-working-on-a-new-ai-chip-designed-to-make-gemini-more-efficient/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T21:21:15+00:00",
    "summary": "Alphabet, Google's parent company, is reportedly working on a new chip designed to make its Gemini models run much more efficiently."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/20/ais-most-important-protocol-is-getting-a-little-bit-easier-to-use/",
    "domain": "大厂 AI 动态",
    "title": "AI’s most important protocol is getting a little bit easier to use",
    "url": "https://techcrunch.com/2026/07/20/ais-most-important-protocol-is-getting-a-little-bit-easier-to-use/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T20:50:40+00:00",
    "summary": "Under the new system, the protocol will take a looser, \"stateless\" approach to session IDs on the server side, similar to how most ordinary websites already work."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/20/x-relaunches-a-rebuilt-android-app-after-year-long-effort/",
    "domain": "大厂 AI 动态",
    "title": "X relaunches a rebuilt Android app after year-long effort",
    "url": "https://techcrunch.com/2026/07/20/x-relaunches-a-rebuilt-android-app-after-year-long-effort/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T19:37:39+00:00",
    "summary": "X says the rebuilt version of its Android app is now available globally."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/20/openai-is-scared-of-open-weight-models-should-the-us-be/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI is scared of open-weight models. Should the US be?",
    "url": "https://techcrunch.com/2026/07/20/openai-is-scared-of-open-weight-models-should-the-us-be/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T19:33:25+00:00",
    "summary": "Talk of banning Chinese-made open-weight LLMs reveals the challenge of turning AI into a business."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/20/natural-raises-30m-to-reinvent-payments-for-ai-agents-and-take-on-stripe/",
    "domain": "大厂 AI 动态",
    "title": "Natural raises $30M to reinvent payments for AI agents — and take on Stripe",
    "url": "https://techcrunch.com/2026/07/20/natural-raises-30m-to-reinvent-payments-for-ai-agents-and-take-on-stripe/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T19:11:25+00:00",
    "summary": "The one-year-old startup aims to reinvent financial architecture for autonomous AI transactions."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/20/judge-pauses-110b-paramount-warner-bros-merger/",
    "domain": "大厂 AI 动态",
    "title": "Judge pauses $110B Paramount-Warner Bros. merger",
    "url": "https://techcrunch.com/2026/07/20/judge-pauses-110b-paramount-warner-bros-merger/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T17:58:50+00:00",
    "summary": "The lawsuit from the states alleges that the deal would harm movie theaters, basic cable distributors, and audiences."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/20/adobe-camera-apps-new-feature-will-critique-your-photos-using-ai/",
    "domain": "大厂 AI 动态",
    "title": "Adobe camera app’s new feature will critique your photos using AI",
    "url": "https://techcrunch.com/2026/07/20/adobe-camera-apps-new-feature-will-critique-your-photos-using-ai/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T15:45:00+00:00",
    "summary": "Adobe's Project Indigo can now remove all kinds of backgrounds from photos you snap using the app."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/20/hackers-are-exploiting-recently-patched-wordpress-bugs-putting-millions-of-websites-at-risk/",
    "domain": "大厂 AI 动态",
    "title": "Hackers are exploiting recently patched WordPress bugs, putting millions of websites at risk",
    "url": "https://techcrunch.com/2026/07/20/hackers-are-exploiting-recently-patched-wordpress-bugs-putting-millions-of-websites-at-risk/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T15:35:37+00:00",
    "summary": "Two critical security flaws in WordPress’ software have given hackers the chance to remotely take over tens of millions of websites, according to an estimate by a cybersecurity researcher."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/",
    "domain": "大厂 AI 动态",
    "title": "YouTube clarifies policies around AI slop and upsetting videos",
    "url": "https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T15:23:06+00:00",
    "summary": "YouTube has updated its monetization policies to more clearly define the kinds of AI-generated and low-quality videos that can’t earn ad revenue."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/20/inference-startup-infinity-raises-15m-from-touring-capital-openai-and-athropic-researchers/",
    "domain": "大厂 AI 动态",
    "title": "Inference startup Infinity raises $15M from Touring Capital, OpenAI and Anthropic researchers",
    "url": "https://techcrunch.com/2026/07/20/inference-startup-infinity-raises-15m-from-touring-capital-openai-and-athropic-researchers/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T15:15:00+00:00",
    "summary": "AI infrastructure company Infinity announced Monday a $15 million raise at a $100 million valuation from investors including Touring Capital, Principal VC, and researchers from companies such as OpenA"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/20/hackers-stole-significant-amount-of-data-from-tech-firm-relied-on-by-thousands-of-us-hospitals-and-pharmacies/",
    "domain": "大厂 AI 动态",
    "title": "Hackers stole ‘significant’ amount of data from tech firm relied on by thousands of US hospitals and pharmacies",
    "url": "https://techcrunch.com/2026/07/20/hackers-stole-significant-amount-of-data-from-tech-firm-relied-on-by-thousands-of-us-hospitals-and-pharmacies/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T15:01:20+00:00",
    "summary": "Edinburgh-based tech firm Craneware said customer data was stolen during a cyberattack. The company makes software that thousands of U.S. hospitals, pharmacies, and clinics rely on for billing patient"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/20/watch-flock-safety-ceo-garrett-langley-discuss-the-future-of-surveillance-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Watch Flock Safety CEO Garrett Langley discuss the future of surveillance at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/07/20/watch-flock-safety-ceo-garrett-langley-discuss-the-future-of-surveillance-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T14:30:00+00:00",
    "summary": "Flock Safety sits right at the center of the debate over where the line should be drawn between privacy and public safety. That’s why we’re bringing Flock’s founder and CEO Garrett Langley to the stag"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/20/hugging-face-confirms-breach-affected-internal-datasets-and-credentials-urges-users-to-take-action/",
    "domain": "大厂 AI 动态",
    "title": "Hugging Face confirms breach affected internal datasets and credentials, urges users to take action",
    "url": "https://techcrunch.com/2026/07/20/hugging-face-confirms-breach-affected-internal-datasets-and-credentials-urges-users-to-take-action/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T12:39:28+00:00",
    "summary": "Hugging Face is urging users to rotate any access tokens stored on the platform and review account activity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/20/strictlyvc-returns-to-new-york-city-september-10-to-celebrate-a-huge-year-for-the-citys-startup-community/",
    "domain": "大厂 AI 动态",
    "title": "StrictlyVC returns to New York City September 10 to celebrate a huge year for the city’s startup community",
    "url": "https://techcrunch.com/2026/07/20/strictlyvc-returns-to-new-york-city-september-10-to-celebrate-a-huge-year-for-the-citys-startup-community/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T12:30:00+00:00",
    "summary": "For the first time since 2024, StrictlyVC is coming back to New York City — and we're bringing the kind of access you’d expect from an under-wraps event to the whole startup, VC, and dealmaking commun"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/19/netflix-paid-587m-for-ben-afflecks-ai-filmmaking-startup/",
    "domain": "大厂 AI 动态",
    "title": "Netflix paid $587M for Ben Affleck’s AI filmmaking startup",
    "url": "https://techcrunch.com/2026/07/19/netflix-paid-587m-for-ben-afflecks-ai-filmmaking-startup/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T21:45:00+00:00",
    "summary": "Netflix revealed that it paid $587 million in cash for InterPositive, a startup co-founded by Ben Affleck."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/19/what-to-watch-for-after-jensen-huangs-japan-visit/",
    "domain": "大厂 AI 动态",
    "title": "What to watch for after Jensen Huang’s Japan visit",
    "url": "https://techcrunch.com/2026/07/19/what-to-watch-for-after-jensen-huangs-japan-visit/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T21:16:07+00:00",
    "summary": "Jensen Huang left Tokyo with deals spanning Japan's entire tech ecosystem."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/19/can-an-apple-lawsuit-derail-openais-hardware-plans/",
    "domain": "大厂 AI 动态",
    "title": "Can an Apple lawsuit derail OpenAI’s hardware plans?",
    "url": "https://techcrunch.com/2026/07/19/can-an-apple-lawsuit-derail-openais-hardware-plans/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T19:24:45+00:00",
    "summary": "On the latest episode of Equity, we debate whether Apple's lawsuit will cast a shadow over OpenAi's much-discussed plans to get into hardware and go public."
  },
  {
    "id": "rss:https://stratechery.com/2026/whos-afraid-of-chinese-models/",
    "domain": "大厂 AI 动态",
    "title": "Who’s Afraid of Chinese Models?",
    "url": "https://stratechery.com/2026/whos-afraid-of-chinese-models/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T11:00:08+00:00",
    "summary": "Everyone is worried about Chinese models, but the frontier labs will be fine; we need to enable open U.S. alternatives."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/cop-charged-with-covering-bodycam-to-photograph-naked-prisoners/",
    "domain": "大厂 AI 动态",
    "title": "DA: Cop covered bodycam to snap nude prisoners on his iPhone—but other cams caught him",
    "url": "https://arstechnica.com/tech-policy/2026/07/cop-charged-with-covering-bodycam-to-photograph-naked-prisoners/",
    "source": "Nate Anderson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T22:15:51+00:00",
    "summary": "Pennsylvania cop charged with oppression and obstruction."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/firefighting-drones-in-the-works-as-wildfires-plague-us-nearly-year-round/",
    "domain": "大厂 AI 动态",
    "title": "Firefighting drones in the works as wildfires plague US nearly year-round",
    "url": "https://arstechnica.com/ai/2026/07/firefighting-drones-in-the-works-as-wildfires-plague-us-nearly-year-round/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T21:55:52+00:00",
    "summary": "California and XPRIZE competition tests whether drones can stop wildfires early."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/judge-halts-paramounts-111b-purchase-of-warner-bros-in-win-for-us-states/",
    "domain": "大厂 AI 动态",
    "title": "Judge halts Paramount's $111B purchase of Warner Bros. in win for US states",
    "url": "https://arstechnica.com/tech-policy/2026/07/judge-halts-paramounts-111b-purchase-of-warner-bros-in-win-for-us-states/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T21:10:14+00:00",
    "summary": "Judge grants restraining order, saying merger \"likely to violate antitrust laws.\""
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/the-space-force-is-now-seeking-to-buy-up-to-30-billion-in-rocket-launches/",
    "domain": "大厂 AI 动态",
    "title": "The Space Force is now seeking to buy up to $30 billion in rocket launches",
    "url": "https://arstechnica.com/space/2026/07/the-space-force-is-now-seeking-to-buy-up-to-30-billion-in-rocket-launches/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T20:30:25+00:00",
    "summary": "The Trump administration is asking the Space Force to do a lot. This will require more launches."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/att-loses-key-ruling-in-bid-to-stop-offering-basic-phone-service-in-california/",
    "domain": "大厂 AI 动态",
    "title": "AT&T loses key ruling in bid to stop offering basic phone service in California",
    "url": "https://arstechnica.com/tech-policy/2026/07/att-loses-key-ruling-in-bid-to-stop-offering-basic-phone-service-in-california/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T19:20:49+00:00",
    "summary": "AT&#038;T suffers setback but will keep asking court and FCC to preempt state rules."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/07/our-playstation-price-analysis-shows-why-physical-games-still-matter/",
    "domain": "大厂 AI 动态",
    "title": "RIP bargain bin: The price impact of Sony's disc-free PlayStation plan",
    "url": "https://arstechnica.com/gaming/2026/07/our-playstation-price-analysis-shows-why-physical-games-still-matter/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T18:06:05+00:00",
    "summary": "Used discs are often cheaper than even deep digital discounts."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/07/f1-in-belgium-the-2026-cars-look-pathetic-on-all-the-best-racetracks/",
    "domain": "大厂 AI 动态",
    "title": "F1 in Belgium: Machine learning algorithms are ruining the sport",
    "url": "https://arstechnica.com/cars/2026/07/f1-in-belgium-the-2026-cars-look-pathetic-on-all-the-best-racetracks/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T15:59:18+00:00",
    "summary": "Many will say Spa is the best racetrack on earth, but not for these F1 cars."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/aliexpress-fined-625m-for-failing-to-remove-unsafe-toys-dangerous-cosmetics/",
    "domain": "大厂 AI 动态",
    "title": "AliExpress hit with record $625M fine after failing to make EU-ordered fixes",
    "url": "https://arstechnica.com/tech-policy/2026/07/aliexpress-fined-625m-for-failing-to-remove-unsafe-toys-dangerous-cosmetics/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T15:32:45+00:00",
    "summary": "Online retailer AliExpress says it's shocked by largest DSA fine yet."
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
    "id": "hn:48678873",
    "domain": "股票",
    "title": "OpenAI leans toward waiting until next year for IPO",
    "url": "https://www.nytimes.com/2026/06/25/technology/openai-ipo-artificial-intelligence.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 179,
    "published_at": "2026-06-25T20:36:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48974426",
    "domain": "股票",
    "title": "Big tech needs to justify AI spending as investors dump stocks",
    "url": "https://www.bloomberg.com/news/articles/2026-07-19/big-tech-needs-to-justify-ai-spending-as-investors-dump-stocks",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 44,
    "published_at": "2026-07-20T04:41:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48950580",
    "domain": "股票",
    "title": "SpaceX stock drops to a new low and loses $1T in value in a month",
    "url": "https://www.businessinsider.com/spacex-stock-drops-new-low-ipo-price-starship-launch-scrubbed-2026-7",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 73,
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
    "points": 37,
    "published_at": "2026-07-20T19:52:49+00:00",
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
    "id": "hn:48967807",
    "domain": "股票",
    "title": "Claude Code skill for searching royalty-free stock photos via the Pexels API",
    "url": "https://github.com/amalshehu/pexels-skill",
    "source": "amalshehu",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-19T12:55:11+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3776897",
    "domain": "股票",
    "title": "磁悬浮离心压缩机：液冷时代的“动力心脏”，产业规模有望迎来3倍增长？",
    "url": "https://wallstreetcn.com/premium/articles/3776897?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T05:47:38+00:00",
    "summary": "磁悬浮离心压缩机正从传统工业制冷领域跃升为AI数据中心液冷系统的“动力心脏”，2025-2030年全球市场规模预计从87.4亿美元增长至215亿美元，CAGR达19.7%。"
  },
  {
    "id": "wscn:3777531",
    "domain": "股票",
    "title": "AI将转向“按结果付费”？OpenAI董事长预言一年内Token付费模式将颠覆",
    "url": "https://wallstreetcn.com/articles/3777531",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T05:45:51+00:00",
    "summary": "企业深陷AI成本焦虑？OpenAI董事长断言：Token计费将在一年内终结！未来行业将告别“算Token”，全面迈向“按业务结果付费”的新商业模式。同时，他对Kimi等低成本模型的真实性价比持审慎态度，AI投资回报正迎来变革拐点。"
  },
  {
    "id": "wscn:3777530",
    "domain": "股票",
    "title": "英伟达的「地下」战役：百亿美元暗光纤为何是比芯片更深的护城河",
    "url": "https://wallstreetcn.com/articles/3777530",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T05:43:56+00:00",
    "summary": "英伟达正秘密斥资50至100亿美元，在全美收购从未激活的暗光纤，自建总带宽达7.6 Petabits/秒的电信级网络。这不是一次简单的基础设施投资——当博通、Marvell的定制芯片持续蚕食GPU份额，英伟达选择将战场从\"谁的芯片更快\"延伸至\"谁能把算力直接送到客户手里\"。"
  },
  {
    "id": "wscn:3777518",
    "domain": "股票",
    "title": "全球科技股反弹！韩股涨幅扩大至4%、三星电子涨6%，油价回落、金价上涨1%",
    "url": "https://wallstreetcn.com/articles/3777518",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T05:08:15+00:00",
    "summary": "亚太股市周二四日来首度反弹，韩国综合指数涨幅扩大至4%，韩国交易所更因涨势过猛启动Sidecar机制，暂停KOSPI程序化买盘。芯片股领涨，三星电子涨6%，日经225指数涨超2%，铠侠涨超10%，纳斯达克100指数期货亦小幅上涨。油价回落缓解通胀压力，但市场真正的考验在于本周开启的科技巨头财报季。"
  },
  {
    "id": "wscn:3776757",
    "domain": "股票",
    "title": "大模型7月激战：国产性能快速攀升，海外巨头开启价格战",
    "url": "https://wallstreetcn.com/premium/articles/3776757?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:29:27+00:00",
    "summary": "全球AI大模型正从“百模大战”的混沌期迈入“诸侯混战”的格局重塑期，能力代差快速收窄、资本开支持续膨胀、开源生态加速全球化。"
  },
  {
    "id": "wscn:3777529",
    "domain": "股票",
    "title": "中信银行总行多条线换将，零售金融部总经理或由副行长兼任",
    "url": "https://wallstreetcn.com/articles/3777529",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:13:42+00:00",
    "summary": "中信银行近期在总行层面启动了涉及零售、对公、风控等多条线人事调整。\n7月20日，据有关媒体报道，中信..."
  },
  {
    "id": "wscn:3777521",
    "domain": "股票",
    "title": "大反转！创业板爆涨超5%，芯片半导体爆发、半导体设备掀涨停潮，恒科指涨近2%，智谱飙涨超25%",
    "url": "https://wallstreetcn.com/articles/3777521",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:02:46+00:00",
    "summary": "盘面上，个股涨跌互现，全市场超2800只个股下跌。量能明显放大，上午半天成交2.01万亿。沪深两市半日成交额2万亿，较上个交易日放量超3300亿。板块方面，半导体、算力硬件产业链探底回升，存储器、CPO方向领涨；锂电池、能源金属、人形机器人、商业航天题材涨幅居前；电力、医药、油气、金融、白酒板块调整。"
  },
  {
    "id": "wscn:3777523",
    "domain": "股票",
    "title": "摩根大通CEO戴蒙警告：市场低估“地缘+财政”双重风险，不会在这个价位买股票或长期美债",
    "url": "https://wallstreetcn.com/articles/3777523",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T03:59:46+00:00",
    "summary": "摩根大通CEO戴蒙罕见亮出底牌：不买股票、不碰长期美债。他警告，市场严重低估了乌克兰战争、中东冲突及财政赤字失控带来的双重风险，“债券义警”终将反扑推高利率。对AI热潮，他以互联网泡沫为鉴——赢家会出现，但绝非按你想象的剧本。"
  },
  {
    "id": "wscn:3777430",
    "domain": "股票",
    "title": "从杠杆ETF到韩元自由兑换：韩国为何如此豪赌？",
    "url": "https://wallstreetcn.com/premium/articles/3777430?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T03:49:23+00:00",
    "summary": "韩国在韩元新低与股市急跌时推进韩元自由兑换，旨在引入外资缓解流动性，但长期波动风险陡增。"
  },
  {
    "id": "wscn:3777527",
    "domain": "股票",
    "title": "唐晓斌：每个细分板块都值得“坚守”，但难再复刻光模块",
    "url": "https://wallstreetcn.com/articles/3777527",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T03:33:18+00:00",
    "summary": "转向AI多赛道“重仓式分散”"
  },
  {
    "id": "wscn:3777526",
    "domain": "股票",
    "title": "私募基金管理规模升至23.66万亿元，再创历史新高",
    "url": "https://wallstreetcn.com/articles/3777526",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T03:30:19+00:00",
    "summary": "管理人数量回落、区域和头部机构集中度提高"
  },
  {
    "id": "wscn:3777519",
    "domain": "股票",
    "title": "AI烧钱背后，华尔街发明了一门新生意",
    "url": "https://wallstreetcn.com/articles/3777519",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T03:04:02+00:00",
    "summary": "摩根士丹利正将AI数据中心融资打造成全新资产类别，凭借将谷歌等科技巨头信用与长期算力合同打包证券化的创新模式，今年上半年资本市场费用暴增逾六成至23亿美元，跻身全球第二。然而，随着融资链条从数据中心延伸至芯片，信用风险悄然积聚——这场10万亿美元的盛宴能否持续，终究取决于AI需求能否兑现。"
  },
  {
    "id": "wscn:3777517",
    "domain": "股票",
    "title": "美股见顶前的财务信号",
    "url": "https://wallstreetcn.com/articles/3777517",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T02:53:49+00:00",
    "summary": "华创证券复盘互联网泡沫期间WorldCom等7家典型标的发现，股价见顶前财务信号遵循清晰传导链条：OCF（先反映经营现金流动能放缓）同比最早预警（平均领先3.7个季度），FCF与EBITDA（分别确认自由现金流压力和经营盈利动能走弱）在顶部前1个季度精准确认，资本开支反而是滞后指标。"
  },
  {
    "id": "wscn:3777522",
    "domain": "股票",
    "title": "AI需求继续爆发，韩国7月前20天经工作日调整后出口增速跃升至62.9%",
    "url": "https://wallstreetcn.com/articles/3777522",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T02:52:10+00:00",
    "summary": "芯片出口是此次增长的核心引擎，同比飙升180.6%，计算机相关产品出货量增幅更接近232%，两项数据均反映出全球对AI算力硬件的旺盛需求。从出口目的地来看，7月前20天，韩国对华出口同比增长94.1%，增幅居各主要市场之首。对美出口增幅接近40%。"
  },
  {
    "id": "wscn:3777520",
    "domain": "股票",
    "title": "AI数据中心成本再添变数！监管收紧，甲骨文或需提供超70亿美元担保",
    "url": "https://wallstreetcn.com/articles/3777520",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T02:34:18+00:00",
    "summary": "甲骨文150亿美元威斯康星数据中心项目遭遇双重夹击：州监管机构拒绝豁免70亿美元信用抵押要求，每年额外成本逾1亿美元；标普同步将其评级下调至BBB-，距垃圾级仅一步之遥。这一履行3000亿美元OpenAI算力合同的关键项目，正将AI扩张的隐性成本推至台前。"
  },
  {
    "id": "wscn:3777515",
    "domain": "股票",
    "title": "流动性专家Michael Howell：全球流动性已见顶，股市最好的窗口已经过去",
    "url": "https://wallstreetcn.com/articles/3777515",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T02:02:54+00:00",
    "summary": "Michael Howell认为，追踪全球流动性动能的核心指标已于去年四季度触顶并持续减速。其65个月流动性周期模型显示，股市最佳窗口已过，市场当前处于\"投机阶段\"——大宗商品强势、收益率曲线熊市平坦化为晚周期特征。当前已非加仓风险资产良机，准备从大宗商品转向现金，最终转向长久期国债。"
  },
  {
    "id": "wscn:3777513",
    "domain": "股票",
    "title": "2028年是大限？美股科技“终局的猜想”",
    "url": "https://wallstreetcn.com/articles/3777513",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T01:44:08+00:00",
    "summary": "美股AI牛市还没熄火，但倒计时或已悄然开启。中信建投最新研究直指：纳指短期不排除从前高回撤10%以上，而2028年可能是这轮科技牛市的\"大限\"。杠杆信号偏红、中国AI模型以极低成本快速追赶、估值扩张趋于钝化……几条可能终结牛市的链条正在成形。更难定价的风险，或许是2028年大选带来的政治冲击。"
  },
  {
    "id": "wscn:3777514",
    "domain": "股票",
    "title": "祛魅、验货、重估：WAIC之后，具身智能的钱流向哪里？",
    "url": "https://wallstreetcn.com/articles/3777514",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T01:34:17+00:00",
    "summary": "这一年，智能体完成了从极客概念到产业议题的跃迁，但资本市场的心态已经变了——\"会聊天\"的故事不再稀缺..."
  },
  {
    "id": "wscn:3777510",
    "domain": "股票",
    "title": "复刻“DeepSeek时刻”？华尔街齐称：Kimi K3反而强化算力需求",
    "url": "https://wallstreetcn.com/articles/3777510",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T01:28:09+00:00",
    "summary": "Kimi K3再次触发 “DeepSeek 式” 担忧，美股半导体板块应声下挫，但多家华尔街机构认为算力需求并未走弱。这款2.8万亿参数、百万上下文长驻推理开源模型，会拉高KV 缓存、HBM、存储及云基建需求。Kimi K3更像是AI使用量扩散的催化剂，而不是硬件需求见顶信号。"
  },
  {
    "id": "wscn:3777512",
    "domain": "股票",
    "title": "Iren、Hut、Nebius全线大涨，英伟达带头砸钱，科技巨头大单涌向“AI云”",
    "url": "https://wallstreetcn.com/articles/3777512",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T00:59:49+00:00",
    "summary": "算力军备竞赛重塑云计算版图：IREN斩获28亿美元AI合同、股价暴涨19%，Hut 8签下15年价值98亿美元租约、潜在总价值逾500亿，英伟达同步披露持有Nebius逾9%股权。三重催化叠加，neocloud赛道全线爆发——科技巨头AI基础设施支出正加速溢出，独立算力运营商的黄金窗口或已打开。"
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
    "id": "hn:48634931",
    "domain": "股票",
    "title": "SpaceX Drops 14% in One Day, Price Now Below IPO Launch",
    "url": "https://finance.yahoo.com/quote/SPCX/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-06-22T19:33:55+00:00",
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
    "id": "hn:48824532",
    "domain": "股票",
    "title": "SpaceX Shares Stumble in Nasdaq-100 Debut",
    "url": "https://www.wsj.com/finance/stocks/spacex-shares-stumble-in-nasdaq-100-debut-9ec10565",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-07T22:00:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48853145",
    "domain": "股票",
    "title": "California universities stockpiling AR-15s, grenades and submachine guns",
    "url": "https://www.theguardian.com/us-news/2026/jul/09/california-universities-military-equipment",
    "source": "sizzle",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-09T22:20:12+00:00",
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
    "id": "hn:48634585",
    "domain": "金融",
    "title": "Canada plans 'nuclear renaissance' with up to 10 reactors built by 2040",
    "url": "https://www.cbc.ca/news/politics/federal-nuclear-strategy-9.7244509",
    "source": "geox",
    "platform": "hackernews",
    "points": 593,
    "published_at": "2026-06-22T19:06:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48915953",
    "domain": "金融",
    "title": "Stripe and Advent have made a joint offer to acquire PayPal – sources",
    "url": "https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/",
    "source": "rvz",
    "platform": "hackernews",
    "points": 493,
    "published_at": "2026-07-15T03:32:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48647444",
    "domain": "金融",
    "title": "Digital euro clears key hurdle as EU seeks to break free from U.S. credit cards",
    "url": "https://finance.yahoo.com/markets/currencies/articles/ecb-secures-key-parliamentary-backing-102718449.html",
    "source": "madars",
    "platform": "hackernews",
    "points": 232,
    "published_at": "2026-06-23T16:27:49+00:00",
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
    "id": "hn:48673787",
    "domain": "金融",
    "title": "Federal agents track down woman, demand she remove Instagram post about ICE",
    "url": "https://www.syracuse.com/news/2026/06/federal-agents-track-down-syracuse-woman-demand-she-remove-instagram-post-about-ice.html",
    "source": "coloneltcb",
    "platform": "hackernews",
    "points": 217,
    "published_at": "2026-06-25T14:16:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:48892638",
    "domain": "金融",
    "title": "Benchmarking 15 “E-Waste” GPUs with Modern Workloads",
    "url": "https://esologic.com/benchmarking-tesla-gpus/",
    "source": "eso_logic",
    "platform": "hackernews",
    "points": 141,
    "published_at": "2026-07-13T13:48:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48703613",
    "domain": "金融",
    "title": "Feds Killed Polestar and Spared Volvo",
    "url": "https://www.thedrive.com/news/feds-killed-polestar-and-spared-volvo-that-should-terrify-you",
    "source": "mraniki",
    "platform": "hackernews",
    "points": 175,
    "published_at": "2026-06-28T01:55:21+00:00",
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
    "id": "rss:https://arxiv.org/abs/2607.16450",
    "domain": "金融",
    "title": "Portfolio Optimization under Heavy Tails and Asymmetric Volatility: Evidence from Taiwan-Exposed ETFs",
    "url": "https://arxiv.org/abs/2607.16450",
    "source": "Ting-Jung Lee, Abootaleb Shirvani, Farzana Afroz, Svetlozar T. Rachev, Frank J. Fabozzi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.16450v1 Announce Type: new Abstract: Taiwan's central role in global semiconductor manufacturing exposes Taiwan-related ETFs to technology concentration, geopolitical uncertainty, and suppl"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.16601",
    "domain": "金融",
    "title": "The conditional higher moment risk measure: second-order asymptotics with FGM contagion",
    "url": "https://arxiv.org/abs/2607.16601",
    "source": "Haifan Hu, Bingzhen Geng, Jiajun Liu, Shijie Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.16601v1 Announce Type: new Abstract: This paper investigates second-order asymptotic expansions for the conditional higher moment (CoHM) coherent risk measure under a Farlie-Gumbel-Morgenst"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.16622",
    "domain": "金融",
    "title": "Proof-of-Stake Dynamics: The Elusive Price Anchor and Endogenous Volatility Harvesting",
    "url": "https://arxiv.org/abs/2607.16622",
    "source": "Mikhail Perepelitsa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.16622v1 Announce Type: new Abstract: In this paper, we develop an open-economy macroeconomic model of a Proof-of-Stake network to analyze nominal token-price dynamics and the systemic effec"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.16970",
    "domain": "金融",
    "title": "Herding and Liquidity in Order-Book Markets. II. Fundamental Anchoring and the Resilience of Liquidity",
    "url": "https://arxiv.org/abs/2607.16970",
    "source": "Jan Novotny",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.16970v1 Announce Type: new Abstract: An order-book market whose liquidity provision is anchored to a fundamental value carries a restoring force: the price mean-reverts to value and the boo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.17020",
    "domain": "金融",
    "title": "Risk Measures on Lipschitz Spaces",
    "url": "https://arxiv.org/abs/2607.17020",
    "source": "Henrik Karlholm, Marlon Moresco, Marcelo Righi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.17020v1 Announce Type: new Abstract: This paper develops a theory of monetary risk measures on metric state spaces. We propose the space of Lipschitz functions vanishing at a reference stat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.17073",
    "domain": "金融",
    "title": "Faithful Decoding",
    "url": "https://arxiv.org/abs/2607.17073",
    "source": "Nisha Peng, John Stachurski, Jingni Yang, Ziyue Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.17073v1 Announce Type: new Abstract: This paper studies transformations that increase efficiency in solving equilibrium systems without information loss. Our approach exploits order-theoret"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.17212",
    "domain": "金融",
    "title": "A General Model for Continuous Time Principal-Agent Problem Under Hidden Action",
    "url": "https://arxiv.org/abs/2607.17212",
    "source": "Jaeyoung Sung, Jianfeng Zhang, Zimu Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.17212v1 Announce Type: new Abstract: In this paper, we study a general continuous-time Principal-Agent (PA) problem, where the agent privately makes effort and consumption decisions over ti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.17381",
    "domain": "金融",
    "title": "Determining Insolvency Regions in Banks: A Stochastic Dynamic Approach Integrating Liquidity and Credit Risk",
    "url": "https://arxiv.org/abs/2607.17381",
    "source": "Nader Karimi, Davood Ahmadian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.17381v1 Announce Type: new Abstract: We develop a continuous-time structural dynamic model to determine the exact insolvency regions of banks arising from the non-linear interaction between"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.17428",
    "domain": "金融",
    "title": "Uniform-Loss Automated Market Making for Prediction Markets",
    "url": "https://arxiv.org/abs/2607.17428",
    "source": "Ciamac C. Moallemi, Dan Robinson, Brian Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.17428v1 Announce Type: new Abstract: Automated market makers (AMMs) for prediction markets descend from market scoring rules, where a mechanism operator subsidizes a market to aggregate bel"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.17502",
    "domain": "金融",
    "title": "Mean-field equilibrium price formation under single-default risk",
    "url": "https://arxiv.org/abs/2607.17502",
    "source": "Masashi Sekine",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.17502v1 Announce Type: new Abstract: We study equilibrium price formation in an incomplete financial market with a large population of agents, where stock prices are subject to a single-def"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.17633",
    "domain": "金融",
    "title": "Social Integration and Housing Behaviours of Immigrants: Evidence from Singapore's Public Housing Market",
    "url": "https://arxiv.org/abs/2607.17633",
    "source": "Yi Fan, Ho Pin Teo, Yong Tu, Wayne Xinwei Wan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.17633v1 Announce Type: new Abstract: This study investigates the impact of social integration on immigrants' housing behaviours from a temporal perspective, using Singapore's differential p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.17649",
    "domain": "金融",
    "title": "Ageing in which place? Spatial analytical framework for evaluating ageing-in-place practices",
    "url": "https://arxiv.org/abs/2607.17649",
    "source": "Yong Tu, Yaopei Wang, Yumeng Yang, Yi Fan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.17649v1 Announce Type: new Abstract: Over the past decade, governments around the world have made significant investments in creating elderly-friendly urban environments within local neighb"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.17827",
    "domain": "金融",
    "title": "A Gate-and-Menu Theory of Collective Tourism Brand Value",
    "url": "https://arxiv.org/abs/2607.17827",
    "source": "Johan Fourie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.17827v1 Announce Type: new Abstract: A collective tourism brand is jointly produced by assets managed by different custodians, so destination managers must decide which assets require colle"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.17991",
    "domain": "金融",
    "title": "Optimal Market Making in Prediction Markets",
    "url": "https://arxiv.org/abs/2607.17991",
    "source": "Dominik Feil, Max Nendel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.17991v1 Announce Type: new Abstract: Prediction markets are attracting growing attention as trading volumes rise and their practical relevance increases. To ensure efficient price discovery"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.18001",
    "domain": "金融",
    "title": "AlphaZeroBeta: Deep Reinforcement Learning for Market-Neutral Portfolios",
    "url": "https://arxiv.org/abs/2607.18001",
    "source": "Boris Belyakov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.18001v1 Announce Type: new Abstract: Market-neutral portfolios aim to generate consistent returns while offsetting systematic market risk. Traditional approaches based on factor models or c"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.16229",
    "domain": "金融",
    "title": "FinBench: Time-Gated Calibration and Uncertainty Benchmarking for Agentic Financial Forecasting",
    "url": "https://arxiv.org/abs/2607.16229",
    "source": "Rishab Ghosh, Vinay Devarakonda",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.16229v1 Announce Type: cross Abstract: Large language models (LLMs) are increasingly used as components of agentic systems that observe, plan, and act. In finance, even \"assistive\" systems "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.16281",
    "domain": "金融",
    "title": "A Novel Hybrid Quantum Reservoir Computing (nHQRC) for Phase Transition Detection in Non-Equilibrium Dynamical Systems",
    "url": "https://arxiv.org/abs/2607.16281",
    "source": "Manoj B. Bhatkar, Prashant M. Yawalkar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.16281v1 Announce Type: cross Abstract: The analysis of highly non-linear stochastic data within non-equilibrium dynamical systems requires computational frameworks capable of detecting late"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.16801",
    "domain": "金融",
    "title": "A Practical Guide to Simulating Correlated Binary Outcomes",
    "url": "https://arxiv.org/abs/2607.16801",
    "source": "Chi Heem Wong, Zied Ben Chaouch",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.16801v1 Announce Type: cross Abstract: Simulating dependent Bernoulli outcomes with prescribed means and pairwise Pearson correlations is a common task in risk modeling. A familiar approach"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.16935",
    "domain": "金融",
    "title": "Robust Control for Marked Point Processes under Transition-Rate Uncertainty",
    "url": "https://arxiv.org/abs/2607.16935",
    "source": "Sascha Desmettre, Philipp C. Hornung",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.16935v1 Announce Type: cross Abstract: We consider a novel robust utility maximisation problem under bounded cumulative transition rate uncertainty within the class of non-Markovian marked "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.17427",
    "domain": "金融",
    "title": "Abliteration Is Not a Scalpel: Off-Target Effects of Refusal Removal on Decision Disposition Across Model Families",
    "url": "https://arxiv.org/abs/2607.17427",
    "source": "Aleksander Fafu{\\l}a",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.17427v1 Announce Type: cross Abstract: Abliteration - deleting a model's refusal direction from its weights - is the standard recipe behind popular \"uncensored\" open-weight models. We show "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.17640",
    "domain": "金融",
    "title": "A Digital Twin-Based Method for Evaluating Local Collective Tariffs in Distribution-Level Energy Systems",
    "url": "https://arxiv.org/abs/2607.17640",
    "source": "Kristoffer Christensen, Bo N{\\o}rregaard J{\\o}rgensen, Zheng Grace Ma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.17640v1 Announce Type: cross Abstract: This work addresses the need for engineering-grounded evaluation of implement-ed tariff mechanisms in distribution-level energy systems. A digital twi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2110.13814",
    "domain": "金融",
    "title": "Bidders' Responses to Auction Format Change in Internet Display Advertising Auctions",
    "url": "https://arxiv.org/abs/2110.13814",
    "source": "Shumpei Goke, Gabriel Y. Weintraub, Ralph Mastromonaco, Sam Seljan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2110.13814v4 Announce Type: replace Abstract: We study actual bidding behavior when a new auction format gets introduced into the marketplace. More specifically, we investigate this question usi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.04371",
    "domain": "金融",
    "title": "Testing for Spillovers in Resource Conservation: Evidence from a Natural Field Experiment",
    "url": "https://arxiv.org/abs/2508.04371",
    "source": "Lorenz Goette, Zhi Hao Lim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2508.04371v3 Announce Type: replace Abstract: This paper studies whether behavioral interventions designed to promote resource conservation in one domain generate spillovers in another. Using a "
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.26568",
    "domain": "金融",
    "title": "Bidding strategies for energy storage players in 100% renewable electricity market: A game-theoretical approach",
    "url": "https://arxiv.org/abs/2509.26568",
    "source": "Arega Getaneh Abate, Dogan Keles, Salim Hassi, Xiufeng Liu, Xiao-Bing Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2509.26568v3 Announce Type: replace Abstract: Large-scale energy storage is expected to be a pivotal source of flexibility in electricity systems supplied entirely by renewable energy sources (R"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.03152",
    "domain": "金融",
    "title": "Political Shocks and Price Discovery in Prediction Markets: Evidence from the 2024 U.S. Presidential Election",
    "url": "https://arxiv.org/abs/2603.03152",
    "source": "Kwok Ping Tsang, Zichao Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2603.03152v4 Announce Type: replace Abstract: What do trading and prices each reveal when political news hits a prediction market? We answer using Polymarket's on-chain ledger around three shock"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.16997",
    "domain": "金融",
    "title": "Hedging the Singularity",
    "url": "https://arxiv.org/abs/2604.16997",
    "source": "Andrew Y. Chen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2604.16997v2 Announce Type: replace Abstract: AI stocks trade at extraordinary valuations. We develop an asset pricing model in which investors use AI stocks to hedge against an AI singularity t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.01356",
    "domain": "金融",
    "title": "A Formally Verified Library of Mathematical Finance in Lean 4",
    "url": "https://arxiv.org/abs/2606.01356",
    "source": "Raphael Coelho",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2606.01356v3 Announce Type: replace Abstract: We describe a library of mathematical finance built in the Lean~4 proof assistant, on top of Mathlib and the BrownianMotion package. It is broad: mo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.02528",
    "domain": "金融",
    "title": "Auditing Asset-Specific Preferences in Financial Large Language Models: Evidence from Bitcoin Representations and Portfolio Allocation",
    "url": "https://arxiv.org/abs/2606.02528",
    "source": "Wenbin Wu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2606.02528v3 Announce Type: replace Abstract: Large language models now power robo-advisors and trading agents, yet whether they carry built-in biases toward specific assets is largely untested."
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.02947",
    "domain": "金融",
    "title": "FOI-O: A global ontology and verification framework for Freedom of Information process modelling",
    "url": "https://arxiv.org/abs/2607.02947",
    "source": "Dylan A Mordaunt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T04:00:00+00:00",
    "summary": "arXiv:2607.02947v2 Announce Type: replace Abstract: Public official-information request records contain process signals. They can support research, workflow review, and analyst-led assessment. Yet the"
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
    "id": "hn:48653311",
    "domain": "金融",
    "title": "Prairieland defendants sentenced today to prison terms ranging from 30-100 years",
    "url": "https://prairielanddefendants.com/press-release/eight-federal-prairieland-defendants-sentenced-today-to-prison-terms-ranging-from-30-100-years-for-common-protest-activity/",
    "source": "panic",
    "platform": "hackernews",
    "points": 88,
    "published_at": "2026-06-23T23:54:00+00:00",
    "summary": ""
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
    "id": "hn:48791799",
    "domain": "金融",
    "title": "Is The Economist Always Wrong?",
    "url": "https://economist.com/interactive/finance-and-economics/2026/07/02/is-the-economist-always-wrong",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 59,
    "published_at": "2026-07-05T06:40:05+00:00",
    "summary": ""
  }
]
```
