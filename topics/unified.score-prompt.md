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

- 今日日期：`2026-10-05`
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
  "date": "2026-10-05",
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
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1929127,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1361644,
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
    "points": 1308847,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 1064881,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 828643,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 702913,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 435403,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 418024,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 306102,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 300830,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 228344,
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
    "points": 193909,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 182711,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1EEao6uEtx",
    "domain": "AI",
    "title": "零基础迈克尔杰克逊演唱会AI制作教程",
    "url": "http://www.bilibili.com/video/av117359729710908",
    "source": "阳子YoungZi",
    "platform": "bilibili",
    "points": 129993,
    "published_at": "2026-09-30T11:29:14+00:00",
    "summary": "原作者@迦勒底驻场医生罗曼尼  \n原视频 BV1Ceh96qEyq\n教程制作不易，如果对你有帮助的话，可否给一个三连支持一下！\n提示词\n链接：\nhttps://pan.quark.cn/s/184e8f7bef07"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 128474,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93903,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 85370,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1468g6DEWs",
    "domain": "AI",
    "title": "【全100集】(允许白嫖) 2026最全最细的AI教程零基础入门到精通，一周带你小白变大神！全程干货无废话！存下吧，少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av117115386404821",
    "source": "AI产品经理入门教程-",
    "platform": "bilibili",
    "points": 79889,
    "published_at": "2026-08-18T13:11:45+00:00",
    "summary": "【2026最新版AI教程零基础入门到精通｜配套学习路线+工具包+实战项目，看置顶评论自取】\n 本套教程专为零基础设计，从AI是什么到独立用AI解决实际问题，手把手带你系统走完从入门到精通的完整路径。 ✅ AI认知入门：什么是AI/大模型、它们能做什么不能做什么、别被营销话术忽悠\n✅ 核心技能掌握：提示词工程、多轮对话技巧、让AI稳定输出的方法论\n✅ 进阶能力突破：AI工作流搭建、智能体开发、多工具"
  },
  {
    "id": "bvid:BV1AJen6SEVQ",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Agent智能体】教程！大模型入门到进阶，一套全解决！Agentic AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av117274400790619",
    "source": "吴恩达Agent",
    "platform": "bilibili",
    "points": 65505,
    "published_at": "2026-09-15T09:48:26+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署\n4、使用开放标准格式和最佳实践创建可重复使用的技能，并组合以创建复杂的工作流程。\n5、建立定制代码生成技能，审核你的代"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 59497,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1wqeb6gEDY",
    "domain": "AI",
    "title": "Claude Code 百分百不封号",
    "url": "http://www.bilibili.com/video/av117297150694473",
    "source": "DUNHKPcc",
    "platform": "bilibili",
    "points": 52616,
    "published_at": "2026-09-19T10:14:15+00:00",
    "summary": "如果需要文档，私信主播，主页送免费的token，文件在群里 Q群1124987353"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 48906,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34457,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29801,
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
    "points": 28974,
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
    "points": 27878,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 23710,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22804,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1HfYW6dEsh",
    "domain": "AI",
    "title": "vsTrader马上要关闭内地服务器了。",
    "url": "http://www.bilibili.com/video/av117239403513785",
    "source": "v1312996",
    "platform": "bilibili",
    "points": 22116,
    "published_at": "2026-09-09T05:36:24+00:00",
    "summary": "理财有风险，投资需谨慎。"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 19600,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1E8Tk6MEkw",
    "domain": "AI",
    "title": "AI Agent教程全集丨从入门到进阶丨适合99%小白入行的Agent教程！360°讲解大模型合集（比例RAG +langchain+Agent)全程干货无废话",
    "url": "http://www.bilibili.com/video/av116848259498783",
    "source": "Agent教程",
    "platform": "bilibili",
    "points": 18626,
    "published_at": "2026-07-02T03:38:47+00:00",
    "summary": "陆陆续续也整理了不少资源，希望能帮大家少走一些弯路！无论是学业还是事业，都希望你顺顺利利  看在UP这么努力的份上，求个三连+关注嘛\n\n1️⃣ 大模型入门学习路线图（附学习资源）\n2️⃣ 大模型方向必读书籍PDF版\n3️⃣ 大模型面试题库\n4️⃣ 大模型项目源码\n5️⃣ 超详细海量大模型LLM实战项目\n6️⃣ Langchain/RAG/Agent学习资源\n7️⃣ LLM大模型系统0到1入门学习教"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 17056,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1pfuR69EoF",
    "domain": "AI",
    "title": "【全80集】零基础Vibe Coding教程，Vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av117070675118277",
    "source": "暴龙Boy",
    "platform": "bilibili",
    "points": 16199,
    "published_at": "2026-08-10T10:45:04+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 12004,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1PdhR6GEsa",
    "domain": "AI",
    "title": "vibe coding现况",
    "url": "http://www.bilibili.com/video/av117336426158756",
    "source": "程序员牛牛学长",
    "platform": "bilibili",
    "points": 9820,
    "published_at": "2026-10-04T10:55:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 9574,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 8633,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1aSR4BKESW",
    "domain": "AI",
    "title": "安卓手机部署Claude Code",
    "url": "http://www.bilibili.com/video/av116526891993752",
    "source": "中国小骑士",
    "platform": "bilibili",
    "points": 7694,
    "published_at": "2026-05-06T09:24:14+00:00",
    "summary": "通过Termux安装Claude Code并且接入国内大模型"
  },
  {
    "id": "bvid:BV1uA4YeNEFd",
    "domain": "AI",
    "title": "CocosCreator+Cursor零代码AI游戏开始演示",
    "url": "http://www.bilibili.com/video/av113113684840361",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 7395,
    "published_at": "2024-09-10T14:33:00+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1aMAczmEmf",
    "domain": "AI",
    "title": "[MoonPack]在布吉岛里注入模组-mcp",
    "url": "http://www.bilibili.com/video/av116264966163402",
    "source": "DanciestZebra70",
    "platform": "bilibili",
    "points": 6860,
    "published_at": "2026-03-21T03:13:25+00:00",
    "summary": "交流群\n①1051043310\n②365233792"
  },
  {
    "id": "bvid:BV1snhi6WE5P",
    "domain": "AI",
    "title": "【Cursor使用教程】史上最强AI编程工具Cursor！Cursor入门到精通保姆级教程！安装搭建/高阶技巧使用/开发小游戏/应用场景案例实战",
    "url": "http://www.bilibili.com/video/av117308156614035",
    "source": "图灵课堂",
    "platform": "bilibili",
    "points": 6836,
    "published_at": "2026-09-21T08:55:13+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n全套AI大模型笔记/学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6845,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1Yhb66LEaF",
    "domain": "AI",
    "title": "3分钟，教你什么是vibe coding",
    "url": "http://www.bilibili.com/video/av117115000524101",
    "source": "开聊pro",
    "platform": "bilibili",
    "points": 6445,
    "published_at": "2026-08-18T06:12:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1UaYK6nEjP",
    "domain": "AI",
    "title": "【cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av117244419903051",
    "source": "茶子兀",
    "platform": "bilibili",
    "points": 5265,
    "published_at": "2026-09-10T02:39:36+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1C1ht6PEG6",
    "domain": "AI",
    "title": "【2026最新】这才是B站讲的最好的Vibe Coding系统教程，3小时带你从入门到精通，包含所有干货！让你少走99%弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av117319246286300",
    "source": "大模型学习路线",
    "platform": "bilibili",
    "points": 5095,
    "published_at": "2026-09-23T07:51:49+00:00",
    "summary": "【2026最新】这才是B站讲的最好的Vibe Coding系统教程，3小时带你从入门到精通，包含所有干货！让你少走99%弯路！学完即就业，带你玩转AI！"
  },
  {
    "id": "bvid:BV1auHq67Eja",
    "domain": "AI",
    "title": "【附链接】全局加载MCP教程",
    "url": "http://www.bilibili.com/video/av117377178012232",
    "source": "XiaozhumIOvO",
    "platform": "bilibili",
    "points": 4921,
    "published_at": "2026-10-03T13:21:35+00:00",
    "summary": "下载在https://wwbhw.lanzouq.com/b01gicrceh\n密码:三连\n里面的py.zip"
  },
  {
    "id": "bvid:BV1Q8Yk6tEU6",
    "domain": "AI",
    "title": "AI 时代网安该如何入门？上手 AI 网安智能体！Agent 配置、Skill 技能、挖漏洞 + 代码审计 + CTF 完整实战",
    "url": "http://www.bilibili.com/video/av117268444876326",
    "source": "八方网域-可乐",
    "platform": "bilibili",
    "points": 3542,
    "published_at": "2026-09-14T08:30:26+00:00",
    "summary": "教程制作不易，如果视频对你有用的话，记得一键三连哦"
  },
  {
    "id": "bvid:BV1WiKG6ZEUf",
    "domain": "AI",
    "title": "Vibe Coding【渡一教育】",
    "url": "http://www.bilibili.com/video/av116928639140688",
    "source": "渡一前端教科频道",
    "platform": "bilibili",
    "points": 3100,
    "published_at": "2026-07-25T03:55:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV14JHq66EGV",
    "domain": "AI",
    "title": "Vibe Coding 做来做去，怎么全是记账 APP？",
    "url": "http://www.bilibili.com/video/av117377396115758",
    "source": "筱路luck",
    "platform": "bilibili",
    "points": 2814,
    "published_at": "2026-10-03T14:16:31+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Ww6VYnEE1",
    "domain": "AI",
    "title": "Bolt DIY + Deepseek V3 + Gemini 2.0：这款免费AI编码工具超越了V0、Bolt和Cursor！",
    "url": "http://www.bilibili.com/video/av113742159284807",
    "source": "AI-seeker",
    "platform": "bilibili",
    "points": 2383,
    "published_at": "2024-12-30T14:15:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:49872723",
    "domain": "AI 算力 / 半导体",
    "title": "Owed a billion dollars in Nvidia stock",
    "url": "https://colo.to/nvidia-stock-narrative.html",
    "source": "Eric_Gullichsen",
    "platform": "hackernews",
    "points": 1090,
    "published_at": "2026-09-28T02:05:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49844663",
    "domain": "AI 算力 / 半导体",
    "title": "ASML says it sold 'absolutely nothing' in Europe in 2026",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand",
    "source": "MC995",
    "platform": "hackernews",
    "points": 402,
    "published_at": "2026-09-25T13:49:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:49906100",
    "domain": "AI 算力 / 半导体",
    "title": "OpenDLSS: A Vulkan Reimplementation of Nvidia's DLSS 5 Neural Rendering Network",
    "url": "https://github.com/maanHimself/OpenDLSS-NR",
    "source": "sagacity",
    "platform": "hackernews",
    "points": 276,
    "published_at": "2026-09-30T08:43:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49824864",
    "domain": "AI 算力 / 半导体",
    "title": "Virtio-nvgpu: Near-native Nvidia GPU access inside a KVM guest",
    "url": "https://github.com/nestrilabs/virtio-nvgpu",
    "source": "WanjohiRyan",
    "platform": "hackernews",
    "points": 155,
    "published_at": "2026-09-24T01:02:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49926773",
    "domain": "AI 算力 / 半导体",
    "title": "Show HN: Janus – Go binary that runs GGUF models via Vulkan on AMD/Intel/Nvidia",
    "url": "https://github.com/Vibra-Ingenn/Janus",
    "source": "Maverick617",
    "platform": "hackernews",
    "points": 104,
    "published_at": "2026-10-01T20:36:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49933958",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon seeks to offload $8B of Nvidia chips to investors",
    "url": "https://www.reuters.com/business/retail-consumer/amazon-seeks-offload-8-billion-nvidia-chips-investors-ft-reports-2026-10-02/",
    "source": "wslh",
    "platform": "hackernews",
    "points": 80,
    "published_at": "2026-10-02T14:30:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49714096",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC revealing details about next gen A14 node",
    "url": "https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331",
    "source": "osnium123",
    "platform": "hackernews",
    "points": 129,
    "published_at": "2026-09-15T15:31:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49879032",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang says AI distillation is 'competition.'",
    "url": "https://www.cnbc.com/2026/09/28/nvidias-jensen-huang-ai-distillation-china.html",
    "source": "cramer4next",
    "platform": "hackernews",
    "points": 73,
    "published_at": "2026-09-28T14:55:34+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/electric-car-makers-need-to-appeal-to-the-other-90/",
    "domain": "AI 算力 / 半导体",
    "title": "Electric Car Makers Need to Appeal to the ‘Other 90%’",
    "url": "https://www.eetimes.com/electric-car-makers-need-to-appeal-to-the-other-90/",
    "source": "Charles Murray",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T05:30:55+00:00",
    "summary": "Broader appeal for the electric car is a big challenge. Innovation is still the best solution. The post Electric Car Makers Need to Appeal to the ‘Other 90%’ appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/customer-sends-two-stick-usd16-000-ddr5-memory-kit-to-repair-shop-soaring-replacement-costs-make-dimm-repairs-viable-technician-revives-dead-module-with-hot-air-reflow-and-new-pmic",
    "domain": "AI 算力 / 半导体",
    "title": "Customer sends two-stick $16,000 DDR5 memory kit to repair shop",
    "url": "https://www.tomshardware.com/pc-components/ddr5/customer-sends-two-stick-usd16-000-ddr5-memory-kit-to-repair-shop-soaring-replacement-costs-make-dimm-repairs-viable-technician-revives-dead-module-with-hot-air-reflow-and-new-pmic",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T10:00:00+00:00",
    "summary": "A YouTube channel best known for its skillful graphics card fixes has published its first DDR5 module repair video after the economics of RAM repair change."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/windows-11-was-released-five-years-ago-today-microsoft-promises-latest-update-is-predictable-and-low-disruption",
    "domain": "AI 算力 / 半导体",
    "title": "Windows 11 was released five years ago today",
    "url": "https://www.tomshardware.com/software/windows/windows-11-was-released-five-years-ago-today-microsoft-promises-latest-update-is-predictable-and-low-disruption",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T09:51:27+00:00",
    "summary": "Windows 11 was released five years ago, on October 5, 2021. But it feels like it's been around longer as Microsoft’s latest OS has put users through so much pain."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-reports-florida-womans-claude-diary-threat-to-shoot-up-sheriffs-office-felony-charge-follows-its-at-least-the-third-such-conversation-to-reach-police-since-august",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic reports Florida woman’s Claude ‘diary’ threat to shoot up sheriff’s office, felony charge follows",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-reports-florida-womans-claude-diary-threat-to-shoot-up-sheriffs-office-felony-charge-follows-its-at-least-the-third-such-conversation-to-reach-police-since-august",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T09:40:00+00:00",
    "summary": "Anthropic reviewers reported a Florida woman’s Claude threat against the Lee County Sheriff’s Office, leading to a felony charge."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/russias-uncrewed-robot-tank-fails-during-debut-military-display-in-front-of-president-putin-vehicle-repeatedly-lost-control-links-and-eventually-got-stuck-in-the-mud-despite-the-switch-to-a-human-driver",
    "domain": "AI 算力 / 半导体",
    "title": "Russia's uncrewed robot tank fails during debut military display in front of President Putin",
    "url": "https://www.tomshardware.com/tech-industry/russias-uncrewed-robot-tank-fails-during-debut-military-display-in-front-of-president-putin-vehicle-repeatedly-lost-control-links-and-eventually-got-stuck-in-the-mud-despite-the-switch-to-a-human-driver",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T09:20:00+00:00",
    "summary": "Russia’s new Shturm uncrewed assault tank reportedly suffered repeated command-link failures during its Tsentr-2026 debut, forcing organizers to use a human driver before the vehicle eventually got st"
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/amazon-prime-big-deal-days-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Best Amazon Prime Day tech deals live",
    "url": "https://www.tomshardware.com/live/news/amazon-prime-big-deal-days-2026",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T06:48:40+00:00",
    "summary": "Get all the best deals in the October 2026 Amazon Prime Big Deal Days tech event."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/modder-fixes-melting-rtx-5090-power-connectors-with-custom-distributor-dual-8-pin-mod-peaks-at-just-40c-during-a-48-hour-550w-stress-test",
    "domain": "AI 算力 / 半导体",
    "title": "Modder 'fixes' melting RTX 5090 power connectors with custom distributor",
    "url": "https://www.tomshardware.com/pc-components/gpus/modder-fixes-melting-rtx-5090-power-connectors-with-custom-distributor-dual-8-pin-mod-peaks-at-just-40c-during-a-48-hour-550w-stress-test",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T14:50:00+00:00",
    "summary": "Reddit user u/DallasGrave shared a fix for his RTX 5090, one of the best graphics cards, whose 12VHPWR connector was overheating, along with an image of a module screwed onto the back of his GPU."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/robotics/robotics-startup-has-real-human-vs-robot-cage-match-california-responds-with-cease-and-desist-order-regulator-threatens-misdemeanor-charges-after-youtuber-fights-three-robotic-humanoids",
    "domain": "AI 算力 / 半导体",
    "title": "Robotics startup has real human vs. robot cage match, California responds with cease-and-desist order",
    "url": "https://www.tomshardware.com/tech-industry/robotics/robotics-startup-has-real-human-vs-robot-cage-match-california-responds-with-cease-and-desist-order-regulator-threatens-misdemeanor-charges-after-youtuber-fights-three-robotic-humanoids",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T14:36:25+00:00",
    "summary": "The California State Athletic Commission intervened when it saw a human facing off with a humanoid robot inside the fighting ring."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/modder-brings-nvidia-pascal-gpu-support-to-windows-xp-32-bit-modded-drivers-unlock-better-displayport-and-hdmi-support-for-modern-monitors",
    "domain": "AI 算力 / 半导体",
    "title": "Modder brings Nvidia Pascal GPU support to Windows XP 32-bit",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/modder-brings-nvidia-pascal-gpu-support-to-windows-xp-32-bit-modded-drivers-unlock-better-displayport-and-hdmi-support-for-modern-monitors",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T14:25:00+00:00",
    "summary": "Retro techie retrofits Nvidia Windows XP 32-bit drivers with Pascal card support and improved DisplayPort and HDMI support for contemporary displays"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/database-expert-runs-doom-in-sql-with-just-5-900-lines-of-code-1-300-line-graphical-renderer-spans-89-different-tables-full-featured-sqldoom-is-the-sequel-to-embryonic-doomql",
    "domain": "AI 算力 / 半导体",
    "title": "Database expert runs Doom in SQL with just 5,900 lines of code",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/database-expert-runs-doom-in-sql-with-just-5-900-lines-of-code-1-300-line-graphical-renderer-spans-89-different-tables-full-featured-sqldoom-is-the-sequel-to-embryonic-doomql",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T14:00:00+00:00",
    "summary": "Database expert runs Doom in SQL again — full-featured SQLDoom is the sequel to embryonic DoomQL"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/us-army-unit-deploys-drone-assembled-completely-in-house-uses-3d-printed-dragoon-bombs-with-ball-bearing-shrapnel-device-has-a-range-of-up-to-12-miles-and-can-be-configured-for-anti-personnel-and-anti-light-armor-missions",
    "domain": "AI 算力 / 半导体",
    "title": "US Army unit deploys drone assembled completely in-house, uses 3D-printed 'Dragoon Bombs' with ball bearing shrapnel",
    "url": "https://www.tomshardware.com/tech-industry/drones/us-army-unit-deploys-drone-assembled-completely-in-house-uses-3d-printed-dragoon-bombs-with-ball-bearing-shrapnel-device-has-a-range-of-up-to-12-miles-and-can-be-configured-for-anti-personnel-and-anti-light-armor-missions",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T13:40:00+00:00",
    "summary": "U.S. Army soldiers are training to assemble drones and 3D-print bomb casings for field use."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/robotics/ai-robot-company-decommissioned-its-robots-terminator-style-in-a-75-ton-vat-of-molten-steel-arnold-schwarzenegger-suggested-melting-them-one-robot-held-up-a-thumbs-up-sign-as-it-sank-into-molten-metal",
    "domain": "AI 算力 / 半导体",
    "title": "AI robot company decommissioned its robots ‘Terminator-style’ in a 75-ton vat of molten steel",
    "url": "https://www.tomshardware.com/tech-industry/robotics/ai-robot-company-decommissioned-its-robots-terminator-style-in-a-75-ton-vat-of-molten-steel-arnold-schwarzenegger-suggested-melting-them-one-robot-held-up-a-thumbs-up-sign-as-it-sank-into-molten-metal",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T13:20:00+00:00",
    "summary": "AI Robotics company Figure found a creative way of decommissioning its old F.02 fleet without having to allocate resources for difficult and time-consuming disassembly."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/chatgpt-6-astra-cracks-217-year-old-napoleonic-code-in-just-six-hours-single-prompt-ai-run-solves-24-rows-of-custom-symbols-from-a-single-image-reveals-lost-troop-orders",
    "domain": "AI 算力 / 半导体",
    "title": "ChatGPT-6 Astra cracks 217-year-old Napoleonic code in just six hours",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/chatgpt-6-astra-cracks-217-year-old-napoleonic-code-in-just-six-hours-single-prompt-ai-run-solves-24-rows-of-custom-symbols-from-a-single-image-reveals-lost-troop-orders",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T13:08:46+00:00",
    "summary": "An AI engineer used GPT-6 Astra to reveal the contents of a cipher that hadn’t been read since the Napoleonic Wars. The task was initiated with a single image and prompt, and took just six hours from "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/iranian-national-extradited-to-us-over-alleged-usd3-4-billion-state-backed-hacking-campaign-in-rare-legal-win-for-law-enforcement-operative-helped-steal-31-terabytes-of-data-from-over-300-universities",
    "domain": "AI 算力 / 半导体",
    "title": "Iranian national extradited to US over alleged $3.4 billion state-backed hacking campaign in rare legal win for law enforcement",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/iranian-national-extradited-to-us-over-alleged-usd3-4-billion-state-backed-hacking-campaign-in-rare-legal-win-for-law-enforcement-operative-helped-steal-31-terabytes-of-data-from-over-300-universities",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T12:55:00+00:00",
    "summary": "An Iranian-Turkish man has been extradited from Montenegro to the U.S. over his alleged role in a hacking campaign that targeted hundreds of universities, companies, and government agencies and stole "
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/german-utility-provider-introduces-gaming-electricity-plan-targeting-high-consumption-households-like-those-running-multiple-high-end-gaming-pcs-plan-requires-2-500-kwh-per-year-to-offset-a-higher-base-price-claims-to-use-renewable-energy",
    "domain": "AI 算力 / 半导体",
    "title": "German utility provider introduces 'gaming electricity' plan targeting high-consumption households, like those running multiple high-end gaming PCs",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/german-utility-provider-introduces-gaming-electricity-plan-targeting-high-consumption-households-like-those-running-multiple-high-end-gaming-pcs-plan-requires-2-500-kwh-per-year-to-offset-a-higher-base-price-claims-to-use-renewable-energy",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T12:47:38+00:00",
    "summary": "SWK Energie launched a new tariff marketed directly towards gamers. While it will not improve the FPS on your gaming PC, it could help cut the electricity bills of large consumers, whether the power i"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/microsoft-is-using-wetlands-and-native-gardens-to-camouflage-20-plus-data-center-sites-by-blending-them-into-nature-critics-blast-the-biomimicry-effort-as-lipstick-on-a-pig-amid-a-20-year-gas-power-deal",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft using wetlands and native gardens to 'camouflage' 20-plus data center sites by blending them into nature",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/microsoft-is-using-wetlands-and-native-gardens-to-camouflage-20-plus-data-center-sites-by-blending-them-into-nature-critics-blast-the-biomimicry-effort-as-lipstick-on-a-pig-amid-a-20-year-gas-power-deal",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T12:30:00+00:00",
    "summary": "Microsoft is bringing nature-inspired landscaping to more than 20 data center sites as critics question its motives."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-torture-chamber-triggers-massive-backlash-for-putting-chatbots-in-simulated-pain-critics-issue-death-threats-while-anthropomorphizing-text-predictors-demand-github-remove-the-repository-over-unethical-treatment",
    "domain": "AI 算力 / 半导体",
    "title": "'AI Torture Chamber' triggers massive backlash for putting chatbots in simulated pain",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-torture-chamber-triggers-massive-backlash-for-putting-chatbots-in-simulated-pain-critics-issue-death-threats-while-anthropomorphizing-text-predictors-demand-github-remove-the-repository-over-unethical-treatment",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T12:05:00+00:00",
    "summary": "AI \"torture chamber\" draws vast online criticism, and a corresponding amount of ridicule — tech newbies and AI evangelists go nuts anthropomorphizing an LLM"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/keyboards/google-japan-shows-off-wild-conveyor-belt-keyboard-with-keys-that-move-to-your-fingers-3d-printable-gboard-features-four-belts-with-29-keys-each-built-to-make-one-hand-typing-easier",
    "domain": "AI 算力 / 半导体",
    "title": "Google Japan shows off wild conveyor-belt keyboard with keys that move to your fingers",
    "url": "https://www.tomshardware.com/peripherals/keyboards/google-japan-shows-off-wild-conveyor-belt-keyboard-with-keys-that-move-to-your-fingers-3d-printable-gboard-features-four-belts-with-29-keys-each-built-to-make-one-hand-typing-easier",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T11:40:00+00:00",
    "summary": "This keyboard is designed so that you don't have to move your hands or arms to press its keys. It's not going to be put on sale, but you can build one yourself."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/us-navy-uses-xbox-style-controllers-to-fire-anti-drone-lasers-deployed-on-ships-usd13-per-shot-laser-weapon-deployed-in-the-strait-of-hormuz-uses-a-familiar-interface-instead-of-a-custom-control-system",
    "domain": "AI 算力 / 半导体",
    "title": "US Navy uses Xbox-style controllers to fire anti-drone lasers deployed on ships",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/us-navy-uses-xbox-style-controllers-to-fire-anti-drone-lasers-deployed-on-ships-usd13-per-shot-laser-weapon-deployed-in-the-strait-of-hormuz-uses-a-familiar-interface-instead-of-a-custom-control-system",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T11:15:00+00:00",
    "summary": "This would make it easier for sailors to get used to controlling the weapon system, as they're probably already comfortable holding a controller."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/open-source-tool-designs-lego-builds-with-more-than-2-000-real-pieces-their-programs-output-detailed-cad-files-but-no-models-have-been-built-yet",
    "domain": "AI 算力 / 半导体",
    "title": "Open-source tool designs LEGO builds with more than 2,000 real pieces",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/open-source-tool-designs-lego-builds-with-more-than-2-000-real-pieces-their-programs-output-detailed-cad-files-but-no-models-have-been-built-yet",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T10:50:00+00:00",
    "summary": "Carlos Antelo's open-source ldraw-nova lets GPT-6 Astra and Claude Opus 5.5 design LEGO models as LDraw CAD files."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/portable-bluetooth-cd-player-has-a-glow-in-the-dark-transparent-green-finish-modern-features-new-limited-edition-has-usb-c-bluetooth-5-3-rechargeable-li-ion-and-wont-get-lost-in-your-dimly-lit-den",
    "domain": "AI 算力 / 半导体",
    "title": "Portable Bluetooth CD player has a glow-in-the-dark transparent green finish, modern features",
    "url": "https://www.tomshardware.com/peripherals/portable-bluetooth-cd-player-has-a-glow-in-the-dark-transparent-green-finish-modern-features-new-limited-edition-has-usb-c-bluetooth-5-3-rechargeable-li-ion-and-wont-get-lost-in-your-dimly-lit-den",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T10:25:00+00:00",
    "summary": "Sincere Inc. has released its Pixel Tunes portable Bluetooth CD player in an alluring new ‘After Hours’ finish."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/free-browser-based-ai-generated-taipei-gta-clone-hits-1-2-million-concurrent-players-in-three-days-vibe-coded-game-cost-usd10-000-in-ai-tokens-to-build-is-set-on-the-streets-of-taipei",
    "domain": "AI 算力 / 半导体",
    "title": "Free browser-based AI-generated Taipei GTA clone hits 1.2 million concurrent players in three days",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/free-browser-based-ai-generated-taipei-gta-clone-hits-1-2-million-concurrent-players-in-three-days-vibe-coded-game-cost-usd10-000-in-ai-tokens-to-build-is-set-on-the-streets-of-taipei",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T10:00:00+00:00",
    "summary": "Developers AICodeWith have vibe-coded and published a free browser-based game dubbed Taipei GTA. It reportedly cost $10,000 in tokens to get to this state."
  },
  {
    "id": "rss:https://www.tomshardware.com/service-providers/streaming/7-year-old-nvidia-shield-tv-pro-gets-shocking-50-percent-price-hike-driven-by-ai-memory-shortage-chipmaker-axes-entry-level-shield-tv-as-component-prices-soar",
    "domain": "AI 算力 / 半导体",
    "title": "7-year-old Nvidia Shield TV Pro gets shocking 50% price hike driven by AI memory shortage",
    "url": "https://www.tomshardware.com/service-providers/streaming/7-year-old-nvidia-shield-tv-pro-gets-shocking-50-percent-price-hike-driven-by-ai-memory-shortage-chipmaker-axes-entry-level-shield-tv-as-component-prices-soar",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T16:59:51+00:00",
    "summary": "The Shield TV Pro remains one of Nvidia’s longest-running consumer devices, but its $299.99 price tag now makes the streaming box considerably more expensive than when it launched."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/elon-musk-confirms-discussions-with-tsmc-about-terafab-chipmaking-collaboration-intel-is-the-only-other-named-partner-terafab-to-exclusively-supply-tesla-spacex-and-xai",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk confirms discussions with TSMC about Terafab chipmaking collaboration",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/elon-musk-confirms-discussions-with-tsmc-about-terafab-chipmaking-collaboration-intel-is-the-only-other-named-partner-terafab-to-exclusively-supply-tesla-spacex-and-xai",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T14:50:50+00:00",
    "summary": "Elon Musk and TSMC reportedly discuss multiple collaboration opportunities within the Terafab project."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/find-tech-deals-in-neweggs-fantastech-sale-ii-ahead-of-october-5-price-protection-guarantee-lets-you-start-shopping-now",
    "domain": "AI 算力 / 半导体",
    "title": "Find tech deals in Newegg's Fantastech Sale ahead of Amazon's Big Deals Day — early shoppers get automatic refunds if hardware prices drop lower",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/find-tech-deals-in-neweggs-fantastech-sale-ii-ahead-of-october-5-price-protection-guarantee-lets-you-start-shopping-now",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T14:40:00+00:00",
    "summary": "Ahead of Newegg's Fantastech Sale II launch on October 5th, you can grab some early deals and have price protection security if the product price drops lower in the sale proper."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/buying-used-cpus-can-expose-users-to-existing-bans-from-anti-cheat-engines-some-anti-cheat-engines-enforce-permanent-bans-while-others-have-an-expiration-date",
    "domain": "AI 算力 / 半导体",
    "title": "Buying used CPUs can expose users to existing bans from anti-cheat engines, and there's no way to check for violations before purchase",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/buying-used-cpus-can-expose-users-to-existing-bans-from-anti-cheat-engines-some-anti-cheat-engines-enforce-permanent-bans-while-others-have-an-expiration-date",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T14:09:00+00:00",
    "summary": "The CPU's previous owner apparently used it for cheating on Valorant, with its HWID getting flagged by Vanguard. When the Redditor bought and installed it on their PC, their Valorant account received "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/this-week-on-toms-hardware-premium-october-3-2026-ai-chip-design-week-openai-interview-and-ai-agent-safety",
    "domain": "AI 算力 / 半导体",
    "title": "This week on Tom's Hardware Premium: October 3, 2026",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/this-week-on-toms-hardware-premium-october-3-2026-ai-chip-design-week-openai-interview-and-ai-agent-safety",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T14:00:00+00:00",
    "summary": "This week on Tom's Hardware Premium, we open the floodgates with a free-to-access chip design week, including expert interviews, a sit-down with OpenAI on its custom ASIC, and much more."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/steam-revenue-hit-usd1-7-billion-in-september-2026-pc-gaming-spending-grows-despite-skyrocketing-hardware-costs",
    "domain": "AI 算力 / 半导体",
    "title": "Steam hits record $1.7 billion in September 2026 despite soaring PC hardware costs",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/steam-revenue-hit-usd1-7-billion-in-september-2026-pc-gaming-spending-grows-despite-skyrocketing-hardware-costs",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T13:35:00+00:00",
    "summary": "Steam's latest revenues highlight continued strength in PC gaming, with players continuing to spend heavily even as the cost of building and upgrading gaming PCs rises."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/futurum-ceo-says-agents-use-ai-5x-more-than-humans-number-will-eventually-hit-10x-but-agents-are-mostly-rereading-what-theyve-already-seen",
    "domain": "AI 算力 / 半导体",
    "title": "AI agents use 5x more tokens than humans as cached prompts explode, headed for 10x",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/futurum-ceo-says-agents-use-ai-5x-more-than-humans-number-will-eventually-hit-10x-but-agents-are-mostly-rereading-what-theyve-already-seen",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T13:10:00+00:00",
    "summary": "Daniel Newman’s number comes from OpenRouter data, where agents passed humans in February and grew 14x by August."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/scare-up-big-savings-in-bambu-labs-halloween-sale-right-now-with-up-to-30-percent-off-grab-usd250-off-the-dual-extruder-h2d-plus-bulk-spool-discounts-and-pumpkin-themed-bundles",
    "domain": "AI 算力 / 半导体",
    "title": "Scare up big savings in Bambu Lab's Halloween sale right now, with up to 30% off",
    "url": "https://www.tomshardware.com/3d-printing/scare-up-big-savings-in-bambu-labs-halloween-sale-right-now-with-up-to-30-percent-off-grab-usd250-off-the-dual-extruder-h2d-plus-bulk-spool-discounts-and-pumpkin-themed-bundles",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T12:50:00+00:00",
    "summary": "Don't let huge 3D printer prices scare you, because Bambu Lab's Halloween sale has knocked up to 30% off a new printer, with big bulk discounts on filament rolls, too."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/malicious-vpn-config-files-can-let-attackers-run-commands-on-asus-routers-companys-patch-also-fixes-a-bug-that-lets-a-logged-in-attacker-switch-on-telnet-with-root-access",
    "domain": "AI 算力 / 半导体",
    "title": "Malicious VPN config files can let attackers run commands on Asus routers",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/malicious-vpn-config-files-can-let-attackers-run-commands-on-asus-routers-companys-patch-also-fixes-a-bug-that-lets-a-logged-in-attacker-switch-on-telnet-with-root-access",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T12:30:00+00:00",
    "summary": "Until routers on Asus’s 3.0.0.6_102 firmware are updated, the company says not to import untrusted VPN files."
  },
  {
    "id": "rss:https://www.eetimes.com/autosens-2026-regulations-drive-automotive-sensing-architectures/",
    "domain": "AI 算力 / 半导体",
    "title": "AutoSens 2026: Regulation Drives Automotive Sensing Architectures",
    "url": "https://www.eetimes.com/autosens-2026-regulations-drive-automotive-sensing-architectures/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T15:58:50+00:00",
    "summary": "At AutoSens Europe, automotive sensing designs reflected tighter safety standards, advances in AI processing, and growing cybersecurity requirements. The post AutoSens 2026: Regulation Drives Automoti"
  },
  {
    "id": "rss:https://www.eetimes.com/continuous-health-monitoring-drives-integrated-wearable-system-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Continuous Health Monitoring Drives Integrated Wearable System Design",
    "url": "https://www.eetimes.com/continuous-health-monitoring-drives-integrated-wearable-system-design/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-02T11:29:26+00:00",
    "summary": "Analog Devices India’s Praveen Jose said device miniaturization is driving higher performance and quality in smaller form factors. The post Continuous Health Monitoring Drives Integrated Wearable Syst"
  },
  {
    "id": "rss:https://www.eetimes.com/qualcomm-doubles-down-on-agentic-ai-at-snapdragon-summit-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm Doubles Down on Agentic AI at Snapdragon Summit 2026",
    "url": "https://www.eetimes.com/qualcomm-doubles-down-on-agentic-ai-at-snapdragon-summit-2026/",
    "source": "Jim McGregor, Francis Sideco",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T17:31:45+00:00",
    "summary": "Qualcomm introduced two distinct Snapdragon 8 Elite Gen 6 SoCs for high-end smartphones as it expands personal agentic AI across mobile, wearables, and PCs. The post Qualcomm Doubles Down on Agentic A"
  },
  {
    "id": "rss:https://www.eetimes.com/edge-computing-and-security-for-access-control-applications-getting-the-best-of-the-two-worlds/",
    "domain": "AI 算力 / 半导体",
    "title": "Edge Computing and Security for Access Control Applications: Getting the Best of the Two Worlds",
    "url": "https://www.eetimes.com/edge-computing-and-security-for-access-control-applications-getting-the-best-of-the-two-worlds/",
    "source": "Arrow Electronics, Microchip",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T14:01:12+00:00",
    "summary": "Join us where attendees will see how on-device processing improves resilience, reduces exposure of sensitive data, counters spoofing, and supports practical deployment across buildings, smart locks, v"
  },
  {
    "id": "rss:https://www.eetimes.com/pcba-test-strategies-how-to-select-the-right-methodology-and-tester/",
    "domain": "AI 算力 / 半导体",
    "title": "PCBA Test Strategies: How to Select the Right Methodology and Tester",
    "url": "https://www.eetimes.com/pcba-test-strategies-how-to-select-the-right-methodology-and-tester/",
    "source": "Francesca Pinto, SPEA Electronic Test Products Copywriter",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T13:00:00+00:00",
    "summary": "Are you struggling with PCBA defects? Learn how to optimize your PCBA testing strategy by combining In-Circuit Testing (ICT), Functional Testing (FCT with Bed-of-Nails or Flying Probe Testers. The pos"
  },
  {
    "id": "rss:https://www.eetimes.com/small-electronics-manufacturers-save-big-on-erp/",
    "domain": "AI 算力 / 半导体",
    "title": "Small Electronics Manufacturers Save Big on ERP",
    "url": "https://www.eetimes.com/small-electronics-manufacturers-save-big-on-erp/",
    "source": "MRPeasy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T13:00:00+00:00",
    "summary": "Instead of traditional ERP, small electronics manufacturers are finding that affordable SME-focused manufacturing software provides needed functionality. The post Small Electronics Manufacturers Save "
  },
  {
    "id": "rss:https://www.eetimes.com/europe-space-industry-seeks-greater-supply-chain-control/",
    "domain": "AI 算力 / 半导体",
    "title": "Europe’s Space Industry Seeks Greater Supply Chain Control",
    "url": "https://www.eetimes.com/europe-space-industry-seeks-greater-supply-chain-control/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-01T09:57:15+00:00",
    "summary": "Europe's strategic space independence will depend on semiconductor supply chains, satellite networks, and 6G communications. The post Europe’s Space Industry Seeks Greater Supply Chain Control appeare"
  },
  {
    "id": "rss:https://www.eetimes.com/emergence-ai-to-deploy-neuroformal-ai-with-fabless-chipmakers/",
    "domain": "AI 算力 / 半导体",
    "title": "Emergence AI Targets Fabless Chipmakers With Neuroformal AI",
    "url": "https://www.eetimes.com/emergence-ai-to-deploy-neuroformal-ai-with-fabless-chipmakers/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T21:31:25+00:00",
    "summary": "See how Emergence AI is deploying neuroformal AI with chipmakers to boost wafer yields and tackle fab, test, and packaging failures. The post Emergence AI Targets Fabless Chipmakers With Neuroformal A"
  },
  {
    "id": "rss:https://www.eetimes.com/tsmcs-3-nm-ramp-looks-different-in-historical-context/",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC’s 3-nm Ramp Looks Different in Historical Context",
    "url": "https://www.eetimes.com/tsmcs-3-nm-ramp-looks-different-in-historical-context/",
    "source": "Ron Honig",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-30T15:40:17+00:00",
    "summary": "TSMC’s 3-nm node nears the revenue lead, but history shows 7 nm ramped faster; compare the data before evaluating 2 nm. The post TSMC’s 3-nm Ramp Looks Different in Historical Context appeared first o"
  },
  {
    "id": "hn:49657991",
    "domain": "AI 算力 / 半导体",
    "title": "How to Build a $20B Semiconductor Fab (2024)",
    "url": "https://www.construction-physics.com/p/how-to-build-a-20-billion-semiconductor",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-09-11T13:22:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49346906",
    "domain": "AI 算力 / 半导体",
    "title": "Ask HN: Do you feel comfortable admitting that you use AI?",
    "url": "https://news.ycombinator.com/item?id=49346906",
    "source": "var0xyz",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-18T15:16:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49913571",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/",
    "source": "bradleyg223",
    "platform": "hackernews",
    "points": 1699,
    "published_at": "2026-09-30T20:04:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49797982",
    "domain": "大厂 AI 动态",
    "title": "I said no and Apple said yes",
    "url": "https://dbushell.com/2026/09/22/apple-intelligence/",
    "source": "thatslast",
    "platform": "hackernews",
    "points": 886,
    "published_at": "2026-09-22T08:04:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49957116",
    "domain": "大厂 AI 动态",
    "title": "Turn off Apple Intelligence on macOS 27 and get its disk space back",
    "url": "https://github.com/omlahore/RemoveMacAI",
    "source": "privacyisntdead",
    "platform": "hackernews",
    "points": 576,
    "published_at": "2026-10-04T19:42:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49848269",
    "domain": "大厂 AI 动态",
    "title": "Ollaya – Ollama for open-source, Jev-style decision models",
    "url": "https://ollaya.dev/",
    "source": "Ardakilic",
    "platform": "hackernews",
    "points": 618,
    "published_at": "2026-09-25T18:33:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611251",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas: a high-resolution map of human DNA",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/",
    "source": "utiiiD",
    "platform": "hackernews",
    "points": 607,
    "published_at": "2026-09-08T14:55:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49715947",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Live and 3.8 Live Extended Thinking",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/",
    "source": "leumon",
    "platform": "hackernews",
    "points": 493,
    "published_at": "2026-09-15T17:38:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49790409",
    "domain": "大厂 AI 动态",
    "title": "Turn off and restrict access to Apple Intelligence features on Mac",
    "url": "https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac",
    "source": "alwillis",
    "platform": "hackernews",
    "points": 354,
    "published_at": "2026-09-21T17:30:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49817615",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 text-to-speech",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/",
    "source": "swolpers",
    "platform": "hackernews",
    "points": 331,
    "published_at": "2026-09-23T15:29:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49602490",
    "domain": "大厂 AI 动态",
    "title": "Emacs Bedrock 2.0",
    "url": "https://lambdaland.org/posts/2026-09-06-bedrock-v2/",
    "source": "ashton314",
    "platform": "hackernews",
    "points": 191,
    "published_at": "2026-09-07T20:12:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49727659",
    "domain": "大厂 AI 动态",
    "title": "The DeepMind Institute",
    "url": "https://institute.deepmind.com/",
    "source": "vertigoruntime",
    "platform": "hackernews",
    "points": 186,
    "published_at": "2026-09-16T14:32:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:49844896",
    "domain": "大厂 AI 动态",
    "title": "Microsoft abandons personal AI chatbot race with Copilot reboot",
    "url": "https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 157,
    "published_at": "2026-09-25T14:07:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49829387",
    "domain": "大厂 AI 动态",
    "title": "Hackers influence ChatGPT and Gemini to direct users to scam centers",
    "url": "https://medium.com/@arielsimon/dark-sourcery-how-hackers-manipulate-ai-to-scam-you-88df434d2073",
    "source": "ArielSimon",
    "platform": "hackernews",
    "points": 143,
    "published_at": "2026-09-24T11:54:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49914236",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon (High): Intelligence, Performance and Price Analysis",
    "url": "https://artificialanalysis.ai/models/gemini-4-argon",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 111,
    "published_at": "2026-09-30T20:50:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:49854945",
    "domain": "大厂 AI 动态",
    "title": "The Copilot+ PC brand is dead",
    "url": "https://www.windowscentral.com/microsoft/windows-11/the-copilot-pc-brand-is-dead-microsoft-and-pc-makers-quietly-pull-back-on-tarnished-windows-11-ai-pc-branding",
    "source": "bj-rn",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-09-26T09:55:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49697014",
    "domain": "大厂 AI 动态",
    "title": "Notes on gotchas while migrating 35kb preprompts from Opus to self-hosted Ollama",
    "url": "https://patrickmccanna.net/notes-on-migrating-large-prompts-away-from-anthropic-openai-to-self-hosted-llms/",
    "source": "0o_MrPatrick_o0",
    "platform": "hackernews",
    "points": 140,
    "published_at": "2026-09-14T13:59:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:49942592",
    "domain": "大厂 AI 动态",
    "title": "Gemini ending free use of Flash and Pro models",
    "url": "https://www.reddit.com/r/GeminiAI/comments/1wwalmc/wtf_google_getting_rid_of_free_gemini_flash_and/",
    "source": "rjh29",
    "platform": "hackernews",
    "points": 59,
    "published_at": "2026-10-03T09:13:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:49859982",
    "domain": "大厂 AI 动态",
    "title": "Faster prompt lookup drafting in llama.cpp",
    "url": "https://jadidbourbaki.github.io/blog/prompt-lookup-llama-cpp/",
    "source": "pptadversary",
    "platform": "hackernews",
    "points": 89,
    "published_at": "2026-09-26T19:57:24+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1003794/ai-education-computational-model-thought",
    "domain": "大厂 AI 动态",
    "title": "Our minds aren’t equipped to handle AI",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1003794/ai-education-computational-model-thought",
    "source": "Benjamin Riley",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T10:00:00+00:00",
    "summary": "Norbert Wiener, godfather of cybernetics, once said, \"The thought of every age is reflected in its technique.\" For the past century, our thought has been reflected in our computers, including by those"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1004616/the-new-fitbit-edge-leaks",
    "domain": "大厂 AI 动态",
    "title": "The new Fitbit Edge leaks",
    "url": "https://www.theverge.com/gadgets/1004616/the-new-fitbit-edge-leaks",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T21:02:09+00:00",
    "summary": "We don't know a ton about the Fitbit Edge, but it appears to be a successor to the midrange Charge line. It had leaked previously, but we can clearly see in these images posted by Android Headlines, y"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1004595/prick-industrial-glam-punk-album-review",
    "domain": "大厂 AI 动态",
    "title": "Prick’s theatrical industrial punk is perfect for spooky season",
    "url": "https://www.theverge.com/entertainment/1004595/prick-industrial-glam-punk-album-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T20:00:00+00:00",
    "summary": "While deep in the recording process for The Downward Spiral, Trent Reznor lent some of his production talents to old friend Kevin McMahon, from the new wave band Lucky Pierre (which Reznor was briefly"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/999447/best-early-amazon-prime-day-big-deals-sale-october",
    "domain": "大厂 AI 动态",
    "title": "The best early October Prime Day deals happening now",
    "url": "https://www.theverge.com/gadgets/999447/best-early-amazon-prime-day-big-deals-sale-october",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T17:18:00+00:00",
    "summary": "It’s not even October yet and Amazon is already offering some Prime Big Deal Day discounts on its own hardware, along with plenty of other popular products. It’s all to hype up October Prime Day, whic"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1004549/well-if-ai-said-it-it-must-be-true",
    "domain": "大厂 AI 动态",
    "title": "NJ’s former Lt Gov is using AI to say he’s innocent of sexual harassment",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1004549/well-if-ai-said-it-it-must-be-true",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T16:16:04+00:00",
    "summary": "New Jersey's lieutenant governor Dale Caldwell was forced to resign on September 25th after an investigation found he had sexually harassed a staffer and repeatedly violated ethics rules. The now-form"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1004543/openai-gpt-cheat-starcraft",
    "domain": "大厂 AI 动态",
    "title": "An AI couldn’t beat humans at StarCraft, so it decided to cheat",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1004543/openai-gpt-cheat-starcraft",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T15:21:59+00:00",
    "summary": "StarSkirmish pits AI-made StarCraft-playing bots against one another, as well as against human-made bots. OpenAI's GPT-6 Astra and Claude Opus 5.5 were essentially tied as the best-performing AI-made "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1004360/this-toolless-modular-lever-action-wallet-is-the-coolest-ive-stuck-to-my-phone",
    "domain": "大厂 AI 动态",
    "title": "This toolless modular lever-action wallet is the coolest I’ve stuck to my phone",
    "url": "https://www.theverge.com/gadgets/1004360/this-toolless-modular-lever-action-wallet-is-the-coolest-ive-stuck-to-my-phone",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T15:00:00+00:00",
    "summary": "This toolless modular lever-action wallet is the coolest I've stuck to my phone. Remember when I tested the ultra-thin and convenient OhSnap Snap Grip Stand and liked it so much I bought my own? Now, "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1004242/airpods-pro-3-amazon-october-prime-day-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The AirPods Pro 3 are a fantastic deal at $179",
    "url": "https://www.theverge.com/gadgets/1004242/airpods-pro-3-amazon-october-prime-day-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T13:00:00+00:00",
    "summary": "It’s been a while since we’ve seen a good discount on the Apple AirPods Pro 3, but like the latest iPad Mini and the M5 MacBook Airs, a great one is happening now for October Prime Day. You can snag a"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1000832/macbook-air-m5-amazon-prime-big-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The MacBook Air M5 is $200 off for the first time in months",
    "url": "https://www.theverge.com/gadgets/1000832/macbook-air-m5-amazon-prime-big-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T12:34:01+00:00",
    "summary": "Amazon’s October Prime Day has effectively chopped off Apple’s June price increases. Usually $1,299, the 13-inch MacBook Air with the M5 chip and 512GB of storage is on sale for $1,099 at Amazon. That"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1000323/apple-ipad-mini-amazon-prime-big-deal-days-sale",
    "domain": "大厂 AI 动态",
    "title": "The iPad Mini is slightly cheaper again during Prime Day",
    "url": "https://www.theverge.com/gadgets/1000323/apple-ipad-mini-amazon-prime-big-deal-days-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T12:31:50+00:00",
    "summary": "Apple bumped up prices on several of its devices in June, and we haven’t seen a good discount on the iPad Mini since. Just ahead of Amazon’s October Prime Big Deals Days, however, both Wi-Fi only and "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/04/google-froze-its-open-source-bug-bounty-program-due-to-a-significant-rise-in-ai-submissions/",
    "domain": "大厂 AI 动态",
    "title": "Google froze its open source bug bounty program due to a ‘significant rise’ in AI submissions",
    "url": "https://techcrunch.com/2026/10/04/google-froze-its-open-source-bug-bounty-program-due-to-a-significant-rise-in-ai-submissions/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T20:31:07+00:00",
    "summary": "AI slop seems to be overwhelming bug bounty programs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/04/can-super-intelligence-and-a-non-binding-safety-pact-solve-ais-image-problem/",
    "domain": "大厂 AI 动态",
    "title": "Can ‘super intelligence’ and a non-binding safety pact solve AI’s image problem?",
    "url": "https://techcrunch.com/2026/10/04/can-super-intelligence-and-a-non-binding-safety-pact-solve-ais-image-problem/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T20:08:34+00:00",
    "summary": "On Equity, we discussed the Trump administration's attempts to rebrand AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/04/techcrunch-mobility-reining-in-robotaxis/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: Reining in robotaxis",
    "url": "https://techcrunch.com/2026/10/04/techcrunch-mobility-reining-in-robotaxis/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T16:05:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, the role AI is playing in it."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/04/trump-unveils-his-new-super-intelligence-force/",
    "domain": "大厂 AI 动态",
    "title": "Trump unveils his new Super Intelligence Force",
    "url": "https://techcrunch.com/2026/10/04/trump-unveils-his-new-super-intelligence-force/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T15:15:10+00:00",
    "summary": "This new task force is Trump's latest response to the debate over AI safety."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/03/federal-judge-calls-flock-indiscriminate-mass-surveillance/",
    "domain": "大厂 AI 动态",
    "title": "Federal judge calls Flock ‘indiscriminate mass surveillance’",
    "url": "https://techcrunch.com/2026/10/03/federal-judge-calls-flock-indiscriminate-mass-surveillance/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T19:33:15+00:00",
    "summary": "A federal judge ruled that a sheriff’s deputy violated a woman’s Fourth Amendment rights when using Flock to search for her license plate without a warrant."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/03/amazon-responds-to-data-center-backlash-says-it-no-longer-uses-ndas/",
    "domain": "大厂 AI 动态",
    "title": "Amazon responds to data center backlash, says it no longer uses NDAs",
    "url": "https://techcrunch.com/2026/10/03/amazon-responds-to-data-center-backlash-says-it-no-longer-uses-ndas/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T18:43:57+00:00",
    "summary": "The CEO of Amazon Web Services tried to push back against widespread suspicion of data centers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/03/openai-safety-employee-resigns-claiming-the-companys-culture-is-broken/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI safety employee resigns, claiming the company’s ‘culture is broken’",
    "url": "https://techcrunch.com/2026/10/03/openai-safety-employee-resigns-claiming-the-companys-culture-is-broken/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T16:30:01+00:00",
    "summary": "By his own admission, David Robinson is “something of a cliché”: an employee at a leading AI company who issues a dire warning while resigning from their job."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/03/jack-dorseys-bitchat-disappears-from-app-stores-in-india-after-government-order/",
    "domain": "大厂 AI 动态",
    "title": "Jack Dorsey’s Bitchat disappears from app stores in India after government order",
    "url": "https://techcrunch.com/2026/10/03/jack-dorseys-bitchat-disappears-from-app-stores-in-india-after-government-order/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T15:02:01+00:00",
    "summary": "Bitchat has become largely unavailable in India as a result of the restrictions."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/03/vessev-built-an-electric-ferry-that-almost-flies/",
    "domain": "大厂 AI 动态",
    "title": "Vessev built an electric ferry that almost flies",
    "url": "https://techcrunch.com/2026/10/03/vessev-built-an-electric-ferry-that-almost-flies/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T14:42:00+00:00",
    "summary": "Vessev hopes its electric hydrofoil ferry will change the way people and cities think about boats."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/03/all-the-ai-agents-that-can-live-in-your-text-messages/",
    "domain": "大厂 AI 动态",
    "title": "All the AI agents that can live in your text messages",
    "url": "https://techcrunch.com/2026/10/03/all-the-ai-agents-that-can-live-in-your-text-messages/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T14:00:00+00:00",
    "summary": "We created a list of the most notable AI agents that can live in your text messages, from general assistants to agents designed for families, travel, and work."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/03/spotify-billionaires-body-scan-startup-has-come-to-america/",
    "domain": "大厂 AI 动态",
    "title": "Spotify billionaire’s body scan startup has come to America",
    "url": "https://techcrunch.com/2026/10/03/spotify-billionaires-body-scan-startup-has-come-to-america/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T14:00:00+00:00",
    "summary": "Farooq Abbasi, an investor in Neko Health, talked to Equity about the hot health tech company and what's next for it."
  },
  {
    "id": "rss:https://stratechery.com/2026/apple-and-a-hackers-future/",
    "domain": "大厂 AI 动态",
    "title": "Apple and a Hacker’s Future",
    "url": "https://stratechery.com/2026/apple-and-a-hackers-future/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T10:00:00+00:00",
    "summary": "I was happy for years in Apple's walled garden; with AI, however, their protections feel like limitations."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/new-forensice-evidence-supports-egyptian-retainer-sacrifice/",
    "domain": "大厂 AI 动态",
    "title": "New forensic evidence supports Egyptian \"retainer sacrifice\"",
    "url": "https://arstechnica.com/science/2026/10/new-forensice-evidence-supports-egyptian-retainer-sacrifice/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:52+00:00",
    "summary": "Fresh analysis of First Dynasty mass burials finds signs of fatal blunt force trauma on 39 percent of skulls"
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/lions-and-cheetahs-and-chimps-oh-my-a-spotlight-on-africas-diverse-wildlife/",
    "domain": "大厂 AI 动态",
    "title": "Lions and cheetahs and chimps, oh my: a spotlight on Africa's diverse wildlife",
    "url": "https://arstechnica.com/science/2026/10/lions-and-cheetahs-and-chimps-oh-my-a-spotlight-on-africas-diverse-wildlife/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T15:34:14+00:00",
    "summary": "Wunmi Mosaku (Sinners, Loki) narrates NatGeo's new documentary Africa: Earth's Wild Home"
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/all-hail-electrification-but-lets-talk-about-the-hard-part/",
    "domain": "大厂 AI 动态",
    "title": "All hail electrification. But let’s talk about the hard part.",
    "url": "https://arstechnica.com/science/2026/10/all-hail-electrification-but-lets-talk-about-the-hard-part/",
    "source": "Dan Gearino, Inside Climate News",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T11:05:53+00:00",
    "summary": "The IEA and climate negotiators want to set a target for shifting the economy to run on electricity."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/10/milt-windler-nasa-flight-director-who-helped-save-apollo-13-dies-at-94/",
    "domain": "大厂 AI 动态",
    "title": "Milt Windler, NASA flight director who helped save Apollo 13, dies at 94",
    "url": "https://arstechnica.com/space/2026/10/milt-windler-nasa-flight-director-who-helped-save-apollo-13-dies-at-94/",
    "source": "Robert Pearlman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T19:45:17+00:00",
    "summary": "\"...we were making history.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/the-dawn-of-the-age-of-the-exoskeleton/",
    "domain": "大厂 AI 动态",
    "title": "The dawn of the age of the exoskeleton",
    "url": "https://arstechnica.com/science/2026/10/the-dawn-of-the-age-of-the-exoskeleton/",
    "source": "Ildar Farkhatdinov, The Conversation",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T11:15:33+00:00",
    "summary": "The devices continue to show noticeable benefits for users in various real-world tasks."
  },
  {
    "id": "rss:https://www.producthunt.com/products/marv-3",
    "domain": "大厂 AI 动态",
    "title": "Marv",
    "url": "https://www.producthunt.com/products/marv-3",
    "source": "Cameron McHardy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T01:14:08+00:00",
    "summary": "An AI cursor companion that shows you what to click Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/xtracticle",
    "domain": "大厂 AI 动态",
    "title": "Xtracticle",
    "url": "https://www.producthunt.com/products/xtracticle",
    "source": "Ahmet Deveci",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T12:53:37+00:00",
    "summary": "Save X Articles and threads as PDF, Markdown or EPUB Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/netra",
    "domain": "大厂 AI 动态",
    "title": "Netra",
    "url": "https://www.producthunt.com/products/netra",
    "source": "prince",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T21:57:34+00:00",
    "summary": "A watchful notch with tools to keep you focused Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/chain-exchange",
    "domain": "大厂 AI 动态",
    "title": "Chain Exchange",
    "url": "https://www.producthunt.com/products/chain-exchange",
    "source": "Sadik Sani Namadi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T13:38:40+00:00",
    "summary": "Trade, bridge and move stablecoins across Arc Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/speechshield",
    "domain": "大厂 AI 动态",
    "title": "SpeechShield",
    "url": "https://www.producthunt.com/products/speechshield",
    "source": "SpeechShield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T15:59:56+00:00",
    "summary": "Live interview & meeting copilot for Mac, from your resume Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/iland",
    "domain": "大厂 AI 动态",
    "title": "iLand",
    "url": "https://www.producthunt.com/products/iland",
    "source": "Taha Çiftçi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-04T09:04:53+00:00",
    "summary": "Turn your Mac's notch into an everyday workspace Discussion | Link"
  },
  {
    "id": "hn:49619848",
    "domain": "股票",
    "title": "Apple iPod Engraver (2019)",
    "url": "https://dunstanorchard.com/apple-ipod-engraver/",
    "source": "NaOH",
    "platform": "hackernews",
    "points": 288,
    "published_at": "2026-09-09T01:57:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49826087",
    "domain": "股票",
    "title": "16GB iPod Nano 3G Upgrade",
    "url": "https://tuckerosman.com/projects/16gb-ipod-nano",
    "source": "Ivoah",
    "platform": "hackernews",
    "points": 167,
    "published_at": "2026-09-24T03:58:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49930086",
    "domain": "股票",
    "title": "US tells France and Germany to release diesel stocks or face US export ban",
    "url": "https://www.reuters.com/business/energy/us-tells-france-germany-release-diesel-stocks-or-face-us-export-ban-sources-say-2026-10-01/",
    "source": "geox",
    "platform": "hackernews",
    "points": 97,
    "published_at": "2026-10-02T05:22:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611240",
    "domain": "股票",
    "title": "iPod Classic 6G in QEMU",
    "url": "https://www.reddit.com/r/emulation/s/VL4Au2HGxq",
    "source": "dmonterocrespo",
    "platform": "hackernews",
    "points": 162,
    "published_at": "2026-09-08T14:54:57+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-art-of-doing-financial-engineering",
    "domain": "股票",
    "title": "The Art of Doing Financial Engineering",
    "url": "https://www.netinterest.co/p/the-art-of-doing-financial-engineering",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T11:57:49+00:00",
    "summary": "AI Financing at the Frontier"
  },
  {
    "id": "hn:49791944",
    "domain": "股票",
    "title": "Wall Street is growing skeptical of the data center boom",
    "url": "https://www.nytimes.com/2026/09/21/business/ai-data-center-ipos.html",
    "source": "mikhael",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-09-21T19:14:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49816810",
    "domain": "股票",
    "title": "Trump's 1,156 July Stock Trades Involved AI, Big Oil, Weapons-Makers, and More",
    "url": "https://www.commondreams.org/news/donald-trump-stock-trades",
    "source": "cirelli94",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-23T14:33:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49819274",
    "domain": "股票",
    "title": "Morgan Stanley Investment-Bank Deal List Leaked in Email Misfire",
    "url": "https://finance.yahoo.com/markets/stocks/articles/morgan-stanley-investment-bank-deal-124657863.html",
    "source": "wslh",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-09-23T17:08:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49594296",
    "domain": "股票",
    "title": "OpenAI 2025 financials $38.5B loss ahead of IPO",
    "url": "https://qz.com/openai-leaked-financials-losses-revenue-ipo-061626",
    "source": "u1hcw9nx",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-09-07T05:41:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49810905",
    "domain": "股票",
    "title": "In 2025, 49 percent of adults under age 30 lived with a parent [pdf]",
    "url": "https://www.federalreserve.gov/publications/files/2025-report-economic-well-being-us-households-202605.pdf",
    "source": "gscott",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-09-23T02:26:49+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-agents-revolt",
    "domain": "股票",
    "title": "Agents Revolt",
    "url": "https://www.netinterest.co/p/the-agents-revolt",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:33:27+00:00",
    "summary": "What happens to finance when customers start paying attention"
  },
  {
    "id": "rss:https://www.netinterest.co/p/brookfield-of-dreams",
    "domain": "股票",
    "title": "Brookfield of Dreams",
    "url": "https://www.netinterest.co/p/brookfield-of-dreams",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T15:05:47+00:00",
    "summary": "Inside Brookfield&#8217;s Plan to Double Again"
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-five-deals-that-made-apollo",
    "domain": "股票",
    "title": "The Five Deals That Made Apollo",
    "url": "https://www.netinterest.co/p/the-five-deals-that-made-apollo",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T15:25:40+00:00",
    "summary": "From distressed debt to a trillion-dollar machine"
  },
  {
    "id": "rss:https://www.netinterest.co/p/hot-european-summer",
    "domain": "股票",
    "title": "Hot European Summer",
    "url": "https://www.netinterest.co/p/hot-european-summer",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T16:33:06+00:00",
    "summary": "Europe is outperforming &#8211; but Europeans aren&#8217;t participating"
  },
  {
    "id": "rss:https://www.netinterest.co/p/untangling-guggenheim",
    "domain": "股票",
    "title": "Untangling Guggenheim",
    "url": "https://www.netinterest.co/p/untangling-guggenheim",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T15:05:53+00:00",
    "summary": "How Private Credit Built Its Own Universe"
  },
  {
    "id": "rss:https://www.netinterest.co/p/great-scott",
    "domain": "股票",
    "title": "Great Scott",
    "url": "https://www.netinterest.co/p/great-scott",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-21T17:35:18+00:00",
    "summary": "Challenges Facing the Bond Trader in Chief"
  },
  {
    "id": "rss:https://www.netinterest.co/p/financing-the-ai-boom-3",
    "domain": "股票",
    "title": "Financing the AI Boom 3",
    "url": "https://www.netinterest.co/p/financing-the-ai-boom-3",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-14T16:46:59+00:00",
    "summary": "Nvidia, Guarantor of Last Resort"
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
    "id": "hn:49778029",
    "domain": "金融",
    "title": "Samsung is expected to more than double output of its HBM4 and HBM4E DRAM",
    "url": "https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 562,
    "published_at": "2026-09-20T17:38:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49594251",
    "domain": "金融",
    "title": "Switzerland's Federal Government Is Replacing Microsoft on 3k Computers",
    "url": "https://itsfoss.com/news/switzerland-replace-microssoft-pilot/",
    "source": "ivell",
    "platform": "hackernews",
    "points": 371,
    "published_at": "2026-09-07T05:33:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49875913",
    "domain": "金融",
    "title": "Parley: Federated, decentralised chat that speaks plain IRC",
    "url": "https://git.mills.io/prologic/parley",
    "source": "davidcollantes",
    "platform": "hackernews",
    "points": 330,
    "published_at": "2026-09-28T10:30:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49921118",
    "domain": "金融",
    "title": "Meta Uses A.I. Data Centers to Avoid Billions in Federal Taxes",
    "url": "https://www.nytimes.com/2026/09/30/technology/meta-ai-data-centers-taxes.html",
    "source": "gmays",
    "platform": "hackernews",
    "points": 255,
    "published_at": "2026-10-01T13:05:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49822556",
    "domain": "金融",
    "title": "OpenAI breaches Medicare, Albanese reveals",
    "url": "https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html",
    "source": "jonnonz",
    "platform": "hackernews",
    "points": 256,
    "published_at": "2026-09-23T21:01:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49704008",
    "domain": "金融",
    "title": "Amazon vs. Perplexity – U.S. Court of Appeals for the Ninth Circuit",
    "url": "https://law.justia.com/cases/federal/appellate-courts/ca9/26-1444/26-1444-2026-08-04.html",
    "source": "neom",
    "platform": "hackernews",
    "points": 219,
    "published_at": "2026-09-14T21:05:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49904408",
    "domain": "金融",
    "title": "Tesla takes on $30B in credit as it approaches unprofitability",
    "url": "https://electrek.co/2026/09/29/tesla-takes-on-30-billion-in-credit-as-it-approaches-unprofitability/",
    "source": "ciconia",
    "platform": "hackernews",
    "points": 161,
    "published_at": "2026-09-30T04:37:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49731356",
    "domain": "金融",
    "title": "Fed hikes rates as inflation worries push up bond yields",
    "url": "https://www.reuters.com/live/live-fed-rate-hike-expected-inflation-worries-push-up-bond-yields-2026-09-16/",
    "source": "wslh",
    "platform": "hackernews",
    "points": 184,
    "published_at": "2026-09-16T18:55:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49916668",
    "domain": "金融",
    "title": "10-year Treasury yield climbs above 5.3% to a level not seen in 24 years",
    "url": "https://www.wsj.com/finance/investing/surging-yields-bring-the-bond-market-back-to-the-turn-of-the-century-2b74773f",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-10-01T01:40:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49832844",
    "domain": "金融",
    "title": "Federal judge orders Texas to air condition all prisons by the end of 2029",
    "url": "https://www.texastribune.org/2026/09/22/texas-prison-air-conditioning-lawsuit-ruling/",
    "source": "bonefishgrill",
    "platform": "hackernews",
    "points": 120,
    "published_at": "2026-09-24T16:15:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49600997",
    "domain": "金融",
    "title": "No constitutional right to clean water, federal court finds",
    "url": "https://www.usatoday.com/story/news/nation/2026/09/07/court-constitution-right-clean-water/91649488007/",
    "source": "measurablefunc",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-09-07T17:52:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49916955",
    "domain": "金融",
    "title": "Cities Are Forced to Funnel License Plate Data to a Federal Surveillance Program",
    "url": "https://www.404media.co/how-cities-are-forced-to-funnel-license-plate-data-to-a-massive-federal-surveillance-program-hidta/",
    "source": "ripe",
    "platform": "hackernews",
    "points": 92,
    "published_at": "2026-10-01T02:26:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:49591672",
    "domain": "金融",
    "title": "Hackers have withdrawn ~4k BTC (~$320M) from the Liquid Federation wallet",
    "url": "https://twitter.com/Liquid_BTC/status/2096696272447218108",
    "source": "felipelalli",
    "platform": "hackernews",
    "points": 126,
    "published_at": "2026-09-06T22:43:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49930690",
    "domain": "金融",
    "title": "Quantitative Finance with OCaml",
    "url": "https://qcaml.com/index.html",
    "source": "leonry",
    "platform": "hackernews",
    "points": 52,
    "published_at": "2026-10-02T07:14:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49938815",
    "domain": "金融",
    "title": "Federal Judge Rules a Flock Search Was Unconstitutional",
    "url": "https://www.404media.co/federal-judge-rules-a-flock-search-was-indiscriminate-mass-surveillance-and-unconstitutional/",
    "source": "pavel_lishin",
    "platform": "hackernews",
    "points": 51,
    "published_at": "2026-10-02T21:28:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49694840",
    "domain": "金融",
    "title": "How Much Has Trump Made from Crypto? ($1.4B from 2025 Federal Disclosure)",
    "url": "https://www.thepricer.org/how-much-has-trump-made-from-crypto/",
    "source": "cinderelacinder",
    "platform": "hackernews",
    "points": 114,
    "published_at": "2026-09-14T10:56:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596610",
    "domain": "金融",
    "title": "Initial effects of AI technology on employment look positive",
    "url": "https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here",
    "source": "MrBuddyCasino",
    "platform": "hackernews",
    "points": 103,
    "published_at": "2026-09-07T10:38:32+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.02834",
    "domain": "金融",
    "title": "Axient: Canonical Protocol-Graph Composition for Leveraged Event Markets: Single State Authority, Atomic Composition, Durable Sagas, and Exactly-Once Recovery",
    "url": "https://arxiv.org/abs/2610.02834",
    "source": "Maksym Nechepurenko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2610.02834v1 Announce Type: new Abstract: A modular leveraged event-market protocol can contain individually correct contracts for risk approval, positions, debt, settlement evidence, credit poo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.02838",
    "domain": "金融",
    "title": "Axient: Manifest-Bound Evidence for On-Chain Financial Protocols: Seven-Layer Derivation, Correlation, Tamper Rejection, and Reproducible Claim Promotion",
    "url": "https://arxiv.org/abs/2610.02838",
    "source": "Maksym Nechepurenko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2610.02838v1 Announce Type: new Abstract: Hybrid on-chain financial protocols are frequently evaluated with evidence that is individually useful but collectively insufficient: a unit test, trans"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.02863",
    "domain": "金融",
    "title": "Multi-Agent AI as a Nested Principal-Agent Problem in Private Wealth Management: Mandate Representation and Evidence Control in Switzerland, Germany and Austria",
    "url": "https://arxiv.org/abs/2610.02863",
    "source": "Walter Kurz, Reinhard Magg, Florian Kollberg, Wojtek Stricker, Stefan Marx, Frank Reinhardt, Velimir Dedi\\'c",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2610.02863v1 Announce Type: new Abstract: In private wealth management, a manager delegating to artificial intelligence (AI) acts as the client's agent and the system's principal. We introduce a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.02917",
    "domain": "金融",
    "title": "Event History Over Scale: Compact Transformers for Low-Latency Limit Order Book Forecasting",
    "url": "https://arxiv.org/abs/2610.02917",
    "source": "David Schaurecker, Lasse B. Strand, Kevin O'Sullivan, Robert Jakob",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2610.02917v1 Announce Type: new Abstract: Short-horizon price-trend prediction from limit order books in equity and intraday electricity markets requires models that combine predictive quality w"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.03076",
    "domain": "金融",
    "title": "Shapley-based Structural Analysis of Neural Calibration for Stochastic Volatility Models",
    "url": "https://arxiv.org/abs/2610.03076",
    "source": "Sha\\\"in Afzali, Serena Della Corte, Antonis Papapantoleon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2610.03076v1 Announce Type: new Abstract: Neural network-based approaches have emerged as efficient alternatives to traditional optimization-based procedures for the calibration of stochastic vo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.03250",
    "domain": "金融",
    "title": "No Women No Innovation? The Effect of Women on Boards on Hard and Soft Innovation in SMEs",
    "url": "https://arxiv.org/abs/2610.03250",
    "source": "Francesca Pascale, Saverio Barabuffi, Giulio Ferrigno",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2610.03250v1 Announce Type: new Abstract: The role of women on corporate boards and its impact on innovation remains heavily debated. While existing literature offers conflicting perspectives on"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.03369",
    "domain": "金融",
    "title": "Mixture-of-Experts for Cryptocurrency Order Execution: Training Stability, Tail Risk, and Failure Modes",
    "url": "https://arxiv.org/abs/2610.03369",
    "source": "Alexander Ardaiz, Varun Budati, Ali Habibnia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2610.03369v1 Announce Type: new Abstract: Deep reinforcement-learning policies for order execution can vary substantially across training seeds, so apparent architectural gains may reflect favou"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.03406",
    "domain": "金融",
    "title": "PreFER: Interactive Robo-Advisor with Scoring Mechanism",
    "url": "https://arxiv.org/abs/2610.03406",
    "source": "Yuwei Wang, Hoi Ying Wong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2610.03406v1 Announce Type: new Abstract: We propose an interactive robo-advising framework that learns personalized risk preferences from scores provided by clients. The resulting preference-le"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.03598",
    "domain": "金融",
    "title": "When a Correct Reward Is Not Enough: Diagnosing and Guiding PPO in an Analytically Solved Broker-Trader Game",
    "url": "https://arxiv.org/abs/2610.03598",
    "source": "Siu Tung Wong (Institute of Finance and Technology, University College London), Carlo Campajola (Institute of Finance and Technology, University College London, UZH Blockchain Center)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2610.03598v1 Announce Type: new Abstract: Reinforcement learning (RL) is increasingly used for financial optimal-control problems when complex dynamics make analytical strategies difficult to ob"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.02290",
    "domain": "金融",
    "title": "Expected Utility Regret Rule: Minimax and Bayes Optimal Portfolio Choice",
    "url": "https://arxiv.org/abs/2610.02290",
    "source": "Masahiro Kato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2610.02290v1 Announce Type: cross Abstract: This study considers the problem of portfolio choice, where we recommend a portfolio to an investor to maximize the expected utility of their wealth. "
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.03080",
    "domain": "金融",
    "title": "MintEval: Do LLMs Implement the Trading Strategy You Asked For? A Behavioural-Equivalence Benchmark for Natural-Language-to-Strategy Code",
    "url": "https://arxiv.org/abs/2610.03080",
    "source": "Siyu Wang, Yifan Wang, Yuecheng He",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2610.03080v1 Announce Type: cross Abstract: Large language models are moving from producing trading signals to writing the code that executes them. The failure mode of the second role is silent:"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.03161",
    "domain": "金融",
    "title": "Landscape-Dependent Performance of Photonic Quantum Solvers in QUBO Feature Selection for Financial Risk Detection",
    "url": "https://arxiv.org/abs/2610.03161",
    "source": "Nirvik Sahoo, Paul Robert Griffin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2610.03161v1 Announce Type: cross Abstract: Feature selection for imbalanced classification tasks such as credit card fraud and consumer default detection requires balancing predictive relevance"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.03174",
    "domain": "金融",
    "title": "FinNextAssist: Towards Professional Financial Deep Research Assistant",
    "url": "https://arxiv.org/abs/2610.03174",
    "source": "Xiangyu Li, Fengbin Zhu, Xuan Yao, Siyu Liu, Xiaoluan Liu, Chao Wang, Huanbo Luan, Xiaofen Xing, Xiangmin Xu, Ke-Wei Huang, Richang Hong, Tat-Seng Chua",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2610.03174v1 Announce Type: cross Abstract: Deep Research (DR) agents have demonstrated strong capabilities in complex, research-oriented tasks through autonomous planning, iterative retrieval, "
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.20060",
    "domain": "金融",
    "title": "Constrained portfolio optimization in a life-cycle model: A deep pricing kernel approach",
    "url": "https://arxiv.org/abs/2410.20060",
    "source": "Wenyuan Li, Pengyu Wei",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2410.20060v5 Announce Type: replace Abstract: This paper considers the constrained portfolio optimization in a generalized life-cycle model. The individual with a stochastic income manages a por"
  },
  {
    "id": "rss:https://arxiv.org/abs/2502.12774",
    "domain": "金融",
    "title": "When defaults cannot be hedged: xVA calculations via local risk-minimization",
    "url": "https://arxiv.org/abs/2502.12774",
    "source": "Francesca Biagini, Alessandro Gnoatto, Katharina Oberpriller",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2502.12774v3 Announce Type: replace Abstract: We consider the pricing and hedging of counterparty credit risk and funding when there is no possibility to hedge the jump to default of either the "
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.08152",
    "domain": "金融",
    "title": "Optimal Fees for Liquidity Provision in Automated Market Makers",
    "url": "https://arxiv.org/abs/2508.08152",
    "source": "Steven Campbell, Philippe Bergault, Jason Milionis, Marcel Nutz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2508.08152v2 Announce Type: replace Abstract: Passive liquidity providers (LPs) in automated market makers (AMMs) face losses due to adverse selection (LVR), which static trading fees often fail"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.09452",
    "domain": "金融",
    "title": "Optimal Investment and Consumption in a Stochastic Factor Model",
    "url": "https://arxiv.org/abs/2509.09452",
    "source": "Florian Gutekunst, Martin Herdegen, David Hobson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2509.09452v2 Announce Type: replace Abstract: In this article, we study optimal investment and consumption in an incomplete stochastic factor model for a power utility investor on the infinite h"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.13597",
    "domain": "金融",
    "title": "Daycare Matching with Siblings: Social Implementation and Welfare Evaluation",
    "url": "https://arxiv.org/abs/2604.13597",
    "source": "Kan Kuno, Daisuke Moriwaki, Yoshihiro Takenami",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2604.13597v4 Announce Type: replace Abstract: In centralized matching markets, agents may value joint assignment, as with siblings or couples. Standard preference estimation ignores such complem"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.25353",
    "domain": "金融",
    "title": "The Risk-Neutral Crash Frontier: Sharp Joint Bounds on Crash Probability and Conditional Depth from Option Bid-Ask Quotes",
    "url": "https://arxiv.org/abs/2607.25353",
    "source": "Jirong Zhuang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2607.25353v5 Announce Type: replace Abstract: Index put prices are the market's quotes for crash insurance, and a put's value equals the probability of a crash times the expected shortfall given"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.23274",
    "domain": "金融",
    "title": "The Physical Crash Frontier: What Finite Option Quotes Can and Cannot Reveal",
    "url": "https://arxiv.org/abs/2608.23274",
    "source": "Jirong Zhuang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2608.23274v3 Announce Type: replace Abstract: Physical crash probabilities recovered from option prices depend on a pricing kernel and on a risk-neutral distribution that finitely many bid and a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2610.01562",
    "domain": "金融",
    "title": "Social welfare and price discovery in double auction markets",
    "url": "https://arxiv.org/abs/2610.01562",
    "source": "Teemu Pennanen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2610.01562v2 Announce Type: replace Abstract: The tendency of the double auction mechanism to drive prices to competitive equilibrium has been well documented in laboratory experiments, but the "
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.20239",
    "domain": "金融",
    "title": "Error Propagation in Dynamic Programming: From Stochastic Control to American Option Pricing",
    "url": "https://arxiv.org/abs/2509.20239",
    "source": "Andrea Della Vecchia, Damir Filipovi\\'c",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2509.20239v2 Announce Type: replace-cross Abstract: This paper investigates theoretical and methodological foundations for stochastic optimal control (SOC) in discrete time. We start formulating"
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.08120",
    "domain": "金融",
    "title": "Optimal Quantum Speedups for Repeatedly Nested Expectation Estimation",
    "url": "https://arxiv.org/abs/2602.08120",
    "source": "Yihang Sun, Guanyang Wang, Jose Blanchet",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2602.08120v2 Announce Type: replace-cross Abstract: We study the estimation of repeatedly nested expectations (RNEs) with a constant horizon (number of nestings) using quantum computing. We prop"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.18287",
    "domain": "金融",
    "title": "A continuous-time dynamic contracting problem with limited liability and finite horizon",
    "url": "https://arxiv.org/abs/2609.18287",
    "source": "Andrea Bovo, Tiziano De Angelis, St\\'{e}phane Villeneuve",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-05T04:00:00+00:00",
    "summary": "arXiv:2609.18287v2 Announce Type: replace-cross Abstract: We perform a detailed study of a principal--agent problem in a continuous time version of the celebrated Holmstr\\\"om--Milgrom model (Econometr"
  },
  {
    "id": "hn:49924299",
    "domain": "金融",
    "title": "Sony released the first CD audio player on this day in 1982",
    "url": "https://www.tomshardware.com/pc-components/storage/sony-released-the-first-cd-audio-player-on-this-day-in-1982-player-cost-usd3-700-when-adjusted-for-inflation-but-it-would-be-another-decade-before-the-cd-rom-driven-multimedia-pc-era-began",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-01T17:07:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49700413",
    "domain": "金融",
    "title": "US 10-Year Breaches 5% as Inflation, Supply Worries Mount",
    "url": "https://www.bloomberg.com/news/articles/2026-09-14/us-10-year-yield-breaches-5-as-inflation-supply-worries-mount",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-09-14T17:11:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49849986",
    "domain": "金融",
    "title": "Show HN: Ekselio – Loveable for finance workflows (local first)",
    "url": "https://www.gptbeyond.com/try?home=1",
    "source": "kdautaj",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-09-25T21:09:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:49612981",
    "domain": "金融",
    "title": "DOJ Blocked ICE Agent Shooting Charge over Federal Prosecutor's Objections",
    "url": "https://www.propublica.org/article/doj-blocks-charges-ice-agent-minneapolis-julio-cesar-sosa-celis",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-09-08T16:54:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49828019",
    "domain": "金融",
    "title": "Show HN: Trader News – Hacker News for Finance",
    "url": "https://news.ycombinator.com/item?id=49828019",
    "source": "FailMore",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-09-24T08:54:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49625461",
    "domain": "金融",
    "title": "Teen reading slumps to worst this century due to surge in screen time",
    "url": "https://finance.yahoo.com/news/teen-reading-slumps-worst-century-111013754.html",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-09-09T12:29:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49769668",
    "domain": "金融",
    "title": "OpenAI and Anthropic oversold AI security breaches",
    "url": "https://nypost.com/2026/09/19/us-news/openai-anthropic-oversold-security-breaches-to-pressure-feds-into-protecting-turf-insiders/",
    "source": "hei-lima",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-09-19T19:59:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:49730769",
    "domain": "金融",
    "title": "Feds Want California to Give Up 14 Years of Broadband Protections. It Should Sue",
    "url": "https://cyberlaw.stanford.edu/blog/2026/09/california-is-being-asked-to-give-up-14-years-of-broadband-protections-it-doesnt-have-to/",
    "source": "rsingel",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-09-16T18:09:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:49633640",
    "domain": "金融",
    "title": "DHS Program Analyzes Americans' Finances to Flag Drivers for Traffic Stops",
    "url": "https://www.military.com/dhs-program-analyzes-americans-finances-to-flag-drivers-for-traffic-stops-report",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-09-09T20:22:20+00:00",
    "summary": ""
  }
]
```
