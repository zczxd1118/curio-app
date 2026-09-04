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

- 今日日期：`2026-09-04`
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
  "date": "2026-09-04",
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
    "points": 4433726,
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
    "points": 1822112,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1803744,
    "published_at": "2026-04-22T09:02:25+00:00",
    "summary": "本期视频因为白菜要毕业了，up伤心过度导致了拖更（）"
  },
  {
    "id": "bvid:BV14rzQB9EJj",
    "domain": "AI",
    "title": "Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill / Hook / 图片 / 上下文处理/ 后台任务",
    "url": "http://www.bilibili.com/video/av115954889596221",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1298232,
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
    "points": 1238933,
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
    "points": 1154665,
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
    "points": 701087,
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
    "points": 698346,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 672831,
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
    "points": 659039,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1BFouBYERu",
    "domain": "AI",
    "title": "手把手教你在Claude Code中熟练使用SKILL技能！",
    "url": "http://www.bilibili.com/video/av116453927814340",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 424436,
    "published_at": "2026-04-23T12:09:57+00:00",
    "summary": "本期视频耗时半个月制作，希望大家能够点赞三连加关注，感谢！\n\n内容包括了一下几个方面：\n00:27 Skill简介\n01:39 Skill和Plugin的区别\n02:51 安装他人的Skill\n04:44 手动创建自己的SKill\n07:30 控制Skill的触发行为\n08:01 Skill的查看和管理\n08:20 Skill的停用和删除\n08:55 找优质Skill的三种渠道"
  },
  {
    "id": "bvid:BV16Luq6FEmP",
    "domain": "AI",
    "title": "当不懂代码的老婆，第一次接触vibe coding……",
    "url": "http://www.bilibili.com/video/av117076211536327",
    "source": "糖果果的未来要发光",
    "platform": "bilibili",
    "points": 339796,
    "published_at": "2026-08-11T09:50:27+00:00",
    "summary": "当不懂代码的老婆，第一次接触vibe coding……"
  },
  {
    "id": "bvid:BV16zDfBtECQ",
    "domain": "AI",
    "title": "为什么越来越多的人抛弃 MCP，转向 CLI？",
    "url": "http://www.bilibili.com/video/av116377675373297",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 329766,
    "published_at": "2026-04-10T01:10:33+00:00",
    "summary": "为什么越来越多的人抛弃 MCP，转向 CLI？#modelcontextprotocol #cli #agent #ai #llm #token #openclaw"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 280391,
    "published_at": "2025-04-15T00:59:13+00:00",
    "summary": "MCP终极指南 - 带你深入掌握MCP（基础篇）\n\n时间轴：\n01:05 MCP简要介绍\n02:47 安装 MCP Host（Cline）\n03:15 配置 Cline 用的 API Key\n06:01 第一个 MCP 问题\n06:31 概念解释：MCP Server 和 Tool\n09:13 配置 MCP Server\n14:19 使用 MCP Server\n15:24 MCP 交互流程详解\n1"
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 280195,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1hM8X6kEso",
    "domain": "AI",
    "title": "一个月6度电、营业额4.5W+，我把工作室的MacMini变成了24小时运作的AI服务器…",
    "url": "http://www.bilibili.com/video/av117159493637308",
    "source": "小宇Boi",
    "platform": "bilibili",
    "points": 274291,
    "published_at": "2026-08-26T02:53:09+00:00",
    "summary": "一台 Mac mini，如何变成 24 小时在线的本地 AI 服务器？本期视频小宇将带你完成基础设置，并部署 Hermes、Docker、UU 远程和 Tailscale，解锁远程办公与 AI 自动化！"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 266694,
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
    "points": 253713,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1e3t4etExj",
    "domain": "AI",
    "title": "手摸手的AI编程cursor实战【小白教程】",
    "url": "http://www.bilibili.com/video/av113148447169565",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 235583,
    "published_at": "2024-09-17T01:00:00+00:00",
    "summary": "喜欢的朋友可以三连+关注～这对我真的很重要"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 229102,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1Zgud6LEoh",
    "domain": "AI",
    "title": "【最新版】小白速通 Codex 教程（含 DeepSeek 接入，无需 ChatGPT 订阅）",
    "url": "http://www.bilibili.com/video/av117070826047031",
    "source": "林粒粒呀",
    "platform": "bilibili",
    "points": 212738,
    "published_at": "2026-08-10T10:54:20+00:00",
    "summary": "Codex 安装 + 上手速通，保姆级教程！\n无需 ChatGPT 订阅，国内直连 DeepSeek"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 180546,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 180088,
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
    "points": 158502,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1nyVDzaE1x",
    "domain": "AI",
    "title": "8分钟教会你写 MCP",
    "url": "http://www.bilibili.com/video/av114480138686354",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 154781,
    "published_at": "2025-05-15T09:00:00+00:00",
    "summary": "10分钟讲清楚 Prompt, Agent, MCP 是什么: https://www.bilibili.com/video/BV1aeLqzUE6L\n让uv管理Python的一切: https://www.bilibili.com/video/BV1Stwfe1E7s/\n\ndemo code: https://gist.github.com/cradiator/76629158bec214036"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 107127,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 99895,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93557,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54765,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1sZMq6qEko",
    "domain": "AI",
    "title": "从0做出你的第一个App ｜ 零基础AI编程保姆教程",
    "url": "http://www.bilibili.com/video/av117038647352026",
    "source": "木子不写代码",
    "platform": "bilibili",
    "points": 54263,
    "published_at": "2026-08-07T12:15:00+00:00",
    "summary": "这期视频，我会手把手带你，用 AI 做出你的第一个 App。\n全程假设你没有任何编程和AI的基础，\n我们从如何写需求提示词开始，\n到确定页面结构和设计，\n产品需求文档，\n开发计划，\n第一版APP验收，\ngit代码存档，\n二次开发，\n界面美化，\n做好的APP也会开源给到大家，\n我也会演示如何获取这个项目源代码并且用AI继续定制开发，\n视频到最后，\n你会收获一个为自己的工作和生活定制的专属APP！\n和"
  },
  {
    "id": "bvid:BV1vbHnecEq7",
    "domain": "AI",
    "title": "Manim + Cursor：用AI做 3Blue1Brown 风格动画",
    "url": "http://www.bilibili.com/video/av113071439873010",
    "source": "kate人不错",
    "platform": "bilibili",
    "points": 46198,
    "published_at": "2024-09-03T03:22:44+00:00",
    "summary": "本视频介绍了Manim，这是一个能创建各种数学动画和可视化内容的工具（但它的用途不仅限于数学动画）。视频展示了多个用Manim制作的动画示例，并详细讲解了其基本用法，涵盖从简单图形到复杂函数和公式展示的内容。此外，视频还介绍了如何与Cursor联动使用。最后，视频推荐了Replit平台作为Manim的在线使用环境，并分享了一些使用技巧和更多学习资源。\n\n时间戳：\n0:00 Manim简介\n2:08"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 41382,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30468,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1WwD9BEES7",
    "domain": "AI",
    "title": "保姆级ClaudeCode从0到1完整实战项目",
    "url": "http://www.bilibili.com/video/av116391835343750",
    "source": "是茂宇呀",
    "platform": "bilibili",
    "points": 29388,
    "published_at": "2026-04-12T12:59:04+00:00",
    "summary": "花了两天录制了这个教程帮助到家从0到1的完整做一个项目并带大家入门，项目中用到的相关提示词及文档教我都分享了在了www.maoyu.site"
  },
  {
    "id": "bvid:BV1C3jt64EPS",
    "domain": "AI",
    "title": "B站讲的最好的Vibe Coding企业级项目实战教程（2026最新版）从入门到进阶，七天速通Claude Code+Codex+CursorAI工程化编程开发",
    "url": "http://www.bilibili.com/video/av116787425383675",
    "source": "图灵学院诸葛",
    "platform": "bilibili",
    "points": 25555,
    "published_at": "2026-06-21T09:48:04+00:00",
    "summary": "制作不易，大家喜欢视频记得点点关注，一键三连呀【点赞、投币、收藏】感谢支持！\n 【本视频笔记代码、大模型最新学习路线、系统学习课程、实战案例、电子书+问题解答等戳这里获取→https://www.bilibili.com/read/cv39576966/?jump_opus=1】"
  },
  {
    "id": "bvid:BV1dZud6VE5G",
    "domain": "AI",
    "title": "【AI实战】AI Agent智能教务排课与教学质量分析系统，基于SpringAI+Springboot+Agent的教务排课系统，教学质量分析系统",
    "url": "http://www.bilibili.com/video/av117070104692483",
    "source": "武哥聊编程",
    "platform": "bilibili",
    "points": 24804,
    "published_at": "2026-08-10T07:48:01+00:00",
    "summary": "完整资料：https://aigcbaba.com/course/98"
  },
  {
    "id": "bvid:BV1UR416jERL",
    "domain": "AI",
    "title": "不稳定服务器的统治第二季：一口气看完！！！",
    "url": "http://www.bilibili.com/video/av117179206868262",
    "source": "我的世界_枷锁",
    "platform": "bilibili",
    "points": 23505,
    "published_at": "2026-08-30T00:00:00+00:00",
    "summary": "喜欢的点点关注哟~~"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 23514,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1B97868EZK",
    "domain": "AI",
    "title": "Claude Code全流程开发实战丨MCP实战、Skills+Agent多工具协作、AI编程、自动化工作流、私有化部署、转行AI岗",
    "url": "http://www.bilibili.com/video/av116810192131401",
    "source": "博学谷",
    "platform": "bilibili",
    "points": 21675,
    "published_at": "2026-06-25T10:11:09+00:00",
    "summary": "视频配套资源领取方式戳：https://www.bilibili.com/opus/1217780115004456969\n或关注【博学谷】公综号回复关键词领取：260625\n学完本课程，你将能够独立完成AI Agent 研发与落地：深度掌握 Claude Code 辅助编程、Skill 技能包编排与 MCP 协议集成打通私有系统连接的“桥梁”，并能学会私有化部署。最终凭借“AI Coding 重"
  },
  {
    "id": "bvid:BV1HmojYNE76",
    "domain": "AI",
    "title": "15分钟Java快速构建MCP Server",
    "url": "http://www.bilibili.com/video/av114337213647750",
    "source": "有趣程序员的boredlife",
    "platform": "bilibili",
    "points": 18211,
    "published_at": "2025-04-14T16:26:09+00:00",
    "summary": "15分钟Java快速构建MCP Server"
  },
  {
    "id": "bvid:BV1htCnY4ET6",
    "domain": "AI",
    "title": "用 Cursor AI 写 flutter 直接喂设计图就行 | flutter教程",
    "url": "http://www.bilibili.com/video/av113723805008238",
    "source": "独立开发者_猫哥",
    "platform": "bilibili",
    "points": 18023,
    "published_at": "2024-12-27T08:21:35+00:00",
    "summary": "✏️【关于本期视频】\n在上一篇文章《Flutter 使用 Cursor 和 Figma 快速生成界面代码》中，有同学提到他直接使用了设计稿的图片进行生成。我试了一下，效果确实很好。因此，我整理了一些文档，希望对大家有所帮助。\n下图展示了我没有手动编写任何代码实现的消息首页，支持上下滑动刷新数据。\n👉 文档 https://ducafecat.com/blog/use-cursor-ai-flutt"
  },
  {
    "id": "bvid:BV1k73y6fEDx",
    "domain": "AI",
    "title": "【ClaudeCode】这绝对是b站讲的最好的Claude Code保姆级全套教程，2026最新版，包含所有干货！七天就能从小白到大神！学完即就业，玩转AI技术",
    "url": "http://www.bilibili.com/video/av117001821488596",
    "source": "爬虫逆向",
    "platform": "bilibili",
    "points": 17120,
    "published_at": "2026-07-29T07:25:00+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！"
  },
  {
    "id": "bvid:BV1rSKU6RE4i",
    "domain": "AI",
    "title": "【快速入门】目前B站讲的最好的CurSor AI编程完整实战教程，环境配置+智能编码+多行业项目实战一次学会！新手小白也能看懂，刷到就是赚到！",
    "url": "http://www.bilibili.com/video/av116832707090068",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 15567,
    "published_at": "2026-06-29T09:39:35+00:00",
    "summary": "一路整理了很多AI大模型干货资源，都是亲身筛选过的，帮大家避开弯路、省去自己摸索的麻烦。真心祝大家学业事业都一路顺利！用心整理内容不容易，觉得有用就留个三连+关注，后续持续分享更多实用干货！\n1️⃣ 大模型入门学习路线图（附学习资源） \n2️⃣ 大模型方向必读书籍PDF版 \n3️⃣ 大模型面试题库 \n4️⃣ 大模型项目源码 \n5️⃣ 超详细海量大模型LLM实战项目 \n6️⃣ Langchain/R"
  },
  {
    "id": "bvid:BV1eMgG6QEeG",
    "domain": "AI",
    "title": "【吴恩达】这绝对是把《Vibe Coding》讲得最通透的一套课！手把手教你构建自己的企业级AI工作流，学完直接落地！——附带课件代码",
    "url": "http://www.bilibili.com/video/av117081815189025",
    "source": "吴恩达Agents",
    "platform": "bilibili",
    "points": 15317,
    "published_at": "2026-08-12T09:29:57+00:00",
    "summary": "Vibe Coding火了，但你会发现——AI写的代码像开盲盒，今天能跑明天崩，项目一大就乱套。\n规范驱动开发（SDD） 就是来解决这个问题的。它的核心理念很简单：在让AI写代码之前，先和AI在统一的规范文档里对齐需求，把开发变成可预测、可追溯、可控制的过程。"
  },
  {
    "id": "bvid:BV1Tz8g6HErC",
    "domain": "AI",
    "title": "【全748集】B站最全最细的AI Agent零基础入门教程，2026最新版，教学通俗易懂，小白适用！普通人也能抓住的AI风口！手把手教会你agent智能体搭建~",
    "url": "http://www.bilibili.com/video/av117115201789701",
    "source": "AI全栈开发",
    "platform": "bilibili",
    "points": 13951,
    "published_at": "2026-08-18T11:27:05+00:00",
    "summary": "【2026最新版AI Agent智能体零基础全套教程 | 配套源码+学习路线+项目案例，看置顶评论自取】\n本套教程专为零基础设计，从Agent原理到独立打造智能体，手把手带你系统掌握AI Agent智能体搭建。\n✅ Agent基础：什么是Agent、三大核心能力（规划/工具/记忆）\n✅ 主流框架：Langchain、LangGraph主流框架\n✅ 多Agent协作：A2A协议、任务编排与调度\n✅ "
  },
  {
    "id": "bvid:BV18j5DzyEmD",
    "domain": "AI",
    "title": "Cursor-AI编程完整版入门教程",
    "url": "http://www.bilibili.com/video/av114379827713362",
    "source": "SiKi老师",
    "platform": "bilibili",
    "points": 12877,
    "published_at": "2025-04-22T11:00:00+00:00",
    "summary": "更多编程教程请访问我们官网www.sikiedu.com\n\nHi，我是SiKi老师，这个课程里面老师会带着大家学习使用全球目前最火的AI编程工具-Cursor的使用。\n\n教学内容：\n1、Cursor的下载和安装\n2、Cursor的基本设置\n3、使用Cursor开发贪吃蛇游戏\n4、使用Cursor开发一个博客网站\n5、Trae（字节旗下AI编程工具）的使用初体验"
  },
  {
    "id": "bvid:BV1n9g36wEiZ",
    "domain": "AI",
    "title": "5分钟教会你，什么是agent？",
    "url": "http://www.bilibili.com/video/av117097082392253",
    "source": "开聊",
    "platform": "bilibili",
    "points": 12647,
    "published_at": "2026-08-15T02:12:34+00:00",
    "summary": "呵呵，多评论。"
  },
  {
    "id": "bvid:BV1RCqPBFEDq",
    "domain": "AI",
    "title": "使用 Claude Code 从零到一开发项目",
    "url": "http://www.bilibili.com/video/av115848605932169",
    "source": "AgenticX",
    "platform": "bilibili",
    "points": 11817,
    "published_at": "2026-01-06T14:33:59+00:00",
    "summary": "我过去启动 Claude Code 项目的方式完全错误：只是简单输入 “claude”，然后毫无规划、毫无准备、毫无系统地自由发挥式提示——这就好比不画蓝图就直接盖房子。\n过去一年中，我用 Claude Code 构建了数十个项目，最终总结出一套简洁的三阶段系统（PSB：Plan-规划、Setup-设置、Build-构建），让每个项目从第一天起就轻松十倍。\n本视频中，我将分享自己每次启动新 Cla"
  },
  {
    "id": "bvid:BV1wyuy6WEKx",
    "domain": "AI",
    "title": "一口气带你看完Ai服务器的工作原理！",
    "url": "http://www.bilibili.com/video/av117064517812350",
    "source": "丰铭科学解说",
    "platform": "bilibili",
    "points": 11676,
    "published_at": "2026-08-10T01:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1Q4NczHEwg",
    "domain": "AI",
    "title": "Anthropic《Claude Code 实战 | Claude Code in Action》中英字幕",
    "url": "http://www.bilibili.com/video/av116203729259669",
    "source": "GPT中英字幕课程资源",
    "platform": "bilibili",
    "points": 11221,
    "published_at": "2026-03-14T00:00:00+00:00",
    "summary": "https://anthropic.skilljar.com/claude-code-in-action"
  },
  {
    "id": "hn:49458161",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia agrees to acquire Hugging Face for $13B",
    "url": "https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 1982,
    "published_at": "2026-08-27T01:12:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49434378",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI Jalapeño: Better than Nvidia Blackwell",
    "url": "https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia",
    "source": "bmulholland",
    "platform": "hackernews",
    "points": 584,
    "published_at": "2026-08-25T14:06:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:49548952",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia to acquire Hugging Face",
    "url": "https://www.cnbc.com/2026/09/03/nvidia-agrees-to-buy-hugging-face-for-almost-13-billion-ai-expansion.html",
    "source": "tosh",
    "platform": "hackernews",
    "points": 309,
    "published_at": "2026-09-03T12:10:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49466052",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia projects $673B in sales as AI demand widens",
    "url": "https://forgeeks.net/nvidia-673-billion-ai-growth-forecast/",
    "source": "kuuuzya",
    "platform": "hackernews",
    "points": 111,
    "published_at": "2026-08-27T15:04:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49552375",
    "domain": "AI 算力 / 半导体",
    "title": "Texas Data Center Map: See where data centers are operating or planned",
    "url": "https://www.kxan.com/news/texas/texas-data-center-tracker-see-where-600-projects-are-operating-or-planned-across-state-in-interactive-map/",
    "source": "simonpure",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-09-03T16:10:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:49469249",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Starts Pac as AI Chip Maker Builds DC Influence Force",
    "url": "https://news.bgov.com/bloomberg-government-news/nvidia-starts-a-pac-as-ai-chip-maker-buids-influence-force-in-dc",
    "source": "rarisma",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-08-27T18:34:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49557813",
    "domain": "AI 算力 / 半导体",
    "title": "Tell HN: NVIDIA's Acquisition of HuggingFace was for $HuggingFace",
    "url": "https://news.ycombinator.com/item?id=49557813",
    "source": "MontagFTB",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-09-03T22:08:41+00:00",
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
    "id": "rss:https://www.eetimes.com/when-the-package-becomes-an-electrical-design-variable/",
    "domain": "AI 算力 / 半导体",
    "title": "When the Package Becomes an Electrical Design Variable",
    "url": "https://www.eetimes.com/when-the-package-becomes-an-electrical-design-variable/",
    "source": "Takaki Murata",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T07:50:10+00:00",
    "summary": "AI power integrity now lives inside the package, not just the PCB. Treat chip, package, and board as one PDN. The post When the Package Becomes an Electrical Design Variable appeared first on EE Times"
  },
  {
    "id": "rss:https://www.eetimes.com/7-steps-to-take-now-meet-the-eu-cra-9-11-26-reporting-deadline/",
    "domain": "AI 算力 / 半导体",
    "title": "7 Steps to Take Now: Meet the EU CRA 9/11/26 Reporting Deadline",
    "url": "https://www.eetimes.com/7-steps-to-take-now-meet-the-eu-cra-9-11-26-reporting-deadline/",
    "source": "By Colin Duggan, CEO and co-founder, BG Networks",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:31:18+00:00",
    "summary": "Prepare for the EU Cyber Resilience Act's September 2026 reporting deadline; follow these seven steps to ensure compliance and readiness. The post 7 Steps to Take Now: Meet the EU CRA 9/11/26 Reportin"
  },
  {
    "id": "rss:https://www.eetimes.com/techworks-aligns-u-k-semiconductors-under-uksia-umbrella/",
    "domain": "AI 算力 / 半导体",
    "title": "TechWorks Aligns U.K. Semiconductors Under UKSIA Umbrella",
    "url": "https://www.eetimes.com/techworks-aligns-u-k-semiconductors-under-uksia-umbrella/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T13:46:01+00:00",
    "summary": "TechWorks corrals U.K. chip groups under UKSIA as funding surges 65% and 700 execs swarm London. The post TechWorks Aligns U.K. Semiconductors Under UKSIA Umbrella appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/display-developments-challenge-controllers/",
    "domain": "AI 算力 / 半导体",
    "title": "Display Developments Challenge Controllers",
    "url": "https://www.eetimes.com/display-developments-challenge-controllers/",
    "source": "Teng Tang Yang, Senior Division Director of Product Marketing Division, UMC",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T13:00:00+00:00",
    "summary": "Discover how AMOLED, micro-OLED and advanced DDIC technologies are transforming displays with higher resolution, lower power and immersive experiences. The post Display Developments Challenge Controll"
  },
  {
    "id": "rss:https://www.eetimes.com/indias-quantum-journey-goes-beyond-the-qubit/",
    "domain": "AI 算力 / 半导体",
    "title": "India’s Quantum Journey Goes Beyond the Qubit",
    "url": "https://www.eetimes.com/indias-quantum-journey-goes-beyond-the-qubit/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T08:00:47+00:00",
    "summary": "IBM’s Amaravati deployment could accelerate India’s quantum ecosystem as startups develop processors, software, and supporting technologies. The post India’s Quantum Journey Goes Beyond the Qubit appe"
  },
  {
    "id": "rss:https://www.eetimes.com/mercedes-spinout-athos-closes-its-doors/",
    "domain": "AI 算力 / 半导体",
    "title": "Mercedes Spinout Athos Closes Its Doors",
    "url": "https://www.eetimes.com/mercedes-spinout-athos-closes-its-doors/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T17:07:04+00:00",
    "summary": "The startup was unable to secure the financing required to continue commercialising its chiplet-based technology The post Mercedes Spinout Athos Closes Its Doors appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/secure-safety-security-communications-cut-time-complexity-and-install-cost/",
    "domain": "AI 算力 / 半导体",
    "title": "Secure Safety & Security Communications: Cut Time, Complexity, and Install Cost",
    "url": "https://www.eetimes.com/secure-safety-security-communications-cut-time-complexity-and-install-cost/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:21:11+00:00",
    "summary": "Join this webinar, where we will demonstrate how to enable next-generation security and building safety networks while reducing wiring complexity, improving fault detection, and much more. The post Se"
  },
  {
    "id": "rss:https://www.eetimes.com/astella-joins-5g-acia-shanghai-to-advance-industrial-5g-and-iiot-innovation/",
    "domain": "AI 算力 / 半导体",
    "title": "Astella Joins 5G-ACIA Shanghai to Advance Industrial 5G and IIoT Innovation",
    "url": "https://www.eetimes.com/astella-joins-5g-acia-shanghai-to-advance-industrial-5g-and-iiot-innovation/",
    "source": "Astella Technologies Limited",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:19:21+00:00",
    "summary": "Astella announces its participation in the 5G-ACIA Industrial 5G Day in Shanghai, a dedicated industry event focused on Industrial 5G. The post Astella Joins 5G-ACIA Shanghai to Advance Industrial 5G "
  },
  {
    "id": "rss:https://www.eetimes.com/manufacturing-growth-slows-in-august-amid-supply-and-cost-strains/",
    "domain": "AI 算力 / 半导体",
    "title": "Manufacturing Growth Slows in August Amid Supply and Cost Strains",
    "url": "https://www.eetimes.com/manufacturing-growth-slows-in-august-amid-supply-and-cost-strains/",
    "source": "News Desk",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:00:00+00:00",
    "summary": "U.S. manufacturing growth continued for the eighth consecutive month in August, though momentum slowed due to supply chain and cost pressures. The post Manufacturing Growth Slows in August Amid Supply"
  },
  {
    "id": "rss:https://www.eetimes.com/indian-startup-hrdwyr-builds-ai-native-socs-for-the-physical-world/",
    "domain": "AI 算力 / 半导体",
    "title": "Indian Startup HrdWyr Builds AI-Native SoCs for the Physical World",
    "url": "https://www.eetimes.com/indian-startup-hrdwyr-builds-ai-native-socs-for-the-physical-world/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T08:00:00+00:00",
    "summary": "HrdWyr is developing AI-native SoCs for power management, motor control, and other applications where AI meets physical systems. The post Indian Startup HrdWyr Builds AI-Native SoCs for the Physical W"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/external-ssds/lexar-announces-worlds-thinnest-portable-ssd-in-celebration-of-the-brands-30th-anniversary-lexar-muse-drive-achieves-0-15-inch-thickness-with-proprietary-pogo-pin-cable-magnetic-sleeve-for-phone-mounting",
    "domain": "AI 算力 / 半导体",
    "title": "Lexar announces ‘world’s thinnest portable SSD’ in celebration of the brand’s 30th anniversary – Lexar Muse drive achieves 0.15-inch thickness with proprietary pogo-pin cable, magnetic sleeve for phon",
    "url": "https://www.tomshardware.com/pc-components/external-ssds/lexar-announces-worlds-thinnest-portable-ssd-in-celebration-of-the-brands-30th-anniversary-lexar-muse-drive-achieves-0-15-inch-thickness-with-proprietary-pogo-pin-cable-magnetic-sleeve-for-phone-mounting",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T07:00:00+00:00",
    "summary": "Lexar’s slimmest-ever Muse drive aims for a barely there design that magnetically attaches to your iPhone for recording directly on the drive. But to achieve its petite 80×48×3.8 mm dimensions, it use"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-acquires-hugging-face-for-usd12-93-billion-company-gains-control-of-major-ai-model-distribution-platform",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia acquires Hugging Face for $12.93 billion — company gains control of major AI model distribution platform",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-acquires-hugging-face-for-usd12-93-billion-company-gains-control-of-major-ai-model-distribution-platform",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T19:05:37+00:00",
    "summary": "Nvidia expands beyond AI hardware with its $12.93 billion acquisition of Hugging Face, gains control of a major open AI model platform, vows to preserve its support for competing models, clouds, and h"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/lenovo-details-its-rtx-spark-laptops-yoga-pro-9n-and-yoga-9n-2-in-1-get-full-specs-stylus-support",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo details its RTX Spark laptops — Yoga Pro 9n and Yoga 9n 2-in-1 get full specs, stylus support",
    "url": "https://www.tomshardware.com/laptops/lenovo-details-its-rtx-spark-laptops-yoga-pro-9n-and-yoga-9n-2-in-1-get-full-specs-stylus-support",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:00:00+00:00",
    "summary": "Lenovo detailed its RTX Spark laptops ahead of IFA in Berlin, releasing full specs and showing off stylus compatibility."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/lenovos-ideapad-vibe-laptops-stand-out-with-seven-colors-and-swappable-keycaps-14-15-inch-models-with-snapdragon-x-and-amd-ai-400-cpus-to-start-at-usd699",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo’s IdeaPad Vibe laptops stand out with seven colors and swappable keycaps – 14,15-inch models with Snapdragon X and AMD AI 400 CPUs to start at $699",
    "url": "https://www.tomshardware.com/laptops/lenovos-ideapad-vibe-laptops-stand-out-with-seven-colors-and-swappable-keycaps-14-15-inch-models-with-snapdragon-x-and-amd-ai-400-cpus-to-start-at-usd699",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:00:00+00:00",
    "summary": "Lenovo’s latest IdeaPad laptops are all about colorful vibes. The Vibe lineup will come in seven hues, with swappable keyboard keycaps so you can match the chassis or go for a pop of contrast. The 14-"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/lenovo-ditches-fans-in-favor-of-solid-state-airjet-tech-in-super-slim-1-8-pound-aeroblade-laptop-concept-company-also-lands-at-ifa-with-a-14-inch-rollable-screen-notebook-that-expands-to-17-inches",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo ditches fans in favor of solid-state AirJet tech in super-slim, 1.8-pound AeroBlade laptop concept – company also lands at IFA with a 14-inch rollable screen notebook that expands to 17 inches",
    "url": "https://www.tomshardware.com/laptops/lenovo-ditches-fans-in-favor-of-solid-state-airjet-tech-in-super-slim-1-8-pound-aeroblade-laptop-concept-company-also-lands-at-ifa-with-a-14-inch-rollable-screen-notebook-that-expands-to-17-inches",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:00:00+00:00",
    "summary": "Lenovo is rolling out two new laptop concepts at IFA 2026: A 1.83-pound, 0.39-inch-thick AeroBlade using Frore System’s AirJet solid-state cooling tech, and a compact 14-inch rollable-screen portable "
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/nvidias-rtx-spark-n1x-launches-in-october-for-laptops-and-desktops-18-or-20-cpu-cores-paired-with-5-120-or-6-144-cuda-cores-up-to-128gb-of-unified-memory",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's RTX Spark N1X launches in October for laptops and desktops — 18 or 20 CPU cores, paired with 5,120 or6,144 CUDA cores, up to 128GB of unified memory",
    "url": "https://www.tomshardware.com/laptops/nvidias-rtx-spark-n1x-launches-in-october-for-laptops-and-desktops-18-or-20-cpu-cores-paired-with-5-120-or-6-144-cuda-cores-up-to-128gb-of-unified-memory",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:00:00+00:00",
    "summary": "Systems with Nvidia's RTX Spark N1X chips will launch in October in mini PCs and laptops, with the chips coming in two configurations."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-pair-utility-joins-every-gpu-in-your-home-into-a-cluster-for-agentic-ai-tasks-tool-uses-spare-cycles-to-keep-agent-swarms-from-hammering-one-gpu",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia PAIR utility joins every GPU in your home into a cluster for agentic AI tasks — tool uses spare cycles to keep agent swarms from hammering one GPU",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-pair-utility-joins-every-gpu-in-your-home-into-a-cluster-for-agentic-ai-tasks-tool-uses-spare-cycles-to-keep-agent-swarms-from-hammering-one-gpu",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:00:00+00:00",
    "summary": "Nvidia's Personal AI Router (PAIR) clustering utility lets agentic AI workloads take advantage of every spare GPU cycle on a home network, potentially making for faster execution and more private infe"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/lenovo-thinkcentre-x-ultra-packs-gorgon-halo-amd-ryzen-ai-max-pro-495-shows-up-in-mini-workstation",
    "domain": "AI 算力 / 半导体",
    "title": "Lenovo ThinkCentre X Ultra packs Gorgon Halo — AMD Ryzen AI Max+ Pro 495 shows up in mini workstation",
    "url": "https://www.tomshardware.com/laptops/lenovo-thinkcentre-x-ultra-packs-gorgon-halo-amd-ryzen-ai-max-pro-495-shows-up-in-mini-workstation",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:00:00+00:00",
    "summary": "AMD's Gorgon Halo chips are breaking cover. Ahead of IFA, Lenovo showed off the THinkCentre X Ultra with an AMD Ryzen AI Max+ Pro 495."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intels-core-ultra-400-nova-lake-launch-schedule-leaks-out-mass-production-in-q4-first-nova-lake-cpus-in-q1-2027",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's Core Ultra 400 'Nova Lake' launch schedule leaks out — mass production in Q4, first Nova Lake CPUs in Q1 2027",
    "url": "https://www.tomshardware.com/pc-components/cpus/intels-core-ultra-400-nova-lake-launch-schedule-leaks-out-mass-production-in-q4-first-nova-lake-cpus-in-q1-2027",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T15:58:41+00:00",
    "summary": "Intel's Core Ultra 400-series 'Nova Lake-S' CPUs are on track for mass production next quarter, but they will only launch in Q1 2027 with 28-core models coming first."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/how-to-install-a-ps5-ssd-in-2026",
    "domain": "AI 算力 / 半导体",
    "title": "How to install a PS5 SSD in 2026",
    "url": "https://www.tomshardware.com/pc-components/ssds/how-to-install-a-ps5-ssd-in-2026",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T15:30:00+00:00",
    "summary": "Learn how to install an M.2 NVMe SSD in your PlayStation 5, PlayStation 5 Slim, or PlayStation 5 Pro in under five minutes."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/almost-70-percent-of-voters-in-missouri-city-recall-council-member-who-said-yes-to-ai-data-center-tax-breaks-councilor-said-disagreement-over-an-issue-shouldnt-be-enough-to-unseat-him",
    "domain": "AI 算力 / 半导体",
    "title": "Almost 70% of voters in Missouri city vote to recall council member who said yes to AI data center tax breaks — councilor said disagreement over an issue shouldn’t be enough to unseat him",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/almost-70-percent-of-voters-in-missouri-city-recall-council-member-who-said-yes-to-ai-data-center-tax-breaks-councilor-said-disagreement-over-an-issue-shouldnt-be-enough-to-unseat-him",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T14:52:55+00:00",
    "summary": "The people of Independence, Missouri, voted to recall councilor John Perkins after he voted to give a Nebius data center tax breaks amounting to more than $6 billion. Perkins said that a single vote s"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/openai-ceo-sam-altman-says-38-000-chatgpt-queries-use-as-much-water-as-the-production-of-one-almond-says-data-centers-use-no-more-water-than-an-office-building",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI CEO Sam Altman says 38,000 ChatGPT queries use as much water as the production of one almond — says data centers use no more water than an office building",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/openai-ceo-sam-altman-says-38-000-chatgpt-queries-use-as-much-water-as-the-production-of-one-almond-says-data-centers-use-no-more-water-than-an-office-building",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T14:35:53+00:00",
    "summary": "Sam Altman says that a single almond uses up more water than 38,000 ChatGPT queries. He said that the concerns of people about data centers using up so much water are nothing but a \"robust meme,\" and "
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-46-percent-on-pc-hardware-in-amazons-labor-day-2026-sale-huge-discounts-on-tech",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to 46% on PC hardware in Amazon's Labor Day 2026 sale — huge discounts on tech",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-46-percent-on-pc-hardware-in-amazons-labor-day-2026-sale-huge-discounts-on-tech",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T14:29:01+00:00",
    "summary": "Amazon is hosting a Labor Day sale with up to 46% off our favorite tech products."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/benchmarking-31-different-cpus-in-onimusha-way-of-the-sword-x3d-beats-flagships-by-10-percent-270k-plus-falls-behind-raptor-lake-refresh",
    "domain": "AI 算力 / 半导体",
    "title": "Benchmarking 31 different CPUs in Onimusha: Way of the Sword — X3D beats flagships by 10%, 270K Plus falls behind Raptor Lake Refresh",
    "url": "https://www.tomshardware.com/pc-components/cpus/benchmarking-31-different-cpus-in-onimusha-way-of-the-sword-x3d-beats-flagships-by-10-percent-270k-plus-falls-behind-raptor-lake-refresh",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T12:32:30+00:00",
    "summary": "Onimusha: Way of the Sword closes out an excellent year for Capcom. We put the RE Engine to the test once again, benchmarking 31 different CPUs to see how they scale in the game."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-eliminates-fellow-titles-changes-standard-of-technical-leadership-combines-deep-expertise-with-strategic-vision-and-measurable-tactical-progress",
    "domain": "AI 算力 / 半导体",
    "title": "Intel scraps 44-year-old 'Fellow' title for top scientists, changes 'standard of technical leadership' — technical luminaries must now deliver measurable business results, combine deep expertise with ",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-eliminates-fellow-titles-changes-standard-of-technical-leadership-combines-deep-expertise-with-strategic-vision-and-measurable-tactical-progress",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T12:13:44+00:00",
    "summary": "Intel gets rid of hundreds of vice presidents, replaces 'Fellows' with 'distinguished engineers,' changes 'standards of technical leadership.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/rpcs3-emulator-devs-slam-nvidia-dlss-5-as-ai-slop-generator-says-industry-pushing-more-upscalers-and-frame-generation-to-hallucinate-games-and-hide-their-lack-of-optimisation",
    "domain": "AI 算力 / 半导体",
    "title": "RPCS3 emulator devs slam Nvidia DLSS 5 as 'AI-slop generator' — says industry pushing 'more upscalers and frame generation to hallucinate games and hide their lack of optimisation'",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/rpcs3-emulator-devs-slam-nvidia-dlss-5-as-ai-slop-generator-says-industry-pushing-more-upscalers-and-frame-generation-to-hallucinate-games-and-hide-their-lack-of-optimisation",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T12:10:38+00:00",
    "summary": "RPCS3 explains why modern temporal upscalers are difficult to implement in PS3 emulation as modders continue experimenting with the leaked DLSS 5 DLL."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/iconic-packard-bell-brand-rises-from-the-ashes-after-13-years-with-the-dotbook-14-at-ifa-colorful-and-affordable-intel-twin-lake-laptop-is-europe-only-for-now",
    "domain": "AI 算力 / 半导体",
    "title": "Iconic Packard Bell brand rises from the ashes after 13 years with the DotBook 14 at IFA — colorful and affordable Intel Twin Lake laptop is Europe-only, for now",
    "url": "https://www.tomshardware.com/laptops/iconic-packard-bell-brand-rises-from-the-ashes-after-13-years-with-the-dotbook-14-at-ifa-colorful-and-affordable-intel-twin-lake-laptop-is-europe-only-for-now",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T12:03:26+00:00",
    "summary": "Packard Bell is back, under the wing of Acer at IFA 2026, with the Taiwanese PC maker’s unveiling of the colorful Dot family, including a laptop, headphones, input peripherals, and more."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tsmc-fab-equipment-demand-nearly-doubles-in-six-months-ai-surge-pushes-2026-capex-toward-usd64b-amid-tool-shortages",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC fab equipment demand nearly doubles in six months — AI surge pushes 2026 CapEx toward $64B amid tool shortages",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-fab-equipment-demand-nearly-doubles-in-six-months-ai-surge-pushes-2026-capex-toward-usd64b-amid-tool-shortages",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T11:00:00+00:00",
    "summary": "TSMC's equipment requirements have nearly doubled in just eight months as AI demand drives an unprecedented fab expansion, yet its 2026 CapEx budget has risen by only around 15%."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/get-a-ddr5-gaming-pc-with-rtx-5060-ti-for-just-usd1-399-save-21-percent-on-the-intel-core-ultra-7-270k-plus-powered-cyberpower-system",
    "domain": "AI 算力 / 半导体",
    "title": "Get a DDR5 gaming PC with RTX 5060 Ti for just $1,399 — save 21% on the Intel Core Ultra 7 270K Plus-powered CyberPower system",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/get-a-ddr5-gaming-pc-with-rtx-5060-ti-for-just-usd1-399-save-21-percent-on-the-intel-core-ultra-7-270k-plus-powered-cyberpower-system",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T10:55:28+00:00",
    "summary": "Save $370 on a new CyberPower system with Intel Core Ultra 7 270K Plus processor and Nvidia RTX 5060 Ti graphics."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/network-switches/score-a-gigabit-lan-upgrade-for-less-than-usd10-with-this-limited-time-tp-link-switch-deal-plug-and-play-network-upgrade-for-your-home-or-office-unlocks-5-ultra-fast-ethernet-ports-to-help-you-ditch-laggy-wi-fi",
    "domain": "AI 算力 / 半导体",
    "title": "Score a gigabit LAN upgrade for less than $10 with this limited-time TP-Link switch deal — plug-and-play network upgrade for your home or office unlocks 5 ultra-fast Ethernet ports to help you ditch l",
    "url": "https://www.tomshardware.com/networking/network-switches/score-a-gigabit-lan-upgrade-for-less-than-usd10-with-this-limited-time-tp-link-switch-deal-plug-and-play-network-upgrade-for-your-home-or-office-unlocks-5-ultra-fast-ethernet-ports-to-help-you-ditch-laggy-wi-fi",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T10:50:55+00:00",
    "summary": "Grab a 41% saving on this 5-port TP-Link gigabit Ethernet switch, down to only $9.98 for a limited-time only."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/nexus-mods-acquires-steamdb-after-13-years-of-solo-dev-work-promises-no-ads-no-paywalls-and-smarter-mod-update-tracking",
    "domain": "AI 算力 / 半导体",
    "title": "Nexus Mods acquires SteamDB after 13 years of solo dev work — promises no ads, no paywalls, and smarter mod-update tracking",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/nexus-mods-acquires-steamdb-after-13-years-of-solo-dev-work-promises-no-ads-no-paywalls-and-smarter-mod-update-tracking",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T10:30:00+00:00",
    "summary": "Nexus Mods takes in SteamDB under its wing — new owners promise site will remain ad-free and non-paywalled"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/steve-wozniak-signed-apple-1-motherboard-expected-to-achieve-up-to-usd800-000-at-auction-fully-working-board-also-comes-with-a-signed-letter-from-steve-jobs",
    "domain": "AI 算力 / 半导体",
    "title": "Steve Wozniak-signed Apple 1 motherboard expected to achieve up to $800,000 at auction — fully working board also comes with a signed letter from Steve Jobs",
    "url": "https://www.tomshardware.com/desktops/steve-wozniak-signed-apple-1-motherboard-expected-to-achieve-up-to-usd800-000-at-auction-fully-working-board-also-comes-with-a-signed-letter-from-steve-jobs",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T10:15:00+00:00",
    "summary": "A 'beautifully preserved in working condition' Apple-1 computer motherboard signed by Steve Wozniak with a letter signed by Steve Jobs is up for auction next month at Bonhams in New York."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/chinese-supercomputer-manufacturer-reveals-the-worlds-first-64-thread-mobile-workstation-for-ai-domestic-cpu-paired-with-mystery-gpu-with-16gb-of-vram-promises-cloud-level-performance",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese supercomputer manufacturer reveals the 'world's first' 64-thread mobile workstation for AI — homegrown CPU paired with mystery GPU with 16GB of VRAM promises cloud-level performance",
    "url": "https://www.tomshardware.com/laptops/chinese-supercomputer-manufacturer-reveals-the-worlds-first-64-thread-mobile-workstation-for-ai-domestic-cpu-paired-with-mystery-gpu-with-16gb-of-vram-promises-cloud-level-performance",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T10:00:00+00:00",
    "summary": "Sugon has released a teaser of an upcoming mobile workstation with a 64-thread processor and 16GB of VRAM to tackle AI models."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/microsoft-will-expand-windows-11-memory-integrity-feature-to-more-pcs-starting-in-october-security-feature-reduces-gaming-performance-on-some-systems",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft will expand Windows 11 Memory Integrity feature to more PCs starting in October — security feature reduces gaming performance on some systems",
    "url": "https://www.tomshardware.com/software/windows/microsoft-will-expand-windows-11-memory-integrity-feature-to-more-pcs-starting-in-october-security-feature-reduces-gaming-performance-on-some-systems",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T16:07:29+00:00",
    "summary": "Microsoft will begin enabling Memory Integrity by default on more eligible Windows PCs through quality updates in October, expanding kernel-level protection while preserving existing opt-outs for user"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/hybrid-bonding-roadmap-examined",
    "domain": "AI 算力 / 半导体",
    "title": "The current state of Hybrid Bonding in 2026 — TSMC sits at 6 microns and the HBM delay that nobody expected",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/hybrid-bonding-roadmap-examined",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T15:05:41+00:00",
    "summary": "Hybrid bonding, the copper-to-copper joining technique that replaces solder microbumps in 3D chip stacks, is in high-volume production on logic and freshly postponed on memory."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/gopro-to-expand-into-ai-data-centers-after-usd285-million-merger-with-optical-photonics-company-move-to-solve-camera-makers-financial-woes-move-manufacturing-back-into-the-us",
    "domain": "AI 算力 / 半导体",
    "title": "GoPro to expand into AI data centers after $285 million merger with optical-photonics company — move to solve camera maker’s financial woes, move manufacturing back into the US",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/gopro-to-expand-into-ai-data-centers-after-usd285-million-merger-with-optical-photonics-company-move-to-solve-camera-makers-financial-woes-move-manufacturing-back-into-the-us",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T14:43:10+00:00",
    "summary": "GoPro is merging with optical-photonics company Starman Optical in a deal worth at least $285 million. This move will wipe out the company's $92 million outstanding debt, let it start manufacturing it"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/samsung-teases-new-hbm5-with-twice-the-performance-of-hbm4e-ambitious-data-transfer-rates-could-hint-at-4-096-bit-interface",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung teases new HBM5 with twice the performance of HBM4E —ambitious data transfer rates could hint at 4,096-bit interface",
    "url": "https://www.tomshardware.com/pc-components/dram/samsung-teases-new-hbm5-with-twice-the-performance-of-hbm4e-ambitious-data-transfer-rates-could-hint-at-4-096-bit-interface",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T14:38:20+00:00",
    "summary": "Samsung expects HBM5 to deliver 4 TB/s of bandwidth per stack by late 2020s, which will enable AI accelerators with aggregated memory bandwidth of around 100 TB/s."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/russian-hacker-faces-up-to-20-years-in-prison-following-extradition-and-indictment-over-us-phishing-campaign-that-allegedly-infected-80-000-pcs-hacker-stole-victims-data-via-remote-access",
    "domain": "AI 算力 / 半导体",
    "title": "Russian hacker faces up to 20 years in prison, following extradition and indictment over US phishing campaign that allegedly infected 80,000 PCs — hacker stole victims' data via remote access",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/russian-hacker-faces-up-to-20-years-in-prison-following-extradition-and-indictment-over-us-phishing-campaign-that-allegedly-infected-80-000-pcs-hacker-stole-victims-data-via-remote-access",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T14:22:37+00:00",
    "summary": "Russian national faces US charges over a phishing campaign that allegedly infected 80,000 PCs and stole credentials and personal data"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/tape-companies-ship-160-exabytes-of-storage-in-2025-ai-data-demands-drive-unprecedented-data-growth-capacity-shipped-in-q1-2026-rose-57-percent-yoy-driven-by-ai-lto-9-momentum-and-early-lto-10-uptake",
    "domain": "AI 算力 / 半导体",
    "title": "Tape companies ship 160 exabytes of storage in 2025, AI data demands drive 'unprecedented data growth' — capacity shipped in Q1 2026 rose 57% YOY driven by AI, LTO‑9 momentum, and early LTO‑10 uptake",
    "url": "https://www.tomshardware.com/pc-components/storage/tape-companies-ship-160-exabytes-of-storage-in-2025-ai-data-demands-drive-unprecedented-data-growth-capacity-shipped-in-q1-2026-rose-57-percent-yoy-driven-by-ai-lto-9-momentum-and-early-lto-10-uptake",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:24:55+00:00",
    "summary": "Tape storage companies celebrate capacity shipment growth of 57% YOY for Q1 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/we-explored-early-dlss-5-performance-with-community-mods-and-the-limits-of-the-12v-2x6-power-connector-may-hold-it-back-on-the-rtx-5090",
    "domain": "AI 算力 / 半导体",
    "title": "We explored early DLSS 5 performance with community mods — and the limits of the 12V-2x6 power connector may hold it back on the RTX 5090",
    "url": "https://www.tomshardware.com/pc-components/gpus/we-explored-early-dlss-5-performance-with-community-mods-and-the-limits-of-the-12v-2x6-power-connector-may-hold-it-back-on-the-rtx-5090",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T13:21:38+00:00",
    "summary": "DLSS 5 officially releases later this week, but we tested it on the RTX 5090 using community mods to see what kind of performance drop and extra power draw you can expect."
  },
  {
    "id": "hn:49387755",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia AVO scores 100% on the ARC-AGI-3 interactive reasoning benchmark",
    "url": "https://twitter.com/NVIDIAAI/status/2090786258981466231",
    "source": "dsrtslnd23",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-08-21T13:26:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49480449",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Insists It Can Keep Printing Money to Fund the AI Boom",
    "url": "https://www.wsj.com/tech/ai/nvidia-insists-it-can-keep-printing-money-to-fund-the-ai-boom-195e7d5e",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-08-28T15:57:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49537553",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Flash and 3.8 Flash Cyber",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/",
    "source": "bratao",
    "platform": "hackernews",
    "points": 1144,
    "published_at": "2026-09-02T15:12:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49289112",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.7 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 968,
    "published_at": "2026-08-13T17:23:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49184755",
    "domain": "大厂 AI 动态",
    "title": "Changes at Google DeepMind: Demis Hassabis from CEO to Chair, Jeff Dean departs",
    "url": "https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/",
    "source": "colesantiago",
    "platform": "hackernews",
    "points": 867,
    "published_at": "2026-08-05T16:05:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49220126",
    "domain": "大厂 AI 动态",
    "title": "DeepMind's WeatherNext model achieves breakthrough forecasting cyclones",
    "url": "https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/",
    "source": "bhavansig",
    "platform": "hackernews",
    "points": 449,
    "published_at": "2026-08-08T09:18:50+00:00",
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
    "id": "hn:49267928",
    "domain": "大厂 AI 动态",
    "title": "llama.cpp",
    "url": "https://llama.app",
    "source": "kristianpaul",
    "platform": "hackernews",
    "points": 364,
    "published_at": "2026-08-12T04:51:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49467922",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni 1.1 Flash",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/",
    "source": "saretup",
    "platform": "hackernews",
    "points": 296,
    "published_at": "2026-08-27T17:06:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49259339",
    "domain": "大厂 AI 动态",
    "title": "Apple Silicon and macOS VMs: Faster LLM Inference with llama.cpp",
    "url": "https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md",
    "source": "frabonacci",
    "platform": "hackernews",
    "points": 307,
    "published_at": "2026-08-11T14:50:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:49256057",
    "domain": "大厂 AI 动态",
    "title": "What I learned by putting GitHub Copilot behind a MitM proxy",
    "url": "https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm",
    "source": "j0selit0",
    "platform": "hackernews",
    "points": 200,
    "published_at": "2026-08-11T10:40:47+00:00",
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
    "id": "hn:49198583",
    "domain": "大厂 AI 动态",
    "title": "Show HN: The Channels SDK – Bring Any Agent to Any Channel (Slack, MS Teams)",
    "url": "https://github.com/CopilotKit/channels-sdk",
    "source": "davidmckayv",
    "platform": "hackernews",
    "points": 121,
    "published_at": "2026-08-06T16:05:51+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/986960/lexar-muse-ultra-thin-ssd-storage-drive-proprietary-cable",
    "domain": "大厂 AI 动态",
    "title": "Lexar’s Muse is an ultra-slim portable SSD that’s less than 4mm thick",
    "url": "https://www.theverge.com/tech/986960/lexar-muse-ultra-thin-ssd-storage-drive-proprietary-cable",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T07:00:00+00:00",
    "summary": "Following the lead of companies like Xteink, Lexar is the latest to sacrifice a USB-C port in the pursuit of slimming down its hardware. When the Lexar Muse Ultra-Slim Portable SSD launches later this"
  },
  {
    "id": "rss:https://www.theverge.com/tech/989581/aqara-smart-lighting-ifa-2026",
    "domain": "大厂 AI 动态",
    "title": "Aqara goes all in on smart lighting",
    "url": "https://www.theverge.com/tech/989581/aqara-smart-lighting-ifa-2026",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T07:00:00+00:00",
    "summary": "After showing off several smart home firsts at CES, Aqara has returned to IFA with a major lineup of smart lighting compatible with both Zigbee and Thread. One of these new devices is the Floor Lamp T"
  },
  {
    "id": "rss:https://www.theverge.com/tech/989657/rugone-xsnap-7-pro-smartphone-removable-action-camera-rugged-waterproof",
    "domain": "大厂 AI 动态",
    "title": "This rugged phone’s removable camera can survive and capture your extreme adventures",
    "url": "https://www.theverge.com/tech/989657/rugone-xsnap-7-pro-smartphone-removable-action-camera-rugged-waterproof",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T07:00:00+00:00",
    "summary": "RugOne's Xsnap 7 Pro comes with both an IP68 and IP69K rating, meaning the rugged phone can survive intense water blasts and complete submersion for up to 30 minutes. But what really sets the Xsnap 7 "
  },
  {
    "id": "rss:https://www.theverge.com/games/989978/nvidia-dlss-5-rtx-40",
    "domain": "大厂 AI 动态",
    "title": "Nvidia will officially bring DLSS 5 to older GPUs — but won’t give gamers full control",
    "url": "https://www.theverge.com/games/989978/nvidia-dlss-5-rtx-40",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T01:49:25+00:00",
    "summary": "Officially, Nvidia's controversial DLSS 5 AI rendering was supposed to launch this evening with only a single game, only on Nvidia's latest RTX 50 GPUs, and with developers in full control of their ar"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/989501/tesla-cybercab-launch-robotaxi-austin-musk",
    "domain": "大厂 AI 动态",
    "title": "The unusually muted Tesla Cybercab launch",
    "url": "https://www.theverge.com/transportation/989501/tesla-cybercab-launch-robotaxi-austin-musk",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T00:25:06+00:00",
    "summary": "At a private, closed-door event in Austin, Texas today, Tesla officially launched its gilded car of the future: the Cybercab. It's a huge milestone for Elon Musk, who has been hyping the imminent arri"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/989962/steve-ballmer-kawhi-leonard-pablo-torre-finds-out",
    "domain": "大厂 AI 动态",
    "title": "Steve Ballmer got suspended by the NBA because of a podcast and a jumbotron corruption scandal",
    "url": "https://www.theverge.com/entertainment/989962/steve-ballmer-kawhi-leonard-pablo-torre-finds-out",
    "source": "Richard Lawler",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T23:37:37+00:00",
    "summary": "Last September, Steve Ballmer insisted in an ESPN interview that the Clippers weren't involved in a shady-looking $28 million endorsement deal for his star player, Kawhi Leonard, that involved no actu"
  },
  {
    "id": "rss:https://www.theverge.com/tech/988648/ugreen-magflow-pro-magnetic-wireless-power-bank-10k-liquid-cooling",
    "domain": "大厂 AI 动态",
    "title": "You can watch the coolant flow inside Ugreen’s liquid-cooled power bank",
    "url": "https://www.theverge.com/tech/988648/ugreen-magflow-pro-magnetic-wireless-power-bank-10k-liquid-cooling",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T22:00:00+00:00",
    "summary": "Does your power bank have \"CryoPulse technology\" or a \"Cyber Window\"? If you disappointingly answered \"no\" to both, you might want to consider upgrading to Ugreen's new MagFlow Pro Magnetic Power Bank"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/989880/dungeons-and-dragons-ravenloft-netflix",
    "domain": "大厂 AI 动态",
    "title": "Dungeons &#038; Dragons is getting a &#8216;Ravenloft&#8217; live-action Netflix series",
    "url": "https://www.theverge.com/entertainment/989880/dungeons-and-dragons-ravenloft-netflix",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T20:48:05+00:00",
    "summary": "A Ravenloft series is currently in development from executive producer Alfonso Cuar&#243;n, writer and executive producer John August, and Hasbro Entertainment, Deadline reports. It could bring to lif"
  },
  {
    "id": "rss:https://www.theverge.com/policy/989769/tiktok-house-committee-china-kids-online-safety",
    "domain": "大厂 AI 动态",
    "title": "Congressman says TikTok backed out of a meeting to avoid child safety questions",
    "url": "https://www.theverge.com/policy/989769/tiktok-house-committee-china-kids-online-safety",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T18:37:57+00:00",
    "summary": "TikTok backed out of a congressional committee's \"public roundtable\" set for this month over concerns it would be asked about child safety practices, the chair of the committee said. After negotiating"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/989499/samsung-q-series-soundbar-dbrand-killswitch-2-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Samsung&#8217;s beloved Q Series sound system is hundreds off for Labor Day",
    "url": "https://www.theverge.com/gadgets/989499/samsung-q-series-soundbar-dbrand-killswitch-2-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T18:14:07+00:00",
    "summary": "Researching, buying, then finally assembling a sound system for your TV is daunting, but it doesn’t have to be. If you want one of the best kits you can get at a rare discount, Best Buy and Amazon are"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/the-sameness-problem-behind-those-unappetizing-ai-generated-menus/",
    "domain": "大厂 AI 动态",
    "title": "The sameness problem behind those unappetizing AI-generated menus",
    "url": "https://techcrunch.com/2026/09/03/the-sameness-problem-behind-those-unappetizing-ai-generated-menus/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:21:03+00:00",
    "summary": "While restaurant owners might look to generative AI as a shortcut to sprucing up their menu, customers can viscerally sense that something is wrong with the food."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/crusoe-reportedly-raises-3b-at-a-30b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Crusoe reportedly raises $3B at a $30B valuation",
    "url": "https://techcrunch.com/2026/09/03/crusoe-reportedly-raises-3b-at-a-30b-valuation/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T00:48:42+00:00",
    "summary": "The round came together after the data center developer reportedly secured a $13 billion contract with Jane Street."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/oura-files-to-go-public/",
    "domain": "大厂 AI 动态",
    "title": "Oura files to go public",
    "url": "https://techcrunch.com/2026/09/03/oura-files-to-go-public/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T22:35:41+00:00",
    "summary": "The ring maker says that its business has shown significant revenue growth over the past year."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/tesla-is-asking-people-if-they-want-to-buy-and-run-cybercab-fleets/",
    "domain": "大厂 AI 动态",
    "title": "Tesla is asking people if they want to buy and run Cybercab fleets",
    "url": "https://techcrunch.com/2026/09/03/tesla-is-asking-people-if-they-want-to-buy-and-run-cybercab-fleets/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T22:18:30+00:00",
    "summary": "The company published a form on its website Thursday soliciting info from people who are interested in \"Cybercab fleet vehicle purchasing.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/startup-arr-is-less-secure-than-ever-new-research-shows/",
    "domain": "大厂 AI 动态",
    "title": "Startup ARR is less secure than ever, new research shows",
    "url": "https://techcrunch.com/2026/09/03/startup-arr-is-less-secure-than-ever-new-research-shows/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T20:59:23+00:00",
    "summary": "The AI era has completely broken enterprise buying patterns, and startups haven't yet figured out how to navigate."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/the-cybercab-is-teslas-fork-in-the-road-moment/",
    "domain": "大厂 AI 动态",
    "title": "The Cybercab is Tesla’s ‘fork in the road’ moment",
    "url": "https://techcrunch.com/2026/09/03/the-cybercab-is-teslas-fork-in-the-road-moment/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T19:42:48+00:00",
    "summary": "The company is about to formally launch the gold two-seater, with no steering wheel or pedals -- a move that could change Tesla forever."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/accel-reportedly-in-talks-to-lead-1b-round-for-thinking-machines-at-40b-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Accel reportedly in talks to lead $1B round for Thinking Machines at $40B valuation",
    "url": "https://techcrunch.com/2026/09/03/accel-reportedly-in-talks-to-lead-1b-round-for-thinking-machines-at-40b-valuation/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T19:36:29+00:00",
    "summary": "The high-profile startup's annual revenue run rate stands at over $100 million."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/utilities-are-racing-to-link-up-with-fusion-startups-with-realta-fusion-the-latest-to-benefit/",
    "domain": "大厂 AI 动态",
    "title": "Utilities are racing to link up with fusion startups, with Realta Fusion the latest to benefit",
    "url": "https://techcrunch.com/2026/09/03/utilities-are-racing-to-link-up-with-fusion-startups-with-realta-fusion-the-latest-to-benefit/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T19:29:16+00:00",
    "summary": "The grid has been straining under the weight of new AI data centers, and that has utilities courting fusion startups."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/abliteration-ai-is-making-a-business-out-of-removing-ai-guardrails/",
    "domain": "大厂 AI 动态",
    "title": "Abliteration.ai is making a business out of removing AI guardrails",
    "url": "https://techcrunch.com/2026/09/03/abliteration-ai-is-making-a-business-out-of-removing-ai-guardrails/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T18:37:57+00:00",
    "summary": "Abliteration.AI is making powerful AI models without guardrails easier to access, arguing that giving defenders the same tools as bad actors could ultimately improve cybersecurity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/meta-is-paying-to-peek-at-how-you-use-their-latest-ai-model/",
    "domain": "大厂 AI 动态",
    "title": "Meta is paying to peek at how you use their latest AI model",
    "url": "https://techcrunch.com/2026/09/03/meta-is-paying-to-peek-at-how-you-use-their-latest-ai-model/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T18:19:56+00:00",
    "summary": "For its new Muse Spark model, intended for operating coding and other agents, Meta is offering an explicit discount averaging out to about 95% for users who \"contribute\" to the development of future m"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/openai-launches-astra-its-powerful-and-controversial-new-model/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI launches Astra, its powerful (and controversial) new model",
    "url": "https://techcrunch.com/2026/09/03/openai-launches-astra-its-powerful-and-controversial-new-model/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T18:01:45+00:00",
    "summary": "OpenAI claims that Astra represents \"a new frontier on computer and browser use,\" and that it handles tasks with unmatched \"speed, accuracy, and safety.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/qualcomm-backs-ultrahuman-in-70m-round-on-bet-to-turn-smart-rings-into-computers/",
    "domain": "大厂 AI 动态",
    "title": "Qualcomm backs Ultrahuman in $70M round on bet to turn smart rings into computers",
    "url": "https://techcrunch.com/2026/09/03/qualcomm-backs-ultrahuman-in-70m-round-on-bet-to-turn-smart-rings-into-computers/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T17:00:00+00:00",
    "summary": "Ultrahuman is targeting a $200 million annual revenue run rate by January 2027 as it builds a new Qualcomm-powered smart ring."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/circular-unveils-ring-3-series-with-contactless-payments-and-on-finger-vibration-alerts/",
    "domain": "大厂 AI 动态",
    "title": "Circular unveils Ring 3 series with contactless payments and on-finger vibration alerts",
    "url": "https://techcrunch.com/2026/09/03/circular-unveils-ring-3-series-with-contactless-payments-and-on-finger-vibration-alerts/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:42:54+00:00",
    "summary": "The Circular Ring 3 series announcement comes amid a year of heightened competition in the smart ring market, following the launches of the Oura Ring 5 and RingConn Gen 3."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/ollie-is-betting-privacy-can-win-the-ai-assistant-race/",
    "domain": "大厂 AI 动态",
    "title": "Ollie is betting its focus on privacy can help it win the AI assistant race",
    "url": "https://techcrunch.com/2026/09/03/ollie-is-betting-privacy-can-win-the-ai-assistant-race/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:09:01+00:00",
    "summary": "The family-focused AI assistant wants access to the details of your everyday life, but says it won’t use that data to train AI models or share it with others."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/google-launches-ai-voice-features-in-gmail-docs-and-keep/",
    "domain": "大厂 AI 动态",
    "title": "Google launches AI voice features in Gmail, Docs, and Keep",
    "url": "https://techcrunch.com/2026/09/03/google-launches-ai-voice-features-in-gmail-docs-and-keep/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T16:00:00+00:00",
    "summary": "Users can search for emails or draft documents using the new conversational feature."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/googles-latest-ai-weather-model-gives-you-no-excuse-to-forget-your-umbrella/",
    "domain": "大厂 AI 动态",
    "title": "Google’s latest AI weather model gives you no excuse to forget your umbrella",
    "url": "https://techcrunch.com/2026/09/03/googles-latest-ai-weather-model-gives-you-no-excuse-to-forget-your-umbrella/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T15:00:00+00:00",
    "summary": "WeatherNext 3 is the latest wave of a sea change in meteorology brought out by deep learning techniques. Google says it will start feeding into weather information users see in search, Google Maps, an"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/volunteer-at-techcrunch-founder-summit-in-boston/",
    "domain": "大厂 AI 动态",
    "title": "Volunteer at TechCrunch Founder Summit in Boston",
    "url": "https://techcrunch.com/2026/09/03/volunteer-at-techcrunch-founder-summit-in-boston/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T13:00:00+00:00",
    "summary": "Our rebranded Boston event, TechCrunch Founder Summit (formerly All Stage), is back on November 4th! And we are looking for some incredible volunteers to help us make this event happen. If you are int"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/tiktok-comments-are-getting-more-interactive-with-voice-comments-polls-and-more/",
    "domain": "大厂 AI 动态",
    "title": "TikTok comments are getting more interactive with voice comments, polls, and more",
    "url": "https://techcrunch.com/2026/09/03/tiktok-comments-are-getting-more-interactive-with-voice-comments-polls-and-more/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T13:00:00+00:00",
    "summary": "With the additions, the app is borrowing features from messaging apps as it looks to deepen engagement on its platform."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/nvidia-confirms-it-will-buy-hugging-face-for-12-9-billion/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia confirms it will buy Hugging Face for $12.9 billion",
    "url": "https://techcrunch.com/2026/09/03/nvidia-confirms-it-will-buy-hugging-face-for-12-9-billion/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T12:42:45+00:00",
    "summary": "Nvidia said Hugging Face hosts over 3 million models and is used by over 18 million developers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/03/amazons-zoox-expands-its-robotaxi-service-to-las-vegas-airport/",
    "domain": "大厂 AI 动态",
    "title": "Amazon’s Zoox expands its robotaxi service to Las Vegas airport",
    "url": "https://techcrunch.com/2026/09/03/amazons-zoox-expands-its-robotaxi-service-to-las-vegas-airport/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T12:12:56+00:00",
    "summary": "Zoox is expanding to this critical ride-hailing destination a few weeks after it started charging for robotaxi rides."
  },
  {
    "id": "rss:https://stratechery.com/2026/fable-5-1-enterprise-frontier-safeguards/",
    "domain": "大厂 AI 动态",
    "title": "Fable 5.1, Enterprise Frontier Safeguards",
    "url": "https://stratechery.com/2026/fable-5-1-enterprise-frontier-safeguards/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-02T10:00:00+00:00",
    "summary": "Fable 5.1 is out, and the hated Fable data retention policy is not just being altered, but entirely removed in the meantime. Plus, why increased caching is a win-win."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/reports-rfk-jr-ordered-measles-deaths-deletion-cdc-still-secretly-counts-them/",
    "domain": "大厂 AI 动态",
    "title": "Reports: RFK Jr. ordered measles deaths deletion; CDC still secretly counts them",
    "url": "https://arstechnica.com/health/2026/09/reports-rfk-jr-ordered-measles-deaths-deletion-cdc-still-secretly-counts-them/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T22:13:50+00:00",
    "summary": "CDC staff had already accepted the measles death reports when RFK Jr. meddled."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/09/xbox-imposes-harsh-new-time-limits-for-game-pass-game-streaming/",
    "domain": "大厂 AI 动态",
    "title": "Xbox imposes harsh new time limits for Game Pass game streaming",
    "url": "https://arstechnica.com/gaming/2026/09/xbox-imposes-harsh-new-time-limits-for-game-pass-game-streaming/",
    "source": "Kyle Orland",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T21:10:59+00:00",
    "summary": "Over 1 million Game Pass subscribers will have to pay more for their heavy streaming use."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/150-research-primates-got-diarrhea-flooding-lab-with-priceless-vaccine-data/",
    "domain": "大厂 AI 动态",
    "title": "150 research primates got diarrhea, flooding lab with priceless vaccine data",
    "url": "https://arstechnica.com/health/2026/09/150-research-primates-got-diarrhea-flooding-lab-with-priceless-vaccine-data/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T20:14:48+00:00",
    "summary": "Researchers now have clear new targets and insights for developing a Shigella vaccine."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/09/us-senator-calls-on-the-nsa-to-give-guidance-for-use-of-vpns/",
    "domain": "大厂 AI 动态",
    "title": "Confused about which VPN is right, US senator asks the NSA for guidance",
    "url": "https://arstechnica.com/security/2026/09/us-senator-calls-on-the-nsa-to-give-guidance-for-use-of-vpns/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T19:52:06+00:00",
    "summary": "Open source, commercial, single-hop, multi-hop, mixnet? The array of options is dizzying."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/nj-urges-scotus-to-rule-that-kalshi-sports-bets-are-gambling-not-swaps/",
    "domain": "大厂 AI 动态",
    "title": "Supreme Court urged to let states regulate sports bets on prediction markets",
    "url": "https://arstechnica.com/tech-policy/2026/09/nj-urges-scotus-to-rule-that-kalshi-sports-bets-are-gambling-not-swaps/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T19:42:02+00:00",
    "summary": "Circuit split raised the odds that SCOTUS will rule on Kalshi fight against states."
  },
  {
    "id": "rss:https://arstechnica.com/information-technology/2026/09/vmware-migration-reduces-tottenham-hotspurs-licensing-fees-by-85-percent/",
    "domain": "大厂 AI 动态",
    "title": "VMware migration reduces Tottenham Hotspur's licensing fees by 85 percent",
    "url": "https://arstechnica.com/information-technology/2026/09/vmware-migration-reduces-tottenham-hotspurs-licensing-fees-by-85-percent/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-03T18:58:31+00:00",
    "summary": "Pro soccer team's CTO points to \"issues with the Broadcom takeover.\""
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
    "id": "wscn:3781088",
    "domain": "股票",
    "title": "GPT-6，“强拆”App的墙",
    "url": "https://wallstreetcn.com/articles/3781088",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T07:39:19+00:00",
    "summary": "GPT-6 Astra的关键突破，不只是Computer Use更强，而是AI正在“强拆”App的接口墙。过去，软件没有API，AI就很难进入；如今，Agent可以自主选择API、Browser、Code或直接操作GUI，软件是否开放机器接口不再是AI能否完成任务的必要条件。"
  },
  {
    "id": "wscn:3781085",
    "domain": "股票",
    "title": "野村：若日元持续走弱，日本央行或连续三次加息",
    "url": "https://wallstreetcn.com/articles/3781085",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T07:33:41+00:00",
    "summary": "野村证券警告，若日元持续走软并逼近160关口，日本央行或在未来三次会议（9月、10月及12月）上连续加息，开创数十年来最激进的紧缩节奏。尽管基准预测仍为每季度加息一次，但若高市早苗政府不予干预且美联储降息配合，日元升值空间或被进一步打开。"
  },
  {
    "id": "wscn:3781086",
    "domain": "股票",
    "title": "Meta扎克伯格曾私下致电特朗普：别设AI监管机构",
    "url": "https://wallstreetcn.com/articles/3781086",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T07:33:36+00:00",
    "summary": "据报道，扎克伯格8月曾私下向特朗普通话，对仿照金融业FINRA设立强制性AI监管机构的提案表达反对。目前白宫内部在监管路径上陷入分歧，在仿FINRA的政府审查模式与基于自愿原则的电影协会（MPA）评级模式之间游移，政策最终走向仍不明朗。"
  },
  {
    "id": "wscn:3781087",
    "domain": "股票",
    "title": "韩国出兵霍尔木兹海峡？韩总统府：仍处于“研究审议”阶段",
    "url": "https://wallstreetcn.com/articles/3781087",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T07:29:06+00:00",
    "summary": "韩国正加快研究向霍尔木兹海峡派兵方案，拟派海上巡逻机、军需支援舰等非战斗力量，但尚未作出决定。韩媒称，此举或与特朗普持续要求韩国参与中东事务有关。派兵仍需经过国务会议及国会批准，最终能否落地仍存变数。"
  },
  {
    "id": "wscn:3781080",
    "domain": "股票",
    "title": "美非农前夕，全球股市反弹，韩股收涨1.64%，日元强势，油价小幅走高",
    "url": "https://wallstreetcn.com/articles/3781080",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T07:11:03+00:00",
    "summary": "美联储官员偏鸽表态令市场重新定价加息预期，韩国首尔综指收盘上涨1.64%，报6687.21点。美元兑日元交投于约156.28。布伦特原油小幅走高至每桶约95.65美元，有望创下7月以来最大单周涨幅。现货黄金失守4460美元/盎司，日内跌0.3%。"
  },
  {
    "id": "wscn:3781082",
    "domain": "股票",
    "title": "报道：苹果折叠屏iPhone日产量仅“几百”台，开售初期或供应紧张",
    "url": "https://wallstreetcn.com/articles/3781082",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T07:07:48+00:00",
    "summary": "苹果首款折叠屏iPhone被曝日产量仅\"几百台\"，距离每日数万台的商业化目标相去甚远。8月新增验证程序推迟量产计划，铰链性能与屏幕平整度成卡脖子难题。全年800万至1000万台的目标能否兑现存疑，开售即\"一机难求\"或成定局。"
  },
  {
    "id": "wscn:3781083",
    "domain": "股票",
    "title": "万斯又公开喊话美联储：应该降息",
    "url": "https://wallstreetcn.com/articles/3781083",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T06:43:21+00:00",
    "summary": "美国副总统万斯周四再度公开喊话美联储，称降息是应对当前通胀数据“正确且负责任”的选择，并表示“希望得到美联储的帮助”。这与沃什近期暗示可能加息的立场形成直接冲突。距9月15日FOMC会议不足两周，市场对加息与否的预期几乎五五开。"
  },
  {
    "id": "wscn:3780999",
    "domain": "股票",
    "title": "当马斯克开始造叶片，巴菲特也盯上AI用电：AIDC正在重写“电从哪里来”",
    "url": "https://wallstreetcn.com/premium/articles/3780999?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T06:31:52+00:00",
    "summary": "北美AI数据中心建设速度正在快过电网扩容和大发电设备交付，现场主电由备用方案走向数十GW级市场。重型燃机仍占长期基荷优势，但漫长排产给航改燃机、往复式内燃机和固体氧化物燃料电池打开了空间。未来几年的产业机会，更值得从供给稀缺、出货弹性和渗透率变化三个角度观察。"
  },
  {
    "id": "wscn:3780964",
    "domain": "股票",
    "title": "荷兰央行秘密运回黄金 它究竟看到了什么？",
    "url": "https://wallstreetcn.com/premium/articles/3780964?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T06:22:14+00:00",
    "summary": "操作本身值得细看，因为它暴露了一种非和平时期的思维方式。"
  },
  {
    "id": "wscn:3781081",
    "domain": "股票",
    "title": "800亿美元！全球最大主权基金拟大幅减持美国国债",
    "url": "https://wallstreetcn.com/articles/3781081",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T06:20:04+00:00",
    "summary": "挪威主权财富基金正酝酿一场债券大挪移——拟削减约800亿美元美国国债敞口，转向房利美、房地美担保的机构MBS。此举发生在美债收益率高企、全球债市持续承压之际，市场对主权基金集体撤离美债的警觉情绪或将进一步升温。"
  },
  {
    "id": "wscn:3781079",
    "domain": "股票",
    "title": "今晚美国非农大考，“好消息”也是“坏消息”！",
    "url": "https://wallstreetcn.com/articles/3781079",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T06:14:44+00:00",
    "summary": "华尔街预期新增就业5.5万人，但ADP、裁员数据等先行指标全面走弱，叠加约2.5万移民工作资质到期机械性拖累，彭博经济学家直言：8月非农连续负增长概率相当高，而一旦成真，美联储加息路径将被彻底冻结。摩根大通认为，若数据高于10万人，美股将承受明显压力；3万至7万为\"金发姑娘区间\"。"
  },
  {
    "id": "wscn:3780878",
    "domain": "股票",
    "title": "日债破3%：一口补贴了全世界三十年的“廉价资本之井”正在干涸",
    "url": "https://wallstreetcn.com/premium/articles/3780878?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T05:39:50+00:00",
    "summary": "日元贬值是在装火药，升值才是扣扳机。"
  },
  {
    "id": "wscn:3781084",
    "domain": "股票",
    "title": "美股能否挺过“9月魔咒”？",
    "url": "https://wallstreetcn.com/articles/3781084",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:48:19+00:00",
    "summary": "全球债市抛售和美联储加息预期令美股在刚过去的8月陷入高位震荡，在财报季过后股市逐渐失去了重要的上涨推..."
  },
  {
    "id": "wscn:3781077",
    "domain": "股票",
    "title": "日元为何急涨2%？加息预期催生“套息交易平仓潮”",
    "url": "https://wallstreetcn.com/articles/3781077",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:10:14+00:00",
    "summary": "日元两日累计涨幅近3%，创2024年8月以来最大涨幅。直接导火索是日本央行行长植田和男及委员高田创发表鹰派表态，暗示9月议息会议存在大幅加息可能。野村证券预计本月加息25基点概率较高，极端情形下或连续三次加息。加息预期升温引发日元套息交易大规模平仓，巴西雷亚尔、南非兰特等高息货币同步承压。"
  },
  {
    "id": "wscn:3781062",
    "domain": "股票",
    "title": "A股三大指数集体收跌，大消费、农业股集体走强，半导体低迷，恒指、恒科指均涨2%，权重科网股全线上涨",
    "url": "https://wallstreetcn.com/articles/3781062",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:06:16+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市约4100股飘红，上午半天成交1.25万亿。沪深两市半日成交额1.23万亿，较上个交易日放量1355亿。板块方面，稳定币、传媒、农业、地产、白酒、金融板块走强，AI硬件侧较为低迷，煤炭、有色金属板块调整。"
  },
  {
    "id": "wscn:3780332",
    "domain": "股票",
    "title": "创新药中报业绩复盘：新市场，新叙事，新节点，为何业绩指引开始上调？",
    "url": "https://wallstreetcn.com/premium/articles/3780332?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T03:59:40+00:00",
    "summary": "站在 2026 年中，中国创新药板块的\"市场叙事\"已经发生根本性切换。"
  },
  {
    "id": "wscn:3781076",
    "domain": "股票",
    "title": "lululemon二季度营收转降，中国市场增速放缓",
    "url": "https://wallstreetcn.com/articles/3781076",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T03:40:35+00:00",
    "summary": "美洲同店销售下滑12%"
  },
  {
    "id": "wscn:3781073",
    "domain": "股票",
    "title": "英伟达收购Hugging Face的野望：从芯片霸主到生态\"造王者\"",
    "url": "https://wallstreetcn.com/articles/3781073",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T03:36:47+00:00",
    "summary": "英伟达以129亿美元拿下全球最大开源AI平台Hugging Face，1800万开发者社区一夜易主。从芯片到云算力、从模型投资到开发者工具，黄仁勋正将硬件霸权系统性转化为AI全产业链的隐性定价权——这这不仅是一笔收购，更是一场\"造王者\"的权力锁仓。"
  },
  {
    "id": "wscn:3781068",
    "domain": "股票",
    "title": "日本半导体：投资热潮能否带来产业复兴？",
    "url": "https://wallstreetcn.com/articles/3781068",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T03:26:07+00:00",
    "summary": "中金认为，日本半导体产业正迎来数十年来最大规模投资潮，日本并非全面押注先进制程，而是以\"补短板+强优势\"为战略轴心——既以举国之力扶持Rapidus冲击2nm，又持续巩固材料与设备的全球领先地位。半导体企业市值一年间暴涨约4倍，贡献了日经指数近半涨幅，一场产业复兴正从制造端延伸至资本市场与宏观经济的深层重塑。"
  },
  {
    "id": "wscn:3781064",
    "domain": "股票",
    "title": "韩股风险？高盛：散户已撤，“回购弹药”10月打光，只能看外资了",
    "url": "https://wallstreetcn.com/articles/3781064",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T03:11:07+00:00",
    "summary": "数据显示，韩国散户8月净买入规模较6月暴跌90%，大盘仅靠三星与SK海力士的回购苦撑。但高盛认为，这最后的托底弹药将于10月中旬提前打光！一旦支撑消失，市场将迎剧烈冲击，未来生死完全仰仗外资脸色，为10月潜在的流动性冲击做好准备。"
  },
  {
    "id": "hn:49473629",
    "domain": "股票",
    "title": "Alphabet stock sheds $700B as AI bills climb",
    "url": "https://www.semafor.com/article/08/27/2026/alphabet-stock-sheds-700b-as-ai-bills-climb",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 49,
    "published_at": "2026-08-28T02:23:11+00:00",
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
    "id": "hn:49468651",
    "domain": "股票",
    "title": "US Patriot missile stocks in Europe are 'beyond critical' due to Iran war",
    "url": "https://apnews.com/article/patriot-missiles-iran-war-russia-ukraine-trump-09c7d8030a2e11fbd8ee3f7176b3f2d4",
    "source": "hn_acker",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-08-27T17:54:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49396088",
    "domain": "股票",
    "title": "S&P 500 CEO median pay hits $17.3M, widening CEO-worker ratio to 312-to-1",
    "url": "https://finance.yahoo.com/markets/stocks/articles/p-500-ceo-median-pay-234900518.html",
    "source": "newsomix9xl",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-08-22T02:38:14+00:00",
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
    "id": "hn:49261857",
    "domain": "股票",
    "title": "The SpaceX Sham",
    "url": "https://dissentmagazine.org/online_articles/spacex-ipo-elon-musk-trillionaire/",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-08-11T17:47:03+00:00",
    "summary": ""
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
    "id": "hn:49253785",
    "domain": "股票",
    "title": "OpenAI wraps $7B share sale ahead of potential IPO",
    "url": "https://www.cnbc.com/2026/08/10/openai-wraps-7-billion-share-sale-ahead-of-potential-ipo-.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-08-11T05:40:35+00:00",
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
    "id": "hn:49366252",
    "domain": "股票",
    "title": "OpenAI 'will be a public company in 2027' or sooner, CFO Friar tells employees",
    "url": "https://www.cnbc.com/2026/08/19/open-ai-ipo-timing-2027-friar.html",
    "source": "thm",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-19T19:42:35+00:00",
    "summary": ""
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
    "id": "hn:49200390",
    "domain": "金融",
    "title": "Federal Communications Commission scraps limit on broadcast TV ownership",
    "url": "https://www.nbcnews.com/business/media/federal-communications-commission-scraps-limit-broadcast-tv-ownership-rcna587641",
    "source": "pseudolus",
    "platform": "hackernews",
    "points": 179,
    "published_at": "2026-08-06T18:22:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49415187",
    "domain": "金融",
    "title": "Nearly 3M Teslas recalled in China over hidden door handles",
    "url": "https://www.bbc.com/news/articles/c4g6ggdg030o",
    "source": "chicken-stew",
    "platform": "hackernews",
    "points": 120,
    "published_at": "2026-08-24T04:27:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49245487",
    "domain": "金融",
    "title": "Study links GLP-1 drugs to bigger jump in women's employment than a degree",
    "url": "https://finance.yahoo.com/healthcare/articles/harvard-study-links-glp-1-123000637.html",
    "source": "metadat",
    "platform": "hackernews",
    "points": 131,
    "published_at": "2026-08-10T16:02:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49548497",
    "domain": "金融",
    "title": "Mark Cuban: Why US hospitals \"don't know their costs\"",
    "url": "https://www.beckershospitalreview.com/finance/mark-cuban-why-us-hospitals-dont-know-their-costs/",
    "source": "elo2000",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-09-03T11:07:10+00:00",
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
    "id": "hn:49559666",
    "domain": "金融",
    "title": "Tesla Begins Offering Rides in a Car Without a Steering Wheel",
    "url": "https://www.nytimes.com/2026/09/03/business/tesla-cybercab-robotaxi-rides.html",
    "source": "telotortium",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-09-04T02:08:51+00:00",
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
    "id": "hn:49259043",
    "domain": "金融",
    "title": "Federal vendor with $50M in contracts leaves portal broken for a month",
    "url": "https://www.propublica.org/article/foia-requests-responses",
    "source": "ams1",
    "platform": "hackernews",
    "points": 101,
    "published_at": "2026-08-11T14:32:21+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.02900",
    "domain": "金融",
    "title": "DisclosureBeta: A Measurement-Channel Theory for Regime-Conditioned Betas from LLM-Read Risk Disclosures",
    "url": "https://arxiv.org/abs/2609.02900",
    "source": "Ping Kuen Wong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2609.02900v1 Announce Type: new Abstract: The problem is the beta a desk needs when a firm's price history is too short to trust: an S-1 filer, a recent listing, or a name just past a regime bre"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.02992",
    "domain": "金融",
    "title": "Tempting the Agent: The Economics of Reputation without Persistent Identity in AI Agent Markets",
    "url": "https://arxiv.org/abs/2609.02992",
    "source": "Federico Gatta, Manuel Naviglio, Francesco Tarantelli",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2609.02992v1 Announce Type: new Abstract: Reputation is a fundamental mechanism through which markets sustain trust when service quality cannot be perfectly assessed ex ante, constituting a form"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.03115",
    "domain": "金融",
    "title": "Mean-field equilibrium of heterogeneous agents under market impact",
    "url": "https://arxiv.org/abs/2609.03115",
    "source": "Joseph Lecl\\`ere, Mathieu Rosenbaum",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2609.03115v1 Announce Type: new Abstract: Although market participants generally have access to a common information set, they make decisions based on forecasts formed over heterogeneous horizon"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.03552",
    "domain": "金融",
    "title": "An Entropic Factor Model for Robust Portfolio Replication",
    "url": "https://arxiv.org/abs/2609.03552",
    "source": "Argimiro Arratia, Henryk Gzyl",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2609.03552v1 Announce Type: new Abstract: Portfolio replication, or the construction of a tradable basket of assets to match the risk-return profile of a target benchmark, is fundamentally an il"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.03741",
    "domain": "金融",
    "title": "Bayesian Confidence Recalibration and Research-Equilibrium Criticality: Temporal Support in Robust Portfolios",
    "url": "https://arxiv.org/abs/2609.03741",
    "source": "Han Yan\\c{c}",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2609.03741v1 Announce Type: new Abstract: Robust portfolio rules that reconstruct confidence sets after learning need not preserve the evaluator obtained by prior-by-prior Bayesian transport. In"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.04087",
    "domain": "金融",
    "title": "Global Multi-Maturity SPX-VIX Calibration Beyond Markovian Stitching",
    "url": "https://arxiv.org/abs/2609.04087",
    "source": "Atithi Acharya, Yue Sun, Brandon Augustino, Shouvanik Chakrabarti, Shree Hari Sureshbabu, Charlie Che",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2609.04087v1 Announce Type: new Abstract: We develop a global framework for joint S&amp;P 500 (SPX)-VIX smile calibration across multiple maturities without the conditional-independence restrict"
  },
  {
    "id": "rss:https://arxiv.org/abs/2210.15946",
    "domain": "金融",
    "title": "Local Media and the Shaping of Social Norms: Evidence from the Ebola outbreak",
    "url": "https://arxiv.org/abs/2210.15946",
    "source": "Ada Gonzalez-Torres",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2210.15946v4 Announce Type: replace Abstract: Media's influence on norms and behavior is widely recognized. Less is known about the role played by media being local. I examine this in a high-sta"
  },
  {
    "id": "rss:https://arxiv.org/abs/2504.12851",
    "domain": "金融",
    "title": "Optimal Capital Structure for Life Insurance Companies Offering Surplus Participation",
    "url": "https://arxiv.org/abs/2504.12851",
    "source": "Felix Fie{\\ss}inger, Mitja Stadje",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2504.12851v4 Announce Type: replace Abstract: This manuscript develops a dynamic capital structure model of life insurance companies offering participating contracts. Specifically, we explain wh"
  },
  {
    "id": "rss:https://arxiv.org/abs/2504.19623",
    "domain": "金融",
    "title": "Multi-Horizon Echo State Network Prediction of Intraday Stock Returns",
    "url": "https://arxiv.org/abs/2504.19623",
    "source": "Giovanni Ballarin, Jacopo Capra, Petros Dellaportas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2504.19623v2 Announce Type: replace Abstract: Stock return prediction is a problem that has received much attention in the finance literature. In recent years, sophisticated machine learning pro"
  },
  {
    "id": "rss:https://arxiv.org/abs/2602.19590",
    "domain": "金融",
    "title": "Metaorder modelling and identification from public data",
    "url": "https://arxiv.org/abs/2602.19590",
    "source": "Ezra Goliath, Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2602.19590v2 Announce Type: replace Abstract: Market-order flow in financial markets exhibits long-range correlations. This is a widely known stylised fact of financial markets. A popular hypoth"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.07059",
    "domain": "金融",
    "title": "Diffusive in plain sight: An inconspicuous law of market impact",
    "url": "https://arxiv.org/abs/2606.07059",
    "source": "Julius F. Bonart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2606.07059v2 Announce Type: replace Abstract: Decomposing market impact as the difference between realized and counterfactual returns, and requiring both to be diffusive, yields a structural ide"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.18684",
    "domain": "金融",
    "title": "How firms export: product assignment, export platforms, and hybrid firms",
    "url": "https://arxiv.org/abs/2606.18684",
    "source": "Ra\\'ul M\\'inguez, Asier Minondo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2606.18684v2 Announce Type: replace Abstract: Firms differ in manufacturing and foreign commercialization capabilities. We study how these differences organize exporting through multi-product ex"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.22459",
    "domain": "金融",
    "title": "Settlement Infrastructure, Inside Money Elasticity, and the Network Economics of Distributed Ledger Technology",
    "url": "https://arxiv.org/abs/2607.22459",
    "source": "Michail Samawi, Hui Gong, Francesca Medda",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2607.22459v2 Announce Type: replace Abstract: We construct the Settlement Modernisation Index, a panel dataset of 809 reform events across 24 advanced economies between 1993 and 2024, decomposed"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.13775",
    "domain": "金融",
    "title": "Structured Payment in Pawnshop Borrowing: Mandates vs. Choice",
    "url": "https://arxiv.org/abs/2608.13775",
    "source": "Francis J. DiTraglia, Craig McIntosh, Isaac Meza, Joyce Sadka, Enrique Seira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2608.13775v2 Announce Type: replace Abstract: Pawn loans offer borrowers a substantial degree of repayment flexibility in exchange for a harsh penalty in case of default: forfeit of collateral w"
  },
  {
    "id": "rss:https://arxiv.org/abs/2510.04785",
    "domain": "金融",
    "title": "What shifts threshold distributions in social contagions?",
    "url": "https://arxiv.org/abs/2510.04785",
    "source": "Luca Lazzaro, Manuel S. Mariani, Ren\\'e Algesheimer, Radu Tanase",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2510.04785v2 Announce Type: replace-cross Abstract: Individual thresholds in social contagions capture what fraction of others must adopt a new product or behavior before an individual adopts it"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.14991",
    "domain": "金融",
    "title": "Adaptive Partitioning and Learning for Stochastic Control of Diffusion Processes",
    "url": "https://arxiv.org/abs/2512.14991",
    "source": "Hanqing Jin, Renyuan Xu, Yanzhao Yang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2512.14991v3 Announce Type: replace-cross Abstract: We study reinforcement learning for controlled diffusion processes with unbounded continuous state spaces, bounded continuous actions, and pol"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.25844",
    "domain": "金融",
    "title": "Output-Only Identification and Spectral Monitoring of Coupled Feedback Networks with Known Time-Varying Actuation",
    "url": "https://arxiv.org/abs/2608.25844",
    "source": "Jihwan Woo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2608.25844v2 Announce Type: replace-cross Abstract: Coupled feedback networks are often monitored channel by channel even though cross-channel paths alter both stability margins and transmitted "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.27374",
    "domain": "金融",
    "title": "Distribution-constrained optimal multiple stopping: the Root-type solution",
    "url": "https://arxiv.org/abs/2608.27374",
    "source": "Shuoqing Deng, Daxin Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T04:00:00+00:00",
    "summary": "arXiv:2608.27374v2 Announce Type: replace-cross Abstract: We consider the distribution-constrained optimal stopping problem introduced by Bayraktar and Miller (Mathematical Finance, 2019) and Beiglboc"
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
    "id": "hn:49245071",
    "domain": "金融",
    "title": "Force-Fed by ICE",
    "url": "https://www.theguardian.com/us-news/2026/aug/10/ice-force-feeding-detention-gabar-choli",
    "source": "HotGarbage",
    "platform": "hackernews",
    "points": 97,
    "published_at": "2026-08-10T15:35:44+00:00",
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
    "id": "hn:49432102",
    "domain": "金融",
    "title": "Nostr vs. Fediverse vs. Bluesky: A Comparison of Decentralized Social Protocols",
    "url": "https://soapbox.pub/blog/comparing-protocols",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-08-25T11:27:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49206115",
    "domain": "金融",
    "title": "Anthropic CEO reportedly worried new hires only care about money",
    "url": "https://finance.yahoo.com/technology/ai/articles/anthropic-ceo-reportedly-worried-hires-160000647.html",
    "source": "frays",
    "platform": "hackernews",
    "points": 65,
    "published_at": "2026-08-07T05:15:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49243531",
    "domain": "金融",
    "title": "China is now the world's greatest oil power",
    "url": "https://www.economist.com/finance-and-economics/2026/08/09/china-is-now-the-worlds-great-oil-power",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-08-10T13:40:46+00:00",
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
    "id": "hn:49414279",
    "domain": "金融",
    "title": "Tesla discontinues its Solar Roof tiles, not economically viable",
    "url": "https://electrek.co/2026/08/20/tesla-discontinues-solar-roof-panels-only/",
    "source": "MilnerRoute",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-08-24T01:21:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:49184251",
    "domain": "金融",
    "title": "Fed's Kashkari says 'now is the time to start slowly moving' rates up",
    "url": "https://www.cnbc.com/2026/08/05/feds-kashkari-says-now-is-the-time-to-start-slowly-moving-rates-up.html",
    "source": "mapping365",
    "platform": "hackernews",
    "points": 42,
    "published_at": "2026-08-05T15:24:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49391382",
    "domain": "金融",
    "title": "Tesla sunsets its Solar Roof tiles",
    "url": "https://www.theverge.com/tech/983167/tesla-solar-roof-tiles-discontinued",
    "source": "doener",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-08-21T17:32:57+00:00",
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
    "id": "hn:49215292",
    "domain": "金融",
    "title": "Mykhailo Fedorov reveals struggle to secure Patriot missiles and Western support",
    "url": "https://www.uawire.org/former-ukrainian-defense-minister-mykhailo-fedorov-reveals-struggles-to-secure-patriot-missiles-and-western-support",
    "source": "greedo",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-08-07T19:38:05+00:00",
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
    "id": "hn:49289340",
    "domain": "金融",
    "title": "Hooray for index funds–just don't call them passive",
    "url": "https://www.economist.com/finance-and-economics/2026/08/11/hooray-for-index-funds-just-dont-call-them-passive",
    "source": "thm",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-13T17:37:33+00:00",
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
  },
  {
    "id": "hn:49350858",
    "domain": "金融",
    "title": "AI Is Upending One of Finance's Cushiest Jobs",
    "url": "https://www.bloomberg.com/news/features/2026-06-05/ai-is-upending-traditional-financial-advisor-jobs",
    "source": "theriddlr",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-18T18:59:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49208461",
    "domain": "金融",
    "title": "New Intelligence Warns Russia May Provoke NATO Amid Dwindling U.S. Munitions",
    "url": "https://www.wsj.com/finance/investing/new-intelligence-warns-russia-may-provoke-nato-amid-dwindling-u-s-munitions-68f497c7",
    "source": "doener",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-07T10:52:27+00:00",
    "summary": ""
  }
]
```
