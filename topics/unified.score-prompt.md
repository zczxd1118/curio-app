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

- 今日日期：`2026-07-08`
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
  "date": "2026-07-08",
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
    "points": 3644014,
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
    "points": 1449837,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 940805,
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
    "points": 853007,
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
    "points": 777376,
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
    "points": 666440,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 558704,
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
    "points": 503554,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 380579,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 376436,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1GX9dYWEPw",
    "domain": "AI",
    "title": "我居然能在MC里玩到这么好玩的摸金服务器！",
    "url": "http://www.bilibili.com/video/av114108926068217",
    "source": "物骨",
    "platform": "bilibili",
    "points": 316634,
    "published_at": "2025-03-06T21:00:00+00:00",
    "summary": "视频内容均来自《LRL服务器》\n服务器游玩方式看评论区置顶\n无需正版，不卖数值，爆率嘎嘎高，不会跑路"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 176475,
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
    "points": 174126,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 159825,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 159045,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 150291,
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
    "points": 92460,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 76213,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73607,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 72641,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 62253,
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
    "points": 52860,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29917,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22609,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1JU7E6PEar",
    "domain": "AI",
    "title": "Cursor 已死？我为什么要退订 Cursor ？",
    "url": "http://www.bilibili.com/video/av116819553683121",
    "source": "小狗瑞恩Ryan",
    "platform": "bilibili",
    "points": 18276,
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
    "points": 17732,
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
    "points": 17347,
    "published_at": "2025-05-25T13:36:25+00:00",
    "summary": "文档：https://icnt94i5ctj4.feishu.cn/docx/ZkR3d1lfUosIFCx4qWJcI4QunY0\nshay大佬的HA SSE接入文档：https://bbs.hassbian.com/thread-29314-1-1.html"
  },
  {
    "id": "bvid:BV191TY6KEHk",
    "domain": "AI",
    "title": "【全500集】目前B站最全最细的AI Agent零基础全套教程（从入门到精通），5天从入门到精通AI Agent，学完即可就业！看完这一套Agent教程就够了！",
    "url": "http://www.bilibili.com/video/av116843192851440",
    "source": "Agent智能体-",
    "platform": "bilibili",
    "points": 14879,
    "published_at": "2026-07-01T06:09:09+00:00",
    "summary": "【全500集】目前B站最全最细的AI Agent零基础全套教程（从入门到精通），5天从入门到精通AI Agent，学完即可就业！看完这一套AI Agent教程就够了！"
  },
  {
    "id": "bvid:BV1CbvxBwEah",
    "domain": "AI",
    "title": "真的不用服务器！用Cloudflare Workers+D1轻松搭建网站！",
    "url": "http://www.bilibili.com/video/av115803408045159",
    "source": "软件工程师Tim",
    "platform": "bilibili",
    "points": 13298,
    "published_at": "2025-12-29T14:51:53+00:00",
    "summary": "本期影片分享一下如何利用cloudflare workers搭建网站，并且利用d1免费数据库，实现无服务器的一个带前后端功能的网站。也就是说，即使你没有服务器，也能够搭建一个属于自己的网站。比如我自己搭建的这个案例网站在线留言板。就是完全搭建在cloudflare workers上面的，里面有静态页面 也有动态api接口。都是部署在workers上面的，并且集成了它提供的数据库。\n\n\n#cloud"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 12753,
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
    "points": 12708,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV165dAYxEdD",
    "domain": "AI",
    "title": "只需几行代码用Java写一个MCP服务！从0到1开发MCP服务！",
    "url": "http://www.bilibili.com/video/av114306863598282",
    "source": "图灵诸葛官方号",
    "platform": "bilibili",
    "points": 12210,
    "published_at": "2025-04-09T07:43:00+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持~\r\n本视频配套资料戳这里获取→https://www.bilibili.com/read/cv38661345/\r\n【还可额外领取100w字Java面试宝典】"
  },
  {
    "id": "bvid:BV1P9jRzXEXU",
    "domain": "AI",
    "title": "godot+mcp等于事半功倍，分享godot mcp安装",
    "url": "http://www.bilibili.com/video/av114579896012926",
    "source": "丿依赖丿",
    "platform": "bilibili",
    "points": 11575,
    "published_at": "2025-05-27T13:00:18+00:00",
    "summary": "mcp+godot等于事半功倍，分享如何安装godot的mcp和一些mcp的心得使用，飞书地址https://rohq5ptvba.feishu.cn/docx/CTcBdR56doWfKIxdF76cdBFvn5g"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 10917,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1f7Ts6pEXa",
    "domain": "AI",
    "title": "【Claude Code】大白话保姆级安装全栈教程，从入门到精通，搞定所有开发场景，小白10分钟快速上手，全程干货无废话，存下吧！很难找到更全的！",
    "url": "http://www.bilibili.com/video/av116855188560042",
    "source": "码同学-",
    "platform": "bilibili",
    "points": 9932,
    "published_at": "2026-07-03T08:59:21+00:00",
    "summary": "【Claude Code】大白话保姆级安装全栈教程，从入门到精通，搞定所有开发场景，小白10分钟快速上手，全程干货无废话，存下吧！很难找到更全的！\n【视频配套籽料+问题解答】请看”平论区置顶”自取哦！！！\n视频制作不易，如果视频对你有用的话❤️请一键三莲【长按点赞】支持一下up哦，拜托，这对我真的很重要！"
  },
  {
    "id": "bvid:BV1WBTX6kE1B",
    "domain": "AI",
    "title": "【2026版】这绝对是B站唯一将Vibe Coding从入门到实战讲明白的教程，手把手带你从入门到代码实战开发，存下吧，比啃书好太多了！拿走不谢，允许白嫖！",
    "url": "http://www.bilibili.com/video/av116871663722218",
    "source": "码士集团-马小雪",
    "platform": "bilibili",
    "points": 9859,
    "published_at": "2026-07-06T06:47:51+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！ 【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9156,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV12ojm64EU6",
    "domain": "AI",
    "title": "🧲 Claude Code 工作流：长程任务的规划和执行利器 ⛓️",
    "url": "http://www.bilibili.com/video/av116800494767674",
    "source": "沧海九粟",
    "platform": "bilibili",
    "points": 9122,
    "published_at": "2026-06-24T00:00:00+00:00",
    "summary": "GAC 平台：https://gaccode.com/signup?ref=UWDADYQI\n官方文档：https://code.claude.com/docs/en/workflows\n状态栏技能：https://github.com/webup/skills-cc#-webup-statusline"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 8440,
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
    "points": 7510,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1UfTW6vEvT",
    "domain": "AI",
    "title": "6小时吃透Harness AI工程化编程｜ClaudeCode/Codex Vibe Coding 阿里企业 AI自动化实战，程序员AI编程开发效率提升十倍！",
    "url": "http://www.bilibili.com/video/av116855121385228",
    "source": "ai大模型应用开发实战",
    "platform": "bilibili",
    "points": 7254,
    "published_at": "2026-07-03T08:38:38+00:00",
    "summary": "课程资料→https://www.bilibili.com/read/cv49754608/?jump_opus=1"
  },
  {
    "id": "bvid:BV1vcKS67Ee8",
    "domain": "AI",
    "title": "【AI Coding】这绝对是你看过讲的最好的Vibe Coding企业级项目实战，从入门到进阶，30分钟速通Claude Code✚Codex✚Cursor",
    "url": "http://www.bilibili.com/video/av116832321209292",
    "source": "图灵学院官方",
    "platform": "bilibili",
    "points": 7179,
    "published_at": "2026-06-29T08:02:48+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6509,
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
    "points": 6420,
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based o"
  },
  {
    "id": "bvid:BV1g4MP6SEqJ",
    "domain": "AI",
    "title": "🚀Claude Code有后门？立即锁进Docker Sandboxes里！sbx完整实测：Claude Code、Codex、OpenCode安全隔离运行",
    "url": "http://www.bilibili.com/video/av116862151038488",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 5841,
    "published_at": "2026-07-04T14:23:41+00:00",
    "summary": "视频简介：\nClaude Code有后门？立即锁进Docker Sandboxes里！sbx完整实测：Claude Code、Codex、OpenCode如何安全隔离运行！防隐私泄露、防恶意Skill和MCP \n别再裸奔运行Claude Code了！我用Docker Sandboxes把Claude、Codex、OpenCode全锁进沙盒，实测能不能防隐私泄露和恶意MCP\nClaude Code、"
  },
  {
    "id": "bvid:BV1oqMt6FEj8",
    "domain": "AI",
    "title": "【2026最新Claude Code】Claude Code保姆级完整教程-Claude Code新手保姆级教程-最强AI助手！从入门到进阶【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av116877216980674",
    "source": "资深bug设计工程师",
    "platform": "bilibili",
    "points": 5654,
    "published_at": "2026-07-07T06:18:15+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1YWCgBfEdz",
    "domain": "AI",
    "title": "00_AI Agent for LabVIEW 全面教学：安装、配置、VI解析、代码生成，一次讲透！",
    "url": "http://www.bilibili.com/video/av115547740113313",
    "source": "仪酷智能",
    "platform": "bilibili",
    "points": 5537,
    "published_at": "2025-11-14T11:13:10+00:00",
    "summary": "本视频将从零开始，带你完整掌握 AI Agent for LabVIEW 工具包的使用方法。\n无论你是 LabVIEW 开发者、做自动化/视觉/测试测控的工程师，还是对大模型 + LabVIEW 的结合感兴趣，本期内容都非常值得收藏！\n🔧 本期内容概览\n1）如何下载与安装工具包\n官方下载方式（官网入口）\nVIPM 安装步骤与 64bit 版本注意事项\n\n2）API 接入配置\n支持多家大模型：阿里云"
  },
  {
    "id": "bvid:BV1SfKQ6LEnp",
    "domain": "AI",
    "title": "Cursor+Qoder+Trae三合一 一键续杯！",
    "url": "http://www.bilibili.com/video/av116834669959773",
    "source": "无忧小助手",
    "platform": "bilibili",
    "points": 4864,
    "published_at": "2026-06-29T17:54:50+00:00",
    "summary": "全网独家Cursor、Qoder、trae三合一一键续杯工具，Qoder、Trae切换账号不丢失上下文！"
  },
  {
    "id": "bvid:BV1jWcvzmEzc",
    "domain": "AI",
    "title": "Houdini干货|houdini自己的AI agent（agent工具推荐分享）",
    "url": "http://www.bilibili.com/video/av116057012505638",
    "source": "tiny涵",
    "platform": "bilibili",
    "points": 4787,
    "published_at": "2026-02-12T09:45:41+00:00",
    "summary": "原作者教程：https://www.bilibili.com/video/BV1pwcbzBEEh/?spm_id_from=333.1387.list.card_archive.click&amp;vd_source=da5aa377b2acefadd001ffd4902eca9b\n\nGithub download：https://github.com/Kazama-Suichiku/Houdi"
  },
  {
    "id": "bvid:BV13cmnBFEP9",
    "domain": "AI",
    "title": "Claude Code教程9：Claude Code与GitHub的高效联动",
    "url": "http://www.bilibili.com/video/av115689541077475",
    "source": "木乐乐的异想世界",
    "platform": "bilibili",
    "points": 4748,
    "published_at": "2025-12-09T12:17:23+00:00",
    "summary": "【Claude Code教程第9集中文翻译】Net Ninja带你解锁Claude Code与GitHub的高效联动！本集聚焦实用核心功能：无需复杂配置，在Claude聊天会话中即可设置GitHub集成——安装后自动创建两个关键GitHub Action：①自动审查拉取请求（PR）并给出精准反馈；②当仓库问题提及Claude时，自动在新功能分支处理该问题。注意：需先安装GitHub CLI（附官方"
  },
  {
    "id": "rss:https://www.eetimes.com/can-agentic-ai-solve-the-embedded-software-problem/",
    "domain": "AI 算力 / 半导体",
    "title": "Can Agentic AI Solve the Embedded Software Problem?",
    "url": "https://www.eetimes.com/can-agentic-ai-solve-the-embedded-software-problem/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T22:00:00+00:00",
    "summary": "Agents will also need CPU plus acceleration to run on edge devices, said Ambarella’s Muneyb Minhazuddin. The post Can Agentic AI Solve the Embedded Software Problem? appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/optimizing-electromechanical-hardware-for-extreme-defense-environments/",
    "domain": "AI 算力 / 半导体",
    "title": "Optimizing Electromechanical Hardware for Extreme Defense Environments",
    "url": "https://www.eetimes.com/optimizing-electromechanical-hardware-for-extreme-defense-environments/",
    "source": "Emily Newton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T17:00:00+00:00",
    "summary": "Commercial parts die fast in combat. See how advanced composites, coatings and MIL testing keep defense hardware alive under brutal stress. The post Optimizing Electromechanical Hardware for Extreme D"
  },
  {
    "id": "rss:https://www.eetimes.com/manufacturing-expands-in-june-amid-global-unrest/",
    "domain": "AI 算力 / 半导体",
    "title": "Manufacturing Expands in June Amid Global Unrest",
    "url": "https://www.eetimes.com/manufacturing-expands-in-june-amid-global-unrest/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T12:30:00+00:00",
    "summary": "U.S. manufacturing expanded in June, but Middle East conflict impacted raw materials. The post Manufacturing Expands in June Amid Global Unrest appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/esim-evolves-from-subscriber-identity-to-device-trust/",
    "domain": "AI 算力 / 半导体",
    "title": "eSIM Evolves from Subscriber Identity to Device Trust",
    "url": "https://www.eetimes.com/esim-evolves-from-subscriber-identity-to-device-trust/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T07:00:00+00:00",
    "summary": "eSIM turns SIMs into device trust anchors for IoT, cars and AI, letting fleets switch networks and stay secure remotely. The post eSIM Evolves from Subscriber Identity to Device Trust appeared first o"
  },
  {
    "id": "rss:https://www.eetimes.com/canadas-ai-ecosystem-needs-more-urgency/",
    "domain": "AI 算力 / 半导体",
    "title": "Canada’s AI Ecosystem Needs More Urgency",
    "url": "https://www.eetimes.com/canadas-ai-ecosystem-needs-more-urgency/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T22:00:00+00:00",
    "summary": "Canada has the AI talent. Now, it’s time to scale its domestic compute and sovereign hardware. The post Canada’s AI Ecosystem Needs More Urgency appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/mips-software-to-silicon-with-risc-v-interview-with-mips-physical-ai-is-agentic-ai-at-the-edge/",
    "domain": "AI 算力 / 半导体",
    "title": "MIPS on the RISC-V Shift: ‘Physical AI Is Agentic AI at the Edge’",
    "url": "https://www.eetimes.com/mips-software-to-silicon-with-risc-v-interview-with-mips-physical-ai-is-agentic-ai-at-the-edge/",
    "source": "EE Times Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T17:00:00+00:00",
    "summary": "MIPS bets RISC-V and ARC AI will power physical AI in cars and factory robots. Watch the interview and learn more. The post MIPS on the RISC-V Shift: &#8216;Physical AI Is Agentic AI at the Edge&#8217"
  },
  {
    "id": "rss:https://www.eetimes.com/voice-is-key-to-physical-ai-development-methods-need-to-catch-up/",
    "domain": "AI 算力 / 半导体",
    "title": "Voice Is Key to Physical AI; Development Methods Need to Catch Up",
    "url": "https://www.eetimes.com/voice-is-key-to-physical-ai-development-methods-need-to-catch-up/",
    "source": "Finnur Pind",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T12:41:56+00:00",
    "summary": "To solve far-field ASR challenges, physical AI needs acoustic reality, prompting engineers to use physics-based simulation. The post Voice Is Key to Physical AI; Development Methods Need to Catch Up a"
  },
  {
    "id": "rss:https://www.eetimes.com/kioxia-all-set-to-raise-the-nand-game-in-ai-ssds/",
    "domain": "AI 算力 / 半导体",
    "title": "Kioxia All Set to Raise the NAND Game in AI SSDs",
    "url": "https://www.eetimes.com/kioxia-all-set-to-raise-the-nand-game-in-ai-ssds/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T07:29:33+00:00",
    "summary": "Here is how the Japanese chipmaker is cashing in on NAND flash demand in data center SSDs. The post Kioxia All Set to Raise the NAND Game in AI SSDs appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/unannounced-nvidia-rtx-50-super-gpus-appear-in-seasonic-psu-calculator-unreleased-graphics-cards-shown-with-10-17-percent-higher-tgp-over-original-models",
    "domain": "AI 算力 / 半导体",
    "title": "Unannounced Nvidia RTX 50 Super GPUs appear in Seasonic PSU calculator — unreleased graphics cards shown with 10-17% higher TGP over original models",
    "url": "https://www.tomshardware.com/pc-components/gpus/unannounced-nvidia-rtx-50-super-gpus-appear-in-seasonic-psu-calculator-unreleased-graphics-cards-shown-with-10-17-percent-higher-tgp-over-original-models",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T21:34:05+00:00",
    "summary": "Total graphics power figures for Nvidia's unanounced, unreleased RTX 50 Super-series graphics cards have appeared in Seasonic's PSU capacity calculator, revealing potentially higher TGPs of those prod"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/power-and-water-lag-the-fabs-in-south-koreas-880-billion-chip-and-ai-plan",
    "domain": "AI 算力 / 半导体",
    "title": "South Korea's $880 billion chip and AI plan faces big power and water challenges — a single megacluster requires a quarter of Seoul's total power demand",
    "url": "https://www.tomshardware.com/tech-industry/power-and-water-lag-the-fabs-in-south-koreas-880-billion-chip-and-ai-plan",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T17:27:41+00:00",
    "summary": "The ₩1,350 trillion total combines a $520 billion semiconductor program with AI data center and robotics spending, mostly made up of corporate capex."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/chinese-memory-and-storage-firm-expected-to-post-more-than-60-000-percent-jump-in-profits-due-to-exploding-demand-lexar-owner-longsys-forecasts-nearly-usd1-5-billion-profit-for-1h26-compared-to-usd2-1-million-last-year",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese memory and storage firm expected to post more than 60,000% jump in profits due to exploding demand — Lexar owner Longsys forecasts nearly $1.5 billion profit for 1H26 compared to $2.1 million ",
    "url": "https://www.tomshardware.com/tech-industry/chinese-memory-and-storage-firm-expected-to-post-more-than-60-000-percent-jump-in-profits-due-to-exploding-demand-lexar-owner-longsys-forecasts-nearly-usd1-5-billion-profit-for-1h26-compared-to-usd2-1-million-last-year",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T16:13:09+00:00",
    "summary": "Chinese memory and storage manufacturer Longsys expects to post a massive increase in profits due to the AI-driven chip shortage."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-nearly-usd2-000-on-this-rtx-5090-oled-gaming-laptop-right-now-massive-discount-on-powerhouse-16-inch-lenovo-rig-with-240hz-refresh-rate-32gb-ddr5-ram-2tb-ssd-and-a-24-core-intel-cpu-all-for-usd3-199",
    "domain": "AI 算力 / 半导体",
    "title": "Save nearly $2,000 on this RTX 5090 OLED gaming laptop right now — massive discount on powerhouse 16-inch Lenovo rig with 240Hz refresh rate, 32GB DDR5 RAM, 2TB SSD, and a 24-core Intel CPU, all for $",
    "url": "https://www.tomshardware.com/pc-components/save-nearly-usd2-000-on-this-rtx-5090-oled-gaming-laptop-right-now-massive-discount-on-powerhouse-16-inch-lenovo-rig-with-240hz-refresh-rate-32gb-ddr5-ram-2tb-ssd-and-a-24-core-intel-cpu-all-for-usd3-199",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T14:52:28+00:00",
    "summary": "Grab this Lenovo Legion Pro 7i gaming laptop with an RTX 5090 for just $3,199 right now at B&amp;H Photo, saving you $1,800."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/avx-512-support-is-reportedly-returning-with-intels-next-gen-nova-lake-cpus-latest-linux-kernel-patches-reveal-p-cores-and-e-cores-will-gain-native-512-bit-execution",
    "domain": "AI 算力 / 半导体",
    "title": "AVX-512 support is reportedly returning with Intel's next-gen Nova Lake CPUs — Latest Linux kernel patches reveal P-cores and E-cores will gain native 512-bit execution",
    "url": "https://www.tomshardware.com/pc-components/cpus/avx-512-support-is-reportedly-returning-with-intels-next-gen-nova-lake-cpus-latest-linux-kernel-patches-reveal-p-cores-and-e-cores-will-gain-native-512-bit-execution",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T14:47:47+00:00",
    "summary": "It looks like Intel is adding back AVX-512 support to its client CPUs starting from the upcoming Nova Lake desktop lineup. Previously, we expected to see AVX-256 debut on a consumer family, allowing E"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/companies-are-now-using-automatic-windows-installers-to-display-adware-through-the-microsoft-store-when-you-install-new-hardware-customer-immediately-gets-mcafee-ads-on-their-pc-after-connecting-new-lg-monitor-heres-how-to-block-the-new-ads",
    "domain": "AI 算力 / 半导体",
    "title": "Companies are now using automatic Windows installers to display Adware through the Microsoft Store when you install new hardware — customer immediately gets McAfee ads on their PC after connecting new",
    "url": "https://www.tomshardware.com/software/windows/companies-are-now-using-automatic-windows-installers-to-display-adware-through-the-microsoft-store-when-you-install-new-hardware-customer-immediately-gets-mcafee-ads-on-their-pc-after-connecting-new-lg-monitor-heres-how-to-block-the-new-ads",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T14:46:20+00:00",
    "summary": "LG monitors apparently auto-install an app on your PC when you first connect them, all thanks to the Microsoft Store."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/playstation-disc-petition-approaches-200000-signatures",
    "domain": "AI 算力 / 半导体",
    "title": "PlayStation disc petition approaches 200,000 signatures as backlash grows over Sony's decision to stop producing new physical media — firm still plans to produce optical media for existing titles, but",
    "url": "https://www.tomshardware.com/video-games/playstation/playstation-disc-petition-approaches-200000-signatures",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T14:38:31+00:00",
    "summary": "A Change.org petition urging Sony to keep making physical PlayStation games has passed 172,000 signatures."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/steam-machines-with-the-red-line-of-death-get-a-simple-official-cure-clear-the-cmos-clearing-the-cmos-can-revive-flat-red-lining-cubes",
    "domain": "AI 算力 / 半导体",
    "title": "Steam Machines with the ‘Red Line of Death’ get a simple, official cure: Clear the CMOS — clearing the CMOS can revive flat(red)-lining cubes",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/steam-machines-with-the-red-line-of-death-get-a-simple-official-cure-clear-the-cmos-clearing-the-cmos-can-revive-flat-red-lining-cubes",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T12:55:43+00:00",
    "summary": "Valve’s official account on Reddit has responded to RLOD victims with simple step-by-step instructions to get any affected Steam Machine up and running again."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/uk-gives-data-centers-option-to-apply-for-national-importance-status-that-overrides-local-regulations-cuts-timeline-by-a-year-eligible-projects-to-bypass-local-councils-save-more-than-a-billion-dollars-in-nimby-fights",
    "domain": "AI 算力 / 半导体",
    "title": "UK gives data centers option to apply for 'national importance' status that overrides local regulations, cuts timeline by a year — eligible projects to bypass local councils, save more than a billion ",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/uk-gives-data-centers-option-to-apply-for-national-importance-status-that-overrides-local-regulations-cuts-timeline-by-a-year-eligible-projects-to-bypass-local-councils-save-more-than-a-billion-dollars-in-nimby-fights",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T12:34:12+00:00",
    "summary": "The British government ruled that nationally significant infrastructure projects, which include data centers, can bypass local council approvals. This move is expected to speed up developments by up t"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/snag-32gb-of-ddr5-memory-ryzen-7-9800x3d-and-gigabyte-x870e-motherboard-for-usd233-off-deal-includes-free-aio-in-a-four-item-combo-from-newegg",
    "domain": "AI 算力 / 半导体",
    "title": "Snag 32GB of DDR5 memory, Ryzen 7 9800X3D, and Gigabyte X870E motherboard for $233 off — deal includes 'free' AIO in a four-item combo from Newegg",
    "url": "https://www.tomshardware.com/pc-components/snag-32gb-of-ddr5-memory-ryzen-7-9800x3d-and-gigabyte-x870e-motherboard-for-usd233-off-deal-includes-free-aio-in-a-four-item-combo-from-newegg",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T12:01:22+00:00",
    "summary": "Missed Prime Day? You can still soften the blow of buying PC parts with this three-item AM5 Newegg combo - 32GB of DDR5, 9800X3D, Gigabyte X870E motherboard, and a free AIO to take the sting out of bu"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/pc-cases/corsair-2800x-rs-r-argb-micro-atx-pc-case-hands-on",
    "domain": "AI 算力 / 半导体",
    "title": "Hands-on with Corsair's 2800X RS-R ARGB Micro-ATX PC Case – smaller footprint, roomy internals, includes three fans",
    "url": "https://www.tomshardware.com/pc-components/pc-cases/corsair-2800x-rs-r-argb-micro-atx-pc-case-hands-on",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T12:00:00+00:00",
    "summary": "Corsair’s 2800X RS-R ARGB brings a compact MicroATX design with room for full-size hardware, strong cooling support, and three pre-installed ARGB fans. Priced under $90, it offers solid value for a sm"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/dev-ports-linux-to-ataris-notorious-jaguar-console-from-1993-the-first-64-bit-console-features-2mb-of-ram-13-3-mhz-cpu-and-tom-and-jerry-co-processors-the-jag-was-notoriously-difficult-to-program-and-flopped",
    "domain": "AI 算力 / 半导体",
    "title": "Dev ports Linux to Atari's notorious Jaguar console from 1993 — the first 64-bit console features 2MB of RAM, 13.3 MHz CPU, and Tom and Jerry co-processors; the Jag was notoriously difficult to progra",
    "url": "https://www.tomshardware.com/software/linux/dev-ports-linux-to-ataris-notorious-jaguar-console-from-1993-the-first-64-bit-console-features-2mb-of-ram-13-3-mhz-cpu-and-tom-and-jerry-co-processors-the-jag-was-notoriously-difficult-to-program-and-flopped",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T11:53:39+00:00",
    "summary": "A developer has ported Linux to the Atari Jaguar console. To succeed at the task, they had to overcome severe memory limits, the lack of an MMU, and face off against a handful of unusual hardware quir"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/network-switches/record-low-price-on-this-10-port-poe-switch-with-gigabit-speeds-and-up-to-60w-of-power-save-24-percent-usd38-for-ugreen-switch-that-unlocks-an-extra-eight-power-delivery-ports-for-cameras-and-wi-fi-extenders",
    "domain": "AI 算力 / 半导体",
    "title": "Record-low price on this 10-port PoE+ switch with gigabit speeds and up to 60W of power, save 24% — $38 for Ugreen switch that unlocks an extra eight power-delivery ports for cameras and Wi-Fi extende",
    "url": "https://www.tomshardware.com/networking/network-switches/record-low-price-on-this-10-port-poe-switch-with-gigabit-speeds-and-up-to-60w-of-power-save-24-percent-usd38-for-ugreen-switch-that-unlocks-an-extra-eight-power-delivery-ports-for-cameras-and-wi-fi-extenders",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T11:39:52+00:00",
    "summary": "This Ugreen 10-port unmanaged Ethernet switch is on sale for just $37.97 right now, delivering eight PoE+ ports for up to 60W of power delivery for cameras and WiFi extenders, along with two extra por"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/kioxia-and-sandisk-sample-worlds-densest-3d-nand-new-332-layer-beats-samsungs-400-layer-nand",
    "domain": "AI 算力 / 半导体",
    "title": "Kioxia and Sandisk sample world's densest 3D NAND — new 332-Layer beats Samsung’s 400-Layer NAND",
    "url": "https://www.tomshardware.com/pc-components/ssds/kioxia-and-sandisk-sample-worlds-densest-3d-nand-new-332-layer-beats-samsungs-400-layer-nand",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T11:10:00+00:00",
    "summary": "Kioxia, Sandisk begin to sample BiCS10 3D NAND: 332 active layers and over 29 Gb/mm2 areal capacity."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/unix-copyright-code-infringement-lawsuit-is-back-from-the-dead-ibm-still-under-fire-from-xinuos-about-2003-era-bytes",
    "domain": "AI 算力 / 半导体",
    "title": "Unix copyright code infringement lawsuit is back from the dead — IBM still under fire from Xinuos over 2003-era bytes",
    "url": "https://www.tomshardware.com/software/linux/unix-copyright-code-infringement-lawsuit-is-back-from-the-dead-ibm-still-under-fire-from-xinuos-about-2003-era-bytes",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T10:45:00+00:00",
    "summary": "Unix copyright code infringement back from the dead — IBM is still under fire from Xinuos about 2003-era bytes, with a hearing as recent as June 22."
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/modder-creates-8-192-core-gpu-at-home-out-of-risc-v-microcontrollers-full-graphics-card-will-draw-over-2-000-watts-of-power-requires-a-3d-printer-to-program",
    "domain": "AI 算力 / 半导体",
    "title": "Modder builds 8,192-core GPU at home out of RISC-V microcontrollers — full \"graphics card\" draws over 2,000 watts of power, requires a 3D printer to program",
    "url": "https://www.tomshardware.com/maker-stem/modder-creates-8-192-core-gpu-at-home-out-of-risc-v-microcontrollers-full-graphics-card-will-draw-over-2-000-watts-of-power-requires-a-3d-printer-to-program",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T10:20:00+00:00",
    "summary": "Well-known engineer Matthias Balwierz (aka Bitluni) designed and created an 8,192-core RISC-V GPU at home."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-patent-reveals-new-xbm-memory-architecture-that-ditches-hbms-costly-silicon-interposer-backend-transistor-dram-stack-uses-ucie-links-and-built-in-repair-to-ease-ais-memory-bottleneck",
    "domain": "AI 算力 / 半导体",
    "title": "Intel patent reveals new XBM memory architecture that ditches HBM's costly silicon interposer — backend-transistor DRAM stack uses UCIe links and built-in repair to ease AI's memory bottleneck",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-patent-reveals-new-xbm-memory-architecture-that-ditches-hbms-costly-silicon-interposer-backend-transistor-dram-stack-uses-ucie-links-and-built-in-repair-to-ease-ais-memory-bottleneck",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T10:00:00+00:00",
    "summary": "Intel’s XBM patent proposes an HBM alternative that uses backend-transistor DRAM, UCIe chiplet links, and repair logic to reduce packaging costs and complexity."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/samsungs-chip-division-expects-to-out-earn-its-entire-40-year-history-in-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung chip division's single-year profits beat its past 40 years of profits, combined, due to increased memory and storage prices — Samsung passes Nvidia to become most profitable company in the wor",
    "url": "https://www.tomshardware.com/tech-industry/samsungs-chip-division-expects-to-out-earn-its-entire-40-year-history-in-2026",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T09:30:00+00:00",
    "summary": "Brokerage consensus puts Samsung's full-year 2026 operating profit near 300 trillion won."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/china-made-cxmt-memory-now-supports-faster-speeds-on-msis-amd-motherboards-new-bios-adds-ddr5-8200-validation-on-dual-dimm-ddr5-7200-on-quad-dimm-models",
    "domain": "AI 算力 / 半导体",
    "title": "China-made CXMT memory now supports faster speeds on MSI's AMD motherboards — new BIOS adds DDR5-8200 validation on dual-DIMM, DDR5-7200 on quad-DIMM models",
    "url": "https://www.tomshardware.com/pc-components/ddr5/china-made-cxmt-memory-now-supports-faster-speeds-on-msis-amd-motherboards-new-bios-adds-ddr5-8200-validation-on-dual-dimm-ddr5-7200-on-quad-dimm-models",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T16:20:37+00:00",
    "summary": "MSI has officially validated region-bound Chinese RAM using CXMT modules to run at up to 8,200 MT/s on its AM5 motherboards. Models with two RAM slots can handle these high frequencies a bit better th"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/xbox/microsoft-resets-xbox-by-cutting-3-200-jobs-this-year-divesting-five-game-studios-firm-cites-margins-that-are-3-10x-lower-than-comparable-platform-and-publishing-businesses",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft 'resets' Xbox by cutting 3,200 jobs this year, divesting five game studios — firm cites 'margins that are 3-10x lower than comparable platform and publishing businesses'",
    "url": "https://www.tomshardware.com/video-games/xbox/microsoft-resets-xbox-by-cutting-3-200-jobs-this-year-divesting-five-game-studios-firm-cites-margins-that-are-3-10x-lower-than-comparable-platform-and-publishing-businesses",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T15:39:52+00:00",
    "summary": "Xbox CEO Asha Sharma announced that Microsoft's gaming division will cut 3,200 jobs throughout FY27 and is spinning out studios but not canceling any games."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/printers/raspberry-pi-powered-open-source-printer-earns-design-award-nomination-but-still-has-no-price-nine-months-after-reveal",
    "domain": "AI 算力 / 半导体",
    "title": "Working prototype of open-source printer that promises user-repairability and no subscriptions appears in first video — DRM-free 'Open Printer' inkjet still has no announced price, ship date, or print",
    "url": "https://www.tomshardware.com/peripherals/printers/raspberry-pi-powered-open-source-printer-earns-design-award-nomination-but-still-has-no-price-nine-months-after-reveal",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T15:30:17+00:00",
    "summary": "Open Tools, a Paris-based startup, has announced that its Open Printer has been nominated for two French Design Awards."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen AI Halo review: AMD builds a DGX Spark of its own",
    "url": "https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T15:00:15+00:00",
    "summary": "The Ryzen AI Halo is a turn-key AMD local AI box that’s backed up with first-party software support, handy utilities, and plenty of documentation for local AI explorers. But the performance and applic"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/you-can-now-use-your-sony-headphones-as-a-real-time-head-tracker-for-race-and-flight-simulators-on-pc-several-hundred-games-already-supported-enthusiast-creates-open-source-app-that-translates-live-sensor-data-into-in-game-camera-controls",
    "domain": "AI 算力 / 半导体",
    "title": "You can now use your Sony headphones as a free real-time head tracker for race and flight simulators on PC, several hundred games already supported — enthusiast creates open-source app that translates",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/you-can-now-use-your-sony-headphones-as-a-real-time-head-tracker-for-race-and-flight-simulators-on-pc-several-hundred-games-already-supported-enthusiast-creates-open-source-app-that-translates-live-sensor-data-into-in-game-camera-controls",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T14:36:21+00:00",
    "summary": "A new open-source app called Sony Head Tracker, developed by Nicholas Slattery, reads raw sensor data from Sony headphones and earbuds and converts them into something OpenTrack can understand. From t"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidias-kyber-rack-for-rubin-ultra-slips-to-2028",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Kyber rack for Rubin Ultra reportedly delayed to 2028, stopgap solution also axed due to customer pushback — Analyst firm SemiAnalysis says PCB midplane problems led to the delay [Updated]",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidias-kyber-rack-for-rubin-ultra-slips-to-2028",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T13:33:34+00:00",
    "summary": "Nvidia reportedly won't ship its Kyber NVL144 rack until 2028, a delay of more than 12 months."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/nvidia-and-intel-tout-chips-built-in-america-but-every-arizona-made-blackwell-die-is-still-packaged-in-taiwan",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia and Intel tout homegrown American chip supply chain prowess as country bolsters local production, but gaps remain — crucial Blackwell packaging steps remain offshore as projects grow in scope a",
    "url": "https://www.tomshardware.com/tech-industry/nvidia-and-intel-tout-chips-built-in-america-but-every-arizona-made-blackwell-die-is-still-packaged-in-taiwan",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T12:51:09+00:00",
    "summary": "America's AI supply chain now starts and ends in the U.S., while its most valuable middle steps remain entirely offshore until at least 2028."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/electric-drone-breaks-world-air-speed-record-at-434-mph-designed-for-anti-aircraft-interceptor-roles-german-firm-convincingly-smashed-the-official-409-mph-record-hopes-to-get-stamp-of-approval-from-guinness-soon",
    "domain": "AI 算力 / 半导体",
    "title": "Electric drone breaks world air speed record at 434 mph, designed for anti-aircraft interceptor roles — German firm convincingly smashed the official 409 mph record, hopes to get stamp of approval fro",
    "url": "https://www.tomshardware.com/tech-industry/drones/electric-drone-breaks-world-air-speed-record-at-434-mph-designed-for-anti-aircraft-interceptor-roles-german-firm-convincingly-smashed-the-official-409-mph-record-hopes-to-get-stamp-of-approval-from-guinness-soon",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T12:39:54+00:00",
    "summary": "Quantum Systems Group reckons it has broken the flight speed record for an electric drone. During internal testing last month the Munich-based firm recorded its Apex Recordhunter drone hitting a top s"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/chinas-huawei-to-enter-south-korean-ai-chip-market-with-new-atlas-superpods-clusters-pack-8-192-ascend-950-accelerators-per-deployment-reportedly-challenges-nvidia-dominance-with-tripled-inference-performance-of-h20-at-one-quarter-the-cost",
    "domain": "AI 算力 / 半导体",
    "title": "China’s Huawei to enter South Korean AI chip market with new Atlas SuperPods, clusters pack 8,192 Ascend 950 accelerators per deployment — reportedly challenges Nvidia dominance with 'tripled inferenc",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/chinas-huawei-to-enter-south-korean-ai-chip-market-with-new-atlas-superpods-clusters-pack-8-192-ascend-950-accelerators-per-deployment-reportedly-challenges-nvidia-dominance-with-tripled-inference-performance-of-h20-at-one-quarter-the-cost",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T12:31:48+00:00",
    "summary": "Huawei is reportedly preparing to enter South Korea's AI accelerator market with its Ascend 950 chips and Atlas 950 SuperPod, challenging Nvidia through aggressive pricing, amid a broader push to expa"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/score-a-massive-usd1-050-saving-on-this-rtx-5090-gaming-pc-thats-just-16-percent-more-than-the-gpus-standalone-price-right-now-epic-discount-secures-you-a-formidable-4k-gaming-rig-with-a-9800x3d-32gb-ddr5-and-a-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Score a massive $1,050 saving on this RTX 5090 gaming PC that's just 16% more than the GPU's standalone price right now — epic discount secures you a formidable 4K gaming rig with a 9800X3D, 32GB DDR5",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/score-a-massive-usd1-050-saving-on-this-rtx-5090-gaming-pc-thats-just-16-percent-more-than-the-gpus-standalone-price-right-now-epic-discount-secures-you-a-formidable-4k-gaming-rig-with-a-9800x3d-32gb-ddr5-and-a-2tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T11:45:52+00:00",
    "summary": "Save $1,050 on this epic ABS Kaze II Ruby gaming PC, fitted with a 9800X3D, RTX 5090, 32GB DDR5, and 2TB SSD for just $4,749.05 for a limited time only."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/steam-machine-interview-full-transcript-valve-engineers-discuss-usd1-049-pricing-compact-design-component-shortages-and-windows-support",
    "domain": "AI 算力 / 半导体",
    "title": "Steam Machine interview full transcript: Valve engineers discuss $1,049 pricing, compact design, component shortages, and Windows support",
    "url": "https://www.tomshardware.com/video-games/steam-machine-interview-full-transcript-valve-engineers-discuss-usd1-049-pricing-compact-design-component-shortages-and-windows-support",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T11:32:00+00:00",
    "summary": "Valve's Pierre-Loup Griffais and Yazan Aldehayyat talked to Tom's Hardware about the Steam Machine, it's pricing, engineering, and even Windows support."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/wisconsin-residents-file-class-action-lawsuit-against-microsofts-worlds-most-powerful-ai-data-center-due-to-data-center-noise-plaintiffs-also-mention-construction-noise-and-extreme-light-pollution-from-usd7-3-billion-facility",
    "domain": "AI 算力 / 半导体",
    "title": "Wisconsin residents file class-action lawsuit against Microsoft's 'world's most powerful AI data center' due to data center noise — plaintiffs also mention construction noise and extreme light polluti",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/wisconsin-residents-file-class-action-lawsuit-against-microsofts-worlds-most-powerful-ai-data-center-due-to-data-center-noise-plaintiffs-also-mention-construction-noise-and-extreme-light-pollution-from-usd7-3-billion-facility",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T11:00:00+00:00",
    "summary": "Wisconsin residents file class-action lawsuit against Microsoft due to data center noise — plaintiffs also mention construction noise and extreme light pollution"
  },
  {
    "id": "rss:https://www.eetimes.com/breakthrough-cnt-pellicles-deliver-66x-durability-and-sufficient-transmittance/",
    "domain": "AI 算力 / 半导体",
    "title": "Breakthrough CNT Pellicles Deliver 66x Durability and Sufficient Transmittance",
    "url": "https://www.eetimes.com/breakthrough-cnt-pellicles-deliver-66x-durability-and-sufficient-transmittance/",
    "source": "Lintec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T04:00:00+00:00",
    "summary": "Explore the latest breakthrough in CNT pellicles for EUV lithography: durability is up to 66 times higher, with less transmittance loss. The post Breakthrough CNT Pellicles Deliver 66x Durability and "
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
    "id": "rss:https://www.theverge.com/gadgets/962514/meta-privacy-light-tampering-smart-glasses-update",
    "domain": "大厂 AI 动态",
    "title": "Meta’s glasses will turn off the camera if you tamper with the privacy light",
    "url": "https://www.theverge.com/gadgets/962514/meta-privacy-light-tampering-smart-glasses-update",
    "source": "Victoria Song",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T23:55:19+00:00",
    "summary": "Amid public backlash over its smart glasses, Meta announced that it will be updating its glasses with a new feature that will disable the camera when it detects that someone has tampered with or destr"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/962382/netflix-season-two-viewrship-dropoff-beef-avatar-one-piece-tiktok",
    "domain": "大厂 AI 动态",
    "title": "Of course viewers are giving up on Netflix shows",
    "url": "https://www.theverge.com/entertainment/962382/netflix-season-two-viewrship-dropoff-beef-avatar-one-piece-tiktok",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T21:58:39+00:00",
    "summary": "Even though Netflix is the world's most popular paid streaming service, the company has been struggling to keep viewers watching its series after their first seasons. Beef - the streamer's anthology a"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/962528/netflix-digital-media-brands-streaming",
    "domain": "大厂 AI 动态",
    "title": "Netflix is about to host videos from BuzzFeed, Condé Nast, and other publishers",
    "url": "https://www.theverge.com/streaming/962528/netflix-digital-media-brands-streaming",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T21:37:19+00:00",
    "summary": "Starting on August 3rd, Netflix's streaming library will include video content from dozens of digital media brands including BuzzFeed, Cond&#233; Nast, Hearst Magazines, People Inc, and Tastemade. As "
  },
  {
    "id": "rss:https://www.theverge.com/tech/962485/meta-muse-image-ai-model-instagram",
    "domain": "大厂 AI 动态",
    "title": "Meta’s new Muse Image model can pull other Instagram users into AI photos",
    "url": "https://www.theverge.com/tech/962485/meta-muse-image-ai-model-instagram",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T20:31:58+00:00",
    "summary": "Meta is launching the first AI image generation model made by its Superintelligence Labs division. The Muse Image model now powers the image-making tools across the Meta AI app, Instagram, and WhatsAp"
  },
  {
    "id": "rss:https://www.theverge.com/tech/962415/x-video-editor-recycled-content",
    "domain": "大厂 AI 动态",
    "title": "X says top accounts steal videos from other users as it announces new video tools",
    "url": "https://www.theverge.com/tech/962415/x-video-editor-recycled-content",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T18:28:08+00:00",
    "summary": "Nikita Bier, X's head of product, said in a post on Monday that \"[m]any videos from top accounts are simply stolen from other users, sometimes 5 years after they originally went viral,\" while noting t"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/962187/amble-golf-cart-moon-buggy-ev-design-price-specs",
    "domain": "大厂 AI 动态",
    "title": "The ‘G-Wagen of golf carts’ could be the ideal second car",
    "url": "https://www.theverge.com/transportation/962187/amble-golf-cart-moon-buggy-ev-design-price-specs",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T17:52:51+00:00",
    "summary": "While the auto industry wrings its hands over the electric vehicle market, sweating details like aerodynamic efficiency and range anxiety, a new EV startup based in Lisbon, Portugal, is zagging in a d"
  },
  {
    "id": "rss:https://www.theverge.com/policy/962342/abc-fcc-the-view-free-speech",
    "domain": "大厂 AI 动态",
    "title": "ABC tells the government to get out of its newsrooms",
    "url": "https://www.theverge.com/policy/962342/abc-fcc-the-view-free-speech",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T17:47:38+00:00",
    "summary": "ABC is firing back at the Federal Communications Commission after the agency opened an investigation into The View's airtime of political candidates. In a letter to the FCC on Tuesday, ABC argues that"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/961978/anthropic-claude-cowork-mobile-web",
    "domain": "大厂 AI 动态",
    "title": "Anthropic is launching Claude Cowork on mobile and web",
    "url": "https://www.theverge.com/ai-artificial-intelligence/961978/anthropic-claude-cowork-mobile-web",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T17:46:59+00:00",
    "summary": "Starting Tuesday, Anthropic's Claude Cowork AI platform will be available on mobile and web for the first time. The expanded access is rolling out first to Max subscribers and coming to Claude users o"
  },
  {
    "id": "rss:https://www.theverge.com/tech/962313/made-by-google-pixel-11-launch-event",
    "domain": "大厂 AI 动态",
    "title": "Google announces Pixel 11 launch event in August",
    "url": "https://www.theverge.com/tech/962313/made-by-google-pixel-11-launch-event",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T17:22:48+00:00",
    "summary": "Google is hosting its next Made by Google launch event for Pixel hardware on August 12th in New York City, according to an invitation sent by Google to The Verge. Unusually, the event is taking place "
  },
  {
    "id": "rss:https://www.theverge.com/games/962223/doom-id-software-xbox-layoffs",
    "domain": "大厂 AI 动态",
    "title": "Doom developer id reportedly cut in half as part of Xbox layoffs",
    "url": "https://www.theverge.com/games/962223/doom-id-software-xbox-layoffs",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T16:09:48+00:00",
    "summary": "As part of the mass layoffs hitting Xbox, Doom developer id Software has laid off around 50 percent of its staff, according to Game Developer. One source claimed to the publication that the cuts equat"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/07/final-extension-startup-battlefield-australia-applications-now-close-july-20/",
    "domain": "大厂 AI 动态",
    "title": "Final extension: Startup Battlefield Australia applications now close July 20",
    "url": "https://techcrunch.com/2026/07/07/final-extension-startup-battlefield-australia-applications-now-close-july-20/",
    "source": "Isabelle Johannessen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T22:30:00+00:00",
    "summary": "If you're building something ambitious, this is a fast track to the people who can move your startup forward."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/07/meta-rolls-out-muse-a-new-ai-image-generator/",
    "domain": "大厂 AI 动态",
    "title": "Meta just launched a new AI generator, Muse Image, and users are already pushing back over use of their photos",
    "url": "https://techcrunch.com/2026/07/07/meta-rolls-out-muse-a-new-ai-image-generator/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T22:18:10+00:00",
    "summary": "The new image-generating model has numerous use cases, including advertising and decorating, and creator-based opportunities."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/07/why-the-rise-of-open-source-ai-isnt-hurting-anthropic-yet/",
    "domain": "大厂 AI 动态",
    "title": "Why the rise of open source AI isn’t hurting Anthropic … yet",
    "url": "https://techcrunch.com/2026/07/07/why-the-rise-of-open-source-ai-isnt-hurting-anthropic-yet/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T20:04:32+00:00",
    "summary": "Open source models’ success isn’t coming at the expense of frontier labs. Instead, they each seem to capture two phases of the same life cycle."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/07/microsoft-joins-ai-cost-cutting-trend-by-relying-more-on-its-own-models/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft joins AI cost-cutting trend by relying more on its own models",
    "url": "https://techcrunch.com/2026/07/07/microsoft-joins-ai-cost-cutting-trend-by-relying-more-on-its-own-models/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T19:58:20+00:00",
    "summary": "Microsoft is the latest Silicon Valley giant to cut back on its AI spending."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/07/discord-admits-ai-moderation-bug-wrongfully-banned-users-over-harmless-images/",
    "domain": "大厂 AI 动态",
    "title": "Discord admits AI moderation bug wrongfully banned users over harmless images",
    "url": "https://techcrunch.com/2026/07/07/discord-admits-ai-moderation-bug-wrongfully-banned-users-over-harmless-images/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T19:28:38+00:00",
    "summary": "The company confirmed that the issue had been affecting accounts since May, with an additional 200 users banned over the weekend before its team identified and fixed the problem."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/07/googles-pixel-event-is-set-for-august-12/",
    "domain": "大厂 AI 动态",
    "title": "Google’s Pixel event is set for August 12",
    "url": "https://techcrunch.com/2026/07/07/googles-pixel-event-is-set-for-august-12/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T18:38:29+00:00",
    "summary": "Google's upcoming event in August will introduce new Pixel devices."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/07/figma-acquires-team-behind-a-vibe-coding-app/",
    "domain": "大厂 AI 动态",
    "title": "Figma acquires team behind a vibe-coding app",
    "url": "https://techcrunch.com/2026/07/07/figma-acquires-team-behind-a-vibe-coding-app/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T18:37:01+00:00",
    "summary": "The Y Combinator-backed company started a vibe-coding platform and later built an agent-creation product."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/07/netflix-dabbles-in-shorter-video-content-with-its-new-set-of-publisher-deals-with-variety-others/",
    "domain": "大厂 AI 动态",
    "title": "Netflix dabbles in shorter video content with its new set of publisher deals with Variety, others",
    "url": "https://techcrunch.com/2026/07/07/netflix-dabbles-in-shorter-video-content-with-its-new-set-of-publisher-deals-with-variety-others/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T17:24:35+00:00",
    "summary": "Netflix is bringing 2- to 20-minute videos to its platform through new partnerships with digital publishers, including Rolling Stone and Variety."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/07/the-worst-hacks-and-breaches-of-2026-so-far/",
    "domain": "大厂 AI 动态",
    "title": "Hacked, leaked, and held for ransom: The worst breaches of 2026 so far",
    "url": "https://techcrunch.com/2026/07/07/the-worst-hacks-and-breaches-of-2026-so-far/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T16:45:00+00:00",
    "summary": "From a massive DOGE data breach and the hacking of critical energy and water systems to the hack of an FBI surveillance system, here are the most damaging security incidents and data breaches of 2026."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/",
    "domain": "大厂 AI 动态",
    "title": "Claude Cowork expands to mobile and web",
    "url": "https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T16:27:18+00:00",
    "summary": "With this update, users can start a task from their desk, get status updates on their phone, and pick up the finished output later — even if their laptop is closed."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/07/x-adds-a-video-editor-to-encourage-creators-to-post-original-content-not-stolen-reposts/",
    "domain": "大厂 AI 动态",
    "title": "X adds a video editor to encourage creators to post original content, not stolen reposts",
    "url": "https://techcrunch.com/2026/07/07/x-adds-a-video-editor-to-encourage-creators-to-post-original-content-not-stolen-reposts/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T15:19:33+00:00",
    "summary": "X is rolling out a new video editor and recorder for iOS with multilingual captions, green-screen effects, and other editing tools."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/07/chemistry-ventures-is-raising-500m-for-its-second-fund/",
    "domain": "大厂 AI 动态",
    "title": "VC firm Chemistry is raising $500M for its second fund",
    "url": "https://techcrunch.com/2026/07/07/chemistry-ventures-is-raising-500m-for-its-second-fund/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T15:02:02+00:00",
    "summary": "Chemistry Ventures, the VC firm launched by Bessemer, Index Ventures, and Andreessen Horowitz alums, is raising $500M for its second fund."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/07/ai-law-startup-norm-raises-120m-hits-unicorn-valuation/",
    "domain": "大厂 AI 动态",
    "title": "AI law startup Norm raises $120M, hits unicorn valuation",
    "url": "https://techcrunch.com/2026/07/07/ai-law-startup-norm-raises-120m-hits-unicorn-valuation/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T14:35:42+00:00",
    "summary": "AI law startup Norm has raised a $120 million Series C round led by Khosla Ventures, valuing the startup at $1.2 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/07/this-startup-is-pitting-dealerships-against-each-other-to-bid-on-your-used-car/",
    "domain": "大厂 AI 动态",
    "title": "This startup pits dealerships against each other to bid on your used car",
    "url": "https://techcrunch.com/2026/07/07/this-startup-is-pitting-dealerships-against-each-other-to-bid-on-your-used-car/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T14:00:00+00:00",
    "summary": "Bidbus, which lets dealerships bid on used cars, has raised $15 million in a Series A round that was led by early-stage mobility fund Ibex Investors."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/07/hacktivists-call-out-trump-by-hacking-and-defacing-us-army-websites/",
    "domain": "大厂 AI 动态",
    "title": "Hacktivists call out Trump by hacking and defacing US Army websites",
    "url": "https://techcrunch.com/2026/07/07/hacktivists-call-out-trump-by-hacking-and-defacing-us-army-websites/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T13:10:00+00:00",
    "summary": "The U.S. Army has fixed two of its websites that were hacked to display messages calling President Trump a \"pedophile\" and a \"thief.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/07/savis-app-aims-to-protect-consumers-from-realistic-ai-scams-like-kidnappers-demanding-ransom/",
    "domain": "大厂 AI 动态",
    "title": "Savi’s app aims to protect consumers from realistic AI scams like kidnappers demanding ransom",
    "url": "https://techcrunch.com/2026/07/07/savis-app-aims-to-protect-consumers-from-realistic-ai-scams-like-kidnappers-demanding-ransom/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T12:00:00+00:00",
    "summary": "The company just raised $7 million in seed funding, and is launching its app for iPhone and Android on Tuesday."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/07/the-first-american-autonomous-ground-vehicles-are-fighting-in-ukraine/",
    "domain": "大厂 AI 动态",
    "title": "The first American autonomous ground vehicles are fighting in Ukraine",
    "url": "https://techcrunch.com/2026/07/07/the-first-american-autonomous-ground-vehicles-are-fighting-in-ukraine/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T09:00:00+00:00",
    "summary": "Forterra has deployed more than 100 of its self-driving ATVs in conflict zones in Ukraine."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/netflix-invented-binge-watching-now-it-may-have-outgrown-it/",
    "domain": "大厂 AI 动态",
    "title": "Netflix invented binge-watching. Now it may have outgrown it.",
    "url": "https://techcrunch.com/2026/07/06/netflix-invented-binge-watching-now-it-may-have-outgrown-it/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T00:47:33+00:00",
    "summary": "A new report suggests Netflix viewers aren’t sticking around for Season 2. The bigger issue may be that binge-watching itself is no longer the advantage it once was."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/the-first-ai-run-ransomware-attack-still-needed-a-human/",
    "domain": "大厂 AI 动态",
    "title": "The ‘first’ AI-run ransomware attack still needed a human",
    "url": "https://techcrunch.com/2026/07/06/the-first-ai-run-ransomware-attack-still-needed-a-human/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T23:56:14+00:00",
    "summary": "An AI agent carried out the technical execution of a real-world ransomware attack for the first known time, but new details show a human still chose the victim, set up the infrastructure, and supplied"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/06/us-investors-will-soon-get-access-to-sk-hynix-another-memory-maker-riding-the-ai-boom/",
    "domain": "大厂 AI 动态",
    "title": "US investors will soon get access to SK Hynix, another memory maker riding the AI boom",
    "url": "https://techcrunch.com/2026/07/06/us-investors-will-soon-get-access-to-sk-hynix-another-memory-maker-riding-the-ai-boom/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T23:21:03+00:00",
    "summary": "SK Hynix is experiencing a boom credited to AI. It will ride that to a multibillion-dollar U.S. IPO, expected to take place on Friday."
  },
  {
    "id": "rss:https://stratechery.com/2026/a-script-for-mark-zuckerberg/",
    "domain": "大厂 AI 动态",
    "title": "A Script for Mark Zuckerberg",
    "url": "https://stratechery.com/2026/a-script-for-mark-zuckerberg/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T10:00:00+00:00",
    "summary": "A script for what Mark Zuckerberg should say on Meta's next earnings call."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/michigan-sees-explosive-outbreak-of-diarrheal-parasite-with-over-700-cases/",
    "domain": "大厂 AI 动态",
    "title": "Michigan sees explosive outbreak of diarrheal parasite with over 700 cases",
    "url": "https://arstechnica.com/health/2026/07/michigan-sees-explosive-outbreak-of-diarrheal-parasite-with-over-700-cases/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T22:29:00+00:00",
    "summary": "Cases have risen quickly as officials are working to identify a common source."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/us-manufacturers-energy-costs-soar-because-of-ai-data-center-demand/",
    "domain": "大厂 AI 动态",
    "title": "Data centers’ energy demand threatens Trump’s “Made in America” plan",
    "url": "https://arstechnica.com/tech-policy/2026/07/us-manufacturers-energy-costs-soar-because-of-ai-data-center-demand/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T21:03:07+00:00",
    "summary": "Squeeze on Rust Belt electricity bills threatens Trump’s manufacturing plan."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/surprisingly-large-number-of-people-may-have-marker-for-tick-linked-meat-allergy/",
    "domain": "大厂 AI 动态",
    "title": "Surprisingly large number of people may have marker for tick-linked meat allergy",
    "url": "https://arstechnica.com/health/2026/07/surprisingly-large-number-of-people-may-have-marker-for-tick-linked-meat-allergy/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T20:32:39+00:00",
    "summary": "There's still a slew of questions about why some people develop alpha-gal syndrome."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/supreme-court-lets-texas-enforce-age-verification-law-on-app-stores/",
    "domain": "大厂 AI 动态",
    "title": "SCOTUS lets Texas enforce app store law that Big Tech calls \"censorship regime\"",
    "url": "https://arstechnica.com/tech-policy/2026/07/supreme-court-lets-texas-enforce-age-verification-law-on-app-stores/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T20:18:24+00:00",
    "summary": "Texas win at 5th Circuit left in place as attempts to overturn age law continue."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/07/bethesda-id-software-reportedly-hit-hard-by-microsoft-layoffs/",
    "domain": "大厂 AI 动态",
    "title": "Bethesda, id Software reportedly hit hard by Microsoft layoffs",
    "url": "https://arstechnica.com/gaming/2026/07/bethesda-id-software-reportedly-hit-hard-by-microsoft-layoffs/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T19:52:59+00:00",
    "summary": "As much as 50 percent of some teams affected by reductions, and more could be coming."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/googles-pixel-11-launch-event-is-set-for-august-12-with-possible-price-increases/",
    "domain": "大厂 AI 动态",
    "title": "Google's Pixel 11 launch event is set for August 12, with possible price increases",
    "url": "https://arstechnica.com/gadgets/2026/07/googles-pixel-11-launch-event-is-set-for-august-12-with-possible-price-increases/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T19:08:34+00:00",
    "summary": "Google's new phones could feature glowing LEDs and higher price tags."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/the-weather-channels-streaming-app-gets-a-67-percent-price-hike/",
    "domain": "大厂 AI 动态",
    "title": "The Weather Channel increases streaming subscription prices by up to $20",
    "url": "https://arstechnica.com/gadgets/2026/07/the-weather-channels-streaming-app-gets-a-67-percent-price-hike/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T18:29:24+00:00",
    "summary": "Livestreaming the channel through its app now starts at $5 per month."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/07/the-nintendo-switchs-days-are-numbered-but-what-is-that-number/",
    "domain": "大厂 AI 动态",
    "title": "The Nintendo Switch's days are numbered—but what is that number?",
    "url": "https://arstechnica.com/gaming/2026/07/the-nintendo-switchs-days-are-numbered-but-what-is-that-number/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T18:16:29+00:00",
    "summary": "Ars analysis suggests the 9-year-old console could keep selling for years."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/07/this-race-car-is-made-from-plant-fibers-volcanoes-and-seawater/",
    "domain": "大厂 AI 动态",
    "title": "This race car is made from plant fibers, volcanoes, ... and seawater?",
    "url": "https://arstechnica.com/cars/2026/07/this-race-car-is-made-from-plant-fibers-volcanoes-and-seawater/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T16:45:18+00:00",
    "summary": "The T70S can be eligible for racing events or built to be road-legal."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/facing-us-export-controls-chinas-deepseek-plans-to-make-its-own-chips/",
    "domain": "大厂 AI 动态",
    "title": "Facing US export controls, China's DeepSeek plans to make its own chips",
    "url": "https://arstechnica.com/ai/2026/07/facing-us-export-controls-chinas-deepseek-plans-to-make-its-own-chips/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T16:14:53+00:00",
    "summary": "It's early, but the plan is to reduce dependency on Nvidia and Huawei."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/dragonflies-maneuver-like-fighter-pilots/",
    "domain": "大厂 AI 动态",
    "title": "Dragonflies maneuver like fighter pilots",
    "url": "https://arstechnica.com/science/2026/07/dragonflies-maneuver-like-fighter-pilots/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T15:54:18+00:00",
    "summary": "Male dragonflies' dramatic aerial combat maneuvers emerge from relatively simple vision-based rules."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/new-virus-catalog-reveals-which-pathogens-pose-the-greatest-threat/",
    "domain": "大厂 AI 动态",
    "title": "New virus catalog reveals which pathogens pose the greatest threat",
    "url": "https://arstechnica.com/health/2026/07/new-virus-catalog-reveals-which-pathogens-pose-the-greatest-threat/",
    "source": "Mark Woolhouse",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T13:15:49+00:00",
    "summary": "The data can help predict what a future pandemic virus might look like."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/after-a-stellar-career-ulas-atlas-v-rocket-last-act-is-waiting-on-starliner/",
    "domain": "大厂 AI 动态",
    "title": "ULA's last six Atlas Vs can't launch anything besides Boeing's Starliner",
    "url": "https://arstechnica.com/space/2026/07/after-a-stellar-career-ulas-atlas-v-rocket-last-act-is-waiting-on-starliner/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T11:15:15+00:00",
    "summary": "Amazon says it has enough satellites in orbit to begin initial broadband service at mid-latitudes later this year."
  },
  {
    "id": "rss:https://arstechnica.com/features/2026/07/robot-workers-rising-how-ai-may-drive-general-purpose-autonomy-in-robotics/",
    "domain": "大厂 AI 动态",
    "title": "How AI could enable autonomous robot workers in workplaces—and maybe homes",
    "url": "https://arstechnica.com/features/2026/07/robot-workers-rising-how-ai-may-drive-general-purpose-autonomy-in-robotics/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-07T11:00:18+00:00",
    "summary": "Top robotics researchers and founders explain how robot autonomy is evolving."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/fcc-to-end-biden-era-rule-that-forces-isps-to-list-all-their-fees/",
    "domain": "大厂 AI 动态",
    "title": "FCC to end Biden-era rule that forces ISPs to list all their fees",
    "url": "https://arstechnica.com/tech-policy/2026/07/fcc-to-end-biden-era-rule-that-forces-isps-to-list-all-their-fees/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T21:13:37+00:00",
    "summary": "FCC to let ISPs stop listing all passthrough fees, give single \"up to\" price."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/kremlin-suspected-of-flying-drones-over-europe-using-russian-shadow-fleet/",
    "domain": "大厂 AI 动态",
    "title": "Kremlin suspected of flying drones over Europe using Russian shadow fleet",
    "url": "https://arstechnica.com/gadgets/2026/07/kremlin-suspected-of-flying-drones-over-europe-using-russian-shadow-fleet/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T20:52:42+00:00",
    "summary": "Drone intruders that possibly flew from Russian ships showed Europe isn’t ready."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/whats-the-oldest-americana-flown-in-space/",
    "domain": "大厂 AI 动态",
    "title": "What is the oldest American object ever launched into space?",
    "url": "https://arstechnica.com/space/2026/07/whats-the-oldest-americana-flown-in-space/",
    "source": "Robert Pearlman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T19:57:56+00:00",
    "summary": "From a Revolutionary War flag to the Statue of Liberty..."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/nuclear-regulatory-commission-plans-really-minor-changes-to-safety-regs/",
    "domain": "大厂 AI 动态",
    "title": "NRC is (sort of) getting rid of \"as low as reasonably achievable\" standard",
    "url": "https://arstechnica.com/science/2026/07/nuclear-regulatory-commission-plans-really-minor-changes-to-safety-regs/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T17:48:45+00:00",
    "summary": "Its issues with current nuclear safety standards are termed semantic, not physical."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/katalysts-satellite-rescue-mission-is-now-in-pursuit-of-nasas-swift/",
    "domain": "大厂 AI 动态",
    "title": "Katalyst's satellite rescue mission is now in pursuit of NASA's Swift",
    "url": "https://arstechnica.com/space/2026/07/katalysts-satellite-rescue-mission-is-now-in-pursuit-of-nasas-swift/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-06T17:14:09+00:00",
    "summary": "It will take several weeks for the Link spacecraft to rendezvous with NASA's Swift observatory."
  },
  {
    "id": "wscn:3776441",
    "domain": "股票",
    "title": "韩国股市逼近技术性熊市，监管紧急开会：半导体板块过度集中加剧市场波动",
    "url": "https://wallstreetcn.com/articles/3776441",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T05:50:18+00:00",
    "summary": "韩国KOSPI从历史高点跌幅一度触及20%，逼近技术性熊市。韩国财政部长紧急召集央行及监管机构开会，直指半导体板块高度集中正在放大市场波动。监管层同时盯上快速扩张的单一股票杠杆ETF，警告其正成为此轮剧震的推手。"
  },
  {
    "id": "wscn:3776425",
    "domain": "股票",
    "title": "中东炮火再燃，油价急涨近3%，韩股剧烈波动再度跌至熔断",
    "url": "https://wallstreetcn.com/articles/3776425",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T05:47:56+00:00",
    "summary": "美军对伊朗发动新一轮空袭并撤销其售油豁免，布伦特原油盘中最高涨2.8%突破76美元。亚太股市开盘承压，但随后日韩股市抹去跌幅，午后韩股再度掉头向下跌超6%触发熔断。"
  },
  {
    "id": "wscn:3776428",
    "domain": "股票",
    "title": "恒科指大反攻涨4%，阿里涨超10%，创业板回落，科创50涨近3%，芯片、AI服务器爆发",
    "url": "https://wallstreetcn.com/articles/3776428",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T05:24:50+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市超3300股飘绿，上午半天成交1.72万亿。沪深两市半日成交额1.7万亿，较上个交易日放量720亿。板块方面，算力产业链爆发，服务器、云计算、ASIC芯片方向涨幅居前，锂电、动力电池方向低迷。"
  },
  {
    "id": "wscn:3776440",
    "domain": "股票",
    "title": "小米汽车杀进“9系”红海",
    "url": "https://wallstreetcn.com/articles/3776440",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T05:23:11+00:00",
    "summary": "不是“红米汽车”。"
  },
  {
    "id": "wscn:3776357",
    "domain": "股票",
    "title": "腾讯AI新船票：WorkBuddy登顶生产力工具，从“慢半拍”到“产品之王”蜕变",
    "url": "https://wallstreetcn.com/premium/articles/3776357?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:41:29+00:00",
    "summary": "上线3个月的WorkBuddy已经拿下国内效率AI DAU第一、月访问量885万（+831% MoM）、企业版定价涨价仍然供不应求。"
  },
  {
    "id": "wscn:3776433",
    "domain": "股票",
    "title": "新时代的结构性机会在哪里？（下）【大鹏说 第3讲】",
    "url": "https://wallstreetcn.com/premium/articles/3776433?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:30:38+00:00",
    "summary": "本栏目嘉宾老师介绍：\n \n PPT线上地址：https://img.kp-research.cn..."
  },
  {
    "id": "wscn:3776415",
    "domain": "股票",
    "title": "错失AI狂欢与万亿ETF撤退：宁泉资产坚守“反共识”策略的代价与逻辑",
    "url": "https://wallstreetcn.com/articles/3776415",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:30:12+00:00",
    "summary": "2026年上半年，百亿私募宁泉资产因坚守低估值价值股、回避AI热门板块，在科技单边牛市中遭遇成立以来最严峻挑战，6月回撤幅度达历史最大水平。这折射出市场深层矛盾：A股日均成交额创历史新高，但全市场股票涨跌幅中位数却为-15.4%。上半年A股半导体近乎翻倍，其余板块则呈熊市形态。"
  },
  {
    "id": "wscn:3776416",
    "domain": "股票",
    "title": "SpaceX与Cursor最快本周三发布联合AI模型，剑指Opus 4.8及GPT-5.5",
    "url": "https://wallstreetcn.com/articles/3776416",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:25:38+00:00",
    "summary": "SpaceX旗下AI部门xAI与编程工具公司Cursor即将联合发布AI模型，该模型在xAI的Colossus数据中心从零训练，核心优势在于信息处理速度，部分指标可与Anthropic Opus 4.8及OpenAI GPT-5.5抗衡。"
  },
  {
    "id": "wscn:3776438",
    "domain": "股票",
    "title": "券商业绩持续爆表！招商证券预告半年利润创纪录“破百亿”",
    "url": "https://wallstreetcn.com/articles/3776438",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:19:51+00:00",
    "summary": "后续还有关注点"
  },
  {
    "id": "wscn:3776434",
    "domain": "股票",
    "title": "高盛交易台：美股动量股抛售之凶猛，2020年以来未见！但尚未看到“恐慌”，散户是最大支撑",
    "url": "https://wallstreetcn.com/articles/3776434",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:07:04+00:00",
    "summary": "美股高贝塔动量因子单日重挫约6%，5日跌幅超20%，为2020年以来最猛烈抛售，但高盛交易台表示尚未看到恐慌，当前去风险行为有序，以去杠杆为主。散户逆势净买入，规模达近三年第90百分位，成最大支撑。目前或处调整后期，但因仓位拥挤且缺乏上行催化剂，仍存深度回调隐患。"
  },
  {
    "id": "wscn:3776430",
    "domain": "股票",
    "title": "台积电PIC产能三年扩容30倍，CPO供应链迎来放量窗口",
    "url": "https://wallstreetcn.com/articles/3776430",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:06:52+00:00",
    "summary": "台积电PIC月产能将从当前500片急速扩张至2028年的2.5万片，三年扩容逾30倍，对应PIC年化产出最高近1.94亿颗。英伟达、博通、AMD等AI巨头率先入列量产客户，FAU、激光器等配套供应链同步受益。但从晶圆到终端出货，SoIC良率瓶颈或将实际产出腰斩，CPO真正放量的节奏，仍悬于良率爬坡这道关键门槛之上。"
  },
  {
    "id": "wscn:3776432",
    "domain": "股票",
    "title": "SpaceX和Tesla早期投资人：我正在押注能源、生命科学、替代蛋白质、新材料",
    "url": "https://wallstreetcn.com/articles/3776432",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:04:32+00:00",
    "summary": "押注马斯克29年、投资了他每一家公司的Steve Jurvetson预判：未来三年，AI将引爆能源、农业、建筑三大传统行业。他正重仓核聚变、细胞培养肉、表观遗传编辑等前沿领域，并认为AI算力的指数级增长正将“低毛利烂生意”转变为信息化业务。"
  },
  {
    "id": "wscn:3776431",
    "domain": "股票",
    "title": "靠芯片与AI交易完成逆转，对冲基金创2021年以来最佳半年表现",
    "url": "https://wallstreetcn.com/articles/3776431",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T03:24:06+00:00",
    "summary": "对冲基金行业完成惊人逆转，经历一季度剧烈震荡后，凭借半导体与AI押注录得五年来最佳上半年成绩，平均回报率达7.2%。Whale Rock暴涨72.5%，Millennium单月豪赚37亿美元，芯片股史上最强季度表现成最大功臣。"
  },
  {
    "id": "wscn:3776424",
    "domain": "股票",
    "title": "未来5年砸出今年全年市场规模？马斯克“芯片超级工厂”Terafab大手笔砸半导体设备",
    "url": "https://wallstreetcn.com/articles/3776424",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T03:22:07+00:00",
    "summary": "马斯克正以\"要么自建，要么没有芯片\"的逻辑，推动SpaceX旗下Terafab打造史上最庞大的垂直整合半导体帝国。瑞银测算，该项目五年WFE采购规模约1350亿美元，峰值年支出超500亿——相当于再造一个台积电量级的买家，全球半导体设备市场天花板或将就此改写。"
  },
  {
    "id": "wscn:3776435",
    "domain": "股票",
    "title": "依托自贸金融创新，杭州银行以全链条跨境金融护航首都国企全球发债",
    "url": "https://wallstreetcn.com/articles/3776435",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T02:17:45+00:00",
    "summary": "随着企业“走出去”从产品出海迈向产能出海、体系出海，跨境金融需求正从单一结算融资向全球化、全场景综合..."
  },
  {
    "id": "wscn:3776436",
    "domain": "股票",
    "title": "劳力士蚝式腕表：闪耀的百年时光",
    "url": "https://wallstreetcn.com/articles/3776436",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T02:03:02+00:00",
    "summary": "上海西岸穹顶艺术中心（West Bund Dome）航拍图 © Rolex/Z-Vision2026..."
  },
  {
    "id": "wscn:3776422",
    "domain": "股票",
    "title": "华为“爆改”5nm芯片",
    "url": "https://wallstreetcn.com/articles/3776422",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T02:01:49+00:00",
    "summary": "华为发布“韬定律”V2版论文，以6年、381颗量产芯片为基础，提出“时间缩放”替代传统几何微缩的全新路径。旗舰芯片Kirin 2026首次验证“逻辑折叠”技术，在相同工艺下晶体管密度提升相当于传统三代工艺进化，功耗仅为上代59%。"
  },
  {
    "id": "wscn:3776429",
    "domain": "股票",
    "title": "高盛重提“HALO交易”：第二阶段刚刚开始",
    "url": "https://wallstreetcn.com/articles/3776429",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T02:00:40+00:00",
    "summary": "高盛认为，HALO交易（重资产、低淘汰风险）已进入第二阶段——盈利驱动。估值修复阶段完成，HALO交易关键转向盈利“兑现”，重资产15%的EPS增速预期超越轻资产10%。资本开支超级周期，尤其是AI、能源转型领域，为实物资产构建起强大护城河。"
  },
  {
    "id": "wscn:3775708",
    "domain": "股票",
    "title": "霍尔木兹海峡加速重启，原油跌势是否已接近尾声？",
    "url": "https://wallstreetcn.com/premium/articles/3775708?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T00:48:30+00:00",
    "summary": "霍尔木兹海峡复航致供应激增，油价暴跌，但库存偏低、补库及欧佩克减产将限制跌幅，跌势或近尾声。"
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
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05484",
    "domain": "金融",
    "title": "SHARC: SHAP-Based Interpretability in Machine Learning Risk Models for Regulatory Capital under ICAAP and CCAR",
    "url": "https://arxiv.org/abs/2607.05484",
    "source": "Ujjwala Vadrevu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.05484v1 Announce Type: new Abstract: The adoption of non-parametric machine learning models for regulatory capital estimation introduces a fundamental governance challenge: the inability to"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05627",
    "domain": "金融",
    "title": "Fighting discrimination with reputation: The case of online platforms",
    "url": "https://arxiv.org/abs/2607.05627",
    "source": "Xavier Lambin, Emil Palikot",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.05627v1 Announce Type: new Abstract: On a large French ridesharing platform, new minority drivers earn 11.6% less revenue than otherwise similar nonminority drivers; the gap nearly vanishes"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05802",
    "domain": "金融",
    "title": "Failure Privacy and Safe Collective Expression",
    "url": "https://arxiv.org/abs/2607.05802",
    "source": "Matthew Cashman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.05802v1 Announce Type: new Abstract: Widely held views can go unspoken when speaking out alone invites retaliation. I recast such silence as a problem of safe coalition formation. When safe"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.06117",
    "domain": "金融",
    "title": "Relief-Gated Relative Rotation for QQQ-DIA Allocation: Globally Screened Relative States, Fixed Position Mapping, Incremental Interaction Admission, and Walk-Forward Validation",
    "url": "https://arxiv.org/abs/2607.06117",
    "source": "Zheli Xiong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.06117v1 Announce Type: new Abstract: This paper studies Relief-Gated Relative Rotation (RGRR), a two-ETF rule that allocates between QQQ and DIA by mapping screened relative and macro state"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.06121",
    "domain": "金融",
    "title": "Can Reinforcement Learning Efficiently Discover Price Manipulation?",
    "url": "https://arxiv.org/abs/2607.06121",
    "source": "Ioanna-Yvonni Tsaknaki, Andrea Macr\\`i, Fabrizio Lillo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.06121v1 Announce Type: new Abstract: In this paper, we investigate whether a model-free RL agent can identify and exploit price manipulation opportunities more effectively than a traditiona"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.06204",
    "domain": "金融",
    "title": "Arbitrage-Free Multi-Maturity Risk-Neutral Marginals",
    "url": "https://arxiv.org/abs/2607.06204",
    "source": "Hao Qin, Ruozhong Yang, Charlie Che, Liming Feng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.06204v1 Announce Type: new Abstract: Many quantitative finance methods and applications are formulated in terms of option-implied risk-neutral marginals rather than directly in terms of opt"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.06340",
    "domain": "金融",
    "title": "Signature-based identification of volatility models from path geometry",
    "url": "https://arxiv.org/abs/2607.06340",
    "source": "\\`Oscar Bur\\'es, Rafael De Santiago",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.06340v1 Announce Type: new Abstract: We propose a signature-based framework for the identification of stochastic volatility model classes from observed path data. By mapping volatility traj"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.06355",
    "domain": "金融",
    "title": "Entropic Dynamics of Jump-Diffusion Option Pricing",
    "url": "https://arxiv.org/abs/2607.06355",
    "source": "Mohammad Abedi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.06355v1 Announce Type: new Abstract: Standard models of stock price dynamics and option valuation usually begin by postulating stochastic processes. This paper develops an entropic inferenc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.06427",
    "domain": "金融",
    "title": "The U.S. Mortality Crisis as a Preston Curve Reversal",
    "url": "https://arxiv.org/abs/2607.06427",
    "source": "Ritikaa Khanna, Rourke O'Brien, Andrew Stokes, Atheendar Venkataramani, Elizabeth Wrigley-Field",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.06427v1 Announce Type: new Abstract: U.S. life expectancy stagnated and declined in the 2010s despite continued growth in real per capita income. We use Preston curves to characterize this "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.06502",
    "domain": "金融",
    "title": "What Useful Alphas?",
    "url": "https://arxiv.org/abs/2607.06502",
    "source": "Andrew Y. Chen, Ivo Welch",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.06502v1 Announce Type: new Abstract: This paper examines about 200 published long-short anomaly equity portfolios (Chen and Zimmermann, 2022). Over the period through 2005 (December 2005 an"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05414",
    "domain": "金融",
    "title": "Redistricting Compactness as Constrained Perimeter Minimization: Soap Bubble Theory and Discrete Approximation",
    "url": "https://arxiv.org/abs/2607.05414",
    "source": "Mark B Garman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.05414v1 Announce Type: cross Abstract: We propose a mathematical framework for redistricting compactness grounded in the classical soap bubble problem: the partition of a planar region into"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05695",
    "domain": "金融",
    "title": "Structural Divergence of the Roman--Byzantine Trade Network, 0--1453\\,CE: Persistent Homology, Topological Velocity, and Criticality Indicators of Imperial Collapse",
    "url": "https://arxiv.org/abs/2607.05695",
    "source": "Jose de Jesus Bernal-Alvarado, David Delepine, Carlos Pinedo Guadarrama",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.05695v1 Announce Type: cross Abstract: We extend the persistent homology analysis of~\\paperone{} to the full Roman--Byzantine trade network (0--1453\\,\\textsc{ce}), using 2{,}599 nodes and 4"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05697",
    "domain": "金融",
    "title": "Stability and Dual Valuation of Contingent Claims under Rockafellian Perturbations",
    "url": "https://arxiv.org/abs/2607.05697",
    "source": "Wolfgang Breytmann, Julio Deride, Nicol\\'as Hern\\'andez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.05697v1 Announce Type: cross Abstract: We study the stability of solutions to the discrete-time contingent-claim problem over a finite investment horizon when uncertainty is modeled by rand"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.06153",
    "domain": "金融",
    "title": "From Gravity to Confinement: Wealth Redistribution as Optimal Drift Design in the Fokker-Planck Framework",
    "url": "https://arxiv.org/abs/2607.06153",
    "source": "Anders G Fr{\\o}seth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.06153v1 Announce Type: cross Abstract: A proportional wealth tax acts as a uniform gravitational field on the wealth distribution: it shifts the drift of the Fokker-Planck equation without "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.06220",
    "domain": "金融",
    "title": "Stable Sentiment and Persistent Dynamics in U.S. Economic News over 45 Years",
    "url": "https://arxiv.org/abs/2607.06220",
    "source": "Luis Enrique Correa Rocha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.06220v1 Announce Type: cross Abstract: Collective emotion is often inferred from the tone of mass media, but such emotion is not directly observed. One approximation is to extract sentiment"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.06316",
    "domain": "金融",
    "title": "Does Financial Trading Smooth Non-Convex Markets?",
    "url": "https://arxiv.org/abs/2607.06316",
    "source": "Nicolas Stevens, Peter Cramton, Martial Toniotti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.06316v1 Announce Type: cross Abstract: In non-convex markets, a competitive equilibrium may fail to exist. This turns out to be an important issue in real-world non-convex auction markets, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.06373",
    "domain": "金融",
    "title": "Error Propagation in Spectral Functionals of Shrinkage Covariance Estimators: Perturbation Bounds and Calibrated Inference",
    "url": "https://arxiv.org/abs/2607.06373",
    "source": "Ahmad Koman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.06373v1 Announce Type: cross Abstract: Rolling covariance estimates feed two objects that are routinely treated as market structure. The first is the dominant eigenspace, monitored through "
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.19377",
    "domain": "金融",
    "title": "Government Transparency and Innovation: Evidence from Wireless Products",
    "url": "https://arxiv.org/abs/2510.19377",
    "source": "\\v{S}imon Trlifaj",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2510.19377v3 Announce Type: replace Abstract: We exploit a 1998 administrative quasi-experiment to analyze the effects of government transparency on follow-on innovation. Using the universe of U"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.25826",
    "domain": "金融",
    "title": "Technology Fundamentals and False Bubble Detection: Evidence from Dot-Com and AI Episodes",
    "url": "https://arxiv.org/abs/2604.25826",
    "source": "Haiqiang Chen, Li Chen, Difang Huang, Yuexin Li, Zhengjun Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2604.25826v3 Announce Type: replace Abstract: We show that widely used bubble tests, most prominently the PSY framework, suffer severe size distortion when fundamentals incorporate general-purpo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.27694",
    "domain": "金融",
    "title": "The Satoshi Overhang: Why the Bear Case is Bounded",
    "url": "https://arxiv.org/abs/2604.27694",
    "source": "Karl T. Ulrich",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2604.27694v2 Announce Type: replace Abstract: Renewed attention to the identity of Bitcoin's pseudonymous creator has revived an old worry: that the roughly 1.148 million BTC mined by Satoshi an"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.25438",
    "domain": "金融",
    "title": "Agentic Delegation and the Language Frontier of Software Developers: A Model and Evidence from Claude Code on GitHub",
    "url": "https://arxiv.org/abs/2605.25438",
    "source": "Alexander Quispe, Kevin Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2605.25438v2 Announce Type: replace Abstract: We develop and test a model of agentic delegation in software production. Developers face language-specific entry thresholds; conversational AI main"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09564",
    "domain": "金融",
    "title": "Option prices from operational-time reaction-boundary lattices",
    "url": "https://arxiv.org/abs/2606.09564",
    "source": "Chris Angstmann, Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2606.09564v3 Announce Type: replace Abstract: We consider the role of a continuum operational time u and its mapping to calendar time t and how these relate to event time for option pricing prob"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.00279",
    "domain": "金融",
    "title": "Night and Day: Diurnal Warming and Structural Transformation in India",
    "url": "https://arxiv.org/abs/2607.00279",
    "source": "Vedarshi Shastry",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.00279v2 Announce Type: replace Abstract: This paper finds diverging partial effects of diurnal warming (higher nighttime and daytime temperatures) on agricultural wage-labour shares from de"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.05091",
    "domain": "金融",
    "title": "Any Axes Are Allowed: A Characteristic-Axis Integral Diagnosis of Factor Models",
    "url": "https://arxiv.org/abs/2607.05091",
    "source": "Useong Shin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2607.05091v2 Announce Type: replace Abstract: This paper extends the cap-axis integral diagnostic to general characteristic axes and measures factor-model pricing errors as bridge-alpha curves. "
  },
  {
    "id": "rss:https://arxiv.org/abs/2302.01362",
    "domain": "金融",
    "title": "Signature SDEs from an affine and polynomial perspective",
    "url": "https://arxiv.org/abs/2302.01362",
    "source": "Christa Cuchiero, Sara Svaluto-Ferro, Josef Teichmann",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2302.01362v3 Announce Type: replace-cross Abstract: Signature stochastic differential equations (SDEs) constitute a large class of stochastic processes, here driven by Brownian motions, whose ch"
  },
  {
    "id": "rss:https://arxiv.org/abs/2412.10860",
    "domain": "金融",
    "title": "Classification of Financial Data Using Quantum Support Vector Machine",
    "url": "https://arxiv.org/abs/2412.10860",
    "source": "Seemanta Bhattacharjee, MD. Muhtasim Fuad, A. K. M. Fakhrul Hossain",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T04:00:00+00:00",
    "summary": "arXiv:2412.10860v2 Announce Type: replace-cross Abstract: Quantum Support Vector Machine is a kernel-based approach to classification problems. We study the applicability of quantum kernels to financi"
  }
]
```
