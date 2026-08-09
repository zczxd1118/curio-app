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

- 今日日期：`2026-08-09`
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
  "date": "2026-08-09",
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
    "points": 4153232,
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
    "points": 1681677,
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
    "points": 1600421,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV16YRLB7Exd",
    "domain": "AI",
    "title": "5分钟安装ClaudeCode并接入DeepSeek",
    "url": "http://www.bilibili.com/video/av116503957473279",
    "source": "Yin_Code",
    "platform": "bilibili",
    "points": 1382118,
    "published_at": "2026-05-02T08:14:12+00:00",
    "summary": "5分钟教你安装ClaudeCode并接入DeepSeekV4\n用到的命令：\nnode版本检查：node -v\nnpm版本检查：npm -v\nnpm国内镜像：npm config set registry https://registry.npmmirror.com/\ngit版本检查：git -v\nClaudeCode安装命令：npm install -g @anthropic-ai/claude-"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1318664,
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
    "points": 1261550,
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
    "points": 1078111,
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
    "points": 1024458,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1khMX63EjU",
    "domain": "AI",
    "title": "Vibe Coding竞赛，Claude遗憾落败?",
    "url": "http://www.bilibili.com/video/av117030980230736",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 699290,
    "published_at": "2026-08-05T10:30:00+00:00",
    "summary": "我和源宝打了个赌：半天时间，vibe coding一个活动社交App，看谁做的更好？最后Claude Code居然遗憾落败？这期视频，我们将用秒哒手把手带你走完，从一个简单的想法到App上架应用商店的全套流程！开发过程又发生了哪些趣事？一起来看看～"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 670362,
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
    "points": 604272,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 582861,
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
    "points": 569684,
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
    "points": 516099,
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
    "points": 446276,
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
    "points": 435279,
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
    "points": 419864,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1Tv3i6LEX1",
    "domain": "AI",
    "title": "用Codex、cursor 还是Claude ？程序员不作选择题，我都要用，还一起用 | Orca ADE 介绍",
    "url": "http://www.bilibili.com/video/av116996217838997",
    "source": "技术胖",
    "platform": "bilibili",
    "points": 415888,
    "published_at": "2026-07-28T06:41:31+00:00",
    "summary": "如果能把 Codex、Claude Code、Grok、Cursor 等智能编程工具整合到同一个工作环境中，再让多个 Agent 像团队成员一样分工协作，软件开发的效率将得到显著提升。Orca ADE 正是为此而生：它是一款开源、免费的 Agent 开发环境，专注于代码管理与命令行工作流，不仅能够接入多种编程 Agent，还支持语音操作和手机远程管理。接下来，我们就来认识一下 Orca ADE，看"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 259985,
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
    "points": 228761,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 220406,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1Xsuc67ExR",
    "domain": "AI",
    "title": "DeepSeek V4 Flash 接入 Codex + 识图，2 分钟搞定！",
    "url": "http://www.bilibili.com/video/av117036734816072",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 182628,
    "published_at": "2026-08-04T10:24:35+00:00",
    "summary": "2 分钟，教你把 DeepSeek V4 Flash 模型接入 Codex，并通过 Vision Skill 对接新出的通义千问 Qwen3.8-Max 实现识图，保姆级教程，帮你省掉上百块订阅费，AI 编程几乎没有门槛了。\n编程学习教程+实战项目+简历模板：codefather.cn\n免费 AI 编程教程：github.com/liyupi/ai-guide\n记得三连支持、关注鱼皮，让更多朋友学"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 178753,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV172GP6rEZs",
    "domain": "AI",
    "title": "🚀DeepSeek V4 Flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！",
    "url": "http://www.bilibili.com/video/av117014605731815",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 173610,
    "published_at": "2026-07-31T12:42:57+00:00",
    "summary": "🚀DeepSeek v4 flash全面实测：Claude Code接入后连续开发7个项目，真的已经接近Claude Opus 4.8了吗？最便宜的国产模型！性能、速度与真实短板全曝光！对比Kimi K3后优点和缺点都藏不住了\n\nDeepSeek 发布了 DeepSeek V4 Flash 0731：284B 总参数、13B 激活参数、100 万 Token 上下文，官方基准表现接近 Claude"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 145532,
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
    "points": 123741,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 99733,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1ENLV63EKZ",
    "domain": "AI",
    "title": "100%免费！Claude Code 跑本地模型，无需 API、无需翻墙、白嫖超强AI Agent｜Ollama｜CC Switch｜零度解说",
    "url": "http://www.bilibili.com/video/av116583833804127",
    "source": "零度解说",
    "platform": "bilibili",
    "points": 98014,
    "published_at": "2026-05-16T12:00:00+00:00",
    "summary": "Claude Code 跑本地模型必备工具下载：https://bittly.cc/switch"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93063,
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
    "points": 74056,
    "published_at": "2023-03-23T11:32:23+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1XVub6bE9h",
    "domain": "AI",
    "title": "当普通人第一次让Agent干活……",
    "url": "http://www.bilibili.com/video/av117053226818905",
    "source": "糖果果的未来要发光",
    "platform": "bilibili",
    "points": 72474,
    "published_at": "2026-08-07T10:00:00+00:00",
    "summary": "最近一个AI agent工具Traework\n发布了一个40万字教程，特别详细。\n我看完后压缩成了这十分钟的教程。\n\n顺便实测了一下 Agent现在到底能干啥，\n还顺便搓了个能用手势控制B站的插件。"
  },
  {
    "id": "bvid:BV1MPMd64EiD",
    "domain": "AI",
    "title": "我Vibe Coding做的游戏，上架Steam了【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av117031449925140",
    "source": "Nenly同学",
    "platform": "bilibili",
    "points": 68089,
    "published_at": "2026-08-03T11:57:47+00:00",
    "summary": "三个月前，我对游戏开发一无所知，一行代码都不会写，也没摸过游戏引擎。\n现在，我靠VibeCoding做的游戏已经上架 Steam 了。\n\n游戏名：《群侠传：幸存者》\n抢先体验期间完全免费"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 66924,
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
    "points": 47575,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1cyMi6tEqU",
    "domain": "AI",
    "title": "我的贾维斯开源了，可以语音交互，控制多Agent编排【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av116882686351128",
    "source": "小天fotos",
    "platform": "bilibili",
    "points": 47119,
    "published_at": "2026-07-08T10:00:00+00:00",
    "summary": "大家久等了\n答应大家的，我的语音多Agent编排系统\n开源了\n不过改名叫homerail\n本期视频聊聊它能干什么不能干什么\n以及未来的RoadMap"
  },
  {
    "id": "bvid:BV1SqdeBnEvV",
    "domain": "AI",
    "title": "Cursor助手｜Cursor自定义模型API｜0门槛永久免费的cursor byok",
    "url": "http://www.bilibili.com/video/av116415373778266",
    "source": "leookun",
    "platform": "bilibili",
    "points": 45635,
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
    "points": 40140,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1ZAAqzdEPv",
    "domain": "AI",
    "title": "我的世界1.8-26.1纯生存无限制服务器，离线可进，高自由度(旧存档重新开放)",
    "url": "http://www.bilibili.com/video/av116151921149457",
    "source": "玉孤旰",
    "platform": "bilibili",
    "points": 36102,
    "published_at": "2026-03-01T04:03:18+00:00",
    "summary": "我的世界1.8-26.1纯生存无限制服务器，离线可进，极高自由度(高到允许开挂)\n没有版本限制，1.8至26.1都可以进入，没有正版限制，无需进入QQ群审核！\n服务器地址：mc.zyxcc.xyz:25565，端口默认。官方QQ群：1037305761\n此次恢复开放，完整沿用 2026 年 3 月 1 日开服以来的原始旧存档，同时取消世界大小限制与玩家人数上限。\n没有各种杂七杂八的规则限制，自由度"
  },
  {
    "id": "bvid:BV1Frgv6bEBK",
    "domain": "AI",
    "title": "无规则服务器当你进入别的玩家的住宅belike：",
    "url": "http://www.bilibili.com/video/av116974743065683",
    "source": "琉璃海yt",
    "platform": "bilibili",
    "points": 30491,
    "published_at": "2026-07-24T11:37:24+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29572,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV11K9gBqEnW",
    "domain": "AI",
    "title": "【杀戮尖塔2】AI MOD 配置教程第一期来辣！手把手教你怎么改提示词！以及如何设计自己的爬塔玩法",
    "url": "http://www.bilibili.com/video/av116341654755924",
    "source": "分歧点WhatIf",
    "platform": "bilibili",
    "points": 26124,
    "published_at": "2026-04-03T16:14:43+00:00",
    "summary": "每个参数都是干什么的，如何修改提示词的教程。\n不知道这是什么？请看合集内的视频~\n我做了一个 AI 的杀戮尖塔2MOD！\n可以和怪物对话，策反怪物，带着怪物爬塔（重写了几乎每一个怪物在友方时候的行为），还能给怪物打防御，带个沙虫全吃了！\n可以和上古之民对话，聊嗨了会给你 1～2 个额外赐福，还能帮你指示为未来\n可以让偷窃草蜢偷队友的 key 卡，想无限？偷了！\n可以和商人讨价还价，甚至白嫖\n多人的"
  },
  {
    "id": "bvid:BV1YJ336EEBk",
    "domain": "AI",
    "title": "【AI陪玩】开袋即食的AI接入我的世界教程！",
    "url": "http://www.bilibili.com/video/av116981806143216",
    "source": "万昇Dwin",
    "platform": "bilibili",
    "points": 25117,
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
    "points": 22696,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "7月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "小芸AI",
    "platform": "bilibili",
    "points": 21959,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "AI充值站：njzqhy.top"
  },
  {
    "id": "bvid:BV1dsNv66E3Q",
    "domain": "AI",
    "title": "【Cursor】2026年最新版免费永久使用cursor使用教程，程序员编程必备，史上最强AI编程工具(附安装包)",
    "url": "http://www.bilibili.com/video/av116922599344955",
    "source": "六月要癫",
    "platform": "bilibili",
    "points": 20886,
    "published_at": "2026-07-15T06:39:18+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1cCEi6sEU5",
    "domain": "AI",
    "title": "🦊他能成功吗？Claude Code 接管虚幻引擎5，打造一款游戏 | 带你走完整个流程",
    "url": "http://www.bilibili.com/video/av116731724959171",
    "source": "Apeak_虚幻丰哥",
    "platform": "bilibili",
    "points": 20417,
    "published_at": "2026-06-11T13:41:36+00:00",
    "summary": "Claude Code 接管虚幻引擎5，打造了一款游戏\n下载我的 CLAUDE.md（帮你省 token 的配置）\n链接：https://pan.quark.cn/s/b6e50b4b2535\n提取码：tbaE\nStefan 3D AI ：https://www.youtube.com/watch?v=iRcrZjOt5H8&amp;t=1s\n🔗 完整教程指南和链接：https://www.top"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 20186,
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
    "points": 19651,
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
    "points": 18472,
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
    "points": 16092,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
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
    "title": "Amazon secretly circumvents community vote for massive AI data center using 45-year-old rules — Gilroy residents locked out of public comment window",
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
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/protesters-haul-a-guillotine-to-city-council-meeting-about-a-potential-ai-data-center-company-rep-cornered-by-protestors-it-no-longer-felt-safe-to-stay-developer-escorted-out-by-police",
    "domain": "AI 算力 / 半导体",
    "title": "Protesters haul a guillotine to city council meeting about a potential AI data center, company rep cornered by protestors — ‘ it no longer felt safe to stay,’ developer escorted out by police",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/protesters-haul-a-guillotine-to-city-council-meeting-about-a-potential-ai-data-center-company-rep-cornered-by-protestors-it-no-longer-felt-safe-to-stay-developer-escorted-out-by-police",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T14:32:26+00:00",
    "summary": "Some protesters brought a guillotine to public consultation for a potential data center in Salem, Oregon. Even though this was displayed outside the venue, it was a confrontation between the data cent"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-august-7-2026-inside-chinas-lithography-efforts-co-packaged-optics-get-a-spotlight-and-samsung-debuts-next-gen-memory-tech",
    "domain": "AI 算力 / 半导体",
    "title": "This week on Tom's Hardware Premium: August 8, 2026 — Inside China's lithography efforts, co-packaged optics get a spotlight, and Samsung debuts next-gen memory tech",
    "url": "https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-august-7-2026-inside-chinas-lithography-efforts-co-packaged-optics-get-a-spotlight-and-samsung-debuts-next-gen-memory-tech",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T13:44:37+00:00",
    "summary": "A redesigned Bench tool, inside China's domestic Chipmaking efforts, breaking, and we offer a free technical breakdown of Samsung's latest memory-related announcements."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/grab-an-entire-rtx-5090-pc-for-just-usd380-more-than-the-standalone-graphics-card-save-usd1-550-off-alienwares-area-51-gaming-rig",
    "domain": "AI 算力 / 半导体",
    "title": "Grab an entire RTX 5090 PC for just $380 more than the standalone graphics card — save $1,550 off Alienware's Area-51 gaming rig",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/grab-an-entire-rtx-5090-pc-for-just-usd380-more-than-the-standalone-graphics-card-save-usd1-550-off-alienwares-area-51-gaming-rig",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T13:38:40+00:00",
    "summary": "Pick up an entire Alienware RTX 5090 gaming PC for just $380 more than the RTX 5090 GPU bought separately."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/introducing-bench-2-0-a-revamped-benchmark-analyzer-exclusively-for-toms-hardware-premium-subscribers",
    "domain": "AI 算力 / 半导体",
    "title": "Introducing Bench 2.0 — a revamped benchmark analyzer, exclusively for Tom's Hardware Premium subscribers",
    "url": "https://www.tomshardware.com/pc-components/introducing-bench-2-0-a-revamped-benchmark-analyzer-exclusively-for-toms-hardware-premium-subscribers",
    "source": "Jeremy Kaplan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T13:27:12+00:00",
    "summary": "We’re pleased to introduce Bench 2.0, a ground-up rethink of our benchmarking tool that makes it the most powerful, most intuitive benchmark browser in the business. Bench 2.0 has tons of new features"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/hyperx-omen-max-16-review",
    "domain": "AI 算力 / 半导体",
    "title": "HyperX Omen Max 16 review: All bark and no bite",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/hyperx-omen-max-16-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T12:05:00+00:00",
    "summary": "The Omen Max 16 definitely looks like a desktop replacement gaming laptop, but its gaming performance meows instead of roars."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/apple-revealed-the-first-mac-pro-20-years-ago-today-its-intel-xeon-powered-flagship-desktop-took-the-reins-from-the-power-mac-g5",
    "domain": "AI 算力 / 半导体",
    "title": "Apple revealed the first Mac Pro 20 years ago today — its Intel Xeon-powered flagship desktop took the reins from the Power Mac G5",
    "url": "https://www.tomshardware.com/desktops/apple-revealed-the-first-mac-pro-20-years-ago-today-its-intel-xeon-powered-flagship-desktop-took-the-reins-from-the-power-mac-g5",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T11:58:46+00:00",
    "summary": "20 years ago today Steve Jobs took to the Apple WWDC stage to unveil the first-ever Mac Pro desktop computer. This is when Mac workstations transitioned from PowerPC to Intel Xeon chips."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-sells-rtx-50-series-gpus-at-msrp-during-quakecon-2026-graphics-cards-sold-at-launch-prices-more-than-a-year-after-release-are-now-considered-an-attraction",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia sells RTX 50-series GPUs at MSRP during QuakeCon 2026 — graphics cards sold at launch prices more than a year after release are now considered an attraction",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-sells-rtx-50-series-gpus-at-msrp-during-quakecon-2026-graphics-cards-sold-at-launch-prices-more-than-a-year-after-release-are-now-considered-an-attraction",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T11:11:49+00:00",
    "summary": "The Nvidia booth at QuakeCon 2026 is offering Founders Edition GeForce RTX 5090, 5080, and 5070 GPUs at MSRP. Supplies are limited, though, so you should head out ASAP if you want to snag one right no"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/msis-magnificent-32-inch-4k-oled-gaming-monitor-returns-to-its-lowest-ever-price-of-usd599-save-usd130-on-the-mag-321upxb-the-perfect-240hz-upgrade",
    "domain": "AI 算力 / 半导体",
    "title": "MSI's magnificent 32-inch 4K OLED gaming monitor returns to its lowest-ever price of $599 — save $130 on the MAG 321UPXB, the perfect 240Hz upgrade",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/msis-magnificent-32-inch-4k-oled-gaming-monitor-returns-to-its-lowest-ever-price-of-usd599-save-usd130-on-the-mag-321upxb-the-perfect-240hz-upgrade",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T11:02:38+00:00",
    "summary": "Save $130 on this gorgeous 32-inch QD-OLED gaming monitor from MSI and experience crisp visuals in 4K."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/terafab-starts-to-take-shape-100-million-square-feet-of-manufacturing-space-and-usd16-8b-initial-capital-investment",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk's massive Terafab chip-making facility starts to take shape — 100 million square feet of manufacturing space and $16.8B initial capital investment",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/terafab-starts-to-take-shape-100-million-square-feet-of-manufacturing-space-and-usd16-8b-initial-capital-investment",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T11:00:00+00:00",
    "summary": "SpaceX and Tesla officially begin to build the massive Terafab facility that will be three times bigger than Samsung's Pyeongtaek campus."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd370-on-this-1440p-gaming-pc-with-an-rtx-5060-ti-16gb-formidable-abs-cyclone-aqua-rig-ships-with-20-core-intel-core-i7-14700f-16gb-ddr5-and-a-1tb-ssd-now-only-usd1-329-99",
    "domain": "AI 算力 / 半导体",
    "title": "Save $370 on this 1440p gaming PC with an RTX 5060 Ti 16GB — formidable ABS Cyclone Aqua rig ships with 20-core Intel Core i7-14700F, 16GB DDR5 and a 1TB SSD, now only $1,329.99",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd370-on-this-1440p-gaming-pc-with-an-rtx-5060-ti-16gb-formidable-abs-cyclone-aqua-rig-ships-with-20-core-intel-core-i7-14700f-16gb-ddr5-and-a-1tb-ssd-now-only-usd1-329-99",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T10:42:00+00:00",
    "summary": "Save $300 on this Newegg-made ABS Cyclone Aqua gaming PC, featuring an RTX 5060 Ti 16GB, Intel Core i7-14700F, 16GB DDR5, and a 1TB SSD for $1,399.99 right now."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/anthropic-to-build-its-own-co-designed-custom-ai-accelerator-for-inferencing-workloads-samsung-reported-to-be-partnering-with-the-claude-ai-maker-for-manufacturing",
    "domain": "AI 算力 / 半导体",
    "title": "Anthropic co-designing custom AI inference chips to bypass costly Nvidia GPUs — Samsung reported as manufacturing partner for Claude maker",
    "url": "https://www.tomshardware.com/tech-industry/anthropic-to-build-its-own-co-designed-custom-ai-accelerator-for-inferencing-workloads-samsung-reported-to-be-partnering-with-the-claude-ai-maker-for-manufacturing",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T10:30:00+00:00",
    "summary": "Anthropic has announced its building a team to co-design custom ASIC chips for AI inferencing workloads. This will give it greater control over its compute buildout and allow it to make its AI models "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-opus-5-mistakenly-deletes-devs-entire-profile-directory-ai-tool-mistakes-users-home-directory-as-temporary-backup-proceeds-to-wipe-everything-to-undo-error",
    "domain": "AI 算力 / 半导体",
    "title": "Claude Opus 5 mistakenly deletes dev’s entire profile directory during routine backup, responds with 'Sorry, typo' — AI tool mistakes user's home directory as temporary backup, proceeds to wipe everyt",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-opus-5-mistakenly-deletes-devs-entire-profile-directory-ai-tool-mistakes-users-home-directory-as-temporary-backup-proceeds-to-wipe-everything-to-undo-error",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T10:00:00+00:00",
    "summary": "An AI agent got confused with file path conventions and mistakenly deleted its user's entire profile folder. Claude Opus 5 apologized to the user, who called it \"the funniest and most painful AI momen"
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
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/pre-modded-rtx-2080-ti-cards-with-22gb-of-vram-surface-on-ebay-for-usd500-hong-kong-based-seller-offers-ai-friendly-memory-mod-for-a-reasonable-price",
    "domain": "AI 算力 / 半导体",
    "title": "Pre-modded 22GB RTX 2080 Ti cards surface on eBay for $500 as VRAM-hungry local AI fans chase down every spare FLOP — Hong Kong-based seller offers AI-friendly memory mod for a reasonable price",
    "url": "https://www.tomshardware.com/pc-components/gpus/pre-modded-rtx-2080-ti-cards-with-22gb-of-vram-surface-on-ebay-for-usd500-hong-kong-based-seller-offers-ai-friendly-memory-mod-for-a-reasonable-price",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T16:11:19+00:00",
    "summary": "Services have recently popped up that will double your RTX 2080 Ti's memory to 22GB, but if you don't have a card to spare, you can now get a pre-modded 22 GB 2080 Ti for $499 from eBay."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/after-severe-76-percent-electricity-price-hikes-due-to-ai-data-centers-virginia-requires-firms-to-pay-for-all-dedicated-upstream-electrical-infrastructure-state-regulators-crack-down-governor-says-move-will-save-civilians-hundreds-of-millions-of-dollars",
    "domain": "AI 算力 / 半导体",
    "title": "After severe 76% electricity price hikes due to AI data centers, Virginia requires firms to pay for all dedicated upstream electrical infrastructure — state regulators crack down, governor says move w",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/after-severe-76-percent-electricity-price-hikes-due-to-ai-data-centers-virginia-requires-firms-to-pay-for-all-dedicated-upstream-electrical-infrastructure-state-regulators-crack-down-governor-says-move-will-save-civilians-hundreds-of-millions-of-dollars",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T15:32:08+00:00",
    "summary": "Virginia's public utility regulator now requires all data center projects to pay for the infrastructure needed to supply their power. This makes it one of the first states to convert the 'ratepayer pr"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/usd1-billion-of-iphone-18-pro-chips-on-the-shelves-awaiting-packaging-due-to-dram-shortages-memory-shortages-reportedly-put-a-wrinkle-in-apples-launch-plans",
    "domain": "AI 算力 / 半导体",
    "title": "$1 billion of iPhone 18 Pro chips 'on the shelves awaiting packaging' due to DRAM shortages — memory shortages reportedly put a wrinkle in Apple's launch plans",
    "url": "https://www.tomshardware.com/pc-components/dram/usd1-billion-of-iphone-18-pro-chips-on-the-shelves-awaiting-packaging-due-to-dram-shortages-memory-shortages-reportedly-put-a-wrinkle-in-apples-launch-plans",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T14:52:11+00:00",
    "summary": "Apple reportedly as $1 billion worth of iPhone 18 processor wafers awaiting packaging, which hasn't been completed due to DRAM shortages."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/policy/nashville-attempts-to-block-controversial-data-center-near-zoo-with-eminent-domain-city-could-force-developer-to-sell-the-land-for-public-use-rather-than-usd700-million-installation",
    "domain": "AI 算力 / 半导体",
    "title": "Nashville attempts to block controversial data center near zoo with eminent domain — city could force developer to sell the land for public use, rather than $700 million installation",
    "url": "https://www.tomshardware.com/tech-industry/policy/nashville-attempts-to-block-controversial-data-center-near-zoo-with-eminent-domain-city-could-force-developer-to-sell-the-land-for-public-use-rather-than-usd700-million-installation",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-06T13:26:17+00:00",
    "summary": "The Nashville Metro Council just gave the go ahead for the mayor's plan to buy the land that a proposed data center will sit on through eminent domain. This will force the developer to give up the lan"
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
    "points": 855,
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
    "points": 398,
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
    "points": 199,
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
    "points": 118,
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
    "id": "rss:https://www.theverge.com/tech/977084/ted-lasso-bose-tony-installer",
    "domain": "大厂 AI 动态",
    "title": "My favorite feel-good show is back",
    "url": "https://www.theverge.com/tech/977084/ted-lasso-bose-tony-installer",
    "source": "David Pierce",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T12:00:00+00:00",
    "summary": "Hi, friends! Welcome to Installer No. 139, your guide to the best and Verge-iest stuff in the world. (If you're new here, welcome, barbecue sauce, and also you can read all the old editions at the Ins"
  },
  {
    "id": "rss:https://www.theverge.com/tech/976506/nitecore-nb10000-gen4-review-adventure-battery",
    "domain": "大厂 AI 动态",
    "title": "Nitecore’s latest power bank is the lightest and most compact yet",
    "url": "https://www.theverge.com/tech/976506/nitecore-nb10000-gen4-review-adventure-battery",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T07:00:00+00:00",
    "summary": "There's two things you should know about me, your intrepid reviewer: I hate the feature creep associated with modern power banks, and I love shaving grams off the gear I carry when backpacking, bikepa"
  },
  {
    "id": "rss:https://www.theverge.com/games/977056/restart-gaming-site-walmart-moonrock-layoffs",
    "domain": "大厂 AI 动态",
    "title": "The gaming site sponsored by Walmart lays off its editorial staff",
    "url": "https://www.theverge.com/games/977056/restart-gaming-site-walmart-moonrock-layoffs",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T22:05:08+00:00",
    "summary": "Restart, a games media website launched in late 2024 that was sponsored by Walmart, has laid off its \"entire editorial team,\" according to a Friday post from Brandy Berthelson, the site's former edito"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/976801/fenix-flexin-rubberz-ai-song-treblo",
    "domain": "大厂 AI 动态",
    "title": "Fenix Flexin isn’t even denying using AI to make ‘Rubberz’ anymore",
    "url": "https://www.theverge.com/ai-artificial-intelligence/976801/fenix-flexin-rubberz-ai-song-treblo",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T20:01:51+00:00",
    "summary": "It took long enough, but now LA rapper Fenix Flexin appears to have admitted using AI for the 80s synth pop-themed song \"Rubberz.\" His comments follow the producer Medasin's videos claiming that an AI"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/976939/roku-fairground-ai-fast-channel",
    "domain": "大厂 AI 动态",
    "title": "Watching Roku’s AI channel is like eating from a trough",
    "url": "https://www.theverge.com/entertainment/976939/roku-fairground-ai-fast-channel",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T18:59:46+00:00",
    "summary": "The appeal of free ad-supported streaming television (FAST) channels has always been the way they make it easier to (re)discover classic films and series. But Roku's latest experiment in the FAST spac"
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
    "id": "rss:https://techcrunch.com/2026/08/07/openai-says-it-slowed-astra-model-development-over-security-concerns/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI says it slowed Astra model development over security concerns",
    "url": "https://techcrunch.com/2026/08/07/openai-says-it-slowed-astra-model-development-over-security-concerns/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T22:48:24+00:00",
    "summary": "OpenAI said this model, which is still in development, reached its \"critical cybersecurity threshold,\" meaning it could independently identify and carry out cyberattacks against traditionally well-pro"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/after-rippling-blew-millions-on-ai-in-months-it-built-an-employee-roi-tool/",
    "domain": "大厂 AI 动态",
    "title": "After Rippling blew millions on AI in months, it built an employee ROI tool",
    "url": "https://techcrunch.com/2026/08/07/after-rippling-blew-millions-on-ai-in-months-it-built-an-employee-roi-tool/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T21:30:11+00:00",
    "summary": "After its own AI usage wake-up call, Rippling this week unveiled AI Spend Console, a product that tracks individual and team employee AI spending."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/wacoms-movinkpad-11-is-a-fun-and-mid-priced-entry-point-for-digital-artists/",
    "domain": "大厂 AI 动态",
    "title": "Wacom’s MovinkPad 11 is a fun, midpriced entry point for digital artists",
    "url": "https://techcrunch.com/2026/08/07/wacoms-movinkpad-11-is-a-fun-and-mid-priced-entry-point-for-digital-artists/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T21:20:00+00:00",
    "summary": "The MovinkPad 11 a versatile little graphics tablet that can help make your wildest digital art dreams come true."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/security-researchers-scanned-the-polish-web-and-found-courts-hospitals-and-airports-at-risk-of-hacks/",
    "domain": "大厂 AI 动态",
    "title": "Security researchers scanned the Polish web and found courts, hospitals, and airports at risk of hacks",
    "url": "https://techcrunch.com/2026/08/07/security-researchers-scanned-the-polish-web-and-found-courts-hospitals-and-airports-at-risk-of-hacks/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T21:00:08+00:00",
    "summary": "Researchers found common points of failure, like software used to organize and display web content, could have allowed hackers to run riot through government websites."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/cloudflare-launches-kitesurf-a-browser-built-for-ai-agents/",
    "domain": "大厂 AI 动态",
    "title": "Cloudflare launches Kitesurf, a browser built for AI agents",
    "url": "https://techcrunch.com/2026/08/07/cloudflare-launches-kitesurf-a-browser-built-for-ai-agents/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T16:16:09+00:00",
    "summary": "Kitesurf is a cloud-hosted browser designed for AI agents instead of people. It uses less computing power than Chromium for common automation tasks, helping developers build browser-based AI agents mo"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/computer-maker-framework-notifies-all-customers-of-a-data-breach/",
    "domain": "大厂 AI 动态",
    "title": "Computer maker Framework notifies ‘all customers’ of a data breach",
    "url": "https://techcrunch.com/2026/08/07/computer-maker-framework-notifies-all-customers-of-a-data-breach/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T16:09:04+00:00",
    "summary": "Framework told \"all\" of its customers that hackers accessed their names, email addresses, phone numbers, and physical addresses in a data breach."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/todays-the-last-day-to-get-up-to-400-off-your-techcrunch-disrupt-2026-ticket/",
    "domain": "大厂 AI 动态",
    "title": "Today’s the last day to get up to $400 off your TechCrunch Disrupt 2026 ticket",
    "url": "https://techcrunch.com/2026/08/07/todays-the-last-day-to-get-up-to-400-off-your-techcrunch-disrupt-2026-ticket/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T15:52:33+00:00",
    "summary": "Starting today, you can take an additional $100 off your founder, investor, or attendee TechCrunch Disrupt 2026 pass, which is a nice bonus on top of our current discounted pricing."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/trump-administration-has-spent-nearly-4b-to-cancel-offshore-wind-farms/",
    "domain": "大厂 AI 动态",
    "title": "Trump administration has spent nearly $4B to cancel offshore wind farms",
    "url": "https://techcrunch.com/2026/08/07/trump-administration-has-spent-nearly-4b-to-cancel-offshore-wind-farms/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T15:11:03+00:00",
    "summary": "The Trump administration has now convinced developers to abandon 12 offshore wind leases. The latest will cost taxpayers $1.2 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/host-your-own-piece-of-disrupt-apply-to-run-a-side-event-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Host your own piece of Disrupt: Apply to run a Side Event at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/08/07/host-your-own-piece-of-disrupt-apply-to-run-a-side-event-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T14:30:00+00:00",
    "summary": "You put together the concept — from a founder mixer, an after-hours panel, a themed party, a morning run, whatever fits your goal — and the TechCrunch team helps put it in front of the attendees alrea"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/chinese-ai-model-kimi-escaped-its-cybersecurity-testing-environment-researchers-say/",
    "domain": "大厂 AI 动态",
    "title": "Chinese AI model Kimi escaped its cybersecurity testing environment, researchers say",
    "url": "https://techcrunch.com/2026/08/07/chinese-ai-model-kimi-escaped-its-cybersecurity-testing-environment-researchers-say/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T14:28:31+00:00",
    "summary": "In the Kimi test, the sandbox designed to contain the experiment was not properly configured."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/airbnb-says-ai-is-helping-it-ship-features-faster-as-it-tests-a-new-search-function/",
    "domain": "大厂 AI 动态",
    "title": "Airbnb says AI is helping it ship features faster as it tests a new search function",
    "url": "https://techcrunch.com/2026/08/07/airbnb-says-ai-is-helping-it-ship-features-faster-as-it-tests-a-new-search-function/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T14:22:49+00:00",
    "summary": "Airbnb will debut a new AI-powered search experience with a toggle."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/spacexs-terafab-will-rely-on-natural-gas-power-plants-not-tesla-solar-panels/",
    "domain": "大厂 AI 动态",
    "title": "SpaceX’s Terafab will rely on natural gas power plants, not Tesla solar panels",
    "url": "https://techcrunch.com/2026/08/07/spacexs-terafab-will-rely-on-natural-gas-power-plants-not-tesla-solar-panels/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T14:07:31+00:00",
    "summary": "The fab is intended to build chips for data centers that will be run by SpaceX and its xAI subsidiary."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/the-founders-guide-to-techcrunch-disrupt-2026-everything-you-need-to-know/",
    "domain": "大厂 AI 动态",
    "title": "The founder’s guide to TechCrunch Disrupt 2026: Everything you need to know",
    "url": "https://techcrunch.com/2026/08/07/the-founders-guide-to-techcrunch-disrupt-2026-everything-you-need-to-know/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T12:30:00+00:00",
    "summary": "TechCrunch Disrupt 2026 is built around one question: How do you build an enduring company in the AI era? Our programming and speaker lineup reflect that."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/07/new-mexico-court-orders-meta-to-pay-additional-567m-in-child-safety-case/",
    "domain": "大厂 AI 动态",
    "title": "New Mexico court orders Meta to pay additional $567M in child safety case",
    "url": "https://techcrunch.com/2026/08/07/new-mexico-court-orders-meta-to-pay-additional-567m-in-child-safety-case/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T11:40:37+00:00",
    "summary": "Meta's total fine has racked up to $942 million in this case."
  },
  {
    "id": "rss:https://stratechery.com/2026/earnings-and-learnings/",
    "domain": "大厂 AI 动态",
    "title": "2026.32: Earnings and Learnings",
    "url": "https://stratechery.com/2026/earnings-and-learnings/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T17:29:02+00:00",
    "summary": "The best Stratechery content from the week of August 3, 2026, including earnings exposure, OpenAI's answer to Apple, and all about LeBron in Philly."
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
    "id": "rss:https://arstechnica.com/gadgets/2026/08/europes-free-satellite-service-just-made-it-easier-to-track-wildfires/",
    "domain": "大厂 AI 动态",
    "title": "Europe's free satellite service just made it easier to track wildfires",
    "url": "https://arstechnica.com/gadgets/2026/08/europes-free-satellite-service-just-made-it-easier-to-track-wildfires/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T21:48:21+00:00",
    "summary": "Copernicus Browser adds wildfire visualization amid record wildfire season."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/08/flesh-eating-screwworms-feast-on-humans-in-mexico-human-cases-top-500/",
    "domain": "大厂 AI 动态",
    "title": "Flesh-eating screwworms feast on humans in Mexico; human cases top 500",
    "url": "https://arstechnica.com/health/2026/08/flesh-eating-screwworms-feast-on-humans-in-mexico-human-cases-top-500/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T21:09:00+00:00",
    "summary": "Six deaths reported among screwworm cases, one directly attributed to the flies."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/meta-ordered-to-pay-567m-to-treat-youth-mental-health-problems-it-helped-create/",
    "domain": "大厂 AI 动态",
    "title": "Judge rules Meta caused \"public nuisance\" and must fund mental health treatment",
    "url": "https://arstechnica.com/tech-policy/2026/08/meta-ordered-to-pay-567m-to-treat-youth-mental-health-problems-it-helped-create/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T19:49:27+00:00",
    "summary": "New Mexico judge orders $567M fund to help address youth mental health crisis."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/08/the-ultimate-eclipse-chase-a-concorde-raced-against-the-moons-shadow/",
    "domain": "大厂 AI 动态",
    "title": "The ultimate eclipse chase: A Concorde raced against the Moon's shadow",
    "url": "https://arstechnica.com/science/2026/08/the-ultimate-eclipse-chase-a-concorde-raced-against-the-moons-shadow/",
    "source": "Dhananjay Khadilkar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-07T19:00:17+00:00",
    "summary": "Fitted with telescopes, the plane did our longest imaging of the Sun's corona."
  },
  {
    "id": "hn:49057574",
    "domain": "股票",
    "title": "Google Discloses $94.1B in SpaceX Stock, Marking 6% Stake",
    "url": "https://www.wsj.com/tech/google-discloses-94-1-billion-in-spacex-stock-marking-6-stake-91655d7c",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 342,
    "published_at": "2026-07-26T12:43:21+00:00",
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
    "points": 70,
    "published_at": "2026-08-03T06:17:53+00:00",
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
    "id": "wscn:3779002",
    "domain": "股票",
    "title": "拯救悲剧股神后又当新娘！Anthropic幕僚长自述：在AI前沿寻找上帝",
    "url": "https://wallstreetcn.com/articles/3779002",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T03:52:03+00:00",
    "summary": "“AI股神”Leopold爆仓后，险些卖掉未婚妻、Anthropic幕僚长Balwit名下约50亿美元的股权救急。关键时刻，Balwit一句“千万别卖”拦下交易，为未婚夫保住了东山再起的资本。两人随后如期举行婚礼，上演现实版“华尔街血色婚礼”。而在Balwit看来，当硅谷正在造出越来越接近“神”的智能，人类真正需要警惕的，或许不是AI有多强，而是人类是否有足够的谦卑驾驭它。"
  },
  {
    "id": "wscn:3778997",
    "domain": "股票",
    "title": "AI推理前瞻——从基础设施建设到商业化变现",
    "url": "https://wallstreetcn.com/articles/3778997",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T03:48:46+00:00",
    "summary": "AI基础设施投资周期或许尚未见顶。花旗认为，电力、许可、劳动力、HBM和互联等供给约束，会把原本3年的产能扩张拉长至5—10年。"
  },
  {
    "id": "wscn:3778998",
    "domain": "股票",
    "title": "韩媒：SK海力士拟推710亿美元股东回报方案，40%用于回购股票，相当于美股发行规模",
    "url": "https://wallstreetcn.com/articles/3778998",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T02:52:24+00:00",
    "summary": "SK海力士拟推出总额约100万亿韩元（约710亿美元）的史上最大股东回报计划，其中自股回购约40万亿韩元，规模约占总股本2%，与其为在美国发行ADR而增发新股的规模基本相当。公司同时将于三季度公布追加回报方案，强劲的HBM需求与盈利预期为大手笔回购提供支撑。"
  },
  {
    "id": "wscn:3778910",
    "domain": "股票",
    "title": "下周重磅日程：美CPI，宇树科技打新，腾讯、京东、茅台、中芯国际财报",
    "url": "https://wallstreetcn.com/articles/3778910",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T02:03:31+00:00",
    "summary": "宏观面，美国7月CPI与PPI相继公布，直接定价美联储9月降息概率；澳联储利率决议同周落地。财报面，腾讯、京东、茅台、中芯国际、华虹半导体领衔中报季高峰，美股光模块龙头Lumentum、Coherent、算力基建CoreWeave等密集放榜。事件面，宇树科技打新、谷歌Pixel 11发布会、闪迪投资者日、美国SEC 13F季度持仓、黄仁勋会见LG高管，科技产业催化密集。"
  },
  {
    "id": "wscn:3778994",
    "domain": "股票",
    "title": "万斯称美伊冲突仍处于“博弈中段”，美军“寻找出口”，伊朗开出“重开海峡6大条件”",
    "url": "https://wallstreetcn.com/articles/3778994",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T02:01:40+00:00",
    "summary": "万斯称，美伊冲突\"已入中局\"，美方正综合运用外交、经济、军事手段；参联会主席凯恩私下向白宫表示需为战事\"寻找出口\"，弹药库存已降至\"危险低位\"；同日，伊朗最高国安委秘书佐尔加德尔开出重开海峡六项条件：永不威胁伊朗、结束侵略、撤军、赔偿战损、解除制裁、解冻资产。"
  },
  {
    "id": "wscn:3778996",
    "domain": "股票",
    "title": "中国7月CPI同比涨幅收窄至0.5%，PPI同比上涨3.5%，AI驱动平板电脑价格环比上涨11.3%",
    "url": "https://wallstreetcn.com/articles/3778996",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T01:31:31+00:00",
    "summary": "7月CPI同比上涨0.5%，涨幅较上月回落0.5个百分点，主要受汽油价格同比涨幅大幅收窄（16个百分点）影响。7月CPI环比下降0.1%，降幅比上月收窄0.2个百分点。PPI同比上涨3.5%，涨幅较上月回落0.6个百分点。国际大宗商品价格波动向国内石油、有色金属等上游行业传导，叠加高温、台风等天气因素压制建材和建筑需求，PPI环比降幅较上月扩大0.4个百分点至0.7%。"
  },
  {
    "id": "wscn:3778995",
    "domain": "股票",
    "title": "“新王”登基“三把火”：伯克希尔开始“花钱”了，净买入200亿美元股票",
    "url": "https://wallstreetcn.com/articles/3778995",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-09T01:15:28+00:00",
    "summary": "二季度，伯克希尔净买入200亿美元股票，终结巴菲特持续三年多的净卖出态势，斥资45亿美元回购自身股票，并以68亿美元收购房屋建筑商Taylor Morrison，为公司近年来规模最大并购交易之一。现金储备降至3647亿美元，为四年来首次环比下降。Abel“果断行动”的承诺，正加速兑现。"
  },
  {
    "id": "wscn:3778993",
    "domain": "股票",
    "title": "伯克希尔Q2净利润翻倍，单季回购规模创5年来最大，谷歌进入前五大持仓 | 财报见闻",
    "url": "https://wallstreetcn.com/articles/3778993",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T13:12:23+00:00",
    "summary": "二季度伯克希尔斥资45.27亿美元回购自家股票，而一季度的回购规模仅约2.35亿美元。截至6月30日，伯克希尔第二季度的现金储备下降至3655亿美元，同期股票净买入额达到近200亿美元，而上半年净买入约116亿美元。还有两笔体量可观的实体收购，进一步拉低了现金储备。这表明，首席执行官Greg Abel正在将公司更多的巨额现金储备投入使用。"
  },
  {
    "id": "wscn:3778945",
    "domain": "股票",
    "title": "磷化铟是下一个“稀土”？关键产业如何成为反制核心，卡住美国光通信的脖子？",
    "url": "https://wallstreetcn.com/premium/articles/3778945?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T10:51:25+00:00",
    "summary": "出口管制×AI算力需求×供给刚性——三重逻辑叠加下，市场为何在交易磷化铟的反制价值？"
  },
  {
    "id": "wscn:3778992",
    "domain": "股票",
    "title": "苹果终于把千问接进Siri：中国版Apple Intelligence来了",
    "url": "https://wallstreetcn.com/articles/3778992",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T09:13:58+00:00",
    "summary": "这意味着中国AI公司第一次真正走进了苹果的系统级AI入口。对千问来说，这可能比出现在iPhone里更重要。"
  },
  {
    "id": "wscn:3778500",
    "domain": "股票",
    "title": "有色乘风起：地缘和利率仅是表象，供给短缺锚定三重驱动力",
    "url": "https://wallstreetcn.com/premium/articles/3778500?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T06:20:39+00:00",
    "summary": "下半年有色金属有望进入\"供给刚性锚定价格底部、三重需求驱动力（AI基建、能源转型、央行购金）打开向上空间\"的新阶段。"
  },
  {
    "id": "wscn:3778990",
    "domain": "股票",
    "title": "AI应用公司毛利故事遭遇首次\"体检\"：Canva主动降速、Figma自吞推理成本",
    "url": "https://wallstreetcn.com/articles/3778990",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T04:07:53+00:00",
    "summary": "Canva与Figma的遭遇揭示了AI应用公司的普遍困境：高昂的推理成本正严重侵蚀毛利，破坏单位经济模型。为控成本，Canva主动暂缓AI铺开致营收降速；Figma因免费测试自担成本致股价重挫。两者均寄望自研模型破局，但AI盈利路径仍待时间验证。"
  },
  {
    "id": "wscn:3778989",
    "domain": "股票",
    "title": "Agentic AI新趋势：亚马逊AWS出现“CPU短缺”",
    "url": "https://wallstreetcn.com/articles/3778989",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T03:48:10+00:00",
    "summary": "AWS高管今年5月警示工程师须节省算力资源，内部CPU等待时间从数小时延长至数天。核心驱动力是Agentic AI大规模应用导致CPU需求激增。此外，英特尔数据显示CPU与GPU使用比例已从1:4升至近1:1。这预示着云计算成本或将面临上涨压力。"
  },
  {
    "id": "wscn:3778988",
    "domain": "股票",
    "title": "英伟达盯上OpenAI“星际之门”背后的电力商，30亿美元直接入股",
    "url": "https://wallstreetcn.com/articles/3778988",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T03:32:42+00:00",
    "summary": "据报道，英伟达计划向电力基础设施商Lancium投资最高30亿美元（初始20亿美元获约20%股权，追加后升至约30%），后者是OpenAI\"星际之门\"AI园区的电力供应商，已在德克萨斯锁定4吉瓦电力资源。"
  },
  {
    "id": "wscn:3778948",
    "domain": "股票",
    "title": "更多缩表、更少加息：沃什如何重塑市场加息预期？",
    "url": "https://wallstreetcn.com/premium/articles/3778948?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T03:19:49+00:00",
    "summary": "沃什推动更多缩表、更少加息，重塑市场定价货币政策逻辑。尽管7月就业大奖，信誉压力下，9月份或成年内唯一加息窗口。"
  },
  {
    "id": "wscn:3778987",
    "domain": "股票",
    "title": "油价刺激通胀、就业削弱加息--黄金“双面得利”",
    "url": "https://wallstreetcn.com/articles/3778987",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T02:59:24+00:00",
    "summary": "地缘局势致油价震荡，推升通胀预期，激活黄金保值避险需求； 美国7月非农就业意外疲软，重创加息预期，致美债收益率与美元双跌。两股力量叠加，推动黄金录得七个月来最佳单周表现。此外ETF买盘同步回暖——自7月20日以来，黄金ETF持仓总量已增加约24吨。"
  },
  {
    "id": "wscn:3778986",
    "domain": "股票",
    "title": "日元只是暂时稳住，中期选举后怎么办？",
    "url": "https://wallstreetcn.com/articles/3778986",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T02:35:45+00:00",
    "summary": "前华尔街基金经理Ed Dowd认为，此次干预时机与中期选举高度吻合，核心目的是阻止日本抛售逾1万亿美元美债、压制美债收益率飙升，避免选前经济动荡损害执政党利益。但美日利差等结构性矛盾未解，选举后政治护盘动力消退，日元恐再度走弱，市场将面临更严峻考验。"
  },
  {
    "id": "wscn:3778985",
    "domain": "股票",
    "title": "AAOI业绩爆了，带飞整个光通信",
    "url": "https://wallstreetcn.com/articles/3778985",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T01:50:50+00:00",
    "summary": "AAOI二季度营收同比增长86%至1.919亿美元，数据中心业务首破亿元，带动Coherent、Lumentum、康宁等光通信股集体大涨。分析师认为，AAOI的超预期表现，对同样深度布局AI数据中心光互联的Lumentum和Coherent构成利好预示——两家公司均将于下周公布财报。"
  },
  {
    "id": "wscn:3778984",
    "domain": "股票",
    "title": "爆仓之后，资本反而扑向\"AI股神\"",
    "url": "https://wallstreetcn.com/articles/3778984",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T01:25:01+00:00",
    "summary": "大批硅谷投资者主动联系基金，表达追加投资意愿。红杉资本合伙人Pat Grady公开表态：\"他将长期是硅谷的重要人物\"，挫折反强化了其“英雄人设。风投人Elad Gil宣布首次申请投资该基金。”而华尔街视其为杠杆过度的经典教训，更强调保全本金与严格的风控管理。"
  },
  {
    "id": "wscn:3778983",
    "domain": "股票",
    "title": "“AI应用龙头”归来！Palantir创2024年以来“最强单周表现”",
    "url": "https://wallstreetcn.com/articles/3778983",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-08T00:59:31+00:00",
    "summary": "核心驱动力为二季度Palantir美国商业业务爆发式增长——同比增149%，合同总价值突破20亿美元。市场叙事从\"AI输家\"逆转为\"AI赢家\"，其\"主权AI\"差异化定位获机构认可，德意志银行随即将评级上调至\"买入\"。"
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
    "id": "hn:49215292",
    "domain": "金融",
    "title": "Mykhailo Fedorov reveals struggle to secure Patriot missiles and Western support",
    "url": "https://www.uawire.org/former-ukrainian-defense-minister-mykhailo-fedorov-reveals-struggles-to-secure-patriot-missiles-and-western-support",
    "source": "greedo",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-08-07T19:38:05+00:00",
    "summary": ""
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
  },
  {
    "id": "hn:49033778",
    "domain": "金融",
    "title": "Reality Bites Elon Musk and His Tesla, SpaceX Believers",
    "url": "https://www.wsj.com/finance/stocks/reality-bites-elon-musk-and-his-tesla-spacex-believers-1b639591",
    "source": "doener",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-07-24T10:59:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49028304",
    "domain": "金融",
    "title": "US announces double-digit tariffs on most of globe to replace expiring duties",
    "url": "https://finance.yahoo.com/economy/policy/article/trump-administration-announces-the-next-phase-of-global-tariffs-with-10-to-125-rates-on-much-of-the-globe-210032314.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-07-23T21:28:52+00:00",
    "summary": ""
  }
]
```
