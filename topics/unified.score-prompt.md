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

- 今日日期：`2026-08-20`
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
  "date": "2026-08-20",
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
    "id": "bvid:BV1BVEs6LENZ",
    "domain": "AI",
    "title": "【2026最新Codex】Codex保姆级完整教程-Codex新手保姆级教程-最强AI助手！从入门到进阶，22分钟速通Codex！【附教程文档安装包】",
    "url": "http://www.bilibili.com/video/av116707129561197",
    "source": "编程大佬陈悠秀",
    "platform": "bilibili",
    "points": 2128341,
    "published_at": "2026-06-07T05:32:32+00:00",
    "summary": "最近Codex的能力越来越全面，变成了Codex四大形态里最强一个。 Codex APP 比起 Claude Code，额度更高，功能更全，免费账户也能用。而且不会出现限速、封号、降智等问题，用过的小伙伴直呼真香。本期视频带来一个Codex APP的完整教程"
  },
  {
    "id": "bvid:BV1KjoxBoEQJ",
    "domain": "AI",
    "title": "9分钟搞定！Claude Code 保姆级安装+原理+真实用法（国内直连）",
    "url": "http://www.bilibili.com/video/av116447535765612",
    "source": "人工大黑",
    "platform": "bilibili",
    "points": 1730215,
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
    "points": 1699975,
    "published_at": "2026-03-14T14:22:56+00:00",
    "summary": "AI 核心概念大串联：LLM, Token, Context, Context Window, Prompt, User Prompt, System Prompt, Tool, MCP, Agent, Agent Skill，一期视频带你打通 AI 底层逻辑！"
  },
  {
    "id": "bvid:BV1NvRyBzEhq",
    "domain": "AI",
    "title": "全网最全！60分钟全面掌握Claude Code～【附完整文档】",
    "url": "http://www.bilibili.com/video/av116522328524431",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1520858,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1j9MP6wEV9",
    "domain": "AI",
    "title": "从零开始，学会让桌面Agent帮你干活！【小白教程】",
    "url": "http://www.bilibili.com/video/av116861865887789",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 1335042,
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
    "points": 1279250,
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
    "points": 1153610,
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
    "points": 1078928,
    "published_at": "2026-03-07T11:28:39+00:00",
    "summary": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！"
  },
  {
    "id": "bvid:BV1o4gw6ZExs",
    "domain": "AI",
    "title": "我是怎么用AI干活的？",
    "url": "http://www.bilibili.com/video/av117092535768773",
    "source": "林亦LYi",
    "platform": "bilibili",
    "points": 1052400,
    "published_at": "2026-08-14T12:00:00+00:00",
    "summary": "AI 办公到底能干些啥？它真的能颠覆我们的工作方式，以至于让大厂押上身家也要卷吗？"
  },
  {
    "id": "bvid:BV12omoB4ExF",
    "domain": "AI",
    "title": "黑马程序员全网最全Coze智能体入门到项目实战全套教程，从AI Agent开发入门到6大AI智能体实战项目，涵盖提示词Prompt、RAG、Bot发布微信公众号",
    "url": "http://www.bilibili.com/video/av115713129843205",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 1048921,
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
    "points": 943961,
    "published_at": "2025-01-07T10:01:48+00:00",
    "summary": "普通人也可以看的 AI 编程指南\n全网最详细的 Cursor 教程\nCursor 核心功能、使用技巧和思路\n如何免费白嫖 Cursor"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 875880,
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
    "points": 629262,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1wugF6YEL3",
    "domain": "AI",
    "title": "再见Claude Code！你好DeepSeek Harness！",
    "url": "http://www.bilibili.com/video/av117089415204498",
    "source": "Lau博士的云组会",
    "platform": "bilibili",
    "points": 620091,
    "published_at": "2026-08-13T17:42:16+00:00",
    "summary": "DeepSeek Harness开源了。看完就两个字：牛逼\n本期视频，Lau博士就带着大家一起，解读DeepSeek 亲手做的这个 Harness，到底有什么不一样。"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 599026,
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
    "points": 546172,
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
    "points": 438490,
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
    "points": 420835,
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
    "points": 419064,
    "published_at": "2026-07-28T06:41:31+00:00",
    "summary": "如果能把 Codex、Claude Code、Grok、Cursor 等智能编程工具整合到同一个工作环境中，再让多个 Agent 像团队成员一样分工协作，软件开发的效率将得到显著提升。Orca ADE 正是为此而生：它是一款开源、免费的 Agent 开发环境，专注于代码管理与命令行工作流，不仅能够接入多种编程 Agent，还支持语音操作和手机远程管理。接下来，我们就来认识一下 Orca ADE，看"
  },
  {
    "id": "bvid:BV1eK5DzHEWu",
    "domain": "AI",
    "title": "MCP实战指南，mcp视频教程，2小时学透mcp",
    "url": "http://www.bilibili.com/video/av114380213586544",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 399195,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1vG8QzcE5X",
    "domain": "AI",
    "title": "Claude使用指南，claude code零基础教程，claude code安装配置到实战",
    "url": "http://www.bilibili.com/video/av114933744272468",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 352311,
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
    "points": 269164,
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
    "points": 245153,
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
    "points": 242312,
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
    "points": 179503,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV16Luq6FEmP",
    "domain": "AI",
    "title": "当不懂代码的老婆，第一次接触vibe coding……",
    "url": "http://www.bilibili.com/video/av117076211536327",
    "source": "糖果果的未来要发光",
    "platform": "bilibili",
    "points": 173551,
    "published_at": "2026-08-11T09:50:27+00:00",
    "summary": "当不懂代码的老婆，第一次接触vibe coding……"
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 163955,
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
    "points": 161128,
    "published_at": "2026-03-01T15:14:36+00:00",
    "summary": "1、认识Vibe Coding\n2、入门指南（零基础能学吗？学完后能做什么？）\n3、工具与实践（推荐工具&amp;动手写一个移动端网站）\n4、实操微调（修改页面中图片和文字，有点进阶）\n5、部署云端，让别人看到你的作品"
  },
  {
    "id": "bvid:BV1eYPpeWEnT",
    "domain": "AI",
    "title": "Cursor + MCP = 王炸！彻底颠覆我的Cursor工作流，效率直接起飞",
    "url": "http://www.bilibili.com/video/av114073660301264",
    "source": "御风大世界",
    "platform": "bilibili",
    "points": 151024,
    "published_at": "2025-02-27T03:19:03+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 137868,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 137452,
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
    "points": 99809,
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
    "points": 93287,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV1GRKJ6fEgn",
    "domain": "AI",
    "title": "Kimi K3编程能力炸裂！在Claude Code中全方位实测代码能力，能否超越Fable 5和GPT-5.6l？结果远超我的预期！国产模型跻身世界第一梯队！",
    "url": "http://www.bilibili.com/video/av116934511239163",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 91580,
    "published_at": "2026-07-17T09:10:43+00:00",
    "summary": "视频简介：\n\n月之暗面最新发布的 Kimi K3，拥有2.8万亿参数和100万 Token 上下文窗口，它的真实编程能力究竟怎么样？\n\n本期视频将对 Kimi K3 进行一次完整的高难度编程实测。我们先在官方网页版测试 SVG 手绘灯泡、复杂过河动画、南宋古都轻功游戏和土星自行车比赛，再将 Kimi K3 接入 Claude Code，开发原生 macOS 音乐播放器、侏罗纪坦克射击游戏以及 iO"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 89501,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1xBrDB9E42",
    "domain": "AI",
    "title": "独立开发太累？Godot + Claude Code 搭建 AI 辅助工作流，效率直接起飞！ | 地块召唤师开发实战 #01",
    "url": "http://www.bilibili.com/video/av115911319100158",
    "source": "像素夹心饼干",
    "platform": "bilibili",
    "points": 68819,
    "published_at": "2026-01-18T03:25:00+00:00",
    "summary": "大家好，这里是饼干！🍪\n这是我的新坑——**《地块召唤师》**开发实战分享的第一期。\n很多朋友问独立开发如何提升效率？这期视频我不聊虚的，直接公开我从 0 到 1 搭建的 AI + Godot 高效工作流。\n从游戏引擎的选择，到 Claude Code、Copilot 等 AI 工具的实战配置，再到如何用“明确需求”的方法论（SMART原则+双钻模型）来驾驭 AI，让它不仅仅是写代码的工具，更成为"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 63559,
    "published_at": "2026-03-30T16:47:51+00:00",
    "summary": "Everything Claude Code 是目前 GitHub 上 116K star 的 Claude Code 配置项目。本期从斜杠命令、子代理、Hooks 到学习系统，带你把这个项目真正用起来。"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54248,
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
    "points": 47633,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1W2Ts6YEXW",
    "domain": "AI",
    "title": "AI大模型+网络安全零基础入门全套教程：从Agent选型到AI挖洞全流程！AI挖洞提示词|AI解CTF题|AI审计代码|SRC挖洞|CS渗透|kali-码士集团",
    "url": "http://www.bilibili.com/video/av116854601286698",
    "source": "马士兵老师",
    "platform": "bilibili",
    "points": 45112,
    "published_at": "2026-07-03T06:28:48+00:00",
    "summary": "迈入AI赋能的网络安全新时代！\n\n本课程带你打通大模型与安全实战的底层逻辑。从大模型演进到安全智能体（Agent）构建，硬核实战拉满！手把手教你利用大模型API自动化搞定信息收集、黑盒挖洞、代码审计、解CTF题目及报告编写。深度破解AI挖洞的高效提示词秘籍，攻克复杂场景下的Agent架构与成本选型。\n\n2026安全防线全面升级，带你用AI武装自己，成为驾驭大模型的稀缺AI安全专家！"
  },
  {
    "id": "bvid:BV1ZD5ezjEGZ",
    "domain": "AI",
    "title": "3步将 DeepSeek 接入Cursor，免费无限制使用 AI编程",
    "url": "http://www.bilibili.com/video/av114351574879067",
    "source": "狠活AI科技",
    "platform": "bilibili",
    "points": 40798,
    "published_at": "2025-04-17T05:15:27+00:00",
    "summary": "3步将DeepSeek接入Cursor，免费无限制使用Composer Agent、代码补全等AI编程功能，无需魔法无需订阅速度飞快，DeepSeek-V3-0324效果媲美Pro版会员， 还有Claude 3.7、Gemini 2.5 Pro 等顶级模型"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34144,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1AGRtBnE3S",
    "domain": "AI",
    "title": "别手动写测试用例了!2026最新Claude Code+Skills实现需求文档生成全量用例|全流程AI驱动软件测试落地方案,测试效率翻10倍！",
    "url": "http://www.bilibili.com/video/av116528787756865",
    "source": "清风说测试开发",
    "platform": "bilibili",
    "points": 32235,
    "published_at": "2026-05-07T00:00:00+00:00",
    "summary": "全栈课一共分为6大块内容\n第一块：AI智能体开发基础(AI大模型、工具、记忆、MCP、中间件、Skills等核心内容)\n第二块：Claude Code,Trea+skills实现基于需求文档生成用例，基于OpenClaw实现接口自动化落地，基于hermes Agent实现web自动化落地\n第三块：功能测试的智能体开发(项目RAG知识库搭建+Agent搭建+skills开发，实现用例生成的Agent"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29640,
    "published_at": "2025-07-16T13:10:54+00:00",
    "summary": "Cursor用不了？三款AI编程工具完美代替Cursor\naugmentCode\nTrae\nKiro"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 27736,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1ZRbe6eENh",
    "domain": "AI",
    "title": "DeepSeek Harness安装和使用教程【最新完整版】零基础小白速通deepseek harness入门教程怎么下载插件如何安装如何使用全搞定！",
    "url": "http://www.bilibili.com/video/av117110286062691",
    "source": "鹏哥C语言",
    "platform": "bilibili",
    "points": 26859,
    "published_at": "2026-08-17T10:10:51+00:00",
    "summary": "欢迎大家来到鹏哥课堂！这份DeepSeek Harness教程专为零基础小白打造，全程手把手演示安装、启动Web界面、模型接入、基础任务实操。 很多小白卡在环境配置、命令报错、参数设置，本教程能让你避开各种坑，跟着操作就能成功运行。 搞懂 Agent = 模型 + Harness，让 AI 读写文件、执行命令、自主完成项目任务。本教程适合程序员、AI 爱好者及想上手本地智能体的同学等。希望大家把视"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22722,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1aQMX6oEni",
    "domain": "AI",
    "title": "【Agent面经】目前B站最细的（AI Agent）高频面试八股文，吊打付费，帮你避开99%面试坑！存下吧，很难找全的！",
    "url": "http://www.bilibili.com/video/av117030678239428",
    "source": "Agent开发实战",
    "platform": "bilibili",
    "points": 20829,
    "published_at": "2026-08-03T08:50:19+00:00",
    "summary": "【Agent面试100问】目前B站最细的（AI Agent）高频面试八股文，吊打付费，帮你避开99%面试坑！存下吧，很难找全的！"
  },
  {
    "id": "bvid:BV1zjd3BiEzo",
    "domain": "AI",
    "title": "别再二选一：Claude Code + Codex 联用才是最强姿势",
    "url": "http://www.bilibili.com/video/av116537746791000",
    "source": "星小脉",
    "platform": "bilibili",
    "points": 20360,
    "published_at": "2026-05-08T07:34:23+00:00",
    "summary": "Codex 已悄然追上 Claude Code，GPT 5.5 比肩 Opus 4.7、OpenAI Pro 额度更大方。但作者 Chase 想说：别再纠结谁更好，最佳姿势是把两者一起用——Codex 桌面应用直接跑 Claude Code 终端，让两个模型互查方案、互查代码（一次实测 Claude Code 帮 Codex 抓出 20 个 bug）。背后更重要的思路是 tool agnostic"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 19716,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "hn:49255710",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Risky Business",
    "url": "https://stratechery.com/2026/nvidias-risky-business/",
    "source": "jonbaer",
    "platform": "hackernews",
    "points": 356,
    "published_at": "2026-08-11T10:02:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:49323686",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia dramatically reduces amount of OpenAI infra financing it may guarantee",
    "url": "https://www.reuters.com/business/nvidia-scales-back-250-billion-openai-data-center-guarantee-wsj-reports-2026-08-14/",
    "source": "root-parent",
    "platform": "hackernews",
    "points": 249,
    "published_at": "2026-08-16T21:07:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:49263340",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Lightning and NeMo Switchyard",
    "url": "https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/",
    "source": "droidjj",
    "platform": "hackernews",
    "points": 262,
    "published_at": "2026-08-11T19:35:52+00:00",
    "summary": ""
  },
  {
    "id": "hn:49257947",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Nemotron 3.5 Lightning",
    "url": "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4",
    "source": "beklein",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-08-11T13:26:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:49342314",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discloses $21B stake in SpaceX",
    "url": "https://arstechnica.com/information-technology/2026/08/nvidia-discloses-21b-stake-in-spacex/",
    "source": "joozio",
    "platform": "hackernews",
    "points": 30,
    "published_at": "2026-08-18T07:02:04+00:00",
    "summary": ""
  },
  {
    "id": "hn:49322519",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia discloses $21B stake in SpaceX at end of second quarter",
    "url": "https://www.cnbc.com/2026/08/14/nvidia-discloses-21-billion-stake-in-spacex-at-end-of-second-quarter.html",
    "source": "johnbarron",
    "platform": "hackernews",
    "points": 47,
    "published_at": "2026-08-16T18:40:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49346906",
    "domain": "AI 算力 / 半导体",
    "title": "Ask HN: Do you feel comfortable admitting that you use AI?",
    "url": "https://news.ycombinator.com/item?id=49346906",
    "source": "var0xyz",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-18T15:16:15+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/andes-condor-closure-came-amid-broader-cost-cutting-effort/",
    "domain": "AI 算力 / 半导体",
    "title": "Andes Condor Closure Came Amid Broader Cost-Cutting Effort",
    "url": "https://www.eetimes.com/andes-condor-closure-came-amid-broader-cost-cutting-effort/",
    "source": "Nitin Dahad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T22:00:00+00:00",
    "summary": "Andes Technology’s decision to close Condor was part of a broader 10-20% operational cost-cutting exercise, with Condor probably considered too expensive a bet. The post Andes Condor Closure Came Amid"
  },
  {
    "id": "rss:https://www.eetimes.com/ibm-makes-quantum-cryogenics-modular-but-scaling-problems-remain/",
    "domain": "AI 算力 / 半导体",
    "title": "IBM Makes Quantum Cryogenics Modular, but Scaling Problems Remain",
    "url": "https://www.eetimes.com/ibm-makes-quantum-cryogenics-modular-but-scaling-problems-remain/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T13:55:51+00:00",
    "summary": "IBM’s new cryogenic architecture tackles one obstacle to fault-tolerant quantum computing, while exposing wiring, control, interconnect, and reliability challenges. The post IBM Makes Quantum Cryogeni"
  },
  {
    "id": "rss:https://www.eetimes.com/running-local-llms-on-the-arduino-uno-q-board-a-practical-guide/",
    "domain": "AI 算力 / 半导体",
    "title": "Running Local LLMs on the Arduino® UNO™ Q Board: a Practical Guide",
    "url": "https://www.eetimes.com/running-local-llms-on-the-arduino-uno-q-board-a-practical-guide/",
    "source": "Arduino Team",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T13:00:00+00:00",
    "summary": "Learn how to run local LLMs on Arduino UNO Q — from model selection and quantization to memory constraints and real-world edge AI use cases. The post Running Local LLMs on the Arduino® UNO™ Q Board: a"
  },
  {
    "id": "rss:https://www.eetimes.com/when-interoperability-becomes-infrastructure/",
    "domain": "AI 算力 / 半导体",
    "title": "When Interoperability Becomes Infrastructure",
    "url": "https://www.eetimes.com/when-interoperability-becomes-infrastructure/",
    "source": "Peter Hunt",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T07:43:30+00:00",
    "summary": "As Matter matures, manufacturers face a new challenge: maintaining visibility into connected products after deployment. The post When Interoperability Becomes Infrastructure appeared first on EE Times"
  },
  {
    "id": "rss:https://www.eetimes.com/marvell-targets-ai-bottlenecks-with-memory-disaggregation-portfolio/",
    "domain": "AI 算力 / 半导体",
    "title": "Marvell Targets AI Bottlenecks with Memory-Disaggregation Portfolio",
    "url": "https://www.eetimes.com/marvell-targets-ai-bottlenecks-with-memory-disaggregation-portfolio/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T14:39:27+00:00",
    "summary": "Marvell attacks AI’s memory choke point with SSD, CXL, and photonic fabrics to push data nearer compute. The post Marvell Targets AI Bottlenecks with Memory-Disaggregation Portfolio appeared first on "
  },
  {
    "id": "rss:https://www.eetimes.com/why-standardized-interfaces-are-critical-to-accelerating-humanoid-development/",
    "domain": "AI 算力 / 半导体",
    "title": "Why Standardized Interfaces Are Critical to Accelerating Humanoid Development",
    "url": "https://www.eetimes.com/why-standardized-interfaces-are-critical-to-accelerating-humanoid-development/",
    "source": "Edo Cohen",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T08:15:00+00:00",
    "summary": "Humanoids won’t scale on AI hype alone; standardized MIPI interfaces can cut power, wiring, and cost. The post Why Standardized Interfaces Are Critical to Accelerating Humanoid Development appeared fi"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/samsung-raises-advanced-foundry-prices-by-up-to-15-percent-as-ai-demand-fills-its-4nm-lines",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung raises advanced foundry prices by up to 15% as AI demand fills its 4nm lines, report claims — Chinese customers accepting the largest hikes",
    "url": "https://www.tomshardware.com/tech-industry/samsung-raises-advanced-foundry-prices-by-up-to-15-percent-as-ai-demand-fills-its-4nm-lines",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T16:15:53+00:00",
    "summary": "Samsung raised prices on new orders across its 4nm, 5nm, and 8nm foundry processes in July, with increases reaching 15% for customers in China."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/china-shifting-massive-ai-data-center-complexes-to-rural-provinces-to-tap-surplus-energy-eastern-data-western-computing-strategy-has-chinese-tech-giants-huawei-and-tencent-building-ai-infrastructure-guizhou",
    "domain": "AI 算力 / 半导体",
    "title": "China shifting massive AI data center complexes to rural provinces to tap surplus energy — ‘Eastern Data, Western Computing’ strategy has Chinese tech giants Huawei and Tencent building AI infrastruct",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/china-shifting-massive-ai-data-center-complexes-to-rural-provinces-to-tap-surplus-energy-eastern-data-western-computing-strategy-has-chinese-tech-giants-huawei-and-tencent-building-ai-infrastructure-guizhou",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T15:49:04+00:00",
    "summary": "Chinese tech giants are putting up data centers in rural Chinese provinces with zero resistance. The abundance of land and energy in these areas allowed infrastructure to easily be built with limited "
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/qualcomm-retracts-select-snapdragon-c-power-efficiency-benchmarks-nearly-a-week-after-publication-updated-slide-removes-idle-apps-and-web-browsing-results",
    "domain": "AI 算力 / 半导体",
    "title": "Qualcomm retracts select Snapdragon C power efficiency benchmarks nearly a week after publication — updated slide removes idle apps and web browsing results",
    "url": "https://www.tomshardware.com/laptops/qualcomm-retracts-select-snapdragon-c-power-efficiency-benchmarks-nearly-a-week-after-publication-updated-slide-removes-idle-apps-and-web-browsing-results",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T15:28:06+00:00",
    "summary": "Qualcomm has issued an updated slide for its Snapdragon C power efficiency claims, removing two benchmarks from the results."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/overclocking/you-can-now-buy-a-delidded-ryzen-9-9950x3d2-dual-edition-for-usd1-403-stripped-dual-cache-offering-is-usd500-more-expensive-than-regular-version",
    "domain": "AI 算力 / 半导体",
    "title": "You can now buy a delidded Ryzen 9 9950X3D2 Dual Edition for $1,403 — stripped dual-cache offering is $500 more expensive than regular version",
    "url": "https://www.tomshardware.com/pc-components/overclocking/you-can-now-buy-a-delidded-ryzen-9-9950x3d2-dual-edition-for-usd1-403-stripped-dual-cache-offering-is-usd500-more-expensive-than-regular-version",
    "source": "Zak Killian",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T13:44:47+00:00",
    "summary": "Thermal Grizzly offers the halo CPU with the pop topped for an egregious price, yet it almost makes sense on this chip."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/hacker-leaks-gta-vi-gameplay-and-map-to-protest-digital-only-release-claims-pre-orders-are-a-legacy-of-physical-game-releases",
    "domain": "AI 算力 / 半导体",
    "title": "Hacker leaks GTA VI gameplay and map to protest digital-only release — claims pre-orders are a legacy of physical game releases",
    "url": "https://www.tomshardware.com/video-games/hacker-leaks-gta-vi-gameplay-and-map-to-protest-digital-only-release-claims-pre-orders-are-a-legacy-of-physical-game-releases",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T13:37:23+00:00",
    "summary": "Hacker Cyberleek leaked gameplay clips and the entire map of GTA VI in protest of Rockstar's decision to launch pre-orders of a digital game. They claim that pre-orders were created because physical d"
  },
  {
    "id": "rss:https://www.tomshardware.com/phones/google-to-stop-making-pixel-devices-in-china-report-claims-india-and-vietnam-prime-candidates-for-manufacturing-shift-owing-to-beijing-washington-tensions",
    "domain": "AI 算力 / 半导体",
    "title": "Google to stop making Pixel devices in China, report claims — India and Vietnam prime candidates for manufacturing shift owing to Beijing-Washington tensions",
    "url": "https://www.tomshardware.com/phones/google-to-stop-making-pixel-devices-in-china-report-claims-india-and-vietnam-prime-candidates-for-manufacturing-shift-owing-to-beijing-washington-tensions",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T12:40:00+00:00",
    "summary": "To reduce reliance on China, Google plans to relocate production of Pixel smartphones, smartwatches, and headsets from China to India and Vietnam."
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/comcast-turns-xfinity-routers-into-home-motion-detectors-free-wi-fi-sensing-feature-tracks-rf-interference-with-zero-extra-hardware-required",
    "domain": "AI 算力 / 半导体",
    "title": "Comcast turns Xfinity routers into home motion detectors — free Wi-Fi sensing feature tracks RF interference with zero extra hardware required",
    "url": "https://www.tomshardware.com/networking/routers/comcast-turns-xfinity-routers-into-home-motion-detectors-free-wi-fi-sensing-feature-tracks-rf-interference-with-zero-extra-hardware-required",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T12:20:00+00:00",
    "summary": "To appease concerns about privacy, Wi-Fi Motion is opt-in"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/samsungs-fab-roadmap-examined",
    "domain": "AI 算力 / 半导体",
    "title": "Samsung's fab roadmaps examined — Taylor, Pyeongtaek, and the yield woes behind a $16.5 billion Tesla deal",
    "url": "https://www.tomshardware.com/tech-industry/samsungs-fab-roadmap-examined",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T12:00:00+00:00",
    "summary": "Divided across two countries and four campuses, Samsung's fab roadmap runs from the Korean bases at Pyeongtaek, Hwaseong, and Giheung to the new U.S. site at Taylor."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/jason-kelce-led-marketing-campaign-asks-beer-drinkers-to-send-their-pee-to-ai-data-centers-liquid-death-and-garage-beer-skit-claims-ai-data-centers-waste-millions-of-gallons-of-water",
    "domain": "AI 算力 / 半导体",
    "title": "Jason Kelce-led marketing campaign asks beer drinkers to send their pee to AI data centers — Liquid Death and Garage Beer skit claims 'AI data centers waste millions of gallons of water'",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/jason-kelce-led-marketing-campaign-asks-beer-drinkers-to-send-their-pee-to-ai-data-centers-liquid-death-and-garage-beer-skit-claims-ai-data-centers-waste-millions-of-gallons-of-water",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T11:55:24+00:00",
    "summary": "Two indie brands join together in a viral ad campaign asking people to pee on computers. Taylor Swift's brother-in-law, Jason Kelce, who co-owns one of the brands, stars in this humorous ad where he p"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/beijing-ai-bar-pours-pints-of-foam-with-free-deepseek-tokens-served-from-two-nvidia-dgx-sparks",
    "domain": "AI 算力 / 半导体",
    "title": "Beijing AI bar that offers unlimited free DeepSeek coding tokens with $1.50 drink haemorrhaging cash — 'the bar is completely losing money, ' owner admits",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/beijing-ai-bar-pours-pints-of-foam-with-free-deepseek-tokens-served-from-two-nvidia-dgx-sparks",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T11:44:32+00:00",
    "summary": "An AI-themed bar in Beijing's Zhongguancun tech hub hands out free, unlimited DeepSeek tokens with its drinks, running inference locally on two Nvidia DGX Spark mini-PCs."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/ajinomoto-reportedly-cuts-abf-chip-packaging-film-supply-to-china-by-30-percent",
    "domain": "AI 算力 / 半导体",
    "title": "Ajinomoto reportedly cuts critical chip packaging film supply to China by 30% as domestic substitutes race to qualify — ABF restriction comes following Beijing's rare earth export curbs",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/ajinomoto-reportedly-cuts-abf-chip-packaging-film-supply-to-china-by-30-percent",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T11:40:00+00:00",
    "summary": "Japanese chemical maker Ajinomoto has reportedly told customers in mainland China that it will cut the supply of ABF."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/snag-amds-ryzen-7-7700x3d-with-16gb-of-ram-motherboard-and-a-cooler-for-just-usd609-save-usd124-on-a-b650-atx-board-and-corsair-vengeance-ram-for-a-new-gaming-build",
    "domain": "AI 算力 / 半导体",
    "title": "Snag AMD’s Ryzen 7 7700X3D with 16GB of RAM, motherboard, and a cooler for just $609 — save $124 on a B650 ATX board and Corsair Vengeance RAM for a new gaming build",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/snag-amds-ryzen-7-7700x3d-with-16gb-of-ram-motherboard-and-a-cooler-for-just-usd609-save-usd124-on-a-b650-atx-board-and-corsair-vengeance-ram-for-a-new-gaming-build",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T11:36:03+00:00",
    "summary": "Newegg's combo deal pairs the gaming-centric Ryzen 7 7700X3D, Asus ROG Strix B650-A motherboard, and Corsair Vengeance DDR5 RAM for $609.99, plus a free 240mm AIO—an affordable way into AM5 amid the R"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/microsd-cards/microsd-card-testing-database-celebrates-third-anniversary-with-133-petabytes-of-data-written-across-4-6-million-cycles-hundreds-of-cards-tested-to-failure-reveal-sandisk-as-the-outlier-with-6-failures-of-the-7-tested",
    "domain": "AI 算力 / 半导体",
    "title": "MicroSD card torture test writes 133 petabytes of data across 351 cards over three years — cards tested to failure reveal SanDisk as the outlier with 6 failures of the 7 tested",
    "url": "https://www.tomshardware.com/pc-components/microsd-cards/microsd-card-testing-database-celebrates-third-anniversary-with-133-petabytes-of-data-written-across-4-6-million-cycles-hundreds-of-cards-tested-to-failure-reveal-sandisk-as-the-outlier-with-6-failures-of-the-7-tested",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T11:20:00+00:00",
    "summary": "Matt Cole has been running hundreds of microSD cards through their paces, running them through thousands of cycles until they fail. The results are quite surprising, with both the winners and losers c"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/asrock-x870e-taichi-white-motherboard-review",
    "domain": "AI 算力 / 半导体",
    "title": "ASRock X870E Taichi White Motherboard Review: A Taichi washed in white, now with 10 GbE",
    "url": "https://www.tomshardware.com/pc-components/motherboards/asrock-x870e-taichi-white-motherboard-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T11:15:00+00:00",
    "summary": "The ASRock X870E Taichi White updates the original with a cleaner all-white design and 10 GbE, and is the first ASRock board to feature all-white components. But pricing could scare away some users."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/taiwan-to-pay-every-resident-314-from-its-ai-boom-windfall",
    "domain": "AI 算力 / 半导体",
    "title": "AI server boom funds $314 universal cash payout in Taiwan — President Lai Ching-te says the payout ensures the country's AI windfall 'can be shared by all,' 11% GDP growth and $903B export surge finan",
    "url": "https://www.tomshardware.com/tech-industry/taiwan-to-pay-every-resident-314-from-its-ai-boom-windfall",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T11:00:00+00:00",
    "summary": "Taiwan will hand roughly $314 USD in cash to every resident next year as a boon for the island's residents generated by the AI gold rush. The 2027 central government budget sets aside $7.4 billion USD"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/first-nvidia-h200-shipments-reach-bytedance-and-tencent-as-beijing-loosens-its-import-block",
    "domain": "AI 算力 / 半导体",
    "title": "First Nvidia H200 shipments reach China, ByteDance and Tencent take deliveries as Beijing loosens its import block — most licensed chips must stay in Hong Kong, which can't power them",
    "url": "https://www.tomshardware.com/pc-components/gpus/first-nvidia-h200-shipments-reach-bytedance-and-tencent-as-beijing-loosens-its-import-block",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T10:37:13+00:00",
    "summary": "Beijing wants most of each company's U.S.-licensed allowance, which the FT puts at up to 100,000 units apiece, kept off the mainland."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/usd10-quake-shareware-cd-locked-copies-of-all-id-software-games-behind-a-flawed-encryption-scheme-pay-over-the-phone-system-only-held-up-for-39-days-after-1996-release-leaving-developer-with-150-000-discs-it-couldnt-sell",
    "domain": "AI 算力 / 半导体",
    "title": "$10 Quake shareware CD locked copies of all id Software games behind a flawed encryption scheme — pay-over-the-phone system only held up for 39 days after 1996 release, leaving developer with 150,000 ",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/usd10-quake-shareware-cd-locked-copies-of-all-id-software-games-behind-a-flawed-encryption-scheme-pay-over-the-phone-system-only-held-up-for-39-days-after-1996-release-leaving-developer-with-150-000-discs-it-couldnt-sell",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T10:30:00+00:00",
    "summary": "id Software included locked versions of its entire game library on the $10 Quake shareware CD it released in 1996. But the system meant to allow gamers to pay for and unlock those titles over the phon"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/cut-the-stress-out-of-pc-building-with-this-usd500-discount-on-this-rx-9060-xt-16gb-desktop-intel-core-ultra-9-285-build-also-features-32gb-of-ddr5-2tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Cut the stress out of PC building with this $500 discount on this RX 9060 XT 16GB desktop — Intel Core Ultra 9 285 build also features 32GB of DDR5, 2TB SSD",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/cut-the-stress-out-of-pc-building-with-this-usd500-discount-on-this-rx-9060-xt-16gb-desktop-intel-core-ultra-9-285-build-also-features-32gb-of-ddr5-2tb-ssd",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T10:18:31+00:00",
    "summary": "Get an Intel Core Ultra 9 285 PC with an RX 9060 XT 16GB GPU for just $1,849."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/dev-uses-claude-ai-to-create-native-macos-driver-for-obscure-windows-only-printer-linux-container-hack-enables-system-wide-cmd-p-printing-driver-now-available-on-github",
    "domain": "AI 算力 / 半导体",
    "title": "Dev uses Claude AI to create native macOS driver for 'obscure' Windows-only printer — Linux container hack enables system-wide Cmd-P printing, driver now available on Github",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/dev-uses-claude-ai-to-create-native-macos-driver-for-obscure-windows-only-printer-linux-container-hack-enables-system-wide-cmd-p-printing-driver-now-available-on-github",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T10:00:00+00:00",
    "summary": "A developer has revealed that they used Claude Code to create a macOS laser printer driver for the HP Laser 1008a, a machine designed for Windows users."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/minecraft-creator-works-around-in-game-math-limitations-to-implement-an-llm-using-445k-command-blocks-clever-approach-shrank-initial-block-count-from-over-1-million-requires-no-mods-plugins-or-datapacks-to-work",
    "domain": "AI 算力 / 半导体",
    "title": "Player builds working AI chatbot in vanilla Minecraft using 445K command blocks — clever approach shrank initial block count from over 1 million, requires no mods, plugins, or datapacks to work",
    "url": "https://www.tomshardware.com/video-games/minecraft-creator-works-around-in-game-math-limitations-to-implement-an-llm-using-445k-command-blocks-clever-approach-shrank-initial-block-count-from-over-1-million-requires-no-mods-plugins-or-datapacks-to-work",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T09:30:00+00:00",
    "summary": "Building neural networks in Minecraft using redstone is a relatively common pursuit, but a clever creator has worked around the limitations of command blocks' available math operations to implement an"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/white-house-cuts-data-centers-batteries-and-ar-from-the-us-critical-technology-list",
    "domain": "AI 算力 / 半导体",
    "title": "White House cuts data centers, batteries, and AR from the US critical technology list — post-quantum cryptography, integrated photonics, high entropy alloys among new additions",
    "url": "https://www.tomshardware.com/tech-industry/white-house-cuts-data-centers-batteries-and-ar-from-the-us-critical-technology-list",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T09:24:59+00:00",
    "summary": "Appendix A of the 24-page document rewrites the federal Critical and Emerging Technologies list for the first time since February 2024."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/github-programmer-ports-doom-to-dslr-camera-with-3-inch-tft-lcd-display-canon-eos-550d-with-open-source-magic-lantern-firmware-uses-cameras-button-as-controls-even-plays-sound",
    "domain": "AI 算力 / 半导体",
    "title": "GitHub programmer ports playable Doom to DSLR camera with 3-inch TFT LCD display — Canon EOS 550D with open-source Magic Lantern firmware uses camera's button as controls, even plays sound",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/github-programmer-ports-doom-to-dslr-camera-with-3-inch-tft-lcd-display-canon-eos-550d-with-open-source-magic-lantern-firmware-uses-cameras-button-as-controls-even-plays-sound",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T09:00:00+00:00",
    "summary": "A developer posted their Doom port for the Canon EOS 550D on GitHub. The game uses the Magic Lantern firmware add-on to run on the camera, and uses various camera buttons to play the game directly fro"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/appeals-court-orders-fresh-review-of-djis-chinese-military-company-designation",
    "domain": "AI 算力 / 半导体",
    "title": "DJI scores a win in fight against US ban, appeals court orders fresh review of firm's 'Chinese military company' designation — drone maker will stay on Pentagon list while a judge examines classified ",
    "url": "https://www.tomshardware.com/tech-industry/appeals-court-orders-fresh-review-of-djis-chinese-military-company-designation",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T15:40:10+00:00",
    "summary": "The DC Circuit reversed one of four findings, ruling that a lower court upheld a fully redacted justification without reading the classified record behind it."
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/start-your-3d-printing-journey-with-bambu-labs-awesome-p1s-printer-and-ams-color-printing-module-bundle-for-the-all-time-low-price-of-usd499-in-best-buys-60th-anniversary-sale",
    "domain": "AI 算力 / 半导体",
    "title": "Start your 3D printing journey with Bambu Labs' awesome P1S printer and AMS color-printing module bundle for the all-time low price of $499 in Best Buy's 60th Anniversary Sale",
    "url": "https://www.tomshardware.com/3d-printing/start-your-3d-printing-journey-with-bambu-labs-awesome-p1s-printer-and-ams-color-printing-module-bundle-for-the-all-time-low-price-of-usd499-in-best-buys-60th-anniversary-sale",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T15:31:40+00:00",
    "summary": "Step into 3D printing with Bambu Lab's P1S and AMS combo bundle for $499. Back on sale at its lowest-ever price point."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intels-next-gen-nova-lake-chips-may-skip-bllc-for-mobile-skus-and-debut-on-razor-lake-hx-instead-leaker-claims-new-rumor-says-razor-lake-family-reportedly-uses-tsmcs-n2x-node",
    "domain": "AI 算力 / 半导体",
    "title": "Intel's next-gen Nova Lake chips may skip game-boosting X3D cache rival for mobile SKUs and debut on Razor Lake-HX instead, leaker claims — new rumor says Razor Lake family reportedly uses TSMC's N2X ",
    "url": "https://www.tomshardware.com/pc-components/cpus/intels-next-gen-nova-lake-chips-may-skip-bllc-for-mobile-skus-and-debut-on-razor-lake-hx-instead-leaker-claims-new-rumor-says-razor-lake-family-reportedly-uses-tsmcs-n2x-node",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T14:18:57+00:00",
    "summary": "Nova Lake desktop CPUs look to be the exclusive recipient of bLLC, Intel's answer to AMD's X3D, as the company looks to debut bLLC on mobile with Razor Lake-HX, and possibly Razor Lake-AX. As such, th"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-claims-its-2026-rack-scale-ai-solution-is-4x-more-energy-efficient-than-its-2024-ai-platform-company-says-its-pacing-ahead-of-20x-efficiency-by-2030",
    "domain": "AI 算力 / 半导体",
    "title": "AMD claims its 2026 rack-scale AI solution is 4X more energy efficient than its 2024 AI platform — company says it's pacing ahead of 20X efficiency by 2030",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-claims-its-2026-rack-scale-ai-solution-is-4x-more-energy-efficient-than-its-2024-ai-platform-company-says-its-pacing-ahead-of-20x-efficiency-by-2030",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T14:00:00+00:00",
    "summary": "AMD says its 2025 rack-scale AI system is 4X more energy efficient compared to its 2024 AI solution, though does not produce actual benchmark results."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/asus-rog-swift-pg32ucwm-32-inch-oled-gaming-monitor-review",
    "domain": "AI 算力 / 半导体",
    "title": "Asus ROG Swift PG32UCWM 32-inch OLED gaming monitor review: A flagship display with premium performance and imagery",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/asus-rog-swift-pg32ucwm-32-inch-oled-gaming-monitor-review",
    "source": "Christian Eberle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T13:00:00+00:00",
    "summary": "Asus delivers another flagship OLED with the ROG Swift PG32UCWM. It pulls out all the stops with a 32-inch Tandem RGB Stripe panel, 4K resolution, 240 Hz with 480 Hz/FHD dual mode, HDR10, Dolby Vision"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/adata-xpg-novakey-rgb-ddr5-6000-c30-2x16gb-review-turning-salvage-into-pure-performance",
    "domain": "AI 算力 / 半导体",
    "title": "Adata XPG Novakey RGB DDR5-6000 C30 2x16GB Review — Turning salvage into pure performance",
    "url": "https://www.tomshardware.com/pc-components/ram/adata-xpg-novakey-rgb-ddr5-6000-c30-2x16gb-review-turning-salvage-into-pure-performance",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T12:30:00+00:00",
    "summary": "Amid the memory crunch, Adata unleashes its new XPG Novakey RGB memory kit series. But can the new lineup convince consumers to pick it up?"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/how-to-choose-a-new-motherboard-without-overpaying-scoping-out-the-features-you-need-and-what-you-might-never-use-as-component-costs-soar",
    "domain": "AI 算力 / 半导体",
    "title": "How to choose a new motherboard without overpaying — scoping out the features you need, and what you might never use as component costs soar",
    "url": "https://www.tomshardware.com/pc-components/motherboards/how-to-choose-a-new-motherboard-without-overpaying-scoping-out-the-features-you-need-and-what-you-might-never-use-as-component-costs-soar",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T12:00:00+00:00",
    "summary": "How much motherboard is too much? We look at what you actually get as prices climb — from VRMs and connectivity to premium features and diminishing returns."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/famed-overclocker-1usmus-updates-hydra-overclocking-tool-with-up-to-3000-mhz-memory-offset-new-update-gives-vram-and-power-limit-controls-to-rtx-50-series-gpus",
    "domain": "AI 算力 / 半导体",
    "title": "Overclocker updates Hydra overclocking tool with VRAM and power limit controls for RTX 50-series GPUs — new update gives up to +3000 MHz memory offset",
    "url": "https://www.tomshardware.com/pc-components/gpus/famed-overclocker-1usmus-updates-hydra-overclocking-tool-with-up-to-3000-mhz-memory-offset-new-update-gives-vram-and-power-limit-controls-to-rtx-50-series-gpus",
    "source": "Aaron Klotz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T11:40:00+00:00",
    "summary": "Overclocker 1usmus has released a new update for their Hydra overclocking tool that features VRAM and power limit controls for RTX 50-series GPUs."
  },
  {
    "id": "hn:49325115",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC Uses Old Fabs to Make New Chips [video]",
    "url": "https://www.youtube.com/watch?v=cDxVYQrxeiQ",
    "source": "eig",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-08-17T00:07:42+00:00",
    "summary": ""
  },
  {
    "id": "hn:49282762",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia doubles RTX PRO 6000 Blackwell's MSRP to a staggering $16,000",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-doubles-rtx-pro-6000-blackwells-msrp-to-a-staggering-usd16-000-96gb-card-started-pre-orders-below-usd8-000-last-year",
    "source": "jacquesm",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-08-13T07:28:54+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/nvidia-bets-on-the-classical-side-of-quantum-computing/",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Bets on the Classical Side of Quantum Computing",
    "url": "https://www.eetimes.com/nvidia-bets-on-the-classical-side-of-quantum-computing/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T18:31:00+00:00",
    "summary": "Nvidia positions classical computing infrastructure as a critical layer in the race to build useful quantum computers. The post Nvidia Bets on the Classical Side of Quantum Computing appeared first on"
  },
  {
    "id": "rss:https://www.eetimes.com/tiny-esim-global-reach-simplifying-cellular-connectivity-for-consumer-electronics/",
    "domain": "AI 算力 / 半导体",
    "title": "Tiny eSIM, Global Reach: Simplifying Cellular Connectivity for Consumer Electronics",
    "url": "https://www.eetimes.com/tiny-esim-global-reach-simplifying-cellular-connectivity-for-consumer-electronics/",
    "source": "Infineon Technologies and Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T14:29:25+00:00",
    "summary": "Join this webinar and discover the OPTIGA™ Connect Consumer OC1230, the world's smallest, ultra-low-power eSIM solution built on Infineon's TEGRION™ 28 nm tech. The post Tiny eSIM, Global Reach: Simpl"
  },
  {
    "id": "rss:https://www.eetimes.com/automotive-functional-safety-why-asil-compliance-starts-with-electromagnetic-design/",
    "domain": "AI 算力 / 半导体",
    "title": "Automotive Functional Safety: Why ASIL Compliance Starts with Electromagnetic Design",
    "url": "https://www.eetimes.com/automotive-functional-safety-why-asil-compliance-starts-with-electromagnetic-design/",
    "source": "Cadence Design Systems",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T14:00:00+00:00",
    "summary": "Automotive electronic systems face relentless pressure to meet electromagnetic compatibility (EMC), signal integrity (SI), and power integrity (PI) targets while satisfying strict ASIL safety requirem"
  },
  {
    "id": "rss:https://www.eetimes.com/the-charging-inlet-has-become-a-system-rethinking-ev-charge-control-electronics/",
    "domain": "AI 算力 / 半导体",
    "title": "The Charging Inlet Has Become a System: Rethinking EV Charge-Control Electronics",
    "url": "https://www.eetimes.com/the-charging-inlet-has-become-a-system-rethinking-ev-charge-control-electronics/",
    "source": "Raphi Zadicario, Product Manager and Chief Architect, Lumissil Microsystems",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-17T12:00:00+00:00",
    "summary": "Explore how integrated charge-control architecture reduces complexity while supporting J3400, MCS, and global EV platforms. The post The Charging Inlet Has Become a System: Rethinking EV Charge-Contro"
  },
  {
    "id": "hn:49279812",
    "domain": "AI 算力 / 半导体",
    "title": "Why space is a terrible place to cool a data center",
    "url": "https://thenewstack.io/spacex-and-nvidias-orbital-ai-datacenter-fantasy/",
    "source": "CrankyBear",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-08-12T23:08:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:49289112",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.7 Flash",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/",
    "source": "thisisauserid",
    "platform": "hackernews",
    "points": 967,
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
    "points": 449,
    "published_at": "2026-08-08T09:18:50+00:00",
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
    "id": "hn:49067285",
    "domain": "大厂 AI 动态",
    "title": "Why I Left Google DeepMind",
    "url": "https://www.lesswrong.com/posts/iKm2FhpWkuuBojm82/why-i-left-google-deepmind",
    "source": "eatitraw",
    "platform": "hackernews",
    "points": 200,
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
    "points": 121,
    "published_at": "2026-08-06T16:05:51+00:00",
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
    "id": "hn:49355510",
    "domain": "大厂 AI 动态",
    "title": "Qwen3.8-27B make medium the default effort level instead of xhigh",
    "url": "https://github.com/alainnothere/llama.cpp/blob/disk-cache-eviction/models/templates/Qwen3.8-27B-medium-default.jinja",
    "source": "xlayn",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-08-19T01:44:38+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/981834/hoverair-versa-drone-camera-fcc-loophole-indiegogo",
    "domain": "大厂 AI 动态",
    "title": "Does giving a camera wings dodge the FCC’s drone ban?",
    "url": "https://www.theverge.com/tech/981834/hoverair-versa-drone-camera-fcc-loophole-indiegogo",
    "source": "Sean Hollister",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T22:35:20+00:00",
    "summary": "HoverAir drones always have intriguing gimmicks. This one folds flat to fit in your pocket. This one can land on water. Another can charge inside its carrying case. But the brand's latest trick might "
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/982358/nielsen-ratings-ppm-smart-watch-cowatching-big-data",
    "domain": "大厂 AI 动态",
    "title": "Nielsen is leaning more on wearables to hear what people are watching",
    "url": "https://www.theverge.com/entertainment/982358/nielsen-ratings-ppm-smart-watch-cowatching-big-data",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T19:53:09+00:00",
    "summary": "In order to beef up its ability to accurately measure viewership data in the streaming era, Nielsen is moving forward with a plan to use more information gathered from its partners' wearable devices. "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/982425/google-gemini-student-hub",
    "domain": "大厂 AI 动态",
    "title": "Google Gemini is getting a dedicated student hub",
    "url": "https://www.theverge.com/ai-artificial-intelligence/982425/google-gemini-student-hub",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T19:00:00+00:00",
    "summary": "As we're gearing up for back-to-school season, Google is rolling out a new dedicated student hub in Gemini. It's a one-stop repository for collecting research in a study notebook, creating flashcards,"
  },
  {
    "id": "rss:https://www.theverge.com/games/982406/valve-steam-frame-setup-unboxing-leaked-videos",
    "domain": "大厂 AI 动态",
    "title": "Watch Valve set up the Steam Frame in its own leaked videos",
    "url": "https://www.theverge.com/games/982406/valve-steam-frame-setup-unboxing-leaked-videos",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T18:16:27+00:00",
    "summary": "Valve just leaked several new videos showing the Steam Frame's unboxing, setup process, and various accessories. The videos apparently appeared on the ARM Steam client following an update, but they we"
  },
  {
    "id": "rss:https://www.theverge.com/column/982359/optimizer-wearable-future-google-ai",
    "domain": "大厂 AI 动态",
    "title": "The wearable future is stuck in weird, experimental, existential limbo",
    "url": "https://www.theverge.com/column/982359/optimizer-wearable-future-google-ai",
    "source": "Victoria Song",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T18:00:00+00:00",
    "summary": "This is Optimizer, a weekly newsletter sent from Verge senior reviewer Victoria Song that dissects and discusses the latest gizmos and potions that swear they're going to change your life. Opt in for "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/982242/ipad-air-m4-garmin-inreach-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Grab an iPad Air M4 for its lowest price since the June increase",
    "url": "https://www.theverge.com/gadgets/982242/ipad-air-m4-garmin-inreach-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T17:56:15+00:00",
    "summary": "Almost everything with high-end memory or storage is more expensive these days, and tablets are no exception, so we’re glad to see that Amazon and Best Buy have the most recent 11-inch iPad Air with t"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/982323/openai-hit-brakes-voluntary-pacing-ai",
    "domain": "大厂 AI 动态",
    "title": "OpenAI hit the brakes. Now what?",
    "url": "https://www.theverge.com/ai-artificial-intelligence/982323/openai-hit-brakes-voluntary-pacing-ai",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T17:10:09+00:00",
    "summary": "With a looming IPO, intense competition from Anthropic, and Chinese and open-weight rivals nipping at its heels, OpenAI has plenty of reasons to move fast. Instead, it hit the brakes. On Tuesday, the "
  },
  {
    "id": "rss:https://www.theverge.com/games/982338/grand-theft-auto-vi-gta-leaks-videos",
    "domain": "大厂 AI 动态",
    "title": "GTA VI keeps leaking ahead of its gameplay premiere",
    "url": "https://www.theverge.com/games/982338/grand-theft-auto-vi-gta-leaks-videos",
    "source": "Jay Peters",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T17:03:11+00:00",
    "summary": "Clips of what appears to be Grand Theft Auto VI have hit the internet, possibly spoiling aspects of the game ahead of Rockstar Games' deep dive debuting on Netflix next week and its long-awaited launc"
  },
  {
    "id": "rss:https://www.theverge.com/tech/982270/meta-ai-mac-app",
    "domain": "大厂 AI 动态",
    "title": "Meta AI is getting a Mac app",
    "url": "https://www.theverge.com/tech/982270/meta-ai-mac-app",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T17:00:00+00:00",
    "summary": "Meta is launching a new Mac app dedicated to its AI chatbot. In an announcement on Wednesday, Meta says you can share your window with its AI chatbot, which can provide suggestions, answer questions, "
  },
  {
    "id": "rss:https://www.theverge.com/tech/981537/pixel-11-pro-fold-watch-5-ama",
    "domain": "大厂 AI 动态",
    "title": "We reviewed the new Pixel lineup, ask us anything",
    "url": "https://www.theverge.com/tech/981537/pixel-11-pro-fold-watch-5-ama",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T16:15:00+00:00",
    "summary": "The embargo has lifted on Google's Pixel 11 series, as well as for its Pixel Watch 5. Now we get to talk smack - just kidding, the new hardware is good. We have four reviews live on the site that you "
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/stripe-didnt-really-buy-openrouter-because-of-the-singularity/",
    "domain": "大厂 AI 动态",
    "title": "Stripe didn’t really buy OpenRouter because of the ‘singularity’",
    "url": "https://techcrunch.com/2026/08/19/stripe-didnt-really-buy-openrouter-because-of-the-singularity/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T23:32:00+00:00",
    "summary": "What does a payments giant want with a startup that routes prompts between different AI models? Stripe says it's because of \"the singularity\" but it's really for a far more real and powerful reason."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/waymos-cheaper-next-gen-robotaxi-is-now-open-to-all-riders-in-these-three-cities/",
    "domain": "大厂 AI 动态",
    "title": "Waymo’s cheaper, next-gen robotaxi is now open to all riders in these three cities",
    "url": "https://techcrunch.com/2026/08/19/waymos-cheaper-next-gen-robotaxi-is-now-open-to-all-riders-in-these-three-cities/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T22:25:01+00:00",
    "summary": "The next-generation robotaxi, called the Waymo Ojai, is central to the company's push towards mass scale, and eventually, profitability."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/openai-seeks-to-one-up-anthropic-with-new-customer-privacy-protections/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI seeks to one-up Anthropic with new customer privacy protections",
    "url": "https://techcrunch.com/2026/08/19/openai-seeks-to-one-up-anthropic-with-new-customer-privacy-protections/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T22:10:46+00:00",
    "summary": "A competition is developing between OpenAI and Anthropic over who can provide the best privacy protections for enterprise customer data."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/cognition-ceo-denies-report-that-spacex-tried-to-acquire-the-startup/",
    "domain": "大厂 AI 动态",
    "title": "Cognition CEO denies report that SpaceX tried to acquire the startup",
    "url": "https://techcrunch.com/2026/08/19/cognition-ceo-denies-report-that-spacex-tried-to-acquire-the-startup/",
    "source": "Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T21:51:23+00:00",
    "summary": "SpaceX was reportedly in talks to buy AI coding startup Cognition. SpaceX has already acquired Cursor as it races to catch up to rivals like OpenAI and Anthropic in enterprise AI."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/travis-kalanick-kicks-off-another-round-of-vc-bashing-1-are-helpful/",
    "domain": "大厂 AI 动态",
    "title": "Travis Kalanick kicks off another round of VC bashing: ‘1% are helpful’",
    "url": "https://techcrunch.com/2026/08/19/travis-kalanick-kicks-off-another-round-of-vc-bashing-1-are-helpful/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T21:48:24+00:00",
    "summary": "After raising $1.7 billion for his new robotics company Atoms, Travis Kalanick is introspective about the role VCs have played in his career."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/rillet-raises-100m-series-c-at-1b-valuation-2-years-after-emerging-from-stealth/",
    "domain": "大厂 AI 动态",
    "title": "Rillet raises $100M Series C at $1B valuation — 2 years after emerging from stealth",
    "url": "https://techcrunch.com/2026/08/19/rillet-raises-100m-series-c-at-1b-valuation-2-years-after-emerging-from-stealth/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T20:12:33+00:00",
    "summary": "AI-native account startup Rillet became a unicorn, led by Iconiq, after it doubled its ARR in the past three months, it said."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/gwyneth-paltrow-allegedly-set-to-throw-dinner-in-honor-of-sam-altman/",
    "domain": "大厂 AI 动态",
    "title": "Gwyneth Paltrow allegedly set to throw dinner in honor of Sam Altman",
    "url": "https://techcrunch.com/2026/08/19/gwyneth-paltrow-allegedly-set-to-throw-dinner-in-honor-of-sam-altman/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T20:04:12+00:00",
    "summary": "The actress' firm Kinship Ventures is an investor in the company."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/gambling-on-the-little-league-world-series-sports-bettors-have-gone-too-far/",
    "domain": "大厂 AI 动态",
    "title": "Gambling on the Little League World Series? Sports bettors have gone too far",
    "url": "https://techcrunch.com/2026/08/19/gambling-on-the-little-league-world-series-sports-bettors-have-gone-too-far/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T20:01:02+00:00",
    "summary": "Have we tried turning off society and turning it back on again?"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/ai-was-supposed-to-win-people-over-by-now-it-hasnt/",
    "domain": "大厂 AI 动态",
    "title": "AI was supposed to win people over by now — it hasn’t",
    "url": "https://techcrunch.com/2026/08/19/ai-was-supposed-to-win-people-over-by-now-it-hasnt/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T19:11:40+00:00",
    "summary": "As AI becomes harder to avoid, consumers are growing more wary of the technology — and Silicon Valley is discovering that widespread adoption doesn’t necessarily lead to acceptance."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/google-launches-new-study-tools-for-students-across-search-and-gemini/",
    "domain": "大厂 AI 动态",
    "title": "Google packs Search and Gemini with new AI study tools",
    "url": "https://techcrunch.com/2026/08/19/google-launches-new-study-tools-for-students-across-search-and-gemini/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T19:00:00+00:00",
    "summary": "The launch of the new study features marks Google's latest effort to make Gemini the AI assistant that students turn to when learning and studying, as it continues to compete with companies like OpenA"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/researchers-complain-that-openai-revoked-their-access-to-limited-cyber-program/",
    "domain": "大厂 AI 动态",
    "title": "Researchers say OpenAI revoked their access to limited cyber program",
    "url": "https://techcrunch.com/2026/08/19/researchers-complain-that-openai-revoked-their-access-to-limited-cyber-program/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T18:46:14+00:00",
    "summary": "The idea behind OpenAI's Trusted Access for Cyber program is to give trusted defenders better models so they can report bugs and vulnerabilities to companies, with the aim of getting flaws patched fas"
  },
  {
    "id": "rss:https://techcrunch.com/video/meet-the-startup-helping-wall-street-put-a-price-on-ai-compute/",
    "domain": "大厂 AI 动态",
    "title": "Meet the startup helping Wall Street put a price on AI compute",
    "url": "https://techcrunch.com/video/meet-the-startup-helping-wall-street-put-a-price-on-ai-compute/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T17:26:48+00:00",
    "summary": "The AI buildout shows no signs of slowing. And&#160;with&#160;hundreds of&#160;billions of dollars a year going into data centers and GPUs,&#160;compute has&#160;become the single biggest cost for any"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/t-mobile-chopped-a-cable-to-expel-chinese-hackers-from-its-network/",
    "domain": "大厂 AI 动态",
    "title": "T-Mobile ‘chopped a cable’ to expel Chinese hackers from its network",
    "url": "https://techcrunch.com/2026/08/19/t-mobile-chopped-a-cable-to-expel-chinese-hackers-from-its-network/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T17:26:32+00:00",
    "summary": "The U.S. phone provider escaped a large-scale breach of its network after identifying Chinese-backed hackers early on."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/times-running-out-save-300-on-your-techcrunch-disrupt-2026-pass-until-august-21/",
    "domain": "大厂 AI 动态",
    "title": "Time’s running out! Save $300 on your TechCrunch Disrupt 2026 pass until August 21",
    "url": "https://techcrunch.com/2026/08/19/times-running-out-save-300-on-your-techcrunch-disrupt-2026-pass-until-august-21/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T16:16:18+00:00",
    "summary": "If you’ve been circling around Disrupt, then now’s the best time to lock in your pass and start getting ready to join the rest of the startup community gathering in San Francisco from October 13-15 at"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/terrapowers-nuclear-reactor-has-a-secret-weapon-for-powering-ai-data-centers/",
    "domain": "大厂 AI 动态",
    "title": "TerraPower’s nuclear reactor has a secret weapon for powering AI data centers",
    "url": "https://techcrunch.com/2026/08/19/terrapowers-nuclear-reactor-has-a-secret-weapon-for-powering-ai-data-centers/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T15:44:53+00:00",
    "summary": "TerraPower's nuclear power plant possesses a strategic advantage over competitors, especially when chasing after data center deals."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/rivian-spinout-also-raises-another-150-million/",
    "domain": "大厂 AI 动态",
    "title": "Rivian spinout Also raises another $150M",
    "url": "https://techcrunch.com/2026/08/19/rivian-spinout-also-raises-another-150-million/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T15:39:47+00:00",
    "summary": "The round, led by Prysm Capital, will fund the company's expansion beyond pedal-assist electric bikes and commercial cargo quads to autonomous delivery vehicles."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/sachin-bansals-fintech-navi-raises-first-outside-capital-with-100m-prosus-investment/",
    "domain": "大厂 AI 动态",
    "title": "Sachin Bansal’s fintech Navi raises first outside capital with $100M Prosus investment",
    "url": "https://techcrunch.com/2026/08/19/sachin-bansals-fintech-navi-raises-first-outside-capital-with-100m-prosus-investment/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T15:01:41+00:00",
    "summary": "The investment comes amid Navi plans to go public."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/amazon-makes-its-ai-powered-alexa-free-on-fire-tv-no-prime-required/",
    "domain": "大厂 AI 动态",
    "title": "Amazon makes its AI-powered Alexa+ free on Fire TV, no Prime required",
    "url": "https://techcrunch.com/2026/08/19/amazon-makes-its-ai-powered-alexa-free-on-fire-tv-no-prime-required/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T15:00:00+00:00",
    "summary": "Amazon is making its AI-powered Alexa+ assistant free on all compatible Fire TV devices in the U.S., automatically upgrading users whether or not they subscribe to Prime."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/amazons-prime-air-is-taking-off-in-nearly-500-u-s-cities/",
    "domain": "大厂 AI 动态",
    "title": "Amazon’s Prime Air is taking off in nearly 500 US cities",
    "url": "https://techcrunch.com/2026/08/19/amazons-prime-air-is-taking-off-in-nearly-500-u-s-cities/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T14:57:58+00:00",
    "summary": "Amazon is significantly expanding its Prime Air drone delivery service, with plans to reach nearly 500 U.S. cities by the end of 2026."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/19/calendly-throws-its-hat-into-meeting-note-taker-circus/",
    "domain": "大厂 AI 动态",
    "title": "Calendly throws its hat into meeting note-taker circus",
    "url": "https://techcrunch.com/2026/08/19/calendly-throws-its-hat-into-meeting-note-taker-circus/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T14:09:39+00:00",
    "summary": "Calendly is also releasing a meeting scheduling assistant called Callie."
  },
  {
    "id": "rss:https://stratechery.com/2026/apple-settles-with-e-u-u-s-app-store-fees-att-rules-in-germany/",
    "domain": "大厂 AI 动态",
    "title": "Apple Settles With E.U., U.S. App Store Fees, ATT Rules in Germany",
    "url": "https://stratechery.com/2026/apple-settles-with-e-u-u-s-app-store-fees-att-rules-in-germany/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T10:00:00+00:00",
    "summary": "Apple's App Store is finally facing the reality of lower fees, and the EU should be satisfied with its work; it's ok it's late."
  },
  {
    "id": "rss:https://stratechery.com/2026/nvidia-backs-openai-data-center-anthropic-news-google-buys-spirit-airlines-data/",
    "domain": "大厂 AI 动态",
    "title": "Nvidia Backs OpenAI Data Center, Anthropic News, Google Buys Spirit Airlines Data",
    "url": "https://stratechery.com/2026/nvidia-backs-openai-data-center-anthropic-news-google-buys-spirit-airlines-data/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-18T10:00:00+00:00",
    "summary": "Nvidia makes another deal, this time with a frontier lab; Anthropic's revenue continues to amaze; and maybe data finally is oil."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/08/nasa-calls-off-mission-to-rescue-swift-gamma-ray-observatory/",
    "domain": "大厂 AI 动态",
    "title": "NASA calls off mission to rescue Swift gamma-ray observatory",
    "url": "https://arstechnica.com/space/2026/08/nasa-calls-off-mission-to-rescue-swift-gamma-ray-observatory/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T00:18:48+00:00",
    "summary": "Without a rescue, NASA's Swift Observatory is expected to reenter the atmosphere later this year."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/amazon-aims-for-delivery-drones-to-reach-500-us-neighborhoods-by-end-of-2026/",
    "domain": "大厂 AI 动态",
    "title": "Amazon aims for delivery drones to reach 500 US neighborhoods by end of 2026",
    "url": "https://arstechnica.com/gadgets/2026/08/amazon-aims-for-delivery-drones-to-reach-500-us-neighborhoods-by-end-of-2026/",
    "source": "Jeremy Hsu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T22:02:38+00:00",
    "summary": "US residents face trade-offs as delivery drone services such as Prime Air expand."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/08/framework-responds-to-complaints-that-bios-update-bricked-ryzen-7040-laptops/",
    "domain": "大厂 AI 动态",
    "title": "Framework responds to complaints that BIOS update bricks Ryzen 7040 laptops",
    "url": "https://arstechnica.com/gadgets/2026/08/framework-responds-to-complaints-that-bios-update-bricked-ryzen-7040-laptops/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T20:21:59+00:00",
    "summary": "Framework says it's replacing some out-of-warranty AMD mainboards."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/flight-attendants-freaked-out-that-google-to-buy-tons-of-spirit-employee-data/",
    "domain": "大厂 AI 动态",
    "title": "Flight attendants freaked out that Google is buying tons of Spirit employee data",
    "url": "https://arstechnica.com/tech-policy/2026/08/flight-attendants-freaked-out-that-google-to-buy-tons-of-spirit-employee-data/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T20:04:41+00:00",
    "summary": "Bankrupt Spirit accused of selling out workers in massive data sale to Google."
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
    "id": "hn:49166182",
    "domain": "股票",
    "title": "Bending Spoons makes first post-IPO acquisition with $1.3B Airtable deal",
    "url": "https://live.euronext.com/en/financial-news/bending-spoons-makes-first-post-ipo-acquisition-13-billion-airtable-deal",
    "source": "riffraff",
    "platform": "hackernews",
    "points": 118,
    "published_at": "2026-08-04T09:27:47+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3779865",
    "domain": "股票",
    "title": "具身智能的“ChatGPT时刻”何时到来？王兴兴：快则两到三年，慢则五到十年",
    "url": "https://wallstreetcn.com/articles/3779865",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T03:29:34+00:00",
    "summary": "宇树科技上市次日股价低开6.51%。创始人王兴兴在世界机器人大会上发表主题演讲称，具身智能泛化能力不足是全球共同瓶颈，但他给出乐观预判——最快两三年，机器人将在80%陌生场景中自主完成80%任务。宇树已启动AI自我进化系统，让机器人“自己进化自己”。"
  },
  {
    "id": "wscn:3779863",
    "domain": "股票",
    "title": "股东回报率明年高达8%、目标“不低于50%的自由现金流”--华尔街解读海力士“40万亿韩元回购计划”",
    "url": "https://wallstreetcn.com/articles/3779863",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T03:26:50+00:00",
    "summary": "摩根大通认为，股东回报政策从\"不超过50%自由现金流\"升级为\"不低于50%\"，由上限变下限，向市场传递了明确信号：未来的股东回报只会多、不会少。高盛预测2027年股东回报率达8%，预计未来还将有约7万亿韩元的额外回购。摩根大通预计至2027年底还有逾16%市值的额外回报空间。后续聚焦10月底业绩会。"
  },
  {
    "id": "wscn:3779862",
    "domain": "股票",
    "title": "Stripe收购OpenRouter：估值三个月暴涨4倍，a16z一周连收两笔巨型退出",
    "url": "https://wallstreetcn.com/articles/3779862",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T03:22:34+00:00",
    "summary": "Stripe以70亿至75亿美元正式收购AI模型聚合平台OpenRouter，较三个月前估值暴涨逾四倍。这笔交易将OpenRouter统一计费、多模型接入的能力无缝嵌入Stripe支付生态。更令业界瞩目的是，背后投资方a16z infra在同一周内连续完成Cursor与OpenRouter两笔巨型退出，创下风险投资史上罕见纪录。"
  },
  {
    "id": "wscn:3779866",
    "domain": "股票",
    "title": "费用下降叠加投资收益增长，360上半年扣非净利1.53亿元",
    "url": "https://wallstreetcn.com/articles/3779866",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T03:22:14+00:00",
    "summary": "增值服务与安全业务增速更快"
  },
  {
    "id": "wscn:3779864",
    "domain": "股票",
    "title": "付鹏：聊聊美国财长贝森特8月的两次出手干预【付鹏说图表】",
    "url": "https://wallstreetcn.com/premium/articles/3779864?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T03:16:48+00:00",
    "summary": "财政部回购：只管“通下水道”，不负责“放水”；美联储 QE：直接“抬升水位”，改变宏观贴现率"
  },
  {
    "id": "wscn:3779853",
    "domain": "股票",
    "title": "韩国存储双雄“巨额回购”！Kospi指数大涨6%，全球债市风暴暂歇、日债普涨，金银持稳",
    "url": "https://wallstreetcn.com/articles/3779853",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T03:15:16+00:00",
    "summary": "SK海力士宣布回购注销40万亿韩元库存股，三星电子拟推出逾100万亿韩元股东回报计划。受此提振，SK海力士单日涨12%，三星涨9%，韩国KOSPI指数大涨约6%。与此同时，美国财政部宣布至少将债券回购规模翻倍，全球长端债市抛售潮暂歇，日本各期限国债收益率普遍下行。"
  },
  {
    "id": "wscn:3779825",
    "domain": "股票",
    "title": "Moderna因黑色素瘤疫苗大涨超170%，mRNA迎来黄金时代？",
    "url": "https://wallstreetcn.com/premium/articles/3779825?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T03:08:48+00:00",
    "summary": "Moderna与默沙东合作的个性化mRNA肿瘤疫苗intismeran autogene（mRNA-4157/V940）联用K药（Keytruda）辅助治疗高危黑色素瘤的III期临床（INTerpath-001）达到主要终点RFS与关键次要终点DMFS——这是全球范围内mRNA肿瘤疫苗的第一个III期成功案例。"
  },
  {
    "id": "wscn:3779861",
    "domain": "股票",
    "title": "报道：三星将公布100万亿韩元股东回报计划，公司计划将50%的自由现金流用于股东回报",
    "url": "https://wallstreetcn.com/articles/3779861",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T02:53:24+00:00",
    "summary": "AI存储超级周期带动现金流激增，三星电子将推出逾100万亿韩元史上最大股东回报计划，以50%自由现金流返还股东，特别股息与回购注销为主要选项。SK海力士周三宣布，将回购并注销价值40万亿韩元的库存股，韩国半导体行业回报潮涌现。"
  },
  {
    "id": "wscn:3779856",
    "domain": "股票",
    "title": "贝森特“救美债”就是“放弃美元”，花旗：强烈看多黄金！",
    "url": "https://wallstreetcn.com/articles/3779856",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T02:53:14+00:00",
    "summary": "美日正式结盟护汇，贝森特亲自背书联合买入日元，并将汇率政策纳入国家经济安全框架。花旗揭示，美元强势被主动让渡以换取债务安全，美债久期结构将被重塑，EUR/JPY的185至186成关键警戒线。在美元信用被政策性稀释的历史性时刻，黄金成为储备体系重构的最直接受益资产，花旗给出\"强烈看多\"。"
  },
  {
    "id": "wscn:3779860",
    "domain": "股票",
    "title": "海力士在权威期刊发表CPO路线图：不仅“算力之间用光”，还要把光延伸到内存接口",
    "url": "https://wallstreetcn.com/articles/3779860",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T02:34:04+00:00",
    "summary": "SK海力士联合弗吉尼亚大学等机构在《自然·电子学》发表CPO技术路线图论文。文章提出，算力每两年增长3倍，互联带宽却仅增1.4倍，“带宽墙”成为AI扩展的核心瓶颈。CPO技术被列为突围关键，而更远的愿景是将CPO延伸至内存接口，让多块AI加速器共享同一内存池，提升内存利用效率。"
  },
  {
    "id": "wscn:3779857",
    "domain": "股票",
    "title": "长债利率暴涨之谜",
    "url": "https://wallstreetcn.com/articles/3779857",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T02:16:53+00:00",
    "summary": "30年期美债收益率飙破5.32%创2007年来新高，全球长债市场风险骤升。国金宏观认为，科技巨头AI军备竞赛催生万亿级融资需求，正与美国国债争夺全球长期资本；叠加美联储公信力折价、高油价通胀隐忧，以及日本资金回流这头“灰犀牛”，长端利率上行压力远未终结，黄金或成最终受益者。"
  },
  {
    "id": "wscn:3779859",
    "domain": "股票",
    "title": "A股三大股指齐涨，医药大爆发，创新药掀起涨停潮，恒指、恒科指均涨1%，科网股普涨",
    "url": "https://wallstreetcn.com/articles/3779859",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T02:09:30+00:00",
    "summary": "医药生物板块盘中持续走高，疫苗、细胞免疫、重组蛋白、基因编辑等方向均表现亮眼，石药创新、博腾股份、和元生物、康希诺、键凯科技、华大智造等近20股录得20cm涨停，森萱医药、东富龙、康泰生物、药石科技等多股涨超10%。"
  },
  {
    "id": "wscn:3779548",
    "domain": "股票",
    "title": "黄金冲破4400之后：第二轮行情正在启动？",
    "url": "https://wallstreetcn.com/premium/articles/3779548?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T01:38:57+00:00",
    "summary": "黄金突破4400美元，ETF回流与央行购金共振，若突破4500美元，第二轮行情有望启动。"
  },
  {
    "id": "wscn:3779855",
    "domain": "股票",
    "title": "存储产能洽谈已排至2030年！华邦电子提前启动扩产计划",
    "url": "https://wallstreetcn.com/articles/3779855",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T01:37:43+00:00",
    "summary": "华邦电子提前启动高雄路竹厂Module B扩产计划，预计2027年动工、2029年装机，客户产能洽谈已排至2029年至2030年。AI驱动的存储需求被机构认为将“延续相当长时间”。此外，华邦电子已投入约40亿元布局矽电容产线，最快2027年量产，被视为逻辑与存储之外的第三成长动能。"
  },
  {
    "id": "wscn:3779774",
    "domain": "股票",
    "title": "粮价还没起飞，化肥为何先涨了？不只是“粮食安全”，厄尔尼诺正在打开农资周期的“第二段行情”",
    "url": "https://wallstreetcn.com/premium/articles/3779774?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T01:17:04+00:00",
    "summary": "2026年超强厄尔尼诺预期持续升温，天气扰动已开始影响东南亚、印度等农业主产区，但历史经验显示，强厄尔尼诺并不必然带来主粮全面减产。真正值得关注的是，化肥景气已先于粮价启动：尿素受出口与海外高价支撑，磷肥受资源、硫磺与航运约束，钾肥供给趋紧。若天气冲击在2027年进一步推升粮价和种植收益，当前由供给推动的化肥行情，会不会进入供需共振的第二阶段？"
  },
  {
    "id": "wscn:3779851",
    "domain": "股票",
    "title": "特朗普表态支持，“币圈永续合约巨头”Hyperliquid有望合规入美",
    "url": "https://wallstreetcn.com/articles/3779851",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T01:16:54+00:00",
    "summary": "特朗普亲自为离岸加密衍生品平台Hyperliquid站台，公开表示CFTC主席正推动其\"完全合规\"入美，释放出华盛顿将永续合约交易基础设施纳入监管体系的强烈信号。消息一出，平台代币HYPE价格跳涨，相关上市公司股价飙升31%；Cboe、CME则遭受明显冲击，传统衍生品交易所的市场版图或将迎来历史性重构。"
  },
  {
    "id": "wscn:3779852",
    "domain": "股票",
    "title": "美国需要一次可控的信用风险释放",
    "url": "https://wallstreetcn.com/articles/3779852",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T01:16:29+00:00",
    "summary": "美国30年期国债收益率攀升至5.33%新高，根源在于AI资本支出热潮驱动的民间信用扩张，持续挤压政府融资空间。加息无法抑制这一扩张，反而推高政府融资成本。解决路径有二：一是美联储结构性降息，压低长端利率以缓解矛盾；二是主动释放可控信用风险，恢复信贷市场优胜劣汰机制。"
  },
  {
    "id": "wscn:3779848",
    "domain": "股票",
    "title": "马士基CEO：“我们开始达到极限”...",
    "url": "https://wallstreetcn.com/articles/3779848",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T01:09:24+00:00",
    "summary": "马士基CEO柯文胜罕见\"变调\"——曾被视为集运市场\"逆风\"的贸易战、去全球化、运力过剩，正被重新审视。需求弹性超预期、陆侧港口瓶颈难解，推动运价中枢上移；96%的超高舱位利用率更迫使马士基考虑船队扩张。这场行业巨头的\"叙事转变\"，或将重塑整个集运市场的竞争格局。"
  },
  {
    "id": "wscn:3779849",
    "domain": "股票",
    "title": "业绩暴雷后紧急“灭火”，OpenAI CFO全员会表态：Q3 ARR已增35%，2027年或更早上市",
    "url": "https://wallstreetcn.com/articles/3779849",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T01:09:15+00:00",
    "summary": "面对Q2收入增速仅18%、高管接连出走的双重压力，OpenAI CFO在全员会上亮出Q3最新数据：整体ARR至今增长35%，企业ARR增长50%，并明确表示公司“将在2027年或更早上市”。她同时要求员工不必担忧Anthropic可能抢先IPO，称“我们在跑自己的赛道”。"
  },
  {
    "id": "wscn:3779823",
    "domain": "股票",
    "title": "没有人的文明毫无意义？这个问题的答案已经握在了AI手里（二）",
    "url": "https://wallstreetcn.com/premium/articles/3779823?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-20T01:05:45+00:00",
    "summary": "一个“由天才组成的国家”，第一次可以不通过任何一次生育而被“制造”出来。"
  },
  {
    "id": "hn:49322233",
    "domain": "股票",
    "title": "AI is not just one bubble, strategist says – but a 'rolling sequence of bubbles'",
    "url": "https://fortune.com/2026/08/16/ai-bubble-sequence-saas-software-stocks-silver-prices-chipmakers/",
    "source": "pessimizer",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-16T18:05:39+00:00",
    "summary": ""
  },
  {
    "id": "hn:49338121",
    "domain": "股票",
    "title": "US tech stock correction likely, warn ECB economists",
    "url": "https://www.ft.com/content/cb4b22ab-4183-4d19-be60-6d2fab86d86d",
    "source": "aanet",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-17T21:46:22+00:00",
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
    "id": "hn:49305685",
    "domain": "股票",
    "title": "Backtesting Congress members stock trades by the disclosure date",
    "url": "https://investingpaths.com/tools/congress",
    "source": "ProdRatSuperior",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-14T23:08:56+00:00",
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
    "id": "hn:49257407",
    "domain": "股票",
    "title": "I backtested my own stock rankings. They lost to the index",
    "url": "https://holderdashboard.com/learn/backtest-that-lost-to-the-index",
    "source": "caiocmpaes",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-08-11T12:44:43+00:00",
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
    "id": "hn:49355142",
    "domain": "金融",
    "title": "Sticky wage norms and the real wage cost of unexpected inflation",
    "url": "https://bfi.uchicago.edu/wp-content/uploads/2026/08/BFI_WP_2026-108-1.pdf",
    "source": "jplusequalt",
    "platform": "hackernews",
    "points": 384,
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
    "id": "hn:49175192",
    "domain": "金融",
    "title": "Thanks FedEx, This Is Why We Keep Getting Phished (2024)",
    "url": "https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/",
    "source": "stymaar",
    "platform": "hackernews",
    "points": 338,
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
    "points": 179,
    "published_at": "2026-08-06T18:22:16+00:00",
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
    "id": "hn:49122994",
    "domain": "金融",
    "title": "Situational Awareness down 67% in July in AI stock rout",
    "url": "https://www.wsj.com/finance/investing/situational-awareness-down-67-in-july-in-ai-stock-rout-cd19901f",
    "source": "pondsider",
    "platform": "hackernews",
    "points": 157,
    "published_at": "2026-07-31T13:37:36+00:00",
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
    "id": "rss:https://arxiv.org/abs/2608.17111",
    "domain": "金融",
    "title": "Stranded credentials: how a skill-signaling market absorbed generative AI",
    "url": "https://arxiv.org/abs/2608.17111",
    "source": "Song Yao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2608.17111v1 Announce Type: new Abstract: Generative AI can now perform many tasks that credentialing institutions count on to assess skill. During the AI era, do credentials retain their signal"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.17436",
    "domain": "金融",
    "title": "The Long-Term Effects of British and French Colonization in Africa on Trust in Traditional Leaders",
    "url": "https://arxiv.org/abs/2608.17436",
    "source": "Brice Romuald Gueyap Kounga",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2608.17436v1 Announce Type: new Abstract: Trust in local institutions matters for trade, public goods provision, conflict resolution, and democratic consolidation. Using individual data from rou"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.17481",
    "domain": "金融",
    "title": "A generic nonparametric value-at-risk estimator for high dimensions",
    "url": "https://arxiv.org/abs/2608.17481",
    "source": "Siyuan Sun",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2608.17481v1 Announce Type: new Abstract: We present in this article a non-parametric value-at-risk (VaR+CVaR) algorithm that remains accurate for an arbitrarily large number of underlying posit"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.17636",
    "domain": "金融",
    "title": "COS-TT-CHF: A Tensor-Train Characteristic-Function COS Method for Multi-Asset Option Pricing",
    "url": "https://arxiv.org/abs/2608.17636",
    "source": "Lucas Arenstein, Michael Kastoryano",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2608.17636v1 Announce Type: new Abstract: This paper considers European multi-asset option pricing under L\\'evy and affine characteristic-function models. The main obstruction is the curse of di"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.17715",
    "domain": "金融",
    "title": "Communicating Credit Risk with Large Language Models: Evaluation of Explanations from Standard and Alternative Data-Based Models",
    "url": "https://arxiv.org/abs/2608.17715",
    "source": "Sahab Zandi, Noah Kostesku, Christophe Mues, Mar\\'ia \\'Oskarsd\\'ottir, Cristi\\'an Bravo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2608.17715v1 Announce Type: new Abstract: Credit decisioning is a high-stakes task in which model outputs must be accurate and explainable to support compliant decisions. Although modern credit "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.18022",
    "domain": "金融",
    "title": "Entropic Value-at-Risk portfolio optimization for tempered stable L\\'evy processes",
    "url": "https://arxiv.org/abs/2608.18022",
    "source": "Jaehyung Choi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2608.18022v1 Announce Type: new Abstract: We develop parametric Entropic Value-at-Risk (EVaR) portfolio optimization for tempered stable L\\'evy returns. We derive portfolio cumulant-generating f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.18069",
    "domain": "金融",
    "title": "Revisiting the Intra-Team Communication Method to Elicit Level-k Reasoning in Beauty Contests and 11-20 Games",
    "url": "https://arxiv.org/abs/2608.18069",
    "source": "Zitian Wang, Istiak Ahmed, Patarasate Unjitwattana, Emily Yunxi Xie, Meng-Jhang Fong, Po-Hsuan Lin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2608.18069v1 Announce Type: new Abstract: How level-0 players behave and how they are perceived by higher-level players are central questions in the literature on level-k models of boundedly rat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.17312",
    "domain": "金融",
    "title": "Reputation and institutional certification as complementary trust mechanisms in a single online market",
    "url": "https://arxiv.org/abs/2608.17312",
    "source": "Yuta Kido, Yohsuke Ohtsubo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2608.17312v1 Announce Type: cross Abstract: Reputation and institutional certification are the two main trust mechanisms under information asymmetry, yet their interaction remains poorly underst"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.17363",
    "domain": "金融",
    "title": "Conservation of Short-term Flows: Signed Optimal Transport",
    "url": "https://arxiv.org/abs/2608.17363",
    "source": "Jiaxing Weng",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2608.17363v1 Announce Type: cross Abstract: This paper develops a theoretical framework for signed optimal transport. A global flatness measure induced by the continuum transport equation serves"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.17624",
    "domain": "金融",
    "title": "Governing Delegation to Generative Artificial Intelligence: Human Direction, Work-Related Orientation, and Modes of Use",
    "url": "https://arxiv.org/abs/2608.17624",
    "source": "Jorge F\\'abrega",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2608.17624v1 Announce Type: cross Abstract: Delegating cognitive operations to generative artificial intelligence redistributes execution and raises a governance problem: where human direction o"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.17808",
    "domain": "金融",
    "title": "Self-Consistent Adjoint Policy Iteration for Constrained Dynamic Portfolio Choice",
    "url": "https://arxiv.org/abs/2608.17808",
    "source": "Jeonggyu Huh, Yeoneung Kim, Seungwon Jeong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2608.17808v1 Announce Type: cross Abstract: We develop simulation-based policy iteration for continuous-time portfolio choice with predictable returns and convex constraints. Each outer step re-"
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.20060",
    "domain": "金融",
    "title": "Constrained portfolio optimization in a life-cycle model: A deep pricing kernel approach",
    "url": "https://arxiv.org/abs/2410.20060",
    "source": "Wenyuan Li, Pengyu Wei",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2410.20060v4 Announce Type: replace Abstract: This paper considers the constrained portfolio optimization in a generalized life-cycle model. The individual with a stochastic income manages a por"
  },
  {
    "id": "rss:https://arxiv.org/abs/2503.09212",
    "domain": "金融",
    "title": "How Generative AI Adoption Alters the Demand for Cognitive and Social Skills Within Roles: A Skill-Centric Analysis",
    "url": "https://arxiv.org/abs/2503.09212",
    "source": "Piyush Gulati, Arianna Marchetti, Victoria Sevcenko, Phanish Puranam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2503.09212v3 Announce Type: replace Abstract: A common view holds that generative AI (GenAI) automates cognitive tasks, reshaping roles to emphasize social skills over cognitive ones. Drawing on"
  },
  {
    "id": "rss:https://arxiv.org/abs/2511.17954",
    "domain": "金融",
    "title": "A multi-view contrastive learning framework for spatial embeddings in risk modelling",
    "url": "https://arxiv.org/abs/2511.17954",
    "source": "Freek Holvoet, Christopher Blier-Wong, Katrien Antonio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2511.17954v2 Announce Type: replace Abstract: Incorporating spatial information, particularly when related to climate, weather, and demographic factors, is crucial for improving underwriting pre"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.00346",
    "domain": "金融",
    "title": "Forecasting duration in high-frequency financial data using a self-exciting flexible residual point process",
    "url": "https://arxiv.org/abs/2604.00346",
    "source": "Kyungsub Lee",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2604.00346v2 Announce Type: replace Abstract: This paper presents a method for forecasting limit order book durations using a self-exciting flexible residual point process. High-frequency events"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.03703",
    "domain": "金融",
    "title": "Preying on Leveraged ETFs",
    "url": "https://arxiv.org/abs/2608.03703",
    "source": "Yinhong Zhao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2608.03703v2 Announce Type: replace Abstract: We argue that arbitrageurs preying on the closing rebalances of leveraged exchange-traded funds (LETFs) contributed to the Korean market's extreme v"
  },
  {
    "id": "rss:https://arxiv.org/abs/2405.09260",
    "domain": "金融",
    "title": "Geometric BSDEs",
    "url": "https://arxiv.org/abs/2405.09260",
    "source": "Roger J. A. Laeven, Emanuela Rosazza Gianin, Marco Zullino",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2405.09260v4 Announce Type: replace-cross Abstract: We introduce Geometric Backward Stochastic Differential Equations (GBSDEs) and two-driver BSDEs, which arise naturally in the geometric dynami"
  },
  {
    "id": "rss:https://arxiv.org/abs/2509.03126",
    "domain": "金融",
    "title": "On the Smart Coordination of Flexibility Scheduling in Multi-carrier Integrated Energy Systems",
    "url": "https://arxiv.org/abs/2509.03126",
    "source": "Christian Doh Dinga, Sander van Rijn, Laurens de Vries, Milos Cvetkovic",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2509.03126v2 Announce Type: replace-cross Abstract: Coordinating the interactions between flexibility assets in multi-carrier integrated energy systems (MIES) can lead to an efficient integratio"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.22994",
    "domain": "金融",
    "title": "Grow and Pollute but Invest and Clean: Dynamic Associations between Parent Firm Characteristics and Facility Toxic Releases",
    "url": "https://arxiv.org/abs/2605.22994",
    "source": "George Kapetanios, Steven Ongena, Alexia Ventouri, Huiyan Xiao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2605.22994v2 Announce Type: replace-cross Abstract: This paper examines how relationships between parent-firm characteristics and facility-level toxic releases evolve over time. Using 238,304 ob"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.03646",
    "domain": "金融",
    "title": "Crypto-Microeconomics: The Distribution of Bitcoin Wealth Among Diverse Economic Agents",
    "url": "https://arxiv.org/abs/2607.03646",
    "source": "Syed Azhar Hussain, Kashif Ahmad, Mubashir Husain Rehmani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-19T04:00:00+00:00",
    "summary": "arXiv:2607.03646v2 Announce Type: replace-cross Abstract: Bitcoin (BTC) wealth distribution is often analyzed with macro indicators such as aggregate addresses, wallet balances, prices, network activi"
  },
  {
    "id": "hn:49243531",
    "domain": "金融",
    "title": "China is now the world's greatest oil power",
    "url": "https://www.economist.com/finance-and-economics/2026/08/09/china-is-now-the-worlds-great-oil-power",
    "source": "bookofjoe",
    "platform": "hackernews",
    "points": 55,
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
    "id": "hn:49111879",
    "domain": "金融",
    "title": "Citadel Buys Situational Awareness's Stock Portfolio After Big Losses in AI",
    "url": "https://www.wsj.com/finance/citadel-buys-situational-awarenesss-stock-portfolio-after-big-losses-in-ai-5117159b",
    "source": "mudil",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-07-30T16:00:33+00:00",
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
    "id": "hn:49173576",
    "domain": "金融",
    "title": "Investors in Situational Awareness deserved to lose their shirts",
    "url": "https://www.economist.com/finance-and-economics/2026/08/04/investors-in-situational-awareness-deserved-to-lose-their-shirts",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-08-04T19:18:35+00:00",
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
    "id": "hn:49208461",
    "domain": "金融",
    "title": "New Intelligence Warns Russia May Provoke NATO Amid Dwindling U.S. Munitions",
    "url": "https://www.wsj.com/finance/investing/new-intelligence-warns-russia-may-provoke-nato-amid-dwindling-u-s-munitions-68f497c7",
    "source": "doener",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-07T10:52:27+00:00",
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
    "id": "hn:48999988",
    "domain": "金融",
    "title": "Brazil and US clash over future of payments as Pix system stirs global interest",
    "url": "https://www.reuters.com/business/finance/brazil-us-clash-over-future-payments-popular-pix-system-stirs-global-interest-2026-07-21/",
    "source": "petethomas",
    "platform": "hackernews",
    "points": 17,
    "published_at": "2026-07-21T23:52:52+00:00",
    "summary": ""
  }
]
```
