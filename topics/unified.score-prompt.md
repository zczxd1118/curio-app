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

- 今日日期：`2026-06-19`
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
  "date": "2026-06-19",
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
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1200901,
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
    "points": 1192084,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 938688,
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
    "points": 723710,
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
    "points": 663386,
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
    "points": 424296,
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
    "points": 422522,
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
    "points": 414516,
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
    "points": 394147,
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
    "points": 373673,
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
    "points": 357646,
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
    "points": 329740,
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
    "points": 244019,
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
    "points": 238368,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1h64y1v7tt",
    "domain": "AI",
    "title": "Windows Server2016网络操作系统服务器教程（已更新）",
    "url": "http://www.bilibili.com/video/av760038986",
    "source": "尚优大课堂",
    "platform": "bilibili",
    "points": 227375,
    "published_at": "2021-04-15T03:23:09+00:00",
    "summary": "本视频以Windows Server 2016操作系统为例，演示日常工作中常用的服务器相关功能的配置和管理，能够让大家直观的学习Windows服务器的操作系统各种操作，与大家同学学习提高。"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 174818,
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
    "points": 156776,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 153330,
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
    "points": 143693,
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
    "points": 137817,
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
    "points": 136006,
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
    "points": 120988,
    "published_at": "2026-06-11T15:27:06+00:00",
    "summary": "官方文档地址：https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/claude_code"
  },
  {
    "id": "bvid:BV1j67k6oENA",
    "domain": "AI",
    "title": "Claude Ultracode 超码 上线 | 操控100个Agent并行开发  保姆级实战教程",
    "url": "http://www.bilibili.com/video/av116697163896598",
    "source": "技术胖",
    "platform": "bilibili",
    "points": 104569,
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
    "points": 92684,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1HM7C6BEnF",
    "domain": "AI",
    "title": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！",
    "url": "http://www.bilibili.com/video/av116696929076767",
    "source": "AIAgent开发",
    "platform": "bilibili",
    "points": 77147,
    "published_at": "2026-06-05T10:11:18+00:00",
    "summary": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73226,
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
    "points": 64252,
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
    "points": 58905,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV1DsnzzwEUF",
    "domain": "AI",
    "title": "为什么你要立即开始 Vibe Coding —— All in AI",
    "url": "http://www.bilibili.com/video/av115288397978817",
    "source": "TradingLab",
    "platform": "bilibili",
    "points": 58174,
    "published_at": "2025-09-30T09:00:00+00:00",
    "summary": "没有工作了就去大自然中感受下算力最高的simulation engine——现实。大自然“没有问题“也没问题，没有目标，却有无限创造力。同样人也不需要非要宅在家里vibe coding。或许当人脱离了生存本能与真实环境，沉溺于安全却单调的日常生活，才会苦苦思考如何在AI时代acquire more equity这种问题。回到自然，真正的乐趣无处不在"
  },
  {
    "id": "bvid:BV12cjj6eEnW",
    "domain": "AI",
    "title": "SpaceX 宣布正式以600亿美元收购 Cursor；智谱正式发布 GLM-5.2【AI 早报 2026-06-17】",
    "url": "http://www.bilibili.com/video/av116762880247152",
    "source": "橘鸦Juya",
    "platform": "bilibili",
    "points": 58101,
    "published_at": "2026-06-17T01:42:42+00:00",
    "summary": "相关链接和文字版请看：https://mp.weixin.qq.com/s/qUQrti04igqD6wguDy3dcQ"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 52071,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1rKjG6yEh2",
    "domain": "AI",
    "title": "10分钟+300个Agent：保姆级教程学会Agent Skills！【从零开始】",
    "url": "http://www.bilibili.com/video/av116758736279146",
    "source": "Work-Fisher",
    "platform": "bilibili",
    "points": 47424,
    "published_at": "2026-06-16T10:02:41+00:00",
    "summary": "这期我从最基础的概念，一路讲到上手实操，基本上是从 0 到 1，带你完整走一遍——一个 SKILL 到底是怎么从无到有做出来的。\n国内、国外的创建工具，我也都给你捋了一遍。希望看完这期，你也能动手做出一个真正属于自己的 SKIL。"
  },
  {
    "id": "bvid:BV1fGFsznEas",
    "domain": "AI",
    "title": "vibe coding 10分钟做一个塔罗牌游戏",
    "url": "http://www.bilibili.com/video/av116029028042969",
    "source": "鸭鸭摘花",
    "platform": "bilibili",
    "points": 46450,
    "published_at": "2026-02-07T11:20:13+00:00",
    "summary": "一个简单的教程 一行代码不写 做一个塔罗牌游戏"
  },
  {
    "id": "bvid:BV1FzfoYSE4f",
    "domain": "AI",
    "title": "影刀AI Power零基础教程：02 智能体——打造企业AI超级员工",
    "url": "http://www.bilibili.com/video/av113888003622214",
    "source": "影刀RPA",
    "platform": "bilibili",
    "points": 40162,
    "published_at": "2025-02-06T02:00:00+00:00",
    "summary": "AI智能体：场景化智能助手，打造企业AI超级员工\n影刀AI Power，帮助企业将AI用起来。让每个员工都能拥有AI能力，在工作中使用AI解决问题。\n\n影刀AP企业版免费试用申请：http://s.winrobot360.com/g02tp\n影刀AP社区版使用：https://www.yingdao.com/ai-power/"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 39607,
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
    "points": 38792,
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
    "points": 36218,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1ap2fBvEt9",
    "domain": "AI",
    "title": "如何使用「Operit AI」：你的下一代AI手机助手",
    "url": "http://www.bilibili.com/video/av115677243447909",
    "source": "默睦",
    "platform": "bilibili",
    "points": 31856,
    "published_at": "2025-12-07T08:06:42+00:00",
    "summary": "下载地址：https://github.com/AAswordman/Operit\n\n相关软件资料下载：https://www.123pan.com/s/IKgAjv-Hinsv.html\n\n官方交流群：458862019"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 30819,
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
    "points": 29708,
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
    "points": 29332,
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
    "points": 27353,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 23599,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
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
    "id": "bvid:BV1ZEJA6xEds",
    "domain": "AI",
    "title": "最新方法！国内免费无限制，使用Claude Code！",
    "url": "http://www.bilibili.com/video/av116746874848391",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 20194,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1kxLD6HEYN",
    "domain": "AI",
    "title": "Claude Code怎么全自动跑13小时？实测GLM 5.2开源天花板",
    "url": "http://www.bilibili.com/video/av116763920438810",
    "source": "小白debug",
    "platform": "bilibili",
    "points": 19101,
    "published_at": "2026-06-17T10:14:02+00:00",
    "summary": "我手搓了一个Openclaw"
  },
  {
    "id": "bvid:BV1VbUCBAEZS",
    "domain": "AI",
    "title": "鸿蒙电脑上跑 Claude Code？我真的做到了！",
    "url": "http://www.bilibili.com/video/av115604514148535",
    "source": "jadeCircuit",
    "platform": "bilibili",
    "points": 18618,
    "published_at": "2025-11-24T11:55:31+00:00",
    "summary": "在这期视频中，我展示了我是如何在 HarmonyOS PC 上，通过 HiSH 的 Alpine Linux Shell 让 Claude Code 成功运行的，虽然 HarmonyOS 本身并不支持这些工具。\n华为最近发布了 HarmonyOS PC 版 DevEco Studio 预览版。这个 IDE 整体体验已经很好了，但仍然缺少像 Claude Code 这样强大的 AI 编码工具。\n 所"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17354,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1hnjGzLE14",
    "domain": "AI",
    "title": "【小智教程】手挽手教你如何接入别人的MCP服务",
    "url": "http://www.bilibili.com/video/av114568722450105",
    "source": "空白泡泡糖果",
    "platform": "bilibili",
    "points": 17132,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV1mfJw6uE1Y",
    "domain": "AI",
    "title": "AI Agent 别乱选！2026 AI Agent 深度横评，普通人看完不踩坑｜OpenClaw、Codex、Hermes、WorkBuddy、Claude",
    "url": "http://www.bilibili.com/video/av116747361322195",
    "source": "AI实战派Pro",
    "platform": "bilibili",
    "points": 15991,
    "published_at": "2026-06-14T07:53:12+00:00",
    "summary": "《2026 主流 AI Agent 全维度对比｜OpenClaw / Codex / Claude Cowork / WorkBuddy / Hermes 怎么选？》\n\nHi，我是Alpha，我手把手带大家用AI提升自己工作、生活效率，提升个人竞争力以及用AI赚钱！一起做AI时代的主导者，而不是在焦虑中被AI淘汰！\n关注AI 实战派，让AI替你忙起来！\n\n本期视频介绍：《AI Agent 别乱选！"
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
    "id": "rss:https://www.eetimes.com/intelligent-power-solutions-for-next-gen-robotics-compute-platforms/",
    "domain": "AI 算力 / 半导体",
    "title": "Intelligent Power Solutions for Next-Gen Robotics Compute Platforms",
    "url": "https://www.eetimes.com/intelligent-power-solutions-for-next-gen-robotics-compute-platforms/",
    "source": "Monolithic Power Systems Inc.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T13:07:18+00:00",
    "summary": "Date: Tuesday, July 21, 2026 Time: 9:00am PDT &#124; 12:00pm EDT Not your time zone? Please join us on Tuesday, July 28th @ 15:00 CEST Register Here! Rapid advances in humanoid robotics are being driv"
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
    "id": "rss:https://www.eetimes.com/built-in-memory-built-in-confidence/",
    "domain": "AI 算力 / 半导体",
    "title": "Built-In Memory. Built-In Confidence.",
    "url": "https://www.eetimes.com/built-in-memory-built-in-confidence/",
    "source": "Morten Block, Global Eng. Director, Segments and Technology go-to-market",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T13:00:00+00:00",
    "summary": "Memory shortages put edge AI at risk. NVIDIA Jetson™ integrates validated LPDDR5 DRAM on-module—giving teams a faster, confident path to production. The post Built-In Memory. Built-In Confidence. appe"
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
    "id": "rss:https://www.tomshardware.com/tech-industry/bosch-to-pay-usd36-million-penalty-for-usd72-million-in-illicit-sales-to-huawei-german-company-sold-export-controlled-goods-and-software-to-banned-chinese-firm-between-2020-and-2024",
    "domain": "AI 算力 / 半导体",
    "title": "Bosch to pay $36 million penalty for $72 million in ‘illicit’ sales to Huawei — German company sold export-controlled goods and software to banned Chinese firm between 2020 and 2024",
    "url": "https://www.tomshardware.com/tech-industry/bosch-to-pay-usd36-million-penalty-for-usd72-million-in-illicit-sales-to-huawei-german-company-sold-export-controlled-goods-and-software-to-banned-chinese-firm-between-2020-and-2024",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T11:42:18+00:00",
    "summary": "The U.S. fined Bosch $36 million for selling export-controlled product to Huawei, including software and MEMS sensors. The German company agreed to pay the penalty, as well as disgorging part of the p"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/trump-says-apple-agreed-to-build-chips-with-intel",
    "domain": "AI 算力 / 半导体",
    "title": "Trump says Apple has agreed to 'build' chips with Intel — neither company confirms deal as Intel share price rockets",
    "url": "https://www.tomshardware.com/tech-industry/trump-says-apple-agreed-to-build-chips-with-intel",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T11:32:41+00:00",
    "summary": "President Donald Trump said on Thursday that Apple has agreed to work with Intel to “design and build” chips in the United States."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/chinese-makers-of-dram-modules-ssds-have-a-serious-advantage-over-american-and-taiwanese-suppliers-says-smi-svp-state-guidance-secures-local-dram-and-ssd-supply-while-the-big-three-chase-ai-margins",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese makers of DRAM modules, SSDs have a serious advantage over American and Taiwanese suppliers, says SMI SVP — state guidance secures local DRAM and SSD supply while the Big Three chase AI margin",
    "url": "https://www.tomshardware.com/pc-components/ssds/chinese-makers-of-dram-modules-ssds-have-a-serious-advantage-over-american-and-taiwanese-suppliers-says-smi-svp-state-guidance-secures-local-dram-and-ssd-supply-while-the-big-three-chase-ai-margins",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T10:30:00+00:00",
    "summary": "CCP directives can be lifebuoy for Chinese producers of DRAM modules and solid-state drives as domestic memory makers may be obliged to support the module industry."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptocurrency/digital-entrepreneur-creates-humorous-physical-nft-minting-device-using-a-raspberry-pi-in-quest-for-infinite-money-machine-contraption-trained-on-m3-macbook-can-generate-an-nft-in-3-seconds-has-so-far-sold-one-for-usd9-92",
    "domain": "AI 算力 / 半导体",
    "title": "Digital entrepreneur creates humorous 'physical NFT minting device' using a Raspberry Pi in quest for 'infinite money machine' — contraption trained on M3 MacBook can generate an NFT in 3 seconds, has",
    "url": "https://www.tomshardware.com/tech-industry/cryptocurrency/digital-entrepreneur-creates-humorous-physical-nft-minting-device-using-a-raspberry-pi-in-quest-for-infinite-money-machine-contraption-trained-on-m3-macbook-can-generate-an-nft-in-3-seconds-has-so-far-sold-one-for-usd9-92",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T10:26:50+00:00",
    "summary": "An enterprising young man aims to catch up with the collective wealth of Elon Musk, and his first money spinner is a portable NFT minting gadget."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/kaspersky-finds-malware-hidden-in-steam-wallpapers-that-hijacks-accounts-to-spread-itself",
    "domain": "AI 算力 / 半导体",
    "title": "Kaspersky finds malware hidden in Steam Wallpaper Engine that hijacks accounts to spread itself — dozens of malicious packages downloaded tens of thousands of times",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/kaspersky-finds-malware-hidden-in-steam-wallpapers-that-hijacks-accounts-to-spread-itself",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T10:00:00+00:00",
    "summary": "Attackers have spent the past several months smuggling malware into Steam through animated desktop wallpapers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/frontier-airlines-site-leaks-all-personal-info-with-just-a-glance-at-a-boarding-pass-researcher-claims-booking-number-and-last-name-nets-you-every-passengers-personal-info-including-address-passport-tsa-precheck-and-most-credit-card-info",
    "domain": "AI 算力 / 半导体",
    "title": "Frontier Airlines site leaks all personal info with just a glance at a boarding pass, researcher claims — booking number and last name nets you every passenger's personal info, including address, pass",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/frontier-airlines-site-leaks-all-personal-info-with-just-a-glance-at-a-boarding-pass-researcher-claims-booking-number-and-last-name-nets-you-every-passengers-personal-info-including-address-passport-tsa-precheck-and-most-credit-card-info",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T09:30:00+00:00",
    "summary": "Frontier Airlines site leaks all personal info with just a glance at a boarding pass — just a booking number and last name nets you all passengers' personal info including address, passport, TSA PreCh"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intels-fab-roadmap-examined",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's fab roadmap examined — Arizona, Ohio, Ireland, and the two deadlines deciding 14A process node",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intels-fab-roadmap-examined",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T20:46:27+00:00",
    "summary": "This roadmap provides an in-depth analysis of Intel's current plans for its chip production capacity."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/us-pulls-the-kill-switch-on-anthropics-fable-5-ai-models-sending-global-allies-scrambling-european-and-canadian-leaders-alarm-allies-over-sudden-export-bans",
    "domain": "AI 算力 / 半导体",
    "title": "US pulls the 'kill-switch' on Anthropic's Fable 5 AI models, sending global allies scrambling — European and Canadian leaders alarm allies over sudden export bans",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/us-pulls-the-kill-switch-on-anthropics-fable-5-ai-models-sending-global-allies-scrambling-european-and-canadian-leaders-alarm-allies-over-sudden-export-bans",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T17:36:41+00:00",
    "summary": "Following the Trump administration's block on Anthropic's Mythos 5 and Fable 5 models, world leaders have raised concerns that without direct access to frontier models, they may need to develop their "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/deepseek-was-set-to-be-added-to-us-entity-list-for-supporting-chinas-military-and-intelligence-operations-report-claims-white-house-holds-off-to-avoid-escalating-tensions-with-china",
    "domain": "AI 算力 / 半导体",
    "title": "DeepSeek was set to be added to US Entity List for supporting China’s military and intelligence operations, report claims — White House holds off to avoid escalating tensions with China",
    "url": "https://www.tomshardware.com/tech-industry/deepseek-was-set-to-be-added-to-us-entity-list-for-supporting-chinas-military-and-intelligence-operations-report-claims-white-house-holds-off-to-avoid-escalating-tensions-with-china",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T16:00:45+00:00",
    "summary": "DeepSeek and CXMT, which have both been tagged as supporting Chinese military and intelligence operations, are set to be added to the U.S.'s Entity List. However, the White House hasn't included them "
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/snag-a-pro-level-gaming-monitor-at-entry-level-pricing-gigabyte-27-inch-1440p-180-hz-monitor-up-for-grabs-at-usd159",
    "domain": "AI 算力 / 半导体",
    "title": "Snag a pro-level 180 Hz gaming monitor at entry-level pricing — Gigabyte 27-inch 1440p monitor up for grabs at $159",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/snag-a-pro-level-gaming-monitor-at-entry-level-pricing-gigabyte-27-inch-1440p-180-hz-monitor-up-for-grabs-at-usd159",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T16:00:00+00:00",
    "summary": "For a limited time, Newegg has the Gigabyte GS27QA on sale for $159.99, 36%off its regular price."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-releases-rtx-remix-1-5-with-new-rtx-io-compression-reducing-mod-file-sizes-by-up-to-37-percent-update-also-adds-smooth-normals-and-rtx-remix-skills-agents",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia releases RTX Remix 1.5 with new RTX IO compression reducing mod file sizes by up to 37% — update also adds Smooth Normals and 'RTX Remix Skills' Agents",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-releases-rtx-remix-1-5-with-new-rtx-io-compression-reducing-mod-file-sizes-by-up-to-37-percent-update-also-adds-smooth-normals-and-rtx-remix-skills-agents",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T15:33:55+00:00",
    "summary": "Nvidia has updated RTX Remix with a bunch of new features that will help improve the fidelity and reduce the file size of modded games, along with the complexity of developing said mods."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/researchers-build-brain-like-memory-device-for-ai-sensors-that-may-improve-energy-efficiency-phototransistor-device-combines-light-sensing-memory-and-processing-to-cut-data-movement",
    "domain": "AI 算力 / 半导体",
    "title": "Researchers build brain-like memory device for AI sensors that may improve energy efficiency — phototransistor device combines light sensing, memory, and processing to cut data movement",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/researchers-build-brain-like-memory-device-for-ai-sensors-that-may-improve-energy-efficiency-phototransistor-device-combines-light-sensing-memory-and-processing-to-cut-data-movement",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T14:19:33+00:00",
    "summary": "Oregon State University researchers have developed a brain-inspired phototransistor that combines light sensing, memory, and signal processing in one device. The hardware can electronically control ho"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/undersea-cable-connecting-egypt-and-syria-has-been-cut-damascus-blames-systematic-sabotage-campaign-as-cause-of-damage",
    "domain": "AI 算力 / 半导体",
    "title": "Undersea cable connecting Egypt and Syria has been cut, state-owned telecom operator says — Damascus blames 'systematic sabotage campaign' as cause of damage",
    "url": "https://www.tomshardware.com/networking/undersea-cable-connecting-egypt-and-syria-has-been-cut-damascus-blames-systematic-sabotage-campaign-as-cause-of-damage",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T13:31:39+00:00",
    "summary": "The Syrian government blamed a third party for the damage on its undersea cable that connects it to Egypt. Damascus didn't mention any specific state or non-state actor, but its location makes it a pr"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/first-official-details-of-amds-next-gen-mustang-peak-threadripper-cpus-come-into-view-chips-feature-ddr5-pcie-6-0-and-a-new-socket",
    "domain": "AI 算力 / 半导体",
    "title": "First official details of AMD's next-gen 'Mustang Peak' Threadripper CPUs come into view — chips feature DDR5, PCIe 6.0, and a new socket",
    "url": "https://www.tomshardware.com/pc-components/cpus/first-official-details-of-amds-next-gen-mustang-peak-threadripper-cpus-come-into-view-chips-feature-ddr5-pcie-6-0-and-a-new-socket",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T13:17:24+00:00",
    "summary": "We now have the first confirmed details about AMD's Zen 6-based Threadripper CPUs, code-named Mustang Peak."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd500-on-this-acer-16-predator-helios-neo-16-ips-gaming-laptop-just-usd1-499-99-gets-you-a-powerful-portable-gaming-rig-with-an-rtx-5070-32gb-ddr5-and-intel-core-ultra-9-275-hx-processor",
    "domain": "AI 算力 / 半导体",
    "title": "Save $500 on this Acer 16” Predator Helios Neo 16 IPS Gaming laptop — just $1,499.99 gets you a powerful portable gaming rig with an RTX 5070, 32GB DDR5, and Intel Core Ultra 9 275 HX processor",
    "url": "https://www.tomshardware.com/pc-components/save-usd500-on-this-acer-16-predator-helios-neo-16-ips-gaming-laptop-just-usd1-499-99-gets-you-a-powerful-portable-gaming-rig-with-an-rtx-5070-32gb-ddr5-and-intel-core-ultra-9-275-hx-processor",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T12:11:51+00:00",
    "summary": "Save $500 on Acer’s Predator Helios Neo 16 AI Gaming laptop and score a powerful gaming laptop with 32GB of RAM and RTX 5070 for only $1,499.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/viewsonic-vx2738-2k-27-inch-oled-review",
    "domain": "AI 算力 / 半导体",
    "title": "ViewSonic VX2738-2K 27-inch OLED review: An OLED value play",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/viewsonic-vx2738-2k-27-inch-oled-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T12:10:00+00:00",
    "summary": "ViewSonic’s VX2738-2K OLED is a high-performance 27-inch QHD gaming monitor with 240 Hz, Adaptive-Sync, HDR and Quantum Dot color. It delivers smooth speed, quick response and saturated color for a re"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-reveals-ai-robots-that-taught-themselves-to-install-gpus-into-motherboards-video-shows-robot-solve-high-precision-tasks-like-installing-gpus-all-by-itself",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia reveals AI robots that taught themselves to install GPUs into motherboards — video shows robot ‘solve high-precision tasks like… installing GPUs all by itself’",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-reveals-ai-robots-that-taught-themselves-to-install-gpus-into-motherboards-video-shows-robot-solve-high-precision-tasks-like-installing-gpus-all-by-itself",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T12:06:48+00:00",
    "summary": "Nvidia showcases agentic robots that can teach themselves high-precision and dexterous tasks - like PC building - in the real world."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/fight-the-price-rises-on-ssds-with-this-31-percent-saving-on-samsungs-brilliant-1tb-990-pro-ssd-now-usd219-at-amazon-lowest-price-since-april",
    "domain": "AI 算力 / 半导体",
    "title": "Fight the price rises on SSDs with this 31% saving on Samsung's brilliant 1TB 990 Pro SSD — now $219 at Amazon, lowest price since April",
    "url": "https://www.tomshardware.com/pc-components/ssds/fight-the-price-rises-on-ssds-with-this-31-percent-saving-on-samsungs-brilliant-1tb-990-pro-ssd-now-usd219-at-amazon-lowest-price-since-april",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T11:43:24+00:00",
    "summary": "Save $100 off the price of this 1TB Samsung 990 Pro SSD. Amazon's 31% discount fights off the current storage price rises."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/u-s-govt-asks-court-to-dismiss-naacp-lawsuit-against-elon-musks-xai-over-use-of-unpermitted-gas-turbines-doj-says-grok-model-running-at-colossus-2-supports-mission-critical-operations",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. gov't asks court to dismiss NAACP lawsuit against Elon Musk's xAI over use of unpermitted gas turbines — DOJ says Grok model running at Colossus 2 ‘supports mission-critical operations’",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/u-s-govt-asks-court-to-dismiss-naacp-lawsuit-against-elon-musks-xai-over-use-of-unpermitted-gas-turbines-doj-says-grok-model-running-at-colossus-2-supports-mission-critical-operations",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T11:00:00+00:00",
    "summary": "The US government is seeking dismissal of a lawsuit from the NAACP, arguing that the Colossus 2 data center is crucial for national security. The data center runs the Grok Gov AI model, and the govern"
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
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/952837/barret-zoph-openai-thinking-machines-lab",
    "domain": "大厂 AI 动态",
    "title": "Barret Zoph is out at OpenAI again after just five months",
    "url": "https://www.theverge.com/ai-artificial-intelligence/952837/barret-zoph-openai-thinking-machines-lab",
    "source": "Hayden Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:49:33+00:00",
    "summary": "Five months after returning to OpenAI, Barret Zoph - the company's head of enterprise AI sales - has departed, The Verge has learned. Zoph returned to OpenAI in mid-January after a stint as co-founder"
  },
  {
    "id": "rss:https://www.theverge.com/games/952582/valve-steam-controller-reservations-orders-behind-estimated-date",
    "domain": "大厂 AI 动态",
    "title": "Valve is so behind on Steam Controller orders that some won&#8217;t ship until 2027",
    "url": "https://www.theverge.com/games/952582/valve-steam-controller-reservations-orders-behind-estimated-date",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T20:26:06+00:00",
    "summary": "Valve has some good news and bad news about Steam Controllers. The good news: If you make a reservation for a Steam Controller, the company will now show you one of three estimates of when you'll be a"
  },
  {
    "id": "rss:https://www.theverge.com/tech/952173/epilogue-gb-operator-game-boy-camera-ios-android-app-iphone",
    "domain": "大厂 AI 动态",
    "title": "You can now use the Game Boy Camera with your phone",
    "url": "https://www.theverge.com/tech/952173/epilogue-gb-operator-game-boy-camera-ios-android-app-iphone",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T20:22:46+00:00",
    "summary": "The $50 GB Operator is an accessory that lets you connect, play, and authenticate Game Boy, Game Boy Color, and Game Boy Advance cartridges on PCs and other devices. Now it's getting some new function"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/952326/hbo-max-annual-plan-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "HBO Max&#8217;s annual plans are 28 percent off right now",
    "url": "https://www.theverge.com/gadgets/952326/hbo-max-annual-plan-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T19:18:30+00:00",
    "summary": "The easiest way to save on a streaming service is often to pay for a year upfront, which HBO Max is currently making a lot cheaper. Through July 15, 2026, new and returning subscribers can get 28 perc"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/952126/snap-specs-ar-glasses-vergecast",
    "domain": "大厂 AI 动态",
    "title": "Snap’s Specs look good on nobody",
    "url": "https://www.theverge.com/podcast/952126/snap-specs-ar-glasses-vergecast",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T19:15:03+00:00",
    "summary": "Snap's new smart glasses are probably the most impressive bit of face-computer technology we've seen. They're not VR-headset huge; they don't have a big charging puck; thanks to Snap's many years of A"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/944084/best-early-prime-day-deals",
    "domain": "大厂 AI 动态",
    "title": "The best early Amazon Prime Day deals so far",
    "url": "https://www.theverge.com/gadgets/944084/best-early-prime-day-deals",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T18:54:32+00:00",
    "summary": "Amazon’s earlier-than-usual Prime Day doesn’t begin until June 23rd, but there are several even earlier deals on must-have products that you can check out right now. To name some examples, Apple’s Air"
  },
  {
    "id": "rss:https://www.theverge.com/tech/952441/yueban-xiaoban-self-driving-autonomous-toilet",
    "domain": "大厂 AI 动态",
    "title": "This robotic self-driving toilet comes to you",
    "url": "https://www.theverge.com/tech/952441/yueban-xiaoban-self-driving-autonomous-toilet",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T18:08:17+00:00",
    "summary": "During a recent expo in Shanghai that focuses on elderly care, assistive devices, and rehabilitation medicine, a Chinese company called Yueban debuted a smart toilet that does something we haven't see"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/952283/walmart-plus-half-off-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "A year of Walmart Plus is half off ahead of Prime Day",
    "url": "https://www.theverge.com/gadgets/952283/walmart-plus-half-off-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T17:33:00+00:00",
    "summary": "Do you often find yourself shopping at the big blue, or perhaps you’re just looking for an alternative to Amazon? Either way, Walmart is currently offering a year of its Walmart Plus subscription for "
  },
  {
    "id": "rss:https://www.theverge.com/tech/952354/firefox-home-page-widgets",
    "domain": "大厂 AI 动态",
    "title": "Firefox’s new home page widgets are helping me focus",
    "url": "https://www.theverge.com/tech/952354/firefox-home-page-widgets",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T17:29:50+00:00",
    "summary": "I launched Firefox this morning to find some new blocks on my home page. The widgets that are currently rolling out add sports scores, time zones, a focus timer, and a checklist, which are already som"
  },
  {
    "id": "rss:https://www.theverge.com/news/952264/the-onion-infowars-takeover-alex-jones-relaunch",
    "domain": "大厂 AI 动态",
    "title": "The Onion’s rebooted InfoWars is coming July 2nd",
    "url": "https://www.theverge.com/news/952264/the-onion-infowars-takeover-alex-jones-relaunch",
    "source": "Mia Sato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T17:00:00+00:00",
    "summary": "The Onion's InfoWars officially has a launch date: On July 2nd, the conspiracy network previously run by Alex Jones will return as a comedy and media platform. The reboot comes more than a year and a "
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/19/the-us-says-asmls-top-chip-tool-may-be-in-china-asml-says-it-isnt/",
    "domain": "大厂 AI 动态",
    "title": "The US says ASML’s top chip tool may be in China. ASML says it isn’t",
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
    "title": "Source: Elastic agrees to buy CRV-backed DeductiveAI for up to $85M",
    "url": "https://techcrunch.com/2026/06/18/source-elastic-agrees-to-buy-crv-backed-deductiveai-for-up-to-85m/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T00:51:11+00:00",
    "summary": "DeductiveAI, a startup that uses AI to catch and resolve bugs in software, was founded just three years ago."
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
    "id": "rss:https://techcrunch.com/2026/06/18/the-smartphone-era-created-an-attention-crisis-slowtech-is-fixing-it/",
    "domain": "大厂 AI 动态",
    "title": "The smartphone era created an attention crisis — slow tech is fixing it",
    "url": "https://techcrunch.com/2026/06/18/the-smartphone-era-created-an-attention-crisis-slowtech-is-fixing-it/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T17:16:30+00:00",
    "summary": "“People just really want to take back control of their time, their lives, their attention... They’re down for whatever helps them do that.”"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/texas-government-data-breach-allowed-hackers-to-steal-3-million-drivers-licenses-and-passports/",
    "domain": "大厂 AI 动态",
    "title": "Texas government data breach allowed hackers to steal 3 million driver’s licenses and passports",
    "url": "https://techcrunch.com/2026/06/18/texas-government-data-breach-allowed-hackers-to-steal-3-million-drivers-licenses-and-passports/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T17:12:53+00:00",
    "summary": "A data breach involving government-issued ID documents affects over 3 million people in Texas."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/queer-eyes-life-coach-karamo-brown-launches-ke-a-wellness-app-featuring-his-ai-digital-clone/",
    "domain": "大厂 AI 动态",
    "title": "‘Queer Eye’ life coach Karamo Brown launches Kē, a wellness app featuring his AI digital clone",
    "url": "https://techcrunch.com/2026/06/18/queer-eyes-life-coach-karamo-brown-launches-ke-a-wellness-app-featuring-his-ai-digital-clone/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T16:55:04+00:00",
    "summary": "After spending a year and a half focusing on his own journey — from fitness and nutrition to meditation, sobriety, relationships, and personal growth — Brown wants to help others do the same."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/apple-opens-up-app-store-to-new-competition-in-brazil/",
    "domain": "大厂 AI 动态",
    "title": "Apple opens up App Store to new competition in Brazil",
    "url": "https://techcrunch.com/2026/06/18/apple-opens-up-app-store-to-new-competition-in-brazil/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T15:48:08+00:00",
    "summary": "Apple’s grip on iPhone app distribution is loosening in another major market: Brazil."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/maptap-a-daily-geography-game-is-my-new-wordle/",
    "domain": "大厂 AI 动态",
    "title": "MapTap, a daily geography game, is my new Wordle",
    "url": "https://techcrunch.com/2026/06/18/maptap-a-daily-geography-game-is-my-new-wordle/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T15:47:39+00:00",
    "summary": "MapTap is a phone game that will make you feel smarter after you play it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/general-intuition-in-talks-to-raise-300m-at-around-2b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "General Intuition in talks to raise $300M at around $2B valuation",
    "url": "https://techcrunch.com/2026/06/18/general-intuition-in-talks-to-raise-300m-at-around-2b-valuation/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T15:20:37+00:00",
    "summary": "The startup trains embodied AI and world models using Medal’s dataset of 2 billion videos per year from 10 million monthly active users."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/a-tech-worker-backed-pac-is-bringing-a-5m-knife-to-big-techs-100m-gunfight/",
    "domain": "大厂 AI 动态",
    "title": "A tech worker-backed PAC is bringing a $5M knife to Big Tech’s $100M gunfight",
    "url": "https://techcrunch.com/2026/06/18/a-tech-worker-backed-pac-is-bringing-a-5m-knife-to-big-techs-100m-gunfight/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T15:13:21+00:00",
    "summary": "Guardrails positions itself as a populist political movement that runs on small donations from people in the trenches of the AI boom."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/18/spotifys-reserved-ticket-sales-to-musics-superfans-are-now-going-live/",
    "domain": "大厂 AI 动态",
    "title": "Spotify’s reserved ticket sales to music superfans are now going live",
    "url": "https://techcrunch.com/2026/06/18/spotifys-reserved-ticket-sales-to-musics-superfans-are-now-going-live/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T14:00:00+00:00",
    "summary": "Spotify is launching \"Reserved,\" a new system that will hold two concert tickets for an artist's superfans before they're on sale to the public."
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
    "id": "rss:https://stratechery.com/2026/the-state-of-fable-the-jailbreak-problem-spacex-acquires-cursor/",
    "domain": "大厂 AI 动态",
    "title": "The State of Fable, The Jailbreak Problem, SpaceX Acquires Cursor",
    "url": "https://stratechery.com/2026/the-state-of-fable-the-jailbreak-problem-spacex-acquires-cursor/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T10:00:00+00:00",
    "summary": "The administration is very likely wrong about Fable, but that is ultimately Anthropic's responsibility."
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
    "id": "rss:https://arstechnica.com/culture/2026/06/hulk-punisher-join-peter-parker-in-spider-man-brand-new-day-trailer/",
    "domain": "大厂 AI 动态",
    "title": "Hulk, Punisher join Peter Parker in Spider-Man: Brand New Day trailer",
    "url": "https://arstechnica.com/culture/2026/06/hulk-punisher-join-peter-parker-in-spider-man-brand-new-day-trailer/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T06:37:59+00:00",
    "summary": "Peter Parker to Bruce Banner: \"I didn't know you could get that big.\""
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/06/second-carcass-eating-fly-species-cleared-by-fda-for-maggot-wound-therapy/",
    "domain": "大厂 AI 动态",
    "title": "Second carcass-eating fly species cleared by FDA for maggot wound therapy",
    "url": "https://arstechnica.com/health/2026/06/second-carcass-eating-fly-species-cleared-by-fda-for-maggot-wound-therapy/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T22:11:20+00:00",
    "summary": "Maggot therapy lacks robust data, but it has fans and a fail-safe \"bacon therapy.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/amazon-quera-promise-useful-quantum-error-correction-by-2028/",
    "domain": "大厂 AI 动态",
    "title": "Sooner than expected? Useful quantum error correction promised for 2028.",
    "url": "https://arstechnica.com/science/2026/06/amazon-quera-promise-useful-quantum-error-correction-by-2028/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T20:44:32+00:00",
    "summary": "Elsewhere, beyond-classical quantum hardware, plus classical computing fires back."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/california-says-att-lied-to-fcc-in-attempt-to-shut-off-old-phone-network/",
    "domain": "大厂 AI 动态",
    "title": "California says AT&T lied to FCC in attempt to shut off old phone network",
    "url": "https://arstechnica.com/tech-policy/2026/06/california-says-att-lied-to-fcc-in-attempt-to-shut-off-old-phone-network/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T20:07:40+00:00",
    "summary": "FCC considers AT&#038;T petitions to preempt state rules and discontinue phone service."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/06/massive-breach-spills-credentials-for-thousands-of-sensitive-networks/",
    "domain": "大厂 AI 动态",
    "title": "Massive breach spills credentials for thousands of sensitive networks",
    "url": "https://arstechnica.com/security/2026/06/massive-breach-spills-credentials-for-thousands-of-sensitive-networks/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T19:54:31+00:00",
    "summary": "The affected include Oracle, Lenovo, FedEx, a NATO contractor, and Fortinet."
  },
  {
    "id": "rss:https://arstechnica.com/information-technology/2026/06/tesco-moving-40000-server-workloads-off-vmware-amid-broadcoms-abusive-conduct/",
    "domain": "大厂 AI 动态",
    "title": "Tesco moving 40,000 server workloads off VMware amid Broadcom's “abusive conduct”",
    "url": "https://arstechnica.com/information-technology/2026/06/tesco-moving-40000-server-workloads-off-vmware-amid-broadcoms-abusive-conduct/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T19:43:13+00:00",
    "summary": "Tesco claimed Broadcom hiked its VMware prices by about 175 percent in UK court filings."
  },
  {
    "id": "wscn:3775083",
    "domain": "股票",
    "title": "霍尔木兹海峡通航，对全球流动性有何影响？",
    "url": "https://wallstreetcn.com/articles/3775083",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T08:13:46+00:00",
    "summary": "海峡通航推动原油供需曲线双向扩张，资金从“脱虚向实”回流实体经济，导致剩余流动性收缩。这一过程引发两年美债利率飙升（源于货币基金赎回对短端利率的冲击）和美元指数上行，而并非源于美联储加息预期。30年美债利率回落则印证了长期通胀预期未变。短期赎回冲击不可持续，未来美债利率和美元指数将回落，2026年Q4美国仍具降息可能。"
  },
  {
    "id": "wscn:3775082",
    "domain": "股票",
    "title": "Kalshi年化营收突破20亿美元，较去年11月增长三倍，已与投行初步接洽IPO",
    "url": "https://wallstreetcn.com/articles/3775082",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T08:00:47+00:00",
    "summary": "受大型体育赛事交易推动，预测市场平台Kalshi年化营收突破20亿美元，较去年11月增长约三倍。公司预计最快2027年末或2028年上市。目前Kalshi正拓展机构业务，但面临竞争、监管诉讼及高管空缺等挑战。"
  },
  {
    "id": "wscn:3775080",
    "domain": "股票",
    "title": "161！日元跌至近40年低位，财长重申“将采取大胆行动”",
    "url": "https://wallstreetcn.com/articles/3775080",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T07:29:36+00:00",
    "summary": "日元跌至近40年低位，日本政府虽频频口头警告并豪掷逾700亿美元干预汇市，仍难敌美日高利差、套利交易与再通胀政策带来的结构性压力。市场正押注东京当局或突然出手救汇，但分析认为，只要美国高利率维持，日元弱势恐难根本逆转。"
  },
  {
    "id": "wscn:3775081",
    "domain": "股票",
    "title": "美伊会谈，推迟了",
    "url": "https://wallstreetcn.com/articles/3775081",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T07:28:56+00:00",
    "summary": "瑞士声明说，美国、伊朗、卡塔尔和巴基斯坦原定举行的会谈已被推迟。“瑞士仍愿为这些会谈提供便利。有关比尔根山的相关筹备工作也将继续进行。”"
  },
  {
    "id": "wscn:3775074",
    "domain": "股票",
    "title": "美伊瑞士会谈生变，韩股收跌0.1%，印度IT股大跌，纳指期货跌1%，美元指数站上101关口",
    "url": "https://wallstreetcn.com/articles/3775074",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T07:16:07+00:00",
    "summary": "韩国首尔综指收跌0.1%，报9051.95点。埃森哲下调全年营收指引，引发市场对全球科技服务需求前景的新一轮担忧，印度主要IT股周五大幅下跌。现货黄金日内跌逾2%，现货白银跌幅达3.4%。美元指数涨破101.00关口，创下2025年5月以来最高水平。"
  },
  {
    "id": "wscn:3775077",
    "domain": "股票",
    "title": "陈立武接手英特尔后首次播客访谈：我们的目标是“5-10年10倍”，押注先进封装、玻璃基板和人工钻石",
    "url": "https://wallstreetcn.com/articles/3775077",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T06:45:50+00:00",
    "summary": "英特尔CEO陈立武设定5至10年实现10倍回报的目标，正通过发力EMIB先进封装、玻璃基板及合成钻石等新材料，系统性重构技术路线图以突破物理极限。智能体AI爆发正带动CPU需求强劲回升；代工业务将聚焦良率与信任，并与马斯克共建Terafab项目，预计2030年后英特尔的真正潜力将全面显现。"
  },
  {
    "id": "wscn:3775075",
    "domain": "股票",
    "title": "沃什“鹰派首秀”，高盛下调黄金目标价，“如果今年真加息，金价会进一步下跌”",
    "url": "https://wallstreetcn.com/articles/3775075",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T05:11:53+00:00",
    "summary": "高盛将2026年底黄金目标价下调至4900美元，近期转为“战术谨慎”。报告警告，若秋季加息两次，金价恐跌至4440美元；但全球央行强劲的结构性购金趋势仍提供核心支撑，且中期地缘风险或推动金价突破6000美元。"
  },
  {
    "id": "wscn:3775062",
    "domain": "股票",
    "title": "上市一周上涨37%！市销率高达39倍，SpaceX已比所有标普500成分股“贵”",
    "url": "https://wallstreetcn.com/articles/3775062",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:27:50+00:00",
    "summary": "SpaceX上市首周收盘价185美元，较发行价135美元上涨37%，总市值达2.4万亿美元。以2027年预期市销率39.2倍计算，估值超越标普500所有成分股。分析师目标价从250美元到401美元不等，分歧悬殊。"
  },
  {
    "id": "wscn:3774776",
    "domain": "股票",
    "title": "氮化铝紧缺：1.6T时代的必选品，日本垄断75%份额诱发供应危机？",
    "url": "https://wallstreetcn.com/premium/articles/3774776?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:26:16+00:00",
    "summary": "全球高端氮化铝粉体供给高度集中——日本德山以约75%市场份额垄断全球，而国内2025年需求已达5600吨，国产产能不足2000吨，供需缺口高达3600吨，国产替代迫在眉睫。"
  },
  {
    "id": "wscn:3774897",
    "domain": "股票",
    "title": "下半年资产配置机会在哪里？听徐小庆、刘晨明展望2026下半年大类资产与A股策略如何布局！",
    "url": "https://wallstreetcn.com/articles/3774897",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:15:08+00:00",
    "summary": "6月21日刘晨明主讲Alpha线上闭门私享会：2026下半年A股策略如何布局？哪些资产最值得关注？"
  },
  {
    "id": "wscn:3775070",
    "domain": "股票",
    "title": "高通胀利好“折扣超市”！奥乐齐高歌猛进，美国市场份额增速堪比沃尔玛和Costco",
    "url": "https://wallstreetcn.com/articles/3775070",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T03:15:17+00:00",
    "summary": "高通胀推动美国消费者转向平价购物，德国折扣超市奥乐齐借势加速扩张，以每数日新增一店的速度向2028年3200家门店目标迈进。凭借精简运营和低价自有品牌，其市场份额增速已比肩沃尔玛、Costco等巨头，去年营收达300亿美元且逆势两位数增长。尽管面临侵权纠纷及一站式购物局限，奥乐齐正以长期主义策略强势冲击美国杂货零售格局。"
  },
  {
    "id": "wscn:3775072",
    "domain": "股票",
    "title": "油价跌回“伊战前水平”，市场反应过度了吗？",
    "url": "https://wallstreetcn.com/articles/3775072",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T03:14:23+00:00",
    "summary": "美伊签署框架协议并解封海峡，推动布伦特原油跌破77美元。但分析师警告，金融市场的复产预期与实际市场的供给吃紧存在背离：全球库存持续大减，而运费高企三倍、船东谨慎令物流面临瓶颈。市场虽已提前计入地缘溢价消除，但实际供应恢复仍需时日。"
  },
  {
    "id": "wscn:3775063",
    "domain": "股票",
    "title": "埃森哲股价暴跌18%创近十年新低，AI冲击与中东动荡双重施压",
    "url": "https://wallstreetcn.com/articles/3775063",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T02:39:50+00:00",
    "summary": "因中东局事拖累中东销售并致企业放慢决策，加之新签订单下滑，埃森哲下调全年营收指引，股价周四暴跌18%。此外，AI工具的快速演进也令投资者对该咨询巨头的核心商业模式和转型前景产生深度质疑。"
  },
  {
    "id": "wscn:3774983",
    "domain": "股票",
    "title": "锂电添加剂VC：淡季不淡仅是序章，Q3量价齐升或为高潮",
    "url": "https://wallstreetcn.com/premium/articles/3774983?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T02:35:05+00:00",
    "summary": "VC淡季不淡验证景气上行。"
  },
  {
    "id": "wscn:3775068",
    "domain": "股票",
    "title": "对冲7月加息风险！交易员涌入美债期货，交易量飙升创纪录",
    "url": "https://wallstreetcn.com/articles/3775068",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T02:01:23+00:00",
    "summary": "沃什发表鹰派讲话促使加息预期骤升，引发美国国债期货成交量创历史纪录。交易员大规模押注7月加息，导致市场对其定价概率从接近于零飙升至约五成，此前普遍存在的鸽派降息多头头寸正被系统性拆解。"
  },
  {
    "id": "wscn:3775067",
    "domain": "股票",
    "title": "“不是你想投，梁文锋就会要你的钱”，DeepSeek融资510亿元，他为何选了腾讯、宁德时代、网易、京东？",
    "url": "https://wallstreetcn.com/articles/3775067",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T01:45:59+00:00",
    "summary": "想投DeepSeek者众多，但梁文锋选资方更重产业协同。国资投资人分析，腾讯、京东、网易等入股意在协同自身AI战略；宁德时代参投，或为“算电协同”所需光伏储能提前卡位。有分析指出，此番开放融资，或源于DeepSeek意识到仅靠自有资金难跟上全球AI算力“军备竞赛”，需扩大资本开支以分散研发风险。"
  },
  {
    "id": "wscn:3775064",
    "domain": "股票",
    "title": "网友提问“中国大模型何时达到Fable级别？”，马斯克“可能明年Q1”，智谱CEO唐杰“不需要那么久”",
    "url": "https://wallstreetcn.com/articles/3775064",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T01:45:45+00:00",
    "summary": "智谱AI发布GLM-5.2后，研究员Teortaxes判断中国模型追赶上Fable级别模型需7个月。GLM-5.2在FrontierSWE基准上得74.4分，仅落后Opus 4.8约1个百分点。国产开源模型凭借性能、成本与自主可控优势，正重塑全球AI竞争格局。"
  },
  {
    "id": "wscn:3775065",
    "domain": "股票",
    "title": "SpaceX创纪录IPO后再发200亿美元债务，马斯克要做“当代联合太平洋铁路公司”",
    "url": "https://wallstreetcn.com/articles/3775065",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T01:32:37+00:00",
    "summary": "SpaceX完成创纪录IPO后，拟发债至少200亿美元。据分析师预测，其2031年净债务或超4000亿美元，年资本支出最高突破7000亿美元，主投AI与太空数据中心。马斯克以19世纪联合太平洋铁路自比，但专家指该公司实为“腐败烂账”，称此举“利用公众对历史的无知”；做空者亦指其援引反面案例“颇具讽刺意味”。"
  },
  {
    "id": "wscn:3775060",
    "domain": "股票",
    "title": "60天之后怎么办？美伊备忘录的真问题不是“和不和”而是……",
    "url": "https://wallstreetcn.com/premium/articles/3775060?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T01:22:16+00:00",
    "summary": "“抢时间”"
  },
  {
    "id": "wscn:3775066",
    "domain": "股票",
    "title": "霍尔木兹海峡已重开，但伊朗收费吗、找得到油轮吗？",
    "url": "https://wallstreetcn.com/articles/3775066",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T01:01:52+00:00",
    "summary": "霍尔木兹海峡封锁数月后重开，但因60天过渡期后的通行费谈判及管理机制存在悬念。美方表态模糊，导致航运业深感不安；同时运费飙升引发“无船可租”困境，亚洲炼油商已遭遇履约受阻和不可抗力。"
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
    "id": "rss:https://www.netinterest.co/p/new-pod-trends-in-us-banks-with-john",
    "domain": "股票",
    "title": "🎙️ Trends in US Banking: An Interview with John McDonald & Brian Foran",
    "url": "https://www.netinterest.co/p/new-pod-trends-in-us-banks-with-john",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-02-17T16:45:19+00:00",
    "summary": "Net Interest Extra ep 18"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.19517",
    "domain": "金融",
    "title": "Do Prediction Markets Match Option Prices? Bitcoin Threshold Evidence from Binance and Polymarket",
    "url": "https://arxiv.org/abs/2606.19517",
    "source": "Victoria Portnaya",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:00:00+00:00",
    "summary": "arXiv:2606.19517v1 Announce Type: new Abstract: The digitization of financial markets has produced two classes of platforms that price, in principle, the same state - contingent payoffs: centralized c"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.19550",
    "domain": "金融",
    "title": "Which Portfolios? The Construction Dependence of Factor Model Performance",
    "url": "https://arxiv.org/abs/2606.19550",
    "source": "Useong Shin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:00:00+00:00",
    "summary": "arXiv:2606.19550v1 Announce Type: new Abstract: Factor-model performance depends not only on the model but also on how test assets are constructed. We form characteristic-unsorted random portfolios fr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.19794",
    "domain": "金融",
    "title": "Forecasting AI-Era Productivity: The Intellectually Converged Human Framework and a Missing Cognitive Mediator in Production Function Theory",
    "url": "https://arxiv.org/abs/2606.19794",
    "source": "Kwan Soo Shin, In Seok Kang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:00:00+00:00",
    "summary": "arXiv:2606.19794v1 Announce Type: new Abstract: Why does massive AI investment fail to generate commensurate productivity gains? We argue the paradox is theoretically generated: prevailing production "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.19846",
    "domain": "金融",
    "title": "What Capital After Labor? Forecasting the Talent ROI Transition in the Human-AI Era",
    "url": "https://arxiv.org/abs/2606.19846",
    "source": "Kwan Soo Shin, In Seok Kang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:00:00+00:00",
    "summary": "arXiv:2606.19846v1 Announce Type: new Abstract: AI augmentation breaks the accounting link between labor time and productive contribution, yet firms continue to evaluate talent through time-based over"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.20041",
    "domain": "金融",
    "title": "AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models",
    "url": "https://arxiv.org/abs/2606.20041",
    "source": "Masahiro Kato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:00:00+00:00",
    "summary": "arXiv:2606.20041v1 Announce Type: new Abstract: We propose a model-grounded RAG-based AI economist with an agentic framework for economic scenario analysis using large language models (LLMs) and knowl"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.20079",
    "domain": "金融",
    "title": "How to spot outliers: an Ensemble Anomaly Detection Framework",
    "url": "https://arxiv.org/abs/2606.20079",
    "source": "Daniil Peysakhovich, Rafa{\\l} Sieradzki",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:00:00+00:00",
    "summary": "arXiv:2606.20079v1 Announce Type: new Abstract: Errors in risk valuation outputs arising from data-feed failures, model misconfiguration, or system malfunctions can propagate undetected through an inv"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.20145",
    "domain": "金融",
    "title": "Trends, Volatility, Correlations, and Critical Phenomena in Financial Markets",
    "url": "https://arxiv.org/abs/2606.20145",
    "source": "Sara A. Safari, Christoph Schmidhuber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:00:00+00:00",
    "summary": "arXiv:2606.20145v1 Announce Type: new Abstract: We forecast future volatilities and correlations of financial markets based on the current trends in these markets. This complements previous work that "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.20420",
    "domain": "金融",
    "title": "Advanced Calibration Analysis and Tools: Identifying Influential Observations in Stochastic Interest Rate Model Calibration",
    "url": "https://arxiv.org/abs/2606.20420",
    "source": "Philipp Mahler, Peter Ruckdeschel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:00:00+00:00",
    "summary": "arXiv:2606.20420v1 Announce Type: new Abstract: The accurate calibration of interest rate models is central to market-consistent valuation and Economic Scenario Generators (ESGs). Traditional calibrat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.20485",
    "domain": "金融",
    "title": "Optimal Order of Multi-Agent and General Many-Body Systems",
    "url": "https://arxiv.org/abs/2606.20485",
    "source": "Jake J. Xia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:00:00+00:00",
    "summary": "arXiv:2606.20485v1 Announce Type: new Abstract: This paper develops a general framework for analyzing multi-agent systems with feedback loops between agents actions and collective observations. The fr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.19777",
    "domain": "金融",
    "title": "Have Data Centers Raised Your Electric Bill? Causal Evidence from the United States",
    "url": "https://arxiv.org/abs/2606.19777",
    "source": "Asa Watten, John Bistline, Geoffrey Blanford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:00:00+00:00",
    "summary": "arXiv:2606.19777v1 Announce Type: cross Abstract: We estimate that data centers caused average retail electricity rates to fall modestly in the United States from 2015 to 2024 using an instrumental va"
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.19333",
    "domain": "金融",
    "title": "Swiss-system chess tournaments and unfairness",
    "url": "https://arxiv.org/abs/2410.19333",
    "source": "L\\'aszl\\'o Csat\\'o, Alex Krumer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:00:00+00:00",
    "summary": "arXiv:2410.19333v4 Announce Type: replace Abstract: The Swiss system is an increasingly popular competition format as it provides a favourable trade-off between the number of matches and ranking accur"
  },
  {
    "id": "rss:https://arxiv.org/abs/2503.13328",
    "domain": "金融",
    "title": "Model-independent upper bounds for the prices of Bermudan options with convex payoffs",
    "url": "https://arxiv.org/abs/2503.13328",
    "source": "David Hobson, Dominykas Norgilas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:00:00+00:00",
    "summary": "arXiv:2503.13328v3 Announce Type: replace Abstract: Suppose $\\mu$ and $\\nu$ are probability measures on $\\mathbb{R}$ satisfying $\\mu \\leq_{cx} \\nu$. Let $a$ and $b$ be convex functions on $\\mathbb{R}$"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.17422",
    "domain": "金融",
    "title": "Hired in High Season: Seasonal Labor Demand and Refugee Labor Market Integration",
    "url": "https://arxiv.org/abs/2512.17422",
    "source": "Felix Degenhardt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:00:00+00:00",
    "summary": "arXiv:2512.17422v2 Announce Type: replace Abstract: I examine whether early but temporary access to low-barrier hospitality employment affects refugees' labor market integration. I exploit within-regi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.16326",
    "domain": "金融",
    "title": "Gaming-Resistant Insurance Contracts for Autonomous AI Agents: Strategy-Proof Toll Mechanism Design",
    "url": "https://arxiv.org/abs/2606.16326",
    "source": "Hao-Hsuan Chen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T04:00:00+00:00",
    "summary": "arXiv:2606.16326v2 Announce Type: replace-cross Abstract: Paper A defines a time-consistent actuarial runtime that prices each side-effect-bearing action against a contractually fixed safe default and"
  }
]
```
