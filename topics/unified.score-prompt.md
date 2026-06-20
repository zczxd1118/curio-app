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

- 今日日期：`2026-06-20`
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
  "date": "2026-06-20",
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
    "points": 3283064,
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
    "points": 1213391,
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
    "points": 1197784,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1w9MczyETB",
    "domain": "AI",
    "title": "【Vibe Coding】0基础项目实战教学丨Claude Code，Codex，Cursor教程",
    "url": "http://www.bilibili.com/video/av114669670898752",
    "source": "蛋黄酱拌巧克力",
    "platform": "bilibili",
    "points": 1031883,
    "published_at": "2025-06-12T12:28:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 938760,
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
    "points": 728984,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 663485,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 427521,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1rrQGBeEen",
    "domain": "AI",
    "title": "普通人真可以用Ai赚钱了",
    "url": "http://www.bilibili.com/video/av116403411688845",
    "source": "老强说",
    "platform": "bilibili",
    "points": 424521,
    "published_at": "2026-04-15T11:30:00+00:00",
    "summary": "一键三连+评论报名。我会私信发送报名方式给你。\n请不要相信任何非老强说官方号给你的私信。"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 414602,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 413331,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 373989,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 366606,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1EduzzDEMM",
    "domain": "AI",
    "title": "Vibe Coding零基础教程，智能代码生成实战与原理解析。淘汰你的不是AI是另一个会Vibe Coding的人。Vibe Coding最新教程！",
    "url": "http://www.bilibili.com/video/av114852173515955",
    "source": "芝士好猫meme",
    "platform": "bilibili",
    "points": 329744,
    "published_at": "2025-07-14T15:01:39+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 244480,
    "published_at": "2026-04-04T15:19:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 238895,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 174894,
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
    "points": 156925,
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
    "points": 155694,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 153914,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 143824,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 142832,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 137900,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1RAEz6EE98",
    "domain": "AI",
    "title": "为什么Claude Code+DeepSeekV4是最有性价比的个人AI Agent?",
    "url": "http://www.bilibili.com/video/av116732144392386",
    "source": "呱声一片",
    "platform": "bilibili",
    "points": 130041,
    "published_at": "2026-06-11T15:27:06+00:00",
    "summary": "官方文档地址：https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/claude_code"
  },
  {
    "id": "bvid:BV1KoGE6cE53",
    "domain": "AI",
    "title": "🚀Claude Code重大突破：Workflow功能完整实战教程！ultrawork召唤无数个Agent协同！自动生成JS脚本实现可复用的精准可控工作流",
    "url": "http://www.bilibili.com/video/av116629702777532",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 107665,
    "published_at": "2026-05-24T13:11:48+00:00",
    "summary": "视频简介：\n 全球首测！Anthropic未官宣的Claude Code Workflow隐藏功能完整使用指南，三大阶段六种形态精准解析！AI编程进入脚本化新纪元\n\n 本期视频详细演示了Anthropic为Claude Code V2.1.47和V2.1.48秘密新增的颠覆性Workflow功能！这个被官方从Changelog中紧急删除却未从代码中移除的&quot;隐藏神器&quot;，将成为继M"
  },
  {
    "id": "bvid:BV1j67k6oENA",
    "domain": "AI",
    "title": "Claude Ultracode 超码 上线 | 操控100个Agent并行开发  保姆级实战教程",
    "url": "http://www.bilibili.com/video/av116697163896598",
    "source": "技术胖",
    "platform": "bilibili",
    "points": 104735,
    "published_at": "2026-06-05T11:05:27+00:00",
    "summary": "Ultracode 功能太好用了，就是Claude Code昨天新出的“超码”功能，如果你Vibe Coding ，那这个技巧一定要掌握。他解决了Claude Code 一次性跑不完大型任务的问题。\n本期视频很长，但看完你的AI Coding能力将超越整个团队。并且把视频内容整理成了文字版，放在评论区，方便你学习使用。视频很干，可以先喝口水润润喉咙。"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 92987,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92169,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1HM7C6BEnF",
    "domain": "AI",
    "title": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！",
    "url": "http://www.bilibili.com/video/av116696929076767",
    "source": "AIAgent开发",
    "platform": "bilibili",
    "points": 81873,
    "published_at": "2026-06-05T10:11:18+00:00",
    "summary": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！"
  },
  {
    "id": "bvid:BV1xBrDB9E42",
    "domain": "AI",
    "title": "独立开发太累？Godot + Claude Code 搭建 AI 辅助工作流，效率直接起飞！ | 地块召唤师开发实战 #01",
    "url": "http://www.bilibili.com/video/av115911319100158",
    "source": "像素夹心饼干",
    "platform": "bilibili",
    "points": 64384,
    "published_at": "2026-01-18T03:25:00+00:00",
    "summary": "大家好，这里是饼干！🍪\n这是我的新坑——**《地块召唤师》**开发实战分享的第一期。\n很多朋友问独立开发如何提升效率？这期视频我不聊虚的，直接公开我从 0 到 1 搭建的 AI + Godot 高效工作流。\n从游戏引擎的选择，到 Claude Code、Copilot 等 AI 工具的实战配置，再到如何用“明确需求”的方法论（SMART原则+双钻模型）来驾驭 AI，让它不仅仅是写代码的工具，更成为"
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 59158,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV1WJjF67Eky",
    "domain": "AI",
    "title": "对Claude code上瘾了",
    "url": "http://www.bilibili.com/video/av116768819384530",
    "source": "小王很南",
    "platform": "bilibili",
    "points": 52279,
    "published_at": "2026-06-18T02:50:04+00:00",
    "summary": "我做的交互网站"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 52122,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1ZrXLYyEFx",
    "domain": "AI",
    "title": "自己动手写一个MCP Server，你就知道MCP怎么回事了",
    "url": "http://www.bilibili.com/video/av114183114856586",
    "source": "AI橙爆了",
    "platform": "bilibili",
    "points": 49270,
    "published_at": "2025-03-18T11:15:52+00:00",
    "summary": "视频制作不易，请一键三连！私我领取文档源码"
  },
  {
    "id": "bvid:BV1rKjG6yEh2",
    "domain": "AI",
    "title": "10分钟+300个Agent：保姆级教程学会Agent Skills！【从零开始】",
    "url": "http://www.bilibili.com/video/av116758736279146",
    "source": "Work-Fisher",
    "platform": "bilibili",
    "points": 47956,
    "published_at": "2026-06-16T10:02:41+00:00",
    "summary": "这期我从最基础的概念，一路讲到上手实操，基本上是从 0 到 1，带你完整走一遍——一个 SKILL 到底是怎么从无到有做出来的。\n国内、国外的创建工具，我也都给你捋了一遍。希望看完这期，你也能动手做出一个真正属于自己的 SKIL。"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47128,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 42162,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 38947,
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
    "points": 36313,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 32246,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29724,
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
    "points": 29333,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1EZd3BBEB5",
    "domain": "AI",
    "title": "手把手实战教学：我是如何用一个周末掌握Claude Code的",
    "url": "http://www.bilibili.com/video/av116539105739515",
    "source": "AliAbdaal",
    "platform": "bilibili",
    "points": 28748,
    "published_at": "2026-05-09T13:00:00+00:00",
    "summary": "朋友们，有个叫Claude Code的工具，过去两个月我用它做了很多事情，它真的改变了我的整个工作方式，而且我感觉到Claude Code让人与人之间的差距加速变大。。。这个视频做完我就要发给还没尝试过的亲友！\n看完这条视频，你会了解如何让AI采访你来生成AI工具点子，如何筛选高杠杆项目，如何一边制作工具一边学习AI知识和开发技术概念。你会意识到，在AI时代，你最大的资产也许就是好奇心和突破技术摩"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27370,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV1ZEJA6xEds",
    "domain": "AI",
    "title": "最新方法！国内免费无限制，使用Claude Code！",
    "url": "http://www.bilibili.com/video/av116746874848391",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 23676,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1nf42127MW",
    "domain": "AI",
    "title": "用AI Agent做一个法律咨询助手，罗老看了都直呼内行 feat.通义千问大模型&amp;阿里云百炼平台",
    "url": "http://www.bilibili.com/video/av1204786228",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 21233,
    "published_at": "2024-05-21T05:09:48+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1mfJw6uE1Y",
    "domain": "AI",
    "title": "AI Agent 别乱选！2026 AI Agent 深度横评，普通人看完不踩坑｜OpenClaw、Codex、Hermes、WorkBuddy、Claude",
    "url": "http://www.bilibili.com/video/av116747361322195",
    "source": "AI实战派Pro",
    "platform": "bilibili",
    "points": 19237,
    "published_at": "2026-06-14T07:53:12+00:00",
    "summary": "《2026 主流 AI Agent 全维度对比｜OpenClaw / Codex / Claude Cowork / WorkBuddy / Hermes 怎么选？》\n\nHi，我是Alpha，我手把手带大家用AI提升自己工作、生活效率，提升个人竞争力以及用AI赚钱！一起做AI时代的主导者，而不是在焦虑中被AI淘汰！\n关注AI 实战派，让AI替你忙起来！\n\n本期视频介绍：《AI Agent 别乱选！"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17362,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1cCVZ6NEym",
    "domain": "AI",
    "title": "这绝对是B站讲的最全最细的VibeCoding系统教程，手把手带你从环境安装到实战，包含所有干货！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116673944492771",
    "source": "峰识在大模型",
    "platform": "bilibili",
    "points": 17107,
    "published_at": "2026-06-01T08:53:14+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n本视频配套课件笔记代码/学习大纲/大模型学习路线戳这里获取→https://www.bilibili.com/opus/1195847460814061571?spm_id_from=333.1387.0.0\n另外有需要AI大模型学习路线图+必看书籍（国内外大牛著作）+入门及进阶视频教程+项目实战及源码提供+面试实战场景"
  },
  {
    "id": "bvid:BV1qBJ36yEC1",
    "domain": "AI",
    "title": "【2026最新】这绝对是b站讲的最好的Vibe Coding教程，手把手教你从安装到代码实战的保姆级教程！!少走99%弯路！",
    "url": "http://www.bilibili.com/video/av116752478377523",
    "source": "AI大模型_小奕",
    "platform": "bilibili",
    "points": 15284,
    "published_at": "2026-06-15T05:37:28+00:00",
    "summary": "本套教程从零开始讲解，手把手教学！\n无论是新手小白，还是有一定基础的小伙伴皆可学习。\n如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！"
  },
  {
    "id": "rss:https://www.eetimes.com/defense-sends-clear-signal-to-canadian-semiconductor-industry/",
    "domain": "AI 算力 / 半导体",
    "title": "Defense Sends Clear Signal to Canadian Semiconductor Industry",
    "url": "https://www.eetimes.com/defense-sends-clear-signal-to-canadian-semiconductor-industry/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T22:00:00+00:00",
    "summary": "Canada sharpens its defense and tech edge with policies to boost homegrown chip power. The post Defense Sends Clear Signal to Canadian Semiconductor Industry appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/amazon-newest-gambit-selling-ai-chips/",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon’s Newest Gambit: Selling AI Chips",
    "url": "https://www.eetimes.com/amazon-newest-gambit-selling-ai-chips/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T12:19:36+00:00",
    "summary": "The world’s largest hyperscaler wants to seize the semiconductor moment by selling AI accelerators at scale. The post Amazon’s Newest Gambit: Selling AI Chips appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/all-semiconductor-roads-lead-to-taiwan/",
    "domain": "AI 算力 / 半导体",
    "title": "All Semiconductor Roads Lead to Taiwan",
    "url": "https://www.eetimes.com/all-semiconductor-roads-lead-to-taiwan/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T07:45:00+00:00",
    "summary": "Small in size but outsized in influence, Taiwan has become a linchpin of the global semiconductor supply chain. The post All Semiconductor Roads Lead to Taiwan appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/billions-pour-into-autonomous-defense-as-ai-redefines-warfare/",
    "domain": "AI 算力 / 半导体",
    "title": "Billions Pour into Autonomous Defense as AI Redefines Warfare",
    "url": "https://www.eetimes.com/billions-pour-into-autonomous-defense-as-ai-redefines-warfare/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T19:09:37+00:00",
    "summary": "Record investment is accelerating autonomous military tech, putting edge AI and drones at the center of modern conflict. The post Billions Pour into Autonomous Defense as AI Redefines Warfare appeared"
  },
  {
    "id": "rss:https://www.eetimes.com/the-new-software-standard-for-physical-ai-insert-return-here-for-new-line-accelerating-development-and-deployment-from-months-to-days/",
    "domain": "AI 算力 / 半导体",
    "title": "The New Software Standard for Physical AI",
    "url": "https://www.eetimes.com/the-new-software-standard-for-physical-ai-insert-return-here-for-new-line-accelerating-development-and-deployment-from-months-to-days/",
    "source": "Manuel Roldan, Software Product Manager, SiMa.ai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T14:00:00+00:00",
    "summary": "Building real-time physical AI applications—such as high-performance, multimodal object tracking for autonomous systems within a constrained power envelope—is notoriously difficult. It requires coordi"
  },
  {
    "id": "rss:https://www.eetimes.com/space-industry-is-standardizing-on-risc-v/",
    "domain": "AI 算力 / 半导体",
    "title": "Space Industry Is Standardizing on RISC-V",
    "url": "https://www.eetimes.com/space-industry-is-standardizing-on-risc-v/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T12:00:00+00:00",
    "summary": "Experts at RISC-V Summit Europe outlined how open architectures are transforming computing across the space economy. The post Space Industry Is Standardizing on RISC-V appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/can-catalonia-deliver-on-its-distributed-semiconductor-network/",
    "domain": "AI 算力 / 半导体",
    "title": "Can Catalonia’s Distributed Semiconductor Network Deliver?",
    "url": "https://www.eetimes.com/can-catalonia-deliver-on-its-distributed-semiconductor-network/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T07:15:00+00:00",
    "summary": "Catalonia is unifying its fragmented tech ecosystem into a coordinated semiconductor cluster spanning photonics, packaging, AI, and chip research. The post Can Catalonia’s Distributed Semiconductor Ne"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-will-reinstate-memory-encryption-on-ryzen-9000-cpus-through-a-bios-update-in-july-tsme-is-coming-back-after-valuable-community-feedback",
    "domain": "AI 算力 / 半导体",
    "title": "AMD will reinstate memory encryption on Ryzen 9000 CPUs through a BIOS update in July — TSME is coming back after 'valuable community feedback'",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-will-reinstate-memory-encryption-on-ryzen-9000-cpus-through-a-bios-update-in-july-tsme-is-coming-back-after-valuable-community-feedback",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T21:02:49+00:00",
    "summary": "AMD says it will reinstate firmware memory encryption (TSME) on non-PRO Ryzen 9000 desktop CPUs through a BIOS update in July, following the feature's removal through an earlier firmware update."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/your-15-inch-daily-driver-is-now-usd250-off-dell-15-laptop-with-hexa-core-cpu-8gb-ram-dips-to-usd349",
    "domain": "AI 算力 / 半导体",
    "title": "Your 15-inch daily driver is now $250 off — Dell 15 laptop with hexa-core CPU, 8GB RAM dips to $349",
    "url": "https://www.tomshardware.com/laptops/your-15-inch-daily-driver-is-now-usd250-off-dell-15-laptop-with-hexa-core-cpu-8gb-ram-dips-to-usd349",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T18:00:00+00:00",
    "summary": "The Dell 15 laptop has just come down from its regular price of $599.99 to $349.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/docking-stations-hubs/the-best-thunderbolt-and-usb-c-docks-for-laptops",
    "domain": "AI 算力 / 半导体",
    "title": "The Best Thunderbolt and USB-C Docks in 2026: Up to 140W power delivery, 10 GbE, and even internal M.2 SSD slots",
    "url": "https://www.tomshardware.com/peripherals/docking-stations-hubs/the-best-thunderbolt-and-usb-c-docks-for-laptops",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T16:31:46+00:00",
    "summary": "These are the best Thunderbolt and USB-C docks for expanding your laptop's port options."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/amazon-workers-who-testified-against-ai-data-centers-say-they-were-intimidated-by-the-company-monitored-at-work-employees-face-possible-termination-for-violating-company-policy-speaking-as-representatives",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon workers who testified against AI data centers say they were intimidated by the company, monitored at work — employees face possible termination for violating company policy, speaking as represe",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/amazon-workers-who-testified-against-ai-data-centers-say-they-were-intimidated-by-the-company-monitored-at-work-employees-face-possible-termination-for-violating-company-policy-speaking-as-representatives",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T15:55:04+00:00",
    "summary": "The three Amazon workers claim that they've been intimidated during the Zoom meetings and were being monitored while at work."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/bernie-sanders-files-bill-proposing-50-percent-public-ownership-of-us-ai-firms-and-giving-out-usd1-000-dividends-vp-vance-says-trump-supports-giving-the-american-people-a-stake-in-ai-companies-prefers-pre-distribution-over-giving-away-cash",
    "domain": "AI 算力 / 半导体",
    "title": "Bernie Sanders files bill proposing 50% public ownership of US AI firms and giving out $1,000 dividends — VP Vance says Trump supports giving the American people a stake in AI companies, prefers ‘pre-",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/bernie-sanders-files-bill-proposing-50-percent-public-ownership-of-us-ai-firms-and-giving-out-usd1-000-dividends-vp-vance-says-trump-supports-giving-the-american-people-a-stake-in-ai-companies-prefers-pre-distribution-over-giving-away-cash",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T14:50:06+00:00",
    "summary": "U.S. politicians are thinking about how they can ensure that the American people can benefit from AI."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/asml-denies-us-government-report-that-its-euv-chipmaking-tool-was-shipped-to-china-says-rumors-are-inaccurate-and-damaging-to-our-reputation",
    "domain": "AI 算力 / 半导体",
    "title": "ASML denies US government report that its EUV chipmaking tool was shipped to China — says 'rumors' are 'inaccurate and damaging to our reputation'",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-denies-us-government-report-that-its-euv-chipmaking-tool-was-shipped-to-china-says-rumors-are-inaccurate-and-damaging-to-our-reputation",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T14:20:34+00:00",
    "summary": "U.S. Commerce Secretary Lutnick expresses concerns in a conversation with ASML executives that China has an EUV lithography system as ASML denies shipping such scanners to the PRC."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/epic-games-unveils-launcher-v2-in-re-attempt-to-topple-steam-says-redesigned-storefront-is-up-to-6-5x-faster-promises-player-profiles-user-reviews-universal-controller-support-and-much-more",
    "domain": "AI 算力 / 半导体",
    "title": "Epic Games unveils Launcher V2 in re-attempt to topple Steam, says redesigned storefront is up to 6.5x faster — promises player profiles, user reviews, universal controller support, and much more",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/epic-games-unveils-launcher-v2-in-re-attempt-to-topple-steam-says-redesigned-storefront-is-up-to-6-5x-faster-promises-player-profiles-user-reviews-universal-controller-support-and-much-more",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T13:57:28+00:00",
    "summary": "Epic Games has just shown off a new year-long roadmap for its launcher, promising to bring community-requested features and a faster overall platform in the next 12 months."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/imec-asml-and-tsmc-build-complementary-2d-material-transistors-at-50nm-pitch-on-a-300mm-wafer",
    "domain": "AI 算力 / 半导体",
    "title": "Post-silicon era gets closer as industry giants crack the 2D transistor scaling bottleneck with breakthrough tech — imec, ASML, and TSMC fab complementary 2D-material transistors at 50nm pitch on a 30",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/imec-asml-and-tsmc-build-complementary-2d-material-transistors-at-50nm-pitch-on-a-300mm-wafer",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T13:13:07+00:00",
    "summary": "Imec, ASML, and TSMC have integrated both n-type and p-type transistors with atomically thin 2D channels on a single 300mm wafer."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/usb/best-usb-charger-deals",
    "domain": "AI 算力 / 半导体",
    "title": "Best USB charger deals 2026 – from tiny single-port smartphone chargers to large multi-port laptop chargers, we've found the best deals",
    "url": "https://www.tomshardware.com/peripherals/usb/best-usb-charger-deals",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T12:30:00+00:00",
    "summary": "From small smart devices to laptop charging, we dug up some of the best deals on 30W single-port to 100W multi-port chargers."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/viewsonic-vx2730d-4k-27-inch-4k-dual-refresh-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "ViewSonic VX2730D-4K 27-inch 4K dual-refresh gaming monitor review: Delivering speed, color, accuracy, and pixel density",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/viewsonic-vx2730d-4k-27-inch-4k-dual-refresh-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T12:10:00+00:00",
    "summary": "ViewSonic’s VX2730D-4K is a stellar value. It’s a 27-inch 4K gaming monitor with 144 Hz, 288 Hz in FHD, Adaptive-Sync, wide gamut color and HDR. Accurate color and high performance deliver an excellen"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/intel-hires-former-sk-hynix-chief-seok-hee-lee-to-lead-intel-foundry-advanced-packaging",
    "domain": "AI 算力 / 半导体",
    "title": "Intel hires former SK hynix chief Seok-Hee Lee to lead Intel Foundry advanced packaging — company establishing section as 'focused business with dedicated leadership'",
    "url": "https://www.tomshardware.com/tech-industry/intel-hires-former-sk-hynix-chief-seok-hee-lee-to-lead-intel-foundry-advanced-packaging",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T11:58:41+00:00",
    "summary": "Intel has appointed Seok-Hee Lee, the former chief executive of memory maker SK hynix and battery maker SK On, as executive vice president of Intel Foundry."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/elon-musk-says-that-china-will-have-a-fable-5-class-ai-model-probably-q1-next-year-ceo-of-chinese-anthropic-rival-says-it-wont-take-that-long",
    "domain": "AI 算力 / 半导体",
    "title": "CEO of Chinese Anthropic rival tells Elon Musk that China will have a Fable 5-class AI model before next year — it ‘won’t take that long’ says Jie Tang in response to Musk's prediction of a Q1 target",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/elon-musk-says-that-china-will-have-a-fable-5-class-ai-model-probably-q1-next-year-ceo-of-chinese-anthropic-rival-says-it-wont-take-that-long",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T11:38:05+00:00",
    "summary": "Elon Musk estimated that Chinese AI firms would have an LLM with Mythos level capability by the first quarter of 2027. However, the CEO of Beijing-based Z.ai responded to the comment, saying that thei"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/network-switches/woot-slashes-up-to-46-percent-off-these-wd-black-sn850p-ssds-for-pc-and-ps5-1tb-for-usd189-2tb-for-usd299-and-4tb-for-usd549",
    "domain": "AI 算力 / 半导体",
    "title": "Woot slashes up to 46% off these WD Black SN850P SSDs for PC and PS5 — 1TB for $189, 2TB for $299, and 4TB for $549",
    "url": "https://www.tomshardware.com/networking/network-switches/woot-slashes-up-to-46-percent-off-these-wd-black-sn850p-ssds-for-pc-and-ps5-1tb-for-usd189-2tb-for-usd299-and-4tb-for-usd549",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T11:21:37+00:00",
    "summary": "Grab a great discount on these officially licensed PlayStation 5 SSDs at Woot. The WD Black SN850P in 1TB, 2TB, and 4TB capacities is discounted up to 46% today, or until stocks run out."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/sk-telecom-named-as-the-korean-carrier-at-the-center-of-anthropics-mythos-export-controls",
    "domain": "AI 算力 / 半导体",
    "title": "SK Telecom named as the Korean carrier at the center of Anthropic's Mythos export controls controversy — access was revoked days before White House took Mythos and Fable 5 offline for all foreign nati",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/sk-telecom-named-as-the-korean-carrier-at-the-center-of-anthropics-mythos-export-controls",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T10:54:58+00:00",
    "summary": "Wired has identified SK Telecom as the South Korean telecom company whose access to Anthropic's Claude Mythos model the White House ordered revoked over alleged ties to China."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/16-year-old-sata-ii-ssd-survives-1-petabyte-of-writes-25x-over-the-drives-tbw-rating",
    "domain": "AI 算力 / 半导体",
    "title": "16-year-old SATA II SSD survives 1 petabyte of writes — 25x more than the drive's endurance rating",
    "url": "https://www.tomshardware.com/pc-components/ssds/16-year-old-sata-ii-ssd-survives-1-petabyte-of-writes-25x-over-the-drives-tbw-rating",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T10:30:00+00:00",
    "summary": "As part of an experiment, an enthusiast has written one petabyte of data on a legacy Sandisk P4 SATA II SSD that was released 16 years ago."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/servers/tesco-uk-supermarket-chain-removes-40-000-servers-from-vmware-infrastructure-mass-exodus-continues-due-to-broadcoms-aggressive-subscription-model",
    "domain": "AI 算力 / 半导体",
    "title": "Tesco UK supermarket chain removes 40,000 servers from VMware infrastructure — mass exodus continues due to Broadcom's aggressive subscription model",
    "url": "https://www.tomshardware.com/desktops/servers/tesco-uk-supermarket-chain-removes-40-000-servers-from-vmware-infrastructure-mass-exodus-continues-due-to-broadcoms-aggressive-subscription-model",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T10:00:00+00:00",
    "summary": "Tesco UK supermarket chain moves 40,000 servers off of VMWare infrastructure — mass exodus continues thanks to Broadcom's pricing shenanigans"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-a-massive-usd1-390-on-this-rtx-5080-alienware-gaming-pc-now-just-usd3-159-enormous-discount-delivers-top-specs-for-4k-gameplay-including-a-24-core-intel-cpu-32gb-ddr5-ram-and-a-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save a massive $1,390 on this RTX 5080 Alienware gaming PC, now just $3,159 — enormous discount delivers top specs for 4K gameplay, including a 24-core Intel CPU, 32GB DDR5 RAM, and a 2TB SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-a-massive-usd1-390-on-this-rtx-5080-alienware-gaming-pc-now-just-usd3-159-enormous-discount-delivers-top-specs-for-4k-gameplay-including-a-24-core-intel-cpu-32gb-ddr5-ram-and-a-2tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T09:53:09+00:00",
    "summary": "Don't miss this incredible deal on a high-end Alienware gaming PC with an RTX 5080, 24-core Intel Core Ultra 9 285K, 32GB of fast DDR5 RAM, and a 2TB SSD, all with a whopping $1,390 saving that brings"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/us-energy-regulator-to-order-grid-operators-to-expedite-ai-data-center-applications-says-projects-should-bring-their-own-power-or-cut-usage-during-high-demand",
    "domain": "AI 算力 / 半导体",
    "title": "US energy regulator to order grid operators to expedite AI data center applications — says projects should bring their own power or cut usage during high demand",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/us-energy-regulator-to-order-grid-operators-to-expedite-ai-data-center-applications-says-projects-should-bring-their-own-power-or-cut-usage-during-high-demand",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T09:45:00+00:00",
    "summary": "The FERC says that it will order grid operators to fast-track AI data center connections that generate their own power or reduce demand during peak hours. It demands that these changes must be enacted"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/scammers-in-china-sell-usd222-rtx-4090-with-fake-gpu-die-made-out-of-plastic-instead-of-real-silicon-marked-with-2030-production-dates-the-card-didnt-even-have-working-vram",
    "domain": "AI 算力 / 半导体",
    "title": "Scammers in China sell $222 RTX 4090 with fake GPU die made out of plastic instead of real silicon — marked with 2030 production dates, the card didn't even have working VRAM",
    "url": "https://www.tomshardware.com/pc-components/gpus/scammers-in-china-sell-usd222-rtx-4090-with-fake-gpu-die-made-out-of-plastic-instead-of-real-silicon-marked-with-2030-production-dates-the-card-didnt-even-have-working-vram",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T09:29:20+00:00",
    "summary": "Nvidia dupes keep getting more sophisticated as time goes on, with the latest example using a plastic die instead of real silicon on an RTX 4090."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/upgrade-to-the-200-hz-quantum-dot-experience-for-usd179-grab-the-27-inch-gigabyte-m27q2-qhd-gaming-monitor-before-its-gone",
    "domain": "AI 算力 / 半导体",
    "title": "Upgrade to the 200 Hz quantum dot experience for $179 — grab the 27-inch Gigabyte M27Q2 QHD gaming monitor before it's gone",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/upgrade-to-the-200-hz-quantum-dot-experience-for-usd179-grab-the-27-inch-gigabyte-m27q2-qhd-gaming-monitor-before-its-gone",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T16:00:00+00:00",
    "summary": "For a limited time, you can save up to $100 off on the Gigabyte M27Q2 27-inch 200 Hz gaming monitor on Newegg."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/usb/best-usb-chargers",
    "domain": "AI 算力 / 半导体",
    "title": "Best USB Chargers 2026: Our tested phone and laptop charger picks, from compact GaN to budget charging bliss",
    "url": "https://www.tomshardware.com/peripherals/usb/best-usb-chargers",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T15:15:14+00:00",
    "summary": "We tested 20 laptop and phone chargers, ranging from cheap no-name 15W options to 140W beasts. Find out what stood out as the best."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/msis-new-claw-8-ex-ai-handheld-with-an-intel-arc-g3-extreme-and-32gb-of-ram-costs-usd1-799-company-says-itll-be-a-tough-year-with-chances-of-another-price-hike",
    "domain": "AI 算力 / 半导体",
    "title": "MSI's new Claw 8 EX AI+ handheld with an Intel Arc G3 Extreme and 32GB of RAM costs $1,799 — company says it'll be 'a tough year' with chances of 'another price hike'",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/msis-new-claw-8-ex-ai-handheld-with-an-intel-arc-g3-extreme-and-32gb-of-ram-costs-usd1-799-company-says-itll-be-a-tough-year-with-chances-of-another-price-hike",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T14:24:28+00:00",
    "summary": "MSI's new Arc G3 Extreme-based handheld costs nearly $2,000 but the company is rather apologetic about it, even if it's warning that the price may rise in the future."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ditching-the-cloud-for-local-ai-how-i-use-two-mini-pcs-to-process-millions-of-tokens-a-day-and-save-money-on-costly-api-fees",
    "domain": "AI 算力 / 半导体",
    "title": "Ditching the cloud for local AI — how I use two mini PCs to process millions of tokens a day and save money on costly API fees",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ditching-the-cloud-for-local-ai-how-i-use-two-mini-pcs-to-process-millions-of-tokens-a-day-and-save-money-on-costly-api-fees",
    "source": "Chris Stokel-Walker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T13:10:35+00:00",
    "summary": "As new data center buildouts hit planning walls and AI inference providers hike costs, is the future of AI to roll your own models?"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/noctua-nl-lc1-36-review",
    "domain": "AI 算力 / 半导体",
    "title": "Noctua NL-LC1-36 Review: Compromise paves the way",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/noctua-nl-lc1-36-review",
    "source": "Niels Broekhuijsen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T13:10:00+00:00",
    "summary": "We test Noctua’s first attempt at an all-in-one liquid cooler, focusing specifically on pump performance to determine whether Noctua’s AIO is truly a viable alternative to swapping the fans on another"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/retro-pirate-gets-two-year-suspended-jail-sentence-for-being-stuck-in-the-past-burning-and-selling-remix-cds-of-famous-artists-four-year-investigation-into-copyright-infringement-on-40-year-old-medium-began-in-2018",
    "domain": "AI 算力 / 半导体",
    "title": "Retro pirate gets two-year suspended jail sentence for being stuck in the past, burning and selling remix CDs of famous artists — four-year investigation into copyright infringement on 40-year-old med",
    "url": "https://www.tomshardware.com/pc-components/storage/retro-pirate-gets-two-year-suspended-jail-sentence-for-being-stuck-in-the-past-burning-and-selling-remix-cds-of-famous-artists-four-year-investigation-into-copyright-infringement-on-40-year-old-medium-began-in-2018",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T12:29:36+00:00",
    "summary": "A UK man has been sentenced after pleading guilty to the unauthorized mixing and selling of music CDs, and thus breaking copyright laws. It is 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/cyberpowerpc-gaming-desktop-gxi3800bstv2-review",
    "domain": "AI 算力 / 半导体",
    "title": "CyberPowerPC Gaming Desktop (GXi3800BSTV2) review: A showpiece with real muscle",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/cyberpowerpc-gaming-desktop-gxi3800bstv2-review",
    "source": "Charles Jefferies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T12:10:00+00:00",
    "summary": "Built to be shown off, CyberPower’s latest gaming desktop expertly combines style and speed while keeping the price reasonable."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/bambu-lab-launches-pla-pure-filament-new-material-boasts-kid-safe-toy-certifications-and-asbestos-free-talc",
    "domain": "AI 算力 / 半导体",
    "title": "Bambu Lab launches PLA Pure filament — New material boasts kid-safe toy certifications and \"asbestos-free\" talc",
    "url": "https://www.tomshardware.com/3d-printing/bambu-lab-launches-pla-pure-filament-new-material-boasts-kid-safe-toy-certifications-and-asbestos-free-talc",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T12:00:00+00:00",
    "summary": "A new “pure” PLA from Bambu Lab isn’t what you think it is."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/vpn/save-a-whopping-85-percent-on-a-two-year-surfshark-vpn-subscription-for-your-home-or-office-and-grab-three-extra-months-free-huge-usd436-discount-on-full-privacy-suite-with-antivirus-protection-ad-blocking-and-unlimited-simultaneous-connections-for-just-usd75",
    "domain": "AI 算力 / 半导体",
    "title": "Save a huge 85% on a two-year Surfshark VPN subscription for your home or office and grab three extra months free — huge $436 discount on full privacy suite with antivirus protection, ad blocking and ",
    "url": "https://www.tomshardware.com/software/vpn/save-a-whopping-85-percent-on-a-two-year-surfshark-vpn-subscription-for-your-home-or-office-and-grab-three-extra-months-free-huge-usd436-discount-on-full-privacy-suite-with-antivirus-protection-ad-blocking-and-unlimited-simultaneous-connections-for-just-usd75",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T11:54:16+00:00",
    "summary": "This Surfshark One 2-year VPN deal is now just $75.33, giving you a huge $436.32 saving compared to a standard monthly subscription, with three months extra thrown in for free to keep you protected on"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/network-switches/save-a-whopping-62-percent-on-this-8-port-multi-gigabit-2-5g-ethernet-switch-in-amazons-early-prime-day-sale-upgrade-your-home-network-for-just-usd49",
    "domain": "AI 算力 / 半导体",
    "title": "Save a whopping 62% on this 8-port multi-Gigabit 2.5G Ethernet switch in Amazon's Early Prime Day sale — upgrade your home network for just $49",
    "url": "https://www.tomshardware.com/networking/network-switches/save-a-whopping-62-percent-on-this-8-port-multi-gigabit-2-5g-ethernet-switch-in-amazons-early-prime-day-sale-upgrade-your-home-network-for-just-usd49",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T11:46:08+00:00",
    "summary": "Add more ports to your network setup with this unmanaged multi-Gigabit switch for just $49."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/apple-ceo-tim-cook-warns-ai-driven-price-increases-are-unavoidable-says-company-is-trying-its-best-but-the-situation-has-become-unsustainable",
    "domain": "AI 算力 / 半导体",
    "title": "Apple CEO Tim Cook warns AI-driven price increases are unavoidable — says company is trying its best but 'the situation has become unsustainable'",
    "url": "https://www.tomshardware.com/laptops/apple-ceo-tim-cook-warns-ai-driven-price-increases-are-unavoidable-says-company-is-trying-its-best-but-the-situation-has-become-unsustainable",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T11:45:06+00:00",
    "summary": "Apple's Tim Cook says that Apple can no longer 'shield' its customers from increased prices of DRAM and NAND memory."
  },
  {
    "id": "rss:https://www.eetimes.com/canadian-researchers-reduce-quantum-atmospheric-turbulence/",
    "domain": "AI 算力 / 半导体",
    "title": "Canadian Researchers Reduce Quantum Atmospheric Turbulence",
    "url": "https://www.eetimes.com/canadian-researchers-reduce-quantum-atmospheric-turbulence/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T19:00:00+00:00",
    "summary": "uOttawa cracks quantum turbulence, making ultra-secure communication cheaper. The post Canadian Researchers Reduce Quantum Atmospheric Turbulence appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/reliable-machine-vision-starts-at-the-circuit-level/",
    "domain": "AI 算力 / 半导体",
    "title": "Reliable Machine Vision Starts at the Circuit Level",
    "url": "https://www.eetimes.com/reliable-machine-vision-starts-at-the-circuit-level/",
    "source": "YAGEO Group, Simon Reuning",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T18:01:28+00:00",
    "summary": "Machine vision has become a critical quality gate in modern industrial automation, helping manufacturers inspect products, guide robots, verify assemblies, and reduce production errors. However, relia"
  },
  {
    "id": "rss:https://www.eetimes.com/the-first-time-right-revolution/",
    "domain": "AI 算力 / 半导体",
    "title": "The First-Time-Right Revolution",
    "url": "https://www.eetimes.com/the-first-time-right-revolution/",
    "source": "Atanas Dikov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T17:42:45+00:00",
    "summary": "This paper provides an over view of the Melexis solutions for Zero latency high precision motor control and end of shaft position and torque sensing. A family of magnetic and inductive products for ev"
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
    "id": "rss:https://semianalysis.com/2025/08/13/gpt-5-ad-monetization-and-the-superapp/",
    "domain": "AI 算力 / 半导体",
    "title": "GPT-5 Set the Stage for Ad Monetization and the SuperApp",
    "url": "https://semianalysis.com/2025/08/13/gpt-5-ad-monetization-and-the-superapp/",
    "source": "Doug OLaughlin",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-13T00:27:14+00:00",
    "summary": "To many power users (Pro and Plus), GPT5 was a disappointing release. But with closer inspection, the real release is focused on the vast majority of ChatGPT’s users, which is the 700m+ free userbase "
  },
  {
    "id": "rss:https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/",
    "domain": "AI 算力 / 半导体",
    "title": "Scaling the Memory Wall: The Rise and Roadmap of HBM",
    "url": "https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-08-12T01:16:06+00:00",
    "summary": "The first portion of this report will explain HBM, the manufacturing process, dynamics between vendors, KVCache offload, disaggregated prefill decode, and wide / high-rank EP. The rest of the report w"
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/30/robotics-levels-of-autonomy/",
    "domain": "AI 算力 / 半导体",
    "title": "Robotics Levels of Autonomy",
    "url": "https://semianalysis.com/2025/07/30/robotics-levels-of-autonomy/",
    "source": "Reyk Knuhtsen",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-30T17:02:25+00:00",
    "summary": "Robots have powered manufacturing for decades, yet they stayed single-purpose and thrived only in perfect settings. Previous attempts at intelligent machines overpromised and underdelivered. But they "
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/21/vlsi2025/",
    "domain": "AI 算力 / 半导体",
    "title": "Intel 18A Details & Cost, Future of DRAM 4F2 vs 3D, Backside Power Adoption (or Not), China’s FlipFET, Digital Twins from Atoms to Fabs, and More",
    "url": "https://semianalysis.com/2025/07/21/vlsi2025/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-21T14:23:37+00:00",
    "summary": "Long time readers will recall that SemiAnalysis covers more than just datacenters and AMD. Today we’re back to semiconductors with a tech-focused roundup of the best from this year’s VLSI conference, "
  },
  {
    "id": "rss:https://semianalysis.com/2025/07/11/meta-superintelligence-leadership-compute-talent-and-data/",
    "domain": "AI 算力 / 半导体",
    "title": "Meta Superintelligence – Leadership Compute, Talent, and Data",
    "url": "https://semianalysis.com/2025/07/11/meta-superintelligence-leadership-compute-talent-and-data/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-11T20:12:19+00:00",
    "summary": "Meta’s shocking purchase of 49% of Scale AI at a ~$30B valuation shows that money is of no concern for the $100B annual cashflow ad machine. Despite seemingly unlimited resources, Meta has been fallin"
  },
  {
    "id": "rss:https://www.theverge.com/tech/952855/switchbot-standing-circulator-fan-review",
    "domain": "大厂 AI 动态",
    "title": "SwitchBot’s Standing Circulator Fan is worth fighting for",
    "url": "https://www.theverge.com/tech/952855/switchbot-standing-circulator-fan-review",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T07:00:00+00:00",
    "summary": "I can't remember the last time I got excited about a fan. Normally, I just buy whatever Vornado or Dreo model fits my budget, but that was before I started testing the battery-powered Standing Circula"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/953066/nothing-cmf-phone-delayed-ram-prices",
    "domain": "大厂 AI 动态",
    "title": "Nothing cancels this year&#8217;s CMF phone due to RAM prices",
    "url": "https://www.theverge.com/gadgets/953066/nothing-cmf-phone-delayed-ram-prices",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T21:28:39+00:00",
    "summary": "Nothing's next budget phone is the latest victim of RAMageddon. As 9to5Google reports, Nothing co-founder Akis Evangelidis announced in a post on X that a follow-up to the CMF Phone 2 Pro won't be com"
  },
  {
    "id": "rss:https://www.theverge.com/science/952988/nasa-relativity-space-eric-schmidt-mars",
    "domain": "大厂 AI 动态",
    "title": "NASA selects Eric Schmidt&#8217;s rocket company for a 2028 mission to Mars",
    "url": "https://www.theverge.com/science/952988/nasa-relativity-space-eric-schmidt-mars",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T18:41:48+00:00",
    "summary": "Relativity Space, the rocket company led by former Google executive Eric Schmidt, was picked to launch NASA's Aeolus payload to Mars in 2028, as reported earlier by TechCrunch. Under a new public-priv"
  },
  {
    "id": "rss:https://www.theverge.com/tech/952953/phillips-hue-wired-wall-module-play-lamp-candle-bulb",
    "domain": "大厂 AI 动态",
    "title": "Hue’s wired wall modules bring non-smart lights into its ecosystem",
    "url": "https://www.theverge.com/tech/952953/phillips-hue-wired-wall-module-play-lamp-candle-bulb",
    "source": "Jennifer Pattison Tuohy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T17:24:45+00:00",
    "summary": "Smart lighting company Philips Hue has launched its first wired wall modules. Installed behind existing wall switches, the new devices bring non-smart lights into the Hue ecosystem for the first time."
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/952910/nts-radio-player-atonemo-music-streaming",
    "domain": "大厂 AI 动态",
    "title": "The NTS Radio Player brings the best of internet radio to your hi-fi",
    "url": "https://www.theverge.com/entertainment/952910/nts-radio-player-atonemo-music-streaming",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T14:53:53+00:00",
    "summary": "NTS Radio and Swedish audio company Atonemo have teamed up on a dedicated player that brings NTS's genre-defying mixes and streaming stations to almost any stereo or speaker setup. And, like Atonemo's"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/952906/sam-altman-film-artificial-openai-amazon-mgm-dropped",
    "domain": "大厂 AI 动态",
    "title": "The film about Sam Altman has been dropped by Amazon MGM",
    "url": "https://www.theverge.com/ai-artificial-intelligence/952906/sam-altman-film-artificial-openai-amazon-mgm-dropped",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T14:15:29+00:00",
    "summary": "Luca Guadagnino's film about OpenAI CEO Sam Altman, Artificial, has reportedly been dropped by Amazon MGM. The film, which stars Andrew Garfield and covers the rollercoaster five days in 2023 spanning"
  },
  {
    "id": "rss:https://www.theverge.com/column/952744/optimizer-sunscreen-bemotrizinol-fda-health",
    "domain": "大厂 AI 动态",
    "title": "Our long national sunscreen nightmare is almost over",
    "url": "https://www.theverge.com/column/952744/optimizer-sunscreen-bemotrizinol-fda-health",
    "source": "Victoria Song",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T14:00:00+00:00",
    "summary": "This is Optimizer, a weekly newsletter sent from Verge senior reviewer Victoria Song that dissects and discusses the latest gizmos and potions that swear they're going to change your life. Opt in for "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/952274/t1-phone-pr-firm-not-assisting-trump-mobile-any-further",
    "domain": "大厂 AI 动态",
    "title": "T1 Phone PR firm is &#8216;not assisting Trump Mobile any further&#8217;",
    "url": "https://www.theverge.com/gadgets/952274/t1-phone-pr-firm-not-assisting-trump-mobile-any-further",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T13:00:00+00:00",
    "summary": "Where's the Trump phone? We're going to keep talking about it every week. We don't have the phones we preordered yet, but this week we received unexpected news from Trump Mobile's media relations mana"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/951638/sugar-season-2-colin-farrell-interview-apple-tv",
    "domain": "大厂 AI 动态",
    "title": "In season 2 of Sugar, Colin Farrell’s quirky detective becomes much more human",
    "url": "https://www.theverge.com/entertainment/951638/sugar-season-2-colin-farrell-interview-apple-tv",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T12:00:00+00:00",
    "summary": "When Colin Farrell was doing press for the first season of the detective series Sugar, he had to be very careful with how he spoke. Sugar is a story about a quirky private detective, but it's also sec"
  },
  {
    "id": "rss:https://www.theverge.com/tech/951718/kaleidescape-strato-e-review",
    "domain": "大厂 AI 动态",
    "title": "Kaleidescape’s movie player blows streaming, and your wallet, away",
    "url": "https://www.theverge.com/tech/951718/kaleidescape-strato-e-review",
    "source": "John.Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T12:00:00+00:00",
    "summary": "We've lost something in the past 15 years. Netflix, Amazon, Disney, Apple; they've all convinced us that streaming is the best way to watch movies and shows at home. With everything at our fingertips,"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/19/he-made-your-free-video-player-run-smoothly-now-hes-doing-that-for-robots/",
    "domain": "大厂 AI 动态",
    "title": "He made your free video player run smoothly. Now he’s doing that for robots.",
    "url": "https://techcrunch.com/2026/06/19/he-made-your-free-video-player-run-smoothly-now-hes-doing-that-for-robots/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T00:47:44+00:00",
    "summary": "French serial entrepreneur and open-source legend Jean-Baptiste Kempf has been building Kyber, an infrastructure layer to control remote devices in real time."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/19/encryption-spyware-and-now-mythos-history-shows-why-cyber-export-control-doesnt-work/",
    "domain": "大厂 AI 动态",
    "title": "From PGP to Mythos: a brief history of export controls that didn’t stop anyone",
    "url": "https://techcrunch.com/2026/06/19/encryption-spyware-and-now-mythos-history-shows-why-cyber-export-control-doesnt-work/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T22:40:14+00:00",
    "summary": "For the last 30 years, stopping the flow of cybersecurity-related software has proven to be ineffective. It's unclear why it would work now with Anthropic’s cybersecurity model Mythos."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/19/go-eyes-robotaxis-and-acquisitions-after-japans-biggest-ipo-of-2026-heres-why-it-matters/",
    "domain": "大厂 AI 动态",
    "title": "Go eyes robotaxis and acquisitions after Japan’s biggest IPO of 2026. Here’s why it matters",
    "url": "https://techcrunch.com/2026/06/19/go-eyes-robotaxis-and-acquisitions-after-japans-biggest-ipo-of-2026-heres-why-it-matters/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T21:45:00+00:00",
    "summary": "Go&#8217;s IPO — Japan&#8217;s biggest so far this year — has done more than provide a much-needed boost to the country&#8217;s languishing listing season. It has also supplied the taxi-hailing app wi"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/19/auras-impressive-e-ink-photo-frame-doesnt-even-look-digital/",
    "domain": "大厂 AI 动态",
    "title": "Aura’s impressive e-ink photo frame doesn’t even look digital",
    "url": "https://techcrunch.com/2026/06/19/auras-impressive-e-ink-photo-frame-doesnt-even-look-digital/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T21:00:34+00:00",
    "summary": "What&#8217;s the most cliche possible gift you can give a relative? A digital photo frame, displaying a rotating slideshow of family photos. Now Aura has completely refreshed this product space with i"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/19/every-fusion-startup-that-has-raised-over-100m/",
    "domain": "大厂 AI 动态",
    "title": "Every fusion startup that has raised over $100M",
    "url": "https://techcrunch.com/2026/06/19/every-fusion-startup-that-has-raised-over-100m/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T16:50:58+00:00",
    "summary": "Fusion startups have raised $7.1 billion to date, with the majority of it going to a handful of companies."
  },
  {
    "id": "rss:https://techcrunch.com/video/is-the-us-governments-anthropic-ban-accidentally-helping-the-brand/",
    "domain": "大厂 AI 动态",
    "title": "Is the US government’s Anthropic ban accidentally helping the brand?",
    "url": "https://techcrunch.com/video/is-the-us-governments-anthropic-ban-accidentally-helping-the-brand/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T16:08:17+00:00",
    "summary": "Just as last week&#160;was ending,&#160;the US government&#160;forced Anthropic to pull its two newest models, Fable 5 and Mythos 5, citing national security concerns after Amazon researchers allegedl"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/19/billionaire-ambani-wants-ai-in-every-call-app-and-home/",
    "domain": "大厂 AI 动态",
    "title": "Billionaire Ambani wants AI in every call, app, and home",
    "url": "https://techcrunch.com/2026/06/19/billionaire-ambani-wants-ai-in-every-call-app-and-home/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T15:23:28+00:00",
    "summary": "Reliance is weaving AI into telecom services used by more than 500 million people."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/19/the-ceo-of-allbirds-new-ai-biz-has-a-plan-but-no-employees/",
    "domain": "大厂 AI 动态",
    "title": "The CEO of Allbirds’ new AI biz has a plan, but no team",
    "url": "https://techcrunch.com/2026/06/19/the-ceo-of-allbirds-new-ai-biz-has-a-plan-but-no-employees/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T13:00:00+00:00",
    "summary": "Call it a startup with a sole founder and a very large seed round, but what's next is less clear."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/19/the-us-says-asmls-top-chip-tool-may-be-in-china-asml-says-it-isnt/",
    "domain": "大厂 AI 动态",
    "title": "The US says ASML’s top chip tool may be in China, but how?",
    "url": "https://techcrunch.com/2026/06/19/the-us-says-asmls-top-chip-tool-may-be-in-china-asml-says-it-isnt/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T07:59:12+00:00",
    "summary": "There's a commercial logic that cuts against the idea that ASML would risk its export license to arm a Chinese customer."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/telegram-ban-in-india-sparks-a-rush-to-vpns-rival-apps/",
    "domain": "大厂 AI 动态",
    "title": "Telegram ban in India sparks a rush to VPNs, rival apps",
    "url": "https://techcrunch.com/2026/06/18/telegram-ban-in-india-sparks-a-rush-to-vpns-rival-apps/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T01:01:00+00:00",
    "summary": "Telegram argues India should block specific content, not an entire platform used by millions."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/source-elastic-agrees-to-buy-crv-backed-deductiveai-for-up-to-85m/",
    "domain": "大厂 AI 动态",
    "title": "Source: Elastic agrees to buy CRV-backed Deductive AI for up to $85M",
    "url": "https://techcrunch.com/2026/06/18/source-elastic-agrees-to-buy-crv-backed-deductiveai-for-up-to-85m/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T00:51:11+00:00",
    "summary": "Deductive AI, a startup that uses AI to catch and resolve bugs in software, was founded just three years ago."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/ai-inference-startup-baseten-reportedly-raising-1-5b-months-after-its-last-mega-round/",
    "domain": "大厂 AI 动态",
    "title": "AI inference startup Baseten reportedly raising $1.5B months after its last mega-round",
    "url": "https://techcrunch.com/2026/06/18/ai-inference-startup-baseten-reportedly-raising-1-5b-months-after-its-last-mega-round/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T21:20:13+00:00",
    "summary": "Startup Baseten is reportedly close to finalizing a $1.5 billion round at a $13 billion as the “inference gold rush\" marches on."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/snap-spins-off-ai-video-team-into-new-company-dotmo-due-to-costs/",
    "domain": "大厂 AI 动态",
    "title": "Snap spins off AI video team into new company, Dotmo, due to costs",
    "url": "https://techcrunch.com/2026/06/18/snap-spins-off-ai-video-team-into-new-company-dotmo-due-to-costs/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T20:30:00+00:00",
    "summary": "The Snapchat maker is spinning off yet another internal unit. Dotmo will be composed of current Snap staff who are leaving the social media company to focus on AI video development."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/openai-is-bringing-on-some-big-guns-in-the-lead-up-to-its-ipo/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI is bringing on some big guns in the lead-up to its IPO",
    "url": "https://techcrunch.com/2026/06/18/openai-is-bringing-on-some-big-guns-in-the-lead-up-to-its-ipo/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T19:59:22+00:00",
    "summary": "OpenAI is bulking up before its IPO, landing Transformer co-inventor Noam Shazeer from Google DeepMind and former Trump AI policy official Dean Ball in the same week."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/the-11-standout-startups-from-ycs-demo-day-according-to-vcs/",
    "domain": "大厂 AI 动态",
    "title": "The 11 standout startups from YC’s Demo Day, according to VCs",
    "url": "https://techcrunch.com/2026/06/18/the-11-standout-startups-from-ycs-demo-day-according-to-vcs/",
    "source": "Marina Temkin, Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T19:52:19+00:00",
    "summary": "TechCrunch spoke to investors to find the hottest startups in the Spring 2026 YC batch. Some of them commanded valuations of over $175 million, VCs said."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/rivian-owners-file-lawsuit-alleging-false-promises-on-self-driving-features/",
    "domain": "大厂 AI 动态",
    "title": "Rivian owners file lawsuit alleging false promises on self-driving features",
    "url": "https://techcrunch.com/2026/06/18/rivian-owners-file-lawsuit-alleging-false-promises-on-self-driving-features/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T19:31:45+00:00",
    "summary": "Plaintiffs in the class -action complaint allege Rivian falsely promised for years it would bring hands-free driving to its first-generation R1 vehicles."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/almost-half-of-u-s-singles-feel-negatively-about-ai-in-dating-match-says/",
    "domain": "大厂 AI 动态",
    "title": "Almost half of US singles feel negatively about AI in dating, Match says",
    "url": "https://techcrunch.com/2026/06/18/almost-half-of-u-s-singles-feel-negatively-about-ai-in-dating-match-says/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T18:51:46+00:00",
    "summary": "About 47% of singles look negatively at the use of AI in dating -- but many dating app users are open to AI helping with profile punch-ups and conversation starters."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/amazon-hopes-to-challenge-nvidia-more-directly-by-selling-its-ai-chips/",
    "domain": "大厂 AI 动态",
    "title": "Amazon hopes to challenge Nvidia more directly by selling its AI chips",
    "url": "https://techcrunch.com/2026/06/18/amazon-hopes-to-challenge-nvidia-more-directly-by-selling-its-ai-chips/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T18:22:13+00:00",
    "summary": "AWS is in talks to sell its chips to other data centers. CEO Andy Jassy has said this represents a $50 billion opportunity for the company."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/mivos-new-app-takes-a-mindful-approach-to-managing-screen-time/",
    "domain": "大厂 AI 动态",
    "title": "Mivo’s new app takes a mindful approach to managing screen time",
    "url": "https://techcrunch.com/2026/06/18/mivos-new-app-takes-a-mindful-approach-to-managing-screen-time/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T18:00:00+00:00",
    "summary": "Notably, unlike other apps that might just try to pull you away from your phone, Mivo lets the user decide if they want to continue, encouraging users to become more aware of how and why they’re using"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/ai-data-centers-just-got-a-government-mandated-fast-lane-to-the-grid/",
    "domain": "大厂 AI 动态",
    "title": "AI data centers just got a government-mandated fast lane to the grid",
    "url": "https://techcrunch.com/2026/06/18/ai-data-centers-just-got-a-government-mandated-fast-lane-to-the-grid/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T17:49:23+00:00",
    "summary": "FERC told grid operators to give data centers a fast lane for interconnections, but it failed to address electricity supply shortages."
  },
  {
    "id": "rss:https://stratechery.com/2026/the-stuff-of-mythos/",
    "domain": "大厂 AI 动态",
    "title": "2026.25: The Stuff of Myth(os)",
    "url": "https://stratechery.com/2026/the-stuff-of-mythos/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of June 15, 2026, including Anthropic, e-commerce in the age of AI, and the NBA Finals being a perfect 10."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-michael-morton-about-e-commerce-in-the-age-of-ai/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with Michael Morton About E-Commerce in the Age of AI",
    "url": "https://stratechery.com/2026/an-interview-with-michael-morton-about-e-commerce-in-the-age-of-ai/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T10:00:00+00:00",
    "summary": "An interview with Michael Morton about e-commerce and AI, including the challenges of unfalsifiable bear cases, distribution versus referal models, grocery, and autonomous vehicles."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/rocket-report-rebuild-begins-at-blue-origin-launch-pad-relativity-targets-mars/",
    "domain": "大厂 AI 动态",
    "title": "Rocket Report: Rebuild begins at Blue Origin launch pad; Relativity targets Mars",
    "url": "https://arstechnica.com/space/2026/06/rocket-report-rebuild-begins-at-blue-origin-launch-pad-relativity-targets-mars/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T13:36:53+00:00",
    "summary": "A French launch startup is scrapping the name of its rocket, apparently due to a trademark issue."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/as-global-warming-threatens-corals-scientists-search-for-reefs-that-can-take-the-heat/",
    "domain": "大厂 AI 动态",
    "title": "As global warming threatens corals, scientists search for reefs that can take the heat",
    "url": "https://arstechnica.com/science/2026/06/as-global-warming-threatens-corals-scientists-search-for-reefs-that-can-take-the-heat/",
    "source": "Teresa Tomassoni, Inside Climate News",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T11:15:11+00:00",
    "summary": "Researchers say these coral strongholds may help repopulate more degraded reefs."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/a-bold-satellite-rescue-mission-came-together-in-record-time-but-will-it-work/",
    "domain": "大厂 AI 动态",
    "title": "A bold satellite rescue mission came together in record time, but will it work?",
    "url": "https://arstechnica.com/space/2026/06/a-bold-satellite-rescue-mission-came-together-in-record-time-but-will-it-work/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T00:39:30+00:00",
    "summary": "\"I consider this a success already, just from the fact that we're even going to try this.\""
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/06/microsoft-spots-new-self-propagating-malware-for-stealing-cryptocurrency/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft discovers new lightweight backdoor that steals cryptocurrency",
    "url": "https://arstechnica.com/security/2026/06/microsoft-spots-new-self-propagating-malware-for-stealing-cryptocurrency/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T23:28:52+00:00",
    "summary": "Crypto Clipper spreads over USB and communicates over Tor."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/06/fda-advisors-unanimously-vote-to-approve-modernas-mrna-after-agency-drama/",
    "domain": "大厂 AI 动态",
    "title": "FDA advisors unanimously vote to approve Moderna's mRNA after agency drama",
    "url": "https://arstechnica.com/health/2026/06/fda-advisors-unanimously-vote-to-approve-modernas-mrna-after-agency-drama/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T22:08:59+00:00",
    "summary": "In February, a Trump official refused to review the vaccine."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/as-china-looms-taiwan-makes-more-drones-for-defense-and-the-us-military/",
    "domain": "大厂 AI 动态",
    "title": "As China looms, Taiwan makes more drones for defense and the US military",
    "url": "https://arstechnica.com/ai/2026/06/as-china-looms-taiwan-makes-more-drones-for-defense-and-the-us-military/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T21:21:26+00:00",
    "summary": "Taiwan's drone spending plans for defense could also boost business overseas."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/nasas-1-1-billion-gateway-habitation-module-is-unlikely-to-be-used-for-something-else/",
    "domain": "大厂 AI 动态",
    "title": "NASA asks Northrop Grumman to stop working on lunar HALO module",
    "url": "https://arstechnica.com/space/2026/06/nasas-1-1-billion-gateway-habitation-module-is-unlikely-to-be-used-for-something-else/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T20:49:55+00:00",
    "summary": "\"We are reassigning most affected employees across existing opportunities and programs.\""
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/google-shares-updated-timeline-for-rolling-out-android-developer-verification/",
    "domain": "大厂 AI 动态",
    "title": "Android verification is coming: Google confirms timeline and supported app stores",
    "url": "https://arstechnica.com/gadgets/2026/06/google-shares-updated-timeline-for-rolling-out-android-developer-verification/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T19:53:33+00:00",
    "summary": "A new system service will roll out this month ahead of big changes starting in September."
  },
  {
    "id": "rss:https://arstechnica.com/apple/2026/06/apple-patches-high-severity-eavesdropping-vulnerability-in-beats-studio-buds/",
    "domain": "大厂 AI 动态",
    "title": "Apple patches high-severity eavesdropping vulnerability in Beats Studio Buds",
    "url": "https://arstechnica.com/apple/2026/06/apple-patches-high-severity-eavesdropping-vulnerability-in-beats-studio-buds/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T19:41:35+00:00",
    "summary": "The vulnerability, disclosed 12 months ago, affects multiple manufacturers."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/after-senate-vote-trump-admin-backs-off-plans-to-kill-ocean-monitoring/",
    "domain": "大厂 AI 动态",
    "title": "After Senate vote, Trump admin backs off plans to kill ocean monitoring",
    "url": "https://arstechnica.com/science/2026/06/after-senate-vote-trump-admin-backs-off-plans-to-kill-ocean-monitoring/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T18:19:44+00:00",
    "summary": "It's unclear whether the system is currently intact."
  },
  {
    "id": "rss:https://arstechnica.com/information-technology/2026/06/before-spacex-ipo-investors-in-china-secretly-acquired-stakes/",
    "domain": "大厂 AI 动态",
    "title": "Before SpaceX IPO, investors in China secretly acquired stakes",
    "url": "https://arstechnica.com/information-technology/2026/06/before-spacex-ipo-investors-in-china-secretly-acquired-stakes/",
    "source": "stin Elliott and Joshua Kaplan, ProPublica",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T17:42:18+00:00",
    "summary": "One previously unreported SpaceX investor has ties to Chinese military contractors."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/bernie-sanders-unveils-7-trillion-plan-to-give-americans-control-of-ai-industry/",
    "domain": "大厂 AI 动态",
    "title": "Bernie Sanders unveils $7 trillion plan to give Americans control of AI industry",
    "url": "https://arstechnica.com/tech-policy/2026/06/bernie-sanders-unveils-7-trillion-plan-to-give-americans-control-of-ai-industry/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T17:02:49+00:00",
    "summary": "Biggest AI firms will likely recoil at Bernie Sanders' AI wealth fund."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/hunter-gatherers-in-siberia-died-of-a-plague-outbreak-5500-years-ago/",
    "domain": "大厂 AI 动态",
    "title": "Hunter-gatherers in Siberia died of a plague outbreak 5,500 years ago",
    "url": "https://arstechnica.com/science/2026/06/hunter-gatherers-in-siberia-died-of-a-plague-outbreak-5500-years-ago/",
    "source": "Kiona N. Smith",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T15:04:40+00:00",
    "summary": "We can't blame the Neolithic Transition for the plague anymore."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/cosmonaut-aleksandr-samokutyaev-56-is-first-former-iss-crew-member-to-die/",
    "domain": "大厂 AI 动态",
    "title": "The first long-duration resident of the ISS, a cosmonaut, has died",
    "url": "https://arstechnica.com/space/2026/06/cosmonaut-aleksandr-samokutyaev-56-is-first-former-iss-crew-member-to-die/",
    "source": "Robert Pearlman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T14:34:36+00:00",
    "summary": "Two expeditions, two spacewalks, 322 days in space."
  },
  {
    "id": "rss:https://www.producthunt.com/products/azure-cosmos-db",
    "domain": "大厂 AI 动态",
    "title": "Free AI Image Upscaler",
    "url": "https://www.producthunt.com/products/azure-cosmos-db",
    "source": "AMAN",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T03:15:54+00:00",
    "summary": "Locally Increase Resolution of Images Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/amazon-wholesale-with-stemar-greene",
    "domain": "大厂 AI 动态",
    "title": "Amazon Wholesale with Stemar Greene",
    "url": "https://www.producthunt.com/products/amazon-wholesale-with-stemar-greene",
    "source": "Abuv the Par",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T10:54:39+00:00",
    "summary": "Amazon Wholesale Success Starts with the Right Strategy Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/basedash",
    "domain": "大厂 AI 动态",
    "title": "Basedash Access Controls",
    "url": "https://www.producthunt.com/products/basedash",
    "source": "Max Musing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T16:05:30+00:00",
    "summary": "Control exactly who can access your company data Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/are-you-in-the-weights",
    "domain": "大厂 AI 动态",
    "title": "Are you in the Weights?",
    "url": "https://www.producthunt.com/products/are-you-in-the-weights",
    "source": "Thomas Dimson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T00:56:01+00:00",
    "summary": "Find out if you live forever in the brain of the LLMs Discussion | Link"
  },
  {
    "id": "wscn:3774876",
    "domain": "股票",
    "title": "AI算力的物理基石：PTFE从“塑料王”到“M10高速互联刚需材料”的范式跃迁",
    "url": "https://wallstreetcn.com/premium/articles/3774876?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T04:11:40+00:00",
    "summary": "PTFE：又一个被AI再造的新材料。"
  },
  {
    "id": "wscn:3775111",
    "domain": "股票",
    "title": "相比“开源模型”，“前沿模型”溢价类似“奢侈品包包”！德银：这可能导致市场重估AI",
    "url": "https://wallstreetcn.com/articles/3775111",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T03:31:58+00:00",
    "summary": "德银认为，前沿专有AI模型（如Claude Fable 5，每任务成本约3.25美元）与开源模型（如DeepSeek V4-Pro，约5美分）存在约65倍的成本鸿沟，但对90%的日常任务而言，两者表现相当。随着AI计费模式转向按量收费，企业成本意识觉醒，AI定价锚点正从“算力需求”转向“运营成本”，可能引发比\"DeepSeek时刻\"更深远的市场重估。"
  },
  {
    "id": "wscn:3775110",
    "domain": "股票",
    "title": "德银“向沃什投降”：今年将加息50基点，甚至可能在7月提前加息",
    "url": "https://wallstreetcn.com/articles/3775110",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T02:50:25+00:00",
    "summary": "德银彻底扭转原有宽松预期，全面上调通胀预测，预计今年将加息两次共50个基点，利率升至4.1%；并警告美联储行动或更激进，甚至可能在7月提前加息，或全年加息75个基点。触发因素为新主席沃什鹰派表态及通胀压力广泛持续。"
  },
  {
    "id": "wscn:3775108",
    "domain": "股票",
    "title": "鸿海董事长：每1GW Vera Rubin数据中心，资本开支高达470亿美元，每年电力成本13亿美元",
    "url": "https://wallstreetcn.com/articles/3775108",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T02:23:41+00:00",
    "summary": "刘扬伟引述数据称，建立1GW以Vera Rubin为核心的AIDC，所需机柜数量约为3557座，而单一座Vera Rubin机柜售价即达910万美元，1GW规模的AIDC每年电力支出达13亿美元，而硬件折旧费用更是电力成本的六倍，意味着年度折旧负担约达78亿美元。他预计2030年全球算力将新增106GW电力需求。"
  },
  {
    "id": "wscn:3775107",
    "domain": "股票",
    "title": "1192亿美元！本周美股吸引创纪录资金，投资者涌向科技股",
    "url": "https://wallstreetcn.com/articles/3775107",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T02:06:05+00:00",
    "summary": "截至6月17日当周，流入美国股票基金的资金规模达到创纪录的1192亿美元，刷新历史峰值。科技股成为资金追捧的核心标的，单周流入规模达192亿美元，亦为历史最高。美银警告，如果特朗普支持率在9月前未能出现明显反弹，多头情绪将变得'焦虑不安'。"
  },
  {
    "id": "wscn:3775106",
    "domain": "股票",
    "title": "“新美联储通讯社”：1996还是1999？沃什的第一场考验是“如何看AI”",
    "url": "https://wallstreetcn.com/articles/3775106",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T01:35:27+00:00",
    "summary": "Timiraos认为，沃什执掌美联储的首要考验是判断AI繁荣本质：是1996年的生产率红利（按兵不动），还是1999年的需求过热（需加息）。他倾向拥抱AI生产率叙事而暂不加息，但面临着关税与赤字压力、内部“AI预期透支推高通胀”的分歧，以及废除前瞻指引的政策两难。"
  },
  {
    "id": "wscn:3775105",
    "domain": "股票",
    "title": "学习英伟达“好榜样”，谷歌和博通都开始“有样学样”，开启“AI芯片闭环”",
    "url": "https://wallstreetcn.com/articles/3775105",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T01:10:09+00:00",
    "summary": "谷歌为数据中心提供担保以撬动自研芯片销售，以850亿美元融资计划为后盾争夺算力客户，博通联合阿波罗、黑石设立350亿美元AI算力平台，并提供信用背书。分析指，这种深度绑定芯片厂商、私募信贷与算力需求的“融资闭环”正重塑市场格局，实质性冲击英伟达的垄断份额。"
  },
  {
    "id": "wscn:3775103",
    "domain": "股票",
    "title": "华尔街见闻早餐FM-Radio | 2026年6月20日",
    "url": "https://wallstreetcn.com/articles/3775103",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T23:17:59+00:00",
    "summary": "五分钟看懂全球市场，尽在财经早餐。"
  },
  {
    "id": "wscn:3775104",
    "domain": "股票",
    "title": "特朗普紧盯AI：一周前视Anthropic为“国家安全威胁”，现仍不排除必要时干预",
    "url": "https://wallstreetcn.com/articles/3775104",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T23:10:12+00:00",
    "summary": "被问及是否认为Anthropic对美国安全构成威胁，特朗普称，现在不是，一周前也许是。他说，该司在美政府表达担忧后迅速回应，表现得“非常负责”；不会关闭该司，但不确定是否非得动用法律赋予的紧急权力干预不可。"
  },
  {
    "id": "wscn:3775102",
    "domain": "股票",
    "title": "英国内斗升级！伯纳姆补选大胜、接班概率升破90%，内阁大臣被曝要求斯塔默定下台时间",
    "url": "https://wallstreetcn.com/articles/3775102",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T22:25:11+00:00",
    "summary": "英媒称内阁大臣劝斯塔默主动让位：“你的时间到了”；多名大臣要求他为离职设定时间表。预测市场Polymarket的押注显示，今年不会产生新首相的概率仅为3.5%。"
  },
  {
    "id": "wscn:3775100",
    "domain": "股票",
    "title": "以黎局势挑动市场神经，欧股一度转涨，布油艰难反弹，美元跌落一年高位",
    "url": "https://wallstreetcn.com/articles/3775100",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T22:19:09+00:00",
    "summary": "美股休市。以色列停火消息后，美股期货收窄多数跌幅，泛欧股指曾转涨，矿业板块跌超2%领跌欧股；连日创一年新高的美元指数刷新日低；布油跌超1%；金银收窄多数跌幅，盘中曾跌超2%的现货黄金一度跌不足0.7%。以再袭真主党后，布油一度转涨超1%，全周仍跌近8%。日元终结五连跌、暂别近两年低位；离岸人民币盘中逼近6.80至四周新低。英国政局担忧加剧，英债领跌欧债。"
  },
  {
    "id": "wscn:3775101",
    "domain": "股票",
    "title": "高盛警惕美股：地缘动能趋于停滞，CTA下行不对称风险凸显",
    "url": "https://wallstreetcn.com/articles/3775101",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T22:09:28+00:00",
    "summary": "高盛One-Delta交易台负责人指出，多重风险正在积聚：美伊核谈判实质性受阻，油价地缘溢价尚未被市场充分消化，市场正在为实物原油定价，但尚未充分折现这一信任不足以及美伊协议动能的持续恶化。同时，CTA下行不对称格局已形成，美联储政策框架的不确定性与债券市场波动率上升交织叠加，市场内部结构隐患不可忽视。"
  },
  {
    "id": "wscn:3775098",
    "domain": "股票",
    "title": "以色列被曝与黎真主党达成停火，伊朗证实推迟与美谈判，特朗普施压“耗完60天”，白宫放风准备尽早启程谈判",
    "url": "https://wallstreetcn.com/articles/3775098",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T21:21:49+00:00",
    "summary": "多家媒体称以色列和真主党同意周五停火；美媒称停火生效后一小时内双方各有袭击动作；黎媒称以方“同意停火”后空袭黎南部。伊美谈判斡旋方将21日在埃及会晤。伊外交部指美对黎局势负直接责任，称正讨论未来几天举行谈判的计划。白宫称美代表团准备最早可行时机启程。特朗普称，谈判源于伊朗、而非美方走投无路，他可阻止以袭黎，因为以方“会照我说的做”。"
  },
  {
    "id": "wscn:3775099",
    "domain": "股票",
    "title": "伊朗否认霍尔木兹关闭，暂免通行费但未来或加收保险费，美军称20余船已通过海峡",
    "url": "https://wallstreetcn.com/articles/3775099",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T15:53:50+00:00",
    "summary": "伊朗管理霍尔木兹海峡的机构称，美伊谈判60天内免除海峡通行费；自本周五起，所有经过海峡船舶必须至少提前48小时向伊方提交过境申请；所有通过海峡船只必须办理一项强制性保险，该保险目前免费，未来可能收费。"
  },
  {
    "id": "wscn:3775054",
    "domain": "股票",
    "title": "债市和美联储预期分化了？市场不怕通胀了！",
    "url": "https://wallstreetcn.com/premium/articles/3775054?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T13:07:44+00:00",
    "summary": "因油价暴跌与美联储鹰派转向，盈亏平衡通胀率大幅下行，市场已提前交易通胀回落。"
  },
  {
    "id": "wscn:3775097",
    "domain": "股票",
    "title": "任命前SK海力士CEO领导封装业务，英特尔股价大涨10%创新高",
    "url": "https://wallstreetcn.com/articles/3775097",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T12:23:08+00:00",
    "summary": "英特尔加速重整代工业务，发力AI芯片市场。公司任命SK海力士前CEO Seok-Hee Lee主导先进封装，直接向CEO陈立武汇报；同日苹果确认与英特尔合作在美国本土设计制造芯片。双重利好推动股价飙升10%创历史新高。先进封装被确立为独立运营板块，EMIB-T与HBI技术正推进量产。"
  },
  {
    "id": "wscn:3775088",
    "domain": "股票",
    "title": "谷歌微软联手推新协议，传统科技巨头借标准战围堵Anthropic和OpenAI",
    "url": "https://wallstreetcn.com/articles/3775088",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T12:09:15+00:00",
    "summary": "谷歌、微软等传统科技巨头联合推出“代理资源发现”（ARD）新协议，旨在将自身产品打造为企业AI的统一入口，通过标准战围堵Anthropic与OpenAI。此举与后两者试图将Claude和ChatGPT打造成独立主入口的战略直接冲突，凸显了双方在企业AI生态主导权上的激烈争夺。ARD能否被广泛采纳，仍有待观察。"
  },
  {
    "id": "wscn:3775094",
    "domain": "股票",
    "title": "从\"Token竞赛\"到\"Token节流\"：月人均成本7500美元，天价账单倒逼巨头集体踩刹车",
    "url": "https://wallstreetcn.com/articles/3775094",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T12:04:15+00:00",
    "summary": "企业AI支出从“极限消耗”转向“极限节流”，巨头纷纷为AI使用和智能体工具设置上限以应对失控的成本压力。这一预算管控浪潮引发了企业在控本与生产率之间的分歧，同时也让微软、Databricks等提供成本优化、网关工具及模型路由器的基础设施商迎来红利。"
  },
  {
    "id": "wscn:3775096",
    "domain": "股票",
    "title": "8000万桶原油，准备通过霍尔木兹海峡",
    "url": "https://wallstreetcn.com/articles/3775096",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T12:04:03+00:00",
    "summary": "波斯湾40艘超级油轮上约8000万桶非受制裁原油已蓄势待发，部分船只率先尝试通行，有望缓解亚洲炼厂因前期局势导致的断供与库存压力；但行业组织警告水雷等重大安全风险依然存在，全面复航仍具不确定性。"
  },
  {
    "id": "wscn:3775093",
    "domain": "股票",
    "title": "广东服务业蓝图出炉：剑指11万亿增加值，算力网络、6G与人工智能成三大战略支点",
    "url": "https://wallstreetcn.com/articles/3775093",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T12:03:43+00:00",
    "summary": "《方案》明确，到2030年全省服务业增加值突破11万亿元，通过数智化、标准化、融合化、国际化“四化”提升，推动生产性服务业向高端延伸、生活性服务业向高品质升级。方案以算力网络、6G与人工智能为三大战略支点，加快建设粤港澳大湾区算力枢纽，前瞻布局6G与卫星互联网，推进人工智能全域全时应用，并系统部署金融、物流、文旅等多领域，全面构建优质高效的现代化服务业体系。"
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
    "id": "rss:https://www.netinterest.co/p/defying-the-surveys",
    "domain": "股票",
    "title": "Defying the Surveys",
    "url": "https://www.netinterest.co/p/defying-the-surveys",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-17T16:54:51+00:00",
    "summary": "Banks report a resilient quarter &#8211; and a lurking threat"
  },
  {
    "id": "rss:https://www.netinterest.co/p/shuffling-risk",
    "domain": "股票",
    "title": "Shuffling Risk",
    "url": "https://www.netinterest.co/p/shuffling-risk",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-04-10T15:10:44+00:00",
    "summary": "An Asset Class Reborn"
  },
  {
    "id": "rss:https://www.netinterest.co/p/new-pod-the-race-to-secure-a-bank",
    "domain": "股票",
    "title": "NEW POD! The Race to Secure a Bank Charter with Adam Shapiro of Klaros Group",
    "url": "https://www.netinterest.co/p/new-pod-the-race-to-secure-a-bank",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-31T15:45:44+00:00",
    "summary": "Net Interest Extra ep 21"
  },
  {
    "id": "rss:https://www.netinterest.co/p/revolut-unbound",
    "domain": "股票",
    "title": "Revolut Unbound",
    "url": "https://www.netinterest.co/p/revolut-unbound",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-27T16:20:38+00:00",
    "summary": "The Quest to Build the World&#8217;s First Truly Global Bank"
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-underwriters-of-hormuz",
    "domain": "股票",
    "title": "The Underwriters of Hormuz",
    "url": "https://www.netinterest.co/p/the-underwriters-of-hormuz",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-20T16:23:35+00:00",
    "summary": "A post on marine insurance &#8211; by popular demand"
  },
  {
    "id": "rss:https://www.netinterest.co/p/new-pod-market-intelligence-in-the",
    "domain": "股票",
    "title": "🎙️ Market Intelligence in the Age of AI: An Interview with Morningstar CEO, Kunal Kapoor",
    "url": "https://www.netinterest.co/p/new-pod-market-intelligence-in-the",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-17T16:30:34+00:00",
    "summary": "Net Interest Extra ep 20"
  },
  {
    "id": "rss:https://www.netinterest.co/p/redemption-day",
    "domain": "股票",
    "title": "Redemption Day",
    "url": "https://www.netinterest.co/p/redemption-day",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-13T18:09:28+00:00",
    "summary": "When the exit is smaller than the entrance"
  },
  {
    "id": "rss:https://www.netinterest.co/p/learning-from-lloyd",
    "domain": "股票",
    "title": "Learning from Lloyd",
    "url": "https://www.netinterest.co/p/learning-from-lloyd",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-06T17:42:54+00:00",
    "summary": "Blankfein, Goldman and the Next Market Reckoning"
  },
  {
    "id": "rss:https://www.netinterest.co/p/new-pod-how-credit-markets-shaped",
    "domain": "股票",
    "title": "🎙️ How Credit Markets Shaped a Nation: An Interview with Sarah Quinn",
    "url": "https://www.netinterest.co/p/new-pod-how-credit-markets-shaped",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-03-03T16:45:21+00:00",
    "summary": "Net Interest Extra ep 19"
  },
  {
    "id": "rss:https://www.netinterest.co/p/two-tribes",
    "domain": "股票",
    "title": "Two Tribes",
    "url": "https://www.netinterest.co/p/two-tribes",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-02-27T17:42:58+00:00",
    "summary": "Private Credit, Public Markets and the AI Reckoning"
  },
  {
    "id": "rss:https://www.netinterest.co/p/ai-and-i",
    "domain": "股票",
    "title": "AI and I",
    "url": "https://www.netinterest.co/p/ai-and-i",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-02-20T17:21:53+00:00",
    "summary": "Claude Code, Bloomberg and the Battle for Data"
  }
]
```
