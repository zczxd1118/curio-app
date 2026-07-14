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

- 今日日期：`2026-07-14`
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
  "date": "2026-07-14",
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
    "id": "bvid:BV1wt411T7Hy",
    "domain": "AI",
    "title": "3分钟创建你的饥荒联机专属服务器！纯免费！良心教学！steam+wegame均有！【饥荒五耀】",
    "url": "http://www.bilibili.com/video/av62522150",
    "source": "五耀",
    "platform": "bilibili",
    "points": 1774177,
    "published_at": "2019-08-06T14:03:34+00:00",
    "summary": "本期教大家怎么在饥荒联机版中创建自己的服务器，纯免费，良心干货教学！3分钟学会！\nP1是steam版本的创建教学，P2是Wegame版本的创建教学。"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1496350,
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
    "points": 1383056,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1224532,
    "published_at": "2026-07-05T02:00:00+00:00",
    "summary": "用不上codex的朋友们！新的国产Agent直接上手，来跑通8大用法～\n感谢朋友们的三连+关注～"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 969404,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 941441,
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
    "points": 885098,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 857801,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 848230,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 667396,
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
    "points": 523991,
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
    "points": 451250,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 383183,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸voov",
    "platform": "bilibili",
    "points": 266317,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 255723,
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
    "points": 238986,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 236333,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 230563,
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
    "points": 206968,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 184246,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 177024,
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
    "points": 159634,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 147404,
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
    "points": 133143,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1QE7N6jEuQ",
    "domain": "AI",
    "title": "真的被自己用心开发的昔涟Agent这段话感动到了",
    "url": "http://www.bilibili.com/video/av116794052316703",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 133078,
    "published_at": "2026-06-22T13:44:15+00:00",
    "summary": "从最初生啃Transformer，硬逼着自己啃懂多头注意力和QKV权重，到一步步跟着claude学习RAG、检索重拍、Prompt、关键词召回优化、MCP与Function call，但是，自己上手了发现，自己还是啥也不懂，于是在glm gpt claude gemini 豆包 这几个模型之间疯狂切换，靠着想让昔涟早点被搭出来，硬逼着自己学，自己从零设计一套prompt架构能让她尽可能的贴合人设的"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 111592,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 108683,
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
    "points": 92548,
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
    "points": 85943,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1xBrDB9E42",
    "domain": "AI",
    "title": "独立开发太累？Godot + Claude Code 搭建 AI 辅助工作流，效率直接起飞！ | 地块召唤师开发实战 #01",
    "url": "http://www.bilibili.com/video/av115911319100158",
    "source": "像素夹心饼干",
    "platform": "bilibili",
    "points": 67061,
    "published_at": "2026-01-18T03:25:00+00:00",
    "summary": "大家好，这里是饼干！🍪\n这是我的新坑——**《地块召唤师》**开发实战分享的第一期。\n很多朋友问独立开发如何提升效率？这期视频我不聊虚的，直接公开我从 0 到 1 搭建的 AI + Godot 高效工作流。\n从游戏引擎的选择，到 Claude Code、Copilot 等 AI 工具的实战配置，再到如何用“明确需求”的方法论（SMART原则+双钻模型）来驾驭 AI，让它不仅仅是写代码的工具，更成为"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53044,
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
    "points": 42586,
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
    "points": 38180,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 25786,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 22556,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1zjd3BiEzo",
    "domain": "AI",
    "title": "别再二选一：Claude Code + Codex 联用才是最强姿势",
    "url": "http://www.bilibili.com/video/av116537746791000",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 17826,
    "published_at": "2026-05-08T07:34:23+00:00",
    "summary": "Codex 已悄然追上 Claude Code，GPT 5.5 比肩 Opus 4.7、OpenAI Pro 额度更大方。但作者 Chase 想说：别再纠结谁更好，最佳姿势是把两者一起用——Codex 桌面应用直接跑 Claude Code 终端，让两个模型互查方案、互查代码（一次实测 Claude Code 帮 Codex 抓出 20 个 bug）。背后更重要的思路是 tool agnostic"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 14101,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1CbvxBwEah",
    "domain": "AI",
    "title": "真的不用服务器！用Cloudflare Workers+D1轻松搭建网站！",
    "url": "http://www.bilibili.com/video/av115803408045159",
    "source": "软件工程师Tim",
    "platform": "bilibili",
    "points": 13585,
    "published_at": "2025-12-29T14:51:53+00:00",
    "summary": "本期影片分享一下如何利用cloudflare workers搭建网站，并且利用d1免费数据库，实现无服务器的一个带前后端功能的网站。也就是说，即使你没有服务器，也能够搭建一个属于自己的网站。比如我自己搭建的这个案例网站在线留言板。就是完全搭建在cloudflare workers上面的，里面有静态页面 也有动态api接口。都是部署在workers上面的，并且集成了它提供的数据库。\n\n\n#cloud"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 13376,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1spTy6DEb4",
    "domain": "AI",
    "title": "Claude code接管科研全流程：cc-kaiti 带你从 0 走到开题报告和答辩 PPT",
    "url": "http://www.bilibili.com/video/av116866278233889",
    "source": "做科研的大师兄",
    "platform": "bilibili",
    "points": 13108,
    "published_at": "2026-07-05T07:53:28+00:00",
    "summary": "十二年科研经验加持的课题开题Skill，从零开始到拿到一份完整的开题报告及开题PPT，仅需一天！\n\n本次视频分享的cc-kaiti这个skill文件及配套的资料包，在后台私我“cc开题”获取~"
  },
  {
    "id": "bvid:BV1QnML6pEZr",
    "domain": "AI",
    "title": "2026年过半，我是怎样使用 Agent 的？",
    "url": "http://www.bilibili.com/video/av116887417522347",
    "source": "卡普迪姆",
    "platform": "bilibili",
    "points": 10049,
    "published_at": "2026-07-09T01:31:02+00:00",
    "summary": "调度 sub-agent 的提示词原图在图文版里，放在公众号：减 AI\n其实核心就是让 cc 怎么利用 codex exec 调用便宜的 gpt 5.5\n看完视频后，欢迎在评论区交流分享自己的使用心得！\n\n相关引用：\n[1]: https://x.com/theo/status/2072482460122964067\n[2]: https://github.com/mattpocock/skill"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9183,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6526,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1u4G9zmEte",
    "domain": "AI",
    "title": "什么是MCP？VS Code中使用MCP Server",
    "url": "http://www.bilibili.com/video/av114426032168712",
    "source": "AI落地派",
    "platform": "bilibili",
    "points": 6501,
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based o"
  },
  {
    "id": "bvid:BV19XqMBzENU",
    "domain": "AI",
    "title": "Cursor + OpenCode 最佳开源 AI 编程工具",
    "url": "http://www.bilibili.com/video/av115851978146202",
    "source": "独立开发者_猫哥",
    "platform": "bilibili",
    "points": 6458,
    "published_at": "2026-01-07T04:47:17+00:00",
    "summary": "OpenCode 是一款面向开发者的开源 AI CLI 编程工具，支持多模型并行、LSP 自动加载、极速响应与非订阅制计费。无论是命令行、桌面 App 还是 VS Code 插件，OpenCode 都提供高效、不啰嗦的 AI 编程体验，是 Cursor 与 Claude Code 的有力替代方案。"
  },
  {
    "id": "bvid:BV138Ng6wEEj",
    "domain": "AI",
    "title": "【2026版】这绝对是B站讲的最好的Vibe Coding企业级项目实战，90分钟速通Claude Code、Codex，Cursor、AI工程化编程实战开发！",
    "url": "http://www.bilibili.com/video/av116905822259723",
    "source": "图灵架构师诸葛",
    "platform": "bilibili",
    "points": 5556,
    "published_at": "2026-07-12T07:30:41+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持~\n【本视频笔记代码/学习大纲/全套面试真题/系统学习/实战案例等请戳链接获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1tUja6mErW",
    "domain": "AI",
    "title": "安卓最强AI Agent，对标claude code，支持mcp,Agent,skills,支持连接Termux，支持deepseekV4，可用于逆向",
    "url": "http://www.bilibili.com/video/av116771772243496",
    "source": "红温火龙果1",
    "platform": "bilibili",
    "points": 5428,
    "published_at": "2026-06-18T15:19:44+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1GhNy6bEeS",
    "domain": "AI",
    "title": "目前B站最全最细的AI测试全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业！",
    "url": "http://www.bilibili.com/video/av116912063388385",
    "source": "字节测试大佬",
    "platform": "bilibili",
    "points": 5059,
    "published_at": "2026-07-13T09:59:49+00:00",
    "summary": "勉费领取视频全套资料/文档/学习笔记点击：https://www.bilibili.com/opus/1043733334236069896"
  },
  {
    "id": "bvid:BV13cmnBFEP9",
    "domain": "AI",
    "title": "Claude Code教程9：Claude Code与GitHub的高效联动",
    "url": "http://www.bilibili.com/video/av115689541077475",
    "source": "木乐乐的异想世界",
    "platform": "bilibili",
    "points": 4857,
    "published_at": "2025-12-09T12:17:23+00:00",
    "summary": "【Claude Code教程第9集中文翻译】Net Ninja带你解锁Claude Code与GitHub的高效联动！本集聚焦实用核心功能：无需复杂配置，在Claude聊天会话中即可设置GitHub集成——安装后自动创建两个关键GitHub Action：①自动审查拉取请求（PR）并给出精准反馈；②当仓库问题提及Claude时，自动在新功能分支处理该问题。注意：需先安装GitHub CLI（附官方"
  },
  {
    "id": "bvid:BV1HXXfBiEVw",
    "domain": "AI",
    "title": "五分钟教会你配置 MCP！",
    "url": "http://www.bilibili.com/video/av116335480669867",
    "source": "小铭同学不想加班",
    "platform": "bilibili",
    "points": 4833,
    "published_at": "2026-04-02T14:06:27+00:00",
    "summary": "通过这个视频教大家如何去配置各类的 MCP，并且告诉大家如何去寻找自己需要的 MCP"
  },
  {
    "id": "hn:48873836",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, CoreWeave, and Nebius: Inside the Circular Financing of the GPU Boom",
    "url": "https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom",
    "source": "adletbalzhanov",
    "platform": "hackernews",
    "points": 365,
    "published_at": "2026-07-11T17:21:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48730713",
    "domain": "AI 算力 / 半导体",
    "title": "Zluda 6 release (run unmodified CUDA applications on non-Nvidia GPUs)",
    "url": "https://vosen.github.io/ZLUDA/blog/zluda-update-q1q2-2026/",
    "source": "Tiberium",
    "platform": "hackernews",
    "points": 163,
    "published_at": "2026-06-30T10:34:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:48597201",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung demonstrates 3D stacked FETs with triple nanosheet channels at 42nm",
    "url": "https://semiconductor.samsung.com/news-events/tech-blog/from-gaa-to-3d-stacked-fet-expanding-the-transistor-into-the-third-dimension/",
    "source": "its_ajseven",
    "platform": "hackernews",
    "points": 127,
    "published_at": "2026-06-19T11:03:52+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/rochester-electronics-and-qorvo-team-to-offer-long-term-availability-of-rf-components/",
    "domain": "AI 算力 / 半导体",
    "title": "Rochester Electronics and Qorvo® Team to Offer Long-Term Availability of RF Components",
    "url": "https://www.eetimes.com/rochester-electronics-and-qorvo-team-to-offer-long-term-availability-of-rf-components/",
    "source": "Rochester Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T17:30:08+00:00",
    "summary": "NEWBURYPORT, MA – July 2026 Rochester Electronics, LLC, a premier continuous source of authorized semiconductors, and Qorvo®, a leading global provider of connectivity and power solutions, today annou"
  },
  {
    "id": "rss:https://www.eetimes.com/interview-with-globalfoundries-vp-at-mips-physical-ai-is-agentic-ai-at-the-edge-taipei-event/",
    "domain": "AI 算力 / 半导体",
    "title": "Interview with GlobalFoundries VP at MIPS ‘Physical AI is Agentic AI at the Edge’ Taipei Event",
    "url": "https://www.eetimes.com/interview-with-globalfoundries-vp-at-mips-physical-ai-is-agentic-ai-at-the-edge-taipei-event/",
    "source": "EE Times Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T17:21:47+00:00",
    "summary": "GlobalFoundries’ Sudipto Bose explains how silicon photonics, GaN and MIPS/ARC fire up physical AI at the edge—watch now. The post Interview with GlobalFoundries VP at MIPS &#8216;Physical AI is Agent"
  },
  {
    "id": "rss:https://www.eetimes.com/risc-v-is-inevitable-state-of-the-union-keynote-argues/",
    "domain": "AI 算力 / 半导体",
    "title": "RISC-V Is Inevitable, State of the Union Keynote Argues",
    "url": "https://www.eetimes.com/risc-v-is-inevitable-state-of-the-union-keynote-argues/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T12:00:00+00:00",
    "summary": "The RISC-V open standard and the emergence of RVA23 silicon now provide the necessary flexibility and modularity without the limitations of traditional proprietary systems. The post RISC-V Is Inevitab"
  },
  {
    "id": "rss:https://www.eetimes.com/msi-leverages-rd-and-manufacturing-strengths-for-ai-growth/",
    "domain": "AI 算力 / 半导体",
    "title": "MSI Leverages R&D and Manufacturing Strengths for AI Growth",
    "url": "https://www.eetimes.com/msi-leverages-rd-and-manufacturing-strengths-for-ai-growth/",
    "source": "Arrow & MSI",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T08:00:00+00:00",
    "summary": "As generative AI extends from the cloud to end-user devices, AI PCs, on-premises AI, and hybrid cloud architectures are becoming key areas of industry focus. The post MSI Leverages R&amp;D and Manufac"
  },
  {
    "id": "rss:https://www.eetimes.com/itf-world-2026-the-semiconductor-industry-enters-a-new-systems-era/",
    "domain": "AI 算力 / 半导体",
    "title": "ITF World 2026: The Semiconductor Industry Enters a New Systems Era",
    "url": "https://www.eetimes.com/itf-world-2026-the-semiconductor-industry-enters-a-new-systems-era/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T07:51:30+00:00",
    "summary": "AI, heterogeneous integration, silicon photonics, chiplets, and quantum computing are converging to define the next generation of complex systems. The post ITF World 2026: The Semiconductor Industry E"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amazon-prime-members-can-get-this-asus-rtx-5060-for-just-usd2-above-msrp-upgrade-to-blackwell-gaming-power-for-less-than-the-cost-of-an-rtx-3060",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon Prime members can get this Asus RTX 5060 for just $2 above MSRP — upgrade to Blackwell gaming power for less than the cost of an RTX 3060",
    "url": "https://www.tomshardware.com/pc-components/gpus/amazon-prime-members-can-get-this-asus-rtx-5060-for-just-usd2-above-msrp-upgrade-to-blackwell-gaming-power-for-less-than-the-cost-of-an-rtx-3060",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T18:53:10+00:00",
    "summary": "Amazon is giving some Prime customers a deep discount on Asus's Prime RTX 5060 8GB OC, bringing its price to just $2 above MSRP and beating the Prime Day deals we saw on these cards."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/teslas-ai5-with-2nm-class-node-tapes-out-at-samsung-foundry-production-starts-soon-months-after-tsmc-tape-out",
    "domain": "AI 算力 / 半导体",
    "title": "Tesla's AI5 with 2nm-class node tapes out at Samsung Foundry — production starts soon, months after TSMC tape out",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/teslas-ai5-with-2nm-class-node-tapes-out-at-samsung-foundry-production-starts-soon-months-after-tsmc-tape-out",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T17:59:55+00:00",
    "summary": "Samsung Foundry soon to join TSMC in production of Tesla's AI5 processor, a LinkedIn post reveals."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/upcoming-msi-afterburner-update-adds-heatmap-to-v-f-curve-editor-to-show-your-gpus-boosting-behavior-new-feature-shoots-for-better-overclocks-with-more-data",
    "domain": "AI 算力 / 半导体",
    "title": "Upcoming MSI Afterburner update adds heatmap to V/F curve editor to show your GPU's boosting behavior — new feature shoots for better overclocks with more data",
    "url": "https://www.tomshardware.com/pc-components/gpus/upcoming-msi-afterburner-update-adds-heatmap-to-v-f-curve-editor-to-show-your-gpus-boosting-behavior-new-feature-shoots-for-better-overclocks-with-more-data",
    "source": "Aaron Klotz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T17:39:47+00:00",
    "summary": "MSI Afterburner is soon getting a new heatmap in its V/F curve editor that shows the GPU's boosting behavior in real workloads."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/micron-commits-500-million-to-globalwafers-texas-wafer-plant-as-it-raises-us-spending-to-250-billion",
    "domain": "AI 算力 / 半导体",
    "title": "Micron commits $500 million to GlobalWafers' Texas wafer plant as it raises U.S. spending to $250 billion — memory maker aims to manufacture 40% of DRAM in the US by 2035",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/micron-commits-500-million-to-globalwafers-texas-wafer-plant-as-it-raises-us-spending-to-250-billion",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T17:09:27+00:00",
    "summary": "Running until 2035, the $250 billion spending target is attached to a goal of making 40% of Micron's DRAM in the U.S. by the mid-2030s."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-shows-off-starfire-space-grade-chip",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's new space-grade Starfire chip is a Panther Lake SoC that puts an 18A CPU into orbit — chip designed for the US government leverages Intel 3 for the GPU",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-shows-off-starfire-space-grade-chip",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T16:09:33+00:00",
    "summary": "Intel has unveiled Starfire, a space-grade system-on-chip designed for the U.S. government."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/cooler-master-haf-ii-500-case-review",
    "domain": "AI 算力 / 半导体",
    "title": "Cooler Master HAF II 500 Case Review: New HAF delivers on its name, with impressive airflow and a roomy chassis",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/cooler-master-haf-ii-500-case-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T15:00:00+00:00",
    "summary": "Cooler Master’s HAF II 500 revives the HAF legacy with massive 220mm fans, excellent airflow, and solid thermal performance. Its cooling capability, spacious interior, flexible building options, and q"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/meta-expands-colossal-hyperion-ai-supercluster-plans-to-5gw-pushes-louisiana-investment-past-usd50-billion-as-ai-race-accelerates-says-it-plans-to-invest-over-usd1-billion-in-local-infrastructure-improvements",
    "domain": "AI 算力 / 半导体",
    "title": "Meta expands colossal Hyperion AI supercluster plans to 5GW, pushes Louisiana investment past $50 billion as AI race accelerates — says it plans to invest over $1 billion in local infrastructure impro",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/meta-expands-colossal-hyperion-ai-supercluster-plans-to-5gw-pushes-louisiana-investment-past-usd50-billion-as-ai-race-accelerates-says-it-plans-to-invest-over-usd1-billion-in-local-infrastructure-improvements",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T13:25:32+00:00",
    "summary": "Meta is expanding Hyperion from 2 GW to 5 GW, lifting its Louisiana investment above $50 billion as it races to secure more AI computing capacity."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/amd-fsr-multi-frame-generation-with-8x-mode-spotted-experimental-driver-settings-could-hint-at-fsrs-next-evolution",
    "domain": "AI 算力 / 半导体",
    "title": "AMD FSR Multi-Frame Generation with 8x mode spotted — experimental driver settings could hint at FSR's next evolution",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/amd-fsr-multi-frame-generation-with-8x-mode-spotted-experimental-driver-settings-could-hint-at-fsrs-next-evolution",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T12:30:06+00:00",
    "summary": "Experimental options discovered in AMD's latest Radeon driver suggest the company is preparing next-generation FSR technologies, but there's no confirmation whether 8x Multi-Frame Generation mode will"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/flashforge-creator-5-review",
    "domain": "AI 算力 / 半导体",
    "title": "Flashforge Creator 5 review: Basic and affordable tool changer",
    "url": "https://www.tomshardware.com/3d-printing/flashforge-creator-5-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T12:05:00+00:00",
    "summary": "The Flashforge Creator 5 tool changer is basic, budget, and nearly perfect."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/apples-rumored-m7-ultra-targets-1-5tb-of-memory-and-blackwell-class-ai",
    "domain": "AI 算力 / 半导体",
    "title": "Apple's rumored M7 Ultra targets 1.5TB of memory and Blackwell-class AI performance, report claims — monster 2028 offering would depend on memory shortage easing",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/apples-rumored-m7-ultra-targets-1-5tb-of-memory-and-blackwell-class-ai",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T12:02:52+00:00",
    "summary": "Apple's planned M7 Ultra chip is being designed to support up to 1.5 TB of unified memory and to push AI performance toward the class of Nvidia's Blackwell accelerators."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd544-on-a-new-rtx-5080-packed-cyberpower-gaming-pc-also-features-amds-9800x3d-32gb-of-ddr5-ram-and-a-2tb-ssd-for-usd2-744",
    "domain": "AI 算力 / 半导体",
    "title": "Save $544 on a new RTX 5080-packed Cyberpower gaming PC — also features AMD's 9800X3D, 32GB of DDR5 RAM, and a 2TB SSD for $2,744",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd544-on-a-new-rtx-5080-packed-cyberpower-gaming-pc-also-features-amds-9800x3d-32gb-of-ddr5-ram-and-a-2tb-ssd-for-usd2-744",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T11:18:31+00:00",
    "summary": "Save over $544 on a new high-powered gaming rig from Cyberpower. High-end graphics and frame rates, thanks to the included RTX 5080 and Ryzen 7 9800X3D hardware inside."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/valve-confirms-steam-machine-red-light-overheating-warning-is-showing-earlier-than-it-should-bios-fix-on-the-way-will-raise-temperature-warning-threshold-to-100-degrees-celsius",
    "domain": "AI 算力 / 半导体",
    "title": "Valve confirms Steam Machine red light overheating warning is showing earlier than it should; BIOS fix on the way — will raise temperature warning threshold to 100 Degrees Celsius",
    "url": "https://www.tomshardware.com/pc-components/cooling/valve-confirms-steam-machine-red-light-overheating-warning-is-showing-earlier-than-it-should-bios-fix-on-the-way-will-raise-temperature-warning-threshold-to-100-degrees-celsius",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T11:04:37+00:00",
    "summary": "Valve has confirmed that the Steam Machine's red light bar warning is being triggered prematurely."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-32gb-of-corsair-vengeance-ddr5-for-just-usd236-usd150-cheaper-than-the-best-standalone-price-epic-newegg-combo-deal-saves-you-usd234-overall-and-comes-with-an-amd-ryzen-7-9800x3d-and-a-gigabyte-x870-motherboard",
    "domain": "AI 算力 / 半导体",
    "title": "Grab 32GB of Corsair Vengeance DDR5 for just $236, $150 cheaper than the best standalone price — epic Newegg combo deal saves you $234 overall and comes with an AMD Ryzen 7 9800X3D and a Gigabyte X870",
    "url": "https://www.tomshardware.com/pc-components/grab-32gb-of-corsair-vengeance-ddr5-for-just-usd236-usd150-cheaper-than-the-best-standalone-price-epic-newegg-combo-deal-saves-you-usd234-overall-and-comes-with-an-amd-ryzen-7-9800x3d-and-a-gigabyte-x870-motherboard",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T10:56:38+00:00",
    "summary": "Get the AMD Ryzen 7 9800X3D, 32GB of fast DDR5 RAM, and a Gigabyte X870E motherboard for $1,064.98, with the RAM costing you just $236."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/lenovos-legion-7a-gaming-laptop-now-comes-with-an-rtx-5070-12gb-gpu-option-but-it-costs-usd3-375-paired-with-a-ryzen-ai-9-cpu-sku-was-previously-limited-to-rtx-5060",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo's Legion 7a gaming laptop now comes with an RTX 5070 12GB GPU option — but it costs $3,375 paired with a Ryzen AI 9 CPU, SKU was previously limited to RTX 5060",
    "url": "https://www.tomshardware.com/laptops/lenovos-legion-7a-gaming-laptop-now-comes-with-an-rtx-5070-12gb-gpu-option-but-it-costs-usd3-375-paired-with-a-ryzen-ai-9-cpu-sku-was-previously-limited-to-rtx-5060",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T15:46:18+00:00",
    "summary": "Lenovo has added the RTX 5070 12GB GPU to its Legion 7a gaming laptop, allowing you finally configure it with something better than an RTX 5060. It's very expensive at $3,375 but you're getting a genu"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/irelands-data-centers-consumed-nearly-as-much-electricity-as-every-home-in-the-country-combined-in-2025-server-farms-gulped-23-percent-of-national-power-despite-years-of-grid-restrictions",
    "domain": "AI 算力 / 半导体",
    "title": "Ireland’s data centers consumed nearly as much electricity as every home in the country combined in 2025 — server farms gulped 23% of national power despite years of grid restrictions",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/irelands-data-centers-consumed-nearly-as-much-electricity-as-every-home-in-the-country-combined-in-2025-server-farms-gulped-23-percent-of-national-power-despite-years-of-grid-restrictions",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T15:12:09+00:00",
    "summary": "Ireland’s data centers consumed 23% of the country’s electricity in 2025, rising 10% in one year despite restrictions on new grid connections."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/sega-dreamcast-driver-fixes-appear-in-linux-7-2-rc3-fabled-console-remains-in-favor-while-iconic-computing-architectures-like-i486-fall-by-the-wayside",
    "domain": "AI 算力 / 半导体",
    "title": "Sega Dreamcast driver fixes appear in Linux 7.2-rc3 — fabled console remains in favor while iconic computing architectures like i486 fall by the wayside",
    "url": "https://www.tomshardware.com/software/linux/sega-dreamcast-driver-fixes-appear-in-linux-7-2-rc3-fabled-console-remains-in-favor-while-iconic-computing-architectures-like-i486-fall-by-the-wayside",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T14:51:53+00:00",
    "summary": "A set of updates for Sega Dreamcast hardware has been merged into the Linux 7.2-rc3 kernel this weekend."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-a-blazing-fast-dual-interface-m-2-ssd-enclosure-for-just-usd59-on-amazon-asus-tool-less-rog-strix-aiolos-is-14-percent-off-right-now-featuring-transfer-speeds-up-to-20-gbps",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a blazing-fast dual-interface M.2 SSD enclosure for just $59 on Amazon — Asus' tool-less ROG Strix Aiolos is 14% off right now, featuring transfer speeds up to 20 Gbps",
    "url": "https://www.tomshardware.com/pc-components/grab-a-blazing-fast-dual-interface-m-2-ssd-enclosure-for-just-usd59-on-amazon-asus-tool-less-rog-strix-aiolos-is-14-percent-off-right-now-featuring-transfer-speeds-up-to-20-gbps",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T14:02:10+00:00",
    "summary": "Asus' fancy dual-interface M.2 enclosure is marked down to its lowest price ever on Amazon right now. Not only is it fast, but it also looks clean and has extra on-the-go convenience thanks to its met"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/sothebys-video-showcases-working-apple-1-serial-number-01-0033-part-of-its-upcoming-history-of-science-and-technology-sale",
    "domain": "AI 算力 / 半导体",
    "title": "Sotheby’s video showcases working Apple-1 serial number 01-0033 — part of its upcoming History of Science & Technology sale",
    "url": "https://www.tomshardware.com/desktops/sothebys-video-showcases-working-apple-1-serial-number-01-0033-part-of-its-upcoming-history-of-science-and-technology-sale",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T13:08:56+00:00",
    "summary": "Sotheby’s is preparing a blockbuster History of Science & Technology sale packed with amazing artifacts and collectors’ items which includes a working Apple-1, serial number 01-0033."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/windows-95-detected-installers-by-scanning-program-names-for-the-word-setup",
    "domain": "AI 算力 / 半导体",
    "title": "Windows 95 didn’t detect installers, it ‘guessed’ based on the file name, says veteran dev — it simply checked for words like setup, install, inst, or localized equivalents",
    "url": "https://www.tomshardware.com/software/windows/windows-95-detected-installers-by-scanning-program-names-for-the-word-setup",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T12:48:34+00:00",
    "summary": "The full match list ran to six terms: setup, install, inst, imposta, ayarla, and felrak."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/fcc-approves-orbital-space-mirrors-first-test-satellites-will-launch-this-year-large-spacecraft-reflects-sunlight-to-earths-surface-for-construction-sites-search-and-rescue-lighting-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "FCC approves orbital space mirrors, first test satellites will launch this year — large spacecraft reflects sunlight to Earth’s surface for construction sites, search-and-rescue lighting, and more",
    "url": "https://www.tomshardware.com/tech-industry/fcc-approves-orbital-space-mirrors-first-test-satellites-will-launch-this-year-large-spacecraft-reflects-sunlight-to-earths-surface-for-construction-sites-search-and-rescue-lighting-and-more",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T12:20:20+00:00",
    "summary": "A startup that aims to bring sunlight on Earth after dark just received approval from the FCC to launch its experimental satellite. Critics say that the project could adversely affect astronomy and th"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/cooler-master-mwe-gold-750-v4-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "Cooler Master MWE Gold 750 V4 power supply review: Verified Gold efficiency with mainstream pricing",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/cooler-master-mwe-gold-750-v4-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T12:05:00+00:00",
    "summary": "The fourth revision of Cooler Master’s renowned mainstream series, coming with verified Gold efficiency, a native 12V-2x6 connector, and GPU Shield current monitoring in a compact 140 mm chassis at a "
  },
  {
    "id": "hn:48554206",
    "domain": "AI 算力 / 半导体",
    "title": "Semiconductor Lifeline Keeps Fighter Jets in the Air",
    "url": "https://spectrum.ieee.org/phoenix-semiconductors-legacychips-oems",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-06-16T12:31:02+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/alok-jain-the-engineer-who-never-wanted-to-be-a-manager/",
    "domain": "AI 算力 / 半导体",
    "title": "Alok Jain: The Engineer Who Never Wanted to Be a Manager",
    "url": "https://www.eetimes.com/alok-jain-the-engineer-who-never-wanted-to-be-a-manager/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T20:58:36+00:00",
    "summary": "Meet Alok Jain, the reluctant manager who turned Cadence India into a chip-design powerhouse—and see why AI is his next bet. The post Alok Jain: The Engineer Who Never Wanted to Be a Manager appeared "
  },
  {
    "id": "rss:https://www.eetimes.com/apples-30b-broadcom-deal-signals-expansions-in-ai-u-s-supply-chain/",
    "domain": "AI 算力 / 半导体",
    "title": "Apple’s $30B Broadcom Deal Signals Expansions in AI, U.S. Supply Chain",
    "url": "https://www.eetimes.com/apples-30b-broadcom-deal-signals-expansions-in-ai-u-s-supply-chain/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T12:50:28+00:00",
    "summary": "Apple’s $30B Broadcom bet drags AI data centers and U.S. chipmaking into its orbit… and may hand Intel a lifeline. The post Apple’s $30B Broadcom Deal Signals Expansions in AI, U.S. Supply Chain appea"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-energy-barrier-forces-system-technology-co-optimization/",
    "domain": "AI 算力 / 半导体",
    "title": "The Energy Barrier Reshaping AI Hardware",
    "url": "https://www.eetimes.com/ai-energy-barrier-forces-system-technology-co-optimization/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T07:18:59+00:00",
    "summary": "During Leti Innovation Days 2026, energy efficiency emerged as AI hardware’s next defining constraint. The post The Energy Barrier Reshaping AI Hardware appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/ivan-miranda-releases-files-for-a-3d-printed-electric-motorbike-that-fits-in-a-suitcase",
    "domain": "AI 算力 / 半导体",
    "title": "This 3D-printed electric motorbike folds into your luggage — creator warns it is 'super fast... way too fast'",
    "url": "https://www.tomshardware.com/3d-printing/ivan-miranda-releases-files-for-a-3d-printed-electric-motorbike-that-fits-in-a-suitcase",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T17:21:53+00:00",
    "summary": "Ivan Miranda has released the design files for the Mirandetta, a 3D-printed electric scooter that breaks down to fit inside a suitcase."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/hotspot-temperature-sensor-on-nvidias-blackwell-gaming-gpus-is-still-accessible-if-you-have-access-to-nvidias-internal-mods-tool-nvidia-rtx-5070-ti-caught-throttling-at-107-c-over-poor-tim-application",
    "domain": "AI 算力 / 半导体",
    "title": "Hotspot temperature sensor on Nvidia's Blackwell gaming GPUs is still accessible if you have access to Nvidia's internal MODS tool — Nvidia RTX 5070 Ti caught throttling at 107°C over poor TIM applica",
    "url": "https://www.tomshardware.com/pc-components/gpus/hotspot-temperature-sensor-on-nvidias-blackwell-gaming-gpus-is-still-accessible-if-you-have-access-to-nvidias-internal-mods-tool-nvidia-rtx-5070-ti-caught-throttling-at-107-c-over-poor-tim-application",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T16:18:59+00:00",
    "summary": "Nvidia decided to hide the hotspot temperature on its RTX 50 series, but internal diagnostic tools, such as Nvidia's own \"MODS,\" can still read it. The resulting data reveals how some GPUs can overhea"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/newegg-packs-ryzen-5-9600x-and-16gb-ddr5-into-a-usd520-combo-bundles-also-include-a-b650-motherboard-and-240mm-aio-liquid-cooler",
    "domain": "AI 算力 / 半导体",
    "title": "Newegg packs Ryzen 5 9600X and 16GB DDR5 into a $520 combo — bundles also include a B650 motherboard and 240mm AIO liquid cooler",
    "url": "https://www.tomshardware.com/pc-components/newegg-packs-ryzen-5-9600x-and-16gb-ddr5-into-a-usd520-combo-bundles-also-include-a-b650-motherboard-and-240mm-aio-liquid-cooler",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T15:29:17+00:00",
    "summary": "Gamers looking to build a budget-friendly AM5 PC can pick up a Ryzen 5 9600X, a Gigabyte B650M motherboard, and a Corsair DDR5 memory bundle, with a free 240mm liquid cooler included."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/xbox/brazilian-court-orders-microsoft-to-restore-a-gamers-account-and-digital-library-after-it-told-him-to-rebuy-his-games",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft loses Brazilian court case after telling hacked Xbox user to re-purchase games — tech giant ordered to restore Xbox account with all games and pay $400 in damages",
    "url": "https://www.tomshardware.com/video-games/xbox/brazilian-court-orders-microsoft-to-restore-a-gamers-account-and-digital-library-after-it-told-him-to-rebuy-his-games",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T14:52:11+00:00",
    "summary": "A Brazilian gamer who lost his Microsoft account and all his digital games has won a court order requiring the company to return them."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/bambu-lab-collabs-with-insta360-for-epic-design-contest-win-thousands-in-3d-printers-luna-ultra-cameras-and-gift-cards",
    "domain": "AI 算力 / 半导体",
    "title": "Bambu Lab collabs with Insta360 for epic design contest — win thousands in 3D printers, Luna Ultra cameras, and gift cards",
    "url": "https://www.tomshardware.com/3d-printing/bambu-lab-collabs-with-insta360-for-epic-design-contest-win-thousands-in-3d-printers-luna-ultra-cameras-and-gift-cards",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T14:31:45+00:00",
    "summary": "Your design concept could win a next-gen camera and 3D printer."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/amd-rx-9070-gre-collapses-to-usd499-to-save-1440p-gaming-rdna-4-price-slips-9-percent-to-steal-a-piece-of-nvidias-mid-range-pie",
    "domain": "AI 算力 / 半导体",
    "title": "AMD RX 9070 GRE collapses to $499 to save 1440p gaming — RDNA 4 price slips 9% to steal a piece of Nvidia's mid-range pie",
    "url": "https://www.tomshardware.com/pc-components/gpus/amd-rx-9070-gre-collapses-to-usd499-to-save-1440p-gaming-rdna-4-price-slips-9-percent-to-steal-a-piece-of-nvidias-mid-range-pie",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T14:23:57+00:00",
    "summary": "AMD's Radeon RX 9070 GRE has received its first price cut since launching outside China, making the 1440p-focused RDNA 4 graphics card a more compelling alternative to Nvidia's RTX 5060 Ti 16GB."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/sk-hynix-says-2027-will-be-the-worst-year-for-memory-shortage-forecasts-crunch-to-last-until-2030-ceo-shares-grim-outlook-on-the-day-sk-hynix-gets-listed-on-nasdaq",
    "domain": "AI 算力 / 半导体",
    "title": "SK Hynix says 2027 will be the 'worst year' for memory shortage, forecasts crunch to last until 2030 — CEO shares grim outlook on the day SK Hynix gets listed on Nasdaq",
    "url": "https://www.tomshardware.com/pc-components/dram/sk-hynix-says-2027-will-be-the-worst-year-for-memory-shortage-forecasts-crunch-to-last-until-2030-ceo-shares-grim-outlook-on-the-day-sk-hynix-gets-listed-on-nasdaq",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T13:00:00+00:00",
    "summary": "SK Hynix CEO Kwak Noh-jung says the memory shortage will get even worse in 2027, and claiming the RAM crunch will last at least until the turn of the decade."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/microsoft-struggles-to-fulfill-its-2030-sustainability-promise-amid-carbon-heavy-ai-expansions-the-companys-chief-sustainability-officer-claims-the-target-is-still-feasible",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft struggles to fulfill its 2030 sustainability promise amid carbon-heavy AI expansions — the company's chief sustainability officer claims the target is still feasible",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/microsoft-struggles-to-fulfill-its-2030-sustainability-promise-amid-carbon-heavy-ai-expansions-the-companys-chief-sustainability-officer-claims-the-target-is-still-feasible",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T12:45:00+00:00",
    "summary": "Microsoft's carbon emissions jumped 25% in FY2025 as AI data center expansion outpaced sustainability gains, despite progress in water conservation and waste reduction."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-chairs/razer-soma-chroma-gaming-chair-review",
    "domain": "AI 算力 / 半导体",
    "title": "Razer Soma Chroma Gaming Chair Review: Light on adjustability, but heavy on RGBs",
    "url": "https://www.tomshardware.com/peripherals/gaming-chairs/razer-soma-chroma-gaming-chair-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T12:05:00+00:00",
    "summary": "If you’d like a dose of RGBs to go with your gaming chair, the Soma Chroma delivers for $499."
  },
  {
    "id": "hn:48845518",
    "domain": "AI 算力 / 半导体",
    "title": "Reverse-engineering Nvidia's CUDA-checkpoint for faster cold starts",
    "url": "https://blog.doubleword.ai/what-happens-when-you-checkpoint-a-cuda-process",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-07-09T13:29:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48759308",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia offers startup customers chance to swap compute power for revenue share",
    "url": "https://www.cnbc.com/2026/07/02/nvidia-plans-to-offer-start-up-customers-access-to-revenue-sharing-deals.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-07-02T10:41:33+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/simplifying-intelligent-wireless-design-and-security-certification-for-healthcare-devices/",
    "domain": "AI 算力 / 半导体",
    "title": "Simplifying Intelligent Wireless Design and Security Certification for Healthcare Devices",
    "url": "https://www.eetimes.com/simplifying-intelligent-wireless-design-and-security-certification-for-healthcare-devices/",
    "source": "Infineon Technologies and Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T17:32:02+00:00",
    "summary": "Join Infineon Technologies and Ezurio for a 60-minute webinar exploring the challenges of designing and certifying secured wireless devices for healthcare applications. The post Simplifying Intelligen"
  },
  {
    "id": "rss:https://www.eetimes.com/voyager-spacecraft-the-ultimate-power-management-challenge/",
    "domain": "AI 算力 / 半导体",
    "title": "Voyager Spacecraft: The Ultimate Power Management Challenge?",
    "url": "https://www.eetimes.com/voyager-spacecraft-the-ultimate-power-management-challenge/",
    "source": "Bill Schweber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T14:00:00+00:00",
    "summary": "Voyager’s plutonium heart is fading, forcing NASA to kill instruments one by one; see how engineers ration watts 15B miles away. The post Voyager Spacecraft: The Ultimate Power Management Challenge? a"
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
    "id": "hn:48601996",
    "domain": "AI 算力 / 半导体",
    "title": "ASML denies US Government report that EUV chipmaking tool was shipped to China",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-denies-us-government-report-that-its-euv-chipmaking-tool-was-shipped-to-china-says-rumors-are-inaccurate-and-damaging-to-our-reputation",
    "source": "srameshc",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-06-19T19:03:30+00:00",
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
    "id": "hn:48662999",
    "domain": "大厂 AI 动态",
    "title": "Computer use in Gemini 3.5 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/",
    "source": "swolpers",
    "platform": "hackernews",
    "points": 242,
    "published_at": "2026-06-24T17:21:34+00:00",
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
    "id": "hn:48882949",
    "domain": "大厂 AI 动态",
    "title": "W11 Copilot tells you what's slowing down your PC, while using 1GB RAM itself",
    "url": "https://www.windowslatest.com/2026/07/12/windows-11-copilot-ai-can-now-tell-you-whats-slowing-down-your-pc-while-using-1gb-of-ram-itself/",
    "source": "speckx",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-12T17:45:57+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/965090/microsoft-windows-11-search-menu-ads",
    "domain": "大厂 AI 动态",
    "title": "Microsoft tests Windows Search without all the ads and fluff",
    "url": "https://www.theverge.com/tech/965090/microsoft-windows-11-search-menu-ads",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T21:53:20+00:00",
    "summary": "Microsoft is testing a cleaner version of the Windows 11 search menu that strips it of recommended content and ads. In a blog post on Monday, Microsoft announced that it's rolling out the decluttered "
  },
  {
    "id": "rss:https://www.theverge.com/tech/965084/oneplus-oppo-exit-us-europe",
    "domain": "大厂 AI 动态",
    "title": "OnePlus is reportedly bailing on the US",
    "url": "https://www.theverge.com/tech/965084/oneplus-oppo-exit-us-europe",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T21:48:43+00:00",
    "summary": "OnePlus and its parent company, Oppo, plan to announce in the coming days that OnePlus brand will be leaving the US and European markets, according to a machine translation of a WinFuture report. Shou"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/964914/dji-mic-three-bundle-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "A two-pack of DJI&#8217;s most capable wireless mics just got its first price cut",
    "url": "https://www.theverge.com/gadgets/964914/dji-mic-three-bundle-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T21:03:14+00:00",
    "summary": "Smartphones these days have incredible cameras that are capable of taking smooth, sharp video, but the microphones are often lacking, to say the least. A wireless lavalier microphone can dramatically "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/964982/shokz-openrun-pro-bone-conduction-headphones-summer-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The Shokz OpenRun Pro are the cheapest they’ve been since January",
    "url": "https://www.theverge.com/gadgets/964982/shokz-openrun-pro-bone-conduction-headphones-summer-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T20:57:44+00:00",
    "summary": "Noise-canceling earbuds are great for flights and focusing, but they're not always ideal for outdoor workouts. The last-gen Shokz OpenRun Pro's open-ear design lets you enjoy music while staying aware"
  },
  {
    "id": "rss:https://www.theverge.com/tech/964972/google-pixel-11-colors-rumor",
    "domain": "大厂 AI 动态",
    "title": "The Pixel colors might rule this year",
    "url": "https://www.theverge.com/tech/964972/google-pixel-11-colors-rumor",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T20:52:27+00:00",
    "summary": "This year's Google Pixel 11 lineup might come in a bunch of funky colors. A series of now-deleted Amazon listings spotted by 9to5Google show what appear to be placeholders for Google's upcoming Pixel "
  },
  {
    "id": "rss:https://www.theverge.com/tech/964307/apple-public-betas-ios-27-siri-ai",
    "domain": "大厂 AI 动态",
    "title": "Apple’s public betas for iOS 27 and more are out now",
    "url": "https://www.theverge.com/tech/964307/apple-public-betas-ios-27-siri-ai",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T20:45:40+00:00",
    "summary": "Apple has just released public betas for iOS 27 and other major OS updates that are set to publicly launch this fall. The big new feature this year is Siri AI, the delayed AI-powered revamp to Siri. I"
  },
  {
    "id": "rss:https://www.theverge.com/tech/964800/watchos-27-preview-siri-ai-apple-watch-gestures-smartwatch",
    "domain": "大厂 AI 动态",
    "title": "Siri AI makes the Apple Watch finally feel like a wrist computer",
    "url": "https://www.theverge.com/tech/964800/watchos-27-preview-siri-ai-apple-watch-gestures-smartwatch",
    "source": "Victoria Song",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T20:44:20+00:00",
    "summary": "Siri has been on the Apple Watch since day one, though I'm usually hard-pressed to find people who actually make good use of it. It's kind of just… been there - mostly as a way to set timers when my h"
  },
  {
    "id": "rss:https://www.theverge.com/tech/964714/siri-ai-public-beta-preview-ios-27-hands-on",
    "domain": "大厂 AI 动态",
    "title": "Siri AI is already changing how I use my iPhone",
    "url": "https://www.theverge.com/tech/964714/siri-ai-public-beta-preview-ios-27-hands-on",
    "source": "David Imel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T20:43:20+00:00",
    "summary": "iOS 27 escaped the developer world today with the launch of the first public beta. I've been testing the new operating system since early June, looking for quirks and seeing if it can live up to the h"
  },
  {
    "id": "rss:https://www.theverge.com/tech/964701/apple-macos-27-golden-gate-public-beta-impressions-liquid-glass-siri-ai",
    "domain": "大厂 AI 动态",
    "title": "The macOS 27 public beta is worth it just for the Liquid Glass tweaks",
    "url": "https://www.theverge.com/tech/964701/apple-macos-27-golden-gate-public-beta-impressions-liquid-glass-siri-ai",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T20:43:15+00:00",
    "summary": "The macOS 27 Golden Gate public beta is here, and anyone with an M-series Mac now has easier access to test-drive Apple's latest changes - including a more subdued Liquid Glass aesthetic. That's reaso"
  },
  {
    "id": "rss:https://www.theverge.com/policy/964916/paramount-warner-bros-discovery-states-lawsuit",
    "domain": "大厂 AI 动态",
    "title": "States make last-ditch effort to stop the Paramount ‘media behemoth’",
    "url": "https://www.theverge.com/policy/964916/paramount-warner-bros-discovery-states-lawsuit",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T18:35:48+00:00",
    "summary": "A dozen state attorneys general are trying to block the $110 billion merger of Paramount and Warner Bros Discovery they warn would raise movie prices and crush cable TV distributors. The states - Cali"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/already-rich-already-successful-why-the-last-wave-of-tech-winners-is-grinding-again/",
    "domain": "大厂 AI 动态",
    "title": "Already rich, already successful, why the last wave of tech winners is grinding again",
    "url": "https://techcrunch.com/2026/07/13/already-rich-already-successful-why-the-last-wave-of-tech-winners-is-grinding-again/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T02:46:42+00:00",
    "summary": "They're rolling up their sleeves again, seemingly out of fear of missing AI's defining moment and, presumably, the irresistible allure of making even more money -- potentially a lot more."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/ubers-product-chief-on-hotels-robotaxis-and-why-the-company-doesnt-want-to-be-everything-for-everyone/",
    "domain": "大厂 AI 动态",
    "title": "Uber’s product chief on hotels, robotaxis, and why the company doesn’t want to be “everything for everyone”",
    "url": "https://techcrunch.com/2026/07/13/ubers-product-chief-on-hotels-robotaxis-and-why-the-company-doesnt-want-to-be-everything-for-everyone/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T00:45:00+00:00",
    "summary": "Uber Chief Product Officer Sachin Kansal walks TechCrunch through the company's financial-services ambitions, its increasingly complicated relationship with Waymo, its new AV Labs data operation, and "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/video-generation-startup-pixverse-raises-439m-valuation-soars-past-2b/",
    "domain": "大厂 AI 动态",
    "title": "Video-generation startup PixVerse raises $439M, valuation soars past $2B",
    "url": "https://techcrunch.com/2026/07/13/video-generation-startup-pixverse-raises-439m-valuation-soars-past-2b/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T00:00:00+00:00",
    "summary": "With the cash, the company aims to expand its world model offering and reach customers across geographies."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/x-just-tweaked-its-algorithm-to-make-it-more-friendly-less-battleground/",
    "domain": "大厂 AI 动态",
    "title": "X just tweaked its algorithm to make it more friendly, less battleground",
    "url": "https://techcrunch.com/2026/07/13/x-just-tweaked-its-algorithm-to-make-it-more-friendly-less-battleground/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T23:58:27+00:00",
    "summary": "The social media site says it will amplify posts made by users' mutual followers' to give the feed more of a communal feel."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/hermes-agent-maker-nous-research-in-talks-for-new-funding-at-1-5b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Hermes agent maker Nous Research in talks for new funding at $1.5B valuation",
    "url": "https://techcrunch.com/2026/07/13/hermes-agent-maker-nous-research-in-talks-for-new-funding-at-1-5b-valuation/",
    "source": "Ivan Mehta, Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T23:31:18+00:00",
    "summary": "The company is raising at least $75 million, led by Robot Ventures, with significant participation from USV and other prominent investors."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/satya-nadella-has-issued-a-shocking-warning-to-companies-using-ai/",
    "domain": "大厂 AI 动态",
    "title": "Satya Nadella has issued a shocking warning to companies using AI",
    "url": "https://techcrunch.com/2026/07/13/satya-nadella-has-issued-a-shocking-warning-to-companies-using-ai/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T20:59:00+00:00",
    "summary": "Of all the debates raging about the potential downsides of AI, there is one worry causing the most hand-wringing among AI enthusiasts in Silicon Valley — that the giant AI labs that sell proprietary m"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/apple-says-former-employee-exploited-rare-bug-to-download-confidential-files-after-leaving-for-openai/",
    "domain": "大厂 AI 动态",
    "title": "Apple says former employee exploited ‘rare’ bug to download confidential files after leaving for OpenAI",
    "url": "https://techcrunch.com/2026/07/13/apple-says-former-employee-exploited-rare-bug-to-download-confidential-files-after-leaving-for-openai/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T20:00:17+00:00",
    "summary": "Apple would not comment on the \"security breach,\" which allegedly allowed a former employee to download sensitive files from Apple's network long after he departed the company for rival OpenAI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/the-wildest-allegations-in-apples-trade-secrets-lawsuit-against-openai/",
    "domain": "大厂 AI 动态",
    "title": "The wildest allegations in Apple’s trade secrets lawsuit against OpenAI",
    "url": "https://techcrunch.com/2026/07/13/the-wildest-allegations-in-apples-trade-secrets-lawsuit-against-openai/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T18:22:10+00:00",
    "summary": "Apple’s trade secrets lawsuit against OpenAI contains allegations that range from employees joking about unauthorized access to Apple’s systems to claims that job candidates were asked to bring Apple "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/sam-altmans-space-data-center-trash-talk-is-what-most-experts-already-believe/",
    "domain": "大厂 AI 动态",
    "title": "Sam Altman’s space data center trash talk is what most experts already believe",
    "url": "https://techcrunch.com/2026/07/13/sam-altmans-space-data-center-trash-talk-is-what-most-experts-already-believe/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T17:28:37+00:00",
    "summary": "Responding to Musk accusing him of being a scammer, Altman said, \"homeboy you're the one sellling [sic] public market investors on short-term space datacenters.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/investors-send-general-fusion-soaring-in-debut-as-first-publicly-traded-fusion-company/",
    "domain": "大厂 AI 动态",
    "title": "Investors send General Fusion soaring in debut as first publicly traded fusion company",
    "url": "https://techcrunch.com/2026/07/13/investors-send-general-fusion-soaring-in-debut-as-first-publicly-traded-fusion-company/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T17:03:11+00:00",
    "summary": "General Fusion started trading on the Nasdaq following a reverse merger that saw high redemptions."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/12-states-sue-to-block-paramounts-110b-warner-bros-deal/",
    "domain": "大厂 AI 动态",
    "title": "12 states sue to block Paramount’s $110B Warner Bros. deal",
    "url": "https://techcrunch.com/2026/07/13/12-states-sue-to-block-paramounts-110b-warner-bros-deal/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T17:00:14+00:00",
    "summary": "The states allege that the deal would harm movie theaters, basic cable distributors, and audiences."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/should-ai-help-you-get-away-with-killing-your-spouse/",
    "domain": "大厂 AI 动态",
    "title": "Should AI help you get away with killing your spouse?",
    "url": "https://techcrunch.com/2026/07/13/should-ai-help-you-get-away-with-killing-your-spouse/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T16:31:23+00:00",
    "summary": "What does a world of total user-aligned AI actually look like?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/as-tv-tracking-app-tv-time-shuts-down-its-founder-builds-bingers-a-new-home-for-fans/",
    "domain": "大厂 AI 动态",
    "title": "As TV-tracking app TV Time shuts down, its founder builds Bingers, a new home for fans",
    "url": "https://techcrunch.com/2026/07/13/as-tv-tracking-app-tv-time-shuts-down-its-founder-builds-bingers-a-new-home-for-fans/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T15:49:42+00:00",
    "summary": "The creator of TV Time is building a successor app that will let users import their watch histories and preserve the community that formed around discussing their favorite shows."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/anthropic-starts-localizing-claude-pricing-for-india-its-biggest-market-after-the-us/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic starts localizing Claude pricing for India, its biggest market after the US",
    "url": "https://techcrunch.com/2026/07/13/anthropic-starts-localizing-claude-pricing-for-india-its-biggest-market-after-the-us/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T15:34:59+00:00",
    "summary": "Claude users in India are starting to see Indian rupee-denominated subscription plans."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/spacex-cleared-to-fly-starship-again-after-booster-failure-in-may/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX cleared to fly Starship again after booster failure in May",
    "url": "https://techcrunch.com/2026/07/13/spacex-cleared-to-fly-starship-again-after-booster-failure-in-may/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T14:19:44+00:00",
    "summary": "This will be the first Starship test flight for SpaceX as a public company, testing the market's appetite for the company's \"fly, fail, fix\" approach to rocket development, which often ends in firebal"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/waze-adds-new-ai-powered-features-and-customization-updates/",
    "domain": "大厂 AI 动态",
    "title": "Waze adds new AI-powered features and customization updates",
    "url": "https://techcrunch.com/2026/07/13/waze-adds-new-ai-powered-features-and-customization-updates/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T14:18:16+00:00",
    "summary": "Some of the new features are powered by Google's Gemini AI assistant, which reflects the tech giant's broader push to integrate Gemini across its products while also better positioning Waze to compete"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/lapd-lets-contract-with-surveillance-giant-flock-expire-citing-serious-concerns-over-civil-liberties-and-privacy/",
    "domain": "大厂 AI 动态",
    "title": "LAPD lets contract with surveillance giant Flock expire, citing ‘serious concerns’ over civil liberties and privacy",
    "url": "https://techcrunch.com/2026/07/13/lapd-lets-contract-with-surveillance-giant-flock-expire-citing-serious-concerns-over-civil-liberties-and-privacy/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T14:13:38+00:00",
    "summary": "The LAPD, one of Flock's biggest government customers, is ending its contract with the company citing civil liberties concerns."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/13/ubers-robotaxi-lobbying-effort-has-put-it-on-a-collision-course-with-waymo/",
    "domain": "大厂 AI 动态",
    "title": "Uber’s robotaxi lobbying effort puts it on a collision course with Waymo",
    "url": "https://techcrunch.com/2026/07/13/ubers-robotaxi-lobbying-effort-has-put-it-on-a-collision-course-with-waymo/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T12:30:00+00:00",
    "summary": "Washington, D.C. has become a battleground for Uber and Waymo's competing views."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/12/techcrunch-mobility-a-robotaxi-ultimatum/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: A robotaxi ultimatum",
    "url": "https://techcrunch.com/2026/07/12/techcrunch-mobility-a-robotaxi-ultimatum/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T16:07:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, how AI is playing a part."
  },
  {
    "id": "rss:https://stratechery.com/2026/apple-sues-openai-apples-real-problem/",
    "domain": "大厂 AI 动态",
    "title": "Apple Sues OpenAI, Apple’s Real Problem",
    "url": "https://stratechery.com/2026/apple-sues-openai-apples-real-problem/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T10:00:00+00:00",
    "summary": "Apple is suing AI for stealing trade secrets; there is one guilty employee, but this mostly feels like lashing out."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/spacex-is-gearing-up-for-starships-13th-test-flight-later-this-week/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX is gearing up for Starship's 13th test flight later this week",
    "url": "https://arstechnica.com/space/2026/07/spacex-is-gearing-up-for-starships-13th-test-flight-later-this-week/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T01:17:14+00:00",
    "summary": "This flight will put Starship under higher pressure and test out new Starlink satellites in orbit."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/us-continues-to-shun-ebola-infected-citizens-second-american-sent-to-germany/",
    "domain": "大厂 AI 动态",
    "title": "US continues to shun Ebola-infected citizens; second American sent to Germany",
    "url": "https://arstechnica.com/health/2026/07/us-continues-to-shun-ebola-infected-citizens-second-american-sent-to-germany/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T22:07:34+00:00",
    "summary": "The man is said to be doing well in a Frankfurt hospital."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/07/the-us-government-warns-that-russia-state-hackers-are-coming-after-your-router/",
    "domain": "大厂 AI 动态",
    "title": "The US government warns that Russia state hackers are coming after your router",
    "url": "https://arstechnica.com/security/2026/07/the-us-government-warns-that-russia-state-hackers-are-coming-after-your-router/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T21:03:07+00:00",
    "summary": "With residential proxies all the rage, CISA urges router users to be vigilant."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/ukrainian-drone-strikes-forced-russia-to-stop-shipping-in-vital-sea-corridor/",
    "domain": "大厂 AI 动态",
    "title": "Ukrainian drone strikes forced Russia to stop shipping in vital sea corridor",
    "url": "https://arstechnica.com/gadgets/2026/07/ukrainian-drone-strikes-forced-russia-to-stop-shipping-in-vital-sea-corridor/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T20:41:26+00:00",
    "summary": "Ukraine’s drone blitz halted Russia’s Sea of Azov shipping in under a week."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/07/first-time-ev-buyers-in-california-can-now-claim-a-new-rebate/",
    "domain": "大厂 AI 动态",
    "title": "California creates $3,500 rebate for new electric vehicle buyers",
    "url": "https://arstechnica.com/cars/2026/07/first-time-ev-buyers-in-california-can-now-claim-a-new-rebate/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T19:52:48+00:00",
    "summary": "There's a separate $1,750 rebate for used EVs, but both rebates have a price cap."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/apple-sues-openai-after-ex-engineer-allegedly-used-bug-to-steal-trade-secrets/",
    "domain": "大厂 AI 动态",
    "title": "Apple sues OpenAI after ex-engineer allegedly used bug to steal trade secrets",
    "url": "https://arstechnica.com/tech-policy/2026/07/apple-sues-openai-after-ex-engineer-allegedly-used-bug-to-steal-trade-secrets/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T19:17:51+00:00",
    "summary": "OpenAI accused of conspiring with former Apple employees to steal trade secrets."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/solution-to-feynmans-reverse-sprinkler-puzzle-also-applies-to-silly-sprinklers/",
    "domain": "大厂 AI 动态",
    "title": "Solution to Feynman's reverse sprinkler puzzle also applies to \"silly sprinklers\"",
    "url": "https://arstechnica.com/science/2026/07/solution-to-feynmans-reverse-sprinkler-puzzle-also-applies-to-silly-sprinklers/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T19:00:47+00:00",
    "summary": "New study confirms 2024 \"momentum flux theory\" on how angular momentum of water flows drives rotation."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/states-sue-to-block-paramount-wbd-merger-that-was-approved-by-trump-admin/",
    "domain": "大厂 AI 动态",
    "title": "States sue to block Paramount/WBD merger that was approved by Trump admin",
    "url": "https://arstechnica.com/tech-policy/2026/07/states-sue-to-block-paramount-wbd-merger-that-was-approved-by-trump-admin/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T18:34:35+00:00",
    "summary": "AG: Deal will bring \"higher prices, lower quality, and less content for film and TV.\""
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/07/digger-trailer-is-giving-big-dr-strangelove-vibes/",
    "domain": "大厂 AI 动态",
    "title": "Tom Cruise is utterly transformed in Digger trailer",
    "url": "https://arstechnica.com/culture/2026/07/digger-trailer-is-giving-big-dr-strangelove-vibes/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T17:49:56+00:00",
    "summary": "\"If we can't control the force of nature, at least we can control the narrative.\""
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/apple-and-samsung-benefit-as-memory-shortage-pushes-smartphone-shipments-to-historic-lows/",
    "domain": "大厂 AI 动态",
    "title": "Apple and Samsung benefit as memory shortage pushes smartphone shipments to historic lows",
    "url": "https://arstechnica.com/gadgets/2026/07/apple-and-samsung-benefit-as-memory-shortage-pushes-smartphone-shipments-to-historic-lows/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T17:18:25+00:00",
    "summary": "The biggest smartphone makers keep on trucking in the face of component shortages and economic uncertainty."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/colorado-will-decide-whether-a-right-to-natural-gas-is-added-to-state-constitution/",
    "domain": "大厂 AI 动态",
    "title": "Colorado will decide whether a \"right to natural gas\" is added to state constitution",
    "url": "https://arstechnica.com/tech-policy/2026/07/colorado-will-decide-whether-a-right-to-natural-gas-is-added-to-state-constitution/",
    "source": "Maya McDaniel, Inside Climate News",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T16:49:35+00:00",
    "summary": "The amendment would restrict building codes that promote electrification."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/07/hackers-quickly-prove-that-neo-geo-doom-ports-are-not-impossible/",
    "domain": "大厂 AI 动态",
    "title": "Hackers quickly prove that Neo Geo Doom ports are not \"impossible\"",
    "url": "https://arstechnica.com/gaming/2026/07/hackers-quickly-prove-that-neo-geo-doom-ports-are-not-impossible/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T16:37:14+00:00",
    "summary": "Clever coding and graphical compromises get a classic game on more classic hardware."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/what-happens-if-crew-dragon-stops-flying-in-the-2030s/",
    "domain": "大厂 AI 动态",
    "title": "A \"disaster waiting to happen\"? Industry officials worry about Crew Dragon availability.",
    "url": "https://arstechnica.com/space/2026/07/what-happens-if-crew-dragon-stops-flying-in-the-2030s/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T16:05:03+00:00",
    "summary": "\"It's very clear that in the United States there is a big need for an additional crew vehicle.\""
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/07/now-defenders-are-embracing-the-prompt-injection-too/",
    "domain": "大厂 AI 动态",
    "title": "Now, defenders are embracing the prompt injection, too",
    "url": "https://arstechnica.com/security/2026/07/now-defenders-are-embracing-the-prompt-injection-too/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T15:06:34+00:00",
    "summary": "\"Context bombing\" tricks hacking agents into shutting down before they can do harm."
  },
  {
    "id": "hn:48678873",
    "domain": "股票",
    "title": "OpenAI leans toward waiting until next year for IPO",
    "url": "https://www.nytimes.com/2026/06/25/technology/openai-ipo-artificial-intelligence.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 179,
    "published_at": "2026-06-25T20:36:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:48899454",
    "domain": "股票",
    "title": "$65K to work at Anthropic? Debate ensues amid IPO wave",
    "url": "https://missionlocal.org/2026/07/anthropic-sf-affordability-ipo-housing-evictions-rent/",
    "source": "gcheong",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-07-13T21:56:52+00:00",
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
    "id": "wscn:3776859",
    "domain": "股票",
    "title": "韩股深V反弹，一度跌超5%后转涨，中东局势持续升温、原油上涨，黄金小幅上扬",
    "url": "https://wallstreetcn.com/articles/3776859",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T05:24:52+00:00",
    "summary": "韩国KOSPI指数日内再度涨超1%，SK海力士涨2.9%，三星电子涨4%。WTI原油期货则在今日亚洲盘中进一步涨至每桶80美元上方，布伦特一度突破85美元。现货黄金上涨至4020美元。"
  },
  {
    "id": "wscn:3776790",
    "domain": "股票",
    "title": "成品油裂口：原油供给假宽松下的真紧缺",
    "url": "https://wallstreetcn.com/premium/articles/3776790?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T05:16:03+00:00",
    "summary": "原油供应宽松表象掩盖成品油结构性短缺，炼能瓶颈或推升裂解价差、能源通胀上行。"
  },
  {
    "id": "wscn:3776864",
    "domain": "股票",
    "title": "华尔街不担心资本开支！大摩：明年五大云厂资本开支1.2万亿美元，2028年1.4万亿美元，算力翻四倍",
    "url": "https://wallstreetcn.com/articles/3776864",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:41:12+00:00",
    "summary": "摩根士丹利认为，资本开支上调的主要推手包括GPU成本上涨约20%、数据中心建设周期拉长至3年，以及政治压力倒逼提前开工。更关键的是，资本开支背后是近4倍的算力扩张，将从2025年约30GW增至2028年约120GW，而Meta、亚马逊等的潜在收入空间远未被市场定价。"
  },
  {
    "id": "wscn:3776862",
    "domain": "股票",
    "title": "创业板午后涨超3%，算力硬件反攻、光模块大涨，恒科指翻红，科网股回暖、百度重挫9%",
    "url": "https://wallstreetcn.com/articles/3776862",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:06:26+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市超3100股飘绿，上午半天成交1.64万亿。沪深两市半日成交额1.63万亿，较上个交易日缩量近2300亿。板块方面，商业航天概念股掀跌停潮；半导体、算力硬件产业链持续回调，服务器、云计算方向领跌；AI应用、光伏、机器人题材跌幅靠前。煤炭、油气、零售、医药生物板块逆势走强。"
  },
  {
    "id": "wscn:3776740",
    "domain": "股票",
    "title": "韩国，又一次站在了可以跳下去的高处",
    "url": "https://wallstreetcn.com/premium/articles/3776740?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T03:54:46+00:00",
    "summary": "不怕一万，就怕万一。"
  },
  {
    "id": "wscn:3776872",
    "domain": "股票",
    "title": "韩国央行驳斥半导体见顶论：AI驱动需求持续超越供给，上行周期延伸至2026年",
    "url": "https://wallstreetcn.com/articles/3776872",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T03:52:41+00:00",
    "summary": "AI基础设施投资浪潮之下，韩国央行罕见强势发声：当前半导体上行周期不仅完好，更已超越历史均值40个月，且强度远超以往。供给瓶颈叠加AI驱动的竞争性投资，令本轮扩张逻辑迥异于过去。"
  },
  {
    "id": "wscn:3776863",
    "domain": "股票",
    "title": "AI投资热潮驱动！中国6月出口同比大增27%远超预期，创逾四年新高，上半年出口同比增长17.6%",
    "url": "https://wallstreetcn.com/articles/3776863",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T03:28:11+00:00",
    "summary": "上半年，出口结构持续向高端制造倾斜，高技术产品出口同比大增39%，机电产品占出口总值比重升至63.5%，自主品牌出口增速达25.4%。海关总署副署长王军在国新办新闻发布会上表示，上半年，我国电子元件、电脑零部件等算力硬件进出口额度达到5.13万亿元，增长56.6%。"
  },
  {
    "id": "wscn:3776824",
    "domain": "股票",
    "title": "MPV，没出现ModelY时刻",
    "url": "https://wallstreetcn.com/articles/3776824",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T03:22:58+00:00",
    "summary": "老牌车企的AI兑现节点。"
  },
  {
    "id": "wscn:3776866",
    "domain": "股票",
    "title": "如何监管单股杠杆ETF？周四，全市场都盯着韩国政府这场会",
    "url": "https://wallstreetcn.com/articles/3776866",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T03:21:39+00:00",
    "summary": "韩国单股杠杆ETF上线仅约一个半月，KOSPI周一单日暴跌逾8%，触发年内第七次熔断。该国政府高层经济协调机制将于周四召开会议，正式讨论单股杠杆ETF引发市场波动的应对措施。市场讨论的可能措施包括提高保证金要求、限制每日价格波动幅度、调整杠杆比例，但监管层坦言这些或仅为治标之策。"
  },
  {
    "id": "wscn:3776757",
    "domain": "股票",
    "title": "大模型7月激战：国产性能快速攀升，海外巨头开启价格战",
    "url": "https://wallstreetcn.com/premium/articles/3776757?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T03:21:22+00:00",
    "summary": "全球AI大模型正从“百模大战”的混沌期迈入“诸侯混战”的格局重塑期，能力代差快速收窄、资本开支持续膨胀、开源生态加速全球化。"
  },
  {
    "id": "wscn:3776867",
    "domain": "股票",
    "title": "新鲜零食的风口，卡在高周转和高损耗之间",
    "url": "https://wallstreetcn.com/articles/3776867",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T02:43:16+00:00",
    "summary": "抛弃风口幻想"
  },
  {
    "id": "wscn:3776865",
    "domain": "股票",
    "title": "油价后续怎么走？最大的悬念是：中国！",
    "url": "https://wallstreetcn.com/articles/3776865",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T02:07:56+00:00",
    "summary": "美伊战火未能推高油价，真正的\"幕后主角\"是中国，今春中国石油进口骤降三分之一，意外成为全球油价的稳定器。但随着采购信号隐现，市场屏息等待中国的下一步动作——欧亚集团分析师直言，中国的市场定价权已超越沙特与美国。霍尔木兹变局之下，中国何时出手，将决定油价命运。"
  },
  {
    "id": "wscn:3776861",
    "domain": "股票",
    "title": "高盛韩国交易员的一线观察：韩股“持续且痛苦”的去杠杆，“多头”基金沉默",
    "url": "https://wallstreetcn.com/articles/3776861",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T02:06:26+00:00",
    "summary": "高盛表示，韩国KOSPI单日暴跌9%，这场暴跌并非基本面恶化，而是一场由单股杠杆ETF集中去杠杆引爆的仓位清洗。外资与本地机构合计净卖出超26亿美元，净多头机构却异常沉默。高盛认为，这是流动性危机，不是周期顶部，极端波动或正是布局存储芯片的窗口。"
  },
  {
    "id": "wscn:3776860",
    "domain": "股票",
    "title": "国投证券：类比2021年“茅指数”，黄金历史大顶已经基本明确",
    "url": "https://wallstreetcn.com/articles/3776860",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T01:40:47+00:00",
    "summary": "黄金与AI，2026年的终极决胜时刻正在到来。国投证券策略分析师指出，黄金已现类似2021年\"茅指数\"的顶部信号——美元从\"弱\"变\"不弱\"，AI资本开支催生新美元循环，科技崛起对黄金的抽血效应或比加息更致命。信仰先松，证据后到，天平正悄然倾斜。"
  },
  {
    "id": "wscn:3776857",
    "domain": "股票",
    "title": "华尔街最大清算机构启动区块链实盘测试，股票代币化迈出关键一步",
    "url": "https://wallstreetcn.com/articles/3776857",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T01:10:17+00:00",
    "summary": "美国最大证券清算机构DTCC本周启动区块链实盘测试，涉及股票、国债等资产，是这家美国最大清算机构多年探索后首次在真实环境中验证代币化流程，全面上线目标定于10月。但DTCC明确，区块链无法替代每日处理约20万亿美元交易的净额结算体系，当前最现实的应用场景是抵押品融资与连接加密市场的周末结算。"
  },
  {
    "id": "wscn:3776854",
    "domain": "股票",
    "title": "美联储五大工作组的“大脑”",
    "url": "https://wallstreetcn.com/articles/3776854",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T01:08:43+00:00",
    "summary": "华创证券认为，美联储五大工作组名单获市场专业认可，但改革落地仍需FOMC共识。各组核心方向为： 1. 沟通组：少承诺具体路径，多解释机制； 2. 资产组：审视扩表风险与结构优化； 3. 数据组：拓展高频与微观数据； 4. 生产率组：看好AI长期经济前景； 5. 通胀组：强调目标灵活性并纳入金融周期。"
  },
  {
    "id": "wscn:3776851",
    "domain": "股票",
    "title": "华泰证券：如何看待韩股未来走势？",
    "url": "https://wallstreetcn.com/articles/3776851",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T01:06:10+00:00",
    "summary": "华泰证券认为， 韩股近期回撤并非基本面恶化，而是高杠杆（尤其是杠杆ETF）引发的技术性调整。目前杠杆尚未真正出清，短期需警惕赎回压力与监管政策落地的风险。中长期看，韩股走势仍取决于半导体产业基本面，当前的去杠杆将为后续健康上涨奠定基础。"
  },
  {
    "id": "wscn:3776852",
    "domain": "股票",
    "title": "中金：当前回调或已反映过度悲观预期",
    "url": "https://wallstreetcn.com/articles/3776852",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T00:43:40+00:00",
    "summary": "上证指数年内收益率再度转负，自5月中旬以来回撤幅度已接近3月美伊局势引发的调整。中金策略团队认为，此轮下跌主要源于海外AI负面叙事、韩国杠杆ETF踩踏及地缘风险扰动，当前估值已隐含过度悲观预期。随着云厂商业绩披露与杠杆加速出清，反弹或在1-2周内随时到来，中期慢牛逻辑未变。"
  },
  {
    "id": "wscn:3776856",
    "domain": "股票",
    "title": "韩国股市暴跌，韩元为何反而升值？",
    "url": "https://wallstreetcn.com/articles/3776856",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T00:43:03+00:00",
    "summary": "韩元今年上演“反常剧本”——股市涨它偏跌，股市跌它反而升。背后逻辑直指外资持股的外汇对冲机制：KOSPI每波动1%，即触发约16亿美元的对冲调整。随着SK海力士赴美募资265亿美元启动结汇，韩元强势突破1500关口。韩元正加速“日元化”，与股市的负相关或成新常态。"
  },
  {
    "id": "hn:48612095",
    "domain": "股票",
    "title": "Show HN: My Windows XP portfolio with working Game Boy and iPod",
    "url": "https://mitchivin.com/",
    "source": "mitchivin",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-06-20T19:18:48+00:00",
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
    "id": "hn:48634931",
    "domain": "股票",
    "title": "SpaceX Drops 14% in One Day, Price Now Below IPO Launch",
    "url": "https://finance.yahoo.com/quote/SPCX/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-06-22T19:33:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:48824532",
    "domain": "股票",
    "title": "SpaceX Shares Stumble in Nasdaq-100 Debut",
    "url": "https://www.wsj.com/finance/stocks/spacex-shares-stumble-in-nasdaq-100-debut-9ec10565",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-07T22:00:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48853145",
    "domain": "股票",
    "title": "California universities stockpiling AR-15s, grenades and submachine guns",
    "url": "https://www.theguardian.com/us-news/2026/jul/09/california-universities-military-equipment",
    "source": "sizzle",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-09T22:20:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:48846617",
    "domain": "股票",
    "title": "Sony CEO Just Sold over Half His Stock",
    "url": "https://gamerant.com/sony-ceo-sells-stock/",
    "source": "josephcsible",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-09T14:37:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:48826804",
    "domain": "股票",
    "title": "AI has taken over the stock market. The bond market is next",
    "url": "https://www.economist.com/finance-and-economics/2026/07/07/ai-has-taken-over-the-stock-market-the-bond-market-is-next",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-07-08T02:32:38+00:00",
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
    "id": "hn:48748464",
    "domain": "股票",
    "title": "The Stockholm Telephone Tower with Approximately 5,500 Telephone Lines, 1890",
    "url": "https://rarehistoricalphotos.com/the-stockholm-telephone-tower-1890/",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-07-01T15:27:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48774424",
    "domain": "股票",
    "title": "X has suddenly banned an account documenting Trump's corrupt stock trades",
    "url": "https://twitter.com/HQNewsNow/status/2072699828337864871",
    "source": "doener",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-07-03T12:52:15+00:00",
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
    "id": "hn:48598558",
    "domain": "股票",
    "title": "The average SpaceX buyer post-IPO is almost under water after two-day slide",
    "url": "https://www.cnbc.com/2026/06/18/the-average-spacex-buyer-post-ipo-is-almost-under-water-after-two-day-slide.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 40,
    "published_at": "2026-06-19T13:48:28+00:00",
    "summary": ""
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
    "id": "hn:48777130",
    "domain": "股票",
    "title": "Tesla stock sinks 7% despite strong deliveries report, worst day in nearly 1y",
    "url": "https://www.cnbc.com/2026/07/02/tesla-tsla-q2-2026-vehicle-delivery-production.html",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-03T16:52:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:48789829",
    "domain": "股票",
    "title": "Ask HN: When will the stock market crash?",
    "url": "https://news.ycombinator.com/item?id=48789829",
    "source": "roschdal",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-04T22:55:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:48553976",
    "domain": "股票",
    "title": "SpaceX to acquire Cursor for $60B in stock, days after blockbuster IPO",
    "url": "https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/",
    "source": "frb",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-06-16T12:09:34+00:00",
    "summary": ""
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
    "id": "hn:48714428",
    "domain": "股票",
    "title": "SpaceX just landed in 401(k)s due to key index rule changes",
    "url": "https://moneywise.com/news/top-stories/spacex-401k-anthropic-openai-ipo-index-fund-rules",
    "source": "voxadam",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-06-29T03:25:05+00:00",
    "summary": ""
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
    "id": "hn:48552687",
    "domain": "金融",
    "title": "Feds freaked over Fable 5 after 'fix this code', not jailbreak, say researchers",
    "url": "https://www.theregister.com/security/2026/06/15/feds-freaked-over-fable-5-after-simple-fix-this-code-prompt-not-jailbreak-says-researcher/5255827",
    "source": "_tk_",
    "platform": "hackernews",
    "points": 613,
    "published_at": "2026-06-16T09:26:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:48634585",
    "domain": "金融",
    "title": "Canada plans 'nuclear renaissance' with up to 10 reactors built by 2040",
    "url": "https://www.cbc.ca/news/politics/federal-nuclear-strategy-9.7244509",
    "source": "geox",
    "platform": "hackernews",
    "points": 593,
    "published_at": "2026-06-22T19:06:48+00:00",
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
    "id": "hn:48647444",
    "domain": "金融",
    "title": "Digital euro clears key hurdle as EU seeks to break free from U.S. credit cards",
    "url": "https://finance.yahoo.com/markets/currencies/articles/ecb-secures-key-parliamentary-backing-102718449.html",
    "source": "madars",
    "platform": "hackernews",
    "points": 232,
    "published_at": "2026-06-23T16:27:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48892638",
    "domain": "金融",
    "title": "Benchmarking 15 “E-Waste” GPUs with Modern Workloads",
    "url": "https://esologic.com/benchmarking-tesla-gpus/",
    "source": "eso_logic",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-07-13T13:48:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:48673787",
    "domain": "金融",
    "title": "Federal agents track down woman, demand she remove Instagram post about ICE",
    "url": "https://www.syracuse.com/news/2026/06/federal-agents-track-down-syracuse-woman-demand-she-remove-instagram-post-about-ice.html",
    "source": "coloneltcb",
    "platform": "hackernews",
    "points": 217,
    "published_at": "2026-06-25T14:16:17+00:00",
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
    "id": "rss:https://arxiv.org/abs/2607.09951",
    "domain": "金融",
    "title": "Macroeconomic Risks from Maritime Trade Disruptions",
    "url": "https://arxiv.org/abs/2607.09951",
    "source": "Vipin P. Veetil, Fathimath S. Vemmarath",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.09951v1 Announce Type: new Abstract: This paper develops a model of maritime chokepoint closures in which interrupting a shipping passage produces losses that are not measured, or even boun"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09990",
    "domain": "金融",
    "title": "Political Power in International Trade",
    "url": "https://arxiv.org/abs/2607.09990",
    "source": "Ashwin Bhattathiripad, Vipin P Veetil",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.09990v1 Announce Type: new Abstract: Economic power in international trade is the capacity of one country to impose loss on another by withdrawing from a trading relationship. This paper me"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.10297",
    "domain": "金融",
    "title": "Recovering Structural Organization in Noisy Correlation Networks Using Financial Systems as a Testbed",
    "url": "https://arxiv.org/abs/2607.10297",
    "source": "Imran Ansari, Shashi Jain, Srikanth K. Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.10297v1 Announce Type: new Abstract: Empirical correlation matrices estimated from financial return time series are contaminated by statistical noise arising from finite sample size, obscur"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.10385",
    "domain": "金融",
    "title": "Prices and Competition in Vertically Integrated Launch Markets",
    "url": "https://arxiv.org/abs/2607.10385",
    "source": "Akhil Rao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.10385v1 Announce Type: new Abstract: Over the last 15 years the number of U.S. orbital launches has grown by roughly an order of magnitude. About three-quarters of those launches were on Sp"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.10460",
    "domain": "金融",
    "title": "Learning from an Unknown DGP: Experimental Evidence on Belief Updating with AI Recommendations",
    "url": "https://arxiv.org/abs/2607.10460",
    "source": "Matthew Kovach, Daniel Martin, Gerelt Tserenjigmid",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.10460v1 Announce Type: new Abstract: We use a controlled experiment to study how beliefs are updated after receiving qualitative information (AI recommendations) from an unknown data-genera"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.10542",
    "domain": "金融",
    "title": "optimal credit portfolio and consumption with regime switching and default contagion",
    "url": "https://arxiv.org/abs/2607.10542",
    "source": "Fei Sun, Wenyuan Wang, Kaixin Yan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.10542v1 Announce Type: new Abstract: We study optimal portfolio and consumption in a regime-switching multi-name credit market with default contagion. Defaults generate portfolio losses and"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.10700",
    "domain": "金融",
    "title": "An Extreme Value Perspective on Learning Stress Laws",
    "url": "https://arxiv.org/abs/2607.10700",
    "source": "Mantu Gupta, Anand Deo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.10700v1 Announce Type: new Abstract: We introduce Self-Similar Generative Estimation (SS-GEN), a method for simulating multivariate tail events and estimating rare-event probabilities in bo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.10876",
    "domain": "金融",
    "title": "Not All Family Firms Are Alike: How Founder-Led and Governance-Entrenched Family Control Shape the Trading Environment Around the Firm",
    "url": "https://arxiv.org/abs/2607.10876",
    "source": "Douglas Cumming, Esteban Hernandez, Shan Ji",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.10876v1 Announce Type: new Abstract: Family-firm scholarship offers competing predictions about whether family control protects or threatens market integrity. We argue that the answer depen"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.10934",
    "domain": "金融",
    "title": "Multidimensional stochastic liquidity in Kyle's model of informed trading",
    "url": "https://arxiv.org/abs/2607.10934",
    "source": "Ibrahim Ekren, Evangelos A. Nikitopoulos, Lu Vy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.10934v1 Announce Type: new Abstract: We develop a variational formulation of Kyle's model of informed trading that accommodates stochastic liquidity and multiple traded assets. The main equ"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.11054",
    "domain": "金融",
    "title": "When and Why Na\\\"ive Diversification Works: A Simple Diagnostic Strategy",
    "url": "https://arxiv.org/abs/2607.11054",
    "source": "Han Feng, Difang Huang, Jue Wang, Zhengjun Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.11054v1 Announce Type: new Abstract: We explain the long-standing puzzle of na\\\"ive diversification with a simple, testable condition: equal weighting is minimum-variance optimal when the f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.11328",
    "domain": "金融",
    "title": "Strategic OTC market making with reputation feedback",
    "url": "https://arxiv.org/abs/2607.11328",
    "source": "Alexander Barzykin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.11328v1 Announce Type: new Abstract: Electronic over-the-counter (OTC) liquidity provision is increasingly shaped not only by the price of the next quote, but also by a dealer's accumulated"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.11335",
    "domain": "金融",
    "title": "Minimizing Benchmark-Relative Drawdown Duration via Occupation Time Penalization",
    "url": "https://arxiv.org/abs/2607.11335",
    "source": "Jun Sekine, Marcus Wunsch",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.11335v1 Announce Type: new Abstract: We study a continuous-time portfolio optimization problem in which an investor is evaluated relative to a non-replicable benchmark and seeks to control "
  },
  {
    "id": "rss:https://arxiv.org/abs/2411.04321",
    "domain": "金融",
    "title": "Robust and Fast Bass local volatility",
    "url": "https://arxiv.org/abs/2411.04321",
    "source": "Hao Qin, Charlie Che, Ruozhong Yang, Liming Feng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2411.04321v2 Announce Type: cross Abstract: The Bass Local Volatility Model (Bass-LV), as studied in [Conze and Henry-Labordere, 2021], stands out for its ability to eliminate the need for inter"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.16334",
    "domain": "金融",
    "title": "Volatility Calibration via Automatic Local Regression",
    "url": "https://arxiv.org/abs/2509.16334",
    "source": "Ruozhong Yang, Hao Qin, Charlie Che, Liming Feng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2509.16334v2 Announce Type: cross Abstract: Managing exotic derivatives requires accurate mark-to-market pricing and stable Greeks for reliable hedging. The Local Volatility (LV) model distingui"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.06204",
    "domain": "金融",
    "title": "Arbitrage-Free Multi-Maturity Risk-Neutral Marginals",
    "url": "https://arxiv.org/abs/2607.06204",
    "source": "Hao Qin, Ruozhong Yang, Charlie Che, Liming Feng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.06204v1 Announce Type: cross Abstract: Many quantitative finance methods and applications are formulated in terms of option-implied risk-neutral marginals rather than directly in terms of o"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.08525",
    "domain": "金融",
    "title": "Causal Effects of Protocol-Fee Changes on Liquidity Provision in Automated Market Makers",
    "url": "https://arxiv.org/abs/2607.08525",
    "source": "Wen-Ting Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.08525v1 Announce Type: cross Abstract: Automated market maker (AMM) fee rules are often evaluated by liquidity-provider (LP) welfare, but that objective mixes fee revenue, adverse-selection"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09702",
    "domain": "金融",
    "title": "Fundamental market design as a layer of AI-agent alignment",
    "url": "https://arxiv.org/abs/2607.09702",
    "source": "Omar Inverso, Emilio Tuosto, Dragisa Zunic",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.09702v1 Announce Type: cross Abstract: This paper argues that AI-agent alignment in markets should not be understood only as a property of agents, but also as a property of the interaction "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09906",
    "domain": "金融",
    "title": "Depth-Efficient Quantum Topological Data Analysis for Regime-Specific Detection of Financial Stress",
    "url": "https://arxiv.org/abs/2607.09906",
    "source": "Arul Rhik Mazumder, Shreyan Ronit Mazumder",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.09906v1 Announce Type: cross Abstract: We present, to our knowledge, the first adaptation of Pauli Correlation Encoding (PCE) to quantum topological data analysis, reformulating Betti numbe"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.10503",
    "domain": "金融",
    "title": "A Cascade of Volterra-Operator BBP Transitions in a Correlated Wigner Matrix",
    "url": "https://arxiv.org/abs/2607.10503",
    "source": "Masato Hisakado",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.10503v1 Announce Type: cross Abstract: We study a Wigner-type random matrix in which the off-diagonal correlation between entries is generated by a random factor shared among all entries in"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.10810",
    "domain": "金融",
    "title": "Diachronic Sample Integration: Robust Tail-Risk Estimation with Generative Models",
    "url": "https://arxiv.org/abs/2607.10810",
    "source": "Shuning Zhao, Patrick Wong, Leran Zhang, Xiaolin Hu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.10810v1 Announce Type: cross Abstract: Deep generative models are increasingly used as simulators for downstream decision-making under data scarcity, but in risk-sensitive applications thei"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.10960",
    "domain": "金融",
    "title": "Reinforcement Learning for Execution under Dynamic Fees in a Closed-Loop DEX Simulator",
    "url": "https://arxiv.org/abs/2607.10960",
    "source": "Wen-Ting Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2607.10960v1 Announce Type: cross Abstract: Trader-facing dynamic fees are increasingly proposed for automated market makers (AMMs), but historical data do not identify how order flow would resp"
  },
  {
    "id": "rss:https://arxiv.org/abs/2111.00522",
    "domain": "金融",
    "title": "Constraining to Motivate",
    "url": "https://arxiv.org/abs/2111.00522",
    "source": "Liqun Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2111.00522v3 Announce Type: replace Abstract: Effective decision-making often involves a principal delegating authority to better-informed agents. However, when agents'careers depend on how thei"
  },
  {
    "id": "rss:https://arxiv.org/abs/2407.14016",
    "domain": "金融",
    "title": "Factor-Biased Efficiency Gains from Exporting: Evidence from Colombia",
    "url": "https://arxiv.org/abs/2407.14016",
    "source": "Joonkyo Hong, Davide Luparello",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2407.14016v4 Announce Type: replace Abstract: New exporters often adopt new technology, which may reorganize production rather than lift output uniformly, so efficiency gains can land unevenly a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2504.11881",
    "domain": "金融",
    "title": "Universal portfolios in continuous time: an approach in pathwise It\\^o calculus",
    "url": "https://arxiv.org/abs/2504.11881",
    "source": "Xiyue Han, Alexander Schied",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2504.11881v4 Announce Type: replace Abstract: We provide a simple and straightforward approach to a continuous-time version of Cover's universal portfolio strategies within the model-free contex"
  },
  {
    "id": "rss:https://arxiv.org/abs/2504.16151",
    "domain": "金融",
    "title": "Advertising Spillovers in Mobile Apps: Evidence from Ad Shutoffs and Store Rankings",
    "url": "https://arxiv.org/abs/2504.16151",
    "source": "Harang Ju, Michael Zhao, Sinan Aral",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2504.16151v2 Announce Type: replace Abstract: Using advertising campaign data from a large US-based mobile game developer, the authors study a global advertising shutoff in the context of mobile"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.21535",
    "domain": "金融",
    "title": "Non-Take-Up of Unemployment Benefit II in Germany: A Longitudinal Perspective Using Administrative Data",
    "url": "https://arxiv.org/abs/2508.21535",
    "source": "J\\\"urgen Wiemers",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2508.21535v2 Announce Type: replace Abstract: Extensive research demonstrates that many households eligible for means-tested benefits do not claim them, a phenomenon known as non-take-up. Long-t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.18468",
    "domain": "金融",
    "title": "The Role of Informal Care in Cognitive Outcome and Healthcare Utilization Among Older Adults with Dementia",
    "url": "https://arxiv.org/abs/2509.18468",
    "source": "Mohammad Abdullah Al Faisal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2509.18468v2 Announce Type: replace Abstract: This paper examines the relationship between informal caregiving and both cognitive functioning and healthcare utilization among older adults with d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.25899",
    "domain": "金融",
    "title": "Fast catastrophe bond valuation with neural-network surrogates",
    "url": "https://arxiv.org/abs/2509.25899",
    "source": "Julian Sester, Huansang Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2509.25899v2 Announce Type: replace Abstract: Catastrophe bonds are increasingly important risk-transfer securities, but structural pricing is too slow for real-time valuation, screening, and se"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.04608",
    "domain": "金融",
    "title": "Distributionally Robust Recovery of Omitted Factors from Forecast Residuals with Application to Interest Rate Risk Management",
    "url": "https://arxiv.org/abs/2601.04608",
    "source": "Jinjun Liu, Ming-Yen Cheng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T04:00:00+00:00",
    "summary": "arXiv:2601.04608v3 Announce Type: replace Abstract: A forecasting model compresses its predictors into an estimate of a conditional mean, and the systematic structure that estimate omits survives in t"
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
    "id": "hn:48653311",
    "domain": "金融",
    "title": "Prairieland defendants sentenced today to prison terms ranging from 30-100 years",
    "url": "https://prairielanddefendants.com/press-release/eight-federal-prairieland-defendants-sentenced-today-to-prison-terms-ranging-from-30-100-years-for-common-protest-activity/",
    "source": "panic",
    "platform": "hackernews",
    "points": 88,
    "published_at": "2026-06-23T23:54:00+00:00",
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
    "id": "hn:48791799",
    "domain": "金融",
    "title": "Is The Economist Always Wrong?",
    "url": "https://economist.com/interactive/finance-and-economics/2026/07/02/is-the-economist-always-wrong",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-07-05T06:40:05+00:00",
    "summary": ""
  }
]
```
