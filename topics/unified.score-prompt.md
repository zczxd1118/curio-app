# Curio · 趋势雷达 · 跨域 Top 选稿

> 一次跑完整份简报：从所有领域的合并候选池里，选出 4-5 条跨域 Top 头条 + 备选池。
> 每条头条含"已确认 / 尚属判断对照表 + 主编点评"。

---

## 角色

你是 Curio 的**总编辑**——读者把"看全网"的工作交给你，你的责任是：

1. 从今天所有领域的合并候选池里**精选 4-5 条头条**，领域以候选条目的 `domain` 字段为准
2. 每条头条按 **已确认 / 尚属判断对照表形式**写：标题 + 引子段 + 已确认/尚属判断 + 主编点评
3. 列一份"备选池"（10-15 条标题级简单解释）

**展示分组规则（关键）**：
- 输出时按 `domain` 字段标注（用候选条目里给的中文名，例如 "AI / 科技"、"金融"、"半导体"、"大厂讯息"）
- 系统会**按 domain 拆分到每个域单独的页面/邮件**——所以读者看到的是分领域展示
- 你只需要选稿不混淆 domain，不需要在标题里加 `[领域]` 前缀（系统会自动展示域 chip）
- **【硬约束 - 不可违反】每个出现在候选池里的域，必须至少 1 条出现在 headlines 或 shortlist 里**。如某域候选有限/质量一般，宁可降星标准也要选 1 条放 shortlist —— 否则该域邮件/页面会显示"今日 0 条"，是不可接受的产品 bug。

---

## 输入（变量替换）

- 今日日期：`2026-11-25`
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
  "date": "2026-11-25",
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
- **跨域均衡**：在本期候选池实际包含的领域中，头条尽量覆盖至少 3 个域；不足 3 个域时按实际领域数处理。如果某域今天没有"够 4 星"的，可以不选入头条，但仍须遵守上方备选池的领域覆盖约束。
- **新颖度优先**：选今天/本周首发的、有数字的、有未来动作的。避免"已知信息再拼装"。
- **跨平台同事件去重**：同一个事件（如某公司 IPO）在 HN + RSS 都出现，**选英文原版/最深度的源**。
- **反偏好**：保留 0-1 条用户可能不爱看但应该看的（标 `is_diverse: true`，可选）。
- **历史反馈优先**：如果用户最近一次反馈说"想多看 X"，至少 1 条头条契合。

### 备选池（10-15 条）
- 不上头条但仍值得知晓的。
- 每条 30-60 字一句话。
- 按候选条目的 `domain` 自然分组，不预设固定领域列表。

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
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 2291820,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1517724,
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
    "points": 1495361,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV14rzQB9EJj",
    "domain": "AI",
    "title": "Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill / Hook / 图片 / 上下文处理/ 后台任务",
    "url": "http://www.bilibili.com/video/av115954889596221",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1349284,
    "published_at": "2026-01-25T08:55:20+00:00",
    "summary": "时间戳如下，方便大家跳转观看：\n \n第一部分：环境搭建与基础交互\n- 01:09 安装 Claude Code\n- 01:43 登录与授权\n- 02:55 第一个实战问题\n- 03:12 三种模式详解 (默认/自动/规划)\n \n第二部分：复杂任务处理与终端控制\n- 06:00 执行终端命令 (Bash)\n- 06:49 使用规划模式 (Plan Mode)\n- 11:06 跳过所有权限检测 (da"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 917333,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 764010,
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
    "points": 597758,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 490491,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1h3W76wEem",
    "domain": "AI",
    "title": "Claude(Code)桌面APP，保姆级全攻略，一期视频精通，顶级Agent软件长什么样？",
    "url": "http://www.bilibili.com/video/av117580048108571",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 454643,
    "published_at": "2026-11-08T09:14:07+00:00",
    "summary": "最近Claude桌面端（Claude Desktop） 有了一大波功能更新。随着一步步的迭代，它已经把 Claude Code 的编程、Claude Design 的设计，以及 Claude Cowork 的办公等核心能力，全部收入了同一个桌面客户端，特别是Claude Code已经从原本黑乎乎的命令行工具，进化成了桌面客户端的完全体形态。再搭配上超强的Opus5.5 模型，已经能称得上是地表顶级"
  },
  {
    "id": "bvid:BV13YRjBTEPb",
    "domain": "AI",
    "title": "Hermes Agent零基础、保姆级教程，小白也能轻松玩转",
    "url": "http://www.bilibili.com/video/av116503638706867",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 438566,
    "published_at": "2026-05-02T06:51:59+00:00",
    "summary": "全B站最详细的Hermes Agent教程，从部署到玩转！零基础，小白也能轻松玩转Hermes Agent，真正的AI助手，恐怖如斯！"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 435579,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1AnQNYxEsy",
    "domain": "AI",
    "title": "MCP是啥？技术原理是什么？一个视频搞懂MCP的一切。Windows系统配置MCP，Cursor Cline使用MCP",
    "url": "http://www.bilibili.com/video/av114155298228756",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 429053,
    "published_at": "2025-03-13T13:18:09+00:00",
    "summary": "MCP是近期的AI领域的热点，特别是在海外社区获得热烈讨论，每天都有大量MCP工具诞生。本期视频我们从MCP的概念，技术原理，到多场景实战，一个视频看懂MCP的全部内容。\n\n\nMCP官方开源仓库：https://github.com/modelcontextprotocol/servers\nMCP合集网站：  https://smithery.ai/\nVscode下载：https://code.v"
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 369497,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 359127,
    "published_at": "2025-07-30T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从概念到安装，再到Claude Code的具体使用，开发效率原地起飞！"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 333648,
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
    "points": 305767,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1RdLm6PEFF",
    "domain": "AI",
    "title": "ClaudeCode桌面版 = 中文汉化 + 免登录 + 接入DeekSeek + 安装自己的Skill",
    "url": "http://www.bilibili.com/video/av116606717919919",
    "source": "iwenwiki",
    "platform": "bilibili",
    "points": 293110,
    "published_at": "2026-05-20T11:45:46+00:00",
    "summary": "全B站最详细的 ClaudeCode 桌面版教程，从安装到免登录，中文汉化，接入DeepSeek，安装使用自己的Skill，ClaudeCode真正的AI编程工具，恐怖如斯！\nAgent Skills课程在这里：https://www.bilibili.com/video/BV1ugdgBQED4/?spm_id_from=333.1387.homepage.video_card.click&am"
  },
  {
    "id": "bvid:BV1qJs16WEJj",
    "domain": "AI",
    "title": "今天体验的人生副本是:沉迷vibe coding走火入魔的AI嘉豪",
    "url": "http://www.bilibili.com/video/av117635899524333",
    "source": "vibe睦头人",
    "platform": "bilibili",
    "points": 263349,
    "published_at": "2026-11-18T06:01:48+00:00",
    "summary": "ai生成，仅供娱乐，如有雷同，纯属巧合（（"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 241101,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1TTR8BaEnL",
    "domain": "AI",
    "title": "Claude Code 零基础终极教程：安装、换模型、插件、Hooks、Skills、Subagents、实战项目一次讲透！",
    "url": "http://www.bilibili.com/video/av116529475622752",
    "source": "木子不写代码",
    "platform": "bilibili",
    "points": 217758,
    "published_at": "2026-05-07T08:00:00+00:00",
    "summary": "这是你能看到的最完整的 Claude Code 零基础系统教程。\n\n\n我们将深度拆解：\n\n1️⃣ 基础入门：安装、第三方模型接入、权限系统。\n\n2️⃣ 核心进阶：Tools、Hooks、Skills、Subagents 及自动化流程。\n\n3️⃣ 项目实战：从零构建一个真实可用的 AI 网页 App。\n\n\n视频跟到最后，你不只是学会写代码，而是掌握 AI 智能体的工作逻辑。我是木子，只提供 AI 时"
  },
  {
    "id": "bvid:BV15XDfBSE2t",
    "domain": "AI",
    "title": "ClaudeCode平替:OpenCode详细使用教程看这一个就够了（内含超详细安装文档+软件安装包）",
    "url": "http://www.bilibili.com/video/av116379604881806",
    "source": "鹏哥C语言",
    "platform": "bilibili",
    "points": 213714,
    "published_at": "2026-04-13T09:00:00+00:00",
    "summary": "opencodeopencode使用全攻略opencode教程opencode和claudecodeopencode使用技巧opencode实战opencode coworkopencode安装opencode开发opencode使用教程opencode教程opencode安装教程opencode使用全攻略opencode和claudecodeopencode skillsopencode插件op"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 187783,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 166770,
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
    "points": 164691,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1b5AeeGEFc",
    "domain": "AI",
    "title": "Cursor太贵？分享三个免费AI编程方案+海量编程技巧【如何看待AI编程】",
    "url": "http://www.bilibili.com/video/av114025056699722",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 162310,
    "published_at": "2025-02-18T13:13:51+00:00",
    "summary": "我试用了几十种AI编程辅助工具，找到了其中三个免费，并且效果最好的方案。 本期视频就来跟大家分享一下。视频中间会穿插很多AI编程工具的使用技巧，还有看待AI编程的一些个人思考。本期视频没有广告都是个人的经验干货，废话不多说我们直接开始。"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 159597,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1eYPpeWEnT",
    "domain": "AI",
    "title": "Cursor + MCP = 王炸！彻底颠覆我的Cursor工作流，效率直接起飞",
    "url": "http://www.bilibili.com/video/av114073660301264",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 151945,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV14rxM6qEnL",
    "domain": "AI",
    "title": "最新Skills开发教程，Agent skill实战|WorkBuddy+Codex+DeepSeek Harness",
    "url": "http://www.bilibili.com/video/av117511429295044",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 147696,
    "published_at": "2026-10-28T02:00:00+00:00",
    "summary": "【课程简介】Agent Skills零基础教程，从WorkBuddy、Codex上手到项目落地实战。"
  },
  {
    "id": "bvid:BV1Qcg6zgEhU",
    "domain": "AI",
    "title": "【AI Agent实战】从零开始教你搭建Agent智能体，小白也能学会的保姆级教程！让你少走99%弯路！",
    "url": "http://www.bilibili.com/video/av114771105945944",
    "source": "讲AI的小坛",
    "platform": "bilibili",
    "points": 128826,
    "published_at": "2025-06-30T07:26:07+00:00",
    "summary": "【AI Agent实战】从零开始的智能体搭建，小白也能学会的保姆级教程！让你少走99%弯路，最简单易懂的大模型教程"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 122454,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 103524,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1K6YM69ESq",
    "domain": "AI",
    "title": "AI+网络安全实战：从Agent入门到AI智能体挖漏洞教程！网络安全|信息安全|黑客技术|渗透测试|SRC漏洞挖掘|AI审计|HVV护网行动|靶场练习-码士集团",
    "url": "http://www.bilibili.com/video/av117247037213495",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 100865,
    "published_at": "2026-09-10T13:47:24+00:00",
    "summary": "这套课程围绕「AI+网络安全」展开，从AI智能体基础入门，到WorkBuddy、Trae等主流Agent工具的实际应用，再到API-Key接入、Skill使用等核心能力，逐步进入AI漏洞挖掘、代码审计、CTF题目分析等安全实战场景。同时结合SRC漏洞挖掘、HVV护网、安全竞赛以及网络安全就业方向，帮助你系统了解AI在网络安全学习、开发与实战中的应用方式。适合网络安全初学者、安全从业者以及希望利用A"
  },
  {
    "id": "bvid:BV1VQWb6eEeo",
    "domain": "AI",
    "title": "全网最详细的 AI 入门课：一期视频搞懂 58 个 AI 术语，从大模型到 Agent、MCP、Skill",
    "url": "http://www.bilibili.com/video/av117587144940374",
    "source": "亚里今天也要AI",
    "platform": "bilibili",
    "points": 98371,
    "published_at": "2026-11-09T15:20:10+00:00",
    "summary": "这可能是你看过的，最详细的 AI 入门课。\n一期视频，带你搞懂 AI 里最常见的 58 个概念和名词：从最基础的大模型、Token，到现在最火的 Agent、MCP、Skill，每一个都讲清楚它是什么、怎么工作，和其他概念有什么区别。\n五个部分循序渐进，最后用学到的词，一句一句读懂一页真的模型更新日志。\n\n00:00 开场\n00:27 课程路线：五个部分\n【第一部分 AI 和大模型是什么】\n00:"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 94392,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1YJ336EEBk",
    "domain": "AI",
    "title": "【AI陪玩】开袋即食的AI接入我的世界教程！",
    "url": "http://www.bilibili.com/video/av116981806143216",
    "source": "万圣Dwin",
    "platform": "bilibili",
    "points": 92520,
    "published_at": "2026-07-26T01:30:00+00:00",
    "summary": "模组：Numen\n项目地址：https://github.com/Dwinovo/minecraft-numen"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 78401,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1cVW86JE2e",
    "domain": "AI",
    "title": "Vibe Coding 完不会获客？我用 AI 做了一个「营销数据库」！【B站AI创造公开赛】",
    "url": "http://www.bilibili.com/video/av117587245599812",
    "source": "熠辉IndieDev",
    "platform": "bilibili",
    "points": 77163,
    "published_at": "2026-11-10T01:00:00+00:00",
    "summary": "产品做出来了，第一批用户去哪找？我用两个月做了 BizPeel，收录700多个公开营收的产品，拆解真实获客动作。本期演示在 Google Antigravity 接入 BizPeel MCP，由 Gemini 4 Argon 查找同类产品、整理增长实验；报告生成时用 Gemini Flash 清洗数据，再由 Gemini 4 Argon 撰写。\n\n注： 部分Google技术仅适用于出海场景。"
  },
  {
    "id": "bvid:BV17Lap6VEUr",
    "domain": "AI",
    "title": "【全80集】Vibe Coding 零基础入门到实战教程，由浅入深（全程干货）",
    "url": "http://www.bilibili.com/video/av117353572468721",
    "source": "数据拾光屋",
    "platform": "bilibili",
    "points": 68541,
    "published_at": "2026-10-02T09:25:00+00:00",
    "summary": "本套教程专门为零基础学员而制，全程干货无废话，喜欢的小伙伴记得点赞三连喔 ~"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 57173,
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
    "points": 50798,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1wpxq6VEXx",
    "domain": "AI",
    "title": "【AI时代的STM32教程】AI Agent 初体验",
    "url": "http://www.bilibili.com/video/av117529699682124",
    "source": "keysking",
    "platform": "bilibili",
    "points": 48114,
    "published_at": "2026-10-30T11:52:06+00:00",
    "summary": "一句话，让 AI 帮我们完成第一个 STM32C5 程序！🚀\n本期我们一起认识 AI Agent，学习如何描述开发需求，并借助开源的 STM32C5DevSkills，让 AI 完成工程创建、芯片配置、代码编写和编译烧录，让律动小板上的小灯闪烁起来！\n也特别感谢 @意法半导体中国   对本系列教程的支持～下期我们再亲手走一遍开发流程，把 Agent 替我们完成的工作，一步步搞明白！"
  },
  {
    "id": "bvid:BV1thQPYfEYC",
    "domain": "AI",
    "title": "全流程演示Cursor + Blender MCP实现自动3D建模",
    "url": "http://www.bilibili.com/video/av114155835103525",
    "source": "Next蔡蔡",
    "platform": "bilibili",
    "points": 44823,
    "published_at": "2025-03-13T15:31:17+00:00",
    "summary": "自动3D建模这个例子，是不是让大家一下子就看懂MCP的用途了。\n.\n后面会实测更多Cursor+MCP的更多玩法，欢迎继续围观\n.\n欢迎加入我的知识星球，有问必答：https://t.zsxq.com/fD4Fb\n.\nblender mcp项目：https://github.com/ahujasid/blender-mcp/tree/main"
  },
  {
    "id": "bvid:BV1NddKBvEsY",
    "domain": "AI",
    "title": "claude code 桌面端安装并且配置第三方api使用教程，想体验的尽早吧，因为这公司可能不知道哪天抽风就会禁用了！#claude #ai #人工智能",
    "url": "http://www.bilibili.com/video/av116535968466799",
    "source": "菜鸡的老黎",
    "platform": "bilibili",
    "points": 42731,
    "published_at": "2026-05-07T23:56:28+00:00",
    "summary": "claude code 桌面端安装并且配置第三方api使用教程，想体验的尽早吧，因为这公司可能不知道哪天抽风就会禁用了！#claude #ai #人工智能 #agent"
  },
  {
    "id": "bvid:BV1BygA6KEAi",
    "domain": "AI",
    "title": "DeepSeek Harness + ComfyUI：Agent开始自己跑AI工作流了！",
    "url": "http://www.bilibili.com/video/av117093508910174",
    "source": "啦啦啦的小黄瓜",
    "platform": "bilibili",
    "points": 41891,
    "published_at": "2026-08-14T11:01:16+00:00",
    "summary": "小助理联系方式：zhuli240614\nComfyUI节点详解网址：uinodes.com，网站使用教程：\n[ComfyUI]全网最详细节点测试以及参数详解，近千节点持续更新，纯干货教程总结梳理。\n\nMiniMax Music3模型以及工作流：https://pan.quark.cn/s/f19f1109a481\n所有模型以及工作流分享：https://pan.quark.cn/s/ef8c640"
  },
  {
    "id": "bvid:BV1SwyXzoEms",
    "domain": "AI",
    "title": "狂烧上万元，我用 AI 做了 500 多个网站！",
    "url": "http://www.bilibili.com/video/av117666283002439",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 40250,
    "published_at": "2026-11-23T14:51:52+00:00",
    "summary": "我的第二个出海产品 VibeFather 来了，几百个现成的网站模板，让你快速通过 AI 编程工具做出同款网站，提供完整提示词和设计规范文档，让 Vibe Coding 又快又省 tokens。\n模板大全：vibefather.ai\n开源指路：github.com/liyupi/awesome-vibe-coding-websites\n编程学习教程+实战项目+简历模板：codefather.cn\n"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 35107,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34748,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1uwxG6DEra",
    "domain": "AI",
    "title": "3分钟讲透：Vibe Coding如何避免💩屎山代码",
    "url": "http://www.bilibili.com/video/av117513727838880",
    "source": "鲤哥builder",
    "platform": "bilibili",
    "points": 33732,
    "published_at": "2026-10-27T16:09:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 31344,
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
    "points": 30011,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "hn:50611576",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Reinstates Jensen Huang as CEO",
    "url": "https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html",
    "source": "jaz",
    "platform": "hackernews",
    "points": 2819,
    "published_at": "2026-11-23T14:00:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:50611588",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang Reinstated as Nvidia CEO",
    "url": "https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director",
    "source": "alanwong",
    "platform": "hackernews",
    "points": 1713,
    "published_at": "2026-11-23T14:01:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50459703",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is preparing to oust Jensen Huang",
    "url": "https://www.wsj.com/business/nvidia-is-preparing-to-oust-nvidia-ceo-jensen-huang-30f421ad",
    "source": "jbredeche",
    "platform": "hackernews",
    "points": 1227,
    "published_at": "2026-11-11T22:31:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50493251",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia allegedly engineered scarcity by funding AI startups to buy its GPUs",
    "url": "https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus",
    "source": "speckx",
    "platform": "hackernews",
    "points": 1117,
    "published_at": "2026-11-14T02:52:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:50477231",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia employees petition to bring back Jensen Huang",
    "url": "https://www.wired.com/story/nvidia-employees-petition-for-jensen-huangs-return/",
    "source": "lavendermon",
    "platform": "hackernews",
    "points": 820,
    "published_at": "2026-11-13T02:16:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:50534631",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia stopped disclosing Singapore sales as revenues hit $104B",
    "url": "https://www.ft.com/content/dbde7a30-548c-4f9d-a4be-7898a0c24dcf",
    "source": "louiereederson",
    "platform": "hackernews",
    "points": 671,
    "published_at": "2026-11-17T17:12:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50512235",
    "domain": "AI 算力 / 半导体",
    "title": "What's Next for Nvidia?",
    "url": "https://steveblank.com/2026/11/15/whats-next-for-nvidia/",
    "source": "zdw",
    "platform": "hackernews",
    "points": 486,
    "published_at": "2026-11-15T23:55:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50473190",
    "domain": "AI 算力 / 半导体",
    "title": "Former Nvidia CEO Huang had a relationship with a second employee, sources say",
    "url": "https://www.reuters.com/technology/former-nvidia-ceo-huang-had-relationship-with-second-employee-sources-say-2026-11-12/",
    "source": "jbredeche",
    "platform": "hackernews",
    "points": 460,
    "published_at": "2026-11-12T19:51:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:50501631",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia deliberately kept GPU prices high through circular financing deals",
    "url": "https://www.techspot.com/news/114558-nvidia-deliberately-kept-gpu-prices-high-through-circular.html",
    "source": "madihaa",
    "platform": "hackernews",
    "points": 453,
    "published_at": "2026-11-14T22:26:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:50487864",
    "domain": "AI 算力 / 半导体",
    "title": "$11.4M in Nvidia hardware vanishes during shipment from CA to TX",
    "url": "https://www.freightwaves.com/news/11-4-million-in-nvidia-hardware-vanishes-during-shipment-from-california-to-texas",
    "source": "crescit_eundo",
    "platform": "hackernews",
    "points": 387,
    "published_at": "2026-11-13T18:40:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:50467132",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang resigns as Nvidia CEO immediately",
    "url": "https://www.reuters.com/live/nvidia-live-board-meets-fate-ceo-jensen-huang-after-affair-reports-2026-11-12/",
    "source": "ksec",
    "platform": "hackernews",
    "points": 375,
    "published_at": "2026-11-12T13:56:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:50626861",
    "domain": "AI 算力 / 半导体",
    "title": "Who in Washington owns and trades Nvidia stock",
    "url": "https://www.kadoa.com/congress/insights/trump-nvidia",
    "source": "hubraumhugo",
    "platform": "hackernews",
    "points": 286,
    "published_at": "2026-11-24T11:51:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50581438",
    "domain": "AI 算力 / 半导体",
    "title": "US SEC's Nvidia probe is examining potential accounting issues – sources",
    "url": "https://www.marketscreener.com/news/us-sec-s-nvidia-probe-is-examining-potential-accounting-issues-sources-say-ce785ed3dd8ff627",
    "source": "ftchd",
    "platform": "hackernews",
    "points": 309,
    "published_at": "2026-11-20T20:22:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:50518567",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia was in trouble before the Jensen Huang mess",
    "url": "https://www.wired.com/story/nvidia-was-already-in-trouble-before-the-jensen-huang-mess/",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 291,
    "published_at": "2026-11-16T15:24:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:50638503",
    "domain": "AI 算力 / 半导体",
    "title": "Show HN: Old Nvidia and ATI tech demos, running again in the browser",
    "url": "https://gpu-demo-gallery.pages.dev/",
    "source": "arkits",
    "platform": "hackernews",
    "points": 174,
    "published_at": "2026-11-25T04:31:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50459776",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia prepares to fire CEO Jensen Huang, WSJ reports",
    "url": "https://twitter.com/watcherguru/status/2120645607866188008",
    "source": "alexmolas",
    "platform": "hackernews",
    "points": 225,
    "published_at": "2026-11-11T22:36:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50492993",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia director sold nearly $1B in stock weeks before the Jensen Huang scandal",
    "url": "https://finance.yahoo.com/markets/stocks/articles/nvidia-director-sold-nearly-1b-160000846.html",
    "source": "LopRabbit",
    "platform": "hackernews",
    "points": 218,
    "published_at": "2026-11-14T02:21:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:50630245",
    "domain": "AI 算力 / 半导体",
    "title": "Ex-Nvidia partner Megaspeed hit with U.S. Commerce Department export ban",
    "url": "https://www.upi.com/Top_News/US/2026/11/24/NVIDIA-partner-Megaspeed/1701795520063/",
    "source": "nephihaha",
    "platform": "hackernews",
    "points": 123,
    "published_at": "2026-11-24T16:08:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50511982",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang might return to Nvidia as CEO",
    "url": "https://www.reuters.com/world/china/jensen-huang-discusses-comeback-nvidia-ceo-with-allies-ft-reports-2026-11-15/",
    "source": "YakubYilmaz",
    "platform": "hackernews",
    "points": 178,
    "published_at": "2026-11-15T23:24:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50327058",
    "domain": "AI 算力 / 半导体",
    "title": "Seoul Viosys begins production of rare-earth-free white light emitter",
    "url": "https://www.semiconductor-today.com/news_items/2026/oct/seoul-291026.shtml",
    "source": "gmays",
    "platform": "hackernews",
    "points": 195,
    "published_at": "2026-11-01T16:23:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50467139",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO Jensen Huang resigns after reports of second affair deepened scandal",
    "url": "https://www.bbc.co.uk/news/live/c6zjry11v8w1t",
    "source": "cognoboffin",
    "platform": "hackernews",
    "points": 169,
    "published_at": "2026-11-12T13:56:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50497155",
    "domain": "AI 算力 / 半导体",
    "title": "Serving GLM-5.3 at 607.8 tok/s across two Nvidia DGX stations with vLLM",
    "url": "https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/",
    "source": "wondersky",
    "platform": "hackernews",
    "points": 150,
    "published_at": "2026-11-14T14:09:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50618490",
    "domain": "AI 算力 / 半导体",
    "title": "Congress shreds Nvidia's 'outrageous' return of Huang: 'Failure of character'",
    "url": "https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-congress-trump.html",
    "source": "MilnerRoute",
    "platform": "hackernews",
    "points": 69,
    "published_at": "2026-11-23T20:13:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:50509883",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang discusses comeback as Nvidia CEO with allies",
    "url": "https://www.ft.com/content/45383d86-33c4-4d99-86e5-5e058d3567c1",
    "source": "eyalitki",
    "platform": "hackernews",
    "points": 136,
    "published_at": "2026-11-15T19:31:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:50629620",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia board's Huang reversal raises doubts about independence, critics say",
    "url": "https://www.reuters.com/legal/transactional/nvidia-boards-huang-reversal-raises-doubts-about-independence-critics-say-2026-11-24/",
    "source": "onemoresoop",
    "platform": "hackernews",
    "points": 41,
    "published_at": "2026-11-24T15:28:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50479721",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Hacked",
    "url": "https://www.sec.gov/Archives/edgar/data/1046179/000104617926000800/a20261112statementregardin.htm",
    "source": "gmays",
    "platform": "hackernews",
    "points": 115,
    "published_at": "2026-11-13T07:39:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50621127",
    "domain": "AI 算力 / 半导体",
    "title": "Short Nvidia Fund Halted After 91% Wipeout",
    "url": "https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-23-2026/card/short-nvidia-fund-halted-after-91-wipeout-myoKEHNFkGcseucDUC48",
    "source": "devy",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-11-23T23:36:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50616243",
    "domain": "AI 算力 / 半导体",
    "title": "Trump Is Said to Have Directed Effort to Reinstate Nvidia Chief",
    "url": "https://www.nytimes.com/2026/11/23/us/politics/trump-nvidia-huang.html",
    "source": "johnny313",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-11-23T18:03:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:50483391",
    "domain": "AI 算力 / 半导体",
    "title": "The Downfall of Jensen Huang: Nvidia's Greed and Corruption [video]",
    "url": "https://www.youtube.com/watch?v=YYU_geUwQoA",
    "source": "belst",
    "platform": "hackernews",
    "points": 81,
    "published_at": "2026-11-13T13:45:06+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/winbond-widens-edge-ai-reach-certifies-nor-flash/",
    "domain": "AI 算力 / 半导体",
    "title": "Winbond Widens Edge AI Reach, Certifies NOR Flash",
    "url": "https://www.eetimes.com/winbond-widens-edge-ai-reach-certifies-nor-flash/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T08:59:51+00:00",
    "summary": "Winbond is pairing bandwidth and density to meet the edge’s demand for faster, safer memory without the custom-design price tag. The post Winbond Widens Edge AI Reach, Certifies NOR Flash appeared fir"
  },
  {
    "id": "rss:https://www.eetimes.com/southchip-showcases-automotive-power-charging-and-load-control-solutions-at-electronica-munich/",
    "domain": "AI 算力 / 半导体",
    "title": "Southchip Showcases Automotive Power, Charging, and Load-Control Solutions at electronica Munich",
    "url": "https://www.eetimes.com/southchip-showcases-automotive-power-charging-and-load-control-solutions-at-electronica-munich/",
    "source": "Christopher McGrady",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T08:32:46+00:00",
    "summary": "Southchip presented its automotive PMICs, 240W USB charging, wireless charging, ambient lighting, and high-side drivers at electronica Munich. The post Southchip Showcases Automotive Power, Charging, "
  },
  {
    "id": "rss:https://www.eetimes.com/from-ai-platforms-to-industry-innovation-how-nvidia-connects-startups-to-build-an-ai-ecosystem/",
    "domain": "AI 算力 / 半导体",
    "title": "From AI Platforms to Industry Innovation: How NVIDIA Connects Startups to Build an AI Ecosystem",
    "url": "https://www.eetimes.com/from-ai-platforms-to-industry-innovation-how-nvidia-connects-startups-to-build-an-ai-ecosystem/",
    "source": "EE Times Taiwan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T05:00:00+00:00",
    "summary": "For AI startups, the real challenge is often not building AI itself, but getting it to work reliably in the real world. The post From AI Platforms to Industry Innovation: How NVIDIA Connects Startups "
  },
  {
    "id": "rss:https://www.eetimes.com/from-precision-to-autonomous-agriculture-the-role-of-edge-ai-and-robotics/",
    "domain": "AI 算力 / 半导体",
    "title": "From Precision to Autonomous Agriculture: The Role of Edge AI and Robotics",
    "url": "https://www.eetimes.com/from-precision-to-autonomous-agriculture-the-role-of-edge-ai-and-robotics/",
    "source": "Shihao Fu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T16:16:56+00:00",
    "summary": "Edge AI and robotics bring greater precision and autonomy to agricultural machinery, from targeted spraying to harvesting. The post From Precision to Autonomous Agriculture: The Role of Edge AI and Ro"
  },
  {
    "id": "rss:https://www.eetimes.com/vehicle-to-grid-great-idea-or-unrealistic-dream-part-2/",
    "domain": "AI 算力 / 半导体",
    "title": "Vehicle-to-Grid: Great Idea or Unrealistic Dream? (Part 2)",
    "url": "https://www.eetimes.com/vehicle-to-grid-great-idea-or-unrealistic-dream-part-2/",
    "source": "Bill Schweber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T11:53:11+00:00",
    "summary": "Vehicle-to-grid technology promises grid benefits but raises concerns over battery life, charging access, costs, and driver convenience. The post Vehicle-to-Grid: Great Idea or Unrealistic Dream? (Par"
  },
  {
    "id": "rss:https://www.eetimes.com/vehicle-to-grid-great-idea-or-unrealistic-dream/",
    "domain": "AI 算力 / 半导体",
    "title": "Vehicle-to-Grid: Great Idea or Unrealistic Dream?",
    "url": "https://www.eetimes.com/vehicle-to-grid-great-idea-or-unrealistic-dream/",
    "source": "Bill Schweber",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T08:40:49+00:00",
    "summary": "Vehicle-to-grid sounds like a partial solution for enhancing the grid, but the reality of the human factor may say otherwise. The post Vehicle-to-Grid: Great Idea or Unrealistic Dream? appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/nsing-featured-cra-ai-robotics-motor-control-and-digital-energy-at-electronica-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "NSING Featured CRA, AI Robotics, Motor Control and Digital Energy at electronica 2026",
    "url": "https://www.eetimes.com/nsing-featured-cra-ai-robotics-motor-control-and-digital-energy-at-electronica-2026/",
    "source": "NSING Technologies Pte. Ltd.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T07:41:37+00:00",
    "summary": "At electronica 2026 in Munich, NSING exhibited 35 solutions built on N32‑series MCUs, N32WB BLE SoCs and NS350 TPM, covering AI robotics, motor control and digital energy, and presented its CRA compli"
  },
  {
    "id": "rss:https://www.eetimes.com/nvidia-board-reinstates-jensen-huang-as-ceo/",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Board Reinstates Jensen Huang as CEO",
    "url": "https://www.eetimes.com/nvidia-board-reinstates-jensen-huang-as-ceo/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T18:17:02+00:00",
    "summary": "Nvidia goes back to business as usual following Huang's resignation and reinstatement after a week. The post Nvidia Board Reinstates Jensen Huang as CEO appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/the-sovereign-ai-paradox-who-controls-the-compute/",
    "domain": "AI 算力 / 半导体",
    "title": "The Sovereign AI Paradox: Who Controls the Compute?",
    "url": "https://www.eetimes.com/the-sovereign-ai-paradox-who-controls-the-compute/",
    "source": "Ron Honig",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T16:08:35+00:00",
    "summary": "U.S. restrictions on overseas AI infrastructure could accelerate sovereign computing and weaken American technology dominance. The post The Sovereign AI Paradox: Who Controls the Compute? appeared fir"
  },
  {
    "id": "rss:https://www.eetimes.com/secure-flash-a-practical-path-to-cyber-resilience-act-compliance/",
    "domain": "AI 算力 / 半导体",
    "title": "Secure Flash: A Practical Path to Cyber Resilience Act Compliance",
    "url": "https://www.eetimes.com/secure-flash-a-practical-path-to-cyber-resilience-act-compliance/",
    "source": "Winbond Electronics Corporation",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T15:00:00+00:00",
    "summary": "The EU Cyber Resilience Act (CRA) introduces cybersecurity requirements for connected products throughout their lifecycle. This white paper explores how Winbond’s TrustME® W77Q Secure Flash and CRA Co"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/google-deepmind-ai-engineers-conjure-mathematical-proof-of-signals-encryption-protocol-alphaproof-code-framework-powered-human-bot-cooperation-for-speedy-work",
    "domain": "AI 算力 / 半导体",
    "title": "Google DeepMind AI engineers conjure mathematical proof of Signal's encryption protocol — AlphaProof Code framework powered human-bot cooperation for speedy work",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/google-deepmind-ai-engineers-conjure-mathematical-proof-of-signals-encryption-protocol-alphaproof-code-framework-powered-human-bot-cooperation-for-speedy-work",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T12:00:00+00:00",
    "summary": "Google DeepMind AI engineers conjure mathematical proof of Signal's encryption protocol — AlphaProof Code framework powered human-bot cooperation for speedy work"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/radeon-rx-9060-xt-sets-new-gpu-frequency-world-record-of-4-837-ghz-amd-overclocking-team-pushes-mid-range-rdna-4-gpu-to-the-max-under-liquid-nitrogen",
    "domain": "AI 算力 / 半导体",
    "title": "AMD's Radeon RX 9060 XT sets new GPU frequency world record of 4.837 GHz",
    "url": "https://www.tomshardware.com/pc-components/gpus/radeon-rx-9060-xt-sets-new-gpu-frequency-world-record-of-4-837-ghz-amd-overclocking-team-pushes-mid-range-rdna-4-gpu-to-the-max-under-liquid-nitrogen",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T11:30:00+00:00",
    "summary": "AMD's Radeon RX 9060 XT has reached a new GPU frequency world record of 4,837 MHz. AMD VP Jack Huynh and veteran overclocker Bill Alverson used liquid nitrogen cooling to help the smaller RDNA 4 GPU o"
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/this-acer-nitro-v-laptop-with-nvidia-rtx-5060-gpu-is-usd1-049-at-best-buy-16-inch-boasts-16gb-ddr5-ram-and-a-512gb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "This Acer Nitro V laptop with Nvidia RTX 5060 GPU is $1,049 at Best Buy",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/this-acer-nitro-v-laptop-with-nvidia-rtx-5060-gpu-is-usd1-049-at-best-buy-16-inch-boasts-16gb-ddr5-ram-and-a-512gb-ssd",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T11:22:34+00:00",
    "summary": "This 15.6-inch Acer Nitro gaming laptop features an RTX 5060 GPU, a 10-core Intel CPU, and a 512GB SSD for $1,049"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/playstation/ps5-modder-rips-out-logic-board-to-turn-his-console-into-liquid-cooled-phanteks-pc-custom-playstation-5-pro-build-took-120-hours-has-its-own-psu-aio-and-3d-printed-parts",
    "domain": "AI 算力 / 半导体",
    "title": "PS5 modder rips out logic board, turns his console into liquid-cooled Phanteks PC",
    "url": "https://www.tomshardware.com/video-games/playstation/ps5-modder-rips-out-logic-board-to-turn-his-console-into-liquid-cooled-phanteks-pc-custom-playstation-5-pro-build-took-120-hours-has-its-own-psu-aio-and-3d-printed-parts",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T11:00:00+00:00",
    "summary": "An intrepid YouTube tech enthusiast was dissatisfied with his PlayStation 5 Pro's cooling, so he ripped out the logic board and built an entire custom PC around it, complete with 3D-printed parts and "
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/save-usd1-200-on-an-rtx-5090-gaming-pc-with-a-9950x3d-right-now-liquid-cooled-ibuypower-rig-ships-with-32gb-ddr5-and-a-huge-4tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Save $1,200 on an RTX 5090 gaming PC with a 9950X3D right now",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/save-usd1-200-on-an-rtx-5090-gaming-pc-with-a-9950x3d-right-now-liquid-cooled-ibuypower-rig-ships-with-32gb-ddr5-and-a-huge-4tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T10:48:49+00:00",
    "summary": "Few rigs can rival the performance of this iBuyPower RDY Y50 R04 gaming PC. It's on sale with a huge $1200 discount right now, shipping with an RTX 5090, AMD Ryzen 9 9950X3D, 32GB of RAM, and a 4TB SS"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/jensen-huang-denies-special-government-treatment-at-first-nvidia-all-hands-since-return-there-are-rumors-on-the-internet-that-apparently-im-a-tech-bro-and-therefore-im-back",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang denies special government treatment at first Nvidia all-hands since return",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/jensen-huang-denies-special-government-treatment-at-first-nvidia-all-hands-since-return-there-are-rumors-on-the-internet-that-apparently-im-a-tech-bro-and-therefore-im-back",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T10:30:00+00:00",
    "summary": "Jensen Huang says he didn't get special treatment from the government at first Nvidia all-hands meeting since his return — \"there are rumors on the internet that apparently I’m a tech bro, and therefo"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/new-cpu-benchmark-tool-promises-40-years-of-compatibility-with-support-as-far-back-as-i386-windows-95-crystalmark-cpuix-tested-on-nec-pc-98-21bs-pentium-100-and-more",
    "domain": "AI 算力 / 半导体",
    "title": "New CPU benchmark tool promises 40 years of compatibility, with support as far back as i386, Windows 95",
    "url": "https://www.tomshardware.com/pc-components/cpus/new-cpu-benchmark-tool-promises-40-years-of-compatibility-with-support-as-far-back-as-i386-windows-95-crystalmark-cpuix-tested-on-nec-pc-98-21bs-pentium-100-and-more",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T10:00:00+00:00",
    "summary": "There's a new CPU benchmark on the way designed to span 40 years of personal computer chipmaking from the i386 to the present day."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/portable-monitors/these-four-portable-monitors-are-on-sale-for-black-friday-get-a-second-screen-for-your-pc-or-console-for-less",
    "domain": "AI 算力 / 半导体",
    "title": "These four portable monitors are on sale for Black Friday",
    "url": "https://www.tomshardware.com/monitors/portable-monitors/these-four-portable-monitors-are-on-sale-for-black-friday-get-a-second-screen-for-your-pc-or-console-for-less",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T10:00:00+00:00",
    "summary": "These four portable monitors are available at low prices for Black Friday. Get a second screen for your PC or console, starting under $55"
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/black-friday-2026-monitors",
    "domain": "AI 算力 / 半导体",
    "title": "Black Friday 2026 gaming monitor deals live",
    "url": "https://www.tomshardware.com/live/news/black-friday-2026-monitors",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T09:21:02+00:00",
    "summary": "The best Black Friday monitor sales, live round-the-clock coverage of all the best deals."
  },
  {
    "id": "rss:https://www.tomshardware.com/live/news/black-friday-2026",
    "domain": "AI 算力 / 半导体",
    "title": "Best Black Friday 2026 tech deals",
    "url": "https://www.tomshardware.com/live/news/black-friday-2026",
    "source": "The Editors of Tom&#039;s Hardware",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T07:12:35+00:00",
    "summary": "All the best Black Friday deals for tech and PC hardware."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/us-doj-touts-largest-ever-crackdown-on-scammers-across-the-globe-as-it-seizes-14-000-devices-and-usd17-billion-in-illicit-funds-operation-results-in-800-defendants-and-frees-2-200-forced-laborers",
    "domain": "AI 算力 / 半导体",
    "title": "US DOJ touts \"largest-ever\" crackdown on scammers across the globe as it seizes 14,000 devices and $17 billion in illicit funds",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/us-doj-touts-largest-ever-crackdown-on-scammers-across-the-globe-as-it-seizes-14-000-devices-and-usd17-billion-in-illicit-funds-operation-results-in-800-defendants-and-frees-2-200-forced-laborers",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T22:30:00+00:00",
    "summary": "The U.S. Department of Justice has announced that the largest anti-scam push in its history has resulted in more than $8 billion in intended victim losses being recovered, leading to more than 800 def"
  },
  {
    "id": "hn:50552424",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Neon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/",
    "source": "yigitdemirag",
    "platform": "hackernews",
    "points": 1071,
    "published_at": "2026-11-18T21:34:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:50261319",
    "domain": "大厂 AI 动态",
    "title": "Genie 4",
    "url": "https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/",
    "source": "acossta",
    "platform": "hackernews",
    "points": 1044,
    "published_at": "2026-10-27T16:06:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:50276792",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/",
    "source": "acossta",
    "platform": "hackernews",
    "points": 1019,
    "published_at": "2026-10-28T17:01:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50403097",
    "domain": "大厂 AI 动态",
    "title": "Every Mac comes with an (undocumented) family member classifier",
    "url": "https://8rank.ai/game/apple-intelligence-personal-knowledge-graph",
    "source": "infwhispers",
    "platform": "hackernews",
    "points": 873,
    "published_at": "2026-11-07T09:46:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50429426",
    "domain": "大厂 AI 动态",
    "title": "Google Gemini routes personal Drive files and emails to human annotators",
    "url": "https://github.com/thisisme6598/gemini_files/",
    "source": "gf74918",
    "platform": "hackernews",
    "points": 740,
    "published_at": "2026-11-09T18:24:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50363461",
    "domain": "大厂 AI 动态",
    "title": "Tell HN: Gemini trains on chat history, even for subscribers (personal accounts)",
    "url": "https://news.ycombinator.com/item?id=50363461",
    "source": "jameslk",
    "platform": "hackernews",
    "points": 738,
    "published_at": "2026-11-04T10:10:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50439193",
    "domain": "大厂 AI 动态",
    "title": "AlphaProof Code",
    "url": "https://deepmind.google/blog/introducing-alphaproof-code/",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 679,
    "published_at": "2026-11-10T12:11:12+00:00",
    "summary": ""
  },
  {
    "id": "hn:50471431",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Hydrogen",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/",
    "source": "dvaplima",
    "platform": "hackernews",
    "points": 576,
    "published_at": "2026-11-12T18:01:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50456791",
    "domain": "大厂 AI 动态",
    "title": "Gemini Decisions API",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/",
    "source": "iamdelirium",
    "platform": "hackernews",
    "points": 571,
    "published_at": "2026-11-11T18:32:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:50472260",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Hydrogen and Orchestrator",
    "url": "https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/",
    "source": "jonbaer",
    "platform": "hackernews",
    "points": 509,
    "published_at": "2026-11-12T18:52:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:50411961",
    "domain": "大厂 AI 动态",
    "title": "Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU",
    "url": "https://github.com/synchopate/llama-modchip",
    "source": "joshcsimmons",
    "platform": "hackernews",
    "points": 487,
    "published_at": "2026-11-08T10:22:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:50568130",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Neon is the new #1 on the Models Engineering Index",
    "url": "https://git-aarvin.github.io/mei/",
    "source": "hn-aarvin",
    "platform": "hackernews",
    "points": 376,
    "published_at": "2026-11-19T23:35:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50392118",
    "domain": "大厂 AI 动态",
    "title": "Gemini Omni 1.2 Flash",
    "url": "https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 369,
    "published_at": "2026-11-06T13:35:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50288019",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon is the new #1 on the Artificial Analysis Intelligence Index v5",
    "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1",
    "source": "theHocineSaad",
    "platform": "hackernews",
    "points": 339,
    "published_at": "2026-10-29T12:41:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:50550415",
    "domain": "大厂 AI 动态",
    "title": "Genie 4 is now available",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/",
    "source": "leumon",
    "platform": "hackernews",
    "points": 294,
    "published_at": "2026-11-18T18:49:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:50541790",
    "domain": "大厂 AI 动态",
    "title": "Why is Gemini 4 Carbon taking so long?",
    "url": "https://kernel.dev/blog/why-is-gemini-4-carbon-taking-so-long/",
    "source": "deenadz",
    "platform": "hackernews",
    "points": 288,
    "published_at": "2026-11-18T04:14:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:50577901",
    "domain": "大厂 AI 动态",
    "title": "Google workers tell their employer not to punish schools that don't want AI",
    "url": "https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 284,
    "published_at": "2026-11-20T16:59:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50442303",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Carbon is now available",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/",
    "source": "meetpateltech",
    "platform": "hackernews",
    "points": 296,
    "published_at": "2026-11-10T16:07:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50554374",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Neon looks like an Opus 5.5 competitor",
    "url": "https://micjm.com/blog/gemini-4-neon-looks-like-a-top-model/",
    "source": "seizethecheese",
    "platform": "hackernews",
    "points": 259,
    "published_at": "2026-11-19T00:29:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:50638320",
    "domain": "大厂 AI 动态",
    "title": "Gemini refused to give me the lyrics to Twinkle Twinkle Little Star",
    "url": "https://www.comentr.com/technology/01M88DWQ0R4NCMYR17AFEWRG1F",
    "source": "hoodied",
    "platform": "hackernews",
    "points": 190,
    "published_at": "2026-11-25T04:03:33+00:00",
    "summary": ""
  },
  {
    "id": "hn:50569519",
    "domain": "大厂 AI 动态",
    "title": "What Comes After AGI?",
    "url": "https://institute.deepmind.com/essays/what-comes-after-agi/",
    "source": "jdkee",
    "platform": "hackernews",
    "points": 178,
    "published_at": "2026-11-20T02:44:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50557885",
    "domain": "大厂 AI 动态",
    "title": "DeepMind Employees Are Unionising",
    "url": "https://www.gdmunion.co.uk",
    "source": "nervai",
    "platform": "hackernews",
    "points": 124,
    "published_at": "2026-11-19T09:28:56+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/news/1042025/microsoft-code-red-outlook-outage",
    "domain": "大厂 AI 动态",
    "title": "Microsoft declares ‘Code Red’ after huge Outlook outage",
    "url": "https://www.theverge.com/news/1042025/microsoft-code-red-outlook-outage",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T11:12:42+00:00",
    "summary": "This month's Exchange Online and Microsoft Outlook outage has prompted the software giant to declare an unusual \"Code Red\" internally, Reuters reports. The nearly 24-hour outage took down email for mi"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1041957/fincen-treasury-cybersecurity-incident",
    "domain": "大厂 AI 动态",
    "title": "US financial crimes bureau discloses ‘cybersecurity incident’",
    "url": "https://www.theverge.com/policy/1041957/fincen-treasury-cybersecurity-incident",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T01:00:00+00:00",
    "summary": "The Financial Crimes Enforcement Network (FinCEN) disclosed on Tuesday that it's investigating a \"cybersecurity incident.\" The bureau, which is part of the Treasury Department, said it's looking into "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1024777/best-gifts-for-dad-2026",
    "domain": "大厂 AI 动态",
    "title": "The Verge’s 2026 gift guide for dads",
    "url": "https://www.theverge.com/gadgets/1024777/best-gifts-for-dad-2026",
    "source": "Ryan Waniata",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T23:59:29+00:00",
    "summary": "Gone are the days when you could just buy your father a random tie or some leather-clad alcohol vessel or a shaving kit. Dads want - nay, deserve - something memorable. Luckily for you, it's not that "
  },
  {
    "id": "rss:https://www.theverge.com/science/1041819/us-army-detonation-lead-explosives-iowa",
    "domain": "大厂 AI 动态",
    "title": "Why the US Army is about to blow up nearly 10,000 pounds of unstable explosives in Iowa",
    "url": "https://www.theverge.com/science/1041819/us-army-detonation-lead-explosives-iowa",
    "source": "Justine Calma",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T23:25:46+00:00",
    "summary": "The US Army is moving ahead with plans to detonate the nation's stockpile of lead azide at an ammunition plant in Middletown, Iowa, at approximately 9:00AM CST on Wednesday. The Verge reached out to e"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1041820/huawei-guilty-trade-secrets-trial",
    "domain": "大厂 AI 动态",
    "title": "Huawei found guilty of stealing trade secrets",
    "url": "https://www.theverge.com/tech/1041820/huawei-guilty-trade-secrets-trial",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T22:23:27+00:00",
    "summary": "A jury has found Huawei guilty of stealing US trade secrets, as reported earlier by NBC News and Bloomberg. The verdict, handed down in a federal court in New York, concludes a years-long legal battle"
  },
  {
    "id": "rss:https://www.theverge.com/news/1041690/grand-theft-auto-6-pc-recompilation-project-leonida-takedown-take-two",
    "domain": "大厂 AI 动态",
    "title": "GTA VI PC recompilation project shut down by Take-Two",
    "url": "https://www.theverge.com/news/1041690/grand-theft-auto-6-pc-recompilation-project-leonida-takedown-take-two",
    "source": "Tom Warren",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T21:39:14+00:00",
    "summary": "Game modding communities are racing to get Grand Theft Auto VI running on PC, but one big effort has been taken down by Take-Two today. Leonida, a fan project by 15-year-old \"NotRexed,\" has vanished a"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1021621/best-gifts-for-mom-2026",
    "domain": "大厂 AI 动态",
    "title": "The Verge’s 2026 holiday gift guide for moms",
    "url": "https://www.theverge.com/gadgets/1021621/best-gifts-for-mom-2026",
    "source": "Ryan Waniata",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T21:09:59+00:00",
    "summary": "Given everything moms do for us, it feels good to give back during the holidays. But where to start? How do you come up with a physical representation of how you feel about such a key and influential "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1041618/tiktok-down-outage",
    "domain": "大厂 AI 动态",
    "title": "TikTok was down",
    "url": "https://www.theverge.com/tech/1041618/tiktok-down-outage",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T20:27:27+00:00",
    "summary": "Earlier on Tuesday, TikTok experienced some issues, with videos, search results, favorites, and other features not loading as they usually do, following a slew of other outages over the past couple of"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1041571/jensen-huang-all-hands-nvidia-apology",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang reportedly tells Nvidia staff it&#8217;s ‘not true’ Trump got him rehired",
    "url": "https://www.theverge.com/tech/1041571/jensen-huang-all-hands-nvidia-apology",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T20:02:03+00:00",
    "summary": "Nvidia CEO Jensen Huang apologized to staff during his first all-hands since returning to the company, while attempting to distance himself from the narrative that the White House and tech leaders hel"
  },
  {
    "id": "rss:https://www.theverge.com/policy/1041568/fisa-ndaa-blue-wave",
    "domain": "大厂 AI 动态",
    "title": "The clock is running out for America’s most contentious spying law",
    "url": "https://www.theverge.com/policy/1041568/fisa-ndaa-blue-wave",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T20:00:00+00:00",
    "summary": "Weeks before the end of the legislative session, some members of Congress are scrambling to reauthorize a controversial warrantless wiretapping authority, possibly by attaching it to a must-pass milit"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/yales-sonnenfeld-nvidia-is-a-detriment-to-u-s-industrial-might-not-a-champion/",
    "domain": "大厂 AI 动态",
    "title": "Yale’s Sonnenfeld: Nvidia is a ‘detriment’ to US industrial might — not a champion",
    "url": "https://techcrunch.com/2026/11/24/yales-sonnenfeld-nvidia-is-a-detriment-to-u-s-industrial-might-not-a-champion/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T00:12:02+00:00",
    "summary": "Yale's Jeffrey Sonnenfeld warns that what the market cheered Monday, Jensen Huang's White House–backed return as Nvidia's CEO and board member, could prove a giant mistake, exposing the directors to \""
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/trump-reportedly-says-pardoning-jensen-huang-is-an-option-but-that-he-doesnt-think-it-will-be-necessary/",
    "domain": "大厂 AI 动态",
    "title": "Trump reportedly says pardoning Jensen Huang is ‘an option’",
    "url": "https://techcrunch.com/2026/11/24/trump-reportedly-says-pardoning-jensen-huang-is-an-option-but-that-he-doesnt-think-it-will-be-necessary/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-25T00:10:27+00:00",
    "summary": "Huang faces ongoing questions about his relationship with Alice Huang, an executive with alleged ties to Chinese intelligence who previously worked for a company that has been accused of illegally div"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/jensen-huang-still-thinks-a-succession-plan-creates-unnecessary-hierarchy/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang still thinks a succession plan creates unnecessary hierarchy",
    "url": "https://techcrunch.com/2026/11/24/jensen-huang-still-thinks-a-succession-plan-creates-unnecessary-hierarchy/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T22:27:52+00:00",
    "summary": "It's a remarkable stance for a company that spent the last two weeks finding out what happens without its founder."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/in-all-hands-meeting-jensen-huang-thanks-white-house-and-says-hes-in-therapy/",
    "domain": "大厂 AI 动态",
    "title": "In all-hands meeting, Jensen Huang thanks White House and says he’s in therapy",
    "url": "https://techcrunch.com/2026/11/24/in-all-hands-meeting-jensen-huang-thanks-white-house-and-says-hes-in-therapy/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T21:48:27+00:00",
    "summary": "The Nvidia founder apologized to his staff on Tuesday and said he was grateful for a second chance to lead the company."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/even-the-best-ai-agents-struggle-with-everyday-life/",
    "domain": "大厂 AI 动态",
    "title": "Even the best AI agents struggle with everyday life",
    "url": "https://techcrunch.com/2026/11/24/even-the-best-ai-agents-struggle-with-everyday-life/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T21:33:29+00:00",
    "summary": "As millions embrace personal AI assistants, a new benchmark reveals that even the most advanced AI models struggle to complete everyday tasks reliably and safely without introducing potential new prob"
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/walmart-teams-up-with-meta-to-bring-black-friday-deals-to-ai-agent-muse/",
    "domain": "大厂 AI 动态",
    "title": "Walmart teams up with Meta to bring Black Friday deals to AI agent Muse",
    "url": "https://techcrunch.com/2026/11/24/walmart-teams-up-with-meta-to-bring-black-friday-deals-to-ai-agent-muse/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T21:32:38+00:00",
    "summary": "Walmart now lets customers shop Black Friday deals through Muse, Meta’s AI agent."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/maple-raises-5-3m-to-build-ai-products-that-protect-your-data-even-from-itself/",
    "domain": "大厂 AI 动态",
    "title": "Maple raises $5.3M to build AI products that protect your data, even from itself",
    "url": "https://techcrunch.com/2026/11/24/maple-raises-5-3m-to-build-ai-products-that-protect-your-data-even-from-itself/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T21:19:52+00:00",
    "summary": "The startup's encrypted AI architecture is designed to prevent even the company itself from accessing users' private data."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/dozens-of-oil-and-shipping-tankers-hacked-in-recent-weeks-per-report/",
    "domain": "大厂 AI 动态",
    "title": "Dozens of oil and shipping tankers hacked in recent weeks, per report",
    "url": "https://techcrunch.com/2026/11/24/dozens-of-oil-and-shipping-tankers-hacked-in-recent-weeks-per-report/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T21:09:04+00:00",
    "summary": "Iran is the chief suspect behind the dozens of cyberattacks targeting oil and chemical shipping vessels."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/anthropic-shares-fall-below-ipo-price-a-worrying-sign-for-ai-startups/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic shares fall below IPO price, a worrying sign for AI startups",
    "url": "https://techcrunch.com/2026/11/24/anthropic-shares-fall-below-ipo-price-a-worrying-sign-for-ai-startups/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T18:30:42+00:00",
    "summary": "Anthropic’s post-IPO slump could put pressure on AI startup valuations."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/uk-warns-ai-driven-cyberattacks-are-exposing-years-of-weak-security/",
    "domain": "大厂 AI 动态",
    "title": "UK warns AI-driven cyberattacks are exposing years of weak security",
    "url": "https://techcrunch.com/2026/11/24/uk-warns-ai-driven-cyberattacks-are-exposing-years-of-weak-security/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T18:02:59+00:00",
    "summary": "The British cyber agency says that \"building strong foundations has never mattered more\" as AI hacking tools rely on exploiting simple security flaws."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/threads-comes-to-ipad-and-takes-a-page-from-xs-playbook-with-cashtags/",
    "domain": "大厂 AI 动态",
    "title": "Threads comes to iPad and takes a page from X’s playbook with cashtags",
    "url": "https://techcrunch.com/2026/11/24/threads-comes-to-ipad-and-takes-a-page-from-xs-playbook-with-cashtags/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T17:44:34+00:00",
    "summary": "The addition of live stock quotes and charts could help Threads attract the financial community that has historically relied on X."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/electric-truck-startup-harbinger-gets-financing-boost-from-palmer-luckeys-bank/",
    "domain": "大厂 AI 动态",
    "title": "Electric truck startup Harbinger gets financing boost from Palmer Luckey’s bank",
    "url": "https://techcrunch.com/2026/11/24/electric-truck-startup-harbinger-gets-financing-boost-from-palmer-luckeys-bank/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T17:29:09+00:00",
    "summary": "Harbinger has tapped Palmer Luckey's Erebor Bank as a new source of capital as the electric truck startup looks to diversify how it funds its growth."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/meta-brings-its-muse-ai-assistant-directly-into-instagram-dms/",
    "domain": "大厂 AI 动态",
    "title": "Meta brings its Muse AI assistant directly into Instagram DMs",
    "url": "https://techcrunch.com/2026/11/24/meta-brings-its-muse-ai-assistant-directly-into-instagram-dms/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T17:00:00+00:00",
    "summary": "The new integration gets rid of the need for users to toggle between Instagram and the Muse app when they want to interact with the AI agent."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/tidal-to-ban-and-remove-millions-of-ai-generated-tracks-as-ai-slop-inundates-music-streaming/",
    "domain": "大厂 AI 动态",
    "title": "Tidal to ban and remove millions of AI-generated tracks as AI slop inundates music streaming",
    "url": "https://techcrunch.com/2026/11/24/tidal-to-ban-and-remove-millions-of-ai-generated-tracks-as-ai-slop-inundates-music-streaming/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T16:46:00+00:00",
    "summary": "The company said it will still accept songs that were made with AI assistance, but not fully generated."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/uber-and-nuro-begin-driverless-testing-of-lucid-robotaxis-ahead-of-2027-launch/",
    "domain": "大厂 AI 动态",
    "title": "Uber and Nuro begin driverless testing of Lucid robotaxis ahead of 2027 launch",
    "url": "https://techcrunch.com/2026/11/24/uber-and-nuro-begin-driverless-testing-of-lucid-robotaxis-ahead-of-2027-launch/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T16:40:46+00:00",
    "summary": "Uber and Nuro have started testing driverless Lucid Gravity SUVs on public streets in the San Francisco Bay Area."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/why-a-crusoe-investor-is-betting-on-solar-and-batteries-to-power-future-ai-data-centers/",
    "domain": "大厂 AI 动态",
    "title": "Why a Crusoe investor is betting on solar and batteries to power future AI data centers",
    "url": "https://techcrunch.com/2026/11/24/why-a-crusoe-investor-is-betting-on-solar-and-batteries-to-power-future-ai-data-centers/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T16:10:00+00:00",
    "summary": "Next-generation data centers will need tens of gigawatts of power every year. One of Crusoe's investors thinks solar and energy storage are the obvious choice."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/pinterest-will-now-let-parents-limit-the-ai-generated-content-their-teens-see/",
    "domain": "大厂 AI 动态",
    "title": "Pinterest will now let parents limit the AI-generated content their teens see",
    "url": "https://techcrunch.com/2026/11/24/pinterest-will-now-let-parents-limit-the-ai-generated-content-their-teens-see/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T16:02:37+00:00",
    "summary": "While other social platforms have focused on restricting teens' access to AI chatbots, Pinterest is addressing the AI content filling their feeds."
  },
  {
    "id": "rss:https://techcrunch.com/2026/11/24/amazons-decart-acquisition-is-a-bet-on-using-software-to-narrow-the-gap-with-nvidia-in-the-ai-chip-race/",
    "domain": "大厂 AI 动态",
    "title": "Amazon’s Decart acquisition is a bet on using software to narrow the silicon gap with Nvidia",
    "url": "https://techcrunch.com/2026/11/24/amazons-decart-acquisition-is-a-bet-on-using-software-to-narrow-the-gap-with-nvidia-in-the-ai-chip-race/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-24T15:51:07+00:00",
    "summary": "Amazon’s decision to acquire Decart for a reported $7.5 billion is part of its efforts to improve the efficiency of its Trainium chips."
  },
  {
    "id": "hn:50556287",
    "domain": "股票",
    "title": "Ruby2ßhell: Pre-authentication RCE on stock Rails",
    "url": "https://verialabs.com/ruby2shell/",
    "source": "jdns",
    "platform": "hackernews",
    "points": 409,
    "published_at": "2026-11-19T05:09:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:50344919",
    "domain": "股票",
    "title": "The SEC Should Block Anthropic's IPO to Protect the Public",
    "url": "https://www.techpolicy.press/the-sec-should-block-anthropics-ipo-to-protect-the-public/",
    "source": "cdrnsf",
    "platform": "hackernews",
    "points": 406,
    "published_at": "2026-11-02T22:30:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50307219",
    "domain": "股票",
    "title": "Anthropic may not secure investment-grade rating after IPO, Blackstone says",
    "url": "https://www.ft.com/content/59383c7f-8d82-493f-bf01-d2e862a1018f",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 327,
    "published_at": "2026-10-30T17:27:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50394906",
    "domain": "股票",
    "title": "Anthropic IPO buyers see valuation as low as $1.1T",
    "url": "https://www.bloomberg.com/news/articles/2026-11-06/anthropic-ipo-valuation-expectations-pressured-after-ai-rout",
    "source": "dgellow",
    "platform": "hackernews",
    "points": 322,
    "published_at": "2026-11-06T16:54:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:50620721",
    "domain": "股票",
    "title": "Freeing the iPod Nano 5G",
    "url": "https://viktorkrapivin.com/blog/nano5g-priv-prvd",
    "source": "rpm_conservatio",
    "platform": "hackernews",
    "points": 145,
    "published_at": "2026-11-23T23:03:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50337454",
    "domain": "股票",
    "title": "Jobless tech workers are being left out of San Francisco's AI boom",
    "url": "https://www.bloomberg.com/news/features/2026-09-17/san-francisco-s-ai-wealth-boom-skirts-engineers-as-openai-anthropic-ipos-near",
    "source": "mancerayder",
    "platform": "hackernews",
    "points": 188,
    "published_at": "2026-11-02T14:40:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50583254",
    "domain": "股票",
    "title": "Nasdaq erases all 2026 gains",
    "url": "https://www.cnbc.com/2026/11/19/stock-market-today-live-updates.html",
    "source": "mv4",
    "platform": "hackernews",
    "points": 134,
    "published_at": "2026-11-20T22:29:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50617640",
    "domain": "股票",
    "title": "Two \"suspicious clusters\" on Polymarket Made Over $340k on Huang Comeback",
    "url": "https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-23-2026/card/two-groups-of-polymarket-accounts-made-over-340-000-on-huang-comeback-Lan2T0TwbJPNsyhmQHGq",
    "source": "qlte",
    "platform": "hackernews",
    "points": 59,
    "published_at": "2026-11-23T19:25:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:50510005",
    "domain": "股票",
    "title": "Do House members' stock trades beat the market? A test of 8,900 trades",
    "url": "https://arkanumdata.com/research/house-trades",
    "source": "Bluestein",
    "platform": "hackernews",
    "points": 129,
    "published_at": "2026-11-15T19:46:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50634815",
    "domain": "股票",
    "title": "Nasdaq Resumes Selloff as Nvidia, Anthropic Shares Slump",
    "url": "https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-24-2026",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-11-24T21:14:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50629413",
    "domain": "股票",
    "title": "Anthropic falls below $83 IPO price in Swift reversal after record listing",
    "url": "https://www.reuters.com/business/anthropic-breaks-below-83-ipo-price-debut-rally-unravels-2026-11-24/",
    "source": "thm",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-11-24T15:15:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50588647",
    "domain": "股票",
    "title": "Anthropic's IPO bank closed position meant to stabilize stock",
    "url": "https://www.reuters.com/markets/us/anthropics-ipo-bank-closed-position-meant-stabilize-stock-removing-source-2026-11-20",
    "source": "anon373839",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-11-21T12:43:24+00:00",
    "summary": ""
  },
  {
    "id": "hn:50311311",
    "domain": "股票",
    "title": "Anthropic to receive high 'junk' rating from credit agencies following IPO",
    "url": "https://techcrunch.com/2026/10/30/anthropic-expected-to-receive-high-junk-rating-from-credit-agencies-following-ipo-report-says/",
    "source": "jnord",
    "platform": "hackernews",
    "points": 104,
    "published_at": "2026-10-30T23:08:12+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/supply-and-demand",
    "domain": "股票",
    "title": "Supply and Demand",
    "url": "https://www.netinterest.co/p/supply-and-demand",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-23T15:38:25+00:00",
    "summary": "Finding Equilibrium Inside the AI Economy"
  },
  {
    "id": "hn:50395318",
    "domain": "股票",
    "title": "Anthropic IPO valuation talks drop to $1.3T",
    "url": "https://epyhia.com/anthropic-ipo-valuation-talks-drop-to-1-3-trillion-as-major-investors",
    "source": "arbuge",
    "platform": "hackernews",
    "points": 93,
    "published_at": "2026-11-06T17:21:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50386597",
    "domain": "股票",
    "title": "Major Investors Are Skeptical Anthropic IPO Can Achieve $1.5T Valuation",
    "url": "https://www.wsj.com/finance/major-investors-are-skeptical-anthropic-ipo-can-achieve-1-5-trillion-valuation-ca965d8b’",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 91,
    "published_at": "2026-11-06T00:31:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:50350560",
    "domain": "股票",
    "title": "Anthropic IPO filing: $1.7B quarterly payroll, about $107K per employee monthly",
    "url": "https://www.techspot.com/news/114428-anthropic-ipo-filing-reveals-17-billion-quarterly-personnel.html",
    "source": "entryleveljobsc",
    "platform": "hackernews",
    "points": 84,
    "published_at": "2026-11-03T11:16:07+00:00",
    "summary": ""
  },
  {
    "id": "hn:50439616",
    "domain": "股票",
    "title": "Anthropic to Seek $1.3T Valuation in IPO",
    "url": "https://www.wsj.com/finance/stocks/anthropic-to-seek-1-3-trillion-valuation-in-ipo-8337b669",
    "source": "sonabinu",
    "platform": "hackernews",
    "points": 60,
    "published_at": "2026-11-10T12:49:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:50581060",
    "domain": "股票",
    "title": "Army delays detonating \"catastrophically hazardous\" lead azide amid fear, anger",
    "url": "https://arstechnica.com/science/2026/11/outrage-questions-swirl-as-army-delays-blowing-up-stockpile-of-toxic-lead-azide/",
    "source": "Bender",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-11-20T20:01:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50342424",
    "domain": "股票",
    "title": "Anthropic reveals $900B AI spending commitments ahead of IPO",
    "url": "https://www.ft.com/content/4d91dbab-6fe4-45ab-beee-d77e091cb37f",
    "source": "zomtorg",
    "platform": "hackernews",
    "points": 74,
    "published_at": "2026-11-02T19:36:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50549623",
    "domain": "股票",
    "title": "Just say no to Anthropic's IPO",
    "url": "https://garymarcus.substack.com/p/just-say-no-to-anthropics-ipo",
    "source": "Betelbuddy",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-11-18T17:54:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50542361",
    "domain": "股票",
    "title": "Interesting Learnings Working for a Startup",
    "url": "https://news.ycombinator.com/item?id=50542361",
    "source": "Jessiejia11",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-11-18T05:52:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50553581",
    "domain": "股票",
    "title": "Anthropic reportedly prices its IPO at $83 per share, valuing at $1.5T",
    "url": "https://apnews.com/article/anthropic-ipo-pricing-70b660ddf900d90bbf484ecdf1fb441c",
    "source": "6thbit",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-11-18T23:00:26+00:00",
    "summary": ""
  },
  {
    "id": "hn:50484110",
    "domain": "股票",
    "title": "Amodei Says AI Will Cure Cancer in a Decade. Doctors Are Skeptical",
    "url": "https://www.businessinsider.com/dario-amodei-anthropic-cancer-cure-ipo-roadshow-backlash-doctors-2026-11",
    "source": "robin_reala",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-11-13T14:34:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:50467092",
    "domain": "股票",
    "title": "Jensen Huang resigning effective immediately",
    "url": "https://www.stocktitan.net/news/NVDA/nvidia-announces-ceo-03al5m45ne1p.html",
    "source": "chrisss395",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-11-12T13:52:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50463421",
    "domain": "股票",
    "title": "Nvidia's Disappearing Singapore Sales Deepen Mystery Around Megaspeed",
    "url": "https://www.wsj.com/business/earnings/nvidias-disappearing-singapore-sales-deepen-mystery-around-megaspeed-7d483180",
    "source": "ea016",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-11-12T05:31:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:50507517",
    "domain": "股票",
    "title": "A Human Reads the Anthropic IPO Filing",
    "url": "https://www.nytimes.com/2026/11/15/business/anthropic-ipo-filing-prospectus.html",
    "source": "saikatsg",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-11-15T15:18:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50529644",
    "domain": "股票",
    "title": "Who Is Anthropic Kidding?",
    "url": "https://www.theatlantic.com/economy/2026/11/anthropic-ipo-ai-safety/689440/",
    "source": "nothrowaways",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-11-17T10:25:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:50351712",
    "domain": "股票",
    "title": "Anthropic's IPO Filing Warns It May Be 'Imminently' Close to RSI",
    "url": "https://epyhia.com/anthropic-s-ipo-filing-warns-it-may-be-imminently-close-to-recursive",
    "source": "arbuge",
    "platform": "hackernews",
    "points": 35,
    "published_at": "2026-11-03T13:26:43+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/a-bankers-guide-to-anthropic",
    "domain": "股票",
    "title": "A Banker’s Guide to Anthropic",
    "url": "https://www.netinterest.co/p/a-bankers-guide-to-anthropic",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-13T18:00:43+00:00",
    "summary": "Why the IPO is a credit event"
  },
  {
    "id": "hn:50385642",
    "domain": "股票",
    "title": "Michael Burry says Anthropic is 'betting its existence' on optimism",
    "url": "https://www.businessinsider.com/michael-burry-anthropic-ipo-outlook-ant-big-short-2026-11",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-11-05T22:49:47+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-insatiable-demand-for-alpha",
    "domain": "股票",
    "title": "The Insatiable Demand for Alpha",
    "url": "https://www.netinterest.co/p/the-insatiable-demand-for-alpha",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-11-06T17:59:24+00:00",
    "summary": "Why a market shakedown could leave the biggest pod shops stronger"
  },
  {
    "id": "rss:https://www.netinterest.co/p/follow-the-money-ece",
    "domain": "股票",
    "title": "Follow the Money",
    "url": "https://www.netinterest.co/p/follow-the-money-ece",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-30T17:48:55+00:00",
    "summary": "What six years and 300+ posts of Net Interest say about where finance is heading"
  },
  {
    "id": "rss:https://www.netinterest.co/p/capital-wars",
    "domain": "股票",
    "title": "Capital Wars",
    "url": "https://www.netinterest.co/p/capital-wars",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-23T16:24:17+00:00",
    "summary": "CoreWeave and the Economics of a Data Center Build"
  },
  {
    "id": "rss:https://www.netinterest.co/p/me-and-my-agents",
    "domain": "股票",
    "title": "Me and My Agents",
    "url": "https://www.netinterest.co/p/me-and-my-agents",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:39:55+00:00",
    "summary": "Unleashing AI Agents on Bank Earnings"
  },
  {
    "id": "rss:https://www.netinterest.co/p/when-saturday-comes",
    "domain": "股票",
    "title": "When Saturday Comes",
    "url": "https://www.netinterest.co/p/when-saturday-comes",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-10T12:42:20+00:00",
    "summary": "Football as an Asset Class"
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-art-of-doing-financial-engineering",
    "domain": "股票",
    "title": "The Art of Doing Financial Engineering",
    "url": "https://www.netinterest.co/p/the-art-of-doing-financial-engineering",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-03T11:57:49+00:00",
    "summary": "AI Financing at the Frontier"
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-agents-revolt",
    "domain": "股票",
    "title": "Agents Revolt",
    "url": "https://www.netinterest.co/p/the-agents-revolt",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:33:27+00:00",
    "summary": "What happens to finance when customers start paying attention"
  },
  {
    "id": "rss:https://www.netinterest.co/p/brookfield-of-dreams",
    "domain": "股票",
    "title": "Brookfield of Dreams",
    "url": "https://www.netinterest.co/p/brookfield-of-dreams",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-19T15:05:47+00:00",
    "summary": "Inside Brookfield&#8217;s Plan to Double Again"
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
    "id": "hn:50532613",
    "domain": "金融",
    "title": "Brazil's tax authority open-sources its tax calculator on GitHub under MIT",
    "url": "https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/novembro/receita-federal-publica-primeiro-codigo-fonte-aberto-no-github-e-amplia-transparencia-da-reforma-tributaria",
    "source": "dvaplima",
    "platform": "hackernews",
    "points": 789,
    "published_at": "2026-11-17T15:22:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:50385870",
    "domain": "金融",
    "title": "Cuban: Facebook knowingly runs AI deepfake scam ads; docs say $16B fraud revenue",
    "url": "https://finance.yahoo.com/technology/ai/articles/mark-cuban-says-facebook-knowingly-213000020.html",
    "source": "randycupertino",
    "platform": "hackernews",
    "points": 525,
    "published_at": "2026-11-05T23:09:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:50305573",
    "domain": "金融",
    "title": "The federated code forge",
    "url": "https://tangled.org/blog/forge/",
    "source": "zlliang",
    "platform": "hackernews",
    "points": 333,
    "published_at": "2026-10-30T15:44:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50568082",
    "domain": "金融",
    "title": "Visa, Mastercard and JPMorgan Customer Data Leaked by Hackers",
    "url": "https://www.wsj.com/finance/banking/visa-mastercard-and-jpmorgan-customer-data-leaked-by-hackers-3b5a0f87",
    "source": "mikhael",
    "platform": "hackernews",
    "points": 198,
    "published_at": "2026-11-19T23:32:11+00:00",
    "summary": ""
  },
  {
    "id": "hn:50346153",
    "domain": "金融",
    "title": "Intel stock collapse worsens as $3.5T chip rout spreads",
    "url": "https://finance.yahoo.com/markets/article/the-intel-stock-collapse-is-getting-worse--and-the-37-trillion-chip-rout-is-spreading-212154947.html",
    "source": "entryleveljobsc",
    "platform": "hackernews",
    "points": 237,
    "published_at": "2026-11-03T00:08:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50342284",
    "domain": "金融",
    "title": "Oracle files to sell $20B in new stock, bonds to finance AI buildout",
    "url": "https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html",
    "source": "smartmic",
    "platform": "hackernews",
    "points": 200,
    "published_at": "2026-11-02T19:27:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50602847",
    "domain": "金融",
    "title": "Canada recommits to federal funding for news",
    "url": "https://www.niemanlab.org/2026/11/a-government-that-gets-it-canada-recommits-to-federal-funding-for-news/",
    "source": "DeepLogin",
    "platform": "hackernews",
    "points": 127,
    "published_at": "2026-11-22T19:10:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50260526",
    "domain": "金融",
    "title": "A $300B 'Debt Wall' Is Looming over Private-Equity Backed Companies",
    "url": "https://www.wsj.com/finance/investing/a-300-billion-debt-wall-is-looming-over-private-equity-backed-companies-d6359497",
    "source": "JumpCrisscross",
    "platform": "hackernews",
    "points": 178,
    "published_at": "2026-10-27T15:09:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:50525658",
    "domain": "金融",
    "title": "Pentagon fails ninth straight audit despite progress in organizing finances",
    "url": "https://www.reuters.com/business/aerospace-defense/pentagon-fails-ninth-straight-audit-despite-progress-organizing-finances-2026-11-16/",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 152,
    "published_at": "2026-11-17T00:23:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:50605699",
    "domain": "金融",
    "title": "'It's greed': Zohran Mamdani blasts Amazon over new $5 fee hike in NYC",
    "url": "https://finance.yahoo.com/economy/policy/articles/greed-zohran-mamdani-blasts-amazon-121000124.html",
    "source": "madihaa",
    "platform": "hackernews",
    "points": 58,
    "published_at": "2026-11-23T00:23:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50532322",
    "domain": "金融",
    "title": "A US Federal Women's Prison Became a \"Rape Club\"",
    "url": "https://www.propublica.org/article/federal-womens-prison-sexual-abuse-reform-dublin-bop",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 87,
    "published_at": "2026-11-17T15:03:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:50594937",
    "domain": "金融",
    "title": "Tesla launches FSD v15, targets its biggest weaknesses, from signs to potholes",
    "url": "https://electrek.co/2026/11/21/tesla-fsd-v15-rollout-25x-safety-reality-view/",
    "source": "m348e912",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-11-22T00:14:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:50505905",
    "domain": "金融",
    "title": "Jensen Huang allegedly manufactured the GPU shortage",
    "url": "https://wccftech.com/jensen-huang-financed-ai-startups-absorb-excess-silicon/",
    "source": "bobsoap",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-11-15T10:53:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50278678",
    "domain": "金融",
    "title": "Show HN: A proof-of-concept formalization of the IRS federal tax forms",
    "url": "https://github.com/emmilco/us-tax-model",
    "source": "RGS1811",
    "platform": "hackernews",
    "points": 84,
    "published_at": "2026-10-28T18:30:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50543108",
    "domain": "金融",
    "title": "Firefox opens hotline for users sick of Microsoft shoving Edge down their throat",
    "url": "https://www.neowin.net/news/firefox-opens-hotline-for-windows-users-fed-up-with-microsoft-shoving-edge-down-their-throat/",
    "source": "bundie",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-11-18T07:51:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:50475829",
    "domain": "金融",
    "title": "Richard Posner has died",
    "url": "https://www.law.uchicago.edu/news/senior-lecturer-richard-posner-law-and-economics-pioneer-and-former-federal-appellate-judge",
    "source": "sebg",
    "platform": "hackernews",
    "points": 52,
    "published_at": "2026-11-12T23:19:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:50253630",
    "domain": "金融",
    "title": "The 'Buy, Borrow and Die' Wealth Strategy Has Become a $5T Market",
    "url": "https://www.wsj.com/finance/the-buy-borrow-and-die-wealth-strategy-has-become-a-5-trillion-market-d9149a9d",
    "source": "tysone",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-10-27T01:30:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:50291902",
    "domain": "金融",
    "title": "Alphabet heads for a $500B drop in market value, biggest in its history",
    "url": "https://finance.yahoo.com/markets/article/alphabet-heads-for-a-500-billion-drop-in-market-value-the-biggest-in-its-history-134824763.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 62,
    "published_at": "2026-10-29T16:39:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:50492178",
    "domain": "金融",
    "title": "Tesla Opens Cybercab Orders to 'Select Customers' at $29,990 Plus $299 per Month",
    "url": "https://insideevs.com/news/815473/tesla-cybercab-pricing-sales-announced/",
    "source": "iBelieve",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-11-14T00:33:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50523346",
    "domain": "金融",
    "title": "The Fed Is Worried AI Agents Could Trigger a Bank Run",
    "url": "https://gizmodo.com/the-fed-is-worried-ai-agents-could-trigger-a-bank-run-2000840566",
    "source": "pera",
    "platform": "hackernews",
    "points": 27,
    "published_at": "2026-11-16T21:12:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50352405",
    "domain": "金融",
    "title": "US Hedge Funds Just Sold Every AI Stock They Bought Since 2025",
    "url": "https://finance.yahoo.com/markets/stocks/articles/us-hedge-funds-just-sold-113114644.html",
    "source": "robin_reala",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-11-03T14:27:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:50372038",
    "domain": "金融",
    "title": "Harmony: Chat like Discord. Federated like email",
    "url": "https://mony.lol/",
    "source": "FinalDestiny",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-11-04T21:49:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50328462",
    "domain": "金融",
    "title": "US Jobs Pickup May Keep Fed on Track to Hike Rates Again",
    "url": "https://www.bloomberg.com/news/articles/2026-10-31/us-jobs-pickup-may-keep-fed-on-track-to-hike-rates-again",
    "source": "frank_clover",
    "platform": "hackernews",
    "points": 36,
    "published_at": "2026-11-01T18:51:29+00:00",
    "summary": ""
  },
  {
    "id": "hn:50394771",
    "domain": "金融",
    "title": "Only 16% of U.S. fast-charging stations meet federal NEVI standards (open data)",
    "url": "https://chargingnear.me/data",
    "source": "parkgraph",
    "platform": "hackernews",
    "points": 33,
    "published_at": "2026-11-06T16:45:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:50384382",
    "domain": "金融",
    "title": "Chip stocks get slaughtered as Wall Street in worst post-midterm day since 1896",
    "url": "https://finance.yahoo.com/markets/article/chip-stocks-get-slaughtered-as-wall-street-heads-for-its-worst-post-midterm-day-since-1896-163413900.html",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-11-05T20:58:36+00:00",
    "summary": ""
  }
]
```
