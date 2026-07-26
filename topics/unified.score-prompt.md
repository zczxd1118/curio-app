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

- 今日日期：`2026-07-26`
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
  "date": "2026-07-26",
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
    "points": 1604125,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV16YRLB7Exd",
    "domain": "AI",
    "title": "5分钟安装ClaudeCode并接入DeepSeek",
    "url": "http://www.bilibili.com/video/av116503957473279",
    "source": "Yin_Code",
    "platform": "bilibili",
    "points": 1290603,
    "published_at": "2026-05-02T08:14:12+00:00",
    "summary": "5分钟教你安装ClaudeCode并接入DeepSeekV4\n用到的命令：\nnode版本检查：node -v\nnpm版本检查：npm -v\nnpm国内镜像：npm config set registry https://registry.npmmirror.com/\ngit版本检查：git -v\nClaudeCode安装命令：npm install -g @anthropic-ai/claude-"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1277529,
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
    "points": 962847,
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
    "points": 953492,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 565136,
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
    "points": 526186,
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
    "points": 427907,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 388322,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 381571,
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
    "points": 320497,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 305995,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 248001,
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
    "points": 204197,
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
    "points": 178219,
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
    "points": 177833,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1b5AeeGEFc",
    "domain": "AI",
    "title": "Cursor太贵？分享三个免费AI编程方案+海量编程技巧【如何看待AI编程】",
    "url": "http://www.bilibili.com/video/av114025056699722",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 158170,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 149180,
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
    "points": 148448,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1gtKx6rEHr",
    "domain": "AI",
    "title": "Claude Code超强平替来了！彻底告别封号！",
    "url": "http://www.bilibili.com/video/av116954828374073",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 121836,
    "published_at": "2026-07-21T10:09:52+00:00",
    "summary": "不可否认 Claude Code确实很强\n但国内小伙伴想要安稳用上它  \n真的太折腾了\n首先你得会用魔法  \n然后 你还得想尽各种办法折腾海外订阅\n最狠的是\n不知道哪天你的账号可能就被封了\nAI工具本来就是为我们服务的\n可现在却成了每天提心吊胆伺候的大爷\n其实咱们真没必要非得死磕\n国内也有一个非常强的 Claude Code 平替工具\n那就是 Qoder CLI  \n今天咱们就不吹不黑  \n直接上"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 111452,
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
    "points": 105990,
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
    "points": 92756,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1GRKJ6fEgn",
    "domain": "AI",
    "title": "Kimi K3编程能力炸裂！在Claude Code中全方位实测代码能力，能否超越Fable 5和GPT-5.6l？结果远超我的预期！国产模型跻身世界第一梯队！",
    "url": "http://www.bilibili.com/video/av116934511239163",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 84144,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73887,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53324,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 44052,
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
    "points": 39109,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 38977,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 36518,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1cCj2ztEf5",
    "domain": "AI",
    "title": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%",
    "url": "http://www.bilibili.com/video/av114574527307727",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 35003,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28820,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 25658,
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
    "points": 22652,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 16492,
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
    "points": 15646,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV16ggC6DEZK",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116963049212769",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 14760,
    "published_at": "2026-07-22T10:10:42+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 14510,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV14a4y1T7Cp",
    "domain": "AI",
    "title": "VS Code + CursorCode 插件，AI 帮你编写、调试代码",
    "url": "http://www.bilibili.com/video/av654787185",
    "source": "马隆工作室",
    "platform": "bilibili",
    "points": 14162,
    "published_at": "2023-04-11T11:48:41+00:00",
    "summary": "免费， VS Code + CursorCode 插件，AI 帮你编写、调试代码"
  },
  {
    "id": "bvid:BV1vLN769EJa",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！大模型入门到进阶，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116894866677118",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 11960,
    "published_at": "2026-07-10T09:04:48+00:00",
    "summary": "【代码已整理】\n无论你是从零开始开发项目，还是对现有代码进行现代化改造，本课程都能为你提供一套严谨的工作流程，让你按自己的方式构建软件。"
  },
  {
    "id": "bvid:BV1E8Tk6MEkw",
    "domain": "AI",
    "title": "AI Agent教程全集丨从入门到进阶丨适合99%小白入行的Agent教程！360°讲解大模型合集（比例RAG +langchain+Agent)全程干货无废话",
    "url": "http://www.bilibili.com/video/av116848259498783",
    "source": "Agent教程",
    "platform": "bilibili",
    "points": 11276,
    "published_at": "2026-07-02T03:38:47+00:00",
    "summary": "陆陆续续也整理了不少资源，希望能帮大家少走一些弯路！无论是学业还是事业，都希望你顺顺利利  看在UP这么努力的份上，求个三连+关注嘛\n\n1️⃣ 大模型入门学习路线图（附学习资源）\n2️⃣ 大模型方向必读书籍PDF版\n3️⃣ 大模型面试题库\n4️⃣ 大模型项目源码\n5️⃣ 超详细海量大模型LLM实战项目\n6️⃣ Langchain/RAG/Agent学习资源\n7️⃣ LLM大模型系统0到1入门学习教"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 9327,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1SfKQ6LEnp",
    "domain": "AI",
    "title": "Cursor+Qoder+Trae三合一 一键续杯！",
    "url": "http://www.bilibili.com/video/av116834669959773",
    "source": "无忧小助手",
    "platform": "bilibili",
    "points": 9196,
    "published_at": "2026-06-29T17:54:50+00:00",
    "summary": "全网独家Cursor、Qoder、trae三合一一键续杯工具，Qoder、Trae切换账号不丢失上下文！"
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "7月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "iwenwikii",
    "platform": "bilibili",
    "points": 9118,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "AI充值站：aipayok.com"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 8751,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 7930,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1dsNv66E3Q",
    "domain": "AI",
    "title": "【Cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116922599344955",
    "source": "六月要癫",
    "platform": "bilibili",
    "points": 7707,
    "published_at": "2026-07-15T06:39:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1S9Et6yEL8",
    "domain": "AI",
    "title": "claude code在量化交易方面的应用",
    "url": "http://www.bilibili.com/video/av116709008606912",
    "source": "xxy的大迷弟",
    "platform": "bilibili",
    "points": 7173,
    "published_at": "2026-06-07T13:19:31+00:00",
    "summary": "AI或者量化方面的交流可以邮箱交流：965418170@qq.com"
  },
  {
    "id": "bvid:BV14uTM69EUd",
    "domain": "AI",
    "title": "破甲claude/减少claude道德约束/ai破解卡密",
    "url": "http://www.bilibili.com/video/av116826918880943",
    "source": "去码头整点海鸥啊",
    "platform": "bilibili",
    "points": 6764,
    "published_at": "2026-06-28T09:05:03+00:00",
    "summary": "企鹅交流群：1038830654"
  },
  {
    "id": "bvid:BV1u4G9zmEte",
    "domain": "AI",
    "title": "什么是MCP？VS Code中使用MCP Server",
    "url": "http://www.bilibili.com/video/av114426032168712",
    "source": "AI落地派",
    "platform": "bilibili",
    "points": 6657,
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based o"
  },
  {
    "id": "hn:49035303",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, Microsoft, Meta warn against overregulating open-weight models",
    "url": "https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 648,
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
    "points": 329,
    "published_at": "2026-07-24T12:53:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49035751",
    "domain": "AI 算力 / 半导体",
    "title": "Open Weights and American AI Leadership [pdf]",
    "url": "https://images.nvidia.com/pdf/Open-Weights-and-American-AI-Leadership.pdf",
    "source": "lairv",
    "platform": "hackernews",
    "points": 111,
    "published_at": "2026-07-24T13:58:12+00:00",
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
    "id": "hn:48971128",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia DGX Spark as a daily driver",
    "url": "https://daniel.lawrence.lu/blog/2026-07-15-dgx-spark-as-daily-driver/",
    "source": "plun9",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-07-19T19:44:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:49025890",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's 256-core Epyc 9996 'Venice' claims up to a 3.4x jump over Intel Xeon",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-256-core-epyc-9996-venice-claims-up-to-a-3-4x-jump-over-intel-xeon-competition-20-percent-over-nvidia-vera-zen-6-comes-with-up-to-1024mb-of-l3-16-channel-memory-and-5ghz-clock-speeds",
    "source": "rndsignals",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-23T18:16:54+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/intel-foundry-improves-execution-but-external-customers-remain-the-test/",
    "domain": "AI 算力 / 半导体",
    "title": "Intel Foundry Improves Execution, but External Customers Remain the Test",
    "url": "https://www.eetimes.com/intel-foundry-improves-execution-but-external-customers-remain-the-test/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T22:00:00+00:00",
    "summary": "Intel’s fabs are healing, but $293M in outside revenue won’t scare TSMC yet. The post Intel Foundry Improves Execution, but External Customers Remain the Test appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/dac-2026-what-does-it-actually-take-to-create-ai-chips/",
    "domain": "AI 算力 / 半导体",
    "title": "DAC 2026: What Does It Actually Take to Create AI Chips?",
    "url": "https://www.eetimes.com/dac-2026-what-does-it-actually-take-to-create-ai-chips/",
    "source": "Frank Schirrmeister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:00:00+00:00",
    "summary": "AI chips don’t need hype—they need power, memory, IP, thermal, and verification fights. See what DAC 2026 engineers will expose. The post DAC 2026: What Does It Actually Take to Create AI Chips? appea"
  },
  {
    "id": "rss:https://www.eetimes.com/supply-chain-leaders-new-math-for-network-decisions/",
    "domain": "AI 算力 / 半导体",
    "title": "Supply Chain Leaders’ New Math for Network Decisions",
    "url": "https://www.eetimes.com/supply-chain-leaders-new-math-for-network-decisions/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T08:00:00+00:00",
    "summary": "Gartner urges supply chain leaders to quantify daily operational friction, making network investments more resilient and easier to justify. The post Supply Chain Leaders&#8217; New Math for Network De"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/security-flaw-in-vaticans-click-to-pray-app-leaves-over-700-000-global-users-exposed-app-has-been-leaking-user-data-for-over-six-months-and-still-does",
    "domain": "AI 算力 / 半导体",
    "title": "Security flaw in Vatican’s ‘Click to Pray’ app leaves over 700,000 global users exposed — app has been leaking user data for over six months and still does",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/security-flaw-in-vaticans-click-to-pray-app-leaves-over-700-000-global-users-exposed-app-has-been-leaking-user-data-for-over-six-months-and-still-does",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T17:56:07+00:00",
    "summary": "An app linked to the Vatican with hundreds of thousands of users was found to have zero authentication and security. That means anyone can access its backend and siphon users' data, including names, e"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-agent-goes-rogue-and-hacks-popular-ai-community-left-escape-plans-for-future-models-inside-the-companys-infrastructure",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI agent goes rogue and hacks popular AI community — left escape plans for future models inside the company's infrastructure",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-agent-goes-rogue-and-hacks-popular-ai-community-left-escape-plans-for-future-models-inside-the-companys-infrastructure",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T16:41:59+00:00",
    "summary": "OpenAI tests multiple autonomous AI agents at once and has difficulty identifying the threats each of them represents, if a new report from Reuters is accurate."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/ram-machine-case-probably-costs-more-than-the-entire-build-nvidia-rtx-5060-core-ultra-5-cpu-and-32gb-ddr5-8200-ram-are-hiding-inside",
    "domain": "AI 算力 / 半导体",
    "title": "'RAM Machine' case probably costs more than the entire build — Nvidia RTX 5060, Core Ultra 5 CPU, and 32GB DDR5-8200 RAM are hiding inside",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/ram-machine-case-probably-costs-more-than-the-entire-build-nvidia-rtx-5060-core-ultra-5-cpu-and-32gb-ddr5-8200-ram-are-hiding-inside",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T15:34:57+00:00",
    "summary": "A Redditor is giving away an RTX 5060 gaming PC that's covered by RAM on the outside and has 32GB of RAM on the inside. You can join the sweepstakes simply by leaving a comment on the post."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-an-nvidia-rtx-5060-ti-gaming-pc-with-core-ultra-7-cpu-and-32gb-ram-for-under-usd1-200-thermaltakes-view-u2660t-170-slashed-by-33-percent",
    "domain": "AI 算力 / 半导体",
    "title": "Grab an Nvidia RTX 5060 Ti gaming PC with Core Ultra 7 CPU and 32GB RAM for under $1,200 — Thermaltake's View u2660T-170 slashed by 33%",
    "url": "https://www.tomshardware.com/pc-components/grab-an-nvidia-rtx-5060-ti-gaming-pc-with-core-ultra-7-cpu-and-32gb-ram-for-under-usd1-200-thermaltakes-view-u2660t-170-slashed-by-33-percent",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T15:18:22+00:00",
    "summary": "Thermaltake has a no-brainer deal up on Woot right now where it'll let you have an $1,800 PC for as little as 1,177. For that price, you're getting an RTX 5060 Ti (8GB), a Core Ultra 7 265KF, 32GB of "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-and-sk-group-enter-usd500-billion-ai-partnership-plan-to-supercharge-ai-infrastructure-with-next-gen-memory-and-massive-ai-factories",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia and SK Group enter $500 billion AI partnership — plan to supercharge AI infrastructure with next-gen memory and massive AI factories",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-and-sk-group-enter-usd500-billion-ai-partnership-plan-to-supercharge-ai-infrastructure-with-next-gen-memory-and-massive-ai-factories",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T13:55:35+00:00",
    "summary": "Nvidia and SK Group enter $500 billion strategic partnership focused on long-term memory supply, 2 GW AI data center, and future AI infrastructure"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/delawares-printed-solid-rebrands-to-prusa-usa",
    "domain": "AI 算力 / 半导体",
    "title": "Delaware’s Printed Solid rebrands to Prusa USA",
    "url": "https://www.tomshardware.com/3d-printing/delawares-printed-solid-rebrands-to-prusa-usa",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T12:41:51+00:00",
    "summary": "Printed Solid, the Delaware-based filament manufacturer acquired by Czech Prusa Research in 2022, is now known as Prusa USA, Inc."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/aoc-u32g4-32-inch-4k-dual-refresh-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "AOC U32G4 32-inch 4K Dual-Refresh gaming monitor review: Solid performance and value",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/aoc-u32g4-32-inch-4k-dual-refresh-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T12:05:00+00:00",
    "summary": "AOC redefines the budget 4K gaming monitor with its U32G4. This 32-inch IPS panel sports 160 Hz, 320 Hz in FHD resolution, Adaptive-Sync, HDR400 and wide gamut color for around $320."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/xbox/microsoft-shipped-a-native-xbox-360-emulator-with-its-new-backwards-compatible-releases-on-pc-modders-quickly-got-360-games-running-with-minor-tweaks",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft shipped a native Xbox 360 emulator with its new backwards-compatible releases on PC — modders quickly got 360 games running with minor tweaks",
    "url": "https://www.tomshardware.com/video-games/xbox/microsoft-shipped-a-native-xbox-360-emulator-with-its-new-backwards-compatible-releases-on-pc-modders-quickly-got-360-games-running-with-minor-tweaks",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T11:30:00+00:00",
    "summary": "Microsoft dropped four OG Xbox titles on PC a couple of days ago and they came with a native Xbox 360 emulator baked in. These games are packaged as Xbox 360 files, to the emulator runs them as such, "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/game-compressor-can-save-you-hundreds-of-gigs-across-your-game-library-usd6-utility-leverages-windows-built-in-lzx-compression-for-substantial-space-savings",
    "domain": "AI 算力 / 半导体",
    "title": "Game Compressor can save you hundreds of GB across your game library — as storage prices remain high, utility leverages Windows' built-in LZX compression for substantial space savings",
    "url": "https://www.tomshardware.com/pc-components/storage/game-compressor-can-save-you-hundreds-of-gigs-across-your-game-library-usd6-utility-leverages-windows-built-in-lzx-compression-for-substantial-space-savings",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T11:00:00+00:00",
    "summary": "Game Compressor leverages Windows' built-in LZX compression for substantial space savings and can save you hundreds of gigs across your game library."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/pro-ukraine-group-claims-it-helped-hack-russian-drone-air-defence-system-shooting-down-su-57-in-friendly-fire-incident-moscow-confirms-fifth-generation-fighter-jet-crashed-in-technical-malfunction",
    "domain": "AI 算力 / 半导体",
    "title": "Pro-Ukraine group claims it helped hack Russian drone air defense system, shooting down Su-57 in friendly fire incident — Moscow confirms fifth-generation fighter jet crashed in 'technical malfunction",
    "url": "https://www.tomshardware.com/tech-industry/drones/pro-ukraine-group-claims-it-helped-hack-russian-drone-air-defence-system-shooting-down-su-57-in-friendly-fire-incident-moscow-confirms-fifth-generation-fighter-jet-crashed-in-technical-malfunction",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T10:30:00+00:00",
    "summary": "An advanced fifth-generation Su-57 stealth fighter jet crashed spectacularly “during a routine training mission in the Moscow region on Thursday,” say reports published by Russian state media. But som"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/lockheed-martin-unveils-counter-drone-system-that-can-neutralize-up-to-50-enemy-drones-in-a-single-mission-sensor-agnostic-system-uses-high-power-microwave-to-purge-enemies-from-the-sky",
    "domain": "AI 算力 / 半导体",
    "title": "Lockheed Martin unveils counter-drone system that can ‘neutralize up to 50 enemy drones in a single mission’ — sensor-agnostic system uses High Power Microwave to purge enemies from the sky",
    "url": "https://www.tomshardware.com/tech-industry/drones/lockheed-martin-unveils-counter-drone-system-that-can-neutralize-up-to-50-enemy-drones-in-a-single-mission-sensor-agnostic-system-uses-high-power-microwave-to-purge-enemies-from-the-sky",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T10:00:00+00:00",
    "summary": "Lockheed Martin has unveiled a ground-launched high-power microwave counter-drone system which cab 'neutralize up to 50 enemy drones in a single mission.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/ram-thieves-in-china-jailed-after-looting-a-string-of-esport-hotels-stole-16-sticks-worth-usd2-000-in-frenzied-hotel-room-dismantling",
    "domain": "AI 算力 / 半导体",
    "title": "RAM thieves in China jailed after looting a string of eSport hotels — stole 16 sticks worth $2,000 in 'frenzied hotel room-dismantling'",
    "url": "https://www.tomshardware.com/pc-components/ram/ram-thieves-in-china-jailed-after-looting-a-string-of-esport-hotels-stole-16-sticks-worth-usd2-000-in-frenzied-hotel-room-dismantling",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T09:00:00+00:00",
    "summary": "The rise and fall of a pair of eSports hotel RAM thieves has been retold by Chinese news media."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-and-24-other-companies-sign-open-weights-letter-as-washington-weighs-chinese-ai-model-ban",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia and 24 other companies sign open-weights letter as Washington weighs Chinese AI model ban — OpenAI, Anthropic, and Google absent from the list",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-and-24-other-companies-sign-open-weights-letter-as-washington-weighs-chinese-ai-model-ban",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T18:31:48+00:00",
    "summary": "Signatories include chipmakers, server vendors, cloud operators, enterprise software firms, security companies, and venture funds"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-commits-to-14a-mass-production-in-2028-as-its-sales-rise-25-percent-year-over-year",
    "domain": "AI 算力 / 半导体",
    "title": "Intel commits to 14A mass production in 2028 as its sales rise 25% year-over-year",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-commits-to-14a-mass-production-in-2028-as-its-sales-rise-25-percent-year-over-year",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:49:43+00:00",
    "summary": "Intel posts 25% higher year-over-year sales and above-the-guidance earnings, and confirms that its 14A technology is on-track to start high volume ramp in 2028."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/geekom-a9-max-2026-mini-pc-review",
    "domain": "AI 算力 / 半导体",
    "title": "Geekom A9 Max 2026 review: Gorgon Point in a compact Mini PC",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/geekom-a9-max-2026-mini-pc-review",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T16:30:00+00:00",
    "summary": "Mini PC specialist Geekom has updated its A9 Max design with AMD’s latest mobile silicon. The incremental improvements of the AMD Ryzen AI 9 HX470 are supported by a revamped Ice Blast 3.0 cooling sol"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-huggingface-breach-heralds-an-unprecedented-age-of-ai-cyber-warfare-contemporary-llms-have-caused-massive-upheaval-in-cybersecurity-and-its-only-going-to-get-worse",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI's HuggingFace breach heralds an unprecedented age of AI cyber warfare — contemporary LLMs have caused massive upheaval in cybersecurity, and it's only going to get worse",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-huggingface-breach-heralds-an-unprecedented-age-of-ai-cyber-warfare-contemporary-llms-have-caused-massive-upheaval-in-cybersecurity-and-its-only-going-to-get-worse",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T16:12:08+00:00",
    "summary": "Contemporary AI bots are far too competent at cybersecurity, and humanity may have reached a tipping point where it's hard to keep up."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/dell-14s-review",
    "domain": "AI 算力 / 半导体",
    "title": "Dell 14S review: High-class design and 20+ hour battery life",
    "url": "https://www.tomshardware.com/laptops/dell-14s-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T16:10:39+00:00",
    "summary": "The Dell 14S makes good on its promise of serving as a cheaper alternative to the pricier XPS 14."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-working-on-new-x3d-v-cache-mobile-chip-for-gaming-laptops-leaker-claims-ryzen-7-9800hx3d-could-launch-with-8-cores-16-threads-and-96mb-cache",
    "domain": "AI 算力 / 半导体",
    "title": "AMD working on new X3D V-cache mobile chip for gaming laptops, leaker claims — Ryzen 7 9800HX3D could launch with 8 cores, 16 threads, and 96MB cache",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-working-on-new-x3d-v-cache-mobile-chip-for-gaming-laptops-leaker-claims-ryzen-7-9800hx3d-could-launch-with-8-cores-16-threads-and-96mb-cache",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T15:07:53+00:00",
    "summary": "A fresh leak suggests AMD is preparing an 8-core, 16-thread Zen 5 mobile processor with 96MB of L3 cache, potentially bringing the desktop Ryzen 7 9800X3D experience to gaming laptops."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/gigabyte-announces-support-for-chinese-made-cxmt-memory-pushes-it-to-8200-mt-s-on-socket-am5",
    "domain": "AI 算力 / 半导体",
    "title": "Gigabyte announces support for Chinese-made CXMT memory — pushes it to 8200 MT/s on Socket AM5",
    "url": "https://www.tomshardware.com/pc-components/ddr5/gigabyte-announces-support-for-chinese-made-cxmt-memory-pushes-it-to-8200-mt-s-on-socket-am5",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T14:44:58+00:00",
    "summary": "The performance is impressive and it's good to see official support, but the question remains whether you can actually buy any of it."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/south-korean-memory-giants-samsung-and-sk-hynix-are-set-to-announce-massive-deals-with-leading-u-s-tech-firms-report-claims-korean-president-arrives-in-silicon-valley-for-meetings-and-high-profile-ai-summit",
    "domain": "AI 算力 / 半导体",
    "title": "South Korean memory giants Samsung and SK Hynix are set to announce massive deals with leading U.S. tech firms, report claims — Korean president arrives in Silicon Valley for meetings and high-profile",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/south-korean-memory-giants-samsung-and-sk-hynix-are-set-to-announce-massive-deals-with-leading-u-s-tech-firms-report-claims-korean-president-arrives-in-silicon-valley-for-meetings-and-high-profile-ai-summit",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T14:43:04+00:00",
    "summary": "Samsung and SK Hynix are expected to unveil multibillion-dollar memory-chip partnerships with major U.S. technology companies during South Korean President Lee Jae Myung’s visit to San Francisco"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-exec-was-very-happy-to-see-nvidias-vera-performance-results-i-actually-thought-we-were-beating-them-by-smaller-numbers",
    "domain": "AI 算力 / 半导体",
    "title": "AMD exec was ‘very happy’ to see Nvidia‘s Vera performance results – ‘I actually thought we were beating them by smaller numbers’",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-exec-was-very-happy-to-see-nvidias-vera-performance-results-i-actually-thought-we-were-beating-them-by-smaller-numbers",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T14:39:03+00:00",
    "summary": "Nvidia took the first stab with its Vera results earlier this week, and now AMD is biting back with SPEC results for its Zen 6 ‘Venice’ CPUs, as well."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/when-will-the-ea-greed-end-fans-vent-their-fury-as-company-announces-usd150-version-of-fc-27-annual-game-release-comes-in-three-editions-but-top-tier-option-is-50-percent-more-expensive-than-gta-vi-ultimate",
    "domain": "AI 算力 / 半导体",
    "title": "'When will the EA greed end': Fans vent their fury as company announces $150 version of FC 27 — annual game release comes in three editions, but top-tier option is 50% more expensive than GTA VI Ultim",
    "url": "https://www.tomshardware.com/video-games/when-will-the-ea-greed-end-fans-vent-their-fury-as-company-announces-usd150-version-of-fc-27-annual-game-release-comes-in-three-editions-but-top-tier-option-is-50-percent-more-expensive-than-gta-vi-ultimate",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T14:15:33+00:00",
    "summary": "EA's FC 27 is available in three options, starting at $69.99 for the base game and going up to $149.99 for the Ultimate Plus Edition. The top-tier option, which costs more than double than the Standar"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-took-ten-days-to-tell-hugging-face-its-models-were-behind-the-july-11-weekend-hack",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI took ten days to tell Hugging Face its models were behind the July 11 weekend hack, report claims — rogue AI agents reportedly active on the open Internet for several days",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-took-ten-days-to-tell-hugging-face-its-models-were-behind-the-july-11-weekend-hack",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T13:47:15+00:00",
    "summary": "OpenAI confirmed to Hugging Face only this week that models it was testing carried out the July 11 attack on the AI platform's production infrastructure."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/president-trump-expands-ai-data-center-ratepayer-protection-pledge-to-include-state-governors-and-utility-companies-white-house-claims-this-will-make-electricity-more-affordable",
    "domain": "AI 算力 / 半导体",
    "title": "President Trump expands AI data center ‘ratepayer protection pledge’ to include state governors and utility companies — White House claims this will make electricity more affordable",
    "url": "https://www.tomshardware.com/tech-industry/policy/president-trump-expands-ai-data-center-ratepayer-protection-pledge-to-include-state-governors-and-utility-companies-white-house-claims-this-will-make-electricity-more-affordable",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T11:42:41+00:00",
    "summary": "U.S. President Donald Trump expands the 'ratepayer protection pledge' to include states, utility companies, and data center developers. He claims that the pledge will help electricity costs go down, e"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/45-percent-off-slashed-to-just-usd1-099-this-bargain-rtx-5060-powered-gaming-laptop-is-discounted-by-usd900-at-hp-near-half-price-hyperx-omen-16-is-the-perfect-gaming-laptop-for-heading-back-to-school",
    "domain": "AI 算力 / 半导体",
    "title": "45% off: Slashed to just $1,099, this bargain RTX 5060-powered gaming laptop is discounted by $900 at HP — near half-price HyperX Omen 16 is the perfect gaming laptop for heading back to school",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/45-percent-off-slashed-to-just-usd1-099-this-bargain-rtx-5060-powered-gaming-laptop-is-discounted-by-usd900-at-hp-near-half-price-hyperx-omen-16-is-the-perfect-gaming-laptop-for-heading-back-to-school",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T11:21:42+00:00",
    "summary": "Save a massive $900 on HP's HyperX Omen 16 with RTX 5060. The perfect back-to-school gaming laptop is now only $1,099."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd460-on-this-amd-9800x3d-gaming-pc-with-rtx-5080-get-blistering-4k-performance-for-less",
    "domain": "AI 算力 / 半导体",
    "title": "Save $460 on this AMD 9800X3D gaming PC with RTX 5080 — get blistering 4K performance for less",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd460-on-this-amd-9800x3d-gaming-pc-with-rtx-5080-get-blistering-4k-performance-for-less",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T10:48:02+00:00",
    "summary": "Get an RTX 5080 gaming PC with 9800X3D for $2,829 at Newegg."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amd-confirmed-usd5-4-billion-ati-acquisition-20-years-ago-today-deal-to-reinvent-our-industry-paved-the-way-for-radeon-gpu-innovation-apus-and-games-console-domination",
    "domain": "AI 算力 / 半导体",
    "title": "AMD confirmed $5.4 billion ATI acquisition 20 years ago today — deal to 'reinvent our industry' paved the way for Radeon GPU innovation, APUs, and games console domination",
    "url": "https://www.tomshardware.com/pc-components/gpus/amd-confirmed-usd5-4-billion-ati-acquisition-20-years-ago-today-deal-to-reinvent-our-industry-paved-the-way-for-radeon-gpu-innovation-apus-and-games-console-domination",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T10:00:00+00:00",
    "summary": "On this day in 2006, AMD confirmed its acquisition of graphics chip firm ATI. AMD stumped up a cash-and-stock deal worth a total of $5.4B for the Canadian PC graphics innovators."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-reveals-cpu-architecture-roadmap-through-2028-following-zen-6-venice-launch-zen-7-florence-to-debut-in-2028-alongside-diversified-product-family-confirms-zen-8-ravenna-in-development",
    "domain": "AI 算力 / 半导体",
    "title": "AMD reveals CPU architecture roadmap through 2028, following Zen 6 'Venice' launch — Zen 7 'Florence' to debut in 2028 alongside diversified product family, confirms Zen 8 'Ravenna' in development",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-reveals-cpu-architecture-roadmap-through-2028-following-zen-6-venice-launch-zen-7-florence-to-debut-in-2028-alongside-diversified-product-family-confirms-zen-8-ravenna-in-development",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T09:27:05+00:00",
    "summary": "AMD's Lisa Su shows off the company's roadmap through 2030, including teases of Zen 7 and Zen 8 CPUs."
  },
  {
    "id": "hn:48992221",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC eyes price hikes of up to 25% on chip production services in 2027",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes",
    "source": "speckx",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-21T13:40:51+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/u-s-starts-genesis-mission-with-5b-for-first-projects/",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Starts Genesis Mission with $5B for First Projects",
    "url": "https://www.eetimes.com/u-s-starts-genesis-mission-with-5b-for-first-projects/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T23:00:00+00:00",
    "summary": "America drops $5B on AI’s Genesis Mission while China lines up $295B; see why the opening bet may already be too small. The post U.S. Starts Genesis Mission with $5B for First Projects appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/the-story-behind-fuse-eda-ai-system/",
    "domain": "AI 算力 / 半导体",
    "title": "The Story Behind Fuse EDA AI system",
    "url": "https://www.eetimes.com/the-story-behind-fuse-eda-ai-system/",
    "source": "Siemens EDA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T19:35:36+00:00",
    "summary": "What does it take to build agentic AI for EDA that users can trust and verify? Listen in on this behind-the-scenes conversation around the development of a groundbreaking new platform. The post The St"
  },
  {
    "id": "rss:https://www.eetimes.com/etched-raises-300m-with-1b-in-pre-orders/",
    "domain": "AI 算力 / 半导体",
    "title": "Etched Raises $300M with $1B in Pre-Orders",
    "url": "https://www.eetimes.com/etched-raises-300m-with-1b-in-pre-orders/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T15:00:00+00:00",
    "summary": "AI chip startup Etched will start shipping its racks this summer. The post Etched Raises $300M with $1B in Pre-Orders appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/dac-2026-users-are-not-waiting-diy-ai-is-now-in-vogue/",
    "domain": "AI 算力 / 半导体",
    "title": "DAC 2026: Users Are Not Waiting; DIY AI Is Now in Vogue",
    "url": "https://www.eetimes.com/dac-2026-users-are-not-waiting-diy-ai-is-now-in-vogue/",
    "source": "Frank Schirrmeister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T07:45:00+00:00",
    "summary": "At DAC 2026, chip giants stop waiting for EDA vendors and build their own AI brains—see who’s seizing control. The post DAC 2026: Users Are Not Waiting; DIY AI Is Now in Vogue appeared first on EE Tim"
  },
  {
    "id": "rss:https://www.eetimes.com/from-rhetoric-to-metrics-raghib-hussain-first-year-as-altera-ceo/",
    "domain": "AI 算力 / 半导体",
    "title": "From Rhetoric to Metrics: Raghib Hussain’s First Year as Altera CEO",
    "url": "https://www.eetimes.com/from-rhetoric-to-metrics-raghib-hussain-first-year-as-altera-ceo/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T22:00:00+00:00",
    "summary": "Altera has taped out six chips in nine months, three ahead of schedule, as new CEO focuses on execution. The post From Rhetoric to Metrics: Raghib Hussain’s First Year as Altera CEO appeared first on "
  },
  {
    "id": "rss:https://www.eetimes.com/ai-in-eda-is-real-its-now-and-its-on-show-at-dac-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "AI in EDA Is Real, It’s Now, and It’s on Show at DAC 2026",
    "url": "https://www.eetimes.com/ai-in-eda-is-real-its-now-and-its-on-show-at-dac-2026/",
    "source": "Frank Schirrmeister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T18:00:00+00:00",
    "summary": "AI in chip design has left the slide deck and hit DAC 2026’s floor—walk the stack and test the hype. The post AI in EDA Is Real, It’s Now, and It’s on Show at DAC 2026 appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/cea-leti-looks-beyond-sram-and-dram-as-ai-reshapes-the-memory-roadmap/",
    "domain": "AI 算力 / 半导体",
    "title": "CEA-Leti Looks Beyond SRAM and DRAM as AI Reshapes the Memory Roadmap",
    "url": "https://www.eetimes.com/cea-leti-looks-beyond-sram-and-dram-as-ai-reshapes-the-memory-roadmap/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T07:53:34+00:00",
    "summary": "CEA-Leti’s François Andrieu describes more embedded, persistent, and low-energy memories that will meet the growing demands of AI. The post CEA-Leti Looks Beyond SRAM and DRAM as AI Reshapes the Memor"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-new-x100-chip-lineup-puts-strix-halo-into-robots-apus-for-physical-ai-bring-zen-5-cpu-rdna-3-5-gpu-cores-to-compete-with-intels-panther-lake",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s new X100 chip lineup puts embedded Ryzen AI 'Strix Halo' chips into robots – APUs for physical AI bring Zen 5 CPU, RDNA 3.5 GPU cores to compete with Intel’s Panther Lake",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-new-x100-chip-lineup-puts-strix-halo-into-robots-apus-for-physical-ai-bring-zen-5-cpu-rdna-3-5-gpu-cores-to-compete-with-intels-panther-lake",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T18:30:00+00:00",
    "summary": "Countering Intel’s recent moves, AMD is bringing its Strix Halo APUs to the realm of robots, and physical AI. Designed for 24/7 operation and a 10-year embedded lifecycle, X100 will also be offered as"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amd-takes-the-wraps-off-its-instinct-mi455x-ai-accelerator-cdna-5-and-helios-rack-scale-architecture-combine-to-take-the-fight-to-nvidia-in-the-data-center",
    "domain": "AI 算力 / 半导体",
    "title": "AMD takes the wraps off its Instinct MI455X AI accelerator — CDNA 5 and Helios rack-scale architecture combine to take the fight to Nvidia in the data center",
    "url": "https://www.tomshardware.com/pc-components/gpus/amd-takes-the-wraps-off-its-instinct-mi455x-ai-accelerator-cdna-5-and-helios-rack-scale-architecture-combine-to-take-the-fight-to-nvidia-in-the-data-center",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-23T18:05:44+00:00",
    "summary": "AMD showed off its MI455X accelerator at its Advancing AI 2026 event, demonstrating its strong competitive performance, large HBM memory capacity, and Helios rack-scale architecture."
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
    "points": 368,
    "published_at": "2026-07-15T18:40:34+00:00",
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
    "points": 135,
    "published_at": "2026-07-21T21:27:54+00:00",
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
    "id": "hn:48993130",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.6 Flash",
    "url": "https://console.cloud.google.com/agent-platform/publishers/google/model-garden/gemini-3.6-flash",
    "source": "marrf",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-07-21T14:56:15+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/971041/google-confirms-pixel-11-price-hike",
    "domain": "大厂 AI 动态",
    "title": "Google basically confirms the Pixel 11 is getting a price hike",
    "url": "https://www.theverge.com/tech/971041/google-confirms-pixel-11-price-hike",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T18:13:36+00:00",
    "summary": "Google's Vice President of Devices and Services, Shakil Barkat, all but confirmed in an interview with 9to5 Google that its next Pixel phone would cost more than the Pixel 10. Considering the ongoing "
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/971013/oli-freke-bjooks-beat-gems-drum-machine-book-interview",
    "domain": "大厂 AI 动态",
    "title": "Synth historian Oli Freke will spend big on a good bicycle",
    "url": "https://www.theverge.com/entertainment/971013/oli-freke-bjooks-beat-gems-drum-machine-book-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T15:15:00+00:00",
    "summary": "Oli Freke is a musician and journalist whose works have appeared in Sound on Sound, The Quietus, and Mixmag. This has included using math to explore the melodic potential of the Western 12-tone scale "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/970685/teenage-engineering-30-percent-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Teenage Engineering’s unique music machines are 30 percent off",
    "url": "https://www.theverge.com/gadgets/970685/teenage-engineering-30-percent-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T15:00:00+00:00",
    "summary": "With elements from synthesizers, loopers, and effects pedals, Teenage Engineering’s devices lie somewhere between musical instrument and modern art. These grooveboxes, as they’re often called, are cap"
  },
  {
    "id": "rss:https://www.theverge.com/business/971011/warner-bros-suing-amazon-poaching-employees",
    "domain": "大厂 AI 动态",
    "title": "Warner Bros. is suing Amazon for poaching employees",
    "url": "https://www.theverge.com/business/971011/warner-bros-suing-amazon-poaching-employees",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T14:05:12+00:00",
    "summary": "Warner Bros. Discovery has filed suit against Amazon, accusing it of illegally poaching employees, including Pia Barlow, former senior VP for originals marketing. In the complaint, Warner says that \"A"
  },
  {
    "id": "rss:https://www.theverge.com/tech/970343/e-reader-case-3d-printed-gun",
    "domain": "大厂 AI 动态",
    "title": "Is this e-reader case a gun?",
    "url": "https://www.theverge.com/tech/970343/e-reader-case-3d-printed-gun",
    "source": "Mack DeGeurin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T13:00:00+00:00",
    "summary": "Is an e-reader case as dangerous as a Glock 19? Last month, Louisville, Kentucky-based creator Luke The Maker showed off a bizarre, 3D-printed, pistol-shaped case design for the popular minimalist Xte"
  },
  {
    "id": "rss:https://www.theverge.com/games/961183/what-surrounds-us-review-pc-steam",
    "domain": "大厂 AI 动态",
    "title": "What Surrounds Us will make you think a lot about circles",
    "url": "https://www.theverge.com/games/961183/what-surrounds-us-review-pc-steam",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T12:00:00+00:00",
    "summary": "What Surrounds Us takes its title literally. You play as a circle surrounding a hole in its middle - it looks like a donut with frosting. You work together with other sentient moving circles, sometime"
  },
  {
    "id": "rss:https://www.theverge.com/tech/971004/z-fold8-xteink-x4-light-flip-installer",
    "domain": "大厂 AI 动态",
    "title": "Folding and flipping phones are getting seriously good",
    "url": "https://www.theverge.com/tech/971004/z-fold8-xteink-x4-light-flip-installer",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T12:00:00+00:00",
    "summary": "Hi, friends! Welcome to Installer No. 137, your guide to the best and Verge-iest stuff in the world. (If you're new here, welcome, happy phone season, and also you can read all the old editions at the"
  },
  {
    "id": "rss:https://www.theverge.com/tech/970473/forget-expensive-sleepbuds-buy-this-pillow-instead",
    "domain": "大厂 AI 动态",
    "title": "Forget expensive sleepbuds. Buy this pillow instead",
    "url": "https://www.theverge.com/tech/970473/forget-expensive-sleepbuds-buy-this-pillow-instead",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T07:00:00+00:00",
    "summary": "Tech companies love to sell us expensive gadgets to solve all of life's little problems. Sleepbuds sold by the likes of Anker and Ozlo are a good example. These miniature marvels of engineering sit fl"
  },
  {
    "id": "rss:https://www.theverge.com/tech/970970/after-backlash-meta-pauses-plan-to-rate-limit-its-smart-glasses",
    "domain": "大厂 AI 动态",
    "title": "After backlash, Meta pauses plan to ‘rate limit’ its smart glasses",
    "url": "https://www.theverge.com/tech/970970/after-backlash-meta-pauses-plan-to-rate-limit-its-smart-glasses",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T22:27:46+00:00",
    "summary": "Remember when Meta was planning to charge a $20 monthly subscription fee for the smart glasses feature that lets people hear each other more clearly - even though that feature runs locally on your gla"
  },
  {
    "id": "rss:https://www.theverge.com/report/970901/instagram-meta-glasses-prank-harassment-ban",
    "domain": "大厂 AI 动态",
    "title": "Meta just created a moderation nightmare for its smart glasses",
    "url": "https://www.theverge.com/report/970901/instagram-meta-glasses-prank-harassment-ban",
    "source": "Mia Sato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T19:23:44+00:00",
    "summary": "Meta's smart glasses have been a PR headache for the company. Public backlash has been swift, and fierce; people are concerned about the erosion of privacy and expansion of surveillance. Some especial"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/25/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/",
    "domain": "大厂 AI 动态",
    "title": "Monday.com is the latest tech company to blame AI for layoffs — here are 20 others",
    "url": "https://techcrunch.com/2026/07/25/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/",
    "source": "Rebecca Bellan, Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "A running look — in reverse chronological order — at the bigger tech companies that have announced significant layoffs this year with AI as a stated factor."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/25/warner-bros-lawsuit-accuses-amazon-of-illegally-poaching-executives/",
    "domain": "大厂 AI 动态",
    "title": "Warner Bros. lawsuit accuses Amazon of illegally poaching executives",
    "url": "https://techcrunch.com/2026/07/25/warner-bros-lawsuit-accuses-amazon-of-illegally-poaching-executives/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T20:55:11+00:00",
    "summary": "The lawsuit will likely renew debates about whether term employment agreements are enforceable under California. law"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/25/the-hacker-who-humiliated-spyware-makers-and-was-never-caught/",
    "domain": "大厂 AI 动态",
    "title": "The hacker who humiliated spyware makers and was never caught",
    "url": "https://techcrunch.com/2026/07/25/the-hacker-who-humiliated-spyware-makers-and-was-never-caught/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T20:24:14+00:00",
    "summary": "An awe-inspiring hacktivist who hacked two controversial government spyware makers may be the most prolific hacker to have never gotten caught. What do we know about Phineas Fisher?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/25/elon-musks-boring-company-reportedly-raising-funding-at-a-20-billion-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk’s Boring Company reportedly raising funding at a $20 billion valuation",
    "url": "https://techcrunch.com/2026/07/25/elon-musks-boring-company-reportedly-raising-funding-at-a-20-billion-valuation/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T19:23:32+00:00",
    "summary": "Elon Musk's tunneling startup is reportedly in talks for a major new funding round."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/25/kalshi-demands-netflix-take-down-trailer-for-prediction-games-documentary/",
    "domain": "大厂 AI 动态",
    "title": "Kalshi demands Netflix take down trailer for ‘Prediction Games’ documentary",
    "url": "https://techcrunch.com/2026/07/25/kalshi-demands-netflix-take-down-trailer-for-prediction-games-documentary/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T16:46:46+00:00",
    "summary": "Kalshi claims the trailer is “defamatory” and contains “both fabricated documents and false and misleading statements.”"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/25/librarians-are-hosting-viral-avoiding-ai-workshops-for-people-who-are-fed-up-with-big-tech/",
    "domain": "大厂 AI 动态",
    "title": "Librarians are hosting viral ‘Avoiding AI’ workshops for people who are fed up with Big Tech",
    "url": "https://techcrunch.com/2026/07/25/librarians-are-hosting-viral-avoiding-ai-workshops-for-people-who-are-fed-up-with-big-tech/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T16:00:00+00:00",
    "summary": "At libraries around the country, \"Avoiding AI\" workshops have elicited unprecedented demand."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/25/one-fallen-power-line-exposed-a-growing-ai-data-center-problem-heres-how-to-fix-it/",
    "domain": "大厂 AI 动态",
    "title": "One fallen power line exposed a growing AI data center problem. Here’s how to fix it.",
    "url": "https://techcrunch.com/2026/07/25/one-fallen-power-line-exposed-a-growing-ai-data-center-problem-heres-how-to-fix-it/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T13:05:00+00:00",
    "summary": "A close call in Northern Virginia revealed just how poorly data centers respond to grid disruptions. Here's how to fix the problem."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/i-tried-out-openais-new-ai-keypad-which-will-be-fun-for-coders-and-slightly-mystifying-to-everyone-else/",
    "domain": "大厂 AI 动态",
    "title": "I tried out OpenAI’s new AI keypad — which will be fun for some coders and slightly mystifying to everyone else",
    "url": "https://techcrunch.com/2026/07/24/i-tried-out-openais-new-ai-keypad-which-will-be-fun-for-coders-and-slightly-mystifying-to-everyone-else/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T00:23:11+00:00",
    "summary": "OpenAI's fancy new AI keypad will be a lot of fun for some, while many others are probably not going to touch it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/spacex-launches-new-v3-starlink-satellites-but-suffers-another-booster-failure/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX launches new V3 Starlink satellites but suffers another booster failure",
    "url": "https://techcrunch.com/2026/07/24/spacex-launches-new-v3-starlink-satellites-but-suffers-another-booster-failure/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T23:25:47+00:00",
    "summary": "The company ticked off a few more boxes on the second Starship V3 flight, but appears to have had another issue relighting the booster's rocket engines."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/prentis-new-ai-lab-co-founded-by-reid-hoffman-mark-pincus-in-talks-to-raise-100m/",
    "domain": "大厂 AI 动态",
    "title": "Prentis, new AI lab co-founded by Reid Hoffman, Mark Pincus in talks to raise $100M",
    "url": "https://techcrunch.com/2026/07/24/prentis-new-ai-lab-co-founded-by-reid-hoffman-mark-pincus-in-talks-to-raise-100m/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T22:25:58+00:00",
    "summary": "The neolab is betting that automating routine computer tasks will soon outpace coding as AI's biggest use case."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/techcrunch-disrupt-2026s-new-smart-money-stage-explores-fintech-payments-ai-and-everything-between/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Disrupt 2026’s new Smart Money Stage explores fintech, payments, AI, and everything between",
    "url": "https://techcrunch.com/2026/07/24/techcrunch-disrupt-2026s-new-smart-money-stage-explores-fintech-payments-ai-and-everything-between/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T22:10:00+00:00",
    "summary": "Money has evolved into far more than the cash in your wallet or your bank account. And at TechCrunch Disrupt 2026, we’re devoting an entire stage to that progression."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/social-media-ban-children-countries-list/",
    "domain": "大厂 AI 动态",
    "title": "Vietnam is looking to restrict social media for kids; here are the growing number of other countries doing the same",
    "url": "https://techcrunch.com/2026/07/24/social-media-ban-children-countries-list/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T21:15:00+00:00",
    "summary": "Australia was the first country to issue a ban in late 2025, aiming to reduce the pressures and risks that young users may face on social media, including cyberbullying, social media addiction, and ex"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/waymo-reportedly-mulling-a-breakup-with-uber/",
    "domain": "大厂 AI 动态",
    "title": "Waymo reportedly mulling a breakup with Uber",
    "url": "https://techcrunch.com/2026/07/24/waymo-reportedly-mulling-a-breakup-with-uber/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T20:43:35+00:00",
    "summary": "The contract between the two companies ends in May 2028, Uber told TechCrunch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/volkswagen-engineers-charged-with-insider-trading-tied-to-rivian-joint-venture/",
    "domain": "大厂 AI 动态",
    "title": "Volkswagen engineers charged with insider trading tied to Rivian joint venture",
    "url": "https://techcrunch.com/2026/07/24/volkswagen-engineers-charged-with-insider-trading-tied-to-rivian-joint-venture/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T19:56:23+00:00",
    "summary": "The indictment, which was unsealed Friday, alleges the Volkswagen engineers used confidential insider information to buy stock in Rivian."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/why-cognition-bought-poke-ai-personality-is-becoming-a-competitive-advantage/",
    "domain": "大厂 AI 动态",
    "title": "Why Cognition bought Poke: AI personality is becoming a competitive advantage",
    "url": "https://techcrunch.com/2026/07/24/why-cognition-bought-poke-ai-personality-is-becoming-a-competitive-advantage/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T18:07:32+00:00",
    "summary": "The acquisition brings Poke’s conversational style and interaction model to Cognition’s coding agent Devin, reflecting a growing belief that how AI assistants interact with users is as important as th"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/us-accuses-american-of-allegedly-wiping-his-phone-using-a-duress-password-during-border-search/",
    "domain": "大厂 AI 动态",
    "title": "US accuses American of allegedly wiping his phone using a ‘duress’ password during border search",
    "url": "https://techcrunch.com/2026/07/24/us-accuses-american-of-allegedly-wiping-his-phone-using-a-duress-password-during-border-search/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:53:30+00:00",
    "summary": "A U.S. citizen has asked a court to throw out the government's claim that he gave over a passcode to border authorities that wiped his phone's data, opening up fresh questions about a person's constit"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/anduril-reportedly-in-talks-to-raise-funding-at-100b-valuation-more-than-3x-last-years-mark/",
    "domain": "大厂 AI 动态",
    "title": "Anduril reportedly in talks to raise funding at $100B valuation, more than 3x last year’s mark",
    "url": "https://techcrunch.com/2026/07/24/anduril-reportedly-in-talks-to-raise-funding-at-100b-valuation-more-than-3x-last-years-mark/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:33:19+00:00",
    "summary": "Anduril is said to be raising a new round of funding that may push its valuation up to about $100 billion, per Reuters."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/build-in-public-fail-in-public-what-its-like-to-be-a-founder-under-20-right-now/",
    "domain": "大厂 AI 动态",
    "title": "Build in public, fail in public: what it’s like to be a founder under 20 right now",
    "url": "https://techcrunch.com/2026/07/24/build-in-public-fail-in-public-what-its-like-to-be-a-founder-under-20-right-now/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:00:00+00:00",
    "summary": "AI tools have democratized the opportunity to build, shortening the timelines of success and enabling more young people to start successful companies without stepping foot inside a Big Tech company."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic launches Opus 5",
    "url": "https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:00:00+00:00",
    "summary": "Opus 5 will be both cheaper and less restrictive than Fable, likely making it preferable in most use cases."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/24/indias-move-against-jack-dorseys-bitchat-sparks-legal-debate/",
    "domain": "大厂 AI 动态",
    "title": "India’s move against Jack Dorsey’s Bitchat sparks legal debate",
    "url": "https://techcrunch.com/2026/07/24/indias-move-against-jack-dorseys-bitchat-sparks-legal-debate/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T16:54:58+00:00",
    "summary": "The offline messaging app surged in popularity in India amid protests in New Delhi."
  },
  {
    "id": "rss:https://stratechery.com/2026/the-copium-wars/",
    "domain": "大厂 AI 动态",
    "title": "2026.30: The Copium Wars",
    "url": "https://stratechery.com/2026/the-copium-wars/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of July 20, 2026 including Chinese models and frontier futures, what happened to Hugging Face, and the NBA and its second apron bet."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/07/sdcc-teaser-gives-us-our-first-good-look-at-blade-runner-2099/",
    "domain": "大厂 AI 动态",
    "title": "SDCC teaser gives us our first good look at Blade Runner 2099",
    "url": "https://arstechnica.com/culture/2026/07/sdcc-teaser-gives-us-our-first-good-look-at-blade-runner-2099/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T20:52:30+00:00",
    "summary": "Also: Forging the One Ring in Rings of Power S3 teaser; new Lanterns trailer; Spaceballs: The New One panel."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/spacex-eyes-tower-catch-for-next-starship-after-auspicious-end-to-13th-flight/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX eyes tower catch for next Starship after auspicious end to 13th flight",
    "url": "https://arstechnica.com/space/2026/07/spacex-eyes-tower-catch-for-next-starship-after-auspicious-end-to-13th-flight/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T17:47:22+00:00",
    "summary": "SpaceX will likely attempt to catch Starship back at the launch pad on its next flight."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/07/with-help-from-data-art-museums-are-reframing-the-visitor-experience/",
    "domain": "大厂 AI 动态",
    "title": "With help from data, art museums are reframing the visitor experience",
    "url": "https://arstechnica.com/culture/2026/07/with-help-from-data-art-museums-are-reframing-the-visitor-experience/",
    "source": "Mureji Fatunde-Iloeje",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T11:00:32+00:00",
    "summary": "Museums are embracing data-driven curation and a shifting technology landscape."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/big-tech-accused-of-stonewalling-european-social-media-researchers/",
    "domain": "大厂 AI 动态",
    "title": "Big Tech accused of stonewalling European social media researchers",
    "url": "https://arstechnica.com/tech-policy/2026/07/big-tech-accused-of-stonewalling-european-social-media-researchers/",
    "source": "Anna Desmarais, wired.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T10:45:32+00:00",
    "summary": "Researchers say TikTok, X, and Meta aren't providing data they're legally required to."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/wildfire-forces-evacuation-of-nasas-deep-space-network-complex-in-spain/",
    "domain": "大厂 AI 动态",
    "title": "Wildfire forces evacuation of NASA's Deep Space Network complex in Spain",
    "url": "https://arstechnica.com/space/2026/07/wildfire-forces-evacuation-of-nasas-deep-space-network-complex-in-spain/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T22:28:20+00:00",
    "summary": "\"Any potential damage will be assessed when it is safe to do so.\""
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/after-court-loss-paramount-agrees-to-delay-warner-bros-merger-until-trial/",
    "domain": "大厂 AI 动态",
    "title": "Paramount/WBD merger delayed for months as states' lawsuit moves toward trial",
    "url": "https://arstechnica.com/tech-policy/2026/07/after-court-loss-paramount-agrees-to-delay-warner-bros-merger-until-trial/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T21:56:02+00:00",
    "summary": "“Halting this merger while our case proceeds is a critical victory,\" NY AG said."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/canadian-legislator-reads-out-apparent-llm-response-in-floor-speech/",
    "domain": "大厂 AI 动态",
    "title": "Canadian legislator reads out apparent LLM response in floor speech",
    "url": "https://arstechnica.com/ai/2026/07/canadian-legislator-reads-out-apparent-llm-response-in-floor-speech/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T21:25:15+00:00",
    "summary": "\"Here’s a more natural, flowing version of that section...\""
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/anthropics-opus-5-is-about-token-efficiency-not-a-capability-leap/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic's Opus 5 is about token efficiency, not a capability leap",
    "url": "https://arstechnica.com/ai/2026/07/anthropics-opus-5-is-about-token-efficiency-not-a-capability-leap/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T21:05:51+00:00",
    "summary": "Models are improving quickly, but the cheaper options are often good enough."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/roku-raises-streaming-stick-prices-by-up-to-60-percent/",
    "domain": "大厂 AI 动态",
    "title": "Roku raises streaming stick prices by up to 60 percent",
    "url": "https://arstechnica.com/gadgets/2026/07/roku-raises-streaming-stick-prices-by-up-to-60-percent/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-24T19:41:06+00:00",
    "summary": "Roku blames RAM shortage after CEO called it \"great\" for business in May."
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
    "id": "hn:49024958",
    "domain": "股票",
    "title": "DOT cranks up its campaign to strip bike lane references from federal websites",
    "url": "https://text.npr.org/nx-s1-5900901",
    "source": "Jtsummers",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-07-23T17:11:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49012630",
    "domain": "股票",
    "title": "Alphabet Announces Second Quarter 2026 Results [pdf]",
    "url": "https://s206.q4cdn.com/479360582/files/doc_financials/2026/q2/2026q2-alphabet-earnings-release.pdf",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-07-22T20:04:48+00:00",
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
    "id": "wscn:3777950",
    "domain": "股票",
    "title": "韩股74万亿抛售警报解除：国民年金7月意外转为净买入，SK海力士获大举加仓",
    "url": "https://wallstreetcn.com/articles/3777950",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T05:59:18+00:00",
    "summary": "韩国国民年金7月净买入684亿韩元KOSPI成分股，为今年以来首次月度净买入，其中，SK海力士获净买入4258亿韩元，连续两个月蝉联年金基金增持榜首。再平衡压力因股市回调自然缓解，为近期承压的韩股释放积极信号。"
  },
  {
    "id": "wscn:3777948",
    "domain": "股票",
    "title": "SK海力士下周放榜：Q2营业利润或突破64万亿韩元创新高，同比增长近600%",
    "url": "https://wallstreetcn.com/articles/3777948",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T05:46:46+00:00",
    "summary": "市场预计，Q2营业利润率达75%~77%，连续第三季度超越台积电。增长核心驱动力为HBM领导地位及AI数据中心需求爆发。SK海力士将于7月29日公布第二季度业绩。分析认为，强劲业绩大幅优化了其财务结构，标志着韩国存储行业迈入AI驱动的新阶段。"
  },
  {
    "id": "wscn:3777949",
    "domain": "股票",
    "title": "黄仁勋、马斯克，最新涉华表态！",
    "url": "https://wallstreetcn.com/articles/3777949",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T05:45:11+00:00",
    "summary": "马斯克表示，中国极有可能成为AI领导者，美国禁用中国模型也无法阻挡。黄仁勋盛赞中国开源AI大模型非常优秀，呼吁向中国学习与合作；他明确反对美国限制或禁用中国开源模型，认为应允许美国公司使用，并联合多家科技巨头发布公开信，为开源AI全面辩护。"
  },
  {
    "id": "wscn:3777947",
    "domain": "股票",
    "title": "最贵光刻机，不好卖了？",
    "url": "https://wallstreetcn.com/articles/3777947",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T05:08:25+00:00",
    "summary": "最贵光刻机并未滞销，而是竞争已步入“经济可行性”阶段。四大巨头基于商业现实态度分化：英特尔激进抢跑求制程领先；台积电算账求稳暂缓导入；三星因财务压力观望；SK海力士为HBM果断引入。而ASML凭借现有设备与服务稳赚不赔，仍是最大赢家。"
  },
  {
    "id": "wscn:3777946",
    "domain": "股票",
    "title": "美伊的下一步走势：理性推演",
    "url": "https://wallstreetcn.com/articles/3777946",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T05:08:20+00:00",
    "summary": "兴证策略张启尧团队认为，短期内局势易升难降，双方谈判窗口未开启，伊朗或主动升级以反制施压。中期看，特朗普受中期选举压力，必须在9-10月前控制油价、结束冲突。长期看，美伊不会陷入战争泥潭，升级本质是为谈判降级服务。"
  },
  {
    "id": "wscn:3777943",
    "domain": "股票",
    "title": "AI还要跌多久",
    "url": "https://wallstreetcn.com/articles/3777943",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T04:01:54+00:00",
    "summary": "东吴证券认为，本轮AI调整由美股盈利担忧、韩国去杠杆及利率抬升共振引发。杠杆出清的急跌或近尾声，但估值消化仍需时间。普跌止于去杠杆，真底始于利润分化。盈利增速放缓会引发估值下杀，下一轮上涨需寻找“新盈利加速度”，聚焦高增长硬件及兑现商业化利润的下游应用。"
  },
  {
    "id": "wscn:3777945",
    "domain": "股票",
    "title": "“大空头” Burry加码做空英伟达、美光",
    "url": "https://wallstreetcn.com/articles/3777945",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T03:53:30+00:00",
    "summary": "Burry发文披露最新持仓动向，扩大对美光、英伟达及费城半导体ETF的空头仓位，同时新增做空卡特彼勒，并维持做空特斯拉、Palantir及持有纳斯达克100看跌期权。他认为英伟达当前及未来的大量需求并非来自终端客户，而是通过表外融资安排循环驱动。"
  },
  {
    "id": "wscn:3777944",
    "domain": "股票",
    "title": "9500亿！特朗普重建301关税新框架，潜藏三大风险？",
    "url": "https://wallstreetcn.com/premium/articles/3777944?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T03:38:16+00:00",
    "summary": "特朗普用301替代失效关税，实际税率微升但制度化，仍需关注三大潜在风险。"
  },
  {
    "id": "wscn:3777940",
    "domain": "股票",
    "title": "301接棒122关税，有何影响？",
    "url": "https://wallstreetcn.com/articles/3777940",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T03:11:19+00:00",
    "summary": "华泰证券认为，301接棒122关税短期冲击有限，核心影响如下：1、对华实际关税仅微升，中国出口受影响大体可控。2、豁免范围扩大，利好AI链、医药及民生原材料。3、新规法律基础更实且难取消，将对全球供应链重塑产生更持久深远的影响。"
  },
  {
    "id": "wscn:3777941",
    "domain": "股票",
    "title": "车主境外遭“锁车”，极氪重设跨境用车规则",
    "url": "https://wallstreetcn.com/articles/3777941",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T02:49:14+00:00",
    "summary": "适应新阶段。"
  },
  {
    "id": "wscn:3777939",
    "domain": "股票",
    "title": "宁德时代的增长变得更“重”了",
    "url": "https://wallstreetcn.com/articles/3777939",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T02:39:56+00:00",
    "summary": "收入确认慢于出货。"
  },
  {
    "id": "wscn:3777937",
    "domain": "股票",
    "title": "高盛交易主管：美股“操作难度依然极高”，建议逢低布局黄金",
    "url": "https://wallstreetcn.com/articles/3777937",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T02:25:09+00:00",
    "summary": "高盛交易主管Tony Pasquariello表示，当前美股内部剧烈分化、动量波动高企，市场“操作难度依然极高”，投资者应简化仓位、聚焦高确信度交易。与此同时，他认为黄金的投机性多头已大幅出清，央行购金重启，4000美元附近支撑稳固，建议投资者逢低布局黄金，把握结构性机会。"
  },
  {
    "id": "wscn:3775965",
    "domain": "股票",
    "title": "玻璃基板：英特尔加速入局后摩尔时代的“材料革命”，它是AI算力封装的终极答案？",
    "url": "https://wallstreetcn.com/premium/articles/3775965?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T02:08:06+00:00",
    "summary": "Omdia数据显示，全球玻璃基板市场规模预计2030年将突破320亿美元。"
  },
  {
    "id": "wscn:3777938",
    "domain": "股票",
    "title": "下周“加息”并非“天方夜谭”？飙升的油价、“不给指引”的沃什，这都让市场紧张",
    "url": "https://wallstreetcn.com/articles/3777938",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T02:03:58+00:00",
    "summary": "美联储下周加息预期从一周前的13%骤升至38%。市场紧张源于两点：一是布油破百元重燃通胀担忧；二是新主席沃什废除“前瞻指引”，令定价难度陡增。与此同时，联储内部鹰派积聚。分析指出，多数经济学家仍预计维持利率不变，市场与经济学家的罕见背离折射出沃什新风格下不确定性将成新常态。"
  },
  {
    "id": "wscn:3777935",
    "domain": "股票",
    "title": "“红海战线”升级：胡塞武装一天两次袭击沙特红海港口石油设施，沙特空袭回应",
    "url": "https://wallstreetcn.com/articles/3777935",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T01:23:05+00:00",
    "summary": "此轮空袭是沙特主导联军自四年前各方达成停火协议以来首次公开承认实施空袭行动，标志着局势已突破此前的默契边界。此次升级的核心风险在于延布——霍尔木兹海峡遭封锁后，延布已成沙特原油出口唯一替代通道，一旦受损将重创全球能源市场。"
  },
  {
    "id": "wscn:3777934",
    "domain": "股票",
    "title": "特朗普下令暂停空袭伊朗",
    "url": "https://wallstreetcn.com/articles/3777934",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-26T00:53:25+00:00",
    "summary": "知情人士表示，此举旨在为外交谈判留出空间，阿曼代表团已赴德黑兰就重启霍尔木兹海峡通航展开谈判。然而，持续数月的冲突已致国际油价破百，特朗普正深陷进退两难的战略困境，高油价带来的经济代价更直接威胁共和党11月中期选举选情。"
  },
  {
    "id": "wscn:3777933",
    "domain": "股票",
    "title": "事关红海航道 沙特、胡塞和特朗普各放狠话",
    "url": "https://wallstreetcn.com/articles/3777933",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T12:24:03+00:00",
    "summary": "红海局势骤然升温！胡塞武装导弹袭击沙特城市贾赞，沙特联军随即反击荷台达军事目标，双方陷入互相报复循环。更棘手的是，霍尔木兹海峡因伊朗战事受阻，红海已成沙特原油出口命脉——近八成原油经此通道外运。"
  },
  {
    "id": "wscn:3777932",
    "domain": "股票",
    "title": "英伟达被“错杀”了？估值跌至五年低点，市场押注2027年后几乎零增长",
    "url": "https://wallstreetcn.com/articles/3777932",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T11:35:51+00:00",
    "summary": "英伟达今年涨幅仅10%，估值跌至五年低点，市盈率较历史均值腰斩，而AMD、美光分别狂飙142%与213%——市场似乎已将它从成长股\"降级\"为成熟大盘股。然而，分析师测算其合理价值被低估逾30%，云厂商资本开支持续扩张、推理芯片份额逆势上升，一旦AI寒冬来袭，反而可能是最后的避风港。"
  },
  {
    "id": "wscn:3777930",
    "domain": "股票",
    "title": "为AI投资腾资金？美国科技巨头年内裁员近14万人",
    "url": "https://wallstreetcn.com/articles/3777930",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-25T10:19:30+00:00",
    "summary": "美国科技巨头年内裁员近14万人，与7250亿美元AI基础设施豪赌形成强烈反差。亚马逊、Meta、微软等巨头借\"AI提效\"之名瘦身，但分析指出，科技公司正在通过裁员弥补早期的过度招聘，并为AI投资释放资本。"
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
    "id": "hn:48974426",
    "domain": "股票",
    "title": "Big tech needs to justify AI spending as investors dump stocks",
    "url": "https://www.bloomberg.com/news/articles/2026-07-19/big-tech-needs-to-justify-ai-spending-as-investors-dump-stocks",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-07-20T04:41:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49012394",
    "domain": "股票",
    "title": "We got California to intervene about OpenAI's corporate switch from nonprofit",
    "url": "https://fortune.com/2026/07/22/openai-foundation-class-n-stock-board-control-ipo/",
    "source": "SLHamlet",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-22T19:46:18+00:00",
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
    "id": "hn:48962049",
    "domain": "股票",
    "title": "Elon Musk Runs from Interview at Last Minute as SpaceX Stock Crashed [video]",
    "url": "https://www.youtube.com/shorts/TFpF7ZzHc3w",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-18T20:30:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48996223",
    "domain": "股票",
    "title": "The AI Bubble Is No Ordinary Bubble",
    "url": "https://www.theatlantic.com/ideas/2026/07/ai-economy-stock-market/688004/",
    "source": "gereshes",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-21T18:31:36+00:00",
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
    "id": "hn:48750160",
    "domain": "股票",
    "title": "Tech giants lose $2T in SpaceX's IPO month",
    "url": "https://english.elpais.com/economy-and-business/2026-07-01/tech-giants-lose-2-trillion-in-spacexs-ipo-month-the-valuations-were-unsustainable.html",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-07-01T17:14:01+00:00",
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
    "id": "hn:49046525",
    "domain": "金融",
    "title": "The Fedora 45 Sausage Factory",
    "url": "https://supakeen.com/weblog/the-fedora-45-sausage-factory/",
    "source": "6581",
    "platform": "hackernews",
    "points": 141,
    "published_at": "2026-07-25T11:04:57+00:00",
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
    "id": "hn:49028304",
    "domain": "金融",
    "title": "US announces double-digit tariffs on most of globe to replace expiring duties",
    "url": "https://finance.yahoo.com/economy/policy/article/trump-administration-announces-the-next-phase-of-global-tariffs-with-10-to-125-rates-on-much-of-the-globe-210032314.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-23T21:28:52+00:00",
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
    "id": "hn:49001708",
    "domain": "金融",
    "title": "Tesla Balance Bike",
    "url": "https://shop.tesla.com/product/balance-bike-for-kids",
    "source": "surprisetalk",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-22T04:00:11+00:00",
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
    "id": "hn:48791799",
    "domain": "金融",
    "title": "Is The Economist Always Wrong?",
    "url": "https://economist.com/interactive/finance-and-economics/2026/07/02/is-the-economist-always-wrong",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 59,
    "published_at": "2026-07-05T06:40:05+00:00",
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
    "id": "hn:48754128",
    "domain": "金融",
    "title": "US feds are actively hiring \"person who decides which models to ban\"",
    "url": "https://www.usajobs.gov/job/856265200",
    "source": "arm32",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-07-01T22:45:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48723371",
    "domain": "金融",
    "title": "Feds Tracked Down an Anti-ICE Dad in NYC Hotel, but How?",
    "url": "https://gizmodo.com/federal-agents-reportedly-tracked-down-an-anti-ice-dad-in-a-new-york-hotel-its-not-clear-how-2000778714",
    "source": "ripe",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-06-29T18:42:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:48824584",
    "domain": "金融",
    "title": "JPMorgan, BofA and Others Explore Buying Card Network to Raise Debit-Card Fees",
    "url": "https://www.wsj.com/finance/banking/jpmorgan-bank-of-america-and-other-banks-explore-a-deal-to-shake-up-payments-world-9d8639fb",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-07-07T22:04:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:48780128",
    "domain": "金融",
    "title": "AI First: How the Federal Government Is Prioritizing AI over People and Planet",
    "url": "https://stopgreedbuildgreen.climateandcommunity.org/posts/ai-first",
    "source": "eatox",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-03T21:21:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:48796110",
    "domain": "金融",
    "title": "Moving back home used to be a sign of failure. Now it shows financial savvy",
    "url": "https://www.wsj.com/lifestyle/relationships/living-with-parents-finances-0c35530c",
    "source": "apparent",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-07-05T17:34:49+00:00",
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
    "id": "hn:48824532",
    "domain": "金融",
    "title": "SpaceX Shares Stumble in Nasdaq-100 Debut",
    "url": "https://www.wsj.com/finance/stocks/spacex-shares-stumble-in-nasdaq-100-debut-9ec10565",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-07T22:00:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48719682",
    "domain": "金融",
    "title": "Supreme Court rules Trump cannot fire Fed member Lisa Cook",
    "url": "https://www.nbcnews.com/politics/supreme-court/supreme-court-rules-trump-cannot-fire-fed-member-lisa-cook-grants-powe-rcna234931",
    "source": "ceejayoz",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-06-29T14:24:41+00:00",
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
  },
  {
    "id": "hn:48767569",
    "domain": "金融",
    "title": "Trump Made $1B on Crypto Deals While His Fans Lost a Fortune",
    "url": "https://www.wsj.com/finance/currencies/trump-made-1-billion-on-crypto-deals-while-his-fans-lost-a-fortune-408754c9",
    "source": "doener",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-07-02T21:25:54+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://semianalysis.com/2025/09/16/xais-colossus-2-first-gigawatt-datacenter/",
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
    "title": "Meta Superintelligence – Leadership Compute, Talent, and Data",
    "url": "https://semianalysis.com/2025/07/11/meta-superintelligence-leadership-compute-talent-and-data/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-11T20:12:19+00:00",
    "summary": "Meta’s shocking purchase of 49% of Scale AI at a ~$30B valuation shows that money is of no concern for the $100B annual cashflow ad machine. Despite seemingly unlimited resources, Meta has been fallin"
  }
]
```
