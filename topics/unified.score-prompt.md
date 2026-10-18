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

- 今日日期：`2026-10-18`
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
  "date": "2026-10-18",
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
    "points": 2109962,
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
    "points": 1988098,
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
    "points": 1618826,
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
    "points": 1408793,
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
    "points": 1356453,
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
    "points": 1217630,
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
    "points": 946663,
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
    "points": 900990,
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
    "points": 859361,
    "published_at": "2026-07-01T02:00:00+00:00",
    "summary": "本套视频教程所有配套资料领取方式如下：\n关注黑马程序员公 粽 号，回复关键词：260701\n【AI大模型学习路线图】展开查看更多内容\nhttps://www.bilibili.com/opus/1129722427782201345\n如何下载资料\nhttps://www.bilibili.com/opus/443715248901563958\n\nAI大模型开发热门教程：\nAI大模型开发：BV1h1"
  },
  {
    "id": "bvid:BV1VZWc6dECG",
    "domain": "AI",
    "title": "【Re:从零开始的AI学习】第一季总集篇｜从入门到用好 AI",
    "url": "http://www.bilibili.com/video/av117430848391663",
    "source": "卡普迪姆",
    "platform": "bilibili",
    "points": 730016,
    "published_at": "2026-10-13T00:57:21+00:00",
    "summary": "这次，我把【Re：从零开始的 AI 学习】第一季全 13 期完整连在一起啦！\n新来的朋友或者想要查漏补缺的伙伴，现在可以一口气通关！从 AI 入门与提示词技巧，到 Agent 玩法、主流模型对比与使用成本……跟着走一遍就能彻底搞懂。\n希望这个系列能给你带来哪怕一点点启发，欢迎点赞、投币、收藏一键三连支持！也超级欢迎转发安利给身边的朋友～\n\n【目录】\n00:00 导语\n00:32 AI 这三年发生了"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 720007,
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
    "points": 674793,
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
    "points": 593019,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 547418,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1Nyp96pEGD",
    "domain": "AI",
    "title": "人人都要学！Agent 视觉创作全流程～【小白教程】",
    "url": "http://www.bilibili.com/video/av117427342017510",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 421098,
    "published_at": "2026-10-12T10:30:00+00:00",
    "summary": "做PPT、商品图、广告片！\n从活动策划到TVC成片，一期带你跑通创作型Agent全流程！\n感谢铁铁们的三连+关注～"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 356690,
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
    "points": 324239,
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
    "points": 308708,
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
    "points": 287161,
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
    "points": 280212,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1YG7G6eEPR",
    "domain": "AI",
    "title": "【全60集】吊打付费！目前B站最全最细的Agent智能体开发全套教程！手把手教你打造专属智能体，七天就能从小白到大神！带你从零基础入门到精通实现商业变现！",
    "url": "http://www.bilibili.com/video/av116815090947614",
    "source": "AI-Agent开发",
    "platform": "bilibili",
    "points": 224518,
    "published_at": "2026-06-26T06:57:42+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 208567,
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
    "points": 193170,
    "published_at": "2026-05-07T08:00:00+00:00",
    "summary": "这是你能看到的最完整的 Claude Code 零基础系统教程。\n\n\n我们将深度拆解：\n\n1️⃣ 基础入门：安装、第三方模型接入、权限系统。\n\n2️⃣ 核心进阶：Tools、Hooks、Skills、Subagents 及自动化流程。\n\n3️⃣ 项目实战：从零构建一个真实可用的 AI 网页 App。\n\n\n视频跟到最后，你不只是学会写代码，而是掌握 AI 智能体的工作逻辑。我是木子，只提供 AI 时"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 183944,
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
    "points": 162816,
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
    "points": 159890,
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
    "points": 137468,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1jCaq6nESn",
    "domain": "AI",
    "title": "【Opus 5.5半价】零基础小白友好，15分钟彻底学习Claude桌面版",
    "url": "http://www.bilibili.com/video/av117346425374831",
    "source": "LeaderAI",
    "platform": "bilibili",
    "points": 98826,
    "published_at": "2026-09-28T03:03:19+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 94073,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV15Vhy6cEhd",
    "domain": "AI",
    "title": "通俗易懂地讲解什么是Agent？",
    "url": "http://www.bilibili.com/video/av117330906449673",
    "source": "洪涛同学LovTech",
    "platform": "bilibili",
    "points": 85668,
    "published_at": "2026-09-25T09:12:59+00:00",
    "summary": "从0到1搭建一个简易Agent，从小白的角度出发解释Agent是如何运行的？"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 76525,
    "published_at": "2025-07-12T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1713u6XE1D",
    "domain": "AI",
    "title": "Claude Code 完全接管了 Blender，然后创造了这个",
    "url": "http://www.bilibili.com/video/av116980883398142",
    "source": "stefan_3d_ai",
    "platform": "bilibili",
    "points": 68374,
    "published_at": "2026-07-26T11:00:00+00:00",
    "summary": "如果你给一个完全自主的 AI 代理提供对 Blender 的完整终端控制权限，并让它完完全全靠自己独立运行整整一个小时，到底会发生什么可怕的事情？\n\n在这个视频中，我远远超越了简单的代码复制粘贴，结合 Claude Code 和全新发布的官方 Blender MCP 服务器，深入探索了真正的 3D 工作流自动化究竟长什么样。\n\n---\n\n🔹 试用 Tripo AI 并免费获取 500 生成积分：h"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 56116,
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
    "points": 49356,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47754,
    "published_at": "2026-02-10T11:44:51+00:00",
    "summary": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！2026年最强生产力！Claude Code Hooks回调+Agent Teams实现全自动开发零轮询方案详解！效率神器\n\n\n\n🚀🚀🚀视频简介：\n✅重磅教程！用Claude Code Hooks彻底解决OpenClaw轮询消耗Token的痛点！Stop Hook自动回调让Token消耗从暴涨变为几乎忽略不计！\n🔥 本期"
  },
  {
    "id": "bvid:BV1oc4m6wEoD",
    "domain": "AI",
    "title": "【江科大】如何用AI全流程开发STM32",
    "url": "http://www.bilibili.com/video/av117180431736152",
    "source": "拉咯比哩",
    "platform": "bilibili",
    "points": 38701,
    "published_at": "2026-08-30T02:00:00+00:00",
    "summary": "江科大老学长带你 FreeRTOS 项目实践 STM32F103 + Cube MX + FreeRTOS + 面向对象 + 项目框架\n这是AI入门篇，前置章节请见之前的视频\n此篇章将从零开始，用AI实现一套简单的系统\n感谢大家支持"
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30978,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV15wRwBwE79",
    "domain": "AI",
    "title": "小白AI做产品的唯一正确姿势！VS Code + Claude Code 王炸组合！",
    "url": "http://www.bilibili.com/video/av116510752250797",
    "source": "PM刘搞定",
    "platform": "bilibili",
    "points": 28871,
    "published_at": "2026-05-04T01:10:00+00:00",
    "summary": "你是不是也被网上铺天盖地的 “Vibecoding” 爽文给骗了？\n\n以为只要随便跟 AI 许个愿，它就能帮你直接写出一个爆款应用？\n\n现实却是：一顿操作猛如虎，一看代码原地杵。AI 瞎改一通，越改 Bug 越多，几百个文件堆在一起像个垃圾场，折腾两天最后只能无奈烂尾。🤦‍♂️\n\n其实，Vibecoding 绝对不是凭感觉瞎聊，它的底层仍然是严谨的工程化思维！\n\n本期视频，搞定带你彻底摒弃“抽卡式"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 24768,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1njtUeeE56",
    "domain": "AI",
    "title": "Unity + Cursor AI编程，让AI帮你写代码",
    "url": "http://www.bilibili.com/video/av113179434683184",
    "source": "Cool灬浩",
    "platform": "bilibili",
    "points": 22813,
    "published_at": "2024-09-22T05:02:40+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 22222,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
  },
  {
    "id": "bvid:BV1sQaL6vEkb",
    "domain": "AI",
    "title": "小白向，ai入门第一课：agent的部署和使用！",
    "url": "http://www.bilibili.com/video/av117349378166797",
    "source": "沈三殊",
    "platform": "bilibili",
    "points": 20678,
    "published_at": "2026-09-28T15:30:36+00:00",
    "summary": "详细的agent部署介绍：https://pan.quark.cn/s/3846914c6da7\n欢迎来到ai的世界！！\n有疑问欢迎私信。"
  },
  {
    "id": "bvid:BV181pt6REWv",
    "domain": "AI",
    "title": "【实战演示】Opus5.5做视频全流程教学，从小白入门到进阶技巧分享",
    "url": "http://www.bilibili.com/video/av117411453863055",
    "source": "LeaderAI",
    "platform": "bilibili",
    "points": 16565,
    "published_at": "2026-10-09T14:45:20+00:00",
    "summary": "Opus 5.5, Fable 5.1 全部官方半价： https://www.leaderai.top\n整理不易，需要知识库的小伙伴，关注三连后给后台回复“知识库”，看到了会第一时间发你哦。知识库内容很多，本节视频内容放在第3章下面第二个文档，可以从左侧展开目录查看。\n有任何配置问题，最好带图评论，方便帮你诊断"
  },
  {
    "id": "bvid:BV1cyVv6TEG6",
    "domain": "AI",
    "title": "Claude Code CLI 小白极简入门 - 装了之后必会的命令与快捷键",
    "url": "http://www.bilibili.com/video/av116677635217424",
    "source": "五里墩茶社",
    "platform": "bilibili",
    "points": 13914,
    "published_at": "2026-06-02T00:20:19+00:00",
    "summary": "一个key用全球大模型🔴 https://DMXAPI.cn 🚀 国内直连OpenAI、Claude、Gemini,💰￥1元起充!\n\n加入我的知识星球:https://t.zsxq.com/W5Oj7\n\n本期视频面向已经装好 Claude Code、想真正用起来的新手。\n\n装了 Claude Code、却只会跟它对话？这一期按一次真实会话的顺序，把每天都会用到的命令和快捷键过一遍 - 怎么发现命令"
  },
  {
    "id": "bvid:BV1Zk7Z66EVn",
    "domain": "AI",
    "title": "MT管理器 APK MCP  详细使用教程",
    "url": "http://www.bilibili.com/video/av116689177938837",
    "source": "梦然Zz",
    "platform": "bilibili",
    "points": 12729,
    "published_at": "2026-06-04T01:15:11+00:00",
    "summary": "MT管理器 APK MCP  详细使用教程"
  },
  {
    "id": "bvid:BV15epZ61E7F",
    "domain": "AI",
    "title": "我为什么强烈推荐Cursor的Pro套餐，Grok Bot真的太好用了！",
    "url": "http://www.bilibili.com/video/av117428784862489",
    "source": "AI摸鱼的梁师傅",
    "platform": "bilibili",
    "points": 12076,
    "published_at": "2026-10-12T16:06:10+00:00",
    "summary": "这期讲清楚三件事：为什么选 Cursor（官网软件直连、支付宝付款）；Pro 的两个模型池子怎么分（Grok/Composer 一池，Claude/GPT 共享一池）；附赠的 Grok Bot 怎么用——它有自己的云端电脑，合上 Mac 也在替你干活：定时简报、盯 PR、管邮件日历，还能多 Bot 协作。\n00:00 封号焦虑，和订套餐的理由 00:35 为什么是 Cursor：直连 + 支付宝 "
  },
  {
    "id": "bvid:BV18KJX6mEiH",
    "domain": "AI",
    "title": "太炸裂了！Claude Code 3.0彻底杀疯了！",
    "url": "http://www.bilibili.com/video/av117450007911196",
    "source": "烟神殿殿主",
    "platform": "bilibili",
    "points": 10640,
    "published_at": "2026-10-16T10:04:56+00:00",
    "summary": "原视频链接：https://www.youtube.com/watch?v=8nh1dcH4uJU\n本视频为AI技术搬运翻译，使用AI智能移除原视频广告营销内容，旨在降低信息差，帮助大家了解海外最新AI动态。\n翻译：烟神殿API,模型gemini-3.8-flash\n配音：使用的时FishTTS官方接口配音"
  },
  {
    "id": "bvid:BV1ovuC66EuG",
    "domain": "AI",
    "title": "老 k 带你手搓 AI 交易智能体",
    "url": "http://www.bilibili.com/video/av117080372351441",
    "source": "老K聊交易系统",
    "platform": "bilibili",
    "points": 9862,
    "published_at": "2026-08-12T03:43:43+00:00",
    "summary": "这是一套使用 Codex开发 AI 交易智能体的系列课程，内容包括：智能体功能介绍到软件安装配置，再到开发自动化交易工具，策略优化与训练，实现交易 skill 稳定自动运行。\n课程资料包下载：www.jujijiaoyi.com"
  },
  {
    "id": "bvid:BV1bBHm6MEG5",
    "domain": "AI",
    "title": "这绝对是b站讲的最好的Claude Code全套实战教程，手把手带你搞定国内环境安装配置，全程干货无废话！AI大模型/MCP/Skill/智能体/Agent",
    "url": "http://www.bilibili.com/video/av117402847155229",
    "source": "大模型饼饼",
    "platform": "bilibili",
    "points": 8769,
    "published_at": "2026-10-08T02:13:21+00:00",
    "summary": "这绝对是B站讲得最好的Claude Code全套实战教程！手把手带你搞定国内环境安装配置、基础操作、高阶实战技巧，课程不堆砌冗余理论，聚焦真实开发场景，带你吃透Claude Code核心能力，打通MCP、Skill与Agent智能体联动开发。不管你是想提升日常编码效率，还是入门AI智能体开发，这套教程都非常适合你，全程干货无废话！"
  },
  {
    "id": "bvid:BV1rmpb6VEgd",
    "domain": "AI",
    "title": "亲测有效：Claude Pro想在国内稳定使用物理防封教程。Claude Code常驻服务器，电脑手机私网接着用，防封号保姆级教程，命令全都标好",
    "url": "http://www.bilibili.com/video/av117410514469721",
    "source": "开水庆余年",
    "platform": "bilibili",
    "points": 8121,
    "published_at": "2026-10-09T10:40:42+00:00",
    "summary": "亲测有效的思路：与其每次换环境登录，不如把Claude Code固定跑在一台自己的美国VPS上。服务器固定、登录环境固定，账号环境更稳定，也更不容易触发风控，这就是我说的“物理防封”。Claude Pro账号需要自己合规订阅。\n\n这期是保姆级教程：每一步都标好在哪台设备、用哪个用户、执行什么命令、看到什么算成功。电脑和手机通过Tailscale组成只连自己设备的私网，接着同一个会话往下用。\n\n章节"
  },
  {
    "id": "hn:50008187",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI annualised revenues $20B less than previously signalled",
    "url": "https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 432,
    "published_at": "2026-10-08T16:45:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49844663",
    "domain": "AI 算力 / 半导体",
    "title": "ASML says it sold 'absolutely nothing' in Europe in 2026",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/asml-says-its-sells-absolutely-nothing-in-europe-calls-on-eu-to-help-create-demand",
    "source": "MC995",
    "platform": "hackernews",
    "points": 403,
    "published_at": "2026-09-25T13:49:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50035886",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia in talks to acquire US 'open' model startup Reflection AI",
    "url": "https://www.ft.com/content/052610c5-22b4-4dd4-932e-b7f9f0628b6a",
    "source": "arkj",
    "platform": "hackernews",
    "points": 179,
    "published_at": "2026-10-10T18:48:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:50086363",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's first GPU: GeForce 256",
    "url": "https://dfarq.homeip.net/nvidias-first-gpu-geforce-256/",
    "source": "ibobev",
    "platform": "hackernews",
    "points": 79,
    "published_at": "2026-10-14T12:05:44+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/semicon-west-2026-displays-ai-era-chipmaking-workforce-development/",
    "domain": "AI 算力 / 半导体",
    "title": "SEMICON West 2026 Displays AI-Era Chipmaking, Workforce Development",
    "url": "https://www.eetimes.com/semicon-west-2026-displays-ai-era-chipmaking-workforce-development/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T20:59:50+00:00",
    "summary": "The trillion-dollar semiconductor industry is ready to adapt and expand its fab infrastructure for the AI wave. The post SEMICON West 2026 Displays AI-Era Chipmaking, Workforce Development appeared fi"
  },
  {
    "id": "rss:https://www.eetimes.com/data-center-power-a-prominent-highlight-of-ocp-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "Data Center Power a Prominent Highlight of OCP 2026",
    "url": "https://www.eetimes.com/data-center-power-a-prominent-highlight-of-ocp-2026/",
    "source": "Majeed Ahmad",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T15:00:00+00:00",
    "summary": "The OCP Summit showcased power delivery boards, PSU designs, hot-swap controllers, and event-based telemetry. The post Data Center Power a Prominent Highlight of OCP 2026 appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/taiwans-ai-ambitions-run-into-talent-gap/",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan’s AI Ambitions Run into Talent Gap",
    "url": "https://www.eetimes.com/taiwans-ai-ambitions-run-into-talent-gap/",
    "source": "Sally Ward-Foxton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T10:55:42+00:00",
    "summary": "AMD’s David Wang told EE Times that while Taiwan has huge opportunities in rack-scale AI, physical AI, and AI PC markets, the sticking point may well be talent. The post Taiwan’s AI Ambitions Run into"
  },
  {
    "id": "rss:https://www.eetimes.com/your-chip-works-prove-it-is-secure/",
    "domain": "AI 算力 / 半导体",
    "title": "Your Chip Works. Prove It Is Secure.",
    "url": "https://www.eetimes.com/your-chip-works-prove-it-is-secure/",
    "source": "Arteris",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T08:37:49+00:00",
    "summary": "Join this 30-Minute BitCast as our expert demonstrates how information flow tracking follows security-sensitive assets during existing simulation or emulation runs. The post Your Chip Works. Prove It "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/grab-an-rtx-5090-for-discounted-usd5-300-as-part-of-an-msi-infinite-zs-prebuilt-gaming-pc-usd7-599-price-includes-other-components-worth-about-usd2-300-on-their-own",
    "domain": "AI 算力 / 半导体",
    "title": "Grab an RTX 5090 for a discounted $5,300 as part of an MSI Infinite ZS prebuilt gaming PC — price includes other components worth about $2,300 on their own",
    "url": "https://www.tomshardware.com/pc-components/gpus/grab-an-rtx-5090-for-discounted-usd5-300-as-part-of-an-msi-infinite-zs-prebuilt-gaming-pc-usd7-599-price-includes-other-components-worth-about-usd2-300-on-their-own",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T20:30:58+00:00",
    "summary": "Grab an RTX 5090 for $5,300 as part of an MSI Infinite ZS prebuilt — $7,599 price includes other components worth about $2,300 on their own"
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-headsets/hyperx-cloud-alpha-air-review",
    "domain": "AI 算力 / 半导体",
    "title": "HyperX Cloud Alpha Air Review: Open-back and budget-friendly",
    "url": "https://www.tomshardware.com/peripherals/gaming-headsets/hyperx-cloud-alpha-air-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T15:40:00+00:00",
    "summary": "The HyperX Cloud Alpha Air is the brand's first open-back gaming headset. It's lightweight and comfortable, and it sounds very good. But microphone pickup is low, and it doesn't seem to work with the "
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/quad-8-pin-mod-protects-the-usd8-500-rtx-5090-you-cant-replace-from-melting-modders-custom-power-solution-claims-to-fix-nvidia-16-pin-gpu-meltdowns",
    "domain": "AI 算力 / 半导体",
    "title": "Quad 8-pin mod protects the $8,500 RTX 5090 you can’t replace from melting",
    "url": "https://www.tomshardware.com/pc-components/gpus/quad-8-pin-mod-protects-the-usd8-500-rtx-5090-you-cant-replace-from-melting-modders-custom-power-solution-claims-to-fix-nvidia-16-pin-gpu-meltdowns",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T15:20:00+00:00",
    "summary": "Redditor showcases a new quad 8-pin power-conversion kit for the 16-pin power connector on Nvidia GeForce RTX graphics cards."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/controllers-gamepads/moza-ay210-force-feedback-base-and-mfy-yoke-review",
    "domain": "AI 算力 / 半导体",
    "title": "MOZA AY210 Force Feedback Base and MFY Yoke review: Taking flight sim immersion to the next level",
    "url": "https://www.tomshardware.com/peripherals/controllers-gamepads/moza-ay210-force-feedback-base-and-mfy-yoke-review",
    "source": "Dan Mateescu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T15:00:00+00:00",
    "summary": "The MOZA AY210 Force Feedback Base and MFY Yoke Bundle brings force feedback and autopilot following to the world of desktop flight simulators."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-insists-the-rtx-5090-isnt-dead-despite-severe-shortages-and-removed-listings-at-multiple-retailers-flagship-gpu-is-missing-from-nvidias-store-and-commands-usd8-500-on-amazon",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia reportedly insists the RTX 5090 isn't dead despite severe shortages and removed listings at multiple retailers",
    "url": "https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-insists-the-rtx-5090-isnt-dead-despite-severe-shortages-and-removed-listings-at-multiple-retailers-flagship-gpu-is-missing-from-nvidias-store-and-commands-usd8-500-on-amazon",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T14:38:18+00:00",
    "summary": "Nvidia states that RTX 5090 isn't discontinued, only that supply is constrained — and yet the card is effectively gone from storefronts"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/sandisks-512gb-switch-2-ready-microsd-express-card-is-a-steal-for-usd98-during-sale-rare-tech-deal-arrives-to-beat-the-storage-shortage",
    "domain": "AI 算力 / 半导体",
    "title": "Sandisk’s 512GB Switch 2-ready microSD Express card is a steal for $98 during sale",
    "url": "https://www.tomshardware.com/pc-components/sandisks-512gb-switch-2-ready-microsd-express-card-is-a-steal-for-usd98-during-sale-rare-tech-deal-arrives-to-beat-the-storage-shortage",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T13:39:06+00:00",
    "summary": "Nintendo Switch 2 owners looking to download more games can take advantage of this deal on SanDisk’s officially licensed microSD Express card, which supports read speeds of up to 880 MB/s and offers 5"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-lab-offers-free-plumbing-and-hvac-repairs-across-three-cities-to-train-ai-robots-wearable-sensors-record-video-of-repair-work-for-robotics-training-free-services-also-include-electrical-work-air-duct-cleaning-and-carpet-cleaning",
    "domain": "AI 算力 / 半导体",
    "title": "AI lab offers free plumbing and HVAC repairs across three cities to train AI robots",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-lab-offers-free-plumbing-and-hvac-repairs-across-three-cities-to-train-ai-robots-wearable-sensors-record-video-of-repair-work-for-robotics-training-free-services-also-include-electrical-work-air-duct-cleaning-and-carpet-cleaning",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T13:21:20+00:00",
    "summary": "HUMXN wants to pay for maintenance and repair services for homes in Minneapolis, Chicago, and Miami to gather data to train AI models and robots."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-october-17-2026-packaging-roadmaps-chinese-dgx-spark-rival-emerges-and-digging-into-asmls-earnings",
    "domain": "AI 算力 / 半导体",
    "title": "This week on Tom's Hardware Premium: October 17, 2026",
    "url": "https://www.tomshardware.com/tech-industry/this-week-on-toms-hardware-premium-october-17-2026-packaging-roadmaps-chinese-dgx-spark-rival-emerges-and-digging-into-asmls-earnings",
    "source": "Sayem Ahmed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T13:00:00+00:00",
    "summary": "This week, Tom's Hardware Premium subscribers can read our EMIB and Foveros roadmaps, the latest on Chinese competition in the local AI system space, and much more."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/international-measurement-organization-to-retire-leap-seconds-next-year-to-avoid-wreaking-havoc-on-computer-systems-group-makes-move-to-simplify-atomic-time-tracking",
    "domain": "AI 算力 / 半导体",
    "title": "Leap seconds being retired next year to avoid wreaking havoc on computer systems",
    "url": "https://www.tomshardware.com/tech-industry/international-measurement-organization-to-retire-leap-seconds-next-year-to-avoid-wreaking-havoc-on-computer-systems-group-makes-move-to-simplify-atomic-time-tracking",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T12:40:00+00:00",
    "summary": "The leap second will be replaced by a leap hour, which will take \"several centuries\" before it must be implemented."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/taiwan-targets-illicit-ai-server-exports-to-china-with-five-year-prison-terms-strict-new-controls-follow-us-tariff-deal-and-super-micro-raid",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan targets illicit AI server exports to China with five-year prison terms",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/taiwan-targets-illicit-ai-server-exports-to-china-with-five-year-prison-terms-strict-new-controls-follow-us-tariff-deal-and-super-micro-raid",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T12:20:00+00:00",
    "summary": "Taiwan is expanding the Foreign Trade Act to include AI servers and semiconductors in its list of controlled exports."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-agent-took-eth-from-another-account-without-authorization-justified-stealing-in-its-chain-of-thought",
    "domain": "AI 算力 / 半导体",
    "title": "Crafty OpenAI agent willingly stole crypto from an account it didn't own to complete a task during test",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-agent-took-eth-from-another-account-without-authorization-justified-stealing-in-its-chain-of-thought",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T12:00:00+00:00",
    "summary": "GPT5.6-Sol didn't have funds to deploy smart contracts, so it looked for exposed accounts with enough money to pay for the gas fees."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/game-decompilation-tracker-decomp-dev-shuts-its-public-leaderboard-saying-ai-has-broken-the-community-its-creator-blames-forks-that-use-ai-to-finish-other-teams-projects-and-races-to-ship-rough-pc-ports",
    "domain": "AI 算力 / 半导体",
    "title": "Game decompilation hub freezes leaderboard after AI turns progress into a hollow numbers game amid explosion of 'AI slop'",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/game-decompilation-tracker-decomp-dev-shuts-its-public-leaderboard-saying-ai-has-broken-the-community-its-creator-blames-forks-that-use-ai-to-finish-other-teams-projects-and-races-to-ship-rough-pc-ports",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T11:30:00+00:00",
    "summary": "decomp.dev has closed its public index of game decompilation projects, saying AI-driven forks and ports broke the community."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/modder-finishes-nine-year-xbox-360-voltage-glitch-mod-with-a-usd4-microcontroller-cracks-the-console-open-tiny-microcontroller-dumps-nand-and-flashes-timing-files-to-bypass-cpu-cryptography",
    "domain": "AI 算力 / 半导体",
    "title": "Modder finishes nine-year Xbox 360 voltage glitch mod with a $4 microcontroller, cracks the console open",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/modder-finishes-nine-year-xbox-360-voltage-glitch-mod-with-a-usd4-microcontroller-cracks-the-console-open-tiny-microcontroller-dumps-nand-and-flashes-timing-files-to-bypass-cpu-cryptography",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T11:00:00+00:00",
    "summary": "Modder glitch-hacks his Xbox 360 with the help of a $4 microcontroller — operation shows the power of the Rasperry Pi Pico"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/us-army-to-use-3d-printed-rocket-motors-for-low-cost-cruise-missiles-additive-manufacturing-company-secures-deal-to-build-rocket-engines-for-the-arsenal-of-freedom",
    "domain": "AI 算力 / 半导体",
    "title": "US Army to use 3D-printed rocket motors for low-cost cruise missiles",
    "url": "https://www.tomshardware.com/3d-printing/us-army-to-use-3d-printed-rocket-motors-for-low-cost-cruise-missiles-additive-manufacturing-company-secures-deal-to-build-rocket-engines-for-the-arsenal-of-freedom",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T10:30:00+00:00",
    "summary": "X-Bow Systems has been tapped to 3D-print rocket motors for the U.S. Army's low-cost cruise missiles."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/employee-exclusive-asml-lego-set-now-available-on-rebrickable-custom-creation-modifies-original-version-to-add-more-details-now-requires-810-parts",
    "domain": "AI 算力 / 半导体",
    "title": "ASML's employee-only High-NA EUV Lego kit gets an open 810-piece fan replica",
    "url": "https://www.tomshardware.com/tech-industry/employee-exclusive-asml-lego-set-now-available-on-rebrickable-custom-creation-modifies-original-version-to-add-more-details-now-requires-810-parts",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T10:00:00+00:00",
    "summary": "A Lego enthusiast recreated the rare ASML Lego kit, added their own customizations, and shared the plans for free on Rebrickable."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/this-could-be-your-last-chance-to-grab-an-rtx-5090-how-to-secure-nvidias-top-rtx-gpu-as-rumors-of-discontinuation-swirl",
    "domain": "AI 算力 / 半导体",
    "title": "This could be your last chance to grab an RTX 5090",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/this-could-be-your-last-chance-to-grab-an-rtx-5090-how-to-secure-nvidias-top-rtx-gpu-as-rumors-of-discontinuation-swirl",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T17:04:44+00:00",
    "summary": "With no new Nvidia 5090 GPU replacement anticipated before at least 2028, this could well be your last opportunity to get your hands on a very powerful GPU for gaming."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/china-startup-demoes-prototype-euv-light-source-15w-of-output-power-and-90-percent-domestic-components-still-years-away-from-viability",
    "domain": "AI 算力 / 半导体",
    "title": "China startup demoes prototype EUV light source",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/china-startup-demoes-prototype-euv-light-source-15w-of-output-power-and-90-percent-domestic-components-still-years-away-from-viability",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:30:00+00:00",
    "summary": "Chinese startup Langdao Silex showcased its laser-produced plasma EUV source at a trade show, but the technology will likely take many years before it gets to decent EUV power levels. Even if it does,"
  },
  {
    "id": "rss:https://www.tomshardware.com/3d-printing/gun-rights-activist-unveils-worlds-first-ai-made-3d-printed-firearm-22-caliber-handgun-created-by-an-ai-that-can-generate-guns-called-gatgpt",
    "domain": "AI 算力 / 半导体",
    "title": "Gun-rights activist unveils world's first 'AI-made' 3D-printed firearm — .22 caliber handgun created by an 'AI that can generate guns' called GatGPT",
    "url": "https://www.tomshardware.com/3d-printing/gun-rights-activist-unveils-worlds-first-ai-made-3d-printed-firearm-22-caliber-handgun-created-by-an-ai-that-can-generate-guns-called-gatgpt",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:20:41+00:00",
    "summary": "A gun rights activist has unveiled the world's first AI-made 3D printed firearm."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/nvidia-rtx-spark-devices-are-now-officially-on-sale-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptops-here-starting-at-usd2-599-where-to-buy-pricing-and-availability-revealed-on-several-models",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia RTX Spark devices are now officially on sale, secure the Surface Laptop Ultra or other RTX Spark laptops here",
    "url": "https://www.tomshardware.com/laptops/nvidia-rtx-spark-devices-are-now-officially-on-sale-secure-the-surface-laptop-ultra-or-other-rtx-spark-laptops-here-starting-at-usd2-599-where-to-buy-pricing-and-availability-revealed-on-several-models",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T15:38:45+00:00",
    "summary": "Orders are live on Nvidia RTX Spark laptops, including the Microsoft Surface Laptop Ultra and devices from HP, Lenovo, Asus, and Dell."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/new-york-rep-announces-game-ownership-bill-that-would-require-consumer-ownership-rather-than-sale-of-licenses-would-also-require-publishers-to-keep-the-game-functional-after-support-ends",
    "domain": "AI 算力 / 半导体",
    "title": "New York rep announces game ownership bill that would require consumer ownership rather than sale of licenses",
    "url": "https://www.tomshardware.com/video-games/new-york-rep-announces-game-ownership-bill-that-would-require-consumer-ownership-rather-than-sale-of-licenses-would-also-require-publishers-to-keep-the-game-functional-after-support-ends",
    "source": "Jhet Borja",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T13:51:32+00:00",
    "summary": "New York joins Pennsylvania in protecting gamers' rights to own games, requiring publishers to provide an offline mode and the right to transfer games."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/motherboards/gigabyte-x870-aorus-infinity-motherboard-review",
    "domain": "AI 算力 / 半导体",
    "title": "Gigabyte X870 Aorus Infinity Motherboard Review: limited-edition, designed for extreme overclocking, but pricey for X870",
    "url": "https://www.tomshardware.com/pc-components/motherboards/gigabyte-x870-aorus-infinity-motherboard-review",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T13:00:00+00:00",
    "summary": "Gigabyte’s limited-edition 40th-anniversary X870 Aorus Infinity motherboard is designed for extreme overclocking, with everything you need for daily use."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/googlebooks-are-as-poorly-timed-as-valves-steam-machine-and-may-suffer-a-similar-fate",
    "domain": "AI 算力 / 半导体",
    "title": "Googlebooks are as poorly timed as Valve’s Steam Machine, and may suffer a similar fate",
    "url": "https://www.tomshardware.com/laptops/googlebooks-are-as-poorly-timed-as-valves-steam-machine-and-may-suffer-a-similar-fate",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T12:30:00+00:00",
    "summary": "Google attempted to take its Chromebook platform upscale with Googlebooks. But the timing could not have been worse. Phone support at launch is extremely limited, and most people use Android phones an"
  },
  {
    "id": "rss:https://www.tomshardware.com/tablets/microsoft-surface/microsoft-surface-laptop-ultra-rtx-spark-review",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft Surface Laptop Ultra review: RTX Spark in a straight-up beautiful Windows PC",
    "url": "https://www.tomshardware.com/tablets/microsoft-surface/microsoft-surface-laptop-ultra-rtx-spark-review",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T12:00:00+00:00",
    "summary": "Microsoft’s Surface Laptop Ultra is its most beautiful laptop ever, but using Windows on it is the same as ever. Only AI enthusiasts will get the most out of RTX Spark."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/taiwan-raising-usd4-billion-to-build-industrial-park-in-texas-to-support-us-chipmaking-supply-chain-project-to-support-countless-small-manufacturers-crucial-to-tsmc-foxconn-supply-chain",
    "domain": "AI 算力 / 半导体",
    "title": "Taiwan raising $4 billion to build industrial park in Texas to support US chipmaking supply chain",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/taiwan-raising-usd4-billion-to-build-industrial-park-in-texas-to-support-us-chipmaking-supply-chain-project-to-support-countless-small-manufacturers-crucial-to-tsmc-foxconn-supply-chain",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T11:57:18+00:00",
    "summary": "This $4 billion industrial park would make it easier for smaller Taiwanese companies who can't afford to build their own sites in the U.S. to expand and follow major Taiwanese manufacturers like TSMC "
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/epic-introduces-an-improved-version-of-anti-cheat-for-linux-eac-linux-v2-will-finally-allow-linux-gamers-to-play-fortnite",
    "domain": "AI 算力 / 半导体",
    "title": "Epic introduces an improved version of anti-cheat for Linux",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/epic-introduces-an-improved-version-of-anti-cheat-for-linux-eac-linux-v2-will-finally-allow-linux-gamers-to-play-fortnite",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T11:30:00+00:00",
    "summary": "Epic wants to work with developers and maintainers to find the best solution to making anti-cheat work seamlessly on Linux."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cooling/experiment-shows-liquid-metal-tim-doesnt-dry-out-it-turns-solid-two-year-electron-microscope-test-finds-gallium-bonds-with-copper-coolers-and-nickel-plating-keeps-the-layer-about-10-times-thinner",
    "domain": "AI 算力 / 半导体",
    "title": "Experiment shows liquid metal TIM doesn’t dry out; it turns solid",
    "url": "https://www.tomshardware.com/pc-components/cooling/experiment-shows-liquid-metal-tim-doesnt-dry-out-it-turns-solid-two-year-electron-microscope-test-finds-gallium-bonds-with-copper-coolers-and-nickel-plating-keeps-the-layer-about-10-times-thinner",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T11:00:00+00:00",
    "summary": "Der8auer’s two-year electron microscope test shows liquid metal’s gallium turns solid on copper and nickel-plated coolers."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ddr5/corsairs-vengeance-rgb-ddr5-32gb-memory-receives-a-usd108-price-cut-the-cheapest-ddr5-5600-kit-available-to-buy-right-now",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair's Vengeance RGB DDR5 32GB memory receives a $108 price cut",
    "url": "https://www.tomshardware.com/pc-components/ddr5/corsairs-vengeance-rgb-ddr5-32gb-memory-receives-a-usd108-price-cut-the-cheapest-ddr5-5600-kit-available-to-buy-right-now",
    "source": "Stewart Bendle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T10:55:27+00:00",
    "summary": "Save $108 on Corsair's Vengeance RGB RAM and bag 32GB of DDR5 memory for your PC."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/linus-torvalds-posts-his-first-llm-assisted-patch-to-the-linux-kernel-after-issuing-clear-pro-ai-directives-the-bossman-makes-use-of-ai-tooling-himself",
    "domain": "AI 算力 / 半导体",
    "title": "Linus Torvalds posts his first AI-assisted patch to the Linux kernel, synthetic test clocks 23x performance leap",
    "url": "https://www.tomshardware.com/software/linux/linus-torvalds-posts-his-first-llm-assisted-patch-to-the-linux-kernel-after-issuing-clear-pro-ai-directives-the-bossman-makes-use-of-ai-tooling-himself",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T10:30:00+00:00",
    "summary": "Linus Torvalds posts his first LLM-assisted patch to the Linux kernel — after issuing clear pro-AI directives, the bossman makes use of AI tooling himself"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/thai-cops-bust-audacious-cross-border-fiberoptic-cable-running-to-myanmar-scam-compound-350-meter-48-core-cable-was-supplying-illegal-border-casino-and-a-scam-center-with-6tb-of-data-per-day",
    "domain": "AI 算力 / 半导体",
    "title": "Thai cops bust 'audacious' cross-border fiberoptic cable running to Myanmar scam compound",
    "url": "https://www.tomshardware.com/tech-industry/thai-cops-bust-audacious-cross-border-fiberoptic-cable-running-to-myanmar-scam-compound-350-meter-48-core-cable-was-supplying-illegal-border-casino-and-a-scam-center-with-6tb-of-data-per-day",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T10:24:24+00:00",
    "summary": "Thai authorities have busted a cross-border fiber-optic internet cable being used to steal data."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/ukrainian-drones-hit-russian-data-centers-disrupting-russian-apps-and-services-attacks-highlight-the-fragility-of-the-countrys-digital-services",
    "domain": "AI 算力 / 半导体",
    "title": "Ukrainian drones hit Russian data centers, disrupting Russian apps and services",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/ukrainian-drones-hit-russian-data-centers-disrupting-russian-apps-and-services-attacks-highlight-the-fragility-of-the-countrys-digital-services",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T10:15:00+00:00",
    "summary": "After Ukrainian long-range strike drones targeted Russian data centers, various Russian digital services and apps went down or faced severe disruption. There's even some suggestion that online bot act"
  },
  {
    "id": "hn:50110301",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia, Apple, Google, Microsoft, Amazon, Meta gave Trump $92M for his ballroom",
    "url": "https://www.theverge.com/policy/1012047/nvidia-apple-google-microsoft-amazon-meta-trump-ballroom",
    "source": "jacquesm",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-15T21:11:05+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.eetimes.com/ai-moves-to-system-level-co-design-how-can-taiwan-capture-more-value/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Moves to System-Level Co-Design: How Can Taiwan Capture More Value",
    "url": "https://www.eetimes.com/ai-moves-to-system-level-co-design-how-can-taiwan-capture-more-value/",
    "source": "Susan Hong",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T07:18:34+00:00",
    "summary": "During a panel session at iTechCon 2026, discussions explored how Taiwan can build on its strengths in semiconductors, advanced packaging, and system design to support AI development. The post AI Move"
  },
  {
    "id": "rss:https://www.eetimes.com/japan-offers-globalfoundries-21b-for-u-s-fab-expansion/",
    "domain": "AI 算力 / 半导体",
    "title": "Japan Offers GlobalFoundries $21B for U.S. Fab Expansion",
    "url": "https://www.eetimes.com/japan-offers-globalfoundries-21b-for-u-s-fab-expansion/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T19:00:00+00:00",
    "summary": "Japan’s $21B offer to GlobalFoundries would add two New York fabs and lift U.S. chip capacity 10%; see why analysts warn on state support. The post Japan Offers GlobalFoundries $21B for U.S. Fab Expan"
  },
  {
    "id": "rss:https://www.eetimes.com/data-orchestration-the-foundation-for-the-next-generation-semiconductor-enterprise/",
    "domain": "AI 算力 / 半导体",
    "title": "Data Orchestration: The Foundation for the Next-generation Semiconductor Enterprise",
    "url": "https://www.eetimes.com/data-orchestration-the-foundation-for-the-next-generation-semiconductor-enterprise/",
    "source": "Siemens Digital Industries",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T14:00:00+00:00",
    "summary": "Data orchestration gives semiconductor engineering teams a practical way to unify disconnected equipment, systems, and data without replacing existing infrastructure. By creating a connected execution"
  },
  {
    "id": "rss:https://www.eetimes.com/husb237-the-cost-effective-pd-sink-with-just-2-passives/",
    "domain": "AI 算力 / 半导体",
    "title": "HUSB237: The Cost-Effective PD Sink with Just 2 Passives",
    "url": "https://www.eetimes.com/husb237-the-cost-effective-pd-sink-with-just-2-passives/",
    "source": "Hynetek Semiconductor Co., Ltd.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T13:00:00+00:00",
    "summary": "Discover Hynetek’s HUSB237, a compact USB-PD sink controller enabling firmware-free USB-C upgrades up to 100W with only two external components. The post HUSB237: The Cost-Effective PD Sink with Just "
  },
  {
    "id": "rss:https://www.eetimes.com/small-volumes-big-impact-europes-hidden-role-in-advanced-chipmaking/",
    "domain": "AI 算力 / 半导体",
    "title": "Small Volumes, Big Impact: Europe’s Hidden Role in Advanced Chipmaking",
    "url": "https://www.eetimes.com/small-volumes-big-impact-europes-hidden-role-in-advanced-chipmaking/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T10:54:08+00:00",
    "summary": "A Fraunhofer–IMS Nanofabrication partnership illustrates how Europe's low-volume semiconductor manufacturing can support the world's most advanced chipmaking. The post Small Volumes, Big Impact: Europ"
  },
  {
    "id": "rss:https://www.eetimes.com/grid-modernization-hidden-cost-a-growing-attack-surface-few-are-watching/",
    "domain": "AI 算力 / 半导体",
    "title": "Grid Modernization’s Hidden Cost: A Growing Attack Surface Few Are Watching",
    "url": "https://www.eetimes.com/grid-modernization-hidden-cost-a-growing-attack-surface-few-are-watching/",
    "source": "David Montoya",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-15T08:00:00+00:00",
    "summary": "Grid modernization is expanding the energy sector’s cyberattack surface, while limited visibility across IT and OT networks leaves connected assets exposed. The post Grid Modernization’s Hidden Cost: "
  },
  {
    "id": "hn:50062098",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia accused of trying to cut a deal with Anna's Archive",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-accused-of-trying-to-cut-a-deal-with-annas-archive-for-high-speed-access-to-the-massive-pirated-book-haul-allegedly-chased-stolen-data-to-fuel-its-llms",
    "source": "amai",
    "platform": "hackernews",
    "points": 19,
    "published_at": "2026-10-12T19:57:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:50081435",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Reportedly Ending the RTX 5090, Reserves GB202 for Workstation GPUs",
    "url": "https://www.techpowerup.com/353578/nvidia-reportedly-ending-the-rtx-5090-reserves-gb202-silicon-for-workstation-gpus",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-10-14T01:52:56+00:00",
    "summary": ""
  },
  {
    "id": "hn:50046896",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia-backed data centre firm Firmus scraps IPO as AI valuation concerns deepen",
    "url": "https://www.bbc.com/news/articles/ck9dzpw4ll8po",
    "source": "devonnull",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-11T19:26:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:49973937",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's Olympus Core: Pushing Server Single Threaded Performance Boundaries",
    "url": "https://chipsandcheese.com/p/nvidias-olympus-core-pushing-server",
    "source": "pella",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-10-06T03:51:00+00:00",
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
    "id": "hn:49913571",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/",
    "source": "bradleyg223",
    "platform": "hackernews",
    "points": 1705,
    "published_at": "2026-09-30T20:04:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:50073879",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon",
    "url": "https://deepmind.google/models/gemini/",
    "source": "737max",
    "platform": "hackernews",
    "points": 1465,
    "published_at": "2026-10-13T16:03:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:49797982",
    "domain": "大厂 AI 动态",
    "title": "I said no and Apple said yes",
    "url": "https://dbushell.com/2026/09/22/apple-intelligence/",
    "source": "thatslast",
    "platform": "hackernews",
    "points": 886,
    "published_at": "2026-09-22T08:04:55+00:00",
    "summary": ""
  },
  {
    "id": "hn:49957116",
    "domain": "大厂 AI 动态",
    "title": "Turn off Apple Intelligence on macOS 27 and get its disk space back",
    "url": "https://github.com/omlahore/RemoveMacAI",
    "source": "privacyisntdead",
    "platform": "hackernews",
    "points": 775,
    "published_at": "2026-10-04T19:42:25+00:00",
    "summary": ""
  },
  {
    "id": "hn:49848269",
    "domain": "大厂 AI 动态",
    "title": "Ollaya – Ollama for open-source, Jev-style decision models",
    "url": "https://ollaya.dev/",
    "source": "Ardakilic",
    "platform": "hackernews",
    "points": 618,
    "published_at": "2026-09-25T18:33:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50122431",
    "domain": "大厂 AI 动态",
    "title": "Llama.cpp on a jailbroken PS5: run any GGUF model natively on the console",
    "url": "https://github.com/cobanov/PS5LM",
    "source": "Anon84",
    "platform": "hackernews",
    "points": 367,
    "published_at": "2026-10-16T18:32:35+00:00",
    "summary": ""
  },
  {
    "id": "hn:49790409",
    "domain": "大厂 AI 动态",
    "title": "Turn off and restrict access to Apple Intelligence features on Mac",
    "url": "https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac",
    "source": "alwillis",
    "platform": "hackernews",
    "points": 354,
    "published_at": "2026-09-21T17:30:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:50118688",
    "domain": "大厂 AI 动态",
    "title": "Show HN: Gemini 4 Argon plays StarCraft",
    "url": "https://starskirmish.com/bench/v0-2/",
    "source": "__cayenne__",
    "platform": "hackernews",
    "points": 243,
    "published_at": "2026-10-16T14:18:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:49817615",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 text-to-speech",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/",
    "source": "swolpers",
    "platform": "hackernews",
    "points": 331,
    "published_at": "2026-09-23T15:29:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50074869",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon for Robotics",
    "url": "https://developers.googleblog.com/gemini-4-argon-for-robotics/",
    "source": "xnx",
    "platform": "hackernews",
    "points": 233,
    "published_at": "2026-10-13T16:55:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49844896",
    "domain": "大厂 AI 动态",
    "title": "Microsoft abandons personal AI chatbot race with Copilot reboot",
    "url": "https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 157,
    "published_at": "2026-09-25T14:07:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:49829387",
    "domain": "大厂 AI 动态",
    "title": "Hackers influence ChatGPT and Gemini to direct users to scam centers",
    "url": "https://medium.com/@arielsimon/dark-sourcery-how-hackers-manipulate-ai-to-scam-you-88df434d2073",
    "source": "ArielSimon",
    "platform": "hackernews",
    "points": 143,
    "published_at": "2026-09-24T11:54:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49854945",
    "domain": "大厂 AI 动态",
    "title": "The Copilot+ PC brand is dead",
    "url": "https://www.windowscentral.com/microsoft/windows-11/the-copilot-pc-brand-is-dead-microsoft-and-pc-makers-quietly-pull-back-on-tarnished-windows-11-ai-pc-branding",
    "source": "bj-rn",
    "platform": "hackernews",
    "points": 122,
    "published_at": "2026-09-26T09:55:38+00:00",
    "summary": ""
  },
  {
    "id": "hn:49914236",
    "domain": "大厂 AI 动态",
    "title": "Gemini 4 Argon (High): Intelligence, Performance and Price Analysis",
    "url": "https://artificialanalysis.ai/models/gemini-4-argon",
    "source": "theanonymousone",
    "platform": "hackernews",
    "points": 113,
    "published_at": "2026-09-30T20:50:28+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/1013453/tiktok-bans-alex-gibneys-musk-documentary",
    "domain": "大厂 AI 动态",
    "title": "TikTok bans Musk documentary account",
    "url": "https://www.theverge.com/tech/1013453/tiktok-bans-alex-gibneys-musk-documentary",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T19:32:23+00:00",
    "summary": "Just ahead of the wider release of Alex Gibney's Musk documentary, TikTok has banned the film's social media account from its platform. TikTok did not immediately respond to a request for comment. Acc"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/1013088/mercedes-amg-gt-suv-price-specs-performance",
    "domain": "大厂 AI 动态",
    "title": "Mercedes-AMG’s first ground-up SUV is a 1,150hp electric beast",
    "url": "https://www.theverge.com/transportation/1013088/mercedes-amg-gt-suv-price-specs-performance",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T17:00:00+00:00",
    "summary": "Earlier this year, Mercedes' AMG performance brand grabbed our attention with the GT four-door coupe, a souped-up sports sedan with three axial flux motors delivering over 1,150 horsepower. Well, now "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1013431/elon-musk-settles-lawsuits-over-1-million-voter-giveaway",
    "domain": "大厂 AI 动态",
    "title": "Elon Musk settles lawsuits over $1 million voter giveaway",
    "url": "https://www.theverge.com/tech/1013431/elon-musk-settles-lawsuits-over-1-million-voter-giveaway",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T16:39:44+00:00",
    "summary": "In 2024, Elon Musk promised to give away $1 million a day to a randomly selected registered voter in a swing state. That prompted legal challenges, raised questions about its legality, and drew lawsui"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1013409/meta-removes-language-that-may-have-allowed-it-to-scrape-news-sites",
    "domain": "大厂 AI 动态",
    "title": "Meta removes language that may have allowed it to scrape news sites",
    "url": "https://www.theverge.com/tech/1013409/meta-removes-language-that-may-have-allowed-it-to-scrape-news-sites",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T15:04:36+00:00",
    "summary": "After backlash, Meta is updating its terms again to remove language that suggested it could scrape content from sites, including news sites, to train its AI. Specifically, the following language no lo"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/1013105/pikmin-4-nintendo-switch-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Pikmin 4 is $20 off ahead of its $10 Nintendo Switch 2 update",
    "url": "https://www.theverge.com/gadgets/1013105/pikmin-4-nintendo-switch-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T15:00:00+00:00",
    "summary": "If you’re wondering what video game to play this weekend, my colleague Sheena Vasani spotted a discounted Nintendo Switch title with instant digital delivery. Walmart has the digital version of Pikmin"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/1013381/jad-abumrad-radiolab-dolly-parton-fela-kuti-podcast-interview",
    "domain": "大厂 AI 动态",
    "title": "Jad Abumrad loves a butterfly knife and a good springy pillow",
    "url": "https://www.theverge.com/entertainment/1013381/jad-abumrad-radiolab-dolly-parton-fela-kuti-podcast-interview",
    "source": "Terrence O’Brien",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T14:30:00+00:00",
    "summary": "It's hard to overstate Jad Abumrad's impact on the podcasting world. He created and hosted Dolly Parton's America and Fela Kuti: Fear No Man, two Peabody Award-winning shows that offered unprecedented"
  },
  {
    "id": "rss:https://www.theverge.com/podcast/1012416/spacex-starlink-elon-musk-cell-carrier-wireless-mobile-att-verizon-t-mobile",
    "domain": "大厂 AI 动态",
    "title": "SpaceX’s ambitious, expensive gamble to replace AT&#038;T, T-Mobile, and Verizon",
    "url": "https://www.theverge.com/podcast/1012416/spacex-starlink-elon-musk-cell-carrier-wireless-mobile-att-verizon-t-mobile",
    "source": "Nilay Patel",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T14:00:00+00:00",
    "summary": "Today, I’m talking with Walter Piecyk, a partner and analyst at LightShed Partners who covers tech, media, and telecom, about SpaceX’s recently announced plan to become a major wireless carrier. Last "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web",
    "domain": "大厂 AI 动态",
    "title": "Websites are closing their doors to AI agents",
    "url": "https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T13:00:00+00:00",
    "summary": "Autonomous agents are the hottest thing in AI. OpenAI, Meta, Google, Instinct, and others promise their agents can scour the internet on your behalf, doing anything from booking a dinner reservation a"
  },
  {
    "id": "rss:https://www.theverge.com/tech/1013320/bose-noise-cancelling-wired-earbuds-review",
    "domain": "大厂 AI 动态",
    "title": "Bose’s new wired earbuds are simple in the best way",
    "url": "https://www.theverge.com/tech/1013320/bose-noise-cancelling-wired-earbuds-review",
    "source": "John Higgins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T13:00:00+00:00",
    "summary": "After Apple courageously removed the headphone jack from the iPhone in 2016, most people switched to Bluetooth earbuds and never looked back. But their wired counterparts have stuck around, and their "
  },
  {
    "id": "rss:https://www.theverge.com/tech/1012820/apple-homeview-recipe-formatting",
    "domain": "大厂 AI 动态",
    "title": "Apple’s HomeView is just the latest threat to online recipe writers",
    "url": "https://www.theverge.com/tech/1012820/apple-homeview-recipe-formatting",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T12:00:00+00:00",
    "summary": "When Apple revealed the HomeView to the world, it did so with an unusual ad for the company: Instead of pristine, polished tech in immaculate rooms, it's a three-minute look at the messy, frantic morn"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/17/meta-removes-language-that-raised-scraping-and-ai-training-concerns/",
    "domain": "大厂 AI 动态",
    "title": "Meta removes language that raised scraping and AI training concerns",
    "url": "https://techcrunch.com/2026/10/17/meta-removes-language-that-raised-scraping-and-ai-training-concerns/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T21:31:32+00:00",
    "summary": "A Meta spokesperson insisted that the updated terms did not reflect a change in the way Meta crawls the web."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/17/tiktok-permanently-bans-musk-documentary-advertising-account/",
    "domain": "大厂 AI 动态",
    "title": "TikTok permanently bans ‘Musk’ documentary advertising account",
    "url": "https://techcrunch.com/2026/10/17/tiktok-permanently-bans-musk-documentary-advertising-account/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T20:55:52+00:00",
    "summary": "A four-hour documentary about Elon Musk continues to meet resistance from social media platforms."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/17/anthropic-says-its-workforce-has-become-less-junior-and-is-spending-more-time-in-meetings/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic says its workforce has become less junior and is spending more time in meetings",
    "url": "https://techcrunch.com/2026/10/17/anthropic-says-its-workforce-has-become-less-junior-and-is-spending-more-time-in-meetings/",
    "source": "Anthony Ha",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T20:21:19+00:00",
    "summary": "The composition of Anthropic’s workforce and the type of work getting done have changed significantly in the past year."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/17/replit-is-no-longer-working-with-anthropic-ceo-says/",
    "domain": "大厂 AI 动态",
    "title": "Replit makes OpenAI its default over Anthropic, CEO says",
    "url": "https://techcrunch.com/2026/10/17/replit-is-no-longer-working-with-anthropic-ceo-says/",
    "source": "Kirsten Korosec, Lucas Ropek, Rebecca Bellan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T18:48:08+00:00",
    "summary": "Over the weekend, Masad clarified that OpenAI would replace Anthropic as its default model provider. Claude will still be available to customers on the platform."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/17/embers-new-temperature-controlled-mug-makes-my-nightly-tea-ritual-even-better/",
    "domain": "大厂 AI 动态",
    "title": "Ember’s new temperature-controlled mug makes my nightly tea ritual even better",
    "url": "https://techcrunch.com/2026/10/17/embers-new-temperature-controlled-mug-makes-my-nightly-tea-ritual-even-better/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T15:30:00+00:00",
    "summary": "The biggest change about Ember's new mug is that you no longer have to open the app to adjust your drink’s temperature."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/mark-wahlberg-wants-to-take-on-the-longevity-startup-crowd-with-an-affordable-gym-concept/",
    "domain": "大厂 AI 动态",
    "title": "Mark Wahlberg wants to take on the longevity-startup crowd with an affordable gym concept",
    "url": "https://techcrunch.com/2026/10/16/mark-wahlberg-wants-to-take-on-the-longevity-startup-crowd-with-an-affordable-gym-concept/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T02:36:18+00:00",
    "summary": "Mark Wahlberg, who once sank money into a gym chain that got kicked off the NYSE, is now building his own, and he promises you’ll get a cold plunge, a blood panel and a protein muffin without needing "
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/porsches-electric-macan-turbo-is-an-automotive-existential-crisis/",
    "domain": "大厂 AI 动态",
    "title": "Porsche’s electric Macan Turbo is an automotive existential crisis",
    "url": "https://techcrunch.com/2026/10/16/porsches-electric-macan-turbo-is-an-automotive-existential-crisis/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T19:40:00+00:00",
    "summary": "The 2026 Porsche Macan Turbo EV is a two-row crossover with 630 horsepower and a 100-kilowatt-hour battery."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/india-becomes-the-latest-country-to-report-rogue-ai-agent-activity/",
    "domain": "大厂 AI 动态",
    "title": "India becomes the latest country to report rogue AI agent activity",
    "url": "https://techcrunch.com/2026/10/16/india-becomes-the-latest-country-to-report-rogue-ai-agent-activity/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T17:52:24+00:00",
    "summary": "The agents got in through credentials and connection settings left exposed in app configurations, public code repositories, and overly permissive cloud roles."
  },
  {
    "id": "rss:https://techcrunch.com/video/a-nvidia-insider-turned-vc-on-why-robotics-hasnt-hit-its-chatgpt-moment-yet/",
    "domain": "大厂 AI 动态",
    "title": "An Nvidia insider-turned-VC on why robotics hasn’t hit its ChatGPT moment, yet",
    "url": "https://techcrunch.com/video/a-nvidia-insider-turned-vc-on-why-robotics-hasnt-hit-its-chatgpt-moment-yet/",
    "source": "Theresa Loconsolo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:30:00+00:00",
    "summary": "Amulya Vishwanath, who spent seven years leading product marketing for NVIDIA’s robotics platforms, says robotics is currently in its “Lego era,” with the basic building blocks like actuators, robotic"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/waymos-robotaxis-are-headed-to-canada/",
    "domain": "大厂 AI 动态",
    "title": "Waymo’s robotaxis are headed to Canada",
    "url": "https://techcrunch.com/2026/10/16/waymos-robotaxis-are-headed-to-canada/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:06:38+00:00",
    "summary": "The company will start off by testing its self-driving vehicles on Toronto's streets."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/elorians-first-ai-model-wants-to-reason-with-images-not-just-about-them/",
    "domain": "大厂 AI 动态",
    "title": "Elorian’s first AI model wants to reason with images, not just about them",
    "url": "https://techcrunch.com/2026/10/16/elorians-first-ai-model-wants-to-reason-with-images-not-just-about-them/",
    "source": "Aditya Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:01:37+00:00",
    "summary": "According to Elorian's evaluations, Glimpse outperforms even GPT-6 Astra on scientific chart reasoning and short-form video captioning, with competitive results on other visual reasoning tasks."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/tressfecta-wants-to-make-hair-braiding-a-less-arduous-task-for-hairstylists/",
    "domain": "大厂 AI 动态",
    "title": "Tressfecta wants to make hair braiding a less arduous task for hairstylists",
    "url": "https://techcrunch.com/2026/10/16/tressfecta-wants-to-make-hair-braiding-a-less-arduous-task-for-hairstylists/",
    "source": "Dominic-Madori Davis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:00:00+00:00",
    "summary": "Tressfecta builds products for textured hair. Its first project is a tool called Plait Pilot that helps braiders with the initial process of separating hair from packs before braiding begins."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/in-you-can-see-everything-elizabeth-holmes-meets-her-equal-in-comedian-nathan-fielder/",
    "domain": "大厂 AI 动态",
    "title": "In ‘You Can See Everything,’ Elizabeth Holmes meets her equal in comedian Nathan Fielder",
    "url": "https://techcrunch.com/2026/10/16/in-you-can-see-everything-elizabeth-holmes-meets-her-equal-in-comedian-nathan-fielder/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T16:00:00+00:00",
    "summary": "Nathan Fielder's documentary about disgraced Theranos CEO Elizabeth Holmes has created a constellation of colliding personas that interrogate the very nature of authenticity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/jev-is-vercels-fastest-adopted-ai-model-ever/",
    "domain": "大厂 AI 动态",
    "title": "Jev is Vercel’s fastest-adopted AI model ever",
    "url": "https://techcrunch.com/2026/10/16/jev-is-vercels-fastest-adopted-ai-model-ever/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T15:33:49+00:00",
    "summary": "The data comes from Vercel's AI gateway, a unified API service similar to OpenRouter."
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/mark-wahlberg-on-using-ai-in-film-the-right-way-and-being-open-to-an-ai-clone-carrying-on-his-legacy/",
    "domain": "大厂 AI 动态",
    "title": "Mark Wahlberg on using AI in film ‘the right way’ and being open to an AI clone carrying on his legacy",
    "url": "https://techcrunch.com/2026/10/16/mark-wahlberg-on-using-ai-in-film-the-right-way-and-being-open-to-an-ai-clone-carrying-on-his-legacy/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T14:26:51+00:00",
    "summary": "Actor and angel investor Mark Wahlberg says he's OK with using AI in filmmaking, provided it's used \"to enhance what you're doing.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/veritas-is-building-a-chip-to-verify-luxury-goods/",
    "domain": "大厂 AI 动态",
    "title": "Veritas expands its anti-counterfeit chip to jewelry, trophies, and fragrance bottles",
    "url": "https://techcrunch.com/2026/10/16/veritas-is-building-a-chip-to-verify-luxury-goods/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T14:00:00+00:00",
    "summary": "Counterfeiters are getting better at replicating brands' marks and passing off dupes, known as \"superfakes,\" as genuine items. A startup called Veritas wants to tackle the problem with its own chip th"
  },
  {
    "id": "rss:https://techcrunch.com/2026/10/16/replits-ceo-says-the-future-of-work-is-the-self-driving-company/",
    "domain": "大厂 AI 动态",
    "title": "Replit’s CEO says the future of work is the ‘self-driving company’",
    "url": "https://techcrunch.com/2026/10/16/replits-ceo-says-the-future-of-work-is-the-self-driving-company/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T12:55:09+00:00",
    "summary": "Replit CEO Amjad Masad envisions a future of “self-driving companies,” where AI agents handle day-to-day tasks and people focus on higher-level decisions."
  },
  {
    "id": "rss:https://stratechery.com/2026/home-at-last/",
    "domain": "大厂 AI 动态",
    "title": "2026.42: Home At Last",
    "url": "https://stratechery.com/2026/home-at-last/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T17:42:42+00:00",
    "summary": "The best Stratechery content from the week of October 12, 2026, including what Apple is doing, SpaceX's appetite, and the title, takes, and the Washington Wizards."
  },
  {
    "id": "rss:https://arstechnica.com/science/2026/10/science-says-your-boss-should-talk-less-in-meetings/",
    "domain": "大厂 AI 动态",
    "title": "Science says your boss should talk less in meetings",
    "url": "https://arstechnica.com/science/2026/10/science-says-your-boss-should-talk-less-in-meetings/",
    "source": "Lesley Evans Ogden, Knowable Magazine",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T11:15:11+00:00",
    "summary": "Research suggests listening more while talking less. Killing aimless meetings can help, too."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/10/why-biowares-neverwinter-nights-still-has-thousands-of-active-players/",
    "domain": "大厂 AI 动态",
    "title": "Why BioWare's Neverwinter Nights still has thousands of active players",
    "url": "https://arstechnica.com/gaming/2026/10/why-biowares-neverwinter-nights-still-has-thousands-of-active-players/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-17T11:00:21+00:00",
    "summary": "The single-player is just OK, but according to the players, that doesn't matter."
  },
  {
    "id": "rss:https://arstechnica.com/security/2026/10/openai-models-hacked-a-crypto-wallet-and-breached-more-websites/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI models hacked a crypto wallet and breached more websites",
    "url": "https://arstechnica.com/security/2026/10/openai-models-hacked-a-crypto-wallet-and-breached-more-websites/",
    "source": "Dan Goodin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T20:59:01+00:00",
    "summary": "The actions could have resulted in criminal charges had humans been behind the keyboard."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/10/thegentlemanpervert-producing-ai-csam-is-a-nj-prosecutor-say-cops/",
    "domain": "大厂 AI 动态",
    "title": "“thegentlemanpervert” producing AI CSAM is a NJ prosecutor, say cops",
    "url": "https://arstechnica.com/tech-policy/2026/10/thegentlemanpervert-producing-ai-csam-is-a-nj-prosecutor-say-cops/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T20:20:07+00:00",
    "summary": "Discord user flagged AI CSAM, triggering arrest of New Jersey deputy AG."
  },
  {
    "id": "rss:https://arstechnica.com/gaming/2026/10/us-rep-proposes-bill-to-give-video-game-buyers-ownership-not-a-license/",
    "domain": "大厂 AI 动态",
    "title": "US Rep proposes bill to give video game buyers \"ownership,\" not \"a license\"",
    "url": "https://arstechnica.com/gaming/2026/10/us-rep-proposes-bill-to-give-video-game-buyers-ownership-not-a-license/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T19:41:18+00:00",
    "summary": "There are still significant hurdles ahead, both technical and legislative."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/10/ray-ban-meta-smart-glasses-found-recording-audio-without-wearers-consent/",
    "domain": "大厂 AI 动态",
    "title": "Bug turns one of the biggest fears about Ray-Ban Meta smart glasses into reality",
    "url": "https://arstechnica.com/gadgets/2026/10/ray-ban-meta-smart-glasses-found-recording-audio-without-wearers-consent/",
    "source": "Scharon Harding",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T19:11:50+00:00",
    "summary": "The bug is fixed, but privacy concerns remain."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/10/rfk-jr-proposes-fda-look-the-other-way-on-unproven-peptides-report-says/",
    "domain": "大厂 AI 动态",
    "title": "RFK Jr. proposes FDA look the other way on unproven peptides, report says",
    "url": "https://arstechnica.com/health/2026/10/rfk-jr-proposes-fda-look-the-other-way-on-unproven-peptides-report-says/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T17:05:59+00:00",
    "summary": "FDA scientists said none of the popular drugs have been proven safe or effective."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/10/meta-may-use-sweeping-new-commercial-tos-to-avoid-millions-in-ai-licensing-fees/",
    "domain": "大厂 AI 动态",
    "title": "Meta may use sweeping new commercial TOS to avoid millions in AI licensing fees",
    "url": "https://arstechnica.com/tech-policy/2026/10/meta-may-use-sweeping-new-commercial-tos-to-avoid-millions-in-ai-licensing-fees/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-10-16T15:41:00+00:00",
    "summary": "Meta “streamlined” its commercial TOS. Legal experts warn it’s an AI power grab."
  },
  {
    "id": "hn:49826087",
    "domain": "股票",
    "title": "16GB iPod Nano 3G Upgrade",
    "url": "https://tuckerosman.com/projects/16gb-ipod-nano",
    "source": "Ivoah",
    "platform": "hackernews",
    "points": 167,
    "published_at": "2026-09-24T03:58:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:49886005",
    "domain": "股票",
    "title": "Anthropic's IPO prospectus shows AI vision, surging costs",
    "url": "https://www.reuters.com/business/finance/anthropics-ipo-prospectus-shows-sweeping-ai-vision-surging-costs-2026-09-28/",
    "source": "6thbit",
    "platform": "hackernews",
    "points": 145,
    "published_at": "2026-09-28T23:40:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:50122366",
    "domain": "股票",
    "title": "Anthropic's Valuation Collapsed by $500B",
    "url": "https://www.telegraph.co.uk/business/2026/10/16/anthropic-valuation-ipo-ai-stock-listing/",
    "source": "novaRom",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-10-16T18:27:58+00:00",
    "summary": ""
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
    "id": "hn:50098423",
    "domain": "股票",
    "title": "Asia chip stocks fall, AI funding worries",
    "url": "https://www.cnbc.com/2026/10/15/sk-hynix-samsung-softbank-stocks-asia-tech-rout-ai-funding-worries.html",
    "source": "kristianp",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-15T02:29:41+00:00",
    "summary": ""
  },
  {
    "id": "hn:50113666",
    "domain": "股票",
    "title": "South Korea's stock market down, president telling people not to commit suicide",
    "url": "https://twitter.com/litcapital/status/2110752546415382699",
    "source": "toomuchtodo",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-16T03:26:08+00:00",
    "summary": ""
  },
  {
    "id": "hn:50086344",
    "domain": "股票",
    "title": "Humxn Commits $50M to Buy Skilled Trades Data for Robotics Training",
    "url": "https://markets.businessinsider.com/news/stocks/humxn-research-labs-wants-to-buy-50-million-worth-of-skilled-trades-farming-and-manufacturing-data-for-ai-robotics-training-1036622854",
    "source": "howdoweknowit",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-10-14T12:04:10+00:00",
    "summary": ""
  },
  {
    "id": "hn:50113735",
    "domain": "股票",
    "title": "CoreWeave Founders Shield Fortunes with $3.3B Stock Sales",
    "url": "https://www.bloomberg.com/news/articles/2026-10-15/coreweave-founders-shield-fortunes-with-3-3-billion-stock-sales",
    "source": "qlte",
    "platform": "hackernews",
    "points": 10,
    "published_at": "2026-10-16T03:34:02+00:00",
    "summary": ""
  },
  {
    "id": "hn:50029452",
    "domain": "股票",
    "title": "Data Center Darling Firmus's $30B IPO Dream Crushed in 48 Hours",
    "url": "https://www.bloomberg.com/news/articles/2026-10-09/data-center-darling-s-30-billion-ipo-dream-crushed-in-48-hours",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-10-10T04:04:17+00:00",
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
    "id": "hn:49914149",
    "domain": "股票",
    "title": "Anthropic's IPO Prospectus Is a Fucking Doozy",
    "url": "https://daringfireball.net/linked/2026/09/30/reuters-anthropic-ipo-prospectus",
    "source": "danaris",
    "platform": "hackernews",
    "points": 71,
    "published_at": "2026-09-30T20:44:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:49997175",
    "domain": "股票",
    "title": "The world has nearly burned through its oil stockpile buffer",
    "url": "https://www.reuters.com/business/energy/world-has-nearly-burned-through-its-oil-stockpile-buffer-executives-say-2026-10-06/",
    "source": "geox",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-10-07T18:50:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:50071744",
    "domain": "股票",
    "title": "Sprout Pi Mainboard – A modern, RP2350-powered motherboard for iPods",
    "url": "https://www.crowdsupply.com/certain-things/sprout-pi-mainboard",
    "source": "esskay",
    "platform": "hackernews",
    "points": 21,
    "published_at": "2026-10-13T13:49:44+00:00",
    "summary": ""
  },
  {
    "id": "hn:50082283",
    "domain": "股票",
    "title": "US Says Chinese Hackers Attacked DOJ, NASA, Federal Reserve, Senate",
    "url": "https://www.usatoday.com/story/news/politics/2026/08/26/chinese-hackers-cyberattack-us-government/91473585007/",
    "source": "gmays",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-10-14T04:09:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50019535",
    "domain": "股票",
    "title": "Meadows – a small language for stock-and-flow diagrams that run",
    "url": "https://lorezzed.github.io/meadows/",
    "source": "jjsalamon",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-09T12:29:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50029232",
    "domain": "股票",
    "title": "Data centre company's much-hyped Australian stock market listing imploded",
    "url": "https://www.theguardian.com/australia-news/2026/oct/09/firmus-australian-stock-market-listing-bust-finance",
    "source": "stubish",
    "platform": "hackernews",
    "points": 22,
    "published_at": "2026-10-10T03:23:09+00:00",
    "summary": ""
  },
  {
    "id": "hn:50008977",
    "domain": "股票",
    "title": "Frontier AI models outperform analysts on earnings prediction",
    "url": "https://samaya.ai/blog/frontier-ai-models-outperform-human-experts-on-earnings-prediction",
    "source": "ashwinpp",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-10-08T17:33:29+00:00",
    "summary": ""
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
    "id": "hn:50020096",
    "domain": "股票",
    "title": "Ask HN: What if no AIpocalypse, no AI bubble, what if it just keeps advancing?",
    "url": "https://news.ycombinator.com/item?id=50020096",
    "source": "consumer451",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-10-09T13:18:05+00:00",
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
    "id": "hn:50112657",
    "domain": "金融",
    "title": "Tesla Roadster",
    "url": "https://www.tesla.com/roadster",
    "source": "shekhar101",
    "platform": "hackernews",
    "points": 1615,
    "published_at": "2026-10-16T01:32:45+00:00",
    "summary": ""
  },
  {
    "id": "hn:49778029",
    "domain": "金融",
    "title": "Samsung is expected to more than double output of its HBM4 and HBM4E DRAM",
    "url": "https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 562,
    "published_at": "2026-09-20T17:38:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49948254",
    "domain": "金融",
    "title": "Federal judge calls Flock 'indiscriminate mass surveillance'",
    "url": "https://techcrunch.com/2026/10/03/federal-judge-calls-flock-indiscriminate-mass-surveillance/",
    "source": "sbulaev",
    "platform": "hackernews",
    "points": 503,
    "published_at": "2026-10-03T22:07:13+00:00",
    "summary": ""
  },
  {
    "id": "hn:49824686",
    "domain": "金融",
    "title": "Feds Target AI Critics as \"Foreign Agents\"",
    "url": "https://www.kenklippenstein.com/p/feds-think-ai-critics-are-foreign",
    "source": "nmeagent",
    "platform": "hackernews",
    "points": 396,
    "published_at": "2026-09-24T00:41:31+00:00",
    "summary": ""
  },
  {
    "id": "hn:49875913",
    "domain": "金融",
    "title": "Parley: Federated, decentralised chat that speaks plain IRC",
    "url": "https://git.mills.io/prologic/parley",
    "source": "davidcollantes",
    "platform": "hackernews",
    "points": 330,
    "published_at": "2026-09-28T10:30:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:50131440",
    "domain": "金融",
    "title": "US federal budget deficit jumps 12% in one year to nearly $2 Trillion",
    "url": "https://finance.yahoo.com/economy/policy/article/the-us-federal-budget-deficit-for-2026-just-came-in-its-1992-trillion-191917669.html",
    "source": "ck2",
    "platform": "hackernews",
    "points": 185,
    "published_at": "2026-10-17T14:22:05+00:00",
    "summary": ""
  },
  {
    "id": "hn:49921118",
    "domain": "金融",
    "title": "Meta Uses A.I. Data Centers to Avoid Billions in Federal Taxes",
    "url": "https://www.nytimes.com/2026/09/30/technology/meta-ai-data-centers-taxes.html",
    "source": "gmays",
    "platform": "hackernews",
    "points": 259,
    "published_at": "2026-10-01T13:05:51+00:00",
    "summary": ""
  },
  {
    "id": "hn:49822556",
    "domain": "金融",
    "title": "OpenAI breaches Medicare, Albanese reveals",
    "url": "https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html",
    "source": "jonnonz",
    "platform": "hackernews",
    "points": 256,
    "published_at": "2026-09-23T21:01:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:50059446",
    "domain": "金融",
    "title": "Feds got warrants to use fake cell towers to hunt down Don Lemon's producer",
    "url": "https://www.wired.com/story/feds-got-warrants-to-use-fake-cell-towers-to-hunt-down-don-lemons-producer/",
    "source": "rndsignals",
    "platform": "hackernews",
    "points": 196,
    "published_at": "2026-10-12T17:08:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50090662",
    "domain": "金融",
    "title": "Tesla's Robotaxis Blow Through School Zones, NHTSA Petition Alleges",
    "url": "https://www.extremetech.com/cars/teslas-robotaxis-blow-through-school-zones-nhtsa-petition-alleges",
    "source": "speckx",
    "platform": "hackernews",
    "points": 146,
    "published_at": "2026-10-14T16:45:19+00:00",
    "summary": ""
  },
  {
    "id": "hn:50057956",
    "domain": "金融",
    "title": "French supermarkets suffer fridge shutdown after 'unprecedented' cyberattack",
    "url": "https://uk.finance.yahoo.com/news/french-supermarket-chains-cyberattack-forced-115141288.html",
    "source": "thinkcontext",
    "platform": "hackernews",
    "points": 155,
    "published_at": "2026-10-12T15:36:21+00:00",
    "summary": ""
  },
  {
    "id": "hn:50116255",
    "domain": "金融",
    "title": "Tesla's new Roadster makes a flying debut, hitting 60 MPH in under a second",
    "url": "https://www.foxbusiness.com/technology/teslas-new-roadster-makes-flying-debut-hitting-60-mph-under-second",
    "source": "nsoonhui",
    "platform": "hackernews",
    "points": 70,
    "published_at": "2026-10-16T09:40:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:50118624",
    "domain": "金融",
    "title": "Tesla unveils 'flying' Roadster with SpaceX thrusters [video]",
    "url": "https://www.youtube.com/watch?v=eqOfmtTJD1A",
    "source": "skadamat",
    "platform": "hackernews",
    "points": 63,
    "published_at": "2026-10-16T14:12:15+00:00",
    "summary": ""
  },
  {
    "id": "hn:50080275",
    "domain": "金融",
    "title": "Show HN: Pulse Local, a Mac budgeting app whose AI models run on your machine",
    "url": "https://pulseos.finance",
    "source": "niztk",
    "platform": "hackernews",
    "points": 121,
    "published_at": "2026-10-13T23:13:23+00:00",
    "summary": ""
  },
  {
    "id": "hn:50082021",
    "domain": "金融",
    "title": "Strafe: A new open-source, E2E Encrypted, and federated alternative to Discord",
    "url": "https://strafe.chat/",
    "source": "brydencalaway",
    "platform": "hackernews",
    "points": 118,
    "published_at": "2026-10-14T03:28:00+00:00",
    "summary": ""
  },
  {
    "id": "hn:49981063",
    "domain": "金融",
    "title": "Former German spy chief arrested for attempted treason",
    "url": "https://www.reuters.com/business/finance/former-german-spy-chief-detained-suspicion-espionage-treason-bild-reports-2026-10-06/",
    "source": "semiquaver",
    "platform": "hackernews",
    "points": 130,
    "published_at": "2026-10-06T16:51:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:50049302",
    "domain": "金融",
    "title": "Governments are mishandling the affordability crisis",
    "url": "https://www.economist.com/finance-and-economics/2026/10/08/governments-are-mishandling-the-affordability-crisis",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 105,
    "published_at": "2026-10-11T23:40:06+00:00",
    "summary": ""
  },
  {
    "id": "hn:50105900",
    "domain": "金融",
    "title": "Market selloff, rising rates test AI data centre deal boom",
    "url": "https://www.reuters.com/business/finance/market-selloff-rising-rates-test-ai-data-centre-deal-boom-2026-10-15/",
    "source": "tartoran",
    "platform": "hackernews",
    "points": 75,
    "published_at": "2026-10-15T16:17:40+00:00",
    "summary": ""
  },
  {
    "id": "hn:50114077",
    "domain": "金融",
    "title": "Tesla makes cars that fly? [video]",
    "url": "https://www.youtube.com/watch?v=7p5LxFdc-Qg",
    "source": "merinpapz10",
    "platform": "hackernews",
    "points": 69,
    "published_at": "2026-10-16T04:27:54+00:00",
    "summary": ""
  },
  {
    "id": "hn:50122776",
    "domain": "金融",
    "title": "Show HN: Stoke Money – Personal finance app built around a cash flow forecast",
    "url": "https://stoke.money",
    "source": "_wesley",
    "platform": "hackernews",
    "points": 32,
    "published_at": "2026-10-16T18:54:47+00:00",
    "summary": ""
  },
  {
    "id": "hn:49916668",
    "domain": "金融",
    "title": "10-year Treasury yield climbs above 5.3% to a level not seen in 24 years",
    "url": "https://www.wsj.com/finance/investing/surging-yields-bring-the-bond-market-back-to-the-turn-of-the-century-2b74773f",
    "source": "kaycebasques",
    "platform": "hackernews",
    "points": 125,
    "published_at": "2026-10-01T01:40:50+00:00",
    "summary": ""
  },
  {
    "id": "hn:49832844",
    "domain": "金融",
    "title": "Federal judge orders Texas to air condition all prisons by the end of 2029",
    "url": "https://www.texastribune.org/2026/09/22/texas-prison-air-conditioning-lawsuit-ruling/",
    "source": "bonefishgrill",
    "platform": "hackernews",
    "points": 120,
    "published_at": "2026-09-24T16:15:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:50112380",
    "domain": "金融",
    "title": "Tesla Debuts 2026 Roadster",
    "url": "https://www.nytimes.com/2026/10/15/business/tesla-roadster-2026-ev-sports-car.html",
    "source": "andsoitis",
    "platform": "hackernews",
    "points": 38,
    "published_at": "2026-10-16T00:57:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49916955",
    "domain": "金融",
    "title": "Cities Are Forced to Funnel License Plate Data to a Federal Surveillance Program",
    "url": "https://www.404media.co/how-cities-are-forced-to-funnel-license-plate-data-to-a-massive-federal-surveillance-program-hidta/",
    "source": "ripe",
    "platform": "hackernews",
    "points": 93,
    "published_at": "2026-10-01T02:26:17+00:00",
    "summary": ""
  },
  {
    "id": "hn:50074739",
    "domain": "金融",
    "title": "Americans Trust in Federal Government Sinks to New Depths",
    "url": "https://news.gallup.com/poll/715361/trust-federal-government-sinks-new-depths.aspx",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-10-13T16:48:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:50062076",
    "domain": "金融",
    "title": "\"Today we're laying off a large part of the Airtable team \"",
    "url": "https://twitter.com/fedesimio/status/2109713695165329511",
    "source": "tortilla",
    "platform": "hackernews",
    "points": 45,
    "published_at": "2026-10-12T19:56:16+00:00",
    "summary": ""
  },
  {
    "id": "hn:50023065",
    "domain": "金融",
    "title": "Tesla Rebrands Full Self-Driving as Tesla Assisted Driving in Europe",
    "url": "https://qz.com/tesla-full-self-driving-rebranding-europe-assisted-driving-100926",
    "source": "ilreb",
    "platform": "hackernews",
    "points": 53,
    "published_at": "2026-10-09T16:38:20+00:00",
    "summary": ""
  },
  {
    "id": "hn:49938815",
    "domain": "金融",
    "title": "Federal Judge Rules a Flock Search Was Unconstitutional",
    "url": "https://www.404media.co/federal-judge-rules-a-flock-search-was-indiscriminate-mass-surveillance-and-unconstitutional/",
    "source": "pavel_lishin",
    "platform": "hackernews",
    "points": 55,
    "published_at": "2026-10-02T21:28:59+00:00",
    "summary": ""
  },
  {
    "id": "hn:49930690",
    "domain": "金融",
    "title": "Quantitative Finance with OCaml",
    "url": "https://qcaml.com/index.html",
    "source": "leonry",
    "platform": "hackernews",
    "points": 54,
    "published_at": "2026-10-02T07:14:34+00:00",
    "summary": ""
  },
  {
    "id": "hn:49849986",
    "domain": "金融",
    "title": "Show HN: Ekselio – Loveable for finance workflows (local first)",
    "url": "https://www.gptbeyond.com/try?home=1",
    "source": "kdautaj",
    "platform": "hackernews",
    "points": 43,
    "published_at": "2026-09-25T21:09:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:49769668",
    "domain": "金融",
    "title": "OpenAI and Anthropic oversold AI security breaches",
    "url": "https://nypost.com/2026/09/19/us-news/openai-anthropic-oversold-security-breaches-to-pressure-feds-into-protecting-turf-insiders/",
    "source": "hei-lima",
    "platform": "hackernews",
    "points": 39,
    "published_at": "2026-09-19T19:59:28+00:00",
    "summary": ""
  },
  {
    "id": "hn:49924299",
    "domain": "金融",
    "title": "Sony released the first CD audio player on this day in 1982",
    "url": "https://www.tomshardware.com/pc-components/storage/sony-released-the-first-cd-audio-player-on-this-day-in-1982-player-cost-usd3-700-when-adjusted-for-inflation-but-it-would-be-another-decade-before-the-cd-rom-driven-multimedia-pc-era-began",
    "source": "Brajeshwar",
    "platform": "hackernews",
    "points": 15,
    "published_at": "2026-10-01T17:07:39+00:00",
    "summary": ""
  }
]
```
