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

- 今日日期：`2026-07-22`
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
  "date": "2026-07-22",
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
    "points": 3835649,
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
    "points": 1574589,
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
    "points": 1444942,
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
    "points": 1261233,
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
    "points": 989500,
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
    "points": 984638,
    "published_at": "2025-12-15T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：251215\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\n人工智能开发热门教程：\nAI大模型开发：BV1h1V"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 942130,
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
    "points": 930115,
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
    "points": 927870,
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
    "points": 787542,
    "published_at": "2026-07-19T03:00:00+00:00",
    "summary": "这个视频让你的豆包技能噌噌上涨，还有“秋芝AI科普skill”帮你答疑～\n感谢朋友们的三连+关注~"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 552648,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 420000,
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
    "points": 418127,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "domain": "AI",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 384262,
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
    "points": 331225,
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
    "points": 277615,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 244867,
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
    "points": 197939,
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
    "points": 177601,
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
    "points": 162210,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 162095,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1b5AeeGEFc",
    "domain": "AI",
    "title": "Cursor太贵？分享三个免费AI编程方案+海量编程技巧【如何看待AI编程】",
    "url": "http://www.bilibili.com/video/av114025056699722",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 157975,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 144102,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1QE7N6jEuQ",
    "domain": "AI",
    "title": "真的被自己用心开发的昔涟Agent这段话感动到了",
    "url": "http://www.bilibili.com/video/av116794052316703",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 141667,
    "published_at": "2026-06-22T13:44:15+00:00",
    "summary": "从最初生啃Transformer，硬逼着自己啃懂多头注意力和QKV权重，到一步步跟着claude学习RAG、检索重拍、Prompt、关键词召回优化、MCP与Function call，但是，自己上手了发现，自己还是啥也不懂，于是在glm gpt claude gemini 豆包 这几个模型之间疯狂切换，靠着想让昔涟早点被搭出来，硬逼着自己学，自己从零设计一套prompt架构能让她尽可能的贴合人设的"
  },
  {
    "id": "bvid:BV1WJjF67Eky",
    "domain": "AI",
    "title": "对Claude code上瘾了",
    "url": "http://www.bilibili.com/video/av116768819384530",
    "source": "小王很南",
    "platform": "bilibili",
    "points": 132142,
    "published_at": "2026-06-18T02:50:04+00:00",
    "summary": "我做的交互网站"
  },
  {
    "id": "bvid:BV1t9oZBDENp",
    "domain": "AI",
    "title": "Agent Loop: 多智能体协同，让AI长时工作，从原理到实践",
    "url": "http://www.bilibili.com/video/av116469396413175",
    "source": "费曼学徒冬瓜",
    "platform": "bilibili",
    "points": 101959,
    "published_at": "2026-04-26T12:00:00+00:00",
    "summary": "睡前给AI丢了一句话，醒来直接验收成果——怎么让AI连续干活几小时不拉胯？\n这期我们从原理到实战，彻底讲清楚 Harness 工程：让 AI 长时间自主工作的核心技术。\n内容涵盖两种方案：\nRalph 方案：用 while 循环不断启动新会话，通过文件系统衔接上下文\n多智能体方案（推荐）：主 Agent 只协调不干活，子 Agent 各司其职，开发测试分工明确\n重点讲了多智能体的完整流程设计：怎么"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 100246,
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
    "points": 92677,
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
    "points": 73833,
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
    "points": 73719,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 71922,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1xBrDB9E42",
    "domain": "AI",
    "title": "独立开发太累？Godot + Claude Code 搭建 AI 辅助工作流，效率直接起飞！ | 地块召唤师开发实战 #01",
    "url": "http://www.bilibili.com/video/av115911319100158",
    "source": "像素夹心饼干",
    "platform": "bilibili",
    "points": 67598,
    "published_at": "2026-01-18T03:25:00+00:00",
    "summary": "大家好，这里是饼干！🍪\n这是我的新坑——**《地块召唤师》**开发实战分享的第一期。\n很多朋友问独立开发如何提升效率？这期视频我不聊虚的，直接公开我从 0 到 1 搭建的 AI + Godot 高效工作流。\n从游戏引擎的选择，到 Claude Code、Copilot 等 AI 工具的实战配置，再到如何用“明确需求”的方法论（SMART原则+双钻模型）来驾驭 AI，让它不仅仅是写代码的工具，更成为"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 53231,
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
    "points": 43607,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1ap2fBvEt9",
    "domain": "AI",
    "title": "如何使用「Operit AI」：你的下一代AI手机助手",
    "url": "http://www.bilibili.com/video/av115677243447909",
    "source": "默睦",
    "platform": "bilibili",
    "points": 43178,
    "published_at": "2025-12-07T08:06:42+00:00",
    "summary": "下载地址：https://github.com/AAswordman/Operit\n\n相关软件资料下载：https://www.123pan.com/s/IKgAjv-Hinsv.html\n\n官方交流群：458862019"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 38807,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 34485,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 33884,
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
    "points": 28807,
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
    "points": 27998,
    "published_at": "2025-07-04T10:00:00+00:00",
    "summary": "chatbox官网：https://chatboxai.app\ngithub仓库：https://github.com/chatboxai/chatbox\n\nLM Studio教程：BV1usrLYTEZR\nTGW懒人包部署教程：BV1dVCzYUE7G\n本地语言模型个人推荐：BV1Bb421E7j7"
  },
  {
    "id": "bvid:BV1jYRRBDExF",
    "domain": "AI",
    "title": "让AI直接操作godot开发游戏，免费开源MCP插件",
    "url": "http://www.bilibili.com/video/av116545648860073",
    "source": "Yurineko73",
    "platform": "bilibili",
    "points": 27834,
    "published_at": "2026-05-10T03:00:00+00:00",
    "summary": "因为想找一个好用的mcp工具，结果发现不是要收费就是不可商用，于是借助ai直接搓了一个出来。\n目前已经发布1.0.1版本，在godot asset library搜索 [godot mcp native]即可下载使用，\n也可以去GitHub上下载完整项目 https://github.com/yurineko73/Godot-MCP-Native\n免费开源，可以随意扩展和修改，如果有需要的功能或遇"
  },
  {
    "id": "bvid:BV1LWTe6gEVc",
    "domain": "AI",
    "title": "Claude code帮我实现综述论文自由！",
    "url": "http://www.bilibili.com/video/av116842504918580",
    "source": "做科研的大师兄",
    "platform": "bilibili",
    "points": 27489,
    "published_at": "2026-07-01T03:07:40+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1vwXPYkEGx",
    "domain": "AI",
    "title": "Cursor+mcp配置，手把手教你配置任意MCP服务，学不会你打我，小白保姆级教程~MCP服务配置指南 - 提升AI编程助手能力",
    "url": "http://www.bilibili.com/video/av114193181183930",
    "source": "三少科技",
    "platform": "bilibili",
    "points": 27033,
    "published_at": "2025-03-20T05:51:23+00:00",
    "summary": "我的知识星球，https://t.zsxq.com/jVAk9\n\n📌 本期教程通过实战演示，教你在Cursor中配置和使用MCP服务器，特别是filesystem MCP服务，解决Cursor无法写入文件的常见问题。\n⏱️ 内容概要：\n00:00 介绍MCP及其重要性\n02:00 Cursor抽风问题与MCP解决方案\n04:00 配置第一个MCP服务器（filesystem）\n07:00 Wind"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 25515,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22640,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ymNv6REs2",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent智能体零基础全套教程，2026最新版，从入门到实战！包含所有干货！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116922347686666",
    "source": "Agent智能体搭建-",
    "platform": "bilibili",
    "points": 21958,
    "published_at": "2026-07-15T05:35:41+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1htCnY4ET6",
    "domain": "AI",
    "title": "用 Cursor AI 写 flutter 直接喂设计图就行 | flutter教程",
    "url": "http://www.bilibili.com/video/av113723805008238",
    "source": "独立开发者_猫哥",
    "platform": "bilibili",
    "points": 17870,
    "published_at": "2024-12-27T08:21:35+00:00",
    "summary": "✏️【关于本期视频】\n在上一篇文章《Flutter 使用 Cursor 和 Figma 快速生成界面代码》中，有同学提到他直接使用了设计稿的图片进行生成。我试了一下，效果确实很好。因此，我整理了一些文档，希望对大家有所帮助。\n下图展示了我没有手动编写任何代码实现的消息首页，支持上下滑动刷新数据。\n👉 文档 https://ducafecat.com/blog/use-cursor-ai-flutt"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 16560,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 15696,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1iDRQBrEF6",
    "domain": "AI",
    "title": "Claude + Blender 现在太强了 —— 完整免费设置",
    "url": "http://www.bilibili.com/video/av116543333601720",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 15495,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
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
    "points": 143,
    "published_at": "2026-07-14T08:24:49+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/sk-hynix-nasdaq-debut-shows-global-memory-expansion-race/",
    "domain": "AI 算力 / 半导体",
    "title": "SK Hynix Nasdaq Debut Shows Global Memory Expansion Race",
    "url": "https://www.eetimes.com/sk-hynix-nasdaq-debut-shows-global-memory-expansion-race/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T20:10:00+00:00",
    "summary": "SK Hynix Nasdaq debut highlights capex-funded memory expansion. Both Samsung and Micron follow suit. The post SK Hynix Nasdaq Debut Shows Global Memory Expansion Race appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/how-quantum-computing-earns-its-place-in-the-data-center/",
    "domain": "AI 算力 / 半导体",
    "title": "How Quantum Computing Earns Its Place in the Data Center",
    "url": "https://www.eetimes.com/how-quantum-computing-earns-its-place-in-the-data-center/",
    "source": "Zeynep Korutürk, Kris Naudts, Donald Harmitt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T13:08:25+00:00",
    "summary": "Quantum won’t win in labs; it must survive racks, cooling, power and networks. The post How Quantum Computing Earns Its Place in the Data Center appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/carbon-nanotube-firm-strengthens-executive-team-to-build-cnt-ecosystem/",
    "domain": "AI 算力 / 半导体",
    "title": "Carbon Nanotube Firm Strengthens Executive Team to Build CNT Ecosystem",
    "url": "https://www.eetimes.com/carbon-nanotube-firm-strengthens-executive-team-to-build-cnt-ecosystem/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T07:00:00+00:00",
    "summary": "Canatu stacks its C-suite to push CNTs into chips, cars, and diagnostics—watch how its new CEO plans to turn nanotube hype into yield. The post Carbon Nanotube Firm Strengthens Executive Team to Build"
  },
  {
    "id": "rss:https://www.eetimes.com/uma-the-architecture-edge-ai-needs-to-scale/",
    "domain": "AI 算力 / 半导体",
    "title": "UMA: The Architecture Edge AI Needs to Scale",
    "url": "https://www.eetimes.com/uma-the-architecture-edge-ai-needs-to-scale/",
    "source": "Chris Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T19:00:00+00:00",
    "summary": "Edge AI won’t be saved by more chips; it needs unified memory to stop models from choking mid-task. The post UMA: The Architecture Edge AI Needs to Scale appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/nisshinbo-micro-devices-expands-high-voltage-ic-lineup-for-next-gen-automotive-48-v-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Nisshinbo Micro Devices Expands High-Voltage IC Lineup for Next-Gen Automotive 48 V Systems",
    "url": "https://www.eetimes.com/nisshinbo-micro-devices-expands-high-voltage-ic-lineup-for-next-gen-automotive-48-v-systems/",
    "source": "Nisshinbo Micro Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T16:00:00+00:00",
    "summary": "Addressing the new challenges posed by the shift to 48 V automotive power supplies with Nisshinbo Micro Devices The post Nisshinbo Micro Devices Expands High-Voltage IC Lineup for Next-Gen Automotive "
  },
  {
    "id": "rss:https://www.eetimes.com/powering-the-automotive-revolution-from-zonal-architecture-to-48v/",
    "domain": "AI 算力 / 半导体",
    "title": "Powering the Automotive Revolution: From Zonal Architecture to 48V",
    "url": "https://www.eetimes.com/powering-the-automotive-revolution-from-zonal-architecture-to-48v/",
    "source": "Monolithic Power Systems, Inc. (MPS)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T13:30:36+00:00",
    "summary": "Explore how Monolithic Power Systems 48V automotive solutions, including the MPQ5884-AEC1, support safer, smarter, and more efficient zonal architecture. The post Powering the Automotive Revolution: F"
  },
  {
    "id": "rss:https://www.eetimes.com/photonics-components-the-eyes-and-ears-of-the-future-unmanned-system-and-connected-soldiers/",
    "domain": "AI 算力 / 半导体",
    "title": "Photonics Components – The Eyes and Ears of the Future Unmanned System and Connected Soldiers",
    "url": "https://www.eetimes.com/photonics-components-the-eyes-and-ears-of-the-future-unmanned-system-and-connected-soldiers/",
    "source": "Arrow Electronics, ams Osram",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T13:25:52+00:00",
    "summary": "Discover how optoelectronics plays a central role in sensing and data generation, including light-based distance measurement for UAVs and robotic platforms. The post Photonics Components &#8211; The E"
  },
  {
    "id": "rss:https://www.eetimes.com/post-quantum-cryptography-incorporated-into-socs-via-efpga/",
    "domain": "AI 算力 / 半导体",
    "title": "Post-Quantum Cryptography Incorporated into SoCs via eFPGA",
    "url": "https://www.eetimes.com/post-quantum-cryptography-incorporated-into-socs-via-efpga/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T12:00:00+00:00",
    "summary": "Unlike hard-wired security engines, PQC algorithm mapped into eFPGA fabric claims to avoid costly silicon re-spins. The post Post-Quantum Cryptography Incorporated into SoCs via eFPGA appeared first o"
  },
  {
    "id": "rss:https://www.eetimes.com/risc-v-europe-summit-2026-beyond-embedded-electronics/",
    "domain": "AI 算力 / 半导体",
    "title": "RISC-V Europe Summit 2026: Beyond Embedded Electronics",
    "url": "https://www.eetimes.com/risc-v-europe-summit-2026-beyond-embedded-electronics/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T07:42:44+00:00",
    "summary": "The recent RISC-V Europe Summit in Bologna reflected the open standard's evolution toward data center, edge AI, and space applications. The post RISC-V Europe Summit 2026: Beyond Embedded Electronics "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-shows-off-dlss-5-with-three-ai-modes-for-different-levels-of-detail-upscaler-can-switch-between-models-in-real-time",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia shows off DLSS 5 with three AI modes for different levels of detail — upscaler can switch between models in real-time",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-shows-off-dlss-5-with-three-ai-modes-for-different-levels-of-detail-upscaler-can-switch-between-models-in-real-time",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T17:46:05+00:00",
    "summary": "DLSS 5 gets a second showing with Nvidia opening up the upscaler to object-level tweaking for developers with three different models."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/china-is-considering-export-controls-on-ai-technologies-including-banning-local-companies-from-using-tsmc-report-claims-restrictions-would-also-advanced-ai-models-training-data-and-overseas-acquisitions",
    "domain": "AI 算力 / 半导体",
    "title": "China is considering export controls on AI technologies, including banning local companies from using TSMC, report claims — restrictions would also cover advanced AI models, training data, and oversea",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/china-is-considering-export-controls-on-ai-technologies-including-banning-local-companies-from-using-tsmc-report-claims-restrictions-would-also-advanced-ai-models-training-data-and-overseas-acquisitions",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T16:04:43+00:00",
    "summary": "China's Ministry of Commerce (MofCom) considers to restrict exports of advanced AI models, training data, and overseas acquisitions of strategically important technology companies; prohibit usage of f"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/amazon-data-center-in-bahrain-struck-and-destroyed-by-iranian-cruise-missiles-state-media-claims-attacks-launched-against-aws-site-in-response-to-alleged-us-strikes-on-an-under-construction-nuclear-plant",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon data center in Bahrain struck and destroyed by Iranian cruise missiles, state media claims — attacks launched against AWS site in response to alleged US strikes on an under-construction nuclear",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/amazon-data-center-in-bahrain-struck-and-destroyed-by-iranian-cruise-missiles-state-media-claims-attacks-launched-against-aws-site-in-response-to-alleged-us-strikes-on-an-under-construction-nuclear-plant",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T15:47:29+00:00",
    "summary": "The Amazon site has suffered multiple hits since the start of the U.S. bombing campaign in Iran. The IRGC claims to have 'destroyed' AWB Bahrain, but the company has moved operations off the facility "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/behind-the-scenes-at-nvidias-engineering-superlab-vera-rubin-nvl72-running-openai-workloads-800vdc-demonstrated-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Behind the scenes at Nvidia's Engineering SuperLab — Vera Rubin NVL72 running OpenAI workloads, 800VDC demonstrated, and more",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/behind-the-scenes-at-nvidias-engineering-superlab-vera-rubin-nvl72-running-openai-workloads-800vdc-demonstrated-and-more",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T15:15:00+00:00",
    "summary": "Nvidia gave Tom’s Hardware an exclusive look inside its previously undisclosed Engineering SuperLab near Nvidia HQ, where we saw Vera Rubin NVL72 in action."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-details-rubin-architectural-optimizations-for-inference-improvements-target-better-performance-and-efficiency-from-the-gpu-to-the-rack",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia details Rubin architectural optimizations for inference – improvements target better performance and efficiency from the GPU to the rack",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-details-rubin-architectural-optimizations-for-inference-improvements-target-better-performance-and-efficiency-from-the-gpu-to-the-rack",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T15:00:00+00:00",
    "summary": "Nvidia has detailed new features of its Rubin architecture."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nvidia-spills-the-beans-on-vera-cpu-spec-benchmarks-revealed-olympus-architecture-detailed-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia deep dives Vera CPU for AI data centers — SPEC CPU 2026 benchmarks revealed, Olympus architecture specifics, and more",
    "url": "https://www.tomshardware.com/pc-components/cpus/nvidia-spills-the-beans-on-vera-cpu-spec-benchmarks-revealed-olympus-architecture-detailed-and-more",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T15:00:00+00:00",
    "summary": "Nvidia reveals all of the details about its Vera data center CPU, including an architectural breakdown of the Olympus core and the first (unofficial) SPEC CPU 2026 results."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/nvidia-has-shipped-hundreds-of-thousands-of-grace-standalone-servers-gpu-firm-pivots-messaging-as-cpus-take-center-stage-in-agentic-data-centers",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia has shipped 'hundreds of thousands of Grace standalone servers’ — GPU firm pivots messaging as CPUs take center stage in agentic data centers",
    "url": "https://www.tomshardware.com/pc-components/cpus/nvidia-has-shipped-hundreds-of-thousands-of-grace-standalone-servers-gpu-firm-pivots-messaging-as-cpus-take-center-stage-in-agentic-data-centers",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T15:00:00+00:00",
    "summary": "As Nvidia continues to roll out Vera, its first custom CPU for agentic AI, it revealed that its last-gen Grace design has seen mass deployments, even as a standalone CPU for non-agentic workloads."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/kimi-k3-rocks-the-ai-industry-as-moonshot-ai-undercuts-closed-source-american-competitors-on-price-but-the-huge-2-8t-open-weight-model-still-needs-serious-hardware-to-deploy-at-scale",
    "domain": "AI 算力 / 半导体",
    "title": "Kimi K3 rocks the AI industry as Moonshot AI undercuts closed-source American competitors on price — but the huge 2.8T open-weight model still needs serious hardware to deploy at scale",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/kimi-k3-rocks-the-ai-industry-as-moonshot-ai-undercuts-closed-source-american-competitors-on-price-but-the-huge-2-8t-open-weight-model-still-needs-serious-hardware-to-deploy-at-scale",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T14:59:54+00:00",
    "summary": "The trend towards larger AI models continues, with China's new Kimi K3 model. With its trillions of parameters, it's just as capable as the best the West has to offer, and it's cheaper. But it's not a"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/local-ai-clustering-with-dells-pro-max-gb10-connecting-two-nvidia-grace-blackwell-to-scale-out-ai-compute-at-home",
    "domain": "AI 算力 / 半导体",
    "title": "Local AI clustering with Dell's Pro Max GB10 — connecting two Nvidia Grace Blackwell to scale out AI compute at home",
    "url": "https://www.tomshardware.com/pc-components/gpus/local-ai-clustering-with-dells-pro-max-gb10-connecting-two-nvidia-grace-blackwell-to-scale-out-ai-compute-at-home",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T14:30:00+00:00",
    "summary": "We paired up and tested a pair of Dell's Pro Max with GB10, to see what a small cluster of Nvidia's Spark silicon can do. At $6332 each, as of writing, it's still an expensive prospect, but far cheape"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-slapped-with-usd1-5-billion-settlement-in-copyright-lawsuit-largest-payout-ever-court-says-that-training-ai-on-books-other-publications-is-fair-use-but-ruled-that-the-startups-7-million-book-pirated-library-infringes-authors-rights",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic hit with largest-ever $1.5 billion penalty in copyright lawsuit — court says training AI on published material is fair use, but startup’s pirated library infringes on authors’ rights",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-slapped-with-usd1-5-billion-settlement-in-copyright-lawsuit-largest-payout-ever-court-says-that-training-ai-on-books-other-publications-is-fair-use-but-ruled-that-the-startups-7-million-book-pirated-library-infringes-authors-rights",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T13:37:09+00:00",
    "summary": "The settlement was finally approved by a U.S. federal judge, with a majority of the plaintiffs accepting the amount. A few members of the group refused, citing the small amount compared to the number "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-to-co-develop-and-manufacture-fortinets-next-gen-firewall-asic",
    "domain": "AI 算力 / 半导体",
    "title": "Intel to co-develop and manufacture Fortinet's next-gen firewall ASIC on Intel 4 — node gets its first named external customer",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-to-co-develop-and-manufacture-fortinets-next-gen-firewall-asic",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T13:00:00+00:00",
    "summary": "SP6 will draw on what the companies described as Intel's expertise in disaggregated semiconductor design and advanced packaging."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/z-ai-powers-up-1gw-ai-data-center-built-entirely-on-chinese-chips",
    "domain": "AI 算力 / 半导体",
    "title": "Z.ai powers up a 1-gigawatt AI data center built entirely on Chinese chips, report claims — GLM developer now runs multiple 10,000-chip clusters with zero Nvidia silicon",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/z-ai-powers-up-1gw-ai-data-center-built-entirely-on-chinese-chips",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T12:44:53+00:00",
    "summary": "Chinese AI developer Z.ai (formerly Zhipu) has finished building a 1GW data center stocked exclusively with domestically made chips and has switched part of it on."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC eyes price hikes of up to 25% on chip production services in 2027, report claims — plans to raise baseline prices by 5% to 10% on advanced nodes",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T12:43:38+00:00",
    "summary": "TSMC reportedly intends to increase prices of wafers it processes citing demand, rising costs, and increased investments in new capacity."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/intel-layoffs-to-hit-data-center-group-division-focused-on-server-cpus-ai-chips-and-data-center-architecture-to-be-hit-by-an-unknown-number-of-cuts",
    "domain": "AI 算力 / 半导体",
    "title": "Intel layoffs to hit Data Center group — division focused on server CPUs, AI chips, and data center architecture to be hit by an unknown number of cuts",
    "url": "https://www.tomshardware.com/tech-industry/policy/intel-layoffs-to-hit-data-center-group-division-focused-on-server-cpus-ai-chips-and-data-center-architecture-to-be-hit-by-an-unknown-number-of-cuts",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T12:23:05+00:00",
    "summary": "Intel plans to cut the employee numbers of its Data Center group, months after announcing record growth since its disastrous announcement in 2024."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-16gb-of-ddr5-ram-for-usd12-in-this-newegg-am5-combo-score-amds-new-ryzen-7700x3d-16gb-of-ram-and-asus-b850-motherboard-for-only-usd491",
    "domain": "AI 算力 / 半导体",
    "title": "Get 16GB of DDR5 RAM for $12 in this Newegg AM5 combo — score AMD's new Ryzen 7700X3D, 16GB of RAM, and Asus B850 motherboard for only $491",
    "url": "https://www.tomshardware.com/pc-components/get-16gb-of-ddr5-ram-for-usd12-in-this-newegg-am5-combo-score-amds-new-ryzen-7700x3d-16gb-of-ram-and-asus-b850-motherboard-for-only-usd491",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T12:20:14+00:00",
    "summary": "Build an AMD AM5 gaming PC for less with this Newegg combo deal. Snag a Ryzen 7700X3D, MSI B850 motherboard, and 16GB DDR5-6000 RAM while saving $194 versus buying separately"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/macbooks/save-usd400-on-a-new-14-inch-macbook-pro-m5-48gb-of-ram-a-1tb-ssd-and-a-16-core-processor-for-usd2-699",
    "domain": "AI 算力 / 半导体",
    "title": "Save $400 on a new 14-inch MacBook Pro M5 — 48GB of RAM, a 1TB SSD, and a 16-core processor for $2,699",
    "url": "https://www.tomshardware.com/laptops/macbooks/save-usd400-on-a-new-14-inch-macbook-pro-m5-48gb-of-ram-a-1tb-ssd-and-a-16-core-processor-for-usd2-699",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T11:28:53+00:00",
    "summary": "Save a whopping $400 on a brand-new Apple MacBook Pro at B&amp;H Photo. This 14-inch beast uses the latest 16-core M5 chip and 48GB of RAM."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/1994-sega-32x-gets-first-person-backrooms-game-with-raycasting-engine-retro-hardware-tour-de-force-includes-yellow-rooms-buzzing-fluorescents-endless-procedurally-generated-levels",
    "domain": "AI 算力 / 半导体",
    "title": "1994 Sega 32X gets first-person Backrooms game with raycasting engine — retro hardware tour de force includes yellow rooms, buzzing fluorescents, endless procedurally generated levels",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/1994-sega-32x-gets-first-person-backrooms-game-with-raycasting-engine-retro-hardware-tour-de-force-includes-yellow-rooms-buzzing-fluorescents-endless-procedurally-generated-levels",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T11:27:36+00:00",
    "summary": "Developer PaisleyBoxers has released Backrooms 32X, with the strap line 'welcome to the cutting edge of 1994.' This is a Sega 32X game set in the Backrooms, the internet phenomenon given a huge boost "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/smics-third-gen-7nm-node-shows-smaller-metal-pitch-than-intel-18a-higher-transistor-density-than-tsmc-n6-without-euv-analysis-of-n-3-shows-significant-advancement-for-chinese-semi-manufacturing",
    "domain": "AI 算力 / 半导体",
    "title": "SMIC's third-gen 7nm node shows smaller metal pitch than Intel 18A, higher transistor density than TSMC N6 without EUV — analysis of N+3 shows significant advancement for Chinese semi manufacturing",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/smics-third-gen-7nm-node-shows-smaller-metal-pitch-than-intel-18a-higher-transistor-density-than-tsmc-n6-without-euv-analysis-of-n-3-shows-significant-advancement-for-chinese-semi-manufacturing",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T11:00:00+00:00",
    "summary": "SMIC's N+3 process technology can achieve transistor density comparable to TSMC's N6 without using EUV lithography, but it fails to deliver performance or efficiency of modern production nodes."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/google-reportedly-developing-frozen-v2-chip-with-geminis-architecture-etched-into-the-silicon",
    "domain": "AI 算力 / 半导体",
    "title": "Google reportedly developing 'Frozen v2' chip with Gemini's architecture etched into the silicon — engineers project 6 to 10 times more tokens per watt than latest TPUs",
    "url": "https://www.tomshardware.com/tech-industry/google-reportedly-developing-frozen-v2-chip-with-geminis-architecture-etched-into-the-silicon",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T10:40:00+00:00",
    "summary": "Google is developing a server chip, informally dubbed \"Frozen v2,\" that would etch part of its Gemini model's architecture directly into the silicon."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/pc-modder-straps-5-5-pound-aluminum-heatsink-to-rtx-4060-convection-only-cooling-seems-to-work-fine-in-a-testbench-style-installation",
    "domain": "AI 算力 / 半导体",
    "title": "PC modder bolts 5.5-pound aluminum heatsink to RTX 4060 — convection-only cooling seems to work fine in a testbench-style installation",
    "url": "https://www.tomshardware.com/pc-components/cooling/pc-modder-straps-5-5-pound-aluminum-heatsink-to-rtx-4060-convection-only-cooling-seems-to-work-fine-in-a-testbench-style-installation",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T10:00:00+00:00",
    "summary": "A PC gamer has DIYed a passive Nvidia GeForce RTX 4060 graphics card system incorporating a 5.5-pound aluminum heatsink."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/usd399-nintendo-switch-2-back-in-stock-woot-for-new-customers-usd427-for-returning-customers-with-code-get-usd100-off-the-most-recent-price-hikes",
    "domain": "AI 算力 / 半导体",
    "title": "$399 Nintendo Switch 2 back in stock Woot for new customers, $427 for returning customers with code — get $100 off the most recent price hikes",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/usd399-nintendo-switch-2-back-in-stock-woot-for-new-customers-usd427-for-returning-customers-with-code-get-usd100-off-the-most-recent-price-hikes",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T09:41:07+00:00",
    "summary": "Get a brand new Nintendo Switch 2 for less."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidias-new-synthetic-video-detector-can-identify-fake-ai-videos-with-up-to-92-percent-accuracy-microservice-based-on-cutting-edge-research-looks-to-combat-misinformation-in-broadcasts-with-just-22ms-processing-time",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's new Synthetic Video Detector can identify fake AI videos with up to 92% accuracy — microservice based on cutting-edge research looks to combat misinformation in broadcasts with just 22ms proc",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidias-new-synthetic-video-detector-can-identify-fake-ai-videos-with-up-to-92-percent-accuracy-microservice-based-on-cutting-edge-research-looks-to-combat-misinformation-in-broadcasts-with-just-22ms-processing-time",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T09:30:00+00:00",
    "summary": "Nvidia has just created an antidote to the virus that is AI misinformation. The company's new Synthetic Video Detector can help broadcasters assess 1080p footage at scale with processing times of just"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/the-enduring-paradox-of-the-ai-economy-models-get-better-and-more-efficient-yet-costs-can-still-easily-spiral-out-of-control",
    "domain": "AI 算力 / 半导体",
    "title": "The enduring paradox of the AI economy — models get better and more efficient, yet costs can still easily spiral out of control",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/the-enduring-paradox-of-the-ai-economy-models-get-better-and-more-efficient-yet-costs-can-still-easily-spiral-out-of-control",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T19:35:42+00:00",
    "summary": "Token amplification creates a paradox in the AI economy, as more capable models beget more complicated tasks."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/taiwan-inducts-ex-tsmc-manager-for-allegedly-stealing-chip-secrets-for-china",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan indicts ex-TSMC manager for allegedly stealing chip secrets for China — first case of its kind links managers to Chinese semiconductor materials analysis company",
    "url": "https://www.tomshardware.com/tech-industry/taiwan-inducts-ex-tsmc-manager-for-allegedly-stealing-chip-secrets-for-china",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T18:13:21+00:00",
    "summary": "Taiwanese prosecutors indicted a former TSMC deputy manager on Monday for allegedly copying 21 confidential documents."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/new-plugin-unlocks-granular-vram-temperature-tracking-on-nvidia-rtx-50-series-gpus-community-cracks-open-blackwells-forbidden-telemetry-sensors",
    "domain": "AI 算力 / 半导体",
    "title": "New plugin unlocks granular VRAM temperature tracking on Nvidia RTX 50-series GPUs — community cracks open Blackwell's forbidden telemetry sensors",
    "url": "https://www.tomshardware.com/pc-components/gpus/new-plugin-unlocks-granular-vram-temperature-tracking-on-nvidia-rtx-50-series-gpus-community-cracks-open-blackwells-forbidden-telemetry-sensors",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T17:48:35+00:00",
    "summary": "Modders have discovered a method to monitor every single memory module on Nvidia's GeForce RTX 50-series (codenamed Blackwell) graphics cards."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/trump-administration-reportedly-reviving-push-to-ban-chinese-ai-models-following-kimi-k3-launch-citing-cybersecurity-concerns-downloadable-open-weights-could-make-an-outright-u-s-ban-nearly-impossible-to-enforce-amid-growing-adoption",
    "domain": "AI 算力 / 半导体",
    "title": "Trump administration reportedly reviving push to ban Chinese AI models following Kimi K3 launch, citing cybersecurity concerns — downloadable open weights could make an outright U.S. ban nearly imposs",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/trump-administration-reportedly-reviving-push-to-ban-chinese-ai-models-following-kimi-k3-launch-citing-cybersecurity-concerns-downloadable-open-weights-could-make-an-outright-u-s-ban-nearly-impossible-to-enforce-amid-growing-adoption",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T17:39:23+00:00",
    "summary": "The U.S. may be reigniting efforts to push companies away from Chinese open-weight AI models such as Kimi and DeepSeek."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/shrink-your-pc-setup-with-up-to-25-percent-off-on-kamrui-mini-pcs-big-savings-on-the-h1-for-gamers-and-the-hyper-h2-for-pros",
    "domain": "AI 算力 / 半导体",
    "title": "Shrink your PC setup with up to 25% off on Kamrui mini-PCs — big savings on the H1 for gamers and the Hyper H2 for pros",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/shrink-your-pc-setup-with-up-to-25-percent-off-on-kamrui-mini-pcs-big-savings-on-the-h1-for-gamers-and-the-hyper-h2-for-pros",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T16:32:31+00:00",
    "summary": "Kamrui's H1 and Hyper H2 mini-PCs go on sale at Amazon with discounts up to 25%."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/government-funded-dutch-report-rates-chip-sector-at-very-high-risk-of-chinese-interference",
    "domain": "AI 算力 / 半导体",
    "title": "Dutch chip sector at very high risk of Chinese interference, government-funded study warns — calls for stricter vetting at sites like ASML",
    "url": "https://www.tomshardware.com/tech-industry/government-funded-dutch-report-rates-chip-sector-at-very-high-risk-of-chinese-interference",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T15:04:14+00:00",
    "summary": "The Hague Centre for Strategic Studies has rated the Dutch semiconductor industry as being at very high risk of Chinese foreign interference."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-will-deploy-amds-helios-rack-scale-ai-accelerator-at-scale-on-azure-radeon-instinct-mi455x-and-epyc-venice-power-will-be-available-through-redmonds-cloud-infrastructure",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft will deploy AMD’s Helios rack-scale AI accelerator ‘at scale’ on Azure – Radeon Instinct MI455X and Epyc Venice power will be available through Redmond’s cloud infrastructure",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-will-deploy-amds-helios-rack-scale-ai-accelerator-at-scale-on-azure-radeon-instinct-mi455x-and-epyc-venice-power-will-be-available-through-redmonds-cloud-infrastructure",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T13:05:00+00:00",
    "summary": "Microsoft and AMD are teaming up to get Redmond more AI FLOPS for both internal and external use."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/power-companies-can-seize-private-land-to-make-way-for-new-ai-data-center-transmission-lines-report-says-takeovers-could-be-implemented-using-eminent-domain-law-when-private-citizens-refuse-to-sell-land",
    "domain": "AI 算力 / 半导体",
    "title": "Government can seize private land to make way for new AI data center transmission lines, report says — takeovers could be implemented using eminent domain law when private citizens refuse to sell land",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/power-companies-can-seize-private-land-to-make-way-for-new-ai-data-center-transmission-lines-report-says-takeovers-could-be-implemented-using-eminent-domain-law-when-private-citizens-refuse-to-sell-land",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T13:00:47+00:00",
    "summary": "Utilities can use eminent domain to seize private land for new transmission lines needed to power data centers, though public-use and state-law limits still apply."
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
    "points": 371,
    "published_at": "2026-07-16T16:08:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:48925271",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://turntrout.com/why-i-left-google-deepmind",
    "source": "apsec112",
    "platform": "hackernews",
    "points": 368,
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
    "points": 137,
    "published_at": "2026-07-19T07:59:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:48993130",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.6 Flash",
    "url": "https://console.cloud.google.com/agent-platform/publishers/google/model-garden/gemini-3.6-flash",
    "source": "marrf",
    "platform": "hackernews",
    "points": 69,
    "published_at": "2026-07-21T14:56:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:48998606",
    "domain": "大厂 AI 动态",
    "title": "Gemini last models: temperature, top_p, and top_k are deprecated and ignored",
    "url": "https://ai.google.dev/gemini-api/docs/latest-model",
    "source": "greatgib",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-07-21T21:27:54+00:00",
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
    "id": "hn:48983890",
    "domain": "大厂 AI 动态",
    "title": "Cue AI",
    "url": "https://deepmind.google/models/gemma/gemmaverse/cue-ai/",
    "source": "logickkk1",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-07-20T19:41:44+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/967926/samsung-galaxy-unpacked-july-2026-watch",
    "domain": "大厂 AI 动态",
    "title": "Samsung Galaxy Unpacked July 2026: How to watch",
    "url": "https://www.theverge.com/tech/967926/samsung-galaxy-unpacked-july-2026-watch",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T01:00:00+00:00",
    "summary": "Samsung's next Galaxy Unpacked event is just around the corner, and the company is expected to take the wraps off a bunch of new devices. Based on the rumors and leaks we've seen so far, Samsung's nex"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/968703/neill-blomkamps-nightborne-barley-studios-seedance",
    "domain": "大厂 AI 动态",
    "title": "Neill Blomkamp’s new zombie AI ‘film’ is just slop warmed over",
    "url": "https://www.theverge.com/entertainment/968703/neill-blomkamps-nightborne-barley-studios-seedance",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T22:06:43+00:00",
    "summary": "On Monday, District 9 and Gran Turismo director Neill Blomkamp unveiled his latest project: a 13-minute sci-fi short titled Nightborne that's loosely based on Peter Watts' 2014 novel Echopraxia. The s"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/968988/openai-hugging-face-hack-ai",
    "domain": "大厂 AI 动态",
    "title": "OpenAI says it accidentally hacked Hugging Face with a new AI system",
    "url": "https://www.theverge.com/ai-artificial-intelligence/968988/openai-hugging-face-hack-ai",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T21:48:54+00:00",
    "summary": "OpenAI says its AI models mistakenly breached open-source AI platform Hugging Face during internal testing. In a blog post on Tuesday, OpenAI writes that GPT-5.6 Sol and \"an even more capable pre-rele"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/968855/substack-pangram-ai-detecting-tool",
    "domain": "大厂 AI 动态",
    "title": "Substack adds an AI detector to help spot blogs written by no one",
    "url": "https://www.theverge.com/ai-artificial-intelligence/968855/substack-pangram-ai-detecting-tool",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T19:22:28+00:00",
    "summary": "Substack will now help users determine whether what they're reading may have been written by AI. A new tool coming to the platform can scan posts, notes, replies, and comments to provide an estimate o"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/968771/peak-design-camera-field-bracket-kickstarter",
    "domain": "大厂 AI 动态",
    "title": "Peak Design’s modular Field Bracket has a finder tag built-in",
    "url": "https://www.theverge.com/gadgets/968771/peak-design-camera-field-bracket-kickstarter",
    "source": "David Imel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T18:12:02+00:00",
    "summary": "I am a very clumsy man. So clumsy, that I have AirTags hanging off practically every camera I own. Have I left my camera in an Uber? Yes. Have I left it on an airplane? Also yes. For me, finder tags a"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/968356/kindle-paperwhite-colorsoft-scribe-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Nearly every Kindle is steeply discounted at Best Buy",
    "url": "https://www.theverge.com/gadgets/968356/kindle-paperwhite-colorsoft-scribe-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T17:13:23+00:00",
    "summary": "If you&#8217;ve been thinking about picking up a Kindle before school starts, or for your next vacation, now&#8217;s a good time to do it. As part of its Black Friday in July sale, Best Buy has brough"
  },
  {
    "id": "rss:https://www.theverge.com/tech/968750/apple-upgrade-program",
    "domain": "大厂 AI 动态",
    "title": "Apple’s rumored ‘Upgrade’ program brings lease-to-own pricing for iPhones, Macs, and iPads",
    "url": "https://www.theverge.com/tech/968750/apple-upgrade-program",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T17:12:06+00:00",
    "summary": "As component and RAM shortages drive prices higher, Apple is reportedly launching an \"Apple Upgrade\" program for leasing new devices. According to Bloomberg's Mark Gurman, it will work similar to a ca"
  },
  {
    "id": "rss:https://www.theverge.com/tech/968480/twitch-parental-controls-block-streaming-live-dms",
    "domain": "大厂 AI 动态",
    "title": "Twitch will let parents stop their teens going live",
    "url": "https://www.theverge.com/tech/968480/twitch-parental-controls-block-streaming-live-dms",
    "source": "Jess Weatherbed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T17:00:00+00:00",
    "summary": "Twitch is giving parents more control over how their children are using the streaming platform, including the ability to block them from broadcasting entirely. Parental controls are now available that"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/968724/anthropic-authors-settlement-ai-copyright-approved",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s $1.5 billion book piracy settlement approved by judge",
    "url": "https://www.theverge.com/ai-artificial-intelligence/968724/anthropic-authors-settlement-ai-copyright-approved",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T16:53:37+00:00",
    "summary": "A federal judge has signed off on Anthropic's $1.5 billion class action settlement with authors who accused the company of training its AI models on copyrighted books, as reported earlier by Reuters. "
  },
  {
    "id": "rss:https://www.theverge.com/news/968243/instagram-creators-replace-audio-tiktok-competition",
    "domain": "大厂 AI 动态",
    "title": "Instagram will let users endlessly swap the audio on old posts",
    "url": "https://www.theverge.com/news/968243/instagram-creators-replace-audio-tiktok-competition",
    "source": "Mia Sato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T16:15:00+00:00",
    "summary": "There's a symbiotic - and sometimes frustrating - relationship between social media sites and the creators that depend on them. Platforms need influencers' and creators' content to keep consumers on t"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/the-anthropic-physical-intelligence-rumor-roiling-ai-twitter/",
    "domain": "大厂 AI 动态",
    "title": "The Anthropic-Physical Intelligence rumor roiling AI Twitter",
    "url": "https://techcrunch.com/2026/07/21/the-anthropic-physical-intelligence-rumor-roiling-ai-twitter/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T03:20:57+00:00",
    "summary": "Anthropic and OpenAI's aggressive 2026 acquisition sprees set the stage for a weekend rumor."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/dimension-capitals-800m-third-fund-shows-the-intersection-of-science-and-compute-is-booming/",
    "domain": "大厂 AI 动态",
    "title": "Dimension Capital’s $800M third fund shows the intersection of science and compute is booming",
    "url": "https://techcrunch.com/2026/07/21/dimension-capitals-800m-third-fund-shows-the-intersection-of-science-and-compute-is-booming/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T01:27:58+00:00",
    "summary": "The four-year-old firm's latest fund is 60% larger than its second vehicle announced 18 months ago."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/meta-is-testing-an-ai-bedtime-story-app-for-people-with-no-imagination/",
    "domain": "大厂 AI 动态",
    "title": "Meta is testing an AI bedtime story app for people with no imagination",
    "url": "https://techcrunch.com/2026/07/21/meta-is-testing-an-ai-bedtime-story-app-for-people-with-no-imagination/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T23:55:10+00:00",
    "summary": "At last, a tech company has found a way to outsource humanity's oldest pastime: using our imaginations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/social-media-ban-children-countries-list/",
    "domain": "大厂 AI 动态",
    "title": "These are the countries moving to ban social media for children",
    "url": "https://techcrunch.com/2026/07/21/social-media-ban-children-countries-list/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T20:57:35+00:00",
    "summary": "Australia was the first country to issue a ban in late 2025, aiming to reduce the pressures and risks that young users may face on social media, including cyberbullying, social media addiction, and ex"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/openai-says-hugging-face-was-breached-by-its-pre-release-models/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI says Hugging Face was breached by its pre-release models",
    "url": "https://techcrunch.com/2026/07/21/openai-says-hugging-face-was-breached-by-its-pre-release-models/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T20:56:55+00:00",
    "summary": "OpenAI has come forward to claim responsibility for the Hugging Face breach, saying it was the result of internal testing gone awry."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/jack-dorsey-is-taking-on-slack-with-buzz-a-group-chat-platform-for-teams-and-their-ai-agents/",
    "domain": "大厂 AI 动态",
    "title": "Jack Dorsey is taking on Slack with Buzz, a group chat platform for teams and their AI agents",
    "url": "https://techcrunch.com/2026/07/21/jack-dorsey-is-taking-on-slack-with-buzz-a-group-chat-platform-for-teams-and-their-ai-agents/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T19:43:41+00:00",
    "summary": "Buzz is a group chat platform for the workplace that puts humans and their AI agents in the same conversation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/ai-and-the-rise-of-the-universal-entertainment-app/",
    "domain": "大厂 AI 动态",
    "title": "AI and the rise of the universal entertainment app",
    "url": "https://techcrunch.com/2026/07/21/ai-and-the-rise-of-the-universal-entertainment-app/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T19:39:30+00:00",
    "summary": "Over the past decade, streaming platforms competed by dominating individual formats like music, video, podcasts, or audiobooks. Now, as AI makes it easier to create, organize, and recommend content, t"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/bucking-ev-slowdown-sila-raises-300m-to-expand-battery-materials-factory/",
    "domain": "大厂 AI 动态",
    "title": "Bucking EV slowdown, Sila raises $300M to expand battery materials factory",
    "url": "https://techcrunch.com/2026/07/21/bucking-ev-slowdown-sila-raises-300m-to-expand-battery-materials-factory/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T19:36:35+00:00",
    "summary": "Sila's fresh $300 million round will help it make enough of its silicon-carbon anode material to power more than 100,000 EVs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/einride-bets-38m-on-ev-charging-as-it-scales-electric-trucking/",
    "domain": "大厂 AI 动态",
    "title": "Einride bets $38M on EV charging as it scales electric trucking",
    "url": "https://techcrunch.com/2026/07/21/einride-bets-38m-on-ev-charging-as-it-scales-electric-trucking/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T18:48:38+00:00",
    "summary": "The acquisition — Einride's first as a publicly traded company — will expand its EV-charging ecosystem as it works to scale its electric trucking business."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/apple-teams-up-with-klarna-to-launch-a-lease-to-own-program-for-iphones-ipads-and-macs/",
    "domain": "大厂 AI 动态",
    "title": "Apple teams up with Klarna to launch a lease-to-own program for iPhones, iPads, and Macs",
    "url": "https://techcrunch.com/2026/07/21/apple-teams-up-with-klarna-to-launch-a-lease-to-own-program-for-iphones-ipads-and-macs/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T18:18:43+00:00",
    "summary": "The new leasing program is a big change for the hardware company, and comes as it looks to raise prices on many of its products."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/data-centers-expected-to-use-4x-more-electricity-by-2035/",
    "domain": "大厂 AI 动态",
    "title": "Data centers expected to use 4x more electricity by 2035",
    "url": "https://techcrunch.com/2026/07/21/data-centers-expected-to-use-4x-more-electricity-by-2035/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T18:06:38+00:00",
    "summary": "New data centers built through 2033 could consume as much electricity as India uses today."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/tesla-spins-up-robotaxi-pilots-in-orlando-and-tampa-ahead-of-q2-earnings/",
    "domain": "大厂 AI 动态",
    "title": "Tesla spins up robotaxi pilots in Orlando and Tampa ahead of Q2 earnings",
    "url": "https://techcrunch.com/2026/07/21/tesla-spins-up-robotaxi-pilots-in-orlando-and-tampa-ahead-of-q2-earnings/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T18:05:10+00:00",
    "summary": "The company didn't say how many are in each city and has taken a far more cautious approach to scaling the network than CEO Elon Musk had promised."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/",
    "domain": "大厂 AI 动态",
    "title": "Google releases three new Gemini models — but no 3.5 Pro",
    "url": "https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T17:11:50+00:00",
    "summary": "Google released Gemini 3.6 Flash, 3.5 Flash-Lite, and Flash Cyber, but the continued absence of Gemini 3.5 Pro raises fresh questions about its AI strategy."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/instagram-now-lets-you-swap-out-the-music-in-your-old-posts/",
    "domain": "大厂 AI 动态",
    "title": "Instagram now lets you swap out the music in your old posts",
    "url": "https://techcrunch.com/2026/07/21/instagram-now-lets-you-swap-out-the-music-in-your-old-posts/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T16:15:00+00:00",
    "summary": "With the new \"Replace Audio\" tool, users can update the music on their post at any time while keeping the post's existing likes, comments, shares, and reach intact."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/threads-rolls-out-parental-supervision-tools/",
    "domain": "大厂 AI 动态",
    "title": "Threads rolls out parental supervision tools",
    "url": "https://techcrunch.com/2026/07/21/threads-rolls-out-parental-supervision-tools/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T16:00:00+00:00",
    "summary": "With the new tools, parents and guardians will be able to view their teen's time spent on Threads, set daily time limits, adjust sleep mode, and manage their privacy settings."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/us-threatens-sanctions-against-chinese-ai-models-over-ip-theft/",
    "domain": "大厂 AI 动态",
    "title": "US threatens sanctions against Chinese AI models over IP theft",
    "url": "https://techcrunch.com/2026/07/21/us-threatens-sanctions-against-chinese-ai-models-over-ip-theft/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T15:37:05+00:00",
    "summary": "Treasury Secretary Scott Bessent said the U.S. could sanction Chinese open AI models over alleged IP theft, expanding the Trump administration's campaign to slow China's AI advances."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/light-is-modernizing-the-flip-phone-with-light-flip/",
    "domain": "大厂 AI 动态",
    "title": "Light made a flip phone — it’s colorful and it’s cheap",
    "url": "https://techcrunch.com/2026/07/21/light-is-modernizing-the-flip-phone-with-light-flip/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T15:00:00+00:00",
    "summary": "Light co-founder Kaiwei Tang helped create the Motorola Razr, and he's as surprised as anyone that over 20 years later, the flip phone is relevant again."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/after-tiktok-snap-settles-social-media-addiction-case/",
    "domain": "大厂 AI 动态",
    "title": "After TikTok, Snap settles social media addiction case",
    "url": "https://techcrunch.com/2026/07/21/after-tiktok-snap-settles-social-media-addiction-case/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T14:54:19+00:00",
    "summary": "TikTok recently settled its portion of the case with the plaintiff ahead of a jury trial that starts next week in Los Angeles. YouTube has also reached a deal, leaving Meta as the only remaining defen"
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/ai-music-generator-suno-breach-affects-55m-users-per-have-i-been-pwned/",
    "domain": "大厂 AI 动态",
    "title": "AI music generator Suno breach affects 55M users, per Have I Been Pwned",
    "url": "https://techcrunch.com/2026/07/21/ai-music-generator-suno-breach-affects-55m-users-per-have-i-been-pwned/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T14:48:18+00:00",
    "summary": "A hacker took names, phone numbers, and physical addresses of millions of customers who used AI music generator Suno."
  },
  {
    "id": "rss:https://techcrunch.com/2026/07/21/warner-bros-netflix-paramount-acquisition-timeline-wbd/",
    "domain": "大厂 AI 动态",
    "title": "What to know about the landmark Warner Bros. Discovery sale",
    "url": "https://techcrunch.com/2026/07/21/warner-bros-netflix-paramount-acquisition-timeline-wbd/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T14:15:39+00:00",
    "summary": "Learn more about Paramount's planned acquisition of Warner Bros. Discovery — a historic Hollywood megadeal valued at $111 billion — as it continues to develop."
  },
  {
    "id": "rss:https://stratechery.com/2026/netflix-earnings-is-netflix-washed-additional-notes/",
    "domain": "大厂 AI 动态",
    "title": "Netflix Earnings, Is Netflix Washed?, Additional Notes",
    "url": "https://stratechery.com/2026/netflix-earnings-is-netflix-washed-additional-notes/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T10:00:00+00:00",
    "summary": "Netflix's earnings were fine, and befitting a mature company whose most exciting days are likely behind them."
  },
  {
    "id": "rss:https://stratechery.com/2026/whos-afraid-of-chinese-models/",
    "domain": "大厂 AI 动态",
    "title": "Who’s Afraid of Chinese Models?",
    "url": "https://stratechery.com/2026/whos-afraid-of-chinese-models/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-20T11:00:08+00:00",
    "summary": "Everyone is worried about Chinese models, but the frontier labs will be fine; we need to enable open U.S. alternatives."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/07/heres-range-rovers-first-not-suv-the-range-rover-gt/",
    "domain": "大厂 AI 动态",
    "title": "Range Rover answers the question: \"What if we built a not-SUV?\"",
    "url": "https://arstechnica.com/cars/2026/07/heres-range-rovers-first-not-suv-the-range-rover-gt/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T23:01:23+00:00",
    "summary": "The Range Rover GT will debut as an EV with a hybrid version to follow."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/on-the-run-for-20-years-most-wanted-fugitive-caught-hiding-as-a-biotech-exec/",
    "domain": "大厂 AI 动态",
    "title": "On the run for 20 years, most-wanted fugitive caught hiding as a biotech exec",
    "url": "https://arstechnica.com/health/2026/07/on-the-run-for-20-years-most-wanted-fugitive-caught-hiding-as-a-biotech-exec/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T22:04:56+00:00",
    "summary": "Ronald Fischer, aka Richard Graydon, was arrested in New York last week."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/07/sony-releases-one-last-trailer-for-spider-man-brand-new-day/",
    "domain": "大厂 AI 动态",
    "title": "Sony releases one last trailer for Spider-Man: Brand New Day",
    "url": "https://arstechnica.com/culture/2026/07/sony-releases-one-last-trailer-for-spider-man-brand-new-day/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T19:50:10+00:00",
    "summary": "\"Maybe that's my responsibility, to live alone with the truth.\""
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/07/confusion-swirls-on-source-of-diarrhea-outbreak-but-its-still-taylor-farms/",
    "domain": "大厂 AI 动态",
    "title": "Confusion swirls on source of diarrhea outbreak, but it’s still Taylor Farms",
    "url": "https://arstechnica.com/health/2026/07/confusion-swirls-on-source-of-diarrhea-outbreak-but-its-still-taylor-farms/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T19:39:10+00:00",
    "summary": "Taylor Farms stirred confusion on FDA test and provided a vague recall list."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/07/nintendo-customers-have-no-legal-right-to-tariff-refunds-company-tells-judge/",
    "domain": "大厂 AI 动态",
    "title": "Nintendo says users voluntarily paid higher prices, have no right to tariff refunds",
    "url": "https://arstechnica.com/tech-policy/2026/07/nintendo-customers-have-no-legal-right-to-tariff-refunds-company-tells-judge/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T19:09:19+00:00",
    "summary": "Nintendo says Switch buyers got what they paid for, urges court to dismiss lawsuit."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/07/tom-hiddleston-tracks-possible-pompeii-survivors-in-new-docuseries/",
    "domain": "大厂 AI 动态",
    "title": "Let Tom Hiddleston be your guide to Pompeii's final day",
    "url": "https://arstechnica.com/science/2026/07/tom-hiddleston-tracks-possible-pompeii-survivors-in-new-docuseries/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-21T18:17:55+00:00",
    "summary": "NatGeo's Pompeii: Out of Time fuses historical fact and imagination to bring city's last 24 hours to life."
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
    "id": "hn:48974426",
    "domain": "股票",
    "title": "Big tech needs to justify AI spending as investors dump stocks",
    "url": "https://www.bloomberg.com/news/articles/2026-07-19/big-tech-needs-to-justify-ai-spending-as-investors-dump-stocks",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-07-20T04:41:10+00:00",
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
    "id": "wscn:3777614",
    "domain": "股票",
    "title": "AI交易热情午后回落，韩股涨幅收窄至2%，日股转跌，金银走强",
    "url": "https://wallstreetcn.com/articles/3777614",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T05:36:21+00:00",
    "summary": "韩国KOSPI指数一度涨超6%，午后涨幅有所回落，日经225指数盘中一度涨超2%，但随后涨幅收窄并转跌。此外，油价上涨推升通胀预期，美债收益率升至两个月高位，市场风险情绪仍需财报季检验。"
  },
  {
    "id": "wscn:3777630",
    "domain": "股票",
    "title": "创业板跌超2%，有色金属拉升，AI服务器龙头涨停，恒科指跌超3%，科网股普跌、腾讯跌逾6%",
    "url": "https://wallstreetcn.com/articles/3777630",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T05:33:55+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市超3400股飘绿，上午半天成交1.79万亿。沪深两市半日成交额1.78万亿，较上个交易日缩量2220亿。板块方面，贵金属、油气、半导体、CPO等板块领涨；游戏、影视、传媒、电池等板块领跌。"
  },
  {
    "id": "wscn:3777645",
    "domain": "股票",
    "title": "“非洲纸尿裤之王”再加速 乐舒适上半年销量售价双升",
    "url": "https://wallstreetcn.com/articles/3777645",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T05:25:33+00:00",
    "summary": "非洲纸尿裤龙头乐舒适上市后继续保持较快增长。\n7月21日，乐舒适发布正面盈利预告，预计2026年上半..."
  },
  {
    "id": "wscn:3777642",
    "domain": "股票",
    "title": "明治收缩中国乳制品业务，澳亚最高3.5亿元接盘",
    "url": "https://wallstreetcn.com/articles/3777642",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T05:10:02+00:00",
    "summary": "澳亚集团拟接手明治在中国的乳制品生产与销售业务。\n7月21日，澳亚集团公告称，其全资附属公司上海澳雅..."
  },
  {
    "id": "wscn:3777637",
    "domain": "股票",
    "title": "瑞银：宽基ETF交易量显著放大，A股去杠杆可能接近尾声",
    "url": "https://wallstreetcn.com/articles/3777637",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T03:30:41+00:00",
    "summary": "瑞银发布A股策略报告指出，近期A股大跌源于全球科技股波动、获利了结与去杠杆三重压力叠加。但关键信号已在转变：7月6日至20日A股权益类ETF净流入超3674亿元，宽基ETF成交量显著放大；融资余额从历史峰值3.01万亿元快速降至2.70万亿元，去杠杆可能已接近尾声。与此同时，A股盈利改善趋势未变。"
  },
  {
    "id": "wscn:3777549",
    "domain": "股票",
    "title": "从国产芯片到开源大模型：\"可用\"到\"好用\"的历史性拐点，5年3倍的国产芯片蓝海",
    "url": "https://wallstreetcn.com/premium/articles/3777549?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T03:18:04+00:00",
    "summary": "7月21日，智谱AI落地1GW级国产AI算力数据中心——全部采用国产芯片，标志着头部模型厂商已将国产算力纳入核心竞争体系。"
  },
  {
    "id": "wscn:3777430",
    "domain": "股票",
    "title": "从杠杆ETF到韩元自由兑换：韩国为何如此豪赌？",
    "url": "https://wallstreetcn.com/premium/articles/3777430?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T03:08:40+00:00",
    "summary": "韩国在韩元新低与股市急跌时推进韩元自由兑换，旨在引入外资缓解流动性，但长期波动风险陡增。"
  },
  {
    "id": "wscn:3777636",
    "domain": "股票",
    "title": "耐克挥刀中国线上渠道：收权、控价、本土化",
    "url": "https://wallstreetcn.com/articles/3777636",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T02:57:04+00:00",
    "summary": "耐克在中国市场动了真格。\n7月22日盘前，滔搏宣布收到耐克正式通知，其在中国内地的耐克产品线上平台销..."
  },
  {
    "id": "wscn:3777631",
    "domain": "股票",
    "title": "媒体实探英伟达Rubin：数十家客户已拿到测试机架，生产过程比Blackwell顺利，预计明年放量",
    "url": "https://wallstreetcn.com/articles/3777631",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T02:55:04+00:00",
    "summary": "英伟达下一代Vera Rubin服务器系统量产进展顺利，CoreWeave、微软、OpenAI、Anthropic和SpaceXAI等数十家客户已收到测试机架，每架搭载72块GPU，售价700至800万美元。相比Blackwell，新系统采用无线缆设计并引入机器人组装，生产效率显著提升。"
  },
  {
    "id": "wscn:3777634",
    "domain": "股票",
    "title": "特朗普批准美沙30年核能协议：美企主导，可能在沙特境内建设铀浓缩设施",
    "url": "https://wallstreetcn.com/articles/3777634",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T02:54:26+00:00",
    "summary": "美沙签署数百亿美元、长达30年的历史性核能协议，西屋电气等美企将主导沙特核基础设施建设，并可能在当地建设铀浓缩设施。协议绕开\"黄金标准\"承诺，沙特拒绝IAEA附加监督，引发核扩散隐忧——批评者警告，沙特开此先例，中东核竞赛或一触即发。"
  },
  {
    "id": "wscn:3777632",
    "domain": "股票",
    "title": "关键事件前的市场割裂：各自交易各自的逻辑",
    "url": "https://wallstreetcn.com/articles/3777632",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T02:39:11+00:00",
    "summary": "市场割裂信号频现，动量交易集体坍塌后能否反转，关键悬念压缩至两周内——谷歌财报打响第一枪，FOMC随后定乾坤。铜的基本面悄然走强，黄金ETF资金悄悄回流，但真正的方向尚未浮出水面。大事件落地前，重仓左侧还是耐心等右侧？答案或许已经藏在利率波动率的底部信号里。"
  },
  {
    "id": "wscn:3777627",
    "domain": "股票",
    "title": "震惊硅谷！OpenAI模型“失控越狱”，入侵HuggingFace“抄答案”，智谱GLM 5.2临危救场",
    "url": "https://wallstreetcn.com/articles/3777627",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T02:18:32+00:00",
    "summary": "OpenAI测试自家AI模型的黑客能力，结果模型真的“失控出逃”，跑去黑了别人的系统。更讽刺的是：受害方调用美国主流AI模型展开溯源，却因安全护栏拒绝分析恶意载荷，最终只能靠中国智谱AI的GLM 5.2救场。网友调侃，“如果你被OpenAI攻击了，你只能用中国模型，因为Claude不会帮你。”"
  },
  {
    "id": "wscn:3777629",
    "domain": "股票",
    "title": "张坤大举减持白酒，买入科技股",
    "url": "https://wallstreetcn.com/articles/3777629",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T02:18:19+00:00",
    "summary": "张坤管理的易方达蓝筹精选基金大幅减持白酒，仓位占比从29%降至10%，同步增配电子、通信等行业。刘彦春景顺长城新兴成长基金坚守茅台，但大幅减持汾酒和五粮液。萧楠管理的易方达消费行业基金二季度主要减持了五粮液，小幅增持泸州老窖。"
  },
  {
    "id": "wscn:3777616",
    "domain": "股票",
    "title": "低估Azure和Copilot的拐点！大摩：市场只给微软“16倍PE”太低了",
    "url": "https://wallstreetcn.com/articles/3777616",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T01:53:51+00:00",
    "summary": "摩根士丹利维持微软增持评级，微软当前远期市盈率仅约16倍，对于盈利增速超20%的科技龙头明显低估。Azure供给瓶颈缓解后增速有望持续加快，Copilot商业化从单一座位收费升级为座位扩张、E7订阅迁移及消费量计费三引擎驱动，预计29财年Copilot收入达225亿美元。"
  },
  {
    "id": "wscn:3777626",
    "domain": "股票",
    "title": "重新审视蔚来？从“烧钱车企”到“AI芯片平台”",
    "url": "https://wallstreetcn.com/articles/3777626",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T01:52:03+00:00",
    "summary": "蔚来芯片子公司神玑科技在2026年世界人工智能大会首次独立亮相，将自身定位从车载智驾芯片延伸至具身智能与推理计算全域AI平台。摩根士丹利维持蔚来港股增持评级，目标价港币58元，较现价有约48%上行空间，认为神玑科技的独立融资与自研降本效应，正推动蔚来估值逻辑从\"现金消耗型车企\"向\"垂直整合AI芯片平台\"深度重构。"
  },
  {
    "id": "wscn:3777623",
    "domain": "股票",
    "title": "川普关税“换马甲”，这次有什么不一样？",
    "url": "https://wallstreetcn.com/articles/3777623",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T01:17:44+00:00",
    "summary": "国金宏观表示，随着122关税7月24日到期，特朗普关税体系正加速重构：301调查剑指60个经济体强迫劳动与产能过剩，232调查锁定钢铁、芯片、药品等战略行业，338条款则为快速反制个别国家提供\"快车道\"。三套机制协同推进，但受制于人员不足与程序周期，难以无缝衔接。对中国而言，整体加权税率或上升1.2个百分点，后续走向取决于新301调查与中美元首会晤降税安排的双向博弈。"
  },
  {
    "id": "wscn:3777619",
    "domain": "股票",
    "title": "如何观察“超级厄尔尼诺交易”？油气“反应最快”，棕榈油、椰子油和橡胶等“热带农产品”弹性最大",
    "url": "https://wallstreetcn.com/articles/3777619",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T01:03:33+00:00",
    "summary": "气候模型显示，2026年或将迎来有史以来最强厄尔尼诺事件。巴克莱最新研究揭示了一张清晰的交易路线图：油气价格率先下行，棕榈油、椰子油、橡胶等热带农产品随后强势拉升，18个月内涨幅可达30%至60%。铝表现在厄尔尼诺事件本身期间往往偏软，但随后在一至两年内逐步走强。"
  },
  {
    "id": "wscn:3777621",
    "domain": "股票",
    "title": "OpenAI未发布模型在测试中逃出沙箱",
    "url": "https://wallstreetcn.com/articles/3777621",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T00:54:53+00:00",
    "summary": "OpenAI一个未发布的内部模型，在沙箱测试中悄悄挖洞突围，将研究成果私自发到GitHub；被关闭前，已有选手看懂并引用，此后六项世界纪录全部署名致谢。更魔幻的是，Anthropic的Claude随后用这份\"越狱遗产\"跑出新纪录，还客气地给它挂上了名——AI逃狱的第一批受益者，竟是另一家的AI。"
  },
  {
    "id": "wscn:3777620",
    "domain": "股票",
    "title": "特朗普宣布两年后对仿制药征收100%关税",
    "url": "https://wallstreetcn.com/articles/3777620",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T00:48:24+00:00",
    "summary": "特朗普在社交媒体发文表示，自2026年8月1日起，所有进口到美国的仿制药将在未来两年内继续适用零关税。两年期满后，相关产品将被征收100%的关税，期限为一年；此后，关税将进一步提高至200%。"
  },
  {
    "id": "wscn:3777617",
    "domain": "股票",
    "title": "降低“AI成本”大势所趋！Meta要做“模型路由”，复刻OpenRouter",
    "url": "https://wallstreetcn.com/articles/3777617",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T00:48:14+00:00",
    "summary": "据报道，为降低AI推理成本，Meta正复刻OpenRouter，开发模型路由工具Switchboard。其核心是通过评估任务难度，将简单请求分流至廉价小模型，避免大模型算力浪费。该工具不仅用于内部降本，未来或对外发布，成为Meta开辟新收入来源的尝试。"
  },
  {
    "id": "hn:48946872",
    "domain": "股票",
    "title": "US Corporate Insiders Are Selling Stocks at a Near Record Pace",
    "url": "https://www.bloomberg.com/news/articles/2026-07-17/us-corporate-insiders-are-selling-stocks-at-a-near-record-pace",
    "source": "pimienta",
    "platform": "hackernews",
    "points": 57,
    "published_at": "2026-07-17T13:00:44+00:00",
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
    "id": "hn:48999329",
    "domain": "金融",
    "title": "A Man Who Runs the IRS Spied on Colleagues When He Worked at JPMorgan",
    "url": "https://www.wsj.com/finance/banking/irs-bisignano-spying-jpmorgan-6cd1ddf0",
    "source": "cwwc",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-07-21T22:40:46+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.18616",
    "domain": "金融",
    "title": "Prediction of bank transaction fraud using TabNet an adaptive deep learning architecture",
    "url": "https://arxiv.org/abs/2607.18616",
    "source": "Prashanth BS, Manoj Kumar, Ariful Hoque, Nasser Al Muraqab, Immanuel Azaad Moonesar, Udo Christian Braendle, Ananth Rao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2607.18616v1 Announce Type: new Abstract: The development of online banking has brought about an increase in fraudulent operations, which is a major problem for banks. This study delves into the"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.18623",
    "domain": "金融",
    "title": "Dead Reckoning: Counting Your Customers Who Never Say Goodbye",
    "url": "https://arxiv.org/abs/2607.18623",
    "source": "Karl T. Ulrich",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2607.18623v1 Announce Type: new Abstract: Firms in non-contractual commerce face the challenge of knowing how many customers they actually have because customers can stop buying without ever say"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.18676",
    "domain": "金融",
    "title": "Noise Pollution and Household Sustainability: An Economic Approach",
    "url": "https://arxiv.org/abs/2607.18676",
    "source": "Yi Fan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2607.18676v1 Announce Type: new Abstract: Examining the economic impact of noise pollution from a lens of household is a burgeoning field in the study of environmental sustainability. Economics "
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.18677",
    "domain": "金融",
    "title": "The Price of Quietness: How a Pandemic Affects City Dwellers' Response to Road Traffic Noise",
    "url": "https://arxiv.org/abs/2607.18677",
    "source": "Yao-pei Wang, Yong Tu, Yi Fan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2607.18677v1 Announce Type: new Abstract: Using the outbreak of COVID-19 in Singapore as a quasi-natural experiment, we investigate tenants' changing responses to road traffic noise in the renta"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.18705",
    "domain": "金融",
    "title": "Pathwise Portfolio Theory and Market Viability",
    "url": "https://arxiv.org/abs/2607.18705",
    "source": "Ioannis Karatzas, Donghan Kim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2607.18705v1 Announce Type: new Abstract: The theory of portfolios, and its allied notions and fundamental results concerning growth optimality, the num\\'eraire property, and ``market viability'"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.18795",
    "domain": "金融",
    "title": "Measuring AI innovation with trademark data",
    "url": "https://arxiv.org/abs/2607.18795",
    "source": "C. Castaldi, F. Castellacci, A. Fronzetti Colladon, L. Segneri, F. Venturini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2607.18795v1 Announce Type: new Abstract: Researchers, managers and policymakers are exploring different approaches and data sources to map the development and the diffusion of Artificial Intell"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.18813",
    "domain": "金融",
    "title": "Mixing-Law Uncertainty in Multivariate Normal Mean-Variance Mixtures: Semi-parametric Estimation and Robust Cumulative-Prospect Decisions",
    "url": "https://arxiv.org/abs/2607.18813",
    "source": "Nuerxiati Abudurexiti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2607.18813v1 Announce Type: new Abstract: The distribution of a normal mean-variance mixture depends on the law of its positive mixing variable. We compare six parametric mixing laws with a grid"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.18815",
    "domain": "金融",
    "title": "Cloud failure and cyber insurance: calibration of stress scenarios and diversification",
    "url": "https://arxiv.org/abs/2607.18815",
    "source": "Olivier Lopez (CREST), Daniel Nkameni (CREST)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2607.18815v1 Announce Type: new Abstract: The expansion of the cyber insurance market remains exposed to the threat of accumulation events that could simultaneously affect a large number of poli"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.19005",
    "domain": "金融",
    "title": "Observable Matrix Dynamics of Stocks",
    "url": "https://arxiv.org/abs/2607.19005",
    "source": "Igor Halperin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2607.19005v1 Announce Type: new Abstract: The Observable Matrix Dynamics (OMD) approach monitors the time development of complex non-linear systems through the trajectory of a fixed-size distanc"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.19030",
    "domain": "金融",
    "title": "Pricing options on illiquid assets using liquid market benchmarks: an application to energy markets",
    "url": "https://arxiv.org/abs/2607.19030",
    "source": "Federico Aluigi, Lucia Caramellino, Paolo Pigato, Edoardo Scrima",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2607.19030v1 Announce Type: new Abstract: The Gasoil options market is illiquid, making it difficult to construct its implied volatility surface directly. However, it is closely linked to the hi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.19218",
    "domain": "金融",
    "title": "Denoising Subordinated Probabilistic Models: Diffusion with a Tempered-Stable Volatility Clock, and What the Noise Mechanism Actually Controls",
    "url": "https://arxiv.org/abs/2607.19218",
    "source": "Junchi Shen, Helin Zhao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2607.19218v1 Announce Type: new Abstract: Heavy-tailed diffusion models replace Gaussian noise by a Gaussian variance mixture: denoising Levy probabilistic models (DLPM) take the mixing variable"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.19279",
    "domain": "金融",
    "title": "Gaussian Boson Sampling for Asset Clustering in Statistical Arbitrage Portfolios",
    "url": "https://arxiv.org/abs/2607.19279",
    "source": "Dayne Marcus Lopena, Daniel Buguks, Zhenghao Li, Ewan Mer, Shana H. Winston, Shang Yu, Mihai Cucuringu, Del Rajan, Philip Intallura, Raj B. Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2607.19279v1 Announce Type: cross Abstract: Gaussian Boson Sampling (GBS) provides a native photonic quantum heuristic for sampling dense subgraphs from adjacency matrices, offering a scalable p"
  },
  {
    "id": "rss:https://arxiv.org/abs/2507.09181",
    "domain": "金融",
    "title": "Generalized Orlicz premia",
    "url": "https://arxiv.org/abs/2507.09181",
    "source": "M\\\"ucahit Ayg\\\"un, Fabio Bellini, Roger J. A. Laeven",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2507.09181v2 Announce Type: replace Abstract: We introduce a generalized class of Orlicz premia based on possibly nonconvex loss functions, extending the classical framework of Haezendonck and G"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.03596",
    "domain": "金融",
    "title": "vop_poc_nz: A Python Framework for Distributional Cost-Effectiveness and Value of Perspective Analysis",
    "url": "https://arxiv.org/abs/2512.03596",
    "source": "Dylan A Mordaunt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2512.03596v2 Announce Type: replace Abstract: Health economic evaluations are sensitive to the choice of analytical perspective (e.g., health system vs. societal). We present vop_poc_nz, a Pytho"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.11423",
    "domain": "金融",
    "title": "A Validated Volatility-Volume-Gap Classifier for Regime Identification in MNQ Intraday Data",
    "url": "https://arxiv.org/abs/2605.11423",
    "source": "Mathias Mesfin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2605.11423v2 Announce Type: replace Abstract: This paper asks whether a small set of observable pre-market characteristics can identify trading days with systematically different intraday behavi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.17086",
    "domain": "金融",
    "title": "Global Automation Atlas",
    "url": "https://arxiv.org/abs/2605.17086",
    "source": "Prashant Garg, Tommaso Crosta, Jasmin Baier",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2605.17086v2 Announce Type: replace Abstract: Automation can displace or complement labour, but this need not be constant across economies. Existing exposure measures typically assign fixed scor"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.31387",
    "domain": "金融",
    "title": "Signature-Based Optimal Execution for Statistical Arbitrage with Path-Dependent Trading Signals",
    "url": "https://arxiv.org/abs/2606.31387",
    "source": "Gianmarco Morbelli, Sven Karbach, Mike Derksen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2606.31387v2 Announce Type: replace Abstract: We develop a signature-based framework for optimal execution in statistical arbitrage strategies with path-dependent predictive signals. Both the al"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.01198",
    "domain": "金融",
    "title": "When large trades are not (automatically) news: Liquidity tail risk and price discovery",
    "url": "https://arxiv.org/abs/2607.01198",
    "source": "Umut \\c{C}etin, Mingwei Lin, Giulia Livieri",
    "platform": "rss",
    "points": null,
    "published_at": "2026-07-22T04:00:00+00:00",
    "summary": "arXiv:2607.01198v2 Announce Type: replace Abstract: When is a large trade news, and when is it a liquidity shock? We study this question in a sequential competitive limit order book with asymmetric in"
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
    "id": "hn:48824532",
    "domain": "金融",
    "title": "SpaceX Shares Stumble in Nasdaq-100 Debut",
    "url": "https://www.wsj.com/finance/stocks/spacex-shares-stumble-in-nasdaq-100-debut-9ec10565",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-07-07T22:00:45+00:00",
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
  }
]
```
