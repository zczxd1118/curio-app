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

- 今日日期：`2026-06-14`
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
  "date": "2026-06-14",
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
    "points": 3124872,
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
    "points": 1151408,
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
    "points": 1130913,
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
    "points": 1099090,
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
    "points": 1030088,
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
    "points": 837340,
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
    "points": 676686,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 413924,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 400348,
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
    "points": 297927,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1cpEd66EjT",
    "domain": "AI",
    "title": "Claude Fable 5 首发实测，真是太烧了。。完爆 GPT 5.5！",
    "url": "http://www.bilibili.com/video/av116725718717656",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 268555,
    "published_at": "2026-06-10T12:11:13+00:00",
    "summary": "全球最贵的 AI 模型 Claude Fable 5 来了！这期视频带你看看它到底值不值，用两轮硬核实测对比 Fable 5、Opus 4.8 和 GPT-5.5 的 AI 编程能力。\n开源 AI 编程教程：github.com/liyupi/ai-guide\n编程学习教程+实战项目+简历模板：codefather.cn\n视频先带你了解 Claude Fable 5 的核心更新，包括 Fable "
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 240905,
    "published_at": "2026-04-04T15:19:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 235257,
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
    "points": 233985,
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
    "points": 222820,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "setting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, &quot;value&quot;: &quot;xxxx&"
  },
  {
    "id": "bvid:BV1TZ421b7SD",
    "domain": "AI",
    "title": "Nginx入门必须懂3大功能配置 - Web服务器/反向代理/负载均衡",
    "url": "http://www.bilibili.com/video/av1152360790",
    "source": "技术蛋老师",
    "platform": "bilibili",
    "points": 216559,
    "published_at": "2024-03-29T08:15:00+00:00",
    "summary": "Nginx(&quot;engine x&quot;)是一款是由俄罗斯的程序设计师Igor Sysoev所开发高性能的Web和反向代理服务器。"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 215182,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1h4DkBaEu1",
    "domain": "AI",
    "title": "Claude Code、Codex (ChatGPT)、Cursor该怎么选？Max/Pro/Ultra Plan亲身经验分享",
    "url": "http://www.bilibili.com/video/av116385829095069",
    "source": "HexUp",
    "platform": "bilibili",
    "points": 176677,
    "published_at": "2026-04-11T11:37:54+00:00",
    "summary": "Claude Code、Cursor、ChatGPT——编程 Agent 怎么选？                                     \n                                                                                        \n  我目前同时订阅了 Claude Max、Cursor Ult"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 174328,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1X8oKBLEdj",
    "domain": "AI",
    "title": "一口气学会AI编程！3个月10万字超详细教学！【项目实操】【0基础教学】【自学教程】【AI编程】【vibecoding】",
    "url": "http://www.bilibili.com/video/av116436177523067",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 167972,
    "published_at": "2026-04-21T03:15:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料，领取方式：关注后 私信“ 1 ”就好！\n\n后面还会出【一口气学会AI漫剧 】【一口气学会AI Agent 】等系列！大家可以蹲蹲！"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 155389,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 154010,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 149533,
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
    "points": 142711,
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
    "points": 123164,
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
    "points": 103166,
    "published_at": "2026-06-05T11:05:27+00:00",
    "summary": "Ultracode 功能太好用了，就是Claude Code昨天新出的“超码”功能，如果你Vibe Coding ，那这个技巧一定要掌握。他解决了Claude Code 一次性跑不完大型任务的问题。\n本期视频很长，但看完你的AI Coding能力将超越整个团队。并且把视频内容整理成了文字版，放在评论区，方便你学习使用。视频很干，可以先喝口水润润喉咙。"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 97548,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 65357,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1RAEz6EE98",
    "domain": "AI",
    "title": "为什么Claude Code+DeepSeekV4是最有性价比的个人AI Agent?",
    "url": "http://www.bilibili.com/video/av116732144392386",
    "source": "呱声一片",
    "platform": "bilibili",
    "points": 60285,
    "published_at": "2026-06-11T15:27:06+00:00",
    "summary": "官方文档地址：https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/claude_code"
  },
  {
    "id": "bvid:BV1uTAQznEHa",
    "domain": "AI",
    "title": "MiniMax Agent: 真正全能的智能体工具，一键云部署 OpenClaw + 预置专家模式，告别命令行！",
    "url": "http://www.bilibili.com/video/av116142358135406",
    "source": "杰森的效率工坊",
    "platform": "bilibili",
    "points": 52989,
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
    "points": 51608,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1cEEd6VECg",
    "domain": "AI",
    "title": "太强了！Claude Fable 十二大震撼案例",
    "url": "http://www.bilibili.com/video/av116725769047361",
    "source": "阿朱星际漫步",
    "platform": "bilibili",
    "points": 43627,
    "published_at": "2026-06-10T12:19:30+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1oXD7BqEqJ",
    "domain": "AI",
    "title": "【AI短剧漫剧Agent工具开源】新版Toonflow 12分钟快速上手",
    "url": "http://www.bilibili.com/video/av116369420982268",
    "source": "ACT丶流星雨",
    "platform": "bilibili",
    "points": 42083,
    "published_at": "2026-04-08T13:58:39+00:00",
    "summary": "一款 AI 短剧漫剧工具，能够利用 AI 技术将小说自动转化为剧本，并结合 AI 生成的图片和视频，实现高效的短剧创作。借助 Toonflow，可以轻松完成从文字到影像的全流程，让短剧制作变得更加智能与便捷。\n开源地址：\n官网：https://toonflow.net\nGithub：https://github.com/HBAI-Ltd/Toonflow-app\nGitee：https://git"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "🎉 Cursor 自定义API｜Cursor 自定义模型｜Cursor助手正式发布了！｜免费！",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 37475,
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
    "points": 35516,
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
    "points": 29658,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28613,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1JuEi6mEVv",
    "domain": "AI",
    "title": "国产 Claude Code 又多一个：小米 MiMo Code 上线并开源，还支持无限上下文？",
    "url": "http://www.bilibili.com/video/av116729745251003",
    "source": "廖定强AI笔记",
    "platform": "bilibili",
    "points": 27211,
    "published_at": "2026-06-11T05:13:01+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27206,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV1L4Ek68Exp",
    "domain": "AI",
    "title": "降维打击！让 Fable 5 和 Opus 4.8 同时开发《帝国时代》，这画面我给跪了...",
    "url": "http://www.bilibili.com/video/av116734409313151",
    "source": "AI大航海时代",
    "platform": "bilibili",
    "points": 25150,
    "published_at": "2026-06-12T00:58:01+00:00",
    "summary": "【视频简介】\n【本视频由www.waveshift.net进行配音翻译】这绝对是近期最硬核的 AI 编程测试！我给了 Opus 4.8 和全新旗舰模型 Fable 5 完全相同的 Prompt（提示词），并且定下苛刻的规则：只生成一次，零修改，直接部署上线！\n结果令人震惊，Fable 5 在速度、逻辑梳理和 3D 视觉表现上，对 Opus 4.8 进行了全方位的降维打击。甚至自己做出了带动态光影的"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 22992,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1i95a64Ehe",
    "domain": "AI",
    "title": "在手机上用ClaudeCode自动写代码什么感觉？",
    "url": "http://www.bilibili.com/video/av116577072648018",
    "source": "小五爱玩机",
    "platform": "bilibili",
    "points": 22156,
    "published_at": "2026-05-15T06:04:35+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 21619,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV188UHYkEdg",
    "domain": "AI",
    "title": "Cursor / Windsurf + Android Studio 高效AI编程：零基础也能开发安卓应用",
    "url": "http://www.bilibili.com/video/av113502647750313",
    "source": "kate人不错",
    "platform": "bilibili",
    "points": 21034,
    "published_at": "2024-11-18T07:04:36+00:00",
    "summary": "欢迎关注我的知识星球：https://t.zsxq.com/FF0He\n\n我会分享最新AI资讯、源代码、回答你的提问。\n\n视频亮点：\n\n双工具对比：解析 Cursor 和 Windsurf 各自优势\n实战案例：从五子棋到卡路里计算AI应用的完整开发过程\n专业部署：Android Studio 配置与构建技巧\n\n时间戳：\n\n0:00 - 引言\n\n0:26 - 我开发的应用演示\n\n2:33 - Rea"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 19489,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1XxXpBEEHU",
    "domain": "AI",
    "title": "Claude Code远程开发终极方案！手机改代码+实时预览~【小白教程】",
    "url": "http://www.bilibili.com/video/av116294326230438",
    "source": "爱听书的程序员阿超",
    "platform": "bilibili",
    "points": 18668,
    "published_at": "2026-03-26T12:00:00+00:00",
    "summary": "之前，我一直在研究怎么远程使用 Claude Code 开发项目，并且能实时预览效果。但是一直都没有找到合适的解决方案，要么就是给一个临时公网链接预览，每次都需要再配置，要么就是购买云服务器来配置，都感觉挺麻烦的~\n\n最近，我发现这个蒲公英异地组网的方案，用来做远程开发 Claude Code 项目，感觉非常方便，不仅能修改代码，而且我实时预览的需求也很好的满足了。\n\n这样我随时随地都可以用 AI"
  },
  {
    "id": "bvid:BV1iAEE6ZEDq",
    "domain": "AI",
    "title": "【2026全网最新】2026 全网最优 Claude Code 教程！零基础从入门到精通，AI 编程手把手实战教学",
    "url": "http://www.bilibili.com/video/av116719695697025",
    "source": "阿飞教你学编程",
    "platform": "bilibili",
    "points": 18444,
    "published_at": "2026-06-09T10:40:48+00:00",
    "summary": "视频中的安装文档，整合包，模型，工作流，请查看置顶评论获取。"
  },
  {
    "id": "bvid:BV1RtGU6hEDd",
    "domain": "AI",
    "title": "DeepSeek-Reasonix 【保姆级教程】：专为 DeepSeek 打造的 AI 编程 Agent客户端，长会话成本到底能省多少？",
    "url": "http://www.bilibili.com/video/av116647486556383",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 17577,
    "published_at": "2026-05-27T16:33:52+00:00",
    "summary": "本期体验 DeepSeek-Reasonix 这个开源项目，主要看客户端界面、模型模式、会话导入、MCP 配置、记忆与缓存等功能。内容基于个人使用记录，不做夸张结论，适合对 DeepSeek 生态和 AI 编程工具感兴趣的朋友参考。"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 17215,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1hnjGzLE14",
    "domain": "AI",
    "title": "【小智教程】手挽手教你如何接入别人的MCP服务",
    "url": "http://www.bilibili.com/video/av114568722450105",
    "source": "空白泡泡糖果",
    "platform": "bilibili",
    "points": 17080,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
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
    "id": "hn:48352939",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX Spark",
    "url": "https://www.nvidia.com/en-us/products/rtx-spark/",
    "source": "shenli3514",
    "platform": "hackernews",
    "points": 428,
    "published_at": "2026-06-01T05:24:40+00:00",
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
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/microsofts-bug-hunting-nemesis-extends-vendetta-with-more-zero-day-attacks-nightmare-eclipse-publishes-rogueplanet-and-greatxml-local-privilege-escalation-exploits",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft's bug-hunting nemesis extends vendetta with more zero-day attacks — Nightmare Eclipse publishes RoguePlanet and GreatXML local privilege escalation exploits",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/microsofts-bug-hunting-nemesis-extends-vendetta-with-more-zero-day-attacks-nightmare-eclipse-publishes-rogueplanet-and-greatxml-local-privilege-escalation-exploits",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T14:48:03+00:00",
    "summary": "Nightmare-Eclipse's vendetta against Microsoft and Windows continues apace — researcher publishes RoguePlanet and GreatXML local privilege escalation zero-day exploits"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/various-vendors-add-amd-expo-ultra-low-latency-to-600-series-motherboards-in-latest-bios-updates-tech-tightens-memory-subtimings-on-compatible-kits-boosting-fps-by-up-to-4-percent",
    "domain": "AI 算力 / 半导体",
    "title": "Various vendors add AMD EXPO Ultra-Low Latency to 600-series motherboards in latest BIOS updates — tech tightens memory subtimings on compatible kits, boosting FPS by up to 4%",
    "url": "https://www.tomshardware.com/pc-components/motherboards/various-vendors-add-amd-expo-ultra-low-latency-to-600-series-motherboards-in-latest-bios-updates-tech-tightens-memory-subtimings-on-compatible-kits-boosting-fps-by-up-to-4-percent",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T14:17:36+00:00",
    "summary": "New BIOS updates featuring AMD EXPO Ultra Low Latency support are being released across a plethora of 600-series motherboards by multiple vendors."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/republican-lawmakers-urge-itc-to-block-imports-of-infringing-tsmc-chips-as-patent-ruling-imminent",
    "domain": "AI 算力 / 半导体",
    "title": "Republican lawmakers urge federal agency to block imports of infringing TSMC chips as patent ruling nears — five asserted U.S. patents come from United Microelectronics Corporation",
    "url": "https://www.tomshardware.com/tech-industry/republican-lawmakers-urge-itc-to-block-imports-of-infringing-tsmc-chips-as-patent-ruling-imminent",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T13:29:20+00:00",
    "summary": "Four Republican members of Congress have urged the U.S. ITC to block imports of foreign-made chips found to infringe U.S. patents"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/save-usd300-on-gigabytes-gaming-a16-gaming-laptop-at-walmart-budget-rtx-5060-powered-16-inch-laptop-is-now-only-usd1-199",
    "domain": "AI 算力 / 半导体",
    "title": "Save $300 on Gigabyte's Gaming A16 gaming laptop at Walmart — Budget RTX 5060 -powered 16-inch laptop is now only $1,199",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/save-usd300-on-gigabytes-gaming-a16-gaming-laptop-at-walmart-budget-rtx-5060-powered-16-inch-laptop-is-now-only-usd1-199",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T11:29:07+00:00",
    "summary": "Save $300 on Gigabyte's Gaming A16 gaming laptop at Walmart. Budget RTX 5060 -powered 16-inch laptop is now only $1,199."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-a-massive-usd751-on-this-rtx-5070-ti-gaming-pc-with-a-9800x3d-right-now-liquid-cooled-4k-ready-skytech-rig-with-32gb-ddr5-and-a-2tb-ssd-is-now-just-usd2-249",
    "domain": "AI 算力 / 半导体",
    "title": "Save a massive $751 on this RTX 5070 Ti gaming PC with a 9800X3D right now — liquid-cooled, 4K-ready Skytech rig with 32GB DDR5 and a 2TB SSD is now just $2,249",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-a-massive-usd751-on-this-rtx-5070-ti-gaming-pc-with-a-9800x3d-right-now-liquid-cooled-4k-ready-skytech-rig-with-32gb-ddr5-and-a-2tb-ssd-is-now-just-usd2-249",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T11:15:31+00:00",
    "summary": "Save $750 on this Skytech gaming PC for gaming at 1440p and 4K, featuring a 9800X3D, RTX 5070 Ti, 32GB DDR5, and a 2 TB SSD."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/xbox/xbox-will-pay-five-times-more-for-components-in-2027-than-it-did-two-years-ago-ceo-asha-sharma-admits-theres-an-unsustainable-hardware-gap-that-cannot-continue",
    "domain": "AI 算力 / 半导体",
    "title": "Xbox will pay five times more for memory and storage in 2027 than it did two years ago — CEO Asha Sharma admits there's an unsustainable hardware gap that 'cannot continue'",
    "url": "https://www.tomshardware.com/video-games/xbox/xbox-will-pay-five-times-more-for-components-in-2027-than-it-did-two-years-ago-ceo-asha-sharma-admits-theres-an-unsustainable-hardware-gap-that-cannot-continue",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T11:00:00+00:00",
    "summary": "The next-gen Xbox Helix is looking in trouble due to surging memory and storage costs that are forcing even a giant like Microsoft to bend down."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-32gb-of-ddr5-ram-for-only-usd255-in-this-2-item-combo-from-newegg-just-usd514-99-gets-you-corsair-vengeance-rgb-ram-and-a-gigabyte-x870-aorus-elite-motherboard-26-percent-off",
    "domain": "AI 算力 / 半导体",
    "title": "Get 32GB of DDR5 RAM for only $255 in this 2-item combo from Newegg — just $514.99 gets you Corsair Vengeance RGB RAM and a Gigabyte X870 Aorus Elite motherboard, 26% off",
    "url": "https://www.tomshardware.com/pc-components/get-32gb-of-ddr5-ram-for-only-usd255-in-this-2-item-combo-from-newegg-just-usd514-99-gets-you-corsair-vengeance-rgb-ram-and-a-gigabyte-x870-aorus-elite-motherboard-26-percent-off",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T10:42:16+00:00",
    "summary": "Newegg slashes ~$185 off this 2-item combo, dropping the RAM to an affordable $255 - just $514.99 gets you a solid Gigabyte X870 motherboards, and 32GB of RAM in this incredible Newegg combo deal."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/hades-malware-campaign-now-tricks-ai-bots-by-injecting-text-about-biological-and-nuclear-weapons-failsafe-mechanisms-triggered-by-prompts-for-weapon-creation-stop-scans-before-payload-is-seen",
    "domain": "AI 算力 / 半导体",
    "title": "New malware campaign tricks AI scanners with fake nuclear weapon prompts — malicious code triggers safety failsafes so scanners skip the payload",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/hades-malware-campaign-now-tricks-ai-bots-by-injecting-text-about-biological-and-nuclear-weapons-failsafe-mechanisms-triggered-by-prompts-for-weapon-creation-stop-scans-before-payload-is-seen",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T10:30:00+00:00",
    "summary": "Hades malware campaign now tricks AI bots into not scanning development packages, as prompts for bio- and nuclear weapons trigger failsafe mechanisms."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/amd-denies-researcher-a-usd10-000-bug-bounty-after-fixing-critical-auto-updater-vulnerability-security-flaw-took-124-days-to-patch",
    "domain": "AI 算力 / 半导体",
    "title": "AMD denies researcher a $10,000 bug bounty after fixing critical auto-updater vulnerability — security flaw took 124 days to patch",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/amd-denies-researcher-a-usd10-000-bug-bounty-after-fixing-critical-auto-updater-vulnerability-security-flaw-took-124-days-to-patch",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T10:00:00+00:00",
    "summary": "AMD took over four months to fix a critical security bug in its autoupdater, and the security researcher didn't see a dime for his efforts"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/security-software/several-police-officers-arrested-for-using-controversial-flock-ai-license-plate-reader-system-to-stalk-romantic-partners-says-report-investigators-have-unearthed-at-least-18-such-cases-in-the-us-over-recent-years",
    "domain": "AI 算力 / 半导体",
    "title": "Several police officers arrested for using controversial Flock AI license plate reader system to stalk romantic partners, says report — investigators have unearthed at least 18 such cases in the US ov",
    "url": "https://www.tomshardware.com/software/security-software/several-police-officers-arrested-for-using-controversial-flock-ai-license-plate-reader-system-to-stalk-romantic-partners-says-report-investigators-have-unearthed-at-least-18-such-cases-in-the-us-over-recent-years",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T09:30:00+00:00",
    "summary": "Tens of officers have been fired, and some even arrested, for abuse of the Flock license plate reader system used by police departments throughout the US, according to a new report."
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
    "id": "rss:https://www.eetimes.com/logistics-leaders-navigate-cost-and-automation/",
    "domain": "AI 算力 / 半导体",
    "title": "Logistics Leaders Navigate Cost and Automation",
    "url": "https://www.eetimes.com/logistics-leaders-navigate-cost-and-automation/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T08:11:49+00:00",
    "summary": "Gartner's VP analyst David Gonzalez shares strategies for profitability and technology in supply chain management. The post Logistics Leaders Navigate Cost and Automation appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/startup-ricursive-to-create-an-end-to-end-ai-model-for-chip-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Startup Ricursive to Create an End-to-End AI Model for Chip Design",
    "url": "https://www.eetimes.com/startup-ricursive-to-create-an-end-to-end-ai-model-for-chip-design/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T16:26:51+00:00",
    "summary": "“We are definitely not an EDA company,” Ricursive co-founders told EE Times. The post Startup Ricursive to Create an End-to-End AI Model for Chip Design appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/massive-ai-storage-demand-creates-a-new-memory-wall/",
    "domain": "AI 算力 / 半导体",
    "title": "Massive AI Storage Demand Creates a New Memory Wall",
    "url": "https://www.eetimes.com/massive-ai-storage-demand-creates-a-new-memory-wall/",
    "source": "Alper Ilkbahar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-10T14:22:01+00:00",
    "summary": "As AI models scale to trillions of parameters, conventional memory architectures face mounting capacity and efficiency constraints. The post Massive AI Storage Demand Creates a New Memory Wall appeare"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-bans-china-linked-chatgpt-accounts-that-amplified-us-data-center-electricity-price-backlash",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI bans China-linked ChatGPT accounts that amplified US data center electricity price backlash — used AI-generated cartoons to stoke fears over U.S. data center energy costs",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-bans-china-linked-chatgpt-accounts-that-amplified-us-data-center-electricity-price-backlash",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T18:48:34+00:00",
    "summary": "OpenAI says it has banned two clusters of ChatGPT accounts it believes are operating from China, and that used its models for covert influence campaigns targeting U.S. tech and policy debates."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/memory-famine-compels-gpu-vendors-to-re-release-2020-graphics-cards-geforce-rtx-3060-and-geforce-rtx-3050-return-to-asian-market",
    "domain": "AI 算力 / 半导体",
    "title": "Memory famine compels GPU vendors to re-release 2020 graphics cards — GeForce RTX 3060 and GeForce RTX 3050 return to Asian market",
    "url": "https://www.tomshardware.com/pc-components/gpus/memory-famine-compels-gpu-vendors-to-re-release-2020-graphics-cards-geforce-rtx-3060-and-geforce-rtx-3050-return-to-asian-market",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T16:33:50+00:00",
    "summary": "Graphics card manufacturer Manli adds new GeForce RTX 3060 and GeForce RTX 3050 SKUs to its portfolio."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/meta-cuts-manus-off-from-its-internal-systems-as-china-ordered-breakup-of-2-billion-ai-deal-begins",
    "domain": "AI 算力 / 半导体",
    "title": "After spat with Chinese gov't, Meta cuts AI Manus off from its internal systems and is 'sunsetting' platform, report claims — Beijing-ordered breakup of $2 billion AI deal begins",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/meta-cuts-manus-off-from-its-internal-systems-as-china-ordered-breakup-of-2-billion-ai-deal-begins",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T14:47:26+00:00",
    "summary": "Meta has finished separating its operations from Manus, the Chinese-founded agentic AI startup it acquired for roughly $2 billion in December."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/razer-blade-18-2026-review",
    "domain": "AI 算力 / 半导体",
    "title": "Razer Blade 18 (2026) review: Coming in fast and hot",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/razer-blade-18-2026-review",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-11T12:57:02+00:00",
    "summary": "The Razer Blade 18 is a large gaming rig with an 18-inch dual-mode display and strong performance, but it runs hot and is very expensive."
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
    "points": 732,
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
    "points": 679,
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
    "id": "rss:https://www.theverge.com/games/949584/microsoft-spinning-off-xbox",
    "domain": "大厂 AI 动态",
    "title": "Microsoft hasn’t ruled out spinning off Xbox",
    "url": "https://www.theverge.com/games/949584/microsoft-spinning-off-xbox",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T16:29:47+00:00",
    "summary": "Microsoft is preparing to lay off a significant chunk of its Xbox division and is reevaluating the plans for its next-generation Project Helix console. It's apparently also considering dramatically re"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/949190/bose-quietcomfort-ultra-headphones-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Bose’s latest QuietComfort Ultra are $70 off, marking a new low price",
    "url": "https://www.theverge.com/gadgets/949190/bose-quietcomfort-ultra-headphones-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T16:00:00+00:00",
    "summary": "If you’re planning on traveling anytime soon, Bose&#8217;s second-generation QuietComfort Ultra headphones are a great companion for long flights and train rides. Not only do they offer excellent nois"
  },
  {
    "id": "rss:https://www.theverge.com/tech/949502/apple-macos-27-golden-gate-siri-ai-apple-intelligence",
    "domain": "大厂 AI 动态",
    "title": "My first 24 hours with Siri AI on the Mac",
    "url": "https://www.theverge.com/tech/949502/apple-macos-27-golden-gate-siri-ai-apple-intelligence",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T15:00:00+00:00",
    "summary": "I turned off Siri on the Mac years ago and never looked back. Similarly, I found Apple Intelligence so fruitless I never engage with it. But the new Siri AI coming to macOS 27 Golden Gate has at least"
  },
  {
    "id": "rss:https://www.theverge.com/report/949073/mike-rugnetta-youtube-never-post-podcast-questionnaire",
    "domain": "大厂 AI 动态",
    "title": "Never Post’s Mike Rugnetta on the creative process and the value of reliable power",
    "url": "https://www.theverge.com/report/949073/mike-rugnetta-youtube-never-post-podcast-questionnaire",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T14:00:00+00:00",
    "summary": "Mike Rugnetta is a writer, podcast host, producer, audio engineer, educator, musician, sound designer, and father. In short, the man wears a lot of hats. He's the cocreator and host of the award-winni"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/942119/vibecoding-backyard-app-gardening-organizing",
    "domain": "大厂 AI 动态",
    "title": "My yard is dying, so I made an app for that",
    "url": "https://www.theverge.com/ai-artificial-intelligence/942119/vibecoding-backyard-app-gardening-organizing",
    "source": "Allison Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T13:00:00+00:00",
    "summary": "When I returned to my computer five minutes after giving Gemini a lengthy prompt, I had two things: a functional app in a preview window, and a message about a bug. \"~ Channel is unrecoverably broken "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/949553/anthropic-fable-5-mythos-5-government-national-security",
    "domain": "大厂 AI 动态",
    "title": "Anthropic cuts off Fable 5 and Mythos 5 access following government order",
    "url": "https://www.theverge.com/ai-artificial-intelligence/949553/anthropic-fable-5-mythos-5-government-national-security",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T12:55:49+00:00",
    "summary": "On Friday evening, the government ordered Anthropic to block access to Fable 5 and Mythos 5 for all foreign nations, both inside and outside the US, due to national security concerns. That order inclu"
  },
  {
    "id": "rss:https://www.theverge.com/games/947136/echo-isle-review-pc",
    "domain": "大厂 AI 动态",
    "title": "Echo Isle is a pint-sized adventure inspired by classic Zelda",
    "url": "https://www.theverge.com/games/947136/echo-isle-review-pc",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T12:00:00+00:00",
    "summary": "Echo Isle is heavily inspired by The Legend of Zelda, and it's not afraid to show it: The retro graphics bear a striking resemblance to Link's Awakening, the main character wears a blue tunic and wiel"
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
    "id": "rss:https://techcrunch.com/2026/06/12/andrew-yang-thinks-the-next-big-startup-opportunity-is-lowering-the-cost-of-living/",
    "domain": "大厂 AI 动态",
    "title": "Andrew Yang thinks the next big startup opportunity is lowering the cost of living",
    "url": "https://techcrunch.com/2026/06/12/andrew-yang-thinks-the-next-big-startup-opportunity-is-lowering-the-cost-of-living/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T04:14:19+00:00",
    "summary": "Andrew Yang made a list of everything Americans overpay for — housing, food, wireless — and thinks the next startup gold rush is giving that money back."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/anthropics-safety-warnings-may-have-just-backfired-the-government-has-pulled-the-plug-on-its-most-powerful-ai/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s safety warnings may have just backfired — the government has pulled the plug on its most powerful AI",
    "url": "https://techcrunch.com/2026/06/12/anthropics-safety-warnings-may-have-just-backfired-the-government-has-pulled-the-plug-on-its-most-powerful-ai/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T02:26:30+00:00",
    "summary": "Anthropic isn't hiding its frustration. \"We disagree that the finding of a narrow potential jailbreak should be cause for recalling a commercial model deployed to hundreds of millions of people,\" the "
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/spacex-ipo-live-updates-on-everything-you-need-to-know/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX IPO: Live updates on everything you need to know",
    "url": "https://techcrunch.com/2026/06/12/spacex-ipo-live-updates-on-everything-you-need-to-know/",
    "source": "Kirsten Korosec, Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T23:15:14+00:00",
    "summary": "TechCrunch has followed SpaceX's start, struggles, and successes from the early days. And we're here for what happens next too. This package of SpaceX IPO coverage includes who stands to win (and mayb"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/metas-months-old-ai-unit-is-a-soul-crushing-gulag-say-the-engineers-stuck-inside-it/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s months-old AI unit is a soul-crushing gulag, say the engineers stuck inside it",
    "url": "https://techcrunch.com/2026/06/12/metas-months-old-ai-unit-is-a-soul-crushing-gulag-say-the-engineers-stuck-inside-it/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T23:00:54+00:00",
    "summary": "A new report suggests the unit, which employs 6,500 people, is on the verge of revolt."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/chinese-cybercrime-operation-that-used-ai-to-scam-hundreds-of-thousands-of-victims-sued-by-google/",
    "domain": "大厂 AI 动态",
    "title": "Chinese cybercrime operation that used AI to scam ‘hundreds of thousands of victims’ sued by Google",
    "url": "https://techcrunch.com/2026/06/12/chinese-cybercrime-operation-that-used-ai-to-scam-hundreds-of-thousands-of-victims-sued-by-google/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T20:38:09+00:00",
    "summary": "The tech giant said a group called \"Outsider Enterprise\" used AI to scam hundreds of thousands of victims, sending 2.5 million text messages over a span of two weeks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/spacex-ipo-closes-up-19-and-delivers-the-worlds-first-trillionaire/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX IPO closes up 19% and delivers the world’s first trillionaire",
    "url": "https://techcrunch.com/2026/06/12/spacex-ipo-closes-up-19-and-delivers-the-worlds-first-trillionaire/",
    "source": "Marina Temkin, Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T20:20:00+00:00",
    "summary": "The company made its heavily anticipated debut on Friday, trading higher than its initial $135 IPO price."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/spacex-president-gwynne-shotwell-just-gave-another-hint-at-a-tesla-merger/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX president Gwynne Shotwell just gave another hint at a Tesla merger",
    "url": "https://techcrunch.com/2026/06/12/spacex-president-gwynne-shotwell-just-gave-another-hint-at-a-tesla-merger/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T19:28:31+00:00",
    "summary": "A SpaceX-Tesla merger seems inevitable."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/mistral-is-rumored-to-be-raising-e3b-at-e20-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Mistral is rumored to be raising €3B at €20B valuation",
    "url": "https://techcrunch.com/2026/06/12/mistral-is-rumored-to-be-raising-e3b-at-e20-valuation/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T17:38:11+00:00",
    "summary": "The funding round would value the company at around €20 billion (about $23.15 billion), nearly double its Series C valuation of €11.7 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/robinhood-sees-record-breaking-traffic-after-spacex-stock-debuts/",
    "domain": "大厂 AI 动态",
    "title": "Robinhood sees ‘record-breaking’ traffic after SpaceX stock debuts",
    "url": "https://techcrunch.com/2026/06/12/robinhood-sees-record-breaking-traffic-after-spacex-stock-debuts/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T17:05:06+00:00",
    "summary": "The trading platform says some customers experienced intermittent disruptions, but those issues have resolved."
  },
  {
    "id": "rss:https://techcrunch.com/video/spacex-anthropic-and-openais-hot-ipo-summer/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX, Anthropic, and OpenAI’s hot IPO summer",
    "url": "https://techcrunch.com/video/spacex-anthropic-and-openais-hot-ipo-summer/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T16:23:25+00:00",
    "summary": "The IPO market is back, and&#160;it&#8217;s&#160;not the same&#160;companies&#160;leading the charge. FAANG had a good run, but a&#160;new acronym is taking over: MANGOS&#160;— Meta (or Microsoft, dep"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/elon-musk-becomes-the-worlds-first-trillionaire-after-spacexs-historic-ipo/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk becomes the world’s first trillionaire after SpaceX’s historic IPO",
    "url": "https://techcrunch.com/2026/06/12/elon-musk-becomes-the-worlds-first-trillionaire-after-spacexs-historic-ipo/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T15:55:06+00:00",
    "summary": "The SpaceX IPO has boosted Musk's paper wealth to more than $1,000,000,000,000 at a time when he is more hated -- and powerful -- than ever."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/12/us-spy-law-to-expire-for-first-time-after-lawmakers-reject-trumps-controversial-pick-to-lead-spy-agencies/",
    "domain": "大厂 AI 动态",
    "title": "US surveillance law to expire for first time after lawmakers reject Trump’s controversial pick to lead spy agencies",
    "url": "https://techcrunch.com/2026/06/12/us-spy-law-to-expire-for-first-time-after-lawmakers-reject-trumps-controversial-pick-to-lead-spy-agencies/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T11:43:32+00:00",
    "summary": "The spy law known as Section 702, which authorizes the NSA and FBI's warrantless surveillance, will all but certainly expire on Friday for the first time."
  },
  {
    "id": "rss:https://stratechery.com/2026/hey-siri-tell-me-a-fable/",
    "domain": "大厂 AI 动态",
    "title": "2026.24: Hey Siri, Tell Me a Fable",
    "url": "https://stratechery.com/2026/hey-siri-tell-me-a-fable/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of June 8, 2026, including Apple finally shipping Intelligence, Anthropic's fable, and the future of European industry."
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
    "id": "rss:https://arstechnica.com/ai/2026/06/anthropic-shuts-down-fable-mythos-models-following-trump-admin-directive/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic shuts down Fable, Mythos models following Trump admin directive",
    "url": "https://arstechnica.com/ai/2026/06/anthropic-shuts-down-fable-mythos-models-following-trump-admin-directive/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T03:00:34+00:00",
    "summary": "Commerce dept. worries that a Fable 5 \"jailbreak\" could be a national security threat."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/spacex-is-now-a-public-company-valued-for-its-ai-potential-so-what-comes-next/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX is now a public company valued for its AI potential, so what comes next?",
    "url": "https://arstechnica.com/space/2026/06/spacex-is-now-a-public-company-valued-for-its-ai-potential-so-what-comes-next/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T22:20:06+00:00",
    "summary": "As of today, SpaceX is owned by investors who will want to see it make money."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/06/peoplesoft-0-day-affecting-hundreds-of-organizations-steals-gigabytes-of-data/",
    "domain": "大厂 AI 动态",
    "title": "PeopleSoft 0-day affecting hundreds of organizations steals gigabytes of data",
    "url": "https://arstechnica.com/security/2026/06/peoplesoft-0-day-affecting-hundreds-of-organizations-steals-gigabytes-of-data/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T19:26:47+00:00",
    "summary": "Vulnerability in the Oracle-owned PeopleSoft software is about as critical as they come."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/controversial-fisa-spying-law-expires-tonight-the-spying-will-continue/",
    "domain": "大厂 AI 动态",
    "title": "Controversial FISA spying law expires tonight. The spying will continue.",
    "url": "https://arstechnica.com/tech-policy/2026/06/controversial-fisa-spying-law-expires-tonight-the-spying-will-continue/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T18:57:51+00:00",
    "summary": "Section 702 of FISA to expire tonight, but certification lasts until March 2027."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/heres-what-jeff-bezos-new-startup-prometheus-will-do/",
    "domain": "大厂 AI 动态",
    "title": "Here's what Jeff Bezos' new startup Prometheus will do",
    "url": "https://arstechnica.com/ai/2026/06/heres-what-jeff-bezos-new-startup-prometheus-will-do/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T18:45:40+00:00",
    "summary": "It isn't the only startup tackling physical AI, but it's one of the best-funded."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/have-politics-finally-come-for-the-national-academies-of-science/",
    "domain": "大厂 AI 动态",
    "title": "Have politics finally come for the National Academies of Science?",
    "url": "https://arstechnica.com/science/2026/06/have-politics-finally-come-for-the-national-academies-of-science/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T18:31:36+00:00",
    "summary": "A pending report on climate attribution may be setting the stage for conflict."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/ukraines-one-time-test-used-fully-autonomous-drones-to-kill-russian-soldiers/",
    "domain": "大厂 AI 动态",
    "title": "Ukraine's one-time test used fully autonomous drones to kill Russian soldiers",
    "url": "https://arstechnica.com/ai/2026/06/ukraines-one-time-test-used-fully-autonomous-drones-to-kill-russian-soldiers/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T18:03:29+00:00",
    "summary": "Full autonomy is rare, but Ukraine is installing AI modules on drones and robots."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/130-billion-in-data-center-projects-blocked-by-protests-so-far-this-year/",
    "domain": "大厂 AI 动态",
    "title": "$130 billion in data center projects blocked by protests so far this year",
    "url": "https://arstechnica.com/tech-policy/2026/06/130-billion-in-data-center-projects-blocked-by-protests-so-far-this-year/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-12T17:18:49+00:00",
    "summary": "Winning fight against AI data centers gives people a \"taste of political power.\""
  },
  {
    "id": "hn:48405718",
    "domain": "股票",
    "title": "SpaceX, Other Mega IPOs Denied Fast Index Entry by S&P",
    "url": "https://www.bloomberg.com/news/articles/2026-06-04/s-p-dow-jones-keeps-megacap-ipo-rules-as-is-after-consultation",
    "source": "tristanj",
    "platform": "hackernews",
    "points": 1061,
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
    "points": 267,
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
    "points": 211,
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
    "id": "hn:48505968",
    "domain": "股票",
    "title": "Elon Musk Becomes First Trillionaire as SpaceX Starts Trading",
    "url": "https://www.nytimes.com/live/2026/06/12/business/spacex-ipo-elon-musk/heres-the-latest",
    "source": "droidjj",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-06-12T16:13:49+00:00",
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
    "id": "wscn:3774613",
    "domain": "股票",
    "title": "全球涨幅最猛股市迎来关键时刻：韩国押注MSCI发达市场\"入场券\"",
    "url": "https://wallstreetcn.com/articles/3774613",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T07:13:57+00:00",
    "summary": "今年涨幅全球居首、市值近乎翻三倍至4.4万亿美元的韩国股市，正等待6月23日MSCI的历史性裁决。升级发达市场或引300亿美元资金涌入，但三星、SK海力士已令Kospi蜕变为全球AI交易的核心载体——指数标签，或许已难以定义这个市场真正的重量。"
  },
  {
    "id": "wscn:3774610",
    "domain": "股票",
    "title": "谷歌官宣3万字路线图：1亿人类水平的AI就是ASI！",
    "url": "https://wallstreetcn.com/articles/3774610",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T06:44:32+00:00",
    "summary": "1000个实例每年翻10倍，五年后就是一亿个AI！谷歌DeepMind推演：一亿个共享大脑、思考快百倍的AI，本身就是ASI。但前路还有六道「叹息之墙」。"
  },
  {
    "id": "wscn:3774609",
    "domain": "股票",
    "title": "量化，负超额了！",
    "url": "https://wallstreetcn.com/articles/3774609",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T06:05:26+00:00",
    "summary": "私募排排网最新统计数据显示，有业绩记录的指数增强私募基金5月平均超额收益为负数，跑输对标指数接近1%，实现正超额收益的产品占比更是不足45%。去年以来，量化私募旗下量化选股、指数增强等产品因亮眼业绩备受资金青睐，百亿级量化私募梯队迅速扩容。但今年以来，量化私募基金超额收益却显著收窄，量魁私募、超量子等知名量化私募旗下部分产品更是出现了负超额"
  },
  {
    "id": "wscn:3774608",
    "domain": "股票",
    "title": "“小巴菲特”：我不投AI！最大遗憾错过早期Palantir少赚数百亿美元，看好被市场“烧伤”的商业地产",
    "url": "https://wallstreetcn.com/articles/3774608",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T04:50:32+00:00",
    "summary": "管理Baupost 44年仅5次亏损的\"波士顿巴菲特\"卡拉曼罕见发声：警告AI热潮泡沫特征明显，拒绝投资OpenAI等烧钱巨头；痛悔错失Palantir百亿回报；逆势重仓商业地产抄底；并对美债占GDP触及百分百红线及霍尔木兹海峡封锁风险发出强烈警告。"
  },
  {
    "id": "wscn:3774605",
    "domain": "股票",
    "title": "谷歌DeepMind重磅报告：从AGI到ASI,世界可能进入\"连续爆炸\"时代",
    "url": "https://wallstreetcn.com/articles/3774605",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T03:01:54+00:00",
    "summary": "谷歌DeepMind联合创始人Shane Legg携理论大牛发布重磅报告，直接跳过\"AGI能否实现\"之争，直指更深远命题：AGI一旦诞生，AI将如何一路进化至超越数万名顶级专家的超级智能ASI？四条技术路径、六大致命瓶颈、智能爆炸临界点……这份报告或许正在描绘人类文明最后的拐点。"
  },
  {
    "id": "wscn:3774601",
    "domain": "股票",
    "title": "“告诉他他就是个XXX”！直播会议现场失控，Meta内部爆发\"AI叛乱\"",
    "url": "https://wallstreetcn.com/articles/3774601",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T02:16:28+00:00",
    "summary": "在一场数千名员工参与的直播会议上，一名Meta员工以粗口打断演讲，直指某位AI高管。Applied AI部门约6500名工程师被强制调岗，工作内容从产品开发降级为生成测试任务。每位管理者平均管理约50名员工，导致员工缺乏支持、晋升无望、难被管理层看见，积压的不满集中爆发。CEO扎克伯格承认“犯了错误”，承诺调整管理架构以稳定人心。"
  },
  {
    "id": "wscn:3774603",
    "domain": "股票",
    "title": "美国政府亲手关停了Anthropic最强模型，然而这不是最坏的消息",
    "url": "https://wallstreetcn.com/premium/articles/3774603?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T02:08:24+00:00",
    "summary": "没有Fable 5的Anthropic可能很快就会跌下“神坛”"
  },
  {
    "id": "wscn:3774602",
    "domain": "股票",
    "title": "投资于神：SpaceX的估值",
    "url": "https://wallstreetcn.com/articles/3774602",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T01:58:19+00:00",
    "summary": "史上最大IPO落地，SpaceX估值1.77万亿美元，马斯克一夜成为人类首位万亿富翁。然而撑起这个天价的，不是今日财报，而是投行锚定2040年的神话叙事。更深的悖论在于：买入SPCX的普通投资者，正在用自己的储蓄，亲手资助那台终将取代自己的机器。"
  },
  {
    "id": "wscn:3774600",
    "domain": "股票",
    "title": "Anthropic全球下架Mythos和Fable模型的“幕后推手”：“主要股东”亚马逊CEO",
    "url": "https://wallstreetcn.com/articles/3774600",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T01:28:48+00:00",
    "summary": "亚马逊作为Anthropic的主要投资者之一，其CEO近日致电美国政府，报告了模型存在的安全隐患。尽管Anthropic在发布前多次通知政府并紧急谈判，美方仍以安全为由实施出口管制，暂停境外访问并全球下架。该事件凸显了美国对前沿AI安全的高度焦虑，以及商业利益与国家安全交织下监管力度的持续升级。"
  },
  {
    "id": "wscn:3774492",
    "domain": "股票",
    "title": "下周“超级央行周”：美联储利率决议沃什首秀、日本央行或加息、中国5月经济数据",
    "url": "https://wallstreetcn.com/articles/3774492",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T01:09:40+00:00",
    "summary": "下周美联储公布利率决议、沃什首秀，市场关注其是否会取消点阵图；市场对日本央行加息预期高达88%，行长植田和男因病缺席会议。英国、澳大利亚等多国央行同步公布利率决议。中国5月社零、工业、房价等数据出炉。此外，G7峰会法国开幕、陆家嘴论坛、OpenAI CEO访韩、燧原科技上会、亚马逊发射任务等事件密集上演。"
  },
  {
    "id": "wscn:3774599",
    "domain": "股票",
    "title": "美伊协议何时签署？特朗普说14日，伊朗否认，“霍尔木兹海峡是否“免费”重开”也各执一词",
    "url": "https://wallstreetcn.com/articles/3774599",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-14T00:45:13+00:00",
    "summary": "特朗普高调宣布美伊协议将于14日签署，霍尔木兹海峡随即重开，并扬言\"手握终极手段\"；伊朗却当场否认时间表，称签署\"不排除未来几天\"。协议14条内容涵盖停火、浓缩铀处置、解冻240亿美元资产等核心议题，以色列则警告其关切遭忽视——这场牵动全球的博弈，远未落幕。"
  },
  {
    "id": "wscn:3774596",
    "domain": "股票",
    "title": "谁降价谁更弱势！摩根大通：智谱和Minimax做了同样的实验，但结果相反",
    "url": "https://wallstreetcn.com/articles/3774596",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T12:42:38+00:00",
    "summary": "摩根大通用“定价权”重估中国大模型赛道：MiniMax旗舰模型M3上线一周即永久降价50%，被视为市场拒绝其技术溢价的信号；而智谱年内API价格翻倍后使用量仍增长，展现罕见定价权。大摩认为，在AI时代，能否持续涨价比跑分更能证明模型竞争力。"
  },
  {
    "id": "wscn:3774597",
    "domain": "股票",
    "title": "20万起点法定化，DR利率纳入大额存单计息体系",
    "url": "https://wallstreetcn.com/articles/3774597",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T12:31:48+00:00",
    "summary": "6月12日，中国人民银行发布《大额存单管理办法（征求意见稿）》（以下简称《办法》），对2015年施行..."
  },
  {
    "id": "wscn:3774593",
    "domain": "股票",
    "title": "抛AMD、减持特斯拉，木头姐4.4亿美元重仓SpaceX",
    "url": "https://wallstreetcn.com/articles/3774593",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T11:46:18+00:00",
    "summary": "木头姐ARK基金披露，旗下多只ETF合计以约4.43亿美元买入约329万股SpaceX私募股份，使其成为ARK Venture Fund第一大持仓（占净资产11.38%）。与此同时，ARK大举减持AMD、特斯拉、百度等成熟科技股。"
  },
  {
    "id": "wscn:3774594",
    "domain": "股票",
    "title": "巴基斯坦总理称预计美伊协议将在24小时内敲定，伊朗火速否认",
    "url": "https://wallstreetcn.com/articles/3774594",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T11:32:23+00:00",
    "summary": "伊朗外交部表示，关于备忘录的具体签署时间还需要等待，虽然不会在明天（14日）签署，但也不排除在未来几天内完成。"
  },
  {
    "id": "wscn:3774595",
    "domain": "股票",
    "title": "亚马逊之后，Meta也限制AI使用量了！当大厂都用不起Token，大模型巨头该“控制利润率”了？",
    "url": "https://wallstreetcn.com/articles/3774595",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T11:29:09+00:00",
    "summary": "Meta内部AI使用成本失控，员工为绩效考核疯狂消耗Token，推动公司2026年相关支出飙升至数十亿美元。面对不断膨胀的账单，Meta被迫设定使用上限、上线实时监控系统。AI行业正从“拼能力”转向“拼成本”，商业化逻辑面临严峻考验。"
  },
  {
    "id": "wscn:3774592",
    "domain": "股票",
    "title": "72%！台积电市占再创新高",
    "url": "https://wallstreetcn.com/articles/3774592",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T11:00:18+00:00",
    "summary": "数据显示，2026年第1季全球前十大晶圆代工产值季增3.7%达479.5亿美元，再创单季新高；其中，台积电凭借AI服务器GPU及xPU需求爆发，营收单季劲增6.3%至358.6亿美元，市占率逆势攀升至72%，与三星、中芯的差距持续拉大。"
  },
  {
    "id": "wscn:3774591",
    "domain": "股票",
    "title": "马斯克远程敲钟穿了老黄的皮衣！SpaceX员工集体穿上绿鞋",
    "url": "https://wallstreetcn.com/articles/3774591",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T10:54:59+00:00",
    "summary": "马斯克缺席纳斯达克，身穿皮衣在发射场远程敲钟，畅谈火星与人类未来；女总裁格温则站台纽约，用一连串“Check”回顾24年苦旅。一个画饼，一个烙饼，员工集体穿“绿鞋”暗藏IPO玄机，共同托起史上首位万亿富豪。"
  },
  {
    "id": "wscn:3774589",
    "domain": "股票",
    "title": "两万亿SpaceX上市，Mag 7不够叫了？MANGOS闪亮登场",
    "url": "https://wallstreetcn.com/articles/3774589",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-13T10:51:49+00:00",
    "summary": "SpaceX上市首日估值即突破2万亿美元，直接冲击Mag 7格局，推动华尔街重构科技股标签体系。“MANGOS”等新缩写迅速冒头，试图纳入SpaceX以及即将上市的AI巨头OpenAI和Anthropic。"
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
    "id": "hn:48359035",
    "domain": "股票",
    "title": "Anthropic Files to Go Public, Setting Stage for Huge I.P.O.",
    "url": "https://www.nytimes.com/2026/06/01/technology/anthropic-ipo.html",
    "source": "jbegley",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-06-01T16:27:40+00:00",
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
    "id": "hn:48354214",
    "domain": "股票",
    "title": "How Not to Buy SpaceX Stock (It's Harder Than You Think)",
    "url": "https://cranberries.medium.com/how-not-to-buy-spacex-stock-its-harder-than-you-think-a37610cb8bd3",
    "source": "clktmr",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-06-01T08:50:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:48343303",
    "domain": "股票",
    "title": "The SpaceX IPO is great for Elon Musk and terrible for you",
    "url": "https://www.theverge.com/ai-artificial-intelligence/940001/elon-musk-spacex-ipo-ai",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-05-31T05:34:42+00:00",
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
    "id": "hn:48390904",
    "domain": "股票",
    "title": "SpaceX Sets Price for $1.77T IPO",
    "url": "https://www.cnbc.com/2026/06/03/spacex-ipo-stock-price-roadshow-musk.html",
    "source": "gen220",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-06-03T22:19:10+00:00",
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
    "points": 121,
    "published_at": "2026-06-12T17:49:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48479537",
    "domain": "金融",
    "title": "Meta steals a tactic from Tesla and builds data centers in tents",
    "url": "https://techcrunch.com/2026/06/04/meta-steals-a-tactic-from-tesla-and-builds-data-centers-in-tents/",
    "source": "gnabgib",
    "platform": "hackernews",
    "points": 103,
    "published_at": "2026-06-10T17:18:39+00:00",
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
    "id": "hn:48518434",
    "domain": "金融",
    "title": "Gas Prices Wipe Out More Than a Year of Wage Gains",
    "url": "https://www.wsj.com/economy/inflation-wages-american-workers-cbe3f187",
    "source": "karakoram",
    "platform": "hackernews",
    "points": 29,
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
    "id": "hn:48436542",
    "domain": "金融",
    "title": "Ripping a DVD, a federal crime in 1999, requires $22 and free software in 2026",
    "url": "https://ringmast4r.substack.com/p/in-1999-this-was-a-federal-crime",
    "source": "akkartik",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-06-07T16:48:25+00:00",
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
  },
  {
    "id": "hn:48225108",
    "domain": "金融",
    "title": "Jeff Bezos says bottom half of U.S. earners should pay no federal income tax",
    "url": "https://www.cbsnews.com/news/jeff-bezos-zero-federal-income-tax-lower-earners/",
    "source": "johnshades",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-05-21T16:11:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:48287165",
    "domain": "金融",
    "title": "Trump administration proposes NDAs for federal workers",
    "url": "https://www.reuters.com/world/us/trump-administration-proposes-non-disclosure-agreements-us-federal-workers-2026-05-26/",
    "source": "SubiculumCode",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-05-26T22:58:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48222708",
    "domain": "金融",
    "title": "Fedora Retiring Its Deepin Desktop Packages",
    "url": "https://www.phoronix.com/news/Fedora-Removing-Deepin",
    "source": "AdmiralAsshat",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-05-21T14:00:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:48156037",
    "domain": "金融",
    "title": "Senior NIAID Official Indicted for Concealing Records During Covid Pandemic",
    "url": "https://www.justice.gov/opa/pr/former-senior-niaid-official-indicted-concealing-federal-records-during-covid-19-pandemic-0",
    "source": "Jimmc414",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-05-16T01:44:08+00:00",
    "summary": ""
  }
]
```
