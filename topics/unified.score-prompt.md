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

- 今日日期：`2026-06-17`
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
  "date": "2026-06-17",
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
    "id": "bvid:BV1NvRyBzEhq",
    "domain": "AI",
    "title": "全网最全！60分钟全面掌握Claude Code～【附完整文档】",
    "url": "http://www.bilibili.com/video/av116522328524431",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1173828,
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
    "points": 1166304,
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
    "points": 1041457,
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
    "points": 839586,
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
    "points": 708797,
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
    "points": 628784,
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
    "points": 415888,
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
    "points": 373014,
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
    "points": 344594,
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
    "points": 335739,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 217861,
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
    "points": 196611,
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
    "points": 174640,
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
    "points": 156344,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV18n7Z6dEGS",
    "domain": "AI",
    "title": "【全500集】B站最全最细的AI漫剧零基础全套教程（包含剧本+分镜+静帧+视频+配音+剪辑+保持人物一致性等）手把手教你从入门到精通AI漫剧，学完即可就业、副业",
    "url": "http://www.bilibili.com/video/av116689479997111",
    "source": "哔哩AI漫剧研究社",
    "platform": "bilibili",
    "points": 155415,
    "published_at": "2026-06-04T02:38:24+00:00",
    "summary": "创作不易，感谢大家的三连与支持！\n本套教程从最基础的AI漫剧核心开始到AIGC相关技术的宏观运用，名校名师+央企大佬全程结合项目实战，不仅适合零基础小白学习，也适合有一定基础的同学进阶提升、巩固学习。\n如果觉得视频对你有帮助，就动手多多转发一下吧~"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 151911,
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
    "points": 143370,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "domain": "AI",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 135635,
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
    "points": 131475,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 91569,
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
    "points": 71192,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1HM7C6BEnF",
    "domain": "AI",
    "title": "【B站精选】目前B站最细最全的AI大模型全套教程，2026最新版，包含所有干货！手把手带你从入门到精通！少走99%的弯路！存下吧！真的很难找全的！",
    "url": "http://www.bilibili.com/video/av116696929076767",
    "source": "AIAgent开发",
    "platform": "bilibili",
    "points": 66365,
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
    "points": 63908,
    "published_at": "2026-01-18T03:25:00+00:00",
    "summary": "大家好，这里是饼干！🍪\n这是我的新坑——**《地块召唤师》**开发实战分享的第一期。\n很多朋友问独立开发如何提升效率？这期视频我不聊虚的，直接公开我从 0 到 1 搭建的 AI + Godot 高效工作流。\n从游戏引擎的选择，到 Claude Code、Copilot 等 AI 工具的实战配置，再到如何用“明确需求”的方法论（SMART原则+双钻模型）来驾驭 AI，让它不仅仅是写代码的工具，更成为"
  },
  {
    "id": "bvid:BV1wDFszxEGX",
    "domain": "AI",
    "title": "AI 直接操控 UE5.7！AI 读工程+写蓝图+自动实现功能",
    "url": "http://www.bilibili.com/video/av116030487732208",
    "source": "UnrealXu",
    "platform": "bilibili",
    "points": 60578,
    "published_at": "2026-02-07T17:23:41+00:00",
    "summary": "这是一个把 Codex 接入 UE5 编辑器的 AI 助手插件：支持理解项目结构、定位关键蓝图/输入/关卡对象，辅助编写与修改蓝图和 C++，并在 World 场景层面完成落地调整（灯光/天气/Actor 等）。目前功能持续迭代中，欢迎留言交流、提交需求"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 51911,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1DfEr6UE32",
    "domain": "AI",
    "title": "开源免费，本地电脑变成&quot;公网服务器”，他人也能访问！",
    "url": "http://www.bilibili.com/video/av116734778480044",
    "source": "小宇Boi",
    "platform": "bilibili",
    "points": 44634,
    "published_at": "2026-06-12T02:33:38+00:00",
    "summary": "SKill地址：github.com/xiaoyuboi/cloudflare-tunnel-skill\n部署分为临时部署和长期部署，临时部署会随机分配一个域名，长期部署需要自己提供域名。\n使用方式非常简单，直接将此skill发给Agent，让它帮你操作即可。\n\n如果视频对你有帮助，记得点赞+关注～"
  },
  {
    "id": "bvid:BV1pbR4BSEfB",
    "domain": "AI",
    "title": "【B站天花板】目前B站讲的最全最细的Cherry Studio教程。15分钟教你用CherryStudio+MCP搭建本地知识库+自动化AI智能体！手把手教程！",
    "url": "http://www.bilibili.com/video/av116526841600956",
    "source": "AI大模型应用_",
    "platform": "bilibili",
    "points": 40047,
    "published_at": "2026-05-06T09:11:55+00:00",
    "summary": "【B站天花板】目前B站讲的最全最细的Cherry Studio教程。15分钟教你用CherryStudio+MCP搭建本地知识库+自动化AI智能体！手把手教程！"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 35972,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27318,
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
    "points": 27125,
    "published_at": "2026-05-09T09:24:55+00:00",
    "summary": "视频配套籽料都帮你们整理在这啦：https://www.bilibili.com/opus/972885207239622681\r\n基础学习包，配套课件，PDF电子书籍，问题解答等\r\n记得[热词系列_三连]up持续为你们带来更优质的课程教学！"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 26562,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV16BkEBtEjW",
    "domain": "AI",
    "title": "老张公开课：算力、GPU、AI服务器详解（上）",
    "url": "http://www.bilibili.com/video/av115927962159456",
    "source": "It_server技术分享",
    "platform": "bilibili",
    "points": 26561,
    "published_at": "2026-01-20T14:51:01+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 23396,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1RUDsBWEHb",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的Cursor+Skills实战指南教程，手把手带你开发爆款app，全程干货无废话！比付费效果强十倍！",
    "url": "http://www.bilibili.com/video/av116373464350785",
    "source": "AI大模型技术教程",
    "platform": "bilibili",
    "points": 22594,
    "published_at": "2026-04-09T10:15:00+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\nCursor+Skills频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV1GLdABKEaR",
    "domain": "AI",
    "title": "【自用】Claude Code 驱动 Comsol 复现论文仿真",
    "url": "http://www.bilibili.com/video/av116534089482864",
    "source": "Ricardo_Tsang",
    "platform": "bilibili",
    "points": 21834,
    "published_at": "2026-05-07T16:10:32+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1RH7C6ZEAg",
    "domain": "AI",
    "title": "这绝对是B站唯一将OpenCode 从入门到精通讲明白的教程，手把手带你从入门到实战使用，保姆级教程，存下吧，比啃书好太多了！",
    "url": "http://www.bilibili.com/video/av116696509582055",
    "source": "码士集团_马小帆",
    "platform": "bilibili",
    "points": 19168,
    "published_at": "2026-06-05T08:30:45+00:00",
    "summary": "这绝对是B站唯一将OpenCode 从入门到精通讲明白的教程，手把手带你从入门到实战使用，保姆级教程，存下吧，比啃书好太多了！\n【视频配套籽料+问题解答】请看”平论区置顶”自取哦！！！\n视频制作不易，如果视频对你有用的话❤请一键三莲【长按点赞】支持一下up哦，拜托，这对我真的很重要！"
  },
  {
    "id": "bvid:BV1jYRRBDExF",
    "domain": "AI",
    "title": "让AI直接操作godot开发游戏，免费开源MCP插件",
    "url": "http://www.bilibili.com/video/av116545648860073",
    "source": "Yurineko73",
    "platform": "bilibili",
    "points": 18926,
    "published_at": "2026-05-10T03:00:00+00:00",
    "summary": "因为想找一个好用的mcp工具，结果发现不是要收费就是不可商用，于是借助ai直接搓了一个出来。\n目前已经发布1.0.1版本，在godot asset library搜索 [godot mcp native]即可下载使用，\n也可以去GitHub上下载完整项目 https://github.com/yurineko73/Godot-MCP-Native\n免费开源，可以随意扩展和修改，如果有需要的功能或遇"
  },
  {
    "id": "bvid:BV1QzuRz2Epz",
    "domain": "AI",
    "title": "【中文】Cursor AI Unity 教程：新手指南，简单易懂 ｜ Nikhil Malankar",
    "url": "http://www.bilibili.com/video/av114879017000489",
    "source": "CursorInsider",
    "platform": "bilibili",
    "points": 17363,
    "published_at": "2025-07-19T13:00:00+00:00",
    "summary": "在本视频中，我将带你逐步完成 Cursor AI 在 Unity 中的完整设置和配置，帮助你利用 AI 驱动的代码辅助功能，加速你的游戏开发流程。无论你是正在构建一个新项目，还是将 AI 集成到现有的 Unity 游戏中，本教程都涵盖了你所需的一切。\n\n🔧 你将学到：\n✔️ 如何在 Unity 中安装和配置 Cursor AI\n✔️ 设置 Cursor AI 扩展以实现无缝开发\n✔️ 使用 AI "
  },
  {
    "id": "bvid:BV1wuLHzDEGA",
    "domain": "AI",
    "title": "【Godot&amp;Cursor】0.亲测一个月后，我选择Godot+Cursor组合做独立游戏",
    "url": "http://www.bilibili.com/video/av114398869853632",
    "source": "破妄-胖",
    "platform": "bilibili",
    "points": 13665,
    "published_at": "2025-04-25T13:43:22+00:00",
    "summary": "飞书文档：https://sh67ozct1z.feishu.cn/docx/Hn5jd0cE6op1Sux9RrFcl8Npnbd"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 13423,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV14cZqB8EBY",
    "domain": "AI",
    "title": "AI攻克不了的领域竟然是它？揭秘CNC编程为何让AI束手无策",
    "url": "http://www.bilibili.com/video/av116097411976217",
    "source": "极微视界",
    "platform": "bilibili",
    "points": 13086,
    "published_at": "2026-02-19T12:59:23+00:00",
    "summary": "CNC编程AI化有多难？本视频深度解析为什么AI编程在制造业进展缓慢。\n从材料、刀具、机床到隐性知识，揭秘老师傅的经验为什么无法数字化。\nPowerMill、CloudNC等AI编程软件的真实水平如何？CNC编程师的未来在哪里？\n\n⏱️ 时间轴 Timestamps:\n\n00:00 开篇：AI在CNC领域的困境\n00:20 材料的复杂性：为什么同样是45#钢参数却不同\n01:01 刀具与机床的个体"
  },
  {
    "id": "bvid:BV1CbvxBwEah",
    "domain": "AI",
    "title": "真的不用服务器！用Cloudflare Workers+D1轻松搭建网站！",
    "url": "http://www.bilibili.com/video/av115803408045159",
    "source": "软件工程师Tim",
    "platform": "bilibili",
    "points": 12210,
    "published_at": "2025-12-29T14:51:53+00:00",
    "summary": "本期影片分享一下如何利用cloudflare workers搭建网站，并且利用d1免费数据库，实现无服务器的一个带前后端功能的网站。也就是说，即使你没有服务器，也能够搭建一个属于自己的网站。比如我自己搭建的这个案例网站在线留言板。就是完全搭建在cloudflare workers上面的，里面有静态页面 也有动态api接口。都是部署在workers上面的，并且集成了它提供的数据库。\n\n\n#cloud"
  },
  {
    "id": "bvid:BV1DktBzLEvb",
    "domain": "AI",
    "title": "AI 服务器爆炸图鉴！了解 AI 服务器/GPU服务器长什么样子！",
    "url": "http://www.bilibili.com/video/av114988018571687",
    "source": "ZOMI酱",
    "platform": "bilibili",
    "points": 11447,
    "published_at": "2025-08-07T14:51:04+00:00",
    "summary": "AI 服务器爆炸图鉴！了解 AI 服务器/GPU服务器长什么样子！"
  },
  {
    "id": "bvid:BV1qHEQ6RERo",
    "domain": "AI",
    "title": "使用 Rust 开发 AI Agent - 简介",
    "url": "http://www.bilibili.com/video/av116724259232762",
    "source": "软件工艺师",
    "platform": "bilibili",
    "points": 10917,
    "published_at": "2026-06-10T06:00:43+00:00",
    "summary": "使用 Rust 从 0 开始搭建 AI Agent"
  },
  {
    "id": "bvid:BV1QNEq6uEGM",
    "domain": "AI",
    "title": "全网最详细的Vibe Coding系统教程：Claude Code + Codex 从零到实战，存下吧！真的很难找全了",
    "url": "http://www.bilibili.com/video/av116731557186523",
    "source": "马士兵学堂",
    "platform": "bilibili",
    "points": 9162,
    "published_at": "2026-06-11T13:01:04+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1a4G96qEGz",
    "domain": "AI",
    "title": "【全60集】吊打付费！全网最详细的Agent开发零基础全套教程，从入门到实战！手把手教你搭建专属智能体，全程干货无废话，让你少走99%弯路！存下吧，很难找全的！",
    "url": "http://www.bilibili.com/video/av116650657454753",
    "source": "AI-Agent开发",
    "platform": "bilibili",
    "points": 8569,
    "published_at": "2026-05-28T06:04:47+00:00",
    "summary": "【全60集】吊打付费！全网最详细的Agent开发零基础全套教程，从入门到实战！手把手教你搭建专属智能体，全程干货无废话，让你少走99%弯路！存下吧，很难找全的！"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 8246,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV1ssEE6CEks",
    "domain": "AI",
    "title": "Ai自动画图：CAD建筑平面图测试（CodexGPT5.5）",
    "url": "http://www.bilibili.com/video/av116719259485897",
    "source": "Tutor南洋",
    "platform": "bilibili",
    "points": 8135,
    "published_at": "2026-06-09T08:47:15+00:00",
    "summary": "体验一下ai画图，不过CAD软件基本操作也不能拉下~\nCAD教学基础入门视频合集↓\n传送门：BV1aT4y1B7oY\n整个合集教学的，不要跳着看啊喂！\n看完了那基本就能跟上啦，提问请@我，不然评论太多我是看不到的"
  },
  {
    "id": "bvid:BV1Y4Gd6LELX",
    "domain": "AI",
    "title": "极简安装！Claude Code+CC switch 连接 Deepseek",
    "url": "http://www.bilibili.com/video/av116634383550090",
    "source": "水哥澎湃",
    "platform": "bilibili",
    "points": 7907,
    "published_at": "2026-05-25T09:00:14+00:00",
    "summary": "本视频分享Claude Code 极简安装 + 连接 Deepseek的完整方案，解决国内用户使用不稳定、收费高的问题。用 Harness（马鞍缰绳）思路通俗讲解核心价值，让大模型拥有本地执行、记忆、任务编排能力。全程无复杂命令，包含 Claude Code 部署、CC switch 安装、Deepseek API 配置、连接测试，一步到位，新手也能轻松搞定。\n\n\n00:00  1-目标\n00:2"
  },
  {
    "id": "bvid:BV1qNS8BNESd",
    "domain": "AI",
    "title": "AI黑客实战：Cloud Code自动化渗透测试Hack the Box",
    "url": "http://www.bilibili.com/video/av115652480209157",
    "source": "黑客酒吧",
    "platform": "bilibili",
    "points": 7414,
    "published_at": "2025-12-03T01:11:01+00:00",
    "summary": "Teja挑战AI极限，用Cloud Code CLI在Hack the Box上实现全自动渗透测试！视频展示如何配置AI代理，一键扫描、漏洞利用、权限提升，并自动生成详细渗透报告。亮点包括MCP集成实战、沙盒环境安全测试，以及AI在网络安全中的颠覆性应用。"
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
    "id": "rss:https://www.eetimes.com/ymin-slx-hybrid-supercapacitors-replace-batteries-in-space-constrained-designs/",
    "domain": "AI 算力 / 半导体",
    "title": "YMIN SLX Hybrid Supercapacitors Replace Batteries in Space-Constrained Designs",
    "url": "https://www.eetimes.com/ymin-slx-hybrid-supercapacitors-replace-batteries-in-space-constrained-designs/",
    "source": "Shanghai Yongming Electronic Co.,Ltd",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T13:00:00+00:00",
    "summary": "YMIN SLX Hybrid Supercapacitors feature ultra-small diameters, enabling fast charging, long life, safety, and battery-free advantages. The post YMIN SLX Hybrid Supercapacitors Replace Batteries in Spa"
  },
  {
    "id": "rss:https://www.eetimes.com/risc-v-silicon-in-the-jungle-could-save-the-amazon/",
    "domain": "AI 算力 / 半导体",
    "title": "RISC-V Silicon in the Jungle Could Save the Amazon",
    "url": "https://www.eetimes.com/risc-v-silicon-in-the-jungle-could-save-the-amazon/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T08:41:10+00:00",
    "summary": "Researchers at the University of São Paulo use RISC-V to build the Internet of Trees, a real-time monitoring network for the Amazon rainforest. The post RISC-V Silicon in the Jungle Could Save the Ama"
  },
  {
    "id": "rss:https://www.eetimes.com/globalfoundries-first-chipmaker-to-support-open-standard-for-ai-scale-up/",
    "domain": "AI 算力 / 半导体",
    "title": "GlobalFoundries: First Chipmaker to Support Open Standard for AI Scale Up",
    "url": "https://www.eetimes.com/globalfoundries-first-chipmaker-to-support-open-standard-for-ai-scale-up/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T22:00:00+00:00",
    "summary": "GlobalFoundries leads with the first silicon to support OCI MSA, shaking up AI data centers. The post GlobalFoundries: First Chipmaker to Support Open Standard for AI Scale Up appeared first on EE Tim"
  },
  {
    "id": "rss:https://www.eetimes.com/tensordyne-tapes-out-lns-based-ai-chip-claims-huge-power-advantages/",
    "domain": "AI 算力 / 半导体",
    "title": "Tensordyne Tapes Out LNS-Based AI Chip, Claims Huge Power Advantages",
    "url": "https://www.eetimes.com/tensordyne-tapes-out-lns-based-ai-chip-claims-huge-power-advantages/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T16:00:00+00:00",
    "summary": "The company said it can consume an order of magnitude less power per token versus GPU alternatives. The post Tensordyne Tapes Out LNS-Based AI Chip, Claims Huge Power Advantages appeared first on EE T"
  },
  {
    "id": "rss:https://www.eetimes.com/andy-mclean-rapidus-mou-will-help-british-innovators-access-2-nm-technology/",
    "domain": "AI 算力 / 半导体",
    "title": "Andy McLean: Rapidus MoU Will Help British Innovators Access 2-nm Technology",
    "url": "https://www.eetimes.com/andy-mclean-rapidus-mou-will-help-british-innovators-access-2-nm-technology/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T13:10:12+00:00",
    "summary": "As the UK Semiconductor Centre signs an MoU with Rapidus, EE Times speaks exclusively with its new CEO, Andy McLean. The post Andy McLean: Rapidus MoU Will Help British Innovators Access 2-nm Technolo"
  },
  {
    "id": "rss:https://www.eetimes.com/how-multi-sense-technologies-are-redefining-human-machine-interfaces-and-dexterous-robotics/",
    "domain": "AI 算力 / 半导体",
    "title": "How Multi-Sense Technologies Are Redefining Human-Machine Interfaces and Dexterous Robotics",
    "url": "https://www.eetimes.com/how-multi-sense-technologies-are-redefining-human-machine-interfaces-and-dexterous-robotics/",
    "source": "Vibheesh Bharathan, Director, Head of PSOC™ Multi-Sense MCUs, Infineon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T13:00:00+00:00",
    "summary": "Discover how multi-sense technologies are transforming HMIs, smart appliances, and dexterous robotics with AI-powered tactile sensing. The post How Multi-Sense Technologies Are Redefining Human-Machin"
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
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/agi-ai858-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "AGI AI858 2TB SSD Review — High-end PCIe 5 speeds on a budget",
    "url": "https://www.tomshardware.com/pc-components/ssds/agi-ai858-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T12:10:00+00:00",
    "summary": "The AGI AI858 is a wallet-friendly entry into the high-end PCIe 5.0 SSD playground with good random read latency, a bundled heatsink, and minimal trade-offs."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intels-one-two-punch-plan-in-desktop-cpus-is-taking-shape-z990-spotted-nova-lake-detailed-raptor-lake-next-teased",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's one-two punch plan in desktop CPUs is taking shape — Z990 spotted, Nova Lake detailed, ‘Raptor Lake Next’ teased",
    "url": "https://www.tomshardware.com/pc-components/cpus/intels-one-two-punch-plan-in-desktop-cpus-is-taking-shape-z990-spotted-nova-lake-detailed-raptor-lake-next-teased",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T12:00:00+00:00",
    "summary": "Intel’s next-gen desktop plans are starting to take shape, and Computex entertained a lot of murmurs about what’s coming from Team Blue over the next year at the event."
  },
  {
    "id": "rss:https://www.tomshardware.com/phones/commodore-announces-linux-based-flip-phone-with-no-social-media-no-browser-the-callback-8020-will-be-available-in-five-retro-colorways-starting-at-usd499-runs-99-percent-of-android-apps",
    "domain": "AI 算力 / 半导体",
    "title": "Commodore announces Linux-based flip phone with ‘no social media, no browser’ — the Callback 8020 will be available in five retro colorways starting at $499, runs 99% of Android apps",
    "url": "https://www.tomshardware.com/phones/commodore-announces-linux-based-flip-phone-with-no-social-media-no-browser-the-callback-8020-will-be-available-in-five-retro-colorways-starting-at-usd499-runs-99-percent-of-android-apps",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T11:42:13+00:00",
    "summary": "After some teasing and a couple of red herrings Commodore today unveiled a retro-styled flip phone dubbed the Callback 8020."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/microsd-cards/save-40-percent-on-this-ultra-fast-samsung-microsd-card-with-256gb-storage-now-just-usd47-99-usd32-saving-on-p9-express-model-with-read-speeds-of-up-to-800-mb-s-perfect-for-a-gaming-laptop-or-a-nintendo-switch-2",
    "domain": "AI 算力 / 半导体",
    "title": "Save 40% on this ultra-fast Samsung microSD card with 256GB storage, now just $47.99 — $32 saving on P9 Express model with read speeds of up to 800 MB/s, perfect for a gaming laptop or a Nintendo Swit",
    "url": "https://www.tomshardware.com/pc-components/microsd-cards/save-40-percent-on-this-ultra-fast-samsung-microsd-card-with-256gb-storage-now-just-usd47-99-usd32-saving-on-p9-express-model-with-read-speeds-of-up-to-800-mb-s-perfect-for-a-gaming-laptop-or-a-nintendo-switch-2",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T11:24:29+00:00",
    "summary": "Save $32 on this Samsung P9 Express microSD card with read speeds up to 800MB/s."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/get-an-rtx-5090-gaming-laptop-for-less-than-usd3-000-acers-16-inch-predator-with-2tb-of-storage-and-32gb-of-ram-is-now-usd500-off",
    "domain": "AI 算力 / 半导体",
    "title": "Get an RTX 5090 gaming laptop for less than $3,000 — Acer's 16-inch Predator with 2TB of storage and 32GB of RAM is now $500 off",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/get-an-rtx-5090-gaming-laptop-for-less-than-usd3-000-acers-16-inch-predator-with-2tb-of-storage-and-32gb-of-ram-is-now-usd500-off",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T11:24:20+00:00",
    "summary": "Save $500 on a super-powerful 16-inch gaming laptop with RTX 5090 graphics and a 240Hz OLED screen. Acer's Predator Helios AI falls to just $2,999."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-keyboards/these-are-the-four-keyboards-im-still-using-after-reviewing-keyboards-for-years-how-a-500-hz-tkl-and-a-stream-deck-layout-dominated-my-desk",
    "domain": "AI 算力 / 半导体",
    "title": "These are the four keyboards I'm still using after reviewing keyboards for years — How a 500 Hz TKL and a Stream Deck layout dominated my desk",
    "url": "https://www.tomshardware.com/peripherals/gaming-keyboards/these-are-the-four-keyboards-im-still-using-after-reviewing-keyboards-for-years-how-a-500-hz-tkl-and-a-stream-deck-layout-dominated-my-desk",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T11:10:00+00:00",
    "summary": "It's hard to find a keyboard that's satisfying for both writing and gaming and I'm not sure the perfect board even exists. But while I wait to find it, these are the keyboards I keep coming back to, f"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-massive-sp7-socket-for-epyc-venice-and-intels-gargantuan-9-324-pin-socket-for-diamond-rapids-appear-at-computex-sp7-and-lga9324-1-sockets-will-power-the-next-generation-of-ai-servers",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s massive SP7 socket for EPYC Venice and Intel’s gargantuan 9,324-pin socket for Diamond Rapids appear at Computex — SP7 and LGA9324-1 sockets will power the next generation of AI servers",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-massive-sp7-socket-for-epyc-venice-and-intels-gargantuan-9-324-pin-socket-for-diamond-rapids-appear-at-computex-sp7-and-lga9324-1-sockets-will-power-the-next-generation-of-ai-servers",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T11:06:33+00:00",
    "summary": "Next-generation data center processors from AMD and Intel with 16 DDR5 memory channels are even bigger than today’s designs."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/finland-charges-russian-captain-and-crew-member-of-ship-suspected-of-damaging-undersea-cables-prosecutors-claim-ship-had-eight-more-targets-before-it-was-stopped-by-coast-guard",
    "domain": "AI 算力 / 半导体",
    "title": "Finland charges Russian captain and crew member of ship suspected of damaging undersea cables — prosecutors claim ship had eight more targets before it was stopped by coast guard",
    "url": "https://www.tomshardware.com/networking/finland-charges-russian-captain-and-crew-member-of-ship-suspected-of-damaging-undersea-cables-prosecutors-claim-ship-had-eight-more-targets-before-it-was-stopped-by-coast-guard",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T11:04:28+00:00",
    "summary": "Finnish prosecutors charged two crew members of a cargo ship suspected of deliberately damaging two undersea cables at the turn of the year, with two more remaining detained in Finland. This is the se"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tsmc-says-panel-packaging-wont-replace-cowos-anytime-soon-for-the-largest-future-ai-processors-wafer-level-tech-can-scale-to-58-massive-dies-in-one-package",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC says panel packaging won't replace CoWoS anytime soon for the largest future AI processors — wafer-level tech can scale to 58 massive dies in one package",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-says-panel-packaging-wont-replace-cowos-anytime-soon-for-the-largest-future-ai-processors-wafer-level-tech-can-scale-to-58-massive-dies-in-one-package",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T11:00:00+00:00",
    "summary": "TSMC is exploring panel-level packaging and is working on its CoPoS technology, but the company's Kevin Zhang says wafer-level packaging technologies is considerably more advanced than panel-level pac"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/intels-cancelled-arctic-sound-xe-hp-multi-tile-gpu-surfaces-in-new-engineering-sample-companys-long-lost-data-center-prototype-features-32gb-of-hbm2e",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's long-lost data center prototype 'Arctic Sound' Xe-HP multi-tile GPU surfaces in new engineering sample — Company's cancelled AI processor features 32GB of HBM2E",
    "url": "https://www.tomshardware.com/pc-components/gpus/intels-cancelled-arctic-sound-xe-hp-multi-tile-gpu-surfaces-in-new-engineering-sample-companys-long-lost-data-center-prototype-features-32gb-of-hbm2e",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T10:30:00+00:00",
    "summary": "Intel's cancelled \"Arctic Sound\" AI GPU based on the original Xe-HP architecture has been pictured sporting two tiles and 32GB of HBM2E."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/amazon-uk-has-slashed-43-percent-off-this-excellent-4k-32-inch-oled-gaming-monitor-lowest-ever-price-on-this-asus-rog-strix-oled-now-just-gbp599",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon UK has slashed 43% off this excellent 4K 32-inch OLED gaming monitor — lowest-ever price on this ASUS ROG Strix OLED now just £599",
    "url": "https://www.tomshardware.com/pc-components/amazon-uk-has-slashed-43-percent-off-this-excellent-4k-32-inch-oled-gaming-monitor-lowest-ever-price-on-this-asus-rog-strix-oled-now-just-gbp599",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T10:17:13+00:00",
    "summary": "Get 43% off this excellent Asus ROG Strix OLED monitor."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/project-jupiter-ai-data-center-build-raises-concerns-about-water-usage-in-rural-new-mexico-desert-oracle-calls-water-usage-negligible-for-11-million-gallon-one-time-fill",
    "domain": "AI 算力 / 半导体",
    "title": "Project Jupiter AI data center build raises concerns about water usage in rural New Mexico desert — Oracle calls water usage 'negligible' for 11 million gallon one-time fill",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/project-jupiter-ai-data-center-build-raises-concerns-about-water-usage-in-rural-new-mexico-desert-oracle-calls-water-usage-negligible-for-11-million-gallon-one-time-fill",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T10:00:00+00:00",
    "summary": "Oracle's Project Jupiter is targeting a New Mexico desert already struggling with water consumption, but the company assures residents that the data center's water usage is \"negligible.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/software/operating-systems/reddit-user-gets-valves-amd-first-gaming-os-running-on-intel-hardware-steamos-boots-on-intel-arc-b580-desktop-gpu-but-it-takes-a-radeon-card-installer-workaround-and-resizable-bar-fix",
    "domain": "AI 算力 / 半导体",
    "title": "Enthusiast hacks Valve’s AMD-first gaming OS to run on Intel hardware — SteamOS boots on Intel Arc B580 desktop GPU, but it takes a Radeon card, installer workaround, and Resizable BAR fix",
    "url": "https://www.tomshardware.com/software/operating-systems/reddit-user-gets-valves-amd-first-gaming-os-running-on-intel-hardware-steamos-boots-on-intel-arc-b580-desktop-gpu-but-it-takes-a-radeon-card-installer-workaround-and-resizable-bar-fix",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T09:30:00+00:00",
    "summary": "A Reddit user has shown SteamOS running on an Intel Arc B580 desktop GPU, but the early proof of concept required a Radeon-assisted install workaround and Resizable BAR to recover performance."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-takes-over-mext-to-address-growing-memory-constraints-in-the-data-center-memory-tiering-technology-enables-flash-to-appear-as-dram-to-applications",
    "domain": "AI 算力 / 半导体",
    "title": "AMD takes over MEXT for memory tiering tech that enables flash to appear as DRAM to applications — tech to 'address growing memory constraints' in the data center",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-takes-over-mext-to-address-growing-memory-constraints-in-the-data-center-memory-tiering-technology-enables-flash-to-appear-as-dram-to-applications",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T19:00:47+00:00",
    "summary": "AMD acquires MEXT to get Predictive Memory Engine that offloads infrequently accessed data from DRAM to NAND storage."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/multiple-small-tennessee-counties-pass-temporary-data-center-bans-nashville-also-passed-near-unanimous-moratorium-on-first-reading",
    "domain": "AI 算力 / 半导体",
    "title": "Multiple small Tennessee counties pass temporary data center bans — Nashville also passed near-unanimous moratorium on first reading",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/multiple-small-tennessee-counties-pass-temporary-data-center-bans-nashville-also-passed-near-unanimous-moratorium-on-first-reading",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T18:06:33+00:00",
    "summary": "Two jurisdictions in Tennessee just passed a data center moratorium as three more a set to vote on bills that delay these projects. These temporary bans have gained widespread support, especially in r"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/marvell-details-vision-of-optically-interconnected-data-centers-spanning-across-thousands-of-kilometers-new-interconnects-sampling-later-this-year-would-allow-csps-to-pool-resources-based-on-workload",
    "domain": "AI 算力 / 半导体",
    "title": "Marvell details vision of optically-interconnected data centers spanning across thousands of kilometers — new interconnects sampling later this year would allow CSPs to pool resources based on workloa",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/marvell-details-vision-of-optically-interconnected-data-centers-spanning-across-thousands-of-kilometers-new-interconnects-sampling-later-this-year-would-allow-csps-to-pool-resources-based-on-workload",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T16:49:39+00:00",
    "summary": "Marvell shares its vision for optically connected data centers, connecting devices across hundreds of kilometers, and the company already has hardware to build them."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/chinas-top-court-bars-infineon-from-selling-gan-power-chips-in-china",
    "domain": "AI 算力 / 半导体",
    "title": "China's supreme court bans Infineon from selling GaN power chips in China — market-leader Innoscience secures major victory in multi-region patent war",
    "url": "https://www.tomshardware.com/tech-industry/chinas-top-court-bars-infineon-from-selling-gan-power-chips-in-china",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T14:27:11+00:00",
    "summary": "China's Supreme People's Court on Friday upheld an injunction prohibiting Infineon from selling disputed GaN products in mainland China."
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
    "id": "rss:https://www.theverge.com/gadgets/950958/calvin-and-hobbes-fathers-day-gift-idea-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The Complete Calvin and Hobbes is a great last-minute Father’s Day gift",
    "url": "https://www.theverge.com/gadgets/950958/calvin-and-hobbes-fathers-day-gift-idea-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T20:00:00+00:00",
    "summary": "Father’s Day is nearly here. Hopefully, you already got a gift for dads you care about, but if not, here’s a quick, easy recommendation for anyone who enjoys a good comic strip. The Complete Calvin an"
  },
  {
    "id": "rss:https://www.theverge.com/tech/950936/google-android-17-wear-os-android-xr",
    "domain": "大厂 AI 动态",
    "title": "All the latest news on Android 17, Wear OS 7, and Android XR",
    "url": "https://www.theverge.com/tech/950936/google-android-17-wear-os-android-xr",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T18:30:00+00:00",
    "summary": "Google’s Android 17 update includes highlights like new floating “Bubble” app windows for easier multitasking, a Screen Reaction recording mode, and a 50/50 split gaming mode for foldable phones. Mean"
  },
  {
    "id": "rss:https://www.theverge.com/tech/950651/android-17-release-pixel-drop-google-bubble-screen-reaction",
    "domain": "大厂 AI 动态",
    "title": "Android 17 arrives on Pixel phones today",
    "url": "https://www.theverge.com/tech/950651/android-17-release-pixel-drop-google-bubble-screen-reaction",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T18:00:00+00:00",
    "summary": "Following its official debut last month, Google is now rolling out Android 17 to compatible Pixel phones, alongside additional exclusive features as part of the June Pixel Drop. Not every feature anno"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/950671/wear-os-7-pixel-watches-launch",
    "domain": "大厂 AI 动态",
    "title": "Google launches Wear OS 7 with Live Updates and a battery life boost",
    "url": "https://www.theverge.com/gadgets/950671/wear-os-7-pixel-watches-launch",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T18:00:00+00:00",
    "summary": "Google's Wear OS 7 update is starting to roll out today for the Pixel Watch 2, 3, and 4, adding a new Live Updates feature that tracks live events from your Android smartwatch. Live Updates will now s"
  },
  {
    "id": "rss:https://www.theverge.com/tech/950881/verizon-simplicity-plan-launch",
    "domain": "大厂 AI 动态",
    "title": "Verizon&#8217;s &#8216;Simplicity&#8217; flat-rate plan starts at $30 per month for new customers",
    "url": "https://www.theverge.com/tech/950881/verizon-simplicity-plan-launch",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T17:19:35+00:00",
    "summary": "Verizon is launching a new Simplicity plan that starts at $30 / month for new customers, or $45 / month for existing ones. In its announcement, Verizon says the plan drops activation and upgrade fees,"
  },
  {
    "id": "rss:https://www.theverge.com/tech/950826/apple-airpod-camera-ai-foldable-iphone-rumor",
    "domain": "大厂 AI 动态",
    "title": "Apple 2027 rumors: AirPods with cameras for AI and the second folding iPhone",
    "url": "https://www.theverge.com/tech/950826/apple-airpod-camera-ai-foldable-iphone-rumor",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T17:04:05+00:00",
    "summary": "Now that we're clear of WWDC and all of the new AI-powered features coming to Apple's platforms, Bloomberg reporter Mark Gurman has more details about rumored new hardware, like the camera-equipped Ai"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/950229/qualcomm-snapdragon-reality-elite-xr-smart-glasses-wearables",
    "domain": "大厂 AI 动态",
    "title": "Qualcomm’s latest chip hints that more powerful smart glasses could be on the way",
    "url": "https://www.theverge.com/gadgets/950229/qualcomm-snapdragon-reality-elite-xr-smart-glasses-wearables",
    "source": "Victoria Song",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T17:00:00+00:00",
    "summary": "Smart glasses are still a nascent category, but chipmaker Qualcomm is hard at work upgrading the silicon to power the next wave of XR devices: the Snapdragon Reality Elite. Although Qualcomm is announ"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/950597/xreal-google-aura-xr-glasses-deposit-scheme",
    "domain": "大厂 AI 动态",
    "title": "The Google / Xreal Aura XR glasses are now available to preorder",
    "url": "https://www.theverge.com/gadgets/950597/xreal-google-aura-xr-glasses-deposit-scheme",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T17:00:00+00:00",
    "summary": "The Project Aura glasses collaboration between Xreal and Google is now one step closer to being something you can buy. Reservations for the second Android XR device, now dubbed the Xreal Aura, are ava"
  },
  {
    "id": "rss:https://www.theverge.com/tech/950492/snap-specs-ar-glasses-launch-date-preorder",
    "domain": "大厂 AI 动态",
    "title": "Snap is finally about to ship AR glasses — and they cost a fortune",
    "url": "https://www.theverge.com/tech/950492/snap-specs-ar-glasses-launch-date-preorder",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T16:50:00+00:00",
    "summary": "Snap is finally launching augmented glasses for the public. Specs, which Snap describes as \"a wearable computer built into see-through augmented reality glasses,\" will cost $2,195. You can preorder a "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/945942/prime-day-2026-frequently-asked-questions",
    "domain": "大厂 AI 动态",
    "title": "Everything you need to know about Prime Day 2026",
    "url": "https://www.theverge.com/gadgets/945942/prime-day-2026-frequently-asked-questions",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T16:31:40+00:00",
    "summary": "Amazon Prime Day 2026 is getting closer, and it’s possible you might have some questions about the sale. When does it start? Why is it in June instead of July? And, most importantly, when will the dea"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/anthropics-latest-feud-with-the-trump-admin-may-actually-help-it-sales-data-suggests/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s latest feud with the Trump admin may actually help it, sales data suggests",
    "url": "https://techcrunch.com/2026/06/16/anthropics-latest-feud-with-the-trump-admin-may-actually-help-it-sales-data-suggests/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T22:34:17+00:00",
    "summary": "Anthropic's popularity with business users is growing so well that the latest beef with the government might actually boost it, data from Ramp suggests."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/apple-plans-to-change-its-hide-my-email-privacy-feature-that-could-make-it-less-effective/",
    "domain": "大厂 AI 动态",
    "title": "Apple plans to change its Hide My Email privacy feature that could make it less effective",
    "url": "https://techcrunch.com/2026/06/16/apple-plans-to-change-its-hide-my-email-privacy-feature-that-could-make-it-less-effective/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T22:09:32+00:00",
    "summary": "In the coming weeks, Apple will move anonymously generated emails addresses to a different domain."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/spacex-valuation-balloons-to-2-6t-briefly-passes-amazon/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX valuation balloons to $2.6T, briefly passes Amazon",
    "url": "https://techcrunch.com/2026/06/16/spacex-valuation-balloons-to-2-6t-briefly-passes-amazon/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T20:11:00+00:00",
    "summary": "SpaceX's valuation has increased by $1 trillion since its shares started trading on Friday."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/qualcomm-wants-to-be-the-chip-inside-whatever-replaces-your-smartphone-and-it-just-announced-two-products-toward-that-end/",
    "domain": "大厂 AI 动态",
    "title": "Qualcomm wants to be the chip inside whatever replaces your smartphone, and it just announced two products toward that end",
    "url": "https://techcrunch.com/2026/06/16/qualcomm-wants-to-be-the-chip-inside-whatever-replaces-your-smartphone-and-it-just-announced-two-products-toward-that-end/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T18:22:24+00:00",
    "summary": "Qualcomm CEO Cristiano Amon said Tuesday that the company is working on over 40 different AI wearable devices — including jewelry, earbuds with cameras, pins, and watches — a sign of how aggressively "
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/bug-in-fifa-world-cup-internal-system-gave-anyone-ability-to-modify-tv-stream/",
    "domain": "大厂 AI 动态",
    "title": "Bug in FIFA World Cup internal system gave anyone ability to modify TV stream",
    "url": "https://techcrunch.com/2026/06/16/bug-in-fifa-world-cup-internal-system-gave-anyone-ability-to-modify-tv-stream/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T18:13:49+00:00",
    "summary": "A security researcher said a flaw in FIFA’s online platforms allowed her to access several internal systems, including one that could have allowed her to take control of the TV stream of every World C"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/android-17-launches-with-new-multitasking-tools-as-google-expands-gemini-features/",
    "domain": "大厂 AI 动态",
    "title": "Android 17 launches with new multitasking tools as Google expands Gemini features",
    "url": "https://techcrunch.com/2026/06/16/android-17-launches-with-new-multitasking-tools-as-google-expands-gemini-features/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T18:00:00+00:00",
    "summary": "Google has released Android 17 and Wear OS 7, introducing new multitasking features, parental controls, security tools, and smartwatch upgrades. The launch is also accompanied by a Pixel Drop that bri"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/mobileye-us-robotaxi-launch-will-put-it-on-both-sides-of-the-av-business/",
    "domain": "大厂 AI 动态",
    "title": "Mobileye’s US robotaxi launch will put it on both sides of the AV business",
    "url": "https://techcrunch.com/2026/06/16/mobileye-us-robotaxi-launch-will-put-it-on-both-sides-of-the-av-business/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T17:50:23+00:00",
    "summary": "Mobileye apparently wants to own some of the robotaxi market, even if that puts it in direct competition with companies it supplies its self-driving system to."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/rivian-cuts-hundreds-of-workers-after-r2-deliveries-start/",
    "domain": "大厂 AI 动态",
    "title": "Rivian cuts hundreds of workers after R2 deliveries start",
    "url": "https://techcrunch.com/2026/06/16/rivian-cuts-hundreds-of-workers-after-r2-deliveries-start/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T17:48:20+00:00",
    "summary": "The company said the cuts were part of a restructuring meant to help scale to profitability. Rivian recently pushed back its profitability goal to invest in autonomy."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/snap-finally-debuts-its-long-awaited-ar-glasses-specs-and-oof-they-arent-cheap/",
    "domain": "大厂 AI 动态",
    "title": "Snap finally debuts its long-awaited AR glasses, Specs, and, oof, they aren’t cheap",
    "url": "https://techcrunch.com/2026/06/16/snap-finally-debuts-its-long-awaited-ar-glasses-specs-and-oof-they-arent-cheap/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T17:00:00+00:00",
    "summary": "For over a decade now, Snap has been working on this device. Now the glasses are finally here. So what stands out on first impression?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/sixty-percent-of-u-s-consumers-say-ai-in-brand-messaging-is-a-turnoff-survey-finds/",
    "domain": "大厂 AI 动态",
    "title": "Sixty percent of US consumers say ‘AI’ in brand messaging is a turnoff, survey finds",
    "url": "https://techcrunch.com/2026/06/16/sixty-percent-of-u-s-consumers-say-ai-in-brand-messaging-is-a-turnoff-survey-finds/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T16:49:44+00:00",
    "summary": "WordPress VIP’s latest survey suggests consumers are wary of AI-generated answers even as companies increasingly view AI search as an important referral channel."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/spacex-is-public-everything-you-need-to-know-post-ipo/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX is public: Everything you need to know post-IPO",
    "url": "https://techcrunch.com/2026/06/16/spacex-is-public-everything-you-need-to-know-post-ipo/",
    "source": "Kirsten Korosec, Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T15:53:12+00:00",
    "summary": "TechCrunch has followed SpaceX's start, struggles, and successes from the early days. And we're here for what happens next too. This package of SpaceX IPO coverage includes who stands to win (and mayb"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/india-temporarily-blocks-access-to-telegram-over-exam-fraud-concerns/",
    "domain": "大厂 AI 动态",
    "title": "India orders temporary ban on Telegram over exam fraud concerns",
    "url": "https://techcrunch.com/2026/06/16/india-temporarily-blocks-access-to-telegram-over-exam-fraud-concerns/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T15:49:00+00:00",
    "summary": "The restrictions include a nationwide ban on Telegram until June 22 and a requirement to disable the app's message-editing feature."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/payments-startup-flutterwave-hits-3-2b-valuation-backed-by-ripple/",
    "domain": "大厂 AI 动态",
    "title": "Payments startup Flutterwave hits $3.2B valuation, backed by Ripple",
    "url": "https://techcrunch.com/2026/06/16/payments-startup-flutterwave-hits-3-2b-valuation-backed-by-ripple/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T15:35:39+00:00",
    "summary": "African payments infrastructure company Flutterwave has hit a new valuation and landed blockchain company Ripple as an investor and partner."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/doj-claims-xais-unpermitted-gas-turbines-are-a-matter-of-national-economic-and-energy-security/",
    "domain": "大厂 AI 动态",
    "title": "DOJ claims xAI’s unpermitted gas turbines are a matter of ‘national, economic, and energy security’",
    "url": "https://techcrunch.com/2026/06/16/doj-claims-xais-unpermitted-gas-turbines-are-a-matter-of-national-economic-and-energy-security/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T15:05:03+00:00",
    "summary": "The Justice department says the Pentagon needs xAI to keep using its unpermitted gas turbines."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/plaud-says-its-software-business-topped-100m-in-arr-after-shipping-over-2m-ai-notetakers/",
    "domain": "大厂 AI 动态",
    "title": "Plaud says its software business topped $100M in ARR after shipping over 2M AI notetakers",
    "url": "https://techcrunch.com/2026/06/16/plaud-says-its-software-business-topped-100m-in-arr-after-shipping-over-2m-ai-notetakers/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T15:00:00+00:00",
    "summary": "Plaud is trying to make a mark in a crowded market full of AI-powered meeting notetakers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/robinhoods-note-on-10-layoffs-shows-blaming-ai-isnt-cutting-it/",
    "domain": "大厂 AI 动态",
    "title": "Robinhood’s note on 10% layoffs shows blaming AI isn’t cutting it",
    "url": "https://techcrunch.com/2026/06/16/robinhoods-note-on-10-layoffs-shows-blaming-ai-isnt-cutting-it/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T14:50:09+00:00",
    "summary": "Unlike many of his tech industry peers who have cut thousands of jobs citing the need to restructure to make the most of AI, Robinhood's CEO Vlad Tenev conspicuously made no mention of AI in his note "
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/probably-raises-9m-to-build-a-more-reliable-kind-of-ai/",
    "domain": "大厂 AI 动态",
    "title": "Probably raises $9M to build a more reliable kind of AI",
    "url": "https://techcrunch.com/2026/06/16/probably-raises-9m-to-build-a-more-reliable-kind-of-ai/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T13:15:09+00:00",
    "summary": "Probably wants to prevent hallucinations and factual errors from reaching users, and achieve accuracy on par with deterministic systems."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/this-startups-super-metals-could-soon-be-in-military-drones-luxury-watches-and-chefs-knives/",
    "domain": "大厂 AI 动态",
    "title": "This startup’s super metals could soon be in military drones, luxury watches, and chef’s knives",
    "url": "https://techcrunch.com/2026/06/16/this-startups-super-metals-could-soon-be-in-military-drones-luxury-watches-and-chefs-knives/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T11:25:00+00:00",
    "summary": "Instead of heating metals, Foundation Alloy beats them into submission. The startup has raised $22 million to scale up production of its alloys."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX to acquire Cursor for $60B in stock, days after blockbuster IPO",
    "url": "https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T11:21:41+00:00",
    "summary": "The deal is supposed to help SpaceX's struggling AI division. The company told IPO investors it sees a $26 trillion addressable market in AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/16/threads-adds-new-personalization-and-community-features-as-it-reaches-500m-monthly-users/",
    "domain": "大厂 AI 动态",
    "title": "Threads adds new personalization and community features as it reaches 500M monthly users",
    "url": "https://techcrunch.com/2026/06/16/threads-adds-new-personalization-and-community-features-as-it-reaches-500m-monthly-users/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T11:00:00+00:00",
    "summary": "The Meta-owned social platform announced a series of new features launching today, including a \"Your Algo\" tool that lets users control what they see in their feeds."
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
    "id": "rss:https://stratechery.com/2026/anthropics-safety-superpower/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s Safety Superpower",
    "url": "https://stratechery.com/2026/anthropics-safety-superpower/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T10:00:00+00:00",
    "summary": "Anthropic's belief in its own commitment to safety gives the company license to aggressively favor its business and even challenge the U.S. government."
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
    "id": "rss:https://arstechnica.com/ai/2026/06/anthropic-pauses-token-based-billing-for-its-claude-agent-sdk/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic \"pauses\" token-based billing for its Claude Agent SDK",
    "url": "https://arstechnica.com/ai/2026/06/anthropic-pauses-token-based-billing-for-its-claude-agent-sdk/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T21:00:35+00:00",
    "summary": "Move originally planned for Monday would have heavily increased power users' costs."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/us-approval-of-paramount-warner-bros-deal-surprised-doj-lawyers-report-says/",
    "domain": "大厂 AI 动态",
    "title": "US approval of Paramount/Warner Bros. deal surprised DOJ lawyers, report says",
    "url": "https://arstechnica.com/tech-policy/2026/06/us-approval-of-paramount-warner-bros-deal-surprised-doj-lawyers-report-says/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T18:48:45+00:00",
    "summary": "Trump admin green-lighting $111B deal \"reeks of corruption,\" Sen. Warren says."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/pentagon-boasts-of-using-ai-to-write-reports-mandated-by-congress/",
    "domain": "大厂 AI 动态",
    "title": "Pentagon boasts of using AI to write reports mandated by Congress",
    "url": "https://arstechnica.com/ai/2026/06/pentagon-boasts-of-using-ai-to-write-reports-mandated-by-congress/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T18:11:05+00:00",
    "summary": "Pentagon also claims 1.5 million personnel are using generative AI tools."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/android-17-starts-hitting-pixel-phones-and-watches-today/",
    "domain": "大厂 AI 动态",
    "title": "Android 17 starts hitting Pixel phones and watches today",
    "url": "https://arstechnica.com/gadgets/2026/06/android-17-starts-hitting-pixel-phones-and-watches-today/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T18:00:08+00:00",
    "summary": "Pixels will get their OTA in the coming weeks, but don't expect monumental changes."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/trump-admin-abandons-fight-against-wind-energy-as-clean-energy-output-surges/",
    "domain": "大厂 AI 动态",
    "title": "Trump admin abandons fight against wind energy as clean energy output surges",
    "url": "https://arstechnica.com/science/2026/06/trump-admin-abandons-fight-against-wind-energy-as-clean-energy-output-surges/",
    "source": "Aman Azhar, Inside Climate News",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T16:49:09+00:00",
    "summary": "Legal victories have dampened the Trump admin’s efforts to halt wind and solar power."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/spacex-will-acquire-coding-tool-cursor-to-compete-with-anthropic-openai/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX to acquire AI coding platform Cursor for $60 billion",
    "url": "https://arstechnica.com/ai/2026/06/spacex-will-acquire-coding-tool-cursor-to-compete-with-anthropic-openai/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T16:37:45+00:00",
    "summary": "Separately, neither could compete. Now they hope they can."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/leaked-financial-docs-show-openai-is-losing-billions-of-dollars-a-year/",
    "domain": "大厂 AI 动态",
    "title": "Leaked financial docs show OpenAI is losing billions of dollars a year",
    "url": "https://arstechnica.com/ai/2026/06/leaked-financial-docs-show-openai-is-losing-billions-of-dollars-a-year/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T16:18:07+00:00",
    "summary": "Audited accounting shows growing revenues being dwarfed by R&#038;D, other expenses."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/06/mobileye-is-entering-the-us-robotaxi-market-with-standalone-service/",
    "domain": "大厂 AI 动态",
    "title": "Mobileye is entering the US robotaxi market with standalone service",
    "url": "https://arstechnica.com/cars/2026/06/mobileye-is-entering-the-us-robotaxi-market-with-standalone-service/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T14:20:51+00:00",
    "summary": "The service will leverage its Moovit platform to launch in an a US city in 2027."
  },
  {
    "id": "rss:https://arstechnica.com/staff/2026/06/the-ars-technica-2026-reader-survey-let-your-voice-be-heard/",
    "domain": "大厂 AI 动态",
    "title": "The Ars Technica 2026 Reader Survey: Let your voice be heard!",
    "url": "https://arstechnica.com/staff/2026/06/the-ars-technica-2026-reader-survey-let-your-voice-be-heard/",
    "source": "Ken Fisher",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T13:35:55+00:00",
    "summary": "Tell us how you read Ars, and what you'd like to see more (or less!) of on the front page."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/06/critical-copilot-vulnerability-allowed-hackers-to-seal-2fa-code-from-users/",
    "domain": "大厂 AI 动态",
    "title": "Critical Copilot vulnerability allowed hackers to steal 2FA code from users",
    "url": "https://arstechnica.com/security/2026/06/critical-copilot-vulnerability-allowed-hackers-to-seal-2fa-code-from-users/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T11:15:46+00:00",
    "summary": "SearchLeak exploit shows why the industry's approach to LLM security fails over and over."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/commodores-newest-gadget-is-a-flip-phone-that-blocks-social-media-and-browsers/",
    "domain": "大厂 AI 动态",
    "title": "Commodore’s newest gadget is a flip phone that blocks social media and browsers",
    "url": "https://arstechnica.com/gadgets/2026/06/commodores-newest-gadget-is-a-flip-phone-that-blocks-social-media-and-browsers/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-16T09:00:51+00:00",
    "summary": "Commodore's Callback 8020 is a phone “where the customer is not the product.\""
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/key-mission-for-europes-commercial-space-enterprise-scrubbed-again/",
    "domain": "大厂 AI 动态",
    "title": "Key mission for Europe's commercial space enterprise scrubbed again",
    "url": "https://arstechnica.com/space/2026/06/key-mission-for-europes-commercial-space-enterprise-scrubbed-again/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T23:40:38+00:00",
    "summary": "Isar Aerospace is not hurting for money, but it is sorely lacking in the currency of flight experience."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/06/covid-vaccines-still-protect-against-heart-problems-large-study-finds/",
    "domain": "大厂 AI 动态",
    "title": "Heart protection from COVID shots remains amid updates, study finds",
    "url": "https://arstechnica.com/health/2026/06/covid-vaccines-still-protect-against-heart-problems-large-study-finds/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T21:04:26+00:00",
    "summary": "Despite continued benefits, anti-vaccine rhetoric has driven down vaccination."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/uk-to-ban-social-media-for-kids-under-16-may-impose-overnight-curfews/",
    "domain": "大厂 AI 动态",
    "title": "UK to ban social media for kids under 16, may impose overnight curfews",
    "url": "https://arstechnica.com/tech-policy/2026/06/uk-to-ban-social-media-for-kids-under-16-may-impose-overnight-curfews/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-15T20:14:04+00:00",
    "summary": "Critics say bans push kids to riskier alternatives and can be beaten with VPNs."
  },
  {
    "id": "wscn:3774898",
    "domain": "股票",
    "title": "英伟达B200租赁价被曝将翻倍，GPU采购新订单排到明年Q2",
    "url": "https://wallstreetcn.com/articles/3774898",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T08:31:47+00:00",
    "summary": "AI推理基础设施服务商Baseten首席执行官透露，其云服务商已通知，英伟达B200 GPU租赁价格将于10月续约时上涨约94%，同时采购1000块GPU的交付周期已长达12至15个月。交付瓶颈与租赁涨价叠加，AI推理的算力成本正遭受系统性抬升。"
  },
  {
    "id": "wscn:3774861",
    "domain": "股票",
    "title": "午后拉升！科创50暴涨超4%，AI硬件、芯片半导体大爆发，联讯仪器、兆易创新创新高，港股AI大模型股大涨",
    "url": "https://wallstreetcn.com/articles/3774861",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T08:26:57+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市超3700股飘绿，今日成交3.11万亿。沪深两市成交额3.09万亿，较上一个交易日放量近300亿。板块方面，基板概念股掀涨停潮；半导体产业链盘中崛起，多股创历史新高；中字头股午后异动拉升。AI应用、大消费、文化传媒、煤炭、油气、汽车板块跌幅靠前。"
  },
  {
    "id": "wscn:3774890",
    "domain": "股票",
    "title": "人形机器人价格为什么能“打下来”？",
    "url": "https://wallstreetcn.com/articles/3774890",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T08:20:27+00:00",
    "summary": "核心原因有三：零部件国产化（谐波减速器从万元降至千元级）、供应链密度优势（长三角三小时高铁圈内集聚全产业链，协作摩擦成本极低）、标准化规模效应（零部件从定制件变标准品，累计产量每翻番成本降15%-20%）。预计2027-2028年，机器人售价将跌破工人年薪，触发制造业替代临界点。"
  },
  {
    "id": "wscn:3774891",
    "domain": "股票",
    "title": "SpaceX引爆韩国散户热情，上市首日就买入8亿美元",
    "url": "https://wallstreetcn.com/articles/3774891",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T08:11:02+00:00",
    "summary": "韩国1400万散户在SpaceX上市首日单日净买入高达7.96亿美元，一举超越过去三个月任何美股的累计净买入总量。此前被拒于IPO门外的压抑需求，在二级市场集中爆发——这场\"补仓狂潮\"背后，是韩国散户对马斯克资产长达数年的执念，以及全球投资者对这家市值2.65万亿美元巨头的疯狂追逐。"
  },
  {
    "id": "wscn:3774896",
    "domain": "股票",
    "title": "调用量上涨  腾讯Buddy家族要重新定价了",
    "url": "https://wallstreetcn.com/articles/3774896",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T07:54:24+00:00",
    "summary": "构建可持续收费体系"
  },
  {
    "id": "wscn:3774895",
    "domain": "股票",
    "title": "特朗普：要不是我，以色列早没了",
    "url": "https://wallstreetcn.com/articles/3774895",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T07:50:23+00:00",
    "summary": "美国总统特朗普16日在法国埃维昂莱班出席七国集团峰会期间“敲打”以色列，称如果没有美国和他本人的干预，以色列“早就被炸毁了”。他还批评以色列打击黎巴嫩真主党“时间太长”且导致“太多人丧生”。"
  },
  {
    "id": "wscn:3774795",
    "domain": "股票",
    "title": "半导体出口206%！AI周期金丝雀再鸣：韩国出口为何持续爆发？",
    "url": "https://wallstreetcn.com/premium/articles/3774795?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T07:50:06+00:00",
    "summary": "韩国半导体出口暴增206%，验证AI算力投资仍在加速兑现，但需警惕未来技术迭代与产能扩张带来的周期波动风险。"
  },
  {
    "id": "wscn:3774889",
    "domain": "股票",
    "title": "General Atlantic押注中国AI视频，洽谈领投快手可灵逾20亿美元融资",
    "url": "https://wallstreetcn.com/articles/3774889",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T07:39:58+00:00",
    "summary": "美国私募巨头General Atlantic正洽谈领投快手旗下可灵AI，目标融资逾20亿美元、估值约180亿美元。可灵AI一季度营收超6.5亿元，同比暴增逾300%；随着OpenAI关闭Sora，国际资本正将目光投向这匹中国AI视频黑马。"
  },
  {
    "id": "wscn:3774893",
    "domain": "股票",
    "title": "黄仁勋得州铲土，Coherent光芯片工厂动工",
    "url": "https://wallstreetcn.com/articles/3774893",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T07:38:42+00:00",
    "summary": "当576块GPU跨越八个机架协同运算，铜缆已触及物理极限——光互联正成为AI扩张不可绕过的硬件命题。6月16日，黄仁勋亲赴德克萨斯州为Coherent扩建厂房破土，背后是英伟达20亿美元投资的首个落地节点。全球首条6英寸磷化铟量产线即将提速，算力竞赛的胜负或将在这条\"光的走廊\"里分晓。"
  },
  {
    "id": "wscn:3774886",
    "domain": "股票",
    "title": "今夜全球瞩目，沃什“美联储首秀”会向市场扔炸弹吗？",
    "url": "https://wallstreetcn.com/articles/3774886",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T07:14:35+00:00",
    "summary": "沃什执掌美联储后首次议息会议即将揭晓：利率按兵不动几无悬念，但宽松偏向措辞料将退场、通胀预测面临大幅上调、点阵图初现加息预期——真正的悬念，全压在沃什新闻发布会的每一句措辞上。"
  },
  {
    "id": "wscn:3774884",
    "domain": "股票",
    "title": "美国股债相关性跌至30年低点，瑞银警告：下一轮冲击可能来自利率市场",
    "url": "https://wallstreetcn.com/articles/3774884",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T06:55:28+00:00",
    "summary": "瑞银最新报告揭示，美国股债相关性跌至近30年最低，债券对冲功能正在失效。这一结构性转变可能触发股债协同去杠杆的自我强化风险。与此同时，利率波动率相对股票波动率仍处低位，但转折点或已临近。标普500已充分定价温和收益率上行情景，区域银行等周期板块却仍被低估，机会窗口正在打开。"
  },
  {
    "id": "wscn:3774887",
    "domain": "股票",
    "title": "市场静待沃什首秀，亚太股市收涨，SK海力士再创新高，油价跌入三月低位，债市上扬",
    "url": "https://wallstreetcn.com/articles/3774887",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T06:55:13+00:00",
    "summary": "布伦特原油跌破每桶79美元，四个交易日内累计下跌15%，创逾三个月新低。市场押注美伊协议将重开霍尔木兹海峡，供应大幅释放的预期拖累油价，并推动债券收益率下行。韩国首尔综指收涨1.6%，报8864.24点。SK海力士收涨近6%续创新高。标普500期货上涨0.2%，此前半导体股回调令美国股市周二走弱。"
  },
  {
    "id": "wscn:3774885",
    "domain": "股票",
    "title": "新工具来了！境外央行类机构回购工具到底是啥？",
    "url": "https://wallstreetcn.com/articles/3774885",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T06:54:51+00:00",
    "summary": "该工具是央行向境外央行、国际金融组织及主权财富基金提供短期人民币流动性的机制。机构可通过质押或买断国债等高等级债券，获取7天至3个月资金。此举旨在便利境外机构管理流动性、盘活债券存量，增强其长期持有人民币资产的动力，推动我国金融高水平对外开放。"
  },
  {
    "id": "wscn:3774882",
    "domain": "股票",
    "title": "韩国央行警告：AI芯片公司巨额奖金可能蔓延至全行业，加剧通胀压力",
    "url": "https://wallstreetcn.com/articles/3774882",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T06:22:56+00:00",
    "summary": "韩国央行报告称，三星、SK海力士等芯片巨头发放的巨额奖金，可能引发跨行业薪资竞争与消费扩张，导致薪资压力蔓延至全行业。叠加中东局势引发的能源冲击，韩国5月CPI同比涨3.1%创两年新高。央行行长警示通胀存在\"自我强化\"风险，并罕见强硬表态将在\"为时已晚之前\"启动加息。"
  },
  {
    "id": "wscn:3774883",
    "domain": "股票",
    "title": "美股“七巨头”过时了？华尔街抢推MANGOS ETF",
    "url": "https://wallstreetcn.com/articles/3774883",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T06:22:43+00:00",
    "summary": "从FAANG到\"七巨头\"，华尔街的科技股命名游戏再度升级，\"MANGOS\"横空出世，将Meta、Nvidia、Alphabet、SpaceX与尚未上市的OpenAI、Anthropic打包成新概念，多家ETF发行商已抢先提交申请。但分析人士直指：把几家连交易所都没进的私人公司与超大规模科技巨头捆绑兜售，更像营销噱头而非投资逻辑。"
  },
  {
    "id": "wscn:3774877",
    "domain": "股票",
    "title": "“美国例外论”交易强势回归：美元多头创六年最大增幅",
    "url": "https://wallstreetcn.com/articles/3774877",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T06:20:40+00:00",
    "summary": "全球资金正掀起新一轮\"美国例外论\"行情，CFTC数据显示美元多头头寸创2018年以来最大单周增幅，年初降息共识瓦解。非农数据强劲、核心通胀上行、美联储鹰派预期升温，叠加AI热潮与SpaceX IPO引发外资\"虹吸\"，美元强势已从避险逻辑切换为基本面驱动，全球投资者正用真金白银重注美元资产。"
  },
  {
    "id": "wscn:3774865",
    "domain": "股票",
    "title": "潘功胜陆家嘴论坛讲话：完善短端利率调控机制，创设境外央行回购工具",
    "url": "https://wallstreetcn.com/articles/3774865",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T06:18:12+00:00",
    "summary": "17日陆家嘴论坛上，央行行长潘功胜宣布多项重磅举措：授权六大银行在上海自贸区开展离岸人民币外汇交易试点；创设境外央行回购工具，允许境外官方机构以国债质押获取人民币流动性；研究设立非银流动性支持宏观审慎工具，应对债市极端系统性压力；完善短端利率调控机制，将利率走廊区间由70个基点收窄至50个基点。"
  },
  {
    "id": "wscn:3774872",
    "domain": "股票",
    "title": "互动测试丨投资管理职业方向测评（附CFA®考试2027年教材更新详解）",
    "url": "https://wallstreetcn.com/articles/3774872",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T06:13:12+00:00",
    "summary": "CFA®（特许金融分析师）考试可以帮助你通往金融与投资管理相关的多种职业方向。\n2025年，CFA三..."
  },
  {
    "id": "wscn:3774881",
    "domain": "股票",
    "title": "丁向群陆家嘴论坛讲话：健全具有硬约束的金融风险早期纠正机制",
    "url": "https://wallstreetcn.com/articles/3774881",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T06:04:35+00:00",
    "summary": "丁向群表示，将加快推动银监法、保险法修订出台；支持新型金融业务在上海先行先试；联合出台加快上海国际再保险中心建设若干举措；设立“金监工程”数智监管（上海）研发基地；严厉打击金融“黑灰产”，坚定不移推行保险业“报行合一”等。"
  },
  {
    "id": "wscn:3774875",
    "domain": "股票",
    "title": "釜底抽薪！对工会妥协奖金之后，三星押注2030年实现AI无人工厂",
    "url": "https://wallstreetcn.com/articles/3774875",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T05:57:43+00:00",
    "summary": "一场耗资巨大的罢工危机，正在倒逼三星发动一场更深远的反击。三星推出数据共享平台DSEP并引入AI工厂操作系统，剑指2030年半导体产线完全无人化——这不仅是效率革命，更是管理层向工会夺回谈判筹码的战略布局，其成本结构重塑或将深刻改写全球存储芯片的供给逻辑。"
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
    "id": "rss:https://arxiv.org/abs/2606.17065",
    "domain": "金融",
    "title": "PIVOT: Bridging Black-Scholes Implied-Volatility and Price Objectives via Differentiable J\\\"ackel Operator",
    "url": "https://arxiv.org/abs/2606.17065",
    "source": "Raeid Saqur, Yannick Limmer, Anastasis Kratsios, Blanka Horvath, Hans Buehler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2606.17065v1 Announce Type: new Abstract: Modern option-learning systems operate in two coordinates: price space, where markets quote and no-arbitrage constraints are most naturally enforced, an"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.17079",
    "domain": "金融",
    "title": "Partial Identification of Spatial Production Networks",
    "url": "https://arxiv.org/abs/2606.17079",
    "source": "Shaowen Luo, Kwok Ping Tsang, Zichao Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2606.17079v1 Announce Type: new Abstract: Which regional exposure conclusions are identified when public data do not observe buyer-seller links across states? We study this question by treating "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.17290",
    "domain": "金融",
    "title": "Competing firms, competing regulators: The strategic cost of fragmented climate policy",
    "url": "https://arxiv.org/abs/2606.17290",
    "source": "Nicole Adler, Gianmarco Andreana, Gerben de Jong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2606.17290v1 Announce Type: new Abstract: Climate policy in global network industries is implemented across fragmented jurisdictions, yet firms respond through integrated operational networks. W"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.17373",
    "domain": "金融",
    "title": "Some General Remarks on Private Property",
    "url": "https://arxiv.org/abs/2606.17373",
    "source": "Adnan N. Alabbar, Walter E. Block",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2606.17373v1 Announce Type: new Abstract: Private Property is one of the central institutions of civilized society. We first consider its social, legal, and economic aspects. We then follow the "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.17383",
    "domain": "金融",
    "title": "Model Validation of Agentic AI Systems: A POMDP-Based Framework for Belief-State, Forecast, and Policy Validation",
    "url": "https://arxiv.org/abs/2606.17383",
    "source": "Matthew Francis Dixon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2606.17383v1 Announce Type: new Abstract: Agentic artificial intelligence systems introduce a new class of model risk. Unlike traditional predictive models, autonomous agents continuously acquir"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.17397",
    "domain": "金融",
    "title": "Designing Recommendation Exposure and Favorite Lists: A Field Experiment in a Spot-Work Platform",
    "url": "https://arxiv.org/abs/2606.17397",
    "source": "Kazuki Sekiya, Suguru Otani, Yuki Komatsu, Shunsuke Ozeki, Shunya Noda",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2606.17397v1 Announce Type: new Abstract: How should recommender systems be designed when recommendations shape access to scarce, short-lived opportunities? We study this question in a productio"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.17423",
    "domain": "金融",
    "title": "Martingale Doppelg\\\"anger-Eval: An Identification Framework for Auditing Candlestick Understanding in Vision-Language Models",
    "url": "https://arxiv.org/abs/2606.17423",
    "source": "Ziyao Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2606.17423v1 Announce Type: new Abstract: We introduce Martingale Doppelg\\\"anger-Eval, a public shadow-market benchmark for auditing whether vision-language models (VLMs) use candlestick evidenc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.17503",
    "domain": "金融",
    "title": "What Prediction Markets Can See: Market Formation, Settlement Legibility, and the Geography of Tradable Uncertainty in Africa and Latin America",
    "url": "https://arxiv.org/abs/2606.17503",
    "source": "Ade Adegbenro",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2606.17503v1 Announce Type: new Abstract: Prediction markets are usually evaluated after their contracts exist, by asking how well prices forecast outcomes. We study the prior institutional marg"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.17807",
    "domain": "金融",
    "title": "Household coping mechanisms under grid failure: Evidence from a high electrification context in Lebanon",
    "url": "https://arxiv.org/abs/2606.17807",
    "source": "Majd Olleik, Haytham M. Dbouk, Anne Neumann, Elsa Bou Gebrael, Sebastian Zwickl-Bernhard",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2606.17807v1 Announce Type: new Abstract: Despite near-universal electrification in many countries, electricity supply shortages continue to shape household energy use. This paper examines how h"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.18087",
    "domain": "金融",
    "title": "Environmental Threat and the Nation: Earthquake Risk, Distributive Priority, and Expressive Attachment",
    "url": "https://arxiv.org/abs/2606.18087",
    "source": "Hector Galindo-Silva",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2606.18087v1 Announce Type: new Abstract: This paper studies how long-run earthquake risk shapes national identity, separating a distributive margin (national membership as a rule for allocating"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.17530",
    "domain": "金融",
    "title": "Public transit gains and spatially uneven travel demand changes after NYC congestion pricing",
    "url": "https://arxiv.org/abs/2606.17530",
    "source": "Donghang Li, Dingyi Zhuang, Yunlin Li, Chenan Shen, Nina Cao, Yunhan Zheng, Shenhao Wang, Jinhua Zhao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2606.17530v1 Announce Type: cross Abstract: New York City implemented the nation's first cordon-based congestion pricing program in January 2025, providing an opportunity to evaluate how system-"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.17545",
    "domain": "金融",
    "title": "Continuous-time Optimal Stopping through Deep Reinforcement Learning",
    "url": "https://arxiv.org/abs/2606.17545",
    "source": "Cosmin Borsa, Michael Ludkovski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2606.17545v1 Announce Type: cross Abstract: Simulation based solvers for optimal stopping problems must discretize the stopping decision. Under classical dynamic programming, a coarse exercise g"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.17965",
    "domain": "金融",
    "title": "Thermodynamic description of wealth inequality in the world",
    "url": "https://arxiv.org/abs/2606.17965",
    "source": "Klaus M. Frahm, Leonardo Ermann, Dima L. Shepelyansky",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2606.17965v1 Announce Type: cross Abstract: According to the recent Wealth Thermalization Hypothesis (WTH) the wealth inequality in the world is described by the Rayleigh-Jeans (RJ) thermal dist"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.18005",
    "domain": "金融",
    "title": "LLM Consumer Behavior Theory: Foundations of a Novel Research Field",
    "url": "https://arxiv.org/abs/2606.18005",
    "source": "Manon Reusens, Sofie Goethals, David Martens",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2606.18005v1 Announce Type: cross Abstract: Large language models (LLMs) are increasingly deployed as autonomous agents that make consumption decisions on behalf of users. This shift raises fund"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.18199",
    "domain": "金融",
    "title": "Conformal Prediction Intervals with Tail-Specific Guarantees",
    "url": "https://arxiv.org/abs/2606.18199",
    "source": "Simone Cuonzo, Nina Deliu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2606.18199v1 Announce Type: cross Abstract: This paper extends classical conformal frameworks for constructing prediction intervals with global marginal coverage $1-\\alpha$ to intervals that pro"
  },
  {
    "id": "rss:https://arxiv.org/abs/2111.14631",
    "domain": "金融",
    "title": "Model Risk in Credit Portfolio Models",
    "url": "https://arxiv.org/abs/2111.14631",
    "source": "Christian Meyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2111.14631v2 Announce Type: replace Abstract: Model risk in credit portfolio models is a serious issue for banks but has so far not been tackled comprehensively. We will demonstrate how to deal "
  },
  {
    "id": "rss:https://arxiv.org/abs/2403.00471",
    "domain": "金融",
    "title": "How much inflation can fiscal policy create? Separating household heterogeneity and liquidity",
    "url": "https://arxiv.org/abs/2403.00471",
    "source": "Matthias H\\\"ansel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2403.00471v3 Announce Type: replace Abstract: A key determinant of monetary-fiscal interactions in Heterogeneous Agent New Keynesian (HANK) models is the liquidity value of public debt and its e"
  },
  {
    "id": "rss:https://arxiv.org/abs/2404.02687",
    "domain": "金融",
    "title": "Dynamic Resource Allocation with Karma: An Experimental Study",
    "url": "https://arxiv.org/abs/2404.02687",
    "source": "Ezzat Elokda, Saverio Bolognani, Florian D\\\"orfler, Heinrich H. Nax",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2404.02687v4 Announce Type: replace Abstract: We perform a behavioral experiment of karma, a class of mechanisms for repeated resource allocation with attractive fairness and efficiency properti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2405.20912",
    "domain": "金融",
    "title": "A Branch-Price-Cut-And-Switch Approach for Optimizing Team Formation and Routing for Airport Baggage Handling Tasks with Stochastic Travel Times",
    "url": "https://arxiv.org/abs/2405.20912",
    "source": "Andreas Hagn, Rainer Kolisch, Giacomo Dall'Olio, Stefan Weltge",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2405.20912v5 Announce Type: replace Abstract: In airport operations, optimally using dedicated personnel for baggage handling tasks plays a crucial role in the design of resource-efficient proce"
  },
  {
    "id": "rss:https://arxiv.org/abs/2501.00826",
    "domain": "金融",
    "title": "LLM-Powered Multi-Agent System for Automated Crypto Portfolio Management",
    "url": "https://arxiv.org/abs/2501.00826",
    "source": "Yichen Luo, Yebo Feng, Jiahua Xu, Paolo Tasca, Yang Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2501.00826v3 Announce Type: replace Abstract: Cryptocurrency portfolio management requires the fusion of heterogeneous multi-modal signals, including structured price and on-chain time series, u"
  },
  {
    "id": "rss:https://arxiv.org/abs/2504.18788",
    "domain": "金融",
    "title": "Elite Formation and Family Structure in Prewar Japan: Evidence from the Personnel Inquiry Records",
    "url": "https://arxiv.org/abs/2504.18788",
    "source": "Hiroshi Kumanomido, Suguru Otani, Yutaro Takayasu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2504.18788v4 Announce Type: replace Abstract: This paper introduces a newly constructed individual-level dataset of prewar Japanese elites using the ``Who's Who'' directories published in 1903--"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.14257",
    "domain": "金融",
    "title": "Mapping the causal structure of price formation in Texas's transitioning electricity market",
    "url": "https://arxiv.org/abs/2604.14257",
    "source": "Shiva Madadkhani, Nils Sturma, Mathias Drton, Svetlana Ikonnikova",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2604.14257v2 Announce Type: replace Abstract: Renewable deployment and rising demand from electrification and large digital loads are transforming electricity markets. However, how these develop"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.12872",
    "domain": "金融",
    "title": "Non-Spanning Identification of Scheduled Event Risk in Option Pricing",
    "url": "https://arxiv.org/abs/2606.12872",
    "source": "Tenghan Zhong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2606.12872v2 Announce Type: replace Abstract: Short-dated index options make scheduled macro-announcement risk visible in market prices, but visibility does not imply identification: a flexible "
  },
  {
    "id": "rss:https://arxiv.org/abs/2412.00607",
    "domain": "金融",
    "title": "On a risk model with tree-structured Poisson Markov random field frequency, with application to rainfall events",
    "url": "https://arxiv.org/abs/2412.00607",
    "source": "H\\'el\\`ene Cossette, Benjamin C\\^ot\\'e, Alexandre Dubeau, Etienne Marceau",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2412.00607v4 Announce Type: replace-cross Abstract: In many insurance contexts, dependence between risks of a portfolio may arise from their frequencies. We investigate a dependent risk model in"
  },
  {
    "id": "rss:https://arxiv.org/abs/2502.17518",
    "domain": "金融",
    "title": "Ensemble RL through Classifier Models: Enhancing Risk-Return Trade-offs in Trading Strategies",
    "url": "https://arxiv.org/abs/2502.17518",
    "source": "Zheli Xiong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2502.17518v3 Announce Type: replace-cross Abstract: This paper presents a comprehensive study on the use of ensemble Reinforcement Learning (RL) models in financial trading strategies, leveragin"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.03767",
    "domain": "金融",
    "title": "Trading Frictions in Dynamic Cap-and-Trade Markets",
    "url": "https://arxiv.org/abs/2606.03767",
    "source": "Nicola Borri, Yukun Liu, Aleh Tsyvinski, Xi Wu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-17T04:00:00+00:00",
    "summary": "arXiv:2606.03767v2 Announce Type: replace-cross Abstract: We develop a dynamic stochastic model of markets with an externality and multiple trading frictions, and cap-and-trade as the leading applicat"
  }
]
```
