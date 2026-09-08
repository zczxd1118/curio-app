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

- 今日日期：`2026-09-08`
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
  "date": "2026-09-08",
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
    "points": 4470043,
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
    "points": 1861077,
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
    "points": 1825811,
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
    "points": 1303724,
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
    "points": 1257753,
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
    "points": 1176416,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1kX546QEjG",
    "domain": "AI",
    "title": "保姆级Claude Code速成，必学！简单！【附完整文档】",
    "url": "http://www.bilibili.com/video/av116554859545963",
    "source": "数字游牧人",
    "platform": "bilibili",
    "points": 1079224,
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
    "points": 882880,
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
    "points": 749903,
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
    "points": 723585,
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
    "points": 673091,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 441947,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1rBRQBSEwB",
    "domain": "AI",
    "title": "Claude Code+DeepSeek V4 Pro安装教程｜3步从零装好开始用 | Mac Windows",
    "url": "http://www.bilibili.com/video/av116543199385810",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 377955,
    "published_at": "2026-05-09T10:10:00+00:00",
    "summary": "上期vibe coding零基础教程10万多人看了，私信和评论里问最多的居然不是怎么写需求。\n 而是Claude Code怎么装？DeepSeek怎么接进去？🫣\n\n所以这期作为补丁教程，专门帮大家搞定这3件事：\n 1️⃣ 安装Claude Code\n 2️⃣ 把DeepSeek V4 Pro百万上下文满血版接入Claude Code\n 3️⃣ 在VS Code里正式用起来\n\nMac和Windows"
  },
  {
    "id": "bvid:BV16Luq6FEmP",
    "domain": "AI",
    "title": "当不懂代码的老婆，第一次接触vibe coding……",
    "url": "http://www.bilibili.com/video/av117076211536327",
    "source": "糖果果的未来要发光",
    "platform": "bilibili",
    "points": 349745,
    "published_at": "2026-08-11T09:50:27+00:00",
    "summary": "当不懂代码的老婆，第一次接触vibe coding……"
  },
  {
    "id": "bvid:BV1ahFmzqE9z",
    "domain": "AI",
    "title": "【2026版Agent Skills保姆级教程】2小时从会用到会造，全方位提升工作效率。Claude Skills、Agent技能、OpenCode",
    "url": "http://www.bilibili.com/video/av116044177936465",
    "source": "博学谷",
    "platform": "bilibili",
    "points": 340103,
    "published_at": "2026-02-10T03:28:31+00:00",
    "summary": "视频配套资源领取方式戳：https://www.bilibili.com/opus/1167610370075918393\n或关注博学谷公综号领取，回复关键词：0102\n============================\n学完本课程，就能通过现有的Skill技能让你的AI更聪明，更能干，更可靠，全方位提升工作效率，还可以根据自己需要造出自己想要的skill，用AI 360°武装自己，直接从小"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 326980,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 283455,
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
    "points": 272257,
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
    "points": 256542,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 254027,
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
    "points": 248115,
    "published_at": "2026-08-10T10:54:20+00:00",
    "summary": "Codex 安装 + 上手速通，保姆级教程！\n无需 ChatGPT 订阅，国内直连 DeepSeek"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 185743,
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
    "points": 180813,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1TTR8BaEnL",
    "domain": "AI",
    "title": "Claude Code 零基础终极教程：安装、换模型、插件、Hooks、Skills、Subagents、实战项目一次讲透！",
    "url": "http://www.bilibili.com/video/av116529475622752",
    "source": "木子不写代码",
    "platform": "bilibili",
    "points": 175621,
    "published_at": "2026-05-07T08:00:00+00:00",
    "summary": "这是你能看到的最完整的 Claude Code 零基础系统教程。\n\n\n我们将深度拆解：\n\n1️⃣ 基础入门：安装、第三方模型接入、权限系统。\n\n2️⃣ 核心进阶：Tools、Hooks、Skills、Subagents 及自动化流程。\n\n3️⃣ 项目实战：从零构建一个真实可用的 AI 网页 App。\n\n\n视频跟到最后，你不只是学会写代码，而是掌握 AI 智能体的工作逻辑。我是木子，只提供 AI 时"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 164328,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 155345,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1EBui6xEbT",
    "domain": "AI",
    "title": "WorkBuddy 60分钟超完整保姆级教程！无论是想入门Agent还是想工作提效，听完秒变大神！",
    "url": "http://www.bilibili.com/video/av117076345819236",
    "source": "大梁Max",
    "platform": "bilibili",
    "points": 145722,
    "published_at": "2026-08-11T10:23:28+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV154426xEha",
    "domain": "AI",
    "title": "我的 AI 编程全流程：如何使用 AI 稳定交付一个高质量的产品",
    "url": "http://www.bilibili.com/video/av117178586240848",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 135705,
    "published_at": "2026-08-29T11:38:24+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1YG7G6eEPR",
    "domain": "AI",
    "title": "【全60集】吊打付费！目前B站最全最细的Agent智能体开发全套教程！手把手教你打造专属智能体，七天就能从小白到大神！带你从零基础入门到精通实现商业变现！",
    "url": "http://www.bilibili.com/video/av116815090947614",
    "source": "AI-Agent开发",
    "platform": "bilibili",
    "points": 120994,
    "published_at": "2026-06-26T06:57:42+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 110835,
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
    "points": 93601,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 74379,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54905,
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
    "points": 47683,
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
    "points": 47646,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV15hNq6LE6V",
    "domain": "AI",
    "title": "7月最新Claude防封号最安全的！注册+订阅充值教程！A畜看到直接腿软，大喊完蛋了，随后呜呼",
    "url": "http://www.bilibili.com/video/av116923035617928",
    "source": "harness使用教程-",
    "platform": "bilibili",
    "points": 43040,
    "published_at": "2026-07-15T09:16:34+00:00",
    "summary": "AI充值站：njzqhy.top"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 41561,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 40836,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1XiD5BQEAj",
    "domain": "AI",
    "title": "Claude Code 接入微信、一行命令把Claude Code装进微信、保姆级教程、微信支持Claude Code（cc-connect）远程开发",
    "url": "http://www.bilibili.com/video/av116350093694897",
    "source": "下班学AI",
    "platform": "bilibili",
    "points": 39657,
    "published_at": "2026-04-05T04:02:16+00:00",
    "summary": "【别再看电脑了！】一行命令，让Claude Code实现远程调用🔥\n还在守着电脑终端敲Prompt？太Low了！今天手把手教你用 cc-connect 把Claude Code接入即时通讯工具，实现远程开发。\n👉 本期视频你将学到：\n1️⃣ 一行命令极速部署，无需复杂后端\n2️⃣ 手机端直接操控：发语音、发文字，AI帮你写代码、修Bug\n3️⃣ 远程开发实战：躺在沙发上用手机调优项目\n从此手机就是"
  },
  {
    "id": "bvid:BV1NddKBvEsY",
    "domain": "AI",
    "title": "claude code 桌面端安装并且配置第三方api使用教程，想体验的尽早吧，因为这公司可能不知道哪天抽风就会禁用了！#claude #ai #人工智能",
    "url": "http://www.bilibili.com/video/av116535968466799",
    "source": "菜鸡的老黎",
    "platform": "bilibili",
    "points": 37945,
    "published_at": "2026-05-07T23:56:28+00:00",
    "summary": "claude code 桌面端安装并且配置第三方api使用教程，想体验的尽早吧，因为这公司可能不知道哪天抽风就会禁用了！#claude #ai #人工智能 #agent"
  },
  {
    "id": "bvid:BV1xzGH6uEG8",
    "domain": "AI",
    "title": "AI全自动化搭建复杂Simulink模型！5步即可完成部署，全流程分享！",
    "url": "http://www.bilibili.com/video/av116629870481178",
    "source": "电气攻城狮001",
    "platform": "bilibili",
    "points": 37176,
    "published_at": "2026-05-24T13:50:56+00:00",
    "summary": "本期分享五步实操流程，借助 Claude Code 交互载体接入 DeepSeek 大模型，搭配 2026.5.21 最新版 Simulink Agentic Toolkit，解锁 68 项建模技能。依次完成 API 额度配置、环境部署、工具包安装，连通校验后开启全自动模式。无需手动拖拽模块与布线，输入指令即可依托 Simscape 蓝库，在 MATLAB2026a 中自动搭建三相并网逆变器开环模"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 36777,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29717,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 25486,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1Z5KU6UExC",
    "domain": "AI",
    "title": "【吴恩达2026】Vibe Coding保姆级教程，手把手从环境搭建到工作流完整闭环！——DeepLearning.AI—附带课件代码",
    "url": "http://www.bilibili.com/video/av116951003242391",
    "source": "吴恩达AIAgent",
    "platform": "bilibili",
    "points": 23925,
    "published_at": "2026-07-20T07:01:13+00:00",
    "summary": "本套课专门解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1XxXpBEEHU",
    "domain": "AI",
    "title": "Claude Code远程开发终极方案！手机改代码+实时预览~【小白教程】",
    "url": "http://www.bilibili.com/video/av116294326230438",
    "source": "爱听书的程序员阿超",
    "platform": "bilibili",
    "points": 23342,
    "published_at": "2026-03-26T12:00:00+00:00",
    "summary": "之前，我一直在研究怎么远程使用 Claude Code 开发项目，并且能实时预览效果。但是一直都没有找到合适的解决方案，要么就是给一个临时公网链接预览，每次都需要再配置，要么就是购买云服务器来配置，都感觉挺麻烦的~\n\n最近，我发现这个蒲公英异地组网的方案，用来做远程开发 Claude Code 项目，感觉非常方便，不仅能修改代码，而且我实时预览的需求也很好的满足了。\n\n这样我随时随地都可以用 AI"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 21385,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1N4tH6GE2h",
    "domain": "AI",
    "title": "Anthropic重磅史诗升级！Claude Code 2.0全自动模式深度实测，多智能体协同全自动写完项目！",
    "url": "http://www.bilibili.com/video/av117184256810815",
    "source": "进化中的阿陈",
    "platform": "bilibili",
    "points": 19462,
    "published_at": "2026-08-30T11:39:11+00:00",
    "summary": "程序员彻底被解放了！Anthropic 重磅发布 Claude Code 2.0！新增王炸级 Auto Mode 全自动模式，无需人工确认全自动写完复杂项目；多 Sub-Agents 智能体协同并行开发，原生内置 iOS 模拟器实时调试 App 与无头浏览器测试，配合 Opus 5 简直强到离谱，速看实测！"
  },
  {
    "id": "bvid:BV1eMgG6QEeG",
    "domain": "AI",
    "title": "【吴恩达】这绝对是把《Vibe Coding》讲得最通透的一套课！手把手教你构建自己的企业级AI工作流，学完直接落地！——附带课件代码",
    "url": "http://www.bilibili.com/video/av117081815189025",
    "source": "吴恩达Agents",
    "platform": "bilibili",
    "points": 19180,
    "published_at": "2026-08-12T09:29:57+00:00",
    "summary": "Vibe Coding火了，但你会发现——AI写的代码像开盲盒，今天能跑明天崩，项目一大就乱套。\n规范驱动开发（SDD） 就是来解决这个问题的。它的核心理念很简单：在让AI写代码之前，先和AI在统一的规范文档里对齐需求，把开发变成可预测、可追溯、可控制的过程。"
  },
  {
    "id": "bvid:BV1d1t96EE1b",
    "domain": "AI",
    "title": "【AI漫剧】AI 漫剧完整教程！全套制作工具、实操工作流一次性给到你，从剧本、人物生成再到视频导出全流程拆解，保姆级手把手教学，零基础也能快速上手，学完即可接单",
    "url": "http://www.bilibili.com/video/av117204708233511",
    "source": "即梦AI全套教程",
    "platform": "bilibili",
    "points": 18624,
    "published_at": "2026-09-03T02:24:00+00:00",
    "summary": "想系统学习AI漫剧的小伙伴看置顶评论~\n持续更新中~课程资料”666“获取~求一键三连【长按点赞】支持！"
  },
  {
    "id": "hn:49458161",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia agrees to acquire Hugging Face for $13B",
    "url": "https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 1987,
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
    "points": 328,
    "published_at": "2026-09-03T12:10:33+00:00",
    "summary": ""
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
    "id": "hn:49594189",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Jensen Huang says 'AGI has arrived' and congratulates OpenAI",
    "url": "https://www.businessinsider.com/nvidia-jensen-huang-agi-openai-astra-ai-2026-9",
    "source": "vinni2",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-09-07T05:23:31+00:00",
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
    "id": "rss:https://www.eetimes.com/nvidia-acquires-huggingface-for-12-9b/",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Acquires HuggingFace for $12.9B",
    "url": "https://www.eetimes.com/nvidia-acquires-huggingface-for-12-9b/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T15:58:00+00:00",
    "summary": "The open-source model hub will be acquired by the world’s biggest compute provider. The post Nvidia Acquires HuggingFace for $12.9B appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/why-microcooling-will-be-a-critical-enabler-of-agentic-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Microcooling Will Be a Critical Enabler of Agentic AI",
    "url": "https://www.eetimes.com/why-microcooling-will-be-a-critical-enabler-of-agentic-ai/",
    "source": "Mike Housholder",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T13:19:14+00:00",
    "summary": "Agentic AI won’t thrive on raw compute alone; tiny devices need microcooling to beat heat and sustain intelligence. The post Why Microcooling Will Be a Critical Enabler of Agentic AI appeared first on"
  },
  {
    "id": "rss:https://www.eetimes.com/why-holistic-digital-twins-are-needed-to-accelerate-sdv-development/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Holistic Digital Twins are Needed to Accelerate SDV Development",
    "url": "https://www.eetimes.com/why-holistic-digital-twins-are-needed-to-accelerate-sdv-development/",
    "source": "Heather Campbell, Marketing Director for PAVE360, Siemens EDA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T13:00:00+00:00",
    "summary": "Discover how holistic digital twins help automakers shift left, overcome integration complexity and accelerate modern software-defined vehicle development. The post Why Holistic Digital Twins are Need"
  },
  {
    "id": "rss:https://www.eetimes.com/kioxias-flash-for-dram-initiative-eyes-ai-workloads/",
    "domain": "AI 算力 / 半导体",
    "title": "Kioxia’s Flash-for-DRAM Initiative Eyes AI Workloads",
    "url": "https://www.eetimes.com/kioxias-flash-for-dram-initiative-eyes-ai-workloads/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T08:01:30+00:00",
    "summary": "The CXL-attached memory expansion uses NAND flash optimized for high-speed processing alongside AI compute devices. The post Kioxia&#8217;s Flash-for-DRAM Initiative Eyes AI Workloads appeared first o"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-surpasses-one-million-high-na-euv-wafers-processed-outpaces-the-rest-of-the-industry-combined-company-also-trailblazing-giant-6-12-photomasks-to-speed-production-and-lower-costs1",
    "domain": "AI 算力 / 半导体",
    "title": "Intel surpasses one million High-NA EUV wafers processed, outpaces the rest of the industry combined — company also trailblazing giant 6×12 photomasks to speed production and lower costs",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-surpasses-one-million-high-na-euv-wafers-processed-outpaces-the-rest-of-the-industry-combined-company-also-trailblazing-giant-6-12-photomasks-to-speed-production-and-lower-costs1",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T06:00:00+00:00",
    "summary": "Intel is leading the semiconductor industry with High-NA fleet and process-maturity milestone as it reaches 1 million wafers processed using High-NA tools, moves forward with 6×12 photomask effort."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/arm-debuts-next-gen-semi-custom-neoverse-css-n4-ranger-platform-compute-subsystem-packs-up-to-128-cores-per-die-on-tsmc-n3p",
    "domain": "AI 算力 / 半导体",
    "title": "Arm debuts next-gen semi-custom Neoverse CSS N4 ‘Ranger’ platform — compute subsystem packs up to 128 cores per die on TSMC N3P",
    "url": "https://www.tomshardware.com/pc-components/cpus/arm-debuts-next-gen-semi-custom-neoverse-css-n4-ranger-platform-compute-subsystem-packs-up-to-128-cores-per-die-on-tsmc-n3p",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T02:00:00+00:00",
    "summary": "Arm’s new Neoverse CSS N4 platform can pack up to 128 cores per die and 256 MB of L3 cache, representing a large increase in support over the previous Neoverse CSS N2 platform."
  },
  {
    "id": "rss:https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-38-percent-on-a-new-gaming-pc-before-the-labor-day-sales-end-and-beat-the-price-rises-lock-down-last-minute-savings-on-new-pre-built-rigs-from-best-buy-newegg-and-walmart",
    "domain": "AI 算力 / 半导体",
    "title": "Save up to 38% on a new gaming PC before the Labor Day sales end and beat the price rises — lock down last-minute savings on new pre-built rigs from Best Buy, Newegg, and Walmart",
    "url": "https://www.tomshardware.com/gift-guides-seasonal-sales/save-up-to-38-percent-on-a-new-gaming-pc-before-the-labor-day-sales-end-and-beat-the-price-rises-lock-down-last-minute-savings-on-new-pre-built-rigs-from-best-buy-newegg-and-walmart",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T16:00:16+00:00",
    "summary": "Labor Day is nearly over, but there's still an opportunity to save hundreds on a new gaming PC before the prices rise again."
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/xtool-reveals-its-next-generation-of-lasers-modular-x1-supports-co2-diode-uv-fiber-and-mopa-lasers",
    "domain": "AI 算力 / 半导体",
    "title": "xTool reveals its next generation of lasers — modular X1 supports CO2, Diode, UV, Fiber, and MOPA lasers",
    "url": "https://www.tomshardware.com/maker-stem/xtool-reveals-its-next-generation-of-lasers-modular-x1-supports-co2-diode-uv-fiber-and-mopa-lasers",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T14:05:05+00:00",
    "summary": "The X1 will combine gantry and galvo technology in one machine."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-gpt-6-astra-model-autonomously-completes-portal-in-24-hours-feat-cost-just-usd571-in-tokens",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI’s GPT-6 Astra model autonomously completes Portal in 24 hours — feat cost just $571 in tokens",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-gpt-6-astra-model-autonomously-completes-portal-in-24-hours-feat-cost-just-usd571-in-tokens",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T13:25:56+00:00",
    "summary": "An AI enthusiast has conducted an experiment where OpenAI's new GPT-6 Astra played through the entirety of Valve's Portal 3D puzzler game on its own."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/astonishing-mod-runs-nvidia-dlss-5-on-a-second-gpu-using-a-reshade-add-on-to-reduce-performance-impact-boosts-neural-rendered-fps-up-to-127-percent-game-renders-on-one-card-neural-post-processing-runs-on-the-other-much-like-dedicated-physx-gpus",
    "domain": "AI 算力 / 半导体",
    "title": "Astonishing mod runs DLSS 5 on a second GPU to boost neural-rendered FPS up to 127% — game renders on one card, neural post-processing runs on the other, much like dedicated PhysX GPUs",
    "url": "https://www.tomshardware.com/pc-components/gpus/astonishing-mod-runs-nvidia-dlss-5-on-a-second-gpu-using-a-reshade-add-on-to-reduce-performance-impact-boosts-neural-rendered-fps-up-to-127-percent-game-renders-on-one-card-neural-post-processing-runs-on-the-other-much-like-dedicated-physx-gpus",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T12:33:56+00:00",
    "summary": "A modder has created a ReShade add-on that runs Nvidia's DLSS 5 Neural Rendering on a second GPU, rendering the game on the first GPU to share the performance load."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/montech-century-ii-gold-850w-atx-3-1-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "Montech Century II Gold 850W power supply review: Excellent budget-friendly Gold-tier ATX 3.1 unit with Cybenetics Platinum efficiency",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/montech-century-ii-gold-850w-atx-3-1-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T12:05:00+00:00",
    "summary": "At $90, the Montech Century II Gold 850W ATX 3.1 is a low-cost Gold-tier ATX 3.1 unit with a native 12V-2x6 connector, Cybenetics Platinum efficiency at both 115V and 230V input, and a matte silver ch"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/gta-vice-city-and-gta-iii-return-to-web-browsers-after-a-dmca-takedown-open-source-reverse-engineering-brings-the-classics-to-the-web-with-over-100-fps-performance",
    "domain": "AI 算力 / 半导体",
    "title": "GTA Vice City and GTA III return to web browsers after a DMCA takedown — Open-source reverse engineering brings the classics to the web with over 100 FPS performance",
    "url": "https://www.tomshardware.com/video-games/gta-vice-city-and-gta-iii-return-to-web-browsers-after-a-dmca-takedown-open-source-reverse-engineering-brings-the-classics-to-the-web-with-over-100-fps-performance",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T11:30:00+00:00",
    "summary": "You can play GTA: Vice City and GTA III in your browser right now across pretty much any modern device. The projects are compiled from source codes of the original games and are available on either DO"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/anycubic-photon-p1-max-review",
    "domain": "AI 算力 / 半导体",
    "title": "Anycubic Photon P1 MAX review: bigger, better, and tech-packed",
    "url": "https://www.tomshardware.com/3d-printing/anycubic-photon-p1-max-review",
    "source": "Matt Farmer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T11:05:00+00:00",
    "summary": "Anycubic’s Photon P1 MAX is the latest large resin printer, with new tech alongside its little brother, the P1. It sports a heated vat, Wave Release Technology, and a large, locking build plate and va"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/this-10-inch-4-3-television-hides-your-retro-consoles-in-a-secret-rear-compartment-unicos-traveller-ulw10-trades-composite-video-for-rgb-scart-and-hdmi",
    "domain": "AI 算力 / 半导体",
    "title": "This 10-inch 4:3 television hides your retro consoles in a secret rear compartment — Unico's Traveller ULW10 trades composite video for RGB SCART and HDMI",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/this-10-inch-4-3-television-hides-your-retro-consoles-in-a-secret-rear-compartment-unicos-traveller-ulw10-trades-composite-video-for-rgb-scart-and-hdmi",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T11:00:00+00:00",
    "summary": "The ULW10 Traveller offers retro gamers a compact alternative to modern widescreen TVs, complete with a 4:3 display and CRT-style visuals"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/start-your-3d-printing-journey-for-just-usd169-with-these-elegoo-printers-before-labor-day-ends-lock-in-up-to-35-percent-off-the-easy-to-use-neptune-3-pro-or-go-large-with-the-neptune-4-plus-for-massive-model-printing",
    "domain": "AI 算力 / 半导体",
    "title": "Start your 3D printing journey for just $169 with these Elegoo printers before Labor Day ends — lock in up to 35% off the easy-to-use Neptune 3 Pro or go large with the Neptune 4 Plus for massive mode",
    "url": "https://www.tomshardware.com/3d-printing/start-your-3d-printing-journey-for-just-usd169-with-these-elegoo-printers-before-labor-day-ends-lock-in-up-to-35-percent-off-the-easy-to-use-neptune-3-pro-or-go-large-with-the-neptune-4-plus-for-massive-model-printing",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T10:50:54+00:00",
    "summary": "Grab a huge discount on two of Elegoo's most popular 3D printers right now, with a price drop of up to 35%. Both the Elegoo Neptune 3 Pro and Neptune 4 Plus offer features that both beginners and enth"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/rpcs3-emulator-can-now-run-games-on-pc-directly-from-a-disc-drive-in-landmark-development-unlocks-20-years-of-physical-ps3-games-on-windows-linux-and-macos",
    "domain": "AI 算力 / 半导体",
    "title": "RPCS3 emulator can now run PS3 games on PC directly from a disc drive in landmark development — unlocks 20 years of physical titles on Windows, Linux, and macOS",
    "url": "https://www.tomshardware.com/video-games/playstation/rpcs3-emulator-can-now-run-games-on-pc-directly-from-a-disc-drive-in-landmark-development-unlocks-20-years-of-physical-ps3-games-on-windows-linux-and-macos",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T10:47:25+00:00",
    "summary": "The developers of the Sony PlayStation 3 emulator RPCS3 have told their social media followers that it is now possible to play games straight from discs."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/flea-market-shopper-uncovers-usd1-500-worth-of-samsung-ssds-inside-a-usd30-expansion-card-three-2tb-980-pro-drives-were-hidden-beneath-an-asus-hyper-m-2-heatsink",
    "domain": "AI 算力 / 半导体",
    "title": "Flea market shopper uncovers $1,500 worth of Samsung SSDs inside a $30 expansion card — Three 2TB 980 Pro drives were hidden beneath an Asus Hyper M.2 heatsink",
    "url": "https://www.tomshardware.com/pc-components/ssds/flea-market-shopper-uncovers-usd1-500-worth-of-samsung-ssds-inside-a-usd30-expansion-card-three-2tb-980-pro-drives-were-hidden-beneath-an-asus-hyper-m-2-heatsink",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T10:30:00+00:00",
    "summary": "An extremely fortunate bargain hunter in Kuwait found three Samsung 980 Pro 2TB SSDs slotted inside a $30 PCIe expansion card. Each of those drives is worth between $400 and $500, so it's clear to say"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/this-price-hike-busting-rtx-5080-gaming-pc-is-cheaper-than-it-was-in-april-save-usd500-on-a-9800x3d-beast-with-32gb-of-ddr5-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "This price-hike-busting RTX 5080 gaming PC is cheaper than it was in April — save $500 on a 9800X3D beast with 32GB of DDR5, 2TB SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/this-price-hike-busting-rtx-5080-gaming-pc-is-cheaper-than-it-was-in-april-save-usd500-on-a-9800x3d-beast-with-32gb-of-ddr5-2tb-ssd",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T10:27:52+00:00",
    "summary": "Get an RTX 5080 gaming PC with a 9800X3D CPU for less than $3,000."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/enthusiast-says-dlss-5-pushed-rtx-5090-past-600w-and-melted-the-16-pin-connector-nvidias-neural-rendering-tech-adds-up-to-50-percent-more-power-draw-in-testing",
    "domain": "AI 算力 / 半导体",
    "title": "Enthusiast says DLSS 5 pushed RTX 5090 past 600W and melted the 16-pin connector — Nvidia's neural rendering tech adds up to 50% more power draw in testing",
    "url": "https://www.tomshardware.com/pc-components/gpus/enthusiast-says-dlss-5-pushed-rtx-5090-past-600w-and-melted-the-16-pin-connector-nvidias-neural-rendering-tech-adds-up-to-50-percent-more-power-draw-in-testing",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T10:00:00+00:00",
    "summary": "Another RTX 5090 has gone down but this time it has something else to blame other than its own 16-pin connector. The connector is still what melted but potentially because of DLSS 5 pulling way too mu"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/single-slot-low-profile-75w-rtx-3060-with-no-power-connectors-disappoints-in-tests-gpu-runs-entirely-off-the-pcie-slot-but-offers-severely-crippled-performance-and-frightening-thermals",
    "domain": "AI 算力 / 半导体",
    "title": "Single-slot low-profile 75W RTX 3060 with no power connectors disappoints in tests — GPU runs entirely off the PCIe slot, but offers severely crippled performance and frightening thermals",
    "url": "https://www.tomshardware.com/pc-components/gpus/single-slot-low-profile-75w-rtx-3060-with-no-power-connectors-disappoints-in-tests-gpu-runs-entirely-off-the-pcie-slot-but-offers-severely-crippled-performance-and-frightening-thermals",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T14:58:29+00:00",
    "summary": "If you want to cut your 12GB RTX 3060's performance in half while worsening its thermals, this might be the perfect product for you."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-admits-to-wiki-incident-after-its-agents-were-discovered-using-a-programming-hub-to-communicate-says-more-transparency-is-needed-regarding-misalignments",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI admits to 'wiki incident' after its agents were discovered using a programming hub to communicate — says more transparency is needed regarding misalignments",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-admits-to-wiki-incident-after-its-agents-were-discovered-using-a-programming-hub-to-communicate-says-more-transparency-is-needed-regarding-misalignments",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T14:31:54+00:00",
    "summary": "OpenAI has admitted that its experimental AI agents used an open German programming wiki to communicate."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/fsp-mega-gm-1200w-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "FSP Mega GM 1200W power supply review: An in-house FSP platform that quietly overshoots its own Gold label",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/fsp-mega-gm-1200w-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T13:57:18+00:00",
    "summary": "The FSP Mega GM 1200W power supply features Platinum-grade efficiency, an all-Japanese capacitor set, and a compact footprint that is rare on a 1200W unit."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/bitcoin-mining-data-center-condemned-after-leaking-3-million-gallons-of-water-and-forcing-school-closures-facility-operated-for-years-under-a-city-stop-work-order",
    "domain": "AI 算力 / 半导体",
    "title": "Bitcoin mining data center condemned after leaking 3 million gallons of water and forcing school closures — facility operated for years under a city stop-work order",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/bitcoin-mining-data-center-condemned-after-leaking-3-million-gallons-of-water-and-forcing-school-closures-facility-operated-for-years-under-a-city-stop-work-order",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T13:44:22+00:00",
    "summary": "A Bitcoin mining data center in El Reno, Oklahoma has been condemned after it leaked 3 million gallons of water."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/samsung-990-2tb-pcie-4-0-ssd-falls-to-usd339-99-on-amazon-usd190-discount-makes-high-capacity-storage-more-affordable",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung 990 2TB PCIe 4.0 SSD falls to $339.99 on Amazon — $190 discount makes high-capacity storage more affordable",
    "url": "https://www.tomshardware.com/pc-components/ssds/samsung-990-2tb-pcie-4-0-ssd-falls-to-usd339-99-on-amazon-usd190-discount-makes-high-capacity-storage-more-affordable",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T13:08:31+00:00",
    "summary": "Samsung's 2TB 990 offers plenty of fast storage for games and is currently $190 cheaper than its regular $529.99 price."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/liquid-cooling/msi-meg-coreliquid-e15-360-aio-review-bold-and-stunning-with-market-leading-performance",
    "domain": "AI 算力 / 半导体",
    "title": "MSI MEG CoreLiquid E15 360 AIO Review: Bold and stunning, with market-leading performance",
    "url": "https://www.tomshardware.com/pc-components/liquid-cooling/msi-meg-coreliquid-e15-360-aio-review-bold-and-stunning-with-market-leading-performance",
    "source": "Albert Thomas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T12:48:03+00:00",
    "summary": "MSI’s MEG CoreLiquid E15 360 AIO is a luxury cooling product, with a stunning 6.7-inch screen and industry-leading thermal performance."
  },
  {
    "id": "rss:https://www.tomshardware.com/service-providers/streaming/sales-of-cd-and-vinyl-music-sees-strong-resurgence-amid-physical-media-backlash-us-sales-of-retro-media-were-up-59-percent-and-18-percent-respectively-in-h1-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Sales of CD and vinyl music sees strong resurgence amid physical media backlash — US sales of ‘retro media’ were up 59% and 18%, respectively, in H1 2026",
    "url": "https://www.tomshardware.com/service-providers/streaming/sales-of-cd-and-vinyl-music-sees-strong-resurgence-amid-physical-media-backlash-us-sales-of-retro-media-were-up-59-percent-and-18-percent-respectively-in-h1-2026",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T12:16:13+00:00",
    "summary": "Music industry physical revenues jumped by 25.9% in H1 2026, 'powered by 17.7% vinyl growth and a 58.6% increase in CDs,' reported the RIAA."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/ps5-emulator-can-now-run-the-console-version-of-gta-v-at-up-to-60-fps-on-pc-but-quickly-crashes-as-tweakers-continue-to-optimize-ps5-emulation-advancing-at-an-astronomical-pace-leading-up-to-gta-vi-launch",
    "domain": "AI 算力 / 半导体",
    "title": "PS5 emulator can now run the console version of GTA V at up to 60 FPS on PC, but quickly crashes as tweakers continue to optimize — PS5 emulation advancing at an astronomical pace leading up to GTA VI",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/ps5-emulator-can-now-run-the-console-version-of-gta-v-at-up-to-60-fps-on-pc-but-quickly-crashes-as-tweakers-continue-to-optimize-ps5-emulation-advancing-at-an-astronomical-pace-leading-up-to-gta-vi-launch",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T11:48:08+00:00",
    "summary": "A spark was lit under the PS5 emulation scene a couple of months ago and instead of fading over time, it seems to be burning brighter than ever. GTA V now runs between 40-60 FPS for a few minutes befo"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/former-old-school-runescape-dev-gets-jail-time-for-stealing-usd400-000-from-players-virtual-gold-stolen-and-sold-on-the-black-market-before-jagex-caught-the-culprit-using-hidden-firewall-tweaks",
    "domain": "AI 算力 / 半导体",
    "title": "Former Old School RuneScape dev gets jail time for stealing $400,000 from players — virtual gold stolen and sold on the black market before Jagex caught the culprit using hidden firewall tweaks",
    "url": "https://www.tomshardware.com/video-games/former-old-school-runescape-dev-gets-jail-time-for-stealing-usd400-000-from-players-virtual-gold-stolen-and-sold-on-the-black-market-before-jagex-caught-the-culprit-using-hidden-firewall-tweaks",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T10:30:00+00:00",
    "summary": "A former Jagex employee stole over $400,000 worth of in-game items and virtual currency from OSRS players and sold them on the black market. He was eventually arrested and sentenced to a three-year pr"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/storage/this-246tb-ssd-media-server-is-built-for-millionaire-cinephiles-kaleidescapes-newest-home-theater-vault-supports-25-simultaneous-4k-streams-stores-up-to-2-300-4k-cinematic-movies",
    "domain": "AI 算力 / 半导体",
    "title": "This 246TB SSD media server is built for millionaire cinephiles —Kaleidescape's newest home theater vault supports 25 simultaneous 4K streams, stores up to 2,300 4K cinematic movies",
    "url": "https://www.tomshardware.com/pc-components/storage/this-246tb-ssd-media-server-is-built-for-millionaire-cinephiles-kaleidescapes-newest-home-theater-vault-supports-25-simultaneous-4k-streams-stores-up-to-2-300-4k-cinematic-movies",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T10:00:00+00:00",
    "summary": "Kaleidescape, a maker of luxury home theater equipment, has revealed its latest media server, the \"Compact Terra Prime 246TB SSD.\""
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
    "id": "rss:https://www.eetimes.com/ee-times-magazine-september-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "EE Times Magazine – September 2026",
    "url": "https://www.eetimes.com/ee-times-magazine-september-2026/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-04T22:40:26+00:00",
    "summary": "The September 2026 edition of EE Times Magazine examines how smarter buildings combine ambient energy harvesting, sensing, AI, and connected systems to improve safety while protecting privacy. The pos"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-nearly-50-percent-on-this-awesome-16-inch-oled-laptop-with-a-ryzen-ai-5-430-cpu-and-16gb-ram-hps-macbook-neo-beating-omnibook-x-flip-is-down-to-just-usd699",
    "domain": "AI 算力 / 半导体",
    "title": "Save nearly 50% on this awesome 16-inch OLED laptop with a Ryzen AI 5 430 CPU & 16GB RAM — HP's MacBook Neo-beating OmniBook X Flip is down to just $699",
    "url": "https://www.tomshardware.com/pc-components/save-nearly-50-percent-on-this-awesome-16-inch-oled-laptop-with-a-ryzen-ai-5-430-cpu-and-16gb-ram-hps-macbook-neo-beating-omnibook-x-flip-is-down-to-just-usd699",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T18:51:54+00:00",
    "summary": "If you're looking for a capable machine for everyday tasks and media consumption without breaking the bank, there isn't a better deal out there than this one."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/stripped-down-windows-11-for-ai-developers-demands-64gb-ram-and-insane-250-gb-s-bandwidth-project-zenith-will-debut-on-amds-flagship-ryzen-ai-halo-platform",
    "domain": "AI 算力 / 半导体",
    "title": "Stripped-down Windows 11 for AI developers demands 64GB RAM and insane 250 GB/s bandwidth — Project Zenith will debut on AMD's flagship Ryzen AI Halo platform",
    "url": "https://www.tomshardware.com/software/windows/stripped-down-windows-11-for-ai-developers-demands-64gb-ram-and-insane-250-gb-s-bandwidth-project-zenith-will-debut-on-amds-flagship-ryzen-ai-halo-platform",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T17:18:57+00:00",
    "summary": "Project Zenith is a version of Windows 11 that lets developers work right out of the box. It comes pre-installed with developer tools like Visual Studio Code, GitHub Copilot, and WSL 2+ Ubuntu, among "
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/gamescom-apologizes-after-backlash-over-callous-response-to-indie-dev-hardware-thefts-pledges-security-overhaul-and-invites-devs-to-the-roundtable",
    "domain": "AI 算力 / 半导体",
    "title": "Gamescom apologizes after backlash over callous response to indie dev hardware thefts — pledges security overhaul and invites devs to the roundtable",
    "url": "https://www.tomshardware.com/video-games/gamescom-apologizes-after-backlash-over-callous-response-to-indie-dev-hardware-thefts-pledges-security-overhaul-and-invites-devs-to-the-roundtable",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T16:18:54+00:00",
    "summary": "The Gamescom organizers apologized for their initial response and outlined plans to prevent future incidents. They also praised the community for supporting the affected developers."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-returns-to-selling-founders-edition-rtx-50-series-gpus-at-msrp-in-person-at-pax-west-verified-priority-access-has-rtx-5090-rtx-5080-and-rtx-5070-at-list-price",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia returns to selling Founder's Edition RTX 50-series GPUs at MSRP in person at PAX West — Verified Priority Access has RTX 5090, RTX 5080, and RTX 5070 at list price",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-returns-to-selling-founders-edition-rtx-50-series-gpus-at-msrp-in-person-at-pax-west-verified-priority-access-has-rtx-5090-rtx-5080-and-rtx-5070-at-list-price",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T15:04:13+00:00",
    "summary": "Nvidia is offering its RTX 5090, RTX 5080, and RTX 5070 Founder's Edition models at MSRP at PAX West."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-reportedly-prepping-ryzen-5-7500-non-f-cpu-with-integrated-graphics-at-double-the-price-six-core-zen-4-chip-rumored-to-share-identical-specs-with-its-f-moniker-cousin",
    "domain": "AI 算力 / 半导体",
    "title": "AMD reportedly prepping Ryzen 5 7500 (non-F) CPU with integrated graphics at double the price — Six-core Zen 4 chip rumored to share identical specs with its F-moniker cousin",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-reportedly-prepping-ryzen-5-7500-non-f-cpu-with-integrated-graphics-at-double-the-price-six-core-zen-4-chip-rumored-to-share-identical-specs-with-its-f-moniker-cousin",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-05T13:09:23+00:00",
    "summary": "A new report suggests AMD is preparing a non-F version of the Ryzen 5 7500F with integrated graphics. It would cost 230 Euros, or $267, which would put it above even the 7600X3D in terms of pricing, d"
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
    "id": "hn:49447878",
    "domain": "AI 算力 / 半导体",
    "title": "Who bears the risk in Nvidia's $500B financing platform?",
    "url": "https://www.sascha-steffen.de/updates/nvidia-500bn-ai-financing-credit-risk",
    "source": "rwmj",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-08-26T12:32:31+00:00",
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
    "id": "hn:49537553",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Flash and 3.8 Flash Cyber",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/",
    "source": "bratao",
    "platform": "hackernews",
    "points": 1158,
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
    "id": "hn:49552299",
    "domain": "大厂 AI 动态",
    "title": "WeatherNext 3",
    "url": "https://deepmind.google/science/weathernext/",
    "source": "matthieu_bl",
    "platform": "hackernews",
    "points": 314,
    "published_at": "2026-09-03T16:06:08+00:00",
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
    "id": "hn:49602490",
    "domain": "大厂 AI 动态",
    "title": "Emacs Bedrock 2.0",
    "url": "https://lambdaland.org/posts/2026-09-06-bedrock-v2/",
    "source": "ashton314",
    "platform": "hackernews",
    "points": 102,
    "published_at": "2026-09-07T20:12:12+00:00",
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
    "id": "hn:49566788",
    "domain": "大厂 AI 动态",
    "title": "Project HydraFusion: Frontier quality via multi-model orchestration",
    "url": "https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/",
    "source": "qainsights",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-09-04T16:24:50+00:00",
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
    "id": "hn:49604257",
    "domain": "大厂 AI 动态",
    "title": "WeatherNext 3: Our most advanced global weather AI model",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-weathernext-3/",
    "source": "gmays",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-09-07T23:56:41+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/991008/xiaomi-18-fold-hands-on-impressions-specs-wide",
    "domain": "大厂 AI 动态",
    "title": "Xiaomi’s wide foldable promises more power than Samsung’s",
    "url": "https://www.theverge.com/tech/991008/xiaomi-18-fold-hands-on-impressions-specs-wide",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T07:00:00+00:00",
    "summary": "Xiaomi is the latest manufacturer to release a short, wide foldable phone, in the week Apple is expected to do the same. I got to try the 18 Fold behind closed doors at IFA last week, and while it loo"
  },
  {
    "id": "rss:https://www.theverge.com/games/990676/arm-neural-rendering-mali-g2-ultra-xiaomi-xring-o3",
    "domain": "大厂 AI 动态",
    "title": "First Xiaomi, then the world: why Arm might give phone gaming a huge graphics boost",
    "url": "https://www.theverge.com/games/990676/arm-neural-rendering-mali-g2-ultra-xiaomi-xring-o3",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T02:00:00+00:00",
    "summary": "China is getting first crack at a British technology that might change how mobile games are made and played. Today, the Xiaomi 18 Fold launches in mainland China with an Arm Mali G2-Ultra NX graphics "
  },
  {
    "id": "rss:https://www.theverge.com/transportation/991081/audi-a2-etron-ev-specs-price",
    "domain": "大厂 AI 动态",
    "title": "Audi’s new A2 E-tron is its most affordable and efficient EV yet",
    "url": "https://www.theverge.com/transportation/991081/audi-a2-etron-ev-specs-price",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T20:03:41+00:00",
    "summary": "When shopping for an electric vehicle, affordability is becoming a more common trait. But affordable and energy efficient is truly a rare breed. Often you have to sacrifice one for the other. Want som"
  },
  {
    "id": "rss:https://www.theverge.com/tech/990687/sony-announces-xm4c-headphones",
    "domain": "大厂 AI 动态",
    "title": "Six years later, Sony revisits its legendary XM4 headphones",
    "url": "https://www.theverge.com/tech/990687/sony-announces-xm4c-headphones",
    "source": "John.Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T16:00:00+00:00",
    "summary": "Six years ago Sony and Bose were in the middle of a noise-canceling battle, with each new model of headphones better than the last. In the fall of 2020, Sony released the WH-1000XM4 headphones to wide"
  },
  {
    "id": "rss:https://www.theverge.com/science/991033/ecoflow-makes-the-miniature-power-station-even-smaller",
    "domain": "大厂 AI 动态",
    "title": "EcoFlow makes the miniature power station even smaller",
    "url": "https://www.theverge.com/science/991033/ecoflow-makes-the-miniature-power-station-even-smaller",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T14:59:41+00:00",
    "summary": "If you're in the market for a tiny power station that punches well above its size and weight then have a look at EcoFlow's new fourth-generation River series. The River 260 Gen4 features a 256Wh capac"
  },
  {
    "id": "rss:https://www.theverge.com/tech/988225/ram-shortage-supply-chain-micron-apple-iphone",
    "domain": "大厂 AI 动态",
    "title": "The real reason your phone is getting more expensive",
    "url": "https://www.theverge.com/tech/988225/ram-shortage-supply-chain-micron-apple-iphone",
    "source": "Rani Molla",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T12:00:00+00:00",
    "summary": "When Apple debuts the next generation of iPhones this week, they're likely to come with an unwanted change: a higher price tag. A price hike from the supply-chain powerhouse would be the clearest sign"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/990319/bentley-torcal-ev-power-ride-sound-v8",
    "domain": "大厂 AI 动态",
    "title": "Bentley’s Torcal EV tries to balance authenticity with fake V8 sounds",
    "url": "https://www.theverge.com/transportation/990319/bentley-torcal-ev-power-ride-sound-v8",
    "source": "Peter Nelson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T11:00:00+00:00",
    "summary": "Thanks to their ability to provide a smooth ride and quiet powertrain with ease, electric vehicles are a true shoo-in for the high-end luxury automotive segment. Rolls-Royce has the Spectre, Cadillac'"
  },
  {
    "id": "rss:https://www.theverge.com/tech/990958/huawei-mate-xt-2-trifold-launch-china-privacy-display",
    "domain": "大厂 AI 动态",
    "title": "Huawei copies Samsung’s privacy display in its latest trifold",
    "url": "https://www.theverge.com/tech/990958/huawei-mate-xt-2-trifold-launch-china-privacy-display",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T10:09:42+00:00",
    "summary": "Huawei has released its third trifold phone in China, and the company has clearly had half an eye on Samsung during development. Not only does the Mate XT 2 adopt the inward-folding form factor used o"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/990932/seattle-times-newsday-lawsuit-openai-microsoft",
    "domain": "大厂 AI 动态",
    "title": "Seattle Times and Newsday sue OpenAI and Microsoft for infringement",
    "url": "https://www.theverge.com/ai-artificial-intelligence/990932/seattle-times-newsday-lawsuit-openai-microsoft",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T23:36:04+00:00",
    "summary": "The Seattle Times and Newsday are just the latest plaintiffs to take OpenAI to court, alleging copyright infringement. The two outlets say the company used their journalism as training data for its AI"
  },
  {
    "id": "rss:https://www.theverge.com/tech/990918/amazon-cargo-plane-crashed-miami",
    "domain": "大厂 AI 动态",
    "title": "An Amazon cargo plane crashed at Miami International Airport",
    "url": "https://www.theverge.com/tech/990918/amazon-cargo-plane-crashed-miami",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T20:56:38+00:00",
    "summary": "A plane bearing an Amazon logo overran the runway at Miami International Airport on Sunday during landing, crashing into vehicles and resulting in multiple injuries. The extent of the damage or the se"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/07/eric-wus-newest-company-out-of-stealth-since-may-is-going-after-constructions-labor-crunch/",
    "domain": "大厂 AI 动态",
    "title": "Eric Wu’s newest company, out of stealth since May, is going after construction’s labor crunch",
    "url": "https://techcrunch.com/2026/09/07/eric-wus-newest-company-out-of-stealth-since-may-is-going-after-constructions-labor-crunch/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T02:16:39+00:00",
    "summary": "Eric Wu, who built and ran Opendoor before stepping away in 2022, has had his new company, NavigateAI, out of stealth since May — building AI copilots that give construction workers real-time, hands-f"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/07/artificial-intelligence-definition-glossary-hallucinations-guide-to-common-ai-terms/",
    "domain": "大厂 AI 动态",
    "title": "Opaque recurrence, and other AI terms that you should probably know",
    "url": "https://techcrunch.com/2026/09/07/artificial-intelligence-definition-glossary-hallucinations-guide-to-common-ai-terms/",
    "source": "Natasha Lomas, Romain Dillet, Kyle Wiggers, Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T19:24:00+00:00",
    "summary": "The rise of AI has brought an avalanche of new terms and slang. Here is a glossary with definitions of some of the most important words and phrases you might encounter."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/07/a-secret-new-elizabeth-holmes-documentary-stuns-telluride/",
    "domain": "大厂 AI 动态",
    "title": "A secret new Elizabeth Holmes documentary stuns Telluride",
    "url": "https://techcrunch.com/2026/09/07/a-secret-new-elizabeth-holmes-documentary-stuns-telluride/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T18:02:29+00:00",
    "summary": "Nathan Fielder and Lance Oppenheim's secret Elizabeth Holmes documentary, \"You Can See Everything,\" stunned Telluride audiences Sunday night with its generous access to the Theranos founder."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/07/what-we-expect-from-the-upcoming-apple-launch/",
    "domain": "大厂 AI 动态",
    "title": "What we expect from the upcoming Apple launch",
    "url": "https://techcrunch.com/2026/09/07/what-we-expect-from-the-upcoming-apple-launch/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T15:58:00+00:00",
    "summary": "While Apple's first foldable iPhone Ultra will headline the September 9 launch, we're also expecting news about AirPods and HomePods."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/06/phil-schillers-app-store-exit-reportedly-driven-by-wariness-over-future-plans/",
    "domain": "大厂 AI 动态",
    "title": "Phil Schiller’s App Store exit reportedly driven by wariness over future plans",
    "url": "https://techcrunch.com/2026/09/06/phil-schillers-app-store-exit-reportedly-driven-by-wariness-over-future-plans/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T21:41:06+00:00",
    "summary": "Schiller reportedly had reservations about new CEO John Ternus' goal of bringing in more recurring revenue from the App Store."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/06/authors-push-back-as-publishers-and-agents-seek-share-of-anthropic-settlement/",
    "domain": "大厂 AI 动态",
    "title": "Authors push back as publishers and agents make claims on Anthropic settlement",
    "url": "https://techcrunch.com/2026/09/06/authors-push-back-as-publishers-and-agents-seek-share-of-anthropic-settlement/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T20:47:37+00:00",
    "summary": "Authors say publishers seem to be claiming more than their fair share of settlement payments."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/06/travis-kalanicks-atoms-might-be-getting-into-the-robotaxi-business/",
    "domain": "大厂 AI 动态",
    "title": "Travis Kalanick’s Atoms might be getting into the robotaxi business",
    "url": "https://techcrunch.com/2026/09/06/travis-kalanicks-atoms-might-be-getting-into-the-robotaxi-business/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T16:45:00+00:00",
    "summary": "The Uber founder has said that Atoms will allow him to complete \"unfinished business.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/06/techcrunch-mobility-tesla-cybercab-hits-the-road-and-a-snag/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Mobility: Tesla Cybercab hits the road — and a snag",
    "url": "https://techcrunch.com/2026/09/06/techcrunch-mobility-tesla-cybercab-hits-the-road-and-a-snag/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T16:08:00+00:00",
    "summary": "Welcome back to TechCrunch Mobility, your hub for the future of transportation and now, more than ever, the role AI is playing in it."
  },
  {
    "id": "rss:https://arstechnica.com/features/2026/09/the-ai-data-center-boom-is-causing-new-accountability-problems/",
    "domain": "大厂 AI 动态",
    "title": "The complex corporate web behind a $3.2 billion AI data center",
    "url": "https://arstechnica.com/features/2026/09/the-ai-data-center-boom-is-causing-new-accountability-problems/",
    "source": "Petala Ironcloud",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T11:00:03+00:00",
    "summary": "When multiple companies are behind one project, who bears responsibility for problems?"
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/09/german-company-becomes-first-in-europe-to-launch-fully-commercial-orbital-rocket/",
    "domain": "大厂 AI 动态",
    "title": "German company becomes first in Europe to launch fully commercial orbital rocket",
    "url": "https://arstechnica.com/space/2026/09/german-company-becomes-first-in-europe-to-launch-fully-commercial-orbital-rocket/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T11:55:26+00:00",
    "summary": "\"We achieved within a few years what had taken the European space industry decades before.\""
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/09/farmed-salmon-may-not-be-as-nutritious-as-it-once-was-new-research-suggests/",
    "domain": "大厂 AI 动态",
    "title": "Farmed salmon may not be as nutritious as it once was, new research suggests",
    "url": "https://arstechnica.com/science/2026/09/farmed-salmon-may-not-be-as-nutritious-as-it-once-was-new-research-suggests/",
    "source": "Georgina Gustin, Inside Climate News",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T10:00:35+00:00",
    "summary": "The shift in the fish’s diet is having significant downstream impacts on the environment and climate."
  },
  {
    "id": "rss:https://www.producthunt.com/products/catenary",
    "domain": "大厂 AI 动态",
    "title": "Catenary",
    "url": "https://www.producthunt.com/products/catenary",
    "source": "Giorgio Nícolas",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T02:32:49+00:00",
    "summary": "Spatial canvas IDE for AI coding agents Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/kopai-the-marketplace-for-ai-agents",
    "domain": "大厂 AI 动态",
    "title": "Kopai",
    "url": "https://www.producthunt.com/products/kopai-the-marketplace-for-ai-agents",
    "source": "Surya Sekhar Datta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T17:45:34+00:00",
    "summary": "The Cloud for AI Agents Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/tables-so",
    "domain": "大厂 AI 动态",
    "title": "Tables.so",
    "url": "https://www.producthunt.com/products/tables-so",
    "source": "Jens Bjerregaard",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T15:50:49+00:00",
    "summary": "AI that finds, qualifies and enriches your next customer Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/knockin",
    "domain": "大厂 AI 动态",
    "title": "Knockin'",
    "url": "https://www.producthunt.com/products/knockin",
    "source": "Zac Zuo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T05:02:45+00:00",
    "summary": "Turns your static bio into an AI business card that replies. Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/lyrimuse",
    "domain": "大厂 AI 动态",
    "title": "Lyrimuse",
    "url": "https://www.producthunt.com/products/lyrimuse",
    "source": "Khalil",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T17:58:59+00:00",
    "summary": "Word-synced macOS lyrics that pick the right version Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/trancy-air",
    "domain": "大厂 AI 动态",
    "title": "Trancy Air",
    "url": "https://www.producthunt.com/products/trancy-air",
    "source": "Elidi Martin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T02:16:29+00:00",
    "summary": "Translate anything you see, write, or say with one hotkey Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/minicpm-4-0",
    "domain": "大厂 AI 动态",
    "title": "MiniCPM5-2B",
    "url": "https://www.producthunt.com/products/minicpm-4-0",
    "source": "Zac Zuo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T04:55:38+00:00",
    "summary": "Small enough for the device, built to act Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/good-lads-1-0",
    "domain": "大厂 AI 动态",
    "title": "GoodLads",
    "url": "https://www.producthunt.com/products/good-lads-1-0",
    "source": "Pavel Kucherbaev",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T11:11:39+00:00",
    "summary": "AI growth manager for your Google Ads account Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/airuncode",
    "domain": "大厂 AI 动态",
    "title": "Airuncode",
    "url": "https://www.producthunt.com/products/airuncode",
    "source": "GUSTAVO ARRETURETA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T23:16:55+00:00",
    "summary": "Run multiple local coding agents on your machine Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/remind-7",
    "domain": "大厂 AI 动态",
    "title": "Remind",
    "url": "https://www.producthunt.com/products/remind-7",
    "source": "Chris Doyle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T16:10:46+00:00",
    "summary": "Full-screen meeting reminders with AI briefings Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/tucky",
    "domain": "大厂 AI 动态",
    "title": "Tucky",
    "url": "https://www.producthunt.com/products/tucky",
    "source": "Mehdi Harzallah",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-06T21:09:48+00:00",
    "summary": "Notes docked to your screen edge, with an AI agent inside Discussion | Link"
  },
  {
    "id": "rss:https://www.producthunt.com/products/clipnote-2",
    "domain": "大厂 AI 动态",
    "title": "Clipnote",
    "url": "https://www.producthunt.com/products/clipnote-2",
    "source": "Okumura Daichi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T01:55:40+00:00",
    "summary": "Save your AI conversations so they persist after closing tab Discussion | Link"
  },
  {
    "id": "rss:https://sspai.com/post/113299",
    "domain": "大厂 AI 动态",
    "title": "日本浮生录 11｜越过九州，走进奄美大岛的山海夏日",
    "url": "https://sspai.com/post/113299",
    "source": "SIMON_",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T03:06:21+00:00",
    "summary": "浪还在继续往岸边来，天色也一点一点暗下去。就让奄美大岛和我的这个夏天，停留在这里吧。查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/114307",
    "domain": "大厂 AI 动态",
    "title": "派早报：华为举办 HarmonyOS 7 | HUAWEI Mate XT 2 及全场景新品发布会等",
    "url": "https://sspai.com/post/114307",
    "source": "少数派编辑部",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T00:07:33+00:00",
    "summary": "少数派的近期动态全新iPhone发布在即，来与少数派一起看Apple发布会口袋先知新版本1.3.3上线，你可以自定义任何你想展示的屏幕效果。了解更多能让AI助手通过自然语言指令直接与您的Quote/0 ...查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/114288",
    "domain": "大厂 AI 动态",
    "title": "派评｜近期值得关注的 App",
    "url": "https://sspai.com/post/114288",
    "source": "少数派编辑部",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T10:08:44+00:00",
    "summary": ">下载少数派客户端、关注少数派公众号，解锁全新阅读体验📰>实用、好用的正版软件，少数派为你呈现🚀查看全文"
  },
  {
    "id": "rss:https://sspai.com/post/113877",
    "domain": "大厂 AI 动态",
    "title": "「弯道超车」赛车入门指北 04：全场最快的车，为什么听一辆慢车指挥",
    "url": "https://sspai.com/post/113877",
    "source": "一群小羊说",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-07T07:00:00+00:00",
    "summary": "一辆远没有 F1 赛车快的车，凭什么让各路豪强乖乖排在后面，甚至左右冠军归属？查看全文"
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
    "id": "wscn:3781308",
    "domain": "股票",
    "title": "报道：津巴布韦暂停锑和钨出口以推动本土加工",
    "url": "https://wallstreetcn.com/articles/3781308",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T07:48:03+00:00",
    "summary": "更多消息，持续更新中"
  },
  {
    "id": "wscn:3781304",
    "domain": "股票",
    "title": "中国8月原油进口量环比增长6.2%，精铜与铜精矿进口量同比下降10%，集成电路出口金额同比飙升130%",
    "url": "https://wallstreetcn.com/articles/3781304",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T07:33:39+00:00",
    "summary": "进口数据的核心亮点集中于科技领域，印证了中国在关键技术领域的持续押注。随着中东局势持续紧张，原油进口亦有所回升，国内汽油、柴油等成品油海外销量较7月大幅攀升。"
  },
  {
    "id": "wscn:3781303",
    "domain": "股票",
    "title": "布油逼近100大关！胡塞武装深入内陆，打击沙特能源设施",
    "url": "https://wallstreetcn.com/articles/3781303",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T07:32:15+00:00",
    "summary": "胡塞武装扩大袭击范围，沙特多地能源设施起火、部分运营中断，70余人受伤。叠加霍尔木兹运输受阻与伊朗强硬表态，供应中断忧虑骤升，布伦特原油大涨至98.65美元，逼近100美元关口。"
  },
  {
    "id": "wscn:3781291",
    "domain": "股票",
    "title": "沙特能源设施遭袭推升油价，日元升至六个月高位，美股期指涨跌互现，黄金冲高回落",
    "url": "https://wallstreetcn.com/articles/3781291",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T07:31:39+00:00",
    "summary": "道指期货跌0.7%，纳斯达克100指数期货涨0.2%，日韩股市收跌。美元走弱，日元盘中升至152.89，创2月以来最高水平。现货黄金跌0.1%，此前一度涨0.7%，伦铜期货周二再创历史新高。WTI原油日内涨超2%，布伦特原油日内涨1.8%，报98.73美元/桶。"
  },
  {
    "id": "wscn:3781305",
    "domain": "股票",
    "title": "特朗普发图：新墨西哥州改名“新美国州”，给整个北美洲刷上“星条旗”",
    "url": "https://wallstreetcn.com/articles/3781305",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T07:18:14+00:00",
    "summary": "特朗普发图支持将新墨西哥州更名“新美国州”，并配发AI生成视频，亲自“贴纸”覆盖路牌庆祝。另一张图更将整个北美洲——包括加拿大、墨西哥——全部刷上星条旗。新墨西哥州长强硬拒绝，斥其转移视线。此前特朗普已相继将墨西哥湾改名“美国湾”、安大略湖改名“美国湖”。"
  },
  {
    "id": "wscn:3781306",
    "domain": "股票",
    "title": "中国扩大灵活就业人员等群体基本医保参保规模，缴费年限可以按月累计",
    "url": "https://wallstreetcn.com/articles/3781306",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T07:07:14+00:00",
    "summary": "通知称，在保证医保基金收支平衡的基础上，各地可参照当地职工基本养老保险缴费基数，合理确定灵活就业人员的医保缴费基数。灵活就业人员参加职工医保，缴费年限可以按月累计，每满12个月折算为1年缴费年限。"
  },
  {
    "id": "wscn:3781217",
    "domain": "股票",
    "title": "铜价为何历史新高？主流铜企Q2产量下滑，供给收缩全年指引下调！",
    "url": "https://wallstreetcn.com/premium/articles/3781217?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T06:47:54+00:00",
    "summary": "2026年上半年，全球49家样本铜企产量合计819.6万吨，同比下滑4.3%，减量37.1万吨；二季度同比降幅进一步扩大至4.5%，供给收缩非但未缓解，反而在加深。"
  },
  {
    "id": "wscn:3781300",
    "domain": "股票",
    "title": "理想全速推进自研、车企集体引入“二供”，动力电池行业要变天了？",
    "url": "https://wallstreetcn.com/articles/3781300",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T06:36:55+00:00",
    "summary": "理想汽车26.5亿元入股欣旺达动力、全系加速切换自研电池，直指“去宁德时代化”。鸿蒙智行、小米、小鹏等也密集引入二供多供，电池价格与供应链话语权重构；但宁德时代市占仍超50%，“宁王”地位尚未动摇。"
  },
  {
    "id": "wscn:3781297",
    "domain": "股票",
    "title": "美联储加息概率升至60%、油价逼近100美元，金价为何逆势反弹？",
    "url": "https://wallstreetcn.com/articles/3781297",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T06:03:55+00:00",
    "summary": "美元走软提供关键支撑，现货黄金周二触及每盎司4435美元，抹去前日跌幅。油价逼近百元关口、美联储下周加息概率升至60%，双重压力下涨势受限。本周CPI数据将成最大变量。机构已重建多头仓位，央行购金与美元多元化逻辑持续发酵，但下一波上行或需新的宏观催化剂。"
  },
  {
    "id": "wscn:3781290",
    "domain": "股票",
    "title": "苹果罕见签3-5年NAND长约、或不设价格上限，AI挤占产能令存储议价权易主",
    "url": "https://wallstreetcn.com/articles/3781290",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T04:36:59+00:00",
    "summary": "苹果与铠侠协商3至5年NAND闪存长约，且可能不设价格上限，标志着其采购逻辑从\"压价+多源\"转向\"锁量+长约\"。这一转变源于AI数据中心客户对存储产能的激烈竞争，迫使苹果优先保障供应。存储芯片定价权正从买方向卖方转移，本轮存储周期的持续时间或超出市场传统预期。"
  },
  {
    "id": "wscn:3781046",
    "domain": "股票",
    "title": "几句话顶一千亿 美日一唱一和的“汇率操控”",
    "url": "https://wallstreetcn.com/premium/articles/3781046?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T04:24:28+00:00",
    "summary": "这条路走得漂亮，但脚下就是悬崖。"
  },
  {
    "id": "wscn:3781282",
    "domain": "股票",
    "title": "沪指半日涨0.36%，农业、传媒爆发，宁德时代AH股集体杀跌，恒科指跌超1%，科网股低迷",
    "url": "https://wallstreetcn.com/articles/3781282",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T04:09:43+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市超3400股飘红，上午半天成交1.27万亿，沪深两市半日成交额1.26万亿，较上个交易日放量120余亿。板块方面，磷化工、培育钻石、人造肉概念涨幅居前，教育、农业、房地产板块活跃；光伏逆变器、液冷服务器概念低迷，电工电网板块跌幅居前。"
  },
  {
    "id": "wscn:3781293",
    "domain": "股票",
    "title": "Arm首款集成神经加速器的Mali GPU来了，《燕云十六声》等多款游戏率先尝鲜",
    "url": "https://wallstreetcn.com/articles/3781293",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T04:07:07+00:00",
    "summary": "9月8日，Arm在上海举行的Arm Everywhere China年度大会上推出第二代移动终端计算..."
  },
  {
    "id": "wscn:3781292",
    "domain": "股票",
    "title": "宁德时代，把换电生意做上高速",
    "url": "https://wallstreetcn.com/articles/3781292",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T03:46:41+00:00",
    "summary": "借力地方资本。"
  },
  {
    "id": "wscn:3781287",
    "domain": "股票",
    "title": "美光股价收复“1000美元”，市场关注9月底财报",
    "url": "https://wallstreetcn.com/articles/3781287",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T03:31:16+00:00",
    "summary": "美光科技股价时隔三周重返千元关口，过去12个月累计涨幅近700%。韩国同业SK海力士、三星电子周一分别大涨8.3%和5.7%，存储芯片板块情绪全面回暖。市场目光已锁定9月30日财报——预计每股收益近十倍跳升至30.89美元，营收料从113亿美元跃至504亿美元，增逾三倍。"
  },
  {
    "id": "wscn:3781278",
    "domain": "股票",
    "title": "商品大佬Jeff Currie：美财政部大搞“金融压制”，市场重返“硬资产”时代，黄金1万美元并非空谈",
    "url": "https://wallstreetcn.com/articles/3781278",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T03:23:39+00:00",
    "summary": "前高盛大宗商品主管Jeff Currie指出，全球正处于硬资产超级周期的早期，随着美债利息飙升至1.5万亿美元，美财政部被迫实施“金融压制”，导致通胀侵蚀债务，若黄金外储占比重返1971年前，金价上看1万美元绝非空谈。同时，受制于长达十年的资本开支枯竭，能源“七巨头”远比科技股更具护城河。Currie警告，市场被“富足错觉”蒙蔽了真实短缺，未来企业债收益率甚至将低于主权国债，全面配置实物硬资产才的"
  },
  {
    "id": "wscn:3781285",
    "domain": "股票",
    "title": "略微上调油价预测，高盛预期“中东断航将持续到2027年”，但“价格涨幅不大”",
    "url": "https://wallstreetcn.com/articles/3781285",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T03:14:20+00:00",
    "summary": "高盛最新报告将布伦特及WTI原油价格预测各上调5美元，预计2026年12月分别达85及80美元/桶。尽管中东航运中断将延续至2027年，但因OECD商业库存韧性超预期、中东供应持续恢复，上调幅度相对克制。值得警惕的是，市场隐含的2027年3月布伦特突破100美元概率已从6%骤升至25%，价格风险明显偏向上行。"
  },
  {
    "id": "wscn:3781279",
    "domain": "股票",
    "title": "AI硬件链反弹！拥挤交易过后，TMT目前成交占比到什么位置了？",
    "url": "https://wallstreetcn.com/premium/articles/3781279?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T03:13:05+00:00",
    "summary": "电子＋通信的成交占比已由6月底最高的42%的回落至9月初的27%，与5月初的位置相当。此外，TMT与全A的滚动40日收益差作为TMT超额收益的重要择时指标，历史上该指标触及-10%是行情底部区域的一个重要提示信号。市场对于AI的交易预期在如何变化？"
  },
  {
    "id": "wscn:3781280",
    "domain": "股票",
    "title": "农产品涨价远未结束！高盛：霍尔木兹、厄尔尼诺之外，贸易壁垒才是真正风险放大器",
    "url": "https://wallstreetcn.com/articles/3781280",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T03:12:40+00:00",
    "summary": "霍尔木兹化肥断供、黑海粮食走廊受阻、超级厄尔尼诺三重风险同步发酵，BCOM农业指数年内已涨24%。更关键的是：自2020年以来全球农业贸易限制措施年度新增数量已大约翻倍，市场日益“内顾化”——贸易壁垒越高，同等冲击造成的价格波动反而越大，农产品价格上行尾部风险正在系统性加厚。"
  },
  {
    "id": "wscn:3781286",
    "domain": "股票",
    "title": "AI浪潮推高芯片价格，中国8月出口同比增长25%，进口同比增28.2%",
    "url": "https://wallstreetcn.com/articles/3781286",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-08T03:03:18+00:00",
    "summary": "在全球人工智能基础设施建设热潮带动下，高科技元器件需求大幅攀升，成为支撑中国出口的重要力量。出口已成为当前中国经济增长的主要驱动力。中国8月集成电路出口金额达407.31亿美元，1月至8月累计出口金额达2567.51亿美元，同比增长103.9%。"
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
    "id": "hn:49455629",
    "domain": "股票",
    "title": "150 Years of Global Stock Returns – The Birthplace Lottery",
    "url": "https://beyondpassive.substack.com/p/150-years-of-global-stock-returns",
    "source": "rzk",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-08-26T20:43:59+00:00",
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
    "id": "hn:49594251",
    "domain": "金融",
    "title": "Switzerland's Federal Government Is Replacing Microsoft on 3k Computers",
    "url": "https://itsfoss.com/news/switzerland-replace-microssoft-pilot/",
    "source": "ivell",
    "platform": "hackernews",
    "points": 346,
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
    "points": 164,
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
    "points": 128,
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
    "points": 127,
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
    "id": "hn:49599058",
    "domain": "金融",
    "title": "If a Tesla Cybercab fleet were profitable, Tesla wouldn't sell you one",
    "url": "https://electrek.co/2026/09/07/tesla-cybercab-fleet-profitable-wouldnt-sell/",
    "source": "jijojv",
    "platform": "hackernews",
    "points": 97,
    "published_at": "2026-09-07T14:49:43+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596610",
    "domain": "金融",
    "title": "Initial effects of AI technology on employment look positive",
    "url": "https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here",
    "source": "MrBuddyCasino",
    "platform": "hackernews",
    "points": 84,
    "published_at": "2026-09-07T10:38:32+00:00",
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
    "id": "hn:49564189",
    "domain": "金融",
    "title": "Norway's Oil Fund Proposes Selling Roughly $80B in U.S. Treasurys",
    "url": "https://www.wsj.com/finance/investing/norways-oil-fund-proposes-cut-to-government-bond-holdings-d930893f",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 46,
    "published_at": "2026-09-04T13:15:24+00:00",
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
    "id": "hn:49404624",
    "domain": "金融",
    "title": "Jane Street took $15B hit in July tied to Situational Awareness",
    "url": "https://www.reuters.com/business/finance/jane-street-took-15-billion-hit-july-tied-situational-awareness-sources-say-2026-08-14/",
    "source": "paulpauper",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-08-22T22:50:51+00:00",
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
  }
]
```
