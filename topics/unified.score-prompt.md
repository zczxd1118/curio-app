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

- 今日日期：`2026-06-26`
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
  "date": "2026-06-26",
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
    "points": 3416698,
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
    "points": 1319982,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1NvRyBzEhq",
    "domain": "AI",
    "title": "全网最全！60分钟全面掌握Claude Code～【附完整文档】",
    "url": "http://www.bilibili.com/video/av116522328524431",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1259084,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1247332,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 779989,
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
    "points": 565113,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 453413,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 437649,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 415398,
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
    "points": 376296,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 248150,
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
    "points": 243721,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 221961,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1RAEz6EE98",
    "domain": "AI",
    "title": "为什么Claude Code+DeepSeekV4是最有性价比的个人AI Agent?",
    "url": "http://www.bilibili.com/video/av116732144392386",
    "source": "呱声一片",
    "platform": "bilibili",
    "points": 175803,
    "published_at": "2026-06-11T15:27:06+00:00",
    "summary": "官方文档地址：https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/claude_code"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 175500,
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
    "points": 158416,
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
    "points": 157995,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 152467,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 144938,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 97765,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73365,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 60669,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 52444,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 46152,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1ZEJA6xEds",
    "domain": "AI",
    "title": "最新方法！国内免费无限制，使用Claude Code！",
    "url": "http://www.bilibili.com/video/av116746874848391",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 45696,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 40068,
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
    "points": 36976,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29788,
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
    "points": 29373,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27499,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV1RUDsBWEHb",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的Cursor+Skills实战指南教程，手把手带你开发爆款app，全程干货无废话！比付费效果强十倍！",
    "url": "http://www.bilibili.com/video/av116373464350785",
    "source": "AI大模型技术教程",
    "platform": "bilibili",
    "points": 23893,
    "published_at": "2026-04-09T10:15:00+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\nCursor+Skills频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV1GC5H6WEGs",
    "domain": "AI",
    "title": "新手必看+简单调参解释+视频演示(双子星AI辅助瞄准)",
    "url": "http://www.bilibili.com/video/av116551470549763",
    "source": "布衣封王候",
    "platform": "bilibili",
    "points": 16046,
    "published_at": "2026-05-10T17:46:12+00:00",
    "summary": "新手必看+简单调参解释+视频演示(双子星AI辅助瞄准)双子星AI自行下载地址\nhttps://www.123865.com/s/FymUVv-xi5BA"
  },
  {
    "id": "bvid:BV1ssEE6CEks",
    "domain": "AI",
    "title": "Ai自动画图：CAD建筑平面图测试（CodexGPT5.5）",
    "url": "http://www.bilibili.com/video/av116719259485897",
    "source": "Tutor南洋",
    "platform": "bilibili",
    "points": 13843,
    "published_at": "2026-06-09T08:47:15+00:00",
    "summary": "体验一下ai画图，不过CAD软件基本操作也不能拉下~\nCAD教学基础入门视频合集↓\n传送门：BV1aT4y1B7oY\n整个合集教学的，不要跳着看啊喂！\n看完了那基本就能跟上啦，提问请@我，不然评论太多我是看不到的"
  },
  {
    "id": "bvid:BV14cZqB8EBY",
    "domain": "AI",
    "title": "AI攻克不了的领域竟然是它？揭秘CNC编程为何让AI束手无策",
    "url": "http://www.bilibili.com/video/av116097411976217",
    "source": "极微视界",
    "platform": "bilibili",
    "points": 13502,
    "published_at": "2026-02-19T12:59:23+00:00",
    "summary": "CNC编程AI化有多难？本视频深度解析为什么AI编程在制造业进展缓慢。\n从材料、刀具、机床到隐性知识，揭秘老师傅的经验为什么无法数字化。\nPowerMill、CloudNC等AI编程软件的真实水平如何？CNC编程师的未来在哪里？\n\n⏱️ 时间轴 Timestamps:\n\n00:00 开篇：AI在CNC领域的困境\n00:20 材料的复杂性：为什么同样是45#钢参数却不同\n01:01 刀具与机床的个体"
  },
  {
    "id": "bvid:BV165dAYxEdD",
    "domain": "AI",
    "title": "只需几行代码用Java写一个MCP服务！从0到1开发MCP服务！",
    "url": "http://www.bilibili.com/video/av114306863598282",
    "source": "图灵诸葛官方号",
    "platform": "bilibili",
    "points": 12198,
    "published_at": "2025-04-09T07:43:00+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持~\r\n本视频配套资料戳这里获取→https://www.bilibili.com/read/cv38661345/\r\n【还可额外领取100w字Java面试宝典】"
  },
  {
    "id": "bvid:BV1L3Vd6nEeB",
    "domain": "AI",
    "title": "【2026版】这可能是B站唯一将Codex+Claude Code讲明白的教程，从下载安装到环境配置、核心功能、使用技巧到项目实战讲透，存下吧，比啃书好太多了！",
    "url": "http://www.bilibili.com/video/av116673726257360",
    "source": "12点就睡的林同学",
    "platform": "bilibili",
    "points": 10495,
    "published_at": "2026-06-01T08:08:09+00:00",
    "summary": "别只收藏，不实操。这期 Codex保姆级完整教程 的配套资料，我已经整理好了，适合想系统学习 Codex、AI编程助手、AI开发提效 的同学。资料内容包括：\nCodex入门使用指南、安装与环境配置流程、常用功能操作清单、高效提示词模、编程实战案例拆解、常见问题与避坑总、从入门到项目落地的学习路线图\n如果你想真正学会 Codex，而不是只停留在“看过视频”的层面建议 视频 + 资料 一起搭配学习。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "穷在街头无人问lhj",
    "platform": "bilibili",
    "points": 10009,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1jsEQ6XEw6",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116724292721480",
    "source": "倒计时19",
    "platform": "bilibili",
    "points": 9740,
    "published_at": "2026-06-10T06:04:26+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9096,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1etEQ6DETs",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116724192118321",
    "source": "AI产品经理大模型",
    "platform": "bilibili",
    "points": 8936,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1btjd6JEcD",
    "domain": "AI",
    "title": "十分钟上线一个AI Agent：从创建到部署完整演示",
    "url": "http://www.bilibili.com/video/av116804219375000",
    "source": "GeekHour",
    "platform": "bilibili",
    "points": 8687,
    "published_at": "2026-06-24T10:00:00+00:00",
    "summary": "我们刚更新了一下粉丝福利的机制，点击链接到达活动页（组件链接：https://cloud.tencent.com/act/pro/edgeone-makers-agent?from=30132），点击“点亮 Star &amp; 邀请码福利”活动，粉丝填入邀请码（43621840）即可获得50万Token。\nAI社区地址：https://geekhour.net，欢迎加入！"
  },
  {
    "id": "bvid:BV1oXjc6CEWK",
    "domain": "AI",
    "title": "（2026版）这才是B站讲的最好的Vibe Coding企业级项目实战，Claude Code+Codex+Cursor丨一周学完，让你少走99%弯路！",
    "url": "http://www.bilibili.com/video/av116769742195971",
    "source": "京东架构师诸葛",
    "platform": "bilibili",
    "points": 8642,
    "published_at": "2026-06-18T06:52:48+00:00",
    "summary": "（2026版）这才是B站讲的最好的Vibe Coding企业级项目实战，Claude Code+Codex+Cursor丨一周学完，让你少走99%弯路！\n【视频配套学习笔记、Agent开发、大模型最新学习路线、系统学习、实战案例、电子书+问题解答】都在这了：https://www.bilibili.com/read/cv39979382/"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 8327,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 6984,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 6642,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6468,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1uz8jzdEZy",
    "domain": "AI",
    "title": "AI Agent 设计助手功能教程丨自然语言交互驱动 AI 智能设计花境、导出苗木清单",
    "url": "http://www.bilibili.com/video/av114929986241780",
    "source": "D5渲染器",
    "platform": "bilibili",
    "points": 6365,
    "published_at": "2025-07-28T10:55:00+00:00",
    "summary": "全新上线的D5 2.11版本正式推出D5 AI 设计助手（AI Agent），能够准确理解设计意图，智能处理复杂任务。与 AI 设计助手对话，通过自然语言交互驱动 AI 完成专业任务。首次上线带来了「花境生成器」「智能苗木清单」「D5 Bot」，未来设计助手还将具备更多能力，令创作者更专注核心创意塑造和方案决策。\n\n获取D5渲染器： https://www.d5render.cn/\n\n2.11宣传"
  },
  {
    "id": "bvid:BV1u4G9zmEte",
    "domain": "AI",
    "title": "什么是MCP？VS Code中使用MCP Server",
    "url": "http://www.bilibili.com/video/av114426032168712",
    "source": "AI落地派",
    "platform": "bilibili",
    "points": 6302,
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based o"
  },
  {
    "id": "bvid:BV15i7K69EN7",
    "domain": "AI",
    "title": "【6.22最新发布】claude桌面版安装教程！一周快速入门claude code保姆级教程！",
    "url": "http://www.bilibili.com/video/av116793196676384",
    "source": "是蒜七丫",
    "platform": "bilibili",
    "points": 6215,
    "published_at": "2026-06-22T10:07:14+00:00",
    "summary": "求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连"
  },
  {
    "id": "bvid:BV1eX7A6LEY1",
    "domain": "AI",
    "title": "【2026版】这可能是B站唯一将Vibe Coding企业级项目实战讲明白的教程，Claude Code+Codex+Cursor，存下吧，让你少走99%的弯路",
    "url": "http://www.bilibili.com/video/av116792575925987",
    "source": "12点就睡的林同学",
    "platform": "bilibili",
    "points": 5789,
    "published_at": "2026-06-22T07:53:25+00:00",
    "summary": "【2026版】这可能是B站唯一将Vibe Coding企业级项目实战讲明白的教程，Claude Code+Codex+Cursor，存下吧，让你少走99%的弯路！！\n【视频配套学习笔记、Agent开发、大模型最新学习路线、系统学习、实战案例、电子书+问题解答】都在这了：https://www.bilibili.com/read/cv39979382/"
  },
  {
    "id": "rss:https://www.eetimes.com/jim-keller-on-tenstorrents-blackhole-scaling-and-ipo-ambitions/",
    "domain": "AI 算力 / 半导体",
    "title": "Jim Keller: ‘AI Still Obeys the Old Laws of Compute’",
    "url": "https://www.eetimes.com/jim-keller-on-tenstorrents-blackhole-scaling-and-ipo-ambitions/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T22:00:00+00:00",
    "summary": "Invoking Rent's Rule and Amdahl's Law, Keller argues that memory and communication, not bigger processors, will define the future of AI infrastructure The post Jim Keller: ‘AI Still Obeys the Old Laws"
  },
  {
    "id": "rss:https://www.eetimes.com/openai-jalapeno-will-be-spicy-but-the-real-sizzle-is-its-chip-design-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI’s Jalapeño Will Be Spicy, But the Real Sizzle Is Its Chip Design AI",
    "url": "https://www.eetimes.com/openai-jalapeno-will-be-spicy-but-the-real-sizzle-is-its-chip-design-ai/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T15:59:00+00:00",
    "summary": "The custom inference accelerator follows the hyperscaler playbook, but the AI-automated chip design process could prove the more consequential announcement. The post OpenAI’s Jalapeño Will Be Spicy, B"
  },
  {
    "id": "rss:https://www.eetimes.com/vicfuse-introduces-ul-class-fuse-series-for-modern-ai-infrastructure-and-industrial-protection/",
    "domain": "AI 算力 / 半导体",
    "title": "Vicfuse Introduces UL Class Fuse Series for Modern AI Infrastructure and Industrial Protection",
    "url": "https://www.eetimes.com/vicfuse-introduces-ul-class-fuse-series-for-modern-ai-infrastructure-and-industrial-protection/",
    "source": "VICFUSE",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T13:00:00+00:00",
    "summary": "Vicfuse introduces its UL Class fuse series, an industrial circuit-protection portfolio designed for AC and DC applications. The post Vicfuse Introduces UL Class Fuse Series for Modern AI Infrastructu"
  },
  {
    "id": "rss:https://www.eetimes.com/ibm-shows-sub-1-nm-chips-targeting-production-in-5-years/",
    "domain": "AI 算力 / 半导体",
    "title": "IBM Shows Sub-1-nm Chips, Targeting Production in 5 Years",
    "url": "https://www.eetimes.com/ibm-shows-sub-1-nm-chips-targeting-production-in-5-years/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T10:00:00+00:00",
    "summary": "IBM unveils 0.7-nm nanostack chips promising 100 billion transistors, denser SRAM, and production within five years. The post IBM Shows Sub-1-nm Chips, Targeting Production in 5 Years appeared first o"
  },
  {
    "id": "rss:https://www.eetimes.com/qualcomm-forecasts-billions-in-additional-revenue-from-new-data-center-solutions/",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm Forecasts Billions in Additional Revenue from New Data Center Solutions",
    "url": "https://www.eetimes.com/qualcomm-forecasts-billions-in-additional-revenue-from-new-data-center-solutions/",
    "source": "Jim McGregor",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T07:52:39+00:00",
    "summary": "Qualcomm takes the data center by storm with networking, AI accelerators, and both custom and standard CPUs. The post Qualcomm Forecasts Billions in Additional Revenue from New Data Center Solutions a"
  },
  {
    "id": "rss:https://www.eetimes.com/the-rise-of-autonomous-drone-warfare/",
    "domain": "AI 算力 / 半导体",
    "title": "The Rise of Autonomous Drone Warfare",
    "url": "https://www.eetimes.com/the-rise-of-autonomous-drone-warfare/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T22:14:58+00:00",
    "summary": "Cheap, autonomous drones developed in Ukraine are driving a new era of drone-on-drone warfare. The post The Rise of Autonomous Drone Warfare appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/deep-uv-lithography-processing-the-best-kept-secret-of-euv-lithography/",
    "domain": "AI 算力 / 半导体",
    "title": "Deep UV Lithography Processing, the Best Kept Secret of EUV Lithography",
    "url": "https://www.eetimes.com/deep-uv-lithography-processing-the-best-kept-secret-of-euv-lithography/",
    "source": "Drew Chambers",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T15:35:14+00:00",
    "summary": "EUV grabs the glory, but DUV does the dirty work that keeps advanced chips alive. The post Deep UV Lithography Processing, the Best Kept Secret of EUV Lithography appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/pressure-and-ultrasonic-flow-sensing-for-smarter-fluid-systems-2/",
    "domain": "AI 算力 / 半导体",
    "title": "Pressure and Ultrasonic Flow Sensing for Smarter Fluid Systems",
    "url": "https://www.eetimes.com/pressure-and-ultrasonic-flow-sensing-for-smarter-fluid-systems-2/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T14:00:00+00:00",
    "summary": "Modern fluid systems demand accurate, reliable monitoring to detect inefficiencies, prevent failures, and optimise performance. Engineers often face challenges with measurement accuracy at low flow ra"
  },
  {
    "id": "rss:https://www.eetimes.com/boosting-motor-control-performance-with-advanced-microcontroller-technology/",
    "domain": "AI 算力 / 半导体",
    "title": "Boosting Motor Control Performance with Advanced Microcontroller Technology",
    "url": "https://www.eetimes.com/boosting-motor-control-performance-with-advanced-microcontroller-technology/",
    "source": "GigaDevice",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T13:09:05+00:00",
    "summary": "Join this webinar where our expert will introduce key control concepts such as field-oriented control and power factor correction. The post Boosting Motor Control Performance with Advanced Microcontro"
  },
  {
    "id": "rss:https://www.eetimes.com/solid-state-circuit-breakers-for-dc-grids-architecture-protection-performance/",
    "domain": "AI 算力 / 半导体",
    "title": "Solid-State Circuit Breakers for DC Grids Architecture, Protection Performance",
    "url": "https://www.eetimes.com/solid-state-circuit-breakers-for-dc-grids-architecture-protection-performance/",
    "source": "Infineon Technologies and Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T12:59:13+00:00",
    "summary": "Join this webinar where our expert will present an SSCB for DC grids, developed with building blocks such as Si/SiC JFET/MOSFET switches. The post Solid-State Circuit Breakers for DC Grids Architectur"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-usd79-99-mini-lcd-screen-is-the-ultimate-retro-pc-gadget-and-its-on-sale-at-its-lowest-ever-price-3-5-inch-ips-display-includes-multiple-usb-ports-and-an-sd-card-reader-to-upgrade-your-desk-setup",
    "domain": "AI 算力 / 半导体",
    "title": "This $79.99 mini LCD screen is the ultimate retro PC gadget and it's on sale at its lowest-ever price — 3.5-inch IPS display includes multiple USB ports and an SD card reader to upgrade your desk setu",
    "url": "https://www.tomshardware.com/pc-components/this-usd79-99-mini-lcd-screen-is-the-ultimate-retro-pc-gadget-and-its-on-sale-at-its-lowest-ever-price-3-5-inch-ips-display-includes-multiple-usb-ports-and-an-sd-card-reader-to-upgrade-your-desk-setup",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T06:45:29+00:00",
    "summary": "Pick up this quirky retro mini monitor, with a built-in SD card reader and USB hub, for just $79.99 as a fun upgrade for your PC."
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/best-amazon-prime-day-deals-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Best Amazon Prime Day tech deals live on day four, last chance to grab savings — PC hardware deals on GPUs, CPUs, SSDs, and more",
    "url": "https://www.tomshardware.com/live/news/best-amazon-prime-day-deals-2026",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T06:34:44+00:00",
    "summary": "Find the very best PC hardware deals during Amazon Prime Day."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/prime-day-gaming-mouse-deals-round-up-up-your-game-with-a-new-mouse-on-sale",
    "domain": "AI 算力 / 半导体",
    "title": "Prime Day gaming mouse deals round-up — up your game with a new mouse on sale",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/prime-day-gaming-mouse-deals-round-up-up-your-game-with-a-new-mouse-on-sale",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T02:12:15+00:00",
    "summary": "We've rounded up the best Prime Day deals on gaming mice for every type of gamer — whether you're looking for ultra-lightweight, tons of buttons, or even modular mice, we've got you covered."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/asus-offers-up-to-36-percent-off-its-zenwifi-mesh-routers-tri-band-wi-fi-7-mesh-routers-starting-from-usd297-for-prime-day",
    "domain": "AI 算力 / 半导体",
    "title": "Asus offers up to 36% off its ZenWiFi mesh routers — tri-band Wi-Fi 7 mesh routers starting from $297",
    "url": "https://www.tomshardware.com/networking/routers/asus-offers-up-to-36-percent-off-its-zenwifi-mesh-routers-tri-band-wi-fi-7-mesh-routers-starting-from-usd297-for-prime-day",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T01:28:58+00:00",
    "summary": "Asus is taking up to 36% off its ZenWiFi mesh Wi-Fi 7 routers."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/nintendo-switch-2-is-once-again-usd399-at-woot-for-new-customers-usd419-for-returning-customers-with-code-save-up-to-usd50-while-supplies-last",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo Switch 2 is once again $399 at Woot for new customers, $419 for returning customers with code — save up to $50 while supplies last",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/nintendo-switch-2-is-once-again-usd399-at-woot-for-new-customers-usd419-for-returning-customers-with-code-save-up-to-usd50-while-supplies-last",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T00:33:25+00:00",
    "summary": "Get a brand new Nintendo Switch 2 for less."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-a-radeon-rx-9060-xt-16gb-upgrade-for-just-usd399-take-your-pick-from-four-attainable-options-at-newegg-now",
    "domain": "AI 算力 / 半导体",
    "title": "Get a Radeon RX 9060 XT 16GB upgrade for just $399 — take your pick from four attainable options at Newegg now",
    "url": "https://www.tomshardware.com/pc-components/get-a-radeon-rx-9060-xt-16gb-upgrade-for-just-usd399-take-your-pick-from-four-attainable-options-at-newegg-now",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T23:29:42+00:00",
    "summary": "The RAM price crunch has made affordable 16GB graphics cards an endangered species, but Newegg is offering a path to an affordable upgrade with four $399 RX 9060 XT 16GB options."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-the-fastest-8tb-gen4-ssd-around-for-less-with-this-wd-sn850x-deal-usd1199-sale-makes-it-the-cheapest-big-drive-around",
    "domain": "AI 算力 / 半导体",
    "title": "Get the fastest 8TB Gen4 SSD around for less with this WD SN850X deal — $1199 sale makes it the cheapest big drive around",
    "url": "https://www.tomshardware.com/pc-components/get-the-fastest-8tb-gen4-ssd-around-for-less-with-this-wd-sn850x-deal-usd1199-sale-makes-it-the-cheapest-big-drive-around",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T19:57:45+00:00",
    "summary": "Big SSDs often have the craziest prices in today's tight market, but if you need 8TB of space, you can get it for less with this WD SN850X deal."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/xbox/microsoft-increases-xbox-series-console-prices-for-the-third-time-in-two-years-kills-off-2tb-model-usd100-usd150-upswings-on-every-model",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft increases Xbox Series console prices for the third time in two years, kills off 2TB model — $100-$150 upswings on every model",
    "url": "https://www.tomshardware.com/video-games/xbox/microsoft-increases-xbox-series-console-prices-for-the-third-time-in-two-years-kills-off-2tb-model-usd100-usd150-upswings-on-every-model",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T18:29:56+00:00",
    "summary": "Microsoft increases Xbox Series console prices for the third time in two years — $100-$150 upswings on every model except the now-dead 2 TB version"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/epic-boss-tim-sweeney-blasts-steam-for-putting-ai-tags-on-games-says-move-is-irresponsible-of-valve",
    "domain": "AI 算力 / 半导体",
    "title": "Epic boss Tim Sweeney blasts Steam for putting AI tags on games — says move is ‘irresponsible of Valve’",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/epic-boss-tim-sweeney-blasts-steam-for-putting-ai-tags-on-games-says-move-is-irresponsible-of-valve",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T17:05:41+00:00",
    "summary": "The Epic executive said in an interview after unveiling Unreal Engine 6 that AI tools help make developers far more productive. Putting the AI tag on games discourage their use, especially as titles w"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/scalpers-circle-amds-ryzen-7-5800x3d-10th-anniversary-edition-asking-for-usd600-or-more-re-released-cpu-sees-inconsistent-inventory-on-release-day",
    "domain": "AI 算力 / 半导体",
    "title": "Scalpers circle AMD's Ryzen 7 5800X3D 10th Anniversary Edition, asking for $600 or more — re-released CPU sees inconsistent inventory on release day",
    "url": "https://www.tomshardware.com/pc-components/cpus/scalpers-circle-amds-ryzen-7-5800x3d-10th-anniversary-edition-asking-for-usd600-or-more-re-released-cpu-sees-inconsistent-inventory-on-release-day",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T16:58:05+00:00",
    "summary": "Scalpers are trying to capitalize on the release of the Ryzen 7 5800X3D 10th Anniversary Edition, asking nearly double the CPU's suggested retail price."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-up-to-45-percent-on-steelseries-headsets-keyboards-and-mice-arctic-nova-pro-headset-apex-pro-keyboards-aerox-5-mouse-and-more-are-on-deep-discounts-right-now",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to 45% on SteelSeries headsets, keyboards, and mice — Arctic Nova Pro headset, Apex Pro keyboards, Aerox 5 mouse, and more, are on deep discounts right now",
    "url": "https://www.tomshardware.com/pc-components/save-up-to-45-percent-on-steelseries-headsets-keyboards-and-mice-arctic-nova-pro-headset-apex-pro-keyboards-aerox-5-mouse-and-more-are-on-deep-discounts-right-now",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T16:36:11+00:00",
    "summary": "Take advantage of these Steelseries deals - up to 45% off includes Arctis gaming headsets and GameBuds to Apex Pro keyboards and Aerox mice, now is a great time to upgrade your gaming setup"
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/prime-day-gaming-monitor-deals-live-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Prime Day gaming monitor deals live 2026 — hot sales on the best monitors from Amazon, Newegg, Dell, Best Buy, and more",
    "url": "https://www.tomshardware.com/live/news/prime-day-gaming-monitor-deals-live-2026",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T16:34:18+00:00",
    "summary": "The best Amazon Prime Day 2026 monitor sales, live round-the-clock coverage of all the best deals."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-5800x3d-2026-cpu-review",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen 7 5800X3D re-review: Maxing out DDR4’s gaming potential",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-5800x3d-2026-cpu-review",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T16:25:37+00:00",
    "summary": "AMD has re-released the Ryzen 7 5800X3D to provide some relief from high DDR5 prices, so we’re re-reviewing the CPU to see how it stacks up to current options around the same price."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/b-and-hs-bundles-blowout-offers-32gb-of-ddr5-memory-for-around-usd250-save-on-multiple-bundles-including-ryzen-7-9850x3d-ddr5-and-a-motherboard",
    "domain": "AI 算力 / 半导体",
    "title": "B&H's RAM bundles blowout offers 32GB of DDR5 memory for around $250 — save on multiple bundles, including Ryzen 7 9850X3D, DDR5, and a motherboard",
    "url": "https://www.tomshardware.com/pc-components/b-and-hs-bundles-blowout-offers-32gb-of-ddr5-memory-for-around-usd250-save-on-multiple-bundles-including-ryzen-7-9850x3d-ddr5-and-a-motherboard",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T16:25:00+00:00",
    "summary": "B&amp;H has several bundles on sale right now, offering 32GB of DDR5 memory for around $250 with a motherboard and AMD's Ryzen 7 9850X3D."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/riot-vanguard-adds-an-on-demand-mode-that-stops-anti-cheat-loading-at-boot-on-secured-windows-11-pcs",
    "domain": "AI 算力 / 半导体",
    "title": "Riot Vanguard finally drops its controversial always-on requirement for anti-cheat — new on-demand mode requires a strict Windows 11 security stack",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/riot-vanguard-adds-an-on-demand-mode-that-stops-anti-cheat-loading-at-boot-on-secured-windows-11-pcs",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T16:23:48+00:00",
    "summary": "Riot Games has announced that it plans to let players stop its Vanguard anti-cheat from loading on startup."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/beat-apples-price-increases-on-new-macbooks-with-these-stellar-deals-that-can-save-you-up-to-usd500-big-sale-on-current-gen-pro-air-and-neo-models-avoid-new-price-hikes-with-extra-discounts-on-top",
    "domain": "AI 算力 / 半导体",
    "title": "Beat Apple's price increases on new MacBooks with these stellar deals that can save you up to $500 — big sale on current-gen Pro, Air, and Neo models, avoid new price hikes with extra discounts on top",
    "url": "https://www.tomshardware.com/laptops/macbooks/beat-apples-price-increases-on-new-macbooks-with-these-stellar-deals-that-can-save-you-up-to-usd500-big-sale-on-current-gen-pro-air-and-neo-models-avoid-new-price-hikes-with-extra-discounts-on-top",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T16:02:19+00:00",
    "summary": "Apple is raising MacBook pricing by hundreds of dollars, but these sale week deals are still live, so grab a bargain while you can."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/the-ai-tokenmaxxing-party-is-crashing-over-spiraling-costs-leaked-consulting-firm-audio-suggests-no-one-is-sure-how-to-measure-ai-effectiveness",
    "domain": "AI 算力 / 半导体",
    "title": "The AI tokenmaxxing party is crashing over spiraling costs — leaked consulting firm audio suggests no one is sure how to measure AI effectiveness",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/the-ai-tokenmaxxing-party-is-crashing-over-spiraling-costs-leaked-consulting-firm-audio-suggests-no-one-is-sure-how-to-measure-ai-effectiveness",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T15:27:41+00:00",
    "summary": "A recording from a meeting at consulting firm Accenture has raised concerns over how much companies are spending on AI. As companies bullish on AI rush to take advantage of the technology, solutions t"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/asus-beta-bios-updates-restore-ryzen-9000-memory-encryption-ahead-of-amds-july-timeline-tsme-returns-to-select-am5-boards-after-silent-backlash-over-removal",
    "domain": "AI 算力 / 半导体",
    "title": "Asus beta BIOS updates restore Ryzen 9000 memory encryption ahead of AMD’s July timeline — TSME returns to select AM5 boards after silent backlash over removal",
    "url": "https://www.tomshardware.com/pc-components/cpus/asus-beta-bios-updates-restore-ryzen-9000-memory-encryption-ahead-of-amds-july-timeline-tsme-returns-to-select-am5-boards-after-silent-backlash-over-removal",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T14:54:06+00:00",
    "summary": "Asus has released beta BIOS updates for several X870, B850, and X670 AM5 motherboards, restoring Transparent Secure Memory Encryption support for non-Pro Ryzen 9000 CPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/want-an-rtx-5070-ti-heres-where-to-get-one-for-usd899-dont-pay-retail-and-save-usd220-today",
    "domain": "AI 算力 / 半导体",
    "title": "Want an RTX 5070 Ti? Here’s where to get one for $899 — don't pay retail and save $220 today",
    "url": "https://www.tomshardware.com/pc-components/gpus/want-an-rtx-5070-ti-heres-where-to-get-one-for-usd899-dont-pay-retail-and-save-usd220-today",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T14:28:00+00:00",
    "summary": "Newegg has the Gigabyte GeForce RTX 5070 Ti Eagle OC Ice SFF 16G graphics card up for sale for $899 after direct discounts."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/these-15-under-usd50-gadgets-have-upgraded-my-tech-life-and-theyre-all-on-sale",
    "domain": "AI 算力 / 半导体",
    "title": "These 15 under-$50 gadgets have upgraded my tech life, and they're all on sale",
    "url": "https://www.tomshardware.com/peripherals/these-15-under-usd50-gadgets-have-upgraded-my-tech-life-and-theyre-all-on-sale",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T14:27:33+00:00",
    "summary": "From electric screwdrivers to high-res webcams, these are inexpensive game-changers."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/ram-crisis-bites-apple-as-unprecedented-mac-and-ipad-price-rises-arrive-cheapest-macbook-pro-price-hiked-by-usd400-to-usd1-999",
    "domain": "AI 算力 / 半导体",
    "title": "RAM crisis bites Apple as unprecedented Mac and iPad price rises arrive — cheapest MacBook Pro price hiked by $400 to $1,999",
    "url": "https://www.tomshardware.com/laptops/macbooks/ram-crisis-bites-apple-as-unprecedented-mac-and-ipad-price-rises-arrive-cheapest-macbook-pro-price-hiked-by-usd400-to-usd1-999",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T13:59:58+00:00",
    "summary": "Apple has made the unprecedented decision to hike the prices of all its current computers and tablets with some entry-level model prices up as much as $500."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-claims-that-chinas-alibaba-illicitly-distilled-its-models-from-april-to-june-2026-says-effort-involved-25-000-fake-accounts-and-28-8-million-exchanges-on-claude",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic claims that China's Alibaba used 25,000 fake accounts and 28.8 million exchanges to illicitly 'distill' its Claude model — violations occurred from April to June 2026",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-claims-that-chinas-alibaba-illicitly-distilled-its-models-from-april-to-june-2026-says-effort-involved-25-000-fake-accounts-and-28-8-million-exchanges-on-claude",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T13:26:04+00:00",
    "summary": "AI tech giant Alibaba, often considered as the Amazon of China, is being accused by Anthropic for using Claude to train its AI models. The American AI startup claimed that it traced over 25,000 accoun"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/today-only-you-can-snag-a-37-inch-4k-samsung-monitor-for-just-usd249-b-and-h-offers-up-a-big-productivity-screen-for-50-percent-off-in-a-one-day-deal",
    "domain": "AI 算力 / 半导体",
    "title": "Today only, you can snag a 37-inch 4K Samsung monitor for just $249 – B&H offers up a big productivity screen for 50% off in a one-day deal",
    "url": "https://www.tomshardware.com/pc-components/today-only-you-can-snag-a-37-inch-4k-samsung-monitor-for-just-usd249-b-and-h-offers-up-a-big-productivity-screen-for-50-percent-off-in-a-one-day-deal",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T12:48:33+00:00",
    "summary": "B&amp;H is selling a 37-inch 4K Samsung monitor for half off, or just $249, today only."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/qualcomm-plans-china-specific-data-center-chips-built-to-clear-us-export-limits",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm plans China-specific data center chips — new Dragonfly lineup will include nerfed AI accelerators that comply with export thresholds",
    "url": "https://www.tomshardware.com/tech-industry/qualcomm-plans-china-specific-data-center-chips-built-to-clear-us-export-limits",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T12:45:22+00:00",
    "summary": "Qualcomm has announced that it will bring all four of its Dragonfly data center product lines to China."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-headsets/hyperx-cloud-stinger-3-wireless-review",
    "domain": "AI 算力 / 半导体",
    "title": "HyperX Cloud Stinger 3 Wireless Headset Review: 80 hours and under $100",
    "url": "https://www.tomshardware.com/peripherals/gaming-headsets/hyperx-cloud-stinger-3-wireless-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T12:10:00+00:00",
    "summary": "The HyperX Cloud Stinger 3 Wireless is an over-ear wireless gaming headset with 50mm dynamic drivers, a flip-to-mute boom mic, and up to 80 hours of battery life — all for under $100."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/micron-inks-long-term-supply-agreements-worth-usd100-billion-says-it-has-no-idea-when-ram-crisis-will-end",
    "domain": "AI 算力 / 半导体",
    "title": "Micron inks long-term supply agreements worth $100 billion — says it has no idea when RAM crisis will end",
    "url": "https://www.tomshardware.com/pc-components/dram/micron-inks-long-term-supply-agreements-worth-usd100-billion-says-it-has-no-idea-when-ram-crisis-will-end",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T12:09:58+00:00",
    "summary": "Micron has signed 16 LTAs with various customers to supply DRAM and NAND worth $100 billion."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/steam-machines-will-only-come-with-one-16gb-stick-of-ram-company-may-change-this-to-two-8gb-sticks-in-the-future-but-the-first-batch-of-consoles-is-limited-to-single-channel-memory",
    "domain": "AI 算力 / 半导体",
    "title": "Steam Machines will only come with one 16GB stick of RAM — company may change this to two 8GB sticks in the future, but the first batch of consoles is limited to single-channel memory",
    "url": "https://www.tomshardware.com/video-games/console-gaming/steam-machines-will-only-come-with-one-16gb-stick-of-ram-company-may-change-this-to-two-8gb-sticks-in-the-future-but-the-first-batch-of-consoles-is-limited-to-single-channel-memory",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T10:33:57+00:00",
    "summary": "Valve confirmed to Gamers Nexus that the first batch of Steam Machines will only have one 16GB RAM stick. This would have a negative effect on the console's performance, but the company likely did thi"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/qualcomm-reveals-hbc-near-memory-ai-architecture-ai250-and-ai350-accelerators-touts-6x-higher-bandwidth-per-watt-compared-to-hbm-200x-capacity-compared-to-on-chip-sram",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm reveals HBC near-memory AI architecture, AI250 and AI350 accelerators — touts 6x higher bandwidth-per-watt compared to HBM, 200x capacity compared to on-chip SRAM",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/qualcomm-reveals-hbc-near-memory-ai-architecture-ai250-and-ai350-accelerators-touts-6x-higher-bandwidth-per-watt-compared-to-hbm-200x-capacity-compared-to-on-chip-sram",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T10:00:00+00:00",
    "summary": "Qualcomm unveils HBC near-memory AI architecture, claims it has broken the memory wall."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/back-in-stock-corsairs-tiny-touchscreen-discount-returns-during-prime-week-xeneon-edge-14-5-inch-lcd-touchscreen-hits-usd199-99-agian",
    "domain": "AI 算力 / 半导体",
    "title": "Back in stock! Corsair's tiny touchscreen discount returns during Prime Week — Xeneon Edge 14.5-inch LCD touchscreen hits $199.99 agian",
    "url": "https://www.tomshardware.com/pc-components/back-in-stock-corsairs-tiny-touchscreen-discount-returns-during-prime-week-xeneon-edge-14-5-inch-lcd-touchscreen-hits-usd199-99-agian",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T08:45:55+00:00",
    "summary": "Get 20% off the Corsair Xeneon Edge 14.5-inch LCD Touchscreen."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/grand-theft-auto-6-preorders-begin-tonight-at-midnight-local-time-in-the-us-heres-where-to-buy-get-yours-now-its-in-the-garage-and-ready-to-roll",
    "domain": "AI 算力 / 半导体",
    "title": "Grand Theft Auto 6 preorders begin tonight at midnight local time in the US; here's where to buy — get yours now, it's in the garage and ready to roll",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/grand-theft-auto-6-preorders-begin-tonight-at-midnight-local-time-in-the-us-heres-where-to-buy-get-yours-now-its-in-the-garage-and-ready-to-roll",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T01:07:43+00:00",
    "summary": "The preorder pages for GTA will drop at midnight local time in the US tonight, and you have both the Standard and Ultimate editions at your disposal."
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
    "id": "rss:https://www.theverge.com/gadgets/949350/amazon-prime-day-sale-best-apple-deals-2026",
    "domain": "大厂 AI 动态",
    "title": "This year’s Prime Day deals on Apple products are the best I’ve seen",
    "url": "https://www.theverge.com/gadgets/949350/amazon-prime-day-sale-best-apple-deals-2026",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T23:04:23+00:00",
    "summary": "Amazon&#8217;s Prime Day is now in its third day, and whether you&#8217;re looking for a new pair of wireless earbuds or a smartwatch, there’s a good chance you’ll find a discount. The Apple Watch Ser"
  },
  {
    "id": "rss:https://www.theverge.com/tech/957450/android-17-foldable-gaming-mode-virtual-controller",
    "domain": "大厂 AI 动态",
    "title": "Android 17&#8217;s new foldable gaming mode could make flippy phones more fun",
    "url": "https://www.theverge.com/tech/957450/android-17-foldable-gaming-mode-virtual-controller",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T22:33:54+00:00",
    "summary": "Android 17 is getting a dedicated gaming mode for foldables that will put a virtual gamepad with touch controls on half of your screen to theoretically make it easier to play games. With foldable gami"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/957422/youtube-shorts-update-tiktok",
    "domain": "大厂 AI 动态",
    "title": "YouTube updates Shorts to make it even more like TikTok",
    "url": "https://www.theverge.com/streaming/957422/youtube-shorts-update-tiktok",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T22:08:30+00:00",
    "summary": "YouTube is adding even more TikTok-like features to Shorts, including a new \"clear screen\" mode that removes the icons and text from the video you're watching. In a blog post on Thursday, YouTube says"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/957372/openai-will-delay-gpt-5-6-after-trump-administration-request",
    "domain": "大厂 AI 动态",
    "title": "OpenAI will delay GPT-5.6 after Trump administration request",
    "url": "https://www.theverge.com/ai-artificial-intelligence/957372/openai-will-delay-gpt-5-6-after-trump-administration-request",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T21:57:06+00:00",
    "summary": "The Trump administration, apprehensive of potential security issues, has reportedly asked OpenAI to stagger the release of its next big-ticket model, GPT-5.6. The Information reported that OpenAI CEO "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/957338/framework-laptop-13-pro-ssd-price-cpu",
    "domain": "大厂 AI 动态",
    "title": "Framework has good news and bad news",
    "url": "https://www.theverge.com/gadgets/957338/framework-laptop-13-pro-ssd-price-cpu",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T21:23:47+00:00",
    "summary": "Thanks to the component crisis, it's a bad time to want a new computer. But if you are waiting on a preorder for the Framework Laptop 13 Pro - which Framework's CEO has called the \"MacBook Pro for Lin"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/957170/xbox-series-s-x-prime-day-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Score a discounted Xbox console before the prices jump",
    "url": "https://www.theverge.com/gadgets/957170/xbox-series-s-x-prime-day-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T20:18:47+00:00",
    "summary": "Microsoft announced today that the price of all Xbox models will rise in August, the second time in less than a year as memory prices continue to wreak havoc on every industry from cars to computing. "
  },
  {
    "id": "rss:https://www.theverge.com/tech/956456/instagram-for-tv-youtube-microdramas-longform-video",
    "domain": "大厂 AI 动态",
    "title": "Instagram wants to monopolize your attention",
    "url": "https://www.theverge.com/tech/956456/instagram-for-tv-youtube-microdramas-longform-video",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T20:10:24+00:00",
    "summary": "This week, Instagram launched a series of new features for its smart TV app that are all designed to get people to spend more time on the platform through the biggest screens in their homes. In additi"
  },
  {
    "id": "rss:https://www.theverge.com/tech/956950/ram-crisis-apple-price-increase",
    "domain": "大厂 AI 动态",
    "title": "RAMageddon just got extremely real",
    "url": "https://www.theverge.com/tech/956950/ram-crisis-apple-price-increase",
    "source": "Allison Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T20:00:00+00:00",
    "summary": "As far as prices go, Apple is kind of a reverse canary in the coal mine. With its famously generous margins and immense purchasing volume, it can afford to ride out price fluctuations in its supply ch"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/951081/robot-vacuum-mop-deals-amazon-prime-day-2026",
    "domain": "大厂 AI 动态",
    "title": "The 16 best robot vacuum deals available during Prime Day",
    "url": "https://www.theverge.com/gadgets/951081/robot-vacuum-mop-deals-amazon-prime-day-2026",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T18:47:26+00:00",
    "summary": "If you&#8217;ve been wanting to buy a robot vacuum but have been put off by how much it can cost to get a good one, now is not a bad time to start looking. We&#8217;re now on day three of Prime Day, a"
  },
  {
    "id": "rss:https://www.theverge.com/tech/957151/ram-crisis-component-shortage-prices-computer-apple-microsoft-valve",
    "domain": "大厂 AI 动态",
    "title": "It&#8217;s a bad time to want a new computer",
    "url": "https://www.theverge.com/tech/957151/ram-crisis-component-shortage-prices-computer-apple-microsoft-valve",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T18:20:17+00:00",
    "summary": "It's not exactly surprising that RAMaggeddon is making new tech hardware really expensive. But if you've been in the market for things like a new computer or tablet, this week has been filled with sti"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/the-white-house-is-asking-openai-to-slow-roll-the-release-of-its-new-model-over-safety-concerns/",
    "domain": "大厂 AI 动态",
    "title": "The White House is asking OpenAI to slow roll the release of its new model over safety concerns",
    "url": "https://techcrunch.com/2026/06/25/the-white-house-is-asking-openai-to-slow-roll-the-release-of-its-new-model-over-safety-concerns/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T23:34:39+00:00",
    "summary": "OpenAI reportedly plans to share its newest model, GPT 5.6, with a select group of partners instead of with the broader public. The reason: the Trump administration told it to."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/youtube-shorts-are-getting-even-shorter-with-an-update-that-lets-you-double-the-playback-speed/",
    "domain": "大厂 AI 动态",
    "title": "YouTube Shorts are getting even shorter with an update that lets you double the playback speed",
    "url": "https://techcrunch.com/2026/06/25/youtube-shorts-are-getting-even-shorter-with-an-update-that-lets-you-double-the-playback-speed/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T22:02:12+00:00",
    "summary": "YouTube Shorts is getting a makeover."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/patronus-ai-lands-50m-to-build-digital-worlds-that-stress-test-ai-agents/",
    "domain": "大厂 AI 动态",
    "title": "Patronus AI lands $50M to build ‘digital worlds’ that stress-test AI agents",
    "url": "https://techcrunch.com/2026/06/25/patronus-ai-lands-50m-to-build-digital-worlds-that-stress-test-ai-agents/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T20:19:25+00:00",
    "summary": "Agent-testing startup Patronus AI, founded by former Meta AI researchers, is experiencing nearly insatiable demand, its investor says."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/polymarket-says-hackers-stole-users-funds/",
    "domain": "大厂 AI 动态",
    "title": "Polymarket says hackers stole users’ funds",
    "url": "https://techcrunch.com/2026/06/25/polymarket-says-hackers-stole-users-funds/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T19:58:46+00:00",
    "summary": "The prediction market giant Polymarket said it's refunding users who had funds stolen due to a third-party breach."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/xbox-follows-apple-with-price-increases/",
    "domain": "大厂 AI 动态",
    "title": "Xbox follows Apple with price increases",
    "url": "https://techcrunch.com/2026/06/25/xbox-follows-apple-with-price-increases/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T19:39:55+00:00",
    "summary": "The company says the increases are being driven by rising memory and console storage prices, with costs more than 2.5x higher than previous levels."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/notion-mail-shuts-down-amid-agent-takeover/",
    "domain": "大厂 AI 动态",
    "title": "Notion Mail shuts down amid agent takeover",
    "url": "https://techcrunch.com/2026/06/25/notion-mail-shuts-down-amid-agent-takeover/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T19:14:46+00:00",
    "summary": "The company said it is discontinuing its email inbox in favor of its AI agent offering as users are increasingly handing over the reins of their email to the agents."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/a16z-backed-base-power-is-offering-cheaper-electricity-to-the-power-grid-that-needs-it-most/",
    "domain": "大厂 AI 动态",
    "title": "a16z-backed Base Power is offering cheaper electricity to the power grid that needs it most",
    "url": "https://techcrunch.com/2026/06/25/a16z-backed-base-power-is-offering-cheaper-electricity-to-the-power-grid-that-needs-it-most/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T17:52:05+00:00",
    "summary": "Base Power is skipping the PJM's troubled interconnection queue by placing its batteries at people's homes, offering backup services in exchange."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/anthropics-claude-is-winning-over-paid-consumers-a-market-owned-by-chatgpt/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s Claude is winning over paid consumers, a market owned by ChatGPT",
    "url": "https://techcrunch.com/2026/06/25/anthropics-claude-is-winning-over-paid-consumers-a-market-owned-by-chatgpt/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T17:38:27+00:00",
    "summary": "Despite ChatGPT's commanding market lead, consumers who pay for AI have been increasingly choosing Anthropic's Claude, data shows."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/general-intuitions-2-3b-bet-that-video-games-can-train-ai-agents-for-the-real-world/",
    "domain": "大厂 AI 动态",
    "title": "General Intuition’s $2.3B bet that video games can train AI agents for the real world",
    "url": "https://techcrunch.com/2026/06/25/general-intuitions-2-3b-bet-that-video-games-can-train-ai-agents-for-the-real-world/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T16:55:00+00:00",
    "summary": "General Intuition has raised $320 million to scale AI trained on millions of hours of gameplay, betting action data can help AI develop something closer to human intuition."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/databricks-former-ai-chief-thinks-he-can-cut-ais-power-bill-by-1000x/",
    "domain": "大厂 AI 动态",
    "title": "Databricks’ former AI chief thinks he can cut AI’s power bill by 1,000x",
    "url": "https://techcrunch.com/2026/06/25/databricks-former-ai-chief-thinks-he-can-cut-ais-power-bill-by-1000x/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T16:48:11+00:00",
    "summary": "Un-0 is an image-generation system tool that shows for the first time how the company's technology can replicate conventional AI systems."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/hacked-klue-says-criminals-are-deleting-stolen-customer-data-but-now-other-hackers-are-making-threats/",
    "domain": "大厂 AI 动态",
    "title": "Hacked Klue says criminals are deleting stolen customer data, but now other hackers are making threats",
    "url": "https://techcrunch.com/2026/06/25/hacked-klue-says-criminals-are-deleting-stolen-customer-data-but-now-other-hackers-are-making-threats/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T16:40:15+00:00",
    "summary": "Market research company Klue told customers that it believes the hacking group that stole their data is now deleting it. The company, however, warned about a second group of hackers wanting ransom."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/parker-conrad-knows-which-employees-are-worth-their-ai-spend-and-says-rippling-can-help-you-too/",
    "domain": "大厂 AI 动态",
    "title": "Rippling now wants to be your entire data stack",
    "url": "https://techcrunch.com/2026/06/25/parker-conrad-knows-which-employees-are-worth-their-ai-spend-and-says-rippling-can-help-you-too/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T16:00:00+00:00",
    "summary": "\"There were employees doing things like, 'Claude is so helpful for me — it analyzes my calendar and my email and puts together a plan for me,'\" he says. \"That person was spending at a run rate of $30,"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/google-finance-gets-a-dedicated-app-for-android/",
    "domain": "大厂 AI 动态",
    "title": "Google Finance gets a dedicated app for Android",
    "url": "https://techcrunch.com/2026/06/25/google-finance-gets-a-dedicated-app-for-android/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T16:00:00+00:00",
    "summary": "Users will be able to access their watchlists, real-time market data, live financial news, and Google's AI-powered \"Key Moments\" feature, which explains why stocks moved."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/netris-raises-15m-series-a-from-a16z-to-help-ai-neoclouds-go-live-faster/",
    "domain": "大厂 AI 动态",
    "title": "Netris raises $15M Series A from a16z to help AI neoclouds go live faster",
    "url": "https://techcrunch.com/2026/06/25/netris-raises-15m-series-a-from-a16z-to-help-ai-neoclouds-go-live-faster/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T14:55:38+00:00",
    "summary": "Netris provides software that runs on network switches, and offers a platform that helps neocloud operators reduce the time it takes to go live."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/trump-admin-bars-polestar-from-selling-its-new-evs-in-the-us/",
    "domain": "大厂 AI 动态",
    "title": "Trump administration bars Polestar from selling its new EVs in the US",
    "url": "https://techcrunch.com/2026/06/25/trump-admin-bars-polestar-from-selling-its-new-evs-in-the-us/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T14:55:25+00:00",
    "summary": "The Department of Commerce declined to give the Chinese-owned automaker a special authorization to keep selling EVs in the U.S."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/apple-raises-mac-and-ipad-prices-spares-iphone-for-now/",
    "domain": "大厂 AI 动态",
    "title": "Apple raises Mac and iPad prices, spares iPhone for now",
    "url": "https://techcrunch.com/2026/06/25/apple-raises-mac-and-ipad-prices-spares-iphone-for-now/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T14:52:35+00:00",
    "summary": "Apple raises prices of MacBook Air and Pro along with iPad Air and Pro."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/2-days-left-to-save-up-to-190-join-1000-founders-and-investors-at-techcrunch-founder-summit/",
    "domain": "大厂 AI 动态",
    "title": "2 days left to save up to $190: Join 1,000+ founders and investors at TechCrunch Founder Summit",
    "url": "https://techcrunch.com/2026/06/25/2-days-left-to-save-up-to-190-join-1000-founders-and-investors-at-techcrunch-founder-summit/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T14:00:00+00:00",
    "summary": "Two days left to lock in your spot at TechCrunch Founder Summit 2026 and save up to $190 before Early Bird rates expire on June 26 at 11:59 p.m. PT. Register today."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/trump-admin-proposes-axing-brake-pedal-requirement-for-avs-in-a-boost-for-tesla/",
    "domain": "大厂 AI 动态",
    "title": "Trump administration proposes axing brake-pedal requirement for AVs in a boost for Tesla",
    "url": "https://techcrunch.com/2026/06/25/trump-admin-proposes-axing-brake-pedal-requirement-for-avs-in-a-boost-for-tesla/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T13:58:05+00:00",
    "summary": "The Department of Transportation wants to remove the brake-pedal requirement for vehicles \"designed to be driven exclusively by automated driving systems.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/adobe-acquires-image-and-video-enhancement-tool-maker-topaz-labs/",
    "domain": "大厂 AI 动态",
    "title": "Adobe acquires image and video enhancement tool maker Topaz Labs",
    "url": "https://techcrunch.com/2026/06/25/adobe-acquires-image-and-video-enhancement-tool-maker-topaz-labs/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T13:30:00+00:00",
    "summary": "Adobe said that it will integrate Topaz Labs' tools across its apps."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/25/amazon-ups-india-bet-with-fresh-13b-ai-infrastructure-investment/",
    "domain": "大厂 AI 动态",
    "title": "Amazon ups India bet with fresh $13B AI infrastructure investment",
    "url": "https://techcrunch.com/2026/06/25/amazon-ups-india-bet-with-fresh-13b-ai-infrastructure-investment/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T12:00:38+00:00",
    "summary": "Amazon’s latest India investment comes as global tech companies race to expand AI infrastructure in the country."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-figma-ceo-dylan-field-about-design-and-ai/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with Figma CEO Dylan Field About Design and AI",
    "url": "https://stratechery.com/2026/an-interview-with-figma-ceo-dylan-field-about-design-and-ai/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T10:00:00+00:00",
    "summary": "An interview with Figma CEO Dylan Field about building Figma, and why he believes AI gives the company a tailwind."
  },
  {
    "id": "rss:https://stratechery.com/2026/my-vibe-coding-adventure-the-app-and-the-experience-ten-takeaways/",
    "domain": "大厂 AI 动态",
    "title": "My Vibe Coding Adventure, The App and the Experience, Ten Takeaways",
    "url": "https://stratechery.com/2026/my-vibe-coding-adventure-the-app-and-the-experience-ten-takeaways/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T10:00:00+00:00",
    "summary": "My experience and reflections on vibe coding an app that I plan on actually using regularly."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/microsoft-adds-another-year-to-windows-10-extended-update-program/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft adds another year to Windows 10 extended update program",
    "url": "https://arstechnica.com/gadgets/2026/06/microsoft-adds-another-year-to-windows-10-extended-update-program/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T20:24:09+00:00",
    "summary": "About a quarter of PCs are still running Microsoft's previous operating system."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/fcc-may-kill-2b-program-that-connects-schools-and-libraries-to-internet/",
    "domain": "大厂 AI 动态",
    "title": "FCC may kill $2B program that connects schools and libraries to Internet",
    "url": "https://arstechnica.com/tech-policy/2026/06/fcc-may-kill-2b-program-that-connects-schools-and-libraries-to-internet/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T20:01:08+00:00",
    "summary": "Carr cites screen time concerns, is accused of trying to be \"the nation’s parent.\""
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/notion-killing-skiff-influenced-email-app-since-most-users-use-ai-agents-instead/",
    "domain": "大厂 AI 动态",
    "title": "Notion killing Skiff-influenced email app since most users use AI agents instead",
    "url": "https://arstechnica.com/gadgets/2026/06/notion-killing-skiff-influenced-email-app-since-most-users-use-ai-agents-instead/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T19:04:57+00:00",
    "summary": "Notion is \"going all in on using agents to run your inbox.\""
  },
  {
    "id": "rss:https://arstechnica.com/google/2026/06/google-finance-finally-gets-a-mobile-app-as-ai-powered-overhaul-leaves-beta/",
    "domain": "大厂 AI 动态",
    "title": "Google finally releases a Finance Android app, promises iOS version later in 2026",
    "url": "https://arstechnica.com/google/2026/06/google-finance-finally-gets-a-mobile-app-as-ai-powered-overhaul-leaves-beta/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T18:38:51+00:00",
    "summary": "It took 20 years, but the Finance app arrives just in time to be packed full of AI."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/anthropic-claims-alibaba-defied-trump-to-attack-claude-and-steal-capabilities/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic says Alibaba must be punished for largest Claude cloning attack",
    "url": "https://arstechnica.com/tech-policy/2026/06/anthropic-claims-alibaba-defied-trump-to-attack-claude-and-steal-capabilities/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T18:01:48+00:00",
    "summary": "Alibaba allegedly used 25,000 accounts to mine Claude over 28.8 million exchanges."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/planet-orbits-so-close-to-its-star-that-their-magnetic-fields-connect/",
    "domain": "大厂 AI 动态",
    "title": "Planet orbits so close to its star that their magnetic fields connect",
    "url": "https://arstechnica.com/science/2026/06/planet-orbits-so-close-to-its-star-that-their-magnetic-fields-connect/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T18:00:39+00:00",
    "summary": "At the right point of the orbit and stellar cycle, the star's chromosphere brightens."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/06/feds-deny-polestar-authorization-to-sell-cars-in-us-from-model-year-2027/",
    "domain": "大厂 AI 动态",
    "title": "Feds deny Polestar authorization to sell cars in US from model year 2027",
    "url": "https://arstechnica.com/cars/2026/06/feds-deny-polestar-authorization-to-sell-cars-in-us-from-model-year-2027/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T14:40:23+00:00",
    "summary": "Unlike with Volvo, there will be no authorization for Polestar to sell its cars here."
  },
  {
    "id": "rss:https://arstechnica.com/apple/2026/06/apple-ratchets-up-prices-blames-the-cost-of-memory/",
    "domain": "大厂 AI 动态",
    "title": "Apple ratchets up prices, blames the cost of memory",
    "url": "https://arstechnica.com/apple/2026/06/apple-ratchets-up-prices-blames-the-cost-of-memory/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T14:14:37+00:00",
    "summary": "Some Macs are hundreds of dollars more expensive today than yesterday."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/the-sad-inevitability-of-europes-heat-wave/",
    "domain": "大厂 AI 动态",
    "title": "The \"sad inevitability\" of Europe's heat wave",
    "url": "https://arstechnica.com/science/2026/06/the-sad-inevitability-of-europes-heat-wave/",
    "source": "Lauren Dalban, Inside Climate News",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T13:54:46+00:00",
    "summary": "Europeans are baking under their second heat wave of the summer."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/new-effort-will-get-genome-sequences-for-entire-endangered-species-list/",
    "domain": "大厂 AI 动态",
    "title": "New effort will get genome sequences for entire Endangered Species list",
    "url": "https://arstechnica.com/science/2026/06/new-effort-will-get-genome-sequences-for-entire-endangered-species-list/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T13:40:34+00:00",
    "summary": "Colossal Biosciences will be biobanking tissues from all of them as well."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/every-homo-naledi-we-know-of-is-female-and-the-implications-are-fascinating/",
    "domain": "大厂 AI 动态",
    "title": "Every Homo naledi we know of is female, and the implications are fascinating",
    "url": "https://arstechnica.com/science/2026/06/every-homo-naledi-we-know-of-is-female-and-the-implications-are-fascinating/",
    "source": "Kiona N. Smith",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T13:28:54+00:00",
    "summary": "\"There is no natural explanation,\" says paleoanthropologist John Hawks."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/ibm-claims-worlds-first-sub-1-nanometer-chip-technology/",
    "domain": "大厂 AI 动态",
    "title": "IBM claims world’s first sub-1 nanometer chip technology",
    "url": "https://arstechnica.com/gadgets/2026/06/ibm-claims-worlds-first-sub-1-nanometer-chip-technology/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-25T10:00:55+00:00",
    "summary": "IBM’s nanostack transistors could boost chip performance or energy efficiency."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/06/grand-theft-auto-vi-will-cost-80-without-a-physical-disc/",
    "domain": "大厂 AI 动态",
    "title": "Hotly anticipated Grand Theft Auto VI will cost more than other AAA games",
    "url": "https://arstechnica.com/gaming/2026/06/grand-theft-auto-vi-will-cost-80-without-a-physical-disc/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T22:47:03+00:00",
    "summary": "GTA6 might be an outlier, though—at least for now."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/openai-and-broadcom-announce-chip-designed-for-llm-inference-at-scale/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI and Broadcom announce chip designed for LLM inference at scale",
    "url": "https://arstechnica.com/gadgets/2026/06/openai-and-broadcom-announce-chip-designed-for-llm-inference-at-scale/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T22:28:18+00:00",
    "summary": "The silicon race is heating up amid the struggle to keep up with demand."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/analysis-finds-the-exploration-programs-nasa-recently-canceled-were-running-way-late/",
    "domain": "大厂 AI 动态",
    "title": "13 years and $500 million for a stage adapter? Report justifies NASA cancellations.",
    "url": "https://arstechnica.com/space/2026/06/analysis-finds-the-exploration-programs-nasa-recently-canceled-were-running-way-late/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T21:41:03+00:00",
    "summary": "\"Contract values for these efforts ballooned from nearly $2.8 billion to $5.9 billion.\""
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/06/us-ends-hantavirus-outbreak-response-with-no-answers-on-draconian-quarantines/",
    "domain": "大厂 AI 动态",
    "title": "US ends hantavirus outbreak response with no answers on draconian quarantines",
    "url": "https://arstechnica.com/health/2026/06/us-ends-hantavirus-outbreak-response-with-no-answers-on-draconian-quarantines/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T21:28:39+00:00",
    "summary": "We still don't know why RFK Jr. overruled CDC expert to order strict quarantines."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/06/one-two-punch-delivered-in-global-operation-disrupts-cybercrime-assembly-line/",
    "domain": "大厂 AI 动态",
    "title": "One-two punch delivered in global operation disrupts cybercrime \"assembly line\"",
    "url": "https://arstechnica.com/security/2026/06/one-two-punch-delivered-in-global-operation-disrupts-cybercrime-assembly-line/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T21:03:34+00:00",
    "summary": "\"Operation Endgame\" simultaneously disrupts two widely used crime tools."
  },
  {
    "id": "rss:https://arstechnica.com/features/2026/06/we-take-a-ride-in-slates-24950-electric-pickup/",
    "domain": "大厂 AI 动态",
    "title": "Underpromise, overdeliver? Hands-on with the $24,950 Slate auto.",
    "url": "https://arstechnica.com/features/2026/06/we-take-a-ride-in-slates-24950-electric-pickup/",
    "source": "Roberto Baldwin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T20:28:07+00:00",
    "summary": "It has 205 miles of bare-bones range."
  },
  {
    "id": "wscn:3775572",
    "domain": "股票",
    "title": "“华尔街之王”杰米戴蒙接班人之争：这位交易员出身的黑马成头号候选人",
    "url": "https://wallstreetcn.com/articles/3775572",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T06:57:47+00:00",
    "summary": "摩根大通启动权力交接，董事会将Troy Rohrbaugh与Doug Petno同时擢升为联席总裁，确立接替杰米·戴蒙的两人赛制。曾被视为头号热门的Marianne Lake宣告出局退休，而交易员出身、此前几乎没有消费者业务经验的Rohrbaugh，因被调任主管消费者及社区银行业务，意外跃升为领跑者。"
  },
  {
    "id": "wscn:3775589",
    "domain": "股票",
    "title": "内存涨价反噬终端需求！苹果涨价+OpenAI IPO推迟引爆亚洲芯片股崩盘",
    "url": "https://wallstreetcn.com/articles/3775589",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T06:50:40+00:00",
    "summary": "苹果和微软周四因存储短缺同日宣布涨价，叠加OpenAI考虑推迟IPO，周五亚洲科技股遭猛烈抛售。市场正在重新评估此前的交易逻辑：内存价格上涨带来的芯片股利润扩张，是否正在以压制终端消费需求为代价？AI硬件投资叙事面临新的考验。"
  },
  {
    "id": "wscn:3775587",
    "domain": "股票",
    "title": "联想：内存涨价是“新常态”，DRAM和NAND高价将持续至2030年后",
    "url": "https://wallstreetcn.com/articles/3775587",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T06:13:22+00:00",
    "summary": "告别廉价数码时代！联想发布重磅预警：DRAM和NAND闪存价格已进入结构性上涨周期，即便主要厂商持续扩产，价格也极难回落至2025年初水平。高成本正全面向下传导。未来PC、手机等全品类终端面临持续涨价压力，价格上涨最终将成为2030年及以后的“新常态”。"
  },
  {
    "id": "wscn:3775266",
    "domain": "股票",
    "title": "日本酸素官宣提价30%开启新一轮涨价潮，氦气正升格为半导体产业链“卡脖子”级别战略物资",
    "url": "https://wallstreetcn.com/premium/articles/3775266?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T05:56:49+00:00",
    "summary": "日本巨头宣布全面调涨氦气产品售价30%，再次印证全球氦气紧缺背景下，氦气已进入卖方市场。"
  },
  {
    "id": "wscn:3775571",
    "domain": "股票",
    "title": "科技股回调拖累全球市场，韩股熔断，三星电子、SK海力士跌超4%，黄金持稳于4000美元",
    "url": "https://wallstreetcn.com/articles/3775571",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T05:52:44+00:00",
    "summary": "作为OpenAI重要日本股东的软银集团股价一度暴跌14%；韩股一度重挫近9%并触发今周第二次交易暂停，随后跌幅收窄至不足6%；日经225指数下跌约5%；亚洲股票基准指数整体下挫3.2%。黄金维持在每盎司4000美元附近，白银下跌2.5%。"
  },
  {
    "id": "wscn:3775586",
    "domain": "股票",
    "title": "对话朱江明：零跑造了台自己的阿尔法",
    "url": "https://wallstreetcn.com/articles/3775586",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T05:41:24+00:00",
    "summary": "把高端 MPV 做成走量生意。"
  },
  {
    "id": "wscn:3775584",
    "domain": "股票",
    "title": "逃离“韩国折价”：SK海力士之后，三星也酝酿赴美上市？",
    "url": "https://wallstreetcn.com/articles/3775584",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T05:18:12+00:00",
    "summary": "韩国半导体双雄正加速布局美国资本市场，以期通过吸引全球被动资金流入消解“韩国折价”。继SK海力士宣布下月登陆纳斯达克发行ADR后，三星电子赴美挂牌的传闻也在韩国证券业内迅速发酵，海外投资者关注度远超预期，市场普遍将其视为推动股价上涨的强力催化剂。"
  },
  {
    "id": "wscn:3775583",
    "domain": "股票",
    "title": "汇添富孙浩、博时李庆阳最新发声：芯片超级周期堪比当年房地产大举扩张期，卫星产业现阶段不适合长拿，更多是阶段性机会",
    "url": "https://wallstreetcn.com/articles/3775583",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T05:13:42+00:00",
    "summary": "芯片回调是阶段性补仓上车的机会"
  },
  {
    "id": "wscn:3774904",
    "domain": "股票",
    "title": "硅电容：MLCC潜在颠覆者？AI先进封装时代的百亿冠军赛道",
    "url": "https://wallstreetcn.com/premium/articles/3774904?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:33:35+00:00",
    "summary": "三星电机宣布签下1.5万亿韩元（约合人民币68亿元）硅电容供应大单，标志着这一长期隐身于MLCC阴影下的细分赛道正式进入资本市场的聚光灯。"
  },
  {
    "id": "wscn:3775574",
    "domain": "股票",
    "title": "美光财报给美银的启示：存储超级周期或将持续至2027甚至2030年",
    "url": "https://wallstreetcn.com/articles/3775574",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:08:44+00:00",
    "summary": "美银证券最新研报重磅预判：此轮存储超级周期或将延续至2027年乃至2030年。美光财报五大启示直指行业结构性巨变——供给端晶圆厂扩产困难重重，HBM4销售额已破10亿美元，长期协议加速普及平抑周期波动，全球存储市场年化规模剑指万亿美元。三星、SK海力士集体背书，景气共识空前强烈。"
  },
  {
    "id": "wscn:3775567",
    "domain": "股票",
    "title": "创业板跌超3%，算力硬件集体调整，玻璃基板逆势拉升，恒科指再跌超3%，科网股普遍下挫",
    "url": "https://wallstreetcn.com/articles/3775567",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:06:18+00:00",
    "summary": "盘面上，个股呈现普跌态势，沪深京三市超4600股飘绿，上午半天成交2.44万亿。沪深两市半日成交额2.43万亿，较上个交易日基本持平。板块方面，算力硬件产业链回调，PCB、CPO方向领跌；锂矿、AI应用、稀土永磁、金融科技、创新药、人形机器人概念股纷纷下挫。玻璃基板、光刻机、商业航天题材逆势走强。"
  },
  {
    "id": "wscn:3775581",
    "domain": "股票",
    "title": "顶级大V，第一次为你一个人答题",
    "url": "https://wallstreetcn.com/articles/3775581",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T03:29:48+00:00",
    "summary": "财报夜，你一直在看的那家公司，出了业绩。\n你真正想弄清的，从来不是\"它涨了多少\"。\n而是——\"这件事..."
  },
  {
    "id": "wscn:3775578",
    "domain": "股票",
    "title": "机构经纪业务的下一站：平安证券的生态化探索",
    "url": "https://wallstreetcn.com/articles/3775578",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T03:23:14+00:00",
    "summary": "1991年8月22日，深圳蛇口，平安证券在一间不大的办公室里挂牌成立。几张桌子、一部电话，就是这家后..."
  },
  {
    "id": "wscn:3775575",
    "domain": "股票",
    "title": "SpaceX光环消退，美股航天概念股集体重挫，多只个股6月跌幅逾50%",
    "url": "https://wallstreetcn.com/articles/3775575",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T03:17:02+00:00",
    "summary": "航天泡沫骤然刺破——SpaceX上市非但未点燃持续行情，反成压垮板块的最后一根稻草。本月已有四只航天股跌幅超50%，Rocket Lab重挫44%，航天ETF更遭遇六年最惨单月。分析师直指症结：高企估值难撑漫长的商业化周期，而内部人士解禁潮尚未到来，暴风雨或许才刚刚开始。"
  },
  {
    "id": "wscn:3775164",
    "domain": "股票",
    "title": "功率半导体行业：AI算力与新能源双轮驱动，供给紧俏开启景气上行周期",
    "url": "https://wallstreetcn.com/premium/articles/3775164?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T03:02:01+00:00",
    "summary": "AI算力+新能源+供给收缩，功率半导体迎来新一轮上行周期。"
  },
  {
    "id": "wscn:3775576",
    "domain": "股票",
    "title": "“决策大模型第一股上市：中科闻歌的决策智能进阶之路”",
    "url": "https://wallstreetcn.com/articles/3775576",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T02:59:36+00:00",
    "summary": "察势明道"
  },
  {
    "id": "wscn:3775573",
    "domain": "股票",
    "title": "“K型分化”是“技术革命”的宿命？",
    "url": "https://wallstreetcn.com/articles/3775573",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T02:48:30+00:00",
    "summary": "浙商证券复盘1771年以来五轮技术周期发现，K型分化是每一轮技术革命“导入期”的共同规律，而非当下AI时代的特例。技术红利在导入期几乎全部流向资本端：纺织机时代工人实际收入原地踏步，汽车石油时代1929年前1%人口掌握全国近一半净财富，资本市场同步分化。历史表明，只有经历制度重构，技术红利才能真正走向普惠。"
  },
  {
    "id": "wscn:3775570",
    "domain": "股票",
    "title": "外资出逃、散户爆买！摩根大通详解韩国股市巨震背后的资金博弈",
    "url": "https://wallstreetcn.com/articles/3775570",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T02:13:07+00:00",
    "summary": "韩国股市正上演一场罕见的资金拔河：外资年内净流出近950亿美元，有望刷新亚洲单一市场纪录，而散户以800亿美元接盘硬扛。摩根大通将KOSPI基准情景下目标价上调至12500点，称外资抛售本质是规模约束下的\"被迫减仓\"，非主动看空。AI浪潮驱动存储芯片暴涨，韩国仍是其亚洲第一偏好市场。"
  },
  {
    "id": "wscn:3775569",
    "domain": "股票",
    "title": "美光长协的含金量：客户先押220亿美元，合同不可取消，还锁定“史上最赚钱”的毛利率！",
    "url": "https://wallstreetcn.com/articles/3775569",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T02:12:54+00:00",
    "summary": "美光16份SCA长协锁定客户220亿美元押金，协议底价对应的毛利率将远超62%的历史峰值，14份协议最低收入承诺合计约1000亿美元。分析师Harlan Sur称这意味着美光从周期性的大宗商品供应商，转变为拥有多年合同保护、收入与利润均有下行对冲的长期供应商。华尔街大行集体上调目标价。"
  },
  {
    "id": "wscn:3775371",
    "domain": "股票",
    "title": "“铟强磷弱”的突围战：高纯红磷国产化如何填补磷化铟产业链的最后一块拼图？",
    "url": "https://wallstreetcn.com/premium/articles/3775371?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T02:08:21+00:00",
    "summary": "电子级高纯红磷是一个典型的 “小市场、高壁垒、高集中度” 赛道。在AI算力驱动的光模块需求爆发与国产替代的双重共振下，这一“隐形磷源”正从产业边缘走向舞台中央。"
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
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.26470",
    "domain": "金融",
    "title": "The Growing Self-Reliance of Chinese Innovation",
    "url": "https://arxiv.org/abs/2606.26470",
    "source": "ZIyu Chen, Christopher Esposito",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2606.26470v1 Announce Type: new Abstract: U.S. policy increasingly seeks to slow China's technological rise by restricting its access to American science, on the assumption that Chinese innovati"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.26536",
    "domain": "金融",
    "title": "Too cheap to meter? A stochastic analysis of projected future fusion costs",
    "url": "https://arxiv.org/abs/2606.26536",
    "source": "Stefania B\\\"ohnlein, Fanny B\\\"ose, Christian von Hirschhausen, Claudia Kemfert, Alexander Wimmers",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2606.26536v1 Announce Type: new Abstract: In recent years, technological developments and activities by private actors have led a reemerged discussion of the potential of nuclear fusion to meet "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.26625",
    "domain": "金融",
    "title": "Portfolio Optimization for Commodity ETFs under Heavy-Tailed Returns",
    "url": "https://arxiv.org/abs/2606.26625",
    "source": "Nicholas Appiah, Ali Jaffri, Dilmi C. W. Hettiachchi-Halpe-Kankanamalage, Svetlozar T. Rachev",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2606.26625v1 Announce Type: new Abstract: This paper examines portfolio optimization for commodity exchange-traded funds (ETFs) under heavy-tailed return behavior. Using daily Bloomberg data for"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.26731",
    "domain": "金融",
    "title": "Robust Hedging Valuation Adjustment under Liquidity--Demand Stress",
    "url": "https://arxiv.org/abs/2606.26731",
    "source": "Takayuki Sakuma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2606.26731v1 Announce Type: new Abstract: This paper develops a robust hedging valuation adjustment (HVA) measure for dynamic hedging. Simulated rebalancing and maturity-unwind trades generate a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.26815",
    "domain": "金融",
    "title": "Data-Driven Duration Management -- Term Structure Forecasting Using Machine Learning",
    "url": "https://arxiv.org/abs/2606.26815",
    "source": "Tobias Lausser, Joao Eduardo Vuolo, Rudi Zagst",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2606.26815v1 Announce Type: new Abstract: This paper compares different methods for forecasting the term structure of U.S. and European zero-coupon government bonds using both traditional econom"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.26835",
    "domain": "金融",
    "title": "A sharp order-three obstruction to the aggregation of conditional price-of-risk attribution",
    "url": "https://arxiv.org/abs/2606.26835",
    "source": "Alejandro Rodriguez Dominguez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2606.26835v1 Announce Type: new Abstract: We study the squared price-of-risk premium of a portfolio -- an integrated conditional squared Sharpe-ratio functional, not an expected excess return --"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.26959",
    "domain": "金融",
    "title": "The Shift to Agentic AI: Evidence from Codex",
    "url": "https://arxiv.org/abs/2606.26959",
    "source": "Drew Johnston, David Holtz, Alex Martin Richmond, Christopher Ong, Prasanna Tambe, Aaron Chatterji",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2606.26959v1 Announce Type: new Abstract: We analyze usage data from OpenAI's Codex tool to present large-scale evidence of how agentic AI technology, which can take actions on a user's behalf, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.26966",
    "domain": "金融",
    "title": "Economic complexity at subnational level: A consistency analysis",
    "url": "https://arxiv.org/abs/2606.26966",
    "source": "Wenli Du, Andrea Zaccaria",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2606.26966v1 Announce Type: new Abstract: Several network-based measures have been proposed to assess the economic complexity of countries. These measures have provided important insights into n"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.27100",
    "domain": "金融",
    "title": "Pretrained Time-Series Foundation Models for Financial Return Forecasting",
    "url": "https://arxiv.org/abs/2606.27100",
    "source": "Miquel Noguer I Alonso, Rodolfo Pereira Franklin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2606.27100v1 Announce Type: new Abstract: Financial return forecasting is a difficult test case for time-series foundation models (TSFMs) due to low signal-to-noise ratios, structural breaks, he"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.27150",
    "domain": "金融",
    "title": "Endogenous Reinsurance Pricing in Large Competitive Insurance Markets: Finite-Player and Mean Field Analysis",
    "url": "https://arxiv.org/abs/2606.27150",
    "source": "Ruimeng Hu, Byungdoo Kong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2606.27150v1 Announce Type: new Abstract: We study endogenous reinsurance pricing in a competitive insurance market with one strategic reinsurer and many heterogeneous insurers. The reinsurer ac"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.27335",
    "domain": "金融",
    "title": "Valuing American options and Flexible Forwards contracts in time-dependent models",
    "url": "https://arxiv.org/abs/2606.27335",
    "source": "Leif Andersen, Andrey Itkin, Rakhymzhan Kazbek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2606.27335v1 Announce Type: new Abstract: A flexible forward (FF) is a customized FX hedging instrument that guarantees a fixed exchange rate while letting the holder choose the delivery date wi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.27046",
    "domain": "金融",
    "title": "Conditional Leibniz Derivative Estimation with an Application to American Call Min-Options",
    "url": "https://arxiv.org/abs/2606.27046",
    "source": "Xingyu Ren, Michael C. Fu, Pierre L'Ecuyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2606.27046v1 Announce Type: cross Abstract: Leibniz derivative estimation is a Monte Carlo technique for estimating derivatives of a discontinuous sample performance in stochastic models with re"
  },
  {
    "id": "rss:https://arxiv.org/abs/2304.07672",
    "domain": "金融",
    "title": "Optimal Investment and Consumption Strategies with General Cost Structure under CRRA Utility",
    "url": "https://arxiv.org/abs/2304.07672",
    "source": "Yingting Miao, Qiang Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2304.07672v2 Announce Type: replace Abstract: Transaction costs play a critical role in portfolio allocation and consumption decisions. We study a finite-horizon consumption--investment problem "
  },
  {
    "id": "rss:https://arxiv.org/abs/2505.02678",
    "domain": "金融",
    "title": "A Nested Factor Model for Equity Markets: Reconciling Multifractal Stock Returns and Rough Index Volatilities",
    "url": "https://arxiv.org/abs/2505.02678",
    "source": "Othmane Zarhali, Cecilia Aubrun, Emmanuel Bacry, Jean-Philippe Bouchaud, Jean-Fran\\c{c}ois Muzy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2505.02678v4 Announce Type: replace Abstract: The Nested factor model was introduced by Chicheportiche et al. to represent non-linear correlations between stocks. Stock returns are explained by "
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.19663",
    "domain": "金融",
    "title": "Long-Range Dependence in Financial Markets: Empirical Evidence and Generative Modeling Challenges",
    "url": "https://arxiv.org/abs/2509.19663",
    "source": "Yifan He, Svetlozar Rachev",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2509.19663v3 Announce Type: replace Abstract: This study provides an empirical investigation of long-range dependence (LRD) in financial markets and evaluates the ability of deep generative mode"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.07431",
    "domain": "金融",
    "title": "Optimal Cash Transfers and Microinsurance to Reduce Social Protection Costs",
    "url": "https://arxiv.org/abs/2511.07431",
    "source": "Pablo Azcue, Corina Constantinescu, Jos\\'e Miguel Flores-Contr\\'o, Nora Muler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2511.07431v3 Announce Type: replace Abstract: Design and implementation of appropriate social protection strategies is one of the main targets of the United Nation's Sustainable Development Goal"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.10584",
    "domain": "金融",
    "title": "Volatility time series modeling by single-qubit quantum circuit learning",
    "url": "https://arxiv.org/abs/2512.10584",
    "source": "Tetsuya Takaishi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2512.10584v3 Announce Type: replace Abstract: We employ single-qubit quantum circuit learning (QCL) to model the dynamics of volatility time series. To assess its effectiveness, we generate synt"
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.00548",
    "domain": "金融",
    "title": "The Impact of Trump-Era Tariffs on Financial Market Efficiency",
    "url": "https://arxiv.org/abs/2602.00548",
    "source": "Tetsuya Takaishi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2602.00548v2 Announce Type: replace Abstract: This study examines the effects of Trump-era tariffs on financial market efficiency by applying multifractal detrended fluctuation analysis to the r"
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.00858",
    "domain": "金融",
    "title": "Short-Rate-Dependent Volatility Models",
    "url": "https://arxiv.org/abs/2602.00858",
    "source": "Tim Leung, Matthew Lorig",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2602.00858v3 Announce Type: replace Abstract: We price European options in a class of models in which the volatility of the underlying risky asset depends on the short rate of interest. Our stud"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.00800",
    "domain": "金融",
    "title": "Multiplicative Langevin Process for Volatilities Produces Observed Q-Variance Regularities",
    "url": "https://arxiv.org/abs/2606.00800",
    "source": "William H. Press, Alex Dannenberg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2606.00800v2 Announce Type: replace Abstract: Q-variance (so-called) posits a statistical relationship $\\mathbf{E}(\\sigma^2 | z) = \\sigma_0^2 + \\tfrac{1}{2}z^2$ between an asset's volatility $\\s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09564",
    "domain": "金融",
    "title": "Option prices from operational-time reaction-boundary lattices",
    "url": "https://arxiv.org/abs/2606.09564",
    "source": "Chris Angstmann, Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2606.09564v2 Announce Type: replace Abstract: We consider the role of a continuum operational time u and its mapping to calendar time t and how these relate to event time for option pricing prob"
  },
  {
    "id": "rss:https://arxiv.org/abs/2506.18942",
    "domain": "金融",
    "title": "Advanced Applications of Generative AI in Actuarial Science: Case Studies Beyond ChatGPT",
    "url": "https://arxiv.org/abs/2506.18942",
    "source": "Simon Hatzesberger, Iris Nonneman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2506.18942v3 Announce Type: replace-cross Abstract: This article explores the potential of generative AI (GenAI) to support actuarial practice through four implemented case studies. It situates "
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.00853",
    "domain": "金融",
    "title": "Ranking Quantilized Mean-Field Games with an Application to Early-Stage Venture Investments",
    "url": "https://arxiv.org/abs/2507.00853",
    "source": "Rinel Foguen Tchuendom, Dena Firoozi, Mich\\`ele Breton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2507.00853v2 Announce Type: replace-cross Abstract: Quantilized mean-field game models involve quantiles of the population's distribution. We study a class of such games with a capacity for rank"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.04574",
    "domain": "金融",
    "title": "Dynamic Multi-Pair Trading Strategy in Cryptocurrency Markets with Deep Reinforcement Learning",
    "url": "https://arxiv.org/abs/2606.04574",
    "source": "Damian Lebied\\'z, Robert \\'Slepaczuk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-26T04:00:00+00:00",
    "summary": "arXiv:2606.04574v2 Announce Type: replace-cross Abstract: This study aims to determine whether the application of Deep Reinforcement Learning (DRL) as a specialized execution overlay can enhance pair "
  }
]
```
