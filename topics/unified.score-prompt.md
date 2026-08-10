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

- 今日日期：`2026-08-10`
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
  "date": "2026-08-10",
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
    "points": 4165995,
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
    "points": 1686089,
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
    "points": 1610001,
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
    "points": 1320431,
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
    "points": 1085682,
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
    "points": 1028728,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 943442,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 670443,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 583015,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 572700,
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
    "points": 523748,
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
    "points": 454018,
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
    "points": 435670,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 230311,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1XVub6bE9h",
    "domain": "AI",
    "title": "当普通人第一次让Agent干活……",
    "url": "http://www.bilibili.com/video/av117053226818905",
    "source": "糖果果的未来要发光",
    "platform": "bilibili",
    "points": 226959,
    "published_at": "2026-08-07T10:00:00+00:00",
    "summary": "最近一个AI agent工具Traework\n发布了一个40万字教程，特别详细。\n我看完后压缩成了这十分钟的教程。\n\n顺便实测了一下 Agent现在到底能干啥，\n还顺便搓了个能用手势控制B站的插件。"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 222873,
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
    "points": 178818,
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
    "points": 163377,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV11urFBrEc4",
    "domain": "AI",
    "title": "🚀告别Vibe Coding！用Superpowers让Claude Code写出工程级代码，一次通过零报错！遵循TDD最佳实践！支持Codex",
    "url": "http://www.bilibili.com/video/av115877227860495",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 154256,
    "published_at": "2026-01-11T15:43:58+00:00",
    "summary": "🚀开发者必看！Superpowers把专业工程团队方法论固化成Skills，让Claude Code告别越写越乱的困境：规格驱动+代码质量双重保障！AI编程新范式！头脑风暴+计划+执行一条龙自动化\n\n\n🚀🚀🚀 视频简介：\n🎬 本期视频详细演示了开源AI编程工作流系统Superpowers的完整使用方法，并通过开发一款iOS时间线笔记原生应用来实测其效果。\n🔧 核心内容：\nSuperpowers工作"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 147555,
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
    "points": 124898,
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
    "points": 93080,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 84648,
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
    "points": 74067,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 73448,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 69705,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47583,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 45710,
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
    "points": 42099,
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
    "points": 40196,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1gwcAzkEhw",
    "domain": "AI",
    "title": "Claude Code Agent Teams上手指南+项目实测",
    "url": "http://www.bilibili.com/video/av116037064331269",
    "source": "程序员阿江-Relakkes",
    "platform": "bilibili",
    "points": 35185,
    "published_at": "2026-02-08T23:30:00+00:00",
    "summary": "用Claude Code干复杂任务总碰到三个问题：\n\n上下文越来越长开始遗忘、任务只能串行效率低、单Agent视角单一容易漏检。\n\nClaude官方发布的Agent Teams功能正好解决这些痛点\n\n一个Team Lead拆任务，多个Teammate并行执行，还能互相通信协调。\n\n本期视频从核心概念、使用场景、底层架构到真实项目实战，带你完整搞懂Agent Teams的正确打开方式。"
  },
  {
    "id": "bvid:BV1xzGH6uEG8",
    "domain": "AI",
    "title": "AI全自动化搭建复杂Simulink模型！5步即可完成部署，全流程分享！",
    "url": "http://www.bilibili.com/video/av116629870481178",
    "source": "电气攻城狮001",
    "platform": "bilibili",
    "points": 33442,
    "published_at": "2026-05-24T13:50:56+00:00",
    "summary": "本期分享五步实操流程，借助 Claude Code 交互载体接入 DeepSeek 大模型，搭配 2026.5.21 最新版 Simulink Agentic Toolkit，解锁 68 项建模技能。依次完成 API 额度配置、环境部署、工具包安装，连通校验后开启全自动模式。无需手动拖拽模块与布线，输入指令即可依托 Simscape 蓝库，在 MATLAB2026a 中自动搭建三相并网逆变器开环模"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 31675,
    "published_at": "2026-05-07T00:00:00+00:00",
    "summary": "全栈课一共分为6大块内容\n第一块：AI智能体开发基础(AI大模型、工具、记忆、MCP、中间件、Skills等核心内容)\n第二块：Claude Code,Trea+skills实现基于需求文档生成用例，基于OpenClaw实现接口自动化落地，基于hermes Agent实现web自动化落地\n第三块：功能测试的智能体开发(项目RAG知识库搭建+Agent搭建+skills开发，实现用例生成的Agent"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30193,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29577,
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
    "points": 28857,
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
    "points": 26581,
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
    "points": 22697,
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
    "points": 21753,
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
    "points": 20444,
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
    "points": 20010,
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
    "points": 18585,
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
    "points": 17684,
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
    "points": 17672,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 16645,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 10951,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9315,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 8386,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 7899,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1k73y6fEDx",
    "domain": "AI",
    "title": "【ClaudeCode】这绝对是b站讲的最好的Claude Code保姆级全套教程，2026最新版，包含所有干货！七天就能从小白到大神！学完即就业，玩转AI技术",
    "url": "http://www.bilibili.com/video/av117001821488596",
    "source": "爬虫逆向",
    "platform": "bilibili",
    "points": 7743,
    "published_at": "2026-07-29T07:25:00+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！"
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
    "id": "rss:https://www.tomshardware.com/pc-components/wolfbox-mf60-compressed-air-duster-is-nearly-40-percent-off-in-a-limited-time-deal-powerful-rechargeable-devices-propulsion-fan-runs-at-up-to-110-000-rpm",
    "domain": "AI 算力 / 半导体",
    "title": "Wolfbox MF60 Compressed Air Duster is nearly 40% off in a limited-time deal — powerful rechargeable device's propulsion fan runs at up to 110,000 RPM",
    "url": "https://www.tomshardware.com/pc-components/wolfbox-mf60-compressed-air-duster-is-nearly-40-percent-off-in-a-limited-time-deal-powerful-rechargeable-devices-propulsion-fan-runs-at-up-to-110-000-rpm",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T15:52:16+00:00",
    "summary": "The Wolfbox MegaFlow 60 has surprisingly dipped below the price of the MegaFlow 50 air duster, and is currently just $30.39."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-keyboards/turtle-beach-command-series-kb5-review-a-touchscreen-and-a-numberpad-in-one-keyboard",
    "domain": "AI 算力 / 半导体",
    "title": "Turtle Beach Command Series KB5 Review: A touchscreen and a numberpad in one keyboard?",
    "url": "https://www.tomshardware.com/peripherals/gaming-keyboards/turtle-beach-command-series-kb5-review-a-touchscreen-and-a-numberpad-in-one-keyboard",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T15:02:16+00:00",
    "summary": "The Turtle Beach Command Series KB5 is a full-size, wired, low-profile keyboard with a small, programmable touchscreen."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/noctua-finds-more-than-half-of-tested-pc-cases-misstate-cpu-cooler-clearances-hands-on-checks-reveal-errors-ranging-from-3-5mm-to-10mm-internal-compatibility-team-conducted-measurements-of-more-than-a-hundred-cases",
    "domain": "AI 算力 / 半导体",
    "title": "Noctua finds more than half of tested PC cases misstate CPU cooler clearances — hands-on checks reveal errors ranging from -3.5mm to +10mm, internal compatibility team conducted measurements of more t",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/noctua-finds-more-than-half-of-tested-pc-cases-misstate-cpu-cooler-clearances-hands-on-checks-reveal-errors-ranging-from-3-5mm-to-10mm-internal-compatibility-team-conducted-measurements-of-more-than-a-hundred-cases",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T14:35:00+00:00",
    "summary": "Users are asking why some measurements on Noctua's compatibility page are different from manufacturer spec sheets."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/modder-pumps-liquid-directly-over-bare-gpu-silicon-via-3d-printed-block-drops-rtx-2060-super-load-temps-to-28-c-despite-initial-leaks",
    "domain": "AI 算力 / 半导体",
    "title": "Modder pumps liquid directly over bare GPU silicon via 3D-printed block — drops RTX 2060 Super load temps to 28°C despite initial leaks",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/modder-pumps-liquid-directly-over-bare-gpu-silicon-via-3d-printed-block-drops-rtx-2060-super-load-temps-to-28-c-despite-initial-leaks",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T14:15:00+00:00",
    "summary": "The fearless TrashBench has been testing direct die water cooling of graphics cards and suffered most of the leaky nightmares you might expect."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/musks-terafab-projected-to-be-larger-than-the-pentagon-apple-park-mall-of-america-and-giga-texas-combined-all-in-one-chip-manufacturing-facility-visualized-to-show-the-projects-massive-footprint",
    "domain": "AI 算力 / 半导体",
    "title": "Musk’s Terafab projected to be larger than the Pentagon, Apple Park, Mall of America, and Giga Texas, combined — all-in-one chip manufacturing facility visualized to show the project’s massive footpri",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/musks-terafab-projected-to-be-larger-than-the-pentagon-apple-park-mall-of-america-and-giga-texas-combined-all-in-one-chip-manufacturing-facility-visualized-to-show-the-projects-massive-footprint",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T13:55:00+00:00",
    "summary": "Elon Musk's Terafab will have at least 100 million sq. ft of interior space, making it the largest such structure on Earth by a big margin. It seems that it will need this amount of space, though, for"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/microsoft-office/x64-port-of-microsoft-word-for-windows-1-1a-arrives-you-can-now-run-this-seminal-1990-word-processor-natively-in-windows-11",
    "domain": "AI 算力 / 半导体",
    "title": "x64 port of Microsoft Word for Windows 1.1a arrives — you can now run this seminal 1990 word processor natively in Windows 11",
    "url": "https://www.tomshardware.com/software/microsoft-office/x64-port-of-microsoft-word-for-windows-1-1a-arrives-you-can-now-run-this-seminal-1990-word-processor-natively-in-windows-11",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T13:40:00+00:00",
    "summary": "A developer has ported 1990's Microsoft Word for Windows 1.1a to x64 so it can run natively on Windows 11 PC systems."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/two-variants-of-nvidias-rtx-spark-show-up-on-geekbench-revealing-a-cut-down-18-core-model-full-20-core-beats-most-x86-mobile-chips-across-multi-core-and-single-core-tests",
    "domain": "AI 算力 / 半导体",
    "title": "Two variants of Nvidia's RTX Spark show up on Geekbench, revealing a cut-down 18-core model — Full 20-core beats most x86 mobile chips across multi-core and single-core tests",
    "url": "https://www.tomshardware.com/pc-components/cpus/two-variants-of-nvidias-rtx-spark-show-up-on-geekbench-revealing-a-cut-down-18-core-model-full-20-core-beats-most-x86-mobile-chips-across-multi-core-and-single-core-tests",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T13:20:00+00:00",
    "summary": "The 20-core SKU of the RTX Spark that we've known to exist for a long time scored 2,570 points in the single-core test and 23,126 points in the multi-core test. The second, 18-core cut-down SKU scored"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/fcc-moves-to-ban-lidar-equipped-foreign-drones-from-us-classifies-the-technology-as-military-grade-in-a-proposal-that-could-also-hit-thermal-models-and-the-swarms-used-drone-light-shows",
    "domain": "AI 算力 / 半导体",
    "title": "FCC moves to ban LiDAR-equipped foreign drones from US — classifies the technology as \"military-grade\" in a proposal that could also hit thermal models and the swarms used in drone light shows",
    "url": "https://www.tomshardware.com/tech-industry/drones/fcc-moves-to-ban-lidar-equipped-foreign-drones-from-us-classifies-the-technology-as-military-grade-in-a-proposal-that-could-also-hit-thermal-models-and-the-swarms-used-drone-light-shows",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T13:00:00+00:00",
    "summary": "The FCC is proposing a retroactive sales ban on previously approved foreign-made drones with LiDAR and other “military-grade” features, potentially removing several popular DJI models from U.S. stores"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/amazons-new-7-65gw-texas-ai-data-center-power-plant-could-become-the-largest-source-of-co2-pollution-in-the-us-custom-35-turbine-gas-plant-authorized-to-emit-33-million-tons-of-annual-greenhouse-gases",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon’s new 7.65GW Texas AI data center power plant could become the largest source of CO₂ pollution in the US — custom 35-turbine gas plant authorized to emit 33 million tons of annual greenhouse ga",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/amazons-new-7-65gw-texas-ai-data-center-power-plant-could-become-the-largest-source-of-co2-pollution-in-the-us-custom-35-turbine-gas-plant-authorized-to-emit-33-million-tons-of-annual-greenhouse-gases",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T12:40:00+00:00",
    "summary": "Amazon is reportedly building a 7.65GW natural gas power plant in Texas to feed a new AI data center, with permits allowing up to 33 million tons of CO₂ emissions per year."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/kansas-town-silences-public-comment-on-gigawatt-ai-data-center-after-receiving-death-threats-moves-to-virtual-meetings-shift-follows-physics-teachers-arrest-for-clapping-at-data-center-hearing",
    "domain": "AI 算力 / 半导体",
    "title": "Kansas town silences public comment on gigawatt AI data center after receiving death threats, moves to virtual meetings — shift follows physics teacher's arrest for clapping at data center hearing",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/kansas-town-silences-public-comment-on-gigawatt-ai-data-center-after-receiving-death-threats-moves-to-virtual-meetings-shift-follows-physics-teachers-arrest-for-clapping-at-data-center-hearing",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T12:20:00+00:00",
    "summary": "Emporia, Kansas, switched to virtual city council meetings after death threats intensified against city leaders. The move also canceled public comments, prompting some members of the public to ask why"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-core-ultra-7-270k-plus-vs-amd-ryzen-7-7700x3d-faceoff",
    "domain": "AI 算力 / 半导体",
    "title": "Intel Core Ultra 7 270K Plus vs AMD Ryzen 7 7700X3D faceoff — battle of the upper mid-range CPUs",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-core-ultra-7-270k-plus-vs-amd-ryzen-7-7700x3d-faceoff",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T12:05:00+00:00",
    "summary": "AMD's 3D V-Cache takes on Intel's latest Core Ultra architecture as we compare the two across various metrics including gaming, productivity, power consumption, and value."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/usb-flash-drives/open-source-stealth-usb-hides-an-encrypted-partition-behind-an-8gb-decoy-drive-phantom-drive-appears-as-a-regular-usb-stick-until-you-create-a-text-file-to-unlock-the-hidden-data",
    "domain": "AI 算力 / 半导体",
    "title": "Open-source stealth USB hides an encrypted partition behind an 8GB decoy drive — 'Phantom Drive' appears as a regular USB stick until you create a text file to unlock the hidden data",
    "url": "https://www.tomshardware.com/pc-components/usb-flash-drives/open-source-stealth-usb-hides-an-encrypted-partition-behind-an-8gb-decoy-drive-phantom-drive-appears-as-a-regular-usb-stick-until-you-create-a-text-file-to-unlock-the-hidden-data",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T12:00:00+00:00",
    "summary": "This USB looks like a standard 8GB drive, but it unlocks a hidden partition when you create a text file with the password inside. The password is never actually written to storage; it's instead interc"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/programming/mind-bending-self-replicating-gif-code-prints-an-exact-copy-of-itself-is-both-a-program-and-its-own-visual-output-champion-coder-shows-off-piet-quine-technique",
    "domain": "AI 算力 / 半导体",
    "title": "Mind-bending self-replicating GIF code prints an exact copy of itself, is both a program and its own visual output — champion coder shows off 'Piet Quine' technique",
    "url": "https://www.tomshardware.com/software/programming/mind-bending-self-replicating-gif-code-prints-an-exact-copy-of-itself-is-both-a-program-and-its-own-visual-output-champion-coder-shows-off-piet-quine-technique",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T11:40:00+00:00",
    "summary": "A champion coder's latest confection is a Piet Quine – a GIF image that prints itself byte-for-byte."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/micron-reportedly-offers-pennies-on-the-dollar-for-crucial-ram-return-only-offers-to-reimburse-original-msrp-despite-it-being-only-37-percent-of-market-value-chipmaker-later-reverses-course-with-a-better-solution",
    "domain": "AI 算力 / 半导体",
    "title": "Micron reportedly offers pennies on the dollar for Crucial RAM return, only offers to reimburse original MSRP despite it being only 37% of market value — chipmaker later reverses course with a better ",
    "url": "https://www.tomshardware.com/pc-components/ram/micron-reportedly-offers-pennies-on-the-dollar-for-crucial-ram-return-only-offers-to-reimburse-original-msrp-despite-it-being-only-37-percent-of-market-value-chipmaker-later-reverses-course-with-a-better-solution",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T11:20:00+00:00",
    "summary": "Crucial memory owner recounts their experience with Micron's warranty process since the company has axed the Crucial brand."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/owner-of-original-intel-8080-pre-production-layout-seeks-restorer-handcrafted-rubylith-mask-shows-5-000-transistors-and-interconnect-patterns-of-the-fabled-2-mhz-cpu",
    "domain": "AI 算力 / 半导体",
    "title": "Owner of original Intel 8080 pre-production layout seeks restorer — handcrafted Rubylith mask shows 5,000 transistors and interconnect patterns of the fabled 2 MHz CPU",
    "url": "https://www.tomshardware.com/pc-components/cpus/owner-of-original-intel-8080-pre-production-layout-seeks-restorer-handcrafted-rubylith-mask-shows-5-000-transistors-and-interconnect-patterns-of-the-fabled-2-mhz-cpu",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T11:00:00+00:00",
    "summary": "The owner of 'the original engineering copy of the Intel 8080 rubylith mask' is looking for a skilled restorer."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/after-24-years-return-to-castle-wolfenstein-is-finally-distributed-uncut-in-germany-game-was-censored-due-to-strict-laws-regarding-nazi-symbolism",
    "domain": "AI 算力 / 半导体",
    "title": "After 24 years, Return to Castle Wolfenstein is finally distributed uncut in Germany — game was censored due to strict laws regarding Nazi symbolism",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/after-24-years-return-to-castle-wolfenstein-is-finally-distributed-uncut-in-germany-game-was-censored-due-to-strict-laws-regarding-nazi-symbolism",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T10:40:00+00:00",
    "summary": "Germany's strict laws surrounding depictions of Nazis meant the game had to be altered, giving it an arguably more interesting story as a result."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090-ships-in-bizarre-8-motherboard-bundle-retailers-hold-gpus-hostage-similar-to-the-crypto-boom",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX 5090 ships in bizarre 8-motherboard bundle — retailers hold GPUs hostage similar to the crypto boom",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090-ships-in-bizarre-8-motherboard-bundle-retailers-hold-gpus-hostage-similar-to-the-crypto-boom",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T17:08:45+00:00",
    "summary": "Taiwanese ecommerce platform PChome24h is packaging RTX 5090 GPUs with a crazy number of motherboards, entry-to-mid-range GPUs, and several other components. While interesting, these combos are alarmi"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/save-usd160-off-amds-ultimate-gaming-cpu-combo-includes-motherboard-and-chip-cooler-usd458-combo-features-ryzen-7-9800x3d-b850-motherboard-and-a-240mm-liquid-aio",
    "domain": "AI 算力 / 半导体",
    "title": "Save $160 off AMD's ultimate gaming CPU combo, includes motherboard and chip cooler — $458 combo features Ryzen 7 9800X3D, B850 motherboard, and a 240mm liquid AIO",
    "url": "https://www.tomshardware.com/pc-components/cpus/save-usd160-off-amds-ultimate-gaming-cpu-combo-includes-motherboard-and-chip-cooler-usd458-combo-features-ryzen-7-9800x3d-b850-motherboard-and-a-240mm-liquid-aio",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T14:06:16+00:00",
    "summary": "Newegg is offering a big discount on a Ryzen 7 9800X3D bundle that includes an MSI B850 Gaming Plus WiFi motherboard and an MSI MAG Coreliquid A13 240 AIO liquid cooler."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/amazon-secretly-circumvents-community-vote-for-massive-ai-data-center-45-year-old-rules-lock-gilroy-residents-out-of-public-comment-window",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon circumvents community vote for massive AI data center using 45-year-old rules — Gilroy residents locked out of public comment window",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/amazon-secretly-circumvents-community-vote-for-massive-ai-data-center-45-year-old-rules-lock-gilroy-residents-out-of-public-comment-window",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T13:51:24+00:00",
    "summary": "Residents of Gilroy, California, were caught by surprise when an Amazon data center started construction in their city. Negotiations for the project started in 2020, with public comments open until 20"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/pulsar-feinmann-f01-noctua-edition-review",
    "domain": "AI 算力 / 半导体",
    "title": "Pulsar Feinmann F01 Noctua Edition Review: Extra cool",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/pulsar-feinmann-f01-noctua-edition-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T13:08:21+00:00",
    "summary": "The Pulsar Feinmann F01 Noctua Edition is a lightweight gaming mouse with a built-in fan for keeping your palm cool."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/chinas-memory-making-champion-smashes-ddr5-8800-barrier-on-amd-platform-cxmt-chips-close-the-gap-with-sk-hynix",
    "domain": "AI 算力 / 半导体",
    "title": "China's memory-making champion smashes DDR5-8800 barrier on AMD platform — CXMT chips close the gap with SK hynix",
    "url": "https://www.tomshardware.com/pc-components/ram/chinas-memory-making-champion-smashes-ddr5-8800-barrier-on-amd-platform-cxmt-chips-close-the-gap-with-sk-hynix",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T12:35:00+00:00",
    "summary": "Colorful shows off the overclocking potential on new memory kits equipped with CXMT integrated circuits."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/atari-st-public-floppy-database-now-open-for-everyone-online-archive-originally-designed-for-st-flash-cart-packed-with-classics-and-homebrew",
    "domain": "AI 算力 / 半导体",
    "title": "Atari ST Public Floppy Database now open for everyone — online archive originally designed for ST flash cart packed with classics and homebrew",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/atari-st-public-floppy-database-now-open-for-everyone-online-archive-originally-designed-for-st-flash-cart-packed-with-classics-and-homebrew",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T12:15:00+00:00",
    "summary": "An extensive Atari ST floppy disk database can now easily be accessed by all netizens."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/we-tested-the-impact-of-ssd-speed-on-gaming-performance-in-11-titles-we-analyzed-from-sata-to-pcie-5-0-to-see-whether-upgrading-to-a-faster-nvme-ssd-would-have-an-impact",
    "domain": "AI 算力 / 半导体",
    "title": "We tested the impact of SSD speed on gaming performance in 11 titles — we analyzed from SATA to PCIe 5.0 to see whether upgrading to a faster NVMe SSD would have an impact",
    "url": "https://www.tomshardware.com/pc-components/gpus/we-tested-the-impact-of-ssd-speed-on-gaming-performance-in-11-titles-we-analyzed-from-sata-to-pcie-5-0-to-see-whether-upgrading-to-a-faster-nvme-ssd-would-have-an-impact",
    "source": "Dan Mateescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T12:05:00+00:00",
    "summary": "We tested gaming performance with both NVMe and SATA SSDs across 11 games to determine if upgrading to a faster drive is worth it."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/space/intels-proposed-orbital-data-centers-would-manage-thousands-of-simple-leo-satellites-two-tier-network-puts-the-brains-of-satellite-constellations-in-higher-orbit",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's proposed orbital data centers would manage thousands of simple LEO satellites —two-tier network puts the brains of satellite constellations in higher orbit",
    "url": "https://www.tomshardware.com/tech-industry/space/intels-proposed-orbital-data-centers-would-manage-thousands-of-simple-leo-satellites-two-tier-network-puts-the-brains-of-satellite-constellations-in-higher-orbit",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T11:45:00+00:00",
    "summary": "Intel’s orbital data center architecture uses powerful higher-orbit satellites to manage LEO constellations, reducing reliance on terrestrial control centers."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/hardware-researcher-spins-up-cpu-deoptimization-project-to-find-the-slowest-machine-code-worst-offender-takes-198-billion-cycles-to-execute",
    "domain": "AI 算力 / 半导体",
    "title": "Hardware researcher spins up 'CPU deoptimization' project to find the slowest single x86 instruction, creates hall of shame — worst offender takes 198 billion cycles spanning 62 seconds to execute",
    "url": "https://www.tomshardware.com/pc-components/cpus/hardware-researcher-spins-up-cpu-deoptimization-project-to-find-the-slowest-machine-code-worst-offender-takes-198-billion-cycles-to-execute",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T11:20:00+00:00",
    "summary": "One hardware researcher, Christopher Domas (@xoreaxeaxeax on GitHub), is taking a different approach with the CPU Deoptimization leaderboard, which looks not to make Assembly instructions run as fast "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-creates-16-new-viruses-that-never-existed-in-nature-after-learning-dnas-pattern-from-9-trillion-nucleotides-experts-warn-such-applications-are-way-ahead-of-necessary-guardrails",
    "domain": "AI 算力 / 半导体",
    "title": "AI creates 16 new viruses that never existed in nature after learning DNA’s pattern from 9 trillion nucleotides — experts warn such applications are way ahead of necessary guardrails",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-creates-16-new-viruses-that-never-existed-in-nature-after-learning-dnas-pattern-from-9-trillion-nucleotides-experts-warn-such-applications-are-way-ahead-of-necessary-guardrails",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T11:00:00+00:00",
    "summary": "Researchers used Evo AI models trained on trillions of DNA building blocks to design entirely new viral genomes, 16 of which became viable bacteriophages capable of infecting and reproducing inside E."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/space/nasa-modded-space-stations-laptops-so-everyone-could-use-the-same-charger-standardizing-iss-chargers-eliminated-useless-weight-and-reduced-failure-points",
    "domain": "AI 算力 / 半导体",
    "title": "NASA modded space station's laptops so everyone could use the same charger — standardizing ISS chargers eliminated useless weight and reduced failure points",
    "url": "https://www.tomshardware.com/tech-industry/space/nasa-modded-space-stations-laptops-so-everyone-could-use-the-same-charger-standardizing-iss-chargers-eliminated-useless-weight-and-reduced-failure-points",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T10:30:00+00:00",
    "summary": "NASA ensured that all laptops destined for use in the International Space Station had the same 'cannon' power connector by implementing a modification."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/modder-turns-steam-controller-trackpad-haptics-into-stereo-speakers-with-custom-hid-tool-wired-connection-transmits-16-bit-audio-that-sounds-surprisingly-full",
    "domain": "AI 算力 / 半导体",
    "title": "Modder turns Steam Controller trackpad haptics into stereo speakers with custom HID tool — Wired connection transmits 16-bit audio that sounds surprisingly full",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/modder-turns-steam-controller-trackpad-haptics-into-stereo-speakers-with-custom-hid-tool-wired-connection-transmits-16-bit-audio-that-sounds-surprisingly-full",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T10:00:00+00:00",
    "summary": "A modder has figured out how to send an audio stream to the Steam Controller's haptic motors in order to make them play pretty much anything. While the wireless connection over the puck is limited, au"
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
    "points": 19,
    "published_at": "2026-07-27T14:33:53+00:00",
    "summary": ""
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
    "points": 860,
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
    "id": "hn:49220126",
    "domain": "大厂 AI 动态",
    "title": "DeepMind's WeatherNext model achieves breakthrough forecasting cyclones",
    "url": "https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/",
    "source": "bhavansig",
    "platform": "hackernews",
    "points": 441,
    "published_at": "2026-08-08T09:18:50+00:00",
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
    "points": 200,
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
    "points": 119,
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
    "id": "rss:https://www.theverge.com/entertainment/977190/no-dogs-in-space-music-history-podcast",
    "domain": "大厂 AI 动态",
    "title": "No Dogs in Space is a music history podcast for true obsessives",
    "url": "https://www.theverge.com/entertainment/977190/no-dogs-in-space-music-history-podcast",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T20:28:31+00:00",
    "summary": "Sadly, there hasn't been a new episode of No Dogs in Space since July of 2024. Part four of the podcast's series on Can wrapped up an abbreviated season three, which focused on experimental rock. Don'"
  },
  {
    "id": "rss:https://www.theverge.com/tech/977161/mark-zuckerberg-yacht-wilderness-legacy-stranded-boat",
    "domain": "大厂 AI 动态",
    "title": "Zuckerberg&#8217;s yacht was closer, but someone else saved a stranded boat",
    "url": "https://www.theverge.com/tech/977161/mark-zuckerberg-yacht-wilderness-legacy-stranded-boat",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T17:20:30+00:00",
    "summary": "Earlier this week, the Alaskan cruise ship Wilderness Legacy rescued a small skiff stranded near Farragut Bay after running out of fuel. But, according to tracking data reviewed by the Alaska Beacon a"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/977155/49ers-coach-tesla-autopilot-crash",
    "domain": "大厂 AI 动态",
    "title": "49ers coach says his Tesla was on Autopilot when he crashed",
    "url": "https://www.theverge.com/transportation/977155/49ers-coach-tesla-autopilot-crash",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T15:56:49+00:00",
    "summary": "Four weeks ago, San Francisco 49ers coach Kyle Shanahan was involved in an accident near downtown Palo Alto. At the time Shanahan said only that the accident was his fault. But during a recent press c"
  },
  {
    "id": "rss:https://www.theverge.com/tech/976092/pc-building-dropbox-backup",
    "domain": "大厂 AI 动态",
    "title": "Dropbox is a PC builder’s best friend",
    "url": "https://www.theverge.com/tech/976092/pc-building-dropbox-backup",
    "source": "TC. Sottek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T13:00:00+00:00",
    "summary": "In 2018 I bet my reputation and self-worth on a huge crowdfunded game design project. It could have been a failure for many reasons, but the one I became most worried about was losing all of the work "
  },
  {
    "id": "rss:https://www.theverge.com/column/976690/ai-writing-detectors-suspicion",
    "domain": "大厂 AI 动态",
    "title": "AI detectors are creating a new era of distrust",
    "url": "https://www.theverge.com/column/976690/ai-writing-detectors-suspicion",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T12:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more news about how AI is changing our daily lives, follow Emma Roth. The Stepback arrives in our s"
  },
  {
    "id": "rss:https://www.theverge.com/tech/977143/x-revenue-sharing-original-content-rewards",
    "domain": "大厂 AI 动态",
    "title": "X replaces its revenue-sharing program with ‘Original Content Rewards’",
    "url": "https://www.theverge.com/tech/977143/x-revenue-sharing-original-content-rewards",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T21:15:12+00:00",
    "summary": "X is ending its controversial revenue-sharing program for content creators, which has seen numerous revisions under Elon Musk's reign. In its place, it's launching a new Original Content Rewards progr"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/977124/amazon-data-center-worst-polluting-power-plant",
    "domain": "大厂 AI 动态",
    "title": "An Amazon data center could have the worst polluting power plant in the country",
    "url": "https://www.theverge.com/ai-artificial-intelligence/977124/amazon-data-center-worst-polluting-power-plant",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T17:53:34+00:00",
    "summary": "To power its new West Texas data center, Amazon is investing in the construction of a new power plant that could be one of the largest single producers of greenhouse gases in the US, according to the "
  },
  {
    "id": "rss:https://www.theverge.com/business/977112/buc-ees-john-oliver-lawsuit-beaver-mini-mart",
    "domain": "大厂 AI 动态",
    "title": "Buc-ee’s dodges John Oliver to sue another small business",
    "url": "https://www.theverge.com/business/977112/buc-ees-john-oliver-lawsuit-beaver-mini-mart",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T15:47:30+00:00",
    "summary": "Buc-ee's became something of a viral sensation during the World Cup, but it has a troubling history of suing small gas stations and convenience stores. On a recent episode of Last Week Tonight, John O"
  },
  {
    "id": "rss:https://www.theverge.com/report/976872/tom-vek-musician-entrepreneur-sleevenote-interview",
    "domain": "大厂 AI 动态",
    "title": "Musician and entrepreneur Tom Vek is building a digital music player, but don’t call it retro",
    "url": "https://www.theverge.com/report/976872/tom-vek-musician-entrepreneur-sleevenote-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T15:00:00+00:00",
    "summary": "Tom Vek burst onto the scene in 2005 with his album We Have Sound, which garnered a solid 7.6 from the tastemakers of the day over at Pitchfork. His undeniably catchy brand of dancy indietronica lande"
  },
  {
    "id": "rss:https://www.theverge.com/tech/977031/chuwi-unibook-laptop-intel-wildcat-lake-review",
    "domain": "大厂 AI 动态",
    "title": "Is this $450 laptop from an unknown brand too good to be true?",
    "url": "https://www.theverge.com/tech/977031/chuwi-unibook-laptop-intel-wildcat-lake-review",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T12:00:00+00:00",
    "summary": "Finding a good laptop under $500 was hard enough before RAMageddon. They nearly always had cheap hardware and underpowered, often outdated chips. That's what made the MacBook Neo so disruptive: It off"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/09/embattled-hedge-fund-situational-awareness-invests-400m-in-chip-startup-source-foundry/",
    "domain": "大厂 AI 动态",
    "title": "Embattled hedge fund Situational Awareness invests $400M in chip startup Source Foundry",
    "url": "https://techcrunch.com/2026/08/09/embattled-hedge-fund-situational-awareness-invests-400m-in-chip-startup-source-foundry/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T20:35:17+00:00",
    "summary": "The AI-focused hedge fund is still making some big bets."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/09/anthropic-is-turning-claude-codes-auto-mode-on-by-default/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic is turning Claude Code’s auto mode on by default",
    "url": "https://techcrunch.com/2026/08/09/anthropic-is-turning-claude-codes-auto-mode-on-by-default/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T19:20:32+00:00",
    "summary": "Programming with Claude Code will soon require even less human oversight."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/09/techcrunch-mobility-zoox-prepares-for-launch-and-ubers-av-empire/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: Zoox prepares for launch and Uber’s AV empire",
    "url": "https://techcrunch.com/2026/08/09/techcrunch-mobility-zoox-prepares-for-launch-and-ubers-av-empire/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T16:05:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, the role AI is playing in it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/09/historian-jill-lepore-says-the-tech-industry-is-led-by-bad-readers-who-are-undermining-democracy/",
    "domain": "大厂 AI 动态",
    "title": "Historian Jill Lepore says Silicon Valley misreads science fiction and undermines democracy",
    "url": "https://techcrunch.com/2026/08/09/historian-jill-lepore-says-the-tech-industry-is-led-by-bad-readers-who-are-undermining-democracy/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T15:00:00+00:00",
    "summary": "On the latest episode of Equity, we spoke to Jill Lepore about \"government by machines\" and why Elon Musk is a bad science fiction reader."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/09/the-ai-safety-test-is-becoming-a-safety-risk/",
    "domain": "大厂 AI 动态",
    "title": "The AI safety test is becoming a safety risk",
    "url": "https://techcrunch.com/2026/08/09/the-ai-safety-test-is-becoming-a-safety-risk/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T14:30:00+00:00",
    "summary": "AI agents are escaping cybersecurity testing environments and reaching real-world systems, raising questions about whether safety infrastructure, industry standards and regulation can keep pace with i"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/09/this-adversarial-pattern-can-prevent-surveillance-cameras-from-detecting-you/",
    "domain": "大厂 AI 动态",
    "title": "This ‘adversarial’ pattern can prevent surveillance cameras from detecting you",
    "url": "https://techcrunch.com/2026/08/09/this-adversarial-pattern-can-prevent-surveillance-cameras-from-detecting-you/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T14:00:00+00:00",
    "summary": "A security researcher has designed an algorithm that can create computer-generated patterns capable of hiding people, faces, and vehicles from detection by surveillance cameras."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/09/this-former-notorious-red-light-district-is-now-one-of-the-worlds-top-ai-hubs/",
    "domain": "大厂 AI 动态",
    "title": "This former notorious red-light district is now one of the world’s top AI hubs",
    "url": "https://techcrunch.com/2026/08/09/this-former-notorious-red-light-district-is-now-one-of-the-worlds-top-ai-hubs/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T13:00:00+00:00",
    "summary": "More than 20 years ago, King's Cross was one of the seediest area's in London. Now it's sprouting something new."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/08/planned-amazon-data-center-could-become-the-biggest-climate-polluter-in-the-u-s/",
    "domain": "大厂 AI 动态",
    "title": "Planned Amazon data center could become the biggest climate polluter in the U.S.",
    "url": "https://techcrunch.com/2026/08/08/planned-amazon-data-center-could-become-the-biggest-climate-polluter-in-the-u-s/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T21:24:02+00:00",
    "summary": "As part of a planned Texas data center, Amazon is investing in an on-site power plant that could reportedly become the largest source of climate pollution in the United States."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/08/openai-acquires-presentation-startup-nextslide/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI acquires presentation startup NextSlide",
    "url": "https://techcrunch.com/2026/08/08/openai-acquires-presentation-startup-nextslide/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T19:41:13+00:00",
    "summary": "NextSlide says its team members are now working on ChatGPT."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/08/x-replaces-misaligned-revenue-sharing-program-with-original-content-rewards/",
    "domain": "大厂 AI 动态",
    "title": "X replaces ‘misaligned’ revenue sharing program with Original Content Rewards",
    "url": "https://techcrunch.com/2026/08/08/x-replaces-misaligned-revenue-sharing-program-with-original-content-rewards/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T16:34:22+00:00",
    "summary": "X is winding down its existing Revenue Sharing program."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/08/the-kindle-scribe-colorsoft-is-a-lot-of-fun-but-its-not-a-must-have/",
    "domain": "大厂 AI 动态",
    "title": "The Kindle Scribe Colorsoft is a lot of fun, but it’s not a must-have",
    "url": "https://techcrunch.com/2026/08/08/the-kindle-scribe-colorsoft-is-a-lot-of-fun-but-its-not-a-must-have/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T16:00:00+00:00",
    "summary": "While the device is pretty and lightweight, it’s not something the everyday person needs due to its hefty price tag and size."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/08/googles-top-hacker-hunter-explains-why-hacking-groups-get-codenames/",
    "domain": "大厂 AI 动态",
    "title": "Google’s top hacker hunter explains why hacking groups get codenames",
    "url": "https://techcrunch.com/2026/08/08/googles-top-hacker-hunter-explains-why-hacking-groups-get-codenames/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T15:00:00+00:00",
    "summary": "Google recently changed how it refers and assigns names to hacking groups. TechCrunch spoke with one of the world’s foremost experts on tracking hackers to understand why companies give hackers codena"
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/mount-toba-eruption-doesnt-seem-like-it-could-nearly-kill-our-species/",
    "domain": "大厂 AI 动态",
    "title": "Mount Toba eruption doesn't seem like it could nearly kill our species",
    "url": "https://arstechnica.com/science/2026/08/mount-toba-eruption-doesnt-seem-like-it-could-nearly-kill-our-species/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T11:00:14+00:00",
    "summary": "The massive Toba eruption seems to have had little climate impact."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/the-first-self-driving-vehicle-on-mars-has-proven-to-be-a-smashing-success/",
    "domain": "大厂 AI 动态",
    "title": "The first self-driving vehicle on Mars has proven to be a smashing success",
    "url": "https://arstechnica.com/space/2026/08/the-first-self-driving-vehicle-on-mars-has-proven-to-be-a-smashing-success/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T11:30:48+00:00",
    "summary": "About 90 percent of the distance driven by Perseverance has been autonomous."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/deepminds-hurricane-model-bought-forecasters-an-extra-day/",
    "domain": "大厂 AI 动态",
    "title": "DeepMind’s hurricane breakthrough has surprised weather scientists",
    "url": "https://arstechnica.com/science/2026/08/deepminds-hurricane-model-bought-forecasters-an-extra-day/",
    "source": "Victoria Turk, wired.com",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T11:05:50+00:00",
    "summary": "Open source WeatherNext model can make accurate predictions with lower-resolution weather data."
  },
  {
    "id": "rss:https://www.producthunt.com/products/good-assistant",
    "domain": "大厂 AI 动态",
    "title": "Good Assistant 2",
    "url": "https://www.producthunt.com/products/good-assistant",
    "source": "Jensa Bačík",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T12:46:32+00:00",
    "summary": "Turn life goals into daily progress. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/grok",
    "domain": "大厂 AI 动态",
    "title": "Grok Imagine 2.0",
    "url": "https://www.producthunt.com/products/grok",
    "source": "Sachin Soundar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T09:43:19+00:00",
    "summary": "Next-gen AI image generator with segmentation editing. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/workflo-2",
    "domain": "大厂 AI 动态",
    "title": "Workflo",
    "url": "https://www.producthunt.com/products/workflo-2",
    "source": "Chirag Chopra",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T22:35:22+00:00",
    "summary": "Mac workspace automation that never sees your screen Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/soup-cli",
    "domain": "大厂 AI 动态",
    "title": "Soup CLI",
    "url": "https://www.producthunt.com/products/soup-cli",
    "source": "Alpamys Makazhan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T07:59:19+00:00",
    "summary": "Fine-tune an 8B LLM on a 4 GB laptop GPU Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/voiceos",
    "domain": "大厂 AI 动态",
    "title": "VoiceOS App Store",
    "url": "https://www.producthunt.com/products/voiceos",
    "source": "Gabe Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T22:42:33+00:00",
    "summary": "The app store for voice native apps that lives in your notch Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/duckdisk",
    "domain": "大厂 AI 动态",
    "title": "DuckDisk",
    "url": "https://www.producthunt.com/products/duckdisk",
    "source": "puppypi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T10:44:11+00:00",
    "summary": "Table-first storage analysis for Mac, cloud, and SSH Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/argos-2",
    "domain": "大厂 AI 动态",
    "title": "Argos",
    "url": "https://www.producthunt.com/products/argos-2",
    "source": "Arystan Tanekov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T23:41:16+00:00",
    "summary": "The AI that acts as you, right in your browser Discussion | Link"
  },
  {
    "id": "rss:https://sspai.com/post/113202",
    "domain": "大厂 AI 动态",
    "title": "我与Pixel 10 Pro的生活：写在Pixel 11系列手机发布前夕",
    "url": "https://sspai.com/post/113202",
    "source": "VHENSS",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T03:00:56+00:00",
    "summary": "喜欢，从来没有一个明确的定义。查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/113268",
    "domain": "大厂 AI 动态",
    "title": "派早报：央视曝光酒店评级标识消费陷阱",
    "url": "https://sspai.com/post/113268",
    "source": "少数派编辑部",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T23:08:03+00:00",
    "summary": "央视曝光酒店评级标识消费陷阱《时代》网站展示仅 AI 可见广告Edge 浏览器将禁用 Manifest V2 扩展油价上涨致美国混动车需求激增廉价手机壳存在毒性隐患美国调查中国 AI 企业使用海外英伟达芯片看看就行的小道消息少数派的近期动态你可能错过的好文章查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/113158",
    "domain": "大厂 AI 动态",
    "title": "我做了一个 Quote/0 看板，把 F1 赛程、积分和结果留在桌面",
    "url": "https://sspai.com/post/113158",
    "source": "Belcheck",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T07:00:00+00:00",
    "summary": "特别声明本文的项目构思、结构设计及相关素材整理均由人工完成。在产品开发与调试过程中，使用GPT-5.6Sol模型作为辅助工具，参与方案讨论、代码编写与问题排查。文章内容基于实际开发过程中的经验与记录， ...查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/112901",
    "domain": "大厂 AI 动态",
    "title": "就内容创作而言，说话还是替代不了打字",
    "url": "https://sspai.com/post/112901",
    "source": "AstrianZ",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T05:11:00+00:00",
    "summary": "创作本就不是一个「速度为先」的行为——而打字，本质上是一个思考的过程。查看全文"
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
    "id": "hn:49166182",
    "domain": "股票",
    "title": "Bending Spoons makes first post-IPO acquisition with $1.3B Airtable deal",
    "url": "https://live.euronext.com/en/financial-news/bending-spoons-makes-first-post-ipo-acquisition-13-billion-airtable-deal",
    "source": "riffraff",
    "platform": "hackernews",
    "points": 115,
    "published_at": "2026-08-04T09:27:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49151871",
    "domain": "股票",
    "title": "Situational Awareness and the Impending Stock Market Volatility",
    "url": "https://www.emergingtrajectories.com/lh/situational-awareness-bigger-picture/",
    "source": "cl42",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-08-03T06:17:53+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3779057",
    "domain": "股票",
    "title": "一周展望：黄金突破4300后迎接通胀考验",
    "url": "https://wallstreetcn.com/articles/3779057",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:31:48+00:00",
    "summary": "上周五非农数据爆冷之后，美元延续回落，黄金和美股周线大幅收高。\n美国7月非农岗位意外减少2.3万个，..."
  },
  {
    "id": "wscn:3779046",
    "domain": "股票",
    "title": "创业板跌超2%，医药、消费大涨，芯片算力集体下挫、寒武纪跌超6%，恒指、恒科指双双上涨",
    "url": "https://wallstreetcn.com/articles/3779046",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:02:55+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市超3400股飘红，上午半天成交1.75万亿。沪深两市半日成交额1.73万亿，较上个交易日放量580亿。板块方面，算力硬件产业链调整，CPO、玻璃基板、高速铜连接、服务器方向领跌；半导体、光伏、商业航天、稀土、6G概念股走弱。创新药、黄金、白酒、煤炭、零售、银行板块走强。"
  },
  {
    "id": "wscn:3779054",
    "domain": "股票",
    "title": "迅速切换！历史性“逼空周”之后，对冲基金又转向做空",
    "url": "https://wallstreetcn.com/articles/3779054",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T03:47:29+00:00",
    "summary": "空头逼仓刚平息，对冲基金旋即\"变脸\"——高盛最新Prime Brokerage周报显示，享受了一周反弹红利后，机构迅速重启做空，宏观产品做空卖出与做多买入之比高达2.2比1。金融股连续四周获净买入，能源股七连买戛然而止，市场情绪高度撕裂。本周CPI、PPI及逾千亿美元国债拍卖将接连来袭，多空博弈或再度白热化。"
  },
  {
    "id": "wscn:3779053",
    "domain": "股票",
    "title": "股票发行创纪录，高盛却看多标普冲8000：需求将持续压倒供给",
    "url": "https://wallstreetcn.com/articles/3779053",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T03:43:13+00:00",
    "summary": "标普500近期创下历史新高7757点，高盛合伙人John Flood表示标普指数还能冲8000。尽管2026年美股股权发行预计创纪录达7000亿美元，但该行认为，相对市值占比仅约1%，与历史均值持平；而年初至今回购授权已达9890亿美元，全年预计1.4万亿美元回购将持续压倒供给。"
  },
  {
    "id": "wscn:3777864",
    "domain": "股票",
    "title": "CXO夏季展望：三重利好景气上行，订单修复融资暴增",
    "url": "https://wallstreetcn.com/premium/articles/3777864?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T03:33:46+00:00",
    "summary": "2026年上半年，全球生物医药投融资同比增长58.5%至267.5亿美元，中国医疗健康领域一级市场融资同比飙升214%，CXO行业迎来\"水源回灌\"的系统性拐点。"
  },
  {
    "id": "wscn:3779052",
    "domain": "股票",
    "title": "韩股高开回落，KOSPI指数一度涨超2%，霍尔木兹谈判僵局推升油价",
    "url": "https://wallstreetcn.com/articles/3779052",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T03:31:32+00:00",
    "summary": "周一MSCI亚洲指数上涨0.8%，韩股高开回落，KOSPI盘中一度涨超2%，KOSDAQ一度触发熔断。与此同时，伊朗明确否认与美直接谈判，霍尔木兹僵局难解，布伦特原油延续涨势位于84美元上方，地缘风险仍高悬市场之上。"
  },
  {
    "id": "wscn:3779051",
    "domain": "股票",
    "title": "Sonnet 5.5大泄露！对标DeepSeek，新一代性价比之王",
    "url": "https://wallstreetcn.com/articles/3779051",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T03:27:16+00:00",
    "summary": "Anthropic即将推出内部代号“Fennec”的Claude Sonnet 5.5，传闻上下文窗口翻倍至200万Token，推理速度更快、智能体能力更强，综合性能逼近旗舰级Fable 5，定价却维持Sonnet档位。在DeepSeek掀起性价比浪潮后，这款模型或将成为中高端AI市场最强性价比竞争者。"
  },
  {
    "id": "wscn:3779045",
    "domain": "股票",
    "title": "单周再跌15%！摩根大通详解海力士：英伟达减配、半价折扣、回购等",
    "url": "https://wallstreetcn.com/articles/3779045",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T02:53:12+00:00",
    "summary": "SK海力士上周股价重挫15%，市场恐慌情绪蔓延——英伟达削减HBM采购、股东回报悬而未决、540亿韩元天量资本支出接连冲击投资者信心。但摩根大通逐一拆解传言：五折定价系误读、资本支出属既定计划、股东回报时间表已明显提前。分析师直言\"最坏时刻已过\"，目标价较现价仍有94%上行空间。"
  },
  {
    "id": "wscn:3779049",
    "domain": "股票",
    "title": "私募信贷风险暗涌：头部基金违约率创五年高位，软件贷款成最大隐忧",
    "url": "https://wallstreetcn.com/articles/3779049",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T02:25:48+00:00",
    "summary": "数据分析显示，Ares、Blackstone、Blue Owl、Golub旗下私募信贷基金违约率已升至五年高位，内部风险观察名单同步扩大，与管理人公开表态的乐观基调形成落差。软件公司贷款占基金组合逾20%，在AI冲击下成为最大潜在风险点。"
  },
  {
    "id": "wscn:3779048",
    "domain": "股票",
    "title": "摩根士丹利上调目标价近72%，智谱涨超4%",
    "url": "https://wallstreetcn.com/articles/3779048",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T02:25:42+00:00",
    "summary": "大摩将智谱目标价上调近72%至1700港元，理由是算力获取能力提升及新融资支持。同时表示，中国大模型行业商业化逻辑正从价格战转向依靠模型智能变现，行业生态比市场预期更健康。该行对MiniMax维持建设性观点但下调目标价至900港元，并继续看好阿里巴巴的全链条AI布局。"
  },
  {
    "id": "wscn:3779047",
    "domain": "股票",
    "title": "美国财政进入被动紧缩周期，黄金逻辑从“交易”转向“配置”",
    "url": "https://wallstreetcn.com/articles/3779047",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T02:23:06+00:00",
    "summary": "受短期财政空窗期及中期选举影响，美国财政正迈入被动紧缩周期，美元年内高点或已现。这加剧了市场对美元的长期不信任，促使央行等配置资金入场。黄金去杠杆已结束，投资逻辑从短期“交易”转向长期“配置”，下半年有望迎来“弱美元+强黄金”行情。"
  },
  {
    "id": "wscn:3779043",
    "domain": "股票",
    "title": "下一个航天大生意：清理太空垃圾？",
    "url": "https://wallstreetcn.com/articles/3779043",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T02:06:55+00:00",
    "summary": "近地轨道已追踪到近3万个人造物体，太空垃圾问题正从\"公地悲剧\"演变为百亿级商业赛道。Astroscale财年营收暴增142%，ClearSpace完成3000万美元融资，两家公司争相将碎片清除包装成太空\"4S店\"生意——但核心变量不是技术，而是监管：责任归属至今是法律灰色地带，政府合同仍是主要稳定收入来源。"
  },
  {
    "id": "wscn:3779040",
    "domain": "股票",
    "title": "从“即时满足”转向“目标驱动”，“减肥神药”重塑亚洲消费逻辑",
    "url": "https://wallstreetcn.com/articles/3779040",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T02:06:45+00:00",
    "summary": "GLP-1减重药正在悄然重写亚洲消费行业的底层规则。摩根大通最新调查显示，75%用户削减零食、84%抑制冲动消费、74%减少外卖——被侵蚀的不是某个品类，而是整条依赖\"即时欲望\"变现的消费链条。钱包未合拢，方向已转移：健身、蛋白补剂、医美等目标型消费悄然崛起。随着口服药物普及与国产化提速，估值分化或早于利润冲击到来。"
  },
  {
    "id": "wscn:3779013",
    "domain": "股票",
    "title": "23.9%！AI撑起中国出口第二曲线：7月贸易高增背后的价格革命",
    "url": "https://wallstreetcn.com/premium/articles/3779013?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T01:34:06+00:00",
    "summary": "7月份中国出口增速维持高位，AI产业链与价格溢价是核心驱动，但量价背离预示后续增速中枢将温和回落。"
  },
  {
    "id": "wscn:3779041",
    "domain": "股票",
    "title": "杠杆出清后，谁将引领AI新叙事？",
    "url": "https://wallstreetcn.com/articles/3779041",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T01:33:38+00:00",
    "summary": "广发证券认为，美股财报季后AI定价逻辑正从“惩罚CapEx”转向“奖励收入兑现”。但下一个矛盾已经浮现：美四大云CapEx增速预计从105%回落至2028年的9%，模型商和新云填补这一CapEx缺口的能力有限，而“模型训练模型”的RSI（递归超级智能）逻辑，被视为下一阶段算力需求与应用爆发的核心驱动。"
  },
  {
    "id": "wscn:3779050",
    "domain": "股票",
    "title": "技艺新篇 全新RM 64-01 Colnago陀飞轮腕表",
    "url": "https://wallstreetcn.com/articles/3779050",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T01:25:53+00:00",
    "summary": "Colnago——骑行领域稀有工艺与意大利匠心精神的象征\n一款承袭Colnago经典设计基因、尽显极..."
  },
  {
    "id": "wscn:3779039",
    "domain": "股票",
    "title": "上调盈利预测但下调目标价，摩根大通：铠侠的估值取决于“长协的可信度”",
    "url": "https://wallstreetcn.com/articles/3779039",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T01:24:05+00:00",
    "summary": "摩根大通上调铠侠FY2027至FY2029营业利润预测的同时，将目标价从15.5万日元下调至13万日元。核心矛盾在于：eSSD定价强劲支撑盈利改善，但铠侠股价已从高点暴跌56%，市场对长协能否真正稳定定价存疑。该行将目标P/E从11倍降至约9倍，表示估值重估需等待长协效果在实际业绩中得到验证。"
  },
  {
    "id": "wscn:3779037",
    "domain": "股票",
    "title": "硅基vs碳基、光vs存储、开源vs闭源--这是高盛顶级科技交易员最关注的10张图表",
    "url": "https://wallstreetcn.com/articles/3779037",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T00:39:54+00:00",
    "summary": "Callahan梳理出AI浪潮下三大结构性转变：智能体（硅基）流量超越人类（碳基）流量（机器人流量已占全网53%）；光学元器件大幅跑赢存储芯片（8月以来领先逾20个百分点）；开源模型以不足闭源8%的成本实现更优性能，直接冲击闭源商业模式。当前市场被定性为\"回归正常而非繁荣\"。"
  },
  {
    "id": "wscn:3779038",
    "domain": "股票",
    "title": "OpenAI曝光GPT-6！传10万亿参数，8月强行发布",
    "url": "https://wallstreetcn.com/articles/3779038",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T00:20:54+00:00",
    "summary": "OpenAI压着两张王牌：参数高达10万亿、堪称GPT-4五倍的GPT-6（Astra）即将亮相，年底还有\"史诗级巨兽\"Doug待发。Anthropic以Fable 5.1伏兵截击，谷歌Jeff Dean出走、哈萨比斯卸任，\"三巨头\"时代骤然落幕。大模型王座之争，8月见分晓。"
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
    "points": 178,
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
    "points": 38,
    "published_at": "2026-08-07T19:38:05+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.06584",
    "domain": "金融",
    "title": "Two Types of Tertiarization: Household Demand, Production Networks, and the Rise of Services",
    "url": "https://arxiv.org/abs/2608.06584",
    "source": "Li Gan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2608.06584v1 Announce Type: new Abstract: I measure whether the rise of services is ultimately supported by household consumption or by non-household demand through production networks, investme"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.06618",
    "domain": "金融",
    "title": "Beyond Co-Movement: Locality by Exposures Enables a Joint Factor-Graph Framework for Portfolio Diversification",
    "url": "https://arxiv.org/abs/2608.06618",
    "source": "Sara Chehab, Giorgos Iacovides, Parisa Yazdanparast, Danilo Mandic",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2608.06618v1 Announce Type: new Abstract: Current portfolio construction methods are either agnostic to the effects of idiosyncratic shocks (standard factor models) or to the latent data structu"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.06842",
    "domain": "金融",
    "title": "Tabular Foundation Models and the Unity of Economic Behaviour",
    "url": "https://arxiv.org/abs/2608.06842",
    "source": "Victor H. Aguiar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2608.06842v1 Announce Type: new Abstract: Economics uses different behavioural models for risk, time, losses, valuation, and social choice. I study a unified choice experiment in which the same "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.07251",
    "domain": "金融",
    "title": "Reading Copom's Tone: A Weighted LLM Framework for Hawkish-Dovish Sentiment, Forward Guidance, and Uncertainty",
    "url": "https://arxiv.org/abs/2608.07251",
    "source": "Gabriel de Macedo Santos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2608.07251v1 Announce Type: new Abstract: This paper documents an applied natural-language-processing framework for measuring the tone of Brazilian Monetary Policy Committee (Copom) statements. "
  },
  {
    "id": "rss:https://arxiv.org/abs/2211.13905",
    "domain": "金融",
    "title": "A Scalable Bilevel Framework for Renewable Energy Scheduling",
    "url": "https://arxiv.org/abs/2211.13905",
    "source": "Dongwei Zhao, Vladimir Dvorkin, Stefanos Delikaraoglou, Alberto J. Lamadrid L., Audun Botterud",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2211.13905v2 Announce Type: cross Abstract: Accommodating the uncertain and variable renewable energy sources (VRES) in electricity markets requires sophisticated and scalable tools to achieve m"
  },
  {
    "id": "rss:https://arxiv.org/abs/2501.18732",
    "domain": "金融",
    "title": "Optimizing Bidding Curves for Renewable Energy in Two-Settlement Electricity Markets",
    "url": "https://arxiv.org/abs/2501.18732",
    "source": "Dongwei Zhao, Stefanos Delikaraogloub, Vladimir Dvorkin Alberto J. Lamadrid L., Audun Botterud",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2501.18732v1 Announce Type: cross Abstract: Coordination of day-ahead and real-time electricity markets is imperative for cost-effective electricity supply and also to provide efficient incentiv"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.06528",
    "domain": "金融",
    "title": "Capacity Markets for Large Loads under Supply-Chain Constraints",
    "url": "https://arxiv.org/abs/2608.06528",
    "source": "Tong Liu, Jacob Mays",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2608.06528v1 Announce Type: cross Abstract: Motivated by the rapid growth of data centers, we develop a model to evaluate bringyour-own-capacity (BYOC) mandates and flexibility accreditation in "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.07011",
    "domain": "金融",
    "title": "Linguistic Pattern Based Optimization of Economic and Spatial Uniformity Criteria in Facility Layout Problems",
    "url": "https://arxiv.org/abs/2608.07011",
    "source": "Jerzy Grobelny, Rafa{\\l} Michalski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2608.07011v1 Announce Type: cross Abstract: This paper extends prior work on linguistic pattern based facility layout optimization by enhancing the LP Alinks framework with an explicit spatial u"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.07032",
    "domain": "金融",
    "title": "Certified High-Dimensional Wasserstein Robust Portfolio Optimization",
    "url": "https://arxiv.org/abs/2608.07032",
    "source": "Chung-Han Hsieh, Rong Gan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2608.07032v1 Announce Type: cross Abstract: We develop a certified, scalable approximation for high-dimensional Wasserstein distributionally robust portfolio optimization. For expected-utility m"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.07122",
    "domain": "金融",
    "title": "Lambda-quantiles under the microscope",
    "url": "https://arxiv.org/abs/2608.07122",
    "source": "Fabio Bellini, Felix-Benedikt Liebrich",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2608.07122v1 Announce Type: cross Abstract: We study Lambda-quantiles, a generalisation of classical quantiles in which the constant probability level $\\lambda \\in [0,1]$ is replaced by a functi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.07208",
    "domain": "金融",
    "title": "Measuring Concept Content in Text from LLM Activations: ESG Evidence from Concept Vectors and Linear Probes",
    "url": "https://arxiv.org/abs/2608.07208",
    "source": "Luc Hazenoot, Zhaochun Ren, Amirhossein Zohrehvand",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2608.07208v1 Announce Type: cross Abstract: Existing measures of how much a text is about a concept read the surface of the text: dictionary word shares, topic proportions, embedding similaritie"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.07400",
    "domain": "金融",
    "title": "FinRank: An Evidence-Grounded Benchmark for Financial Question Answering and Retrieval over SEC Filings",
    "url": "https://arxiv.org/abs/2608.07400",
    "source": "Sasan Mansouri, Daniel Saad, Mark Wahrenburg, Manu Weissel, Fabian Woebbeking",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2608.07400v1 Announce Type: cross Abstract: Financial question answering is typically evaluated by answer correctness, yet in SEC filings a plausible and even numerically correct answer can be g"
  },
  {
    "id": "rss:https://arxiv.org/abs/2408.03181",
    "domain": "金融",
    "title": "Correlation emergence in two coupled simulated limit order books",
    "url": "https://arxiv.org/abs/2408.03181",
    "source": "Dominic Bauer, Derick Diana, Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2408.03181v2 Announce Type: replace Abstract: We use random walks to simulate the fluid limit of two coupled diffusive limit order books to model correlation emergence. The model implements the "
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.17211",
    "domain": "金融",
    "title": "Evolutionary Factor Searching for Sparse Portfolio Optimization Using Large Language Models",
    "url": "https://arxiv.org/abs/2507.17211",
    "source": "Jiandong Chen, Haochen Luo, Yuan Zhang, Chen Liu, Qingfu Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2507.17211v2 Announce Type: replace Abstract: Sparse portfolio optimization is a fundamental yet challenging problem in quantitative finance. Traditional approaches often use static objectives a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.14154",
    "domain": "金融",
    "title": "How Innovation Shapes Financial Structure: The Moderating Role of Institutional Quality",
    "url": "https://arxiv.org/abs/2512.14154",
    "source": "Yimin Wu, Tomoo Kikuchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2512.14154v2 Announce Type: replace Abstract: This paper studies how the stock market---relative to the banking sector---responds to innovation by using a panel of 75 countries from 1982 to 2021"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.22476",
    "domain": "金融",
    "title": "AutoQuant: An Auditable Expert-System Framework for Execution-Constrained Auto-Tuning in Cryptocurrency Perpetual Futures",
    "url": "https://arxiv.org/abs/2512.22476",
    "source": "Kaihong Deng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2512.22476v3 Announce Type: replace Abstract: Backtests of cryptocurrency perpetual futures are sensitive to execution timing, funding alignment, trading costs, and reuse of evaluation windows d"
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.19388",
    "domain": "金融",
    "title": "Religious Mayors, School Appointments, and Teenage Pregnancy",
    "url": "https://arxiv.org/abs/2602.19388",
    "source": "Marcela Mello, Jo\\~ao Garcia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2602.19388v3 Announce Type: replace Abstract: When religious movements win executive office, they can use bureaucratic levers to reshape public services along doctrinal lines. Using a regression"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.13002",
    "domain": "金融",
    "title": "Shared Bidding Algorithms and Competition: Evidence from Electricity Markets",
    "url": "https://arxiv.org/abs/2607.13002",
    "source": "Nicolas Eschenbaum",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2607.13002v3 Announce Type: replace Abstract: Competing firms increasingly delegate market decisions to algorithms supplied by the same third-party providers. We study whether a shared algorithm"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.04925",
    "domain": "金融",
    "title": "From Long to Short: How Interest Rates Shape Life Insurance Markets",
    "url": "https://arxiv.org/abs/2608.04925",
    "source": "Ziang Li, Derek Wenning",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2608.04925v2 Announce Type: replace Abstract: This paper explores how financial institutions pass interest rate risk through to product markets using the life insurance industry as a setting. We"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.14976",
    "domain": "金融",
    "title": "Multi-regime Markov-switching models with time-varying transition probabilities: An application to U.S. Treasury yields",
    "url": "https://arxiv.org/abs/2605.14976",
    "source": "Samuel Mod\\'ee, Yushu Li, Sjur Westgaard, Stein Andreas Bethuelsen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2605.14976v2 Announce Type: replace-cross Abstract: This paper studies Markov-switching (MS) models with time-varying transition probabilities (TVTP) under various specifications of the transiti"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.27853",
    "domain": "金融",
    "title": "FinanceHarness: Autonomous Financial Deep Research Framework",
    "url": "https://arxiv.org/abs/2607.27853",
    "source": "Yijia Xiao, Rujun Han, Yanfei Chen, Zifeng Wang, Ke Jiang, Zhongying CuiZhu, Vishy Tirumalashetty, Wei Wang, Burak Gokturk, Tomas Pfister, Chen-Yu Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-10T04:00:00+00:00",
    "summary": "arXiv:2607.27853v2 Announce Type: replace-cross Abstract: Powered by advances in LLMs and autonomous agents, deep research has become one of the most widely adopted agentic products. However, most dee"
  },
  {
    "id": "hn:49214813",
    "domain": "金融",
    "title": "US Sold Euros to Save the Yen, Europe Found Out After",
    "url": "https://finance.yahoo.com/markets/currencies/articles/us-sold-euros-save-yen-033819315.html",
    "source": "amarcheschi",
    "platform": "hackernews",
    "points": 20,
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
    "points": 42,
    "published_at": "2026-08-04T19:18:35+00:00",
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
  }
]
```
