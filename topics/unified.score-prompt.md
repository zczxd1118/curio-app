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

- 今日日期：`2026-06-15`
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
  "date": "2026-06-15",
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
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1160770,
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
    "points": 1147384,
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
    "points": 1124634,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1onb6zwEkk",
    "domain": "AI",
    "title": "【Ai教程】100集（全）从零开始学illustrator软件基础 (Ai2025新手入门实用版)Ai2025零基础入门教程！！！",
    "url": "http://www.bilibili.com/video/av115025985412548",
    "source": "天才AI设计鲨",
    "platform": "bilibili",
    "points": 1033926,
    "published_at": "2025-08-14T11:00:00+00:00",
    "summary": "设计行业5年 是一名资深设计师~PS学习交流 （南极有什么→ 动物 群 ：211582457）\n你的三连是我最大的动力！！你的三连是我最大的动力！！你的三连是我最大的动力！！"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 838131,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 688307,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1ty4y1S7mC",
    "domain": "AI",
    "title": "VS Code 零基础教程 | 持续更新中",
    "url": "http://www.bilibili.com/video/av798033193",
    "source": "兔子不吃米饭",
    "platform": "bilibili",
    "points": 626923,
    "published_at": "2020-12-10T12:00:08+00:00",
    "summary": "不卖课，不广告。\n\nVS Code 基础教程，求点赞，求投币，求分享，求收藏。\n\n谢谢大家。"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 405843,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 371983,
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
    "points": 312420,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 278810,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 235042,
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
    "points": 216128,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1VEA8zYE6f",
    "domain": "AI",
    "title": "翻遍整个B站，这绝对是2026讲的最好的提示词工程（Prompt Engineering）教程，全程干货无废话！让你少走99%的弯路！AI大模型|LLM",
    "url": "http://www.bilibili.com/video/av116147491964472",
    "source": "AIAgent开发",
    "platform": "bilibili",
    "points": 193039,
    "published_at": "2026-02-28T09:22:09+00:00",
    "summary": "翻遍整个B站，这绝对是2026讲的最好的提示词工程（Prompt Engineering）教程，全程干货无废话！让你少走99%的弯路！AI大模型|LLM"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 174438,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 159532,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 155752,
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
    "points": 150411,
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
    "points": 142938,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1djAEzNEYL",
    "domain": "AI",
    "title": "【全187集】全B站最详细AI应用开发教程，2小时快速掌握AI实战开发技巧，手把手教你从0到1做AI项目！小白适用！学完即就业，带你玩转AI开发赛道！",
    "url": "http://www.bilibili.com/video/av116259966489972",
    "source": "AI应用实战",
    "platform": "bilibili",
    "points": 137580,
    "published_at": "2026-03-20T06:09:44+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "domain": "AI",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 134958,
    "published_at": "2026-01-11T15:43:58+00:00",
    "summary": "🚀开发者必看！Superpowers把专业工程团队方法论固化成Skills，让Claude Code告别越写越乱的困境：规格驱动+代码质量双重保障！AI编程新范式！头脑风暴+计划+执行一条龙自动化\n\n\n🚀🚀🚀 视频简介：\n🎬 本期视频详细演示了开源AI编程工作流系统Superpowers的完整使用方法，并通过开发一款iOS时间线笔记原生应用来实测其效果。\n🔧 核心内容：\nSuperpowers工作"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 126347,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1j67k6oENA",
    "domain": "AI",
    "title": "Claude Ultracode 超码 上线 | 操控100个Agent并行开发  保姆级实战教程",
    "url": "http://www.bilibili.com/video/av116697163896598",
    "source": "技术胖",
    "platform": "bilibili",
    "points": 103639,
    "published_at": "2026-06-05T11:05:27+00:00",
    "summary": "Ultracode 功能太好用了，就是Claude Code昨天新出的“超码”功能，如果你Vibe Coding ，那这个技巧一定要掌握。他解决了Claude Code 一次性跑不完大型任务的问题。\n本期视频很长，但看完你的AI Coding能力将超越整个团队。并且把视频内容整理成了文字版，放在评论区，方便你学习使用。视频很干，可以先喝口水润润喉咙。"
  },
  {
    "id": "bvid:BV1P3XTYPEJm",
    "domain": "AI",
    "title": "MCP是怎么对接大模型的？抓取AI提示词，拆解MCP的底层原理",
    "url": "http://www.bilibili.com/video/av114177964246439",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 99621,
    "published_at": "2025-03-17T13:21:11+00:00",
    "summary": "MCP 简单来说是AI大模型的标准化工具箱。 可大模型是怎么知道工具箱里面有哪些工具，使用什么样的参数格式进行调用呢？ MCP与Function Call的关系是什么？ 是不是只有支持Function Call的模型才能使用MCP？ 在上期视频里，爬爬虾介绍了MCP的概念与基础使用，本期视频我们从大模型与提示词的角度再次探讨下MCP协议的底层原理。这次我使用Cloudflare AI Gatewa"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 89970,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 71053,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 69110,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1UWzpBkERN",
    "domain": "AI",
    "title": "Cherry Studio：新版本更新教程！Agent+MCP+全局记忆！手把手教程！",
    "url": "http://www.bilibili.com/video/av115936887578336",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 68278,
    "published_at": "2026-01-22T11:00:00+00:00",
    "summary": "使用下方邀请链接，注册即可获得200万Tokens：\nhttps://console.lanyun.net/#/register?promoterCode=0179\n\nCherry AI官网：https://cherry-ai.com/\nGithub项目页面：https://github.com/CherryHQ/cherry-studio"
  },
  {
    "id": "bvid:BV1XdFzz7Ei8",
    "domain": "AI",
    "title": "不写代码就能轻松开发应用？Cursor+Gemini 超强指挥官工作法！",
    "url": "http://www.bilibili.com/video/av116021511853604",
    "source": "PM刘搞定",
    "platform": "bilibili",
    "points": 56596,
    "published_at": "2026-02-06T03:17:18+00:00",
    "summary": "如何像传统互联网大厂一样指挥AI干活？本期视频通过一个“个人工作台”的实战项目，拆解了一套利用 LLM (Gemini) 辅助 Cursor 开发的高效工作流。\n\n核心内容：\n角色转换：你不是程序员，你是产品经理（PM）。\n文档驱动：如何用 AI 生成标准的产品文档 (PRD)、UI 文档和技术方案。\n避坑指南：如何防止 Cursor “手搓核弹”或开发中途“失忆”。\n\n实操流程：\nStep 1："
  },
  {
    "id": "bvid:BV1HM7C6BEnF",
    "domain": "AI",
    "title": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！",
    "url": "http://www.bilibili.com/video/av116696929076767",
    "source": "AIAgent开发",
    "platform": "bilibili",
    "points": 54438,
    "published_at": "2026-06-05T10:11:18+00:00",
    "summary": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！"
  },
  {
    "id": "bvid:BV1uTAQznEHa",
    "domain": "AI",
    "title": "MiniMax Agent: 真正全能的智能体工具，一键云部署 OpenClaw + 预置专家模式，告别命令行！",
    "url": "http://www.bilibili.com/video/av116142358135406",
    "source": "杰森的效率工坊",
    "platform": "bilibili",
    "points": 53126,
    "published_at": "2026-02-27T11:31:28+00:00",
    "summary": "在这个智能体元年，想让 AI 真正的接管你的工作，但又不想面对黑乎乎的命令行？\nMiniMax Agent就是这个零门槛的桌面智能体工具，帮你做PPT、分析文档、建网站，还能一键部署OpenClaw。搭配强大的 MiniMax M2.5 模型，预置专家系统，直接接管你的日常工作。\n最新重磅更新：MaxClaw，一键云部署OpenClaw，告别命令行与各种Error，给你真正安全隔离的生产环境。"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 51710,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1tXRAYiEYR",
    "domain": "AI",
    "title": "使用Cursor制作高保真原型图",
    "url": "http://www.bilibili.com/video/av114114999356114",
    "source": "AI技术玩家",
    "platform": "bilibili",
    "points": 48463,
    "published_at": "2025-03-06T10:40:35+00:00",
    "summary": "Cursor 除了可以开发代码之外，我们还可以利用 Cursor 来制作高保真的原型图。\n\n在 Agent 模式下 Cursor 就会自动为我们创建一些 HTML + CSS 的代码页面。\n\n然后可以根据我们的需求继续微调，如果你觉得效果不太好，可以参考让 Cursor 参考一些优秀的设计，也可以把你觉得好的设计效果图提供给 Cursor。\n\n设计完成后我们可以使用一个名为 `html.to.de"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 35696,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1CmAGegEpa",
    "domain": "AI",
    "title": "使用Cursor实战Java项目（Cursor写Java代码）",
    "url": "http://www.bilibili.com/video/av114012708733672",
    "source": "小道仙97",
    "platform": "bilibili",
    "points": 31844,
    "published_at": "2025-02-16T09:02:42+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27259,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV17wRQBLEZn",
    "domain": "AI",
    "title": "目前B站最全最新用AI驱动Playwright，不会写代码也能搞定的Web自动化测试，从安装到实战1小时上手",
    "url": "http://www.bilibili.com/video/av116543870535035",
    "source": "web自动化测试",
    "platform": "bilibili",
    "points": 26488,
    "published_at": "2026-05-09T09:24:55+00:00",
    "summary": "视频配套籽料都帮你们整理在这啦：https://www.bilibili.com/opus/972885207239622681\r\n基础学习包，配套课件，PDF电子书籍，问题解答等\r\n记得[热词系列_三连]up持续为你们带来更优质的课程教学！"
  },
  {
    "id": "bvid:BV16BkEBtEjW",
    "domain": "AI",
    "title": "老张公开课：算力、GPU、AI服务器详解（上）",
    "url": "http://www.bilibili.com/video/av115927962159456",
    "source": "It_server技术分享",
    "platform": "bilibili",
    "points": 26180,
    "published_at": "2026-01-20T14:51:01+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1RUDsBWEHb",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的Cursor+Skills实战指南教程，手把手带你开发爆款app，全程干货无废话！比付费效果强十倍！",
    "url": "http://www.bilibili.com/video/av116373464350785",
    "source": "AI大模型技术教程",
    "platform": "bilibili",
    "points": 22231,
    "published_at": "2026-04-09T10:15:00+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\nCursor+Skills频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 21985,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1XrEZ6NEuD",
    "domain": "AI",
    "title": "五分钟带你看懂黑客松冠军的 Claude Code 配置",
    "url": "http://www.bilibili.com/video/av116728436623476",
    "source": "奇思妙想CYC",
    "platform": "bilibili",
    "points": 19553,
    "published_at": "2026-06-11T04:05:00+00:00",
    "summary": "GitHub 上有个 18 万 Star 的仓库，Anthropic 官方黑客松冠军做的。\n他用 Claude Code 做了 10 个月真实产品，把所有配置全部开源：48 个 Agent、182 个 Skill、68 个自定义命令。\n这期带你逛整个仓库，搞清楚大框架，知道从哪里开始学。\n三期系列第 1 篇。"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 17479,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1QzuRz2Epz",
    "domain": "AI",
    "title": "【中文】Cursor AI Unity 教程：新手指南，简单易懂 ｜ Nikhil Malankar",
    "url": "http://www.bilibili.com/video/av114879017000489",
    "source": "CursorInsider",
    "platform": "bilibili",
    "points": 17342,
    "published_at": "2025-07-19T13:00:00+00:00",
    "summary": "在本视频中，我将带你逐步完成 Cursor AI 在 Unity 中的完整设置和配置，帮助你利用 AI 驱动的代码辅助功能，加速你的游戏开发流程。无论你是正在构建一个新项目，还是将 AI 集成到现有的 Unity 游戏中，本教程都涵盖了你所需的一切。\n\n🔧 你将学到：\n✔️ 如何在 Unity 中安装和配置 Cursor AI\n✔️ 设置 Cursor AI 扩展以实现无缝开发\n✔️ 使用 AI "
  },
  {
    "id": "bvid:BV1RH7C6ZEAg",
    "domain": "AI",
    "title": "这绝对是B站唯一将OpenCode 从入门到精通讲明白的教程，手把手带你从入门到实战使用，保姆级教程，存下吧，比啃书好太多了！",
    "url": "http://www.bilibili.com/video/av116696509582055",
    "source": "码士集团_马小帆",
    "platform": "bilibili",
    "points": 16097,
    "published_at": "2026-06-05T08:30:45+00:00",
    "summary": "这绝对是B站唯一将OpenCode 从入门到精通讲明白的教程，手把手带你从入门到实战使用，保姆级教程，存下吧，比啃书好太多了！\n【视频配套籽料+问题解答】请看”平论区置顶”自取哦！！！\n视频制作不易，如果视频对你有用的话❤请一键三莲【长按点赞】支持一下up哦，拜托，这对我真的很重要！"
  },
  {
    "id": "bvid:BV1dCEX64EyY",
    "domain": "AI",
    "title": "【6月最新】吊打付费！2026最强版小龙虾OpenClaw完整安装教学及保姆级教程，一个视频搞懂OpenClaw本地部署/接入微信/飞书/钉钉（附完整操作文档）",
    "url": "http://www.bilibili.com/video/av116723437276125",
    "source": "智能体AI",
    "platform": "bilibili",
    "points": 15800,
    "published_at": "2026-06-10T02:33:14+00:00",
    "summary": "视频中的操作文档，整合包，模型，工作流都整理好啦！评论区抱走哦！！"
  },
  {
    "id": "bvid:BV1JfT4zVEa5",
    "domain": "AI",
    "title": "Cursor1.0新特性BugBot自动化代码Code Review使用教程+实测",
    "url": "http://www.bilibili.com/video/av114630882037891",
    "source": "码里奥Ziho",
    "platform": "bilibili",
    "points": 15351,
    "published_at": "2025-06-05T13:05:30+00:00",
    "summary": "Cursor推出了新的1.0版本，本视频对新特性Bugbot做了一个教程+实测\nBugBot可以在Github进行PR (Pull Request) 的时候，通过AI大模型帮助我们进行CR (Code Review)\n本视频用一个例子演示了如何使用Bugbot功能，并且最后给出了实测的结果\n\n感谢支持！！！欢迎三连\n个人公众号 【码里奥】"
  },
  {
    "id": "bvid:BV1wuLHzDEGA",
    "domain": "AI",
    "title": "【Godot&amp;Cursor】0.亲测一个月后，我选择Godot+Cursor组合做独立游戏",
    "url": "http://www.bilibili.com/video/av114398869853632",
    "source": "破妄-胖",
    "platform": "bilibili",
    "points": 13631,
    "published_at": "2025-04-25T13:43:22+00:00",
    "summary": "飞书文档：https://sh67ozct1z.feishu.cn/docx/Hn5jd0cE6op1Sux9RrFcl8Npnbd"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 13121,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1HFRgBvEVv",
    "domain": "AI",
    "title": "claude接入小米mimo模型基础教程（无claude安装教程）",
    "url": "http://www.bilibili.com/video/av116499343738499",
    "source": "栉旎",
    "platform": "bilibili",
    "points": 12053,
    "published_at": "2026-05-01T12:37:49+00:00",
    "summary": "claude接入小米mimo模型全流程，"
  },
  {
    "id": "bvid:BV1rCJdzFEQg",
    "domain": "AI",
    "title": "让AI帮你干活：WindowsMCP安装和使用！",
    "url": "http://www.bilibili.com/video/av115242814212549",
    "source": "磊哥聊AI",
    "platform": "bilibili",
    "points": 11895,
    "published_at": "2025-09-22T00:00:00+00:00",
    "summary": "AI 自动操作你的电脑，解放双手，提升工作效率。"
  },
  {
    "id": "hn:48377404",
    "domain": "AI 算力 / 半导体",
    "title": "Use your Nvidia GPU's VRAM as swap space on Linux",
    "url": "https://github.com/c0dejedi/nbd-vram",
    "source": "tanelpoder",
    "platform": "hackernews",
    "points": 472,
    "published_at": "2026-06-02T22:55:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48424605",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is proposing a beast of a CPU system for Windows PCs",
    "url": "https://twitter.com/lemire/status/2062880075117113739",
    "source": "tosh",
    "platform": "hackernews",
    "points": 331,
    "published_at": "2026-06-06T12:52:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48355720",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft builds MacBook Pro rival with NVIDIA-powered Surface Laptop Ultra",
    "url": "https://www.windowslatest.com/2026/06/01/microsoft-builds-its-ultimate-macbook-pro-rival-with-the-nvidia-powered-surface-laptop-ultra/",
    "source": "jbk",
    "platform": "hackernews",
    "points": 287,
    "published_at": "2026-06-01T12:04:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:48356654",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Cosmos 3",
    "url": "https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 150,
    "published_at": "2026-06-01T13:32:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48356312",
    "domain": "AI 算力 / 半导体",
    "title": "Launch HN: Expanse (YC P26) – Unlock Wasted GPU Capacity",
    "url": "https://news.ycombinator.com/item?id=48356312",
    "source": "ismaeel_bashir",
    "platform": "hackernews",
    "points": 103,
    "published_at": "2026-06-01T13:05:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48509844",
    "domain": "AI 算力 / 半导体",
    "title": "SkillSpector",
    "url": "https://github.com/NVIDIA/SkillSpector",
    "source": "taubek",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-06-12T21:49:49+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/imec-pushes-quantum-toward-manufacturable-silicon-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Imec Pushes Quantum Toward Manufacturable Silicon Systems",
    "url": "https://www.eetimes.com/imec-pushes-quantum-toward-manufacturable-silicon-systems/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T08:13:05+00:00",
    "summary": "Imec says advanced lithography and semiconductor integration techniques may help scale silicon spin qubits toward manufacturable quantum systems. The post Imec Pushes Quantum Toward Manufacturable Sil"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intels-upcoming-raptor-lake-next-will-reportedly-top-out-at-20-cores-and-retain-core-200-branding-lineup-may-include-a-special-10-core-sku-with-24mb-of-l3-cache",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's upcoming 'Raptor Lake Next' will reportedly top out at 20 cores and retain Core 200 branding — Lineup may include a special 10-core SKU with 24MB of L3 cache",
    "url": "https://www.tomshardware.com/pc-components/cpus/intels-upcoming-raptor-lake-next-will-reportedly-top-out-at-20-cores-and-retain-core-200-branding-lineup-may-include-a-special-10-core-sku-with-24mb-of-l3-cache",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T14:57:07+00:00",
    "summary": "Intel's Raptor Lake family might be coming back for a third time and sit alongside Nova Lake on shelves as the budget-oriented offering from the company."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/servers/amazon-says-its-data-centers-consume-only-0-075-percent-of-the-water-americans-use-for-watering-their-lawns-and-gardens-company-also-boasts-of-its-improvements-in-water-efficiency",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon says its data centers consume only 0.075% of the water Americans use for watering their lawns and gardens — company also boasts of its improvements in water efficiency",
    "url": "https://www.tomshardware.com/desktops/servers/amazon-says-its-data-centers-consume-only-0-075-percent-of-the-water-americans-use-for-watering-their-lawns-and-gardens-company-also-boasts-of-its-improvements-in-water-efficiency",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T14:25:00+00:00",
    "summary": "Amazon says that it uses 2.5 billion gallons of water annually for data center cooling but compares it to the 3.3 trillion gallons of water used for watering lawns and gardens in the U.S. every year."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/computer-history-museum-recalls-astonishing-retro-haul-recovered-from-abandoned-german-warehouse-over-2-000-artifacts-spanning-the-1930s-to-1980s-required-seven-tractor-trailers-after-a-wwii-bomb-scare",
    "domain": "AI 算力 / 半导体",
    "title": "Computer History Museum recalls ‘astonishing’ retro haul recovered from abandoned German warehouse — over 2,000 artifacts spanning the 1930s to 1980s required seven tractor-trailers after a WWII bomb ",
    "url": "https://www.tomshardware.com/tech-industry/computer-history-museum-recalls-astonishing-retro-haul-recovered-from-abandoned-german-warehouse-over-2-000-artifacts-spanning-the-1930s-to-1980s-required-seven-tractor-trailers-after-a-wwii-bomb-scare",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T14:00:00+00:00",
    "summary": "The Computer History Museum recalls one of its biggest ever retro treasure troves. This ‘astonishing’ haul was rescued from an abandoned warehouse in the town of Castrop-Rauxel, Germany."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/apple-made-marketing-gold-from-the-power-mac-g4-supercomputer-export-ban-in-1999-pentagon-banned-sales-of-the-400-mhz-g4-in-50-countries-when-it-launched-and-became-the-first-pc-to-be-classed-as-a-weapon",
    "domain": "AI 算力 / 半导体",
    "title": "Apple made marketing gold from the export ban on Power Mac G4 'supercomputer' in 1999, 'for the first time in history a personal computer has been classified as a weapon' — Pentagon banned sales of th",
    "url": "https://www.tomshardware.com/tech-industry/apple-made-marketing-gold-from-the-power-mac-g4-supercomputer-export-ban-in-1999-pentagon-banned-sales-of-the-400-mhz-g4-in-50-countries-when-it-launched-and-became-the-first-pc-to-be-classed-as-a-weapon",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T14:00:00+00:00",
    "summary": "In the context of the recent tech export bans, we look back at the Apple PowerMac G4 export ban from 1999 and Steve Jobs making marketing gold from the situation."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/servers/researchers-recycle-old-phones-and-cluster-them-into-computing-platforms-says-processors-on-modern-smartphones-deliver-higher-single-core-performance-than-comparable-multicore-servers",
    "domain": "AI 算力 / 半导体",
    "title": "Researchers recycle old phones and cluster them into ‘computing platforms’ that operate as a low-cost data center — says processors on modern smartphones deliver higher single-core performance than co",
    "url": "https://www.tomshardware.com/desktops/servers/researchers-recycle-old-phones-and-cluster-them-into-computing-platforms-says-processors-on-modern-smartphones-deliver-higher-single-core-performance-than-comparable-multicore-servers",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T13:34:49+00:00",
    "summary": "A team of researchers from UC San Diego found that 'old' smartphones from 2023 could be combined to build a server capable of running apps locally, instead of relying on cloud servers located on a dis"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/snapmaker-launches-usd150-000-innovation-fund-for-open-source-3d-printing-cash-rewards-target-developers-backing-the-u1-toolchanger-across-klipper-orcaslicer-and-moonraker-ecosystems",
    "domain": "AI 算力 / 半导体",
    "title": "Snapmaker launches $150,000 Innovation Fund for open source 3D printing — cash rewards target developers backing the U1 toolchanger across Klipper, OrcaSlicer, and Moonraker ecosystems",
    "url": "https://www.tomshardware.com/3d-printing/snapmaker-launches-usd150-000-innovation-fund-for-open-source-3d-printing-cash-rewards-target-developers-backing-the-u1-toolchanger-across-klipper-orcaslicer-and-moonraker-ecosystems",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T13:30:00+00:00",
    "summary": "Snapmaker celebrates 10 years in business by sponsoring open-source developers and you."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-this-msi-codex-z2-16-thread-gaming-ryzen-pc-with-a-2tb-ssd-at-a-usd400-discount-system-packs-a-ryzen-8700f-16gb-ddr5-and-rtx-5060-ti-8gb-for-usd1-499",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this MSI Codex Z2 16-thread gaming Ryzen PC with a 2TB SSD at a $400 discount — system packs a Ryzen 8700F, 16GB DDR5, and RTX 5060 Ti 8GB for $1,499",
    "url": "https://www.tomshardware.com/pc-components/grab-this-msi-codex-z2-16-thread-gaming-ryzen-pc-with-a-2tb-ssd-at-a-usd400-discount-system-packs-a-ryzen-8700f-16gb-ddr5-and-rtx-5060-ti-8gb-for-usd1-499",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T13:28:13+00:00",
    "summary": "MSI's prebuilt gaming desktop pairs a Zen 4 processor with Nvidia's latest RTX 5060 Ti graphics card and comes housed in an airflow-focused chassis with ARGB lighting."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/nist-gets-metal-3d-printers-to-mix-alloys-mid-print-by-rewriting-the-lasers-path",
    "domain": "AI 算力 / 半导体",
    "title": "New 3D printer tech uses elliptical laser beams to stir molten metal and create ‘alloys-on-demand’ — existing machinery can implement technique in software meaning for more convenient, stronger alloy ",
    "url": "https://www.tomshardware.com/3d-printing/nist-gets-metal-3d-printers-to-mix-alloys-mid-print-by-rewriting-the-lasers-path",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T13:02:26+00:00",
    "summary": "NIST has demonstrated a metal 3D printing method that stirs molten metal during the print by sending the laser along looping elliptical paths instead of straight lines."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/microsoft-is-reportedly-testing-copilot-ai-features-with-discrete-gpus-instead-of-npus-a-feature-available-on-windows-app-sdk-with-a-windows-insider-experimental-channel-build-and-developer-mode-turned-on",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft is reportedly testing Copilot+ AI features with discrete GPUs instead of NPUs — a feature available on Windows App SDK with a Windows Insider Experimental Channel build and Developer Mode tu",
    "url": "https://www.tomshardware.com/software/windows/microsoft-is-reportedly-testing-copilot-ai-features-with-discrete-gpus-instead-of-npus-a-feature-available-on-windows-app-sdk-with-a-windows-insider-experimental-channel-build-and-developer-mode-turned-on",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T13:00:00+00:00",
    "summary": "Microsoft is experimenting with Windows AI features on non-Copilot devices, finally allowing AI features to run on discrete GPUs. This move expands its user base and gives more users access to Windows"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-hit-with-sweeping-probe-from-massive-coalition-of-42-us-state-attorneys-general-just-days-after-reported-ipo-filing-subpoena-targets-chatgpt-makers-ads-data-practices-handling-of-minors-model-sycophancy-and-safety-policies",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI hit with sweeping probe from massive coalition of 42 US state attorneys general just days after reported IPO filing — subpoena targets ChatGPT maker’s ads, data practices, handling of minors, m",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-hit-with-sweeping-probe-from-massive-coalition-of-42-us-state-attorneys-general-just-days-after-reported-ipo-filing-subpoena-targets-chatgpt-makers-ads-data-practices-handling-of-minors-model-sycophancy-and-safety-policies",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T12:30:00+00:00",
    "summary": "State attorneys general have opened a broad investigation into OpenAI, subpoenaing documents on ads, user retention, data handling, minors, health data, model behavior, and safety policies."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/amd-taunts-apples-macbook-neo-for-failing-to-run-75-percent-of-top-pc-games-only-5-out-of-the-20-top-pc-games-work-on-the-neo-while-all-run-on-amds-budget-offerings",
    "domain": "AI 算力 / 半导体",
    "title": "AMD taunts Apple's MacBook Neo for failing to run 75% of top PC games — Only 5 out of the 20 top PC games work on the Neo, while all run on AMD's budget offerings",
    "url": "https://www.tomshardware.com/laptops/macbooks/amd-taunts-apples-macbook-neo-for-failing-to-run-75-percent-of-top-pc-games-only-5-out-of-the-20-top-pc-games-work-on-the-neo-while-all-run-on-amds-budget-offerings",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T12:00:00+00:00",
    "summary": "AMD is reminding folks not to buy a MacBook, even if it's as good of a deal as the Neo, if you primarily want to game on it. Instead, AMD's own budget laptops can run all the modern titles you want, w"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/trump-adviser-david-sacks-says-anthropic-refused-to-fix-fable-5-jailbreak-before-us-export-controls",
    "domain": "AI 算力 / 半导体",
    "title": "US government warned Anthropic that Fable 5 had been jailbroken, but firm 'refused' to fix before US implemented export controls — Anthropic defended its decision by saying the jailbreak 'isn’t seriou",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/trump-adviser-david-sacks-says-anthropic-refused-to-fix-fable-5-jailbreak-before-us-export-controls",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T11:46:43+00:00",
    "summary": "David Sacks said the US government warned Anthropic that Claude Fable 5 had been jailbroken and that CEO Dario Amodei refused to fix the flaw."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-cryptomining-networks-320-000-rtx-3090-class-gpus-allegedly-burn-112-megawatts-of-power-on-zero-useful-ai-computation-pearls-gpus-are-doing-random-matrix-math-study-claims",
    "domain": "AI 算力 / 半导体",
    "title": "AI cryptomining network's 320,000 RTX 3090-class GPUs allegedly burn 112 megawatts of power on ‘zero useful AI computation’ — GPU rental costs jump 38%, but Pearl’s cards are doing random matrix math,",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-cryptomining-networks-320-000-rtx-3090-class-gpus-allegedly-burn-112-megawatts-of-power-on-zero-useful-ai-computation-pearls-gpus-are-doing-random-matrix-math-study-claims",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T11:30:00+00:00",
    "summary": "A preprint claims Pearl’s AI mining network consumes 320,000 GPU-equivalents and 112 MW while producing no verified useful AI computation."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/webcams/razer-kiyo-v2-x-review",
    "domain": "AI 算力 / 半导体",
    "title": "Razer Kiyo V2 X Review: Auto-focus for life",
    "url": "https://www.tomshardware.com/peripherals/webcams/razer-kiyo-v2-x-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T11:10:00+00:00",
    "summary": "Razer's Kiyo V2 X is the most budget-friendly of its current webcam lineup; it records video at 1440p / 60 fps and features \"speedy\" auto-focus, a wide 80-degree field of view, and a smoothly integrat"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/hardcore-spongebob-speedrunners-smudged-xbox-optical-disks-to-exploit-lag-clip-trick-filthy-disks-smeared-with-grease-and-sweat-cut-gameplay-times-in-ultimate-pursuit-of-speed",
    "domain": "AI 算力 / 半导体",
    "title": "Hardcore SpongeBob speedrunners smudged Xbox optical disks with sweat and grease to exploit 'lag clip' trick — filthy smeared disks cut gameplay times in ultimate pursuit of speed",
    "url": "https://www.tomshardware.com/video-games/console-gaming/hardcore-spongebob-speedrunners-smudged-xbox-optical-disks-to-exploit-lag-clip-trick-filthy-disks-smeared-with-grease-and-sweat-cut-gameplay-times-in-ultimate-pursuit-of-speed",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T11:00:00+00:00",
    "summary": "A grease smear-induced optical disc reading quirk can save speedrunners lots of time in SpongeBob SquarePants: Battle for Bikini Bottom on Xbox."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd500-on-this-beastly-gaming-rig-with-an-rtx-5060-ti-16gb-ryzen-7800x3d-and-32gb-of-ram-skytechs-desktop-gaming-pc-now-just-usd1-499",
    "domain": "AI 算力 / 半导体",
    "title": "Save $500 on this beastly gaming rig with an RTX 5060 Ti 16GB, Ryzen 7800X3D, and 32GB of RAM — Skytech's desktop gaming PC now just $1,499",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd500-on-this-beastly-gaming-rig-with-an-rtx-5060-ti-16gb-ryzen-7800x3d-and-32gb-of-ram-skytechs-desktop-gaming-pc-now-just-usd1-499",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T14:29:37+00:00",
    "summary": "Looking for a solid gaming PC but tired of seeing exorbitant prices on every retailer's website? We've got you covered with this prebuilt, equipped with high-quality components ready for 1440p gaming "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/more-than-75-data-center-build-outs-worth-usd130-billion-have-been-successfully-blocked-in-the-first-four-months-of-2026-bipartisan-opposition-mounts-nationwide-over-fears-of-soaring-power-and-water-costs",
    "domain": "AI 算力 / 半导体",
    "title": "More than 75 data center build-outs worth $130 billion have been successfully blocked in the first three months of 2026 — bipartisan opposition mounts nationwide over fears of soaring power and water ",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/more-than-75-data-center-build-outs-worth-usd130-billion-have-been-successfully-blocked-in-the-first-four-months-of-2026-bipartisan-opposition-mounts-nationwide-over-fears-of-soaring-power-and-water-costs",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T14:13:22+00:00",
    "summary": "A research firm says the number of blocked data centers in the first quarter of 2026 already matches the number of projects stopped in 2025. The opposition also comes from both sides of the aisle, des"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/amd-challenges-nvidias-dgx-spark-with-usd3-999-ryzen-ai-halo-with-windows-11-support-strix-halo-desktop-undercuts-nvidia-by-usd700-packs-128gb-of-unified-memory",
    "domain": "AI 算力 / 半导体",
    "title": "AMD challenges Nvidia's DGX Spark with $3,999 Ryzen AI Halo with Windows 11 support — Strix Halo desktop undercuts Nvidia by $700, packs 128GB of unified memory",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/amd-challenges-nvidias-dgx-spark-with-usd3-999-ryzen-ai-halo-with-windows-11-support-strix-halo-desktop-undercuts-nvidia-by-usd700-packs-128gb-of-unified-memory",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T14:12:34+00:00",
    "summary": "Powered by the Ryzen AI Max+ 395 processor and 128GB of unified memory, AMD's developer kit arrives as a direct competitor to Nvidia's DGX Spark, which recently saw a price increase to $4,699."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/netgear-countersues-tp-link-alleging-its-american-company-rebrand-is-false-advertising",
    "domain": "AI 算力 / 半导体",
    "title": "Netgear countersues TP-Link, saying firm 'remains, at its core, a Chinese company selling Chinese-made products' — alleges its 'American company' rebrand is false advertising",
    "url": "https://www.tomshardware.com/networking/routers/netgear-countersues-tp-link-alleging-its-american-company-rebrand-is-false-advertising",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T13:47:29+00:00",
    "summary": "Netgear filed counterclaims against TP-Link in federal court in Delaware on June 11, accusing its larger rival of false advertising under the Lanham Act."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-raises-rtx-pro-6000-blackwell-gpu-pricing-to-usd13-250-55-percent-increase-over-msrp-in-a-years-time",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia raises RTX Pro 6000 Blackwell GPU pricing to $13,250 — 55% increase over MSRP in a year's time",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-raises-rtx-pro-6000-blackwell-gpu-pricing-to-usd13-250-55-percent-increase-over-msrp-in-a-years-time",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T12:30:00+00:00",
    "summary": "Nvidia now sells the RTX Pro 6000 Blackwell graphics cards for $13,250, while partner offerings start at $11,359.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-costs-spike-as-subscriptions-hit-pricing-wall-firms-turn-towards-chinese-llms-open-source-models-to-extend-budget",
    "domain": "AI 算力 / 半导体",
    "title": "AI costs spike as subscriptions hit pricing wall — firms turn towards Chinese LLMs, open-source models to extend budget",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-costs-spike-as-subscriptions-hit-pricing-wall-firms-turn-towards-chinese-llms-open-source-models-to-extend-budget",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T12:00:00+00:00",
    "summary": "Companies look for cheaper alternatives as token costs for frontier AI models skyrocket, potentially impacting OpenAI and Anthropic's bottom lines. Subscriptions also take a bite out of these startup'"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-reportedly-preparing-surprise-return-to-ddr4-systems-with-raptor-lake-next-ddr4-platform-slated-for-the-first-half-of-2027-on-the-lga-1700-socket-takes-a-page-from-amds-book-by-extending-budget-platform-longevity",
    "domain": "AI 算力 / 半导体",
    "title": "Intel reportedly preparing surprise return to DDR4 systems with 'Raptor Lake Next' — LGA 1700 platform apparently slated for first half of 2027, takes a page from AMD's book by extending budget platfo",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-reportedly-preparing-surprise-return-to-ddr4-systems-with-raptor-lake-next-ddr4-platform-slated-for-the-first-half-of-2027-on-the-lga-1700-socket-takes-a-page-from-amds-book-by-extending-budget-platform-longevity",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T11:30:00+00:00",
    "summary": "The name came up a few times during our conversations at Computex. Intel has declined to comment on it."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/us-export-control-order-forces-anthropic-to-disable-claude-fable-5-and-mythos-5-worldwide",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. gov't orders Anthropic to disable its newest AI models worldwide due to security threats — ban on Claude Fable 5 and Mythos 5 bars access by any foreign national, even its own employees",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/us-export-control-order-forces-anthropic-to-disable-claude-fable-5-and-mythos-5-worldwide",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T11:24:13+00:00",
    "summary": "Anthropic disabled its two most capable AI models, Claude Fable 5 and Claude Mythos 5, for every customer worldwide on Friday."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/ukraine-used-10-ai-controlled-terminator-drones-to-kill-russian-soldiers-two-years-ago-marking-first-autonomous-killings-of-humans-senior-ukrainian-defense-industry-figure-confirms-this-autonomous-watershed-was-passed-in-2024",
    "domain": "AI 算力 / 半导体",
    "title": "Ukraine used ten AI-controlled ‘Terminator’ drones to kill Russian soldiers two years ago, marking first autonomous killings of humans — autonomous killer quadcopters left ‘everything dead’ says senio",
    "url": "https://www.tomshardware.com/tech-industry/ukraine-used-10-ai-controlled-terminator-drones-to-kill-russian-soldiers-two-years-ago-marking-first-autonomous-killings-of-humans-senior-ukrainian-defense-industry-figure-confirms-this-autonomous-watershed-was-passed-in-2024",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T10:46:57+00:00",
    "summary": "A watershed moment occurred on the battlefields of Ukraine in 2024 when 10 fully autonomous AI-controlled quadcopter drones were sent to the front lines against Russia with ‘Terminator Mode’ engaged."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/video-editing-graphic-design/dev-releases-unblockable-ascii-video-stream-software-mode-5-rendering-puts-out-360p-at-30-fps-using-pure-text",
    "domain": "AI 算力 / 半导体",
    "title": "Dev releases ‘unblockable’ ASCII video stream software, stoking fears of unstoppable ads — delivers 360p video at 30 FPS and acts as a ‘bridge for AI’",
    "url": "https://www.tomshardware.com/software/video-editing-graphic-design/dev-releases-unblockable-ascii-video-stream-software-mode-5-rendering-puts-out-360p-at-30-fps-using-pure-text",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T10:11:13+00:00",
    "summary": "A new and unique video streaming solution is pitched as a 'high-performance, real-time ASCII video rendering engine' that can be used to broadcast 'an unblockable video stream.'"
  },
  {
    "id": "hn:48444451",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia partners with LG robotics to build humanoid robots in South Korea",
    "url": "https://blogs.nvidia.com/blog/nvidia-and-lg-group-ai-factory/",
    "source": "spwa4",
    "platform": "hackernews",
    "points": 59,
    "published_at": "2026-06-08T12:25:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:48234574",
    "domain": "AI 算力 / 半导体",
    "title": "How do you build a semiconductor company on something that's free?",
    "url": "https://www.siliconimist.com/p/the-open-source-silicon-business",
    "source": "johncole",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-05-22T11:49:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:48220446",
    "domain": "AI 算力 / 半导体",
    "title": "IBM invented semiconductor manufacturing automation",
    "url": "https://spectrum.ieee.org/semiconductor-fabrication",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-05-21T10:39:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48431367",
    "domain": "AI 算力 / 半导体",
    "title": "The Russian who invented semiconductors 25 years before the USA",
    "url": "https://www.semidoped.com/p/til-the-man-who-invented-the-future",
    "source": "johncole",
    "platform": "hackernews",
    "points": 53,
    "published_at": "2026-06-07T03:00:52+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/uclas-125m-semiconductor-hub-we-want-high-impact-not-incremental-research/",
    "domain": "AI 算力 / 半导体",
    "title": "UCLA’s $125M Semiconductor Hub: “We Want High Impact, Not Incremental Research”",
    "url": "https://www.eetimes.com/uclas-125m-semiconductor-hub-we-want-high-impact-not-incremental-research/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T19:00:00+00:00",
    "summary": "UCLA launches a $125M semiconductor hub to smash chip bottlenecks with AI research. The post UCLA’s $125M Semiconductor Hub: “We Want High Impact, Not Incremental Research” appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/tecate-group-announces-new-ultracapacitor-cells-rated-foroperation-up-to-105c-221f/",
    "domain": "AI 算力 / 半导体",
    "title": "Tecate Group Announces New Ultracapacitor Cells Rated forOperation up to 105°C (221°F)",
    "url": "https://www.eetimes.com/tecate-group-announces-new-ultracapacitor-cells-rated-foroperation-up-to-105c-221f/",
    "source": "Tecate Group",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T18:49:02+00:00",
    "summary": "San Diego, CA: June 1, 2026. Tecate Group today announced the expansion of its ultracapacitorproduct offerings with new cells rated for operation up to 105°C (221°F). The new TPLT productseries is rat"
  },
  {
    "id": "rss:https://www.eetimes.com/peak-goes-automotive-ethernet-pae-media-converter-connects-100-1000base-t1-with-standard-ethernet/",
    "domain": "AI 算力 / 半导体",
    "title": "PEAK Goes Automotive Ethernet: PAE-Media Converter connects 100/1000BASE-T1 with Standard Ethernet",
    "url": "https://www.eetimes.com/peak-goes-automotive-ethernet-pae-media-converter-connects-100-1000base-t1-with-standard-ethernet/",
    "source": "HMS Networks",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T17:01:05+00:00",
    "summary": "Unique Features for Automotive Testing The PAE-Media Converter addresses crucial market challenges in automotive development and validation with three core innovations. It enables realistic fault simu"
  },
  {
    "id": "rss:https://www.eetimes.com/indian-firm-scales-single-walled-carbon-nanotube-production-for-batteries-and-chips/",
    "domain": "AI 算力 / 半导体",
    "title": "Indian Firm Scales Single-Walled Carbon Nanotube Production for Batteries and Chips",
    "url": "https://www.eetimes.com/indian-firm-scales-single-walled-carbon-nanotube-production-for-batteries-and-chips/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T08:04:16+00:00",
    "summary": "NoPo scales HiPco single-walled carbon nanotube output for sub-2-nm chips and anodes. The post Indian Firm Scales Single-Walled Carbon Nanotube Production for Batteries and Chips appeared first on EE "
  },
  {
    "id": "rss:https://www.eetimes.com/rebellions-bets-on-memory-centric-architecture-as-it-weighs-ipo-options/",
    "domain": "AI 算力 / 半导体",
    "title": "Rebellions Bets on Memory-Centric Architecture as It Weighs IPO Options",
    "url": "https://www.eetimes.com/rebellions-bets-on-memory-centric-architecture-as-it-weighs-ipo-options/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T22:00:00+00:00",
    "summary": "Rebellions leverages memory-centric AI chip designs with SK Hynix and Samsung to fuel IPO ambitions. The post Rebellions Bets on Memory-Centric Architecture as It Weighs IPO Options appeared first on "
  },
  {
    "id": "rss:https://www.eetimes.com/gigadevice-introduces-gd32e512-and-gd32e252-mcus-for-optical-modules/",
    "domain": "AI 算力 / 半导体",
    "title": "GigaDevice Introduces GD32E512 and GD32E252 MCUs for Optical Modules",
    "url": "https://www.eetimes.com/gigadevice-introduces-gd32e512-and-gd32e252-mcus-for-optical-modules/",
    "source": "GigaDevice",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T16:00:00+00:00",
    "summary": "GigaDevice has introduced the new GD32E512 and GD32E252 series MCUs specifically designed for optical module applications. The post GigaDevice Introduces GD32E512 and GD32E252 MCUs for Optical Modules"
  },
  {
    "id": "rss:https://www.eetimes.com/risc-v-targets-data-centers-edge-ai-space/",
    "domain": "AI 算力 / 半导体",
    "title": "RISC-V Targets Data Centers, Edge AI, Space",
    "url": "https://www.eetimes.com/risc-v-targets-data-centers-edge-ai-space/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T13:24:38+00:00",
    "summary": "\"RISC-V is now,\" said Andrea Gallo, CEO of RISC-V International, during his keynote at this week's RISC-V Summit Europe 2026 in Bologna. The post RISC-V Targets Data Centers, Edge AI, Space appeared f"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nvidia-offers-china-early-access-to-vera-cpus-as-h200-sales-stay-frozen",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia preps to sell its Vera CPUs into China as its GPU sales stay frozen — customers encouraged to place orders for CPU shipments as early as August",
    "url": "https://www.tomshardware.com/pc-components/cpus/nvidia-offers-china-early-access-to-vera-cpus-as-h200-sales-stay-frozen",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T16:17:42+00:00",
    "summary": "Nvidia has told Chinese clients that its Arm-based Vera server CPUs could be available as soon as August."
  },
  {
    "id": "rss:https://www.tomshardware.com/tag/prime-day",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon Prime Day",
    "url": "https://www.tomshardware.com/tag/prime-day",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T16:12:44+00:00",
    "summary": "Amazon Prime Day"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/thrustmasters-new-specialized-t-flight-hotas-5-microsoft-flight-simulator-edition-provides-a-plug-and-play-flight-sim-setup-for-just-usd109-featuring-5-axis-control-with-16-bit-precision-and-dual-rudder-system",
    "domain": "AI 算力 / 半导体",
    "title": "Thrustmaster's new specialized T.Flight Hotas 5 Microsoft Flight Simulator Edition provides a plug-and-play flight sim setup for just $109 — featuring 5-axis control with 16-bit precision and dual-rud",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/thrustmasters-new-specialized-t-flight-hotas-5-microsoft-flight-simulator-edition-provides-a-plug-and-play-flight-sim-setup-for-just-usd109-featuring-5-axis-control-with-16-bit-precision-and-dual-rudder-system",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T16:05:13+00:00",
    "summary": "Rocking 16-bit precision, dual-rudder yaw, 5-axis control and a plug-and-play profile for Microsoft Flight Simulator 2024, the new T.Flight Hotas 5 is a solid entry point to flight sims. It works with"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/radeon-rx-9070-xt-finally-appears-in-steam-hardware-survey-rdna-4-flagship-surprisingly-lands-just-behind-rtx-5080",
    "domain": "AI 算力 / 半导体",
    "title": "Radeon RX 9070 XT finally appears in Steam Hardware Survey — RDNA 4 flagship surprisingly lands just behind RTX 5080",
    "url": "https://www.tomshardware.com/pc-components/gpus/radeon-rx-9070-xt-finally-appears-in-steam-hardware-survey-rdna-4-flagship-surprisingly-lands-just-behind-rtx-5080",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T15:09:30+00:00",
    "summary": "AMD’s Radeon RX 9070 XT graphics card has finally penetrated the Steam Survey video card results table, going straight in at position 25."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/nvidias-high-speed-ai-data-center-storage-servers-break-cover-touting-2-9-petabytes-of-storage-and-extreme-pcie-6-0-performance-wiwynn-shows-off-scada-server-with-gpu-accelerated-storage",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's high-speed AI data center storage servers break cover, touting 2.9 petabytes of storage and extreme PCIe 6.0 performance — Wiwynn shows off SCADA server with GPU-accelerated storage",
    "url": "https://www.tomshardware.com/pc-components/ssds/nvidias-high-speed-ai-data-center-storage-servers-break-cover-touting-2-9-petabytes-of-storage-and-extreme-pcie-6-0-performance-wiwynn-shows-off-scada-server-with-gpu-accelerated-storage",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T15:01:59+00:00",
    "summary": "Wiwynn is among the first to demonstrate Nvidia SCADA server that promises to offer AI systems petabytes of ultra-fast storage thanks to GPU-accelerated storage acceleration."
  },
  {
    "id": "hn:48354967",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia announces new AI chip for personal computers",
    "url": "https://www.bbc.com/news/articles/crmp9mppvzro",
    "source": "rishikeshs",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-06-01T10:33:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48439316",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei executive credits bans for accelerating domestic chip independence",
    "url": "https://www.techradar.com/pro/huaweis-chairman-officially-thanks-the-us-government-for-enabling-chinas-semiconductor-industry-chain-to-truly-grow",
    "source": "yogthos",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-06-07T22:38:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48196570",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.5 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/",
    "source": "spectraldrift",
    "platform": "hackernews",
    "points": 962,
    "published_at": "2026-05-19T17:43:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48450142",
    "domain": "大厂 AI 动态",
    "title": "Apple reveals new AI architecture built around Google Gemini models",
    "url": "https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/",
    "source": "unclefuzzy",
    "platform": "hackernews",
    "points": 737,
    "published_at": "2026-06-08T19:14:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:48192224",
    "domain": "大厂 AI 动态",
    "title": "Apple unveils new accessibility features",
    "url": "https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/",
    "source": "interpol_p",
    "platform": "hackernews",
    "points": 726,
    "published_at": "2026-05-19T12:04:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48449084",
    "domain": "大厂 AI 动态",
    "title": "Siri AI",
    "url": "https://www.apple.com/apple-intelligence/",
    "source": "0xedb",
    "platform": "hackernews",
    "points": 681,
    "published_at": "2026-06-08T18:17:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:48233563",
    "domain": "大厂 AI 动态",
    "title": "Steve Wozniak cheered after telling students they have AI – actual intelligence",
    "url": "https://www.businessinsider.com/steve-wozniak-apple-ai-graduation-speech-2026-5",
    "source": "signa11",
    "platform": "hackernews",
    "points": 650,
    "published_at": "2026-05-22T09:04:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48196867",
    "domain": "大厂 AI 动态",
    "title": "Gemini CLI will stop working from June 18, 2026",
    "url": "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/",
    "source": "primaprashant",
    "platform": "hackernews",
    "points": 406,
    "published_at": "2026-05-19T18:03:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48196609",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni",
    "url": "https://deepmind.google/models/gemini-omni/",
    "source": "meetpateltech",
    "platform": "hackernews",
    "points": 323,
    "published_at": "2026-05-19T17:46:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48272354",
    "domain": "大厂 AI 动态",
    "title": "Microsoft Copilot Cowork Exfiltrates Files",
    "url": "https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files",
    "source": "Kneenex",
    "platform": "hackernews",
    "points": 264,
    "published_at": "2026-05-25T21:45:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:48297467",
    "domain": "大厂 AI 动态",
    "title": "Gemini, Gophers, and Fingers. Oh My Alternative Internets Beyond HTTPS",
    "url": "https://brennan.day/gemini-gophers-and-fingers-oh-my-alternative-internets-beyond-https/",
    "source": "ChrisArchitect",
    "platform": "hackernews",
    "points": 147,
    "published_at": "2026-05-27T17:24:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48373764",
    "domain": "大厂 AI 动态",
    "title": "GitHub Copilot App",
    "url": "https://github.com/features/preview/github-app",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 124,
    "published_at": "2026-06-02T17:58:55+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/policy/949679/uk-under-16-social-media-ban-announcement",
    "domain": "大厂 AI 动态",
    "title": "Under-16 social media ban announced by UK government",
    "url": "https://www.theverge.com/policy/949679/uk-under-16-social-media-ban-announcement",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T08:19:09+00:00",
    "summary": "The UK is the latest country to follow Australia in implementing a total social media ban for children under 16, Prime Minister Keir Starmer has announced. The ban, which could take effect from early "
  },
  {
    "id": "rss:https://www.theverge.com/tech/949648/fbi-fake-town-cyberattacks-kinetic-cyber-range",
    "domain": "大厂 AI 动态",
    "title": "The FBI built a small town to simulate cyberattacks",
    "url": "https://www.theverge.com/tech/949648/fbi-fake-town-cyberattacks-kinetic-cyber-range",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T20:35:41+00:00",
    "summary": "Last year, the FBI opened a Cyber Range in Huntsville, Alabama, for simulating cyberattacks. Think of it sort of like the famous Hogan's Alley, but for modern digital crime training. It's a massive 22"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/949644/china-white-house-anthropic-mythos",
    "domain": "大厂 AI 动态",
    "title": "China may have accessed Mythos",
    "url": "https://www.theverge.com/ai-artificial-intelligence/949644/china-white-house-anthropic-mythos",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T18:27:55+00:00",
    "summary": "According to a new report from Semafor, the White House's decision to impose export restrictions on Anthropic's Mythos was driven in part by fears that it had been accessed by a group linked to China."
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/949621/conclave-nyc-summer-block-party-album-review",
    "domain": "大厂 AI 动态",
    "title": "Conclave is the sound of a NYC summer block party",
    "url": "https://www.theverge.com/entertainment/949621/conclave-nyc-summer-block-party-album-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T16:30:00+00:00",
    "summary": "I have this vivid memory of walking to pick up my oldest from school in June of 2022. For a variety of reasons, I was in a very bad place mentally. And to make matters worse, it was brutally hot. I wa"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/948871/world-cup-streaming-free-trial-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "How to watch most of the World Cup matches with free trials",
    "url": "https://www.theverge.com/gadgets/948871/world-cup-streaming-free-trial-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T16:00:00+00:00",
    "summary": "Hoping to catch some World Cup matches while spending as little money as possible? You have a few options for finding a few days of free streaming, although you may choose to eventually pony up some m"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/949620/harmony-universal-remote-version-history",
    "domain": "大厂 AI 动态",
    "title": "The impossible dream of the universal remote",
    "url": "https://www.theverge.com/podcast/949620/harmony-universal-remote-version-history",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T13:42:07+00:00",
    "summary": "You don't really ever have to explain why a universal remote is a good idea. You have a bunch of stuff that needs controlling; this thing controls them all. Many companies have set out to build a prod"
  },
  {
    "id": "rss:https://www.theverge.com/column/948594/solid-state-batteries-semi-solid-state",
    "domain": "大厂 AI 动态",
    "title": "Solid-state batteries still aren’t ready, but gels are",
    "url": "https://www.theverge.com/column/948594/solid-state-batteries-semi-solid-state",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T12:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more on e-bikes, power stations, and how to work anywhere, follow Thomas Ricker. The Stepback arriv"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/949601/amazon-anthropic-fablemythos-government-ban",
    "domain": "大厂 AI 动态",
    "title": "Amazon security research reportedly led to the White House’s Anthropic Fable ban",
    "url": "https://www.theverge.com/ai-artificial-intelligence/949601/amazon-anthropic-fablemythos-government-ban",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T21:39:26+00:00",
    "summary": "According to the Wall Street Journal, the export control directive that led to Anthropic cutting off access to Fable 5 and Mythos 5 was triggered in part by cybersecurity research from Amazon and conv"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/947064/xmen-97-season-2-disney-plus-marvel-masters-of-the-universe-mattel",
    "domain": "大厂 AI 动态",
    "title": "X-Men ’97 has what Master of the Universe is missing",
    "url": "https://www.theverge.com/entertainment/947064/xmen-97-season-2-disney-plus-marvel-masters-of-the-universe-mattel",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T20:00:00+00:00",
    "summary": "In 2026, Marvel and Mattel are both releasing projects designed to capitalize on people's love for iconic animated heroes from their childhoods. Masters of the Universe has put a live-action He-Man on"
  },
  {
    "id": "rss:https://www.theverge.com/games/949593/super-mario-bros-3-million-auction",
    "domain": "大厂 AI 动态",
    "title": "Sealed Super Mario Bros. sells for a record $3 million",
    "url": "https://www.theverge.com/games/949593/super-mario-bros-3-million-auction",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T18:37:21+00:00",
    "summary": "A copy of Super Mario Bros., still in the box and sealed with its original sticker, just sold at Heritage Auctions for $3 million. That absolutely crushes the previous record of $2 million, also for a"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/15/the-ai-layoff-wave-is-becoming-a-powder-keg/",
    "domain": "大厂 AI 动态",
    "title": "The AI layoff wave is becoming a powder keg",
    "url": "https://techcrunch.com/2026/06/15/the-ai-layoff-wave-is-becoming-a-powder-keg/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T07:25:41+00:00",
    "summary": "What makes this combustible: at the very moment that tens of thousands of workers are being shown the door, a small cohort of AI insiders is becoming wealthy on a scale that's hard to comprehend."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/14/orbio-raises-21-million-to-automate-hiring-and-onboarding-for-frontline-workers/",
    "domain": "大厂 AI 动态",
    "title": "Orbio raises $21 million to automate hiring and onboarding for frontline workers",
    "url": "https://techcrunch.com/2026/06/14/orbio-raises-21-million-to-automate-hiring-and-onboarding-for-frontline-workers/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:01:00+00:00",
    "summary": "Orbio announces $21 Million Series A in round led by Dawn Capital."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/14/startup-ceo-charlie-javice-is-reportedly-angling-for-a-trump-pardon/",
    "domain": "大厂 AI 动态",
    "title": "Startup CEO Charlie Javice is reportedly angling for a Trump pardon",
    "url": "https://techcrunch.com/2026/06/14/startup-ceo-charlie-javice-is-reportedly-angling-for-a-trump-pardon/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T21:55:34+00:00",
    "summary": "JPMorgan can't be pleased by any of this."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/14/uk-may-ban-social-media-for-children-under-16/",
    "domain": "大厂 AI 动态",
    "title": "UK may ban social media for children under 16",
    "url": "https://techcrunch.com/2026/06/14/uk-may-ban-social-media-for-children-under-16/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T20:17:00+00:00",
    "summary": "The U.K. seems to be following Australia's lead in banning a wide swath of social media for teens."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/14/as-ai-companies-race-to-go-public-who-else-is-along-for-the-ride/",
    "domain": "大厂 AI 动态",
    "title": "As AI companies race to go public, who else is along for the ride?",
    "url": "https://techcrunch.com/2026/06/14/as-ai-companies-race-to-go-public-who-else-is-along-for-the-ride/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T16:38:09+00:00",
    "summary": "Startups are trying to \"ride that SpaceX IPO wave.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/14/techcrunch-mobility-spacex-rockets-past-tesla/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: SpaceX rockets past Tesla",
    "url": "https://techcrunch.com/2026/06/14/techcrunch-mobility-spacex-rockets-past-tesla/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T16:05:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, how AI is playing a part."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/14/the-new-sonos-play-has-become-my-go-to-desk-and-kitchen-speaker/",
    "domain": "大厂 AI 动态",
    "title": "The new Sonos Play has become my go-to desk and kitchen speaker",
    "url": "https://techcrunch.com/2026/06/14/the-new-sonos-play-has-become-my-go-to-desk-and-kitchen-speaker/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T14:00:00+00:00",
    "summary": "The new Sonos Play can act as a portable speaker inside and outside your home."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/13/as-anthropic-suspends-access-to-new-models-india-debates-its-ai-future/",
    "domain": "大厂 AI 动态",
    "title": "As Anthropic suspends access to new models, India debates its AI future",
    "url": "https://techcrunch.com/2026/06/13/as-anthropic-suspends-access-to-new-models-india-debates-its-ai-future/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T03:00:00+00:00",
    "summary": "Tech leaders debate whether the Anthropic episode is a wake-up call for India’s AI ambitions."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/13/meta-reportedly-moves-to-unwind-2b-manus-deal-after-beijings-demand/",
    "domain": "大厂 AI 动态",
    "title": "Meta reportedly moves to unwind $2B Manus deal after Beijing’s demand",
    "url": "https://techcrunch.com/2026/06/13/meta-reportedly-moves-to-unwind-2b-manus-deal-after-beijings-demand/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T00:03:49+00:00",
    "summary": "Meta starts dismantling its $2 billion Manus acquisition after Beijing ordered the deal reversed."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/13/kpmg-pulls-report-on-ai-usage-due-to-apparent-hallucinations/",
    "domain": "大厂 AI 动态",
    "title": "KPMG pulls report on AI usage due to apparent hallucinations",
    "url": "https://techcrunch.com/2026/06/13/kpmg-pulls-report-on-ai-usage-due-to-apparent-hallucinations/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T20:42:31+00:00",
    "summary": "Once again, AI proves to be an unreliable source of information about AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/13/amazon-ceo-reportedly-raised-anthropic-model-concerns-before-government-crackdown/",
    "domain": "大厂 AI 动态",
    "title": "Amazon CEO reportedly raised Anthropic model concerns before government crackdown",
    "url": "https://techcrunch.com/2026/06/13/amazon-ceo-reportedly-raised-anthropic-model-concerns-before-government-crackdown/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T19:11:41+00:00",
    "summary": "Amazon CEO Andy Jassy may have been the source of security concerns that led Anthropic to cut off worldwide access to two models on Friday."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/13/openai-faces-investigation-from-state-attorneys-general/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI faces investigation from state attorneys general",
    "url": "https://techcrunch.com/2026/06/13/openai-faces-investigation-from-state-attorneys-general/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T16:47:18+00:00",
    "summary": "It's not clear which states are involved, but they're asking about everything from OpenAI's ad policies to its handling of health data."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/13/this-thin-under-pillow-speaker-helped-me-fall-asleep-without-earbuds/",
    "domain": "大厂 AI 动态",
    "title": "This thin under-pillow speaker helped me fall asleep without earbuds",
    "url": "https://techcrunch.com/2026/06/13/this-thin-under-pillow-speaker-helped-me-fall-asleep-without-earbuds/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T16:00:00+00:00",
    "summary": "I’ve struggled with insomnia since I was very young. Like many chronic overthinkers, I tend to fall asleep best when my mind is occupied by something else, such as podcasts, YouTube compilations, or m"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/13/the-fbi-built-its-own-replica-small-town-to-simulate-real-world-cyberattacks/",
    "domain": "大厂 AI 动态",
    "title": "The FBI built its own replica small town to simulate real-world cyberattacks",
    "url": "https://techcrunch.com/2026/06/13/the-fbi-built-its-own-replica-small-town-to-simulate-real-world-cyberattacks/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T11:00:00+00:00",
    "summary": "Hidden inside a building in Alabama, the FBI has created its own small town as a dedicated cyber training ground for simulating cyberattacks."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/did-a-medieval-flying-monk-spot-halleys-comet-twice-its-complicated/",
    "domain": "大厂 AI 动态",
    "title": "Did a medieval flying monk spot Halley's comet, twice? It's complicated",
    "url": "https://arstechnica.com/science/2026/06/did-a-medieval-flying-monk-spot-halleys-comet-twice-its-complicated/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T16:02:53+00:00",
    "summary": "University of Leicester historian thinks Eilmer of Malmesbury saw two different comets: in 1018 and 1066"
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/06/review-disclosure-day-is-big-on-action-light-on-ideas/",
    "domain": "大厂 AI 动态",
    "title": "Review: Disclosure Day is big on action, light on ideas",
    "url": "https://arstechnica.com/culture/2026/06/review-disclosure-day-is-big-on-action-light-on-ideas/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T17:17:44+00:00",
    "summary": "There's nothing new or surprising, but it's still an entertaining film from one of our greatest directors."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/threads-of-underground-fungal-networks-are-long-enough-to-reach-beyond-the-solar-system/",
    "domain": "大厂 AI 动态",
    "title": "Threads of underground fungal networks are long enough to reach beyond the Solar System",
    "url": "https://arstechnica.com/science/2026/06/threads-of-underground-fungal-networks-are-long-enough-to-reach-beyond-the-solar-system/",
    "source": "Wyatt Myskow, Inside Climate News",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T11:18:42+00:00",
    "summary": "Researchers have quantified the length and mass of arbuscular mycorrhizal fungal networks globally."
  },
  {
    "id": "rss:https://www.producthunt.com/products/idledev",
    "domain": "大厂 AI 动态",
    "title": "IdleDev",
    "url": "https://www.producthunt.com/products/idledev",
    "source": "Ishaan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T00:30:41+00:00",
    "summary": "Get paid while your AI agent thinks Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/mimo-3",
    "domain": "大厂 AI 动态",
    "title": "MiMo Code",
    "url": "https://www.producthunt.com/products/mimo-3",
    "source": "Zac Zuo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:00:10+00:00",
    "summary": "A coding agent with explicit long-term memory architecture Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/fonda",
    "domain": "大厂 AI 动态",
    "title": "Fonda",
    "url": "https://www.producthunt.com/products/fonda",
    "source": "Harshit",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T13:55:52+00:00",
    "summary": "Your AI co-founder that remembers decisions + plans for you Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/reignat",
    "domain": "大厂 AI 动态",
    "title": "Reignat",
    "url": "https://www.producthunt.com/products/reignat",
    "source": "Khalid Nouri",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T23:37:43+00:00",
    "summary": "Privacy-friendly web analytics platform built for makers Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/notchcode",
    "domain": "大厂 AI 动态",
    "title": "Notchcode",
    "url": "https://www.producthunt.com/products/notchcode",
    "source": "Bill Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T21:09:41+00:00",
    "summary": "Claude Code + Codex agents in your notch Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/dropmatico",
    "domain": "大厂 AI 动态",
    "title": "Dropmatico",
    "url": "https://www.producthunt.com/products/dropmatico",
    "source": "Naveen Balasubramaniam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T11:30:31+00:00",
    "summary": "Drop. Pick. Done. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/momentra-aesthetic-camera",
    "domain": "大厂 AI 动态",
    "title": "Momentra",
    "url": "https://www.producthunt.com/products/momentra-aesthetic-camera",
    "source": "Jafar Mansuri",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T05:17:09+00:00",
    "summary": "A cozy camera app for beautifully framed memories Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/agentbrush",
    "domain": "大厂 AI 动态",
    "title": "AgentBrush",
    "url": "https://www.producthunt.com/products/agentbrush",
    "source": "Yanis KETO",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T05:21:36+00:00",
    "summary": "Your coding agent's missing tool: image generation Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/emailflow-ai-b2b-lead-generation",
    "domain": "大厂 AI 动态",
    "title": "EmailFlow.AI",
    "url": "https://www.producthunt.com/products/emailflow-ai-b2b-lead-generation",
    "source": "Tareck",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T08:41:55+00:00",
    "summary": "Like Claude Design for Email Newsletters Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/pass-quick-access",
    "domain": "大厂 AI 动态",
    "title": "Pass Quick Access",
    "url": "https://www.producthunt.com/products/pass-quick-access",
    "source": "Ramin Banihashemi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T01:38:58+00:00",
    "summary": "Native quick access and SSH agent for Proton Pass for macOS Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/stackd-cc",
    "domain": "大厂 AI 动态",
    "title": "stackd.cc",
    "url": "https://www.producthunt.com/products/stackd-cc",
    "source": "Arun K",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T16:41:59+00:00",
    "summary": "The answer to \"what's your AI stack?\" Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/kickbacks-ai",
    "domain": "大厂 AI 动态",
    "title": "Kickbacks.ai",
    "url": "https://www.producthunt.com/products/kickbacks-ai",
    "source": "Gabe Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T06:04:58+00:00",
    "summary": "Get paid to wait for Claude Code to finish Discussion | Link"
  },
  {
    "id": "rss:https://36kr.com/p/3853016586359817?f=rss",
    "domain": "大厂 AI 动态",
    "title": "硬氪专访 | 智源研究院院长王仲远：VLA不会死，但世界模型是未来",
    "url": "https://36kr.com/p/3853016586359817?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T01:50:00+00:00",
    "summary": "作者&nbsp;|&nbsp;邱晓芬 编辑&nbsp;|&nbsp;袁斯来 过去几个月，“世界模型”（World Model）从学术黑话迅速膨胀成AI和机器人行业里的关键词。 行业的目光转向背后是切实的焦虑。 一方面，经过了过去两年的野蛮生长，具身智能暴露了当前AI在物理世界中的短板——机器人能识别物体，却不懂“推杯子会掉”；能听懂指令，却无法预判“拧瓶盖需要多大的力”。世界模型正是试图补上这个短"
  },
  {
    "id": "hn:48405718",
    "domain": "股票",
    "title": "SpaceX, Other Mega IPOs Denied Fast Index Entry by S&P",
    "url": "https://www.bloomberg.com/news/articles/2026-06-04/s-p-dow-jones-keeps-megacap-ipo-rules-as-is-after-consultation",
    "source": "tristanj",
    "platform": "hackernews",
    "points": 1062,
    "published_at": "2026-06-04T22:48:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:48455233",
    "domain": "股票",
    "title": "We Think the SpaceX IPO Is Overvalued",
    "url": "https://www.morningstar.com/stocks/why-we-think-spacex-ipo-is-overvalued?content_id=20768396545",
    "source": "0xedb",
    "platform": "hackernews",
    "points": 268,
    "published_at": "2026-06-09T01:56:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48314363",
    "domain": "股票",
    "title": "Sam Altman and Dario Amodei are both walking back AI jobs apocalypse predictions",
    "url": "https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/",
    "source": "ianrahman",
    "platform": "hackernews",
    "points": 236,
    "published_at": "2026-05-28T19:43:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:48373909",
    "domain": "股票",
    "title": "Morningstar values SpaceX at $780B, half its IPO target",
    "url": "https://www.reuters.com/business/media-telecom/morningstar-values-spacex-780-billion-half-its-ipo-target-2026-06-02/",
    "source": "berkeleyjunk",
    "platform": "hackernews",
    "points": 212,
    "published_at": "2026-06-02T18:09:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:48210226",
    "domain": "股票",
    "title": "OpenAI Is Preparing to File for an IPO Soon",
    "url": "https://www.wsj.com/tech/ai/openai-is-preparing-to-file-for-an-ipo-very-soon-0ec95af5",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 206,
    "published_at": "2026-05-20T16:24:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48446310",
    "domain": "股票",
    "title": "Italy's Bending Spoons, owner of AOL and Vimeo, files for Nasdaq IPO",
    "url": "https://www.reuters.com/legal/transactional/italys-bending-spoons-files-us-ipo-2026-06-08/",
    "source": "mmarian",
    "platform": "hackernews",
    "points": 123,
    "published_at": "2026-06-08T15:04:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:48394034",
    "domain": "股票",
    "title": "The SpaceX IPO will be the theft of the century",
    "url": "https://montanaskeptic.substack.com/p/the-spacex-ipo-will-be-the-theft",
    "source": "400thecat",
    "platform": "hackernews",
    "points": 142,
    "published_at": "2026-06-04T04:52:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48504013",
    "domain": "股票",
    "title": "SpaceX's president is floating a Tesla merger as the company begins trading",
    "url": "https://qz.com/spacex-tesla-merger-gwynne-shotwell-ipo-061226",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-06-12T13:47:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48217052",
    "domain": "股票",
    "title": "OpenAI to confidentially file for IPO as soon as Friday",
    "url": "https://www.cnbc.com/2026/05/20/openai-ipo-filing.html",
    "source": "doppp",
    "platform": "hackernews",
    "points": 137,
    "published_at": "2026-05-21T02:24:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48505968",
    "domain": "股票",
    "title": "Elon Musk Becomes First Trillionaire as SpaceX Starts Trading",
    "url": "https://www.nytimes.com/live/2026/06/12/business/spacex-ipo-elon-musk/heres-the-latest",
    "source": "droidjj",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-06-12T16:13:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48385866",
    "domain": "股票",
    "title": "SpaceX's IPO is a disaster waiting to happen for your pension fund",
    "url": "https://www.irishtimes.com/business/2026/06/03/heavily-in-debt-loss-making-with-eyes-on-sending-people-to-mars-why-would-anyone-invest-in-spacex/",
    "source": "anonymousDan",
    "platform": "hackernews",
    "points": 92,
    "published_at": "2026-06-03T16:02:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48499349",
    "domain": "股票",
    "title": "StonkRider – Ride any stock chart",
    "url": "https://stonkrider.com/",
    "source": "nreece",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-06-12T02:58:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48506701",
    "domain": "股票",
    "title": "SpaceX increases almost 30% after biggest IPO",
    "url": "https://www.cnbc.com/2026/06/12/spacex-ipo-spcx-live-updates.html",
    "source": "somenameforme",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-06-12T17:10:07+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3774682",
    "domain": "股票",
    "title": "报道：伊朗将允许霍尔木兹海峡船只自由过境60天",
    "url": "https://wallstreetcn.com/articles/3774682",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T09:27:56+00:00",
    "summary": "更多消息，持续更新中"
  },
  {
    "id": "wscn:3774674",
    "domain": "股票",
    "title": "本周FOMC悬念拉满！沃什上任的第一把火：停止解释一切？",
    "url": "https://wallstreetcn.com/articles/3774674",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T09:18:05+00:00",
    "summary": "执掌美联储不足一月，凯文·沃什便将迎来首场货币政策会议。他高调承诺对美联储沟通机制实施\"政权更迭\"，誓言废除点阵图、终结过度前瞻指引——但现实远比口号残酷：通胀顽固高企，加息讨论已悄然升温，降息承诺正与经济数据正面交锋。改革者还是外交家？周三，答案初现。"
  },
  {
    "id": "wscn:3774681",
    "domain": "股票",
    "title": "周二，日本央行加息“板上钉钉”，1%利率时代有望回归！",
    "url": "https://wallstreetcn.com/articles/3774681",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T09:12:31+00:00",
    "summary": "市场普遍预期日本央行将加息25个基点。巴克莱和野村指出，决定日元走向的关键在于央行能否释放更激进的紧缩信号。核心观测指标有三：实际利率措辞是否调整、有无支持加息50个基点的投票、以及因行长植田和男生病住院而由副行长内田“救场”主持的发布会基调。当前美日利差悬殊，仅一次预期内的加息难以扭转资金流向，日元恐难真正走强。"
  },
  {
    "id": "wscn:3774680",
    "domain": "股票",
    "title": "协议还没签，市场已经替和平干了一杯",
    "url": "https://wallstreetcn.com/articles/3774680",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T08:38:13+00:00",
    "summary": "特朗普宣布美伊协议\"已完成\"，亚洲盘油价跳水4%、日股涨超4%、韩国触发熔断，市场抢先替\"和平\"干了一杯——但这纸协议一个字都还没签。以色列空袭贝鲁特、伊朗拒绝按特朗普时间表落笔，签署前任何一环卡壳，这场拥挤的多头交易，反向杀伤力将远超想象。"
  },
  {
    "id": "wscn:3774679",
    "domain": "股票",
    "title": "AI引爆MLCC，村田积极扩产、三星电机拿下1.5万亿韩元大单",
    "url": "https://wallstreetcn.com/articles/3774679",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T08:35:39+00:00",
    "summary": "AI爆发引发MLCC史上最强周期，高盛预计景气或延至2030年。龙头村田制造产能利用率逼近95%并追加800亿日元扩产；三星电机则斩获1.5万亿韩元史诗级长单，正通过在菲律宾建厂及量产“硅电容”一体化方案锁定AI差异化赛道。"
  },
  {
    "id": "wscn:3774669",
    "domain": "股票",
    "title": "美伊协议“达成”，对冲基金们重启“战前交易手册”",
    "url": "https://wallstreetcn.com/articles/3774669",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T08:33:22+00:00",
    "summary": "美伊和平协议本周五即将落地，原油下跌、美元走软、美债收益率全线回落，市场正加速切换至\"战前模式\"。短期美债、日元、东南亚遭抛售股票相继进入基金经理买入视野，亚洲新兴市场或迎补涨机会，比特币亦触底反弹，一场跨资产的重新定价正在悄然展开。"
  },
  {
    "id": "wscn:3774633",
    "domain": "股票",
    "title": "美伊达成协议，美股盘前半导体股普涨，SpaceX涨超6%，美债收益率全线下行，油价重挫4%",
    "url": "https://wallstreetcn.com/articles/3774633",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T08:21:27+00:00",
    "summary": "美股盘前，美光科技涨超5%，超微电脑涨超5%，AMD涨近5%，英特尔涨近4%，阿斯麦涨近3%。SpaceX涨超6%。布伦特原油跌幅超过4%，逼近每桶83美元，创三个月新低。10年期美国国债收益率下行5个基点至4.43%，掉期交易员对美联储12月前加息25个基点的概率预期从上周五约80%降至约60%。"
  },
  {
    "id": "wscn:3774643",
    "domain": "股票",
    "title": "大爆发！创业板狂飙超5%，算力硬件掀起涨停潮，恒科指涨超1%，智谱狂飙超30%",
    "url": "https://wallstreetcn.com/articles/3774643",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T08:20:39+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市超3800股飘红，今日成交3.05万亿。沪深两市成交额3.03万亿，较上一个交易日缩量超1800亿。板块方面，AI硬件侧主宰市场，覆铜板、光模块、HBM带头猛冲，铜冠铜箔、国际复材、长芯博创、光库科技、太辰光等拿下20CM涨停。"
  },
  {
    "id": "wscn:3774514",
    "domain": "股票",
    "title": "SK海力士默许设备涨价：一场由产能瓶颈驱动的供应链利润再平衡",
    "url": "https://wallstreetcn.com/premium/articles/3774514?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T08:13:35+00:00",
    "summary": "SK海力士允许设备供应商涨价，单看事件本身，不过是3%-4%的价格调整。但从产业周期视角看，它是半导体产业链利润从中心向外围扩散的确认函。"
  },
  {
    "id": "wscn:3774668",
    "domain": "股票",
    "title": "Fable 5被封禁前24小时：白宫多次电话施压，Anthropic拒绝下架，最终遭强制出口管制",
    "url": "https://wallstreetcn.com/articles/3774668",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T08:07:09+00:00",
    "summary": "亚马逊CEO一通电话，点燃了一场持续24小时的美国政府与AI公司之间的正面对决。白宫财政部长、网络安全主任、商务部长轮番致电Anthropic CEO，要求下架刚发布的Fable 5模型，均遭拒绝。最终白宫祭出出口管制“核弹”，封禁境外访问。"
  },
  {
    "id": "wscn:3774677",
    "domain": "股票",
    "title": "为何美伊协议对美联储而言未必是鸽派信号？",
    "url": "https://wallstreetcn.com/articles/3774677",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T08:01:16+00:00",
    "summary": "美伊和平协议消息令美债大涨、降息预期升温，但美国银行泼下冷水：市场的鸽派解读可能大错特错。若协议推动WTI原油在80至90美元区间企稳，通胀温和上行叠加就业风险消退，美联储反而将面临最偏鹰派的政策环境——降息无望，加息才是正解。"
  },
  {
    "id": "wscn:3774676",
    "domain": "股票",
    "title": "突发！Anthropic即将启用实名制刷脸",
    "url": "https://wallstreetcn.com/articles/3774676",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T07:50:34+00:00",
    "summary": "Anthropic宣布将于7月8日起对Claude免费/Pro/Max用户实施身份验证，要求上传带照片的政府证件并拍摄实时自拍进行人脸比对，由第三方平台Persona处理。 此举源于隐私政策更新，官方称数据不用于模型训练。"
  },
  {
    "id": "wscn:3773951",
    "domain": "股票",
    "title": "美国大厂等不及了：SOFC成为AI数据中心自发电的核心",
    "url": "https://wallstreetcn.com/premium/articles/3773951?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T07:38:20+00:00",
    "summary": "据BlackRock测算，到2030年美国需新增约148GW发电容量才能满足数据中心需求。然而，电网基础设施的建设速度严重滞后：根据PJM互联数据，2025年投入运营的AI基础设施项目平均需超7年才能达到运营状态，其中从申请到签署互联互通协议平均需3年以上，获批后还需等待约4年才能正式通电。大型变压器的采购周期已从2021年的约50周急剧延长至2026年的逾160周。"
  },
  {
    "id": "wscn:3774664",
    "domain": "股票",
    "title": "美伊协议“达成”，美国原油库存却已逼近红线，回补需数月",
    "url": "https://wallstreetcn.com/articles/3774664",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T07:30:26+00:00",
    "summary": "全球石油库存已在15周封锁期间大幅消耗，逼近危险低位。美国战略储备已动用6600万桶，库欣商业库存降至2100万桶。能源企业高管警告，库存恢复正常需数月，此外，实际通航与后续谈判仍存变数，能源危机隐患犹存。"
  },
  {
    "id": "wscn:3774665",
    "domain": "股票",
    "title": "下一代光模块之争，不会是赢家通吃？",
    "url": "https://wallstreetcn.com/articles/3774665",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T07:21:17+00:00",
    "summary": "AI算力爆炸式扩张下，光互连赛道并未走向“赢家通吃”。浙商证券最新报告揭示，硅光、LPO、LRO、NPO、CPO、TFLN六大技术路线正按场景分工协作、长期共存，CPO虽是公认终局，商业化挑战犹存；NPO已成国内主流落地路径；TFLN则悄然开辟高端细分赛道，产业链价值加速向上游光芯片与先进封装聚集。"
  },
  {
    "id": "wscn:3774672",
    "domain": "股票",
    "title": "BVLGARI宝格丽携手第二十八届上海国际电影节 闪耀星光共续光影旅程",
    "url": "https://wallstreetcn.com/articles/3774672",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T07:13:21+00:00",
    "summary": "【2026年6月13日，上海】第二十八届上海国际电影节璀璨启幕，意大利珠宝世家BVLGARI宝格丽作为官方合作伙伴，再度携手这一全球影坛盛会。宝格丽以汇聚多元之美的Eclettica万象艺境高级珠宝佳作伴全球影人闪耀亮相，珠宝的瑰丽创想与电影的隽永魅力相辅相成，共绘艺术交融华章。\n\n2026年适逢华语经典影片《刀马旦》上映四十周年，宝格丽携手上海国际电影节联合完成该影片4K修复与杜比全景声版升级，"
  },
  {
    "id": "wscn:3774667",
    "domain": "股票",
    "title": "重磅！硅基量子芯片关键材料，成功攻克",
    "url": "https://wallstreetcn.com/articles/3774667",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T06:31:43+00:00",
    "summary": "我国科学家首次成功实现丰度超99.99%的硅-28同位素自主量产，指标达国际先进水平。作为硅基量子芯片关键材料，它能极大降低量子计算的噪声干扰。该突破标志我国相关产业迈向自主可控，在半导体等前沿领域前景广阔。"
  },
  {
    "id": "wscn:3774650",
    "domain": "股票",
    "title": "光伏新政落地：组件分级分类标准能否成为政策组合拳的“转折之锚”？",
    "url": "https://wallstreetcn.com/premium/articles/3774650?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T06:31:35+00:00",
    "summary": "工信部于2026年6月11日发布的《光伏产品分级分类 第1部分：光伏组件（报批稿）》，不仅是一纸技术规范，更可能是行业供需逻辑重构的“转折之锚”。"
  },
  {
    "id": "wscn:3774666",
    "domain": "股票",
    "title": "微软CEO警告：少数人工智能领域的赢家可能会摧毁“整个行业”",
    "url": "https://wallstreetcn.com/articles/3774666",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T06:28:52+00:00",
    "summary": "纳德拉明确表示，一个掏空整个行业的AI未来，不会得到社会的认可，警告少数模型巨头或将吞噬所有经济价值，导致各行业知识资产流失与“空心化”。Snowflake、Box等科技公司CEO也发出类似警告，凸显业界对AI权力集中化的系统性忧虑。"
  },
  {
    "id": "hn:48193111",
    "domain": "股票",
    "title": "Anthropic Is Preparing for IPO and We Should Be Worried",
    "url": "https://www.vincentschmalbach.com/anthropic-ipo-developers-should-be-worried-v2/",
    "source": "vincent_s",
    "platform": "hackernews",
    "points": 89,
    "published_at": "2026-05-19T13:30:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:48506306",
    "domain": "股票",
    "title": "SpaceX vaults over $2T valuation as stock jumps after record IPO",
    "url": "https://www.reuters.com/legal/transactional/after-record-ipo-musks-spacex-faces-next-test-market-debut-2026-06-12/",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-12T16:39:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48496263",
    "domain": "股票",
    "title": "Musk's SpaceX prices record $75B IPO at $135 a share",
    "url": "https://www.reuters.com/world/musks-spacex-prices-record-75-billion-ipo-135-share-2026-06-11/",
    "source": "TechTechTech",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-11T20:53:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:48497351",
    "domain": "股票",
    "title": "SpaceX officially prices shares at $135 in the largest IPO ever",
    "url": "https://techcrunch.com/2026/06/11/spacex-officially-prices-shares-at-135-in-the-largest-ipo-ever/",
    "source": "7777777phil",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-11T22:36:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:48390053",
    "domain": "股票",
    "title": "Iran war drains US oil stocks to lowest level since 2004",
    "url": "https://www.ft.com/content/d0be73c8-b8d8-4ffd-874e-e97a6ecffef7",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 61,
    "published_at": "2026-06-03T21:06:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48505175",
    "domain": "股票",
    "title": "SpaceX makes largest ever stock market debut at $1.77T valuation",
    "url": "https://www.theguardian.com/science/2026/jun/12/spacex-stock-price-ipo-spcx",
    "source": "thomascountz",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-12T15:10:16+00:00",
    "summary": ""
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
    "id": "hn:48452224",
    "domain": "股票",
    "title": "OpenAI Confidentially Files for IPO",
    "url": "https://www.cnbc.com/2026/06/08/openai-confidentially-files-for-ipo-prepping-wall-street-for-ai-debut.html",
    "source": "rvz",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-06-08T21:16:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48231815",
    "domain": "股票",
    "title": "SpaceX not the behemoth everyone thought",
    "url": "https://www.axios.com/2026/05/21/spacex-ipo-musk-ai",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 61,
    "published_at": "2026-05-22T04:03:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48436328",
    "domain": "股票",
    "title": "Musk's SpaceX IPO Narrative Is a Whole New Level of Bullshit",
    "url": "https://text.tchncs.de/chronik-des-laufenden-wahnsinns/h1elon-musk-has-spouted-his-fair-share-of-bullshit-but-his-latest-claims-about",
    "source": "doener",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-06-07T16:24:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48451099",
    "domain": "股票",
    "title": "Why Morningstar believes the SpaceX IPO is overvalued",
    "url": "https://www.morningstar.com/stocks/why-we-think-spacex-ipo-is-overvalued",
    "source": "ForHackernews",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-06-08T20:07:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48482342",
    "domain": "股票",
    "title": "US stock market to stop shrinking for first time in 23 years",
    "url": "https://www.ft.com/content/f7dae4e1-d650-45ab-ac97-043c7a965d24",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-10T20:37:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:48391046",
    "domain": "股票",
    "title": "We Uncovered a Hidden Wealth Transfer in the SpaceX IPO. You're Holding the Bag [video]",
    "url": "https://www.youtube.com/watch?v=sYA-z0Y8WRQ",
    "source": "CharlesW",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-06-03T22:32:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48229528",
    "domain": "股票",
    "title": "The SpaceX IPO It's Worse Than You Think [video]",
    "url": "https://www.youtube.com/watch?v=-X6YzlY_8tM",
    "source": "ZeljkoS",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-05-21T22:19:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:48404734",
    "domain": "股票",
    "title": "Fidelity lowers SpaceX IPO entry requirement from $500,000 to just $2,000",
    "url": "https://finance.yahoo.com/markets/stocks/articles/fidelity-cuts-spacex-ipo-eligibility-183319186.html",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-06-04T21:15:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48383625",
    "domain": "股票",
    "title": "Dell inks $9.7B Pentagon contract after Trump acquires stock",
    "url": "https://www.washingtonpost.com/politics/2026/05/28/dell-inks-97-billion-pentagon-contract-after-trump-acquires-stock-praises-company/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-06-03T13:19:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48368083",
    "domain": "股票",
    "title": "Ask HN: What is your opinion on index rule changes to accommodate Mega-Cap IPOs?",
    "url": "https://news.ycombinator.com/item?id=48368083",
    "source": "figmert",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-06-02T09:55:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48419956",
    "domain": "股票",
    "title": "Nasdaq falls 4% and suffers worst day since April 2025 traders flee chip stocks",
    "url": "https://www.cnbc.com/2026/06/04/stock-market-today-live-updates.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-06-06T00:02:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:48454210",
    "domain": "金融",
    "title": "Federal judge blocks H1B visa $100K fee",
    "url": "https://www.alaskasnewssource.com/2026/06/08/federal-judge-blocks-h1-b-visa-100k-fee/",
    "source": "naturalmovement",
    "platform": "hackernews",
    "points": 191,
    "published_at": "2026-06-09T00:01:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:48507248",
    "domain": "金融",
    "title": "Tesla Full Self Driving uses bicycle lane in official Denmark approval video",
    "url": "https://politiken.dk/danmark/forbrug/biler/art10875514/Allerede-12-sekunder-inde-i-PR-videoen-beg%C3%A5r-selvk%C3%B8rende-Tesla-f%C3%B8rste-fejl-i-k%C3%B8benhavnsk-gade-%E2%80%93-men-det-bliver-v%C3%A6rre-endnu",
    "source": "Veserv",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-06-12T17:49:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48206387",
    "domain": "金融",
    "title": "The quadratic sandwich",
    "url": "https://fedemagnani.github.io/math/2026/04/08/the-quadratic-sandwich.html",
    "source": "cpp_frog",
    "platform": "hackernews",
    "points": 147,
    "published_at": "2026-05-20T12:06:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:48479537",
    "domain": "金融",
    "title": "Meta steals a tactic from Tesla and builds data centers in tents",
    "url": "https://techcrunch.com/2026/06/04/meta-steals-a-tactic-from-tesla-and-builds-data-centers-in-tents/",
    "source": "gnabgib",
    "platform": "hackernews",
    "points": 105,
    "published_at": "2026-06-10T17:18:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48523232",
    "domain": "金融",
    "title": "Monero Inflation Checker",
    "url": "https://www.moneroinflation.com/",
    "source": "Cider9986",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-06-14T01:16:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48518434",
    "domain": "金融",
    "title": "Gas Prices Wipe Out More Than a Year of Wage Gains",
    "url": "https://www.wsj.com/economy/inflation-wages-american-workers-cbe3f187",
    "source": "karakoram",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-06-13T15:49:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:48360414",
    "domain": "金融",
    "title": "Making Debian or Fedora persistent live images",
    "url": "https://sigwait.org/~alex/blog/2026/05/28/smdBC8.html",
    "source": "henry_flower",
    "platform": "hackernews",
    "points": 89,
    "published_at": "2026-06-01T18:02:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48483445",
    "domain": "金融",
    "title": "US President says 'I love the inflation'",
    "url": "https://www.cnbc.com/2026/06/10/trump-inflation-cpi-iran-oil.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-06-10T22:12:44+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.13697",
    "domain": "金融",
    "title": "On Reference-Regulated Multiperiod Mean-Variance Portfolio Optimization in High Dimensions",
    "url": "https://arxiv.org/abs/2606.13697",
    "source": "Yutao Deng, Jianjun Gao, Weichen Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": "arXiv:2606.13697v1 Announce Type: new Abstract: The multiperiod mean-variance (MV) portfolio optimization serves as a vital expansion of Markowitz's static MV portfolio selection framework. Just like "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.13752",
    "domain": "金融",
    "title": "What is the public's social welfare function?",
    "url": "https://arxiv.org/abs/2606.13752",
    "source": "Richard Layard, Ekaterina Oparina",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": "arXiv:2606.13752v1 Announce Type: new Abstract: Optimal public policy requires a social welfare function defined over individual utilities. While there is substantial research on income-based social w"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.13812",
    "domain": "金融",
    "title": "CFOs Meet LLMs",
    "url": "https://arxiv.org/abs/2606.13812",
    "source": "John R. Graham, Campbell R. Harvey, Manish Jha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": "arXiv:2606.13812v1 Announce Type: new Abstract: Business sentiment is a closely watched economic signal, but measuring it is slow and costly: surveys reach only a few hundred firms, arrive periodicall"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.13981",
    "domain": "金融",
    "title": "An Actuarial Cost and Revenue Model for Helicopter Emergency Medical Services: Estimating Population-Based Coverage and Sustainability Thresholds",
    "url": "https://arxiv.org/abs/2606.13981",
    "source": "Robert D. Lieberthal (Thomas Jefferson University, Lieberthal & Associates, LLC), Sabin Ahmed (The MITRE Corporation), David M. Hechtman (The MITRE Corporation), Lauren R. Indrisano (Elevance Health), Douglas R. Amirault (The MITRE Corporation), Susan Haas (The MITRE Corporation), Varun Saraswathula (Congressional Research Service)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": "arXiv:2606.13981v1 Announce Type: new Abstract: Helicopter emergency medical services (HEMS) provide rapid access to critical care but are costly to operate and difficult to sustain financially. A cle"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.13992",
    "domain": "金融",
    "title": "Group Quantization and Mellin Representations of the Heston Model",
    "url": "https://arxiv.org/abs/2606.13992",
    "source": "Santiago Garcia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": "arXiv:2606.13992v1 Announce Type: new Abstract: We construct a lifted local Lie groupoid formulation of the Heston stochastic-volatility model and use it to give a geometric interpretation of its affi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.14182",
    "domain": "金融",
    "title": "Correlation emergence and the Epps effect in two coupled limit order books",
    "url": "https://arxiv.org/abs/2606.14182",
    "source": "Chris Angstmann, Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": "arXiv:2606.14182v1 Announce Type: new Abstract: We give a unified analytic account of correlation emergence and the Epps effect in two coupled limit order books. The model starts from a discrete rando"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.14621",
    "domain": "金融",
    "title": "Evaluating the Impact of Rhode Island's Self-Sustaining Reemployment Services and Eligibility Assessment (RESEA) Program on Employment Outcomes",
    "url": "https://arxiv.org/abs/2606.14621",
    "source": "Harrison H Li, Shanna Pearson-Merkowitz, David Yokum",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": "arXiv:2606.14621v1 Announce Type: new Abstract: Prolonged unemployment carries serious economic, health, and wellbeing costs. With federal support, most U.S. states now operate a Reemployment Services"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.14050",
    "domain": "金融",
    "title": "Battery Bidding under Price Uncertainty in Wholesale Electricity Markets",
    "url": "https://arxiv.org/abs/2606.14050",
    "source": "Vincent Yinjun-Wang, Madeleine Udell",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": "arXiv:2606.14050v1 Announce Type: cross Abstract: Grid-scale batteries increasingly influence outcomes in wholesale electricity markets, but their observed bid patterns remain difficult to interpret. "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.14331",
    "domain": "金融",
    "title": "Wealth Inequality and Planetary Boundaries in a Stylized Agent-Based Model",
    "url": "https://arxiv.org/abs/2606.14331",
    "source": "Thomas Valade, Michael Benzaquen, Matthieu Cristelli, Stanislao Gualdi, Pierre Lenders",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": "arXiv:2606.14331v1 Announce Type: cross Abstract: At the intersection of rising wealth inequality and intensifying environmental pressures, we investigate a reverse causal relationship that has receiv"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.14386",
    "domain": "金融",
    "title": "Discovery under Hypothesis Redundancy: A Geometric Theory of Discovery Bottlenecks",
    "url": "https://arxiv.org/abs/2606.14386",
    "source": "Li Xia, Baoxun Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": "arXiv:2606.14386v1 Announce Type: cross Abstract: Scientific discovery saturates when new hypotheses cease to provide independent information, even if the nominal hypothesis space remains large. We st"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.14484",
    "domain": "金融",
    "title": "Quantum Horizon: An evaluation of quantum computing as a threat to Bitcoin and Ethereum",
    "url": "https://arxiv.org/abs/2606.14484",
    "source": "Iosif M. Gershteyn, Jacob A. Alber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": "arXiv:2606.14484v1 Announce Type: cross Abstract: Quantum computing poses a real, broad-based, but bounded and substantially mitigable threat to Bitcoin and Ethereum. We separate the two quantum algor"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.23847",
    "domain": "金融",
    "title": "Detecting Lookahead Bias in LLM Forecasts",
    "url": "https://arxiv.org/abs/2512.23847",
    "source": "Zhenyu Gao, Wenxi Jiang, Yutong Yan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": "arXiv:2512.23847v2 Announce Type: replace Abstract: We develop a statistical procedure to detect lookahead bias in economic forecasts generated by large language models (LLMs). Using a date-only recal"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.14852",
    "domain": "金融",
    "title": "Recovering Risk-Neutral Moments from Options",
    "url": "https://arxiv.org/abs/2601.14852",
    "source": "Tjeerd De Vries",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": "arXiv:2601.14852v3 Announce Type: replace Abstract: Extracting risk-neutral dependence from option prices has remained an open problem since Ross (1976). We propose a projection estimator that uses po"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.10060",
    "domain": "金融",
    "title": "Skill Premia and Pre-Marital Investments in Marriage Markets",
    "url": "https://arxiv.org/abs/2605.10060",
    "source": "Aditya Kuvalekar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": "arXiv:2605.10060v3 Announce Type: replace Abstract: I study a decentralized marriage market with search frictions, costly pre-marital skill investments, and non-transferable utility. Despite a fully s"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.18784",
    "domain": "金融",
    "title": "The Insurability Frontier of AI Risk: Mapping Threats to Affirmative Coverage, Silent Exposures, and Exclusions",
    "url": "https://arxiv.org/abs/2605.18784",
    "source": "Alex Leung, Rex Zhang, Ervin Ling, Kentaroh Toyoda, SiewMei Loh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": "arXiv:2605.18784v2 Announce Type: replace Abstract: The rapid diffusion of agentic AI has created a new coverage problem for commercial insurance: some AI-mediated losses are now affirmatively insured"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.14967",
    "domain": "金融",
    "title": "Deep Learning and Elicitability for McKean-Vlasov FBSDEs With Common Noise",
    "url": "https://arxiv.org/abs/2512.14967",
    "source": "Felipe J. P. Antunes, Yuri F. Saporito, Sebastian Jaimungal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": "arXiv:2512.14967v2 Announce Type: replace-cross Abstract: We present a novel numerical method for solving McKean--Vlasov forward--backward stochastic differential equations (MV--FBSDEs) with common no"
  },
  {
    "id": "hn:48384810",
    "domain": "金融",
    "title": "Tesla retroactively added 'supervised' to FSD contracts owners signed years ago",
    "url": "https://electrek.co/2026/06/03/tesla-retroactively-modified-fsd-contracts-supervised/",
    "source": "breve",
    "platform": "hackernews",
    "points": 73,
    "published_at": "2026-06-03T14:43:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48488805",
    "domain": "金融",
    "title": "Feds will abruptly dismantle system monitoring climate change, oceans",
    "url": "https://www.usatoday.com/story/news/nation/2026/06/11/climate-change-ocean-monitoring-system-dismantled/90378309007/",
    "source": "OutOfHere",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-11T11:12:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:48491301",
    "domain": "金融",
    "title": "Craig Federighi Details Apple's Collaboration with Google for Siri AI in iOS 27",
    "url": "https://9to5mac.com/2026/06/08/craig-federighi-details-apples-collaboration-with-google-for-siri-ai-in-ios-27/",
    "source": "tambourine_man",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-11T15:01:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:48436542",
    "domain": "金融",
    "title": "Ripping a DVD, a federal crime in 1999, requires $22 and free software in 2026",
    "url": "https://ringmast4r.substack.com/p/in-1999-this-was-a-federal-crime",
    "source": "akkartik",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-06-07T16:48:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48406282",
    "domain": "金融",
    "title": "S&P Global keeps fast index entry rules unchanged as SpaceX listing looms",
    "url": "https://www.reuters.com/business/finance/sp-global-keeps-fast-entry-proposal-unchanged-spacex-listing-looms-2026-06-04/",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-06-04T23:55:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:48317563",
    "domain": "金融",
    "title": "Microsoft data suggests using AI is more expensive than hiring people",
    "url": "https://finance.yahoo.com/sectors/technology/articles/microsoft-data-suggests-using-ai-225900743.html",
    "source": "voxadam",
    "platform": "hackernews",
    "points": 68,
    "published_at": "2026-05-29T00:49:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48438281",
    "domain": "金融",
    "title": "Boomers are hoarding most of America's wealth and power",
    "url": "https://finance.yahoo.com/economy/articles/golden-years-not-golden-boomers-113000201.html",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-06-07T20:35:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48451917",
    "domain": "金融",
    "title": "Federal judge rules Trump's $100k fee for H-1B visas unlawful",
    "url": "https://www.theguardian.com/us-news/2026/jun/08/trump-h-1b-visa-fee-invalidated",
    "source": "xpl",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-06-08T20:57:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48476514",
    "domain": "金融",
    "title": "GnuCash is right. It's also why I built my own finance app",
    "url": "https://k-id.app/blog/gnucash-is-right/",
    "source": "tinosar",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-06-10T14:06:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:48210413",
    "domain": "金融",
    "title": "Standard Chartered CEO walks back comment about 'lower-value human capital'",
    "url": "https://www.wsj.com/finance/banking/ceo-walks-back-comment-about-replacing-lower-value-human-capital-with-ai-15bdfc5c",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-05-20T16:38:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48449003",
    "domain": "金融",
    "title": "Half of Americans say they're worse off financially than a year ago",
    "url": "https://www.cbsnews.com/news/americans-worse-off-financially-year-ago-fed-survey/",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-06-08T18:12:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:48377347",
    "domain": "金融",
    "title": "Feds failing in bid to take a supercomputer from a climate research center",
    "url": "https://arstechnica.com/science/2026/06/judge-blocks-part-of-trump-admins-effort-to-hurt-colorado-research-center/",
    "source": "yodon",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-06-02T22:46:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48371952",
    "domain": "金融",
    "title": "Amazon joins Microsoft in sending message to employees",
    "url": "https://finance.yahoo.com/sectors/technology/articles/amazon-joins-microsoft-sending-shocking-171700630.html",
    "source": "hereticles",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-06-02T15:58:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:48349067",
    "domain": "金融",
    "title": "Nearly Half of Home Insurance Claims Result in Zero Payout",
    "url": "https://www.wsj.com/finance/the-home-insurance-coin-flip-nearly-half-of-claims-result-in-zero-payout-4b49acaf",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-05-31T19:45:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48401755",
    "domain": "金融",
    "title": "Fedora 43 Upgrade revealed 20 years old Outlook Security Bug",
    "url": "https://fedoramagazine.org/fedora-43-upgrade-revealed-20-years-old-outlook-security-bug/",
    "source": "thewebguyd",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-06-04T17:24:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:48364392",
    "domain": "金融",
    "title": "How to Silence the Federal Workforce",
    "url": "https://www.theatlantic.com/ideas/2026/06/trumps-intimidation-whistleblowers-nda/687377/",
    "source": "paulpauper",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-06-02T00:38:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:48271942",
    "domain": "金融",
    "title": "Show HN: Fungible – A local personal finance app in the terminal",
    "url": "https://github.com/tomfunk/fungible",
    "source": "tomfunk",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-05-25T21:35:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:48403461",
    "domain": "金融",
    "title": "Open Letter to President of Russian Federation from President of Ukraine",
    "url": "https://www.president.gov.ua/en/news/vidkritij-list-prezidentu-rosijskoyi-federaciyi-vid-preziden-104769",
    "source": "defly",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-04T19:27:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48377419",
    "domain": "金融",
    "title": "FBI charges two NIH researchers with smuggling monkeypox to US from Congo",
    "url": "https://www.justice.gov/usao-edmi/pr/feds-charge-foreign-nationals-working-national-institutes-health-smuggling-monkeypox",
    "source": "delichon",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-02T22:58:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48271001",
    "domain": "金融",
    "title": "Stablecoins Are Private Money. That's Why They're a Risk to the Economy",
    "url": "https://www.wsj.com/finance/currencies/stablecoins-are-private-money-thats-why-theyre-a-risk-to-the-economy-d3498171",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-05-25T20:02:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:48328797",
    "domain": "金融",
    "title": "Federal judge orders Trump's name be removed from Kennedy Center",
    "url": "https://www.msn.com/en-us/news/politics/federal-judge-orders-trump-s-name-be-removed-from-kennedy-center/ar-AA24neRw",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-05-29T20:29:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:48327518",
    "domain": "金融",
    "title": "Americans Are Falling Behind on Their $1.25T Credit-Card Bill",
    "url": "https://www.wsj.com/personal-finance/credit/us-credit-card-debt-af5c7c77",
    "source": "tcp_handshaker",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-05-29T18:41:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48284628",
    "domain": "金融",
    "title": "Trump's 25% cut on Nvidia chips to China backfired as Beijing blocks H200 sales",
    "url": "https://finance.yahoo.com/markets/stocks/articles/trumps-25-cut-nvidia-chips-194500691.html",
    "source": "frasermarlow",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-05-26T19:21:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48199462",
    "domain": "金融",
    "title": "Invisible_playwright: Stealth Firefox that passes every bot detection test",
    "url": "https://github.com/feder-cr/invisible_playwright",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-05-19T20:51:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:48330421",
    "domain": "金融",
    "title": "The record divide between corporate profits and worker pay",
    "url": "https://www.wsj.com/finance/stocks/the-record-divide-between-corporate-profits-and-worker-pay-ea4c75bc",
    "source": "hhs",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-05-29T22:55:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:48229518",
    "domain": "金融",
    "title": "Show HN: Smithereen – an early-Facebook-style Fediverse server",
    "url": "https://smithereen.software",
    "source": "grishka",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-05-21T22:18:25+00:00",
    "summary": ""
  }
]
```
