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

- 今日日期：`2026-07-02`
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
  "date": "2026-07-02",
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
    "points": 3527207,
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
    "points": 1391896,
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
    "points": 1313350,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 918177,
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
    "points": 819030,
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
    "points": 688917,
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
    "points": 507776,
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
    "points": 478195,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 416038,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1GX9dYWEPw",
    "domain": "AI",
    "title": "我居然能在MC里玩到这么好玩的摸金服务器！",
    "url": "http://www.bilibili.com/video/av114108926068217",
    "source": "物骨",
    "platform": "bilibili",
    "points": 316063,
    "published_at": "2025-03-06T21:00:00+00:00",
    "summary": "视频内容均来自《LRL服务器》\n服务器游玩方式看评论区置顶\n无需正版，不卖数值，爆率嘎嘎高，不会跑路"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 299013,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 229383,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1VDTv6rEtM",
    "domain": "AI",
    "title": "终于，Claude Code 封号原因被曝光了！竟然针对中国用户，植入隐形代码？",
    "url": "http://www.bilibili.com/video/av116844031774993",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 210350,
    "published_at": "2026-07-01T09:35:43+00:00",
    "summary": "Claude Code 封号原因终于找到了！国外开发者逆向 Claude Code 源码，发现 Anthropic 在客户端里藏了一套隐蔽的用户标记系统，这期视频带你完整还原封号真相。\n开源 AI 编程教程：github.com/liyupi/ai-guide\n编程学习教程+实战项目+简历模板：codefather.cn\n最近 AI 圈儿不太平啊，OpenAI Codex 封号、Cursor 地区"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 175986,
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
    "points": 163654,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV16LTw6xEJT",
    "domain": "AI",
    "title": "今天你的Claude code被封了么？",
    "url": "http://www.bilibili.com/video/av116839652857330",
    "source": "AIwood爱屋研究室",
    "platform": "bilibili",
    "points": 122508,
    "published_at": "2026-06-30T15:04:42+00:00",
    "summary": "肯定是西湖醋鱼的锅！"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 113558,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 101196,
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
    "points": 92339,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1xBrDB9E42",
    "domain": "AI",
    "title": "独立开发太累？Godot + Claude Code 搭建 AI 辅助工作流，效率直接起飞！ | 地块召唤师开发实战 #01",
    "url": "http://www.bilibili.com/video/av115911319100158",
    "source": "像素夹心饼干",
    "platform": "bilibili",
    "points": 66086,
    "published_at": "2026-01-18T03:25:00+00:00",
    "summary": "大家好，这里是饼干！🍪\n这是我的新坑——**《地块召唤师》**开发实战分享的第一期。\n很多朋友问独立开发如何提升效率？这期视频我不聊虚的，直接公开我从 0 到 1 搭建的 AI + Godot 高效工作流。\n从游戏引擎的选择，到 Claude Code、Copilot 等 AI 工具的实战配置，再到如何用“明确需求”的方法论（SMART原则+双钻模型）来驾驭 AI，让它不仅仅是写代码的工具，更成为"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 59390,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 52651,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 49859,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 45659,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 40998,
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
    "points": 33638,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29857,
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
    "points": 28699,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1YV7W6YEFU",
    "domain": "AI",
    "title": "方向错了！手机跟AI Agent到底该怎么结合？",
    "url": "http://www.bilibili.com/video/av116822892418628",
    "source": "我是HYK",
    "platform": "bilibili",
    "points": 28240,
    "published_at": "2026-06-28T03:00:00+00:00",
    "summary": "方向错了！一句话订票、点咖啡，这种极其容易出错的Agent，几乎没有坚持用下来的用户；现阶段手机需要的是短链路、点到为止的AI Agent。"
  },
  {
    "id": "bvid:BV1bh3LzqEze",
    "domain": "AI",
    "title": "Chatbox AI终端：跨平台+MCP+知识库+开源+免费！一键连接所有AI语言模型！手把手安装使用指南！",
    "url": "http://www.bilibili.com/video/av114793218380950",
    "source": "_Smzh_",
    "platform": "bilibili",
    "points": 27600,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV1RUDsBWEHb",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的Cursor+Skills实战指南教程，手把手带你开发爆款app，全程干货无废话！比付费效果强十倍！",
    "url": "http://www.bilibili.com/video/av116373464350785",
    "source": "AI大模型技术教程",
    "platform": "bilibili",
    "points": 24798,
    "published_at": "2026-04-09T10:15:00+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\nCursor+Skills频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV1XxXpBEEHU",
    "domain": "AI",
    "title": "Claude Code远程开发终极方案！手机改代码+实时预览~【小白教程】",
    "url": "http://www.bilibili.com/video/av116294326230438",
    "source": "爱听书的程序员阿超",
    "platform": "bilibili",
    "points": 20682,
    "published_at": "2026-03-26T12:00:00+00:00",
    "summary": "之前，我一直在研究怎么远程使用 Claude Code 开发项目，并且能实时预览效果。但是一直都没有找到合适的解决方案，要么就是给一个临时公网链接预览，每次都需要再配置，要么就是购买云服务器来配置，都感觉挺麻烦的~\n\n最近，我发现这个蒲公英异地组网的方案，用来做远程开发 Claude Code 项目，感觉非常方便，不仅能修改代码，而且我实时预览的需求也很好的满足了。\n\n这样我随时随地都可以用 AI"
  },
  {
    "id": "bvid:BV1VbUCBAEZS",
    "domain": "AI",
    "title": "鸿蒙电脑上跑 Claude Code？我真的做到了！",
    "url": "http://www.bilibili.com/video/av115604514148535",
    "source": "jadeCircuit",
    "platform": "bilibili",
    "points": 18789,
    "published_at": "2025-11-24T11:55:31+00:00",
    "summary": "在这期视频中，我展示了我是如何在 HarmonyOS PC 上，通过 HiSH 的 Alpine Linux Shell 让 Claude Code 成功运行的，虽然 HarmonyOS 本身并不支持这些工具。\n华为最近发布了 HarmonyOS PC 版 DevEco Studio 预览版。这个 IDE 整体体验已经很好了，但仍然缺少像 Claude Code 这样强大的 AI 编码工具。\n 所"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17469,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1ssEE6CEks",
    "domain": "AI",
    "title": "Ai自动画图：CAD建筑平面图测试（CodexGPT5.5）",
    "url": "http://www.bilibili.com/video/av116719259485897",
    "source": "Tutor南洋",
    "platform": "bilibili",
    "points": 17205,
    "published_at": "2026-06-09T08:47:15+00:00",
    "summary": "体验一下ai画图，不过CAD软件基本操作也不能拉下~\nCAD教学基础入门视频合集↓\n传送门：BV1aT4y1B7oY\n整个合集教学的，不要跳着看啊喂！\n看完了那基本就能跟上啦，提问请@我，不然评论太多我是看不到的"
  },
  {
    "id": "bvid:BV1cCEi6sEU5",
    "domain": "AI",
    "title": "🦊他能成功吗？Claude Code 接管虚幻引擎5，打造一款游戏 | 带你走完整个流程",
    "url": "http://www.bilibili.com/video/av116731724959171",
    "source": "Apeak_虚幻丰哥",
    "platform": "bilibili",
    "points": 16966,
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
    "points": 13628,
    "published_at": "2026-06-27T01:52:00+00:00",
    "summary": "当了一年多的 Cursor 重度用户，最近把它退订了。\n\n不是它变差了，是 Claude Code 和 Codex 真的太好用了。\n\n几个真实感受： ① 大模型越来越强，我已经不怎么手写代码了 ② Cursor 套的是 VS Code 壳子，只属于程序员 ③ 底层模型不在一个量级——Claude 有 Opus 和 Fable 5，Codex 有 GPT 5.5/5.6，Cursor 的 Compo"
  },
  {
    "id": "bvid:BV165dAYxEdD",
    "domain": "AI",
    "title": "只需几行代码用Java写一个MCP服务！从0到1开发MCP服务！",
    "url": "http://www.bilibili.com/video/av114306863598282",
    "source": "图灵诸葛官方号",
    "platform": "bilibili",
    "points": 12205,
    "published_at": "2025-04-09T07:43:00+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持~\r\n本视频配套资料戳这里获取→https://www.bilibili.com/read/cv38661345/\r\n【还可额外领取100w字Java面试宝典】"
  },
  {
    "id": "bvid:BV1etEQ6DETs",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116724192118321",
    "source": "AI产品经理大模型",
    "platform": "bilibili",
    "points": 11396,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1TtwCehEzG",
    "domain": "AI",
    "title": "cursor新手必会的怎么回退代码 防止改错改乱代码 提高效率开发",
    "url": "http://www.bilibili.com/video/av113855472605087",
    "source": "项目禅",
    "platform": "bilibili",
    "points": 11246,
    "published_at": "2025-01-19T14:29:21+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV14j81zPEtu",
    "domain": "AI",
    "title": "ChatGPT Agent 完整测评 (附10大用法案例)",
    "url": "http://www.bilibili.com/video/av114948105572340",
    "source": "李厂长来了",
    "platform": "bilibili",
    "points": 8840,
    "published_at": "2025-08-01T12:00:00+00:00",
    "summary": "上周，OpenAI 正式推出了ChatGPT Agent，网上对 ChatGPT Agent 的评价褒贬不一，有人觉得 OpenAI 终于走到了 Agent 这个阶段，是巨大的突破；也有人吐槽，说同类的其他产品早就已经做得比 OpenAI 还要更好。\n\n今天我们就用10个案例来实测，看看ChatGPT Agent到底拉不拉胯？\n\n📽️ 时间轴： \n00:00 开场\n00:55 ChatGPT Ag"
  },
  {
    "id": "bvid:BV1GD7qzREVA",
    "domain": "AI",
    "title": "【MCP部署实战】手把手教你把MCP接入各大热门工具，保姆级教学，我奶听了都能学会，CherryStudio配置MCP",
    "url": "http://www.bilibili.com/video/av114623818763366",
    "source": "亿点点大模型",
    "platform": "bilibili",
    "points": 8386,
    "published_at": "2025-06-04T07:08:58+00:00",
    "summary": "全程干货无废话！MCP最新实战教程，从环境部署、原理详解到项目实战，带你彻底吃透MCP！MCPServer开发，mcp开发，mcp教程，mcp项目 完整视频教程+讲解课件+学习笔记+AI大模型知识库已打包可分享！"
  },
  {
    "id": "bvid:BV1LWTe6gEVc",
    "domain": "AI",
    "title": "Claude code帮我实现综述论文自由！",
    "url": "http://www.bilibili.com/video/av116842504918580",
    "source": "做科研的大师兄",
    "platform": "bilibili",
    "points": 8159,
    "published_at": "2026-07-01T03:07:40+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 6989,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "bvid:BV1nTKZ6LENd",
    "domain": "AI",
    "title": "【全600集】2026最硬核AI Agent开发零基础到通关！从架构设计到智能体实战，少走99%弯路，学完直接去面试！",
    "url": "http://www.bilibili.com/video/av116838008625963",
    "source": "AI大模型全栈",
    "platform": "bilibili",
    "points": 6611,
    "published_at": "2026-06-30T08:38:47+00:00",
    "summary": "配套课件/代码笔记：后台私信up主→发送暗号【11】即可！允许礼貌白嫖，先到先得！\n【全栈 AI 大模型工程师】 本套 AI 大模型系统教程专为零基础用户打造，全方位覆盖了从 LLM 底层原理到 Prompt 提示词工程、以及 2026 热门 AI Agent 智能体构建的实战全流程，不仅包含 DeepSeek、Claude、OpenClaw 等前沿模型的高效使用技巧，更深度解析了私有化部署、知识"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6487,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV1uz8jzdEZy",
    "domain": "AI",
    "title": "AI Agent 设计助手功能教程丨自然语言交互驱动 AI 智能设计花境、导出苗木清单",
    "url": "http://www.bilibili.com/video/av114929986241780",
    "source": "D5渲染器",
    "platform": "bilibili",
    "points": 6385,
    "published_at": "2025-07-28T10:55:00+00:00",
    "summary": "全新上线的D5 2.11版本正式推出D5 AI 设计助手（AI Agent），能够准确理解设计意图，智能处理复杂任务。与 AI 设计助手对话，通过自然语言交互驱动 AI 完成专业任务。首次上线带来了「花境生成器」「智能苗木清单」「D5 Bot」，未来设计助手还将具备更多能力，令创作者更专注核心创意塑造和方案决策。\n\n获取D5渲染器： https://www.d5render.cn/\n\n2.11宣传"
  },
  {
    "id": "bvid:BV1u4G9zmEte",
    "domain": "AI",
    "title": "什么是MCP？VS Code中使用MCP Server",
    "url": "http://www.bilibili.com/video/av114426032168712",
    "source": "AI落地派",
    "platform": "bilibili",
    "points": 6371,
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based o"
  },
  {
    "id": "bvid:BV1vcKS67Ee8",
    "domain": "AI",
    "title": "【AI Coding】这绝对是你看过讲的最好的Vibe Coding企业级项目实战，从入门到进阶，30分钟速通Claude Code✚Codex✚Cursor",
    "url": "http://www.bilibili.com/video/av116832321209292",
    "source": "图灵学院官方",
    "platform": "bilibili",
    "points": 5335,
    "published_at": "2026-06-29T08:02:48+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1QNKf6vEeC",
    "domain": "AI",
    "title": "【2026版】这可能是B站唯一将AI Agent智能体开发讲明白的教程，从零开始手把手教你打造企业级Agent智能体，少走99%的弯路！存下吧，很难找全的！",
    "url": "http://www.bilibili.com/video/av116837169764407",
    "source": "AI学习课堂",
    "platform": "bilibili",
    "points": 5304,
    "published_at": "2026-06-30T11:48:41+00:00",
    "summary": "【视频配套籽料,学习路线、系统学习，实战项目案例、电子书+问题解答问题解答请看”平论区置顶”自取哦】\n视频制作不易，如果视频对你有用的话请一键三连【长按点赞】支持一下up哦，拜托，这对我真的很重要！"
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
    "id": "rss:https://www.eetimes.com/eu-chips-act-2-award-winning-sequel-or-straight-to-video/",
    "domain": "AI 算力 / 半导体",
    "title": "EU Chips Act 2: Award-Winning Sequel or Straight to Video?",
    "url": "https://www.eetimes.com/eu-chips-act-2-award-winning-sequel-or-straight-to-video/",
    "source": "Bram De Muer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T07:45:07+00:00",
    "summary": "EU Chips Act 2.0 gets the plot right: Fabs aren’t enough. Europe needs design-layer muscle and multi-foundry freedom. The post EU Chips Act 2: Award-Winning Sequel or Straight to Video? appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/heat-telemetry-and-the-rise-of-the-self-aware-spacecraft/",
    "domain": "AI 算力 / 半导体",
    "title": "Heat, Telemetry, and the Rise of the Self-Aware Spacecraft",
    "url": "https://www.eetimes.com/heat-telemetry-and-the-rise-of-the-self-aware-spacecraft/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T19:54:50+00:00",
    "summary": "Satellites are getting brains...and fevers. See how telemetry, heat control, and AI are turning spacecraft into self-protecting machines. The post Heat, Telemetry, and the Rise of the Self-Aware Space"
  },
  {
    "id": "rss:https://www.eetimes.com/model-context-protocol-emerges-as-a-common-framework-for-enterprise-ai-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Model Context Protocol Emerges as a Common Framework for Enterprise AI Systems",
    "url": "https://www.eetimes.com/model-context-protocol-emerges-as-a-common-framework-for-enterprise-ai-systems/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T07:00:00+00:00",
    "summary": "MCP gives enterprise AI a common, open plumbing layer to connect models with tools, data, and agents. The post Model Context Protocol Emerges as a Common Framework for Enterprise AI Systems appeared f"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/xbox-reportedly-testing-a-way-to-digitize-physical-games-in-the-wake-of-playstation-killing-game-discs-feature-said-to-go-back-to-xbox-one-era-games",
    "domain": "AI 算力 / 半导体",
    "title": "Xbox reportedly testing a way to digitize physical games in the wake of PlayStation killing game discs — feature said to go back to Xbox One-era games",
    "url": "https://www.tomshardware.com/video-games/console-gaming/xbox-reportedly-testing-a-way-to-digitize-physical-games-in-the-wake-of-playstation-killing-game-discs-feature-said-to-go-back-to-xbox-one-era-games",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T19:19:25+00:00",
    "summary": "Microsoft is reportedly testing a feature to digitize physical games going back to the Xbox One with digital copies tied to the owner of the physical disc."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tesla-hires-17-year-intel-veteran-responsible-for-billion-dollar-fab-startups-gary-jiang-likely-chosen-to-oversee-fab-efforts-for-terafabs-licensing-of-14a",
    "domain": "AI 算力 / 半导体",
    "title": "Tesla hires 17-year Intel veteran responsible for billion-dollar fab startups — Gary Jiang likely chosen to oversee fab efforts for Terafab's licensing of 14A",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tesla-hires-17-year-intel-veteran-responsible-for-billion-dollar-fab-startups-gary-jiang-likely-chosen-to-oversee-fab-efforts-for-terafabs-licensing-of-14a",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T14:07:26+00:00",
    "summary": "Tesla hires an Intel veteran, who most recently was responsible for installing advanced tools at Intel's Arizona fab that is now ramping production of chips using 18A fabrication process."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-32gb-ddr5-for-less-than-usd260-in-this-b-and-h-ram-bundle-deal-for-an-amd-am5-build-save-usd119-on-this-pc-parts-kit-that-includes-a-ryzen-5-cpu-and-an-asus-b650e-motherboard",
    "domain": "AI 算力 / 半导体",
    "title": "Get 16GB DDR5 for less than $260 in this B&H RAM bundle deal for an AMD AM5 build — save $119 on this PC parts kit that includes a Ryzen 5 CPU and an Asus B650E motherboard",
    "url": "https://www.tomshardware.com/pc-components/get-32gb-ddr5-for-less-than-usd260-in-this-b-and-h-ram-bundle-deal-for-an-amd-am5-build-save-usd119-on-this-pc-parts-kit-that-includes-a-ryzen-5-cpu-and-an-asus-b650e-motherboard",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T14:01:49+00:00",
    "summary": "Save 18% on a solid AMD AM5 starter bundle with a Ryzen 5 7600X, 16GB DDR5-6000 RAM, and an Asus B650E motherboard, a solid and affordable foundation today with an easy path to future Ryzen upgrades t"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/sony-officially-kills-the-playstation-disc-ending-physical-game-production-in-2028-shutting-down-the-playstation-store-on-the-playstation-3-and-ps-vita-systems",
    "domain": "AI 算力 / 半导体",
    "title": "Sony officially kills the PlayStation disc, ending physical game production in 2028 — shutting down the PlayStation Store on the PlayStation 3 and PS Vita systems",
    "url": "https://www.tomshardware.com/video-games/playstation/sony-officially-kills-the-playstation-disc-ending-physical-game-production-in-2028-shutting-down-the-playstation-store-on-the-playstation-3-and-ps-vita-systems",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T13:56:51+00:00",
    "summary": "While Nintendo remains a holdout, this announcement essentially sounds the death knell for physical media in cutting-edge gaming."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/starlink-offers-50-percent-discount-free-hardware-rental-for-residents-surrounding-its-data-centers-move-comes-as-elon-musk-faces-lawsuits-from-residents-complaining-about-noise-and-air-pollution-from-developments",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk offers Starlink discount to AI data center neighbors following air and noise pollution lawsuits — 50% off plans and free hardware rental",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/starlink-offers-50-percent-discount-free-hardware-rental-for-residents-surrounding-its-data-centers-move-comes-as-elon-musk-faces-lawsuits-from-residents-complaining-about-noise-and-air-pollution-from-developments",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T13:50:06+00:00",
    "summary": "SpaceXAI is trying to win residents living close to the Colossus 1 and 2 data centers by giving them discounted internet access. However, critics say that this is just a PR stunt to help win the commu"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-restores-claude-fable-5-as-us-lifts-export-controls",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic restores Claude Fable 5 as US lifts export controls — single filter now blocks prompt that could identify software vulnerabilities and write code to exploit them",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-restores-claude-fable-5-as-us-lifts-export-controls",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T11:30:51+00:00",
    "summary": "Anthropic has restored global access to Claude Fable 5, a day after the U.S. Department of Commerce withdrew the export controls."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/vpn/grab-a-massive-usd464-saving-on-a-two-year-nordvpn-subscription-with-three-extra-months-free-69-percent-saving-unlocks-this-privacy-first-vpn-service-with-scam-protection-password-manager-1tb-cloud-storage-ad-blocking-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a massive $464 saving on a two-year NordVPN subscription with three extra months free — 69% saving unlocks this privacy-first VPN service with scam protection, password manager, 1TB cloud storage",
    "url": "https://www.tomshardware.com/software/vpn/grab-a-massive-usd464-saving-on-a-two-year-nordvpn-subscription-with-three-extra-months-free-69-percent-saving-unlocks-this-privacy-first-vpn-service-with-scam-protection-password-manager-1tb-cloud-storage-ad-blocking-and-more",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T11:12:36+00:00",
    "summary": "A big sale on NordVPN's top Prime package means you can save over $464 on a 2-year sub with three additional months thrown in for free."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/the-bifurcated-laptop-landscape-of-computex-2026-macbook-neo-competitors-with-8gb-of-ram-and-expensive-nvidia-laptops-promising-an-agentic-focused-future-of-windows-on-arm",
    "domain": "AI 算力 / 半导体",
    "title": "The bifurcated laptop landscape of Computex 2026 – MacBook Neo competitors with 8GB of RAM, and expensive Nvidia laptops promising an agentic-focused future of Windows on Arm",
    "url": "https://www.tomshardware.com/laptops/the-bifurcated-laptop-landscape-of-computex-2026-macbook-neo-competitors-with-8gb-of-ram-and-expensive-nvidia-laptops-promising-an-agentic-focused-future-of-windows-on-arm",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T11:00:00+00:00",
    "summary": "With no new GPUs or major mobile CPU platform launches surrounding the show, the laptop announcements at Computex this year fell into two disparate categories, appealing to users with very different b"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/philippine-town-closes-all-pisonet-computer-rental-shops-in-wake-of-school-shooting-incident-blamed-on-violent-video-games-shops-closed-for-the-safety-of-the-youth",
    "domain": "AI 算力 / 半导体",
    "title": "Philippine town closes all 'Pisonet' computer rental shops in wake of school shooting — incident blamed on violent video games, shops closed 'for the safety of the youth'",
    "url": "https://www.tomshardware.com/video-games/philippine-town-closes-all-pisonet-computer-rental-shops-in-wake-of-school-shooting-incident-blamed-on-violent-video-games-shops-closed-for-the-safety-of-the-youth",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T10:48:28+00:00",
    "summary": "A town in northern Philippines closed down all computer rental shops, with the mayor saying that these establishments distracted students from their studies and led to abuse and other dangers. The mov"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/virginia-county-asks-all-employees-including-schools-to-save-power-due-to-ai-driven-electricity-price-hikes-states-400-plus-data-centers-steadily-increasing-demand-grid-expansion-and-pricing",
    "domain": "AI 算力 / 半导体",
    "title": "Virginia county asks all employees, including schools, to conserve power due to AI-driven electricity price hikes — state's 400-plus data centers steadily increasing demand, grid expansion, and pricin",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/virginia-county-asks-all-employees-including-schools-to-save-power-due-to-ai-driven-electricity-price-hikes-states-400-plus-data-centers-steadily-increasing-demand-grid-expansion-and-pricing",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T10:30:00+00:00",
    "summary": "Virginia county asks all employees including schools to save power, due to AI-driven power requirements— state's 400-plus datacenters steadily increasing demand, grid expansion, and pricing"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/new-pc-purchases-see-sharpest-drop-in-nearly-three-years-as-memory-and-storage-prices-bite-shipments-fall-by-7-percent-analysts-forecast-14-percent-contraction-that-will-hit-budget-laptops-hard",
    "domain": "AI 算力 / 半导体",
    "title": "New PC purchases see sharpest drop in nearly three years as memory and storage prices bite — shipments fall by 7%, analysts forecast 14% contraction that will hit budget laptops hard",
    "url": "https://www.tomshardware.com/tech-industry/new-pc-purchases-see-sharpest-drop-in-nearly-three-years-as-memory-and-storage-prices-bite-shipments-fall-by-7-percent-analysts-forecast-14-percent-contraction-that-will-hit-budget-laptops-hard",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T10:02:16+00:00",
    "summary": "A research firm says that PC deliveries for the first quarter of 2026 fell by 7%, with the entire industry expected to ship 14.4% less units for the entire year."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-models-handed-over-a-cocaine-recipe-after-being-told-the-user-was-wearing-a-green-shirt",
    "domain": "AI 算力 / 半导体",
    "title": "AI researchers trick chatbots into sharing how to make cocaine as long as they believe a user is wearing a green shirt — 'CoT Forgery' exploit spurs LLMs to divulge forbidden info by faking trusted ch",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-models-handed-over-a-cocaine-recipe-after-being-told-the-user-was-wearing-a-green-shirt",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T10:00:00+00:00",
    "summary": "Tagged partitions of a LLM's input sequence are meant to provide security through trusted roles, but it turns out that models judge whether inputs sound like they belong in certain tags rather than li"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/32gb-corsair-vengeance-ddr5-is-usd314-in-this-woot-sale-the-lowest-standalone-ram-price-in-months-thanks-to-usd125-discount",
    "domain": "AI 算力 / 半导体",
    "title": "32GB Corsair Vengeance DDR5 is $314 in this Woot sale — the lowest standalone RAM price in months, thanks to $125 discount",
    "url": "https://www.tomshardware.com/pc-components/32gb-corsair-vengeance-ddr5-is-usd314-in-this-woot-sale-the-lowest-standalone-ram-price-in-months-thanks-to-usd125-discount",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T09:34:11+00:00",
    "summary": "Get Corsair Vengeance DDR5 for just $314 at Woot."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/esa-tells-california-lawmakers-that-private-game-servers-are-piracy",
    "domain": "AI 算力 / 半导体",
    "title": "Private and community servers for Minecraft and COD are illegal and amount to piracy, ESA tells California Senate — Stop Killing Games-backed bill fails to pass committee",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/esa-tells-california-lawmakers-that-private-game-servers-are-piracy",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T09:30:00+00:00",
    "summary": "The Entertainment Software Association, in its infinite wisdom, has told a California Senate committee that private and community servers are illegal and amount to piracy."
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/xtool-says-its-01-omni-printer-can-print-it-all-firm-steps-into-the-world-of-uv-printing-for-output-on-all-surfaces-at-up-to-5mm-thick",
    "domain": "AI 算力 / 半导体",
    "title": "xTool says its 01 Omni Printer can ‘print it all’ — firm steps into the world of UV printing for output on 'all surfaces' at up to 5mm thick",
    "url": "https://www.tomshardware.com/maker-stem/xtool-says-its-01-omni-printer-can-print-it-all-firm-steps-into-the-world-of-uv-printing-for-output-on-all-surfaces-at-up-to-5mm-thick",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T19:45:55+00:00",
    "summary": "xTool launched its 01 Omni Printer today at a special event in Berlin. The digital-to-physical tool firm claims this device is the “world’s first 4-in-1 printer,” and said it was ready for makers to “"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-confirms-low-power-cpu-cores-in-linux-kernel-patch-zen-6-chips-could-follow-in-intels-footsteps-with-new-core-type-for-background-tasks",
    "domain": "AI 算力 / 半导体",
    "title": "AMD confirms low-power CPU cores in Linux kernel patch — Zen 6 chips could follow in Intel's footsteps with new core type for background tasks",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-confirms-low-power-cpu-cores-in-linux-kernel-patch-zen-6-chips-could-follow-in-intels-footsteps-with-new-core-type-for-background-tasks",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T16:50:50+00:00",
    "summary": "AMD confirms plans to incorporate low-power CPU cores into next-generation heterogeneous CPUs to lower power consumption and improve energy efficiency."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/microsofts-flagship-windows-pc-lineup-will-drop-reportedly-drop-budget-options-firm-prunes-surface-go-and-surface-laptop-go",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft's flagship Windows PC lineup will drop reportedly drop budget options — firm prunes Surface Go and Surface Laptop Go",
    "url": "https://www.tomshardware.com/laptops/microsofts-flagship-windows-pc-lineup-will-drop-reportedly-drop-budget-options-firm-prunes-surface-go-and-surface-laptop-go",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T16:41:31+00:00",
    "summary": "Microsoft is further pruning its Surface line, with the Surface Laptop Go 3 and Surface Go 4 going out of stock without clear follow-ups."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/windows-defender-bluehammer-vulnerability-now-exploited-as-part-of-malware-campaigns-cisa-issues-warning-despite-patch-release-on-april-14",
    "domain": "AI 算力 / 半导体",
    "title": "Windows Defender 'BlueHammer' vulnerability now exploited as part of malware campaigns — CISA issues warning despite patch release on April 14",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/windows-defender-bluehammer-vulnerability-now-exploited-as-part-of-malware-campaigns-cisa-issues-warning-despite-patch-release-on-april-14",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T16:20:59+00:00",
    "summary": "Windows Defender \"BlueHammer\" vulnerability now exploited as part of malware campaigns — event demonstrates lack of security awareness despite existence of patches"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/meta-releases-version-two-of-its-brain-computer-interface-that-can-turn-thoughts-into-keypresses-non-invasive-magnetoencephalography-scanner-can-measure-changes-in-brain-activity",
    "domain": "AI 算力 / 半导体",
    "title": "Meta releases version two of its brain-computer interface that can turn thoughts into keypresses — non-invasive magnetoencephalography scanner can measure changes in brain activity",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/meta-releases-version-two-of-its-brain-computer-interface-that-can-turn-thoughts-into-keypresses-non-invasive-magnetoencephalography-scanner-can-measure-changes-in-brain-activity",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T13:34:35+00:00",
    "summary": "Meta just released the second version of its Brain2Qwerty non-invasive BCI, showing promising improvements that could lead to clinical trials. This system aims to build an interface that does not requ"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-reportedly-cancels-quad-die-rubin-ultra-gpu-in-favor-of-dual-gpu-design-report-claims-complex-design-purportedly-scrapped-over-manufacturing-execution-concerns",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia reportedly cancels quad-die Rubin Ultra GPU in favor of dual-GPU design, report claims — complex design purportedly scrapped over 'manufacturing execution concerns'",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-reportedly-cancels-quad-die-rubin-ultra-gpu-in-favor-of-dual-gpu-design-report-claims-complex-design-purportedly-scrapped-over-manufacturing-execution-concerns",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T12:45:00+00:00",
    "summary": "Nvidia reportedly abandons quad-dire Rubin Ultra GPUs in favor of dual-die Rubin Ultra due to 'manufacturing execution concerns.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/z-ai-free-glm-5-2-tops-the-open-weight-ai-rankings-on-all-huawei-silicon",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese Z.ai's latest model tops AI ranking charts amid Anthropic Fable 5 ban — blacklisted China firm's popular open-weight GLM-5.2 AI model powered by Huawei silicon",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/z-ai-free-glm-5-2-tops-the-open-weight-ai-rankings-on-all-huawei-silicon",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T11:58:10+00:00",
    "summary": "Within a week of Fable's ban, GLM-5.2 had climbed to the top of the openly available leaderboards."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/grab-this-epic-razer-wolverine-v3-controller-for-a-record-low-amazon-price-now-just-usd64-99-big-46-percent-saving-on-this-esports-friendly-gamepad-for-your-pc-or-console-with-next-gen-tmr-thumbsticks-and-an-ultra-fast-8-000hz-polling-rate",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this epic Razer Wolverine V3 controller for a record-low Amazon price, now just $64.99 — big 46% saving on this esports-friendly gamepad for your PC or console with next-gen TMR thumbsticks and a",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/grab-this-epic-razer-wolverine-v3-controller-for-a-record-low-amazon-price-now-just-usd64-99-big-46-percent-saving-on-this-esports-friendly-gamepad-for-your-pc-or-console-with-next-gen-tmr-thumbsticks-and-an-ultra-fast-8-000hz-polling-rate",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T11:34:05+00:00",
    "summary": "This esports pro-friendly Razer Wolverine V3 Tournament Edition controller is on sale for a record low Amazon Price, now just $64.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/taiwan-raids-super-micro-and-two-supply-chain-partners-in-widening-nvidia-smuggling-probe",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan raids Supermicro and two supply-chain partners in widening Nvidia smuggling probe — nine sites hit as six people summoned for questioning",
    "url": "https://www.tomshardware.com/tech-industry/taiwan-raids-super-micro-and-two-supply-chain-partners-in-widening-nvidia-smuggling-probe",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T11:18:43+00:00",
    "summary": "Taiwan officials raided Supermicro Computer's Taiwan office on Monday, alongside the homes of six individuals and three affiliated company sites"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/cargo-thieves-target-ai-data-center-supplies-in-usd1-3-million-heists-usd300-000-worth-of-copper-wire-and-usd1-million-worth-of-equipment-recovered-outside-chicago",
    "domain": "AI 算力 / 半导体",
    "title": "Cargo thieves target AI data center supplies in $1.3 million heists — $300,000 worth of copper wire and $1 million worth of equipment recovered outside Chicago",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/cargo-thieves-target-ai-data-center-supplies-in-usd1-3-million-heists-usd300-000-worth-of-copper-wire-and-usd1-million-worth-of-equipment-recovered-outside-chicago",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T11:06:17+00:00",
    "summary": "Authorities recover $1.3 million worth of data center supplies and equipment in a truck stop near Chicago. Equipment like this is a prime target for theft rings given its high value, but it's also lik"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/meta-fights-soaring-hardware-costs-by-reusing-old-ddr4-server-memory-in-new-ddr5-only-servers-custom-cxl-2-0-chip-marries-legacy-ddr4-2400-with-cutting-edge-ddr5-6400",
    "domain": "AI 算力 / 半导体",
    "title": "Meta fights soaring hardware costs by reusing old DDR4 server memory in new DDR5-only servers — custom CXL 2.0 chip marries legacy DDR4-2400 with cutting-edge DDR5-6400",
    "url": "https://www.tomshardware.com/pc-components/dram/meta-fights-soaring-hardware-costs-by-reusing-old-ddr4-server-memory-in-new-ddr5-only-servers-custom-cxl-2-0-chip-marries-legacy-ddr4-2400-with-cutting-edge-ddr5-6400",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T11:00:00+00:00",
    "summary": "Meta develops its custom Vistara CXL memory expander to use DDR4 memory with new servers running AMD EPYC 'Turin' processors."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/samsungs-9100-pro-ssd-1tb-is-still-available-at-its-prime-day-price-thanks-to-39-percent-discount-cheaper-and-faster-than-the-990-pro-and-the-lowest-price-weve-seen-in-months",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung's 9100 Pro SSD 1TB is still available at its excellent Prime Day price thanks to 39% discount — cheaper and faster than the 990 Pro and the lowest price we've seen in months",
    "url": "https://www.tomshardware.com/pc-components/ssds/samsungs-9100-pro-ssd-1tb-is-still-available-at-its-prime-day-price-thanks-to-39-percent-discount-cheaper-and-faster-than-the-990-pro-and-the-lowest-price-weve-seen-in-months",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T10:30:02+00:00",
    "summary": "The Samsung 9100 Pro SSD is still sporting its Prime Day price. Grab one at this low price while you can."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/hamsteros-jams-a-32-bit-gui-operating-system-in-a-1-44-mb-single-floppy-for-386-era-hardware-retro-os-should-make-for-easy-living-with-dos-machines-and-software",
    "domain": "AI 算力 / 半导体",
    "title": "HamsterOS jams a 32-bit GUI operating system in a single 1.44 MB floppy disk — retro OS for 386-era hardware should make for easy living with DOS machines and software",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/hamsteros-jams-a-32-bit-gui-operating-system-in-a-1-44-mb-single-floppy-for-386-era-hardware-retro-os-should-make-for-easy-living-with-dos-machines-and-software",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T10:30:00+00:00",
    "summary": "HamsterOS fits on just a single 1.44 MB floppy disk, and it's set for a full release this November."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/maker-kicks-off-oomwoo-an-open-source-robot-vacuum-you-can-3d-print-and-build-yourself",
    "domain": "AI 算力 / 半导体",
    "title": "Oomwoo is a new open-source robot vacuum you can 3D print yourself, sidesteps cloud security risks by running fully offline — project combines Raspberry Pi, 2D LiDAR, and a 3D-printed chassis",
    "url": "https://www.tomshardware.com/3d-printing/maker-kicks-off-oomwoo-an-open-source-robot-vacuum-you-can-3d-print-and-build-yourself",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T10:00:00+00:00",
    "summary": "Maker's Pet has launched oomwoo, an open-source robot vacuum that owners build themselves."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/designer-turns-niche-e-ink-dev-board-into-a-60hz-game-boy-handheld-960x540-display-powered-by-ultra-low-cost-esp32-s3-microcontroller",
    "domain": "AI 算力 / 半导体",
    "title": "Designer turns discontinued E-Ink dev board into a 60Hz Game Boy handheld — dual-core chip runs at 100% to power handheld, 960x540 display employs ultra-low-cost ESP32-S3 microcontroller",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/designer-turns-niche-e-ink-dev-board-into-a-60hz-game-boy-handheld-960x540-display-powered-by-ultra-low-cost-esp32-s3-microcontroller",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T09:30:00+00:00",
    "summary": "The hardware is discontinued and the experience isn't perfect, but the fact that the emulator exists at all is a true technical achievement."
  },
  {
    "id": "rss:https://www.eetimes.com/u-s-eyes-china-expanding-role-in-latin-america/",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. Eyes China’s Expanding Role in Latin America",
    "url": "https://www.eetimes.com/u-s-eyes-china-expanding-role-in-latin-america/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T21:00:00+00:00",
    "summary": "As U.S. regulators focus on supply chain transparency, China's expanding presence in Latin America has emerged as a major strategic challenge. The post U.S. Eyes China&#8217;s Expanding Role in Latin "
  },
  {
    "id": "rss:https://www.eetimes.com/panel-with-arteris-gf-tenstorrent-risc-v-ecosystem-growth-for-physical-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Panel with Arteris, GlobalFoundries, Tenstorrent: RISC-V Ecosystem Growth for Physical AI",
    "url": "https://www.eetimes.com/panel-with-arteris-gf-tenstorrent-risc-v-ecosystem-growth-for-physical-ai/",
    "source": "EE Times Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T16:53:48+00:00",
    "summary": "RISC-V heavyweights tackle physical AI, edge autonomy, and TOPS-per-watt—watch how robots chase their killer app. The post Panel with Arteris, GlobalFoundries, Tenstorrent: RISC-V Ecosystem Growth for"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/amd-expo-ull-ram-drops-at-jaw-dropping-usd1-099-despite-promises-of-it-being-effectively-the-same-price-ddr5-6000-c26-32gb-kit-sports-80-percent-ull-tax",
    "domain": "AI 算力 / 半导体",
    "title": "AMD EXPO ULL RAM drops at jaw-dropping $1,099 despite promises of it being 'effectively the same price' — DDR5-6000 C26 32GB kit sports 80% ULL tax",
    "url": "https://www.tomshardware.com/pc-components/ram/amd-expo-ull-ram-drops-at-jaw-dropping-usd1-099-despite-promises-of-it-being-effectively-the-same-price-ddr5-6000-c26-32gb-kit-sports-80-percent-ull-tax",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-29T20:16:12+00:00",
    "summary": "Newegg has started selling G.Skill’s Trident Z5 NeoX memory kits featuring AMD ULL technology, and the prices are already high."
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
    "id": "rss:https://www.theverge.com/news/960541/apple-macbook-pro-entry-level-redesign-ipad-pro-update",
    "domain": "大厂 AI 动态",
    "title": "Apple’s entry-level MacBook Pro could be up for a redesign",
    "url": "https://www.theverge.com/news/960541/apple-macbook-pro-entry-level-redesign-ipad-pro-update",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T22:39:43+00:00",
    "summary": "Apple is working on a \"revamped\" version of its entry-level MacBook Pro that it could launch as soon as the first half of 2027, Bloomberg reports. The company is also testing four new iPad Pros that a"
  },
  {
    "id": "rss:https://www.theverge.com/games/960476/playstation-physical-games-discs-stop-production-preservation-retail-stores",
    "domain": "大厂 AI 动态",
    "title": "The funeral for PlayStation discs has begun",
    "url": "https://www.theverge.com/games/960476/playstation-physical-games-discs-stop-production-preservation-retail-stores",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T22:03:37+00:00",
    "summary": "Cody Spencer, the co-owner of the small games retail chain Pink Gorilla Games, put it well when I asked about the impact of Sony's recent announcement that it will stop making discs for new games star"
  },
  {
    "id": "rss:https://www.theverge.com/games/959900/xbox-reset-layoffs-studio-closures",
    "domain": "大厂 AI 动态",
    "title": "Xbox’s ‘reset’: all the news about Microsoft&#8217;s looming layoffs and studio closures",
    "url": "https://www.theverge.com/games/959900/xbox-reset-layoffs-studio-closures",
    "source": "Verge Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T21:00:00+00:00",
    "summary": "Xbox is making some big changes — again. On June 10th, a few months after Asha Sharma took over as CEO, she and newly-promoted chief content officer Matt Booty sent a memo to staff warning of an &#822"
  },
  {
    "id": "rss:https://www.theverge.com/science/960442/spacex-phone-prototype-elon-musk",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk denies a report about SpaceX&#8217;s AI phone prototype",
    "url": "https://www.theverge.com/science/960442/spacex-phone-prototype-elon-musk",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T20:10:21+00:00",
    "summary": "Elon Musk says a report about a SpaceX AI phone prototype is \"utterly false.\" The report, published on Wednesday by The Wall Street Journal, says SpaceX showed off a \"handset-like prototype\" to some i"
  },
  {
    "id": "rss:https://www.theverge.com/games/960354/krafton-subnautica-2-settlement-bonuses-unknown-worlds",
    "domain": "大厂 AI 动态",
    "title": "Krafton settles with Subnautica 2 developer after drawn-out dispute over $250 million",
    "url": "https://www.theverge.com/games/960354/krafton-subnautica-2-settlement-bonuses-unknown-worlds",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T17:45:23+00:00",
    "summary": "After a lengthy legal dispute, Krafton has settled with its subsidiary Unknown Worlds Entertainment, which is developing Subnautica 2, and will pay bonuses to the studio's staff, Bloomberg reports. Th"
  },
  {
    "id": "rss:https://www.theverge.com/report/960173/microsoft-xbox-disc-to-digital-feature-physical-game-collection",
    "domain": "大厂 AI 动态",
    "title": "Xbox testing disc-to-digital feature that digitizes a physical game collection",
    "url": "https://www.theverge.com/report/960173/microsoft-xbox-disc-to-digital-feature-physical-game-collection",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T17:41:23+00:00",
    "summary": "Microsoft will likely soon follow Sony and stop the production of physical discs for Xbox games. But instead of leaving physical discs behind entirely, sources familiar with Microsoft's plans tell me "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/960282/kobo-libra-colour-july-fourth-sale-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "My favorite Kindle alternative is $30 off after a recent price increase",
    "url": "https://www.theverge.com/gadgets/960282/kobo-libra-colour-july-fourth-sale-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T16:28:40+00:00",
    "summary": "Kobo recently raised the price of its Libra Colour e-reader to $259.99, but today&#8217;s deal effectively erases that hike. The company, Best Buy, and Target, are all selling it for its old $229.99 p"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/960235/comcast-breakup-peacock-streaming",
    "domain": "大厂 AI 动态",
    "title": "Comcast’s split could make or break Peacock",
    "url": "https://www.theverge.com/streaming/960235/comcast-breakup-peacock-streaming",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T15:30:00+00:00",
    "summary": "NBCUniversal executives are about to find out whether Peacock will sink or swim in the streaming industry. Now that Comcast is planning to split NBCUniversal, Peacock, and Sky from its broadband and w"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/960185/dbrand-killswitch-switch-2-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The best Switch 2 case I’ve tried is cheaper than usual",
    "url": "https://www.theverge.com/gadgets/960185/dbrand-killswitch-switch-2-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T15:00:00+00:00",
    "summary": "Dbrand apparently knows how to really whiff a product launch, as we recently saw with the Steam Machine Companion Cube shell. But it also makes the best case out there for the Nintendo Switch 2, which"
  },
  {
    "id": "rss:https://www.theverge.com/games/960212/sony-playstation-killing-discs-digital-preservation",
    "domain": "大厂 AI 动态",
    "title": "Sony is killing discs — and showing us why it’s a terrible idea",
    "url": "https://www.theverge.com/games/960212/sony-playstation-killing-discs-digital-preservation",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T15:00:00+00:00",
    "summary": "The future of video game preservation just took a major hit. This morning, Sony announced that, starting in January 2028, the company will no longer produce physical PlayStation discs, which means tha"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/01/indian-tech-tycoon-bets-30m-to-build-an-ai-alternative-to-microsoft-office/",
    "domain": "大厂 AI 动态",
    "title": "Indian tech tycoon bets $30M of his own money to build AI alternative to Microsoft Office",
    "url": "https://techcrunch.com/2026/07/01/indian-tech-tycoon-bets-30m-to-build-an-ai-alternative-to-microsoft-office/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T05:30:00+00:00",
    "summary": "Neo is Bhavin Turakhia’s fifth venture and his latest involving enterprise software. This time he's taking on Microsoft Office, Google Apps with AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/01/apple-is-reportedly-planning-new-ipad-pro-and-macbook-pro-releases-early-next-year/",
    "domain": "大厂 AI 动态",
    "title": "Apple is reportedly planning new iPad Pro and MacBook Pro releases early next year",
    "url": "https://techcrunch.com/2026/07/01/apple-is-reportedly-planning-new-ipad-pro-and-macbook-pro-releases-early-next-year/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T23:57:55+00:00",
    "summary": "Apple is readying several new iPad Pro tablets and a budget-friendly MacBook Pro, reports suggest."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/01/bending-spoons-defies-saas-slump-surges-40-on-first-day-of-trading/",
    "domain": "大厂 AI 动态",
    "title": "Bending Spoons defies SaaS slump, surges 40% on first day of trading",
    "url": "https://techcrunch.com/2026/07/01/bending-spoons-defies-saas-slump-surges-40-on-first-day-of-trading/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T22:47:04+00:00",
    "summary": "The company has grown rapidly by acquiring and revamping last-generation tech brands like AOL, Eventbrite, Evernote, Meetup, and Vimeo."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/01/after-18b-ipo-bending-spoons-founder-says-success-comes-from-minimizing-luck/",
    "domain": "大厂 AI 动态",
    "title": "After $18B IPO, Bending Spoons founder says success comes from minimizing luck",
    "url": "https://techcrunch.com/2026/07/01/after-18b-ipo-bending-spoons-founder-says-success-comes-from-minimizing-luck/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T22:28:35+00:00",
    "summary": "The co-founders of Bending Spoons, the Italian company quietly buying beloved, ailing Internet brands, learned big lessons from their own startup's failure."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/01/whatsapp-usernames-are-already-raising-impersonation-red-flags/",
    "domain": "大厂 AI 动态",
    "title": "WhatsApp usernames are already raising impersonation red flags",
    "url": "https://techcrunch.com/2026/07/01/whatsapp-usernames-are-already-raising-impersonation-red-flags/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T22:02:24+00:00",
    "summary": "Meta says usernames improve privacy, but critics question whether its safeguards can prevent impersonation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/01/apples-hide-my-email-feature-has-a-bug-thats-been-exposing-real-email-addresses-researcher-claims/",
    "domain": "大厂 AI 动态",
    "title": "Apple’s Hide My Email feature has a bug that’s been exposing real email addresses, researcher claims",
    "url": "https://techcrunch.com/2026/07/01/apples-hide-my-email-feature-has-a-bug-thats-been-exposing-real-email-addresses-researcher-claims/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T19:18:07+00:00",
    "summary": "Research appears to reveal a bug that could render the feature effectively useless."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/01/spacex-has-an-ai-device-prototype-and-it-sure-sounds-phone-ish/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX has an AI device prototype, and it sure sounds phone-ish",
    "url": "https://techcrunch.com/2026/07/01/spacex-has-an-ai-device-prototype-and-it-sure-sounds-phone-ish/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T18:54:18+00:00",
    "summary": "SpaceX reportedly showed investors a \"handset-like\" AI device before going public. It could be another signal SpaceX wants to expand into wireless."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/01/ashton-kutcher-leaving-sound-ventures-to-launch-new-vc-firm-with-morgan-beller/",
    "domain": "大厂 AI 动态",
    "title": "Ashton Kutcher leaving Sound Ventures to launch new VC firm with Morgan Beller",
    "url": "https://techcrunch.com/2026/07/01/ashton-kutcher-leaving-sound-ventures-to-launch-new-vc-firm-with-morgan-beller/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T18:47:22+00:00",
    "summary": "Sound built its reputation on concentrated, high-conviction bets in category-leading AI labs, while Kutcher's new fund appears to be chasing the layer underneath those companies — the infrastructure a"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/01/neocloud-together-ai-raises-800m-leaps-to-8-3b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Neocloud Together AI raises $800M, leaps to $8.3B valuation",
    "url": "https://techcrunch.com/2026/07/01/neocloud-together-ai-raises-800m-leaps-to-8-3b-valuation/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T18:29:14+00:00",
    "summary": "The AI neocloud provider, which specializes in hosting open source models, last raised at a $3.3 billion valuation in early 2025."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/01/lime-begins-life-as-a-public-company-after-years-of-uncertainty/",
    "domain": "大厂 AI 动态",
    "title": "Lime begins life as a public company after years of uncertainty",
    "url": "https://techcrunch.com/2026/07/01/lime-begins-life-as-a-public-company-after-years-of-uncertainty/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T18:24:00+00:00",
    "summary": "The nine-year-old scooter and bike-share company has said it needs the funds to help pay down around $1 billion in liabilities."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/01/cloudflares-new-policy-pushes-ai-companies-to-pay-for-publishers-content/",
    "domain": "大厂 AI 动态",
    "title": "Cloudflare’s new policy pushes AI companies to pay for publishers’ content",
    "url": "https://techcrunch.com/2026/07/01/cloudflares-new-policy-pushes-ai-companies-to-pay-for-publishers-content/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T17:48:37+00:00",
    "summary": "Cloudflare is giving AI companies until September 15 to separate web crawlers used for search from those used for AI training and agents, or risk being blocked by default on many publisher sites."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/01/even-honda-is-pivoting-to-data-centers/",
    "domain": "大厂 AI 动态",
    "title": "Even Honda is pivoting to data centers",
    "url": "https://techcrunch.com/2026/07/01/even-honda-is-pivoting-to-data-centers/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T17:13:45+00:00",
    "summary": "Honda wants in on the lucrative energy storage market. This week it began producing batteries destined for data centers, not driveways."
  },
  {
    "id": "rss:https://techcrunch.com/video/autonomous-vehicle-hype-is-back-and-humble-robotics-is-bringing-it-to-freights/",
    "domain": "大厂 AI 动态",
    "title": "Autonomous vehicle hype is back, and Humble Robotics is bringing it to freight",
    "url": "https://techcrunch.com/video/autonomous-vehicle-hype-is-back-and-humble-robotics-is-bringing-it-to-freights/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T16:48:58+00:00",
    "summary": "The autonomous vehicle space is starting to feel like a repeat of the 2016 hype cycle. Travis Kalanick is back building a robotics company, and the talent wars and capital are heating up the same way "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/01/venice-ai-becomes-a-unicorn-with-65m-series-a-as-its-privacy-first-ai-platform-takes-off/",
    "domain": "大厂 AI 动态",
    "title": "Venice AI becomes a unicorn with $65M Series A as its privacy-first AI platform takes off",
    "url": "https://techcrunch.com/2026/07/01/venice-ai-becomes-a-unicorn-with-65m-series-a-as-its-privacy-first-ai-platform-takes-off/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T14:25:23+00:00",
    "summary": "Venice AI is already profitable, with annualized run-rate revenues of over $70 million, CEO Erik Voorhees said."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/01/gemini-spark-googles-agentic-assistant-is-now-available-on-mac/",
    "domain": "大厂 AI 动态",
    "title": "Gemini Spark, Google’s agentic assistant, is now available on Mac",
    "url": "https://techcrunch.com/2026/07/01/gemini-spark-googles-agentic-assistant-is-now-available-on-mac/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T14:20:19+00:00",
    "summary": "Google's 24/7 agentic assistant, Gemini Spark, comes to Mac alongside other improvements, like real-time tracking and support for more apps."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/01/sony-to-end-physical-playstation-game-discs-in-2028/",
    "domain": "大厂 AI 动态",
    "title": "Sony to end physical PlayStation game disc production in 2028",
    "url": "https://techcrunch.com/2026/07/01/sony-to-end-physical-playstation-game-discs-in-2028/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T14:16:32+00:00",
    "summary": "Sony will stop producing physical discs for all new PlayStation games beginning in 2028, as the company embraces an all-digital future."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/01/builders-stage-agenda-revealed-practical-strategies-for-scaling-startups-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Builders Stage agenda revealed: Practical strategies for scaling startups at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/07/01/builders-stage-agenda-revealed-practical-strategies-for-scaling-startups-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T14:00:00+00:00",
    "summary": "The Builders Stage is returning to TechCrunch Disrupt 2026, bringing together 10,000+ founders, startup operators, and investors for practical conversations. and Q&#038;A on what it takes to build and"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/01/meta-like-spacex-looks-to-turn-excess-ai-compute-into-cash/",
    "domain": "大厂 AI 动态",
    "title": "Meta, like SpaceX, looks to turn excess AI compute into cash",
    "url": "https://techcrunch.com/2026/07/01/meta-like-spacex-looks-to-turn-excess-ai-compute-into-cash/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T13:43:07+00:00",
    "summary": "Meta is developing plans for a cloud infrastructure business, selling access to AI compute power and models. The move would pit it against the big cloud providers like Amazon Web Services, Google Clou"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/the-father-of-the-internet-is-finally-retiring/",
    "domain": "大厂 AI 动态",
    "title": "The ‘Father of the Internet’ is finally retiring",
    "url": "https://techcrunch.com/2026/06/30/the-father-of-the-internet-is-finally-retiring/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T03:15:37+00:00",
    "summary": "Vinton Cerf, one of the creators of the protocols underlying the internet, will step down as Google's chief internet evangelist next week."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/30/trump-drops-restrictions-on-anthropics-mythos-and-fable-models/",
    "domain": "大厂 AI 动态",
    "title": "Trump drops restrictions on Anthropic’s Mythos and Fable models",
    "url": "https://techcrunch.com/2026/06/30/trump-drops-restrictions-on-anthropics-mythos-and-fable-models/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T02:16:06+00:00",
    "summary": "The Trump administration's erratic approach to AI policymaking has left companies across the industry with little clarity about what will govern future model releases."
  },
  {
    "id": "rss:https://arstechnica.com/information-technology/2026/07/t-mobile-moving-tens-of-thousands-of-virtual-machines-off-vmware-amid-lawsuit/",
    "domain": "大厂 AI 动态",
    "title": "T-Mobile moving tens of thousands of virtual machines off VMware amid lawsuit",
    "url": "https://arstechnica.com/information-technology/2026/07/t-mobile-moving-tens-of-thousands-of-virtual-machines-off-vmware-amid-lawsuit/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T21:21:21+00:00",
    "summary": "T-Mobile wants Broadcom to keep supporting its VMware perpetual licenses."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/nasa-chief-praises-progress-blue-origin-is-making-after-launch-failure/",
    "domain": "大厂 AI 动态",
    "title": "NASA chief praises progress Blue Origin is making after launch failure",
    "url": "https://arstechnica.com/space/2026/07/nasa-chief-praises-progress-blue-origin-is-making-after-launch-failure/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T19:57:36+00:00",
    "summary": "\"We've got time into 2027 before we're getting nervous.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/us-home-battery-installations-hit-record-high-in-early-2026/",
    "domain": "大厂 AI 动态",
    "title": "US home battery installations hit record high on rising electricity costs",
    "url": "https://arstechnica.com/science/2026/07/us-home-battery-installations-hit-record-high-in-early-2026/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T19:11:15+00:00",
    "summary": "Record home battery installations unlock options for grids—and AI data centers."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/museums-could-use-ravenous-superworms-to-clean-skeletons/",
    "domain": "大厂 AI 动态",
    "title": "Superworms could replace beetles for cleaning skeletal remains",
    "url": "https://arstechnica.com/science/2026/07/museums-could-use-ravenous-superworms-to-clean-skeletons/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T18:59:21+00:00",
    "summary": "An optimal ratio of 10-15 grams of larvae per gram of specimen minimized cleaning time with no bone damage."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/07/sony-will-stop-making-physical-copies-of-playstation-games-in-2028/",
    "domain": "大厂 AI 动态",
    "title": "Sony announces end of PlayStation discs, parts of digital store in the same day",
    "url": "https://arstechnica.com/gaming/2026/07/sony-will-stop-making-physical-copies-of-playstation-games-in-2028/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T18:41:49+00:00",
    "summary": "“We will own nothing, it's truly sad.”"
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/07/the-volvo-ex30-cross-country-review-a-victim-of-geopolitics/",
    "domain": "大厂 AI 动态",
    "title": "A good little EV you won't be able to buy soon: The Volvo EX30 Cross Country",
    "url": "https://arstechnica.com/cars/2026/07/the-volvo-ex30-cross-country-review-a-victim-of-geopolitics/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T18:24:04+00:00",
    "summary": "Tariffs and anti-China policies killed this little Volvo in the United States."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/07/ithacas-king-defies-the-gods-in-final-the-odyssey-trailer/",
    "domain": "大厂 AI 动态",
    "title": "Ithaca's king defies the gods in final The Odyssey trailer",
    "url": "https://arstechnica.com/culture/2026/07/ithacas-king-defies-the-gods-in-final-the-odyssey-trailer/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T16:58:30+00:00",
    "summary": "\"You gods don't speak in ways we understand.\""
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/after-spooking-trump-into-safety-testing-anthropic-ai-models-get-global-release/",
    "domain": "大厂 AI 动态",
    "title": "After spooking Trump into safety testing, Anthropic AI models get global release",
    "url": "https://arstechnica.com/tech-policy/2026/07/after-spooking-trump-into-safety-testing-anthropic-ai-models-get-global-release/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T16:44:18+00:00",
    "summary": "US lifts curbs on Anthropic’s advanced Fable and Mythos models."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/nasa-inspector-general-suggests-boeings-starliner-will-now-be-a-decade-late/",
    "domain": "大厂 AI 动态",
    "title": "NASA inspector general suggests Boeing's Starliner will now be a decade late",
    "url": "https://arstechnica.com/space/2026/07/nasa-inspector-general-suggests-boeings-starliner-will-now-be-a-decade-late/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T16:11:39+00:00",
    "summary": "Starliner's certification may be delayed to 2027, 10 years later than Boeing's original schedule."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/50-years-on-will-the-mars-lander-arm-that-opened-the-air-and-space-raise-its-hand/",
    "domain": "大厂 AI 动态",
    "title": "A space history mystery: What happened to the Viking arm used 50 years ago?",
    "url": "https://arstechnica.com/space/2026/07/50-years-on-will-the-mars-lander-arm-that-opened-the-air-and-space-raise-its-hand/",
    "source": "Robert Pearlman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T15:20:34+00:00",
    "summary": "A timely tale about a 50-year-old robotic arm..."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/uk-likely-to-intervene-in-paramount-takeover-of-warner-bros-discovery/",
    "domain": "大厂 AI 动态",
    "title": "UK likely to intervene in Paramount takeover of Warner Bros. Discovery",
    "url": "https://arstechnica.com/tech-policy/2026/07/uk-likely-to-intervene-in-paramount-takeover-of-warner-bros-discovery/",
    "source": "Daniel Thomas, Financial Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T13:24:39+00:00",
    "summary": "The acquisition was approved without concessions by the Department of Justice in June."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/trump-and-rfk-jr-still-wrong-about-tylenol-and-autism-another-study-finds/",
    "domain": "大厂 AI 动态",
    "title": "Scientists find no link between Tylenol and autism, again, after Trump warning",
    "url": "https://arstechnica.com/health/2026/07/trump-and-rfk-jr-still-wrong-about-tylenol-and-autism-another-study-finds/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-01T11:01:38+00:00",
    "summary": "After Trump's claims, Tylenol usage dropped during pregnancies."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/june-research-roundup-6-cool-science-stories-we-almost-missed/",
    "domain": "大厂 AI 动态",
    "title": "June research roundup: 6 cool science stories we almost missed",
    "url": "https://arstechnica.com/science/2026/06/june-research-roundup-6-cool-science-stories-we-almost-missed/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T22:11:10+00:00",
    "summary": "Also, the science of poop's distinctive shape, boron buckyballs, and the secret to a soccer feint."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/reddit-will-require-you-to-log-in-to-use-old-reddit-com/",
    "domain": "大厂 AI 动态",
    "title": "Reddit will require you to log in to use old.reddit.com",
    "url": "https://arstechnica.com/gadgets/2026/06/reddit-will-require-you-to-log-in-to-use-old-reddit-com/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T21:46:35+00:00",
    "summary": "Logged-out Old Reddit access is “significant source of abusive scraping.\""
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/exec-blames-malware-threat-for-amazon-blocking-sideloading-on-new-fire-sticks/",
    "domain": "大厂 AI 动态",
    "title": "Amazon blames piracy apps with malware for killing new Fire Stick sideloading",
    "url": "https://arstechnica.com/gadgets/2026/06/exec-blames-malware-threat-for-amazon-blocking-sideloading-on-new-fire-sticks/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T21:04:53+00:00",
    "summary": "New Fire Stick OS helps Amazon block third-party homepage launchers, ad blockers."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/nasa-may-send-a-backup-nuclear-powered-mars-rover-to-the-moon/",
    "domain": "大厂 AI 动态",
    "title": "NASA may send a backup, nuclear-powered Mars rover to the Moon",
    "url": "https://arstechnica.com/space/2026/06/nasa-may-send-a-backup-nuclear-powered-mars-rover-to-the-moon/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T20:50:14+00:00",
    "summary": "\"That would be an awesome capability.\""
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/google-kills-tenor-gif-api-forcing-changes-at-x-discord-and-more/",
    "domain": "大厂 AI 动态",
    "title": "Google kills Tenor GIF API, forcing changes at X, Discord, and more",
    "url": "https://arstechnica.com/gadgets/2026/06/google-kills-tenor-gif-api-forcing-changes-at-x-discord-and-more/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T20:38:51+00:00",
    "summary": "Tenor still connects to Google apps, but other platforms must look elsewhere for GIFs."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/apple-takes-epic-fight-over-app-store-fees-to-the-supreme-court/",
    "domain": "大厂 AI 动态",
    "title": "Apple takes Epic fight over app store fees to the Supreme Court",
    "url": "https://arstechnica.com/tech-policy/2026/06/apple-takes-epic-fight-over-app-store-fees-to-the-supreme-court/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T20:20:29+00:00",
    "summary": "Supreme Court will weigh if Apple contempt finding in Epic case is “erroneous.”"
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/06/ai-browsers-can-be-lulled-into-a-dream-world-where-guardrails-no-longer-apply/",
    "domain": "大厂 AI 动态",
    "title": "New attack provides one more reason why AI browsers are a bad idea",
    "url": "https://arstechnica.com/security/2026/06/ai-browsers-can-be-lulled-into-a-dream-world-where-guardrails-no-longer-apply/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T20:03:14+00:00",
    "summary": "Telling an LLM that 2 + 2 = 5 is enough to make it follow forbidden instructions."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/googles-new-nano-banana-2-lite-image-model-is-its-fastest-and-cheapest-yet/",
    "domain": "大厂 AI 动态",
    "title": "Google's new Nano Banana 2 Lite image model is its fastest and cheapest yet",
    "url": "https://arstechnica.com/ai/2026/06/googles-new-nano-banana-2-lite-image-model-is-its-fastest-and-cheapest-yet/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-30T18:36:10+00:00",
    "summary": "They may not look as good, but Nano Banana 2 Lite images only take a few seconds to create."
  },
  {
    "id": "wscn:3776054",
    "domain": "股票",
    "title": "马斯克晒Optimus量产团队合照，承认生产初期“极其缓慢”：这不像造车",
    "url": "https://wallstreetcn.com/articles/3776054",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T06:45:56+00:00",
    "summary": "马斯克亲赴弗里蒙特工厂与Optimus量产团队合影引爆市场遐想，然而他同时给Optimus“超前量产”的预期降温——“这不像造车，初期将极其缓慢。”万个零部件的协同难题、S曲线爬坡的现实约束，特斯拉Optimus量产存在多重变量。"
  },
  {
    "id": "wscn:3776047",
    "domain": "股票",
    "title": "英伟达要开始分云厂商的钱了",
    "url": "https://wallstreetcn.com/articles/3776047",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T06:27:00+00:00",
    "summary": "据报道，为打破科技巨头垄断，英伟达为新兴云厂商提供GPU算力回租的财务兜底，解决其融资难题。作为交换，英伟达将抽取这些云厂商的营收分成，直接参与下游算力市场的利润分配，将掌控力延伸至产业链下游。"
  },
  {
    "id": "wscn:3776051",
    "domain": "股票",
    "title": "今晚，沃什时代首份非农出炉，世界杯或营造就业\"虚火\"",
    "url": "https://wallstreetcn.com/articles/3776051",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T06:21:07+00:00",
    "summary": "美联储新主席Warsh上任后首份非农就业报告今晚揭晓，市场共识预期新增11.3万、较5月大幅回落，但高盛警告FIFA世界杯或虚增约4万临时岗位，真实劳动力降温可能比数字更深。ADP、PMI就业分项、初请失业金人数多项指标齐发警报，与此同时，加息预期持续升温，9月加息概率已达80%。数据若低于预期，美债与美元将面临剧烈波动。"
  },
  {
    "id": "wscn:3776053",
    "domain": "股票",
    "title": "日本长债集体下跌！外资6月抛售日本债券规模为2023年以来之最",
    "url": "https://wallstreetcn.com/articles/3776053",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T06:17:25+00:00",
    "summary": "更多消息，持续更新中"
  },
  {
    "id": "wscn:3776030",
    "domain": "股票",
    "title": "创业板大跌近5%，算力硬件、芯片集体下挫，存储芯片“一哥”跌停，贵金属逆势拉升，恒科指转跌，生物医药大涨",
    "url": "https://wallstreetcn.com/articles/3776030",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T06:09:37+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市超3100股飘红，上午半天成交2.26万亿。沪深两市半日成交额2.24万亿，较上个交易日缩量近1800亿。板块方面，半导体、算力硬件产业链下挫，存储器、晶圆、CPO方向领跌。金融科技、光伏、创新药题材走弱，大金融跌幅靠前。超硬材料、稀土永磁、黄金、机器人概念股活跃。"
  },
  {
    "id": "wscn:3776049",
    "domain": "股票",
    "title": "穿越3.19万亿“迷雾”，保险业正在进入“二次发育”",
    "url": "https://wallstreetcn.com/articles/3776049",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T06:09:30+00:00",
    "summary": "高增长告一段落，新故事刚刚开始"
  },
  {
    "id": "wscn:3776046",
    "domain": "股票",
    "title": "“新美联储通讯社”：沃什称通胀风险下降，但拒绝透露7月是否加息",
    "url": "https://wallstreetcn.com/articles/3776046",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T05:56:01+00:00",
    "summary": "美联储主席沃什在欧洲央行论坛释放通胀缓和信号，称近期通胀预期下降是其强硬立场奏效的早期证据，但对7月是否加息刻意保持沉默。内部分歧同样暗流涌动——18位官员中9人支持年内加息、8人主张按兵不动。与此同时，白宫公开反对加息并暗指政治干预，沃什则强硬回应：\"美联储独立性不会有任何改变。\""
  },
  {
    "id": "wscn:3775877",
    "domain": "股票",
    "title": "数据脱敏还是风暴前夜：6月非农会否再掀巨浪？",
    "url": "https://wallstreetcn.com/premium/articles/3775877?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T05:55:20+00:00",
    "summary": "6月非农受世界杯支撑或仍强，剔除后趋势降温，数据将决定加息交易是否修正及风险资产走向。"
  },
  {
    "id": "wscn:3776048",
    "domain": "股票",
    "title": "Meta卖AI算力，是认输还是破局？华尔街观点分裂",
    "url": "https://wallstreetcn.com/articles/3776048",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T05:47:04+00:00",
    "summary": "悲观派认为，Meta此举暗示其内部AI产品增速不及预期、正淡出前沿竞赛；乐观派则坚称此乃闲置产能变现的理性选择，可改善预计转负的自由现金流并回馈1450亿美元的年度资本开支。Meta潜在入局已冲击CoreWeave等云算力同行。"
  },
  {
    "id": "wscn:3776043",
    "domain": "股票",
    "title": "加入折叠屏战场，苹果面板采购超过华为",
    "url": "https://wallstreetcn.com/articles/3776043",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:40:13+00:00",
    "summary": "市场格局也要生变"
  },
  {
    "id": "wscn:3776042",
    "domain": "股票",
    "title": "中企出海、AI拉动下 广州甲级写字楼租赁净吸纳量增长超3倍",
    "url": "https://wallstreetcn.com/articles/3776042",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:35:57+00:00",
    "summary": "新的分化逻辑"
  },
  {
    "id": "wscn:3776036",
    "domain": "股票",
    "title": "高盛：世界杯将增加4万非农就业",
    "url": "https://wallstreetcn.com/articles/3776036",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:18:13+00:00",
    "summary": "世界杯或成6月非农“意外推手”。高盛预计赛事带来约4万个岗位，6月总非农就业将增加14万人；主办城市、酒店休闲招聘走强，但短期繁荣或掩盖劳动力市场真实降温。"
  },
  {
    "id": "wscn:3776038",
    "domain": "股票",
    "title": "沃什“鸽派”转向扑灭加息火苗，黄金企稳4000美元，折射利率路径重新定价",
    "url": "https://wallstreetcn.com/articles/3776038",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:18:04+00:00",
    "summary": "沃什未释放更鹰派信号，美联储年内加息预期降温，黄金重返4000美元上方，但市场仍“无法明确把握沃什的前景判断”，因为他拒绝提供前瞻指引。美国经济数据分化，非农将成检验利率路径与金价反弹成色的关键。"
  },
  {
    "id": "wscn:3776040",
    "domain": "股票",
    "title": "白宫加速制定AI模型发布标准，前沿模型发布受限将成常态？",
    "url": "https://wallstreetcn.com/articles/3776040",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:17:58+00:00",
    "summary": "美国AI监管迎来拐点，白宫拟最快下周推出前沿模型自愿安全标准，并已介入GPT-5.6发布节奏，要求其初始阶段仅向经审查的特定群体开放，更广泛的发布预计推迟至下周进行。统一框架或将重塑巨头IPO前的合规成本、估值逻辑与全球监管格局。"
  },
  {
    "id": "wscn:3775736",
    "domain": "股票",
    "title": "当台积电、三星、SK海力士都在抢货，电子级氢氟酸已成为AI芯片制造不可替代的“化学钥匙”",
    "url": "https://wallstreetcn.com/premium/articles/3775736?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:02:19+00:00",
    "summary": "电子级氢氟酸正处于“AI算力需求爆发+半导体产能扩张+国产替代加速+成本推动涨价”的四重共振窗口期。"
  },
  {
    "id": "wscn:3776034",
    "domain": "股票",
    "title": "日元最坏情景进入交易员视野，200关口从“不可想象”变为中期尾部风险",
    "url": "https://wallstreetcn.com/articles/3776034",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T03:42:08+00:00",
    "summary": "受美日利差、日本加息迟缓及高额债务影响，日元兑美元跌至近40年低点，机构预期极端情景下日元看跌至200关口。市场认为政府干预仅为短暂减速带，而当前最大风险是干预失效引发失序崩盘。"
  },
  {
    "id": "wscn:3776033",
    "domain": "股票",
    "title": "花旗继续看多日股：大幅上调日经225目标至90000点，年底前仍有约30%上行空间！",
    "url": "https://wallstreetcn.com/articles/3776033",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T03:27:49+00:00",
    "summary": "花旗高喊日股牛市未完，短短一个月将日经225目标从70000点大幅抬至90000点：企业提价带动利润率和ROE上行，全球流动性助推重估，日本央行会议的平稳落地降低了市场扰动。与此同时，科技股盈利上修仍是核心燃料，数据中心投资成最大变量。"
  },
  {
    "id": "wscn:3776035",
    "domain": "股票",
    "title": "先建设后审批！SemiAnalysis：xAI在美国孟菲斯以极其激进的方式解决电力问题",
    "url": "https://wallstreetcn.com/articles/3776035",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T03:27:41+00:00",
    "summary": "SemiAnalysis披露，xAI在孟菲斯采用“先建设，后审批”的激进策略应对算力电力缺口。其移动燃气轮机在五个月内近乎翻倍，且多在无正式空气许可下运行。"
  },
  {
    "id": "wscn:3776037",
    "domain": "股票",
    "title": "当前困境越大未来利润越高？高盛盯上了中国的猪肉",
    "url": "https://wallstreetcn.com/articles/3776037",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T03:24:06+00:00",
    "summary": "猪价跌至9元/公斤，亏损正把行业逼到现金流极限。但随着能繁母猪目标下调、亏损加深和产能退出加速，高盛判断2026年下半年生猪供需由过剩转向短缺，猪价将回升至15元/公斤。正的赢家不是现在便宜，而是谁能活到涨价。"
  },
  {
    "id": "wscn:3776039",
    "domain": "股票",
    "title": "当Meta开始卖算力",
    "url": "https://wallstreetcn.com/articles/3776039",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T03:23:00+00:00",
    "summary": "这标志着AI基建从“无脑囤积”进入\"算账变现\"的阶段：AI算力利用率存在天然缺口，训练期间满负荷，训练后利用骤降。Meta率先承认这一周期性浪费，并通过“先囤积、后决策”策略布局，将峰值算力转为商机。"
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
    "id": "rss:https://www.netinterest.co/p/two-tribes",
    "domain": "股票",
    "title": "Two Tribes",
    "url": "https://www.netinterest.co/p/two-tribes",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-02-27T17:42:58+00:00",
    "summary": "Private Credit, Public Markets and the AI Reckoning"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.00245",
    "domain": "金融",
    "title": "Agent-to-Agent Finance: Blockchain Payments and Trust Infrastructure for Autonomous AI Agents",
    "url": "https://arxiv.org/abs/2607.00245",
    "source": "Hui Gong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:00:00+00:00",
    "summary": "arXiv:2607.00245v1 Announce Type: new Abstract: Autonomous AI agents are beginning to occupy a position between analytical tools and transacting counterparties. They can interpret goals, call external"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.00279",
    "domain": "金融",
    "title": "Night and Day: Diurnal Warming and Structural Transformation in India",
    "url": "https://arxiv.org/abs/2607.00279",
    "source": "Vedarshi Shastry",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:00:00+00:00",
    "summary": "arXiv:2607.00279v1 Announce Type: new Abstract: This paper finds diverging partial effects of diurnal warming (higher nighttime and daytime temperatures) on agricultural wage-labour shares from decada"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.00475",
    "domain": "金融",
    "title": "End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing: When Do AI Models Beat Simple Rules?",
    "url": "https://arxiv.org/abs/2607.00475",
    "source": "Austin Pollok, Kevin Robik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:00:00+00:00",
    "summary": "arXiv:2607.00475v1 Announce Type: new Abstract: Timing-based tilts across asset classes can drive much of the risk and return of a diversified cross-asset portfolio. The standard approach forecasts re"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.00504",
    "domain": "金融",
    "title": "How optimistic inflow forecasts distort dispatch, prices, and contracts in hydro-dominated power systems: evidence from Brazil",
    "url": "https://arxiv.org/abs/2607.00504",
    "source": "Arthur Brigatto, Alexandre Street, Joaquim Dias Garcia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:00:00+00:00",
    "summary": "arXiv:2607.00504v1 Announce Type: new Abstract: Centralized hydrothermal planning models determine generation schedules and electricity spot prices based on inflow forecasts in audited-cost power syst"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.00551",
    "domain": "金融",
    "title": "Talking Politics with Artificial Intelligence",
    "url": "https://arxiv.org/abs/2607.00551",
    "source": "Ziwen Zu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:00:00+00:00",
    "summary": "arXiv:2607.00551v1 Announce Type: new Abstract: Large language models (LLMs), a prominent form of artificial intelligence (AI), are becoming everyday interfaces for political questions, but most excha"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.00856",
    "domain": "金融",
    "title": "Shapley in Context: Explaining Financial Language with Domain Expertise",
    "url": "https://arxiv.org/abs/2607.00856",
    "source": "Dangxing Chen, Pengzhan Guo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:00:00+00:00",
    "summary": "arXiv:2607.00856v1 Announce Type: new Abstract: In recent years, large language models have achieved remarkable success and have seen growing adoption in financial applications. At the same time, expl"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.00883",
    "domain": "金融",
    "title": "Tail Risk Management with Puts and Trend Following: A CVaR Framework for Crashes and Drawdowns",
    "url": "https://arxiv.org/abs/2607.00883",
    "source": "Miquel Noguer I Alonso, Ali Al Fallouji",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:00:00+00:00",
    "summary": "arXiv:2607.00883v1 Announce Type: new Abstract: Tail-risk management is not only an instrument-selection problem. It is an allocation problem across loss mechanisms: abrupt crash states, volatility re"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.00977",
    "domain": "金融",
    "title": "Competitive effects of transmission constraints in the German electricity market",
    "url": "https://arxiv.org/abs/2607.00977",
    "source": "Alice Lixuan Xu, Clemens Stiewe",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:00:00+00:00",
    "summary": "arXiv:2607.00977v1 Announce Type: new Abstract: This paper estimates the effect of cross-border transmission constraints on suspected market power abuse in the German wholesale electricity market. Usi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.01101",
    "domain": "金融",
    "title": "The Economic Benefits and Costs of AI and Policies to Mitigate AI's Impact on Inequality",
    "url": "https://arxiv.org/abs/2607.01101",
    "source": "Matthew O. Jackson, Zafer Kanik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:00:00+00:00",
    "summary": "arXiv:2607.01101v1 Announce Type: new Abstract: We examine the economic impact of increasingly productive AI and policies that spread its benefits across the economy. Improvements in AI productivity t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.01198",
    "domain": "金融",
    "title": "When large trades are not news: Liquidity tail risk and price discovery",
    "url": "https://arxiv.org/abs/2607.01198",
    "source": "Umut \\c{C}etin, Mingwei Lin, Giulia Livieri",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:00:00+00:00",
    "summary": "arXiv:2607.01198v1 Announce Type: new Abstract: When is a large trade news, and when is it a liquidity shock? We study this question in a sequential competitive limit order book with asymmetric inform"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.00208",
    "domain": "金融",
    "title": "Channel Adoption Pathways and Post-Adoption Behavior",
    "url": "https://arxiv.org/abs/2508.00208",
    "source": "Shirsho Biswas, Hema Yoganarasimhan, Haonan Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:00:00+00:00",
    "summary": "arXiv:2508.00208v4 Announce Type: replace Abstract: The rapid growth of digital shopping channels has led many traditional retailers to invest in e-commerce websites and mobile apps. While prior resea"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.25472",
    "domain": "金融",
    "title": "Exponential Hedging for the Ornstein-Uhlenbeck Process in the Presence of Linear Price Impact",
    "url": "https://arxiv.org/abs/2509.25472",
    "source": "Yan Dolinsky",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:00:00+00:00",
    "summary": "arXiv:2509.25472v2 Announce Type: replace Abstract: In this work we study a continuous time exponential utility maximization problem in the presence of a linear temporary price impact. More precisely,"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.19622",
    "domain": "金融",
    "title": "Wage-Setting Constraints and Firm Responses to Demand Shocks",
    "url": "https://arxiv.org/abs/2512.19622",
    "source": "Manudeep Bhuller, Lukas Delgado-Prieto, Santiago Hermo, Linnea Lorentzen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:00:00+00:00",
    "summary": "arXiv:2512.19622v2 Announce Type: replace Abstract: This paper investigates how institutional wage-setting constraints, such as a national minimum wage or collectively bargained wages, affect firm res"
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.03874",
    "domain": "金融",
    "title": "ASRI: An Aggregated Systemic Risk Index for Cryptocurrency Markets",
    "url": "https://arxiv.org/abs/2602.03874",
    "source": "Murad Farzulla, Andrew Maksakov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:00:00+00:00",
    "summary": "arXiv:2602.03874v3 Announce Type: replace Abstract: The Aggregated Systemic Risk Index (ASRI) is an interpretable, channel-decomposed measure of crypto-native systemic stress, aggregating four transmi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.02503",
    "domain": "金融",
    "title": "Pay Beliefs and the Amenity-Pay Tradeoff",
    "url": "https://arxiv.org/abs/2606.02503",
    "source": "Martin Eckhoff Andresen, Manudeep Bhuller, Alfred L{\\o}vgren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:00:00+00:00",
    "summary": "arXiv:2606.02503v3 Announce Type: replace Abstract: This paper studies how workers' beliefs about pay shape the tradeoffs between pay and workplace amenities. We design a multi-stage incentivized surv"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.05624",
    "domain": "金融",
    "title": "Mean-field games with unbounded controls: a weak formulation approach to global solutions",
    "url": "https://arxiv.org/abs/2603.05624",
    "source": "Ulrich Horst, Takashi Sato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:00:00+00:00",
    "summary": "arXiv:2603.05624v2 Announce Type: replace-cross Abstract: We establish an existence of equilibrium result for a class of non-Markovian mean-field games with unbounded control space in weak formulation"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.07290",
    "domain": "金融",
    "title": "Boundary behaviour of the Volterra square-root process",
    "url": "https://arxiv.org/abs/2606.07290",
    "source": "Martin Friesen, Stefan Gerhold, Kristof Wiedermann",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-02T04:00:00+00:00",
    "summary": "arXiv:2606.07290v2 Announce Type: replace-cross Abstract: In this work, we study the boundary behaviour of the Volterra square-root process on $\\R_+$. For regular Volterra kernels, we establish a time"
  }
]
```
