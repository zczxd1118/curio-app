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

- 今日日期：`2026-07-17`
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
  "date": "2026-07-17",
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
    "points": 3788715,
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
    "points": 1526778,
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
    "points": 978777,
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
    "points": 941760,
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
    "points": 902452,
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
    "points": 880908,
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
    "points": 667893,
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
    "points": 534058,
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
    "points": 479533,
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
    "points": 384462,
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
    "points": 375454,
    "published_at": "2026-07-01T09:35:43+00:00",
    "summary": "Claude Code 封号原因终于找到了！国外开发者逆向 Claude Code 源码，发现 Anthropic 在客户端里藏了一套隐蔽的用户标记系统，这期视频带你完整还原封号真相。\n开源 AI 编程教程：github.com/liyupi/ai-guide\n编程学习教程+实战项目+简历模板：codefather.cn\n最近 AI 圈儿不太平啊，OpenAI Codex 封号、Cursor 地区"
  },
  {
    "id": "bvid:BV1GX9dYWEPw",
    "domain": "AI",
    "title": "我居然能在MC里玩到这么好玩的摸金服务器！",
    "url": "http://www.bilibili.com/video/av114108926068217",
    "source": "物骨",
    "platform": "bilibili",
    "points": 317606,
    "published_at": "2025-03-06T21:00:00+00:00",
    "summary": "视频内容均来自《LRL服务器》\n服务器游玩方式看评论区置顶\n无需正版，不卖数值，爆率嘎嘎高，不会跑路"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 269609,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 257744,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 239079,
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
    "points": 234514,
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
    "points": 189625,
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
    "points": 177287,
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
    "points": 161773,
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
    "points": 159862,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1WJjF67Eky",
    "domain": "AI",
    "title": "对Claude code上瘾了",
    "url": "http://www.bilibili.com/video/av116768819384530",
    "source": "小王很南",
    "platform": "bilibili",
    "points": 129997,
    "published_at": "2026-06-18T02:50:04+00:00",
    "summary": "我做的交互网站"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 129599,
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
    "points": 110745,
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
    "points": 92582,
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
    "points": 92152,
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
    "points": 88822,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73757,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53110,
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
    "points": 43010,
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
    "points": 38407,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 29400,
    "published_at": "2026-05-07T00:00:00+00:00",
    "summary": "全栈课一共分为6大块内容\n第一块：AI智能体开发基础(AI大模型、工具、记忆、MCP、中间件、Skills等核心内容)\n第二块：Claude Code,Trea+skills实现基于需求文档生成用例，基于OpenClaw实现接口自动化落地，基于hermes Agent实现web自动化落地\n第三块：功能测试的智能体开发(项目RAG知识库搭建+Agent搭建+skills开发，实现用例生成的Agent"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28779,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 27142,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1JU7E6PEar",
    "domain": "AI",
    "title": "Cursor 已死？我为什么要退订 Cursor ？",
    "url": "http://www.bilibili.com/video/av116819553683121",
    "source": "祥子在学AI",
    "platform": "bilibili",
    "points": 25991,
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
    "points": 22627,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 15295,
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
    "points": 14722,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 14583,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1yyQEBdEkm",
    "domain": "AI",
    "title": "【2026B站最全】Claude Code+软件测试实操教程!看完我直接删了收藏夹所有测试教程,从账号注册到Plan驱动测试项目,小白3天上手！",
    "url": "http://www.bilibili.com/video/av116408092525631",
    "source": "软件测试大神",
    "platform": "bilibili",
    "points": 14576,
    "published_at": "2026-04-15T09:55:02+00:00",
    "summary": "配套资料👉：https://b23.tv/qvhxmaQ\n包括:AI测试网站，几十个AI场景测试完整流程，skil文档，测试八股文，项目源码，测试用例模板，工具安装包，学习计划表，学习路线，100g测试新人资料包等等，资料百分百免费，放心领取~"
  },
  {
    "id": "bvid:BV1DPwGe1Ekf",
    "domain": "AI",
    "title": "Cursor从小白到专家-第15课：如何用Cursor+Dify搭建本地知识库？",
    "url": "http://www.bilibili.com/video/av113836698898908",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 14290,
    "published_at": "2025-01-16T08:55:00+00:00",
    "summary": "在第九课“如何用 cursor + coze 搭建线上知识库”的分享后，有一部分精神股东表示，想要本地知识库的搭建教程。\n.\n有求必应，今天第15课的分享就是“用 cursor + dify 搭建本地知识库”，手把手教会。我们第16课见 ~"
  },
  {
    "id": "bvid:BV14a4y1T7Cp",
    "domain": "AI",
    "title": "VS Code + CursorCode 插件，AI 帮你编写、调试代码",
    "url": "http://www.bilibili.com/video/av654787185",
    "source": "马隆工作室",
    "platform": "bilibili",
    "points": 14082,
    "published_at": "2023-04-11T11:48:41+00:00",
    "summary": "免费， VS Code + CursorCode 插件，AI 帮你编写、调试代码"
  },
  {
    "id": "bvid:BV1etEQ6DETs",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116724192118321",
    "source": "AI产品经理大模型",
    "platform": "bilibili",
    "points": 13985,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV15JdkYxEGg",
    "domain": "AI",
    "title": "MCP还不会配置？Cherry Studio软件MCP服务配置教程",
    "url": "http://www.bilibili.com/video/av114331324778025",
    "source": "去飞GoFly",
    "platform": "bilibili",
    "points": 9193,
    "published_at": "2025-04-14T02:30:00+00:00",
    "summary": "MCP服务网站：https://smithery.ai/\nCherry Studio官方网站：https://cherry-ai.com/"
  },
  {
    "id": "bvid:BV1ydNT61Ef4",
    "domain": "AI",
    "title": "【幻兽帕鲁】幻兽帕鲁1.0服务器（非ue4ss）/本地模组安装教程",
    "url": "http://www.bilibili.com/video/av116905352366251",
    "source": "SngZi",
    "platform": "bilibili",
    "points": 8787,
    "published_at": "2026-07-12T05:31:39+00:00",
    "summary": "本视频为幻兽帕鲁1.0版本模组安装教程，本视频中主要为steam创意工坊的模组安装，如果需要N网的请看下期。\n视频仅为个人观点，教程为个人研究所得，如有问题大家留言即可"
  },
  {
    "id": "bvid:BV18VQKBbEF7",
    "domain": "AI",
    "title": "详细讲解x64dbg配置MCP实现Ai自动化分析代码",
    "url": "http://www.bilibili.com/video/av116383765502158",
    "source": "流水线的王_",
    "platform": "bilibili",
    "points": 8772,
    "published_at": "2026-04-11T02:45:54+00:00",
    "summary": "x64dbg配置MCP，实现Ai自动化分析代码，详细讲解。"
  },
  {
    "id": "bvid:BV12MEg6pE9o",
    "domain": "AI",
    "title": "【乐鑫教程】乐鑫文档 MCP 服务器上线，现已支持微信登录！",
    "url": "http://www.bilibili.com/video/av116713957956440",
    "source": "乐鑫信息科技",
    "platform": "bilibili",
    "points": 7721,
    "published_at": "2026-06-08T10:17:31+00:00",
    "summary": "手把手教你如何使用最新乐鑫文档知识库，帮你在 Claude / Cursor 等平台解答问题、生成代码、迁移 ESP-IDF 版本、烧录固件。 MCP 服务器现已支持微信扫码一键登录，快来一试！\n\n视频重点内容包括👇：\n\n- 如何将 MCP 服务器添加到 VS Code\n- 让 Copilot 基于乐鑫文档对比旧版和最新版 I2C 驱动\n- 驱动迁移\n- Copilot 编译代码、烧录代码并监控输"
  },
  {
    "id": "bvid:BV1vLN769EJa",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Vibe Coding】教程！大模型入门到进阶，一套全解决！DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116894866677118",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 7064,
    "published_at": "2026-07-10T09:04:48+00:00",
    "summary": "【代码已整理】\n无论你是从零开始开发项目，还是对现有代码进行现代化改造，本课程都能为你提供一套严谨的工作流程，让你按自己的方式构建软件。"
  },
  {
    "id": "bvid:BV1u4G9zmEte",
    "domain": "AI",
    "title": "什么是MCP？VS Code中使用MCP Server",
    "url": "http://www.bilibili.com/video/av114426032168712",
    "source": "AI落地派",
    "platform": "bilibili",
    "points": 6548,
    "published_at": "2025-04-30T08:51:30+00:00",
    "summary": "什么是MCP，怎么样使用MCP Server，不用写SQL语句就可以查询数据库。\n\nMCP Servers\nhttps://smithery.ai/\nhttps://github.com/punkpeye/awesome-mcp-servers\nhttps://github.com/modelcontextprotocol/servers\n\nMCP Server for MySQL based o"
  },
  {
    "id": "bvid:BV1fNs9eiEm9",
    "domain": "AI",
    "title": "Cursor AI编程结合cocos3.8游戏开发教程-01",
    "url": "http://www.bilibili.com/video/av113187471105975",
    "source": "太阳8800",
    "platform": "bilibili",
    "points": 6536,
    "published_at": "2024-09-23T15:15:13+00:00",
    "summary": "开源源码仓库\nhttps://gitee.com/gamepublic/chess-cards"
  },
  {
    "id": "bvid:BV19XqMBzENU",
    "domain": "AI",
    "title": "Cursor + OpenCode 最佳开源 AI 编程工具",
    "url": "http://www.bilibili.com/video/av115851978146202",
    "source": "独立开发者_猫哥",
    "platform": "bilibili",
    "points": 6472,
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
    "points": 370,
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
    "points": 141,
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
    "id": "rss:https://www.eetimes.com/ai-data-centers-push-silicon-photonics-toward-300-mm-scale/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Data Centers Push Silicon Photonics Toward 300-mm Scale",
    "url": "https://www.eetimes.com/ai-data-centers-push-silicon-photonics-toward-300-mm-scale/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T14:00:00+00:00",
    "summary": "AI data centers are torching copper’s reign as ST pushes 300-mm silicon photonics for faster, denser optical links. The post AI Data Centers Push Silicon Photonics Toward 300-mm Scale appeared first o"
  },
  {
    "id": "rss:https://www.eetimes.com/india-adds-pieces-to-strengthen-its-electronics-supply-chain-puzzle/",
    "domain": "AI 算力 / 半导体",
    "title": "India Adds Pieces to Strengthen Its Electronics Supply Chain Puzzle",
    "url": "https://www.eetimes.com/india-adds-pieces-to-strengthen-its-electronics-supply-chain-puzzle/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T07:00:00+00:00",
    "summary": "India races to own more of its electronics value chain, from OSATs to PCBs, but imported materials still hold the leash. The post India Adds Pieces to Strengthen Its Electronics Supply Chain Puzzle ap"
  },
  {
    "id": "rss:https://www.eetimes.com/how-nidec-is-rethinking-gear-design-for-humanoid-and-mobile-robots/",
    "domain": "AI 算力 / 半导体",
    "title": "How Nidec Is Rethinking Gear Design for Humanoid and Mobile Robots",
    "url": "https://www.eetimes.com/how-nidec-is-rethinking-gear-design-for-humanoid-and-mobile-robots/",
    "source": "EE Times Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T21:06:44+00:00",
    "summary": "Nidec tackles the brutal gearbox tradeoffs behind humanoid robots, from zero backlash to lighter integrated actuators. The post How Nidec Is Rethinking Gear Design for Humanoid and Mobile Robots appea"
  },
  {
    "id": "rss:https://www.eetimes.com/tyl-semi-de-risks-chiplets-with-new-business-model/",
    "domain": "AI 算力 / 半导体",
    "title": "TYLsemi De-Risks Chiplets With New Business Model",
    "url": "https://www.eetimes.com/tyl-semi-de-risks-chiplets-with-new-business-model/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T19:00:00+00:00",
    "summary": "Startup TYLsemi wants to address the gap between ASIC houses and design services, taking on the risk of developing large chiplet-based chips for AI infrastructure customers. The post TYLsemi De-Risks "
  },
  {
    "id": "rss:https://www.eetimes.com/why-tl3228-is-the-go-to-standard-chip-powering-true-8k-wireless-gaming-peripherals/",
    "domain": "AI 算力 / 半导体",
    "title": "Why TL3228 Is the Go-To Standard Chip Powering True 8K Wireless Gaming Peripherals",
    "url": "https://www.eetimes.com/why-tl3228-is-the-go-to-standard-chip-powering-true-8k-wireless-gaming-peripherals/",
    "source": "Telink",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T13:00:00+00:00",
    "summary": "The TL3228 integrates a dual-core RISC-V processor consisting of a high-performance D25F core and an energy-efficient N22 core. The post Why TL3228 Is the Go-To Standard Chip Powering True 8K Wireless"
  },
  {
    "id": "rss:https://www.eetimes.com/massive-stock-full-chain-service-your-global-semiconductor-partner/",
    "domain": "AI 算力 / 半导体",
    "title": "Massive Stock, Full-Chain Service — Your Global Semiconductor Partner",
    "url": "https://www.eetimes.com/massive-stock-full-chain-service-your-global-semiconductor-partner/",
    "source": "NEW IDEAS INDUSTRIAL CO., LIMITED",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T13:00:00+00:00",
    "summary": "Discover how New Ideas Industrial can stabilize your semiconductor supply chain for AI, storage, and UAV applications. The post Massive Stock, Full-Chain Service — Your Global Semiconductor Partner ap"
  },
  {
    "id": "rss:https://www.eetimes.com/after-magdeburg-intel-builds-on-ireland-existing-strength/",
    "domain": "AI 算力 / 半导体",
    "title": "After Magdeburg, Intel Builds on Ireland’s Existing Strength",
    "url": "https://www.eetimes.com/after-magdeburg-intel-builds-on-ireland-existing-strength/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T11:24:18+00:00",
    "summary": "Leixlip cannot replace Magdeburg, but it shows the value of expanding where fabs, demand, and ecosystems already exist. The post After Magdeburg, Intel Builds on Ireland’s Existing Strength appeared f"
  },
  {
    "id": "rss:https://www.eetimes.com/probabilistic-computing-is-already-here-here-is-how-it-works/",
    "domain": "AI 算力 / 半导体",
    "title": "Probabilistic Computing Is Already Here; Here Is How It Works",
    "url": "https://www.eetimes.com/probabilistic-computing-is-already-here-here-is-how-it-works/",
    "source": "Phillip Stanley-Marbel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T07:21:54+00:00",
    "summary": "Probabilistic computing is addressing Monte Carlo bottlenecks, with UxHw hardware in use at Boeing and CERN. The post Probabilistic Computing Is Already Here; Here Is How It Works appeared first on EE"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/linus-torvalds-rebukes-anti-ai-stances-in-the-linux-kernel-code-review-process-says-linux-is-not-one-of-those-anti-ai-projects-creator-embraces-ai-as-just-a-tool-and-clearly-a-useful-one",
    "domain": "AI 算力 / 半导体",
    "title": "Linus Torvalds rebukes anti-AI stances in the Linux kernel code review process, says 'Linux is not one of those anti-AI projects' — creator embraces AI as just a tool and 'clearly a useful one'",
    "url": "https://www.tomshardware.com/software/linux/linus-torvalds-rebukes-anti-ai-stances-in-the-linux-kernel-code-review-process-says-linux-is-not-one-of-those-anti-ai-projects-creator-embraces-ai-as-just-a-tool-and-clearly-a-useful-one",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T16:59:13+00:00",
    "summary": "Linus Torvalds, Linux's creator and kernel manager, has seemingly taken an accepting stance of AI-assisted tooling."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/quantum-computing/neural-atom-quantum-computing-roadmap-how-laser-cooled-trapped-atoms-could-pave-the-path-beyond-physical-qubit-counts",
    "domain": "AI 算力 / 半导体",
    "title": "Neural atom quantum computing roadmap — how laser-cooled trapped atoms could pave the path beyond physical qubit counts",
    "url": "https://www.tomshardware.com/tech-industry/quantum-computing/neural-atom-quantum-computing-roadmap-how-laser-cooled-trapped-atoms-could-pave-the-path-beyond-physical-qubit-counts",
    "source": "Francisco Pires",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T16:52:54+00:00",
    "summary": "Neural Atom Quantum Computing is a rapidly accelerating part of the Quantum puzzle. Featuring software-defined configurable arrays, qubits can be physically moved mid-computation, and this roadmap hig"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-7700x3d-is-exclusive-to-newegg-in-north-america-usd329-cpu-wont-be-available-at-other-vendors-until-at-least-q4",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen 7 7700X3D is exclusive to Newegg in North America — $329 CPU won't be available at other vendors until at least Q4",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-7700x3d-is-exclusive-to-newegg-in-north-america-usd329-cpu-wont-be-available-at-other-vendors-until-at-least-q4",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T16:47:21+00:00",
    "summary": "AMD's newest CPU, the Ryzen 7 7700X3D, costs $329 and is available exclusively at Newegg in Canada and the United States till the end of Q3 2026. It's a great gaming performer but there are better opt"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tower-semiconductor-revives-shuttered-panasonic-era-fab-in-3-billion-japan-photonics-expansion",
    "domain": "AI 算力 / 半导体",
    "title": "Tower Semiconductor revives shuttered Panasonic-era fab in $3 billion Japan photonics expansion — METI-backed plan targets $3.6 billion revenue by 2028",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tower-semiconductor-revives-shuttered-panasonic-era-fab-in-3-billion-japan-photonics-expansion",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T15:39:09+00:00",
    "summary": "Tower Semiconductor has announced a dual-track expansion of its 300mm silicon photonics, silicon germanium, and advanced packaging operations in Japan"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/lenovo-announces-worlds-first-laptop-with-inkjet-printed-oled-the-legion-r9000p-is-equipped-with-a-240-hz-ijp-panel-from-tcl-csot",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo announces world's first laptop with inkjet-printed OLED — the Legion R9000P is equipped with a 240 Hz IJP panel from TCL CSOT",
    "url": "https://www.tomshardware.com/monitors/lenovo-announces-worlds-first-laptop-with-inkjet-printed-oled-the-legion-r9000p-is-equipped-with-a-240-hz-ijp-panel-from-tcl-csot",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T15:20:36+00:00",
    "summary": "The Lenovo Legion R9000P is the first laptop to be equipped with an IJP OLED from TCL CSOT. This display promises a 240 Hz refresh rate and 99% DCI-P3 coverage for a fraction of the price of tradition"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-and-japans-noetra-consortium-to-build-140mw-rubin-ai-factory-with-27500-gpus",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia and Japan unveil world's first national AI infrastructure — Noetra consortium to build a 140MW Rubin AI factory with 27,500 GPUs",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-and-japans-noetra-consortium-to-build-140mw-rubin-ai-factory-with-27500-gpus",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T13:43:58+00:00",
    "summary": "Nvidia today announced that it's working with Japan's Noetra Corp. to build a 140-megawatt AI factory packing 27,500 Rubin GPUs and 13,750 Vera CPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-7700x3d-cpu-review",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen 7 7700X3D review: A slower 7800X3D, but not necessarily a cheaper one",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-7700x3d-cpu-review",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T13:00:00+00:00",
    "summary": "The 7700X3D is a 7800X3D with lower boost clock speeds, but it doesn’t deliver the same value as we’ve seen with previous versions of this segmentation."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/elon-musk-spent-estimated-usd1-billion-on-an-energy-company-to-power-xai-filings-reveal-apr-energy-owns-a-fleet-of-trailer-mounted-gas-and-diesel-turbines-capable-of-generating-more-than-1-gigawatt",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk spent estimated $1 billion on an energy company to power xAI, filings reveal — APR Energy owns a fleet of trailer-mounted gas and diesel turbines capable of generating more than 1 gigawatt",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/elon-musk-spent-estimated-usd1-billion-on-an-energy-company-to-power-xai-filings-reveal-apr-energy-owns-a-fleet-of-trailer-mounted-gas-and-diesel-turbines-capable-of-generating-more-than-1-gigawatt",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T12:45:17+00:00",
    "summary": "An FTC document revealed that Elon Musk purchased APR Energy, a mobile natural gas and diesel turbine generator provider, for an estimated $1 billion. The deal wasn't announced publicly and was only d"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/tsmc-commits-another-100-billion-to-arizona-for-at-least-four-more-2nm-fabs",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC commits another $100 billion to Arizona for at least four more 2nm fabs — 2026 capex could hit $64 billion following another record quarterly earnings",
    "url": "https://www.tomshardware.com/tech-industry/tsmc-commits-another-100-billion-to-arizona-for-at-least-four-more-2nm-fabs",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T12:10:51+00:00",
    "summary": "TSMC will invest an additional $100 billion in the U.S. to build at least four more chipmaking plants and advanced packaging facilities in Arizona."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/asus-rog-xreal-r1-review",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Xreal R1 Review: Gaming-focused AR glasses deliver 240 Hz performance and RGB style",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/asus-rog-xreal-r1-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T12:00:00+00:00",
    "summary": "Asus throws in everything but the kitchen sink with the ROG Xreal R1, including a 240 Hz refresh rate and a breakout box for connecting to a PC or console."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/prusa-research-founder-edition-indx-launches-limited-1-000-unit-run-of-revolutionary-toolchanger-mod-now-shipping",
    "domain": "AI 算力 / 半导体",
    "title": "Prusa Research Founder Edition INDX launches — limited 1,000-unit run of revolutionary toolchanger mod now shipping",
    "url": "https://www.tomshardware.com/3d-printing/prusa-research-founder-edition-indx-launches-limited-1-000-unit-run-of-revolutionary-toolchanger-mod-now-shipping",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T11:55:55+00:00",
    "summary": "One thousand Prusa CORE One INDX Founder’s Editions have shipped, giving a lucky few first access to Bondtech’s revolutionary toolchanger mod. The Founders Edition is a special limited run, intended f"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/save-usd300-on-the-bambu-lab-p1s-right-now-in-stock-and-back-to-a-record-low-usd399-score-a-huge-discount-on-this-fully-enclosed-easy-to-use-corexy-3d-printer-with-automatic-bed-leveling-and-a-beginner-friendly-setup",
    "domain": "AI 算力 / 半导体",
    "title": "Save $300 on the Bambu Lab P1S right now, in stock and back to a record-low $399 — score a huge discount on this fully enclosed, easy-to-use CoreXY 3D printer with automatic bed leveling and a beginne",
    "url": "https://www.tomshardware.com/3d-printing/save-usd300-on-the-bambu-lab-p1s-right-now-in-stock-and-back-to-a-record-low-usd399-score-a-huge-discount-on-this-fully-enclosed-easy-to-use-corexy-3d-printer-with-automatic-bed-leveling-and-a-beginner-friendly-setup",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T11:07:16+00:00",
    "summary": "The Bambu Lab P1S 3D printer is on sale for $399.99 right now, back at its record low price."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/keyboards/openais-first-hardware-device-is-an-rgb-macropod-codex-micro-features-13-low-profile-keys-and-a-joystick-for-controlling-ai-coding-agents",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI's first hardware device is an RGB macropod — 'Codex Micro' features 13 low-profile keys and a joystick for controlling AI coding agents",
    "url": "https://www.tomshardware.com/peripherals/keyboards/openais-first-hardware-device-is-an-rgb-macropod-codex-micro-features-13-low-profile-keys-and-a-joystick-for-controlling-ai-coding-agents",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T11:00:00+00:00",
    "summary": "OpenAI has launched the \"Codex Micro\" marcopad in collaboration with Work Louder. It uses RGB to provide feedback about your coding agents in Codex, and features various customizable inputs to maximiz"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/get-an-rtx-5080-gaming-laptop-for-just-usd2-199-thanks-to-this-hp-omen-max-deal-save-usd1-500-on-amd-ryzen-9-beast-with-32gb-of-ram",
    "domain": "AI 算力 / 半导体",
    "title": "Get an RTX 5080 gaming laptop for just $2,199 thanks to this HP Omen Max deal — save $1,500 on AMD Ryzen 9 beast with 32GB of RAM",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/get-an-rtx-5080-gaming-laptop-for-just-usd2-199-thanks-to-this-hp-omen-max-deal-save-usd1-500-on-amd-ryzen-9-beast-with-32gb-of-ram",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T10:33:11+00:00",
    "summary": "Get $1,500 off this HP Omen Max gaming laptop with AMD Ryzen 9, RTX 5080, and 32GB of RAM."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/scientists-synchronize-105-000-nano-oscillators-in-just-45-nanoseconds-paving-the-way-for-a-highly-efficient-and-fast-alternative-to-transistors",
    "domain": "AI 算力 / 半导体",
    "title": "Scientists synchronize 105,000 nano-oscillators in just 45 nanoseconds — paving the way for a highly efficient and fast alternative to transistors",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/scientists-synchronize-105-000-nano-oscillators-in-just-45-nanoseconds-paving-the-way-for-a-highly-efficient-and-fast-alternative-to-transistors",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T10:30:00+00:00",
    "summary": "Scientists synchronize 105,000 nano-oscillators in just 45 nanoseconds — paving way for highly efficient and fast alternative to transistors"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/ex-sega-engineer-creates-super-realistic-crt-monitor-emulator-incredible-retro-offering-even-includes-tv-screen-tapping-to-fix-picture",
    "domain": "AI 算力 / 半导体",
    "title": "Ex-Sega engineer creates 'super realistic' CRT monitor emulator — incredible retro offering even includes TV screen tapping to fix picture",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/ex-sega-engineer-creates-super-realistic-crt-monitor-emulator-incredible-retro-offering-even-includes-tv-screen-tapping-to-fix-picture",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T10:00:00+00:00",
    "summary": "A CRT emulation project has implemented percussive maintenance support. Just hit it for a chance to improve the picture."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/open-source-ps3-emulator-says-its-now-compatible-with-over-75-percent-of-all-ps3-games-on-pc-rpcs3-announcement-comes-weeks-after-sony-announced-the-shuttering-of-the-playstation-store-for-ps3-and-ps-vita-by-july-2027",
    "domain": "AI 算力 / 半导体",
    "title": "75% of all PS3 games reportedly now run on PC via open-source emulator RPCS3 — announcement comes weeks after Sony's plan to shutter the PlayStation Store for PS3 and PS Vita by 2027",
    "url": "https://www.tomshardware.com/video-games/playstation/open-source-ps3-emulator-says-its-now-compatible-with-over-75-percent-of-all-ps3-games-on-pc-rpcs3-announcement-comes-weeks-after-sony-announced-the-shuttering-of-the-playstation-store-for-ps3-and-ps-vita-by-july-2027",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T09:00:00+00:00",
    "summary": "The RPCS3 team has successfully ensured that more than 2,600 PS3 titles are now compatible with the emulator. This means that 75.33% of all PS3 games can now be played on Windows, Linux, macOS, and Fr"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidias-huang-vows-to-deliver-giant-amounts-of-vera-rubin-company-says-that-our-roadmap-is-intact",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Huang vows to deliver 'giant amounts' of Vera Rubin — company says that 'our roadmap is intact'",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidias-huang-vows-to-deliver-giant-amounts-of-vera-rubin-company-says-that-our-roadmap-is-intact",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T19:07:17+00:00",
    "summary": "Chief executive of Nvidia says the company is on track to produce 'giant amounts' of Vera Rubin-based machines, but fails to address rumored delays of Kyber NVL144 racks from 2027 to 2028."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/cxmts-ddr5-ram-isnt-as-performant-or-as-consistent-as-sk-hynix-dies-early-testing-shows-reveals-resistance-to-voltage-scaling-and-inferior-manual-overclocking-capabilities",
    "domain": "AI 算力 / 半导体",
    "title": "CXMT's DDR5 RAM isn't as performant or as consistent as SK hynix dies, early testing shows — reveals resistance to voltage scaling and inferior manual overclocking capabilities",
    "url": "https://www.tomshardware.com/pc-components/ddr5/cxmts-ddr5-ram-isnt-as-performant-or-as-consistent-as-sk-hynix-dies-early-testing-shows-reveals-resistance-to-voltage-scaling-and-inferior-manual-overclocking-capabilities",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T16:34:54+00:00",
    "summary": "Early testing hints that CXMT-made DDR5 RAM performs worse than SK Hynix-made DDR5 at the same clock speeds, while being harder to manually overclock as well. It also allegedly doesn't scale with volt"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/asrock-phantom-gaming-and-steel-legend-360-lcd-review",
    "domain": "AI 算力 / 半导体",
    "title": "ASRock Phantom Gaming and Steel Legend 360 LCD review: An impressive cooling debut",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/asrock-phantom-gaming-and-steel-legend-360-lcd-review",
    "source": "Albert Thomas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T16:11:45+00:00",
    "summary": "ASRock has entered the cooling market with the Phantom Gaming 360 LCD and Steel Legend 360 LCD AIOs. We’ve tested both liquid coolers with AMD’s Ryzen 9 9950X3D to benchmark their thermal proficiency."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-becomes-the-first-company-to-ship-high-volume-logic-chips-made-with-asmls-high-na-euv-select-panther-lake-layers-on-18a-are-now-dual-qualified-for-0-55-na-scanners",
    "domain": "AI 算力 / 半导体",
    "title": "Intel becomes the first company to ship high-volume logic chips made with ASML's High NA EUV — select Panther Lake layers on 18A are now dual-qualified for 0.55 NA scanners",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-becomes-the-first-company-to-ship-high-volume-logic-chips-made-with-asmls-high-na-euv-select-panther-lake-layers-on-18a-are-now-dual-qualified-for-0-55-na-scanners",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T15:33:13+00:00",
    "summary": "Intel is using ASML’s High-NA EUV tools to pattern select Panther Lake layers, marking the technology’s first use in high-volume logic production"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-a-dji-osmo-camera-at-some-of-lowest-us-prices-ever",
    "domain": "AI 算力 / 半导体",
    "title": "Grab a DJI Osmo camera at some of lowest US prices ever",
    "url": "https://www.tomshardware.com/pc-components/grab-a-dji-osmo-camera-at-some-of-lowest-us-prices-ever",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T15:18:10+00:00",
    "summary": "An exclusive sale on AliExpress slashes prices on DJI’s Osmo ultra-compact handheld cameras, bringing them to some of the lowest prices in the U.S."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intels-emib-packaging-gains-traction-as-chip-designers-look-to-skirt-tsmcs-cowos-constraints-googles-reported-decision-for-9th-gen-tpus-highlights-intels-attractive-alternative",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's EMIB packaging gains traction as chip designers look to skirt TSMC's CoWoS constraints — Google's reported decision for 9th-gen TPUs highlights Intel's attractive alternative",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intels-emib-packaging-gains-traction-as-chip-designers-look-to-skirt-tsmcs-cowos-constraints-googles-reported-decision-for-9th-gen-tpus-highlights-intels-attractive-alternative",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T14:45:15+00:00",
    "summary": "Google has reportedly chosen Intel's EMIB-T over TSMC's CoWoS-L for its next-generation TPU, codenamed Humufish. But will Google be alone in its alleged decision?"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/pcie-gen7-development-has-already-started-says-silicon-motions-alex-chou-nvidias-storage-next-initiative-is-becoming-a-focal-point",
    "domain": "AI 算力 / 半导体",
    "title": "'PCIe Gen7 development has already started,' says Silicon Motion's Alex Chou — Nvidia's Storage Next initiative is becoming a focal point",
    "url": "https://www.tomshardware.com/pc-components/ssds/pcie-gen7-development-has-already-started-says-silicon-motions-alex-chou-nvidias-storage-next-initiative-is-becoming-a-focal-point",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T14:09:24+00:00",
    "summary": "Silicon Motion is a relatively new entrant to the data center storage market, which has quickly landed orders from various customers and is now ramping up shipments of its high-end PCIe 5.0 SSD contro"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd400-on-a-27-inch-lg-ultragear-oled-monitor-limited-time-discount-nets-you-an-awesome-oled-monitor-with-fast-240hz-refresh-rate-for-your-gaming-pc",
    "domain": "AI 算力 / 半导体",
    "title": "Save $400 on a 27-inch LG Ultragear OLED Monitor — limited-time discount nets you an awesome OLED monitor with fast 240Hz refresh rate for your gaming PC",
    "url": "https://www.tomshardware.com/pc-components/save-usd400-on-a-27-inch-lg-ultragear-oled-monitor-limited-time-discount-nets-you-an-awesome-oled-monitor-with-fast-240hz-refresh-rate-for-your-gaming-pc",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T13:40:14+00:00",
    "summary": "Save $400 on LG’s 27-inch UltraGear 27GS93QE OLED gaming monitor, now $499.99 - with QHD 240 Hz OLED panel, true blacks, and FreeSync/G-Sync support, this deal is worth grabbing."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/pc-gamer-turns-steam-games-into-cartridges-with-ingenious-2-5-inch-ssd-system-games-are-stored-on-128gb-drives-alongside-a-script-to-auto-start-the-title-once-plugged-in",
    "domain": "AI 算力 / 半导体",
    "title": "PC gamer turns Steam games into cartridges with ingenious 2.5-inch SSD system — games are stored on 128GB drives alongside a script to auto-start the title once plugged in",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/pc-gamer-turns-steam-games-into-cartridges-with-ingenious-2-5-inch-ssd-system-games-are-stored-on-128gb-drives-alongside-a-script-to-auto-start-the-title-once-plugged-in",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T12:16:35+00:00",
    "summary": "A PC gamer has created and demonstrated a handy Steam Game Cartridge system."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/palit-officially-announces-rtx-3060-return-with-new-infinity-2-oc-launch-2021-gpu-with-12gb-of-vram-is-an-ai-crisis-stopgap",
    "domain": "AI 算力 / 半导体",
    "title": "Palit officially announces RTX 3060 return with 'new' Infinity 2 OC launch — 2021 GPU with 12GB of VRAM is an AI crisis stopgap",
    "url": "https://www.tomshardware.com/pc-components/gpus/palit-officially-announces-rtx-3060-return-with-new-infinity-2-oc-launch-2021-gpu-with-12gb-of-vram-is-an-ai-crisis-stopgap",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T11:59:06+00:00",
    "summary": "Nvidia has rebooted its five-year-old RTX 3060 graphics card, as is, for the modern AI era, bringing back the GPU officially at its original $329 price. It still features 12GB of VRAM, which serves as"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/elon-musks-starlink-releases-smaller-and-lighter-v5-residential-kit-offers-speeds-of-up-to-375-mbps-and-almost-half-the-power-consumption-of-v4",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk's Starlink releases smaller and lighter V5 residential kit — offers speeds of up to 375 Mbps and almost half the power consumption of V4",
    "url": "https://www.tomshardware.com/networking/routers/elon-musks-starlink-releases-smaller-and-lighter-v5-residential-kit-offers-speeds-of-up-to-375-mbps-and-almost-half-the-power-consumption-of-v4",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T11:47:52+00:00",
    "summary": "Starlink just released a new generation of its Starlink terminal, which reduces its weight by more than 50% and is significantly smaller, too. This should make it easier to install, especially for DIY"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/score-16gb-of-ddr5-ram-for-just-usd61-99-in-this-newegg-parts-bundle-with-the-7800x3d-epic-kit-deal-for-a-gaming-pc-build-nets-you-usd189-in-savings-and-ships-with-a-gigabyte-motherboard-and-free-msi-mag-cooler",
    "domain": "AI 算力 / 半导体",
    "title": "Score 16GB of DDR5 RAM for just $61.99 in this Newegg parts bundle with the 7800X3D — epic kit deal for a gaming PC build nets you $189 in savings and ships with a Gigabyte motherboard and free MSI MA",
    "url": "https://www.tomshardware.com/pc-components/score-16gb-of-ddr5-ram-for-just-usd61-99-in-this-newegg-parts-bundle-with-the-7800x3d-epic-kit-deal-for-a-gaming-pc-build-nets-you-usd189-in-savings-and-ships-with-a-gigabyte-motherboard-and-free-msi-mag-cooler",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T11:30:15+00:00",
    "summary": "This 7800X3D bundle from Newegg saves you $188 and ships with a Gigabyte motherboard and 16GB of DDR5 RAM for just $636.99 overall."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/best-buy-has-slashed-usd900-off-this-asus-64gb-2-in-1-touchscreen-gaming-laptop-usd2-099-rog-flow-z13-is-great-for-both-gaming-and-ai-use",
    "domain": "AI 算力 / 半导体",
    "title": "Best Buy has slashed $900 off this Asus 64GB 2-in-1 touchscreen gaming laptop — $2,099 RoG Flow Z13 is great for both gaming and AI use",
    "url": "https://www.tomshardware.com/laptops/best-buy-has-slashed-usd900-off-this-asus-64gb-2-in-1-touchscreen-gaming-laptop-usd2-099-rog-flow-z13-is-great-for-both-gaming-and-ai-use",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T11:24:13+00:00",
    "summary": "Gaming laptop or touchscreen tablet, you choose. Save $900 on the Asus RoG Flow Z13 at Best Buy."
  },
  {
    "id": "hn:48894277",
    "domain": "AI 算力 / 半导体",
    "title": "Apple's rumored M7 Ultra targets 1.5TB and Blackwell-class AI performance",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/apples-rumored-m7-ultra-targets-1-5tb-of-memory-and-blackwell-class-ai",
    "source": "rbanffy",
    "platform": "hackernews",
    "points": 26,
    "published_at": "2026-07-13T15:32:19+00:00",
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
    "id": "hn:48845518",
    "domain": "AI 算力 / 半导体",
    "title": "Reverse-engineering Nvidia's CUDA-checkpoint for faster cold starts",
    "url": "https://blog.doubleword.ai/what-happens-when-you-checkpoint-a-cuda-process",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-09T13:29:52+00:00",
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
    "id": "hn:48925271",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://turntrout.com/why-i-left-google-deepmind",
    "source": "apsec112",
    "platform": "hackernews",
    "points": 356,
    "published_at": "2026-07-15T18:40:34+00:00",
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
    "id": "hn:48936451",
    "domain": "大厂 AI 动态",
    "title": "NotebookLM is now Gemini Notebook",
    "url": "https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/",
    "source": "xnx",
    "platform": "hackernews",
    "points": 279,
    "published_at": "2026-07-16T16:08:13+00:00",
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
    "id": "rss:https://www.theverge.com/games/966815/epic-games-fortnite-ai-powered-personas",
    "domain": "大厂 AI 动态",
    "title": "Fortnite is getting a bunch of AI-powered ‘personas’",
    "url": "https://www.theverge.com/games/966815/epic-games-fortnite-ai-powered-personas",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T21:30:35+00:00",
    "summary": "Get ready for more AI characters in Fortnite. Developer Epic Games is going to let Fortnite creators publish experiences featuring characters with AI-powered voices starting on July 30th, and ahead of"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/966613/samsung-the-frame-art-tv-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Samsung’s 55-inch Frame art TV is $200 cheaper than usual",
    "url": "https://www.theverge.com/gadgets/966613/samsung-the-frame-art-tv-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T20:47:30+00:00",
    "summary": "Samsung’s Frame is different from your average 4K TV. Its biggest selling point involves what it does when you aren’t actively using it. It can display art, turning your living room into a gallery. Th"
  },
  {
    "id": "rss:https://www.theverge.com/streaming/966633/netflix-ai-titles-q2-2026-earnings",
    "domain": "大厂 AI 动态",
    "title": "Netflix says around 300 titles used generative AI",
    "url": "https://www.theverge.com/streaming/966633/netflix-ai-titles-q2-2026-earnings",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T20:29:27+00:00",
    "summary": "Netflix says roughly 300 titles on its platform used generative AI, most of which occurred in post-production. The streaming service revealed the news in its second-quarter earnings report released on"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/966726/cd-sales-vinyl-physical-media-luminate",
    "domain": "大厂 AI 动态",
    "title": "Why are people buying so many CDs?",
    "url": "https://www.theverge.com/entertainment/966726/cd-sales-vinyl-physical-media-luminate",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T19:55:29+00:00",
    "summary": "CD sales are apparently going up, reportedly thanks to fans realizing they're an affordable way to support their favorite artists. According to a new report from research firm Luminate, 16.3 million C"
  },
  {
    "id": "rss:https://www.theverge.com/news/966676/trump-teleprompter-operator-kalshi-bets-mention-markets-investigation",
    "domain": "大厂 AI 动态",
    "title": "Kalshi says it caught Trump&#8217;s teleprompter operator insider trading",
    "url": "https://www.theverge.com/news/966676/trump-teleprompter-operator-kalshi-bets-mention-markets-investigation",
    "source": "Mia Sato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T18:43:14+00:00",
    "summary": "Kalshi users betting on what President Donald Trump would say during his speeches were reportedly up against tough competition: the president's teleprompter operator. ABC News reports that federal inv"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/966647/new-york-governor-kathy-hochul-ai-policies",
    "domain": "大厂 AI 动态",
    "title": "New York governor says she&#8217;s using AI to analyze &#8216;every single rule&#8217; in the state",
    "url": "https://www.theverge.com/ai-artificial-intelligence/966647/new-york-governor-kathy-hochul-ai-policies",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T17:58:37+00:00",
    "summary": "New York Governor Kathy Hochul might have just signed a moratorium on new AI data centers in the state, but she's not against using the technology herself. During an interview with Bloomberg's Odd Lot"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/966651/ecovacs-deebot-x11-robot-vacuum-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Ecovacs&#8217; self-cleaning Deebot X11 has hit a new low price",
    "url": "https://www.theverge.com/gadgets/966651/ecovacs-deebot-x11-robot-vacuum-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T17:57:15+00:00",
    "summary": "Sometimes it feels like keeping your floors clean is one of those never-ending chores, which is why it's nice to have a versatile robot vacuum take it off your hands. The Ecovacs Deebot X11 robovac / "
  },
  {
    "id": "rss:https://www.theverge.com/policy/966588/eu-dma-ai-android-siri-ai",
    "domain": "大厂 AI 动态",
    "title": "Google is better than Apple at playing the AI regulations game",
    "url": "https://www.theverge.com/policy/966588/eu-dma-ai-android-siri-ai",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T16:55:54+00:00",
    "summary": "Today, the European Union ordered Google to give its AI rivals greater access to Android, the open-source operating system that powers billions of devices worldwide. The demand is hardly surprising. I"
  },
  {
    "id": "rss:https://www.theverge.com/games/966589/roblox-build-ai-phone-moblie-games",
    "domain": "大厂 AI 动态",
    "title": "Roblox will let people use AI to make games on their phone",
    "url": "https://www.theverge.com/games/966589/roblox-build-ai-phone-moblie-games",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T16:45:29+00:00",
    "summary": "Roblox is about to let people make games with AI right inside its mobile app, which could make a platform that's already filled with content of questionable quality feel even more overloaded. The comp"
  },
  {
    "id": "rss:https://www.theverge.com/tech/966112/google-gemini-notebook-notebooklm",
    "domain": "大厂 AI 动态",
    "title": "Google is renaming NotebookLM to Gemini Notebook",
    "url": "https://www.theverge.com/tech/966112/google-gemini-notebook-notebooklm",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T16:00:00+00:00",
    "summary": "Google is giving its AI note-taking app a new name. The company announced on Thursday that NotebookLM is becoming Gemini Notebook, but will remain a standalone app even as it integrates more deeply ac"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/san-francisco-mayor-pushes-for-tougher-rules-after-the-waymo-traffic-fiasco/",
    "domain": "大厂 AI 动态",
    "title": "San Francisco mayor pushes for tougher rules after the Waymo traffic fiasco",
    "url": "https://techcrunch.com/2026/07/16/san-francisco-mayor-pushes-for-tougher-rules-after-the-waymo-traffic-fiasco/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T23:25:22+00:00",
    "summary": "In the wake of a massive hours-long gridlock event, San Francisco mayor Daniel Lurie has told state regulators it's time to put more requirements on robotaxi operators like Waymo."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/spacex-suddenly-aborts-second-starship-v3-launch-after-ignition/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX suddenly aborts second Starship V3 launch after ignition",
    "url": "https://techcrunch.com/2026/07/16/spacex-suddenly-aborts-second-starship-v3-launch-after-ignition/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T23:01:27+00:00",
    "summary": "The company didn't immediately say what went wrong. SpaceX's stock plunged more than 4% in after-hours trading before paring losses."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/coca-cola-suspended-production-at-its-fairlife-dairy-after-a-ransomware-attack/",
    "domain": "大厂 AI 动态",
    "title": "Coca-Cola suspended production at its Fairlife dairy after a ransomware attack",
    "url": "https://techcrunch.com/2026/07/16/coca-cola-suspended-production-at-its-fairlife-dairy-after-a-ransomware-attack/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T21:22:31+00:00",
    "summary": "Coca Cola said dairy production at its Fairlife unit will \"remain suspended\" in the United States following a hack."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/founders-fund-hires-former-openai-exec-ryan-beiermeister-and-not-because-of-her-mafia-skills/",
    "domain": "大厂 AI 动态",
    "title": "Founders Fund hires former OpenAI exec Ryan Beiermeister (and not because of her ‘Mafia’ skills)",
    "url": "https://techcrunch.com/2026/07/16/founders-fund-hires-former-openai-exec-ryan-beiermeister-and-not-because-of-her-mafia-skills/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T20:07:14+00:00",
    "summary": "Ryan Beiermeister, who demonstrated cool analysis in the Founders Fund YouTube series \"Mafia,\" has joined the firm as a partner."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/google-vids-now-lets-you-star-in-your-own-ai-videos/",
    "domain": "大厂 AI 动态",
    "title": "Google Vids now lets you star in your own AI videos",
    "url": "https://techcrunch.com/2026/07/16/google-vids-now-lets-you-star-in-your-own-ai-videos/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T18:32:54+00:00",
    "summary": "Google is adding personalized AI avatars to Vids that let users create videos starring a digital version of themselves, alongside Gemini Omni-powered tools for generating and editing videos from promp"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/roblox-launches-an-ai-powered-game-creation-feature-in-its-mobile-app/",
    "domain": "大厂 AI 动态",
    "title": "Roblox launches an AI-powered game-creation feature in its mobile app",
    "url": "https://techcrunch.com/2026/07/16/roblox-launches-an-ai-powered-game-creation-feature-in-its-mobile-app/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T18:22:06+00:00",
    "summary": "Roblox's new \"Build\" feature lets users generate basic games using a single text prompt."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/oil-giant-bp-shutters-its-corporate-venture-arm-after-20-years/",
    "domain": "大厂 AI 动态",
    "title": "Oil giant BP shutters its corporate venture arm after 20 years",
    "url": "https://techcrunch.com/2026/07/16/oil-giant-bp-shutters-its-corporate-venture-arm-after-20-years/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T17:37:03+00:00",
    "summary": "BP Ventures is shutting down, ending a nearly 20-year run that was marked by reportedly lackluster returns."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/ubers-14-8b-delivery-hero-deal-would-nearly-double-its-global-footprint/",
    "domain": "大厂 AI 动态",
    "title": "Uber’s $14.8B Delivery Hero deal would nearly double its global footprint",
    "url": "https://techcrunch.com/2026/07/16/ubers-14-8b-delivery-hero-deal-would-nearly-double-its-global-footprint/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T17:12:00+00:00",
    "summary": "Uber has agreed to acquire Delivery Hero in a $14.8 billion all-stock deal that would nearly double the company’s global footprint and create one of the world’s largest food-delivery platforms outside"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/newsletter-platform-beehiiv-now-lets-subscribers-chat-with-each-other-adds-ai/",
    "domain": "大厂 AI 动态",
    "title": "Newsletter platform Beehiiv now lets subscribers chat with each other, adds AI",
    "url": "https://techcrunch.com/2026/07/16/newsletter-platform-beehiiv-now-lets-subscribers-chat-with-each-other-adds-ai/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T17:00:00+00:00",
    "summary": "Beehiiv is launching an AI Copilot to help publishers with user growth and analytics."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/x-cracks-down-on-creators-who-steal-content/",
    "domain": "大厂 AI 动态",
    "title": "X cracks down on creators who steal content",
    "url": "https://techcrunch.com/2026/07/16/x-cracks-down-on-creators-who-steal-content/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T16:40:36+00:00",
    "summary": "X will use Grok AI to better detect stolen content, redirect payouts to original creators, and crack down on engagement bait."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/ai-powered-travel-agency-fora-hits-unicorn-status-raises-60m/",
    "domain": "大厂 AI 动态",
    "title": "AI-powered travel agency Fora hits unicorn status, raises $60M",
    "url": "https://techcrunch.com/2026/07/16/ai-powered-travel-agency-fora-hits-unicorn-status-raises-60m/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T16:08:40+00:00",
    "summary": "Travel agency Fora announced a $60 million Series D round led by Forerunner and Tactile Ventures, valuing the company at $1 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/googles-ai-mode-now-lets-you-link-and-interact-with-select-apps/",
    "domain": "大厂 AI 动态",
    "title": "Google’s AI Mode now lets you link and interact with select apps",
    "url": "https://techcrunch.com/2026/07/16/googles-ai-mode-now-lets-you-link-and-interact-with-select-apps/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T16:00:00+00:00",
    "summary": "With this new update, Google is expanding AI Mode beyond answering questions and into completing tasks across the apps they use regularly."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/google-continues-its-renaming-streak-by-turning-notebooklm-to-gemini-notebook/",
    "domain": "大厂 AI 动态",
    "title": "Google continues its renaming streak by turning NotebookLM to Gemini Notebook",
    "url": "https://techcrunch.com/2026/07/16/google-continues-its-renaming-streak-by-turning-notebooklm-to-gemini-notebook/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T16:00:00+00:00",
    "summary": "Google said users can soon access their notebooks through AI Mode in Search."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/yes-you-can-now-order-doordash-from-the-command-line/",
    "domain": "大厂 AI 动态",
    "title": "Yes, you can now order DoorDash from the command line",
    "url": "https://techcrunch.com/2026/07/16/yes-you-can-now-order-doordash-from-the-command-line/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T15:38:55+00:00",
    "summary": "DoorDash is opening a limited beta of dd-cli, a command-line tool that lets developers and AI agents search stores, build carts, and place orders from the terminal, marking another step toward softwar"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/uk-cops-say-arrest-of-two-young-hackers-disrupted-the-operations-of-an-infamous-hacking-group/",
    "domain": "大厂 AI 动态",
    "title": "UK cops say arrest of two young hackers disrupted the operations of an infamous hacking group",
    "url": "https://techcrunch.com/2026/07/16/uk-cops-say-arrest-of-two-young-hackers-disrupted-the-operations-of-an-infamous-hacking-group/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T15:37:47+00:00",
    "summary": "Owen Flowers and Thalha Jubair, two members of the prolific Scattered Spider hacking group, pleaded guilty and were sentenced to five years and six months in jail for hacking London’s metropolitan tra"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/period-tracker-stardust-shares-users-health-data-with-analytics-firm-says-mozilla-research/",
    "domain": "大厂 AI 动态",
    "title": "Period tracker Stardust shares users’ health data with analytics firm, says Mozilla research",
    "url": "https://techcrunch.com/2026/07/16/period-tracker-stardust-shares-users-health-data-with-analytics-firm-says-mozilla-research/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T15:33:28+00:00",
    "summary": "One period tracker app tested by Mozilla was 'squeaky clean,' while another app was seen sharing users' health data with an analytics company, underscoring vast differences in user privacy among these"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/why-is-openai-selling-a-chatgpt-basketball/",
    "domain": "大厂 AI 动态",
    "title": "Why is OpenAI selling a ChatGPT basketball?",
    "url": "https://techcrunch.com/2026/07/16/why-is-openai-selling-a-chatgpt-basketball/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T15:31:09+00:00",
    "summary": "You may have heard that OpenAI released its first piece of hardware this week. You may not have heard about the ChatGPT basketball."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/how-a-former-deepmind-researcher-raised-at-a-300m-pre-seed-valuation-before-launching-a-product/",
    "domain": "大厂 AI 动态",
    "title": "How a former DeepMind researcher raised at a $300M pre-seed valuation before launching a product",
    "url": "https://techcrunch.com/2026/07/16/how-a-former-deepmind-researcher-raised-at-a-300m-pre-seed-valuation-before-launching-a-product/",
    "source": "Maggie Nye",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T15:02:00+00:00",
    "summary": "Drawing on more than a decade spent helping build some of the world's most influential AI systems, including research that later informed the development of ChatGPT, Andrew Dai explains why he believe"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/sheryl-sandberg-leads-10-million-investment-in-ai-powered-vehicle-inspection-service/",
    "domain": "大厂 AI 动态",
    "title": "Sheryl Sandberg leads $10 million investment in AI-powered vehicle inspection service",
    "url": "https://techcrunch.com/2026/07/16/sheryl-sandberg-leads-10-million-investment-in-ai-powered-vehicle-inspection-service/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T15:00:00+00:00",
    "summary": "The startup, founded in 2021, lets enterprise customers use smartphones to scan and spot vehicle damage."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/16/why-ami-labs-alexandre-lebrun-wont-call-his-ai-agi-or-superintelligence/",
    "domain": "大厂 AI 动态",
    "title": "Why AMI Labs’ Alexandre LeBrun won’t call his AI ‘AGI’ or ‘superintelligence’",
    "url": "https://techcrunch.com/2026/07/16/why-ami-labs-alexandre-lebrun-wont-call-his-ai-agi-or-superintelligence/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T14:40:00+00:00",
    "summary": "While everyone in AI is chasing \"superintelligence,\" Alexandre LeBrun, CEO of Yann LeCun’s world model startup, AMI Labs, dismisses the word."
  },
  {
    "id": "rss:https://stratechery.com/2026/ibm-misses-ibms-mainframe-moat-ibms-many-ai-problems/",
    "domain": "大厂 AI 动态",
    "title": "IBM Misses, IBM’s Mainframe Moat, IBM’s Many AI Problems",
    "url": "https://stratechery.com/2026/ibm-misses-ibms-mainframe-moat-ibms-many-ai-problems/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-15T10:00:19+00:00",
    "summary": "IBM announced preliminary results that spooked the software market generally; this is a story, however, specifically about IBM and its mainframe franchise."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/spacex-scrubs-starship-launch-after-some-of-its-engines-didnt-start/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX scrubs Starship launch after some of its engines didn't start",
    "url": "https://arstechnica.com/space/2026/07/spacex-scrubs-starship-launch-after-some-of-its-engines-didnt-start/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T00:02:54+00:00",
    "summary": "\"Now offloading propellant. Next launch attempt hopefully in a few days.\""
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/two-trump-health-nominees-crash-and-burn-in-tense-senate-hearing/",
    "domain": "大厂 AI 动态",
    "title": "Two Trump health nominees crash and burn in tense Senate hearing",
    "url": "https://arstechnica.com/health/2026/07/two-trump-health-nominees-crash-and-burn-in-tense-senate-hearing/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T22:33:24+00:00",
    "summary": "Both nominees flailed in their own unique ways as senators sought answers."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/hp-fined-1-4-billion-rupees-for-cartelization-of-ink-cartridges-toner-pcs/",
    "domain": "大厂 AI 动态",
    "title": "HP fined 1.4 billion rupees for “cartelization” of ink cartridges, toner, PCs",
    "url": "https://arstechnica.com/gadgets/2026/07/hp-fined-1-4-billion-rupees-for-cartelization-of-ink-cartridges-toner-pcs/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T22:02:31+00:00",
    "summary": "Resellers threatened to ditch HP printing supplies for counterfeits."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/t-mobile-bungled-forced-plan-migration-canceling-some-users-free-lines/",
    "domain": "大厂 AI 动态",
    "title": "T-Mobile bungled forced plan migration, canceling some users' free lines",
    "url": "https://arstechnica.com/tech-policy/2026/07/t-mobile-bungled-forced-plan-migration-canceling-some-users-free-lines/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T20:52:47+00:00",
    "summary": "T-Mobile to restore free lines lost during plan migration, but price hikes remain."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/07/its-official-eu-will-force-google-to-share-search-data-and-open-up-ai-on-android/",
    "domain": "大厂 AI 动态",
    "title": "It's official: EU will force Google to share search data and open up AI on Android",
    "url": "https://arstechnica.com/gadgets/2026/07/its-official-eu-will-force-google-to-share-search-data-and-open-up-ai-on-android/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T20:41:45+00:00",
    "summary": "Google says these changes could endanger user privacy and security."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/xai-cant-deny-grok-makes-csam-anymore-so-its-suing-users/",
    "domain": "大厂 AI 动态",
    "title": "xAI can’t deny Grok makes CSAM anymore. So it’s suing users.",
    "url": "https://arstechnica.com/tech-policy/2026/07/xai-cant-deny-grok-makes-csam-anymore-so-its-suing-users/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T20:26:23+00:00",
    "summary": "Elon Musk's xAI files first lawsuit against Grok user accused of making child sex images."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/fear-of-humanoid-robots-spurs-human-workers-to-strike-at-hyundai-auto-factory/",
    "domain": "大厂 AI 动态",
    "title": "Fear of humanoid robots spurs human workers to strike at Hyundai auto factory",
    "url": "https://arstechnica.com/ai/2026/07/fear-of-humanoid-robots-spurs-human-workers-to-strike-at-hyundai-auto-factory/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T20:09:48+00:00",
    "summary": "Hyundai aims to deploy 25,000 Atlas robots starting with US factories in 2028."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/07/trump-teleprompter-aide-made-100000-betting-on-what-trump-would-say-reports-say/",
    "domain": "大厂 AI 动态",
    "title": "Trump teleprompter aide made $100,000 betting on what Trump would say, reports say",
    "url": "https://arstechnica.com/culture/2026/07/trump-teleprompter-aide-made-100000-betting-on-what-trump-would-say-reports-say/",
    "source": "Nate Anderson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T19:55:46+00:00",
    "summary": "If only someone could have predicted it."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/07/2026-toyota-rav4-plug-in-review-good-but-skip-the-gr-sport/",
    "domain": "大厂 AI 动态",
    "title": "2026 Toyota RAV4 plug-in: Big battery means daily drives are all-electric",
    "url": "https://arstechnica.com/cars/2026/07/2026-toyota-rav4-plug-in-review-good-but-skip-the-gr-sport/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T19:46:22+00:00",
    "summary": "Toyota's everyday small SUV should rarely require trips to the gas station."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/07/now-even-russias-most-elite-hackers-are-using-clickfix-to-infect-devices/",
    "domain": "大厂 AI 动态",
    "title": "Now, even Russia's most elite hackers are using Clickfix to infect devices",
    "url": "https://arstechnica.com/security/2026/07/now-even-russias-most-elite-hackers-are-using-clickfix-to-infect-devices/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T19:28:33+00:00",
    "summary": "The social-engineering technique has primarily been a tool of financially motivated criminals."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/linus-torvalds-to-critics-of-ai-coding-in-linux-fork-it-or-just-walk-away/",
    "domain": "大厂 AI 动态",
    "title": "Linus Torvalds to critics of AI coding in Linux: \"Fork it. Or just walk away.\"",
    "url": "https://arstechnica.com/ai/2026/07/linus-torvalds-to-critics-of-ai-coding-in-linux-fork-it-or-just-walk-away/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T19:18:23+00:00",
    "summary": "Creator says he will \"very loudly ignore\" those arguing for a ban on AI tools."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/weve-seen-helium-baked-off-a-rocky-exoplanets-atmosphere/",
    "domain": "大厂 AI 动态",
    "title": "We've seen helium baked off a rocky exoplanet's atmosphere",
    "url": "https://arstechnica.com/science/2026/07/weve-seen-helium-baked-off-a-rocky-exoplanets-atmosphere/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-16T18:00:15+00:00",
    "summary": "If the large, rocky planet is losing helium, then we can infer what is left behind."
  },
  {
    "id": "hn:48933344",
    "domain": "股票",
    "title": "SpaceX stock erases all its gains and slides below IPO price in intraday trading",
    "url": "https://www.latimes.com/business/story/2026-07-16/spacex-stock-erases-gains-slides-below-ipo-price-in-intraday-trading",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 290,
    "published_at": "2026-07-16T12:02:11+00:00",
    "summary": ""
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
    "id": "hn:48938001",
    "domain": "股票",
    "title": "SPCX is now Wall Street's most shorted new stock",
    "url": "https://invezz.com/news/2026/07/16/the-worlds-most-valuable-ipo-spcx-is-now-wall-streets-most-shorted-new-stock/",
    "source": "lbrito",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-07-16T18:03:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:48923343",
    "domain": "股票",
    "title": "SpaceX stock sinks below $135 IPO price for the first time",
    "url": "https://www.cnbc.com/2026/07/15/spacex-spcx-stock-ipo-price.html",
    "source": "abduhl",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-07-15T16:30:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:48907665",
    "domain": "股票",
    "title": "IBM is on pace for its worst day ever",
    "url": "https://www.cnn.com/2026/07/14/tech/ibm-stock-worst-day-ever",
    "source": "1970-01-01",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-07-14T14:39:25+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3777165",
    "domain": "股票",
    "title": "沪指跌破3800点，电力银行逆势拉升，医药芯片深度回调，恒科指跌近5%，AI大模型双雄齐跌、智谱跌近30%",
    "url": "https://wallstreetcn.com/articles/3777165",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T05:41:18+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市近4400股飘绿，上午半天成交1.61万亿。沪深两市半日成交额1.6万亿，较上个交易日放量超1200亿。板块方面，半导体、算力硬件产业链持续调整，CPO、存储器、PCB方向领跌；医药生物行业下挫，CRO、创新药方向跌幅靠前。电力股逆势走强。"
  },
  {
    "id": "wscn:3777177",
    "domain": "股票",
    "title": "报道：智谱ARR达到10亿美元，半年增长15倍",
    "url": "https://wallstreetcn.com/articles/3777177",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T05:32:55+00:00",
    "summary": "智能涌现从多个独立信源处获悉，截至2026年7月，智谱的ARR（年度经常性收入）已经达到10亿美元。有分析称，智谱达到10亿美金ARR的速度，远超预期。曾有投资人表示，智谱的ARR预计到2026年底，才能达到10亿-15亿美金。"
  },
  {
    "id": "wscn:3776981",
    "domain": "股票",
    "title": "300万亿养老金回流日本：GPIF能否扭转日元贬值？",
    "url": "https://wallstreetcn.com/premium/articles/3776981?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T05:27:21+00:00",
    "summary": "日本养老基金增配国内资产可短期支撑日元日债，但信号大于实质，反转需央行加息与基本面改善。"
  },
  {
    "id": "wscn:3777176",
    "domain": "股票",
    "title": "国家发改委发布《人工智能合作发展行动计划》，推动智能算力普惠、开源生态共享",
    "url": "https://wallstreetcn.com/articles/3777176",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T05:04:46+00:00",
    "summary": "人工智能合作发展行动计划包括：优质数据供给行动、智能算力普惠行动、开源生态共享行动、人工智能深度赋能行动、数智人才共育行动、规则标准共建行动、安全治理协作行动、人工智能向善行动。"
  },
  {
    "id": "wscn:3777166",
    "domain": "股票",
    "title": "美股还有“去杠杆空间”！摩根大通：需要三个月才能恢复到4月前水平",
    "url": "https://wallstreetcn.com/articles/3777166",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T03:59:09+00:00",
    "summary": "摩根大通判断，美股6月启动的去杠杆进程仍在持续，杠杆股票ETF、期权和保证金账户均存在进一步去杠杆空间，预计还需约三个月的震荡行情，相关指标才能回归4月前水平。但从更长周期看，去杠杆压力消退后市场有望获得结构性托底。"
  },
  {
    "id": "wscn:3777167",
    "domain": "股票",
    "title": "如何理解韩国央行此次加息？",
    "url": "https://wallstreetcn.com/articles/3777167",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T03:58:15+00:00",
    "summary": "韩国央行2026年7月16日全票加息25基点至2.75%，为三年半来首次，原因在于经济过热（增长预期上调至3%）、通胀升至3.2%、首尔房价大涨及韩元偏弱。广发证券认为后续继续加息概率较大，10月或再加，终端利率预计3.0%—3.5%。"
  },
  {
    "id": "wscn:3776634",
    "domain": "股票",
    "title": "CDU液冷泵:一场由AI机柜功率推动的产业升级，能否演绎“量价齐升”的成长叙事？",
    "url": "https://wallstreetcn.com/premium/articles/3776634?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T03:50:43+00:00",
    "summary": "随着AI芯片功耗提升，液冷成为高密度算力基础设施，核心部件CDU液冷泵受市场关注。作为决定流量能效的核心，CDU架构演进带动水泵向大功率、电子智能化升级。2026年下半年，英伟达与谷歌液冷平台集中部署，行业迎批量采购。其投资逻辑在于液冷渗透率提高、单泵功率上升、双泵冗余及电子屏蔽化推动的“量增与结构升级”。国内厂商具成本与响应优势，但头部认证、持续交付及长期可靠性是核心竞争力。"
  },
  {
    "id": "wscn:3774897",
    "domain": "股票",
    "title": "下半年资产配置机会在哪里？听徐小庆分享股债汇市场最新洞察，推演配置逻辑",
    "url": "https://wallstreetcn.com/articles/3774897",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T03:18:30+00:00",
    "summary": "7月19日徐小庆主讲Alpha线上闭门私享会：展望2026下半年大类资产配置风向，哪些资产最值得关注？"
  },
  {
    "id": "wscn:3777164",
    "domain": "股票",
    "title": "Doubleline CIO：沃什不是“披着鹰皮的鸽子”，债市已“代劳” 美联储加息",
    "url": "https://wallstreetcn.com/articles/3777164",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T02:35:03+00:00",
    "summary": "Doubleline CIO Jeffrey Sherman认为，债券市场已悄然替美联储完成了部分紧缩工作——收益率曲线上斜、市场开始定价加息可能，新任美联储主席沃什或可按兵不动。与此同时，6月核心CPI出现2020年以来首次环比负值，通胀互换一年期一度跌破2%；但AI需求与股市财富效应仍在推高核心PCE，私募信贷\"投资级\"叙事遭到质疑，CCC级资产风险暗流涌动。"
  },
  {
    "id": "wscn:3777169",
    "domain": "股票",
    "title": "全球股市正在杠杆化、散户化和短期化",
    "url": "https://wallstreetcn.com/articles/3777169",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T02:33:12+00:00",
    "summary": "美国和韩国散户成为单股杠杆ETF交易主力，推动市场走向短期化和高波动。杠杆ETF降低了门槛、放大了价格波动的速度与幅度，并严重缩短市场耐心。近期韩美等多地收紧监管，虽提高门槛防范杠杆扎堆，但去杠杆过程已引发市场剧烈震荡，短期边际定价权正因散户与杠杆工具的共振而发生重构。"
  },
  {
    "id": "wscn:3776760",
    "domain": "股票",
    "title": "全球年需求仅百吨，铪为什么能成为AI时代的“黄金小金属”？",
    "url": "https://wallstreetcn.com/premium/articles/3776760?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T02:12:10+00:00",
    "summary": "铪过去只是核工业与航空发动机里的小众金属，但随着先进逻辑芯片、DRAM、HBM 持续升级，这种全球年需求仅百吨的伴生金属，正走向半导体制造核心环节——国内 4N 级氧化铪价格已从 2022 年的约 450 万元/吨涨至 2026 年的约 950 万元/吨。但市场只盯金属铪涨价并不全面：真正决定长期空间的，是能否提纯为电子级氧化铪、再加工成进入晶圆厂原子层沉积设备的铪前驱体。这轮由价格驱动的行情，究"
  },
  {
    "id": "wscn:3777170",
    "domain": "股票",
    "title": "2026华为乾崑媒体日在深启幕，奕境X9以旗舰之姿登场",
    "url": "https://wallstreetcn.com/articles/3777170",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T02:09:53+00:00",
    "summary": "7月16-17日，以 “安全有乾崑 安心赴美好”为主题的2026华为乾崑媒体日在深成功举办。现场面向..."
  },
  {
    "id": "wscn:3777161",
    "domain": "股票",
    "title": "摩根大通：A股的“AI去杠杆”是健康回调，而非泡沫破裂",
    "url": "https://wallstreetcn.com/articles/3777161",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T01:29:34+00:00",
    "summary": "摩根大通认为，近期A股AI板块回调本质上是杠杆出清而非基本面恶化。IT行业融资交易占比回落且科技ETF逆势吸金，显示去杠杆接近尾声；中美云巨头资产负债率远低于历史泡沫期，财力依旧稳健。随着大模型迭代、硬件供给约束延续至2028年。"
  },
  {
    "id": "wscn:3777163",
    "domain": "股票",
    "title": "加入AI短剧平台战场，阅文上线“起点剧场”",
    "url": "https://wallstreetcn.com/articles/3777163",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T01:19:32+00:00",
    "summary": "采取了付费订阅模式"
  },
  {
    "id": "wscn:3777160",
    "domain": "股票",
    "title": "铠侠一个月“腰斩”，野村依旧上调目标价：NAND闪存价格仍将保持涨势",
    "url": "https://wallstreetcn.com/articles/3777160",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T00:41:32+00:00",
    "summary": "铠侠股价较峰值腰斩之际，野村证券逆势出手——将目标价上调至12.6万日元并重申买入。核心底气来自两大催化剂：NAND位元价格涨幅持续超预期，中国台湾厂商ADATA单季SSD销售暴增87%印证供需偏紧；美国AI出口管制阴霾随GPT-5.6全面开放加速消散。"
  },
  {
    "id": "wscn:3777156",
    "domain": "股票",
    "title": "AI交易已经成了“橡皮筋”，高盛顶尖交易员：问题是“何时会断”",
    "url": "https://wallstreetcn.com/articles/3777156",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T00:13:27+00:00",
    "summary": "高盛EMEA股票交易主管指出，超大规模云计算商正超额押注AI基建，但近期回报面临巨大不确定性。随着开源模型逼近闭源，市场价值链正由硬件商向掌控分发与工作流的“收费站”平台型企业轮动。算力未来或商品化，二季度财报将成为近期AI回报路径的关键试金石。"
  },
  {
    "id": "wscn:3777153",
    "domain": "股票",
    "title": "SpaceX取消“星舰”第13次试飞任务，马斯克：将换发动机，下周初重新尝试发射",
    "url": "https://wallstreetcn.com/articles/3777153",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T00:12:49+00:00",
    "summary": "SpaceX星舰第13次试飞因多台发动机未能点火，于7月16日被迫中止，马斯克表示将在数日内再次尝试，最有可能的发射时间是下周初，为了确保顺利飞行，将更换2台猛禽发动机。消息公布后，SpaceX股价盘后一度跌超4%，自6月高点以来累计下跌约三分之一，市值蒸发逾8600亿美元。"
  },
  {
    "id": "wscn:3777158",
    "domain": "股票",
    "title": "提前预警业绩后股价暴跌，IBM“弄巧成拙”？",
    "url": "https://wallstreetcn.com/articles/3777158",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T00:09:27+00:00",
    "summary": "IBM董事会主动选择提前披露二季度业绩预警，CEO公开承认“这个季度我们失误了”，但换来的是股价单日暴跌25%——这是IBM百年历史上最惨烈的单日跌幅。市值跌破2000亿美元，华尔街开始讨论拆分可能性，激进投资者或将介入。AI浪潮正在挤压IBM的传统硬件和软件业务，但这次坦诚换来的却是恐慌。"
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
    "id": "hn:48915953",
    "domain": "金融",
    "title": "Stripe and Advent have made a joint offer to acquire PayPal – sources",
    "url": "https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/",
    "source": "rvz",
    "platform": "hackernews",
    "points": 486,
    "published_at": "2026-07-15T03:32:45+00:00",
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
    "id": "hn:48892638",
    "domain": "金融",
    "title": "Benchmarking 15 “E-Waste” GPUs with Modern Workloads",
    "url": "https://esologic.com/benchmarking-tesla-gpus/",
    "source": "eso_logic",
    "platform": "hackernews",
    "points": 141,
    "published_at": "2026-07-13T13:48:42+00:00",
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
    "id": "rss:https://arxiv.org/abs/2607.14446",
    "domain": "金融",
    "title": "Which Green Technology to Subsidize? Evidence from Electric Vehicles in South Korea",
    "url": "https://arxiv.org/abs/2607.14446",
    "source": "Youngjin Hong, In Kyung Kim, Frank Verboven",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T04:00:00+00:00",
    "summary": "arXiv:2607.14446v1 Announce Type: new Abstract: We develop a framework to compare the relative effectiveness of subsidizing alternative emission-reducing technologies. We show that an intermediate tec"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.14585",
    "domain": "金融",
    "title": "Governing Artificial Intelligence: Public Preferences and Regulatory Options",
    "url": "https://arxiv.org/abs/2607.14585",
    "source": "Magnus Lundgren, Jonas Tallberg",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T04:00:00+00:00",
    "summary": "arXiv:2607.14585v1 Announce Type: new Abstract: Artificial intelligence (AI) is rapidly transforming economies, societies, and polities, raising fundamental questions about how it should be regulated."
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.14713",
    "domain": "金融",
    "title": "Does Multi-Agent Debate Improve AI Feedback on Research Papers?",
    "url": "https://arxiv.org/abs/2607.14713",
    "source": "Tomas Havranek, Zuzana Irsova",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T04:00:00+00:00",
    "summary": "arXiv:2607.14713v1 Announce Type: new Abstract: Probably not, at least for meta-analyses in economics. In a pre-registered, identity-masked, within-paper experiment, the authors of 44 meta-analyses ra"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.15057",
    "domain": "金融",
    "title": "Existence and convergence of discrete-time Kyle models with multiple insiders",
    "url": "https://arxiv.org/abs/2607.15057",
    "source": "Jin Choi, Kasper Larsen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T04:00:00+00:00",
    "summary": "arXiv:2607.15057v1 Announce Type: new Abstract: We extend the limited participation model in Basak and Cuoco (1998) to allow for traders with different time-preference coefficients but identical const"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.15168",
    "domain": "金融",
    "title": "Indirect Variational Inference: Applications to Earnings Dynamics",
    "url": "https://arxiv.org/abs/2607.15168",
    "source": "Neele Balke, Stephane Bonhomme, Thibaut Lamadon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T04:00:00+00:00",
    "summary": "arXiv:2607.15168v1 Announce Type: new Abstract: Latent-variable models are central to economics but often entail intractable integration. Variational inference (VI), widely used in machine learning, t"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.15195",
    "domain": "金融",
    "title": "SciPhy Reinforcement Learning for Portfolio Optimization",
    "url": "https://arxiv.org/abs/2607.15195",
    "source": "Igor Halperin, Andrey Itkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T04:00:00+00:00",
    "summary": "arXiv:2607.15195v1 Announce Type: new Abstract: This paper introduces a dynamic portfolio optimization framework for large institutional investors using Scientific Physics-Informed Reinforcement Learn"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.14361",
    "domain": "金融",
    "title": "NeuralChaos: Optimal Adapted Approximation of Square Integrable Predictable Processes",
    "url": "https://arxiv.org/abs/2607.14361",
    "source": "Anastasis Kratsios, Giulia Livieri, Philipp Schmocker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T04:00:00+00:00",
    "summary": "arXiv:2607.14361v1 Announce Type: cross Abstract: We address fundamental challenges in representing and computing $\\mathbb{R}^{d}$-valued predictable square-integrable processes over $[0,T]$, collecte"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.14518",
    "domain": "金融",
    "title": "Structure-Aware Variational State Preparation for Quantum Basket Option Pricing",
    "url": "https://arxiv.org/abs/2607.14518",
    "source": "Dongwoo Kim, Zhenyu Cui, Daniel K. Park, Chihoon Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T04:00:00+00:00",
    "summary": "arXiv:2607.14518v1 Announce Type: cross Abstract: Basket option pricing often relies on Monte Carlo estimation, for which quantum amplitude estimation (QAE) provides a quadratic speed-up. However, the"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.15119",
    "domain": "金融",
    "title": "Thermodynamic theory of voting and EU elections",
    "url": "https://arxiv.org/abs/2607.15119",
    "source": "Klaus M. Frahm, Dima L. Shepelyansky",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T04:00:00+00:00",
    "summary": "arXiv:2607.15119v1 Announce Type: cross Abstract: We introduce a thermodynamic theory of voting and show that it provides a good description of distribution of party votes in EU elections. The theory "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.15134",
    "domain": "金融",
    "title": "Platform Choice, Trust, and Privacy in the Consumer AI Assistant Market",
    "url": "https://arxiv.org/abs/2607.15134",
    "source": "Jennifer Zou",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T04:00:00+00:00",
    "summary": "arXiv:2607.15134v1 Announce Type: cross Abstract: We study how a representative sample of United States adult AI-assistant users (n=1,999; June 2026) choose among platforms, allocate tasks across them"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.07987",
    "domain": "金融",
    "title": "Automated Trading System for Straddle-Option Based on Deep Q-Learning",
    "url": "https://arxiv.org/abs/2509.07987",
    "source": "Yiran Wan, Xinyu Ying, Shengze Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T04:00:00+00:00",
    "summary": "arXiv:2509.07987v2 Announce Type: replace Abstract: Straddle Option is a financial trading tool that explores volatility premiums in high-volatility markets without predicting price direction. Althoug"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.26523",
    "domain": "金融",
    "title": "\"Rich-Get-Richer\"? Platform Attention and Earnings Inequality using Patreon Earnings Data",
    "url": "https://arxiv.org/abs/2509.26523",
    "source": "Ilan Strauss, Jangho Yang, Mariana Mazzucato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T04:00:00+00:00",
    "summary": "arXiv:2509.26523v3 Announce Type: replace Abstract: Using monthly Patreon earnings, we quantify how platform attention algorithms shape earnings concentration across creator economies. Patreon is a to"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.09564",
    "domain": "金融",
    "title": "Option prices from operational-time reaction-boundary lattices",
    "url": "https://arxiv.org/abs/2606.09564",
    "source": "Chris Angstmann, Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T04:00:00+00:00",
    "summary": "arXiv:2606.09564v4 Announce Type: replace Abstract: We consider the role of a continuum operational time $u$, its mapping to calendar time $t$, and their relation to event time in option-pricing probl"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.04103",
    "domain": "金融",
    "title": "Governing Generative AI Across Financial Institutions: A Framework for Generative AI Risk Control",
    "url": "https://arxiv.org/abs/2607.04103",
    "source": "Dennis Mao, Alessandra Lin, Yixin Kang, Yiqing Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T04:00:00+00:00",
    "summary": "arXiv:2607.04103v3 Announce Type: replace Abstract: Generative artificial intelligence is moving from general-purpose experimentation toward specialized applications across banking, capital markets, i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.12248",
    "domain": "金融",
    "title": "When Directional Accuracy Lies: A Base-Rate-Honest Benchmark for LoRA-Adapted TimesFM on Equity Forecasting",
    "url": "https://arxiv.org/abs/2607.12248",
    "source": "Taizhen Cheung",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T04:00:00+00:00",
    "summary": "arXiv:2607.12248v2 Announce Type: replace Abstract: Large pretrained time-series models such as TimesFM are attractive for financial forecasting, but raw directional accuracy is a misleading scoreboar"
  },
  {
    "id": "rss:https://arxiv.org/abs/2601.05050",
    "domain": "金融",
    "title": "Large language models can effectively convince people to believe conspiracies",
    "url": "https://arxiv.org/abs/2601.05050",
    "source": "Thomas H. Costello, Kellin Pelrine, Matthew Kowal, Jasper Timm, Antonio A. Arechar, Jean-Fran\\c{c}ois Godbout, Adam Gleave, David Rand, Gordon Pennycook",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T04:00:00+00:00",
    "summary": "arXiv:2601.05050v3 Announce Type: replace-cross Abstract: Large language models (LLMs) have been shown to be persuasive across a variety of contexts. But it remains unclear whether this persuasive pow"
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
    "id": "hn:48677039",
    "domain": "金融",
    "title": "The AI Data-Center Boom Is Sparking a Third Wave of Inflation",
    "url": "https://www.wsj.com/economy/the-data-center-boom-is-sparking-a-third-wave-of-inflation-926adc6e",
    "source": "gmays",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-06-25T17:58:44+00:00",
    "summary": ""
  }
]
```
