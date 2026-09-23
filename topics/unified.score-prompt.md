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

- 今日日期：`2026-09-23`
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
  "date": "2026-09-23",
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
    "id": "bvid:BV1rq4y117uA",
    "domain": "AI",
    "title": "保姆级教程！教你开设MC服务器，自己当服主权限不求人！【我的世界】",
    "url": "http://www.bilibili.com/video/av592774390",
    "source": "苏打baka",
    "platform": "bilibili",
    "points": 2446655,
    "published_at": "2022-01-01T15:08:21+00:00",
    "summary": "教程类视频制作不易 点个收藏随时回来学习\n投币加经验！轻松到LV6！\n喜欢的话别忘了关注苏打！\n你的支持是我更新的最大动力！\n↓↓↓↓↓视频中使用到的连接↓↓↓↓↓\nspigot核心下载：https://getbukkit.org/download/spigot\nWIKI解释：https://minecraft.fandom.com/zh/wiki/Server.properties?so=sea"
  },
  {
    "id": "bvid:BV1E7wtzaEdq",
    "domain": "AI",
    "title": "从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！",
    "url": "http://www.bilibili.com/video/av116227955497963",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 1985818,
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
    "points": 1897998,
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
    "points": 1592454,
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
    "points": 1325185,
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
    "points": 1319112,
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
    "points": 1268929,
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
    "points": 964428,
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
    "points": 945590,
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
    "points": 890144,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1GsY76dEqW",
    "domain": "AI",
    "title": "一口气搞懂Agent到底怎么用！",
    "url": "http://www.bilibili.com/video/av117252103997988",
    "source": "GenJi是真想教会你",
    "platform": "bilibili",
    "points": 813318,
    "published_at": "2026-09-11T11:30:00+00:00",
    "summary": "AI Agent这两年大家都听麻了，但真到上手，claude、codex这些又是注册、又是命令行，人还没踏进Agent大门，就先被劝退了。这期视频我用0门槛的国产Agent——字节旗下的TraeWork，用六个超真实的案例，手把手带你玩转Agent！完整的文字教程和GitHub神级Skill清单，打包放置顶评论了。教程制作不易，觉得有一点点帮助的话，记得一键三连～"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 803843,
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
    "points": 690386,
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
    "points": 673893,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1RSFUzVEAG",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码",
    "url": "http://www.bilibili.com/video/av116045469783373",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 581497,
    "published_at": "2026-02-10T08:59:28+00:00",
    "summary": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码"
  },
  {
    "id": "bvid:BV1SRM86xEPE",
    "domain": "AI",
    "title": "一口气学会 Vibe Coding AI 编程！从开荒到做出第一个项目【附完整文档】【Cursor】【0基础教学】",
    "url": "http://www.bilibili.com/video/av116879800665673",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 443180,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1Vz3v6XE7w",
    "domain": "AI",
    "title": "纯手搓一部AI漫剧一个月收获3.1w！附教程！全流程操作演示！让零基础也能学会AI漫剧制作技巧！更多AI漫剧工具提示词+变现方法及全套教程都整啦！拿走不谢~",
    "url": "http://www.bilibili.com/video/av116996553312339",
    "source": "comfyui视频工作流",
    "platform": "bilibili",
    "points": 381379,
    "published_at": "2026-07-28T12:00:00+00:00",
    "summary": "本套教程从零开始讲解，手把手教学，无论是新手小白，还是有一定经验的选手，皆可学习~\n配套工具软件 | 素材 | AIGC SeeDance2.0 即梦AI 学习路线\n分享给各位还在寻找资料宝子们！一键三联抱走吖\n视频制作不易，同学们觉得对你有帮助的话记得点点关注，一键三连【666】感谢支持！！"
  },
  {
    "id": "bvid:BV1aqjX61E6g",
    "domain": "AI",
    "title": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent",
    "url": "http://www.bilibili.com/video/av116803598557031",
    "source": "大模型开发",
    "platform": "bilibili",
    "points": 373609,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 341882,
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
    "points": 295314,
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
    "points": 293608,
    "published_at": "2026-06-25T09:00:00+00:00",
    "summary": "作者知识星球：https://t.zsxq.com/ubYr8\n作者的第一个VibeCoding：https://github.com/cradiator/memory_map_visualizer"
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 284717,
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
    "points": 266302,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1X8oKBLEdj",
    "domain": "AI",
    "title": "一口气学会AI编程！3个月10万字超详细教学！【项目实操】【0基础教学】【自学教程】【AI编程】【vibecoding】",
    "url": "http://www.bilibili.com/video/av116436177523067",
    "source": "Git源宝",
    "platform": "bilibili",
    "points": 226494,
    "published_at": "2026-04-21T03:15:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料，领取方式：关注后 私信“ 1 ”就好！\n\n后面还会出【一口气学会AI漫剧 】【一口气学会AI Agent 】等系列！大家可以蹲蹲！"
  },
  {
    "id": "bvid:BV154426xEha",
    "domain": "AI",
    "title": "我的 AI 编程全流程：如何使用 AI 稳定交付一个高质量的产品",
    "url": "http://www.bilibili.com/video/av117178586240848",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 221702,
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
    "points": 212517,
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
    "points": 184932,
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
    "points": 182710,
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
    "points": 181946,
    "published_at": "2025-04-18T12:48:54+00:00",
    "summary": "MCPPPPPPPPPPPPPPPPPPPP"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 181383,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV1YG7G6eEPR",
    "domain": "AI",
    "title": "【全60集】吊打付费！目前B站最全最细的Agent智能体开发全套教程！手把手教你打造专属智能体，七天就能从小白到大神！带你从零基础入门到精通实现商业变现！",
    "url": "http://www.bilibili.com/video/av116815090947614",
    "source": "AI-Agent开发",
    "platform": "bilibili",
    "points": 167834,
    "published_at": "2026-06-26T06:57:42+00:00",
    "summary": "【视频配套籽料、学习路线、GitHub项目、实战案例集、电子书+问题解答请看 ”置顶平论” 自取哦】\n本套教程从零开始讲解，手把手教学，包含Python快速入门、AI开发环境搭建及提示词工程、Transformer架构和预训练、SFT、RLHF等一些基础概念、RAG、Agent、Langchain、大模型微调和私有化部署\n无论是新手小白，还是有一定编码经验的选手，皆可学习\n如果视频对你有用的话请 "
  },
  {
    "id": "bvid:BV16NvCBrEVs",
    "domain": "AI",
    "title": "什么是Vibe Coding，以及怎么使用？",
    "url": "http://www.bilibili.com/video/av115797133368973",
    "source": "清华姜学长",
    "platform": "bilibili",
    "points": 165052,
    "published_at": "2025-12-28T12:36:33+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1RNTtzMENj",
    "domain": "AI",
    "title": "从零编写MCP并发布上线，超简单！手把手教程",
    "url": "http://www.bilibili.com/video/av114630814862349",
    "source": "技术爬爬虾",
    "platform": "bilibili",
    "points": 157346,
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
    "points": 122290,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1wDhj6wEa8",
    "domain": "AI",
    "title": "全网刷屏的 Jev 模型正式开放！保姆级教程 + 实战测评",
    "url": "http://www.bilibili.com/video/av117313592367632",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 118571,
    "published_at": "2026-09-22T07:50:41+00:00",
    "summary": "全网爆火的 Jev 模型是什么？有什么用？怎么使用？怎么接入 AI 编程工具（比如 Codex）？效果真的好么？跟 DeepSeek V4 Flash 比速度如何？傻子可懂的 Jev 保姆级实战教程 + 实战测评来啦。\n编程学习教程+实战项目+简历模板：codefather.cn\n免费 AI 编程教程：github.com/liyupi/ai-guide\n记得三连支持、关注鱼皮，让更多朋友学到知识"
  },
  {
    "id": "bvid:BV16hTc6xEpF",
    "domain": "AI",
    "title": "【Codex实战】手摸手教你多Agent协同开发",
    "url": "http://www.bilibili.com/video/av116839870891259",
    "source": "路边爱吃瓜",
    "platform": "bilibili",
    "points": 99490,
    "published_at": "2026-06-30T16:00:22+00:00",
    "summary": "Codex多Agent协同开发"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93777,
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
    "points": 75636,
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
    "points": 75127,
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
    "points": 55380,
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
    "points": 48493,
    "published_at": "2026-04-16T17:16:48+00:00",
    "summary": "Cursor 助手已发布！下载使用文档：https://docs.leokun.cn\n\n我在本地实现了Cursor 的大部分官方服务(主要是bidi+runSSE的grpc)，然后以标准的 Openai API 或Anthropic接口直接发送给其他 API，全程流量都没有到 cursor官方，真正的 local first，支持思维链，支持局域网地址"
  },
  {
    "id": "bvid:BV1ApYD6KEkD",
    "domain": "AI",
    "title": "马斯克收购Cursor后，Cursor的性价比现在已经爆表",
    "url": "http://www.bilibili.com/video/av117254955993228",
    "source": "jopatk",
    "platform": "bilibili",
    "points": 42320,
    "published_at": "2026-09-11T23:19:58+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1utE4z9EML",
    "domain": "AI",
    "title": "自己开发 MCP 服务器，本地大模型调用 MCP",
    "url": "http://www.bilibili.com/video/av114517669314664",
    "source": "新建文件夹X",
    "platform": "bilibili",
    "points": 30765,
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
    "points": 28951,
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
    "points": 26022,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 22943,
    "published_at": "2026-05-15T18:01:19+00:00",
    "summary": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型\n代金券领取链接：https://cloud.siliconflow.cn/i/hkV35uvp\nnodejs下载链接：Node.js — Download Node.js®\ncc-switch下载链接：github.com/farion1231/cc-switch/releases\n安装包和笔记下载链接：http"
  },
  {
    "id": "bvid:BV1CCKq6FEkz",
    "domain": "AI",
    "title": "手搓家庭服务器，让你AI帮你写的网站真正能分享给朋友访问！",
    "url": "http://www.bilibili.com/video/av116945030487459",
    "source": "村里的阿彪",
    "platform": "bilibili",
    "points": 22119,
    "published_at": "2026-07-19T05:43:16+00:00",
    "summary": "用一些二手配件手搓一台家庭服务器，从配件到落地深度了解，端口映射环境配置，内网穿透，一个视频带你了解全套流程！从此你的AI做的程序建的网站，才能真正被别人访问！"
  },
  {
    "id": "bvid:BV1k73y6fEDx",
    "domain": "AI",
    "title": "【ClaudeCode】这绝对是b站讲的最好的Claude Code保姆级全套教程，2026最新版，包含所有干货！七天就能从小白到大神！学完即就业，玩转AI技术",
    "url": "http://www.bilibili.com/video/av117001821488596",
    "source": "爬虫逆向",
    "platform": "bilibili",
    "points": 20290,
    "published_at": "2026-07-29T07:25:00+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n如果视频对你有用的话请 一键三连【长按点赞】支持一下UP哦，拜托，这对我真的很重要！"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 16661,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1cFtv6MEGF",
    "domain": "AI",
    "title": "【吴恩达】全169集（完整版）耗时一个月整理的Vibe Coding课程，从入门到进阶，详细讲解，通俗易懂，适合所有零基础小白学习，学完即可就业！！！",
    "url": "http://www.bilibili.com/video/av117210647369799",
    "source": "吴恩达Agentic",
    "platform": "bilibili",
    "points": 16445,
    "published_at": "2026-09-04T03:31:33+00:00",
    "summary": "视频来源：DeepLearning.AI\n课件代码：评论区自取\n本课程我们将学习到：\n解决 AI 写代码无规范、项目混乱、新旧代码无法兼容、迭代失控等痛点，完整演示一套标准化 AI 软件开发流水线：从环境初始化、项目章程、功能规范编写，到 AI 自动编码、自动化校验、多轮需求迭代、MVP 交付，最后讲解遗留项目改造、自定义工作流、可替换编码 Agent 底层设计，全程带完整项目实操。"
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
    "points": 583,
    "published_at": "2026-09-12T15:08:27+00:00",
    "summary": ""
  },
  {
    "id": "hn:49714096",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC revealing details about next gen A14 node",
    "url": "https://iedm26.mapyourshow.com/8_0/sessions/session-details.cfm?scheduleid=331",
    "source": "osnium123",
    "platform": "hackernews",
    "points": 127,
    "published_at": "2026-09-15T15:31:55+00:00",
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
    "id": "rss:https://www.eetimes.com/canadian-startup-sees-success-in-space-qualification/",
    "domain": "AI 算力 / 半导体",
    "title": "Canadian Startup Sees Success in Space Qualification",
    "url": "https://www.eetimes.com/canadian-startup-sees-success-in-space-qualification/",
    "source": "Gary Hilson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T16:21:10+00:00",
    "summary": "Novigrad is forging a pathway for faster, more accessible radiation testing as a growing wave of space missions drives demand for reliable, resilient electronics. The post Canadian Startup Sees Succes"
  },
  {
    "id": "rss:https://www.eetimes.com/guc-announces-2nm-16-gbps-hbm4e-ip/",
    "domain": "AI 算力 / 半导体",
    "title": "GUC Announces 2nm 16 Gbps HBM4E IP",
    "url": "https://www.eetimes.com/guc-announces-2nm-16-gbps-hbm4e-ip/",
    "source": "Global Unichip Corp. (GUC)",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T13:00:00+00:00",
    "summary": "Discover GUC's design-ready HBM4E PHY and Controller IP, adopted in customers' AI ASICs. The post GUC Announces 2nm 16 Gbps HBM4E IP appeared first on EE Times."
  },
  {
    "id": "rss:https://www.eetimes.com/how-ai-is-accelerating-pcb-design-and-prototyping/",
    "domain": "AI 算力 / 半导体",
    "title": "How AI Is Accelerating PCB Design and Prototyping",
    "url": "https://www.eetimes.com/how-ai-is-accelerating-pcb-design-and-prototyping/",
    "source": "Emily Newton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T07:59:35+00:00",
    "summary": "AI tools compress PCB design timelines from months to hours, enabling faster iteration cycles and letting engineers focus on innovation. The post How AI Is Accelerating PCB Design and Prototyping appe"
  },
  {
    "id": "rss:https://www.eetimes.com/singapore-turning-quantum-research-into-business-opportunity/",
    "domain": "AI 算力 / 半导体",
    "title": "Singapore: Turning Quantum Research into Business Opportunity",
    "url": "https://www.eetimes.com/singapore-turning-quantum-research-into-business-opportunity/",
    "source": "Pietro Guzzetti",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T20:00:00+00:00",
    "summary": "Singapore’s government funding, research infrastructure, and commercial focus are creating a booming regional hub for quantum technologies. The post Singapore: Turning Quantum Research into Business O"
  },
  {
    "id": "rss:https://www.eetimes.com/ai-power-demands-push-gan-into-data-center-design/",
    "domain": "AI 算力 / 半导体",
    "title": "AI Power Demands Push GaN into Data Center Design",
    "url": "https://www.eetimes.com/ai-power-demands-push-gan-into-data-center-design/",
    "source": "Stephen Las Marias",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T16:59:04+00:00",
    "summary": "Rising AI power demands are pushing data center designers toward GaN-based power conversion for higher efficiency and density. The post AI Power Demands Push GaN into Data Center Design appeared first"
  },
  {
    "id": "rss:https://www.eetimes.com/highly-integrated-multibeam-beamformers-offer-swap-benefits-for-payload-phased-array-antennas/",
    "domain": "AI 算力 / 半导体",
    "title": "Highly Integrated Multibeam Beamformers Offer SWaP Benefits for Payload Phased Array Antennas",
    "url": "https://www.eetimes.com/highly-integrated-multibeam-beamformers-offer-swap-benefits-for-payload-phased-array-antennas/",
    "source": "Analog Devices",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T14:00:00+00:00",
    "summary": "Satellite payload designers are under growing pressure to deliver more capacity, wider coverage, and greater flexibility while working within strict size, weight, and power constraints. As phased-arra"
  },
  {
    "id": "rss:https://www.eetimes.com/redefining-intelligent-hmi-at-the-edge-how-ai-is-transforming-human-machine-interaction/",
    "domain": "AI 算力 / 半导体",
    "title": "Redefining Intelligent HMI at the Edge: How AI Is Transforming Human-Machine Interaction",
    "url": "https://www.eetimes.com/redefining-intelligent-hmi-at-the-edge-how-ai-is-transforming-human-machine-interaction/",
    "source": "Omar Cruz, Senior Manager PSOC™ Edge, Infineon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:00:00+00:00",
    "summary": "Next-generation HMI systems are evolving beyond the touchscreen into intelligent, context-aware experiences powered by edge AI The post Redefining Intelligent HMI at the Edge: How AI Is Transforming H"
  },
  {
    "id": "rss:https://www.eetimes.com/design-once-reuse-forever-the-reconfigurable-analog-front-end/",
    "domain": "AI 算力 / 半导体",
    "title": "Design Once, Reuse Forever: The Reconfigurable Analog Front End",
    "url": "https://www.eetimes.com/design-once-reuse-forever-the-reconfigurable-analog-front-end/",
    "source": "Robert Schreiber, Analog Product Marketing Director, Renesas Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:00:00+00:00",
    "summary": "AnalogPAK turns the analog front end into a configurable, reusable design: one PCB supports multiple sensors and ranges with no board re-spin. The post Design Once, Reuse Forever: The Reconfigurable A"
  },
  {
    "id": "rss:https://www.eetimes.com/scaling-physical-ai-deployment-beyond-the-demo/",
    "domain": "AI 算力 / 半导体",
    "title": "Scaling Physical AI Deployment Beyond the Demo",
    "url": "https://www.eetimes.com/scaling-physical-ai-deployment-beyond-the-demo/",
    "source": "Intel Corporation",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:00:00+00:00",
    "summary": "Scaling VLA robotics requires optimized inference, heterogeneous compute and real-time control on edge hardware. The post Scaling Physical AI Deployment Beyond the Demo appeared first on EE Times."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/microsd-cards/beat-the-switch-2-storage-crisis-with-this-usd99-512gb-microsd-express-card-amazon-deal-slashes-33-percent-off-high-performance-samsung-p9",
    "domain": "AI 算力 / 半导体",
    "title": "Beat the Switch 2 storage crisis with this $99 512GB microSD Express card",
    "url": "https://www.tomshardware.com/pc-components/microsd-cards/beat-the-switch-2-storage-crisis-with-this-usd99-512gb-microsd-express-card-amazon-deal-slashes-33-percent-off-high-performance-samsung-p9",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T18:18:55+00:00",
    "summary": "Amazon has slashed 33% off the price of the Samsung P9 microSD Express card for the Nintendo Switch 2, bringing it down to $99.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/durabook-z14i-dx3-rugged-mobile-workstation-folds-three-screens-into-a-9-8-kg-chassis-luggable-targets-military-emergency-services-and-field-professionals",
    "domain": "AI 算力 / 半导体",
    "title": "Durabook Z14I-DX3 rugged mobile workstation folds three screens into a 9.8 kg chassis",
    "url": "https://www.tomshardware.com/laptops/durabook-z14i-dx3-rugged-mobile-workstation-folds-three-screens-into-a-9-8-kg-chassis-luggable-targets-military-emergency-services-and-field-professionals",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T16:33:41+00:00",
    "summary": "Built for military, emergency services and industrial applications, the Z14I-DX3 packs three sunlight-readable 14-inch touchscreens and up to RTX 5000 Ada graphics into one exceptionally rugged mobile"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/get-this-spiffy-stealthy-msi-rtx-5090-for-just-usd4-299-geforce-week-at-walmart-serves-up-a-rare-deal-on-nvidias-fastest-gaming-gpu",
    "domain": "AI 算力 / 半导体",
    "title": "Get this spiffy, stealthy MSI Gaming Trio RTX 5090 for just $4,299",
    "url": "https://www.tomshardware.com/pc-components/gpus/get-this-spiffy-stealthy-msi-rtx-5090-for-just-usd4-299-geforce-week-at-walmart-serves-up-a-rare-deal-on-nvidias-fastest-gaming-gpu",
    "source": "Jeffrey Kampman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T15:00:52+00:00",
    "summary": "Walmart has MSI's GeForce RTX 5090 Gaming Trio for just $4299 as part of its GeForce Week event, a rare deal on the most powerful graphics card around as the AI boom drives prices ever higher."
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/bambu-lab-r1-review",
    "domain": "AI 算力 / 半导体",
    "title": "Bambu Lab R1 Review: This one stands alone",
    "url": "https://www.tomshardware.com/maker-stem/bambu-lab-r1-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T14:00:00+00:00",
    "summary": "Bambu Lab leverages its mastery of motion systems and UI to create a nearly perfect stand-alone laser."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-keyboards/glorious-gmmk-eternal-review",
    "domain": "AI 算力 / 半导体",
    "title": "Glorious GMMK Eternal Review: Fits anywhere, sounds great",
    "url": "https://www.tomshardware.com/peripherals/gaming-keyboards/glorious-gmmk-eternal-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T13:00:00+00:00",
    "summary": "Glorious' new GMMK Eternal is a compact 96-percent wired keyboard with hot-swappable mechanical switches and three layers of sound-dampening in the case."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptomining/well-be-the-first-to-mine-bitcoin-in-space-says-nvidia-backed-startup-starcloud-will-fire-up-its-asics-after-its-second-spacecraft-reaches-orbit-later-this-year",
    "domain": "AI 算力 / 半导体",
    "title": "‘We’ll be the first to mine Bitcoin in space’ says Nvidia-backed startup",
    "url": "https://www.tomshardware.com/tech-industry/cryptomining/well-be-the-first-to-mine-bitcoin-in-space-says-nvidia-backed-startup-starcloud-will-fire-up-its-asics-after-its-second-spacecraft-reaches-orbit-later-this-year",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T12:59:50+00:00",
    "summary": "An Nvidia-backed startup plans to establish a Bitcoin mining operation in space before the year is out."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/us-and-china-propose-hotline-to-de-escalate-ai-threats-ahead-of-washington-summit-comms-channel-between-both-nations-to-be-left-open-in-case-of-national-security-threats-posed-by-autonomous-artificial-intelligence",
    "domain": "AI 算力 / 半导体",
    "title": "US and China propose hotline to de-escalate AI threats ahead of Washington summit",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/us-and-china-propose-hotline-to-de-escalate-ai-threats-ahead-of-washington-summit-comms-channel-between-both-nations-to-be-left-open-in-case-of-national-security-threats-posed-by-autonomous-artificial-intelligence",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T12:13:41+00:00",
    "summary": "The U.S. and China have proposed implementing AI red lines that will not be crossed, as well as a hotline between the two countries to provide rapid communication and opportunities for joint responses"
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/gaming-pc-with-rtx-5060-32gb-of-ram-and-1tb-of-storage-gets-usd500-discount-neweggs-capable-abs-cyclone-aqua-prebuilt-is-usd1-199-with-code",
    "domain": "AI 算力 / 半导体",
    "title": "Gaming PC with RTX 5060, 32GB of RAM, and 1TB of storage gets $500 discount",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/gaming-pc-with-rtx-5060-32gb-of-ram-and-1tb-of-storage-gets-usd500-discount-neweggs-capable-abs-cyclone-aqua-prebuilt-is-usd1-199-with-code",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T11:30:00+00:00",
    "summary": "Newegg's ABS Cyclone Aqua prebuilt combines Intel's 20-core Core i7-14700F with Nvidia's RTX 5060 8GB, and 32GB of DDR4 memory for less than the cost of building a comparable system"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/dram-is-now-more-expensive-than-compute-chips-on-per-area-basis-ai-demand-drives-memory-die-value-past-leading-edge-silicon",
    "domain": "AI 算力 / 半导体",
    "title": "Memory chips are now more expensive than compute chips on a per-area basis",
    "url": "https://www.tomshardware.com/pc-components/dram/dram-is-now-more-expensive-than-compute-chips-on-per-area-basis-ai-demand-drives-memory-die-value-past-leading-edge-silicon",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T11:12:35+00:00",
    "summary": "DRAM makers may potentially get more money for their wafers than TSMC gets for its N3 wafers."
  },
  {
    "id": "rss:https://www.tomshardware.com/raspberry-pi/raspberry-pi-locks-boards-to-factory-ram-capacities-in-firmware-engineer-tells-diy-modders-dont-waste-your-time-trying-repairs-or-upgrades-company-cites-shady-reseller-scams",
    "domain": "AI 算力 / 半导体",
    "title": "Raspberry Pi locks boards to factory RAM capacities in firmware",
    "url": "https://www.tomshardware.com/raspberry-pi/raspberry-pi-locks-boards-to-factory-ram-capacities-in-firmware-engineer-tells-diy-modders-dont-waste-your-time-trying-repairs-or-upgrades-company-cites-shady-reseller-scams",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T11:07:17+00:00",
    "summary": "Raspberry Pi users are being firmware blocked from swapping the RAM chips on their SBCs for repairs or upgrades."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/this-usd299-2tb-msi-ssd-is-one-of-the-least-expensive-pcie-4-0-ssds-you-can-buy-right-now-just-10-cents-per-gb-yields-a-speedy-upgrade-for-your-internal-storage",
    "domain": "AI 算力 / 半导体",
    "title": "This $299 2TB MSI SSD is one of the least expensive PCIe 4.0 SSDs you can buy right now",
    "url": "https://www.tomshardware.com/pc-components/this-usd299-2tb-msi-ssd-is-one-of-the-least-expensive-pcie-4-0-ssds-you-can-buy-right-now-just-10-cents-per-gb-yields-a-speedy-upgrade-for-your-internal-storage",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T10:48:20+00:00",
    "summary": "Get a solid deal on the 2TB MSI Spatium M461 SSD. Just $299 after promo code nets one of the least expensive Gen 4x4 SSDs available today."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/dapustor-splits-qlc-ssd-to-create-a-fast-pslc-region-in-dual-mode-drive-trades-6-percent-to-20-percent-of-its-qlc-capacity-for-more-than-7x-faster-random-writes",
    "domain": "AI 算力 / 半导体",
    "title": "New DapuStor SSD pairs high-capacity QLC with a permanent pSLC region",
    "url": "https://www.tomshardware.com/pc-components/ssds/dapustor-splits-qlc-ssd-to-create-a-fast-pslc-region-in-dual-mode-drive-trades-6-percent-to-20-percent-of-its-qlc-capacity-for-more-than-7x-faster-random-writes",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T10:30:00+00:00",
    "summary": "DapuStor’s dual-mode J5060 QLC SSD runs part of its NAND as pSLC, trading 4TB of a 30.72TB drive for 800GB of fast flash."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/chinas-cxmt-hits-12nm-class-dram-milestone-new-5th-gen-dram-tech-uses-quadruple-patterning-to-boost-die-capacity-by-50-percent",
    "domain": "AI 算力 / 半导体",
    "title": "China's CXMT hits 12nm-class DRAM milestone",
    "url": "https://www.tomshardware.com/pc-components/dram/chinas-cxmt-hits-12nm-class-dram-milestone-new-5th-gen-dram-tech-uses-quadruple-patterning-to-boost-die-capacity-by-50-percent",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T10:00:00+00:00",
    "summary": "China's DRAM champion CXMT has begun mass production using its 5th Geb DRAM process technology"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/openai-and-anthropic-are-reportedly-seeking-out-smaller-data-center-deals-to-meet-current-demand-20-30-mw-facilities-to-provide-capacity-as-mega-structures-undergo-construction",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI and Anthropic scramble for smaller data centers as massive gigawatt projects lag",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/openai-and-anthropic-are-reportedly-seeking-out-smaller-data-center-deals-to-meet-current-demand-20-30-mw-facilities-to-provide-capacity-as-mega-structures-undergo-construction",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T09:30:00+00:00",
    "summary": "OpenAI and Anthropic are seeking to secure immediate capacity, through smaller data center deals, to meet current demand, despite spending billions on massive deals elsewhere."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/iphone-18-pro-max-storage-can-drop-lower-than-a-hard-drive-at-1-1-mb-s-during-heavy-writes-qlc-nand-offers-higher-capacity-but-reportedly-suffers-38-percent-drop-compared-to-tlc-based-pro",
    "domain": "AI 算力 / 半导体",
    "title": "iPhone 18 Pro Max storage can drop lower than a hard drive at 1.1 MB/s during heavy writes",
    "url": "https://www.tomshardware.com/pc-components/ssds/iphone-18-pro-max-storage-can-drop-lower-than-a-hard-drive-at-1-1-mb-s-during-heavy-writes-qlc-nand-offers-higher-capacity-but-reportedly-suffers-38-percent-drop-compared-to-tlc-based-pro",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T17:34:47+00:00",
    "summary": "Apple's use of QLC NAND allows the iPhone 18 Pro Max to offer higher storage capacity, but Homolab's testing highlights the potential performance trade-off under sustained writes."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/gaming-pcs/get-the-worlds-fastest-gaming-cpu-and-a-dlss-5-capable-gpu-in-a-gaming-pc-for-usd2-299-fully-loaded-powerhouse-sports-ryzen-7-9800x3d-rtx-5080-founders-edition-32gb-ram-and-1tb-ssd",
    "domain": "AI 算力 / 半导体",
    "title": "Get the world’s fastest gaming CPU and a DLSS 5-capable GPU in a gaming PC for $2,299",
    "url": "https://www.tomshardware.com/desktops/gaming-pcs/get-the-worlds-fastest-gaming-cpu-and-a-dlss-5-capable-gpu-in-a-gaming-pc-for-usd2-299-fully-loaded-powerhouse-sports-ryzen-7-9800x3d-rtx-5080-founders-edition-32gb-ram-and-1tb-ssd",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T17:19:27+00:00",
    "summary": "Walmart is selling a CyberPowerPC gaming PC with a Ryzen 7 9800X3D, GeForce RTX 5080 Founders Edition, 32GB of DDR5-6000 memory, and a 1TB PCIe 4.0 SSD for $2,299."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/local-opposition-blocked-usd68-billion-worth-of-data-center-projects-in-the-second-quarter-of-2026-data-center-investments-reportedly-still-on-track-to-hit-usd32-trillion-by-2050",
    "domain": "AI 算力 / 半导体",
    "title": "Local opposition blocked $68 billion worth of data center projects in the second quarter of 2026",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/local-opposition-blocked-usd68-billion-worth-of-data-center-projects-in-the-second-quarter-of-2026-data-center-investments-reportedly-still-on-track-to-hit-usd32-trillion-by-2050",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T16:00:00+00:00",
    "summary": "Local opposition to data center buildouts has blocked $68 billion worth of data center projects in the second quarter of 2026, despite investments still rising."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/amd-beats-intel-to-the-trillion-dollar-club-as-stock-price-soars-firm-joins-nvidia-broadcom-and-sk-hynix-for-companies-worth-over-usd1-trillion",
    "domain": "AI 算力 / 半导体",
    "title": "AMD beats Intel to the trillion-dollar club as stock price soars",
    "url": "https://www.tomshardware.com/tech-industry/amd-beats-intel-to-the-trillion-dollar-club-as-stock-price-soars-firm-joins-nvidia-broadcom-and-sk-hynix-for-companies-worth-over-usd1-trillion",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T15:42:55+00:00",
    "summary": "AMD has crossed the $1 trillion market cap mark, joining an exclusive list of less than two dozen companies around the world."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/amd-ryzen-5-5500f-and-7500-show-up-at-retail-with-pricing-above-msrp-budget-cpus-are-usd20-more-expensive-than-list-price-even-from-first-party-sellers",
    "domain": "AI 算力 / 半导体",
    "title": "AMD Ryzen 5 5500F and 7500 show up at retail with pricing above MSRP",
    "url": "https://www.tomshardware.com/pc-components/cpus/amd-ryzen-5-5500f-and-7500-show-up-at-retail-with-pricing-above-msrp-budget-cpus-are-usd20-more-expensive-than-list-price-even-from-first-party-sellers",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T14:45:00+00:00",
    "summary": "Nearly two weeks after they were announced, AMD's Ryzen 5 5500F and 7500 (non-F) are available for sale, though prices are slightly above MSRP."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-shelves-global-ai-chip-rollout-as-chinas-own-demand-outstrips-supply-15-488-chip-atlas-clusters-leverage-optical-networking-to-counter-nvidia-scales-to-120-eflops",
    "domain": "AI 算力 / 半导体",
    "title": "Huawei shelves global AI chip rollout as China's own demand outstrips supply",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-shelves-global-ai-chip-rollout-as-chinas-own-demand-outstrips-supply-15-488-chip-atlas-clusters-leverage-optical-networking-to-counter-nvidia-scales-to-120-eflops",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T14:30:00+00:00",
    "summary": "Huawei says it will not offer its latest AI hardware outside of China citing lack of capacity to serve domestic demand."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/new-rtx-5070-autumn-limited-edition-gaming-gpu-doubles-as-an-air-freshener-with-built-in-e-sports-aromatherapy-ax-gamings-white-and-purple-card-also-features-an-anime-character-and-floral-graphics",
    "domain": "AI 算力 / 半导体",
    "title": "New RTX 5070 Autumn Limited Edition gaming GPU doubles as an air freshener with built-in 'e-sports aromatherapy'",
    "url": "https://www.tomshardware.com/pc-components/gpus/new-rtx-5070-autumn-limited-edition-gaming-gpu-doubles-as-an-air-freshener-with-built-in-e-sports-aromatherapy-ax-gamings-white-and-purple-card-also-features-an-anime-character-and-floral-graphics",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T14:00:00+00:00",
    "summary": "AX Gaming has revealed its latest seasonal anime-themed limited edition graphics card which, this time, is designed to please your nose as much as your eyes."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/snag-the-least-expensive-32gb-ddr5-6000-memory-kit-available-for-only-usd429-usd40-off-promo-code-for-v-color-manta-xsky-yields-the-least-expensive-ddr5-6000-cl30-kit-available-right-now",
    "domain": "AI 算力 / 半导体",
    "title": "Snag the least expensive 32GB DDR5-6000 memory kit available for only $429",
    "url": "https://www.tomshardware.com/pc-components/snag-the-least-expensive-32gb-ddr5-6000-memory-kit-available-for-only-usd429-usd40-off-promo-code-for-v-color-manta-xsky-yields-the-least-expensive-ddr5-6000-cl30-kit-available-right-now",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:30:00+00:00",
    "summary": "Buy 32GB of V-Color Manta XSky RAM for only $429. This capable, white DDR5-6000 CL30 kit is one of the best deals out for the speed and timings"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/president-trump-has-announced-plans-for-new-ai-force-and-ai-czar-amid-growing-ai-safety-concerns-new-unit-will-cherish-ai-and-not-stifle-it-trump-clarifies-while-dismissing-safety-warnings-as-hoaxes",
    "domain": "AI 算力 / 半导体",
    "title": "President Trump has announced plans for new 'AI Force' and 'AI Czar' amid growing AI safety concerns",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/president-trump-has-announced-plans-for-new-ai-force-and-ai-czar-amid-growing-ai-safety-concerns-new-unit-will-cherish-ai-and-not-stifle-it-trump-clarifies-while-dismissing-safety-warnings-as-hoaxes",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:15:00+00:00",
    "summary": "President Trump says he will create an AI Force and appoint a new AI czar while prioritizing rapid U.S. AI development and competition with China."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/typesafe-ais-jev-offers-an-alternative-to-llms-that-claims-to-be-193x-faster-and-445x-cheaper-system-one-type-model-is-bespoke-for-probabilistic-decision-making",
    "domain": "AI 算力 / 半导体",
    "title": "TypeSafe AI's Jev offers an alternative to LLMs that claims to be 193x faster and 445x cheaper",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/typesafe-ais-jev-offers-an-alternative-to-llms-that-claims-to-be-193x-faster-and-445x-cheaper-system-one-type-model-is-bespoke-for-probabilistic-decision-making",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:09:27+00:00",
    "summary": "Last week saw the debut of TypeSafe AI's Jev, its first \"System One\" model. Rather than chatting with users like conventional LLMs, it's strictly designed for statement evaluation and decision-making,"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/playstation-3-emulation-devs-work-around-an-nvidia-bug-for-up-to-37-percent-faster-performance-open-source-coders-reach-out-to-nvidia-to-over-uncovered-bug",
    "domain": "AI 算力 / 半导体",
    "title": "PlayStation 3 emulation devs work around an Nvidia bug for up to 37% faster performance",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/playstation-3-emulation-devs-work-around-an-nvidia-bug-for-up-to-37-percent-faster-performance-open-source-coders-reach-out-to-nvidia-to-over-uncovered-bug",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:00:00+00:00",
    "summary": "The developers of RPCS3 have found a workaround for an Nvidia driver bug and are touting up to 37% performance gains."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/apple-mac-studio-m5-ultra-review",
    "domain": "AI 算力 / 半导体",
    "title": "Apple Mac Studio (M5 Ultra) review: Local model citizen outpaces DGX Spark and Threadripper",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/apple-mac-studio-m5-ultra-review",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:00:00+00:00",
    "summary": "The Mac Studio with M5 Ultra delivers powerhouse productivity and AI performance in a small chassis."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/mediateks-next-gen-dimensity-cx-c10-max-will-power-new-googlebook-initiative-3nm-soc-has-similar-specs-to-kompanio-ultra-in-chromebook-plus-devices-despite-claims-of-elevating-computing-portfolio",
    "domain": "AI 算力 / 半导体",
    "title": "MediaTek next-gen Dimensity CX C10 Max will power new Googlebook initiative",
    "url": "https://www.tomshardware.com/pc-components/cpus/mediateks-next-gen-dimensity-cx-c10-max-will-power-new-googlebook-initiative-3nm-soc-has-similar-specs-to-kompanio-ultra-in-chromebook-plus-devices-despite-claims-of-elevating-computing-portfolio",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:00:00+00:00",
    "summary": "MediaTek's next-gen Dimensity CX C10 Max will arrive inside Googlebook devices, featuring similar specs as the Kompanio Ultra 910 currently available."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/hands-on-with-googlebooks-five-models-the-new-googlebook-os-and-a-mac-style-experience-for-android-users-at-premium-prices",
    "domain": "AI 算力 / 半导体",
    "title": "Hands-on with Googlebooks — Five models, the new Googlebook OS, and a Mac-style experience for Android users at premium prices",
    "url": "https://www.tomshardware.com/laptops/hands-on-with-googlebooks-five-models-the-new-googlebook-os-and-a-mac-style-experience-for-android-users-at-premium-prices",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:00:00+00:00",
    "summary": "Google has detailed its new Googlebooks, five laptops combining Android and ChromeOS to make a Mac-like experience for Android users, with a ton of Gemini tacked on."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/mini-pcs/apple-mac-mini-late-2026-review",
    "domain": "AI 算力 / 半导体",
    "title": "Apple Mac mini (Late 2026) Review: Strong performance, but losing its grip on value",
    "url": "https://www.tomshardware.com/desktops/mini-pcs/apple-mac-mini-late-2026-review",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T13:00:00+00:00",
    "summary": "The M6 Mac mini gets a considerable speed boost and a considerable price hike."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/china-crafts-working-3nm-gate-all-around-transistors-without-euv-stacked-nanosheets-target-3nm-without-euv-but-full-node-remains-distant",
    "domain": "AI 算力 / 半导体",
    "title": "China crafts working 3nm gate-all-around transistors without EUV",
    "url": "https://www.tomshardware.com/tech-industry/china-crafts-working-3nm-gate-all-around-transistors-without-euv-stacked-nanosheets-target-3nm-without-euv-but-full-node-remains-distant",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T12:30:00+00:00",
    "summary": "As China's IMECAS demonstrates its ability to build GAA transistors without using DUV tools allegedly for 3nm-class process technology, the country remains years away from any practical implementation"
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
    "points": 821,
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
    "id": "hn:49715947",
    "domain": "大厂 AI 动态",
    "title": "Gemini 3.8 Live and 3.8 Live Extended Thinking",
    "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/",
    "source": "leumon",
    "platform": "hackernews",
    "points": 491,
    "published_at": "2026-09-15T17:38:18+00:00",
    "summary": ""
  },
  {
    "id": "hn:49790409",
    "domain": "大厂 AI 动态",
    "title": "Turn off and restrict access to Apple Intelligence features on Mac",
    "url": "https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac",
    "source": "alwillis",
    "platform": "hackernews",
    "points": 344,
    "published_at": "2026-09-21T17:30:21+00:00",
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
    "id": "hn:49773998",
    "domain": "大厂 AI 动态",
    "title": "Microsoft agentically ports Copilot runtime to Rust for $120K",
    "url": "https://www.theregister.com/devops/2026/09/18/microsoft-agentically-ports-copilot-runtime-to-rust-for-120k/5297549",
    "source": "pjmlp",
    "platform": "hackernews",
    "points": 48,
    "published_at": "2026-09-20T09:08:52+00:00",
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
    "id": "hn:49743685",
    "domain": "大厂 AI 动态",
    "title": "Economic policy for AGI",
    "url": "https://institute.deepmind.com/essays/economic-policy-for-agi/",
    "source": "alphabetatango",
    "platform": "hackernews",
    "points": 66,
    "published_at": "2026-09-17T17:12:51+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/999167/openai-elite-mathematicians-panel",
    "domain": "大厂 AI 动态",
    "title": "OpenAI wants to consult elite mathematicians about how to not fumble again",
    "url": "https://www.theverge.com/ai-artificial-intelligence/999167/openai-elite-mathematicians-panel",
    "source": "Robert Hart",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T00:17:17+00:00",
    "summary": "After turning a string of spectacular mathematical results into a reputational crisis, OpenAI is consulting human mathematicians to help it figure out a less disastrous path forward. On Monday, the co"
  },
  {
    "id": "rss:https://www.theverge.com/entertainment/999056/paramount-warner-bros-discovery-merger-annual-film-quota-guardrails",
    "domain": "大厂 AI 动态",
    "title": "Paramount will need to release way more movies to make this merger work",
    "url": "https://www.theverge.com/entertainment/999056/paramount-warner-bros-discovery-merger-annual-film-quota-guardrails",
    "source": "Charles Pulliam-Moore",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T22:26:07+00:00",
    "summary": "Now that Paramount has reached a settlement with the 12 states that were suing to block its $110 billion merger with Warner Bros. Discovery (WBD), the studio is even closer to becoming one of the worl"
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/999094/rabbit-ai-agent-os3",
    "domain": "大厂 AI 动态",
    "title": "Rabbit’s new AI agent doesn’t need an R1 to run",
    "url": "https://www.theverge.com/ai-artificial-intelligence/999094/rabbit-ai-agent-os3",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T20:52:40+00:00",
    "summary": "Rabbit, the company behind the underwhelming R1 device, is rolling out a standalone AI agent that you don't need its hardware to use, as reported earlier by Wired. The startup says its new OS3 \"agenti"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/998791/ceer-ev-saudi-arabia-foxconn-exobot",
    "domain": "大厂 AI 动态",
    "title": "Saudi Arabia’s new Exobot EVs make the Cybertruck look normal",
    "url": "https://www.theverge.com/transportation/998791/ceer-ev-saudi-arabia-foxconn-exobot",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T20:14:54+00:00",
    "summary": "The Kingdom of Saudi Arabia is mostly known for its global dominance over petroleum production and oil reserves - not necessarily cars and auto manufacturing, and certainly not electric vehicle produc"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/998842/qualcomm-snapdragon-8-elite-extreme-gen-6",
    "domain": "大厂 AI 动态",
    "title": "Qualcomm’s Snapdragon 8 Elite Gen 6 comes in an Extreme version too",
    "url": "https://www.theverge.com/gadgets/998842/qualcomm-snapdragon-8-elite-extreme-gen-6",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T20:00:00+00:00",
    "summary": "Qualcomm has announced the Snapdragon 8 Elite Gen 6, this year joined by the 8 Elite Extreme Gen 6 too. The company describes both new phone chips as flagships, and the spec differences are relatively"
  },
  {
    "id": "rss:https://www.theverge.com/tech/998844/motorola-signature-27-specs-snapdragon-8-elite-extreme-gen-6",
    "domain": "大厂 AI 动态",
    "title": "Motorola’s wild-looking Signature 27 runs Qualcomm’s new Extreme chipset",
    "url": "https://www.theverge.com/tech/998844/motorola-signature-27-specs-snapdragon-8-elite-extreme-gen-6",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T20:00:00+00:00",
    "summary": "Motorola is the first company to announce a phone running Qualcomm's top-end Snapdragon 8 Elite Extreme Gen 6 chip. The Signature 27 looks set to be Motorola's most advanced flagship in some years, th"
  },
  {
    "id": "rss:https://www.theverge.com/tech/998874/apple-iphone-18-pro-ios-27-camera-texture-grain-photographic-style",
    "domain": "大厂 AI 动态",
    "title": "Apple clarifies that Texture and Grain controls are exclusive to the latest iPhones’ cameras",
    "url": "https://www.theverge.com/tech/998874/apple-iphone-18-pro-ios-27-camera-texture-grain-photographic-style",
    "source": "Andrew Liszewski",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T19:48:08+00:00",
    "summary": "Apple's new texture and grain controls for stylizing photos will be more limited on older phones than initially expected. A confusingly worded press release from Apple indicated that the new features,"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/998932/googlebook-preorder-pixel-buds-2a-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Score free Pixel Buds 2A when you preorder a Googlebook at Best Buy",
    "url": "https://www.theverge.com/gadgets/998932/googlebook-preorder-pixel-buds-2a-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T19:28:55+00:00",
    "summary": "The Android-powered Googlebooks are coming soon, with familiar brands and specs that rival Windows Copilot machines. For anyone eager to get their hands on any the new laptops, there’s a preorder perk"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/998824/apple-magic-keyboard-touch-interstellar-4k-blu-ray-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Save $30 on Apple’s Magic Keyboard with Touch ID and a numpad",
    "url": "https://www.theverge.com/gadgets/998824/apple-magic-keyboard-touch-interstellar-4k-blu-ray-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T18:10:57+00:00",
    "summary": "Until the end of the day on September 22nd, 2026, Best Buy and Amazon have the black Apple Magic Keyboard on sale for $169.99, a $30 discount from the usual price. This is the souped-up version of App"
  },
  {
    "id": "rss:https://www.theverge.com/tech/998914/trump-truth-social-api-lawsuit-san-francisco",
    "domain": "大厂 AI 动态",
    "title": "San Francisco sues Trump Media for selling early access to Trump posts",
    "url": "https://www.theverge.com/tech/998914/trump-truth-social-api-lawsuit-san-francisco",
    "source": "Gaby Del Valle",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T17:43:50+00:00",
    "summary": "San Francisco is suing the Trump Media &#38; Technology Group, the parent company behind Truth Social, for selling early access to President Donald Trump's posts on the social media site. The lawsuit,"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/were-already-fighting-yesterdays-battle-greeces-prime-minister-gets-candid-about-ai/",
    "domain": "大厂 AI 动态",
    "title": "‘We’re already fighting yesterday’s battle’: Greece’s prime minister gets candid about AI",
    "url": "https://techcrunch.com/2026/09/22/were-already-fighting-yesterdays-battle-greeces-prime-minister-gets-candid-about-ai/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:59:08+00:00",
    "summary": "Most leaders on a trade mission stick to the pitch, but when I interviewed Greek Prime Minister Kyriakos Mitsotakis this week, he also admitted that no government is ready for what AI is about to do."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/discords-age-verification-era-is-upon-us-despite-community-backlash/",
    "domain": "大厂 AI 动态",
    "title": "Discord’s age verification era is upon us, despite community backlash",
    "url": "https://techcrunch.com/2026/09/22/discords-age-verification-era-is-upon-us-despite-community-backlash/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T03:31:12+00:00",
    "summary": "According to Discord, 90% of users will not have to verify their age."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/techcrunch-founder-summits-agenda-revealed-unlock-fundraising-hiring-and-ai-insights-in-boston-on-november-4/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Founder Summit’s agenda revealed: Unlock fundraising, hiring, and AI insights in Boston on November 4",
    "url": "https://techcrunch.com/2026/09/22/techcrunch-founder-summits-agenda-revealed-unlock-fundraising-hiring-and-ai-insights-in-boston-on-november-4/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T23:21:49+00:00",
    "summary": "Founders shouldn't have to learn the hardest lessons the hardest way. TechCrunch Founder Summit is designed to make the challenges of starting a company easier and the highs that much greater."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/snorkel-ai-triples-valuation-to-3-5b-as-demand-for-ai-training-data-booms/",
    "domain": "大厂 AI 动态",
    "title": "Snorkel AI triples valuation to $3.5B as demand for AI training data booms",
    "url": "https://techcrunch.com/2026/09/22/snorkel-ai-triples-valuation-to-3-5b-as-demand-for-ai-training-data-booms/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T21:56:43+00:00",
    "summary": "The seven-year-old startup has raised a $350 million Series E to fuel its data-as-a-service approach."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/qualcomm-launches-two-new-smartphone-chips-with-emphasis-on-ai/",
    "domain": "大厂 AI 动态",
    "title": "Qualcomm launches two new smartphone chips with emphasis on AI",
    "url": "https://techcrunch.com/2026/09/22/qualcomm-launches-two-new-smartphone-chips-with-emphasis-on-ai/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T20:00:00+00:00",
    "summary": "Qualcomm said that its new top chip can run 30B mixture-of-expert model locally."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/apple-could-take-on-whoop-with-a-new-fitness-tracker-report-says/",
    "domain": "大厂 AI 动态",
    "title": "Apple could take on Whoop with a new fitness tracker, report says",
    "url": "https://techcrunch.com/2026/09/22/apple-could-take-on-whoop-with-a-new-fitness-tracker-report-says/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T19:27:57+00:00",
    "summary": "Apple may be developing a new fitness tracker as part of its new generation of hardware devices."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/meta-admits-muses-likeness-to-openclaw-isnt-a-coincidence/",
    "domain": "大厂 AI 动态",
    "title": "Meta admits Muse’s likeness to OpenClaw isn’t a coincidence",
    "url": "https://techcrunch.com/2026/09/22/meta-admits-muses-likeness-to-openclaw-isnt-a-coincidence/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T19:09:11+00:00",
    "summary": "Meta says Muse was built from scratch, but acknowledges the AI assistant was \"heavily inspired\" by OpenClaw — down to some of its workspace filenames and content."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/hacking-group-shinyhunters-claims-it-breached-the-fbi-stole-agents-and-applicants-data/",
    "domain": "大厂 AI 动态",
    "title": "Hacking group ShinyHunters claims it breached the FBI, stole agents’ and applicants’ data",
    "url": "https://techcrunch.com/2026/09/22/hacking-group-shinyhunters-claims-it-breached-the-fbi-stole-agents-and-applicants-data/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T18:40:30+00:00",
    "summary": "The theft of agents' personal information could present a major counterintelligence threat, where agents and their families are extorted into cooperating with a foreign government."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/a16z-is-challenging-silicon-valleys-love-for-drop-outs-by-launching-a-school/",
    "domain": "大厂 AI 动态",
    "title": "a16z is challenging Silicon Valley’s love for drop-outs by launching a school",
    "url": "https://techcrunch.com/2026/09/22/a16z-is-challenging-silicon-valleys-love-for-drop-outs-by-launching-a-school/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T18:24:34+00:00",
    "summary": "This academy for promising high school grads is somewhere between a trade school, Y Combinator, and Peter Thiel's Fellowship Program."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI launches GPT-6 Sol and Luna, boasting lower cost and fewer mistakes",
    "url": "https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T18:00:00+00:00",
    "summary": "OpenAI is launching two new models, which it says are cut from the same cloth as Astra."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/waymos-latest-expansion-strategy-teenagers/",
    "domain": "大厂 AI 动态",
    "title": "Waymo’s latest expansion strategy: teenagers",
    "url": "https://techcrunch.com/2026/09/22/waymos-latest-expansion-strategy-teenagers/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T17:36:06+00:00",
    "summary": "Waymo is opening its robotaxi service to teenagers aged 13 to 17 in Nashville, its second city to offer rides to minors."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/anthropic-releases-opus-5-5-with-lower-prices-and-fable-level-performance/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic releases Opus 5.5 with lower prices and Fable-level performance",
    "url": "https://techcrunch.com/2026/09/22/anthropic-releases-opus-5-5-with-lower-prices-and-fable-level-performance/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T16:30:07+00:00",
    "summary": "Anthropic called it \"the strongest-performing model we've tested to date.\""
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/stolen-passwords-are-exposing-americas-water-providers-to-hackers/",
    "domain": "大厂 AI 动态",
    "title": "Stolen passwords are exposing America’s water providers to hackers",
    "url": "https://techcrunch.com/2026/09/22/stolen-passwords-are-exposing-americas-water-providers-to-hackers/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T15:50:58+00:00",
    "summary": "Researchers say another looming threat hangs over some of America's most important critical infrastructure."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/noble-carbon-will-show-how-its-making-ev-charger-installs-painless-at-techcrunch-disrupt/",
    "domain": "大厂 AI 动态",
    "title": "Noble Carbon will show how it’s making EV charger installs painless at TechCrunch Disrupt",
    "url": "https://techcrunch.com/2026/09/22/noble-carbon-will-show-how-its-making-ev-charger-installs-painless-at-techcrunch-disrupt/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T15:00:00+00:00",
    "summary": "Noble Carbon has developed a smart circuit breaker that allows households to electrify without the pain of a main panel upgrade."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/five-ai-safety-sessions-every-founder-should-have-on-their-techcrunch-disrupt-2026-agenda/",
    "domain": "大厂 AI 动态",
    "title": "Five AI safety sessions every founder should have on their TechCrunch Disrupt 2026 agenda",
    "url": "https://techcrunch.com/2026/09/22/five-ai-safety-sessions-every-founder-should-have-on-their-techcrunch-disrupt-2026-agenda/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T15:00:00+00:00",
    "summary": "At TechCrunch Disrupt 2026, five sessions across the AI Stage and Real World AI Stage cover AI safety, featuring leaders from Anthropic, Nvidia, AWS, Waabi, and more. Register before September 25 to s"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/astroforge-is-putting-ai-in-command-of-its-next-spacecraft/",
    "domain": "大厂 AI 动态",
    "title": "AstroForge is putting AI in command of its next spacecraft",
    "url": "https://techcrunch.com/2026/09/22/astroforge-is-putting-ai-in-command-of-its-next-spacecraft/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T15:00:00+00:00",
    "summary": "Autonomy-1 will have a small, transformer-based AI model taking charge of a space probe."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/techcrunch-disrupt-2026-aaron-edsinger-brings-hello-robots-stretch-4-to-life-onstage/",
    "domain": "大厂 AI 动态",
    "title": "TechCrunch Disrupt 2026: Aaron Edsinger brings Hello Robot’s Stretch 4 to life onstage",
    "url": "https://techcrunch.com/2026/09/22/techcrunch-disrupt-2026-aaron-edsinger-brings-hello-robots-stretch-4-to-life-onstage/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T14:30:00+00:00",
    "summary": "Hello Robot CEO and co-founder Aaron Edsinger will bring Stretch 4 for a live demo on the Real World AI Stage at TechCrunch Disrupt 2026. Register before September 25 to save up to $200, plus get a se"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/exhibitor-program-reopened-book-by-sept-30/",
    "domain": "大厂 AI 动态",
    "title": "Exhibit tables added: One last chance to showcase your startup at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/22/exhibitor-program-reopened-book-by-sept-30/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T14:15:00+00:00",
    "summary": "We have reopened our exhibitor program for 1 more week. Book your exhibit table by September 30 at 11:59 p.m. PT and showcase your startup in front of 10,000+ founders, investors, and tech leaders at "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/tiktoks-us-arm-joins-lantern-a-cross-platform-child-safety-initiative/",
    "domain": "大厂 AI 动态",
    "title": "TikTok’s US arm joins Lantern, a cross-platform child safety initiative",
    "url": "https://techcrunch.com/2026/09/22/tiktoks-us-arm-joins-lantern-a-cross-platform-child-safety-initiative/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T14:00:00+00:00",
    "summary": "Eight months after establishing a U.S.-based joint venture, TikTok is getting on board fellow platforms to support industrywide child safety work."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/22/4-days-to-save-up-to-200-reason-2-of-5-to-be-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "4 days to save up to $200: Reason 2 of 5 to be at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/09/22/4-days-to-save-up-to-200-reason-2-of-5-to-be-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T14:00:00+00:00",
    "summary": "Save up to $200 on your TechCrunch Disrupt 2026 pass, plus 50% off a second pass before prices increase on September 25 at 11:59 p.m. PT. Register today."
  },
  {
    "id": "rss:https://stratechery.com/2026/amazon-blocks-muse-amazons-moat-aggregator-v-aggregator/",
    "domain": "大厂 AI 动态",
    "title": "Amazon Blocks Muse, Amazon’s Moat, Aggregator v Aggregator",
    "url": "https://stratechery.com/2026/amazon-blocks-muse-amazons-moat-aggregator-v-aggregator/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T10:00:00+00:00",
    "summary": "Amazon predictably blocked Muse, but there is room for a deal based on the reality that Amazon's physical world investments are an AI moat."
  },
  {
    "id": "rss:https://stratechery.com/2026/frontier-overhangs/",
    "domain": "大厂 AI 动态",
    "title": "Frontier Overhangs",
    "url": "https://stratechery.com/2026/frontier-overhangs/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-21T10:00:00+00:00",
    "summary": "Pacing the frontier may be sincere, but it would also be strategically useful for the frontier labs to have time to reduce overhangs caused by model advancement."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/womans-brain-worm-infection-confirmed-after-eggs-grow-tails-in-lab-test/",
    "domain": "大厂 AI 动态",
    "title": "Woman's brain worm infection confirmed after eggs grow tails in lab test",
    "url": "https://arstechnica.com/health/2026/09/womans-brain-worm-infection-confirmed-after-eggs-grow-tails-in-lab-test/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T21:42:14+00:00",
    "summary": "There is no single definitive test for these worms, but the tail is fairly convincing."
  },
  {
    "id": "rss:https://arstechnica.com/ai/2026/09/new-anthropic-openai-models-make-same-promise-a-little-more-for-a-lot-less-money/",
    "domain": "大厂 AI 动态",
    "title": "New Anthropic, OpenAI models make same promise: A little more for a lot less money",
    "url": "https://arstechnica.com/ai/2026/09/new-anthropic-openai-models-make-same-promise-a-little-more-for-a-lot-less-money/",
    "source": "Samuel Axon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T21:25:18+00:00",
    "summary": "The frontier AI model race has entered its comparison shopping phase."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/cities-across-us-oppose-trump-fcc-plan-to-preempt-local-broadband-rules/",
    "domain": "大厂 AI 动态",
    "title": "Cities across US oppose Trump FCC plan to preempt local broadband rules",
    "url": "https://arstechnica.com/tech-policy/2026/09/cities-across-us-oppose-trump-fcc-plan-to-preempt-local-broadband-rules/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-22T20:38:30+00:00",
    "summary": "Cities defend permit requirements, say ISPs aren't building networks fast enough."
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
    "points": 71,
    "published_at": "2026-09-21T19:14:30+00:00",
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
    "id": "hn:49810905",
    "domain": "股票",
    "title": "In 2025, 49 percent of adults under age 30 lived with a parent [pdf]",
    "url": "https://www.federalreserve.gov/publications/files/2025-report-economic-well-being-us-households-202605.pdf",
    "source": "gscott",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-09-23T02:26:49+00:00",
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
    "id": "hn:49778029",
    "domain": "金融",
    "title": "Samsung is expected to more than double output of its HBM4 and HBM4E DRAM",
    "url": "https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say",
    "source": "giuliomagnifico",
    "platform": "hackernews",
    "points": 557,
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
    "id": "rss:https://arxiv.org/abs/2609.25965",
    "domain": "金融",
    "title": "Modeling interest rate swap volatility with GARCH processes",
    "url": "https://arxiv.org/abs/2609.25965",
    "source": "Micha{\\l} Balcerek, Micha{\\l} Wronka",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2609.25965v1 Announce Type: new Abstract: We examine the conditional volatility dynamics of the USD 1Yx10Y forward swap rate using GARCH(1,1), GJR-GARCH(1,1), and a two-regime Markov-switching G"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.26062",
    "domain": "金融",
    "title": "The Elasticity of Substitution between Native and Immigrant Labor: A Meta-Analysis",
    "url": "https://arxiv.org/abs/2609.26062",
    "source": "Klara Kantova, Tomas Havranek, Zuzana Irsova, Jiri Schwarz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2609.26062v1 Announce Type: new Abstract: This paper presents the first comprehensive meta-analysis of the elasticity of substitution between native and immigrant labor, drawing on 1,091 estimat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.26212",
    "domain": "金融",
    "title": "Trust, Rule of Law, and the Size Premium: Evidence from a Meta-Analysis",
    "url": "https://arxiv.org/abs/2609.26212",
    "source": "Jiri Schwarz, Tomas Havranek, Zuzana Irsova, Jiri Novak",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2609.26212v1 Announce Type: new Abstract: Reported estimates of the size premium, the tendency of smaller firms to earn higher average returns than larger firms, vary widely across studies, coun"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.26349",
    "domain": "金融",
    "title": "Optimal Investment and Consumption in Financial Markets with Integrated Variance Clocks",
    "url": "https://arxiv.org/abs/2609.26349",
    "source": "Eduardo Abi Jaber, Florian Gutekunst, Martin Herdegen, David Hobson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2609.26349v1 Announce Type: new Abstract: We study the infinite-horizon optimal investment and consumption problem in a general class of continuous financial markets, where uncertainty is driven"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.26604",
    "domain": "金融",
    "title": "The network advantage: benefits of interregional scientific knowledge spillovers on AI patenting",
    "url": "https://arxiv.org/abs/2609.26604",
    "source": "Saverio Barabuffi, Jacopo Cricchio, Alberto Di Minin, Guido Pialli",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2609.26604v1 Announce Type: new Abstract: Knowledge spillovers have largely been studied as unintended externalities diffusing through geographic proximity, while deliberate interregional networ"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.26606",
    "domain": "金融",
    "title": "Liquidity Provision and Rebate Design in Option Markets",
    "url": "https://arxiv.org/abs/2609.26606",
    "source": "Samuel N. Cohen, Lyndon Drake, Zihan Guo, Christoph Reisinger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2609.26606v1 Announce Type: new Abstract: We provide a model for the nested optimisation problem of market making and rebate design problems in option markets and find optimal strategies. A sing"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.25144",
    "domain": "金融",
    "title": "The Informational Content in Lepto-Variance and Its Relation to Higher Moments",
    "url": "https://arxiv.org/abs/2609.25144",
    "source": "Vassilis Polimenis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2609.25144v1 Announce Type: cross Abstract: Lepto-regression is defined as the machine learning process of constructing a Regression Tree of a target feature on itself. It is a novel, model-free"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.25452",
    "domain": "金融",
    "title": "Risk diversification for infinitely divisible distributions",
    "url": "https://arxiv.org/abs/2609.25452",
    "source": "Peng Liu, Tiantian Mao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2609.25452v1 Announce Type: cross Abstract: In this paper, we study the diversification properties of convex combinations of iid random variables with infinitely divisible distributions. We char"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.25617",
    "domain": "金融",
    "title": "Hierarchical Multi-Task Learning with Liquidity-Aware Signals for Stock Forecasting",
    "url": "https://arxiv.org/abs/2609.25617",
    "source": "Hengyi Yang, Sida Lin, Yiyan Qi, Yankai Chen, Haohan Zhang, Xianhua Peng, Jian Guo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2609.25617v1 Announce Type: cross Abstract: Stock price forecasting is a long-standing challenge in computational finance, driven by the inherent randomness of markets and complex temporal patte"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.25677",
    "domain": "金融",
    "title": "Seeing Is Not Perceiving: When Synthetic Consumers Can and Cannot Pretest Visual Marketing",
    "url": "https://arxiv.org/abs/2609.25677",
    "source": "Yi-Lin Tsai (Arvin), Yung-Hsiu (Arvin), Lai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2609.25677v1 Announce Type: cross Abstract: Marketers now deploy generative AI agents as synthetic consumers to pretest visual assets such as logos, packaging, and advertising at a fraction of h"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.26242",
    "domain": "金融",
    "title": "Can You Delete a Year of Market Data? Machine Unlearning Against Exact Retraining Oracles",
    "url": "https://arxiv.org/abs/2609.26242",
    "source": "Junyi Ye",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2609.26242v1 Announce Type: cross Abstract: When a data license expires, deleting stored records does not remove influence encoded in a trained forecaster. Machine unlearning seeks to remove thi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.26303",
    "domain": "金融",
    "title": "Target alignment, dilution and forecast selection when cross-sectional forecasts share a common target",
    "url": "https://arxiv.org/abs/2609.26303",
    "source": "Masoud Soleimani",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2609.26303v1 Announce Type: cross Abstract: Forecasters often score the same units per date against one standardized realized outcome. We show that every standardized forecast splits exactly int"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.26445",
    "domain": "金融",
    "title": "A Practical Guide on Graphical Model Validation",
    "url": "https://arxiv.org/abs/2609.26445",
    "source": "Mario V. W\\\"uthrich",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2609.26445v1 Announce Type: cross Abstract: This manuscript formalizes the most popular model validation tools used in general insurance actuarial modeling. These include graphical tools like ca"
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.06906",
    "domain": "金融",
    "title": "First order Martingale model risk and semi-static hedging",
    "url": "https://arxiv.org/abs/2410.06906",
    "source": "Nathan Sauldubois, Nizar Touzi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2410.06906v3 Announce Type: replace Abstract: We investigate model risk distributionally robust sensitivities for functionals on the Wasserstein space when the underlying model is constrained to"
  },
  {
    "id": "rss:https://arxiv.org/abs/2508.04003",
    "domain": "金融",
    "title": "The Marginal Effects of Ethereum Network MEV Transaction Re-Ordering",
    "url": "https://arxiv.org/abs/2508.04003",
    "source": "Bruce Mizrach, Nathaniel Yoshida",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2508.04003v3 Announce Type: replace Abstract: Two MEV builders now produce nearly 80\\% of Ethereum blocks. Block builders have the ability to reorder transactions on the blockchain in a way that"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.13334",
    "domain": "金融",
    "title": "Computable Countermarkets and the Limits of Universal Trading",
    "url": "https://arxiv.org/abs/2604.13334",
    "source": "Karl Svozil",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2604.13334v3 Announce Type: replace Abstract: We explain why no trading algorithm can guarantee profit in every market. For each deterministic program that always returns a finite-precision posi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.17166",
    "domain": "金融",
    "title": "The Virtue of Sparsity in Complexity",
    "url": "https://arxiv.org/abs/2604.17166",
    "source": "Nima Afsharhajari, Jonathan Yu-Meng Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2604.17166v2 Announce Type: replace Abstract: Sparsity or complexity? In modern high-dimensional asset pricing, these are often viewed as competing principles: recent empirical evidence favors r"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.08812",
    "domain": "金融",
    "title": "Little Impact of ChatGPT on High School Test Scores",
    "url": "https://arxiv.org/abs/2605.08812",
    "source": "Nick Huntington-Klein",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2605.08812v3 Announce Type: replace Abstract: In educational settings, AI can be used as a learning aid, but can also be used to avoid schoolwork, passing classes while learning little. Most exi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.15614",
    "domain": "金融",
    "title": "When Do Type-Specific Wages Buffer Distributional Incidence in TANK?",
    "url": "https://arxiv.org/abs/2605.15614",
    "source": "Kenji Miyazaki",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2605.15614v3 Announce Type: replace Abstract: When do relative wages buffer the unequal incidence of aggregate shocks? I derive a consumption-gap decomposition and a present-value condition for "
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.28853",
    "domain": "金融",
    "title": "Financially Guided Deep Portfolio Optimization",
    "url": "https://arxiv.org/abs/2605.28853",
    "source": "Rahul Fernandes, Travis Desell",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2605.28853v2 Announce Type: replace Abstract: Portfolio optimization in real-world financial markets is notoriously difficult due to non-stationarity, noisy data, and high transaction costs. Sta"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.28230",
    "domain": "金融",
    "title": "Boundary-Induced Apparent Risk Aversion in Nonergodic Multiplicative Growth",
    "url": "https://arxiv.org/abs/2607.28230",
    "source": "Ling Zhang, Boyan Xing, Zhenyu She, Zixiang Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2607.28230v3 Announce Type: replace Abstract: Finite multiplicative systems often cease to evolve when a lower continuation threshold is reached, whereas standard growth-optimal benchmarks assum"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00858",
    "domain": "金融",
    "title": "Data-Driven Measures of High-Frequency Trading",
    "url": "https://arxiv.org/abs/2608.00858",
    "source": "Gbenga Ibikunle, Ben Moews, Dmitriy Muravyev, Khaladdin Rzayev",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2608.00858v3 Announce Type: replace Abstract: Public data do not identify high-frequency trading (HFT), and standard proxies do not separate liquidity-supplying from liquidity-demanding strategi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2404.15391",
    "domain": "金融",
    "title": "Data-Driven Mechanism Design via Multi-Agent Revealed Preferences",
    "url": "https://arxiv.org/abs/2404.15391",
    "source": "Luke Snow, Vikram Krishnamurthy",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2404.15391v4 Announce Type: replace-cross Abstract: We study a sequence of independent one-shot non-cooperative games where agents play equilibria determined by a tunable mechanism. Observing on"
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.14788",
    "domain": "金融",
    "title": "Polynomial Scaling is Possible For Neural Operator Approximations of Structured Families of BSDEs",
    "url": "https://arxiv.org/abs/2410.14788",
    "source": "Takashi Furuya, Anastasis Kratsios",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2410.14788v4 Announce Type: replace-cross Abstract: Neural operator (NO) architectures learn nonlinear maps between infinite-dimensional function spaces and are widely used to accelerate simulat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.25338",
    "domain": "金融",
    "title": "Optimal threshold resetting in collective diffusive search",
    "url": "https://arxiv.org/abs/2603.25338",
    "source": "Arup Biswas, Satya N Majumdar, Arnab Pal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2603.25338v3 Announce Type: replace-cross Abstract: Stochastic resetting has attracted significant attention in recent years due to its wide-ranging applications across physics, biology, and sea"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.08285",
    "domain": "金融",
    "title": "Beyond Agent Architecture: Execution Assumptions and Reproducibility in LLM-Based Trading Systems",
    "url": "https://arxiv.org/abs/2606.08285",
    "source": "Junyi Yao, Zihao Zheng, Baichuan Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2606.08285v2 Announce Type: replace-cross Abstract: Large language models (LLMs) and agentic systems are increasingly proposed for financial trading, yet their reported performance remains diffi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.22006",
    "domain": "金融",
    "title": "Printed but not benchmarkable: most building-decarbonisation disclosure cannot be matched to the pathways that stranding regulation assumes",
    "url": "https://arxiv.org/abs/2607.22006",
    "source": "Jingyi Xu, Minghui Cheng, Anchen Sun",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-23T04:00:00+00:00",
    "summary": "arXiv:2607.22006v2 Announce Type: replace-cross Abstract: Cities are beginning to enforce carbon limits on existing buildings. Science-based decarbonisation pathways set those limits one asset type an"
  },
  {
    "id": "hn:49626052",
    "domain": "金融",
    "title": "One woman's Tesla was remotely controlled by an abusive ex-partner",
    "url": "https://www.theguardian.com/australia-news/2026/sep/09/how-one-womans-tesla-was-remotely-controlled-and-harass-by-her-abusive-ex-partner-ntwnfb",
    "source": "gradschool",
    "platform": "hackernews",
    "points": 75,
    "published_at": "2026-09-09T13:16:45+00:00",
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
    "id": "hn:49730841",
    "domain": "金融",
    "title": "Fed approves interest rate hike, signals one more to come this year",
    "url": "https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html",
    "source": "rawgabbit",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-09-16T18:14:36+00:00",
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
    "id": "hn:49667360",
    "domain": "金融",
    "title": "A Decade of Hype, 3k Roofs, and One Redirect URL: Tesla Kills the Solar Roof",
    "url": "https://www.gadgetreview.com/a-decade-of-hype-3000-roofs-and-one-redirect-url-tesla-kills-the-solar-roof",
    "source": "upofadown",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-09-12T00:38:23+00:00",
    "summary": ""
  }
]
```
