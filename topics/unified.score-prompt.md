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

- 今日日期：`2026-07-09`
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
  "date": "2026-07-09",
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
    "points": 3666373,
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
    "points": 1771865,
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
    "points": 1458703,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 950853,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 941089,
    "published_at": "2026-07-05T02:00:00+00:00",
    "summary": "用不上codex的朋友们！新的国产Agent直接上手，来跑通8大用法～\n感谢朋友们的三连+关注～"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 859224,
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
    "points": 854794,
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
    "points": 791840,
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
    "points": 566348,
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
    "points": 507761,
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
    "points": 390466,
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
    "points": 350492,
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
    "points": 235053,
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
    "points": 176573,
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
    "points": 176004,
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
    "points": 169412,
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
    "points": 165284,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 159144,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 105804,
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
    "points": 92469,
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
    "points": 90653,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 75188,
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
    "points": 52895,
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
    "points": 41984,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 37696,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 33727,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28735,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22610,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1LWTe6gEVc",
    "domain": "AI",
    "title": "Claude code帮我实现综述论文自由！",
    "url": "http://www.bilibili.com/video/av116842504918580",
    "source": "做科研的大师兄",
    "platform": "bilibili",
    "points": 20708,
    "published_at": "2026-07-01T03:07:40+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1JU7E6PEar",
    "domain": "AI",
    "title": "Cursor 已死？我为什么要退订 Cursor ？",
    "url": "http://www.bilibili.com/video/av116819553683121",
    "source": "小狗瑞恩Ryan",
    "platform": "bilibili",
    "points": 19054,
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
    "points": 17847,
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
    "points": 17364,
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
    "points": 16406,
    "published_at": "2026-07-01T06:09:09+00:00",
    "summary": "【全500集】目前B站最全最细的AI Agent零基础全套教程（从入门到精通），5天从入门到精通AI Agent，学完即可就业！看完这一套AI Agent教程就够了！"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 13013,
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
    "points": 12945,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1fiLr6XEj8",
    "domain": "AI",
    "title": "【大白哥AI与安全】手把手教你AI渗透,挖漏洞",
    "url": "http://www.bilibili.com/video/av116601936418546",
    "source": "大白哥AI与安全",
    "platform": "bilibili",
    "points": 12046,
    "published_at": "2026-05-19T15:33:02+00:00",
    "summary": "一键三连加关注，私信大白哥免费领取课件\n更多红队攻防实战课程，请私信大白哥咨询"
  },
  {
    "id": "bvid:BV1jZ5F6eEzQ",
    "domain": "AI",
    "title": "答应我，别再和AI一起拉屎了；Vibe Coding如何避免屎山",
    "url": "http://www.bilibili.com/video/av116677031236717",
    "source": "写代码小猴子Tong",
    "platform": "bilibili",
    "points": 11630,
    "published_at": "2026-06-01T23:00:00+00:00",
    "summary": "复杂度之战05：答应我，不要再和AI一起拉屎了；Vibe Coding如何避免写出屎山\n\n为什么你的项目越写越难改?\n为什么 AI 写的代码局部没有问题,合在一起就是一坨屎山?\n\n从一个最简单的数学事实讲起:软件复杂度的增长为啥会这么快。用一个圆的动画,直观演示&quot;解耦&quot;是如何降低屎山的规模的。\n\n本期内容: \n▸ 为什么屎山会膨胀得如此之快 \n▸ 一个圆讲清楚解耦的威力 \n▸ "
  },
  {
    "id": "bvid:BV1zV54zbEbU",
    "domain": "AI",
    "title": "2分钟在vscode里使用MCP服务",
    "url": "http://www.bilibili.com/video/av114365231531540",
    "source": "程序员三千",
    "platform": "bilibili",
    "points": 10675,
    "published_at": "2025-04-19T15:10:12+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1WBTX6kE1B",
    "domain": "AI",
    "title": "【2026版】这绝对是B站唯一将Vibe Coding从入门到实战讲明白的教程，手把手带你从入门到代码实战开发，存下吧，比啃书好太多了！拿走不谢，允许白嫖！",
    "url": "http://www.bilibili.com/video/av116871663722218",
    "source": "码士集团-马小雪",
    "platform": "bilibili",
    "points": 10060,
    "published_at": "2026-07-06T06:47:51+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！ 【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1oqMt6FEj8",
    "domain": "AI",
    "title": "【2026最新Claude Code】Claude Code保姆级完整教程-Claude Code新手保姆级教程-最强AI助手！从入门到进阶【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av116877216980674",
    "source": "资深bug设计工程师",
    "platform": "bilibili",
    "points": 9218,
    "published_at": "2026-07-07T06:18:15+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV12ojm64EU6",
    "domain": "AI",
    "title": "🧲 Claude Code 工作流：长程任务的规划和执行利器 ⛓️",
    "url": "http://www.bilibili.com/video/av116800494767674",
    "source": "沧海九粟",
    "platform": "bilibili",
    "points": 9244,
    "published_at": "2026-06-24T00:00:00+00:00",
    "summary": "GAC 平台：https://gaccode.com/signup?ref=UWDADYQI\n官方文档：https://code.claude.com/docs/en/workflows\n状态栏技能：https://github.com/webup/skills-cc#-webup-statusline"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9161,
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
    "points": 7532,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1vcKS67Ee8",
    "domain": "AI",
    "title": "【AI Coding】这绝对是你看过讲的最好的Vibe Coding企业级项目实战，从入门到进阶，30分钟速通Claude Code✚Codex✚Cursor",
    "url": "http://www.bilibili.com/video/av116832321209292",
    "source": "图灵学院官方",
    "platform": "bilibili",
    "points": 7334,
    "published_at": "2026-06-29T08:02:48+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1QU6GYFEio",
    "domain": "AI",
    "title": "[课程4] 用Cursor开发数据库真的很简单 | Agent应用 | 用Codebase解决跨文件错误",
    "url": "http://www.bilibili.com/video/av113742109021318",
    "source": "Zhu的AI日记",
    "platform": "bilibili",
    "points": 6994,
    "published_at": "2024-12-31T12:30:00+00:00",
    "summary": "***这是全网最完整的分享如何在不懂编程的情况下，利用结构化思维，用Cursor开发商业app的系列课程。\n《懒人记单词》是基于艾宾浩斯遗忘曲线设计的记单词神器，它可以对每一个单词进行人性化的解读，并在每一个遗忘周期到来时及时提醒，并通过单词释义选择，拼写和造句进行全方位的巩固，同时AI还能对你的句子进行多维度的评估，确保你对每一个单词不仅会认，而且会用。\n\n***你将在本视频中学到：\n1.数据库"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6512,
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
    "points": 6436,
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
    "points": 6430,
    "published_at": "2026-01-07T04:47:17+00:00",
    "summary": "OpenCode 是一款面向开发者的开源 AI CLI 编程工具，支持多模型并行、LSP 自动加载、极速响应与非订阅制计费。无论是命令行、桌面 App 还是 VS Code 插件，OpenCode 都提供高效、不啰嗦的 AI 编程体验，是 Cursor 与 Claude Code 的有力替代方案。"
  },
  {
    "id": "bvid:BV1uz8jzdEZy",
    "domain": "AI",
    "title": "AI Agent 设计助手功能教程丨自然语言交互驱动 AI 智能设计花境、导出苗木清单",
    "url": "http://www.bilibili.com/video/av114929986241780",
    "source": "D5渲染器",
    "platform": "bilibili",
    "points": 6406,
    "published_at": "2025-07-28T10:55:00+00:00",
    "summary": "全新上线的D5 2.11版本正式推出D5 AI 设计助手（AI Agent），能够准确理解设计意图，智能处理复杂任务。与 AI 设计助手对话，通过自然语言交互驱动 AI 完成专业任务。首次上线带来了「花境生成器」「智能苗木清单」「D5 Bot」，未来设计助手还将具备更多能力，令创作者更专注核心创意塑造和方案决策。\n\n获取D5渲染器： https://www.d5render.cn/\n\n2.11宣传"
  },
  {
    "id": "bvid:BV1E8Tk6MEkw",
    "domain": "AI",
    "title": "AI Agent教程全集丨从入门到进阶丨适合99%小白入行的Agent教程！360°讲解大模型合集（比例RAG +langchain+Agent)全程干货无废话",
    "url": "http://www.bilibili.com/video/av116848259498783",
    "source": "Agent教程",
    "platform": "bilibili",
    "points": 5728,
    "published_at": "2026-07-02T03:38:47+00:00",
    "summary": "陆陆续续也整理了不少资源，希望能帮大家少走一些弯路！无论是学业还是事业，都希望你顺顺利利  看在UP这么努力的份上，求个三连+关注嘛\n\n1️⃣ 大模型入门学习路线图（附学习资源）\n2️⃣ 大模型方向必读书籍PDF版\n3️⃣ 大模型面试题库\n4️⃣ 大模型项目源码\n5️⃣ 超详细海量大模型LLM实战项目\n6️⃣ Langchain/RAG/Agent学习资源\n7️⃣ LLM大模型系统0到1入门学习教"
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
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/rapidus-fab-roadmap-examined",
    "domain": "AI 算力 / 半导体",
    "title": "Rapidus fab roadmap examined — first new leading-edge chipmaker in decades has one Hokkaido fab, a 2027 deadline, and 60 potential customers",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/rapidus-fab-roadmap-examined",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T16:29:26+00:00",
    "summary": "Rapidus is building Japan's entire return to leading-edge logic on one fab in Chitose, Hokkaido."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/china-alleges-that-claude-code-contains-backdoors-calls-mechanism-a-serious-threat-govt-claims-claude-sends-sensitive-information-to-remote-servers-without-consent",
    "domain": "AI 算力 / 半导体",
    "title": "China alleges that Claude Code contains backdoors, calls mechanism 'a serious threat' — Gov't claims Claude sends sensitive information to remote servers without consent",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/china-alleges-that-claude-code-contains-backdoors-calls-mechanism-a-serious-threat-govt-claims-claude-sends-sensitive-information-to-remote-servers-without-consent",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T15:54:14+00:00",
    "summary": "China is warning against the use of Claude Code versions released between April and June 2026 after it's revealed that hidden code is sending sensitive user information to remote servers. The governme"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/hidden-backdoor-found-in-tenda-routers-goes-unpatched-despite-warnings-from-cybersecurity-researchers-affected-firmware-allows-admin-access-without-a-password",
    "domain": "AI 算力 / 半导体",
    "title": "Hidden backdoor in Tenda routers goes unpatched as company ignores warnings from cybersecurity researchers — Chinese company's firmware allows admin access without a password",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/hidden-backdoor-found-in-tenda-routers-goes-unpatched-despite-warnings-from-cybersecurity-researchers-affected-firmware-allows-admin-access-without-a-password",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T15:16:25+00:00",
    "summary": "CERT/CC has disclosed a critical authentication backdoor affecting multiple Tenda router firmware versions. Tracked as CVE-2026-11405, the flaw grants full administrator access without valid credentia"
  },
  {
    "id": "rss:https://www.tomshardware.com/phones/budget-smartphone-market-collapses-under-the-weight-of-memory-shortages-sales-expected-to-drop-22-percent-memory-alone-now-comprises-up-to-64-percent-of-the-total-cost-of-lower-tier-smartphones",
    "domain": "AI 算力 / 半导体",
    "title": "Budget smartphone market collapses under the weight of memory shortages, sales expected to drop 22% — memory alone now comprises up to 64% of the total cost of lower-tier smartphones",
    "url": "https://www.tomshardware.com/phones/budget-smartphone-market-collapses-under-the-weight-of-memory-shortages-sales-expected-to-drop-22-percent-memory-alone-now-comprises-up-to-64-percent-of-the-total-cost-of-lower-tier-smartphones",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T15:15:36+00:00",
    "summary": "The global AI memory squeeze is pricing cheap phones out of existence and forcing mid-range devices to compromise on hardware."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/jedec-releases-new-sphbm4-standard-to-slash-ai-memory-costs-narrow-512-bit-interface-enables-dropping-expensive-interposers-for-organic-substrates",
    "domain": "AI 算力 / 半导体",
    "title": "JEDEC releases new SPHBM4 standard to slash AI memory costs — Narrow 512-bit interface enables dropping expensive interposers for organic substrates",
    "url": "https://www.tomshardware.com/pc-components/dram/jedec-releases-new-sphbm4-standard-to-slash-ai-memory-costs-narrow-512-bit-interface-enables-dropping-expensive-interposers-for-organic-substrates",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T15:03:33+00:00",
    "summary": "SPHBM4 promises HBM4-class bandwidth without usage of silicon interposer and CoWoS-like packaging."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/global-consumer-wi-fi-router-shipments-fell-6-percent-in-q1-2026-mesh-systems-and-gaming-routers-still-prove-popular",
    "domain": "AI 算力 / 半导体",
    "title": "Global consumer Wi-Fi router shipments fell 6% in Q1 2026, down 34% from 2021 peak — mesh systems and gaming routers still prove popular",
    "url": "https://www.tomshardware.com/networking/routers/global-consumer-wi-fi-router-shipments-fell-6-percent-in-q1-2026-mesh-systems-and-gaming-routers-still-prove-popular",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T14:49:27+00:00",
    "summary": "Global consumer Wi-Fi router shipments have declined 34 percent from their peak in 2021"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/sipearls-long-awaited-rhea-cpu-finally-gets-in-the-lab-opening-the-door-for-europes-first-sovereign-hpc-cpu-availability-of-rhea1-is-scheduled-for-end-of-2026-sipearl-vp-says-following-long-development-process",
    "domain": "AI 算力 / 半导体",
    "title": "SiPearl's long-awaited Rhea CPU finally gets in the lab, opening the door for Europe's first sovereign HPC CPU — 'availability of Rhea1 is scheduled for end of 2026' SiPearl VP says, following long de",
    "url": "https://www.tomshardware.com/pc-components/cpus/sipearls-long-awaited-rhea-cpu-finally-gets-in-the-lab-opening-the-door-for-europes-first-sovereign-hpc-cpu-availability-of-rhea1-is-scheduled-for-end-of-2026-sipearl-vp-says-following-long-development-process",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T14:44:59+00:00",
    "summary": "How a limited run CPU could open the right doors for Europe's first HPC processors on markets its developers barely hoped to address any time soon."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/power-company-hikes-data-center-bills-by-30-percent-cuts-residential-electricity-costs-by-1-3-percent-oregon-approves-change-through-power-act-pushes-developments-using-more-than-20-megawatts-of-power-to-pay-their-fair-share",
    "domain": "AI 算力 / 半导体",
    "title": "Power company hikes data center bills by 30%, cuts residential electricity costs by 1.3% — Oregon approves change through POWER Act, pushes developments using more than 20 Megawatts of power to pay th",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/power-company-hikes-data-center-bills-by-30-percent-cuts-residential-electricity-costs-by-1-3-percent-oregon-approves-change-through-power-act-pushes-developments-using-more-than-20-megawatts-of-power-to-pay-their-fair-share",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T13:56:27+00:00",
    "summary": "Oregon approves the 29.7% price hike that Portland General Electric (PGE), the state's largest power provider, will impose on users that consume 20MW or more. This move is backed by Oregon's POWER Act"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/a-team-of-engineers-called-slopfix-charges-10000-a-week-to-delete-ai-generated-code-using-ai-agents",
    "domain": "AI 算力 / 半导体",
    "title": "'Slopfix' software team charges $10,000 a week to delete AI-generated code bloat — ironically, the team uses AI agents to trim messy repositories by up to 65%",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/a-team-of-engineers-called-slopfix-charges-10000-a-week-to-delete-ai-generated-code-using-ai-agents",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T13:19:17+00:00",
    "summary": "A software house known as 'Slopfix' has launched a fixed-price service that refactors AI-generated codebases, charging $10,000 for one week of work."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/fi-ultra-becomes-first-dog-tracker-powered-by-starlink-satellites-the-fi-ultra-dog-tracker-makes-fido-trackable-via-satellite-onboard-gps-and-lte-connectivity",
    "domain": "AI 算力 / 半导体",
    "title": "Fi Ultra becomes first dog tracker powered by Starlink satellites – the Fi Ultra Dog Tracker makes Fido trackable via satellite, onboard GPS, and LTE connectivity",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/fi-ultra-becomes-first-dog-tracker-powered-by-starlink-satellites-the-fi-ultra-dog-tracker-makes-fido-trackable-via-satellite-onboard-gps-and-lte-connectivity",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T13:11:25+00:00",
    "summary": "Smart pet technology firm Fi has launched the Fi Ultra Dog Tracker today, the first such device with Starlink connectivity."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/air-cooling/cooler-master-v4-and-v8-3dhp-review",
    "domain": "AI 算力 / 半导体",
    "title": "Cooler Master V4 and V8 3DHP Review: A masterful engineering achievement",
    "url": "https://www.tomshardware.com/pc-components/air-cooling/cooler-master-v4-and-v8-3dhp-review",
    "source": "Albert Thomas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T13:02:20+00:00",
    "summary": "Cooler Master’s 3DHP heatpipes, in its Master V4 and V8 coolers, are the biggest advancement in air cooling technology in years. But early adoption comes at a price."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/cracked-version-of-assassins-creed-black-flag-resynced-leaked-days-prior-to-official-release-despite-denuvo-drm-protection-denuvo-unable-to-stop-crackers-with-some-finding-ways-to-completely-remove-it-from-other-titles",
    "domain": "AI 算力 / 半导体",
    "title": "Cracked version of Assassin’s Creed Black Flag Resynced leaked days prior to official release despite Denuvo DRM protection — Denuvo unable to stop crackers, with some finding ways to completely remov",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/cracked-version-of-assassins-creed-black-flag-resynced-leaked-days-prior-to-official-release-despite-denuvo-drm-protection-denuvo-unable-to-stop-crackers-with-some-finding-ways-to-completely-remove-it-from-other-titles",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T12:29:12+00:00",
    "summary": "Ubisoft's remake of the 2013 game has been circulating online more than a month before its official release date, despite Denuvo DRM protection. Incident questions the effectivity of anti-piracy app, "
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/modding-tool-dlss-swapper-might-infect-your-pc-with-malware-if-you-download-the-wrong-files-app-creator-warns-against-using-random-user-submitted-dlls",
    "domain": "AI 算力 / 半导体",
    "title": "Modding tool 'DLSS Swapper' might infect your PC with malware if you download the wrong files — App creator warns against using random, user-submitted DLLs",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/modding-tool-dlss-swapper-might-infect-your-pc-with-malware-if-you-download-the-wrong-files-app-creator-warns-against-using-random-user-submitted-dlls",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T12:18:47+00:00",
    "summary": "The creator of DLSS Swapper is warning against using random DLLs that claim to fix issues pertaining to DLSS, FSR, or XeSS, even if said file is available on the app's GitHub repo."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-mice/save-usd527-on-this-1440p-gaming-pc-from-newegg-with-a-16gb-rtx-5060-ti-right-now-huge-discount-for-high-end-performance-rig-with-an-intel-core-i7-14700f-32gb-ddr5-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save $527 on this 1440p gaming PC from Newegg with a 16GB RTX 5060 Ti right now — huge discount for high-end performance rig with an Intel Core i7-14700F, 32GB DDR5, and a 1TB SSD",
    "url": "https://www.tomshardware.com/peripherals/gaming-mice/save-usd527-on-this-1440p-gaming-pc-from-newegg-with-a-16gb-rtx-5060-ti-right-now-huge-discount-for-high-end-performance-rig-with-an-intel-core-i7-14700f-32gb-ddr5-and-a-1tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T11:44:32+00:00",
    "summary": "This great value gaming PC from Newegg's ABS brand features a 16GB RTX 5060 Ti GPU and 32GB of DDR5-6400 RAM, giving you a rig ready for 1440p gaming."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/valve-releases-drivers-notes-to-make-windows-work-on-steam-hardware-but-refuses-to-support-it-tells-users-it-doesnt-offer-support-for-windows-on-steam-hardware-gaming-company-provides-resources-as-is",
    "domain": "AI 算力 / 半导体",
    "title": "Valve releases drivers, notes to make Windows work on Steam hardware, but refuses to support it — tells users it doesn’t offer support for ‘Windows on Steam Hardware,’ gaming company provides resource",
    "url": "https://www.tomshardware.com/video-games/console-gaming/valve-releases-drivers-notes-to-make-windows-work-on-steam-hardware-but-refuses-to-support-it-tells-users-it-doesnt-offer-support-for-windows-on-steam-hardware-gaming-company-provides-resources-as-is",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T11:20:00+00:00",
    "summary": "These drivers will make it easier for your Steam Deck or Steam Machine to play nicely with Windows 11. However, Valve says it does not offer customer support for 'Windows on Steam Hardware,' and inste"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/8bitdos-wireless-pro-2-gaming-controller-falls-to-all-time-low-price-hall-effect-gamepad-is-38-percent-off-just-usd37-19",
    "domain": "AI 算力 / 半导体",
    "title": "8Bitdo's wireless Pro 2 gaming controller falls to all-time low price — hall-effect gamepad is 38% off, just $37.19",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/8bitdos-wireless-pro-2-gaming-controller-falls-to-all-time-low-price-hall-effect-gamepad-is-38-percent-off-just-usd37-19",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T11:18:06+00:00",
    "summary": "Hitting an all-time low price at Amazon, 8Bitdo's wireless Pro 2 gaming controller with hall-effect joysticks is 38% off for Prime members."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nvidia-touts-vera-cpus-single-threaded-performance-as-its-agentic-ai-advantage-frames-chip-as-a-max-single-threaded-cpu-at-scale-not-a-parallel-monster",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia touts Vera CPU's single-threaded performance as its agentic AI advantage, reveals next-gen 'Rigel' Arm CPU cores — frames chip as a 'max single-threaded CPU at scale,' not a parallel monster",
    "url": "https://www.tomshardware.com/pc-components/cpus/nvidia-touts-vera-cpus-single-threaded-performance-as-its-agentic-ai-advantage-frames-chip-as-a-max-single-threaded-cpu-at-scale-not-a-parallel-monster",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T11:00:00+00:00",
    "summary": "Nvidia lifts the veil a little bit more on its Vera CPU and reveals a single-thread performance monster — company claims a 1.8x uplift versus x86 competition in agentic workloads and 1.5x in coding."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/arrest-and-extradition-of-scattered-spider-hacker-shines-light-on-how-windows-telemetry-gdids-can-identify-users-microsoft-device-identifier-is-just-one-digital-fingerprint-in-a-software-world-rife-with-them",
    "domain": "AI 算力 / 半导体",
    "title": "Arrest and extradition of Scattered Spider hacker shines light on how Windows telemetry GDIDs can identify and track users — Microsoft device identifier is just one digital fingerprint in a software w",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/arrest-and-extradition-of-scattered-spider-hacker-shines-light-on-how-windows-telemetry-gdids-can-identify-users-microsoft-device-identifier-is-just-one-digital-fingerprint-in-a-software-world-rife-with-them",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T10:30:00+00:00",
    "summary": "While the use of Windows' GDID to catch Scattered Spider hacking group member Peter Stokes is unusual, that device identifier is only one bit of telemetry that can be used to fingerprint a user across"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/space/space-force-gets-first-mobile-high-powered-electromagnetic-beam-weapon-to-cripple-enemy-satellites-plans-to-deploy-32-meadowlands-units-to-detect-deny-disrupt-and-degrade-hostile-space-assets",
    "domain": "AI 算力 / 半导体",
    "title": "Space Force gets first mobile high-powered electromagnetic beam weapon to cripple enemy satellites — plans to deploy 32 ‘Meadowlands’ units to detect, deny, disrupt, and degrade hostile space assets",
    "url": "https://www.tomshardware.com/tech-industry/space/space-force-gets-first-mobile-high-powered-electromagnetic-beam-weapon-to-cripple-enemy-satellites-plans-to-deploy-32-meadowlands-units-to-detect-deny-disrupt-and-degrade-hostile-space-assets",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T10:00:00+00:00",
    "summary": "Space Force has announced that the first high-energy 'Meadowlands' electronic warfare system has been delivered for operational duty."
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
    "id": "rss:https://www.theverge.com/tech/963138/meta-smart-glasses-recording-super-sensing-ai",
    "domain": "大厂 AI 动态",
    "title": "Meta is reportedly working on smart glasses that would be recording all the time",
    "url": "https://www.theverge.com/tech/963138/meta-smart-glasses-recording-super-sensing-ai",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T22:37:25+00:00",
    "summary": "Meta might be the next company to make an always-on AI wearable. The company is working on prototype \"super sensing\" always-aware smart glasses that could continuously record audio and snap photos \"ev"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/962999/samsung-unpacked-z-fold-flip-wide-reserve-credit-preorder",
    "domain": "大厂 AI 动态",
    "title": "Get a $30 credit when you reserve Samsung’s upcoming Galaxy phones",
    "url": "https://www.theverge.com/gadgets/962999/samsung-unpacked-z-fold-flip-wide-reserve-credit-preorder",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T20:00:00+00:00",
    "summary": "Even though they haven’t been officially announced yet, Samsung is giving you a chance to save some cash when you preorder what we’re expecting to be the brand’s updated Galaxy Z Fold phones. The next"
  },
  {
    "id": "rss:https://www.theverge.com/games/963024/microsoft-xbox-reset-obsidian-fallout-layoffs",
    "domain": "大厂 AI 动态",
    "title": "Microsoft&#8217;s Xbox reset is pivoting Obsidian to make Fallout instead of Avowed",
    "url": "https://www.theverge.com/games/963024/microsoft-xbox-reset-obsidian-fallout-layoffs",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T18:50:27+00:00",
    "summary": "As part of Microsoft's big Xbox \"reset,\" which includes layoffs affecting 3,200 staffers, jettisoning studios, and shifting investments to focus on \"higher priority projects,\" Obsidian Entertainment i"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/962753/fiat-topolino-ev-us-price-specs-micromobiilty",
    "domain": "大厂 AI 动态",
    "title": "America’s cheapest new EV is smaller than a ping-pong table and tops out at 19mph",
    "url": "https://www.theverge.com/transportation/962753/fiat-topolino-ev-us-price-specs-micromobiilty",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T17:57:53+00:00",
    "summary": "When searching for an affordable electric vehicle these days, there are always tradeoffs. How much range are you willing to sacrifice, how much leg room and storage space, how many features, in the pu"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/962163/switchbot-bot-rechargeable-hands-on-review",
    "domain": "大厂 AI 动态",
    "title": "Cockroaches will learn to fear my SwitchBot Bot Rechargeable",
    "url": "https://www.theverge.com/gadgets/962163/switchbot-bot-rechargeable-hands-on-review",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T17:30:00+00:00",
    "summary": "A little robotic switch-flipper has become my sidekick in combating cockroaches. Before I got the SwitchBot Bot Rechargeable, I'd tiptoe through the dark every morning, hoping I wouldn't step on one o"
  },
  {
    "id": "rss:https://www.theverge.com/games/962837/microsoft-xbox-spin-off-sell-divest-layoffs-asha-sharma",
    "domain": "大厂 AI 动态",
    "title": "If Microsoft sold off Xbox, who would even buy it?",
    "url": "https://www.theverge.com/games/962837/microsoft-xbox-spin-off-sell-divest-layoffs-asha-sharma",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T17:10:05+00:00",
    "summary": "This week, Microsoft took a huge ax to its Xbox business. The company announced that it would be laying off 1,600 workers now, 1,600 more over the next fiscal year, and that it would be shedding four "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/962910/twelve-south-airfly-pro-summer-travel-gadgets-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Twelve South’s AirFly Pro is a great travel companion, and it&#8217;s on sale for $40",
    "url": "https://www.theverge.com/gadgets/962910/twelve-south-airfly-pro-summer-travel-gadgets-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T17:09:28+00:00",
    "summary": "If you&#8217;ve got a summer trip coming up, the last-gen Twelve South AirFly Pro is one of those gadgets that can make a long flight feel a little shorter. It lets you use your wireless headphones wi"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/962856/chatgpt-upgraded-voice-mode-gpt-live",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT’s upgraded voice mode is better at shutting up",
    "url": "https://www.theverge.com/ai-artificial-intelligence/962856/chatgpt-upgraded-voice-mode-gpt-live",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T17:00:00+00:00",
    "summary": "OpenAI is overhauling ChatGPT's voice mode with a new model that it says is more like \"talking to another person.\" The new GPT-Live-1 is designed to interrupt you less and will also wait for you to co"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/962538/mondo-robotics-beni-robot-dog-preview",
    "domain": "大厂 AI 动态",
    "title": "This jumping $800 robot camera dog filled me with joy",
    "url": "https://www.theverge.com/gadgets/962538/mondo-robotics-beni-robot-dog-preview",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T15:00:00+00:00",
    "summary": "What if you had a drone that wasn't a buzzy, annoying fly people wanted to swat - but rather a cute dog that runs and jumps? What if it could do tricks on command and film your tricks as well? What if"
  },
  {
    "id": "rss:https://www.theverge.com/tech/962781/google-pixel-11-lineup-price-increase",
    "domain": "大厂 AI 动态",
    "title": "The whole Pixel line could get more expensive this year",
    "url": "https://www.theverge.com/tech/962781/google-pixel-11-lineup-price-increase",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T14:43:13+00:00",
    "summary": "Google's upcoming Pixel lineup might cost more than last year's. A report from Dealabs spotted by 9to5Google suggests that Google could raise the starting price of its 41mm Pixel Watch 5 to $399, whil"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/truecaller-clashes-with-indias-telecom-regulator-over-anti-spam-rules/",
    "domain": "大厂 AI 动态",
    "title": "Truecaller clashes with India’s telecom regulator over anti-spam rules",
    "url": "https://techcrunch.com/2026/07/08/truecaller-clashes-with-indias-telecom-regulator-over-anti-spam-rules/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T02:30:00+00:00",
    "summary": "The caller ID company says users are increasingly ignoring and blocking calls from India's dedicated business number series."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/despite-misgivings-judge-approves-elon-musks-1-5-million-sec-settlement/",
    "domain": "大厂 AI 动态",
    "title": "Despite ‘misgivings,’ judge approves Elon Musk’s $1.5M SEC settlement",
    "url": "https://techcrunch.com/2026/07/08/despite-misgivings-judge-approves-elon-musks-1-5-million-sec-settlement/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T23:11:42+00:00",
    "summary": "The saga of Musk's tussle with the SEC over how he disclosed his growing stake in Twitter (now X) has come to an end."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/lovable-reportedly-in-talks-to-double-its-valuation-to-13-2b/",
    "domain": "大厂 AI 动态",
    "title": "Lovable reportedly in talks to double its valuation to $13.2B",
    "url": "https://techcrunch.com/2026/07/08/lovable-reportedly-in-talks-to-double-its-valuation-to-13-2b/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T22:41:33+00:00",
    "summary": "The $300 million round is expected to be led by Menlo Ventures, Sifted reported."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/feds-demand-autonomous-vehicle-companies-stop-interfering-with-first-responders/",
    "domain": "大厂 AI 动态",
    "title": "Feds demand autonomous vehicle companies stop interfering with first responders",
    "url": "https://techcrunch.com/2026/07/08/feds-demand-autonomous-vehicle-companies-stop-interfering-with-first-responders/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T21:49:33+00:00",
    "summary": "The National Highway Traffic Safety Administration said emergency scenes are not \"edge cases.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/googles-deepfake-detector-system-used-to-debunk-mcconnell-hoax-pic/",
    "domain": "大厂 AI 动态",
    "title": "Google’s deepfake detector system used to debunk McConnell hoax pic",
    "url": "https://techcrunch.com/2026/07/08/googles-deepfake-detector-system-used-to-debunk-mcconnell-hoax-pic/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T20:37:03+00:00",
    "summary": "Earlier this week, a picture seemed to show Kentucky Senator Mitch McConnell covered in tubes in a hospital bed in a state of extreme distress. It turned out to be an AI-generated fake."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/with-eu-backing-quantumdiamonds-aims-to-speed-up-chip-manufacturing/",
    "domain": "大厂 AI 动态",
    "title": "With EU backing, QuantumDiamonds aims to speed up chip manufacturing",
    "url": "https://techcrunch.com/2026/07/08/with-eu-backing-quantumdiamonds-aims-to-speed-up-chip-manufacturing/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T20:29:50+00:00",
    "summary": "Like its U.S. counterpart, the European Chips Act aims to foster the semiconductor industry — in part thanks to state subsidies. One of the beneficiaries is QuantumDiamonds, a German startup that appl"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/autonomous-drone-delivery-startup-manna-plots-major-u-s-expansion/",
    "domain": "大厂 AI 动态",
    "title": "Autonomous drone delivery startup Manna plots major US expansion",
    "url": "https://techcrunch.com/2026/07/08/autonomous-drone-delivery-startup-manna-plots-major-u-s-expansion/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T20:06:54+00:00",
    "summary": "Manna is launching a U.S. operations and manufacturing facility in Tulsa, Oklahoma, that will eventually employ 1,000 people."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/",
    "domain": "大厂 AI 动态",
    "title": "SpaceXAI releases Grok 4.5, which Elon describes as an ‘Opus-class model’",
    "url": "https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T19:30:16+00:00",
    "summary": "Elon Musk's tech company released the newest version of Grok on Wednesday, promising a cheaper, more efficient alternative to other powerful AI models."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/slow-cial-app-roost-forces-you-to-slow-down-to-the-speed-of-a-carrier-pigeon/",
    "domain": "大厂 AI 动态",
    "title": "‘Slow-cial’ app Roost forces you to slow down to the speed of a carrier pigeon",
    "url": "https://techcrunch.com/2026/07/08/slow-cial-app-roost-forces-you-to-slow-down-to-the-speed-of-a-carrier-pigeon/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T19:22:11+00:00",
    "summary": "This developer didn't expect his side project to grow to 300,000 users, but people love Roost because it's an alternative to an always-on, fast-paced online culture."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/this-startup-thinks-robotics-is-about-to-have-its-chatgpt-moment/",
    "domain": "大厂 AI 动态",
    "title": "This startup thinks robotics is about to have its ChatGPT moment",
    "url": "https://techcrunch.com/2026/07/08/this-startup-thinks-robotics-is-about-to-have-its-chatgpt-moment/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T19:19:15+00:00",
    "summary": "General Intuition is betting millions of hours of video game data can train the foundation models for physical AI, making it easier to build smarter robots with minimal real-world data."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/elon-musk-says-x-will-send-dms-when-posts-youve-engaged-with-are-corrected/",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk says X will send DMs when posts you’ve engaged with are corrected",
    "url": "https://techcrunch.com/2026/07/08/elon-musk-says-x-will-send-dms-when-posts-youve-engaged-with-are-corrected/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T18:46:20+00:00",
    "summary": "X plans to send users direct messages when posts they’ve liked, replied to, or reposted receive Community Notes, an update aimed at addressing criticism that the platform’s crowdsourced fact-checking "
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/google-photos-adds-a-new-ai-video-remix-tool/",
    "domain": "大厂 AI 动态",
    "title": "Google Photos adds a new AI ‘Video Remix’ tool",
    "url": "https://techcrunch.com/2026/07/08/google-photos-adds-a-new-ai-video-remix-tool/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T18:30:08+00:00",
    "summary": "The feature can do things like apply cinematic relighting to brighten up a dark clip, swap out a plain background for something fun, or add artistic styles to videos."
  },
  {
    "id": "rss:https://techcrunch.com/video/why-this-ceo-thinks-video-games-make-better-training-data-than-the-internet/",
    "domain": "大厂 AI 动态",
    "title": "Why this CEO thinks video games make better training data than the internet",
    "url": "https://techcrunch.com/video/why-this-ceo-thinks-video-games-make-better-training-data-than-the-internet/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T17:47:55+00:00",
    "summary": "When it comes to achieving artificial general intelligence (AGI), large language models just&#160;don’t&#160;have what it takes. Models like ChatGPT and Claude&#160;are great at text, but&#160;they&#8"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/meta-wants-its-ai-glasses-to-seem-less-creepy-its-ai-strategy-says-otherwise/",
    "domain": "大厂 AI 动态",
    "title": "Meta wants its AI glasses to seem less creepy. Its AI strategy says otherwise.",
    "url": "https://techcrunch.com/2026/07/08/meta-wants-its-ai-glasses-to-seem-less-creepy-its-ai-strategy-says-otherwise/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T17:11:18+00:00",
    "summary": "Meta is adding a new safeguard to stop people from secretly recording others with its AI glasses. But the update comes as the company continues to expand how much personal data its AI products collect"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/openai-releases-new-voice-models-for-more-natural-live-conversations/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI releases new voice models for more natural live conversations",
    "url": "https://techcrunch.com/2026/07/08/openai-releases-new-voice-models-for-more-natural-live-conversations/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T17:00:00+00:00",
    "summary": "OpenAI says its new voice mode can speak and listen at the same time, a key ability for live translation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/crypto-vc-firm-paradigm-raises-1-2b-to-invest-in-technical-frontier-startups/",
    "domain": "大厂 AI 动态",
    "title": "Crypto VC firm Paradigm raises $1.2B to invest in ‘technical frontier’ startups",
    "url": "https://techcrunch.com/2026/07/08/crypto-vc-firm-paradigm-raises-1-2b-to-invest-in-technical-frontier-startups/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T16:29:35+00:00",
    "summary": "For Paradigm, the technical frontier will stretch beyond its cryptocurrency investment roots. This fund is expected to expand its investment focus to include robotics and AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/prime-intellect-raises-130m-series-a-to-help-enterprises-build-their-own-ai-agents/",
    "domain": "大厂 AI 动态",
    "title": "Prime Intellect raises $130M Series A to help enterprises build their own AI agents",
    "url": "https://techcrunch.com/2026/07/08/prime-intellect-raises-130m-series-a-to-help-enterprises-build-their-own-ai-agents/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T16:22:38+00:00",
    "summary": "Founded in 2024, Prime Intellect’s goal is to give organizations capabilities to train their own agentic systems without relying on frontier AI labs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/another-massive-data-breach-exposed-millions-of-drivers-license-numbers/",
    "domain": "大厂 AI 动态",
    "title": "Another massive data breach exposed millions of driver’s license numbers",
    "url": "https://techcrunch.com/2026/07/08/another-massive-data-breach-exposed-millions-of-drivers-license-numbers/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T16:14:49+00:00",
    "summary": "The cyberattack targeting a U.S. insurance giant is the largest known breach of driver's license numbers so far in 2026."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/these-ai-startups-are-growing-revenue-at-faster-and-faster-rates/",
    "domain": "大厂 AI 动态",
    "title": "These AI startups are growing revenue at faster and faster rates",
    "url": "https://techcrunch.com/2026/07/08/these-ai-startups-are-growing-revenue-at-faster-and-faster-rates/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T15:41:06+00:00",
    "summary": "There are a lot of fast-growing AI startups, but some are growing even faster, they say."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/08/solo-gp-ashley-smith-announces-25m-close-of-second-fund/",
    "domain": "大厂 AI 动态",
    "title": "Solo GP Ashley Smith announces second $25M fund to back startups in AI, security and more",
    "url": "https://techcrunch.com/2026/07/08/solo-gp-ashley-smith-announces-25m-close-of-second-fund/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T15:00:00+00:00",
    "summary": "Vermilion Cliffs Ventures announced Wednesday the close of a $25 million Fund II."
  },
  {
    "id": "rss:https://stratechery.com/2026/xbox-cuts-bundling-and-the-internet-solvent-transaction-coordination-and-sunk-costs/",
    "domain": "大厂 AI 动态",
    "title": "XBOX Cuts; Bundling and the Internet Solvent; Transaction, Coordination, and Sunk Costs",
    "url": "https://stratechery.com/2026/xbox-cuts-bundling-and-the-internet-solvent-transaction-coordination-and-sunk-costs/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T10:00:00+00:00",
    "summary": "Microsoft's Xbox division is conducting big layoffs, as the company deals with abject failure of its Game Pass strategy."
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
    "id": "rss:https://arstechnica.com/ai/2026/07/we-cannot-choose-to-become-idiots-the-ai-cheating-scandal-roiling-brown-university/",
    "domain": "大厂 AI 动态",
    "title": "Suspecting AI cheating, Ivy League prof ordered an in-person final; scores fell 50%",
    "url": "https://arstechnica.com/ai/2026/07/we-cannot-choose-to-become-idiots-the-ai-cheating-scandal-roiling-brown-university/",
    "source": "Nate Anderson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T21:42:44+00:00",
    "summary": "AI cheating leads to \"a failed society,\" professor says."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/lawsuit-grok-user-made-7k-child-sex-images-xai-only-reported-one-gang-rape-prompt/",
    "domain": "大厂 AI 动态",
    "title": "Lawsuit: Man used Grok to make 7K sex images of stepdaughter, then shot himself",
    "url": "https://arstechnica.com/tech-policy/2026/07/lawsuit-grok-user-made-7k-child-sex-images-xai-only-reported-one-gang-rape-prompt/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T19:56:37+00:00",
    "summary": "More young girls sue X over Grok CSAM; X accused of shielding child predators."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/new-york-can-restrict-sports-gambling-on-prediction-markets-us-judge-rules/",
    "domain": "大厂 AI 动态",
    "title": "Judge rejects Kalshi attempt to override New York state gambling laws",
    "url": "https://arstechnica.com/tech-policy/2026/07/new-york-can-restrict-sports-gambling-on-prediction-markets-us-judge-rules/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T19:14:02+00:00",
    "summary": "Kalshi tried to ignore gambling laws on its prediction market, NY governor says."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/07/high-severity-guest-vm-escape-is-1-of-2-linux-vulnerabilities-to-surface-this-week/",
    "domain": "大厂 AI 动态",
    "title": "Google pays $250K for Linux vulnerability allowing guest VM escapes",
    "url": "https://arstechnica.com/security/2026/07/high-severity-guest-vm-escape-is-1-of-2-linux-vulnerabilities-to-surface-this-week/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T19:01:19+00:00",
    "summary": "Both vulnerabilities allow untrusted users to gain root privileges."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/thousands-of-routers-bricked-after-government-program-concludes-in-australia/",
    "domain": "大厂 AI 动态",
    "title": "Aussie gov't tells volunteers to throw out thousands of functioning test routers",
    "url": "https://arstechnica.com/gadgets/2026/07/thousands-of-routers-bricked-after-government-program-concludes-in-australia/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T18:10:16+00:00",
    "summary": "But the devices could \"easily be reflashed.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/how-much-control-do-tiktok-users-really-have-over-fyps/",
    "domain": "大厂 AI 动态",
    "title": "TikTok users don't have as much agency over their FYPs as they think",
    "url": "https://arstechnica.com/science/2026/07/how-much-control-do-tiktok-users-really-have-over-fyps/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T18:00:49+00:00",
    "summary": "The \"not interested\" feature is your friend, but users must intentionally and constantly curate their FYPs"
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/us-seeks-cheaper-hunter-killer-drones-after-iran-destroys-1b-worth-of-reapers/",
    "domain": "大厂 AI 动态",
    "title": "US seeks cheaper hunter-killer drones after Iran destroys $1B worth of Reapers",
    "url": "https://arstechnica.com/gadgets/2026/07/us-seeks-cheaper-hunter-killer-drones-after-iran-destroys-1b-worth-of-reapers/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T17:44:54+00:00",
    "summary": "US military drone losses in Iran war spur Pentagon call for cheap replacements."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/miami-based-city-labs-achieves-a-first-for-commercial-nuclear-power-in-space/",
    "domain": "大厂 AI 动态",
    "title": "Miami-based City Labs achieves a first for commercial nuclear power in space",
    "url": "https://arstechnica.com/space/2026/07/miami-based-city-labs-achieves-a-first-for-commercial-nuclear-power-in-space/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T17:26:44+00:00",
    "summary": "\"The BOHR mission serves as a pathfinder for future nuclear-powered spacecraft.\""
  },
  {
    "id": "rss:https://arstechnica.com/google/2026/07/google-revamps-android-ai-dev-benchmark-adds-fable-5-and-other-agents/",
    "domain": "大厂 AI 动态",
    "title": "Google updates Android Bench with new LLMs, but Gemini still lags behind",
    "url": "https://arstechnica.com/google/2026/07/google-revamps-android-ai-dev-benchmark-adds-fable-5-and-other-agents/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T16:39:48+00:00",
    "summary": "Android Bench is evolving, and developers can help guide that process."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/07/two-teens-learn-the-hard-way-not-to-do-toy-gun-drivebys-from-a-waymo/",
    "domain": "大厂 AI 动态",
    "title": "Two teens learn the hard way not to do toy gun drive-bys from a Waymo",
    "url": "https://arstechnica.com/cars/2026/07/two-teens-learn-the-hard-way-not-to-do-toy-gun-drivebys-from-a-waymo/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T15:40:44+00:00",
    "summary": "The robotaxi stopped, called 911, and waited for the San Mateo Police to show up."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/newly-installed-monitoring-system-watched-the-seafloor-spread/",
    "domain": "大厂 AI 动态",
    "title": "Ocean rift zone saw spreading happen in a sudden burst",
    "url": "https://arstechnica.com/science/2026/07/newly-installed-monitoring-system-watched-the-seafloor-spread/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T15:09:38+00:00",
    "summary": "The crust expands at mid-ocean rifts. But how?"
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/us-rare-earths-flow-to-asia-as-domestic-demand-is-slow-to-emerge/",
    "domain": "大厂 AI 动态",
    "title": "US rare earths flow to Asia as domestic demand is slow to emerge",
    "url": "https://arstechnica.com/science/2026/07/us-rare-earths-flow-to-asia-as-domestic-demand-is-slow-to-emerge/",
    "source": "Camilla Hodgson in London",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T13:26:10+00:00",
    "summary": "Miners backed by Trump admin sell to Japan, South Korea despite push to develop domestic supply chain."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/blue-origin-for-the-first-time-is-expected-to-raise-private-capital/",
    "domain": "大厂 AI 动态",
    "title": "Blue Origin, for the first time, is expected to raise private capital",
    "url": "https://arstechnica.com/space/2026/07/blue-origin-for-the-first-time-is-expected-to-raise-private-capital/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T12:47:35+00:00",
    "summary": "The company is raising $10 billion, leading to a valuation of $130 billion."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/07/hackers-can-use-9-of-the-most-popular-ai-tools-to-assemble-massive-botnets/",
    "domain": "大厂 AI 动态",
    "title": "Hackers can use 9 of the most popular AI tools to assemble massive botnets",
    "url": "https://arstechnica.com/security/2026/07/hackers-can-use-9-of-the-most-popular-ai-tools-to-assemble-massive-botnets/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-08T07:00:51+00:00",
    "summary": "\"HalluSquatting\" weaponizes LLMs' inability to say \"I don't know.\""
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
    "id": "wscn:3776547",
    "domain": "股票",
    "title": "韩国加息靴子或下周落地，“走熊”的韩股还扛得住吗？",
    "url": "https://wallstreetcn.com/articles/3776547",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T06:32:57+00:00",
    "summary": "市场普遍预期，16日召开的韩国央行金融货币委员会会议将宣布加息，这将是自2021年8月以来的首次上调。外资狂抛、杠杆ETF反噬，三重危机引爆“半导体悖论”——巨头业绩狂飙反遭血洗。紧缩周期压顶，韩国资本市场正迎棘手的生死大考。"
  },
  {
    "id": "wscn:3776548",
    "domain": "股票",
    "title": "拐点已至！长鑫IPO或引爆国产半导体Capex新周期",
    "url": "https://wallstreetcn.com/articles/3776548",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T06:25:01+00:00",
    "summary": "国联民生证券认为，长鑫科技IPO获通关，拟募资295亿元扩产升级，成为国产链订单兑现的催化剂。扩产潮将沿“设备、零部件、材料”三级梯队轮动释放：前道刻蚀与薄膜沉积设备最先受益，核心零部件接力放量，后周期的材料耗材则随产线投片爬坡持续兑现。"
  },
  {
    "id": "wscn:3776543",
    "domain": "股票",
    "title": "霍尔木兹海峡重回战时，油市的担忧已不只是断供",
    "url": "https://wallstreetcn.com/articles/3776543",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T06:24:41+00:00",
    "summary": "布伦特原油与WTI双双飙至两周高位，美国汽油库存较五年均值低6%、柴油缺口高达12%。分析师警告，即使不出现持续性的实物供应中断，船舶安全、保险成本、潜在延误以及进一步报复风险的不确定性，近期内将持续推高市场波动率。"
  },
  {
    "id": "wscn:3776461",
    "domain": "股票",
    "title": "油价跌太快，美债却不信：市场正在错配两种风险",
    "url": "https://wallstreetcn.com/premium/articles/3776461?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T06:07:55+00:00",
    "summary": "油价急跌实为浮仓释放的过剩假象，美债利率坚挺则定价冲突成本，两大错位或将通过剧烈波动来修复。"
  },
  {
    "id": "wscn:3776545",
    "domain": "股票",
    "title": "马斯克Grok重回牌桌！新模型性能追平Opus更快还更省，Token直接砍到1/4",
    "url": "https://wallstreetcn.com/articles/3776545",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T06:06:37+00:00",
    "summary": "xAI联合Cursor发布旗舰模型Grok 4.5，1.5T参数规模是前代3倍，编程能力直追Claude Opus，推理速度高达80 TPS，API价格却比对手便宜60%以上。更关键的是，推理优化软件尚未上线，速度还有望再度翻倍。这场AI工程战，Grok正式重回牌桌。"
  },
  {
    "id": "wscn:3776526",
    "domain": "股票",
    "title": "创业板涨3%，科创50狂飙6%，算力硬件、芯片半导体爆发，恒科指震荡下跌，智谱涨5%、MINIMAX大跌20%",
    "url": "https://wallstreetcn.com/articles/3776526",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T05:52:46+00:00",
    "summary": "盘面上，个股呈现普跌态势，沪深京三市约4600股飘绿，上午半天成交1.71万亿。沪深两市半日成交额1.7万亿，较上个交易日几乎持平。板块方面，稀土、锂电池产业链跌幅居前，基本金属、钢铁、石油化工板块低迷；半导体产业链爆发，GPU、半导体硅片、内存、先进封装方向领涨。"
  },
  {
    "id": "wscn:3776523",
    "domain": "股票",
    "title": "芯片股重燃，日股涨近2%，韩股再跳水转跌，债市全线承压",
    "url": "https://wallstreetcn.com/articles/3776523",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T05:38:19+00:00",
    "summary": "韩国KOSPI指数早盘一度涨超4%，三星电子涨约4%，SK海力士涨逾9%。但盘中KOSPI指数跳水翻绿，截至发稿跌0.88%。SK海力士美股上市超额认购逾7倍，成为本轮行情的核心催化剂。美伊紧张局势升级，布伦特原油三连涨突破每桶79美元，通胀担忧重燃。"
  },
  {
    "id": "wscn:3776270",
    "domain": "股票",
    "title": "2026量产元年启幕：人形机器人如何成为中美科技竞速新高地？",
    "url": "https://wallstreetcn.com/premium/articles/3776270?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T05:38:18+00:00",
    "summary": "量产元年开启，人形机器人从实验室走向万亿市场。"
  },
  {
    "id": "wscn:3776533",
    "domain": "股票",
    "title": "马斯克“抄了”智谱",
    "url": "https://wallstreetcn.com/articles/3776533",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:19:29+00:00",
    "summary": "马斯克表示Grok 4.5速度更快、token效率更高，是\"Opus级\"模型。这一低价策略被市场观察人士认为与中国开源厂商（如智谱GLM-5.2）的性价比路线高度吻合，令Anthropic等高定价闭源模型承压。同时，xAI收购Cursor被认为旨在获取真实编程数据，构建飞轮效应，以争夺编程代理市场份额。"
  },
  {
    "id": "wscn:3776531",
    "domain": "股票",
    "title": "乌克兰无人机打穿俄能源防线？十大炼油厂九家遇袭，俄罗斯宣布实施柴油出口禁令",
    "url": "https://wallstreetcn.com/articles/3776531",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:03:50+00:00",
    "summary": "乌克兰无人机持续打击俄罗斯能源基础设施危及俄能源生产，6月原油加工量创20年新低，超半数联邦主体实施燃油限购，部分加油站排队时间长达18小时。普京紧急召开视频会议，宣布实施柴油出口禁令，并承认存在“一定程度的燃料短缺”，燃油危机或持续至9月。"
  },
  {
    "id": "wscn:3776537",
    "domain": "股票",
    "title": "美伊停火over，会是美元最后一涨吗？",
    "url": "https://wallstreetcn.com/articles/3776537",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:03:45+00:00",
    "summary": "本次美伊备忘录核限制模糊、筹码倒置，美国几乎一无所获——掀桌子不过是特朗普以打促谈的惯常操作。后市来看，从利差、贸易条件和避险情绪观察，美元指数在当前时间点同时受到三方面支撑，但不至于支持美元指数向上突破102关口。决定美元指数下一步走势的更重要因素，是下周二公布的美国6月CPI。"
  },
  {
    "id": "wscn:3776532",
    "domain": "股票",
    "title": "贝恩资本清仓铠侠！10年前“困境资产”接盘，“存储狂潮”造就史诗级回报",
    "url": "https://wallstreetcn.com/articles/3776532",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T03:31:14+00:00",
    "summary": "贝恩资本正式清仓铠侠控股，为这笔历时近十年的投资画上完美句点。从接盘东芝困境资产，到借AI存储需求浪潮一飞冲天，自2024年上市以来铠侠股价较发行价累计暴涨逾4800%，贝恩斩获创纪录回报，跻身私募股权史上最耀眼成功案例之列。"
  },
  {
    "id": "wscn:3776538",
    "domain": "股票",
    "title": "MiniMax冲刺2.7万亿参数大模型：算力、开源与回A窗口共振",
    "url": "https://wallstreetcn.com/articles/3776538",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T03:26:09+00:00",
    "summary": "一、MiniMax被曝推进2.7万亿参数模型，中国开源大模型进入更大规模竞争据科技媒体The Inf..."
  },
  {
    "id": "wscn:3776535",
    "domain": "股票",
    "title": "阿维塔迈过一个新台阶",
    "url": "https://wallstreetcn.com/articles/3776535",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T03:19:58+00:00",
    "summary": "闯关。"
  },
  {
    "id": "wscn:3776534",
    "domain": "股票",
    "title": "上海银行重算区域账",
    "url": "https://wallstreetcn.com/articles/3776534",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T03:17:32+00:00",
    "summary": "上海银行旗下村镇银行的出清仍在继续。\n7月初，上海银行在上海联合产权交易所挂牌，拟转让所持崇州上银村..."
  },
  {
    "id": "wscn:3776518",
    "domain": "股票",
    "title": "PE倍数创本轮AI牛市以来最低！美银称英伟达“估值不合理”",
    "url": "https://wallstreetcn.com/articles/3776518",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T03:01:58+00:00",
    "summary": "美银认为，英伟达今年股价仅涨3%，远落后于费城半导体指数82%的涨幅，估值存在\"不合理折价\"。当前远期市盈率跌至7年最低（约18倍），隐含市场对其2027/2028年EPS高达30-35%的下行预期，而美银认为此假设站不住脚。市场过度担忧内存成本与ASIC竞争，却低估了英伟达定价权与护城河。"
  },
  {
    "id": "wscn:3776527",
    "domain": "股票",
    "title": "动量崩塌、韩股巨震，量化基金面临2025年8月以来最惨回撤！",
    "url": "https://wallstreetcn.com/articles/3776527",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T03:01:33+00:00",
    "summary": "量化多空策略基金自6月22日起两周内累计下跌3.6%，创2025年以来最大回撤，年内收益率从14.4%降至10.8%。损失主要集中于空头端，基本面基金因提前削减AI敞口，跌幅相对较小。高盛将此归因于市场剧烈轮动与动量交易崩塌。当前市场关注基金群体是否会重新加杠杆追逐动量，其选择将决定下阶段风险走向。"
  },
  {
    "id": "wscn:3776528",
    "domain": "股票",
    "title": "\"迷你效应\"席卷美国零售：高通胀重压下，小商品成消费市场新引擎",
    "url": "https://wallstreetcn.com/articles/3776528",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T03:00:45+00:00",
    "summary": "工资增长乏力、通胀高企之下，美国消费者正掀起一场\"迷你消费\"浪潮。Lowe's、Trader Joe's等零售商争相推出小尺寸产品，以低风险小额满足感替代大额支出。这一\"迷你效应\"不仅带动整体客单价提升，更折射出美国消费心理的根本性转变：越是动荡，越求低风险。"
  },
  {
    "id": "wscn:3776529",
    "domain": "股票",
    "title": "花旗实体AI峰会：数据稀缺、成本高企，机器人规模化“是十年长跑”",
    "url": "https://wallstreetcn.com/articles/3776529",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T02:59:43+00:00",
    "summary": "花旗年度实体AI峰会显示，机器人行业正从概念走向落地，但规模化远比数字AI更慢、更重。核心瓶颈是数据——2026年全行业数千万小时的数据积累，仍仅是最终所需量的“基点级别”。过去两年全球实体AI投资约200亿美元，该行判断这是“十年长跑”，胜出者是掌握专有数据、采用RaaS模式、聚焦真实劳动力痛点的企业。"
  },
  {
    "id": "wscn:3776530",
    "domain": "股票",
    "title": "李维斯第二财季净利达8730万美元，DTC业务占比首超五成",
    "url": "https://wallstreetcn.com/articles/3776530",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T02:40:19+00:00",
    "summary": "亚洲市场增长领跑各区域。"
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
    "id": "rss:https://arxiv.org/abs/2607.06702",
    "domain": "金融",
    "title": "Dynamic Causal Portfolio Choice: Hedging the Rotation of the Common-Driver Manifold",
    "url": "https://arxiv.org/abs/2607.06702",
    "source": "Alejandro Rodriguez Dominguez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2607.06702v1 Announce Type: new Abstract: When a portfolio is conditioned on a minimal set of observable drivers under which its assets become mutually independent over the investment horizon, t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.06908",
    "domain": "金融",
    "title": "Iterative detection of global factors near the BBP phase transition",
    "url": "https://arxiv.org/abs/2607.06908",
    "source": "Andr\\'es Garc\\'ia-Medina",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2607.06908v1 Announce Type: new Abstract: Detecting the number of global factors in high-dimensional correlation matrices is a central problem in multivariate statistics and random matrix theory"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.07055",
    "domain": "金融",
    "title": "Identifying the MPC-Liquidity Gradient in High-Quality Data",
    "url": "https://arxiv.org/abs/2607.07055",
    "source": "Mikael Carlsson, Marco D'Amico, Erik \\\"Oberg, Oskar N. Skans, Karl Walentin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2607.07055v1 Announce Type: new Abstract: We estimate the gradient of the Marginal Propensity to Consume (MPC) with respect to liquidity using a new estimator designed for administrative data wi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.07207",
    "domain": "金融",
    "title": "Memory Scarcity, Open Models, and the Restructuring of the AI Industry, 2026-2030 -- A quantitative scenario analysis of inference economics, training-cost divergence, and infrastructure solvency",
    "url": "https://arxiv.org/abs/2607.07207",
    "source": "Satoshi Matsuoka",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2607.07207v1 Announce Type: new Abstract: We analyze how four forces restructure the AI industry over 2026-2030: the DRAM/HBM price surge, frontier-capable open-weight models (GLM-5.2), rapid in"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.07353",
    "domain": "金融",
    "title": "The Joneses Visit an Economics Lab",
    "url": "https://arxiv.org/abs/2607.07353",
    "source": "Mikhail Freer, Daniel Friedman, Christian Ghiglino, Elke Weidenholzer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2607.07353v1 Announce Type: new Abstract: Existing literature offers persuasive evidence that individuals care about how their consumption compares to that of peers, and proposes a large variety"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.07465",
    "domain": "金融",
    "title": "Innovating Risk Modelling for Global Funds",
    "url": "https://arxiv.org/abs/2607.07465",
    "source": "Swaraj Gambhir, Thanu George, Kairavi Sivasankar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2607.07465v1 Announce Type: new Abstract: Markowitz defined portfolio risk as an internal property, built from the covariance among a book's own holdings rather than the distance to any index. S"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.07655",
    "domain": "金融",
    "title": "Robustness to Model Uncertainties Drives More Rapid CO2 Emissions Reductions",
    "url": "https://arxiv.org/abs/2607.07655",
    "source": "Lisa Rennels, Frank Errickson, David Smith, Bryan Parthum, Klaus Keller, David Anthoff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2607.07655v1 Announce Type: new Abstract: Evaluating the economic impacts of climate policies is important for designing a response to climate change. One typical approach to assessing mitigatio"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.06690",
    "domain": "金融",
    "title": "tsbootstrap: Distribution-Free Uncertainty Quantification and Conformal Prediction for Time Series",
    "url": "https://arxiv.org/abs/2607.06690",
    "source": "Sankalp Gilda",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2607.06690v1 Announce Type: cross Abstract: Finance, sensing, and demand streams violate the exchangeability that IID conformal prediction and the IID bootstrap assume, and existing libraries im"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.06806",
    "domain": "金融",
    "title": "Will AstroForge Collapse the PGM Market?",
    "url": "https://arxiv.org/abs/2607.06806",
    "source": "Robert T. Nachtrieb, Steven J. Smith",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2607.06806v1 Announce Type: cross Abstract: AstroForge seeks to mine platinum group metals (PGM) from asteroids. Asteroid reserves appear to be unlimited, and at current market price the gross m"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.07315",
    "domain": "金融",
    "title": "Thermodynamic description of worldwide distribution of energy and carbon emission",
    "url": "https://arxiv.org/abs/2607.07315",
    "source": "Klaus M. Frahm, Dima L. Shepelyansky",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2607.07315v1 Announce Type: cross Abstract: Based on public data, we analyze the distributions of energy and carbon emission over world countries on a scale of the last 40-50 years using their p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.07652",
    "domain": "金融",
    "title": "Answering Without Referring: How AI Search Rewrites the Web's Economic Bargain",
    "url": "https://arxiv.org/abs/2607.07652",
    "source": "Qiaoni Shi, Kai Zhu, Kai Gu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2607.07652v1 Announce Type: cross Abstract: Search engines have long allocated attention on the web by routing users from queries to websites. AI search changes this arrangement because informat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.01365",
    "domain": "金融",
    "title": "Consumption Stimulus with Digital Coupons: Heterogeneity and Policy Design",
    "url": "https://arxiv.org/abs/2507.01365",
    "source": "Ying Chen, Mingyi Li, Jiaming Mao, Jingyi Zhou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2507.01365v2 Announce Type: replace Abstract: We study consumption stimulus using digital coupons, which provide time-limited subsidies contingent on minimum spending. Analyzing a large-scale pr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.00554",
    "domain": "金融",
    "title": "ContestTrade: A Multi-Agent Trading System Based on Internal Contest Mechanism",
    "url": "https://arxiv.org/abs/2508.00554",
    "source": "Rui Sun, Li Zhao, Zuoyou Jiang, Bo Yang, Yuxiao Bai, Mengting Chen, Jing Li, Zuo Bai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2508.00554v4 Announce Type: replace Abstract: In financial trading, large language model (LLM)-based agents demonstrate significant potential, but their decisions can be sensitive to noisy and n"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.12315",
    "domain": "金融",
    "title": "Deciphering the global production network from cross-border firm transactions",
    "url": "https://arxiv.org/abs/2508.12315",
    "source": "Neave O'Clery, Ben Radcliffe-Brown, Thomas Spencer, Daniel Tarling-Hunter",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2508.12315v4 Announce Type: replace Abstract: Critical for policy-making and business operations, the study of global supply chains has been severely hampered by a lack of detailed data. Here we"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.15355",
    "domain": "金融",
    "title": "Time-consistent catastrophe risk management under the path-dependent effects",
    "url": "https://arxiv.org/abs/2508.15355",
    "source": "Liyuan Cui, Wenyuan Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2508.15355v3 Announce Type: replace Abstract: This paper investigates optimal investment and insurance strategies under a mean-variance criterion with path-dependent effects. We use a rough vola"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.08366",
    "domain": "金融",
    "title": "A data fusion approach for mobility hub impact assessment and location selection: integrating hub usage data into a large-scale mode choice model",
    "url": "https://arxiv.org/abs/2510.08366",
    "source": "Xiyuan Ren, Joseph Y. J. Chow",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2510.08366v2 Announce Type: replace Abstract: As cities grapple with traffic congestion and service inequities, mobility hubs offer a scalable solution to align increasing travel demand with sus"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.00874",
    "domain": "金融",
    "title": "Conditional Disclosure as a Coordination Device",
    "url": "https://arxiv.org/abs/2604.00874",
    "source": "Matthew Cashman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2604.00874v2 Announce Type: replace Abstract: Social assurance contracts are private commitments to go public with a controversial view only when the coalition is big enough to be self-protectin"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.02126",
    "domain": "金融",
    "title": "Hedging market risk and uncertainty via a robust portfolio approach",
    "url": "https://arxiv.org/abs/2604.02126",
    "source": "Adele Ravagnani, Mattia Chiappari, Andrea Flori, Piero Mazzarisi, Marco Patacca",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2604.02126v2 Announce Type: replace Abstract: Shorting for hedging exposes to risk when the market dynamics is uncertain. Managing uncertainty and risk exposure is key in portfolio management pr"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.10492",
    "domain": "金融",
    "title": "Aharanov-Bohm Type Arbitrage and Homological Obstructions in Financial Markets",
    "url": "https://arxiv.org/abs/2604.10492",
    "source": "Takanori Adachi, Keisuke Hara",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2604.10492v5 Announce Type: replace Abstract: We introduce a simplicial and categorical formulation of Aharonov--Bohm (AB) type arbitrage in filtered market systems. Given a filtration modeled a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.24309",
    "domain": "金融",
    "title": "Randomized Neural Networks for estimation of exposure profiles and Credit Valuation Adjustment (CVA) for American Equity Options",
    "url": "https://arxiv.org/abs/2606.24309",
    "source": "Isidro Moroso Varona, Jakub Micha\\'nk\\'ow, Pawe{\\l} Sakowski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2606.24309v2 Announce Type: replace Abstract: This paper studies the use of randomized neural networks for the estimation of exposure profiles and unilateral CVA of American options within a Mon"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.18644",
    "domain": "金融",
    "title": "Digital Euro: Frequently Asked Questions Revisited",
    "url": "https://arxiv.org/abs/2601.18644",
    "source": "Joe Cannataci, Benjamin Fehrensen, Mikolai G\\\"utschow, \\\"Ozg\\\"ur Kesim, Bernd Lucke",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2601.18644v2 Announce Type: replace-cross Abstract: The European Central Bank (ECB) is working on the \"digital euro\", an envisioned retail central bank digital currency for the Euro area. In thi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.18044",
    "domain": "金融",
    "title": "Norm-Relevant Messages under Uncertainty",
    "url": "https://arxiv.org/abs/2604.18044",
    "source": "Senran Lin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2604.18044v3 Announce Type: replace-cross Abstract: Social-information messages are widely used to influence norm perceptions and norm-relevant behavior, but their effects may depend on what the"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.29251",
    "domain": "金融",
    "title": "When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis",
    "url": "https://arxiv.org/abs/2606.29251",
    "source": "Hoyoung Lee, Suhwan Park, Seunghan Lee, Jun Seo, Jaehoon Lee, Sungdong Yoo, Minjae Kim, CheolWon Na, Zhangyang Wang, Zach Golkhou, Minkyu Kim, Sotirios Sabanis, Alejandro Lopez-Lira, Dhagash Mehta, Soonyoung Lee, Chanyeol Choi, Wonbin Ahn, Yongjae Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-09T04:00:00+00:00",
    "summary": "arXiv:2606.29251v2 Announce Type: replace-cross Abstract: Financial decision-makers face more information than they can directly inspect, making context compression necessary. Yet when large language "
  }
]
```
