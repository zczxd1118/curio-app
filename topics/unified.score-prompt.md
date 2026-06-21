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

- 今日日期：`2026-06-21`
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
  "date": "2026-06-21",
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
    "points": 1204883,
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
    "points": 735916,
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
    "points": 437155,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 414720,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 377850,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 374406,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1VEA8zYE6f",
    "domain": "AI",
    "title": "翻遍整个B站，这绝对是2026讲的最好的提示词工程（Prompt Engineering）教程，全程干货无废话！让你少走99%的弯路！AI大模型|LLM",
    "url": "http://www.bilibili.com/video/av116147491964472",
    "source": "AIAgent开发",
    "platform": "bilibili",
    "points": 201804,
    "published_at": "2026-02-28T09:22:09+00:00",
    "summary": "翻遍整个B站，这绝对是2026讲的最好的提示词工程（Prompt Engineering）教程，全程干货无废话！让你少走99%的弯路！AI大模型|LLM"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 185655,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 174994,
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
    "points": 157108,
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
    "points": 154635,
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
    "points": 143975,
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
    "points": 140285,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "domain": "AI",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 136618,
    "published_at": "2026-01-11T15:43:58+00:00",
    "summary": "🚀开发者必看！Superpowers把专业工程团队方法论固化成Skills，让Claude Code告别越写越乱的困境：规格驱动+代码质量双重保障！AI编程新范式！头脑风暴+计划+执行一条龙自动化\n\n\n🚀🚀🚀 视频简介：\n🎬 本期视频详细演示了开源AI编程工作流系统Superpowers的完整使用方法，并通过开发一款iOS时间线笔记原生应用来实测其效果。\n🔧 核心内容：\nSuperpowers工作"
  },
  {
    "id": "bvid:BV15zjF6eEji",
    "domain": "AI",
    "title": "Codex 开发程序  一次全部讲明白",
    "url": "http://www.bilibili.com/video/av116768399955480",
    "source": "技术胖",
    "platform": "bilibili",
    "points": 105010,
    "published_at": "2026-06-18T01:01:41+00:00",
    "summary": "视频时间戳：\n第一部分：认识 Codex 与环境准备\n01:18 Codex 是什么\n02:16 Codex 生态与多端入口\n02:54 安装 Codex 桌面客户端\n04:28 验证与安装 Codex CLI\n05:54 新建项目与打开第一个项目\n07:19 让 Codex 读懂项目结构\n08:01 安装与初始化 CodeGraph\n第二部分：基础交互与真实开发流程\n09:41 基础交互与真实开"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 93488,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1UWzpBkERN",
    "domain": "AI",
    "title": "Cherry Studio：新版本更新教程！Agent+MCP+全局记忆！手把手教程！",
    "url": "http://www.bilibili.com/video/av115936887578336",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 69505,
    "published_at": "2026-01-22T11:00:00+00:00",
    "summary": "使用下方邀请链接，注册即可获得200万Tokens：\nhttps://console.lanyun.net/#/register?promoterCode=0179\n\nCherry AI官网：https://cherry-ai.com/\nGithub项目页面：https://github.com/CherryHQ/cherry-studio"
  },
  {
    "id": "bvid:BV1wDFszxEGX",
    "domain": "AI",
    "title": "AI 直接操控 UE5.7！AI 读工程+写蓝图+自动实现功能",
    "url": "http://www.bilibili.com/video/av116030487732208",
    "source": "UnrealXu",
    "platform": "bilibili",
    "points": 61155,
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
    "points": 52194,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1p2DyB4Ee3",
    "domain": "AI",
    "title": "Agent记忆框架怎么选？5大Agent Memory项目工程级横向对比，哪一种才是未来Agent记忆的标准答案",
    "url": "http://www.bilibili.com/video/av116386449853382",
    "source": "唐国梁Tommy",
    "platform": "bilibili",
    "points": 47017,
    "published_at": "2026-04-11T14:08:32+00:00",
    "summary": "Agent 为什么总&quot;失忆&quot;？本期系统拆解 5 个最具代表性的开源记忆框架，适合有 Agent开发基础、想搞清楚记忆层该怎么设计的同学，看完可以建立完整的认知框架。                       \n                                  \n 本期内容：                                           "
  },
  {
    "id": "bvid:BV1oXD7BqEqJ",
    "domain": "AI",
    "title": "【AI短剧漫剧Agent工具开源】新版Toonflow 12分钟快速上手",
    "url": "http://www.bilibili.com/video/av116369420982268",
    "source": "ACT丶流星雨",
    "platform": "bilibili",
    "points": 46229,
    "published_at": "2026-04-08T13:58:39+00:00",
    "summary": "一款 AI 短剧漫剧工具，能够利用 AI 技术将小说自动转化为剧本，并结合 AI 生成的图片和视频，实现高效的短剧创作。借助 Toonflow，可以轻松完成从文字到影像的全流程，让短剧制作变得更加智能与便捷。\n开源地址：\n官网：https://toonflow.net\nGithub：https://github.com/HBAI-Ltd/Toonflow-app\nGitee：https://git"
  },
  {
    "id": "bvid:BV15sNiecEZc",
    "domain": "AI",
    "title": "五款AI聚合客户端，这次不用跑来跑去了",
    "url": "http://www.bilibili.com/video/av113983935747114",
    "source": "果核次元",
    "platform": "bilibili",
    "points": 42522,
    "published_at": "2025-02-11T07:01:27+00:00",
    "summary": "全网AI，一网打尽。只要你配置好，直接无敌"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 39120,
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
    "points": 36432,
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
    "points": 27387,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV1RH7C6ZEAg",
    "domain": "AI",
    "title": "这绝对是B站唯一将OpenCode 从入门到精通讲明白的教程，手把手带你从入门到实战使用，保姆级教程，存下吧，比啃书好太多了！",
    "url": "http://www.bilibili.com/video/av116696509582055",
    "source": "码士集团_马小帆",
    "platform": "bilibili",
    "points": 23143,
    "published_at": "2026-06-05T08:30:45+00:00",
    "summary": "这绝对是B站唯一将OpenCode 从入门到精通讲明白的教程，手把手带你从入门到实战使用，保姆级教程，存下吧，比啃书好太多了！\n【视频配套籽料+问题解答】请看”平论区置顶”自取哦！！！\n视频制作不易，如果视频对你有用的话❤请一键三莲【长按点赞】支持一下up哦，拜托，这对我真的很重要！"
  },
  {
    "id": "bvid:BV1tCvPzAETp",
    "domain": "AI",
    "title": "上班族必备：零基础 10 分钟用 Copilot 搭建 AI 代理！",
    "url": "http://www.bilibili.com/video/av115095443148619",
    "source": "李厂长来了",
    "platform": "bilibili",
    "points": 22953,
    "published_at": "2025-08-30T04:00:00+00:00",
    "summary": "本期视频我将告诉你，如何用微软Copilot Studio 来构建自己的 AI 代理——完全不需要编程背景。\n\n我会教给你如何从创建代理、用你的文档训练它，到连接邮件等各种工具，甚至还能设置自动化工作流。\n\n🧰 AI工具:\nCopilot Studio网站：microsoft365.com\nCopilot Studio进阶用法网站：copilotstudio.microsoft.com\n\n📽️ 时"
  },
  {
    "id": "bvid:BV1k1jv6jEBD",
    "domain": "AI",
    "title": "【每日meme】Vibe Coding 篇",
    "url": "http://www.bilibili.com/video/av116774137765772",
    "source": "地球西西弗",
    "platform": "bilibili",
    "points": 22647,
    "published_at": "2026-06-19T01:21:35+00:00",
    "summary": "来源：Reddit r/vibecoding, r/vibecodingmemes"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 18831,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1wuLHzDEGA",
    "domain": "AI",
    "title": "【Godot&amp;Cursor】0.亲测一个月后，我选择Godot+Cursor组合做独立游戏",
    "url": "http://www.bilibili.com/video/av114398869853632",
    "source": "破妄-胖",
    "platform": "bilibili",
    "points": 13688,
    "published_at": "2025-04-25T13:43:22+00:00",
    "summary": "飞书文档：https://sh67ozct1z.feishu.cn/docx/Hn5jd0cE6op1Sux9RrFcl8Npnbd"
  },
  {
    "id": "bvid:BV1uVSUBkEfZ",
    "domain": "AI",
    "title": "Microsoft Copilot完整教程(上) 从入门到Agent 一站式掌握AI办公",
    "url": "http://www.bilibili.com/video/av116351721084069",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 12853,
    "published_at": "2026-04-05T11:00:20+00:00",
    "summary": "2026年最全面的Microsoft Copilot教程上半部分。从Copilot首页入门到Agent深度解析，涵盖搜索、资料库、AI视频生成、Copilot Pages、PowerPoint智能幻灯片等全部功能。由培训了6万人的AI顾问Cherie Brock与Sabrina Ramonov联合讲解。"
  },
  {
    "id": "bvid:BV1cCEi6sEU5",
    "domain": "AI",
    "title": "🦊他能成功吗？Claude Code 接管虚幻引擎5，打造一款游戏 | 带你走完整个流程",
    "url": "http://www.bilibili.com/video/av116731724959171",
    "source": "Apeak_虚幻丰哥",
    "platform": "bilibili",
    "points": 12767,
    "published_at": "2026-06-11T13:41:36+00:00",
    "summary": "Claude Code 接管虚幻引擎5，打造了一款游戏\n下载我的 CLAUDE.md（帮你省 token 的配置）\n链接：https://pan.quark.cn/s/b6e50b4b2535\n提取码：tbaE\nStefan 3D AI ：https://www.youtube.com/watch?v=iRcrZjOt5H8&amp;t=1s\n🔗 完整教程指南和链接：https://www.top"
  },
  {
    "id": "bvid:BV1CbvxBwEah",
    "domain": "AI",
    "title": "真的不用服务器！用Cloudflare Workers+D1轻松搭建网站！",
    "url": "http://www.bilibili.com/video/av115803408045159",
    "source": "软件工程师Tim",
    "platform": "bilibili",
    "points": 12431,
    "published_at": "2025-12-29T14:51:53+00:00",
    "summary": "本期影片分享一下如何利用cloudflare workers搭建网站，并且利用d1免费数据库，实现无服务器的一个带前后端功能的网站。也就是说，即使你没有服务器，也能够搭建一个属于自己的网站。比如我自己搭建的这个案例网站在线留言板。就是完全搭建在cloudflare workers上面的，里面有静态页面 也有动态api接口。都是部署在workers上面的，并且集成了它提供的数据库。\n\n\n#cloud"
  },
  {
    "id": "bvid:BV1qHEQ6RERo",
    "domain": "AI",
    "title": "使用 Rust 开发 AI Agent - 简介",
    "url": "http://www.bilibili.com/video/av116724259232762",
    "source": "软件工艺师",
    "platform": "bilibili",
    "points": 12168,
    "published_at": "2026-06-10T06:00:43+00:00",
    "summary": "使用 Rust 从 0 开始搭建 AI Agent"
  },
  {
    "id": "bvid:BV1rCJdzFEQg",
    "domain": "AI",
    "title": "让AI帮你干活：WindowsMCP安装和使用！",
    "url": "http://www.bilibili.com/video/av115242814212549",
    "source": "磊哥聊AI",
    "platform": "bilibili",
    "points": 12057,
    "published_at": "2025-09-22T00:00:00+00:00",
    "summary": "AI 自动操作你的电脑，解放双手，提升工作效率。"
  },
  {
    "id": "bvid:BV1DktBzLEvb",
    "domain": "AI",
    "title": "AI 服务器爆炸图鉴！了解 AI 服务器/GPU服务器长什么样子！",
    "url": "http://www.bilibili.com/video/av114988018571687",
    "source": "ZOMI酱",
    "platform": "bilibili",
    "points": 11570,
    "published_at": "2025-08-07T14:51:04+00:00",
    "summary": "AI 服务器爆炸图鉴！了解 AI 服务器/GPU服务器长什么样子！"
  },
  {
    "id": "bvid:BV1yT8qzMEbd",
    "domain": "AI",
    "title": "基于SpringAI开发Java版mcp服务",
    "url": "http://www.bilibili.com/video/av114942720148945",
    "source": "程序员Cafe",
    "platform": "bilibili",
    "points": 11454,
    "published_at": "2025-07-30T15:05:27+00:00",
    "summary": "如何用Java开发一个mcp服务？如何把已有的spingboot微服务改造成mcp服务呢？如何在mcp客户端调用mcp服务？\n今天来一个保姆级教学"
  },
  {
    "id": "bvid:BV1ssEE6CEks",
    "domain": "AI",
    "title": "Ai自动画图：CAD建筑平面图测试（CodexGPT5.5）",
    "url": "http://www.bilibili.com/video/av116719259485897",
    "source": "Tutor南洋",
    "platform": "bilibili",
    "points": 10510,
    "published_at": "2026-06-09T08:47:15+00:00",
    "summary": "体验一下ai画图，不过CAD软件基本操作也不能拉下~\nCAD教学基础入门视频合集↓\n传送门：BV1aT4y1B7oY\n整个合集教学的，不要跳着看啊喂！\n看完了那基本就能跟上啦，提问请@我，不然评论太多我是看不到的"
  },
  {
    "id": "bvid:BV1a4G96qEGz",
    "domain": "AI",
    "title": "【全60集】吊打付费！全网最详细的Agent开发零基础全套教程，从入门到实战！手把手教你搭建专属智能体，全程干货无废话，让你少走99%弯路！存下吧，很难找全的！",
    "url": "http://www.bilibili.com/video/av116650657454753",
    "source": "AI-Agent开发",
    "platform": "bilibili",
    "points": 9136,
    "published_at": "2026-05-28T06:04:47+00:00",
    "summary": "【全60集】吊打付费！全网最详细的Agent开发零基础全套教程，从入门到实战！手把手教你搭建专属智能体，全程干货无废话，让你少走99%弯路！存下吧，很难找全的！"
  },
  {
    "id": "bvid:BV1GvmzBUEfj",
    "domain": "AI",
    "title": "【AI杂谈】3 claude code概念讲解与配置",
    "url": "http://www.bilibili.com/video/av115718414668601",
    "source": "左-岚",
    "platform": "bilibili",
    "points": 9092,
    "published_at": "2025-12-14T14:38:05+00:00",
    "summary": "飞书的ai杂谈目录下\nhttps://my.feishu.cn/wiki/space/7600816265116011716\n\n米醋工作室 AI 开发环境配置完整指南https://www.micu.wiki/t/topic/571\nClaude Code 常见问题与故障排查https://www.micu.wiki/t/topic/570\nClaude Code 核心概念详解\nhttps://w"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9057,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "穷在街头无人问lhj",
    "platform": "bilibili",
    "points": 8741,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1ExV16FEGU",
    "domain": "AI",
    "title": "「我看谁不学Coze3.0」扣子3.0多Agent实战｜三种Agent全用上，手把手搭AI内容创作团队",
    "url": "http://www.bilibili.com/video/av116684497094372",
    "source": "麦当mdldm",
    "platform": "bilibili",
    "points": 8635,
    "published_at": "2026-06-03T05:26:12+00:00",
    "summary": "扣子3.0的多Agent协作到底怎么玩？这期从概念到实操全讲透，三种Agent（原生/云端/本地）全部用到，搭一套真实能跑的自媒体内容创作AI团队。\n✅ 看完你能做到：\n搞清楚扣子3.0三种Agent的区别和适用场景\n理解「项目空间」的核心逻辑，不再把它当成多开窗口\n在扣子里创建原生Agent、云端Agent，并接入本地Claude Code\n跑通一个「调研→整理→写入本地文件」的完整多Agent"
  },
  {
    "id": "bvid:BV1Y4Gd6LELX",
    "domain": "AI",
    "title": "极简安装！Claude Code+CC switch 连接 Deepseek",
    "url": "http://www.bilibili.com/video/av116634383550090",
    "source": "水哥澎湃",
    "platform": "bilibili",
    "points": 8380,
    "published_at": "2026-05-25T09:00:14+00:00",
    "summary": "本视频分享Claude Code 极简安装 + 连接 Deepseek的完整方案，解决国内用户使用不稳定、收费高的问题。用 Harness（马鞍缰绳）思路通俗讲解核心价值，让大模型拥有本地执行、记忆、任务编排能力。全程无复杂命令，包含 Claude Code 部署、CC switch 安装、Deepseek API 配置、连接测试，一步到位，新手也能轻松搞定。\n\n\n00:00  1-目标\n00:2"
  },
  {
    "id": "bvid:BV1jsEQ6XEw6",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116724292721480",
    "source": "倒计时19",
    "platform": "bilibili",
    "points": 7680,
    "published_at": "2026-06-10T06:04:26+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1qNS8BNESd",
    "domain": "AI",
    "title": "AI黑客实战：Cloud Code自动化渗透测试Hack the Box",
    "url": "http://www.bilibili.com/video/av115652480209157",
    "source": "黑客酒吧",
    "platform": "bilibili",
    "points": 7583,
    "published_at": "2025-12-03T01:11:01+00:00",
    "summary": "Teja挑战AI极限，用Cloud Code CLI在Hack the Box上实现全自动渗透测试！视频展示如何配置AI代理，一键扫描、漏洞利用、权限提升，并自动生成详细渗透报告。亮点包括MCP集成实战、沙盒环境安全测试，以及AI在网络安全中的颠覆性应用。"
  },
  {
    "id": "bvid:BV1ZnEJ6NEJ6",
    "domain": "AI",
    "title": "pi agent 最佳实践 | Harness Agent 定制全流程实战",
    "url": "http://www.bilibili.com/video/av116703891558374",
    "source": "程序员暮闲",
    "platform": "bilibili",
    "points": 7539,
    "published_at": "2026-06-06T15:45:29+00:00",
    "summary": "本期视频系统演示 pi agent 的安装、模型配置与扩展开发流程，重点讲解如何通过 TypeScript extensions、skills、themes、prompt template和 pi package完成拓展，把 pi agent 打造成适合自己工作流的高度定制化 AI Agent。"
  },
  {
    "id": "bvid:BV1etEQ6DETs",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116724192118321",
    "source": "AI产品经理大模型",
    "platform": "bilibili",
    "points": 7311,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6449,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1jCJs6UECL",
    "domain": "AI",
    "title": "豆包最新推出办公任务模式，你的专属办公Agent 来了！",
    "url": "http://www.bilibili.com/video/av116743888444368",
    "source": "翻奇兽AI",
    "platform": "bilibili",
    "points": 6387,
    "published_at": "2026-06-13T17:11:14+00:00",
    "summary": ""
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
    "id": "rss:https://www.tomshardware.com/pc-components/get-amds-flagship-ryzen-7-9800x3d-with-32gb-of-ddr5-memory-and-an-msi-b850-wi-fi-7-motherboard-at-a-discount-micro-center-bundles-are-now-available-on-amazon",
    "domain": "AI 算力 / 半导体",
    "title": "Get AMD's flagship Ryzen 7 9800X3D with 32GB of DDR5 memory and an MSI B850 Wi-Fi 7 motherboard at a discount — Micro Center bundles are now available on Amazon",
    "url": "https://www.tomshardware.com/pc-components/get-amds-flagship-ryzen-7-9800x3d-with-32gb-of-ddr5-memory-and-an-msi-b850-wi-fi-7-motherboard-at-a-discount-micro-center-bundles-are-now-available-on-amazon",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T17:57:35+00:00",
    "summary": "Micro Center is now selling some of its bundles on Amazon, including this 9800X3D combo that gives you an excellent motherboard and fast RAM without breaking the bank."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/wds-2tb-black-ssd-price-drops-by-nearly-20-percent-ahead-of-prime-day-sale-grab-the-2tb-sn7100-for-usd242-96",
    "domain": "AI 算力 / 半导体",
    "title": "WD's 2TB Black SSD price drops by nearly 20% ahead of Prime Day sale — grab the 2TB SN7100 for $242.96",
    "url": "https://www.tomshardware.com/pc-components/ssds/wds-2tb-black-ssd-price-drops-by-nearly-20-percent-ahead-of-prime-day-sale-grab-the-2tb-sn7100-for-usd242-96",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T16:45:07+00:00",
    "summary": "The WD Black SN7100 stands out for its high-end performance, low operating temperatures, and impressive efficiency. It is one of the few PCIe 4.0 SSDs that can compete with flagship drives while consu"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd300-on-this-1440p-ready-gaming-pc-with-32gb-ddr5-ram-grab-the-asus-rog-gm700-with-amds-ryzen-7-8700f-and-rx-9060-xt-for-just-usd1-199",
    "domain": "AI 算力 / 半导体",
    "title": "Save $300 on this 1440p-ready gaming PC with 32GB DDR5 RAM — grab the Asus ROG GM700 with AMD's Ryzen 7 8700F and RX 9060 XT for just $1,199",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd300-on-this-1440p-ready-gaming-pc-with-32gb-ddr5-ram-grab-the-asus-rog-gm700-with-amds-ryzen-7-8700f-and-rx-9060-xt-for-just-usd1-199",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T15:25:58+00:00",
    "summary": "Asus' ROG GM700 is a great prebuilt, packing powerful components for a solid price without compromising on the details. It just happens to look nice, too, if you're into the gamer aesthetic."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/award-winning-resin-3d-printer-for-beginners-is-36-percent-off-grab-the-anycubic-photon-p1-with-dual-color-material-kit-for-usd619-99",
    "domain": "AI 算力 / 半导体",
    "title": "Award-winning resin 3D printer for beginners is 36% off — grab the Anycubic Photon P1 with dual-color material kit for $619.99",
    "url": "https://www.tomshardware.com/3d-printing/award-winning-resin-3d-printer-for-beginners-is-36-percent-off-grab-the-anycubic-photon-p1-with-dual-color-material-kit-for-usd619-99",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T15:02:44+00:00",
    "summary": "Featuring a precision steel build plate, wireless printing support, and excellent print quality, the Anycubic Photon P1 is now available with a dual-color material kit at its lowest advertised price y"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/china-unifies-tech-sector-to-build-grid-free-orbiting-satellite-ai-data-centers-challenging-elon-musks-spacex-beijings-forced-chip-and-satellite-alliance-announced-a-week-before-musks-ai1-reveal",
    "domain": "AI 算力 / 半导体",
    "title": "China unifies tech sector to build grid-free orbiting satellite AI data centers, challenging Elon Musk's SpaceX — Beijing's forced chip and satellite alliance announced a week before Musk’s AI1 reveal",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/china-unifies-tech-sector-to-build-grid-free-orbiting-satellite-ai-data-centers-challenging-elon-musks-spacex-beijings-forced-chip-and-satellite-alliance-announced-a-week-before-musks-ai1-reveal",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T14:53:42+00:00",
    "summary": "Beijing says the Space Computing Industry Innovation Center will bring together rocket and satellite manufacturers, chip manufacturers, and AI labs to develop a space-based data center system."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/best-uk-amazon-prime-day-tech-deals",
    "domain": "AI 算力 / 半导体",
    "title": "The best UK Amazon Prime Day tech deals 2026 — epic savings on premium gaming PCs and laptops, peripherals, 3D printers at Currys, Argos, Scan and CCL, too",
    "url": "https://www.tomshardware.com/pc-components/best-uk-amazon-prime-day-tech-deals",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T14:06:35+00:00",
    "summary": "The best UK deals on gaming PCs, laptops, tools, and accessories for Amazon Prime Day"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/rare-asml-special-edition-monopoly-board-unearthed-in-social-media-trade-enthusiast-swaps-2007-employee-gift-for-high-na-euv-lego-kit",
    "domain": "AI 算力 / 半导体",
    "title": "Rare ASML Special Edition Monopoly board unearthed in social media trade — enthusiast swaps 2007 employee gift for High-NA EUV Lego kit",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/rare-asml-special-edition-monopoly-board-unearthed-in-social-media-trade-enthusiast-swaps-2007-employee-gift-for-high-na-euv-lego-kit",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T13:49:56+00:00",
    "summary": "We just witnessed a significant semiconductor industry related non-cash trade deal take place on Twitter/X."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/web-app-drives-valves-new-steam-controller-across-the-floor-using-its-rumble-motors",
    "domain": "AI 算力 / 半导体",
    "title": "New web app can make Valve's Steam Controller drift across your desk like an RC car — web app drives the gamepad using its rumble motors",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/web-app-drives-valves-new-steam-controller-across-the-floor-using-its-rumble-motors",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T13:37:38+00:00",
    "summary": "A developer has created a Chromium browser-based tool that turns Valve's second-gen Steam Controller into a self-propelled RC car."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/3d-scanning/best-3d-scanners",
    "domain": "AI 算力 / 半导体",
    "title": "The best 3D scanners 2026 — the top performing models we've benchmarked",
    "url": "https://www.tomshardware.com/3d-printing/3d-scanning/best-3d-scanners",
    "source": "Andrew Sink",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T13:17:22+00:00",
    "summary": "We help you find the best 3D scanners for high accuracy, portability, and more."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-and-amds-new-ace-cpu-extensions-bring-an-efficient-ai-oriented-instruction-set-to-x86-a-new-design-makes-matrix-multiplication-more-power-and-density-efficient",
    "domain": "AI 算力 / 半导体",
    "title": "Intel and AMD's new ACE CPU extensions bring an efficient AI-oriented instruction set to x86 — a new design makes matrix multiplication more power- and density-efficient",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-and-amds-new-ace-cpu-extensions-bring-an-efficient-ai-oriented-instruction-set-to-x86-a-new-design-makes-matrix-multiplication-more-power-and-density-efficient",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T12:00:00+00:00",
    "summary": "ACE CPU extensions bring an efficient AI-oriented instruction set to x86 — new design makes matrix multiplication more power- and density-efficient"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/unlucky-pc-builder-sent-rtx-5070-from-amazon-gets-dvd-rewriter-and-a-busted-logic-board-from-an-early-2000s-kenwood-av-receiver-instead-usd700-gpu-turns-out-to-be-e-waste-thanks-to-return-scam",
    "domain": "AI 算力 / 半导体",
    "title": "Unlucky PC builder sent RTX 5070 from Amazon, gets DVD rewriter and a busted logic board from an early 2000's Kenwood AV receiver instead — $700 GPU turns out to be e-waste thanks to return scam",
    "url": "https://www.tomshardware.com/pc-components/gpus/unlucky-pc-builder-sent-rtx-5070-from-amazon-gets-dvd-rewriter-and-a-busted-logic-board-from-an-early-2000s-kenwood-av-receiver-instead-usd700-gpu-turns-out-to-be-e-waste-thanks-to-return-scam",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T11:30:00+00:00",
    "summary": "Another person has fallen victim to Amazon's generous return policy, as they received a disc drive, a mousepad, and an AV receiver instead of the $700 RTX 5070 they ordered."
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/researcher-turns-wi-fi-smart-lightbulb-into-a-banned-book-library-open-source-project-makes-digital-books-available-via-a-server-and-open-wi-fi-access-point-hacked-into-an-esp32-powered-bulb",
    "domain": "AI 算力 / 半导体",
    "title": "Researcher turns wi-fi smart lightbulb into a Banned Book Library — open source project makes digital books available via a server and open Wi-Fi access point hacked into an ESP32-powered bulb",
    "url": "https://www.tomshardware.com/maker-stem/researcher-turns-wi-fi-smart-lightbulb-into-a-banned-book-library-open-source-project-makes-digital-books-available-via-a-server-and-open-wi-fi-access-point-hacked-into-an-esp32-powered-bulb",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T11:00:00+00:00",
    "summary": "A security researcher has added another dimension to smart lightbulbs by stealthily adding what they call a 'cyberpunk digital dead drop' full of 'banned books.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/china-shows-off-a-backpack-sized-anti-drone-laser-that-one-soldier-can-carry",
    "domain": "AI 算力 / 半导体",
    "title": "China unveils man-portable anti-drone laser that can burn through a drone 1,600 feet away in four seconds — backpack-sized 2-kilowatt weapon uses AI for targeting, weighs 55 pounds, and can be carried",
    "url": "https://www.tomshardware.com/tech-industry/china-shows-off-a-backpack-sized-anti-drone-laser-that-one-soldier-can-carry",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T10:30:00+00:00",
    "summary": "Chinese defense supplier Harbin Xinguang Optic-Electronics Technology demo’d two man-portable anti-drone lasers at a Beijing arms expo this week."
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
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/953183/the-atlantic-searchable-database-music-ai-training-data",
    "domain": "大厂 AI 动态",
    "title": "The Atlantic created a searchable database of the music used to train AI",
    "url": "https://www.theverge.com/ai-artificial-intelligence/953183/the-atlantic-searchable-database-music-ai-training-data",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T18:46:48+00:00",
    "summary": "Atlantic reporter Alex Reisner recently uncovered four datasets of music being used to train AI models and made them fully searchable for the public. Two of the sets are absolutely enormous at 12 mill"
  },
  {
    "id": "rss:https://www.theverge.com/report/953116/experimental-musician-youtuber-hainbach-interview",
    "domain": "大厂 AI 动态",
    "title": "Musician and YouTuber Hainbach on ‘Breath of the Wild’ and Swiss Army Knives",
    "url": "https://www.theverge.com/report/953116/experimental-musician-youtuber-hainbach-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T15:20:00+00:00",
    "summary": "Stefan Paul Goetsch, better known as Hainbach, is a German experimental composer, artist, and YouTuber who is perhaps most famous for making music with laboratory equipment and scientific instruments."
  },
  {
    "id": "rss:https://www.theverge.com/games/949875/moves-of-the-diamond-hand-rpg-dice-jazz-noir",
    "domain": "大厂 AI 动态",
    "title": "Moves of the Diamond Hand is an unfinished, irresistibly weird dice-based RPG",
    "url": "https://www.theverge.com/games/949875/moves-of-the-diamond-hand-rpg-dice-jazz-noir",
    "source": "Adi Robertson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T14:00:00+00:00",
    "summary": "From its opening minutes, Moves of the Diamond Hand is upfront about what it offers: You're going to have a lot of strange conversations, and you're going to roll a lot of dice. Get on board with this"
  },
  {
    "id": "rss:https://www.theverge.com/tech/952547/toy-story-5-tech-android-17-snap-specs-installer",
    "domain": "大厂 AI 动态",
    "title": "Toy Story has the right take on tech",
    "url": "https://www.theverge.com/tech/952547/toy-story-5-tech-android-17-snap-specs-installer",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T12:00:00+00:00",
    "summary": "Hi, friends! Welcome to Installer No. 133, your guide to the best and Verge-iest stuff in the world. (If you're new here, welcome, happy belated Juneteenth, and also you can read all the old editions "
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
    "id": "rss:https://techcrunch.com/2026/06/20/signals-meredith-whittaker-wants-you-to-remember-that-ai-chatbots-are-not-your-friends/",
    "domain": "大厂 AI 动态",
    "title": "Signal’s Meredith Whittaker wants you to remember that AI chatbots ‘are not your friends’",
    "url": "https://techcrunch.com/2026/06/20/signals-meredith-whittaker-wants-you-to-remember-that-ai-chatbots-are-not-your-friends/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T20:32:29+00:00",
    "summary": "\"These are not your friends. These are not conscious beings. These are not sentient interlocutors.”"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/20/in-the-weights-is-your-new-ai-centric-vanity-search/",
    "domain": "大厂 AI 动态",
    "title": "In the Weights is your new AI-centric vanity search",
    "url": "https://techcrunch.com/2026/06/20/in-the-weights-is-your-new-ai-centric-vanity-search/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T19:41:11+00:00",
    "summary": "So ... what's your In the Weights score?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/20/founders-funds-outlier-bet-on-humanely-killed-fish/",
    "domain": "大厂 AI 动态",
    "title": "Founders Fund’s outlier bet on humanely killed fish",
    "url": "https://techcrunch.com/2026/06/20/founders-funds-outlier-bet-on-humanely-killed-fish/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T18:26:02+00:00",
    "summary": "Shinkei makes a refrigerator-sized robot called Poseidon to kill fish quickly and humanely."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/20/nobel-laureate-john-jumper-is-leaving-deepmind-for-rival-anthropic/",
    "domain": "大厂 AI 动态",
    "title": "Nobel laureate John Jumper is leaving DeepMind for rival Anthropic",
    "url": "https://techcrunch.com/2026/06/20/nobel-laureate-john-jumper-is-leaving-deepmind-for-rival-anthropic/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T16:39:57+00:00",
    "summary": "Jumper isn't the only big name leaving Google DeepMind."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/20/every-new-ios-27-feature-thats-worth-knowing-about/",
    "domain": "大厂 AI 动态",
    "title": "Every new iOS 27 feature that’s worth knowing about",
    "url": "https://techcrunch.com/2026/06/20/every-new-ios-27-feature-thats-worth-knowing-about/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T15:00:00+00:00",
    "summary": "While it's not flashy like Apple’s new Siri AI and Apple Intelligence upgrades, there are still a number of additions to iOS 27 worth looking at."
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
    "title": "Go eyes robotaxis and acquisitions after Japan’s biggest IPO of 2026 — here’s why it matters",
    "url": "https://techcrunch.com/2026/06/19/go-eyes-robotaxis-and-acquisitions-after-japans-biggest-ipo-of-2026-heres-why-it-matters/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T21:45:00+00:00",
    "summary": "Go's IPO — Japan's biggest so far this year — has done more than provide a much-needed boost to the country's languishing listing season. It has also supplied the taxi-hailing app with the capital req"
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
    "summary": "All of Aura's frames connect to the Aura app, which is where you can upload photos from your phone, web, email, iCloud, or Google Photos."
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
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/the-uk-will-scan-asylum-seekers-faces-for-age-checks-despite-knowing-the-tech-is-flawed/",
    "domain": "大厂 AI 动态",
    "title": "The UK will scan asylum-seekers’ faces for age checks—despite knowing the tech is flawed",
    "url": "https://arstechnica.com/tech-policy/2026/06/the-uk-will-scan-asylum-seekers-faces-for-age-checks-despite-knowing-the-tech-is-flawed/",
    "source": "Matt Burgess, Maddy Varner, May Bulman, Gabriel Geiger, WIRED.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T11:15:09+00:00",
    "summary": "Tests of age-verification technology show the risks of life-altering errors."
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
    "id": "rss:https://www.producthunt.com/products/poolside",
    "domain": "大厂 AI 动态",
    "title": "Laguna by Poolside",
    "url": "https://www.producthunt.com/products/poolside",
    "source": "fmerian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T15:00:44+00:00",
    "summary": "Foundation models for agentic coding and long-horizon work Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/agent-37-38",
    "domain": "大厂 AI 动态",
    "title": "Agent 37",
    "url": "https://www.producthunt.com/products/agent-37-38",
    "source": "fmerian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T19:03:23+00:00",
    "summary": "Give every customer their own Hermes or OpenClaw agent Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/oioi",
    "domain": "大厂 AI 动态",
    "title": "oioi",
    "url": "https://www.producthunt.com/products/oioi",
    "source": "Vishesh Yadav",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T15:05:27+00:00",
    "summary": "a fast, glassy clipboard manager for macOS, Windows & Linux Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/cloudback",
    "domain": "大厂 AI 动态",
    "title": "Cloudback MCP Server",
    "url": "https://www.producthunt.com/products/cloudback",
    "source": "Evgeniy Kosjakov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T20:46:39+00:00",
    "summary": "Manage your backups from Claude, Cursor, and VS Code Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/notchkin",
    "domain": "大厂 AI 动态",
    "title": "Notchkin",
    "url": "https://www.producthunt.com/products/notchkin",
    "source": "Danny Stankowski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T23:28:02+00:00",
    "summary": "A notes app that lives in your MacBook's notch. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/pixlie",
    "domain": "大厂 AI 动态",
    "title": "Pixlie",
    "url": "https://www.producthunt.com/products/pixlie",
    "source": "Illia Ovcharenko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T11:37:24+00:00",
    "summary": "AI video studio: text & image to video, with real control Discussion | Link"
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
    "id": "rss:https://www.producthunt.com/products/gitsync-for-macos",
    "domain": "大厂 AI 动态",
    "title": "GitSync for macOS",
    "url": "https://www.producthunt.com/products/gitsync-for-macos",
    "source": "Kevin Tobler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T21:52:21+00:00",
    "summary": "Visual GitHub management directly from a graphical interface Discussion | Link"
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
    "id": "rss:https://36kr.com/p/3859926114161665?f=rss",
    "domain": "大厂 AI 动态",
    "title": "硬氪首发|moody前高管搭档大疆骨干入局陪伴机器人，锦秋领投，融资数千万",
    "url": "https://36kr.com/p/3859926114161665?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T10:01:25+00:00",
    "summary": "硬氪获悉，AI-Native科技潮玩品牌ZuzuZoos查无此园（杭州多蓝艾梦智能科技旗下）近日完成数千万元Pre-A轮融资，锦秋领投、上海复容跟投。此次融资将主要AI大模型迭代、硬件产品扩建、IP生态深化、全球市场拓展、核心团队扩容。 ZuzuZoos成立于2025年，聚焦“AI陪伴机器人+AI潮玩”。创始人董晓楠是前摩根士丹利投资银行分析师，曾任新消费独角兽企业moody事业部总经理，任职期间"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3862642781230339?f=rss",
    "domain": "大厂 AI 动态",
    "title": "德美化工：下属公司拟750万美元出售境外三处土地资产",
    "url": "https://36kr.com/newsflashes/3862642781230339?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T08:03:25+00:00",
    "summary": "36氪获悉，德美化工公告，公司控股子公司施华特秘鲁公司下属公司Silvateam ICA S.A.C.拟将其持有的三处土地（含土地上的建筑物、水井及其他附属设施）出售给Uvica S.A.C.，交易价格共计750万美元。此次资产出售目的是盘活公司资产，提高资产运营效率。经初步测算，交易完成后，预计增加归属于上市公司股东的净利润约95.3万美元。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3862617771283463?f=rss",
    "domain": "大厂 AI 动态",
    "title": "公募REITs上市满五周年，共上市86只REITs募资2450亿元",
    "url": "https://36kr.com/newsflashes/3862617771283463?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T07:37:59+00:00",
    "summary": "6月21日，公募REITs上市满五周年。截至目前，全市场已上市86只REITs，总募集规模2450亿元，其中上交所59只合计募资1760亿元。随着首批商业不动产REITs的正式落地，形成了涵盖高速公路、产业园区、能源、保租房及商业不动产等多元业态的资产格局。扩募方面，截至2026年6月，沪市共有14单项目进入实质性扩募阶段，其中8单已完成上市、5单发布扩募公告，扩募资产呈现跨类型、跨区域创新特点，"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3862597400859913?f=rss",
    "domain": "大厂 AI 动态",
    "title": "巴林国家银行正与巴林、科威特相关银行洽谈潜在合并事宜",
    "url": "https://36kr.com/newsflashes/3862597400859913?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T07:17:15+00:00",
    "summary": "巴林国家银行正与巴林、科威特相关银行洽谈潜在合并事宜。（新浪财经）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3862514491003912?f=rss",
    "domain": "大厂 AI 动态",
    "title": "高盛大砍黄金目标价，长期多头转趋谨慎",
    "url": "https://36kr.com/newsflashes/3862514491003912?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T06:45:52+00:00",
    "summary": "高盛日前将2026年年终黄金价格预测下调了500美元/盎司，因美联储今年料不会再降息。该行分析师表示，将12月黄金目标价下调至4900美元/盎司。这意味着金价今年下半年仍有望上涨，但涨幅将小于此前的预期。近年来，这家华尔街巨头一直是黄金市场最坚定、最高调的看多声音之一。此次下调黄金目标价，标志着该行基调出现了轻微转变。（财联社）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3862499085686025?f=rss",
    "domain": "大厂 AI 动态",
    "title": "印度谋求在美印贸易协定中获取竞争优势",
    "url": "https://36kr.com/newsflashes/3862499085686025?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T06:24:12+00:00",
    "summary": "媒体援引印度一名联邦部长的消息称，在取得相较于其他国家的竞争优势前，印度不太可能落实拟议中的美印贸易协定。报道称，印度工商部长于周六新闻发布会上表示：“目前悬而未决的核心问题是，我方关税水平必须低于其他竞争国家。”（新浪财经）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3862494481880322?f=rss",
    "domain": "大厂 AI 动态",
    "title": "比特币ETF 30天净流出63.5亿美元，创历史新高",
    "url": "https://36kr.com/newsflashes/3862494481880322?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T06:00:33+00:00",
    "summary": "Galaxy Research披露，比特币ETF在过去30天内净流出资金达63.5亿美元，创下历史新高，在所有582个30天窗口期内排名第一。（界面）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3862484158731266?f=rss",
    "domain": "大厂 AI 动态",
    "title": "德意志银行上调美国通胀预期",
    "url": "https://36kr.com/newsflashes/3862484158731266?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T05:41:41+00:00",
    "summary": "德意志银行上调美国通胀预期，全面修正美联储政策判断，预计2026年美联储合计加息50个基点、利率升至4.1%，7月或提前加息。（新华财经）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3862439214322691?f=rss",
    "domain": "大厂 AI 动态",
    "title": "SpaceX上市前被MSCI打最低ESG评级",
    "url": "https://36kr.com/newsflashes/3862439214322691?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T05:25:20+00:00",
    "summary": "据报道，指数提供商MSCI在SpaceX本月进行创纪录的750亿美元公开募股之前，授予了其最低级别的环境、社会和治理（ESG）评级“CCC”。根据MSCI的说法，这使得SpaceX“因其高风险敞口及未能管理重大ESG风险而落后于行业”。EDHEC商学院气候研究所的项目主任Frédéric Ducoulombier表示：“该公司不佳的争议评估、极差的治理评估和较低的总体ESG评级不应让任何人感到意外"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3862458180359424?f=rss",
    "domain": "大厂 AI 动态",
    "title": "微信AI助手“小微”小范围灰度上线",
    "url": "https://36kr.com/newsflashes/3862458180359424?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T05:03:37+00:00",
    "summary": "微信AI已小范围灰度上线。部分网友微信主界面左上角已出现小眼睛式样图标，该图标即为AI助手“小微”测试版入口。据腾讯客服介绍，微信小微是微信团队在小范围内测的原生AI助手，小微支持通过文字或语音对话操作微信原生功能、调起小程序等，例如帮助好友发送消息、查询朋友圈、预约服务等。（财联社）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3862422164935689?f=rss",
    "domain": "大厂 AI 动态",
    "title": "广西南宁：新能源智能船舶完成试航",
    "url": "https://36kr.com/newsflashes/3862422164935689?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T05:00:52+00:00",
    "summary": "6月20日，中技船舶首批9艘新能源船舶集中试航仪式在广西南宁港举行。9艘船舶包含无人驾驶智慧船、商用作业船、民用休闲船，适配执法巡逻、景区观光等各类场景，助力内河航运绿色转型。（新华社）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3862419587781894?f=rss",
    "domain": "大厂 AI 动态",
    "title": "AI投资热潮向上游扩散，美股多家半导体设备龙头今年翻倍",
    "url": "https://36kr.com/newsflashes/3862419587781894?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T04:38:21+00:00",
    "summary": "回顾年初至今的美股市场，不仅半导体、光通信等AI硬件板块集体狂飙，产业链上游的半导体设备赛道亦同步走出亮眼升势。据统计，美股总市值超百亿美元的9家半导体设备公司，今年以来股价涨幅均已超过75%。其中，应用材料、拉姆研究、科磊、泰瑞达、MKS Inc、英特格、Onto Innovation Inc这7只个股年内股价实现翻倍。就产业逻辑而言，种种迹象表明，半导体设备正迎来机构所谓的“卖方市场”。（财联"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3862376847709189?f=rss",
    "domain": "大厂 AI 动态",
    "title": "富国银行：预测标普500指数到2027年底将升至8600-8800点",
    "url": "https://36kr.com/newsflashes/3862376847709189?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T04:18:52+00:00",
    "summary": "富国银行表示，极度看好后市，预测标普500指数到2027年底将升至8600-8800点。（财联社）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3862375326176262?f=rss",
    "domain": "大厂 AI 动态",
    "title": "科技赋能，全国夏播粮食进度近七成",
    "url": "https://36kr.com/newsflashes/3862375326176262?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T03:59:19+00:00",
    "summary": "农业农村部最新农情调度显示，目前全国夏播粮食进度近七成。今年，粮食主产区大力推广种肥同播技术，有效提升种植质量。（央视新闻）"
  },
  {
    "id": "wscn:3775127",
    "domain": "股票",
    "title": "港股，是人民币和美元的实时记分板",
    "url": "https://wallstreetcn.com/articles/3775127",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T07:15:30+00:00",
    "summary": "上海陆家嘴与华盛顿美联储同步亮相——潘功胜密集释放政策信号，科创50单日飙涨4.69%；沃什用史上最短130字声明宣告鹰派首秀，美股三大指数集体跳水。一边主动管理预期，一边刻意撤回信号；一边为AI企业开辟融资通道，一边追问AI是否重写货币规则。港股，正是这场货币信心博弈的实时记分板。"
  },
  {
    "id": "wscn:3775124",
    "domain": "股票",
    "title": "数字经济时代，三驾马车已经失真",
    "url": "https://wallstreetcn.com/articles/3775124",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T06:01:40+00:00",
    "summary": "国金证券认为数字经济时代，传统\"三驾马车\"分析框架正因统计口径局限而日益失真。中国5月固投、社零双双转负，但工业与服务业生产逆势走高，GDP增速稳健。根源在于社零遗漏服务消费，固投未含无形资产投资——而后者恰是AI时代高速增长的核心引擎。"
  },
  {
    "id": "wscn:3774396",
    "domain": "股票",
    "title": "资金撤退，基本面却在好转，银行板块的叙事能否由“防御”走向“修复”？",
    "url": "https://wallstreetcn.com/premium/articles/3774396?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T05:43:42+00:00",
    "summary": "高股息筑底，优质区域行掘金。"
  },
  {
    "id": "wscn:3775123",
    "domain": "股票",
    "title": "市场“不可调和的矛盾”：如何给科技股估值",
    "url": "https://wallstreetcn.com/articles/3775123",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T04:09:15+00:00",
    "summary": "广发证券认为，科技股估值定价无绝对标准，核心取决于投资期限与方法论。景气投资者应淡化静态估值，重视景气边际变化；价值投资者则需严守估值纪律，等待均值回归。当前科技与传统行业估值分化达历史峰值，但历史显示，有产业趋势支撑时，极致分化可持续近20个月，并非转熊必要条件。"
  },
  {
    "id": "wscn:3775122",
    "domain": "股票",
    "title": "GPT-5.6或将下周问世：从“模型”迈向“可执行Agent”，定价或仅为竞品1/3",
    "url": "https://wallstreetcn.com/articles/3775122",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T04:07:00+00:00",
    "summary": "GPT-5.6据报涵盖mini、标准版及Pro版。该模型上下文窗口扩展至150万tokens，具备视觉复刻、SVG 3D生成及浏览器自动化等Agent能力，词元定价约为Claude的三分之一。OpenAI称其为对GPT-5.5的\"有意义改进\"，但Reddit网友讨论认为，5.6仅为小版本迭代，真正的模型级突破需等待GPT-6。"
  },
  {
    "id": "wscn:3775121",
    "domain": "股票",
    "title": "企业端开始“算力降本”之际，高盛警告5.3万亿AI资本支出正逼近信贷饱和！",
    "url": "https://wallstreetcn.com/articles/3775121",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T02:37:20+00:00",
    "summary": "高盛预测2025至2030年超大规模云企业资本支出将达5.3万亿美元，摩根士丹利估算仅数据中心建设到2028年即需2.9万亿，其中大量依赖债务融资。与此同时，企业端已开始踩刹车，Uber、沃尔玛等纷纷限制AI使用量，计费模式从订阅制转向按词元收费，令成本压力骤然显现。"
  },
  {
    "id": "wscn:3775120",
    "domain": "股票",
    "title": "沃什的野望：五“刀”重构美联储",
    "url": "https://wallstreetcn.com/articles/3775120",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T02:08:28+00:00",
    "summary": "美联储主席沃什在6月FOMC会议上宣布成立五大工作组，开启对货币政策执行机制的系统性改革。五大领域涵盖沟通机制、资产负债表、数据使用、生产率与就业、通胀框架，旨在打破前瞻指引困境、推进资产负债表瘦身、构建实时数据决策体系、评估AI时代生产率影响，并优化通胀衡量指标。"
  },
  {
    "id": "wscn:3775117",
    "domain": "股票",
    "title": "下周重磅日程：“美联储最爱通胀指标”、英伟达股东大会、OpenAI或发新模型、美光财报",
    "url": "https://wallstreetcn.com/articles/3775117",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T02:04:26+00:00",
    "summary": "美国PCE通胀与GDP出炉，若数据偏热将强化美联储鹰派预期。英伟达股东大会聚焦Blackwell与Vera架构产能；美光财报直接检验存储芯片景气度。国内方面，最新LPR、工业企业利润公布；火山引擎原动力大会与上海世界移动通信大会接连召开，豆包大模型或升级。事件方面，OpenAI系列模型GPT 5.6有望登场，SK海力士赴美上市或获批准。此外，美伊谈判需继续关注。"
  },
  {
    "id": "wscn:3775119",
    "domain": "股票",
    "title": "“沃什首秀”是“十年一遇的转折点”？野村：警惕“预防性加息”演变为“实质性紧缩”",
    "url": "https://wallstreetcn.com/articles/3775119",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T01:26:26+00:00",
    "summary": "野村证券首席宏观策略师Matsuzawa指出，市场严重低估美联储长期加息风险。他认为，AI投资扩张与生产率提升将推动经济和通胀超预期，迫使美联储从\"预防性加息\"滑入实质性紧缩周期，届时10年期美债收益率将大幅突破5%。他警告，此次FOMC会议回望或将成为AI繁荣信贷周期终结的历史起点。"
  },
  {
    "id": "wscn:3775090",
    "domain": "股票",
    "title": "德邦基金迎新任董事长尉迟平！",
    "url": "https://wallstreetcn.com/articles/3775090",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T01:04:20+00:00",
    "summary": "6月19日，德邦基金发布变更公告。经股东提名、董事会选举，尉迟平正式出任公司董事长，原代董事长武晓春..."
  },
  {
    "id": "wscn:3775118",
    "domain": "股票",
    "title": "美伊谈判在即，伊朗军方宣布关闭霍尔木兹海峡",
    "url": "https://wallstreetcn.com/articles/3775118",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-21T00:43:39+00:00",
    "summary": "美伊谈判前夕，伊朗宣布关闭霍尔木兹海峡，称因以色列持续袭击黎巴嫩，此举为对\"背信弃义\"行为的回应。与此同时，双方代表团赴瑞士展开技术谈判，伊朗警告若美方未能履行承诺、约束以色列，伊美谅解备忘录将面临破裂风险。"
  },
  {
    "id": "wscn:3774897",
    "domain": "股票",
    "title": "下半年资产配置机会在哪里？听徐小庆、刘晨明展望2026下半年大类资产与A股策略如何布局！",
    "url": "https://wallstreetcn.com/articles/3774897",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T12:18:38+00:00",
    "summary": "6月21日刘晨明主讲Alpha线上闭门私享会：2026下半年A股策略如何布局？哪些资产最值得关注？"
  },
  {
    "id": "wscn:3775114",
    "domain": "股票",
    "title": "AI Agent时代的云基础设施是怎样的？你需要理解“Agent Runtime 完整飞轮”",
    "url": "https://wallstreetcn.com/articles/3775114",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T09:50:21+00:00",
    "summary": "在Nebius Inflection 2026峰会上，公司高管提出AI云基建正面临从“无状态推理”向“Agent Runtime（智能体运行期）”的范式转移，计费模式将由“按Token”转向“按结果”付费。面对Agent循环执行放大错误率及成本失控的痛点，新一代基建需具备多模型路由、持久化执行、结构化数据层、全链路可观测性及严格的安全与成本上限控制。"
  },
  {
    "id": "wscn:3775054",
    "domain": "股票",
    "title": "债市和美联储预期分化了？市场不怕通胀了！",
    "url": "https://wallstreetcn.com/premium/articles/3775054?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T08:23:16+00:00",
    "summary": "因油价暴跌与美联储鹰派转向，盈亏平衡通胀率大幅下行，市场已提前交易通胀回落。"
  },
  {
    "id": "wscn:3775113",
    "domain": "股票",
    "title": "“AI最紧瓶颈”！存储的影响已扩展至宏观经济，加剧整体通胀",
    "url": "https://wallstreetcn.com/articles/3775113",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-20T07:06:28+00:00",
    "summary": "德银认为，AI对高带宽存储（HBM）的结构性需求疯狂挤占传统产能，供给缺口难以在2027年前弥合。存储成本飙升已传导至消费电子、汽车等终端市场，推高整体通胀，美国电子PPI同比涨幅达26.9%，存储危机正从芯片业演变为宏观经济关键变量。"
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
