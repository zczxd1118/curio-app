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

- 今日日期：`2026-07-20`
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
  "date": "2026-07-20",
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
    "points": 3805852,
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
    "points": 1555384,
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
    "points": 1427399,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 985225,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV12omoB4ExF",
    "domain": "AI",
    "title": "黑马程序员全网最全Coze智能体入门到项目实战全套教程，从AI Agent开发入门到6大AI智能体实战项目，涵盖提示词Prompt、RAG、Bot发布微信公众号",
    "url": "http://www.bilibili.com/video/av115713129843205",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 978254,
    "published_at": "2025-12-15T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：251215\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\n人工智能开发热门教程：\nAI大模型开发：BV1h1V"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 917276,
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
    "points": 907628,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1mhKv68EPQ",
    "domain": "AI",
    "title": "豆包真能干活了！【豆包Agent入门教程】",
    "url": "http://www.bilibili.com/video/av116944258728161",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 499078,
    "published_at": "2026-07-19T03:00:00+00:00",
    "summary": "这个视频让你的豆包技能噌噌上涨，还有“秋芝AI科普skill”帮你答疑～\n感谢朋友们的三连+关注~"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 494990,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 409209,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 385603,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "domain": "AI",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 384194,
    "published_at": "2025-03-22T04:02:08+00:00",
    "summary": "很多人都想学编程,但被高门槛劝退。本期给大家介绍一款零门槛的AI编程工具-豆包电脑版。通过3个实战案例,带你体验如何用AI轻松实现编程。\n\n豆包电脑版特点:\n- 中文界面,所见即所得\n- 支持html代码预览\n- 支持Python运行\n- 可生成完整项目代码\n- 历史版本管理\n- 代码一键导出\n\n时间戳\n00:00 为什么要学AI编程\n03:19 案例1:图片压缩网站实战\n04:15 案例2:数据"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 303270,
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
    "points": 257153,
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
    "points": 194354,
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
    "points": 177460,
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
    "points": 162042,
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
    "points": 159974,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1b5AeeGEFc",
    "domain": "AI",
    "title": "Cursor太贵？分享三个免费AI编程方案+海量编程技巧【如何看待AI编程】",
    "url": "http://www.bilibili.com/video/av114025056699722",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 157859,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 148440,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 148345,
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
    "points": 141548,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 112562,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 96909,
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
    "points": 95167,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 92609,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 73799,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1GRKJ6fEgn",
    "domain": "AI",
    "title": "Kimi K3编程能力炸裂！在Claude Code中全方位实测代码能力，能否超越Fable 5和GPT-5.6l？结果远超我的预期！国产模型跻身世界第一梯队！",
    "url": "http://www.bilibili.com/video/av116934511239163",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 60681,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53165,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47423,
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
    "points": 43367,
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
    "points": 38630,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1cCj2ztEf5",
    "domain": "AI",
    "title": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%",
    "url": "http://www.bilibili.com/video/av114574527307727",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 34971,
    "published_at": "2025-05-26T14:20:15+00:00",
    "summary": "Cursor+Claude Code+Claude 4终极组合！仅用10分钟为开源项目Magentic-UI完美集成JWT用户认证系统，编程效率提升300%，告别传统开发模式！小白也能轻松开发商业项目\n\n🚀🚀🚀视频简介：\n✅【保姆级教程】从技术栈分析到功能实现：Claude Code完整开发流程深度解析！从零开始为微软开源智能体项目添加完整用户认证功能，支持注册登录退出，让你的AI应用瞬间变身多用"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 33863,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 28915,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1g6fdYcEes",
    "domain": "AI",
    "title": "Cursor从小白到专家-第19课：如何用Cursor开发安卓APP？",
    "url": "http://www.bilibili.com/video/av113888322524233",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 28796,
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
    "points": 27963,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV1vwXPYkEGx",
    "domain": "AI",
    "title": "Cursor+mcp配置，手把手教你配置任意MCP服务，学不会你打我，小白保姆级教程~MCP服务配置指南 - 提升AI编程助手能力",
    "url": "http://www.bilibili.com/video/av114193181183930",
    "source": "三少科技",
    "platform": "bilibili",
    "points": 27024,
    "published_at": "2025-03-20T05:51:23+00:00",
    "summary": "我的知识星球，https://t.zsxq.com/jVAk9\n\n📌 本期教程通过实战演示，教你在Cursor中配置和使用MCP服务器，特别是filesystem MCP服务，解决Cursor无法写入文件的常见问题。\n⏱️ 内容概要：\n00:00 介绍MCP及其重要性\n02:00 Cursor抽风问题与MCP解决方案\n04:00 配置第一个MCP服务器（filesystem）\n07:00 Wind"
  },
  {
    "id": "bvid:BV1RUDsBWEHb",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的Cursor+Skills实战指南教程，手把手带你开发爆款app，全程干货无废话！比付费效果强十倍！",
    "url": "http://www.bilibili.com/video/av116373464350785",
    "source": "AI大模型技术教程",
    "platform": "bilibili",
    "points": 26504,
    "published_at": "2026-04-09T10:15:00+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\nCursor+Skills频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 25441,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1pkK56aEVG",
    "domain": "AI",
    "title": "GPT-5.6在Claude Code中表现远超Codex | Theo - t3․gg",
    "url": "http://www.bilibili.com/video/av116929612221157",
    "source": "浮生千山路w",
    "platform": "bilibili",
    "points": 19936,
    "published_at": "2026-07-16T12:29:37+00:00",
    "summary": "来源：https://www.youtube.com/watch?v=Noo0NWD0gHU\n原标题：gpt 5.6 is way better in Claude Code\n频道：Theo - t3․gg\n发布时间：2026-07-16\n\n内容简介：\n作者使用GPT-5.6 Sol版本在Claude Code中进行编程，发现其表现相较于Codex有显著提升，体验令人震惊。视频由Coderabbi"
  },
  {
    "id": "bvid:BV1htCnY4ET6",
    "domain": "AI",
    "title": "用 Cursor AI 写 flutter 直接喂设计图就行 | flutter教程",
    "url": "http://www.bilibili.com/video/av113723805008238",
    "source": "独立开发者_猫哥",
    "platform": "bilibili",
    "points": 17861,
    "published_at": "2024-12-27T08:21:35+00:00",
    "summary": "✏️【关于本期视频】\n在上一篇文章《Flutter 使用 Cursor 和 Figma 快速生成界面代码》中，有同学提到他直接使用了设计稿的图片进行生成。我试了一下，效果确实很好。因此，我整理了一些文档，希望对大家有所帮助。\n下图展示了我没有手动编写任何代码实现的消息首页，支持上下滑动刷新数据。\n👉 文档 https://ducafecat.com/blog/use-cursor-ai-flutt"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17575,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 15699,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 15389,
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
    "points": 15263,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1spTy6DEb4",
    "domain": "AI",
    "title": "Claude code接管科研全流程：cc-kaiti 带你从 0 走到开题报告和答辩 PPT",
    "url": "http://www.bilibili.com/video/av116866278233889",
    "source": "做科研的大师兄",
    "platform": "bilibili",
    "points": 14953,
    "published_at": "2026-07-05T07:53:28+00:00",
    "summary": "十二年科研经验加持的课题开题Skill，从零开始到拿到一份完整的开题报告及开题PPT，仅需一天！\n\n本次视频分享的cc-kaiti这个skill文件及配套的资料包，在后台私我“cc开题”获取~"
  },
  {
    "id": "bvid:BV1etEQ6DETs",
    "domain": "AI",
    "title": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！",
    "url": "http://www.bilibili.com/video/av116724192118321",
    "source": "AI产品经理大模型",
    "platform": "bilibili",
    "points": 14127,
    "published_at": "2026-06-10T05:41:54+00:00",
    "summary": "【2026最新】目前B站最全最细的Vibe Coding全套系统教程，零代码也能直接上手！七天就能从小白到大神！少走99%的弯路！存下吧！很难找全的！"
  },
  {
    "id": "bvid:BV1UfTW6vEvT",
    "domain": "AI",
    "title": "6小时吃透Harness AI工程化编程｜ClaudeCode/Codex Vibe Coding 阿里企业 AI自动化实战，程序员AI编程开发效率提升十倍！",
    "url": "http://www.bilibili.com/video/av116855121385228",
    "source": "ai大模型应用开发实战",
    "platform": "bilibili",
    "points": 14033,
    "published_at": "2026-07-03T08:38:38+00:00",
    "summary": "课程资料看置顶第一条评论领取！"
  },
  {
    "id": "bvid:BV1ymNv6REs2",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent智能体零基础全套教程，2026最新版，从入门到实战！包含所有干货！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116922347686666",
    "source": "Agent智能体搭建-",
    "platform": "bilibili",
    "points": 12631,
    "published_at": "2026-07-15T05:35:41+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
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
    "points": 142,
    "published_at": "2026-07-14T08:24:49+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/creality-k2-se-3d-printer-price-slashed-by-17-percent-now-under-usd250-grab-a-competitive-entry-level-high-speed-multicolor-device-at-a-bargain-price",
    "domain": "AI 算力 / 半导体",
    "title": "Creality K2 SE 3D printer price slashed by 17%, now under $250 — grab a competitive entry-level high-speed multicolor device at a bargain price",
    "url": "https://www.tomshardware.com/pc-components/creality-k2-se-3d-printer-price-slashed-by-17-percent-now-under-usd250-grab-a-competitive-entry-level-high-speed-multicolor-device-at-a-bargain-price",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T15:04:07+00:00",
    "summary": "The Creality K2 SE drops to $248.99 in this limited-time deal, making it a great option for anyone looking to start 3D printing but want to have access to some advanced features."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-next-gen-10-core-medusa-point-apu-shows-up-on-geekbench-again-with-its-best-score-yet-leaked-sku-outpaces-every-other-x86-mobile-chip-in-the-single-core-test",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's next-gen 10-core 'Medusa Point' APU shows up on Geekbench again, with its best score yet — leaked SKU outpaces every other x86 mobile chip in the single-core test",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-next-gen-10-core-medusa-point-apu-shows-up-on-geekbench-again-with-its-best-score-yet-leaked-sku-outpaces-every-other-x86-mobile-chip-in-the-single-core-test",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T14:35:00+00:00",
    "summary": "AMD's next 10-core mobile part from the Medusa Point family is looking a lot faster than its previous two Gorgon Point and Strix Point SKUs, respectively. Early leaks keep highlighting an ever-improvi"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/zilog-z80-turns-50-as-open-source-replacement-heads-for-drop-in-dip40-silicon",
    "domain": "AI 算力 / 半导体",
    "title": "Zilog Z80 turns 50 as an open-source replacement heads to drop-in DIP40 silicon — iconic 8-bit CPU launched in July 1976 and was discontinued in 2024",
    "url": "https://www.tomshardware.com/tech-industry/zilog-z80-turns-50-as-open-source-replacement-heads-for-drop-in-dip40-silicon",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T14:12:55+00:00",
    "summary": "The original Z80 packed 8,500 transistors on a 4μm process and typically ran at 2.5 MHz."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/memory-chip-boss-admits-ram-prices-are-abnormally-high-sk-group-chairman-considering-building-a-semiconductor-plant-in-the-us-to-expand-supply-calm-chipflation",
    "domain": "AI 算力 / 半导体",
    "title": "Memory chip boss admits RAM prices are 'abnormally high' — SK Group chairman considering building a semiconductor plant in the US to expand supply, calm ‘chipflation’",
    "url": "https://www.tomshardware.com/tech-industry/policy/memory-chip-boss-admits-ram-prices-are-abnormally-high-sk-group-chairman-considering-building-a-semiconductor-plant-in-the-us-to-expand-supply-calm-chipflation",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T13:55:00+00:00",
    "summary": "SK Group Chairman Chey Tae-won said that prices for memory chips are \"abnormally high\" and that the industry must take steps to increase production and reduce prices. If it fails to do that, new entra"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/phantom-twist-drone-spins-so-fast-that-it-is-nearly-invisible-flying-device-adds-motion-blur-to-the-real-world",
    "domain": "AI 算力 / 半导体",
    "title": "‘Phantom Twist’ drone spins so fast that it is nearly invisible — flying device adds motion blur to the real world",
    "url": "https://www.tomshardware.com/tech-industry/drones/phantom-twist-drone-spins-so-fast-that-it-is-nearly-invisible-flying-device-adds-motion-blur-to-the-real-world",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T13:27:34+00:00",
    "summary": "Researchers from Northwestern University in Illinois have built a drone that rotates so fast it is cloaked by motion blur."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/samsung-cuts-hundreds-of-us-consumer-electronics-jobs-ahead-of-texas-hq-move",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung cuts hundreds of US consumer electronics jobs ahead of Texas HQ move — 739 roles affected in New Jersey as chip division posts record profit",
    "url": "https://www.tomshardware.com/tech-industry/samsung-cuts-hundreds-of-us-consumer-electronics-jobs-ahead-of-texas-hq-move",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T12:48:01+00:00",
    "summary": "Samsung told Reuters that a majority of the affected New Jersey employees received relocation offers, while others were let go."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/russian-drones-spotted-using-screwed-on-magnetic-compasses-as-navigation-aids-the-on-board-camera-can-occasionally-tilt-down-to-check-bearings-if-satellite-comms-are-lost",
    "domain": "AI 算力 / 半导体",
    "title": "Russian drones spotted using screwed-on magnetic compasses as navigation aids — the on-board camera can occasionally tilt down to check bearings if satellite comms are lost",
    "url": "https://www.tomshardware.com/tech-industry/drones/russian-drones-spotted-using-screwed-on-magnetic-compasses-as-navigation-aids-the-on-board-camera-can-occasionally-tilt-down-to-check-bearings-if-satellite-comms-are-lost",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T12:05:34+00:00",
    "summary": "Russian drone troops are adding cheap magnetic compasses to help find their bearings. Crude add-on helps them find their bearings and locate their targets even without GPS."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/coil-whine-can-be-musical-demonstrates-engineering-student-this-usually-hated-noise-can-make-some-people-happy",
    "domain": "AI 算力 / 半导体",
    "title": "Coil whine can be musical, demonstrates engineering student — this usually hated noise can make some people happy",
    "url": "https://www.tomshardware.com/pc-components/coil-whine-can-be-musical-demonstrates-engineering-student-this-usually-hated-noise-can-make-some-people-happy",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T11:20:34+00:00",
    "summary": "Video shows that electronic noise pollution can become music."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/crazed-enthusiast-runs-pc-on-192-aa-batteries-successfully-boots-into-hannah-montana-linux-system-is-stable-during-stress-testing-and-even-plays-freedoom",
    "domain": "AI 算力 / 半导体",
    "title": "Crazed enthusiast runs PC on 192 AA batteries, successfully boots into Hannah Montana Linux — System is stable during stress testing and even plays FreeDoom",
    "url": "https://www.tomshardware.com/desktops/pc-building/crazed-enthusiast-runs-pc-on-192-aa-batteries-successfully-boots-into-hannah-montana-linux-system-is-stable-during-stress-testing-and-even-plays-freedoom",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T10:00:00+00:00",
    "summary": "A creator by the name of \"Uwoslab\" just jerry-rigged three battery banks together, each made up of 64 AA Alkaline cells, to form a giant 192-cell array that's enough to power an AM4 system."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/clever-hacker-fits-537-000-domains-in-a-tiny-usd5-esp32-ad-blocking-dongle-firmware-uses-only-around-50kb-of-ram-and-can-answer-blocked-lookups-in-10-milliseconds",
    "domain": "AI 算力 / 半导体",
    "title": "Clever hacker fits 537,000 domains in a tiny $5 ESP32 ad-blocking dongle — firmware uses only around 50KB of RAM and can answer blocked lookups in 10 milliseconds",
    "url": "https://www.tomshardware.com/networking/clever-hacker-fits-537-000-domains-in-a-tiny-usd5-esp32-ad-blocking-dongle-firmware-uses-only-around-50kb-of-ram-and-can-answer-blocked-lookups-in-10-milliseconds",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T10:00:00+00:00",
    "summary": "This project uses a clever hashing trick to fit over half a million blocked domains into just 4MB of flash memory."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/gta-3-and-vice-city-are-now-playable-inside-san-andreas-a-mod-lets-you-revisit-liberty-city-and-vice-city-without-leaving-san-andreas",
    "domain": "AI 算力 / 半导体",
    "title": "GTA 3 and Vice City are now playable inside San Andreas — a mod lets you revisit Liberty City and Vice City without leaving San Andreas",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/gta-3-and-vice-city-are-now-playable-inside-san-andreas-a-mod-lets-you-revisit-liberty-city-and-vice-city-without-leaving-san-andreas",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T17:48:22+00:00",
    "summary": "A GTA modder has embedded GTA 3 and Vice City within San Andreas, even nesting Vice City within GTA 3, with all three games continuing to run simultaneously."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amds-new-ryzen-7-7700x3d-plummets-to-usd279-days-after-launch-the-x3d-chip-rules-the-mid-range-at-its-discounted-price",
    "domain": "AI 算力 / 半导体",
    "title": "AMD’s new Ryzen 7 7700X3D plummets to $279 days after launch — the X3D chip rules the mid-range at its discounted price",
    "url": "https://www.tomshardware.com/pc-components/cpus/amds-new-ryzen-7-7700x3d-plummets-to-usd279-days-after-launch-the-x3d-chip-rules-the-mid-range-at-its-discounted-price",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T17:40:13+00:00",
    "summary": "The Ryzen 7 7700X3D has suddenly become a solid value thanks to a $50 promo code, knocking its price down from $329 to just $279 on Newegg."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/strapping-11-fans-and-a-360mm-aio-to-an-rtx-3080-sounds-crazy-until-you-see-the-30-c-temp-drop-modded-gpu-delivered-less-than-5-fps-uplift",
    "domain": "AI 算力 / 半导体",
    "title": "Strapping 11 fans and a 360mm AIO to an RTX 3080 sounds crazy until you see the 30°C temp drop — modded GPU delivered less than 5 FPS uplift at turbojet noise levels",
    "url": "https://www.tomshardware.com/pc-components/cooling/strapping-11-fans-and-a-360mm-aio-to-an-rtx-3080-sounds-crazy-until-you-see-the-30-c-temp-drop-modded-gpu-delivered-less-than-5-fps-uplift",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T17:22:49+00:00",
    "summary": "TrashBench recently decided to test whether adding more and more fans to a powerful GPU would improve its performance."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/jurassic-park-packed-usd4-million-of-legit-1993-computer-hardware-a-software-engineer-detailed-every-single-piece-of-hardware-in-the-film",
    "domain": "AI 算力 / 半导体",
    "title": "Jurassic Park packed $4 million of legit 1993 computer hardware — a software engineer detailed every single piece of hardware in the film",
    "url": "https://www.tomshardware.com/desktops/jurassic-park-packed-usd4-million-of-legit-1993-computer-hardware-a-software-engineer-detailed-every-single-piece-of-hardware-in-the-film",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T17:12:53+00:00",
    "summary": "Google software engineer Fabien Sanglard meticulously listed the computer hardware and software used in the first Jurassic Park film. He even added details for each device, turning the film into somet"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/grab-amds-ryzen-7-5800x3d-10th-anniversary-cpu-with-motherboard-and-16gb-ram-for-just-usd529-save-over-usd100-on-this-epic-amd-gaming-bundle",
    "domain": "AI 算力 / 半导体",
    "title": "Grab AMD’s Ryzen 7 5800X3D 10th Anniversary CPU with motherboard and 16GB RAM for just $529 — save over $100 on this epic AMD gaming bundle",
    "url": "https://www.tomshardware.com/pc-components/cpus/grab-amds-ryzen-7-5800x3d-10th-anniversary-cpu-with-motherboard-and-16gb-ram-for-just-usd529-save-over-usd100-on-this-epic-amd-gaming-bundle",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T15:19:27+00:00",
    "summary": "Newegg has a great combo bundle on sale with over $100 in savings for the fastest DDR4 gaming system you can build today. It pairs a Ryzen 7 5800X3D with 16GB of CL16 DDR4-3200 RAM and an Asus TUF Gam"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-50-super-gpus-are-reportedly-ready-but-stuck-in-limbo-due-to-excessive-gddr7-pricing-3gb-gddr7-module-costs-triple-the-price-of-2gb",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX 50 Super GPUs are reportedly ready, but stuck in limbo due to excessive GDDR7 pricing — 3GB GDDR7 module costs triple the price of 2GB",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-50-super-gpus-are-reportedly-ready-but-stuck-in-limbo-due-to-excessive-gddr7-pricing-3gb-gddr7-module-costs-triple-the-price-of-2gb",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T13:45:42+00:00",
    "summary": "The 3GB GDDR7 chips that the RTX 50 Super GPUs will use reportedly cost twice to thrice as much as the 2GB chips found on vanilla RTX 50-series graphics cards. This would likely push the retail price "
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/wearable-tech/nvidia-ceo-jensen-huangs-trademark-leather-jacket-raises-nearly-usd1-million-at-charity-auction-bidding-makes-usd60-000-valuation-look-like-pocket-change",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang’s trademark leather jacket raises nearly $1 Million at charity auction — bidding makes $60,000 valuation look like pocket change",
    "url": "https://www.tomshardware.com/peripherals/wearable-tech/nvidia-ceo-jensen-huangs-trademark-leather-jacket-raises-nearly-usd1-million-at-charity-auction-bidding-makes-usd60-000-valuation-look-like-pocket-change",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T13:22:12+00:00",
    "summary": "‘The Jensen Jacket’ achieved a hammer price of $960,000 this weekend."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/security-engineer-ports-password-cracker-hashcat-to-gameboy-advance-16-8-mhz-chip-can-perform-a-meager-727-hashes-a-second-30-million-times-slower-than-a-modern-rig",
    "domain": "AI 算力 / 半导体",
    "title": "Security engineer ports password cracker hashcat to Gameboy Advance — 16.8 MHz chip can perform a meager 727 hashes a second, 30 million times slower than a modern rig",
    "url": "https://www.tomshardware.com/video-games/nintendo/security-engineer-ports-password-cracker-hashcat-to-gameboy-advance-16-8-mhz-chip-can-perform-a-meager-727-hashes-a-second-30-million-times-slower-than-a-modern-rig",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T11:30:00+00:00",
    "summary": "Gameboy Advance port of hashcat allows for advanced password cracking in meager hardware — so long as you're willing to wait"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/agi-ai828-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "AGI AI828 SSD Review: A near-last resort for those on a budget",
    "url": "https://www.tomshardware.com/pc-components/ssds/agi-ai828-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T11:10:00+00:00",
    "summary": "The AGI AI828 is a budget drive with subpar performance and power efficiency. This makes it a last resort, although in the current market, it might be good enough for some."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/korean-outfit-hosting-1-44mb-game-development-contest-to-honor-the-floppy-disk-entrants-must-confine-entire-fileset-including-resources-engine-and-library-to-miniscule-storage-format",
    "domain": "AI 算力 / 半导体",
    "title": "Korean outfit hosting 1.44MB game development contest to honor the floppy disk — entrants must confine entire fileset, including resources, engine, and library, to miniscule storage format",
    "url": "https://www.tomshardware.com/software/korean-outfit-hosting-1-44mb-game-development-contest-to-honor-the-floppy-disk-entrants-must-confine-entire-fileset-including-resources-engine-and-library-to-miniscule-storage-format",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T11:00:00+00:00",
    "summary": "There’s a new 'open to everyone' floppy disk-size game development competition with cash prizes for the best three submissions."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/autonomous-micro-drone-achieves-first-air-to-air-insect-kill-on-the-way-towards-completely-eradicating-mosquitoes-40-gram-unit-uses-car-parking-sensors-can-eliminate-insects-at-up-to-26-feet",
    "domain": "AI 算力 / 半导体",
    "title": "Autonomous micro-drone achieves first air-to-air insect kill on the way 'towards completely eradicating mosquitoes' — 40-gram unit uses car parking sensors, can eliminate insects at up to 26 feet",
    "url": "https://www.tomshardware.com/tech-industry/drones/autonomous-micro-drone-achieves-first-air-to-air-insect-kill-on-the-way-towards-completely-eradicating-mosquitoes-40-gram-unit-uses-car-parking-sensors-can-eliminate-insects-at-up-to-26-feet",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T09:00:00+00:00",
    "summary": "A micro-drone designed to locate and eradicate mosquitoes has passed an important milestone with its first recorded air-to-air kill."
  },
  {
    "id": "rss:https://www.eetimes.com/new-material-beats-coppers-thermal-conductivity/",
    "domain": "AI 算力 / 半导体",
    "title": "New Material Beats Copper’s Thermal Conductivity",
    "url": "https://www.eetimes.com/new-material-beats-coppers-thermal-conductivity/",
    "source": "Bill Schweber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T19:00:00+00:00",
    "summary": "Meet θ-TaN, a metal that moves heat nearly 3× better than copper—and could upend chip cooling layers. The post New Material Beats Copper’s Thermal Conductivity appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/asml-raises-outlook-plans-more-euv-capacity/",
    "domain": "AI 算力 / 半导体",
    "title": "ASML Raises Outlook, Plans More EUV Capacity",
    "url": "https://www.eetimes.com/asml-raises-outlook-plans-more-euv-capacity/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T14:00:00+00:00",
    "summary": "ASML raised its full-year outlook as AI demand prompted plans to expand lithography capacity through at least 2028. The post ASML Raises Outlook, Plans More EUV Capacity appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/tsmc-boosts-2026-expansion-budget-adds-100b-to-u-s-investment/",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Boosts 2026 Expansion Budget, Adds $100B to U.S. Investment",
    "url": "https://www.eetimes.com/tsmc-boosts-2026-expansion-budget-adds-100b-to-u-s-investment/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T05:55:59+00:00",
    "summary": "TSMC is raising its 2026 capital budget to $64 billion and adding $100 billion to its U.S. investment for AI. The post TSMC Boosts 2026 Expansion Budget, Adds $100B to U.S. Investment appeared first o"
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
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/asmls-planned-low-na-euv-machine-price-hikes-reportedly-frustrate-tsmc-lithography-machine-maker-comes-knocking-to-make-bank-on-tsmcs-profitable-fabs-potentially-costing-the-taiwanese-chipmaker-billions",
    "domain": "AI 算力 / 半导体",
    "title": "ASML's planned Low-NA EUV machine price hikes reportedly frustrate TSMC — lithography machine maker comes knocking to make bank on TSMC's profitable fabs, potentially costing the Taiwanese chipmaker b",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asmls-planned-low-na-euv-machine-price-hikes-reportedly-frustrate-tsmc-lithography-machine-maker-comes-knocking-to-make-bank-on-tsmcs-profitable-fabs-potentially-costing-the-taiwanese-chipmaker-billions",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T15:57:16+00:00",
    "summary": "ASML says that the increased productivity of its Low-NA EUV tools gives it an option to increase the prices of these scanners in the future. The move may have a drastic effect on TSMC's future expansi"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tsmc-confirms-significant-yield-and-performance-improvements-in-a14-update-strong-interest-from-ai-hpc-and-smartphone-customers",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC confirms significant yield and performance improvements in A14 update — strong interest from AI/HPC and smartphone customers",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-confirms-significant-yield-and-performance-improvements-in-a14-update-strong-interest-from-ai-hpc-and-smartphone-customers",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T15:30:26+00:00",
    "summary": "TSMC's A14 process technology progresses faster than N2 at this stage of development as developers of both client and AI/HPC plan to use it."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/fbi-arrests-florida-man-in-steam-malware-investigaton-after-tracing-stolen-bitcoin-to-uber-eats-gift-cards",
    "domain": "AI 算力 / 半导体",
    "title": "Florida man arrested after allegedly stealing $220,000 in crypto using malware hidden in Steam Games — 8,000 devices infected",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/fbi-arrests-florida-man-in-steam-malware-investigaton-after-tracing-stolen-bitcoin-to-uber-eats-gift-cards",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T14:43:21+00:00",
    "summary": "Federal agents arrested 21-year-old Zyaire Dontaevious Zamarion Wilkins of North Lauderdale, Florida, on Tuesday."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/best-back-to-school-tech-deals-on-laptops-and-essential-tech-save-on-new-semester-essentials-now",
    "domain": "AI 算力 / 半导体",
    "title": "Best Back to School tech deals on laptops and essential tech — save on new semester essentials now",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/best-back-to-school-tech-deals-on-laptops-and-essential-tech-save-on-new-semester-essentials-now",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T14:29:45+00:00",
    "summary": "Grab savings on the best back-to-school tech deals."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/gamestop-ceo-says-sonys-decision-to-go-disc-less-is-totally-irrelevant-claims-software-including-physical-discs-accounts-for-only-12-percent-of-the-companys-business",
    "domain": "AI 算力 / 半导体",
    "title": "GameStop CEO says Sony's decision to go disc-less is 'totally irrelevant' — claims software, including physical discs, accounts for only 12% of the company's business",
    "url": "https://www.tomshardware.com/video-games/console-gaming/gamestop-ceo-says-sonys-decision-to-go-disc-less-is-totally-irrelevant-claims-software-including-physical-discs-accounts-for-only-12-percent-of-the-companys-business",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T13:51:39+00:00",
    "summary": "GameStop CEO Ryan Cohen says Sony’s physical game exit is irrelevant to the company's business, amid a $56 billion eBay takeover, as collectibles now drive growth."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/lawmakers-want-us-government-to-ban-memory-chips-from-china-even-in-allied-supply-chains-citing-unacceptable-risk-to-national-economic-and-supply-chain-security",
    "domain": "AI 算力 / 半导体",
    "title": "Lawmakers want US government to ban memory chips from China, even in allied supply chains — citing 'unacceptable risk' to national, economic, and supply chain security",
    "url": "https://www.tomshardware.com/pc-components/dram/lawmakers-want-us-government-to-ban-memory-chips-from-china-even-in-allied-supply-chains-citing-unacceptable-risk-to-national-economic-and-supply-chain-security",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T13:05:44+00:00",
    "summary": "U.S. lawmakers demand Commerce Secretary Howard Lutnick to ban imports of memory chips from China to the U.S., ask allies to do the same."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/ai-data-centers-must-produce-as-much-power-as-they-use-australia-pm-says-new-national-ai-framework-will-also-ensure-water-efficiency-and-protect-intellectual-property-rights",
    "domain": "AI 算力 / 半导体",
    "title": "AI data centers must produce as much power as they use, Australia PM says — new national AI framework will also ensure water efficiency and protect intellectual property rights",
    "url": "https://www.tomshardware.com/tech-industry/policy/ai-data-centers-must-produce-as-much-power-as-they-use-australia-pm-says-new-national-ai-framework-will-also-ensure-water-efficiency-and-protect-intellectual-property-rights",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T12:16:03+00:00",
    "summary": "Australian Prime Minister Anthony Albanese announced the \"Australian Standards for A.I.,\" which will serve as a national framework for data center developments related to AI. The government plans to s"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-nova-lake-leak-points-to-core-ultra-series-400-branding-staggered-release-next-year-hotly-anticipated-flagship-52-core-desktop-cpu-might-not-arrive-until-late-2027",
    "domain": "AI 算力 / 半导体",
    "title": "Intel Nova Lake leak points to Core Ultra Series 400 branding, staggered release next year — hotly anticipated flagship 52-core desktop CPU might not arrive until late 2027",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-nova-lake-leak-points-to-core-ultra-series-400-branding-staggered-release-next-year-hotly-anticipated-flagship-52-core-desktop-cpu-might-not-arrive-until-late-2027",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T12:08:13+00:00",
    "summary": "Intel's upcoming Nova Lake desktop processors continue to gather momentum, with fresh reports hinting at Core Ultra Series 400 branding and a phased launch timeline."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3",
    "domain": "AI 算力 / 半导体",
    "title": "China's 2.8-trillion-parameter Kimi K3 beats Claude Fable 5 in Frontend Code Arena benchmark— Moonshot AI delivers largest open-weight AI model ever, as China works around U.S. compute limits",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-17T11:32:01+00:00",
    "summary": "Beijing-based Moonshot AI has released Kimi K3, a 2.8 trillion parameter model that the company describes in its technical blog as the world's first open 3T-class system."
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
    "id": "hn:48925271",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://turntrout.com/why-i-left-google-deepmind",
    "source": "apsec112",
    "platform": "hackernews",
    "points": 364,
    "published_at": "2026-07-15T18:40:34+00:00",
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
    "id": "hn:48965880",
    "domain": "大厂 AI 动态",
    "title": "Ollama: All Aboard Open Models",
    "url": "https://ollama.com/blog/all-aboard-open-models",
    "source": "inferhaven",
    "platform": "hackernews",
    "points": 132,
    "published_at": "2026-07-19T07:59:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48959297",
    "domain": "大厂 AI 动态",
    "title": "Our Approach to Bioresilience: Isomorphic Labs and Google DeepMind",
    "url": "https://deepmind.google/blog/our-approach-to-bioresilience/",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-07-18T16:02:45+00:00",
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
    "id": "hn:48965012",
    "domain": "大厂 AI 动态",
    "title": "Google's Gemini delay: Coding stumbles, clashing teams and frustrated engineers",
    "url": "https://www.latimes.com/business/story/2026-07-17/inside-googles-gemini-delay-coding-stumbles-clashing-teams-frustrated-engineers",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-07-19T04:35:08+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/967696/four-tet-wingdings-album-review",
    "domain": "大厂 AI 动态",
    "title": "This unpronounceable series of glyphs is an incredible side project from Kieran Hebden (aka Four Tet)",
    "url": "https://www.theverge.com/entertainment/967696/four-tet-wingdings-album-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T21:02:45+00:00",
    "summary": "Just why? &#645;&#865;&#865;&#865;&#865;&#865;&#865;&#865;&#865;&#865;&#865;&#865;(&#824;&#802;&#795;&#828;&#798;&#813;&#843;&#837;)&#824;&#858;&#816;&#859;&#788;&#830;&#768;&#831;&#850;&#834;:&#820;&"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/967687/kodak-ec35-point-and-shoot-film-camera",
    "domain": "大厂 AI 动态",
    "title": "Kodak EC35 is a dirt-cheap point-and-shoot film camera",
    "url": "https://www.theverge.com/gadgets/967687/kodak-ec35-point-and-shoot-film-camera",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T19:26:06+00:00",
    "summary": "Following the success of its $99 Kodak-branded Snapic A1, Reto Project is releasing the Kodak EC35, an even more affordable 35mm film camera for just $34.99. The EC35 certainly isn't fancy. Its 25mm a"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/967678/1010benja-semiramis-dream-suno-ai-music",
    "domain": "大厂 AI 动态",
    "title": "I hate that I don’t hate this song made with Suno",
    "url": "https://www.theverge.com/entertainment/967678/1010benja-semiramis-dream-suno-ai-music",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T17:35:54+00:00",
    "summary": "I would never go so far as to say there's no place for AI in music (I'm a fan of Holly Herndon, after all). But I generally find music made with generative AI to be offensively boring, especially the "
  },
  {
    "id": "rss:https://www.theverge.com/policy/967674/fbi-wont-investigate-ice-assaults",
    "domain": "大厂 AI 动态",
    "title": "The FBI reportedly won’t investigate ICE anymore",
    "url": "https://www.theverge.com/policy/967674/fbi-wont-investigate-ice-assaults",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T16:42:10+00:00",
    "summary": "According to the New York Times, federal agents have been told that the FBI will no longer be investigating confrontations involving ICE agents. The DHS and DOJ denied the change in policy to The Time"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/967485/telepathic-instruments-orchid-tame-impala-synth-review",
    "domain": "大厂 AI 动态",
    "title": "Orchid is a delightfully retro and approachable hipster synth",
    "url": "https://www.theverge.com/entertainment/967485/telepathic-instruments-orchid-tame-impala-synth-review",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T15:15:00+00:00",
    "summary": "In 2017, I bought an old Magnus chord organ off Craigslist for $10. It's one of my favorite music gear purchases. Electric chord organs let you play full chords with just a press of a button, making t"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/967336/birdfy-feeder-ai-powered-smart-bird-feeder-with-camera-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Birdfy&#8217;s solar-powered smart feeder is down to one of its best prices",
    "url": "https://www.theverge.com/gadgets/967336/birdfy-feeder-ai-powered-smart-bird-feeder-with-camera-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T15:00:00+00:00",
    "summary": "Birdfy has kicked off a midyear sale, taking up to 40 percent off a range of its smart bird feeders. One of the best deals is on Netvue’s Birdfy Feeder AI-Powered Smart Bird Feeder with Camera, which "
  },
  {
    "id": "rss:https://www.theverge.com/policy/967651/us-marshals-arrest-the-tate-brothers-in-miami",
    "domain": "大厂 AI 动态",
    "title": "US Marshals arrest the Tate brothers in Miami",
    "url": "https://www.theverge.com/policy/967651/us-marshals-arrest-the-tate-brothers-in-miami",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T14:20:48+00:00",
    "summary": "The manosphere influencers Andrew and Tristan Tate were arrested Saturday in Miami by US Marshals in relation to new rape and sex trafficking charges in England. According to the Associated Press, Bri"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/967642/the-clapper-version-history",
    "domain": "大厂 AI 动态",
    "title": "The Clapper was a bad smart home gadget — and a viral sensation",
    "url": "https://www.theverge.com/podcast/967642/the-clapper-version-history",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T13:28:26+00:00",
    "summary": "Clap on. Clap off. Well, more like, Clap, pause for half a beat but no longer because otherwise it'll stop hearing you, clap again because you waited too long, clap louder and faster, that didn't work"
  },
  {
    "id": "rss:https://www.theverge.com/column/967179/physical-discs-gta-vi-playstation-rockstar-games",
    "domain": "大厂 AI 动态",
    "title": "The future of physical games is not looking great",
    "url": "https://www.theverge.com/column/967179/physical-discs-gta-vi-playstation-rockstar-games",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T12:00:00+00:00",
    "summary": "This is The Stepback, a weekly newsletter breaking down one essential story from the tech world. For more on video games and physical media, follow Jay Peters. The Stepback arrives in our subscribers'"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/966701/solar-car-challenge-high-school-student-race-texas",
    "domain": "大厂 AI 动态",
    "title": "The grueling, 630-mile road race where the only fuel is sunlight",
    "url": "https://www.theverge.com/transportation/966701/solar-car-challenge-high-school-student-race-texas",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T11:00:00+00:00",
    "summary": "On July 19th, dozens of teams of high school students will begin a five-day, 630-mile road race from Fort Worth to Fort Stockton in Texas. But this is not your typical contest. The students design and"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/19/netflix-paid-587m-for-ben-afflecks-ai-filmmaking-startup/",
    "domain": "大厂 AI 动态",
    "title": "Netflix paid $587M for Ben Affleck’s AI filmmaking startup",
    "url": "https://techcrunch.com/2026/07/19/netflix-paid-587m-for-ben-afflecks-ai-filmmaking-startup/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T21:45:00+00:00",
    "summary": "Netflix revealed that it paid $587 million in cash for InterPositive, a startup co-founded by Ben Affleck."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/19/what-to-watch-for-after-jensen-huangs-japan-visit/",
    "domain": "大厂 AI 动态",
    "title": "What to watch for after Jensen Huang’s Japan visit",
    "url": "https://techcrunch.com/2026/07/19/what-to-watch-for-after-jensen-huangs-japan-visit/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T21:16:07+00:00",
    "summary": "Jensen Huang left Tokyo with deals spanning Japan's entire tech ecosystem."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/19/can-an-apple-lawsuit-derail-openais-hardware-plans/",
    "domain": "大厂 AI 动态",
    "title": "Can an Apple lawsuit derail OpenAI’s hardware plans?",
    "url": "https://techcrunch.com/2026/07/19/can-an-apple-lawsuit-derail-openais-hardware-plans/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T19:24:45+00:00",
    "summary": "On the latest episode of Equity, we debate whether Apple's lawsuit will cast over OpenAi's much-discussed plans to get into hardware and go public."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/19/techcrunch-mobility-the-battle-over-robotaxi-rules/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: The battle over robotaxi rules",
    "url": "https://techcrunch.com/2026/07/19/techcrunch-mobility-the-battle-over-robotaxi-rules/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T16:05:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, how AI is playing a part."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/19/odyssey-director-christopher-nolan-calls-ai-an-obvious-trojan-horse/",
    "domain": "大厂 AI 动态",
    "title": "‘Odyssey’ director Christopher Nolan calls AI an obvious ‘Trojan horse’",
    "url": "https://techcrunch.com/2026/07/19/odyssey-director-christopher-nolan-calls-ai-an-obvious-trojan-horse/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T14:52:08+00:00",
    "summary": "\"Everybody knows the Greeks are inside.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/19/nonprofit-current-ai-is-racing-to-build-the-world-wide-web-of-ai-free-for-all/",
    "domain": "大厂 AI 动态",
    "title": "Nonprofit Current AI is racing to build the World Wide Web of AI, free for all",
    "url": "https://techcrunch.com/2026/07/19/nonprofit-current-ai-is-racing-to-build-the-world-wide-web-of-ai-free-for-all/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T14:00:00+00:00",
    "summary": "Current AI, a non-profit building AI that leaves no one culture behind, has made remarkable progress across devices, AI chat and more."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/18/waymo-appears-to-pause-san-francisco-service-amidst-power-outage/",
    "domain": "大厂 AI 动态",
    "title": "Waymo says San Francisco service has resumed after one-hour pause",
    "url": "https://techcrunch.com/2026/07/18/waymo-appears-to-pause-san-francisco-service-amidst-power-outage/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T19:30:23+00:00",
    "summary": "This isn’t the first time power outages have caused issues for Waymo."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/18/kimi-threat-or-menace/",
    "domain": "大厂 AI 动态",
    "title": "Kimi: Threat or menace?",
    "url": "https://techcrunch.com/2026/07/18/kimi-threat-or-menace/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T18:51:07+00:00",
    "summary": "Chinese company Moonshot AI released a new version of its Kimi model this week, prompting concern about \"full AI communism.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/18/all-the-evs-that-were-discontinued-or-killed-off-in-the-u-s-this-year/",
    "domain": "大厂 AI 动态",
    "title": "All the EVs that were discontinued or killed off in the U.S. this year",
    "url": "https://techcrunch.com/2026/07/18/all-the-evs-that-were-discontinued-or-killed-off-in-the-u-s-this-year/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T16:30:00+00:00",
    "summary": "Th Honda Prologue will no longer be sold in the U.S., joining a growing list of EV models to exit the market this year."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/18/federal-employees-can-download-tiktok-on-their-work-phones-again/",
    "domain": "大厂 AI 动态",
    "title": "Federal employees can download TikTok on their work phones again",
    "url": "https://techcrunch.com/2026/07/18/federal-employees-can-download-tiktok-on-their-work-phones-again/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T15:54:24+00:00",
    "summary": "The Department of Justice says that federal employees can now download TikTok on their government devices."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/18/a-600-mile-road-trip-and-data-proves-ev-charging-doesnt-suck-anymore/",
    "domain": "大厂 AI 动态",
    "title": "A 600-mile road trip (and data) proves EV charging doesn’t suck anymore",
    "url": "https://techcrunch.com/2026/07/18/a-600-mile-road-trip-and-data-proves-ev-charging-doesnt-suck-anymore/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T14:32:00+00:00",
    "summary": "A recent road trip in an EV revealed just how much faster and more reliable DC Fast charging has become in the U.S."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/07/indias-first-privately-developed-rocket-reaches-orbit-on-dramatic-debut-launch/",
    "domain": "大厂 AI 动态",
    "title": "India's first privately-developed rocket reaches orbit on dramatic debut launch",
    "url": "https://arstechnica.com/space/2026/07/indias-first-privately-developed-rocket-reaches-orbit-on-dramatic-debut-launch/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T22:11:21+00:00",
    "summary": "\"On the first attempt, reaching orbit, I never thought it was possible.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/as-mosquito-ranges-expand-better-monitoring-is-key-to-preventing-disease/",
    "domain": "大厂 AI 动态",
    "title": "As mosquito ranges expand, better monitoring is key to preventing disease",
    "url": "https://arstechnica.com/science/2026/07/as-mosquito-ranges-expand-better-monitoring-is-key-to-preventing-disease/",
    "source": "Madeline Shaw, Inside Climate News",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T11:19:31+00:00",
    "summary": "Monitoring is expensive and labor intensive. But it helps public health officials stop outbreaks."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/07/will-ai-fix-prior-authorization-or-make-it-worse/",
    "domain": "大厂 AI 动态",
    "title": "Will AI fix prior authorization—or make it worse?",
    "url": "https://arstechnica.com/ai/2026/07/will-ai-fix-prior-authorization-or-make-it-worse/",
    "source": "Joshua Cohen, Undark Magazine",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T11:18:25+00:00",
    "summary": "The government is piloting a program that uses AI for insurance-coverage decisions."
  },
  {
    "id": "rss:https://www.producthunt.com/products/rewisp-an-ambient-memory-for-your-mac",
    "domain": "大厂 AI 动态",
    "title": "Rewisp",
    "url": "https://www.producthunt.com/products/rewisp-an-ambient-memory-for-your-mac",
    "source": "Yashmit Bhaverisetti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T11:45:09+00:00",
    "summary": "See it once. Ask forever. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/basert",
    "domain": "大厂 AI 动态",
    "title": "BaseRT",
    "url": "https://www.producthunt.com/products/basert",
    "source": "Lukas Wesemann",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T08:15:22+00:00",
    "summary": "6.4x faster than llama.cpp, 3.9x faster than MLX Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/detourmap",
    "domain": "大厂 AI 动态",
    "title": "Detourmap",
    "url": "https://www.producthunt.com/products/detourmap",
    "source": "Albanius",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-18T09:27:10+00:00",
    "summary": "Every place worth the detour, on one interactive map Discussion | Link"
  },
  {
    "id": "rss:https://36kr.com/p/3902068392658566?f=rss",
    "domain": "大厂 AI 动态",
    "title": "专访靳玉志：「境」和「界」并不冲突，共同落实「电子螺丝钉」的战略定位",
    "url": "https://36kr.com/p/3902068392658566?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T04:32:43+00:00",
    "summary": "华为公司高级副总裁、引望公司CEO 靳玉志 文｜肖漫 编辑｜李勤、杨轩 过去几年，华为一直强调自己在汽车行业的身份只有一个——“智能网联汽车的增量部件提供商”。 尽管一遍遍地强调，但随着合作车型不断扩容，“界”（指鸿蒙智行生态联盟中的问界、享界、智界、尊界、尚界）之外又出现了“境”（启境、奕境等），华为乾崑智驾授权体验中心开始向消费者开放，华为在汽车产业中的角色再一次被审视：它究竟是一家供应商，还"
  },
  {
    "id": "rss:https://36kr.com/p/3903396279125888?f=rss",
    "domain": "大厂 AI 动态",
    "title": "在WAIC地下一层找机会的年轻人：光鲜是过去，眼下是生存",
    "url": "https://36kr.com/p/3903396279125888?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T03:02:32+00:00",
    "summary": "6个年轻创业者在WAIC的故事 文｜温丽虹 王欣逸 编辑｜张雨忻 在上海世博的WAIC现场，想找初创公司的主场H4得颇费一番功夫。 经安检进入主会场，远远只看到会场墙壁上H1到H3的标识。跟随汹涌人群挤进一楼主展馆，几名忙着操纵具身智能机器人的知名厂商工程师翻了翻他们群聊里的展会地图，抱歉地告诉我，他们也不清楚：“这里只有H1到H3，没有H4。你是不是去分会场找找？” 属于初创团队的场地在主展馆地"
  },
  {
    "id": "rss:https://36kr.com/p/3903383663478403?f=rss",
    "domain": "大厂 AI 动态",
    "title": "谁还在卷参数？WAIC2026全是能干活的实体AI！",
    "url": "https://36kr.com/p/3903383663478403?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T02:49:41+00:00",
    "summary": "&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;7月17日-20日，一起在WAIC2026现场，看见人工智能真正进入产业深处。 过去一年，围绕AI行业的讨论正在变得更具体。大模型能力仍在持续迭代，但外界关注的重点，已经不再只停留在模型参数、模型发布和单点能力展示上。随着智能体、具身智能、空间智能、AI基础设施等方向不断演进，行业开始更频"
  },
  {
    "id": "rss:https://36kr.com/p/3903365398185857?f=rss",
    "domain": "大厂 AI 动态",
    "title": "从“连得上”到“算得懂”，天基通算融合初创公司押注无人系统，首轮融资数千万元｜36氪首发",
    "url": "https://36kr.com/p/3903365398185857?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T02:30:06+00:00",
    "summary": "文&nbsp;|&nbsp;阿至 封面来源｜Pexels 中国低轨卫星星座的规模化部署已经进入关键时间窗口。 一组直观的数据进展是：中国星网已完成第一代组网，垣信卫星在轨运行卫星数量突破200颗，长征十号乙型火箭成功完成全球首次海上网系回收，头部商业公司的可回收火箭也将迎来关键首飞节点。 当“上天”这件事的成本有望迅速下降，产业链的注意力也在从“怎么把卫星打上去”转向一个更务实的问题：卫星组网之后"
  },
  {
    "id": "rss:https://36kr.com/p/3901396207584902?f=rss",
    "domain": "大厂 AI 动态",
    "title": "腾讯云ADP 4.0海外版发布，要把企业级智能体带到全球市场 | 最前线",
    "url": "https://36kr.com/p/3901396207584902?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T01:30:27+00:00",
    "summary": "腾讯云的企业级智能体平台，正式出海了。 7月18日，在2026世界人工智能大会上，腾讯云正式发布了智能体开发平台 ADP 4.0海外版，同步升级智能工作台、Claw 模式、Skill 广场三大核心模块，围绕触达、交互、生态、连接四大能力做了全面国际化适配。 ADP 的全称是 Agent Development Platform，定位为企业级 AgentOps 平台，覆盖智能体的构建、分发和治理全生"
  },
  {
    "id": "rss:https://36kr.com/p/3902007640459145?f=rss",
    "domain": "大厂 AI 动态",
    "title": "从烤披萨到拿快递，满场跑的机器人终于要进你家了｜WAIC 2026全面探展",
    "url": "https://36kr.com/p/3902007640459145?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T01:20:44+00:00",
    "summary": "史上最热的WAIC都整了哪些活？看这一篇就够了。 文｜邓咏仪 周鑫雨 王欣逸 温丽虹 编辑｜张雨忻 如果你想知道今年的AI圈第一盛事热度如何，只要来上海感受逼近40度的高温，就能同频共振。 没有很热，只有更热。 7月17日，2026年世界人工智能大会在上海世博展览馆正式开幕。展览面积首次突破10万平方米，1100余家企业参展，3000余项展品集中亮相，超300款产品全球首发。从展商数量来看，和20"
  },
  {
    "id": "rss:https://36kr.com/p/3899612612494976?f=rss",
    "domain": "大厂 AI 动态",
    "title": "红熊AI完成数亿元A+轮融资，基于AI“记忆科学”从To B服务延伸至To C应用｜36氪首发",
    "url": "https://36kr.com/p/3899612612494976?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T01:00:00+00:00",
    "summary": "36氪获悉，红熊AI今日宣布完成数亿元人民币A+轮融资，投后估值接近30亿元人民币。本轮融资由浙江九纬私募基金、嘉兴彰元创业投资与老股东格睿丰联合投资。这是红熊AI在短短15个月内完成的第6轮融资。 据了解，本轮融资资金将主要用于持续深化AI记忆科学的类人大脑基础研究、加速OpenBear通用大模型与MemoryBear记忆科学系统的深度融合，以及扩大智能客服、智能营销、ChatBI与智能教育四大"
  },
  {
    "id": "rss:https://36kr.com/p/3903220264404608?f=rss",
    "domain": "大厂 AI 动态",
    "title": "8点1氪丨长鑫科技中签号出炉：共约770.22万个；西班牙1-0战胜阿根廷，夺得本届世界杯冠军；月之暗面有望最快6个月内赴港上市",
    "url": "https://36kr.com/p/3903220264404608?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T00:05:13+00:00",
    "summary": "今日热点导览 任泽平团队回应VIP群聊解散 市场监管总局发布《个体工商户信用信息应用指南》 “工业维生素”价格暴涨，钼铁一天跳涨1500元 黄仁勋皮夹克拍出96万美元天价 韩国承诺放宽韩元获取渠道，力争实现“自由兑换货币”目标 TOP3大新闻 长鑫科技中签号出炉：共约770.22万个 36氪获悉，长鑫科技披露首次公开发行股票网上中签结果，中签号码共有7702207个，每个中签号码只能认购500股长"
  },
  {
    "id": "rss:https://36kr.com/p/3902428274427525?f=rss",
    "domain": "大厂 AI 动态",
    "title": "科氪 | 从生命预警到七诊合参，安顿“双核首发”的技术密码",
    "url": "https://36kr.com/p/3902428274427525?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-19T10:35:30+00:00",
    "summary": "在2026世界人工智能大会（WAIC 2026）上，安顿健康以两项首发引发广泛关注：我国首个生命预警表标准，以及行业首个七诊合参中医机器人——安顿中医机器人。 WAIC现场图片 两项首发背后，是一套从感知层到算法层再到输出层的完整技术体系。 核心引擎：天回·AI脉诊算法与三重置信体系 安顿双核首发的技术底座，是一套名为\"天回·AI脉诊算法\"的自研核心技术。该算法首次将中医24种脉象细分为120余个"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3903594720396932?f=rss",
    "domain": "大厂 AI 动态",
    "title": "源杰科技盘中触及20CM跌停",
    "url": "https://36kr.com/newsflashes/3903594720396932?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T06:21:53+00:00",
    "summary": "36氪获悉，源杰科技盘中触及20CM跌停，报1324.80元。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3903591202162562?f=rss",
    "domain": "大厂 AI 动态",
    "title": "报告：腾讯WorkBuddy在国内PC端AI原生办公智能体市场6月单月访问量破2000万",
    "url": "https://36kr.com/newsflashes/3903591202162562?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T06:18:18+00:00",
    "summary": "7月20日，最新发布的《2026年Q2中国办公智能体平台市场洞察报告》显示：腾讯WorkBuddy在国内PC端AI原生办公智能体市场6月单月访问量破2000万，保持市场第一领先优势。"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3903585520371588?f=rss",
    "domain": "大厂 AI 动态",
    "title": "中信建投：Kimi K3模型达全球Tier1，国产模型再现DeepSeek时刻",
    "url": "https://36kr.com/newsflashes/3903585520371588?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T06:12:32+00:00",
    "summary": "36氪获悉，中信建投研报指出，坚定看好AI产业趋势。我们认为，K3是本周全球大模型行业的分水岭事件，也是另一个DeepSeek时刻：K3的发布意味着中国大模型第一次以“竞争威胁”身份进入全球大模型叙事——2.8万亿参数 + 100万上下文+Code Arena登顶，证明国产模型已在Agentic Coding主战场与美国前沿模型正面交锋。其他建议重点关注应用层机会：1）K3提升了开源模型智能水平，"
  },
  {
    "id": "rss:https://36kr.com/newsflashes/3903580278785669?f=rss",
    "domain": "大厂 AI 动态",
    "title": "波音预计未来20年全球民航服务市场规模达4.9万亿美元",
    "url": "https://36kr.com/newsflashes/3903580278785669?f=rss",
    "source": "36氪",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T06:07:12+00:00",
    "summary": "波音公司7月18日发布报告称，未来20年全球民航服务市场规模预计将达到4.9万亿美元，同时行业将需要新增超过240万名民航专业人员，以支持机队扩张和航空业发展。报告预计，到2045年前，全球民航业将需要新增约67.4万名飞行员、72.8万名维修技术人员和102.3万名客舱乘务人员。其中，约三分之二的人才需求用于替代退休人员，另外三分之一用于支持全球机队增长。（界面）"
  },
  {
    "id": "hn:48933344",
    "domain": "股票",
    "title": "SpaceX stock erases all its gains and slides below IPO price in intraday trading",
    "url": "https://www.latimes.com/business/story/2026-07-16/spacex-stock-erases-gains-slides-below-ipo-price-in-intraday-trading",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 312,
    "published_at": "2026-07-16T12:02:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:48948435",
    "domain": "股票",
    "title": "Short sellers notch $8.7B profit as SpaceX shares dip to IPO price",
    "url": "https://www.reuters.com/business/media-telecom/short-sellers-rack-up-87-bln-profit-spacex-slips-below-ipo-price-ortex-2026-07-16/",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 167,
    "published_at": "2026-07-17T15:17:54+00:00",
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
    "id": "hn:48958985",
    "domain": "股票",
    "title": "Traders are increasingly betting against SpaceX just weeks after IPO",
    "url": "https://www.ft.com/content/2b96703d-440b-46db-8d86-9fff9ecc59d5",
    "source": "ethanhawksley",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-07-18T15:26:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48938001",
    "domain": "股票",
    "title": "SPCX is now Wall Street's most shorted new stock",
    "url": "https://invezz.com/news/2026/07/16/the-worlds-most-valuable-ipo-spcx-is-now-wall-streets-most-shorted-new-stock/",
    "source": "lbrito",
    "platform": "hackernews",
    "points": 80,
    "published_at": "2026-07-16T18:03:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:48950580",
    "domain": "股票",
    "title": "SpaceX stock drops to a new low and loses $1T in value in a month",
    "url": "https://www.businessinsider.com/spacex-stock-drops-new-low-ipo-price-starship-launch-scrubbed-2026-7",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-07-17T18:26:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:48946872",
    "domain": "股票",
    "title": "US Corporate Insiders Are Selling Stocks at a Near Record Pace",
    "url": "https://www.bloomberg.com/news/articles/2026-07-17/us-corporate-insiders-are-selling-stocks-at-a-near-record-pace",
    "source": "pimienta",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-07-17T13:00:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48974426",
    "domain": "股票",
    "title": "Big Tech Needs to Justify AI Spending as Investors Dump Stocks",
    "url": "https://www.bloomberg.com/news/articles/2026-07-19/big-tech-needs-to-justify-ai-spending-as-investors-dump-stocks",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-07-20T04:41:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:48967807",
    "domain": "股票",
    "title": "Claude Code skill for searching royalty-free stock photos via the Pexels API",
    "url": "https://github.com/amalshehu/pexels-skill",
    "source": "amalshehu",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-19T12:55:11+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3777405",
    "domain": "股票",
    "title": "退钱不玩了！韩国散户杠杆押注SK海力士、三星血亏，单只杠杆ETF较高点跌70%",
    "url": "https://wallstreetcn.com/articles/3777405",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T06:21:03+00:00",
    "summary": "KODEX SK海力士单股杠杆ETF自6月高点已跌约70%。散户净买入达94亿美元，亏损几乎全由国内个人投资者承担。有投资者留言：\"我想回到开始炒股之前，把我的钱还给我。\"分析人士警告，去杠杆进程或尚未结束，市场或面临持续压力。"
  },
  {
    "id": "wscn:3777408",
    "domain": "股票",
    "title": "鸿海首度拿下SpaceX AI服务器代工订单，规模达520亿美元",
    "url": "https://wallstreetcn.com/articles/3777408",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T06:20:40+00:00",
    "summary": "鸿海斩获SpaceX价值520亿美元的AI大单，打破戴尔与美超微的寡占格局，首次打入其供应链。这笔涵盖1.3万柜英伟达GB300服务器的订单未计入鸿海此前指引，将显著调升其下半年至明年业绩预期。得益于全球制造产能、光通信及CPO等一站式技术布局，鸿海今年AI服务器全球市占率有望超四成。"
  },
  {
    "id": "wscn:3777407",
    "domain": "股票",
    "title": "三星美国消费电子部门裁员逾800人，手机部门出现史上首次亏损",
    "url": "https://wallstreetcn.com/articles/3777407",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T06:19:34+00:00",
    "summary": "三星电子正经历冰火两重天：芯片业务利润预计同比暴涨约19倍，移动部门却预告史上首次亏损。美国消费电子子公司已在新泽西、德克萨斯两地合计裁员逾800人，内部员工直言\"这或许只是开始\"。苹果施压、中国品牌夹击、AI推高芯片成本，三管齐下令消费电子业务雪上加霜。"
  },
  {
    "id": "wscn:3777406",
    "domain": "股票",
    "title": "本周最大悬念：Mag 7财报，能否给美股\"续命\"？",
    "url": "https://wallstreetcn.com/articles/3777406",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T06:08:40+00:00",
    "summary": "科技巨头财报季鸣枪，Alphabet与特斯拉率先交卷，成美股走向关键。“科技七姐妹”盈利预期强劲，重回资金“安全港”。但美银警告市场已现“极端仓位”狂热，若AI资本投入生变，叠加地缘与美联储变数，美股恐迎尾部风暴。"
  },
  {
    "id": "wscn:3776757",
    "domain": "股票",
    "title": "大模型7月激战：国产性能快速攀升，海外巨头开启价格战",
    "url": "https://wallstreetcn.com/premium/articles/3776757?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T06:08:38+00:00",
    "summary": "全球AI大模型正从“百模大战”的混沌期迈入“诸侯混战”的格局重塑期，能力代差快速收窄、资本开支持续膨胀、开源生态加速全球化。"
  },
  {
    "id": "wscn:3777388",
    "domain": "股票",
    "title": "沪指午后翻绿，“煤电酒油”爆发，科技股再度下跌，恒科指涨超2%，科网股集体拉升",
    "url": "https://wallstreetcn.com/articles/3777388",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T05:48:14+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市约3100股飘红，上午半天成交1.68万亿。沪深两市半日成交额1.67万亿，较上个交易日放量近700亿。板块方面，油气、煤炭、电力、白酒、保险、银行、黄金、医药生物板块涨幅居前。半导体、算力硬件产业链持续回调，PCB、光刻机、存储器方向领跌。"
  },
  {
    "id": "wscn:3777204",
    "domain": "股票",
    "title": "程坦美国宏观研究特训营：穿透宏观乱局之下的数据真相",
    "url": "https://wallstreetcn.com/articles/3777204",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T05:47:44+00:00",
    "summary": "打破宏观投研远离市场“不接地气”的通病，突破“只见树木不见森林”的碎片化认知，建立可验证的宏观投研决策闭环"
  },
  {
    "id": "wscn:3777401",
    "domain": "股票",
    "title": "通往60万亿之路：如何看消费弹性？",
    "url": "https://wallstreetcn.com/articles/3777401",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T05:38:18+00:00",
    "summary": "东吴宏观卢哲团队认为，中国消费处地产下行后半程，有望先于房价见底。实现2030年社零60万亿目标的关键是耐用品修复及服务消费与价格回升。非耐用品是稳定器；最大变量耐用品的补贴透支预计消化至2027年9月，整体消费内生动能将在2027年四季度明显改善。"
  },
  {
    "id": "wscn:3777402",
    "domain": "股票",
    "title": "恐慌信号！高盛交易员：AI信用风险已开始向更广泛市场扩散",
    "url": "https://wallstreetcn.com/articles/3777402",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T05:38:11+00:00",
    "summary": "AI超大规模数据中心的资本开支逻辑正出现裂缝——高盛顶级衍生品交易员Garrett发出警告：相关信用利差持续走阔，恐慌指数单周飙升5.5点，科技板块遭遇10年来最大规模抛售，标普500已难以真实反映个股实际表现。他一语成谶：\"若你上半年赚得风光，7月恐怕极为难熬。\""
  },
  {
    "id": "wscn:3777404",
    "domain": "股票",
    "title": "任泽平再回应“学员炒股亏1000万”：其加入会员时间只有一两周，自行配置的标的和加杠杆，我们没推荐个股，深表惋惜和痛心",
    "url": "https://wallstreetcn.com/articles/3777404",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T05:37:48+00:00",
    "summary": "花2980元加入\"泽平宏观VIP\"，一位投资者重仓加融资押注存储芯片股，账户爆仓亏损超1000万，痛呼\"一辈子毁了\"。任泽平团队紧急解散所有VIP群后连发多篇声明自辩：从不推荐个股，百次提醒\"勿加杠杆\"，学员系自行操作。然而，其本人近期密集喊多科技牛的记录，难掩争议。"
  },
  {
    "id": "wscn:3777399",
    "domain": "股票",
    "title": "权益大佬神玉飞“下一站”水落石出，出任南华基金副总经理",
    "url": "https://wallstreetcn.com/articles/3777399",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T04:05:53+00:00",
    "summary": "能否带来权益投研新视角"
  },
  {
    "id": "wscn:3777392",
    "domain": "股票",
    "title": "花旗：新兴市场涨势强但过度集中，上调中国至超配、战术性下调韩国",
    "url": "https://wallstreetcn.com/articles/3777392",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T03:37:52+00:00",
    "summary": "MSCI新兴市场指数年初至今涨幅约20%，但涨势高度集中于韩国和中国台湾，两者合计占新兴市场EM基准指数约50%权重。花旗认为，AI波动性上升令集中风险暴露，而中国仓位轻、宏观环境改善，具备“涨势扩散”条件，恒生指数2026年底目标为29600点，沪深300目标为5600点。"
  },
  {
    "id": "wscn:3777398",
    "domain": "股票",
    "title": "工信部：推动建立算力市场化定价标准，着力培育全国一体化技术市场",
    "url": "https://wallstreetcn.com/articles/3777398",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T03:32:30+00:00",
    "summary": "工信部最新数据显示，前5个月规模以上工业企业营业收入利润率达5.66%，创2024年以来月度累计新高；制造业AI应用普及率突破30%，开源大模型全球下载量破百亿次。工信部同时宣布，将推动算力市场化定价标准，并着力打破技术交易区域壁垒，构建全国一体化技术市场。"
  },
  {
    "id": "wscn:3777383",
    "domain": "股票",
    "title": "科技股抛售继续，韩股跌超4%，美伊冲突推油价破91美元、现货黄金下跌",
    "url": "https://wallstreetcn.com/articles/3777383",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T03:31:31+00:00",
    "summary": "美伊冲突升级，布伦特原油一度涨超3.8%，突破91美元/桶，创6月以来新高。韩国综指跌幅持续扩大，一度跌超4.35%，韩国交易所相继对KOSDAQ和KOSPI启动程序化卖盘熔断机制；MSCI亚太指数距6月高点跌幅已超9%，逼近技术性回调区间。科技股抛售持续，费城半导体指数上周五已跌入熊市。"
  },
  {
    "id": "wscn:3777394",
    "domain": "股票",
    "title": "Anthropic被曝测试AMD GPU，AI巨头正在系统性降低单一算力依赖",
    "url": "https://wallstreetcn.com/articles/3777394",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T03:21:28+00:00",
    "summary": "芯片分析机构SemiAnalysis从AMD高管公开代码中发现，Anthropic将成为AMD新客户，这家Claude背后的AI独角兽已构建起涵盖谷歌TPU、三星的多元算力矩阵，如今再引AMD入局，剑指供应链风险与英伟达垄断议价的双重破局。"
  },
  {
    "id": "wscn:3777397",
    "domain": "股票",
    "title": "字节游戏的AI试错，这回试出了路",
    "url": "https://wallstreetcn.com/articles/3777397",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T03:13:44+00:00",
    "summary": "勤奋和耐心没有捷径"
  },
  {
    "id": "wscn:3777395",
    "domain": "股票",
    "title": "头部量化“迅猛加仓”，灵均投资公告两周内自购2亿",
    "url": "https://wallstreetcn.com/articles/3777395",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T03:05:00+00:00",
    "summary": "恰逢跌破3800点之际"
  },
  {
    "id": "wscn:3777393",
    "domain": "股票",
    "title": "高盛解读新易盛财报：Q2利润大超预期，800G/1.6T 光模块出货量将持续提升",
    "url": "https://wallstreetcn.com/articles/3777393",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T03:04:23+00:00",
    "summary": "高盛认为，新易盛Q2净利润指引中位数超预期44%，核心驱动为AI资本开支激增及产品向800G/1.6T高速光模块升级。随光芯片供应改善与产能扩张，高速光模块出货量将持续攀升。基于强劲基本面，高盛全面上调其2026-2028年盈利预测，目标价上调至633元，维持“买入”评级。"
  },
  {
    "id": "wscn:3777396",
    "domain": "股票",
    "title": "一周展望：黄金酝酿反弹？聚焦科技巨头财报",
    "url": "https://wallstreetcn.com/articles/3777396",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T03:02:54+00:00",
    "summary": "上周中东战火升级刺激原油价格飙升15%，黄金周线延续回落一度跌破4000美元，半而导体板块的持续回调..."
  },
  {
    "id": "wscn:3777390",
    "domain": "股票",
    "title": "电池消费税或加速行业洗牌，宁德时代更抗压，乘用车影响不大、储能回报更敏感",
    "url": "https://wallstreetcn.com/articles/3777390",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T02:44:17+00:00",
    "summary": "摩根大通和高盛认为，电池消费税计入“税金及附加”，不影响营收和毛利率，但将对营业利润和净利润带来一定影响。行业龙头整体可控，宁德时代凭借海外收入占比高、盈利缓冲厚及议价能力强最具韧性；国内市场为主、盈利较弱的厂商压力更大。乘用车终端影响有限，但储能项目回报率更敏感，行业整合或加速。"
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
    "id": "hn:48947500",
    "domain": "股票",
    "title": "A.I. Is Running on Borrowed Money",
    "url": "https://www.nytimes.com/2026/07/17/business/ai-spending-oracle-stocks-bonds.html",
    "source": "ripe",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-07-17T14:01:11+00:00",
    "summary": ""
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
    "points": 493,
    "published_at": "2026-07-15T03:32:45+00:00",
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
    "id": "hn:48953857",
    "domain": "金融",
    "title": "Nadella Blasts AI Industry's Double Standard",
    "url": "https://finance.biggo.com/news/438f299b-ca23-468d-b37d-0ffe09a4ca55",
    "source": "nittanymount",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-07-18T00:28:46+00:00",
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
    "points": 59,
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
