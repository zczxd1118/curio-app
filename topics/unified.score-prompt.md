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

- 今日日期：`2026-06-24`
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
  "date": "2026-06-24",
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
    "points": 3375570,
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
    "points": 1282904,
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
    "points": 1241407,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1229595,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 939304,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1ig9jYUERk",
    "domain": "AI",
    "title": "黑马程序员DeepSeek+Cursor+Devbox+Sealos带你零代码搞定实战项目开发部署视频教程，基于AI完成项目的设计、开发、测试、联调、部署全流程",
    "url": "http://www.bilibili.com/video/av114101778908628",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 928219,
    "published_at": "2025-03-04T07:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公综号，回复关键词：deepseek\n【Java学习路线图】展开查看更多内容\nhttps://www.bilibili.com/read/cv9965357\n学习集Q结Q地群：625260577\n\nJava最高效学习路线图（依次向下顺序学习即可）\nJava基础：BV1821CY8E2d\nJavaweb+AI：BV1yGydYEE3H\n苍穹外卖："
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 882235,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 843445,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 762742,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1mzFVzPEB6",
    "domain": "AI",
    "title": "（比刷剧爽！）2026公认最好的《Claude Code》教程，附课件代码—Claude Code探索-测试-重构-调试代码库",
    "url": "http://www.bilibili.com/video/av116005959505146",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 551175,
    "published_at": "2026-02-03T09:29:30+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1.使用 Claude 代码来探索、开发、测试、重构和调试代码库。\n2.使用 MCP 服务器（例如 Playwright 和 Figma MCP 服务器）扩展 Claude Code 的功能。\n3.将 Claude Code 最佳实践应用于三个项目：探索和开发 RAG 聊天机器人的代码库，重构电子商务数据的 Ju"
  },
  {
    "id": "bvid:BV1RSFUzVEAG",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码",
    "url": "http://www.bilibili.com/video/av116045469783373",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 530894,
    "published_at": "2026-02-10T08:59:28+00:00",
    "summary": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 516022,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 444358,
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
    "points": 415086,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1Yi5M6DERk",
    "domain": "AI",
    "title": "【Claude Code】这绝对是b站讲的最好的Claude Code教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！AI大模型",
    "url": "http://www.bilibili.com/video/av116560144369496",
    "source": "双非本想做大模型",
    "platform": "bilibili",
    "points": 414508,
    "published_at": "2026-05-12T06:24:19+00:00",
    "summary": "如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！\n【视频配套籽料+问题解答请看”平论区置顶”自取哦】"
  },
  {
    "id": "bvid:BV1nkXkYfEfF",
    "domain": "AI",
    "title": "零基础也能用AI编程!豆包电脑版让你3分钟做出实用工具",
    "url": "http://www.bilibili.com/video/av114200730933577",
    "source": "花叔v",
    "platform": "bilibili",
    "points": 383523,
    "published_at": "2025-03-22T04:02:08+00:00",
    "summary": "很多人都想学编程,但被高门槛劝退。本期给大家介绍一款零门槛的AI编程工具-豆包电脑版。通过3个实战案例,带你体验如何用AI轻松实现编程。\n\n豆包电脑版特点:\n- 中文界面,所见即所得\n- 支持html代码预览\n- 支持Python运行\n- 可生成完整项目代码\n- 历史版本管理\n- 代码一键导出\n\n时间戳\n00:00 为什么要学AI编程\n03:19 案例1:图片压缩网站实战\n04:15 案例2:数据"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 375597,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV16zDfBtECQ",
    "domain": "AI",
    "title": "为什么越来越多的人抛弃 MCP，转向 CLI？",
    "url": "http://www.bilibili.com/video/av116377675373297",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 250904,
    "published_at": "2026-04-10T01:10:33+00:00",
    "summary": "为什么越来越多的人抛弃 MCP，转向 CLI？#modelcontextprotocol #cli #agent #ai #llm #token #openclaw"
  },
  {
    "id": "bvid:BV1AHDuBoE2S",
    "domain": "AI",
    "title": "锐评vibe coding工具“从夯到拉”",
    "url": "http://www.bilibili.com/video/av116347090502349",
    "source": "布鲁歇一歇",
    "platform": "bilibili",
    "points": 246736,
    "published_at": "2026-04-04T15:19:25+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1KJySBfEjW",
    "domain": "AI",
    "title": "我抛弃了 Cursor，用 Claude Code 写了 99% 的代码 （Claude Code 深度体验）",
    "url": "http://www.bilibili.com/video/av115456522388028",
    "source": "数字黑魔法",
    "platform": "bilibili",
    "points": 242071,
    "published_at": "2025-10-29T08:37:03+00:00",
    "summary": "本视频不构成任何投资建议。DYOR。"
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 242016,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 223100,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1kxLD6HEYN",
    "domain": "AI",
    "title": "Claude Code怎么全自动跑13小时？实测GLM 5.2开源天花板",
    "url": "http://www.bilibili.com/video/av116763920438810",
    "source": "小白debug",
    "platform": "bilibili",
    "points": 205920,
    "published_at": "2026-06-17T10:14:02+00:00",
    "summary": "我手搓了一个Openclaw"
  },
  {
    "id": "bvid:BV1VCVS6PEAd",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent零基础全套教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116668525186915",
    "source": "大模型入门教程",
    "platform": "bilibili",
    "points": 193981,
    "published_at": "2026-05-31T09:46:57+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1X8oKBLEdj",
    "domain": "AI",
    "title": "一口气学会AI编程！3个月10万字超详细教学！【项目实操】【0基础教学】【自学教程】【AI编程】【vibecoding】",
    "url": "http://www.bilibili.com/video/av116436177523067",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 175312,
    "published_at": "2026-04-21T03:15:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料，领取方式：关注后 私信“ 1 ”就好！\n\n后面还会出【一口气学会AI漫剧 】【一口气学会AI Agent 】等系列！大家可以蹲蹲！"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 175298,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1RAEz6EE98",
    "domain": "AI",
    "title": "为什么Claude Code+DeepSeekV4是最有性价比的个人AI Agent?",
    "url": "http://www.bilibili.com/video/av116732144392386",
    "source": "呱声一片",
    "platform": "bilibili",
    "points": 158861,
    "published_at": "2026-06-11T15:27:06+00:00",
    "summary": "官方文档地址：https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/claude_code"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 157690,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 156618,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 147556,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 144545,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1g49KBqE1g",
    "domain": "AI",
    "title": "【Java+大模型】Java AI Agent✚Spring AI✚Spring AI Alibaba Agent Framework整体结构✚Skill！",
    "url": "http://www.bilibili.com/video/av116339758860081",
    "source": "图灵官方",
    "platform": "bilibili",
    "points": 95691,
    "published_at": "2026-04-03T08:15:24+00:00",
    "summary": "整理制作不易，大家记得点个关注，一键三连呀【点赞、收藏、转发】感谢支持~\n配套大模型笔记/AI大模型学习大纲/面试真题自取：https://www.bilibili.com/read/cv39638062/?spm_id_from=333.1387.0.0&amp;jump_opus=1"
  },
  {
    "id": "bvid:BV1WJjF67Eky",
    "domain": "AI",
    "title": "对Claude code上瘾了",
    "url": "http://www.bilibili.com/video/av116768819384530",
    "source": "小王很南",
    "platform": "bilibili",
    "points": 79352,
    "published_at": "2026-06-18T02:50:04+00:00",
    "summary": "我做的交互网站"
  },
  {
    "id": "bvid:BV17Ejt6QE9Y",
    "domain": "AI",
    "title": "一旦被Claude判定&quot;危险&quot;，你之后说的每句话都会被动手脚——实测曝光",
    "url": "http://www.bilibili.com/video/av116787609863495",
    "source": "YJFGL",
    "platform": "bilibili",
    "points": 75660,
    "published_at": "2026-06-21T10:26:28+00:00",
    "summary": "续上一条视频。这次我测出了更具体的触发机制：\n当对话中**某一条消息被系统分类器判定为&quot;潜在存在危害&quot;**之后，从那条消息开始，之后所有的 user 消息后面都会被持续注入一段隐藏文本。\n也就是说，这不是无差别的全程注入，而是一旦被系统标记，就会进入一种&quot;持续追加提醒&quot;的状态，并且这个状态会一直保持到对话结束，用户完全不知情、也无法解除。\n这意味着：\n你某一"
  },
  {
    "id": "bvid:BV1MJXZBgE32",
    "domain": "AI",
    "title": "AI Coding 进阶：从 Vibe/Plan/Spec 到 Harness Engineering 与 Agent Teams",
    "url": "http://www.bilibili.com/video/av116334289491216",
    "source": "Qoder",
    "platform": "bilibili",
    "points": 63314,
    "published_at": "2026-04-02T09:00:33+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV17Sjy6vEoA",
    "domain": "AI",
    "title": "Claude Code平替Kimi Code教程：视频理解，数据插件，Goal，Swarm，ACP等进阶玩法",
    "url": "http://www.bilibili.com/video/av116798313727318",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 62215,
    "published_at": "2026-06-23T10:30:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1ZjDYB7Eam",
    "domain": "AI",
    "title": "从 0 到 1：6小时掌握 Vibe Coding！ Claude Code ＋ AI 这支影片直接让你超越 90% AI 玩家",
    "url": "http://www.bilibili.com/video/av116362122894759",
    "source": "李哈利Harry",
    "platform": "bilibili",
    "points": 60232,
    "published_at": "2026-04-08T11:00:00+00:00",
    "summary": "🌟 加入AI大师社群并运用AI创业赚钱：https://www.skool.com/aiagent/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n📌 加入我的免费 Skool 社群，获取模板：https://www.skool.com/aiagent8/about?ref=f2b566934c5c4639aaa47ab1fe39310e\n\n🚧 开始使用 n8"
  },
  {
    "id": "bvid:BV12NK1zMESx",
    "domain": "AI",
    "title": "如何用Cursor开发大项目，全流程讲解，干货十足",
    "url": "http://www.bilibili.com/video/av114758657246726",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 58394,
    "published_at": "2025-06-28T02:37:22+00:00",
    "summary": "视频主题&amp;项目背景\n主题： 分享个人如何使用cursor 从0到1开发一个比较大的项目，使用的技术栈是vue+小程序+java\n项目\n一个B2B的订货商城及供应链全流程管理，包含的端有：\n小程序商城端\n供应商端\n仓储物流端\n司机配送端\n销售端\n后台管理系统\n以上小程序端都是使用webview的方式\n核心功能：\n商城的基本功能: 正逆向订单、商品、购物车、优惠券、积分、钱包、充值、工单等\n供"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 52338,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1rv7A6oEeP",
    "domain": "AI",
    "title": "2026版LangChain教程，langchain快速入门， Agent智能体rag项目实战",
    "url": "http://www.bilibili.com/video/av116792827579053",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 47978,
    "published_at": "2026-06-23T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】LangChain学习一套通，从入门到三大综合项目实战"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 41051,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1QuWbzGEEQ",
    "domain": "AI",
    "title": "巨日禄AI教程--新手到精通",
    "url": "http://www.bilibili.com/video/av115395738476069",
    "source": "骆创AI",
    "platform": "bilibili",
    "points": 40961,
    "published_at": "2025-10-18T14:54:50+00:00",
    "summary": "我深入浅出的讲解了整个工具制作，和制作思维。这个视频足够解决目前，市面上大多数不会用巨日禄的团队的问题。 会用不会用都能从这个教程中有所收货。任何问题也都可以问我。我忙的过来都会回答。"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 39724,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1hxMbzqEzU",
    "domain": "AI",
    "title": "小智MCP自由了！我开源了个命令行神器实现多MCP聚合",
    "url": "http://www.bilibili.com/video/av114686414625640",
    "source": "闪电蘑菇",
    "platform": "bilibili",
    "points": 39476,
    "published_at": "2025-06-15T08:31:55+00:00",
    "summary": "- 我写的小智客户端命令行工具\n - github: https://github.com/shenjingnan/xiaozhi-client\n - gitee: https://gitee.com/shenjingnan/xiaozhi-client\n\n- 小智官方MCP示例代码仓库：\n - github: https://github.com/78/mcp-calculator\n - git"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 36777,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1x6Vt6dEef",
    "domain": "AI",
    "title": "100 小时测试 Claude Code vs Codex（真实结果）",
    "url": "http://www.bilibili.com/video/av116656495925868",
    "source": "设计之道",
    "platform": "bilibili",
    "points": 31273,
    "published_at": "2026-05-29T06:44:49+00:00",
    "summary": "【海外 AI 订阅】\n国内直连，支付宝付款，不用代理，\n一站订阅 ChatGPT / Codex / Claude Code / X\n订阅链接：https://bewild.ai?code=SJZD\n订阅时请填优惠邀请码：SJZD，具体优惠金额以官网为准。\n\n【视频介绍】\n我花了 100 个小时测试 Claude Code 和 Codex，结果真的让我非常意外。\n相同的提示词、相同的项目构建、两个"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 29768,
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
    "points": 29362,
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
    "points": 28671,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1mfJw6uE1Y",
    "domain": "AI",
    "title": "AI Agent 别乱选！2026 AI Agent 深度横评，普通人看完不踩坑｜OpenClaw、Codex、Hermes、WorkBuddy、Claude",
    "url": "http://www.bilibili.com/video/av116747361322195",
    "source": "AI实战派Pro",
    "platform": "bilibili",
    "points": 28362,
    "published_at": "2026-06-14T07:53:12+00:00",
    "summary": "《2026 主流 AI Agent 全维度对比｜OpenClaw / Codex / Claude Cowork / WorkBuddy / Hermes 怎么选？》\n\nHi，我是Alpha，我手把手带大家用AI提升自己工作、生活效率，提升个人竞争力以及用AI赚钱！一起做AI时代的主导者，而不是在焦虑中被AI淘汰！\n关注AI 实战派，让AI替你忙起来！\n\n本期视频介绍：《AI Agent 别乱选！"
  },
  {
    "id": "rss:https://www.eetimes.com/snug-india-2026-synopsys-unveils-first-multiphysics-fusion-tools-since-ansys-deal/",
    "domain": "AI 算力 / 半导体",
    "title": "SNUG India 2026: Synopsys Unveils First Multiphysics Fusion Tools Since Ansys Deal",
    "url": "https://www.eetimes.com/snug-india-2026-synopsys-unveils-first-multiphysics-fusion-tools-since-ansys-deal/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T17:00:00+00:00",
    "summary": "Synopsys debuts Multiphysics Fusion tools post-Ansys, unifying EDA and physics for advanced node and 3DIC designs. The post SNUG India 2026: Synopsys Unveils First Multiphysics Fusion Tools Since Ansy"
  },
  {
    "id": "rss:https://www.eetimes.com/how-spain-built-a-quantum-ecosystem-without-calling-it-one/",
    "domain": "AI 算力 / 半导体",
    "title": "How Spain Built a Quantum Ecosystem Without Calling It One",
    "url": "https://www.eetimes.com/how-spain-built-a-quantum-ecosystem-without-calling-it-one/",
    "source": "Marta P. Estarellas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T12:15:30+00:00",
    "summary": "Spain is turning Europe’s theoretical talk of digital sovereignty into practical reality. The post How Spain Built a Quantum Ecosystem Without Calling It One appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/cea-leti-ceo-ais-real-bottleneck-is-architecture/",
    "domain": "AI 算力 / 半导体",
    "title": "CEA-Leti CEO: AI’s Real Bottleneck Is Architecture",
    "url": "https://www.eetimes.com/cea-leti-ceo-ais-real-bottleneck-is-architecture/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T07:00:00+00:00",
    "summary": "AI's growth is hitting an architectural wall, not just compute—discover why integration trumps raw power in this exclusive interview. The post CEA-Leti CEO: AI’s Real Bottleneck Is Architecture appear"
  },
  {
    "id": "rss:https://www.eetimes.com/critical-components-for-reliable-factory-automation-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Critical Components for Reliable Factory Automation Design",
    "url": "https://www.eetimes.com/critical-components-for-reliable-factory-automation-design/",
    "source": "Same Sky and Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T17:15:13+00:00",
    "summary": "This webinar will provide a practical overview of product selection and implementation within factory automation applications. The post Critical Components for Reliable Factory Automation Design appea"
  },
  {
    "id": "rss:https://www.eetimes.com/globalfoundries-qualinx-put-europes-chip-sovereignty-to-the-fab-test/",
    "domain": "AI 算力 / 半导体",
    "title": "GlobalFoundries, Qualinx Put Europe’s Chip Sovereignty to the Fab Test",
    "url": "https://www.eetimes.com/globalfoundries-qualinx-put-europes-chip-sovereignty-to-the-fab-test/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T17:00:00+00:00",
    "summary": "GlobalFoundries and Qualinx deliver Europe's first fully secure chip supply chain. The post GlobalFoundries, Qualinx Put Europe’s Chip Sovereignty to the Fab Test appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/software-to-silicon-with-risc-v-for-physical-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Software to Silicon With RISC-V for Physical AI",
    "url": "https://www.eetimes.com/software-to-silicon-with-risc-v-for-physical-ai/",
    "source": "EE Times Staff",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T14:13:07+00:00",
    "summary": "Discover how RISC-V is reshaping AI chip design—watch to see why it's becoming the default ISA. The post Software to Silicon With RISC-V for Physical AI appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/beyond-isolation-novosenses-isolation-platform-elevates-system-safety-for-advanced-power-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "Beyond Isolation: NOVOSENSE’s Isolation+ Platform Elevates System Safety for Advanced Power Systems",
    "url": "https://www.eetimes.com/beyond-isolation-novosenses-isolation-platform-elevates-system-safety-for-advanced-power-systems/",
    "source": "Christopher McGrady",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T10:00:00+00:00",
    "summary": "Isolation+ is the strategic framework that unifies NOVOSENSE’s entire isolation portfolio. The post Beyond Isolation: NOVOSENSE&#8217;s Isolation+ Platform Elevates System Safety for Advanced Power Sy"
  },
  {
    "id": "rss:https://www.eetimes.com/securing-next-generation-defense-by-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Securing Next-Generation Defense by Design",
    "url": "https://www.eetimes.com/securing-next-generation-defense-by-design/",
    "source": "Daryl Flack",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T07:00:00+00:00",
    "summary": "In an environment of cloud platforms and AI models, security must be embedded into defense systems from the outset. The post Securing Next-Generation Defense by Design appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/amazon-prime-day-2026-deals",
    "domain": "AI 算力 / 半导体",
    "title": "Best Amazon Prime Day tech deals live on day two — PC hardware deals on GPUs, CPUs, SSDs, and more",
    "url": "https://www.tomshardware.com/live/news/amazon-prime-day-2026-deals",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T06:51:55+00:00",
    "summary": "Find the very best PC hardware deals during Amazon Prime Day."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-brilliant-usd11-power-button-gadget-lets-you-switch-your-pc-on-from-your-desk-with-ease-perfect-desk-upgrade-means-you-dont-need-to-bend-down-to-turn-your-rig-on-or-off-anymore-ships-with-super-durable-mechanical-keys-and-rgb-lighting",
    "domain": "AI 算力 / 半导体",
    "title": "This brilliant $11 power button gadget lets you switch your PC on from your desk with ease — perfect desk upgrade means you don't need to bend down to turn your rig on or off anymore, ships with super",
    "url": "https://www.tomshardware.com/pc-components/this-brilliant-usd11-power-button-gadget-lets-you-switch-your-pc-on-from-your-desk-with-ease-perfect-desk-upgrade-means-you-dont-need-to-bend-down-to-turn-your-rig-on-or-off-anymore-ships-with-super-durable-mechanical-keys-and-rgb-lighting",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T06:51:25+00:00",
    "summary": "Who doesn't want a statement power button on their desk for $11? Don't miss out on this ultimate desk gadget."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-almost-usd1-500-instantly-on-an-rtx-5080-gaming-pc-legion-tower-7i-gen-10-packs-core-ultra-7-265k-and-32gb-ddr5",
    "domain": "AI 算力 / 半导体",
    "title": "Save almost $1,500 instantly on an RTX 5080 gaming PC — Legion Tower 7i Gen 10 packs Core Ultra 7 265K and 32GB DDR5",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-almost-usd1-500-instantly-on-an-rtx-5080-gaming-pc-legion-tower-7i-gen-10-packs-core-ultra-7-265k-and-32gb-ddr5",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T21:26:57+00:00",
    "summary": "Lenovo temporarily puts the Legion Tower 7i Gen 10 on sale for $2,899.99, 33% off its regular price tag."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-chairs/best-gaming-chair-deals-prime-day",
    "domain": "AI 算力 / 半导体",
    "title": "Best Amazon Prime Day Gaming Chairs Deals 2026 — deals on Secretlab, Libernovo, Razer, and more",
    "url": "https://www.tomshardware.com/peripherals/gaming-chairs/best-gaming-chair-deals-prime-day",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T20:58:06+00:00",
    "summary": "The best deals on gaming chairs for every budget, style, and comfort level during Amazon Prime Day 2026. Upgrade your gaming chair with something high-quality and on sale, now!"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/acers-4tb-gm7-pcie-4-0-ssd-drops-to-usd470-for-prime-day-2tb-and-4tb-models-are-both-on-sale-for-up-to-23-percent-off",
    "domain": "AI 算力 / 半导体",
    "title": "Acer's 4TB GM7 PCIe 4.0 SSD drops to $470 for Prime Day — 2TB and 4TB models are both on sale for up to 23% off",
    "url": "https://www.tomshardware.com/pc-components/acers-4tb-gm7-pcie-4-0-ssd-drops-to-usd470-for-prime-day-2tb-and-4tb-models-are-both-on-sale-for-up-to-23-percent-off",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T20:26:05+00:00",
    "summary": "The Acer Predator GM7 4TB is on sale for $469.99, bringing it down to its lowest prices since February."
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/soldering-irons/the-best-prime-day-soldering-iron-deals-for-hobbyists-and-makers-right-now-take-advantage-of-these-limited-time-sale-discounts-on-digital-irons-premium-solder-heat-proof-accessories-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "The best Prime Day soldering iron deals for hobbyists and makers right now — take advantage of these limited-time sale discounts on digital irons, premium solder, heat-proof accessories, and more",
    "url": "https://www.tomshardware.com/maker-stem/soldering-irons/the-best-prime-day-soldering-iron-deals-for-hobbyists-and-makers-right-now-take-advantage-of-these-limited-time-sale-discounts-on-digital-irons-premium-solder-heat-proof-accessories-and-more",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T18:31:43+00:00",
    "summary": "Grab a new soldiering iron or accessories during this Amazon Prime Day sales week, with the best recommendations included here."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/best-gaming-laptop-deals-discount",
    "domain": "AI 算力 / 半导体",
    "title": "Best Amazon Prime Day gaming laptop PC deals 2026 — epic discounts on Dell, Alienware, MSI, ROG, and others",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/best-gaming-laptop-deals-discount",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T17:19:10+00:00",
    "summary": "Here are the best gaming laptop deals during Amazon Prime Day 2026. We're constantly updating this list with the best deals still available across all of the major retailers."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/these-are-the-best-cpu-cooler-deals-we-found-this-prime-day-up-to-33-percent-off-deals-from-cooler-master-arctic-tryx-corsair-and-pccooler-for-every-budget",
    "domain": "AI 算力 / 半导体",
    "title": "These are the best CPU cooler deals we found this Prime Day, up to 33% off — deals from Cooler Master, Arctic, Tryx, Corsair, and PCCooler for every budget",
    "url": "https://www.tomshardware.com/pc-components/these-are-the-best-cpu-cooler-deals-we-found-this-prime-day-up-to-33-percent-off-deals-from-cooler-master-arctic-tryx-corsair-and-pccooler-for-every-budget",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T16:56:12+00:00",
    "summary": "As Amazon's Prime Day gets started, now's your chance to snag some awesome deals on CPU coolers. We have singled out options from across the board, highlighting the best offers at each price point. Ar"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/the-best-switch-2-accessories-prime-day-2026-controllers-cameras-cases-screen-protectors-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "The best Switch 2 accessories Prime Day 2026 — controllers, cameras, cases, screen protectors, and more",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/the-best-switch-2-accessories-prime-day-2026-controllers-cameras-cases-screen-protectors-and-more",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T16:20:42+00:00",
    "summary": "Upgrade your Nintendo Switch 2 with these essential accessories."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/grab-this-creality-3d-printer-tool-kit-for-all-time-low-usd25-49-for-prime-day-74-piece-set-includes-everything-that-you-need-for-3d-printer-maintenance-and-comes-in-a-neat-organizer-for-storage-and-transport",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this Creality 3D Printer tool kit for all-time low $25.49 for Prime Day — 74-piece set includes everything that you need for 3D printer maintenance and comes in a neat organizer for storage and t",
    "url": "https://www.tomshardware.com/pc-components/grab-this-creality-3d-printer-tool-kit-for-all-time-low-usd25-49-for-prime-day-74-piece-set-includes-everything-that-you-need-for-3d-printer-maintenance-and-comes-in-a-neat-organizer-for-storage-and-transport",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T16:04:29+00:00",
    "summary": "The Creality 3D Printer Tool Kit is on sale at 15% of for Prime Day 2026. This brings the price down to $25.49, helping you save some cash if you want to complete your 3D printing setup."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-an-amazing-usd900-off-a-4tb-samsung-9100-pro-ssd-in-blockbuster-prime-day-deal-remarkable-sale-brings-pcie-5-0-nvme-drive-from-usd1-360-down-to-just-usd459",
    "domain": "AI 算力 / 半导体",
    "title": "Get a 4TB Samsung 9100 Pro SSD for just $459 in blockbuster Prime Day sale — remarkable deal shaves $900 off PCIe 5.0 NVMe drive to bring it below MSRP [Updated]",
    "url": "https://www.tomshardware.com/pc-components/save-an-amazing-usd900-off-a-4tb-samsung-9100-pro-ssd-in-blockbuster-prime-day-deal-remarkable-sale-brings-pcie-5-0-nvme-drive-from-usd1-360-down-to-just-usd459",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T15:59:56+00:00",
    "summary": "Samsung's 4TB 9100 Pro PCIe 5.0 NVMe SSD is on sale for a remarkable price, bringing its $1,360 MSRP down to just $460."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd250-on-the-cheapest-rtx-5080-around-this-prime-day-gigabyte-gaming-oc-geforce-rtx-5080-at-stellar-pricing-on-newegg",
    "domain": "AI 算力 / 半导体",
    "title": "Save $250 on the cheapest RTX 5080 around this Prime Day — Gigabyte Gaming OC GeForce RTX 5080 at stellar pricing on Newegg",
    "url": "https://www.tomshardware.com/pc-components/save-usd250-on-the-cheapest-rtx-5080-around-this-prime-day-gigabyte-gaming-oc-geforce-rtx-5080-at-stellar-pricing-on-newegg",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T15:54:30+00:00",
    "summary": "The Gigabyte Gaming OC GeForce RTX 5080 pairs factory overclocking, triple-fan cooling, and support for DLSS 4.5 with a $250 discount, bringing one of Nvidia's fastest gaming GPUs closer to its intend"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/scuf-prime-day-sale-brings-pro-control-and-precision-savings-of-up-to-26-percent-for-gamers",
    "domain": "AI 算力 / 半导体",
    "title": "SCUF Prime Day sale brings pro control and precision savings of up to 26% for gamers",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/scuf-prime-day-sale-brings-pro-control-and-precision-savings-of-up-to-26-percent-for-gamers",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T15:43:24+00:00",
    "summary": "SCUF has slashed the prices of the Envision and Valor Pro controllers by up to 26% for this Prime Day."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/the-swiss-army-knife-of-usb-dvd-drives-is-on-sale-also-features-a-built-in-m-2-ssd-slot-usb-hub-and-sata-hard-drive-dock-usd26-for-dvd-writer-and-hub-usd39-gets-an-added-sata-or-m-2-ssd-dock",
    "domain": "AI 算力 / 半导体",
    "title": "The Swiss army knife of USB DVD drives is on sale, also features a built-in M.2 SSD slot, USB hub, and SATA hard drive dock — $26 for DVD writer and hub, $39 gets an added SATA or M.2 SSD dock",
    "url": "https://www.tomshardware.com/pc-components/storage/the-swiss-army-knife-of-usb-dvd-drives-is-on-sale-also-features-a-built-in-m-2-ssd-slot-usb-hub-and-sata-hard-drive-dock-usd26-for-dvd-writer-and-hub-usd39-gets-an-added-sata-or-m-2-ssd-dock",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T15:22:47+00:00",
    "summary": "Portable DVD writers with flash media reading and SATA drive docking abilities are on sale at Amazon Prime Day 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/best-gaming-pc-deals-prebuilts",
    "domain": "AI 算力 / 半导体",
    "title": "Best Prime Day Gaming PC Deals 2026 — deals from Amazon, Best Buy, Newegg, Dell, Lenovo, and others",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/best-gaming-pc-deals-prebuilts",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T14:56:42+00:00",
    "summary": "We've gathered the top pre-built gaming desktop deals during Amazon Prime Day 2026. We're constantly updating this list with the best deals across all retailers."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/best-ssd-deals-discounts",
    "domain": "AI 算力 / 半导体",
    "title": "Best Prime Day SSD deals 2026 — savings on Samsung, WD, Crucial, and other SSDs at Amazon, Newegg, and others",
    "url": "https://www.tomshardware.com/pc-components/ssds/best-ssd-deals-discounts",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T14:45:56+00:00",
    "summary": "We've rounded up the best SSD deals to help you expand your PC's storage without breaking the bank during Amazon Prime Day 2026. We're constantly updating this list with the best deals across all reta"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/geekom-launches-mini-pc-prime-day-offers-with-up-to-34-percent-off-also-an-exclusive-8-percent-discount-code-oodles-of-sleek-mini-pc-choices-packing-amd-ryzen-and-intel-core-ultra-chips",
    "domain": "AI 算力 / 半导体",
    "title": "Geekom launches Mini PC Prime Day offers with up to 34% off, also an exclusive 8% discount code — oodles of sleek mini PC choices packing AMD Ryzen and Intel Core Ultra chips",
    "url": "https://www.tomshardware.com/pc-components/geekom-launches-mini-pc-prime-day-offers-with-up-to-34-percent-off-also-an-exclusive-8-percent-discount-code-oodles-of-sleek-mini-pc-choices-packing-amd-ryzen-and-intel-core-ultra-chips",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T14:37:29+00:00",
    "summary": "Mini PC specialist Geekom has stuffed its Amazon webstore with a multitude of diminutive computers with discounts as deep as 34% off."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/best-ram-memory-deals",
    "domain": "AI 算力 / 半导体",
    "title": "Best Amazon Prime Day RAM deals 2026 — discounts on DDR5 and DDR4 to beat the memory price crunch",
    "url": "https://www.tomshardware.com/pc-components/ram/best-ram-memory-deals",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T14:35:47+00:00",
    "summary": "We're rounding up the best RAM deals from retailers across the U.S during Amazon Prime Day 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/nvidia-announces-liquid-cooling-system-that-runs-hotter-than-a-hot-tub-promises-to-reduce-electricity-consumption-and-cut-water-use-by-up-to-100-percent-but-sustainability-challenges-remain",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia announces liquid cooling system that runs ‘hotter than a hot tub’ — promises to reduce electricity consumption and cut water use by up to 100%, but sustainability challenges remain",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/nvidia-announces-liquid-cooling-system-that-runs-hotter-than-a-hot-tub-promises-to-reduce-electricity-consumption-and-cut-water-use-by-up-to-100-percent-but-sustainability-challenges-remain",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T13:36:21+00:00",
    "summary": "This system raises the base coolant temperature to 113 degrees F (45 degrees C) to save on electricity costs and reduce water consumption to basically zero."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd447-on-this-3-item-combo-from-newegg-just-usd1-082-buys-a-speedy-huge-4tb-samsung-9100-pro-ssd-32gb-ddr5-ram-and-an-asus-tuf-gaming-x870e-plus-motherboard-during-prime-day-sales",
    "domain": "AI 算力 / 半导体",
    "title": "Save $447 on this 3-item combo from Newegg - just $1,082 buys a speedy, huge 4TB Samsung 9100 Pro SSD, 32GB DDR5 RAM, and an Asus TUF Gaming X870E-Plus motherboard during Prime Day sales",
    "url": "https://www.tomshardware.com/pc-components/save-usd447-on-this-3-item-combo-from-newegg-just-usd1-082-buys-a-speedy-huge-4tb-samsung-9100-pro-ssd-32gb-ddr5-ram-and-an-asus-tuf-gaming-x870e-plus-motherboard-during-prime-day-sales",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T13:23:49+00:00",
    "summary": "Spend $1,082 for over $1,530 worth of hardware in this Newegg combo - $447 discount brings pricing back down to earth, if only for Prime Day"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/grab-these-vital-3d-printer-maintenance-tools-at-a-discount-with-these-prime-day-2026-deals-up-to-30-percent-off-hoto-creality-wera-and-ifixit-kits",
    "domain": "AI 算力 / 半导体",
    "title": "Grab these vital 3D printer maintenance tools at a discount with these Prime Day 2026 deals — up to 30% off HOTO, Creality, Wera, and iFixit kits",
    "url": "https://www.tomshardware.com/3d-printing/grab-these-vital-3d-printer-maintenance-tools-at-a-discount-with-these-prime-day-2026-deals-up-to-30-percent-off-hoto-creality-wera-and-ifixit-kits",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T13:14:20+00:00",
    "summary": "3D printers need maintenance and with these great tools you’ll be producing great prints all day long."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/msi-claw-8-ex-ai-plus-review",
    "domain": "AI 算力 / 半导体",
    "title": "MSI Claw 8 EX AI+ review: Unmatched performance and a jaw-dropping price tag",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/msi-claw-8-ex-ai-plus-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T13:00:00+00:00",
    "summary": "It has the performance muscle that is unmatched in this class, but the Claw 8 EX AI+’s $1,799 price tag and lack of OLED leave us scratching our heads."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/supercomputers/chinas-lineshine-supercomputer-dethrones-us-el-capitan-secures-first-place-in-top-500-list-first-machine-in-the-rankings-to-sustain-more-than-2-exaflops-of-double-precision-performance-using-only-cpus",
    "domain": "AI 算力 / 半导体",
    "title": "China's LineShine supercomputer dethrones US' El Capitan, secures first place in Top 500 list — first machine in the rankings to sustain more than 2 ExaFLOPS of double-precision performance using only",
    "url": "https://www.tomshardware.com/tech-industry/supercomputers/chinas-lineshine-supercomputer-dethrones-us-el-capitan-secures-first-place-in-top-500-list-first-machine-in-the-rankings-to-sustain-more-than-2-exaflops-of-double-precision-performance-using-only-cpus",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T12:55:33+00:00",
    "summary": "China's LineShine supercomputer is now officially the world's fastest FP64 machine, but its mixed-precision results are behind those of El Capitan, Frontier, and Aurora."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/these-15-under-usd50-gadgets-have-upgraded-my-tech-life-and-theyre-all-on-sale-for-prime-day",
    "domain": "AI 算力 / 半导体",
    "title": "These 15 under-$50 gadgets have upgraded my tech life, and they're all on sale for Prime Day",
    "url": "https://www.tomshardware.com/peripherals/these-15-under-usd50-gadgets-have-upgraded-my-tech-life-and-theyre-all-on-sale-for-prime-day",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T12:41:14+00:00",
    "summary": "From electric screwdrivers to high-res webcams, these are inexpensive game-changers."
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/prime-day-gaming-monitors-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Prime Day gaming monitor deals live 2026 — hot sales on monitors from Amazon, Newegg, Dell, Best Buy, and more",
    "url": "https://www.tomshardware.com/live/news/prime-day-gaming-monitors-2026",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T12:21:42+00:00",
    "summary": "The best Amazon Prime Day 2026 monitor sales, live round-the-clock coverage of all the best deals."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/california-drivers-accuse-gas-station-operators-of-using-ai-to-boost-pump-prices-lawsuit-seeks-damages-for-antitrust-violations",
    "domain": "AI 算力 / 半导体",
    "title": "California drivers accuse gas station operators of using AI to boost pump prices — lawsuit seeks damages for antitrust violations",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/california-drivers-accuse-gas-station-operators-of-using-ai-to-boost-pump-prices-lawsuit-seeks-damages-for-antitrust-violations",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T12:17:37+00:00",
    "summary": "Californians pay the highest gas prices in the U.S. and a proposed class action says that the issue has been exacerbated by an AI-tool that smartly squeezes customers for the best profits."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/oracle-lays-off-21-000-employees-in-just-12-months-due-to-ai-adoption-and-costly-ai-infrastructure-ambitions-says-layoffs-will-continue-as-internal-ai-deployment-grows",
    "domain": "AI 算力 / 半导体",
    "title": "Oracle lays off 21,000 employees in just 12 months due to AI adoption and costly AI infrastructure ambitions — says layoffs will continue as internal AI deployment grows",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/oracle-lays-off-21-000-employees-in-just-12-months-due-to-ai-adoption-and-costly-ai-infrastructure-ambitions-says-layoffs-will-continue-as-internal-ai-deployment-grows",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T12:05:15+00:00",
    "summary": "Oracle cut 21,000 jobs in fiscal year 2026 as AI automation and AI cloud expansions reshape its workforce and spending strategy."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/upgrade-to-wi-fi-7-with-these-prime-day-savings-tp-link-wi-fi-7-routers-get-big-prime-day-discounts",
    "domain": "AI 算力 / 半导体",
    "title": "Upgrade to Wi-Fi 7 with these Prime Day savings — TP-Link Wi-Fi 7 routers get big Prime Day discounts",
    "url": "https://www.tomshardware.com/networking/routers/upgrade-to-wi-fi-7-with-these-prime-day-savings-tp-link-wi-fi-7-routers-get-big-prime-day-discounts",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T11:00:00+00:00",
    "summary": "Amazon has some fantastic deals on TP-Link wireless routers"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/valve-working-on-steamos-for-general-release-company-collaborating-with-nvidia-to-ensure-compatibility-hints-at-dual-boot-capabilities-in-the-future",
    "domain": "AI 算力 / 半导体",
    "title": "Valve working on SteamOS for general release — company collaborating with Nvidia to ensure compatibility, hints at dual-boot capabilities in the future",
    "url": "https://www.tomshardware.com/video-games/console-gaming/valve-working-on-steamos-for-general-release-company-collaborating-with-nvidia-to-ensure-compatibility-hints-at-dual-boot-capabilities-in-the-future",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T10:53:10+00:00",
    "summary": "Valve engineer Pierre-Loup Griffais says that the company is working on expanding SteamOS compatibility with Nvidia and other hardware platforms. This should make it easier for users to install the ga"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/get-up-to-usd900-off-a-new-dell-pc-instant-savings-on-everyday-systems-to-powerful-gaming-rigs",
    "domain": "AI 算力 / 半导体",
    "title": "Get up to $900 off a new Dell PC — instant savings on everyday systems to powerful gaming rigs",
    "url": "https://www.tomshardware.com/pc-components/get-up-to-usd900-off-a-new-dell-pc-instant-savings-on-everyday-systems-to-powerful-gaming-rigs",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T10:47:04+00:00",
    "summary": "Dell is running a big sale on the brand’s prebuilt systems with savings up to $900."
  },
  {
    "id": "rss:https://www.eetimes.com/defense-sends-clear-signal-to-canadian-semiconductor-industry/",
    "domain": "AI 算力 / 半导体",
    "title": "Defense Sends Clear Signal to Canadian Semiconductor Industry",
    "url": "https://www.eetimes.com/defense-sends-clear-signal-to-canadian-semiconductor-industry/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T22:00:00+00:00",
    "summary": "Canada sharpens its defense and tech edge with policies to boost homegrown chip power. The post Defense Sends Clear Signal to Canadian Semiconductor Industry appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/amazon-newest-gambit-selling-ai-chips/",
    "domain": "AI 算力 / 半导体",
    "title": "Amazon’s Newest Gambit: Selling AI Chips",
    "url": "https://www.eetimes.com/amazon-newest-gambit-selling-ai-chips/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-19T12:19:36+00:00",
    "summary": "The world’s largest hyperscaler wants to seize the semiconductor moment by selling AI accelerators at scale. The post Amazon’s Newest Gambit: Selling AI Chips appeared first on EE Times."
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
    "id": "rss:https://www.theverge.com/gadgets/951081/robot-vacuum-mop-deals-amazon-prime-day-2026",
    "domain": "大厂 AI 动态",
    "title": "The best robot vacuum deals available during Prime Day",
    "url": "https://www.theverge.com/gadgets/951081/robot-vacuum-mop-deals-amazon-prime-day-2026",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T00:17:27+00:00",
    "summary": "If you&#8217;ve been wanting to buy a robot vacuum but have been put off by how much it can cost to get a good one, now is not a bad time to start looking. Prime Day has kicked off, though more than j"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/949350/amazon-prime-day-sale-best-apple-deals-2026",
    "domain": "大厂 AI 动态",
    "title": "This year’s Prime Day deals on Apple products are the best I’ve seen",
    "url": "https://www.theverge.com/gadgets/949350/amazon-prime-day-sale-best-apple-deals-2026",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T23:58:13+00:00",
    "summary": "Amazon&#8217;s Prime Day sale is here, and whether you&#8217;re looking for a new pair of wireless earbuds or a smartwatch, there’s a good chance you’ll find a discount. The Apple Watch Series 11 has "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/950871/nex-playground-prime-day-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The Nex Playground is down to its pre-RAMageddon price during Prime Day",
    "url": "https://www.theverge.com/gadgets/950871/nex-playground-prime-day-deal-sale",
    "source": "Allison Johnson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T23:00:00+00:00",
    "summary": "The Nex Playground is the family-centric, Kinect-like game console that made one Verge editor’s kids laugh, cry, and ask for more playtime, even when they were sick. The motion-based game play isn’t p"
  },
  {
    "id": "rss:https://www.theverge.com/tech/955385/google-home-familiar-faces-clothing",
    "domain": "大厂 AI 动态",
    "title": "Google Home will soon get better at recognizing you",
    "url": "https://www.theverge.com/tech/955385/google-home-familiar-faces-clothing",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T22:28:19+00:00",
    "summary": "A new update for Google Home could make it less likely your smart home cameras mistake you for someone else, just because you're facing away from the camera. Starting June 23rd, Google's expanding its"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/954899/luca-guadagnino-artificial-sam-altman-amazon-a24-neon-mubi-chatgpt",
    "domain": "大厂 AI 动态",
    "title": "Hollywood is bending the knee to OpenAI",
    "url": "https://www.theverge.com/entertainment/954899/luca-guadagnino-artificial-sam-altman-amazon-a24-neon-mubi-chatgpt",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T22:03:18+00:00",
    "summary": "Netflix, A24, Focus Features, and Warner Bros.' Clockwork have all reportedly decided to pass on picking up Artificial - director Luca Guadagnino's new biographical drama about OpenAI cofounder / CEO "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/953936/roborock-saros-20-amazon-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Prime Day takes $240 off Roborock’s Saros 20, one of our favorite robovacs",
    "url": "https://www.theverge.com/gadgets/953936/roborock-saros-20-amazon-deal-sale",
    "source": "Sheena Vasani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T21:00:00+00:00",
    "summary": "The best robot vacuums are the ones you barely have to think about, and the Roborock Saros 20 fits that description well. It&#8217;s why it&#8217;s one of our favorite robovac / mop hybrids, and thank"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/954049/meta-quest-3s-vr-headset-prime-day-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "The Meta Quest 3S is on sale for $297 — which is basically its old price",
    "url": "https://www.theverge.com/gadgets/954049/meta-quest-3s-vr-headset-prime-day-deal-sale",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T21:00:00+00:00",
    "summary": "The Meta Quest 3S VR headset with 128GB of storage is $296.79 (about $53 off) at Amazon. This is Meta&#8217;s entry-level VR headset, which launched back in 2024 for $299.99 before getting a price inc"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/948610/best-prime-day-tech-deals-sale",
    "domain": "大厂 AI 动态",
    "title": "The best Prime Day deals we found on our favorite gear",
    "url": "https://www.theverge.com/gadgets/948610/best-prime-day-tech-deals-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T20:59:34+00:00",
    "summary": "Amazon’s Prime Day is on, and it’s happening for the next four days. Prime members can jump into the deals now until the sale officially ends at 3:01AM ET / 12:01AM PT June 27th. Many discounts will r"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/955139/xteink-x3-x4-e-ink-reader-amazon-prime-day-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Xteink’s tiny e-readers are 20 percent off for Prime Day",
    "url": "https://www.theverge.com/gadgets/955139/xteink-x3-x4-e-ink-reader-amazon-prime-day-deal-sale",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T20:11:24+00:00",
    "summary": "The Xteink X4 and smaller X3 e-readers are discounted to $55.20 (regularly $69) and $63.20 (normally $79), respectively, as part of Amazon’s Prime Day promotions this week. Both e-readers are signific"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/951901/prime-day-video-games-switch-playstation-xbox-pc-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Prime Day has some solid deals on Switch 2, PS5, and Xbox games",
    "url": "https://www.theverge.com/gadgets/951901/prime-day-video-games-switch-playstation-xbox-pc-deal-sale",
    "source": "Antonio G. Di Benedetto",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T20:00:00+00:00",
    "summary": "There are some some sizable discounts on new and recent hits from the last few years for the Nintendo Switch 2, PlayStation 5, and the Xbox Series X / S for Prime Day. Most Amazon game deals are physi"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/23/how-to-invest-when-everything-is-moving-too-fast/",
    "domain": "大厂 AI 动态",
    "title": "How to invest when everything is moving too fast",
    "url": "https://techcrunch.com/2026/06/23/how-to-invest-when-everything-is-moving-too-fast/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T06:26:11+00:00",
    "summary": "TechCrunch's StrictlyVC evening in Los Angeles late last week brought together two of the more straight-talking investors working in AI right now. They were as entertaining as they were illuminating."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/23/walmart-backed-flipkart-expands-quick-commerce-push-as-amazon-ramps-up-in-india/",
    "domain": "大厂 AI 动态",
    "title": "Walmart-backed Flipkart expands quick-commerce push as Amazon ramps up in India",
    "url": "https://techcrunch.com/2026/06/23/walmart-backed-flipkart-expands-quick-commerce-push-as-amazon-ramps-up-in-india/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T00:30:00+00:00",
    "summary": "Walmart-backed Flipkart has crossed 1,000 micro-fulfillment centers as Amazon accelerates its own quick-commerce push in India."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/23/indias-moengage-bets-marketings-future-on-millions-of-ai-agents/",
    "domain": "大厂 AI 动态",
    "title": "India’s MoEngage bets that the future of marketing is millions of AI agents",
    "url": "https://techcrunch.com/2026/06/23/indias-moengage-bets-marketings-future-on-millions-of-ai-agents/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T23:30:00+00:00",
    "summary": "The all-cash deal gives MoEngage access to technology that assigns AI agents to individual customers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/23/superhuman-acquires-ai-detection-startup-gptzero/",
    "domain": "大厂 AI 动态",
    "title": "Superhuman acquires AI detection startup GPTZero",
    "url": "https://techcrunch.com/2026/06/23/superhuman-acquires-ai-detection-startup-gptzero/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T21:48:23+00:00",
    "summary": "Superhuman, which also has an AI detection tool as part of Grammarly, has snapped up GPTZero."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/23/after-betting-the-firm-on-anthropic-menlo-ventures-raises-victorious-3b-fund/",
    "domain": "大厂 AI 动态",
    "title": "After betting the firm on Anthropic, Menlo Ventures raises victorious $3B fund",
    "url": "https://techcrunch.com/2026/06/23/after-betting-the-firm-on-anthropic-menlo-ventures-raises-victorious-3b-fund/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T19:49:55+00:00",
    "summary": "Menlo has created a solid rep for itself as an AI investor, all based on one gutsy $750 million move in 2024."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/23/klue-says-hackers-stole-credential-from-2022-that-led-to-customer-data-breaches/",
    "domain": "大厂 AI 动态",
    "title": "Klue says hackers stole credential from 2022 that led to customer data breaches",
    "url": "https://techcrunch.com/2026/06/23/klue-says-hackers-stole-credential-from-2022-that-led-to-customer-data-breaches/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T19:43:56+00:00",
    "summary": "It's unclear why Klue had not revoked the credential after the limited pilot, which hackers then used to breach a system holding keys for accessing customers' data."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/23/mark-zuckerberg-wants-meta-to-launch-its-own-prediction-market/",
    "domain": "大厂 AI 动态",
    "title": "Mark Zuckerberg wants Meta to launch its own prediction market",
    "url": "https://techcrunch.com/2026/06/23/mark-zuckerberg-wants-meta-to-launch-its-own-prediction-market/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T19:19:44+00:00",
    "summary": "The app would be independent of Meta's other social media offerings, although sources told the NYT that those social sites could direct users to engagement with the app."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/23/anthropics-claude-tag-is-learning-your-company-one-slack-message-at-a-time/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s Claude Tag is learning your company, one Slack message at a time",
    "url": "https://techcrunch.com/2026/06/23/anthropics-claude-tag-is-learning-your-company-one-slack-message-at-a-time/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T17:00:00+00:00",
    "summary": "Anthropic’s new Claude Tag brings an always-on AI teammate to Slack. But beyond productivity, the feature is a strategic play to capture organizational context, institutional knowledge, and enterprise"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/23/password-manager-maker-lastpass-says-hackers-stole-customer-support-case-data-during-klue-breach/",
    "domain": "大厂 AI 动态",
    "title": "Password manager maker LastPass says hackers stole customer support case data during Klue breach",
    "url": "https://techcrunch.com/2026/06/23/password-manager-maker-lastpass-says-hackers-stole-customer-support-case-data-during-klue-breach/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T15:12:37+00:00",
    "summary": "This is the second data breach to affect LastPass customers in recent years, after one of the password manager's tech partners was recently breached."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/23/halobraid-raises-7m-from-seven-seven-six-to-end-the-six-hour-hair-salon-appointment/",
    "domain": "大厂 AI 动态",
    "title": "HaloBraid raises $7M from Seven Seven Six to end the six-hour hair salon appointment",
    "url": "https://techcrunch.com/2026/06/23/halobraid-raises-7m-from-seven-seven-six-to-end-the-six-hour-hair-salon-appointment/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T15:09:38+00:00",
    "summary": "HaloBraid aims to help salons speed up braiding with its first device, slated to launch later this year, that acts as a braiding assistant for professional stylists."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/23/meta-debuts-new-cheaper-smart-glasses-under-its-own-brand/",
    "domain": "大厂 AI 动态",
    "title": "Meta debuts new, cheaper smart glasses under its own brand",
    "url": "https://techcrunch.com/2026/06/23/meta-debuts-new-cheaper-smart-glasses-under-its-own-brand/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T14:11:23+00:00",
    "summary": "The smart glasses are available in several countries starting today in a variety of color and lens combinations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/23/4-days-left-to-save-up-to-190-on-techcrunch-founder-summit-2026/",
    "domain": "大厂 AI 动态",
    "title": "4 days left to save up to $190 on TechCrunch Founder Summit 2026",
    "url": "https://techcrunch.com/2026/06/23/4-days-left-to-save-up-to-190-on-techcrunch-founder-summit-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T14:00:00+00:00",
    "summary": "Four days left to save up to $190 on your pass to TechCrunch Founder Summit 2026 — the ultimate founder bootcamp — before Early Bird rates end on June 26 at 11:59 p.m. PT. Register today."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/23/ribbie-turns-real-time-baseball-stats-into-arcade-like-pixel-art-broadcasts/",
    "domain": "大厂 AI 动态",
    "title": "Ribbie turns real-time baseball stats into arcade-like, pixel-art broadcasts",
    "url": "https://techcrunch.com/2026/06/23/ribbie-turns-real-time-baseball-stats-into-arcade-like-pixel-art-broadcasts/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T13:58:30+00:00",
    "summary": "Ribbie lets you follow along live with MLB games with a delightful, arcade-inspired interface."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/23/fika-jobs-raises-4m-to-build-a-video-first-hiring-platform-where-ai-agents-interview-candidates/",
    "domain": "大厂 AI 动态",
    "title": "Fika Jobs raises $4M to build a video-first hiring platform where AI agents interview candidates",
    "url": "https://techcrunch.com/2026/06/23/fika-jobs-raises-4m-to-build-a-video-first-hiring-platform-where-ai-agents-interview-candidates/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T13:00:00+00:00",
    "summary": "Stockholm-based startup Fika Jobs is building a video-first hiring platform that combines AI interview agents with short-form video profiles, creating something that feels like a cross between LinkedI"
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/",
    "domain": "大厂 AI 动态",
    "title": "The running list: major tech layoffs in 2026 where employers cited AI",
    "url": "https://techcrunch.com/2026/06/22/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/",
    "source": "Rebecca Bellan, Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T01:27:55+00:00",
    "summary": "A running look — in reverse chronological order — at the bigger tech companies that have announced significant layoffs this year with AI as a stated factor."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/openai-launches-new-initiative-to-help-find-and-patch-open-source-bugs/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI launches new initiative to help find and patch open source bugs",
    "url": "https://techcrunch.com/2026/06/22/openai-launches-new-initiative-to-help-find-and-patch-open-source-bugs/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T00:11:31+00:00",
    "summary": "OpenAI is using AI to help the open source community better protect itself."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/tesla-pushes-back-on-autopilot-narrative-after-fatal-texas-crash/",
    "domain": "大厂 AI 动态",
    "title": "Tesla pushes back on Autopilot narrative after fatal Texas crash",
    "url": "https://techcrunch.com/2026/06/22/tesla-pushes-back-on-autopilot-narrative-after-fatal-texas-crash/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T22:59:57+00:00",
    "summary": "Whether the Autopilot system was truly active, overridden, or malfunctioning likely won't be resolved until investigators finish combing through the vehicle's data logs."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/shareholders-sue-ubers-board-over-sexual-assaults-other-incidents/",
    "domain": "大厂 AI 动态",
    "title": "Shareholders sue Uber’s board over sexual assaults, other incidents",
    "url": "https://techcrunch.com/2026/06/22/shareholders-sue-ubers-board-over-sexual-assaults-other-incidents/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T22:43:12+00:00",
    "summary": "The lawsuit, led by a Detroit pension fund, alleges Uber's board and management has cut too many compliance corners, resulting in thousands of lawsuits."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/the-ai-world-is-getting-loopy/",
    "domain": "大厂 AI 动态",
    "title": "The AI world is getting ‘loopy’",
    "url": "https://techcrunch.com/2026/06/22/the-ai-world-is-getting-loopy/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T20:53:11+00:00",
    "summary": "The loop takes agentic AI a step further by authorizing a swarm of agents to work continuously in the background, endlessly."
  },
  {
    "id": "rss:https://techcrunch.com/2026/06/22/microsoft-and-chevron-plan-one-of-the-largest-gas-powered-data-center-projects-in-us/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft and Chevron plan one of the largest gas-powered data center projects in US",
    "url": "https://techcrunch.com/2026/06/22/microsoft-and-chevron-plan-one-of-the-largest-gas-powered-data-center-projects-in-us/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T20:37:19+00:00",
    "summary": "Microsoft inked a 20-year power purchase agreement with Chevron, locking in decades of carbon emissions from a new natural gas power plant."
  },
  {
    "id": "rss:https://stratechery.com/2026/memory-chips-and-china-microsoft-and-chinese-models/",
    "domain": "大厂 AI 动态",
    "title": "Memory Chips and China, Microsoft and Chinese Models",
    "url": "https://stratechery.com/2026/memory-chips-and-china-microsoft-and-chinese-models/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T10:00:00+00:00",
    "summary": "The big three memory makers may come to regret opening up the door to Chinese memory makers; Microsoft, meanwhile, is very incentivized to use Chinese models."
  },
  {
    "id": "rss:https://stratechery.com/2026/apple-price-increases-apple-intelligence-and-the-e-u/",
    "domain": "大厂 AI 动态",
    "title": "Apple Price Increases, Apple Intelligence and the E.U.",
    "url": "https://stratechery.com/2026/apple-price-increases-apple-intelligence-and-the-e-u/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T10:00:00+00:00",
    "summary": "Apple is (finally) raising prices, but they're not shipping Siri AI to the E.U."
  },
  {
    "id": "rss:https://arstechnica.com/information-technology/2026/06/executive-order-bumps-up-deadline-to-move-off-quantum-vulnerable-crypto/",
    "domain": "大厂 AI 动态",
    "title": "White House drastically shortens deadline for dropping quantum-vulnerable crypto",
    "url": "https://arstechnica.com/information-technology/2026/06/executive-order-bumps-up-deadline-to-move-off-quantum-vulnerable-crypto/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T22:30:57+00:00",
    "summary": "Order warns of national security risks if post-quantum cryptography isn't adopted in time."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/uss-climate-gov-site-taken-down-by-trump-relaunched-by-nonprofit/",
    "domain": "大厂 AI 动态",
    "title": "US's climate.gov site, taken down by Trump, relaunched by nonprofit",
    "url": "https://arstechnica.com/science/2026/06/uss-climate-gov-site-taken-down-by-trump-relaunched-by-nonprofit/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T22:07:56+00:00",
    "summary": "Climate.us has now restored everything taken down by the government."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/police-tout-using-drone-to-disarm-incapacitated-person-in-nationwide-first/",
    "domain": "大厂 AI 动态",
    "title": "Odd police video shows drone removing knife from motionless suspect",
    "url": "https://arstechnica.com/gadgets/2026/06/police-tout-using-drone-to-disarm-incapacitated-person-in-nationwide-first/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T20:43:42+00:00",
    "summary": "Promo video comes as more US police departments fly drones as first responders."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/oracles-21000-layoffs-help-drive-its-debt-fueled-ai-investments/",
    "domain": "大厂 AI 动态",
    "title": "Oracle’s 21,000 layoffs help drive its debt-fueled AI investments",
    "url": "https://arstechnica.com/ai/2026/06/oracles-21000-layoffs-help-drive-its-debt-fueled-ai-investments/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T20:17:38+00:00",
    "summary": "Oracle is spending billions on data center infrastructure to support AI."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/06/a-curious-crossover-the-toyota-c-hr-review/",
    "domain": "大厂 AI 动态",
    "title": "A curious crossover: The Toyota C-HR review",
    "url": "https://arstechnica.com/cars/2026/06/a-curious-crossover-the-toyota-c-hr-review/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T18:19:50+00:00",
    "summary": "Although it's on the smaller side, this electric vehicle is not very chill."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/abc-asks-viewers-to-protest-fcc-attempt-to-control-who-is-allowed-on-the-view/",
    "domain": "大厂 AI 动态",
    "title": "ABC asks viewers to protest FCC attempt to \"control who is allowed\" on The View",
    "url": "https://arstechnica.com/tech-policy/2026/06/abc-asks-viewers-to-protest-fcc-attempt-to-control-who-is-allowed-on-the-view/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T17:59:40+00:00",
    "summary": "\"The FCC wants to control who is allowed on the show,\" ABC ad tells viewers."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/06/early-land-animals-skipped-the-tadpole-phase/",
    "domain": "大厂 AI 动态",
    "title": "Early land animals skipped the tadpole phase",
    "url": "https://arstechnica.com/science/2026/06/early-land-animals-skipped-the-tadpole-phase/",
    "source": "Jacek Krywko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T17:49:09+00:00",
    "summary": "Current amphibian development may not have been typical of early land vertebrates."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/06/trump-may-be-mystery-patient-in-odd-case-of-79yo-getting-experimental-obesity-drug/",
    "domain": "大厂 AI 动态",
    "title": "Trump may be mystery patient in odd case of 79yo getting experimental obesity drug",
    "url": "https://arstechnica.com/health/2026/06/trump-may-be-mystery-patient-in-odd-case-of-79yo-getting-experimental-obesity-drug/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T16:16:54+00:00",
    "summary": "White House spokesperson denied it was Trump only after story was published."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/everyone-pays-the-price-as-patent-holders-on-seeds-stifle-innovation/",
    "domain": "大厂 AI 动态",
    "title": "Everyone pays the price as patent holders on seeds stifle innovation",
    "url": "https://arstechnica.com/tech-policy/2026/06/everyone-pays-the-price-as-patent-holders-on-seeds-stifle-innovation/",
    "source": "Julie Dawson, Kiki Hubbard, and Paulina Jenney, The Conversation",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T13:59:25+00:00",
    "summary": "The US is one of a handful of countries that allow patents on plant varieties."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/06/taika-waititi-brings-more-dramatic-tone-to-klara-and-the-sun-trailer/",
    "domain": "大厂 AI 动态",
    "title": "Sony releases trailer for Taika Waititi's Klara and the Sun",
    "url": "https://arstechnica.com/culture/2026/06/taika-waititi-brings-more-dramatic-tone-to-klara-and-the-sun-trailer/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T13:55:14+00:00",
    "summary": "Tonally, the trailer gives strong vibes akin to the director's 2016 feature Hunt for the Wilderpeople."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/06/how-to-burst-the-ai-bubble-strike-at-its-roots/",
    "domain": "大厂 AI 动态",
    "title": "How to burst the AI bubble: Strike at its roots",
    "url": "https://arstechnica.com/gadgets/2026/06/how-to-burst-the-ai-bubble-strike-at-its-roots/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T12:00:34+00:00",
    "summary": "Sci-fi author/tech journalist Cory Doctorow on his new book, The Reverse Centaur's Guide to Life After AI."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/with-starfall-spacex-eyes-an-edge-in-global-cargo-delivery-from-orbit/",
    "domain": "大厂 AI 动态",
    "title": "With Starfall, SpaceX eyes an edge in global cargo delivery from orbit",
    "url": "https://arstechnica.com/space/2026/06/with-starfall-spacex-eyes-an-edge-in-global-cargo-delivery-from-orbit/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-23T05:25:16+00:00",
    "summary": "The purpose of Starfall is to support the \"transport and delivery of goods through space.\""
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/06/gm-installs-robots-at-flagship-ev-factory-after-laying-off-1300-workers/",
    "domain": "大厂 AI 动态",
    "title": "GM installs robots at flagship EV factory after laying off 1,300 workers",
    "url": "https://arstechnica.com/ai/2026/06/gm-installs-robots-at-flagship-ev-factory-after-laying-off-1300-workers/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T21:52:39+00:00",
    "summary": "US autoworkers union warns of robot automation as dark factory future looms."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/06/report-kennedy-space-center-not-ready-for-era-of-super-heavy-rockets/",
    "domain": "大厂 AI 动态",
    "title": "Report: Kennedy Space Center not ready for era of super heavy rockets",
    "url": "https://arstechnica.com/space/2026/06/report-kennedy-space-center-not-ready-for-era-of-super-heavy-rockets/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T21:28:19+00:00",
    "summary": "SpaceX has told NASA it plans to launch Starship every eight days from Kennedy."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/06/man-used-massage-gun-on-his-tired-eyeballs-it-went-as-well-as-youd-expect/",
    "domain": "大厂 AI 动态",
    "title": "Man used massage gun on his tired eyeballs. It went as well as you'd expect.",
    "url": "https://arstechnica.com/health/2026/06/man-used-massage-gun-on-his-tired-eyeballs-it-went-as-well-as-youd-expect/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T21:02:08+00:00",
    "summary": "He had retinal tears and bruises from squishing his eyeballs with the gun."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/06/polymarkets-viral-videos-showed-people-winning-big-but-the-bets-were-fake/",
    "domain": "大厂 AI 动态",
    "title": "Polymarket's viral videos showed people winning big, but the bets were fake",
    "url": "https://arstechnica.com/tech-policy/2026/06/polymarkets-viral-videos-showed-people-winning-big-but-the-bets-were-fake/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T20:10:34+00:00",
    "summary": "\"Winning\" bets were made on cloned website and would have lost money, WSJ finds."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/06/following-user-outcry-amd-reinstates-memory-encryption-in-consumer-cpus/",
    "domain": "大厂 AI 动态",
    "title": "Following user outcry, AMD reinstates memory encryption in consumer CPUs",
    "url": "https://arstechnica.com/security/2026/06/following-user-outcry-amd-reinstates-memory-encryption-in-consumer-cpus/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T19:16:52+00:00",
    "summary": "Critics saw the move as an underhanded way to steer them toward more costly chips."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/06/valves-steam-machine-ships-june-29-for-1049-but-you-probably-wont-be-able-to-buy-one-yet/",
    "domain": "大厂 AI 动态",
    "title": "Valve's Steam Machine ships June 29 for $1,049, but you probably won't be able to buy one yet",
    "url": "https://arstechnica.com/gaming/2026/06/valves-steam-machine-ships-june-29-for-1049-but-you-probably-wont-be-able-to-buy-one-yet/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-22T19:02:45+00:00",
    "summary": "Valve says it's using a randomized purchase queue to make the experience \"less frustrating and more fair.\""
  },
  {
    "id": "wscn:3775351",
    "domain": "股票",
    "title": "全球股市波动加剧，韩股上演“过山车行情”，美元触及七个月高位，黄金跌超1.3%",
    "url": "https://wallstreetcn.com/articles/3775351",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T06:38:15+00:00",
    "summary": "韩国首尔综指收涨3.3%，报8471.02点。此前一度跌超1%。美国股指期货小幅走高。国际原油价格继续承压，WTI原油日内跌幅0.42%、跌破73关口。10年期美债收益率持稳于4.5%下方。美元指数在连续两日上涨后趋于稳定，日内微涨0.05%，持平于101.4附近。"
  },
  {
    "id": "wscn:3775374",
    "domain": "股票",
    "title": "A股再现“大肉签”！688797，飙涨900%",
    "url": "https://wallstreetcn.com/articles/3775374",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T06:28:19+00:00",
    "summary": "国产半导体核心零部件龙头臻宝科技6月24日登陆科创板，盘中最高涨幅超900%，股价一度飙至465元，中一签最高盈利超20万元，总市值近660亿元，较44.56元的发行价暴涨逾850%，成为近期A股市场最强新股之一。"
  },
  {
    "id": "wscn:3775295",
    "domain": "股票",
    "title": "李蓓私募单周净值跌超15%：市场正在经历怎样的K型裂变？",
    "url": "https://wallstreetcn.com/premium/articles/3775295?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T06:18:33+00:00",
    "summary": "李蓓规模腰斩折射市场K型分化加剧，科技资本开支扩张主导行情，AI泡沫隐现但产业景气尚未见顶。"
  },
  {
    "id": "wscn:3775375",
    "domain": "股票",
    "title": "Anthropic发布重大更新推出CC进化版Claude Tag，Karpathy：LLM第三次交互革命来了",
    "url": "https://wallstreetcn.com/articles/3775375",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T06:14:56+00:00",
    "summary": "Anthropic推出Claude Code进化版“Claude Tag”。它以团队成员身份接入Slack，具备多人协作、持续学习、主动介入与异步执行四大核心能力。Karpathy称其开启了LLM第三次交互革命：AI已演变为拥有组织工具和上下文、与人类并肩工作的独立异步实体。"
  },
  {
    "id": "wscn:3775378",
    "domain": "股票",
    "title": "华硕预判PC涨价潮降温，预计第三季度只会出现个位数的涨幅",
    "url": "https://wallstreetcn.com/articles/3775378",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T05:43:31+00:00",
    "summary": "华硕预计第三季度产品价格涨幅将收窄至个位数，意味着自2025年四季度以来累计上涨30%的PC涨价潮有所放缓。这主要得益于核心零部件价格回调及市场承压，但分析师警告内存价格上涨压力或延续至2028年。"
  },
  {
    "id": "wscn:3775377",
    "domain": "股票",
    "title": "特朗普施压石油公司：油价必须更快下跌，否则面临司法部调查",
    "url": "https://wallstreetcn.com/articles/3775377",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T05:41:48+00:00",
    "summary": "特朗普怒斥大型石油公司\"哄抬油价\"，亲自喊话司法部立即介入调查，强硬表态再度拖累国际油价跌破关键位。然而专家直言此举不过是\"政治秀\"——汽油定价链条复杂，零售价滞后原油数周才能传导。与此同时，霍尔木兹海峡通航改善，供应压力或迎来实质性缓解。"
  },
  {
    "id": "wscn:3775380",
    "domain": "股票",
    "title": "奥斯曼・登贝莱 （OUSMANE DEMBÉLÉ） 携手亨利・雅克（Henry Jacques） 不期而遇，续写宿命之约",
    "url": "https://wallstreetcn.com/articles/3775380",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T05:37:24+00:00",
    "summary": "胆识与创造力兼具的传奇香氛世家，邂逅心怀热爱的香水藏家，万般可能，皆由此生。"
  },
  {
    "id": "wscn:3775362",
    "domain": "股票",
    "title": "创业板涨1%，科创50暴涨近4%，PCB、光通信反弹，创新药再拉升，恒科指涨超2%，半导体狂飙",
    "url": "https://wallstreetcn.com/articles/3775362",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T05:30:49+00:00",
    "summary": "盘面上，个股跌多涨少，沪深京三市近4500股飘绿，上午半天成交2.1万亿。沪深两市半日成交额2.09万亿，较上个交易日缩量2318亿。板块方面，半导体产业链逆势走强，先进封装、存储器、PCB方向领涨；锂矿、CRO、氟化工概念股活跃。金融科技、AI应用、工业金属、大消费题材调整。"
  },
  {
    "id": "wscn:3774769",
    "domain": "股票",
    "title": "下一个六氟化钨？金属铋7月或将迎来大变局",
    "url": "https://wallstreetcn.com/premium/articles/3774769?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T05:17:21+00:00",
    "summary": "日本泰和热磁（全球碲化铋市场60%份额）7N碲化铋库存预计6月底耗尽，已停止接受800G和1.6T光模块用TEC的新订货，全球AI光模块供应链正面临实质性断裂风险。"
  },
  {
    "id": "wscn:3774507",
    "domain": "股票",
    "title": "金刚石散热：超越液冷，它是AI“热力学终极圣杯”？",
    "url": "https://wallstreetcn.com/premium/articles/3774507?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:10:34+00:00",
    "summary": "传统铜基散热材料的热导率天花板（约400W/m·K）与热膨胀系数不匹配（铜约17×10⁻⁶/K vs 硅约2.6×10⁻⁶/K）两大物理瓶颈已难以支撑下一代AI芯片的散热需求。金刚石材料凭借2200W/m·K的超高热导率（铜的5倍以上）、与硅接近的热膨胀系数（约1.1ppm/K）以及优异的化学稳定性，成为目前唯一能够同时满足高导热、低热应力、长寿命三大要求的散热方案候选者。"
  },
  {
    "id": "wscn:3775139",
    "domain": "股票",
    "title": "高端PI膜：黄金薄膜的\"供需悬崖\"，从1.2万吨缺口演化220亿国产替代蓝海",
    "url": "https://wallstreetcn.com/premium/articles/3775139?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:01:25+00:00",
    "summary": "产业链反馈显示，宇部兴产（UBE）电子级PI膜80%产能已被下游以溢价锁定，海外大厂产能被英伟达等AI算力巨头锁至2027年。这揭示了高端PI膜很可能正经历结构性供需失衡的临界点。"
  },
  {
    "id": "wscn:3775368",
    "domain": "股票",
    "title": "高盛相信“腾讯估值修复取决于AI叙事进展”，微信AI内测是关键一步",
    "url": "https://wallstreetcn.com/articles/3775368",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T03:48:36+00:00",
    "summary": "微信AI助手\"小微\"启动内测，标志着这一超级应用正式进军智能体赛道。然而腾讯股价周一下跌1.6%，跑输大盘。高盛指出，市场疑虑集中于三点：自研WeLM模型与混元并行引发资源重复投入担忧；全面推广后推理成本或侵蚀利润达5%-17%；短期变现路径尚不清晰。"
  },
  {
    "id": "wscn:3775369",
    "domain": "股票",
    "title": "种种迹象显示“接近周期顶部”，但瑞银坚持：现在退出中国科技股“为时过早”",
    "url": "https://wallstreetcn.com/articles/3775369",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T03:47:50+00:00",
    "summary": "全球芯片股暴跌当日，瑞银发布报告指出中国AI科技上行周期已出现仓位拥挤、估值偏高、IPO增多等“接近顶部”信号，但维持超配判断。核心依据是：当前盈利增速约80%，过去3个月盈利预期上调15%，订单能见度延伸至2027年底；历史上科技股在触顶前最后3个月平均仍有48%涨幅。"
  },
  {
    "id": "wscn:3775354",
    "domain": "股票",
    "title": "终于涨不动了，开启调整的美股支撑位在哪？",
    "url": "https://wallstreetcn.com/articles/3775354",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T03:38:25+00:00",
    "summary": "美股三个月狂飙后骤然失速，芯片股抛售拖累纳指重挫，标普逼近技术十字路口。标普500指数近端支撑是7340、7237点，中期防线为7000点；纳指100指数方面，29300、28930点和50日均线为支撑位；市场广度能否修复，或成AI行情续命关键。"
  },
  {
    "id": "wscn:3775365",
    "domain": "股票",
    "title": "“AI需求可见度”延伸至2028年！美银美林：存储在此之前不会“供过于求”，半导体设备将大幅增长",
    "url": "https://wallstreetcn.com/articles/3775365",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T03:16:39+00:00",
    "summary": "在全球芯片股遭遇“芯片惨剧”当天，美银发布报告，将AI需求可见度延伸至2028年。DRAM/NAND供给充裕率在2028年前持续高于110%，不存在实质性过剩风险；半导体设备支出2028年将达2500亿美元，较此前预测上调23%。该行据此将美光目标价上调至1500美元。"
  },
  {
    "id": "wscn:3774983",
    "domain": "股票",
    "title": "锂电添加剂VC：淡季不淡仅是序章，Q3量价齐升或为高潮",
    "url": "https://wallstreetcn.com/premium/articles/3774983?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T02:49:56+00:00",
    "summary": "VC淡季不淡验证景气上行。"
  },
  {
    "id": "wscn:3775360",
    "domain": "股票",
    "title": "豆包正式推出收费版，三档定价、最高一年6000元，贵不贵？",
    "url": "https://wallstreetcn.com/articles/3775360",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T02:38:34+00:00",
    "summary": "豆包正式上线专业版付费订阅，三档定价为68元、200元、500元/月，高级版一年最高6000元，免费版日常功能不受影响。核心新功能是接入豆包2.1 Pro模型的“办公任务模式”，支持操控本地电脑、定时任务、内置Office套件等。收费背后是严峻的成本压力：日均算力消耗数千万元，但日收入不足百万元。"
  },
  {
    "id": "wscn:3775367",
    "domain": "股票",
    "title": "越疆科技一季度营收增长111%：“All in 具身智能”战略进入商业回报期",
    "url": "https://wallstreetcn.com/articles/3775367",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T02:36:17+00:00",
    "summary": "2026年6月23日，越疆科技披露一季度未经审计营运数据：营业收入约人民币1.12亿元，同比增长约1..."
  },
  {
    "id": "wscn:3775356",
    "domain": "股票",
    "title": "微信6年来最大改版——关于微信AI助手小微的15条思考",
    "url": "https://wallstreetcn.com/articles/3775356",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T02:36:16+00:00",
    "summary": "微信6年最大改版来了——AI助手“小微”低调灰度测试，却暗藏大棋局。语音优先、多入口融合、自然语言激活支付/朋友圈等沉寂数据，还能几分钟生成专属小工具。更关键的是，小微一旦全量上线，凭借14亿用户或将成全球第二大AI助手，真正的对手不是豆包，而是苹果Siri。"
  },
  {
    "id": "wscn:3775364",
    "domain": "股票",
    "title": "全球科技股暴跌：AI牛市的又一场压力测试",
    "url": "https://wallstreetcn.com/articles/3775364",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T02:07:38+00:00",
    "summary": "HBM4扩产放缓消息、美光财报前仓位出逃、监管警告杠杆ETF、养老基金罕见转身做卖方，四重信号24小时共振，在韩国引爆了一个被300亿美元杠杆产品深度绑架的市场，并向全球市场传导。AI叙事正从\"无限想象\"切换至\"计算回报\"，美光财报将是定性这场暴跌究竟是技术踩踏还是牛市转折的最终裁判。"
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
    "id": "rss:https://www.netinterest.co/p/ai-and-i",
    "domain": "股票",
    "title": "AI and I",
    "url": "https://www.netinterest.co/p/ai-and-i",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-02-20T17:21:53+00:00",
    "summary": "Claude Code, Bloomberg and the Battle for Data"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.23873",
    "domain": "金融",
    "title": "Relaxation Times for Nonextensive Systems Using Gradient Flow for the Maximization of Tsallis Entropy: An Application to Financial Market Dynamics",
    "url": "https://arxiv.org/abs/2606.23873",
    "source": "Sandhya Devi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2606.23873v1 Announce Type: new Abstract: In this work, we develop a method to estimate the relaxation time (the time required to reach equilibrium) of a nonextensive system such as financial ma"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.23883",
    "domain": "金融",
    "title": "Monotonicity of Normalized Implied-Volatility Coordinates under No-Arbitrage",
    "url": "https://arxiv.org/abs/2606.23883",
    "source": "Jian Sun",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2606.23883v1 Announce Type: new Abstract: For a fixed maturity, an arbitrage-free option smile induces natural normalized strike coordinates. This paper makes three contributions. First, it give"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.23922",
    "domain": "金融",
    "title": "Regenerative Bonds: Formal Debt, Mutual-Aid, and Local Settlement Capacity",
    "url": "https://arxiv.org/abs/2606.23922",
    "source": "William O. Ruddick (Yeshey), Alex (Yeshey), Cahana, Tom Shael",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2606.23922v1 Announce Type: new Abstract: This paper develops regenerative bonds as formal debt instruments whose disclosed use-of-proceeds and governance rules allocate proceeds to locally gove"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.24019",
    "domain": "金融",
    "title": "Empirical Confirmation of the Square-Root Law of Market Impact in a U.S. Large-Cap Equity",
    "url": "https://arxiv.org/abs/2606.24019",
    "source": "Aniket Vasaikar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2606.24019v1 Announce Type: new Abstract: We test the square-root law (SRL) of market impact on a single U.S. large-capitalisation equity, Apple Inc. (AAPL), using the full Nasdaq TotalView-ITCH"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.24212",
    "domain": "金融",
    "title": "Path Space Robust Bayesian Portfolio Selection",
    "url": "https://arxiv.org/abs/2606.24212",
    "source": "Andy Au",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2606.24212v1 Announce Type: new Abstract: A Bayesian investor learns an unknown asset drift by Kalman-Bucy filtering and trades the mean-variance optimal portfolio, but his observation model may"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.24309",
    "domain": "金融",
    "title": "Randomized Neural Networks for estimation of exposure profiles and Credit Valuation Adjustment (CVA) for American Equity Options",
    "url": "https://arxiv.org/abs/2606.24309",
    "source": "Isidro Moroso Varona, Jakub Micha\\'nk\\'ow, Pawe{\\l} Sakowski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2606.24309v1 Announce Type: new Abstract: This thesis studies the use of randomized neural networks for the estimation of exposure profiles and unilateral CVA of American options within a Monte "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.24319",
    "domain": "金融",
    "title": "Spatial accessibility to food banks hinders food parcel uptake in England and Wales, particularly in rural areas",
    "url": "https://arxiv.org/abs/2606.24319",
    "source": "Laura Sheppard, Carmen Cabrera, Daphne Badounas, Bonnie Boyana Buyuklieva, Sukankana Chakraborty, Huanfa Chen, Sarah Wise, Howard Wong, Rachael Jones, Neave O'Clery",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2606.24319v1 Announce Type: new Abstract: Food bank use in the UK has soared in recent years. The combination of a global pandemic, over-stretched and underfunded public services, and a cost-of-"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.24399",
    "domain": "金融",
    "title": "Energy Poverty as a Structural Trap: The Role of Housing Efficiency and Non-Convex Technology",
    "url": "https://arxiv.org/abs/2606.24399",
    "source": "Nazaria Solferino",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2606.24399v1 Announce Type: new Abstract: Energy poverty persists even among households that are not income-poor, suggesting a deeper mechanism than mere budget constraints. We develop a model i"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.24439",
    "domain": "金融",
    "title": "Change from within? The strategies used by public officials to advance post-growth approaches",
    "url": "https://arxiv.org/abs/2606.24439",
    "source": "Laura Angresius, Milena B\\\"uchs, Daniel W. O'Neill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2606.24439v1 Announce Type: new Abstract: Current societies face interconnected environmental and social crises. Post-growth research argues that addressing these challenges requires a reorganiz"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.23980",
    "domain": "金融",
    "title": "Diagonal Frog: High-order positivity-preserving FD schemes for anisotropic Fokker-Planck equations",
    "url": "https://arxiv.org/abs/2606.23980",
    "source": "Andrey Itkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2606.23980v1 Announce Type: cross Abstract: The Fokker-Planck equation is fundamental to statistical mechanics, yet in settings with multiple state variables, anisotropic (cross-) diffusion, and"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.24616",
    "domain": "金融",
    "title": "AI Tokenomics: The Economics of Tokens, Computation, and Pricing in Foundation Models",
    "url": "https://arxiv.org/abs/2606.24616",
    "source": "Quanyan Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2606.24616v1 Announce Type: cross Abstract: Tokens have become the practical accounting unit for modern foundation model services, linking information processing, computation, memory use, energy"
  },
  {
    "id": "rss:https://arxiv.org/abs/2108.02283",
    "domain": "金融",
    "title": "Machine Learning Classification and Portfolio Construction: Does the Loss Function Matter?",
    "url": "https://arxiv.org/abs/2108.02283",
    "source": "Yang Bai, Kuntara Pukthuanthong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2108.02283v3 Announce Type: replace Abstract: Classification outperforms regression across matched machine learning models in portfolio construction. A stacking ensemble of gradient boosted tree"
  },
  {
    "id": "rss:https://arxiv.org/abs/2407.18957",
    "domain": "金融",
    "title": "When AI Meets Finance (StockAgent): Large Language Model-based Stock Trading in Simulated Real-world Environments",
    "url": "https://arxiv.org/abs/2407.18957",
    "source": "Chong Zhang, Xinyi Liu, Zhongmou Zhang, Mingyu Jin, Lingyao Li, Zhenting Wang, Wenyue Hua, Dong Shu, Suiyuan Zhu, Xiaobo Jin, Sujian Li, Mengnan Du, Yongfeng Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2407.18957v5 Announce Type: replace Abstract: Can AI Agents simulate real-world trading environments to investigate the impact of external factors on stock trading activities (e.g., macroeconomi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.00368",
    "domain": "金融",
    "title": "Exploring Trade Openness and Logistics Efficiency in the G20 Economies: A Bootstrap ARDL Analysis of Growth Dynamics",
    "url": "https://arxiv.org/abs/2509.00368",
    "source": "Haibo Wang, Lutfu Sua",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2509.00368v3 Announce Type: replace Abstract: This study examines the relationship between trade openness, logistics performance, and economic growth within G20 economies. Using a Bootstrap Auto"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.19271",
    "domain": "金融",
    "title": "Managing Portfolios Across the Return Distribution",
    "url": "https://arxiv.org/abs/2510.19271",
    "source": "Jozef Barunik, Lukas Janasek, Attila Sarkany",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2510.19271v2 Announce Type: replace Abstract: We develop a dynamic portfolio-choice framework in which investors target the region of the payoff distribution that the portfolio is designed to im"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.19511",
    "domain": "金融",
    "title": "Compensation-based risk-sharing",
    "url": "https://arxiv.org/abs/2510.19511",
    "source": "Jan Dhaene, Atibhav Chaudhry, Ka Chun Cheung, Austin Riis-Due",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2510.19511v4 Announce Type: replace Abstract: This paper studies the mathematical problem of allocating payouts (compensations) in an endowment contingency fund using a risk-sharing rule that sa"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08419",
    "domain": "金融",
    "title": "The Winner's Bliss in Common-Value Auctions under Horizontal Differentiation",
    "url": "https://arxiv.org/abs/2606.08419",
    "source": "Jiawei Chen, Anh Nguyen, Matthew Shum",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2606.08419v2 Announce Type: replace Abstract: We study common-value auctions in which bidders have horizontally differentiated preferences. In a specific two-bidder parameterization, winning con"
  },
  {
    "id": "rss:https://arxiv.org/abs/2506.08026",
    "domain": "金融",
    "title": "TIP-Search: Time-Predictable Inference Scheduling for Market Prediction under Uncertain Load",
    "url": "https://arxiv.org/abs/2506.08026",
    "source": "Xibai Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2506.08026v4 Announce Type: replace-cross Abstract: Real-time market prediction services need correct predictions before a decision deadline; a correct prediction delivered late is not usable. T"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.15991",
    "domain": "金融",
    "title": "Quantum Futures Interactive: A Live Demonstration of Post-Quantum Blockchain Security, Infrastructure Tradeoffs, and Sustainable Distributed Trust",
    "url": "https://arxiv.org/abs/2605.15991",
    "source": "Dongping Liu, Aoyu Zhang, Luyao Zhang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2605.15991v3 Announce Type: replace-cross Abstract: Advances in quantum computing challenge the hardness assumptions underlying widely deployed public-key cryptography in blockchain systems. Alt"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.22337",
    "domain": "金融",
    "title": "Theorist Toolbox: Tools for Agent Based LLM-assisted economic theory Research",
    "url": "https://arxiv.org/abs/2606.22337",
    "source": "Moran Koren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2606.22337v2 Announce Type: replace-cross Abstract: Empirical economists often start their projects with a toolbox. Shared packages, replication archives, and circulated guides shorten the time "
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.23032",
    "domain": "金融",
    "title": "IPO Finance Agent: Evaluation of LLM Financial Analysts beyond Finance Agent v2, with Automated Rubric Generation -- the Case of the SpaceX (SPCX) IPO",
    "url": "https://arxiv.org/abs/2606.23032",
    "source": "Mostapha Benhenda",
    "platform": "rss",
    "points": null,
    "published_at": "2026-06-24T04:00:00+00:00",
    "summary": "arXiv:2606.23032v2 Announce Type: replace-cross Abstract: Finance Agent v2 (by Vals AI) has emerged as the reference benchmark for evaluating both Anthropic Claude and OpenAI ChatGPT frontier language"
  }
]
```
