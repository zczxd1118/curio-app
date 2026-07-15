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

- 今日日期：`2026-07-15`
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
  "date": "2026-07-15",
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
    "points": 3764149,
    "published_at": "2026-01-15T03:56:12+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署"
  },
  {
    "id": "bvid:BV1wt411T7Hy",
    "domain": "AI",
    "title": "3分钟创建你的饥荒联机专属服务器！纯免费！良心教学！steam+wegame均有！【饥荒五耀】",
    "url": "http://www.bilibili.com/video/av62522150",
    "source": "五耀",
    "platform": "bilibili",
    "points": 1774575,
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
    "points": 1505802,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1229361,
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
    "points": 972925,
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
    "points": 941580,
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
    "points": 891086,
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
    "points": 859446,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1ZzvUBXEoL",
    "domain": "AI",
    "title": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av115818910194374",
    "source": "极客教学",
    "platform": "bilibili",
    "points": 791615,
    "published_at": "2026-01-01T08:40:14+00:00",
    "summary": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 667597,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1RSFUzVEAG",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码",
    "url": "http://www.bilibili.com/video/av116045469783373",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 558946,
    "published_at": "2026-02-10T08:59:28+00:00",
    "summary": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 527215,
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
    "points": 463081,
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
    "points": 383664,
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
    "points": 243686,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 239845,
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
    "points": 237365,
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
    "points": 215651,
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
    "points": 186232,
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
    "points": 177131,
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
    "points": 159725,
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
    "points": 147574,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1QE7N6jEuQ",
    "domain": "AI",
    "title": "真的被自己用心开发的昔涟Agent这段话感动到了",
    "url": "http://www.bilibili.com/video/av116794052316703",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 134316,
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
    "points": 116670,
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
    "points": 109332,
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
    "points": 92559,
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
    "points": 88308,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 84691,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53062,
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
    "points": 42736,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29990,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27876,
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
    "points": 26218,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV15i7K69EN7",
    "domain": "AI",
    "title": "【6.22最新发布】claude桌面版安装教程！一周快速入门claude code保姆级教程！",
    "url": "http://www.bilibili.com/video/av116793196676384",
    "source": "是蒜七丫",
    "platform": "bilibili",
    "points": 23048,
    "published_at": "2026-06-22T10:07:14+00:00",
    "summary": "求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连求三连"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22623,
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
    "points": 18306,
    "published_at": "2026-06-11T13:41:36+00:00",
    "summary": "Claude Code 接管虚幻引擎5，打造了一款游戏\n下载我的 CLAUDE.md（帮你省 token 的配置）\n链接：https://pan.quark.cn/s/b6e50b4b2535\n提取码：tbaE\nStefan 3D AI ：https://www.youtube.com/watch?v=iRcrZjOt5H8&amp;t=1s\n🔗 完整教程指南和链接：https://www.top"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 15218,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 14515,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 14315,
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
    "points": 13793,
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
    "points": 13790,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1CbvxBwEah",
    "domain": "AI",
    "title": "真的不用服务器！用Cloudflare Workers+D1轻松搭建网站！",
    "url": "http://www.bilibili.com/video/av115803408045159",
    "source": "软件工程师Tim",
    "platform": "bilibili",
    "points": 13619,
    "published_at": "2025-12-29T14:51:53+00:00",
    "summary": "本期影片分享一下如何利用cloudflare workers搭建网站，并且利用d1免费数据库，实现无服务器的一个带前后端功能的网站。也就是说，即使你没有服务器，也能够搭建一个属于自己的网站。比如我自己搭建的这个案例网站在线留言板。就是完全搭建在cloudflare workers上面的，里面有静态页面 也有动态api接口。都是部署在workers上面的，并且集成了它提供的数据库。\n\n\n#cloud"
  },
  {
    "id": "bvid:BV165dAYxEdD",
    "domain": "AI",
    "title": "只需几行代码用Java写一个MCP服务！从0到1开发MCP服务！",
    "url": "http://www.bilibili.com/video/av114306863598282",
    "source": "图灵诸葛官方号",
    "platform": "bilibili",
    "points": 12215,
    "published_at": "2025-04-09T07:43:00+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持~\r\n本视频配套资料戳这里获取→https://www.bilibili.com/read/cv38661345/\r\n【还可额外领取100w字Java面试宝典】"
  },
  {
    "id": "bvid:BV1vKTj6ZEZ1",
    "domain": "AI",
    "title": "Java AI Agent大模型开发，Spring AI+Spring AI Alibaba Agent+Skill，原理→框架→组件→调优→实战项目完整教程",
    "url": "http://www.bilibili.com/video/av116849819781343",
    "source": "java架构师徐庶",
    "platform": "bilibili",
    "points": 9091,
    "published_at": "2026-07-02T10:14:08+00:00",
    "summary": "这套视频是2026年Java后端转型AI Agent的完整闭环教程，不只教你调用大模型，更吃透Spring AI Alibaba底层架构与企业落地方案；学完既能搞定面试跳槽、拿到高薪AI岗，也能在现有公司落地智能客服、知识库、业务自动化等 AI项目!给大家整理了一份超全学习资料资料包含视频笔记+源码+面试题合集+简历模板+面试指导+Java+Al大模型全栈架构师学习路线图|职业规划领资料戳:htt"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 8543,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 6998,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "bvid:BV1haMh6cEkv",
    "domain": "AI",
    "title": "【7.8最新发布】ClaudeCode桌面版安装+中文汉化教程+免费白嫖Opus4.8",
    "url": "http://www.bilibili.com/video/av116879666447399",
    "source": "我不是皮皮奇",
    "platform": "bilibili",
    "points": 6919,
    "published_at": "2026-07-08T00:30:00+00:00",
    "summary": "7月份全B站最新免费的ClaudeCode桌面版教程，从0到1的安装，免登录，中文汉化，接入opus4.8，ClaudeCode永远的神！\nCCSwitch详细配置教程：https://b23.tv/x1WZKve"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6529,
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
    "points": 6518,
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
    "points": 6460,
    "published_at": "2026-01-07T04:47:17+00:00",
    "summary": "OpenCode 是一款面向开发者的开源 AI CLI 编程工具，支持多模型并行、LSP 自动加载、极速响应与非订阅制计费。无论是命令行、桌面 App 还是 VS Code 插件，OpenCode 都提供高效、不啰嗦的 AI 编程体验，是 Cursor 与 Claude Code 的有力替代方案。"
  },
  {
    "id": "hn:48873836",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, CoreWeave, and Nebius: Inside the Circular Financing of the GPU Boom",
    "url": "https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom",
    "source": "adletbalzhanov",
    "platform": "hackernews",
    "points": 367,
    "published_at": "2026-07-11T17:21:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:48903715",
    "domain": "AI 算力 / 半导体",
    "title": "Alternative(s) to run CUDA on non-Nvidia hardware",
    "url": "https://www.hpcwire.com/2026/07/09/spectral-compute-aims-to-set-cuda-free-will-it-succeed/",
    "source": "alok-g",
    "platform": "hackernews",
    "points": 131,
    "published_at": "2026-07-14T08:24:49+00:00",
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
    "id": "rss:https://www.eetimes.com/electronic-design-industry-rides-chip-wave-apac-leads-q1-2026-growth/",
    "domain": "AI 算力 / 半导体",
    "title": "Electronic Design Industry Rides Chip Wave, APAC Leads Q1 2026 Growth",
    "url": "https://www.eetimes.com/electronic-design-industry-rides-chip-wave-apac-leads-q1-2026-growth/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T17:00:00+00:00",
    "summary": "Chip design tools are cashing in: Q1 EDA revenue hit $5.7B as APAC surged 17.7% and hyperscalers went DIY. The post Electronic Design Industry Rides Chip Wave, APAC Leads Q1 2026 Growth appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/five-test-considerations-to-prepare-for-q-day/",
    "domain": "AI 算力 / 半导体",
    "title": "Five Test Considerations to Prepare for Q-Day",
    "url": "https://www.eetimes.com/five-test-considerations-to-prepare-for-q-day/",
    "source": "Sameh Yamany",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T12:30:00+00:00",
    "summary": "Q-Day is coming fast, and “harvest now, decrypt later” is already in play. The post Five Test Considerations to Prepare for Q-Day appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/solving-motion-connectivity-and-efficiency-challenges-in-factory-automation/",
    "domain": "AI 算力 / 半导体",
    "title": "Solving Motion, Connectivity, and Efficiency Challenges in Factory Automation",
    "url": "https://www.eetimes.com/solving-motion-connectivity-and-efficiency-challenges-in-factory-automation/",
    "source": "Arrow Electronics and Microchip Technology",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T08:46:25+00:00",
    "summary": "Explore factory automation challenges from the designer’s perspective and discover how to tackle development while improving performance. The post Solving Motion, Connectivity, and Efficiency Challeng"
  },
  {
    "id": "rss:https://www.eetimes.com/spain-semiconductor-industry-convenes-to-forge-domestic-alliances/",
    "domain": "AI 算力 / 半导体",
    "title": "Spain Semiconductor Industry Convenes to Forge Domestic Alliances",
    "url": "https://www.eetimes.com/spain-semiconductor-industry-convenes-to-forge-domestic-alliances/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T07:32:41+00:00",
    "summary": "AESEMI holds the first semiconductor MatchMaking day in Spain to forge new alliances and consolidate the ecosystem. The post Spain Semiconductor Industry Convenes to Forge Domestic Alliances appeared "
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
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/us-govt-allows-chinese-telecom-giant-zte-to-purchase-nvidia-h200-ai-chips-firm-joins-alibaba-tencent-and-bytedance-in-access-to-hopper-tech",
    "domain": "AI 算力 / 半导体",
    "title": "US gov't allows Chinese telecom giant ZTE to purchase Nvidia H200 AI chips — firm joins Alibaba, Tencent, and ByteDance in access to Hopper tech",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/us-govt-allows-chinese-telecom-giant-zte-to-purchase-nvidia-h200-ai-chips-firm-joins-alibaba-tencent-and-bytedance-in-access-to-hopper-tech",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T19:46:26+00:00",
    "summary": "The United States has licensed Chinese telecom giant ZTE to purchase restricted Nvidia H200 AI chips, but Chinese regulators and domestic procurement initiatives may limit the material impact of the c"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/samsung-990-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung 990 2TB SSD Review: New flash, familiar speeds",
    "url": "https://www.tomshardware.com/pc-components/ssds/samsung-990-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T16:00:00+00:00",
    "summary": "The Samsung 990 is the QLC variant of the manufacturer’s 990 EVO Plus. Despite having newer flash, it largely performs like last-gen, with mediocre power efficiency."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/elon-musks-colossus-2-data-center-installed-59-natural-gas-turbines-without-permission-report-claims-thousands-of-tons-of-pollutants-reportedly-impact-black-communities-in-mississippi-already-suffering-from-elevated-lung-disease-rates",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk’s Colossus 2 data center installed 59 natural gas turbines without permission, report claims — thousands of tons of pollutants reportedly impact black communities in Mississippi already suff",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/elon-musks-colossus-2-data-center-installed-59-natural-gas-turbines-without-permission-report-claims-thousands-of-tons-of-pollutants-reportedly-impact-black-communities-in-mississippi-already-suffering-from-elevated-lung-disease-rates",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T15:55:29+00:00",
    "summary": "The population of the communities surrounding the Colossus 2 site, which is in the center of a lawsuit involving unpermitted natural gas turbines and pollution, is predominantly black."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/china-claims-chip-exports-nearly-doubled-to-177-billion-in-the-first-half-of-2026",
    "domain": "AI 算力 / 半导体",
    "title": "China claims chip exports nearly doubled to $177 billion in the first half of 2026 as memory prices surged — 96% year-on-year increase inflated by hikes",
    "url": "https://www.tomshardware.com/tech-industry/china-claims-chip-exports-nearly-doubled-to-177-billion-in-the-first-half-of-2026",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T14:52:27+00:00",
    "summary": "The Chinese customs administration attributed the surge to global demand for AI hardware."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-invests-usd5-7-billion-in-ireland-fab-aims-to-boost-output-of-xeon-6-next-gen-xeon-products-built-on-intel-3-process",
    "domain": "AI 算力 / 半导体",
    "title": "Intel invests $5.7 billion in Ireland fab — aims to boost output of Xeon 6, next-gen Xeon products built on Intel 3 process",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-invests-usd5-7-billion-in-ireland-fab-aims-to-boost-output-of-xeon-6-next-gen-xeon-products-built-on-intel-3-process",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T13:09:10+00:00",
    "summary": "Intel to modernize semiconductor production facility in Ireland in a bid to increase output of Xeon 6 and other Xeon products made using Intel 3 fabrication process."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/razer-blade-16-2026-review",
    "domain": "AI 算力 / 半导体",
    "title": "Razer Blade 16 (2026) review: Competitive gaming performance and class-leading endurance",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/razer-blade-16-2026-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T13:00:00+00:00",
    "summary": "If you can stomach the nearly $5,000 price tag, the Razer Blade 16 delivers on gaming performance and endurance."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/new-york-enacts-one-year-data-center-ban-on-projects-larger-than-50-megawatts-first-us-state-to-implement-moratorium-will-also-pursue-repealing-tax-exemptions",
    "domain": "AI 算力 / 半导体",
    "title": "New York enacts one-year data center ban on projects larger than 50 megawatts — first US state to implement moratorium; will also pursue repealing tax exemptions",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/new-york-enacts-one-year-data-center-ban-on-projects-larger-than-50-megawatts-first-us-state-to-implement-moratorium-will-also-pursue-repealing-tax-exemptions",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T12:17:43+00:00",
    "summary": "New York is the first to pass a statewide data center moratorium, which pauses all projects greater than 50 MW for one year. The governor's office said that it will create a GEIS to hold developments "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-5800x3d-is-back-in-stock-with-up-to-usd173-in-savings-thanks-to-these-newegg-deals-free-usd70-msi-mag-cooler-brings-costs-well-below-msrp-for-the-standalone-cpu-alongside-an-extra-usd100-off-for-a-16gb-ram-and-motherboard-bundle",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen 7 5800X3D is back in stock with up to $173 in savings, thanks to these Newegg deals — free $70 MSI MAG cooler brings costs well below MSRP for the standalone CPU, alongside an extra $100 off",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-5800x3d-is-back-in-stock-with-up-to-usd173-in-savings-thanks-to-these-newegg-deals-free-usd70-msi-mag-cooler-brings-costs-well-below-msrp-for-the-standalone-cpu-alongside-an-extra-usd100-off-for-a-16gb-ram-and-motherboard-bundle",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T11:39:27+00:00",
    "summary": "The AMD Ryzen 7 5800X3D is back in stock and on sale, with up to $173 in savings to be had at Newegg."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/nvidia-slashes-list-of-authorized-customers-in-asia-in-a-bid-to-reduce-ai-chip-smuggling-report-claims-company-sent-field-inspectors-called-customers-to-check-if-business-is-genuine-after-pressure-from-washington",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia slashes list of authorized customers in Asia in a bid to reduce AI chip smuggling, report claims — company sent field inspectors, called customers to check if business is genuine after pressure",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/nvidia-slashes-list-of-authorized-customers-in-asia-in-a-bid-to-reduce-ai-chip-smuggling-report-claims-company-sent-field-inspectors-called-customers-to-check-if-business-is-genuine-after-pressure-from-washington",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T11:08:54+00:00",
    "summary": "The company culled its list of verified customers, cutting out more than half of its existing client list to reduce incidents of smuggling. Remaining clients have passed more stringent checks, includi"
  },
  {
    "id": "rss:https://www.tomshardware.com/speakers/drops-usd130-desktop-pc-speakers-are-now-just-usd23-save-a-massive-82-percent-on-these-dual-orientation-bmr1-v2-speakers",
    "domain": "AI 算力 / 半导体",
    "title": "Drop's $130 desktop PC speakers are now just $23 — save a massive 82% on these dual-orientation BMR1 V2 speakers",
    "url": "https://www.tomshardware.com/speakers/drops-usd130-desktop-pc-speakers-are-now-just-usd23-save-a-massive-82-percent-on-these-dual-orientation-bmr1-v2-speakers",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T11:04:14+00:00",
    "summary": "Save a massive 82% on these slimline dual-orientation Drop BMR1 V2 nearfield monitor speakers. Pay only $23 to bathe your desktop setup in sound."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/retro-nintendo-switch-2-dock-looks-exactly-like-the-nintendo-64-and-holds-six-game-cards-in-its-cartridge-slot-the-64bitdock-is-available-now-starting-at-usd89",
    "domain": "AI 算力 / 半导体",
    "title": "Retro Nintendo Switch 2 dock looks exactly like the Nintendo 64 and holds six Game Cards in its cartridge slot — the 64BITDOCK is available now starting at $89",
    "url": "https://www.tomshardware.com/video-games/nintendo/retro-nintendo-switch-2-dock-looks-exactly-like-the-nintendo-64-and-holds-six-game-cards-in-its-cartridge-slot-the-64bitdock-is-available-now-starting-at-usd89",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T10:51:06+00:00",
    "summary": "A new Nintendo Switch dock shell has been designed to mimic the sleek undulating curves of the classic Nintendo 64."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/enthusiast-reverse-engineers-steam-controller-2-puck-creates-diy-openpuck-that-works-without-steam-input-custom-firmware-can-emulate-nintendo-playstation-and-xbox-controllers",
    "domain": "AI 算力 / 半导体",
    "title": "Enthusiast reverse-engineers Steam Controller 2 puck, creates DIY 'OpenPuck' that works without Steam Input — custom firmware can emulate Nintendo, PlayStation, and Xbox controllers",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/enthusiast-reverse-engineers-steam-controller-2-puck-creates-diy-openpuck-that-works-without-steam-input-custom-firmware-can-emulate-nintendo-playstation-and-xbox-controllers",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T10:30:00+00:00",
    "summary": "OpenPuck is custom, open-source firmware that can turn a microcontroller into a DIY Steam Controller puck in minutes. You can then use your Steam Controller as a native Xbox, PlayStation or Switch con"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/modder-runs-counter-strike-clone-at-60-fps-on-the-original-sony-psp-openstrike-is-a-proof-of-concept-with-bot-rounds",
    "domain": "AI 算力 / 半导体",
    "title": "Modder successfully runs Counter-Strike clone at 60 FPS on the original Sony PSP — created his own Rust-based 3D engine to power 480 x 272 gameplay, also works on PS Vita",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/modder-runs-counter-strike-clone-at-60-fps-on-the-original-sony-psp-openstrike-is-a-proof-of-concept-with-bot-rounds",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T10:00:00+00:00",
    "summary": "OpenStrike is a Counter-Strike clone built for the PSP, and the project is already running at 60 FPS with bot rounds."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/manufacturing/researchers-create-programmable-material-that-can-steer-heat-and-remember-its-state-without-power-breakthrough-could-eventually-aid-ai-chip-cooling-and-silicon-photonics",
    "domain": "AI 算力 / 半导体",
    "title": "Researchers create programmable material that can steer heat and remember its state without power — breakthrough could eventually aid AI chip cooling and silicon photonics",
    "url": "https://www.tomshardware.com/tech-industry/manufacturing/researchers-create-programmable-material-that-can-steer-heat-and-remember-its-state-without-power-breakthrough-could-eventually-aid-ai-chip-cooling-and-silicon-photonics",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T09:30:00+00:00",
    "summary": "Researchers created a programmable thermal material that steers heat and retains its state without power, a breakthrough that could benefit AI chips, silicon photonics, and infrared devices."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/enclosures/boutique-diy-hi-fi-solution-lets-you-repurpose-your-old-ide-optical-drives-as-a-standalone-audio-player-usd190-cd-rom-player-01-features-a-laser-cut-enclosure-and-a-custom-pcb",
    "domain": "AI 算力 / 半导体",
    "title": "Boutique DIY Hi-Fi solution lets you repurpose your old IDE optical drives as a standalone audio player — $190 CD-ROM Player 01 features a laser-cut enclosure and a custom PCB",
    "url": "https://www.tomshardware.com/pc-components/enclosures/boutique-diy-hi-fi-solution-lets-you-repurpose-your-old-ide-optical-drives-as-a-standalone-audio-player-usd190-cd-rom-player-01-features-a-laser-cut-enclosure-and-a-custom-pcb",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T09:00:00+00:00",
    "summary": "A stylish new product encourages the repurposing of old IDE optical drives as standalone audio players."
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
    "id": "rss:https://www.theverge.com/policy/965792/google-epic-withdraw-injunction-third-party-app-stores-coming-google-play",
    "domain": "大厂 AI 动态",
    "title": "Google and Epic give up fighting — third-party Android app stores are coming next week",
    "url": "https://www.theverge.com/policy/965792/google-epic-withdraw-injunction-third-party-app-stores-coming-google-play",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T03:28:53+00:00",
    "summary": "Epic Games and Google have just jointly withdrawn their attempt to retroactively settle the lawsuit that's changing how Android app stores work in the United States - and that means Google will be for"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/965565/cmf-nothing-watch-3-pro-smartwatch-ios-android-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Nothing’s good-looking Watch 3 Pro smartwatch is just $69",
    "url": "https://www.theverge.com/gadgets/965565/cmf-nothing-watch-3-pro-smartwatch-ios-android-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T22:24:26+00:00",
    "summary": "While most fitness trackers are losing the screens to keep the price low, the CMF by Nothing Watch 3 Pro is a bit different. The budget-friendly smartwatch with a 1.43-inch OLED display is even cheape"
  },
  {
    "id": "rss:https://www.theverge.com/tech/965643/microsoft-windows-11-july-2026-patch-tuesday-updates",
    "domain": "大厂 AI 动态",
    "title": "Windows 11&#8217;s big patch Tuesday allows you to hold off on updates for longer",
    "url": "https://www.theverge.com/tech/965643/microsoft-windows-11-july-2026-patch-tuesday-updates",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T21:32:04+00:00",
    "summary": "Microsoft just released a long list of improvements for Windows 11 as part of its bigger patch Tuesdays, and that includes the ability to pause updates indefinitely, as reported earlier by Windows Cen"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/965670/openai-chatgpt-ai-smart-speaker-hardware-device",
    "domain": "大厂 AI 动态",
    "title": "OpenAI may announce a ChatGPT smart speaker this year",
    "url": "https://www.theverge.com/ai-artificial-intelligence/965670/openai-chatgpt-ai-smart-speaker-hardware-device",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T21:26:32+00:00",
    "summary": "OpenAI's first device is set to be a smart speaker that lets you talk with ChatGPT, according to a report from Bloomberg. The device apparently won't have a screen, but will use a camera and additiona"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/965600/spacexai-grok-build-repository-upload",
    "domain": "大厂 AI 动态",
    "title": "SpaceXAI&#8217;s Grok programming tool was uploading its users&#8217; entire codebase to cloud storage",
    "url": "https://www.theverge.com/ai-artificial-intelligence/965600/spacexai-grok-build-repository-upload",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T19:25:00+00:00",
    "summary": "SpaceXAI's Grok Build AI coding tool was spotted uploading users' entire codebases to Google Cloud before it was reported, and the company turned it off. The Register reports that Cereblab published f"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/965476/philips-hue-essential-starter-kit-hue-bridge-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Philips Hue&#8217;s budget-friendly Essential starter kit has hit a new low price",
    "url": "https://www.theverge.com/gadgets/965476/philips-hue-essential-starter-kit-hue-bridge-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T17:36:05+00:00",
    "summary": "Although most of Prime Day&#8217;s unusually good Philips Hue deals have ended, a few remain, and some, including the black Philips Hue Twilight Sleep and Wake-Up Light, are even cheaper. None, howeve"
  },
  {
    "id": "rss:https://www.theverge.com/tech/965518/plex-tv-down-outage-issues",
    "domain": "大厂 AI 动态",
    "title": "Plex problems prevented users from streaming movies and shows",
    "url": "https://www.theverge.com/tech/965518/plex-tv-down-outage-issues",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T17:23:25+00:00",
    "summary": "Plex services experienced some major issues on Tuesday, with multiple users reporting problems on Plex's forums and on Reddit. Many people use Plex as a way to stream shows and movies they host locall"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/965490/nintendo-switch-2-choose-your-game-bundle-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Nintendo’s Switch 2 bundle that includes a game is $50 off",
    "url": "https://www.theverge.com/gadgets/965490/nintendo-switch-2-choose-your-game-bundle-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T17:20:34+00:00",
    "summary": "Discounts on the Nintendo Switch 2 are rare, but they do happen on occasion. There’s one happening now, actually, on the company’s $499.99 console bundle that includes a digital game (Mario Kart World"
  },
  {
    "id": "rss:https://www.theverge.com/tech/965486/meta-lawsuit-former-employees-ai-layoffs",
    "domain": "大厂 AI 动态",
    "title": "Meta accused of using biased AI targeting for mass layoffs",
    "url": "https://www.theverge.com/tech/965486/meta-lawsuit-former-employees-ai-layoffs",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T17:18:11+00:00",
    "summary": "A group of 26 former Meta employees is suing the company over claims that it used AI tools to unfairly target workers on leave with layoffs, as reported earlier by Reuters. In the lawsuit, the employe"
  },
  {
    "id": "rss:https://www.theverge.com/tech/965378/boston-dynamics-spot-robot-dog-delivery-assistant",
    "domain": "大厂 AI 动态",
    "title": "Boston Dynamics tries using &#8216;robot dogs&#8217; for deliveries",
    "url": "https://www.theverge.com/tech/965378/boston-dynamics-spot-robot-dog-delivery-assistant",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T16:52:47+00:00",
    "summary": "Boston Dynamics' robotic quadruped Spot has already found work doing routine factory inspections and patrolling the ruins of Pompeii, but what about deliveries? The company is testing a new conveyor b"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/openai-researcher-miles-wang-in-talks-to-launch-ai-drug-discovery-startup-valued-at-2b/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI researcher Miles Wang in talks to launch AI drug discovery startup valued at $2B",
    "url": "https://techcrunch.com/2026/07/14/openai-researcher-miles-wang-in-talks-to-launch-ai-drug-discovery-startup-valued-at-2b/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T00:27:04+00:00",
    "summary": "The funding discussions point to investor interest in applying AI to make breakthroughs in life sciences."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/lorde-says-ai-glasses-are-not-sexy/",
    "domain": "大厂 AI 动态",
    "title": "Lorde says AI glasses are ‘not sexy’",
    "url": "https://techcrunch.com/2026/07/14/lorde-says-ai-glasses-are-not-sexy/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T23:10:02+00:00",
    "summary": "\"Increasingly in our world, it gets harder and harder to know what is real,\" Lorde said onstage."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/openais-first-hardware-device-is-reportedly-a-screenless-speaker-that-can-move/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s first hardware device is reportedly a screenless speaker that can move",
    "url": "https://techcrunch.com/2026/07/14/openais-first-hardware-device-is-reportedly-a-screenless-speaker-that-can-move/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T22:22:24+00:00",
    "summary": "The device is weirdly described as involving \"mechanical elements that can move on their own\" and the Bloomberg report includes the detail that the device is designed to \"feel like a companion and bec"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/openai-pushes-back-on-apple-trade-secret-lawsuit/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI pushes back on Apple trade secret lawsuit",
    "url": "https://techcrunch.com/2026/07/14/openai-pushes-back-on-apple-trade-secret-lawsuit/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T22:07:42+00:00",
    "summary": "OpenAI has issued another statement on the lawsuit, this time suggesting it lacks merit."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/openais-new-flagship-model-deletes-files-on-its-own-people-keep-warning/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s new flagship model deletes files on its own, people keep warning",
    "url": "https://techcrunch.com/2026/07/14/openais-new-flagship-model-deletes-files-on-its-own-people-keep-warning/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T21:50:11+00:00",
    "summary": "A number of social media posts claim that GPT-5.6 Sol deleted files and data without warning. OpenAI had basically disclosed the problem in June."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/apple-opens-its-new-siri-ai-to-everyone-with-the-ios-27-public-beta/",
    "domain": "大厂 AI 动态",
    "title": "Apple opens its new Siri AI to everyone with the iOS 27 public beta",
    "url": "https://techcrunch.com/2026/07/14/apple-opens-its-new-siri-ai-to-everyone-with-the-ios-27-public-beta/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T19:42:27+00:00",
    "summary": "If you’ve been waiting to try Apple’s revamped Siri without installing a developer beta, you now can. The company on Tuesday released the iOS 27 public beta, giving iPhone owners early access to its A"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/anthropics-newest-ad-is-creeping-people-out/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s newest ad is creeping people out",
    "url": "https://techcrunch.com/2026/07/14/anthropics-newest-ad-is-creeping-people-out/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T19:41:27+00:00",
    "summary": "Anthropic has consistently attempted to depict itself as the ethical foil to other AI companies. This latest marketing stunt — which leans into criticism of AI as a way to make Anthropic seem aware of"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/the-founder-of-hinge-raised-18m-to-build-a-new-ai-dating-service-overtone/",
    "domain": "大厂 AI 动态",
    "title": "The founder of Hinge raised $18M to build a new AI dating service, Overtone",
    "url": "https://techcrunch.com/2026/07/14/the-founder-of-hinge-raised-18m-to-build-a-new-ai-dating-service-overtone/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T19:39:39+00:00",
    "summary": "Overtone describes itself as \"a voice- and audio-forward service, enabled by AI, that provides highly curated introductions.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/lucid-motors-denies-report-its-considering-bankruptcy/",
    "domain": "大厂 AI 动态",
    "title": "Lucid Motors denies report it’s considering bankruptcy",
    "url": "https://techcrunch.com/2026/07/14/lucid-motors-denies-report-its-considering-bankruptcy/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T18:47:14+00:00",
    "summary": "The company said the \"rumors are completely false\" after its stock sank more than 50% on a report that it was weighing the option."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/google-faces-another-ai-training-lawsuit-from-major-publishers/",
    "domain": "大厂 AI 动态",
    "title": "Google faces another AI training lawsuit from major publishers",
    "url": "https://techcrunch.com/2026/07/14/google-faces-another-ai-training-lawsuit-from-major-publishers/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T18:33:31+00:00",
    "summary": "Hachette, Cengage, Elsevier, and other publishers allege that Google trained its AI on copyrighted works without the necessary permissions."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/deepmind-ceo-calls-for-an-independent-standards-body-to-regulate-frontier-ai/",
    "domain": "大厂 AI 动态",
    "title": "DeepMind CEO calls for an independent standards body to regulate frontier AI",
    "url": "https://techcrunch.com/2026/07/14/deepmind-ceo-calls-for-an-independent-standards-body-to-regulate-frontier-ai/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T17:45:55+00:00",
    "summary": "DeepMind CEO Demis Hassabis is proposing an AI \"standards body\" modeled after FINRA, to test frontier models and develop best practices for their release."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/deepseek-reportedly-in-talks-to-raise-1-5b-then-ipo/",
    "domain": "大厂 AI 动态",
    "title": "DeepSeek reportedly in talks to raise $1.5B, then IPO",
    "url": "https://techcrunch.com/2026/07/14/deepseek-reportedly-in-talks-to-raise-1-5b-then-ipo/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T16:45:23+00:00",
    "summary": "DeepSeek, the Chinese large language model developer, is said to be preparing for a 2027 IPO debut as it also looks to raise around $1.5 billion in new funds at a $71 billion valuation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/metas-adam-mosseri-says-ai-token-budgets-could-soon-be-capped-per-engineer/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s Adam Mosseri says AI token budgets could soon be capped per engineer",
    "url": "https://techcrunch.com/2026/07/14/metas-adam-mosseri-says-ai-token-budgets-could-soon-be-capped-per-engineer/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T16:22:15+00:00",
    "summary": "Instagram head Adam Mosseri believes companies will eventually need to manage AI token spending the same way they manage payroll or other operating expenses, predicting that engineers could soon face "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/google-images-gets-a-pinterest-like-redesign-focused-on-discovery/",
    "domain": "大厂 AI 动态",
    "title": "Google Images gets a Pinterest-like redesign focused on discovery",
    "url": "https://techcrunch.com/2026/07/14/google-images-gets-a-pinterest-like-redesign-focused-on-discovery/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T16:00:00+00:00",
    "summary": "Now, when users navigate to Google Images, they'll see a \"For You\" gallery of images tailored to their interests and browsing history."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/new-york-state-halts-construction-of-all-new-data-centers/",
    "domain": "大厂 AI 动态",
    "title": "New York State halts construction of all new data centers",
    "url": "https://techcrunch.com/2026/07/14/new-york-state-halts-construction-of-all-new-data-centers/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T15:17:59+00:00",
    "summary": "New York has become the first state to temporarily halt approval of large data centers, as Gov. Kathy Hochul argues the AI-driven building boom shouldn’t come at the expense of higher electricity cost"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/iran-abused-mobile-networks-vulnerabilities-to-locate-u-s-military-in-the-middle-east-report-says/",
    "domain": "大厂 AI 动态",
    "title": "Iran abused mobile networks’ vulnerabilities to locate US military in the Middle East, report says",
    "url": "https://techcrunch.com/2026/07/14/iran-abused-mobile-networks-vulnerabilities-to-locate-u-s-military-in-the-middle-east-report-says/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T15:14:40+00:00",
    "summary": "The Iranian government exploited well-known flaws in cellphone networks to locate and then strike U.S. military personnel in the build-up and beginning of the war."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/ringconn-3-review/",
    "domain": "大厂 AI 动态",
    "title": "I’m de-influencing you from buying the RingConn 3 (even though it’s pretty)",
    "url": "https://techcrunch.com/2026/07/14/ringconn-3-review/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T14:45:11+00:00",
    "summary": "The RingConn 3 actually looks like real jewelry, not a wearable -- but its fitness tracking and headache detection features are disappointing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/reflection-inks-1b-compute-deal-with-nebius/",
    "domain": "大厂 AI 动态",
    "title": "Reflection inks $1B compute deal with Nebius",
    "url": "https://techcrunch.com/2026/07/14/reflection-inks-1b-compute-deal-with-nebius/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T14:37:48+00:00",
    "summary": "Reflection AI has signed a $1 billion deal to access Nebius' compute. Reflection was founded in 2024 and is developing open source AI technology."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/the-real-ai-race-may-no-longer-be-at-the-frontier-open-models-hugging-face/",
    "domain": "大厂 AI 动态",
    "title": "The real AI race may no longer be at the frontier",
    "url": "https://techcrunch.com/2026/07/14/the-real-ai-race-may-no-longer-be-at-the-frontier-open-models-hugging-face/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T14:24:53+00:00",
    "summary": "Hugging Face CEO Clem Delangue says enterprises increasingly want open models, due to cost, accessibility, and ownership. Do frontier models still matter if most production AI ends up running on open "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/14/telegrams-shortlink-domain-is-back-online-after-day-long-suspension/",
    "domain": "大厂 AI 动态",
    "title": "Telegram’s shortlink domain is back online after day-long suspension",
    "url": "https://techcrunch.com/2026/07/14/telegrams-shortlink-domain-is-back-online-after-day-long-suspension/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T14:10:13+00:00",
    "summary": "Telegram CEO Pavel Durov confirmed an outage in a tweet, saying that shortlinks to the messaging app had \"stopped working.\""
  },
  {
    "id": "rss:https://stratechery.com/2026/the-openai-super-app-chatgpt-codex-whither-chat/",
    "domain": "大厂 AI 动态",
    "title": "The OpenAI Super App, ChatGPT = Codex, Whither Chat",
    "url": "https://stratechery.com/2026/the-openai-super-app-chatgpt-codex-whither-chat/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T10:00:00+00:00",
    "summary": "OpenAI has refashioned Codex as the new ChatGPT; is the company abandoning the chat category they pioneered?"
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
    "id": "rss:https://arstechnica.com/security/2026/07/microsoft-secure-boot-has-been-broken-for-most-of-its-existence/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft’s Secure Boot has been broken for a decade and no one noticed until now",
    "url": "https://arstechnica.com/security/2026/07/microsoft-secure-boot-has-been-broken-for-most-of-its-existence/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T22:20:48+00:00",
    "summary": "Old and forgotten \"shims\" Microsoft failed to revoke have made Secure Boot bypasses simple."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/americans-in-congo-barred-from-returning-home-amid-ebola-outbreak/",
    "domain": "大厂 AI 动态",
    "title": "Trump admin puts Americans in Congo on \"do-not-board\" list, barring return",
    "url": "https://arstechnica.com/health/2026/07/americans-in-congo-barred-from-returning-home-amid-ebola-outbreak/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T22:09:31+00:00",
    "summary": "Citizens must now spend 21 days in a third country before they are allowed to come home."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/lawsuit-claims-metas-layoff-decisions-were-made-by-ai-not-humans/",
    "domain": "大厂 AI 动态",
    "title": "Lawsuit claims Meta's layoff decisions were made by AI, not humans",
    "url": "https://arstechnica.com/tech-policy/2026/07/lawsuit-claims-metas-layoff-decisions-were-made-by-ai-not-humans/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T20:05:53+00:00",
    "summary": "Meta denies using AI to terminate workers with disabilities and medical problems."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/taco-bell-eyed-in-explosive-diarrheal-outbreak-leafy-greens-suspected/",
    "domain": "大厂 AI 动态",
    "title": "Probe into explosive diarrheal cases points to Taco Bell and bad lettuce",
    "url": "https://arstechnica.com/health/2026/07/taco-bell-eyed-in-explosive-diarrheal-outbreak-leafy-greens-suspected/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T19:00:02+00:00",
    "summary": "Federal officials have not confirmed a source yet—and there may be multiple sources."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/us-military-sent-explosive-drone-boats-into-combat-for-the-first-time/",
    "domain": "大厂 AI 动态",
    "title": "US military sent explosive drone boats into combat for the first time",
    "url": "https://arstechnica.com/ai/2026/07/us-military-sent-explosive-drone-boats-into-combat-for-the-first-time/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T18:00:01+00:00",
    "summary": "US military’s drone boats struck an Iranian naval port as war heats up again."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/these-painted-e-tattoos-could-be-the-future-of-wearable-biosensors/",
    "domain": "大厂 AI 动态",
    "title": "These painted e-tattoos could be the future of wearable biosensors",
    "url": "https://arstechnica.com/science/2026/07/these-painted-e-tattoos-could-be-the-future-of-wearable-biosensors/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T17:31:58+00:00",
    "summary": "Conductive ink is painted directly onto the skin in colorful custom designs, drying into working electrodes."
  },
  {
    "id": "rss:https://arstechnica.com/google/2026/07/google-revamps-image-search-for-its-25th-anniversary-with-more-images-and-more-ai/",
    "domain": "大厂 AI 动态",
    "title": "Google revamps image search for its 25th anniversary with more images and more AI",
    "url": "https://arstechnica.com/google/2026/07/google-revamps-image-search-for-its-25th-anniversary-with-more-images-and-more-ai/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T16:28:14+00:00",
    "summary": "The new Google image search will use your \"unique interests\" to create an always-updated gallery."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/new-york-is-the-first-state-to-impose-a-data-center-moratorium/",
    "domain": "大厂 AI 动态",
    "title": "New York bans data center construction for a year, rattling AI industry",
    "url": "https://arstechnica.com/tech-policy/2026/07/new-york-is-the-first-state-to-impose-a-data-center-moratorium/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T15:06:28+00:00",
    "summary": "New York’s data center moratorium may become the blueprint for anti-AI movement."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/boomers-not-gen-z-are-the-generation-cutting-back-most-on-alcohol/",
    "domain": "大厂 AI 动态",
    "title": "Boomers, not Gen Z, are the generation cutting back most on alcohol",
    "url": "https://arstechnica.com/health/2026/07/boomers-not-gen-z-are-the-generation-cutting-back-most-on-alcohol/",
    "source": "Madeleine Speed, Financial Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-14T13:19:16+00:00",
    "summary": "New research overturns assumption that abstinent younger drinkers are behind weak demand."
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
    "id": "hn:48907665",
    "domain": "股票",
    "title": "IBM is on pace for its worst day ever",
    "url": "https://www.cnn.com/2026/07/14/tech/ibm-stock-worst-day-ever",
    "source": "1970-01-01",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-07-14T14:39:25+00:00",
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
    "id": "wscn:3776902",
    "domain": "股票",
    "title": "剧烈爆仓之后：狂暴的韩股杠杆出清何时迎来终局？",
    "url": "https://wallstreetcn.com/premium/articles/3776902?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T05:07:16+00:00",
    "summary": "韩股去杠杆仍处强平尾声，融资盘尚未出清，监管收紧与杠杆释放节奏将决定市场真正企稳时点。"
  },
  {
    "id": "wscn:3776988",
    "domain": "股票",
    "title": "阿斯麦Q2业绩全面超预期，再度上调全年指引，宣布英特尔采用最先进光刻设备 | 财报见闻",
    "url": "https://wallstreetcn.com/articles/3776988",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T05:02:22+00:00",
    "summary": "阿斯麦将2026年全年净销售额预期上调至430亿至450亿欧元，较此前360亿至400亿欧元的区间大幅提升。阿斯麦披露，英特尔已在美国俄勒冈州工厂正式将High NA EUV设备用于部分Ultra 3（猎豹湖）处理器的量产制造。"
  },
  {
    "id": "wscn:3776757",
    "domain": "股票",
    "title": "大模型7月激战：国产性能快速攀升，海外巨头开启价格战",
    "url": "https://wallstreetcn.com/premium/articles/3776757?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:31:46+00:00",
    "summary": "全球AI大模型正从“百模大战”的混沌期迈入“诸侯混战”的格局重塑期，能力代差快速收窄、资本开支持续膨胀、开源生态加速全球化。"
  },
  {
    "id": "wscn:3776985",
    "domain": "股票",
    "title": "霍尔木兹爆发激烈交火！特朗普：伊朗像伟大拳击手，你以为击败他，结果被重拳反击；若伊朗不回来谈判，将轰炸电厂桥梁，不排除派地面部队",
    "url": "https://wallstreetcn.com/articles/3776985",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:07:27+00:00",
    "summary": "特朗普表示，除非伊朗重返谈判桌，否则美军将在下周打击其桥梁和发电厂。特朗普说：“我们明后晚将对他们进行猛烈打击，而到了下周，情况对他们来说将会变得非常糟糕，因为下周的目标将是桥梁和发电厂。除非他们坐下来谈判，否则我们将摧毁他们所有桥梁和发电厂。”特朗普还表示不排除向伊朗派遣地面部队的可能性。不过，他没有对此作进一步说明。"
  },
  {
    "id": "wscn:3776980",
    "domain": "股票",
    "title": "科创50跌超3%，半导体产业链全线下挫，创新药、白酒逆势拉升，恒科指涨1%，长飞光纤港股跳水",
    "url": "https://wallstreetcn.com/articles/3776980",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:06:01+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市超3600股飘红，上午半天成交1.73万亿。沪深两市半日成交额1.72万亿，较上个交易日放量900亿。板块方面，半导体产业链全线下挫，先进封装、光刻机、晶圆方向领跌；算力硬件题材全线回调，GPU、存储器、PCB方向跌幅明显。创新药概念股大涨，白酒、零售等大消费活跃。"
  },
  {
    "id": "wscn:3776984",
    "domain": "股票",
    "title": "徐阳辞任安踏品牌CEO 主品牌零售改造进入复盘期",
    "url": "https://wallstreetcn.com/articles/3776984",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T03:47:12+00:00",
    "summary": "安踏主品牌突发“换帅”"
  },
  {
    "id": "wscn:3776983",
    "domain": "股票",
    "title": "提高门槛！韩国券商讨论上调芯片股杠杆ETF的最低存款要求",
    "url": "https://wallstreetcn.com/articles/3776983",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T03:27:59+00:00",
    "summary": "韩国芯片股杠杆ETF上市不足半年已近乎腰斩，投资者损失惨重。韩国金融投资协会联合十大资管CEO紧急磋商，拟将投资此类杠杆产品的最低存款要求从目前的1000万韩元（约6714美元）水平上调、分散每日再平衡交易时段，多管齐下为这场\"杠杆风暴\"亡羊补牢。"
  },
  {
    "id": "wscn:3776971",
    "domain": "股票",
    "title": "5年内逼近，10年内超越地面数据中心！这家投行搭了太空数据中心的成本模型",
    "url": "https://wallstreetcn.com/articles/3776971",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T03:12:21+00:00",
    "summary": "德意志银行测算，太空数据中心当前部署成本是地面的约6倍，但随着星舰发射成本大幅下降和卫星技术迭代，2029年SpaceX AI1卫星部署后差距可收窄至1.2倍，2032年有望实现成本反超。关键驱动力是星舰的快速可复用化：发射成本有望从目前约每公斤1429美元降至数年后的每公斤43美元。"
  },
  {
    "id": "wscn:3776982",
    "domain": "股票",
    "title": "占比达41%！中国开源模型下载量超越美国",
    "url": "https://wallstreetcn.com/articles/3776982",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T03:12:01+00:00",
    "summary": "据Hugging Face 2026年春季报告，中国开源模型已占该平台下载量的41%，超越美国。OpenRouter前六大最受欢迎模型全部来自中国机构，Anthropic排名第七。企业成本压力推动“模型路由”策略普及，中国开源模型正批量进入全球企业采购选项。"
  },
  {
    "id": "wscn:3776967",
    "domain": "股票",
    "title": "单周暴涨2.5倍、5个月涨了7倍！OpenAI的Codex用户已突破800万",
    "url": "https://wallstreetcn.com/articles/3776967",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T02:34:17+00:00",
    "summary": "GPT-5.6上线后，Codex与ChatGPT Work合并周活跃用户突破800万，5个月内用户规模扩大逾7倍。爆发式增长致OpenAI基础设施承压，被迫压缩上下文窗口、优化推理容量。OpenAI同步推进平台化战略，将Codex整合进ChatGPT桌面端，但使用额度瓶颈仍是核心挑战。"
  },
  {
    "id": "wscn:3776974",
    "domain": "股票",
    "title": "长飞光纤港股开盘大涨22%，大摩上调评级至超配",
    "url": "https://wallstreetcn.com/articles/3776974",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T02:32:13+00:00",
    "summary": "摩根士丹利上调长飞光纤光缆H股评级至超配，叠加公司发布业绩预喜——预计2026年上半年净利润同比最高暴增逾9倍至30亿元，双重催化剂共振推动股价单日最大涨幅达22%。大摩指出，此前50%回调已充分消化供应端担忧，AI驱动光纤超级周期需求不改，当前估值极具吸引力，入场时机成熟。"
  },
  {
    "id": "wscn:3776978",
    "domain": "股票",
    "title": "中国6月社零同比回升至1%，上半年同比增长1.3%",
    "url": "https://wallstreetcn.com/articles/3776978",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T02:26:57+00:00",
    "summary": "6月社会消费品零售总额同比增长1.0%，较上月由负转正，通讯器材类以16.5%增速领跑，汽车类持续下滑拖累整体表现。上半年，社会消费品零售总额248722亿元，同比增长1.3%。其中，除汽车以外的消费品零售额229034亿元，增长2.8%。"
  },
  {
    "id": "wscn:3776975",
    "domain": "股票",
    "title": "中国二季度GDP同比4.3%，上半年同比增长4.7%",
    "url": "https://wallstreetcn.com/articles/3776975",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T02:20:37+00:00",
    "summary": "上半年装备制造业增加值同比增长9.3%，高技术制造业增加值增长13.3%，分别快于全部规模以上工业增加值3.9和7.9个百分点。分产品看，3D打印设备、锂离子电池、工业机器人产品产量同比分别增长48.5%、39.3%、28.0%。"
  },
  {
    "id": "wscn:3776979",
    "domain": "股票",
    "title": "中国1-6月份城镇固定资产投资下降5.7%，航空、航天器及设备制造业增长23.3%",
    "url": "https://wallstreetcn.com/articles/3776979",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T02:19:38+00:00",
    "summary": "分领域看，基础设施投资同比下降2.4%，制造业投资下降1.2%，房地产开发投资下降18.0%。高技术产业投资同比增长4.6%，其中航空、航天器及设备制造业，计算机及办公设备制造业，信息服务业投资同比分别增长23.3%、8.1%、15.5%。"
  },
  {
    "id": "wscn:3776976",
    "domain": "股票",
    "title": "中国1至6月全国房地产开发投资同比降18%，新建商品房销售额同比下降13.6%",
    "url": "https://wallstreetcn.com/articles/3776976",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T02:15:22+00:00",
    "summary": "其中住宅投资29300亿元，下降17.8%，降幅扩大2.2个百分点。6月末，商品房待售面积76315万平方米，同比下降0.9%。数据还显示，1—6月份，房地产开发企业到位资金40233亿元，同比下降20.2%。"
  },
  {
    "id": "wscn:3776977",
    "domain": "股票",
    "title": "中国6月规模以上工业增加值同比加速至5.3%，计算机、通信和其他电子设备制造业增长15.7%",
    "url": "https://wallstreetcn.com/articles/3776977",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T02:11:14+00:00",
    "summary": "6月份，规模以上工业增加值同比实际增长5.3%，增速比上月加快0.8个百分点。分行业看，铁路、船舶、航空航天和其他运输设备制造业增长18.2%，电气机械和器材制造业增长7.0%，计算机、通信和其他电子设备制造业增长15.7%。"
  },
  {
    "id": "wscn:3776970",
    "domain": "股票",
    "title": "美股溢价飞天！海力士的“美股-韩股”套利交易最早要到7月29日，且散户无法参与",
    "url": "https://wallstreetcn.com/articles/3776970",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T02:04:17+00:00",
    "summary": "SK海力士ADR上市仅三个交易日，相对韩国本地股的溢价已飙升至51%。然而套利机制几近完全失灵——新股转换通道要等到7月29日才开放，转换规则单向受限，个人投资者更被完全拒之门外。参照台积电ADR长期维持约19%溢价的先例，这场\"价差盛宴\"或将持续相当长时间。"
  },
  {
    "id": "wscn:3776972",
    "domain": "股票",
    "title": "6月70城房价：一线城市房价环比涨幅回落，各线城市房价同比降幅继续收窄",
    "url": "https://wallstreetcn.com/articles/3776972",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T01:52:05+00:00",
    "summary": "70个大中城市中，新建商品住宅价格环比上涨城市达到20个，为2025年5月以来最多，较上月增加4个，呈现出更广泛的价格企稳迹象。一线城市继续扮演价格回稳的领头角色，其中上海新建住房同比录得3.1%的正增长。但一线城市二手房价环比涨幅小幅回落至0.3%，新房价格环比涨幅回落至涨0.1%。"
  },
  {
    "id": "wscn:3776969",
    "domain": "股票",
    "title": "高盛韩国一线评论：IBM暴跌验证了存储短缺，散户投降但韩股关键支撑位挺住了，机构相信存储扩产不会太猛",
    "url": "https://wallstreetcn.com/articles/3776969",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T01:13:45+00:00",
    "summary": "高盛首尔团队认为，IBM暴跌25%印证企业客户将资本支出转向存储采购，\"挤出效应\"蔓延至非AI企业买家，从真实经济层面确认存储短缺的广度与深度，存储供应商定价权持续增强。韩股在关键支撑位获机构净买入，散户割肉出局使筹码更干净；受制于设备短缺，存储产能实际扩张将远不及预期，维持KOSPI目标价12000点，立场看多。"
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
    "id": "hn:48892638",
    "domain": "金融",
    "title": "Benchmarking 15 “E-Waste” GPUs with Modern Workloads",
    "url": "https://esologic.com/benchmarking-tesla-gpus/",
    "source": "eso_logic",
    "platform": "hackernews",
    "points": 138,
    "published_at": "2026-07-13T13:48:42+00:00",
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
    "points": 70,
    "published_at": "2026-07-12T21:04:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48915953",
    "domain": "金融",
    "title": "Stripe, Advent offer to buy PayPal for more than $53B",
    "url": "https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/",
    "source": "rvz",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-15T03:32:45+00:00",
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
    "id": "rss:https://arxiv.org/abs/2607.12156",
    "domain": "金融",
    "title": "(Early) AI Compute Asset Pricing",
    "url": "https://arxiv.org/abs/2607.12156",
    "source": "Federico M. Bandi, Yinan Su",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2607.12156v1 Announce Type: new Abstract: Compute (computing power) is a scarce, capital-intensive input at the center of the AI economy. Compute capital expenditure and service flow already exc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.12205",
    "domain": "金融",
    "title": "A Unified Credit Expansion Theory on Housing Cycle: Causal Evidence for Within- and Cross-Metro Patterns in the Prior, Boom, Bust, and Recovery Periods",
    "url": "https://arxiv.org/abs/2607.12205",
    "source": "Bo Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2607.12205v1 Announce Type: new Abstract: During the 1999-2019 U.S. housing cycle, three empirical facts present a puzzle: in the boom period, the correlation between income growth and mortgage "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.12248",
    "domain": "金融",
    "title": "When Directional Accuracy Lies: A Base-Rate-Honest Benchmark for LoRA-Adapted TimesFM on Equity Forecasting",
    "url": "https://arxiv.org/abs/2607.12248",
    "source": "Taizhen Cheung, SA Kwon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2607.12248v1 Announce Type: new Abstract: Large pretrained time-series models such as TimesFM are attractive for financial forecasting, but raw directional accuracy is a misleading scoreboard in"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.12345",
    "domain": "金融",
    "title": "Forecasting Inflation with Microdata: An Adaptive Machine Learning Approach",
    "url": "https://arxiv.org/abs/2607.12345",
    "source": "Catherine Chen, Chen Gao, Jonathon Hazell, Lihua Lei, Chen Lian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2607.12345v1 Announce Type: new Abstract: Does microeconomic heterogeneity help to forecast aggregate inflation in a non-stationary environment? We develop a scan test for whether one forecast o"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.12407",
    "domain": "金融",
    "title": "Statistical Properties and Power Analysis of Divergence Measures for Credit Risk Model Monitoring",
    "url": "https://arxiv.org/abs/2607.12407",
    "source": "Abdullah Karasan, Alper Hekimo\\u{g}lu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2607.12407v1 Announce Type: new Abstract: Divergence measures are essential tools for detecting distributional shifts in model monitoring, particularly crucial given the volatility of financial "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.12414",
    "domain": "金融",
    "title": "Beyond Consistent Scenarios: Deriving Indirect Influence, Transition Resistance, and Adjustment Dynamics",
    "url": "https://arxiv.org/abs/2607.12414",
    "source": "Andrew G. Ross, Julia Gershenzon, Andreas Kleefeld",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2607.12414v1 Announce Type: new Abstract: Assessments of structural change and economic transition dynamics, such as those arising in the energy transition, depend on internally consistent quali"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.12479",
    "domain": "金融",
    "title": "Ito-Wentzell Formula and Dupire Stochastic PDE",
    "url": "https://arxiv.org/abs/2607.12479",
    "source": "Vladimir Lucic",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2607.12479v1 Announce Type: new Abstract: Starting from the classic result of Wentzell, we derive a conditional forward equation and an associated stochastic Dupire PDE for a local-stochastic-vo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.13002",
    "domain": "金融",
    "title": "Shared Bidding Algorithms and Competition: Evidence from Electricity Markets",
    "url": "https://arxiv.org/abs/2607.13002",
    "source": "Nicolas Eschenbaum",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2607.13002v1 Announce Type: new Abstract: Competing firms increasingly delegate pricing and bidding decisions to algorithms supplied by the same third-party providers. We study whether a shared "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.11935",
    "domain": "金融",
    "title": "Eigenvector rotation precedes eigenvalue-based early-warning signals: a TVP-Kalman approach to detecting critical transitions",
    "url": "https://arxiv.org/abs/2607.11935",
    "source": "Gildas Tiwang Ngueuleweu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2607.11935v1 Announce Type: cross Abstract: Early-warning signals (EWS) for critical transitions are predominantly based on changes in the dominant eigenvalue of the system's Jacobian-rising var"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.12990",
    "domain": "金融",
    "title": "A Noise-Aware Quantum Algorithm for Credit Valuation Adjustments on Real Quantum Hardware",
    "url": "https://arxiv.org/abs/2607.12990",
    "source": "Guillem Borr\\`as Espert, Francisco G\\'omez Casanova, Luis de Pedro S\\'anchez, Senaida Hern\\'andez Santana, Pablo Serrano Molinero",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2607.12990v1 Announce Type: cross Abstract: Credit Valuation Adjustment (CVA) requires repeated risk-neutral expectation estimation, making it a natural test bed for quantum amplitude estimation"
  },
  {
    "id": "rss:https://arxiv.org/abs/1911.12944",
    "domain": "金融",
    "title": "Hedging short-maturity Asian options in local volatility models",
    "url": "https://arxiv.org/abs/1911.12944",
    "source": "Jiuk Jang, Jaehyun Kim, Hyungbin Park, Jonghwa Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:1911.12944v3 Announce Type: replace Abstract: This paper discusses the short-maturity behavior of Asian option prices and hedging portfolios. We consider the risk-neutral valuation and the delta"
  },
  {
    "id": "rss:https://arxiv.org/abs/2504.02987",
    "domain": "金融",
    "title": "Model Combination in Risk Sharing under Ambiguity",
    "url": "https://arxiv.org/abs/2504.02987",
    "source": "Emma Kroell, Sebastian Jaimungal, Silvana M. Pesenti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2504.02987v3 Announce Type: replace Abstract: We consider the problem of an agent who faces losses in continuous time over a finite time horizon and may choose to share some of these losses with"
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.03903",
    "domain": "金融",
    "title": "Taming Tail Risk: Regime-Weighted Conformal Calibration for Nonstationary Value-at-Risk",
    "url": "https://arxiv.org/abs/2602.03903",
    "source": "Marc Schmitt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2602.03903v2 Announce Type: replace Abstract: Value-at-risk (VaR) forecasts drive trading constraints and capital allocation, yet realized exceedance rates concentrate in stress periods, when lo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.04004",
    "domain": "金融",
    "title": "Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures: A Systematic Falsification Study",
    "url": "https://arxiv.org/abs/2605.04004",
    "source": "Mathias Mesfin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2605.04004v2 Announce Type: replace Abstract: This paper asks a straightforward question: do common intraday momentum signals built from price and volume data produce a tradable edge in Micro E-"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05091",
    "domain": "金融",
    "title": "Overshooting the Coordinate: Where Factor Corrections Land on Characteristic Axes",
    "url": "https://arxiv.org/abs/2607.05091",
    "source": "Useong Shin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2607.05091v5 Announce Type: replace Abstract: Maximum-Sharpe spanning measures how factors expand the investment opportunity set, not where they leave pricing errors along the characteristics th"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.06427",
    "domain": "金融",
    "title": "The U.S. Mortality Crisis as a Preston Curve Reversal",
    "url": "https://arxiv.org/abs/2607.06427",
    "source": "Ritikaa Khanna, Rourke O'Brien, Andrew Stokes, Atheendar Venkataramani, Elizabeth Wrigley-Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2607.06427v2 Announce Type: replace Abstract: U.S. life expectancy stagnated and declined in the 2010s despite continued growth in real per capita income. We use Preston curves to characterize t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2107.11575",
    "domain": "金融",
    "title": "Peace Through Side Payments",
    "url": "https://arxiv.org/abs/2107.11575",
    "source": "Jingfeng Lu, Zongwei Lu, Christian Riis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2107.11575v5 Announce Type: replace-cross Abstract: We study strategic bargaining for peaceful settlement before conflict escalates into war (modeled as an all-pay auction), comparing two protoc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2212.05317",
    "domain": "金融",
    "title": "On a Merton Problem with Irreversible Healthcare Investment",
    "url": "https://arxiv.org/abs/2212.05317",
    "source": "Giorgio Ferrari, Shihao Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2212.05317v3 Announce Type: replace-cross Abstract: We propose a tractable dynamic framework for the joint determination of optimal consumption, portfolio choice, and irreversible healthcare inv"
  },
  {
    "id": "rss:https://arxiv.org/abs/2412.15239",
    "domain": "金融",
    "title": "Modeling Story Expectations: A Generative Framework using LLMs",
    "url": "https://arxiv.org/abs/2412.15239",
    "source": "Hortense Fong, George Gui, Bo Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2412.15239v4 Announce Type: replace-cross Abstract: Consumers' engagement with stories is shaped by their expectations about what will happen next, yet modeling these forward-looking beliefs ove"
  },
  {
    "id": "rss:https://arxiv.org/abs/2412.17526",
    "domain": "金融",
    "title": "State spaces of multifactor approximations of nonnegative Volterra processes",
    "url": "https://arxiv.org/abs/2412.17526",
    "source": "Eduardo Abi Jaber, Christian Bayer, Simon Breneis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2412.17526v2 Announce Type: replace-cross Abstract: We show that the state spaces of multifactor Markovian processes, coming from approximations of nonnegative Volterra processes, are given by e"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.16274",
    "domain": "金融",
    "title": "A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data",
    "url": "https://arxiv.org/abs/2601.16274",
    "source": "Alessio Brini, Ekaterina Seregina",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2601.16274v2 Announce Type: replace-cross Abstract: We propose the Mixed-Panels-Transformer Encoder (MPTE), a framework for estimating factor models in panels with mixed frequencies and nonlinea"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.11962",
    "domain": "金融",
    "title": "Composite likelihood inference of fractional Gaussian processes with sequentially optimal subset selection",
    "url": "https://arxiv.org/abs/2606.11962",
    "source": "Mathis Fourreau, Matthieu Garcin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T04:00:00+00:00",
    "summary": "arXiv:2606.11962v2 Announce Type: replace-cross Abstract: The composite likelihood method reduces the computational cost of parameter estimation in time series by considering several subsets of observ"
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
