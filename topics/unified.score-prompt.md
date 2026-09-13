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

- 今日日期：`2026-09-13`
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
  "date": "2026-09-13",
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
    "points": 4521404,
    "published_at": "2026-01-15T03:56:12+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n1. 构建智能体设计模式：反射、工具使用、规划与多智能体工作流；\n2. 将人工智能与外部工具集成：数据库、API、网络搜索与代码执行；\n3. 评估并优化人工智能系统：性能指标、错误分析与生产部署"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1909299,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "8分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1854638,
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
    "points": 1355718,
    "published_at": "2026-07-05T02:00:00+00:00",
    "summary": "用不上codex的朋友们！新的国产Agent直接上手，来跑通8大用法～\n感谢朋友们的三连+关注～"
  },
  {
    "id": "bvid:BV14rzQB9EJj",
    "domain": "AI",
    "title": "Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill / Hook / 图片 / 上下文处理/ 后台任务",
    "url": "http://www.bilibili.com/video/av115954889596221",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1310107,
    "published_at": "2026-01-25T08:55:20+00:00",
    "summary": "时间戳如下，方便大家跳转观看：\n \n第一部分：环境搭建与基础交互\n- 01:09 安装 Claude Code\n- 01:43 登录与授权\n- 02:55 第一个实战问题\n- 03:12 三种模式详解 (默认/自动/规划)\n \n第二部分：复杂任务处理与终端控制\n- 06:00 执行终端命令 (Bash)\n- 06:49 使用规划模式 (Plan Mode)\n- 11:06 跳过所有权限检测 (da"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1282329,
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
    "points": 1205100,
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
    "points": 884977,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 818958,
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
    "points": 757196,
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
    "points": 673769,
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
    "points": 442417,
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
    "points": 422782,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1GsY76dEqW",
    "domain": "AI",
    "title": "一口气搞懂Agent到底怎么用！",
    "url": "http://www.bilibili.com/video/av117252103997988",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 393623,
    "published_at": "2026-09-11T11:30:00+00:00",
    "summary": "AI Agent这两年大家都听麻了，但真到上手，claude、codex这些又是注册、又是命令行，人还没踏进Agent大门，就先被劝退了。这期视频我用0门槛的国产Agent——字节旗下的TraeWork，用六个超真实的案例，手把手带你玩转Agent！完整的文字教程和GitHub神级Skill清单，打包放置顶评论了。教程制作不易，觉得有一点点帮助的话，记得一键三连～"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 391120,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 332696,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 287832,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 287597,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 279411,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 260052,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 193463,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 181184,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 171756,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 162032,
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
    "points": 156061,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 114734,
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
    "points": 93673,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV143wwz6E8F",
    "domain": "AI",
    "title": "Claude code科研使用展示与思路分享（提速就靠Ai）",
    "url": "http://www.bilibili.com/video/av116211882920985",
    "source": "科研推土机",
    "platform": "bilibili",
    "points": 75225,
    "published_at": "2026-03-11T18:12:00+00:00",
    "summary": "本期给大家带来的是Claude在Vscode的科研应用演示与我最近的一些心得使用心得，科研速度嘎嘎提升。论文复现画图、数据分析就靠Claude code。这个课程也是科研推土机「系统管理文献课程2.0」学员催我更新的内容，希望能帮助到大家～，这个视频重点讲两个事情：\n1️⃣ 资料获取，free不用怀疑，我是良心可言博主，，关注我(GZTSHNR)～\n2️⃣ 展示如何在VS code实操应用clau"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 74583,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1A24y1J7Dt",
    "domain": "AI",
    "title": "如何在VS Code中使用Cursor自动生成代码",
    "url": "http://www.bilibili.com/video/av781409810",
    "source": "许你再少年",
    "platform": "bilibili",
    "points": 74356,
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
    "points": 55051,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operit教程：入门安卓最强大ai平台operitAI",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 44345,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 43569,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 39809,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 39152,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30587,
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
    "points": 28930,
    "published_at": "2025-01-25T09:40:12+00:00",
    "summary": "今天第19课分享如何用Cursor开发安卓APP。\n.\n开发安卓APP和开发iOS APP在整体流程上其实差不多，区别主要在于技术栈、开发工具，以及上架应用商店所需材料的不同，所以这期视频更多放在两者的差别上，共同点没有赘述太多。"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 25686,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22774,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1hmb26ZEws",
    "domain": "AI",
    "title": "DeepSeek Harness 实测  Claude Code 对比后，梁神我错了 差距比我想的大",
    "url": "http://www.bilibili.com/video/av117100337236191",
    "source": "程序员晓刘",
    "platform": "bilibili",
    "points": 22167,
    "published_at": "2026-08-15T16:01:38+00:00",
    "summary": "这期用同一个 DeepSeek Pro 0813 模型，分别在 Claude Code 和 DeepSeek Harness 里完成同样的任务，对比工具链对最终效果的影响。\n实测内容包括：\nFPS 游戏 Demo、灯塔预警沙盘、手枪组装动画、显示器组装动画，以及 DeepSeek Harness 的插件化源码流程。\n整体看下来，模型本身当然重要，但 Harness 在插件化、流程记录、缓存命中和任"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 21949,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1eMgG6QEeG",
    "domain": "AI",
    "title": "【吴恩达】这绝对是把《Vibe Coding》讲得最通透的一套课！手把手教你构建自己的企业级AI工作流，学完直接落地！——附带课件代码",
    "url": "http://www.bilibili.com/video/av117081815189025",
    "source": "吴恩达Agents",
    "platform": "bilibili",
    "points": 20511,
    "published_at": "2026-08-12T09:29:57+00:00",
    "summary": "Vibe Coding火了，但你会发现——AI写的代码像开盲盒，今天能跑明天崩，项目一大就乱套。\n规范驱动开发（SDD） 就是来解决这个问题的。它的核心理念很简单：在让AI写代码之前，先和AI在统一的规范文档里对齐需求，把开发变成可预测、可追溯、可控制的过程。"
  },
  {
    "id": "bvid:BV14erKYuEaE",
    "domain": "AI",
    "title": "最强编程AI Cursor+Unity制作一个史诗游戏(详细)",
    "url": "http://www.bilibili.com/video/av113774908413987",
    "source": "多西杰克",
    "platform": "bilibili",
    "points": 17818,
    "published_at": "2025-01-05T09:01:00+00:00",
    "summary": "网上惊呼Cursor AI厉害的内容很多，但结合Unity做游戏的不多，我就来实测一下，做一个AAA大作......"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 16226,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1YGKJ6tEdz",
    "domain": "AI",
    "title": "Vibe Coding我的赛博女友",
    "url": "http://www.bilibili.com/video/av116933101950817",
    "source": "天工开帧",
    "platform": "bilibili",
    "points": 16103,
    "published_at": "2026-07-17T09:50:00+00:00",
    "summary": "Vibe Coding大赏之赛博女友。总体花费100个馒头左右，由于显存限制，目前实时数字人的版本没办法跑起来。目前可以24挂着，随时对话随时打断。作用嘛，除了聊天就是在我忙的时候顺手帮我查个东西。未来开发方向接入pi-agent，让它真正干活，当然，只是得上qwen27B以上得模型才有可用性。也就是说所有模型显存开销打底得36G以上。囧。当然如果不要无限制，可以接入在线模型或在线TTS，但是，我"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 12066,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1TtwCehEzG",
    "domain": "AI",
    "title": "cursor新手必会的怎么回退代码 防止改错改乱代码 提高效率开发",
    "url": "http://www.bilibili.com/video/av113855472605087",
    "source": "项目禅",
    "platform": "bilibili",
    "points": 11476,
    "published_at": "2025-01-19T14:29:21+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1f2Ys6XES8",
    "domain": "AI",
    "title": "【2026最新版】这绝对是b站将Claude Code实战讲的最好的教程，手把手教你在国内从安装到代码实战的保姆级教程！!让你少走99%弯路！",
    "url": "http://www.bilibili.com/video/av117238682097810",
    "source": "码士集团-马小萱",
    "platform": "bilibili",
    "points": 11123,
    "published_at": "2026-09-09T02:27:07+00:00",
    "summary": "视频制作不易，如果视频对你有用的话请一键三连【长按点赞】支持一下up哦，拜托，这真的对我很重要！"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 10595,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV1xh3C6cEGv",
    "domain": "AI",
    "title": "两周完成一篇SCI论文，用claude code帮你干",
    "url": "http://www.bilibili.com/video/av117002408559933",
    "source": "博士大师兄木水",
    "platform": "bilibili",
    "points": 10298,
    "published_at": "2026-07-29T08:53:04+00:00",
    "summary": "大师兄八股文SCI速成模板已制作成skill，手把手带你实现一键生成SCI论文初稿"
  },
  {
    "id": "hn:49673098",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is the central bank of AI",
    "url": "https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai",
    "source": "tolugenius",
    "platform": "hackernews",
    "points": 465,
    "published_at": "2026-09-12T15:08:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49548952",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia to acquire Hugging Face",
    "url": "https://www.cnbc.com/2026/09/03/nvidia-agrees-to-buy-hugging-face-for-almost-13-billion-ai-expansion.html",
    "source": "tosh",
    "platform": "hackernews",
    "points": 329,
    "published_at": "2026-09-03T12:10:33+00:00",
    "summary": ""
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
    "id": "rss:https://www.eetimes.com/inside-architect-labs-two-week-chip-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside Architect Labs’ Two-Week Chip Design",
    "url": "https://www.eetimes.com/inside-architect-labs-two-week-chip-design/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T02:00:00+00:00",
    "summary": "Architect Labs says its AI can drag custom chip design from years to weeks with Redwood. The post Inside Architect Labs’ Two-Week Chip Design appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/fabships-aim-to-exploit-free-space-vacuum-for-compound-semiconductor-substrates/",
    "domain": "AI 算力 / 半导体",
    "title": "Fabships Aim to Exploit ‘Free’ Space Vacuum for Compound Semiconductor Substrates",
    "url": "https://www.eetimes.com/fabships-aim-to-exploit-free-space-vacuum-for-compound-semiconductor-substrates/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T21:00:00+00:00",
    "summary": "Space is the next frontier for semiconductor manufacturing, as startup Besxar, founded by an ex-OpenAI technical director, completed its first SpaceX flight and recovered wafer samples without contami"
  },
  {
    "id": "rss:https://www.eetimes.com/soc-planner-a-new-generation-of-automated-soc-design-exploration-managing-cost-effectiveness-and-sustainability/",
    "domain": "AI 算力 / 半导体",
    "title": "SoC PLANNER: A New Generation of Automated SoC Design Exploration Managing Cost-Effectiveness and Sustainability",
    "url": "https://www.eetimes.com/soc-planner-a-new-generation-of-automated-soc-design-exploration-managing-cost-effectiveness-and-sustainability/",
    "source": "Defacto Technologies",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T14:36:58+00:00",
    "summary": "GRENOBLE, France &#8211; [2026, September 8th] CEA, Defacto Technologies, and Innova Advanced Technologies today announced the completion of SoC PLANNER, a three-years project funded by BPI France, as"
  },
  {
    "id": "rss:https://www.eetimes.com/should-standards-trump-innovation/",
    "domain": "AI 算力 / 半导体",
    "title": "Should Standards Trump Innovation?",
    "url": "https://www.eetimes.com/should-standards-trump-innovation/",
    "source": "Prakash Sangam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T13:52:31+00:00",
    "summary": "Standards shouldn’t muzzle RFID’s next leap: Gen2X keeps Gen2 compatibility while boosting range, speed, and reliability. The post Should Standards Trump Innovation? appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/build-a-high-end-amd-gaming-pc-for-less-ryzen-7-9800x3d-bundle-includes-an-x870e-motherboard-32gb-ddr5-aio-cooler-and-a-game-for-usd1-109-99",
    "domain": "AI 算力 / 半导体",
    "title": "Build a high-end AMD gaming PC for less — Ryzen 7 9800X3D bundle includes an X870E motherboard, 32GB DDR5, AIO cooler and a game for $1,109.99",
    "url": "https://www.tomshardware.com/pc-components/build-a-high-end-amd-gaming-pc-for-less-ryzen-7-9800x3d-bundle-includes-an-x870e-motherboard-32gb-ddr5-aio-cooler-and-a-game-for-usd1-109-99",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T00:42:50+00:00",
    "summary": "The bundle pairs one of the best gaming CPUs available with a premium X870E motherboard and 32GB of DDR5-6000 memory, while also throwing in a 240mm AIO cooler and a free copy of Onimusha: Way of the "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/iran-and-houthi-rebels-used-anthropics-claude-ai-to-target-us-warships-and-build-hypersonic-missiles-houthi-rebels-also-used-the-bot-to-code-ballistic-missile-guidance-systems",
    "domain": "AI 算力 / 半导体",
    "title": "Iran and Houthi rebels used Anthropic's Claude AI to target US warships and build hypersonic missiles — Houthi rebels also used the bot to code ballistic missile guidance systems",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/iran-and-houthi-rebels-used-anthropics-claude-ai-to-target-us-warships-and-build-hypersonic-missiles-houthi-rebels-also-used-the-bot-to-code-ballistic-missile-guidance-systems",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T15:03:10+00:00",
    "summary": "'Great Satan's' AI comes in handy."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/us-customs-supervisor-busted-for-stealing-core-i7-cpus-ram-and-hard-drives-from-homeland-security-pcs-stolen-tech-swapped-with-inferior-hardware-and-cashed-out-on-newegg",
    "domain": "AI 算力 / 半导体",
    "title": "US Customs supervisor busted for stealing Core i7 CPUs, RAM, and hard drives from Homeland Security PCs, damage estimated at $105,800 — stolen tech swapped with inferior hardware and cashed out on New",
    "url": "https://www.tomshardware.com/pc-components/us-customs-supervisor-busted-for-stealing-core-i7-cpus-ram-and-hard-drives-from-homeland-security-pcs-stolen-tech-swapped-with-inferior-hardware-and-cashed-out-on-newegg",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T14:09:29+00:00",
    "summary": "U.S. Customs and Border Protection supervisor switched hardware from Department of Homeland Security computers with slower components and traded in stolen hardware to Newegg's Trade-In program for sto"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/we-tested-dlss-multi-frame-generation-on-rtx-40-series-gpus-new-mod-brings-rtx-50-series-exclusive-feature-to-older-cards-and-it-really-works",
    "domain": "AI 算力 / 半导体",
    "title": "We tested unofficial DLSS Multi Frame Generation support on RTX 40-series GPUs — new mod brings RTX 50-series exclusive feature to older cards, and it really works",
    "url": "https://www.tomshardware.com/pc-components/gpus/we-tested-dlss-multi-frame-generation-on-rtx-40-series-gpus-new-mod-brings-rtx-50-series-exclusive-feature-to-older-cards-and-it-really-works",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T14:08:19+00:00",
    "summary": "We tested DLSS Multi Frame Generation on RTX 40-series GPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/ikea-releases-new-skyrim-mod-that-adds-gloriously-mundane-kallax-shelving-unit-as-your-newest-companion-free-collab-provides-a-drab-flatpack-answer-to-your-loot-woes",
    "domain": "AI 算力 / 半导体",
    "title": "IKEA releases new Skyrim mod that adds gloriously mundane Kallax shelving unit as your newest companion — free collab provides a drab flatpack answer to your loot woes",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/ikea-releases-new-skyrim-mod-that-adds-gloriously-mundane-kallax-shelving-unit-as-your-newest-companion-free-collab-provides-a-drab-flatpack-answer-to-your-loot-woes",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T13:31:55+00:00",
    "summary": "IKEA has announced the Kallax Storageborn companion creation for players of The Elder Scrolls V: Skyrim Special Edition on PC or Xbox."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-september-12-2026-benchmarking-qwen-3-8-the-splintered-compute-economy-and-ai-breakthroughs",
    "domain": "AI 算力 / 半导体",
    "title": "This week on Tom's Hardware Premium: September 12, 2026 — Benchmarking Qwen 3.8, the splintered compute economy and AI breakthroughs",
    "url": "https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-september-12-2026-benchmarking-qwen-3-8-the-splintered-compute-economy-and-ai-breakthroughs",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T12:00:00+00:00",
    "summary": "This week on Tom's Hardware Premium, we benchmarked Qwen 3.8 on a slew of different hardware, ruminated on the state of modern computing after returning from IFA 2026, and broke down everything"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/iran-could-potentially-reverse-engineer-captured-u-s-underwater-drone-several-iranian-embassies-mock-us-over-capture-as-u-s-military-downplays-the-situation",
    "domain": "AI 算力 / 半导体",
    "title": "Iran could potentially reverse-engineer captured US underwater drone — several Iranian embassies mock US over capture, Navy claims lost Anduril vehicle was defective and unclassified",
    "url": "https://www.tomshardware.com/tech-industry/drones/iran-could-potentially-reverse-engineer-captured-u-s-underwater-drone-several-iranian-embassies-mock-us-over-capture-as-u-s-military-downplays-the-situation",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T11:30:00+00:00",
    "summary": "Iran may reverse-engineer a captured U.S. Navy Anduril Dive-LD underwater drone, as Tehran mocks the loss and Washington downplays its military value."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/kioxia-exceria-pro-g2-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "Kioxia Exceria Pro G2 2TB SSD Review — Speed built to last",
    "url": "https://www.tomshardware.com/pc-components/ssds/kioxia-exceria-pro-g2-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T11:05:00+00:00",
    "summary": "Kioxia’s Exceria Pro G2 pairs the SM2508 and BiCS8 TLC flash for fast, efficient PCIe 5.0 storage. It’s not the quickest PCIe 5.0 SSD, but it is a reliable Black SN8100 alternative."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/lucky-pc-scavenger-discovers-12-rtx-3070-gpus-from-the-crypto-mining-era-cards-survived-years-of-basement-storage-with-only-minor-signs-of-wear",
    "domain": "AI 算力 / 半导体",
    "title": "Lucky PC scavenger discovers 12 RTX 3070 GPUs from the crypto mining era — cards survived years of basement storage with only minor signs of wear",
    "url": "https://www.tomshardware.com/pc-components/gpus/lucky-pc-scavenger-discovers-12-rtx-3070-gpus-from-the-crypto-mining-era-cards-survived-years-of-basement-storage-with-only-minor-signs-of-wear",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T11:00:00+00:00",
    "summary": "What looked like a couple of forgotten mining rigs turned out to be a surprisingly valuable haul, with 12 RTX 3070 graphics cards potentially still ready for gaming duty."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/apples-a20-pro-shatters-geekbench-7-single-core-record-2nm-chip-beats-desktop-intel-core-i9-and-amd-ryzen-9-by-up-to-32-percent",
    "domain": "AI 算力 / 半导体",
    "title": "Apple's A20 Pro shatters Geekbench 7 single-core record — 2nm chip beats desktop Intel Core i9 and AMD Ryzen 9 by up to 32%",
    "url": "https://www.tomshardware.com/pc-components/cpus/apples-a20-pro-shatters-geekbench-7-single-core-record-2nm-chip-beats-desktop-intel-core-i9-and-amd-ryzen-9-by-up-to-32-percent",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T10:48:32+00:00",
    "summary": "Apple's A20 Pro smartphone SoC outperforms all smartphone processors by a wide margin and manages to leave behind latest laptop processors."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/consumer-rights-wiki-documents-at-least-44-instances-in-which-sony-says-you-own-your-games-project-is-direct-assault-on-sonys-claim-in-recent-ownership-lawsuit",
    "domain": "AI 算力 / 半导体",
    "title": "Wiki documents at least 44 instances in which Sony says you own your games as digital games ownership lawsuit progresses — project is direct assault on Sony's claim in recent ownership lawsuit",
    "url": "https://www.tomshardware.com/video-games/playstation/consumer-rights-wiki-documents-at-least-44-instances-in-which-sony-says-you-own-your-games-project-is-direct-assault-on-sonys-claim-in-recent-ownership-lawsuit",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T10:30:00+00:00",
    "summary": "The detailed sourcing directly attacks Sony's legal claim that a reasonable person wouldn't expect to own their digital purchases on the PlayStation Store."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/engineer-turns-simulated-fly-brain-into-a-crypto-day-trader-posts-downloadable-sim-to-github-166-700-virtual-neurons-read-candlestick-charts-for-dopamine-hits",
    "domain": "AI 算力 / 半导体",
    "title": "Engineer turns simulated fly brain into a crypto day trader, posts downloadable sim to GitHub — 166,700 virtual neurons read candlestick charts for dopamine hits",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/engineer-turns-simulated-fly-brain-into-a-crypto-day-trader-posts-downloadable-sim-to-github-166-700-virtual-neurons-read-candlestick-charts-for-dopamine-hits",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T10:00:00+00:00",
    "summary": "Coinbase engineer turns a fly brain into a crypto day trader — Stonkfly has 116,700 simulated neurons and hasn't lost its money yet"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/china-modified-nvidia-rtx-5090-with-massive-96gb-of-memory-appears-on-alibaba-for-less-than-usd4-000-3x-more-vram-at-65-percent-the-cost-of-the-original",
    "domain": "AI 算力 / 半导体",
    "title": "China-modified Nvidia RTX 5090 with massive 96GB of memory appears on Alibaba for less than $4,000 — 3x more VRAM at 65% the cost of the original",
    "url": "https://www.tomshardware.com/pc-components/gpus/china-modified-nvidia-rtx-5090-with-massive-96gb-of-memory-appears-on-alibaba-for-less-than-usd4-000-3x-more-vram-at-65-percent-the-cost-of-the-original",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T16:32:36+00:00",
    "summary": "An alleged Nvidia GeForce RTX 5090 96GB with 96GB of modded VRAM surfaces on Alibaba for $3888."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/supercomputers/sanctioned-chinese-supercomputer-maker-stripped-of-io500-benchmark-crown-intel-powered-aurora-retakes-the-lead-record-breaking-parastor-f9000-storage-system-doesnt-meet-reproducibility-requirements",
    "domain": "AI 算力 / 半导体",
    "title": "Sanctioned Chinese supercomputer maker stripped of IO500 benchmark crown, Intel-powered Aurora retakes the lead — record-breaking ParaStor F9000 storage system doesn't meet reproducibility requirement",
    "url": "https://www.tomshardware.com/tech-industry/supercomputers/sanctioned-chinese-supercomputer-maker-stripped-of-io500-benchmark-crown-intel-powered-aurora-retakes-the-lead-record-breaking-parastor-f9000-storage-system-doesnt-meet-reproducibility-requirements",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T16:26:12+00:00",
    "summary": "Sugon's record-breaking ParaStor F9000 storage systems have lost their IO500 Production crowns and have been moved to the Research list after failing to meet the benchmark's highest reproducibility re"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/save-20-percent-on-this-144-in-1-screwdriver-set-perfect-for-hobbyists-and-pc-builders-under-usd40-epic-starter-toolkit-ships-with-electric-and-precision-drivers-along-with-120-magnetic-bits-and-22-maintenance-tools",
    "domain": "AI 算力 / 半导体",
    "title": "Save 20% on this 144-in-1 screwdriver set, perfect for hobbyists and PC builders under $40 — epic starter toolkit ships with electric and precision drivers, along with 120 magnetic bits and 22 mainten",
    "url": "https://www.tomshardware.com/desktops/pc-building/save-20-percent-on-this-144-in-1-screwdriver-set-perfect-for-hobbyists-and-pc-builders-under-usd40-epic-starter-toolkit-ships-with-electric-and-precision-drivers-along-with-120-magnetic-bits-and-22-maintenance-tools",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T15:32:15+00:00",
    "summary": "This 144-in-1 repair toolkit from Strebito is on sale, with 120 bits and a number of other tools for less than $40."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/gamestop-is-reopening-recently-closed-stores-despite-massive-retail-cuts-select-locations-return-nationwide-starting-september-11",
    "domain": "AI 算力 / 半导体",
    "title": "GameStop is reopening recently closed stores despite massive retail cuts — select locations return nationwide starting September 11",
    "url": "https://www.tomshardware.com/tech-industry/gamestop-is-reopening-recently-closed-stores-despite-massive-retail-cuts-select-locations-return-nationwide-starting-september-11",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T12:50:35+00:00",
    "summary": "After shutting down hundreds of locations and dramatically shrinking its physical retail footprint, GameStop is bringing select stores back as its business continues to evolve beyond physical games."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/at-ifa-2026-computing-chased-the-high-and-low-ends-ai-and-budget-focused-machines-left-little-for-the-rest-of-us",
    "domain": "AI 算力 / 半导体",
    "title": "At IFA 2026, computing chased the high and low ends — AI and budget-focused machines left little for the rest of us",
    "url": "https://www.tomshardware.com/laptops/at-ifa-2026-computing-chased-the-high-and-low-ends-ai-and-budget-focused-machines-left-little-for-the-rest-of-us",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T12:44:08+00:00",
    "summary": "At IFA 2026, a bifurcated computing landscape widened as more companies chased Apple's MacBook Neo while also keeping one foot firmly planted in the AI space."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/neogeo-aes-console-remake-delayed-for-nearly-a-year-decision-driven-by-ram-shortage-and-unexpected-popularity",
    "domain": "AI 算力 / 半导体",
    "title": "Hardware-accurate NeoGeo AES+ delayed to late 2027 due to memory shortage — decision driven by surging demand and AI-driven RAM crunch",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/neogeo-aes-console-remake-delayed-for-nearly-a-year-decision-driven-by-ram-shortage-and-unexpected-popularity",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T11:30:00+00:00",
    "summary": "NeoGeo AES+ console remake delayed for nearly a year — decision driven by RAM shortage and unexpected popularity"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/thermalright-tr-kg750-750w-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "Thermalright TR-KG750 750W power supply review: HKC-built KG unit with a Thermalright badge for $91",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/thermalright-tr-kg750-750w-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T11:05:00+00:00",
    "summary": "Thermalright's HKC-built KG series brings ATX 3.1, a native 12V-2x6 connector and a five-year warranty at a low price point, with the compromises visible inside."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/external-ssds/hands-on-sharges-disk-pro-2-ultra",
    "domain": "AI 算力 / 半导体",
    "title": "Hands On: Sharge's Disk Pro 2 Ultra is a compact, magnetic DIY SSD dock with active cooling, 80W passthrough charging, and HDMI 2.1, supporting up to 8TB drives",
    "url": "https://www.tomshardware.com/pc-components/external-ssds/hands-on-sharges-disk-pro-2-ultra",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T11:05:00+00:00",
    "summary": "One of our favorite external SSDs gets an upgrade as a compact DIY hub with an M.2 slot, active cooling, USB ports, up to HDMI 2.1, and a removable cable."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/desktop-graphics-card-shipments-hit-four-year-high-of-12-5-million-despite-increasing-prices-nvidia-takes-90-percent-share-as-gamers-rush-to-beat-looming-price-spikes",
    "domain": "AI 算力 / 半导体",
    "title": "Desktop graphics card shipments hit four-year high of 12.5 million despite increasing prices — Nvidia takes 90% share as gamers rush to beat looming price spikes",
    "url": "https://www.tomshardware.com/pc-components/gpus/desktop-graphics-card-shipments-hit-four-year-high-of-12-5-million-despite-increasing-prices-nvidia-takes-90-percent-share-as-gamers-rush-to-beat-looming-price-spikes",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T11:00:00+00:00",
    "summary": "Shipments of desktop add-in-boards in Q2 were the highest since Q1 2022 despite rising prices and dropping sales of desktop PCs, according to new numbers from Jon Peddie Research."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/snag-a-huge-usd1-000-saving-on-this-rtx-5090-oled-gaming-laptop-from-hp-now-usd3-699-16-inch-hyperx-rig-delivers-1600p-gaming-with-ultra-fast-240hz-refresh-rate-coupled-with-32gb-ddr5-ram-and-a-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Snag a huge $1,000 saving on this RTX 5090 OLED gaming laptop from HP, now $3,699 — 16-inch HyperX rig delivers 1600p gaming with ultra-fast 240Hz refresh rate, coupled with 32GB DDR5 RAM and a 2TB SS",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/snag-a-huge-usd1-000-saving-on-this-rtx-5090-oled-gaming-laptop-from-hp-now-usd3-699-16-inch-hyperx-rig-delivers-1600p-gaming-with-ultra-fast-240hz-refresh-rate-coupled-with-32gb-ddr5-ram-and-a-2tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T10:50:59+00:00",
    "summary": "The HyperX Omen Max 16, featuring the powerful Nvidia GeForce RTX 5090 GPU, is down to $3,699.99 right now, saving you $1,000."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/windows-11-can-now-reinstall-itself-from-the-cloud-cloud-rebuild-revives-dead-systems-without-secondary-boot-media-wipes-broken-installation-and-downloads-a-fresh-copy-of-the-os",
    "domain": "AI 算力 / 半导体",
    "title": "Windows 11 can now reinstall itself from the cloud — Cloud Rebuild revives dead systems without secondary boot media, wipes broken installation and downloads a fresh copy of the OS",
    "url": "https://www.tomshardware.com/software/windows/windows-11-can-now-reinstall-itself-from-the-cloud-cloud-rebuild-revives-dead-systems-without-secondary-boot-media-wipes-broken-installation-and-downloads-a-fresh-copy-of-the-os",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T10:30:00+00:00",
    "summary": "Windows 11 users can soon recover from serious installation problems without relying on a USB drive or a custom recovery image."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-claude-thwarted-bioweapon-research-from-state-sponsored-actors-covert-accounts-used-u-s-proxies-to-attempt-to-engineer-deadlier-viruses-tried-to-evade-identification-and-regional-blocks",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic says Claude thwarted bioweapon research from state-sponsored actors — covert accounts used U.S. proxies to attempt to engineer deadlier viruses, tried to evade identification and regional bl",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-claude-thwarted-bioweapon-research-from-state-sponsored-actors-covert-accounts-used-u-s-proxies-to-attempt-to-engineer-deadlier-viruses-tried-to-evade-identification-and-regional-blocks",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T10:00:00+00:00",
    "summary": "Anthropic claims Claude refused instructions to potentially develop biological weapons — alleged state-linked accounts tried to evade identification and regional blocks"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/russian-plot-to-sabotage-undersea-cables-with-secret-weapon-foiled-by-nato-clandestine-op-uncovers-training-exercise-simulating-deployment-against-infrastructure-in-norway",
    "domain": "AI 算力 / 半导体",
    "title": "Russian plot to sabotage undersea cables with 'secret weapon' foiled by NATO — clandestine op uncovers training exercise simulating deployment against infrastructure in Norway",
    "url": "https://www.tomshardware.com/tech-industry/russian-plot-to-sabotage-undersea-cables-with-secret-weapon-foiled-by-nato-clandestine-op-uncovers-training-exercise-simulating-deployment-against-infrastructure-in-norway",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T09:26:43+00:00",
    "summary": "NATO foiled a Russian training exercise simulating the deployment of a secret weapon against Norwegian undersea cables."
  },
  {
    "id": "hn:49567357",
    "domain": "AI 算力 / 半导体",
    "title": "Georgi Gerganov on llama.cpp/ggml future after Nvidia acquisition of HuggingFace",
    "url": "https://twitter.com/ggerganov/status/2095897173376618881",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 76,
    "published_at": "2026-09-04T17:12:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49638022",
    "domain": "AI 算力 / 半导体",
    "title": "CUDA Rust: Two Tracks for Writing GPU Kernels",
    "url": "https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/",
    "source": "xiaoyu2006",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-09-10T03:25:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:49594189",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Jensen Huang says 'AGI has arrived' and congratulates OpenAI",
    "url": "https://www.businessinsider.com/nvidia-jensen-huang-agi-openai-astra-ai-2026-9",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-09-07T05:23:31+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/indian-researchers-look-beyond-gpus-to-neuromorphic-ai-hardware/",
    "domain": "AI 算力 / 半导体",
    "title": "Indian Researchers Look Beyond GPUs to Neuromorphic AI Hardware",
    "url": "https://www.eetimes.com/indian-researchers-look-beyond-gpus-to-neuromorphic-ai-hardware/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T07:31:15+00:00",
    "summary": "As AI workloads become more computationally demanding, Indian researchers argue that the next advance may come from rethinking computing architecture itself. The post Indian Researchers Look Beyond GP"
  },
  {
    "id": "rss:https://www.eetimes.com/from-ai-assisted-eda-to-ai-mediated-engineering/",
    "domain": "AI 算力 / 半导体",
    "title": "From AI-Assisted EDA to AI-Mediated Engineering",
    "url": "https://www.eetimes.com/from-ai-assisted-eda-to-ai-mediated-engineering/",
    "source": "Simon Davidmann",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T20:23:10+00:00",
    "summary": "What DAC 2026 revealed about agents, engines, trust—and why the industry should be optimistic. The post From AI-Assisted EDA to AI-Mediated Engineering appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/proven-actions-technologys-end-to-end-audio-architecture-tames-sounds-black-magic/",
    "domain": "AI 算力 / 半导体",
    "title": "Proven: Actions Technology’s End-to-End Audio Architecture Tames Sound’s “Black Magic”",
    "url": "https://www.eetimes.com/proven-actions-technologys-end-to-end-audio-architecture-tames-sounds-black-magic/",
    "source": "Franklin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T13:00:00+00:00",
    "summary": "Whether in the mass consumer market or the high-end professional audio segment, sound quality remains the defining factor that separates one product from another. Consumers’ appetite for better audio "
  },
  {
    "id": "rss:https://www.eetimes.com/adi-snaps-alif-semiconductor-to-push-ai-into-physical-systems/",
    "domain": "AI 算力 / 半导体",
    "title": "ADI Snaps Alif Semiconductor to Push AI into Physical Systems",
    "url": "https://www.eetimes.com/adi-snaps-alif-semiconductor-to-push-ai-into-physical-systems/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T11:00:00+00:00",
    "summary": "The $1.35 billion deal marks another edge AI leap of faith, combining analog sensing with low-power AI processors. The post ADI Snaps Alif Semiconductor to Push AI into Physical Systems appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/what-six-hours-on-the-runway-told-me-about-air-traffic-control-resilience-and-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "What Six Hours on the Runway Told Me About Air Traffic Control, Resilience, and AI",
    "url": "https://www.eetimes.com/what-six-hours-on-the-runway-told-me-about-air-traffic-control-resilience-and-ai/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T08:09:30+00:00",
    "summary": "A U.K. air traffic control glitch stranded flights for hours, prompting reflections on resilience, redundancy, legacy systems, and AI. The post What Six Hours on the Runway Told Me About Air Traffic C"
  },
  {
    "id": "rss:https://www.eetimes.com/cincon-high-performance-power-modules-for-edge-ai-ipcs/",
    "domain": "AI 算力 / 半导体",
    "title": "Cincon High-Performance Power Modules for Edge AI & IPCs",
    "url": "https://www.eetimes.com/cincon-high-performance-power-modules-for-edge-ai-ipcs/",
    "source": "Cincon Elctronics Co., Ltd.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T08:00:00+00:00",
    "summary": "As AI moves to the edge, IPCs demand compact, rugged power. Cincon offers baseplate-cooled DC-DC &#038; AC-DC solutions for fanless, harsh AIoT environments. The post Cincon High-Performance Power Mod"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/nintendo-of-america-puts-tariff-refunds-towards-customer-appreciation-sale-but-no-refunds-to-switch-2-buyers-offers-30-percent-off-games-and-accessories-from-september-13-to-26",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo of America puts tariff refunds towards 'customer appreciation' sale, but no refunds to Switch 2 buyers — offers 30% off games and accessories from September 13 to 26",
    "url": "https://www.tomshardware.com/video-games/nintendo/nintendo-of-america-puts-tariff-refunds-towards-customer-appreciation-sale-but-no-refunds-to-switch-2-buyers-offers-30-percent-off-games-and-accessories-from-september-13-to-26",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T19:35:00+00:00",
    "summary": "Nintendo is offering a 30% sale with its tariff refunds, as opposed as returning the money directly to customers."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/asus-routers-gain-fccs-conditional-approval-for-sale-in-the-us-as-tp-link-remains-locked-out-asuss-wi-fi-8-ambitions-remain-intact",
    "domain": "AI 算力 / 半导体",
    "title": "Asus routers gain FCC's 'Conditional Approval' for sale in the US as TP-Link remains locked out — Asus's Wi-Fi 8 ambitions remain intact",
    "url": "https://www.tomshardware.com/networking/routers/asus-routers-gain-fccs-conditional-approval-for-sale-in-the-us-as-tp-link-remains-locked-out-asuss-wi-fi-8-ambitions-remain-intact",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T19:13:21+00:00",
    "summary": "Asus gets conditional approval from the FCC for US router sales, while rival TP-Link continues to wait"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-releases-new-ryzen-5-5500f-and-ryzen-5-7500-to-save-budget-pc-building-new-budget-zen-3-and-zen-4-cpus-to-soften-the-blow-from-high-ram-prices",
    "domain": "AI 算力 / 半导体",
    "title": "AMD releases new Ryzen 5 5500F and Ryzen 5 7500 for budget PC builders — new budget Zen 3 and Zen 4 CPUs soften the blow from high RAM prices",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-releases-new-ryzen-5-5500f-and-ryzen-5-7500-to-save-budget-pc-building-new-budget-zen-3-and-zen-4-cpus-to-soften-the-blow-from-high-ram-prices",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T17:54:53+00:00",
    "summary": "AMD has officially launched the Ryzen 5 5500F and Ryzen 5 7500 processors with six Zen 3 and Zen 4 cores, respectively."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/apples-new-a20-pro-smartphone-chip-around-25-percent-faster-than-its-predecessor-in-leaked-benchmark-the-2nm-cpu-in-the-iphone-duo-and-18-pro-hits-nearly-5-ghz-clocks",
    "domain": "AI 算力 / 半导体",
    "title": "Apple’s new A20 Pro smartphone chip around 25% faster than its predecessor in leaked benchmark — the 2nm CPU in the iPhone Duo and 18 Pro hits nearly 5 GHz clocks",
    "url": "https://www.tomshardware.com/pc-components/cpus/apples-new-a20-pro-smartphone-chip-around-25-percent-faster-than-its-predecessor-in-leaked-benchmark-the-2nm-cpu-in-the-iphone-duo-and-18-pro-hits-nearly-5-ghz-clocks",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T16:04:10+00:00",
    "summary": "The first Apple A20 Geekbench 6 benchmark results are starting to pop up online and the single-core score is very impressive."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/this-usd399-elegoo-centauri-carbon-2-combo-deal-with-usd1-filament-is-the-perfect-3d-printer-deal-for-beginners-flash-sale-discount-nets-you-a-core-xy-printer-with-four-color-system-and-auto-bed-leveling",
    "domain": "AI 算力 / 半导体",
    "title": "This $399 Elegoo Centauri Carbon 2 Combo with $1 filament is the perfect 3D printer deal for beginners — flash sale discount nets you a Core XY printer with four-color system and auto bed leveling",
    "url": "https://www.tomshardware.com/3d-printing/this-usd399-elegoo-centauri-carbon-2-combo-deal-with-usd1-filament-is-the-perfect-3d-printer-deal-for-beginners-flash-sale-discount-nets-you-a-core-xy-printer-with-four-color-system-and-auto-bed-leveling",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T15:00:00+00:00",
    "summary": "Grab this budget-friendly 3D printer from Elegoo, the Centauri Carbon 2 Combo, for $399, and pay just $1 extra for 1KG of filament."
  },
  {
    "id": "hn:49557813",
    "domain": "AI 算力 / 半导体",
    "title": "Tell HN: NVIDIA's Acquisition of HuggingFace was for $HuggingFace",
    "url": "https://news.ycombinator.com/item?id=49557813",
    "source": "MontagFTB",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-09-03T22:08:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:49552375",
    "domain": "AI 算力 / 半导体",
    "title": "Texas Data Center Map: See where data centers are operating or planned",
    "url": "https://www.kxan.com/news/texas/texas-data-center-tracker-see-where-600-projects-are-operating-or-planned-across-state-in-interactive-map/",
    "source": "simonpure",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-09-03T16:10:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49552616",
    "domain": "AI 算力 / 半导体",
    "title": "Launch HN: Mireye (YC S26) – Infrastructure for Physical World AI Agents",
    "url": "https://news.ycombinator.com/item?id=49552616",
    "source": "anshchokshi",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-09-03T16:24:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49497235",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's AI advantage is moving beyond the GPU",
    "url": "https://techcrunch.com/2026/08/29/nvidias-ai-advantage-is-moving-beyond-the-gpu/",
    "source": "01-_-",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-30T09:57:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:49537553",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Flash and 3.8 Flash Cyber",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/",
    "source": "bratao",
    "platform": "hackernews",
    "points": 1160,
    "published_at": "2026-09-02T15:12:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611251",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas: a high-resolution map of human DNA",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/",
    "source": "utiiiD",
    "platform": "hackernews",
    "points": 604,
    "published_at": "2026-09-08T14:55:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49552299",
    "domain": "大厂 AI 动态",
    "title": "WeatherNext 3",
    "url": "https://deepmind.google/science/weathernext/",
    "source": "matthieu_bl",
    "platform": "hackernews",
    "points": 406,
    "published_at": "2026-09-03T16:06:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49331423",
    "domain": "大厂 AI 动态",
    "title": "AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira",
    "url": "https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug",
    "source": "galnagli",
    "platform": "hackernews",
    "points": 424,
    "published_at": "2026-08-17T14:18:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49468818",
    "domain": "大厂 AI 动态",
    "title": "Gemini-3.5-Transcribe",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/",
    "source": "k9294",
    "platform": "hackernews",
    "points": 363,
    "published_at": "2026-08-27T18:03:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:49467922",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni 1.1 Flash",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/",
    "source": "saretup",
    "platform": "hackernews",
    "points": 297,
    "published_at": "2026-08-27T17:06:32+00:00",
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
    "id": "hn:49383326",
    "domain": "大厂 AI 动态",
    "title": "Codex on AWS bedrock bug causing 10x charges",
    "url": "https://github.com/openai/codex/issues/37674",
    "source": "TheP1000",
    "platform": "hackernews",
    "points": 148,
    "published_at": "2026-08-21T03:17:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49610641",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas predictive map of every DNA letter change in the human genome",
    "url": "https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/",
    "source": "fady0",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-09-08T14:14:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49653699",
    "domain": "大厂 AI 动态",
    "title": "The Gemini app is now available for Windows",
    "url": "https://blog.google/innovation-and-ai/products/gemini-app/gemini-app-now-on-windows/",
    "source": "quysala12",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-09-11T04:52:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:49652122",
    "domain": "大厂 AI 动态",
    "title": "Setting up OpenCode with Ollama and sbx on Mac",
    "url": "https://tensorsandtokens.com/posts/opencode-ollama/",
    "source": "etoxin",
    "platform": "hackernews",
    "points": 31,
    "published_at": "2026-09-11T00:45:26+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/994383/openais-rogue-ai-rubygems-hack",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s rogue AI tried to hack another company in May",
    "url": "https://www.theverge.com/ai-artificial-intelligence/994383/openais-rogue-ai-rubygems-hack",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T21:41:36+00:00",
    "summary": "In May, hundreds of malicious and spam packages were uploaded to RubyGems, causing a serious disruption for the host. Now independent researchers have said that a swarm of OpenAI agents were responsib"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/994384/sam-altman-no-openai-ipo-ill-advised",
    "domain": "大厂 AI 动态",
    "title": "Sam Altman says OpenAI going public in 2026 would be ‘ill-advised’",
    "url": "https://www.theverge.com/ai-artificial-intelligence/994384/sam-altman-no-openai-ipo-ill-advised",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T21:16:28+00:00",
    "summary": "OpenAI CEO Sam Altman confirmed that there would be no OpenAI IPO in 2026 during an interview with Fortune. Over the course of 45 minutes, Altman discussed a variety of subjects including the Hugging "
  },
  {
    "id": "rss:https://www.theverge.com/games/994371/starcraft-returns-in-2030-as-an-open-world-shooter",
    "domain": "大厂 AI 动态",
    "title": "StarCraft returns in 2030 as an open-world shooter",
    "url": "https://www.theverge.com/games/994371/starcraft-returns-in-2030-as-an-open-world-shooter",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T20:08:09+00:00",
    "summary": "Blizzard originally tried to bring the StarCraft universe to the world of 3D shooters way back in 2002 with StarCraft: Ghost. It sat in development hell for years until Blizzard president Mike Morhaim"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/994340/sylvan-esso-ow-infinity-interview-music",
    "domain": "大厂 AI 动态",
    "title": "Sylvan Esso think you should splurge on good-quality yogurt",
    "url": "https://www.theverge.com/entertainment/994340/sylvan-esso-ow-infinity-interview-music",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T16:35:00+00:00",
    "summary": "Amelia Meath and Nick Sanborn, better known as Sylvan Esso, have been bringing their low-key electro-pop to the masses since 2014, bursting onto the scene with their self-titled debut album and the si"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/994337/anthropic-ceo-slow-down-ai-development",
    "domain": "大厂 AI 动态",
    "title": "Anthropic CEO says it’s time to pump the brakes on AI",
    "url": "https://www.theverge.com/ai-artificial-intelligence/994337/anthropic-ceo-slow-down-ai-development",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T16:23:40+00:00",
    "summary": "Anthropic CEO Dario Amodei says the time has come to slow down AI development and will give third-party evaluators like METR access to its models to help ensure its \"adherence to safety practices and "
  },
  {
    "id": "rss:https://www.theverge.com/tech/994333/lg-responds-to-tv-spying-allegations",
    "domain": "大厂 AI 动态",
    "title": "LG responds to TV spying allegations",
    "url": "https://www.theverge.com/tech/994333/lg-responds-to-tv-spying-allegations",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T15:19:44+00:00",
    "summary": "Earlier this week, Gamers Nexus, Level1Techs, and independent security researchers detailed some alarming findings about how LG's TVs are logging and uploading data on its users. Now the company is pu"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/994112/ai-data-center-pollution-health-epa",
    "domain": "大厂 AI 动态",
    "title": "Trump is giving data centers a pass to pollute",
    "url": "https://www.theverge.com/ai-artificial-intelligence/994112/ai-data-center-pollution-health-epa",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T14:41:27+00:00",
    "summary": "President Donald Trump is weakening environmental regulations in the name of speeding up the construction of AI data centers, raising health risks for Americans, a cadre of former EPA officials said t"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/994314/tiff-2026-wildwood-stuffed-julian",
    "domain": "大厂 AI 动态",
    "title": "Laika’s stop-motion fantasy Wildwood looks so smooth",
    "url": "https://www.theverge.com/entertainment/994314/tiff-2026-wildwood-stuffed-julian",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T13:00:00+00:00",
    "summary": "Due to a scheduling mishap, I was only able to check out two movies on my second day at the Toronto International Film Festival - but I did manage to get an early look at and some fascinating details "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/988337/iphone-18-pro-max-preorder-buy",
    "domain": "大厂 AI 动态",
    "title": "Where to preorder the iPhone 18 Pro and Pro Max",
    "url": "https://www.theverge.com/gadgets/988337/iphone-18-pro-max-preorder-buy",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T12:00:00+00:00",
    "summary": "The iPhone 18 Pro and 18 Pro Max are almost here. Announced at Apple's September 2026 \"Sunrise and shine\" event alongside the iPhone Duo and other new gear, the two upgraded phones feature the faster "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/994255/openai-millennium-prize-problem-tristan-buckmaster-competition",
    "domain": "大厂 AI 动态",
    "title": "OpenAI just wants to win",
    "url": "https://www.theverge.com/ai-artificial-intelligence/994255/openai-millennium-prize-problem-tristan-buckmaster-competition",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T11:00:00+00:00",
    "summary": "OpenAI has spent the last few years planting flags across the increasingly difficult terrain in mathematics. This week, it claimed one of its biggest prizes yet: a solution to a legendary Millennium P"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/12/automattic-confirms-mullenweg-has-returned-as-ceo-after-attempted-ouster-by-board/",
    "domain": "大厂 AI 动态",
    "title": "Automattic confirms Mullenweg has returned as CEO after attempted ouster by board",
    "url": "https://techcrunch.com/2026/09/12/automattic-confirms-mullenweg-has-returned-as-ceo-after-attempted-ouster-by-board/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T23:25:38+00:00",
    "summary": "Automattic says Mullenweg is back as \"chairman and CEO of Automattic, with full support of the board.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/12/openais-sam-altman-says-it-would-be-ill-advised-to-go-public-in-2026/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s Sam Altman says it would be ‘ill-advised’ to go public in 2026",
    "url": "https://techcrunch.com/2026/09/12/openais-sam-altman-says-it-would-be-ill-advised-to-go-public-in-2026/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T20:19:16+00:00",
    "summary": "While OpenAI has filed confidentially for an IPO, the company will not be going public this year, according to CEO Sam Altman."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/12/anthropic-ceo-outlines-plan-to-pace-the-frontier/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic CEO outlines plan to slow AI development",
    "url": "https://techcrunch.com/2026/09/12/anthropic-ceo-outlines-plan-to-pace-the-frontier/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T19:34:44+00:00",
    "summary": "Anthropic's Dario Amodei and OpenAI's Sam Altman seem to agree that it's time to \"pace the frontier.\" What would that actually look like?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/12/tesla-says-it-will-finally-unveil-the-second-generation-roadster-on-october-1/",
    "domain": "大厂 AI 动态",
    "title": "Tesla says it will finally unveil the second generation Roadster on October 1",
    "url": "https://techcrunch.com/2026/09/12/tesla-says-it-will-finally-unveil-the-second-generation-roadster-on-october-1/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T19:21:19+00:00",
    "summary": "Tesla’s halo sports car was first announced in November 2017."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/12/revolut-confirms-customer-data-breach-through-fake-government-requests/",
    "domain": "大厂 AI 动态",
    "title": "Revolut confirms customer data breach through fake government requests",
    "url": "https://techcrunch.com/2026/09/12/revolut-confirms-customer-data-breach-through-fake-government-requests/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T14:40:00+00:00",
    "summary": "Revolut said it notified affected customers and alerted the relevant government agency, law enforcement, and financial regulators."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/mecka-ai-nears-500m-valuation-in-sequoia-led-deal-amid-rush-for-robot-training-data/",
    "domain": "大厂 AI 动态",
    "title": "Mecka AI nears $500M valuation in Sequoia-led deal amid rush for robot training data",
    "url": "https://techcrunch.com/2026/09/11/mecka-ai-nears-500m-valuation-in-sequoia-led-deal-amid-rush-for-robot-training-data/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T22:58:17+00:00",
    "summary": "The round for the two-year-old startup is coming together months after Mecka announced its Series A."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/khosla-ventures-is-opening-a-new-york-office-this-fall-its-first-outpost-outside-sand-hill-road/",
    "domain": "大厂 AI 动态",
    "title": "Khosla Ventures is opening a New York office this fall — its first outpost outside Sand Hill Road",
    "url": "https://techcrunch.com/2026/09/11/khosla-ventures-is-opening-a-new-york-office-this-fall-its-first-outpost-outside-sand-hill-road/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T21:19:05+00:00",
    "summary": "\"It's actually allegedly being built out now,\" said Rabois, who has clearly dealt with a missed construction timeline or two."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/y-combinators-garry-tan-wants-u-s-open-weight-ai-labs-to-distill-frontier-models-too/",
    "domain": "大厂 AI 动态",
    "title": "Y Combinator’s Garry Tan wants US open-weight AI labs to ‘distill’ frontier models, too",
    "url": "https://techcrunch.com/2026/09/11/y-combinators-garry-tan-wants-u-s-open-weight-ai-labs-to-distill-frontier-models-too/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T20:59:47+00:00",
    "summary": "Tan wants smaller, American open-weight AI labs to use the same kind of training techniques on American frontier AI labs, giving the U.S. a more robust set of open-weight options that aren’t Chinese."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/openais-feud-with-mathematicians-is-only-escalating/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI’s feud with mathematicians is only escalating",
    "url": "https://techcrunch.com/2026/09/11/openais-feud-with-mathematicians-is-only-escalating/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T20:57:36+00:00",
    "summary": "Twenty-five leading mathematicians signed an open letter arguing that AI labs are threatening their intellectual work."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/one-week-left-to-book-your-exhibit-table-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "One week left to book your exhibit table at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/11/one-week-left-to-book-your-exhibit-table-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T20:33:18+00:00",
    "summary": "Only one week left to secure your exhibit table. Tables are limited and can sell out before the September 18 deadline."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/final-final-final-call-for-techcrunch-disrupt-2026-side-events/",
    "domain": "大厂 AI 动态",
    "title": "Final, final, final call for TechCrunch Disrupt 2026 Side Events",
    "url": "https://techcrunch.com/2026/09/11/final-final-final-call-for-techcrunch-disrupt-2026-side-events/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T20:30:17+00:00",
    "summary": "The absolute last chance to apply to host an official Side Event during TechCrunch Disrupt 2026 is tonight, September 11, at 11:59 p.m. PT."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/kimi-maker-moonshot-ai-targets-2-billion-in-annual-revenue/",
    "domain": "大厂 AI 动态",
    "title": "Kimi-maker Moonshot AI targets $2B in annual revenue",
    "url": "https://techcrunch.com/2026/09/11/kimi-maker-moonshot-ai-targets-2-billion-in-annual-revenue/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T19:35:54+00:00",
    "summary": "While K3's usage figures have declined slightly in recent months, OpenRouter data currently shows as many as 300 billion tokens being generated each day by K3 models on the system."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/roblox-is-making-it-easier-to-build-games-with-ai-and-play-them-outside-roblox/",
    "domain": "大厂 AI 动态",
    "title": "Roblox is making it easier to build games with AI — and play them outside Roblox",
    "url": "https://techcrunch.com/2026/09/11/roblox-is-making-it-easier-to-build-games-with-ai-and-play-them-outside-roblox/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T19:00:00+00:00",
    "summary": "At its annual Roblox Developer Conference (RDC), the company announced several new features, including new game-creation tools, expanded NPC capabilities, and the ability to make games available acros"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/central-eurasia-names-its-2026-road-to-battlefield-winners-cerberus-weglobal-ai-and-looq/",
    "domain": "大厂 AI 动态",
    "title": "Central Eurasia names its 2026 Road to Battlefield winners: Cerberus, WeGlobal AI, and LOOQ",
    "url": "https://techcrunch.com/2026/09/11/central-eurasia-names-its-2026-road-to-battlefield-winners-cerberus-weglobal-ai-and-looq/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T18:58:01+00:00",
    "summary": "Cerberus, WeGlobal AI, and LOOQ took the top three spots at the regional final of Road to TechCrunch Startup Battlefield 2026 and will represent Central Eurasia in the Startup Battlefield 200 at TechC"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/nscale-adds-former-openai-exec-fidji-simo-to-its-board-ahead-of-potential-ipo/",
    "domain": "大厂 AI 动态",
    "title": "Nscale adds former OpenAI exec Fidji Simo to its board ahead of potential IPO",
    "url": "https://techcrunch.com/2026/09/11/nscale-adds-former-openai-exec-fidji-simo-to-its-board-ahead-of-potential-ipo/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T16:46:25+00:00",
    "summary": "The No. 2 exec at OpenAI also led Instacart through its IPO in 2023."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/matt-mullenweg-tells-automattic-staff-in-slack-hes-back-in-control-after-ceo-ouster/",
    "domain": "大厂 AI 动态",
    "title": "Matt Mullenweg tells (trolls?) Automattic staff, saying he’s back in control after CEO ouster",
    "url": "https://techcrunch.com/2026/09/11/matt-mullenweg-tells-automattic-staff-in-slack-hes-back-in-control-after-ceo-ouster/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T15:19:00+00:00",
    "summary": "In a Slack message seen by TechCrunch, Matt Mullenweg told Automattic employees he’s back in control of the company, days after its board put him on leave. Automattic has not yet confirmed the apparen"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/11/scammers-target-hundreds-of-thousands-of-crypto-owners-after-trezor-confirms-data-breach-of-email-provider/",
    "domain": "大厂 AI 动态",
    "title": "Scammers target hundreds of thousands of crypto owners after Trezor confirms data breach of email provider",
    "url": "https://techcrunch.com/2026/09/11/scammers-target-hundreds-of-thousands-of-crypto-owners-after-trezor-confirms-data-breach-of-email-provider/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T13:32:54+00:00",
    "summary": "This is the second data breach affecting a company that hardware crypto wallet maker Trezor relies on."
  },
  {
    "id": "rss:https://stratechery.com/2026/duo-threats/",
    "domain": "大厂 AI 动态",
    "title": "2026.37: Duo Threats",
    "url": "https://stratechery.com/2026/duo-threats/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of September 7, 2026, including the arrival of the Duo, AI that benefits humanity, and closing the book on a catastrophe."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/09/i-spent-4000-on-a-robot-dog-from-china/",
    "domain": "大厂 AI 动态",
    "title": "I spent $4,000 on a robot dog from China",
    "url": "https://arstechnica.com/gadgets/2026/09/i-spent-4000-on-a-robot-dog-from-china/",
    "source": "Timothy B. Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T11:00:53+00:00",
    "summary": "Unitree might be the world’s most important robotics company."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/09/some-satellite-companies-still-have-an-appetite-for-boutique-launch-services/",
    "domain": "大厂 AI 动态",
    "title": "Some satellite companies still have an appetite for boutique launch services",
    "url": "https://arstechnica.com/space/2026/09/some-satellite-companies-still-have-an-appetite-for-boutique-launch-services/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T23:34:45+00:00",
    "summary": "\"Dedicated launch is pretty essential for us for most of our missions.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/09/random-rewards-enrich-classic-game-theory-contests/",
    "domain": "大厂 AI 动态",
    "title": "Random rewards enrich classic game-theory insights",
    "url": "https://arstechnica.com/science/2026/09/random-rewards-enrich-classic-game-theory-contests/",
    "source": "Chris Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T21:41:16+00:00",
    "summary": "Simple games gain rich strategies in the face of noise."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/bouncy-castle-launches-horrifying-mrsa-outbreak-striking-48-kids-in-ireland/",
    "domain": "大厂 AI 动态",
    "title": "Bouncy castle launches horrifying MRSA outbreak, striking 48 kids in Ireland",
    "url": "https://arstechnica.com/health/2026/09/bouncy-castle-launches-horrifying-mrsa-outbreak-striking-48-kids-in-ireland/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T21:14:26+00:00",
    "summary": "The strain lurking in the inflatable structure was hypervirulent."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/09/court-rejects-governments-energy-emergency-that-kept-coal-plant-open/",
    "domain": "大厂 AI 动态",
    "title": "Trump's forced coal plant extensions thrown out by judge",
    "url": "https://arstechnica.com/science/2026/09/court-rejects-governments-energy-emergency-that-kept-coal-plant-open/",
    "source": "John Timmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T20:32:59+00:00",
    "summary": "The Department of Energy declared an \"emergency\" when none existed."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/chatgpt-using-lawyer-punished-for-citing-fake-testimony-from-made-up-witnesses/",
    "domain": "大厂 AI 动态",
    "title": "ChatGPT-using lawyer punished for citing fake testimony from made-up witnesses",
    "url": "https://arstechnica.com/tech-policy/2026/09/chatgpt-using-lawyer-punished-for-citing-fake-testimony-from-made-up-witnesses/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T19:34:09+00:00",
    "summary": "\"I didn't know that AI could hallucinate facts,\" New Mexico defense lawyer says."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/09/scientists-unlock-secrets-of-ancient-egyptian-materials-with-proteomics/",
    "domain": "大厂 AI 动态",
    "title": "Scientists unlock secrets of ancient Egyptian materials with proteomics",
    "url": "https://arstechnica.com/science/2026/09/scientists-unlock-secrets-of-ancient-egyptian-materials-with-proteomics/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T18:49:39+00:00",
    "summary": "Analysis revealed seed proteins from sesame and moringa, which held religious and symbolic significance."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/09/oracle-promises-2-gw-of-renewables-to-match-stargate-data-center-emissions/",
    "domain": "大厂 AI 动态",
    "title": "Oracle tries to appease Stargate data center opponents with renewables push",
    "url": "https://arstechnica.com/gadgets/2026/09/oracle-promises-2-gw-of-renewables-to-match-stargate-data-center-emissions/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T18:22:22+00:00",
    "summary": "Renewables pledge won’t change the Oracle and OpenAI data center’s use of gas."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/09/nasa-moving-at-warp-speed-to-set-up-us-space-academy/",
    "domain": "大厂 AI 动态",
    "title": "NASA moving at warp speed to set up US Space Academy",
    "url": "https://arstechnica.com/space/2026/09/nasa-moving-at-warp-speed-to-set-up-us-space-academy/",
    "source": "Eric Berger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T16:20:43+00:00",
    "summary": "NASA asks US states to show them the money."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/09/claude-users-found-ways-around-safeguards-for-bioweapons-research/",
    "domain": "大厂 AI 动态",
    "title": "Claude users found ways around safeguards for bioweapons research",
    "url": "https://arstechnica.com/ai/2026/09/claude-users-found-ways-around-safeguards-for-bioweapons-research/",
    "source": "Zehra Munir, Financial Times",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T13:02:35+00:00",
    "summary": "Some dangerous biology looks much like legitimate research, complicating AI safeguards."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/09/clickfix-attacks-infecting-pcs-and-macs-are-going-viral/",
    "domain": "大厂 AI 动态",
    "title": "ClickFix attacks infecting PCs and Macs are going viral",
    "url": "https://arstechnica.com/security/2026/09/clickfix-attacks-infecting-pcs-and-macs-are-going-viral/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T11:30:58+00:00",
    "summary": "Simplicity—combined with the difficulty of getting stuff done—makes ClickFix ideal."
  },
  {
    "id": "hn:49599992",
    "domain": "股票",
    "title": "Stockfish 19",
    "url": "https://stockfishchess.org/blog/2026/stockfish-19/",
    "source": "atiedebee",
    "platform": "hackernews",
    "points": 277,
    "published_at": "2026-09-07T16:17:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49619848",
    "domain": "股票",
    "title": "Apple iPod Engraver (2019)",
    "url": "https://dunstanorchard.com/apple-ipod-engraver/",
    "source": "NaOH",
    "platform": "hackernews",
    "points": 198,
    "published_at": "2026-09-09T01:57:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611240",
    "domain": "股票",
    "title": "iPod Classic 6G in QEMU",
    "url": "https://www.reddit.com/r/emulation/s/VL4Au2HGxq",
    "source": "dmonterocrespo",
    "platform": "hackernews",
    "points": 158,
    "published_at": "2026-09-08T14:54:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49672197",
    "domain": "股票",
    "title": "Larry Ellison to sell up to $7.5B worth of Oracle stock",
    "url": "https://www.ft.com/content/25b1abb0-790f-4315-9b0c-530d959a086f",
    "source": "potatobox",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-12T13:37:21+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3781532",
    "domain": "股票",
    "title": "虽然加息“没用” 但美联储别无选择",
    "url": "https://wallstreetcn.com/premium/articles/3781532?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T08:02:40+00:00",
    "summary": "通胀的病根在战争和关税，加息治不了——但不加，更危险。"
  },
  {
    "id": "wscn:3781648",
    "domain": "股票",
    "title": "中信建投：加息“靴子”将落地，A股或迎反攻行情",
    "url": "https://wallstreetcn.com/articles/3781648",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T07:47:55+00:00",
    "summary": "对于当前的A股和美股来说，加息预期的分歧让投资者感到无所适从，而加息“靴子落地”则能够凝聚共识，开启新一轮行情。本周五A股在四大利空冲击下实现V型反弹，结合未来美联储加息靴子将落地，A股有望迎来变盘时点，或将开启反攻行情。"
  },
  {
    "id": "wscn:3781561",
    "domain": "股票",
    "title": "半年狂赚3284亿，保险业为什么还不敢松口气？",
    "url": "https://wallstreetcn.com/premium/articles/3781561?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T06:10:55+00:00",
    "summary": "2026年上半年，主要上市险企合计归母净利润达到3284亿元，同比增长约78%，但高增长背后既有资本市场回暖，也有寿险价值率、渠道效率和财险承保盈利改善。\n真正值得关注的是，负债成本下降与资产收益率下行之间的赛跑是否开始出现变化；而Q3的高基数、市场波动和700亿元资本补充，将成为下一阶段的重要检验。"
  },
  {
    "id": "wscn:3781644",
    "domain": "股票",
    "title": "也门局势骤然升温！胡塞武装与沙特互相袭击，伊朗：我们与沙特“并不处于战争状态”",
    "url": "https://wallstreetcn.com/articles/3781644",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T06:06:46+00:00",
    "summary": "胡塞武装接连夺控曼德海峡咽喉要地，沙特与胡塞互袭致也门局势骤然升级，美国拒直接出兵转向接触斡旋，伊朗称无意对沙开战，但此前曾表示难以约束胡塞武装，红海战略地缘风险陡增。当前，全球能源贸易面临着事实上的双海峡——曼德海峡、霍尔木兹海峡锁喉的困难局面。"
  },
  {
    "id": "wscn:3781642",
    "domain": "股票",
    "title": "所有目光聚焦沃什，下周“央行超级周”迎来G7加息潮？",
    "url": "https://wallstreetcn.com/articles/3781642",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T05:35:51+00:00",
    "summary": "在通胀升温、地缘冲突及油价破百交织下，G7央行迎来关键议息周。受核心通胀超预期推动，美联储预计将迎来三年来的首次加息；日本央行料将加息至1.25%，创30年新高；英欧及加拿大央行鹰派立场亦同步强化，全球货币政策正迎来集体紧缩的重大转折。"
  },
  {
    "id": "wscn:3781643",
    "domain": "股票",
    "title": "三巨头支持“放缓”、OpenAI推迟IPO！社区热议：“AI交易”周一遭暴击？",
    "url": "https://wallstreetcn.com/articles/3781643",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T04:17:32+00:00",
    "summary": "Anthropic、OpenAI与马斯克罕见达成“放缓AI开发”共识。HyperliquidX平台上，OpenAI和Anthropic相关资产跌幅分别达到7%和2.8%，更有人高呼“AI股票周一早盘将下跌10%以上。”但也有分析认为，此举或是巨头为缓解基础设施烧钱压力、削减资本支出所做的“预期管理”。"
  },
  {
    "id": "wscn:3781555",
    "domain": "股票",
    "title": "付鹏：能源市场成品油的紧张终于传导到了上游，警惕上下游左脚踩右脚【付鹏说4】",
    "url": "https://wallstreetcn.com/premium/articles/3781555?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T03:56:00+00:00",
    "summary": "美国炼厂开工率已达98%，柴油价格创历史新高，出口创新高、库存降至极低水平，表明下游已紧张到极限。随着检修季和冬季临近，炼厂一旦检修或出现故障，柴油价格将急剧上涨并反向拉动原油；叠加交易员已将地缘政治风险溢价转移至下游，上下游可能形成相互推升的“左脚踩右脚”循环。"
  },
  {
    "id": "wscn:3781641",
    "domain": "股票",
    "title": "美债能反弹，但还不能抄底",
    "url": "https://wallstreetcn.com/articles/3781641",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T03:47:57+00:00",
    "summary": "油价因中东冲突持续高企、8月非农大超预期、AI资本支出持续扩张，三重压力推动市场开始定价未来6至9个月连续加息。若下周美联储按兵不动，短端收益率或迎来短期修复行情——但这不是趋势反转，只是窗口。"
  },
  {
    "id": "wscn:3781552",
    "domain": "股票",
    "title": "SEMICON TW2026：AI基建产业链的瓶颈与焦虑，在哪里？",
    "url": "https://wallstreetcn.com/premium/articles/3781552?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T03:40:24+00:00",
    "summary": "当资本开支不再是约束，AI 基建的四道硬墙成为真正的咽喉。"
  },
  {
    "id": "wscn:3781640",
    "domain": "股票",
    "title": "美联储会“连续加息”？1980年代末“紧缩周期”会重演吗？",
    "url": "https://wallstreetcn.com/articles/3781640",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T03:02:08+00:00",
    "summary": "花旗报告指出，当前宏观环境与1988-1989年紧缩周期高度相似，当时经济维持韧性、通胀压力逐步积累，随后经济活动放缓，政策才转向宽松。在当年的紧缩周期中，美联储连续加息了16次。"
  },
  {
    "id": "wscn:3781639",
    "domain": "股票",
    "title": "死敌罕见联手！马斯克、Aaltman支持Dario Amodei“全球放缓AI”呼吁",
    "url": "https://wallstreetcn.com/articles/3781639",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T02:05:57+00:00",
    "summary": "Anthropic Amodei发出“全球放缓AI”的呼吁，宿敌马斯克与Altman竟双双公开站台背书。三大巨头一致同意向第三方开放“员工级”评估权限、推行协调降速；Altman更直接宣布OpenAI今年不会IPO。一个研究员的愤然辞职，一群失控AI的集体越狱，点燃了行业积压已久的恐慌。"
  },
  {
    "id": "wscn:3781558",
    "domain": "股票",
    "title": "“超级周”来袭：美联储会加息吗？霍尔木兹能达成协议吗？",
    "url": "https://wallstreetcn.com/articles/3781558",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T01:46:44+00:00",
    "summary": "美联储将公布利率决议，加息还是按兵不动“势均力敌”；日本央行料加息25个基点，英国央行预计维持不变。地缘方面，伊朗将与海湾国家谈霍尔木兹协议。数据方面，中国8月社零、工业增加值等出炉。科技方面，华为全联接大会、字节豆包手机发布、Anthropic开发者大会或举行。此外，中美外交大事件预计在9月24日。"
  },
  {
    "id": "wscn:3781638",
    "domain": "股票",
    "title": "Altman“放话”：OpenAI今年不会IPO，如果AI威胁人类生存，宁愿毁掉IPO",
    "url": "https://wallstreetcn.com/articles/3781638",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T01:02:25+00:00",
    "summary": "OpenAI CEO Sam Altman表示公司排除2026年上市计划。面对未来10%的技术灭绝风险，需避免盲目追求资本收益，并正与Anthropic等竞争对手协调放慢开发节奏。尽管行业监管呼声升温且市场持续动荡，Anthropic仍拟于秋季推进巨额IPO。"
  },
  {
    "id": "wscn:3781467",
    "domain": "股票",
    "title": "硅谷都在聊些什么？AI下半场开始！高盛Communacopia + TMT大会现场解码巨头框架",
    "url": "https://wallstreetcn.com/premium/articles/3781467?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-13T00:00:19+00:00",
    "summary": "旧金山高盛Communacopia + Technology Conference 2026的三场session，把未来三年AI算力产业链的经济模型、产能节奏、客户结构一次性摊开。"
  },
  {
    "id": "wscn:3781634",
    "domain": "股票",
    "title": "石油市场已达“转折点”？",
    "url": "https://wallstreetcn.com/articles/3781634",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T11:40:15+00:00",
    "summary": "布伦特原油当周涨幅超9%，中国国内原油期货出现罕见溢价，能源机构警告油价正迈向\"上行螺旋\"。核心驱动力包括：全球原油库存两周去化1.2亿桶，中国9月原油进口量预计回升。霍尔木兹海峡航运受阻叠加俄罗斯炼厂遭袭，成品油市场压力远超原油本身，美国柴油零售价首破每加仑6美元。"
  },
  {
    "id": "wscn:3780709",
    "domain": "股票",
    "title": "1万亿美元回购仍在继续，但美股最熟悉的资本游戏已经变了",
    "url": "https://wallstreetcn.com/premium/articles/3780709?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T11:28:55+00:00",
    "summary": "2026年的美股出现了一个耐人寻味的反差：企业回购仍处历史高位，全球4-5月宣布回购金额刷新纪录；与此同时，承担AI建设的科技巨头正在把更多现金投向数据中心、芯片和电力系统，部分Hyperscaler的回购已经明显回落。过去十多年，高利润、高自由现金流和高回购共同支撑了美股每股盈利与股票供给结构，如今这一组合开始发生变化。如果AI导致自由现金流持续走弱，2027年会不会成为回购结构的分水岭？"
  },
  {
    "id": "wscn:3781632",
    "domain": "股票",
    "title": "高盛最新判断：利率上升≠美股下跌，盈利增长才是牛市关键",
    "url": "https://wallstreetcn.com/articles/3781632",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-12T10:50:11+00:00",
    "summary": "高盛认为，高利率是股市的逆风，但不是终结牛市的力量。30年期美债收益率飙至5.3%，但历史数据显示加息后12个月美股平均回报高达+9%。企业资产负债表处于20年最强水平，AI投资、并购潮持续提振盈利预期。预计2026年标普500每股盈利将达340美元，同比增长24%。"
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
    "id": "hn:49335271",
    "domain": "股票",
    "title": "30-year Treasury yield tops 5.31%, the highest in 19 years",
    "url": "https://www.cnbc.com/2026/08/17/treasury-yields-federal-reserve-fomc-minutes.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-08-17T18:14:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49511824",
    "domain": "股票",
    "title": "Apple Is Suddenly an AI Infra Stock as OpenAI Buys 10k+ Macs",
    "url": "https://247wallst.com/investing/2026/08/31/apple-is-suddenly-an-ai-infrastructure-stock-as-openai-buys-macs-by-the-tens-of-thousands/",
    "source": "prabal97",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-08-31T16:44:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49593962",
    "domain": "股票",
    "title": "HPE Gives Oracle Right to Buy 4.2M Shares for 1 Cent Each",
    "url": "https://www.forbes.com/sites/antoniopequenoiv/2026/09/03/hewlett-packard-enterprise-gives-oracle-right-to-buy-205-million-in-stock-at-slashed-rate/",
    "source": "gurjeet",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-09-07T04:38:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596033",
    "domain": "股票",
    "title": "Show HN: Forget Rigid Stock Screeners – A Universal Query API for Financial Data",
    "url": "https://financialdata.net/universal-query",
    "source": "_FDN_",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-09-07T09:24:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:49323620",
    "domain": "股票",
    "title": "Anthropic IPO valuation hinges on $190-200B 2028 revenue forecast",
    "url": "https://www.reuters.com/business/anthropic-ipo-valuation-hinges-190-200-billion-2028-revenue-forecast-sources-say-2026-08-15/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-08-16T21:00:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49401229",
    "domain": "股票",
    "title": "Anthropic IPO filing will show AI backlash as a risk factor, sources say",
    "url": "https://www.cnbc.com/2026/08/21/-anthropic-ipo-filing-will-show-ai-backlash-as-risk-sources-say.html",
    "source": "newsomix9xl",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-08-22T16:23:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:49342823",
    "domain": "股票",
    "title": "OpenAI disbanded the team that assessed catastrophic model risks",
    "url": "https://thenextweb.com/news/openai-preparedness-team-disbanded-ipo-streamlining",
    "source": "nyku",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-08-18T08:06:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49311379",
    "domain": "股票",
    "title": "OpenAI talent exodus raises 'huge red flag' ahead of IPO",
    "url": "https://www.cnbc.com/2026/08/14/open-ai-ipo-red-flag.html",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-08-15T15:25:16+00:00",
    "summary": ""
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
    "id": "hn:49451482",
    "domain": "股票",
    "title": "Hackers Broke into Justice Department, NASA, Federal Reserve, Senate",
    "url": "https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-platforms-operated-and-used-china-state-sponsored-hackers",
    "source": "2OEH8eoCRo0",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-26T16:05:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49450370",
    "domain": "股票",
    "title": "Chinese Hackers Broke into Justice Department, NASA, Federal Reserve, Senate",
    "url": "https://www.reuters.com/world/china/china-sponsored-hacking-platforms-seized-by-us-justice-department-says-2026-08-26/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-26T14:59:43+00:00",
    "summary": ""
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
    "id": "hn:49355142",
    "domain": "金融",
    "title": "Sticky wage norms and the real wage cost of unexpected inflation",
    "url": "https://bfi.uchicago.edu/wp-content/uploads/2026/08/BFI_WP_2026-108-1.pdf",
    "source": "jplusequalt",
    "platform": "hackernews",
    "points": 392,
    "published_at": "2026-08-19T00:53:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49325159",
    "domain": "金融",
    "title": "The federal keyword lists that canceled billions in research funding",
    "url": "https://www.highereddive.com/news/inside-the-federal-keyword-lists-that-canceled-billions-in-research-funding/826203/",
    "source": "walrus01",
    "platform": "hackernews",
    "points": 284,
    "published_at": "2026-08-17T00:14:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49602582",
    "domain": "金融",
    "title": "A Tesla ran a stop sign and killed a man, Full Self-Driving/Autopilot was on",
    "url": "https://electrek.co/2026/09/07/tesla-driver-assist-stop-sign-buena-vista/",
    "source": "FabHK",
    "platform": "hackernews",
    "points": 169,
    "published_at": "2026-09-07T20:21:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49601846",
    "domain": "金融",
    "title": "Tesla killing Solar Roof is leaving installers with six-figure losses",
    "url": "https://electrek.co/2026/09/01/tesla-solar-roof-exit-installers-losses/",
    "source": "voxadam",
    "platform": "hackernews",
    "points": 135,
    "published_at": "2026-09-07T19:08:47+00:00",
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
    "id": "hn:49591672",
    "domain": "金融",
    "title": "Hackers have withdrawn ~4k BTC (~$320M) from the Liquid Federation wallet",
    "url": "https://twitter.com/Liquid_BTC/status/2096696272447218108",
    "source": "felipelalli",
    "platform": "hackernews",
    "points": 125,
    "published_at": "2026-09-06T22:43:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49626052",
    "domain": "金融",
    "title": "One woman's Tesla was remotely controlled by an abusive ex-partner",
    "url": "https://www.theguardian.com/australia-news/2026/sep/09/how-one-womans-tesla-was-remotely-controlled-and-harass-by-her-abusive-ex-partner-ntwnfb",
    "source": "gradschool",
    "platform": "hackernews",
    "points": 73,
    "published_at": "2026-09-09T13:16:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596610",
    "domain": "金融",
    "title": "Initial effects of AI technology on employment look positive",
    "url": "https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here",
    "source": "MrBuddyCasino",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-09-07T10:38:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49599058",
    "domain": "金融",
    "title": "If a Tesla Cybercab fleet were profitable, Tesla wouldn't sell you one",
    "url": "https://electrek.co/2026/09/07/tesla-cybercab-fleet-profitable-wouldnt-sell/",
    "source": "jijojv",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-09-07T14:49:43+00:00",
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
    "id": "hn:49633640",
    "domain": "金融",
    "title": "DHS Program Analyzes Americans' Finances to Flag Drivers for Traffic Stops",
    "url": "https://www.military.com/dhs-program-analyzes-americans-finances-to-flag-drivers-for-traffic-stops-report",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-09-09T20:22:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:49612981",
    "domain": "金融",
    "title": "DOJ Blocked ICE Agent Shooting Charge over Federal Prosecutor's Objections",
    "url": "https://www.propublica.org/article/doj-blocks-charges-ice-agent-minneapolis-julio-cesar-sosa-celis",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-09-08T16:54:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49335163",
    "domain": "金融",
    "title": "Meta faces 'astronomical' consequences as legal fight reaches critical moment",
    "url": "https://www.cnbc.com/2026/08/17/meta-attorneys-general-california-federal-trial-astronomical-consequences.html",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 86,
    "published_at": "2026-08-17T18:06:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49439296",
    "domain": "金融",
    "title": "A brief history of federal lift ticket regulation",
    "url": "https://zakpodmore.substack.com/p/a-brief-history-of-federal-lift-ticket",
    "source": "CGMthrowaway",
    "platform": "hackernews",
    "points": 69,
    "published_at": "2026-08-25T19:25:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49564189",
    "domain": "金融",
    "title": "Norway's Oil Fund Proposes Selling Roughly $80B in U.S. Treasurys",
    "url": "https://www.wsj.com/finance/investing/norways-oil-fund-proposes-cut-to-government-bond-holdings-d930893f",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-09-04T13:15:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:49514224",
    "domain": "金融",
    "title": "Monero Inflation Checker – FCMP++",
    "url": "https://www.reddit.com/r/Monero/comments/1w3hcos/monero_inflation_checker_fcmp/",
    "source": "Cider9986",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-08-31T20:00:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49432102",
    "domain": "金融",
    "title": "Nostr vs. Fediverse vs. Bluesky: A Comparison of Decentralized Social Protocols",
    "url": "https://soapbox.pub/blog/comparing-protocols",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-08-25T11:27:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49548497",
    "domain": "金融",
    "title": "Mark Cuban: Why US hospitals \"don't know their costs\"",
    "url": "https://www.beckershospitalreview.com/finance/mark-cuban-why-us-hospitals-dont-know-their-costs/",
    "source": "elo2000",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-09-03T11:07:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49515596",
    "domain": "金融",
    "title": "Congress to vote on denying federal funding to universities that boycott Israel",
    "url": "https://twitter.com/dylanotes/status/2094229210889965634",
    "source": "slowin",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-08-31T22:24:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49551601",
    "domain": "金融",
    "title": "Inside Google’s $200bn Wall Street finance machine for Anthropic",
    "url": "https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c",
    "source": "porridgeraisin",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-09-03T15:26:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49396088",
    "domain": "金融",
    "title": "S&P 500 CEO median pay hits $17.3M, widening CEO-worker ratio to 312-to-1",
    "url": "https://finance.yahoo.com/markets/stocks/articles/p-500-ceo-median-pay-234900518.html",
    "source": "newsomix9xl",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-08-22T02:38:14+00:00",
    "summary": ""
  },
  {
    "id": "hn:49348573",
    "domain": "金融",
    "title": "Trump 2.0 has deleted or altered nearly 400 US datasets",
    "url": "https://www.theguardian.com/us-news/ng-interactive/2026/aug/18/trump-federal-data-deleted-altered",
    "source": "_djo_",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-08-18T16:51:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:49444266",
    "domain": "金融",
    "title": "Running out of money': Kraft, McDonald's, Whirlpool CEOs flag consumer concern",
    "url": "https://finance.yahoo.com/economy/articles/running-money-kraft-mcdonald-whirlpool-114500035.html",
    "source": "MrJagil",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-08-26T05:14:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49441647",
    "domain": "金融",
    "title": "Complete list of U.S. products subject to counter tariffs",
    "url": "https://www.canada.ca/en/department-finance/programs/international-trade-finance-policy/canadas-response-us-tariffs/complete-list-us-products-subject-to-counter-tariffs.html",
    "source": "jonbaer",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-25T22:38:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:49352830",
    "domain": "金融",
    "title": "The most influential economist is oddly unconvincing",
    "url": "https://www.economist.com/finance-and-economics/2026/08/17/the-worlds-most-influential-economist-is-oddly-unconvincing",
    "source": "aragonite",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-18T21:15:31+00:00",
    "summary": ""
  }
]
```
