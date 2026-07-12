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

- 今日日期：`2026-07-12`
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
  "date": "2026-07-12",
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
    "points": 3712920,
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
    "points": 1479616,
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
    "points": 1374663,
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
    "points": 1366147,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1213830,
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
    "points": 962112,
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
    "points": 941233,
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
    "points": 873098,
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
    "points": 824881,
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
    "points": 583220,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 517785,
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
    "points": 425539,
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
    "points": 382124,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1VDTv6rEtM",
    "domain": "AI",
    "title": "终于，Claude Code 封号原因被曝光了！竟然针对中国用户，植入隐形代码？",
    "url": "http://www.bilibili.com/video/av116844031774993",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 359822,
    "published_at": "2026-07-01T09:35:43+00:00",
    "summary": "Claude Code 封号原因终于找到了！国外开发者逆向 Claude Code 源码，发现 Anthropic 在客户端里藏了一套隐蔽的用户标记系统，这期视频带你完整还原封号真相。\n开源 AI 编程教程：github.com/liyupi/ai-guide\n编程学习教程+实战项目+简历模板：codefather.cn\n最近 AI 圈儿不太平啊，OpenAI Codex 封号、Cursor 地区"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 237273,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 204122,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 198201,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 190662,
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
    "points": 180682,
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
    "points": 176820,
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
    "points": 161408,
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
    "points": 159415,
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
    "points": 147111,
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
    "points": 129919,
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
    "points": 129507,
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
    "points": 102780,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92502,
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
    "points": 81255,
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
    "points": 66928,
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
    "points": 52979,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1DLgWzdE3A",
    "domain": "AI",
    "title": "[mc服务器常识普及]怎么给自己管理员op权限",
    "url": "http://www.bilibili.com/video/av114897136456574",
    "source": "愿雪时yes",
    "platform": "bilibili",
    "points": 45090,
    "published_at": "2025-07-22T13:39:32+00:00",
    "summary": "蓝夜科技官网\nhttps://www.mczbc.cn/?i74e504\n主播邀请码：74e504\n\n粉丝群 941618230\n整合包推荐配置: https://www.yuque.com/yuqueyonghurwfkkx/emg34z/dsd5y8gpbrhlkgar\n蓝夜科技教程: https://www.yuque.com/yuqueyonghurwfkkx/goyxu9\n\n\n【蓝夜科技"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 42321,
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
    "points": 38007,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1x6Vt6dEef",
    "domain": "AI",
    "title": "100 小时测试 Claude Code vs Codex（真实结果）",
    "url": "http://www.bilibili.com/video/av116656495925868",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 36890,
    "published_at": "2026-05-29T06:44:49+00:00",
    "summary": "【海外 AI 订阅】\n国内直连，支付宝付款，不用代理，\n一站订阅 ChatGPT / Codex / Claude Code / X\n订阅链接：https://bewild.ai?code=SJZD\n订阅时请填优惠邀请码：SJZD，具体优惠金额以官网为准。\n\n【视频介绍】\n我花了 100 个小时测试 Claude Code 和 Codex，结果真的让我非常意外。\n相同的提示词、相同的项目构建、两个"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28754,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27805,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 24880,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22617,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1JU7E6PEar",
    "domain": "AI",
    "title": "Cursor 已死？我为什么要退订 Cursor ？",
    "url": "http://www.bilibili.com/video/av116819553683121",
    "source": "祥子在学AI",
    "platform": "bilibili",
    "points": 21757,
    "published_at": "2026-06-27T01:52:00+00:00",
    "summary": "当了一年多的 Cursor 重度用户，最近把它退订了。\n\n不是它变差了，是 Claude Code 和 Codex 真的太好用了。\n\n几个真实感受： ① 大模型越来越强，我已经不怎么手写代码了 ② Cursor 套的是 VS Code 壳子，只属于程序员 ③ 底层模型不在一个量级——Claude 有 Opus 和 Fable 5，Codex 有 GPT 5.5/5.6，Cursor 的 Compo"
  },
  {
    "id": "bvid:BV1cCEi6sEU5",
    "domain": "AI",
    "title": "🦊他能成功吗？Claude Code 接管虚幻引擎5，打造一款游戏 | 带你走完整个流程",
    "url": "http://www.bilibili.com/video/av116731724959171",
    "source": "Apeak_虚幻丰哥",
    "platform": "bilibili",
    "points": 18044,
    "published_at": "2026-06-11T13:41:36+00:00",
    "summary": "Claude Code 接管虚幻引擎5，打造了一款游戏\n下载我的 CLAUDE.md（帮你省 token 的配置）\n链接：https://pan.quark.cn/s/b6e50b4b2535\n提取码：tbaE\nStefan 3D AI ：https://www.youtube.com/watch?v=iRcrZjOt5H8&amp;t=1s\n🔗 完整教程指南和链接：https://www.top"
  },
  {
    "id": "bvid:BV1hnjGzLE14",
    "domain": "AI",
    "title": "【小智教程】手挽手教你如何接入别人的MCP服务",
    "url": "http://www.bilibili.com/video/av114568722450105",
    "source": "空白泡泡糖果",
    "platform": "bilibili",
    "points": 17380,
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
    "points": 17074,
    "published_at": "2025-05-17T05:36:05+00:00",
    "summary": "让AI替你打工！教你用Trae+MCP自动操作网页，采集数据，有手就能学会！mcp教程，mcp实战，mcp开发"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 15082,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 13656,
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
    "points": 13404,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 12523,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1fiLr6XEj8",
    "domain": "AI",
    "title": "【大白哥AI与安全】手把手教你AI渗透,挖漏洞",
    "url": "http://www.bilibili.com/video/av116601936418546",
    "source": "大白哥AI与安全",
    "platform": "bilibili",
    "points": 12380,
    "published_at": "2026-05-19T15:33:02+00:00",
    "summary": "一键三连加关注，私信大白哥免费领取课件\n更多红队攻防实战课程，请私信大白哥咨询"
  },
  {
    "id": "bvid:BV1WBTX6kE1B",
    "domain": "AI",
    "title": "【2026版】这绝对是B站唯一将Vibe Coding从入门到实战讲明白的教程，手把手带你从入门到代码实战开发，存下吧，比啃书好太多了！拿走不谢，允许白嫖！",
    "url": "http://www.bilibili.com/video/av116871663722218",
    "source": "码士集团-马小雪",
    "platform": "bilibili",
    "points": 10148,
    "published_at": "2026-07-06T06:47:51+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！ 【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV178Nj6xE2q",
    "domain": "AI",
    "title": "【全748集】吃透B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116893289683945",
    "source": "小全栈",
    "platform": "bilibili",
    "points": 9297,
    "published_at": "2026-07-10T02:30:30+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9173,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "hn:48873836",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, CoreWeave, and Nebius: Inside the Circular Financing of the GPU Boom",
    "url": "https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom",
    "source": "adletbalzhanov",
    "platform": "hackernews",
    "points": 216,
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
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/colibri-proof-of-concept-gains-frontier-level-1-5-tb-ai-model-novel-approach-runs-on-only-25gb-of-ram-and-shows-promise-for-local-ai-setups",
    "domain": "AI 算力 / 半导体",
    "title": "Colibrì proof-of-concept gains frontier-level 1.5-TB AI model — novel approach runs on only 25GB of RAM and shows promise for local AI setups",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/colibri-proof-of-concept-gains-frontier-level-1-5-tb-ai-model-novel-approach-runs-on-only-25gb-of-ram-and-shows-promise-for-local-ai-setups",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T11:30:00+00:00",
    "summary": "Colibrì proof-of-concept gets a frontier-level AI model running on only 25 GB of RAM and a modest CPU"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/fake-go-dns-scanner-published-700-malicious-versions-before-researchers-traced-it-to-222-github-repos",
    "domain": "AI 算力 / 半导体",
    "title": "Fake Go DNS scanner spread malware through over 200 GitHub repos — 'Operation Muck and Load' has published 700 malicious modules since January",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/fake-go-dns-scanner-published-700-malicious-versions-before-researchers-traced-it-to-222-github-repos",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T11:00:00+00:00",
    "summary": "The module published its first version on January 24 this year and has since accumulated more than 1,200 versions."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/flock-cameras-mistakenly-track-car-reviewer-over-stolen-tags-police-ambush-tester-in-store-parking-lot-and-detain-him-for-an-hour",
    "domain": "AI 算力 / 半导体",
    "title": "Flock cameras mistakenly track car reviewer over 'stolen' tags — police ambush tester in store parking lot and detain him for an hour",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/flock-cameras-mistakenly-track-car-reviewer-over-stolen-tags-police-ambush-tester-in-store-parking-lot-and-detain-him-for-an-hour",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T10:30:00+00:00",
    "summary": "Flock AI cameras failed to read the smaller digits on a non-standard New Jersey plate, leading cops to block in the driver on suspicion of driving a vehicle with \"stolen\" tags. It turns out the initia"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/apple-sues-openai-over-alleged-theft-of-trade-secrets-claims-company-mentored-incoming-employees-on-bringing-confidential-information",
    "domain": "AI 算力 / 半导体",
    "title": "Apple sues OpenAI over alleged theft of trade secrets — claims company mentored incoming employees on bringing confidential information",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/apple-sues-openai-over-alleged-theft-of-trade-secrets-claims-company-mentored-incoming-employees-on-bringing-confidential-information",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T21:59:42+00:00",
    "summary": "Apple sued OpenAI, including its own former employees, over the theft of trade secrets as both companies build up AI hardware businesses."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/sk-hynix-and-tetramem-collaborate-on-experimental-chip-to-bolster-energy-efficiency-for-edge-ai-devices-memristor-based-in-memory-soc-research-leaves-performance-questions-up-in-the-air",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix and TetraMem collaborate on experimental chip to bolster energy efficiency for edge AI devices — memristor-based in-memory SoC research leaves performance questions up in the air",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/sk-hynix-and-tetramem-collaborate-on-experimental-chip-to-bolster-energy-efficiency-for-edge-ai-devices-memristor-based-in-memory-soc-research-leaves-performance-questions-up-in-the-air",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:58:53+00:00",
    "summary": "SK hynix, TetraMem, and the University of Southern California built a memristor-based in-memory computing system-on-chip for AI edge devices, achieving promising energy efficiency, but failed to demon"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-it-can-read-claudes-thoughts-as-detailed-in-new-research-paper-models-observed-to-have-a-global-workspace-revealing-more-of-what-makes-llms-tick",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic says it can read Claude's 'thoughts,' as detailed in new research paper — models observed to have a global workspace, revealing more of what makes LLMs tick",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-it-can-read-claudes-thoughts-as-detailed-in-new-research-paper-models-observed-to-have-a-global-workspace-revealing-more-of-what-makes-llms-tick",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:44:12+00:00",
    "summary": "Anthropic has discovered an internal \"J-space\" for its Claude AI that displays similarities to human internal processing. While the AI developer anthropomorphizes it as thought, it may yet prove usefu"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/intels-midrange-core-ultra-5-245k-is-down-to-its-lowest-price-ever-at-just-usd179-on-amazon-save-up-to-42-percent-on-a-solid-gaming-cpu-with-14-cores-and-pcie-5-0-support",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's midrange Core Ultra 5 245K is down to its lowest price ever at just $179 on Amazon — save up to 42% on a solid gaming CPU with 14 cores and PCIe 5.0 support",
    "url": "https://www.tomshardware.com/pc-components/intels-midrange-core-ultra-5-245k-is-down-to-its-lowest-price-ever-at-just-usd179-on-amazon-save-up-to-42-percent-on-a-solid-gaming-cpu-with-14-cores-and-pcie-5-0-support",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:27:09+00:00",
    "summary": "Intel's forgotten 14-core SKU from last year has received a sizable discount on Amazon, making it one of the best value propositions in CPUs right now. It performs amicably in gaming and professional "
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/steam-sales-reportedly-topped-usd11-billion-during-h1-2026-due-to-shifting-trends-staggering-growth-driven-by-influx-of-chinese-players-and-booming-legacy-catalogues",
    "domain": "AI 算力 / 半导体",
    "title": "Steam sales reportedly topped $11 billion during H1 2026 due to shifting trends — staggering growth driven by influx of Chinese players and booming legacy catalogues",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/steam-sales-reportedly-topped-usd11-billion-during-h1-2026-due-to-shifting-trends-staggering-growth-driven-by-influx-of-chinese-players-and-booming-legacy-catalogues",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T15:25:19+00:00",
    "summary": "Steam made an estimated $11.1 billion in revenue in the first six months of 2026, according to estimates from research firm Alinea Analytics. That's more than it did in the entire pandemic-ridden year"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/asus-rog-strix-scar-18-2026-review",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Strix Scar 18 (2026) Review: Stunning Mini‑LED, serious muscle, and a few missed steps",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/asus-rog-strix-scar-18-2026-review",
    "source": "Charles Jefferies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T15:16:42+00:00",
    "summary": "The Asus ROG Strix Scar 18 pairs an 18-inch mini-LED display with cutting-edge components, but omissions like PCIe 5.0 storage and dual-channel RAM —plus slightly weaker performance than Razer’s Blade"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/tencent-is-reportedly-in-talks-to-acquire-manus-from-meta-following-beijing-intervention-company-expects-to-remain-independent-of-chinese-tech-giant",
    "domain": "AI 算力 / 半导体",
    "title": "Tencent is reportedly in talks to acquire Manus from Meta, following Beijing intervention — company expects to remain independent of Chinese tech giant",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/tencent-is-reportedly-in-talks-to-acquire-manus-from-meta-following-beijing-intervention-company-expects-to-remain-independent-of-chinese-tech-giant",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T15:00:01+00:00",
    "summary": "Tencent is in talks with Manus and other investors to raise the $2 billion needed to buy back the startup from Meta. Beijing ordered the two companies to unwind the deal six months after the surprise "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-raises-a-record-usd26-5-billion-in-historic-u-s-ipo-south-korean-memory-giant-to-fund-massive-hbm-manufacturing-expansions",
    "domain": "AI 算力 / 半导体",
    "title": "SK hynix raises a record $26.5 billion in historic U.S. IPO — South Korean memory giant to fund massive HBM manufacturing expansions",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-raises-a-record-usd26-5-billion-in-historic-u-s-ipo-south-korean-memory-giant-to-fund-massive-hbm-manufacturing-expansions",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T14:27:41+00:00",
    "summary": "SK hynix raised $26.5 billion in a record-breaking Nasdaq IPO, as it plans to channel the windfall from surging AI demand and sold-out HBM supply to fund new fabs."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/nanya-to-quadruple-capital-spending-to-6-2-billion-in-2027",
    "domain": "AI 算力 / 半导体",
    "title": "Nanya to quadruple capital spending to $6.2 billion in 2027 as DRAM prices push gross margin to 79.5% — Q2 revenue skyrockets as ASPs for memory continue to surge",
    "url": "https://www.tomshardware.com/tech-industry/nanya-to-quadruple-capital-spending-to-6-2-billion-in-2027",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T13:31:21+00:00",
    "summary": "Nanya Technology plans capex of more than TW$200 billion ($6.2 billion) in 2027, roughly four times its budget for this year."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/japanese-chipmaker-rapidus-to-offer-lower-wafer-pricing-than-tsmc-2nm-class-silicon-to-be-priced-around-usd20-000-on-2027-launch",
    "domain": "AI 算力 / 半导体",
    "title": "Japanese chipmaker Rapidus to offer lower wafer pricing than TSMC — 2nm class silicon to be priced around $20,000 on 2027 launch",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/japanese-chipmaker-rapidus-to-offer-lower-wafer-pricing-than-tsmc-2nm-class-silicon-to-be-priced-around-usd20-000-on-2027-launch",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T12:56:48+00:00",
    "summary": "Japanese chipmaker Rapidus discloses one more aspect of its strategy: to offer lower quotes than TSMC."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/vpn/save-84-percent-on-a-two-year-expressvpn-subscription-offering-four-additional-months-for-free-upgrade-your-privacy-for-under-usd70-with-no-logs-access-to-servers-in-105-countries-worldwide",
    "domain": "AI 算力 / 半导体",
    "title": "Save 84% on a two-year ExpressVPN subscription, offering four additional months for free — upgrade your privacy for under $70 with no-logs access to servers in 105 countries worldwide",
    "url": "https://www.tomshardware.com/software/vpn/save-84-percent-on-a-two-year-expressvpn-subscription-offering-four-additional-months-for-free-upgrade-your-privacy-for-under-usd70-with-no-logs-access-to-servers-in-105-countries-worldwide",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T11:41:27+00:00",
    "summary": "Right now, you'll save $378 in total on over two years' worth of ExpressVPN, now priced at $69.72, with four extra months thrown in for free."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/researchers-turn-hbm-on-its-side-to-tackle-ai-memorys-heat-wall-korean-v-die-and-japanese-mosaic-designs-promise-higher-bandwidth-denser-stacks-and-cooler-future-gpus",
    "domain": "AI 算力 / 半导体",
    "title": "Researchers turn HBM on its side to tackle AI memory’s heat wall — Korean V-Die and Japanese MOSAIC designs promise higher bandwidth, denser stacks, and cooler future GPUs",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/researchers-turn-hbm-on-its-side-to-tackle-ai-memorys-heat-wall-korean-v-die-and-japanese-mosaic-designs-promise-higher-bandwidth-denser-stacks-and-cooler-future-gpus",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T11:40:00+00:00",
    "summary": "Researchers in Korea and Japan have proposed sideways-stacked DRAM designs that could push future AI memory beyond conventional HBM limits by improving cooling, bandwidth, and capacity while reducing "
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/mice/logitechs-mx-master-4-hits-usd102-at-lenovo-up-your-productivity-game-with-haptic-feedback-and-effortless-scrolling",
    "domain": "AI 算力 / 半导体",
    "title": "Logitech's MX Master 4 hits $102 at Lenovo — up your productivity game with haptic feedback and effortless scrolling",
    "url": "https://www.tomshardware.com/peripherals/mice/logitechs-mx-master-4-hits-usd102-at-lenovo-up-your-productivity-game-with-haptic-feedback-and-effortless-scrolling",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T11:34:15+00:00",
    "summary": "Pick up the fantastic Logitech MX Master 4 productivity mouse from Lenovo and make a saving when you stack these two Lenovo e-coupon codes."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/chat-control-1-0-sneaks-through-the-eu-parliament-letting-companies-scan-user-data-without-warrants-legal-tactic-used-to-force-a-majority-required-re-vote-on-eve-of-parliament-break",
    "domain": "AI 算力 / 半导体",
    "title": "Chat Control 1.0 sneaks through the EU Parliament, letting companies scan user data without warrants — legal tactic used to force a majority-required re-vote on eve of Parliament break",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/chat-control-1-0-sneaks-through-the-eu-parliament-letting-companies-scan-user-data-without-warrants-legal-tactic-used-to-force-a-majority-required-re-vote-on-eve-of-parliament-break",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T11:00:00+00:00",
    "summary": "Chat Control 1.0 sneaks through the EU Parliament, letting companies scan user data without warrants — legal skullduggery used to force a majority-required re-vote on eve of Parliament break"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/micron-takes-a-500-million-position-in-americas-only-300mm-wafer-plant",
    "domain": "AI 算力 / 半导体",
    "title": "Micron lifts U.S. spending to $250 billion — company takes $500 million position in America's only 300 mm wafer plant",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/micron-takes-a-500-million-position-in-americas-only-300mm-wafer-plant",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T10:40:00+00:00",
    "summary": "Micron has said it will invest up to $3 billion in the US semiconductor supply chain, with $500 million of that going to GlobalWafers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/samsung-readies-gaia-ai-accelerator-for-client-devices-hp-and-lenovo-are-reportedly-validating-the-npu",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung readies Gaia AI accelerator for PCs — HP and Lenovo are reportedly validating the NPU",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/samsung-readies-gaia-ai-accelerator-for-client-devices-hp-and-lenovo-are-reportedly-validating-the-npu",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T10:20:00+00:00",
    "summary": "Samsung reportedly preps Gaia AI accelerator for client devices that is already being tested by HP and Lenovo."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/minecraft-shown-running-on-game-boy-color-and-game-boy-in-3d-with-textures-developer-coaxed-3d-look-out-of-old-hardware",
    "domain": "AI 算力 / 半导体",
    "title": "Minecraft shown running on Game Boy Color and Game Boy in 3D with textures — developer coaxed 3D look out of barely-there hardware",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/minecraft-shown-running-on-game-boy-color-and-game-boy-in-3d-with-textures-developer-coaxed-3d-look-out-of-old-hardware",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T10:00:00+00:00",
    "summary": "Because getting it to run on the Game Boy Advance clearly wasn't hard enough."
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
    "id": "rss:https://www.eetimes.com/as-ai-moves-from-training-to-inference-optics-moves-closer-to-the-chip/",
    "domain": "AI 算力 / 半导体",
    "title": "As AI Moves from Training to Inference, Optics Moves Closer to the Chip",
    "url": "https://www.eetimes.com/as-ai-moves-from-training-to-inference-optics-moves-closer-to-the-chip/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T07:15:00+00:00",
    "summary": "Imec researchers argue that co-packaged optics will not be enough for future AI systems, pushing the industry toward 2.5D and eventually 3D optical I/O. The post As AI Moves from Training to Inference"
  },
  {
    "id": "rss:https://www.eetimes.com/white-house-executive-order-brings-new-urgency-to-post-quantum-cryptography/",
    "domain": "AI 算力 / 半导体",
    "title": "White House Executive Order Brings New Urgency to Post-Quantum Cryptography",
    "url": "https://www.eetimes.com/white-house-executive-order-brings-new-urgency-to-post-quantum-cryptography/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T17:00:00+00:00",
    "summary": "Quantum hackers won’t wait: White House orders PQC by 2030, forcing contractors and tech firms to move now. The post White House Executive Order Brings New Urgency to Post-Quantum Cryptography appeare"
  },
  {
    "id": "rss:https://www.eetimes.com/rise-of-the-ai-data-center-why-infrastructure-strategy-is-now-a-board-level-issue/",
    "domain": "AI 算力 / 半导体",
    "title": "Rise of the AI Data Center – Why Infrastructure Strategy Is Now a Board-Level Issue",
    "url": "https://www.eetimes.com/rise-of-the-ai-data-center-why-infrastructure-strategy-is-now-a-board-level-issue/",
    "source": "Delta Electronics Americas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T14:00:00+00:00",
    "summary": "This white paper describes the critical engineering and strategic pain points behind today&#8217;s AI data center infrastructure gap and offers practical frameworks for resolving them. Whether you&#82"
  },
  {
    "id": "rss:https://www.eetimes.com/sambanova-raises-1-billion-signs-jpmorganchase-as-a-customer/",
    "domain": "AI 算力 / 半导体",
    "title": "SambaNova Raises $1B, Signs JPMorganChase as a Customer",
    "url": "https://www.eetimes.com/sambanova-raises-1-billion-signs-jpmorganchase-as-a-customer/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T07:45:00+00:00",
    "summary": "The enterprise market is beginning to kick in, SambaNova CEO tells EE Times. The post SambaNova Raises $1B, Signs JPMorganChase as a Customer appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/mems-heralds-an-overdue-step-change-in-switching-technology/",
    "domain": "AI 算力 / 半导体",
    "title": "MEMS Heralds an Overdue Step Change in Switching Technology",
    "url": "https://www.eetimes.com/mems-heralds-an-overdue-step-change-in-switching-technology/",
    "source": "Russ Garcia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T07:40:00+00:00",
    "summary": "Ditch creaky relays: MEMS switches slash heat, power draw and bulk for AI data centers and automation. The post MEMS Heralds an Overdue Step Change in Switching Technology appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/teamgroup-g70-pro-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "TeamGroup G70 Pro 2TB SSD Review: Low latency meets affordable DRAM",
    "url": "https://www.tomshardware.com/pc-components/ssds/teamgroup-g70-pro-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T17:17:56+00:00",
    "summary": "The TeamGroup G70 Pro is a high-end drive without a high-end price. Good performance, but poor power efficiency keeps it in check."
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
    "points": 132,
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
    "id": "rss:https://www.theverge.com/gadgets/964499/nopia-viral-synth-finished-price-release-demo",
    "domain": "大厂 AI 动态",
    "title": "After years of teasing, the viral Nopia synth is ‘basically finished’",
    "url": "https://www.theverge.com/gadgets/964499/nopia-viral-synth-finished-price-release-demo",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T20:57:42+00:00",
    "summary": "After setting the music gear corner of the internet on fire back in 2023 with the first glimpse at the Nopia, creators Martin Grieco and Roc&#237;o Gal are almost ready to bring it to market. The duo "
  },
  {
    "id": "rss:https://www.theverge.com/policy/964493/oregons-ag-delay-paramount-warner-bros-merger",
    "domain": "大厂 AI 动态",
    "title": "Oregon’s Attorney General withdraws effort to delay Paramount and Warner Bros. merger",
    "url": "https://www.theverge.com/policy/964493/oregons-ag-delay-paramount-warner-bros-merger",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T18:44:12+00:00",
    "summary": "Oregon Attorney General Dan Rayfield had been seeking documents from Paramount related to its takeover of Warner Bros. Discovery. Rayfield also asked a state circuit court judge to delay the closing o"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/963509/image-line-ceo-constantin-koehncke-fl-studio-interview",
    "domain": "大厂 AI 动态",
    "title": "FL Studio head Constantin Koehncke turns to Reddit for feedback and fun",
    "url": "https://www.theverge.com/entertainment/963509/image-line-ceo-constantin-koehncke-fl-studio-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T15:00:00+00:00",
    "summary": "If you're a music maker of a certain age, then you probably once dabbled with a pirated copy of a little app called Fruity Loops. These days it's called FL Studio, and Constantin Koehncke, is the man "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/964138/nintendo-talking-flower-mario-wonder-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Nintendo’s Talking Flower got a small price cut",
    "url": "https://www.theverge.com/gadgets/964138/nintendo-talking-flower-mario-wonder-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T15:00:00+00:00",
    "summary": "If you’re the type of person who could always use a little extra positive affirmation, or you have a weakness for weird gadgets, the Talking Flower might be of interest. I’m only kind of serious. The "
  },
  {
    "id": "rss:https://www.theverge.com/science/964478/white-house-avi-loeb-aliens-ufo-uap-council",
    "domain": "大厂 AI 动态",
    "title": "White House taps the guy who keeps crying ‘aliens’ to run UFO group",
    "url": "https://www.theverge.com/science/964478/white-house-avi-loeb-aliens-ufo-uap-council",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T14:18:33+00:00",
    "summary": "Harvard astrophysicist Avi Loeb will head the UAP Science Advisory Council established by the White House, the Pentagon, the Office of the Director of National Intelligence, the FBI, and \"the intellig"
  },
  {
    "id": "rss:https://www.theverge.com/policy/964302/ice-donald-trump-killings",
    "domain": "大厂 AI 动态",
    "title": "ICE are heavily armed killers. They’re also huge losers",
    "url": "https://www.theverge.com/policy/964302/ice-donald-trump-killings",
    "source": "TC. Sottek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T13:00:00+00:00",
    "summary": "Donald Trump's Homeland Security regime has been at the center of two critical stories in the past two weeks. In the first, federal agents shot and killed a man and quickly got to work justifying the "
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/964061/dosa-divas-review-ps5-steam-switch",
    "domain": "大厂 AI 动态",
    "title": "A tasty RPG that will make you very hungry",
    "url": "https://www.theverge.com/entertainment/964061/dosa-divas-review-ps5-steam-switch",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T12:00:00+00:00",
    "summary": "Roleplaying games are often defined by excess. Storylines that span dozens of hours, side quests so big they could be their own game, massive worlds that require complex maps to explore, and casts so "
  },
  {
    "id": "rss:https://www.theverge.com/tech/964169/ifixit-repairs-kit-nothing-3a-installer",
    "domain": "大厂 AI 动态",
    "title": "The perfect kit for all your tiny repairs",
    "url": "https://www.theverge.com/tech/964169/ifixit-repairs-kit-nothing-3a-installer",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T12:00:00+00:00",
    "summary": "Hi, friends! Welcome to Installer No. 135, your guide to the best and Verge-iest stuff in the world. (If you're new here, welcome, crank the AC, and also you can read all the old editions at the Insta"
  },
  {
    "id": "rss:https://www.theverge.com/reviews/963814/joolca-hottap-portable-shower-review",
    "domain": "大厂 AI 动态",
    "title": "Are you filthy enough for a $700 portable shower?",
    "url": "https://www.theverge.com/reviews/963814/joolca-hottap-portable-shower-review",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T07:00:00+00:00",
    "summary": "Hot showers, like electricity, are a luxury that's easy to take for granted. That all changes after a few nights camping at a music festival, a week toiling at a backcountry job site, or overlanding a"
  },
  {
    "id": "rss:https://www.theverge.com/tech/964425/flock-safety-cease-and-desist-letter",
    "domain": "大厂 AI 动态",
    "title": "No, Flock isn&#8217;t threatening people for debating surveillance",
    "url": "https://www.theverge.com/tech/964425/flock-safety-cease-and-desist-letter",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T00:10:38+00:00",
    "summary": "On Thursday, the Instagram account for a lecture series in Newport Beach, CA posted a photo of what appeared to be a cease and desist letter from the surveillance technology company Flock Safety. Floc"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/11/reed-jobs-would-rather-talk-about-curing-cancer-than-his-last-name/",
    "domain": "大厂 AI 动态",
    "title": "Reed Jobs would rather talk about curing cancer than his last name",
    "url": "https://techcrunch.com/2026/07/11/reed-jobs-would-rather-talk-about-curing-cancer-than-his-last-name/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T00:16:06+00:00",
    "summary": "When we last sat down with Jobs at TechCrunch Disrupt nearly three years ago, his firm Yosemite was brand new and biotech was still reeling from its post-pandemic crash. Now, the venture outfit has a "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/11/this-slushie-machine-was-a-lifesaver-during-nycs-heat-wave/",
    "domain": "大厂 AI 动态",
    "title": "This slushie machine was a lifesaver during NYC’s heat wave",
    "url": "https://techcrunch.com/2026/07/11/this-slushie-machine-was-a-lifesaver-during-nycs-heat-wave/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T22:00:00+00:00",
    "summary": "Last weekend&#8217;s brutal NYC heat wave had me craving a frozen drink almost every afternoon. Normally, that would mean sweating through a walk to 7-Eleven for a slurpee. This time, though, I stayed"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/11/smart-glasses-without-a-camera-even-realities-bets-productivity-beats-recording-everyone/",
    "domain": "大厂 AI 动态",
    "title": "Smart glasses without a camera? Even Realities bets productivity beats recording everyone",
    "url": "https://techcrunch.com/2026/07/11/smart-glasses-without-a-camera-even-realities-bets-productivity-beats-recording-everyone/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T17:30:00+00:00",
    "summary": "The glasses are targeted at people who might be constantly in meetings, giving presentations, and traveling to countries where different languages are spoken."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/11/openai-bets-on-families-as-chatgpt-goes-deeper-into-households/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI bets on families as ChatGPT goes deeper into households",
    "url": "https://techcrunch.com/2026/07/11/openai-bets-on-families-as-chatgpt-goes-deeper-into-households/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T14:13:00+00:00",
    "summary": "ChatGPT is hiring a dedicated product manager to build experiences for families, caregivers, and older adults, according to a job posting."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/us-cyber-agency-cisa-had-to-build-its-incident-playbook-during-the-incident-agency-reveals/",
    "domain": "大厂 AI 动态",
    "title": "US cybersecurity agency CISA had to build its incident playbook during the incident, agency reveals",
    "url": "https://techcrunch.com/2026/07/10/us-cyber-agency-cisa-had-to-build-its-incident-playbook-during-the-incident-agency-reveals/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T01:01:28+00:00",
    "summary": "Independent cybersecurity journalist Brian Krebs reported in May that a security researcher with cyber firm GitGuardian alerted him to reams of exposed passwords stored in a publicly accessible GitHub"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/phia-accused-of-cookie-stuffing-taking-affiliate-credit-on-purchases-it-didnt-earn/",
    "domain": "大厂 AI 动态",
    "title": "Phia accused of ‘cookie stuffing,’ taking affiliate credit on purchases it didn’t earn",
    "url": "https://techcrunch.com/2026/07/10/phia-accused-of-cookie-stuffing-taking-affiliate-credit-on-purchases-it-didnt-earn/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T00:29:25+00:00",
    "summary": "Phia, the shopping startup founded by Bill Gates’ daughter, Phoebe, and her friend Sophia Kianni is under fire for a practice known as “cookie stuffing,” which helped the product receive commissions a"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/meta-removes-controversial-ai-feature-on-instagram-after-backlash/",
    "domain": "大厂 AI 动态",
    "title": "Meta removes controversial AI feature on Instagram after backlash",
    "url": "https://techcrunch.com/2026/07/10/meta-removes-controversial-ai-feature-on-instagram-after-backlash/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T23:55:07+00:00",
    "summary": "\"Our intent was to provide a useful creative tool and to give people control over whether their public content could be referenced in this way,\" the company said in a blog post. \"We've heard the feedb"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/blueskys-interim-ceo-toni-schneider-drops-the-interim/",
    "domain": "大厂 AI 动态",
    "title": "Bluesky’s interim CEO, Toni Schneider, drops the ‘interim’",
    "url": "https://techcrunch.com/2026/07/10/blueskys-interim-ceo-toni-schneider-drops-the-interim/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T21:51:55+00:00",
    "summary": "Schneider, who formerly served as the CEO of Automattic and is a partner at True Ventures, says he is \"all in\" on the unconventional social media platform."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/apple-sues-openai-over-alleged-trade-secret-theft/",
    "domain": "大厂 AI 动态",
    "title": "Apple sues OpenAI over alleged trade secret theft",
    "url": "https://techcrunch.com/2026/07/10/apple-sues-openai-over-alleged-trade-secret-theft/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T21:00:29+00:00",
    "summary": "Apple alleges the misconduct was directed by OpenAI's senior leadership, including a longtime former employee."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/filing-college-app-fizz-accuses-vc-of-sharing-confidential-startup-information-with-rival-sidechat/",
    "domain": "大厂 AI 动态",
    "title": "Filing: College app Fizz accuses VC of sharing confidential startup information with rival Sidechat",
    "url": "https://techcrunch.com/2026/07/10/filing-college-app-fizz-accuses-vc-of-sharing-confidential-startup-information-with-rival-sidechat/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T17:42:36+00:00",
    "summary": "Fizz has expanded its lawsuit against rival Sidechat, alleging that a Maveron VC shared its confidential information obtained during a fundraising meeting with the competing startup."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/sk-hynix-raises-26-5b-in-the-biggest-foreign-ipo-in-us-history-is-urged-to-build-new-us-fabs/",
    "domain": "大厂 AI 动态",
    "title": "SK Hynix raises $26.5B in the biggest foreign IPO in US history, is urged to build new US fabs",
    "url": "https://techcrunch.com/2026/07/10/sk-hynix-raises-26-5b-in-the-biggest-foreign-ipo-in-us-history-is-urged-to-build-new-us-fabs/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T17:17:12+00:00",
    "summary": "The AI chip boom just produced its biggest Wall Street moment yet. Now SK Hynix and Samsung are being asked to build U.S. factories."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/a-new-app-hypertexting-turns-the-open-web-into-a-scrollable-social-media-like-feed/",
    "domain": "大厂 AI 动态",
    "title": "A new app, HyperTexting, turns the open web into a scrollable social media-like feed",
    "url": "https://techcrunch.com/2026/07/10/a-new-app-hypertexting-turns-the-open-web-into-a-scrollable-social-media-like-feed/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T17:11:51+00:00",
    "summary": "HyperTexting's new app aims to make the open web feel more like social media by turning websites, blogs, newsletters, and podcasts into a scrollable feed, while also making it easier to post to your o"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/china-is-catching-up-to-elon-musks-reusable-rockets/",
    "domain": "大厂 AI 动态",
    "title": "China is catching up to Elon Musk’s reusable rockets",
    "url": "https://techcrunch.com/2026/07/10/china-is-catching-up-to-elon-musks-reusable-rockets/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:51:07+00:00",
    "summary": "China's state-owned space company recovered its first orbital rocket booster after launch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/disney-is-considering-a-free-streaming-tier-report-says/",
    "domain": "大厂 AI 动态",
    "title": "Disney+ is considering a free streaming tier, report says",
    "url": "https://techcrunch.com/2026/07/10/disney-is-considering-a-free-streaming-tier-report-says/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:29:05+00:00",
    "summary": "The launch of free content would allow Disney+ to better compete with free services like YouTube and Tubi, which are capturing a growing share of consumers’ viewing time."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/dumb-co-dared-me-to-trade-my-iphone-for-a-hacked-flip-phone/",
    "domain": "大厂 AI 动态",
    "title": "Dumb Co dared me to trade my iPhone for a hacked flip phone",
    "url": "https://techcrunch.com/2026/07/10/dumb-co-dared-me-to-trade-my-iphone-for-a-hacked-flip-phone/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:06:49+00:00",
    "summary": "Dumb Co sells flip phones that sync to your smartphone, bridging the infinite connectivity of the iPhone and the unrealistic limitations of an early 2000s relic."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/oratomic-raises-300m-to-build-a-viable-quantum-computer-that-needs-only-20k-qubits/",
    "domain": "大厂 AI 动态",
    "title": "Oratomic raises $300M to build a viable quantum computer that needs only 20K qubits",
    "url": "https://techcrunch.com/2026/07/10/oratomic-raises-300m-to-build-a-viable-quantum-computer-that-needs-only-20k-qubits/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T15:00:09+00:00",
    "summary": "The massive round was co-led by ARCH Venture Partners, Spark Capital, and Khosla Ventures."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/netflix-could-be-planning-always-on-live-tv-channels/",
    "domain": "大厂 AI 动态",
    "title": "Netflix could be planning ‘always-on’ live TV channels",
    "url": "https://techcrunch.com/2026/07/10/netflix-could-be-planning-always-on-live-tv-channels/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T14:53:08+00:00",
    "summary": "Amid signs of slowing engagement, Netflix is reportedly considering launching \"always-on\" live channels, giving subscribers something to tune into 24/7."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/eu-threatens-meta-with-fines-over-addictive-features-on-facebook-and-instagram/",
    "domain": "大厂 AI 动态",
    "title": "EU threatens Meta with fines over addictive features on Facebook and Instagram",
    "url": "https://techcrunch.com/2026/07/10/eu-threatens-meta-with-fines-over-addictive-features-on-facebook-and-instagram/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T14:19:40+00:00",
    "summary": "The tech giant is in breach of the Digital Services Act by focusing on features like infinite scroll, autoplay, push notifications, and the highly personalized recommendation algorithms, the European "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/florida-ransomware-negotiator-convicted-for-helping-ransomware-gang-extort-us-companies/",
    "domain": "大厂 AI 动态",
    "title": "Florida ransomware negotiator convicted for helping ransomware gang extort US companies",
    "url": "https://techcrunch.com/2026/07/10/florida-ransomware-negotiator-convicted-for-helping-ransomware-gang-extort-us-companies/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T14:11:03+00:00",
    "summary": "A third ransomware negotiator has been jailed for helping a notorious ransomware group extort American victim companies into paying the hackers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/10/hugging-faces-ceo-on-why-companies-are-done-renting-their-ai/",
    "domain": "大厂 AI 动态",
    "title": "Hugging Face’s CEO on why companies are done renting their AI",
    "url": "https://techcrunch.com/2026/07/10/hugging-faces-ceo-on-why-companies-are-done-renting-their-ai/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T14:00:00+00:00",
    "summary": "Open source AI is booming, according to&#160;Hugging Face&#160;CEO&#160;Clem Delangue. The company has grown into something like a GitHub for AI in recent years, where AI builders can share and downlo"
  },
  {
    "id": "rss:https://stratechery.com/2026/xbox-on-the-rocks/",
    "domain": "大厂 AI 动态",
    "title": "2026.28: XBOX On the Rocks",
    "url": "https://stratechery.com/2026/xbox-on-the-rocks/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of July 6, 2026, including a word from Mark Zuckerberg*, pulling the plug on XBOX, and toilet talk."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/a-jupiter-size-planet-that-escaped-its-stars-death/",
    "domain": "大厂 AI 动态",
    "title": "A Jupiter-size planet that escaped its star's death",
    "url": "https://arstechnica.com/science/2026/07/a-jupiter-size-planet-that-escaped-its-stars-death/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T12:00:58+00:00",
    "summary": "It's unclear how the planet avoided its star's bloated red giant stage."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/overhaul-of-public-lands-grazing-regulations-seeks-to-cut-public-involvement/",
    "domain": "大厂 AI 动态",
    "title": "Overhaul of public lands grazing regulations seeks to cut public involvement",
    "url": "https://arstechnica.com/tech-policy/2026/07/overhaul-of-public-lands-grazing-regulations-seeks-to-cut-public-involvement/",
    "source": "Mark Olalde, ProPublica, and Jimmy Tobias for High Country News",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T11:11:26+00:00",
    "summary": "For the first time since 1995, the Bureau of Land Management is rewriting its grazing regulations."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/quantum-error-correction-can-constantly-recalibrate-a-processor/",
    "domain": "大厂 AI 动态",
    "title": "Quantum error correction can constantly recalibrate a processor",
    "url": "https://arstechnica.com/science/2026/07/quantum-error-correction-can-constantly-recalibrate-a-processor/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T23:02:30+00:00",
    "summary": "Reinforcement learning uses error information to adjust control algorithms."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/on-americas-250th-more-cities-used-drone-surveillance-to-spot-illegal-fireworks/",
    "domain": "大厂 AI 动态",
    "title": "Increased drone surveillance of illegal July 4th fireworks led to $100K fine",
    "url": "https://arstechnica.com/gadgets/2026/07/on-americas-250th-more-cities-used-drone-surveillance-to-spot-illegal-fireworks/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T22:37:22+00:00",
    "summary": "More police and firefighters use drones to catch and deter illegal fireworks."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/china-recovered-its-first-reusable-rocket-and-showed-a-new-way-to-do-it/",
    "domain": "大厂 AI 动态",
    "title": "China recovered its first reusable rocket and showed a new way to do it",
    "url": "https://arstechnica.com/space/2026/07/china-recovered-its-first-reusable-rocket-and-showed-a-new-way-to-do-it/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T21:41:43+00:00",
    "summary": "\"Clearly, they admire the work that's being done by SpaceX and are trying to replicate it.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/expedition-captures-first-images-of-shackletons-last-ship/",
    "domain": "大厂 AI 动态",
    "title": "Check out the first images of Quest shipwreck",
    "url": "https://arstechnica.com/science/2026/07/expedition-captures-first-images-of-shackletons-last-ship/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T19:59:31+00:00",
    "summary": "The Quest shipwreck is in worse shape than expected, but it has turned into a thriving marine ecosystem."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/ransomware-negotiator-helped-attackers-extort-his-own-clients-gets-6-year-sentence/",
    "domain": "大厂 AI 动态",
    "title": "Ransomware negotiator hired to represent victims was working for the attackers",
    "url": "https://arstechnica.com/tech-policy/2026/07/ransomware-negotiator-helped-attackers-extort-his-own-clients-gets-6-year-sentence/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T19:40:11+00:00",
    "summary": "Six years in prison for man who \"sold out the very victims he was hired to represent.\""
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/anti-vaccine-changes-under-rfk-jr-will-hurt-vulnerable-toddlers-study-confirms/",
    "domain": "大厂 AI 动态",
    "title": "Study shows how toxic RFK Jr.’s change to measles vaccine is for US toddlers",
    "url": "https://arstechnica.com/health/2026/07/anti-vaccine-changes-under-rfk-jr-will-hurt-vulnerable-toddlers-study-confirms/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T19:25:04+00:00",
    "summary": "The children who get a combination shot are some of the most vulnerable."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/07/valves-steam-machine-verified-ratings-offer-more-questions-than-answers/",
    "domain": "大厂 AI 动态",
    "title": "Valve's new Steam Machine verification system is silent on these Steam Deck-busters",
    "url": "https://arstechnica.com/gaming/2026/07/valves-steam-machine-verified-ratings-offer-more-questions-than-answers/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:53:31+00:00",
    "summary": "Dozens of titles too taxing for Steam Deck are still unrated for the new hardware."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/firmware-update-bricks-hue-bridge-pro-devices-philips-gives-free-replacements/",
    "domain": "大厂 AI 动态",
    "title": "Firmware update bricks Hue Bridge Pro devices; Philips gives free replacements",
    "url": "https://arstechnica.com/gadgets/2026/07/firmware-update-bricks-hue-bridge-pro-devices-philips-gives-free-replacements/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:36:09+00:00",
    "summary": "Affected users will have to configure their lights and settings all over again."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/an-orbiting-disco-ball-gave-einsteins-theory-its-most-precise-test-yet/",
    "domain": "大厂 AI 动态",
    "title": "An orbiting disco ball gave Einstein’s theory its most precise test yet",
    "url": "https://arstechnica.com/science/2026/07/an-orbiting-disco-ball-gave-einsteins-theory-its-most-precise-test-yet/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T16:11:35+00:00",
    "summary": "The Earth may not be that massive, but it still distorts space-time."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/disable-auto-play-and-infinite-scroll-or-risk-massive-fines-eu-tells-meta/",
    "domain": "大厂 AI 动态",
    "title": "Disable autoplay and infinite scroll or risk massive fines, EU tells Meta",
    "url": "https://arstechnica.com/tech-policy/2026/07/disable-auto-play-and-infinite-scroll-or-risk-massive-fines-eu-tells-meta/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T15:46:18+00:00",
    "summary": "Digital Services Act may force Meta to make big changes on its platforms."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/nasa-finally-releases-a-critical-planning-document-for-private-space-stations/",
    "domain": "大厂 AI 动态",
    "title": "NASA sure seems to be asking an awful lot of private space stations",
    "url": "https://arstechnica.com/space/2026/07/nasa-finally-releases-a-critical-planning-document-for-private-space-stations/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T15:15:58+00:00",
    "summary": "\"Industry finally knows what NASA is asking of them.\""
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/07/vw-group-and-unions-disagree-on-plan-to-streamline-the-automaker/",
    "domain": "大厂 AI 动态",
    "title": "Volkswagen Group tells its board how to fix it, unions disagree",
    "url": "https://arstechnica.com/cars/2026/07/vw-group-and-unions-disagree-on-plan-to-streamline-the-automaker/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-10T13:51:10+00:00",
    "summary": "VW's plan calls for half as many models but didn't mention closures or job cuts."
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
    "id": "wscn:3776716",
    "domain": "股票",
    "title": "机构实地调研：台积电赢了现在的CPO，三星在押注下一场",
    "url": "https://wallstreetcn.com/articles/3776716",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T05:47:23+00:00",
    "summary": "台积电凭借博通、英伟达的交换机CPO产品率先商业化落地；三星则另辟蹊径，布局将HBM、逻辑芯片与硅光芯片整合于同一封装的2.xD方案，瞄准AI计算封装的光学I/O赛道。三星的\"三位一体\"垂直整合是潜在优势，但良率挑战与商业化时间表仍是最大变数。订单落地，才是检验胜负的唯一标准。"
  },
  {
    "id": "wscn:3776551",
    "domain": "股票",
    "title": "MSCI中国相对收益跌到25年以来最低位：全球资金为何开始回头？",
    "url": "https://wallstreetcn.com/premium/articles/3776551?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T04:24:09+00:00",
    "summary": "彭博社一张图把中国资产的相对低迷推到聚光灯下：MSCI中国相对MSCI全球的收益比值，已降至2001年以来少见低位。但这并不意味着中国资产缺少机会，而是MSCI中国的指数结构没有充分暴露于本轮全球AI硬件和科技牛市。随着全球AI交易拥挤、海外资金低配中国、A股硬科技和中国AI价值链开始被重新定价，全球资金正在从“是否回避中国”转向“如何重新配置中国”。这是全面反转的信号，还是一轮结构性重估的开始？"
  },
  {
    "id": "wscn:3776714",
    "domain": "股票",
    "title": "全球存储扩产+海外设备供应告急，国产半导体设备迎“超级时代”",
    "url": "https://wallstreetcn.com/articles/3776714",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T04:00:53+00:00",
    "summary": "国金证券认为AI算力驱动存储扩产，国产半导体设备迎历史机遇。海外设备交期拉长至12-24个月，长鑫、长江存储2026年采购规模预计达550-630亿元，国产替代加速落地。量检测与FT测试设备国产化率最低，替代空间最大，为当前核心关注方向。风险在于资本开支不及预期及验证进度滞后。"
  },
  {
    "id": "wscn:3776709",
    "domain": "股票",
    "title": "蚂蚁灵波，为什么要从头训练机器人大脑",
    "url": "https://wallstreetcn.com/articles/3776709",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T03:21:53+00:00",
    "summary": "灵波发布 6 款模型，更像是在拆解机器人大脑仍未解决的单点问题。模型数量未来反而可能减少。"
  },
  {
    "id": "wscn:3776708",
    "domain": "股票",
    "title": "翰森制药的出海，不靠声量",
    "url": "https://wallstreetcn.com/articles/3776708",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T03:21:47+00:00",
    "summary": "一次三期成功，兑现的是走了十年的路。"
  },
  {
    "id": "wscn:3776715",
    "domain": "股票",
    "title": "三星电子将龙仁首座芯片厂投产提前至2029年，比原计划早1-2年",
    "url": "https://wallstreetcn.com/articles/3776715",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T03:18:32+00:00",
    "summary": "报道称三星电子已将龙仁国家产业园区首座晶圆厂的投产目标定为2029年，较此前市场预期的2030至2031年有所提前。三星电子此前已宣布，将在平泽、龙仁半导体集群等地合计投资2030万亿韩元。投产时间的提前，意味着三星电子得以更迅速地回应全球人工智能芯片需求的快速增长。"
  },
  {
    "id": "wscn:3776710",
    "domain": "股票",
    "title": "伊朗关闭霍尔木兹海峡、打击美在中东目标，美军对伊发动新一轮袭击、多地传出爆炸声",
    "url": "https://wallstreetcn.com/articles/3776710",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T03:06:04+00:00",
    "summary": "伊朗革命卫队于7月12日宣布封闭霍尔木兹海峡，禁止所有船只通行，直至美国停止干预为止。美军宣布对伊朗发动打击，以回应海峡民用船只遇袭事件。伊朗随后对美国在中东多国目标实施报复。巴林、约旦、科威特、卡塔尔、阿联酋相继响起防空警报或爆炸声，伊朗南部多地亦传出爆炸。"
  },
  {
    "id": "wscn:3776713",
    "domain": "股票",
    "title": "美银Hartnett：日本银行股是“全球避险情绪领先指标”，下半年有“四大逆向交易机会”",
    "url": "https://wallstreetcn.com/articles/3776713",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T02:46:01+00:00",
    "summary": "美银策略师Hartnett警告，当前市场存在\"四个不\"共识：美国经济不着陆、美联储不加息、AI资本开支不削减、美国民主党不横扫中期选举。这种罕见的全面乐观本身即为最大风险，任一共识落空将引发剧烈重定价。他提出四类逆向交易策略，并将日本银行股视为全球风险偏好的预警指标。"
  },
  {
    "id": "wscn:3776632",
    "domain": "股票",
    "title": "下周重磅日程：中国GDP与美国CPI、沃什听证会、WAIC大会、长鑫科技打新与台积电财报",
    "url": "https://wallstreetcn.com/articles/3776632",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T02:05:46+00:00",
    "summary": "美国6月CPI、PPI及经济褐皮书密集出炉，美联储主席沃什首次出席国会听证；中国二季度GDP、社零、工业增加值等数据同步亮相。WAIC人工智能大会召开，华为Atlas 950真机或首秀，Gemini 3.5 Pro传将发布。财报季方面，华尔街五大行同日放榜，ASML、台积电验证AI需求；国内长鑫科技IPO打新备受关注。此外，韩国央行预计时隔五年重启加息，而霍尔木兹再度关闭，美伊局势再升级。"
  },
  {
    "id": "wscn:3776712",
    "domain": "股票",
    "title": "财报季、沃什和美国通胀--美联储和市场将走向何方？下周“初见端倪”！",
    "url": "https://wallstreetcn.com/articles/3776712",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T01:36:15+00:00",
    "summary": "美联储新主席沃什下周将首次出席国会听证，恰逢美国6月CPI、PPI数据密集发布。市场对7月加息隐含概率仅24%，彭博经济学家认为超预期通胀与沃什鹰派表态同时发生概率不高。而高盛认为美联储政策路径的不确定性，已成为短期内股市面临的最关键风险变量，叠加下周Q2财报季开幕，市场波动性或将显著上升。"
  },
  {
    "id": "wscn:3776711",
    "domain": "股票",
    "title": "不是稀土，却胜似稀土：中国为何开始管控氦气出口？一场半导体供应链保卫战正在展开",
    "url": "https://wallstreetcn.com/premium/articles/3776711?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T00:40:55+00:00",
    "summary": "从气球填充气体到AI时代的“隐形命脉”，氦气正在经历一场产业价值重估。2026年7月，中国宣布限制氦气出口，而全球市场此前已经因卡塔尔供应扰动、俄罗斯出口收紧以及AI半导体需求爆发陷入紧平衡。作为先进制程、HBM、高速光通信和航空航天领域不可替代的关键材料，氦气的重要性正在快速提升。此次政策并非简单的贸易限制，而是全球产业链围绕稀缺资源展开竞争的缩影。随着供应端约束长期存在、需求端受AI产业驱动持"
  },
  {
    "id": "wscn:3776706",
    "domain": "股票",
    "title": "全球市场步入“动荡之夏”：警惕美联储变局、日元危机和财报季大考",
    "url": "https://wallstreetcn.com/articles/3776706",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T12:11:58+00:00",
    "summary": "全球金融市场看似平静却暗流汹涌：美联储新主席沃什减少前瞻指引放大政策不确定性，日元跌破162关口再触套利爆仓危机。瑞银脆弱度指标飚至0.9高位，单股波动率超指数三倍。在夏季流动性匮乏之际，美股二季度财报24%的高增长预期一旦落空，恐引爆指数级剧烈回撤。"
  },
  {
    "id": "wscn:3776707",
    "domain": "股票",
    "title": "智谱创始人唐杰发布内部信：将开启 Touch High（摸高）计划，“不登顶，就是失败”",
    "url": "https://wallstreetcn.com/articles/3776707",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T11:32:09+00:00",
    "summary": "今日智谱创始人唐杰发布内部信，阐述智谱对 AGI 接下来竞争的理解。唐杰在信中表示，智谱接下来将继续延续所谓 “反直觉” 路线，开启 “Touch High（摸高）计划”，即继续聚焦于 AGI 研究，而不是短期商业变现。"
  },
  {
    "id": "wscn:3776705",
    "domain": "股票",
    "title": "伊朗最高领袖称将报复美以，特朗普：1000枚导弹已瞄准伊朗",
    "url": "https://wallstreetcn.com/articles/3776705",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T11:02:00+00:00",
    "summary": "穆杰塔巴再次将美国和以色列列为已故最高领袖及其他遇难者遇难事件的责任方，表示伊朗将继续追究其责任，并强调将作出报复回应。美国总统特朗普10日说，1000枚导弹已瞄准伊朗。若伊朗暗杀或试图暗杀他本人，还会有数千枚导弹随即发射。"
  },
  {
    "id": "wscn:3776704",
    "domain": "股票",
    "title": "成也 Seedance 2.0，败也 Seedance 2.0！AI漫剧行业已经没有了？",
    "url": "https://wallstreetcn.com/articles/3776704",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T10:28:23+00:00",
    "summary": "国内 AI 漫剧和 AI 剧已经从「效率红利」进入「慢性死亡」：政策风向、平台流量、供给爆炸、工具公司被大厂挤压，几股力量叠在一起，把一个刚刚冒头的内容生意迅速打成了彩票生意。"
  },
  {
    "id": "wscn:3776703",
    "domain": "股票",
    "title": "阿里合计持股长鑫科技近5%，超过董事长朱一明",
    "url": "https://wallstreetcn.com/articles/3776703",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T08:22:28+00:00",
    "summary": "阿里巴巴以76亿元押注长鑫科技，合计持股近5%，持股数量甚至超过创始人朱一明。这笔投资远不止财务回报——长鑫科技已是阿里云核心供应商，双方深度绑定\"算存一体化\"产业链。此次长鑫科技冲刺科创板第二大IPO，募资295亿元，阿里从存储芯片、大模型到具身智能的全链布局正加速兑现。"
  },
  {
    "id": "wscn:3776701",
    "domain": "股票",
    "title": "过去两年规模几乎翻倍，美国ETF“火的发烫”",
    "url": "https://wallstreetcn.com/articles/3776701",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T06:00:08+00:00",
    "summary": "美国ETF行业正经历史无前例的扩张，2026年资产规模逼近16万亿美元，年内净流入破万亿。主动型ETF包揽四成资金，杠杆ETF成交量激增50%放大流动性。精准化集中主题ETF崛起，美股科技与半导体成核心驱动力。"
  },
  {
    "id": "wscn:3776698",
    "domain": "股票",
    "title": "1个月上涨25%后，美国生物医药板块周五重挫",
    "url": "https://wallstreetcn.com/articles/3776698",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T05:26:59+00:00",
    "summary": "美股生物医药板块因集中获利了结引发急跌，高贝塔代表性ETF（XBI）单日大跌4%。Moderna、ImmunityBio等年内暴涨股在无基本面利空的情况下回撤8%~11%，资金呈现从高风险小盘股向强防御大市值药企跨板块结构性轮动。"
  },
  {
    "id": "wscn:3776700",
    "domain": "股票",
    "title": "昂跑亚太区将换帅，中国增长功臣升任全球市场负责人",
    "url": "https://wallstreetcn.com/articles/3776700",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T05:04:49+00:00",
    "summary": "继任者未定"
  },
  {
    "id": "wscn:3776699",
    "domain": "股票",
    "title": "牧原上半年预亏57亿至67亿元 降本与屠宰业务提供缓冲",
    "url": "https://wallstreetcn.com/articles/3776699",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-11T05:02:45+00:00",
    "summary": "成本持续压降"
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
    "id": "hn:48505968",
    "domain": "股票",
    "title": "Elon Musk Becomes First Trillionaire as SpaceX Starts Trading",
    "url": "https://www.nytimes.com/live/2026/06/12/business/spacex-ipo-elon-musk/heres-the-latest",
    "source": "droidjj",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-06-12T16:13:49+00:00",
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
    "id": "hn:48506701",
    "domain": "股票",
    "title": "SpaceX increases almost 30% after biggest IPO",
    "url": "https://www.cnbc.com/2026/06/12/spacex-ipo-spcx-live-updates.html",
    "source": "somenameforme",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-06-12T17:10:07+00:00",
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
    "id": "hn:48717469",
    "domain": "金融",
    "title": "The CEO of Mullvad is the main financer of the Swedish Örebro party",
    "url": "https://det.social/@lostgen/116820546568940358",
    "source": "Risse",
    "platform": "hackernews",
    "points": 694,
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
    "id": "hn:48878126",
    "domain": "金融",
    "title": "Under federal rule, colleges must leave grads better off or lose financial aid",
    "url": "https://www.npr.org/2026/06/30/nx-s1-5835631/turner-camhi-do-no-harm-college-loans",
    "source": "nradov",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-07-12T04:00:14+00:00",
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
    "id": "hn:48735748",
    "domain": "金融",
    "title": "Supreme Court takes sledgehammer to federal regulatory structure",
    "url": "https://www.npr.org/2026/06/29/nx-s1-5875161/supreme-court-takes-sledgehammer-to-much-of-federal-governments-regulatory-structure",
    "source": "marojejian",
    "platform": "hackernews",
    "points": 82,
    "published_at": "2026-06-30T17:05:58+00:00",
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
    "id": "hn:48849827",
    "domain": "金融",
    "title": "FrontierFinance: The largest open benchmark for investor workflows",
    "url": "https://research.samaya.ai/benchmarks/frontier-finance",
    "source": "ashwinpp",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-09T17:49:05+00:00",
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
    "id": "hn:48609233",
    "domain": "金融",
    "title": "Big Tech is borrowing like never before",
    "url": "https://startupfortune.com/big-tech-is-borrowing-like-never-before-and-the-fed-just-made-that-a-lot-more-expensive/",
    "source": "krupan",
    "platform": "hackernews",
    "points": 64,
    "published_at": "2026-06-20T13:49:15+00:00",
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
    "id": "hn:48678494",
    "domain": "金融",
    "title": "Feds deny Polestar authorization to sell cars in US from model year 2027",
    "url": "https://arstechnica.com/cars/2026/06/feds-deny-polestar-authorization-to-sell-cars-in-us-from-model-year-2027/",
    "source": "Quinner",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-06-25T20:00:35+00:00",
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
    "id": "hn:48779065",
    "domain": "金融",
    "title": "Tesla Robotaxi Launches in Miami",
    "url": "https://twitter.com/robotaxi/status/2073030246161367153",
    "source": "spikels",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-07-03T19:38:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:48546358",
    "domain": "金融",
    "title": "US Government Reportedly Allowing Federal Data Center Rules to Expire",
    "url": "https://gizmodo.com/us-government-reportedly-allowing-federal-data-center-rules-to-expire-2000772083",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-06-15T20:06:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48763600",
    "domain": "金融",
    "title": "Married couple killed in first known fatal Tesla Semi crash",
    "url": "https://www.sfchronicle.com/tech/article/tesla-semi-fatal-crash-22329122.php",
    "source": "FireBeyond",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-02T16:09:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:48673197",
    "domain": "金融",
    "title": "Federating Clusters for Zero-Downtime Kubernetes",
    "url": "https://linkerd.io/2026/06/24/federating-clusters-for-zero-downtime-kubernetes/index.html",
    "source": "PagCatOli",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-06-25T13:37:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:48518434",
    "domain": "金融",
    "title": "Gas Prices Wipe Out More Than a Year of Wage Gains",
    "url": "https://www.wsj.com/economy/inflation-wages-american-workers-cbe3f187",
    "source": "karakoram",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-06-13T15:49:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:48613112",
    "domain": "金融",
    "title": "Dallas Fed: 30% of housing cost increase driven by unauthorized immigration [pdf]",
    "url": "https://www.dallasfed.org/~/media/documents/research/papers/2026/wp2607.pdf",
    "source": "silexia",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-06-20T21:25:10+00:00",
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
    "id": "hn:48677039",
    "domain": "金融",
    "title": "The AI Data-Center Boom Is Sparking a Third Wave of Inflation",
    "url": "https://www.wsj.com/economy/the-data-center-boom-is-sparking-a-third-wave-of-inflation-926adc6e",
    "source": "gmays",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-06-25T17:58:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48678979",
    "domain": "金融",
    "title": "Trump administration asks OpenAI to stagger release of new model",
    "url": "https://ca.finance.yahoo.com/news/trump-administration-asks-openai-stagger-204300837.html",
    "source": "fla",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-06-25T20:47:46+00:00",
    "summary": ""
  }
]
```
