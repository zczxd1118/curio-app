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

- 今日日期：`2026-06-18`
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
  "date": "2026-06-18",
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
    "points": 3243513,
    "published_at": "2026-01-15T03:56:12+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1185238,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1NvRyBzEhq",
    "domain": "AI",
    "title": "全网最全！60分钟全面掌握Claude Code～【附完整文档】",
    "url": "http://www.bilibili.com/video/av116522328524431",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1185176,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1184439,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1w9MczyETB",
    "domain": "AI",
    "title": "【Vibe Coding】0基础项目实战教学丨Claude Code，Codex，Cursor教程",
    "url": "http://www.bilibili.com/video/av114669670898752",
    "source": "蛋黄酱拌巧克力",
    "platform": "bilibili",
    "points": 1031748,
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
    "points": 938600,
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
    "points": 717532,
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
    "points": 663259,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 572923,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 420363,
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
    "points": 414427,
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
    "points": 373361,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 371905,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 347423,
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
    "points": 329733,
    "published_at": "2025-07-14T15:01:39+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1GX9dYWEPw",
    "domain": "AI",
    "title": "我居然能在MC里玩到这么好玩的摸金服务器！",
    "url": "http://www.bilibili.com/video/av114108926068217",
    "source": "物骨",
    "platform": "bilibili",
    "points": 314711,
    "published_at": "2025-03-06T21:00:00+00:00",
    "summary": "视频内容均来自《LRL服务器》\n服务器游玩方式看评论区置顶\n无需正版，不卖数值，爆率嘎嘎高，不会跑路"
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 243528,
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
    "points": 237754,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中使用Claude Code agent并配置DeepSeek v4 model【闲谈】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸voov",
    "platform": "bilibili",
    "points": 230719,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "setting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, &quot;value&quot;: &quot;xxxx&"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 174724,
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
    "points": 156574,
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
    "points": 152628,
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
    "points": 143570,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 133736,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 132167,
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
    "points": 108883,
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
    "points": 104371,
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
    "points": 92209,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73212,
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
    "points": 64076,
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
    "points": 58646,
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
    "points": 51985,
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
    "points": 49262,
    "published_at": "2025-03-18T11:15:52+00:00",
    "summary": "视频制作不易，请一键三连！私我领取文档源码"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47098,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1rKjG6yEh2",
    "domain": "AI",
    "title": "10分钟+300个Agent：保姆级教程学会Agent Skills！【从零开始】",
    "url": "http://www.bilibili.com/video/av116758736279146",
    "source": "Work-Fisher",
    "platform": "bilibili",
    "points": 46712,
    "published_at": "2026-06-16T10:02:41+00:00",
    "summary": "这期我从最基础的概念，一路讲到上手实操，基本上是从 0 到 1，带你完整走一遍——一个 SKILL 到底是怎么从无到有做出来的。\n国内、国外的创建工具，我也都给你捋了一遍。希望看完这期，你也能动手做出一个真正属于自己的 SKIL。"
  },
  {
    "id": "bvid:BV1FzfoYSE4f",
    "domain": "AI",
    "title": "影刀AI Power零基础教程：02 智能体——打造企业AI超级员工",
    "url": "http://www.bilibili.com/video/av113888003622214",
    "source": "影刀RPA",
    "platform": "bilibili",
    "points": 40135,
    "published_at": "2025-02-06T02:00:00+00:00",
    "summary": "AI智能体：场景化智能助手，打造企业AI超级员工\n影刀AI Power，帮助企业将AI用起来。让每个员工都能拥有AI能力，在工作中使用AI解决问题。\n\n影刀AP企业版免费试用申请：http://s.winrobot360.com/g02tp\n影刀AP社区版使用：https://www.yingdao.com/ai-power/"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 38602,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 36677,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 36101,
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
    "points": 31689,
    "published_at": "2025-12-07T08:06:42+00:00",
    "summary": "下载地址：https://github.com/AAswordman/Operit\n\n相关软件资料下载：https://www.123pan.com/s/IKgAjv-Hinsv.html\n\n官方交流群：458862019"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29699,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 29077,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1HFDSBPE7b",
    "domain": "AI",
    "title": "3分钟教你部署ai我的世界陪玩！",
    "url": "http://www.bilibili.com/video/av116390124067729",
    "source": "我叫非主流_",
    "platform": "bilibili",
    "points": 27829,
    "published_at": "2026-04-12T11:45:00+00:00",
    "summary": "这是上期视频的教程，求求大家给个三连把="
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27336,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV1fWixBbEgP",
    "domain": "AI",
    "title": "别再用老方法了！Cocos Creator 3.8 + AI 开发实战：从0构建可商用的登录奖励模块",
    "url": "http://www.bilibili.com/video/av115840888408359",
    "source": "游戏主程进阶之路",
    "platform": "bilibili",
    "points": 19544,
    "published_at": "2026-01-05T05:43:24+00:00",
    "summary": "需 要 源 码 请 【＋O、O、裙】【822】【159】【534】"
  },
  {
    "id": "bvid:BV1hnjGzLE14",
    "domain": "AI",
    "title": "【小智教程】手挽手教你如何接入别人的MCP服务",
    "url": "http://www.bilibili.com/video/av114568722450105",
    "source": "空白泡泡糖果",
    "platform": "bilibili",
    "points": 17118,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV13sJcz9Egm",
    "domain": "AI",
    "title": "让AI替你打工！教你用Trae+MCP自动操作网页，采集数据，有手就能学会！mcp教程，mcp实战，mcp开发",
    "url": "http://www.bilibili.com/video/av114521544852773",
    "source": "大模型实战课程",
    "platform": "bilibili",
    "points": 16751,
    "published_at": "2025-05-17T05:36:05+00:00",
    "summary": "让AI替你打工！教你用Trae+MCP自动操作网页，采集数据，有手就能学会！mcp教程，mcp实战，mcp开发"
  },
  {
    "id": "bvid:BV1cCVZ6NEym",
    "domain": "AI",
    "title": "这绝对是B站讲的最全最细的VibeCoding系统教程，手把手带你从环境安装到实战，包含所有干货！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116673944492771",
    "source": "峰识在大模型",
    "platform": "bilibili",
    "points": 16022,
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
    "points": 15256,
    "published_at": "2026-06-15T05:37:28+00:00",
    "summary": "本套教程从零开始讲解，手把手教学！\n无论是新手小白，还是有一定基础的小伙伴皆可学习。\n如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！"
  },
  {
    "id": "bvid:BV1S3Eq6NE8c",
    "domain": "AI",
    "title": "快手P9专家讲解:Structured  Vibe Coding  从工具到方法的系统实战",
    "url": "http://www.bilibili.com/video/av116731490081424",
    "source": "印客学院-",
    "platform": "bilibili",
    "points": 14861,
    "published_at": "2026-06-11T12:42:38+00:00",
    "summary": "✅ 一套完整的方法论：从Karpathy原始定义到业界共识公式，彻底搞懂什么是“结构化Vibe Coding”\n✅ 四大工具品类全景图：App Builder / AI-Native IDE / Terminal Agent / Working Agent，找到最适合你的那一款\n✅ 新项目7步法：脑暴→规划→搭建→MVP→验证→硬化→迭代，每一步都有章可循\n✅ 30分钟Live Demo：现场用C"
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
    "source": "Simon Reuning",
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
    "id": "rss:https://www.eetimes.com/beyond-chiplets-cmos-2-0-moves-scaling-into-the-circuit/",
    "domain": "AI 算力 / 半导体",
    "title": "Beyond Chiplets, CMOS 2.0 Moves Scaling into the Circuit",
    "url": "https://www.eetimes.com/beyond-chiplets-cmos-2-0-moves-scaling-into-the-circuit/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T12:47:44+00:00",
    "summary": "Imec’s Zsolt Tokei and Arm’s Mohamed Awad explain why CMOS 2.0 could redefine semiconductor scaling beyond chiplets. The post Beyond Chiplets, CMOS 2.0 Moves Scaling into the Circuit appeared first on"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-isnt-the-real-bottleneck-in-autonomy-wireless-is/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Isn’t the Real Bottleneck in Autonomy; Wireless Is",
    "url": "https://www.eetimes.com/ai-isnt-the-real-bottleneck-in-autonomy-wireless-is/",
    "source": "Andrew Skafel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T08:37:54+00:00",
    "summary": "The future of drones, robotics, and autonomous systems will depend not only on AI, but also on reliable communications in congested, contested, and degraded environments. The post AI Isn’t the Real Bo"
  },
  {
    "id": "rss:https://www.eetimes.com/ee-times-magazine-june-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "EE Times Magazine – June 2026",
    "url": "https://www.eetimes.com/ee-times-magazine-june-2026/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T22:30:00+00:00",
    "summary": "The June 2026 edition of EE Times Magazine explores autonomous aerospace and defense systems—from orbital data centers to AI-enabled drones. The post EE Times Magazine – June 2026 appeared first on EE"
  },
  {
    "id": "rss:https://www.eetimes.com/sima-launches-agentic-development-environment-for-physical-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "SiMa Launches Agentic Development Environment for Physical AI",
    "url": "https://www.eetimes.com/sima-launches-agentic-development-environment-for-physical-ai/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T17:50:36+00:00",
    "summary": "Edge AI chip company said it can speed up engineer productivity when transferring to its hardware from months to hours. The post SiMa Launches Agentic Development Environment for Physical AI appeared "
  },
  {
    "id": "rss:https://www.eetimes.com/amd-snaps-mext-to-break-the-memory-wall/",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Snaps MEXT to Break the Memory Wall",
    "url": "https://www.eetimes.com/amd-snaps-mext-to-break-the-memory-wall/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T13:50:23+00:00",
    "summary": "AMD acquires MEXT to slash AI memory costs and break the memory wall. The post AMD Snaps MEXT to Break the Memory Wall appeared first on EE Times."
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
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/this-usd339-corsair-32gb-ddr5-ram-kit-is-the-cheapest-on-sale-right-now-usd45-less-than-the-next-best-rival-secure-overclockable-rgb-kit-with-6-000-mt-s-speeds-for-a-new-gaming-pc-build-and-beat-inevitable-future-price-rises",
    "domain": "AI 算力 / 半导体",
    "title": "This $339 Corsair 32GB DDR5 RAM kit is the cheapest on sale right now, $45 less than the next-best rival — secure overclockable RGB kit with 6,000 MT/s speeds for a new gaming PC build and beat inevit",
    "url": "https://www.tomshardware.com/pc-components/ddr5/this-usd339-corsair-32gb-ddr5-ram-kit-is-the-cheapest-on-sale-right-now-usd45-less-than-the-next-best-rival-secure-overclockable-rgb-kit-with-6-000-mt-s-speeds-for-a-new-gaming-pc-build-and-beat-inevitable-future-price-rises",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T10:31:14+00:00",
    "summary": "This 32GB Corsair Vengeance DDR5-6000 RAM kit is on sale at Woot for $339.99 right now, $45 less than its next-best rival."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/silicon-motions-client-pcie-6-x-roadmap-is-driven-by-nvidia-not-by-amd-and-intel-rtx-spark-agentic-ai-platform-could-fuel-a-hunger-for-storage-bandwidth",
    "domain": "AI 算力 / 半导体",
    "title": "SMI says Nvidia is driving its consumer PCIe 6.0 roadmap, not AMD and Intel — RTX Spark agentic AI platform fuels a hunger for storage bandwidth",
    "url": "https://www.tomshardware.com/pc-components/ssds/silicon-motions-client-pcie-6-x-roadmap-is-driven-by-nvidia-not-by-amd-and-intel-rtx-spark-agentic-ai-platform-could-fuel-a-hunger-for-storage-bandwidth",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T10:30:00+00:00",
    "summary": "Nvidia may be ahead of AMD and Intel with PCIe Gen6-supporting platform for client PCs due to its client agentic AI ambitions, and that roadmap has suppliers like Silicon Motion paying attention."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-silently-removes-memory-encryption-from-consumer-ryzen-cpus-leaving-users-unaware-that-they-may-be-vulnerable-security-feature-vanishes-after-newer-agesa-firmware-amd-engineers-go-radio-silent-when-pressed-about-the-change",
    "domain": "AI 算力 / 半导体",
    "title": "AMD silently removes memory encryption from consumer Ryzen CPUs, leaving users unaware that they may be vulnerable — security feature vanishes after newer AGESA firmware, AMD engineers go radio silent",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-silently-removes-memory-encryption-from-consumer-ryzen-cpus-leaving-users-unaware-that-they-may-be-vulnerable-security-feature-vanishes-after-newer-agesa-firmware-amd-engineers-go-radio-silent-when-pressed-about-the-change",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T10:00:00+00:00",
    "summary": "AMD has reportedly stripped TSME from consumer Ryzen processors after years of working support, with testing suggesting newer AGESA firmware disables the memory-encryption feature while Pro and EPYC C"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/chinese-memory-vendors-snub-industry-giants-in-favor-of-homegrown-ram-chips-samsung-micron-and-sk-hynix-face-a-chinese-supply-chain-revolt",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese memory brands ditch Samsung and Micron for homegrown CXMT and YMTC silicon — Corsair, HP, and Dell are already adopting the China-produced DDR5 chips",
    "url": "https://www.tomshardware.com/pc-components/ram/chinese-memory-vendors-snub-industry-giants-in-favor-of-homegrown-ram-chips-samsung-micron-and-sk-hynix-face-a-chinese-supply-chain-revolt",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T09:30:00+00:00",
    "summary": "Chinese memory brands Gloway and KingBank have begun using homemade chips to produce DDR5 memory kits in lieu of Samsung, Micron, or SK hynix DRAM."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intels-performance-enhanced-18a-p-process-enters-risk-production-enhanced-node-promises-9-percent-performance-improvement-at-iso-power",
    "domain": "AI 算力 / 半导体",
    "title": "Intel’s performance-enhanced 18A-P process enters risk production — drop-in 18A upgrade promises 9% performance improvement at iso-power, cuts thermal resistance by 40%",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intels-performance-enhanced-18a-p-process-enters-risk-production-enhanced-node-promises-9-percent-performance-improvement-at-iso-power",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T21:00:00+00:00",
    "summary": "Intel's enhanced 18A-P has entered risk production, laying the groundwork to ramp the node into full production in the coming months."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/dells-usd699-xps-13-laptop-is-now-available-with-the-macbook-neo-in-its-sights-entry-level-xps-design-comes-with-wildcat-lake-8gb-of-ram-and-a-512gb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Dell's $699 XPS 13 laptop is now available with the MacBook Neo in its sights — entry-level XPS design comes with Wildcat Lake, 8GB of RAM, and a 512GB SSD",
    "url": "https://www.tomshardware.com/laptops/dells-usd699-xps-13-laptop-is-now-available-with-the-macbook-neo-in-its-sights-entry-level-xps-design-comes-with-wildcat-lake-8gb-of-ram-and-a-512gb-ssd",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T17:22:07+00:00",
    "summary": "Dell's $699 XPS 13 laptop ($599 for students) has the MacBook Neo in its sights, and it's now available sporting one of Intel's new entry-level Wildcat Lake CPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/sandisk-optimus-gx-pro-8100-8tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "SanDisk Optimus GX Pro 8100 8TB SSD Review — the undisputed king of high-capacity PCIe 5.0 SSDs",
    "url": "https://www.tomshardware.com/pc-components/ssds/sandisk-optimus-gx-pro-8100-8tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T16:30:43+00:00",
    "summary": "The SanDisk Optimus GX Pro 8100 is a top-tier drive with excellent performance, exceptional random read latency, and good power efficiency. As you'd imagine, it just has a pricing issue."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/build-an-elite-amd-gaming-pc-around-gigabytes-x870-motherboard-for-usd70-off-gigabyte-x870-aorus-elite-wifi7-drops-to-usd249",
    "domain": "AI 算力 / 半导体",
    "title": "Build an elite AMD gaming PC around Gigabyte's X870 motherboard for $70 off — Gigabyte X870 Aorus Elite WiFi7 drops to $249",
    "url": "https://www.tomshardware.com/pc-components/motherboards/build-an-elite-amd-gaming-pc-around-gigabytes-x870-motherboard-for-usd70-off-gigabyte-x870-aorus-elite-wifi7-drops-to-usd249",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T16:30:00+00:00",
    "summary": "The Gigabyte X870 Aorus Elite WiFi7 usually retails for $319..99, but the premium motherboard has gone on sale for $249.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/logitechs-new-g305-x-superlight-weighs-just-59-grams-and-costs-usd79-company-also-releases-new-hot-swappable-g316-x-98-keyboard",
    "domain": "AI 算力 / 半导体",
    "title": "Logitech's new G305 X Superlight weighs just 59 grams and costs $79 — company also releases hot-swappable G316 X 98 keyboard with pixel display, translucent control knob",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/logitechs-new-g305-x-superlight-weighs-just-59-grams-and-costs-usd79-company-also-releases-new-hot-swappable-g316-x-98-keyboard",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T16:05:05+00:00",
    "summary": "Logitech's latest gaming peripherals include a redesigned 59-gram G305 X Superlight mouse with 8,000 Hz polling and a customizable G316 X 98 mechanical keyboard featuring hot-swappable switches and a "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/the-retail-ssd-market-has-almost-disappeared-says-silicon-motion-exec-pc-oems-are-buying-third-party-drives-as-direct-nand-supply-dries-up",
    "domain": "AI 算力 / 半导体",
    "title": "'The retail SSD market has almost disappeared,' says Silicon Motion exec — PC OEMs are buying third-party drives as direct NAND supply dries up",
    "url": "https://www.tomshardware.com/pc-components/ssds/the-retail-ssd-market-has-almost-disappeared-says-silicon-motion-exec-pc-oems-are-buying-third-party-drives-as-direct-nand-supply-dries-up",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T15:27:52+00:00",
    "summary": "Vice president of client storage solutions at Silicon Motion warns that the retail SSD market has almost disappeared as NAND makers prioritize shipments of memory to AI data centers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/semianalysis-opens-its-own-chip-teardown-lab",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese fab SMIC's 7nm metal pitch beats Intel 18A but lags 38% on density, teardown finds — Huawei's sanctions-beating HiSilicon Kirin 9030 is the first subject of SemiAnalysis's new teardown lab",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/semianalysis-opens-its-own-chip-teardown-lab",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T15:06:00+00:00",
    "summary": "SemiAnalysis has published the first teardown from its new in-house lab, focusing on the minimum local metal pitch on SMIC’s third-gen 7nm at 32.5nm."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/noctua-finally-releases-its-first-aio-coolers-prices-start-at-usd220-for-240mm-features-the-companys-legendary-a-series-fans",
    "domain": "AI 算力 / 半导体",
    "title": "Noctua finally releases its first AIO coolers — prices start at $220 for 240mm, features the company’s legendary A-series fans",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/noctua-finally-releases-its-first-aio-coolers-prices-start-at-usd220-for-240mm-features-the-companys-legendary-a-series-fans",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T14:05:03+00:00",
    "summary": "Noctua just dropped its NL-LC1 AIO coolers on Amazon, with the 240mm option starting at $219.95. It also comes with an optional 80mm auxiliary fan to help keep other components cooler and reduce case "
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/18-funky-tech-gift-ideas-for-fathers-day-2026-get-something-a-little-different-for-dad-this-year",
    "domain": "AI 算力 / 半导体",
    "title": "18 funky tech gift ideas for Father's Day 2026 — get something a little different for dad this year",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/18-funky-tech-gift-ideas-for-fathers-day-2026-get-something-a-little-different-for-dad-this-year",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T14:00:00+00:00",
    "summary": "Celebrate Father's Day this Sunday, the 21st of June, by getting your pops a nice little tech gift for his collection."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/smis-pcie-6-0-ssd-controller-for-consumer-ssds-coming-next-year-but-severe-nand-shortages-will-get-even-worse-in-2027-as-ai-data-centers-swallow-supply-an-interview-with-silicon-motions-svp-nelson-duann",
    "domain": "AI 算力 / 半导体",
    "title": "SMI's PCIe 6.0 SSD controller for consumer SSDs coming next year, but severe NAND shortages will get even worse in 2027 as AI data centers swallow supply — An interview with Silicon Motion's SVP Nelso",
    "url": "https://www.tomshardware.com/pc-components/ssds/smis-pcie-6-0-ssd-controller-for-consumer-ssds-coming-next-year-but-severe-nand-shortages-will-get-even-worse-in-2027-as-ai-data-centers-swallow-supply-an-interview-with-silicon-motions-svp-nelson-duann",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T13:30:00+00:00",
    "summary": "Silicon Motion's Nelson Duann discusses NAND supply crisis in the consumer SSD market and the future of consumer storage."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/msi-mpg-coreliquid-p22-360-review",
    "domain": "AI 算力 / 半导体",
    "title": "MSI MPG Coreliquid P22 360 Review: Low noise, strong performance, budget price",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/msi-mpg-coreliquid-p22-360-review",
    "source": "Albert Thomas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T13:00:00+00:00",
    "summary": "The MSI MPG Coreliquid P22 360 is a new AIO with a low price tag, strong thermal performance, and a 2.1-inch IPS display. We’ve tested this liquid cooler paired with AMD’s Ryzen 9 9950X3D CPU to bench"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/microsoft-debuts-surface-pro-and-surface-laptop-with-new-jade-green-color-and-qualcomm-snapdragon-x2-chips-refreshed-devices-start-at-usd1-499-with-16gb-of-ram",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft debuts Surface Pro and Surface Laptop with new jade green color and Qualcomm Snapdragon X2 chips — refreshed devices start at $1,499 with 16GB of RAM",
    "url": "https://www.tomshardware.com/laptops/microsoft-debuts-surface-pro-and-surface-laptop-with-new-jade-green-color-and-qualcomm-snapdragon-x2-chips-refreshed-devices-start-at-usd1-499-with-16gb-of-ram",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T13:00:00+00:00",
    "summary": "Microsoft is updating the Surface Pro and Surface Laptop using the latest Qualcomm Snapdragon X2 chips, along with haptic feedback on the Laptop's touchpad and a new jade color."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/qualcomm-mulls-taking-over-jim-kellers-tenstorrent-report-claims-deal-for-ai-chipmaker-would-value-the-company-at-between-usd8-billion-and-usd10-billion",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm mulls taking over Jim Keller's Tenstorrent, report claims — deal for AI chipmaker would value the company at between $8 billion and $10 billion",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/qualcomm-mulls-taking-over-jim-kellers-tenstorrent-report-claims-deal-for-ai-chipmaker-would-value-the-company-at-between-usd8-billion-and-usd10-billion",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T12:48:21+00:00",
    "summary": "Qualcomm is in talks to buy RISC-V-based AI accelerator and CPU developer Tenstorrent for $8 billion - $10 billion."
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
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/952011/midjourney-medical-ai-ultrasound-scan",
    "domain": "大厂 AI 动态",
    "title": "Midjourney goes from generating cat images to full-body ultrasound scans",
    "url": "https://www.theverge.com/ai-artificial-intelligence/952011/midjourney-medical-ai-ultrasound-scan",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T03:12:31+00:00",
    "summary": "Midjourney CEO David Holz just showed off the company's first hardware product and plans to build a San Francisco spa, which he admitted is a bit different from the \"cat pictures\" produced by its AI i"
  },
  {
    "id": "rss:https://www.theverge.com/tech/951948/apple-tim-cook-price-increases-ram",
    "domain": "大厂 AI 动态",
    "title": "Tim Cook says RAM expenses are &#8216;unsustainable&#8217; and Apple is going to raise prices",
    "url": "https://www.theverge.com/tech/951948/apple-tim-cook-price-increases-ram",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T21:42:21+00:00",
    "summary": "Apple is planning to raise prices in response to the ongoing memory shortage. In an interview with The Wall Street Journal, Apple CEO Tim Cook says \"price increases are unavoidable:\" We're doing our b"
  },
  {
    "id": "rss:https://www.theverge.com/tech/951863/vsco-studio-pro-vsco-one-subscription",
    "domain": "大厂 AI 动态",
    "title": "VSCO launches Studio Pro mobile photo editing app and plans $500 per year subscription",
    "url": "https://www.theverge.com/tech/951863/vsco-studio-pro-vsco-one-subscription",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T20:43:28+00:00",
    "summary": "VSCO is taking on Adobe with a new Studio Pro editing app rolling out today on iOS and coming to macOS later this year, as Bloomberg reports. At launch, the app offers tools for batch editing, style m"
  },
  {
    "id": "rss:https://www.theverge.com/games/951785/epic-games-fortnite-unreal-fest-2026-unreal-engine-6-ai-metaverse",
    "domain": "大厂 AI 动态",
    "title": "Epic wants to let you bring your Fortnite skins to other games",
    "url": "https://www.theverge.com/games/951785/epic-games-fortnite-unreal-fest-2026-unreal-engine-6-ai-metaverse",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T19:09:00+00:00",
    "summary": "Epic Games has been touting the potential of an interoperable metaverse for years, though that vision hasn't yet become a reality. But with Unreal Engine 6, the next major version of its game developm"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/951703/anthropic-shutdown-export-controls",
    "domain": "大厂 AI 动态",
    "title": "Anthropic got hit by export rules nobody understands",
    "url": "https://www.theverge.com/ai-artificial-intelligence/951703/anthropic-shutdown-export-controls",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T18:28:50+00:00",
    "summary": "Anthropic has spent much of this week fighting to get its newest AI models back online after the Trump administration abruptly ordered the company to cut access for all foreign nationals, including us"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/951653/pew-research-ai-chatbot-usage-advancing-too-quickly",
    "domain": "大厂 AI 动态",
    "title": "Two-thirds of Americans think AI is advancing too quickly",
    "url": "https://www.theverge.com/ai-artificial-intelligence/951653/pew-research-ai-chatbot-usage-advancing-too-quickly",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T17:20:24+00:00",
    "summary": "According to the latest Pew Research poll, 49 percent of Americans report using chatbots at least occasionally, but 63 percent think the tech is advancing too quickly. Overall, use of AI chatbots has "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/951602/amazon-echo-dot-max-early-prime-day-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The Echo Dot Max is cheaper than ever in an early Prime Day sale",
    "url": "https://www.theverge.com/gadgets/951602/amazon-echo-dot-max-early-prime-day-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T16:47:43+00:00",
    "summary": "We’re seeing good early Prime Day deals ahead of the event next week, and unsurprisingly, some of the best deals are on Amazon&#8217;s own devices. Several Echo speakers have dropped to new low prices"
  },
  {
    "id": "rss:https://www.theverge.com/column/951516/trump-anthropic-feud-mythos-fable-white-house",
    "domain": "大厂 AI 动态",
    "title": "Vibe-decoding the White House-Anthropic fight over Fable",
    "url": "https://www.theverge.com/column/951516/trump-anthropic-feud-mythos-fable-white-house",
    "source": "Tina Nguyen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T16:27:00+00:00",
    "summary": "Hello and welcome to Regulator, an email for Verge subscribers about technology, politics, and what happens when science crashes headlong into self-interest. Not a subscriber? Sign up here today! Got "
  },
  {
    "id": "rss:https://www.theverge.com/report/951481/snap-specs-wearables-smart-glasses-fashion",
    "domain": "大厂 AI 动态",
    "title": "Can anyone look cool wearing Snap’s $2,000 glasses?",
    "url": "https://www.theverge.com/report/951481/snap-specs-wearables-smart-glasses-fashion",
    "source": "Victoria Song",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T16:13:34+00:00",
    "summary": "Yesterday, Snap debuted its new $2,195 Specs glasses. In an interview with CNBC, Snap CEO Evan Spiegel described the Specs as something the company had been working on for more than 12 years, an attem"
  },
  {
    "id": "rss:https://www.theverge.com/games/951533/gta-v-ps5-xbox-series-x-upgrade",
    "domain": "大厂 AI 动态",
    "title": "We got free GTA V upgrades before GTA VI",
    "url": "https://www.theverge.com/games/951533/gta-v-ps5-xbox-series-x-upgrade",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T15:45:36+00:00",
    "summary": "Rockstar Games will allow players to upgrade older versions of Grand Theft Auto V for PlayStation 5 and Xbox Series X / S for free just months before the launch of GTA VI. Starting June 18th, players "
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/nasa-picks-eric-schmidts-rocket-company-for-mars-mission-setting-up-a-race-with-spacex/",
    "domain": "大厂 AI 动态",
    "title": "NASA picks Eric Schmidt’s rocket company for Mars mission, setting up a race with SpaceX",
    "url": "https://techcrunch.com/2026/06/17/nasa-picks-eric-schmidts-rocket-company-for-mars-mission-setting-up-a-race-with-spacex/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T06:26:24+00:00",
    "summary": "Relativity Space—a rocket maker acquired by former Google executive chair Eric Schmidt last year after stumbling on the path to orbit—might just beat SpaceX to Mars."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/how-to-turn-off-ai-in-your-google-docs/",
    "domain": "大厂 AI 动态",
    "title": "How to turn off AI in your Google Docs",
    "url": "https://techcrunch.com/2026/06/17/how-to-turn-off-ai-in-your-google-docs/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T01:23:51+00:00",
    "summary": "Here's what you need to do to get those pesky \"write with Gemini\" pop-ups to go away."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/ai-is-hurting-apple-in-more-ways-than-one-it-may-force-iphone-price-increases/",
    "domain": "大厂 AI 动态",
    "title": "AI is hurting Apple in more ways than one: it may force iPhone price increases",
    "url": "https://techcrunch.com/2026/06/17/ai-is-hurting-apple-in-more-ways-than-one-it-may-force-iphone-price-increases/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T23:28:21+00:00",
    "summary": "CEO Tim Cook said in a recent interview that the situation is \"unsustainable.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/chi-hua-chien-saw-facebook-coming-now-he-says-the-real-ai-winners-wont-be-selling-ai/",
    "domain": "大厂 AI 动态",
    "title": "Chi-Hua Chien saw Facebook coming — now he says the real AI winners won’t be selling AI",
    "url": "https://techcrunch.com/2026/06/17/chi-hua-chien-saw-facebook-coming-now-he-says-the-real-ai-winners-wont-be-selling-ai/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T21:30:50+00:00",
    "summary": "Chi-Hua Chien has spent more than two decades as a venture capitalist, but he thinks like a cultural anthropologist."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/roelof-botha-joins-spacexs-board-of-directors/",
    "domain": "大厂 AI 动态",
    "title": "Roelof Botha joins SpaceX’s board of directors",
    "url": "https://techcrunch.com/2026/06/17/roelof-botha-joins-spacexs-board-of-directors/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T20:32:52+00:00",
    "summary": "The former Sequoia Capital leader is filling an \"existing vacancy\" on SpaceX's board, days after the company went public in the largest IPO ever."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/after-unveiling-ridiculously-expensive-ar-glasses-snaps-stock-takes-a-dive/",
    "domain": "大厂 AI 动态",
    "title": "After unveiling ridiculously expensive AR glasses, Snap’s stock takes a dive",
    "url": "https://techcrunch.com/2026/06/17/after-unveiling-ridiculously-expensive-ar-glasses-snaps-stock-takes-a-dive/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T20:24:28+00:00",
    "summary": "Snap's long-awaited smart glasses debut hasn't exactly done wonders for the company's stock."
  },
  {
    "id": "rss:https://techcrunch.com/video/neas-tiffany-luck-says-enterprises-are-still-figuring-out-their-ai-roi/",
    "domain": "大厂 AI 动态",
    "title": "NEA’s Tiffany Luck says enterprises are still figuring out their AI ROI",
    "url": "https://techcrunch.com/video/neas-tiffany-luck-says-enterprises-are-still-figuring-out-their-ai-roi/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T20:17:38+00:00",
    "summary": "Tokenmaxxing&#160;was&#160;the hottest trend in Silicon Valley earlier this year, with CEOs encouraging employees to push AI usage as far&#160;as it would go.&#160;Then the bill came due. Uber&#160;re"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/ftc-lawsuit-reveals-how-subscription-scam-networks-evade-app-store-enforcement/",
    "domain": "大厂 AI 动态",
    "title": "FTC lawsuit reveals how subscription scam networks evade app store enforcement",
    "url": "https://techcrunch.com/2026/06/17/ftc-lawsuit-reveals-how-subscription-scam-networks-evade-app-store-enforcement/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T19:46:16+00:00",
    "summary": "A new FTC lawsuit reveals how sophisticated subscription app operators can allegedly use shell companies and payment infrastructure to stay active on app stores despite mounting consumer complaints."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/world-leaders-want-american-ai-they-just-dont-want-america-to-be-able-to-turn-it-off/",
    "domain": "大厂 AI 动态",
    "title": "World leaders want American AI. They just don’t want America to be able to turn it off.",
    "url": "https://techcrunch.com/2026/06/17/world-leaders-want-american-ai-they-just-dont-want-america-to-be-able-to-turn-it-off/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T19:01:19+00:00",
    "summary": "French President Macron and Indian PM Modi raised alarms at the G7 summit that the U.S. could cut off access to American AI overnight — a fear the Anthropic blackout just made real."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/anthropic-becomes-first-ai-startup-to-join-the-frontier-carbon-removal-coalition/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic becomes first AI startup to join the Frontier carbon removal coalition",
    "url": "https://techcrunch.com/2026/06/17/anthropic-becomes-first-ai-startup-to-join-the-frontier-carbon-removal-coalition/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T18:30:56+00:00",
    "summary": "Anthropic has joined the Frontier coalition, which received another $915M in pledges to fund carbon removal projects."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/cybercriminals-allegedly-hacked-tens-of-thousands-of-fortinet-firewalls-used-by-major-companies-all-over-the-world/",
    "domain": "大厂 AI 动态",
    "title": "Cybercriminals allegedly hacked tens of thousands of Fortinet firewalls used by major companies all over the world",
    "url": "https://techcrunch.com/2026/06/17/cybercriminals-allegedly-hacked-tens-of-thousands-of-fortinet-firewalls-used-by-major-companies-all-over-the-world/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T18:20:06+00:00",
    "summary": "An alleged Russian-speaking group of cybercriminals is reportedly compromising and targeting several major companies that use Fortinet Firewalls and VPNs through previously known passwords."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/social-medias-next-evolution-user-controlled-algorithms/",
    "domain": "大厂 AI 动态",
    "title": "Social media’s next evolution: user-controlled algorithms",
    "url": "https://techcrunch.com/2026/06/17/social-medias-next-evolution-user-controlled-algorithms/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T18:19:48+00:00",
    "summary": "Social media feeds are becoming more customizable as platforms like Threads, Instagram, and TikTok introduce tools that let users directly influence the algorithms powering their recommendations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/world-model-maker-odyssey-nabs-1-45b-valuation-backed-by-amazon-and-other-big-names/",
    "domain": "大厂 AI 动态",
    "title": "World model maker Odyssey nabs $1.45B valuation backed by Amazon and other big names",
    "url": "https://techcrunch.com/2026/06/17/world-model-maker-odyssey-nabs-1-45b-valuation-backed-by-amazon-and-other-big-names/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T17:43:07+00:00",
    "summary": "World models are the next big thing in AI beyond LLMs and, with this round, Odyssey has cemented itself as one of the startups to watch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/mastodon-looks-to-newsletters-to-help-revive-the-open-social-web/",
    "domain": "大厂 AI 动态",
    "title": "Mastodon looks to newsletters to help revive the open social web",
    "url": "https://techcrunch.com/2026/06/17/mastodon-looks-to-newsletters-to-help-revive-the-open-social-web/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T17:38:01+00:00",
    "summary": "Mastodon’s newly launched newsletter feature lets anyone subscribe to creators by email, even without a Mastodon account."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/only-16-percent-of-americans-think-ai-will-have-a-positive-impact-on-society-a-new-study-shows/",
    "domain": "大厂 AI 动态",
    "title": "Only 16 percent of Americans think AI will have a positive impact on society, a new study shows",
    "url": "https://techcrunch.com/2026/06/17/only-16-percent-of-americans-think-ai-will-have-a-positive-impact-on-society-a-new-study-shows/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T17:00:01+00:00",
    "summary": "Although Wall Street loves AI, every day Americans are significantly less optimistic about the industry, a new report from Pew Research shows."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/two-stanford-grads-raise-11m-to-build-a-noninvasive-wearable-for-hormone-tracking/",
    "domain": "大厂 AI 动态",
    "title": "Two Stanford grads raise $11M to build a noninvasive wearable for hormone tracking",
    "url": "https://techcrunch.com/2026/06/17/two-stanford-grads-raise-11m-to-build-a-noninvasive-wearable-for-hormone-tracking/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T16:54:48+00:00",
    "summary": "Clair Health will track inflammation and bloating markers, energy levels, and cycle phase classification to give insights into cycle irregularities and perimenopause, as well as hormonal fluctuations,"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/google-bets-on-gemini-to-reinvent-the-smart-home-speaker/",
    "domain": "大厂 AI 动态",
    "title": "Google bets on Gemini to reinvent the smart home speaker",
    "url": "https://techcrunch.com/2026/06/17/google-bets-on-gemini-to-reinvent-the-smart-home-speaker/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T16:30:09+00:00",
    "summary": "Google is betting generative AI can breathe new life into the smart speaker. The company's new $99.99 Google Home Speaker replaces the rigid commands of the Google Assistant era with more conversation"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/paypal-ventures-shutters-as-company-restructuring-continues/",
    "domain": "大厂 AI 动态",
    "title": "PayPal Ventures shutters as company restructuring continues",
    "url": "https://techcrunch.com/2026/06/17/paypal-ventures-shutters-as-company-restructuring-continues/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T16:10:13+00:00",
    "summary": "The corporate venture arm ends after 10 years and 80 investments."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/the-slowtech-revolution-is-here-to-kill-your-phone-addiction-and-rescue-your-attention-span/",
    "domain": "大厂 AI 动态",
    "title": "The slowtech revolution is here to kill your phone addiction and rescue your attention span",
    "url": "https://techcrunch.com/2026/06/17/the-slowtech-revolution-is-here-to-kill-your-phone-addiction-and-rescue-your-attention-span/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T15:24:41+00:00",
    "summary": "“People just really want to take back control of their time, their lives, their attention... They’re down for whatever helps them do that.”"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/17/collecting-robot-training-data-is-dirty-unglamorous-work-some-ai-labs-are-already-paying-xdof-to-do-it/",
    "domain": "大厂 AI 动态",
    "title": "Collecting robot training data is dirty, unglamorous work. Some AI labs are already paying XDOF to do it.",
    "url": "https://techcrunch.com/2026/06/17/collecting-robot-training-data-is-dirty-unglamorous-work-some-ai-labs-are-already-paying-xdof-to-do-it/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T15:00:00+00:00",
    "summary": "If physical AI is going to match the accomplishments of LLMs, there's a data problem that needs to be solved."
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
    "id": "rss:https://stratechery.com/2026/fox-buys-roku-the-problem-with-foxs-smart-strategy-streaming-that-works/",
    "domain": "大厂 AI 动态",
    "title": "Fox Buys Roku, The Problem With Fox’s Smart Strategy, Streaming That Works",
    "url": "https://stratechery.com/2026/fox-buys-roku-the-problem-with-foxs-smart-strategy-streaming-that-works/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T10:00:00+00:00",
    "summary": "The market hates Fox's acquisition of Roku, but the company is trading extraction from rights holders for leverage as a renter."
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
    "id": "rss:https://arstechnica.com/ai/2026/06/ai-coding-agents-can-autonomously-direct-robot-training/",
    "domain": "大厂 AI 动态",
    "title": "AI coding agents taught robots how to install GPUs and cut zip ties",
    "url": "https://arstechnica.com/ai/2026/06/ai-coding-agents-can-autonomously-direct-robot-training/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T19:25:19+00:00",
    "summary": "Nvidia's self-improvement program for robots enlists teams of AI coding agents."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/06/the-slate-trucks-price-may-have-leaked-starts-at-24950/",
    "domain": "大厂 AI 动态",
    "title": "The Slate Truck's price may have leaked, starts at $24,950",
    "url": "https://arstechnica.com/cars/2026/06/the-slate-trucks-price-may-have-leaked-starts-at-24950/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T18:23:21+00:00",
    "summary": "The official launch takes place next week."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/dangerous-ai-models-are-coming-no-matter-what/",
    "domain": "大厂 AI 动态",
    "title": "\"Dangerous\" AI models are coming no matter what",
    "url": "https://arstechnica.com/ai/2026/06/dangerous-ai-models-are-coming-no-matter-what/",
    "source": "Lily Hay Newman, WIRED.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T17:50:46+00:00",
    "summary": "AI models with advanced hacking capabilities will soon be the norm."
  },
  {
    "id": "rss:https://arstechnica.com/google/2026/06/the-gemini-powered-google-home-speaker-arrives-on-june-25-for-100/",
    "domain": "大厂 AI 动态",
    "title": "Ten months later, the $100 Google Home Speaker is finally available for preorder",
    "url": "https://arstechnica.com/google/2026/06/the-gemini-powered-google-home-speaker-arrives-on-june-25-for-100/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T15:57:14+00:00",
    "summary": "Google's new smart speaker is more about Gemini than audio quality."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/towers-once-planned-for-california-shuttle-launches-leveled-for-spacex-rockets/",
    "domain": "大厂 AI 动态",
    "title": "Towers once planned for California shuttle launches leveled for SpaceX rockets",
    "url": "https://arstechnica.com/space/2026/06/towers-once-planned-for-california-shuttle-launches-leveled-for-spacex-rockets/",
    "source": "Robert Pearlman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T15:47:09+00:00",
    "summary": "\"Space Launch Complex-6 represents six decades of American innovation.\""
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/06/truly-evil-fda-rejection-of-gene-therapy-overturned-after-trump-official-ousted/",
    "domain": "大厂 AI 动态",
    "title": "\"Truly evil\" FDA rejection of gene therapy overturned after Trump official ousted",
    "url": "https://arstechnica.com/health/2026/06/truly-evil-fda-rejection-of-gene-therapy-overturned-after-trump-official-ousted/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T15:12:31+00:00",
    "summary": "Gene therapy company UniQure had another FDA meeting after Vinay Prasad's exit."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/06/native-nacs-ports-infotainment-upgrade-for-my27-porsche-taycan/",
    "domain": "大厂 AI 动态",
    "title": "Native NACS ports, infotainment upgrade for MY27 Porsche Taycan",
    "url": "https://arstechnica.com/cars/2026/06/native-nacs-ports-infotainment-upgrade-for-my27-porsche-taycan/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T12:00:45+00:00",
    "summary": "The bigger battery is standard and there are now simulated \"E-Shifts.\""
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/06/windows-and-linux-users-the-deadline-to-update-secure-boot-keys-is-near/",
    "domain": "大厂 AI 动态",
    "title": "Windows and Linux users: The deadline to update Secure Boot keys is near",
    "url": "https://arstechnica.com/security/2026/06/windows-and-linux-users-the-deadline-to-update-secure-boot-keys-is-near/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T11:15:17+00:00",
    "summary": "What you need to know about the expiration of keys securing your machine's boot sequence."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/trump-admin-helps-xai-fight-pollution-lawsuit-says-military-needs-grok-for-war/",
    "domain": "大厂 AI 动态",
    "title": "Trump admin tries to block Clean Air Act lawsuit over xAI's gas turbines",
    "url": "https://arstechnica.com/tech-policy/2026/06/trump-admin-helps-xai-fight-pollution-lawsuit-says-military-needs-grok-for-war/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T22:22:44+00:00",
    "summary": "NAACP lawsuit says xAI uses gas turbines without permits for Grok data center."
  },
  {
    "id": "rss:https://arstechnica.com/information-technology/2026/06/hpe-tempts-vmware-users-partners-with-year-of-free-virtualization-software/",
    "domain": "大厂 AI 动态",
    "title": "Year of free HPE software a “step in the correct direction” in VMware rivalry",
    "url": "https://arstechnica.com/information-technology/2026/06/hpe-tempts-vmware-users-partners-with-year-of-free-virtualization-software/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T22:11:15+00:00",
    "summary": "Partner tells Ars that HPE should be giving out more free VM Essentials licenses."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/cockroaches-scurry-around-with-thousands-of-pieces-of-bacterial-genomes/",
    "domain": "大厂 AI 动态",
    "title": "Cockroaches scurry around with thousands of pieces of bacterial genomes",
    "url": "https://arstechnica.com/science/2026/06/cockroaches-scurry-around-with-thousands-of-pieces-of-bacterial-genomes/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T21:54:41+00:00",
    "summary": "Transferring genes across species doesn't just happen in microbes."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/amid-launch-bottleneck-amazon-has-hundreds-of-satellites-waiting-to-fly/",
    "domain": "大厂 AI 动态",
    "title": "Among the large new rockets Amazon was counting on, only Europe has delivered",
    "url": "https://arstechnica.com/space/2026/06/amid-launch-bottleneck-amazon-has-hundreds-of-satellites-waiting-to-fly/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T21:14:08+00:00",
    "summary": "\"As for Arianespace, they have definitely stepped up.\""
  },
  {
    "id": "wscn:3774963",
    "domain": "股票",
    "title": "风险偏好重燃，英特尔美股盘前涨7%，日韩股市新高，日元创近两年新低，黄金向上触及4300美元",
    "url": "https://wallstreetcn.com/articles/3774963",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T08:12:03+00:00",
    "summary": "标普500指数期货上涨0.7%，纳斯达克期货涨1.1%，英特尔美股盘前涨近7%，特朗普称将帮助英特尔，因为需要设计和制造芯片。布伦特原油跌逾2%至每桶78美元以下。欧洲股指期货小幅下跌0.5%，亚洲股市整体上涨，科技股表现领跑，日经225指数收涨1.6%，韩国首尔综指涨幅达2.3%。"
  },
  {
    "id": "wscn:3774999",
    "domain": "股票",
    "title": "全球央行吹响抗通胀“集结号”：欧日齐步加息，美联储秋季紧缩风险骤升",
    "url": "https://wallstreetcn.com/articles/3774999",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T08:08:42+00:00",
    "summary": "中东战火点燃能源通胀，全球央行集体\"变脸\"。欧洲央行时隔近两年首度加息，日本利率升至30年高位，高盛警告美联储秋季或连续加息2至3次，利率市场剧烈重定价——首次加息预期从2027年骤然提前至今年10月。从法兰克福到雅加达，一场席卷发达与新兴市场的超级紧缩周期，正式拉开帷幕。"
  },
  {
    "id": "wscn:3775009",
    "domain": "股票",
    "title": "车圈尽头是 AI，李想先一步到了路口",
    "url": "https://wallstreetcn.com/articles/3775009",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T08:08:38+00:00",
    "summary": "下一场战争，不在车圈。"
  },
  {
    "id": "wscn:3775008",
    "domain": "股票",
    "title": "以色列袭击黎巴嫩南部两地",
    "url": "https://wallstreetcn.com/articles/3775008",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T08:07:28+00:00",
    "summary": "据黎巴嫩“广场”电视台18日报道，以色列国防军当天上午对黎巴嫩南部两地发动袭击，造成1人死亡、1人受伤。据伊朗塔斯尼姆通讯社18日报道，伊朗外交部发言人巴加埃当天表示，如果以色列继续袭击黎巴嫩，将被视为违反美国的承诺。"
  },
  {
    "id": "wscn:3774998",
    "domain": "股票",
    "title": "硅片：Fab大扩产下迟到的涨价",
    "url": "https://wallstreetcn.com/articles/3774998",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T08:00:11+00:00",
    "summary": "硅片是Fab绕不开的重资产主材，因长协锁价，行业整体仍处盈亏线以下。现稼动率已打满，散单率先涨价，供需缺口已现。硅片行业应该属于周期偏左侧的简单题，胜率高、赔率好，效率一般，越往后供给越紧张，比较适合喜欢周期左侧一点、熬得住的“科技老登们”。"
  },
  {
    "id": "wscn:3775007",
    "domain": "股票",
    "title": "让AI走进千家万户，17项举措推进“人工智能+消费”发展",
    "url": "https://wallstreetcn.com/articles/3775007",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T07:59:20+00:00",
    "summary": "在商品消费领域，《意见》提出扩大智能终端供给，推动消费电子产品从功能型向智能型转变。布局人形机器人消费新赛道，加速机器人从工业场景向消费场景渗透。在服务消费领域，《意见》围绕居家、养老、文旅、住宿餐饮、教育五大场景，也提出了多项务实举措。"
  },
  {
    "id": "wscn:3775002",
    "domain": "股票",
    "title": "长存集团“放权”，光谷国资入主武汉新芯",
    "url": "https://wallstreetcn.com/articles/3775002",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T07:54:57+00:00",
    "summary": "长存集团IPO辅导启动仅一个月，其旗下武汉新芯股份的控股权便易主——武汉光谷半导体产投拟收购长存集团持有的武汉新芯39%股权，交易完成后，这家背靠武汉东湖高新区管委会的国资平台将以47.88%的持股比例单独控制武汉新芯。"
  },
  {
    "id": "wscn:3775005",
    "domain": "股票",
    "title": "五问+一图，读懂《促进平台经济大中小企业协同发展行动方案（2026—2028年）》",
    "url": "https://wallstreetcn.com/articles/3775005",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T07:52:23+00:00",
    "summary": "《行动方案》围绕推动平台经济大中小企业协同发展水平显著提升的目标，提出3方面工作举措。一是强化创新协同引领。促进大中小企业加强创新合作，增强科技、产业和服务创新发展能力。二是健全生态协同体系。加大中小企业品质提升、品牌建设等扶持力度，支持大中小企业协同出海，强化平台经营合规。三是深化开放协同联动。引导平台企业加快技术、数据、算力等要素与中小企业开放共享，建立中小企业公共服务平台。"
  },
  {
    "id": "wscn:3774776",
    "domain": "股票",
    "title": "氮化铝紧缺：1.6T时代的必选品，日本垄断75%份额诱发供应危机？",
    "url": "https://wallstreetcn.com/premium/articles/3774776?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T07:46:37+00:00",
    "summary": "全球高端氮化铝粉体供给高度集中——日本德山以约75%市场份额垄断全球，而国内2025年需求已达5600吨，国产产能不足2000吨，供需缺口高达3600吨，国产替代迫在眉睫。"
  },
  {
    "id": "wscn:3775004",
    "domain": "股票",
    "title": "AI之外，还能买什么？",
    "url": "https://wallstreetcn.com/articles/3775004",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T07:43:52+00:00",
    "summary": "瑞银最新REVS框架显示，以GLP-1受益股为代表的医疗健康板块跃升至全球主题榜首，同时美国工业类主题信号改善，共同成为当前最具性价比的“AI之外”配置优选。"
  },
  {
    "id": "wscn:3775000",
    "domain": "股票",
    "title": "七部门重磅发文：培育一批平台经济领域制造业单项冠军企业",
    "url": "https://wallstreetcn.com/articles/3775000",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T07:35:04+00:00",
    "summary": "《行动方案》提出，到2028年，推动平台经济大中小企业协同发展水平显著提升，形成一批可复制推广的协同创新模式，培育一批平台经济领域制造业单项冠军企业。持续培育壮大科技领军企业，加快培育人工智能一人公司（AI OPC）。提升平台企业词元（Token）普惠服务能力，面向中小企业共性需求优化智能体服务，降低中小企业获取与应用门槛。"
  },
  {
    "id": "wscn:3775003",
    "domain": "股票",
    "title": "美联储变天！沃什首秀引发市场巨震",
    "url": "https://wallstreetcn.com/articles/3775003",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T07:21:47+00:00",
    "summary": "沃什时代的第一次美联储政策会议带来了新的沟通模式，传递了鲜明的政策立场转变，并引发了市场定价的全面修..."
  },
  {
    "id": "wscn:3774995",
    "domain": "股票",
    "title": "特朗普：苹果将与英特尔合作在美国生产芯片",
    "url": "https://wallstreetcn.com/articles/3774995",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T07:21:06+00:00",
    "summary": "特朗普亲自宣布苹果与英特尔达成芯片合作，将在美国本土 共同设计和制造芯片。此举一举多得：苹果借此分散对台积电的高度依赖，英特尔则借顶级客户背书重燃代工业务信心。背后是特朗普政府持股英特尔、豪掷百亿美元、强力推动半导体供应链回流的棋局。"
  },
  {
    "id": "wscn:3775001",
    "domain": "股票",
    "title": "大盘涨了账户却亏了？理财通线上私享会带你读透芯片+商业航天两大核心方向",
    "url": "https://wallstreetcn.com/articles/3775001",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T07:14:44+00:00",
    "summary": "2026年下半年，科技板块还有多少空间？"
  },
  {
    "id": "wscn:3774997",
    "domain": "股票",
    "title": "72家A股公司连夜提示风险！“概念当道则鸡犬升天”之风可以休矣",
    "url": "https://wallstreetcn.com/articles/3774997",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T07:05:40+00:00",
    "summary": "6月17日晚，72家A股公司集中发布风险提示，涉及大量热门概念股。这些公司与相关概念或弱相关、或完全无关，却遭爆炒，估值严重透支。高估值若无业绩支撑，终将靠股价下跌消化。历史案例警示，概念炒作本质是\"击鼓传花\"，投资者应保持警醒，切勿盲目跟风。"
  },
  {
    "id": "wscn:3774987",
    "domain": "股票",
    "title": "郭明錤：玻璃基板是台积电CoPoS的核心，是“必须有”不是“锦上添花”",
    "url": "https://wallstreetcn.com/articles/3774987",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T07:04:35+00:00",
    "summary": "郭明錤深度解读台积电泄露幻灯片：玻璃核心基板是AI芯片制造的\"必须有\"条件而非可选优化，其电源完整性改善可直接转化为更强算力，英伟达等客户高度关注。台积电联手Ibiden与Innolux攻克关键技术瓶颈，量产目标锁定2028年底，有望重塑AI封装格局。"
  },
  {
    "id": "wscn:3774992",
    "domain": "股票",
    "title": "改革美联储，沃什已经等不及了！",
    "url": "https://wallstreetcn.com/articles/3774992",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T07:03:58+00:00",
    "summary": "美联储新主席沃什以史上最短FOMC声明完成首秀，拒填点阵图、设立五大改革工作组，鹰派信号震动市场——美元录年内最大单日涨幅，加息预期骤然升温。然而\"工作组将研究\"几成口头禅，改革雄心与政策真空并存，沃什时代的美联储，不确定性或比以往更频繁降临。"
  },
  {
    "id": "wscn:3774996",
    "domain": "股票",
    "title": "上市三天散户砸入3.7亿美元，SpaceX吸金力碾美股“七巨头”",
    "url": "https://wallstreetcn.com/articles/3774996",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T07:03:48+00:00",
    "summary": "数据显示，SpaceX上市后前三个交易日，散户净买入该股金额高达3.698亿美元，超过苹果、微软、英伟达、谷歌、亚马逊、Meta及特斯拉组成的\"科技七巨头\"同期净买入总额。"
  },
  {
    "id": "wscn:3774769",
    "domain": "股票",
    "title": "下一个六氟化钨？金属铋7月或将迎来大变局",
    "url": "https://wallstreetcn.com/premium/articles/3774769?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T07:00:03+00:00",
    "summary": "日本泰和热磁（全球碲化铋市场60%份额）7N碲化铋库存预计6月底耗尽，已停止接受800G和1.6T光模块用TEC的新订货，全球AI光模块供应链正面临实质性断裂风险。"
  },
  {
    "id": "wscn:3774993",
    "domain": "股票",
    "title": "当微软都烧不起Token了，“模型路由”成为企业AI的“核心需求”",
    "url": "https://wallstreetcn.com/articles/3774993",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T06:57:52+00:00",
    "summary": "Token支出已成企业AI最烫手的难题，连微软都扛不住了。当“用得起”取代“用得强”成为企业的优先级，“模型路由”——根据任务复杂度动态匹配最经济模型的能力——不再是技术选型，而是决定AI项目能否算得过账的核心需求。"
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
    "id": "rss:https://arxiv.org/abs/2606.18288",
    "domain": "金融",
    "title": "A Knowledge Theory of Capital:The Value of Natural and Artificial Intelligence",
    "url": "https://arxiv.org/abs/2606.18288",
    "source": "Jeffrey Gardiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2606.18288v1 Announce Type: new Abstract: This volume develops a knowledge theory of capital for economies in which productive capacity increasingly resides in software, data, models, routines, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.18684",
    "domain": "金融",
    "title": "How firms export: direct and indirect exporting, intermediaries, and hybrid firms",
    "url": "https://arxiv.org/abs/2606.18684",
    "source": "Ra\\'ul M\\'inguez, Asier Minondo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2606.18684v1 Announce Type: new Abstract: Some firms export their own products directly, others rely on intermediary firms to export on their behalf, and still others both export their own produ"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.18719",
    "domain": "金融",
    "title": "Reassessing the role of intermediaries in exports",
    "url": "https://arxiv.org/abs/2606.18719",
    "source": "Aitor Garmendia-Lazcano, Ra\\'ul M\\'inguez, Asier Minondo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2606.18719v1 Announce Type: new Abstract: Previous studies conclude that intermediaries account for a large share of exports. Using Spanish firm-level data, we show that many firms classified as"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.18805",
    "domain": "金融",
    "title": "Emotional driving: Reference-dependent emotions and risky driving behavior after sporting events",
    "url": "https://arxiv.org/abs/2606.18805",
    "source": "Travis Richardson, Steve Bickley, Ho Fai Ben Chan, Benno Torgler, Shamsunnahar Yasmin, Tim Pawlowski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2606.18805v1 Announce Type: new Abstract: Using average vehicle speed data in 10-minute increments at the Traffic Message Channel (TMC) location level, along with precise crash timing and locati"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.18994",
    "domain": "金融",
    "title": "Climate Policy and The Energy Transition",
    "url": "https://arxiv.org/abs/2606.18994",
    "source": "Roy Sarkis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2606.18994v1 Announce Type: new Abstract: This paper studies the macroeconomic dynamics of climate policy in a multi-sector dynamic general equilibrium model with renewable and non-renewable ene"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.19038",
    "domain": "金融",
    "title": "Collective completeness and pricing-hedging duality II",
    "url": "https://arxiv.org/abs/2606.19038",
    "source": "Alessandro Doldi, Marco Frittelli, Marco Maggis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2606.19038v1 Announce Type: new Abstract: This paper complements and extends Doldi, Frittelli and Maggis, Collective completeness and pricing-hedging duality, Math. Finan. Econ. 19, 757-784 (202"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.19052",
    "domain": "金融",
    "title": "An extendable, integrated, and dynamic approach to forecasting and stress-testing credit risk",
    "url": "https://arxiv.org/abs/2606.19052",
    "source": "Marcel Muller, Arno Botha, Conrad Beyers",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2606.19052v1 Announce Type: new Abstract: An integrated and extendable approach for stress-testing loan portfolios is presented, which includes both a loan production component and a credit risk"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.19214",
    "domain": "金融",
    "title": "Testing Centralized and Polycentric Computational Planning",
    "url": "https://arxiv.org/abs/2606.19214",
    "source": "Ricardo Alonzo Fern\\'andez Salguero",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2606.19214v1 Announce Type: new Abstract: This paper presents a reproducible synthetic benchmark comparing a computational planner, an agent-based market, and a hybrid meta-market within a commo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.19318",
    "domain": "金融",
    "title": "Fitting Accumulated Stock Returns with Tempered Skew t-Distribution",
    "url": "https://arxiv.org/abs/2606.19318",
    "source": "Siqi Shao, R. A. Serota",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2606.19318v1 Announce Type: new Abstract: We analyze distributions of historic S&amp;P500 multi-day returns, for the number of days of accumulation from 20 to 120. With the increase of the numbe"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.18545",
    "domain": "金融",
    "title": "The Gini-Bayes Connection: The CAP Slope as Bayes' Theorem, with Applications to Weight of Evidence, Somers' $D$, and Calibration",
    "url": "https://arxiv.org/abs/2606.18545",
    "source": "Denis Burakov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2606.18545v1 Announce Type: cross Abstract: The probabilistic reading of the cumulative accuracy profile (CAP) has a long industry lineage. Falkenstein, Boral and Carty (2000) state, in discrete"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.18935",
    "domain": "金融",
    "title": "Optimal Consumption and Retirement Time under Shortfall Risk Measure",
    "url": "https://arxiv.org/abs/2606.18935",
    "source": "Lijun Bo, Yijie Huang, Tingting Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2606.18935v1 Announce Type: cross Abstract: This paper studies the optimal portfolio, consumption, and endogenous early retirement problem within a benchmark tracking framework by incorporating "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.19263",
    "domain": "金融",
    "title": "Digital Speech Acts Retain Control of Copyright with People, Not Platforms",
    "url": "https://arxiv.org/abs/2606.19263",
    "source": "James Golike, Ehud Shapiro",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2606.19263v1 Announce Type: cross Abstract: Legal precedents protect computer code as copyrightable expression. They have enabled centralized digital platforms -- operating from corporate server"
  },
  {
    "id": "rss:https://arxiv.org/abs/2308.00805",
    "domain": "金融",
    "title": "Second-Order Approximation of Limit Order Books in a Single-Scale Regime",
    "url": "https://arxiv.org/abs/2308.00805",
    "source": "Ulrich Horst, D\\\"orte Kreher, Konstantins Starovoitovs",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2308.00805v3 Announce Type: replace Abstract: We establish a first- and second-order approximation for an infinite dimensional limit order book model in a single (critical) scaling regime where "
  },
  {
    "id": "rss:https://arxiv.org/abs/2505.07231",
    "domain": "金融",
    "title": "Mean Field Portfolio Games with Epstein-Zin Preferences",
    "url": "https://arxiv.org/abs/2505.07231",
    "source": "Guanxing Fu, Ulrich Horst",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2505.07231v2 Announce Type: replace Abstract: We study mean field portfolio games under Epstein-Zin preferences, which naturally encompass the classical time-additive power utility as a special "
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.10492",
    "domain": "金融",
    "title": "Aharanov-Bohm Type Arbitrage and Homological Obstructions in Financial Markets",
    "url": "https://arxiv.org/abs/2604.10492",
    "source": "Takanori Adachi, Keisuke Hara",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2604.10492v4 Announce Type: replace Abstract: We introduce a simplicial and categorical formulation of Aharonov-Bohm (AB) type arbitrage in filtered market systems. Given a filtration modeled as"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.05882",
    "domain": "金融",
    "title": "Market Informedness and Market-Maker Profitability: The Trade-Off Between Adverse Selection and Price Discovery",
    "url": "https://arxiv.org/abs/2606.05882",
    "source": "Konrad Och\\k{e}dzan, Nino Antulov-Fantulin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2606.05882v2 Announce Type: replace Abstract: This paper studies how market informedness affects market makers' profitability in a computational market environment with heterogeneous learning ag"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.17397",
    "domain": "金融",
    "title": "Designing Recommendation Exposure and Favorite Lists: A Field Experiment in a Spot-Work Platform",
    "url": "https://arxiv.org/abs/2606.17397",
    "source": "Kazuki Sekiya, Suguru Otani, Yuki Komatsu, Shunsuke Ozeki, Shunya Noda",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2606.17397v2 Announce Type: replace Abstract: How should recommender systems be designed when recommendations shape access to scarce, short-lived opportunities? We study this question in a produ"
  },
  {
    "id": "rss:https://arxiv.org/abs/2209.01378",
    "domain": "金融",
    "title": "RNN(p) for Power Consumption Forecasting",
    "url": "https://arxiv.org/abs/2209.01378",
    "source": "Roberto Baviera, Pietro Manzoni",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2209.01378v3 Announce Type: replace-cross Abstract: An elementary Recurrent Neural Network that operates on p time lags, called an RNN(p), is the natural generalisation of a linear autoregressiv"
  },
  {
    "id": "rss:https://arxiv.org/abs/2501.17577",
    "domain": "金融",
    "title": "On the Singular Control of a Diffusion and its Running Infimum or Supremum",
    "url": "https://arxiv.org/abs/2501.17577",
    "source": "Giorgio Ferrari, Neofytos Rodosthenous",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2501.17577v2 Announce Type: replace-cross Abstract: We study a class of singular stochastic control problems for a one-dimensional diffusion $X$ in which the performance criterion to be optimise"
  },
  {
    "id": "rss:https://arxiv.org/abs/2506.01101",
    "domain": "金融",
    "title": "Gradient-based Stochastic Optimization of Utility-based Shortfall Risk",
    "url": "https://arxiv.org/abs/2506.01101",
    "source": "Sumedh Gupte, Prashanth L. A., Sanjay P. Bhat",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2506.01101v2 Announce Type: replace-cross Abstract: We consider the problems of estimation and optimization of utility-based shortfall risk (UBSR). We extend UBSR to cover possibly unbounded ran"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.07367",
    "domain": "金融",
    "title": "Criteria for the economic viability of fusion power plants",
    "url": "https://arxiv.org/abs/2604.07367",
    "source": "D. G. Whyte, A. Lo, R. Bielajew, M. Hancock, R. Moeykens, G. Shaw",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2604.07367v2 Announce Type: replace-cross Abstract: Commercial fusion energy requires frameworks to assess both the scientific and economic viability of a wide variety of fusion concepts. Inspir"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.22463",
    "domain": "金融",
    "title": "Quantum analog-encoding for correlated Gaussian vectors and their exponentiation with application to rough volatility",
    "url": "https://arxiv.org/abs/2604.22463",
    "source": "Tassa Thaksakronwong, Koichi Miyamoto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2604.22463v2 Announce Type: replace-cross Abstract: Quantum computing may speed up numerical problems involving large matrices that are demanding for classical computers, and active research on "
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.30442",
    "domain": "金融",
    "title": "When market boundaries weaken: Network reconfiguration and regime-dependent cross-asset spillovers",
    "url": "https://arxiv.org/abs/2605.30442",
    "source": "Ruixue Jing, Luis Enrique Correa Rocha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2605.30442v2 Announce Type: replace-cross Abstract: Cryptocurrencies are increasingly adopted as investment assets, making their interactions with traditional financial markets central to cross-"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.15936",
    "domain": "金融",
    "title": "A game of information",
    "url": "https://arxiv.org/abs/2606.15936",
    "source": "Dorje C. Brody",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-18T04:00:00+00:00",
    "summary": "arXiv:2606.15936v2 Announce Type: replace-cross Abstract: A game of information concerns two players transmitting messages that are obscured by noise. A receiver digests the combination of the two inf"
  }
]
```
