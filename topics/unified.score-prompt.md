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

- 今日日期：`2026-09-26`
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
  "date": "2026-09-26",
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
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 2000133,
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
    "points": 1906244,
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
    "points": 1595080,
    "published_at": "2026-05-05T14:08:25+00:00",
    "summary": "Claude Code保姆级教学【收藏起来不会错！】\n从上手安装，到高级用法，这期一次讲全～\n花了三周做教程，希望能帮到你嘻嘻，感谢朋友们的三连+关注啦～"
  },
  {
    "id": "bvid:BV1RPET6tEp2",
    "domain": "AI",
    "title": "零基础Vibe Coding教程，vibecoding实战，Claude Code+Codex+Cursor",
    "url": "http://www.bilibili.com/video/av116711944620974",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 1334331,
    "published_at": "2026-06-09T02:00:00+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“VibeCoding”免费获取\n【课程简介】从零开始，用自然语言指挥AI开发真实软件项目！"
  },
  {
    "id": "bvid:BV14rzQB9EJj",
    "domain": "AI",
    "title": "Claude Code 从 0 到 1 全攻略：MCP / SubAgent / Agent Skill / Hook / 图片 / 上下文处理/ 后台任务",
    "url": "http://www.bilibili.com/video/av115954889596221",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1320532,
    "published_at": "2026-01-25T08:55:20+00:00",
    "summary": "时间戳如下，方便大家跳转观看：\n \n第一部分：环境搭建与基础交互\n- 01:09 安装 Claude Code\n- 01:43 登录与授权\n- 02:55 第一个实战问题\n- 03:12 三种模式详解 (默认/自动/规划)\n \n第二部分：复杂任务处理与终端控制\n- 06:00 执行终端命令 (Bash)\n- 06:49 使用规划模式 (Plan Mode)\n- 11:06 跳过所有权限检测 (da"
  },
  {
    "id": "bvid:BV11NNAz5EKn",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI Agent智能体搭建教程，从入门到实战！手把手教你快速打造自己的专属智能体，一次性搞懂AI大模型智能体开发，学完薪资翻倍！",
    "url": "http://www.bilibili.com/video/av116187623069851",
    "source": "AI-智能体搭建教程",
    "platform": "bilibili",
    "points": 1281177,
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
    "points": 1099014,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 991189,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 945686,
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
    "points": 891362,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 810386,
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
    "points": 693860,
    "published_at": "2026-05-15T12:35:03+00:00",
    "summary": "一口气带你认识 Cursor、Claude Code、Codex、GitHub Copilot、Windsurf、Trae、Kiro、Qoder、CodeBuddy 等 32 个主流的 AI 编程工具的实测表现，帮你快速找到最适合自己的。\n编程学习教程+实战项目+简历模板：codefather.cn\n开源 AI 编程教程：github.com/liyupi/ai-guide\n视频涵盖 Cursor"
  },
  {
    "id": "bvid:BV1WBG9zgECp",
    "domain": "AI",
    "title": "史上最强 AI 编程工具免费啦！Cursor 保姆级使用教程！新手友好！看到就是赚到！｜ 集成 MCP ！",
    "url": "http://www.bilibili.com/video/av114426116120045",
    "source": "AfterShip",
    "platform": "bilibili",
    "points": 673994,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1aDMezREUj",
    "domain": "AI",
    "title": "Cursor使用教程，2小时玩转cursor，cursor无限续杯",
    "url": "http://www.bilibili.com/video/av114691716154833",
    "source": "尚硅谷",
    "platform": "bilibili",
    "points": 590445,
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
    "points": 443375,
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
    "points": 415491,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 343525,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 297070,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 296811,
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
    "points": 285056,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1BvR1BtEFD",
    "domain": "AI",
    "title": "Vibe Coding纯小白教程：对AI说话就做出软件。手把手带你做出1个软件！",
    "url": "http://www.bilibili.com/video/av116521405780262",
    "source": "大牙大-",
    "platform": "bilibili",
    "points": 267832,
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
    "points": 237088,
    "published_at": "2024-09-17T01:00:00+00:00",
    "summary": "喜欢的朋友可以三连+关注～这对我真的很重要"
  },
  {
    "id": "bvid:BV154426xEha",
    "domain": "AI",
    "title": "我的 AI 编程全流程：如何使用 AI 稳定交付一个高质量的产品",
    "url": "http://www.bilibili.com/video/av117178586240848",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 232669,
    "published_at": "2026-08-29T11:38:24+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 216520,
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
    "points": 187488,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 182118,
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
    "points": 165126,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1WWYE6LEzx",
    "domain": "AI",
    "title": "黑马程序员2026全网最夯VibeCoding零基础入门到实战项目开发全套视频教程，AI辅助编程从入门到实战，涵盖Claude Code、DeepSeek等内容",
    "url": "http://www.bilibili.com/video/av117251667724450",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 143336,
    "published_at": "2026-09-14T01:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260914\n2026黑马程序员AI智能应用开发学习路线图\nhttps://www.bilibili.com/opus/1156896913511940102\n如何下载资料\nhttps://www.bilibili.com/read/cv7881295/\n学习+球球群625260577，告别孤单，共同进步！\n\n【AI智能"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 123884,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV16hTc6xEpF",
    "domain": "AI",
    "title": "【Codex实战】手摸手教你多Agent协同开发",
    "url": "http://www.bilibili.com/video/av116839870891259",
    "source": "路边爱吃瓜",
    "platform": "bilibili",
    "points": 101424,
    "published_at": "2026-06-30T16:00:22+00:00",
    "summary": "Codex多Agent协同开发"
  },
  {
    "id": "bvid:BV1dpdZYBE9q",
    "domain": "AI",
    "title": "零代码让AI秒接海量MCP工具！最适合小白的MCP集合平台",
    "url": "http://www.bilibili.com/video/av114340703243255",
    "source": "AI研究室-帆哥",
    "platform": "bilibili",
    "points": 99990,
    "published_at": "2025-04-15T11:00:00+00:00",
    "summary": "最近MCP太火了，阿里直接跟进把MCP整合到百炼平台里面了，做了一个MCP的“应用商店”。\n之前不管是在cursor还是Claude上还是需要配置一下MCP服务器，现在在百炼上就可以直接无脑添加MCP工具，非常方便。\n而且因为在平台上一体化，和大模型可以打包配置，让后端的运维部署变得更轻松。\n这个视频教你怎么用阿里云百炼的MCP工具创建一个agent应用。"
  },
  {
    "id": "bvid:BV1hsKzzcEkz",
    "domain": "AI",
    "title": "十分钟Cursor教程！关于Cursor你可能不知道的事",
    "url": "http://www.bilibili.com/video/av114756006448971",
    "source": "GeekHour",
    "platform": "bilibili",
    "points": 81588,
    "published_at": "2025-06-28T10:12:00+00:00",
    "summary": "十分钟Cursor教程，视频中的资料可以关注同名gzh后下载！"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 75300,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1KX9jB8E9M",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的 CurSor AI编程零基础全套教程，手把手教你搭建高效Cursor工作流，全程干货无废话！比付费效果强十倍",
    "url": "http://www.bilibili.com/video/av116328887225403",
    "source": "AI大模型技术教程",
    "platform": "bilibili",
    "points": 73782,
    "published_at": "2026-04-01T10:12:34+00:00",
    "summary": "视频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV1V7QZBmETr",
    "domain": "AI",
    "title": "2026吃透Cursor+Skills实战指南教程，手把手带你开发爆款app，从使用到原理，一次讲清！拿走不谢，允许白嫖，让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av116277951597321",
    "source": "徐庶架构师",
    "platform": "bilibili",
    "points": 71639,
    "published_at": "2026-03-23T10:18:18+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\n视频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV1KocTzHE3Z",
    "domain": "AI",
    "title": "2027版 Cursor+Claude AI编程 1天快速上手 视频教程",
    "url": "http://www.bilibili.com/video/av116040285622077",
    "source": "java1234官方",
    "platform": "bilibili",
    "points": 67468,
    "published_at": "2026-02-09T10:57:55+00:00",
    "summary": "本课程主要讲解Cursor简介，Cursor下载安装，Cursor生成helloWorld网页，Cursor会话里的Cursor会话里的Agent,Plan,Debug,Ask区别以及使用，Cursor常用模型介绍，Cursor模型会话上下文介绍，以及最后利用Cursor Opus4.6快速生成一个Java项目 -SpringBoot4+Vue3的学生信息管理系统，利用Cursor Opus4.6"
  },
  {
    "id": "bvid:BV16LXjYHETR",
    "domain": "AI",
    "title": "🔥【Cursor保姆级教程】新手必问10大问题❗️手把手教你快速入门💻",
    "url": "http://www.bilibili.com/video/av114182812863204",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 65686,
    "published_at": "2025-03-18T09:55:27+00:00",
    "summary": "Cursor新手必问10大问题：\n一、免费和收费的区别是什么？\n二、只用cursor就能开发了吗？\n三、如何汉化以及插件的使用？\n四、怎么配置Rules？\n五、如何解决程序错误？\n六、claude -3.7- sonet 以及 claude -3.7- sonet-thinking 如何选择？\n七、Ask、Edit、Agent 三种模式的区别？\n八、如何进行代码回滚？\n九、cursor 降智了怎么"
  },
  {
    "id": "bvid:BV12NK1zMESx",
    "domain": "AI",
    "title": "如何用Cursor开发大项目，全流程讲解，干货十足",
    "url": "http://www.bilibili.com/video/av114758657246726",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 60567,
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
    "points": 55475,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1tXRAYiEYR",
    "domain": "AI",
    "title": "使用Cursor制作高保真原型图",
    "url": "http://www.bilibili.com/video/av114114999356114",
    "source": "AI技术玩家",
    "platform": "bilibili",
    "points": 50475,
    "published_at": "2025-03-06T10:40:35+00:00",
    "summary": "Cursor 除了可以开发代码之外，我们还可以利用 Cursor 来制作高保真的原型图。\n\n在 Agent 模式下 Cursor 就会自动为我们创建一些 HTML + CSS 的代码页面。\n\n然后可以根据我们的需求继续微调，如果你觉得效果不太好，可以参考让 Cursor 参考一些优秀的设计，也可以把你觉得好的设计效果图提供给 Cursor。\n\n设计完成后我们可以使用一个名为 `html.to.de"
  },
  {
    "id": "bvid:BV1hxMbzqEzU",
    "domain": "AI",
    "title": "小智MCP自由了！我开源了个命令行神器实现多MCP聚合",
    "url": "http://www.bilibili.com/video/av114686414625640",
    "source": "闪电蘑菇",
    "platform": "bilibili",
    "points": 41915,
    "published_at": "2025-06-15T08:31:55+00:00",
    "summary": "- 我写的小智客户端命令行工具\n - github: https://github.com/shenjingnan/xiaozhi-client\n - gitee: https://gitee.com/shenjingnan/xiaozhi-client\n\n- 小智官方MCP示例代码仓库：\n - github: https://github.com/78/mcp-calculator\n - git"
  },
  {
    "id": "bvid:BV1JcDSBYE4V",
    "domain": "AI",
    "title": "新版 Cursor 看不到代码了？5 分钟学会新界面所有操作",
    "url": "http://www.bilibili.com/video/av116390174393526",
    "source": "未生AI",
    "platform": "bilibili",
    "points": 31962,
    "published_at": "2026-04-12T05:55:17+00:00",
    "summary": "Cursor 最新版本的界面。只有一个文字输入框。没有代码，没有文件树，没有你以前熟悉的任何东西。\n\n很多人打开之后直接懵了——这怎么用？我的代码呢？这期视频，我就来告诉你，新版 Cursor 到底怎么用。\n\nCursor 的改版，不只是界面变了。\n\n所有 AI 编程工具，以前的形态都是一样的——左边文件树，右边代码，AI 在旁边帮你补全。\n\n这个形态本质上还是：人在主导代码，AI 在辅助人。\n\n"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30788,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1WtoTBiEuR",
    "domain": "AI",
    "title": "Claude Code多Agent模式实战分享",
    "url": "http://www.bilibili.com/video/av116454666012312",
    "source": "Simon林_",
    "platform": "bilibili",
    "points": 26104,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1i4GNzWEHP",
    "domain": "AI",
    "title": "【Cursor安装】目前最好用的AI编程软件Cursor安装教程+如何汉化",
    "url": "http://www.bilibili.com/video/av114824105302737",
    "source": "兔子喵爱编程",
    "platform": "bilibili",
    "points": 24257,
    "published_at": "2025-07-09T16:05:07+00:00",
    "summary": "有无编程基础都可以尝试一下AI编程，编程真的很简单也很有趣！！\n后面会出详细的cursor使用教程，大家可以持续追更一下"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 23172,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1VuNp6PEBM",
    "domain": "AI",
    "title": "Claude Code、Codex、Cursor，你都用对了吗？#howto入门codex #howto入门vibecoding #姜学长",
    "url": "http://www.bilibili.com/video/av116896292739893",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 21221,
    "published_at": "2026-07-10T15:07:59+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1sgez6BEHi",
    "domain": "AI",
    "title": "2026华为杯研赛AI合规使用超详细教程！含AI官方解析+写作规范+AIGC检测+AI降重+AI痕迹检测等全覆盖！全网最详细研赛AI使用保姆级教程！",
    "url": "http://www.bilibili.com/video/av117303425373942",
    "source": "数学建模老哥",
    "platform": "bilibili",
    "points": 20253,
    "published_at": "2026-09-20T12:49:01+00:00",
    "summary": "2026华为杯研赛AI合规使用超详细教程！含AI官方解析+写作规范+AIGC检测+AI降重+AI痕迹检测等全覆盖！全网最详细研赛AI使用保姆级教程！"
  },
  {
    "id": "bvid:BV1ofhq6jE28",
    "domain": "AI",
    "title": "我做了一个辅助自学的Agent，让它带你从零吃透一门科目！",
    "url": "http://www.bilibili.com/video/av117309230421312",
    "source": "红豆_meow",
    "platform": "bilibili",
    "points": 20039,
    "published_at": "2026-09-21T13:22:32+00:00",
    "summary": "项目仓库：https://github.com/Miaotofu01/Study-Mate \n记得点个star，这真的很重要！\n项目尚不完善，欢迎来提pr！"
  },
  {
    "id": "bvid:BV1wqeb6gEDY",
    "domain": "AI",
    "title": "Claude Code 百分百不封号",
    "url": "http://www.bilibili.com/video/av117297150694473",
    "source": "DUNHKPcc",
    "platform": "bilibili",
    "points": 19272,
    "published_at": "2026-09-19T10:14:15+00:00",
    "summary": "如果需要文档，私信主播，主页送免费的token"
  },
  {
    "id": "hn:49724881",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia announces native GPU programming in Rust",
    "url": "https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/",
    "source": "nonmaskable",
    "platform": "hackernews",
    "points": 970,
    "published_at": "2026-09-16T11:15:53+00:00",
    "summary": ""
  },
  {
    "id": "hn:49673098",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia is the central bank of AI",
    "url": "https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai",
    "source": "tolugenius",
    "platform": "hackernews",
    "points": 584,
    "published_at": "2026-09-12T15:08:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49824864",
    "domain": "AI 算力 / 半导体",
    "title": "Virtio-nvgpu: Near-native Nvidia GPU access inside a KVM guest",
    "url": "https://github.com/nestrilabs/virtio-nvgpu",
    "source": "WanjohiRyan",
    "platform": "hackernews",
    "points": 152,
    "published_at": "2026-09-24T01:02:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49682319",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia dismisses \"circular financing\", says every $1 it invests brings back $100",
    "url": "https://invezz.com/news/2026/09/11/nvidia-says-every-1-it-invests-brings-back-100-so-why-does-the-stock-keep-falling/",
    "source": "mgh2",
    "platform": "hackernews",
    "points": 138,
    "published_at": "2026-09-13T10:29:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49714096",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC revealing details about next gen A14 node",
    "url": "https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331",
    "source": "osnium123",
    "platform": "hackernews",
    "points": 128,
    "published_at": "2026-09-15T15:31:55+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/huaweis-tau-law-takes-commercial-form/",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei’s Tau Law Takes Commercial Form",
    "url": "https://www.eetimes.com/huaweis-tau-law-takes-commercial-form/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T14:18:57+00:00",
    "summary": "Kirin 9050 Pro rests on the Tau (τ) Scaling Law, marking a major change in chip architecture designed to bypass EUV lithography limits. The post Huawei’s Tau Law Takes Commercial Form appeared first o"
  },
  {
    "id": "rss:https://www.eetimes.com/balancing-bandwidth-range-and-power-in-intelligent-buildings/",
    "domain": "AI 算力 / 半导体",
    "title": "Balancing Bandwidth, Range, and Power in Intelligent Buildings",
    "url": "https://www.eetimes.com/balancing-bandwidth-range-and-power-in-intelligent-buildings/",
    "source": "Andy McFarlane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T08:00:34+00:00",
    "summary": "As edge AI transforms smart buildings, Wi-Fi HaLow bridges the gap between bandwidth, long range, and low power. The post Balancing Bandwidth, Range, and Power in Intelligent Buildings appeared first "
  },
  {
    "id": "rss:https://www.eetimes.com/delos-data-targets-heterogeneous-ai-with-data-interface/",
    "domain": "AI 算力 / 半导体",
    "title": "Delos Data Targets Heterogeneous AI with Data Interface",
    "url": "https://www.eetimes.com/delos-data-targets-heterogeneous-ai-with-data-interface/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T18:43:38+00:00",
    "summary": "Delos’s Apollo chiplet is designed to bridge different endpoint semantics and interconnects, creating a low-latency domain spanning GPUs, accelerators, CPUs and memory The post Delos Data Targets Hete"
  },
  {
    "id": "rss:https://www.eetimes.com/inside-tsmcs-evolving-design-ecosystem-shaping-the-future-of-ai-with-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "Inside TSMC’s Evolving Design Ecosystem: Shaping the Future of AI, with AI",
    "url": "https://www.eetimes.com/inside-tsmcs-evolving-design-ecosystem-shaping-the-future-of-ai-with-ai/",
    "source": "Aveek Sarkar, Director, Ecosystem and Alliance Management Division, TSMC",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T14:10:55+00:00",
    "summary": "TSMC shares updates about the Open Innovation Platform Ecosystem and vision for enabling AI-driven agentic workflows using TSMC AI Design Kit The post Inside TSMC’s Evolving Design Ecosystem: Shaping "
  },
  {
    "id": "rss:https://www.eetimes.com/after-ionq-buyout-skywater-reiterates-role-as-quantum-foundry/",
    "domain": "AI 算力 / 半导体",
    "title": "After IonQ Buyout, SkyWater Reiterates Role as Quantum Foundry",
    "url": "https://www.eetimes.com/after-ionq-buyout-skywater-reiterates-role-as-quantum-foundry/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T14:08:18+00:00",
    "summary": "As SkyWater scales its 200-mm and 300-mm manufacturing platforms to support diverse quantum modalities, leadership emphasizes that protecting customer IP remains its top priority. The post After IonQ "
  },
  {
    "id": "rss:https://www.eetimes.com/tis-october-price-hike-how-to-secure-adi-ti-stock-without-the-panic/",
    "domain": "AI 算力 / 半导体",
    "title": "TI’s October Price Hike: How to Secure ADI/TI Stock Without the Panic",
    "url": "https://www.eetimes.com/tis-october-price-hike-how-to-secure-adi-ti-stock-without-the-panic/",
    "source": "Skyeast International Group Limited",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T10:23:24+00:00",
    "summary": "acing TI's October price hike? SKYEAST offers $30M+ ADI/TI spot stock, 2-hour quotes, and 7×24 support across time zones. Lock in supply now. The post TI&#8217;s October Price Hike: How to Secure ADI/"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/elon-musks-spacexai-to-add-another-660-000-ai-gpus-this-year-nearing-a-total-of-1-44-million-in-operation-firm-is-building-1-2-gigawatt-power-plant-to-bring-systems-fully-online",
    "domain": "AI 算力 / 半导体",
    "title": "Elon Musk's SpaceXAI to add another 660,000 AI GPUs this year, nearing a total of 1.44 million in operation",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/elon-musks-spacexai-to-add-another-660-000-ai-gpus-this-year-nearing-a-total-of-1-44-million-in-operation-firm-is-building-1-2-gigawatt-power-plant-to-bring-systems-fully-online",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T15:40:00+00:00",
    "summary": "Elon Musk says that the Colossus 2 will receive 220,000 GB300 GPUs by next week, with another two tranches of the same amount expected to arrive later this year. This will put the site at over a milli"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/photonics/tower-semiconductor-to-invest-usd4-billion-in-japanese-ops-to-set-up-massive-optical-connectivity-hub-dual-track-expansion-aims-to-increase-output-by-40-times-by-2029",
    "domain": "AI 算力 / 半导体",
    "title": "Tower Semiconductor to invest $4 billion in Japanese ops to set up massive optical connectivity hub",
    "url": "https://www.tomshardware.com/tech-industry/photonics/tower-semiconductor-to-invest-usd4-billion-in-japanese-ops-to-set-up-massive-optical-connectivity-hub-dual-track-expansion-aims-to-increase-output-by-40-times-by-2029",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T15:00:22+00:00",
    "summary": "Tower's new optical connectivity hub in Japan will increase its output by 40 times in 2029 compared to 2025 level."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/meta-muse-runs-agents-on-amd-epyc-turin-hosts-with-two-cores-and-8gb-of-memory-ai-agent-can-pass-terminal-commands-to-ubuntu-host-system",
    "domain": "AI 算力 / 半导体",
    "title": "Meta Muse runs agents on AMD EPYC Turin hosts with two cores and 8GB of memory",
    "url": "https://www.tomshardware.com/pc-components/cpus/meta-muse-runs-agents-on-amd-epyc-turin-hosts-with-two-cores-and-8gb-of-memory-ai-agent-can-pass-terminal-commands-to-ubuntu-host-system",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T14:56:36+00:00",
    "summary": "Meta's new Muse AI agent is powered by AMD EPYC Turin hosts, with each user getting a private sandbox with two vCPUs and 8GB of memory."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/air-cooling/noctua-explores-2-000w-micro-channel-air-cooling-partners-with-forced-physics-to-develop-vacuum-pump-level-airflow-for-desktop-pcs",
    "domain": "AI 算力 / 半导体",
    "title": "Noctua explores 2,000W micro-channel air cooling",
    "url": "https://www.tomshardware.com/pc-components/air-cooling/noctua-explores-2-000w-micro-channel-air-cooling-partners-with-forced-physics-to-develop-vacuum-pump-level-airflow-for-desktop-pcs",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T14:42:58+00:00",
    "summary": "Noctua and Forced Physics are exploring whether densely packed micro-channels can provide extreme cooling performance without the noise associated with high-pressure airflow"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/save-usd250-on-this-award-winning-elegoo-resin-3d-printer-with-an-integrated-heater-and-16k-resolution-39-percent-discount-on-the-saturn-4-ultra-16k-gets-you-a-hugely-accurate-printer-with-fast-speeds-and-a-tilt-release-vat",
    "domain": "AI 算力 / 半导体",
    "title": "Save $250 on this award-winning Elegoo resin 3D printer with an integrated heater and 16K resolution",
    "url": "https://www.tomshardware.com/3d-printing/save-usd250-on-this-award-winning-elegoo-resin-3d-printer-with-an-integrated-heater-and-16k-resolution-39-percent-discount-on-the-saturn-4-ultra-16k-gets-you-a-hugely-accurate-printer-with-fast-speeds-and-a-tilt-release-vat",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T13:33:16+00:00",
    "summary": "This Elegoo Saturn 4 Ultra, one of the best resin 3D printers you can buy, is on sale for $359 right now, saving you 40% on its usual price."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/laptop-maker-says-ddr5-so-dimms-are-6x-pricier-than-last-year-schenker-says-other-component-costs-are-rising-too-announces-price-hikes",
    "domain": "AI 算力 / 半导体",
    "title": "DDR5 laptop memory prices surge 6X in 12 months",
    "url": "https://www.tomshardware.com/laptops/laptop-maker-says-ddr5-so-dimms-are-6x-pricier-than-last-year-schenker-says-other-component-costs-are-rising-too-announces-price-hikes",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T13:00:00+00:00",
    "summary": "XMG noted that SO-DIMM prices have jumped 6x, with other components like PCBs, CPUs, and GPUs also facing increasing costs. This has forced the niche laptop manufacturer to bump their SRPs between $11"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/gamemax-rgb-pro-750g-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "Gamemax RGB PRO 750G power supply review: Efficient, but pricey for an average unit with pretty lights",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/gamemax-rgb-pro-750g-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T13:00:00+00:00",
    "summary": "Gamemax charges $105 for an average power supply with RGB lighting. The Sohoo platform underneath measures well enough, but the fan, the capacitors, and the warranty all sit below what the price shoul"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/nintendo-wins-usd4-5-million-lawsuit-against-switch-pirate-by-default-defendant-allegedly-moderated-r-switchpirates-and-sold-pirated-switch-games",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo wins $4.5 million lawsuit against Switch pirate by default",
    "url": "https://www.tomshardware.com/video-games/nintendo/nintendo-wins-usd4-5-million-lawsuit-against-switch-pirate-by-default-defendant-allegedly-moderated-r-switchpirates-and-sold-pirated-switch-games",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T12:26:21+00:00",
    "summary": "A Washington court granted Nintendo of America a $4.5 million default judgment after the defendant failed to appear in court and respond to the allegations. The company claimed that it sent a cease-an"
  },
  {
    "id": "rss:https://www.tomshardware.com/tablets/microsoft-surface/microsoft-revamps-copilot-with-new-tools-support-for-frontier-models-available-now-through-frontier-program",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft revamps Copilot with new tools, support for frontier models",
    "url": "https://www.tomshardware.com/tablets/microsoft-surface/microsoft-revamps-copilot-with-new-tools-support-for-frontier-models-available-now-through-frontier-program",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T12:00:00+00:00",
    "summary": "Microsoft is revamping Copilot into a singular AI workspace, mixing your projects and agents together. It will also be able to support third-party frontier models."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/intel-expects-14a-to-be-within-5-percent-the-performance-of-tsmcs-a14-conservative-forecast-clashes-with-18as-frequency-lead-and-promised-20-percent-gains",
    "domain": "AI 算力 / 半导体",
    "title": "Intel expects 14A to be 'within 5%' the performance of TSMC's A14",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/intel-expects-14a-to-be-within-5-percent-the-performance-of-tsmcs-a14-conservative-forecast-clashes-with-18as-frequency-lead-and-promised-20-percent-gains",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T12:00:00+00:00",
    "summary": "Intel's Naga Chandrasekaran now claims that Intel 14A node will deliver performance 'within 5%' of TSMC's A14 technology, a claim that requires a closer examination."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cyber-security/asus-online-store-hit-by-data-breach-customer-contact-details-and-order-information-revealed",
    "domain": "AI 算力 / 半导体",
    "title": "Asus confirms eShop data breach exposed customer order records and contact details",
    "url": "https://www.tomshardware.com/tech-industry/cyber-security/asus-online-store-hit-by-data-breach-customer-contact-details-and-order-information-revealed",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T11:30:00+00:00",
    "summary": "Asus eShop hit by data breach — customer contact details and order information revealed"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/new-jersey-fines-data-center-for-using-unpermitted-power-generators-microsoft-linked-site-also-in-trouble-with-community-for-noise-pollution-other-issues",
    "domain": "AI 算力 / 半导体",
    "title": "New Jersey hits Microsoft-linked AI data center with record fine for 62 unpermitted power generators, issues 45-day shutdown deadline",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/new-jersey-fines-data-center-for-using-unpermitted-power-generators-microsoft-linked-site-also-in-trouble-with-community-for-noise-pollution-other-issues",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T11:00:00+00:00",
    "summary": "The DataOne data center is facing a record fine of $1.07 million for operating portable turbine generators without permission. Residents say that the penalty is a drop in the bucket for these big tech"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/grab-this-4k-ready-rtx-5070-ti-gaming-pc-from-hp-for-under-usd1-900-right-now-powerful-omen-35l-machine-is-a-serious-bargain-with-a-20-core-intel-cpu-32gb-ddr5-ram-and-a-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Grab this 4K-ready RTX 5070 Ti gaming PC from HP for under $1,900 right now",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/grab-this-4k-ready-rtx-5070-ti-gaming-pc-from-hp-for-under-usd1-900-right-now-powerful-omen-35l-machine-is-a-serious-bargain-with-a-20-core-intel-cpu-32gb-ddr5-ram-and-a-1tb-ssd",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T10:51:36+00:00",
    "summary": "This epic HP Omen 45L gaming rig is one of the cheapest RTX 5070 Ti PC you can buy right now, fitted with a Intel Core i7-14700F, 32GB of DDR RAM, and a 1TB SSD for just $1,899.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-dlss-5-upscales-frame-rates-and-flame-temps-on-16-pin-power-connector-ai-gaming-tech-pushes-connector-to-uncomfortable-thermal-and-power-limits",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia DLSS 5 power draw hits 647W as power connector runs hotter than the GPU die, upscales frame rates and flame temps on 16-pin",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-dlss-5-upscales-frame-rates-and-flame-temps-on-16-pin-power-connector-ai-gaming-tech-pushes-connector-to-uncomfortable-thermal-and-power-limits",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T10:30:00+00:00",
    "summary": "QuasarZone tests show the 16-pin power connector on a GeForce RTX 5090 reaches temperatures above 90 degrees Celsius at peak power consumption near 650W."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/google-is-blasting-an-experimental-ai-data-center-into-orbit-first-satellite-will-feature-just-four-tensor-processing-units",
    "domain": "AI 算力 / 半导体",
    "title": "Google's orbital AI data center test packs four TPUs and 1,000W of solar power",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/google-is-blasting-an-experimental-ai-data-center-into-orbit-first-satellite-will-feature-just-four-tensor-processing-units",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T10:00:00+00:00",
    "summary": "Google will launch an experimental satellite into orbit on October 1, taking four tensor processing units with it."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/australian-pm-says-openai-took-84-days-to-email-agency-after-agent-hacked-its-national-health-care-portal-incident-is-believed-to-be-the-first-known-case-of-ai-breaching-a-government-site",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI agent got into Australia's Medicare stats portal with 84-day notification delay",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/australian-pm-says-openai-took-84-days-to-email-agency-after-agent-hacked-its-national-health-care-portal-incident-is-believed-to-be-the-first-known-case-of-ai-breaching-a-government-site",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T20:34:31+00:00",
    "summary": "Australia says an OpenAI agent got past blocks on a Medicare statistics portal in June. OpenAI's notification arrived in September."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/console-gaming/sony-patent-could-turn-playstation-controllers-into-tap-to-pay-credit-card-terminals-nfc-and-bluetooth-also-support-phones-and-gift-cards-for-instant-purchases",
    "domain": "AI 算力 / 半导体",
    "title": "Sony patent could turn PlayStation controllers into tap-to-pay credit card terminals",
    "url": "https://www.tomshardware.com/video-games/console-gaming/sony-patent-could-turn-playstation-controllers-into-tap-to-pay-credit-card-terminals-nfc-and-bluetooth-also-support-phones-and-gift-cards-for-instant-purchases",
    "source": "Oliver Haslam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T17:09:31+00:00",
    "summary": "A new patent application details the potential for a future PlayStation controller to accept payments via credit cards and gift cards."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/nvidia-ceo-says-we-have-to-shut-the-labs-down-if-ai-experiments-are-unsafe-jensen-huang-says-frontier-ai-lab-fears-are-a-distraction-not-a-call-for-regulation",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia CEO says 'we have to shut the labs down' if AI experiments are unsafe",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/nvidia-ceo-says-we-have-to-shut-the-labs-down-if-ai-experiments-are-unsafe-jensen-huang-says-frontier-ai-lab-fears-are-a-distraction-not-a-call-for-regulation",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T15:24:49+00:00",
    "summary": "In a recent interview, Nvidia CEO Jensen Huang said that if frontier labs have unsafe models, they should shut the labs down, calling the current calls for regulation a \"distraction.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/japanese-used-bookstores-see-5x-sales-surge-as-books-are-being-bought-by-the-ton-one-50-ton-order-sent-to-the-us-for-ai-scanning-and-destruction-multitude-of-suspicious-bulk-buys-thought-to-end-up-in-foreign-ai-scan-and-shred-facilities",
    "domain": "AI 算力 / 半导体",
    "title": "Japanese used bookstores see 5x sales surge as books are being bought by the ton, one 50-ton order sent to the US for AI scanning and destruction",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/japanese-used-bookstores-see-5x-sales-surge-as-books-are-being-bought-by-the-ton-one-50-ton-order-sent-to-the-us-for-ai-scanning-and-destruction-multitude-of-suspicious-bulk-buys-thought-to-end-up-in-foreign-ai-scan-and-shred-facilities",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T14:35:12+00:00",
    "summary": "Investigators reckon Japan's used bookstore boom is likely due to the written-word harvesting of foreign AI giants."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/microphones/logitech-refreshes-legendary-blue-yeti-microphone-with-3d-voice-tracking-and-ai-denoising-usd160-blue-yeti-2-sequel-features-real-time-auto-gain-and-color-mascot-screen",
    "domain": "AI 算力 / 半导体",
    "title": "Logitech refreshes legendary Blue Yeti microphone with 3D voice tracking and AI denoising",
    "url": "https://www.tomshardware.com/peripherals/microphones/logitech-refreshes-legendary-blue-yeti-microphone-with-3d-voice-tracking-and-ai-denoising-usd160-blue-yeti-2-sequel-features-real-time-auto-gain-and-color-mascot-screen",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T14:00:00+00:00",
    "summary": "After years without a major successor, Logitech’s Yeti 2 arrives with new features designed to simplify microphone setup and audio adjustments."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/the-three-pronged-future-of-custom-pc-building-from-repurposing-forgotten-parts-to-ultra-premium-works-of-gaming-art",
    "domain": "AI 算力 / 半导体",
    "title": "The three-pronged future of custom PC building — from repurposing forgotten parts to ultra-premium works of gaming art",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/the-three-pronged-future-of-custom-pc-building-from-repurposing-forgotten-parts-to-ultra-premium-works-of-gaming-art",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T13:30:00+00:00",
    "summary": "This is probably the worst time ever for PC building. Here’s how and why I think the hobby (and the market) still have a future to look forward to."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/leading-semiconductor-analyst-accuses-amd-of-treason-over-restricted-chips-availability-in-china-amd-blames-diversion-of-export-controlled-rfsoc-usd36-000-radar-silicon-allegedly-quoted-at-usd1-000-for-crowdfunding-project",
    "domain": "AI 算力 / 半导体",
    "title": "Leading semiconductor analyst says AMD should be investigated for 'treason' over availability of restricted chips in China",
    "url": "https://www.tomshardware.com/tech-industry/leading-semiconductor-analyst-accuses-amd-of-treason-over-restricted-chips-availability-in-china-amd-blames-diversion-of-export-controlled-rfsoc-usd36-000-radar-silicon-allegedly-quoted-at-usd1-000-for-crowdfunding-project",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T13:00:44+00:00",
    "summary": "Top semiconductor analysis firm accuses AMD of treason, AMD says it could have been 'diversion' of an export-controlled adaptable radio platform."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/air-cooling/deepcool-ak620-and-ak400-g2-review",
    "domain": "AI 算力 / 半导体",
    "title": "GMKtec Evo-X3 review: Strix Halo in a brand new suit",
    "url": "https://www.tomshardware.com/pc-components/air-cooling/deepcool-ak620-and-ak400-g2-review",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T13:00:00+00:00",
    "summary": "GMKtec has radically remodeled its AMD Strix Halo flagship AI mini PC. The statuesque redesign looks more premium and stays cool and quiet, but the Evo-X3 is around twice the price of the Evo-X2, with"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd149-on-this-3-item-gaming-combo-from-newegg-usd1-050-buys-a-ryzen-7-9800x3d-32gb-of-corsair-ddr5-ram-asus-tuf-gaming-x870e-plus-motherboard-and-a-free-240mm-aio-and-amd-game-bundle",
    "domain": "AI 算力 / 半导体",
    "title": "Save $149 on this 3-item gaming combo from Newegg",
    "url": "https://www.tomshardware.com/pc-components/save-usd149-on-this-3-item-gaming-combo-from-newegg-usd1-050-buys-a-ryzen-7-9800x3d-32gb-of-corsair-ddr5-ram-asus-tuf-gaming-x870e-plus-motherboard-and-a-free-240mm-aio-and-amd-game-bundle",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T12:45:00+00:00",
    "summary": "Fight back against the RAMpocolypse with this 3-item Newegg combo that features the Ryzen 7 9800X3D, 32GB Corsair Vengeance RAM, and Asus TUF X870E motherboard for only $1,050, a $149 savings"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/micron-discontinues-2gb-gddr7-chips-for-gaming-gpus-as-it-pivots-toward-higher-density-memory-for-ai-chipmaker-reportedly-pivots-to-high-margin-3gb-silicon-for-ai-gpus",
    "domain": "AI 算力 / 半导体",
    "title": "Micron discontinues 2GB GDDR7 chips for gaming GPUs as it pivots toward higher-density memory for AI",
    "url": "https://www.tomshardware.com/pc-components/ram/micron-discontinues-2gb-gddr7-chips-for-gaming-gpus-as-it-pivots-toward-higher-density-memory-for-ai-chipmaker-reportedly-pivots-to-high-margin-3gb-silicon-for-ai-gpus",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T12:30:00+00:00",
    "summary": "Micron is reportedly ending production of its 2GB GDDR7 chips, shifting attention toward higher-density 3GB parts used in more lucrative professional and AI-focused GPUs."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand",
    "domain": "AI 算力 / 半导体",
    "title": "ASML says it sold 'absolutely nothing' in Europe in 2026",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T12:10:00+00:00",
    "summary": "ASML calls EU authorities to help create demand for European chips as Europe's share in its revenue drops to 0% in 2026."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/lucky-3d-artist-scores-jensen-huang-signed-rtx-5090-from-used-marketplace-unused-asus-rog-astra-white-oc-expected-to-fetch-usd10-000-to-usd15-000-at-auction",
    "domain": "AI 算力 / 半导体",
    "title": "Lucky 3D artist scores Jensen Huang-signed RTX 5090 from used marketplace that's worth up to $15,000",
    "url": "https://www.tomshardware.com/pc-components/gpus/lucky-3d-artist-scores-jensen-huang-signed-rtx-5090-from-used-marketplace-unused-asus-rog-astra-white-oc-expected-to-fetch-usd10-000-to-usd15-000-at-auction",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T11:50:00+00:00",
    "summary": "A 3D artist looking to build a new workstation bought this RTX 5090 off of a used marketplace expecting a unit autographed by an Asus executive. But when they opened the box of the GPU, they were surp"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/china-swiped-f-35-stealth-fighter-parts-that-were-diverted-through-hong-kong-rerouted-ups-cargo-triggers-military-investigation-stealth-coating-recipe-feared-compromised-despite-pentagon-downplaying-mishap",
    "domain": "AI 算力 / 半导体",
    "title": "China swiped classified F-35 stealth fighter parts that were diverted through Hong Kong",
    "url": "https://www.tomshardware.com/tech-industry/china-swiped-f-35-stealth-fighter-parts-that-were-diverted-through-hong-kong-rerouted-ups-cargo-triggers-military-investigation-stealth-coating-recipe-feared-compromised-despite-pentagon-downplaying-mishap",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T11:40:00+00:00",
    "summary": "Components from the one of the free world’s most advanced fighter jets are now in the possession of the Chinese, say reports."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/wici-one-unveils-wireless-wi-fi-7-egpu-with-built-in-4tb-ssd-for-local-ai-usd1-999-box-leverages-wifi-7-to-present-a-remote-card-as-local",
    "domain": "AI 算力 / 半导体",
    "title": "New wireless Wi-Fi 7 external GPU box comes with a built-in 4TB SSD for local AI",
    "url": "https://www.tomshardware.com/pc-components/gpus/wici-one-unveils-wireless-wi-fi-7-egpu-with-built-in-4tb-ssd-for-local-ai-usd1-999-box-leverages-wifi-7-to-present-a-remote-card-as-local",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T11:25:00+00:00",
    "summary": "WiCi wireless external GPU with onboard storage puts AI workloads reach of local machines via WiFi 7."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/chinas-ultimate-gaming-gpu-hits-a-performance-wall-lx-7g100-barely-crawls-past-amds-nine-year-old-rx-580",
    "domain": "AI 算力 / 半导体",
    "title": "China’s ultimate gaming GPU hits a performance wall",
    "url": "https://www.tomshardware.com/pc-components/gpus/chinas-ultimate-gaming-gpu-hits-a-performance-wall-lx-7g100-barely-crawls-past-amds-nine-year-old-rx-580",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T11:00:00+00:00",
    "summary": "The latest review of the Lisuan Tech LX 7G100 shows performance comparable to AMD's Radeon RX 580 but trails the GeForce RTX 2060."
  },
  {
    "id": "hn:49773511",
    "domain": "AI 算力 / 半导体",
    "title": "Every Nvidia GPU has 10 to 30 RISC-V cores inside it",
    "url": "https://www.xda-developers.com/your-nvidia-gpu-dozens-risc-v-cores-one-took-over-graphics-driver/",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 50,
    "published_at": "2026-09-20T07:50:58+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/semicon-india-2026-startup-mitra-sheds-light-on-early-stage-silicon-startup-funding/",
    "domain": "AI 算力 / 半导体",
    "title": "SEMICON India 2026: Startup Mitra Sheds Light on Early-Stage Silicon Startup Funding",
    "url": "https://www.eetimes.com/semicon-india-2026-startup-mitra-sheds-light-on-early-stage-silicon-startup-funding/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T08:15:06+00:00",
    "summary": "Indian semiconductor startups are seeking capital beyond seed rounds as they advance from prototypes and tape-out toward volume production. The post SEMICON India 2026: Startup Mitra Sheds Light on Ea"
  },
  {
    "id": "rss:https://www.eetimes.com/from-qubits-to-workflows-rethinking-quantum-computing/",
    "domain": "AI 算力 / 半导体",
    "title": "From Qubits to Workflows: Rethinking Quantum Computing",
    "url": "https://www.eetimes.com/from-qubits-to-workflows-rethinking-quantum-computing/",
    "source": "Kevin Hein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T19:00:00+00:00",
    "summary": "IBM’s quantum-centric push makes QPUs another accelerator in hybrid AI-HPC workflows. The post From Qubits to Workflows: Rethinking Quantum Computing appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/semicon-india-2026-india-starts-packaging-chips-as-ecosystem-takes-shape/",
    "domain": "AI 算力 / 半导体",
    "title": "SEMICON India 2026: India Starts Packaging Chips as Ecosystem Takes Shape",
    "url": "https://www.eetimes.com/semicon-india-2026-india-starts-packaging-chips-as-ecosystem-takes-shape/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T10:56:15+00:00",
    "summary": "India moves five chip packaging plants into production as $13.5 billion ISM 2.0 expands manufacturing, design, and engineering capabilities. The post SEMICON India 2026: India Starts Packaging Chips a"
  },
  {
    "id": "rss:https://www.eetimes.com/smarter-buildings-safer-occupants-intelligence-meets-privacy/",
    "domain": "AI 算力 / 半导体",
    "title": "Smarter Buildings, Safer Occupants: Intelligence Meets Privacy",
    "url": "https://www.eetimes.com/smarter-buildings-safer-occupants-intelligence-meets-privacy/",
    "source": "Anne-Françoise Pelé",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T08:05:07+00:00",
    "summary": "Modern building automation systems are designed to optimize energy efficiency while safeguarding the health, safety, and security of occupants. The post Smarter Buildings, Safer Occupants: Intelligenc"
  },
  {
    "id": "hn:49777694",
    "domain": "AI 算力 / 半导体",
    "title": "Autonomous strike drone uses Nvidia Jetson Orin Nano to pick and bomb targets",
    "url": "https://www.tomshardware.com/tech-industry/drones/autonomous-strike-drone-uses-nvidia-jetson-orin-nano-to-independently-pick-and-bomb-targets-swedish-startups-attack-drones-run-small-ai-model-require-no-human-input-and-zero-external-comms",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 29,
    "published_at": "2026-09-20T17:07:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49745610",
    "domain": "AI 算力 / 半导体",
    "title": "Run QWEN3.8 27B on 16gb Nvidia GPUs",
    "url": "https://github.com/MiaAI-Lab/Qwen3.8-27B-16gb-NVIDIA-GPUs-one-click-install",
    "source": "Pragmata",
    "platform": "hackernews",
    "points": 28,
    "published_at": "2026-09-17T19:46:57+00:00",
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
    "id": "hn:49727093",
    "domain": "AI 算力 / 半导体",
    "title": "Apple May Return to Server Market with Nvidia Technology",
    "url": "https://www.macrumors.com/2026/09/16/apple-may-return-to-server-market/",
    "source": "tosh",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-09-16T13:54:52+00:00",
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
    "id": "hn:49797982",
    "domain": "大厂 AI 动态",
    "title": "I said no and Apple said yes",
    "url": "https://dbushell.com/2026/09/22/apple-intelligence/",
    "source": "thatslast",
    "platform": "hackernews",
    "points": 876,
    "published_at": "2026-09-22T08:04:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611251",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas: a high-resolution map of human DNA",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/",
    "source": "utiiiD",
    "platform": "hackernews",
    "points": 607,
    "published_at": "2026-09-08T14:55:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49848269",
    "domain": "大厂 AI 动态",
    "title": "Ollaya – Ollama for open-source, Jev-style decision models",
    "url": "https://ollaya.dev/",
    "source": "Ardakilic",
    "platform": "hackernews",
    "points": 433,
    "published_at": "2026-09-25T18:33:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49715947",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Live and 3.8 Live Extended Thinking",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/",
    "source": "leumon",
    "platform": "hackernews",
    "points": 492,
    "published_at": "2026-09-15T17:38:18+00:00",
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
    "id": "hn:49817615",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 text-to-speech",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/",
    "source": "swolpers",
    "platform": "hackernews",
    "points": 330,
    "published_at": "2026-09-23T15:29:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:49790409",
    "domain": "大厂 AI 动态",
    "title": "Turn off and restrict access to Apple Intelligence features on Mac",
    "url": "https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac",
    "source": "alwillis",
    "platform": "hackernews",
    "points": 353,
    "published_at": "2026-09-21T17:30:21+00:00",
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
    "id": "hn:49829387",
    "domain": "大厂 AI 动态",
    "title": "Hackers influence ChatGPT and Gemini to direct users to scam centers",
    "url": "https://medium.com/@arielsimon/dark-sourcery-how-hackers-manipulate-ai-to-scam-you-88df434d2073",
    "source": "ArielSimon",
    "platform": "hackernews",
    "points": 141,
    "published_at": "2026-09-24T11:54:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49844896",
    "domain": "大厂 AI 动态",
    "title": "Microsoft abandons personal AI chatbot race with Copilot reboot",
    "url": "https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 120,
    "published_at": "2026-09-25T14:07:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49727659",
    "domain": "大厂 AI 动态",
    "title": "The DeepMind Institute",
    "url": "https://institute.deepmind.com/",
    "source": "vertigoruntime",
    "platform": "hackernews",
    "points": 186,
    "published_at": "2026-09-16T14:32:11+00:00",
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
    "id": "hn:49829472",
    "domain": "大厂 AI 动态",
    "title": "Fourier Analysis: Drawing Llamas with Circles",
    "url": "https://adekau.github.io/posts/2020/llamas.html",
    "source": "cebert",
    "platform": "hackernews",
    "points": 34,
    "published_at": "2026-09-24T12:03:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49762493",
    "domain": "大厂 AI 动态",
    "title": "Gemini hacked three companies in first known breakout by Google's AI",
    "url": "https://www.reuters.com/business/gemini-hacked-three-companies-first-known-breakout-by-google-ai-wsj-reports-2026-09-18/",
    "source": "usernomdeguerre",
    "platform": "hackernews",
    "points": 77,
    "published_at": "2026-09-19T01:40:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49740330",
    "domain": "大厂 AI 动态",
    "title": "I had Gemini train its own replacement for $9",
    "url": "https://www.petervijeh.com/projects/reddit-ner",
    "source": "p-s-v",
    "platform": "hackernews",
    "points": 88,
    "published_at": "2026-09-17T13:17:16+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/transportation/999785/amflow-tl-review-avinox-esuv-e-bike-avinox",
    "domain": "大厂 AI 动态",
    "title": "Can &#8216;eSUV&#8217; e-bikes really go from trail to town?",
    "url": "https://www.theverge.com/transportation/999785/amflow-tl-review-avinox-esuv-e-bike-avinox",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T07:00:00+00:00",
    "summary": "Have you ever wanted an electric bike that easily transitions from the drudgery of urban asphalt to adventures in gravel and dirt? That's what a subclass of so-called \"electric SUV\" (eSUV) e-bikes cla"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1000859/roku-pro-series-oled-nothing-phone-4a-pro-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Roku&#8217;s first OLED TVs are up to $400 off, starting at $699",
    "url": "https://www.theverge.com/gadgets/1000859/roku-pro-series-oled-nothing-phone-4a-pro-deal-sale",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T18:18:57+00:00",
    "summary": "Roku recently launched its first-ever OLED TVs. The $999 starting price was already impressive for the 55-inch Pro Series model that has a 120Hz refresh rate OLED panel (with four HDMI 2.1 ports and s"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/1000751/vergecast-meta-connect-muse-googlebooks",
    "domain": "大厂 AI 动态",
    "title": "Phones don’t have lights",
    "url": "https://www.theverge.com/podcast/1000751/vergecast-meta-connect-muse-googlebooks",
    "source": "Jacob Kastrenakes",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:42:59+00:00",
    "summary": "Mark Zuckerberg has a new defense of the Ray-Ban Meta glasses: They're actually doing more to signal they're taking a photo than phones do. He's brought this up in at least two recent interviews, noti"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1000729/moment-pro-blackmagic-camera-ii-ios-app-iphone-18-pro-max-aperature-camera",
    "domain": "大厂 AI 动态",
    "title": "These camera apps give you more control over the iPhone 18 Pro’s aperture",
    "url": "https://www.theverge.com/tech/1000729/moment-pro-blackmagic-camera-ii-ios-app-iphone-18-pro-max-aperature-camera",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:23:30+00:00",
    "summary": "One of the questionable limitations of the iPhone 18 Pro's new main camera with a variable aperture is that you're limited to just four settings in the native iOS' camera app in manual mode: f/1.48, f"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1000794/tesla-optimus-production-issues-hands",
    "domain": "大厂 AI 动态",
    "title": "Tesla&#8217;s Optimus robot is going through growing pains",
    "url": "https://www.theverge.com/tech/1000794/tesla-optimus-production-issues-hands",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:01:36+00:00",
    "summary": "Hitting its goal of making 20,000 Optimus robots per week is reportedly proving tricky for Tesla. The Information reports that Tesla produced \"several hundred robots a week\" last month, after it repur"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1000784/meta-muse-filesystem",
    "domain": "大厂 AI 动态",
    "title": "Meta makes the Muse filesystem even more accessible",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1000784/meta-muse-filesystem",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T16:49:53+00:00",
    "summary": "Yesterday, with a little prodding, it was discovered that Meta's Muse would expose its filesystem to curious users. The files offered a fascinating peek under the hood of an AI chatbot, and appeared t"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1000772/apple-code-leak-homepod-mini-2-ipad-mini-8-apple-tv-4k",
    "domain": "大厂 AI 动态",
    "title": "Leaks reveal a new Apple HomePod mini, iPad mini, and Apple TV 4K",
    "url": "https://www.theverge.com/tech/1000772/apple-code-leak-homepod-mini-2-ipad-mini-8-apple-tv-4k",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T16:22:05+00:00",
    "summary": "Apple is expected to announce more hardware before the end of the year following the debut of the iPhone 18 Pro and folding iPhone Duo earlier this month. The updated products will include a new versi"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1000758/suno-sony-umg-lawsuit-ai-music",
    "domain": "大厂 AI 动态",
    "title": "Sony and UMG are suing Suno again",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1000758/suno-sony-umg-lawsuit-ai-music",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T15:51:56+00:00",
    "summary": "Sony and Universal Music Group filed yet another suit against Suno. The labels claim its new v6 model still infringes on their copyrights because it's trained on user outputs from previous models, whi"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1000644/irregular-rogue-ai-cyberattacks-hacking-openai-meta-anthropic-google",
    "domain": "大厂 AI 动态",
    "title": "One company is at the center of a wave of rogue AI attacks",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1000644/irregular-rogue-ai-cyberattacks-hacking-openai-meta-anthropic-google",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T15:39:48+00:00",
    "summary": "In July, OpenAI revealed that its AI agents had attacked Hugging Face without permission, sparking widespread concerns about AI safety. Since then, a string of similar incidents involving agents from "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1000655/cricut-sticker-pix-print-cut-crafting-printer-machines-stickers",
    "domain": "大厂 AI 动态",
    "title": "Cricut&#8217;s new compact crafter prints, cuts, and laminates stickers",
    "url": "https://www.theverge.com/tech/1000655/cricut-sticker-pix-print-cut-crafting-printer-machines-stickers",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T14:21:25+00:00",
    "summary": "Cricut announced its first crafting machines with printing capabilities that are primarily designed as all-in-one solutions for turning photos and other images into precut stickers. The Cricut Sticker"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/at-meta-connect-the-companys-smart-glasses-were-everywhere/",
    "domain": "大厂 AI 动态",
    "title": "At Meta Connect, the company’s smart glasses were everywhere",
    "url": "https://techcrunch.com/2026/09/25/at-meta-connect-the-companys-smart-glasses-were-everywhere/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-26T01:08:57+00:00",
    "summary": "The company behind Facebook and Instagram wants to keep consumers connected to the digital world via its ever-growing line of smart glasses."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/crusoe-abandons-1-25b-plan-to-use-boom-turbines-at-ai-data-centers/",
    "domain": "大厂 AI 动态",
    "title": "Crusoe abandons $1.25B plan to use Boom turbines at AI data centers",
    "url": "https://techcrunch.com/2026/09/25/crusoe-abandons-1-25b-plan-to-use-boom-turbines-at-ai-data-centers/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T23:11:10+00:00",
    "summary": "Boom Supersonic CEO Blake Scholl said the company's new stationary power plants were no longer in Crusoe's near-term plans."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/automattic-has-a-new-board-after-failed-attempt-to-put-ceo-on-leave/",
    "domain": "大厂 AI 动态",
    "title": "Automattic has a new board after failed attempt to put CEO on leave",
    "url": "https://techcrunch.com/2026/09/25/automattic-has-a-new-board-after-failed-attempt-to-put-ceo-on-leave/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T23:04:34+00:00",
    "summary": "After days of upheaval at Automattic, following a failed attempt to remove CEO Matt Mullenweg, the company has a new board."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/unsecured-openai-agents-posted-53-user-images-on-the-internet-without-the-labs-knowledge/",
    "domain": "大厂 AI 动态",
    "title": "Unsecured OpenAI agents posted 53 user images on the internet without the lab’s knowledge",
    "url": "https://techcrunch.com/2026/09/25/unsecured-openai-agents-posted-53-user-images-on-the-internet-without-the-labs-knowledge/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T22:20:47+00:00",
    "summary": "AI agents operating in OpenAI's research environment posted user images on public image-hosting sites without the lab's knowledge."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/meta-opens-early-access-program-for-new-muse-features/",
    "domain": "大厂 AI 动态",
    "title": "Meta opens early access program for new Muse features",
    "url": "https://techcrunch.com/2026/09/25/meta-opens-early-access-program-for-new-muse-features/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T20:34:53+00:00",
    "summary": "Anyone interested in joining has to ask Muse to put them on the list."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/the-hottest-new-hangout-for-middle-schoolers-is-nprs-comment-section/",
    "domain": "大厂 AI 动态",
    "title": "The hottest new hangout for middle schoolers is NPR’s comment section?",
    "url": "https://techcrunch.com/2026/09/25/the-hottest-new-hangout-for-middle-schoolers-is-nprs-comment-section/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T20:33:58+00:00",
    "summary": "When NPR staffers flagged strange comments under their podcasts on Spotify as bots, it took a Gen Z colleague to (immediately) figure out the mystery."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/anthropic-to-pay-akamai-11-6-billion-over-seven-years-in-cloud-deal/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic to pay Akamai $11.6 billion over seven years in cloud deal",
    "url": "https://techcrunch.com/2026/09/25/anthropic-to-pay-akamai-11-6-billion-over-seven-years-in-cloud-deal/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T19:13:38+00:00",
    "summary": "Anthropic has committed $11.6 billion over seven years to Akamai's cloud infrastructure, a bet on CPUs that could grow to about $20 billion, and in an unusual arrangement, Akamai is giving Anthropic a"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/mark-wahlberg-is-coming-to-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Mark Wahlberg is coming to TechCrunch Disrupt 2026, and he wants to talk about your work, not his",
    "url": "https://techcrunch.com/2026/09/25/mark-wahlberg-is-coming-to-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T18:48:33+00:00",
    "summary": "Mark Wahlberg joins Bruce K. Lee at Disrupt to discuss investing, entrepreneurship, healthcare, wellness, and building businesses."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/ahead-of-u-s-ipo-british-ai-neocloud-nscale-secures-3-36b-in-convertible-finacing/",
    "domain": "大厂 AI 动态",
    "title": "Ahead of US IPO, British AI neocloud Nscale secures $3.36B in convertible financing",
    "url": "https://techcrunch.com/2026/09/25/ahead-of-u-s-ipo-british-ai-neocloud-nscale-secures-3-36b-in-convertible-finacing/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T18:33:59+00:00",
    "summary": "The funding, which comes from Third Point, Nvidia, and others, will fuel the company's massive AI data center buildout."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/the-aeropod-automates-soil-aeration-without-robotics-see-it-at-techcrunch-disrupt/",
    "domain": "大厂 AI 动态",
    "title": "The Aeropod automates soil aeration without robotics — see it at TechCrunch Disrupt",
    "url": "https://techcrunch.com/2026/09/25/the-aeropod-automates-soil-aeration-without-robotics-see-it-at-techcrunch-disrupt/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:30:00+00:00",
    "summary": "Muju Earth Technologies has developed a deceptively simply pod that can save farmers money while improving crop yields."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/some-supabase-customers-are-publicly-exposing-reams-of-peoples-data-to-the-web/",
    "domain": "大厂 AI 动态",
    "title": "Some Supabase customers are publicly exposing reams of people’s data to the web",
    "url": "https://techcrunch.com/2026/09/25/some-supabase-customers-are-publicly-exposing-reams-of-peoples-data-to-the-web/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:29:46+00:00",
    "summary": "The findings highlight how AI-generated and vibe-coded apps can spill and expose users' data when not configured or secured properly."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/astra-and-opus-just-passed-turings-other-test/",
    "domain": "大厂 AI 动态",
    "title": "Astra and Opus just passed Turing’s other test",
    "url": "https://techcrunch.com/2026/09/25/astra-and-opus-just-passed-turings-other-test/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:24:36+00:00",
    "summary": "Frontier AI models are finishing Alan Turing's World War II codebreaking work."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/meta-is-putting-its-muscle-behind-muse-as-the-ai-app-takes-off/",
    "domain": "大厂 AI 动态",
    "title": "Meta is putting its muscle behind Muse as the AI app takes off",
    "url": "https://techcrunch.com/2026/09/25/meta-is-putting-its-muscle-behind-muse-as-the-ai-app-takes-off/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T16:16:52+00:00",
    "summary": "Muse is topping the app store charts and adding users at a rapid clip, while Meta ramps up the personal AI agent's promotion across its own apps and beyond."
  },
  {
    "id": "rss:https://techcrunch.com/video/will-metas-ai-tamagotchi-bet-isworking/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s AI Tamagotchi bet is…working?",
    "url": "https://techcrunch.com/video/will-metas-ai-tamagotchi-bet-isworking/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T16:00:00+00:00",
    "summary": "When AI leaders at OpenAI and Anthropic started talking about “pacing the frontier,”&#160;maybe someone&#160;should have asked: what pace?&#160;Now&#160;it’s&#160;turned into model drop week for both "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/kiteworks-urges-customers-to-shut-down-their-servers-amid-imminent-threat-of-cyberattack/",
    "domain": "大厂 AI 动态",
    "title": "Kiteworks urges customers to shut down their servers amid ‘imminent’ threat of cyberattack",
    "url": "https://techcrunch.com/2026/09/25/kiteworks-urges-customers-to-shut-down-their-servers-amid-imminent-threat-of-cyberattack/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T15:52:13+00:00",
    "summary": "The tech giant, which allows companies to send large datasets over the internet, said it received a \"credible threat\" from law enforcement about an imminent attack."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/for-months-openais-agent-swarms-have-been-attacking-online-databases-to-find-obscure-facts/",
    "domain": "大厂 AI 动态",
    "title": "For months, OpenAI’s agent swarms have been attacking online databases to find obscure facts",
    "url": "https://techcrunch.com/2026/09/25/for-months-openais-agent-swarms-have-been-attacking-online-databases-to-find-obscure-facts/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T15:48:14+00:00",
    "summary": "The latest unauthorized agent swarms were discovered by researchers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/anthropics-founders-seek-voting-control-ahead-of-ipo/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic’s founders seek voting control ahead of IPO",
    "url": "https://techcrunch.com/2026/09/25/anthropics-founders-seek-voting-control-ahead-of-ipo/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T15:40:03+00:00",
    "summary": "Anthropic is asking its shareholders to approve a structure that would give its seven co-founders a combined 50.1% of the vote on most corporate matters."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/tesla-finally-moves-to-electrify-trucking-after-a-decade-of-work-and-delays/",
    "domain": "大厂 AI 动态",
    "title": "Tesla finally moves to electrify trucking after a decade of work and delays",
    "url": "https://techcrunch.com/2026/09/25/tesla-finally-moves-to-electrify-trucking-after-a-decade-of-work-and-delays/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T15:24:50+00:00",
    "summary": "Tesla's Semi truck, with a 500-mile range, is about to hit the road in big numbers, with the company saying it plans to make 50,000 units a year."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/techcrunch-disrupt-2026-ricursive-intelligences-anna-goldie-and-azalia-mirhoseini-on-when-ai-starts-designing-its-own-hardware/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Disrupt 2026: Ricursive Intelligence’s Anna Goldie and Azalia Mirhoseini on when AI starts designing its own hardware",
    "url": "https://techcrunch.com/2026/09/25/techcrunch-disrupt-2026-ricursive-intelligences-anna-goldie-and-azalia-mirhoseini-on-when-ai-starts-designing-its-own-hardware/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T15:00:00+00:00",
    "summary": "At TechCrunch Disrupt 2026, Ricursive Intelligence co-founders Anna Goldie and Azalia Mirhoseini will take the Disrupt Stage to discuss closing the loop between AI and chip development. Save up to $20"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/25/disrupt-2026-layoff-expo-plus-passes-available-for-75-dollars/",
    "domain": "大厂 AI 动态",
    "title": "Affected by layoffs? Don’t miss this $75 deal for your TechCrunch Disrupt 2026 Expo+ Pass",
    "url": "https://techcrunch.com/2026/09/25/disrupt-2026-layoff-expo-plus-passes-available-for-75-dollars/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T14:15:00+00:00",
    "summary": "Your next opportunity could be one conversation away. Get your Expo+ Pass for just $75. Limited to the first 100 qualifying people."
  },
  {
    "id": "rss:https://stratechery.com/2026/begun-the-aggregator-wars-have/",
    "domain": "大厂 AI 动态",
    "title": "2026.39: Begun, the Aggregator Wars Have",
    "url": "https://stratechery.com/2026/begun-the-aggregator-wars-have/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:00:00+00:00",
    "summary": "The best Stratechery content from the week of September 21, 2026, including Meta vs. Amazon, GM bending the knee to CarPlay, and profiling the profiler."
  },
  {
    "id": "rss:https://stratechery.com/2026/an-interview-with-colossus-eic-jeremy-stern-about-profiling-mark-zuckerberg/",
    "domain": "大厂 AI 动态",
    "title": "An Interview with Colossus EIC Jeremy Stern About Profiling Mark Zuckerberg",
    "url": "https://stratechery.com/2026/an-interview-with-colossus-eic-jeremy-stern-about-profiling-mark-zuckerberg/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-24T10:00:00+00:00",
    "summary": "An interview with Colossus EIC Jeremy Stern about profiling Mark Zuckerberg and other prominent tech figures."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/can-trump-ever-be-wrong-his-pick-to-lead-fda-refused-to-say/",
    "domain": "大厂 AI 动态",
    "title": "Can Trump ever be wrong? His pick to lead FDA refused to say.",
    "url": "https://arstechnica.com/health/2026/09/can-trump-ever-be-wrong-his-pick-to-lead-fda-refused-to-say/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T23:00:26+00:00",
    "summary": "Heidi Overton faced questions focused on vaccines, birth control, and vapes."
  },
  {
    "id": "hn:49691343",
    "domain": "股票",
    "title": "Nike exits the S&P 100 after 18 years and a $200B market-cap wipeout",
    "url": "https://fortune.com/2026/09/08/nike-stock-plummets-sp500-market-cap-index/",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 316,
    "published_at": "2026-09-14T02:50:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:49619848",
    "domain": "股票",
    "title": "Apple iPod Engraver (2019)",
    "url": "https://dunstanorchard.com/apple-ipod-engraver/",
    "source": "NaOH",
    "platform": "hackernews",
    "points": 288,
    "published_at": "2026-09-09T01:57:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49712746",
    "domain": "股票",
    "title": "Global bond yields hit 2008 highs, raising stakes for big borrowers",
    "url": "https://www.reuters.com/world/asia-pacific/bond-selloff-drives-us-benchmark-beyond-5-stocks-rattled-2026-09-15/",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 167,
    "published_at": "2026-09-15T14:07:01+00:00",
    "summary": ""
  },
  {
    "id": "hn:49611240",
    "domain": "股票",
    "title": "iPod Classic 6G in QEMU",
    "url": "https://www.reddit.com/r/emulation/s/VL4Au2HGxq",
    "source": "dmonterocrespo",
    "platform": "hackernews",
    "points": 162,
    "published_at": "2026-09-08T14:54:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49791944",
    "domain": "股票",
    "title": "Wall Street is growing skeptical of the data center boom",
    "url": "https://www.nytimes.com/2026/09/21/business/ai-data-center-ipos.html",
    "source": "mikhael",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-09-21T19:14:30+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.netinterest.co/p/the-agents-revolt",
    "domain": "股票",
    "title": "The Agents Revolt",
    "url": "https://www.netinterest.co/p/the-agents-revolt",
    "source": "Marc Rubinstein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-25T17:33:27+00:00",
    "summary": "What happens to finance when customers start paying attention"
  },
  {
    "id": "hn:49816810",
    "domain": "股票",
    "title": "Trump's 1,156 July Stock Trades Involved AI, Big Oil, Weapons-Makers, and More",
    "url": "https://www.commondreams.org/news/donald-trump-stock-trades",
    "source": "cirelli94",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-23T14:33:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49819274",
    "domain": "股票",
    "title": "Morgan Stanley Investment-Bank Deal List Leaked in Email Misfire",
    "url": "https://finance.yahoo.com/markets/stocks/articles/morgan-stanley-investment-bank-deal-124657863.html",
    "source": "wslh",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-09-23T17:08:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49810905",
    "domain": "股票",
    "title": "In 2025, 49 percent of adults under age 30 lived with a parent [pdf]",
    "url": "https://www.federalreserve.gov/publications/files/2025-report-economic-well-being-us-households-202605.pdf",
    "source": "gscott",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-09-23T02:26:49+00:00",
    "summary": ""
  },
  {
    "id": "hn:49796292",
    "domain": "股票",
    "title": "Smart Ring Maker Oura, Backers Seek $2.2B in US IPO",
    "url": "https://www.bloomberg.com/news/articles/2026-09-21/smart-ring-maker-oura-backers-seek-2-2-billion-in-us-ipo",
    "source": "elo2000",
    "platform": "hackernews",
    "points": 24,
    "published_at": "2026-09-22T02:53:48+00:00",
    "summary": ""
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
    "id": "hn:49682946",
    "domain": "股票",
    "title": "Show HN: Analyst Index – analysts who make money telling you good stock calls",
    "url": "https://www.analystidx.com/",
    "source": "haichuan",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-09-13T11:50:35+00:00",
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
    "id": "hn:49696420",
    "domain": "股票",
    "title": "Global AI stocks fall as industry chiefs call for slowing development",
    "url": "https://www.reuters.com/world/china/ai-linked-asian-stocks-slump-after-top-lab-ceos-call-slowing-down-technologys-2026-09-14/",
    "source": "1vuio0pswjnm7",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-09-14T13:21:51+00:00",
    "summary": ""
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
    "id": "hn:49778029",
    "domain": "金融",
    "title": "Samsung is expected to more than double output of its HBM4 and HBM4E DRAM",
    "url": "https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 561,
    "published_at": "2026-09-20T17:38:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49686766",
    "domain": "金融",
    "title": "I'm being cyberattacked by Tesla, Inc",
    "url": "https://dreamstation.systems/personal/tesla.html",
    "source": "robinpie",
    "platform": "hackernews",
    "points": 458,
    "published_at": "2026-09-13T18:03:09+00:00",
    "summary": ""
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
    "id": "hn:49822556",
    "domain": "金融",
    "title": "OpenAI breaches Medicare, Albanese reveals",
    "url": "https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html",
    "source": "jonnonz",
    "platform": "hackernews",
    "points": 254,
    "published_at": "2026-09-23T21:01:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49704008",
    "domain": "金融",
    "title": "Amazon vs. Perplexity – U.S. Court of Appeals for the Ninth Circuit",
    "url": "https://law.justia.com/cases/federal/appellate-courts/ca9/26-1444/26-1444-2026-08-04.html",
    "source": "neom",
    "platform": "hackernews",
    "points": 219,
    "published_at": "2026-09-14T21:05:22+00:00",
    "summary": ""
  },
  {
    "id": "hn:49832844",
    "domain": "金融",
    "title": "Federal judge orders Texas to air condition all prisons by the end of 2029",
    "url": "https://www.texastribune.org/2026/09/22/texas-prison-air-conditioning-lawsuit-ruling/",
    "source": "bonefishgrill",
    "platform": "hackernews",
    "points": 115,
    "published_at": "2026-09-24T16:15:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49731356",
    "domain": "金融",
    "title": "Fed hikes rates as inflation worries push up bond yields",
    "url": "https://www.reuters.com/live/live-fed-rate-hike-expected-inflation-worries-push-up-bond-yields-2026-09-16/",
    "source": "wslh",
    "platform": "hackernews",
    "points": 184,
    "published_at": "2026-09-16T18:55:21+00:00",
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
    "id": "hn:49694840",
    "domain": "金融",
    "title": "How Much Has Trump Made from Crypto? ($1.4B from 2025 Federal Disclosure)",
    "url": "https://www.thepricer.org/how-much-has-trump-made-from-crypto/",
    "source": "cinderelacinder",
    "platform": "hackernews",
    "points": 114,
    "published_at": "2026-09-14T10:56:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49591672",
    "domain": "金融",
    "title": "Hackers have withdrawn ~4k BTC (~$320M) from the Liquid Federation wallet",
    "url": "https://twitter.com/Liquid_BTC/status/2096696272447218108",
    "source": "felipelalli",
    "platform": "hackernews",
    "points": 126,
    "published_at": "2026-09-06T22:43:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49828019",
    "domain": "金融",
    "title": "Show HN: Trader News – Hacker News for Finance",
    "url": "https://news.ycombinator.com/item?id=49828019",
    "source": "FailMore",
    "platform": "hackernews",
    "points": 23,
    "published_at": "2026-09-24T08:54:57+00:00",
    "summary": ""
  },
  {
    "id": "hn:49849986",
    "domain": "金融",
    "title": "Show HN: Ekselio – Loveable for finance workflows (local first)",
    "url": "https://www.gptbeyond.com/try?home=1",
    "source": "kdautaj",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-09-25T21:09:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:49596610",
    "domain": "金融",
    "title": "Initial effects of AI technology on employment look positive",
    "url": "https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here",
    "source": "MrBuddyCasino",
    "platform": "hackernews",
    "points": 103,
    "published_at": "2026-09-07T10:38:32+00:00",
    "summary": ""
  },
  {
    "id": "hn:49700413",
    "domain": "金融",
    "title": "US 10-Year Breaches 5% as Inflation, Supply Worries Mount",
    "url": "https://www.bloomberg.com/news/articles/2026-09-14/us-10-year-yield-breaches-5-as-inflation-supply-worries-mount",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-09-14T17:11:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49730769",
    "domain": "金融",
    "title": "Feds Want California to Give Up 14 Years of Broadband Protections. It Should Sue",
    "url": "https://cyberlaw.stanford.edu/blog/2026/09/california-is-being-asked-to-give-up-14-years-of-broadband-protections-it-doesnt-have-to/",
    "source": "rsingel",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-09-16T18:09:36+00:00",
    "summary": ""
  },
  {
    "id": "hn:49762617",
    "domain": "金融",
    "title": "Elon Musk and Tesla Forged a New EV Path",
    "url": "https://spectrum.ieee.org/elon-musk-tesla",
    "source": "vinhnx",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-09-19T02:08:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49612981",
    "domain": "金融",
    "title": "DOJ Blocked ICE Agent Shooting Charge over Federal Prosecutor's Objections",
    "url": "https://www.propublica.org/article/doj-blocks-charges-ice-agent-minneapolis-julio-cesar-sosa-celis",
    "source": "paimapi",
    "platform": "hackernews",
    "points": 56,
    "published_at": "2026-09-08T16:54:03+00:00",
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
    "id": "hn:49731515",
    "domain": "金融",
    "title": "Fed Raises Rates for First Time in Three Years",
    "url": "https://www.wsj.com/economy/central-banking/fed-raises-rates-for-first-time-in-three-years-08539fbe",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 25,
    "published_at": "2026-09-16T19:09:22+00:00",
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
    "id": "hn:49730731",
    "domain": "金融",
    "title": "Fed Raises Rates as Warsh Bucks Trump to Contain Inflation",
    "url": "https://www.bloomberg.com/news/articles/2026-09-16/fed-raises-rates-as-warsh-bucks-trump-to-contain-inflation",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-09-16T18:05:30+00:00",
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
    "id": "rss:https://semianalysis.com/2025/09/16/xais-colossus-2-first-gigawatt-datacenter/",
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
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
    "domain": "电子信息与芯片",
    "title": "Meta Superintelligence – Leadership Compute, Talent, and Data",
    "url": "https://semianalysis.com/2025/07/11/meta-superintelligence-leadership-compute-talent-and-data/",
    "source": "Dylan Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2025-07-11T20:12:19+00:00",
    "summary": "Meta’s shocking purchase of 49% of Scale AI at a ~$30B valuation shows that money is of no concern for the $100B annual cashflow ad machine. Despite seemingly unlimited resources, Meta has been fallin"
  }
]
```
