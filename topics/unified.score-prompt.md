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

- 今日日期：`2026-09-01`
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
  "date": "2026-09-01",
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
    "points": 4402818,
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
    "points": 1785410,
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
    "points": 1562149,
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
    "points": 1346756,
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
    "points": 1293961,
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
    "points": 1221520,
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
    "points": 1136432,
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
    "points": 1078797,
    "published_at": "2026-08-14T12:00:00+00:00",
    "summary": "AI 办公到底能干些啥？它真的能颠覆我们的工作方式，以至于让大厂押上身家也要卷吗？"
  },
  {
    "id": "bvid:BV1aeLqzUE6L",
    "domain": "AI",
    "title": "10分钟讲清楚 Prompt, Agent, MCP 是什么",
    "url": "http://www.bilibili.com/video/av114410228025650",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 880237,
    "published_at": "2025-05-01T09:00:00+00:00",
    "summary": "up的科学星球：https://t.zsxq.com/ubYr8"
  },
  {
    "id": "bvid:BV1ZzvUBXEoL",
    "domain": "AI",
    "title": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！",
    "url": "http://www.bilibili.com/video/av115818910194374",
    "source": "极客教学",
    "platform": "bilibili",
    "points": 864957,
    "published_at": "2026-01-01T08:40:14+00:00",
    "summary": "【2026最新版】保姆级AI Agent智能体系统教程，手把手带你从0基础开始搭建企业级AI Agent智能体！全程干货无废话！让你少走99%的弯路！"
  },
  {
    "id": "bvid:BV1RFTc62EaK",
    "domain": "AI",
    "title": "黑马Vibe Coding零基础入门，vibecoding项目，涵盖Claude Code、Cursor、Codex、SDD、LangChain、Agent开发",
    "url": "http://www.bilibili.com/video/av116838327388595",
    "source": "黑马程序员",
    "platform": "bilibili",
    "points": 676483,
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
    "points": 672601,
    "published_at": "2025-05-01T04:00:00+00:00",
    "summary": "相信你已经在网上刷到过不少的 AI 工具，但如果你让我推荐最值得我们每个人学习的一款 AI 工具，那绝对就是史上最强的 AI 编程工具 —— Cursor。为此，我们录制了一个保姆级的 Cursor 新手教程，在这里免费分享给大家。即使你是一个对 AI 完全 0 基础的新手小白，看完这个视频后，你也可以彻底了解 Cursor 这个软件，并知道如何从 0 到 1 用 Cursor 做出入门级的 AI"
  },
  {
    "id": "bvid:BV1xwVr6FEh4",
    "domain": "AI",
    "title": "【全748集】目前B站最全最细的AI Agent开发零基础教程，2026最新版，包含所有干货！七天就能从小白到大神！少走99%的弯路！学完即就业，带你玩转AI！",
    "url": "http://www.bilibili.com/video/av116680671890321",
    "source": "AI大模型码农",
    "platform": "bilibili",
    "points": 661883,
    "published_at": "2026-06-02T14:20:53+00:00",
    "summary": "视频配套仔料+大模型入门到进阶全套仔料\n已经整理打包好\n如果视频对你有用的话请一键三连【长按点赞】支持一下up哦"
  },
  {
    "id": "bvid:BV1cq5q6CEu3",
    "domain": "AI",
    "title": "从夯到拉，锐评 32 个 AI 编程工具！",
    "url": "http://www.bilibili.com/video/av116578532200786",
    "source": "程序员鱼皮",
    "platform": "bilibili",
    "points": 652949,
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
    "points": 586492,
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
    "points": 441144,
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
    "points": 404606,
    "published_at": "2025-04-23T02:00:20+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】对于程序员，MCP必知必学，Java+SpringAI / LangChain / LangChain4J+MCP，一旦掌握AI智能落地项目，会大大增加在就业市场的竞争力！"
  },
  {
    "id": "bvid:BV1ABu96JEAR",
    "domain": "AI",
    "title": "【保姆级教程】WorkBuddy彻底玩明白！只看这一期就够了！10节付费课内容全公开，完整工作流+实战技巧全揭秘，零基础一小时从入门到精通【附完整资料】",
    "url": "http://www.bilibili.com/video/av117069685262348",
    "source": "workbuddy应用实战",
    "platform": "bilibili",
    "points": 356821,
    "published_at": "2026-08-10T06:05:50+00:00",
    "summary": "这可能是B站最全的WorkBuddy免费教程。咱们把付费课程做成了免费课程，感谢观众大老爷的两币奉上，有喜欢的也可以一键三连。 评论“蓝皮书”领取全套资料\n我花了整整一周，从安装到实战到管理思维，把WorkBuddy这个腾讯云AI桌面工作台拆成了10步，每一步都带实操。你不需要任何基础，跟着点就行。"
  },
  {
    "id": "bvid:BV1ia9UBPESQ",
    "domain": "AI",
    "title": "在VScode中配置Claude Code并接入DeepSeek V4 Pro【oo唠嗑教程】",
    "url": "http://www.bilibili.com/video/av116487012549813",
    "source": "沉默的羔丸ovo",
    "platform": "bilibili",
    "points": 319857,
    "published_at": "2026-04-29T08:23:29+00:00",
    "summary": "配置方法如下：\n(想用真心换取你的关注...蟹蟹泥...)\nsetting.json添加：\n{ &quot;name&quot;: &quot;ANTHROPIC_BASE_URL&quot;, &quot;value&quot;: &quot;https://xxxx&quot; }, \n{ &quot;name&quot;: &quot;ANTHROPIC_AUTH_TOKEN&quot;, "
  },
  {
    "id": "bvid:BV1qGc7zwEX6",
    "domain": "AI",
    "title": "史上最强 AI 编程工具Cursor来啦！Cursor保姆级使用教程！新手友好！看到就是赚到！！！",
    "url": "http://www.bilibili.com/video/av116061928226926",
    "source": "知名的阿呆同学",
    "platform": "bilibili",
    "points": 279218,
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
    "points": 278106,
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
    "points": 262472,
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
    "points": 251615,
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
    "points": 208386,
    "published_at": "2026-06-24T06:22:18+00:00",
    "summary": "【2026最新】B站最全最细的AI零基础入门教程，教学通俗易懂，小白适用！普通人也能抓住的AI风口！学完即就业，带你玩转AI赛道！大模型|agent"
  },
  {
    "id": "bvid:BV13R5EzbE6E",
    "domain": "AI",
    "title": "火遍全网的MCP是什么？怎么用？如何自己开发一个MCP服务？一个视频带你入门！",
    "url": "http://www.bilibili.com/video/av114358956854079",
    "source": "玄离199",
    "platform": "bilibili",
    "points": 180376,
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
    "points": 175771,
    "published_at": "2026-04-27T08:51:41+00:00",
    "summary": "Claude Code保姆级全套教程（软件+文档）\n   喜欢视频课程的同学一键三连多多支持一下，长按点赞五秒=lv6大佬 可以的发送彩色弹幕哦。\n配套源码项目已打包评论区回复up"
  },
  {
    "id": "bvid:BV1ExV36wEsE",
    "domain": "AI",
    "title": "VS Code 安装 Claude Code 并接入 DeepSeek！Claude Code for VS Code！VSCode使用ClaudeCode插件",
    "url": "http://www.bilibili.com/video/av116662871268177",
    "source": "FutureAI实验室",
    "platform": "bilibili",
    "points": 172118,
    "published_at": "2026-05-30T09:44:52+00:00",
    "summary": "本节视频编号71，评论区自助领取配套文档，记得一键三连哦！"
  },
  {
    "id": "bvid:BV16zPuzHE9n",
    "domain": "AI",
    "title": "Vibe Coding快速入门-喂饭级实操课（9节完）",
    "url": "http://www.bilibili.com/video/av116154538398331",
    "source": "桥哥聊AI",
    "platform": "bilibili",
    "points": 161523,
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
    "points": 154300,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV1uhVq69EVu",
    "domain": "AI",
    "title": "【2026最新Cursor使用教程】史上最强 AI 编程工具Cursor！Cursor保姆级使用教程！从入门到实战，零基础小白也能学会",
    "url": "http://www.bilibili.com/video/av116678943839396",
    "source": "有点子is丫",
    "platform": "bilibili",
    "points": 153554,
    "published_at": "2026-06-02T05:57:01+00:00",
    "summary": "【2026最新版】这绝对是B站讲的最好的Cursor全流程实战教程， 全程干货无废话，学完即就业！\n视频教程 附 所需源码 文档 软件"
  },
  {
    "id": "bvid:BV1wqMw6NEB6",
    "domain": "AI",
    "title": "Claude的安装并且如何配置ccswitch转接第三方API完整使用教程#codex #ai #安装#大模型#API#ccswitch#claude",
    "url": "http://www.bilibili.com/video/av116861479946306",
    "source": "老便秘了",
    "platform": "bilibili",
    "points": 119658,
    "published_at": "2026-07-04T11:32:40+00:00",
    "summary": "Claude的安装并且如何配置ccswitch转接第三方API完整使用教程#codex #ai #安装#大模型#API#ccswitch#claude"
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 104552,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1ZRbe6eENh",
    "domain": "AI",
    "title": "DeepSeek Harness安装和使用教程【最新完整版】零基础小白速通deepseek harness入门教程怎么下载插件如何安装如何使用全搞定！",
    "url": "http://www.bilibili.com/video/av117110286062691",
    "source": "鹏哥C语言",
    "platform": "bilibili",
    "points": 101158,
    "published_at": "2026-08-17T10:10:51+00:00",
    "summary": "欢迎大家来到鹏哥课堂！这份DeepSeek Harness教程专为零基础小白打造，全程手把手演示安装、启动Web界面、模型接入、基础任务实操。 很多小白卡在环境配置、命令报错、参数设置，本教程能让你避开各种坑，跟着操作就能成功运行。 搞懂 Agent = 模型 + Harness，让 AI 读写文件、执行命令、自主完成项目任务。本教程适合程序员、AI 爱好者及想上手本地智能体的同学等。希望大家把视"
  },
  {
    "id": "bvid:BV1QuZAY2EW1",
    "domain": "AI",
    "title": "10 分钟！零基础彻底学会 Cursor AI 编程 | Cursor AI 编程｜Cursor 进阶技巧 | Cursor 开发小程序 | 小白 AI 编程",
    "url": "http://www.bilibili.com/video/av114246079809849",
    "source": "Geek4Fun",
    "platform": "bilibili",
    "points": 93478,
    "published_at": "2025-03-29T14:02:03+00:00",
    "summary": "Hello 大家好，不需要懂任何编程知识，也不需要写一行代码，10 分钟让你彻底学会 AI 编程！手把手带你从:\n- 0基础到入门\n- 用户端的选择\n- 开发出一款非常有实用价值的应用\n- 借助 AI 来画设计图！\n- 接入 Deepseek 和把数据存在云服务器\n- 实用的 AI 进阶技巧"
  },
  {
    "id": "bvid:BV154426xEha",
    "domain": "AI",
    "title": "我的 AI 编程全流程：如何使用 AI 稳定交付一个高质量的产品",
    "url": "http://www.bilibili.com/video/av117178586240848",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 72220,
    "published_at": "2026-08-29T11:38:24+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1bjKkzPEEA",
    "domain": "AI",
    "title": "cursor+uniapp零基础开发工作报告小程序❗️30分钟保姆级教程",
    "url": "http://www.bilibili.com/video/av114756274947612",
    "source": "智码侃侃Tom",
    "platform": "bilibili",
    "points": 67051,
    "published_at": "2025-06-28T02:00:00+00:00",
    "summary": "这期视频我们将用AI完成前端开发+后端开发，并实现用户数据隔离的功能，让小程序达到可商用的标准，理论+实操+效果演示帮助零基础的同学快速上手。"
  },
  {
    "id": "bvid:BV1BnVpz5EBD",
    "domain": "AI",
    "title": "全网爆火的MCP到底是什么？如何使用MCP？【小白入门教程】",
    "url": "http://www.bilibili.com/video/av114461616643308",
    "source": "直男山禾",
    "platform": "bilibili",
    "points": 54677,
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
    "points": 48114,
    "published_at": "2026-08-07T12:15:00+00:00",
    "summary": "这期视频，我会手把手带你，用 AI 做出你的第一个 App。\n全程假设你没有任何编程和AI的基础，\n我们从如何写需求提示词开始，\n到确定页面结构和设计，\n产品需求文档，\n开发计划，\n第一版APP验收，\ngit代码存档，\n二次开发，\n界面美化，\n做好的APP也会开源给到大家，\n我也会演示如何获取这个项目源代码并且用AI继续定制开发，\n视频到最后，\n你会收获一个为自己的工作和生活定制的专属APP！\n和"
  },
  {
    "id": "bvid:BV1vYFQzQE4P",
    "domain": "AI",
    "title": "🚀OpenClaw高级使用经验之如何调用Claude Code最省Token！Claude Code Hooks回调+Agent Teams全自动开发零轮询",
    "url": "http://www.bilibili.com/video/av116046157647899",
    "source": "AI超元域",
    "platform": "bilibili",
    "points": 47671,
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
    "points": 47201,
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
    "points": 41265,
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
    "points": 36890,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1NpubzYE8c",
    "domain": "AI",
    "title": "Cursor用不了？三款AI编程工具完美代替Cursor",
    "url": "http://www.bilibili.com/video/av114863061864380",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 29683,
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
    "points": 28903,
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
    "points": 25240,
    "published_at": "2026-04-23T15:18:08+00:00",
    "summary": "Claude Code有2种多Agent模式：多个subagents模式和多个独立agent模式"
  },
  {
    "id": "bvid:BV1iTbX6JEyy",
    "domain": "AI",
    "title": "3分钟安装ClaudeCode并接入deepseek-v4-pro大模型",
    "url": "http://www.bilibili.com/video/av117105437443910",
    "source": "大海资源",
    "platform": "bilibili",
    "points": 20956,
    "published_at": "2026-08-16T13:34:16+00:00",
    "summary": "优雅的访问github：https://www.bilibili.com/video/BV1aiDjB8E83/\nClaude桌面版教程：https://www.bilibili.com/video/BV1anhG6KEYc/\ncodex桌面版教程：https://www.bilibili.com/video/BV1PkGg6BEBz/\n文字教程：https://www.dhzyw.com/arc"
  },
  {
    "id": "bvid:BV1WS5B6WECp",
    "domain": "AI",
    "title": "10分钟完成Ubuntu安装Claude Code并免费使用DeepSeekV4模型",
    "url": "http://www.bilibili.com/video/av116579891153749",
    "source": "不倒翁lhj",
    "platform": "bilibili",
    "points": 20738,
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
    "points": 16575,
    "published_at": "2026-05-09T07:11:36+00:00",
    "summary": "【简介】\nAnthropic 刚刚发布了用于创意工具的官方 Claude Connectors —— 其中 Blender 连接器对 3D 艺术家来说最重要。在本视频中，我将展示最佳的 Claude + Blender 免费设置，以及为什么这次更新可能会改变我们构建 3D 场景的方式。\n\n【你将学到】\n01:13 步骤 1：安装 Blender MCP 和 Claude Code\n02:31 步骤"
  },
  {
    "id": "bvid:BV18TZYY8EuJ",
    "domain": "AI",
    "title": "微软最新AI Agent入门课程 • 中英",
    "url": "http://www.bilibili.com/video/av114246130076146",
    "source": "Mindofuture",
    "platform": "bilibili",
    "points": 15733,
    "published_at": "2025-03-30T02:06:00+00:00",
    "summary": "在这门包含10节课的课程中，我们将带你从概念到代码，全面覆盖构建AI代理的基础知识。在这里找到完整的“AI代理入门”课程及代码示例\nhttps://github.com/microsoft/ai-agents-for-beginners\n\nP01 什么是AI代理\nP02 使用哪种AI代理框架\nP03 如何设计优秀的AI代理\nP04 什么是代理工具使用设计模式\nP05 什么是代理式RAG\nP06 如"
  },
  {
    "id": "bvid:BV1N4tH6GE2h",
    "domain": "AI",
    "title": "Anthropic重磅史诗升级！Claude Code 2.0全自动模式深度实测，多智能体协同全自动写完项目！",
    "url": "http://www.bilibili.com/video/av117184256810815",
    "source": "进化中的阿陈",
    "platform": "bilibili",
    "points": 14590,
    "published_at": "2026-08-30T11:39:11+00:00",
    "summary": "程序员彻底被解放了！Anthropic 重磅发布 Claude Code 2.0！新增王炸级 Auto Mode 全自动模式，无需人工确认全自动写完复杂项目；多 Sub-Agents 智能体协同并行开发，原生内置 iOS 模拟器实时调试 App 与无头浏览器测试，配合 Opus 5 简直强到离谱，速看实测！"
  },
  {
    "id": "hn:49458161",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia agrees to acquire Hugging Face for $13B",
    "url": "https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8",
    "source": "mfiguiere",
    "platform": "hackernews",
    "points": 1979,
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
    "id": "rss:https://www.eetimes.com/sk-hynixs-4b-hbm-project-targets-u-s-chipmaking-gap/",
    "domain": "AI 算力 / 半导体",
    "title": "SK Hynix’s $4B HBM Project Targets U.S. Chipmaking Gap",
    "url": "https://www.eetimes.com/sk-hynixs-4b-hbm-project-targets-u-s-chipmaking-gap/",
    "source": "Alan Patterson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T07:47:37+00:00",
    "summary": "SK Hynix’s $4B Indiana HBM fab aims to plug America’s AI chip packaging hole and build a Purdue-backed supply chain by 2029. The post SK Hynix’s $4B HBM Project Targets U.S. Chipmaking Gap appeared fi"
  },
  {
    "id": "rss:https://www.eetimes.com/automotive-software-defined-vehicle-sdv-architectures/",
    "domain": "AI 算力 / 半导体",
    "title": "Automotive Software Defined Vehicle (SDV) Architectures",
    "url": "https://www.eetimes.com/automotive-software-defined-vehicle-sdv-architectures/",
    "source": "Infineon Technologies, Arrow Electronics",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T07:46:38+00:00",
    "summary": "Join this presentation where our expert will highlight how modern vehicles are evolving into software-centric platforms that can be continuously updated, enhanced, and monetized throughout their lifec"
  },
  {
    "id": "rss:https://www.eetimes.com/suse-positions-hardware-choice-as-a-core-part-of-sovereign-ai/",
    "domain": "AI 算力 / 半导体",
    "title": "SUSE Positions Hardware Choice as a Core Part of Sovereign AI",
    "url": "https://www.eetimes.com/suse-positions-hardware-choice-as-a-core-part-of-sovereign-ai/",
    "source": "Yashasvini Razdan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T16:57:05+00:00",
    "summary": "SUSE says enterprises need the flexibility to change AI hardware without rebuilding their infrastructure. The post SUSE Positions Hardware Choice as a Core Part of Sovereign AI appeared first on EE Ti"
  },
  {
    "id": "rss:https://www.eetimes.com/when-off-the-shelf-isnt-enough/",
    "domain": "AI 算力 / 半导体",
    "title": "When Off-The-Shelf Isn’t Enough",
    "url": "https://www.eetimes.com/when-off-the-shelf-isnt-enough/",
    "source": "Bulgin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T14:00:00+00:00",
    "summary": "Solving High-Current Connectivity Challenges in Data Centre Cooling As data centre power densities increase, cooling equipment must deliver greater performance, reliability and consistency while suppo"
  },
  {
    "id": "rss:https://www.eetimes.com/advanced-cooling-technologies-address-the-automotive-heat-challenge/",
    "domain": "AI 算力 / 半导体",
    "title": "Advanced Cooling Technologies Address the Automotive Heat Challenge",
    "url": "https://www.eetimes.com/advanced-cooling-technologies-address-the-automotive-heat-challenge/",
    "source": "Danny J. Lohan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T07:46:55+00:00",
    "summary": "New cooling technologies are emerging as electric drivetrains, AI processors, and autonomous systems push automotive heat fluxes higher. The post Advanced Cooling Technologies Address the Automotive H"
  },
  {
    "id": "rss:https://www.tomshardware.com/networking/routers/tp-link-announces-its-first-consumer-wi-fi-8-routers-archer-8-ultra-preorder-commences-september-30-in-select-regions",
    "domain": "AI 算力 / 半导体",
    "title": "TP-Link announces its first consumer Wi-Fi 8 routers — Archer 8 Ultra preorder commences September 30, in select regions",
    "url": "https://www.tomshardware.com/networking/routers/tp-link-announces-its-first-consumer-wi-fi-8-routers-archer-8-ultra-preorder-commences-september-30-in-select-regions",
    "source": "Brandon Hill",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "TP-Link’s Wi-Fi 8 launch remains complicated in the US due to ongoing FCC restrictions"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/kingstons-nv3-1tb-pcie-4-0-ssd-drops-to-usd156-99-at-newegg-27-percent-off-brings-it-down-to-just-15-7-cents-per-gb",
    "domain": "AI 算力 / 半导体",
    "title": "Kingston's NV3 1TB PCIe 4.0 SSD drops to $156.99 at Newegg — 27% off brings it down to just 15.7 cents per GB",
    "url": "https://www.tomshardware.com/pc-components/ssds/kingstons-nv3-1tb-pcie-4-0-ssd-drops-to-usd156-99-at-newegg-27-percent-off-brings-it-down-to-just-15-7-cents-per-gb",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T18:16:28+00:00",
    "summary": "The Kingston NV3 may not be built for heavy workloads, but its respectable gaming performance and low power consumption make this PCIe 4.0 SSD a compelling secondary storage upgrade."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ram/g-skill-drops-new-amd-expo-ull-ram-for-ryzen-cpus-flare-x5x-brings-new-ull-optimized-subtimings-but-pricing-remains-a-mystery",
    "domain": "AI 算力 / 半导体",
    "title": "G.Skill drops new AMD EXPO ULL RAM for Ryzen CPUs — Flare X5X brings new ULL optimized subtimings, but pricing remains a mystery",
    "url": "https://www.tomshardware.com/pc-components/ram/g-skill-drops-new-amd-expo-ull-ram-for-ryzen-cpus-flare-x5x-brings-new-ull-optimized-subtimings-but-pricing-remains-a-mystery",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T17:28:43+00:00",
    "summary": "G.Skill launches new Flare X5X DDR5 memory kits with AMD EXPO ULL technology for Ryzen processors."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/trump-says-communities-that-reject-data-centers-want-to-end-up-being-backwards-and-poor-president-claims-china-could-not-be-happier-with-ai-data-center-backlash-in-the-us",
    "domain": "AI 算力 / 半导体",
    "title": "Trump says communities that reject data centers 'want to end up being backwards and poor' — President claims China 'could not be happier' with AI data center backlash in the US",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/trump-says-communities-that-reject-data-centers-want-to-end-up-being-backwards-and-poor-president-claims-china-could-not-be-happier-with-ai-data-center-backlash-in-the-us",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T17:05:57+00:00",
    "summary": "President Donald Trump claims that communities rejecting AI data center constructions \"want to end up being backwards and poor.\""
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/manufacturing/motorless-solid-state-cooler-uses-heat-to-cool-itself-could-recycle-processor-heat-into-cooling-shape-memory-alloy-films-could-turn-data-center-exhaust-into-refrigeration",
    "domain": "AI 算力 / 半导体",
    "title": "Motorless solid-state cooler uses heat to cool itself; could recycle processor heat into cooling — shape-memory alloy films could turn data center exhaust into refrigeration",
    "url": "https://www.tomshardware.com/tech-industry/manufacturing/motorless-solid-state-cooler-uses-heat-to-cool-itself-could-recycle-processor-heat-into-cooling-shape-memory-alloy-films-could-turn-data-center-exhaust-into-refrigeration",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T15:40:00+00:00",
    "summary": "German and Japanese researchers demonstrate a heat-driven elastocaloric cooler that uses shape-memory alloys to turn waste heat into cooling."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-usd240-on-a-four-item-gaming-build-combo-from-newegg-usd1-113-buys-a-ryzen-7-9800x3d-32gb-of-corsair-ddr5-ram-a-gigabyte-x870e-motherboard-plus-a-free-240mm-aio-and-amd-game-bundle",
    "domain": "AI 算力 / 半导体",
    "title": "Save $240 on a four-item gaming build combo from Newegg – $1,113 buys a Ryzen 7 9800X3D, 32GB of Corsair DDR5 RAM, a Gigabyte X870E Motherboard, plus a free 240mm AIO and AMD game bundle",
    "url": "https://www.tomshardware.com/pc-components/save-usd240-on-a-four-item-gaming-build-combo-from-newegg-usd1-113-buys-a-ryzen-7-9800x3d-32gb-of-corsair-ddr5-ram-a-gigabyte-x870e-motherboard-plus-a-free-240mm-aio-and-amd-game-bundle",
    "source": "Joe Shields",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T15:26:42+00:00",
    "summary": "This Newegg 3-item bundle pairs the fast, gaming-focused Ryzen 7 9800X3D with 32GB of Corsair Vengeance DDR5-6000 RAM and a Gigabyte X870E Aorus Pro board for only $1,113.99. That's a $240 savings, pl"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-and-lisa-su-snubbed-by-times-2026-ai-list-paris-hilton-and-ben-affleck-among-others-make-the-list-as-architects-of-ai-are-totally-absent",
    "domain": "AI 算力 / 半导体",
    "title": "Jensen Huang and Lisa Su snubbed by TIME’s 2026 list of top 100 AI leaders — Paris Hilton and Ben Affleck, among others, make the list as ‘Architects of AI’ inexplicably not listed",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-and-lisa-su-snubbed-by-times-2026-ai-list-paris-hilton-and-ben-affleck-among-others-make-the-list-as-architects-of-ai-are-totally-absent",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T14:52:59+00:00",
    "summary": "Nvidia’s sole representative on the fourth annual TIME100 AI is its head of sustainability, who sits alongside Paris Hilton and Ben Affleck."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpu-drivers/nvidias-latest-driver-update-breaks-mvolt-overclocking-functionality-nifty-open-source-app-allowed-users-to-increase-the-power-limit-to-700w-on-their-rtx-50-series-gpus-without-hardware-mods",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia's latest driver update breaks mVolt+ overclocking functionality — Nifty, open-source app allowed users to increase the power limit to 700W on their RTX 50-series GPUs without hardware mods",
    "url": "https://www.tomshardware.com/pc-components/gpu-drivers/nvidias-latest-driver-update-breaks-mvolt-overclocking-functionality-nifty-open-source-app-allowed-users-to-increase-the-power-limit-to-700w-on-their-rtx-50-series-gpus-without-hardware-mods",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T14:35:14+00:00",
    "summary": "Overclocking utility mVolt+ seems to have been blocked by the latest Nvidia driver update, hard crashing the moment you try to adjust the core power limit. However, it seems like a driver conflict mor"
  },
  {
    "id": "rss:https://www.tomshardware.com/maker-stem/xtool-f2-ultra-uv-dual-laser-engraver-review",
    "domain": "AI 算力 / 半导体",
    "title": "xTool F2 Ultra UV dual laser engraver review: So cool it’s hot",
    "url": "https://www.tomshardware.com/maker-stem/xtool-f2-ultra-uv-dual-laser-engraver-review",
    "source": "Denise Bertacchi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T14:30:00+00:00",
    "summary": "xTool’s new F2 Ultra UV cuts and engraves with cold UV light."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/key-nvidia-and-intel-supplier-raided-over-alleged-china-origin-fraud-unimicron-faces-probe-over-pcb-origin-washing-risk-of-40-percent-u-s-tariff-penalty",
    "domain": "AI 算力 / 半导体",
    "title": "Key Nvidia and Intel supplier raided over alleged China origin fraud — Unimicron faces probe over PCB origin washing, risk of 40% U.S. tariff penalty",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/key-nvidia-and-intel-supplier-raided-over-alleged-china-origin-fraud-unimicron-faces-probe-over-pcb-origin-washing-risk-of-40-percent-u-s-tariff-penalty",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T11:55:33+00:00",
    "summary": "Taiwanese prosecutors are investigating Unimicron, one of the world’s largest PCB and chip substrate makers and a key supplier to Nvidia, Intel, Google, and Amazon, over allegations that it shipped Ch"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/chinas-cxmt-beats-western-chipmakers-to-announcement-of-lpddr6-mass-production-xiaomi-smartphones-to-debut-industrys-first-lpddr6-chips",
    "domain": "AI 算力 / 半导体",
    "title": "China's CXMT beats Western chipmakers to announcement of LPDDR6 mass production — Xiaomi smartphones to debut industry’s first LPDDR6 chips",
    "url": "https://www.tomshardware.com/pc-components/dram/chinas-cxmt-beats-western-chipmakers-to-announcement-of-lpddr6-mass-production-xiaomi-smartphones-to-debut-industrys-first-lpddr6-chips",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T10:30:00+00:00",
    "summary": "CXMT claims to be the first to mass-produce LPDDR6 memory. Yet, for a niche phone."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/diehard-asus-customer-gets-rma-denied-for-a-cheap-2-4-ghz-headset-receiver-despite-spending-more-than-usd30-000-with-the-brand-firm-refuses-to-send-a-cheap-dongle-then-relents-after-social-media-backlash",
    "domain": "AI 算力 / 半导体",
    "title": "Diehard Asus customer gets RMA denied for a cheap 2.4 GHz headset receiver despite spending more than $30,000 with the brand — firm refuses to send a cheap dongle, then relents after social media back",
    "url": "https://www.tomshardware.com/peripherals/diehard-asus-customer-gets-rma-denied-for-a-cheap-2-4-ghz-headset-receiver-despite-spending-more-than-usd30-000-with-the-brand-firm-refuses-to-send-a-cheap-dongle-then-relents-after-social-media-backlash",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T10:00:00+00:00",
    "summary": "Asus refused to replace a loyal customer's wireless headset receiver because accessories are apparently not covered under warranty. The customer was not happy to see his dedication be put into questio"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/man-uses-robot-vacuum-to-covertly-record-his-wifes-affair-wins-divorce-settlement-but-gets-sentenced-to-prison-for-making-an-illegal-recording-husband-lands-behind-bars-after-counter-suit-over-privacy-rights",
    "domain": "AI 算力 / 半导体",
    "title": "Man uses robot vacuum to covertly record his wife's affair, wins divorce settlement but gets sentenced to prison for making an illegal recording — Husband lands behind bars after counter-suit over pri",
    "url": "https://www.tomshardware.com/tech-industry/man-uses-robot-vacuum-to-covertly-record-his-wifes-affair-wins-divorce-settlement-but-gets-sentenced-to-prison-for-making-an-illegal-recording-husband-lands-behind-bars-after-counter-suit-over-privacy-rights",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T09:30:00+00:00",
    "summary": "A Taiwanese man sued his wife for having an affair using recordings from a robot vacuum to prove his case. He won, but got sued by the wife for infringing on her personal privacy and was fined the equ"
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/speedy-34-inch-240-hz-ultrawide-oled-monitor-now-usd600-off-lg-ultragear-34gx900a-b-only-usd599-99",
    "domain": "AI 算力 / 半导体",
    "title": "Speedy 34-inch 240 Hz ultrawide OLED monitor now $600 off — LG UltraGear 34GX900A-B only $599.99",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/speedy-34-inch-240-hz-ultrawide-oled-monitor-now-usd600-off-lg-ultragear-34gx900a-b-only-usd599-99",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T18:08:43+00:00",
    "summary": "The LG UltraGear 34GX900A-B packs a fast 240 Hz OLED panel and 3440 x 1440 resolution into an immersive 800R curved display, now available for 50% off."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/dlss-5-mod-brings-next-gen-tech-to-old-ampere-gpus-but-frame-rates-are-horrible-most-games-tank-to-single-digits-high-end-gpus-can-hit-up-to-40-fps-in-some-cases",
    "domain": "AI 算力 / 半导体",
    "title": "DLSS 5 mod brings next-gen tech to old Ampere GPUs, but frame rates are horrible — most games tank to single digits, high-end GPUs can hit up to 40 FPS in some cases",
    "url": "https://www.tomshardware.com/pc-components/gpus/dlss-5-mod-brings-next-gen-tech-to-old-ampere-gpus-but-frame-rates-are-horrible-most-games-tank-to-single-digits-high-end-gpus-can-hit-up-to-40-fps-in-some-cases",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T16:30:30+00:00",
    "summary": "DLSS 5 now runs on Ampere GPUs thanks to a patched DLL, but performance is expectedly poor for the most part. You can get up to 30-40 FPS in edge cases with minimum in-game settings, but newer titles "
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/data-centers/spacex-starts-in-house-turbine-blade-manufacturing-to-boost-gas-powered-generator-output-for-elons-ai-data-centers-new-manufacturing-strategy-cuts-generator-delays-by-18-months",
    "domain": "AI 算力 / 半导体",
    "title": "SpaceX starts in-house turbine blade manufacturing to boost gas-powered generator output for Elon's AI data centers — new manufacturing strategy cuts generator delays by 18 months",
    "url": "https://www.tomshardware.com/tech-industry/data-centers/spacex-starts-in-house-turbine-blade-manufacturing-to-boost-gas-powered-generator-output-for-elons-ai-data-centers-new-manufacturing-strategy-cuts-generator-delays-by-18-months",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T14:49:50+00:00",
    "summary": "Turbine blades and vanes are among the most complicated turbine engine parts to build, with processes taking as long as 60 to 90 weeks. Because of this, Musk wants to bring their manufacturing in-hous"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/retro-gaming/donkey-kong-64-finally-gets-a-fully-native-pc-port-written-in-c-dk64-rekongpiled-brings-ultrawide-support-uncapped-framerates-and-zero-ai-code",
    "domain": "AI 算力 / 半导体",
    "title": "Donkey Kong 64 finally gets a fully native PC port written in C — DK64 ReKONGpiled brings ultrawide support, uncapped framerates, and zero AI code",
    "url": "https://www.tomshardware.com/video-games/retro-gaming/donkey-kong-64-finally-gets-a-fully-native-pc-port-written-in-c-dk64-rekongpiled-brings-ultrawide-support-uncapped-framerates-and-zero-ai-code",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T14:26:14+00:00",
    "summary": "A team of veteran developers has recompiled Donkey Kong 64 in C, so it runs natively on Windows, Linux, and Mac. The entire project is free, uses no generative AI, but still includes more features tha"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/massive-12tb-steam-leak-reveals-decades-of-unreleased-games-archived-files-include-unseen-half-life-2-episode-3-builds-and-assets",
    "domain": "AI 算力 / 半导体",
    "title": "Massive 12TB Steam leak reveals decades of unreleased games — archived files include unseen Half-Life 2: Episode 3 builds and assets",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/massive-12tb-steam-leak-reveals-decades-of-unreleased-games-archived-files-include-unseen-half-life-2-episode-3-builds-and-assets",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T12:48:42+00:00",
    "summary": "Early builds of Valve games from 2003 to 2013 have been found in a 12TB archive pulled from the company's old servers. These pre-release versions act like time capsules, preserving the state of the ga"
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/at-least-three-exhibitors-got-robbed-at-gamescom-2026-laptops-and-handhelds-with-unfinished-game-builds-stolen-from-locked-cabinets",
    "domain": "AI 算力 / 半导体",
    "title": "At least three exhibitors got robbed at Gamescom 2026 — laptops and handhelds with unfinished game builds stolen from locked cabinets",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/at-least-three-exhibitors-got-robbed-at-gamescom-2026-laptops-and-handhelds-with-unfinished-game-builds-stolen-from-locked-cabinets",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T12:34:59+00:00",
    "summary": "Several developers, publishers, and studios have had their laptops and handheld consoles stolen at Gamescom 2026. However, the organizers said that it's only responsible for general security, and exhi"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/external-ssds/adata-urban-tapsafe-2tb-review",
    "domain": "AI 算力 / 半导体",
    "title": "Adata Urban Tapsafe 2TB review: Solid-state storage you unlock with your phone",
    "url": "https://www.tomshardware.com/pc-components/external-ssds/adata-urban-tapsafe-2tb-review",
    "source": "Matt Safford",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T12:05:00+00:00",
    "summary": "Adata's Urban Tapsafe portable SSD sports magnetic face plates, a metal mounting clip, the ability to unlock the drive with your phone, and share selective access with others via an app."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/diy-archivists-push-budget-nikons-to-902-000-clicks-to-save-1-800-rare-books-team-trains-neural-net-on-photoshop-edits-to-process-526-000-scans",
    "domain": "AI 算力 / 半导体",
    "title": "DIY archivists push budget Nikons to 902,000 clicks to save 1,800 rare books — team trains neural net on Photoshop edits to process 526,000 scans",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/diy-archivists-push-budget-nikons-to-902-000-clicks-to-save-1-800-rare-books-team-trains-neural-net-on-photoshop-edits-to-process-526-000-scans",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T12:00:00+00:00",
    "summary": "An epic book preservation effort."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/dram/chinas-top-dram-maker-cxmt-sues-pentagon-over-its-blacklisting-argues-chips-are-standard-civilian-jedec-spec-not-defense-hardware",
    "domain": "AI 算力 / 半导体",
    "title": "China's top DRAM maker CXMT sues Pentagon over its blacklisting — argues chips are standard civilian JEDEC spec, not defense hardware",
    "url": "https://www.tomshardware.com/pc-components/dram/chinas-top-dram-maker-cxmt-sues-pentagon-over-its-blacklisting-argues-chips-are-standard-civilian-jedec-spec-not-defense-hardware",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T11:30:00+00:00",
    "summary": "Chinese DRAM maker CXMT wants the US Department of Defense to remove it from the list of companies linked to the Chinese military."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/power-supplies/corsair-rm1000e-2026-thermalprotect-power-supply-review",
    "domain": "AI 算力 / 半导体",
    "title": "Corsair RM1000e (2026) ThermalProtect power supply review: Temperature-sensing 12V-2x6 cable shuts the GPU down before a connector can melt",
    "url": "https://www.tomshardware.com/pc-components/power-supplies/corsair-rm1000e-2026-thermalprotect-power-supply-review",
    "source": "E. Fylladitakis",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T11:05:00+00:00",
    "summary": "Corsair's mainstream RMe series returns for 2026 with Platinum-class efficiency, a 500W fanless window, and a temperature-sensing 12V-2x6 cable that shuts the GPU down before a connector can melt."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/poor-liquid-metal-application-almost-destroys-asus-zephyrus-m16-laptop-eats-through-the-processor-lid-paste-replacement-triples-framerates-drops-temps-and-eliminates-hard-crashes",
    "domain": "AI 算力 / 半导体",
    "title": "Poor liquid metal application almost destroys Asus Zephyrus M16 laptop, eats through the processor lid — paste replacement triples framerates, drops temps, and eliminates hard crashes",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/poor-liquid-metal-application-almost-destroys-asus-zephyrus-m16-laptop-eats-through-the-processor-lid-paste-replacement-triples-framerates-drops-temps-and-eliminates-hard-crashes",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T11:00:00+00:00",
    "summary": "A user on Reddit shared their story about how the factory-applied liquid metal on their Asus Zephyrus M16 gaming laptop corroded the heatsink and lid of their CPU. It got so bad that the corrosion was"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/modders-solder-power-cables-directly-to-rtx-5090-pcb-to-eliminate-notorious-melting-16-pin-connector-bare-board-galax-hof-card-pulls-600w-under-chiller-cooling",
    "domain": "AI 算力 / 半导体",
    "title": "Modders solder power cables directly to RTX 5090 PCB to eliminate notorious melting 16-pin connector — bare-board Galax HOF card pulls 600W under chiller cooling",
    "url": "https://www.tomshardware.com/pc-components/gpus/modders-solder-power-cables-directly-to-rtx-5090-pcb-to-eliminate-notorious-melting-16-pin-connector-bare-board-galax-hof-card-pulls-600w-under-chiller-cooling",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T10:30:00+00:00",
    "summary": "TecLab, a Brazilian YouTuber, has just shown the most dangerous method of bypassing the 16-pin connector on an RTX 5090 — by soldering wires directly to the card's PCB. In an attempt to save the GPU f"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/us-military-uses-high-energy-lasers-to-shoot-down-three-mexican-cartel-drones-over-the-southern-border-narcos-suspected-of-using-uavs-for-surveillance-and-reconnaissance-to-support-illegal-activities",
    "domain": "AI 算力 / 半导体",
    "title": "US military uses high-energy lasers to shoot down three Mexican cartel drones over the southern border — narcos suspected of using UAVs for surveillance and reconnaissance to support illegal activitie",
    "url": "https://www.tomshardware.com/tech-industry/drones/us-military-uses-high-energy-lasers-to-shoot-down-three-mexican-cartel-drones-over-the-southern-border-narcos-suspected-of-using-uavs-for-surveillance-and-reconnaissance-to-support-illegal-activities",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-30T10:00:00+00:00",
    "summary": "The US military has successfully deployed a laser defense system on the southern border of the country and shot down alleged Mexican cartel drones. These UAVs are suspected of spotting U.S. law enforc"
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
    "id": "rss:https://www.eetimes.com/googles-marvell-deal-shows-custom-silicon-spreading-beyond-the-tpu/",
    "domain": "AI 算力 / 半导体",
    "title": "Google’s Marvell Deal Shows Custom Silicon Spreading Beyond the TPU",
    "url": "https://www.eetimes.com/googles-marvell-deal-shows-custom-silicon-spreading-beyond-the-tpu/",
    "source": "Pat Brans",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-28T21:59:13+00:00",
    "summary": "Google’s expanded relationship with Marvell suggests that memory, networking, storage, and data movement are candidates for specialization too. The post Google’s Marvell Deal Shows Custom Silicon Spre"
  },
  {
    "id": "rss:https://www.tomshardware.com/software/linux/california-lawmakers-unanimously-pass-linux-exemption-from-age-verification-law-software-distributed-under-the-gpl-mit-bsd-and-apache-licenses-are-exempt",
    "domain": "AI 算力 / 半导体",
    "title": "California lawmakers unanimously pass Linux exemption from age-verification law — software distributed under the GPL, MIT, BSD, and Apache licenses are exempt",
    "url": "https://www.tomshardware.com/software/linux/california-lawmakers-unanimously-pass-linux-exemption-from-age-verification-law-software-distributed-under-the-gpl-mit-bsd-and-apache-licenses-are-exempt",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T15:57:13+00:00",
    "summary": "California’s legislature has passed Assembly Bill 1856, exempting open-source operating systems from the State’s Digital Age Assurance Act months before the law is due to take effect on January 1, 202"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/usb-flash-drives/magnetic-core-memory-usb-drive-transfers-files-in-sneakernet-first-text-and-image-files-get-moved-between-pcs-via-hugely-constrained-archaic-memory-tech",
    "domain": "AI 算力 / 半导体",
    "title": "Magnetic core memory USB drive transfers files in sneakernet first — text and image files get moved between PCs via hugely constrained archaic memory tech",
    "url": "https://www.tomshardware.com/pc-components/usb-flash-drives/magnetic-core-memory-usb-drive-transfers-files-in-sneakernet-first-text-and-image-files-get-moved-between-pcs-via-hugely-constrained-archaic-memory-tech",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T15:14:44+00:00",
    "summary": "A dinner plate-sized magnetic core memory homebrew USB device has been used to transfer a text file from one PC to another for the first time."
  },
  {
    "id": "rss:https://www.tomshardware.com/monitors/gaming-monitors/get-a-32-inch-samsung-odyssey-g55c-curved-gaming-monitor-for-usd199-1440p-165-hz-screen-is-39-percent-off-at-amazon-for-a-limited-time",
    "domain": "AI 算力 / 半导体",
    "title": "Get a 32-inch Samsung Odyssey G55C curved gaming monitor for $199 — 1440p 165 Hz screen is 39% off at Amazon for a limited time",
    "url": "https://www.tomshardware.com/monitors/gaming-monitors/get-a-32-inch-samsung-odyssey-g55c-curved-gaming-monitor-for-usd199-1440p-165-hz-screen-is-39-percent-off-at-amazon-for-a-limited-time",
    "source": "Jowi Morales",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T14:20:00+00:00",
    "summary": "The Samsung Odyssey G55C is a 32-inch curved gaming monitor with a 1440p QHD resolution and 1ms response time. It's currently on sale at just $199.99, saving you $130 off its $329.99 MSRP."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/drones/startup-raises-usd7-million-to-build-backpack-portable-8-8-ounce-drone-interceptors-mara-claims-20x-cost-advantage-over-other-interceptors-priced-one-for-one-against-attack-drones",
    "domain": "AI 算力 / 半导体",
    "title": "Startup raises $7 million to build backpack-portable 8.8-ounce drone interceptors — Mara claims 20x cost advantage over other interceptors, priced one-for-one against attack drones",
    "url": "https://www.tomshardware.com/tech-industry/drones/startup-raises-usd7-million-to-build-backpack-portable-8-8-ounce-drone-interceptors-mara-claims-20x-cost-advantage-over-other-interceptors-priced-one-for-one-against-attack-drones",
    "source": "Luke James",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-29T14:16:20+00:00",
    "summary": "San Francisco defense startup Mara has secured $7 million in a pre-seed round to produce what it calls Spike, a portable counter-drone system housed inside a backpack."
  },
  {
    "id": "hn:49455507",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Announces Financial Results for Second Quarter Fiscal 2027",
    "url": "https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027",
    "source": "NewCzech",
    "platform": "hackernews",
    "points": 20,
    "published_at": "2026-08-26T20:35:48+00:00",
    "summary": ""
  },
  {
    "id": "hn:49417669",
    "domain": "AI 算力 / 半导体",
    "title": "Some of Russia's A.I. Drones Are Powered by Nvidia",
    "url": "https://www.nytimes.com/2026/08/24/world/europe/ukraine-war-nvidia-ai-autonomous-drones.html",
    "source": "reaperducer",
    "platform": "hackernews",
    "points": 18,
    "published_at": "2026-08-24T10:16:03+00:00",
    "summary": ""
  },
  {
    "id": "hn:49436796",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI claims its new chips can outperform Nvidia processors in tests",
    "url": "https://www.bloomberg.com/news/articles/2026-08-25/openai-claims-its-new-chips-can-outperform-nvidia-processors-in-tests",
    "source": "TravisJamison",
    "platform": "hackernews",
    "points": 16,
    "published_at": "2026-08-25T16:35:58+00:00",
    "summary": ""
  },
  {
    "id": "hn:49423067",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia Groq 3 LPX Unlocks Ultrafast Interactivity at Long Context",
    "url": "https://developer.nvidia.com/blog/how-nvidia-groq-3-lpx-unlocks-ultrafast-interactivity-at-long-context-on-nvidia-vera-rubin/",
    "source": "frozenport",
    "platform": "hackernews",
    "points": 14,
    "published_at": "2026-08-24T17:22:37+00:00",
    "summary": ""
  },
  {
    "id": "hn:49424444",
    "domain": "AI 算力 / 半导体",
    "title": "Nvidia customers notified about AI-related price hikes above 15%",
    "url": "https://www.reuters.com/business/nvidia-customers-notified-about-ai-related-price-hikes-above-15-bloomberg-news-2026-08-22/",
    "source": "dgellow",
    "platform": "hackernews",
    "points": 13,
    "published_at": "2026-08-24T19:06:30+00:00",
    "summary": ""
  },
  {
    "id": "hn:49464837",
    "domain": "AI 算力 / 半导体",
    "title": "U.S. considers fresh round of tariffs on semiconductors, report says",
    "url": "https://www.cnbc.com/2026/08/27/trump-semiconductor-tech-tariffs.html",
    "source": "mikhael",
    "platform": "hackernews",
    "points": 11,
    "published_at": "2026-08-27T13:45:11+00:00",
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
    "id": "hn:49515293",
    "domain": "大厂 AI 动态",
    "title": "29,787 Open Ollama Servers and an Unsolved Mystery",
    "url": "https://day50.dev/woahllama/",
    "source": "kristopolous",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-08-31T21:52:49+00:00",
    "summary": ""
  },
  {
    "id": "rss:https://www.theverge.com/tech/987032/google-tv-streamer-price-increase",
    "domain": "大厂 AI 动态",
    "title": "The Google TV Streamer now costs $50 more",
    "url": "https://www.theverge.com/tech/987032/google-tv-streamer-price-increase",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T22:32:51+00:00",
    "summary": "Google raised the price of its 4K streaming box to $149, up $50 from its original $99 price. The new price is currently live at the Google Store and Best Buy, but Amazon appears to still be offering t"
  },
  {
    "id": "rss:https://www.theverge.com/tech/985986/jmgo-4k-gaming-projector-price-specs",
    "domain": "大厂 AI 动态",
    "title": "JMGO’s very bright all-in-one projector looks ideal for gamers and sports",
    "url": "https://www.theverge.com/tech/985986/jmgo-4k-gaming-projector-price-specs",
    "source": "Thomas Ricker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T22:00:00+00:00",
    "summary": "JMGO's 4K 120Hz Iris Ultra Max all-in-one Google TV projector is now available outside China. It gets its name from a new dual-iris system that lets it produce an impressive 10,000:1 native contrast, "
  },
  {
    "id": "rss:https://www.theverge.com/tech/986982/amazon-advertising-prices-ftc-lawsuit",
    "domain": "大厂 AI 动态",
    "title": "FTC lawsuit alleges Amazon has been ‘secretly and systematically’ overcharging for ads",
    "url": "https://www.theverge.com/tech/986982/amazon-advertising-prices-ftc-lawsuit",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T21:41:42+00:00",
    "summary": "The FTC and 22 state attorneys general are suing Amazon for allegedly using a \"secret ad surcharge\" to drive up prices for ads on its website and app. FTC chairman Andrew Ferguson claims in a blog pos"
  },
  {
    "id": "rss:https://www.theverge.com/tech/986967/apple-vision-pro-mlb-red-sox-yankees-immersive-game",
    "domain": "大厂 AI 动态",
    "title": "I went to the loneliest baseball game on Apple Vision Pro",
    "url": "https://www.theverge.com/tech/986967/apple-vision-pro-mlb-red-sox-yankees-immersive-game",
    "source": "Mia Sato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T21:18:27+00:00",
    "summary": "This weekend, I strapped on an Apple Vision Pro to watch a baseball game in immersive virtual reality for the first time. It was technically impressive, visually pretty remarkable, and also didn't mak"
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/986901/alienware-qdoled-2726dm-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Alienware’s budget-friendly QD-OLED is discounted for the first time",
    "url": "https://www.theverge.com/gadgets/986901/alienware-qdoled-2726dm-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T19:31:59+00:00",
    "summary": "While memory and storage prices are still high, there are still good discounts on other gaming-related hardware. Take Alienware’s AW2726DM, for example. Dell is selling it for $319.99, a $30 break fro"
  },
  {
    "id": "rss:https://www.theverge.com/news/986721/car-tech-survey-jd-power-smart-ignition",
    "domain": "大厂 AI 动态",
    "title": "Car owners want tech they can ignore",
    "url": "https://www.theverge.com/news/986721/car-tech-survey-jd-power-smart-ignition",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T17:11:17+00:00",
    "summary": "Automakers keep shoving more tech into their cars, despite evidence that consumers are increasingly fed up with huge screens and glitchy software. In fact, the features that car owners appreciate the "
  },
  {
    "id": "rss:https://www.theverge.com/tech/986869/apple-phil-schiller-stepping-down",
    "domain": "大厂 AI 动态",
    "title": "Phil Schiller is leaving his biggest jobs at Apple",
    "url": "https://www.theverge.com/tech/986869/apple-phil-schiller-stepping-down",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T16:54:07+00:00",
    "summary": "Longtime Apple executive Phil Schiller is stepping down from his role as the head of the App Store and Apple events, according to a report from Bloomberg. Following the change, Schiller will keep his "
  },
  {
    "id": "rss:https://www.theverge.com/tech/986847/markiplier-gopro-investor",
    "domain": "大厂 AI 动态",
    "title": "Markiplier is now GoPro’s biggest shareholder",
    "url": "https://www.theverge.com/tech/986847/markiplier-gopro-investor",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T16:38:10+00:00",
    "summary": "YouTuber Mark \"Markiplier\" Fischbach has invested enough in GoPro to become its single largest shareholder, with an 8.5 percent stake in the company, Bloomberg reports. Speaking to Bloomberg, Fischbac"
  },
  {
    "id": "rss:https://www.theverge.com/tech/986832/read-tim-cooks-final-message-as-ceo-to-apple-staff",
    "domain": "大厂 AI 动态",
    "title": "Read Tim Cook&#8217;s final message to Apple staff as CEO",
    "url": "https://www.theverge.com/tech/986832/read-tim-cooks-final-message-as-ceo-to-apple-staff",
    "source": "TC. Sottek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T16:30:45+00:00",
    "summary": "Steve Jobs' successor carried the torch of the iPhone and built Apple into a global powerhouse with few rivals. Since becoming CEO in 2011, Tim Cook has led the company to become one of the most domin"
  },
  {
    "id": "rss:https://www.theverge.com/tech/986789/linux-debian-generative-ai-policy",
    "domain": "大厂 AI 动态",
    "title": "Debian won&#8217;t ban AI code from its Linux distribution",
    "url": "https://www.theverge.com/tech/986789/linux-debian-generative-ai-policy",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T15:34:58+00:00",
    "summary": "Debian voted to allow developers to use AI tools in their contributions to the Linux distribution's \"development, maintenance, [and] documentation.\" The new policy on AI acknowledges that \"responsible"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/magna-increases-bet-on-battery-swapping-in-india-with-35m-for-yuma/",
    "domain": "大厂 AI 动态",
    "title": "Magna increases bet on battery swapping in India with $35M for Yuma",
    "url": "https://techcrunch.com/2026/08/31/magna-increases-bet-on-battery-swapping-in-india-with-35m-for-yuma/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T05:00:00+00:00",
    "summary": "Magna's investment in Yuma Energy has reached $87 million as the Canadian auto supplier increases its majority stake in the Indian battery-swapping firm."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/lachy-groom-backs-indian-startup-aiming-to-keep-aircraft-aloft-for-a-year/",
    "domain": "大厂 AI 动态",
    "title": "Lachy Groom backs Indian startup aiming to keep aircraft aloft for a year",
    "url": "https://techcrunch.com/2026/08/31/lachy-groom-backs-indian-startup-aiming-to-keep-aircraft-aloft-for-a-year/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T00:30:00+00:00",
    "summary": "Founded by a 20-year-old, Alteon is developing autonomous aircraft that hopes to harvest wind energy to stay aloft for several months."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/apple-shares-shocking-evidence-against-former-employee-accused-of-stealing-company-data-for-openai/",
    "domain": "大厂 AI 动态",
    "title": "Apple shares ‘shocking evidence’ against former employee accused of stealing company data for OpenAI",
    "url": "https://techcrunch.com/2026/08/31/apple-shares-shocking-evidence-against-former-employee-accused-of-stealing-company-data-for-openai/",
    "source": "Amanda Silberling",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T00:13:00+00:00",
    "summary": "Apple says it has evidence that a former employee destroyed evidence of data theft after learning he was under investigation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/polymarket-reportedly-raises-300-million-from-donald-trump-jr-s-investment-fund/",
    "domain": "大厂 AI 动态",
    "title": "Polymarket reportedly raises $300 million from Donald Trump Jr.’s investment fund",
    "url": "https://techcrunch.com/2026/08/31/polymarket-reportedly-raises-300-million-from-donald-trump-jr-s-investment-fund/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T23:41:10+00:00",
    "summary": "The firm, 1789 Capital, led the funding round that reportedly will total around $1 billion."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/a16z-brings-growth-fund-to-8-5b-days-after-launching-new-1-1b-fund/",
    "domain": "大厂 AI 动态",
    "title": "a16z brings growth fund to $8.5B days after launching new $1.1B fund",
    "url": "https://techcrunch.com/2026/08/31/a16z-brings-growth-fund-to-8-5b-days-after-launching-new-1-1b-fund/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T23:14:14+00:00",
    "summary": "Andreessen Horowitz held out its hand and returned with billions more in new funds to invest in startups."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/a-group-funded-by-andreessen-horowitz-and-brockman-plan-data-center-ads-to-sway-midterms/",
    "domain": "大厂 AI 动态",
    "title": "A group funded by Andreessen, Horowitz, and Brockman plans data center ads to sway midterms",
    "url": "https://techcrunch.com/2026/08/31/a-group-funded-by-andreessen-horowitz-and-brockman-plan-data-center-ads-to-sway-midterms/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T22:14:05+00:00",
    "summary": "Build American AI plans to lobby voters in select states about the virtues of data centers by spending millions of dollars on ads."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/ftc-accuses-amazon-of-running-a-secret-ad-surcharge-scheme-in-new-lawsuit/",
    "domain": "大厂 AI 动态",
    "title": "FTC accuses Amazon of running a ‘secret ad surcharge scheme’ in new lawsuit",
    "url": "https://techcrunch.com/2026/08/31/ftc-accuses-amazon-of-running-a-secret-ad-surcharge-scheme-in-new-lawsuit/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T20:20:25+00:00",
    "summary": "Amazon is facing a new lawsuit from the FTC and 22 states for allegedly secretly charging businesses more for advertising."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/the-pentagon-now-has-its-own-version-of-chatgpt-and-grok/",
    "domain": "大厂 AI 动态",
    "title": "The Pentagon now has its own version of ChatGPT and Grok",
    "url": "https://techcrunch.com/2026/08/31/the-pentagon-now-has-its-own-version-of-chatgpt-and-grok/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T20:13:45+00:00",
    "summary": "Versions of OpenAI's ChatGPT and SpaceXAI's Grok will join Google's Gemini on the Pentagon's central portal for AI tools."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/apply-now-to-host-a-side-event-at-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Apply now to host a Side Event at TechCrunch Disrupt 2026",
    "url": "https://techcrunch.com/2026/08/31/apply-now-to-host-a-side-event-at-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T19:32:21+00:00",
    "summary": "Apply before September 4 to be a part of the TechCrunch Disrupt community by hosting your own Side Event."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/instagram-puts-new-limits-on-undisclosed-ai-profiles/",
    "domain": "大厂 AI 动态",
    "title": "Instagram puts new limits on undisclosed AI profiles",
    "url": "https://techcrunch.com/2026/08/31/instagram-puts-new-limits-on-undisclosed-ai-profiles/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T19:16:59+00:00",
    "summary": "As frustration over AI influencers has been growing, Instagram is limiting the reach of undisclosed AI profiles."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/apples-top-app-store-exec-phil-schiller-follows-wave-of-exits-as-ceo-tim-cook-steps-down/",
    "domain": "大厂 AI 动态",
    "title": "Apple’s top App Store exec, Phil Schiller, follows wave of exits as CEO Tim Cook steps down",
    "url": "https://techcrunch.com/2026/08/31/apples-top-app-store-exec-phil-schiller-follows-wave-of-exits-as-ceo-tim-cook-steps-down/",
    "source": "Lucas Ropek",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T19:02:06+00:00",
    "summary": "The longtime executive won't be leaving Apple just yet but staff at the company say it's a step closer to Schiller retiring."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/microsoft-tests-fix-for-latest-hours-long-outlook-outage/",
    "domain": "大厂 AI 动态",
    "title": "Microsoft tests fix for latest hours-long Outlook outage",
    "url": "https://techcrunch.com/2026/08/31/microsoft-tests-fix-for-latest-hours-long-outlook-outage/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T18:56:41+00:00",
    "summary": "Microsoft says it's testing a fix for the widespread Outlook issues that have led to email delays and failures."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/kalshi-bans-george-santos-for-life-over-state-of-the-union-bets/",
    "domain": "大厂 AI 动态",
    "title": "Kalshi bans George Santos for life over State of the Union bets",
    "url": "https://techcrunch.com/2026/08/31/kalshi-bans-george-santos-for-life-over-state-of-the-union-bets/",
    "source": "Kirsten Korosec",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T18:53:41+00:00",
    "summary": "The disciplinary action comes two months after the Commodity Futures Trading Commission settled charges against Santos."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/harvard-law-dropout-raises-6m-for-blue-voice-to-build-a-harvey-for-police-officers/",
    "domain": "大厂 AI 动态",
    "title": "Harvard Law dropout raises $6M for Blue Voice to build a ‘Harvey for police officers’",
    "url": "https://techcrunch.com/2026/08/31/harvard-law-dropout-raises-6m-for-blue-voice-to-build-a-harvey-for-police-officers/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T18:35:11+00:00",
    "summary": "Blue Voice is trained on department-specific laws, local ordinances, protocols, and guidelines that general-purpose AI tools can't access on the public internet."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/hackers-claim-millions-of-patient-records-stolen-during-data-breach-at-healthcare-giant-mckesson/",
    "domain": "大厂 AI 动态",
    "title": "Hackers claim millions of patient records stolen during data breach at healthcare giant McKesson",
    "url": "https://techcrunch.com/2026/08/31/hackers-claim-millions-of-patient-records-stolen-during-data-breach-at-healthcare-giant-mckesson/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T18:10:09+00:00",
    "summary": "The company, which distributes medicines and medical devices to hospitals and healthcare practices across the U.S., said it was hacked and expects intermittent service degradation."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/ryan-breslow-is-raising-up-to-27m-in-pay-to-play-bridge-funding-to-save-bolt/",
    "domain": "大厂 AI 动态",
    "title": "Ryan Breslow is raising up to $27M in pay-to-play bridge funding to save Bolt",
    "url": "https://techcrunch.com/2026/08/31/ryan-breslow-is-raising-up-to-27m-in-pay-to-play-bridge-funding-to-save-bolt/",
    "source": "Marina Temkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T17:14:44+00:00",
    "summary": "The controversial founder of the checkout startup once valued at $11 billion is putting in $5 million of his own money."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/tim-cooks-parting-message-apple-is-in-the-hands-of-a-product-builder/",
    "domain": "大厂 AI 动态",
    "title": "Tim Cook’s parting message: Apple is in the hands of a product builder",
    "url": "https://techcrunch.com/2026/08/31/tim-cooks-parting-message-apple-is-in-the-hands-of-a-product-builder/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T17:02:42+00:00",
    "summary": "Tim Cook’s farewell memo to Apple employees offers a glimpse at how he wants John Ternus to be seen: as a product builder with deep experience across the iPhone, Mac, AirPods, and other major hardware"
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/vlc-crosses-7-billion-downloads/",
    "domain": "大厂 AI 动态",
    "title": "VLC crosses 7 billion downloads",
    "url": "https://techcrunch.com/2026/08/31/vlc-crosses-7-billion-downloads/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T16:07:46+00:00",
    "summary": "In our world of expensive streaming platforms, the very free and offline VLC media player has crossed 7 billion downloads."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/three-year-old-ai-media-search-startup-clipto-hits-a-250m-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Clipto uses AI to search terabytes of video and is now valued at $250M",
    "url": "https://techcrunch.com/2026/08/31/three-year-old-ai-media-search-startup-clipto-hits-a-250m-valuation/",
    "source": "Kate Park",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T16:00:00+00:00",
    "summary": "The three-year-old startup says it reached $15 million in ARR and profitability before raising its latest $15 million round."
  },
  {
    "id": "rss:https://techcrunch.com/2026/08/31/how-ai-could-make-it-harder-for-governments-to-use-hacking-tools/",
    "domain": "大厂 AI 动态",
    "title": "How AI could make it harder for governments to use hacking tools",
    "url": "https://techcrunch.com/2026/08/31/how-ai-could-make-it-harder-for-governments-to-use-hacking-tools/",
    "source": "Lorenzo Franceschi-Bicchierai",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T15:19:32+00:00",
    "summary": "AI is proving effective at finding and exploiting vulnerabilities. Some say this will make it harder for governments to use hacking tools and spyware and could reignite calls to backdoor devices."
  },
  {
    "id": "rss:https://stratechery.com/2026/meta-settles-a-framework-for-regulating-content-the-rest-of-big-tech/",
    "domain": "大厂 AI 动态",
    "title": "Meta Settles, A Framework For Regulating Content, The Rest of Big Tech",
    "url": "https://stratechery.com/2026/meta-settles-a-framework-for-regulating-content-the-rest-of-big-tech/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T10:00:00+00:00",
    "summary": "Meta's settlement makes sense for all parties, but the entire sage highlights why any solution to regulating technology feels off."
  },
  {
    "id": "rss:https://arstechnica.com/cars/2026/08/the-bentley-supersports-a-stripped-out-engineers-indulgence/",
    "domain": "大厂 AI 动态",
    "title": "The Bentley Supersports: A stripped-out engineer's indulgence",
    "url": "https://arstechnica.com/cars/2026/08/the-bentley-supersports-a-stripped-out-engineers-indulgence/",
    "source": "Jonathan M. Gitlin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T23:01:16+00:00",
    "summary": "It's the lightest Bentley in 85 years."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/08/trump-admin-shelves-cyclospora-research-despite-record-breaking-outbreak/",
    "domain": "大厂 AI 动态",
    "title": "Trump admin shelves Cyclospora research despite record-breaking outbreak",
    "url": "https://arstechnica.com/health/2026/08/trump-admin-shelves-cyclospora-research-despite-record-breaking-outbreak/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T21:23:09+00:00",
    "summary": "The CDC has tallied nearly 30,000 confirmed and probable cases this summer."
  },
  {
    "id": "rss:https://arstechnica.com/staff/2026/08/get-in-on-the-ars-community-that-doesnt-fit-beneath-an-article/",
    "domain": "大厂 AI 动态",
    "title": "Get in on the Ars community that doesn’t fit beneath an article",
    "url": "https://arstechnica.com/staff/2026/08/get-in-on-the-ars-community-that-doesnt-fit-beneath-an-article/",
    "source": "Eric Bangeman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T21:12:01+00:00",
    "summary": "You've read the stories. Now check out our forums."
  },
  {
    "id": "rss:https://arstechnica.com/culture/2026/08/review-coyote-vs-acme-is-an-unabashed-love-letter-to-looney-tunes/",
    "domain": "大厂 AI 动态",
    "title": "Review: Coyote vs. Acme is an unabashed love letter to Looney Tunes",
    "url": "https://arstechnica.com/culture/2026/08/review-coyote-vs-acme-is-an-unabashed-love-letter-to-looney-tunes/",
    "source": "Jennifer Ouellette",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T20:02:16+00:00",
    "summary": "Director Dave Green's live action/animated hybrid captures smart, subversive weirdness of the classic cartoons."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/trump-tells-fcc-to-punish-journalist-for-calling-his-election-results-mixed/",
    "domain": "大厂 AI 动态",
    "title": "Trump tells FCC to punish journalist for calling his election results \"mixed\"",
    "url": "https://arstechnica.com/tech-policy/2026/08/trump-tells-fcc-to-punish-journalist-for-calling-his-election-results-mixed/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T18:39:25+00:00",
    "summary": "Trump furious at NBC's Kristen Welker for saying he had mixed results in primary endorsements."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/08/zlibrary-my-beloved-anthropic-staff-chats-extolling-piracy-cited-in-sony-suit/",
    "domain": "大厂 AI 动态",
    "title": "“Zlibrary my beloved”: Anthropic staff chats extolling piracy cited in Sony suit",
    "url": "https://arstechnica.com/tech-policy/2026/08/zlibrary-my-beloved-anthropic-staff-chats-extolling-piracy-cited-in-sony-suit/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-08-31T18:10:45+00:00",
    "summary": "Lawsuit: Anthropic’s torrenting totally screwed songwriters as AI songs top charts."
  },
  {
    "id": "hn:49511824",
    "domain": "股票",
    "title": "Apple Is Suddenly an AI Infra Stock as OpenAI Buys 10k+ Macs",
    "url": "https://247wallst.com/investing/2026/08/31/apple-is-suddenly-an-ai-infrastructure-stock-as-openai-buys-macs-by-the-tens-of-thousands/",
    "source": "prabal97",
    "platform": "hackernews",
    "points": 37,
    "published_at": "2026-08-31T16:44:15+00:00",
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
    "id": "wscn:3780819",
    "domain": "股票",
    "title": "两部门：9月1日起外籍个人股息红利不再免征个税",
    "url": "https://wallstreetcn.com/articles/3780819",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T08:23:22+00:00",
    "summary": "外籍个人从外商投资企业取得的股息红利所得，也应按照“利息、股息、红利所得”项目缴纳个人所得税，适用20%税率。专家认为，从税制公平的角度来看，同样是投资者，从一个被投资企业分配到股息红利时，如果外国投资者可以免税，而中国投资者却需要缴税，这显然是不够公平的。"
  },
  {
    "id": "wscn:3780791",
    "domain": "股票",
    "title": "A股三大股指集体收跌，农业股逆势掀涨停潮，银行批量创新高，算力硬件下挫，恒指跌1%，科网股普跌",
    "url": "https://wallstreetcn.com/articles/3780791",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T08:15:48+00:00",
    "summary": "盘面上，个股涨多跌少，沪深京三市超3300股飘红，今日成交2.05万亿。沪深两市成交额2.03万亿，较上一个交易日缩量近1000亿。板块方面，中际旭创午后突袭未果，AI核心标的普遍低迷，对指数形成压制。银行股批量刷新历史新高，农业股大面积涨停表现出众，传媒板块继续火热，零售、白酒、医美、保险板块活跃。"
  },
  {
    "id": "wscn:3780815",
    "domain": "股票",
    "title": "印度总理莫迪又喊话：非必要，不买黄金",
    "url": "https://wallstreetcn.com/articles/3780815",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T08:10:26+00:00",
    "summary": "印度总理莫迪年内第二次公开劝阻民众购买黄金，提倡自力更生。现货黄金日内跌破4400美元关口。印度2025-26财年黄金进口额达创纪录的719.8亿美元（同比增24%），国际金价大涨加剧了以美元结算的外汇与卢比汇率压力。"
  },
  {
    "id": "wscn:3780816",
    "domain": "股票",
    "title": "透视广发证券半年报：核心业务全面开花，AI双向布局加速增长",
    "url": "https://wallstreetcn.com/articles/3780816",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T07:56:50+00:00",
    "summary": "今年以来，A股市场持续回暖，券商业绩继续保持强劲增长。\n作为头部券商，广发证券交出了一份高增长的成绩..."
  },
  {
    "id": "wscn:3780814",
    "domain": "股票",
    "title": "日本财务大臣淡化加息压力说法：未与贝森特讨论货币政策",
    "url": "https://wallstreetcn.com/articles/3780814",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T07:55:30+00:00",
    "summary": "日本财务大臣片山皋月称，日美已就维持日元有序波动达成共识，但否认与美财长贝森特讨论货币政策。然而，据NHK此前报道，贝森特在G20会议期间与片山皋月及日本央行行长植田和男会谈时，明确表示日本下一步应当加息。目前日元再度逼近160关口，市场对日本央行9月会议加息预期持续升温。"
  },
  {
    "id": "wscn:3780811",
    "domain": "股票",
    "title": "“沪八条”实施以来市场反馈积极，8月一、二手住房成交面积同比增15%",
    "url": "https://wallstreetcn.com/articles/3780811",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T07:18:11+00:00",
    "summary": "\"沪八条\"出台后，上海楼市显著回暖：一手住房日均签约定金量激增90%，新开盘项目认购比超1.5；二手住房连续9个月单月成交逾2万套，成交价格环比上升。外环外市场尤为活跃，部分项目日均来访量提升50%、成交量翻番。房票安置加速推进，6个城中村项目已发放房票446张。"
  },
  {
    "id": "wscn:3780800",
    "domain": "股票",
    "title": "H酸一天涨1万元，染料行业六年价格战要结束了吗？",
    "url": "https://wallstreetcn.com/premium/articles/3780800?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T07:17:47+00:00",
    "summary": "从2025年底约2.5万元/吨，到今年高位报价12万元/吨，分散染料核心中间体还原物价格数倍上涨；8月31日，H酸市场均价进一步升至10万元/吨。与此同时，分散黑、深蓝、活性黑等主流染料成交价持续抬升，小品种染料也开始补涨。\n表面看，这是中间体紧缺叠加“金九银十”的涨价行情；更值得关注的是，多年低价竞争之后，染料行业的成本曲线、库存结构和企业价格策略正在同步变化。\n这一轮上涨究竟只是旺季脉冲，还是"
  },
  {
    "id": "wscn:3780808",
    "domain": "股票",
    "title": "主权债息创2008年新高！美日国债相继破位，全球债市为何全线溃败？",
    "url": "https://wallstreetcn.com/articles/3780808",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T07:10:14+00:00",
    "summary": "10年期美债收益率冲破4.78%直逼5%大关，10年期日债收益率时隔30年首度触及3%——全球两大基准国债相继破位背后，是宏观压力的集中爆发：全球通胀高企、财政赤字失控、多国降息无望。5%的美债收益率或许不是终点，而是新常态的起点。"
  },
  {
    "id": "wscn:3780812",
    "domain": "股票",
    "title": "三部门发布《汽车行业境外竞争行为与合规建设指引》：规范境外定价秩序，强化车联网数据合规",
    "url": "https://wallstreetcn.com/articles/3780812",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T07:06:05+00:00",
    "summary": "《指引》提出，企业应建立以成本为基础、国际市场供求为导向的定价策略，制定清晰价格梯度，合理确定国家（地区）间价格差异。应确保车联网及自动驾驶相关信息收集、使用、保护及数据跨境传输合规，保护消费者个人隐私。加强境外反垄断合规建设，有效识别、评估和管控各类反垄断法律风险。"
  },
  {
    "id": "wscn:3780810",
    "domain": "股票",
    "title": "美伊冲突持续之际，美陆军部长辞职，五角大楼高层接连出走",
    "url": "https://wallstreetcn.com/articles/3780810",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T06:56:13+00:00",
    "summary": "美陆军部长Driscoll因与国防部长Hegseth在解雇陆军参谋长及现代化改革等重大决策上产生严重分歧而辞职，致使陆军两大要职同时悬空。此番离职凸显五角大楼高层人事动荡加剧，而声誉良好的Driscoll未来或加入副总统Vance的竞选团队。"
  },
  {
    "id": "wscn:3780806",
    "domain": "股票",
    "title": "今年苹果发布会最大的悬念，不是折叠屏",
    "url": "https://wallstreetcn.com/articles/3780806",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T06:43:50+00:00",
    "summary": "对中国用户而言，真正的大事是：缺席近两年的Apple智能终于完成备案，联手千问、百度有望正式登陆国行iPhone——这或许比折叠屏更值得期待。此外，苹果将打破惯例延后发布标准版，秋季仅保留搭载2nm芯片的Pro系列及首款折叠屏。阵容全面高端化叠加成本暴涨，新机涨价或成定局。"
  },
  {
    "id": "wscn:3780807",
    "domain": "股票",
    "title": "标普500站稳200日均线，9月可能躲过“最差月份”的大跌魔咒",
    "url": "https://wallstreetcn.com/articles/3780807",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T06:43:17+00:00",
    "summary": "尽管9月历史数据表现较弱，但标普500因站稳200日均线且处于历史高位附近，技术面下行风险大幅收窄。指数8月录得2021年以来最佳同月表现，年内已累涨逾12%。分析师认为四季度反弹格局初具雏形，但通胀走势与中东地缘局势仍是最大变量。"
  },
  {
    "id": "wscn:3780704",
    "domain": "股票",
    "title": "敢为天下先！AI长剧首次上星湖南卫视：全AI影视内容工业化的关键一跃？",
    "url": "https://wallstreetcn.com/premium/articles/3780704?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T06:31:26+00:00",
    "summary": "2026年8月31日，国内首部全AI制作30集长剧《后西游记》登陆湖南卫视黄金档与芒果TV双平台，标志AI内容首次进入主流长内容播出体系，并成为广电\"21条\"后首部\"边制作、边审核、边播出\"的剧集。"
  },
  {
    "id": "wscn:3780805",
    "domain": "股票",
    "title": "1996年来首次！日本基准债券收益率突破3%关口",
    "url": "https://wallstreetcn.com/articles/3780805",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T06:28:34+00:00",
    "summary": "这背后三重驱动力叠加：美财长贝森特在G20期间罕见公开施压日本加息、市场对日本央行9月加息概率预期高达90%，以及全球债券抛售潮共振。尽管今天10年期国债拍卖需求稳健，但市场市场对后续走势的分歧并未消散，周四30年期日债拍卖若疲软，或触发全球连锁抛售。"
  },
  {
    "id": "wscn:3780783",
    "domain": "股票",
    "title": "全球债券抛售潮加剧，日债基准收益率升破3%，中东油轮遇袭推升油价、现货黄金跌破4400",
    "url": "https://wallstreetcn.com/articles/3780783",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T05:49:32+00:00",
    "summary": "美联储9月加息预期升至65%，日本10年期国债收益率30年来首触3%；澳大利亚10年期国债收益率跳涨至5.19%，为2011年7月以来最高。中东局势升温推动布伦特原油逼近92美元。亚太股市表现分化，MSCI亚太指数微涨0.3%，台股领涨，韩国综合股价指数下跌0.13%。东证指数涨0.5%，日经225指数跌0.4%。"
  },
  {
    "id": "wscn:3780639",
    "domain": "股票",
    "title": "不让黄金绑架泰铢：泰国央行限制黄金交易是否真见成效？",
    "url": "https://wallstreetcn.com/premium/articles/3780639?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T05:14:05+00:00",
    "summary": "泰国央行限制黄金交易、鼓励美元结算，但近期金价上涨使泰铢与金价相关性回升，政策效果有限，后续或更严。"
  },
  {
    "id": "wscn:3780804",
    "domain": "股票",
    "title": "小红书内测“发日常”，向“朋友圈”再迈一步？",
    "url": "https://wallstreetcn.com/articles/3780804",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T03:52:18+00:00",
    "summary": "三天后自动隐藏，可转为普通笔记。"
  },
  {
    "id": "wscn:3780801",
    "domain": "股票",
    "title": "美联储和财政部“双重挤压”，30年期美债收益率创2006年以来最长高位纪录",
    "url": "https://wallstreetcn.com/articles/3780801",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T03:41:57+00:00",
    "summary": "美国30年期国债收益率今年收盘破5%的天数已达55天，创2006年以来之最，8月更触及5.34%高点，逼近22年峰值。财政赤字积重难返、9月企业债发行潮汹涌、美联储鹰派加息概率升至70%，三重压力叠加之下，财政部扩大回购的救场之举被分析师直斥\"杯水车薪\"。"
  },
  {
    "id": "wscn:3780803",
    "domain": "股票",
    "title": "付鹏：摩天大楼的阻尼器原理——低波动率的表面之下，美股需要关注什么？【付鹏说2】",
    "url": "https://wallstreetcn.com/premium/articles/3780803?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T03:39:33+00:00",
    "summary": "当前AI资本支出这条正向主线已从确定性窗口转入不确定性窗口，结构上呈现的收敛三角形表明每一次分化之后的支撑力量都在减弱，第四次内部同向大概率正在临近，且更可能以冲击的形式出现。"
  },
  {
    "id": "wscn:3780802",
    "domain": "股票",
    "title": "AI芯片需求持续爆发，韩国8月出口同比激增近七成",
    "url": "https://wallstreetcn.com/articles/3780802",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T03:38:41+00:00",
    "summary": "韩国8月出口同比增长68.7%至982.5亿美元，连续第15个月增长。半导体出口激增209%至466.5亿美元，创历史新高，连续三个月突破400亿美元，主要受AI基础设施投资驱动。贸易顺差扩至347.5亿美元，连续三个月超300亿美元。但出口呈\"K形\"分化，汽车、船舶等非科技行业表现落后。"
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
    "id": "rss:https://arxiv.org/abs/2608.29025",
    "domain": "金融",
    "title": "Deep Hedging Under Realistic Market Frictions: A Regime-Conditional Empirical Study of Dynamic Option Hedging on Bitcoin Options",
    "url": "https://arxiv.org/abs/2608.29025",
    "source": "Sheryan Kumar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.29025v1 Announce Type: new Abstract: Classical option-hedging methods like Black-Scholes delta assume constant, free rebalancing, which real markets don't allow. Deep hedging trains a neura"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.29423",
    "domain": "金融",
    "title": "Improving Swaption Calibration in Factor HJM Stochastic Volatility Models: A First-Order Correction to Frozen Swap-Rate Loadings",
    "url": "https://arxiv.org/abs/2608.29423",
    "source": "Bram Brongers",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.29423v1 Announce Type: new Abstract: The factor HJM stochastic volatility model introduced by Sepp and Rakhmonov (2025) obtains tractable swaption pricing by freezing the nonlinear swap-rat"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.29468",
    "domain": "金融",
    "title": "The Convergence Rate of Stochastic Tracking with Application to Optimal Execution",
    "url": "https://arxiv.org/abs/2608.29468",
    "source": "Marcel Nutz, Moritz Voss",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.29468v1 Announce Type: new Abstract: We study the quadratic tracking problem of a general stochastic target process with absolutely continuous controls, with and without terminal constraint"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.29669",
    "domain": "金融",
    "title": "Wasserstein-Barycentric Interaction Fields for Spatial Factor Models: Evidence from Language-Model Representations",
    "url": "https://arxiv.org/abs/2608.29669",
    "source": "Marcus Gawronsky, Chun-Sung Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.29669v1 Announce Type: new Abstract: Spatial return models take the interaction matrix as given and leave feedback uninterpreted. We construct a bandwidth-free field from firms' language-mo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.29692",
    "domain": "金融",
    "title": "Portfolio Risk Bounds without Cross-Asset Return Covariances: Distributional Fields from Language-Model Representations",
    "url": "https://arxiv.org/abs/2608.29692",
    "source": "Marcus Gawronsky, Chun-Sung Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.29692v1 Announce Type: new Abstract: Portfolio risk assessment ordinarily relies on reliable estimates of cross-asset return covariances, which are difficult to obtain in short, high-dimens"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.29786",
    "domain": "金融",
    "title": "Recovering Posterior Beliefs in Credit Risk: A Latent-State EM Extension of the Information-Geometric Framework",
    "url": "https://arxiv.org/abs/2608.29786",
    "source": "Lorenzo Quirini",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.29786v1 Announce Type: new Abstract: This paper develops a latent-state framework for recovering borrower-level posterior beliefs in credit-risk analysis. Creditworthiness and financial fra"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.29843",
    "domain": "金融",
    "title": "The Price of Intelligence: A Quality-Adjusted Price Index for AI Services",
    "url": "https://arxiv.org/abs/2608.29843",
    "source": "Louis Yiven Zhu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.29843v1 Announce Type: new Abstract: Posted prices for AI inference have fallen steadily since 2024, yet the measured speed of that fall depends almost entirely on the method of measurement"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.30321",
    "domain": "金融",
    "title": "Optimal Block Time for AMM Liquidity Providers under Jump-Diffusion Prices",
    "url": "https://arxiv.org/abs/2608.30321",
    "source": "Nils Bundi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.30321v1 Announce Type: new Abstract: Loss-versus-Rebalancing (LVR) is the dominant adverse-selection cost borne by liquidity providers on automated market makers. Under geometric Brownian m"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.30446",
    "domain": "金融",
    "title": "End-to-End Neural Shrinkage of Indefinite Pairwise Correlation Matrices for Small-Cap-Inclusive Portfolios",
    "url": "https://arxiv.org/abs/2608.30446",
    "source": "Christian Bongiorno, Lorenzo Villassero",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.30446v1 Announce Type: new Abstract: Small-cap-inclusive equity universes contain recently listed and intermittently traded securities, so enforcing a common look-back discards a substantia"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.30490",
    "domain": "金融",
    "title": "Two Kinds of Nothing: What Insignificant Results in Finance Actually Show",
    "url": "https://arxiv.org/abs/2608.30490",
    "source": "David Tan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.30490v1 Announce Type: new Abstract: Claims of the form \"we find no evidence that X affects Y\" appear throughout the applied finance literature, yet whether such a claim contains evidence o"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.30519",
    "domain": "金融",
    "title": "Authority-Inference Separation in Agentic Finance: First-Line Control, Blockchain Enforcement, and Replayable Assurance",
    "url": "https://arxiv.org/abs/2608.30519",
    "source": "Hui Gong, Michail Samawi, Francesca Medda",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.30519v1 Announce Type: new Abstract: AI agents can select tools, counterparties, and transaction parameters, yet inference should not itself confer authority to execute a financial action. "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.30522",
    "domain": "金融",
    "title": "Tariff Threats, Macroeconomic Expectations, and Policy Communication Strategies: Experiments Based on a Multi-Agent System",
    "url": "https://arxiv.org/abs/2608.30522",
    "source": "Jianhao Lin, Lexuan Sun, Yixin Yan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.30522v1 Announce Type: new Abstract: Tariff threats can move household beliefs before policy is enacted, yet their rapidly changing language is difficult to study with conventional surveys."
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.30558",
    "domain": "金融",
    "title": "A note on markets with semi-static trading strategies",
    "url": "https://arxiv.org/abs/2608.30558",
    "source": "Mikl\\'os R\\'asonyi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.30558v1 Announce Type: new Abstract: We investigate arbitrage in a discrete-time financial market model where, in addition to finitely many dynamically traded assets, there are also static "
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.30749",
    "domain": "金融",
    "title": "Importance Sampling Enhanced with the COS Method for the Portfolio Risk Allocation",
    "url": "https://arxiv.org/abs/2608.30749",
    "source": "Fang Fang, Xiaoyu Shen, Qinling Wang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.30749v1 Announce Type: new Abstract: We introduce ISCOS, a cross-entropy importance-sampling calibration method for rare credit-portfolio losses. We derive Gaussian and Gaussian--inverse-Ga"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.30867",
    "domain": "金融",
    "title": "Neural Calibration of a Complete Market Model",
    "url": "https://arxiv.org/abs/2608.30867",
    "source": "Andrea Molent, Michel Vellekoop",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.30867v1 Announce Type: new Abstract: We propose a neural calibration method to construct a recombining binomial tree directly from a set of given option prices. Rather than estimating a con"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.30999",
    "domain": "金融",
    "title": "Metaorder modelling and identification from public data",
    "url": "https://arxiv.org/abs/2608.30999",
    "source": "Ezra Goliath, Tim Gebbie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.30999v1 Announce Type: new Abstract: Market-order flow in financial markets exhibits long-range correlations. This is a widely known stylised fact of financial markets. A popular hypothesis"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.31041",
    "domain": "金融",
    "title": "Agentic Quantitative Trading: A Survey of Workflows, Systems, and Evaluation",
    "url": "https://arxiv.org/abs/2608.31041",
    "source": "Fengrui Hua, Hengyi Yang, Xinlei Hao, Haohan Zhang, Bokai Cao, Yiyan Qi, Jia Li, Jian Guo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.31041v1 Announce Type: new Abstract: Quantitative trading is moving from isolated predictive models toward agentic workflows that combine reasoning, tool use, memory, and feedback. This sur"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.29473",
    "domain": "金融",
    "title": "Stochastic Optimal Control of Hawkes Jump-Diffusion Systems",
    "url": "https://arxiv.org/abs/2608.29473",
    "source": "Daria Sakhanda, Joshu\\'e Hel\\'i Ricalde-Guerrero",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.29473v1 Announce Type: cross Abstract: This paper is devoted to developing a framework for stochastic growth models with environmental risk, in which rare but catastrophic shocks interact w"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.29818",
    "domain": "金融",
    "title": "Decarbonising price formation: unit-level evidence on battery storage and the imbalance price in the GB Balancing Mechanism",
    "url": "https://arxiv.org/abs/2608.29818",
    "source": "Robert Dalton, Aidan O'Sullivan",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.29818v1 Announce Type: cross Abstract: Renewables now dominate Great Britain's generation mix but rarely occupy the marginal price-setting position, which raises the question of which flexi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2405.11392",
    "domain": "金融",
    "title": "Deep Penalty Methods: A Class of Deep Learning Algorithms for Solving High Dimensional Optimal Stopping Problems",
    "url": "https://arxiv.org/abs/2405.11392",
    "source": "Yunfei Peng, Pengyu Wei, Wei Wei, Xiaole Xue",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2405.11392v3 Announce Type: replace Abstract: We propose a deep learning algorithm for high dimensional optimal stopping problems. Our method is inspired by the penalty method for solving free b"
  },
  {
    "id": "rss:https://arxiv.org/abs/2410.23447",
    "domain": "金融",
    "title": "Systematic Covariance Envelopes from Wasserstein Geometry: Evidence from Language-Model Representations",
    "url": "https://arxiv.org/abs/2410.23447",
    "source": "Marcus Gawronsky, Chun-Sung Huang",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2410.23447v2 Announce Type: replace Abstract: Firm characteristics are commonly represented as fixed vectors, even though evidence about firms' operations arrives as heterogeneous collections of"
  },
  {
    "id": "rss:https://arxiv.org/abs/2603.10807",
    "domain": "金融",
    "title": "Risk-Adjusted Harm Scoring for Automated Red Teaming for LLMs in Financial Services",
    "url": "https://arxiv.org/abs/2603.10807",
    "source": "Fabrizio Dimino, Bhaskarjit Sarmah, Stefano Pasquali",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2603.10807v2 Announce Type: replace Abstract: Existing LLM safety evaluations rely on binary attack-success rates and domain-agnostic taxonomies, leaving regulated Banking, Financial Services, a"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.22230",
    "domain": "金融",
    "title": "Performance Manipulation: Labor Market Implications in AI-assisted Era",
    "url": "https://arxiv.org/abs/2604.22230",
    "source": "Xiaoyun Qiu, Yang Yu, Haifeng Xu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2604.22230v2 Announce Type: replace Abstract: Performance manipulation arises when agents exploit easily measurable, routine tasks to inflate observable outcomes without contributing genuine inn"
  },
  {
    "id": "rss:https://arxiv.org/abs/2604.27700",
    "domain": "金融",
    "title": "Data-Driven Stochastic Optimal Control for Intraday Electricity Trading by Renewable Producers",
    "url": "https://arxiv.org/abs/2604.27700",
    "source": "Chiheb Ben Hammouda, Michael Samet, Raul Tempone",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2604.27700v2 Announce Type: replace Abstract: The rapid growth of weather-dependent renewable generation increases price volatility and imbalance penalty risk in power markets, creating the need"
  },
  {
    "id": "rss:https://arxiv.org/abs/2605.11180",
    "domain": "金融",
    "title": "The Value of Information: A Puzzle",
    "url": "https://arxiv.org/abs/2605.11180",
    "source": "Ohad Kadan, Asaf Manela",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2605.11180v2 Announce Type: replace Abstract: We show that the total value of information to informed traders can be measured by the covariation between price changes and order flow. This covari"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.13844",
    "domain": "金融",
    "title": "The Value of Peer Review and the Reward to Reputation",
    "url": "https://arxiv.org/abs/2607.13844",
    "source": "Johan Fourie",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2607.13844v3 Announce Type: replace Abstract: Journals cannot referee every paper they receive. When submissions outrun the time reviewers can give, an editor must decide what to do with the pap"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.03703",
    "domain": "金融",
    "title": "Preying on Leveraged ETFs",
    "url": "https://arxiv.org/abs/2608.03703",
    "source": "Yinhong Zhao",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.03703v4 Announce Type: replace Abstract: We argue that speculators preying on the closing rebalances of leveraged exchange-traded funds (LETFs) contributed to the Korean market's extreme vo"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.15667",
    "domain": "金融",
    "title": "Scalable Pontryagin-Guided Adjoint-to-Control Recovery for Constrained Dynamic Portfolio Choice",
    "url": "https://arxiv.org/abs/2608.15667",
    "source": "Jaegi Jeon, Jeonggyu Huh, Hyeng Keun Koo, Byung Hwa Lim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.15667v3 Announce Type: replace Abstract: We study continuous-time multi-asset portfolio choice and consumption under smooth pointwise constraints, including state-dependent feasible sets. T"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.24894",
    "domain": "金融",
    "title": "Forecasting Weather-Driven Price Dynamics Across Sri Lankan Tea Market Catalogues",
    "url": "https://arxiv.org/abs/2608.24894",
    "source": "Hesandi Mallawarachchi, Senilka Madurapperumage, Nadil Kulathunge, Thilokya Angeesa, Nethsith Gunaweera, Sandeepa Weerasekara, Patalee Narasinghe, Nisansa de Silva, Sandareka Wickramanayake",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.24894v2 Announce Type: replace Abstract: The Colombo Tea Auction (CTA) plays a vital role in determining global tea prices, yet the relationship between local weather conditions and price b"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.26473",
    "domain": "金融",
    "title": "DTD-VAE: Disentangled Temporal Dependencies VAE for Credit Risk Prediction",
    "url": "https://arxiv.org/abs/2608.26473",
    "source": "Xiaobo Guo, Lu-an Dong, Yanbo Wang, Peng Zhang, Cai Zhi, Youru Li",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-01T04:00:00+00:00",
    "summary": "arXiv:2608.26473v2 Announce Type: replace Abstract: Evaluating customer creditworthiness is crucial for retail banking operations, as it impacts marketing strategies, customer relationship management,"
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
