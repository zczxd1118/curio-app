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

- 今日日期：`2026-07-13`
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
  "date": "2026-07-13",
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
    "points": 3727871,
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
    "points": 1487734,
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
    "points": 1379026,
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
    "points": 1373947,
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
    "points": 1219777,
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
    "points": 965579,
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
    "points": 941332,
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
    "points": 878887,
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
    "points": 836636,
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
    "points": 590093,
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
    "points": 521050,
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
    "points": 437140,
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
    "points": 382683,
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
    "points": 362958,
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
    "points": 238133,
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
    "points": 235262,
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
    "points": 217660,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1kxLD6HEYN",
    "domain": "AI",
    "title": "Claude Code怎么全自动跑13小时？实测GLM 5.2开源天花板",
    "url": "http://www.bilibili.com/video/av116763920438810",
    "source": "小白debug",
    "platform": "bilibili",
    "points": 215062,
    "published_at": "2026-06-17T10:14:02+00:00",
    "summary": "我手搓了一个Openclaw"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 198403,
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
    "points": 182498,
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
    "points": 176911,
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
    "points": 161496,
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
    "points": 159508,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1QE7N6jEuQ",
    "domain": "AI",
    "title": "真的被自己用心开发的昔涟Agent这段话感动到了",
    "url": "http://www.bilibili.com/video/av116794052316703",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 131560,
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
    "points": 106984,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 99564,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92535,
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
    "points": 83531,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1T3NE6jECj",
    "domain": "AI",
    "title": "用 AI 学技术，我做了一个 skill ｜详细教程附源码",
    "url": "http://www.bilibili.com/video/av116894262692635",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 73368,
    "published_at": "2026-07-10T09:26:30+00:00",
    "summary": "以公众号作为信息源，开发一个信息雷达Agent系统。可以自动抓取、通知和沉淀有价值的文章。再基于各种优质的技术文章做一个技术学习路线图 Skill ，只需要给AI提供一个想要学的内容，Agent就能规划出完整的学习路线。\n完整提示词\n\n文字版攻略：\nhttps://github.com/tech-shrimp/tech-shrimp-qclaw-project\n前后端完整代码：\nhttps://g"
  },
  {
    "id": "bvid:BV1heMh6fEm9",
    "domain": "AI",
    "title": "【城】大厂Agent实战对比，谁能真正帮打工人摸鱼｜含Skill实战",
    "url": "http://www.bilibili.com/video/av116879297352139",
    "source": "网络小白_Uncle城",
    "platform": "bilibili",
    "points": 73286,
    "published_at": "2026-07-08T10:00:00+00:00",
    "summary": "三款桌面端AI Agent同台PK，同样是Deepseek-V4-Pro模型，谁更能帮打工人干活(。・ω・。)？\n本期视频我把网易有道LobsterAI、腾讯workbuddy、字节TRAE Work拉到一起，三个真实工作任务从头跑到尾，只看Agent本身行不行＞︿＜\nExcel整合报表、竞品调研方案、数据看板网页部署……结果嘛，有的能交差，有的返工，有的重做::&gt;_&lt;::\n到底谁才是"
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 62622,
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
    "points": 53013,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1KDNA6eEgr",
    "domain": "AI",
    "title": "Claude Code 暗藏监控后门！专门标记中国用户｜Unicode 隐写 + 时区检测深度拆解",
    "url": "http://www.bilibili.com/video/av116901594337479",
    "source": "网络小白_Uncle城",
    "platform": "bilibili",
    "points": 47606,
    "published_at": "2026-07-12T03:30:00+00:00",
    "summary": "2026年6月30日，Reddit用户逆向Claude Code时撞见了一套隐藏的检测代码：每次AI请求，用一个肉眼无法分辨的Unicode字符，标记出你是不是【中国用户】。这个后门从4月2日运行到被发现，整整三个月。\n这期视频拆解了完整技术链路：\n├ 时区检测 + 147条加密域名黑名单（XOR key=91）\n├ Unicode隐写术：U+0027 → U+2019/U+02BC/U+02B9"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47371,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1QjM366EfH",
    "domain": "AI",
    "title": "工信部发布Claude Code安全后门隐患风险提示，GPT&amp;Grok明日共同上线 | 7月8日AI日报第450期",
    "url": "http://www.bilibili.com/video/av116883642849956",
    "source": "infinite灵感港",
    "platform": "bilibili",
    "points": 47269,
    "published_at": "2026-07-08T10:30:00+00:00",
    "summary": "今日内容：\n1·NVDB发布Claude Code防范提示[00:03] \n2·Grok4.5 &amp; GPT5.6相关资讯[00:39] \n3·智谱 &amp; Deepseek相关资讯[01:04] \n4·Meta发布Muse Image模型[01:31] \n5·Claude Cowork开放手机端[01:51]"
  },
  {
    "id": "bvid:BV17WNW6kEJ1",
    "domain": "AI",
    "title": "马斯克花重金买来的 Cursor 外挂，帮助 Grok 4.5 在编程和 Agent 能力上取得巨大进步 | 浪浪妈雷达图",
    "url": "http://www.bilibili.com/video/av116897282527245",
    "source": "图灵坐标",
    "platform": "bilibili",
    "points": 38225,
    "published_at": "2026-07-11T01:58:45+00:00",
    "summary": "更新日志：\n1.将雷达图维度中的“学术认知边界”更名为“科学推理”，以降低认知负担\n2.因 AA 连续两期新模型（Claude Sonnet 5、Grok 4.5）均未公布 IFBench 基准测试分数，本频道决定将 IFBench 标为待定数据源，指令遵循维度现仅由 Text Arena IF 构成"
  },
  {
    "id": "bvid:BV1xzGH6uEG8",
    "domain": "AI",
    "title": "AI全自动化搭建复杂Simulink模型！5步即可完成部署，全流程分享！",
    "url": "http://www.bilibili.com/video/av116629870481178",
    "source": "电气攻城狮001",
    "platform": "bilibili",
    "points": 28887,
    "published_at": "2026-05-24T13:50:56+00:00",
    "summary": "本期分享五步实操流程，借助 Claude Code 交互载体接入 DeepSeek 大模型，搭配 2026.5.21 最新版 Simulink Agentic Toolkit，解锁 68 项建模技能。依次完成 API 额度配置、环境部署、工具包安装，连通校验后开启全自动模式。无需手动拖拽模块与布线，输入指令即可依托 Simscape 蓝库，在 MATLAB2026a 中自动搭建三相并网逆变器开环模"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27829,
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
    "points": 25340,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1fWixBbEgP",
    "domain": "AI",
    "title": "别再用老方法了！Cocos Creator 3.8 + AI 开发实战：从0构建可商用的登录奖励模块",
    "url": "http://www.bilibili.com/video/av115840888408359",
    "source": "游戏主程进阶之路",
    "platform": "bilibili",
    "points": 23250,
    "published_at": "2026-01-05T05:43:24+00:00",
    "summary": "需 要 源 码 请 【＋O、O、裙】【822】【159】【534】"
  },
  {
    "id": "bvid:BV1JU7E6PEar",
    "domain": "AI",
    "title": "Cursor 已死？我为什么要退订 Cursor ？",
    "url": "http://www.bilibili.com/video/av116819553683121",
    "source": "祥子在学AI",
    "platform": "bilibili",
    "points": 22734,
    "published_at": "2026-06-27T01:52:00+00:00",
    "summary": "当了一年多的 Cursor 重度用户，最近把它退订了。\n\n不是它变差了，是 Claude Code 和 Codex 真的太好用了。\n\n几个真实感受： ① 大模型越来越强，我已经不怎么手写代码了 ② Cursor 套的是 VS Code 壳子，只属于程序员 ③ 底层模型不在一个量级——Claude 有 Opus 和 Fable 5，Codex 有 GPT 5.5/5.6，Cursor 的 Compo"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22618,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1cCEi6sEU5",
    "domain": "AI",
    "title": "🦊他能成功吗？Claude Code 接管虚幻引擎5，打造一款游戏 | 带你走完整个流程",
    "url": "http://www.bilibili.com/video/av116731724959171",
    "source": "Apeak_虚幻丰哥",
    "platform": "bilibili",
    "points": 18119,
    "published_at": "2026-06-11T13:41:36+00:00",
    "summary": "Claude Code 接管虚幻引擎5，打造了一款游戏\n下载我的 CLAUDE.md（帮你省 token 的配置）\n链接：https://pan.quark.cn/s/b6e50b4b2535\n提取码：tbaE\nStefan 3D AI ：https://www.youtube.com/watch?v=iRcrZjOt5H8&amp;t=1s\n🔗 完整教程指南和链接：https://www.top"
  },
  {
    "id": "bvid:BV1etEQ6DETs",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116724192118321",
    "source": "AI产品经理大模型",
    "platform": "bilibili",
    "points": 13544,
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
    "points": 12975,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1WBTX6kE1B",
    "domain": "AI",
    "title": "【2026版】这绝对是B站唯一将Vibe Coding从入门到实战讲明白的教程，手把手带你从入门到代码实战开发，存下吧，比啃书好太多了！拿走不谢，允许白嫖！",
    "url": "http://www.bilibili.com/video/av116871663722218",
    "source": "码士集团-马小雪",
    "platform": "bilibili",
    "points": 10153,
    "published_at": "2026-07-06T06:47:51+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！ 【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV12ojm64EU6",
    "domain": "AI",
    "title": "🧲 Claude Code 工作流：长程任务的规划和执行利器 ⛓️",
    "url": "http://www.bilibili.com/video/av116800494767674",
    "source": "沧海九粟",
    "platform": "bilibili",
    "points": 9663,
    "published_at": "2026-06-24T00:00:00+00:00",
    "summary": "GAC 平台：https://gaccode.com/signup?ref=UWDADYQI\n官方文档：https://code.claude.com/docs/en/workflows\n状态栏技能：https://github.com/webup/skills-cc#-webup-statusline"
  },
  {
    "id": "bvid:BV1QnML6pEZr",
    "domain": "AI",
    "title": "2026年过半，我是怎样使用 Agent 的？",
    "url": "http://www.bilibili.com/video/av116887417522347",
    "source": "卡普迪姆",
    "platform": "bilibili",
    "points": 8353,
    "published_at": "2026-07-09T01:31:02+00:00",
    "summary": "调度 sub-agent 的提示词原图在图文版里，放在公众号：减 AI\n其实核心就是让 cc 怎么利用 codex exec 调用便宜的 gpt 5.5\n看完视频后，欢迎在评论区交流分享自己的使用心得！\n\n相关引用：\n[1]: https://x.com/theo/status/2072482460122964067\n[2]: https://github.com/mattpocock/skill"
  },
  {
    "id": "bvid:BV1aVMp63Ee7",
    "domain": "AI",
    "title": "把你的hermes打造成满血全模态：生图+生视频+图片理解+视频理解+语音生成~ | Agnes+Minimax M3",
    "url": "http://www.bilibili.com/video/av116891494387060",
    "source": "在下李君陌",
    "platform": "bilibili",
    "points": 7630,
    "published_at": "2026-07-09T18:46:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1g4MP6SEqJ",
    "domain": "AI",
    "title": "🚀Claude Code有后门？立即锁进Docker Sandboxes里！sbx完整实测：Claude Code、Codex、OpenCode安全隔离运行",
    "url": "http://www.bilibili.com/video/av116862151038488",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 6717,
    "published_at": "2026-07-04T14:23:41+00:00",
    "summary": "视频简介：\nClaude Code有后门？立即锁进Docker Sandboxes里！sbx完整实测：Claude Code、Codex、OpenCode如何安全隔离运行！防隐私泄露、防恶意Skill和MCP \n别再裸奔运行Claude Code了！我用Docker Sandboxes把Claude、Codex、OpenCode全锁进沙盒，实测能不能防隐私泄露和恶意MCP\nClaude Code、"
  },
  {
    "id": "hn:48873836",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, CoreWeave, and Nebius: Inside the Circular Financing of the GPU Boom",
    "url": "https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom",
    "source": "adletbalzhanov",
    "platform": "hackernews",
    "points": 362,
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
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/964539/lorde-says-ray-ban-meta-ai-glasses-are-not-sexy",
    "domain": "大厂 AI 动态",
    "title": "Lorde says Ray-Ban Meta AI glasses are ‘not sexy’",
    "url": "https://www.theverge.com/ai-artificial-intelligence/964539/lorde-says-ray-ban-meta-ai-glasses-are-not-sexy",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T20:10:19+00:00",
    "summary": "Lorde was performing at the Real Cool Festival in Madrid on Thursday and took some time during her set to speak out against AI glasses. While she didn't specify any brands in particular, it's likely s"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/964532/the-soft-pink-truth-shall-we-go-on-sinning-so-that-grace-may-increase-review",
    "domain": "大厂 AI 动态",
    "title": "Shall We Go On Sinning So That Grace May Increase? is hypnotic, healing, and hopeful",
    "url": "https://www.theverge.com/entertainment/964532/the-soft-pink-truth-shall-we-go-on-sinning-so-that-grace-may-increase-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T19:40:00+00:00",
    "summary": "Matmos are an incredibly accomplished duo between their own solo records like the masterpiece A Chance to Cut Is a Chance to Cure and production classic Bjork records like Vespertine. But Drew Daniel,"
  },
  {
    "id": "rss:https://www.theverge.com/tech/964519/apple-silicon-self-driving-car-ai-m7-ultra",
    "domain": "大厂 AI 动态",
    "title": "Apple’s failed self-driving car program left a legacy of powerful AI chips",
    "url": "https://www.theverge.com/tech/964519/apple-silicon-self-driving-car-ai-m7-ultra",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T16:27:06+00:00",
    "summary": "Apple's self-driving car program never really got off the ground, but it may have been what made the company's chips the powerful AI performers they are. Early in the development of the self-driving p"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/964125/steelseries-arctis-nova-pro-wireless-headset-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "One of SteelSeries&#8217; best gaming headsets is over $100 off",
    "url": "https://www.theverge.com/gadgets/964125/steelseries-arctis-nova-pro-wireless-headset-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T15:00:00+00:00",
    "summary": "SteelSeries has the Arctis Nova Pro Wireless gaming headset on sale for $239.99 (currently between $300 and $350 at other retailers). The Xbox version that supports a host of other platforms including"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/964515/philips-hue-smart-lights-version-history",
    "domain": "大厂 AI 动态",
    "title": "How Philips Hue got the smart home right",
    "url": "https://www.theverge.com/podcast/964515/philips-hue-smart-lights-version-history",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T14:38:01+00:00",
    "summary": "The state of the smart home can be frustrating, because it is just so obvious how things ought to work. You should be able to control everything from everywhere. Your spaces should adapt to what you'r"
  },
  {
    "id": "rss:https://www.theverge.com/tech/964386/oura-ring-5-review-smart-ring-wearables",
    "domain": "大厂 AI 动态",
    "title": "Less is more with the Oura Ring 5",
    "url": "https://www.theverge.com/tech/964386/oura-ring-5-review-smart-ring-wearables",
    "source": "Victoria Song",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T14:00:00+00:00",
    "summary": "If you're reading an Oura Ring 5 review at The Verge, you likely fall into one of two camps: newcomers looking for a smartwatch alternative, or Oura users pondering an upgrade. In the case of the form"
  },
  {
    "id": "rss:https://www.theverge.com/games/964262/blue-prince-family-bonding",
    "domain": "大厂 AI 动态",
    "title": "Blue Prince became a bonding — and learning — experience for my family",
    "url": "https://www.theverge.com/games/964262/blue-prince-family-bonding",
    "source": "John.Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T13:00:00+00:00",
    "summary": "I've always been the gamer in the family. When my son was born nearly 11 years ago, gaming was one of the things I looked forward to sharing with him. Pulling up a chair next to me, he would watch as "
  },
  {
    "id": "rss:https://www.theverge.com/column/963346/ai-data-centers-fight",
    "domain": "大厂 AI 动态",
    "title": "The fight against AI data centers is just beginning",
    "url": "https://www.theverge.com/column/963346/ai-data-centers-fight",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T12:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more on the data center buildout, follow Emma Roth. The Stepback arrives in our subscribers' inboxe"
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
    "summary": "Ninja's latest slushie machine builds on the popularity of the original Slushi, but with a big upgrade."
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
    "id": "rss:https://arstechnica.com/culture/2026/07/the-real-mystery-behind-moana-after-1700-years-why-did-polynesians-suddenly-sail-east/",
    "domain": "大厂 AI 动态",
    "title": "The real mystery behind Moana: After 1,700 years, why did Polynesians suddenly sail east?",
    "url": "https://arstechnica.com/culture/2026/07/the-real-mystery-behind-moana-after-1700-years-why-did-polynesians-suddenly-sail-east/",
    "source": "David Sear, Manoj Joshi, and Mark Peaple, The Conversation",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T11:12:19+00:00",
    "summary": "New climate evidence adds context to these long voyages."
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
    "id": "rss:https://36kr.com/p/3893457328700165?f=rss",
    "domain": "大厂 AI 动态",
    "title": "一场高转化抽奖活动应该怎么设计？从奖品、规则到传播路径的完整拆解",
    "url": "https://36kr.com/p/3893457328700165?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T05:27:38+00:00",
    "summary": "在微信私域生态中，抽奖几乎是商家长期使用的互动玩法：公众号涨粉、社群促活、线下门店引流、会员权益发放、品牌活动传播，都能看到它的身影。它的优势很直接：用户理解门槛低、参与反馈快、成本相对可控，也容易和微信内的公众号、社群、小程序、门店场景结合。 但也正因为抽奖看起来简单，很多活动最后只做成了“一次热闹”。参与人数有了，目标用户没沉淀；奖品发出去了，后续转化没接住；前端页面很热闹，后端领奖、核销、数"
  },
  {
    "id": "rss:https://36kr.com/p/3893519389293056?f=rss",
    "domain": "大厂 AI 动态",
    "title": "倩碧押注PDRN护肤赛道，高端美妆品牌加速切入医美护理市场｜最前线",
    "url": "https://36kr.com/p/3893519389293056?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T03:33:13+00:00",
    "summary": "随着医美消费逐渐从单次项目体验转向长期肌肤管理，传统高端护肤品牌正在寻找新的增长空间。 36氪获悉，近日，雅诗兰黛集团旗下品牌倩碧在中国发布CX肌源深修水光系列产品，切入近年来快速升温的PDRN（聚脱氧核糖核苷酸）护肤赛道。 该系列以重组PDRN为核心成分。据雅诗兰黛集团介绍，这是全球首款以重组PDRN为核心成分的护肤产品。此次新品发布，也是倩碧近年来持续强化“科学护肤”和医美护理关联度的重要动作"
  },
  {
    "id": "rss:https://36kr.com/p/3893430641703429?f=rss",
    "domain": "大厂 AI 动态",
    "title": "lululemon「割不动」中国人了",
    "url": "https://36kr.com/p/3893430641703429?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T03:07:43+00:00",
    "summary": "作者 |&nbsp;谢芸子 编辑 | 张帆 在中国市场，lululemon开始被人们拿着放大镜审视。 6月中旬，lululemon在上海北外滩举办了一场大型户外瑜伽活动，中途遭遇暴雨。lululemon并未取消活动，而是让上千人在湿滑的瑜伽垫上完成了全套动作。 现场画面被社交网络疯传。整齐划一的雨中静坐，被人们诟病为“矫揉造作”“品牌不为用户着想”，甚至被部分网友拿来与《周处除三害》中的邪教作对比"
  },
  {
    "id": "rss:https://36kr.com/p/3879780282495236?f=rss",
    "domain": "大厂 AI 动态",
    "title": "AI家庭智能硬件公司获数千万元融资，首款产品今年上线海外｜硬氪首发",
    "url": "https://36kr.com/p/3879780282495236?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T03:00:00+00:00",
    "summary": "作者｜黄楠 编辑｜袁斯来 硬氪获悉，威联机器人科技（深圳）有限公司（以下简称“MOVA LINCO”）近日完成数千万元天使融资。融资资金将主要用于AI算法底层技术研发、完善产品量产体系，以及全球化渠道布局和家庭AI生态的持续建设。 MOVA LINCO核心团队来自头部网络通信与智能硬件企业，在路由器、NAS存储及AI算力设备等方面拥有深厚的技术积累与产品经验。公司产品矩阵以AI智能语音路由器、AI"
  },
  {
    "id": "rss:https://36kr.com/p/3893473722514181?f=rss",
    "domain": "大厂 AI 动态",
    "title": "36氪首发 | 港中大博士、前大疆工程师创业消费级四足机器人，天使轮获正轩领投数千万元",
    "url": "https://36kr.com/p/3893473722514181?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T02:47:38+00:00",
    "summary": "作者&nbsp;|&nbsp;乔钰杰 编辑&nbsp;|&nbsp;袁斯来 硬氪获悉，深圳光之跃迁科技有限公司（Lumisition Robotics）（以下简称“光之跃迁”）近日完成近五千万元天使轮融资，由正轩领投，光点资本、力合资本、松禾资本、恒信未来等机构跟投。本轮资金将主要用于产品研发、算法迭代及量产准备。 光之跃迁成立于2026年2月，聚焦消费级四足机器人市场，希望以“全地形移动底盘”切"
  },
  {
    "id": "rss:https://36kr.com/p/3893445208717826?f=rss",
    "domain": "大厂 AI 动态",
    "title": "对话Om AI赵天成：多年坚守，押注物理AI原生的「流式」未来",
    "url": "https://36kr.com/p/3893445208717826?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T02:39:18+00:00",
    "summary": "一个从未见过监控画面的多模态模型，却比在监控数据上练了多年的小模型“老将”更懂监控。这不是科幻电影，这是2023年Om AI联汇的一场“无心插柳”，也是CEO兼首席科学家赵天成博士更加坚信“多模态训练方式能为物理开放世界带来泛化性”的关键节点。彼时，AI行业正在追求以大语言模型为核心的生成式AI。 三年后，这个多模态模型演变成了VLX——全球首个面向物理AI的端侧流式多模态模型系列。首次提出“端侧"
  },
  {
    "id": "rss:https://36kr.com/p/3885232033378308?f=rss",
    "domain": "大厂 AI 动态",
    "title": "头部人形机器人关节公司半年再获新融资，同创伟业领投数亿元｜硬氪首发",
    "url": "https://36kr.com/p/3885232033378308?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T02:37:39+00:00",
    "summary": "作者｜黄楠 编辑｜袁斯来 硬氪获悉，零差云控（深圳）科技股份有限公司（以下简称“零差云控”）近日完成C++轮融资数亿元，本轮由同创伟业领投、国泰君安创新投资跟投，老股东华控基金追加投资。本轮资金将用于产能扩张和全球市场布局。源式资本担任本轮独家财务顾问，并由一苇资本和源式资本共同担任后续融资财务顾问。 人形机器人赛道在经历了概念爆火与资本狂热后，行业关键词正在悄然转变，供应链的产能与可靠性成为真正"
  },
  {
    "id": "rss:https://36kr.com/p/3890940898867712?f=rss",
    "domain": "大厂 AI 动态",
    "title": "年入4亿、服务600+品牌，膳食补充剂原料商「纽邦生物」获近2亿元C+轮融资｜36氪首发",
    "url": "https://36kr.com/p/3890940898867712?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T00:00:00+00:00",
    "summary": "文｜胡香赟 编辑｜海若镜 36氪获悉，南京纽邦生物（NNB Nutrition）近期已完成近2亿元人民币融资。本轮融资由国寿股权领投、老股东明熙资本跟投，募集资金主要用于产品研发、新工厂建设等。这也是纽邦生物半年内完成的第二笔超亿元人民币融资。 纽邦生物专注于膳食补充剂原料研发，累计推出40余款原创原料，在研产品管线超100项，覆盖运动营养、体重管理、认知健康、抗衰等领域，服务雀巢、联合利华、百事"
  },
  {
    "id": "rss:https://36kr.com/p/3893305996442118?f=rss",
    "domain": "大厂 AI 动态",
    "title": "8点1氪丨SK海力士CEO称史上最大存储短缺将在明年到来；苹果起诉OpenAI窃取商业机密‌；赛力斯预计上半年净亏损15亿元-18亿元",
    "url": "https://36kr.com/p/3893305996442118?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T23:55:49+00:00",
    "summary": "今日热点导览 世界杯决赛一块草皮卖3050元，上架后很快售空 中国石化完成对中国航油重组 巨力索具因误导性陈述被罚450万元 SK海力士考虑“内存即服务”模式，或允许客户租赁而非购买芯片 马斯克据悉要求特斯拉员工转向使用Grok TOP 3 大新闻 SK海力士CEO：2027年将成为存储行业历史上供应最紧张的一年 美东时间周五（7月10日）晚间，SK海力士首席执行官郭鲁正（Kwak Noh-jun"
  },
  {
    "id": "rss:https://36kr.com/p/3892442708032264?f=rss",
    "domain": "大厂 AI 动态",
    "title": "“背后空无一人”的LV，这次中国人彻底不买账了",
    "url": "https://36kr.com/p/3892442708032264?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-12T09:29:03+00:00",
    "summary": "LV 最近，广西一场洪水，又双叒叕让不少品牌登上热搜。 在一众的品牌捐款名单里，除了常见的消费巨头互联网大厂之外，人们还看到了一个新面孔，那就是茉莉奶白。 茉莉奶白 有人说，“自己淋雨，还想着给别人撑伞”。毕竟前不久，茉莉奶白自己还相当焦头烂额。 本来好好卖20块一杯茶饮，突然被一个卖3万包的顶级大牌闹到跟法庭相见，理由是杯子上的四叶草“近似”。网友一句话总结到位： LV跌倒，茉莉奶白吃饱。 LV"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3893685460613891?f=rss",
    "domain": "大厂 AI 动态",
    "title": "Stellantis集团2026年第二季度出货量预计为160万辆，同比增长10%",
    "url": "https://36kr.com/newsflashes/3893685460613891?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T06:21:40+00:00",
    "summary": "7月13日，Stellantis集团发布了今年第二季度其在全球范围内的出货量预测。截至2026年6月30日，Stellantis集团在今年第二季度的出货量预计为160万辆，同比2025年第二季度增长了10%，出货量的整体增长主要由北美和欧洲市场所推动。在中东和非洲，主要由于区域冲突的影响导致了集团在该地区出货量的下滑；在南美，疲软的阿根廷市场影响了集团在该地区的业绩表现。（界面）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3893684716173826?f=rss",
    "domain": "大厂 AI 动态",
    "title": "杰华特在北京成立集成电路公司，注册资本1亿",
    "url": "https://36kr.com/newsflashes/3893684716173826?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T06:20:55+00:00",
    "summary": "36氪获悉，天眼查App显示，近日，杰华特集成电路（北京）有限公司成立，法定代表人为周逊伟，注册资本1亿人民币，经营范围包括集成电路制造、集成电路设计、集成电路芯片及产品制造等。股东信息显示，该公司由杰华特微电子股份有限公司全资持股。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3893681416108544?f=rss",
    "domain": "大厂 AI 动态",
    "title": "寒武纪成交额达200亿元",
    "url": "https://36kr.com/newsflashes/3893681416108544?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T06:17:33+00:00",
    "summary": "36氪获悉，寒武纪成交额达200亿元，现跌1.24%。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3893678361328385?f=rss",
    "domain": "大厂 AI 动态",
    "title": "天威视讯换帅完成工商变更",
    "url": "https://36kr.com/newsflashes/3893678361328385?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T06:14:27+00:00",
    "summary": "36氪获悉，天眼查App显示，近日，天威视讯发生工商变更，张育民卸任法定代表人、董事长，由季彤接任。该公司成立于1995年7月，注册资本约8.03亿人民币，经营范围包括信息系统集成、互联网数据服务、物联网技术服务等，由深圳广播电影电视集团、中国电信股份有限公司等共同持股。据媒体报道，此前，该公司发布公告称，公司完成董事会换届选举，季彤正式出任公司党委书记、董事长。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3893671821064961?f=rss",
    "domain": "大厂 AI 动态",
    "title": "现货黄金向下跌破4050美元/盎司",
    "url": "https://36kr.com/newsflashes/3893671821064961?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T06:07:47+00:00",
    "summary": "36氪获悉，现货黄金向下跌破4050美元/盎司，日内下跌1.68%。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3893669541952004?f=rss",
    "domain": "大厂 AI 动态",
    "title": "滴滴亮相联合国可持续交通主题边会，分享巴西绿色出行实践",
    "url": "https://36kr.com/newsflashes/3893669541952004?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T06:05:28+00:00",
    "summary": "近日，2026年联合国可持续发展高级别政治论坛可持续交通主题边会在纽约联合国总部举行，滴滴旗下巴西出行平台99创新总监蒂亚戈·希波利托（Thiago Hipolito）受邀参会并分享了基于中国经验推动巴西可持续出行转型方面的实践。据其介绍，四年前99平台上仅有约80辆电动汽车。截至目前，这一数字已突破3.5万辆。未来五年，99计划在巴西推动超过30万辆新能源车辆登记运营，进一步推动巴西绿色出行与低"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3893664390576643?f=rss",
    "domain": "大厂 AI 动态",
    "title": "2026年暑期档票房破30亿元",
    "url": "https://36kr.com/newsflashes/3893664390576643?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T06:00:14+00:00",
    "summary": "据网络平台数据，截至目前，2026年暑期档电影总票房（含预售）突破30亿元。（央视新闻）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3893644459768578?f=rss",
    "domain": "大厂 AI 动态",
    "title": "台积电：6月营收同比增长67.9％ 环比增长6.2%",
    "url": "https://36kr.com/newsflashes/3893644459768578?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T05:39:57+00:00",
    "summary": "36氪获悉，台积电6月营收为4,426.8亿新台币，同比增长67.9％，环比增长6.2%。2026年1至6月份的总收入为24044.8亿新台币，同比增长35.6%。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3893641733667334?f=rss",
    "domain": "大厂 AI 动态",
    "title": "沪深两市成交额突破2万亿",
    "url": "https://36kr.com/newsflashes/3893641733667334?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T05:37:11+00:00",
    "summary": "36氪获悉，沪深两市成交额突破2万亿，较上一个交易日此时缩量超3700亿元。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3893631898450433?f=rss",
    "domain": "大厂 AI 动态",
    "title": "兆易创新触及跌停",
    "url": "https://36kr.com/newsflashes/3893631898450433?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T05:27:11+00:00",
    "summary": "36氪获悉，兆易创新触及跌停，成交额超300亿元。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3893564315679497?f=rss",
    "domain": "大厂 AI 动态",
    "title": "亨通光电旗下江苏新能源智控公司增资至7.7亿，增幅约31%",
    "url": "https://36kr.com/newsflashes/3893564315679497?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T05:23:22+00:00",
    "summary": "36氪获悉，天眼查App显示，近日，江苏亨通新能源智控科技有限公司发生工商变更，注册资本由约5.9亿人民币增至约7.7亿人民币，增幅约31%。该公司成立于2016年6月，法定代表人为陆春良，经营范围包括新能源技术研究、开发及推广，智能控制设备的设计、生产、销售、安装、调试及相关技术服务，充电桩系统的设计、安装、调试与运营等，由亨通光电全资持股。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3893613227178498?f=rss",
    "domain": "大厂 AI 动态",
    "title": "深成指、创业板指午后跌超3%",
    "url": "https://36kr.com/newsflashes/3893613227178498?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T05:08:11+00:00",
    "summary": "36氪获悉，深成指、创业板指午后跌超3%，沪指跌1.84%，商业航天、算力硬件、游戏传媒、半导体芯片等方向跌幅居前，沪深京三市下跌个股近4600只。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3893600659569157?f=rss",
    "domain": "大厂 AI 动态",
    "title": "美众议院本周将表决永久实行夏令时法案",
    "url": "https://36kr.com/newsflashes/3893600659569157?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T05:04:16+00:00",
    "summary": "根据美国方面消息，美国国会众议院将在本周就一项永久实行夏令时的法案进行表决。不过关于这一议题，美国国内仍然存在较大争议。今年5月，美国国会众议院能源和商业委员会以48比1的结果通过了《阳光保护法案》，该法案旨在永久取消美国每年两次调整时间的做法，让夏令时全年永久化。而美国国会参议院一些议员则威胁说，即使法案在众议院投票中通过，他们也将在参议院否决这一法案。（央视新闻）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3893598367120129?f=rss",
    "domain": "大厂 AI 动态",
    "title": "AI潮玩品牌“珞博智能”完成亿元级Pre-A轮融资",
    "url": "https://36kr.com/newsflashes/3893598367120129?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:59:02+00:00",
    "summary": "36氪获悉，近日，AI潮玩品牌珞博智能（Robopoet）正式宣布完成亿元级Pre-A轮融资。本轮融资由华映资本与广和通联合领投，涂鸦智能跟投，同时老股东红杉中国、金沙江创投持续加码跟投。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3893599860849152?f=rss",
    "domain": "大厂 AI 动态",
    "title": "陈龙强离任百信银行首席数字官，出任京东科技副总裁",
    "url": "https://36kr.com/newsflashes/3893599860849152?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:54:35+00:00",
    "summary": "原百信银行首席数字官陈龙强已正式离职，现出任京东科技副总裁，主要负责不良资产收购及数字化运营体系的搭建。（21财经）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3893563385445123?f=rss",
    "domain": "大厂 AI 动态",
    "title": "万事达卡考虑出售英国支付子公司Vocalink股权",
    "url": "https://36kr.com/newsflashes/3893563385445123?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:52:25+00:00",
    "summary": "媒体援引两名知情匿名人士消息报道，万事达卡正考虑出售旗下支付机构 Vocalink 的多数股权。万事达卡内部相关洽谈尚处于初步阶段，目前尚未收到任何确定收购报价。若出售 51% 控股权，这笔交易估值约 4 亿英镑。万事达卡方面拒绝对此事置评。（新浪财经）"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3893547816450565?f=rss",
    "domain": "大厂 AI 动态",
    "title": "腾讯等入股语用科技",
    "url": "https://36kr.com/newsflashes/3893547816450565?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:43:34+00:00",
    "summary": "36氪获悉，天眼查App显示，近日，语用（上海）科技有限公司发生工商变更，新增腾讯旗下上海启善投资有限公司、HongShan Growth VII Holdco B, Ltd.、厦门雅恒创业投资基金合伙企业（有限合伙）等为股东，同时，注册资本由25万人民币增至125万人民币。 该公司成立于2026年5月，法定代表人为林俊旸，经营范围包括软件开发、数据处理服务等，现由林俊旸及上述新增股东共同持股。"
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
    "id": "wscn:3776754",
    "domain": "股票",
    "title": "中东战事搅动市场，韩股大跌9%触发熔断，SK海力士重挫14%，原油上涨，黄金下跌",
    "url": "https://wallstreetcn.com/articles/3776754",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T06:16:18+00:00",
    "summary": "韩国KOSPI指数日内一度跌超9%，SK海力士跌14.5%，三星电子跌11%。此前韩股跌超8%，触发熔断机制，暂停交易20分钟。纳斯达克100指数期货下跌1.3%，欧洲股市开盘前期货亦显示将下跌约1%。黄金下跌1.3%，报每盎司约4065美元；白银跌幅接近3%，报每盎司约58.20美元。"
  },
  {
    "id": "wscn:3776775",
    "domain": "股票",
    "title": "高盛：伊朗战争不足以打乱通胀锚，预计美联储全年按兵不动",
    "url": "https://wallstreetcn.com/articles/3776775",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T06:16:06+00:00",
    "summary": "美伊冲突持续升温，但高盛最新研究显示，油价较战时峰值已下跌约30%，大宗商品冲击正在快速消退，通胀传导效应将于三四季度明显减弱。核心PCE月涨幅料维持20至23个基点区间，这一路径足以让美联储全年按兵不动——但容错空间极为有限，一旦油价重返100美元，货币政策天平随时可能倾斜。"
  },
  {
    "id": "wscn:3776758",
    "domain": "股票",
    "title": "创业板跌3%，科创50大跌近4%，存储芯片重挫、兆易创新跌停，恒科指跌超1%，科网股普跌",
    "url": "https://wallstreetcn.com/articles/3776758",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T06:14:28+00:00",
    "summary": "盘面上，个股呈现普跌态势，沪深京三市下跌个股超4600只。量能大幅萎缩，上午半天成交1.86万亿。沪深两市半日成交额1.85万亿，较上个交易日缩量近3200亿。板块方面，商业航天概念大幅下挫；算力硬件产业链走弱，超硬材料、PCB方向领跌；光伏、AI应用、锂电池、人形机器人、工业金属、金融科技概念股跌幅靠前。中药、银行板块逆势走强。"
  },
  {
    "id": "wscn:3776777",
    "domain": "股票",
    "title": "特朗普政府施压，SK海力士在美选址建厂，崔泰源：条件合适就投资！",
    "url": "https://wallstreetcn.com/articles/3776777",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T06:05:36+00:00",
    "summary": "SK海力士会长崔泰源首度公开表态正在全球物色存储晶圆厂选址，美国在列。这是迄今最明确的赴美建厂信号——背后是美国商务部长点名施压、美光2500亿美元扩产的步步紧逼。与此同时，海力士CEO警告2027年将现史上最严存储荒，HBM需求更是供不应求。这家市值1.2万亿美元的芯片巨头，正站在全球产业版图重构的风暴中心。"
  },
  {
    "id": "wscn:3776776",
    "domain": "股票",
    "title": "韩国银行贷款额度耗尽85%，股市杠杆资金面临断供，借钱炒股或“刹车”！",
    "url": "https://wallstreetcn.com/articles/3776776",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T05:59:44+00:00",
    "summary": "韩国信贷空间亮起红灯：五大商业银行上半年已消耗超85%的全年家庭贷款额度，其中两家更是直接“超限”。受监管总量管控限制，下半年信贷面临“断崖式”收紧，银行将被迫压降余额。这导致此前由住房和信用贷款持续驱动的增量资金来源遭切断，下半年股市加杠杆的外部融资通道将实质性收窄，市场杠杆资金面临强制降温。"
  },
  {
    "id": "wscn:3776772",
    "domain": "股票",
    "title": "三星已完成特斯拉AI5芯片流片，即将进入大规模量产准备阶段",
    "url": "https://wallstreetcn.com/articles/3776772",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T05:56:46+00:00",
    "summary": "特斯拉下一代AI芯片AI5已完成流片，即将在三星德克萨斯泰勒工厂以2纳米工艺量产，这是三星晶圆代工首次承接超大型2纳米商业订单。当前非存储器部门单季亏损约6000亿韩元，分析人士认为，随着明年特斯拉订单正式出货，三星晶圆代工扭亏在望，但量产良率仍是关键变数。"
  },
  {
    "id": "wscn:3776773",
    "domain": "股票",
    "title": "美AI巨头发债2440亿较去年翻倍，债市喊撑不住了",
    "url": "https://wallstreetcn.com/articles/3776773",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T05:54:36+00:00",
    "summary": "科技巨头的AI军备竞赛正将债券市场逼向极限。Alphabet、亚马逊、Meta等六大\"AI超大规模计算商\"今年已累计发债2440亿美元，较去年翻超一倍。英伟达、亚马逊接连250亿美元的发行令市场猝不及防，信用利差加速走阔。更令投资者不安的是——这场烧钱竞赛远未终止，数千亿新债仍在路上。"
  },
  {
    "id": "wscn:3776769",
    "domain": "股票",
    "title": "调整已至尾声，新一轮上涨缓图之",
    "url": "https://wallstreetcn.com/articles/3776769",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T05:47:09+00:00",
    "summary": "申万宏源认为，科技与非科技板块调整结构已趋完备，本轮市场调整步入尾声。短期资金惯性被打破，上涨节奏放缓，需等待新产业催化重启行情。中期AI产业趋势仍是主战场，未来行情将呈“科技领涨、百花齐放”格局。"
  },
  {
    "id": "wscn:3776725",
    "domain": "股票",
    "title": "BBU小圆柱电池——AI算力时代的“隐形刚需”，被低估的千亿级赛道？",
    "url": "https://wallstreetcn.com/premium/articles/3776725?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T05:38:13+00:00",
    "summary": "BBU（电池备份单元）正从AI服务器的“可选配件”跃升为“架构刚需”，2026-2030年全球BBU电芯需求将从近4亿颗爆发式增长至28亿颗，市场空间有望突破1000亿元。"
  },
  {
    "id": "wscn:3776774",
    "domain": "股票",
    "title": "台积电6月营收4426.8亿元台币，同比增长67.9％创纪录，上半年揽入逾2.4万亿新台币",
    "url": "https://wallstreetcn.com/articles/3776774",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T05:33:28+00:00",
    "summary": "彭博计算显示台积电第二季度营收1.27万亿元台币。分析师普遍预期，2026年第三季度单季营收有望刷新历史纪录，全年营收增速或维持在30%以上的高景气区间。数据显示，2026年1至6月合并营收合计约2.40万亿元新台币，较去年同期增长35.6%。"
  },
  {
    "id": "wscn:3776768",
    "domain": "股票",
    "title": "红烛故事停服 字节继续调整内容业务版图",
    "url": "https://wallstreetcn.com/articles/3776768",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T05:22:10+00:00",
    "summary": "资源有新投向。"
  },
  {
    "id": "wscn:3776717",
    "domain": "股票",
    "title": "油价崩了，CPI降了：美国6月CPI会改变美联储路径吗？",
    "url": "https://wallstreetcn.com/premium/articles/3776717?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T05:22:00+00:00",
    "summary": "6月CPI或因油价回落明显降温，但核心通胀粘性仍强，美联储短期料维持观望，政策转向仍待后续。"
  },
  {
    "id": "wscn:3776771",
    "domain": "股票",
    "title": "韩国政府：将设立“未来应对基金”，推进AI半导体等三大“超级项目”",
    "url": "https://wallstreetcn.com/articles/3776771",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T05:16:05+00:00",
    "summary": "更多消息，持续更新中"
  },
  {
    "id": "wscn:3776770",
    "domain": "股票",
    "title": "量产与动工同月落地、十年长约锁定北美：台积电封装“第二增长曲线”浮出水面",
    "url": "https://wallstreetcn.com/articles/3776770",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:56:35+00:00",
    "summary": "AI芯片需求持续爆发，台积电正以前所未有的速度重构全球先进封装版图。嘉义二期破土、美国亚利桑那双厂落子，CoWoS产能订单排至2027年，年复合增速超80%。先进封装营收占比将于2027年突破15%，正式跃升为台积电继先进制程之后的第二条核心增长引擎。"
  },
  {
    "id": "wscn:3776562",
    "domain": "股票",
    "title": "交换机超级周期：AI\"第三个算力瓶颈\"，以太网主宰万亿盛宴？",
    "url": "https://wallstreetcn.com/premium/articles/3776562?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:27:39+00:00",
    "summary": "全球AI以太网数据中心交换机市场正经历前所未有的超级周期，2025-2030年CAGR高达61%，市场规模将从约81亿美元飙升至889亿美元。"
  },
  {
    "id": "wscn:3776767",
    "domain": "股票",
    "title": "时隔4个月，“海选”总经理到位，海富通副总魏峻履新鹏安基金",
    "url": "https://wallstreetcn.com/articles/3776767",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:13:00+00:00",
    "summary": "业内人才均衡布局中"
  },
  {
    "id": "wscn:3776764",
    "domain": "股票",
    "title": "韩国券商一句业绩“不及预期”，SK海力士大跌12%，存储板块全线承压！",
    "url": "https://wallstreetcn.com/articles/3776764",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:02:44+00:00",
    "summary": "韩国券商KIS预测SK海力士Q2营业利润60.4万亿韩元，同比暴增556%，但低于市场共识65万亿韩元约8%。核心原因是HBM收入占比高、受长期合约价格约束，ASP涨幅低于市场均值。KIS同步下调2026、2027年盈利预期9%和11%，但维持380万韩元目标价，称下调仅是LTA修正非基本面恶化。"
  },
  {
    "id": "wscn:3776752",
    "domain": "股票",
    "title": "海峡\"罗生门\"推升加息押注，对冲基金黄金多头降至11.5万份",
    "url": "https://wallstreetcn.com/articles/3776752",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T03:59:04+00:00",
    "summary": "美伊冲突持续升级，霍尔木兹海峡通航陷入罗生门，油价走高重燃通胀警报，金价周一跌逾1%至4073美元，三年牛市已告终结、自高位累计回落超两成。加息预期卷土重来令贵金属承压，本周二美联储主席沃什国会首秀叠加6月CPI数据，将成决定金价短期走向的关键时刻。"
  },
  {
    "id": "wscn:3776765",
    "domain": "股票",
    "title": "对话《盛世天下》总制作人Demi：互动影视开始走出“新手村”",
    "url": "https://wallstreetcn.com/articles/3776765",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T03:46:31+00:00",
    "summary": "自己决定剧情走向"
  },
  {
    "id": "wscn:3776761",
    "domain": "股票",
    "title": "付鹏：深度解析AI产业链周期与2026下半年最重要的观察指标【付鹏说29】",
    "url": "https://wallstreetcn.com/premium/articles/3776761?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T03:40:08+00:00",
    "summary": "AI产业“修路式”上游算力资本支出周期已现增速见顶信号，科技大厂自由现金流归零可能结束粗放烧钱扩张阶段，当前产业正式从硬件生产力投入期，迈入依赖Token降价、真实终端需求落地的软件与垂直应用价值兑现期，产业链利润重心将持续向下游迁移"
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
    "points": 190,
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
    "points": 63,
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
    "points": 44,
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
    "id": "rss:https://arxiv.org/abs/2607.08849",
    "domain": "金融",
    "title": "Experimental Evidence on the Learning Impact of Generative AI",
    "url": "https://arxiv.org/abs/2607.08849",
    "source": "Zara Contractor, Germ\\'an Reyes",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.08849v1 Announce Type: new Abstract: We study how generative AI affects student learning in a randomized experiment. In proctored, in-person sessions, undergraduates learn about an unfamili"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.08907",
    "domain": "金融",
    "title": "Herding and Liquidity in Order-Book Markets. I. A Robust Liquidity-Stress Crossover and its Reflexive Mechanism",
    "url": "https://arxiv.org/abs/2607.08907",
    "source": "Jan Novotny",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.08907v1 Announce Type: new Abstract: Agent-based models of markets readily produce emergent instabilities, but telling a genuine collective effect apart from a parameter artefact takes disc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.08920",
    "domain": "金融",
    "title": "AI Adoption in S&P 500 Firms",
    "url": "https://arxiv.org/abs/2607.08920",
    "source": "Yang Yu, Martin Fleming, Lucy Hampton, Christophe Combemale, Neil Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.08920v1 Announce Type: new Abstract: The adoption of artificial intelligence (AI) by large enterprises is an important potential source of aggregate productivity improvement and labor marke"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09132",
    "domain": "金融",
    "title": "Distortion risk measures of step-weighted distribution",
    "url": "https://arxiv.org/abs/2607.09132",
    "source": "Chunle Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.09132v1 Announce Type: new Abstract: In this note, we study distortion risk measures of step-weighted distribution."
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09230",
    "domain": "金融",
    "title": "When Does Order Flow Matter? State-Dependent L2 Liquidity-State Transitions in Crypto Futures",
    "url": "https://arxiv.org/abs/2607.09230",
    "source": "Joohyoung Jeon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.09230v1 Announce Type: new Abstract: Building event-conditioned market models requires separating macro-event labels from persistent microstructure state. We study this distinction in Binan"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09355",
    "domain": "金融",
    "title": "Ever since Ellsberg",
    "url": "https://arxiv.org/abs/2607.09355",
    "source": "Aluma Dembo, Shachar Kariv, Matthew Polisson, John K. -H. Quah",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.09355v1 Announce Type: new Abstract: Ellsberg's famous paradox challenged Savage's subjective expected utility theory (EUT) -- which reduces uncertainty to risk -- by suggesting an aversion"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09426",
    "domain": "金融",
    "title": "The Quarter-Hour Effect: Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures",
    "url": "https://arxiv.org/abs/2607.09426",
    "source": "Chan Kim, Peter Reinhard Hansen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.09426v1 Announce Type: new Abstract: Cryptocurrency markets exhibit periodic bursts in volatility and volume at one-, five-, and quarter-hour marks. Using trade data for six Binance perpetu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09461",
    "domain": "金融",
    "title": "Deep Learning for Dynamic Programming with Recursive Utility Using First-order Conditions",
    "url": "https://arxiv.org/abs/2607.09461",
    "source": "Xianhua Peng, Wu Guo, Songyan Wang, Jianfei Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.09461v1 Announce Type: new Abstract: This paper proposes the certainty-equivalent first-order learning (CEFOL) algorithm, a deep learning algorithm for solving discrete-time dynamic program"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09505",
    "domain": "金融",
    "title": "Objective and subjective entropy measures of portfolio suboptimality",
    "url": "https://arxiv.org/abs/2607.09505",
    "source": "Ati S Sharma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.09505v1 Announce Type: new Abstract: The cost of holding a suboptimal portfolio instead of the Kelly-optimal one admits two exact relative-entropy representations. Under the true measure, t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09514",
    "domain": "金融",
    "title": "Does Regulation Bite at Gateways? Evidence from MiCA and Stablecoins",
    "url": "https://arxiv.org/abs/2607.09514",
    "source": "Nicola Borri, Kirill Shakhnov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.09514v1 Announce Type: new Abstract: Gateways are trading venues where regulation can change the assets investors can trade. We study this margin using MiCA-EU's Markets in Crypto-Assets Re"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09589",
    "domain": "金融",
    "title": "Regional Economic Impacts of the Just Energy Transition: Lessons for Coal Regions",
    "url": "https://arxiv.org/abs/2607.09589",
    "source": "Imke Rhoden, Jae-Hyuck Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.09589v1 Announce Type: new Abstract: The coal phase-out's regional economic impact is a key challenge of the energy transition, as employment and fiscal dependence in coal regions face stru"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.08681",
    "domain": "金融",
    "title": "SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets",
    "url": "https://arxiv.org/abs/2607.08681",
    "source": "Shilin Ou, Yifan Xu, Luyao Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.08681v1 Announce Type: cross Abstract: As agentic AI systems are increasingly applied to cyber-physical environments, their evaluation requires assessment of both task performance and trust"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09435",
    "domain": "金融",
    "title": "Voting Biases in Decentralized Autonomous Organization (DAO) Governance",
    "url": "https://arxiv.org/abs/2607.09435",
    "source": "Stefano Balietti, Pietro Saggese, Markus Strohmaier",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.09435v1 Announce Type: cross Abstract: Decentralized Autonomous Organizations (DAOs) use token-weighted voting to allocate resources, set protocol rules, and legitimate collective decisions"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09556",
    "domain": "金融",
    "title": "A novel robust mixed integer linear programming model for index tracking problem under no rebalancing: heuristic optimization approach",
    "url": "https://arxiv.org/abs/2607.09556",
    "source": "Danial Ramezani, Mostafa Abouei Ardakan, Mohamadreza Dehghani Ahmadabad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.09556v1 Announce Type: cross Abstract: Passive management has increasingly won popularity over the past few years because of its advantages, such as lower management fees and transaction co"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09566",
    "domain": "金融",
    "title": "Large-Scale Portfolio Optimization Problem Under Cardinality Constraint With Enhanced Multi-Objective Evolutionary Algorithms",
    "url": "https://arxiv.org/abs/2607.09566",
    "source": "Danial Ramezani, Mostafa Abouei Ardakan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.09566v1 Announce Type: cross Abstract: Decision-making is posing an increasingly formidable challenge to investors because of the growing number of alternatives available in financial marke"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.09568",
    "domain": "金融",
    "title": "Perturbed utility Markovian traffic equilibrium: theory and computation",
    "url": "https://arxiv.org/abs/2607.09568",
    "source": "Rui Yao, Kenan Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.09568v1 Announce Type: cross Abstract: Large-scale traffic assignment requires equilibrium models that are both behaviorally plausible and computationally tractable. This paper develops a p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.21019",
    "domain": "金融",
    "title": "Beyond Trade Openness: Network-Based Evidence on African Economic Integration",
    "url": "https://arxiv.org/abs/2410.21019",
    "source": "Tekilu Tadesse Choramo, Jemal Abafita, Yerali Gandica, Luis E C Rocha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2410.21019v2 Announce Type: replace Abstract: This paper develops a network-based methodology for measuring economic integration in Africa. Conventional indicators such as trade openness and int"
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.01365",
    "domain": "金融",
    "title": "Consumption Stimulus with Digital Coupons: Heterogeneity and Policy Design",
    "url": "https://arxiv.org/abs/2507.01365",
    "source": "Ying Chen, Mingyi Li, Jonathan J. Mao, Jingyi Zhou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2507.01365v3 Announce Type: replace Abstract: We study consumption stimulus using digital coupons, which provide time-limited subsidies contingent on minimum spending. Analyzing a large-scale pr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.09006",
    "domain": "金融",
    "title": "Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics",
    "url": "https://arxiv.org/abs/2603.09006",
    "source": "Anders G Fr{\\o}seth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2603.09006v3 Announce Type: replace Abstract: We develop spectral portfolio theory by establishing a direct identification: neural network weight matrices trained on stochastic processes are por"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05091",
    "domain": "金融",
    "title": "Any Axes Are Allowed: A Characteristic-Axis Integral Diagnostic of Factor Models",
    "url": "https://arxiv.org/abs/2607.05091",
    "source": "Useong Shin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.05091v4 Announce Type: replace Abstract: This paper extends the cap-axis integral diagnostic to general characteristic axes, measuring factor-model pricing errors as bridge-alpha curves. A "
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.16006",
    "domain": "金融",
    "title": "Heterogeneous Returns and Wealth Tax Neutrality: A Fokker-Planck Framework",
    "url": "https://arxiv.org/abs/2603.16006",
    "source": "Anders G Fr{\\o}seth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2603.16006v3 Announce Type: replace-cross Abstract: We extend the Fokker-Planck framework of Froseth (2026, arXiv:2603.05283) to populations of investors with heterogeneous, persistent return-ge"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.24190",
    "domain": "金融",
    "title": "Dynamical thermalization and turbulence in social stratification models",
    "url": "https://arxiv.org/abs/2603.24190",
    "source": "Klaus M. Frahm, Dima L. Shepelyansky",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2603.24190v2 Announce Type: replace-cross Abstract: We study the nonlinear chaotic dynamics in a system of linear oscillators coupled by social network links with an additional stratification of"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.03888",
    "domain": "金融",
    "title": "Local Gaussian Correlation in the Tails: A Scarcity Diagnostic, an Optimal Local Bandwidth, and the Limits of Adaptivity",
    "url": "https://arxiv.org/abs/2607.03888",
    "source": "Akash Deep, Gagan Deep",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-13T04:00:00+00:00",
    "summary": "arXiv:2607.03888v2 Announce Type: replace-cross Abstract: Local Gaussian correlation (LGC) measures dependence locally, making it a natural tool for tail dependence and financial contagion, but its es"
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
    "id": "hn:48849827",
    "domain": "金融",
    "title": "FrontierFinance: The largest open benchmark for investor workflows",
    "url": "https://research.samaya.ai/benchmarks/frontier-finance",
    "source": "ashwinpp",
    "platform": "hackernews",
    "points": 17,
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
  }
]
```
