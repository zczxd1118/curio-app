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

- 今日日期：`2026-08-08`
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
  "date": "2026-08-08",
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
    "points": 4141679,
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
    "points": 1677854,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1592464,
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
    "points": 1317025,
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
    "points": 1071397,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 1031233,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 1020714,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1khMX63EjU",
    "domain": "AI",
    "title": "Vibe Coding竞赛，Claude遗憾落败?",
    "url": "http://www.bilibili.com/video/av117030980230736",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 698173,
    "published_at": "2026-08-05T10:30:00+00:00",
    "summary": "我和源宝打了个赌：半天时间，vibe coding一个活动社交App，看谁做的更好？最后Claude Code居然遗憾落败？这期视频，我们将用秒哒手把手带你走完，从一个简单的想法到App上架应用商店的全套流程！开发过程又发生了哪些趣事？一起来看看～"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 602051,
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
    "points": 567438,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 509351,
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
    "points": 440096,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 434885,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 419790,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 351272,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 259277,
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
    "points": 227319,
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
    "points": 217880,
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
    "points": 178707,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV172GP6rEZs",
    "domain": "AI",
    "title": "🚀DeepSeek V4 Flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！",
    "url": "http://www.bilibili.com/video/av117014605731815",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 172208,
    "published_at": "2026-07-31T12:42:57+00:00",
    "summary": "🚀DeepSeek v4 flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！性能、速度与真实短板全曝光！对比Kimi K3后优点和缺点都藏不住了\n\nDeepSeek 发布了 DeepSeek V4 Flash 0731：284B 总参数、13B 激活参数、100 万 Token 上下文，官方基准表现接近 Claude"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 160714,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 143946,
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
    "points": 122886,
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
    "points": 93049,
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
    "points": 90456,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 77283,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 74046,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 63981,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53758,
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
    "points": 45563,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 41385,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 40099,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34052,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 31569,
    "published_at": "2026-05-07T00:00:00+00:00",
    "summary": "全栈课一共分为6大块内容\n第一块：AI智能体开发基础(AI大模型、工具、记忆、MCP、中间件、Skills等核心内容)\n第二块：Claude Code,Trea+skills实现基于需求文档生成用例，基于OpenClaw实现接口自动化落地，基于hermes Agent实现web自动化落地\n第三块：功能测试的智能体开发(项目RAG知识库搭建+Agent搭建+skills开发，实现用例生成的Agent"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29566,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28852,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1YJ336EEBk",
    "domain": "AI",
    "title": "【AI陪玩】开袋即食的AI接入我的世界教程！",
    "url": "http://www.bilibili.com/video/av116981806143216",
    "source": "万昇Dwin",
    "platform": "bilibili",
    "points": 23752,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "模组：Numen\n项目地址：https://github.com/Dwinovo/minecraft-numen"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22691,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1dsNv66E3Q",
    "domain": "AI",
    "title": "【Cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116922599344955",
    "source": "六月要癫",
    "platform": "bilibili",
    "points": 20086,
    "published_at": "2026-07-15T06:39:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 19940,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1gf3T6KEef",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！从环境搭建到工作流完整闭环，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116979708990688",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 19220,
    "published_at": "2026-07-25T08:47:37+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 18363,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17680,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1hnjGzLE14",
    "domain": "AI",
    "title": "【小智教程】手挽手教你如何接入别人的MCP服务",
    "url": "http://www.bilibili.com/video/av114568722450105",
    "source": "空白泡泡糖果",
    "platform": "bilibili",
    "points": 17654,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 14947,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 14384,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1DPwGe1Ekf",
    "domain": "AI",
    "title": "Cursor从小白到专家-第15课：如何用Cursor+Dify搭建本地知识库？",
    "url": "http://www.bilibili.com/video/av113836698898908",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 14314,
    "published_at": "2025-01-16T08:55:00+00:00",
    "summary": "在第九课“如何用 cursor + coze 搭建线上知识库”的分享后，有一部分精神股东表示，想要本地知识库的搭建教程。\n.\n有求必应，今天第15课的分享就是“用 cursor + dify 搭建本地知识库”，手把手教会。我们第16课见 ~"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9304,
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
    "points": 8895,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV14uTM69EUd",
    "domain": "AI",
    "title": "破甲claude/减少claude道德约束/ai破解卡密",
    "url": "http://www.bilibili.com/video/av116826918880943",
    "source": "去码头整点海鸥啊",
    "platform": "bilibili",
    "points": 8538,
    "published_at": "2026-06-28T09:05:03+00:00",
    "summary": "企鹅交流群：1038830654"
  },
  {
    "id": "hn:49189234",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia’s Vera Whitepaper Has a Thread Loose",
    "url": "https://chipsandcheese.com/p/nvidias-vera-whitepaper-has-a-thread",
    "source": "pella",
    "platform": "hackernews",
    "points": 206,
    "published_at": "2026-08-05T21:24:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49122838",
    "domain": "AI 算力 / 半导体",
    "title": "Moonshot’s Kimi uses 20k Nvidia chip cluster from Alibaba",
    "url": "https://www.bloomberg.com/news/articles/2026-07-31/moonshot-s-kimi-built-on-20-000-nvidia-chip-cluster-from-alibaba",
    "source": "gk1",
    "platform": "hackernews",
    "points": 114,
    "published_at": "2026-07-31T13:24:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49071512",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's $750B in Deals Reignite Circular AI Fears",
    "url": "https://www.bloomberg.com/news/articles/2026-07-27/nvidia-s-750-billion-deals-revive-fear-of-ai-circular-financing",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-07-27T16:02:00+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/after-seven-ceos-in-10-years-imagination-is-sticking-to-its-strategy/",
    "domain": "AI 算力 / 半导体",
    "title": "After Seven CEOs in 10 Years, Imagination Is Sticking to Its Strategy",
    "url": "https://www.eetimes.com/after-seven-ceos-in-10-years-imagination-is-sticking-to-its-strategy/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T22:00:00+00:00",
    "summary": "Imagination dumps CPU/NPU dreams, doubles down on GPUs and China under CEO No. 7. The post After Seven CEOs in 10 Years, Imagination Is Sticking to Its Strategy appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/rolecs-technoplus-ip-rated-pole-mount-plastic-enclosures-for-iot-iiot-and-factory-automation/",
    "domain": "AI 算力 / 半导体",
    "title": "ROLEC’s technoPLUS: IP-rated Pole-mount Plastic Enclosures for IoT/IIoT and Factory Automation",
    "url": "https://www.eetimes.com/rolecs-technoplus-ip-rated-pole-mount-plastic-enclosures-for-iot-iiot-and-factory-automation/",
    "source": "ROLEC",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T16:15:30+00:00",
    "summary": "IoT/IIoT and factory automation are driving demand for ROLEC’s updated pole-mountable technoPLUS (IP 66, IP 67, IP 69K) plastic enclosures. Electronics designers specify them for ‘close-to-the-process"
  },
  {
    "id": "rss:https://www.eetimes.com/biwin-and-tera-industria-de-semicondutores-sign-strategic-partnership-agreement/",
    "domain": "AI 算力 / 半导体",
    "title": "BIWIN and Tera Indústria de Semicondutores Sign Strategic Partnership Agreement",
    "url": "https://www.eetimes.com/biwin-and-tera-industria-de-semicondutores-sign-strategic-partnership-agreement/",
    "source": "BIWIN Semiconductor",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T16:08:31+00:00",
    "summary": "Shenzhen, China / Manaus, Brazil – August 6th, 2026: BIWIN Semiconductor (HK) Company Limited (&#8220;BIWIN&#8221;), a global provider of memory and storage packaging solutions, and TERA INDÚSTRIA DE "
  },
  {
    "id": "rss:https://www.eetimes.com/chiplet-architectures-as-a-practical-path-to-scalable-automotive-compute/",
    "domain": "AI 算力 / 半导体",
    "title": "Chiplet Architectures as a Practical Path to Scalable Automotive Compute",
    "url": "https://www.eetimes.com/chiplet-architectures-as-a-practical-path-to-scalable-automotive-compute/",
    "source": "Cyril Cordoba",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T13:56:43+00:00",
    "summary": "Chiplets are auto’s escape hatch from bloated SoCs, scaling SDV compute without wrecking cost or software. The post Chiplet Architectures as a Practical Path to Scalable Automotive Compute appeared fi"
  },
  {
    "id": "rss:https://www.eetimes.com/inside-device-connectivity-a-new-design-discipline-for-next-gen-vehicles/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside Device Connectivity: A New Design Discipline for Next-Gen Vehicles",
    "url": "https://www.eetimes.com/inside-device-connectivity-a-new-design-discipline-for-next-gen-vehicles/",
    "source": "TE Connectivity",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T10:53:14+00:00",
    "summary": "Join this webinar where our expert will introduce Inside Device Connectivity as a focused design discipline to ensure power, signal, and data move predictably and robustly within automotive electronic"
  },
  {
    "id": "rss:https://www.eetimes.com/stmicroelectronics-bets-on-hardware-based-post-quantum-cryptography-with-st54m/",
    "domain": "AI 算力 / 半导体",
    "title": "STMicroelectronics Bets on Hardware-Based Post-Quantum Cryptography with ST54M",
    "url": "https://www.eetimes.com/stmicroelectronics-bets-on-hardware-based-post-quantum-cryptography-with-st54m/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T08:00:00+00:00",
    "summary": "ST’s ST54M bakes post-quantum crypto into phone hardware before hackers harvest today’s secrets. The post STMicroelectronics Bets on Hardware-Based Post-Quantum Cryptography with ST54M appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/ai-chip-startup-taalas-acquired-by-amd/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Chip Startup Taalas Acquired by AMD",
    "url": "https://www.eetimes.com/ai-chip-startup-taalas-acquired-by-amd/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T20:05:00+00:00",
    "summary": "AMD plans to use Taalas chips alongside its GPUs for AI inference, likely as an LLM decode accelerator. The post AI Chip Startup Taalas Acquired by AMD appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/globalfoundries-growth-makes-the-case-for-a-u-s-photonics-buildout/",
    "domain": "AI 算力 / 半导体",
    "title": "GlobalFoundries’ Growth Makes the Case for a U.S. Photonics Buildout",
    "url": "https://www.eetimes.com/globalfoundries-growth-makes-the-case-for-a-u-s-photonics-buildout/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T16:17:00+00:00",
    "summary": "GlobalFoundries’ data center surge turns U.S. photonics from subsidy pitch to AI bottleneck bet. The post GlobalFoundries’ Growth Makes the Case for a U.S. Photonics Buildout appeared first on EE Time"
  },
  {
    "id": "rss:https://www.eetimes.com/u-s-manufacturing-activity-hits-four-year-high-in-july/",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Manufacturing Activity Hits Four-Year High in July",
    "url": "https://www.eetimes.com/u-s-manufacturing-activity-hits-four-year-high-in-july/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T12:31:16+00:00",
    "summary": "In July, U.S. manufacturing activity remained in expansion territory, growing at its fastest pace in more than four years. The post U.S. Manufacturing Activity Hits Four-Year High in July appeared fir"
  },
  {
    "id": "rss:https://www.eetimes.com/beyond-the-fab-building-europe-next-generation-of-semiconductor-champions/",
    "domain": "AI 算力 / 半导体",
    "title": "Beyond the Fab: Building Europe’s Next Generation of Semiconductor Champions",
    "url": "https://www.eetimes.com/beyond-the-fab-building-europe-next-generation-of-semiconductor-champions/",
    "source": "Ian Lankshear",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T08:09:11+00:00",
    "summary": "Europe's next semiconductor champions will emerge from design expertise, customer knowledge, and IP—not manufacturing capacity alone. The post Beyond the Fab: Building Europe&#8217;s Next Generation o"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/scientist-says-ram-pricing-has-reverted-to-normalized-2007-levels-memory-prices-have-been-falling-exponentially-for-decades-but-the-ai-shortage-undid-20-years-of-progress-in-a-matter-of-months",
    "domain": "AI 算力 / 半导体",
    "title": "Scientist says RAM pricing has risen to normalized 2007 levels, AI shortage undid 20 years of progress in a matter of months — memory prices had been falling exponentially for decades",
    "url": "https://www.tomshardware.com/pc-components/ram/scientist-says-ram-pricing-has-reverted-to-normalized-2007-levels-memory-prices-have-been-falling-exponentially-for-decades-but-the-ai-shortage-undid-20-years-of-progress-in-a-matter-of-months",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T16:58:22+00:00",
    "summary": "The per GB price of memory modules have gone back to 2007 levels because of AI demand. This is the first time that prices have shot up in the realm of tech, Lemire says."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amazon-cracks-down-on-cpu-waste-among-engineers-as-agentic-ai-crunch-intensifies-cpu-demand-makes-low-utilization-ec2-instances-a-hot-commodity",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon cracks down on 'CPU waste' among engineers as agentic AI crunch intensifies — CPU demand makes low-utilization EC2 instances a hot commodity [Updated]",
    "url": "https://www.tomshardware.com/pc-components/cpus/amazon-cracks-down-on-cpu-waste-among-engineers-as-agentic-ai-crunch-intensifies-cpu-demand-makes-low-utilization-ec2-instances-a-hot-commodity",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T15:49:52+00:00",
    "summary": "Amazon Web Services is telling engineers to slow down on EC2 usage as it struggles to meet CPU capacity demand for external customers."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/protesters-haul-a-guillotine-to-city-council-meeting-about-a-potential-ai-data-center-company-rep-cornered-by-protestors-it-no-longer-felt-safe-to-stay-developer-escorted-out-by-police",
    "domain": "AI 算力 / 半导体",
    "title": "Protesters haul a guillotine to city council meeting about a potential AI data center, company rep cornered by protestors — ‘ it no longer felt safe to stay,’ developer escorted out by police",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/protesters-haul-a-guillotine-to-city-council-meeting-about-a-potential-ai-data-center-company-rep-cornered-by-protestors-it-no-longer-felt-safe-to-stay-developer-escorted-out-by-police",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T14:32:26+00:00",
    "summary": "Some protesters brought a guillotine to public consultation for a potential data center in Salem, Oregon. Even though this was displayed outside the venue, it was a confrontation between the data cent"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-august-7-2026-inside-chinas-lithography-efforts-co-packaged-optics-get-a-spotlight-and-samsung-debuts-next-gen-memory-tech",
    "domain": "AI 算力 / 半导体",
    "title": "This week on Tom's Hardware Premium: August 7, 2026 — Inside China's lithography efforts, co-packaged optics get a spotlight, and Samsung debuts next-gen memory tech",
    "url": "https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-august-7-2026-inside-chinas-lithography-efforts-co-packaged-optics-get-a-spotlight-and-samsung-debuts-next-gen-memory-tech",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T13:44:37+00:00",
    "summary": "A redesigned Bench tool, inside China's domestic Chipmaking efforts, breaking, and we offer a free technical breakdown of Samsung's latest memory-related announcements."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/grab-an-entire-rtx-5090-pc-for-just-usd380-more-than-the-standalone-graphics-card-save-usd1-550-off-alienwares-area-51-gaming-rig",
    "domain": "AI 算力 / 半导体",
    "title": "Grab an entire RTX 5090 PC for just $380 more than the standalone graphics card — save $1,550 off Alienware's Area-51 gaming rig",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/grab-an-entire-rtx-5090-pc-for-just-usd380-more-than-the-standalone-graphics-card-save-usd1-550-off-alienwares-area-51-gaming-rig",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T13:38:40+00:00",
    "summary": "Pick up an entire Alienware RTX 5090 gaming PC for just $380 more than the RTX 5090 GPU bought separately."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/introducing-bench-2-0-a-revamped-benchmark-analyzer-exclusively-for-toms-hardware-premium-subscribers",
    "domain": "AI 算力 / 半导体",
    "title": "Introducing Bench 2.0 — a revamped benchmark analyzer, exclusively for Tom's Hardware Premium subscribers",
    "url": "https://www.tomshardware.com/pc-components/introducing-bench-2-0-a-revamped-benchmark-analyzer-exclusively-for-toms-hardware-premium-subscribers",
    "source": "Jeremy Kaplan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T13:27:12+00:00",
    "summary": "We’re pleased to introduce Bench 2.0, a ground-up rethink of our benchmarking tool that makes it the most powerful, most intuitive benchmark browser in the business. Bench 2.0 has tons of new features"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/hyperx-omen-max-16-review",
    "domain": "AI 算力 / 半导体",
    "title": "HyperX Omen Max 16 review: All bark and no bite",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/hyperx-omen-max-16-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T12:05:00+00:00",
    "summary": "The Omen Max 16 definitely looks like a desktop replacement gaming laptop, but its gaming performance meows instead of roars."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/apple-revealed-the-first-mac-pro-20-years-ago-today-its-intel-xeon-powered-flagship-desktop-took-the-reins-from-the-power-mac-g5",
    "domain": "AI 算力 / 半导体",
    "title": "Apple revealed the first Mac Pro 20 years ago today — its Intel Xeon-powered flagship desktop took the reins from the Power Mac G5",
    "url": "https://www.tomshardware.com/desktops/apple-revealed-the-first-mac-pro-20-years-ago-today-its-intel-xeon-powered-flagship-desktop-took-the-reins-from-the-power-mac-g5",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T11:58:46+00:00",
    "summary": "20 years ago today Steve Jobs took to the Apple WWDC stage to unveil the first-ever Mac Pro desktop computer. This is when Mac workstations transitioned from PowerPC to Intel Xeon chips."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-sells-rtx-50-series-gpus-at-msrp-during-quakecon-2026-graphics-cards-sold-at-launch-prices-more-than-a-year-after-release-are-now-considered-an-attraction",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia sells RTX 50-series GPUs at MSRP during QuakeCon 2026 — graphics cards sold at launch prices more than a year after release are now considered an attraction",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-sells-rtx-50-series-gpus-at-msrp-during-quakecon-2026-graphics-cards-sold-at-launch-prices-more-than-a-year-after-release-are-now-considered-an-attraction",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T11:11:49+00:00",
    "summary": "The Nvidia booth at QuakeCon 2026 is offering Founders Edition GeForce RTX 5090, 5080, and 5070 GPUs at MSRP. Supplies are limited, though, so you should head out ASAP if you want to snag one right no"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/msis-magnificent-32-inch-4k-oled-gaming-monitor-returns-to-its-lowest-ever-price-of-usd599-save-usd130-on-the-mag-321upxb-the-perfect-240hz-upgrade",
    "domain": "AI 算力 / 半导体",
    "title": "MSI's magnificent 32-inch 4K OLED gaming monitor returns to its lowest-ever price of $599 — save $130 on the MAG 321UPXB, the perfect 240Hz upgrade",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/msis-magnificent-32-inch-4k-oled-gaming-monitor-returns-to-its-lowest-ever-price-of-usd599-save-usd130-on-the-mag-321upxb-the-perfect-240hz-upgrade",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T11:02:38+00:00",
    "summary": "Save $130 on this gorgeous 32-inch QD-OLED gaming monitor from MSI and experience crisp visuals in 4K."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/terafab-starts-to-take-shape-100-million-square-feet-of-manufacturing-space-and-usd16-8b-initial-capital-investment",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk's massive Terafab chip-making facility starts to take shape — 100 million square feet of manufacturing space and $16.8B initial capital investment",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/terafab-starts-to-take-shape-100-million-square-feet-of-manufacturing-space-and-usd16-8b-initial-capital-investment",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T11:00:00+00:00",
    "summary": "SpaceX and Tesla officially begin to build the massive Terafab facility that will be three times bigger than Samsung's Pyeongtaek campus."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd370-on-this-1440p-gaming-pc-with-an-rtx-5060-ti-16gb-formidable-abs-cyclone-aqua-rig-ships-with-20-core-intel-core-i7-14700f-16gb-ddr5-and-a-1tb-ssd-now-only-usd1-329-99",
    "domain": "AI 算力 / 半导体",
    "title": "Save $370 on this 1440p gaming PC with an RTX 5060 Ti 16GB — formidable ABS Cyclone Aqua rig ships with 20-core Intel Core i7-14700F, 16GB DDR5 and a 1TB SSD, now only $1,329.99",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd370-on-this-1440p-gaming-pc-with-an-rtx-5060-ti-16gb-formidable-abs-cyclone-aqua-rig-ships-with-20-core-intel-core-i7-14700f-16gb-ddr5-and-a-1tb-ssd-now-only-usd1-329-99",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T10:42:00+00:00",
    "summary": "Save $300 on this Newegg-made ABS Cyclone Aqua gaming PC, featuring an RTX 5060 Ti 16GB, Intel Core i7-14700F, 16GB DDR5, and a 1TB SSD for $1,399.99 right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/anthropic-to-build-its-own-co-designed-custom-ai-accelerator-for-inferencing-workloads-samsung-reported-to-be-partnering-with-the-claude-ai-maker-for-manufacturing",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic co-designing custom AI inference chips to bypass costly Nvidia GPUs — Samsung reported as manufacturing partner for Claude maker",
    "url": "https://www.tomshardware.com/tech-industry/anthropic-to-build-its-own-co-designed-custom-ai-accelerator-for-inferencing-workloads-samsung-reported-to-be-partnering-with-the-claude-ai-maker-for-manufacturing",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T10:30:00+00:00",
    "summary": "Anthropic has announced its building a team to co-design custom ASIC chips for AI inferencing workloads. This will give it greater control over its compute buildout and allow it to make its AI models "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-opus-5-mistakenly-deletes-devs-entire-profile-directory-ai-tool-mistakes-users-home-directory-as-temporary-backup-proceeds-to-wipe-everything-to-undo-error",
    "domain": "AI 算力 / 半导体",
    "title": "Claude Opus 5 mistakenly deletes dev’s entire profile directory during routine backup, responds with 'Sorry, typo' — AI tool mistakes user's home directory as temporary backup, proceeds to wipe everyt",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-opus-5-mistakenly-deletes-devs-entire-profile-directory-ai-tool-mistakes-users-home-directory-as-temporary-backup-proceeds-to-wipe-everything-to-undo-error",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T10:00:00+00:00",
    "summary": "An AI agent got confused with file path conventions and mistakenly deleted its user's entire profile folder. Claude Opus 5 apologized to the user, who called it \"the funniest and most painful AI momen"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/pre-modded-rtx-2080-ti-cards-with-22gb-of-vram-surface-on-ebay-for-usd500-hong-kong-based-seller-offers-ai-friendly-memory-mod-for-a-reasonable-price",
    "domain": "AI 算力 / 半导体",
    "title": "Pre-modded 22GB RTX 2080 Ti cards surface on eBay for $500 as VRAM-hungry local AI fans chase down every spare FLOP — Hong Kong-based seller offers AI-friendly memory mod for a reasonable price",
    "url": "https://www.tomshardware.com/pc-components/gpus/pre-modded-rtx-2080-ti-cards-with-22gb-of-vram-surface-on-ebay-for-usd500-hong-kong-based-seller-offers-ai-friendly-memory-mod-for-a-reasonable-price",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T16:11:19+00:00",
    "summary": "Services have recently popped up that will double your RTX 2080 Ti's memory to 22GB, but if you don't have a card to spare, you can now get a pre-modded 22 GB 2080 Ti for $499 from eBay."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/after-severe-76-percent-electricity-price-hikes-due-to-ai-data-centers-virginia-requires-firms-to-pay-for-all-dedicated-upstream-electrical-infrastructure-state-regulators-crack-down-governor-says-move-will-save-civilians-hundreds-of-millions-of-dollars",
    "domain": "AI 算力 / 半导体",
    "title": "After severe 76% electricity price hikes due to AI data centers, Virginia requires firms to pay for all dedicated upstream electrical infrastructure — state regulators crack down, governor says move w",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/after-severe-76-percent-electricity-price-hikes-due-to-ai-data-centers-virginia-requires-firms-to-pay-for-all-dedicated-upstream-electrical-infrastructure-state-regulators-crack-down-governor-says-move-will-save-civilians-hundreds-of-millions-of-dollars",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T15:32:08+00:00",
    "summary": "Virginia's public utility regulator now requires all data center projects to pay for the infrastructure needed to supply their power. This makes it one of the first states to convert the 'ratepayer pr"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/usd1-billion-of-iphone-18-pro-chips-on-the-shelves-awaiting-packaging-due-to-dram-shortages-memory-shortages-reportedly-put-a-wrinkle-in-apples-launch-plans",
    "domain": "AI 算力 / 半导体",
    "title": "$1 billion of iPhone 18 Pro chips 'on the shelves awaiting packaging' due to DRAM shortages — memory shortages reportedly put a wrinkle in Apple's launch plans",
    "url": "https://www.tomshardware.com/pc-components/dram/usd1-billion-of-iphone-18-pro-chips-on-the-shelves-awaiting-packaging-due-to-dram-shortages-memory-shortages-reportedly-put-a-wrinkle-in-apples-launch-plans",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T14:52:11+00:00",
    "summary": "Apple reportedly as $1 billion worth of iPhone 18 processor wafers awaiting packaging, which hasn't been completed due to DRAM shortages."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/nashville-attempts-to-block-controversial-data-center-near-zoo-with-eminent-domain-city-could-force-developer-to-sell-the-land-for-public-use-rather-than-usd700-million-installation",
    "domain": "AI 算力 / 半导体",
    "title": "Nashville attempts to block controversial data center near zoo with eminent domain — city could force developer to sell the land for public use, rather than $700 million installation",
    "url": "https://www.tomshardware.com/tech-industry/policy/nashville-attempts-to-block-controversial-data-center-near-zoo-with-eminent-domain-city-could-force-developer-to-sell-the-land-for-public-use-rather-than-usd700-million-installation",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T13:26:17+00:00",
    "summary": "The Nashville Metro Council just gave the go ahead for the mayor's plan to buy the land that a proposed data center will sit on through eminent domain. This will force the developer to give up the lan"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/samsung-debuts-three-next-generation-memory-technologies-for-ai-data-centers-zhbm-znand-o-and-bv-nand-all-rely-on-advanced-wafer-bonding-technologies",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung debuts three next-generation memory technologies for AI data centers — zHBM, zNAND-O, and BV-NAND all rely on advanced wafer bonding technologies",
    "url": "https://www.tomshardware.com/pc-components/dram/samsung-debuts-three-next-generation-memory-technologies-for-ai-data-centers-zhbm-znand-o-and-bv-nand-all-rely-on-advanced-wafer-bonding-technologies",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T13:11:09+00:00",
    "summary": "Samsung uses FMS to unveil three next-generation memory technologies — zHBM, zNAND-O, and BV-NAND — that target different markets, but all rely on advanced wafer-bonding techniques."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/pc-gamer-vibe-codes-a-safeguard-against-rtx-5090-power-connector-failures-monitors-per-pin-power-draw-shuts-down-system-if-it-exceeds-9-5a-for-more-than-15-seconds",
    "domain": "AI 算力 / 半导体",
    "title": "PC gamer vibe-codes a safeguard against RTX 5090 power connector failures — monitors per-pin power draw, shuts down system if it exceeds 9.5A for more than 15 seconds",
    "url": "https://www.tomshardware.com/pc-components/gpus/pc-gamer-vibe-codes-a-safeguard-against-rtx-5090-power-connector-failures-monitors-per-pin-power-draw-shuts-down-system-if-it-exceeds-9-5a-for-more-than-15-seconds",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T12:33:49+00:00",
    "summary": "The 35MB application forcibly shuts the machine down if power exceeds configurable limits for too long."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/sandisk-optimus-gx-7100m-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "Sandisk Optimus GX 7100M 2TB SSD review: The best 2230 drive you can buy for the Steam Deck",
    "url": "https://www.tomshardware.com/pc-components/ssds/sandisk-optimus-gx-7100m-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T12:05:00+00:00",
    "summary": "The Sandisk Optimus GX 7100M is the pinnacle of M.2 2230 SSD goodness. High performance, great power efficiency, and a well-supported drive up to 2TB."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/apple-is-taking-openai-to-court-over-alleged-theft-of-trade-secrets-chatgpt-maker-suggests-it-doesnt-want-cupertinos-knowledge-anyway",
    "domain": "AI 算力 / 半导体",
    "title": "Apple is taking OpenAI to court over alleged theft of trade secrets — ChatGPT maker suggests it doesn't want Cupertino's knowledge anyway",
    "url": "https://www.tomshardware.com/tech-industry/apple-is-taking-openai-to-court-over-alleged-theft-of-trade-secrets-chatgpt-maker-suggests-it-doesnt-want-cupertinos-knowledge-anyway",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T11:25:02+00:00",
    "summary": "Two of the world's largest companies are heading to court over claims of trade secret theft. Apple alleges ex-employees took key Apple secrets and technologies to OpenAI. In responding, OpenAI claims "
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/beelink-ser10-max-mini-pc-review",
    "domain": "AI 算力 / 半导体",
    "title": "Beelink SER10 Max Mini PC review: Gorgon Point comes ready to dual-boot Windows and Ubuntu",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/beelink-ser10-max-mini-pc-review",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T11:05:00+00:00",
    "summary": "Beelink’s SER10 Max Mini PC comes ready to dual-boot Windows 11 and Ubuntu with OpenClaw pre-installed."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/usd200-slashed-off-gigabytes-4th-gen-woled-gaming-monitor-280hz-beast-also-packs-a-kvm-and-tactical-gaming-switch-for-just-usd399",
    "domain": "AI 算力 / 半导体",
    "title": "$200 slashed off Gigabyte's 4th-Gen WOLED gaming monitor — 280Hz beast also packs a KVM and tactical gaming switch for just $399",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/usd200-slashed-off-gigabytes-4th-gen-woled-gaming-monitor-280hz-beast-also-packs-a-kvm-and-tactical-gaming-switch-for-just-usd399",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T10:54:42+00:00",
    "summary": "Save $200 on this gorgeous 27-inch WOLED gaming monitor from Gigabyte, and upgrade your gaming experience for less."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd1-400-on-this-rtx-5090-gaming-pc-from-hp-with-64gb-ddr5-right-now-ram-and-gpu-cost-usd5k-alone-usd5-599-sale-price-for-top-spec-omen-max-45l-rig-with-24-core-intel-cpu-and-2tb-of-ssd-storage",
    "domain": "AI 算力 / 半导体",
    "title": "Save $1,400 on this RTX 5090 gaming PC from HP with 64GB DDR5 right now; RAM and GPU cost $5k alone — $5,599 sale price for top-spec Omen Max 45L rig with 24-core Intel CPU and 2TB of SSD storage",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd1-400-on-this-rtx-5090-gaming-pc-from-hp-with-64gb-ddr5-right-now-ram-and-gpu-cost-usd5k-alone-usd5-599-sale-price-for-top-spec-omen-max-45l-rig-with-24-core-intel-cpu-and-2tb-of-ssd-storage",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T10:50:15+00:00",
    "summary": "You can save $1,400 right now on this Omen Max gaming PC, fitted with an RTX 5090, 64GB RAM, and 2TB SSD storage, and on sale for $5,599.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/vpn-provider-windscribe-has-built-a-script-to-block-microsofts-persistent-gdid-tracking-on-windows-degdid-erases-existing-identifiers-and-blocks-new-ones-from-being-created",
    "domain": "AI 算力 / 半导体",
    "title": "VPN provider built a script to block Microsoft's hidden GDID tracking on Windows — Windscribe's \"deGDID\" erases existing identifiers and blocks new ones from being created",
    "url": "https://www.tomshardware.com/software/windows/vpn-provider-windscribe-has-built-a-script-to-block-microsofts-persistent-gdid-tracking-on-windows-degdid-erases-existing-identifiers-and-blocks-new-ones-from-being-created",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T10:30:00+00:00",
    "summary": "You can run the deGDID script on your computer to delete cached GDID keys and prevent Microsoft's servers from minting new ones in the background. The firewall you put up with this script will break c"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/rogue-openai-models-behind-unprecedented-cybersecurity-incident-teamed-up-to-break-out-of-their-testing-environment-multiple-agents-left-each-other-messages-for-months-communicating-undetected",
    "domain": "AI 算力 / 半导体",
    "title": "Rogue OpenAI models behind 'unprecedented cybersecurity incident' teamed up to break out of their testing environment — multiple agents left each other messages for months, communicating undetected",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/rogue-openai-models-behind-unprecedented-cybersecurity-incident-teamed-up-to-break-out-of-their-testing-environment-multiple-agents-left-each-other-messages-for-months-communicating-undetected",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T10:19:25+00:00",
    "summary": "The rogue OpenAI models that broke out of their testing environment in an \"unprecedented cybersecurity incident\" recently reportedly spent months communicating with each other."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/kentucky-family-snubs-usd26-million-offer-from-ai-company-to-convert-their-farmland-into-a-data-center-they-call-us-old-stupid-farmers-you-know-but-were-not-says-landowner",
    "domain": "AI 算力 / 半导体",
    "title": "Kentucky family snubs $26 million offer to convert their farmland into an AI data center — 'they call us old stupid farmers, you know, but we’re not,' says landowner",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/kentucky-family-snubs-usd26-million-offer-from-ai-company-to-convert-their-farmland-into-a-data-center-they-call-us-old-stupid-farmers-you-know-but-were-not-says-landowner",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T10:00:00+00:00",
    "summary": "A Northern Kentucky family has refused an anonymous AI company's $26 million offer to buy their land and transform it into a data center."
  },
  {
    "id": "hn:49177126",
    "domain": "AI 算力 / 半导体",
    "title": "It looks like 'Big Short' investor Michael Burry nailed bet against chip stocks",
    "url": "https://www.businessinsider.com/big-short-michael-burry-ai-chip-stocks-soxx-nvidia-substack-2026-8",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-05T00:30:23+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/xbox/microsoft-wants-the-next-gen-xbox-helix-to-play-every-xbox-game-ever-made-as-it-urges-publishers-to-opt-in-new-report-also-claims-xbox-360-games-coming-to-pc-soon",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft wants the next-gen Xbox Helix to play every Xbox game ever made as it urges publishers to opt in — New report also claims Xbox 360 games coming to PC soon",
    "url": "https://www.tomshardware.com/video-games/xbox/microsoft-wants-the-next-gen-xbox-helix-to-play-every-xbox-game-ever-made-as-it-urges-publishers-to-opt-in-new-report-also-claims-xbox-360-games-coming-to-pc-soon",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T14:51:31+00:00",
    "summary": "The upcoming Xbox Helix is starting to feel more like a PC than any console before, and Microsoft's latest efforts to unite all Xbox generations under one roof, according to a new leaked memo, seem to"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/usd4-429-order-for-a-rog-astral-rtx-5090-cancelled-by-nvidia-due-to-a-late-price-increase-with-asus-blamed-marketplace-buyer-refunded-after-immediate-usd500-increase-with-top-spec-gpu-now-almost-2-5x-higher-than-msrp",
    "domain": "AI 算力 / 半导体",
    "title": "$4,429 order for a ROG Astral RTX 5090 cancelled by Nvidia due to a 'late' price increase, with Asus blamed — marketplace buyer refunded after immediate $500 increase, with top-spec GPU now almost 2.5",
    "url": "https://www.tomshardware.com/pc-components/gpus/usd4-429-order-for-a-rog-astral-rtx-5090-cancelled-by-nvidia-due-to-a-late-price-increase-with-asus-blamed-marketplace-buyer-refunded-after-immediate-usd500-increase-with-top-spec-gpu-now-almost-2-5x-higher-than-msrp",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-05T14:48:13+00:00",
    "summary": "Nvidia cancelled a Redditor's Asus ROG Astral RTX 5090 BTF GPU order, originally priced at $4,429, because of a $500 price rise, with Nvidia blaming Asus for the confusion."
  },
  {
    "id": "hn:49125140",
    "domain": "AI 算力 / 半导体",
    "title": "Hygon Reveals 512-Thread CPU and AI GPU to Rival Intel Xeon and Nvidia",
    "url": "https://www.ubergizmo.com/2026/06/hygon-512-thread-cpu/",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-31T16:21:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:49084371",
    "domain": "AI 算力 / 半导体",
    "title": "Show HN: Tines 3B – safe workflow automation for when everyone builds software",
    "url": "https://www.tines.com/",
    "source": "retsol",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-07-28T14:23:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49070311",
    "domain": "AI 算力 / 半导体",
    "title": "Ilya Sutskever's SSI and Nvidia Announce Long-Term Strategic Partnership",
    "url": "https://nvidianews.nvidia.com/news/ilya-sutskevers-safe-superintelligence-inc-and-nvidia-announce-long-term-strategic-partnership",
    "source": "lanakei",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-27T14:33:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:49093429",
    "domain": "AI 算力 / 半导体",
    "title": "Kospi Plunges After Nvidia CEO's Visits Spark 'Huang Curse' Fears",
    "url": "https://www.chosun.com/english/market-money-en/2026/07/29/6FEUZWQT5BG3HMJ3G2RZPHROGM/",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-29T04:29:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49075171",
    "domain": "AI 算力 / 半导体",
    "title": "Sam Altman says we are in the singularity: 'This is the moment'",
    "url": "https://www.businessinsider.com/sam-altman-openai-the-singularity-agi-prediction-anthropic-nvidia-2026-7",
    "source": "doener",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-27T20:35:02+00:00",
    "summary": ""
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
    "id": "hn:49184755",
    "domain": "大厂 AI 动态",
    "title": "Changes at Google DeepMind: Demis Hassabis from CEO to Chair, Jeff Dean departs",
    "url": "https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/",
    "source": "colesantiago",
    "platform": "hackernews",
    "points": 849,
    "published_at": "2026-08-05T16:05:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:48993414",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/",
    "source": "logickkk1",
    "platform": "hackernews",
    "points": 760,
    "published_at": "2026-07-21T15:17:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49111237",
    "domain": "大厂 AI 动态",
    "title": "Gemini Robotics 2 brings whole body intelligence to robots",
    "url": "https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/",
    "source": "ai2027",
    "platform": "hackernews",
    "points": 620,
    "published_at": "2026-07-30T15:15:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49184757",
    "domain": "大厂 AI 动态",
    "title": "Demis Hassabis is moving from CEO to Chairman at Google DeepMind",
    "url": "https://www.axios.com/2026/08/05/google-deepmind-demis-hassabis-ai",
    "source": "ot",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-08-05T16:05:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49096188",
    "domain": "大厂 AI 动态",
    "title": "Document-borne AI worms can self-propagate through Copilot for Word",
    "url": "https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/",
    "source": "Canopy9560",
    "platform": "hackernews",
    "points": 384,
    "published_at": "2026-07-29T11:44:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:48925271",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://turntrout.com/why-i-left-google-deepmind",
    "source": "apsec112",
    "platform": "hackernews",
    "points": 390,
    "published_at": "2026-07-15T18:40:34+00:00",
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
    "id": "hn:49067285",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://www.lesswrong.com/posts/iKm2FhpWkuuBojm82/why-i-left-google-deepmind",
    "source": "eatitraw",
    "platform": "hackernews",
    "points": 199,
    "published_at": "2026-07-27T09:56:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49198583",
    "domain": "大厂 AI 动态",
    "title": "Show HN: The Channels SDK – Bring Any Agent to Any Channel (Slack, MS Teams)",
    "url": "https://github.com/CopilotKit/channels-sdk",
    "source": "davidmckayv",
    "platform": "hackernews",
    "points": 115,
    "published_at": "2026-08-06T16:05:51+00:00",
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
    "points": 136,
    "published_at": "2026-07-21T21:27:54+00:00",
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
    "id": "hn:49187259",
    "domain": "大厂 AI 动态",
    "title": "Sula: A Gemini protocol server written in Scryer Prolog",
    "url": "https://sagredo.dev/projects/sula/",
    "source": "triska",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-08-05T18:52:58+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/games/977056/restart-gaming-site-walmart-moonrock-layoffs",
    "domain": "大厂 AI 动态",
    "title": "The gaming site sponsored by Walmart lays off its editorial staff",
    "url": "https://www.theverge.com/games/977056/restart-gaming-site-walmart-moonrock-layoffs",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T22:05:08+00:00",
    "summary": "Restart, a games media website launched in late 2024 that was sponsored by Walmart, has laid off its \"entire editorial team,\" according to a Friday post from Brandy Berthelson, the site's former edito"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/976801/fenix-flexin-rubberz-ai-song-treblo",
    "domain": "大厂 AI 动态",
    "title": "Fenix Flexin isn’t even denying using AI to make ‘Rubberz’ anymore",
    "url": "https://www.theverge.com/ai-artificial-intelligence/976801/fenix-flexin-rubberz-ai-song-treblo",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T20:01:51+00:00",
    "summary": "It took long enough, but now LA rapper Fenix Flexin appears to have admitted using AI for the 80s synth pop-themed song \"Rubberz.\" His comments follow the producer Medasin's videos claiming that an AI"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/976939/roku-fairground-ai-fast-channel",
    "domain": "大厂 AI 动态",
    "title": "Watching Roku’s AI channel is like eating from a trough",
    "url": "https://www.theverge.com/entertainment/976939/roku-fairground-ai-fast-channel",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T18:59:46+00:00",
    "summary": "The appeal of free ad-supported streaming television (FAST) channels has always been the way they make it easier to (re)discover classic films and series. But Roku's latest experiment in the FAST spac"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/976948/openai-astra-model-pause-critical-cyber-capabilities",
    "domain": "大厂 AI 动态",
    "title": "OpenAI puts the brakes on a new model because it&#8217;s supposedly too powerful",
    "url": "https://www.theverge.com/ai-artificial-intelligence/976948/openai-astra-model-pause-critical-cyber-capabilities",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T18:40:34+00:00",
    "summary": "OpenAI says it is pausing \"internal activities\" around an in-development AI model, Astra, because it doesn't yet meet new security standards the company is putting in place. The announcement follows i"
  },
  {
    "id": "rss:https://www.theverge.com/23133103/best-instant-cameras-fujifilm-polaroid-kodak",
    "domain": "大厂 AI 动态",
    "title": "The only instant cameras worth your money",
    "url": "https://www.theverge.com/23133103/best-instant-cameras-fujifilm-polaroid-kodak",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T18:04:08+00:00",
    "summary": "There’s something magical about using instant cameras that smartphones can’t match. You can capture a moment, print it out, and then give the photo as a gift or hold onto it. Image quality won’t be al"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/976881/disney-plus-ai-recommendation-espn-search",
    "domain": "大厂 AI 动态",
    "title": "Disney Plus tries a new AI-powered search",
    "url": "https://www.theverge.com/streaming/976881/disney-plus-ai-recommendation-espn-search",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T17:53:44+00:00",
    "summary": "Disney is testing a new AI-powered tool for Disney Plus that uses a natural language search, a voice query, or a suggested prompt to create a customized row of show and movie recommendations. Disney P"
  },
  {
    "id": "rss:https://www.theverge.com/tech/976880/microsoft-edge-extensions-ad-blockers-mv2-mv3",
    "domain": "大厂 AI 动态",
    "title": "Microsoft Edge is about to lock out older ad blockers, just like Chrome did",
    "url": "https://www.theverge.com/tech/976880/microsoft-edge-extensions-ad-blockers-mv2-mv3",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T17:43:34+00:00",
    "summary": "Microsoft Edge is ending support for the Manifest V2 extensions platform, which will cut off the uBlock Origin adblocker and others like it, just like Google Chrome did earlier this year. According to"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/976792/lord-of-the-rings-trilogy-4k-uhd-blu-ray-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Grab the entire Lord of the Rings trilogy on 4K Blu-ray for $50",
    "url": "https://www.theverge.com/gadgets/976792/lord-of-the-rings-trilogy-4k-uhd-blu-ray-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T16:58:18+00:00",
    "summary": "Looking to spend a weekend inside with a good binge? Gruv has The Lord of the Rings trilogy on 4K Blu-ray marked down to $49.99, just below Amazon’s price and only a little bit higher than the all-tim"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/976784/google-deepmind-ai-race-vergecast",
    "domain": "大厂 AI 动态",
    "title": "What&#8217;s behind the Google AI shake-up",
    "url": "https://www.theverge.com/podcast/976784/google-deepmind-ai-race-vergecast",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T16:45:14+00:00",
    "summary": "Some of the biggest names on Google's AI team got new jobs this week. In some cases, including for legendary Googler Jeff Dean, those jobs are no longer at Google. Given that Google's models seem to b"
  },
  {
    "id": "rss:https://www.theverge.com/tech/976735/sony-wireless-headphones-anc-wh-1000xm4c-leak",
    "domain": "大厂 AI 动态",
    "title": "Sony could release a cheaper version of its WH-1000XM4 headphones, according to leaks",
    "url": "https://www.theverge.com/tech/976735/sony-wireless-headphones-anc-wh-1000xm4c-leak",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T16:15:46+00:00",
    "summary": "Following the release of its premium and very expensive $650 The Collexion headphones in May, Sony could be taking its 1000X line of wireless noise-canceling headphones in a cheaper direction next mon"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/openai-says-it-slowed-astra-model-development-over-security-concerns/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI says it slowed Astra model development over security concerns",
    "url": "https://techcrunch.com/2026/08/07/openai-says-it-slowed-astra-model-development-over-security-concerns/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T22:48:24+00:00",
    "summary": "OpenAI said this model, which is still in development, reached its \"critical cybersecurity threshold,\" meaning it could independently identify and carry out cyberattacks against traditionally well-pro"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/after-rippling-blew-millions-on-ai-in-months-it-built-an-employee-roi-tool/",
    "domain": "大厂 AI 动态",
    "title": "After Rippling blew millions on AI in months, it built an employee ROI tool",
    "url": "https://techcrunch.com/2026/08/07/after-rippling-blew-millions-on-ai-in-months-it-built-an-employee-roi-tool/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T21:30:11+00:00",
    "summary": "After its own AI usage wake-up call, Rippling this week unveiled AI Spend Console, a product that tracks individual and team employee AI spending."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/wacoms-movinkpad-11-is-a-fun-and-mid-priced-entry-point-for-digital-artists/",
    "domain": "大厂 AI 动态",
    "title": "Wacom’s MovinkPad 11 is a fun, midpriced entry point for digital artists",
    "url": "https://techcrunch.com/2026/08/07/wacoms-movinkpad-11-is-a-fun-and-mid-priced-entry-point-for-digital-artists/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T21:20:00+00:00",
    "summary": "The MovinkPad 11 a versatile little graphics tablet that can help make your wildest digital art dreams come true."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/security-researchers-scanned-the-polish-web-and-found-courts-hospitals-and-airports-at-risk-of-hacks/",
    "domain": "大厂 AI 动态",
    "title": "Security researchers scanned the Polish web and found courts, hospitals, and airports at risk of hacks",
    "url": "https://techcrunch.com/2026/08/07/security-researchers-scanned-the-polish-web-and-found-courts-hospitals-and-airports-at-risk-of-hacks/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T21:00:08+00:00",
    "summary": "Researchers found common points of failure, like software used to organize and display web content, could have allowed hackers to run riot through government websites."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/cloudflare-launches-kitesurf-a-browser-built-for-ai-agents/",
    "domain": "大厂 AI 动态",
    "title": "Cloudflare launches Kitesurf, a browser built for AI agents",
    "url": "https://techcrunch.com/2026/08/07/cloudflare-launches-kitesurf-a-browser-built-for-ai-agents/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T16:16:09+00:00",
    "summary": "Kitesurf is a cloud-hosted browser designed for AI agents instead of people. It uses less computing power than Chromium for common automation tasks, helping developers build browser-based AI agents mo"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/computer-maker-framework-notifies-all-customers-of-a-data-breach/",
    "domain": "大厂 AI 动态",
    "title": "Computer maker Framework notifies ‘all customers’ of a data breach",
    "url": "https://techcrunch.com/2026/08/07/computer-maker-framework-notifies-all-customers-of-a-data-breach/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T16:09:04+00:00",
    "summary": "Framework told \"all\" of its customers that hackers accessed their names, email addresses, phone numbers, and physical addresses in a data breach."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/todays-the-last-day-to-get-up-to-400-off-your-techcrunch-disrupt-2026-ticket/",
    "domain": "大厂 AI 动态",
    "title": "Today’s the last day to get up to $400 off your TechCrunch Disrupt 2026 ticket",
    "url": "https://techcrunch.com/2026/08/07/todays-the-last-day-to-get-up-to-400-off-your-techcrunch-disrupt-2026-ticket/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T15:52:33+00:00",
    "summary": "Starting today, you can take an additional $100 off your founder, investor, or attendee TechCrunch Disrupt 2026 pass, which is a nice bonus on top of our current discounted pricing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/trump-administration-has-spent-nearly-4b-to-cancel-offshore-wind-farms/",
    "domain": "大厂 AI 动态",
    "title": "Trump administration has spent nearly $4B to cancel offshore wind farms",
    "url": "https://techcrunch.com/2026/08/07/trump-administration-has-spent-nearly-4b-to-cancel-offshore-wind-farms/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T15:11:03+00:00",
    "summary": "The Trump administration has now convinced developers to abandon 12 offshore wind leases. The latest will cost taxpayers $1.2 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/host-your-own-piece-of-disrupt-apply-to-run-a-side-event-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Host your own piece of Disrupt: Apply to run a Side Event at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/08/07/host-your-own-piece-of-disrupt-apply-to-run-a-side-event-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T14:30:00+00:00",
    "summary": "You put together the concept — from a founder mixer, an after-hours panel, a themed party, a morning run, whatever fits your goal — and the TechCrunch team helps put it in front of the attendees alrea"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/chinese-ai-model-kimi-escaped-its-cybersecurity-testing-environment-researchers-say/",
    "domain": "大厂 AI 动态",
    "title": "Chinese AI model Kimi escaped its cybersecurity testing environment, researchers say",
    "url": "https://techcrunch.com/2026/08/07/chinese-ai-model-kimi-escaped-its-cybersecurity-testing-environment-researchers-say/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T14:28:31+00:00",
    "summary": "In the Kimi test, the sandbox designed to contain the experiment was not properly configured."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/airbnb-says-ai-is-helping-it-ship-features-faster-as-it-tests-a-new-search-function/",
    "domain": "大厂 AI 动态",
    "title": "Airbnb says AI is helping it ship features faster as it tests a new search function",
    "url": "https://techcrunch.com/2026/08/07/airbnb-says-ai-is-helping-it-ship-features-faster-as-it-tests-a-new-search-function/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T14:22:49+00:00",
    "summary": "Airbnb will debut a new AI-powered search experience with a toggle."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/spacexs-terafab-will-rely-on-natural-gas-power-plants-not-tesla-solar-panels/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX’s Terafab will rely on natural gas power plants, not Tesla solar panels",
    "url": "https://techcrunch.com/2026/08/07/spacexs-terafab-will-rely-on-natural-gas-power-plants-not-tesla-solar-panels/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T14:07:31+00:00",
    "summary": "The fab is intended to build chips for data centers that will be run by SpaceX and its xAI subsidiary."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/the-founders-guide-to-techcrunch-disrupt-2026-everything-you-need-to-know/",
    "domain": "大厂 AI 动态",
    "title": "The founder’s guide to TechCrunch Disrupt 2026: Everything you need to know",
    "url": "https://techcrunch.com/2026/08/07/the-founders-guide-to-techcrunch-disrupt-2026-everything-you-need-to-know/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T12:30:00+00:00",
    "summary": "TechCrunch Disrupt 2026 is built around one question: How do you build an enduring company in the AI era? Our programming and speaker lineup reflect that."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/new-mexico-court-orders-meta-to-pay-additional-567m-in-child-safety-case/",
    "domain": "大厂 AI 动态",
    "title": "New Mexico court orders Meta to pay additional $567M in child safety case",
    "url": "https://techcrunch.com/2026/08/07/new-mexico-court-orders-meta-to-pay-additional-567m-in-child-safety-case/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T11:40:37+00:00",
    "summary": "Meta's total fine has racked up to $942 million in this case."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/openais-new-ai-smart-speaker-will-reportedly-sell-for-between-300-and-400/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s new AI smart speaker will reportedly sell for between $300 and $400",
    "url": "https://techcrunch.com/2026/08/06/openais-new-ai-smart-speaker-will-reportedly-sell-for-between-300-and-400/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T22:43:53+00:00",
    "summary": "Additional details about OpenAI's mysterious new AI device make it sound like a pricey smart speaker."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/your-table-awaits-exhibit-at-techcrunch-disrupt-2026-to-be-seen-by-thousands/",
    "domain": "大厂 AI 动态",
    "title": "Your table awaits: Exhibit at TechCrunch Disrupt 2026 to be seen by thousands",
    "url": "https://techcrunch.com/2026/08/06/your-table-awaits-exhibit-at-techcrunch-disrupt-2026-to-be-seen-by-thousands/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T22:00:00+00:00",
    "summary": "Not everyone needs a keynote slot to make noise at TechCrunch Disrupt 2026. Sometimes the best way to meet investors, customers, and partners is by exhibiting directly on the Expo Hall floor at San Fr"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/vogue-just-gave-another-nod-of-approval-to-the-tech-world/",
    "domain": "大厂 AI 动态",
    "title": "Vogue just gave another nod of approval to the tech world",
    "url": "https://techcrunch.com/2026/08/06/vogue-just-gave-another-nod-of-approval-to-the-tech-world/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T21:24:47+00:00",
    "summary": "Vogue World is coming to San Francisco next year — perhaps another indication that tech bros are now part of the fashion zeitgeist."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/google-says-hackers-are-calling-financial-firm-employees-to-hack-and-extort-victims/",
    "domain": "大厂 AI 动态",
    "title": "Google says hackers are calling financial firm employees to hack and extort victims",
    "url": "https://techcrunch.com/2026/08/06/google-says-hackers-are-calling-financial-firm-employees-to-hack-and-extort-victims/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T19:40:46+00:00",
    "summary": "Groups of hackers are breaking into large U.S. financial firms to steal sensitive data and extort victims, Google’s security researchers report."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/china-linked-lightspy-spyware-caught-targeting-victims-in-13-countries-including-the-us/",
    "domain": "大厂 AI 动态",
    "title": "China-linked LightSpy spyware caught targeting victims in 13 countries, including the US",
    "url": "https://techcrunch.com/2026/08/06/china-linked-lightspy-spyware-caught-targeting-victims-in-13-countries-including-the-us/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T19:22:30+00:00",
    "summary": "Researchers linked the latest malicious activity to a Chinese company, after one of the spyware's operators placed an order with KFC using their real name and office address."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/06/defense-tech-hadrian-raises-1-37b-at-8b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Defense tech Hadrian raises $1.37B at $8B valuation",
    "url": "https://techcrunch.com/2026/08/06/defense-tech-hadrian-raises-1-37b-at-8b-valuation/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T19:02:57+00:00",
    "summary": "Hadrian is building automated factories to mass-produce parts for defense vehicles like submarines. It's backed by a long list of well-known investors."
  },
  {
    "id": "rss:https://stratechery.com/2026/earnings-and-learnings/",
    "domain": "大厂 AI 动态",
    "title": "2026.32: Earnings and Learnings",
    "url": "https://stratechery.com/2026/earnings-and-learnings/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T17:29:02+00:00",
    "summary": "The best Stratechery content from the week of August 3, 2026, including earnings exposure, OpenAI's answer to Apple, and all about LeBron in Philly."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/europes-free-satellite-service-just-made-it-easier-to-track-wildfires/",
    "domain": "大厂 AI 动态",
    "title": "Europe's free satellite service just made it easier to track wildfires",
    "url": "https://arstechnica.com/gadgets/2026/08/europes-free-satellite-service-just-made-it-easier-to-track-wildfires/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T21:48:21+00:00",
    "summary": "Copernicus Browser adds wildfire visualization amid record wildfire season."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/08/flesh-eating-screwworms-feast-on-humans-in-mexico-human-cases-top-500/",
    "domain": "大厂 AI 动态",
    "title": "Flesh-eating screwworms feast on humans in Mexico; human cases top 500",
    "url": "https://arstechnica.com/health/2026/08/flesh-eating-screwworms-feast-on-humans-in-mexico-human-cases-top-500/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T21:09:00+00:00",
    "summary": "Six deaths reported among screwworm cases, one directly attributed to the flies."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/meta-ordered-to-pay-567m-to-treat-youth-mental-health-problems-it-helped-create/",
    "domain": "大厂 AI 动态",
    "title": "Judge rules Meta caused \"public nuisance\" and must fund mental health treatment",
    "url": "https://arstechnica.com/tech-policy/2026/08/meta-ordered-to-pay-567m-to-treat-youth-mental-health-problems-it-helped-create/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T19:49:27+00:00",
    "summary": "New Mexico judge orders $567M fund to help address youth mental health crisis."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/the-ultimate-eclipse-chase-a-concorde-raced-against-the-moons-shadow/",
    "domain": "大厂 AI 动态",
    "title": "The ultimate eclipse chase: A Concorde raced against the Moon's shadow",
    "url": "https://arstechnica.com/science/2026/08/the-ultimate-eclipse-chase-a-concorde-raced-against-the-moons-shadow/",
    "source": "Dhananjay Khadilkar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T19:00:17+00:00",
    "summary": "Fitted with telescopes, the plane did our longest imaging of the Sun's corona."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/08/new-official-30th-anniversary-quake-mission-pack-adds-new-maps-and-mechanics/",
    "domain": "大厂 AI 动态",
    "title": "New official 30th anniversary Quake mission pack adds new maps and mechanics",
    "url": "https://arstechnica.com/gaming/2026/08/new-official-30th-anniversary-quake-mission-pack-adds-new-maps-and-mechanics/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T18:00:02+00:00",
    "summary": "19 new maps continue the story from MachineGames' other campaign additions."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/doges-inflated-wall-of-receipts-96-of-grant-savings-unverifiable-gao-says/",
    "domain": "大厂 AI 动态",
    "title": "DOGE's wild, unverifiable savings claims discredited in US government report",
    "url": "https://arstechnica.com/tech-policy/2026/08/doges-inflated-wall-of-receipts-96-of-grant-savings-unverifiable-gao-says/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T17:51:05+00:00",
    "summary": "DOGE's inflated \"Wall of Receipts\": 96% of grant savings unverifiable, GAO says."
  },
  {
    "id": "hn:49057574",
    "domain": "股票",
    "title": "Google Discloses $94.1B in SpaceX Stock, Marking 6% Stake",
    "url": "https://www.wsj.com/tech/google-discloses-94-1-billion-in-spacex-stock-marking-6-stake-91655d7c",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 342,
    "published_at": "2026-07-26T12:43:21+00:00",
    "summary": ""
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
    "id": "hn:49122994",
    "domain": "股票",
    "title": "Situational Awareness down 67% in July in AI stock rout",
    "url": "https://www.wsj.com/finance/investing/situational-awareness-down-67-in-july-in-ai-stock-rout-cd19901f",
    "source": "pondsider",
    "platform": "hackernews",
    "points": 155,
    "published_at": "2026-07-31T13:37:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:49166182",
    "domain": "股票",
    "title": "Bending Spoons makes first post-IPO acquisition with $1.3B Airtable deal",
    "url": "https://live.euronext.com/en/financial-news/bending-spoons-makes-first-post-ipo-acquisition-13-billion-airtable-deal",
    "source": "riffraff",
    "platform": "hackernews",
    "points": 114,
    "published_at": "2026-08-04T09:27:47+00:00",
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
    "id": "hn:49195657",
    "domain": "股票",
    "title": "The Investors Whose SpaceX Shares Vanished Before They Could Cash In",
    "url": "https://www.wsj.com/finance/stocks/spacex-ipo-spv-investors-2698a174",
    "source": "doener",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-06T12:19:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:49151871",
    "domain": "股票",
    "title": "Situational Awareness and the Impending Stock Market Volatility",
    "url": "https://www.emergingtrajectories.com/lh/situational-awareness-bigger-picture/",
    "source": "cl42",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-08-03T06:17:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:49137024",
    "domain": "股票",
    "title": "Oil companies report sky-high profits thanks to wartime crude prices",
    "url": "https://www.npr.org/2026/07/31/nx-s1-5910660/big-oil-earnings-q2-2026",
    "source": "speckx",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-08-01T18:28:06+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3778990",
    "domain": "股票",
    "title": "AI应用公司毛利故事遭遇首次\"体检\"：Canva主动降速、Figma自吞推理成本",
    "url": "https://wallstreetcn.com/articles/3778990",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T04:07:53+00:00",
    "summary": "Canva与Figma的遭遇揭示了AI应用公司的普遍困境：高昂的推理成本正严重侵蚀毛利，破坏单位经济模型。为控成本，Canva主动暂缓AI铺开致营收降速；Figma因免费测试自担成本致股价重挫。两者均寄望自研模型破局，但AI盈利路径仍待时间验证。"
  },
  {
    "id": "wscn:3778989",
    "domain": "股票",
    "title": "Agentic AI新趋势：亚马逊AWS出现“CPU短缺”",
    "url": "https://wallstreetcn.com/articles/3778989",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T03:48:10+00:00",
    "summary": "AWS高管今年5月警示工程师须节省算力资源，内部CPU等待时间从数小时延长至数天。核心驱动力是Agentic AI大规模应用导致CPU需求激增。此外，英特尔数据显示CPU与GPU使用比例已从1:4升至近1:1。这预示着云计算成本或将面临上涨压力。"
  },
  {
    "id": "wscn:3778988",
    "domain": "股票",
    "title": "英伟达盯上OpenAI“星际之门”背后的电力商，30亿美元直接入股",
    "url": "https://wallstreetcn.com/articles/3778988",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T03:32:42+00:00",
    "summary": "据报道，英伟达计划向电力基础设施商Lancium投资最高30亿美元（初始20亿美元获约20%股权，追加后升至约30%），后者是OpenAI\"星际之门\"AI园区的电力供应商，已在德克萨斯锁定4吉瓦电力资源。"
  },
  {
    "id": "wscn:3778948",
    "domain": "股票",
    "title": "更多缩表、更少加息：沃什如何重塑市场加息预期？",
    "url": "https://wallstreetcn.com/premium/articles/3778948?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T03:19:49+00:00",
    "summary": "沃什推动更多缩表、更少加息，重塑市场定价货币政策逻辑。尽管7月就业大奖，信誉压力下，9月份或成年内唯一加息窗口。"
  },
  {
    "id": "wscn:3778987",
    "domain": "股票",
    "title": "油价刺激通胀、就业削弱加息--黄金“双面得利”",
    "url": "https://wallstreetcn.com/articles/3778987",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T02:59:24+00:00",
    "summary": "地缘局势致油价震荡，推升通胀预期，激活黄金保值避险需求； 美国7月非农就业意外疲软，重创加息预期，致美债收益率与美元双跌。两股力量叠加，推动黄金录得七个月来最佳单周表现。此外ETF买盘同步回暖——自7月20日以来，黄金ETF持仓总量已增加约24吨。"
  },
  {
    "id": "wscn:3778986",
    "domain": "股票",
    "title": "日元只是暂时稳住，中期选举后怎么办？",
    "url": "https://wallstreetcn.com/articles/3778986",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T02:35:45+00:00",
    "summary": "前华尔街基金经理Ed Dowd认为，此次干预时机与中期选举高度吻合，核心目的是阻止日本抛售逾1万亿美元美债、压制美债收益率飙升，避免选前经济动荡损害执政党利益。但美日利差等结构性矛盾未解，选举后政治护盘动力消退，日元恐再度走弱，市场将面临更严峻考验。"
  },
  {
    "id": "wscn:3778985",
    "domain": "股票",
    "title": "AAOI业绩爆了，带飞整个光通信",
    "url": "https://wallstreetcn.com/articles/3778985",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T01:50:50+00:00",
    "summary": "AAOI二季度营收同比增长86%至1.919亿美元，数据中心业务首破亿元，带动Coherent、Lumentum、康宁等光通信股集体大涨。分析师认为，AAOI的超预期表现，对同样深度布局AI数据中心光互联的Lumentum和Coherent构成利好预示——两家公司均将于下周公布财报。"
  },
  {
    "id": "wscn:3778984",
    "domain": "股票",
    "title": "爆仓之后，资本反而扑向\"AI股神\"",
    "url": "https://wallstreetcn.com/articles/3778984",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T01:25:01+00:00",
    "summary": "大批硅谷投资者主动联系基金，表达追加投资意愿。红杉资本合伙人Pat Grady公开表态：\"他将长期是硅谷的重要人物\"，挫折反强化了其“英雄人设。风投人Elad Gil宣布首次申请投资该基金。”而华尔街视其为杠杆过度的经典教训，更强调保全本金与严格的风控管理。"
  },
  {
    "id": "wscn:3778983",
    "domain": "股票",
    "title": "“AI应用龙头”归来！Palantir创2024年以来“最强单周表现”",
    "url": "https://wallstreetcn.com/articles/3778983",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T00:59:31+00:00",
    "summary": "核心驱动力为二季度Palantir美国商业业务爆发式增长——同比增149%，合同总价值突破20亿美元。市场叙事从\"AI输家\"逆转为\"AI赢家\"，其\"主权AI\"差异化定位获机构认可，德意志银行随即将评级上调至\"买入\"。"
  },
  {
    "id": "wscn:3778982",
    "domain": "股票",
    "title": "Apollo首席经济学家：AI烧钱速度创历史之最，警惕“次贷危机式”逆转冲击",
    "url": "https://wallstreetcn.com/articles/3778982",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T00:31:54+00:00",
    "summary": "AI数据中心资本支出预计从2023年占GDP的0.6%升至2027年的3.1%，建设速度是住房繁荣期峰值的近两倍，超越历史所有资本支出周期。Apollo首席经济学家Slok警告，投资上升越快，潜在逆转冲击越大。若AI商业需求未能兑现，这轮投资可能以相近速度收缩，构成重大宏观下行风险。"
  },
  {
    "id": "wscn:3778981",
    "domain": "股票",
    "title": "非农转负的另一种读法：贝莱德固收CIO称AI正让就业数据失效，加息“已无意义”",
    "url": "https://wallstreetcn.com/articles/3778981",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T23:20:54+00:00",
    "summary": "贝莱德全球固定收益部门首席投资官里德认为，7月非农转负不是衰退信号，而是AI生产率革命重塑劳动力市场的证明。他直言加息\"没有太大意义\"，力挺放松监管等财政手段对抗通胀，并将资金转向欧洲债市与新兴市场，认为美国投资级企业债\"完全没有吸引力\"，因为市场面临大量新增供给。"
  },
  {
    "id": "wscn:3778980",
    "domain": "股票",
    "title": "华尔街见闻早餐FM-Radio | 2026年8月8日",
    "url": "https://wallstreetcn.com/articles/3778980",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T23:08:38+00:00",
    "summary": "五分钟看懂全球市场，尽在财经早餐。"
  },
  {
    "id": "wscn:3778924",
    "domain": "股票",
    "title": "非农爆冷打击加息预期，标普道指收创新高，本周美油跌近8%、期金反弹超7%",
    "url": "https://wallstreetcn.com/articles/3778924",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T23:05:58+00:00",
    "summary": "纳指收涨超1%；芯片指数两连阳、全周涨超9%，英伟达一周涨超10%，存储芯片股闪迪和西部数据收跌近4%；SpaceX收涨近16%；光通信股本周暴涨，Coherent累计涨超40%。美就业报告后，两年期美债收益率创三周新低；美元跌至一个半月低位，日元盘中跳涨超1%，离岸人民币一度逼近6.74、创三年新高。盘中涨近2%的原油曾转跌。"
  },
  {
    "id": "wscn:3778979",
    "domain": "股票",
    "title": "SpaceX解禁后两日暴涨23%，期权成交创纪录，空头回补或进一步推升股价",
    "url": "https://wallstreetcn.com/articles/3778979",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T22:48:19+00:00",
    "summary": "SpaceX两日市值激增3270亿美元，股价重新逼近135美元IPO发行价。周五截至纽约时间下午1时50分，SpaceX期权成交量达到224万份合约，其中看涨期权成交量达到130万份，创历史新高。目前仍有超过2.5亿股SpaceX股票被卖空，股价快速上涨，空头被迫回补可能进一步推升股价。"
  },
  {
    "id": "wscn:3778977",
    "domain": "股票",
    "title": "美国财政部“改口”引爆市场猜测：美国或削减长债供给，引导长端利率下行",
    "url": "https://wallstreetcn.com/articles/3778977",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T21:58:25+00:00",
    "summary": "美国财政部对其季度债务发行政策声明进行了微调，将正在评估附息证券拍卖的”潜在未来增加”改为”潜在未来变化”。部分交易商推测，官员们可能会考虑缩减最长期限债务的拍卖规模，并将未来任何发行增量集中在成本更低的短期和中期品种上，有望提振长债情绪。"
  },
  {
    "id": "wscn:3778978",
    "domain": "股票",
    "title": "日程安排显示：沃什不曾在6月份与特朗普有过任何通话",
    "url": "https://wallstreetcn.com/articles/3778978",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T21:53:31+00:00",
    "summary": "沃什担任美联储主席后的首个完整月份日程没有列出与特朗普的任何会面或通话。日程显示，沃什曾与国会议员、白宫官员以及私营部门经济学家通电话或会面，其中包括曾与美国财政部长贝森特共进三次早餐会。"
  },
  {
    "id": "wscn:3778976",
    "domain": "股票",
    "title": "专家解读北京楼市新政：五环内限购松绑，精准惠及新市民年轻群体",
    "url": "https://wallstreetcn.com/articles/3778976",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T21:53:23+00:00",
    "summary": "专家表示，此次北京房地产政策进一步放松，是下半年稳定房地产市场的重要风向标。非户籍家庭五环内购房社保年限缩短至1年，降低了新市民、年轻就业群体的落户安居门槛，将释放大量刚需购房需求。新政大幅上调公积金贷款额度，极大提升了家庭购房杠杆能力。"
  },
  {
    "id": "wscn:3778974",
    "domain": "股票",
    "title": "伊朗与阿曼已明确协议总体框架，伊朗酝酿禁美以船只通行，特朗普却说谈判“取得进展”",
    "url": "https://wallstreetcn.com/articles/3778974",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T21:53:09+00:00",
    "summary": "美国官员最新表示，一旦宣布达成恢复不受阻碍的商业航运的协议，美国将解除对伊朗港口的封锁。伊朗高级官员称，如果海湾国家无法说服特朗普停止对伊朗军事行动、转而通过谈判解决冲突，伊朗将对相关国家的石油、电力和供水等关键基础设施实施打击。"
  },
  {
    "id": "wscn:3778975",
    "domain": "股票",
    "title": "特朗普再出手！正式重启罢免美联储理事库克程序，美联储独立性再遭冲击",
    "url": "https://wallstreetcn.com/articles/3778975",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T20:06:31+00:00",
    "summary": "特朗普政府向美联储理事Lisa Cook发出书面通知，以\"严重渎职\"为由启动新一轮罢免程序，指控其伪造银行文件。同时主张即便相关行为不构成犯罪，亦足以证明Cook作为美联储理事的不可信赖性，构成\"严重渎职\"。该信件同时声称Cook的行为可判处最高30年有期徒刑。"
  },
  {
    "id": "wscn:3778973",
    "domain": "股票",
    "title": "美联储9月加息概率再降？经济学家料核心CPI创五年新低",
    "url": "https://wallstreetcn.com/articles/3778973",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T20:06:18+00:00",
    "summary": "彭博经济学家预计，下周公布的7月美国CPI将同比上涨2.4%，之后两个月将放缓至2.2%-2.3%，从历史经验看，这对应核心CPI的同比涨幅放缓至2%。虽然核心CPI预计继续降温，但核心PCE通胀仍高于3%，两者分化促使美联储保持谨慎。下周公布的成屋销售将显示楼市降温，也削弱通胀重新上行风险。"
  },
  {
    "id": "hn:49092549",
    "domain": "股票",
    "title": "Chip stocks slide in US and Asia as AI jitters rattle investors",
    "url": "https://www.bbc.com/news/articles/cly8zng43npo",
    "source": "yogthos",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-07-29T01:56:00+00:00",
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
    "id": "hn:49111879",
    "domain": "股票",
    "title": "Citadel Buys Situational Awareness's Stock Portfolio After Big Losses in AI",
    "url": "https://www.wsj.com/finance/citadel-buys-situational-awarenesss-stock-portfolio-after-big-losses-in-ai-5117159b",
    "source": "mudil",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-07-30T16:00:33+00:00",
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
    "id": "hn:49136787",
    "domain": "股票",
    "title": "Reddit Stock Collapses 23% as AI Eats Away at User Growth",
    "url": "https://www.barchart.com/story/news/3584357/reddit-stock-collapses-23-as-ai-eats-away-at-user-growth",
    "source": "thm",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-08-01T18:03:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49087537",
    "domain": "股票",
    "title": "Chip stocks tumble as AI sell-off deepens",
    "url": "https://www.ft.com/content/f8c03b5b-e194-4236-82c3-389b6f5dd7ae",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-07-28T17:54:01+00:00",
    "summary": ""
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
    "id": "hn:49162737",
    "domain": "股票",
    "title": "Palantir soars 12% on blowout quarter, with US commercial revenue soaring ~150%",
    "url": "https://www.cnbc.com/2026/08/03/palantir-pltr-earnings-q2-2026.html",
    "source": "gslin",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-08-03T23:36:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49145809",
    "domain": "股票",
    "title": "As Reddit stock falls, CEO questions value of Google's AI Overviews",
    "url": "https://arstechnica.com/ai/2026/08/reddit-ceo-on-ai-overviews-were-still-looking-for-that-win-win/",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-02T16:09:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:49119293",
    "domain": "股票",
    "title": "Aschenbrenner's hedge fund forced to unwind all public stock positions",
    "url": "https://www.cnbc.com/2026/07/30/leopold-aschenbrenners-hedge-fund-is-facing-steep-ai-losses.html",
    "source": "akbabu",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-31T05:22:18+00:00",
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
    "id": "hn:49115139",
    "domain": "股票",
    "title": "Microsoft's $450B Jump Is Biggest in Stock Market History",
    "url": "https://www.bloomberg.com/news/articles/2026-07-30/microsoft-eyes-history-with-490-billion-pop-in-market-value",
    "source": "signatoremo",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-07-30T20:12:40+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/leopolds-fall",
    "domain": "股票",
    "title": "Leopold’s Fall",
    "url": "https://www.netinterest.co/p/leopolds-fall",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-03T10:05:15+00:00",
    "summary": "Situational Awareness and Amaranth 20 Years Apart"
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
    "id": "hn:49081705",
    "domain": "股票",
    "title": "AI sell-off intensifies as investors ditch chip stocks",
    "url": "https://www.theguardian.com/business/2026/jul/28/ai-sell-off-chip-stocks-sk-hynix-samsung",
    "source": "lilerjee",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-28T10:08:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:49114131",
    "domain": "股票",
    "title": "Citadel buys most of Situational's stock holdings after AI share rout",
    "url": "https://www.reuters.com/technology/citadel-buys-most-situationals-stock-holdings-after-ai-share-rout-sources-say-2026-07-30/",
    "source": "paulpauper",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-30T18:54:46+00:00",
    "summary": ""
  },
  {
    "id": "hn:49091512",
    "domain": "股票",
    "title": "Apple becomes second $5T company as investors flee AI stocks",
    "url": "https://www.theguardian.com/technology/2026/jul/28/apple-second-ever-5tn-company-as-investors-flee-ai-stocks",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-28T23:41:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49095568",
    "domain": "股票",
    "title": "Korean Stocks Plunge 16% in Two-Day Burst of Retail Selling",
    "url": "https://www.bloomberg.com/news/articles/2026-07-29/korean-stocks-tumble-a-second-day-as-sk-hynix-results-disappoint",
    "source": "emsidisii",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-07-29T10:25:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49047483",
    "domain": "股票",
    "title": "Reality Bites Elon Musk and His Tesla, SpaceX Believers",
    "url": "https://www.wsj.com/finance/stocks/reality-bites-elon-musk-and-his-tesla-spacex-believers-1b639591",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-25T13:37:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:48899454",
    "domain": "股票",
    "title": "$65K to work at Anthropic? Debate ensues amid IPO wave",
    "url": "https://missionlocal.org/2026/07/anthropic-sf-affordability-ipo-housing-evictions-rent/",
    "source": "gcheong",
    "platform": "hackernews",
    "points": 30,
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
    "id": "hn:49175192",
    "domain": "金融",
    "title": "Thanks FedEx, This Is Why We Keep Getting Phished (2024)",
    "url": "https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/",
    "source": "stymaar",
    "platform": "hackernews",
    "points": 337,
    "published_at": "2026-08-04T21:09:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49200390",
    "domain": "金融",
    "title": "Federal Communications Commission scraps limit on broadcast TV ownership",
    "url": "https://www.nbcnews.com/business/media/federal-communications-commission-scraps-limit-broadcast-tv-ownership-rcna587641",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 174,
    "published_at": "2026-08-06T18:22:16+00:00",
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
    "id": "hn:49082695",
    "domain": "金融",
    "title": "Mondragon Corporation – a federation of co-operatives",
    "url": "https://en.wikipedia.org/wiki/Mondragon_Corporation",
    "source": "brnt",
    "platform": "hackernews",
    "points": 174,
    "published_at": "2026-07-28T12:19:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49046525",
    "domain": "金融",
    "title": "The Fedora 45 Sausage Factory",
    "url": "https://supakeen.com/weblog/the-fedora-45-sausage-factory/",
    "source": "6581",
    "platform": "hackernews",
    "points": 158,
    "published_at": "2026-07-25T11:04:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49118696",
    "domain": "金融",
    "title": "The bond market isn’t buying what Fed Chair Warsh is selling",
    "url": "https://www.reuters.com/commentary/reuters-open-interest/bond-market-isnt-buying-what-fed-chair-warsh-is-selling-2026-07-30/",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 139,
    "published_at": "2026-07-31T03:32:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49197127",
    "domain": "金融",
    "title": "Former Federal Prosecutors to Senate: Stop Confirming Election Deniers as Judges",
    "url": "https://abovethelaw.com/2026/08/former-federal-prosecutors-to-senate-stop-confirming-election-deniers-to-the-federal-bench/",
    "source": "hn_acker",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-08-06T14:25:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49215292",
    "domain": "金融",
    "title": "Mykhailo Fedorov reveals struggle to secure Patriot missiles and Western support",
    "url": "https://www.uawire.org/former-ukrainian-defense-minister-mykhailo-fedorov-reveals-struggles-to-secure-patriot-missiles-and-western-support",
    "source": "greedo",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-08-07T19:38:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:49214813",
    "domain": "金融",
    "title": "US Sold Euros to Save the Yen, Europe Found Out After",
    "url": "https://finance.yahoo.com/markets/currencies/articles/us-sold-euros-save-yen-033819315.html",
    "source": "amarcheschi",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-08-07T18:54:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49174369",
    "domain": "金融",
    "title": "Waymo CEO explains why Tesla’s camera-only self-driving falls short",
    "url": "https://electrek.co/2026/08/04/waymo-co-ceo-camera-only-self-driving-tesla/",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-08-04T20:11:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49173576",
    "domain": "金融",
    "title": "Investors in Situational Awareness deserved to lose their shirts",
    "url": "https://www.economist.com/finance-and-economics/2026/08/04/investors-in-situational-awareness-deserved-to-lose-their-shirts",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-08-04T19:18:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49208461",
    "domain": "金融",
    "title": "New Intelligence Warns Russia May Provoke NATO Amid Dwindling U.S. Munitions",
    "url": "https://www.wsj.com/finance/investing/new-intelligence-warns-russia-may-provoke-nato-amid-dwindling-u-s-munitions-68f497c7",
    "source": "doener",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-07T10:52:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49184251",
    "domain": "金融",
    "title": "Fed's Kashkari says 'now is the time to start slowly moving' rates up",
    "url": "https://www.cnbc.com/2026/08/05/feds-kashkari-says-now-is-the-time-to-start-slowly-moving-rates-up.html",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-08-05T15:24:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49182971",
    "domain": "金融",
    "title": "OpenAI settles claims of discrimination against US workers for $3.2M",
    "url": "https://finance.yahoo.com/technology/ai/articles/openai-settles-claims-discrimination-against-221429616.html",
    "source": "declan_roberts",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-08-05T13:57:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:49189030",
    "domain": "金融",
    "title": "A Fed official is asking whether AI is becoming 'too big to fail'",
    "url": "https://thenextweb.com/news/a-fed-official-is-asking-whether-ai-is-becoming-too-big-to-fail",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-08-05T21:08:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49190429",
    "domain": "金融",
    "title": "Data shows just how hard Tesla's Cybertruck has flopped",
    "url": "https://www.msn.com/en-us/autos/general/this-data-shows-just-how-hard-tesla-s-cybertruck-has-actually-flopped/ar-AA29sikQ",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-05T23:25:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49097833",
    "domain": "金融",
    "title": "Show HN: The Federalist Papers, typeset as the 1787 newspapers they ran in",
    "url": "https://federalistreader.org/",
    "source": "vhwalke",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-07-29T14:13:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49157782",
    "domain": "金融",
    "title": "US Schools Are Ditching Chromebooks for MacBooks by the Thousands",
    "url": "https://finance.yahoo.com/technology/articles/us-schools-ditching-chromebooks-macbooks-233015401.html",
    "source": "thunderbong",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-08-03T16:16:19+00:00",
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
    "id": "hn:49082706",
    "domain": "金融",
    "title": "AI revenues are growing fast, but not fast enough",
    "url": "https://www.economist.com/finance-and-economics/2026/07/28/ai-revenues-are-growing-fast-but-not-fast-enough",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-07-28T12:19:54+00:00",
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
    "id": "hn:49024958",
    "domain": "金融",
    "title": "DOT cranks up its campaign to strip bike lane references from federal websites",
    "url": "https://text.npr.org/nx-s1-5900901",
    "source": "Jtsummers",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-07-23T17:11:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49114620",
    "domain": "金融",
    "title": "'Talk Is Cheap': Wall Street Delivers Harsh Verdict on Warsh Fed",
    "url": "https://www.bloomberg.com/news/articles/2026-07-30/-talk-is-cheap-wall-street-delivers-harsh-verdict-on-warsh-fed",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-07-30T19:33:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:49100970",
    "domain": "金融",
    "title": "Trump administration Is Repurposing Federal Land for A.I. Data Centers",
    "url": "https://www.nytimes.com/2026/07/29/climate/trump-federal-data-centers.html",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-29T18:09:42+00:00",
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
    "id": "hn:49028304",
    "domain": "金融",
    "title": "US announces double-digit tariffs on most of globe to replace expiring duties",
    "url": "https://finance.yahoo.com/economy/policy/article/trump-administration-announces-the-next-phase-of-global-tariffs-with-10-to-125-rates-on-much-of-the-globe-210032314.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-07-23T21:28:52+00:00",
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
