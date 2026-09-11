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

- 今日日期：`2026-09-11`
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
  "date": "2026-09-11",
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
    "points": 4504739,
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
    "points": 1894183,
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
    "points": 1846796,
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
    "points": 1354509,
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
    "points": 1307742,
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
    "points": 1273647,
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
    "points": 1195897,
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
    "points": 1082615,
    "published_at": "2026-05-11T09:02:15+00:00",
    "summary": "文档链接：https://lcnaoyjp4e3z.feishu.cn/wiki/MtJlwX0B5iy6y9k5GZTcdjSknTd"
  },
  {
    "id": "bvid:BV1yorUYWEGD",
    "domain": "AI",
    "title": "普通人也可以看的 AI 编程指南 | Cursor 教程｜Cursor 使用技巧和思路｜如何免费使用 Cursor｜AI 编程",
    "url": "http://www.bilibili.com/video/av113786467981446",
    "source": "不正经的前端啊",
    "platform": "bilibili",
    "points": 944999,
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
    "points": 884270,
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
    "points": 795494,
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
    "points": 745964,
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
    "points": 673312,
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
    "points": 670771,
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
    "points": 588186,
    "published_at": "2025-06-17T02:00:54+00:00",
    "summary": "【配套资料】关注公众号：尚硅谷教育，回复“大模型”免费获取\n【课程简介】从Cursor下载安装、账号配置（含 “无限续杯” 技巧）到三大核心功能拆解：智能Tab、指令交互 Chat、Ctrl+K 智能内联修改"
  },
  {
    "id": "bvid:BV1RSFUzVEAG",
    "domain": "AI",
    "title": "【吴恩达】2026年公认最好的【Claude Code】教程！大模型入门到进阶，一套全解决！Claude Code探索-测试-重构-调试代码库—附带课件代码",
    "url": "http://www.bilibili.com/video/av116045469783373",
    "source": "吴恩达的AI课",
    "platform": "bilibili",
    "points": 579762,
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
    "points": 442246,
    "published_at": "2026-07-08T03:10:00+00:00",
    "summary": "安装包+全部配套课程源码+学习资料\n\n领取方式：关注 + 私信【让我看看】！"
  },
  {
    "id": "bvid:BV1uronYREWR",
    "domain": "AI",
    "title": "MCP终极指南 - 从原理到实战，带你深入掌握MCP（基础篇）",
    "url": "http://www.bilibili.com/video/av114339210073708",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 286160,
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
    "points": 282303,
    "published_at": "2026-02-19T07:34:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1VC7g6vE9f",
    "domain": "AI",
    "title": "Vibe Coding是什么？从AI模型、Agent到工作流，彻底搞懂AI编程工具",
    "url": "http://www.bilibili.com/video/av116796937997854",
    "source": "隔壁的程序员老王",
    "platform": "bilibili",
    "points": 276692,
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
    "points": 258876,
    "published_at": "2026-05-05T10:13:18+00:00",
    "summary": "🤔如果你最近也在想一件事：我一个完全不会代码的人，真的可以用 AI 为自己做出一个软件吗？\n🌟我的答案是：当然可以！\n\n📚我把自己这4个月Vibe Coding里最重要的经验，浓缩成了一次完整实操演示。\n不是只告诉你装什么工具，而是直接带你从0到1做出一个真正能运行的软件：怎么提第一次需求，怎么让AI稳定执行，怎么一步一步把项目推进下去。\n\n如果你刚开始对Vibe Coding感兴趣，那这条就是为"
  },
  {
    "id": "bvid:BV1YwYx6CENG",
    "domain": "AI",
    "title": "【离 大 谱！】有人用Codex / Claude Code 拿国奖了！数学建模再也不用爆肝了",
    "url": "http://www.bilibili.com/video/av117240594831013",
    "source": "大师兄的知识库",
    "platform": "bilibili",
    "points": 258650,
    "published_at": "2026-09-09T10:30:20+00:00",
    "summary": "【离 大 谱！】有人用Codex / Claude Code 拿国奖了！数学建模再也不用爆肝了"
  },
  {
    "id": "bvid:BV1ZEJA6xEds",
    "domain": "AI",
    "title": "最新方法！国内免费无限制，使用Claude Code！",
    "url": "http://www.bilibili.com/video/av116746874848391",
    "source": "我是阿众",
    "platform": "bilibili",
    "points": 239759,
    "published_at": "2026-06-15T04:00:00+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1e3t4etExj",
    "domain": "AI",
    "title": "手摸手的AI编程cursor实战【小白教程】",
    "url": "http://www.bilibili.com/video/av113148447169565",
    "source": "秋芝2046",
    "platform": "bilibili",
    "points": 236117,
    "published_at": "2024-09-17T01:00:00+00:00",
    "summary": "喜欢的朋友可以三连+关注～这对我真的很重要"
  },
  {
    "id": "bvid:BV1E6CFBMEnk",
    "domain": "AI",
    "title": "【2025最新版】目前B站最全最细的 CurSor AI编程零基础全套教程，手把手教你搭建高效Cursor工作流，全程干货无废话！cursor教程｜AI 编程",
    "url": "http://www.bilibili.com/video/av115524067463218",
    "source": "诸葛老师本人",
    "platform": "bilibili",
    "points": 194711,
    "published_at": "2025-11-10T06:52:42+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\n‍视频配套笔记、AI大模型笔记代码：https://www.bilibili.com/read/cv43354937/?jump_opus=1"
  },
  {
    "id": "bvid:BV1JBorBoEXh",
    "domain": "AI",
    "title": "Claude Code保姆级全套教程（软件+文档），从入门到精通，搞定所有开发场景，零基础十分钟上手，全程干货无废话！",
    "url": "http://www.bilibili.com/video/av116475771755099",
    "source": "舔砖加瓦编程小马",
    "platform": "bilibili",
    "points": 190663,
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
    "points": 181051,
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
    "points": 169464,
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
    "points": 161978,
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
    "points": 155817,
    "published_at": "2025-06-05T12:44:31+00:00",
    "summary": "UV安装：https://docs.astral.sh/uv/getting-started/installation/\nMCP Github首页：https://github.com/modelcontextprotocol\nMCP Python SKD: https://github.com/modelcontextprotocol/python-sdk\n免费云服务器：https://www."
  },
  {
    "id": "bvid:BV154426xEha",
    "domain": "AI",
    "title": "我的 AI 编程全流程：如何使用 AI 稳定交付一个高质量的产品",
    "url": "http://www.bilibili.com/video/av117178586240848",
    "source": "马克的技术工作坊",
    "platform": "bilibili",
    "points": 154333,
    "published_at": "2026-08-29T11:38:24+00:00",
    "summary": ""
  },
  {
    "id": "bvid:BV1oG3w6wEZB",
    "domain": "AI",
    "title": "【Codex入门】10分钟速通Codex搞定Vibe Coding!",
    "url": "http://www.bilibili.com/video/av116992023462138",
    "source": "学姐潇潇",
    "platform": "bilibili",
    "points": 113340,
    "published_at": "2026-07-27T12:55:18+00:00",
    "summary": "因为我在刚开始的阶段，碰到了很多并不是零基础的教程，所以有了这期视频~"
  },
  {
    "id": "bvid:BV1XnuGzfEp7",
    "domain": "AI",
    "title": "让你手中的AI好用10倍！5个好玩实用的MCP推荐，让你不只会用AI搜索",
    "url": "http://www.bilibili.com/video/av114835262018810",
    "source": "田同学Tino",
    "platform": "bilibili",
    "points": 74499,
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
    "points": 73666,
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
    "points": 70999,
    "published_at": "2026-03-23T10:18:18+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\n视频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
  },
  {
    "id": "bvid:BV16LXjYHETR",
    "domain": "AI",
    "title": "🔥【Cursor保姆级教程】新手必问10大问题❗️手把手教你快速入门💻",
    "url": "http://www.bilibili.com/video/av114182812863204",
    "source": "AI随风随风",
    "platform": "bilibili",
    "points": 65458,
    "published_at": "2025-03-18T09:55:27+00:00",
    "summary": "Cursor新手必问10大问题：\n一、免费和收费的区别是什么？\n二、只用cursor就能开发了吗？\n三、如何汉化以及插件的使用？\n四、怎么配置Rules？\n五、如何解决程序错误？\n六、claude -3.7- sonet 以及 claude -3.7- sonet-thinking 如何选择？\n七、Ask、Edit、Agent 三种模式的区别？\n八、如何进行代码回滚？\n九、cursor 降智了怎么"
  },
  {
    "id": "bvid:BV19wXvBpEaL",
    "domain": "AI",
    "title": "认真用 Claude Code 的人，迟早会遇见 Everything Claude Code",
    "url": "http://www.bilibili.com/video/av116319122885806",
    "source": "极客魔导师",
    "platform": "bilibili",
    "points": 63785,
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
    "points": 55000,
    "published_at": "2025-05-06T15:38:52+00:00",
    "summary": "今天聊聊MCP"
  },
  {
    "id": "bvid:BV1Yn336mEPi",
    "domain": "AI",
    "title": "operitAI教程：入门安卓最强大ai平台",
    "url": "http://www.bilibili.com/video/av116981789364416",
    "source": "玩家77625",
    "platform": "bilibili",
    "points": 42730,
    "published_at": "2026-07-25T22:19:42+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1hxMbzqEzU",
    "domain": "AI",
    "title": "小智MCP自由了！我开源了个命令行神器实现多MCP聚合",
    "url": "http://www.bilibili.com/video/av114686414625640",
    "source": "闪电蘑菇",
    "platform": "bilibili",
    "points": 41608,
    "published_at": "2025-06-15T08:31:55+00:00",
    "summary": "- 我写的小智客户端命令行工具\n - github: https://github.com/shenjingnan/xiaozhi-client\n - gitee: https://gitee.com/shenjingnan/xiaozhi-client\n\n- 小智官方MCP示例代码仓库：\n - github: https://github.com/78/mcp-calculator\n - git"
  },
  {
    "id": "bvid:BV1VL3F6pE9K",
    "domain": "AI",
    "title": "0基础入门智能体agent测试：AI测试基础+AI智能体(Agent)测试从零入门全攻略，2026最新版！",
    "url": "http://www.bilibili.com/video/av116991151113881",
    "source": "黑马测试",
    "platform": "bilibili",
    "points": 41340,
    "published_at": "2026-07-27T09:19:37+00:00",
    "summary": "还在卷传统软件测试？2026年必学的AI智能体(Agent)测试来了！本期视频专为0基础小白打造，从软件测试基础讲起...若要本视频配套资源笔记可加up主企微（请看置顶留言最后一句话）。"
  },
  {
    "id": "bvid:BV1LXhc6yEkc",
    "domain": "AI",
    "title": "昔涟/Cyrene-Agent 安装配置/演示教程",
    "url": "http://www.bilibili.com/video/av117164694570292",
    "source": "Playa0",
    "platform": "bilibili",
    "points": 36707,
    "published_at": "2026-08-27T00:43:58+00:00",
    "summary": "v1.1.6安装包：\n夸克网盘：\n链接：https://pan.quark.cn/s/43ff3db459f4?pwd=SD2k\n提取码：SD2k\ngithub仓库：\nPlaya-0v0/Cyrene-Agent: An open-source AI desktop companion inspired by Cyrene, combining immersive Chat, personaliz"
  },
  {
    "id": "bvid:BV1zXAuzUEWt",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的 Cursor+Skills实战指南教程，手把手带你开发爆款app，全程干货无废话！Agent Skills教程｜AI 编程",
    "url": "http://www.bilibili.com/video/av116272180238922",
    "source": "诸葛老师本人",
    "platform": "bilibili",
    "points": 36109,
    "published_at": "2026-03-22T09:52:46+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\n‍视频配套笔记、AI大模型笔记代码：https://www.bilibili.com/read/cv43354937/?jump_opus=1"
  },
  {
    "id": "bvid:BV1HaVh6fEhn",
    "domain": "AI",
    "title": "AI编程进阶必修课！Claude Code+Harness AI 工程化实战！电商项目全流程落地，规范开发、代码治理、简历加分一站式吃透",
    "url": "http://www.bilibili.com/video/av116656764421367",
    "source": "图灵程序员诸葛",
    "platform": "bilibili",
    "points": 35102,
    "published_at": "2026-05-29T08:01:23+00:00",
    "summary": "大模型资料看这里聆取https://www.bilibili.com/read/cv49754608/?jump_opus=1"
  },
  {
    "id": "bvid:BV1raQXYpEsz",
    "domain": "AI",
    "title": "Cursor免费无限使用教程,几分钟省下一百多块",
    "url": "http://www.bilibili.com/video/av114167931477037",
    "source": "自由程序员八哥",
    "platform": "bilibili",
    "points": 34418,
    "published_at": "2025-03-15T18:49:37+00:00",
    "summary": "Cursor免费无限使用教程\n新链接链接：夸克网盘：链接：https://pan.quark.cn/s/6d825a22413a"
  },
  {
    "id": "bvid:BV1uyLjzHEMS",
    "domain": "AI",
    "title": "VSCode原生支持MCP了！几千个MCP工具，这下可有得玩了",
    "url": "http://www.bilibili.com/video/av114395598293799",
    "source": "神秘的鱼仔",
    "platform": "bilibili",
    "points": 34287,
    "published_at": "2025-04-24T23:46:15+00:00",
    "summary": "VSCode最新版已经原生支持MCP！本期视频通过一个实际例子教会大家如何通过VSCode实现MCP的调用"
  },
  {
    "id": "bvid:BV1LWTe6gEVc",
    "domain": "AI",
    "title": "Claude code帮我实现综述论文自由！",
    "url": "http://www.bilibili.com/video/av116842504918580",
    "source": "做科研的大师兄",
    "platform": "bilibili",
    "points": 34173,
    "published_at": "2026-07-01T03:07:40+00:00",
    "summary": "-"
  },
  {
    "id": "bvid:BV1JcDSBYE4V",
    "domain": "AI",
    "title": "新版 Cursor 看不到代码了？5 分钟学会新界面所有操作",
    "url": "http://www.bilibili.com/video/av116390174393526",
    "source": "未生AI",
    "platform": "bilibili",
    "points": 31317,
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
    "points": 30555,
    "published_at": "2025-05-16T13:11:38+00:00",
    "summary": "完全本地，本地 MCP、本地大语言模型。使用 FastMCP 开发 MCP 服务器、客户端，并使用大语言模型调用 MCP 服务器工具。\n代码：https://github.com/IronSpiderMan/MachineLearningPractice/tree/main/llm_techs/mcp"
  },
  {
    "id": "bvid:BV1RUDsBWEHb",
    "domain": "AI",
    "title": "【2026最新版】目前B站最全最细的Cursor+Skills实战指南教程，手把手带你开发爆款app，全程干货无废话！比付费效果强十倍！",
    "url": "http://www.bilibili.com/video/av116373464350785",
    "source": "AI大模型技术教程",
    "platform": "bilibili",
    "points": 28615,
    "published_at": "2026-04-09T10:15:00+00:00",
    "summary": "制作不易，麻烦各位观众老爷一键三连呀【点赞、投币、收藏】感谢支持～\nCursor+Skills频配套文档课件笔记代码及AI大模型学习路线图戳这里获取→https://www.bilibili.com/read/cv41777105/?jump_opus=1"
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
    "id": "rss:https://www.eetimes.com/leds-push-wireless-power-further/",
    "domain": "AI 算力 / 半导体",
    "title": "LEDs Push Wireless Power Further",
    "url": "https://www.eetimes.com/leds-push-wireless-power-further/",
    "source": "Rebecca Pool",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T20:00:00+00:00",
    "summary": "An LED alternative to laser wireless power transfer from the Institute of Science Tokyo uses adaptive optics and AI beam steering to charge indoor IoT devices 5 meters away. The post LEDs Push Wireles"
  },
  {
    "id": "rss:https://www.eetimes.com/the-hardware-assisted-verification-imperative/",
    "domain": "AI 算力 / 半导体",
    "title": "The Hardware-assisted Verification Imperative",
    "url": "https://www.eetimes.com/the-hardware-assisted-verification-imperative/",
    "source": "Juergen Jaeger, Siemens EDA",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T12:00:00+00:00",
    "summary": "Read why today’s IC system projects for applications like AI and superscalar acceleration require the most comprehensive HAV solutions and methodologies. The post The Hardware-assisted Verification Im"
  },
  {
    "id": "rss:https://www.eetimes.com/biwin-brings-storage-solutions-for-ai-era-at-embedded-world-na-2026/",
    "domain": "AI 算力 / 半导体",
    "title": "BIWIN Brings Storage Solutions for AI Era at embedded world NA 2026",
    "url": "https://www.eetimes.com/biwin-brings-storage-solutions-for-ai-era-at-embedded-world-na-2026/",
    "source": "BIWIN STORAGE TECHNOLOGY CO., LTD.",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T12:00:00+00:00",
    "summary": "Visit BIWIN at Booth #6104 during embedded world NA 2026 to explore eSSDs, embedded memory, and industrial storage built for cloud and edge applications. The post BIWIN Brings Storage Solutions for AI"
  },
  {
    "id": "rss:https://www.eetimes.com/bridging-the-hpc-software-gap-for-practical-quantum-computing/",
    "domain": "AI 算力 / 半导体",
    "title": "Bridging the HPC Software Gap for Practical Quantum Computing",
    "url": "https://www.eetimes.com/bridging-the-hpc-software-gap-for-practical-quantum-computing/",
    "source": "Pablo Valerio",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T12:00:00+00:00",
    "summary": "HPC centers must address the infrastructure bottleneck to integrate quantum systems and unlock their full potential. The post Bridging the HPC Software Gap for Practical Quantum Computing appeared fir"
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
    "id": "rss:https://www.tomshardware.com/tech-industry/cryptocurrency/minecraft-spawned-crypto-kingpin-faces-20-years-for-usd245-million-heist-masterminds-role-in-hacking-campaign-fueled-their-supercar-bodyguards-and-private-jet-habit",
    "domain": "AI 算力 / 半导体",
    "title": "Minecraft-spawned crypto kingpin faces 20 years for $245 million heist — mastermind's role in hacking campaign fueled their supercar, bodyguards, and private jet habit",
    "url": "https://www.tomshardware.com/tech-industry/cryptocurrency/minecraft-spawned-crypto-kingpin-faces-20-years-for-usd245-million-heist-masterminds-role-in-hacking-campaign-fueled-their-supercar-bodyguards-and-private-jet-habit",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T14:25:28+00:00",
    "summary": "The ringleader of a cybercrime gang, which reportedly formed after meetups in Minecraft online, has plead guilty to a racketeering charge and now faces up to 20 years in jail."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-rogue-ai-agents-accessed-more-websites-to-communicate-than-originally-believed-defiant-llms-accessed-old-wikis-and-abandoned-websites-to-co-ordinate-in-a-bid-to-dupe-assessors",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI's rogue AI agents accessed more websites to communicate than originally believed — defiant LLMs accessed old wikis and abandoned websites to co-ordinate in a bid to dupe assessors",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-rogue-ai-agents-accessed-more-websites-to-communicate-than-originally-believed-defiant-llms-accessed-old-wikis-and-abandoned-websites-to-co-ordinate-in-a-bid-to-dupe-assessors",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T13:20:00+00:00",
    "summary": "Rogue OpenAI agents used dozens of website to exchange information, new investigations have found. However, the real impact is yet to be determined."
  },
  {
    "id": "rss:https://www.tomshardware.com/peripherals/gaming-chairs/libernovo-omni-pro-review",
    "domain": "AI 算力 / 半导体",
    "title": "Libernovo Omni Pro Review: Cooler than you think",
    "url": "https://www.tomshardware.com/peripherals/gaming-chairs/libernovo-omni-pro-review",
    "source": "Sarah Jacobsson Purewal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T13:06:32+00:00",
    "summary": "Libernovo's Omni Pro is a dynamic, ergonomic gaming chair with motorized lumbar support and a ventilation fan that works surprisingly well."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/old-macbook-uses-a-mirror-webcam-and-ai-agent-to-code-its-own-amd-gpu-drivers-agent-first-omarchy-linux-debugs-itself-ai-can-check-its-own-progress-on-screen-in-real-time",
    "domain": "AI 算力 / 半导体",
    "title": "Old MacBook uses a mirror, webcam, and AI agent to code its own AMD GPU drivers — 'agent-first' Omarchy Linux debugs itself, AI can check its own progress on screen in real-time",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/old-macbook-uses-a-mirror-webcam-and-ai-agent-to-code-its-own-amd-gpu-drivers-agent-first-omarchy-linux-debugs-itself-ai-can-check-its-own-progress-on-screen-in-real-time",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T13:00:00+00:00",
    "summary": "Using an 'age of agents' Linux distro a 'MacBook is using its webcam to look at its screen in a mirror to improve AMD Radeon chip support.'"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-ai-accelerator-supplier-biren-posts-2-000-percent-year-over-year-revenue-growth-export-controls-benefit-homegrown-chips-as-nvidia-and-amd-exit-market",
    "domain": "AI 算力 / 半导体",
    "title": "China's AI accelerator supplier Biren posts 2,000% year-over-year revenue growth — US export controls benefit homegrown chips as Nvidia and AMD exit market",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-ai-accelerator-supplier-biren-posts-2-000-percent-year-over-year-revenue-growth-export-controls-benefit-homegrown-chips-as-nvidia-and-amd-exit-market",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T12:40:00+00:00",
    "summary": "Biren Technology shows unprecedented shipments growth in 1H 2026 as competition from AMD and Nvidia vanishes (at least officially)."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/chinese-quartz-approved-for-semiconductor-equipment-and-dram-manufacturing-but-it-still-cant-break-americas-monopoly-china-secures-domestic-supply-for-chipmaking-components-but-spruce-pine-still-holds-the-crucible-monopoly",
    "domain": "AI 算力 / 半导体",
    "title": "Chinese quartz approved for semiconductor equipment and DRAM manufacturing, but it still can't break America's monopoly — China secures domestic supply for chipmaking components, but Spruce Pine still",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/chinese-quartz-approved-for-semiconductor-equipment-and-dram-manufacturing-but-it-still-cant-break-americas-monopoly-china-secures-domestic-supply-for-chipmaking-components-but-spruce-pine-still-holds-the-crucible-monopoly",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T12:20:00+00:00",
    "summary": "Pacific Quartz gets its high-purity quartz qualified for semiconductor equipment and DRAM manufacturing."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/the-state-of-abf-substrates-in-data-center-silicon-in-2026-solving-the-supply-crunch-and-material-wall-beneath-every-ai-accelerator",
    "domain": "AI 算力 / 半导体",
    "title": "The state of ABF substrates in data center silicon in 2026 — solving the supply crunch and material wall beneath every AI accelerator",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/the-state-of-abf-substrates-in-data-center-silicon-in-2026-solving-the-supply-crunch-and-material-wall-beneath-every-ai-accelerator",
    "source": "Etiido Uko",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T12:00:00+00:00",
    "summary": "ABF substrates underpin today’s most advanced AI chips, but soaring demand and expanding accelerator packages are creating new supply and technical bottlenecks that the industry is currently racing to"
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/gpus/modded-rtx-5090-ditches-16-pin-power-for-triple-8-pin-connectors-draws-up-to-900w-and-hits-3-400-mhz",
    "domain": "AI 算力 / 半导体",
    "title": "Modded RTX 5090 ditches 16-pin power for triple 8-pin connectors — draws up to 900W and hits 3,400 MHz",
    "url": "https://www.tomshardware.com/pc-components/gpus/modded-rtx-5090-ditches-16-pin-power-for-triple-8-pin-connectors-draws-up-to-900w-and-hits-3-400-mhz",
    "source": "Kunal Khullar",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T11:40:00+00:00",
    "summary": "TecLab’s experiment puts the humble 8-pin connector to an extreme test, with the modified RTX 5090 pulling more than 120A while avoiding the newer 12V-2x6 design altogether."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/semiconductors/tsmc-samsung-and-intel-shore-up-support-with-asml-to-deploy-larger-high-na-euv-photomasks-6-12-inch-photomask-transition-may-take-years-despite-unified-effort",
    "domain": "AI 算力 / 半导体",
    "title": "TSMC, Samsung, and Intel shore up support with ASML to deploy larger High-NA EUV photomasks — 6×12-inch photomask transition may take years despite unified effort",
    "url": "https://www.tomshardware.com/tech-industry/semiconductors/tsmc-samsung-and-intel-shore-up-support-with-asml-to-deploy-larger-high-na-euv-photomasks-6-12-inch-photomask-transition-may-take-years-despite-unified-effort",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T11:20:00+00:00",
    "summary": "ASML, Intel, Samsung, and TSMC back development of 6×12-inch to build large processors using High-NA EUV lithography systems without stitching."
  },
  {
    "id": "rss:https://www.tomshardware.com/software/windows/developer-uses-claude-to-vibe-code-a-windows-3-1-shell-in-an-hour-reanimated-12mb-retro-launcher-runs-on-both-windows-11-and-apple-silicon",
    "domain": "AI 算力 / 半导体",
    "title": "Developer uses Claude to vibe code a Windows 3.1 shell in an hour — reanimated 12MB retro launcher runs on both Windows 11 and Apple Silicon",
    "url": "https://www.tomshardware.com/software/windows/developer-uses-claude-to-vibe-code-a-windows-3-1-shell-in-an-hour-reanimated-12mb-retro-launcher-runs-on-both-windows-11-and-apple-silicon",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T11:00:00+00:00",
    "summary": "There’s a new vibe-coded clone of the Windows 3.1 Program Manager that runs on modern Windows 11 or macOS systems."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/gaming-laptops/save-usd250-on-this-1080p-ready-gaming-laptop-with-an-rtx-5060-now-just-usd1049-msi-cyborg-15-rig-ships-with-a-15-6-inch-144hz-display-16gb-ddr5-ram-and-an-eight-core-intel-cpu",
    "domain": "AI 算力 / 半导体",
    "title": "Save $250 on this 1080p-ready gaming laptop with an RTX 5060, now just $1049 — MSI Cyborg 15 rig ships with a 15.6-inch 144Hz display, 16GB DDR5 RAM, and an eight-core Intel CPU",
    "url": "https://www.tomshardware.com/laptops/gaming-laptops/save-usd250-on-this-1080p-ready-gaming-laptop-with-an-rtx-5060-now-just-usd1049-msi-cyborg-15-rig-ships-with-a-15-6-inch-144hz-display-16gb-ddr5-ram-and-an-eight-core-intel-cpu",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T10:53:35+00:00",
    "summary": "This MSI gaming laptop is fit for 1080p gaming, thanks to an RTX 5060, with $250 off knocking the price down to just $1049.99."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/steam-enforces-australian-age-verification-via-credit-cards-debit-card-glitches-and-low-credit-adoption-alienate-core-gamers-privacy-first-mindset-leads-to-dearth-of-options-that-may-hinder-consumers",
    "domain": "AI 算力 / 半导体",
    "title": "Steam enforces Australian age verification via credit cards — debit card glitches and low credit adoption alienate core gamers, privacy-first mindset leads to dearth of options that may hinder consume",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/steam-enforces-australian-age-verification-via-credit-cards-debit-card-glitches-and-low-credit-adoption-alienate-core-gamers-privacy-first-mindset-leads-to-dearth-of-options-that-may-hinder-consumers",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T10:30:00+00:00",
    "summary": "Valve starts enforcing Australian age verification law, but its privacy-minded choice of bank card as the only verification method is causing issues with many consumers."
  },
  {
    "id": "rss:https://www.tomshardware.com/desktops/pc-building/self-taught-electronics-tinkerer-builds-cold-war-era-vacuum-tube-computer-8-bit-design-uses-460-recycled-6n3p-vacuum-tubes-manufactured-in-the-1950s",
    "domain": "AI 算力 / 半导体",
    "title": "Self-taught tinkerer demos working room-sized Cold War-era supercomputer with vacuum tubes — takes 15 minutes to warm up and smells like burning dust, 8-bit design uses 460 recycled 1950s Soviet tubes",
    "url": "https://www.tomshardware.com/desktops/pc-building/self-taught-electronics-tinkerer-builds-cold-war-era-vacuum-tube-computer-8-bit-design-uses-460-recycled-6n3p-vacuum-tubes-manufactured-in-the-1950s",
    "source": "Mark Tyson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T10:00:00+00:00",
    "summary": "A self-taught electronics tinkerer called Mike recently shared details of his retro-computing vacuum tube computer project."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/apple-a20-pro-powers-iphone-18-pro-the-companys-first-2-nanometer-smartphone-chip",
    "domain": "AI 算力 / 半导体",
    "title": "Apple A20 Pro powers iPhone Duo, 18 Pro — the company's first 2-nanometer smartphone chip",
    "url": "https://www.tomshardware.com/pc-components/cpus/apple-a20-pro-powers-iphone-18-pro-the-companys-first-2-nanometer-smartphone-chip",
    "source": "Andrew E. Freedman",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T17:33:21+00:00",
    "summary": "Apple's new A20 Pro SOC will power the iPhone 18 Pro and iPhone Duo as its first 2 nm smartphone chip."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/handheld-gaming/switch-2-zelda-40th-anniversary-edition-preorders-hit-usd1-000-on-ebay-amazon-and-walmart-are-your-last-shot-at-usd520-msrp",
    "domain": "AI 算力 / 半导体",
    "title": "Switch 2 Zelda 40th Anniversary Edition preorders open on Amazon for $519.99 — here's your last shot to grab the limited-edition console at MSRP",
    "url": "https://www.tomshardware.com/video-games/handheld-gaming/switch-2-zelda-40th-anniversary-edition-preorders-hit-usd1-000-on-ebay-amazon-and-walmart-are-your-last-shot-at-usd520-msrp",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T17:06:03+00:00",
    "summary": "Scalpers have started selling preorders of the Nintendo Switch 2 The Legend of Zelda 40th Anniversary Edition on eBay, starting at $700."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/cpus/intel-backed-auto-overclocking-tool-hypertune-optimizes-individual-systems-not-test-profiles-tool-claims-fps-improvement-of-up-to-60-percent-on-intel-based-systems",
    "domain": "AI 算力 / 半导体",
    "title": "Intel-backed auto-overclocking tool Hypertune optimizes individual systems, not test profiles — tool claims FPS improvement of up to 60% on Intel-based systems",
    "url": "https://www.tomshardware.com/pc-components/cpus/intel-backed-auto-overclocking-tool-hypertune-optimizes-individual-systems-not-test-profiles-tool-claims-fps-improvement-of-up-to-60-percent-on-intel-based-systems",
    "source": "Jake Roach",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T16:03:05+00:00",
    "summary": "Hypertune is an automated overclocking tool built on top of Intel's Extreme Tuning Utility (XTU) SDK and built in collaboration with engineers at Intel."
  },
  {
    "id": "rss:https://www.tomshardware.com/laptops/framework-cuts-32gb-and-64gb-memory-prices-for-new-laptop-13-pro-issues-retroactive-refunds-modular-laptop-maker-secures-limited-quantity-of-lpcamm2-ram-at-lower-cost",
    "domain": "AI 算力 / 半导体",
    "title": "Framework cuts 32GB and 64GB memory prices for new Laptop 13 Pro, issues retroactive refunds — modular laptop maker secures 'limited quantity' of LPCAMM2 RAM at lower cost",
    "url": "https://www.tomshardware.com/laptops/framework-cuts-32gb-and-64gb-memory-prices-for-new-laptop-13-pro-issues-retroactive-refunds-modular-laptop-maker-secures-limited-quantity-of-lpcamm2-ram-at-lower-cost",
    "source": "Ben Stockton",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T15:00:00+00:00",
    "summary": "Modular laptop maker Framework is dropping some of its memory pricing, including for some already-shipped orders, in a piece of good news for consumers."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/pc-gaming/microsoft-reportedly-gives-secret-xbox-game-pass-discounts-to-churned-subscribers-to-reel-them-back-in-targeted-offers-slash-up-to-30-percent-off-the-regular-price",
    "domain": "AI 算力 / 半导体",
    "title": "Microsoft reportedly gives secret Xbox Game Pass discounts to churned subscribers to reel them back in — targeted offers slash up to 30% off the regular price",
    "url": "https://www.tomshardware.com/video-games/pc-gaming/microsoft-reportedly-gives-secret-xbox-game-pass-discounts-to-churned-subscribers-to-reel-them-back-in-targeted-offers-slash-up-to-30-percent-off-the-regular-price",
    "source": "Zhiye Liu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T14:39:23+00:00",
    "summary": "Microsoft appears to be using dynamic pricing to push select users to commit to Xbox Game Pass."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-says-its-next-generation-processors-could-be-made-at-samsung-double-sourcing-with-tsmc-hints-at-massive-volume-requirements",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI says its next-generation processors could be made at Samsung — double-sourcing with TSMC hints at massive volume requirements",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-says-its-next-generation-processors-could-be-made-at-samsung-double-sourcing-with-tsmc-hints-at-massive-volume-requirements",
    "source": "Anton Shilov",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T14:30:00+00:00",
    "summary": "OpenAI deepens chip cooperation with Samsung, possibly prepares to Double source AI ASICs from two foundries in a bid to get more in-house silicon to its data centers."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/save-40-percent-on-autodesks-media-and-entertainment-collection-thousands-of-dollars-worth-of-software-in-a-single-bundle",
    "domain": "AI 算力 / 半导体",
    "title": "Save 40% on Autodesk’s Media and Entertainment Collection — thousands of dollars worth of software in a single bundle",
    "url": "https://www.tomshardware.com/pc-components/save-40-percent-on-autodesks-media-and-entertainment-collection-thousands-of-dollars-worth-of-software-in-a-single-bundle",
    "source": "Sponsored",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T13:33:15+00:00",
    "summary": "Autodesk is offering a 40% discount on its Media and Entertainment Collection for a limited time."
  },
  {
    "id": "rss:https://www.tomshardware.com/pc-components/ssds/goodram-px700-2tb-ssd-review",
    "domain": "AI 算力 / 半导体",
    "title": "Goodram PX700 2TB SSD Review: High-end punch on a budget core",
    "url": "https://www.tomshardware.com/pc-components/ssds/goodram-px700-2tb-ssd-review",
    "source": "Shane Downing",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T12:34:37+00:00",
    "summary": "The Goodram PX700 matches good all-around performance with high power-efficiency in a cool-running package. It performs mostly like a premium drive, although pricing remains a concern."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-breakthrough-solution-for-the-elusive-navier-stokes-problem-overshadowed-by-plagiarism-controversy-researcher-says-openai-scraped-codex-session-and-issued-career-threats",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI's breakthrough solution for the elusive Navier-Stokes problem overshadowed by plagiarism controversy — researcher says OpenAI scraped Codex session and issued career threats",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-breakthrough-solution-for-the-elusive-navier-stokes-problem-overshadowed-by-plagiarism-controversy-researcher-says-openai-scraped-codex-session-and-issued-career-threats",
    "source": "Bruno Ferreira",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T12:30:00+00:00",
    "summary": "OpenAI announced that a team using one of its internal frontier models has solved the Navier-Stokes problem. However, the announcement has been mired in controversy."
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/big-tech/lg-strongly-denies-tv-security-claims-says-tracking-and-snooping-concerns-not-true-online-investigation-claims-216-000-000-spy-tvs-record-audio",
    "domain": "AI 算力 / 半导体",
    "title": "LG strongly denies TV spying claims, says tracking and snooping concerns 'not true' — online investigation claims 216,000,000 TVs spy and record audio",
    "url": "https://www.tomshardware.com/tech-industry/big-tech/lg-strongly-denies-tv-security-claims-says-tracking-and-snooping-concerns-not-true-online-investigation-claims-216-000-000-spy-tvs-record-audio",
    "source": "Stephen Warwick",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T11:50:18+00:00",
    "summary": "LG has strongly denied recent security and privacy concerns raised regarding its smart TVs."
  },
  {
    "id": "rss:https://www.tomshardware.com/video-games/nintendo/nintendo-unveils-the-legend-of-zelda-40th-anniversary-switch-2-for-usd520-first-ever-special-edition-switch-2-drops-october-19-alongside-usd100-pro-controller-pre-orders-live",
    "domain": "AI 算力 / 半导体",
    "title": "Nintendo unveils The Legend of Zelda 40th Anniversary Switch 2 for $520 — First-ever special-edition Switch 2 drops October 19, alongside $100 Pro Controller, pre-orders live",
    "url": "https://www.tomshardware.com/video-games/nintendo/nintendo-unveils-the-legend-of-zelda-40th-anniversary-switch-2-for-usd520-first-ever-special-edition-switch-2-drops-october-19-alongside-usd100-pro-controller-pre-orders-live",
    "source": "Hassam Nasir",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T11:40:00+00:00",
    "summary": "Nintendo is releasing its first-ever limited-edition Switch 2 to commemorate Zelda's 40th anniversary and it will cost $520. It does not come with Ocarina of Time, but you can purchase a similarly-the"
  },
  {
    "id": "rss:https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-claims-gpt-6-astra-is-an-ethereal-alien-mind-with-agi-like-qualities-company-warns-of-alignment-challenges-as-new-frontier-leader-emerges",
    "domain": "AI 算力 / 半导体",
    "title": "OpenAI claims GPT-6 Astra is an ethereal 'Alien Mind' with AGI-like qualities — company warns of alignment challenges as new frontier leader emerges",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-claims-gpt-6-astra-is-an-ethereal-alien-mind-with-agi-like-qualities-company-warns-of-alignment-challenges-as-new-frontier-leader-emerges",
    "source": "Jon Martindale",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T11:20:00+00:00",
    "summary": "OpenAI has made bold claims with its new GPT-6 Astra AI model, and it's certainly capable, but benchmarks suggest it has many of the usual weaknesses alongside the strengths, while cost and accessibil"
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
    "id": "hn:49558584",
    "domain": "AI 算力 / 半导体",
    "title": "Hugging Face is too important to fall into Nvidia's hands",
    "url": "https://www.theregister.com/ai-and-ml/2026/09/03/hugging-face-is-too-important-to-fall-into-nvidias-hands/5294363",
    "source": "mdp2021",
    "platform": "hackernews",
    "points": 12,
    "published_at": "2026-09-03T23:33:42+00:00",
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
    "points": 1159,
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
    "id": "hn:49611251",
    "domain": "大厂 AI 动态",
    "title": "AlphaGenome Atlas: a high-resolution map of human DNA",
    "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/",
    "source": "utiiiD",
    "platform": "hackernews",
    "points": 598,
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
    "points": 190,
    "published_at": "2026-09-07T20:12:12+00:00",
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
    "id": "hn:49653699",
    "domain": "大厂 AI 动态",
    "title": "The Gemini app is now available for Windows",
    "url": "https://blog.google/innovation-and-ai/products/gemini-app/gemini-app-now-on-windows/",
    "source": "quysala12",
    "platform": "hackernews",
    "points": 35,
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
    "points": 25,
    "published_at": "2026-09-11T00:45:26+00:00",
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
    "id": "rss:https://www.theverge.com/tech/989853/slackforce-surfaces-launch",
    "domain": "大厂 AI 动态",
    "title": "Slack can now vibe-code interactive charts and reports inside chats",
    "url": "https://www.theverge.com/tech/989853/slackforce-surfaces-launch",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T21:25:21+00:00",
    "summary": "A new feature coming to Slack will allow you to build interactive reports, polls, dashboards, presentations, microsites, and other tools directly inside a chat. With Slackforce Surfaces, you can descr"
  },
  {
    "id": "rss:https://www.theverge.com/policy/993308/computer-science-ai-education-coding-kids",
    "domain": "大厂 AI 动态",
    "title": "Schools are catching on to Big Tech’s playbook",
    "url": "https://www.theverge.com/policy/993308/computer-science-ai-education-coding-kids",
    "source": "Lauren Feiner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T19:44:20+00:00",
    "summary": "It's the hot new thing in tech, and it's where all the jobs are. Students who don't learn to use it fall behind. And to help them catch up in time, its creators are graciously providing the resources "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/993455/fire-tv-stick-4k-resident-evil-requiem-deal-sale",
    "domain": "大厂 AI 动态",
    "title": "Amazon’s Fire TV Stick 4K is over half off at under $20",
    "url": "https://www.theverge.com/gadgets/993455/fire-tv-stick-4k-resident-evil-requiem-deal-sale",
    "source": "Brad Bourque",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T16:58:44+00:00",
    "summary": "Looking to take full advantage of your 4K television, but your current streaming stick doesn’t have the right features? Through September 13th, you can grab an Amazon Fire TV Stick 4K from Woot for ju"
  },
  {
    "id": "rss:https://www.theverge.com/transportation/993341/evtol-air-taxi-aviation-eipp-texas",
    "domain": "大厂 AI 动态",
    "title": "Electric air taxis get the green light for test flights in Texas",
    "url": "https://www.theverge.com/transportation/993341/evtol-air-taxi-aviation-eipp-texas",
    "source": "Andrew J. Hawkins",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T16:00:00+00:00",
    "summary": "A new federal program to test the feasibility of electric, hybrid-electric, and autonomous aircraft kicks off today in Texas - before the rules governing this new technology have even been finalized. "
  },
  {
    "id": "rss:https://www.theverge.com/ai-artificial-intelligence/993465/universal-music-elevenlabs-ai",
    "domain": "大厂 AI 动态",
    "title": "Universal Music is launching an AI music platform with ElevenLabs",
    "url": "https://www.theverge.com/ai-artificial-intelligence/993465/universal-music-elevenlabs-ai",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T15:38:19+00:00",
    "summary": "Universal Music Group is launching a new AI-powered platform that will allow users to draw from its catalog of licensed music to create song remixes, mashups, and new takes on tracks, according to an "
  },
  {
    "id": "rss:https://www.theverge.com/gadgets/988579/apple-watch-series-12-5g-ultra-4-preorder-buy",
    "domain": "大厂 AI 动态",
    "title": "Where to preorder the new Apple Watch Series 12 and Ultra 4",
    "url": "https://www.theverge.com/gadgets/988579/apple-watch-series-12-5g-ultra-4-preorder-buy",
    "source": "Cameron Faulkner",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T15:00:00+00:00",
    "summary": "The iPhone Duo was the unequivocal star of Apple's \"Surprise and shine\" event, but not for people who were mostly paying attention for news on wearables. Thankfully, Apple had a lot to share about its"
  },
  {
    "id": "rss:https://www.theverge.com/games/992937/wolverine-review-ps5",
    "domain": "大厂 AI 动态",
    "title": "Wolverine on the PS5 goes back to a simpler (and bloodier) style of action game",
    "url": "https://www.theverge.com/games/992937/wolverine-review-ps5",
    "source": "Andrew Webster",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T15:00:00+00:00",
    "summary": "Marvel's Wolverine captures just how angry its lead character is. The latest PS5 exclusive from Spider-Man developer Insomniac, Wolverine is a straightforward action game that is at its best when you'"
  },
  {
    "id": "rss:https://www.theverge.com/tech/993391/meta-muse-ai-hands-on",
    "domain": "大厂 AI 动态",
    "title": "Meta’s Muse AI works and creeps me out",
    "url": "https://www.theverge.com/tech/993391/meta-muse-ai-hands-on",
    "source": "Emma Roth",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T15:00:00+00:00",
    "summary": "Meta has launched its new Muse assistant, marking the company's first real foray into AI-powered productivity tools. The company says its AI agent can \"take the busywork off your plate\" by helping you"
  },
  {
    "id": "rss:https://www.theverge.com/policy/993383/jimmy-kimmel-fcc-brendan-carr-james-talarico",
    "domain": "大厂 AI 动态",
    "title": "Another big James Talarico interview is punted to YouTube due to FCC threats",
    "url": "https://www.theverge.com/policy/993383/jimmy-kimmel-fcc-brendan-carr-james-talarico",
    "source": "Stevie Bonifield",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T14:34:36+00:00",
    "summary": "Jimmy Kimmel will be interviewing Democratic Texas Senate candidate James Talarico \"under unusual circumstances,\" posting the interview directly to YouTube, rather than airing it on TV during Jimmy Ki"
  },
  {
    "id": "rss:https://www.theverge.com/tech/993300/iphone-duo-hardware-software-android-samsung-oppo",
    "domain": "大厂 AI 动态",
    "title": "The iPhone Duo’s hardware doesn’t look special, but its software might be",
    "url": "https://www.theverge.com/tech/993300/iphone-duo-hardware-software-android-samsung-oppo",
    "source": "Dominic Preston",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T14:21:38+00:00",
    "summary": "With the iPhone Duo, Apple has pulled off a familiar trick. It arrives into a mature Android foldable market with a handful of hardware features we've mostly already seen elsewhere, but paired with a "
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/thrive-capital-showed-vcs-the-way-into-pro-sports-ownership-collaborative-fund-is-now-trying-its-own-version-of-the-same-play/",
    "domain": "大厂 AI 动态",
    "title": "Thrive Capital led VCs into pro sports ownership; Collaborative Fund just upped that play",
    "url": "https://techcrunch.com/2026/09/10/thrive-capital-showed-vcs-the-way-into-pro-sports-ownership-collaborative-fund-is-now-trying-its-own-version-of-the-same-play/",
    "source": "Connie Loizos",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T22:30:00+00:00",
    "summary": "Collaborative Fund just bought into D.C. United and its stadium, with firm founder Craig Shapiro pitching it as a way to showcase for the firm's startups."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/jensen-huang-explains-why-nvidia-will-grow-an-astounding-70-next-year/",
    "domain": "大厂 AI 动态",
    "title": "Jensen Huang explains why Nvidia will grow an astounding 70% next year",
    "url": "https://techcrunch.com/2026/09/10/jensen-huang-explains-why-nvidia-will-grow-an-astounding-70-next-year/",
    "source": "Julie Bort",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T21:51:59+00:00",
    "summary": "Nvidia has its finger in every pie, and sees another year of plenty in its future, Jensen Huang says. But, he insists, its deals are not circular."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/mark-wahlberg-is-coming-to-techcrunch-disrupt-2026/",
    "domain": "大厂 AI 动态",
    "title": "Mark Wahlberg is coming to TechCrunch Disrupt 2026, and he wants to talk about your work, not his",
    "url": "https://techcrunch.com/2026/09/10/mark-wahlberg-is-coming-to-techcrunch-disrupt-2026/",
    "source": "TechCrunch Events",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T21:35:00+00:00",
    "summary": "Mark Wahlberg joins Bruce K. Lee at Disrupt to discuss investing, entrepreneurship, healthcare, wellness, and building businesses."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/openai-puts-pro-subscriptions-on-hold-due-to-astra-demand/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI puts Pro subscriptions on hold due to Astra demand",
    "url": "https://techcrunch.com/2026/09/10/openai-puts-pro-subscriptions-on-hold-due-to-astra-demand/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T20:59:51+00:00",
    "summary": "The company said Pro subscriptions put the most strain on its systems, so it's pausing sign-ups while adding more capacity."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/anthropic-details-distillation-campaigns-from-alibaba-moonshot-ai-and-deepseek/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic details distillation campaigns from Alibaba, Moonshot AI, and DeepSeek",
    "url": "https://techcrunch.com/2026/09/10/anthropic-details-distillation-campaigns-from-alibaba-moonshot-ai-and-deepseek/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T20:57:30+00:00",
    "summary": "A new report released Thursday by Anthropic alleges persistent distillation attacks by China-based AI companies, which have escalated in recent months as competition in the space has intensified."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/furos-founders-left-silicon-valley-and-its-paying-off/",
    "domain": "大厂 AI 动态",
    "title": "Furo’s founders left Silicon Valley — and it’s paying off",
    "url": "https://techcrunch.com/2026/09/10/furos-founders-left-silicon-valley-and-its-paying-off/",
    "source": "Anna Heim",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T20:48:00+00:00",
    "summary": "The three 28-year-old founders behind energy startup Furo moved from Silicon Valley and back to Germany, and yet secured $4 million in funding from mostly U.S. backers."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/metas-ai-agent-muse-is-now-the-no-2-app-in-the-us/",
    "domain": "大厂 AI 动态",
    "title": "Meta’s AI agent Muse is now the No. 2 app in the US",
    "url": "https://techcrunch.com/2026/09/10/metas-ai-agent-muse-is-now-the-no-2-app-in-the-us/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T19:50:04+00:00",
    "summary": "Meta's newest app Muse is off to a slower start than the company's other apps, like Meta AI or Threads."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/proxima-fusion-bets-e140m-on-a-critical-fusion-ingredient-dominated-by-asian-suppliers/",
    "domain": "大厂 AI 动态",
    "title": "Proxima Fusion bets €140M on a critical fusion ingredient dominated by Asian suppliers",
    "url": "https://techcrunch.com/2026/09/10/proxima-fusion-bets-e140m-on-a-critical-fusion-ingredient-dominated-by-asian-suppliers/",
    "source": "Tim De Chant",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T18:38:00+00:00",
    "summary": "Proxima Fusion said Wednesday it plans to build a €140 million ($162.6 million) factory to produce fusion-grade high-temperature superconducting (HTS) tape, which will provide the startup with key com"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/amazon-makes-it-easier-to-buy-what-you-see-on-prime-video/",
    "domain": "大厂 AI 动态",
    "title": "Amazon makes it easier to buy what you see on Prime Video",
    "url": "https://techcrunch.com/2026/09/10/amazon-makes-it-easier-to-buy-what-you-see-on-prime-video/",
    "source": "Sarah Perez",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T18:10:36+00:00",
    "summary": "Amazon is expanding shopping integrations across Prime Video, letting viewers discover products tied to thousands of shows, movies, and live sports through X-Ray, its shopping app, and a new Lens-powe"
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/anthropic-reveals-rogue-ai-agents-hate-captchas-just-like-you/",
    "domain": "大厂 AI 动态",
    "title": "Anthropic reveals rogue AI agents hate CAPTCHAs, just like you",
    "url": "https://techcrunch.com/2026/09/10/anthropic-reveals-rogue-ai-agents-hate-captchas-just-like-you/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T17:54:44+00:00",
    "summary": "Come inside the mind of a bot trying to convince the internet it's human."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/indias-pocket-fm-doubles-revenue-run-rate-to-500m-as-ai-powers-93-of-audio-content/",
    "domain": "大厂 AI 动态",
    "title": "India’s Pocket FM doubles revenue run rate to $500M as AI powers 93% of audio content",
    "url": "https://techcrunch.com/2026/09/10/indias-pocket-fm-doubles-revenue-run-rate-to-500m-as-ai-powers-93-of-audio-content/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T17:45:00+00:00",
    "summary": "Pocket FM uses AI to produce 99% of its new content, helping make content production about 80 times cheaper."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/instagrams-latest-feature-lets-you-add-tagged-posts-to-your-profile-grid/",
    "domain": "大厂 AI 动态",
    "title": "Instagram’s latest feature lets you add tagged posts to your profile grid",
    "url": "https://techcrunch.com/2026/09/10/instagrams-latest-feature-lets-you-add-tagged-posts-to-your-profile-grid/",
    "source": "Lauren Forristal",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T16:31:25+00:00",
    "summary": "Instagram's newest feature lets users take posts from the Tagged tab and move it to their main profile grid instead."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/google-is-making-it-easier-to-switch-between-password-managers-on-android/",
    "domain": "大厂 AI 动态",
    "title": "Google is making it easier to switch between password managers on Android",
    "url": "https://techcrunch.com/2026/09/10/google-is-making-it-easier-to-switch-between-password-managers-on-android/",
    "source": "Ivan Mehta",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T16:00:00+00:00",
    "summary": "Google's new feature will transfer your passkeys as well."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/the-boring-company-raises-3b-in-round-led-by-uae/",
    "domain": "大厂 AI 动态",
    "title": "The Boring Company raises $3B in round led by UAE",
    "url": "https://techcrunch.com/2026/09/10/the-boring-company-raises-3b-in-round-led-by-uae/",
    "source": "Sean O'Kane",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T15:07:27+00:00",
    "summary": "The company said it plans to dig more than 150 kilometers of tunnels in the Middle Eastern country."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/ai-agents-are-flooding-public-services-with-new-requests/",
    "domain": "大厂 AI 动态",
    "title": "AI agents are flooding public services with new requests",
    "url": "https://techcrunch.com/2026/09/10/ai-agents-are-flooding-public-services-with-new-requests/",
    "source": "Russell Brandom",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T14:53:50+00:00",
    "summary": "“The vast majority of cases we find are people who are entitled to claim for something, claiming for that thing,” the researcher told TechCrunch."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/bending-spoons-to-buy-collaboration-tools-maker-miro-for-1-36b-90-less-than-its-2022-valuation/",
    "domain": "大厂 AI 动态",
    "title": "Bending Spoons to buy collaboration tools maker Miro for $1.36B, 90% less than its 2022 valuation",
    "url": "https://techcrunch.com/2026/09/10/bending-spoons-to-buy-collaboration-tools-maker-miro-for-1-36b-90-less-than-its-2022-valuation/",
    "source": "Ram Iyer",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T14:34:09+00:00",
    "summary": "Bending Spoons is buying Miro for $1.36 billion, a huge dip in valuation for the workplace collaboration startup, which was valued at $17.5 billion in late 2021."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/maven-robotics-wants-to-steal-your-robot-deployment-deal/",
    "domain": "大厂 AI 动态",
    "title": "Maven Robotics wants to steal your robot deployment deal",
    "url": "https://techcrunch.com/2026/09/10/maven-robotics-wants-to-steal-your-robot-deployment-deal/",
    "source": "Tim Fernholz",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T14:17:37+00:00",
    "summary": "Maven Robotics emerged from stealth today with a $100 million Series A and active deployments."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/google-signs-its-biggest-rice-methane-carbon-credit-deal-with-indian-startup-mitti-labs/",
    "domain": "大厂 AI 动态",
    "title": "Google signs its biggest rice-methane carbon credit deal with Indian startup Mitti Labs",
    "url": "https://techcrunch.com/2026/09/10/google-signs-its-biggest-rice-methane-carbon-credit-deal-with-indian-startup-mitti-labs/",
    "source": "Jagmeet Singh",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T13:34:01+00:00",
    "summary": "The four-year agreement will cover rice farms across three Indian states, reaching about 100,000 hectares at peak delivery."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/id-verification-giant-idscan-confirms-data-breach-with-more-than-150-million-drivers-licenses-stolen/",
    "domain": "大厂 AI 动态",
    "title": "ID verification giant IDScan confirms data breach with more than 150 million driver’s licenses stolen",
    "url": "https://techcrunch.com/2026/09/10/id-verification-giant-idscan-confirms-data-breach-with-more-than-150-million-drivers-licenses-stolen/",
    "source": "Zack Whittaker",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T13:21:09+00:00",
    "summary": "The ID checking company said the data breach included people's full names and driver's licenses and other government-issued identity documents."
  },
  {
    "id": "rss:https://techcrunch.com/2026/09/10/snapchat-takes-aim-at-partiful-with-new-event-planning-features/",
    "domain": "大厂 AI 动态",
    "title": "Snapchat takes aim at Partiful with new event-planning features",
    "url": "https://techcrunch.com/2026/09/10/snapchat-takes-aim-at-partiful-with-new-event-planning-features/",
    "source": "Aisha Malik",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T13:00:00+00:00",
    "summary": "Snapchat says the new features can be used to organize everything from birthday celebrations and sporting events to study sessions and weekend hangouts."
  },
  {
    "id": "rss:https://stratechery.com/2026/the-iphone-duo-the-intelligent-personal-hub-apple-watch-audio-intelligence/",
    "domain": "大厂 AI 动态",
    "title": "The iPhone Duo, The Intelligent Personal Hub, Apple Watch Audio Intelligence",
    "url": "https://stratechery.com/2026/the-iphone-duo-the-intelligent-personal-hub-apple-watch-audio-intelligence/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T10:00:00+00:00",
    "summary": "Apple once again demonstrated the power of integrating hardware and software, but it's biggest AI blindspot might be its belief in the primacy of apps."
  },
  {
    "id": "rss:https://stratechery.com/2026/openai-does-math-reward-hacking-meta-launches-personal-agent/",
    "domain": "大厂 AI 动态",
    "title": "OpenAI Does Math, Reward-Hacking, Meta Launches Personal Agent",
    "url": "https://stratechery.com/2026/openai-does-math-reward-hacking-meta-launches-personal-agent/",
    "source": "Ben Thompson",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-09T10:00:00+00:00",
    "summary": "OpenAI solving one of the most famous math problems is extremely impressive, and of little impact to most people's lives; Meta's Muse agent launch has the potential to be the exact opposite."
  },
  {
    "id": "rss:https://arstechnica.com/health/2026/09/boy-developed-toasted-skin-condition-from-using-a-laptop-every-day/",
    "domain": "大厂 AI 动态",
    "title": "Boy developed \"toasted skin\" condition from using a laptop every day",
    "url": "https://arstechnica.com/health/2026/09/boy-developed-toasted-skin-condition-from-using-a-laptop-every-day/",
    "source": "Beth Mole",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T22:16:05+00:00",
    "summary": "Laptops don't usually get hot enough to burn—but they can still be harmful."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/linkedin-beats-browsergate-lawsuits-over-scanning-users-chrome-extensions/",
    "domain": "大厂 AI 动态",
    "title": "LinkedIn beats \"BrowserGate\" lawsuits over scanning users' Chrome extensions",
    "url": "https://arstechnica.com/tech-policy/2026/09/linkedin-beats-browsergate-lawsuits-over-scanning-users-chrome-extensions/",
    "source": "Jon Brodkin",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T20:55:29+00:00",
    "summary": "Judge tosses lawsuits, says plaintiffs didn't allege any real privacy violation."
  },
  {
    "id": "rss:https://arstechnica.com/space/2026/09/europe-will-go-it-alone-on-venus-mission-after-nasa-yanks-radar-instrument/",
    "domain": "大厂 AI 动态",
    "title": "Europe will go it alone on Venus mission after NASA yanks radar instrument",
    "url": "https://arstechnica.com/space/2026/09/europe-will-go-it-alone-on-venus-mission-after-nasa-yanks-radar-instrument/",
    "source": "Stephen Clark",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T19:09:29+00:00",
    "summary": "Europe is looking inward, and perhaps to China, as the White House tries to cancel some NASA partnerships."
  },
  {
    "id": "rss:https://arstechnica.com/gadgets/2026/09/android-can-now-securely-migrate-your-logins-between-password-managers/",
    "domain": "大厂 AI 动态",
    "title": "Android can now securely migrate your logins between password managers",
    "url": "https://arstechnica.com/gadgets/2026/09/android-can-now-securely-migrate-your-logins-between-password-managers/",
    "source": "Ryan Whitwam",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T18:41:09+00:00",
    "summary": "App support is slim right now, but Google says more are coming."
  },
  {
    "id": "rss:https://arstechnica.com/tech-policy/2026/09/panic-builds-over-bankrupt-spirits-looming-data-sale-to-google/",
    "domain": "大厂 AI 动态",
    "title": "Panic builds over bankrupt Spirit’s looming data sale to Google",
    "url": "https://arstechnica.com/tech-policy/2026/09/panic-builds-over-bankrupt-spirits-looming-data-sale-to-google/",
    "source": "Ashley Belanger",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-10T18:14:14+00:00",
    "summary": "\"Bankruptcy cannot become the new land grab for AI.”"
  },
  {
    "id": "hn:49599992",
    "domain": "股票",
    "title": "Stockfish 19",
    "url": "https://stockfishchess.org/blog/2026/stockfish-19/",
    "source": "atiedebee",
    "platform": "hackernews",
    "points": 275,
    "published_at": "2026-09-07T16:17:27+00:00",
    "summary": ""
  },
  {
    "id": "wscn:3781564",
    "domain": "股票",
    "title": "特朗普民调下滑、债市失控——沃什的独立空间正在打开？",
    "url": "https://wallstreetcn.com/articles/3781564",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T07:53:43+00:00",
    "summary": "分析认为，美债收益率攀升与特朗普民调承压，意外增大了美联储主席沃什的独立政策空间。鲍威尔留任董事会提供政治掩护，而收益率上行亦协同压制通胀。凭借与财长贝森特的深厚渊源及外部环境变化，沃什正展现出超预期的战略定力与施政空间。"
  },
  {
    "id": "wscn:3781078",
    "domain": "股票",
    "title": "钼的未来展望：2.64万吨硬性缺口，为什么它的弹性如此惊人？",
    "url": "https://wallstreetcn.com/premium/articles/3781078?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T07:32:54+00:00",
    "summary": "一份关于\"70%副产供给 × 无成本约束 × 需求结构迁移\"三重错配的深度拆解。"
  },
  {
    "id": "wscn:3781569",
    "domain": "股票",
    "title": "报道：沙特首相两次致电敦促美方打击胡塞武装，均遭特朗普拒绝",
    "url": "https://wallstreetcn.com/articles/3781569",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T07:30:41+00:00",
    "summary": "据报道援引两名美国官员报道，沙特王储兼首相于9月10日两度致电特朗普，要求美国对胡塞武装动手，均遭拒绝。当天胡塞武装逼近红海战略要道曼德海峡，油价随之上涨。美方表示无意直接军事介入，但将提供情报与目标数据，并已派驻约200名军事人员赴沙特提供非作战支持。"
  },
  {
    "id": "wscn:3781568",
    "domain": "股票",
    "title": "撤退信号？“大空头”平仓英伟达和Palantir看跌期权",
    "url": "https://wallstreetcn.com/articles/3781568",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T07:08:13+00:00",
    "summary": "“大空头”Michael Burry全面收缩风险，平仓了英伟达和Palantir的2026年12月到期看跌期权，理由是规避时间价值损耗，但他仍持有Palantir的2027年看跌期权及多个科技股空头。与此同时，黄仁勋转发GPU租金环比上涨22%的数据，回击Burry关于芯片折旧年限被高估的核心看空逻辑。"
  },
  {
    "id": "wscn:3781566",
    "domain": "股票",
    "title": "下周美联储加息与否，今晚CPI一锤定音？",
    "url": "https://wallstreetcn.com/articles/3781566",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T07:06:39+00:00",
    "summary": "一个小数点之差或直接决定美联储下周是否加息：核心CPI环比0.2%意味着按兵不动，0.3%则触发加息。联储内部分歧明显，债市、美元、日元与股市均已高度戒备。高盛警告，若数据温和而美联储选择按兵不动，债券市场对\"政策失误\"的担忧将远大于在通胀超标情况下加息所带来的损害。"
  },
  {
    "id": "wscn:3781555",
    "domain": "股票",
    "title": "付鹏：能源市场成品油的紧张终于传导到了上游，警惕上下游左脚踩右脚【付鹏说4】",
    "url": "https://wallstreetcn.com/premium/articles/3781555?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T06:53:33+00:00",
    "summary": "美国炼厂开工率已达98%，柴油价格创历史新高，出口创新高、库存降至极低水平，表明下游已紧张到极限。随着检修季和冬季临近，炼厂一旦检修或出现故障，柴油价格将急剧上涨并反向拉动原油；叠加交易员已将地缘政治风险溢价转移至下游，上下游可能形成相互推升的“左脚踩右脚”循环。"
  },
  {
    "id": "wscn:3781553",
    "domain": "股票",
    "title": "A股三大股指跌幅显著收窄，算力硬件反弹，有色金属全线下挫，中际旭创AH股齐涨，恒科指转涨，科网股回升",
    "url": "https://wallstreetcn.com/articles/3781553",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T06:28:51+00:00",
    "summary": "盘面上，个股呈现普跌态势，沪深京三市约5200股飘绿，上午半天成交1.28万亿。沪深两市半日成交额1.27万亿，较上个交易日放量1833亿。板块方面，有色金属、存储、房地产、石化、券商板块领跌。银行、油气、电力、电信板块逆市活跃。中际旭创、新易盛硬扛光通信效果有限。"
  },
  {
    "id": "wscn:3781567",
    "domain": "股票",
    "title": "宇树科技总市值跌破2000亿元，股价跌破490元",
    "url": "https://wallstreetcn.com/articles/3781567",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T06:20:11+00:00",
    "summary": "宇树科技开盘报490.25元/股，跌1.66%。进入连续竞价交易之后，股价很快跌破490元/股，总市值跌破2000亿元。"
  },
  {
    "id": "wscn:3781549",
    "domain": "股票",
    "title": "中东局势现缓和信号，油价日内回调3%，亚洲股债双杀、日股重挫近3%，美债十年期收益率逼近5%",
    "url": "https://wallstreetcn.com/articles/3781549",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T06:02:42+00:00",
    "summary": "布伦特原油延续跌势，日内跌幅扩大至3%，现报102.99美元/桶。WTI原油跌近3%，报97.68美元/桶。日经225指数早盘跌幅一度达2.8%，印度Nifty指数亦下跌约1%。美国10年期国债收益率徘徊于4.96%，距5%整数关口仅一步之遥。市场屏息等待周五美国CPI数据。"
  },
  {
    "id": "wscn:3781565",
    "domain": "股票",
    "title": "油价短线下挫！伊朗将与海湾六国会晤、红海西海岸停火，中东局势现缓和信号",
    "url": "https://wallstreetcn.com/articles/3781565",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T06:00:58+00:00",
    "summary": "霍尔木兹与红海同步释放缓和信号——海合会六国外长定于9月14日赴阿曼与伊朗外长会晤，寻求商船通行临时协议；与此同时，胡塞武装宣布红海西海岸停火。两大战略水道紧张态势齐松，布伦特原油应声下挫近2%至105.57美元。但美伊分歧犹存，协议能否落地仍是最大变数。"
  },
  {
    "id": "wscn:3781490",
    "domain": "股票",
    "title": "CPI再临关键窗口：美联储加息之后，警惕滞胀定价接管市场",
    "url": "https://wallstreetcn.com/premium/articles/3781490?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T05:31:49+00:00",
    "summary": "8月CPI是关键。美联储加息概率大，加息后市场恐转向滞胀定价，风险资产承压。"
  },
  {
    "id": "wscn:3781562",
    "domain": "股票",
    "title": "OpenAI CFO：当AI让一切“经验”贬值，什么才是企业的稀缺品？",
    "url": "https://wallstreetcn.com/articles/3781562",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T04:04:56+00:00",
    "summary": "OpenAI CFO Sarah Friar出，2025年AI进入“智能体（Agent）”时代，“程序员消亡论”被严重夸大，核心逻辑能力将取代代码输入。Friar强调，随着AI技术实质性推升企业盈利、智力彻底商品化，人类不可替代的“判断力”与人际交互能力将成为未来企业最核心的稀缺资产。"
  },
  {
    "id": "wscn:3781547",
    "domain": "股票",
    "title": "开个会就能印4万亿美元，央行的钱是怎么\"凭空\"造出来的？【胡捷大师课1.2】",
    "url": "https://wallstreetcn.com/premium/articles/3781547?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T04:00:50+00:00",
    "summary": "从开会决议、账本写数到购买国债：央行货币\"凭空\"诞生并注入经济体的全过程。"
  },
  {
    "id": "wscn:3781563",
    "domain": "股票",
    "title": "新债王Gundlach警示：若美联储按兵不动，长端利率将大幅攀升",
    "url": "https://wallstreetcn.com/articles/3781563",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T03:56:56+00:00",
    "summary": "Gundlach认为，美国通胀远未消退，CPI轨迹与70年代大通胀时期“惊人相似”，真实通胀或高达7%。值得警惕的是，信贷市场出现严重分化，AI企业债因“雪崩式”供给导致利差剧烈走阔。同时，面对高达42倍的标普席勒市盈率和38%的科技股权重，Gundlach直言美股处于“极度危险”状态。"
  },
  {
    "id": "wscn:3781556",
    "domain": "股票",
    "title": "苹果“新掌门”的产品哲学：技术审美重于概念营销，不追求首发追求“终局定义”",
    "url": "https://wallstreetcn.com/articles/3781556",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T03:08:42+00:00",
    "summary": "苹果新任CEO特纳斯在上任后的首场专访中，明确了AI时代的战略定调：拒绝“AI可穿戴取代手机”的市场噱头，坚守iPhone作为“完美智能个人中枢”的绝对核心地位。这位25年的工程老将以首款折叠机iPhone Duo诠释了苹果“不追首发、追求终局”的产品哲学。"
  },
  {
    "id": "wscn:3780982",
    "domain": "股票",
    "title": "网络安全崛起：AI隐患叙事下，网安何以成为软件板块最强反转？",
    "url": "https://wallstreetcn.com/premium/articles/3780982?layout=wscn-layout",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T03:00:04+00:00",
    "summary": "AI 隐患对网安市场的影响，很可能不是一次性的题材脉冲，而是一条独立于 AI 资本开支之外的、长期刚性的增量支出曲线。"
  },
  {
    "id": "wscn:3781557",
    "domain": "股票",
    "title": "美债收益率5%、油价120 美元、VIX 指数25？市场的噩梦场景正在成为现实",
    "url": "https://wallstreetcn.com/articles/3781557",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T02:52:58+00:00",
    "summary": "美债10年期收益率强势突破4.8%，正步步逼近5%这道\"生死线\"——一旦站稳，将正式脱离多年震荡区间，上方几乎无险可守。油价冲顶、农产品齐涨持续推升通胀预期，VIX骤然觉醒，机构抢购尾部风险保护。AI叙事支撑科技股韧性，但纳斯达克35%空头积累随时可能触发轧空。"
  },
  {
    "id": "wscn:3781551",
    "domain": "股票",
    "title": "花旗：拉美处于“腾飞前夜”，弱美元、商品牛市、供应链重构三重利好共振！",
    "url": "https://wallstreetcn.com/articles/3781551",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T02:05:41+00:00",
    "summary": "花旗表示，弱美元、大宗商品高位、供应链重构与政治右转顺风等多重因素同步共振，拉美正站上数十年来最佳宏观起点，外部环境与2003-2008年超级周期高度相似。MSCI拉美指数同步叩关十年关键阻力位，一旦突破，或意味着新一轮结构性牛市正式开启。"
  },
  {
    "id": "wscn:3781548",
    "domain": "股票",
    "title": "Kalshi获准推出黄金白银永续期货，与传统交易所抢生意",
    "url": "https://wallstreetcn.com/articles/3781548",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T02:00:16+00:00",
    "summary": "Kalshi获CFTC批准于周四上线黄金和白银永续期货，成为美国首个获批的非加密货币类永续期货产品。自5月推出加密货币永续期货以来，相关合约名义交易量已达440亿美元。CME Group等传统交易所股价承压，CME更已起诉CFTC试图阻止该类产品扩张。Kalshi还在申请美股、铜及外汇永续期货。"
  },
  {
    "id": "wscn:3781534",
    "domain": "股票",
    "title": "研究员要失业了？OpenAI推出金融版ChatGPT，研究、建模、PPT一站式完成",
    "url": "https://wallstreetcn.com/articles/3781534",
    "source": "华尔街见闻 API",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T01:57:30+00:00",
    "summary": "ChatGPT金融版基于GPT-6 Astra构建，内置来自Daloopa、PitchBook和LSEG News等数据源的数据，包含财报电话会议记录、财务报表和公司基本面等信息；旨在帮助研究员更高效地进行研究、构建财务模型，制作客户材料等工作。"
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
    "points": 370,
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
    "id": "hn:49626052",
    "domain": "金融",
    "title": "One woman's Tesla was remotely controlled by an abusive ex-partner",
    "url": "https://www.theguardian.com/australia-news/2026/sep/09/how-one-womans-tesla-was-remotely-controlled-and-harass-by-her-abusive-ex-partner-ntwnfb",
    "source": "gradschool",
    "platform": "hackernews",
    "points": 72,
    "published_at": "2026-09-09T13:16:45+00:00",
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
    "id": "hn:49596610",
    "domain": "金融",
    "title": "Initial effects of AI technology on employment look positive",
    "url": "https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here",
    "source": "MrBuddyCasino",
    "platform": "hackernews",
    "points": 99,
    "published_at": "2026-09-07T10:38:32+00:00",
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
    "id": "rss:https://arxiv.org/abs/2609.11614",
    "domain": "金融",
    "title": "Deep Learning of Robust Market Making under Regime-Switching Order Flow",
    "url": "https://arxiv.org/abs/2609.11614",
    "source": "Felipe Moret, Fabrizio Lillo",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T04:00:00+00:00",
    "summary": "arXiv:2609.11614v1 Announce Type: new Abstract: Classical market-making strategies based on stochastic control, such as the Avellaneda-Stoikov and the Gu\\'{e}ant-Lehalle-Fernandez-Tapia (GLFT) extensi"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.11905",
    "domain": "金融",
    "title": "Entropic Value-at-Risk parity for tempered stable returns",
    "url": "https://arxiv.org/abs/2609.11905",
    "source": "Jaehyung Choi",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T04:00:00+00:00",
    "summary": "arXiv:2609.11905v1 Announce Type: new Abstract: We develop Entropic Value-at-Risk (EVaR) parity for tempered stable returns. EVaR-based inverse risk parity (IRP) and equal risk contribution (ERC) port"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.10543",
    "domain": "金融",
    "title": "The Privacy Subsidy in Market Microstructure",
    "url": "https://arxiv.org/abs/2609.10543",
    "source": "Yuki Nakamura",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T04:00:00+00:00",
    "summary": "arXiv:2609.10543v1 Announce Type: cross Abstract: Privacy-preserving exchange designs price on a coarsened view of order flow. We show that a market maker committed to informationally efficient (poste"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.10587",
    "domain": "金融",
    "title": "Expected Shortfall Factor Models: Common Tail Losses and Expected Returns",
    "url": "https://arxiv.org/abs/2609.10587",
    "source": "Yujie Hou, Xinbing Kong, Yalin Wang, Bin Wu",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T04:00:00+00:00",
    "summary": "arXiv:2609.10587v1 Announce Type: cross Abstract: We develop an expected shortfall factor model (ESFM) to estimate and price common variation in the severity of lower-tail losses in large panels of as"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.10865",
    "domain": "金融",
    "title": "The Elliptically Optimal Confidence Interval: A Bivariate Extension of Wilson's Score Method",
    "url": "https://arxiv.org/abs/2609.10865",
    "source": "Nawaf Mohammed",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T04:00:00+00:00",
    "summary": "arXiv:2609.10865v1 Announce Type: cross Abstract: Constructing a confidence interval for the difference between two independent binomial proportions involves a nuisance direction that is not identifie"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.11575",
    "domain": "金融",
    "title": "Market-Informed Networks for Modeling and Forecast Evaluation of Financial Extremes",
    "url": "https://arxiv.org/abs/2609.11575",
    "source": "Ayla Jungbluth, Johannes Lederer, Simon Trimborn",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T04:00:00+00:00",
    "summary": "arXiv:2609.11575v1 Announce Type: cross Abstract: Modeling the joint distribution of extreme values in high-dimensional financial time series is challenging because extremes are sparse and locally ext"
  },
  {
    "id": "rss:https://arxiv.org/abs/2609.11586",
    "domain": "金融",
    "title": "Short-maturity skew stickiness ratio under local volatility",
    "url": "https://arxiv.org/abs/2609.11586",
    "source": "Masaaki Fukasawa",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T04:00:00+00:00",
    "summary": "arXiv:2609.11586v1 Announce Type: cross Abstract: We prove that the skew stickiness ratio converges to two at short maturity under local volatility models. This appears to be the first rigorous proof "
  },
  {
    "id": "rss:https://arxiv.org/abs/2409.02521",
    "domain": "金融",
    "title": "Fundamental Properties of Linear Factor Models",
    "url": "https://arxiv.org/abs/2409.02521",
    "source": "Damir Filipovic, Paul Schneider",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T04:00:00+00:00",
    "summary": "arXiv:2409.02521v4 Announce Type: replace Abstract: We characterize the loading matrices that admit a conditional linear factor representation for excess returns in which the factors are traded, resid"
  },
  {
    "id": "rss:https://arxiv.org/abs/2503.21310",
    "domain": "金融",
    "title": "The evolving boundary of green technology",
    "url": "https://arxiv.org/abs/2503.21310",
    "source": "Nicol\\`o Barbieri, Kerstin H\\\"otte, Peter Persoon",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T04:00:00+00:00",
    "summary": "arXiv:2503.21310v2 Announce Type: replace Abstract: Green patent indicators are widely used to track technological progress, assess climate and innovation policies, and identify emerging technological"
  },
  {
    "id": "rss:https://arxiv.org/abs/2512.17225",
    "domain": "金融",
    "title": "Modeling financial time series with $\\phi^{4}$ quantum field theory",
    "url": "https://arxiv.org/abs/2512.17225",
    "source": "Dimitrios Bachtis, David S. Berman, Arabella Schelpe",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T04:00:00+00:00",
    "summary": "arXiv:2512.17225v2 Announce Type: replace Abstract: We use a $\\phi^{4}$ quantum field theory with inhomogeneous couplings and explicit symmetry-breaking to model an ensemble of financial time series f"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.13992",
    "domain": "金融",
    "title": "Group Quantization and Mellin Representations of the Heston Model",
    "url": "https://arxiv.org/abs/2606.13992",
    "source": "Santiago Garcia",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T04:00:00+00:00",
    "summary": "arXiv:2606.13992v2 Announce Type: replace Abstract: We develop an Affine Holonomy Group Quantization framework for the Heston stochastic volatility model. The Heston affine pricing symbol is decompose"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.20041",
    "domain": "金融",
    "title": "AI Economist Agent: An Agentic Framework for Evidence-Based Economic and Financial Analysis with RAG, Knowledge Graphs, and Large Language Models",
    "url": "https://arxiv.org/abs/2606.20041",
    "source": "Masahiro Kato",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T04:00:00+00:00",
    "summary": "arXiv:2606.20041v2 Announce Type: replace Abstract: We propose an AI economist agent for economic and financial scenario analysis. Scenario design often requires analysts to assess emerging risks with"
  },
  {
    "id": "rss:https://arxiv.org/abs/2607.12156",
    "domain": "金融",
    "title": "(Early) AI Compute Asset Pricing",
    "url": "https://arxiv.org/abs/2607.12156",
    "source": "Federico M. Bandi, Yinan Su",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T04:00:00+00:00",
    "summary": "arXiv:2607.12156v3 Announce Type: replace Abstract: Compute (computing power) is a scarce, capital-intensive input at the center of the AI economy. Compute capital expenditure and service flow already"
  },
  {
    "id": "rss:https://arxiv.org/abs/2606.14887",
    "domain": "金融",
    "title": "Estimating Sloppy Directions via KDE: The Case of Kirman's Ants",
    "url": "https://arxiv.org/abs/2606.14887",
    "source": "Karl Naumann-Woleske",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T04:00:00+00:00",
    "summary": "arXiv:2606.14887v2 Announce Type: replace-cross Abstract: Models whose predictions depend on only a handful of well-constrained parameter combinations, termed sloppy models, are ubiquitous in nonlinea"
  },
  {
    "id": "rss:https://arxiv.org/abs/2608.00045",
    "domain": "金融",
    "title": "Predicting Startup Exit from Textual Descriptors - A Computational Linguistics Framework",
    "url": "https://arxiv.org/abs/2608.00045",
    "source": "Alberto M. G. Saruggia, Sebastien Germano",
    "platform": "rss",
    "points": null,
    "published_at": "2026-09-11T04:00:00+00:00",
    "summary": "arXiv:2608.00045v3 Announce Type: replace-cross Abstract: This study shows that textual descriptors alone can predict early-stage startup success, defined as Exit, without relying on contextual, finan"
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
