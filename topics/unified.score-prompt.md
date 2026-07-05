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

- 今日日期：`2026-07-05`
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
  "date": "2026-07-05",
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
    "points": 3581219,
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
    "points": 1420857,
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
    "points": 1333957,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 940473,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 930758,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1ig9jYUERk",
    "domain": "AI",
    "title": "黑马程序员DeepSeek+Cursor+Devbox+Sealos带你零代码搞定实战项目开发部署视频教程，基于AI完成项目的设计、开发、测试、联调、部署全流程",
    "url": "http://www.bilibili.com/video/av114101778908628",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 930292,
    "published_at": "2025-03-04T07:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公综号，回复关键词：deepseek\n【Java学习路线图】展开查看更多内容\nhttps://www.bilibili.com/read/cv9965357\n学习集Q结Q地群：625260577\n\nJava最高效学习路线图（依次向下顺序学习即可）\nJava基础：BV1821CY8E2d\nJavaweb+AI：BV1yGydYEE3H\n苍穹外卖："
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 851577,
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
    "points": 835375,
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
    "points": 733444,
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
    "points": 532102,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 331809,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1VDTv6rEtM",
    "domain": "AI",
    "title": "终于，Claude Code 封号原因被曝光了！竟然针对中国用户，植入隐形代码？",
    "url": "http://www.bilibili.com/video/av116844031774993",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 316681,
    "published_at": "2026-07-01T09:35:43+00:00",
    "summary": "Claude Code 封号原因终于找到了！国外开发者逆向 Claude Code 源码，发现 Anthropic 在客户端里藏了一套隐蔽的用户标记系统，这期视频带你完整还原封号真相。\n开源 AI 编程教程：github.com/liyupi/ai-guide\n编程学习教程+实战项目+简历模板：codefather.cn\n最近 AI 圈儿不太平啊，OpenAI Codex 封号、Cursor 地区"
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 251964,
    "published_at": "2026-04-04T15:19:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1wpTJ6yEAq",
    "domain": "AI",
    "title": "我教了140万人装ClaudeCode，现在决定暂时卸载它……",
    "url": "http://www.bilibili.com/video/av116851967270281",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 250534,
    "published_at": "2026-07-02T19:16:20+00:00",
    "summary": "拧巴啊……"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 231502,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 176203,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 168680,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 160668,
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
    "points": 158789,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 118264,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 103621,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92397,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 65500,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 62845,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 52746,
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
    "points": 41384,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1hxMbzqEzU",
    "domain": "AI",
    "title": "小智MCP自由了！我开源了个命令行神器实现多MCP聚合",
    "url": "http://www.bilibili.com/video/av114686414625640",
    "source": "闪电蘑菇",
    "platform": "bilibili",
    "points": 39819,
    "published_at": "2025-06-15T08:31:55+00:00",
    "summary": "- 我写的小智客户端命令行工具\n - github: https://github.com/shenjingnan/xiaozhi-client\n - gitee: https://gitee.com/shenjingnan/xiaozhi-client\n\n- 小智官方MCP示例代码仓库：\n - github: https://github.com/78/mcp-calculator\n - git"
  },
  {
    "id": "bvid:BV1ap2fBvEt9",
    "domain": "AI",
    "title": "如何使用「Operit AI」：你的下一代AI手机助手",
    "url": "http://www.bilibili.com/video/av115677243447909",
    "source": "默睦",
    "platform": "bilibili",
    "points": 35353,
    "published_at": "2025-12-07T08:06:42+00:00",
    "summary": "下载地址：https://github.com/AAswordman/Operit\n\n相关软件资料下载：https://www.123pan.com/s/IKgAjv-Hinsv.html\n\n官方交流群：458862019"
  },
  {
    "id": "bvid:BV188Tn6ZE3f",
    "domain": "AI",
    "title": "如何在地铁上VibeCoding？",
    "url": "http://www.bilibili.com/video/av116851229071296",
    "source": "子杰Kyro",
    "platform": "bilibili",
    "points": 32070,
    "published_at": "2026-07-02T16:14:15+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29889,
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
    "points": 28708,
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
    "points": 24760,
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
    "points": 22595,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1qDMw6xE1J",
    "domain": "AI",
    "title": "【坦克世界】整个服务器就我一个不开桂么？",
    "url": "http://www.bilibili.com/video/av116861060650248",
    "source": "胖丁咸宁七",
    "platform": "bilibili",
    "points": 20905,
    "published_at": "2026-07-04T09:56:11+00:00",
    "summary": "剪辑员:@0筒隐月子0  \n投稿邮箱1149241078@qq.com 大家有什么有趣的素材什么类型的都可以收！\n直播地址 https://live.bilibili.com/1620209 周二~周日晚8-凌晨2点准时直播！周一休息！\n粉丝一群：559726097 粉丝二群：613247655"
  },
  {
    "id": "bvid:BV1CnTh6yEzd",
    "domain": "AI",
    "title": "Claude官方刚发布的科研神器Claude Science，科研效率直接起飞！",
    "url": "http://www.bilibili.com/video/av116840541984361",
    "source": "旭光升",
    "platform": "bilibili",
    "points": 19006,
    "published_at": "2026-06-30T18:48:21+00:00",
    "summary": "就在刚刚，Anthropic正式发布了专为科研人员打造的AI工具——Claude Science！\n视频里第一时间带大家看了这个工具的核心功能：\n 1️⃣ 内置科学渲染器，可直接查看蛋白质结构和分子，结果可复现并追溯到代码\n 2️⃣ 内置持续化Python/R内核，未来或许不再需要单独打开RStudio\n 3️⃣ 可连接本地电脑或GPU/HPC集群，自动构建环境、管理计算任务\n 4️⃣ 主打单细胞"
  },
  {
    "id": "bvid:BV1cCEi6sEU5",
    "domain": "AI",
    "title": "🦊他能成功吗？Claude Code 接管虚幻引擎5，打造一款游戏 | 带你走完整个流程",
    "url": "http://www.bilibili.com/video/av116731724959171",
    "source": "Apeak_虚幻丰哥",
    "platform": "bilibili",
    "points": 17330,
    "published_at": "2026-06-11T13:41:36+00:00",
    "summary": "Claude Code 接管虚幻引擎5，打造了一款游戏\n下载我的 CLAUDE.md（帮你省 token 的配置）\n链接：https://pan.quark.cn/s/b6e50b4b2535\n提取码：tbaE\nStefan 3D AI ：https://www.youtube.com/watch?v=iRcrZjOt5H8&amp;t=1s\n🔗 完整教程指南和链接：https://www.top"
  },
  {
    "id": "bvid:BV1JU7E6PEar",
    "domain": "AI",
    "title": "Cursor 已死？我为什么要退订 Cursor ？",
    "url": "http://www.bilibili.com/video/av116819553683121",
    "source": "小狗瑞恩Ryan",
    "platform": "bilibili",
    "points": 16181,
    "published_at": "2026-06-27T01:52:00+00:00",
    "summary": "当了一年多的 Cursor 重度用户，最近把它退订了。\n\n不是它变差了，是 Claude Code 和 Codex 真的太好用了。\n\n几个真实感受： ① 大模型越来越强，我已经不怎么手写代码了 ② Cursor 套的是 VS Code 壳子，只属于程序员 ③ 底层模型不在一个量级——Claude 有 Opus 和 Fable 5，Codex 有 GPT 5.5/5.6，Cursor 的 Compo"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 14764,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV1LWTe6gEVc",
    "domain": "AI",
    "title": "Claude code帮我实现综述论文自由！",
    "url": "http://www.bilibili.com/video/av116842504918580",
    "source": "做科研的大师兄",
    "platform": "bilibili",
    "points": 14720,
    "published_at": "2026-07-01T03:07:40+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV14cZqB8EBY",
    "domain": "AI",
    "title": "AI攻克不了的领域竟然是它？揭秘CNC编程为何让AI束手无策",
    "url": "http://www.bilibili.com/video/av116097411976217",
    "source": "极微视界",
    "platform": "bilibili",
    "points": 13980,
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
    "points": 13157,
    "published_at": "2025-12-29T14:51:53+00:00",
    "summary": "本期影片分享一下如何利用cloudflare workers搭建网站，并且利用d1免费数据库，实现无服务器的一个带前后端功能的网站。也就是说，即使你没有服务器，也能够搭建一个属于自己的网站。比如我自己搭建的这个案例网站在线留言板。就是完全搭建在cloudflare workers上面的，里面有静态页面 也有动态api接口。都是部署在workers上面的，并且集成了它提供的数据库。\n\n\n#cloud"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "穷在街头无人问lhj",
    "platform": "bilibili",
    "points": 12088,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1etEQ6DETs",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116724192118321",
    "source": "AI产品经理大模型",
    "platform": "bilibili",
    "points": 11963,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1XaE96REta",
    "domain": "AI",
    "title": "【2026最新版】这绝对是B站唯一将MCP入门+实战讲明白的教程，手把手带你从入门到代码实战开发，存下吧，比啃书好太多了！学完即就业，让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116725047625978",
    "source": "ollama本地部署",
    "platform": "bilibili",
    "points": 10541,
    "published_at": "2026-06-10T09:22:30+00:00",
    "summary": "视频配套的学习资料已经整理好了，如需领取戳👉https://b23.tv/Qdi8fs5\n无论是新手小白，还是有一定编码经验的选手，皆可学习"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 9665,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9151,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 8420,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV1DXTY6hEPv",
    "domain": "AI",
    "title": "Claude国内注册防封号：直接订阅Claude API｜Claude Pro/Max三种订阅方法，封号后如何退款？国内接码+微信支付开通，玩转Opus 4.8",
    "url": "http://www.bilibili.com/video/av116843108964309",
    "source": "Ai实测官",
    "platform": "bilibili",
    "points": 7864,
    "published_at": "2026-07-01T12:00:00+00:00",
    "summary": "Claude国内注册订阅全流程！接码、微信支付、防封号一条视频讲清楚，无需信用卡和美区ID。本期实测三种订阅方法（WildAI第三方/苹果礼品卡/Google Play），并独家对比封号后能否拿到官方退款——真金白银踩坑总结。\n直接订阅Claude 官方API才是防封号最好的方法。触发pro/max封号的机制在这里都不算数。\n新手也能跟着开通Claude Pro/Max，玩转Opus 4.8、Cl"
  },
  {
    "id": "bvid:BV191TY6KEHk",
    "domain": "AI",
    "title": "【全500集】目前B站最全最细的AI Agent零基础全套教程（从入门到精通），5天从入门到精通AI Agent，学完即可就业！看完这一套Agent教程就够了！",
    "url": "http://www.bilibili.com/video/av116843192851440",
    "source": "Agent智能体-",
    "platform": "bilibili",
    "points": 7577,
    "published_at": "2026-07-01T06:09:09+00:00",
    "summary": "【全500集】目前B站最全最细的AI Agent零基础全套教程（从入门到精通），5天从入门到精通AI Agent，学完即可就业！看完这一套AI Agent教程就够了！"
  },
  {
    "id": "bvid:BV18qz9BNECx",
    "domain": "AI",
    "title": "嵌入式开发新玩法！大材小用Claude Code ，STM32 点灯，告别手写代码",
    "url": "http://www.bilibili.com/video/av115972958651618",
    "source": "SparkLab-AI嵌入式",
    "platform": "bilibili",
    "points": 6680,
    "published_at": "2026-01-28T13:32:34+00:00",
    "summary": "SparkLab｜Claude Code 嵌入式实战第一弹：零基础用 AI 一键生成 STM32 工程，轻松点亮 LED，手把手演示全程操作，新手也能跟着做～关注解锁更多 AI 写嵌入式代码技巧，评论区蹲 Prompt 的朋友扣【AI 点灯】！\n#AI 嵌入式 #ClaudeCode #STM32 点灯"
  },
  {
    "id": "rss:https://www.eetimes.com/inside-infineon-e5b-dresden-fab-virtual-fab-cloning-fast-tracked-the-launch/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside Infineon’s €5B Dresden Fab: Virtual Fab Cloning Fast-Tracked the Launch",
    "url": "https://www.eetimes.com/inside-infineon-e5b-dresden-fab-virtual-fab-cloning-fast-tracked-the-launch/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T10:40:05+00:00",
    "summary": "At the opening of its Dresden smart power fab, Infineon’s COO said virtual fab cloning enabled delivery three months ahead of schedule. The post Inside Infineon&#8217;s €5B Dresden Fab: Virtual Fab Cl"
  },
  {
    "id": "rss:https://www.eetimes.com/sk-hynix-plans-713b-domestic-investment/",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix Plans $713B Domestic Investment",
    "url": "https://www.eetimes.com/sk-hynix-plans-713b-domestic-investment/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T13:57:51+00:00",
    "summary": "SK hynix is set to invest $713 billion to expand its semiconductor manufacturing capacity in South Korea and plans a Nasdaq listing. The post SK hynix Plans $713B Domestic Investment appeared first on"
  },
  {
    "id": "rss:https://www.eetimes.com/spains-semiconductor-landscape-six-stories-from-a-growing-ecosystem/",
    "domain": "AI 算力 / 半导体",
    "title": "Spain’s Semiconductor Landscape: Six Stories from a Growing Ecosystem",
    "url": "https://www.eetimes.com/spains-semiconductor-landscape-six-stories-from-a-growing-ecosystem/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T07:10:19+00:00",
    "summary": "EE Times examines the companies, institutes, and policy initiatives positioning Spain within Europe’s next wave of semiconductor innovation. The post Spain’s Semiconductor Landscape: Six Stories from "
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/50-feet-long-fiber-optic-hdmi-cable-and-steam-controller-2-is-enthusiasts-answer-to-the-steam-machine-dismisses-valves-new-console-for-a-diy-bazzite-setup-with-a-controller",
    "domain": "AI 算力 / 半导体",
    "title": "50-feet-long fiber optic HDMI cable and Steam Controller 2 is enthusiasts' answer to the Steam Machine — dismisses Valve's new console for a DIY Bazzite setup with a controller",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/50-feet-long-fiber-optic-hdmi-cable-and-steam-controller-2-is-enthusiasts-answer-to-the-steam-machine-dismisses-valves-new-console-for-a-diy-bazzite-setup-with-a-controller",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T16:58:51+00:00",
    "summary": "An enthusiast is DIYing his own Steam Machine through ancient, lost methods known as cables that turn his existing PC into the perfect couch gaming setup. As expected, the Steam Controller 2 is also i"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/sony-crammed-an-entire-ps1-into-a-dualshock-controller-that-connects-to-your-tv-but-killed-the-project-playstation-puga-offered-game-studios-a-mere-10-cents-per-unit-sold",
    "domain": "AI 算力 / 半导体",
    "title": "Sony crammed an entire PS1 into a DualShock controller that connects to your TV, but killed the project — PlayStation Puga offered game studios a mere 10 cents per unit sold",
    "url": "https://www.tomshardware.com/video-games/console-gaming/sony-crammed-an-entire-ps1-into-a-dualshock-controller-that-connects-to-your-tv-but-killed-the-project-playstation-puga-offered-game-studios-a-mere-10-cents-per-unit-sold",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T15:16:24+00:00",
    "summary": "Sony successfully built a PlayStation 1 console that fit inside a controller but had to cancel the project after game studios were unhappy with the royalties they would make from the project."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/chinese-ymtc-ssds-make-their-way-into-retail-lenovo-laptops-media-outlet-slams-ymtc-pcie-4-0-drive-for-below-average-for-an-ssd-in-an-office-laptop-in-review",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese YMTC SSDs make their way into retail Lenovo laptops — media outlet slams YMTC PCIe 4.0 drive for 'below average for an SSD in an office laptop' in review",
    "url": "https://www.tomshardware.com/pc-components/ssds/chinese-ymtc-ssds-make-their-way-into-retail-lenovo-laptops-media-outlet-slams-ymtc-pcie-4-0-drive-for-below-average-for-an-ssd-in-an-office-laptop-in-review",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T15:07:08+00:00",
    "summary": "Lenovo has seemingly begun using YMTC SSDs in some of its laptop models, allowing the Chinese storage chip company to gain a foothold in the U.S. This is despite its inclusion on the U.S. Department o"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/get-a-premium-27-inch-1440p-240-hz-oled-gaming-monitor-for-only-usd349-oled-for-the-price-of-ips",
    "domain": "AI 算力 / 半导体",
    "title": "Get a premium 27-inch 1440p 240 Hz OLED gaming monitor for only $349 — OLED for the price of IPS",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/get-a-premium-27-inch-1440p-240-hz-oled-gaming-monitor-for-only-usd349-oled-for-the-price-of-ips",
    "source": "Anj Bryant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T14:16:28+00:00",
    "summary": "If you've been meaning to upgrade to an OLED monitor but budget options scare you off because of burn-in, Asus has the answer for you. Not only does this monitor feature great specs, but it also has a"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/cheyenne-suspends-data-center-fill-and-flush-and-closed-loop-discharges-after-meta-contractor-contaminated-its-reuse-water-system",
    "domain": "AI 算力 / 半导体",
    "title": "Meta data center water discharges suspended after contaminating the city's reclamation water supply with bacterium — system offline for months for cleaning, closed-loop cooling system purge spread rar",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/cheyenne-suspends-data-center-fill-and-flush-and-closed-loop-discharges-after-meta-contractor-contaminated-its-reuse-water-system",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T14:02:22+00:00",
    "summary": "Fill-and-flush is a commissioning step whereby crews fill a cooling loop's piping with water and flush it to clear debris before the system is run."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/aoc-u27g4xm-27-inch-4k-160-hz-dual-refresh-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "AOC U27G4XM 27-inch 4K 160 Hz Dual-Refresh Gaming Monitor Review: Speed, Flexibility And Value",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/aoc-u27g4xm-27-inch-4k-160-hz-dual-refresh-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T13:17:31+00:00",
    "summary": "AOC brings speed, flexibility, and value in its U27G4XM. It’s a 27-inch dual-mode IPS panel with 4K resolution at 160 Hz, FHD resolution at 320 Hz and Adaptive-Sync. It also has a Mini LED backlight w"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/memory-price-surge-begins-to-cool-as-consumers-hit-affordability-limit-ai-demand-still-keeps-dram-and-nand-prices-climbing-through-q3-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Memory price surge begins to cool as consumers hit affordability limit — AI demand still keeps DRAM and NAND prices climbing through Q3 2026",
    "url": "https://www.tomshardware.com/pc-components/ram/memory-price-surge-begins-to-cool-as-consumers-hit-affordability-limit-ai-demand-still-keeps-dram-and-nand-prices-climbing-through-q3-2026",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T11:47:34+00:00",
    "summary": "TrendForce says DRAM and NAND prices will continue to rise through Q3 2026, but AI-driven gains are slowing as PC and smartphone makers reach their affordability limits."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/the-ultimate-4k-rtx-5090-gaming-titan-plummets-usd2-580-huge-discount-makes-the-alienware-area-51-with-24-core-cpu-and-64gb-ram-irresistible",
    "domain": "AI 算力 / 半导体",
    "title": "The ultimate 4K RTX 5090 gaming titan plummets $2,580 — huge discount makes the Alienware Area-51 with 24-core CPU and 64GB RAM irresistible",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/the-ultimate-4k-rtx-5090-gaming-titan-plummets-usd2-580-huge-discount-makes-the-alienware-area-51-with-24-core-cpu-and-64gb-ram-irresistible",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T11:43:13+00:00",
    "summary": "Dell has slashed the price of the Alienware Area-51 with a Core Ultra 9 285K, GeForce RTX 5090, and 64GB of DDR5 RAM by $2,580."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/windows-guru-uses-stirling-engine-to-cool-amd-threadripper-3970x-waste-heat-energy-spins-the-engines-flywheel",
    "domain": "AI 算力 / 半导体",
    "title": "Windows guru uses 19th-century Stirling Engine tech for auxiliary cooling on AMD Threadripper 3970X system — waste heat energy spins the $40 engine's flywheel",
    "url": "https://www.tomshardware.com/pc-components/cooling/windows-guru-uses-stirling-engine-to-cool-amd-threadripper-3970x-waste-heat-energy-spins-the-engines-flywheel",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T11:30:00+00:00",
    "summary": "Windows development guru Dave W. Plummer shared a brief video demonstrating a novel Stirling Engine powered cooling solution for his AMD Threadripper chipset."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/enthusiast-hides-gaming-pc-inside-living-room-fan-using-3d-printed-parts-disassembled-atomman-g7-cooled-by-dreo-tower-fan-that-shifts-air-at-28-feet-per-second",
    "domain": "AI 算力 / 半导体",
    "title": "Enthusiast hides gaming PC inside living room fan using 3D-printed parts — disassembled AtomMan G7 cooled by Dreo tower fan that shifts air at 28 feet per second",
    "url": "https://www.tomshardware.com/3d-printing/enthusiast-hides-gaming-pc-inside-living-room-fan-using-3d-printed-parts-disassembled-atomman-g7-cooled-by-dreo-tower-fan-that-shifts-air-at-28-feet-per-second",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T11:00:00+00:00",
    "summary": "Creator Zac Builds mounted their mini-PC to the side of their living room fan to hide it plain sight."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/startup-unveils-3d-printed-nuclear-reactor-module-to-power-ai-data-centers-touted-as-the-worlds-first-subcritical-solid-state-factory-built-thorium-nuclear-reactor",
    "domain": "AI 算力 / 半导体",
    "title": "Startup unveils 3D-printed nuclear reactor module to power AI data centers —touted as ‘the world’s first subcritical, solid-state, factory-built thorium nuclear reactor’",
    "url": "https://www.tomshardware.com/3d-printing/startup-unveils-3d-printed-nuclear-reactor-module-to-power-ai-data-centers-touted-as-the-worlds-first-subcritical-solid-state-factory-built-thorium-nuclear-reactor",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T11:00:00+00:00",
    "summary": "Nuclear tech startup Ampera revealed a small modular reactor manufactured using 3D printing techniques. The company says that it expects to be the first one to mass produce these power sources for dat"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/fire-hydrant-signs-with-starlink-antennas-tested-for-emergency-wi-fi-in-disaster-prone-japan-existing-widespread-grid-of-street-level-furniture-can-be-used-for-communications-network-fallback",
    "domain": "AI 算力 / 半导体",
    "title": "Fire hydrant signs with Starlink antennas tested for emergency Wi-Fi in disaster-prone Japan— existing widespread grid of street-level furniture can be used for communications network fallback",
    "url": "https://www.tomshardware.com/networking/fire-hydrant-signs-with-starlink-antennas-tested-for-emergency-wi-fi-in-disaster-prone-japan-existing-widespread-grid-of-street-level-furniture-can-be-used-for-communications-network-fallback",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T10:00:00+00:00",
    "summary": "Japan’s Fire Hydrant Sign Co., Ltd. has demonstrated an expansive Wi-Fi network that melds its established infrastructure of street signs with Starlink satellite broadband antennas."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/companies-join-hands-to-collectively-dunk-on-playstations-all-digital-future-dominos-pizza-kfc-and-gamesir-all-threaten-an-end-to-physical-production",
    "domain": "AI 算力 / 半导体",
    "title": "Companies join hands to collectively dunk on PlayStation's all-digital future — Domino's pizza, KFC, and GameSir all threaten an end to physical production",
    "url": "https://www.tomshardware.com/tech-industry/companies-join-hands-to-collectively-dunk-on-playstations-all-digital-future-dominos-pizza-kfc-and-gamesir-all-threaten-an-end-to-physical-production",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T10:00:00+00:00",
    "summary": "Companies on social media are coming together to mock Sony's decision of ceasing production of physical discs for PlayStation games. These brands are shifting to a digital-only model in an even more a"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-keyboards/turtle-beach-kp7-review",
    "domain": "AI 算力 / 半导体",
    "title": "Turtle Beach KP7 Review: The accessory that does everything",
    "url": "https://www.tomshardware.com/peripherals/gaming-keyboards/turtle-beach-kp7-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T16:26:03+00:00",
    "summary": "Turtle Beach's KP7 keypad can be used with its KB7 keyboard or as a standalone macropad. And it's nice — but pricey."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-reportedly-adding-two-new-22-core-skus-with-game-boosting-cache-to-nova-lake-s-lineup-125w-unlocked-and-65w-locked-part-rumored-to-be-part-of-single-tile-core-ultra-5-tier",
    "domain": "AI 算力 / 半导体",
    "title": "Intel reportedly adding two new 22-core SKUs with game-boosting cache to Nova Lake-S lineup — 125W unlocked and 65W locked part rumored to be part of single-tile Core Ultra 5 tier",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-reportedly-adding-two-new-22-core-skus-with-game-boosting-cache-to-nova-lake-s-lineup-125w-unlocked-and-65w-locked-part-rumored-to-be-part-of-single-tile-core-ultra-5-tier",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T15:44:10+00:00",
    "summary": "Intel is apparently cooking up two new 22-core Nova Lake-S SKUs with up to 144MB of bLLC. One is a locked 65W variant and one is an unlocked 125W part, and both are said to be part of the Core Ultra 5"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-confirms-price-hikes-on-select-consumer-and-server-cpus-citing-supply-costs-and-demand-select-xeon-processors-now-over-usd1-000-more-expensive",
    "domain": "AI 算力 / 半导体",
    "title": "Intel confirms price hikes on select consumer and server CPUs citing supply costs and demand — select Xeon processors now over $1,000 more expensive",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-confirms-price-hikes-on-select-consumer-and-server-cpus-citing-supply-costs-and-demand-select-xeon-processors-now-over-usd1-000-more-expensive",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T14:45:33+00:00",
    "summary": "Intel confirms price increases for Core Ultra 200S Plus, Xeon 6 processors, cites market dynamics, rising costs, soaring demand."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/samsung-sk-hynix-and-micron-face-a-third-dram-price-fixing-lawsuit",
    "domain": "AI 算力 / 半导体",
    "title": "Inside the history of DRAM price-fixing lawsuits — how HBM allocations could make a difference after two decades of failed cases",
    "url": "https://www.tomshardware.com/pc-components/dram/samsung-sk-hynix-and-micron-face-a-third-dram-price-fixing-lawsuit",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T14:13:04+00:00",
    "summary": "17 plaintiffs sued Samsung, SK hynix, and Micron in the U.S. District Court for the Northern District of California in late June."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/brand-new-steam-machine-hit-with-red-line-of-death-gpu-failure-after-playing-no-mans-sky-for-just-five-minutes-console-bricked-itself-following-update-in-incident-eerily-reminiscent-of-xbox-360-launch",
    "domain": "AI 算力 / 半导体",
    "title": "Brand new Steam Machine hit with 'red line of death' GPU failure after playing No Man's Sky for just five minutes — console 'bricked itself' following update in failure that echoes the horror of the X",
    "url": "https://www.tomshardware.com/video-games/console-gaming/brand-new-steam-machine-hit-with-red-line-of-death-gpu-failure-after-playing-no-mans-sky-for-just-five-minutes-console-bricked-itself-following-update-in-incident-eerily-reminiscent-of-xbox-360-launch",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T13:58:19+00:00",
    "summary": "A Redditor experience the deadly \"Red Line of Death\" on their Steam Machine, indicating GPU failure. They've just been playing for five minutes and then updated the console before experiencing the iss"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/hp-omnibook-ultra-14-snapdragon-x2-elite-2026-review",
    "domain": "AI 算力 / 半导体",
    "title": "HP OmniBook Ultra 14 review: Potent Snapdragon performance, great endurance, premium pricing",
    "url": "https://www.tomshardware.com/laptops/hp-omnibook-ultra-14-snapdragon-x2-elite-2026-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T13:34:57+00:00",
    "summary": "HP hits the mark on performance and battery life, but you’ll pay a hefty price for its OmniBook Ultra with Qualcomm Snapdragon X2 Elite."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/blackstone-owned-qts-abandons-planned-worlds-largest-data-center-campus-after-years-of-lawsuits-2-100-acre-virginia-digital-gateway-project-dies-over-a-newspaper-notice-technicality",
    "domain": "AI 算力 / 半导体",
    "title": "Blackstone-owned QTS abandons planned world’s largest data center campus after years of lawsuits — 2,100-acre Virginia Digital Gateway project dies over a newspaper-notice technicality",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/blackstone-owned-qts-abandons-planned-worlds-largest-data-center-campus-after-years-of-lawsuits-2-100-acre-virginia-digital-gateway-project-dies-over-a-newspaper-notice-technicality",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T13:32:53+00:00",
    "summary": "Blackstone-owned QTS has withdrawn its final appeal for Virginia’s 22-million-square-foot Digital Gateway campus, ending the massive data center project."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/sk-hynix-samsung-micron-among-semiconductor-industry-group-lobbying-against-government-intervention-on-domestic-memory-chip-supply-says-move-would-worsen-situation-suggests-tax-deductions-on-consumer-electronics-instead",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix, Samsung, Micron among semiconductor industry group lobbying against government intervention on domestic memory chip supply — says move would worsen situation, suggests tax deductions on cons",
    "url": "https://www.tomshardware.com/tech-industry/sk-hynix-samsung-micron-among-semiconductor-industry-group-lobbying-against-government-intervention-on-domestic-memory-chip-supply-says-move-would-worsen-situation-suggests-tax-deductions-on-consumer-electronics-instead",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T13:17:47+00:00",
    "summary": "A lawmaker suggested to the administration that it should prioritize American manufacturers when it comes to memory chip supplies, but the SEMI industry group is pushing back against this. It says tha"
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-47-percent-on-dell-and-alienware-gaming-pcs-and-laptops-in-this-july-4th-flash-sale-big-sale-discounts-on-pricey-kit-including-gaming-chairs-and-monitors-for-a-limited-time-only",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to 47% on Dell and Alienware gaming PCs and laptops in this July 4th flash sale — big sale discounts on pricey kit including gaming chairs and monitors for a limited time only",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-47-percent-on-dell-and-alienware-gaming-pcs-and-laptops-in-this-july-4th-flash-sale-big-sale-discounts-on-pricey-kit-including-gaming-chairs-and-monitors-for-a-limited-time-only",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T13:00:00+00:00",
    "summary": "Grab a bargain on these Dell and Alienware PCs, laptops, and monitors over the July 4th holiday weekend."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-71-percent-on-hp-gaming-desktops-and-laptops-this-july-4-weekend-sale-could-land-you-a-gaming-pc-for-less",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to 71% on HP gaming desktops and laptops this July 4 — weekend sale could land you a gaming PC for less",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-71-percent-on-hp-gaming-desktops-and-laptops-this-july-4-weekend-sale-could-land-you-a-gaming-pc-for-less",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T11:49:56+00:00",
    "summary": "Get up to 71% off HP gaming desktops, laptops, and accessories this July 4."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-chairs/up-to-usd129-off-secretlab-gaming-chairs-and-desks-in-july-4-sale-save-on-the-titan-evo-magnus-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Up to $129 off Secretlab gaming chairs and desks in July 4 sale — save on the Titan Evo, Magnus, and more",
    "url": "https://www.tomshardware.com/peripherals/gaming-chairs/up-to-usd129-off-secretlab-gaming-chairs-and-desks-in-july-4-sale-save-on-the-titan-evo-magnus-and-more",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T11:13:58+00:00",
    "summary": "Save up to $129 on Secretlab gaming chairs and desks thanks to a July 4 sale."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-18a-wafer-to-wafer-yield-issues-fixed-report-claims-says-production-up-to-15-000-wafers-per-month-at-both-sites",
    "domain": "AI 算力 / 半导体",
    "title": "Intel 18A wafer-to-wafer yield issues fixed, report claims — says production up to 15,000 wafers per month at both sites",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-18a-wafer-to-wafer-yield-issues-fixed-report-claims-says-production-up-to-15-000-wafers-per-month-at-both-sites",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T10:49:40+00:00",
    "summary": "Intel reportedly solves one of the key issues that plagued its 18A process technology, but others may still be there."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/hp-has-slashed-usd1-075-off-this-rtx-5070-gaming-pc-in-its-july-4-sale-omen-35l-with-32gb-of-ram-now-just-usd1-724",
    "domain": "AI 算力 / 半导体",
    "title": "HP has slashed $1,075 off this RTX 5070 gaming PC in its July 4 sale — Omen 35L with 32GB of RAM now just $1,724",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/hp-has-slashed-usd1-075-off-this-rtx-5070-gaming-pc-in-its-july-4-sale-omen-35l-with-32gb-of-ram-now-just-usd1-724",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T10:27:57+00:00",
    "summary": "This RTX 5070 gaming PC is now just $1,724, featuring 32GB of RAM and Intel's 265F CPU."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/github-thumbs-nose-at-sonys-controversial-end-to-physical-media-with-its-introduction-of-repo-cds-offers-limited-run-of-1-000-cd-rom-copies-of-public-github-repos-for-preservation",
    "domain": "AI 算力 / 半导体",
    "title": "GitHub thumbs nose at Sony's controversial end to physical media with its introduction of Repo CDs — offers limited run of 1,000 CD-ROM copies of public GitHub repos for preservation",
    "url": "https://www.tomshardware.com/pc-components/storage/github-thumbs-nose-at-sonys-controversial-end-to-physical-media-with-its-introduction-of-repo-cds-offers-limited-run-of-1-000-cd-rom-copies-of-public-github-repos-for-preservation",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T10:27:12+00:00",
    "summary": "GitHub has announced that it will be giving developers a way to obtain their public repo on a CD-ROM. Context is provided by Sony's recent decision to abandon game discs."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/this-144-in-1-electric-screwdriver-set-is-a-must-buy-toolkit-for-pc-building-and-hobbyists-now-under-usd40-20-percent-saving-on-kit-with-a-second-precision-driver-120-magnetic-bits-and-22-maintenance-tools-for-builds-and-repairs",
    "domain": "AI 算力 / 半导体",
    "title": "This 144-in-1 electric screwdriver set is a must-buy toolkit for PC building and hobbyists, now under $40 — 20% saving on kit with a second precision driver, 120 magnetic bits, and 22 maintenance tool",
    "url": "https://www.tomshardware.com/desktops/pc-building/this-144-in-1-electric-screwdriver-set-is-a-must-buy-toolkit-for-pc-building-and-hobbyists-now-under-usd40-20-percent-saving-on-kit-with-a-second-precision-driver-120-magnetic-bits-and-22-maintenance-tools-for-builds-and-repairs",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T10:23:10+00:00",
    "summary": "Save 20% on this 144-in-1 repair toolkit from Strebito, with 120 bits and a number of other tools for less than $40."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/robotics/scientists-have-created-a-3d-printed-remote-controlled-cyborg-cockroach-equipped-with-ir-cameras-living-insects-fitted-with-flexible-diving-suit-can-survive-and-move-underwater-for-three-hours",
    "domain": "AI 算力 / 半导体",
    "title": "Scientists have created a 3D-printed remote-controlled cyborg cockroach equipped with IR cameras — living insects fitted with flexible 'diving suit' can survive and move underwater for three hours",
    "url": "https://www.tomshardware.com/tech-industry/robotics/scientists-have-created-a-3d-printed-remote-controlled-cyborg-cockroach-equipped-with-ir-cameras-living-insects-fitted-with-flexible-diving-suit-can-survive-and-move-underwater-for-three-hours",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T09:22:28+00:00",
    "summary": "Singaporean scientists outfitted remote-controlled cockroaches with scuba suits in a bid to use them in rescue operations and explore extreme environments like Mars."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/jensen-huangs-iconic-signed-leather-jacket-expected-to-fetch-up-to-usd60-000-in-charity-auction-sothebys-says-item-was-worn-at-a-foxconn-tech-day-in-2023-and-the-signature-has-been-professionally-authenticated",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang’s iconic signed leather jacket expected to fetch up to $60,000 in charity auction — Sotheby’s says item was worn at a Foxconn Tech Day in 2023 and the signature has been professionally au",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/jensen-huangs-iconic-signed-leather-jacket-expected-to-fetch-up-to-usd60-000-in-charity-auction-sothebys-says-item-was-worn-at-a-foxconn-tech-day-in-2023-and-the-signature-has-been-professionally-authenticated",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T09:12:50+00:00",
    "summary": "One of Jensen Huang’s used leather jackets is up for auction, with an estimate of $40,000 to $60,000. The money will go to charity."
  },
  {
    "id": "rss:https://www.eetimes.com/turkey-needs-to-make-its-own-chips-not-just-design-them/",
    "domain": "AI 算力 / 半导体",
    "title": "Turkey Needs to Make Its Own Chips, Not Just Design Them",
    "url": "https://www.eetimes.com/turkey-needs-to-make-its-own-chips-not-just-design-them/",
    "source": "Oğuz Ergin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T12:42:59+00:00",
    "summary": "Turkey has built a strong chip design base, but without domestic manufacturing, its semiconductor sovereignty remains on loan. The post Turkey Needs to Make Its Own Chips, Not Just Design Them appeare"
  },
  {
    "id": "rss:https://www.eetimes.com/opensearch-powers-ai-data-infrastructure-as-agentic-workloads-scale/",
    "domain": "AI 算力 / 半导体",
    "title": "OpenSearch Powers AI Data Infrastructure as Agentic Workloads Scale",
    "url": "https://www.eetimes.com/opensearch-powers-ai-data-infrastructure-as-agentic-workloads-scale/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T07:40:09+00:00",
    "summary": "OpenSearch turns AI’s data deluge into hybrid search, observability, and agent monitoring while avoiding vendor lock-in. The post OpenSearch Powers AI Data Infrastructure as Agentic Workloads Scale ap"
  },
  {
    "id": "rss:https://www.eetimes.com/engineering-heterogeneity-at-scale/",
    "domain": "AI 算力 / 半导体",
    "title": "Engineering Heterogeneity at Scale",
    "url": "https://www.eetimes.com/engineering-heterogeneity-at-scale/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T20:49:24+00:00",
    "summary": "AI has outgrown traditional chips. The future belongs to integrated systems that stack compute, memory, photonics, and power, and HLSI is driving the shift. The post Engineering Heterogeneity at Scale"
  },
  {
    "id": "rss:https://www.eetimes.com/design-of-a-single-pair-ethernet-system-with-power-over-data-lines-spoe/",
    "domain": "AI 算力 / 半导体",
    "title": "Design of a Single Pair Ethernet System with Power over Data Lines (SPoE)",
    "url": "https://www.eetimes.com/design-of-a-single-pair-ethernet-system-with-power-over-data-lines-spoe/",
    "source": "Dr.-Ing. Heinz Zenkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T14:00:00+00:00",
    "summary": "Single Pair Ethernet is becoming increasingly popular in industrial networking due to the simplified cabling with just one twisted pair of wires. If power is also supplied via this, the SPE transmissi"
  },
  {
    "id": "rss:https://www.eetimes.com/oxmiq-raises-35m-for-gpu-ip-expands-focus-to-data-center-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Oxmiq Raises $35M for GPU IP, Expands Focus to Data Center Design",
    "url": "https://www.eetimes.com/oxmiq-raises-35m-for-gpu-ip-expands-focus-to-data-center-design/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T13:15:00+00:00",
    "summary": "OxCore GPU IP is up and running on FPGA today, CEO Raja Koduri told EE Times. The post Oxmiq Raises $35M for GPU IP, Expands Focus to Data Center Design appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/rapid-component-obsolescence-is-reshaping-todays-semiconductor-procurement-dynamics/",
    "domain": "AI 算力 / 半导体",
    "title": "Rapid Component Obsolescence Is Reshaping Today’s Semiconductor Procurement Dynamics",
    "url": "https://www.eetimes.com/rapid-component-obsolescence-is-reshaping-todays-semiconductor-procurement-dynamics/",
    "source": "Landyn Murphy, Senior Content Marketing Specialist, Rochester Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T13:00:00+00:00",
    "summary": "Today’s semiconductor component&#160;landscape is more complex than ever. Obsolescence has shifted from an occasional disruption to a persistent operational risk. As product lifecycles shorten and sup"
  },
  {
    "id": "rss:https://www.eetimes.com/sales-forecasting-guide-for-electronics-manufacturing-smbs/",
    "domain": "AI 算力 / 半导体",
    "title": "Sales Forecasting Guide for Electronics Manufacturing SMBs",
    "url": "https://www.eetimes.com/sales-forecasting-guide-for-electronics-manufacturing-smbs/",
    "source": "MRPeasy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T13:00:00+00:00",
    "summary": "Sales forecasting helps manufacturers estimate future demand so they can plan production, purchasing, and capacity before customer orders become urgent. The post Sales Forecasting Guide for Electronic"
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
    "id": "rss:https://www.theverge.com/science/961459/nasa-emergency-save-swift-observatory-katalyst-space-technologies",
    "domain": "大厂 AI 动态",
    "title": "NASA launched an emergency mission to stop the Swift Observatory from crashing to Earth",
    "url": "https://www.theverge.com/science/961459/nasa-emergency-save-swift-observatory-katalyst-space-technologies",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T19:06:27+00:00",
    "summary": "The Swift Observatory was launched in 2004, but recent solar storms have pushed its orbit lower, and it's in danger of burning up in Earth's atmosphere as soon as this year. To try and stave off its d"
  },
  {
    "id": "rss:https://www.theverge.com/policy/961449/white-house-mamdani-heatwave-deletion",
    "domain": "大厂 AI 动态",
    "title": "White House deletes thousands of web pages about energy conservation as heatwave slams US",
    "url": "https://www.theverge.com/policy/961449/white-house-mamdani-heatwave-deletion",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T16:19:06+00:00",
    "summary": "The US Department of Energy reportedly deleted about 6,000 pages related to energy conservation as a historic heatwave tears across the country. The deletion was suspiciously timed, following Republic"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/960753/matic-robot-vacuum-mop-price-increase-cost-buy",
    "domain": "大厂 AI 动态",
    "title": "Matic’s robot vacuum is getting a $250 price hike in September",
    "url": "https://www.theverge.com/gadgets/960753/matic-robot-vacuum-mop-price-increase-cost-buy",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T16:00:00+00:00",
    "summary": "The Matic is our favorite robot vacuum by a pretty comfortable margin. If you&#8217;ve been thinking about buying one, you may want to plan on doing it sooner than later. The company will raise its pr"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/960958/flatbush-zombies-erick-the-architect-interview",
    "domain": "大厂 AI 动态",
    "title": "Flatbush Zombies’ Erick the Architect misses his BlackBerry keyboard",
    "url": "https://www.theverge.com/entertainment/960958/flatbush-zombies-erick-the-architect-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T15:00:00+00:00",
    "summary": "Erick the Architect is a founding member of, and the primary producer for, the legendary Flatbush Zombies. He's toured the world, performed on Kimmel and Fallon, played Coachella, and collaborated wit"
  },
  {
    "id": "rss:https://www.theverge.com/tech/960837/epomaker-rt98-mechanical-keyboard-modular-numpad-review",
    "domain": "大厂 AI 动态",
    "title": "Hey number pad lovers, this is a keyboard we can finally agree on",
    "url": "https://www.theverge.com/tech/960837/epomaker-rt98-mechanical-keyboard-modular-numpad-review",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T14:00:00+00:00",
    "summary": "I know a vocal group of people who swear by the number pad on their keyboard. And yet, for years I haven't cared about using one - until I put my hands on the Epomaker RT98. It's a mechanical keyboard"
  },
  {
    "id": "rss:https://www.theverge.com/tech/960509/ikko-mindone-pro-hands-on",
    "domain": "大厂 AI 动态",
    "title": "The square-ish phone that I wanted to love",
    "url": "https://www.theverge.com/tech/960509/ikko-mindone-pro-hands-on",
    "source": "Allison Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T13:00:00+00:00",
    "summary": "The Ikko MindOne Pro is delightfully small. I keep calling it a square phone, which isn't quite right; the screen is square, but the phone itself is slightly rectangular. The camera flips up so you ca"
  },
  {
    "id": "rss:https://www.theverge.com/tech/960854/ai-fanfiction-ao3-claude-detector",
    "domain": "大厂 AI 动态",
    "title": "The fanfiction community is at war with AI — and itself",
    "url": "https://www.theverge.com/tech/960854/ai-fanfiction-ao3-claude-detector",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T12:00:00+00:00",
    "summary": "Over the past week, a new fanworks movement has kicked off, with the aim to root out authors using generative AI. But the detection methods being implemented are questionable, and any fanfic writer co"
  },
  {
    "id": "rss:https://www.theverge.com/tech/961332/qi-active-cooling-really-works",
    "domain": "大厂 AI 动态",
    "title": "Qi fan fan",
    "url": "https://www.theverge.com/tech/961332/qi-active-cooling-really-works",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T07:00:00+00:00",
    "summary": "Despite my initial skepticism, I'm now sold on wireless Qi chargers that add integrated fans to keep your phone cool while charging. I figured they'd be too loud, or too weak, or too gimmicky, but I'm"
  },
  {
    "id": "rss:https://www.theverge.com/tech/961387/amazon-2023-fire-hd-10-tablet-4gb-update",
    "domain": "大厂 AI 动态",
    "title": "Amazon updated 2023’s Fire HD 10 tablet with 4GB of RAM",
    "url": "https://www.theverge.com/tech/961387/amazon-2023-fire-hd-10-tablet-4gb-update",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T17:33:55+00:00",
    "summary": "The Fire HD 8 that launched in 2024 was the last new addition to Amazon's budget-minded tablet lineup, but the company has quietly updated the Fire HD 10 that debuted the year before. In 2023 it was o"
  },
  {
    "id": "rss:https://www.theverge.com/policy/961004/world-cup-america-250-surveillance-drones-cameras",
    "domain": "大厂 AI 动态",
    "title": "While you’re watching the World Cup, the feds may be watching you",
    "url": "https://www.theverge.com/policy/961004/world-cup-america-250-surveillance-drones-cameras",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T15:00:00+00:00",
    "summary": "It's a big year for America. It's the semiquincentennial, otherwise known as America250, and the United States is cohosting the World Cup. But spectators at these events - and the millions of people w"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/04/new-google-commercial-imagines-a-declaration-of-independence-written-with-help-from-ai/",
    "domain": "大厂 AI 动态",
    "title": "New Google commercial imagines a Declaration of Independence written with help from AI",
    "url": "https://techcrunch.com/2026/07/04/new-google-commercial-imagines-a-declaration-of-independence-written-with-help-from-ai/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T20:55:25+00:00",
    "summary": "Two hundred and fifty years after the signing of the Declaration of Independence, a new commercial asks: What if the Founding Fathers had access to Google Workspace?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/04/midjourney-wants-hollywood-studios-to-reveal-the-details-of-their-ai-usage/",
    "domain": "大厂 AI 动态",
    "title": "Midjourney wants Hollywood studios to reveal the details of their AI usage",
    "url": "https://techcrunch.com/2026/07/04/midjourney-wants-hollywood-studios-to-reveal-the-details-of-their-ai-usage/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T18:00:05+00:00",
    "summary": "As part of an ongoing legal dispute with three Hollywood studios, Midjourney is seeking to compel those studios to reveal how they use AI themselves."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/04/alibaba-reportedly-bans-employees-from-using-claude-code/",
    "domain": "大厂 AI 动态",
    "title": "Alibaba reportedly bans employees from using Claude Code",
    "url": "https://techcrunch.com/2026/07/04/alibaba-reportedly-bans-employees-from-using-claude-code/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T16:32:08+00:00",
    "summary": "Alibaba has reportedly classified Claude Code as high-risk software."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/04/what-is-mistral-ai-everything-to-know-about-the-openai-competitor/",
    "domain": "大厂 AI 动态",
    "title": "What is Mistral AI? Everything to know about the OpenAI competitor",
    "url": "https://techcrunch.com/2026/07/04/what-is-mistral-ai-everything-to-know-about-the-openai-competitor/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T15:51:32+00:00",
    "summary": "Mistral AI, which offers some open source AI models, has raised significant funding since its creation in 2023, with the ambition to “put frontier AI in the hands of everyone.”"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/03/artificial-intelligence-definition-glossary-hallucinations-guide-to-common-ai-terms/",
    "domain": "大厂 AI 动态",
    "title": "The only AI glossary you’ll need this year",
    "url": "https://techcrunch.com/2026/07/03/artificial-intelligence-definition-glossary-hallucinations-guide-to-common-ai-terms/",
    "source": "Natasha Lomas, Romain Dillet, Kyle Wiggers, Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T21:20:00+00:00",
    "summary": "The rise of AI has brought an avalanche of new terms and slang. Here is a glossary with definitions of some of the most important words and phrases you might encounter."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/03/as-the-browser-wars-heat-up-here-are-the-hottest-alternatives-to-chrome-and-safari-in-2026/",
    "domain": "大厂 AI 动态",
    "title": "The browser wars aren’t about search anymore — here are the best alternatives to Chrome and Safari",
    "url": "https://techcrunch.com/2026/07/03/as-the-browser-wars-heat-up-here-are-the-hottest-alternatives-to-chrome-and-safari-in-2026/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T18:43:00+00:00",
    "summary": "We’ve compiled an overview of some of the top alternative browsers available today aiming to challenge Chrome and Safari."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/03/the-dune-keypad-device-can-be-your-meeting-controller-and-more/",
    "domain": "大厂 AI 动态",
    "title": "The Dune keypad device can be your meeting controller and more",
    "url": "https://techcrunch.com/2026/07/03/the-dune-keypad-device-can-be-your-meeting-controller-and-more/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T18:28:30+00:00",
    "summary": "The gadget has three buttons, and it changes context based on what app you are looking at. For instance, in meeting apps and sites, it could be toggle mic, toggle video, and bring window to the front."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/03/chevy-built-an-all-american-ev-truck-why-is-nobody-buying-it/",
    "domain": "大厂 AI 动态",
    "title": "Chevy built an all-American EV truck — why is nobody buying it?",
    "url": "https://techcrunch.com/2026/07/03/chevy-built-an-all-american-ev-truck-why-is-nobody-buying-it/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T16:30:00+00:00",
    "summary": "The Chevy Silverado EV is a solid first draft of an EV pickup truck. Here's what could make it better."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/07/review-supergirl-is-not-the-disaster-its-low-box-office-suggests/",
    "domain": "大厂 AI 动态",
    "title": "Review: Supergirl is not the disaster its low box office suggests",
    "url": "https://arstechnica.com/culture/2026/07/review-supergirl-is-not-the-disaster-its-low-box-office-suggests/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T16:49:14+00:00",
    "summary": "It’s a pretty good movie, but it needed to be a great movie to thrive in an oversaturated superhero market."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/when-the-ability-to-smell-goes-away/",
    "domain": "大厂 AI 动态",
    "title": "When the ability to smell goes away",
    "url": "https://arstechnica.com/science/2026/07/when-the-ability-to-smell-goes-away/",
    "source": "Victoria Clayton, Knowable Magazine",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T11:04:31+00:00",
    "summary": "Disturbances in this critical sense are often linked to problems with brain health."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/a-martian-rock-has-lots-of-carbon-on-it-and-its-not-clear-why/",
    "domain": "大厂 AI 动态",
    "title": "A martian rock has lots of carbon on it, and it's not clear why",
    "url": "https://arstechnica.com/science/2026/07/a-martian-rock-has-lots-of-carbon-on-it-and-its-not-clear-why/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T11:00:41+00:00",
    "summary": "Biology could explain the find, but there are other potential explanations."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/rocket-report-indian-startup-nears-first-launch-spacexs-millenary-milestone/",
    "domain": "大厂 AI 动态",
    "title": "Rocket Report: Indian startup nears first launch; SpaceX's millenary milestone",
    "url": "https://arstechnica.com/space/2026/07/rocket-report-indian-startup-nears-first-launch-spacexs-millenary-milestone/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T13:55:35+00:00",
    "summary": "NASA awarded Rocket Lab deals for three dedicated launches using the company's Electron rocket."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/07/inside-the-luddite-festival-harnessing-gen-zs-rage-against-big-tech/",
    "domain": "大厂 AI 动态",
    "title": "Inside the Luddite festival harnessing Gen Z’s rage against Big Tech",
    "url": "https://arstechnica.com/culture/2026/07/inside-the-luddite-festival-harnessing-gen-zs-rage-against-big-tech/",
    "source": "Vittoria Elliott, WIRED.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T12:00:36+00:00",
    "summary": "New York City’s Summer of Ludd festival is teaching people how to live offline."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/07/at-250-years-there-are-still-reasons-for-hope-in-america/",
    "domain": "大厂 AI 动态",
    "title": "Despite the darkness, I still see signs of hope in America",
    "url": "https://arstechnica.com/culture/2026/07/at-250-years-there-are-still-reasons-for-hope-in-america/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T11:30:22+00:00",
    "summary": "It's difficult to pinpoint the moment in my life where America started to lose the plot."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/07/smithsonian-starstruck-vr-exhibit-lets-you-stroll-through-the-stars/",
    "domain": "大厂 AI 动态",
    "title": "Visiting the stars (and planets, and telescopes) in VR",
    "url": "https://arstechnica.com/culture/2026/07/smithsonian-starstruck-vr-exhibit-lets-you-stroll-through-the-stars/",
    "source": "Rob Pegoraro",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T11:15:35+00:00",
    "summary": "Walkthrough experience includes visits to stars, exoplanets, and observatories."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/07/wing-commander-iv-and-the-fmv-future-that-never-quite-was/",
    "domain": "大厂 AI 动态",
    "title": "Wing Commander IV and the FMV future that never quite was",
    "url": "https://arstechnica.com/gaming/2026/07/wing-commander-iv-and-the-fmv-future-that-never-quite-was/",
    "source": "Lee Hutchinson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T11:03:39+00:00",
    "summary": "C:\\ArsGames takes a look at the time Chris Roberts more or less made a whole movie."
  },
  {
    "id": "rss:https://www.producthunt.com/products/checklistfox",
    "domain": "大厂 AI 动态",
    "title": "ChecklistFox",
    "url": "https://www.producthunt.com/products/checklistfox",
    "source": "Usama Khalid",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T20:40:09+00:00",
    "summary": "AI checklist maker for beautiful pdfs, free & instant Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/termi-protocol",
    "domain": "大厂 AI 动态",
    "title": "Termi Protocol",
    "url": "https://www.producthunt.com/products/termi-protocol",
    "source": "Eric Omer Ercan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T21:14:15+00:00",
    "summary": "Watch your AI coding agents build, live in 3D Discussion | Link"
  },
  {
    "id": "rss:https://36kr.com/p/3882365879005186?f=rss",
    "domain": "大厂 AI 动态",
    "title": "硬氪首发 | 港大教授成立的忆生科技获数亿天使轮融资，致力于为机器人造一套记忆系统",
    "url": "https://36kr.com/p/3882365879005186?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T06:27:30+00:00",
    "summary": "作者&nbsp;|&nbsp;邱晓芬 编辑&nbsp;|&nbsp;袁斯来 硬氪获悉，「忆生科技」（TranscEngram）完成数亿元天使轮融资，本轮投资方阵容横跨产业资本与国资平台，包括正大旗下中生制药、浦东创投、张江科投、张江高科、弘信电子、云晖资本、沃肯资本、金舵资本等。 「忆生科技」致力于从科学第一性原理出发，用\"感知—预测—交互\"闭环构建机器人\"大脑+小脑\"统一系统，探索下一代可解释自"
  },
  {
    "id": "rss:https://36kr.com/p/3882364132077577?f=rss",
    "domain": "大厂 AI 动态",
    "title": "硬氪首发 | 清华车辆学院师兄弟创业具身智能，已完成数亿元天使融资，将落地汽车产业",
    "url": "https://36kr.com/p/3882364132077577?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T06:25:53+00:00",
    "summary": "作者&nbsp;|&nbsp;邱晓芬 编辑&nbsp;|&nbsp;袁斯来 硬氪获悉，具身智能公司「光象科技」宣布完成累计数亿元天使轮融资。 最新一轮由珠海科技产业集团、兴证资本、松禾资本、顺禧基金、慕华科创、SeeFund、亿宸资本、上市公司行云科技等头部财投与产投深度参与，老股东零一创投、L2F光源创业者基金持续加注。 本轮资金将重点投入物理原生基座模型的研发迭代，并推进具身智能机器人在工业场"
  },
  {
    "id": "rss:https://36kr.com/p/3882361033322755?f=rss",
    "domain": "大厂 AI 动态",
    "title": "硬氪首发 | 小米前高管唐沐创业咖啡机器人，完成数亿融资，林斌、黎万强投过",
    "url": "https://36kr.com/p/3882361033322755?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T06:23:00+00:00",
    "summary": "作者&nbsp;|&nbsp;邱晓芬 编辑&nbsp;|&nbsp;袁斯来 硬氪获悉，通用餐饮具身机器人公司「影智XBOT」连续完成数亿元两轮融资——其中，A轮的2亿元融资由香港简坤资本GPTX出资，B轮融资为3-5亿元人民币，由多支政府基金、美元基金和产业投资方共同参与出资。 这是目前餐饮垂直机器人领域规模最大的一笔融资之一。 在此之前，「影智XBOT」还完成了一轮天使融资，出资人阵容豪华——包"
  },
  {
    "id": "rss:https://36kr.com/p/3880770270425089?f=rss",
    "domain": "大厂 AI 动态",
    "title": "对话傲鲨创始人徐振华：当科幻机甲成为户外装备，外骨骼如何重新定义人机关系？",
    "url": "https://36kr.com/p/3880770270425089?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T03:25:22+00:00",
    "summary": "《流浪地球2》与游戏《死亡搁浅》中，主角身穿外骨骼行走的人类未来图景，正在成为户外爱好者的真实装备。 7月4日，阳澄湖半岛度假区，十几个人身穿“机甲”在湖畔徒步。他们穿的是傲鲨VIATRIX增程动力外骨骼机器人，走几步后很快步伐变得轻盈，这是外骨骼通过学习他们的行走姿态，在抬腿瞬间加上一定推力，使6公里的徒步体验更像一次悠闲的City walk。 当天的机甲徒步活动由傲鲨联合户外平台一帐之地共同策"
  },
  {
    "id": "rss:https://36kr.com/p/3880629882679301?f=rss",
    "domain": "大厂 AI 动态",
    "title": "9点1氪｜阿里内部全面禁用Claude Code；FF洛杉矶总部人去楼空？公司回应：不实；微软砸25亿美元组建6000人AI新公司",
    "url": "https://36kr.com/p/3880629882679301?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T01:03:44+00:00",
    "summary": "今日热点导览 三部门：调整节能汽车、新能源汽车车船税优惠政策 三星传获Meta超10万亿韩元AI芯片代工订单 茉莉奶白小程序更换彩色Logo Meta打算出售富余算力引发科技股回落 英伟达前光互连技术高管Ashkan Seyedi加入艾迈斯欧司朗 TOP3大新闻 因存在植入后门风险，阿里内部全面禁用Claude Code 36氪从阿里内部人士处获悉，因近期Claude Code被曝存在植入后门的安"
  },
  {
    "id": "rss:https://36kr.com/p/3879991356157952?f=rss",
    "domain": "大厂 AI 动态",
    "title": "36氪首发 | 剑桥副教授创业硅光芯片，已合作华为，获一亿投资",
    "url": "https://36kr.com/p/3879991356157952?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T01:00:00+00:00",
    "summary": "图源/企业 作者丨欧雪 编辑丨袁斯来 硬氪获悉，硅基光电子集成芯片研发商光引科技近期已完成1亿元Pre-A轮融资，投资方包括光子强链基金、善达投资、长飞基金、洛阳英才、中科创星、西安财金。资金将主要用于上海新实验室建设、人才招募及量产推进。 光引科技2021年成立于徐州，核心团队孵化自英国剑桥大学研发团队。创始人程祺翔为剑桥大学博士、剑桥大学副教授，在光子集成领域深耕超16年，曾就职于华为海思光电"
  },
  {
    "id": "rss:https://36kr.com/p/3879807100023040?f=rss",
    "domain": "大厂 AI 动态",
    "title": "400家starup聚集、阿斯利康重押13亿欧元，创新药出海欧洲绕不开这座城｜最前线",
    "url": "https://36kr.com/p/3879807100023040?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T12:28:30+00:00",
    "summary": "文｜胡香赟 编辑｜海若镜 2026年6月底，西班牙瓦尔德希伯伦大学医院（Vall d’Hebron University Hospital）宣布完成欧洲首例单孔机器人儿科肾输尿管切除术。 瓦尔德希伯伦大学医院是西班牙规模最大的综合医院之一，年接诊量过百万人次，在整个欧洲医疗系统内，这家医院对前沿医疗技术、产品的探索都称得上“先锋”。此前，世界首例供体来自安乐死患者的面部移植手术就在这里完成。 本次"
  },
  {
    "id": "rss:https://36kr.com/p/3879814941437956?f=rss",
    "domain": "大厂 AI 动态",
    "title": "秋声 | 袁进辉新公司冲港股IPO，成立不到三年",
    "url": "https://36kr.com/p/3879814941437956?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T11:12:32+00:00",
    "summary": "本文约2700字，建议阅读6分钟 作者&nbsp;|&nbsp;彭孝秋 编者按：AI大爆发之际，越来越多公司走向资本市场。每一份招股书翻动的声音里，都藏着一家公司想说与未曾明说的全部。 鉴于此，硬氪特推出「秋声」专栏。秋声取自欧阳修《秋声赋》，借“听秋声”之意，产业冷暖，辨公司成色，记录企业冲刺IPO途中那些被写下与被隐藏的真实。这是我们第七期，硅基流动。 Q2的最后一天，硅基流动向港交所递交了上"
  },
  {
    "id": "rss:https://36kr.com/p/3879796756754694?f=rss",
    "domain": "大厂 AI 动态",
    "title": "氪星晚报｜西贝餐饮集团退出小女当家；FF洛杉矶总部人去楼空？公司回应：不实",
    "url": "https://36kr.com/p/3879796756754694?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T10:55:45+00:00",
    "summary": "大公司： 德银：Meta云业务或打开千亿美元级AI投入变现通道，2027年收入最高增300亿美元 针对Meta拟向外部客户出售AI算力及模型访问权限的消息，德意志银行认为，这并不意味着Meta削弱前沿模型或“超级智能”布局，而更可能是将较旧、非核心或阶段性闲置的算力对外变现，同时保留最新一代芯片用于内部训练。此举有望把市场对Meta“高资本开支、收入回报有限”的担忧，转向对其新增高利润收入选择权的"
  },
  {
    "id": "rss:https://36kr.com/p/3877919172047111?f=rss",
    "domain": "大厂 AI 动态",
    "title": "理想组织再动刀：去中间环节，整车和智驾产品回归研发｜36氪独家",
    "url": "https://36kr.com/p/3877919172047111?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-03T10:45:12+00:00",
    "summary": "图源视觉中国 文｜肖漫编辑｜李勤、杨轩 “回归创业状态”，去年李想说出这个目标后，理想汽车还在进行组织和流程精简。 36氪汽车从多位知情人士处获悉，理想即将围绕产品决策流程进行新一轮组织架构调整，计划将产品部的部分关键职能拆分，并入研发部门。 从群组关系来看，理想汽车产品部由范皓宇负责，包含电动本体、空间智能、自动驾驶终端产品、交互设计、平台运营、App与官网等。 了解调整动向的人士向36氪汽车透"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3882343015444736?f=rss",
    "domain": "大厂 AI 动态",
    "title": "中金：建议中长期逢低布局农产品多头行情",
    "url": "https://36kr.com/newsflashes/3882343015444736?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T06:03:32+00:00",
    "summary": "7月5日，中金公司研报认为，历经2023-2025年全球农产品持续累库、价格深度下行的调整周期后，2026年农产品板块或正式迎来周期拐点，全品类价格底部充分夯实，整体确立易涨难跌的运行格局。综合判断，2026年下半年全球大宗农产品或无单边下跌基础，成本筑牢底部、供给收缩确立趋势、天气提供脉冲弹性、需求打开上行空间，板块整体或逐步开启周期向上态势，板块行情排序为油脂、棉花、天然橡胶、白糖＞大豆、玉米"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3882340907954177?f=rss",
    "domain": "大厂 AI 动态",
    "title": "电影《小黄人与大怪兽》上映3天，总票房破9000万元",
    "url": "https://36kr.com/newsflashes/3882340907954177?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T06:01:23+00:00",
    "summary": "7月5日，据网络平台数据，电影《小黄人与大怪兽》上映3天，总票房破9000万元。（每日经济新闻）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3882330361590022?f=rss",
    "domain": "大厂 AI 动态",
    "title": "华工科技复杂曲面六轴激光加工装备入选工信部工业母机创新产品典型案例",
    "url": "https://36kr.com/newsflashes/3882330361590022?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T05:50:40+00:00",
    "summary": "7月4日，工业和信息化部装备工业发展中心正式公布《2026年度工业母机创新产品典型案例名单》。华工科技复杂曲面六轴激光加工装备成功入选。（证券时报）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3882317458043141?f=rss",
    "domain": "大厂 AI 动态",
    "title": "中金公司战略部负责人马葵兼任中金国际副总裁",
    "url": "https://36kr.com/newsflashes/3882317458043141?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T05:37:32+00:00",
    "summary": "近日，中金国际迎来关键人事变动，集团战略部负责人马葵正式兼任中金国际副总裁。马葵1996 年毕业于对外经济贸易大学，先后获得国际经济合作专业学士学位与国际金融硕士学位。1998年4月加入中金公司，先后担任财务部、市场风险部、计划分析部、运营支持部负责人，历任助理首席财务官、财务总监等职。2024年2月，根据工作安排辞去财务总监一职，出任中金公司战略部负责人，并于2026年6月兼任中金国际副总裁。现"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3882317021212680?f=rss",
    "domain": "大厂 AI 动态",
    "title": "蒋方舟再回应被清华教授指控论文造假",
    "url": "https://36kr.com/newsflashes/3882317021212680?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T05:37:06+00:00",
    "summary": "青年作家蒋方舟7月5日在其个人社交平台再发文，题目为《关于肖鹰教授指控我论文“全面造假”的逐项说明》。文中称，肖鹰教授的指控存在系统性的夸大与失实（比如说作者论文“全面造假”），对于这些严重失实、足以损害作者名誉的指控，作者予以明确、坚决的否认。蒋方舟表示，已经于昨日（7月4日）报警，并且将会将相关材料递交给清华大学相关部门，以及用法律手段维护自己的利益。（界面新闻）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3882310540357896?f=rss",
    "domain": "大厂 AI 动态",
    "title": "2026年暑期档电影票房（含预售）突破20亿元",
    "url": "https://36kr.com/newsflashes/3882310540357896?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T05:30:30+00:00",
    "summary": "7月5日，据网络平台数据，截至目前，2026年暑期档电影总票房（含预售）突破20亿元。（证券时报）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3882255495311362?f=rss",
    "domain": "大厂 AI 动态",
    "title": "张雪称负债接近1亿元，本月将还清全部债务",
    "url": "https://36kr.com/newsflashes/3882255495311362?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T04:34:30+00:00",
    "summary": "7月4日，张雪发布视频称，这个月就不是亿万“负”翁了。张雪透露自己目前负债接近1亿元，这次卖了一点股份，卖完后就会把债务全部还清，“再也不欠钱了”。（界面新闻）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3882254845423624?f=rss",
    "domain": "大厂 AI 动态",
    "title": "麦科医药MT1002完成Ib/II期首例入组，卒中“双管线”布局加速推进",
    "url": "https://36kr.com/newsflashes/3882254845423624?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T04:33:51+00:00",
    "summary": "7月3日，麦科医药-B（02335.HK）公告称，其自主研发的急性缺血性卒中管线MT1002的Ib/II期临床试验完成首例患者入组。这是该公司6月24日登陆港交所后，核心管线推进的又一实质性进展。MT1002为一款凝血因子II与GPIIb/IIIa双靶点拮抗剂，兼具抗凝与抗血小板作用。本次Ib/II期试验为多中心、分两部分设计：第一部分评估安全性、药代动力学特征；第二部分在更大规模患者中通过随机、"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3882254004924678?f=rss",
    "domain": "大厂 AI 动态",
    "title": "马未都发视频，回应“铜像疑云”",
    "url": "https://36kr.com/newsflashes/3882254004924678?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T04:32:59+00:00",
    "summary": "7月4日，马未都在其多个社交平台账号发布了一则视频，公开回应近期引发舆论热议的“被盗佛像疑似现身观复博物馆”一事。马未都表示，2005年观复博物馆厦门馆筹办期间，在厦门白鹭洲古玩城征集文物时发现了这尊佛像，“当时发现这尊佛像后，与该古玩城的合法商户细致商讨。因为我们认为这件佛像非常重要，我们需要知道它的来源。我就告知了商户，我们购买以后，一定会在博物馆长期展出。卖家是清楚这个后果的，也告知我们这个"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3882233720303621?f=rss",
    "domain": "大厂 AI 动态",
    "title": "鸿准6月营收同比增长10.66%",
    "url": "https://36kr.com/newsflashes/3882233720303621?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T04:12:21+00:00",
    "summary": "鸿准7月5日公布2026年6月合并营收为150.55亿元新台币，较去年同期的136.05亿元增长10.66%。累计来看，2026年1至6月合并营收为556.22亿元新台币，较去年同期的712.22亿元减少21.90%，显示上半年整体仍处于同比下滑态势。（界面新闻）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3882215401271303?f=rss",
    "domain": "大厂 AI 动态",
    "title": "大立光6月营收37.12亿元新台币",
    "url": "https://36kr.com/newsflashes/3882215401271303?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T03:53:43+00:00",
    "summary": "大立光7月5日公布6月份最新营运数据，单月营业收入净额降至新台币37.12亿元，同比减少10.46%。（界面新闻）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3882213157531905?f=rss",
    "domain": "大厂 AI 动态",
    "title": "罕见热浪来袭，预计美国超1.65亿人面临高温健康风险",
    "url": "https://36kr.com/newsflashes/3882213157531905?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T03:51:26+00:00",
    "summary": "近期，一场大范围罕见热浪正席卷美国东部和中部地区，多地刷新历史同期最高气温纪录。据美国国家气象局预测，7月4日美国“独立日”假期期间，美国多地将持续遭遇危险的热浪，预计将有超过1.65亿人面临“重大”或“极端”高温健康风险。（央视新闻）"
  },
  {
    "id": "wscn:3776217",
    "domain": "股票",
    "title": "华为首颗“韬芯片”霸气侧漏",
    "url": "https://wallstreetcn.com/articles/3776217",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T06:45:05+00:00",
    "summary": "新版论文从方法论层面进一步论证了“韬定律”成为“后摩尔时代”指导半导体产业发展新原则的可行性，还细化了麒麟移动芯片和昇腾AI算力平台未来5到10年的落地路线，为全球半导体产业提供了摩尔定律之外的第二条可持续发展路径。"
  },
  {
    "id": "wscn:3775383",
    "domain": "股票",
    "title": "铷铯：AI与新能源的“战略稀缺金属”，供需断崖打开4倍增长空间？",
    "url": "https://wallstreetcn.com/premium/articles/3775383?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T06:28:48+00:00",
    "summary": "全球铷铯资源极度稀缺、供给高度垄断，而钙钛矿光伏、太空能源、6G通信、量子技术等新兴需求的爆发式增长，正在推动铷铯盐市场从“吨级”向“千吨级”跨越。"
  },
  {
    "id": "wscn:3775829",
    "domain": "股票",
    "title": "VLCC运价坐上“过山车”，但决定行业方向的“锚”并没有松动",
    "url": "https://wallstreetcn.com/premium/articles/3775829?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T06:19:19+00:00",
    "summary": "VLCC的风险溢价正在让位给基本面价值。"
  },
  {
    "id": "wscn:3776218",
    "domain": "股票",
    "title": "OpenAI塌房！Scaling law原作曝bug，万亿算力全白烧",
    "url": "https://wallstreetcn.com/articles/3776218",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T06:02:52+00:00",
    "summary": "DeepMind研究员指出，OpenAI最初的Scaling Law错误引导 AI 行业长期“重参数、轻数据”，让大量模型训练不足、算力配置失衡，全球或因此浪费了数年研发时间和海量 GPU 资源。后续研究证实，模型与数据应同步放大，此前方向可能浪费了海量算力。"
  },
  {
    "id": "wscn:3776215",
    "domain": "股票",
    "title": "史无前例！为找稀土，日本开始“拆空调”了……",
    "url": "https://wallstreetcn.com/articles/3776215",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T04:40:08+00:00",
    "summary": "鉴于国内稀土资源短缺，日本首次开始从废旧的家用空调中提取稀土。日网民吐槽：“已经到了不得不捡垃圾的地步”。"
  },
  {
    "id": "wscn:3776211",
    "domain": "股票",
    "title": "天下苦DRAM久矣",
    "url": "https://wallstreetcn.com/articles/3776211",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T04:09:09+00:00",
    "summary": "DRAM价格暴涨，已成AI算力部署关键瓶颈，根源在于HBM持续挤占产能。价格倒逼技术路线转向：AMD以AI调度冷数据至闪存，Apple将模型常驻NAND，Marvell以硬件压缩扩容，闪迪推HBF新架构。纯DRAM堆砌时代结束，AI推理转向多层内存架构，以分层策略平衡性能与成本。"
  },
  {
    "id": "wscn:3776214",
    "domain": "股票",
    "title": "俄乌互相发动大规模袭击",
    "url": "https://wallstreetcn.com/articles/3776214",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T03:50:16+00:00",
    "summary": "俄罗斯国防部4日发表声明说，过去24小时内，俄军袭击了乌军在142个地区的燃料、能源和运输基础设施，以及远程无人机生产和储存设施，并对乌军和外国雇佣兵的临时部署地点进行了打击。乌克兰武装部队总参谋部4日通报称，3日至4日夜间，共记录268次交火。"
  },
  {
    "id": "wscn:3775748",
    "domain": "股票",
    "title": "半导体扩产超级周期“黄金窗口”：材料与设备的万亿拐点红利",
    "url": "https://wallstreetcn.com/premium/articles/3775748?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T03:49:51+00:00",
    "summary": "三星、SK海力士正开启存储芯片领域史无前例的扩产浪潮，全球存储资本开支2026/2027年预计分别达1103亿和1685亿美元，同比增长63%/53%。"
  },
  {
    "id": "wscn:3776213",
    "domain": "股票",
    "title": "A股万亿天团，“深圳造”只剩独苗",
    "url": "https://wallstreetcn.com/articles/3776213",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T03:42:15+00:00",
    "summary": "截至今年6月30日，注册地位于深圳的A股万亿市值公司仅剩工业富联一家，比亚迪、中国平安、招商银行相继跌出万亿阵营。“深圳造”的万亿市值公司四去其三的背后，一方面是市场风格转换的呈现，另一方面则是产业转型升级的映射。"
  },
  {
    "id": "wscn:3776130",
    "domain": "股票",
    "title": "下周重磅日程：中国通胀数据、美联储会议纪要、SK海力士美股首秀、智谱MiniMax解禁",
    "url": "https://wallstreetcn.com/articles/3776130",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T03:39:00+00:00",
    "summary": "中国6月CPI、PPI及外储数据下周公布，市场关注价格“K型分化”是否延续。美联储6月会议纪要出炉，此外美国将就对60国加征关税举行听证会。苹果、OpenAI、Meta等科技巨头CEO将齐聚太阳谷峰会，美股二季报序幕开启。智谱、MiniMax港股解禁，流动性压力骤升。SpaceX将入纳指，SK海力士ADR美股首秀，OpenAI GPT-5.6即将发布。"
  },
  {
    "id": "wscn:3776210",
    "domain": "股票",
    "title": "HBM竞赛升级！美光日本90亿美元扩建项目开工，预计2028年出货",
    "url": "https://wallstreetcn.com/articles/3776210",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T03:09:20+00:00",
    "summary": "美光投资约93亿美元启动日本广岛工厂扩建，重点推进HBM等先进存储产品量产，预计2028年夏季出货。日本政府提供最高5000亿日元补贴。此次扩产旨在应对AI芯片需求激增带来的供给缺口，强化对英伟达等厂商的供应能力。"
  },
  {
    "id": "wscn:3776208",
    "domain": "股票",
    "title": "无惧回调！瑞银上调海力士目标价，预测“三大利好”即将到来",
    "url": "https://wallstreetcn.com/articles/3776208",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T02:28:09+00:00",
    "summary": "SK海力士近5日跌8%，瑞银报告将其12个月目标价从300万韩元上调至320万韩元，主要基于三大催化剂：长协锁价覆盖60%–70%的量价，盈利确定性增强；HBM4预计2026年Q2规模出货；美股ADR上市后有望加大回购力度。"
  },
  {
    "id": "wscn:3776207",
    "domain": "股票",
    "title": "与特朗普通话85分钟，普京称“俄军正全线进攻”，此前威胁夺乌克兰更多土地建安全区",
    "url": "https://wallstreetcn.com/articles/3776207",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T01:47:34+00:00",
    "summary": "据俄方通报，普京在7月4日与特朗普的通话中表示，俄军正全线发起进攻，重申愿外交解决但须兼顾俄方原则立场；特朗普承诺推动尽快停火，特使及女婿将访莫斯科调解。当地时间7月3日，普京穿迷彩服视察前线，宣布控制卢甘斯克，并威胁在哈尔科夫、苏梅夺占更多土地作为“安全区”。"
  },
  {
    "id": "wscn:3776204",
    "domain": "股票",
    "title": "精准预测“美股动量股”暴跌后，高盛看到“逢低买入”的迹象",
    "url": "https://wallstreetcn.com/articles/3776204",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T01:25:04+00:00",
    "summary": "高盛高贝塔动量篮子（GSPRHIMO）近两日重挫18%，创2020年来最大跌幅。该策略2026年已多次出现两日跌超10%后修复的走势，当前模式高度相似。高盛提前预警7月回调并认为跌幅已为战术反弹留出空间，但仓位极度拥挤，若去杠杆持续，潜在最大回撤或达现有跌幅两倍。"
  },
  {
    "id": "wscn:3776206",
    "domain": "股票",
    "title": "PC及内存硬盘价格持续高位：硬盘一天三个价，经销商喊出“非刚需别买”",
    "url": "https://wallstreetcn.com/articles/3776206",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-05T01:06:40+00:00",
    "summary": "多位PC经销商表示，目前零部件和整机的价格已经处于极端高位，但未来还要涨价，且至少在一年内看不到（涨价）尽头。商家直言：“除非AI泡沫破灭，价格不可能降下来。”"
  },
  {
    "id": "wscn:3776202",
    "domain": "股票",
    "title": "韩国存储扩产、Meta出租算力--野村谈“存储两大利空”",
    "url": "https://wallstreetcn.com/articles/3776202",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T13:05:08+00:00",
    "summary": "野村认为，“存储两大利空”实为伪命题。韩方投资需数年才能落地，且HBM挤压通用产能，全球存储核心矛盾仍是严重短缺；Meta此举旨在提升资本回报率，将压低算力成本，反而会激发更庞大的AI增量需求。AI需求未见顶，情绪错杀为板块提供了重估窗口。"
  },
  {
    "id": "wscn:3776203",
    "domain": "股票",
    "title": "苹果AI功能未能引爆换机潮，瑞银调查显示用户升级意愿持续下滑",
    "url": "https://wallstreetcn.com/articles/3776203",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T11:45:57+00:00",
    "summary": "结果显示，因Apple Intelligence提前换机的意愿降至约24%，而认为其对购机\"无影响\"的比例升至约31%。美国市场12个月内iPhone购买意向同比上升约300个基点至约20%，英国和德国市场涨幅更为显著；折叠屏iPhone被视为潜在需求亮点，初期或贡献约500万台销量。"
  },
  {
    "id": "wscn:3776200",
    "domain": "股票",
    "title": "高盛：美股AI上涨力竭，下半年布局防御板块，看好医疗、欧洲防务",
    "url": "https://wallstreetcn.com/articles/3776200",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T10:58:38+00:00",
    "summary": "高盛认为，主导上半年的AI与动量交易已经出现力竭信号，短期面临剧烈回调与平仓踩踏风险。医疗板块受生物工艺及药企并购周期双重驱动；防务股因持仓轻、估值低迎来布局拐点。落后的周期、软件与消费股有望补涨，建议使用“剔除AI”指数篮子对冲科技股杀跌风险。"
  },
  {
    "id": "wscn:3776201",
    "domain": "股票",
    "title": "网络营销新规落地前夜，某地公募行业闭门会释放严监管信号，“大V挂靠”未必合规，产品营销与品牌、投教边界在哪？",
    "url": "https://wallstreetcn.com/articles/3776201",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T10:49:15+00:00",
    "summary": "从“砸钱投大V”到“宁可不做，也不做错”，公募行业迎来营销生存法则切换。"
  },
  {
    "id": "wscn:3776199",
    "domain": "股票",
    "title": "当AI账单失控，模型路由器成为企业降本新宠",
    "url": "https://wallstreetcn.com/articles/3776199",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-04T10:16:42+00:00",
    "summary": "企业AI账单失控，“模型路由器”成降本杀手锏。该技术按任务复杂度智能调度大小AI模型，最高狂砍97%算力开支且不降质。目前巨头与初创全面入局，资本重金押注，这道“控费阀门”已成AI基建赛道不可忽视的新风口。"
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
  }
]
```
